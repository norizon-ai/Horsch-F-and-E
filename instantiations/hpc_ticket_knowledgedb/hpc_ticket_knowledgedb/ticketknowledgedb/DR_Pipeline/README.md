# HPC Deep Research (DR) System

A multi-agent deep research workflow implementation for HPC support, adapted for GPT-OSS models with practical workarounds for real-world deployment.

## 🚀 Quick Start

```bash
# Single query
python run_dr.py --query "How do I access my \$WORK directory in JupyterHub?"

# Interactive mode
python run_dr.py --interactive

# Brief output only
python run_dr.py --query "Why is my SLURM job not starting?" --brief

# Test connections
python run_dr.py --test-connections
```

## 🏗️ Architecture Overview

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   run_dr.py     │───▶│   dr_workflow.py │───▶│ supervisor_agent│
│   (Entry Point) │    │   (Orchestrator) │    │   (Coordinator) │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                                         │
                       ┌─────────────────────────────────┼─────────────────────────────────┐
                       ▼                                 ▼                                 ▼
            ┌─────────────────┐              ┌─────────────────┐              ┌─────────────────┐
            │ research_agent  │              │assumption_checker│              │ search_service  │
            │ (Multi-source)  │              │ (Fact-checking) │              │ (Elasticsearch) │
            └─────────────────┘              └─────────────────┘              └─────────────────┘
```

## 🎯 Core Features

### **Multi-Agent Research Pipeline**
- **Research Agent**: Conducts zero-shot, docs-only, and tickets-only research
- **Assumption Checker**: Validates and reformulates user assumptions
- **Supervisor Agent**: Orchestrates iterations and quality assessment
- **Search Service**: Interfaces with Elasticsearch for knowledge retrieval

### **Adaptive Iteration Strategy**
- **Iteration 1**: Comprehensive research + assumption validation
- **Iteration 2+**: Solution-focused research + fact-checking
- **Early Stopping**: High-quality direct answers bypass multi-iteration flow

### **Quality Assurance**
- Fact-checking against official documentation
- Assumption reformulation (positive statements only)
- Source attribution and confidence scoring
- Contradiction detection and correction

## ⚙️ Configuration

### **LLM Configuration** (`dr_config.py`)
```python
# Default GPT-OSS setup
llm_base_url: str = "http://lme49.cs.fau.de:30000/v1"
llm_api_key: str = "dummy"  
llm_model: str = "openai/gpt-oss-120b"
llm_temperature: float = 0.2
llm_max_tokens: int = 2000
```

### **Search Configuration**
```python
# Elasticsearch setup
elastic_url: str = "http://localhost:9200"
max_search_results: int = 10
search_timeout: int = 30
```

### **Research Parameters**
```python
max_iterations: int = 3
max_concise_answer_sentences: int = 4
confidence_threshold: float = 0.7
```

## 🔧 Dependencies

### **Required Python Packages**
```bash
pip install langchain-openai langchain-core requests asyncio
```

### **External Services**
1. **Elasticsearch** with populated indices:
   - `docs`: HPC documentation 
   - `tickets`: Support ticket database
2. **GPT-OSS Model Server** (or compatible OpenAI API endpoint)

### **Data Requirements**
- FAQ file: `docsmd/https___doc.nhr.fau.de_faq_index.html.md`
- Populated Elasticsearch indices with HPC knowledge

## 🚨 Implementation Deviations from "True" Deep Research

### **1. Channel Tag Problem & Workarounds**

**Issue**: GPT-OSS models sometimes generate internal reasoning with channel tags like `<|channel|>analysis<|message|>content<|end|>` instead of clean answers.

**Our Workarounds**:
```python
# Clean up channel formatting in supervisor_agent.py
if "<|channel|>" in answer:
    if "<|channel|>final<|message|>" in answer:
        answer = answer.split("<|channel|>final<|message|>")[-1]
    answer = answer.replace("<|channel|>", "").replace("<|message|>", "")
```

**Impact**: Final answers may occasionally show internal reasoning instead of clean responses.

### **2. Simplified Multi-Agent Communication**

**True DR**: Complex inter-agent communication with shared memory and negotiation protocols.

**Our Implementation**: Sequential pipeline with structured data passing:
- No real-time agent negotiation
- Predefined research types and workflows
- Supervisor makes unilateral decisions

**Why**: GPT-OSS models struggle with complex multi-agent protocols; sequential approach is more reliable.

### **3. Assumption Reformulation Strategy**

**True DR**: Binary validation (TRUE/FALSE) with detailed reasoning.

**Our Approach**: Positive reformulation to avoid LLM confusion:
```python
# Instead of: "User assumption X is FALSE"
# We generate: "Documentation indicates Y is actually the case"
```

**Why**: Negative statements confuse GPT-OSS models and lead to hallucinations.

### **4. Quality Assessment Simplification**

**True DR**: Complex multi-dimensional quality metrics with uncertainty quantification.

**Our Implementation**: 
- Simple 5-point scale (INSUFFICIENT to EXCELLENT)
- Confidence scoring (0.0-1.0)
- Boolean contribution flags

**Why**: GPT-OSS models have difficulty with complex scoring schemas; simpler metrics are more reliable.

### **5. Search Strategy Limitations**

**True DR**: Sophisticated query expansion, semantic search, and result fusion.

**Our Implementation**:
- Simple keyword-based Elasticsearch queries
- Query simplification to avoid "too many clauses" errors
- Basic result ranking by score

**Why**: Complex search strategies often fail with Elasticsearch limitations and model constraints.

## 🛠️ Known Issues & Workarounds

### **Elasticsearch "Too Many Clauses" Error**
```python
# Simplified query generation in research_agent.py
def _simplify_query_for_tickets(self, user_query: str) -> str:
    # Extract key terms instead of using full query
    key_terms = []
    software_terms = ['gromacs', 'tensorflow', 'pytorch', 'cuda', 'mpi']
    # ... limit to 4 terms max
```

### **Verbose Final Answers**
**Problem**: LLM generates full reports instead of concise answers.

**Solution**: Aggressive prompt engineering with explicit constraints:
```python
system_prompt = """CRITICAL: You must provide ONLY a brief, direct answer. 
DO NOT generate a structured report with sections.
Maximum 4 sentences TOTAL."""
```

### **Import Path Issues**
**Problem**: Module imports fail when running directly vs. as package.

**Solution**: Dual import strategy in all modules:
```python
try:
    from dr_models import ResearchType  # Direct execution
except ImportError:
    from .dr_models import ResearchType  # Package import
```

## 📊 Performance Characteristics

### **Typical Response Times**
- Simple queries (direct FAQ match): 10-30 seconds
- Complex queries (multi-iteration): 60-120 seconds
- Very complex queries: 120-180 seconds

### **Quality Metrics**
- Direct answer hit rate: ~70% for common HPC questions
- Multi-iteration trigger rate: ~30% of queries
- Average confidence score: 0.75-0.85

### **Resource Usage**
- Memory: ~200-500MB during execution
- Network: Heavy Elasticsearch and LLM API usage
- Storage: Minimal (logs and temporary data only)

## 🔍 Debugging & Development

### **Enable Verbose Output**
```bash
python run_dr.py --query "your question" # Full detailed output
python run_dr.py --query "your question" --brief # Concise only
```

### **Test System Components**
```bash
python run_dr.py --test-connections
```

### **Common Debug Points**
1. **LLM Connection**: Check `dr_config.py` URL and model name
2. **Elasticsearch**: Verify indices exist and are populated
3. **FAQ File**: Ensure FAQ markdown file exists at expected path
4. **Channel Tags**: Check final answers for formatting issues

### **Adding New Research Types**
1. Add to `ResearchType` enum in `dr_models.py`
2. Implement method in `research_agent.py`
3. Update supervisor logic in `supervisor_agent.py`

## 🎯 Use Cases

### **Ideal For**:
- HPC support automation
- Technical documentation Q&A
- Multi-source knowledge synthesis
- Assumption validation workflows

### **Not Ideal For**:
- Real-time chat applications (too slow)
- Simple FAQ lookups (overkill)
- Non-technical domains (specialized for HPC)
- High-frequency automated queries (resource intensive)

## 🤝 Contributing

### **Code Style**
- Use type hints for all function parameters
- Async/await for all I/O operations
- Comprehensive error handling with graceful degradation
- Clear separation between agents and services

### **Testing Strategy**
- Test with diverse query types (simple, complex, malformed)
- Verify assumption reformulation quality
- Check final answer conciseness
- Monitor for channel tag leakage

### **Performance Optimization**
- Cache frequent searches
- Optimize Elasticsearch queries
- Reduce LLM token usage
- Implement request batching where possible

---

**Note**: This implementation prioritizes reliability and practical deployment over theoretical "pure" Deep Research principles. The workarounds are necessary for stable operation with GPT-OSS models in production environments.
