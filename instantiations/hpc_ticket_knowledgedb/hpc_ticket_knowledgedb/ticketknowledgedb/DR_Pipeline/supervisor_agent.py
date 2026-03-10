#!/usr/bin/env python3
"""
Supervisor Agent for HPC Deep Research system
Orchestrates the research process and assesses answer quality
"""

import asyncio
from typing import List, Tuple
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
import re

# Try absolute imports first (for direct execution), then relative imports (for package use)
try:
    from dr_models import (
        ResearchType, ResearchAnswer, UserAssumption, QualityAssessment, 
        QualityScore, DRIteration, HPCSearchRequest, SearchResult
    )
    from dr_config import config
    from research_agent import ResearchAgent
    from assumption_checker import AssumptionChecker
    from search_service import search_service
except ImportError:
    from .dr_models import (
        ResearchType, ResearchAnswer, UserAssumption, QualityAssessment, 
        QualityScore, DRIteration, HPCSearchRequest, SearchResult
    )
    from .dr_config import config
    from .research_agent import ResearchAgent
    from .assumption_checker import AssumptionChecker
    from .search_service import search_service


class SupervisorAgent:
    """Supervisor agent that orchestrates the DR process"""
    
    def __init__(self):
        self.llm = ChatOpenAI(
            base_url=config.llm_base_url,
            api_key=config.llm_api_key,
            model=config.llm_model,
            temperature=config.llm_temperature,
            max_tokens=config.llm_max_tokens,
            timeout=config.llm_timeout,
            request_timeout=config.llm_timeout
        )
        self.research_agent = ResearchAgent()
        self.assumption_checker = AssumptionChecker()
    
    async def conduct_dr_workflow(self, user_query: str) -> List[DRIteration]:
        """Conduct the complete DR workflow with multiple iterations"""
        print("Starting DR workflow...")
        
        iterations = []
        
        for iteration_num in range(1, config.max_iterations + 1):
            iteration = await self.conduct_iteration(user_query, iteration_num, iterations)
            iterations.append(iteration)
            
            # Check if we should continue
            if self._should_stop_iterations(iteration):
                break
            
            # Check for high-quality direct answer (early stopping)
            if iteration_num == 1 and self._has_high_quality_direct_answer(iteration):
                print("Supervisor: High-quality direct answer found - stopping after first iteration")
                break
        
        print(f"DR workflow completed after {len(iterations)} iteration(s)")
        
        return iterations
    
    async def conduct_iteration(self, user_query: str, iteration_num: int, previous_iterations: List[DRIteration]) -> DRIteration:
        """Conduct a single iteration of the DR workflow"""
        print(f"\nDR Iteration {iteration_num}")
        
        # First iteration: Comprehensive research + assumption checking
        if iteration_num == 1:
            research_types = [ResearchType.ZERO_SHOT, ResearchType.DOCS_ONLY, ResearchType.TICKETS_ONLY]
            print("Strategy: Comprehensive research + assumption validation")
            
            # Perform research
            research_answers = await self.research_agent.conduct_research(user_query, research_types)
            
            # Check user assumptions
            user_assumptions = await self.assumption_checker.check_assumptions(user_query)
            
        else:
            # Follow-up iterations: Solution-oriented, fact-check previous proposals
            research_types = [ResearchType.DOCS_ONLY, ResearchType.TICKETS_ONLY]  # Skip zero-shot
            print("Strategy: Solution-oriented research + fact-checking previous proposals")
            
            # Get the best answer from previous iteration for fact-checking
            previous_iteration = previous_iterations[-1]
            best_previous_answer = self._get_best_answer(previous_iteration.research_answers)
            
            # Perform targeted research with context from previous iteration
            research_answers = await self._solution_oriented_research(
                user_query, research_types, best_previous_answer, previous_iteration.user_assumptions
            )
            
            # Don't re-check user assumptions, but validate our proposed solution
            user_assumptions = await self._fact_check_proposed_solution(
                user_query, best_previous_answer, previous_iteration.user_assumptions
            )
        
        # Assess quality of research answers
        quality_assessments = await self._assess_answer_quality(user_query, research_answers)
        
        # Create iteration record
        iteration = DRIteration(
            iteration_number=iteration_num,
            research_answers=research_answers,
            user_assumptions=user_assumptions,
            quality_assessments=quality_assessments,
            supervisor_decision=""
        )
        
        # Make supervision decision
        decision = await self._make_supervision_decision(user_query, iteration, previous_iterations)
        iteration.supervisor_decision = decision
        
        return iteration
    
    def _get_best_answer(self, research_answers: List[ResearchAnswer]) -> ResearchAnswer:
        """Get the best answer from a list based on confidence and reasoning"""
        if not research_answers:
            return None
        
        # Prioritize direct answers, then by confidence
        direct_answers = [a for a in research_answers if "Direct answer found" in a.reasoning]
        if direct_answers:
            return max(direct_answers, key=lambda x: x.confidence)
        
        return max(research_answers, key=lambda x: x.confidence)
    
    async def _solution_oriented_research(
        self, 
        user_query: str, 
        research_types: List[ResearchType],
        best_previous_answer: ResearchAnswer,
        previous_assumptions: List[UserAssumption]
    ) -> List[ResearchAnswer]:
        """Perform solution-oriented research that builds on previous findings"""
        
        print("Building on previous findings for solution-oriented research")
        
        # Create enhanced queries that incorporate previous findings
        solution_context = f"""
Previous best answer: {best_previous_answer.answer if best_previous_answer else 'None'}

Invalid user assumptions identified:
{chr(10).join([f"- {a.assumption}" for a in previous_assumptions if not a.is_valid])}

Now find the most practical, actionable solution for: {user_query}
"""
        
        # Use the research agent but with enhanced context
        research_answers = await self.research_agent.conduct_research(solution_context, research_types)
        
        # Update the reasoning to reflect solution-oriented approach
        for answer in research_answers:
            answer.reasoning = f"Solution-oriented research building on iteration 1 findings: {answer.reasoning}"
        
        return research_answers
    
    async def _fact_check_proposed_solution(
        self,
        user_query: str,
        proposed_solution: ResearchAnswer,
        original_assumptions: List[UserAssumption]
    ) -> List[UserAssumption]:
        """Fact-check the proposed solution instead of re-checking user assumptions"""
        
        if not proposed_solution:
            return original_assumptions
        
        print("Fact-checking proposed solution against documentation")
        
        # Extract claims from the proposed solution
        solution_claims = await self._extract_solution_claims(proposed_solution.answer)
        
        # Validate each claim against documentation
        validated_claims = []
        for claim in solution_claims:
            # Search for evidence for this specific claim
            search_request = HPCSearchRequest(
                query=claim,
                search_type="docs",
                max_results=3
            )
            
            search_response = await search_service.search(search_request)
            
            if not search_response.error and search_response.results:
                # Validate this claim
                is_valid = await self._validate_solution_claim(claim, search_response.results)
                validated_claims.append(UserAssumption(
                    assumption=f"Solution claim: {claim}",
                    is_valid=is_valid,
                    evidence=f"Validated against {len(search_response.results)} documentation sources",
                    confidence=0.8 if is_valid else 0.2
                ))
        
        print(f"  Fact-checked {len(validated_claims)} solution claims")
        
        # Return original invalid assumptions plus new solution validation
        return original_assumptions + validated_claims
    
    async def _extract_solution_claims(self, solution_text: str) -> List[str]:
        """Extract factual claims from the proposed solution"""
        
        system_prompt = """Extract the key factual claims from this solution that can be verified against documentation.

Focus on:
- Technical procedures and commands
- System behaviors and capabilities  
- File system properties and access methods
- Authentication and authorization claims
- Resource allocation and usage patterns

Return each claim as a separate line, focusing on verifiable facts."""

        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=f"Solution to analyze: {solution_text}")
        ]
        
        response = await self.llm.ainvoke(messages)
        claims = [line.strip() for line in response.content.split('\n') if line.strip()]
        
        return claims[:5]  # Limit to top 5 claims
    
    async def _validate_solution_claim(self, claim: str, evidence_sources: List[SearchResult]) -> bool:
        """Validate a single solution claim against evidence"""
        
        evidence_text = ""
        for source in evidence_sources:
            evidence_text += f"Source: {source.title}\nContent: {source.content[:300]}...\n\n"
        
        system_prompt = """Validate whether the claim is supported by the provided documentation evidence.

Return only: TRUE (if supported), FALSE (if contradicted), or UNKNOWN (if insufficient evidence)"""

        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=f"Claim: {claim}\n\nEvidence:\n{evidence_text}")
        ]
        
        try:
            response = await self.llm.ainvoke(messages)
            response_text = response.content
            
            verdict = response_text.strip().upper()
            
            return verdict == "TRUE"
        except Exception as e:
            print(f"    [ERROR] Error validating solution claim: {str(e)}")
            return False
    
    async def _assess_answer_quality(self, user_query: str, research_answers: List[ResearchAnswer]) -> List[QualityAssessment]:
        """Assess the quality of research answers"""
        print("Supervisor: Assessing answer quality")
        
        assessment_tasks = []
        for answer in research_answers:
            assessment_tasks.append(self._assess_single_answer(user_query, answer))
        
        assessments = await asyncio.gather(*assessment_tasks)
        
        # Log assessment summary
        for i, assessment in enumerate(assessments):
            answer_type = research_answers[i].research_type.value
            print(f"  📈 {answer_type}: {assessment.score.name} (contributes: {assessment.contributes_to_answer})")
        
        return assessments
    
    async def _assess_single_answer(self, user_query: str, research_answer: ResearchAnswer) -> QualityAssessment:
        """Assess quality of a single research answer"""
        
        system_prompt = """You are an expert HPC system administrator evaluating research answer quality.

Assess how well this research answer addresses the user's question on these dimensions:

1. **Relevance**: Does it directly address the user's question?
2. **Completeness**: Does it provide sufficient information to help the user?
3. **Accuracy**: Is the information technically sound and specific?
4. **Actionability**: Does it provide concrete steps or commands when needed?
5. **Source Quality**: Are the sources authoritative and relevant?

SCORING:
- EXCELLENT (5): Outstanding answer that fully addresses the question
- GOOD (4): Strong answer with minor gaps
- ADEQUATE (3): Acceptable answer but missing some important details
- POOR (2): Partially relevant but significant issues
- INSUFFICIENT (1): Does not adequately address the question

RESPONSE FORMAT:
SCORE: [1-5]
CONTRIBUTES: [YES/NO] - Does this answer contribute meaningfully to solving the user's question?
ADDRESSES_QUESTION: [YES/NO] - Does this directly address what the user asked?
FACTUAL_ACCURACY: [0.0-1.0] - How confident are you in the technical accuracy?
COMPLETENESS: [0.0-1.0] - How complete is the answer?
REASONING: [Detailed explanation of the assessment]"""

        # Prepare answer content
        sources_summary = f"{len(research_answer.sources)} sources" if research_answer.sources else "no sources"
        content = f"""USER QUESTION: {user_query}

RESEARCH ANSWER TO EVALUATE:
Type: {research_answer.research_type.value}
Confidence: {research_answer.confidence:.2f}
Sources: {sources_summary}
Reasoning: {research_answer.reasoning}

Answer: {research_answer.answer}"""

        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=content)
        ]
        
        try:
            response = await self.llm.ainvoke(messages)
            response_text = response.content
            
            # Robust parsing with multiple fallback patterns
            def extract_score(text: str) -> int:
                """Extract score with robust parsing"""
                # Try multiple patterns
                patterns = [
                    r'SCORE:\s*(\d+)',  # SCORE: 5
                    r'SCORE:\s*\*\*\s*(\d+)',  # SCORE: ** 5
                    r'SCORE:\s*\*\*(\d+)\*\*',  # SCORE: **5**
                    r'SCORE:\s*\[(\d+)\]',  # SCORE: [5]
                    r'SCORE:\s*(\d+)/5',  # SCORE: 5/5
                    r'(\d+)/5',  # 5/5
                    r'score.*?(\d+)',  # score is 5
                ]
                
                for pattern in patterns:
                    match = re.search(pattern, text, re.IGNORECASE)
                    if match:
                        score = int(match.group(1))
                        if 1 <= score <= 5:
                            return score
                
                # If no valid score found, return default
                return 3
            
            def extract_yes_no(text: str, field: str) -> bool:
                """Extract YES/NO fields with robust parsing"""
                patterns = [
                    rf'{field}:\s*(YES|NO)',
                    rf'{field}:\s*\*\*(YES|NO)\*\*',
                    rf'{field}:\s*\[(YES|NO)\]',
                ]
                
                for pattern in patterns:
                    match = re.search(pattern, text, re.IGNORECASE)
                    if match:
                        return match.group(1).upper() == "YES"
                
                # Default to True if not found
                return True
            
            def extract_float(text: str, field: str) -> float:
                """Extract float fields with robust parsing"""
                patterns = [
                    rf'{field}:\s*([0-9.]+)',
                    rf'{field}:\s*\*\*([0-9.]+)\*\*',
                    rf'{field}:\s*\[([0-9.]+)\]',
                ]
                
                for pattern in patterns:
                    match = re.search(pattern, text, re.IGNORECASE)
                    if match:
                        try:
                            value = float(match.group(1))
                            if 0.0 <= value <= 1.0:
                                return value
                        except ValueError:
                            continue
                
                # Default value
                return 0.7
            
            def extract_reasoning(text: str) -> str:
                """Extract reasoning with robust parsing"""
                patterns = [
                    r'REASONING:\s*(.+?)(?:\n\n|\Z)',
                    r'REASONING:\s*(.+)',
                ]
                
                for pattern in patterns:
                    match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
                    if match:
                        return match.group(1).strip()
                
                return "No reasoning provided"
            
            # Parse all fields with robust extraction
            score_value = extract_score(response_text)
            contributes = extract_yes_no(response_text, "CONTRIBUTES")
            addresses = extract_yes_no(response_text, "ADDRESSES_QUESTION")
            accuracy = extract_float(response_text, "FACTUAL_ACCURACY")
            completeness = extract_float(response_text, "COMPLETENESS")
            reasoning = extract_reasoning(response_text)
            
            score = QualityScore(score_value)
            
            return QualityAssessment(
                score=score,
                reasoning=reasoning,
                contributes_to_answer=contributes,
                addresses_user_question=addresses,
                factual_accuracy=accuracy,
                completeness=completeness
            )
            
        except Exception as e:
            print(f"    [ERROR] Error assessing answer quality: {str(e)}")
            return QualityAssessment(
                score=QualityScore.ADEQUATE,
                reasoning=f"Assessment error: {str(e)}",
                contributes_to_answer=True,
                addresses_user_question=True,
                factual_accuracy=0.5,
                completeness=0.5
            )
    
    async def _make_supervision_decision(
        self,
        user_query: str,
        iteration: DRIteration,
        iterations: List[DRIteration]
    ) -> str:
        """Make supervision decision about whether to continue research"""

        # Calculate quality metrics
        if not iteration.quality_assessments:
            # Handle case with no quality assessments (e.g., simple how-to questions)
            avg_score = 0.0
            contributing_answers = 0
            addressing_answers = 0
        else:
            avg_score = sum(assessment.score.value for assessment in iteration.quality_assessments) / len(iteration.quality_assessments)
            contributing_answers = sum(1 for assessment in iteration.quality_assessments if assessment.contributes_to_answer)
            addressing_answers = sum(1 for assessment in iteration.quality_assessments if assessment.addresses_user_question)

        # Check for invalid assumptions
        invalid_assumptions = [a for a in iteration.user_assumptions if not a.is_valid and a.confidence > 0.7]

        # Decision logic
        decision_factors = {
            "avg_quality": avg_score,
            "contributing_count": contributing_answers,
            "addressing_count": addressing_answers,
            "total_answers": len(iteration.research_answers),
            "invalid_assumptions": len(invalid_assumptions),
            "iteration": iteration.iteration_number
        }

        # EARLY STOPPING: Check if we have sufficient quality to stop immediately
        # This avoids unnecessary LLM calls for simple questions with good answers
        if self._should_stop_early(avg_score, contributing_answers, addressing_answers,
                                    len(iteration.research_answers), invalid_assumptions):
            print("Early stopping: High quality answers found")
            return "COMPLETE"
        
        print(f"🤔 Supervisor decision factors:")
        print(f"   Average quality: {avg_score:.1f}/5.0")
        print(f"   Contributing answers: {contributing_answers}/{len(iteration.research_answers)}")
        print(f"   Addressing question: {addressing_answers}/{len(iteration.research_answers)}")
        print(f"   Invalid assumptions: {len(invalid_assumptions)}")
        print(f"   🔄 Iteration: {iteration.iteration_number}/{config.max_iterations}")
        
        # Generate decision
        system_prompt = """You are a research supervisor deciding whether the current research iteration provides sufficient information to answer the user's HPC question.

Consider:
1. Quality of research answers
2. How many answers contribute meaningfully
3. Whether answers directly address the question
4. Any problematic user assumptions detected
5. Current iteration number (max 3 iterations)

DECISION CRITERIA:
- CONTINUE if answers are insufficient or major assumptions are wrong
- COMPLETE if answers adequately address the question

RESPONSE FORMAT:
DECISION: [CONTINUE/COMPLETE]
REASONING: [Detailed explanation of decision]"""

        content = f"""USER QUESTION: {user_query}

RESEARCH QUALITY METRICS:
- Average Quality Score: {avg_score:.1f}/5.0
- Contributing Answers: {contributing_answers}/{len(iteration.research_answers)}
- Directly Addressing Question: {addressing_answers}/{len(iteration.research_answers)}
- Invalid User Assumptions: {len(invalid_assumptions)}
- Current Iteration: {iteration.iteration_number}/{config.max_iterations}

QUALITY ASSESSMENTS:
"""
        
        for i, (answer, assessment) in enumerate(zip(iteration.research_answers, iteration.quality_assessments)):
            content += f"\n{answer.research_type.value}: {assessment.score.name} - {assessment.reasoning[:100]}..."
        
        if invalid_assumptions:
            content += f"\n\nINVALID ASSUMPTIONS DETECTED:\n"
            for assumption in invalid_assumptions:
                content += f"- {assumption.assumption}\n"
                content += f"Evidence: {assumption.evidence[:200]}...\n\n"
        
        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=content)
        ]
        
        try:
            response = await self.llm.ainvoke(messages)
            response_text = response.content
            
            print(f"🤖 Supervisor LLM response: {response_text[:200]}...")
            
            decision = "COMPLETE" if "DECISION: COMPLETE" in response_text else "CONTINUE"
            reasoning_match = response_text.split("REASONING:")[1].strip() if "REASONING:" in response_text else "No reasoning provided"
            
            print(f"Supervisor decision: {decision}")
            print(f"Reasoning: {reasoning_match[:100]}...")
            
            # Override decision if max iterations reached
            if iteration.iteration_number >= config.max_iterations:
                decision = "COMPLETE"
                reasoning_match += f" (Max iterations {config.max_iterations} reached)"
                print(f"🔄 Max iterations reached, forcing COMPLETE")
            
            # Store reasoning in iteration for debugging
            iteration.supervisor_reasoning = reasoning_match
            
            return decision  # Return decision, not reasoning
            
        except Exception as e:
            print(f"    [ERROR] Error making supervision decision: {str(e)}")
            # Default to complete if error occurs
            return "COMPLETE"
    
    def _should_stop_iterations(self, iteration: DRIteration) -> bool:
        """Check if we should stop iterations based on decision"""
        return iteration.supervisor_decision == "COMPLETE"
    
    def _has_high_quality_direct_answer(self, iteration: DRIteration) -> bool:
        """Check if iteration contains a high-quality direct answer"""
        for answer in iteration.research_answers:
            if ("Direct answer found" in answer.reasoning and
                answer.confidence > 0.8):
                print(f"  Found high-quality direct answer (confidence: {answer.confidence:.2f})")
                return True
        return False

    def _should_stop_early(
        self,
        avg_quality: float,
        contributing_count: int,
        addressing_count: int,
        total_answers: int,
        invalid_assumptions: list
    ) -> bool:
        """
        Determine if we should stop early based on quality metrics.

        Stops early if:
        - Average quality is GOOD (4.0+) or EXCELLENT (5.0)
        - At least 2 answers contribute meaningfully
        - All answers address the user's question
        - No significant invalid assumptions detected

        This prevents unnecessary iterations for simple, well-answered questions.
        """
        # Don't stop early if we have invalid assumptions that need addressing
        if len(invalid_assumptions) > 0:
            return False

        # Excellent quality (5.0) with full coverage → stop immediately
        if avg_quality >= 5.0 and addressing_count >= 2:
            print(f"  EXCELLENT quality ({avg_quality:.1f}/5.0) with {addressing_count} addressing answers")
            return True

        # Good quality (4.0+) with strong consensus → stop
        if (avg_quality >= 4.0 and
            contributing_count >= 2 and
            addressing_count == total_answers and  # All answers address the question
            total_answers >= 2):  # At least 2 independent answers
            print(f"  GOOD quality ({avg_quality:.1f}/5.0) with {contributing_count}/{total_answers} contributing")
            return True

        # Adequate quality (3.5+) with perfect consensus → stop
        # This catches cases where docs + tickets agree even if quality is "adequate"
        if (avg_quality >= 3.5 and
            addressing_count == total_answers and
            contributing_count == total_answers and
            total_answers >= 3):  # All 3+ answers agree and contribute
            print(f"  Strong consensus ({avg_quality:.1f}/5.0) across all {total_answers} answers")
            return True

        return False
    
    async def generate_final_report(self, user_query: str, iterations: List[DRIteration]) -> str:
        """Generate comprehensive final report with structured analysis"""
        print("Supervisor: Generating structured comprehensive report")
        
        # Collect all research findings
        all_answers = []
        all_assumptions = []
        
        for iteration in iterations:
            all_answers.extend(iteration.research_answers)
            all_assumptions.extend(iteration.user_assumptions)
        
        # Separate answers by type
        direct_answer = None
        docs_answers = []
        tickets_answers = []
        
        for answer in all_answers:
            if "Direct answer found" in answer.reasoning:
                direct_answer = answer
            elif answer.research_type == ResearchType.DOCS_ONLY:
                docs_answers.append(answer)
            elif answer.research_type == ResearchType.TICKETS_ONLY:
                tickets_answers.append(answer)
        
        # Generate structured report
        report = await self._generate_structured_report(
            user_query, 
            direct_answer, 
            docs_answers, 
            tickets_answers, 
            all_assumptions
        )
        
        print("=" * 80)
        print("COMPREHENSIVE REPORT GENERATED:")
        print("=" * 80)
        print(report)
        print("=" * 80)
        
        return report
    
    async def _generate_structured_report(self, user_query: str, direct_answer, docs_answers, tickets_answers, assumptions) -> str:
        """Generate structured report following the required format"""
        
        system_prompt = """You MUST follow this EXACT structure. Do NOT deviate from this format. Do NOT create your own sections.

MANDATORY STRUCTURE - USE THESE EXACT HEADINGS:

## 1. REQUEST BREAKDOWN
Analyze what the user is actually asking for and what they expect as output.

## 2. ASSUMPTION ANALYSIS
Present user assumptions that were validated or invalidated. Show misconceptions corrected.

## 3. DIRECT ANSWER ADVOCACY
State: "We should always look at the direct answer first - it's backed by official FAQ"
Present the direct answer if found.

## 4. DIRECT ANSWER ASSESSMENT
Evaluate if the direct answer is helpful and complete. Identify gaps.

## 5. DOCUMENTATION ANALYSIS
Discuss what official docs provide to fill gaps not covered by direct answer.

## 6. TICKET ANALYSIS
Only if docs don't address all points - use tickets to complete gaps.

## 7. SOLUTION RANKING
Clear hierarchy: Direct Answer > Docs > Tickets. Explain why each source is prioritized.

## 8. FOCUSED SOLUTION
Provide practical, step-by-step guidance the user should follow.

CRITICAL: Use ONLY these 8 sections with these EXACT headings. Do NOT add tables, code blocks, or other formatting. Keep each section concise and focused."""

        # Prepare content
        content_parts = [f"USER QUERY: {user_query}"]
        
        if direct_answer:
            content_parts.append(f"\nDIRECT ANSWER FOUND:\n{direct_answer.answer}")
        
        if docs_answers:
            content_parts.append(f"\nDOCS RESEARCH:")
            for i, answer in enumerate(docs_answers, 1):
                content_parts.append(f"Docs {i}: {answer.answer}")
        
        if tickets_answers:
            content_parts.append(f"\nTICKETS RESEARCH:")
            for i, answer in enumerate(tickets_answers, 1):
                content_parts.append(f"Ticket {i}: {answer.answer}")
        
        if assumptions:
            content_parts.append(f"\nUSER ASSUMPTIONS:")
            for assumption in assumptions:
                status = "VALID" if assumption.is_valid else "INVALID"
                content_parts.append(f"- {status}: {assumption.assumption}")
                content_parts.append(f"  Evidence: {assumption.evidence[:200]}...")
        
        content = "\n".join(content_parts)
        
        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=content)
        ]
        
        response = await self.llm.ainvoke(messages)
        return response.content
    
    async def generate_concise_answer(self, user_query: str, comprehensive_report: str) -> str:
        """Generate concise final answer with fact-checking against docs"""
        print("Supervisor: Generating fact-checked concise answer")
        
        # First, generate initial concise answer
        initial_answer = await self._generate_initial_concise_answer(user_query, comprehensive_report)
        
        return initial_answer
    
    async def _generate_initial_concise_answer(self, user_query: str, comprehensive_report: str) -> str:
        """Generate initial concise answer"""
        
        system_prompt = f"""You are an HPC support specialist helping a user solve their cluster computing problem.

CRITICAL: You must provide ONLY a brief, direct answer. DO NOT generate a structured report with sections.

The user asked: "{user_query}"

YOUR ROLE: Act as helpful HPC support staff. Provide a practical solution that will actually fix their problem.

ABSOLUTE REQUIREMENTS:
- Maximum {config.max_concise_answer_sentences} sentences TOTAL
- NO section headers (## 1. REQUEST BREAKDOWN, etc.)
- NO numbered sections 
- NO structured format
- NO analysis sections
- PLAIN TEXT ONLY - just answer the question directly
- PROVIDE A WORKING SOLUTION - tell them exactly what to do to fix their issue

FORBIDDEN:
- Do NOT write "## 1. REQUEST BREAKDOWN"
- Do NOT write "## 2. ASSUMPTION ANALYSIS" 
- Do NOT write any section headers at all
- Do NOT create a structured report
- Do NOT provide step-by-step numbered lists

REQUIRED FORMAT:
Write a concise answer that directly solves their problem with specific commands/actions they should take. Include information about the HPC system they are using.

USER QUESTION: {user_query}

Provide a direct solution. Tell them exactly what commands to run to fix their problem."""

        content = f"COMPREHENSIVE RESEARCH REPORT:\n{comprehensive_report}\n\nProvide a direct 2-4 sentence answer to: {user_query}"
        
        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=content)
        ]
        
        response = await self.llm.ainvoke(messages)
        answer = response.content.strip()
        
        # Clean up any channel formatting that might slip through
        if "<|channel|>" in answer:
            # Extract just the final message part
            if "<|channel|>final<|message|>" in answer:
                answer = answer.split("<|channel|>final<|message|>")[-1]
            # Remove any remaining channel tags
            answer = answer.replace("<|channel|>", "").replace("<|message|>", "").replace("<|end|>", "").replace("<|start|>", "")
            answer = answer.strip()
        
        # Emergency cleanup: if it still has section headers, extract just the first few sentences
        if "##" in answer or "REQUEST BREAKDOWN" in answer:
            # Find the first actual answer content after any headers
            lines = answer.split('\n')
            clean_lines = []
            for line in lines:
                if not line.strip().startswith('##') and not line.strip().startswith('#') and line.strip():
                    clean_lines.append(line.strip())
                    if len(clean_lines) >= 3:  # Stop after a few sentences
                        break
            answer = ' '.join(clean_lines)
        
        return answer
