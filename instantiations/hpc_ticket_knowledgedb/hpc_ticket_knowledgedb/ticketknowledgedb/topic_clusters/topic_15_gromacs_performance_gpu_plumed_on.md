# Topic 15: gromacs_performance_gpu_plumed_on

Number of tickets: 94

## Tickets in this topic:

### 2022120942001341_Gromacs%20on%20Meggie%20%5Bmpt4014h%5D.md
# Ticket 2022120942001341

 # HPC-Support Ticket: Gromacs on Meggie Cluster

## Keywords
- Gromacs
- Meggie cluster
- GPU performance
- Benchmarking
- FAUbox
- Slurm submit script
- Illegal instruction error
- CUDA code
- GPU allocation

## Summary
The user was running Gromacs simulations on the Meggie cluster, which might not be optimal. The HPC Admin offered to benchmark the user's system to find the optimal hardware setup. The user provided Gromacs input files (.tpr) for benchmarking. The HPC Admin shared benchmarking results and suggested using the TinyGPU cluster for better performance. The user encountered an "Illegal instruction" error when trying to run Gromacs on TinyGPU, which was resolved by allocating a GPU using `salloc`.

## Root Cause of the Problem
- The user was running Gromacs simulations on a suboptimal cluster (Meggie).
- The user encountered an "Illegal instruction" error when trying to run Gromacs on TinyGPU due to attempting to run CUDA code on the cluster frontend without a GPU.

## Solution
- The HPC Admin benchmarked the user's system and suggested using the TinyGPU cluster for better performance.
- The HPC Admin provided a Slurm submit script for running jobs on TinyGPU.
- To resolve the "Illegal instruction" error, the HPC Admin advised the user to allocate a GPU using the command `salloc -t tinygpu --gres=gpu:rtx2080ti:1 --time=03:00:00` before loading the Gromacs module and running Gromacs commands.

## General Learnings
- Benchmarking can help determine the optimal hardware setup for specific simulations.
- GPUs often provide better performance for Gromacs simulations compared to CPUs.
- When encountering an "Illegal instruction" error with Gromacs on a cluster, it may be due to attempting to run CUDA code without a GPU. Allocating a GPU can resolve this issue.
- FAUbox can be used to share large files with HPC Admins for benchmarking purposes.
- Slurm submit scripts are used to submit jobs on clusters like TinyGPU.
---

### 2024051942000627_GROMACS%202024.2.md
# Ticket 2024051942000627

 ```markdown
# HPC-Support Ticket: GROMACS 2024.2 Installation

## Keywords
- GROMACS 2024.2
- Installation
- HPC Clusters
- Modules

## Summary
A user requested the installation of GROMACS 2024.2 on the HPC clusters. The HPC Admins confirmed the installation on several clusters.

## Problem
- **Root Cause**: User needed GROMACS 2024.2 for their computational tasks.

## Solution
- **Action Taken**: HPC Admins installed GROMACS 2024.2 on Woody, TinyGPU, Fritz, and Alex clusters.
- **Modules Available**: `gromacs/2024.2-*`

## What Can Be Learned
- **Installation Process**: HPC Admins can install specific software versions upon user request.
- **Cluster Availability**: Different clusters (Woody, TinyGPU, Fritz, Alex) can have the same software installed.
- **User Communication**: Users should provide specific details about the software they need, including version and source links if available.

## Follow-Up
- Ensure users are aware of the new modules available.
- Update documentation to reflect the availability of GROMACS 2024.2 on the specified clusters.
```
---

### 2021100542001166_Gromacs%20Multi%20GPU.md
# Ticket 2021100542001166

 # HPC Support Ticket: Gromacs Multi-GPU Performance

## Keywords
- Gromacs
- Multi-GPU
- Performance
- A100 GPUs
- Benchmarking
- Resource Optimization

## Problem
- User experienced poor performance when running MD simulations in Gromacs using multiple GPUs.
- Suspected incorrect command usage.

## Root Cause
- Multi-GPU performance in Gromacs is generally not optimal.
- User may not have used the correct parameters for multi-GPU setup.

## Solution
- **Recommendation**: Use single-GPU for optimal resource usage.
- **Benchmarks**:
  - **1x A100**: `gmx mdrun -s salm_bin_md_1.tpr -v -nb gpu -pme gpu -bonded gpu -update gpu -nsteps 200000 -ntomp 32 -ntmpi 1 -pin on -pinstride 1` -> 170 ns/day
  - **2x A100**: `gmx mdrun -s salm_bin_md_1.tpr -v -nb gpu -pme gpu -bonded gpu -nsteps 200000 -ntomp 32 -ntmpi 4 -gpu_id 01 -npme 1 -pin on -pinstride 1` -> 192 ns/day
  - **4x A100**: `gmx mdrun -s salm_bin_md_1.tpr -v -nb gpu -pme gpu -bonded gpu -nsteps 200000 -ntomp 32 -ntmpi 4 -npme 1 -pin on -pinstride 1` -> 236 ns/day
- **Environment Variables for Multi-GPU**:
  ```bash
  export GMX_GPU_DD_COMMS=true
  export GMX_GPU_PME_PP_COMMS=true
  export GMX_GPU_FORCE_UPDATE_DEFAULT_GPU=true
  ```
- **Optimization Flags**: `-ntomp 32 -ntmpi 1 -pin on -pinstride 1`

## General Learnings
- Multi-GPU setups in Gromacs may not always yield better performance.
- Single-GPU runs are generally recommended for optimal resource usage.
- Proper parameter tuning and environment variable settings are crucial for performance.
- Metadynamic simulations with multiple walkers may benefit from multi-GPU setups.

## References
- [Multi-GPU Gromacs Jobs on TinyGPU](https://hpc.fau.de/2021/06/18/multi-gpu-gromacs-jobs-on-tinygpu/)
---

### 2022110942002351_Simulation%20of%20small%20systems%20on%20Alex%20%5Bb118bb14%5D.md
# Ticket 2022110942002351

 ```markdown
# HPC Support Ticket Conversation Summary

## Keywords
- GROMACS
- MPS server
- GPU utilization
- Simulation setup
- Performance optimization
- Job chaining
- Hanging jobs

## What Can Be Learned
1. **MPS Server Usage**: The MPS server can be used to run multiple simulations on a single GPU, which can improve performance for smaller systems.
2. **Performance Optimization**: Tuning parameters like `-ntomp` and `-ntmpi` can significantly improve simulation performance.
3. **Job Chaining**: Using `sbatch --dependency` is a convenient way to chain jobs for extending simulations.
4. **Hanging Jobs**: GROMACS jobs can hang after a certain period, which may be related to specific input files or system issues.
5. **Debugging Hanging Jobs**: Checking for corrupted restart files and ensuring proper input parameters can help diagnose hanging jobs.

## Root Cause of the Problem
- The user's GROMACS jobs were hanging after 16 hours, possibly due to specific input parameters or system issues.

## Solution
- The user was advised to check for corrupted restart files and ensure proper input parameters.
- The user was also advised to try running simulations on different GPU types (A100 vs. A40) to see if the issue persists.

## Additional Notes
- The user was provided with scripts and benchmarks for optimizing GROMACS performance using the MPS server.
- The user was advised to use job chaining for extending simulations.
- The user was informed about potential issues with NUMA regions when requesting less than a full node.
```
---

### 2024030542001709_Problems%20with%20running%20gromacs%20on%20meggie.md
# Ticket 2024030542001709

 ```markdown
# HPC Support Ticket: Problems with Running GROMACS on Meggie

## Keywords
- GROMACS
- Job Submission
- squeue
- srun
- MPI Process
- Time Limit

## Problem Description
A student was unable to run GROMACS simulations on the Meggie cluster. The jobs appeared to be running according to the `squeue` command but produced no output and stopped after 24 hours due to hitting the time limit.

## Root Cause
The job scripts contained two commands:
1. `gmx_mpi grompp -f equil_npt.mdp -c confout.gro -p topology.top -o equilibrium_2.tpr`
2. `srun gmx_mpi mdrun -s equllibrium_2.tpr -maxh 24 -deffnm npt_2`

The first command was missing the `srun` prefix, causing it to run with only one MPI process on one core. This prevented the second command from starting.

## Solution
Ensure that all commands in the job script that require parallel execution are prefixed with `srun` to utilize multiple MPI processes.

## Lessons Learned
- Always check job scripts for proper use of `srun` to ensure commands are executed in parallel.
- Monitor job output and logs to verify that all commands are executed as expected.
- Properly structured job scripts are crucial for efficient use of HPC resources.
```
---

### 2021070542004188_I_O%20error.md
# Ticket 2021070542004188

 ```markdown
# HPC Support Ticket: I/O Error

## Keywords
- I/O error
- Gromacs simulation
- Denial of Service (DoS) attack
- HPCVAULT
- Disk space
- Quota
- File locking
- VMD installation

## Problem Description
- User encountered I/O errors during Gromacs simulations on HPCVAULT.
- Errors included:
  - `Cannot fsync 'md2.log'; maybe you are out of disk space?`
  - `Failed to lock: md2.log. Already running simulation?`
  - `Failed to lock: md2.log. Remote I/O error.`
- User attempted to restart the jobs but faced issues with file locking.

## Root Cause
- A Denial of Service (DoS) attack on HPCVAULT between 13:30 and 15:30 caused the I/O errors.

## Solution
- The DoS attack was the primary cause of the I/O errors.
- Manually deleting or moving log files helped in some cases to restart the simulations.
- Further investigation into Gromacs-specific issues might be needed for jobs that did not restart successfully.

## Additional Information
- User inquired about the availability of VMD on the HPC systems.

## Notes
- HPC Admins suggested that the issue with Gromacs not restarting properly might be due to its handling of file operations.
- Each job on HPCVAULT has its own Cgroup (CPUset + GPUs), making `-pinoffset` unnecessary.

## Follow-up
- Further tips on restarting Gromacs jobs might be provided later by the support team.
- The availability of VMD on the HPC systems was not addressed in the provided conversation.
```
---

### 2022012742001229_Gromacs%20Jobs%20TinyGPU%20%5Bmpt4005h%5D.md
# Ticket 2022012742001229

 # HPC Support Ticket: Gromacs Jobs TinyGPU

## Keywords
- Gromacs
- GPU
- Performance
- OpenMP
- SMT
- Slurm
- CPU pinning

## Problem
- Low GPU utilization in Gromacs jobs on TinyGPU.
- Suboptimal job performance due to missing or incorrect flags in job scripts.

## Root Cause
- Gromacs was not called with optimal flags for GPU utilization.
- OpenMP threads were not set to take advantage of SMT on RTX* nodes.

## Solution
1. **Explicitly set Gromacs flags**:
   - Use `-nb pme -pme gpu -bonded gpu -update gpu` to ensure GPU utilization.
   - Ensure GPU communication environment variables are not set to 1 unless using multi-GPU.

2. **Double OpenMP threads**:
   - Use `-ntomp 8` to take advantage of SMT on RTX* nodes.

3. **CPU pinning**:
   - Use `-pin on` and `-pinstride 1` to distribute threads evenly across CPU cores.
   - `-pinoffset` is not necessary as Slurm sets the cpuset.

## Additional Notes
- Gromacs automatically sets some flags to "auto," but explicit setting can improve performance.
- Slurm includes SMT threads in the cpuset, so no additional sbatch options are needed.
- Gromacs detects all CPU cores, but Slurm restricts access to the allocated cores.

## References
- [Gromacs mdrun documentation](https://manual.gromacs.org/documentation/current/onlinehelp/gmx-mdrun.html)
- [Gromacs performance guide](https://manual.gromacs.org/documentation/current/user-guide/mdrun-performance.html)

## Conclusion
- The user agreed to implement the suggested changes and will report back if any issues arise.
- The ticket was closed with the expectation that the user will contact support if further assistance is needed.
---

### 2020032042002482_plumed%20for%20tinyGPU.md
# Ticket 2020032042002482

 ```markdown
# HPC-Support Ticket: PLUMED for tinyGPU

## Keywords
- PLUMED
- GROMACS
- Metadynamics Simulation
- GPU
- tinyGPU
- Performance Optimization

## Summary
A user requested the installation of a PLUMED-patched GROMACS version on tinyGPU to run metadynamics simulations. The HPC Admin provided an experimental module and instructions for its use. The user reported that the performance was not satisfactory compared to CPU-only simulations on another system.

## Problem
- User needed a PLUMED-patched GROMACS version for metadynamics simulations on tinyGPU.
- Performance of PLUMED-patched GROMACS on GPUs was not optimal.

## Solution
- HPC Admin installed an experimental module: `gromacs/2019.4-mkl-CUDA102-plumed2.5.3`.
- Instructions provided for using the module:
  - Use `mpirun` instead of the usual `gmx mdrun -nt ...`.
  - Do not manually load an MPI module.
  - Use the binary `gmx_mpi` for running simulations.
- User feedback indicated that CPU-only simulations were more efficient for their specific use case.

## Lessons Learned
- PLUMED-patched GROMACS on GPUs may not always provide performance benefits.
- It is important to test and compare performance with CPU-only simulations.
- Experimental modules should be used with caution and feedback is crucial for further optimization.

## References
- [PLUMED Performance Optimization](https://www.plumed.org/doc-v2.5/user-doc/html/performance-optimization.html)
```
---

### 42329768_Instalation%20Gromacs%205%20in%20Lima%3F.md
# Ticket 42329768

 ```markdown
# HPC Support Ticket: Installation of Gromacs 5 in Lima

## Keywords
- Gromacs 5
- Lima
- Emmy
- Computational Power
- Testing Section
- Module File Error

## Summary
A user inquired about the availability of Gromacs 5 on the Lima cluster, as it was already installed on Emmy but the user did not require the same computational power.

## Root Cause
- User needed Gromacs 5 on Lima for simulations.
- Gromacs 5 was already installed on Lima but was in the testing section.
- There was a minor error in the module file.

## Solution
- The HPC Admin confirmed that Gromacs 5 ("gromacs/5.0.4-mkl-sse4.1") was available on Lima.
- The error in the module file was corrected.

## General Learnings
- Always check the testing section for newly installed software.
- Module file errors can be corrected by the HPC Admin team.
- Users should communicate their specific needs to ensure the appropriate resources are allocated.
```
---

### 2023022042001032_GROMACS%202023%20Installation.md
# Ticket 2023022042001032

 ```markdown
# HPC-Support Ticket: GROMACS 2023 Installation

## Keywords
- GROMACS 2023.1
- Performance Improvement
- GPU Optimization
- Module Installation
- Temperature and Pressure Coupling Interval

## Summary
A user requested the installation of GROMACS 2023.1 on the HPC system "Alex" due to performance improvements in GPU usage. The HPC Admin responded by informing the user about the availability of a new, but largely untested, GROMACS module.

## Root Cause
- User requested a specific version of GROMACS (2023.1) for improved performance on GPUs.

## Solution
- HPC Admin installed a new GROMACS module (2023.0-gcc11.2.0-mkl-cuda) on Alex, which is still under testing.

## What Can Be Learned
- Users may request specific software versions for performance reasons.
- HPC Admins can respond by installing the requested software or providing an alternative.
- Communication about the testing status of new modules is important.
```
---

### 2022102442000736_Best%20setup%20for%20TREMD%20simulations%20-%20b119ee.md
# Ticket 2022102442000736

 ```markdown
# HPC Support Ticket: Best Setup for TREMD Simulations

## Subject
Best setup for TREMD simulations - b119ee

## Keywords
- TREMD simulations
- Gromacs
- Alex cluster
- Fritz cluster
- Replica exchange
- GPU
- Performance benchmarking
- Checkpoint errors

## Problem
- User needs help with the best setup (number of nodes, ranks, threads) for running 26 parallel TREMD simulations with Gromacs on Alex or Fritz cluster.
- Simulations need to communicate to exchange replicas every 500 steps.

## Observations
- The number of replicas should ideally be a multiple of 8 for optimal performance.
- Performance benchmarks:
  - 3 Fritz nodes: 7 ns/day
  - 8 GPUs on Alex: 199 ns/day
- Typo in the list of replicas: number10 is not listed, number19 is listed twice, causing Gromacs writing errors.
- Checkpoint writing issues when running 26 replicas on 8 GPUs on Alex.

## Solutions
- For consistency, use 26 replicas on Fritz.
- Successfully ran 26 replicas on 8 GPUs on Alex with a performance of 120.6 ns/day.
- Added code for invoking an MPS server to run multiple simulation instances on one GPU.
- Corrected the typo in the list of replicas.

## Documentation
- Use of an MPS server while running multiple walker metadynamic simulations can be found in the documentation: [Gromacs Documentation](https://hpc.fau.de/systems-services/documentation-instructions/special-applications-and-tips-tricks/gromacs/#collapse_5)

## Closure
- The ticket was closed as the user successfully ran 26 replicas on 8 GPUs.
```
---

### 2023072542001818_Gromacs%202022.5%20plumed%20patched.md
# Ticket 2023072542001818

 # HPC Support Ticket: Gromacs 2022.5 with Plumed 2.8 Installation

## Keywords
- Gromacs 2022.5
- Plumed 2.8
- Installation
- HPC Clusters (Fritz, Alex)
- Spack
- GCC
- OpenMPI
- MKL
- CUDA

## Summary
A user requested the installation of Gromacs 2022.5 with Plumed 2.8 on the HPC clusters Fritz and Alex.

## User Request
- Installation of Gromacs 2022.5 with Plumed 2.8 on Fritz and Alex.
- Links to documentation:
  - [Plumed 2.8 Changes](https://www.plumed.org/doc-v2.8/user-doc/html/_c_h_a_n_g_e_s-2-8.html)
  - [Gromacs 2022.5 with Plumed](https://www.plumed.org/doc-v2.8/user-doc/html/gromacs-2022-5.html)

## HPC Admin Response
- Gromacs 2022.5 with Plumed 2.8.3 installed on both clusters.
- Installation details:
  - **Alex:**
    ```
    /apps/SPACK/0.19.1/bin/spack install gromacs@2022.5%gcc@11.2.0 +cuda +mpi +plumed target=zen2 ^plumed@2.8.3%gcc@11.2.0 target=zen2 ^openmpi@4.1.4%gcc@11.2.0 target=zen2 ^cuda%gcc@8.5.0 ^cmake%gcc@8.5.0 ^hwloc%gcc@8.5.0 ^intel-oneapi-mkl%gcc@8.5.0 ^py-cython%gcc@8.5.0 ^numactl%gcc@8.5.0
    ```
  - **Fritz:**
    ```
    /apps/SPACK/0.17.1/bin/spack install gromacs@2022.5%gcc@11.2.0 +mpi +plumed ^plumed@2.8.3%gcc@11.2.0 ^cmake%gcc@8.5.0 ^hwloc%gcc@8.5.0 ^intel-oneapi-mkl%gcc@8.5.0 ^py-cython%gcc@8.5.0 ^numactl%gcc@8.5.0 ^libevent%gcc@8.5.0 ^/rao6zup ^/ndctakg ^/uswo72d
    ```
- User advised to thoroughly test the installation.

## Solution
- Gromacs 2022.5 with Plumed 2.8.3 installed using Spack on both Fritz and Alex clusters.
- Specific configurations and dependencies included in the installation commands.

## General Learning
- Proper installation of software versions and dependencies using Spack.
- Importance of thorough testing after installation.
- Collaboration between users and HPC admins for software requests and installations.
---

### 2024080542002833_gmx_MMPBSA.py.md
# Ticket 2024080542002833

 # HPC Support Ticket: gmx_MMPBSA.py

## Keywords
- gmx_MMPBSA.py
- GROMACS
- AmberTools
- MPI4Py
- Private Installation
- Module Installation

## Problem
- User inquires about the availability of `gmx_MMPBSA.py` on the HPC clusters (fritz or alex).
- The tool requires compilation with GROMACS, AmberTools 20 or 21, and MPI4Py.
- User asks if a private installation is necessary or if it can be provided as a module.

## Solution
- HPC Admin suggests a private installation as the tool is not currently available and there have been no prior requests.
- If more requests come in, a module installation will be considered.

## General Learnings
- Users may need to perform private installations for specialized tools not yet available on the HPC clusters.
- Frequent requests for a specific tool may lead to its inclusion as a module.
- Communication with HPC Admins is essential for understanding the availability and installation process of new tools.
---

### 2022030242001816_tpr-file%20for%20perform.-test.md
# Ticket 2022030242001816

 # HPC Support Ticket: Performance Test with GROMACS

## Keywords
- GROMACS
- Performance Test
- TPR File
- GPU (A40, A100)
- Cluster (Alex, Fritz)
- Slurm
- Benchmark

## Summary
A user provided a TPR file for a performance test using GROMACS. The HPC admin conducted benchmark tests on different hardware configurations and clusters.

## User Issue
- User provided a TPR file with 266387 atoms for performance testing.

## HPC Admin Actions
- Conducted performance tests using GROMACS version 2021.5 on Alex and Fritz clusters.
- Tested GPU configurations on A40 and A100 with varying `ntomp` values.
- Tested multi-node configurations on Fritz cluster using Slurm.

## Results
- **GPU Performance:**
  - A40:
    - `ntomp16`: 72.920 ns/day
    - `ntomp32`: 69.700 ns/day
  - A100:
    - `ntomp16`: 82.059 ns/day
    - `ntomp32`: 77.574 ns/day
- **Fritz Cluster Performance:**
  - 2 nodes: 56.688 ns/day
  - 4 nodes: 99.470 ns/day
  - 6 nodes: 147.055 ns/day

## Solution
- The HPC admin provided detailed performance results and recommended hardware configurations based on the tests.
- The user was advised to choose the hardware they are most experienced with and to contact the HPC support team for further questions.

## General Learnings
- Performance testing with GROMACS involves running benchmarks on different hardware configurations.
- GPU performance can vary significantly based on the hardware and `ntomp` settings.
- Multi-node performance can be optimized by adjusting the number of nodes and tasks per node.
- Slurm scripts can be customized to allocate resources effectively for performance tests.

## Recommendations
- Users should provide detailed information about their system and requirements for performance testing.
- HPC admins should conduct thorough benchmark tests and provide clear recommendations based on the results.
- Users should be encouraged to contact the HPC support team for any questions or further assistance.
---

### 2024120842000036_GROMACS%202024.4.md
# Ticket 2024120842000036

 ```markdown
# HPC-Support Ticket Conversation: GROMACS 2024.4 Installation

## Keywords
- GROMACS 2024.4
- Installation
- Alex
- gcc11.2.0
- mkl
- cuda

## Problem
- User requested the installation of GROMACS 2024.4 on the HPC system named Alex.

## Solution
- HPC Admin confirmed the installation of GROMACS 2024.4 with the specific configuration `gromacs/2024.4-gcc11.2.0-mkl-cuda`.

## General Learnings
- Users can request specific software versions and configurations.
- HPC Admins can install and confirm the availability of requested software.
- Effective communication between users and HPC Admins ensures timely resolution of software requests.
```
---

### 2020022842000597_Meggie%20account.md
# Ticket 2020022842000597

 # HPC Support Ticket Summary

## Subject: Meggie Account

### Keywords:
- Gromacs
- Plumed
- Slurm
- Meggie
- Emmy
- TinyGPU
- Metadynamics Simulations
- MPI
- GPU
- Priority Boost
- Snapshots
- HILLS Files

### General Learnings:
- **Account Specification**: Users need to specify an account in their batch scripts for Slurm.
- **Module Dependencies**: Gromacs modules handle their own dependencies, no need to load Intel MPI separately.
- **Parallel Runs**: Use `mdrun_mpi` instead of `gmx mdrun` for parallel runs.
- **Resource Allocation**: Ensure the number of processes matches the requested resources.
- **Priority Boost**: HPC admins can provide priority boosts for urgent simulations.
- **Data Backup**: Snapshots can be used to recover lost data.
- **Regular Job Monitoring**: Important to regularly check job outputs to avoid data loss.

### Root Causes and Solutions:
- **MPI Initialization Error**:
  - **Root Cause**: Incorrect MPI binary used.
  - **Solution**: Use `mdrun_mpi` instead of `gmx mdrun`.

- **Empty HILLS Files**:
  - **Root Cause**: Issue with Plumed output configuration.
  - **Solution**: Check Plumed output settings and use snapshots for data recovery.

- **Plumed Installation**:
  - **Root Cause**: Plumed not installed on GPU systems.
  - **Solution**: Use Emmy cluster where Plumed is supported.

- **Priority Boost**:
  - **Root Cause**: Long queue times.
  - **Solution**: Request priority boost from HPC admins.

### Additional Notes:
- **GPU Access**: TinyGPU can be accessed via Woody, but queue times may still be long.
- **Gromacs Chain Jobs**: Successfully run by many users, using `-maxh` to ensure graceful job completion.
- **Data Recovery**: Snapshots can be found in the `/home/vault` directory.

This summary provides a concise overview of the issues and solutions discussed in the support ticket, serving as a reference for future support cases.
---

### 2018121742002011_PLUMED%2BGromacs%20%20installation%20on%20Meggie.md
# Ticket 2018121742002011

 # HPC-Support Ticket Conversation: PLUMED+Gromacs Installation on Meggie

## Keywords
- PLUMED
- Gromacs
- Installation
- Software Policy
- User Account
- Meggie Cluster

## Summary
A user inquired about installing PLUMED (v. 2.4) as a patch to Gromacs 2018-4 on the Meggie cluster. The user was unsure if they were allowed to install software on their account.

## Root Cause
- User uncertainty about software installation policy on the HPC cluster.

## Solution
- HPC Admin confirmed that users are allowed to install software on their accounts.

## General Learnings
- Users can install software on their accounts on the Meggie cluster.
- PLUMED can be installed as a patch to Gromacs for MD simulations.

## Ticket Conversation
### User
```
Dear HPC Admin,

We need to use PLUMED (v. 2.4)+Gromacs for some of our simulations. PLUMED is a plugin that works with some MD codes and can be used to analyze MD simulations or to bias them. It can be installed as a patch to Gromacs 2018-4.

Can I install it on MEGGIE on e.g. my account or is it not allowed to install software on the clusters? (sorry, I couldn't find this information on the website).

Many thanks,
Best regards,
User
```

### HPC Admin
```
Dear User,

Feel free to install it yourself!

Best,
HPC Admin
```

## Conclusion
Users are permitted to install software on their accounts on the Meggie cluster, including PLUMED as a patch to Gromacs for MD simulations.
---

### 2020031242001613_Gromacs%20jobs%20on%20Emmy%20-%20bccc018h.md
# Ticket 2020031242001613

 # HPC Support Ticket: Gromacs Jobs on Emmy

## Keywords
- Gromacs
- MPI
- Job Script
- Parallel Execution
- Scaling Tests
- PME Processes

## Problem
- User's jobs on Emmy were not behaving as expected.
- Using `mpirun` in a bash script caused high load on nodes.
- Incorrect executable (`gmx mdrun`) used for parallel Gromacs.

## Root Cause
- Incorrect use of `mpirun` in the job script.
- Wrong Gromacs executable for parallel processing.

## Solution
- Replace `gmx mdrun` with `mdrun_mpi` for parallel execution.
- Avoid using `mpirun` in the bash script.
- Provided a corrected job script for the user.

## Job Script Example
```bash
#!/bin/bash -l
#PBS -N partial_agonist
#PBS -l nodes=4:ppn=40
#PBS -l walltime=24:00:00
#PBS -m abe
#PBS -M user@fau.de
module load gromacs/2019.6-mkl-IVB-plumed-2.6.0-drr
cd $PBS_O_WORKDIR
i=0
while [ $i -lt 300 ]; do
let j=i+1
gmx grompp -f 100ps_eq.mdp -c pa_100ps_eq_${i}.gro -p pa_system_100ps_eq_${i}.top -r pa_100ps_eq_${i}.gro -n index.ndx -o pa_100ps_eq_${j}.tpr -maxwarn 2
mpirun mdrun_mpi -v -deffnm pa_100ps_eq_${j} -maxh 23.5
./remove_water.pl pa_100ps_eq_${i}.gro pa_system_100ps_eq_${i}.top pa_100ps_eq_${j}.gro water_${i}.gro pa_system_100ps_eq_${j}.top
echo -e "0\nq" | gmx make_ndx -f pa_100ps_eq_${j}.gro -o index.ndx
let i++
done
```

## Additional Recommendations
- Conduct scaling tests before increasing node counts.
- Tune the number of PME processes based on input requirements.

## References
- [Gromacs Documentation](https://www.anleitungen.rrze.fau.de/hpc/special-applications-and-tips-tricks/gromacs/)

## Outcome
- The user's jobs were corrected and ran successfully.
- The choice of 4 nodes was deemed appropriate.
---

### 2023062242000737_Gromacs%20Job%20on%20Alex%20does%20not%20use%20GPU%20%5Bb171dc10%5D.md
# Ticket 2023062242000737

 # HPC Support Ticket: Gromacs Job on Alex does not use GPU

## Keywords
- Gromacs
- GPU
- JobID 767839
- Logs
- Walltime
- LINCS-Fehler
- ssh-Key
- srun
- FAQ

## Problem Description
- Gromacs job on Alex (JobID 767839) stopped using GPU after a short period.
- Suspected bug in Gromacs causing it to hang without properly terminating.
- User did not receive Gromacs log files due to job termination and walltime issues.
- User unable to log into the node running the job.

## Root Cause
- Possible LINCS-Fehler causing Gromacs to crash with a "core dump."
- Job terminated due to walltime, preventing log files from being written back to $WORK.
- User unable to log into the node due to lack of ssh-key for Portalaccounts.

## Solution
- Check for LINCS-Fehler in future jobs.
- Use srun to attach to running jobs: `srun --pty --overlap --jobid YOUR-JOBID bash [-l]`.
- Refer to FAQ for logging into nodes: [FAQ Link](https://hpc.fau.de/faqs/#innerID-13183).

## General Learnings
- Ensure proper handling of walltime and log file storage.
- Understand the limitations of Portalaccounts for logging into nodes.
- Use srun to attach to running jobs for troubleshooting.
- Be aware of potential bugs in software like Gromacs that may cause jobs to hang.
---

### 2019020642002647_bccb15%2C%20core.-files.md
# Ticket 2019020642002647

 # HPC Support Ticket: Core Dump Files in User Directory

## Keywords
- Core dump files
- Segmentation fault
- Gromacs
- `ulimit`
- `/etc/security/limits.conf`

## Problem Description
- User observed multiple 20GB `core.xxxx` files in their directory.
- These files were generated in a short period on 01.02.
- The directory contains a long-running Gromacs simulation.

## Root Cause
- The `core.xxxx` files are core dumps generated due to a segmentation fault in the Gromacs simulation.

## Solution
- **Immediate Action**: Disable core dump generation by adding `ulimit -c 0` at the beginning of the job script.
- **Long-term Fix**: Update `/etc/security/limits.conf` with `* soft core 0` to prevent core dump generation system-wide. This change will be applied in the next image rebuild and deployment on Meggie.

## General Learnings
- Core dump files are generated upon segmentation faults for debugging purposes.
- Core dump generation can be controlled using `ulimit -c` command.
- System-wide settings for core dump generation can be managed via `/etc/security/limits.conf`.
- It's important to use official support channels instead of contacting individual staff members.
---

### 2020110542001648_gromacs%20module%20gromacs_2020.1-mkl-CUDA102.md
# Ticket 2020110542001648

 # HPC Support Ticket: Segmentation Fault with GROMACS

## Keywords
- Segmentation Fault
- GROMACS
- mdrun
- CUDA
- PBS Flags

## Problem Description
- User encountered segmentation faults when running GROMACS (version 2020.1-mkl-CUDA102) using `mdrun`.
- The issue was consistent across multiple jobs.
- User suspected potential issues with PBS flags in the job script.

## Error File
- `/home/woody/tumu/tumu002h/my_example/protein/JRUN_protein_unres.err`

## Job Script
- `/home/woody/tumu/tumu002h/my_example/protein/JRUN_protein_unrestrained`

## Root Cause
- The root cause of the segmentation fault was not explicitly identified in the conversation.

## Solution
- The user resolved the issue independently.
- HPC Admins noted that they would have limited insights into segmentation faults.

## General Learnings
- Segmentation faults in GROMACS can be challenging to diagnose.
- Users should review their job scripts and configurations for potential issues.
- Independent troubleshooting can sometimes resolve complex issues.

## Next Steps for Support
- If similar issues arise, encourage users to review their job scripts and configurations.
- Provide resources or documentation on common causes of segmentation faults in GROMACS.
- Consider consulting with the Training and Support Group Leader (Georg Hager) for additional insights.
---

### 2021081242001835_Gromacs-Job%20auf%20Meggie%20%5Bbccb007h%5D.md
# Ticket 2021081242001835

 ```markdown
# HPC Support Ticket: Gromacs-Job auf Meggie [bccb007h]

## Keywords
- Gromacs
- Meggie
- TinyGPU
- Version 2019
- Version 2021.1
- 1-Knoten-Jobs
- GPU-Cluster
- Module Load

## Problem
- User was running Gromacs jobs on Meggie using an outdated version (2019).
- Inefficient use of resources by running 1-Knoten-Jobs on a massively parallel cluster.

## Solution
- HPC Admin advised the user to switch to the latest Gromacs version.
- Recommended moving Gromacs jobs to the TinyGPU cluster, which has the latest Gromacs version available via `module load gromacs/2021.1-mkl-CUDA111-ebyjbq`.
- Offered assistance for the transition to TinyGPU.

## General Learnings
- Always use the latest software versions for optimal resource utilization.
- Consider moving jobs to specialized clusters (e.g., GPU clusters) for better performance.
- HPC Admins can assist with transitions and provide necessary support.
```
---

### 2024030742000993_GROMACS%202024.1%20_%20Performance%20_%20Best%20Practice.md
# Ticket 2024030742000993

 ```markdown
# HPC-Support Ticket: GROMACS 2024.1 / Performance / Best Practice

## Subject
GROMACS 2024.1 / Performance / Best Practice

## User Report
- **Issue 1:** Error when using old submit script with `-ntmpi 1` flag.
  - **Error Message:** "Setting the number of thread-MPI ranks is only supported with thread-MPI and GROMACS was compiled without thread-MPI"
  - **Solution:** Remove `-ntmpi 1` flag.
  - **Impact:** Only single GPU jobs can be submitted on Alex.

- **Issue 2:** Warning about GPU-aware MPI.
  - **Warning Message:** "GPU-aware MPI detected, but by default GROMACS will not make use the direct GPU communication capabilities of MPI. For improved performance try enabling the feature by setting the GMX_ENABLE_DIRECT_GPU_COMM environment variable."
  - **Solution:** Setting `GMX_ENABLE_DIRECT_GPU_COMM=1` resulted in slight performance degradation.
  - **Impact:** No performance improvement observed.

- **Issue 3:** Best practice for `mdrun` command.
  - **Proposal:** Change `mdrun` command for single GPU job on Alex.
  - **Current Command:**
    ```sh
    gmx mdrun -s -ntmpi 1 -ntomp 16 -pme gpu -bonded gpu -update gpu -pin on -pinstride 1 -deffnm $TPR -cpi $SLURM_SUBMIT_DIR/$TPR
    ```
  - **Proposed Command:**
    ```sh
    gmx_mpi mdrun -s -pin on -pinstride 1 -deffnm $TPR -cpi $SLURM_SUBMIT_DIR/$TPR
    ```
  - **Reason:** Automatic GPU usage, avoids potential job failures.

## HPC Admin Response
- **Issue 1 & 2:** Fixed by updating the module. The wrong build variant (`gmx_mpi` instead of `gmx`) was used.
- **Issue 3:** HPC Admin will add a note about potential errors with `-update gpu` and will benchmark the system with OPC-water on Fritz and Alex.

## Benchmark Results
- **System:** A40, gmx2024.1
- **Command:**
  ```sh
  gmx mdrun -s OPC-water.tpr -ntmpi 1 -ntomp 16 -nsteps 200000 -nb gpu -pme gpu -bonded gpu -update cpu -pin on -pinstride 1 -pinoffset 0
  ```
- **Performance:** 205.318 ns/day

## Conclusion
- **Root Cause:** Incorrect build variant used for GROMACS 2024.1.
- **Solution:** Update the module to the correct build variant.
- **Best Practice:** Use the proposed `mdrun` command for single GPU jobs to avoid potential job failures.
```
---

### 2023110242002709_Gromacs%20Jobs%20on%20TinyGPU%20do%20not%20use%20GPU%20%5Bmpt4022h%5D.md
# Ticket 2023110242002709

 # HPC Support Ticket: Gromacs Jobs on TinyGPU do not use GPU

## Keywords
- Gromacs
- GPU
- TinyGPU
- JobIDs 679822 and 679830
- .tpr files
- SLURM
- Domain decomposition
- Equilibration

## Problem Description
- User's Gromacs jobs on TinyGPU are not utilizing the allocated GPUs.
- Jobs are expected to offload non-bonding calculations to the GPU.

## Root Cause
- The system is not well equilibrated, leading to domain decomposition errors.
- Initial temperature set to 0 K, which might not be suitable for the simulation.

## Ticket Conversation Summary
- **HPC Admin**: Notified the user about the GPU utilization issue and offered to benchmark the system.
- **User**: Provided .tpr files and the job submission script for benchmarking.
- **HPC Admin**: Attempted to benchmark the system but encountered domain decomposition errors. Suggested longer equilibration and consultation with the user's supervisor.

## Solution/Next Steps
- Ensure the system is properly equilibrated before running the simulation.
- Re-evaluate the initial temperature setting for the simulation.
- Consult with the user's supervisor for further guidance.

## Notes
- The job submission script provided by the user includes various environment variables for GPU settings.
- The HPC Admin mentioned testing on a different system (fritz) due to issues on TinyGPU.

## Related Resources
- [Gromacs Documentation](http://manual.gromacs.org/documentation/)
- [FAU HPC Documentation](https://hpc.fau.de/)

## Ticket Status
- Unresolved; awaiting user action to equilibrate the system and potentially adjust simulation parameters.
---

### 42172352_modified%20version%20of%20gromacs.md
# Ticket 42172352

 # HPC Support Ticket Conversation: Modified Version of Gromacs Installation

## Keywords
- Gromacs installation
- Compiler issues
- MPI support
- Library mismatch
- GLIBC version
- cmake errors

## General Learnings
- **Compiler Mismatch**: Ensure that the compiler used by MPI-compiler wrappers matches the plain compiler used in other circumstances.
- **Library Compatibility**: Binaries compiled on one system may not run on another due to differences in Linux distributions and library versions.
- **MPI Support**: Verify that Gromacs is built with true MPI support for multi-node runs.
- **Error Reporting**: Provide detailed error messages and steps taken to help diagnose issues more effectively.

## Root Cause of Problems
1. **Compiler Mismatch**: The error message indicated a mismatch between the compiler used by the MPI-compiler wrappers and the plain compiler.
2. **Library Mismatch**: Binaries compiled on Woody did not run on LiMa due to differences in Linux distributions and library versions.
3. **GLIBC Version**: The version of GLIBC required by the compiled binaries was not available on LiMa.
4. **cmake Errors**: cmake failed on LiMa with an undefined reference to `isfinite`.

## Solutions
1. **Compiler Mismatch**: Use the Intel compilers and Intel MKL for FFTs to ensure compatibility.
   ```bash
   module purge
   module load intel64/12.1up11
   ./configure --prefix=/home/woody/bccb/..... --with-fft=mkl CC=icc CFLAGS="-O3 -axSSE4.2,SSE4.1,SSSE3,SSE3,SSE2 $MKL_INC" CXX=icpc CXXFLAGS="-O3 -axSSE4.2,SSE4.1,SSSE3,SSE3,SSE2 $MKL_INC" LDFLAGS="-L$MKL_BASE/lib/em64t -Wl,-rpath,$MKL_BASE/lib/em64t" --enable-shared
   make; make install
   ```
2. **Library Compatibility**: Use the provided Gromacs module on LiMa if available.
3. **GLIBC Version**: Ensure that the required GLIBC version is available on the target system.
4. **cmake Errors**: Verify that all dependencies are correctly installed and that the build environment is properly configured.

## Additional Notes
- **MPI Support**: Use `ldd` to check if the compiled binaries reference `libmpi*` to ensure true MPI support.
- **Script Issues**: Ensure that job scripts are correctly configured to avoid issues with multiple processes running simultaneously.

This documentation can be used to diagnose and resolve similar issues in the future.
---

### 2020082642001374_Plumed%20plugin.md
# Ticket 2020082642001374

 # HPC Support Ticket: Plumed Plugin

## Keywords
- Metadynamics simulations
- Gromacs
- Plumed plugin
- Data analysis
- Module loading

## Problem
- User is performing metadynamics simulations using Gromacs with Plumed on Emmy.
- User needs the Plumed plugin to analyze the data produced by the simulations.
- User is unsure if Plumed is set up correctly on Emmy.

## Root Cause
- User was unaware that Plumed is already included in the Gromacs module they are using.
- User needed guidance on how to access and use Plumed for data analysis.

## Solution
- Confirm that Plumed is included in the `gromacs/2019.6-mkl-IVB-plumed-2.6.0-drr` module.
- Instruct the user to load the Gromacs module and verify the Plumed installation by running `which plumed` on the command line.
- Provide the path to the Plumed installation: `/apps/Gromacs/plumed-2.6.0-drr-boost/bin/plumed`.
- Advise the user to use Plumed as a command line tool for analysis.

## General Learning
- Always check if the required tools are included in the modules you are using.
- Use the `which` command to verify the installation path of tools.
- Load the necessary modules to access the tools for data analysis.

## Related Documentation
- [Gromacs Documentation](http://www.gromacs.org/Documentation)
- [Plumed Documentation](https://www.plumed.org/doc-v2.6/user-doc/html/_index.html)
- [RRZE HPC Services](http://www.hpc.rrze.fau.de/)
---

### 2022012742001032_Gromacs%20Jobs%20auf%20TinyGPU%2C%20%24TMPDIR%2C%20miniconda%20%5Bbcpc000h%5D.md
# Ticket 2022012742001032

 # HPC Support Ticket: Gromacs Jobs auf TinyGPU, $TMPDIR, miniconda

## Keywords
- Gromacs
- TinyGPU
- $TMPDIR
- miniconda
- NFS-Server
- Performance
- Simulation
- Job Submission

## Problem
- High load on NFS servers causing performance issues for Gromacs jobs.
- User is using a miniconda version of Gromacs in addition to the provided module.
- Issues with `gmx trjconv` and `gmx grompp` on TinyGPU nodes.

## Root Cause
- High load on NFS servers leading to slower data access and write operations.
- Incompatibility or issues with the provided Gromacs module on TinyGPU nodes, leading to the use of a miniconda version.

## Solution
- **Use $TMPDIR for Simulation Data:**
  - Write simulation data to the local disk ($TMPDIR) during the job.
  - Copy the data back to the submission directory at the end of the job.
  - Ensure enough time is allocated for copying data before job termination.

- **Script Modification:**
  ```bash
  cp ./$TPR $TMPDIR
  cd $TMPDIR
  gmx mdrun -s -ntmpi 1 -ntomp 32 -pme gpu -bonded gpu -update gpu -pin on -pinstride 1 -v -deffnm $TPR -cpi $SLURM_SUBMIT_DIR/$TPR
  cp * $SLURM_SUBMIT_DIR
  cd $SLURM_SUBMIT_DIR
  ```

- **Remove miniconda and Local GMX Installation:**
  - The user removed the miniconda and local GMX installation from the scripts as the provided Gromacs module worked well on other clusters (Alex and Meggie).

## Additional Notes
- The user will share the modified scripts with colleagues to reduce support workload.
- The HPC admin will investigate the issues with `gmx trjconv` and `gmx grompp` on TinyGPU nodes.
- The use of `rsync -a` is recommended for copying data back to the submission directory if more input is copied.

## Conclusion
- Using $TMPDIR for simulation data helps mitigate performance issues caused by high load on NFS servers.
- The provided Gromacs module should be sufficient for most clusters, but specific issues on TinyGPU nodes need further investigation.
- Sharing modified scripts with colleagues helps in standardizing best practices and reduces support workload.
---

### 2018032042002003_gmx%20auf%20tinygpu%3F.md
# Ticket 2018032042002003

 # HPC Support Ticket: GROMACS on tinygpu Cluster

## Keywords
- GROMACS
- tinygpu cluster
- CUDA
- mdrun
- mdrun_mpi
- Multi-Node
- MPI
- GPU
- PME
- Energiegruppe
- ntmpi
- ntomp
- Pinning

## Summary
A user inquired about running GROMACS on the tinygpu cluster using the CUDA variant. The user also had issues with multi-node parallelization using GROMACS.

## Root Cause
- User needed guidance on using GROMACS with CUDA on the tinygpu cluster.
- User faced issues with multi-node parallelization using GROMACS.

## Solution
### Using GROMACS with CUDA on tinygpu
- Use the module `gromacs/2018.0-mkl-CUDA91`.
- Ensure only one energy group is defined.
- At least one MPI process per GPU is required.
- Adjust `-ntmpi` and `-ntomp` values as needed.
- Use `-pme` to specify whether PME calculations should be done on GPU or CPU.
- Run GROMACS with `gmx mdrun`.
- Check GROMACS output for GPU usage and thread allocation.

### Multi-Node Parallelization
- Use `mdrun_mpi` for multi-node runs.
- Example command: `mpirun_rrze -v -pinexpr S0:0-9@S1:0-9`.

## General Learnings
- Always check for the correct module version to avoid incorrect results.
- Proper configuration of MPI and OpenMP threads is crucial for efficient GPU usage.
- Monitor GROMACS output to ensure GPUs are being utilized correctly.
- Multi-node runs require specific commands and configurations.

## Ticket Status
- The ticket was closed as the user's issues were resolved.

## Additional Notes
- The user was advised to experiment with different configurations to optimize performance.
- The HPC Admin provided detailed instructions and closed the ticket after resolving the user's queries.
---

### 2023113042001087_Gromacs%20Error%20-%20k101ee10.md
# Ticket 2023113042001087

 ```markdown
# HPC-Support Ticket: Gromacs Error - k101ee10

## Subject
Gromacs Error - k101ee10

## Keywords
- Gromacs
- File I/O error
- Disk space
- Fileserver load
- Local storage
- $TMPDIR

## Problem Description
User encountered repeated failures in Gromacs simulations under $WORK directory for project k101ee. The error message indicated a file input/output error, specifically unable to write 'md.log', suggesting a possible disk space issue. However, the user reported having sufficient disk space (~12 TB). The issue was specific to simulations named `kca_small_molecule`, `2_kca_small_molecule`, and `3_kca_small_molecule`.

## Root Cause
- High load on the fileserver causing delays in file operations.
- Frequent writing of `nstcalcenergy` every 100 steps and compressed trajectory every 1000 steps, which exacerbated the issue under high fileserver load.

## Solution
1. **Reduce Frequency of Data Writing**:
   - Adjust the `nstcalcenergy` and trajectory writing intervals in the `.mdp` file to reduce the frequency of file operations.

2. **Use Local Storage**:
   - Write simulation data to the local storage of the compute node using `$TMPDIR` at the beginning of the job.
   - Copy the data back to the fileserver at the end of the job.
   - Ensure sufficient time is allocated for copying data back before job termination.

## Example Usage
Refer to the example usage of Gromacs with local storage at [Gromacs Documentation](https://hpc.fau.de/systems-services/documentation-instructions/special-applications-and-tips-tricks/gromacs/#collapse_3).

## Additional Notes
- The HPC Admins are aware of the current fileserver load issues and are working to resolve them.
- Users should monitor their simulations and adjust data writing frequencies as needed to mitigate similar issues.
```
---

### 2018052842001737_problem%20running%20gromacs.md
# Ticket 2018052842001737

 ```markdown
# HPC Support Ticket: Problem Running GROMACS

## Keywords
- GROMACS
- Command not found
- MPI startup error
- OFA fabric not available
- Fallback fabric not enabled
- Job script
- stdout/stderr files

## Problem Description
- User unable to run GROMACS version 5.1.2-mkl-IVB on the Emmy cluster.
- Error message: "command not found."
- Attempted to use GROMACS with PLUMED patch for metadynamics simulations.
- Error message: "[0] MPI startup(): ofa fabric is not available and fallback fabric is not enabled."

## Root Cause
- GROMACS command not found indicates a possible issue with the module loading or environment setup.
- MPI startup error suggests a configuration issue with the MPI fabric settings.

## Requested Information
- Job script
- stdout/stderr files from the batch system

## Solution
- Not explicitly provided in the conversation.
- HPC Admin requested additional information to diagnose the issue further.

## General Learnings
- Ensure proper module loading and environment setup for GROMACS.
- Check MPI fabric settings and ensure fallback fabric is enabled.
- Provide job scripts and stdout/stderr files for detailed troubleshooting.
```
---

### 2022112842003564_gromacs%202022.md
# Ticket 2022112842003564

 # HPC Support Ticket: Gromacs 2022 Installation

## Keywords
- Gromacs 2022.4
- Bug-fix
- Cluster installation
- User request
- HPC Admin response

## Summary
A user requested the installation of the latest Gromacs version (2022.4) due to a bug-fix that affects their work. The HPC Admin inquired about the most urgent cluster for the installation and subsequently installed the software on the specified cluster.

## Root Cause
- User required the latest Gromacs version (2022.4) to address a specific bug-fix.

## Solution
- HPC Admin installed Gromacs 2022.4 on the specified cluster (Alex).
- Other clusters will follow in a stepwise manner.

## What Can Be Learned
- Importance of timely software updates to address user-specific issues.
- Effective communication between users and HPC Admins for prioritizing tasks.
- Stepwise installation approach for maintaining consistency across clusters.

## Steps Taken
1. User requested the installation of Gromacs 2022.4.
2. HPC Admin asked for the most urgent cluster.
3. User specified the cluster (Alex).
4. HPC Admin installed Gromacs 2022.4 on the specified cluster.
5. HPC Admin confirmed the installation and planned for stepwise installation on other clusters.

## Conclusion
Timely and targeted software updates are crucial for addressing user-specific issues. Effective communication and prioritization ensure smooth operations and user satisfaction.
---

### 2022012742001005_Gromacs%20Jobs%20auf%20TinyGPU%2C%20%24TMPDIR%2C%20miniconda%20%5Bbcpc001h%5D.md
# Ticket 2022012742001005

 # HPC Support Ticket: Gromacs Jobs auf TinyGPU, $TMPDIR, miniconda

## Keywords
- Gromacs
- Job script optimization
- NFS server load
- Local node storage
- Miniconda
- Gromacs version
- CPU vs GPU performance

## Problem
- High loads on NFS servers causing slow data access and write operations.
- User's jobs experiencing performance issues due to high NFS load caused by other users.
- User is using a miniconda version of Gromacs in addition to the provided module.

## Root Cause
- Inefficient job script leading to excessive NFS access.
- Unclear reason for using miniconda version of Gromacs.

## Solution
- **Job Script Optimization**: Modify the job script to write simulation data to the local node storage first and then copy it to the final destination to reduce NFS access.
- **Miniconda Clarification**: Investigate the reason for using the miniconda version of Gromacs. If it is not necessary, guide the user to use the provided module.
- **Resource Allocation**: Encourage the use of GPUs for Gromacs jobs as they provide better performance compared to CPUs.

## General Learnings
- High NFS loads can significantly impact job performance.
- Writing data to local node storage before copying it to the final destination can improve performance.
- Understanding the reasons behind users' software choices can help in providing better support.
- GPUs are generally more efficient for certain types of jobs, such as those using Gromacs.

## Follow-up Actions
- Monitor job performance after script optimization.
- Consider providing the latest version of Gromacs on CPU clusters if there is a valid use case and it helps in better resource utilization.
- Keep an eye on NFS server loads and optimize jobs accordingly.
---

### 2020081942000398_gromacs%20gmx%20binary%20on%20tinygpu.md
# Ticket 2020081942000398

 ```markdown
# HPC Support Ticket: gromacs gmx binary on tinygpu

## Summary
- **User Issue**: Unable to access gromacs binaries on tinygpu.
- **Root Cause**: Missing module or incorrect module loading.
- **Solution**: Ensure correct module is loaded and verify job script.

## Keywords
- gromacs
- gmx
- tinygpu
- module
- job script
- account sharing
- GPU allocation
- performance
- acknowledgment

## Lessons Learned
1. **Account Sharing**: Account sharing is not permitted. Each user must submit their own application.
2. **Module Loading**: Ensure the correct module is loaded in the job script.
3. **GPU Allocation**: Verify GPU allocation in the job script to avoid wasting resources.
4. **Performance Considerations**: Evaluate the cost-benefit of using specific GPUs for performance gains.
5. **Acknowledgment**: Follow the provided format for acknowledging HPC resources in publications.

## Detailed Conversation

### Initial Issue
- **User**: Unable to access gromacs binaries on tinygpu.
- **HPC Admin**: Requested job script, job ID, and output files for further investigation.

### Account Sharing
- **HPC Admin**: Noted that account sharing is not permitted. Each user must submit their own application.
- **User**: Confirmed that the job was submitted for a colleague and agreed to follow the correct procedure.

### Module Loading
- **User**: Provided job script with module `gromacs/2020.1-mkl-CUDA102` loaded.
- **HPC Admin**: Identified that the job was wasting GPU resources due to incorrect allocation.

### GPU Allocation
- **HPC Admin**: Noted that the job requested 2 GPUs but used only one. Suggested optimizing GPU allocation.
- **User**: Acknowledged the issue and agreed to correct the job script.

### Performance Considerations
- **HPC Admin**: Discussed the cost-benefit of using specific GPUs and the impact on performance.
- **User**: Agreed to evaluate the performance gains and adjust GPU allocation accordingly.

### Acknowledgment
- **User**: Requested guidance on acknowledging HPC resources in a publication.
- **HPC Admin**: Provided a suggested format for acknowledgment.

## Conclusion
- Ensure correct module loading and GPU allocation in job scripts.
- Follow the correct procedure for account applications and acknowledgments.
```
---

### 2020101442003381_Gromacs_Plumed%20problems.md
# Ticket 2020101442003381

 ```markdown
# Gromacs/Plumed Metadynamics Simulation Writing Problems

## Problem Description

The user, Jacqueline Calderon, is experiencing writing problems with the HILLS file generated from metadynamics simulations using Gromacs/Plumed on Meggie. The HILLS file contains corrupted data, indicated by null characters (`^@`) and incomplete lines. This issue occurs when running multiple replicas in parallel, with each replica writing to the same COLVAR and HILLS files.

## Troubleshooting Steps

1. **Initial Communication**:
   - The user provided details about the problem, including the simulation setup and the corrupted HILLS file.
   - The user mentioned that the issue does not occur on other HPC systems like SuperMUC.

2. **HPC Admin Response**:
   - HPC Admins (Thomas Zeiser, Anna Kahler) investigated the issue and suggested that the problem might be due to multiple processes writing to the same file simultaneously.
   - They recommended checking if the problem is reproducible and if it occurs on other HPC systems.

3. **Further Investigation**:
   - The user uploaded relevant files to the FAUbox for further analysis.
   - HPC Admins attempted to reproduce the issue but were unable to do so with the provided setup.

4. **Potential Solution**:
   - HPC Admins suggested using the `-multidir` option from the GROMACS documentation to run multiple simulations in separate directories, which might prevent writing conflicts.
   - The command to run the simulations would be: `mpirun -np x gmx_mpi mdrun -s topol -multidir <names-of-directories>`.

## Conclusion

The writing problem in the HILLS file is likely caused by multiple processes writing to the same file simultaneously. Using the `-multidir` option to run simulations in separate directories may resolve the issue. The user will attempt this solution in their next simulations.

## References

- [GROMACS Documentation on Multi-Simulations](http://manual.gromacs.org/documentation/current/user-guide/mdrun-features.html#running-multi-simulations)
```

This report provides a concise overview of the problem, the troubleshooting steps, and the potential solution. It can be used as a reference for HPC support employees to address similar issues in the future.
---

### 2022030442001643_pl%C3%83%C2%B6tzlich%20h%C3%83%C2%A4ngende%20Gromacs-Jobs%20auf%20Alex%20-%20bccb004h.md
# Ticket 2022030442001643

 ```markdown
# HPC-Support Ticket: plötzlich hängende Gromacs-Jobs auf Alex - bccb004h

## Problem Description
Gromacs jobs are hanging after a certain number of steps, specifically around 81500000 steps. The issue is reproducible and affects all available Gromacs versions (2020.6, 2021.4, 2021.5, 2022). The problem occurs only with systems that use constraints and virtual sites, such as those containing cholesterol.

## Root Cause
The root cause appears to be a threadMPI-Deadlock in the Gromacs software. The stack trace indicates that the process is stuck in `tMPI_Event_wait` and `dd_sendrecv2_rvec` functions.

## Affected Systems
- Alex cluster
- A100 GPU
- Systems with cholesterol (using constraints and virtual sites)

## Observations
- The issue occurs regardless of the storage location (e.g., $TMPDIR).
- The problem does not occur on a local machine with Gromacs 2021.4.
- Resubmitting the job allows it to continue from where it left off, but it hangs again after another 81500000 steps.

## Workaround
Restarting the job allows it to continue from the last checkpoint, although it will hang again after the same number of steps.

## Debugging Steps
- HPC Admin attached a debugger to the hanging process and identified the deadlock in the Gromacs source code.
- The user tested various configurations and versions to narrow down the issue.

## Next Steps
- Further investigation into the Gromacs source code is required to identify and fix the deadlock.
- Testing with different `ntomp` and `ntmpi` settings may provide additional insights.

## Conclusion
The issue is likely a bug in the Gromacs software that causes a threadMPI-Deadlock. Restarting the job is a temporary workaround, but a permanent fix will require deeper investigation into the Gromacs source code.
```
---

### 2024020542003254_GROMACS%202023.4.md
# Ticket 2024020542003254

 ```markdown
# HPC-Support Ticket: GROMACS 2023.4 Installation Request

## Keywords
- GROMACS
- Installation
- Version 2023.4
- Alex
- gcc11.2.0
- mkl
- cuda

## Problem
- User requested the installation of GROMACS 2023.4 on the Alex system.

## Solution
- HPC Admin confirmed the availability of GROMACS 2023.4 with the configuration `gromacs/2023.4-gcc11.2.0-mkl-cuda` on Alex.

## General Learnings
- Users can request specific software versions to be installed on HPC systems.
- HPC Admins can provide information on the availability of requested software versions and their configurations.
- Communication between users and HPC Admins is essential for ensuring that the required software is available and properly configured.
```
---

### 2024062542002924_Low%20GPU%20utilization%20for%20multi-GPU%20Gromacs%20Job%20on%20Alex%20%5Bb119ee10%5D.md
# Ticket 2024062542002924

 # Low GPU Utilization for Multi-GPU Gromacs Job

## Keywords
- Low GPU utilization
- Gromacs
- Multi-GPU
- Benchmarks
- TPR file

## Problem Description
- User reported low GPU utilization for a currently running Gromacs job.
- The job was slower compared to previous similar jobs.

## Root Cause
- The exact root cause was not determined in the initial conversation.

## Solution
- HPC Admin offered to run benchmarks to identify potential improvements.
- User uploaded the TPR file to the admin's FAUbox for further analysis.

## Actions Taken
- HPC Admin contacted the user to offer assistance.
- User uploaded the necessary TPR file for benchmarking.

## General Learnings
- Low GPU utilization can significantly impact job performance.
- Benchmarking can help identify and resolve performance issues.
- Collaboration between users and HPC support is essential for troubleshooting.

## Next Steps
- Run benchmarks using the provided TPR file.
- Analyze the results to identify potential improvements.
- Provide feedback and recommendations to the user.
---

### 2021112242001944_Fw%3A%20Frage%20bzgl.%20gmx%20tune_pme.md
# Ticket 2021112242001944

 ```markdown
# HPC-Support Ticket Conversation: gmx tune_pme Issues

## Subject
Frage bzgl. gmx tune_pme

## Keywords
- GROMACS 2021.1
- tune_pme
- mdrun
- MPI
- srun
- mpirun
- PMI server
- I_MPI_PMI_LIBRARY
- benchtest.log
- Invalid --distribution specification
- Device or resource busy
- OFI endpoint open failed

## Problem Description
The user encountered issues with `gmx tune_pme` for GROMACS 2021.1 on Meggie. The script for earlier GROMACS versions kept failing with the message that `mdrun` could not be called. The error message in `benchtest.log` indicated an invalid `--distribution` specification. Additionally, every GROMACS command displayed a warning about the PMI server not being found.

## Root Cause
- The `export MPIRUN` variable was causing issues with `srun`, which expects `-n` or `--ntasks` instead of `-np`.
- The `gmx tune_pme` command was failing due to resource allocation issues when `-np` was set to values greater than 18.
- The serial binary of GROMACS was required for `tune_pme` to function correctly.

## Solution
- Ignore the PMI server warning as it is not critical for the initial `gmx_mpi tune_pme` command.
- Remove the `export MPIRUN` variable and use `mpirun` directly.
- Use the serial binary of GROMACS for `tune_pme`:
  ```bash
  /apps/SPACK/0.16.1/opt/linux-centos7-broadwell/gcc-8.2.0/gromacs-2021.1-jphnxl67mz7tffs54c5h54atlh5hv5xw/bin/gmx tune_pme -s *.tpr -steps 10000 -resetstep 2000 -ntpr 0 -r 2 -npme auto -np 120 -mdrun 'gmx_mpi mdrun'
  ```
- Ensure that the `-np` value does not exceed 18 for successful execution.

## General Learning
- Understand the differences between `srun` and `mpirun` command flags.
- Be aware of resource allocation limits and adjust `-np` values accordingly.
- Use the correct binary (serial vs. parallel) for specific GROMACS commands.
- Ignore non-critical warnings unless they directly impact the command execution.
```
---

### 2024112542003146_Renaming%20error%20-%20n102af11.md
# Ticket 2024112542003146

 ```markdown
# HPC-Support Ticket: Renaming Error - n102af11

## Subject
Renaming error for simulation files using GROMACS on Alex.

## User Issue
- **Error Description**: System I/O error: Failed to rename temp.top0jzR6w to /home/atuin/n102af/n102af11/PDZ2_Jul21_Second/newtop.top
- **Context**: User running GROMACS simulations on Alex, storing data on /home/atuin.

## HPC Admin Response
- **Root Cause**: High load on the file server (atuin) causing I/O errors.
- **Suggested Solution**:
  - Use node-local storage (`$TMPDIR`) for temporary files during the simulation.
  - Allocate an interactive job for preparation and submit production as a chain job.
  - Example job script: [GROMACS Single GPU Job on Alex](https://doc.nhr.fau.de/apps/gromacs/#single-gpu-job-on-alex).

## Follow-Up
- **User Query**: Request for specific script modifications to use `$TMPDIR`.
- **HPC Admin**: Scheduled a Zoom meeting to assist with script modifications.
- **Additional Issue**: User unable to get a prompt after login due to file server issues.
- **Final Recommendation**: Redo the setup in the affected directory due to a corrupted file.

## Keywords
- GROMACS
- Renaming error
- File server load
- Node-local storage
- Interactive job
- Chain job
- Script modification
- Zoom meeting
- Corrupted file

## Lessons Learned
- High load on file servers can cause I/O errors.
- Using node-local storage (`$TMPDIR`) can alleviate file server load.
- Interactive jobs can be used for preparation, followed by chain jobs for production.
- Corrupted files may require a complete setup redone in the affected directory.
```
---

### 2022072742002548_Metadynamics%2C%20Fail.md
# Ticket 2022072742002548

 ```markdown
# HPC-Support Ticket: Metadynamics Simulation Fail

## Keywords
- Metadynamics Simulation
- Segmentation Fault
- HILLS File
- .bashrc
- GROMACS
- PLUMED

## Problem Description
The user encountered a segmentation fault while running a metadynamics simulation on the HPC cluster. The error occurred during the execution of the `mdrun` command, specifically when the `plumed` library was performing calculations.

## Error Message
```
[f0778:229246:0:229246] Caught signal 11 (Segmentation fault: address not mapped to object at address (nil))
==== backtrace (tid: 229246) ====
...
srun: error: f0778: task 366: Segmentation fault (core dumped)
srun: launch/slurm: _step_signal: Terminating StepId=111990.0
```

## Root Cause
The issue was traced to the user's `~/.bashrc` file, which was binding a custom version of GROMACS via miniconda. This custom setup was causing conflicts with the HPC cluster's software environment.

## Solution
The user deleted the `~/.bashrc` file, which resolved the segmentation fault issue. This indicates that the custom GROMACS setup was the root cause of the problem.

## Lessons Learned
- Custom software setups in user environments (e.g., via `.bashrc` and miniconda) can cause conflicts with the HPC cluster's software stack.
- Deleting or modifying the `~/.bashrc` file can resolve such conflicts.
- It is important to ensure that the software versions and configurations used in the HPC environment are compatible with the cluster's setup.

## Additional Notes
- The user initially attempted to run the simulation with a pre-created HILLS file, which did not resolve the issue.
- The problem was reproducible with the same input files used by another user who did not encounter the issue, suggesting a user-specific configuration problem.
```
---

### 2022120842002421_constant%20pH%20sims%20mit%20gromacs.md
# Ticket 2022120842002421

 # HPC Support Ticket: Constant pH Simulations with GROMACS

## Keywords
- GROMACS
- Constant pH simulations
- Performance
- CPU installation
- GPU installation
- Production quality

## Summary
A user requested the installation of a specific GROMACS version that supports constant pH simulations. The request was initially delayed due to a special GROMACS version required for an NHR project. The HPC Admin later installed the requested version on the Fritz cluster.

## User Request
- Installation of GROMACS version for constant pH simulations.
- Links to the GitLab repository and associated paper provided.
- Performance considerations for CPU and GPU installations mentioned.

## HPC Admin Response
- Installation of `gromacs-constantph/9bb0cc2f-gcc8.5.0-impi-mkl` on Fritz.
- Notification that the code is not yet of production quality and results should not be published.
- Advice to wait for the final version to be merged into GROMACS.

## User Feedback
- Acknowledgment of the installation.
- Concern about the code quality and plans to review it in January.
- Appreciation for the support and well-wishes for the holidays.

## Lessons Learned
- Importance of communicating the production readiness of software versions.
- Handling requests for specific software versions and their dependencies.
- Considerations for performance differences between CPU and GPU installations.
- Managing user expectations regarding software quality and updates.

## Solution
- The requested GROMACS version was installed on the Fritz cluster.
- Users were advised to wait for the final production-quality version before publishing results.
---

### 2022071942001724_MetaD%20on%20Fritz.md
# Ticket 2022071942001724

 # HPC Support Ticket: MetaD on Fritz

## Keywords
- Gromacs
- MetaD
- Shared Libraries
- libgsl.so.25
- Spack
- Reinstallation

## Problem Description
The user encountered an error while executing Gromacs on the Fritz cluster. The error message indicated a missing shared library:
```
/apps/SPACK/0.17.1/opt/linux-almalinux8-icelake/gcc-11.2.0/gromacs-2021.4-cslbgjlcidgpwkel54pqcleu63eeqfek/bin/gmx_mpi:
error while loading shared libraries: libgsl.so.25: cannot open shared object file: No such file or directory
```

## Root Cause
The HPC Admins identified that the Gromacs installation was missing the `libgsl.so.25` shared library due to a missing Spack package.

## Solution
The HPC Admins reinstalled the Gromacs version with the Plumed plugin, ensuring that all necessary dependencies, including `gsl` and `py-cython`, were included.

## Steps Taken
1. The user reported the issue with a detailed error message and the script used.
2. The HPC Admins investigated and found that the `gsl` package was missing.
3. The Gromacs version with the Plumed plugin was reinstalled to include the missing dependencies.
4. The user was notified to try again, and the issue was resolved.

## Lessons Learned
- Ensure all dependencies are correctly installed when using Spack packages.
- Reinstallation of software packages can resolve issues related to missing dependencies.
- Effective communication between users and HPC Admins is crucial for quick problem resolution.

## Script Used by the User
```bash
#!/bin/bash -l
#SBATCH --job-name=test_meta
#SBATCH --ntasks-per-node=72
#SBATCH --partition=singlenode
#SBATCH --nodes=1
#SBATCH --time=24:00:00
#SBATCH --export=NONE
#SBATCH --mail-type=all
#SBATCH --mail-user=jacqueline.c.calderon@fau.de

unset SLURM_EXPORT_ENV
module load gromacs/2021.4-gcc11.2.0-ompi-mkl-plumed
export I_MPI_JOB_RESPECT_PROCESS_PLACEMENT=off
srun gmx_mpi mdrun -v -deffnm npy4_02rsr_Gi_meta -plumed plumed_ini.dat -cpi
```

## Conclusion
The issue was resolved by reinstalling the Gromacs package with all necessary dependencies. This highlights the importance of ensuring that all required libraries are present when using software packages on HPC systems.
---

### 2021081842002378_Multi-walker%20Gromacs%20von%20multi-gpu%20machines.md
# Ticket 2021081842002378

 ```markdown
# Multi-walker Gromacs on Multi-GPU Machines

## Keywords
- Multi-walker metadynamics
- Gromacs
- PLUMED
- Multi-GPU
- Performance optimization
- Walkers
- TPR files

## Summary
A user needed assistance with running multi-walker metadynamics on multi-GPU machines using Gromacs and PLUMED. The initial setup involved 10 walkers, but it was recommended to use a multiple of 8 walkers for better performance.

## Problem
- Initial setup with 10 walkers was not optimal.
- PLUMED patches for Gromacs 2021 were not available, necessitating the use of Gromacs 2020.
- Performance needed to be optimized for multi-GPU setups.

## Solution
- The user was advised to create TPR files compatible with Gromacs 2020.
- The number of walkers was increased to 32 and then to 64 to better saturate the GPUs.
- A script was provided to adjust the number of tasks and GPUs.
- Performance metrics were shared:
  - 12.186 ns/d/walker on 8 GPUs
  - 11.165 ns/d/walker on 4 GPUs
  - 8.812 ns/d/walker with 72 walkers
  - 10.846 ns/d/walker with 64 walkers

## Additional Notes
- The performance difference between the user's system and another system was noted, possibly due to differences in PLUMED settings.
- It was suggested to adjust the rate of exchange in PLUMED if possible.
- The user was advised to start simulations with the current setup while further optimizations were explored.

## Conclusion
The user was able to optimize the number of walkers and achieve better performance on multi-GPU machines. Further adjustments in PLUMED settings may be required for additional performance gains.
```
---

### 2022091542001808_Blog%20post%20%22Gromacs%20performance%20on%20different%20GPU%20types%22.md
# Ticket 2022091542001808

 ```markdown
# HPC Support Ticket: Blog post "Gromacs performance on different GPU types"

## Keywords
- GROMACS
- GPU benchmarks
- Performance
- Multi-GPU
- CPU cores
- MPI settings
- PME
- Thread-MPI
- OpenMP
- Inter-node communication

## Summary
A user from Universiteit Leiden reached out regarding a blog post on GROMACS performance on different GPU types. The user had questions about the benchmarking process, including the number of GPUs used, the number of times each benchmark was run, and specific settings for CPU and MPI runs.

## User Questions and Responses
1. **Single vs. Multiple GPUs:**
   - **User Question:** Did you run all benchmarks on a single GPU or also on multiple GPUs?
   - **HPC Admin Response:** All benchmarks were run on a single GPU. Previous results showed that a multiple GPU setup can lead to performance decrease for small systems. For large systems, a multiple GPU setup can give performance improvements but should be tested individually.

2. **Number of Runs:**
   - **User Question:** How many times did you run each benchmark?
   - **HPC Admin Response:** All benchmarks ran once. There are small fluctuations (less than 10%) between runs and these fluctuations can also be observed between different nodes of the same hardware.

3. **Data for System 4:**
   - **User Question:** There was no link to the data used for system_4 in the blog post. Would it be possible to share the data with me so that I can also run this particular benchmark?
   - **HPC Admin Response:** Unfortunately, the data for system 4 cannot be shared as it is taken from ongoing research and has not yet been published.

4. **Running Time for Systems 5 and 6:**
   - **User Question:** What was the running time for systems 5 and 6 on the nodes with RTX2080TIs?
   - **HPC Admin Response:** The benchmark of system 5 on an RTX2080TI took 26 minutes and system 6 ran on an RTX2080TI for 51 minutes.

5. **CPU Core Dependence:**
   - **HPC Admin Response:** The benchmarks were run using increasing numbers of CPU cores (1-32) and found that, despite offloading all possible calculations to the GPU, the overall performance is greatly depending on the available number of CPU cores; some parts of the simulation are still carried out on the CPU.

6. **MPI and CPU Settings:**
   - **User Question:** Would it be possible to share the settings that you used for “-npme $npme -ntmpi $ntmpi -ntomp $ntomp” and the settings for the MPI run on the Meggie cluster?
   - **HPC Admin Response:** The settings for MPI runs on Meggie and the settings for the Icelake node from the blogpost are not easily shared. However, a benchmark script was provided that automatically runs different settings for ntmpi, ntomp, and npme and will also set the number of processes and the number of processes per node.

7. **Difference in Simulation Steps:**
   - **User Question:** Why did you use 30000 steps for the CPU benchmarks compared to 200000 steps for the GPU benchmark?
   - **HPC Admin Response:** 200,000 steps were chosen for the benchmarks on GPU to ensure a walltime of at least 60s.

## Additional Information
- The user was directed to another set of benchmarks available from HECBioSim, which used similar files to run GROMACS benchmarks on various HPC systems in the UK.
- The user was advised to replace "gmx" with "gmx_mpi" and remove the mdrun setting "-ntmpi" for multi-node GROMACS runs.

## Conclusion
The user's questions were addressed, and additional resources and scripts were provided to aid in their benchmarking efforts. The user was also informed about the importance of testing runtime parameters for multi-node GROMACS runs to avoid performance loss due to inter-node communication.
```
---

### 2022031142000631_Gromacs5.1.2%20-%20Jobs%20auf%20Emmy%20%5Bexzi000h%5D.md
# Ticket 2022031142000631

 ```markdown
# HPC-Support Ticket: Gromacs 5.1.2 Jobs on Emmy

## Keywords
- Gromacs
- Emmy
- GPU
- Performance
- Benchmark
- Verification
- Consistency

## Summary
A user was running Gromacs 5.1.2 jobs on Emmy for a long-running project. The HPC admin inquired about the reason for using an outdated version and suggested switching to newer versions for better performance on GPUs. The user explained the need for consistency in the final verification runs but was interested in benchmarking newer versions.

## Problem
- User running outdated Gromacs version (5.1.2) on Emmy.
- Potential performance improvements with newer Gromacs versions on GPUs.

## Solution
- User agreed to continue with Gromacs 5.1.2 for consistency but provided a .tpr file for benchmarking.
- HPC admin conducted benchmarks on various GPUs (A40, A100, RTX3080, RTX2080Ti) using Gromacs 2021.5 and 2022.0.
- Results showed significant performance improvements on GPUs compared to Emmy.

## Benchmark Results
- **RTX2080Ti**: 199.5 ns/day (Gromacs 2021.5), 211.0 ns/day (Gromacs 2022.0)
- **RTX3080**: 220.5 ns/day (Gromacs 2021.5), 215.1 ns/day (Gromacs 2022.0)
- **A100**: 317.4 ns/day (Gromacs 2021.5), 317.9 ns/day (Gromacs 2022.0)
- **A40**: 323.7 ns/day (Gromacs 2021.5), 326.3 ns/day (Gromacs 2022.0)

## Additional Notes
- Setting specific environment variables further improved performance.
- Recommendation to switch future projects to GPUs for better performance.

## Conclusion
The user was informed about the significant performance benefits of using newer Gromacs versions on GPUs. The HPC admin offered assistance for future projects and transitions to GPU-based simulations.
```
---

### 2023110242001531_Gromacs%20Job%20on%20Alex%20only%20uses%20one%20GPU%20%5Bk101ee11%5D.md
# Ticket 2023110242001531

 # HPC Support Ticket: Gromacs Job on Alex only uses one GPU

## Keywords
- Gromacs
- GPU allocation
- Slurm script
- Benchmarking
- Performance optimization
- Environment variables

## Problem
- User's Gromacs job on Alex was only utilizing one of the allocated two GPUs.
- Inefficient use of multi-GPU setup leading to potential performance decrease.

## Root Cause
- Incorrect GPU allocation in the Slurm script.
- Lack of explicit flags in Gromacs to efficiently run on more than one GPU.

## Solution
- Correct the Slurm script for proper GPU allocation using `#SBATCH --gres=gpu:a100:2`.
- Use explicit flags in Gromacs to distribute ranks across GPUs:
  ```bash
  gmx mdrun -s step7.tpr -ntmpi 4 -ntomp 8 -npme 1 -nb gpu -pme gpu -bonded gpu -update cpu -pin on -pinstride 1
  ```
- Set environment variables for performance optimization:
  ```bash
  export GMX_GPU_PME_DECOMPOSITION=1
  export GMX_USE_GPU_BUFFER_OPS=1
  export GMX_DISABLE_GPU_TIMING=1
  export GMX_ENABLE_DIRECT_GPU_COMM=1
  export GMX_CUDA_GRAPH=true
  export GMX_ENABLE_STAGED_GPU_TO_CPU_PMEPP_COMM=1
  ```

## Benchmarking Results
- **2x A40**:
  - Without environment variables: 26.4 ns/day
  - With environment variables: 28.4 ns/day
  - With graph: 28.4 ns/day
- **2x A100**:
  - Without environment variables: 44.5 ns/day
  - With environment variables: 49.7 ns/day
  - With graph: 50.3 ns/day

## General Learnings
- Proper GPU allocation and explicit flags are crucial for efficient multi-GPU usage in Gromacs.
- Environment variables can provide small but significant performance improvements.
- Benchmarking different GPU setups can help optimize performance for specific systems.
- Users can monitor job performance using the ClusterCockpit monitoring system.

## Additional Resources
- ClusterCockpit monitoring system: [https://monitoring.nhr.fau.de/](https://monitoring.nhr.fau.de/)
- FAUbox for file sharing with HPC Admins.
---

### 42341992_gromacs%205%20on%20woody.tinyblue.md
# Ticket 42341992

 # HPC Support Ticket: gromacs 5 on woody.tinyblue

## Keywords
- gromacs 5.0.4-mkl
- Module ERROR
- mpiexec.static Error
- Missing file error

## Problem Description
- **Module ERROR**: Missing close-brace in the module file for gromacs 5.0.4-mkl.
- **mpiexec.static Error**: Argument -n specifies 192 processors, but the config file only matched 181.
- **Missing file error**: Cannot access specified file path.

## Root Cause
- The module file for gromacs 5.0.4-mkl had a syntax error (missing close-brace).
- The mpiexec.static error indicates a mismatch between the specified number of processors and the available configuration.
- The missing file error suggests that the specified file path does not exist.

## Solution
- **Module ERROR**: The bug in the module file has been fixed recently. New jobs should not suffer from this problem anymore.
- **mpiexec.static Error**: Ensure that the number of processors specified matches the available configuration.
- **Missing file error**: Verify the file path and ensure that the file exists.

## General Learnings
- Syntax errors in module files can cause module loading issues.
- Mismatches in processor specifications can lead to mpiexec errors.
- Always check file paths and ensure the existence of files to avoid missing file errors.

## Actions Taken
- The HPC Admin confirmed that the module file bug has been fixed.
- No specific actions mentioned for the mpiexec.static error or the missing file error.

## Next Steps
- Users should retry running their simulations to confirm the fix for the module error.
- If the mpiexec.static error or missing file error persists, further investigation is needed.
---

### 2021110442002085_Gromacs-Jobs%20auf%20TinyGPU%202x%20rtx2080ti%20%5Bbccb006h%5D.md
# Ticket 2021110442002085

 # HPC Support Ticket: Gromacs-Jobs auf TinyGPU 2x RTX2080TI

## Keywords
- Gromacs
- Multi-GPU
- Performance
- Benchmarking
- TinyGPU
- RTX2080TI

## Summary
A user was running Gromacs jobs on TinyGPU with 2x RTX2080TI GPUs. The HPC Admin noticed this and inquired about the performance, as previous tests had shown poor results with 2 GPUs. The user provided performance data showing better scaling with 2 GPUs for their specific simulations.

## Root Cause
- The user was running Gromacs jobs with 2 GPUs, which the HPC Admin had previously found to be suboptimal in some cases.

## Solution
- The user provided performance data showing that for their specific simulations, using 2 GPUs resulted in better performance (23 ns/day for 1 GPU vs. 45 ns/day for 2 GPUs).
- The HPC Admin acknowledged the user's findings and approved the use of 2 GPUs for their jobs.

## General Learnings
- Performance of multi-GPU jobs can vary depending on the specific simulation and software version.
- Benchmarking with the specific simulation parameters is important to determine the optimal GPU configuration.
- Communication between users and HPC Admins can help resolve performance concerns and optimize resource usage.

## References
- [Multi-GPU Gromacs Jobs on TinyGPU](https://hpc.fau.de/2021/06/18/multi-gpu-gromacs-jobs-on-tinygpu/)
---

### 2021052142001636_Gromacs-Jobs%20auf%20TinyGPU%20%5Bbcpc000h%5D.md
# Ticket 2021052142001636

 ```markdown
# HPC-Support Ticket: Gromacs-Jobs auf TinyGPU

## Problem
- User is running Gromacs jobs on TinyGPU cluster using multiple GPUs.
- Assumption that using more than one GPU would result in performance gain.

## Root Cause
- Gromacs does not scale well with multiple GPUs.
- User inherited job settings from a predecessor without optimization.

## Solution
- HPC Admin ran benchmarks with different Gromacs versions and GPU configurations.
- Found that using a newer Gromacs version (2021.1) on a single GPU produced similar performance to using four GPUs with an older version (2019.0).
- Recommended using the newer Gromacs version and optimizing program flags.
- Suggested using `$TMPDIR` for temporary files to avoid network overhead.

## Key Learnings
- Always test and optimize job settings instead of inheriting them.
- Newer software versions can provide significant performance improvements.
- Gromacs does not scale well with multiple GPUs; using a single GPU can be more efficient.
- Using `$TMPDIR` for temporary files can improve performance by reducing network access.

## Actions Taken
- HPC Admin provided detailed benchmark results and recommendations.
- User agreed to use the optimized settings and gave permission to include the case in the NHR Newsletter.
- HPC Admin reviewed the user's submit script and provided feedback on using `$TMPDIR`.

## Additional Notes
- The user is a pharmacist with limited scripting knowledge.
- HPC Admin offered ongoing support for scripting and optimization.
```
---

### 2023022442002275_GROMACS%20%2B%20PLUMED.md
# Ticket 2023022442002275

 # HPC-Support Ticket: GROMACS + PLUMED

## Keywords
- GROMACS
- PLUMED
- Patching
- Version Compatibility
- Installation
- Testing

## Summary
A user requested the installation of GROMACS version 2022.5 patched with PLUMED 2.8.2 on the HPC system "alex." The ticket involved multiple iterations to identify the correct versions and compatibility issues.

## Root Cause
- The user initially requested a non-released version of PLUMED (2.8.2).
- There was a misunderstanding regarding the compatibility of GROMACS versions with PLUMED 2.8.1.

## Solution
- The HPC Admin installed GROMACS 2022.3 patched with PLUMED 2.8.1.
- The user was advised to test the installation thoroughly.

## Steps Taken
1. **Initial Request**: User requested GROMACS 2022.5 with PLUMED 2.8.2.
2. **Admin Response**: Informed the user that PLUMED 2.8.2 is not released.
3. **User Clarification**: Requested GROMACS 2022.5 with PLUMED 2.8.1.
4. **Compatibility Check**: Admin identified that GROMACS 2022.5 is not supported by PLUMED 2.8.1.
5. **Alternative Version**: User requested GROMACS 2022.3 with PLUMED 2.8.1.
6. **Installation**: Admin installed GROMACS 2022.3 with PLUMED 2.8.1 and advised the user to test it.

## Lessons Learned
- Always check the release status and compatibility of software versions before requesting installations.
- Clear communication and iterative problem-solving are essential for resolving version compatibility issues.
- Thorough testing is required after automated installations to ensure functionality.

## Conclusion
The ticket was resolved by installing a compatible version of GROMACS patched with PLUMED. The user was advised to test the installation and report any issues.
---

### 2024102242004483_Gromacs-Job%20auf%20Alex%20nutzt%20nur%204%20von%208%20GPUs%20%5Be102ef11%5D.md
# Ticket 2024102242004483

 # HPC Support Ticket: Gromacs Job Utilizing Only 4 of 8 GPUs

## Keywords
- Gromacs
- GPU utilization
- Job script configuration
- Multinode GPU computation
- Performance optimization

## Problem Description
- A Gromacs job allocated 8 GPUs but utilized only 4.
- The issue was due to an incorrectly set flag in the Gromacs command: `-ntmpi 4` which starts 4 ranks, allowing only 4 GPUs to be addressed.

## Root Cause
- Incorrect `-ntmpi` flag setting in the Gromacs command.

## Solution
- Adjust the `-ntmpi` flag to match the number of GPUs allocated.
  - For 8 GPUs, use `-ntmpi 8`.
  - If only 4 GPUs are needed, adjust the SBATCH line accordingly: `#SBATCH --gres=gpu:a100:4`.

## Additional Information
- Multinode GPU computation is possible but may not significantly improve performance.
- The HPC Admins are working on compiling an optimized version of Gromacs for multinode GPU usage.

## Job Script Adjustment for Multinode GPU
- No specific instructions provided in the conversation, but it is implied that adjusting the `-ntmpi` flag and SBATCH directives is necessary.

## Performance Considerations
- Using multiple nodes may not always result in better performance compared to using a single node.
- Performance optimization for multinode GPU computation is ongoing.

## Conclusion
- Ensure the `-ntmpi` flag matches the number of GPUs allocated.
- Adjust SBATCH directives to reflect the actual number of GPUs required.
- Multinode GPU computation is possible but may require further optimization for significant performance gains.

---

This documentation aims to help support employees troubleshoot similar issues related to GPU utilization in Gromacs jobs.
---

### 42323177_gromacs%205.md
# Ticket 42323177

 # HPC Support Ticket: Gromacs 5 Installation and Usage

## Keywords
- Gromacs 5
- Cluster installation
- GPU support
- Module availability
- Testing and benchmarking

## Summary
A user inquired about the availability of Gromacs 5 on the cluster for a new project. The HPC Admin provided information on the test installation of Gromacs 5.0.4 on LiMa and Emmy clusters, including details on GPU support and how to request GPU nodes.

## Root Cause
- User needed to know if Gromacs 5 was installed on the cluster.

## Solution
- Gromacs 5.0.4 is available on LiMa and Emmy clusters.
- Modules available: `gromacs/5.0.4-mkl-sse4.1`, `gromacs/5.0.4-mkl-IVB`, and `gromacs/5.0.4-mkl-IVB-CUDA50`.
- GPU support is available on Emmy with specific nodes having 1 or 2 GPUs.
- To request GPU nodes, use `:k20m`, `:k20m1x`, or `:k20m2x` in addition to `:ppn=40`.
- Jobs requesting GPUs are automatically placed in the "accel" queue.
- Users are advised to test the new version thoroughly before production runs and to check if GPUs provide acceleration.

## General Learnings
- Always check for the availability of new software versions on the cluster.
- Understand the specific modules and their features, such as GPU support.
- Follow the correct procedures to request specific resources like GPUs.
- Conduct thorough testing before using new software versions for production runs.

## Additional Notes
- Gromacs 5.0.4 is still in the testing phase and may not be available on all clusters (e.g., Woody and Tiny).
- Benchmark tests with Gromacs 5.0.2 showed mixed performance compared to the previous version.
---

### 2018032742002312_Gromacs%202018%20auf%20Emmy%20f%C3%83%C2%BCr%20GPU-Nutzung.md
# Ticket 2018032742002312

 # HPC-Support Ticket Conversation Analysis

## Keywords
- Gromacs 2018
- GPU-Nutzung
- Emmy-Cluster
- CUDA
- MPI
- Segmentation Fault
- NVidia-Treiber
- Sicherheitsupdates

## What Can Be Learned

### User Inquiries
- User requested information on the benefits of using Gromacs 2018 with GPU support on the Emmy-Cluster.
- User reported issues with GPU recognition and segmentation faults in Gromacs 2018.1.

### HPC Admin Responses
- HPC Admins provided ungetestete modules for Gromacs 2018.1 with GPU support.
- HPC Admins suggested using specific parameters for optimal performance with GPUs.
- HPC Admins identified and fixed issues related to GPU recognition and segmentation faults.
- HPC Admins reported problems with a buggy NVidia-Treiber (390.30) causing issues with jobs.

### Solutions and Recommendations
- For GPU recognition issues, ensure that the correct GPU support is compiled into the Gromacs module.
- Use the following parameters for optimal performance on the Emmy-Cluster: `-nb gpu -ntmpi 4 -ntomp 10`.
- If encountering segmentation faults, try restarting the job or check for recent updates to the NVidia-Treiber.
- HPC Admins recommended using the threaded/tmpi version of Gromacs (`gmx mdrun`) without `mpirun` for better performance.

### Root Causes and Solutions
- **GPU Recognition Issue**: The problem was due to the lack of support for older Kepler-Generation GPUs in the initial build. Solution: Ensure proper compilation with support for the required GPUs.
- **Segmentation Fault**: The issue was likely caused by a buggy NVidia-Treiber (390.30). Solution: Update the NVidia-Treiber to a stable version.

### Performance Benchmarks
- The user reported a 3.5% speed increase with Gromacs 2018 without GPU support compared to version 5.1.2.
- The best performance with GPUs was achieved on a k20m2x-Node with parameters `-nb gpu -ntmpi 4 -ntomp 10`.
- Multi-node performance was not significantly better than single-node performance.

### General Recommendations
- Always test new software versions and report any issues to the HPC Admins.
- Keep software and drivers up to date to avoid compatibility issues.
- Benchmark different configurations to find the optimal performance settings for specific workloads.

This analysis provides a summary of the key points and solutions from the HPC-Support ticket conversation, which can be used as a reference for future support cases.
---

### 2023072142001209_Fw%3A%20Benchmarks%20Fritz%20-%20bccb004h%20-%20sehr%20gro%C3%83%C2%9Fe%20Gromacs-Systeme%20ohne%20P.md
# Ticket 2023072142001209

 # HPC Support Ticket: Benchmarks Fritz - bccb004h - sehr große Gromacs-Systeme ohne PME

## Keywords
- Benchmarks
- Gromacs
- Fritz
- PME
- tpr-Dateien
- FAUbox
- Performance
- Skalierung
- Knoten
- ns/day
- -ntomp
- -dlb
- Simulationsparameter
- Effizienz

## Summary
The user requested benchmarks for large Gromacs systems without PME on the Fritz cluster. The HPC Admin provided benchmark results and guidance on scaling and performance.

## Problem
- User needed benchmarks for Gromacs systems with 0.5 million and 1.8 million particles.
- Systems were created with Gromacs 2021.

## Solution
- HPC Admin ran benchmarks using Gromacs Version 2021.5-gcc11.2.0-impi-mkl on 1, 2, and 3 Fritz nodes with "-dlb yes".
- Provided performance results in ns/day for different systems and node configurations.
- Advised on the trade-off between performance and inter-node communication overhead.
- Ran additional benchmarks with updated simulation parameters and 5 nodes.

## Key Takeaways
- Benchmarks are essential for optimizing the performance of large simulations.
- Increasing the number of nodes can improve performance but also increases communication overhead.
- Adjusting simulation parameters and the number of nodes can help achieve the desired performance.
- The HPC Admin can assist with running benchmarks and interpreting results.

## Follow-up
- User will run simulations on their account once access is granted.
- Additional benchmarks were provided for updated simulation parameters and 5 nodes.

## Conclusion
The HPC Admin successfully assisted the user with benchmarking and provided valuable insights into optimizing the performance of large Gromacs simulations on the Fritz cluster.
---

### 2023030342001536_h%C3%83%C2%A4ngende%20Gromacs-Jobs%20auf%20Alex%20-%20b118bb14.md
# Ticket 2023030342001536

 # HPC Support Ticket: Hängende Gromacs-Jobs auf Alex

## Problem Description
Gromacs jobs on Alex are hanging after 8-16 hours, causing the jobs to stop writing to the log file and resulting in a deadlock. This issue is suspected to be a bug in Gromacs, specifically in the routines `dd_sendrecv2_rvec` and `dd_move_x` or `dd_move_x_specat`.

## Root Cause
The root cause of the problem is a suspected bug in Gromacs, which is triggered by specific input behavior. The bug causes the jobs to hang and stop writing to the log file, leading to a deadlock in the `sendrecv` routine.

## Solution
To mitigate the issue, the following steps were taken:

1. **Reduce Job Runtime**: Reduce the requested job runtime to half of the original time (e.g., from 24 hours to 12 hours) to minimize the impact of hanging jobs on the compute time quota.

2. **Automatic Restarts**: Implement automatic restarts for the jobs. An example script for automatic restarts can be found [here](https://hpc.fau.de/systems-services/documentation-instructions/special-applications-and-tips-tricks/gromacs/#collapse_2).

3. **Monitoring Script**: Add a monitoring script to the job script to automatically kill the Gromacs process if it has not written to the log file for a specified period (e.g., 5 minutes). The monitoring script is as follows:

```bash
GMX_PID=$!
echo GMX_PID=$GMX_PID
while true; do
    sleep 30
    LAST_OUTPUT=$(stat -c %Y npt.log)
    NOW=$(date +%s)
    AGE=$(( $NOW - $LAST_OUTPUT ))
    if [ $AGE -gt 300 ]; then
        echo "TOO OLD: $AGE"
        kill $GMX_PID
        break
    else
        echo "AGE=$AGE; continuing"
    fi
done &
wait $GMX_PID
echo "finished or killed"
```

4. **Adjust Gromacs Command**: Modify the Gromacs command to use `-ntmpi 1 -ntomp 16` to potentially avoid the bug, although this may result in a slight performance loss.

## Additional Information
- The issue was observed across different GPU models, and it is not specific to a particular model.
- The problem was reported by multiple users on different HPC systems, suggesting a widespread bug in Gromacs.
- The HPC Admins provided support and guidance throughout the troubleshooting process.

## Conclusion
The hanging jobs issue in Gromacs is a suspected bug that can be mitigated by reducing job runtime, implementing automatic restarts, adding a monitoring script, and adjusting the Gromacs command. Further investigation into the bug is ongoing.
---

### 2019111942003408_Multi-GPU%20Gromacs.md
# Ticket 2019111942003408

 # Multi-GPU Gromacs Configuration Issue

## Keywords
- Multi-GPU
- Gromacs
- MPI
- OpenMP
- GPU utilization
- Job configuration

## Problem
- User's multi-GPU jobs were not utilizing all available GPUs.
- The jobs were configured to request 8 cores and 2 GPUs but only one GPU was being used.

## Root Cause
- Incorrect Gromacs command configuration: `-nt 8` resulted in 1x MPI + 8x OpenMP, limiting GPU usage to one per MPI process.

## Solution
- Adjust the Gromacs command to properly distribute MPI and OpenMP processes to utilize multiple GPUs.
  - Example configurations:
    ```sh
    gmx mdrun -ntmpi 2 -ntomp 4 -npme 1 ...
    ```
    or
    ```sh
    gmx mdrun -ntmpi 4 -ntomp 2 -npme 1 ...
    ```

## General Learning
- Ensure proper configuration of MPI and OpenMP processes to maximize GPU utilization in multi-GPU jobs.
- Understand the relationship between MPI processes and GPU usage in Gromacs.

## References
- HPC Services, Friedrich-Alexander-Universitaet Erlangen-Nuernberg
- Regionales RechenZentrum Erlangen (RRZE)
- [HPC Support](mailto:support-hpc@fau.de)
- [RRZE HPC Website](http://www.hpc.rrze.fau.de/)
---

### 2020021442000765_Gromacs-Jobs%20auf%20TinyGPU%20-%20bccb004h.md
# Ticket 2020021442000765

 # HPC Support Ticket: Gromacs Jobs on TinyGPU

## Keywords
- Gromacs
- TinyGPU
- PPN
- MPI
- OpenMPI
- GPU utilization
- Job optimization

## Problem
- User's jobs on TinyGPU implicitly request 2 GPUs with `:ppn=8`.
- Gromacs is configured with `-nt 8`, leading to 1 MPI thread and 8 OpenMPI threads.
- Only one GPU is utilized, leaving the second GPU idle.

## Root Cause
- Incorrect configuration of Gromacs parameters leading to inefficient GPU utilization.

## Solution
- **Option A:** Reduce resource allocation to `:ppn=4` to allow more jobs to run concurrently on the cluster.
- **Option B:** Optimize Gromacs parameters to `-ntmpi 2 -ntomp 4 -npme 1` to utilize both GPUs effectively and potentially speed up the job.

## General Learning
- Ensure proper configuration of job parameters to optimize resource utilization.
- Check job logs (e.g., `md.log`) for indications of resource usage.
- Adjusting parameters can lead to better performance and more efficient use of cluster resources.

## References
- HPC Services, Friedrich-Alexander-Universitaet Erlangen-Nuernberg
- Regionales RechenZentrum Erlangen (RRZE)
- [HPC Support](mailto:support-hpc@fau.de)
- [RRZE HPC Website](http://www.hpc.rrze.fau.de/)
---

### 2021061642001519_Gromacs-Jobs%20auf%20TinyGPU%20%5Bbccb006h%5D.md
# Ticket 2021061642001519

 # HPC Support Ticket: Gromacs-Jobs auf TinyGPU

## Keywords
- Gromacs
- TinyGPU
- GPU allocation
- Performance optimization
- Umbrella simulations
- Sub-jobs
- Thread pinning

## Summary
An HPC admin noticed that a user was repeatedly requesting four GPUs for Gromacs jobs on TinyGPU. The admin reached out to the user to offer assistance in optimizing the job parameters, as using four GPUs might not always be the best choice for Gromacs simulations.

## User's Explanation
- The user intentionally requested four GPUs to run multiple sub-jobs, each on a different GPU.
- The goal was to perform several Umbrella simulations for different systems, distributing the individual window simulations across the four GPUs.
- The user took a whole node (four GPUs) to pin threads as desired, achieving high performance (~5000-7000 ns/day).
- The user provided Python and shell scripts for coordinating the job distribution.

## HPC Admin's Response
- The admin acknowledged the user's explanation and confirmed that the jobs were not causing any issues on TinyGPU.
- The admin appreciated the user's detailed response and did not have further concerns.

## Lessons Learned
- **GPU Allocation**: Users may request multiple GPUs for specific reasons, such as running multiple sub-jobs simultaneously.
- **Performance Optimization**: Pinning threads and distributing jobs across GPUs can significantly improve performance for certain workflows.
- **Communication**: Clear communication between users and HPC admins can help resolve concerns and optimize job parameters.

## Root Cause of the Problem
- The admin's initial concern was based on monitoring data showing repeated requests for four GPUs, which is not always optimal for Gromacs simulations.

## Solution
- The user provided a valid explanation for the GPU allocation, and the admin confirmed that the jobs were not causing any issues. No further action was required.

## Follow-up
- Users should be encouraged to provide detailed explanations for their job configurations when contacted by HPC admins.
- HPC admins should continue to monitor job allocations and offer assistance for optimization when necessary.
---

### 2023060142001123_Help%20with%20performance%20on%20the%20alex%20cluster%20-%20b119ee10%20%28SimMediSoft%29.md
# Ticket 2023060142001123

 ```markdown
# HPC-Support Ticket: Help with performance on the alex cluster - Gromacs Simulation

## Summary
User requested help with optimizing Gromacs simulation performance on the alex cluster. The simulation involved a system with approximately 2.6 million atoms for 100 ns. Initial performance was 11.808 ns/day using 8 GPUs.

## Key Points Learned

### Performance Optimization
- **Environment Variables**: Several environment variables were recommended to optimize Gromacs performance:
  ```bash
  export GMX_GPU_PME_DECOMPOSITION=1
  export GMX_USE_GPU_BUFFER_OPS=1
  export GMX_DISABLE_GPU_TIMING=1
  export GMX_ENABLE_DIRECT_GPU_COMM=1
  export GMX_GPU_PME_PP_COMMS=true
  export GMX_GPU_DD_COMMS=true
  ```
- **Gromacs Version**: Gromacs 2023 was used with the module `gromacs/2023.0-gcc11.2.0-mkl-cuda`.
- **Optimal GPU Configuration**: Best performance was achieved with 4 A40 GPUs.
- **Gromacs Call**:
  ```bash
  gmx mdrun -s <name-of-file>.tpr -ntmpi 8 -ntomp 8 -npme 1 -pin on -pinstride 1 -nb gpu -bonded gpu -pme gpu -update gpu
  ```

### Slurm Job Submission
- **Slurm Parameters**: The `--ntasks` option in Slurm should not be modified for Gromacs simulations.
- **MPS Server**: Only needed for multiple simulations running in parallel, such as replica exchange or multiple walkers.

### Storage Quota
- **Quota Increase**: User's quota was increased to 20 TB to address storage issues.
- **File Transfer**: For large files, alternative methods to SFTP should be considered.

### Zoom Meeting
- **Support Session**: A Zoom meeting was scheduled to provide further support and answer specific questions about Gromacs on GPUs.
- **Slides**: Slides about Gromacs use on GPUs were shared during the meeting.

## Root Cause of Performance Issue
- Suboptimal configuration of environment variables and Gromacs parameters.

## Solution
- Use the recommended environment variables and Gromacs call configuration.
- Optimize GPU usage based on the provided benchmarks.
- Increase storage quota to handle large simulation files.

## Closure
The ticket was closed after providing detailed optimization steps and scheduling a support session to address further questions.
```
---

### 2016060742000681_mdrun_mpi%20with%20gromacs%204.6.6-mkl%20on%20tinyblue.md
# Ticket 2016060742000681

 ```markdown
# HPC-Support Ticket: mdrun_mpi with gromacs 4.6.6-mkl on tinyblue

## Keywords
- gromacs 4.6.6
- mdrun
- mdrun_mpi
- tinyblue
- module file error

## Problem Description
User encountered issues starting gromacs 4.6.6 on tinyblue. The binaries `mdrun` and `mdrun_mpi` were not found, despite gromacs5 working correctly.

## Root Cause
There was an error in the module file for TinyBlue and gromacs/4.6.6-mkl.

## Solution
The HPC Admin corrected the error in the module file, allowing the binaries to be found correctly.

## Lessons Learned
- Ensure module files are correctly configured to avoid issues with binary paths.
- Verify module configurations when users report missing binaries.

## Ticket Status
Closed successfully.
```
---

### 2020062442001005_Gromacs%20Jobs%20on%20Emmy%20%28bccc018h%2C%201316540%2C%201316541%2C%20...%29.md
# Ticket 2020062442001005

 # HPC Support Ticket: Gromacs Jobs Overloading Nodes

## Keywords
- Gromacs
- Job overloading
- Computational nodes
- mpiexec
- mdrun
- mdrun_mpi
- Parallelization

## Problem
- User's Gromacs jobs were overloading computational nodes.
- Each node has 20 physical cores, but the jobs were running about 740 processes on a single node.

## Root Cause
- Incorrect command used for parallelization: `mpiexec gmx mdrun`

## Solution
- Use the correct command for parallelizing Gromacs simulations across multiple nodes:
  ```
  mpiexec mdrun_mpi
  ```
- Refer to the official documentation for running Gromacs on the cluster: [Gromacs Documentation](https://www.anleitungen.rrze.fau.de/hpc/special-applications-and-tips-tricks/gromacs/)

## General Lessons
- Ensure that jobs are properly parallelized to avoid overloading nodes.
- Use the correct commands and syntax for running specific applications on the HPC cluster.
- Consult the official documentation for application-specific guidelines.

## Actions Taken by HPC Admins
- Terminated the overloading jobs.
- Provided the correct command and documentation link to the user.
---

### 2021110442001942_Gromacs-Jobs%20auf%20TinyGPU%202x%20rtx2080ti%20%5Bbcpc000h%5D.md
# Ticket 2021110442001942

 # HPC Support Ticket: Gromacs-Jobs auf TinyGPU 2x rtx2080ti

## Keywords
- Gromacs
- TinyGPU
- rtx2080ti
- SLURM
- GPU allocation
- Performance optimization

## Problem
- User requested 2 GPUs but only used 1 GPU in their Gromacs job.
- Incorrect program flags in the Gromacs command led to inefficient resource usage.

## Root Cause
- The Gromacs command (`gmx mdrun -v -ntmpi 1 -ntomp 8 -pme gpu -nb gpu -bonded gpu -update gpu -pin on -pinstride 1 -deffnm $TPR -cpi $SLURM_SUBMIT_DIR/$TPR`) was configured to use only 1 GPU, despite the SLURM script requesting 2 GPUs (`#SBATCH --gres=gpu:rtx2080ti:2`).

## Solution
- For optimal performance, it is recommended to use only 1 GPU for Gromacs jobs.
- If using 2 GPUs, the Gromacs command should be modified to include `-ntmpi 2` and `-npme 1`.
- Example command for 1 GPU: `gmx mdrun -s -ntmpi 1 -ntomp 32 -pme gpu -bonded gpu -update gpu -pin on -pinstride 1 -v`.
- To reduce waiting times, use `--gres=gpu:1` in the SLURM script to allow automatic selection of available GPUs.

## Benchmark Results
- 1 GPU:
  - RTX2080TI: 228 ns/day
  - RTX3080: 269 ns/day
- 2 GPUs:
  - Performance was generally lower compared to 1 GPU.

## Additional Tips
- Using multiple GPUs with Gromacs may not always result in better performance.
- Refer to [Multi-GPU Gromacs Jobs on TinyGPU](https://hpc.fau.de/2021/06/18/multi-gpu-gromacs-jobs-on-tinygpu/) for more information.

## Conclusion
- The user was advised to stick with 1 GPU for their Gromacs jobs to achieve the best performance.
- The HPC Admin provided benchmark results and recommended SLURM script modifications to optimize resource allocation and reduce waiting times.
---

### 2024052242003074_Availability%20of%20CHARMM36%20forcefield%20in%20GROMACS%20-%20n102af11.md
# Ticket 2024052242003074

 ```markdown
# HPC Support Ticket: Availability of CHARMM36 Forcefield in GROMACS

## Subject
Availability of CHARMM36 or the additive CHARMM36 forcefield in any of the GROMACS module versions on the Alex or Fritz clusters.

## User Inquiry
- User inquired about the availability of the CHARMM36 forcefield in GROMACS on the Alex or Fritz clusters.
- User did not find the forcefield listed in the directories.

## HPC Admin Response
- CHARMM36 forcefield is not installed by default via Spack.
- User advised to download the CHARMM36 forcefield files from the official website and unpack them into a directory.
- User instructed to provide the absolute path in the forcefield.itp file.

## Key Points Learned
- **Forcefield Availability**: CHARMM36 forcefield is not installed by default in GROMACS via Spack.
- **Manual Installation**: Users can manually download and install the CHARMM36 forcefield.
- **File Upload Issues**: User faced issues with uploading files using FAUbox and GigaMove.
- **Simulation Setup**: User provided simulation files for assistance.
- **Parameter Generation**: User encountered errors related to missing parameters for ligands, which require generation before setting up the MD simulation.

## Solutions Provided
- **Manual Download and Installation**: User guided to download and extract CHARMM36 forcefield files and add them to the working directory.
- **Command Line Example**: Provided command line example for running GROMACS with CHARMM36 forcefield.
- **File Upload Assistance**: User assisted with uploading files using FAUbox and GigaMove.
- **Parameter Generation**: User advised to generate parameters for ligands before setting up the MD simulation.

## Root Cause of Problems
- **Missing Parameters**: Errors occurred due to missing parameters for ligands in the simulation setup.
- **File Upload Issues**: User faced difficulties uploading entire folders, leading to clumsy directory structures.

## Additional Notes
- **Account Extension**: User's account was extended upon request.
- **24/7 Service**: HPC support does not offer 24/7 service; requests sent over the weekend are answered on Monday.

## References
- [CHARMM36 Forcefield Download](http://mackerell.umaryland.edu/charmm_ff.shtml#gromacs)
- [GROMACS BioExcel Forum](https://gromacs.bioexcel.eu/t/charmm36-forcefield-itp-vs-local-installation/8834)
- [FAUbox](https://faubox.rrze.uni-erlangen.de/)
- [GigaMove](https://gigamove.rwth-aachen.de/de)
```
---

### 2025031042003526_hpc%20support%20-%20gromacs%20simulation.md
# Ticket 2025031042003526

 # HPC Support Ticket: GROMACS Simulation Performance

## Keywords
- GROMACS 2021
- High parallelization
- Performance optimization
- Simulation scaling
- Filesystem performance

## Problem
- User needs to simulate an atomistic system of 200,000 atoms in CHARMM using GROMACS 2021.
- Requires 500 ns of simulation by Friday.
- Current performance on a single GPU is approximately 30 ns/day.

## Solution
- **Resource Allocation**: HPC Admin reserved 16 nodes on Fritz.
- **Command**: `salloc -N16 --time=1:0:0 --ntasks-per-node=72; srun gmx_mpi mdrun -dlb yes -s topol.tpr -maxh 0.5`
- **Expected Performance**: ~250 ns/day without extensive tuning.

## Test Results
- User ran multiple simulations with varying nodes and npme settings.
- Best performance achieved with 8 nodes and 96 npme, yielding 170 ns/day.

## Additional Issues
- Filesystem performance is slow, especially when deleting large amounts of data (11TB).

## Conclusion
- High parallelization on Fritz significantly improved simulation performance.
- Filesystem performance issues noted for further investigation.

## Future Reference
- For similar performance issues, consider allocating more nodes and optimizing npme settings.
- Monitor filesystem performance and address slowdowns as needed.
---

### 2024052742003609_Gromacs%20on%204%20GPU%20on%20Alex%20%5Bc102fd10%5D.md
# Ticket 2024052742003609

 # HPC Support Ticket: Gromacs on 4 GPU on Alex

## Keywords
- Gromacs
- GPU utilization
- Optimization
- .tpr file
- CPU-cluster
- Performance improvement

## Problem
- User increased GPU number from 2 to 4 for a Gromacs job.
- Low GPU utilization observed.

## Root Cause
- Inefficient use of GPU resources for the given simulation.

## Solution
- **Initial Assessment**: HPC Admin requested the .tpr file to provide optimized parameters.
- **Optimization Attempt**: HPC Admin tried to find GPU hardware to improve performance but was unsuccessful.
- **Alternative Solution**: Suggested switching to CPU-cluster Fritz for better performance.
  - Command used on Fritz: `gmx_mpi mdrun -npme 54 -ntomp 2 -dlb yes -s prod.tpr`
  - Performance achieved: 59.4 ns/day
- **SLURM Script for Fritz**:
  ```bash
  #!/bin/bash -l
  #
  #SBATCH --nodes=4
  #SBATCH --ntasks-per-node=72
  #SBATCH --time=24:00:00
  #SBATCH --export=NONE
  unset SLURM_EXPORT_ENV
  ```

## General Learnings
- Increasing GPU count does not always lead to better performance.
- Optimizing parameters based on the .tpr file can improve performance.
- Switching to a CPU-cluster can sometimes provide better performance for certain simulations.
- Proper SLURM script configuration is essential for efficient job submission.
---

### 2025021742004274_Regarding%20the%20available%20gromacs%20modules.md
# Ticket 2025021742004274

 # HPC Support Ticket Conversation: Gromacs Constant pH Version

## Keywords
- Gromacs
- Constant pH
- Module
- Spack
- Hidden Module
- Production Runs
- Publications

## Summary
A user inquired about the availability of a specific version of Gromacs software, known as "Constant pH Gromacs," on the HPC cluster. The user referred to a paper specifying this version.

## Problem
- User needed access to the "Constant pH Gromacs" version.
- The repository for this version mentioned it should not be used for production runs or publications, but the user provided evidence of its use in research.

## Solution
- HPC Admin informed the user about a hidden Gromacs-ConstantPH module available on the cluster.
- The user was instructed to load the module using specific commands:
  ```sh
  module load 000-all-spack-pkgs/0.19.1
  module load gromacs-constantph/main-gcc11.2.0-mkl-cuda-g5gqt7s
  ```
- The user was advised that these steps are necessary because the module is hidden.

## General Learnings
- Some software modules may be hidden and require specific steps to access.
- Users should be aware of the status of software versions they intend to use, especially regarding production runs and publications.
- HPC Admins can provide detailed instructions on accessing hidden modules.

## References
- [Gromacs Constant pH Repository](https://gitlab.com/gromacs-constantph/constantph)
- [Paper Specifying Constant pH Gromacs](https://pubs.acs.org/doi/10.1021/acs.jctc.2c00516)
- [Research Findings Using Constant pH Gromacs](https://doi.org/10.1101/2024.12.06.627182)
- [Research Findings Using Constant pH Gromacs](https://doi.org/10.1101/2024.11.27.625717)
---

### 2021090642003601_Gromacs-Job%20auf%20Meggie%20%5Bbcpc000h%5D.md
# Ticket 2021090642003601

 # HPC Support Ticket: Gromacs-Job auf Meggie

## Keywords
- Gromacs
- Meggie
- TinyGPU
- Performance
- Software Version
- Resource Optimization

## Problem
- User was running Gromacs jobs on Meggie with an outdated version of Gromacs.

## Root Cause
- The user was using old scripts that utilized an outdated version of Gromacs.

## Solution
- The user was advised to use the latest version of Gromacs for better performance.
- The user was also advised to consider moving simulations to TinyGPU for more efficient resource usage.

## Actions Taken
- HPC Admin informed the user about the outdated Gromacs version and provided links to articles on performance gains with newer versions and the benefits of using TinyGPU.
- The user updated their scripts to use the latest Gromacs version and moved their jobs to TinyGPU.

## Outcome
- The user successfully updated their jobs and moved them to TinyGPU, resulting in better performance and resource optimization.
- The ticket was closed as the user followed the suggested actions.

## General Learnings
- Always use the latest software versions for better performance.
- Consider moving jobs to more efficient hardware like TinyGPU for resource optimization.
- HPC Admins are available to assist with any questions or issues related to software updates and job migrations.

## References
- [Multi-GPU Gromacs Jobs on TinyGPU](https://hpc.fau.de/2021/06/18/multi-gpu-gromacs-jobs-on-tinygpu/)
- [Gromacs Shootout: Intel IceLake vs NVIDIA GPU](https://hpc.fau.de/2021/08/10/gromacs-shootout-intel-icelake-vs-nvidia-gpu/)
---

### 2025030742002604_Python%28%3F%29-Jobs%20on%20Alex%20%5Bb118bb16%5D.md
# Ticket 2025030742002604

 # HPC-Support Ticket: Python(?)-Jobs on Alex

## Keywords
- GPU utilization
- Gromacs
- MPI
- Slurm jobs
- Python input
- Job optimization

## Summary
The user was experiencing low GPU utilization (20-40%) in their Gromacs jobs. The issue was related to the use of an MPI version of Gromacs, which was CPU-limited for certain types of simulations.

## Root Cause
- The user was running multidir simulations with Gromacs, which required MPI for free energy calculations.
- The current CPU-per-GPU limit was set to 16, which was insufficient for the user's needs.
- The user was running numerous short jobs, which is not optimal for the batch system.

## Solution
- The user requested an increase in the CPU-per-GPU limit to improve GPU utilization.
- The user agreed to consolidate short jobs into a single script to reduce the load on the batch system.
- The user provided detailed information about the Gromacs version and Python input used in their jobs.

## General Learnings
- Always provide detailed information about the software and scripts used in HPC jobs.
- Consolidate short jobs into a single script to optimize batch system usage.
- GPU utilization can be improved by adjusting the CPU-per-GPU limit for certain types of simulations.
- Communication between the user and HPC admins is crucial for optimizing job performance.
---

### 2021020142003507_Gromacs%20jobs%20on%20TinyGPU%20-%20bccb007h.md
# Ticket 2021020142003507

 # HPC Support Ticket: Gromacs Jobs on TinyGPU

## Keywords
- Gromacs
- TinyGPU
- GPU utilization
- Job configuration
- Resource allocation

## Issue
- User has two jobs waiting for resources on TinyGPU.
- Both jobs request 4 GPUs but are configured to use only one GPU.

## Root Cause
- The Gromacs binary used by the user is multi-threaded but can only utilize a single GPU.
- Requesting multiple GPUs for a single Gromacs run is not beneficial in most cases.

## Solution
- Change the job configuration to request a single GPU (ppn=4).

## General Learnings
- Ensure that job configurations match the capabilities of the software being used.
- Over-requesting resources can lead to inefficient use of HPC resources.
- Gromacs jobs typically benefit from a single GPU per run.

## Actions Taken
- HPC Admin advised the user to adjust the job configuration to request a single GPU.

## Follow-up
- Monitor user's job submissions to ensure proper resource allocation.
- Provide additional guidance on optimizing Gromacs jobs if needed.
---

### 2021120342000578_Benchmark-Jobs%20on%20Alex%20%5Bbccb006h%5D.md
# Ticket 2021120342000578

 # HPC Support Ticket: Benchmark-Jobs on Alex

## Keywords
- Benchmark Jobs
- GPU Utilization
- Gromacs Flags
- Job Monitoring
- Python Script
- Simulation Distribution
- Wait Times

## Problem Description
- Some benchmark jobs on Alex are not utilizing all requested GPUs.
- Pauses in GPU usage observed during job execution.
- Inefficient use of GPU resources.

## Root Cause
- Incorrect Gromacs flags (e.g., `-ntmpi 2`) leading to underutilization of GPUs.
- Python script distributing simulations across GPUs but causing significant wait times between simulations.

## Solution
- Adjust Gromacs parameters to ensure full utilization of GPUs (e.g., `-ntmpi 4` for 2 GPUs, `-ntmpi 8` for 4 GPUs).
- Modify the Python script to start only one simulation per run to minimize wait times.

## General Learnings
- Ensure proper configuration of job parameters to maximize resource utilization.
- Monitor job performance and adjust scripts to reduce inefficiencies.
- Communicate with users to understand their workflow and provide tailored solutions.
---

### 2021102542001066_Resubmitting%20jobs.md
# Ticket 2021102542001066

 # HPC Support Ticket: Resubmitting Jobs

## Keywords
- Job resubmission
- Regular expressions
- Gromacs
- SIMRUN numbering
- `sed` command
- `mpirun` vs `srun`

## Problem
- User experiences issues with job resubmission script, particularly with run numbering when running more than 10 jobs.
- Regular expression in the script does not match all digits, leading to incorrect numbering.
- Issues with running simulations using the new Gromacs version on Meggie.

## Root Cause
- Incorrect regular expression in the script (`sed -e "s/^export SIMRUN=[0-6.]/expo..."`) does not match digits "7", "8", or "9".
- Use of `mpirun --oversubscribe` instead of `srun` for the new Gromacs+Plumed module.

## Solution
- Adjust the regular expression to match all single-digit numbers using `[0-9]?`.
- Replace `mpirun --oversubscribe` with `srun` for the new Gromacs+Plumed module.
- Ensure the SIMRUN number is adjusted to the number of the last completed run to avoid starting from "0" again.

## General Learnings
- Regular expressions should be carefully crafted to match all intended patterns.
- Using `srun` instead of `mpirun --oversubscribe` can resolve issues with certain modules.
- Adjusting the SIMRUN number is crucial for continuous job numbering in automatic resubmissions.

## Additional Resources
- [Regex101](https://regex101.com/) for testing regular expressions.
- HPC Services support for further assistance.
---

### 2020120942001415_Your%20current%20jobs%20on%20Emmy%20%28bccc018h%29.md
# Ticket 2020120942001415

 # HPC Support Ticket: Your current jobs on Emmy (bccc018h)

## Keywords
- Gromacs
- MPI
- mpiexec
- mdrun
- Parallel computing
- Multithreading
- Job script
- Cluster monitoring

## Problem
- User's jobs were not running optimally on the cluster.
- The job script used `mpiexec gmx mdrun -v -deffnm 100ps_eq_${j}`, starting 20 serial Gromacs processes that performed multithreading.

## Root Cause
- Incorrect usage of Gromacs command in the job script, leading to inefficient parallel computing.

## Solution
- Change the job script to use the MPI-version of Gromacs, which is optimized for parallel computing.
  ```bash
  mpiexec mdrun_mpi -v -deffnm 100ps_eq_${j}
  ```
- Refer to the official documentation for Gromacs on the HPC website for further details: [Gromacs Documentation](https://www.anleitungen.rrze.fau.de/hpc/special-applications-and-tips-tricks/gromacs/#collapse_1)

## Outcome
- The issue was resolved after the user updated the job script to use `mdrun_mpi`.
- Jobs run on 8.12. and 10.12.2020 used the correct `mdrun_mpi` command.

## General Learning
- Ensure that job scripts are optimized for parallel computing by using the appropriate MPI commands.
- Regularly monitor cluster jobs to identify and address inefficiencies.
- Provide users with clear documentation and support for optimizing their job scripts.
---

### 2021081242000729_Gromacs-Jobs%20auf%20Meggie%20%5Bbccb006h%5D.md
# Ticket 2021081242000729

 # HPC Support Ticket: Gromacs Jobs on Meggie

## Keywords
- Gromacs
- Job Monitoring
- Version Update
- GPU Cluster
- Resource Optimization

## Summary
- **Root Cause**: User was using an outdated version of Gromacs (2019.3) which was causing performance issues.
- **Solution**: HPC Admin suggested updating to the latest Gromacs version (2021.1) and testing the job on the GPU cluster (TinyGPU).

## Detailed Conversation
- **HPC Admin**: Notified the user that their Gromacs jobs were performing poorly due to using an outdated version (2019.3). Suggested updating to the latest version (2021.1) and testing the job on the GPU cluster (TinyGPU).
- **User**: Responded that they prefer not to change versions within a project but agreed to switch to TinyGPU despite no significant performance difference in initial tests.

## Lessons Learned
- Regularly update software versions to benefit from performance improvements.
- Test jobs on different clusters (e.g., GPU clusters) to optimize resource usage.
- Communicate with users to understand their project constraints and offer alternative solutions.

## Actions Taken
- HPC Admin provided guidance on updating Gromacs version and suggested testing on TinyGPU.
- User agreed to switch to TinyGPU to free up resources on Meggie.

## Follow-Up
- Monitor the performance of the job on TinyGPU.
- Provide further assistance if needed to optimize job parameters for better performance on the GPU cluster.
---

### 42169821_gromacs3%20on%20woody.md
# Ticket 42169821

 # HPC Support Ticket: gromacs3 on woody

## Keywords
- gromacs
- installation
- old version
- woody
- fftw3
- Intel MKL
- performance degradation
- configure errors
- make errors

## Summary
A user requested the installation of an old and modified version of gromacs on the woody cluster for test calculations. The HPC Admin provided instructions for the user to build the software themselves due to the age of the version. The user encountered issues during the installation process.

## Problem
The user faced installation problems when following the provided instructions. The issues were documented in `configure.out`, `configure.log`, and `make.out` files located in the user's directory.

## Solution
The HPC Admin provided a step-by-step recipe to build the old version of gromacs:
1. Download the sources and un-tar them.
2. Load the required modules: `module load intel64/12.1up11 fftw3/3.2.2-intel11.1`.
3. Configure the build with specific flags: `env CPPFLAGS="$FFTW_INC" LDFLAGS="-L$FFTW_LIBDIR" ./configure --enable-mpi --program-suffix=_mpi --prefix=$WOODYHOME/gromacs-3.3.1-special`.
4. Build the `mdrun` executable: `make mdrun`.
5. Install the `mdrun` executable: `make install-mdrun`.

## Notes
- Using fftw3 instead of Intel MKL may result in slight performance degradation, but it should not be critical for a few test calculations.
- Further problem clarification was handled outside of the ticketing system (OTRS).

## Learning Points
- Old software versions may not be installed publicly due to maintenance and compatibility concerns.
- Users can be guided to build software themselves with detailed instructions.
- Common issues during software installation include configuration and make errors.
- Performance considerations should be communicated when suggesting alternative libraries (e.g., fftw3 vs. Intel MKL).

## Next Steps
- Review the `configure.out`, `configure.log`, and `make.out` files for specific error messages.
- Provide additional troubleshooting steps if the initial instructions do not resolve the issue.
- Document common installation problems and their solutions for future reference.
---

### 2021111242000857_Jobs%20on%20Emmy%20with%20Gromacs%205.1.2%20%5Bexzi003h%5D.md
# Ticket 2021111242000857

 # HPC-Support Ticket: Jobs on Emmy with Gromacs 5.1.2

## Keywords
- Gromacs
- Emmy
- TinyGPU
- GPU
- LINCS errors
- Performance benchmarking
- Segmentation fault
- Equilibration

## Summary
- User running jobs on Emmy with an old version of Gromacs (5.1.2).
- Issues with Nose-Hoover implementation in Gromacs 2019 led to downgrade.
- HPC Admin suggested updating to Gromacs 2021.4 and benchmarking on GPUs.
- User encountered LINCS errors with Gromacs 2021.1 on TinyGPU.

## Root Cause
- LINCS errors likely due to unequilibrated system or rapid temperature increase.
- Segmentation fault in Gromacs 2020 on Emmy.

## Solutions
- HPC Admin provided benchmark results showing significant performance increase with GPUs.
- User advised to use `-ntomp 4` for best performance on GTX1080TI.
- HPC Admin suggested running simulations on Emmy until GPU issue is resolved.
- HPC Admin attempted to reproduce LINCS errors and suggested step-by-step equilibration.

## Benchmark Results
- Gromacs 2021.1 on TinyGPU showed significant performance increase compared to Emmy.
- RTX3080 and A100 GPUs showed the highest performance.

## Commands Used
- `module load gromacs/2021.1-mkl-CUDA111-ebyjbq`
- `gmx mdrun -v -deffnm iteration_${i}_423KTmod -s iteration_${i}_423KTmod.tpr -nb gpu -bonded gpu -pme gpu -pin on -pinstride 1 -ntmpi 1 -ntomp 8`
- `gmx grompp -f md_423.mdp -c nptavg_it6_423KTmod_2.gro -p topology_6_423KTmod.top`
- `gmx mdrun -v -s topol.tpr -nb gpu -pme gpu -bonded gpu -update cpu -ntmpi 1 -ntomp 4 -pin on -pinstride 1`

## Conclusion
- User should continue using Emmy for current simulations.
- Further investigation needed to resolve LINCS errors on GPUs.
- Step-by-step equilibration suggested to prevent LINCS errors.
---

### 2020091142002274_Re%3A%20TinyGPU-Boost%20f%C3%83%C2%BCr%20SCC-Team.md
# Ticket 2020091142002274

 ```markdown
# HPC Support Ticket Conversation Analysis

## Keywords
- TinyGPU-Boost
- GROMACS Benchmark
- V100 GPUs
- Multi-GPU Implementation
- Performance Measurements
- Datasets

## Summary
- **Request**: User requested a boost or reservation for two V100 GPUs in TinyGPU until the end of September for specific accounts.
- **GROMACS Benchmark**: User inquired about GROMACS benchmark datasets mentioned in an Nvidia blog post.
- **Response**: HPC Admin provided a link to GROMACS benchmark files and offered assistance for further questions.

## Root Cause of the Problem
- User needed access to specific GPU resources for a competition.
- User required benchmark datasets for GROMACS to reproduce results from an Nvidia blog post.

## Solution
- HPC Admin provided the necessary benchmark files via a link.
- User was informed that two V100 GPUs would be sufficient for experimentation, with the option to wait for larger runs.

## General Learnings
- **Resource Allocation**: Understanding how to allocate and reserve GPU resources for specific projects or competitions.
- **Benchmark Data**: Importance of providing benchmark datasets for users to reproduce and validate performance results.
- **Communication**: Effective communication between users and HPC Admins to address resource needs and technical queries.
```
---

### 2020052942002284_mdrun%20auf%20GPU%3F.md
# Ticket 2020052942002284

 Sure, here is the report:

---

### HPC Support Ticket Summary

**User:** Frances D. Lenahan

**Issue:** Performance and configuration issues with GROMACS simulations on Emmy and TinyGPU.

**HPC Admins:** Thomas Zeiser, Anna Kahler

**Date:** 29.05.2020 - 30.06.2020

**Problem:**
- User encountered performance issues with GROMACS simulations on Emmy.
- User tested GPU simulations on TinyGPU but faced issues with LJPME long-range dispersion interactions not being available on GPUs.
- User implemented `-gcom` flag which affected the saving frequency of energies, impacting the ability to accurately predict diffusion of small gas molecules in alkanes.
- User sought advice on whether to continue using Emmy or switch to TinyGPU for new simulations.

**Solution:**
- HPC Admins provided detailed guidance on using `-gcom` and other flags to optimize performance.
- HPC Admins conducted benchmark tests to evaluate the performance of GPU simulations on TinyGPU.
- HPC Admins suggested using TinyGPU for new simulations due to better performance and cost-efficiency.
- HPC Admins provided information on the limitations of `-gcom` and suggested alternative approaches to maintain saving frequency while improving performance.

**Keywords:** GROMACS, Emmy, TinyGPU, Performance, Simulation, GPU, `-gcom`, LJPME, Energy Saving Frequency, Diffusion Prediction, Alkanes, Benchmark Tests.

---

This report summarizes the key points and solutions provided by the HPC Admins to address the user's issues with GROMACS simulations on Emmy and TinyGPU. The user was guided on optimizing performance using various flags and was advised to switch to TinyGPU for new simulations due to better performance and cost-efficiency. The limitations of certain flags were also discussed, and alternative approaches were suggested to maintain the saving frequency of energies while improving performance.
---

### 2022071142001506_Problem%20Gromacs%20auf%20Meggie.md
# Ticket 2022071142001506

 # HPC-Support Ticket: Problem Gromacs auf Meggie

## Subject
Problem Gromacs auf Meggie

## User
- **Account**: bccc034h
- **Issue**: Unable to start Gromacs simulation on Meggie
- **Module**: gromacs/2020.6-gcc-openmpi-mkl-plumed2.7.2
- **Error Message**: Segmentation fault (11)

## HPC Admin
- **Initial Response**: Requested Slurm-Outputfile, Jobskript, Gromacs-Outputfile, and .tpr-Datei for detailed analysis.
- **Diagnosis**: Identified incorrect parameter in the job script.
- **Solution**: Corrected the job script parameter to `--ntasks-per-node`.

## 2nd Level Support Team
- **Involvement**: Not explicitly mentioned in the conversation.

## Root Cause
- **Issue**: Incorrect parameter in the job script causing Slurm to distribute processes incorrectly.
- **Solution**: Corrected the job script parameter to `--ntasks-per-node`.

## Keywords
- Gromacs
- Segmentation fault
- Slurm
- Job script
- Parameter correction

## What to Learn
- **Job Script Parameters**: Ensure correct parameters are used in job scripts to avoid process distribution issues.
- **Segmentation Faults**: Segmentation faults can be caused by incorrect job script parameters.
- **Slurm Configuration**: Proper configuration of Slurm parameters is crucial for successful job execution.

## Solution
- **Correction**: Ensure the job script uses `--ntasks-per-node` to correctly distribute tasks.

## Ticket Closure
- **Status**: Problem resolved, ticket closed.
---

### 2017102442001094_Probleme%20min%20Gromacs%20auf%20meggie.md
# Ticket 2017102442001094

 ```markdown
# HPC-Support Ticket: Probleme mit Gromacs auf Meggie

## Problem
- User konnte Gromacs-Simulation auf Meggie nicht starten.
- Energieminimierung mit Gromacs 4.6.7 und 5.1.3 führte zu Segmentation Fault.
- Problem trat nach einem Update der Intel-Compiler auf.

## Ursache
- Update der Intel-Compiler (intel64 und intelmpi) am Samstag.
- Mögliche Inkompatibilität zwischen den neuen Compilern und den bestehenden Gromacs-Versionen.

## Lösung
- HPC Admin hat Gromacs 4.6.7 mit den aktuellen Intel-Compilern neu gebaut.
- Neue Versionen von Gromacs (5.1.4 und 2016.4) wurden installiert.
- Alte Versionen von Gromacs (5.1.3 und 2016) wurden als "deprecated" markiert.

## Schritte zur Lösung
1. HPC Admin hat die neuen Intel-Compiler (intel64/17.0up05) geladen.
2. Gromacs 4.6.7 wurde neu kompiliert und getestet.
3. Neue Versionen von Gromacs (5.1.4 und 2016.4) wurden installiert.
4. User wurde informiert, die neuen Versionen zu verwenden.

## Hinweise
- Bei zukünftigen Updates der Intel-Compiler sollte geprüft werden, ob bestehende Software neu kompiliert werden muss.
- Umgebungsvariable `LD_BIND_NOW` kann temporär helfen, aber eine Neukompilierung ist die langfristige Lösung.

## Schlüsselwörter
- Gromacs
- Intel-Compiler
- Segmentation Fault
- Neukompilierung
- Update
```
---

### 2024100742004056_Fw%3A%20GROMACS%20%28gpu-enabled%29%20on%20several%20nodes%20and%20GROMACS2024%20compilation.md
# Ticket 2024100742004056

 # HPC Support Ticket: GROMACS (GPU-enabled) on Several Nodes and GROMACS2024 Compilation

## Keywords
- GROMACS
- GPU-enabled
- Multi-node
- Submit script
- Performance
- PLUMED
- Compilation

## Summary
A user is requesting assistance with running large-scale simulations using GROMACS (GPU-enabled) on multiple nodes and GPUs. The user also inquires about the compilation of GROMACS2024 and how to write a submit script for it.

## Problem
- The user's current submit script for running GROMACS on multiple nodes is not functional.
- The user wants to know if multi-node simulations are possible and how to write a working submit script.
- The user plans to upgrade to GROMACS2024.1 and needs information on its compilation and an example submit script.

## Solution
- **Multi-Node Simulations**: The HPC Admin has conducted tests and found that multi-node simulations may not be beneficial. Further benchmarks are being conducted.
- **Submit Script**: The user's submit script needs to be modified. The HPC Admin will provide further details after additional benchmarks.
- **GROMACS2024.1 Compilation**: The HPC Admin will provide information on the compilation of GROMACS2024.1 and an example submit script after further investigation.

## Lessons Learned
- Multi-node simulations with GROMACS may not always be beneficial and require thorough benchmarking.
- Submit scripts for multi-node simulations need careful configuration.
- Users should be informed about the compilation details and example submit scripts for new software versions.

## Next Steps
- The HPC Admin will conduct further benchmarks and provide detailed information on multi-node simulations and GROMACS2024.1 compilation.
- The user should wait for the HPC Admin's feedback before proceeding with large-scale simulations.
---

### 2024121942002353_Gromacs%20flag%20-v%20%5Bc103cb10%5D.md
# Ticket 2024121942002353

 # HPC Support Ticket: Gromacs Flag -v

## Keywords
- Gromacs
- Debugging Flag
- Network Load
- Simulation Performance
- Fileserver Load

## Issue
- User was running Gromacs simulations with the debugging flag `-v` enabled.
- This flag generates a large amount of irrelevant information for production runs.
- High network and fileserver load due to excessive data writing.

## Root Cause
- The debugging flag `-v` was included in the user's standard scripts, causing unnecessary data output and increased load on the network and fileserver.

## Solution
- Remove the debugging flag `-v` from the Gromacs scripts to reduce unnecessary data output and improve simulation performance.

## General Learning
- Avoid using debugging flags in production runs as they can generate excessive data and slow down simulations.
- Regularly review job scripts to ensure they are optimized for performance and do not contribute to unnecessary system load.

## Actions Taken
- HPC Admin advised the user to remove the debugging flag `-v` from their Gromacs scripts.
- User acknowledged the advice and agreed to remove the flag.

## Follow-up
- Monitor the fileserver and network load to ensure the issue is resolved.
- Provide further assistance if needed.
---

### 2024121942002371_Gromacs%20flag%20-v%20%5Bk101ee10%5D.md
# Ticket 2024121942002371

 # HPC Support Ticket: Gromacs Flag -v

## Keywords
- Gromacs
- Debugging Flag (-v)
- Fileserver Load
- Network Performance
- Job Scripts
- Simulation Performance

## Problem
- User had the debugging flag `-v` enabled in Gromacs, which generates a large amount of irrelevant information for production runs.
- This excessive logging can slow down simulations and increase load on the fileserver and network.

## Root Cause
- The debugging flag `-v` was inadvertently left enabled in the user's job scripts, leading to increased I/O and network load.

## Solution
- Remove the `-v` flag from all job scripts to reduce unnecessary logging and improve simulation performance.

## Additional Notes
- The HPC Admin also requested the user to remind a professor about a pending review through JARDS.

## General Learning
- Always review job scripts to ensure debugging flags are removed for production runs.
- Excessive logging can impact both simulation performance and overall system load.

---

This documentation can be used to address similar issues in the future by ensuring that debugging flags are properly managed in job scripts.
---

### 2021072142002999_Gromacs%2C%20Fehlermeldung%3A%20There%20is%20no%20domain%20decomposition%20for%20108%20ranks%20that%.md
# Ticket 2021072142002999

 # HPC Support Ticket Analysis

## Subject
Gromacs, Fehlermeldung: There is no domain decomposition for 108 ranks that is compatible with the given box and a minimum cell size of 2.13209 nm

## Keywords
- Gromacs
- Domain decomposition
- Minimum cell size
- LINCS Fehler
- Positional Restraints
- Batch system (PBS/Torque, Slurm)
- sbatch
- qsub
- Reimaging

## Issues and Solutions

### Issue 1: Domain Decomposition Error
- **Problem**: User received an error message indicating no compatible domain decomposition for 108 ranks with the given box and minimum cell size.
- **Solution**: The issue was resolved by performing a "reimaging."

### Issue 2: LINCS Fehler
- **Problem**: During energy minimization, numerous LINCS errors were generated, indicating issues with constraints and excessive movement of bonds/angles.
- **Solution**: Suggested to follow a step-by-step protocol for relaxing different components of the system (water, membrane, protein, ligand) sequentially.

### Issue 3: Invalid Number of Nodes Error
- **Problem**: User received an error message `sbatch: error: invalid number of nodes (-N 2-1)` when submitting a script.
- **Solution**: The script was intended for the PBS/Torque batch system but was submitted using Slurm. The issue was resolved by using `qsub.tinygpu` instead of `sbatch.tinygpu`.

## General Learnings
- **Batch System Compatibility**: Ensure that job scripts are compatible with the batch system being used (PBS/Torque vs. Slurm).
- **Step-by-Step Simulation Setup**: For complex simulations, follow a structured protocol to relax different components of the system sequentially.
- **Reimaging**: Performing a "reimaging" can resolve issues related to domain decomposition errors.
- **Error Messages**: Understand and address specific error messages (e.g., LINCS errors) by adjusting simulation parameters or constraints.

## Conclusion
The ticket was closed as the issues were resolved by performing a "reimaging" and using the correct batch system commands. The user was also advised on how to set up the simulation to avoid LINCS errors.
---

### 2024030542003716_Gromacs%202024.1.md
# Ticket 2024030542003716

 ```markdown
# HPC Support Ticket: Gromacs 2024.1 Installation

## Keywords
- GROMACS
- Installation
- Alex
- gcc11.2.0
- mkl
- cuda

## Summary
A user requested the installation of GROMACS 2024.1 on the Alex system.

## Problem
- User requested the installation of GROMACS 2024.1.

## Solution
- HPC Admin installed an untested version of GROMACS 2024.1 with the configuration `gromacs/2024.1-gcc11.2.0-mkl-cuda`.

## Lessons Learned
- Ensure that software installations are tested before confirming availability to users.
- Communicate the status of software installations clearly to users.
```
---

### 2022092142001967_Regarding%20facing%20error%20during%20multinode%20simulations%20using%20Gromacs.md
# Ticket 2022092142001967

 ```markdown
# HPC-Support Ticket: Regarding Facing Error During Multinode Simulations Using Gromacs

## Problem Description
- **User Issue**: Error during multinode simulations using Gromacs after system upgrade.
- **Error Messages**:
  - `execvp error on file mdrun_mpi (no such file or directory)`
  - `execvp error on file mdrun_mpi+OMP (no such file or directory)`
  - `execvp error on file gmx_mpi (no such file or directory)`
- **Command Used**: `mpirun mdrun_mpi+OMP -np 160 -deffnm /home/hpc/mpt4/mpt4022h/kcl100/nvt3/nvt -maxh 24`

## Root Cause
- The specified executables (`mdrun_mpi`, `mdrun_mpi+OMP`, `gmx_mpi`) do not exist in the specified paths.
- The issue occurs only during multinode simulations, not single-node simulations.

## Troubleshooting Steps
1. **HPC Admin**: Suggested checking for typos in the file path.
2. **User**: Confirmed the file `nvt.tpr` exists in the directory.
3. **HPC Admin**: Identified the correct Gromacs module and executable for multinode simulations.

## Solution
- **Correct Module**: `gromacs/2021.4-gcc11.2.0-impi-mkl-plumed`
- **Correct Command**: `srun gmx_mpi mdrun -deffnm /home/hpc/mpt4/mpt4022h/kcl100/nvt3/nvt -maxh 24`
- **Explanation**: `srun` should automatically set the number of threads according to the batch script parameters.

## Outcome
- The user confirmed that using the correct module and command resolved the issue.

## Keywords
- Gromacs
- Multinode Simulations
- execvp error
- mdrun_mpi
- gmx_mpi
- srun
- Slurm
- HPC Upgrade

## General Learning
- Ensure the correct module and executable are used for multinode simulations.
- Verify file paths and executable names to avoid `execvp` errors.
- Use `srun` for parallel job submissions to automatically manage resources.
```
---

### 2023071342002616_GROMACS%202023.2.md
# Ticket 2023071342002616

 ```markdown
# HPC Support Ticket: GROMACS 2023.2 Installation

## Keywords
- GROMACS 2023.2
- Installation
- Alex
- Benchmarks
- Stability

## Problem
- User requested the installation of GROMACS 2023.2 on the HPC system Alex.

## Solution
- HPC Admin informed the user that GROMACS 2023.2 (gromacs/2023.2-gcc11.2.0-mkl-cuda) is already installed on Alex.
- Benchmarks performed by the HPC Admin indicate good performance.
- User advised to verify the stability of their simulations.

## General Learnings
- Regularly check for new software versions and their availability on the HPC system.
- Benchmarks and stability checks are crucial after new software installations.
- Communicate with users to ensure they are aware of the latest software updates and their performance.
```
---

### 2019051542001812_GROMACS_PLUMED%20module%20mit%20DRR-module%20-%20hpc-ID%20bcpc07.md
# Ticket 2019051542001812

 # HPC Support Ticket: GROMACS/PLUMED Module with DRR for Adaptive-Biasing-Force Simulation

## Subject
GROMACS/PLUMED module mit DRR-module - hpc-ID bcpc07

## User Request
- User wants to use the DRR module from PLUMED with GROMACS for an adaptive-biasing-force simulation.
- Standard installation does not include this module.
- Request for a patched version of GROMACS (2018 or 2019) with the DRR module.

## HPC Admin Actions
- Initial attempt to provide `gromacs/2018.6-mkl-plumed-2.5.1-drr`.
- Compilation succeeded but PLUMED did not recognize the input for ABF calculations.
- User provided additional compilation options (`--enable-boost_serialization`).
- Multiple attempts to compile PLUMED and GROMACS with the required options.
- BOOST serialization issues were encountered.
- Final successful build with `boost_serialization` linked and PLUMED recognized as an extension of GROMACS.

## Root Cause
- Missing compilation options (`--enable-boost_serialization`) for PLUMED.
- BOOST serialization issues during the build process.

## Solution
- Compile PLUMED with `--enable-boost_serialization` and `--enable-modules=drr`.
- Use SPACK to manage BOOST serialization dependencies.
- Ensure `boost_serialization` is linked correctly during the build process.

## Keywords
- GROMACS
- PLUMED
- DRR module
- Adaptive-biasing-force simulation
- BOOST serialization
- Compilation options
- SPACK

## Lessons Learned
- Ensure all required compilation options are included when building custom modules.
- Use SPACK to manage dependencies and avoid compilation issues.
- Test the final build to ensure all extensions and modules are recognized correctly.

## Final Status
- Successful build of `gromacs/2018.6-mkl-plumed-2.5.1-drr` with PLUMED recognizing the DRR module.
- User confirmed the module works and the first calculation is running.
---

### 2024020542001569_Job%20on%20Alex%20does%20not%20use%20allocated%20GPU%20%5Bb188dc13%5D.md
# Ticket 2024020542001569

 # HPC Support Ticket: Job on Alex does not use allocated GPU

## Keywords
- GPU utilization
- Gromacs
- Job allocation
- Performance optimization
- Monitoring

## Problem
- User's jobs on Alex (JobID 1074091, 1074090, and 1074089) were not utilizing the allocated two GPUs.
- Gromacs command line contained `-ntmpi 1 -ntomp 32`, which only invoked one rank on the GPU, resulting in only one GPU being used.

## Root Cause
- Incorrect Gromacs command line parameters leading to underutilization of allocated GPUs.

## Solution
- Change the Gromacs command line parameters to `-ntmpi 2 -ntomp 16` to ensure both GPUs are utilized.

## Additional Information
- Depending on the size of the simulation system, using multiple GPUs might decrease overall performance.
- Users can monitor GPU utilization using ClusterCockpit at [monitoring.nhr.fau.de](https://monitoring.nhr.fau.de/).
- Alternatively, users can attach to their running job with `srun --pty --overlap --jobid YOUR-JOBID bash` and use `nvidia-smi` to check GPU utilization.

## Actions Taken
- HPC Admin provided guidance on modifying the Gromacs command line.
- User updated the submit script as suggested.
- User will perform performance analysis using the provided tools.

## Closure
- Ticket closed as the user implemented the suggested changes and will perform further analysis.

---

This report provides a concise summary of the issue, the root cause, the solution, and additional information for future reference.
---

### 2022110842002558_Load%20imbalance%20on%20nodes%20%2B%20Gromacs%20on%20CPU%20%5Bmpt4022h%5D.md
# Ticket 2022110842002558

 ```markdown
# HPC Support Ticket Conversation Summary

## Issue: Load Imbalance on Nodes + Gromacs on CPU

### Key Points:
- User encountered load imbalance issues with Gromacs jobs on a parallel CPU cluster.
- HPC Admins suggested transitioning to GPU for better performance.
- Benchmarking and optimization of Gromacs on TinyGPU were performed.
- User faced issues with out-of-memory errors and MPI deadlocks during PME calculations.
- Solutions included using cut-off for Coulomb type and ensuring correct module usage.

### Solutions:
- **Transition to GPU**: Gromacs shows higher performance on GPUs, especially with recent code changes.
- **Benchmarking**: Performance on TinyGPU (RTX2080Ti and RTX3080) was significantly better than on Meggie.
- **Out-of-Memory Error**: Specify Coulomb type as cut-off to avoid errors related to PME calculations.
- **Module Usage**: Ensure correct Gromacs module is used on TinyGPU frontend to avoid "Illegal instruction" errors.
- **Checkpoint Restart**: Ensure all relevant files (md.log, traj_comp.xtc, ener.edr) are present for continuing simulations.

### Additional Notes:
- Use `$WORK` directory for storing simulation data instead of `$HOME`.
- For detailed job monitoring, log into the job monitoring system using HPC username and password.
- If issues persist, a Zoom meeting can be scheduled for further assistance.

### Conclusion:
The user successfully transitioned to GPU and resolved load imbalance and out-of-memory errors by following the provided solutions. Benchmarking on TinyGPU showed improved performance, and the user was guided on how to continue jobs from the last checkpoint.
```
---

### 2025031842004207_GROMACS%202025.1.md
# Ticket 2025031842004207

 # HPC-Support Ticket: GROMACS 2025.1 Installation Request

## Keywords
- GROMACS 2025.1
- Installation
- alex/woody
- SPACK
- Software Update

## Summary
A user requested the installation of GROMACS 2025.1 on the alex/woody system. The HPC Admin responded that the new version of GROMACS has significant changes and SPACK does not yet support it, indicating that the installation will take some time.

## Root Cause
- The user requested a specific version of GROMACS that is not yet supported by SPACK.

## Solution
- The HPC Admin acknowledged the request and informed the user that the installation will take some time due to the changes in the new version of GROMACS.

## General Learnings
- New software versions may not be immediately supported by package managers like SPACK.
- Installation of new software versions may require additional time and effort from the HPC team.
- Communication with users about the status of software installations is important.

## Next Steps
- Monitor the availability of GROMACS 2025.1 in SPACK.
- Plan and execute the installation of GROMACS 2025.1 on alex/woody.
- Keep the user informed about the progress of the installation.
---

### 2024010942003776_help%20parallel%20gromacs%20jobs%20-%20b119ee10.md
# Ticket 2024010942003776

 # HPC Support Ticket Conversation Report

## Subject
Help parallel GROMACS jobs - b119ee10

## User
Marijana Ugrina

## Issue
User needs to run 100 parallel GROMACS jobs on the Fritz cluster. The GROMACS tpr files are located in the folder: `/home/atuin/b119ee/b119ee10/run200`. Using GROMACS version 2023.1.

## Key Points Learned

### Initial Setup
- User requested an example script for running 100 parallel GROMACS jobs.
- Simulations are independent and not connected (e.g., REMD or metadynamics).

### Performance Benchmarking
- HPC Admins benchmarked 10 simulations in parallel on Alex and Fritz.
- Recommended using Alex due to better performance on a single A40 with GROMACS 2023.3.

### Data Management
- Simulations were initially set up to copy data to local SSD at the beginning and save back to the working directory before the job ends.
- Issues with copying large amounts of data led to long copy times (7-8 hours).

### Solutions
- **Multidir Option**: Initially suggested but not feasible due to the nature of the simulations.
- **No Append Option**: Suggested to avoid appending trajectories and to use only xtc files to save memory.
- **Ceph Storage**: Introduced a new storage solution (Ceph) to handle large amounts of data efficiently.
  - Allocation of workspace: `ws_allocate run200 90`
  - Accessing workspace: `STORAGE_DIR="$(ws_find run200)"`

### Script Adjustments
- Adjusted the submit script to use the new workspace and avoid unnecessary copying.
- Ensured the simulation continues properly and attaches to old files.

### Final Setup
- User decided to continue with the current setup for the final batch and will implement the new method for future simulations.

## Conclusion
The conversation highlights the importance of efficient data management and the use of appropriate storage solutions for large-scale simulations. The final setup ensures that the user can run their simulations without overloading the NFS server and with minimal data copying.

## References
- [GROMACS Manual](https://manual.gromacs.org/current/user-guide/managing-simulations.html#appending-to-output-files)
- [Ceph Documentation](https://doc.nhr.fau.de/data/workspaces/)

---

This report provides a summary of the key points learned from the support ticket conversation, focusing on the initial setup, performance benchmarking, data management solutions, and final setup for running parallel GROMACS jobs on the Fritz cluster.
---

### 2020010742002921_Installation%20of%20new%20Gromacs%20versions%20on%20Emmy%20and%20TinyGPU.md
# Ticket 2020010742002921

 # HPC-Support Ticket Conversation Analysis

## Keywords
- Gromacs versions (2019.5, 2020)
- Performance issues
- GPU offloading
- Benchmarking
- SIMD instructions
- Hyperthreading (:smt)
- Dynamic load balancing (DLB)
- OpenMP threads
- Walltime
- PME mesh
- Wait GPU NB local

## What to Learn Generally
- The importance of benchmarking new software versions on HPC clusters.
- How to troubleshoot performance issues in HPC applications.
- The impact of different hardware configurations on software performance.
- The role of SIMD instructions and hyperthreading in performance optimization.
- The use of dynamic load balancing and OpenMP threads in HPC applications.

## Root Cause of the Problem
- The user experienced significant performance degradation with Gromacs 2020 compared to Gromacs 2019.5 on both TinyGPU and Emmy clusters.
- The performance issue was primarily due to increased wait times in 'Wait GPU NB local' and 'PME mesh' operations.

## Solution
- The user was advised to use the :smt option to enable hyperthreading, which allows more threads to run without performance degradation.
- The user was also advised to adjust the -ntmpi and -ntomp parameters to ensure the product of these values matches the number of threads requested in the batch script.
- The user was encouraged to enable dynamic load balancing (DLB) and set the pinstride to 1 to optimize CPU loading.
- The user was informed about the potential impact of SIMD instructions on performance and advised to consult the Gromacs mailing list for further assistance.
- The HPC Admins installed Gromacs 2020.1 on TinyGPU and Emmy to see if the performance issue persisted.

## Conclusion
- The performance issue was confirmed by the Gromacs development team, and a Bugzilla entry was created to track the issue.
- The user decided to wait for further updates from the Gromacs team before conducting additional benchmarks.
- The HPC Admins provided continuous support and guidance throughout the troubleshooting process.
---

### 42242862_segmentation%20fault.md
# Ticket 42242862

 # HPC Support Ticket: Segmentation Fault

## Keywords
- Segmentation fault
- GROMACS
- MPI
- Domain decomposition error
- Water molecules

## Problem Description
- User encountered segmentation faults when running GROMACS jobs with 4 or 8 processors.
- For 8 processors, additional errors included unexpected disconnect completion events and assertion failures.

## Root Cause
- Incorrect placement of water molecules in the system due to a script error, leading to rapid movement and system crashes.

## Troubleshooting Steps
- User identified the issue with water molecules and corrected the problem.

## Solution
- Fixing the water molecule placement in the system resolved the segmentation faults and other related errors.

## General Learnings
- Segmentation faults in GROMACS can be caused by issues with the simulation setup, such as incorrect particle placement.
- Domain decomposition errors typically indicate problems with particles leaving their designated cells.
- Always verify the simulation setup and input files to avoid such issues.

## Support Team Involved
- HPC Admins
- 2nd Level Support Team
---

### 2018071042002622_Multi%20node%20simulations%20in%20double%20precision%20%28%20gromacs_5.1.1-mkl-IVB_d%20%29.md
# Ticket 2018071042002622

 # HPC Support Ticket: Multi-Node Simulations in Double Precision (Gromacs/5.1.1-mkl-IVB_d)

## Keywords
- Multi-node jobs
- Double precision
- Gromacs
- mdrun_mpi_d
- EMMY
- LiMa
- No such file or directory

## Problem Description
The user attempted to run multi-node jobs using double precision with the `gromacs/5.1.1-mkl-IVB_d` version on EMMY. The command used was:
```
mpirun_rrze -pinexpr S0:0-19@S1:0-19 mdrun_mpi_d -deffnm NVT1 -cpo continue1.cpt -maxh 1.0
```
This resulted in a "no such file or directory" error. However, the single precision version without the `_d` suffix worked correctly.

## Root Cause
The installation process did not append the `_d` suffix to the MPI binary for the double precision version of Gromacs.

## Solution
The HPC Admin created a link to ensure that both `mdrun_mpi` and `mdrun_mpi_d` work for the `gromacs/5.1.1-mkl-IVB_d` version.

## Additional Information
- The user requested access to `gromacs/5.1.1-mkl-IVB_d` on LiMa, but the HPC Admin informed that there is no double precision Gromacs installed on LiMa, and no new software will be installed as LiMa is close to its End of Life (EOL).

## Lessons Learned
- Ensure that the installation process correctly appends the `_d` suffix to the MPI binary for double precision versions of software.
- Communicate the availability and limitations of software versions on different HPC systems to users.
---

