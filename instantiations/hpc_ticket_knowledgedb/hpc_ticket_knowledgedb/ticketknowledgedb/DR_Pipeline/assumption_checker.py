#!/usr/bin/env python3
"""
Assumption Checker Agent for HPC Deep Research system
Identifies and validates user assumptions that might be incorrect
"""

import asyncio
import re
from typing import List, Optional
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

# Try absolute imports first (for direct execution), then relative imports (for package use)
try:
    from dr_models import UserAssumption, SearchResult, HPCSearchRequest
    from dr_config import config
    from search_service import search_service
except ImportError:
    from .dr_models import UserAssumption, SearchResult, HPCSearchRequest
    from .dr_config import config
    from .search_service import search_service


class AssumptionChecker:
    """Agent responsible for identifying and checking user assumptions"""
    
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
    
    async def check_assumptions(self, user_query: str) -> List[UserAssumption]:
        """Extract and validate user assumptions from the query"""
        print("Assumption Checker: Analyzing user assumptions")
        print(f"  Query: '{user_query}'")

        # OPTIMIZATION: Skip assumption checking for simple how-to questions
        # These queries don't contain assumptions, just requests for information
        is_simple = self._is_simple_how_to_question(user_query)
        print(f"  Is simple how-to question? {is_simple}")

        if is_simple:
            print("  [SKIP] Simple how-to question detected - skipping assumption checking")
            return []

        # Step 1: Extract assumptions from user query
        print("  [CHECKING] Asking LLM to extract assumptions...")
        assumptions_text = await self._extract_assumptions(user_query)
        print(f"  [LLM RESPONSE] Raw assumptions text:")
        print(f"    {assumptions_text[:200]}...")

        assumptions_list = self._parse_assumptions(assumptions_text)
        print(f"  [PARSED] Found {len(assumptions_list)} assumptions:")
        for i, assumption in enumerate(assumptions_list, 1):
            print(f"    {i}. {assumption}")

        if not assumptions_list:
            print("  [RESULT] No significant assumptions detected")
            return []

        print(f"  [VALIDATING] Found {len(assumptions_list)} assumptions to validate")

        # Step 2: Validate assumptions against documentation
        validated_assumptions = await self._validate_assumptions(assumptions_list)

        print(f"  [COMPLETE] Validated {len(validated_assumptions)} assumptions")
        return validated_assumptions

    def _is_simple_how_to_question(self, query: str) -> bool:
        """
        Check if the query is a simple how-to question without assumptions.

        Simple how-to questions start with:
        - "How do I..."
        - "How can I..."
        - "How to..."
        - "What is..."
        - "What does..."

        And don't contain assumption indicators like:
        - "I tried..."
        - "I assume..."
        - "I thought..."
        - "Should I..." (implies assumptions about options)
        - Conditional statements ("if", "when I do X, Y happens")
        """
        query_lower = query.lower().strip()

        # Simple how-to starters (no assumptions)
        simple_starters = [
            "how do i",
            "how can i",
            "how to",
            "what is",
            "what does",
            "what are",
            "where is",
            "where can i find",
            "show me how",
        ]

        # Assumption indicators (contains assumptions)
        assumption_indicators = [
            "i tried",
            "i assume",
            "i thought",
            "should i",
            "is it better to",
            "which is better",
            "i'm doing",
            "i am doing",
            "why is my",
            "why does my",
            "my job",
            "my code",
            "when i",
            "if i",
        ]

        # Check if it's a simple how-to question
        is_simple = any(query_lower.startswith(starter) for starter in simple_starters)
        matching_starter = next((s for s in simple_starters if query_lower.startswith(s)), None)

        # Check if it contains assumption indicators
        has_assumptions = any(indicator in query_lower for indicator in assumption_indicators)
        matching_indicator = next((i for i in assumption_indicators if i in query_lower), None)

        # Debug logging
        print(f"    [DEBUG] Query (lowercase): '{query_lower}'")
        print(f"    [DEBUG] Matches simple starter? {is_simple} (matched: '{matching_starter}')")
        print(f"    [DEBUG] Has assumption indicators? {has_assumptions} (found: '{matching_indicator}')")
        print(f"    [DEBUG] Result: is_simple={is_simple} AND not has_assumptions={not has_assumptions}")

        # Only skip if it's simple AND doesn't have assumption indicators
        return is_simple and not has_assumptions
    
    async def _extract_assumptions(self, user_query: str) -> str:
        """Extract implicit assumptions from user query"""
        
        # Determine number of assumptions based on query complexity
        query_words = len(user_query.split())
        if query_words <= 15:
            max_assumptions = 3
        elif query_words <= 30:
            max_assumptions = 5
        else:
            max_assumptions = config.max_assumptions
        
        system_prompt = f"""You are an expert at identifying implicit assumptions in HPC user questions.

Analyze the user's question ONLY if it contains implicit assumptions that need validation.

ONLY extract assumptions if the user is:
- Making statements about how something works
- Describing a problem with their setup/code
- Comparing options ("should I use X or Y?")
- Mentioning previous attempts or errors

DO NOT extract assumptions for simple information requests like:
- "How do I...?"
- "What is...?"
- "Show me how to..."

If the query contains assumptions, extract up to {max_assumptions} that could lead to incorrect guidance.

EXAMPLES OF REAL ASSUMPTIONS:
- "The --partition parameter is optional and SLURM will choose the best one"
- "$WORK storage is temporary and gets cleaned regularly"
- "I can change my walltime limit after the job starts"

RESPONSE FORMAT:
If assumptions found: Return a numbered list
If NO assumptions: Return "NONE"

USER QUERY: {user_query}

Extract assumptions (or respond "NONE"):"""

        messages = [
            SystemMessage(content="You are an expert at identifying implicit assumptions in technical questions."),
            HumanMessage(content=system_prompt)
        ]
        
        response = await self.llm.ainvoke(messages)
        return response.content
    
    def _parse_assumptions(self, assumptions_text: str) -> List[str]:
        """Parse assumptions from LLM response"""
        assumptions = []

        # Check if LLM responded with "NONE" (no assumptions)
        if "NONE" in assumptions_text.upper() and len(assumptions_text.strip()) < 20:
            return []

        lines = assumptions_text.strip().split('\n')

        for line in lines:
            line = line.strip()
            # Match patterns like "1. assumption" or "- assumption"
            if re.match(r'^\d+\.\s+', line) or re.match(r'^-\s+', line):
                # Remove the number/bullet and clean up
                assumption = re.sub(r'^\d+\.\s+', '', line)
                assumption = re.sub(r'^-\s+', '', assumption)
                assumption = assumption.strip()
                if assumption and len(assumption) > 10:
                    assumptions.append(assumption)

        return assumptions[:config.max_assumptions]
    
    async def _validate_assumptions(self, assumptions: List[str]) -> List[UserAssumption]:
        """Validate assumptions against official documentation"""
        print(f"    Validating {len(assumptions)} assumptions against documentation")
        
        # Search documentation for evidence
        search_queries = self._generate_search_queries(assumptions)
        search_tasks = []
        
        for query in search_queries:
            search_request = HPCSearchRequest(
                query=query,
                search_type="docs",  # Only use official docs for assumption checking
                max_results=5
            )
            search_tasks.append(search_service.search(search_request))
        
        search_responses = await asyncio.gather(*search_tasks)
        
        # Combine all search results
        all_evidence = []
        for response in search_responses:
            if not response.error:
                all_evidence.extend(response.results)
        
        print(f"    Found {len(all_evidence)} pieces of evidence")
        
        # Validate each assumption
        validation_tasks = []
        for assumption in assumptions:
            validation_tasks.append(self._validate_single_assumption(assumption, all_evidence))
        
        validated_assumptions = await asyncio.gather(*validation_tasks)
        
        return [a for a in validated_assumptions if a is not None]
    
    def _generate_search_queries(self, assumptions: List[str]) -> List[str]:
        """Generate search queries to find evidence for assumptions"""
        queries = []
        
        for assumption in assumptions:
            # Extract key terms from assumption
            key_terms = []
            
            # Look for specific HPC terms
            hpc_terms = ['jupyterhub', 'work', 'home', 'ssh', 'slurm', 'module', 'filesystem', 'storage', 'cluster']
            for term in hpc_terms:
                if term.lower() in assumption.lower():
                    key_terms.append(term)
            
            # Create search query
            if key_terms:
                query = ' '.join(key_terms[:3])  # Use top 3 terms
            else:
                # Fallback: use first few words of assumption
                words = assumption.split()[:4]
                query = ' '.join(words)
            
            queries.append(query)
        
        return queries
    
    async def _validate_single_assumption(self, assumption: str, evidence_sources: List[SearchResult]) -> UserAssumption:
        """Validate a single assumption against evidence sources"""
        
        # Prepare evidence content
        evidence_content = ""
        for i, source in enumerate(evidence_sources, 1):
            evidence_content += f"\nEVIDENCE {i}:\n"
            evidence_content += f"Title: {source.title}\n"
            evidence_content += f"Content: {source.content[:800]}...\n\n"
        
        system_prompt = """You are fact-checking a user assumption against HPC documentation.

Your task: Instead of saying what is FALSE, reformulate the assumption into what IS actually true according to the documentation.

PROCESS:
1. Check if the assumption is supported by the evidence
2. If supported: state what the documentation confirms
3. If not supported: reformulate to state what the documentation actually says instead

IMPORTANT: Only state what IS backed by documentation. Do not state what ISN'T true.

Respond with:
VERDICT: SUPPORTED or REFORMULATED
FACTUAL_STATEMENT: [What the documentation actually says]
CONFIDENCE: [0.0-1.0]"""

        content = f"USER ASSUMPTION: {assumption}\n\nEVIDENCE:\n{evidence_content}"
        
        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=content)
        ]
        
        try:
            response = await self.llm.ainvoke(messages)
            response_text = response.content.strip()
            
            # Parse verdict
            is_valid = "VERDICT: SUPPORTED" in response_text
            
            # Extract factual statement
            factual_statement = assumption  # Default to original
            if "FACTUAL_STATEMENT:" in response_text:
                factual_statement = response_text.split("FACTUAL_STATEMENT:")[1].split("CONFIDENCE:")[0].strip()
            
            # Extract confidence
            confidence = 0.5  # Default
            confidence_patterns = [
                r"CONFIDENCE:\s*([0-9]*\.?[0-9]+)",
                r"confidence.*?([0-9]*\.?[0-9]+)",
                r"([0-9]*\.?[0-9]+)"
            ]
            
            for pattern in confidence_patterns:
                match = re.search(pattern, response_text, re.IGNORECASE)
                if match:
                    try:
                        confidence = float(match.group(1))
                        confidence = max(0.0, min(1.0, confidence))  # Clamp to [0,1]
                        break
                    except (ValueError, IndexError):
                        continue
            
            return UserAssumption(
                assumption=factual_statement,  # Use reformulated factual statement
                is_valid=is_valid,
                evidence=evidence_content[:500] + "..." if len(evidence_content) > 500 else evidence_content,
                confidence=confidence
            )
            
        except Exception as e:
            print(f"      [ERROR] Error validating assumption: {str(e)}")
            return UserAssumption(
                assumption=assumption,
                is_valid=False,
                evidence=f"Error during validation: {str(e)}",
                confidence=0.1
            )
