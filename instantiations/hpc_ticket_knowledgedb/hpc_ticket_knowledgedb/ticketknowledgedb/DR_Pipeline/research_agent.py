#!/usr/bin/env python3
"""
Research Agent for HPC Deep Research system
Performs different types of research: zero-shot, docs-only, and ticket-based
"""

import asyncio
import re
from typing import List, Optional
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

# Try absolute imports first (for direct execution), then relative imports (for package use)
try:
    from dr_models import ResearchType, ResearchAnswer, SearchResult, HPCSearchRequest
    from dr_config import config
    from search_service import search_service
except ImportError:
    from .dr_models import ResearchType, ResearchAnswer, SearchResult, HPCSearchRequest
    from .dr_config import config
    from .search_service import search_service


class ResearchAgent:
    """Agent responsible for performing different types of research"""
    
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
    
    async def conduct_research(self, user_query: str, research_types: List[ResearchType]) -> List[ResearchAnswer]:
        """Conduct research based on requested research types"""
        
        print(f"Research Agent: Starting {len(research_types)} research types")
        
        # Map research types to their corresponding methods
        research_tasks = []
        
        for research_type in research_types:
            if research_type == ResearchType.ZERO_SHOT:
                research_tasks.append(self._zero_shot_research(user_query))
            elif research_type == ResearchType.DOCS_ONLY:
                research_tasks.append(self._docs_only_research(user_query))
            elif research_type == ResearchType.TICKETS_ONLY:
                research_tasks.append(self._tickets_only_research(user_query))
        
        # Execute research tasks
        research_results = await asyncio.gather(*research_tasks, return_exceptions=True)
        
        # Filter out None results and exceptions
        valid_results = []
        for result in research_results:
            if isinstance(result, Exception):
                print(f"  [!] Research task failed: {str(result)}")
            elif result is not None:
                valid_results.append(result)
        
        completed_tasks = len([r for r in research_results if not isinstance(r, Exception) and r is not None])
        print(f"Research Agent: Completed {completed_tasks} research tasks")
        
        return valid_results
    
    async def _zero_shot_research(self, user_query: str) -> ResearchAnswer:
        """Perform zero-shot research without any search"""
        print("  Zero-shot research: Generating answer without search")
        
        system_prompt = """You are an expert in various domains.

Answer the user's question based solely on your knowledge.

Provide a comprehensive answer covering:
- Direct response to the question
- Technical details and context
- Common practices and procedures if applicable
- Best practices and recommendations

Be honest about limitations - if you're uncertain about specific details (unknown configration settings, site and system specific details), say so."""

        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=user_query)
        ]
        
        response = await self.llm.ainvoke(messages)
        answer_text = response.content
        
        # Estimate confidence based on answer characteristics
        confidence = self._estimate_confidence(answer_text, has_sources=False)
        
        return ResearchAnswer(
            research_type=ResearchType.ZERO_SHOT,
            answer=answer_text,
            confidence=confidence,
            sources=[],
            reasoning="Generated using general knowledge without specific documentation",
            token_count=len(answer_text.split())
        )
    
    async def _docs_only_research(self, user_query: str) -> ResearchAnswer:
        """Perform research using only official documentation"""
        print("  Docs-only research: Searching official documentation")
        
        # Search documentation
        search_request = HPCSearchRequest(
            query=user_query,
            search_type="docs",
            max_results=config.max_search_results
        )
        
        search_response = await search_service.search(search_request)
        
        if search_response.error:
            print(f"    [ERROR] Search error: {search_response.error}")
            return self._create_error_answer(ResearchType.DOCS_ONLY, search_response.error)
        
        print(f"    Found {len(search_response.results)} documentation results")
        
        # New: Print top documentation sources
        for i, src in enumerate(search_response.results[:3], 1):
            try:
                print(f"      • DOC {i}: {src.title[:80]} (score={src.score:.2f})")
            except Exception:
                pass
        
        # Generate answer based on documentation
        answer_text = await self._generate_answer_from_sources(
            user_query, 
            search_response.results, 
            "official documentation"
        )
        
        # Estimate confidence based on answer characteristics
        has_sources = len(search_response.results) > 0
        confidence = self._estimate_confidence(answer_text, has_sources=has_sources)
        
        return ResearchAnswer(
            research_type=ResearchType.DOCS_ONLY,
            answer=answer_text,
            confidence=confidence,
            sources=search_response.results,
            reasoning="Based on official documentation sources",
            token_count=len(answer_text.split())
        )
    
    async def _tickets_only_research(self, user_query: str) -> ResearchAnswer:
        """Perform research using only support tickets to find similar cases"""
        print("  Tickets-only research: Searching similar support cases")
        
        # Search tickets
        search_request = HPCSearchRequest(
            query=user_query,
            search_type="tickets",
            max_results=config.max_search_results
        )
        
        search_response = await search_service.search(search_request)
        
        if search_response.error:
            print(f"    [ERROR] Search error: {search_response.error}")
            return self._create_error_answer(ResearchType.TICKETS_ONLY, search_response.error)
        
        print(f"    Found {len(search_response.results)} similar support cases")
        
        # New: Print top ticket sources
        for i, src in enumerate(search_response.results[:3], 1):
            try:
                print(f"      • TICKET {i}: {src.title[:80]} (score={src.score:.2f})")
            except Exception:
                pass
        
        # Generate answer based on similar cases
        answer_text = await self._generate_answer_from_sources(
            user_query, 
            search_response.results, 
            "similar support tickets and resolved cases"
        )
        
        # Estimate confidence based on answer characteristics
        has_sources = len(search_response.results) > 0
        confidence = self._estimate_confidence(answer_text, has_sources=has_sources)
        
        return ResearchAnswer(
            research_type=ResearchType.TICKETS_ONLY,
            answer=answer_text,
            confidence=confidence,
            sources=search_response.results,
            reasoning="Based on similar support cases",
            token_count=len(answer_text.split())
        )
    
    async def _direct_answer_search(self, user_query: str) -> Optional[ResearchAnswer]:
        """Search for direct answers to the exact question in documentation"""
        print(f"  Direct answer search: Checking FAQ directly")
        print(f"      Query: '{user_query}'")
        
        # Read the FAQ file directly
        faq_file_path = "/Users/sebastian/Downloads/ticketknowledgedb/docsmd/https___doc.nhr.fau.de_faq_index.html.md"
        
        try:
            with open(faq_file_path, 'r', encoding='utf-8') as f:
                faq_content = f.read()
            
            print(f"      Loaded FAQ file ({len(faq_content)} characters)")
            
            # Ask LLM: Is this question addressed in the FAQ?
            is_addressed, answer_text = await self._check_faq_simple(user_query, faq_content)
            
            if is_addressed:
                print(f"    Question addressed in FAQ")
                print(f"    Answer: {answer_text[:300]}...")
                return ResearchAnswer(
                    research_type=ResearchType.ZERO_SHOT,
                    answer=answer_text,
                    confidence=0.9,
                    sources=[],  # No search results, direct file read
                    reasoning=f"Direct answer found in FAQ file",
                    token_count=len(answer_text.split())
                )
            else:
                print(f"    Question not addressed in FAQ")
                return None
                
        except Exception as e:
            print(f"      [ERROR] Error reading FAQ file: {str(e)}")
            return None
    
    async def _check_faq_simple(self, user_query: str, faq_content: str) -> tuple[bool, str]:
        """Simple check: Is the question addressed in the FAQ?"""
        
        system_prompt = """You are analyzing a FAQ document.

Task: Check if the FAQ addresses the user's question and provide an answer if it does.

Instructions:
1. Look through the FAQ for information relevant to the question
2. If you find relevant information, provide a helpful answer
3. If not, respond with exactly "NOT ADDRESSED"

Be practical and helpful."""

        user_message = f"""Question: {user_query}

FAQ Content:
{faq_content}

Is this question addressed in the FAQ? If yes, provide the answer. If no, respond "NOT ADDRESSED"."""

        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=user_message)
        ]
        
        try:
            response = await self.llm.ainvoke(messages)
            response_text = response.content.strip()
            
            print(f"      🤖 LLM response: {response_text[:100]}...")
            
            if "NOT ADDRESSED" in response_text:
                return False, ""
            else:
                return True, response_text
                
        except Exception as e:
            print(f"      [ERROR] Error in FAQ check: {str(e)}")
            return False, ""
    
    async def _generate_answer_from_sources(self, user_query: str, sources: List[SearchResult], source_description: str) -> str:
        """Generate answer based on provided sources"""
        
        # Prepare sources content
        sources_content = ""
        for i, source in enumerate(sources[:8], 1):  # Limit to top 8 sources
            sources_content += f"\nSOURCE {i}:\n"
            sources_content += f"Title: {source.title}\n"
            sources_content += f"Content: {source.content}\n"
            if source.highlight:
                sources_content += f"Key highlights: {source.highlight}\n"
            sources_content += "\n"
        
        system_prompt = f"""You are an expert in various domains.

Answer the user's question based on the provided {source_description}.

IMPORTANT GUIDELINES:
1. Use ONLY information from the provided sources
2. Cite sources when making specific claims
3. If sources don't fully answer the question, be explicit about limitations
4. Focus on practical, actionable information
5. Include specific commands, procedures, or steps when available
6. Maintain technical accuracy - don't extrapolate beyond the provided information

If the sources are insufficient to answer the question completely, clearly state what information is missing."""

        content = f"USER QUESTION: {user_query}\n\nAVAILABLE SOURCES:\n{sources_content}"
        
        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=content)
        ]
        
        response = await self.llm.ainvoke(messages)
        return response.content
    
    def _estimate_confidence(self, answer: str, has_sources: bool) -> float:
        """Estimate confidence in the answer using LLM-based assessment"""
        print(f"Confidence assessment - has_sources: {has_sources}")
        print(f"Answer preview: {answer[:200]}...")
        
        try:
            confidence_prompt = f"""
You are evaluating the quality and reliability of an HPC support answer. Rate the confidence level from 0.0 to 1.0 based on these criteria:

**Answer Quality Factors:**
- Completeness: Does it fully address the question?
- Specificity: Are concrete commands/steps provided?
- Clarity: Is it easy to understand and follow?
- Technical accuracy indicators: Does it show deep technical knowledge?

**Source Reliability:**
- Has sources: {has_sources}

**Answer to evaluate:**
{answer}

**Instructions:**
1. Evaluate the answer quality on technical completeness, specificity, and clarity
2. Consider source availability as a reliability indicator
3. Look for uncertainty markers ("might", "possibly", "I'm not sure")
4. Assess if the answer provides actionable guidance

**Confidence Scale:**
- 0.9-1.0: Excellent, complete, specific answer with strong sources
- 0.7-0.8: Good answer with minor gaps or moderate sources
- 0.5-0.6: Adequate but incomplete or uncertain
- 0.3-0.4: Poor quality or highly uncertain
- 0.0-0.2: Very poor or no useful information

**REQUIRED OUTPUT FORMAT:**
CONFIDENCE: [number between 0.0 and 1.0]

Example: CONFIDENCE: 0.85

Only output the confidence line, nothing else."""

            response = self.llm.invoke(confidence_prompt)
            
            # Simple, robust parsing
            confidence_text = response.content.strip()
            print(f"🤖 LLM confidence response: '{confidence_text}'")
            
            # Extract confidence with simple, bulletproof parsing
            import re
            match = re.search(r'CONFIDENCE:\s*(\d+\.?\d*)', confidence_text)
            
            if match:
                confidence = float(match.group(1))
                # Ensure confidence is in valid range
                confidence = max(0.0, min(1.0, confidence))
                print(f"Parsed confidence: {confidence}")
            else:
                print(f"[!] Failed to parse confidence from: {confidence_text}")
                # Fallback to simple heuristics
                base_confidence = 0.3 if not has_sources else 0.6
                # Simple uncertainty detection
                uncertainty_markers = ["don't know", "unclear", "not sure", "might", "possibly", "uncertain"]
                if any(marker in answer.lower() for marker in uncertainty_markers):
                    base_confidence *= 0.7
                
                confidence = min(1.0, base_confidence)
                print(f"🔄 Fallback confidence: {confidence}")
            
            print(f"Final LLM confidence assessment: {confidence:.2f}")
            return confidence
            
        except Exception as e:
            print(f"[ERROR] Error in LLM confidence estimation: {e}")
            print(f"🔧 Exception details - has_sources: {has_sources}")
            # Fallback to simple estimation
            base_confidence = 0.3 if not has_sources else 0.6
            # Simple uncertainty detection
            uncertainty_markers = ["don't know", "unclear", "not sure", "might", "possibly", "uncertain"]
            if any(marker in answer.lower() for marker in uncertainty_markers):
                base_confidence *= 0.7
            fallback_confidence = min(1.0, base_confidence)
            print(f"🔄 Exception fallback confidence: {fallback_confidence}")
            return fallback_confidence
    
    def _create_error_answer(self, research_type: ResearchType, error: str) -> ResearchAnswer:
        """Create an error answer when research fails"""
        return ResearchAnswer(
            research_type=research_type,
            answer=f"Unable to perform {research_type.value} research due to error: {error}",
            confidence=0.0,
            sources=[],
            reasoning=f"Research failed: {error}",
            token_count=0
        )

    def _calculate_relevance_threshold(self, user_query: str) -> float:
        """Calculate dynamic relevance threshold based on query characteristics"""
        # Base threshold
        threshold = 6.0
        
        # Adjust based on query length (longer queries need higher precision)
        word_count = len(user_query.split())
        if word_count <= 5:
            threshold = 5.0  # Short queries, lower threshold
        elif word_count >= 10:
            threshold = 7.0  # Long queries, higher threshold
        
        # Adjust based on question type indicators
        question_words = ['how', 'what', 'where', 'when', 'why', 'can', 'should', 'will']
        if any(word in user_query.lower() for word in question_words):
            threshold -= 0.5  # Questions often have direct answers
        
        return threshold

    async def _solution_focused_research(self, user_query: str, previous_findings: str) -> ResearchAnswer:
        """Perform solution-focused research based on previous findings"""
        print("  Solution-focused research: Building on previous findings")
        
        # Prepare sources content
        sources_content = f"PREVIOUS FINDINGS:\n{previous_findings}\n\nUSER QUESTION:\n{user_query}"
        
        system_prompt = """You are an expert in various domains.

Task: Provide a solution-focused answer based on the previous findings and user's question.

Instructions:
1. Analyze the previous findings and identify gaps or areas for improvement
2. Use the user's question to guide the research and provide a practical solution
3. Focus on actionable information and specific steps or commands
4. Maintain technical accuracy and avoid extrapolating beyond the provided information

If the previous findings are insufficient to answer the question completely, clearly state what information is missing."""

        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=sources_content)
        ]
        
        response = await self.llm.ainvoke(messages)
        answer_text = response.content
        
        # Estimate confidence based on answer characteristics
        has_sources = "SOURCE" in previous_findings
        confidence = self._estimate_confidence(answer_text, has_sources=has_sources)
        
        return ResearchAnswer(
            research_type=ResearchType.SOLUTION_FOCUSED,
            answer=answer_text,
            confidence=confidence,
            sources=[],
            reasoning="Generated using previous findings and user's question",
            token_count=len(answer_text.split())
        )
    
    async def _deep_docs_research(self, user_query: str, previous_findings: str) -> ResearchAnswer:
        """Perform deep documentation research based on previous findings"""
        print("  Deep documentation research: Searching official documentation")
        
        # Search documentation
        search_request = HPCSearchRequest(
            query=user_query,
            search_type="docs",
            max_results=config.max_search_results
        )
        
        search_response = await search_service.search(search_request)
        
        if search_response.error:
            print(f"    [ERROR] Search error: {search_response.error}")
            return self._create_error_answer(ResearchType.DOCS_ONLY, search_response.error)
        
        print(f"    Found {len(search_response.results)} documentation results")
        
        # New: Print top documentation sources
        for i, src in enumerate(search_response.results[:3], 1):
            try:
                print(f"      • DOC {i}: {src.title[:80]} (score={src.score:.2f})")
            except Exception:
                pass
        
        # Generate answer based on documentation
        answer_text = await self._generate_answer_from_sources(
            user_query, 
            search_response.results, 
            "official documentation"
        )
        
        # Estimate confidence based on answer characteristics
        has_sources = len(search_response.results) > 0
        confidence = self._estimate_confidence(answer_text, has_sources=has_sources)
        
        return ResearchAnswer(
            research_type=ResearchType.DOCS_ONLY,
            answer=answer_text,
            confidence=confidence,
            sources=search_response.results,
            reasoning="Based on official documentation sources",
            token_count=len(answer_text.split())
        )

    def _count_sources_in_answer(self, answer_text: str) -> int:
        """Count actual sources cited in the answer"""
        # Simple heuristic: count occurrences of "SOURCE" in the answer
        return answer_text.count("SOURCE")
