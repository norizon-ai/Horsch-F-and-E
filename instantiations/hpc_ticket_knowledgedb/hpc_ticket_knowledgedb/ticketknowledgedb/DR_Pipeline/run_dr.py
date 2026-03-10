#!/usr/bin/env python3
"""
Direct runner for the HPC Deep Research (DR) System
Can be executed directly from the DR_Pipeline directory
"""

import sys
import os
import asyncio
import argparse

# Add the current directory to Python path so we can import our modules
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Now import our modules
from dr_workflow import dr_service


async def main():
    """Main application entry point"""
    parser = argparse.ArgumentParser(
        description="HPC Deep Research (DR) System",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python run_dr.py --query "How do I access my $WORK directory in JupyterHub?"
  python run_dr.py --interactive
  python run_dr.py --query "Why is my SLURM job not starting?" --brief
        """
    )
    
    parser.add_argument(
        "--query", 
        type=str, 
        help="HPC question to research"
    )
    
    parser.add_argument(
        "--interactive", 
        action="store_true", 
        help="Start interactive mode"
    )
    
    parser.add_argument(
        "--brief", 
        action="store_true", 
        help="Show only concise answer (no detailed output)"
    )
    
    parser.add_argument(
        "--test-connections", 
        action="store_true", 
        help="Test system connections and exit"
    )
    
    args = parser.parse_args()
    
    # Initialize DR service
    print("Starting HPC Deep Research (DR) System")
    print("=" * 60)

    if not await dr_service.initialize():
        print("[ERROR] Failed to initialize DR service")
        sys.exit(1)

    if args.test_connections:
        print("All connections successful")
        return
    
    # Process single query
    if args.query:
        await process_single_query(args.query, not args.brief)
        return
    
    # Interactive mode
    if args.interactive or (not args.query and not args.test_connections):
        await interactive_mode(not args.brief)
        return
    
    # No action specified
    parser.print_help()


async def process_single_query(query: str, detailed_output: bool = True):
    """Process a single query"""
    print(f"\nProcessing query: {query[:100]}...")

    try:
        result = await dr_service.process_query(query, detailed_output)

        if not detailed_output:
            # Brief mode - only show concise answer
            print("\n" + "=" * 60)
            print("ANSWER")
            print("=" * 60)
            print(result.concise_answer)
            print("=" * 60)
            print(f"Confidence: {result.confidence_score:.2f} | Time: {result.processing_time:.1f}s | Iterations: {result.total_iterations}")

    except KeyboardInterrupt:
        print("\n[!] Query processing interrupted")
    except Exception as e:
        print(f"\n[ERROR] Error processing query: {str(e)}")


async def interactive_mode(detailed_output: bool = True):
    """Run in interactive mode"""
    print("\n" + "=" * 60)
    print("HPC Deep Research - Interactive Mode")
    print("=" * 60)
    print("Enter HPC questions for comprehensive research")
    print("Commands:")
    print("  'exit' or 'quit' - Exit the system")
    print("  'help' - Show this help")
    print("  'brief' - Toggle brief/detailed output")
    print("  'config' - Show current configuration")
    print("=" * 60)
    
    brief_mode = not detailed_output
    
    while True:
        try:
            user_input = input("\nHPC DR> ").strip()
            
            if not user_input:
                continue
            
            # Handle commands
            if user_input.lower() in ["exit", "quit", "bye"]:
                print("👋 Goodbye!")
                break
            
            elif user_input.lower() == "help":
                print("\n📖 Available commands:")
                print("  exit, quit - Exit the system")
                print("  help - Show this help")
                print("  brief - Toggle brief/detailed output")
                print("  config - Show current configuration")
                print("  Or enter any HPC question for research")
                continue
            
            elif user_input.lower() == "brief":
                brief_mode = not brief_mode
                mode = "brief" if brief_mode else "detailed"
                print(f"Output mode: {mode}")
                continue

            elif user_input.lower() == "config":
                print("\nCurrent configuration:")
                from dr_config import config
                print(f"  LLM Model: {config.llm_model}")
                print(f"  Max Iterations: {config.max_iterations}")
                print(f"  Elasticsearch: {config.elastic_url}")
                continue
            
            # Process as HPC query
            await process_single_query(user_input, not brief_mode)
            
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except EOFError:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"\n[ERROR] Error: {str(e)}")
            print("Please try again or type 'exit' to quit")


def cli_main():
    """CLI entry point"""
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nSystem terminated. Goodbye!")
    except Exception as e:
        print(f"\n[ERROR] System error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    cli_main()
