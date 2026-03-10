#!/usr/bin/env python3
"""
HPC Deep Research Workflow with Phoenix Tracing and Fact-Checking Hardening
Searches both documentation and ticket knowledgebase in parallel
Creates comprehensive reports based on search results with fact-checking mechanisms
"""

import asyncio
import os
import sys
import json
import requests
import re
import argparse
from typing import Dict, List, Any, Optional, Tuple, Set
from datetime import datetime
import uuid
from enum import Enum
from dataclasses import dataclass

# Phoenix tracing imports (optional)
try:
    from phoenix.otel import register
    from opentelemetry import trace
    PHOENIX_AVAILABLE = True
except ImportError:
    PHOENIX_AVAILABLE = False
    print(" Phoenix tracing not available (install phoenix-otel)")

# LangChain imports
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_openai import ChatOpenAI
from langchain.callbacks.base import BaseCallbackHandler

# Pydantic for data models
from pydantic import BaseModel, Field

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Configuration
OPENAI_COMPATIBLE_BASE_URL = "http://lme49.cs.fau.de:30000/v1"
OPENAI_COMPATIBLE_API_KEY = "dummy"
OPENAI_COMPATIBLE_MODEL = "openai/gpt-oss-120b"

ELASTIC_URL = os.getenv("ELASTIC_URL", "http://localhost:9200")
DOCS_INDEX = "docs"
TICKETS_INDEX = "tickets"

# Global tracing variables
tracer_provider = None
tracing_enabled = False

def setup_tracing(enable_trace: bool = False):
    """Setup Phoenix tracing if requested and available"""
    global tracer_provider, tracing_enabled
    
    if not enable_trace:
        print(" Tracing disabled")
        return
    
    if not PHOENIX_AVAILABLE:
        print(" Phoenix tracing requested but not available")
        return
    
    try:
        tracer_provider = register(
            project_name="hpc-deep-research",
            endpoint="http://localhost:6006/v1/traces",
            auto_instrument=True
        )
        tracing_enabled = True
        print(" Phoenix tracing enabled at http://localhost:6006")
    except Exception as e:
        print(f" Phoenix tracing setup failed: {e}")
        tracing_enabled = False

# Enhanced callback handler for LLM tracing
class HPCLLMCallbackHandler(BaseCallbackHandler):
    """Callback handler for HPC-specific LLM tracing"""
    
    def __init__(self):
        super().__init__()
        self.tracer = trace.get_tracer(__name__) if tracing_enabled else None
        self.current_span = None
    
    def on_llm_start(self, serialized: Dict[str, Any], prompts: List[str], **kwargs) -> None:
        """Called when LLM starts generating"""
        if not self.tracer:
            return
            
        self.current_span = self.tracer.start_span("HPC LLM Generation")
        self.current_span.set_attribute("llm.model", OPENAI_COMPATIBLE_MODEL)
        self.current_span.set_attribute("llm.prompts_count", len(prompts))
        self.current_span.set_attribute("llm.total_prompt_length", sum(len(p) for p in prompts))
        
        if prompts:
            preview = prompts[0][:200] + "..." if len(prompts[0]) > 200 else prompts[0]
            self.current_span.set_attribute("llm.prompt_preview", preview)
        
        if tracing_enabled:
            print(f" Phoenix: HPC LLM generation starting")
    
    def on_llm_end(self, response, **kwargs) -> None:
        """Called when LLM finishes generating"""
        if not self.current_span:
            return
            
        if hasattr(response, 'generations') and response.generations:
            total_length = 0
            for gen_list in response.generations:
                for gen in gen_list:
                    if hasattr(gen, 'text'):
                        total_length += len(gen.text)
                    elif hasattr(gen, 'message') and hasattr(gen.message, 'content'):
                        total_length += len(gen.message.content)
            
            self.current_span.set_attribute("llm.response_length", total_length)
            self.current_span.set_attribute("llm.generations_count", len(response.generations))
            
            # Add response preview
            if response.generations and response.generations[0]:
                first_gen = response.generations[0][0]
                if hasattr(first_gen, 'text'):
                    preview = first_gen.text[:200] + "..." if len(first_gen.text) > 200 else first_gen.text
                elif hasattr(first_gen, 'message') and hasattr(first_gen.message, 'content'):
                    preview = first_gen.message.content[:200] + "..." if len(first_gen.message.content) > 200 else first_gen.message.content
                else:
                    preview = "No content available"
                self.current_span.set_attribute("llm.response_preview", preview)
        
        self.current_span.end()
        self.current_span = None
        
        if tracing_enabled:
            print(f" Phoenix: HPC LLM generation completed")
    
    def on_llm_error(self, error: Exception, **kwargs) -> None:
        """Called when LLM encounters an error"""
        if self.current_span:
            self.current_span.set_attribute("llm.error", str(error))
            self.current_span.set_attribute("llm.error_type", type(error).__name__)
            self.current_span.end()
            self.current_span = None
        
        if tracing_enabled:
            print(f" Phoenix: HPC LLM generation error: {error}")

# Data models
class HPCSearchResult(BaseModel):
    """HPC search result from Elasticsearch"""
    id: str = Field(description="Document ID")
    title: str = Field(description="Document title")
    text: str = Field(description="Document content")
    score: float = Field(description="Relevance score")
    highlight: Optional[str] = Field(description="Highlighted passages")
    source_type: str = Field(description="docs or tickets")
    url: Optional[str] = Field(description="URL for documentation")
    ticket_id: Optional[str] = Field(description="Ticket ID for tickets")
    keywords: Optional[List[str]] = Field(description="Keywords for tickets")

class HPCTicketResult(BaseModel):
    """HPC ticket result from Elasticsearch"""
    id: str = Field(description="Ticket ID")
    title: str = Field(description="Ticket title")
    text: str = Field(description="Ticket content")
    score: float = Field(description="Relevance score")
    highlight: Optional[str] = Field(description="Highlighted passages")
    ticket_id: str = Field(description="Ticket ID")
    keywords: Optional[List[str]] = Field(description="Keywords for tickets")

class HPCSearchResults(BaseModel):
    """Collection of HPC search results"""
    query: str = Field(description="Original search query")
    docs_results: List[HPCSearchResult] = Field(description="Documentation results")
    tickets_results: List[HPCTicketResult] = Field(description="Ticket results")
    total_docs_found: int = Field(description="Total docs found")
    total_tickets_found: int = Field(description="Total tickets found")
    error: Optional[str] = Field(description="Error message if search failed")

class FactCheckResult(BaseModel):
    """Fact-checking result"""
    claim: str = Field(description="Claim to be fact-checked")
    evidence: Optional[str] = Field(description="Evidence supporting or refuting the claim")
    verdict: str = Field(description="Fact-checking verdict (e.g., 'TRUE', 'FALSE', 'UNKNOWN')")
    confidence: float = Field(description="Confidence level of the fact-checking result")

class FactCheckResults(BaseModel):
    """Collection of fact-checking results"""
    query: str = Field(description="Original search query")
    fact_check_results: List[FactCheckResult] = Field(description="Fact-checking results")

# Elasticsearch search functions
async def search_elasticsearch_index(query: str, index_name: str) -> Tuple[List[HPCSearchResult], int, Optional[str]]:
    """Search a specific Elasticsearch index"""
    try:
        # Configure search fields based on index
        if index_name == DOCS_INDEX:
            fields = ["title^2", "text", "titles"]
            source_fields = ["id", "title", "text", "url", "titles"]
        else:  # tickets index
            fields = ["title^2", "summary^1.5", "keywords^1.5", "text", 
                     "problem_description", "solution", "actions_taken"]
            source_fields = ["id", "ticket_id", "title", "text", "keywords", 
                           "summary", "problem_description", "solution"]
        
        search_data = {
            "query": {
                "multi_match": {
                    "query": query,
                    "fields": fields,
                    "type": "best_fields",
                    "fuzziness": "AUTO"
                }
            },
            "size": 10,
            "_source": source_fields,
            "highlight": {
                "fields": {
                    "text": {"fragment_size": 200, "number_of_fragments": 3},
                    "title": {},
                    "summary": {},
                    "solution": {"fragment_size": 200, "number_of_fragments": 2}
                }
            },
            "sort": [
                {"_score": {"order": "desc"}}
            ]
        }

        search_url = f"{ELASTIC_URL}/{index_name}/_search"
        headers = {"Content-Type": "application/json"}
        
        response = requests.post(search_url, json=search_data, headers=headers, timeout=30)
        
        if response.status_code == 200:
            raw_results = response.json()
            hits = raw_results.get("hits", {}).get("hits", [])
            total = raw_results.get("hits", {}).get("total", {}).get("value", 0)
            
            results = []
            for hit in hits:
                source = hit.get("_source", {})
                highlight = hit.get("highlight", {})
                
                # Combine all highlights
                all_highlights = []
                for field, fragments in highlight.items():
                    all_highlights.extend(fragments)
                highlight_text = " ... ".join(all_highlights) if all_highlights else None
                
                if index_name == DOCS_INDEX:
                    result = HPCSearchResult(
                        id=source.get("id", ""),
                        title=source.get("title", ""),
                        text=source.get("text", "")[:1000],  # Truncate for memory
                        score=hit.get("_score", 0.0),
                        highlight=highlight_text,
                        source_type=index_name,
                        url=source.get("url") if index_name == DOCS_INDEX else None,
                        ticket_id=source.get("ticket_id") if index_name == TICKETS_INDEX else None,
                        keywords=source.get("keywords") if index_name == TICKETS_INDEX else None
                    )
                else:
                    result = HPCTicketResult(
                        id=source.get("id", ""),
                        title=source.get("title", ""),
                        text=source.get("text", "")[:1000],  # Truncate for memory
                        score=hit.get("_score", 0.0),
                        highlight=highlight_text,
                        ticket_id=source.get("ticket_id", ""),
                        keywords=source.get("keywords", [])
                    )
                
                results.append(result)
            
            return results, total, None
        else:
            return [], 0, f"Elasticsearch error: {response.status_code} - {response.text}"
            
    except Exception as e:
        return [], 0, f"Search error: {str(e)}"

async def parallel_hpc_search(query: str) -> HPCSearchResults:
    """Search both documentation and tickets in parallel"""
    tracer = trace.get_tracer(__name__) if tracing_enabled else None
    
    # Use the same pattern as the main function for consistent tracing
    if not tracer:
        class DummySpan:
            def __enter__(self): return self
            def __exit__(self, *args): pass
            def set_attribute(self, *args): pass
        search_span = DummySpan()
    else:
        search_span = tracer.start_as_current_span("Parallel HPC Knowledge Search")
    
    with search_span as span:
        if span and hasattr(span, 'set_attribute'):
            span.set_attribute("search.query", query)
            span.set_attribute("search.timestamp", datetime.now().isoformat())
        
        try:
            print(f"    Searching docs index: {DOCS_INDEX}")
            print(f"    Searching tickets index: {TICKETS_INDEX}")
            
            # Execute both searches in parallel
            docs_task = search_elasticsearch_index(query, DOCS_INDEX)
            tickets_task = search_elasticsearch_index(query, TICKETS_INDEX)
            
            docs_results, docs_total, docs_error = await docs_task
            tickets_results, tickets_total, tickets_error = await tickets_task
            
            # Log search results
            print(f"    Docs found: {docs_total} ({len(docs_results)} returned)")
            print(f"    Tickets found: {tickets_total} ({len(tickets_results)} returned)")
            
            # Combine errors if any
            error = None
            if docs_error and tickets_error:
                error = f"Docs: {docs_error}; Tickets: {tickets_error}"
                print(f"    Both searches failed: {error}")
            elif docs_error:
                error = f"Docs error: {docs_error}"
                print(f"    Docs search failed: {docs_error}")
            elif tickets_error:
                error = f"Tickets error: {tickets_error}"
                print(f"    Tickets search failed: {tickets_error}")
            
            if span and hasattr(span, 'set_attribute'):
                span.set_attribute("search.docs_results", len(docs_results))
                span.set_attribute("search.tickets_results", len(tickets_results))
                span.set_attribute("search.docs_total", docs_total)
                span.set_attribute("search.tickets_total", tickets_total)
                span.set_attribute("search.success", not bool(error))
                span.set_attribute("search.docs_index", DOCS_INDEX)
                span.set_attribute("search.tickets_index", TICKETS_INDEX)
                if error:
                    span.set_attribute("search.error", error)
                
                # Add detailed results info
                if docs_results:
                    span.set_attribute("search.docs_top_score", docs_results[0].score)
                    span.set_attribute("search.docs_titles", json.dumps([d.title[:50] for d in docs_results[:3]]))
                if tickets_results:
                    span.set_attribute("search.tickets_top_score", tickets_results[0].score)
                    span.set_attribute("search.tickets_ids", json.dumps([t.ticket_id for t in tickets_results[:3]]))
            
            return HPCSearchResults(
                query=query,
                docs_results=docs_results,
                tickets_results=tickets_results,
                total_docs_found=docs_total,
                total_tickets_found=tickets_total,
                error=error
            )
            
        except Exception as e:
            error_msg = f"Parallel search error: {str(e)}"
            print(f"    Search exception: {error_msg}")
            
            if span and hasattr(span, 'set_attribute'):
                span.set_attribute("search.error", error_msg)
                span.set_attribute("search.error_type", type(e).__name__)
            
            return HPCSearchResults(
                query=query,
                docs_results=[],
                tickets_results=[],
                total_docs_found=0,
                total_tickets_found=0,
                error=error_msg
            )

def extract_search_queries_from_response(response_text: str) -> List[str]:
    """Extract search queries from LLM response"""
    search_queries = []
    
    # Look for definitive statements
    lines = response_text.split('\n')
    for line in lines:
        if line.strip() and (line.strip().startswith(('1.', '2.', '3.', '4.', '5.', '-', '*'))):
            query = re.sub(r'^\d+\.\s*', '', line.strip())
            query = re.sub(r'^[-*]\s*', '', query.strip())
            if query and len(query) > 3:
                search_queries.append(query)
    
    # Fallback: look for quoted terms
    quoted_terms = re.findall(r'"([^"]+)"', response_text)
    for term in quoted_terms:
        if len(term) > 3 and term not in search_queries:
            search_queries.append(term)
    
    return search_queries[:5]  # Limit to 5 queries

async def fact_check_claims(claims: List[str], search_results: List[HPCSearchResults], llm) -> List[FactCheckResult]:
    """Fact-check claims against search results with parallel processing"""
    tracer = trace.get_tracer(__name__) if tracing_enabled else None
    
    with tracer.start_as_current_span("Fact-Check Claims") if tracer else DummySpan() as span:
        if span and hasattr(span, 'set_attribute'):
            span.set_attribute("claims_count", len(claims))
        
        # Compile all available evidence
        all_evidence = []
        faq_evidence = []  # Special tracking for FAQ content
        
        for search_result in search_results:
            for doc in search_result.docs_results:
                evidence_text = f"[DOC] {doc.title}: {doc.text}"
                all_evidence.append(evidence_text)
                
                # Track FAQ content separately
                if "faq" in doc.title.lower() or "faq" in doc.url.lower():
                    faq_evidence.append(evidence_text)
            
            for ticket in search_result.tickets_results:
                all_evidence.append(f"[TICKET] {ticket.title}: {ticket.text}")
        
        # Limit evidence to prevent token overflow
        evidence_text = "\n".join(all_evidence[:15])  # Top 15 pieces of evidence
        faq_text = "\n".join(faq_evidence[:5])  # Top 5 FAQ entries
        
        print(f"    Parallel fact-checking {len(claims)} claims...")
        
        # Create fact-checking tasks
        tasks = []
        for i, claim in enumerate(claims):
            task = fact_check_single_claim(claim, evidence_text, faq_text, llm, i)
            tasks.append(task)
        
        # Execute all fact-checks in parallel
        results = await asyncio.gather(*tasks)
        
        if span and hasattr(span, 'set_attribute'):
            span.set_attribute("fact_check_results_count", len(results))
            true_count = len([r for r in results if r.verdict == "TRUE"])
            false_count = len([r for r in results if r.verdict == "FALSE"])
            unknown_count = len([r for r in results if r.verdict == "UNKNOWN"])
            span.set_attribute("true_claims", true_count)
            span.set_attribute("false_claims", false_count)
            span.set_attribute("unknown_claims", unknown_count)
        
        return results

async def fact_check_single_claim(claim: str, evidence_text: str, faq_text: str, llm, index: int) -> FactCheckResult:
    """Fact-check a single claim against evidence"""
    tracer = trace.get_tracer(__name__) if tracing_enabled else None
    
    with tracer.start_as_current_span(f"Fact-Check Claim {index}") if tracer else DummySpan() as span:
        fact_check_prompt = f"""You are a meticulous HPC fact-checker. Verify if the following claim is supported by the provided evidence.

CLAIM TO VERIFY:
{claim}

AVAILABLE EVIDENCE:
{evidence_text}

FAQ EVIDENCE (Special Attention):
{faq_text}

FACT-CHECKING INSTRUCTIONS:
1. **FAQ Priority**: If the claim relates to FAQ content, check the FAQ evidence carefully
2. **Exact Matches**: Look for direct statements that support or contradict the claim
3. **Reasonable Inferences**: Accept claims that are reasonable interpretations of documented information
4. **Context Matters**: Consider the context and intent of the claim
5. **Documentation Gaps**: If evidence is silent, mark as UNKNOWN rather than FALSE

VERDICT OPTIONS:
- TRUE: The claim is directly supported by the evidence or is a reasonable interpretation
- FALSE: The claim is directly contradicted by the evidence
- UNKNOWN: The evidence is insufficient or silent on this claim

RESPONSE FORMAT:
VERDICT: [TRUE/FALSE/UNKNOWN]
CONFIDENCE: [0.0-1.0]
EVIDENCE: [Quote the specific evidence that supports your verdict, or explain why it's unknown]

Be especially careful with FAQ-related claims - they often contain practical solutions that should be preserved."""

        messages = [
            SystemMessage(content="You are a careful fact-checker who values both accuracy and helpfulness, especially for FAQ content."),
            HumanMessage(content=fact_check_prompt)
        ]
        
        try:
            response = await llm.ainvoke(messages)
            response_text = response.content
            
            # Parse the response
            verdict_match = re.search(r'VERDICT:\s*(TRUE|FALSE|UNKNOWN)', response_text, re.IGNORECASE)
            confidence_match = re.search(r'CONFIDENCE:\s*([0-9.]+)', response_text)
            evidence_match = re.search(r'EVIDENCE:\s*(.+)', response_text, re.DOTALL)
            
            verdict = verdict_match.group(1).upper() if verdict_match else "UNKNOWN"
            confidence = float(confidence_match.group(1)) if confidence_match else 0.0
            evidence = evidence_match.group(1).strip() if evidence_match else "No evidence provided"
            
            result = FactCheckResult(
                claim=claim,
                verdict=verdict,
                confidence=confidence,
                evidence=evidence
            )
            
            print(f"    Fact-checked: {claim[:50]}... → {verdict} ({confidence:.2f})")
            
            if span and hasattr(span, 'set_attribute'):
                span.set_attribute("claim", claim)
                span.set_attribute("verdict", verdict)
                span.set_attribute("confidence", confidence)
            
            return result
            
        except Exception as e:
            print(f"    Error fact-checking claim: {str(e)}")
            return FactCheckResult(
                claim=claim,
                verdict="UNKNOWN",
                confidence=0.0,
                evidence=f"Error during fact-checking: {str(e)}"
            )

async def detect_contradictions(user_query: str, search_results: List[HPCSearchResults], llm) -> List[str]:
    """Detect contradictions between user assumptions and documentation"""
    tracer = trace.get_tracer(__name__) if tracing_enabled else None
    
    if not tracer:
        class DummySpan:
            def __enter__(self): return self
            def __exit__(self, *args): pass
            def set_attribute(self, *args): pass
        contradiction_span = DummySpan()
    else:
        contradiction_span = tracer.start_as_current_span("Detect Contradictions")
    
    with contradiction_span as span:
        if span and hasattr(span, 'set_attribute'):
            span.set_attribute("contradiction.user_query", user_query)
        
        try:
            # Compile evidence
            all_evidence = []
            for search_result in search_results:
                for doc in search_result.docs_results:
                    all_evidence.append(f"[DOC:{doc.id}] {doc.title}: {doc.text}")
                for ticket in search_result.tickets_results:
                    all_evidence.append(f"[TICKET:{ticket.ticket_id}] {ticket.title}: {ticket.text}")
            
            evidence_text = "\n\n".join(all_evidence[:15])  # Limit evidence
            
            contradiction_prompt = """You are an expert HPC system administrator analyzing user questions for potential misconceptions.

USER QUERY: {user_query}

OFFICIAL DOCUMENTATION AND TICKETS:
{evidence_text}

Task: Identify any assumptions or claims in the user's query that contradict the official documentation.

Look for common misconceptions about:
- Storage systems (temporary vs persistent, quotas, locations)
- Job scheduling and resource allocation
- Software environments and modules
- Cluster configurations and access methods
- File system properties and behaviors

If you find contradictions, list them clearly. If no contradictions are found, respond with "NO_CONTRADICTIONS".

Format your response as:
CONTRADICTION_1: [User assumption] contradicts [Official documentation fact]
CONTRADICTION_2: [User assumption] contradicts [Official documentation fact]
etc.

Or simply: NO_CONTRADICTIONS"""

            messages = [HumanMessage(content=contradiction_prompt.format(user_query=user_query, evidence_text=evidence_text))]
            
            response = await llm.ainvoke(messages)
            
            contradictions = []
            response_text = response.content
            
            if "NO_CONTRADICTIONS" not in response_text.upper():
                # Extract contradictions
                contradiction_matches = re.findall(r'CONTRADICTION_\d+:\s*(.+)', response_text, re.IGNORECASE)
                contradictions = [match.strip() for match in contradiction_matches]
            
            if span and hasattr(span, 'set_attribute'):
                span.set_attribute("contradiction.found_count", len(contradictions))
                span.set_attribute("contradiction.detected", len(contradictions) > 0)
            
            if contradictions:
                print(f"    Detected {len(contradictions)} potential contradictions")
                for i, contradiction in enumerate(contradictions, 1):
                    print(f"      {i}. {contradiction}")
            else:
                print("    No contradictions detected between user query and documentation")
            
            return contradictions
            
        except Exception as e:
            print(f"    Error detecting contradictions: {e}")
            if span and hasattr(span, 'set_attribute'):
                span.set_attribute("contradiction.error", str(e))
            return []

def extract_claims_from_response(response_text: str) -> List[str]:
    """Extract factual claims from LLM response for fact-checking"""
    claims = []
    
    # Look for definitive statements
    sentences = re.split(r'[.!?]+', response_text)
    
    # Priority patterns - more important claims get higher priority
    high_priority_patterns = [
        r'\b(is|are)\s+(temporary|permanent|persistent|ephemeral)\b',  # Storage type claims
        r'\b(always|never)\s+(deleted|removed|cleaned|backed up)\b',  # Absolute behavior claims
        r'\b(quota|limit)\s+(is|are)\s+\d+',  # Specific quota claims
        r'\b(located|stored|mounted)\s+(in|on|at)\s+\S+',  # Location claims
    ]
    
    medium_priority_patterns = [
        r'\b(has|have|will|can|cannot|must|should)\b',  # Definitive verbs
        r'\b(all|every|only|exactly)\s+\w+',  # Absolute terms with objects
        r'\b(size|capacity)\s+(of|is)\s+',  # Resource specifications
    ]
    
    low_priority_patterns = [
        r'\b(typically|usually|generally|often)\b',  # Qualified statements
        r'\b(may|might|could|would)\b',  # Conditional statements
    ]
    
    # Extract claims with priority scoring
    claim_scores = []
    
    for sentence in sentences:
        sentence = sentence.strip()
        if len(sentence) < 15:  # Skip very short sentences
            continue
            
        # Skip sentences that are clearly not factual claims
        if any(skip_pattern in sentence.lower() for skip_pattern in [
            'for example', 'such as', 'including', 'see also', 'refer to',
            'please note', 'important:', 'note:', 'warning:', 'tip:'
        ]):
            continue
            
        score = 0
        matched = False
        
        # Check high priority patterns
        for pattern in high_priority_patterns:
            if re.search(pattern, sentence, re.IGNORECASE):
                score = 3
                matched = True
                break
        
        # Check medium priority patterns if not already matched
        if not matched:
            for pattern in medium_priority_patterns:
                if re.search(pattern, sentence, re.IGNORECASE):
                    score = 2
                    matched = True
                    break
        
        # Check low priority patterns if not already matched
        if not matched:
            for pattern in low_priority_patterns:
                if re.search(pattern, sentence, re.IGNORECASE):
                    score = 1
                    matched = True
                    break
        
        if matched:
            # Clean up the claim
            claim = sentence.strip()
            if claim and claim not in [c[0] for c in claim_scores]:
                claim_scores.append((claim, score))
    
    # Sort by score (highest first) and extract unique claims
    claim_scores.sort(key=lambda x: x[1], reverse=True)
    
    # Dynamic limit based on content and priority
    high_priority_claims = [c[0] for c in claim_scores if c[1] == 3]
    medium_priority_claims = [c[0] for c in claim_scores if c[1] == 2]
    low_priority_claims = [c[0] for c in claim_scores if c[1] == 1]
    
    # Intelligent selection: prioritize important claims but don't overwhelm
    selected_claims = []
    
    # Always include high priority claims (up to 8)
    selected_claims.extend(high_priority_claims[:8])
    
    # Add medium priority claims if we have room (up to 6 more)
    remaining_slots = max(0, 15 - len(selected_claims))
    selected_claims.extend(medium_priority_claims[:min(6, remaining_slots)])
    
    # Add low priority claims if we still have room (up to 4 more)
    remaining_slots = max(0, 15 - len(selected_claims))
    selected_claims.extend(low_priority_claims[:min(4, remaining_slots)])
    
    print(f"    📊 Extracted {len(selected_claims)} claims for fact-checking:")
    print(f"      • High priority: {len(high_priority_claims)} (selected: {len([c for c in selected_claims if c in high_priority_claims])})")
    print(f"      • Medium priority: {len(medium_priority_claims)} (selected: {len([c for c in selected_claims if c in medium_priority_claims])})")
    print(f"      • Low priority: {len(low_priority_claims)} (selected: {len([c for c in selected_claims if c in low_priority_claims])})")
    
    return selected_claims

async def extract_user_assumptions(user_query: str, llm) -> List[str]:
    """Extract implicit assumptions from the user's query using LLM (proportional to complexity)"""
    
    # Determine appropriate number of assumptions based on query complexity
    query_words = len(user_query.split())
    if query_words <= 15:
        max_assumptions = 3  # Simple queries: 3 assumptions
    elif query_words <= 30:
        max_assumptions = 5  # Medium queries: 5 assumptions
    else:
        max_assumptions = 8  # Complex queries: 8 assumptions
    
    extraction_prompt = f"""You are an expert at identifying implicit assumptions in HPC user questions. Analyze the following user query and extract the underlying assumptions the user might be making.

USER QUERY:
{user_query}

INSTRUCTIONS:
1. **Identify implicit assumptions**: What does the user seem to assume about how the system works?
2. **Focus on technical assumptions**: About filesystems, permissions, mounts, services, configurations
3. **Consider misconceptions**: What might the user incorrectly believe?
4. **Be specific**: Make assumptions concrete and testable
5. **Keep it focused**: Extract only the {max_assumptions} MOST RELEVANT assumptions for this specific query
6. **Quality over quantity**: Better to have fewer, highly relevant assumptions than many generic ones

EXAMPLES OF GOOD ASSUMPTIONS:
- "JupyterHub automatically mounts all filesystems available on login nodes"
- "Directory access problems are always caused by permission issues"
- "Environment variables are identical across all HPC services"
- "$WORK storage is automatically available in all HPC interfaces"

RESPONSE FORMAT:
Return a numbered list of assumptions, one per line:
1. [First assumption]
2. [Second assumption]
...

Extract the {max_assumptions} most relevant assumptions now:"""

    messages = [
        SystemMessage(content="You are an expert at identifying implicit user assumptions in HPC technical questions. Focus on quality and relevance over quantity."),
        HumanMessage(content=extraction_prompt)
    ]
    
    try:
        response = await llm.ainvoke(messages)
        response_text = response.content
        
        # Parse the numbered list
        assumptions = []
        lines = response_text.strip().split('\n')
        
        for line in lines:
            line = line.strip()
            # Match patterns like "1. assumption" or "- assumption"
            if re.match(r'^\d+\.\s+', line) or re.match(r'^-\s+', line):
                # Remove the number/bullet and clean up
                assumption = re.sub(r'^\d+\.\s+', '', line)
                assumption = re.sub(r'^-\s+', '', assumption)
                assumption = assumption.strip()
                if assumption and len(assumption) > 10:  # Filter out very short assumptions
                    assumptions.append(assumption)
        
        # Limit to the determined number of assumptions
        final_assumptions = assumptions[:max_assumptions]
        
        print(f"    📊 Extracted {len(final_assumptions)} assumptions (query complexity: {query_words} words)")
        
        return final_assumptions
        
    except Exception as e:
        print(f"    Error extracting assumptions: {str(e)}")
        # Fallback to fewer generic assumptions for simple queries
        fallback_assumptions = [
            "The system should work consistently across all access methods",
            "Standard HPC resources are available in all interfaces"
        ]
        if max_assumptions >= 3:
            fallback_assumptions.append("Documentation covers all common use cases")
        
        return fallback_assumptions[:max_assumptions]

async def check_user_assumptions(assumptions: List[str], search_results: List[HPCSearchResults], llm) -> List[FactCheckResult]:
    """Check user assumptions against search results"""
    tracer = trace.get_tracer(__name__) if tracing_enabled else None
    
    with tracer.start_as_current_span("Check User Assumptions") if tracer else DummySpan() as span:
        if span and hasattr(span, 'set_attribute'):
            span.set_attribute("assumptions_count", len(assumptions))
        
        # Compile all available evidence from our searches
        all_evidence = []
        
        for search_result in search_results:
            for doc in search_result.docs_results:
                all_evidence.append(f"[DOC] {doc.title}: {doc.text}")
            
            for ticket in search_result.tickets_results:
                all_evidence.append(f"[TICKET] {ticket.title}: {ticket.text}")
        
        # Limit evidence to prevent token overflow
        evidence_text = "\n".join(all_evidence[:20])  # Top 20 pieces of evidence
        
        print(f"    Checking {len(assumptions)} user assumptions against search results...")
        
        # Create assumption-checking tasks
        tasks = []
        for i, assumption in enumerate(assumptions):
            task = check_single_assumption(assumption, evidence_text, llm, i)
            tasks.append(task)
        
        # Execute all checks in parallel
        results = await asyncio.gather(*tasks)
        
        if span and hasattr(span, 'set_attribute'):
            span.set_attribute("assumption_results_count", len(results))
            true_count = len([r for r in results if r.verdict == "TRUE"])
            false_count = len([r for r in results if r.verdict == "FALSE"])
            unknown_count = len([r for r in results if r.verdict == "UNKNOWN"])
            span.set_attribute("true_assumptions", true_count)
            span.set_attribute("false_assumptions", false_count)
            span.set_attribute("unknown_assumptions", unknown_count)
        
        return results

async def check_single_assumption(assumption: str, evidence_text: str, llm, index: int) -> FactCheckResult:
    """Check a single user assumption against evidence"""
    tracer = trace.get_tracer(__name__) if tracing_enabled else None
    
    with tracer.start_as_current_span(f"Check Assumption {index}") if tracer else DummySpan() as span:
        assumption_check_prompt = f"""You are checking whether a user's implicit assumption is supported by the available evidence from HPC documentation and support tickets.

USER ASSUMPTION TO VERIFY:
{assumption}

AVAILABLE EVIDENCE FROM SEARCHES:
{evidence_text}

INSTRUCTIONS:
1. **Check if the assumption is supported**: Does the evidence confirm this assumption?
2. **Look for contradictions**: Does the evidence contradict this assumption?
3. **Consider documentation gaps**: If the evidence is silent, the assumption may be incorrect
4. **Focus on what's documented**: Only what's explicitly stated or clearly implied

VERDICT OPTIONS:
- TRUE: The assumption is supported by the evidence
- FALSE: The assumption is contradicted by the evidence  
- UNKNOWN: The evidence is insufficient to confirm or deny the assumption

RESPONSE FORMAT:
VERDICT: [TRUE/FALSE/UNKNOWN]
CONFIDENCE: [0.0-1.0]
EVIDENCE: [Quote specific evidence that supports your verdict, or explain why it's unknown]

Focus on checking the user's assumptions, not generating new claims."""

        messages = [
            SystemMessage(content="You are checking user assumptions against documented evidence."),
            HumanMessage(content=assumption_check_prompt)
        ]
        
        try:
            response = await llm.ainvoke(messages)
            response_text = response.content
            
            # Parse the response
            verdict_match = re.search(r'VERDICT:\s*(TRUE|FALSE|UNKNOWN)', response_text, re.IGNORECASE)
            confidence_match = re.search(r'CONFIDENCE:\s*([0-9.]+)', response_text)
            evidence_match = re.search(r'EVIDENCE:\s*(.+)', response_text, re.DOTALL)
            
            verdict = verdict_match.group(1).upper() if verdict_match else "UNKNOWN"
            confidence = float(confidence_match.group(1)) if confidence_match else 0.0
            evidence = evidence_match.group(1).strip() if evidence_match else "No evidence provided"
            
            result = FactCheckResult(
                claim=assumption,
                verdict=verdict,
                confidence=confidence,
                evidence=evidence
            )
            
            print(f"    Assumption: {assumption[:50]}... → {verdict} ({confidence:.2f})")
            
            if span and hasattr(span, 'set_attribute'):
                span.set_attribute("assumption", assumption)
                span.set_attribute("verdict", verdict)
                span.set_attribute("confidence", confidence)
            
            return result
            
        except Exception as e:
            print(f"    Error checking assumption: {str(e)}")
            return FactCheckResult(
                claim=assumption,
                verdict="UNKNOWN",
                confidence=0.0,
                evidence=f"Error during assumption checking: {str(e)}"
            )

async def comprehensive_hpc_research(user_query: str) -> Tuple[str, str]:
    """Perform comprehensive HPC research with optional tracing"""
    tracer = trace.get_tracer(__name__) if tracing_enabled else None
    
    if not tracer:
        # If no tracing, use dummy context manager
        class DummySpan:
            def __enter__(self): return self
            def __exit__(self, *args): pass
            def set_attribute(self, *args): pass
        
        main_span = DummySpan()
    else:
        main_span = tracer.start_as_current_span("Comprehensive HPC Research Process")
    
    with main_span as span:
        if span and hasattr(span, 'set_attribute'):
            span.set_attribute("user_query", user_query)
            span.set_attribute("user_query_length", len(user_query))
            span.set_attribute("research_start_time", datetime.now().isoformat())
        
        try:
            # Initialize LLM with callback
            llm_callback = HPCLLMCallbackHandler()
            llm = ChatOpenAI(
                base_url=OPENAI_COMPATIBLE_BASE_URL,
                api_key=OPENAI_COMPATIBLE_API_KEY,
                model=OPENAI_COMPATIBLE_MODEL,
                temperature=0.2,
                max_tokens=2000,
                callbacks=[llm_callback]
            )
            
            # Step 1: Initial analysis and query planning
            print("Analyzing HPC question and planning searches...")
            
            with tracer.start_as_current_span("Initial HPC Analysis & Query Planning") if tracer else DummySpan() as analysis_span:
                system_prompt = """You are an expert HPC (High Performance Computing) system administrator and researcher specializing in NHR@FAU systems.

Analyze the following HPC question and identify the most important search terms for both documentation and historical support tickets.

Create a list of search queries that will help provide a comprehensive answer covering:
- Technical documentation from NHR@FAU
- Historical support tickets with similar issues
- Best practices and solutions

Focus on HPC-specific terms like:
- SLURM batch system (sbatch, srun, salloc)
- Cluster names (Fritz, Alex, Woody, TinyGPU)
- Software modules and environments
- Storage systems and quotas
- GPU allocation and usage
- Python/Conda environments
- MPI and parallel computing
- Job scheduling and resource allocation

Provide your response in this format:
SEARCH QUERIES:
1. [Search term 1]
2. [Search term 2]
3. [Search term 3]
etc."""

                messages = [
                    SystemMessage(content=system_prompt),
                    HumanMessage(content=user_query)
                ]
                
                if analysis_span and hasattr(analysis_span, 'set_attribute'):
                    analysis_span.set_attribute("llm.system_prompt_length", len(system_prompt))
                    analysis_span.set_attribute("llm.user_query_length", len(user_query))
                    analysis_span.set_attribute("llm.messages_count", len(messages))
                
                initial_response = await llm.ainvoke(messages)
                
                if analysis_span and hasattr(analysis_span, 'set_attribute'):
                    analysis_span.set_attribute("llm.response_length", len(initial_response.content))
                    analysis_span.set_attribute("llm.response_preview", initial_response.content[:300] + "...")
                
                print(f"Analysis completed: {len(initial_response.content)} characters")
            
            # Step 2: Extract search queries
            with tracer.start_as_current_span("Extract and Prepare Search Queries") if tracer else DummySpan() as query_span:
                search_queries = extract_search_queries_from_response(initial_response.content)
                
                # Always include the original user query as the first search (1:1 direct search)
                direct_search_queries = [user_query]  # Direct 1:1 search
                direct_search_queries.extend(search_queries)  # Add generated queries
                search_queries = direct_search_queries
                
                # Default HPC searches if none found
                if len(search_queries) == 1:  # Only the direct query exists
                    search_queries.extend([
                        "SLURM batch job submission",
                        "Python conda environment setup", 
                        "GPU allocation Fritz cluster",
                        "storage quota exceeded",
                        "module load software"
                    ])
                
                if query_span and hasattr(query_span, 'set_attribute'):
                    query_span.set_attribute("search_queries_count", len(search_queries))
                    query_span.set_attribute("search_queries_planned", json.dumps(search_queries))
                    query_span.set_attribute("direct_query_included", True)
                    query_span.set_attribute("fallback_queries_used", len(search_queries) == 6 and search_queries[1] == "SLURM batch job submission")
                
                print(f"Executing {len(search_queries)} searches (including direct 1:1 search)...")
                print(f"  Direct search: {user_query}")
                for i, query in enumerate(search_queries[1:], 2):
                    print(f"  Generated {i-1}: {query}")
            
            # Step 3: Comprehensive documentation search first
            print("\n🔍 Stage 1: Comprehensive documentation search...")
            
            with tracer.start_as_current_span("Documentation Search") if tracer else DummySpan() as doc_search_span:
                # Execute all searches on documentation index only
                doc_search_tasks = []
                for query in search_queries:
                    task = search_elasticsearch_index(query, DOCS_INDEX)
                    doc_search_tasks.append(task)
                
                print(f"    Executing {len(doc_search_tasks)} documentation searches...")
                doc_search_results = await asyncio.gather(*doc_search_tasks)
                
                # Collect all documentation results
                all_doc_results = []
                total_docs_found = 0
                
                for i, results in enumerate(doc_search_results):
                    query = search_queries[i]
                    print(f"    Doc Search {i+1}: {query}")
                    print(f"      Docs found: {results[1]} ({len(results[0])} returned)")
                    
                    total_docs_found += results[1]
                    
                    for doc in results[0]:
                        all_doc_results.append({
                            'type': 'doc',
                            'id': doc.id,
                            'title': doc.title,
                            'text': doc.text,
                            'score': doc.score,
                            'highlight': doc.highlight,
                            'url': doc.url,
                            'source_query': query
                        })
                
                if doc_search_span and hasattr(doc_search_span, 'set_attribute'):
                    doc_search_span.set_attribute("total_docs_found", total_docs_found)
                    doc_search_span.set_attribute("doc_results_collected", len(all_doc_results))
                
                print(f"    📚 Total documentation results: {len(all_doc_results)} from {total_docs_found} found")

            # Step 4: Evaluate documentation sufficiency
            print("\n📊 Evaluating documentation sufficiency...")
            
            with tracer.start_as_current_span("Documentation Sufficiency Assessment") if tracer else DummySpan() as sufficiency_span:
                # Create assessment prompt
                doc_assessment_content = f"Original Question: {user_query}\n\n"
                doc_assessment_content += "=== DOCUMENTATION SEARCH RESULTS ===\n\n"
                
                for i, doc_result in enumerate(all_doc_results[:10], 1):  # Top 10 for assessment
                    doc_assessment_content += f"DOC #{i}:\n"
                    doc_assessment_content += f"Title: {doc_result['title']}\n"
                    doc_assessment_content += f"URL: {doc_result['url']}\n"
                    doc_assessment_content += f"Content: {doc_result['text'][:800]}...\n"
                    if doc_result['highlight']:
                        doc_assessment_content += f"Highlights: {doc_result['highlight']}\n"
                    doc_assessment_content += "\n"
                
                sufficiency_prompt = """You are an HPC documentation analyst. Assess whether the documentation results above provide sufficient information to answer the user's question comprehensively.

ASSESSMENT CRITERIA:
- Can the question be answered completely using only the documentation?
- Are there specific technical details, commands, or procedures covered?
- Is the information authoritative and complete?
- Are there any gaps that would require practical user experience (tickets) to fill?

Respond with one of:
- SUFFICIENT: Documentation provides complete answer
- INSUFFICIENT: Need additional sources (tickets) for complete answer
- PARTIAL: Documentation covers basics but lacks practical details

Provide a brief explanation (2-3 sentences) of your assessment."""

                sufficiency_messages = [
                    SystemMessage(content=sufficiency_prompt),
                    HumanMessage(content=doc_assessment_content)
                ]
                
                print("    🤖 Assessing documentation completeness...")
                sufficiency_response = await llm.ainvoke(sufficiency_messages)
                sufficiency_assessment = sufficiency_response.content.strip()
                
                # Parse assessment
                needs_tickets = "INSUFFICIENT" in sufficiency_assessment or "PARTIAL" in sufficiency_assessment
                
                print(f"    📋 Assessment: {sufficiency_assessment[:100]}...")
                print(f"    🎯 Ticket search needed: {'Yes' if needs_tickets else 'No'}")
                
                if sufficiency_span and hasattr(sufficiency_span, 'set_attribute'):
                    sufficiency_span.set_attribute("assessment", sufficiency_assessment)
                    sufficiency_span.set_attribute("needs_tickets", needs_tickets)
                    sufficiency_span.set_attribute("docs_evaluated", len(all_doc_results[:10]))

            # Step 5: Conditional ticket search
            all_ticket_results = []
            if needs_tickets:
                print("\n🎫 Stage 2: Supplementary ticket search...")
                
                with tracer.start_as_current_span("Ticket Search") if tracer else DummySpan() as ticket_search_span:
                    # Execute searches on tickets index only
                    ticket_search_tasks = []
                    for query in search_queries:
                        task = search_elasticsearch_index(query, TICKETS_INDEX)
                        ticket_search_tasks.append(task)
                    
                    print(f"    Executing {len(ticket_search_tasks)} ticket searches...")
                    ticket_search_results = await asyncio.gather(*ticket_search_tasks)
                    
                    # Collect ticket results
                    total_tickets_found = 0
                    
                    for i, results in enumerate(ticket_search_results):
                        query = search_queries[i]
                        print(f"    Ticket Search {i+1}: {query}")
                        print(f"      Tickets found: {results[1]} ({len(results[0])} returned)")
                        
                        total_tickets_found += results[1]
                        
                        for ticket in results[0]:
                            all_ticket_results.append({
                                'type': 'ticket',
                                'id': ticket.id,
                                'title': ticket.title,
                                'text': ticket.text,
                                'score': ticket.score,
                                'highlight': ticket.highlight,
                                'ticket_id': ticket.ticket_id,
                                'keywords': ticket.keywords,
                                'source_query': query
                            })
                    
                    if ticket_search_span and hasattr(ticket_search_span, 'set_attribute'):
                        ticket_search_span.set_attribute("total_tickets_found", total_tickets_found)
                        ticket_search_span.set_attribute("ticket_results_collected", len(all_ticket_results))
                    
                    print(f"    🎫 Total ticket results: {len(all_ticket_results)} from {total_tickets_found} found")
            else:
                print("\n✅ Documentation sufficient - skipping ticket search")

            # Step 6: Combine and evaluate results
            print(f"\n📊 Combining results for final analysis...")
            print(f"    📚 Documentation results: {len(all_doc_results)}")
            print(f"    🎫 Ticket results: {len(all_ticket_results)}")
            
            # Combine all results for evaluation
            all_results_for_evaluation = all_doc_results + all_ticket_results
            
            # Create mock search results for compatibility with existing code
            search_results_list = []
            if all_doc_results:
                # Group docs by query
                docs_by_query = {}
                for doc in all_doc_results:
                    query = doc['source_query']
                    if query not in docs_by_query:
                        docs_by_query[query] = []
                    docs_by_query[query].append(HPCSearchResult(
                        id=doc['id'],
                        title=doc['title'],
                        text=doc['text'],
                        score=doc['score'],
                        highlight=doc['highlight'],
                        url=doc['url'],
                        source_type="docs",
                        ticket_id=None,
                        keywords=None
                    ))
                
                for query, docs in docs_by_query.items():
                    search_results_list.append(HPCSearchResults(
                        query=query,
                        docs_results=docs,
                        tickets_results=[],
                        total_docs_found=len(docs),
                        total_tickets_found=0,
                        error=None
                    ))
            
            if all_ticket_results:
                # Group tickets by query
                tickets_by_query = {}
                for ticket in all_ticket_results:
                    query = ticket['source_query']
                    if query not in tickets_by_query:
                        tickets_by_query[query] = []
                    tickets_by_query[query].append(HPCTicketResult(
                        id=ticket['id'],
                        title=ticket['title'],
                        text=ticket['text'],
                        score=ticket['score'],
                        highlight=ticket['highlight'],
                        ticket_id=ticket['ticket_id'],
                        keywords=ticket['keywords']
                    ))
                
                for query, tickets in tickets_by_query.items():
                    # Find existing search result or create new one
                    existing_result = None
                    for result in search_results_list:
                        if result.query == query:
                            existing_result = result
                            break
                    
                    if existing_result:
                        existing_result.tickets_results = tickets
                        existing_result.total_tickets_found = len(tickets)
                    else:
                        search_results_list.append(HPCSearchResults(
                            query=query,
                            docs_results=[],
                            tickets_results=tickets,
                            total_docs_found=0,
                            total_tickets_found=len(tickets),
                            error=None
                        ))

            # Step 7: Evaluate and score search results for relevance
            print("\n📊 Evaluating search result relevance...")
            
            with tracer.start_as_current_span("Evaluate Search Result Relevance") if tracer else DummySpan() as eval_span:
                print(f"    � Evaluating {len(all_results_for_evaluation)} total search results...")
                
                # Create relevance evaluation prompt
                relevance_prompt = f"""You are an expert HPC system administrator evaluating search results for their relevance to a user question.

USER QUESTION: {user_query}

SEARCH RESULTS TO EVALUATE:
"""
                
                # Add each result with a unique identifier
                for i, result in enumerate(all_results_for_evaluation, 1):
                    result_type = "DOCUMENTATION" if result['type'] == 'doc' else "SUPPORT TICKET"
                    
                    relevance_prompt += f"""
RESULT_{i} ({result_type}):
Title: {result['title']}
Content: {result['text'][:300]}...
Search Query: {result['source_query']}
Elasticsearch Score: {result['score']:.2f}
"""
                
                relevance_prompt += f"""

EVALUATION TASK:
For each result, evaluate how useful it would be for answering the user's question. Consider:

1. **Direct Relevance**: Does it directly address the user's question?
2. **Technical Accuracy**: Does it contain accurate technical information?
3. **Completeness**: Does it provide actionable information or complete answers?
4. **Specificity**: Is it specific to the user's context (NHR@FAU, specific systems)?
5. **Practical Value**: Would this help the user solve their problem?

SCORING SCALE:
- 9-10: Extremely relevant, directly answers the question
- 7-8: Highly relevant, provides important context or partial answers
- 5-6: Moderately relevant, contains useful related information
- 3-4: Somewhat relevant, tangentially related
- 1-2: Low relevance, minimal connection to the question
- 0: Not relevant

RESPONSE FORMAT:
For each result, provide:
RESULT_X: [Score 0-10] - [Brief explanation of relevance]

Example:
RESULT_1: 8 - Directly explains Lustre filesystem behavior which is central to the question
RESULT_2: 3 - Mentions storage but focuses on unrelated backup procedures
"""

                eval_messages = [
                    SystemMessage(content="You are an expert HPC administrator focused on identifying the most relevant information for user questions."),
                    HumanMessage(content=relevance_prompt)
                ]
                
                print("    🤖 Running relevance evaluation...")
                eval_response = await llm.ainvoke(eval_messages)
                
                # Parse relevance scores
                eval_text = eval_response.content
                result_scores = []
                
                for i, result in enumerate(all_results_for_evaluation, 1):
                    # Look for RESULT_X: score pattern
                    pattern = rf'RESULT_{i}:\s*(\d+(?:\.\d+)?)\s*-\s*(.+?)(?=RESULT_\d+:|$)'
                    match = re.search(pattern, eval_text, re.IGNORECASE)
                    
                    if match:
                        score = float(match.group(1))
                        explanation = match.group(2).strip()
                    else:
                        # Fallback: use elasticsearch score normalized to 0-10
                        score = min(10, result['score'] * 2)  # Simple normalization
                        explanation = "Auto-scored based on search relevance"
                    
                    result_scores.append({
                        'result': result,
                        'relevance_score': score,
                        'explanation': explanation,
                        'combined_score': (score * 0.7) + (result['score'] * 0.3)  # Weighted combination
                    })
                
                # Sort by combined score and select top results with emphasis on docs
                result_scores.sort(key=lambda x: x['combined_score'], reverse=True)
                
                # Separate docs and tickets for balanced selection with emphasis on docs
                doc_results = [r for r in result_scores if r['result']['type'] == 'doc']
                ticket_results = [r for r in result_scores if r['result']['type'] == 'ticket']
                
                # Give docs higher priority: boost their scores by 15% for final ranking
                for doc_result in doc_results:
                    doc_result['combined_score'] *= 1.15  # 15% boost for documentation
                
                # Re-sort after boosting doc scores
                result_scores.sort(key=lambda x: x['combined_score'], reverse=True)
                
                # Select top 8 docs and top 4 tickets (emphasizing documentation)
                top_docs = doc_results[:8]  # Increased from 4 to 8
                top_tickets = ticket_results[:4]  # Increased from 2 to 4
                
                # Combine and sort by boosted score for final presentation
                top_results = top_docs + top_tickets
                top_results.sort(key=lambda x: x['combined_score'], reverse=True)
                
                print(f"    🏆 Top results selected (documentation-emphasized):")
                print(f"      📚 Documentation: {len(top_docs)} results (prioritized)")
                print(f"      🎫 Support Tickets: {len(top_tickets)} results")
                print(f"      📊 Total: {len(top_results)} results")
                
                for i, scored_result in enumerate(top_results, 1):
                    result = scored_result['result']
                    score = scored_result['relevance_score']
                    result_type = "DOC" if result['type'] == 'doc' else "TICKET"
                    boost_indicator = " (boosted)" if result['type'] == 'doc' else ""
                    print(f"      {i}. [{result_type}] {result['title'][:50]}...{boost_indicator} (Score: {score:.1f})")
                
                if eval_span and hasattr(eval_span, 'set_attribute'):
                    eval_span.set_attribute("evaluation.total_results", len(all_results_for_evaluation))
                    eval_span.set_attribute("evaluation.top_docs_selected", len(top_docs))
                    eval_span.set_attribute("evaluation.top_tickets_selected", len(top_tickets))
                    eval_span.set_attribute("evaluation.total_top_results", len(top_results))
                    eval_span.set_attribute("evaluation.doc_emphasis", True)
                    eval_span.set_attribute("evaluation.doc_boost_factor", 1.15)
                    if top_results:
                        eval_span.set_attribute("evaluation.avg_top_score", sum(r['relevance_score'] for r in top_results) / len(top_results))
                        eval_span.set_attribute("evaluation.score_range", f"{top_results[-1]['relevance_score']:.1f}-{top_results[0]['relevance_score']:.1f}")

            # Step 8: Generate comprehensive report with top results
            print("\n📝 Generating comprehensive HPC research report...")
            
            with tracer.start_as_current_span("Generate Comprehensive HPC Report") if tracer else DummySpan() as report_span:
                final_system_prompt = """You are an expert HPC system administrator and researcher specializing in NHR@FAU systems.

Based on the following search results from official documentation and historical support tickets, create a comprehensive HPC research report for the original question.

IMPORTANT: The search results have been evaluated and ranked by relevance. Focus primarily on the documentation results as they are the most authoritative sources.

Your report should:
1. Directly answer the user's question using the most relevant information
2. Provide technical details and context from the documentation
3. Include relevant examples from support tickets only when they add practical value
4. Cite sources using the format from the report (e.g., 【FAQ】【Getting-Started】)
5. Be thorough but focused on actionable information
6. Highlight any limitations or gaps in the available information

Structure your report with clear sections and include source references for all technical claims."""

                # Prepare content with top results prominently featured
                final_content = f"Original Question: {user_query}\n\n"
                
                # Add top results section (with content truncation)
                final_content += "=== TOP RESULTS (Evaluated and Ranked) ===\n\n"
                
                for i, scored_result in enumerate(top_results, 1):
                    result = scored_result['result']
                    score = scored_result['relevance_score']
                    explanation = scored_result['explanation']
                    
                    result_type = "DOCUMENTATION" if result['type'] == 'doc' else "SUPPORT TICKET"
                    
                    final_content += f"RANK #{i} - {result_type} (Relevance Score: {score:.1f}/10)\n"
                    final_content += f"Title: {result['title']}\n"
                    final_content += f"Relevance: {explanation}\n"
                    
                    if result['type'] == 'doc':
                        final_content += f"URL: {result['url']}\n"
                    else:
                        final_content += f"Ticket ID: {result['ticket_id']}\n"
                        if result['keywords']:
                            final_content += f"Keywords: {', '.join(result['keywords'][:5])}\n"  # Limit keywords
                    
                    # Truncate content to prevent token overflow
                    content_text = result['text']
                    if len(content_text) > 1500:  # Limit content length
                        content_text = content_text[:1500] + "... [TRUNCATED]"
                    final_content += f"Content: {content_text}\n"
                    
                    if result['highlight']:
                        highlight_text = result['highlight']
                        if len(highlight_text) > 300:  # Limit highlight length
                            highlight_text = highlight_text[:300] + "... [TRUNCATED]"
                        final_content += f"Key Highlights: {highlight_text}\n"
                    
                    final_content += f"Source Query: {result['source_query']}\n\n"

                final_messages = [
                    SystemMessage(content=final_system_prompt),
                    HumanMessage(content=final_content)
                ]
                
                if report_span and hasattr(report_span, 'set_attribute'):
                    report_span.set_attribute("final_system_prompt_length", len(final_system_prompt))
                    report_span.set_attribute("final_content_length", len(final_content))
                    report_span.set_attribute("final_messages_count", len(final_messages))
                
                print("    🤖 Generating comprehensive report...")
                final_response = await llm.ainvoke(final_messages)
                
                if report_span and hasattr(report_span, 'set_attribute'):
                    report_span.set_attribute("final_response_length", len(final_response.content))
                    report_span.set_attribute("final_response_preview", final_response.content[:300] + "...")

            # Step 9: Extract user assumptions for fact-checking (not report claims)
            print("\n🔍 Extracting user assumptions for verification...")
            
            user_assumptions = await extract_user_assumptions(user_query, llm)
            
            # Step 10: Parallel assumption checking and contradiction detection
            print("\n🚀 Running parallel assumption checking and contradiction detection...")
            
            # Execute assumption-checking and contradiction detection in parallel
            assumption_check_task = check_user_assumptions(user_assumptions, search_results_list, llm)
            contradiction_task = detect_contradictions(user_query, search_results_list, llm)
            
            # Wait for both to complete
            assumption_results, contradictions = await asyncio.gather(
                assumption_check_task,
                contradiction_task
            )
            
            # Step 11: Hardened report revision if issues found
            print("\n🔍 Performing fact-checking and contradiction analysis...")
            
            # Determine fact-checking strictness based on source types
            docs_only = len(all_ticket_results) == 0
            fact_check_mode = "LENIENT" if docs_only else "STRICT"
            
            print(f"    📋 Fact-checking mode: {fact_check_mode} ({'docs only' if docs_only else 'docs + tickets'})")
            
            # Check if revision is needed with different thresholds
            false_claims = [r for r in assumption_results if r.verdict == "FALSE"]
            unknown_claims = [r for r in assumption_results if r.verdict == "UNKNOWN"]
            
            if docs_only:
                # More lenient for documentation-only scenarios
                needs_revision = len(false_claims) > 0 or len(contradictions) > 0 or len(unknown_claims) > 6
                unknown_threshold = 6
            else:
                # Stricter when tickets are involved
                needs_revision = len(false_claims) > 0 or len(contradictions) > 0 or len(unknown_claims) > 3
                unknown_threshold = 3
            
            if needs_revision:
                print(f"    ⚠ Issues detected - generating revised report:")
                if false_claims:
                    print(f"      • {len(false_claims)} false claims detected")
                if contradictions:
                    print(f"      • {len(contradictions)} contradictions detected")
                if len(unknown_claims) > unknown_threshold:
                    print(f"      • {len(unknown_claims)} unverifiable claims detected (threshold: {unknown_threshold})")
                
                # Generate revision prompt with mode-specific instructions
                if docs_only:
                    revision_instructions = """
REVISION INSTRUCTIONS (DOCUMENTATION-FOCUSED MODE):
1. CORRECT all FALSE claims using the provided evidence
2. ADDRESS all contradictions between user assumptions and documentation
3. For UNKNOWN claims: Keep them if they are reasonable interpretations of documented information
4. Only remove claims that are clearly contradicted by documentation
5. Prefer stating "Documentation does not explicitly mention..." rather than removing helpful guidance
6. Include practical troubleshooting steps even if not explicitly documented
7. Use ONLY information that can be reasonably inferred from official documentation
8. When making reasonable inferences, clearly mark them as such"""
                else:
                    revision_instructions = """
REVISION INSTRUCTIONS (STRICT MODE - DOCS + TICKETS):
1. CORRECT all FALSE claims using the provided evidence
2. ADDRESS all contradictions between user assumptions and documentation
3. REPLACE uncertain claims with explicit uncertainty statements (e.g., "Documentation unclear on...")
4. REQUIRE explicit source citations for ALL technical claims
5. Use ONLY information that can be verified from the search results
6. When information is missing or unclear, explicitly state this rather than guessing"""
                
                revision_prompt = f"""The initial report contained factual errors. Generate a revised version.

ORIGINAL REPORT:
{final_response.content}

FACT-CHECK RESULTS:
"""
                
                for result in assumption_results:
                    revision_prompt += f"\nCLAIM: {result.claim}\nVERDICT: {result.verdict} (Confidence: {result.confidence:.2f})\nEVIDENCE: {result.evidence}\n"
                
                if contradictions:
                    revision_prompt += f"\nCONTRADICTIONS DETECTED:\n"
                    for i, contradiction in enumerate(contradictions, 1):
                        revision_prompt += f"{i}. {contradiction}\n"
                
                revision_prompt += revision_instructions
                revision_prompt += "\n\nGenerate a revised report with the same structure but with corrected information and appropriate source attribution."

                revision_messages = [
                    SystemMessage(content=f"You are an HPC technical writer in {fact_check_mode} mode, balancing accuracy with helpfulness."),
                    HumanMessage(content=revision_prompt)
                ]
                
                print("    🔄 Generating revised report with corrections...")
                revised_response = await llm.ainvoke(revision_messages)
                final_response = revised_response
                
                print(f"    ✅ Report revised with {fact_check_mode.lower()} fact-checking")
            else:
                print("    ✅ No significant issues detected - using original report")
            
            # Step 12: Generate hardened concise answer
            print("\n🎯 Generating fact-checked concise answer...")
            
            with tracer.start_as_current_span("Generate Concise Answer") if tracer else DummySpan() as concise_span:
                concise_prompt = f"""You are an expert HPC support specialist. Based on the comprehensive research report below, provide a CONCISE, DIRECT answer to the user's original question.

ORIGINAL USER QUESTION:
{user_query}

COMPREHENSIVE RESEARCH REPORT:
{final_response.content}

INSTRUCTIONS FOR CONCISE ANSWER:
1. **Maximum 3-4 sentences** - This is strictly enforced
2. **Answer as HPC support staff** - You are helping the user directly
3. **Answer the user's core question directly** - Don't add extra information they didn't ask for
4. **Include only the most critical information** needed to answer their question
5. **Include essential commands/steps** if the question requires action
6. **Cite ONLY official documentation** using format 【FAQ】【Getting-Started】- NO ticket citations
7. **No headers, tables, or formatting** - plain text only
8. **Focus on what the user actually asked** - not everything you could tell them
9. **Outline fact-checked possibilities** - what options are actually available

EXAMPLES OF GOOD CONCISE ANSWERS (based on FAQ style):

**Q: How can I get access to HPC systems?**
- "Depending on your status, there are different ways to get an HPC account - external researchers need institutional sponsorship and must submit requests through a FAU PI who creates a project in the HPC portal【FAQ】. Access is not available as a commercial subscription, but GPU resources can be requested once your account is approved【Getting-Started】."

**Q: I am unable to access my $WORK directory when using JupyterHub.**
- "First, login via SSH and create a link to $WORK in your $HOME directory with `ln -s $WORK $HOME/work`【FAQ】. This allows you to access $WORK from JupyterHub since the containers don't automatically mount all filesystems."

**Q: Why does my application give an http/https timeout?**
- "By default compute nodes cannot access the internet directly, resulting in connection timeouts【FAQ】. Configure proxy settings with `export http_proxy=http://proxy.nhr.fau.de:80` and `export https_proxy=http://proxy.nhr.fau.de:80` in your job script or interactive session."

**Q: SSH is asking for a password, but I do not have one.**
- "HPC accounts created through the HPC portal do not have passwords - authentication is done through SSH keys only【FAQ】. Generate an SSH key pair, upload your public key to the HPC portal, and configure your SSH connection to use key-based authentication."

**Q: The software I need is not installed. What can I do now?**
- "All software is provided using environment modules - check available applications and development tools in the documentation【FAQ】. You can install software yourself using user-spack functionality or containers via Apptainer if the needed package isn't centrally installed."

**Q: Why is my job not starting after I have submitted it to the queue?**
- "The batch system assigns priority based on waiting time, partition, user group, and recently used compute time (fairshare)【FAQ】. If you've submitted many jobs recently, your priority decreases to allow other users' jobs to run."

**Q: How can I request an interactive job on a cluster?**
- "Interactive jobs can be requested using `salloc` with the appropriate options for testing or debugging【FAQ】. Purge all loaded modules with `module purge` before issuing the `salloc` command to avoid environment issues."""

                concise_messages = [
                    SystemMessage(content="You are an expert at providing concise, direct answers to HPC questions. Keep responses to 3-4 sentences maximum."),
                    HumanMessage(content=concise_prompt)
                ]
                
                print("    📝 Generating concise answer...")
                concise_response = await llm.ainvoke(concise_messages)
                
                # Validate that the response is actually concise
                concise_text = concise_response.content.strip()
                sentence_count = len([s for s in concise_text.split('.') if s.strip()])
                
                if sentence_count > 5:
                    print(f"    ⚠️ Warning: Response has {sentence_count} sentences, should be 3-4")
                
                if concise_span and hasattr(concise_span, 'set_attribute'):
                    concise_span.set_attribute("concise.sentence_count", sentence_count)
                    concise_span.set_attribute("concise.character_count", len(concise_text))
                    concise_span.set_attribute("concise.within_limit", sentence_count <= 4)
                
                return final_response.content, concise_text
            
        except Exception as e:
            if span and hasattr(span, 'set_attribute'):
                span.set_attribute("research.error", str(e))
                span.set_attribute("research.error_type", type(e).__name__)
            raise e

@dataclass
class ReportTemplate:
    """Template for structuring HPC research reports"""
    name: str
    description: str
    sections: List[str]
    focus_areas: List[str]
    special_instructions: str

# Define report templates
REPORT_TEMPLATES = {
    "technical_troubleshooting": ReportTemplate(
        name="Technical Troubleshooting",
        description="For technical problems, errors, and system issues",
        sections=[
            "Problem Analysis",
            "Root Cause Investigation", 
            "Step-by-Step Troubleshooting",
            "Solution Implementation",
            "Prevention Measures"
        ],
        focus_areas=["error diagnosis", "system behavior", "configuration issues", "workarounds"],
        special_instructions="Focus on actionable troubleshooting steps, diagnostic commands, and verified solutions. Include specific error messages and their meanings."
    ),
    
    "access_policy": ReportTemplate(
        name="Access and Policy Information",
        description="For questions about access, accounts, permissions, and policies",
        sections=[
            "Access Requirements",
            "Application Process",
            "Available Resources",
            "Policies and Restrictions",
            "Next Steps"
        ],
        focus_areas=["eligibility criteria", "application procedures", "resource availability", "policy compliance"],
        special_instructions="Provide clear eligibility requirements, step-by-step application processes, and policy details. Be explicit about what is and isn't allowed."
    ),
    
    "software_usage": ReportTemplate(
        name="Software and Tools Guidance",
        description="For questions about using specific software, tools, or workflows",
        sections=[
            "Software Overview",
            "Installation and Setup",
            "Usage Instructions",
            "Best Practices",
            "Common Issues and Solutions"
        ],
        focus_areas=["module loading", "configuration", "job submission", "performance optimization"],
        special_instructions="Include specific commands, module names, and configuration examples. Focus on practical usage patterns and optimization tips."
    ),
    
    "resource_planning": ReportTemplate(
        name="Resource Planning and Allocation",
        description="For questions about resource requirements, quotas, and planning",
        sections=[
            "Resource Assessment",
            "Available Options",
            "Allocation Process",
            "Usage Guidelines",
            "Monitoring and Management"
        ],
        focus_areas=["compute resources", "storage options", "scheduling", "quota management"],
        special_instructions="Provide specific resource specifications, allocation procedures, and usage monitoring guidance."
    ),
    
    "general_information": ReportTemplate(
        name="General Information",
        description="For general inquiries and informational questions",
        sections=[
            "Overview",
            "Key Information",
            "Available Options",
            "Additional Resources",
            "Contact Information"
        ],
        focus_areas=["system overview", "available services", "documentation links", "support contacts"],
        special_instructions="Provide comprehensive overview with links to detailed documentation and appropriate contact information."
    )
}

async def select_report_template(user_query: str, llm) -> ReportTemplate:
    """Select the most appropriate report template based on the user query"""
    
    template_descriptions = "\n".join([
        f"- {key}: {template.description}"
        for key, template in REPORT_TEMPLATES.items()
    ])
    
    selection_prompt = f"""You are an expert at categorizing HPC user questions to select the most appropriate report template.

USER QUERY:
{user_query}

AVAILABLE REPORT TEMPLATES:
{template_descriptions}

INSTRUCTIONS:
1. Analyze the user's question to understand their primary need
2. Consider what type of information would be most helpful
3. Select the template that best matches their query type
4. Focus on the main intent, not just keywords

RESPONSE FORMAT:
TEMPLATE: [template_key]
REASONING: [Brief explanation of why this template fits]

Examples:
- "I can't access my files" → technical_troubleshooting
- "How do I get an account?" → access_policy  
- "How do I use TensorFlow?" → software_usage
- "What GPU resources are available?" → resource_planning
- "What is the HPC cluster?" → general_information

Select the template now:"""

    messages = [
        SystemMessage(content="You are an expert at categorizing HPC questions to select appropriate report templates."),
        HumanMessage(content=selection_prompt)
    ]
    
    try:
        response = await llm.ainvoke(messages)
        response_text = response.content
        
        # Extract template selection
        template_match = re.search(r'TEMPLATE:\s*(\w+)', response_text, re.IGNORECASE)
        reasoning_match = re.search(r'REASONING:\s*(.+)', response_text, re.IGNORECASE | re.DOTALL)
        
        if template_match:
            template_key = template_match.group(1).lower()
            reasoning = reasoning_match.group(1).strip() if reasoning_match else "No reasoning provided"
            
            if template_key in REPORT_TEMPLATES:
                selected_template = REPORT_TEMPLATES[template_key]
                print(f"    📋 Selected template: {selected_template.name}")
                print(f"    💭 Reasoning: {reasoning}")
                return selected_template
        
        # Fallback to general information template
        print("    📋 Defaulting to General Information template")
        return REPORT_TEMPLATES["general_information"]
        
    except Exception as e:
        print(f"    Error selecting template: {str(e)}")
        return REPORT_TEMPLATES["general_information"]

async def main():
    """Main application for HPC deep research"""
    parser = argparse.ArgumentParser(description="HPC Deep Research Workflow")
    parser.add_argument("--trace", action="store_true", help="Enable Phoenix tracing")
    parser.add_argument("--query", type=str, help="HPC question to research")
    
    args = parser.parse_args()
    
    # Setup tracing
    setup_tracing(args.trace)
    
    print("=" * 80)
    print("  HPC Deep Research Workflow")
    print("=" * 80)
    print(f"AI Model: {OPENAI_COMPATIBLE_MODEL}")
    print(f"Endpoint: {OPENAI_COMPATIBLE_BASE_URL}")
    print(f"Elasticsearch: {ELASTIC_URL}")
    print(f"Documentation Index: {DOCS_INDEX}")
    print(f"Tickets Index: {TICKETS_INDEX}")
    if tracing_enabled:
        print("Phoenix Tracing: http://localhost:6006")
    else:
        print("Tracing: Disabled")
    print()
    print("Available commands:")
    print("  - Enter HPC question for comprehensive research")
    print("  - 'exit' to quit")
    print("=" * 80)
    print()
    
    # If query provided as argument, process it and exit
    if args.query:
        print(f"Processing query: {args.query[:100]}...")
        report, answer = await comprehensive_hpc_research(args.query)
        print("\n" + "=" * 80)
        print("HPC RESEARCH REPORT:")
        print("=" * 80)
        print(report)
        print("=" * 80)
        print("\n" + "=" * 80)
        print("CONCISE FINAL ANSWER:")
        print("=" * 80)
        print(answer)
        print("=" * 80)
        return
    
    # Interactive mode
    while True:
        try:
            user_input = input("HPC Question> ").strip()
            
            if user_input.lower() in ["exit", "quit", "bye"]:
                print("Goodbye! ")
                break
            
            if not user_input:
                continue
            
            print(f"\nAnalyzing HPC question: {user_input[:100]}...")
            print("Starting comprehensive HPC research...\n")
            
            report, answer = await comprehensive_hpc_research(user_input)
            
            print("\n" + "=" * 80)
            print("HPC RESEARCH REPORT:")
            print("=" * 80)
            print(report)
            print("=" * 80)
            print("\n" + "=" * 80)
            print("CONCISE FINAL ANSWER:")
            print("=" * 80)
            print(answer)
            print("=" * 80)
            
            if tracing_enabled:
                print(f"\nComplete Phoenix Traces: http://localhost:6006")
                print("   LLM Generations with detailed metrics")
                print("   Parallel Elasticsearch searches")
                print("   Complete HPC research workflow")
                print("   Performance metrics")
            print()
            
        except KeyboardInterrupt:
            print("\n\nGoodbye! ")
            break
        except Exception as e:
            print(f"\nError during HPC research: {str(e)}")
            print("Please try with a different question.\n")

if __name__ == "__main__":
    # Test system connections
    print("Checking system connections...")
    
    # Test Phoenix (if tracing requested)
    if "--trace" in sys.argv:
        try:
            response = requests.get("http://localhost:6006/health", timeout=5)
            if response.status_code == 200:
                print("Phoenix running on http://localhost:6006")
            else:
                print("Phoenix connection issues")
        except:
            print("Phoenix not reachable")
    
    # Test Elasticsearch
    try:
        response = requests.get(f"{ELASTIC_URL}/_cluster/health", timeout=5)
        if response.status_code == 200:
            print("Elasticsearch connected")
        else:
            print("Elasticsearch connection issues")
    except:
        print("Elasticsearch not reachable")
    
    # Test LLM endpoint
    try:
        test_response = requests.post(
            f"{OPENAI_COMPATIBLE_BASE_URL}/chat/completions",
            json={
                "model": OPENAI_COMPATIBLE_MODEL,
                "messages": [{"role": "user", "content": "Test"}],
                "max_tokens": 10
            },
            headers={"Content-Type": "application/json"},
            timeout=10
        )
        if test_response.status_code == 200:
            print("AI model connected")
        else:
            print("AI model connection issues")
    except:
        print("AI model not reachable")
    
    print()
    
    # Run the application
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nSystem terminated. Goodbye!")
    except Exception as e:
        print(f"System error: {e}")
