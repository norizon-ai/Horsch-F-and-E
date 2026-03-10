#!/usr/bin/env python3
"""
Main HPC Deep Research (DR) Workflow
Orchestrates the complete multi-agent DR process
"""

import asyncio
import time
from typing import Optional

# Try absolute imports first (for direct execution), then relative imports (for package use)
try:
    from dr_models import DRResult
    from dr_config import config
    from supervisor_agent import SupervisorAgent
    from search_service import search_service
except ImportError:
    from .dr_models import DRResult
    from .dr_config import config
    from .supervisor_agent import SupervisorAgent
    from .search_service import search_service


class DRWorkflow:
    """Main workflow orchestrator for the HPC Deep Research system"""
    
    def __init__(self):
        self.supervisor = SupervisorAgent()
    
    async def process_query(self, user_query: str) -> DRResult:
        """Process a user query through the complete DR workflow"""
        start_time = time.time()
        
        print("=" * 80)
        print("HPC Deep Research (DR) Workflow")
        print("=" * 80)
        print(f"Query: {user_query}")
        print(f"Model: {config.llm_model}")
        print(f"Max Iterations: {config.max_iterations}")
        print("=" * 80)
        
        try:
            # Step 1: Supervisor orchestrates the research process
            iterations = await self.supervisor.conduct_dr_workflow(user_query)
            
            # New: Print an intermediate summary before final outputs
            print("\n" + "-" * 80)
            print("INTERMEDIATE SUMMARY (before final outputs)")
            print("-" * 80)
            if not iterations:
                print("(no iterations produced)")
            else:
                for it in iterations:
                    print(f"Iteration {it.iteration_number}: {len(it.research_answers)} answers, {len(it.user_assumptions)} assumptions, {len(it.quality_assessments)} assessments")
                    for ans in it.research_answers:
                        print(f"  • {ans.research_type.value}: conf={ans.confidence:.2f}, sources={len(ans.sources)}")
                    if it.supervisor_decision:
                        print(f"  Decision: {it.supervisor_decision}")
            
            # Step 2: Generate comprehensive report
            print("\n" + "=" * 80)
            print("GENERATING FINAL OUTPUTS")
            print("=" * 80)
            
            final_report = await self.supervisor.generate_final_report(user_query, iterations)
            
            # Step 3: Generate concise answer with fact-checking
            concise_answer = await self.supervisor.generate_concise_answer(user_query, final_report)
            
            # Calculate final confidence score
            confidence_score = self._calculate_final_confidence(iterations)
            
            processing_time = time.time() - start_time
            
            result = DRResult(
                user_query=user_query,
                iterations=iterations,
                final_report=final_report,
                concise_answer=concise_answer,
                total_iterations=len(iterations),
                processing_time=processing_time,
                confidence_score=confidence_score
            )
            
            print(f"\nDR Workflow completed in {processing_time:.1f}s")
            print(f"Final confidence: {confidence_score:.2f}")
            print(f"Total iterations: {len(iterations)}")
            
            return result
            
        except Exception as e:
            processing_time = time.time() - start_time
            print(f"\n[ERROR] DR Workflow failed after {processing_time:.1f}s: {str(e)}")
            
            # Return error result
            return DRResult(
                user_query=user_query,
                iterations=[],
                final_report=f"DR Workflow failed: {str(e)}",
                concise_answer=f"Unable to process query due to error: {str(e)}",
                total_iterations=0,
                processing_time=processing_time,
                confidence_score=0.0
            )
    
    def _calculate_final_confidence(self, iterations) -> float:
        """Calculate final confidence score based on all iterations"""
        if not iterations:
            return 0.0
        
        # Get the last iteration (most refined)
        last_iteration = iterations[-1]
        
        # Average confidence from research answers
        research_confidences = [answer.confidence for answer in last_iteration.research_answers]
        avg_research_confidence = sum(research_confidences) / len(research_confidences) if research_confidences else 0.0
        
        # Average quality scores
        quality_scores = [assessment.score.value / 5.0 for assessment in last_iteration.quality_assessments]
        avg_quality_score = sum(quality_scores) / len(quality_scores) if quality_scores else 0.0
        
        # Check for invalid assumptions (reduces confidence)
        invalid_assumptions = [a for a in last_iteration.user_assumptions if not a.is_valid and a.confidence > 0.7]
        assumption_penalty = len(invalid_assumptions) * 0.1
        
        # Combine factors
        final_confidence = (avg_research_confidence * 0.4 + avg_quality_score * 0.6) - assumption_penalty
        
        return max(0.0, min(1.0, final_confidence))
    
    def print_detailed_results(self, result: DRResult):
        """Print detailed results of the DR process"""
        print("\n" + "=" * 80)
        print("DETAILED DR RESULTS")
        print("=" * 80)
        
        print(f"Query: {result.user_query}")
        print(f"Processing Time: {result.processing_time:.1f}s")
        print(f"Total Iterations: {result.total_iterations}")
        print(f"Final Confidence: {result.confidence_score:.2f}")
        
        # Print iteration details
        for iteration in result.iterations:
            print(f"\n--- Iteration {iteration.iteration_number} ---")
            
            # Research answers
            for answer, assessment in zip(iteration.research_answers, iteration.quality_assessments):
                print(f"  {answer.research_type.value}:")
                print(f"    Quality: {assessment.score.name}")
                print(f"    Confidence: {answer.confidence:.2f}")
                print(f"    Sources: {len(answer.sources)}")
                print(f"    Contributes: {assessment.contributes_to_answer}")

            # User assumptions
            if iteration.user_assumptions:
                print(f"  Assumptions checked: {len(iteration.user_assumptions)}")
                for assumption in iteration.user_assumptions:
                    status = "[OK]" if assumption.is_valid else "[!]"
                    print(f"    {status} {assumption.assumption[:60]}...")

            print(f"  Decision: {iteration.supervisor_decision}")
        
        print("\n" + "=" * 80)
        print("COMPREHENSIVE REPORT")
        print("=" * 80)
        print(result.final_report)

        print("\n" + "=" * 80)
        print("CONCISE FINAL ANSWER")
        print("=" * 80)
        print(result.concise_answer)
        print("=" * 80)


class DRService:
    """Service wrapper for the DR workflow with connection testing"""
    
    def __init__(self):
        self.workflow = DRWorkflow()
    
    async def initialize(self) -> bool:
        """Initialize and test all service connections"""
        print("Initializing DR Service...")

        # Test Elasticsearch connection
        if not search_service.test_connection():
            print("[ERROR] Elasticsearch connection failed")
            return False
        print("Elasticsearch connected")
        
        # Test LLM connection
        try:
            import requests
            test_response = requests.post(
                f"{config.llm_base_url}/chat/completions",
                json={
                    "model": config.llm_model,
                    "messages": [{"role": "user", "content": "Test"}],
                    "max_tokens": 10
                },
                headers={"Content-Type": "application/json"},
                timeout=10
            )
            if test_response.status_code == 200:
                print("LLM connected")
            else:
                print("[ERROR] LLM connection failed")
                return False
        except Exception as e:
            print(f"[ERROR] LLM connection failed: {str(e)}")
            return False

        # Validate configuration
        if not config.validate():
            print("[ERROR] Configuration validation failed")
            return False
        print("Configuration validated")

        print("DR Service ready")
        return True
    
    async def process_query(self, user_query: str, detailed_output: bool = True) -> DRResult:
        """Process a query with optional detailed output"""
        result = await self.workflow.process_query(user_query)
        
        if detailed_output:
            self.workflow.print_detailed_results(result)
        
        return result


# Global DR service instance
dr_service = DRService()
