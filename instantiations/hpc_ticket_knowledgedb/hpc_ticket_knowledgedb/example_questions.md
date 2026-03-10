# Example HPC Questions

This document contains example questions you can use to test the HPC Ticket Knowledge Database system.

## Basic Questions

### Access & Authentication
- "How do I get an HPC account?"
- "I can't log in to the cluster. What should I check?"
- "How do I set up SSH keys for cluster access?"
- "What is the process for renewing my HPC account?"

### File Systems & Storage
- "How do I access my $WORK directory in JupyterHub?"
- "What is the difference between $HOME and $WORK directories?"
- "How can I increase my storage quota?"
- "Where should I store temporary files during job execution?"

### Job Submission (SLURM)
- "How do I submit a job to SLURM?"
- "What are the basic SLURM commands I need to know?"
- "How do I check the status of my submitted jobs?"
- "Why is my job sitting in the queue for so long?"

## Intermediate Questions

### Job Configuration
- "How do I request multiple nodes for my job?"
- "What's the maximum walltime I can request?"
- "How do I specify GPU requirements in my SLURM script?"
- "How can I get email notifications when my job finishes?"

### Software & Modules
- "How do I load the Python module on the cluster?"
- "What versions of GROMACS are available?"
- "How do I install my own Python packages?"
- "Can I use Conda environments on the HPC cluster?"

### GPUs & Accelerators
- "How do I run a job on a GPU node?"
- "What GPU partitions are available?"
- "How can I check GPU utilization during my job?"
- "Why is my GPU job showing low utilization?"

## Advanced Questions

### Performance & Optimization
- "My MPI job is running slower than expected. What could be wrong?"
- "How can I improve the I/O performance of my simulation?"
- "What's the best practice for reading many small files?"
- "How do I use the fast scratch space effectively?"

### Software Installation
- "Can I compile my own software on the cluster?"
- "How do I install a custom version of TensorFlow?"
- "What compilers are available and which should I use?"
- "How do I use Singularity/Apptainer containers?"

### Data Management
- "How can I transfer large datasets to the cluster?"
- "What's the best way to backup my important data?"
- "How do I share data with my research group?"
- "Can I mount the cluster filesystem on my local machine?"

## Domain-Specific Questions

### Computational Chemistry
- "How do I run VASP calculations on the cluster?"
- "What's the optimal setup for Gaussian jobs?"
- "How can I use multiple GPUs with GROMACS?"
- "What libraries are needed for Quantum ESPRESSO?"

### Machine Learning & AI
- "How do I set up PyTorch with CUDA support?"
- "What's the best way to use JupyterHub for ML experiments?"
- "How can I monitor my neural network training progress?"
- "Can I use TensorBoard on the cluster?"

### CFD & Engineering
- "How do I submit ANSYS Fluent jobs?"
- "What's the license situation for Star-CCM+?"
- "How can I run OpenFOAM in parallel?"
- "What visualization tools are available?"

## Troubleshooting Questions

### Common Errors
- "My job failed with 'Out of Memory' error. What should I do?"
- "I'm getting a 'Permission denied' error. How do I fix it?"
- "Why does my job say 'Invalid account/partition combination'?"
- "My Python script works locally but fails on the cluster. Why?"

### Connection Issues
- "I can't connect via SSH. What might be the problem?"
- "The VPN connection keeps dropping. Any solutions?"
- "How do I access the cluster from outside the university network?"

### Module & Library Issues
- "I'm getting 'libmkl not found' error. How do I fix it?"
- "Module commands are not working. What's wrong?"
- "My Conda environment is not activating properly."

## Test Cases for System Validation

### Should Return Direct Answers
1. **"What is SLURM?"**
   - Expected: Basic definition from documentation
   - Confidence: High (0.8+)
   - Sources: Docs

2. **"How do I load a module?"**
   - Expected: `module load <name>` command
   - Confidence: High
   - Sources: Docs, tickets

### Should Trigger Deep Research
3. **"Why is my GPU job underutilized and how can I fix it?"**
   - Expected: Multi-iteration research
   - Should check: Tickets, docs, examples
   - Should reformulate: Assumptions about GPU usage

4. **"What's the best practice for running large-scale parallel simulations?"**
   - Expected: Comprehensive answer
   - Sources: Tickets, docs, knowledge base
   - Iterations: 2-3

### Should Validate Assumptions
5. **"I heard the cluster doesn't support Python 3.10, is that true?"**
   - Expected: Assumption checking
   - Should verify: Module availability
   - Should reformulate: Correct version information

### Edge Cases
6. **"How do I submit a SLURM job to PBS?"**
   - Expected: Clarification that PBS ≠ SLURM
   - Should correct: Job scheduler confusion

7. **"Can I run Docker containers on the cluster?"**
   - Expected: Apptainer/Singularity alternative
   - Should explain: Docker restrictions

## Testing Different Query Modes

### Brief Mode Test
```bash
curl -X POST http://localhost:8001/query \
  -H "Content-Type: application/json" \
  -d '{"query": "How do I submit a SLURM job?", "brief": true}'
```
Expected: Concise answer without detailed report

### Detailed Mode Test
```bash
curl -X POST http://localhost:8001/query \
  -H "Content-Type: application/json" \
  -d '{"query": "How do I optimize my parallel MPI job?", "brief": false}'
```
Expected: Full research report with iterations

### Streaming Test
```bash
curl -X POST http://localhost:8001/query/stream \
  -H "Content-Type: application/json" \
  -d '{"query": "What GPU resources are available?"}'
```
Expected: SSE stream with incremental updates

## Quality Metrics

Good answers should have:
- **Confidence ≥ 0.7**: High-quality research
- **2-3 Iterations**: Comprehensive coverage
- **Multiple Sources**: Docs + tickets + knowledge base
- **Clear Attribution**: Source citations
- **Actionable Content**: Specific commands/examples

## Tips for Writing Good Questions

### Good Questions
- Specific and clear
- Include context when relevant
- Use proper terminology
- Examples:
  - "How do I allocate 4 GPUs for my TensorFlow training job?"
  - "What's the difference between tinygpu and alex partitions?"

### Avoid
- Extremely vague questions
- Multiple unrelated questions in one
- Non-HPC related queries
- Examples:
  - "How do I use computers?" (too vague)
  - "Tell me about Python and also Linux and GPUs" (too broad)

## Testing Workflow

1. **Start with basic questions** to verify system works
2. **Test domain-specific questions** to check knowledge coverage
3. **Try complex queries** to test deep research capabilities
4. **Test edge cases** to verify error handling
5. **Compare answers** with actual documentation

## Notes

- The DR system learns from tickets, so answers may include workarounds from past issues
- Some answers may reference specific cluster names (alex, woody, tinygpu, etc.)
- Processing time varies: 10-30s for simple queries, 60-180s for complex ones
- Confidence scores help assess answer quality
