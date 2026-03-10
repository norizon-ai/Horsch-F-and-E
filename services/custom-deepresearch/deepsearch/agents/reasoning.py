"""
Reasoning Agent Mixin

Provides a common reasoning loop implementation for agents.
Agents that inherit from this mixin get a ReAct-style reasoning loop.
"""

import time
from typing import Any, List, Optional, TYPE_CHECKING

from deepsearch.models.agent import AgentResult, AgentIteration, AgentToolCall
from deepsearch.observability import get_logger, TracingContext, add_span_event, add_span_attributes

if TYPE_CHECKING:
    from deepsearch.llm import LLMMessage
    from deepsearch.models import ToolResult

logger = get_logger(__name__)


class ReasoningAgentMixin:
    """
    Mixin providing common reasoning loop implementation.

    Agents that inherit from both BaseAgent and this mixin get
    a standard ReAct-style reasoning loop with tool calling.

    The reasoning loop:
    1. Build system prompt with agent context
    2. Present task to LLM with available tools
    3. LLM chooses tool or provides answer
    4. Execute tool and add result to context
    5. Repeat until LLM signals completion or max iterations

    Usage:
        class MyAgent(BaseAgent, ReasoningAgentMixin):
            async def run(self, task: str, **kwargs) -> AgentResult:
                return await self.reasoning_loop(task, **kwargs)
    """

    async def reasoning_loop(
        self,
        task: str,
        context: Optional[str] = None,
        **kwargs,
    ) -> AgentResult:
        """
        Execute a standard reasoning loop.

        Args:
            task: The research task
            context: Optional additional context
            **kwargs: Additional parameters

        Returns:
            AgentResult with findings and sources
        """
        from deepsearch.llm import LLMMessage

        async with TracingContext(
            f"agent.{self.name}.reasoning_loop",
            attributes={
                "agent.name": self.name,
                "agent.max_iterations": self.max_iterations,
                "agent.tool_count": len(self.tools),
                "input.task": task[:300],
            },
        ) as loop_span:
            start_time = time.time()
            iterations: List[AgentIteration] = []
            all_sources = []
            conversation_history = []

            # Build system prompt
            system_prompt = self._build_system_prompt(task, context)
            conversation_history.append(LLMMessage.system(system_prompt))

            # Initial user message with task
            user_message = self._build_task_message(task, context)
            conversation_history.append(LLMMessage.user(user_message))

            logger.info(
                "reasoning_loop_start",
                agent=self.name,
                task=task[:100],
                max_iterations=self.max_iterations,
            )

            for iteration_num in range(1, self.max_iterations + 1):
                iteration = AgentIteration(iteration_number=iteration_num)
                add_span_event("agent_iteration_start", {
                    "iteration.number": iteration_num,
                    "agent.name": self.name,
                })

                logger.info(
                    "agent_iteration_start",
                    agent=self.name,
                    iteration=iteration_num,
                )

                # Ask LLM what to do
                try:
                    response = await self.llm.complete_with_functions(
                        messages=conversation_history,
                        functions=self._tool_schemas(),
                        temperature=0.3,
                    )
                except Exception as e:
                    logger.error(
                        "agent_llm_error",
                        agent=self.name,
                        iteration=iteration_num,
                        error=str(e),
                    )
                    # Return partial result on LLM failure
                    return AgentResult(
                        success=False,
                        agent_name=self.name,
                        task=task,
                        answer="",
                        confidence=0.0,
                        sources=all_sources,
                        iterations=iterations,
                        error=f"LLM error: {e}",
                        processing_time_ms=(time.time() - start_time) * 1000,
                    )

                if response.function_call:
                    # Execute the tool
                    tool_name = response.function_call.name
                    tool_args = response.function_call.arguments

                    iteration.thought = f"Using {tool_name} to gather information"

                    tool = self._get_tool(tool_name)
                    if tool:
                        call_start = time.time()
                        try:
                            result = await self._execute_tool(
                                tool=tool,
                                tool_args=tool_args,
                                task=task,
                            )
                            call_duration = (time.time() - call_start) * 1000

                            tool_call = AgentToolCall(
                                tool_name=tool_name,
                                arguments=tool_args,
                                result=result.data if result.success else None,
                                success=result.success,
                                error=result.error,
                                duration_ms=call_duration,
                            )
                            iteration.tool_calls.append(tool_call)

                            # Add span event for tool call
                            add_span_event("tool_call_complete", {
                                "tool.name": tool_name,
                                "tool.success": result.success,
                                "tool.duration_ms": call_duration,
                            })

                            # Collect sources if present
                            if result.success and hasattr(result.data, "sources"):
                                all_sources.extend(result.data.sources)
                            elif result.success and isinstance(result.data, dict):
                                if "sources" in result.data:
                                    all_sources.extend(result.data["sources"])
                                elif "results" in result.data:
                                    all_sources.extend(result.data["results"])

                            # Format result for conversation
                            result_text = self._format_tool_result(result)
                            iteration.observation = result_text

                            # Add to conversation
                            conversation_history.append(
                                LLMMessage.function(tool_name, result_text)
                            )

                            logger.info(
                                "agent_tool_call",
                                agent=self.name,
                                tool=tool_name,
                                success=result.success,
                                duration_ms=call_duration,
                            )

                        except Exception as e:
                            logger.error(
                                "tool_execution_error",
                                agent=self.name,
                                tool=tool_name,
                                error=str(e),
                            )
                            tool_call = AgentToolCall(
                                tool_name=tool_name,
                                arguments=tool_args,
                                success=False,
                                error=str(e),
                            )
                            iteration.tool_calls.append(tool_call)
                            iteration.observation = f"Error: {e}"
                            conversation_history.append(
                                LLMMessage.function(tool_name, f"Error: {e}")
                            )
                    else:
                        # Tool not found
                        logger.warning(
                            "tool_not_found",
                            agent=self.name,
                            tool=tool_name,
                        )
                        iteration.observation = f"Tool not found: {tool_name}"
                        conversation_history.append(
                            LLMMessage.function(tool_name, f"Tool not found: {tool_name}")
                        )

                    iteration.decision = "CONTINUE"

                else:
                    # LLM provided a direct answer - we're done
                    iteration.thought = "Synthesizing findings"
                    iteration.decision = "COMPLETE"
                    iterations.append(iteration)

                    # Extract the final answer
                    answer = response.content
                    confidence = self._estimate_confidence(answer, all_sources)

                    processing_time = (time.time() - start_time) * 1000

                    # Add final attributes to span
                    loop_span.set_attribute("output.success", True)
                    loop_span.set_attribute("output.iterations_count", len(iterations))
                    loop_span.set_attribute("output.sources_count", len(all_sources))
                    loop_span.set_attribute("output.confidence", confidence)

                    logger.info(
                        "reasoning_loop_complete",
                        agent=self.name,
                        iterations=len(iterations),
                        sources=len(all_sources),
                        confidence=confidence,
                        duration_ms=processing_time,
                    )

                    return AgentResult.ok(
                        agent_name=self.name,
                        task=task,
                        answer=answer,
                        confidence=confidence,
                        sources=all_sources,
                        iterations=iterations,
                        processing_time_ms=processing_time,
                    )

                iterations.append(iteration)

            # Max iterations reached - synthesize what we have
            logger.info(
                "max_iterations_reached",
                agent=self.name,
                iterations=self.max_iterations,
            )

            final_answer = await self._synthesize_findings(
                task, iterations, all_sources, conversation_history
            )

            processing_time = (time.time() - start_time) * 1000

            # Add final attributes to span
            loop_span.set_attribute("output.success", True)
            loop_span.set_attribute("output.iterations_count", len(iterations))
            loop_span.set_attribute("output.sources_count", len(all_sources))
            loop_span.set_attribute("output.max_iterations_reached", True)

            return AgentResult.ok(
                agent_name=self.name,
                task=task,
                answer=final_answer,
                confidence=self._estimate_confidence(final_answer, all_sources),
                sources=all_sources,
                iterations=iterations,
                processing_time_ms=processing_time,
                metadata={"max_iterations_reached": True},
            )

    async def _execute_tool(
        self,
        tool: Any,
        tool_args: dict,
        task: str,
    ) -> "ToolResult":
        """
        Execute a tool with the given arguments.

        Override this method to add preprocessing or other logic
        before tool execution.

        Args:
            tool: The tool instance to execute
            tool_args: Arguments from the LLM function call
            task: The original task (used as fallback for query)

        Returns:
            ToolResult from tool execution
        """
        return await tool.execute(
            query=tool_args.get("query", task),
            **{k: v for k, v in tool_args.items() if k != "query"},
        )

    def _build_system_prompt(self, task: str, context: Optional[str]) -> str:
        """Build the system prompt for the reasoning loop."""
        try:
            return self.prompts.get_prompt(
                self.prompt_category,
                "system",
                agent_name=self.name,
                tool_count=len(self.tools),
                tool_names=", ".join(t.name for t in self.tools),
            )
        except Exception:
            # Fallback if prompt not found
            tool_list = "\n".join(f"- {t.name}: {t.description}" for t in self.tools)
            return f"""You are {self.name}, a specialized research agent.

You have {len(self.tools)} tools available:
{tool_list}

Use them to accomplish the research task given to you.
When you have gathered enough information, provide your answer directly
without calling any more tools. Always cite your sources."""

    def _build_task_message(self, task: str, context: Optional[str]) -> str:
        """Build the task message for the user."""
        if context:
            return f"Research task: {task}\n\nContext:\n{context}"
        return f"Research task: {task}"

    def _format_tool_result(self, result: "ToolResult") -> str:
        """Format tool result for conversation history with document content."""
        if not result.success:
            return f"Error: {result.error}"

        data = result.data

        # Handle searchAnswer type (from retriever)
        if hasattr(data, "answer"):
            sources_summary = (
                f"{len(data.sources)} sources"
                if hasattr(data, "sources") and data.sources
                else "no sources"
            )
            return f"Found ({sources_summary}):\n{data.answer}"

        # Handle dict with results (from Elasticsearch tool)
        if isinstance(data, dict):
            if "results" in data:
                results = data["results"]
                if results:
                    # Include document content, not just titles
                    summary = f"Found {len(results)} results:\n\n"
                    for i, r in enumerate(results[:8], 1):  # Show top 8 for better completeness
                        # Extract title
                        if hasattr(r, "title"):
                            title = r.title
                        elif isinstance(r, dict) and "title" in r:
                            title = r["title"]
                        else:
                            title = "Untitled"

                        # Extract content
                        if hasattr(r, "content"):
                            content = r.content
                        elif isinstance(r, dict) and "content" in r:
                            content = r["content"]
                        else:
                            content = ""

                        # Truncate content to reasonable size for LLM context
                        # 3000 chars per doc × 8 docs = ~24k chars, well within context limits
                        content_preview = content[:3000] if content else "[No content]"
                        if len(content) > 3000:
                            content_preview += "..."

                        summary += f"--- Document {i}: {title} ---\n"
                        summary += f"{content_preview}\n\n"

                    return summary
            if "content" in data:
                return f"Content:\n{data['content'][:2000]}"

        return str(data)[:2000]

    def _estimate_confidence(self, answer: str, sources: list) -> float:
        """Estimate confidence with better heuristics based on content analysis."""
        import re

        if not answer or len(answer.strip()) < 20:
            return 0.1

        # Start with reasonable base confidence
        base_confidence = 0.4

        # Boost for sources (up to 0.3 for 5+ sources)
        if sources:
            base_confidence += min(0.3, len(sources) * 0.06)

        # Boost for specific content (measurements, codes, citations)
        specificity_patterns = [
            r'\d+\s*(kg|mm|cm|m|°C|bar|V|A|Hz|kW)',  # Measurements
            r'[A-Z]{2,4}-\d{3,}',  # Product codes
            r'\[\d+\]',  # Citations
        ]
        for pattern in specificity_patterns:
            if re.search(pattern, answer):
                base_confidence += 0.05

        # Reduce for uncertainty markers
        uncertainty_markers = [
            "could not find", "no information", "nicht gefunden",
            "keine Information", "unklar", "not specified",
            "might", "possibly", "unclear", "not sure", "uncertain",
        ]
        if any(m in answer.lower() for m in uncertainty_markers):
            base_confidence -= 0.1

        # Boost for structured answers
        if any(marker in answer for marker in ["**", "##", "1.", "- "]):
            base_confidence += 0.05

        # Boost for strong assertions backed by sources
        if sources and any(
            phrase in answer.lower()
            for phrase in ["according to", "found that", "shows that", "states that"]
        ):
            base_confidence += 0.1

        return max(0.15, min(0.95, base_confidence))

    async def _synthesize_findings(
        self,
        task: str,
        iterations: list,
        sources: list,
        conversation_history: list,
    ) -> str:
        """Synthesize findings when max iterations reached."""
        from deepsearch.llm import LLMMessage

        synthesis_prompt = f"""Based on your research so far, provide your best answer to:
{task}

Summarize what you found and note any limitations or gaps in the information."""

        conversation_history.append(LLMMessage.user(synthesis_prompt))

        response = await self.llm.complete(
            messages=conversation_history,
            temperature=0.3,
            max_tokens=1000,
        )

        return response.content
