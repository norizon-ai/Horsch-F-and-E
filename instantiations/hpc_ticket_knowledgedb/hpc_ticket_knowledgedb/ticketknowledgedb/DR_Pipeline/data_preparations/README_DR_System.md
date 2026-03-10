# HPC Deep Research (DR) System

A multi-agent system for comprehensive HPC question answering with fact-checking and assumption validation.

## 🏗️ Architecture

The DR system implements a clean multi-agent architecture:

### Core Agents

1. **Supervisor Agent** (`supervisor_agent.py`)
   - Orchestrates the entire research process
   - Assesses answer quality and decides on iterations
   - Generates final reports and concise answers
   - Performs final fact-checking against documentation

2. **Research Agent** (`research_agent.py`)
   - Performs three types of research in parallel:
     - **Zero-shot**: General HPC knowledge without search
     - **Docs-only**: Official documentation search
     - **Tickets-only**: Similar support cases search

3. **Assumption Checker** (`assumption_checker.py`)
   - Extracts implicit user assumptions from queries
   - Validates assumptions against official documentation
   - Identifies potentially incorrect user beliefs

### Supporting Components

- **Search Service** (`search_service.py`): Elasticsearch interface
- **Configuration** (`dr_config.py`): System configuration management
- **Data Models** (`dr_models.py`): Type definitions and data structures
- **Workflow** (`dr_workflow.py`): Main orchestration logic

## 🚀 Key Features

### Multi-Agent Research
- **Parallel Processing**: All research types run simultaneously
- **Quality Assessment**: Each answer is evaluated for relevance and accuracy
- **Iterative Refinement**: Up to 3 iterations based on quality thresholds

### Fact-Checking & Validation
- **Assumption Checking**: Identifies and validates user assumptions
- **Documentation Priority**: Official docs prioritized over tickets
- **Final Fact-Check**: Concise answers verified against documentation only

### Intelligent Decision Making
- **Quality Scoring**: 5-point scale (EXCELLENT to INSUFFICIENT)
- **Contribution Assessment**: Evaluates how much each answer helps
- **Confidence Scoring**: Automated confidence calculation
- **Iteration Control**: Smart decisions on when to continue research

## 📋 Output Structure

### Comprehensive Report
- Integrates findings from all research types
- Addresses problematic user assumptions
- Provides technical details with source citations
- Structured with clear sections

### Concise Answer
- **Maximum 3-4 sentences** (strictly enforced)
- **Direct answer** to user's core question
- **Essential commands/steps** only
- **Source citations** using 【Documentation】format
- **Fact-checked** against official documentation

## 🔧 Installation & Setup

### Prerequisites
```bash
pip install langchain-openai pydantic requests asyncio
```

### Configuration
Set environment variables or modify `dr_config.py`:
```bash
export LLM_BASE_URL="http://lme49.cs.fau.de:30000/v1"
export LLM_MODEL="openai/gpt-oss-120b"
export ELASTIC_URL="http://localhost:9200"
export DOCS_INDEX="docs"
export TICKETS_INDEX="tickets"
```

### Elasticsearch Setup
Ensure you have the required indices:
- `docs`: Official NHR@FAU documentation
- `tickets`: Historical support tickets

## 💻 Usage

### Command Line Interface
```bash
# Single query
python -m DR_Pipeline.main --query "How do I access $WORK in JupyterHub?"

# Interactive mode
python -m DR_Pipeline.main --interactive

# Brief output (concise answer only)
python -m DR_Pipeline.main --query "Why is my job not starting?" --brief

# Test connections
python -m DR_Pipeline.main --test-connections
```

### Python API
```python
from DR_Pipeline import dr_service

# Initialize the service
await dr_service.initialize()

# Process a query
result = await dr_service.process_query(
    "How do I access my $WORK directory in JupyterHub?"
)

# Access results
print("Concise Answer:")
print(result.concise_answer)

print("\nComprehensive Report:")
print(result.final_report)

print(f"\nConfidence: {result.confidence_score:.2f}")
print(f"Iterations: {result.total_iterations}")
print(f"Processing Time: {result.processing_time:.1f}s")
```

### Advanced Usage
```python
# Access detailed iteration data
for iteration in result.iterations:
    print(f"Iteration {iteration.iteration_number}:")
    
    # Research answers
    for answer in iteration.research_answers:
        print(f"  {answer.research_type.value}: {answer.confidence:.2f}")
    
    # User assumptions
    for assumption in iteration.user_assumptions:
        status = "✓" if assumption.is_valid else "✗"
        print(f"  {status} {assumption.assumption}")
    
    print(f"  Decision: {iteration.supervisor_decision}")
```

## 🔍 Research Process Flow

```
1. User Query Input
   ↓
2. Supervisor Agent Starts
   ↓
3. Parallel Execution:
   ├── Research Agent (Zero-shot, Docs, Tickets)
   └── Assumption Checker (Extract & Validate)
   ↓
4. Quality Assessment
   ├── Score each research answer (1-5)
   ├── Evaluate contribution to user question
   └── Check factual accuracy & completeness
   ↓
5. Supervision Decision
   ├── Continue if quality insufficient
   └── Complete if adequate (max 3 iterations)
   ↓
6. Final Report Generation
   ├── Integrate best findings
   ├── Address invalid assumptions
   └── Provide comprehensive guidance
   ↓
7. Concise Answer Generation
   ├── Distill to 3-4 sentences
   ├── Focus on user's core question
   └── Include essential commands only
   ↓
8. Final Fact-Check
   ├── Verify against documentation only
   ├── Correct any factual errors
   └── Add uncertainty if unclear
```

## 📊 Quality Assurance

### Research Quality Scoring
- **EXCELLENT (5)**: Outstanding, fully addresses question
- **GOOD (4)**: Strong answer with minor gaps
- **ADEQUATE (3)**: Acceptable but missing details
- **POOR (2)**: Partially relevant with issues
- **INSUFFICIENT (1)**: Does not address question

### Assumption Validation
- **TRUE**: Supported by official documentation
- **FALSE**: Contradicted by documentation
- **UNKNOWN**: Insufficient evidence to determine

### Final Answer Constraints
- Maximum 4 sentences (strictly enforced)
- Plain text only (no formatting)
- Direct answer to core question
- Essential information only
- Source citations required

## 🛡️ Accuracy Features

Based on lessons learned from the previous hardened implementation:

1. **Documentation Priority**: Official docs weighted higher than tickets
2. **Assumption Checking**: Identifies wrong user beliefs early
3. **Final Fact-Check**: Concise answers verified against docs only
4. **Uncertainty Handling**: Explicit statements when information unclear
5. **Source Attribution**: All technical claims must be cited
6. **Quality Thresholds**: Minimum quality requirements for completion

## 🔧 Configuration Options

### DR Process Settings
```python
max_iterations = 3              # Maximum research iterations
quality_threshold = 0.7         # Minimum quality to complete
confidence_threshold = 0.6      # Minimum confidence threshold
max_assumptions = 5             # Maximum assumptions to check
```

### Output Settings
```python
max_report_length = 5000        # Maximum report length
max_concise_answer_sentences = 4 # Strict sentence limit
```

### Search Settings
```python
max_search_results = 10         # Results per search
search_timeout = 30             # Search timeout in seconds
```

## 📈 Performance Metrics

The system tracks:
- **Processing Time**: Total time for complete workflow
- **Confidence Score**: Automated confidence assessment
- **Quality Scores**: Individual answer quality ratings
- **Iteration Count**: Number of research iterations performed
- **Assumption Validation**: Count of valid/invalid assumptions

## 🚨 Error Handling

- **Connection Failures**: Graceful degradation with error messages
- **Search Errors**: Fallback to available sources
- **LLM Errors**: Retry logic and error reporting
- **Configuration Issues**: Validation and clear error messages

## 📝 Example Outputs

### Query: "How do I access my $WORK directory in JupyterHub?"

**Concise Answer:**
> JupyterHub containers don't automatically mount all filesystems, so create a symbolic link to access $WORK: `ln -s $WORK $HOME/work`【FAQ】. This allows you to navigate to the work folder in JupyterHub's file browser and access your persistent storage. You can also directly use the path `/work/username` if you know your username.

**Confidence:** 0.87 | **Time:** 23.4s | **Iterations:** 2

## 🔄 Migration from Previous System

Key improvements over the hardened workflow:
- **Cleaner Architecture**: Multi-agent design vs monolithic
- **Better Modularity**: Separate files for each component
- **Simplified Logic**: Removed complex hardening layers
- **Official DR Methodology**: Follows established DR patterns
- **Improved Quality Assessment**: More sophisticated evaluation
- **Enhanced Assumption Checking**: Better user assumption validation

## 🤝 Contributing

1. Follow the multi-agent architecture
2. Maintain type hints and documentation
3. Add appropriate error handling
4. Test with various HPC scenarios
5. Ensure fact-checking accuracy

## 📄 License

Internal HPC research tool for NHR@FAU systems.
