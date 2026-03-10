"""
Supervisor Agent

Orchestrates tools and agents via LLM function calling.
The supervisor decides which tools/agents to call and synthesizes final results.

Supports two modes:
- Tool mode (legacy): Direct tool execution
- Agent mode: Delegation to specialized research agents
"""

import time
from typing import Any, Dict, List, Optional, Literal, Union, TYPE_CHECKING

from pydantic import BaseModel, Field

from deepsearch.tools import ToolRegistry, BaseTool
from deepsearch.agents import AgentRegistry, BaseAgent
from deepsearch.models import (
    ToolResult,
    ToolCallRecord,
    DRIteration,
    DRResult,
    searchAnswer,
    QualityAssessment,
    QualityScore,
    AgentResult,
    ResearchFinding,
    FindingSource,
)
from deepsearch.observability import (
    get_logger,
    set_user_query,
    TracingContext,
    SpanKind,
    add_span_attributes,
    add_span_event,
)

if TYPE_CHECKING:
    from deepsearch.llm import LLMProvider, LLMMessage
    from deepsearch.prompts import PromptManager
    from deepsearch.api.models import ConversationMessage
    from deepsearch.api.streaming import EventStream

logger = get_logger(__name__)


# Query type to report template mapping
QUERY_TYPE_TEMPLATE_MAP = {
    "FACTUAL_LOOKUP": "generate_report_factual",
    "TROUBLESHOOTING": "generate_report_troubleshooting",
    "PROCEDURAL": "generate_report_procedural",
    "SPECIFICATION_COMPARISON": "generate_report_comparison",
    "CONCEPTUAL": "generate_report",  # Use default for explanations
    "MULTI_PART": "generate_report",  # Use default for complex queries
}


class QueryClassification(BaseModel):
    """Classification of user query for format selection."""

    query_type: str = Field(
        default="CONCEPTUAL",
        description="Type of query: FACTUAL_LOOKUP, TROUBLESHOOTING, PROCEDURAL, SPECIFICATION_COMPARISON, CONCEPTUAL, MULTI_PART",
    )
    complexity: str = Field(
        default="MEDIUM", description="Complexity level: SIMPLE, MEDIUM, COMPLEX"
    )
    format_hint: str = Field(
        default="", description="Suggested output format structure"
    )


class SupervisorConfig(BaseModel):
    """Configuration for the supervisor agent."""

    execution_strategy: Literal["iterative", "parallel"] = Field(
        default="iterative",
        description="How to execute tools/agents: iterative (one at a time) or parallel",
    )
    max_iterations: int = Field(
        default=3, ge=1, le=10, description="Maximum search iterations"
    )
    quality_threshold: float = Field(
        default=0.7, ge=0.0, le=1.0, description="Quality threshold for early stopping"
    )
    generate_report: bool = Field(
        default=True, description="Whether to generate final report"
    )
    generate_concise_answer: bool = Field(
        default=True, description="Whether to generate concise answer"
    )
    use_agents: bool = Field(
        default=True,
        description="Use agent delegation (True) or direct tools (False)",
    )
    parallel_agents: bool = Field(
        default=True,
        description="Execute multiple agents in parallel when possible",
    )
    search_timeout_seconds: float = Field(
        default=120.0,
        ge=5.0,
        le=600.0,
        description="Total timeout for search operation in seconds",
    )
    tool_timeout_seconds: float = Field(
        default=60.0,
        ge=5.0,
        le=300.0,
        description="Timeout for individual tool/agent execution in seconds",
    )
    report_max_tokens: int = Field(
        default=4000,
        ge=500,
        le=8000,
        description="Maximum tokens for final report generation",
    )


class SupervisorAgent:
    """
    Orchestrates tools and specialized agents via LLM function calling.

    The supervisor:
    1. Receives a query from the user
    2. Decides which tools/agents to call (via LLM function calling)
    3. Executes tools directly OR delegates to specialized agents
    4. Assesses quality and decides to continue or complete
    5. Generates final report and concise answer

    Supports two modes:
    - Agent mode (default): Delegates to specialized research agents
    - Tool mode: Direct tool execution (legacy/fallback)
    """

    def __init__(
        self,
        llm: "LLMProvider",
        prompts: "PromptManager",
        config: Optional[SupervisorConfig] = None,
        tools: Optional[List[BaseTool]] = None,
        agents: Optional[List[BaseAgent]] = None,
        stream: Optional["EventStream"] = None,
    ):
        """
        Initialize the supervisor.

        Args:
            llm: LLM provider for decision making
            prompts: PromptManager for loading prompts
            config: Supervisor configuration
            tools: Specific tools to use (defaults to all registered)
            agents: Specific agents to use (defaults to all registered)
            stream: Optional EventStream for real-time progress events
        """
        self.llm = llm
        self.prompts = prompts
        self.config = config or SupervisorConfig()
        self._tools = tools  # If None, will use ToolRegistry
        self._agents = agents  # If None, will use AgentRegistry
        self._stream = stream  # For SSE event streaming
        self._active_stream = None  # Set per-search in search() method

        logger.info(
            "supervisor_init",
            strategy=self.config.execution_strategy,
            max_iterations=self.config.max_iterations,
            use_agents=self.config.use_agents,
        )

    @property
    def tools(self) -> List[BaseTool]:
        """Get available tools."""
        if self._tools is not None:
            return self._tools
        return ToolRegistry.all_tools()

    @property
    def agents(self) -> List[BaseAgent]:
        """Get available agents."""
        if self._agents is not None:
            return self._agents
        return AgentRegistry.all_agents()

    def function_schemas(self) -> List[Dict[str, Any]]:
        """Get function calling schemas for tools OR agents."""
        if self.config.use_agents and self.agents:
            # Return agent delegation schemas (delegate_to_<agent>)
            return [agent.to_function_schema() for agent in self.agents]
        else:
            # Fallback to tool schemas
            return [tool.to_function_schema() for tool in self.tools]

    async def search(
        self,
        query: str,
        job_id: Optional[str] = None,
        conversation_history: Optional[List["ConversationMessage"]] = None,
        stream: Optional["EventStream"] = None,
    ) -> DRResult:
        """
        Execute the search workflow.

        Args:
            query: User query
            job_id: Optional job ID for tracking
            conversation_history: Optional conversation context for follow-up questions
            stream: Optional EventStream for real-time progress events (overrides init stream)

        Returns:
            DRResult with all iterations and final answer

        Raises:
            asyncio.TimeoutError: If search exceeds search_timeout_seconds
        """
        import asyncio
        from deepsearch.llm import LLMMessage

        # Use provided stream or fall back to init stream
        self._active_stream = stream or self._stream

        async with TracingContext(
            "supervisor.search",
            attributes={
                # OpenInference semantic conventions for Phoenix
                "openinference.span.kind": "CHAIN",
                "input.query": query[:500],
                "input.job_id": job_id or "",
                "input.has_history": bool(conversation_history),
                "input.streaming": self._active_stream is not None,
                "supervisor.strategy": self.config.execution_strategy,
                "supervisor.max_iterations": self.config.max_iterations,
                "supervisor.use_agents": self.config.use_agents,
            },
        ) as span:
            start_time = time.time()
            set_user_query(query)

            logger.info(
                "search_start",
                query=query[:100],
                job_id=job_id,
                has_history=bool(conversation_history),
                history_length=len(conversation_history) if conversation_history else 0,
            )

            iterations: List[DRIteration] = []
            classification: Optional[QueryClassification] = None

            try:
                # Apply overall search timeout
                async with asyncio.timeout(self.config.search_timeout_seconds):
                    # Classify query first to determine output format
                    classification = await self._classify_query(query)
                    span.set_attribute("query.type", classification.query_type)
                    span.set_attribute("query.complexity", classification.complexity)

                    # Execute iterations
                    if self.config.execution_strategy == "iterative":
                        iterations = await self._iterative_search(
                            query, conversation_history, classification
                        )
                    else:
                        iterations = await self._parallel_search(query)
            except asyncio.TimeoutError:
                logger.error(
                    "search_timeout",
                    query=query[:100],
                    timeout_seconds=self.config.search_timeout_seconds,
                    iterations_completed=len(iterations),
                )
                span.set_attribute("error.type", "timeout")
                raise

            # Collect all findings from all iterations
            all_findings: List[ResearchFinding] = []
            for iteration in iterations:
                all_findings.extend(iteration.all_findings)

            # Generate final outputs
            final_report = ""
            concise_answer = ""

            # Emit thinking event for report generation
            if self._active_stream and self.config.generate_report and all_findings:
                await self._active_stream.progress(
                    "generating_report",
                    "Generating final report..."
                )

            if self.config.generate_report and all_findings:
                final_report = await self._generate_report(query, all_findings, classification)

            if self.config.generate_concise_answer and all_findings:
                concise_answer = await self._generate_concise_answer(
                    query, all_findings
                )

            # Calculate confidence
            confidence = self._calculate_confidence(iterations)

            processing_time = (time.time() - start_time) * 1000

            result = DRResult(
                user_query=query,
                iterations=iterations,
                final_report=final_report,
                concise_answer=concise_answer,
                confidence_score=confidence,
                total_iterations=len(iterations),
                processing_time_ms=processing_time,
                job_id=job_id,
            )

            # Add output attributes to span
            span.set_attribute("output.iterations_count", len(iterations))
            span.set_attribute("output.confidence_score", confidence)
            span.set_attribute("output.processing_time_ms", processing_time)
            span.set_attribute("output.findings_count", len(all_findings))

            logger.info(
                "search_complete",
                iterations=len(iterations),
                confidence=confidence,
                duration_ms=processing_time,
            )

        return result

    def _format_conversation_history(
        self, history: Optional[List["ConversationMessage"]]
    ) -> str:
        """Format conversation history for LLM context.

        Args:
            history: List of previous messages

        Returns:
            Formatted string for inclusion in prompts
        """
        if not history:
            return ""

        formatted_parts = []
        for msg in history:
            role_label = "User" if msg.role == "user" else "Assistant"
            content = msg.content

            # Add sources info for assistant messages
            if msg.role == "assistant" and msg.sources:
                sources_str = ", ".join(f'"{s}"' for s in msg.sources[:5])
                if len(msg.sources) > 5:
                    sources_str += f" (+{len(msg.sources) - 5} more)"
                content = f"{content}\n[Sources: {sources_str}]"

            formatted_parts.append(f"{role_label}: {content}")

        return "\n---\n".join(formatted_parts)

    async def _classify_query(self, query: str) -> QueryClassification:
        """Classify query type to determine output format and research budget.

        Args:
            query: User query to classify

        Returns:
            QueryClassification with type, complexity, and format hint
        """
        from deepsearch.llm import LLMMessage
        import re

        async with TracingContext(
            "supervisor.classify_query",
            attributes={"input.query": query[:200]},
        ) as span:
            try:
                prompt = self.prompts.get_prompt(
                    "supervisor",
                    "classify_query",
                    query=query,
                )

                response = await self.llm.complete(
                    messages=[LLMMessage.user(prompt)],
                    temperature=0.1,
                    max_tokens=200,
                )

                # Parse response
                text = response.content

                query_type = "CONCEPTUAL"
                type_match = re.search(
                    r"TYPE:\s*(FACTUAL_LOOKUP|TROUBLESHOOTING|SPECIFICATION_COMPARISON|PROCEDURAL|CONCEPTUAL|MULTI_PART)",
                    text,
                    re.IGNORECASE,
                )
                if type_match:
                    query_type = type_match.group(1).upper()

                complexity = "MEDIUM"
                complexity_match = re.search(
                    r"COMPLEXITY:\s*(SIMPLE|MEDIUM|COMPLEX)", text, re.IGNORECASE
                )
                if complexity_match:
                    complexity = complexity_match.group(1).upper()

                format_hint = ""
                hint_match = re.search(r"FORMAT_HINT:\s*(.+?)(?:\n|$)", text)
                if hint_match:
                    format_hint = hint_match.group(1).strip()

                classification = QueryClassification(
                    query_type=query_type,
                    complexity=complexity,
                    format_hint=format_hint,
                )

                span.set_attribute("output.query_type", query_type)
                span.set_attribute("output.complexity", complexity)

                logger.info(
                    "query_classified",
                    query_type=query_type,
                    complexity=complexity,
                    format_hint=format_hint[:50] if format_hint else "",
                )

                return classification

            except Exception as e:
                logger.warning("query_classification_failed", error=str(e))
                span.set_attribute("error", str(e))
                # Return default classification on failure
                return QueryClassification()

    async def _iterative_search(
        self,
        query: str,
        user_history: Optional[List["ConversationMessage"]] = None,
        classification: Optional[QueryClassification] = None,
    ) -> List[DRIteration]:
        """Execute search iteratively (one tool/agent at a time)."""
        import asyncio
        from deepsearch.llm import LLMMessage

        iterations = []
        llm_conversation = []

        # Use default classification if not provided
        if classification is None:
            classification = QueryClassification()

        # Build system prompt based on mode (agents vs tools)
        if self.config.use_agents and self.agents:
            agent_descriptions = "\n".join(
                f"- {a.name}: {a.description}" for a in self.agents
            )
            system_prompt = self.prompts.get_prompt(
                "supervisor",
                "system",
                agent_count=len(self.agents),
                agent_descriptions=agent_descriptions,
                tool_count=len(self.agents),  # For backwards compatibility
            )
        else:
            system_prompt = self.prompts.get_prompt(
                "supervisor",
                "system",
                tool_count=len(self.tools),
            )
        llm_conversation.append(LLMMessage.system(system_prompt))

        # Format conversation history if present
        history_context = self._format_conversation_history(user_history)

        # Initial user message with optional conversation context and classification
        if history_context:
            user_prompt = self.prompts.get_prompt(
                "supervisor",
                "search_query_with_history",
                query=query,
                conversation_history=history_context,
                query_type=classification.query_type,
                complexity=classification.complexity,
                format_hint=classification.format_hint or "Standard report format",
            )
        else:
            user_prompt = self.prompts.get_prompt(
                "supervisor",
                "search_query",
                query=query,
                query_type=classification.query_type,
                complexity=classification.complexity,
                format_hint=classification.format_hint or "Standard report format",
            )
        llm_conversation.append(LLMMessage.user(user_prompt))

        for iteration_num in range(1, self.config.max_iterations + 1):
            async with TracingContext(
                "supervisor.iteration",
                attributes={
                    "iteration.number": iteration_num,
                    "iteration.max": self.config.max_iterations,
                },
            ) as iteration_span:
                logger.info("iteration_start", iteration=iteration_num)

                iteration = DRIteration(iteration_number=iteration_num)
                tool_calls: List[ToolCallRecord] = []
                findings: List[ResearchFinding] = []

                # Emit thinking event for frontend
                if self._active_stream:
                    await self._active_stream.progress(
                        "analyzing",
                        f"Analyzing query (iteration {iteration_num})..."
                    )

                # Ask LLM which tool/agent to call (supervisor decision)
                functions = self.function_schemas()

                # Extract system prompt for tracing
                system_prompt = next(
                    (m.content for m in llm_conversation if m.role == "system"), None
                )

                async with TracingContext(
                    "supervisor.llm.decision",
                    span_kind=SpanKind.CLIENT,
                    attributes={
                        # OpenInference semantic conventions for Phoenix
                        "openinference.span.kind": "LLM",
                        "llm.model_name": self.llm.model if hasattr(self.llm, 'model') else "unknown",
                        "input.conversation_length": len(llm_conversation),
                    },
                ) as decision_span:
                    # OpenInference semantic convention attributes for Phoenix Info tab
                    from openinference.semconv.trace import SpanAttributes, OpenInferenceSpanKindValues
                    decision_span.set_attribute(SpanAttributes.OPENINFERENCE_SPAN_KIND, OpenInferenceSpanKindValues.LLM.value)

                    # Use indexed format for messages
                    for i, m in enumerate(llm_conversation):
                        decision_span.set_attribute(f"llm.input_messages.{i}.message.role", m.role)
                        decision_span.set_attribute(f"llm.input_messages.{i}.message.content", m.content[:4000])

                    # Add function names
                    decision_span.set_attribute(
                        "input.function_names",
                        str([f.get("function", {}).get("name", "") for f in functions])
                    )

                    # Add granular function attributes for Phoenix visibility
                    for func in functions:
                        func_def = func.get("function", {})
                        func_name = func_def.get("name", "unknown")
                        decision_span.set_attribute(
                            f"input.function.{func_name}.description",
                            func_def.get("description", "")
                        )
                        # Add parameter descriptions
                        params = func_def.get("parameters", {}).get("properties", {})
                        for param_name, param_def in params.items():
                            decision_span.set_attribute(
                                f"input.function.{func_name}.parameters.{param_name}.description",
                                param_def.get("description", "")
                            )
                            decision_span.set_attribute(
                                f"input.function.{func_name}.parameters.{param_name}.type",
                                param_def.get("type", "")
                            )

                    response = await self.llm.complete_with_functions(
                        messages=llm_conversation,
                        functions=functions,
                        temperature=0.2,
                    )

                    # Add output attributes with OpenInference indexed format
                    output_content = response.content or ""
                    if response.function_call:
                        output_content = f"Function call: {response.function_call.name}({response.function_call.arguments})"

                    decision_span.set_attribute("llm.output_messages.0.message.role", "assistant")
                    decision_span.set_attribute("llm.output_messages.0.message.content", output_content[:4000])

                    if response.function_call:
                        decision_span.set_attribute("llm.output_messages.0.message.tool_calls.0.tool_call.function.name", response.function_call.name)
                        decision_span.set_attribute("llm.output_messages.0.message.tool_calls.0.tool_call.function.arguments", str(response.function_call.arguments))

                if response.function_call:
                    func_name = response.function_call.name
                    func_args = response.function_call.arguments

                    call_start = time.time()

                    # Check if this is an agent delegation
                    if func_name.startswith("delegate_to_"):
                        agent = self._get_agent(func_name)
                        if agent:
                            # Execute agent with timeout - extract task and filter it from kwargs
                            task = func_args.get("task", func_args.get("query", query))
                            extra_kwargs = {
                                k: v
                                for k, v in func_args.items()
                                if k not in ("task", "query")
                            }

                            # Wrap agent execution in tracing span
                            async with TracingContext(
                                f"supervisor.delegate_to_{agent.name}",
                                attributes={
                                    "agent.name": agent.name,
                                    "agent.description": (
                                        agent.description[:200]
                                        if agent.description
                                        else None
                                    ),
                                    "agent.tool_names": [t.name for t in agent.tools],
                                    "input.task": task[:300] if task else None,
                                },
                            ) as delegation_span:
                                # Emit agent starting event
                                if self._active_stream:
                                    await self._active_stream.agent_status(
                                        iteration_number=iteration_num,
                                        agent_name=func_name,
                                        status="searching",
                                        search_query=task[:200] if task else None,
                                        display_name=agent.display_name,
                                        icon_url=agent.icon_url,
                                        searching_label=agent.searching_label,
                                        item_label=agent.item_label,
                                    )

                                try:
                                    async with asyncio.timeout(
                                        self.config.tool_timeout_seconds
                                    ):
                                        agent_result = await agent.run(
                                            task, **extra_kwargs
                                        )
                                except asyncio.TimeoutError:
                                    logger.warning(
                                        "agent_timeout",
                                        agent=func_name,
                                        timeout_seconds=self.config.tool_timeout_seconds,
                                    )
                                    agent_result = AgentResult(
                                        success=False,
                                        agent_name=func_name,
                                        task=task,
                                        answer="",
                                        confidence=0.0,
                                        error=f"Agent timed out after {self.config.tool_timeout_seconds}s",
                                    )

                                # Add output attributes to delegation span
                                delegation_span.set_attribute(
                                    "output.success", agent_result.success
                                )
                                delegation_span.set_attribute(
                                    "output.confidence", agent_result.confidence
                                )
                                delegation_span.set_attribute(
                                    "output.sources_count",
                                    (
                                        len(agent_result.sources)
                                        if agent_result.sources
                                        else 0
                                    ),
                                )

                            call_duration = (time.time() - call_start) * 1000

                            tool_calls.append(
                                ToolCallRecord(
                                    tool_name=func_name,
                                    arguments=func_args,
                                    result=(
                                        agent_result if agent_result.success else None
                                    ),
                                    success=agent_result.success,
                                    error=agent_result.error,
                                    duration_ms=call_duration,
                                )
                            )

                            # Convert AgentResult to ResearchFinding (unified model)
                            finding = ResearchFinding.from_agent_result(agent_result)
                            findings.append(finding)

                            # Emit agent completed event
                            if self._active_stream:
                                await self._active_stream.agent_status(
                                    iteration_number=iteration_num,
                                    agent_name=func_name,
                                    status="done",
                                    results_count=(
                                        len(agent_result.sources)
                                        if agent_result.success
                                        else 0
                                    ),
                                    display_name=agent.display_name,
                                    icon_url=agent.icon_url,
                                    searching_label=agent.searching_label,
                                    item_label=agent.item_label,
                                )

                            # Add result to conversation
                            result_text = self._format_agent_result(agent_result)
                            llm_conversation.append(
                                LLMMessage.function(func_name, result_text)
                            )
                        else:
                            logger.warning("agent_not_found", name=func_name)
                            llm_conversation.append(
                                LLMMessage.function(
                                    func_name, f"Agent not found: {func_name}"
                                )
                            )
                    else:
                        # Execute tool directly (fallback/legacy mode) with timeout
                        tool = self._get_tool(func_name)
                        if tool:
                            tool_query = func_args.get("query", query)

                            # Emit tool starting event
                            if self._active_stream:
                                await self._active_stream.agent_status(
                                    iteration_number=iteration_num,
                                    agent_name=func_name,
                                    status="searching",
                                    search_query=(
                                        tool_query[:200] if tool_query else None
                                    ),
                                    display_name=None,  # Tools don't have display metadata
                                    icon_url=None,
                                )

                            try:
                                async with asyncio.timeout(
                                    self.config.tool_timeout_seconds
                                ):
                                    result = await tool.execute(
                                        query=tool_query,
                                        **{
                                            k: v
                                            for k, v in func_args.items()
                                            if k != "query"
                                        },
                                    )
                            except asyncio.TimeoutError:
                                logger.warning(
                                    "tool_timeout",
                                    tool=func_name,
                                    timeout_seconds=self.config.tool_timeout_seconds,
                                )
                                result = ToolResult.fail(
                                    f"Tool timed out after {self.config.tool_timeout_seconds}s"
                                )
                            call_duration = (time.time() - call_start) * 1000

                            tool_calls.append(
                                ToolCallRecord(
                                    tool_name=func_name,
                                    arguments=func_args,
                                    result=result.data if result.success else None,
                                    success=result.success,
                                    error=result.error,
                                    duration_ms=call_duration,
                                )
                            )

                            # Convert ToolResult to ResearchFinding (unified model)
                            finding = ResearchFinding.from_tool_result(
                                result, func_name, call_duration
                            )
                            findings.append(finding)

                            # Emit tool completed event
                            if self._active_stream:
                                # Try to get results count from tool result
                                results_count = 0
                                if result.success and result.data:
                                    if isinstance(result.data, dict):
                                        results_count = len(
                                            result.data.get(
                                                "sources",
                                                result.data.get("results", []),
                                            )
                                        )
                                    elif hasattr(result.data, "sources"):
                                        results_count = len(result.data.sources)
                                    elif hasattr(result.data, "results"):
                                        results_count = len(result.data.results)
                                await self._active_stream.agent_status(
                                    iteration_number=iteration_num,
                                    agent_name=func_name,
                                    status="done",
                                    results_count=results_count,
                                    display_name=None,  # Tools don't have display metadata
                                    icon_url=None,
                                )

                            # Add tool result to conversation
                            result_text = self._format_tool_result(result)
                            llm_conversation.append(
                                LLMMessage.function(func_name, result_text)
                            )
                        else:
                            logger.warning("tool_not_found", name=func_name)
                            llm_conversation.append(
                                LLMMessage.function(
                                    func_name, f"Tool not found: {func_name}"
                                )
                            )

                else:
                    # LLM chose not to call anything - it's ready to answer
                    logger.info("no_function_call", iteration=iteration_num)
                    iteration.supervisor_decision = "COMPLETE"
                    iteration.supervisor_reasoning = "LLM provided direct answer"
                    iterations.append(iteration)
                    break

                # Assess quality and decide next step
                successful_findings = [f for f in findings if f.success]
                if successful_findings:
                    assessment = await self._assess_quality_finding(
                        query, successful_findings[-1]
                    )
                    iteration.quality_assessment = assessment

                    if assessment.score >= QualityScore.GOOD:
                        iteration.supervisor_decision = "COMPLETE"
                        iteration.supervisor_reasoning = (
                            f"Quality score {assessment.score.name} meets threshold"
                        )
                    else:
                        iteration.supervisor_decision = "CONTINUE"
                        iteration.supervisor_reasoning = (
                            f"Quality score {assessment.score.name} below threshold"
                        )

                iteration.tool_calls = tool_calls
                iteration.findings = findings  # Use new unified findings field
                iterations.append(iteration)

                # Emit iteration complete event
                if self._active_stream:
                    tools_called = [tc.tool_name for tc in tool_calls]
                    await self._active_stream.iteration(
                        number=iteration_num,
                        tools_called=tools_called,
                        decision=iteration.supervisor_decision,
                    )

                # Set iteration span attributes
                iteration_span.set_attribute(
                    "output.decision", iteration.supervisor_decision or "UNKNOWN"
                )
                iteration_span.set_attribute("output.tool_calls_count", len(tool_calls))
                iteration_span.set_attribute("output.findings_count", len(findings))

                # Early stop check
                if iteration.supervisor_decision == "COMPLETE":
                    break

        return iterations

    async def _parallel_search(self, query: str) -> List[DRIteration]:
        """Execute search in parallel (all tools at once)."""
        import asyncio

        iteration = DRIteration(iteration_number=1)
        tool_calls: List[ToolCallRecord] = []
        findings: List[ResearchFinding] = []

        # Capture stream reference for inner function
        active_stream = self._active_stream

        # Execute all tools in parallel
        async def execute_tool(tool: BaseTool) -> tuple:
            """Execute tool and return (ToolCallRecord, ResearchFinding)."""
            # Emit tool starting event
            if active_stream:
                await active_stream.agent_status(
                    iteration_number=1,
                    agent_name=tool.name,
                    status="searching",
                    search_query=query[:200] if query else None,
                    display_name=None,  # Tools don't have display metadata
                    icon_url=None,
                )

            start = time.time()
            try:
                result = await tool.execute(query=query)
                duration = (time.time() - start) * 1000

                record = ToolCallRecord(
                    tool_name=tool.name,
                    arguments={"query": query},
                    result=result.data if result.success else None,
                    success=result.success,
                    error=result.error,
                    duration_ms=duration,
                )

                finding = ResearchFinding.from_tool_result(result, tool.name, duration)

                # Emit tool completed event
                if active_stream:
                    results_count = 0
                    if result.success and result.data:
                        if isinstance(result.data, dict):
                            results_count = len(
                                result.data.get(
                                    "sources", result.data.get("results", [])
                                )
                            )
                        elif hasattr(result.data, "sources"):
                            results_count = len(result.data.sources)
                        elif hasattr(result.data, "results"):
                            results_count = len(result.data.results)
                    await active_stream.agent_status(
                        iteration_number=1,
                        agent_name=tool.name,
                        status="done",
                        results_count=results_count,
                        display_name=None,  # Tools don't have display metadata
                        icon_url=None,
                    )

                return record, finding

            except Exception as e:
                duration = (time.time() - start) * 1000
                record = ToolCallRecord(
                    tool_name=tool.name,
                    arguments={"query": query},
                    success=False,
                    error=str(e),
                    duration_ms=duration,
                )
                finding = ResearchFinding.failure(
                    source_type=FindingSource.TOOL,
                    source_name=tool.name,
                    error=str(e),
                )

                # Emit tool completed event (with error)
                if active_stream:
                    await active_stream.agent_status(
                        iteration_number=1,
                        agent_name=tool.name,
                        status="done",
                        results_count=0,
                        display_name=None,  # Tools don't have display metadata
                        icon_url=None,
                    )

                return record, finding

        tasks = [execute_tool(tool) for tool in self.tools]
        results = await asyncio.gather(*tasks)

        for record, finding in results:
            tool_calls.append(record)
            findings.append(finding)

        iteration.tool_calls = tool_calls
        iteration.findings = findings
        iteration.supervisor_decision = "COMPLETE"
        iteration.supervisor_reasoning = "Parallel execution complete"

        # Emit iteration complete event
        if active_stream:
            await active_stream.iteration(
                number=1,
                tools_called=[t.name for t in self.tools],
                decision="COMPLETE",
            )

        return [iteration]

    def _get_tool(self, name: str) -> Optional[BaseTool]:
        """Get tool by name."""
        for tool in self.tools:
            if tool.name == name:
                return tool
        return ToolRegistry.get(name)

    def _get_agent(self, name: str) -> Optional[BaseAgent]:
        """Get agent by name (handles delegate_to_ prefix)."""
        # Strip the delegate_to_ prefix if present
        agent_name = name
        if name.startswith("delegate_to_"):
            agent_name = name[len("delegate_to_") :]

        for agent in self.agents:
            if agent.name == agent_name:
                return agent
        return AgentRegistry.get(agent_name)

    def _format_agent_result(self, result: AgentResult) -> str:
        """Format agent result for conversation."""
        if not result.success:
            return f"Agent error: {result.error}"

        sources_summary = (
            f"{len(result.sources)} sources" if result.sources else "no sources"
        )
        iterations_summary = f"{len(result.iterations)} iterations"

        return (
            f"Agent {result.agent_name} findings "
            f"(confidence: {result.confidence:.2f}, {sources_summary}, {iterations_summary}):\n"
            f"{result.answer}"
        )

    def _format_tool_result(self, result: ToolResult) -> str:
        """Format tool result for conversation."""
        if not result.success:
            return f"Error: {result.error}"

        if isinstance(result.data, searchAnswer):
            answer = result.data
            sources_summary = (
                f"{len(answer.sources)} sources" if answer.sources else "no sources"
            )
            return f"Answer (confidence: {answer.confidence:.2f}, {sources_summary}):\n{answer.answer}"

        return str(result.data)

    async def _assess_quality_finding(
        self,
        query: str,
        finding: ResearchFinding,
    ) -> QualityAssessment:
        """Assess quality of a research finding (unified model)."""
        from deepsearch.llm import LLMMessage

        async with TracingContext(
            "supervisor.quality_assessment",
            attributes={
                "input.finding_confidence": finding.confidence,
                "input.finding_sources_count": finding.sources_count,
            },
        ) as span:
            try:
                prompt = self.prompts.get_prompt(
                    "supervisor",
                    "assess_quality",
                    query=query,
                    answer=finding.answer[:2000],
                    sources_count=finding.sources_count,
                    confidence=finding.confidence,
                )

                response = await self.llm.complete(
                    messages=[LLMMessage.user(prompt)],
                    temperature=0.1,
                    max_tokens=500,
                )

                assessment = self._parse_quality_assessment(response.content)
                span.set_attribute("output.score", assessment.score.name)
                span.set_attribute(
                    "output.factual_accuracy", assessment.factual_accuracy
                )
                return assessment

            except Exception as e:
                logger.error("quality_assessment_failed", error=str(e))
                span.set_attribute("error", str(e))
                return QualityAssessment(
                    score=QualityScore.ADEQUATE,
                    reasoning="Assessment failed, using default",
                    contributes_to_answer=True,
                    addresses_user_question=True,
                    factual_accuracy=0.5,
                    completeness=0.5,
                )

    def _parse_quality_assessment(self, text: str) -> QualityAssessment:
        """Parse LLM quality assessment response."""
        import re

        # Extract score
        score = QualityScore.ADEQUATE
        score_match = re.search(r"SCORE:\s*(\d)", text)
        if score_match:
            score_val = int(score_match.group(1))
            score = QualityScore(max(1, min(5, score_val)))

        # Extract other fields
        contributes = "YES" in text.upper() and "CONTRIBUTES" in text.upper()
        addresses = "ADDRESSES" in text.upper() and "YES" in text.upper()

        factual = 0.5
        factual_match = re.search(r"FACTUAL_ACCURACY:\s*([\d.]+)", text)
        if factual_match:
            factual = float(factual_match.group(1))

        completeness = 0.5
        complete_match = re.search(r"COMPLETENESS:\s*([\d.]+)", text)
        if complete_match:
            completeness = float(complete_match.group(1))

        reasoning = ""
        reasoning_match = re.search(r"REASONING:\s*(.+)", text, re.DOTALL)
        if reasoning_match:
            reasoning = reasoning_match.group(1).strip()[:500]

        return QualityAssessment(
            score=score,
            reasoning=reasoning or "Assessment parsed",
            contributes_to_answer=contributes,
            addresses_user_question=addresses,
            factual_accuracy=factual,
            completeness=completeness,
        )

    async def _generate_report(
        self,
        query: str,
        findings: List[ResearchFinding],
        classification: Optional[QueryClassification] = None,
    ) -> str:
        """Generate final structured report from research findings.

        Uses format-specific templates based on query classification:
        - FACTUAL_LOOKUP: Brief, direct answer
        - TROUBLESHOOTING: Causes + solutions + escalation
        - PROCEDURAL: Prerequisites + numbered steps + verification
        - SPECIFICATION_COMPARISON: Table format with summary
        - CONCEPTUAL/MULTI_PART: Default comprehensive report
        """
        from deepsearch.llm import LLMMessage

        # Determine which template to use
        if classification:
            template_name = QUERY_TYPE_TEMPLATE_MAP.get(
                classification.query_type, "generate_report"
            )
        else:
            template_name = "generate_report"

        async with TracingContext(
            "supervisor.generate_report",
            attributes={
                "input.findings_count": len(findings),
                "input.total_sources": sum(f.sources_count for f in findings),
                "input.template": template_name,
                "input.query_type": classification.query_type if classification else "unknown",
            },
        ) as span:
            try:
                # Combine all findings
                combined = "\n\n---\n\n".join(
                    f"**{f.source_name}** ({f.source_type.value}, confidence: {f.confidence:.2f}):\n{f.answer}"
                    for f in findings
                )

                # Try to get the format-specific template, fall back to default
                try:
                    prompt = self.prompts.get_prompt(
                        "supervisor",
                        template_name,
                        query=query,
                        search_findings=combined,
                        sources_count=sum(f.sources_count for f in findings),
                    )
                    logger.info(
                        "report_template_selected",
                        template=template_name,
                        query_type=classification.query_type if classification else "default",
                    )
                except Exception as template_error:
                    # Fall back to default template if specific one doesn't exist
                    logger.warning(
                        "report_template_fallback",
                        requested=template_name,
                        error=str(template_error),
                    )
                    prompt = self.prompts.get_prompt(
                        "supervisor",
                        "generate_report",
                        query=query,
                        search_findings=combined,
                        sources_count=sum(f.sources_count for f in findings),
                    )

                # Use streaming if we have an active stream and LLM supports it
                has_stream = self._active_stream is not None
                has_streaming_method = hasattr(self.llm, 'complete_streaming')
                logger.info(
                    "report_streaming_decision",
                    has_stream=has_stream,
                    has_streaming_method=has_streaming_method,
                    will_stream=has_stream and has_streaming_method,
                )

                if has_stream and has_streaming_method:
                    try:
                        logger.info("report_streaming_start")
                        report_parts = []
                        chunk_count = 0
                        async for chunk in self.llm.complete_streaming(
                            messages=[LLMMessage.user(prompt)],
                            temperature=0.3,
                            max_tokens=self.config.report_max_tokens,
                        ):
                            chunk_count += 1
                            logger.debug("report_chunk_received", chunk_num=chunk_count, length=len(chunk))
                            await self._active_stream.report_chunk(chunk)
                            report_parts.append(chunk)
                        report = "".join(report_parts)
                        logger.info("report_streaming_complete", chunks=chunk_count, length=len(report))
                        span.set_attribute("output.report_length", len(report))
                        return report
                    except Exception as stream_error:
                        import traceback
                        logger.error(
                            "report_streaming_failed",
                            error=str(stream_error),
                            traceback=traceback.format_exc(),
                        )
                        # Fall through to non-streaming

                # Fallback to non-streaming
                logger.info("report_using_non_streaming")
                response = await self.llm.complete(
                    messages=[LLMMessage.user(prompt)],
                    temperature=0.3,
                    max_tokens=self.config.report_max_tokens,
                )
                span.set_attribute("output.report_length", len(response.content))
                return response.content

            except Exception as e:
                logger.error("report_generation_failed", error=str(e))
                span.set_attribute("error", str(e))
                return f"Report generation failed: {e}"

    async def _generate_concise_answer(
        self,
        query: str,
        findings: List[ResearchFinding],
    ) -> str:
        """Generate brief concise answer from research findings."""
        from deepsearch.llm import LLMMessage

        async with TracingContext(
            "supervisor.generate_concise_answer",
            attributes={"input.findings_count": len(findings)},
        ) as span:
            try:
                # Use best finding as primary source
                best_finding = (
                    max(findings, key=lambda f: f.confidence) if findings else None
                )
                if not best_finding:
                    span.set_attribute("output.skipped", True)
                    return ""

                span.set_attribute(
                    "input.best_finding_confidence", best_finding.confidence
                )

                prompt = self.prompts.get_prompt(
                    "supervisor",
                    "generate_concise_answer",
                    query=query,
                    search_summary=best_finding.answer[:1500],
                    max_sentences=4,
                )

                response = await self.llm.complete(
                    messages=[LLMMessage.user(prompt)],
                    temperature=0.2,
                    max_tokens=300,
                )

                span.set_attribute("output.answer_length", len(response.content))
                return response.content

            except Exception as e:
                logger.error("concise_answer_failed", error=str(e))
                span.set_attribute("error", str(e))
                return ""

    def _calculate_confidence(self, iterations: List[DRIteration]) -> float:
        """Calculate overall confidence from iterations using all findings."""
        if not iterations:
            return 0.0

        all_confidences = []
        for iteration in iterations:
            # Use all_findings to include both new findings and legacy search_answers
            for finding in iteration.all_findings:
                all_confidences.append(finding.confidence)

            if iteration.quality_assessment:
                all_confidences.append(iteration.quality_assessment.factual_accuracy)

        if not all_confidences:
            return 0.0

        return sum(all_confidences) / len(all_confidences)
