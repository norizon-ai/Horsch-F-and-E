#!/usr/bin/env python3
"""
Example usage of the HPC Deep Research (DR) System
Demonstrates the multi-agent DR workflow for HPC question answering
"""

import asyncio
import sys
from DR_Pipeline import dr_service


async def example_basic_usage():
    """Basic usage example"""
    print("🚀 HPC Deep Research System - Basic Example")
    print("=" * 60)
    
    # Initialize the DR service
    print("Initializing DR service...")
    if not await dr_service.initialize():
        print("❌ Failed to initialize DR service")
        return
    
    # Example HPC questions
    example_queries = [
        "How do I access my $WORK directory in JupyterHub?",
        "Why is my SLURM job not starting?",
        "How can I get access to GPU resources?",
        "What should I do when I get 'quota exceeded' error?",
    ]
    
    # Process each query
    for i, query in enumerate(example_queries, 1):
        print(f"\n{'='*60}")
        print(f"Example {i}: {query}")
        print('='*60)
        
        try:
            # Process the query (brief mode for examples)
            result = await dr_service.process_query(query, detailed_output=False)
            
            # Display results
            print(f"\n🎯 CONCISE ANSWER:")
            print(f"{result.concise_answer}")
            
            print(f"\n📊 METRICS:")
            print(f"Confidence: {result.confidence_score:.2f}")
            print(f"Processing Time: {result.processing_time:.1f}s")
            print(f"Iterations: {result.total_iterations}")
            
            # Show iteration summary
            if result.iterations:
                last_iteration = result.iterations[-1]
                print(f"Research Types: {len(last_iteration.research_answers)}")
                print(f"Assumptions Checked: {len(last_iteration.user_assumptions)}")
                
                # Show assumption validation results
                if last_iteration.user_assumptions:
                    valid_assumptions = sum(1 for a in last_iteration.user_assumptions if a.is_valid)
                    total_assumptions = len(last_iteration.user_assumptions)
                    print(f"Valid Assumptions: {valid_assumptions}/{total_assumptions}")
        
        except Exception as e:
            print(f"❌ Error processing query: {str(e)}")
        
        # Add delay between queries
        if i < len(example_queries):
            print("\nWaiting 2 seconds before next query...")
            await asyncio.sleep(2)


async def example_detailed_analysis():
    """Detailed analysis example"""
    print("\n" + "="*60)
    print("🔍 DETAILED ANALYSIS EXAMPLE")
    print("="*60)
    
    query = "I can't access my files in JupyterHub, but they work fine via SSH"
    
    print(f"Query: {query}")
    print("\nProcessing with detailed output...")
    
    try:
        # Process with detailed output
        result = await dr_service.process_query(query, detailed_output=True)
        
        # Additional analysis
        print("\n" + "="*60)
        print("📋 DETAILED ITERATION ANALYSIS")
        print("="*60)
        
        for iteration in result.iterations:
            print(f"\n--- Iteration {iteration.iteration_number} ---")
            
            # Analyze research answers
            print("Research Results:")
            for answer, assessment in zip(iteration.research_answers, iteration.quality_assessments):
                print(f"  📊 {answer.research_type.value}:")
                print(f"    Quality: {assessment.score.name}")
                print(f"    Confidence: {answer.confidence:.2f}")
                print(f"    Contributes: {'Yes' if assessment.contributes_to_answer else 'No'}")
                print(f"    Sources: {len(answer.sources)}")
                if answer.sources:
                    print(f"    Top Source: {answer.sources[0].title[:50]}...")
            
            # Analyze assumptions
            if iteration.user_assumptions:
                print("\nAssumption Analysis:")
                for assumption in iteration.user_assumptions:
                    status = "✅ Valid" if assumption.is_valid else "❌ Invalid"
                    print(f"  {status}: {assumption.assumption[:60]}...")
                    print(f"    Confidence: {assumption.confidence:.2f}")
            
            print(f"\nSupervisor Decision: {iteration.supervisor_decision}")
            print(f"Continue Research: {'Yes' if iteration.needs_another_iteration else 'No'}")
    
    except Exception as e:
        print(f"❌ Error in detailed analysis: {str(e)}")


async def example_api_integration():
    """Example of API integration patterns"""
    print("\n" + "="*60)
    print("🔌 API INTEGRATION EXAMPLE")
    print("="*60)
    
    # Example of how you might integrate this into a web service
    queries_and_contexts = [
        {
            "query": "How do I submit a GPU job?",
            "user_context": "New user, first time using SLURM",
            "priority": "high"
        },
        {
            "query": "My Python environment is broken",
            "user_context": "Experienced user, conda environment issues",
            "priority": "medium"
        }
    ]
    
    results = []
    
    for item in queries_and_contexts:
        print(f"\nProcessing: {item['query']}")
        print(f"Context: {item['user_context']}")
        print(f"Priority: {item['priority']}")
        
        try:
            # In a real API, you might modify the query based on context
            enhanced_query = f"{item['query']} (User context: {item['user_context']})"
            
            result = await dr_service.process_query(enhanced_query, detailed_output=False)
            
            # Store result with metadata
            api_result = {
                "original_query": item["query"],
                "user_context": item["user_context"],
                "priority": item["priority"],
                "answer": result.concise_answer,
                "confidence": result.confidence_score,
                "processing_time": result.processing_time,
                "iterations": result.total_iterations,
                "timestamp": "2024-01-01T12:00:00Z"  # Would be actual timestamp
            }
            
            results.append(api_result)
            
            print(f"✅ Processed in {result.processing_time:.1f}s")
            print(f"Answer: {result.concise_answer[:100]}...")
            
        except Exception as e:
            print(f"❌ Error: {str(e)}")
    
    print(f"\n📊 Batch Results: {len(results)} queries processed")
    avg_time = sum(r["processing_time"] for r in results) / len(results) if results else 0
    avg_confidence = sum(r["confidence"] for r in results) / len(results) if results else 0
    print(f"Average Processing Time: {avg_time:.1f}s")
    print(f"Average Confidence: {avg_confidence:.2f}")


async def main():
    """Main example runner"""
    print("🎯 HPC Deep Research (DR) System Examples")
    print("This script demonstrates various usage patterns")
    print()
    
    try:
        # Run examples
        await example_basic_usage()
        await example_detailed_analysis()
        await example_api_integration()
        
        print("\n" + "="*60)
        print("✅ All examples completed successfully!")
        print("="*60)
        print("\nNext steps:")
        print("1. Try the interactive mode: python -m DR_Pipeline.main --interactive")
        print("2. Process your own queries: python -m DR_Pipeline.main --query 'Your question'")
        print("3. Integrate into your applications using the Python API")
        
    except KeyboardInterrupt:
        print("\n⚠️ Examples interrupted by user")
    except Exception as e:
        print(f"\n❌ Example failed: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
