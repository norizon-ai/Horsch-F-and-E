# Topic 1: nodes_job_jobs_node_the

Number of tickets: 526

## Tickets in this topic:

### 2024032542002279_MPI%20Startup%20notification.md
# Ticket 2024032542002279

 ```markdown
# HPC-Support Ticket: MPI Startup Notification

## Subject
MPI startup notification regarding unsupported I_MPI_WAITMODE for shm:ofi fabrics.

## Keywords
MPI, I_MPI_WAITMODE, shm:ofi fabrics, oversubscription, Intel MPI, SLURM, ClusterCockpit

## Problem Description
User receives a notification in the `*.o${JOBID}` file:
```
MPI startup(): I_MPI_WAITMODE is unsupported for shm:ofi fabrics please specify I_MPI_FABRICS=ofi or I_MPI_FABRICS=shm
```

## Root Cause
The issue is related to oversubscribing the compute nodes. The user applied for 9 nodes (648 cores) but ran with 1000 MPI processes, leading to uneven CPU load across nodes.

## Solution
- Ensure the number of MPI processes matches the allocated resources.
- Avoid oversubscribing nodes to prevent performance degradation.

## Lessons Learned
- Oversubscribing nodes can lead to performance issues and MPI warnings.
- Always verify the number of processes and allocated resources in the job submission script.
- Use monitoring tools like ClusterCockpit to check CPU load and resource usage.

## Actions Taken
- HPC Admin reproduced the issue and identified oversubscription as the cause.
- User corrected the job submission script to match the number of MPI processes with allocated resources.

## Conclusion
Proper resource allocation and avoiding oversubscription are crucial for optimal performance and preventing MPI-related warnings.
```
---

### 42056306_ORCA%20uses%20too%20much%20memory.%20Fwd%3A%20Your%20Job%20ID%20340942%20on%20the%20RRZE%20Woodcrest.md
# Ticket 42056306

 ```markdown
# HPC Support Ticket: ORCA Memory Usage Issue

## Keywords
- ORCA
- Memory usage
- mpirun
- `--npernode`
- HPC cluster

## Problem Description
The user encountered an issue where their ORCA calculations were consuming too much memory, leading to nodes running out of swap space and potentially causing system instability. The user was unable to modify the `mpirun` parameters directly because `mpirun` is executed by ORCA itself.

## Root Cause
- The ORCA calculations were too memory-intensive for the allocated resources.
- The user could not directly modify the `mpirun` parameters to reduce memory usage per node.

## Solution
The HPC Admin provided a workaround to overwrite the `mpirun` command by creating a custom script. The steps were as follows:

1. Create a subdirectory named `MpirunPPN2` in the user's home directory or current working directory.
2. Within this directory, create a file named `mpirun` with the following contents:
    ```bash
    #!/bin/bash
    echo "USING SPECIAL MPIRUN $0 : adding '--npernode 2' to the original arguments $*"
    ${MPIROOTDIR}/bin/mpirun --npernode 2 $*
    ```
3. Make the `mpirun` file executable using `chmod u+x mpirun`.
4. In the jobs that require too much memory, use the following command:
    ```bash
    env PATH=SomePath/MpirunPPN2:$PATH ${ORCABASE}/orca {$filename}.inp
    ```
    Replace `SomePath` with the directory used in steps 1-3.

## Outcome
The user confirmed that the solution worked, and the memory usage issue was resolved.

## General Learning
- Customizing `mpirun` parameters can help manage memory usage for memory-intensive applications.
- Creating a custom script to overwrite the default `mpirun` command is a viable solution when direct modification is not possible.
- Proper memory management is crucial to prevent system instability and ensure efficient resource utilization.
```
---

### 2023103142003291_Multi-node%20jobs%20auf%20Alex.md
# Ticket 2023103142003291

 # HPC Support Ticket: Multi-node Jobs auf Alex

## Keywords
- Multi-node jobs
- CUDA-aware MPI
- Benchmark
- A100 nodes
- QoS (Quality of Service)
- OpenMPI

## Problem
- User requested permissions for multi-node jobs on Alex for their project.
- User needed to run a benchmark using CUDA-aware MPI that requires multiple nodes.

## Solution
- The project was already enabled for multi-node jobs on A100 nodes.
- User was advised to use the `--qos=a100multi` option.
- Additional advice was given to consider the performance differences based on the MPI version used.
- User was recommended to test the new `openmpi/4.1.6*` modules on Alex.

## General Learnings
- Ensure users are aware of the QoS options available for their projects.
- Performance of CUDA-aware MPI benchmarks can vary significantly based on the MPI version.
- Always recommend testing the latest modules for optimal performance.

## References
- [HPC Portal](https://hpc.fau.de/)
- [Helpdesk Ticket](https://www.helpdesk.rrze.fau.de/otrs/index.pl?Action=AgentTicketZoom;TicketID=1143773)

## Roles
- **HPC Admins**: Provided permissions and technical advice.
- **2nd Level Support Team**: Offered additional performance considerations and module recommendations.

## Root Cause
- User was unaware of the existing permissions and the correct QoS option to use for multi-node jobs.

## Resolution
- Informed the user about the existing permissions and the correct QoS option.
- Provided additional advice on MPI performance and recommended testing the latest OpenMPI modules.
---

### 2024080842003194_Benchmarks%20auf%20den%20Fritz%201Tb%20Knoten.md
# Ticket 2024080842003194

 # HPC Support Ticket: Benchmarks auf den Fritz 1TB Knoten

## Keywords
- Fritz Cluster
- Sapphire Rapid Prozessoren
- spr1tb, spr2tb Partitionen
- High-memory Knoten
- Benchmarks
- Single-Node Performance
- Multi-Node Scaling
- Latenz-Zeit
- Switch

## Problem
- User möchte Benchmarks auf den neuesten Knoten mit Sapphire Rapid Prozessoren durchführen.
- Diese Knoten sind für high-memory Rechnungen vorgesehen, aber die Tests des Users benötigen nicht viel Speicherplatz.
- Frage: Erlaubnis zur Nutzung der spr1tb Knoten, obwohl die Speicherkapazitäten nicht gebraucht werden.

## Lösung
- HPC Admin erlaubt die Nutzung der spr1tb Knoten für die Benchmarks.
- Alle SPR-Knoten sind an Leaf-Switch 18 angebunden und haben somit die gleiche Bandbreite und Latenz.

## Zusätzliche Informationen
- Alle 48 Knoten sind am selben Switch angebunden und haben somit die gleiche Latenz-Zeit zueinander.

## Allgemeines
- User arbeitet an der Verbesserung des FFT Codes eines Quantenchemieprogramms.
- Benchmarks sind für eine Publikation vorgesehen.
- Fritz Cluster bietet Knoten mit Sapphire Rapid Prozessoren unter den Partitionen spr1tb und spr2tb.

## Root Cause
- User benötigt Zugang zu spezifischen Knoten für Benchmarks, obwohl diese Knoten für andere Zwecke vorgesehen sind.

## Solution
- HPC Admin erlaubt die Nutzung der spezifischen Knoten für die Benchmarks.
- Bestätigung, dass alle relevanten Knoten am selben Switch angebunden sind und somit die gleiche Latenz-Zeit haben.
---

### 2024060342002279_Tier3-Access-Fritz%20%22Jan%20Alexander%20Koziol%22%20_%20mpt1011h.md
# Ticket 2024060342002279

 # HPC Support Ticket Conversation Analysis

## Keywords
- HPC Account Activation
- Fritz Cluster
- Single-node Throughput
- Multi-node Workload
- Node Hours
- C++ Compiler
- NLopt Library
- Mean-field Calculations
- Phase Diagram
- Publication
- TRR 306 QuCoLiMa

## Summary
- **User Request:** Access to Fritz cluster for mean-field calculations of long-range interacting Dicke-Ising models.
- **Resources Requested:**
  - Single-node throughput (72 cores, 250 GB)
  - Multi-node workload (HDR100 Infiniband with 1:4 blocking; per node: 72 cores, 250 GB)
  - 10,000 node hours on Fritz
- **Software Requirements:**
  - C++ Compiler
  - Nonlinear optimization library (NLopt)
- **Expected Outcome:** Phase diagram for TRR 306 grant, leading to a publication.

## Actions Taken
- **HPC Admin:** Enabled the user's HPC account on Fritz.

## Lessons Learned
- **Account Activation:** Ensure that user accounts are promptly enabled upon request.
- **Resource Allocation:** Understand and document the specific resource requirements for different types of workloads.
- **Software Installation:** Note that users may install their own software libraries in their home directories.
- **Research Outcomes:** Be aware of the expected outcomes and their significance to the user's research projects.

## Root Cause of the Problem
- User needed access to the Fritz cluster for specific computational tasks.

## Solution
- HPC Admin enabled the user's account on the Fritz cluster.

## Future Reference
- For similar requests, ensure that the account is activated and the necessary resources are allocated as per the user's requirements.
- Document any special software installations or configurations needed by the user.
---

### 2022032942002542_Job%20Performance%20auf%20Fritz%20%7C%20iwpa79.md
# Ticket 2022032942002542

 # HPC Support Ticket: Job Performance auf Fritz | iwpa79

## Keywords
- Job Performance
- OpenFoam
- MPI Processes
- Slurm Cluster
- srun
- mpirun
- NUMA Domain
- Monitoring
- Scalability Tests

## Summary
The user experienced poor job performance on the Fritz cluster, particularly with OpenFoam jobs. The monitoring showed unstable metrics, which were suspected to be related to the binding of MPI processes on the nodes.

## Root Cause
The user's job submission command `mpirun -np 2304 -npernode 72 pisoFoam ...` resulted in processes being pinned to NUMA domains instead of individual cores.

## Solution
The HPC Admin recommended using `srun` instead of `mpirun` for better process pinning. Alternatively, using `mpirun pisoFoam` without the `-np` and `-npernode` options was suggested.

## Actions Taken
1. **User Response**: The user agreed to try the recommended alternatives and provided job IDs for comparison.
2. **Monitoring**: The user was advised to check the monitoring tool to view job performance metrics.
3. **Scalability Tests**: The HPC Admin suggested performing scalability tests with different node counts to improve efficiency.

## Additional Notes
- The use of `srun` is generally recommended on Slurm clusters to avoid unintended results from the combination of Slurm and `mpirun`.
- The monitoring tool can be accessed at [monitoring.nhr.fau.de](https://monitoring.nhr.fau.de) using the HPC account.
- The jobs were not close to hardware limits, indicating potential for optimization through scalability tests.

## Conclusion
Using `srun` or adjusting the `mpirun` command can improve job performance by ensuring proper process pinning. Scalability tests can further optimize resource usage.
---

### 2023072442002337_Regarding%20hpc%20problems.md
# Ticket 2023072442002337

 # HPC Support Ticket Analysis: Regarding HPC Problems

## Keywords
- MPI-IO issue
- NFS mounting
- Vault storage
- VTK files
- Simulation freezes
- POSIX-IO
- Parallel filesystem

## Problem Summary
- User encounters intermittent issues with simulations on the Meggie cluster.
- Errors occur especially when writing VTK files to the vault directory.
- Simulations sometimes freeze without outputting to log files or VTK folders.
- User's colleagues do not face similar issues.

## Root Cause
- The issue is likely related to MPI-IO and the way the vault directory is mounted.
- The vault is not mounted with the 'noac' option, which can cause problems with MPI-IO.

## Solution Attempts
- Initial suggestion to use `$FASTTMP` was not feasible as it is no longer available on Meggie.
- Recommendation to revert to POSIX-IO where only one process performs IO.
- Suggestion to move to a cluster with a parallel filesystem, such as Fritz.

## Steps for User
1. **Use POSIX-IO**: Modify the simulation to use POSIX-IO instead of MPI-IO.
2. **Move to a Different Cluster**: Consider moving simulations to a cluster with a parallel filesystem, like Fritz.

## Additional Notes
- The issue is intermittent and does not affect all users, making it challenging to diagnose.
- The vault directory is not guaranteed to work with MPI-IO due to its mounting configuration.

## Conclusion
- The user should try using POSIX-IO or move to a cluster with a parallel filesystem to resolve the intermittent simulation issues.

---

This documentation can be used to address similar issues in the future by referring to the steps and recommendations provided.
---

### 2024031942004511_Tier3-Access-Fritz%20%22Amritanshu%20Verma%22%20_%20ihpc130h.md
# Ticket 2024031942004511

 ```markdown
# HPC Support Ticket Conversation Analysis

## Keywords
- Account activation
- Fritz cluster
- Single-node throughput
- Multi-node workload
- Molecular dynamics simulations
- GROMACS
- Benchmarking
- Energy consumption

## Summary
- **User Request**: Access to Fritz cluster for PhD work involving benchmarking molecular dynamics simulations using GROMACS.
- **Requirements**:
  - Single-node throughput (72 cores, 250 GB)
  - Multi-node workload (HDR100 Infiniband with 1:4 blocking; per node: 72 cores, 250 GB)
  - 1000 node hours
- **Expected Outcome**: Energy consumption data from various benchmarking simulations.

## Root Cause of the Problem
- User needed access to the Fritz cluster for specific computational resources and software.

## Solution
- **HPC Admin Action**: Account enabled on Fritz cluster.

## General Learnings
- Proper justification is required for single-node throughput requests.
- Multi-node workloads need to specify interconnect and blocking details.
- Benchmarking and energy consumption studies are common use cases for HPC resources.
- GROMACS is a frequently used software for molecular dynamics simulations.
```
---

### 2024110842002429_a100multi%20access%20for%20CEEC-LSTM%20-%20EuroHPC%20Center%20of%20Excellence%20for%20Exascale%20CFD.md
# Ticket 2024110842002429

 # HPC Support Ticket: a100multi Access for CEEC-LSTM

## Keywords
- Multi-node access
- QoS specification
- GPU resources
- Neko module
- A100multi
- A40multi
- ClusterCockpit
- Job scheduling

## Summary
The user encountered an issue with submitting multi-node jobs due to an invalid QoS specification. The user's project had 40,000 GPU-hours allocated but was unable to request more than one node.

## Root Cause
- The user's account was not eligible for the `a100multi` QoS.
- The user had used negligible GPU resources, making it difficult for the admin to assess the need for multi-node access.
- ClusterCockpit was down, preventing the admin from checking the user's previous jobs.

## Solution
- The HPC Admin activated multi-node access for the user's project (`b237dc`) after reviewing the provided single-node job IDs.
- The user was informed that scheduling multi-node jobs may require more time as multiple complete nodes need to become available.
- The Neko module was removed from Alex as it was compiled without MPI enabled on the device, affecting performance.
- The user was granted access to submit jobs with multiple A40 nodes, with the caveat that the interconnect of the A40 nodes is weaker than that of the A100 nodes.

## General Learnings
- Multi-node access is not activated by default and requires admin intervention.
- Providing single-node job IDs similar to the intended multi-node jobs can help the admin make an informed decision.
- The interconnect speed of different node types can affect job performance.
- Self-built binaries may not require a module on the cluster if they are widely used within a project.

## Follow-up
- The user should communicate the changes to all colleagues involved in the project.
- The user should be aware of the interconnect speed differences between A100 and A40 nodes when submitting multi-node jobs.
---

### 2024090242003229_Tier3-Access-Fritz%20%22Matthias%20Walther%22%20_%20mpt1014h.md
# Ticket 2024090242003229

 ```markdown
# HPC Support Ticket: Tier3-Access-Fritz

## Keywords
- HPC Account Activation
- Fritz Cluster
- Single-Node Throughput
- C++, Boost, Eigen
- Quantum Magnets
- Ordinary Differential Equations
- OMP Parallel
- Memory Requirements
- Node Hours

## Summary
- **User Request**: Access to Fritz cluster for single-node throughput with special justification (72 cores, 250 GB).
- **Software Needed**: C++, Boost, Eigen.
- **Application**: Solving large sets of ordinary differential equations for quantum magnets.
- **Expected Results**: Higher system sizes and higher quality data for future publications.

## Root Cause
- User requires additional computational resources and memory not available on their current system (Meggie).

## Solution
- HPC Admin enabled the user's account on Fritz.

## Lessons Learned
- Users may need access to more powerful clusters for specific computational tasks.
- Proper justification and resource allocation are necessary for enabling access to advanced HPC resources.
- Communication between users and HPC Admins is crucial for understanding and fulfilling computational needs.
```
---

### 2023112142005573_Multi-Node%20GPU%20Training%20-%20p102eb10.md
# Ticket 2023112142005573

 # Multi-Node GPU Training Issue

## Keywords
- Multi-Node Jobs
- GPU Training
- Batch Job Submission
- Node Count Specification
- Partition Configuration
- QoS (Quality of Service)
- OpenMPI

## Problem
- **Root Cause:** User attempted to submit a multi-node job but received an error due to the partition configuration limiting the maximum number of nodes to 1.
- **Error Message:** `sbatch: error: Batch job submission failed: Node count specification invalid`

## Solution
- **Admin Action:** Multi-node jobs need to be enabled per account. The admin enabled this feature for the user's account.
- **User Instructions:**
  - Use `--qos=a100multi` for multi-node jobs to access up to 8 nodes.
  - Ensure exclusive node usage with `--gres=gpu[:a100]:8`.
  - If using OpenMPI, utilize one of the 4.1.6 modules.

## General Learnings
- Multi-node jobs may require specific permissions and configurations.
- Understanding partition configurations is crucial for job submissions.
- Proper QoS and resource specifications are necessary for successful job submissions.
- Specific modules may be required for certain software tools like OpenMPI.
---

### 2023050942003261_WRF%20jobs%20on%20fritz%20-%20gwgk002h%20_%20b128dc.md
# Ticket 2023050942003261

 # HPC Support Ticket: WRF Jobs on Fritz

## Keywords
- WRF jobs
- Resource utilization
- Submit script
- MPI processes
- OpenMP
- OMP_PLACES
- OMP_STACKSIZE
- Scalability
- Performance optimization

## Problem
- User's job did not efficiently utilize resources on the 'fritz' hardware.
- Submit script was not optimized for the hardware with 72 cores per node.

## Root Cause
- Suboptimal submit script for the given hardware.
- Potential issues with OpenMP stack memory.

## Solutions Provided
1. **Submit Script Optimization**:
   - HPC Admin provided four new submit scripts tailored for the 'fritz' hardware.
   - Suggested testing all scripts with short runs to determine the most suitable one.

2. **Resource Utilization**:
   - Advised testing with a single node first to find the best configuration.
   - Recommended scaling up the number of nodes only if a speedup is observed.

3. **OpenMP Configuration**:
   - Suggested changing `OMP_PLACES=sockets` to `OMP_PLACES=cores` in the submit scripts.
   - Advised setting `OMP_STACKSIZE` to avoid potential crashes with many OpenMP threads.
     ```bash
     export OMP_STACKSIZE=500m
     ```
   - Noted that `ulimit -s unlimited` may also be necessary for some runs.

## General Learnings
- Always ensure submit scripts are tailored to the specific hardware.
- Test different configurations to find the optimal setup.
- Be mindful of OpenMP settings like `OMP_PLACES` and `OMP_STACKSIZE` to avoid performance issues and crashes.
- Scale up resources only if it results in a performance improvement.

## Next Steps for User
- Test the provided submit scripts with short runs.
- Adjust OpenMP settings as suggested.
- Monitor performance and scale up resources if beneficial.
---

### 2023041142004141_OOM-Kill%20on%20woody.md
# Ticket 2023041142004141

 ```markdown
# HPC-Support Ticket: OOM-Kill on woody

## Keywords
- OutOfMemory-kill
- H5 files
- Python
- Memory flags
- Large files

## Problem Description
- User is attempting to merge multiple H5 files into a single large file.
- The process is being terminated by an OutOfMemory-kill.
- The output file size at the time of the kill is approximately 21GB.
- User has tried various memory flags without success.

## Root Cause
- The issue is likely due to an inefficient implementation in Python, leading to high memory usage.
- The output indicates that 121.3 GiB out of the requested 128 GiB (94.8%) of RAM is being used.

## Solution
- The filesystem supports much larger files than a few GB.
- The problem is related to the Python implementation.
- Reference to a previous HPC Cafe talk on Python and performance: [HPC Cafe Talk](https://hpc.fau.de/2023/03/13/monthly-hpc-cafe-python-and-performance-march-21-hybrid-event/)

## General Learnings
- Large file operations in Python can lead to high memory usage.
- Efficient memory management is crucial for handling large files.
- Reviewing and optimizing Python code can help prevent OutOfMemory-kill issues.
- The filesystem is not the limiting factor for large file sizes.
```
---

### 2021100642004241_Likwid%20Pin%20for%20distributing%20pinning%20on%20meggie.md
# Ticket 2021100642004241

 ```markdown
# HPC-Support Ticket: Likwid Pin for Distributing Pinning on Meggie

## Subject
Issue with pinning OpenMP threads to sockets using `likwid-pin`.

## User Issue
- **Problem**: User encounters a warning when trying to pin 2 OpenMP threads each to S0 and S1.
  - Warning: `WARN: Selected affinity domain S1 has only -1 hardware threads, but selection string evaluates to 1 threads.`
- **Root Cause**: Incorrect CPU selection for `likwid-pin`.

## HPC Admin Response
- **Explanation**: The user's CPU selection for `likwid-pin` was incorrect. The logical pinning inside affinity domains like `S0:0` should refer to the first indexed CPU in the CPU list of `S0`.
  - Domain `S0`: 0,1,2,3,4,5,6,7,8,9
  - Domain `S1`: 10,11,12,13,14,15,16,17,18,19
  - The user's selection contained `S1:10`, which is outside of the `S1` list, causing a divide-by-zero error.

## Solution
- **Correct Pinning Expression**: Use `S0:0@S1:0` to select the first physical HW thread of both sockets, `S0` and `S1`.
- **SLURM Configuration**:
  - Use `srun -n 1 -c 2 --cores-per-socket=1 likwid-pin -c S0:0@S1:0 ./hello` to specify the resources.
  - Alternatively, use `--cpu-bind=none` to disable SLURM's affinity mechanism, which was interfering with `likwid-pin`.
  - Example: `srun --cpu-bind=none likwid-pin -c S0:0@S1:0 ./hello`

## Additional Notes
- **likwid-mpirun**: Uses `--cpu_bind=none` as well, so it should work without additional flags.
- **Domain Listing**: The CPUs get listed in `S1` if:
  - `--cpu-bind=none` is added.
  - `--cpus-per-task` is either omitted from the batch script or set to a value other than 2.

## Conclusion
- The issue was resolved by correcting the CPU selection and adjusting the SLURM configuration to avoid interference with `likwid-pin`.
```
---

### 2023042642004051_SSDs%20auf%20Fritz%3F.md
# Ticket 2023042642004051

 ```markdown
# HPC Support Ticket: SSDs auf Fritz?

## Keywords
- SSDs
- Fritz Cluster
- /scratch
- /dev/sda3
- Documentation
- System-SSD
- DWPD

## Problem
- User noticed the presence of `/scratch` on node `f0819`, which corresponds to `/dev/sda3`.
- The documentation for the Fritz cluster does not mention local SSDs on the nodes.

## Root Cause
- The Fritz nodes have a system SSD with limited capacity (240 GB) and durability (0.3 DWPD).
- The documentation omits mentioning these SSDs due to their limitations.

## Solution
- The system SSDs are primarily for logs and other system-related tasks.
- Users should avoid heavy usage of these SSDs due to their limited capacity and durability.

## Additional Information
- User mentioned a tool being developed at TU Dresden: [ratarmount](https://github.com/mxmlnkn/ratarmount).

## Conclusion
- The SSDs on Fritz nodes are not intended for extensive user data storage.
- Users should be cautious about the capacity and durability limitations of these SSDs.
```
---

### 42055055_Neueres%20Java%20auf%20woody.md
# Ticket 42055055

 # HPC Support Ticket: Newer Java on Woody

## Keywords
- Java Development Kit (JDK)
- NUMA support
- Performance improvement
- Default version update

## Summary
A user requested an update to a newer version of the JDK on the HPC system "woody" to take advantage of NUMA support.

## Root Cause
- The current JDK version did not support NUMA, leading to suboptimal performance for the user's application.

## Solution
- HPC Admins installed JDK 1.6 Update 21, which includes NUMA support.
- The user tested the new version and reported significant performance improvements.
- The new JDK version was set as the default on "woody".

## Details
- **User Request:** Install JDK 1.6 Update 18 or newer for NUMA support.
- **Admin Action:** Installed JDK 1.6 Update 21 and created a module for it.
- **User Feedback:** Performance improved from 43 seconds to 8-9 seconds using the `-XX:+UseNUMA` option.
- **Admin Follow-up:** Made JDK 1.6 Update 21 the default version on "woody".

## Lessons Learned
- Updating software versions can significantly improve performance, especially when new features like NUMA support are utilized.
- User testing and feedback are crucial for validating the effectiveness of software updates.
- Setting updated software versions as default can benefit all users of the HPC system.
---

### 2024082042003385_Tier3-Access-Fritz%20%22Georgios%20Vakalopoulos%22%20_%20iwia108h.md
# Ticket 2024082042003385

 # HPC Support Ticket Analysis

## Keywords
- Tier3 Access
- Fritz
- iwia108h
- Multi-node workload
- HDR100 Infiniband
- Intel OneAPI suite
- SYCL code
- Performance analysis
- waLBerla application

## Summary
- **User Request:** Access to Fritz for multi-node workload with specific hardware and software requirements.
- **Hardware Requirements:** HDR100 Infiniband with 1:4 blocking, 72 cores, 250 GB per node.
- **Software Requirements:** Intel OneAPI suite compatible with SYCL code.
- **Application:** Performance analysis on Intel CPU using SYCL-ported code.
- **Expected Outcome:** Performance metrics from waLBerla application.

## Actions Taken
- **HPC Admin:** Granted access to Fritz for the specified user.

## Lessons Learned
- **Access Granting:** Ensure proper communication and documentation when granting access to HPC resources.
- **Resource Allocation:** Understand and document the specific hardware and software requirements for user requests.
- **Application Support:** Be prepared to support performance analysis tasks and specific software suites like Intel OneAPI.

## Root Cause
- User required access to specific HPC resources for performance analysis.

## Solution
- Access granted to Fritz for the specified user with the required resources.

## Follow-Up
- Ensure the user is aware of the granted access and any further steps required for their workload.
- Monitor resource usage and provide support as needed for the performance analysis task.
---

### 2020011042001344_Job%20auf%20Emmy%3A%201217388%20%28iwpa048h%29.md
# Ticket 2020011042001344

 ```markdown
# HPC Support Ticket: Job auf Emmy: 1217388 (iwpa048h)

## Keywords
- Job Efficiency
- Resource Allocation
- Script Analysis
- Processor Utilization

## Problem Description
The user's job on Emmy is utilizing only 4 out of the 6 requested nodes, with a total of 146 processes. This indicates inefficient resource usage.

## Root Cause
- The job script requests 210 processes, but internally, the job is not utilizing all requested resources.
- Possible copy-paste error in job configuration, leading to inconsistent resource requests.

## Analysis
- HPC Admins reviewed the job script and found that the user frequently switches between different node counts.
- The script requests 210 processes but does not fully utilize them.

## Solution
- Advise the user to ensure full utilization of requested resources or adjust the resource request accordingly.
- Review job scripts for consistency and correct resource allocation.

## References
- Job Info Links:
  - [Job 1217388](https://www.hpc.rrze.fau.de/HPC-Status/job-info.php?USER=iwpa048h&JOBID=1217388&ACCESSKEY=cb6d782a&SYSTEM=EMMY)
  - [Job 1217425](https://www.hpc.rrze.fau.de/HPC-Status/job-info.php?USER=iwpa048h&JOBID=1217425&ACCESSKEY=e3135a11&SYSTEM=EMMY)
  - [Job 1218568](https://www.hpc.rrze.fau.de/HPC-Status/job-info.php?USER=iwpa048h&JOBID=1218568&ACCESSKEY=32100b3b&SYSTEM=EMMY)

## General Learning
- Regularly monitor job efficiency to ensure optimal resource utilization.
- Review job scripts for consistency in resource requests.
- Provide guidance to users on efficient resource allocation.
```
---

### 42074092_FASTEST%20SegFault%20auf%20LiMa.md
# Ticket 42074092

 ```markdown
# HPC-Support Ticket: Segmentation Fault on LiMa

## Subject
FASTEST SegFault auf LiMa

## User Issue
- User encountered a segmentation fault (SIGSEGV) when running a job with 8 MPI tasks.
- The job worked with 4 MPI tasks and multiple threads.
- The error occurred during MPI startup, with tasks exiting before completion.
- Attempts to generate a core file were unsuccessful.

## Batch Script
```bash
#!/bin/bash -l
#PBS -l nodes=4:ppn=24,walltime=01:00:00
#PBS -N FFSdnsHYB
#source /apps/rrze/etc/use-rrze-modules.sh
cd $PBS_O_WORKDIR
/apps/rrze/bin/mpirun_rrze-intelmpd -intelmpi -np 8 -npernode 2 -pin "0,1,2,3,4,5 6,7,8,9,10,11" ./fhp.intel64shrmpi < ffs10.fls > dump_hyb
```

## Error Message
```
forrtl: severe (174): SIGSEGV, segmentation fault occurred
...
mpiexec-0.84-lima: Warning: tasks 0-1,3 exited before completing MPI startup.
mpiexec-0.84-lima: Warning: tasks 2,6 exited before completing MPI startup.
mpiexec-0.84-lima: Warning: tasks 4-5,7 exited before completing MPI startup.
```

## HPC Admin Response
- The issue was specific to a particular input.
- To enable core dumps, add `limit coredumpsize unlimited` temporarily in `.cshrc`.
- Compile with `-traceback -g` to make the code location traceable.

## Keywords
- Segmentation Fault
- SIGSEGV
- MPI Startup
- Core Dump
- Traceback
- Input Specific

## Lessons Learned
- Segmentation faults can be input-specific.
- Enable core dumps by setting `limit coredumpsize unlimited` in `.cshrc`.
- Use `-traceback -g` during compilation to trace the code location causing the fault.
```
---

### 2022121442000742_Ressourcennutzung%20auf%20Fritz%20-%20NHR%40FAU%20_%20b122bd11.md
# Ticket 2022121442000742

 ```markdown
# HPC Support Ticket: Resource Usage on Fritz - NHR@FAU

## Keywords
- Resource allocation
- Job script optimization
- ClusterCockpit
- HPC-Portal
- Rechenzeitbudget

## Problem
- User's jobs are using only 6 cores and up to 20 GB of memory per node.
- Each node on Fritz has 72 cores and 250 GB of memory.
- Inefficient resource usage leading to unnecessary consumption of the user's compute budget.

## Solution
- HPC Admin advised the user to bundle multiple calculations into a single job script to improve resource utilization.
- User was directed to monitor job data via ClusterCockpit accessible through the HPC-Portal.

## Actions Taken
- HPC Admin provided guidance on efficient resource usage.
- No response from the user; no compute activity recorded since December.
- Ticket closed with a note to continue discussion in a linked ticket.

## Lessons Learned
- Users should be aware of the resource allocation granularity on Fritz (whole nodes or multiples thereof).
- Bundling multiple calculations into a single job script can optimize resource usage and reduce the consumption of the compute budget.
- Monitoring tools like ClusterCockpit are available for users to track their job performance and resource usage.
```
---

### 2020113042002028_Node%20allocation%20on%20emmy%20%7C%20mptf005h.md
# Ticket 2020113042002028

 ```markdown
# HPC Support Ticket: Node Allocation Issue

## Keywords
- Node allocation
- Job script
- mpirun
- -npernode argument
- Compute nodes

## Problem
- User's job is using less than half of the allocated compute nodes.

## Root Cause
- The variable `N` in the job script was not adapted to the increased number of nodes.

## Solution
- Cancel the current job.
- Adapt the variable `N` in the job script to the increased number of nodes.
- If the lower number of processes was intentional, distribute them evenly to the compute nodes by using the `-npernode` argument for `mpirun`.

## General Learning
- Ensure that job scripts are configured to utilize the allocated compute nodes efficiently.
- Use the `-npernode` argument for `mpirun` to distribute processes evenly across nodes if fewer processes are intended.

## Actions Taken
- HPC Admin informed the user about the issue and provided a solution.
- User acknowledged the information.
- Ticket closed as resolved.
```
---

### 2018073042002175_cluster%20queue.md
# Ticket 2018073042002175

 # HPC Support Ticket Analysis

## Keywords
- Cluster queue
- Job submission
- Running jobs
- Special user
- Cluster availability

## Summary
A user submitted a job to the LiMa cluster, but it remained in the queue. The user observed that only jobs from a single user (iwst031h) were running and inquired about the special status of this user and the estimated availability of the cluster.

## Root Cause
- Job stuck in queue
- Potential resource monopolization by a single user

## What Can Be Learned
- **Job Queue Management**: Understanding how jobs are managed in the queue and why some jobs might be delayed.
- **Resource Allocation**: Identifying if certain users have priority access to cluster resources.
- **Cluster Availability**: Estimating when the cluster will be available for other users.

## Solution (if found)
- Investigate the status of the job queue and the running jobs.
- Check if the user (iwst031h) has special permissions or priority.
- Provide an estimate for when the cluster will be available for other jobs.

## Next Steps
- HPC Admins should review the job queue and resource allocation policies.
- Communicate with the user about the current status and expected availability.

---

This documentation can help support employees understand and resolve similar issues related to job queues and resource allocation on the cluster.
---

### 2024060742001352_Tier3-Access-Fritz%20%22Kai%20He%22%20_%20btr0110h.md
# Ticket 2024060742001352

 # HPC Support Ticket: Tier3-Access-Fritz

## Keywords
- Tier3 Access
- Account Enablement
- Fritz HPC
- Python3
- Topic Modeling
- Natural Language Processing (NLP)

## Summary
- **User Request**: Access to Tier3 resources on Fritz HPC for topic modeling using Python3.
- **Resources Requested**:
  - Single-node throughput (72 cores, 250 GB)
  - 24,000 node hours
- **Application**: Topic modeling for text analysis.
- **Expected Results**: Topics for the given text.

## Conversation Highlights
- **HPC Admin**: Informed the user that their HPC account has been enabled on Fritz.
- **User**: Acknowledged the enablement and thanked the HPC Admin.

## Lessons Learned
- **Process**: Tier3 access requests require special justification and approval.
- **Communication**: Clear and timely communication between the user and HPC Admin is crucial for account enablement.
- **Resource Allocation**: Proper documentation of resource requirements and expected outcomes is essential for granting access.

## Root Cause of the Problem
- User needed access to Tier3 resources for a specific computational task.

## Solution
- HPC Admin enabled the user's account on Fritz after reviewing the request and justification.

## Documentation for Future Reference
- Ensure that users provide detailed justification for Tier3 access requests.
- Confirm that the required resources and software are available on the HPC system.
- Maintain clear communication with users regarding the status of their requests and account enablement.
---

### 2020021842000838_VASP%20Jobs%20on%20Emmy%20%281240550%2C..%20mpap001h%29.md
# Ticket 2020021842000838

 # HPC Support Ticket: VASP Jobs on Emmy

## Keywords
- VASP jobs
- Computational performance
- PPN (processors per node)
- NCORE
- Resource utilization
- Benchmarking

## Problem Description
- User's VASP jobs on Emmy were underperforming and not utilizing all available resources.
- Specifically, jobs were using only half of the available cores and memory.

## Root Cause
- The user was setting `ppn=10` instead of `20`, leading to underutilization of resources.

## Solution
- The user performed benchmarking tests with different `ppn` and `NCORE` settings.
- Based on the results, the user decided to continue with `ppn=20` and `NCORE=5` for optimal performance.

## Benchmarking Results
```
(ppn, NCORE) = (10, 1):  ELAPSED TIME (sec) = 7005.451,
(ppn, NCORE) = (10, 5):  ELAPSED TIME (sec) = 7189.019,
(ppn, NCORE) = (10,10):  ELAPSED TIME (sec) = 7712.396,
(ppn, NCORE) = (20, 1):  ELAPSED TIME (sec) = 7432.741,
(ppn, NCORE) = (20, 5):  ELAPSED TIME (sec) = 4821.705,
(ppn, NCORE) = (20,10):  ELAPSED TIME (sec) = 4987.107,
(ppn, NCORE) = (20,20):  ELAPSED TIME (sec) = 5688.797.
```

## Recommendations
- HPC Admins recommend using `PPN=20` and `NCORE=10` as a 'failsafe' setting.
- The user was also informed about the availability of the Meggie cluster for potentially faster calculations.

## General Learnings
- Proper configuration of `ppn` and `NCORE` is crucial for optimal performance of VASP jobs.
- Benchmarking with different settings can help identify the best configuration for specific workloads.
- Regular monitoring of job performance and resource utilization can help identify and address inefficiencies.
---

### 2024091142003177_HPC-Build-_Jobsetup%20und%20LIKWID-Anbindung.md
# Ticket 2024091142003177

 # HPC-Support Ticket Conversation: HPC-Build-/Jobsetup und LIKWID-Anbindung

## Keywords
- HPC-Build-/Jobsetup
- LIKWID-Anbindung
- Apptainer
- Slurm
- LIKWID-Bridge
- perf_event
- Singularity
- Container
- Job Submission
- Debug Output
- Zoom Meeting

## General Learnings
- **Container Setup**: Ensure that the code is included in the container along with dependencies.
- **Job Submission**: Use `salloc` with appropriate flags (`-c`, `--exclusive`, `-p`, `-C`) to allocate resources.
- **LIKWID Integration**: Use `ACCESSMODE=perf_event` for LIKWID within containers.
- **Debugging**: Check debug outputs for socket connections and ensure all threads are properly configured.
- **Collaboration**: Schedule meetings for detailed troubleshooting and guidance.

## Root Cause of the Problem
- **LIKWID Bridge Issue**: The LIKWID bridge socket connection was not functioning as expected, leading to incomplete measurements.
- **Job Submission Error**: The Slurm job was not configured to access multiple CPU cores, causing issues with multi-threaded execution.

## Solutions
- **LIKWID Bridge**: Use `ACCESSMODE=perf_event` for LIKWID within containers to avoid bridge issues.
- **Job Submission**: Ensure the Slurm job is configured with `-c` to allocate the required number of CPU cores.
- **Debugging**: Analyze debug outputs for socket connections and ensure all threads are properly configured.

## Detailed Conversation

### Initial Issue
- User had issues with LIKWID integration in a container and job submission using Slurm.

### Steps Taken
1. **Container Setup**:
   - HPC Admin suggested including the code (`rtgi-code`) in the container along with dependencies.
   - Test the container on a frontend before submitting a job.

2. **Job Submission**:
   - HPC Admin provided a sample Slurm job submission command:
     ```bash
     $ salloc -t 04:00:00 --exclusive -c 72 -p singlenode -C "hwperf"
     $ singularity shell testcontainer.sif
     ```
   - Ensure the job is configured to access multiple CPU cores.

3. **LIKWID Integration**:
   - HPC Admin suggested using `ACCESSMODE=perf_event` for LIKWID within containers:
     ```bash
     git clone https://github.com/RRZE-HPC/likwid.git
     cd likwid
     make PREFIX=/usr ACCESSMODE=perf_event
     make PREFIX=/usr ACCESSMODE=perf_event install
     ```
   - This allows LIKWID to perform measurements within the container.

4. **Debugging**:
   - User encountered issues with multi-threaded execution.
   - HPC Admin analyzed debug outputs and suggested ensuring all threads are properly configured.

5. **Collaboration**:
   - HPC Admin scheduled Zoom meetings for detailed troubleshooting and guidance.

### Final Resolution
- **LIKWID Bridge**: Use `ACCESSMODE=perf_event` to avoid bridge issues.
- **Job Submission**: Ensure the Slurm job is configured with `-c` to allocate the required number of CPU cores.
- **Debugging**: Analyze debug outputs for socket connections and ensure all threads are properly configured.

This report provides a detailed overview of the steps taken to resolve the user's issues with LIKWID integration and job submission on an HPC system. It can be used as a reference for similar issues in the future.
---

### 2024031842004451_WG%3A%20W%202%20Schneider%2C%20NF%20Amft%20-%20W%202%20sF%20mit%20TT%20W%203.md
# Ticket 2024031842004451

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject
WG: W 2 Schneider, NF Amft - W 2 sF mit TT W 3

## Keywords
- Hochleistungscomputercluster
- Datenanalyse
- Simulationen
- Eigene Knotenpunkte
- Core Hours
- FAU
- NHR@FAU
- Zentralisierung
- HPC-Grundversorgung

## Problem
- User requests access to HPC clusters for data analysis and simulations.
- Specifically asks for "eigene Knotenpunkte" (dedicated nodes) and approximately 1 million core hours per year.

## Root Cause
- Unclear definition of "eigene Knotenpunkte."
- Need for dedicated resources and specific core hours.

## Solution
- Clarification that dedicated nodes are likely not feasible.
- Confirmation that 1 million core hours per year is manageable within existing resources.
- Suggested response emphasizing the centralized HPC resources available at NHR@FAU.

## What Can Be Learned
- **Resource Allocation**: Understanding the feasibility of allocating dedicated nodes versus shared resources.
- **Core Hours Management**: Assessing the capacity of existing HPC clusters to meet specific core hour requirements.
- **Communication**: Crafting clear and informative responses to user requests, highlighting available resources and institutional policies.

## Example Response
"Die FAU betreibt seit sehr vielen Jahren eine erfolgreiche (re)Zentralisierung der Hochleistungsrechner. Am NHR@FAU stehen für die HPC-Grundversorgung ausreichend Ressourcen niederschwellig zur Verfügung, um 1 Mio Core-h pro Jahr zur Verfügung stellen zu können."
```
---

### 2019120842000135_Alternative%20zu%20memoryhog%3F.md
# Ticket 2019120842000135

 # HPC Support Ticket: Alternative zu memoryhog?

## Keywords
- memoryhog
- meggie
- meggie2
- load average
- responsiveness
- RAM
- ulimit
- open files

## Problem
- User needs an alternative to `memoryhog` for running a job that requires 13 GB RAM but not much CPU time.
- `memoryhog` is unresponsive due to high load (average > 200).
- User's jobs on `meggie` are delayed due to the unresponsiveness of `memoryhog`.
- User tried `meggie2` but encountered limits on the number of open files (1024 on `cshpc` and frontends, 8192 on `memoryhog`).

## Root Cause
- High load on `memoryhog` causing unresponsiveness.
- Insufficient ulimit settings for open files on `meggie2`.

## Solution
- HPC Admin increased the ulimit for open files on `meggie2` to 4096.
- User was advised to try running the job on `meggie2` with the increased ulimit.

## General Learnings
- High load on a specific node can cause delays and unresponsiveness.
- ulimit settings for open files can be a limiting factor for certain jobs.
- HPC Admin can adjust ulimit settings to accommodate user needs.
- It's important to consider the impact on other users when adjusting resource limits.
---

### 2020010942002006_terrible%20performance%20of%20jobs%20on%20Emmy%20_%20iwsp004h.md
# Ticket 2020010942002006

 # HPC Support Ticket Analysis: Poor Job Performance on Emmy / iwsp004h

## Keywords
- Performance issues
- MPI processes
- Memory bandwidth
- Floating point operations
- MPI library
- Array jobs
- Monitoring system

## Summary
- **Issue**: User's jobs on Emmy cluster exhibiting poor performance.
- **Symptoms**:
  - Low memory bandwidth usage (max 250 MB/s out of 80,000 MB/s).
  - Low floating point operations (max 700 MFlop/s out of 500,000 MFlop/s).
  - Over 70% of cycles spent in MPI library.
- **Root Cause**: Inefficient use of resources, possibly due to suboptimal MPI configuration or code inefficiency.
- **Solution**: Not explicitly stated, but further discussion and appointment with HPC Admins suggested for performance improvement.

## Lessons Learned
- Monitor job performance metrics such as memory bandwidth and floating point operations.
- High percentage of cycles spent in MPI library indicates potential communication bottlenecks.
- Engage with HPC Admins for detailed performance analysis and optimization strategies.
- Ensure array jobs are properly supported in the monitoring system for better tracking and analysis.

## Next Steps
- Schedule an appointment with HPC Admins to discuss performance optimization.
- Review MPI configuration and code efficiency.
- Implement changes based on the discussion and monitor performance improvements.
---

### 2024071242000636_Multi-node%20A40%20jobs%20f%C3%83%C2%BCr%20DAREXA-F%20%28b182dc%29.md
# Ticket 2024071242000636

 # HPC Support Ticket: Multi-node A40 Jobs for DAREXA-F

## Keywords
- Multi-node jobs
- A40 nodes
- A100 nodes
- Ethernet networking
- MPI partitioned communication
- Bandwidth
- QoS (Quality of Service)

## Problem
- User requested multi-node access for A40 nodes for the DAREXA-F project.
- Multi-node jobs were already approved for A100 nodes but not for A40 nodes.

## Root Cause
- A40 nodes have limited Ethernet networking and are not typically suited for multi-node jobs.

## User Workload
- MPI partitioned communication with compression.
- Benchmarking with a maximum of 2 nodes.
- Reproducible bandwidth is acceptable even with slower Ethernet.

## Solution
- HPC Admins granted the project (`b182dc`) access to multi-node jobs on A40 nodes with the QoS setting `--qos=a40multi`.

## General Learnings
- A40 nodes are not ideal for multi-node jobs due to limited Ethernet networking.
- Understanding the specific workload requirements is crucial for determining the suitability of different node types.
- QoS settings can be adjusted to allow multi-node jobs on specific node types.

## Next Steps
- Monitor the performance of multi-node jobs on A40 nodes.
- Provide feedback to HPC Admins if further adjustments are needed.

## References
- [HPC Support Email](mailto:support-hpc@fau.de)
- [HPC Website](https://hpc.fau.de/)
---

### 2020012042002217_Empire-Jobs%20auf%20Emmy%20-%20bca109.md
# Ticket 2020012042002217

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject: Empire-Jobs auf Emmy - bca109

### Keywords:
- MPI processes
- Job scheduling
- Load balancing
- Hybrid computing
- IntelMPI
- Job monitoring

### Summary:
The user was experiencing issues with their jobs on the Emmy HPC system. The HPC Admin identified that the MPI processes were not being distributed correctly across nodes, leading to high load on a single node.

### Root Cause:
- The user was starting all MPI processes on the first node using `mpiexec -np 16`, which caused excessive load on that node.
- The user assumed that IntelMPI would automatically distribute processes in a round-robin fashion, which was not the case.

### Solution:
- The HPC Admin advised the user to explicitly specify hybrid computing and limit the number of MPI processes per node.
- The user acknowledged the issue and agreed to modify their job scripts accordingly.

### Lessons Learned:
- Always explicitly specify the distribution of MPI processes across nodes to avoid overloading a single node.
- Regularly monitor job performance and load distribution to ensure efficient use of HPC resources.
- Documentation and assumptions about default behaviors should be verified with actual implementation.

### Follow-up:
- The HPC Admin noted that even after the user made changes, some jobs were still not performing optimally. Further investigation and adjustments may be needed.
```
---

### 2022020342000719_Re%3A%20%5BRRZE-HPC%5D%20Call%20for%20early-adopter%20of%20parallel%20computer%20Fritz.md
# Ticket 2022020342000719

 ```markdown
# HPC Support Ticket Conversation Analysis

## Keywords
- Early Adopter
- Fritz
- Python3/Anaconda
- Gurobi
- Julia
- CPU Hours
- Consultation
- License Server
- NFS Server
- IO Rate
- GFlop/s
- Workflow Changes

## General Learnings
- **Early Adopter Process**: Activation of early-access accounts is fast (~1 day).
- **Software Installation**: Users can install needed software in user mode if central installation takes time.
- **License Server**: The HPC team does not run the license server for Gurobi.
- **CPU Hours**: No strict limits for early-access, but consultation may be required for significant CPU hours.
- **Job Performance**: Jobs causing high IO rates and low GFlop/s may require optimization before moving to Fritz.
- **Workflow Changes**: Single-core jobs need to be adapted to the full-node granularity of Fritz.

## Root Cause of the Problem
- **High IO Rate**: Jobs causing constant outgoing network rate of >6 MB/s per node, potentially overloading NFS servers.
- **Low Performance**: Jobs only doing about 10 GFlop/s per node, indicating inefficient use of resources.
- **Single-Core Jobs**: Jobs running on single cores need to be adapted to full-node granularity.

## Solution
- **Consultation**: Required before moving to Fritz to address high IO rates and low performance.
- **Workflow Adaptation**: Jobs need to be optimized to utilize full nodes efficiently.
```
---

### 2023042642002517_Tier3-Access-Fritz%20%22Christian%20Greff%22%20_%20iww8008h.md
# Ticket 2023042642002517

 # HPC Support Ticket Analysis: Resource Management Issue with Python Program

## Keywords
- Python program
- Resource management
- Job submission
- Process stalling
- Idle cores
- Monitoring data
- Workload reorganization
- Master-worker scheme

## Summary
A user's Python program, acting as a resource management tool for job submission, was causing inefficiencies in resource usage. The program initially spawned a large number of processes, which decreased over time, but often led to stalling or idle cores.

## Root Cause
- Inefficient resource management by the user's Python program.
- Poor handling of process completion, leading to stalling and idle cores.

## Observed Issues
- Initial spawning of 400 processes.
- Decrease to 20 processes after half an hour.
- Stalling of the Python program or delayed completion of some processes, causing idle cores.

## Suggested Solutions
- **HPC Admin**: Suggested showing the user monitoring data and asking for workload reorganization.
  - Identify long-running tasks and group them together.
  - Implement a real master-worker scheme to balance the load.

## Actions Taken
- **HPC Admin**: Contacted the user and provided suggestions for improvement.
- The ticket was closed after notifying the user, although no response was received.

## General Learnings
- Monitoring user jobs can help identify inefficiencies in resource usage.
- Providing users with monitoring data and suggestions can help improve job efficiency.
- Implementing proper master-worker schemes can prevent resource wastage.

## Follow-up
- If similar issues arise, monitor the user's jobs and provide specific suggestions for improvement based on the observed data.
---

### 2023072142002815_Node%27s%20reservation%20on%20Fritz%20%2B%20temporary%20change%20in%20Sapphire%20Rapid%20nodes%20lim.md
# Ticket 2023072142002815

 # HPC Support Ticket Analysis

## Subject
Node's reservation on Fritz + temporary change in Sapphire Rapid nodes limit

## Keywords
- Node reservation
- Fritz nodes
- Icakelae
- Sapphire Rapid
- DRAM power
- Node limit
- Experimental setup

## Summary
The user requested reservations on two Fritz nodes (one with Icakelae and one with Sapphire Rapid) due to variations in DRAM power and the need for extended run times. Additionally, the user requested a temporary increase in the Sapphire Rapid nodes limit from 8 to 16 to rerun an experimental setup.

## Root Cause
- Variations in DRAM power across nodes.
- Script execution time exceeding the allotted 24 hours.
- Unexpected variations in experimental results requiring a rerun.

## Solution
- HPC Admins created reservations for the user: `ReservationName=ihpc040h_spr` and `ReservationName=ihpc040h_icx`.
- The node limit for Sapphire Rapid nodes was temporarily increased to 16.
- The reservations were later canceled upon user confirmation that they were no longer needed.

## General Learnings
- Users may require specific node reservations due to hardware variations.
- Temporary adjustments to node limits can be made to accommodate experimental needs.
- Regular follow-ups are necessary to ensure reservations are still required and to free up resources when no longer needed.

## Actions Taken
- Created node reservations.
- Temporarily increased node limit.
- Followed up with the user to confirm completion and cancel reservations.

## Follow-Up
- Ensure that the node limit is reverted to its original setting after the temporary increase.
- Confirm that the cancellation of reservations does not impact currently running scripts.
---

### 2024061242003957_Long%20Waiting%20Time.md
# Ticket 2024061242003957

 ```markdown
# HPC-Support Ticket: Long Waiting Time

## Keywords
- Job Queue
- Waiting Time
- Fair-Share System
- GPU Hours
- Priority Flag

## Problem Description
- User's jobs are not getting allocated and have been queued for a long time.
- Previously, the waiting period was shorter.
- The issue started last week.

## Root Cause
- High number of active users leading to all nodes being filled with jobs.
- User has a low priority due to extensive use of GPU hours in the past.
- Fair-share system in place, which lowers priority for users who have used the system more.

## Solution
- User needs to wait until other users have finished their jobs.
- Understanding of the fair-share system and its impact on job priority.

## General Learnings
- The cluster operates on a fair-share system, where heavy users get lower priority.
- Long waiting times can be due to high demand and active users.
- Users should be aware of their usage and the impact on their job priority.

## Notes
- The user was running jobs on 3 GPUs and had used a significant amount of GPU hours.
- The fair-share system ensures that all users get a chance to access resources.
```
---

### 2024042642002775_Tier3-Access-Fritz%20%22Venkata%20Naga%20Satya%20Sai%20Ravi%20Kiran%20Ayyala%20Somayajula%22%20_%20i.md
# Ticket 2024042642002775

 ```markdown
# HPC Support Ticket Conversation Analysis

## Subject
Tier3-Access-Fritz "Venkata Naga Satya Sai Ravi Kiran Ayyala Somayajula" / iwia052h

## Keywords
- Tier3 Access
- Fritz Cluster
- Account Activation
- Single-node Throughput
- Multi-node Workload
- Rechenzeit
- WALBERLA
- EXASTENCILS
- Performance Simulations

## Summary
- **Request**: User requested access to the Fritz cluster for performance simulations of charged particles applications.
- **Requirements**:
  - Single-node throughput (72 cores, 250 GB)
  - Multi-node workload (HDR100 Infiniband with 1:4 blocking; per node: 72 cores, 250 GB)
  - Rechenzeit: 1000 node hours
  - Software: WALBERLA, EXASTENCILS
- **Expected Outcome**: Performance plots and other performance metrics for a publication.

## Actions Taken
- **HPC Admin**: Requested account activation.
- **HPC Admin**: Confirmed account activation for the Fritz cluster.

## Lessons Learned
- **Account Activation Process**: Understanding the steps involved in activating a user account for a specific cluster.
- **Resource Allocation**: Importance of specifying resource requirements clearly, including single-node and multi-node workloads.
- **Software Requirements**: Ensuring that the required software (WALBERLA, EXASTENCILS) is available and accessible for the user.
- **Communication**: Effective communication between the user and HPC support team for resource allocation and account activation.

## Root Cause of the Problem
- User needed access to the Fritz cluster for specific computational tasks.

## Solution
- HPC Admin activated the user's account for the Fritz cluster, allowing them to proceed with their computational tasks.
```
---

### 2024103042002853_Tier3-Access-Fritz%20%22Robert%20Lahmann%22%20_%20mpp130.md
# Ticket 2024103042002853

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Keywords
- HPC Access
- Multi-node Workload
- HDR100 Infiniband
- MEEP
- MPI
- Simulation
- Radio Signals
- RNO-G Detector
- Funding Request

## Summary
A user requested access to the HPC system for a multi-node workload involving simulations of radio signals in ice using MEEP and MPI software. The user specified the required resources and expected outcomes, including the potential for further funding requests.

## Details
- **User Request:**
  - Multi-node workload with HDR100 Infiniband (1:4 blocking)
  - 72 cores and 250 GB per node
  - 10,000 node hours on Fritz
  - Required software: MEEP, MPI
  - Application: Simulations of radio signal propagation in ice for the RNO-G detector
  - Expected results: Reproduction of recorded data and simulations for the RNO-G detector
  - Additional notes: Simulation results to be used for a funding request to employ a Ph.D. student

- **HPC Admin Response:**
  - User granted access to the HPC system (Fritz)
  - Ticket closed after access was granted

## Lessons Learned
- **Access Request Process:**
  - Users can request access to HPC resources by specifying their needs, including hardware requirements, software, and expected outcomes.
  - HPC Admins review and grant access based on the provided information.

- **Resource Allocation:**
  - Users should clearly specify their resource requirements, such as node hours, cores, and memory.
  - Specifying the software needed (e.g., MEEP, MPI) helps in ensuring the environment is correctly set up.

- **Application and Outcomes:**
  - Detailing the application and expected outcomes aids in understanding the purpose and importance of the workload.
  - Additional notes, such as the potential for funding requests, provide context for the importance of the simulation results.

## Conclusion
This ticket conversation demonstrates the process for requesting and granting access to HPC resources. It highlights the importance of clear communication regarding resource requirements, software needs, and the purpose of the workload.
```
---

### 2023080742000502_Half%20precision%20auf%20Fritz%3F.md
# Ticket 2023080742000502

 ```markdown
# HPC-Support Ticket Conversation: Half Precision Support on Fritz

## Keywords
- Half precision
- Bfloat16
- Ice Lake
- Sapphire Rapids
- Vector instructions
- Performance testing
- DFG-Projekt

## Summary
A user inquired about the support for half precision, specifically bfloat16, on the Fritz cluster, which is based on Ice Lake architecture. The user mentioned an upcoming DFG project that requires performance testing with bfloat16.

## Problem
- **Root Cause**: The user needed to know if the Fritz cluster supports bfloat16 for performance testing in an upcoming DFG project.

## Solution
- **HPC Admin Response**: Ice Lake architecture does not support bfloat16. However, the Fritz cluster also includes 64 Sapphire Rapids nodes, which do support bfloat16.
- **CPUID Flags for Sapphire Rapids**: The admin provided a list of CPUID flags for Sapphire Rapids, highlighting the support for `avx512_bf16` and `amx_bf16`.

## Conclusion
The user was informed that Sapphire Rapids nodes on the Fritz cluster support bfloat16, making them suitable for the user's performance testing needs.

## General Learning
- **Architecture-Specific Features**: Different CPU architectures have varying support for vector instructions and precision formats.
- **Cluster Configuration**: The Fritz cluster includes nodes with different architectures, allowing for flexibility in supporting various computational needs.
- **Communication**: Effective communication between users and HPC admins is crucial for understanding and addressing specific computational requirements.
```
---

### 2025031342001862_KONWIHR-III%3A%20Dynamics%20of%20Complex%20Fluids%20-%20iwmm100.md
# Ticket 2025031342001862

 # HPC-Support Ticket Conversation: KONWIHR-III Dynamics of Complex Fluids - iwmm100

## Keywords
- KONWIHR-III
- Dynamics of Complex Fluids
- Lattice Boltzmann
- Performance Optimization
- Profiling
- Benchmarks
- LIKWID
- Skylake
- Rome Dual Socket
- AVX512
- Gitlab
- Videokonferenz
- BBB
- Zoom

## Summary
The conversation revolves around a new KONWIHR project focusing on the dynamics of complex fluids using Lattice Boltzmann methods. The project aims to optimize performance, particularly in high-parallel and complex simulation scenarios.

## Root Cause of the Problem
- Performance degradation in high-parallel execution.
- Inefficient use of AVX512 on Skylake chips.
- Lack of detailed profiling and benchmarks for complex scenarios.

## Solutions and Actions Taken
- **Profiling and Benchmarks**: Identify critical code sections and develop practical benchmarks.
- **AVX512 Optimization**: Disable AVX512 on Skylake chips due to performance issues.
- **Collaboration**: Schedule meetings to define clear performance goals and develop a roadmap.
- **Code Access**: Provide access to the code repository on Gitlab for further analysis.

## General Learnings
- **Performance Optimization**: Understanding the performance characteristics of different CPU architectures is crucial.
- **Collaboration**: Regular meetings and clear communication are essential for project success.
- **Profiling Tools**: Tools like LIKWID are valuable for identifying performance bottlenecks.
- **Benchmarking**: Developing practical and representative benchmarks is key to measuring and improving performance.

## Next Steps
- Define clear performance goals.
- Develop and run benchmarks to identify performance bottlenecks.
- Continue collaboration through regular meetings and videoconferences.
- Optimize code based on profiling results.

## Additional Notes
- The project is part of the KONWIHR campaign 2024/1.
- The code is currently hosted on a Gitlab server and is not publicly accessible.
- The team prefers videoconferencing for regular communication.

---

This report provides a concise summary of the HPC-Support Ticket conversation, highlighting the key issues, solutions, and next steps for the KONWIHR-III project on the dynamics of complex fluids.
---

### 2023053142001793_Re%3A%20%5BNHR%40FAU%5D%20Info%20Verf%C3%83%C2%BCgbarkeit%20SPR%20High%20Memory%20Knoten%20auf%20Fri.md
# Ticket 2023053142001793

 # HPC Support Ticket Conversation Analysis

## Keywords
- High-memory nodes
- SPR Knoten
- Fritz Cluster
- NHR@FAU Projekt
- Freischalten
- Intel Xeon Platinum 8470
- DDR5 RAM
- hpc-support@fau.de

## Summary
- **User Request:** Access to high-memory nodes for a specific project.
- **HPC Admin Response:** Access granted for the specified project.

## What Can Be Learned
- **Availability of High-Memory Nodes:** The Fritz Cluster has 64 high-memory nodes, with 48 nodes having 1 TB DDR5 RAM and 16 nodes having 2 TB DDR5 RAM.
- **Processor Specifications:** Each node is equipped with two Intel Xeon Platinum 8470 “Sapphire Rapids” processors with 52 cores each.
- **Job Limits:** Up to eight SPR1TB or two SPR2TB nodes can be requested per job.
- **Access Procedure:** Users can request access to these nodes via a formless email to hpc-support@fau.de.
- **Support Availability:** The NHR@FAU Support Team is available to assist with any questions regarding the use of HPC systems and the porting of applications to Fritz and Alex.

## Root Cause of the Problem
- The user needed access to high-memory nodes for their project.

## Solution
- The HPC Admin granted access to the high-memory nodes for the specified project.

## Documentation for Support Employees
- **Requesting Access to High-Memory Nodes:** Users can send a formless email to hpc-support@fau.de to request access to high-memory nodes for their projects.
- **Node Specifications:** High-memory nodes are equipped with Intel Xeon Platinum 8470 processors and either 1 TB or 2 TB DDR5 RAM.
- **Job Limits:** Users can request up to eight SPR1TB or two SPR2TB nodes per job.

This documentation can be used to assist users in requesting access to high-memory nodes and to provide information about the specifications and limits of these nodes.
---

### 2022102742000589_Cluster%20tinyx.md
# Ticket 2022102742000589

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject: Cluster tinyx

### Keywords:
- Slurm
- Threads per node
- Maintenance
- Batch script
- OpenMP
- srun

### Problem:
- User reports that their code, which previously ran with 128 threads per node, now runs with only 1 thread per node on the cluster tinyx.
- Issue started after recent maintenance.

### Root Cause:
- A bug in the new Slurm version installed during maintenance caused the `--cpus-per-task=128` option not to be correctly propagated to the `srun` command.

### Solution:
- Workaround provided: Add the `--cpus-per-task=128` option directly to the `srun` call in the batch script.

### Lessons Learned:
- Maintenance activities can introduce bugs in software versions.
- It's important to verify that resource allocation options are correctly propagated after updates.
- Users should be aware of potential issues after maintenance and be prepared to adjust their scripts accordingly.

### Example Batch Script Adjustment:
```bash
#!/bin/bash -l
#SBATCH --clusters tinyfat
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=128
#SBATCH --time=24:00:00
#SBATCH --job-name=output
#SBATCH --error=output-%j.err
#SBATCH --output=output-%j.out
#SBATCH --mail-type=ALL
#SBATCH --export=NONE
#SBATCH --exclusive

unset SLURM_EXPORT_ENV

module load boost/1.74.0-gcc9.3
module load hdf5/1.10.7-gcc9.3-openmpi
module load cmake/3.18.4
module load gcc/10.2.0
module load openmpi/3.1.6-gcc9.3
module load mkl/2019.5
module load fftw/3.3.8-gcc9.3-openmpi

cd "${SLURM_SUBMIT_DIR}"

srun --cpus-per-task=128 /home/hpc/mptf/mptf007h/boltzmann/quantum_boltz_noise_omp_parallel_omega_fermion.ex /home/vault/mptf/mptf007h/boltzmann_CDW/TEST_ANTONIO/param_boltz_226.in
```

### Conclusion:
- The issue was resolved by adding the `--cpus-per-task=128` option to the `srun` command, ensuring the correct number of threads were allocated.
- Future maintenance should include thorough testing of resource allocation to prevent similar issues.
```
---

### 2020101842000439_Resource%20temporarily%20unavailabe%2C%20STAR-CCM%2B%202020.2.md
# Ticket 2020101842000439

 # HPC-Support Ticket: Resource Temporarily Unavailable, STAR-CCM+ 2020.2

## Keywords
- Resource temporarily unavailable
- STAR-CCM+
- Login nodes
- Gittergenerierung (Mesh generation)
- Memoryhog
- HPC account sharing

## Summary
A user encountered an error while attempting to generate a mesh for a simulation using STAR-CCM+ on the HPC system. The error message indicated that the resource was temporarily unavailable. The issue was caused by running resource-intensive processes on the login nodes, which are shared resources for all HPC users.

## Root Cause
- Running resource-intensive tasks (mesh generation) on login nodes, which are not designed for such operations.
- Misunderstanding about the appropriate use of HPC resources.

## Solution
- **Do not use login nodes for resource-intensive tasks**: Login nodes are shared resources and should not be used for tasks like mesh generation.
- **Use appropriate nodes for mesh generation**: The user was advised to use the `memoryhog` node for mesh generation, which had been successfully used in the past.
- **Account sharing**: HPC accounts are personal and should not be shared. If multiple users need access, each should apply for their own account.

## General Learnings
- **Login Node Usage**: Login nodes are for lightweight tasks such as job submission, file management, and compiling code. Resource-intensive tasks should be submitted to compute nodes.
- **Resource Allocation**: Understand the appropriate nodes for different tasks to avoid disrupting other users.
- **Account Management**: Ensure that HPC accounts are not shared and that each user has their own account for proper resource management and security.

## Follow-up Actions
- **Documentation**: Ensure that the correct procedures for using different nodes are documented and communicated to users.
- **Training**: Provide training on the appropriate use of HPC resources to prevent similar issues in the future.

## Closure
The ticket was closed as the user understood the correct procedure for mesh generation and the importance of not using login nodes for resource-intensive tasks. No further action was required.
---

### 2024111142001898_Inquiry%20regarding%20multinode%20limit%20on%20Alex.md
# Ticket 2024111142001898

 # HPC Support Ticket: Inquiry regarding multinode limit on Alex

## Summary
User inquires about multinode limits for A100 and A40 nodes on Alex.

## Keywords
- Multinode limit
- A100 nodes
- A40 nodes
- Slurm
- Job scheduling
- Node allocation

## Problem
- User requests access to 8 A100 multinodes for educational and PhD work.
- User observes `QOSMaxNodePerJobLimit` in the job priority column.
- User's jobs for 8 A100 and 8 A40 nodes were allocated fewer nodes than requested.

## Root Cause
- The system allows jobs with up to 8 nodes (64 GPUs).
- Large jobs disrupt scheduling and are allowed in rare cases.
- Current queue has jobs with 300x A100 waiting, making it unrealistic to schedule an 8-node job with only 10 minutes runtime.

## Solution
- User should submit the job and wait for it to be executed.
- User should expect a wait time of up to 1-2 days due to priority and availability.
- User should verify node allocation and job statistics to ensure correct resource usage.

## Additional Information
- User's batch script specifies 8 GPUs per node and 8 nodes.
- ClusterCockpit shows that both jobs received their 8 nodes, but user's logs indicate fewer nodes were used.
- User will investigate the discrepancy, possibly related to pinning.

## Conclusion
- User understands the multinode limit and the impact of large jobs on scheduling.
- User will keep the job in the queue and verify resource allocation.
- Ticket can be closed as the original question about the multinode limit has been answered.
---

### 42161830_Linux%20Testcluster.md
# Ticket 42161830

 ```markdown
# HPC Support Ticket: Linux Testcluster Job Delay

## Keywords
- Linux Testcluster
- Job Queue
- Wartungsarbeiten (Maintenance)
- Warteschleife (Queue)

## Problem Description
- User reports that jobs submitted to the Linux Testcluster are stuck in the queue.
- Both larger and smaller test jobs are affected.
- User inquires about potential maintenance activities on the cluster.

## Root Cause
- No maintenance activities were being conducted.
- Another job was running on the node, causing the user's jobs to remain in the queue.

## Solution
- No specific action was required from the user.
- The HPC Admin confirmed that the cluster was functioning normally and that the delay was due to another job occupying the node.

## General Learnings
- Job delays in the queue can occur due to other jobs running on the cluster.
- Users should be aware that job scheduling can be affected by the workload of other users.
- Regular communication with HPC Admins can help clarify the status of job queues and cluster operations.

## References
- HPC Services, Friedrich-Alexander-Universitaet Erlangen-Nuernberg
- Regionales RechenZentrum Erlangen (RRZE)
```
---

### 2020052942001491_Jobs%20on%20emmy%20-%20iwpa014h.md
# Ticket 2020052942001491

 # HPC Support Ticket: Jobs on emmy - iwpa014h

## Keywords
- Process placement
- OpenFoam jobs
- Empty nodes
- mpirun options
- `--bind-to core`
- `-npernode 20`

## Problem Description
The user's recent OpenFoam jobs on the HPC system "emmy" were experiencing issues with process placement, resulting in some nodes being completely empty.

## Root Cause
The exact root cause was not explicitly stated, but it was related to the process placement configuration of the jobs.

## Solution
The HPC Admin suggested two potential solutions:
1. Adding the `--bind-to core` option to the job script.
2. Using the `-npernode 20` option for mpirun to ensure proper process distribution across nodes.

The user confirmed they would add the suggested mpirun option to their script.

## Outcome
The ticket was closed after the HPC Admin observed that the recent jobs appeared to be running correctly, indicating that the suggested solution was effective.

## General Learnings
- Proper configuration of process placement is crucial for efficient resource utilization in HPC jobs.
- The `--bind-to core` and `-npernode` options can help ensure that processes are evenly distributed across available nodes.
- Collaboration between users and HPC support can help identify and resolve job configuration issues.
---

### 2022121542000375_HPC-Kursaccounts%20und%20Reservierung%20Fritz%20f%C3%83%C2%BCr%2011.-13.01.23.md
# Ticket 2022121542000375

 # HPC Support Ticket Analysis

## Subject
HPC-Kursaccounts und Reservierung Fritz für 11.-13.01.23

## Keywords
- HPC-Kursaccounts
- Reservierung
- Fritz
- LIKWID Engineering
- Slurm
- NIS
- ReservationName
- StartTime
- EndTime
- Duration
- Nodes
- NodeCnt
- CoreCnt
- Features
- PartitionName
- Flags
- TRES
- Users
- Groups
- Accounts
- Licenses
- State
- BurstBuffer
- Watts
- MaxStartDelay

## Summary
A request was made for 50 HPC course accounts with access to Fritz for a LIKWID Engineering course. The duration of the accounts was from January 1, 2023, to January 13, 2023. Additionally, a reservation for 50 Fritz nodes was requested for January 11, 12, and 13, from 14:00 to 22:00.

## Root Cause
The user needed HPC course accounts and node reservations for a specific training session.

## Solution
1. **Account Data**: Account data was sent via chat to the requester.
2. **Slurm Activation**: Accounts were activated in Slurm once they were known in NIS.
3. **Reservations**: Reservations were created for the specified dates and times.
   - **Reservation Details**:
     - **Day 1**: January 11, 2023, 14:00-22:00, 45 nodes, 3240 cores.
     - **Day 2**: January 12, 2023, 14:00-22:00, 45 nodes, 3240 cores.
     - **Day 3**: January 13, 2023, 14:00-22:00, 45 nodes, 3240 cores.

## General Learnings
- **Account Management**: Ensure account data is sent and accounts are activated in Slurm.
- **Reservation Setup**: Create reservations with specific details including start time, end time, nodes, and cores.
- **Communication**: Use chat or other communication methods to share account data with the requester.

## Notes
- The reservations were set up with specific flags such as OVERLAP, IGNORE_JOBS, SPEC_NODES, and MAGNETIC.
- The state of the reservations was initially set to INACTIVE.

This documentation can be used as a reference for setting up course accounts and reservations for future requests.
---

### 2022052542002493_Bitte%20Jobpriorit%C3%83%C2%A4t%20auf%20Alex%20anpassen.md
# Ticket 2022052542002493

 ```markdown
# HPC Support Ticket: Job Priority Adjustment

## Keywords
- Job priority
- Job overtaking
- HPC Admin
- User request

## Summary
A user requested to prioritize a specific job (ID: 297107) so that it would overtake their other waiting jobs on the HPC system.

## Root Cause
The user needed a specific job to be processed ahead of their other pending jobs.

## Solution
The HPC Admin adjusted the job priority as requested and informed the relevant personnel via chat.

## General Learning
- Users may request job prioritization for specific tasks.
- HPC Admins can adjust job priorities to meet user needs.
- Communication with relevant personnel is important for ensuring smooth operations.
```
---

### 2023112442002089_Problems%20with%20VASP%20and%20XTB%20jobs%20-%20b163cb15.md
# Ticket 2023112442002089

 # HPC Support Ticket: Problems with VASP and XTB Jobs

## Keywords
- VASP
- XTB
- Turbomole
- Job Termination
- Memory Issues
- Parallelization
- ClusterCockpit
- Monitoring

## Summary
- **VASP Job Issue**: JobId=1016304 did not terminate normally.
- **XTB Job Issue**: JobId=1016274 and JobId=1016270 had parallelization issues.

## Root Cause
- **VASP Job**: Unknown issue causing job termination.
- **XTB Job**: Incorrect parallelization settings leading to inefficient core usage.

## Solution
- **VASP Job**: Restarting the job resolved the issue. Increasing `NCORE` in `INCAR` to 36 may help with memory issues.
- **XTB Job**: Ensure jobs run on a single node (72 cores) for parallelization. Use ClusterCockpit to monitor CPU load and verify core usage.

## Steps Taken
1. **HPC Admin**: Notified user about job issues and provided initial troubleshooting steps.
2. **User**: Restarted VASP job and adjusted XTB job settings.
3. **HPC Admin**: Provided instructions on using ClusterCockpit for monitoring CPU load.

## Lessons Learned
- **VASP Jobs**: Restarting can sometimes resolve one-time issues. Adjusting `NCORE` can help with memory problems.
- **XTB Jobs**: Ensure proper parallelization settings. Use monitoring tools to verify core usage.
- **General**: Use ClusterCockpit for monitoring job performance and resource usage.

## Resources
- [ClusterCockpit](https://portal.hpc.fau.de/)
- [Monitoring System](https://monitoring.nhr.fau.de/monitoring/user/b163cb15)

## Follow-up
- Monitor VASP jobs for recurring issues.
- Verify XTB jobs are utilizing all available cores on a single node.

---

This documentation can be used to troubleshoot similar issues with VASP and XTB jobs in the future.
---

### 2024052842003554_Gro%C3%83%C2%9Fer%20Benchmark%20Run%20Fritz.md
# Ticket 2024052842003554

 # HPC-Support Ticket Conversation Analysis

## Keywords
- Benchmark Run
- Fritz
- Nodes
- Partition
- Reservation
- Slurm
- Job Submission
- Error Messages
- Reboot
- Load
- MPI Processes
- Binary
- Job Cancellation
- Timeout
- Task Launch
- Killed Tasks

## General Learnings
- **Communication and Collaboration**: The conversation highlights the importance of clear and timely communication between users and HPC admins.
- **Resource Management**: Understanding the limits and configurations of partitions and nodes is crucial for efficient job submission.
- **Troubleshooting**: Identifying and resolving issues related to job submission, task launch, and node management requires a systematic approach.
- **Documentation**: Accurate and up-to-date documentation is essential for users to understand the system's capabilities and limitations.

## Root Cause of Problems
1. **Typo in Configuration**: Initial issues were due to a typo in the configuration file.
2. **Partition Limits**: The user encountered errors due to exceeding the node limits of the 'big' partition.
3. **Job Cancellation**: The job was not properly cancelled, leading to nodes being stuck.
4. **High Load**: High load on a specific node (atuin) caused issues with MPI processes.

## Solutions
1. **Correct Typo**: The HPC admin corrected the typo in the configuration file.
2. **Reboot Nodes**: The admin rebooted a large number of nodes to resolve the issue with stuck jobs.
3. **Restart Slurm**: A restart of Slurm was required to apply the new configuration.
4. **Monitor Load**: The admin identified high load on a specific node and took appropriate actions.

## Detailed Analysis

### Initial Request
- **User**: Requested a benchmark run with more than 64 nodes for a project.
- **HPC Admin**: Provided instructions to submit jobs with up to 256 nodes using `--reserversion=HEISSRISSE --partition=big`.

### Configuration Issue
- **User**: Encountered an error due to a typo (`--reserversion` instead of `--reservation`).
- **HPC Admin**: Corrected the typo and confirmed that jobs with up to 512 nodes should be possible.

### Partition Limits
- **User**: Encountered an error when submitting a job with more than 256 nodes.
- **HPC Admin**: Confirmed that the 'big' partition limit was increased to 512 nodes after a Slurm restart.

### Job Cancellation Issue
- **User**: Encountered a timeout error during task launch and had to manually cancel the job.
- **HPC Admin**: Rebooted a large number of nodes to resolve the issue with stuck jobs.

### High Load Issue
- **HPC Admin**: Identified high load on a specific node (atuin) and took appropriate actions.

### Final Status
- **User**: Confirmed that the job with 512 nodes was successful.
- **HPC Admin**: Asked about additional jobs and the need for the reservation.

This analysis provides a comprehensive overview of the issues encountered and the steps taken to resolve them, serving as a valuable resource for future troubleshooting.
---

### 2024102042000632_Tier3-Access-Fritz%20%22Ekkehard%20Steinmacher%22%20_%20iwia116h.md
# Ticket 2024102042000632

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Keywords
- Tier3 Access
- Fritz
- Multi-node workload
- HDR100 Infiniband
- PICLas library
- Master's thesis
- Installation
- Compilation
- Testing

## Summary
- **User Request**: Access to Fritz for multi-node workload using PICLas library for a master's thesis.
- **Requirements**:
  - Multi-node workload with HDR100 Infiniband (1:4 blocking)
  - 72 cores and 250 GB per node
  - 40 node hours
  - Software: PICLas library
- **Purpose**: Installation, compilation, and testing of PICLas library for thesis work.

## Outcome
- **HPC Admin Response**: User granted access to Fritz with the specified account.

## Lessons Learned
- **Access Request Process**: Users can request access to specific HPC resources by providing detailed requirements and justifications.
- **Resource Allocation**: HPC Admins review and approve resource requests based on provided details.
- **Software Installation**: Users may need to install and test specific software libraries for their projects.

## Root Cause of the Problem
- User needed access to Fritz for thesis work involving multi-node workloads and specific software.

## Solution
- HPC Admin granted access to the user, allowing them to proceed with their project.
```
---

### 2022120142003399_regarding%20multiple%20node%20access.md
# Ticket 2022120142003399

 # HPC Support Ticket: Multiple Node Access

## Keywords
- Multiple node access
- waLBerla simulations
- Fritz cluster
- Node limits
- Tier3 service
- NHR project

## Problem
- User needs access to multiple nodes for running simulations on waLBerla.
- Requires information on the procedure and maximum number of nodes available.

## Solution
- **Tier3 Service**: Limit of 24 nodes for all jobs running simultaneously. Individual limit depends on other jobs in the group.
- **NHR Project**: If included in an NHR project, the limit is 64 nodes per job.

## Notes
- User should contact the relevant project leader for inclusion in the NHR project to access more nodes.
- The HPC Admin provided information on node limits and the procedure for accessing multiple nodes.

## Action Items
- User to follow up with the project leader for NHR project inclusion if more nodes are required.
- HPC Admin to monitor and manage node allocations based on current usage and project requirements.

## Additional Information
- **Contact**: HPC Support at `support-hpc@fau.de`
- **Website**: [FAU HPC](https://hpc.fau.de/)

This documentation can be used as a reference for future support tickets related to multiple node access and node limits on the Fritz cluster.
---

### 2022060942001451_Fritz%20Singlenode%20ReqNodeNotAvail.md
# Ticket 2022060942001451

 ```markdown
# HPC Support Ticket: Fritz Singlenode ReqNodeNotAvail

## Keywords
- Fritz-Cluster
- Single-node Jobs
- ReqNodeNotAvail
- UnavailableNodes
- Hardwarewartung
- sinfo
- MOTD

## Problem Description
- User unable to submit single-node jobs on Fritz-Cluster.
- Error message: "ReqNodeNotAvail, UnavailableNodes:f0812".
- Multinode jobs are running without issues.
- Same problem experienced by another user.

## Root Cause
- Single-node partition nodes are currently unavailable due to hardware maintenance.

## Solution
- Wait for the nodes to become available again.
- Check the status of nodes using the `sinfo` command.
- Monitor the Message of the Day (MOTD) for updates on node availability.

## General Learnings
- Regular maintenance can affect node availability.
- Use `sinfo` to check node status.
- MOTD provides important updates on system status.
```
---

### 2021062242001605_problem%20with%20fftw3%20on%20the%20tinyfat%20cluster.md
# Ticket 2021062242001605

 ```markdown
# HPC Support Ticket Conversation Summary

## User Information
- **Name:** Antonio Picano
- **Affiliation:** Physics Department, FAU Erlangen-Nürnberg
- **Supervisor:** Prof. Eckstein

## Issue Description
The user encountered issues with linking the FFTW library and running parallel code on the tinyfat cluster. The main problems were related to understanding OpenMP parallelization, nested parallelism, and the correct usage of FFTW and MKL libraries.

## Key Points Addressed
1. **OpenMP Threads Configuration:**
   - The user was advised to define the number of OpenMP threads in the environment using `#define NUM_THREADS 64` and `omp_set_num_threads(NUM_THREADS)`.
   - The user was informed about the correct usage of `srun` to avoid running the code multiple times unintentionally.

2. **Nested OpenMP Parallelism:**
   - The user was informed about the potential issues with nested OpenMP parallelism when calling threaded libraries inside a parallel region.
   - The user was advised to enforce the library to not use OpenMP to avoid overloading the cores.

3. **FFTW and MKL Libraries:**
   - The user was advised to use the FFTW interface of the MKL library for better performance.
   - The user was informed about the correct linking of the FFTW library in the Makefile.

4. **Performance Issues:**
   - The user observed performance degradation when running parallel code compared to serial code.
   - The user was advised to manually time function calls to understand the performance bottlenecks.

## Resolution
The HPC Admins provided detailed guidance on configuring OpenMP, avoiding nested parallelism, and using the correct libraries. They also profiled the user's code to identify performance bottlenecks and provided suggestions for improvement.

## Next Steps
The user was advised to attend OpenMP courses and consider applying for help through KONWHIR to further improve their understanding and implementation of parallel programming.

## Conclusion
The user's issues were addressed through detailed explanations and suggestions from the HPC Admins. The user was encouraged to continue learning and improving their parallel programming skills.
```
---

### 2024011142001184_Meggie%20down.md
# Ticket 2024011142001184

 # HPC Support Ticket: Meggie Cluster Node Availability

## Keywords
- Meggie cluster
- Node availability
- Power management
- Job scheduling
- Deadlines

## Problem
- **User Report:** 480 nodes down on the Meggie cluster, only 180 allocated, none idle for jobs.
- **Root Cause:** Nodes were powered down before the holiday break to save energy due to low utilization.

## Solution
- **Admin Action:** Nodes were powered up again as needed to accommodate user jobs.
- **User Feedback:** Confirmed that jobs started running after additional nodes were brought online.

## General Learnings
- **Energy Management:** Nodes may be powered down during periods of low utilization to save energy.
- **Communication:** Users should be informed about power management practices to avoid confusion.
- **Job Scheduling:** Users with deadlines should communicate their needs to ensure adequate resources are available.

## Follow-up Actions
- **Documentation:** Update user documentation to include information about energy-saving measures and their impact on node availability.
- **Monitoring:** Regularly monitor cluster utilization to ensure that nodes are powered up as needed to meet user demands.
---

### 2018032742001402_mediocre%20performance%20of%20psi4%20jobs%20on%20Meggie%20_%20bctc009h.md
# Ticket 2018032742001402

 ```markdown
# HPC Support Ticket: Mediocre Performance of psi4 Jobs on Meggie

## Keywords
- psi4 jobs
- Meggie
- mediocre performance
- job optimization
- HPC monitoring
- appointment scheduling
- job graphs
- compute resources

## Summary
The user's psi4 jobs on Meggie were showing mediocre performance. The HPC Admin noticed phases where the jobs were not utilizing all compute resources efficiently. The user was advised to make an appointment to discuss possible improvements.

## Problem
- **Root Cause**: The psi4 jobs had phases where only the first node was working, leading to underutilization of compute resources.
- **Symptoms**: Approximately 40% of compute resources were unused during certain phases of the job runtime.

## Solution
- **Appointment Scheduling**: The user was advised to schedule an appointment with the HPC support team to discuss the job behavior and potential improvements.
- **Job Monitoring**: The user was provided with a link to view job graphs and an AccessKey to monitor job performance.
- **Optimization**: The user planned to optimize the jobs to reduce waiting time on the rest of the nodes.

## Follow-Up
- The user agreed to optimize the jobs after the holidays.
- The HPC Admin noted that some jobs showed improved performance (~20% more Flops/s), but it was unclear if the user had made specific optimizations.

## General Learnings
- **Job Monitoring**: Utilize job graphs and monitoring tools to identify performance issues.
- **Appointment Scheduling**: Schedule appointments with the HPC support team for in-depth analysis and optimization discussions.
- **Resource Utilization**: Ensure that jobs are efficiently utilizing all allocated compute resources to avoid underutilization.
```
---

### 2016042842001108_jobs%20auf%20Emmy.md
# Ticket 2016042842001108

 # HPC Support Ticket: Job Queue Delays on Emmy

## Keywords
- Job queue
- Fairshare
- Defective nodes
- Prioritization

## Problem
- User's simulations stuck in the queue for days despite available nodes.
- User needs simulations for manuscript completion.

## Root Cause
- Defective or crashed nodes not distinguishable from free nodes in user view.
- Fairshare policy allocating significant compute time to user's group.

## Solution
- HPC Admin prioritized specific jobs (587267, 587271, 587595) for the user.
- User informed about fairshare data and node status visibility issue.

## General Learnings
- Users may not be aware of fairshare policies and node health status.
- Communication about job prioritization and resource allocation is crucial.
- Addressing user concerns promptly can prevent delays in research outputs.

## Ticket Status
- Closed: User satisfied with the resolution.
---

### 2020021242001526_Meggie.md
# Ticket 2020021242001526

 ```markdown
# HPC Support Ticket: Meggie Frontend Performance Issue

## Keywords
- Meggie
- Frontend
- Performance
- Slow
- CPU Usage
- Process `reconstructPar`

## Summary
A user reported that the frontends on Meggie were extremely slow. Another user had a process `reconstructPar` running that was consuming 100% CPU.

## Root Cause
- High CPU usage by a specific process (`reconstructPar`) affecting overall performance.

## Solution
- HPC Admin acknowledged the issue and took action to address the high CPU usage by user `iwpa79`.

## General Learnings
- High CPU usage by individual processes can degrade overall system performance.
- Monitoring and addressing resource-intensive processes is crucial for maintaining system stability.
```
---

### 2024102142001004_Dummyaccount%20%2B%20Reservierung%20saprap2%20f%C3%83%C2%BCr%20CLPE%20Tutorial.md
# Ticket 2024102142001004

 ```markdown
# HPC Support Ticket Analysis

## Subject
Dummyaccount + Reservierung saprap2 für CLPE Tutorial

## Keywords
- Dummy account
- Reservation
- saprap2 node
- CLPE Tutorial
- Testcluster

## User Request
- Request for a dummy account starting from 1.11.
- Reservation of the saprap2 node in the test cluster from 17.11 to 19.11 for the CLPE Tutorial on 18.11.

## HPC Admin Response
- Account details provided:
  - Username: w10z0000
  - Password: Vu=f?o4n
- Reservation details:
  - ReservationName: CLPE
  - StartTime: 2024-11-17T00:00:00
  - EndTime: 2024-11-20T00:00:00
  - Duration: 3-00:00:00
  - Nodes: saprap2
  - NodeCnt: 1
  - CoreCnt: 104
  - TRES: cpu=208
  - Users: ihpc030h, w10z0000
  - State: INACTIVE

## Notes
- The request was initially deferred.
- A note was added with a reference to a course link: [Course Link](https://www.idm.fau.de/coma/hpcCourse/show/5042)

## Root Cause
- User required a dummy account and node reservation for a specific tutorial.

## Solution
- HPC Admin provided the dummy account details and confirmed the reservation.

## General Learning
- Understand the process for creating dummy accounts and reserving nodes for specific events.
- Ensure to provide detailed reservation information including start time, end time, nodes, and users.
- Reference relevant links or notes for additional context.
```
---

### 2024051542003088_OpenMolcas.md
# Ticket 2024051542003088

 ```markdown
# HPC-Support Ticket Conversation: OpenMolcas

## Keywords
- OpenMolcas
- Parallelization
- OpenMP
- MPI
- Global Arrays (GA)
- SLURM
- Module Installation
- Performance Testing
- TMPDIR

## Summary
A user requested support for installing and optimizing OpenMolcas for future projects. The HPC team provided assistance in compiling and testing the software, addressing parallelization issues, and offering recommendations for efficient usage.

## Issues and Solutions

### Issue: Parallelization Not Working
- **Root Cause**: The initial module was compiled without MPI/Global Arrays support, and OpenMP parallelization was not effective.
- **Solution**: The HPC team recompiled OpenMolcas with Global Arrays (GA) support, which showed acceptable speedup up to 4 cores. Two new modules were installed: `openmolcas/23.06-ompi` and `openmolcas/23.06-ompi-icx`.

### Issue: Job Script Optimization
- **Root Cause**: The user was using explicit paths starting with `/scratch/...`, which could lead to I/O issues.
- **Solution**: The HPC team recommended using the environment variable `$TMPDIR` for job-specific directories to reduce I/O.

### Issue: Setting OpenMP Threads
- **Root Cause**: The user was not setting OpenMP threads correctly in the job script.
- **Solution**: The HPC team provided the correct SLURM settings for OpenMP threads:
  ```bash
  export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
  echo "OMP_NUM_THREADS=$OMP_NUM_THREADS"
  export SRUN_CPUS_PER_TASK=$SLURM_CPUS_PER_TASK
  ```

## General Learnings
- **Module Installation**: The HPC team can install and test modules based on user requests, ensuring they meet the required specifications.
- **Performance Testing**: The team conducts performance tests to identify the most efficient configurations for software usage.
- **User Guidance**: The HPC team provides detailed guidance on optimizing job scripts and using environment variables for better performance.

## Conclusion
The HPC team successfully installed and optimized OpenMolcas for the user, addressing parallelization issues and providing recommendations for efficient usage. The user was advised to test different configurations to identify the best setup for their specific needs.
```
---

### 2023092042003607_Tier3-Access-Fritz%20%22Stefan%20Hiemer%22%20_%20iww8014h.md
# Ticket 2023092042003607

 # HPC Support Ticket: Tier3-Access-Fritz

## Keywords
- User Access
- Fritz Cluster
- LAMMPS
- Benchmarking
- Multi-node Workload
- DFG/NHR Proposal

## Summary
- **User Request**: Access to Fritz cluster for benchmarking LAMMPS on metallic systems.
- **Requirements**: Multi-node workload with HDR100 Infiniband, 72 cores, 250 GB per node.
- **Purpose**: Estimate computational requirements for a DFG/NHR proposal.
- **Expected Outcome**: Successful application of benchmarking.

## Actions Taken
- **HPC Admin**: Granted user access to Fritz cluster using the script `/root/bin/add-early-user-with-partition-limits.sh`.
- **HPC Admin**: Notified user of access and offered assistance with benchmarks.

## Lessons Learned
- **User Access**: Script `/root/bin/add-early-user-with-partition-limits.sh` is used to grant user access to Fritz.
- **Benchmarking**: Users may request access for benchmarking purposes to estimate future computational needs.
- **Software**: LAMMPS is a commonly used software for molecular dynamics simulations.

## Root Cause of Problem
- User required access to Fritz cluster for benchmarking purposes.

## Solution
- HPC Admin granted access using the appropriate script and notified the user.

## Follow-up
- Offer assistance with benchmarking as needed.
- Ensure user has access to required software (LAMMPS) and resources.
---

### 2022110942002985_Jobs%20auf%20Woody%20-%20mpwm023h.md
# Ticket 2022110942002985

 ```markdown
# HPC Support Ticket: Jobs auf Woody - mpwm023h

## Keywords
- Job submission
- Resource allocation
- Cores
- Hauptspeicherbedarf
- `--ntasks-per-node`

## Problem
- User submitted over 600 jobs on Woody, each requesting 4 cores using the `--ntasks-per-node=4` option.
- Jobs were only utilizing one core, and the memory requirement was the primary reason for requesting more cores.

## Root Cause
- Inefficient resource allocation: Jobs were requesting more cores than needed, leading to underutilization of resources.

## Solution
- HPC Admin advised the user to use `--ntasks-per-node=1` unless there are valid reasons for requesting more cores.
- This change allows four times as many jobs to run simultaneously, optimizing resource usage.

## Lessons Learned
- Always verify the resource requirements of jobs to ensure efficient use of HPC resources.
- Adjust job submission scripts to request only the necessary resources to avoid wastage.
- Regularly review and update job submission practices to align with current resource usage patterns.
```
---

### 2023082742000724_OMP%20VASP%20jobs%20but%20with%20an%20OpenMP-enabled%20binary%20-%20bctc034h.md
# Ticket 2023082742000724

 # HPC Support Ticket: OMP VASP Jobs with OpenMP-Enabled Binary

## Keywords
- VASP
- OpenMP
- Job Script
- OMP Threads
- OMP_STACKSIZE
- Monitoring System

## Problem
- User's VASP jobs were running on only 8 cores per node, significantly lower than the available 104 cores on SPR nodes.
- The job script specified 13 OMP threads, but the VASP binary was likely not built with OpenMP enabled.

## Root Cause
- The VASP binary was not built with OpenMP support, leading to inefficient resource utilization.

## Solution
- Ensure the VASP binary is built with OpenMP enabled.
- Add the following to the job script when running VASP with OpenMP:
  ```bash
  export OMP_STACKSIZE=500m
  ```
  This is recommended by VASP developers for combining MPI and OpenMP.

## Additional Information
- Monitoring links for the jobs:
  - [JobId=814745](https://monitoring.nhr.fau.de/monitoring/job/4879664)
  - [JobId=814723](https://monitoring.nhr.fau.de/monitoring/job/4879543)
- Reference: [Combining MPI and OpenMP in VASP](https://www.vasp.at/wiki/index.php/Combining_MPI_and_OpenMP)

## Outcome
- The ticket was closed due to no response from the user.

## General Learnings
- Always ensure that the binary of the software being used is built with the required support (e.g., OpenMP).
- Follow software-specific recommendations for optimal performance, such as setting `OMP_STACKSIZE` for VASP.
- Monitor job performance and resource utilization to identify potential issues.
---

### 2020102042003093_Job%20auf%20Meggie%20mit%20jobid%3D827781.md
# Ticket 2020102042003093

 # HPC Support Ticket Analysis: Job Inefficiency on Meggie

## Keywords
- Job inefficiency
- Resource wastage
- Slurm job script
- mpirun
- SLURM_JOB_NUM_NODES
- Monitoring system

## Summary
A job on Meggie (jobid=827781) was flagged for inefficient resource usage. The job requested 20 nodes but utilized only 9, leading to resource wastage.

## Root Cause
- The job script requested 20 nodes (`#BATCH --nodes=20`) but used `mpirun -ppn 18 -np $((9*18))`, limiting the job to 9 nodes.

## Solution
- Use the `$SLURM_JOB_NUM_NODES` variable to dynamically set the number of processes based on the allocated nodes.
- Example: `mpirun -ppn 18 -np $((SLURM_JOB_NUM_NODES * 18))`

## Documentation References
- [Intel MPI Documentation](https://www.anleitungen.rrze.fau.de/hpc/environment/#intelmpi)
- [Batch Processing Documentation](https://www.anleitungen.rrze.fau.de/hpc/batch-processing/#slurmscripts)

## Follow-up
- The user implemented the suggested changes, and the issue was resolved.
- No further response was received, but the job scripts were updated correctly.

## General Learning
- Always ensure that the number of processes (`-np`) in `mpirun` matches the number of allocated nodes to avoid resource wastage.
- Utilize Slurm environment variables like `$SLURM_JOB_NUM_NODES` to make job scripts more flexible and efficient.
---

### 2019052042002356_TinyFat%3A%20submitted%20jobs%20are%20long%20in%20the%20queue%2C%20bca203.md
# Ticket 2019052042002356

 # HPC Support Ticket: Job Queue Delay on TinyFat

## Keywords
- Job queue delay
- ORCA jobs
- TinyFat
- Broadwell nodes
- Priority usage

## Summary
A user reported that their ORCA jobs on TinyFat, specifically on the "broadwell256" nodes, had been in the queue for over 24 hours. The user inquired about the status of the broadwell nodes and the reason for the delay.

## Root Cause
- The broadwell nodes were functioning correctly.
- The delay was due to the group that paid for these nodes using them, resulting in higher priority for their jobs.

## Solution
- The user was informed that the nodes were working fine and that the delay was due to priority usage by the group that paid for the nodes.
- The user was advised to consider using TinyEth for smaller calculations.
- The user inquired about running ORCA on Meggie or Emmy, specifically version 4.1.1, but no response was provided in the given conversation.

## General Learning
- Job queue delays can occur due to priority usage by groups that have paid for specific nodes.
- Users should be aware of the priority system and consider alternative resources if their jobs are delayed.
- Communication about software availability on different clusters (e.g., Meggie, Emmy) can help users plan their computations more effectively.
---

### 2024081942001899_Multinode-Freischaltung%20f%C3%83%C2%BCr%20Benchmark%20Projekt.md
# Ticket 2024081942001899

 ```markdown
# HPC Support Ticket: Multinode-Freischaltung für Benchmark Projekt

## Keywords
- Multinode Freischaltung
- Benchmark
- Stable Diffusion
- sacctmgr
- QoS (Quality of Service)
- a40multi
- a100multi

## Problem
- User requested multinode access for project `v111dc10` to benchmark Stable Diffusion.

## Solution
- HPC Admin updated the account settings to include `a40multi` and `a100multi` QoS.

## Actions Taken
- HPC Admin executed the following commands:
  ```bash
  sacctmgr update account v111dc set qos+=a40multi -i
  sacctmgr update account v111dc set qos+=a100multi -i
  ```

## Lessons Learned
- Multinode access can be granted by updating the account's QoS settings using `sacctmgr`.
- Specific QoS settings (e.g., `a40multi`, `a100multi`) need to be added to enable multinode functionality.

## Notes
- Ensure that the project ID (`v111dc10`) is correctly referenced in the commands.
- Confirm with the user that the changes have been applied successfully.
```
---

### 2024121342002122_GUI%20bug%20in%20Cluster%20Cockpit.md
# Ticket 2024121342002122

 # HPC Support Ticket: GUI Bug in Cluster Cockpit

## Keywords
- GUI bug
- Cluster Cockpit
- Job duration
- Billing
- Graphical UI

## Problem Description
- **Root Cause:** The graphical UI in Cluster Cockpit displays an incorrect job duration.
- **User Report:** A job that finished in just over three hours is shown as taking over thirty hours in the plot.

## Impact
- The bug does not affect the actual billing time, which is correctly shown in the HPC Portal.

## Solution
- **Status:** Known issue.
- **Action Taken:** HPC Admins are aware of the problem. No immediate fix is mentioned.

## General Learnings
- Users should verify job durations through other means (e.g., output files) rather than relying solely on the graphical UI.
- Billing information in the HPC Portal is accurate despite the UI bug.

## Notes
- The issue was reported during the holiday season, indicating ongoing support and monitoring.
- The problem does not impact the user's billed computation time.

---

This documentation can be used to address similar UI bugs in the future, ensuring users are aware that billing information remains accurate despite visual discrepancies.
---

### 2024013142000656_Jobs%20on%20Fritz%20not%20using%20resources%20-%20b159cb14.md
# Ticket 2024013142000656

 # HPC Support Ticket: Jobs Not Using Resources

## Keywords
- OpenMP parallelization
- SRUN_CPUS_PER_TASK
- SLURM_CPUS_PER_TASK
- Single-node jobs
- Resource utilization
- Job script optimization

## Issue
- User has 22 single-node jobs running on one core each, leaving 71 cores idle.
- Job scripts indicate the intention to use OpenMP parallelization.

## Root Cause
- The environment variable `SRUN_CPUS_PER_TASK` is not set, leading to inefficient resource utilization.

## Solution
- Set the environment variable `SRUN_CPUS_PER_TASK` to `$SLURM_CPUS_PER_TASK` in the job script:
  ```bash
  export SRUN_CPUS_PER_TASK=$SLURM_CPUS_PER_TASK
  ```
- Consider packing multiple runs into one job script to better utilize node resources, given that each program does not require much memory and does not use all cores.
- For optimal performance on Fritz, which has two sockets, consider running two instances of the program, each on 36 cores of a socket.

## Additional Notes
- Even with the environment variable set, the speedup compared to a single-core calculation may not be significant.
- If the issue persists, contact the HPC support team for further assistance.

## Relevant Personnel
- HPC Admins
- 2nd Level Support Team
- Georg Hager (Training and Support Group Leader)
- Harald Lanig (NHR Rechenzeit Support)
- Jan Eitzinger, Gruber (Software and Tools Developer)

## Contact
- Email: support-hpc@fau.de
- Website: [FAU HPC](https://hpc.fau.de/)
---

### 2023062142001765_Fw%3A%20%5BNHR%40FAU%5D%20Info%20Verf%C3%83%C2%BCgbarkeit%20SPR%20High%20Memory%20Knoten%20auf%20Fri.md
# Ticket 2023062142001765

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Keywords
- Fritz Cluster
- High Memory Nodes
- Job Submission
- salloc
- Invalid Account
- NHR@FAU Project
- GPU Resources
- Regular Nodes

## Summary
A user encountered issues submitting jobs to the Fritz cluster due to an invalid account or account/partition combination. The user's project was initially only approved for GPU resources on Alex, not Fritz. The HPC Admin enabled the user's project on Fritz, including access to high memory nodes.

## Root Cause
- The user's project was not initially approved for Fritz resources, leading to job submission errors.

## Solution
- The HPC Admin enabled the user's project on Fritz, resolving the job submission issue.

## General Learnings
- Ensure that projects are approved for the specific resources they intend to use.
- High memory nodes on Fritz are available for NHR@FAU projects upon request.
- Regular nodes with 72 cores and 256 GB memory are also available on Fritz.
- Users should contact HPC support for resource access and any issues related to job submission.

## Actions Taken
- The HPC Admin enabled the user's project on Fritz, including access to high memory nodes.
- The user confirmed that they only need regular nodes with 256 GB memory for sporadic access.

## Recommendations
- Users should verify their project's resource allocations before attempting to submit jobs.
- Contact HPC support for any issues related to resource access or job submission.
```
---

### 2020022642001732_Re%3A%20Clusternutzung.md
# Ticket 2020022642001732

 ```markdown
# HPC Support Ticket: Clusternutzung

## Keywords
- RAM usage
- User ID (UID)
- ps command
- Python process
- Jupyter kernel

## Problem Description
- User observed that a non-existent user was consuming 5% of RAM.
- The output of the `ps` command showed a Python process running under a specific UID.

## Root Cause
- Misunderstanding of the `ps` command output.
- The user assumed the job was running under a username rather than a UID.

## Solution
- Clarification that the UID 384299 corresponds to an existing user account (mppi079h).
- The user realized their mistake in interpreting the output.

## Lessons Learned
- Always verify the UID to ensure it corresponds to an existing user.
- Understand the output of the `ps` command, especially the difference between UID and username.
- Misinterpretation of command outputs can lead to incorrect assumptions about resource usage.
```
---

### 2015110342000797_Failed%20OFA%20fabric%20probably%20in%20LIMA%20node%20l1321.md
# Ticket 2015110342000797

 # HPC Support Ticket: Failed OFA Fabric

## Keywords
- OFA fabric error
- MPI startup error
- Node crash
- Infiniband
- Batch system process crash
- Node reboot

## Problem Description
- **Error Message:** "MPI startup(): ofa fabric is not available and fallback fabric is not enabled"
- **Node:** l1321 (suspected)
- **Job ID:** 1770179
- **Rank:** 12
- **Exit Status:** Return code 254

## Root Cause
- Possible issue with the OFA fabric on node l1321.
- Node l1321 crashed the batch system process.

## Actions Taken
- HPC Admins rebooted node l1321.
- Uncertainty remains if l1321 was the actual problematic node as Infiniband seemed to work.

## Resolution
- Rebooted the suspected node.
- Requested user feedback to confirm if the issue persists.

## Follow-up
- User should report back if the crashes continue.

## General Learning
- OFA fabric errors can cause MPI startup failures.
- Node crashes can impact the batch system process.
- Rebooting the node is a common troubleshooting step.
- Confirmation of the issue resolution is necessary to ensure the correct node was identified.
---

### 2023090642001609_Fehlermeldung%20MPI%20Meggie.md
# Ticket 2023090642001609

 # HPC Support Ticket: MPI Error on Meggie

## Keywords
- MPI
- LAMMPS
- libfabric
- psm2
- timeout error
- FI_PSM2_CONN_TIMEOUT
- omnipath

## Summary
A user encountered a timeout error when running LAMMPS simulations using MPI on the Meggie cluster. The error message suggested increasing the `FI_PSM2_CONN_TIMEOUT` value. The issue initially resolved itself but reoccurred later.

## Root Cause
The root cause of the problem was identified as omnipath-related issues on the Meggie cluster, as confirmed by an HPC Admin.

## Solution
- **Temporary Workaround**: Increase the `FI_PSM2_CONN_TIMEOUT` value to mitigate timeout errors.
- **Permanent Fix**: Address the omnipath problems on the Meggie cluster to resolve the underlying issue.

## Lessons Learned
- Timeout errors during MPI jobs can be indicative of network issues.
- Increasing timeout values can serve as a temporary workaround but may not address the root cause.
- Communication with HPC Admins is crucial for identifying and resolving cluster-wide issues.

## Follow-up Actions
- Monitor the Meggie cluster for omnipath problems.
- Inform users about any ongoing network issues that may affect their jobs.
- Document and share workarounds for common errors to assist users in troubleshooting.
---

### 2024070942003676_Tier3-Access-Fritz%20%22Brendan%20Waters%22%20_%20iwia107h.md
# Ticket 2024070942003676

 ```markdown
# HPC Support Ticket Conversation Analysis

## Keywords
- Account activation
- Multi-node workload
- HDR100 Infiniband
- WaLBerla
- Python
- Performance benchmarking
- Tier3-Grundversorgung

## Summary
- **User Request**: Access to HPC system "Fritz" for multi-node workload.
- **Requirements**:
  - Multi-node workload with HDR100 Infiniband (1:4 blocking).
  - Per node: 72 cores, 250 GB.
  - Required software: WaLBerla, Python.
  - Application: Scaling test of WaLBerla code for specific scalar transport application.
  - Expected results: Performance benchmarking for a computer & fluids paper.
  - Additional notes: Work undertaken under Tier3-Grundversorgung.

## Actions Taken
- **HPC Admin**: Enabled the user's account on Fritz.

## Lessons Learned
- **Account Activation**: Ensure user accounts are activated promptly upon request.
- **Resource Allocation**: Understand and allocate resources based on user-specified requirements (e.g., multi-node workload, specific software).
- **Project Documentation**: Note the project details and expected outcomes for future reference and support.

## Root Cause of the Problem
- User needed access to the HPC system for a specific project.

## Solution
- HPC Admin enabled the user's account on Fritz.
```
---

### 2023060142001203_D%C3%83%C2%BCrfen%20wir%20gr%C3%83%C2%B6%C3%83%C2%9Fere%20Jobs%20auf%20fritz%20versuchen%3F%20a105cb.md
# Ticket 2023060142001203

 # HPC Support Ticket Conversation Summary

## Subject: Running Larger Jobs on Fritz

### Keywords:
- Lustre performance
- Large-scale jobs
- Job scheduling
- Partition reservation
- Network topology
- I/O performance
- Contingent management

### General Learnings:
- **Lustre Performance**: Lustre on Fritz performs well, comparable to other systems like Hawk and SuperMUC-NG.
- **Job Scheduling**: Large jobs can cause significant downtime and are generally discouraged during regular operation.
- **Partition Reservation**: For large jobs, it's better to reserve nodes for a defined period to avoid excessive downtime.
- **Network Topology**: Fritz has a non-homogenous non-blocking network with islands of 64 nodes, which can affect performance.
- **I/O Performance**: I/O operations are critical and can be a bottleneck, especially with large jobs.
- **Contingent Management**: Users should be aware of their contingent and plan jobs accordingly.

### Root Cause of the Problem:
- User wants to run larger jobs on Fritz but is concerned about system performance and job scheduling.

### Solution:
- **Partition Reservation**: HPC Admins can reserve nodes for large jobs during specific periods, such as maintenance windows.
- **Job Submission**: Users can submit jobs in advance and monitor them as needed.
- **Feedback on Plots**: Improve plot readability by projecting lines with surfaces.

### Conversation Summary:

#### User:
- Requested to run larger jobs on Fritz due to positive Lustre performance results.
- Provided details on job configurations and I/O operations.
- Asked about contingent management and job scheduling.

#### HPC Admin:
- Confirmed that larger jobs are possible but need to be scheduled carefully to avoid excessive downtime.
- Suggested reserving nodes for large jobs during maintenance windows.
- Provided feedback on network topology and its impact on performance.
- Confirmed that jobs were successfully submitted and completed.

### Additional Notes:
- **Plot Feedback**: HPC Admin suggested improving plot readability by projecting lines with surfaces.
- **Job Completion**: Jobs were successfully submitted and completed during a maintenance window.

This summary provides a concise overview of the conversation, highlighting key points and solutions for future reference.
---

### 2022121242002011_Capriccio%20method%20%2B%20Lammps%20usage%20%5Bb136dc13%5D.md
# Ticket 2022121242002011

 ```markdown
# HPC-Support Ticket: Capriccio Method + Lammps Usage

## Keywords
- Capriccio simulations
- Lammps
- Floating point operations (Flop/s)
- Hardware usage optimization
- Zoom meeting
- Code improvement
- KONWHIR
- Matlab
- C++
- Dissertation deadlines
- SFB-Begutachtung

## Summary
- **Issue**: Low Flop/s in Capriccio simulations using Lammps on Fritz and Meggie clusters.
- **Root Cause**: Inefficient code usage, possibly due to limited programming experience.
- **Solution**:
  - Scheduled Zoom meeting to discuss method and Lammps usage.
  - Recommended KONWHIR for coding assistance.
  - Suggested testing code on a single node to check performance.
  - Planned follow-up meeting in February.

## Details
- HPC Admin noticed low Flop/s in Capriccio simulations using Lammps.
- Scheduled a Zoom meeting to discuss optimization.
- Users expressed willingness to improve code but have limited programming experience.
- Original MD code from Darmstadt, continuum part uses Matlab, could switch to C++.
- Due to dissertation deadlines and SFB-Begutachtung, no immediate code changes expected.
- Users agreed to test code on a single node for performance comparison.
- Next meeting planned for February.

## Conclusion
- Ticket closed with plans for further optimization discussions in February.
- Users encouraged to seek assistance through KONWHIR for coding improvements.
```
---

### 2024011742001959_Tier3-Access-Fritz%20%22Alfonso%20Fernandez%22%20_%20gwgk101h.md
# Ticket 2024011742001959

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject: Tier3-Access-Fritz "Alfonso Fernandez" / gwgk101h

### Keywords:
- Tier3 Access
- Fritz
- Account Approval
- Multi-node Workload
- HDR100 Infiniband
- WRF Model
- GNU Compilers
- Intel Compiler Suite
- NetCDF, MPICH, zlib, libpng, Jasper
- NCL, NCVIEW, NCO, CDO, GDAL, Python
- Humboldt Fellowship
- Amazon Deforestation
- Climate Simulations
- High Resolution
- Tropical Andes

### Summary:
- **User Request**: Access to Fritz for multi-node workload with specific hardware and software requirements.
- **Hardware Requirements**: HDR100 Infiniband with 1:4 blocking, 72 cores, 250 GB per node.
- **Software Requirements**: GNU compilers, Intel compiler suite, various libraries, and post-processing tools.
- **Project Details**: Climate simulations to study the impact of Amazon deforestation on high mountain environments.
- **Expected Results**: High-resolution climate fields for studying changes in key variables affecting mountain climate and the cryosphere.

### Root Cause:
- User required access to Fritz for a specific project involving climate simulations.

### Solution:
- **HPC Admin**: Granted access to Fritz for the user's account (gwgk101h).

### Lessons Learned:
- **Access Granting**: Proper documentation and communication are essential when granting access to HPC resources.
- **Project Requirements**: Understanding the specific hardware and software requirements for complex projects is crucial for effective support.
- **Collaboration**: Effective collaboration between HPC Admins and users ensures that project needs are met efficiently.

### Follow-up Actions:
- Ensure that the user has all necessary software and hardware resources.
- Monitor the user's progress and provide additional support as needed.
```
---

### 2023053042003131_AW%3A%20%5BNHR%40FAU%5D%20Info%20Verf%C3%83%C2%BCgbarkeit%20SPR%20High%20Memory%20Knoten%20auf%20Fri.md
# Ticket 2023053042003131

 ```markdown
# HPC Support Ticket Conversation Summary

## Keywords
- Project Access
- High Memory Nodes
- Multi-Node Computing
- Project Expiration
- Job Monitoring
- Feature Selection
- Machine Learning
- Job Termination

## General Learnings
- **Project Access**: Users need to provide a good reason for accessing high memory nodes.
- **Job Monitoring**: Users should use the monitoring system to check job performance.
- **Project Expiration**: Users should be aware of project expiration dates and request extensions if needed.
- **Job Termination**: Jobs can be terminated if they are blocking resources for too long.

## Conversation Summary

### Initial Request
- **User**: Requested access to the Fritz cluster for project b131dc.
- **HPC Admin**: Granted access to standard nodes with 72 cores and 256 GB of main memory.

### High Memory Nodes
- **User**: Provided details about their project involving acoustic features and machine learning.
- **HPC Admin**: Explained that regular nodes are for multi-node computing, while high memory nodes have limited node availability.

### Project Expiration
- **HPC Admin**: Reminded the user about the project expiration and the process for extension.
- **HPC Admin**: Extended the project by three months.

### Job Monitoring
- **HPC Admin**: Notified the user about job performance issues and provided a link to the monitoring system.
- **User**: Acknowledged the issue and fixed the experiment configuration.

### Job Termination
- **HPC Admin**: Terminated jobs that were blocking resources for too long.
- **User**: Confirmed that the issue was resolved.

## Root Cause and Solution
- **Root Cause**: The user's jobs were not performing as expected due to an issue with the experiment configuration and dataset.
- **Solution**: The user fixed the experiment configuration, which resolved the issue.
```
---

### 2018091842001936_Query%20regarding%20new%20installation%20of%20Openfoam%20v1806.md
# Ticket 2018091842001936

 ```markdown
# Query regarding new installation of OpenFOAM v1806

## Problem Description
- **User Issue**: Intermittent job failures in OpenFOAM v1806 simulations after running for several hours.
- **Error Message**: "Primary job terminated normally, but 1 process returned a non-zero exit code. Per user-direction, the job has been aborted."
- **Root Cause**: OpenFOAM's use of `fork()` system call in combination with MPI, which is known to cause issues.

## Keywords
- OpenFOAM v1806
- MPI
- fork()
- Segmentation fault
- Job abortion

## HPC Admin Response
- **Diagnosis**: The issue is likely due to OpenFOAM calling an external program using `fork()`, which can cause memory corruption or other system errors when used with MPI.
- **Suggestion**: Refer to [Open MPI FAQ](https://www.open-mpi.org/faq/?category=tuning#fork-warning) for potential solutions.
- **Additional Notes**: The `fork()` warning might be a side effect rather than the root cause. OpenFOAM has a tendency to call `printStack` on internal errors, which then invokes `fork()`.

## Solution
- **Immediate Action**: Disable the `fork()` warning by setting the `mpi_warn_on_fork` MCA parameter to 0 if the user is confident that the application can handle it.
- **Long-term**: Investigate OpenFOAM's internal error handling to prevent the need for `fork()` calls.

## Conclusion
- The issue is likely due to the interaction between OpenFOAM's use of `fork()` and MPI.
- Users should be cautious when running OpenFOAM simulations that involve `fork()` calls and consider disabling the MPI warning if they are confident in their application's stability.
```
---

### 2024051642002489_Request%20to%20use%20the%20spr1tb%20%26%20spr2tb%20partition%20-%20Project%20a104bc.md
# Ticket 2024051642002489

 # HPC Support Ticket Conversation Analysis

## Keywords
- High-memory nodes
- Sapphire nodes
- Gamma-ray emission
- Synthetic HI velocity maps
- POLARIS radiative transfer code
- Memory requirements
- NHR projects

## Summary
The user requested access to high-memory nodes (Sapphire nodes) for their project due to the memory-intensive nature of their analysis tasks. The HPC Admin confirmed that the requested nodes are now generally available.

## Root Cause of the Problem
- The user's analysis tasks require more memory than available on standard Ice Lake nodes (250 GB).
- Specific tasks include producing gamma-ray emission spectra and synthetic HI velocity maps, which require up to 300 GB and 2 TB of RAM, respectively.

## Solution
- The HPC Admin confirmed that the high-memory nodes (spr1tb & spr2tb) are now generally available for use.
- The user can proceed with their analysis tasks using the Sapphire nodes.

## General Learnings
- High-memory nodes can be requested for memory-intensive tasks.
- Documentation should be kept up-to-date to reflect the availability of resources.
- Clear communication of resource requirements and justifications helps in efficient resource allocation.

## Next Steps
- Update the documentation to reflect the general availability of spr1tb & spr2tb nodes.
- Monitor the usage of high-memory nodes to ensure efficient resource allocation.
---

### 2018112042000151_Fortran%20Speicher%20Alignment.md
# Ticket 2018112042000151

 # HPC-Support Ticket: Fortran Memory Alignment

## Keywords
- Fortran
- Memory Alignment
- Performance Optimization
- Cache Thrashing
- SIMD Code
- Intel Xeon Phi

## Summary
The user inquired about the effectiveness of memory alignment in Fortran for performance optimization. The discussion revolved around the impact of memory alignment on modern CPUs and specific cases like Intel Xeon Phi.

## Root Cause
- The user was experimenting with memory alignment to optimize performance but was unsure about its effectiveness.

## Discussion
- **HPC Admin**: Memory alignment has minimal impact on modern CPUs. Penalties for unaligned access are negligible unless dealing with SIMD code and L1 cache-bound data.
- **User**: The user mentioned that they couldn't avoid using pointers and wanted to test alignment for performance gains.
- **HPC Admin**: Restrictive alignment can lead to cache thrashing, making it counterproductive. Intel Xeon Phi had specific alignment requirements, but modern CPUs handle unaligned loads more efficiently.

## Solution
- **HPC Admin**: Advised against focusing on memory alignment for performance optimization unless there is a specific use case showing significant performance gains.
- **User**: No noticeable performance improvement or degradation was observed from the alignment experiment.

## Conclusion
- Memory alignment is generally not worth the effort for performance optimization on modern CPUs. Focus should be on other optimization techniques unless a specific use case demonstrates significant benefits from alignment.

## Additional Notes
- The user mentioned having an Intel Application Performance Snapshot from the KNLBooster in Jülich but found it difficult to interpret.
- The discussion highlighted the complexities of optimizing code for specific architectures like Intel Xeon Phi.
---

### 2022111442002975_Help%20with%20parallel%20processing%20on%20the%20cluster.md
# Ticket 2022111442002975

 # HPC Support Ticket: Help with Parallel Processing on the Cluster

## Keywords
- R programming
- Parallel processing
- doParallel
- foreach
- SLURM
- Singularity VM

## Problem Description
- User's R scripts use more threads than specified.
- Jobs either consume excessive resources or fail completely.
- User runs scripts on a Singularity VM.

## Root Cause
- The script automatically detects and uses all available cores on the compute node.
- Multiple instances of the script lead to excessive resource usage.

## Troubleshooting Steps
1. **HPC Admin** requested the location of the user's code on the HPC filesystem.
2. **HPC Admin** identified the issue with automatic core detection in the script.
3. **HPC Admin** suggested modifying the script to use the number of cores allocated by SLURM.

## Solution
- Modify the R script to use the environment variable `$SLURM_JOB_CPUS_PER_NODE` to set the number of cores.
- Replace automatic core detection with the following code:
  ```R
  number_of_cores <- Sys.getenv("SLURM_JOB_CPUS_PER_NODE")
  cl <- parallel::makeCluster(number_of_cores)
  doParallel::registerDoParallel(cl)
  ```
- Alternatively, use the following approach to register the parallel backend:
  ```R
  library(doParallel)
  registerDoParallel(cores=number_of_cores)
  ```

## Follow-up
- The user was asked to test the solution and provide the job ID for further monitoring.
- The ticket was closed due to no further feedback from the user and no new jobs since the suggested solution.

## References
- [StackOverflow: doParallel cluster vs cores](https://stackoverflow.com/questions/28829300/doparallel-cluster-vs-cores)
- [Job Monitoring Links](https://monitoring.nhr.fau.de/monitoring/job/)
---

### 2022012642003041_strategy%20for%20long%20simulations%20%28climate%20group%29.md
# Ticket 2022012642003041

 # HPC-Support Ticket Conversation: Strategy for Long Simulations (Climate Group)

## Keywords
- Long simulations
- Climate group
- WRF model
- 24h limit
- Fritz cluster
- SPACK
- NCL
- NCVIEW
- HDF5
- csh
- parallel-netcdf
- real.exe
- WPS
- netcdf-c
- netcdf-fortran
- libpng
- time command
- Intel MPI
- OpenMPI
- RHEL8.x
- RHEL7.x
- Lustre
- Visualization node

## Summary
The conversation revolves around the strategy for running long simulations using the WRF model on the Fritz cluster. The main issues discussed include the 24-hour limit on job runtime, access to standard file systems, recompilation of libraries, and specific software dependencies.

## Issues and Solutions

### 1. 24-hour Limit for Jobs
- **Issue**: The user needs to run simulations longer than the 24-hour limit.
- **Solution**: The HPC Admin can extend the wall time limit for specific jobs, but there is no guarantee that the infrastructure will support such long runs.

### 2. Access to Standard File Systems
- **Issue**: The user needs access to standard file systems (home, saturn, vault) from the Fritz cluster.
- **Solution**: All directories starting with `/home` are accessible on Fritz. However, `$FASTTMP` directories (`/lxfs` or `/elxfs`) are not accessible.

### 3. Recompilation of Libraries
- **Issue**: The user needs to know if libraries compiled on Meggie need to be recompiled for Fritz due to OS/compiler differences.
- **Solution**: Fritz uses RHEL8.x while Meggie used RHEL7.x. Old binaries may work but need to be tested individually. Some pre-/post-processing steps can still be performed on Meggie.

### 4. Specific Software Dependencies
- **Issue**: The user encounters issues with specific software dependencies like NCL, NCVIEW, HDF5, csh, parallel-netcdf, real.exe, WPS, netcdf-c, netcdf-fortran, libpng, and the time command.
- **Solution**:
  - **NCL and NCVIEW**: Temporarily use Meggie for these tools. NCVIEW installation via SPACK is postponed.
  - **HDF5**: Ensure the correct variant is used (`+cxx` or `~szip`).
  - **csh**: The login nodes now have `(t)csh`, which should resolve the issue with the WRF compile script.
  - **parallel-netcdf**: A direct module is now available.
  - **real.exe**: The job was extended to 8 days, but the user should optimize the configuration for better performance.
  - **WPS**: Link to the appropriate libpng files under SPACK.
  - **netcdf-c and netcdf-fortran**: Create a `NetCDF` directory in the user's home directory and link the necessary files.
  - **time command**: Use the SPACK time module.

### 5. Visualization Node
- **Issue**: The user needs graphical evaluation of data.
- **Solution**: A visualization node will be available on Fritz in the future, which will have more tools for graphical evaluation.

## Conclusion
The conversation highlights the need for extended job runtime, access to standard file systems, and specific software dependencies for long simulations on the Fritz cluster. The HPC Admins provided solutions and workarounds for the issues encountered, ensuring the user can proceed with their simulations.
---

### 2024062442002561_Jobs%20stuck%20on%20Priority.md
# Ticket 2024062442002561

 # HPC Support Ticket: Jobs Stuck on Priority

## Keywords
- Job submission
- Priority
- A40 queue
- Alex system
- Compute time

## Problem Description
User unable to submit jobs in the Alex system, specifically in the A40 queue. Jobs remain stuck with the "Priority" message.

## Root Cause
- Jobs from other users with higher priority are being processed first.
- Priority is determined by recent compute time usage.

## Solution
- Wait for jobs with higher priority to complete.
- Priority will improve as other users' compute time usage increases.

## General Learning
- Job priority is influenced by recent compute time usage.
- Higher priority jobs are processed first, which can cause delays for lower priority jobs.
- Patience is required as job priority will improve over time.

## Next Steps for Support
- Monitor the user's job status.
- Provide updates if the situation changes or if further investigation is needed.
---

### 2025030742001865_MPI%20related%20error%3F.md
# Ticket 2025030742001865

 ```markdown
# HPC Support Ticket: MPI Related Error

## Summary
- **User Issue**: Job gets killed a few seconds after starting with an MPI error.
- **Software**: Fortran 90 software using MPI and MUMPS for brain elastic property image reconstruction.
- **Error Source**: Potentially related to MUMPS installation.

## Key Points
- **Initial Contact**: User reported job failure with MPI error.
- **Admin Response**: Requested minimal example or relevant code for debugging.
- **User Feedback**: Provided input files and job script.
- **Admin Suggestions**:
  - Modify job script to use `#!/bin/bash -l`.
  - Uncomment module load line.
  - Suggested using Spack to install MUMPS.

## Debugging Steps
- **Compiler Flags**: Suggested using `-O0 -C -g -traceback` for debugging.
- **Job Script Fixes**:
  - Change shebang to `#!/bin/bash -l`.
  - Uncomment module load line.
- **MUMPS Installation**:
  - Suggested using Spack for MUMPS installation.
  - Command: `spack install mumps@5.5.1`.

## Outcome
- **Error Persistence**: Error persisted after job script modifications.
- **Next Steps**: Reinstall MUMPS using Spack to identify potential installation issues.

## Conclusion
- **Root Cause**: Likely related to MUMPS installation.
- **Solution**: Reinstall MUMPS using Spack and verify installation steps.

## References
- [Spack Documentation](https://doc.nhr.fau.de/apps/spack/)
- [FAQ Error T57](https://doc.nhr.fau.de/faq/#error-t57)
```
---

### 2018071842001691_67%20OOM%20Meggieknoten.md
# Ticket 2018071842001691

 # HPC Support Ticket: OOM Nodes Issue

## Keywords
- OOM (Out of Memory)
- HPC Nodes
- Technical Measures
- Downtime

## Problem Description
- User reported OOM issues with HPC nodes.
- Nodes need to be fixed to resolve the OOM errors.

## Communication Summary
- **User Request**: Asked if someone could address the OOM issues with the nodes.
- **HPC Admin Response**: Planned to address the issue after an upcoming power downtime, aiming to reduce OOM occurrences through technical measures.

## Root Cause
- OOM errors on HPC nodes.

## Solution
- HPC Admins planned to implement technical measures to reduce OOM occurrences after the scheduled power downtime.

## General Learnings
- OOM issues can be addressed through technical measures.
- Scheduling maintenance after downtimes can be an effective strategy for implementing fixes.

## Next Steps
- Monitor the nodes after the downtime to ensure the technical measures have reduced OOM occurrences.
- Document any specific technical measures taken for future reference.
---

### 2022091942003559_Permission%20for%20creating%20Slurm%20reservations%20on%20Fritz.md
# Ticket 2022091942003559

 ```markdown
# HPC-Support Ticket Conversation: Permission for Creating Slurm Reservations on Fritz

## Keywords
- Slurm reservations
- Permissions
- Admin privileges
- Fritz nodes
- In-core Performance Engineering courses

## Summary
A user requested permissions to create Slurm reservations for specific Fritz nodes for upcoming courses. The HPC Admin clarified that granting such permissions would require full admin privileges, which is not feasible. The standard procedure is for the user to provide details of the required reservations, and the HPC team will handle the reservation.

## Root Cause
- User misunderstanding of permission requirements for creating Slurm reservations.

## Solution
- The user should provide the HPC team with the necessary details (number of nodes, time period, users/groups) for the reservation.
- The HPC team will handle the reservation process.

## General Learning
- Creating Slurm reservations requires admin privileges.
- Users should communicate their reservation needs to the HPC team, who will manage the reservations.
- Clarify user expectations and standard procedures to avoid misunderstandings.
```
---

### 2024120942003086_resubmit%20jobs%20on%20Fritz%20%5Bgwgi019h%5D.md
# Ticket 2024120942003086

 # HPC Support Ticket: Resubmit Jobs on Fritz

## Keywords
- Resubmit jobs
- Chain jobs
- Dependencies
- Slurm
- Node allocation
- Simulations

## Problem
- User runs long simulations that need to be restarted multiple times.
- Dedicated resubmit jobs block an entire node without doing actual work.
- User specifies fewer CPUs for resubmission jobs, but they still use 72 CPUs.

## Root Cause
- Inefficient use of dedicated resubmit jobs.
- Incorrect CPU allocation for resubmission jobs.

## Solution
- Use chain jobs with dependencies to automate the resubmission process.
- Move the resubmission logic to the job that does the work to avoid blocking nodes.

## General Learnings
- Avoid using dedicated resubmit jobs as they can block nodes unnecessarily.
- Chain jobs with dependencies can automate the resubmission process efficiently.
- Jobs on Fritz always allocate all 72 cores per node, regardless of the specified number of CPUs.

## References
- [Chain Jobs with Dependencies](https://doc.nhr.fau.de/batch-processing/advanced-topics-slurm/#chain-jobs-with-dependencies)
---

### 2023040342005138_Re%3A%20Alex%20GPU%20multi-node%20_%20longer%20sessions%20-%20b143dc18.md
# Ticket 2023040342005138

 # HPC Support Ticket Conversation Summary

## Keywords
- Multi-node training
- GPU nodes (A100, A40)
- QoS (Quality of Service)
- Resource limitations
- Fair sharing
- Interconnect (Ethernet, Infiniband)
- Job scheduling

## General Learnings
- Users can request multi-node training access for their HPC accounts.
- Different GPU types (A100, A40) have different interconnect capabilities.
- Resource limitations and fair sharing policies are in place to ensure equitable access to HPC resources.
- Job scheduling and resource allocation can impact other users and projects.
- Users should be aware of the interconnect capabilities of different GPU types when planning multi-node jobs.

## Root Causes and Solutions
- **Request for multi-node training access:**
  - **Root Cause:** User requires access to multi-node training for their research.
  - **Solution:** HPC Admins enabled the user's account for multi-node training using the `--qos=a100multi` and `--qos=a40multi` flags.

- **Resource limitations and fair sharing:**
  - **Root Cause:** User is concerned about the impact of their large jobs on other users and projects.
  - **Solution:** HPC Admins explained the fair sharing policies and dynamic throttling measures in place to ensure equitable access to resources.

- **Interconnect capabilities of different GPU types:**
  - **Root Cause:** User is unsure about the interconnect capabilities of A40 nodes compared to A100 nodes.
  - **Solution:** HPC Admins explained that A40 nodes are connected by Ethernet, which has a weaker interconnect compared to the Infiniband of A100 nodes.

- **Job scheduling and resource allocation:**
  - **Root Cause:** User has questions about the limitations on the number of GPU nodes they can request for their jobs.
  - **Solution:** HPC Admins provided information on the maximum number of nodes that can be requested for a single job and the factors that determine the total number of nodes that can be used at any given time.

## Documentation and Resources
- Users should refer to the HPC website and documentation for more information on resource limitations, job scheduling, and fair sharing policies.
- HPC Admins can provide additional guidance and support for users with specific questions or concerns.

## Notes
- The interconnect capabilities of different GPU types can impact the performance of multi-node jobs.
- Users should be mindful of the impact of their jobs on other users and projects and respect fair sharing policies.
- HPC Admins may employ dynamic throttling measures to ensure equitable access to resources.
- Users can request access to multi-node training and longer training sessions through the HPC support ticket system.
---

### 2022040942000366_measure%20CPU%20memory%20usage%20alex.md
# Ticket 2022040942000366

 # HPC Support Ticket: Measure CPU Memory Usage

## Keywords
- Memory usage
- CPU
- Valgrind
- Massif
- Out of memory errors
- Top
- /proc/meminfo
- /sys/fs/cgroup/memory/slurm/uid_*/job_*/memory.max_usage_in_bytes
- Slurm
- System monitoring

## Problem
- User is experiencing out of memory errors while assembling a large tridiagonal block matrix on the CPU.
- User expected memory usage does not match actual usage.
- Valgrind's Massif tool is not available on the cluster.

## Solution/Suggestions
- **Alternative Tools**: Use `top` or monitor `/proc/meminfo` to check memory consumption while the job is running.
- **Slurm Data**: Check `/sys/fs/cgroup/memory/slurm/uid_*/job_*/memory.max_usage_in_bytes` for memory usage data, though accuracy may vary.
- **System Monitoring**: Refer to graphs from system monitoring for a rough estimate of average memory usage over time. Note that data is collected once per minute, so temporary peaks may not be detected.

## Notes
- Valgrind is not provided on the cluster and there are no plans to install it.
- Slurm accounting data may not match system monitoring data.

## Root Cause
- The root cause of the memory discrepancy is not explicitly determined in this conversation. Further investigation using the suggested tools may be required.

## Next Steps
- User should employ the suggested methods to monitor memory usage and gather more data to diagnose the issue.
- If the problem persists, further assistance from HPC Admins or the 2nd Level Support team may be needed.
---

### 2024050742002791_Tier3-Access-Fritz%20%22Manuel%20Saigger%22%20_%20gwgk007h.md
# Ticket 2024050742002791

 # HPC Support Ticket Conversation Analysis

## Keywords
- Tier3 Access
- Fritz
- Multi-node workload
- HDR100 Infiniband
- WRF (Weather Research and Forecasting Model)
- HDF5
- NetCDF
- Intel
- IntelMPI
- Python
- Atmospheric simulations
- Deep learning model
- Training data set

## Summary
- **User Request:** Access to Fritz for multi-node workload with specific hardware and software requirements.
- **Hardware Requirements:** HDR100 Infiniband with 1:4 blocking, 72 cores, 250 GB per node.
- **Software Requirements:** WRF, HDF5, NetCDF, Intel, IntelMPI, Python.
- **Compute Time:** 100,000 node hours.
- **Application:** Atmospheric simulations for deep learning model training.

## Actions Taken
- **HPC Admin:** Enabled user account to use Fritz.

## Lessons Learned
- **User Needs:** Understanding specific hardware and software requirements for complex simulations.
- **Admin Response:** Quick account enablement for access to required resources.
- **Future Reference:** Ensure similar requests are handled efficiently by verifying hardware and software needs and enabling access promptly.

## Root Cause of the Problem
- User needed access to specific HPC resources for large-scale simulations.

## Solution
- HPC Admin enabled the user's account to access the required resources.

## Documentation for Support Employees
- **For similar requests:** Verify hardware and software requirements, ensure account has necessary permissions, and enable access to the specified HPC resources.
- **Contact Information:** Use the provided email and contact form for further communication and support.
---

### 2025030642003187_Reservierung%20auf%20fritz%20f%C3%83%C2%BCr%20ihpc119h.md
# Ticket 2025030642003187

 ```markdown
# HPC Support Ticket: Reservierung auf fritz für ihpc119h

## Keywords
- Reservierung
- Fritz-Knoten
- Leaf-Switch
- Masterarbeiterin
- Zeitfenster

## Summary
- **User Request:** Reservation of 5 Fritz nodes for a master's student. Preference for all nodes to be on the same leaf switch. Requested time: Friday, 07.03, 11:00-22:00. Alternative: Saturday, 08.03, same time.
- **HPC Admin Response:** The request was initially deferred and later closed as resolved.

## Root Cause
- The user needed a specific reservation for a master's student's project, with a preference for nodes on the same leaf switch.

## Solution
- The request was handled by the HPC Admin, who initially deferred it and later closed it as resolved. No specific details on the resolution were provided.

## General Learning
- Users may request specific node reservations for projects, including preferences for node locations.
- HPC Admins handle such requests and may defer or close them based on availability and other factors.
- It is important to communicate clearly with users about the status of their requests.
```
---

### 2024121642003125_Tier3-Access-Fritz%20%22Deepak%20Charles%20Chellapandian%22%20_%20mfdk103h.md
# Ticket 2024121642003125

 ```markdown
# HPC Support Ticket Analysis

## Keywords
- Multi-node workload
- HDR100 Infiniband
- PyTorch, libtorch, Gloo, MPI
- Bloch Meconnel equation
- MRI sequence optimization
- Physics-informed neural network
- Complex-128 bits
- Distributed Data Parallel
- Scalability
- High-resolution MRI clinical sequences

## Summary
- **User Request**: Access to HPC cluster "Fritz" for a multi-node workload with specific hardware and software requirements.
- **Hardware Requirements**: HDR100 Infiniband with 1:4 blocking, 72 cores per node, 250 GB RAM per node.
- **Software Requirements**: PyTorch or libtorch, Gloo, MPI.
- **Application**: Simulation of Bloch Meconnel equation for MRI sequence optimization using a physics-informed neural network.
- **Expected Outcome**: Scalability of heavily memory-bound simulation for optimizing longer high-resolution MRI clinical sequences.
- **User Experience**: Experienced HPC user and CUDA developer.

## Root Cause of the Problem
- The user requires access to the "Fritz" cluster to scale their simulation, which was previously run on a different node but found to be not scalable enough.

## Solution
- **HPC Admin Response**: The user was granted access to the "Fritz" cluster with their account.

## General Learnings
- Understanding the need for scalable solutions in HPC environments.
- Importance of multi-node workloads for complex simulations.
- Utilization of specific software tools like PyTorch, libtorch, Gloo, and MPI for distributed data parallel methods.
- The role of HPC admins in granting access and managing user requests.
```
---

### 42298773_Priority%20on%20Emmy.md
# Ticket 42298773

 # HPC Support Ticket: Priority on Emmy

## Keywords
- Priority improvement
- Resource allocation
- Job optimization
- Load balancing
- Code efficiency
- Federal HPC systems

## Summary
A user requested priority improvement for their account on the Emmy HPC system due to upcoming deadlines. The HPC Admins provided insights into the user's resource usage and offered suggestions for optimization.

## Root Cause
- User's jobs were not efficiently utilizing resources, with some nodes finishing work hours before others.
- The code appeared to be idle for several hours before job completion or being killed by the batch system.

## Solutions and Suggestions
- **Priority Boost**: The HPC Admin granted a slight priority boost but noted that it would impact other users.
- **Code Optimization**: The user was advised to optimize their code to reduce resource usage.
- **Monitoring**: The user was encouraged to monitor jobs to ensure efficient resource utilization.
- **Federal HPC Systems**: The user was advised to consider applying for a project on federal HPC systems for larger compute time demands.

## General Learnings
- Regularly monitor job performance to ensure efficient resource usage.
- Optimize code to reduce resource requirements.
- Consider applying for projects on federal HPC systems for large-scale computing needs.
- Avoid replying to old tickets to prevent notification issues.

## Actions Taken
- The HPC Admin provided a priority boost initially but later removed it due to fairness concerns.
- The scheduling algorithm was adjusted to improve overall utilization and throughput.

## Follow-up
- The user was advised not to reply to old tickets to avoid notification issues.
- The user was informed about their above-average resource allocation and the need to balance resource distribution among all users.
---

### 42296290_Cron%20jobs%20on%20HPC.md
# Ticket 42296290

 # Cron Jobs on HPC

## Keywords
- Cron jobs
- Frontend nodes
- Compute nodes
- HPC FAQ
- Support contact

## Summary
- **User Issue**: Cron jobs not running on HPC frontend nodes.
- **Root Cause**: Unclear, but possibly related to the specific configuration or environment of the cron jobs.
- **Solution**: Cron jobs are allowed on frontend nodes but not on compute nodes. Ensure the cron job does not cause excessive load.

## Detailed Conversation
- **User**: Asked about the possibility and permission to run cron jobs on HPC machines. Mentioned editing crontab on "emmy" but the job did not run.
- **HPC Admin**: Clarified that cron jobs are allowed on frontend nodes but not on compute nodes. Advised to use the proper support contact address.
- **User**: Confirmed the issue was on frontend nodes and the cron job was not computationally intensive.
- **HPC Admin**: Acknowledged the issue and suggested it might be resolved.

## Lessons Learned
- Always use the proper support contact address for new issues.
- Cron jobs are allowed on frontend nodes but not on compute nodes.
- Ensure cron jobs do not cause excessive load on the system.
- If a cron job does not run, check the configuration and environment settings.

## Next Steps
- Verify the cron job configuration and environment settings.
- If the issue persists, provide detailed logs and configuration for further troubleshooting.
---

### 2025020242000804_Inquiry%20About%20Node%20Status%20on%20Cluster%20Meggie.md
# Ticket 2025020242000804

 # HPC Support Ticket Conversation Analysis

## Keywords
- Node Status
- Meggie Cluster
- DOWN Nodes
- DRAIN Nodes
- Migration
- Fritz
- Woody
- Core-Count

## Summary
- **User Inquiry**: Concern about the status of nodes on the Meggie cluster, with many nodes marked as DOWN or DRAIN.
- **HPC Admin Response**: Acknowledgment of the aging hardware and difficulty in maintaining it. Suggestion to migrate to newer clusters (Fritz or Woody) based on core-count requirements.

## Root Cause
- Aging hardware leading to increased node failures on the Meggie cluster.

## Solution
- **Immediate Action**: Reactivation of a few nodes.
- **Long-Term Solution**: Migration to newer clusters (Fritz or Woody) to ensure better performance and reliability.

## General Learnings
- Older HPC clusters may experience increased hardware failures.
- Users should be prepared to migrate to newer clusters for better performance and reliability.
- Regular monitoring and maintenance of hardware are crucial for the longevity of HPC clusters.

## Next Steps for Support Employees
- Monitor the status of nodes on older clusters.
- Assist users in migrating to newer clusters if necessary.
- Provide guidance on selecting appropriate clusters based on core-count requirements.
---

### 2024020742001743_Freischaltung%20Multi-Node-Jobs.md
# Ticket 2024020742001743

 ```markdown
# HPC Support Ticket: Freischaltung Multi-Node-Jobs

## Keywords
- Multi-Node-Jobs
- Account Freischaltung
- Sprachmodell
- Fine-Tuning
- QoS (Quality of Service)

## Problem
- User requires access to multi-node jobs for fine-tuning experiments on a language model.

## Solution
- HPC Admin enabled multi-node job access for the user's account.
- User instructed to specify `--qos=a100multi` in job submissions.

## General Learnings
- Multi-node jobs require explicit activation by HPC Admins.
- Specific QoS parameters (`--qos=a100multi`) must be included in job scripts for multi-node jobs.
```
---

### 2017101942001415_lima1%20reagiert%20extrem%20langsam.md
# Ticket 2017101942001415

 ```markdown
# HPC Support Ticket: lima1 reagiert extrem langsam

## Keywords
- Slow login
- SSH delay
- Performance issue
- lima1
- lima2
- Swapping
- Memory usage

## Summary
A user reported that `lima1` was responding extremely slowly, with SSH login taking approximately 20 seconds. The issue was not reproducible by the HPC Admin, suggesting it might have been a temporary problem.

## Root Cause
- Possible memory-intensive process causing the system to swap heavily.

## Solution
- The issue resolved itself, indicating a temporary overload.
- No specific process was identified, but monitoring tools like `top` showed a kernel in the waiting state.

## Lessons Learned
- Temporary performance issues can be caused by memory-intensive processes.
- Monitoring tools like `top` can help identify processes causing performance degradation.
- Regular monitoring and quick response to user reports can help maintain system performance.
```
---

### 2024093042001955_Data%20downloading%20process%20on%20alex.md
# Ticket 2024093042001955

 # HPC Support Ticket: Data Downloading Process on Alex

## Keywords
- Data downloading
- CPU resources
- Alex server
- Fritz cluster
- Internet connection
- ConnectTimeout errors
- Huggingface
- Login node
- Core-hours

## Problem Description
- User needs to download and process datasets using only CPU resources.
- User experiences ConnectTimeout errors when downloading data from the Internet on job nodes.

## Root Cause
- Alex server does not support allocating only CPU resources.
- Shared internet connections on nodes lead to decreased bandwidth when multiple users are active.

## Solution
- **CPU Resources**: Use Fritz, the CPU cluster, for CPU-only tasks. Provide detailed information about data processing requirements to HPC Admins.
- **Internet Connection**: For light downloading tasks, use the login node. Alternatively, download data locally and transfer it to the HPC machines.

## Steps Taken
1. User contacted HPC support regarding CPU-only resource allocation and internet connection issues.
2. HPC Admin suggested using the Fritz cluster for CPU-only tasks and provided alternatives for data downloading.
3. User provided detailed information about data processing requirements.
4. HPC Admin granted access to the Fritz cluster with sufficient CPU core-hours for the user's project.

## General Learnings
- Always contact HPC support through the official email for faster response times.
- Provide detailed information about data processing requirements to help HPC Admins allocate appropriate resources.
- Use the login node for light downloading tasks to avoid ConnectTimeout errors.
- Consider downloading data locally and transferring it to HPC machines for better internet connectivity.

## Related Links
- [Huggingface Repo](https://huggingface.co/)
- [Example Data Processing Script](https://github.com/Yangyi-Chen/SOLO/blob/main/scripts/data/imagenet_train/process_imagenet_21k.py)
- [FAU HPC Support](mailto:hpc-support@fau.de)
- [FAU HPC Website](https://hpc.fau.de/)
---

### 42251127_%22Insufficient%20virtual%20memory%22%20in%20Lima.md
# Ticket 42251127

 # HPC Support Ticket: Insufficient Virtual Memory

## Keywords
- Insufficient virtual memory
- forrtl: severe (41)
- Memory limit
- Misconfiguration

## Problem Description
- User encountered an error: "forrtl: severe (41): insufficient virtual memory"
- The same program runs on another machine using 942 MB virtual memory per processor with 16 processors
- User requested 4 nodes, each with a memory limit of 24 GB

## Root Cause
- Misconfiguration on the user's side

## Solution
- The issue was resolved by the user after correcting the misconfiguration

## Lessons Learned
- Always verify configuration settings when encountering memory-related errors
- Ensure that the requested resources match the program's requirements
- Misconfigurations can lead to insufficient virtual memory errors even when the requested resources seem adequate

## Actions Taken
- User identified and corrected the misconfiguration
- HPC Admins confirmed the resolution of the issue

## Follow-up
- No further action required as the problem was resolved by the user
---

### 2023060542004221_HPC-Account%20Jonas%20Miederer.md
# Ticket 2023060542004221

 # HPC-Support Ticket Conversation Analysis

## Keywords
- HPC Account
- Reinforcement Learning
- Cluster Fritz
- Cluster Woody
- TinyGPU
- Job Size
- CPU Cores
- GPU
- HPC-Cafe
- IdM-Kennung
- Password

## General Learnings
- **Formal Requirements**: An HPC account application can be processed even without a departmental stamp.
- **Cluster Suitability**: Different clusters have different granularities and architectures. It's important to match the job requirements with the appropriate cluster.
  - **Fritz**: Granularity of 72 cores.
  - **Woody**: Each node has 32 cores, higher clock speed than Fritz.
  - **TinyGPU**: Suitable for GPU-based jobs.
- **Account Setup**: After account creation, it may take a few hours for password changes to be recognized and up to 2 days for services to be fully set up.
- **Support Resources**: HPC-Cafe and online introductions are recommended for new users. Documentation is available for getting started.

## Root Cause of the Problem
- The user initially requested access to the Fritz cluster for a job size of 32 CPU cores, which is not a suitable match for Fritz's granularity of 72 cores.

## Solution
- The user was advised to use the Woody cluster instead, which has nodes with 32 cores, matching the user's job size requirement.
- The user's account was set up, and they were provided with instructions for password setup and introductions to HPC resources.

## Follow-up
- The user's account was successfully created and activated on the Woody cluster.
- The user was informed about the availability of their account and provided with relevant support resources.

This analysis can help support employees to understand the importance of matching job requirements with appropriate clusters and the process of account setup for new users.
---

### 2024091142000091_Tier3-Access-Fritz%20%22Jonas%20Rock%22%20_%20v112ef10.md
# Ticket 2024091142000091

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject: Tier3-Access-Fritz "Jonas Rock" / v112ef10

### Keywords:
- Account Activation
- Multi-node Workload
- HDR100 Infiniband
- AVX-512 Vectorized Path Tracer
- LIKWID
- Benchmarking
- KONWIHR Project

### Summary:
- **User Request:** Access to Fritz for a multi-node workload with specific hardware requirements.
- **Hardware Requirements:** HDR100 Infiniband with 1:4 blocking, 72 cores, 250 GB per node.
- **Software Requirements:** Standard Linux build system, LIKWID.
- **Application:** Testing and evaluation of an AVX-512 vectorized path tracer.
- **Expected Results:** Benchmark and analysis results.

### Actions Taken:
- **HPC Admin:** Automatically activated the user's account on Fritz.

### What Can Be Learned:
- **Account Activation Process:** Automatic account activation for approved requests.
- **Hardware and Software Requirements:** Understanding user needs for specific hardware and software setups.
- **Project Details:** Importance of documenting project details for future reference.

### Root Cause of the Problem:
- User needed access to specific HPC resources for their project.

### Solution:
- Account was automatically activated by the HPC Admin, providing the user with the necessary access.
```
---

### 2024121242002151_Tier3-Access-Fritz%20%22Alexander%20Raphael%20Groos%22%20_%20gwgi021h.md
# Ticket 2024121242002151

 # HPC Support Ticket Analysis

## Keywords
- Tier3 Access
- Fritz
- Single-node throughput
- Python, PyTorch, TensorFlow
- Climate data modeling
- Glacier surface mass balance
- Regional climate data
- European Alps
- Mountain regions
- Open-source model

## Summary
- **User Request**: Access to Fritz for single-node throughput (72 cores, 250 GB) for 100,000 node hours.
- **Software Needed**: Python, PyTorch, TensorFlow.
- **Application**: Statistical downscaling of climate data and regional glacier surface mass balance modeling.
- **Expected Results**: New open-source glacier surface energy balance model and revised glacier projections for the European Alps and other mountain regions until 2100.

## Root Cause
- User required special justification for single-node throughput.

## Solution
- HPC Admin granted access to Fritz with the user's account.

## General Learnings
- Users need to provide detailed justifications for resource-intensive requests.
- HPC Admins can approve access based on the provided justifications.
- Common applications include climate data modeling and regional glacier studies.
- Key software tools for such applications are Python, PyTorch, and TensorFlow.

## Documentation for Support Employees
- Ensure users provide detailed justifications for high resource requests.
- Verify the required software and applications before granting access.
- Communicate approval decisions clearly to the user.

---

This documentation can be used to handle similar requests for resource-intensive applications in the future.
---

### 2022031142000514_meggie%20jobs.md
# Ticket 2022031142000514

 ```markdown
# HPC Support Ticket: Meggie Jobs Issue

## Subject
meggie jobs

## User Issue
1. Jobs running longer than expected (~28 hours).
2. Jobs stuck in the queue for three days without any progress.

## Root Cause
1. **Long Running Jobs**: Meggie has been very busy.
2. **Queue Delay**: Scheduling is based on fairshare, not the order of job submission. User's jobs are single-core, not suited for Meggie's multi-node parallel workload.

## Solution
- **Long Running Jobs**: No specific solution provided; users should expect delays during busy periods.
- **Queue Delay**: Users should submit jobs that utilize multiple cores to better suit Meggie's architecture.

## Keywords
- Meggie
- Job scheduling
- Fairshare
- Single-core jobs
- Multi-node jobs
- Queue delay

## General Learnings
- Meggie is designed for parallel multi-node jobs.
- Scheduling is based on fairshare, not the order of job submission.
- Single-core jobs are not well-suited for Meggie and may experience delays.
```
---

### 2022121542003032_Wiederholtes%20Absturzen%20von%20Starccm%2B%20auf%20den%20front%20end%20nodes.md
# Ticket 2022121542003032

 # HPC Support Ticket: Repeated Crashes of StarCCM+ on Front End Nodes

## Keywords
- StarCCM+
- Front end nodes
- CPU-hours limit
- Process-Checker
- Interactive job
- Post-processing
- Local visualization

## Problem Description
The user reported repeated crashes of StarCCM+ on the front end nodes while performing post-processing of simulations. The software crashed even during simple tasks like saving files, which had previously worked without issues.

## Root Cause
The crashes were due to the user exceeding the 8 CPU-hours limit imposed on the front end nodes. This limit is the sum of the runtime of all started threads/processes, not the real-time duration. The front end nodes are not intended for resource-intensive work to avoid impacting other users.

## Solution
1. **Avoid Resource-Intensive Tasks on Front End Nodes**: The user should avoid running resource-intensive applications like StarCCM+ on the front end nodes.
2. **Interactive Job**: Initially, it was suggested to start the StarCCM+ GUI via an interactive job or log in via SSH to the requested node. However, this was later clarified as not possible.
3. **Local Visualization**: The recommended solution is to copy the simulation files to a local machine and perform the visualization locally.

## Lessons Learned
- Front end nodes have a CPU-hours limit to prevent resource-intensive tasks from affecting other users.
- Users should be aware of the limitations of front end nodes and use them accordingly.
- For resource-intensive tasks, users should consider using compute nodes or local machines for post-processing.
- Clear communication about the capabilities and limitations of the HPC resources is crucial for user satisfaction and system efficiency.

## Follow-Up Actions
- Ensure users are informed about the CPU-hours limit on front end nodes.
- Provide guidance on how to perform post-processing on local machines or request interactive jobs if applicable.
- Monitor and update documentation to reflect the correct procedures for using HPC resources.
---

### 2023072542001827_Fritz%20_%20metadynamics%20_%20gromacs_2021.4-gcc11.2.0-ompi-mkl-plumed.md
# Ticket 2023072542001827

 # HPC Support Ticket Analysis: Metadynamics Simulation Issues

## Keywords
- Metadynamics
- GROMACS
- Segmentation Fault
- Job Placement
- Debugging
- MPI
- Process Placement

## Problem Description
- User ran metadynamics MD simulations using GROMACS on the HPC cluster.
- One simulation crashed with a segmentation fault (signal 11).
- Another simulation's end time shifted unexpectedly.

## Root Cause
- The segmentation fault suggests a potential issue with the code or memory access.
- The shifting end time of the simulation could be due to various factors, including hardware issues or job scheduling.

## Ticket Conversation Summary
- User reported issues with metadynamics simulations.
- HPC Admin suggested that the job placement is unlikely the cause.
- Discussion on MPI process placement and potential conflicts.
- HPC Admin advised reproducing the issue and using a debugger.

## Solution
- Reproduce the issue to identify the root cause.
- Use a debugger to analyze the segmentation fault.
- Review job scheduling and MPI process placement settings.

## General Learnings
- Segmentation faults often indicate issues with code or memory access.
- Job scheduling and MPI process placement settings can affect simulation performance.
- Reproducing issues and using debuggers are essential for troubleshooting.

## References
- [Stack Overflow Post on Segmentation Fault](https://stackoverflow.com/questions/71074993/caught-signal-11-segmentation-fault-address-not-mapped-to-object-at-address-n)
- [Intel MPI Environment Variables](https://www.intel.com/content/www/us/en/docs/mpi-library/developer-reference-windows/2021-8/hydra-environment-variables.html#I_MPI_JOB_RESPECT_PROCESS_PLACEMENT)
---

### 2018051742000633_Request%20for%20priority%20access%20on%20HPC.md
# Ticket 2018051742000633

 # HPC Support Ticket: Request for Priority Access

## Keywords
- Priority access
- HPC clusters (Woody, Emmy)
- Fairshare adjustment
- Conference deadline
- KONWIHR project

## Summary
- **User Request**: Priority access to HPC clusters for urgent simulations before an international conference.
- **Root Cause**: Upcoming conference deadline requiring additional computational resources.
- **Solution**: Increased fairshare for specified users; advised to minimize usage by other group members to boost priority.

## Details
- **Request**: User requested priority access to Woody and Emmy clusters for two colleagues to complete simulations before an international conference.
- **Admin Response**:
  - Clusters are full; no miracles expected.
  - Fairshare increased for specified users.
  - Advised to reduce usage by other group members to enhance priority.
  - Noted that frequent special boost requests are not encouraged.
- **Additional Information**:
  - KONWIHR project proposals reviewed twice a year; next window in approximately 5 months.

## Lessons Learned
- **Resource Management**: Adjusting fairshare can help prioritize urgent tasks.
- **User Responsibility**: Users can influence priority by managing group usage.
- **Proposal Timing**: Be aware of proposal review cycles for future planning.

## Action Items
- **HPC Admins**: Monitor fairshare adjustments and cluster usage.
- **Users**: Plan ahead for resource-intensive tasks and be mindful of group usage.

## Follow-Up
- **HPC Admins**: Ensure fairshare adjustments are effective and monitor overall cluster load.
- **Users**: Provide feedback on the effectiveness of the fairshare adjustment and any further needs.
---

### 2019021442000562_Elmer_Ice%20profiling.md
# Ticket 2019021442000562

 # Elmer/Ice Profiling Support Ticket

## Keywords
- Elmer/Ice
- Profiling
- Performance Analysis
- Fortran
- HPC Support
- MATC
- Solver Timings
- Log Level
- Flop Rate
- Speicherbandbreite

## Summary
A user encountered performance issues with their Elmer/Ice application and sought assistance with profiling their Fortran code. The user initially attempted profiling using the `-pg` compiler option but had limited success. The HPC support team provided guidance and collaborated with the user to identify and address performance bottlenecks.

## Root Cause
- The user's initial profiling attempts were unsuccessful due to the complexity of the Elmer/Ice codebase and the difficulty in identifying hotspots.
- The use of MATC (Material Calculator) functions was identified as a significant performance bottleneck.
- The user's code included small helper routines and libraries that appeared as major time consumers, obscuring the actual performance issues.

## Solution
- The HPC support team suggested using a lauffähiger Testfall that closely resembles the user's production environment.
- The team performed a Laufzeitprofil and measured Hardware Performance Counter to identify time-critical routines.
- The team discovered that MATC functions were slow and suggested moving away from MATC to user-defined subroutines written directly in Fortran.
- The team also recommended setting the Log level to 5 to obtain Solver timings and ensure they accumulate correctly to the Gesamtlaufzeit.
- The user was advised to validate the changes by testing the modified code and ensuring it still produces correct results.

## Lessons Learned
- Profiling complex applications like Elmer/Ice can be challenging, and initial attempts may not yield clear results.
- Collaboration with the HPC support team and external experts can provide valuable insights and solutions.
- Identifying and addressing performance bottlenecks in MATC functions can significantly improve application performance.
- Validating changes and ensuring correctness is crucial when optimizing code for performance.

## References
- Related tickets:
  - [2018121742001584](https://www.helpdesk.rrze.fau.de/otrs/index.pl?Action=AgentTicketZoom;TicketID=687869)
  - [2018121342001448](https://www.helpdesk.rrze.fau.de/otrs/index.pl?Action=AgentTicketZoom;TicketID=687397;ArticleID=2064050)
  - [2018111942001117](https://www.helpdesk.rrze.fau.de/otrs/index.pl?Action=AgentTicketZoom;TicketID=682710)
- External resources:
  - [Spack for building Elmer/Ice](https://github.com/spack/spack/pull/10860)
  - Contact with Mikko Byckling at Intel and Jens Weismüller at LRZ for additional performance insights.
---

### 2017071342002413_Segmentation%20fault%20bei%20sander.MPI.md
# Ticket 2017071342002413

 # HPC Support Ticket: Segmentation Fault bei sander.MPI

## Keywords
- Segmentation fault
- sander.MPI
- Stack size
- ulimit
- Fortran runtime environment

## Problem Description
- User encounters a segmentation fault when running `sander.MPI` on the HPC system.
- The error occurs with all available modules on the system.
- The process runs successfully in serial mode (`sander`) despite some error messages.
- A smaller system with the same inputs ran successfully earlier.

## Root Cause
- The Fortran runtime environment of `sander` requires more stack space than the default allocation for the user's input data.

## Solution
- Add the following line to the job script before the `mpirun/sander` call:
  ```bash
  ulimit -s unlimited
  ```
- This increases the stack size to unlimited, preventing segmentation faults.

## General Learnings
- Segmentation faults can be caused by insufficient stack size.
- Adjusting the stack size using `ulimit -s` can resolve such issues.
- Always check for stack size requirements when dealing with segmentation faults in MPI applications.

## Roles Involved
- **HPC Admins**: Provided the solution to increase stack size.
- **User**: Reported the issue and confirmed the solution worked.

## Conclusion
- Increasing the stack size using `ulimit -s unlimited` resolved the segmentation fault issue for the user's `sander.MPI` job. This solution can be applied to similar issues in the future.
---

### 2018102942000575_Fehler%20bei%20HPC%20Job%20Allokierung%20Lima%20Cluster.md
# Ticket 2018102942000575

 ```markdown
# HPC Support Ticket: Fehler bei HPC Job Allokierung Lima Cluster

## Problem Description
- User's jobs on the Lima Cluster were allocating 6 nodes but only utilizing one, leading to resource wastage.
- High load (60) on the single utilized node indicated a potential issue in the job script.

## Root Cause
- The user's job script was designed to run multiple serial processes on a single node, leading to inefficient resource utilization.
- The user misunderstood the allocation of nodes and processors, resulting in idle nodes.

## Solution
- The HPC Admin explained that requesting multiple nodes does not automatically distribute the workload across those nodes.
- The user was advised to split the work into single-node jobs and use a local work scheduler like GNU parallel to manage the execution.
- The user agreed to distribute the jobs as single-node jobs, which would be more efficient for their non-parallelizable C++ program.

## Keywords
- Resource wastage
- Job script issue
- Single-node jobs
- GNU parallel
- Load distribution

## General Learnings
- Understanding the difference between node allocation and actual resource utilization is crucial for efficient job scheduling.
- Serial jobs should be managed using local work schedulers to optimize resource usage.
- Proper communication and guidance from HPC Admins can help users optimize their job scripts and improve overall system performance.
```
---

### 2021121542002553_Jobs%20auf%20Woody%20-%20mpwm027h.md
# Ticket 2021121542002553

 # HPC Support Ticket: Short Job Durations on Woody

## Keywords
- Short job durations
- High job volume
- Cluster load
- Dateiserver load
- Job scheduling
- Bug in user code

## Problem Description
- User submitted over 4,000 jobs on Woody, with most jobs running for only a few seconds.
- This created an extreme load on the cluster and dateiservers, affecting all HPC users.

## Root Cause
- A bug in the user's code caused jobs to terminate early or have very short runtimes.

## Impact
- High volume of short jobs led to excessive load on the cluster and dateiservers.
- Negatively impacted the performance and availability of HPC resources for other users.

## Solution
- User acknowledged the issue and attributed it to a bug in their code.
- HPC Admin adjusted the `maui.cfg` configuration to mitigate the impact.

## Lessons Learned
- Users should monitor job durations to ensure they are not excessively short.
- High volume of short jobs can significantly impact cluster performance.
- Regular communication with users is essential to address and resolve issues promptly.
- Adjusting job scheduling configurations can help manage cluster load.

## Follow-up Actions
- Users should fix bugs in their code to prevent short job durations.
- HPC Admins should continue monitoring job durations and cluster load.
- Regularly review and adjust job scheduling configurations as needed.
---

### 2023080942001712_Assistance%20Needed%20for%20Running%20Large%20Video%20Compression%20Job%20on%20HPC%20Cluster.md
# Ticket 2023080942001712

 # HPC Support Ticket: Assistance Needed for Running Large Video Compression Job on HPC Cluster

## Summary
- **User Issue**: Out of Memory (OOM) error when processing large video files (~300GB) using WinRAR for compression.
- **Error Message**: `slurmstepd-tg090: error: Detected 1 oom-kill event(s) in StepId=633181.0. Some of your processes may have been killed by the cgroup out-of-memory handler. srun: error: tg090: task 0: Out Of Memory`
- **Cluster**: tinyx (frontend for tinygpu and tinyfat)
- **Job Submission Script**: Uses `srun python HPC_COMP_FINAL.py`

## Root Cause
- **Memory Allocation**: The job requires more memory than available (128 GB RAM).
- **Incorrect Cluster**: Job submitted to tinygpu instead of tinyfat.

## Solutions
1. **Memory Optimization**:
   - Process files in chunks to reduce memory usage.
   - Use a cluster with more memory (tinyfat).

2. **Correct Job Submission**:
   - Use `sbatch.tinyfat` for job submission to tinyfat.
   - Remove `srun` if not using MPI.

## Key Learnings
- **Memory Management**: Large files should be processed in chunks to avoid OOM errors.
- **Cluster Selection**: Ensure the correct cluster is used for job submission.
- **Job Submission**: Use appropriate commands for job submission (`sbatch.tinyfat` for tinyfat).

## Additional Notes
- **Storage Location**: Consider using `$WORK` instead of `$HPCVAULT` for non-backup data.
- **GPU Allocation**: Ensure GPU resources are not requested unnecessarily.

## Follow-up
- **Job ID**: Provide the job ID of a failed job for further investigation if the issue persists.

---

This documentation provides a summary of the issue, root cause, solutions, key learnings, and additional notes for future reference in handling similar errors.
---

### 2023080442001178_Freischaltung%20high-memory%20Knoten.md
# Ticket 2023080442001178

 # HPC Support Ticket: Freischaltung high-memory Knoten

## Keywords
- High-memory nodes
- Freischaltung
- NHR@FAU Projekt
- 1TB RAM
- 2TB RAM
- Aeroacoustik-Simulation
- Partition spr1tb
- Partition spr2tb

## Problem
- User requested access to high-memory nodes for their project (b145dc, group ID 80086) for an aeroacoustics simulation requiring significant RAM.
- Initial request did not receive a timely response, causing delays in accessing the required resources.

## Solution
- HPC Admins granted access to the 1TB RAM nodes (partition spr1tb) after the initial request.
- User subsequently requested access to the 2TB RAM nodes, which was also granted (partition spr2tb).

## Lessons Learned
- **Communication**: Ensure timely responses to user requests to avoid delays in project work.
- **Resource Allocation**: High-memory nodes are crucial for memory-intensive applications like aeroacoustics simulations.
- **Documentation**: Provide clear instructions on how to request and utilize high-memory nodes, including any specific requirements for batch files.

## Action Items
- **HPC Admins**: Monitor and respond promptly to user requests for resource allocation.
- **2nd Level Support Team**: Assist users in understanding and utilizing high-memory nodes effectively.
- **Training and Support Group Leader**: Ensure documentation is up-to-date and accessible for users needing high-memory nodes.

## Root Cause
- Delay in response to the initial request for high-memory node access.

## Resolution
- Access to both 1TB and 2TB RAM nodes was granted, allowing the user to proceed with their simulation.

## Follow-up
- Ensure users are aware of the partitions (spr1tb and spr2tb) and how to request them in their batch files.
- Provide any additional support needed for the aeroacoustics simulation.
---

### 2022092142004571_Alternative%20zu%20HPC%20Meggie%20f%C3%83%C2%BCr%20StarCCM%20Simulationen.md
# Ticket 2022092142004571

 # HPC Support Ticket Conversation Summary

## Key Points Learned

- **Meggie Cluster Availability**: The Meggie cluster is available, but the `$FASTTMP` filesystem is unavailable due to a hardware defect. Simulations can be run on Meggie and output can be written to other filesystems, though this may increase simulation time due to slower network connectivity.
- **Grundversorgung on Fritz**: Users can apply for Grundversorgung on Fritz by filling out a form. The upper limit for Grundversorgung is the same as the lower limit of an NHR normal project, which is 1 million core-hours for the entire group.
- **NHR Application**: For larger computational needs, an NHR application is required, which can be submitted without a DFG-funded project.
- **Star-CCM+ Version**: An older version of Star-CCM+ (2020.2) was installed on Meggie to ensure project consistency. Passwordless SSH between nodes was re-enabled to support this version.
- **Batch Script Issues**: Initial batch scripts for Star-CCM+ did not work due to compatibility issues. A correct example script was provided, and the `--batchsystem slurm` option is mandatory for proper process startup.
- **Approval Time**: The approval time for Grundversorgung applications is expected to be a few days, much shorter than the 3-4 weeks typically required for NHR applications.

## Root Cause and Solution

- **Root Cause**: The primary issue was the unavailability of the `$FASTTMP` filesystem and compatibility problems with the Star-CCM+ version.
- **Solution**: Users were advised to run simulations on Meggie and write output to other filesystems. An older version of Star-CCM+ was installed, and passwordless SSH was re-enabled. Correct batch scripts were provided to ensure proper process startup.

## Keywords

- Meggie Cluster
- Grundversorgung
- NHR Application
- Star-CCM+
- Batch Script
- Passwordless SSH
- Simulation Output
- Network Connectivity
- Core-Hours
- Approval Time

## Conclusion

The ticket conversation highlights the importance of understanding the availability and limitations of different filesystems and the necessity of proper version compatibility for software used in HPC environments. The support team provided timely solutions and guidance to ensure the user could continue their work effectively.
---

### 2023071842003213_Multi-node%20access%20Alex%20-%20b182dc10.md
# Ticket 2023071842003213

 # HPC Support Ticket: Multi-node Access Request

## Keywords
- Multi-node jobs
- DAREXA-F user
- Group access
- qos=a100multi

## Summary
A user requested multi-node job access for their DAREXA-F user account and the associated group.

## Problem
- User requested multi-node job access for their specific user account and the entire group.

## Solution
- The HPC Admin enabled the group for `qos=a100multi`.

## Lessons Learned
- Users can request multi-node job access for specific accounts or groups.
- HPC Admins can enable groups for specific quality of service (QoS) settings.
- Communication with HPC Admins is essential for enabling advanced features.

## Action Taken
- The group `b182dc` was enabled for `qos=a100multi` by the HPC Admin.

## Follow-up
- Ensure that users are aware of the process for requesting multi-node job access.
- Document the steps for enabling QoS settings for future reference.
---

### 2023061642000203_Maximum%20allreduce%20size%3F.md
# Ticket 2023061642000203

 # HPC-Support Ticket Conversation: Maximum allreduce size?

## User Issue
- User encountered an upper limit on the size of allreduces in the current Intel-MPI installation.
- Assertion failed in file `intel_transport_allreduce.h` at line 1129: `frame_size <= SHM_NODE_ALLREDUCE_LARGE_PAYLOAD_SIZE`.
- User requested the size limit for allreduces and whether it can be modified in the environment to allow for larger allreduces.

## HPC Admin Response
- Suggested increasing the debug level to gather more information.
- Provided a link to Intel's documentation on `I_MPI_COLL*` environment variables.
- Suggested adjusting `I_MPI_COLL_INTRANODE_SHM_THRESHOLD`.
- Provided a link to a relevant thread on Intel's community forum.

## User Testing
- User tested different values for `I_MPI_ADJUST_ALLREDUCE` and found that values 5 and 6 were beneficial for their algorithm at the given size.

## Solution
- The issue was resolved by setting `I_MPI_ADJUST_ALLREDUCE=8` in the submit script.

## Additional Information
- The user shared the results of their instrumentations, which can help with future problems of other users.

## Conclusion
- The ticket was closed as the user was satisfied with the solution.
---

### 2024022842000491_VTK%20visualization.md
# Ticket 2024022842000491

 # VTK Visualization Job Issues

## Keywords
- VTK visualization
- Volume rendering
- Job submission
- PENDING status
- Visualization node
- Kernel memory leakage
- NVIDIA GPU drivers
- Health check
- Slurm
- `sbatch`
- `squeue`
- `sacct`
- `$FASTTMP`

## Summary
A user experienced issues with VTK visualization jobs getting stuck in PENDING status. The problem was intermittent and related to the visualization node and potential kernel memory leakage triggered by the job.

## Root Cause
- **Access Control**: Initially, the visualization queue had access control enabled, causing job rejection.
- **Node Maintenance**: The visualization node required additional prodding after maintenance to function correctly.
- **Kernel Memory Leakage**: The job triggered a health check for kernel memory leakage, possibly due to high memory usage by NVIDIA GPU drivers.

## Solutions
- **Access Control**: Removed access control from the visualization queue.
- **Node Maintenance**: Rebooted the visualization node to resolve maintenance-related issues.
- **Health Check**: Increased the warning threshold for the memory leak check to accommodate high memory usage by GPU drivers.

## User Job Details
- **Data Location**: `$FASTTMP` (/lustre/b159cb/b159cb11/varying-forcing/orangutan/N0512_kMeta3.0_P16384)
- **Data Size**: 2.3TB (0.8TB accessed during the job)
- **File Size**: 4.6GB each (1.6GB relevant data per file)
- **Number of Files**: 512

## Monitoring
- **Memory Usage**: High kernel memory usage during jobs, but returns to low levels afterward.
- **Health Check**: Regularly monitor memory usage to detect potential long-term memory leaks.

## Documentation
- **User Guide**: [HPC Documentation on Remote Visualization](https://hpc.fau.de/systems-services/documentation-instructions/clusters/fritz-cluster/#remotevis)

## Conclusion
The issue was resolved by addressing access control, rebooting the node, and adjusting health check thresholds. Regular monitoring is recommended to prevent future issues.
---

### 2024061742002976_high%20cpu%20load%20-%20b172da10.md
# Ticket 2024061742002976

 ```markdown
# HPC Support Ticket: High CPU Load - b172da10

## Problem Description
- User's recent array jobs with JobID=1351906 showed unusually high CPU load according to cluster monitoring.
- User was calculating 16 large dense matrices (2^16 x 2^16) and parallelizing the calculations on 15 nodes.

## Root Cause
- The user's Python script used `multiprocessing.cpu_count()` to determine the number of cores, which led to oversubscription when running array jobs.
- Numpy/scipy libraries were using multithreading on top of the user's multiprocessing, causing high CPU load.

## Solution
- Set `export OMP_NUM_THREADS=1` in the job script to disable multithreading in numpy/scipy.
- Simplify the calculation to avoid unnecessary multiprocessing:
  ```python
  Hi_dot = ss.coo_matrix.dot(H_i, evec)
  result = np.dot(evec.T, Hi_dot)
  ```
- This approach was found to be faster and more efficient.

## Keywords
- High CPU load
- Multiprocessing
- Multithreading
- Oversubscription
- Array jobs
- Numpy/scipy
- OMP_NUM_THREADS

## General Learning
- Always check for multithreading in libraries when using multiprocessing.
- Disable multithreading if it causes oversubscription.
- Simplify calculations when possible to improve performance.
```
---

### 2023080742002224_jobs%20on%20fritz.md
# Ticket 2023080742002224

 # HPC Support Ticket: Jobs on Fritz

## Keywords
- Resource usage
- Job monitoring
- Parallel scalability benchmarks
- Single core runtime
- NHR user portal

## Summary
An HPC Admin contacted a user regarding multiple jobs on Fritz that appeared to be underutilizing resources. The user confirmed that these jobs were tests for parallel scalability benchmarks and requested information about single core runtimes on similar nodes.

## Root Cause
- User was running parallel scalability benchmarks, which might have appeared as improper resource usage.

## Solution
- HPC Admin encouraged the user to check their jobs using the monitoring system.
- User confirmed the nature of the jobs and provided additional context.

## What to Learn
- Always verify the nature of jobs with users if resource usage seems unusual.
- Encourage users to utilize the monitoring system to keep track of their jobs.
- Understand that benchmarking and testing might result in atypical resource usage patterns.

## Links
- [Monitoring System](https://monitoring.nhr.fau.de/monitoring/user/b168dc12?state=running)
- [NHR User Portal Access](https://hpc.fau.de/faq/how-can-i-access-a-link-to-monitoring-nhr-fau-de)

## Next Steps
- Continue monitoring the jobs to ensure they complete as expected.
- Provide the user with any requested information regarding single core runtimes if available.
---

### 2023110842000816_Job%20distribution%20between%20nodes.md
# Ticket 2023110842000816

 # HPC Support Ticket: Job Distribution Between Nodes

## Keywords
- MPI ranks
- SLURM
- CPU distribution
- `--distribution=block:block,pack`
- `srun`
- `SLURM_TASKS_PER_NODE`

## Problem
- User wants to distribute 160 MPI ranks across 3 nodes (72 CPUs per node) with a specific distribution pattern (`SLURM_TASKS_PER_NODE=72(x2),16`).
- Default SLURM distribution is `SLURM_TASKS_PER_NODE=54,53(x2)`.
- User tried `--distribution=block:block:block,pack` without success.

## Root Cause
- The default distribution shown by `SLURM_TASKS_PER_NODE` is generated at resource allocation with `sbatch`.
- The user's script should overwrite this default distribution with `srun --distribution=block:block,pack`.

## Solution
- Verify the distribution by adding `srun -m block:block,pack -n 160 hostname | sort | uniq -c` at the top of the job script.
- Ensure `--cpus-per-task=1` is propagated to `srun` by either re-adding the option or using `export SRUN_CPUS_PER_TASK=$SLURM_CPUS_PER_TASK`.

## General Learning
- SLURM's default distribution can be overwritten by `srun` options.
- Verify task distribution within the job script using `srun` and `hostname`.
- Ensure CPU per task settings are correctly propagated to `srun`.

## Roles Involved
- HPC Admins
- 2nd Level Support Team
- Head of the Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support
- Software and Tools Developer
---

### 2024111842001714_Request%20for%20Multi-Node%20Alex%20Access.md
# Ticket 2024111842001714

 ```markdown
# HPC Support Ticket Conversation Analysis

## Subject: Request for Multi-Node Alex Access

### Keywords
- Multi-node access
- Alex cluster
- Fritz
- Testfront
- Hiwi
- Portal account
- GPU access
- QoS specification
- Job script error

### Summary
A user requested access to multiple HPC systems (Fritz, Alex, Testfront) for a Hiwi. The process involved creating a portal account, enabling access to the required systems, and troubleshooting multi-node access issues on the Alex cluster.

### Key Learnings
1. **Account Creation**:
   - The user provided the Hiwi's email address for portal account creation.
   - The HPC Admin created the portal account and enabled access to the required systems.

2. **Multi-Node Access**:
   - The user requested multi-node access on the Alex cluster for GPU communication.
   - The HPC Admin enabled the account on Alex but encountered issues with multi-node access.

3. **Troubleshooting**:
   - The user reported an error with the job script due to an invalid QoS specification.
   - The HPC Admin was notified to resolve the multi-node access issue.

### Root Cause of the Problem
- The job script error was due to an invalid QoS specification, indicating that multi-node access was not properly configured.

### Solution
- The HPC Admin needs to ensure that the multi-node access configuration is correctly set up for the user's account.
- The user should verify the QoS specification in the job script and ensure it matches the available configurations.

### Next Steps
- The HPC Admin should review the multi-node access configuration for the user's account.
- The user should check the job script for the correct QoS specification and resubmit the job.

### Additional Notes
- The user also requested access to specific Testfront nodes, which were eventually enabled.
- The process involved multiple steps and required coordination between the user and the HPC Admin.
```
---

### 2024020842002937_Concurrent%20MPI%20Jobs.md
# Ticket 2024020842002937

 # Concurrent MPI Jobs Issue

## Keywords
- MPI
- Concurrent Jobs
- srun
- mpirun
- Multi-prog
- Environment Variables

## Problem Description
- User has two separate MPI communicators.
- The first application sends data to the second one for processing.
- The user runs the MPI concurrent jobs using `srun`.
- Data passing between applications fails on the current cluster but works on a different cluster with the Cray compiler.

## Root Cause
- The issue might be related to the specific configuration or environment of the current cluster.

## Solutions
1. **Use `mpirun` instead of `srun`:**
   ```bash
   mpirun -n 720 ./application1 : -n 72 ./application2
   ```
   - No need for the `-N` flag.
   - Ensure the module with which the application is built is loaded.

2. **Use `srun` with the `--multi-prog` argument:**
   ```bash
   srun -n 792 -l --multi-prog silly.conf
   ```
   - `silly.conf` should contain:
     ```
     0-719        ./application1
     720-791      ./application2
     ```

## Outcome
- The user confirmed that the suggested solutions worked well.

## General Learnings
- Different clusters may require different configurations for MPI jobs.
- Using `mpirun` instead of `srun` can sometimes resolve issues.
- The `--multi-prog` argument in `srun` can be used to run multiple programs in a single job step.
---

### 2022012842000951_Jobs%20auf%20emmy%20%7C%20mppi087h.md
# Ticket 2022012842000951

 # HPC Support Ticket: Jobs auf emmy | mppi087h

## Keywords
- Job submission
- Node allocation
- Queue management
- Certificate expiration
- Python

## Summary
- **Root Cause**: User submitted multiple jobs requesting 4 nodes but only utilizing 1 node.
- **Solution**: HPC Admin deleted the pending jobs and advised the user to resubmit with the correct node allocation (`nodes=1`).

## Details
- **Issue**: User submitted several hundred jobs on `emmy` requesting 4 nodes but only using 1 node.
- **Action Taken**: HPC Admin deleted the jobs that had not yet started.
- **Advice**: User was advised to resubmit jobs with the correct node allocation (`nodes=1`).
- **Additional Note**: There was a mention of an expired certificate, but no specific action was detailed regarding this issue.

## Lessons Learned
- Ensure proper node allocation when submitting jobs to avoid wasting resources.
- Regularly check job submissions to identify and correct inefficient resource usage.
- Communicate with users through available channels (e.g., ECAP-Chat) to provide guidance and resolve issues promptly.

## Follow-Up
- Monitor job submissions for similar issues.
- Provide training or documentation on proper job submission practices to prevent recurrence.
---

### 2022081642002512_ARM%20Server%20mit%20SVE.md
# Ticket 2022081642002512

 # HPC-Support Ticket Conversation: ARM Server mit SVE

## Keywords
- ARM Architecture
- SVE Befehlssatz
- Fujitsu A64FX Systeme
- NHR@KIT
- LRZ BEAST Cluster

## Problem
- User inquires about the availability of ARM architecture-based computing resources with the new SVE instruction set at RRZE.

## Solution
- RRZE does not currently operate any SVE-capable systems.
- NHR@KIT operates Fujitsu A64FX systems with SVE in the Future Technologies Partition.
- LRZ also has Fujitsu A64FX systems in the BEAST Cluster.

## What Can Be Learned
- RRZE does not have ARM architecture-based systems with SVE.
- NHR@KIT and LRZ are alternative centers with Fujitsu A64FX systems supporting SVE.
- Users interested in SVE-capable systems should contact NHR@KIT or LRZ.

## References
- [NHR@KIT Future Technologies Partition](https://www.nhr.kit.edu/userdocs/ftp/)
- [LRZ BEAST Cluster](https://www.lrz.de/presse/ereignisse/2020-11-06_BEAST/)
---

### 2024021342000778_HPC-Kurskennungen%20f%C3%83%C2%BCr%20PPHPS24%2020.-22.2.2024.md
# Ticket 2024021342000778

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject
HPC-Kurskennungen für PPHPS24 20.-22.2.2024

## Keywords
- HPC Accounts
- Course Reservation
- Batch System
- Username + Password
- Node Reservation
- Slurm
- sacctmgr
- COMA

## Summary
A user requested the setup of 30 HPC course accounts for a specific course (PPHPS24) with a specified duration and node reservation on the "fritz" system. The HPC Admin provided details about the course setup and reservations.

## User Request
- **Accounts**: 30 HPC course accounts
- **Duration**: From immediate until 23.2.2024
- **System**: fritz
- **Course**: PPHPS24
- **Reservation**: 28 nodes for specified time periods

## HPC Admin Actions
- **Account Setup**: Created accounts with specific details
  - `sacctmgr add account k_z34d set descr="pphps24-kurs, feb 2024 - gha" parent=fau`
  - `/root/bin/slurm-add-acct_v3.py -c fritz --skip-all --no-new-accounts --whitelist z34d --limits "-1 -1 4"`
- **Reservation Setup**: Created reservations for specified time periods
  - `ReservationName=PPHPS24-1 StartTime=2024-02-20T10:30:00 EndTime=2024-02-20T17:30:00`
  - `ReservationName=PPHPS24-2 StartTime=2024-02-21T09:00:00 EndTime=2024-02-21T17:30:00`
  - `ReservationName=PPHPS24-3 StartTime=2024-02-22T09:00:00 EndTime=2024-02-22T16:30:00`
- **Passwords**: Passwords were retrieved from COMA and sent via chat

## Lessons Learned
- **Account Setup**: Use `sacctmgr` and custom scripts for account setup
- **Reservation Setup**: Use specific commands to create node reservations
- **Password Management**: Retrieve passwords from COMA and distribute securely

## Root Cause of the Problem
The user needed HPC accounts and node reservations for a specific course.

## Solution
The HPC Admin set up the accounts and reservations as requested and provided the necessary passwords.
```
---

### 2024072542002404_Batch%20job%20interpretation.md
# Ticket 2024072542002404

 ```markdown
# HPC Support Ticket: Batch Job Interpretation

## Subject
Batch job and resource utilization confusion leading to OOM (Out of Memory) error.

## User Issue
- Two jobs: one finishes without error, the other results in an OOM error.
- Job1: Finishes successfully.
  - Total RAM usage: 91.1 GiB.
  - GPU utilization: 97%, memory utilization: 16%.
- Job2: Fails with OOM error.
  - Total RAM usage: 107.5 GiB.
  - GPU utilization: 97%, memory utilization: 17%.
- User suspects the issue is due to extra copies of images used in the training process in Job2.

## HPC Admin Response
- Job2 is killed due to "out of memory".
- Main memory usage might be the issue, not GPU memory.
- Node has 512GB main memory, and the user should be able to use 128GB.
- Suggested to try different values for data distribution to find the impact on memory requirements.

## Key Points Learned
- **OOM Error**: Job2 failed due to an OOM error, likely caused by increased memory usage from extra image copies.
- **Resource Utilization**:
  - GPU utilization and memory utilization were similar in both jobs.
  - Main memory usage differed significantly (91.1 GiB vs. 107.5 GiB).
- **Graph Interpretation**:
  - CPU load graph y-axis represents the load average.
  - Mem_used graph y-axis represents memory usage in GB.
  - A100 GPUs have 40GB RAM, but the y-axis on the CPU load graph can exceed 40 due to the load average metric.

## Solution
- Reduce the number of image copies used in the training process to lower memory usage.
- Monitor main memory usage and adjust data distribution to optimize memory requirements.

## Additional Notes
- Understanding job statistics and graphs can help in analyzing and fixing memory-related issues.
- Main memory usage should be considered along with GPU memory usage when diagnosing OOM errors.
```
---

### 2023012942000279_slow%20mpi%20communication%20%5Bproject%20b166ea%5D.md
# Ticket 2023012942000279

 # HPC Support Ticket: Slow MPI Communication in AREPO Simulation

## Subject
Slow MPI communication in strong scaling test for hydrodynamics simulation using AREPO.

## User Description
- **Issue**: MPI communication time does not scale well with the number of CPUs.
- **Code**: AREPO hydrodynamics simulation.
- **Modules**:
  - `intel/2021.4.0 intelmpi/2021.7.0 hdf5/1.10.7-intel fftw/3.3.10-ompi gsl/2.7`
  - Also tried with OpenMPI but it was slower.
- **Execute Command**: `srun -n 64 ./Arepo param.txt 2 217`

## HPC Admin Responses
- **Initial Response**:
  - Requested input files for further testing.
  - Suggested monitoring jobs for performance analysis.

- **Further Investigation**:
  - Asked if the issue is platform- or library-specific.
  - Inquired about the understanding of the program and if it is memory-bound.

- **Analysis**:
  - Identified that the communication-intensive components scale poorly on Fritz.
  - Noted that the code speed is satisfactory but scaling can be improved.
  - Observed that processes were not pinned and distributed randomly to different CPUs.

## User Clarifications
- **Project Details**:
  - Consists of a few hundred mid-sized simulations.
  - Code is capable of handling larger-scale simulations but not necessary for the current project.

- **Performance**:
  - Code speed is satisfactory.
  - Interested in improving scaling relation if possible.

## Solution
- **Resource Allocation**:
  - Ensure processes are pinned to specific CPUs.
  - Use `--ntasks-per-node=32` and `srun --exact --cpu-freq=2400000-2400000` to fix resource allocation.

## Conclusion
- The issue with MPI communication scaling is related to resource allocation.
- Proper pinning of processes and setting CPU frequency can improve performance.
- Further monitoring and performance analysis can be done if needed.

## Keywords
- MPI communication
- Strong scaling
- AREPO
- Resource allocation
- Performance analysis
- Hydrodynamics simulation

## Lessons Learned
- Proper resource allocation is crucial for optimal MPI communication.
- Monitoring jobs can help identify performance bottlenecks.
- Pinning processes to specific CPUs can improve scaling.
---

### 2022030242000728_Hohe%20Load%20auf%20Emmy-Knoten%20%28mpt1010h%20Patrick%20Adelhardt%29.md
# Ticket 2022030242000728

 # HPC Support Ticket: High Load on Emmy Nodes

## Keywords
- High load
- Oversubscription
- MPI configuration
- Performance optimization
- Memory bandwidth
- Gleitkomma-Performance
- Job imbalance

## Summary
The user's jobs were causing high load on the Emmy nodes, with up to 160 processes on nodes with 40 hyperthreads. This was not intentional and was caused by appending commands to the MPI configuration file instead of overwriting it. Additionally, the jobs showed performance issues with low memory bandwidth and Gleitkomma-Performance.

## Root Cause
- Incorrect handling of MPI configuration file leading to oversubscription.
- Inefficient job distribution causing imbalances and poor resource utilization.

## Solution
- The user identified and fixed the issue with the MPI configuration file.
- HPC Admins offered to analyze the code for performance optimization.
- A Zoom meeting was scheduled to discuss and address the performance issues.

## Lessons Learned
- Avoid oversubscribing nodes by starting more processes than the available hyperthreads.
- Regularly monitor job performance and resource utilization.
- Properly manage MPI configuration files to prevent unintentional job submissions.
- Collaborate with HPC Admins for performance analysis and optimization.

## Next Steps
- Continue monitoring job performance.
- Implement suggested optimizations from the performance analysis.
- Ensure proper handling of MPI configuration files in future job submissions.

## References
- HPC Services, Friedrich-Alexander-Universitaet Erlangen-Nuernberg
- Regionales RechenZentrum Erlangen (RRZE)
- [HPC Support Email](mailto:support-hpc@fau.de)
- [HPC Website](http://hpc.fau.de/)
---

### 2020021742003337_Reboot%20woody3%3F.md
# Ticket 2020021742003337

 # HPC Support Ticket: Reboot woody3?

## Keywords
- Reboot
- woody3
- Job loss
- Frontend
- Cluster nodes

## Summary
A user inquired about the potential impact of a scheduled reboot on running jobs.

## Root Cause
- woody3 announced a reboot at 8:15 AM the next day.
- User was concerned about the potential loss of running jobs.

## Solution
- **HPC Admin** clarified that the reboot only affected the frontend.
- Cluster nodes were unaffected, so running jobs on the cluster were not lost.
- Any processes running directly on woody3 were lost.

## Lessons Learned
- Rebooting the frontend does not impact running jobs on the cluster nodes.
- Processes running directly on the frontend will be lost during a reboot.
- Clear communication about the scope of maintenance activities can alleviate user concerns.

## Action Taken
- **HPC Admin** provided reassurance that cluster jobs were not affected.
- User acknowledged the information.

## Future Reference
- When scheduling maintenance, specify which components will be affected.
- Ensure users understand the distinction between frontend and cluster nodes.
---

### 2024031342002569_Tier3-Access-Fritz%20%22Dinesh%20Parthasarathy%22%20_%20iwia058h.md
# Ticket 2024031342002569

 ```markdown
# HPC Support Ticket Conversation Analysis

## Subject
Tier3-Access-Fritz "Dinesh Parthasarathy" / iwia058h

## Keywords
- Account Enablement
- Multi-node Workload
- HDR100 Infiniband
- HyTeG
- EvoStencils
- Genetic Programming
- Finite Element Simulation
- Multigrid Solvers

## Summary
- **User Request**: A user requested access to the Fritz HPC system for a multi-node workload.
- **Resource Requirements**:
  - Multi-node workload with HDR100 Infiniband with 1:4 blocking.
  - Per node: 72 cores, 250 GB.
  - 400 node hours on Fritz.
- **Software Requirements**:
  - HyTeG: C++ framework for large-scale high-performance finite element simulations.
  - EvoStencils: Genetic Programming framework for the automatic design of multigrid solvers.
- **Application**: Use Genetic Programming to find optimal multigrid solvers in the finite element simulation framework.
- **Expected Results**: Understanding/discovery of optimal multigrid cycles for a given problem.

## Actions Taken
- **HPC Admin**: The HPC Admin enabled the user's account on Fritz.

## Lessons Learned
- **Account Enablement Process**: The ticket highlights the process of enabling a user account on the Fritz HPC system.
- **Resource Allocation**: Understanding the specific resource requirements for multi-node workloads, including cores, memory, and interconnect specifications.
- **Software Requirements**: Identifying the specific software frameworks required for the user's research, such as HyTeG and EvoStencils.
- **Application of Genetic Programming**: The use of Genetic Programming for optimizing multigrid solvers in finite element simulations.

## Root Cause of the Problem
- The user required access to the Fritz HPC system for a specific research project involving multi-node workloads and specialized software.

## Solution
- The HPC Admin enabled the user's account on Fritz, granting them the necessary access to perform their research.
```
---

### 2022020442001609_Early-Fritz%20%22Sven%20Maisel%22%20_%20bctc39.md
# Ticket 2022020442001609

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject: Early-Fritz "Sven Maisel" / bctc39

### Keywords:
- Early-Fritz
- Infiniband-Karten
- Partition "singlenode"
- VASP
- Ab-initio molecular dynamics simulations
- SCALMS catalysts

### Summary:
- **User Request:** Access to the Fritz cluster for single-node and multi-node workloads.
- **Resources Requested:** 72 cores, 250 GB RAM per job.
- **Software Needed:** VASP.
- **Application:** Ab-initio molecular dynamics simulations of liquid metals for catalysis research.
- **Expected Results:** New element combinations and support materials for SCALMS catalysts.

### Issues and Solutions:
- **Issue:** Limited availability of Infiniband cards due to supply shortages.
  - **Solution:** Most nodes are available in the "singlenode" partition with 72 cores and 250 GB RAM.
- **Issue:** Parallel file system not yet available.
  - **Solution:** Users should refer to the documentation for updates.
- **Issue:** VASP module not centrally available.
  - **Solution:** Awaiting a Makefile template.

### General Learnings:
- **Documentation:** Continuously updated at [Fritz Cluster Documentation](https://hpc.fau.de/systems-services/systems-documentation-instructions/clusters/fritz-cluster/).
- **MOTD:** Valuable information is provided upon logging into Fritz.
- **Software Availability:** Some software modules, like VASP, may not be immediately available due to pending templates.

### Root Cause of the Problem:
- **Limited Hardware Resources:** Supply shortages of Infiniband cards.
- **Software Availability:** Delay in the availability of the VASP module.

### Solution:
- **Hardware:** Use the "singlenode" partition for current workloads.
- **Software:** Monitor documentation for updates on the VASP module.
```
---

### 2018110542001643_setting%20up%20for%20a%20longer%20run.md
# Ticket 2018110542001643

 # HPC Support Ticket: Setting Up for a Longer Run

## Keywords
- WRF model
- OpenMP
- MPI
- Wall time extension
- Storage quota
- Job submission
- Performance optimization

## Summary
The user needs to run the WRF model over Greenland for the last five years. The current configuration allows running 50 days of model time in 24 hours of wall time using 18 nodes. The user aims to optimize the run time and requests a wall time extension and increased storage space.

## Issues and Solutions

### OpenMP Not Working
- **Issue**: OpenMP is not effective; the load on nodes is only 10, which is the number of MPI processes started per node.
- **Solution**:
  - Ensure WRF is compiled with OpenMP support (`dm+sm` #67 instead of `dmpar` #66).
  - Increase the number of MPI processes per node (e.g., `-ntasks=200` instead of `-ntasks=20` for 20 nodes).

### Job Submission and Wall Time Extension
- **Issue**: The user needs a wall time extension to run the model continuously for a year.
- **Solution**:
  - Submit jobs with a 24-hour wall time and provide the JobIDs to HPC Admins for extension to 10 days.
  - No need to wait for the Christmas period; jobs can run at any time unless there are scheduled downtimes.

### Storage Quota
- **Issue**: The user needs increased storage space to accommodate the runs and post-processing.
- **Solution**:
  - The HPC Admin increased the user's quota on `$WOODYHOME` to ~7TB.
  - Consider using the new HPC-NFS storage if it becomes available.

### Performance Optimization
- **Issue**: The user aims to reduce the runtime of the WRF model.
- **Solution**:
  - Recompile WRF with OpenMP support.
  - Increase the number of MPI processes per node to utilize all physical cores.
  - Reduce the number of variables to write out to speed up the run.

## Conclusion
The user successfully recompiled WRF with OpenMP support and increased the number of MPI processes, resulting in a significant reduction in runtime. The user will submit longer runs and request wall time extensions as needed.

## Additional Notes
- The user adapted the sbatch script from a previous one provided by the HPC Admin.
- The user plans to further optimize the run time by increasing the number of nodes.

This documentation can be used to address similar issues in the future, focusing on OpenMP configuration, job submission, and storage management.
---

### 2024121042001807_Changing%20RAPL%20settings%20on%20Fritz%20f0401%20node.md
# Ticket 2024121042001807

 ```markdown
# HPC-Support Ticket: Changing RAPL Settings on Fritz Node

## Subject
Changing RAPL settings on Fritz f0401 node

## Keywords
- RAPL
- SLURM
- Fritz cluster
- Node reservation
- Permission error
- Governor powersave
- likwid-perfctr
- sysfeature

## Problem Description
- User is attempting to change RAPL package limit settings on a reserved node (f0401) in the Fritz cluster.
- Error message indicates permission issues when trying to set the RAPL features.
- Node appears unavailable despite no jobs in the queue.

## Error Messages
```
Failed to set feature 'rapl.pkg_limit_1' to '110.0' (Type socket, Resp Unable to set sysfeature: Operation not permitted)
Failed to set feature 'rapl.pkg_limit_2' to '110.0' (Type socket, Resp Unable to set sysfeature: Operation not permitted)
```

## Root Cause
- Permission error when attempting to set RAPL features.
- Possible misconfiguration or lack of necessary permissions on the reserved node.

## Solution
- Ensure the user has the necessary permissions to modify RAPL settings.
- Verify that the node is correctly reserved and configured for the user's experiments.
- Check SLURM configuration and ensure that the node is not inadvertently locked or unavailable.

## Additional Notes
- The user was advised to use `--constraint=hwperf` for likwid-perfctr.
- The node's governor is set to powersave, which might affect performance measurements.

## Next Steps
- HPC Admins to investigate the permission settings on the node.
- Verify node availability and ensure no other jobs are interfering.
- Provide the user with the necessary permissions or an alternative method to change RAPL settings.
```
---

### 2022032942002631_hpc%20slots.md
# Ticket 2022032942002631

 # HPC Support Ticket: Insufficient Slots Error

## Keywords
- Slots
- likwid-mpirun
- Batch system
- srun/mpirun
- Error message
- Queue

## Problem Description
- User receives an error message stating that there are not enough slots available to satisfy the requested 320 slots for a job that previously ran successfully.
- The job does not enter the queue and instead starts immediately, resulting in the error.

## Root Cause
- The error message is likely generated by `likwid-mpirun` rather than the batch system.
- There may have been changes in the calculation of slots.

## Solution
- **Short-term**: Investigate and address any changes in the slot calculation within `likwid-mpirun`.
- **Long-term**: Recommend using the batch system's options and `srun/mpirun` instead of `likwid-mpirun` for general job submissions. Use `likwid-mpirun` only for Likwid measurements or interactive operations.

## General Learning
- Understand the difference between `likwid-mpirun` and the batch system's `srun/mpirun`.
- Recognize that `likwid-mpirun` is more suitable for specific measurements and interactive use, not for general job submissions.
- Ensure proper slot calculation and management to avoid such errors.

## Next Steps
- Verify the slot calculation within `likwid-mpirun`.
- Update job scripts to use `srun/mpirun` for better compatibility with the batch system.
- Monitor job submissions to ensure they enter the queue correctly when slots are unavailable.
---

### 2021081342002289_Elmer_Ice%20Meggie%20installation.md
# Ticket 2021081342002289

 # HPC-Support Ticket: Elmer/Ice Meggie Installation

## Keywords
- Elmer/Ice
- Meggie
- MPI
- Login nodes
- Batch job
- Resource temporarily unavailable

## Problem Description
- User encountered issues running Elmer/Ice tests on Meggie.
- Compilation and installation were successful, but tests failed with MPI communication errors.
- Error message indicated resource unavailability and communication issues.

## Root Cause
- Attempting to run MPI code on login nodes, which is not supported.

## Solution
- Run the test suite in a regular batch job or an interactive batch job instead of on the login nodes.

## General Learnings
- MPI code should not be run on login nodes.
- Always use batch jobs for running MPI tests and applications.
- Resource unavailability errors can indicate improper use of login nodes for MPI tasks.

## Support Team Involvement
- HPC Admins provided the solution by identifying the issue with running MPI code on login nodes.

## Additional Notes
- The user had a successful installation on Emmy and was attempting to replicate it on Meggie.
- Comparison with another user's setup did not resolve the issue.
- The user was advised to run the tests in a batch job to avoid the errors encountered.
---

### 2023110942001322_dmrg-Jobs%20auf%20Fritz%20-%20b165da.md
# Ticket 2023110942001322

 ```markdown
# HPC Support Ticket: Low CPU Utilization in DMRG Jobs

## Keywords
- CPU Utilization
- DMRG Jobs
- ClusterCockpit
- JobID
- HPC Portal

## Issue
- **Root Cause**: Low CPU utilization in DMRG jobs.
- **Symptoms**: JobID=991960 showed low CPU usage.

## Diagnosis
- **HPC Admin**: Noted low CPU utilization in the user's DMRG jobs.
- **User**: Acknowledged the issue and decided to abort the jobs to investigate further.

## Solution
- **User Action**: Aborted the jobs to diagnose the issue.
- **HPC Admin**: Provided guidance to check CPU utilization via ClusterCockpit accessible through the HPC Portal.

## General Learnings
- Always monitor CPU utilization for jobs to ensure efficient resource usage.
- Use ClusterCockpit to diagnose job performance issues.
- Aborting problematic jobs can help in identifying underlying issues.
```
---

### 2025022142002697_Job%20extensions%2029896%20helma.md
# Ticket 2025022142002697

 ```markdown
# HPC Support Ticket: Job Extensions 29896 helma

## Summary
- **User Request**: Extension of job ID 29896 for one week.
- **Reason**: Preparation for the March project on helma+.
- **Issues Encountered**: High network load, node failure.
- **Resolution**: Job optimization and extension granted.

## Keywords
- Job extension
- Network load
- Node failure
- Job optimization
- SLURM

## Detailed Conversation

### Initial Request
- **User**: Requested extension of job ID 29896 for one week.
- **Reason**: Preparation for the March project on helma+.

### Issues Identified
- **HPC Admin**: Noted high network load (16 nodes reading 3 GB/s each, potentially 30 PB traffic in a week).
- **HPC Admin**: Job aborted due to node failure (h11-10).

### Actions Taken
- **User**: Killed the job due to high network load and started a new job on 4 nodes.
- **HPC Admin**: Extended the optimized job (ID 30964) to 7 days.

### Additional Requests
- **User**: Inquired about group limits due to limit errors for another user.
- **HPC Admin**: No waiting jobs found for the specified group.

## Root Cause
- **High Network Load**: The initial job was causing excessive network traffic.
- **Node Failure**: Job aborted due to node failure, possibly related to high network load.

## Solution
- **Job Optimization**: User optimized the job to reduce network load.
- **Job Extension**: HPC Admin extended the optimized job to 7 days.

## Notes
- **Job Extension**: Extensions are granted but not guaranteed to run for the full duration.
- **Group Limits**: No waiting jobs found for the specified group.

## Conclusion
- **User**: Successfully optimized the job to reduce network load.
- **HPC Admin**: Granted the extension for the optimized job.
```
---

### 2023092542004571_Slurm%20settings%20-%20nfcc%20-%20slow%20CPMD%20on%20Fritz%26CCC-Cluster%20due%20to%20wrong%20pinnin.md
# Ticket 2023092542004571

 # HPC Support Ticket: Slow CPMD on Fritz&CCC-Cluster due to Wrong Pinning

## Keywords
- SLURM
- Pinning
- CPMD
- Performance Issues
- SLURM Configuration
- SelectType
- OpenMP

## Problem Description
- User reported slow CPMD calculations on the Fritz cluster.
- Suspected issue with thread pinning on nodes.
- Similar issues observed on another cluster after SLURM update to 23.02.2.

## Root Cause
- Incorrect thread pinning due to SLURM settings.
- Recent SLURM update on Fritz required specific job script modifications for OpenMP.

## Solution
- Use `export SRUN_CPUS_PER_TASK=$SLURM_CPUS_PER_TASK` in the job script if OpenMP is used.
- SLURM version on Fritz is 22.05.9.
- SLURM configuration settings:
  ```plaintext
  SelectType=select/cons_tres
  SelectTypeParameters=CR_Core_Memory,CR_CORE_DEFAULT_DIST_BLOCK
  ```

## Additional Information
- SLURM configuration file location: `/var/run/slurm/conf/slurm.conf`
- User was advised to test the solution thoroughly.

## Ticket Status
- Closed as the problem was resolved.

## Lessons Learned
- Always check SLURM configuration and version after updates.
- Ensure job scripts are updated to match new SLURM requirements, especially for OpenMP.
- Proper thread pinning is crucial for optimal performance in HPC environments.
---

### 2020072242000455_Frage%20zu%20Cluster.md
# Ticket 2020072242000455

 # HPC Support Ticket: Priority and XFactor Calculation

## Keywords
- Priority
- XFactor
- Job Scheduling
- Cluster
- Resource Allocation

## Problem
User inquires about the calculation of Priority and XFactor values for jobs on the cluster.

## Root Cause
User lacks understanding of the factors influencing job priority and XFactor.

## Solution
HPC Admin explains that the priority calculation considers:
- User's resource consumption over the last 10 days
- Group's resource consumption over the last 10 days
- General priority boosts based on financial contributions to HPC procurement

## General Learnings
- Job priority is influenced by recent resource usage and financial contributions.
- Understanding these factors can help users optimize their job scheduling.

## Next Steps
- Users should monitor their resource usage to better predict job priority.
- Further documentation or training on job scheduling factors may be beneficial.
---

### 2021081342001191_issue%3A%20likwid-mpirun%20on%20meggie.md
# Ticket 2021081342001191

 ```markdown
# HPC Support Ticket Summary

## Issue: likwid-mpirun on Meggie Cluster

### User:
- User attempted to run a PureMPI application using `likwid-mpirun` on the Meggie cluster.
- The user encountered issues with running 16 processes on a single node and multiple nodes.

### Root Cause:
- `likwid-mpirun` is not a replacement for `mpiexec/mpirun` in SLURM-based systems.
- The execution environment is already set up by SLURM, and `likwid-mpirun` cannot break out of this environment.
- The user encountered an oversubscription error when trying to run 16 processes on a single node.
- The user also encountered issues with running processes on multiple nodes due to a bug in the processes-per-node calculation in the Lua script.

### Solution:
- The user was advised to use `likwid-mpirun` as a replacement for `srun` in interactive usage.
- The user was advised to load the appropriate module first to ensure that the MPI starters are present.
- The user was advised to use the latest version of `likwid-mpirun` (5.2.0) to fix the oversubscription error.
- The user was advised to apply a patch to fix the processes-per-node calculation bug in the Lua script.
- The user was advised to use the `--mpiopts` option to set additional job options.
- The user was advised to use the `-g MEM` option to get performance counters.
- The user was advised to use the `--cpu-freq` option to set the clock frequency.
- The user was advised to use the `likwid-setFrequencies` command to set the clock frequency in batch scripts.

### Additional Information:
- The user was advised to test the clock frequency to ensure that it is fixed.
- The user was advised to use hardware performance counters to measure the clock frequency.
- The user was advised to use the `likwid-mpirun` command with the `-mpi slurm` option to adjust the CPU frequency.
- The user was advised to use the `likwid-setFrequencies` command to set the clock frequency in interactive usage.

### Conclusion:
- The user was able to run the PureMPI application on multiple nodes by applying the patch to fix the processes-per-node calculation bug in the Lua script.
- The user was able to measure the clock frequency using hardware performance counters.
- The user was advised to use the `likwid-setFrequencies` command to set the clock frequency in batch scripts.
```
---

### 2024091242003406_ClusterCockpit.md
# Ticket 2024091242003406

 # HPC Support Ticket: ClusterCockpit Issues

## Keywords
- ClusterCockpit
- Job Monitoring
- Metrics
- Archiving
- Timeout
- GPU Utilization
- Memory Utilization

## Summary
The user reported several issues with ClusterCockpit, including intermittent failures to display statistics, particularly for older jobs, and a specific large job not being monitored correctly. Additionally, the user inquired about the definitions and thresholds for certain metrics.

## Issues and Solutions

### Issue 1: Intermittent Failures to Display Statistics
- **Root Cause**: The first call to ClusterCockpit often fails, and statistics for older jobs are not always displayed.
- **Solution**: The HPC Admins acknowledged the issue and mentioned that an update is in progress to improve the loading speed and stability of ClusterCockpit.

### Issue 2: Large Job Not Monitored Correctly
- **Root Cause**: The large job (ID 2038301) was not displayed due to archiving failure and missing data files.
- **Solution**: The HPC Admins identified that the job's extended runtime and large resource usage caused the archiving process to fail. They have addressed the timeout issue internally and will deploy an update after completing internal tests.

### Issue 3: Metric Definitions and Thresholds
- **Root Cause**: The user was unclear about the definitions and thresholds for `acc_utilization`, `nv_mem_util`, and `acc_mem_used`.
- **Solution**: The HPC Admins provided definitions and thresholds for the metrics:
  - **acc_utilization**: Percent of time during which one or more kernels were executing on the GPU.
  - **nv_mem_util**: Percent of time during which global (device) memory was being read or written.
  - **acc_mem_used**: Allocated device memory (in bytes).
  - **Thresholds**:
    - `acc_utilization`: Peak 100%, Normal 80%, Caution 50%, Alert 20%
    - `nv_mem_util`: Peak 100%, Normal 80%, Caution 20%, Alert 10%
    - `acc_mem_used` (Sum of 8 GPU): Peak 640GB, Normal 320GB, Caution 160GB, Alert 80GB
    - `acc_mem_used` (1 GPU): Peak 80GB, Normal 40GB, Caution 20GB, Alert 10GB

## General Learnings
- ClusterCockpit may experience issues with displaying statistics, particularly for older jobs.
- Large jobs with extended runtimes and significant resource usage can cause archiving failures.
- Metrics such as `acc_utilization`, `nv_mem_util`, and `acc_mem_used` have specific definitions and thresholds that users should be aware of.
- The HPC Admins are actively working on updates to improve ClusterCockpit's performance and stability.

## Next Steps
- Monitor the deployment of the ClusterCockpit update.
- Continue to address any archiving issues for large jobs.
- Provide clear documentation on metric definitions and thresholds for users.
---

### 2023020942003231_Multi-node%20training%20-%20b143dc11.md
# Ticket 2023020942003231

 # HPC Support Ticket: Multi-node Training

## Keywords
- Multi-node job
- QoS specification
- Walltime extension
- JobID
- Invalid qos specification

## Problem
- User attempted to start a multi-node job but received an "Invalid qos specification" error.
- User requested permission to use multiple nodes and inquired about extending walltime for jobs.

## Root Cause
- Multi-node jobs require explicit permission and are available on demand.
- User's account was not initially configured for multi-node jobs.

## Solution
- HPC Admin enabled the user's account for multi-node jobs with the `--qos=a100multi` specification.
- User was instructed to send JobIDs for jobs requiring extended walltime, which HPC Admin agreed to manually adjust if operationally feasible.

## General Learnings
- Multi-node jobs are not enabled by default and require a specific QoS specification.
- Walltime for jobs can be extended upon request, subject to operational constraints.
- Users should provide JobIDs for jobs needing extended walltime.

## Actions Taken
- HPC Admin enabled multi-node job capability for the user's account.
- HPC Admin offered to manually extend walltime for specific jobs upon receiving JobIDs.

## Follow-up
- User thanked HPC Admin for the quick and excellent support.
- User requested walltime extension for a specific job (JobID: 680823) and was instructed to send JobIDs for future extensions.
---

### 2022041442001346_64-node-jobs%20on%20Fritz%20%5Biww8000h%5D.md
# Ticket 2022041442001346

 # HPC Support Ticket: 64-node-jobs on Fritz

## Keywords
- 64-node jobs
- Slurm script
- `#SBATCH --switches=1`
- `ReqNodeNotAvail`
- UnavailableNodes
- Top500 Linpack run
- Multinode partition

## Summary
The user was granted access to use up to 64 nodes per job on Fritz, with a total allowance of 128 nodes. However, the user encountered issues with job submission where the job did not start and reported `ReqNodeNotAvail` with specific unavailable nodes.

## Root Cause
- The issue was due to partial reservations of nodes in the multinode partition for the preparation of a Top500 Linpack run.

## Solution
- The user was advised to be patient and check the Message of the Day (MOTD) on Fritz, which indicated that nodes might be reserved without further notice for the Top500 Linpack run.

## General Learnings
- Always check the MOTD for any ongoing maintenance or reservations that might affect job submissions.
- Be patient during periods of high system usage or maintenance.
- Ensure that the Slurm script includes `#SBATCH --switches=1` to allocate nodes on a single island, although Slurm might start the job regardless of the requested switches.

## Additional Notes
- The user did not receive any specific error messages related to access permissions but encountered node unavailability issues.
- The HPC Admins provided timely support and advised the user about the ongoing preparations for the Top500 Linpack run.
---

### 2024081542000978_Two%20large%20jobs%20with%20too%20low%20cpu_load%20-%20b165da17.md
# Ticket 2024081542000978

 ```markdown
# HPC Support Ticket: Two Large Jobs with Low CPU Load

## Keywords
- Low CPU load
- Large jobs
- Input issues
- Job IDs
- Nodes
- User non-responsive

## Summary
- **Issue**: Two large jobs (IDs: 1532998 and 1532999) running on 56 nodes each had very low average CPU load, with many nodes showing virtually zero load.
- **Root Cause**: Suspected issues with the input data or configuration.
- **Action Taken**: HPC Admin notified the user about the low CPU load and potential input issues.
- **Outcome**: The ticket was closed due to the user not responding.

## Lessons Learned
- Regularly monitor large jobs for CPU load to identify potential issues early.
- Ensure users are responsive to notifications about job performance issues.
- Consider setting up automated alerts for jobs with abnormally low CPU usage.
```
---

### 2018111942001117_Abschaltung%20LiMa%20_%20Migration%20Jobs%20gwgi17.md
# Ticket 2018111942001117

 ```markdown
# HPC Support Ticket Conversation Summary

## Problem Description
The user encountered performance issues with Elmer/Ice jobs on the LiMa cluster. The jobs were not efficiently utilizing the system's resources, leading to poor performance and long runtimes.

## Key Learnings
1. **Compiler and Library Optimizations**: Different compiler options and library configurations significantly impact the performance of Elmer/Ice jobs. For example, using the Intel Compiler with MKL libraries showed better performance compared to GNU Compiler with default libraries.
2. **Mesh Size and Partitioning**: The size of the mesh and the number of partitions affect the performance. Larger meshes and optimal partitioning can improve performance.
3. **Convergence Behavior**: The convergence behavior of the solver is dependent on the number of MPI processes. This can lead to varying iteration counts and runtimes.
4. **Hardware Utilization**: The jobs were not efficiently utilizing the hardware resources. Monitoring tools like LIKWID showed that the CPU was often idle, and the cache bandwidth was not fully utilized.
5. **Code Optimization**: The user's code had inefficiencies, such as excessive branching and suboptimal use of libraries. Profiling the code can help identify hotspots and areas for optimization.

## Solutions
1. **Compiler and Library Configurations**: Test different compiler options and library configurations to find the optimal settings for the jobs.
2. **Mesh Size and Partitioning**: Adjust the mesh size and partitioning to ensure optimal load distribution across the available resources.
3. **Convergence Analysis**: Analyze the convergence behavior of the solver to understand the impact of different MPI process counts.
4. **Hardware Utilization**: Use monitoring tools to ensure that the jobs are efficiently utilizing the hardware resources. Optimize the code to reduce idle CPU time and improve cache utilization.
5. **Code Profiling**: Profile the code to identify hotspots and areas for optimization. Use this information to guide code improvements.

## Conclusion
The performance issues with Elmer/Ice jobs on the LiMa cluster were addressed through a combination of compiler and library optimizations, mesh size and partitioning adjustments, convergence analysis, hardware utilization improvements, and code profiling. These steps helped identify and resolve inefficiencies, leading to better performance and reduced runtimes.
```
---

### 2023100242003871_AW%3A%20New%20invitation%20for%20%22Studentische%20Abschlu%C3%83%C2%9Farbeiten%20Tier3%20Grundversor.md
# Ticket 2023100242003871

 # HPC-Support Ticket Conversation Summary

## Keywords
- Multi-node jobs
- HDR200 Infiniband
- GPUDirect RDMA
- OpenMPI modules
- Performance issues
- Bandwidth testing

## What Can Be Learned
- **Multi-Node Job Requests**: Users can request multiple nodes for jobs using specific QoS settings.
- **Infiniband Connectivity**: Nodes should be connected via Infiniband, but performance issues may indicate connectivity problems.
- **OpenMPI Modules**: Different OpenMPI modules have varying performance characteristics, especially regarding GPUDirect RDMA support.
- **Performance Testing**: Users can perform bandwidth tests to diagnose performance issues.
- **Module Issues**: Specific modules may have bugs or missing dependencies that need to be addressed.

## Ticket Conversation Summary

### Initial Request
- **User**: Requested access to multiple nodes for testing communication between nodes in the GPGPU cluster Alex.
- **Specific Interest**: Communication over HDR200 Infiniband.

### HPC Admin Responses
- **QoS Setting**: Informed the user to use `--qos=a100multi` to request multiple nodes.
- **Module Suggestions**: Suggested using specific OpenMPI modules for better performance.
- **Performance Issues**: Identified performance issues related to OpenMPI not being CUDA aware or lacking GPUDirect RDMA support.

### Detailed Investigation
- **User Tests**: User provided scripts and data from tests showing performance issues.
- **Admin Analysis**: Admins analyzed the data and identified that OpenMPI was not utilizing GPUDirect RDMA.
- **Module Fixes**: Admins suggested using older modules that had better performance and provided updates to newer modules.

### Solutions
- **Module Update**: Admins fixed an issue with the `libmpi.so.40` shared object file not being found.
- **Performance Improvement**: User confirmed that the suggested module (`openmpi/4.1.2-nvhpc21.11-cuda`) significantly improved performance.

### Closure
- **Ticket Closure**: The ticket was closed due to inactivity after the user confirmed that the issue was resolved.

## Root Cause and Solution
- **Root Cause**: The root cause of the performance issue was the lack of GPUDirect RDMA support in the OpenMPI module being used.
- **Solution**: Using an older OpenMPI module (`openmpi/4.1.2-nvhpc21.11-cuda`) that had better GPUDirect RDMA support resolved the performance issue.

## Documentation for Future Reference
- **Multi-Node Job Requests**: Users should use `--qos=a100multi` to request multiple nodes.
- **OpenMPI Modules**: Ensure that the OpenMPI module being used supports GPUDirect RDMA for optimal performance.
- **Performance Testing**: Users can perform bandwidth tests to diagnose performance issues and compare results with expected values.
- **Module Issues**: If specific modules have bugs or missing dependencies, admins should address these issues promptly.

This summary provides a concise overview of the ticket conversation, the root cause of the problem, and the solution implemented. It can be used as a reference for support employees to resolve similar issues in the future.
---

### 2020050842000806_Jobs%20auf%20Woody%20brauchen%20%C3%83%C2%BCber%208GB%20-%20mpwm009h.md
# Ticket 2020050842000806

 ```markdown
# HPC Support Ticket: Jobs auf Woody brauchen über 8GB

## Keywords
- Memory usage
- Swapping
- Resource allocation
- Job scheduling
- System monitoring
- Woody cluster
- TinyFAT cluster

## Problem Description
- User's jobs on Woody regularly require more than 8 GB of RAM.
- Jobs start swapping heavily when executed on nodes with only 8 GB of RAM.
- System monitoring shows significant swap usage and high page-in/page-out rates.

## Root Cause
- Insufficient memory allocation for the jobs, leading to excessive swapping.

## Solution
- Update resource request to `nodes=1:ppn=4:any32g` to ensure jobs run on nodes with 32 GB of RAM.
- For jobs requiring more than 32 GB, consider switching to the TinyFAT cluster.

## General Learnings
- Monitor job memory usage to prevent swapping.
- Adjust resource requests to match job requirements.
- Consider alternative clusters for jobs with higher memory needs.
```
---

### 2021022342003038_Frage%20zur%20devel%20queue%20auf%20Emmy.md
# Ticket 2021022342003038

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Keywords
- MPI Tests
- Frontend
- Interactive Jobs
- Job Scheduling
- Fairshare
- Devel Queue
- Work Queue
- Job Monitoring
- Arbeitsspeicher
- X-Factor
- TinyFat

## General Learnings
- **MPI Tests on Frontend**: Not allowed. Use interactive jobs for testing.
- **Job Scheduling**: Fairshare based on actual resource usage. Aborted jobs only count the actual runtime.
- **Devel Queue**: Limited to 8 nodes and 1 hour. Jobs exceeding these limits are routed to the work queue.
- **Job Monitoring**: Use job monitoring tools to check memory usage for batch jobs. Use `pbsdsh` for interactive jobs.
- **X-Factor**: Influenced by requested walltime. Shorter jobs have an advantage.
- **TinyFat**: Only single-node jobs allowed. Not suitable for large simulations requiring multiple nodes.

## Root Cause of the Problem
- User encountered issues running MPI tests on the frontend due to the "ofa fabric is not available" error.
- Needed to understand the impact of aborted jobs on job scheduling and fairshare.
- Required clarification on the limitations of the devel queue and how to monitor memory usage.

## Solution
- Use interactive jobs for MPI tests instead of running them on the frontend.
- Aborted jobs only affect fairshare based on actual runtime, not requested walltime.
- The devel queue is limited to 8 nodes and 1 hour. Larger jobs are routed to the work queue.
- Use job monitoring tools to check memory usage for batch jobs and `pbsdsh` for interactive jobs.
- The X-Factor is influenced by requested walltime, with shorter jobs having an advantage.
- TinyFat is not suitable for multi-node jobs, so the user should continue using Emmy for large simulations.
```
---

### 2022020642000553_out%20of%20memory%20error%20alex.md
# Ticket 2022020642000553

 # HPC-Support Ticket: Out of Memory Error on Alex

## Subject
Out of memory error while running a large application on Alex.

## User Description
- **Issue**: Out of memory error when running a large application on Alex.
- **Error Message**:
  ```
  slurmstepd: error: Detected 1 oom-kill event(s) in StepId=24515.0. Some of your processes may have been killed by the cgroup out-of-memory handler.
  srun: error: a0605: task 0: Out Of Memory
  srun: launch/slurm: _step_signal: Terminating StepId=24515.0
  slurmstepd: error: *** STEP 24515.0 ON a0605 CANCELLED AT 2022-02-06T16:07:11 ***
  slurmstepd: error: Detected 1 oom-kill event(s) in StepId=24515.batch. Some of your processes may have been killed by the cgroup out-of-memory handler.
  ```
- **Observation**: The error occurs after a few iterations of the same task, especially when copying to/from GPU.

## HPC Admin Response
- **Diagnosis**: The processes on the host are trying to allocate more memory than available (~920 GB for A100 nodes).
- **Details**:
  ```
  [Sun Feb  6 11:44:20 2022] Tasks state (memory values in pages):
  [Sun Feb  6 11:44:20 2022] [  pid  ]   uid   tgid  total_vm       rss pgtables_bytes swapents oom_score_adj name
  [Sun Feb  6 11:44:20 2022] [  94337]      0 94337      1827       177    61440        0             0 sleep
  [Sun Feb  6 11:44:20 2022] [  94359] 411818 94359      4247       648    69632        0             0 slurm_script
  [Sun Feb  6 11:44:20 2022] [  96210] 411818 96210     91067      3745   249856        0             0 srun
  [Sun Feb  6 11:44:20 2022] [  96211] 411818 96211     12807       222   118784        0             0 srun
  [Sun Feb  6 11:44:20 2022] [  96227] 411818 96227 179753106 36124965 291815424        0             0 call_INLA
  [Sun Feb  6 11:44:20 2022] [  96228] 411818 96228 179741181 45655468 368205824        0             0 call_INLA
  [Sun Feb  6 11:44:20 2022] [  96229] 411818 96229 179739507 48363138 389894144        0             0 call_INLA
  [Sun Feb  6 11:44:20 2022] [  96230] 411818 96230 179744592 52825492 425652224        0             0 call_INLA
  [Sun Feb  6 11:44:20 2022] [  96231] 411818 96231 179729768 41770638 337076224        0             0 call_INLA
  [Sun Feb  6 11:44:20 2022] [  96232] 411818 96232    991833   366191  3543040        0             0 call_INLA
  [Sun Feb  6 11:44:20 2022] [  96233] 411818 96233    987637   366306  3518464        0             0 call_INLA
  [Sun Feb  6 11:44:20 2022] [  96234] 411818 96234    988686   365739  3534848        0             0 call_INLA
  ```
- **Root Cause**: The out-of-memory issue is not from the GPUs but from the host. The CPU part is trying to allocate too much memory on the host.

## User Follow-Up
- **Additional Information**: The user is performing tridiagonal block matrix factorizations on the GPUs. The issue persists even when using a single GPU and performing a single matrix factorization.
- **Observation**: The memory usage on a single V100 GPU is constant at 8 GB, but the issue occurs on Alex.

## HPC Admin Final Response
- **Clarification**: The out-of-memory issue is from the host, not the GPUs. The CPU part is trying to allocate too much memory.

## Solution
- **Recommendation**: Investigate the CPU memory allocation and optimize the application to reduce memory usage on the host.

## Keywords
- Out of memory
- GPU
- Host memory
- Slurm
- OOM-kill
- Matrix factorization

## General Learning
- Out-of-memory errors can occur due to excessive memory allocation by the CPU part of the application.
- Monitoring memory usage on both the host and GPUs is crucial for diagnosing such issues.
- Optimizing the application to reduce memory usage on the host can help resolve out-of-memory errors.
---

### 2022120742002674_einige%20Jobs%20machen%20nichts%20-%20k103bf.md
# Ticket 2022120742002674

 ```markdown
# HPC Support Ticket Analysis

## Subject: einige Jobs machen nichts - k103bf

### Keywords:
- Memory usage
- Job failure
- Testing
- Input data

### Summary:
- **Issue**: Some jobs are not running as expected.
- **Root Cause**:
  - Memory usage increases abruptly for 32x96 systems, potentially causing issues for 44x144 systems.
  - Incorrect input data for smaller jobs (269206, 269207).
- **Solution**:
  - Memory usage issue is not relevant for the current project phase.
  - Correct input data for smaller jobs to prevent future issues.

### Lessons Learned:
- Monitor memory usage for large system jobs.
- Ensure all input data is correct before submitting jobs.
- Testing code for specific system sizes may not be relevant for the entire project.

### Actions Taken:
- HPC Admin analyzed job files and identified memory usage patterns.
- User confirmed that the memory issue is not relevant for the current project phase.
- User acknowledged the input data issue and assured it would not recur.

### Closure:
- Ticket closed as the issues were identified and resolved.
```
---

### 2022090142003243_Tier3-Access-Fritz%20%22Mattis%20Go%C3%83%C2%9Fler%22%20_%20nfcc010h.md
# Ticket 2022090142003243

 # HPC Support Ticket Analysis

## Subject
Tier3-Access-Fritz "Mattis Goßler" / nfcc010h

## Keywords
- Rechenzeit
- FAU-Grundversorgung
- NHR-Antrag
- Core-Stunden
- Knotenstunden
- CPMD
- Molecular dynamics simulation

## Problem
- User requested 100,000 node hours, which translates to 7.2 million core hours.
- This exceeds the computational resources available under FAU-Grundversorgung.

## Root Cause
- Misunderstanding of the required computational resources.
- User intended to request 100,000 core hours instead of node hours.

## Solution
- User clarified the actual requirement of 100,000 core hours.
- HPC Admin approved the request within the FAU-Grundversorgung framework.

## What Can Be Learned
- Importance of accurate resource estimation in HPC requests.
- Difference between node hours and core hours.
- Procedure for requesting additional computational resources through NHR-Antrag if needed.

## Actions Taken
- HPC Admin initially denied the request due to excessive resource demand.
- User corrected the resource requirement.
- HPC Admin approved the corrected request and activated the user's account.

## References
- [NHR Application Rules](https://hpc.fau.de/systems-services/documentation-instructions/nhr-application-rules/)

## Notes
- Ensure users are aware of the resource limits under FAU-Grundversorgung.
- Provide clear guidelines on how to request additional resources if needed.
---

### 2023102542002043_array%20job%20running%20on%20one%20core%20-%20k103bf17.md
# Ticket 2023102542002043

 # HPC Support Ticket: Array Job Running on One Core

## Keywords
- Array job
- Core utilization
- Memory usage
- Monitoring system
- ClusterCockpit
- Job optimization

## Problem Description
- User submitted an array job of size 101.
- Each job runs on one core of Fritz nodes, leaving 71 cores idle.
- Jobs do not use a significant amount of memory.

## Root Cause
- Inefficient resource utilization due to each job running on a single core.

## Solution
- Optimize job submission to utilize more cores per node.
- Use the monitoring system to track job performance and resource usage.

## Steps for User
1. Log into the portal: [HPC Portal](https://portal.hpc.fau.de/)
2. Click on "Go to ClusterCockpit".
3. Use the monitoring system: [Monitoring System](https://monitoring.nhr.fau.de/monitoring/user/k103bf17?state=running)

## Additional Information
- Job name: `g48dt1p11_p`
- Contact HPC Admins for further assistance: [support-hpc@fau.de](mailto:support-hpc@fau.de)

## General Learning
- Ensure efficient use of HPC resources by optimizing job submissions.
- Utilize monitoring tools to track and improve job performance.
- Communicate with HPC Admins for guidance on resource management.
---

### 2024082642003374_Request%20for%20information%20about%20the%20availability%20of%20the%20nodes%20in%20Meggie%20cluster.md
# Ticket 2024082642003374

 # HPC Support Ticket: Meggie Cluster Node Availability

## Keywords
- Meggie cluster
- Node availability
- Maintenance
- Hardware issue
- Management node reboot

## Summary
A research assistant encountered issues with node availability on the Meggie cluster due to scheduled maintenance. The user requested a timeline for node availability to plan their work accordingly.

## Root Cause
- Broken hardware on the management node required a reboot.
- Compute nodes were placed into maintenance to minimize the impact.

## Solution
- The HPC Admin informed the user that the Meggie cluster would be available again shortly after the reboot of the management node.

## Lessons Learned
- Regular communication about maintenance schedules can help users plan their work effectively.
- Hardware issues can necessitate the temporary unavailability of compute nodes.
- Rebooting the management node is a common solution to address hardware issues.

## Action Items
- Ensure timely updates on maintenance schedules to users.
- Provide clear communication regarding the expected downtime and availability of nodes.

## References
- HPC Support Email: support-hpc@fau.de
- HPC Website: [hpc.fau.de](https://hpc.fau.de/)
---

### 2019060742001255_Bad%20performance%20of%202bands_bethe%20jobs%20on%20Emmy%20_%20mptf009h.md
# Ticket 2019060742001255

 ### HPC-Support Ticket Conversation Summary

**Subject:** Poor Performance of 2bands_bethe Jobs on Emmy / mptf009h

**Root Cause:**
- Inefficient use of OpenMP threads.
- Slow complex multiplication function `__muldc32`.

**Solution:**
- Compile the code with the `-fast-math` flag to speed up complex multiplications.
- Ensure proper specification of queues to avoid old nodes.
- Increase the number of OpenMP threads if the workload allows.
- Consider using MPI parallelization if possible.

**Keywords:**
- OpenMP
- MPI
- Performance Optimization
- Complex Multiplication
- HPC Cluster
- Emmy
- TinyFAT

**What Can Be Learned:**
- Proper configuration of OpenMP threads is crucial for performance.
- The `__muldc32` function can significantly slow down performance.
- Specifying the correct queue and node type can improve job efficiency.
- Combining MPI and OpenMP can help distribute workload effectively.

**Conversation Highlights:**

1. **Initial Issue:**
   - User's jobs showed poor performance (20 DP-GFlop/s per node).
   - Low load despite setting `OMP_NUM_THREADS`.

2. **Admin Suggestions:**
   - Check job performance and load issues.
   - Suggested meeting to discuss code characterization and performance improvement.

3. **User Actions:**
   - User compiled the code with `-fast-math` flag, improving performance by a factor of 3.
   - User specified the correct queue to avoid old nodes.

4. **Further Optimization:**
   - Admin suggested using more cores if possible.
   - User mentioned that MPI parallelization is not feasible for the most demanding part of the code.

5. **Final Recommendations:**
   - Admin suggested trying MPI processes on a single node with OpenMP threads.
   - User confirmed that OpenMP parallelism is sufficient for their workload.

**Conclusion:**
The user successfully improved the performance of their jobs by compiling with the `-fast-math` flag and ensuring proper queue specification. Further optimization can be achieved by effectively utilizing OpenMP threads and considering MPI parallelization where applicable.
---

### 2023051042001359_FASTTMP.md
# Ticket 2023051042001359

 # HPC-Support Ticket: FASTTMP

## Subject
- **User Query:** Alternatives for running long-term WRF simulations after the shutdown of $FASTTMP on Meggie.

## Keywords
- FASTTMP
- Meggie
- WRF simulations
- $WORK
- Fritz-Cluster
- Tier3 user
- Tier2 user
- Data migration
- HPC account

## Problem
- **Root Cause:** Shutdown of $FASTTMP on Meggie.
- **Impact:** User needs an alternative for running long-term WRF simulations.

## Solution
- **Recommendations:**
  - Consider using $WORK, but be cautious of IO-intensive code impacting the shared server.
  - Move to Fritz-Cluster for better hardware and resources.
- **Steps Taken:**
  - User filled out the form for Fritz-Cluster access.
  - HPC Admin granted Tier3 access to the user.
  - Discussion on the advantages of Tier2 access for shorter queue times and high memory nodes.

## General Learnings
- **Cluster Status:** Meggie is old and will be turned off soon due to dying hardware.
- **User Types:**
  - Tier3 users have limited resource access (~20% of Fritz).
  - Tier2 users have access to more resources and shorter queue times.
- **Data Migration:** Moving to Fritz-Cluster does not impact access to other clusters, but data migration may be needed if invited to a Tier2 project.
- **Contract Considerations:** External users with contracts specifying resources need to discuss how moving to a new cluster will affect their allocations.

## References
- [HPC-Cafe Slides on Cluster Status](https://hpc.fau.de/files/2023/04/2023-04-25-HPC-Cafe-Beschaffung.pdf)
- [HPC Storage Documentation](https://hpc.fau.de/systems-services/documentation-instructions/hpc-storage/)
---

### 2022111642000741_Tier3-Access-Fritz%20%22Stefan%20Becker%22%20_%20iwpa26.md
# Ticket 2022111642000741

 # HPC Support Ticket Analysis

## Keywords
- Certificate expiration
- Tier3 access
- NHR projects
- Rechenzeit (compute time)
- Single-node throughput
- Multi-node workload
- Software requirements (StarCCM, OpenFOAM, Python, Matlab)
- Flow acoustics simulations

## Summary
- **Root Cause**: Certificate expiration led to initial access issues.
- **User Request**: Access to Tier3 resources for flow acoustics simulations, requiring specific software and compute resources.
- **HPC Admin Response**: Suggested using NHR projects for compute time due to limited Tier3 resources.
- **Solution**: Account was activated on Fritz, but strong recommendation to use NHR projects for compute time.

## Detailed Analysis
- **Initial Issue**: Certificate expiration caused access problems.
- **User Needs**:
  - Single-node throughput with special justification (72 cores, 250 GB).
  - Multi-node workload with HDR100 Infiniband (1:4 blocking; 72 cores, 250 GB per node).
  - Required software: StarCCM, OpenFOAM, Python, Matlab.
  - Application: Flow acoustics simulations.
  - Expected results: Simulation results matching measurement data.
- **HPC Admin Actions**:
  - Suggested using NHR projects for compute time.
  - Activated the user's account on Fritz but advised against using Tier3 resources due to limited availability.

## Lessons Learned
- **Certificate Management**: Ensure certificates are up-to-date to avoid access issues.
- **Resource Allocation**: Encourage users to utilize NHR projects for compute time to optimize resource usage.
- **Communication**: Maintain clear communication with users regarding resource availability and recommendations.

## Future Reference
- **Certificate Renewal**: Implement a system to track and renew certificates before expiration.
- **Resource Guidance**: Provide users with clear guidelines on when to use Tier3 resources versus NHR projects.
- **Documentation**: Update documentation to include steps for requesting and managing compute time on different projects.
---

### 2022102142002132_libfabric%3Atimeout%20error.md
# Ticket 2022102142002132

 ```markdown
# HPC Support Ticket: libfabric Timeout Error

## Keywords
- Timeout Error
- libfabric
- PSM2
- Omnipath-Netzwerk
- Meggie
- FI_PSM2_CONN_TIMEOUT

## Problem Description
User reports intermittent "Timeout Error" when starting jobs on Meggie, causing computations to fail. The error message suggests increasing `FI_PSM2_CONN_TIMEOUT`.

## Root Cause
- Defective links in the Omnipath-Netzwerk due to a recent power outage.
- These links occasionally disrupt the network, causing timeouts.

## Solution
- HPC Admins are working to identify and fix all defective links.
- Users are advised to retry their jobs if they encounter this issue.

## Additional Information
- The issue is expected to persist until all defective links are identified and fixed.
- Increasing `FI_PSM2_CONN_TIMEOUT` may help mitigate the issue temporarily.

## Next Steps
- Continue monitoring the network for defective links.
- Inform users to retry their jobs if they encounter timeouts.
- Consider increasing `FI_PSM2_CONN_TIMEOUT` as a temporary workaround.
```
---

### 2022062342003092_StarCCM%2B%20Jobs%20auf%20emmy%20%7C%20iwst074h.md
# Ticket 2022062342003092

 # HPC Support Ticket: StarCCM+ Jobs Resource Imbalance

## Keywords
- StarCCM+
- Resource imbalance
- Co-simulation
- Process allocation
- `-np` option
- `-machinefile` option
- SMT threads
- Job optimization

## Problem Description
- User's StarCCM+ simulations on the HPC cluster showed uneven resource usage.
- Some nodes had no computation, leading to resource waste.
- The automatic process allocation by `starlaunch` seemed ineffective.
- Options `-np` and `-machinefile` were ignored, resulting in more processes than specified.

## Root Cause
- The simulation alternated between compute-intensive and less intensive phases, causing load imbalance.
- The user was unable to separate these processes effectively.

## Solution Attempts
- User tried to resolve the issue but faced difficulties in separating the processes.
- User requested permission to run smaller jobs to test potential solutions.

## Admin Response
- Admin acknowledged the issue and allowed the user to run simulations despite the imbalance.
- Admin suggested optimizing process allocation and limiting to 20 processes per node to potentially reduce simulation time.

## Outcome
- User was permitted to run jobs with the existing imbalance, recognizing that it was phase-dependent.
- No final resolution was documented, but the user was encouraged to continue testing and optimizing.

## Lessons Learned
- Uneven resource usage in simulations can be acceptable if it occurs in phases.
- Proper process allocation and limiting processes per node can help optimize simulation performance.
- Users should be encouraged to test and optimize their jobs even if a perfect solution is not immediately available.

## References
- [HPC Status Job Info](https://www.hpc.rrze.fau.de/HPC-Status/job-info.php?USER=iwst074h&JOBID=1655340&ACCESSKEY=dfd15a43&SYSTEM=EMMY)
- [FAU HPC Support](https://hpc.fau.de/)
---

### 2018121042002131_number%20of%20threads%20for%20jobs%20on%20Emmy%20_%20iww8015h.md
# Ticket 2018121042002131

 # HPC Support Ticket: Number of Threads for Jobs on Emmy

## Keywords
- Emmy
- MPI processes
- OpenMP threads
- Physical cores
- SMT threads
- Job optimization

## Problem
- **Root Cause:** User submitted jobs with 4 MPI processes, each using 40 threads, totaling 160 threads on a single node.
- **Issue:** Emmy nodes have only 20 physical cores or 40 SMT threads, making 160 threads suboptimal.

## Solution
- **Action Taken:** HPC Admin advised the user to adjust the number of threads.
- **User Response:** User planned to resubmit the task with 4 MPI processes, each using 10 OpenMP threads.

## General Learning
- Ensure that the total number of threads in a job does not exceed the available SMT threads on the node.
- Adjust the number of MPI processes and OpenMP threads to optimize resource usage.

## Next Steps
- Monitor job performance after adjusting the number of threads.
- Provide further guidance if performance issues persist.
---

### 2022012442002251_Early-Fritz%20%22Nico%20Staffen%22%20_%20bcpc002h.md
# Ticket 2022012442002251

 ```markdown
# HPC Support Ticket Analysis

## Subject: Early-Fritz "Nico Staffen" / bcpc002h

### Keywords
- Early-adopter
- Fritz cluster
- Single-node throughput
- Multi-node workload
- Infiniband HCAs
- GROMACS 2021.4
- Molecular Dynamic Simulations
- Acceleration of simulation time
- SSH access
- Partition "singlenode"
- Documentation
- MOTD

### Summary
- **User Request**: Access to Fritz cluster for single-node and multi-node workloads using GROMACS 2021.4 for molecular dynamic simulations.
- **Initial Setup**: User was granted access to the "singlenode" partition due to limited Infiniband cards.
- **Access Details**: SSH access provided for both internal and external networks.
- **Documentation**: Initial documentation is in progress, with additional information available in the MOTD upon login.
- **Multi-node Access**: User was later granted access to multi-node jobs.

### Root Cause of the Problem
- Limited availability of Infiniband cards due to supply issues.

### Solution
- User was initially restricted to the "singlenode" partition.
- Later, the user was granted access to multi-node jobs once more Infiniband cards became available.

### General Learnings
- **Access Management**: Users can be granted access to specific partitions based on resource availability.
- **Documentation**: Importance of providing initial documentation and updating it as the system evolves.
- **Communication**: Clear communication about access details and system updates is crucial for user satisfaction.
- **Resource Allocation**: Managing resource allocation based on hardware availability and user needs.

### Actions Taken
- **Initial Access**: User was granted access to the "singlenode" partition.
- **SSH Access**: Provided SSH access details for both internal and external networks.
- **Documentation**: Informed the user about the ongoing documentation process and the availability of MOTD information.
- **Multi-node Access**: Later granted the user access to multi-node jobs.
```
---

### 42321627_Turbomole%206.6%20processor%20issue.md
# Ticket 42321627

 # HPC Support Ticket: Turbomole 6.6 Processor Issue

## Keywords
- Turbomole 6.6
- Processor limit
- Optimization procedure
- Convergence issue
- Performance monitoring
- Emmy cluster

## Problem Description
- User experienced convergence issues with Turbomole 6.6 optimization procedures on the Lima cluster when using 192 processors, despite successful convergence with 28 processors.
- The same procedure converged easily on another cluster.

## Root Cause
- Turbomole is known to have issues running efficiently on a large number of cores/nodes.
- The convergence failure message originated from Turbomole itself, indicating a potential input-related issue.

## Findings
- Performance monitoring showed poor performance for the job using 192 processors compared to the job using 28 processors.
- No cluster-related problems were identified.

## Solution
- Consult with a Turbomole expert to address potential input-related issues.
- Consider using fewer processors for better performance and convergence.

## Additional Information
- There are currently no plans to provide or support Turbomole on the Emmy cluster.

## Next Steps for Support
- Advise users to check Turbomole documentation or consult with Turbomole experts for input-related issues.
- Monitor and document similar performance issues with Turbomole for future reference.

## Related Files
- `/home/rrze/bcp1/bcp136/DPV1_28`
- `/home/rrze/bcp1/bcp136/DPV1_192`
- `/home/rrze/bcp1/bcp136/DPV1_192/DPV1_192.o1549419`

## Contact Information
- HPC Services: support-hpc@fau.de
- [HPC RRZE Website](http://www.hpc.rrze.fau.de/)
---

### 2024121042003609_High%20Priority%20of%20HPC%20Resource%20-%20Master%20Thesis%20-%20JialunWu.md
# Ticket 2024121042003609

 # HPC Support Ticket: High Priority of HPC Resource - Master Thesis

## Keywords
- GPU Resources
- Priority
- H100
- V100
- RTX2080
- RTX3080
- Wartezeit
- Berechtigungen

## Problem
- User is experiencing long wait times for GPU resources (H100 or V100) due to "Reason=Priority".
- User is unable to execute their experiments due to these wait times.

## Root Cause
- High demand for powerful GPU resources leading to long wait times.
- User's jobs are being deprioritized to allow other users access to resources.

## Solution
- **HPC Admin** suggests that the user cannot be given higher priority as the system automatically adjusts priority based on recent activity.
- To reduce wait time, the user is advised to use less powerful GPUs (RTX2080 and RTX3080) for some of their computations.

## General Learning
- Priorities for jobs are dynamically set based on user activity and cannot be manually overridden.
- Using less powerful resources can help reduce wait times for high-demand resources.
- Effective resource management is crucial for fair usage and access to HPC resources.
---

### 2020121342000131_Yambo%20Jobs%20auf%20Emmy%20-%20mpp3004h.md
# Ticket 2020121342000131

 # HPC Support Ticket: Yambo Jobs auf Emmy - mpp3004h

## Keywords
- Yambo Jobs
- Out-of-memory
- Parallelisierung
- Hyperthreading
- Speicherauslastung
- Job-Submission-Skript
- Manuelle Reaktivierung
- Zoom-Meeting

## Problem
- User caused 20% of Emmy nodes to crash due to out-of-memory errors.
- Repeated issues with HPC jobs despite previous warnings.
- User's jobs require manual reactivation of nodes.

## Root Cause
- User was implicitly using hyperthreading by specifying 40 CPUs per node instead of the available 20 physical CPUs.
- Systematic testing of different parallelization options in Yambo led to out-of-memory events.

## Solution
- User corrected the job submission script to request only 20 CPUs per node.
- User proposed to stop testing with higher cutoff values and continue with less memory-intensive calculations.
- User suggested spreading out tests over a longer period to avoid overwhelming the system.

## Lessons Learned
- Ensure job submission scripts are correctly configured to avoid hyperthreading issues.
- Systematic testing of parallelization options can lead to out-of-memory events.
- Spreading out tests over a longer period can help reduce the impact on the system.
- Manual reactivation of nodes is required after out-of-memory events, which can be burdensome for HPC admins.
- Communication and coordination with users are essential to find sustainable solutions.

## Next Steps
- Schedule a Zoom meeting with the user, second-level support team, and HPC admins to discuss a long-term solution.
- Implement mechanisms to automatically handle out-of-memory events if possible.
- Continue monitoring the user's jobs to ensure compliance with the agreed-upon solutions.
---

### 2023030742001761_Using%20VASP%20with%20OpenMP.md
# Ticket 2023030742001761

 # HPC Support Ticket: Using VASP with OpenMP

## Keywords
- VASP
- OpenMP
- MPI
- Hybrid Parallelization
- SLURM
- OMP_PLACES
- OMP_PROC_BIND
- OMP_NUM_THREADS

## Summary
- **Issue**: User experienced errors when running VASP with hybrid MPI+OpenMP parallelization.
- **Root Cause**: Incorrect setting of `OMP_PLACES` and `OMP_NUM_THREADS`.
- **Solution**: Correctly set `OMP_PLACES` to "cores" and use SLURM syntax to set the number of threads.

## Detailed Conversation

### Initial Suggestion
- **HPC Admin**: Recommended using hybrid MPI+OpenMP parallelization for VASP6.
  - Suggested configuration: 4 MPI processes and 18 OpenMP threads per node.
  - Added environment variables:
    ```bash
    export OMP_PLACES=cores
    export OMP_PROC_BIND=true
    ```

### User Feedback
- **User**: Reported that hybrid mode seemed faster by about 30%.
- **User**: Encountered errors when running hybrid mode for a specific calculation.

### Troubleshooting
- **HPC Admin**: Clarified that `OMP_PLACES` should be set to "cores" and not a number.
  - Correct SLURM syntax for setting threads:
    ```bash
    #SBATCH --cpus-per-task=18
    export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
    echo "OMP_NUM_THREADS=$OMP_NUM_THREADS"
    export OMP_PLACES=cores
    export OMP_PROC_BIND=true
    ```

### Further Assistance
- **HPC Admin**: Requested access to the user's directory to diagnose the error.
- **HPC Admin**: Provided additional tips for running VASP with hybrid XC functional.

## Lessons Learned
- **Hybrid Parallelization**: Combining MPI and OpenMP can improve performance for certain workloads.
- **Environment Variables**: Correctly setting `OMP_PLACES` and `OMP_NUM_THREADS` is crucial for proper functioning.
- **SLURM Syntax**: Use SLURM syntax to set the number of threads for OpenMP.

## References
- [OpenMP Specification](https://www.openmp.org/spec-html/5.0/openmpse53.html)
- [VASP Tips and Tricks](https://hpc.fau.de/systems-services/documentation-instructions/special-applications-and-tips-tricks/vasp)
---

### 2023051742001917_ClusterCockpit%2C%20Filters%2C%20Statistics.md
# Ticket 2023051742001917

 # HPC Support Ticket: ClusterCockpit Filters Based on Statistics Issue

## Keywords
- ClusterCockpit
- Filters
- Statistics
- Non-running jobs
- Job states

## Problem Description
The user is unable to manage filters based on statistics in ClusterCockpit. The options work fine, but the "Statistics" feature does not function regardless of the measure selected. The user has tried all job states (running, completed, etc.) before attempting to manage filters based on statistics.

## Root Cause
The root cause of the problem is not explicitly stated in the conversation. However, it appears to be related to the functionality of the "Statistics" feature in the "Filters" menu of ClusterCockpit, specifically when dealing with non-running jobs.

## Solution
No solution is provided in the conversation. The ticket was closed without a clear resolution.

## General Learnings
- **ClusterCockpit Issues**: Be aware of potential issues with the "Statistics" feature in the "Filters" menu.
- **Job States**: Ensure to test filters with different job states (running, completed, etc.) to identify any state-specific issues.
- **Ticket Closure**: Ensure tickets are closed with a clear resolution or next steps for the user.

## Next Steps for Support
- Investigate the "Statistics" feature in ClusterCockpit to identify any bugs or configuration issues.
- Provide a clear resolution or workaround for the user if the issue is identified.
- Update documentation to reflect any known issues or solutions related to ClusterCockpit filters and statistics.
---

### 2024062042002737_LIKWID%20issues%20with%20perfcounter.md
# Ticket 2024062042002737

 ```markdown
# LIKWID Issues with Perfcounter

## Keywords
- LIKWID
- Perfcounter
- Multi-node jobs
- Timeout
- Access Daemon
- Filesystem

## Problem Description
When running multi-node jobs with LIKWID performance counter features enabled, especially with multiple jobs submitted, LIKWID often fails to read out the needed metrics. The error messages indicate issues with accessing the performance counters and socket files.

## Error Messages
- `ERROR - [/apps/FAUsrc-EL8/likwid/likwid-5.3.0/src/access_client.c:226] No such file or directory`
- `Exiting due to timeout: The socket file at '/tmp/likwid-1179670' could not be opened within 10 seconds.`
- `ERROR - [/apps/FAUsrc-EL8/likwid/likwid-5.3.0/src/perfmon.c:perfmon_init:2131] Cannot get access to performance counters`
- `/usr/bin/id: cannot find name for user ID 210964`
- `/usr/bin/id: cannot find name for group ID 80121`

## Root Cause
The issue is primarily related to the filesystem side rather than LIKWID itself. There is a 15-second timeout, and when multiple nodes/jobs/tasks start up simultaneously, this timeout is not sufficient.

## Solution
Preload the access daemon to the node to ensure it is running before the job starts. This can be done using the following commands:

```bash
srun -N <num_nodes> -n 1 /apps/FAUsrc-EL8/likwid/likwid-5.3.0/sbin/likwid-accessD
sleep(15)
```

This ensures that `likwid-accessD` is started once on every node and has enough time to initialize before the job begins.

## Additional Information
- A full log and instructions for reproducing the issue are available [here](https://gitlab.cs.fau.de/ed86uzaf/parconnect/-/blob/master/LIKWID-ERROR.md).
- For further assistance, contact the HPC support team.
```
---

### 2022120842003028_Jobs%20auf%20Woody%20-%20iw30001h.md
# Ticket 2022120842003028

 # HPC Support Ticket: Jobs auf Woody - iw30001h

## Keywords
- Job resource allocation
- Core reservation
- Serial application
- Memory usage
- Billing

## Problem
- User was requesting 32 cores for jobs on Woody.
- The application appeared to be serial.
- Memory usage was higher than what was allocated per core, but jobs never used more than 1/5 of the node's memory.

## Root Cause
- Misunderstanding of resource allocation: User thought specifying `#SBATCH –cpus-per-task=32` allowed the code to use up to 32 cores if needed, not realizing it reserved 32 cores by default.

## Solution
- HPC Admin reduced the allowed cores for the user's account from 1000 to 600.
- User was advised to request only the necessary cores for their jobs in the future.

## General Learnings
- Cores and associated memory are allocated based on the job request, regardless of actual usage.
- Users are billed for the resources they request, not just what they use.
- Proper resource allocation is crucial for efficient use of HPC systems.
- Even with higher than expected usage, the user was still within acceptable limits.

## Actions Taken
- HPC Admin updated the user's account to reduce the number of allowed cores.
- HPC Admin explained the resource allocation and billing policy to the user.

## Follow-up
- User apologized for the misunderstanding and agreed to request resources more appropriately in the future.
- HPC Admin assured the user that their usage was still within acceptable limits.
---

### 2019120442002337_Job%20on%20Meggie%20557793%20-%20WRF%20_%20gwgk0003h.md
# Ticket 2019120442002337

 # HPC Support Ticket Conversation Analysis

## Subject: Job on Meggie 557793 - WRF

### Keywords:
- Job Submission
- SLURM
- MPI
- Environment Variables
- WRF Simulation
- Debugging
- Job Stalling

### Summary:
The user encountered issues with job submission and execution on the HPC system. The main problems included improper resource allocation, incorrect MPI executable usage, and environment variable misconfiguration.

### Issues Identified:
1. **Resource Allocation**:
   - The user specified `mpiexec -N 20` while requesting 16 nodes with 20 cores each, leading to only the first node being used.
   - **Solution**: Remove `mpiexec -N 20` and ensure proper SLURM directives:
     ```bash
     #SBATCH --nodes=16
     #SBATCH --tasks-per-node=20
     ```

2. **Incorrect MPI Executable**:
   - The user was using an MPI executable from a Conda environment instead of the one from Intel MPI.
   - **Solution**: Ensure the correct MPI executable is used by setting the appropriate environment variables and paths.

3. **Environment Variables**:
   - The user was loading modules in their `.profile`, which complicated debugging.
   - **Solution**: Remove `#SBATCH --get-user-env` from the SLURM script and explicitly set the environment inside the batch script.

4. **Job Stalling**:
   - The user's jobs were stalling without producing output files.
   - **Solution**: Check the compilation of `wrf.exe` and ensure the correct versions of libraries (HDF5/NetCDF) are used. Consider using pre-built WRF modules if available.

### Recommendations:
- Use the development queue for testing and debugging:
  ```bash
  #SBATCH --partition=devel
  #SBATCH --time=01:00:00
  #SBATCH --nodes=4
  ```
- Consult with colleagues who have successfully run similar simulations.
- Follow the protocol for building WRF and use the correct versions of required libraries.

### Additional Notes:
- Ensure that the environment is set explicitly within the batch script to avoid conflicts and simplify debugging.
- Monitor job activity and output to identify issues early.

### Conclusion:
Proper resource allocation, correct MPI executable usage, and explicit environment variable settings are crucial for successful job execution on the HPC system. Following these recommendations should help resolve the issues encountered by the user.
---

### 2022021842001101_Jobs%20auf%20emmy%20%7C%20corz036h.md
# Ticket 2022021842001101

 # HPC-Support Ticket Conversation Analysis

## Subject: Jobs auf emmy | corz036h

### Keywords
- HPC Cluster
- Job Performance
- MPI
- mpirun
- SMT Threads
- Resource Allocation
- OpenMPI
- Job Output
- Access Key

### General Learnings
- Importance of proper resource allocation in HPC jobs.
- Differences in MPI variants (e.g., OpenMPI vs. IntelMPI) and their impact on job distribution.
- How to modify `mpirun` commands to avoid using SMT threads.
- Checking job performance and resource utilization using provided web links and access keys.

### Root Cause of the Problem
- User's jobs were not utilizing all allocated nodes effectively due to improper `mpirun` configuration, leading to the use of SMT threads and leaving other nodes empty.

### Solution
- Add the `-npernode 20` option to the `mpirun` command to ensure that only 20 processes are started per node, avoiding the use of SMT threads.

### Example
- Original Command: `mpirun -np 160 python3 simulation.py`
- Modified Command: `mpirun -np 160 -npernode 20 python3 simulation.py`

### Additional Notes
- Users should regularly check the performance of their completed jobs to ensure efficient resource utilization.
- Access keys for job outputs can be found at the end of the job output files and used to review job performance on the provided web link.

### References
- HPC Services, Friedrich-Alexander-Universitaet Erlangen-Nuernberg
- Regionales RechenZentrum Erlangen (RRZE)
- [HPC Status Job Info](https://www.hpc.rrze.fau.de/HPC-Status/job-info.php)

### Roles Involved
- **HPC Admins**: Provided guidance on proper `mpirun` configuration and resource allocation.
- **User**: Requested assistance with optimizing job performance and resource utilization.
---

### 42277777_Problem%20running%20jobs%20on%20lima.md
# Ticket 42277777

 # HPC Support Ticket Analysis

## Keywords
- FORTRAN libraries
- MPI versions
- Disk quota
- Job abortion
- Module loading

## Lessons Learned

### Issue 1: Missing FORTRAN Libraries
- **Root Cause**: Incompatible MPI versions and improper module loading.
- **Solution**: Ensure consistent MPI versions during compilation and execution. Load the same modules used during compilation in the job script.

### Issue 2: Disk Quota Exceeded
- **Root Cause**: User's disk usage exceeded the allowable limit.
- **Solution**: Check the maximum allowable disk usage for users and ensure the user stays within the limit.

## General Guidelines
- Always load the same modules used during software compilation in job scripts.
- Avoid mixing different MPI versions as they are generally incompatible.
- Regularly monitor disk usage to prevent jobs from being aborted due to exceeded quotas.

## Actions Taken
- HPC Admin provided guidance on module loading and MPI version consistency.
- User resolved the FORTRAN library issue by following the admin's advice.
- A new ticket was created for the disk quota issue to address it separately.

## Future Reference
- Ensure users are aware of the importance of consistent module loading and MPI versions.
- Provide clear documentation on disk quota limits and how to monitor usage.

---

This report can be used as a reference for support employees to troubleshoot similar issues in the future.
---

### 2019100642000482_Aktuelle%20STAR-CCM%2B-Version%20auf%20Tiny.md
# Ticket 2019100642000482

 ```markdown
# HPC Support Ticket Conversation Analysis

## Keywords
- STAR-CCM+
- Memoryhog
- TinyFAT
- Job priority
- Resource utilization
- Simulation
- Mesh generation
- Postprocessing
- Account sharing
- Monitoring data

## General Learnings
- **Job Priority**: Job priority can be reduced due to inefficient resource utilization.
- **Resource Utilization**: Efficient use of computational resources is crucial for maintaining job priority.
- **Simulation Steps**: Different steps of a simulation (e.g., mesh generation, postprocessing) should be optimized for resource usage.
- **Monitoring**: Monitoring data can be accessed online using specific tools provided by the HPC services.
- **Account Sharing**: Account sharing is against the usage rules and should be avoided.
- **Software Updates**: Software updates can be requested and provided by the HPC support team.

## Root Causes and Solutions

### Root Cause: Inefficient Resource Utilization
- **Problem**: Jobs using too many nodes without efficient utilization.
- **Solution**: Optimize the number of nodes requested for each job step to improve resource utilization and maintain job priority.

### Root Cause: Lack of Response to Support Emails
- **Problem**: Delayed or no response to support emails leading to reduced job priority.
- **Solution**: Ensure timely response to support emails to avoid misunderstandings and maintain job priority.

### Root Cause: Incorrect Job Configuration
- **Problem**: Jobs not executing FLOPs or showing poor runtime behavior.
- **Solution**: Check job configurations and ensure they are correctly set up for efficient execution.

### Root Cause: Insufficient Memory for Mesh Generation
- **Problem**: Mesh generation requiring more memory than available on standard nodes.
- **Solution**: Use nodes with larger memory capacity for mesh generation steps.

### Root Cause: Account Sharing
- **Problem**: Suspicion of account sharing due to multiple people responding to support emails.
- **Solution**: Ensure that only the account owner responds to support emails to avoid suspicion of account sharing.

## Documentation for Support Employees

### STAR-CCM+ Updates
- **Request**: Update STAR-CCM+ to the latest version.
- **Solution**: HPC Admins can provide updates and ensure compatibility with existing systems.

### Job Priority Management
- **Issue**: Job priority reduced due to inefficient resource utilization.
- **Solution**: Optimize job configurations to use resources efficiently and respond to support emails promptly.

### Monitoring Data Access
- **Request**: Access to monitoring data for job performance analysis.
- **Solution**: Monitoring data can be accessed online using the provided tools and access keys.

### Resource Utilization Optimization
- **Issue**: Inefficient use of computational resources leading to reduced job priority.
- **Solution**: Optimize the number of nodes requested for each job step and ensure efficient resource utilization.

### Account Sharing Prevention
- **Issue**: Suspicion of account sharing due to multiple people responding to support emails.
- **Solution**: Ensure that only the account owner responds to support emails to avoid suspicion of account sharing.

### Software Command Equivalents
- **Request**: Command equivalent for starting simulations on Memoryhog.
- **Solution**: Memoryhog does not support batch systems; simulations need to be started interactively.
```
---

### 2020121042000922_Last%20friendly%20reminder%20Yambo%20Job%20Emmy%201398166%20mpp3000h.md
# Ticket 2020121042000922

 # HPC Support Ticket: Yambo Job Configuration Issue

## Keywords
- Yambo Jobs
- Job Configuration
- MPI
- OpenMP
- Resource Utilization
- Job Removal

## Summary
A user has repeatedly submitted incorrectly configured Yambo jobs to the cluster, leading to inefficient resource utilization. The HPC Admin has issued a final warning before taking action to remove such jobs without further notice.

## Root Cause
- **Incorrect MPI Configuration**: The user configured `mpirun -np 20 -ppn 10`, which starts 20 processes with 10 processes per node. However, the user requested 12 nodes, resulting in 10 nodes being idle.
- **OpenMP Threading Issue**: The OpenMP threading was not functioning correctly, leading to uneven load distribution between nodes. The first node had a load of ~14, while the second node had a load of ~10, with only the first node performing calculations.

## Solution
- **Correct MPI Configuration**: Ensure that the number of processes and nodes requested are correctly aligned to avoid idle nodes.
- **Fix OpenMP Threading**: Address the OpenMP threading issue to ensure even load distribution and efficient resource utilization across all nodes.

## Action Taken
- The HPC Admin has warned the user about the consequences of repeated misconfigurations and provided specific details about the current issue.
- A screenshot of the current resource utilization was attached for reference.

## Next Steps
- The user should correct the job configuration and address the OpenMP threading issue.
- The HPC Admin will remove jobs without further warning if the issue persists.

## Notes
- This ticket serves as a reminder for proper job configuration and efficient resource utilization on the cluster.
- Users should ensure that their job configurations are optimized to avoid wasting computational resources.
---

### 2024011642000891_Multi-gpu%20flag%20request.md
# Ticket 2024011642000891

 ```markdown
# HPC Support Ticket: Multi-GPU Flag Request

## Keywords
- Multi-GPU training
- QoS flag
- a100multi
- User account

## Summary
A user requested the addition of the multi-node flag option `--qos=a100multi` to facilitate multi-GPU training.

## Root Cause
The user needed the `--qos=a100multi` flag to be enabled for their account to perform multi-GPU training.

## Solution
The HPC Admin enabled the `--qos=a100multi` option for the user's account.

## General Learning
- Users may require specific QoS flags for advanced computing tasks such as multi-GPU training.
- HPC Admins can enable these flags upon user request.
- Ensure proper communication and confirmation of the request and its fulfillment.
```
---

### 2018061242002139_Bitte%20um%20Jobverl%C3%83%C2%A4ngerung.md
# Ticket 2018061242002139

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject: Bitte um Jobverlängerung

### Keywords:
- Job extension
- Meggie
- Netz-I/O
- Job phases

### Summary:
A user requested an extension of their running processes on the HPC system "Meggie" by 20 days. The HPC Admin provided insights into job behavior, suggesting that the issue might be related to the job transitioning into a different phase, which is accompanied by significant network I/O.

### Root Cause:
- The job might be transitioning into a different phase, causing significant network I/O.

### Solution:
- No explicit solution provided in the conversation. Further investigation into job phases and network I/O might be required.

### General Learnings:
- Job extensions can be requested by users.
- Job behavior, such as network I/O, can change during different phases of the job.
- Admins can analyze job graphs to understand job behavior and potential issues.
```
---

### 2024081242003159_Frontend%20node%20allocation.md
# Ticket 2024081242003159

 # HPC Support Ticket: Frontend Node Allocation Issue

## Keywords
- Frontend node allocation
- Meggie cluster
- Resource allocation delay
- Scheduled downtime
- Reboot

## Problem Description
- **User Issue**: The user reported difficulty accessing the frontend node of the Meggie cluster, experiencing long delays in resource allocation.
- **Context**: The user mentioned a scheduled downtime starting the next day.

## Root Cause
- **Identified Issue**: There was a problem with the Meggie cluster that required a reboot.

## Solution
- **Action Taken**: The HPC Admin rebooted the Meggie cluster to resolve the issue.

## Lessons Learned
- **Monitoring**: Regular monitoring and user feedback are crucial for identifying and resolving issues promptly.
- **Communication**: Clear communication about scheduled downtimes and system issues helps manage user expectations.

## Next Steps
- **Follow-up**: Ensure the user can access the frontend node after the reboot.
- **Documentation**: Update internal documentation to include steps for troubleshooting similar issues in the future.

---

This report provides a concise overview of the issue, the actions taken, and the lessons learned, which can be used to address similar problems in the future.
---

### 2024102842001841_Alex%20Multi-Node%20Access%20f%C3%83%C2%BCr%20SCC%20Studis.md
# Ticket 2024102842001841

 # HPC Support Ticket: Multi-Node Access for SCC Students

## Keywords
- Multi-node access
- Student Cluster Competition (SCC)
- Alex cluster
- GPU limit
- Account configuration

## Problem
- **User Request:** Enable multi-node access on the Alex cluster for SCC students (scvl100).
- **Details:** The request is for access to 2 nodes for testing purposes, not performance.

## Solution
- **Action Taken:** HPC Admins granted multi-node access to the specified accounts.
- **Configuration:** Accounts now have `a40/100multi` and a limit of 16 GPUs.

## What Can Be Learned
- **Process:** HPC Admins can configure multi-node access and GPU limits for specific user groups.
- **Use Case:** This is useful for educational purposes, such as allowing students to test multi-node setups.

## Notes
- Ensure proper communication with users to understand their specific needs.
- Document any changes made to user accounts for future reference.

---

This documentation can be used to handle similar requests for multi-node access and GPU limits on the Alex cluster.
---

### 2024120642002332_Tier3-Access-Fritz%20%22Daniela%20Ayvazova%22%20_%20iwst112h.md
# Ticket 2024120642002332

 # HPC Support Ticket: Tier3-Access-Fritz

## Keywords
- Tier 3 Access
- Single-node throughput
- Multi-node workload
- Python
- Fortran compiler
- MPI
- High-fidelity simulations
- Turbulent flows
- Master's thesis
- Statistical averages

## Summary
- **User Request**: Access to Tier 3 systems for high-fidelity simulations of turbulent flows and data analysis.
- **Requirements**:
  - Single-node throughput (72 cores, 250 GB)
  - Multi-node workload (HDR100 Infiniband with 1:4 blocking; per node: 72 cores, 250 GB)
  - 200,000 node hours on Fritz
  - Software: Python, Fortran compiler, MPI
- **Expected Outcomes**: Optimization of computing and human time for statistical averages in high-fidelity simulations.

## Root Cause
- User needs access to Tier 3 systems for running simulations and analyzing large datasets.

## Solution
- HPC Admin confirmed the request as "done," indicating that the access was granted.

## Learning Points
- Understanding the process for requesting and granting Tier 3 access.
- Importance of justifying resource requirements for high-performance computing.
- Common software tools used in high-fidelity simulations and data analysis (Python, Fortran compiler, MPI).

## Next Steps
- Ensure the user is aware of the granted access and any follow-up procedures.
- Monitor the usage of resources to ensure compliance with the requested specifications.

---

This documentation can be used as a reference for handling similar requests for Tier 3 access and understanding the typical requirements and processes involved.
---

### 2024022842002686_Tier3-Access-Fritz%20%22Richard%20Angersbach%22%20_%20iwia025h.md
# Ticket 2024022842002686

 # HPC Support Ticket Analysis

## Keywords
- Account activation
- Fritz cluster
- Multi-node workload
- HDR100 Infiniband
- Benchmarking
- Performance evaluation

## Summary
- **User Request:** Access to Fritz cluster for multi-node workload with specific hardware and software requirements.
- **HPC Admin Response:** Account enabled for Fritz cluster.

## Details
- **Hardware Requirements:**
  - HDR100 Infiniband with 1:4 blocking
  - 72 cores per node
  - 250 GB memory per node
- **Software Requirements:**
  - Compiler modules
  - Likwid
  - MPI runtimes
  - CMake
  - Git
- **Compute Time:** 1000 node hours on Fritz
- **Application:** Benchmarking of a generated multigrid solver with mesh refinement
- **Expected Outcomes:** Performance evaluation of computation and communication routines for icelake architectures

## Solution
- HPC Admin enabled the user's account for access to the Fritz cluster.

## General Learnings
- Proper documentation of user requests and admin responses is crucial for tracking and resolving issues.
- Understanding user requirements for hardware and software is essential for providing appropriate support.
- Clear communication between users and HPC admins ensures efficient resolution of access requests.
---

### 2020052742002859_Is%20simulation%20running%20or%20stalled%20openFoam-V1906..md
# Ticket 2020052742002859

 # HPC Support Ticket: Is Simulation Running or Stalled OpenFoam-V1906

## Keywords
- OpenFoam
- Simulation
- Stalled Job
- Log File
- Processor Load
- Decomposition
- Control Volume
- Collated File Format

## Summary
A user reported an issue with an OpenFoam simulation that appeared to be stalled despite showing processor load. The job was submitted using a batch script and involved a large number of processors.

## Problem Description
- **Module**: openfoam/1906-gcc8.2.0-openmpi-55wj52l
- **Nodes**: 50
- **Processors**: 1998
- **Mesh**: 12 million control volumes
- **Decomposition**: Successfully decomposed into 1998 processors
- **File Format**: Collated file format used to reduce unnecessary folder creation
- **Log File**: Empty logfile.log and no standard error recorded
- **Job Status**: Running according to `qstat -a`

## Root Cause
- The simulation was stalled, generating processor load but not performing any operations.
- The issue was likely related to the large number of processes (1998) used, as a similar simulation with 318 processors ran successfully.

## Solution
- **Monitor Log File**: Monitor the log file to determine if the job is still running. If nothing is written for an extended period, the job is likely stalled.
- **Cancel and Resubmit**: Cancel the stalled job and resubmit it.
- **Reduce Processors**: Consider reducing the number of processors. Using 1998 processors resulted in only 6000 control volumes per process, which is generally not efficient for computation.

## Additional Notes
- The user explained that the decomposition in OpenFoam is determined by the product of xDecomposition, yDecomposition, and zDecomposition, which limited the number of processors to 1998.
- The HPC Admin suggested that the issue might be an internal problem with OpenFoam related to the large number of processes.

## Conclusion
The simulation stalled due to the large number of processes used. Reducing the number of processors and monitoring the log file can help resolve the issue. If the problem persists, further debugging of the simulation process may be necessary.
---

### 2025020842000741_Tier3-Access-Fritz%20%22cai%20tian%22%20_%20iwst114h.md
# Ticket 2025020842000741

 # HPC Support Ticket Conversation Analysis

## Keywords
- HPC Account Activation
- Fritz Cluster
- Single-node Throughput
- Multi-node Workload
- Python
- Computational Fluid Dynamics (CFD)
- Data-driven Optimization
- Bayesian Method
- Fluid-dynamic Loads
- Cylindrical Structures

## Summary
- **User Request**: The user requested access to the Fritz HPC cluster for a project involving computational fluid dynamics (CFD) simulations and data-driven optimizations.
- **Resource Requirements**:
  - Single-node throughput (72 cores, 250 GB)
  - Multi-node workload (HDR100 Infiniband with 1:4 blocking; per node: 72 cores, 250 GB)
  - 990,000 node hours on Fritz
- **Software Needed**: Python
- **Application**: The project aims to reduce fluid-dynamic loads on cylindrical structures using CFD simulations and data-driven optimizations.

## Actions Taken
- **HPC Admin**: The HPC account was enabled on Fritz.

## Lessons Learned
- **Account Activation**: Ensure that new user accounts are promptly activated after receiving the request.
- **Resource Allocation**: Understand the specific resource requirements for different types of workloads (single-node vs. multi-node).
- **Software Availability**: Ensure that the required software (Python in this case) is available and properly configured on the cluster.

## Root Cause of the Problem
- The user needed access to the Fritz HPC cluster for a specific project involving CFD simulations and data-driven optimizations.

## Solution
- The HPC Admin enabled the user's account on the Fritz cluster, addressing the user's need for access.

## Future Reference
- This ticket can serve as a reference for handling account activation requests and understanding the resource requirements for CFD and data-driven optimization projects.
---

### 42193135_Jobs%20on%20Woody.md
# Ticket 42193135

 # HPC Support Ticket: Jobs on Woody

## Keywords
- Job script
- Resource allocation
- MPI
- mpirun
- Node utilization

## Issue
- User requested 8 nodes but specified `-np 3` in the job script, leading to underutilization of resources.
- Only the first node was partially used, leaving 7 nodes empty.

## Root Cause
- Incorrect specification of the number of processes (`-np`) in the job script.

## Solution
- Correct the job script to specify the appropriate number of processes (e.g., `-np 32`).
- Alternatively, remove the explicit `-np` argument to use all allocated resources by default.

## General Learning
- Ensure that the number of processes specified in the job script matches the requested resources.
- Using the default behavior of `mpirun` can simplify job script configuration.

## Actions Taken
- HPC Admins deleted the running jobs to prevent resource wastage.
- User was advised to correct the job script and resubmit the jobs.
---

### 2021100642004198_Fwd%3A%20%5BOptik%5D%20WG%3A%20Abgabe%20DELTA%20HPC%20Clustersystem.md
# Ticket 2021100642004198

 ```markdown
# HPC-Support Ticket: Abgabe DELTA HPC Clustersystem

## Subject
Fwd: [Optik] WG: Abgabe DELTA HPC Clustersystem

## Keywords
- HPC Cluster
- Hardware Donation
- Emmy Nodes
- Woody Nodes
- Infinityband
- DELTA HPC Cluster

## Summary
A user inquired about the potential interest in acquiring an 8-year-old DELTA HPC Cluster system from the Max-Planck-Institut für Chemische Physik fester Stoffe in Dresden. The system includes CPUs/nodes similar to Emmy nodes and features 40 GB/s Infinityband.

## User Inquiry
The user forwarded an email about the availability of the DELTA HPC Cluster system, suggesting it might be useful as additional Woody nodes or as a replacement/extension for Emmy nodes. The user acknowledged the age of the hardware but wanted to share the information.

## HPC Admin Response
The HPC Admin thanked the user for the information but noted that due to the age of the hardware and the upcoming delivery of a new parallel computer, the offered nodes are not of interest.

## Lessons Learned
- **Hardware Age Consideration**: Older hardware may not be worth the effort, especially if newer systems are expected soon.
- **Community Collaboration**: Sharing information about available resources, even if not immediately useful, can be beneficial for future reference.
- **Cluster Expansion**: Evaluating the compatibility and usefulness of donated hardware requires careful consideration of current and future needs.

## Root Cause
The user was interested in potential hardware donations to expand or replace existing HPC resources.

## Solution
The HPC Admin determined that the offered hardware was not suitable due to its age and the impending arrival of new systems.
```
---

### 2022111842001414_VASP%20Job%20auf%20Meggie%20%5Bmpap002h%5D.md
# Ticket 2022111842001414

 # HPC Support Ticket: VASP Job auf Meggie

## Keywords
- VASP
- SLURM
- $SLURM_CPUS_PER_TASK
- MPI
- OpenMP
- Job Script Optimization

## Problem
- The user's VASP job script was using the variable `$SLURM_CPUS_PER_TASK`, which was set to 0 due to the current SLURM commands.
- The job was not optimally utilizing the hardware resources.

## Root Cause
- The user's job script was not correctly configured to use hybrid MPI/OpenMP parallelization.
- The VASP binary was compiled without OpenMP support, making the use of `$SLURM_CPUS_PER_TASK` unnecessary.

## Solution
- **For MPI-only jobs:**
  - Reduce the number of nodes and increase the number of MPI tasks per node.
  - Example configuration:
    ```bash
    #SBATCH --nodes=4
    #SBATCH --tasks-per-node=20
    ```
- **For hybrid MPI/OpenMP jobs:**
  - Add the following line to the job script with the desired number of OpenMP threads:
    ```bash
    #SBATCH --cpus-per-task=<Anzahl OMP Threads>
    ```

## General Learnings
- Always ensure that the job script is configured to match the parallelization method used by the application (MPI, OpenMP, or hybrid).
- Proper configuration of SLURM variables is crucial for optimal resource utilization.
- Regularly review and update job scripts to remove any outdated or unnecessary variables.

## Follow-up
- If the job cannot be completed in the allocated time, the user can request additional nodes.
- For further assistance, the user can contact the HPC support team.
---

### 2023090142000584_Rechenzeit%20auf%20Fritz_Meggie%20kaufen%3F.md
# Ticket 2023090142000584

 # HPC-Support Ticket Conversation Analysis

## Keywords
- Rechenzeit
- Industrielle Projekte
- Core-h
- Fritz-Cluster
- Lizenzierung
- Datenschutz
- Sicherheitsanforderungen
- FAU-Einrichtung

## Summary
A user inquires about purchasing compute time for an industrial project on the Fritz/Meggie HPC systems, despite no longer being affiliated with FAU. The HPC Admin provides information on the feasibility and potential costs, as well as additional considerations such as software licensing, data protection, and security requirements.

## Root Cause of the Problem
The user needs to understand the availability and cost of purchasing compute time for an industrial project on the Fritz/Meggie HPC systems.

## Solution
The HPC Admin outlines the following points:
- The HPC center generally does not sell compute time but is open to discussing the user's specific needs.
- The user estimates a need for 12 Fritz-Nodes for 1.5 months, totaling 1-1.5 million core-hours, spread over 6-12 months.
- The HPC Admin asks for more details on software licensing, data protection requirements, and potential collaboration with a FAU institution.

## What Can Be Learned
- The HPC center is cautious about selling compute time for industrial projects but is willing to consider specific cases.
- Users should provide detailed estimates of their compute needs, including the number of nodes and core-hours.
- Additional considerations for industrial projects include software licensing, data protection, and security requirements.
- Collaboration with a FAU institution may be beneficial for such projects.

## Next Steps
- The user should provide more information on software licensing, data protection requirements, and potential FAU collaboration.
- The HPC Admin will evaluate the feasibility and cost of providing the requested compute time based on the additional information.
---

### 2020112742000894_Your%20Job%20on%20Meggie%28%20iww8018h%2C%20842585%29.md
# Ticket 2020112742000894

 # HPC Support Ticket Analysis

## Subject: Your Job on Meggie (iww8018h, 842585)

### Keywords
- Job behavior
- Resource settings
- MPI / OpenMP tasks
- Expired certificate

### Summary
- **Issue**: A user's job on Meggie exhibited strange behavior.
- **Root Cause**: Not explicitly stated, but likely related to job settings or resource requests.
- **Solution**: The user was advised to check job settings, including requested resources and MPI/OpenMP tasks.

### Details
- **HPC Admin**: Notified the user about the strange behavior of their job and suggested checking job settings.
- **Follow-up**: The ticket was closed due to no response from the user.

### Lessons Learned
- Always verify job settings, including resource requests and MPI/OpenMP tasks, when encountering strange job behavior.
- Ensure certificates are up-to-date to avoid issues related to expired certificates.

### Next Steps
- If similar issues arise, advise users to review their job settings and ensure all certificates are valid.
- Provide additional support if users need assistance with job configuration.

### References
- HPC Services, Friedrich-Alexander-Universitaet Erlangen-Nuernberg
- Regionales RechenZentrum Erlangen (RRZE)
- [HPC Support Email](mailto:support-hpc@fau.de)
- [HPC Website](http://www.hpc.rrze.fau.de/)
---

### 2022092142005347_Tier3-Access-Fritz%20%22Julian%20Benz%22%20_%20iwst079h.md
# Ticket 2022092142005347

 ```markdown
# HPC Support Ticket Conversation Analysis

## Keywords
- Account Activation
- Resource Allocation
- Multi-Node Workload
- Software Requirement
- Aeroacoustic Simulations
- DFG Project
- Large Scale Application

## Summary
- **User Request**: Access to HPC system "Fritz" for multi-node workload with specific hardware and software requirements.
- **Resource Requirements**: 4000 node hours, Star CCM+ software, 72 cores, 250 GB per node.
- **Application**: Aeroacoustic simulations for noise reduction on axial fans.
- **Additional Notes**: Simulations for students, pending large-scale application.

## Root Cause of the Problem
- The user's account needed to be activated on the HPC system "Fritz".
- The user's group had reached the limit of available nodes under the FAU-Grundversorgung.

## Solution
- **Account Activation**: The HPC Admin activated the user's account on "Fritz".
- **Resource Allocation**: The HPC Admin informed the user about the resource limitations under the FAU-Grundversorgung.

## General Learnings
- **Account Management**: Ensure timely activation of user accounts on HPC systems.
- **Resource Allocation**: Communicate resource limitations and allocation policies clearly to users.
- **Project Management**: Users should submit detailed project applications, including resource requirements and expected outcomes.

## Next Steps
- **User**: Submit a detailed application for the DFG project and the large-scale application.
- **HPC Admin**: Monitor resource usage and ensure compliance with allocation policies.
```
---

### 42075671_Calculation%20crashed%20out.md
# Ticket 42075671

 ```markdown
# HPC Support Ticket: Calculation Crashed Out

## Subject
Calculation crashed out

## User Issue
- User unable to run a VASP calculation for more than 1 hour.
- Error indicates a possible node crash.
- Job allocates 56 nodes.
- User suspects node crash but inputs are fine.

## Error Details
- Job ID: 390200
- Job Name: M4HSE06C
- Queue: work
- Requested resources: neednodes=56:ppn=4, nodes=56:ppn=4, walltime=01:00:00
- Used resources: cput=18:50:13, mem=396668436kb, vmem=462170664kb, walltime=00:07:22
- Error: `forrtl: error (78): process killed (SIGTERM)`

## HPC Admin Response
- No suspicious activity on nodes.
- Memory usage surge observed on job nodes.
- User has a history of crashing nodes due to excessive memory usage.
- Memory usage restricted to prevent node crashes.

## User Follow-Up
- User requests memory usage data for recent jobs.
- User explains job setup and requests access to a special queue for longer run times.

## HPC Admin Response
- Memory usage data not available for short jobs.
- User advised to monitor memory usage interactively.
- Memory limit lifted temporarily to allow more memory per process.
- Access to special queue denied due to priority concerns.

## User Testing
- User runs job with one core per node to avoid crashing nodes.
- Job runs but requires more iterations to converge.
- User requests further memory limit increase to use 2 cores per node.

## HPC Admin Response
- Memory limit increased to allow 2 cores per node.
- User advised to test during cluster downtime.

## User Testing
- Job crashes after 15 minutes despite monitoring memory usage.
- Memory usage around 30%.

## HPC Admin Response
- Memory limitation removed for user account.
- User advised to test again.

## Final Status
- User confirms job runs better after memory limitation removal.
- Further testing required for jobs needing more memory.

## Keywords
- VASP calculation
- Memory usage
- Node crash
- Job crash
- Memory limitation
- Special queue
- Interactive batchjob
- Memory monitoring

## Lessons Learned
- Excessive memory usage can cause job crashes.
- Monitoring memory usage interactively can help diagnose issues.
- Adjusting memory limits can resolve job crashes.
- Access to special queues may be denied due to priority concerns.
- Testing during cluster downtime can be beneficial.
```
---

### 2024102242003635_Tier3-Access-Fritz%20%22Tamas%20Gal%22%20_%20mpo1217.md
# Ticket 2024102242003635

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Keywords
- Tier3-Access-Fritz
- Multi-node workload
- HDR100 Infiniband
- MPICH/OpenMPI
- Radio Astronomy
- Software stack installation
- Testing and documentation

## Summary
- **User Request**: Access to Fritz for testing and documentation of MPI-based software stacks for the ECAP Radio Astronomy group.
- **Requirements**:
  - Multi-node workload with HDR100 Infiniband (1:4 blocking)
  - Per node: 72 cores, 250 GB
  - Rechenzeit: 1000 node hours
  - Software: MPICH/OpenMPI
- **Expected Outcome**: Successful implementation and documentation of the software stack for future calculations in radio astronomy.

## HPC Admin Response
- **Action**: User granted access to Fritz.
- **Suggestion**: Consider using KONWIHR for larger actions.

## Lessons Learned
- **Access Granting**: HPC Admins can grant access to specific clusters like Fritz.
- **Resource Allocation**: Users can request specific resources like multi-node workloads and node hours.
- **Software Requirements**: Users should specify required software (e.g., MPICH/OpenMPI) for their workloads.
- **Documentation and Testing**: Access can be granted for testing and documentation purposes.
- **Alternative Resources**: For larger actions, users may be directed to consider other resources like KONWIHR.

## Root Cause of the Problem
- User needed access to Fritz for specific workload requirements.

## Solution
- HPC Admin granted access to Fritz and suggested considering KONWIHR for larger actions.
```
---

### 42349783_ivyep1.md
# Ticket 42349783

 ```markdown
# HPC-Support Ticket: ivyep1

## Keywords
- ivyep1
- likwid
- daemon error
- no such device
- cpu 0 reg 0x38d

## Problem Description
The user encounters errors when using likwid on the ivyep1 node. The errors indicate a failure to read and write data through the daemon, with the specific error message being 'no such device' for cpu 0 reg 0x38d.

## Root Cause
The errors suggest that likwid is attempting to access a device or register that does not exist on the specified CPU.

## Solution
No explicit solution was provided in the conversation. Further investigation is required to determine if the issue is due to a misconfiguration, hardware limitation, or a bug in likwid.

## General Learnings
- **Error Identification**: Recognize the specific error message 'no such device' for cpu 0 reg 0x38d as an indication of a potential hardware or configuration issue.
- **Tool Behavior**: Understand that likwid may produce errors if it attempts to access non-existent hardware components.
- **Troubleshooting Steps**: Consider checking the hardware specifications and likwid configuration to ensure compatibility.

## Next Steps
- **Investigation**: HPC Admins or 2nd Level Support should investigate the hardware specifications of ivyep1 and the likwid configuration.
- **Consultation**: Consult with Software and Tools developers (Jan Eitzinger, Gruber) for potential updates or patches to likwid.
- **Documentation**: Update internal documentation with the findings and any resolution steps for future reference.
```
---

### 2019031342000875_w2dynamics-Jobs%20_%20iwi400h.md
# Ticket 2019031342000875

 # HPC Support Ticket: w2dynamics-Jobs / iwi400h

## Keywords
- w2dynamics-Jobs
- MPI-Library
- Performance Issues
- Monitoring Data
- Flops
- Speicherbandbreite
- Netzwerk-Traffic
- perf top

## Problem Description
The w2dynamics-Jobs are experiencing performance issues. According to `perf top`, the jobs spend 95% of the time in the MPI-Library. Monitoring data indicates that the jobs are not performing any significant operations: no Flops, no memory bandwidth usage, and no network traffic.

## Root Cause
The root cause of the problem is not explicitly stated in the conversation, but it is implied that the jobs are stuck in the MPI-Library, leading to inactivity.

## Solution
No explicit solution is provided in the conversation. Further investigation is needed to determine why the jobs are spending most of their time in the MPI-Library.

## Next Steps
- Investigate the MPI-Library to identify any potential issues.
- Check job configurations and dependencies to ensure they are correctly set up.
- Monitor the jobs closely to gather more detailed performance data.

## References
- [Job Info 1](https://www.hpc.rrze.fau.de/HPC-Status/job-info.php?USER=iwi4000h&JOBID=1071083&ACCESSKEY=365b432d&SYSTEM=EMMY)
- [Job Info 2](https://www.hpc.rrze.fau.de/HPC-Status/job-info.php?USER=iwi4000h&JOBID=1071063&ACCESSKEY=f80e04bd&SYSTEM=EMMY)
- [Job Info 3](https://www.hpc.rrze.fau.de/HPC-Status/job-info.php?USER=iwi4000h&JOBID=1071084&ACCESSKEY=21b42431&SYSTEM=EMMY)

## Notes
- The ticket indicates that job 1071153 is still running.
- Further communication with the user or additional monitoring may be required to resolve the issue.
---

### 2022112342002225_Pinning%20PARDISO.md
# Ticket 2022112342002225

 # HPC Support Ticket: Pinning PARDISO

## Keywords
- Pinning
- PARDISO
- CPU architecture
- Thread pinning
- NUMA domains
- likwid-topology
- lscpu
- hwloc
- OpenMP
- CPUset
- likwid-mpirun

## Problem
- User is experiencing variability in pinning threads for PARDISO.
- The user intends to pin the first 32 cores but observes that the actual cores being used do not match the intended pinning.
- The user seeks a command to view the architecture of the Fritz nodes.
- The user is considering distributing the workload across both CPU sockets.

## Solution
- **Viewing CPU Architecture**: Use tools like `likwid-topology` or `lscpu` to view the CPU architecture. Within a program, use `likwid` or `hwloc`.
- **Pinning Threads**: The user's code for pinning threads may not be functioning as intended. The HPC Admin suggests modifying the code to distribute the workload across both sockets:
  ```cpp
  for(int i=0; i<threads_level2 / 2; i++){
      hwt[i] = i;
  }
  for(int i=0; i<threads_level2 / 2; i++){
      // 36 is the first hwt of the 2. socket
      hwt[i] = 36 + i;
  }
  ```
- **True Pinning**: For true pinning, each OpenMP thread should be pinned to a single hardware thread using `pin_hwthreads(1, hwt[omp_get_thread_num()])`. However, this may be difficult to implement within PARDISO.
- **Alternative Pinning**: Consider using `likwid-mpirun -pin S0:0-17@S1:0-17` for pinning, but this requires further investigation.

## General Learnings
- Understanding CPU architecture is crucial for effective thread pinning.
- Tools like `likwid-topology`, `lscpu`, `likwid`, and `hwloc` are useful for viewing CPU architecture.
- Proper thread pinning requires ensuring that each thread is pinned to a specific hardware thread.
- Distributing workload across multiple CPU sockets can improve performance.
- The `likwid-mpirun` tool can be used for pinning threads, but its usage may require further investigation.
---

### 2024061442002918_Hybrid%20MPI_OpenMP%20jobs%20on%20Fritz%20-%20b144dc19.md
# Ticket 2024061442002918

 # Hybrid MPI/OpenMP Job Configuration Issue

## Keywords
- Hybrid MPI/OpenMP
- CPU Load
- Job Script
- OMP_NUM_THREADS
- SRUN_CPUS_PER_TASK
- Fritz Cluster

## Problem
- User's jobs on Fritz cluster exhibited very high CPU load.
- Job scripts were not properly configured for OpenMP or hybrid MPI/OpenMP calculations.

## Root Cause
- Incorrect or missing configuration of `OMP_NUM_THREADS` and `SRUN_CPUS_PER_TASK` in the job scripts.

## Solution
- Set `OMP_NUM_THREADS` and `SRUN_CPUS_PER_TASK` according to the template provided in the documentation: [Hybrid OpenMP/MPI Job (Single Node)](https://doc.nhr.fau.de/clusters/fritz/#hybrid-openmpmpi-job-single-node).

## General Learning
- Proper configuration of environment variables is crucial for efficient resource utilization in hybrid MPI/OpenMP jobs.
- Always refer to the official documentation for setting up job scripts to avoid performance issues.

## Follow-Up
- Ensure that users are aware of the correct configuration settings for hybrid jobs.
- Provide links to relevant documentation in support communications.
---

### 2022031042002792_Early-Fritz%20%22Christian%20Ritterhoff%22%20_%20nfcc007h.md
# Ticket 2022031042002792

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject: Early-Fritz / nfcc007h

### Keywords:
- Early-User
- Certificate Expired
- Single-Node Throughput
- Multi-Node Workload
- Infiniband HCAs
- IntelMPI
- MKL Library
- Intel Compiler
- FFT-Library

### Summary:
- **User Request:**
  - **Contact:** User requested early access to Fritz.
  - **Needs:** Single-node throughput until more Infiniband HCAs arrive (72 cores, 250 GB), multi-node workload (HDR100 Infiniband with 1:4 blocking; per node: 72 cores, 250 GB).
  - **Software:** IntelMPI, MKL library, Intel compiler.
  - **Application:** Test the new hybrid parallelized implementation of the FFT-library.
  - **Expected Results:** Evaluate performance on new nodes.

- **HPC Admin Response:**
  - **Action:** User was granted early access to Fritz.
  - **Issue:** Certificate has expired.

### Root Cause of the Problem:
- Certificate expiration.

### Solution:
- User was granted early access despite the certificate expiration issue.

### General Learnings:
- Importance of timely certificate renewal.
- Process for granting early access to users.
- Common software requirements for HPC users (IntelMPI, MKL library, Intel compiler).
- Typical use cases for early access, such as testing new implementations.

### Next Steps:
- Ensure certificate renewal processes are in place.
- Document the early access granting procedure for future reference.
```
---

### 2024102842004507_Multinode%20feature%20request%20on%20Alex%20Cluster.md
# Ticket 2024102842004507

 ```markdown
# HPC Support Ticket: Multinode Feature Request on Alex Cluster

## Keywords
- Multinode access
- Alex cluster
- A100 nodes
- Bandwidth benchmarking
- GPU application development
- Performance issues
- Waiting times

## Summary
A user requested access to multiple A100 nodes on the Alex cluster for bandwidth benchmarking and GPU application development. The HPC Admin team acknowledged the request but noted potential performance issues and long waiting times for GPUs on the Alex cluster.

## Root Cause
- The user needed multinode access for developing lecture content and benchmarking.
- The Alex cluster had known performance issues with multinode operations.
- High demand for GPUs on the Alex cluster resulted in long waiting times.

## Solution
- The HPC Admin team granted the user access to allocate multinodes on the Alex cluster.
- The user was informed about the potential issues and advised to consider waiting for the Helma cluster, which might offer better performance and availability.

## General Learnings
- Multinode access requests should be evaluated considering the current performance and demand on the cluster.
- Users should be informed about potential issues and alternative options if available.
- Communication between the user and the support team is crucial for addressing specific needs and providing appropriate solutions.
```
---

### 2018050542000058_Sperrung%20auf%20Meggie%20nach%20exzessiven%20OOM%20_%20bca109.md
# Ticket 2018050542000058

 ```markdown
# HPC Support Ticket: Excessive OOM Errors on Meggie

## Keywords
- Out-of-Memory (OOM)
- Job Crashes
- Account Suspension
- Benchmarking
- Job Optimization

## Summary
A user's account was suspended due to excessive OOM errors causing crashes on multiple nodes. The user's jobs had previously caused similar issues.

## Root Cause
- The user submitted overly large jobs without considering the memory limitations of the nodes.
- The user's benchmarking approach was too optimistic, leading to memory overuse.

## Solution
- The user consulted with the main developer of the software (Empire) to identify and fix the issue.
- The user committed to being more cautious with job submissions to avoid future OOM errors.

## Actions Taken
- The user's account was suspended by HPC Admins due to the impact on the system.
- The user met with the main developer to diagnose and resolve the problem.
- The user requested reactivation of their account after addressing the issue.

## Follow-Up
- The user's subsequent jobs were monitored and found to be within acceptable parameters.
- No further OOM errors were reported after the user's account was reactivated.

## Lessons Learned
- Users should be aware of the memory requirements of their jobs and the limitations of the HPC system.
- Benchmarking should be done carefully to avoid overloading the system.
- Regular communication with software developers can help in diagnosing and resolving issues.
```
---

### 2022021042000554_Thread%20Zahl.md
# Ticket 2022021042000554

 # HPC Support Ticket: Thread Zahl

## Keywords
- OpenMP (OMP) Parallelization
- Thread Count
- Woody Cluster
- Hybrid Application
- Oversubscription

## Problem
User is seeking an appropriate thread count for OpenMP parallelization on the Woody cluster.

## Solution
- **Woody Cluster Specifications**: Each Woody node has 4 cores.
- **Recommended Thread Count**:
  - For pure OpenMP applications: Use 4 threads.
  - For hybrid applications: Ensure the product of the number of processes and OpenMP threads equals 4.
- **Oversubscription**: The solution assumes the application does not benefit from oversubscription.

## General Learning
- Understanding the hardware specifications of the cluster nodes is crucial for optimizing parallelization.
- The number of threads for OpenMP should match the number of available cores for optimal performance.
- In hybrid applications, the total number of threads should be distributed appropriately between processes and OpenMP threads.

## Roles Involved
- **HPC Admins**: Provided the solution and hardware specifications.
- **User**: Requested information on thread count for OpenMP parallelization.

## Additional Notes
- Ensure that the application's performance is monitored to verify that it does not benefit from oversubscription.
- Regularly update certificates to avoid expiration issues.
---

### 2018111342000834_OpenFoam%20parallel%20I_O.md
# Ticket 2018111342000834

 # OpenFoam Parallel I/O Issue

## Keywords
- OpenFoam
- Parallel I/O
- MPI
- Threading Support
- Performance Issues
- Collated File Format

## Problem Description
The user is experiencing performance issues with OpenFoam 5 when using the collated file format for parallel I/O. The simulations are significantly slower compared to the normal decomposition into N processor folders. The user suspects that the lack of threading support for MPI might be the cause of the issue.

## Root Cause
The root cause of the performance issue is not yet determined. However, it is suspected that the lack of threading support for MPI or the use of the collated file format might be contributing to the problem. Additionally, the user mentioned that they are using 'scotch decomposition' in the decomposePar dictionary, which could also be a factor.

## Troubleshooting Steps
1. The user ran some test simulations with OpenFoam 5 using both the collated file format and the normal decomposition into N processor folders.
2. The user observed that the simulations using the collated file format were significantly slower.
3. The user requested that the HPC Admins enable threading support for MPI to see if that would improve the performance.

## Solution
The HPC Admins provided a version of OpenFoam (openfoam/5.0-trusty-ompithreads) that was compiled with MPI threading support (--enable-mpi-thread-multiple). The user was asked to run test simulations using this version and provide feedback.

## Follow-up
The HPC Admins observed that OpenFoam behaves strangely when the collated file format is selected, regardless of whether the old MPI or the updated threaded MPI is used. They also noticed significant Ethernet traffic when the collated file format is used, which might be the cause of the low performance. The issue is still under investigation.

## Lessons Learned
- The collated file format in OpenFoam 5 can cause performance issues, possibly due to increased Ethernet traffic.
- Enabling threading support for MPI might not always resolve performance issues with the collated file format.
- The choice of decomposition method (e.g., 'scotch decomposition') can also potentially impact performance.

## Next Steps
- Further investigation is needed to determine the root cause of the performance issue with the collated file format.
- The user should continue to provide feedback on their test simulations to help the HPC Admins troubleshoot the issue.
---

### 2019062742001851_Request%20of%20high%20priority%20running%20simulations%20on%20Emmy.md
# Ticket 2019062742001851

 ```markdown
# HPC Support Ticket: High Priority Request for Simulations

## Keywords
- High Priority
- Simulations
- Emmy Cluster
- SFB Transregio 103 Project
- Priority Boost
- Negative Impact

## Summary
A user requested high priority to run simulations on the Emmy cluster for a specific project. The request was granted but noted that it might negatively impact other users.

## User Request
- **Request**: High priority for running simulations on Emmy cluster until next Friday.
- **Project**: SFB Transregio 103 project.
- **Current Status**: Three jobs submitted, more to be submitted later.
- **Username**: iww1003h

## HPC Admin Response
- **Action**: Priority boost activated until July 6th.
- **Note**: The boost may have a negative impact on the rest of the group.

## Follow-Up
- **Action**: Priority boost on Emmy removed.

## Root Cause
- User needed high priority for time-sensitive simulations related to a specific project.

## Solution
- Temporary priority boost granted with a note on potential negative impact.
- Boost later removed.

## General Learning
- High priority requests should be carefully considered due to potential impacts on other users.
- Communication about the impact of priority boosts is important.
```
---

### 2024120642001468_Inquiry%20About%20Maximum%20Node%20Usage%20and%20Task%20Efficiency%20Recommendations.md
# Ticket 2024120642001468

 # HPC Support Ticket Conversation Summary

## Subject
Inquiry About Maximum Node Usage and Task Efficiency Recommendations

## Keywords
- Maximum Node Usage
- Computational Efficiency
- Error Code 143
- Slurm Job Failure
- Node Allocation

## What Can Be Learned

### Maximum Node Usage
- The maximum number of nodes depends on the cluster. For example, the Meggie cluster allows up to 64 nodes.
- Users should refer to the [documentation](https://doc.nhr.fau.de/clusters/overview/) for specific cluster limits.

### Efficiency Recommendations
- For job ID 2384685, no specific efficiency recommendations were provided as the job appeared to be utilizing all available cores effectively.

### Error Inquiry
- **Error Code 143**: The job with ID 2384626 failed with ExitCode 143.
- **Root Cause**: The error was not reproducible and affected only one job. The user suspected it might be due to requesting too many nodes (30 nodes), but this was not confirmed.
- **Solution**: The user was advised to continue with simulations and reopen the ticket if the problem reappears.

## General Guidance
- Users should ensure they are aware of the maximum node limits for their specific cluster.
- If encountering non-reproducible errors, users should monitor for recurrence and provide detailed error logs if possible.
- For efficiency recommendations, users should ensure all available cores are utilized and refer to best practices in the documentation.

## Conclusion
This conversation highlights the importance of understanding cluster-specific limits and the need for detailed error reporting for effective troubleshooting. Users should refer to the documentation for cluster-specific guidelines and best practices.
---

### 2022100442004771_Jobs%20on%20woody%20%7C%20iwsp011h.md
# Ticket 2022100442004771

 # HPC Support Ticket: Jobs on woody | iwsp011h

## Keywords
- Job allocation
- Core usage
- SLURM arrays
- Resource waste

## Problem
- User's jobs on `woody` allocated 11 cores but only used between 5 and 10 cores.
- Inefficient use of compute resources.

## Root Cause
- User misunderstood the indexing of SLURM arrays, which start at 0.
- Some job arrays finished earlier than the maximum wall time, leading to underutilization of allocated cores.

## Solution
- HPC Admin advised the user to allocate fewer cores or adjust computations to utilize all allocated cores.
- User acknowledged the issue and adjusted the jobs to run with 10 cores, starting 10 processes at the beginning of the job.

## Outcome
- Ticket closed after user adjusted job settings to better utilize allocated resources.

## General Learning
- Always ensure that the number of cores allocated to a job matches the number of processes that will run concurrently.
- Understand the behavior of job arrays and indexing in SLURM to avoid resource underutilization.
- Regularly monitor job performance to optimize resource allocation.
---

### 2018070542003033_Taktprobleme%20auf%20Knoten%20m0730.md
# Ticket 2018070542003033

 # HPC Support Ticket: Taktprobleme auf Knoten m0730

## Keywords
- Taktprobleme
- Knoten m0730
- Health check script
- Governor
- Conservative
- Job
- Cpufrequenz
- Reboot

## Summary
- **Issue**: Taktprobleme (clock issues) on node m0730.
- **Root Cause**: Unclear from the provided conversation.
- **Solution**: A health check script (`/apps/rrze/sbin/health-check-2016.sh`) was updated to include a test for the issue. The test checks if the governor is not set to conservative and if a job is running that requires a different CPU frequency.
- **Status**: The script could not be tested immediately because all affected nodes were rebooted.

## What Can Be Learned
- **Health Check Script**: The health check script was updated to include a new test for clock issues.
- **Governor Settings**: The script checks if the governor is not set to conservative and if there is a job running that requires a different CPU frequency.
- **Reboot Impact**: Rebooting nodes can prevent immediate testing of new health check scripts.

## Next Steps
- **Testing**: Once nodes with the issue are available, test the updated health check script to ensure it functions correctly.
- **Monitoring**: Continue monitoring nodes for clock issues and apply the health check script as needed.

## Roles Involved
- **HPC Admins**: Implemented the health check script update.
- **2nd Level Support Team**: Not directly involved in the provided conversation but should be aware of the script update for future reference.

## Additional Notes
- Ensure that the health check script is documented and accessible to all support team members for future troubleshooting.
---

### 2023082342002757_jobs%20with%20high%20cpu%20load%20-%20b165da.md
# Ticket 2023082342002757

 ```markdown
# HPC Support Ticket: Jobs with High CPU Load

## Keywords
- High CPU load
- Job scripts
- ntasks-per-node
- Undeliverable email

## Summary
- **Issue**: User's recent jobs have an unusually high CPU load.
- **Affected Jobs**: Jobs with `ntasks-per-node` different from 72.
- **Root Cause**: Unknown, possibly related to job scripts or code.
- **Solution**: Not provided; user advised to check job scripts and code.

## Conversation Details
- **HPC Admin**: Notified the user about high CPU load in recent jobs and suggested checking job scripts and code.
- **User**: Email delivery failure due to incorrect email address.
- **HPC Admin**: Confirmed incorrect email address.

## Lessons Learned
- **Monitoring**: Regularly monitor job performance to identify unusual CPU loads.
- **Communication**: Ensure correct email addresses for effective communication.
- **Job Configuration**: Pay attention to job configuration parameters like `ntasks-per-node`.

## Next Steps
- **User**: Check job scripts and code for potential issues.
- **HPC Admin**: Follow up with the user to ensure the issue is resolved.
```
---

### 2018082842000705__lxfs%20und%20%22Batch%20Queue%22.md
# Ticket 2018082842000705

 # HPC Support Ticket Conversation Analysis

## Keywords
- Quantenchemieprogramm GAMESS
- /lxfs
- $FASTTMP
- Batch Queue System
- Parallelisieren
- MPI
- LiMa-Cluster
- Gateway-Rechner cshpc

## Root Cause of the Problem
- User unable to access /lxfs ($FASTTMP) on the Gateway-Rechner cshpc.
- User needs examples for the Batch Queue System.
- User requires assistance with parallelizing GAMESS on multiple nodes.

## Solution
- **Access to /lxfs ($FASTTMP)**: The user can only access $FASTTMP when on the LiMa-Cluster. It is not available on the externally accessible Gateway-Rechner cshpc.
- **Batch Queue System**: Information and examples can be found at [LiMa-Cluster Batch System Documentation](https://www.anleitungen.rrze.fau.de/hpc/lima-cluster/#batch).
- **Parallelizing on Multiple Nodes**: The user's program needs to be compiled with MPI to utilize multiple nodes.

## General Learnings
- Ensure users are aware of the specific environments where certain resources (like $FASTTMP) are available.
- Provide clear documentation and examples for using the Batch Queue System.
- Emphasize the necessity of MPI compilation for programs to run on multiple nodes.

## Conclusion
The user's issues were resolved by clarifying the availability of $FASTTMP, providing documentation for the Batch Queue System, and explaining the requirement for MPI compilation for multi-node parallelization.
---

### 2021070142000386_Your%20Job%20on%20Meggie%20898258%20%28iwal050h%29.md
# Ticket 2021070142000386

 ```markdown
# HPC Support Ticket Analysis: Job Inefficiency on Meggie

## Keywords
- Job inefficiency
- Node allocation
- Parallelization
- Job monitoring
- Job database
- Job arrays

## Summary
The user's job on Meggie was inefficiently using allocated nodes, leading to resource wastage. The HPC admins provided guidance on optimizing node allocation and parallelization. Additionally, there were issues with job tracking in the database due to job arrays.

## Root Cause
- **Inefficient Node Usage**: The user's job was only utilizing one out of four allocated nodes.
- **Job Database Issue**: Job arrays caused disruptions in the job import process on Meggie.

## Solution
- **Node Allocation**: The user was advised to allocate only one node or to parallelize the simulation to use more nodes effectively.
- **Job Database Fix**: The job import issue was addressed by re-importing all jobs since June.

## Lessons Learned
- **Resource Management**: Ensure that jobs are efficiently using allocated resources to avoid wastage.
- **Parallelization**: Encourage users to parallelize their simulations to make better use of multiple nodes.
- **Job Tracking**: Regularly monitor job imports and address any issues caused by job arrays or other factors.

## Actions Taken
- **User Notification**: The user was notified about the inefficient node usage and provided with suggestions for improvement.
- **Job Termination**: The inefficient job was terminated to free up resources.
- **Database Maintenance**: The job import process was fixed, and all jobs since June were re-imported.
```
---

### 2022062242003807_Woody%3A%20iwso060h%27s%20process%20allocating%20much%20resources.md
# Ticket 2022062242003807

 ```markdown
# HPC Support Ticket: Resource Allocation Issue on Woody Frontend

## Keywords
- Resource allocation
- High memory usage
- Woody frontend
- Process management
- System load

## Problem Description
- User reported that a process (`iwso060h`) was potentially slowing down the Woody frontend (`woody3`).
- Another user (`iwi5073h`) was also reported to be allocating a large amount of RAM, causing slowdowns.

## Root Cause
- A process was consuming 120 GB of memory on a machine with only 96 GB of RAM.
- The process was using 0% CPU, indicating it was not progressing and was blocking memory for other users.

## Solution
- The offending process was identified and killed by the HPC Admin.

## Lessons Learned
- Monitoring system load and resource usage is crucial for maintaining system performance.
- Users should be educated on proper resource allocation to avoid blocking memory for other users.
- Regular checks and prompt action on processes consuming excessive resources can prevent system slowdowns.
```
---

### 42075558_Abgebrochene%20Rechnungen%20auf%20LiMa.md
# Ticket 42075558

 # HPC Support Ticket: Abgebrochene Rechnungen auf LiMa

## Keywords
- Walltime
- Job Abortion
- File System
- MPI
- PBS
- Batch Script
- Runtime

## Problem
- User noticed that jobs exceeding walltime or aborted on LiMa are not found under `wsfs` as usual on Woody.
- User inquired if this is due to their batch script or if files are located elsewhere.
- User also asked if it is normal for the runtime to display 00:00:00 throughout the computation.

## Root Cause
- Different file systems for `$FASTTMP` on LiMa and Woody.
- Batch script issue with file duplication.
- MPI start mechanism `mpiexec.hydra` does not provide CPU time information to PBS.

## Solution
- Files are located under `/lxfs` on LiMa, not `/wsfs`.
- Remove the line `. /apps/rrze/etc/use-rrze-modules.sh` from the batch script.
- Replace `cp * ${PBS_O_WORKDIR}/$JOBNAME/` with `rsync --remove-source-files * ${PBS_O_WORKDIR}/$JOBNAME/` to delete files from `$FASTTMP` upon successful copy.
- Use `qstat -a` to check the wallclock time consumed.

## General Learnings
- Understand the differences in file systems between different HPC clusters.
- Ensure batch scripts are optimized to avoid file duplication.
- Be aware of the limitations of different MPI start mechanisms regarding CPU time reporting.
- Use appropriate commands to check the wallclock time consumed by jobs.
---

### 2020101342003098_OpenFoam%20Jobs%20on%20emmy%20%7C%20iwpa014h.md
# Ticket 2020101342003098

 # HPC Support Ticket: OpenFoam Jobs on emmy | iwpa014h

## Keywords
- OpenFoam
- Job Scheduling
- mpirun
- npernode
- Node Allocation

## Issue
- **Root Cause:** User's job (1357189) was only running on two of the three requested nodes.
- **Symptom:** Inefficient resource utilization.

## Solution
- **Action Taken:** HPC Admin advised the user to add `-npernode 20` to their `mpirun` command.
- **Outcome:** This adjustment ensures that the job utilizes all requested nodes efficiently.

## General Learning
- **Resource Allocation:** Ensure that jobs are configured to utilize all allocated nodes.
- **mpirun Options:** Use `-npernode` to specify the number of processes per node.
- **Communication:** Promptly inform users of resource utilization issues and provide clear instructions for resolution.

## Relevant Parties
- **HPC Admins:** Provided support and guidance.
- **User:** Acknowledged the issue and agreed to fix it.

## Documentation
- **Purpose:** To assist in resolving similar issues related to job scheduling and resource allocation.
- **Usage:** Refer to this ticket for guidance on configuring `mpirun` for efficient node utilization.
---

### 2024112142002458_Tier3-Access-Fritz%20%22Christoph%20Alt%22%20_%20iwia027h.md
# Ticket 2024112142002458

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Keywords
- Single-node throughput
- Multi-node workload
- HDR100 Infiniband
- Intel oneAPI/Sycl
- Benchmarking
- Performance insights
- Overhead analysis

## Summary
- **User Request**:
  - **Contact**: User requested access for benchmarking and testing.
  - **Requirements**:
    - Single-node throughput (72 cores, 250 GB)
    - Multi-node workload (HDR100 Infiniband with 1:4 blocking; per node: 72 cores, 250 GB)
  - **Compute Time**: 100 node hours on Fritz
  - **Software**: Intel oneAPI/Sycl
  - **Application**: Testing and benchmarking for SyCL/OneAPI
  - **Expected Results**: Insights into SyCL/Intel OneAPI performance and overheads

- **HPC Admin Response**:
  - The request was initially deferred.
  - Later marked as completed.

## Lessons Learned
- **Request Handling**:
  - Requests for specific hardware configurations and software requirements need to be carefully reviewed.
  - Benchmarking and testing requests should be handled with attention to resource allocation and justification.

- **Software and Performance**:
  - Intel oneAPI/Sycl is a key software for benchmarking and performance testing.
  - Understanding the performance and overheads introduced by new software frameworks is crucial for optimizing HPC workloads.

- **Communication**:
  - Clear communication between users and HPC admins is essential for efficient resource allocation and problem resolution.
  - Documentation of requests and responses helps in tracking the progress and resolution of support tickets.

## Root Cause and Solution
- **Root Cause**: User required specific resources and software for benchmarking and testing.
- **Solution**: The request was reviewed and eventually marked as completed, indicating that the necessary resources and permissions were granted.
```
---

### 2020121142001821_Abbruch%20von%20grossen%20Jobs.md
# Ticket 2020121142001821

 # HPC Support Ticket Conversation Analysis

## Subject: Abbruch von grossen Jobs

### User:
**Issue:**
Large jobs (approximately 2000 ranks on 200 Compute-Nodes, no Hyperthreading) run successfully but encounter an error during or before the epilogue.

**Error Message:**
```
I_MPI_CMD is too long and will not be established
Starting epilogue... Fri Dec 11 13:07:53 CET 2020
=== JOB_STATISTICS ===
=== current date     : Fri Dec 11 13:07:53 CET 2020
= Job-ID             : 1398320.eadm
= Job-Name           : simulicious
= Queue              : big
= PBS_O_WORKDIR      : /home/hpc/mpm1/mpm1002h/Simulicious.git
= Requested resources:
ncpus=1,neednodes=100:ppn=40,nodes=100:ppn=40,walltime=01:30:00
= Used resources     :
cput=05:07:35,mem=8200900kb,vmem=32973052kb,walltime=00:16:01
= Node list          :
e1128,e1112,e1106,e1028,e1026,e1025,e1024,e1020,e1019,e1007,e1004,e0948,e0947,e0937,e0935,e0927,e0926,e0925,e0923,e0918,e0904,e0903,e0902,e0901,e0852,e0849,e0847,e0844,e0843,e0842,e0837,e0821,e0809,e0808,e0742,e0732,e0731,e0729,e0722,e0720,e0719,e0717,e0704,e0703,e0647,e0635,e0634,e0627,e0612,e0602,e0547,e0546,e0539,e0537,e0533,e0527,e0524,e0523,e0520,e0514,e0452,e0449,e0446,e0426,e0425,e0421,e0417,e0416,e0415,e0409,e0402,e0353,e0352,e0344,e0342,e0340,e0323,e0319,e0316,e0313,e0250,e0248,e0239,e0238,e0237,e0230,e0229,e0228,e0224,e0221,e0218,e0208,e0147,e0137,e0111,e0107,e0106,e0105,e0103,e0102
= AccessKey          : 2972d0ad
=====================
Power management available, setting all CPUs to ondemand govenor
End of epilogue: Fri Dec 11 13:08:24 CET 2020
===================================================
```

**Error in Error File:**
```
/var/spool/torque/mom_priv/epilogue: line 152: 40122 Killed
     /apps/rrze/bin/timeout 30 curl -u rrzeweb:rrzeweb
"http://eadm/cgi-bin/cluster-status/job-statistic.pl?jobid=${jobid}&arrayid="
```

### HPC Admin:
**Response:**
The issue is likely due to the use of `mpirun` with a long command line, which is not supported. The solution is to switch to the Intel MPI runtime by loading the Intel compiler module and using `mpirun` or `mpiexec`.

**Steps:**
1. Load the Intel compiler module.
2. Use `mpirun` or `mpiexec` from the Intel MPI runtime.

**Additional Information:**
- For more details on loading the Intel compiler module, refer to the [HPC Environment Documentation](https://www.anleitungen.rrze.fau.de/hpc/environment/#intelmpi).
- For setting the binding options, refer to the [HPC Wiki on Binding/Pinning](https://hpc-wiki.info/hpc/Binding/Pinning#Options_for_Binding_in_Intel_MPI).

**Conclusion:**
Switching to the Intel MPI runtime should resolve the issue with the long command line error.

---

**Note:** This report is intended for internal use by HPC support employees to assist in resolving similar issues in the future.
---

### 2024092342002673_Using%20a100multi.md
# Ticket 2024092342002673

 # HPC Support Ticket Conversation Summary

## Subject
Using a100multi

## User Issue
- User requested access to multiple nodes for scaling tests with Quantum ESPRESSO and LAMMPS.
- Initial tests were successful over 8 GPUs.
- User wanted to test on multiple nodes.

## HPC Admin Responses
- HPC Admins noted that multi-node jobs can lead to significant GPU time loss due to waiting for nodes to become available simultaneously.
- User's previous jobs were too short, leading to inefficient resource utilization.
- HPC Admins suggested reserving nodes for benchmarking to avoid idle time.
- A reservation for 4 nodes for 24 hours was placed but not utilized by the user.
- Discussion on the impact of reservations on project allocations and the need for efficient resource usage.

## Key Points Learned
- **Multi-Node Job Concerns**: Multi-node jobs can result in significant idle time, especially for short jobs.
- **Reservation for Benchmarking**: Reserving nodes can help run multiple benchmarks in quick succession without waiting for nodes to become available.
- **Efficient Resource Utilization**: Short jobs can lead to inefficient use of resources, impacting overall project allocations.
- **User Responsibility**: Users should be aware of the impact of their job requests on resource allocation and utilization.

## Root Cause of the Problem
- User's jobs were too short, leading to inefficient resource utilization.
- Lack of understanding about the impact of reservations on project allocations.

## Solution
- **Pre-Reservation Testing**: Suggested comparing performance on two GPUs within the same node versus two GPUs on different nodes to determine the need for full multi-node testing.
- **Efficient Job Scheduling**: Encouraged running longer jobs to minimize idle time and improve resource utilization.
- **User Education**: Informed the user about the impact of reservations and the importance of efficient resource usage.

## Conclusion
- The user was informed about the importance of efficient resource utilization and the impact of reservations.
- Future benchmarking should consider the duration of jobs to minimize idle time and improve overall resource usage.
- Users should be aware of the potential impact of their job requests on project allocations and resource availability.
---

### 2024010242000942_low%20CPU%20loads%20-%20VASP%20NEB%20-%20b146dc14.md
# Ticket 2024010242000942

 # HPC Support Ticket: Low CPU Loads - VASP NEB

## Keywords
- Low CPU utilization
- VASP
- NEB (Nudged Elastic Band)
- Slurm script
- Parallelization settings (NCORE)
- MPI processes
- INCAR file

## Summary
A user submitted multiple VASP NEB jobs that were underutilizing CPU resources. Each job was allocated 8 nodes but only utilized 2 nodes, leaving the remaining 6 nodes idle.

## Root Cause
- Incorrect parallelization setting (NCORE) in VASP's input file.
- Slurm script configured to start only 208 MPI processes, utilizing only the first two nodes.

## Solution
- Correct the parallelization settings in VASP's input file to ensure all allocated nodes are utilized.
- Ensure the Slurm script is configured to start the correct number of MPI processes to utilize all allocated nodes.
- Relax the end points individually before running the NEB job to ensure only the images are relaxed, not the end points.

## Lessons Learned
- Always verify the parallelization settings in the application's input file.
- Ensure the job scheduler script (Slurm in this case) is configured correctly to utilize all allocated resources.
- For NEB calculations in VASP, relax the end points individually before running the NEB job.
- The number of MPI processes should match the number of tasks specified in the Slurm script.

## Follow-up
- The ticket was closed after the user acknowledged the issue and planned to correct it in future runs.
- The HPC Admin offered to assist further if access to the input file (INCAR) was provided.
---

### 2019121142000638_OpenPose-Jobs%20auf%20Meggie%20-%20sles000h.md
# Ticket 2019121142000638

 # HPC Support Ticket: OpenPose Jobs on Meggie

## Keywords
- OpenPose
- Meggie
- Singularity
- Job Script
- Memory Usage
- OOM (Out of Memory)
- numactl
- TinyGPU

## Summary
The user was running OpenPose jobs on the Meggie cluster, and the HPC Admin noticed that some jobs were behaving strangely, particularly in terms of memory usage and performance.

## Root Cause
- **Memory Issues**: OpenPose with hand detection requires more memory, leading to OOM (Out of Memory) errors.
- **Incorrect Job Script**: The user was running a job script intended for TinyGPU on the Meggie cluster, causing inefficiencies and unusual behavior.

## Details
- The HPC Admin observed two classes of jobs running on Meggie, one with a conditional check for `/scratchssd` and another using `numactl` to distribute tasks across CPU cores.
- The job script intended for TinyGPU was not suitable for Meggie, leading to performance issues.

## Solution
- The user acknowledged the issue and stopped submitting new jobs with the incorrect script.
- The user cleared the queue and resubmitted jobs with the correct script, ensuring compatibility with the Meggie cluster.

## Lessons Learned
- Ensure that job scripts are tailored to the specific cluster they are running on.
- Monitor memory usage for jobs that require significant resources.
- Regularly review job performance metrics to identify and address anomalies.

## Actions Taken
- The HPC Admin alerted the user about the unusual job behavior and provided details on the differences in job scripts.
- The user corrected the job script and resubmitted jobs accordingly.

## Recommendations
- Users should verify that their job scripts are optimized for the specific cluster environment.
- HPC Admins should continue to monitor job performance and provide feedback to users as needed.

## Follow-Up
- Monitor the performance of the resubmitted jobs to ensure they are running correctly.
- Provide additional guidance or resources to users if similar issues arise in the future.
---

### 2023070442003311_Job%20on%20Fritz%20with%20too%20high%20CPU%20load%20-%20gwgi019h.md
# Ticket 2023070442003311

 # HPC Support Ticket: Job on Fritz with Too High CPU Load

## Keywords
- Fritz cluster
- Job script
- OpenMP
- Monitoring system
- CPU load
- ntasks-per-node

## Problem Description
- **Root Cause**: User's job script was not updated to match the hardware specifications of the Fritz cluster, specifically the number of cores per node.
- **Symptoms**: High CPU load on Fritz cluster.

## Solution
- **Action Taken**: HPC Admin notified the user about the issue and provided links to the monitoring system and relevant documentation.
- **User Response**: The user acknowledged the issue and mentioned that the job script was not updated for Fritz's number of cores per node.
- **Resolution**: The user was advised to update the job script, specifically the `ntasks-per-node` parameter, to an appropriate value for the Fritz cluster (72 cores per node).

## General Learnings
- Always ensure job scripts are updated to match the hardware specifications of the cluster being used.
- Utilize the monitoring system to diagnose job-related issues.
- Refer to cluster-specific documentation for accurate hardware information.

## Relevant Links
- [Monitoring System](https://monitoring.nhr.fau.de/monitoring/job/4615154)
- [Accessing Monitoring System FAQ](https://hpc.fau.de/faq/how-can-i-access-a-link-to-monitoring-nhr-fau-de)
- [Fritz Cluster Documentation](https://hpc.fau.de/systems-services/documentation-instructions/clusters/fritz-cluster/)

## Ticket Status
- The ticket was closed as the error did not recur.
---

### 42321978_Non%20realiatic%20performance%20difference%20between%20openmpi%20and%20intelmpi.md
# Ticket 42321978

 # HPC Support Ticket: Non-Realistic Performance Difference between OpenMPI and IntelMPI

## Keywords
- OpenMPI
- IntelMPI
- VASP
- Performance Issues
- OpenFabrics Subsystem
- Lockable Memory
- Reboot

## Problem Description
- User encountered performance issues with VASP (gamma only, 5.3.5) compiled using OpenMPI.
- OpenMPI runs were significantly slower and exhibited erratic performance compared to IntelMPI.
- Warning message indicated OpenFabrics subsystem was configured to allow only partial physical memory registration.

## Root Cause
- The OpenFabrics subsystem configuration limited the amount of lockable memory, causing MPI jobs to run with erratic performance, hang, and/or crash.

## Solution
- HPC Admins implemented a change in system services to allow unlimited lockable memory.
- The change will become effective after the compute nodes reboot.
- The reboot schedule was not immediately available, but the user was informed that the fix would be applied during the next downtime.

## Additional Notes
- The user observed similar warnings on another cluster (LiMa) but did not experience significant performance differences in previous tests.
- The user was advised that LiMa would also receive the fix after the next downtime.

## Lessons Learned
- Configuration of the OpenFabrics subsystem can significantly impact the performance of MPI jobs.
- Ensuring unlimited lockable memory can resolve performance issues related to OpenMPI.
- Changes to system services may require a reboot to take effect, and users should be informed about the reboot schedule.

## Next Steps
- Monitor the performance of OpenMPI jobs after the reboot.
- Ensure that all affected clusters receive the necessary configuration changes during the next downtime.
---

### 2023060142000491_VASP%20users%3A%20hybrid%20MPI_OpenMP.md
# Ticket 2023060142000491

 ```markdown
# HPC-Support Ticket: VASP Users - Hybrid MPI/OpenMP

## Keywords
- VASP
- Hybrid MPI/OpenMP
- Parallelization
- Optimization
- OMP_STACKSIZE
- HSE calculations

## Summary
- **Issue**: Users from a specific research group are using their own VASP binaries, potentially missing out on optimized parallelization and performance.
- **Root Cause**: Custom VASP binaries may not be configured for optimal hybrid MPI/OpenMP parallelization.
- **Solution**:
  - Encourage users to build VASP in hybrid mode with MPI+OpenMP.
  - For HSE calculations with many OMP threads, increase the OMP stack size to prevent crashes:
    ```bash
    export OMP_STACKSIZE=500m
    ```

## Action Taken
- HPC Admin contacted the 2nd Level Support team to assist users in building VASP with hybrid MPI/OpenMP.
- Ticket closed due to lack of user response.

## General Learnings
- Custom binaries may not leverage the best parallelization and optimization strategies.
- Hybrid MPI/OpenMP can improve performance for certain workloads.
- Increasing OMP_STACKSIZE can prevent crashes in memory-intensive calculations.
```
---

### 2024112242002009_Likwid-mpirun%20on%20fritz%20for%20nested%20MPI%20applications.md
# Ticket 2024112242002009

 # HPC-Support Ticket: Likwid-mpirun on Fritz for Nested MPI Applications

## Subject
Using likwid-mpirun on Fritz for nested MPI applications.

## User Details
- User has a Python program that launches multiple MPI processes (using mpi4py) across multiple Fritz nodes, pinned to each socket.
- Each MPI process launches a binary that is MPI parallel.
- User aims to pin the MPI processes at the binary level to cores within the respective socket.

## Issue
- User tried using srun at the Python level and likwid-mpirun at the binary level but couldn't enforce pinning for MPI processes in the Python script using srun (pinning to sockets).
- Using likwid-mpirun at both the Python and binary levels caused the job to stall without any output.
- I_MPI_PIN_DOMAIN variable was set by SLURM, causing issues with pinning in batch mode.

## Solution
- Remove `--cpus-per-task` from the SBATCH parameters to avoid SLURM setting I_MPI_PIN_DOMAIN.
- Manually supply the hostname and CPU ID list to the mpirun calls for the binary.

## Keywords
- likwid-mpirun
- nested MPI applications
- pinning MPI processes
- SLURM
- I_MPI_PIN_DOMAIN
- mpi4py
- batch processing

## Lessons Learned
- SLURM sets I_MPI_PIN_DOMAIN based on `--cpus-per-task`, which can interfere with pinning in nested MPI applications.
- Manual specification of hostnames and CPU IDs can be used to work around pinning issues.
- Chain jobs or array jobs can be used to restructure the workflow and avoid nested MPI calls.

## Additional Notes
- User was advised to look into chain jobs and restructure the pipeline to avoid nested MPI calls.
- A video call was held to discuss the issue and potential solutions.

## References
- [Documentation on array jobs or chain jobs with or without dependencies among the jobs](https://doc.nhr.fau.de/batch-processing/advanced-topics-slurm)
---

### 42254372_Nutzung%20Windows-Cluster.md
# Ticket 42254372

 # HPC Support Ticket: Usage of Windows Cluster

## Keywords
- Windows Cluster
- Job Scheduling
- TestNode
- TestQueue
- Resource Allocation

## Problem
A user reported that a single user had started a large number of jobs, completely utilizing the Windows Cluster for an extended period. This made it difficult for the user to run test jobs for their project.

## Root Cause
- Overutilization of cluster resources by a single user.
- Lack of awareness about dedicated test resources.

## Solution
- The HPC Admin informed the user about the existence of a TestNode and TestQueue specifically designed for short-term testing.
- The TestNode and TestQueue have a maximum job runtime of one hour, ensuring that all users can test their jobs promptly.

## What Can Be Learned
- Users should be made aware of dedicated test resources to avoid overloading the main cluster.
- Proper resource allocation and job scheduling are crucial for efficient cluster usage.
- Communication about available resources and their intended use can help prevent resource conflicts.

## Actions Taken
- The user was informed about the TestNode and TestQueue.
- The user confirmed they would use the TestNode for their initial tests.

## Status
- The issue was resolved, and the user was able to proceed with their work.

---

This documentation can be used to address similar issues in the future by informing users about dedicated test resources and ensuring proper resource allocation.
---

### 2024071042001559_Fehlermeldung%20Woody-srun.md
# Ticket 2024071042001559

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject: Fehlermeldung Woody-srun

### Keywords:
- LAMMPS
- srun
- mpirun
- Fehlermeldung
- I_MPI_FABRICS
- Woody-Cluster
- Shared-Memory
- Mellanox-Ethernet-Karte

### Summary:
A user encountered an error when starting LAMMPS via `srun` on the Woody-Cluster. The error message was "w2302:rank1.lmp: Failed to modify UD QP to INIT on mlx5_0: Operation not permitted". The user was able to run the application using `mpirun` with 4 CPUs, suggesting the issue was not with the LAMMPS input file.

### Root Cause:
The error was due to the Mellanox Ethernet card (mlx5_0) not being properly configured for single-node jobs. The Intel MPI library was trying to use the Ethernet card instead of shared memory.

### Solution:
Setting the environment variable `I_MPI_FABRICS=shm` resolved the issue. This forces the Intel MPI library to use shared memory instead of the Ethernet card. The intel-mpi module on Woody now automatically sets this variable.

### Lessons Learned:
1. **Environment Variables**: Setting specific environment variables can resolve issues related to MPI communication.
2. **Shared Memory vs. Ethernet**: For single-node jobs, shared memory should be used instead of Ethernet for better performance and to avoid permission issues.
3. **Testing with mpirun**: Running jobs with `mpirun` can help diagnose issues that may not be apparent when using `srun`.
4. **Automatic Configuration**: Ensuring that modules automatically set necessary environment variables can prevent common user errors.

### Additional Information:
- **Cluster**: Woody
- **Account**: iwc2100h
- **Job ID**: 4902497
- **MPI Library**: Intel MPI Library, Version 2021.7

### Conclusion:
The issue was resolved by setting the `I_MPI_FABRICS=shm` environment variable, which is now automatically set by the intel-mpi module on Woody. This ensures that single-node jobs use shared memory instead of the Mellanox Ethernet card.
```
---

### 2022061442001137_Re%3A%20%5BRRZE-HPC%5D%20HPC%20Cafe%20today%3A%20New%20clusters%20and%20compute%20time%20application.md
# Ticket 2022061442001137

 ```markdown
# HPC Support Ticket Conversation Summary

## Subject: Re: [RRZE-HPC] HPC Cafe today: New clusters and compute time application process

### Key Points Learned:

1. **HPC Cafe and Intro Sessions**:
   - The HPC Cafe and intro sessions provide additional support and training for HPC users.
   - The HPC Cafe on June 14, 2022, focused on new clusters and compute time application processes.

2. **Cluster and Job Management**:
   - Users can submit jobs to the HPC cluster using SLURM.
   - The `sbatch` command is used to submit batch scripts.
   - The `srun` command is used to run interactive jobs or within batch scripts.

3. **MPI and Python**:
   - MPI jobs can be run using `srun python` or `srun python3`.
   - The `mpi4py` package needs to be installed correctly to avoid module not found errors.
   - Ensure the correct MPI compiler wrapper is set before installing `mpi4py`.

4. **R and Bioconductor**:
   - R version 4.0.2 is available on the cluster.
   - Bioconductor requires specific R versions; version 3.15 requires R 4.2.
   - Users can install packages in a personal library if the system library is not writable.

5. **Support and Sprechstunde**:
   - The HPC support team offers Sprechstunde (office hours) for personalized support.
   - Users can schedule Zoom meetings for detailed assistance.

### Common Issues and Solutions:

1. **MPI Job Submission**:
   - Ensure the batch script includes the correct module load commands.
   - Use `srun python` or `srun python3` to run MPI jobs.

2. **mpi4py Installation**:
   - Install `mpi4py` using the correct MPI compiler wrapper:
     ```bash
     MPICC=$(which mpicc) pip install --no-cache-dir mpi4py
     ```
   - Ensure no conflicting MPI installations are present in the environment.

3. **R and Bioconductor**:
   - Install Bioconductor packages in a personal library if the system library is not writable:
     ```R
     install.packages("BiocManager", lib = "~/R/x86_64-pc-linux-gnu-library/4.0")
     BiocManager::install(version = "3.12")
     ```
   - Ensure the correct R version is used for specific Bioconductor versions.

4. **Job Output**:
   - Ensure the batch script correctly specifies output and error files:
     ```bash
     #SBATCH --output=output.txt
     #SBATCH --error=error.txt
     ```
   - Check the `$SLURM_SUBMIT_DIR` for job output files.

### Conclusion:
The conversation highlights the importance of correctly setting up job scripts, managing dependencies, and utilizing support resources. The HPC support team provides comprehensive assistance through various channels, including intro sessions, Sprechstunde, and personalized Zoom meetings.
```
---

### 2024071242001448_Woody-Probleme%20bei%20CPU%20Erh%C3%83%C2%B6hung.md
# Ticket 2024071242001448

 ```markdown
# HPC-Support Ticket: Woody-Probleme bei CPU Erhöhung

## Problem Description
User encountered issues with LAMMPS simulations on the Woody cluster when using more than 4 CPUs. Simulations were timing out and not completing within the expected timeframe. The output file indicated that the simulation halted during the creation of the neighborhood list ("Finding 1-2 1-3 1-4 neighbors ...").

## Keywords
- LAMMPS
- Woody Cluster
- CPU Scaling
- Timeout
- Neighborhood List
- SLURM
- MPI Process Pinning

## Ticket Details
- **Account:** iwc2100h
- **Job IDs:** 4CPU: 4912760; 6CPU: 4912767

## Root Cause
The issue was traced to the use of the `balance` function in LAMMPS, which affects the distribution of the simulation space across CPUs. This function was found to be incompatible with certain combinations of Intel CPUs and LAMMPS.

## Solution
The user removed the `balance` function from the LAMMPS input script, which resolved the issue.

## Additional Recommendations
- Avoid using `--output` and `--error` options in SLURM submit scripts. SLURM automatically names outputs and adds the JobID, making it easier to locate outputs and preventing accidental overwrites.
- For better performance, pin MPI processes using `srun --cpu-bind=cores`.

## Conclusion
The problem was not related to the server but rather to a specific function in LAMMPS. Removing the `balance` function allowed the simulations to run successfully with more than 4 CPUs.
```
---

### 2025010942000937_Tier3-Access-Fritz%20%22Christoph%20Heigl%22%20_%20iwst109h.md
# Ticket 2025010942000937

 # HPC Support Ticket Analysis

## Keywords
- **Access Grant**: Fritz
- **Software**: Star-CCM+, Python with MPI
- **Resources**: Single-node throughput, Multi-node workload
- **Application**: Fluid-structure-acoustic-interaction simulations
- **Expected Outcomes**: Improved understanding of acoustic back-coupling
- **Licence Keys**: Change for Star-CCM+

## Summary
- **Access Granted**: User was granted access to Fritz.
- **Software Licence Change**: Notification about a change in licence keys for Star-CCM+.
- **Resource Requirements**:
  - Single-node throughput (72 cores, 250 GB)
  - Multi-node workload (HDR100 Infiniband with 1:4 blocking; per node: 72 cores, 250 GB)
- **Compute Time**: 20,000 node hours on Fritz.
- **Software Needs**: Star-CCM+, Python with MPI.
- **Application**: Fluid-structure-acoustic-interaction simulations for human phonation process.
- **Expected Results**: Improved understanding of acoustic back-coupling, comparison with measurement data, potential application in voice therapy.

## Root Cause of the Problem
- **Licence Key Change**: Potential issues with Star-CCM+ due to licence key change.

## Solution
- **Notification**: Users were informed to report any issues related to the licence key change for Star-CCM+.

## General Learnings
- **Access Management**: Proper communication and notification about access grants and software changes.
- **Resource Allocation**: Understanding and documenting specific resource requirements for complex simulations.
- **Software Maintenance**: Importance of informing users about changes in software licences to preemptively address potential issues.

## Next Steps
- **Monitoring**: Keep an eye on any reported issues related to Star-CCM+ licence keys.
- **Support**: Provide prompt assistance if users encounter problems due to the licence key change.
---

### 2023042842002282_Using%20VASP-6%20in%20hybrid%20mode%3A%20MPI%2BOpenMP%20-%20bctc027h.md
# Ticket 2023042842002282

 # HPC Support Ticket: Using VASP-6 in Hybrid Mode (MPI+OpenMP)

## Keywords
- VASP-6
- Hybrid Mode
- MPI+OpenMP
- Performance
- Resource Utilization
- Binary Compilation
- VASP Users List

## Problem
- User's VASP-6 job (jobID=555350) did not utilize resources efficiently.
- Low workload observed, indicating potential issues with OpenMP parallelization.

## Root Cause
- Possible issues with the VASP binary not being compiled with OpenMP.
- The type of calculations performed might not be OpenMP parallelized.

## Solution
- Rebuild the VASP binary with OpenMP compiler options enabled.
- Alternatively, use the pre-installed VASP module on the system (`vasp6/6.3.2-hybrid-intel-impi-AVX512`).
- Ensure the user is added to the list of VASP users on the system by the HPC Admin.

## Additional Information
- Documentation on VASP-6 performance with MPI+OpenMP can be found at: [VASP Documentation](https://hpc.fau.de/systems-services/documentation-instructions/special-applications-and-tips-tricks/vasp)

## Contact
- For further assistance, contact the HPC Support Team at [support-hpc@fau.de](mailto:support-hpc@fau.de).

---

This report provides a concise overview of the issue, root cause, and solution for using VASP-6 in hybrid mode (MPI+OpenMP) on the HPC system. It can be used as a reference for support employees to address similar issues in the future.
---

### 2022111042000841_Optimizing%20ASCII%20processing%20jobs%20%5Bb127dc10%5D.md
# Ticket 2022111042000841

 # HPC Support Ticket: Optimizing ASCII Processing Jobs

## Keywords
- ASCII data processing
- Optimization
- OpenMP
- Environment variables
- OMP_PROC_BIND
- OMP_PLACES

## Summary
The user was processing several GB of ASCII data in their `bash_Onsager*` jobs. The HPC Admin identified potential optimization opportunities and provided recommendations to improve performance.

## Root Cause
- The user's jobs were processing large amounts of ASCII data, which could potentially be optimized.

## Solution
- The HPC Admin recommended setting the environment variables `OMP_PROC_BIND` and `OMP_PLACES` to pin each OpenMP thread to a separate core, reducing execution time by preventing the OS from arbitrarily migrating threads.

```bash
export OMP_PROC_BIND=close
export OMP_PLACES=cores
```

## Steps Taken
1. **Initial Contact**: The HPC Admin contacted the user regarding potential optimizations for their ASCII data processing jobs.
2. **Data Access**: The user provided the path to the job data directory.
3. **Additional Files**: The user provided additional `box*.txt` files required for the job.
4. **Benchmarking**: The HPC Admin performed benchmarks on the ASCII processing steps.
5. **Recommendations**: The HPC Admin recommended setting specific environment variables to optimize OpenMP thread binding.

## Conclusion
The user was advised to implement the recommended environment variable settings to potentially reduce execution time for their ASCII data processing jobs.

## Follow-up
The user acknowledged the recommendations and planned to include them in their script.

---

This report provides a concise summary of the support ticket, including the root cause, solution, steps taken, and follow-up actions. It can serve as a reference for future optimization requests related to ASCII data processing jobs.
---

### 2021080542000948_Jobs%20auf%20emmy%20%7C%20cusc001h.md
# Ticket 2021080542000948

 ```markdown
# HPC Support Ticket: Jobs auf emmy | cusc001h

## Keywords
- Job efficiency
- MPI processes
- Node utilization
- mpirun options
- `-npernode`

## Problem
- Jobs on emmy were only utilizing half of the requested nodes.

## Root Cause
- MPI processes were not evenly distributed across the nodes.

## Solution
- Use the `-npernode 20` option with `mpirun` to distribute MPI processes evenly across the nodes.

## Example
```
mpirun -npernode 20 ...
```

## Outcome
- The user implemented the suggested change, and the issue was resolved.

## Notes
- No response from the user, but the change was observed in subsequent jobs.
```
---

### 2020112242000456_Fehlermeldung%20bei%20Zugriff%20auf%20MPI.md
# Ticket 2020112242000456

 # HPC Support Ticket Analysis: Fehlermeldung bei Zugriff auf MPI

## Keywords
- MPI
- Elmer/Ice
- Batch Job
- Slurm
- Account
- Partition
- Login-Knoten
- Interactive Job

## Problem
- User cannot execute MPI binary "ElmerSolver" on login nodes.
- User receives error message when submitting batch jobs with `sbatch`.

## Root Cause
- MPI binaries cannot be run directly on login nodes.
- User's HPC account was not activated on the specific cluster (Meggie).

## Solution
- Use interactive jobs with Slurm for testing MPI binaries.
- Ensure the HPC account is activated on the specific cluster.
- Define the correct account and partition in the batch script if required.

## General Learnings
- MPI binaries should be tested using interactive jobs with Slurm.
- Ensure HPC accounts are activated on the relevant clusters.
- Proper account and partition definitions are necessary for successful job submissions.

## References
- [Interactive Jobs with Slurm](https://www.anleitungen.rrze.fau.de/hpc/batch-processing/#slurm)

## Additional Notes
- If issues persist, consult with colleagues who have successfully run similar tests.
- Ensure proper communication with users to understand their specific needs and issues.
---

### 2023051542001046_Fwd%3A%20CPU%20pinning.md
# Ticket 2023051542001046

 # HPC Support Ticket: CPU Pinning

## Keywords
- CPU pinning
- OpenMP
- MPI
- NUMA domains
- Performance monitoring
- `top` command
- `likwid-topology`
- Load imbalance
- Memory bound
- First-touch policy

## Summary
- **User Issue**: User experiencing performance drops and load imbalance with CPU pinning.
- **Root Cause**: Incorrect pinning leading to load imbalance across NUMA domains.
- **Solution**: Use `OMP_PLACES` and `OMP_PROC_BIND` for proper pinning. Ensure balanced load across NUMA domains.

## Detailed Conversation

### Initial Problem
- User reported issues with CPU pinning using `CPU_SET`.
- Threads were pinned but not to the correct cores.
- Performance drops observed after pinning.

### Diagnostic Steps
- **HPC Admin**: Suggested using `top` command to check pinning.
- **HPC Admin**: Recommended using `likwid-topology` for node architecture.
- **HPC Admin**: Identified potential load imbalance due to uneven thread distribution across NUMA domains.

### Recommendations
- **HPC Admin**: Suggested using `OMP_PLACES` and `OMP_PROC_BIND` for better pinning.
- **HPC Admin**: Advised running a job with 16 threads to compare performance across one vs. two NUMA domains.

### Further Investigation
- **HPC Admin**: Suggested a Zoom call for detailed discussion.
- **HPC Admin**: Provided example configuration for pinning MPI processes and OpenMP threads.

### Outcome
- **HPC Admin**: Fixed pinning issues during a virtual call.
- **HPC Admin**: Identified that the code is memory bound, and moving from 32 to 64 cores did not improve performance.
- **HPC Admin**: Observed 70% efficiency when moving from 1 to 4 NUMA domains.
- **HPC Admin**: Suggested continuing with 1 MPI process per node for faster runs.

## Conclusion
- Proper pinning using `OMP_PLACES` and `OMP_PROC_BIND` resolved load imbalance issues.
- Memory-bound nature of the code limits performance improvement with additional cores.
- Efficiency of 70% is acceptable for the given workload.
- Recommended continuing with 1 MPI process per node for optimal performance.
---

### 2024040542002868_H%C3%83%C2%B6here%20Prio%20f%C3%83%C2%BCr%20Revision.md
# Ticket 2024040542002868

 ```markdown
# HPC Support Ticket: Higher Priority for Revision

## Keywords
- Priority Increase
- Revision
- Time-Critical
- Resource Allocation
- HPC Admin
- FAU
- NHR@FAU

## Summary
A user requested a higher priority for their jobs on specific HPC resources due to time-critical revision work.

## Root Cause
- User requires higher priority for time-critical revision work.
- Current resource utilization is moderate, suggesting no immediate need for manual intervention.

## Solution
- The decision to increase priority lies with the HPC admin.
- Current resource utilization does not necessitate manual intervention.

## Lessons Learned
- Users may request priority increases for time-sensitive tasks.
- Resource utilization should be assessed before making priority adjustments.
- Final decision on priority changes rests with the HPC admin.
```
---

### 2025011642003091_Tier3-Access-Fritz%20%22Fabian%20Teichmann%22%20_%20iwgt002h.md
# Ticket 2025011642003091

 ```markdown
# HPC Support Ticket: Tier3-Access-Fritz

## Keywords
- Single-node throughput
- Special justification
- Python deepxde
- Multifidelity Neural Network (MFNN)
- Material prediction
- Hyperparameters
- Node hours
- Account activation

## Summary
A user requested access to the HPC system "Fritz" for a project involving training a Multifidelity Neural Network (MFNN) to predict mechanical properties of aluminum. The request included specific resource requirements and expected outcomes.

## User Request
- **Contact:** User's email and account ID
- **Resource Requirement:** Single-node throughput (72 cores, 250 GB)
- **Compute Time:** 1000 node hours on Fritz
- **Software:** Python deepxde
- **Application:** Training MFNN for material prediction
- **Expected Results:** Tuned hyperparameters and optimized model for a journal paper and proposal

## HPC Admin Response
- **Action:** The request was initially deferred.
- **Resolution:** The user's account was later activated to use the Fritz system.

## Root Cause
The user needed access to specific HPC resources for a computational project.

## Solution
The HPC Admin activated the user's account to allow access to the requested resources.

## General Learnings
- Users may require special justification for high resource demands.
- Activation of user accounts for specific HPC systems may involve a review process.
- Communication with users should include confirmation of account activation and access to requested resources.
```
---

### 2021061042002654_Issue%20on%20job%20failures%20using%20lammps%20with%20gpu%20and%20openmpi.md
# Ticket 2021061042002654

 # HPC Support Ticket: Issue on Job Failures Using LAMMPS with GPU and OpenMPI

## Keywords
- LAMMPS
- GPU (K20m1x)
- OpenMPI
- Job failures
- Walltime exceeded
- Infiniband ports
- Subnet GID prefix
- Cuda driver error
- mpirun arguments

## Problem Description
- Job finishes before the requested walltime but gets stuck until it exceeds the walltime.
- Warning about multiple active Infiniband ports with the same subnet GID prefix.
- Cuda driver error messages in the error file.
- Incorrect `mpirun` usage for OpenMPI compiled LAMMPS.

## Root Cause
- Incorrect `mpirun` command used for OpenMPI compiled LAMMPS.
- Multiple Infiniband ports with the same subnet GID prefix causing warnings.
- Potential Cuda driver errors affecting job execution.

## Solution
- Use `mpirun` from OpenMPI for applications compiled with OpenMPI.
- Suppress the Infiniband warning using the `--mca btl_openib_warn_default_gid_prefix 0` argument with `mpirun`.
- Investigate and resolve Cuda driver errors for stable job execution.

## Lessons Learned
- Ensure the correct `mpirun` command is used based on the MPI library the application is compiled with.
- Understand and manage Infiniband port configurations to avoid warnings.
- Address Cuda driver errors to prevent job failures.

## Additional Notes
- The accel nodes in Emmy have two Infiniband ports connected to the same IB network, which is correct.
- The job was aborted by the PBS Server due to exceeding the walltime limit.
- The user's LAMMPS package was compiled using OpenMPI, requiring the use of OpenMPI's `mpirun`.
---

### 2023060942002001_SLURM%20verwendet%2064%20Threads%20bei%20--cpus-per-task%3D2.md
# Ticket 2023060942002001

 # HPC Support Ticket: SLURM Thread Allocation Issue

## Keywords
- SLURM
- Thread allocation
- CPU binding
- SMT (Simultaneous Multithreading)
- Physical cores
- Logical cores
- `--cpus-per-task`
- `--cpu-bind`
- `--threads-per-core`
- `--hint=nomultithread`

## Problem Description
The user noticed that when starting a task with `--cpus-per-task=2`, SLURM allocates all CPU cores instead of the specified number. For other values, such as `--cpus-per-task=4`, the correct number of threads is allocated. The user wants to ensure that threads are distributed across physical cores rather than logical cores.

## Root Cause
The issue seems to be related to SLURM's handling of SMT (Simultaneous Multithreading) and the default behavior of CPU binding. The user wants to disable SMT effectively, ensuring one thread per physical core.

## Solution Attempts
1. **Using `--cpu-bind=verbose,cores`**:
   ```bash
   srun --ntasks=1 --cpus-per-task=2 --cpu-bind=verbose,cores <cmd>
   ```
   This option binds threads to physical cores but does not disable SMT.

2. **Using `--threads-per-core`**:
   The user encountered an error: "Cannot request more threads per core than the job allocation."

3. **Using `--hint=nomultithread`**:
   This option did not work as expected.

## HPC Admin Response
- The HPC Admin confirmed that the issue might be related to the SLURM version or configuration.
- The SLURM configuration file (`slurm.conf`) was checked and found to be correct.
- Similar issues have been reported on the SLURM mailing list, suggesting it might be a version-specific problem.

## Conclusion
The issue could not be resolved with the current SLURM version and configuration. The HPC Admin suggested that it might be a bug or limitation in the SLURM version used on the test cluster. Further investigation or updates to SLURM might be necessary to resolve the issue.

## Recommendations
- Check for updates or patches to SLURM that might address the issue.
- Consider testing on other clusters with different SLURM versions to see if the problem persists.
- Document the issue for future reference and to help other users experiencing similar problems.
---

### 2020091442001564_OpenMP%20_Fortran.md
# Ticket 2020091442001564

 # HPC-Support Ticket: OpenMP / Fortran

## Summary
User is developing a program for simulating large crystal structures and has implemented OpenMP to speed up processing. However, the OpenMP implementation is not scaling as expected compared to the serial code.

## Problem Description
- The serial code performs a 3D Fourier transform for each atom in a crystal structure.
- The Fourier space is a regular grid, allowing for simple addition of the complex exponential function's argument.
- Initial OpenMP implementation is slow due to all threads writing to the same large array.
- Rewriting the code to loop over the Fourier space first and then over atoms improves scaling but requires more multiplications.

## Root Cause
- Inefficient memory access patterns and thread contention when writing to the same array.
- Suboptimal loop structure leading to increased computational overhead.

## Solution
- Optimize memory access by reducing the size of the temporary array.
- Rearrange loops to minimize thread contention and computational overhead.
- Use appropriate compiler flags and optimizations to improve performance.

## Keywords
- OpenMP
- Fortran
- Fourier Transform
- Parallelization
- Memory Access
- Loop Optimization
- Compiler Flags

## General Learnings
- Proper memory access patterns are crucial for efficient parallelization.
- Loop restructuring can significantly impact performance in parallel codes.
- Compiler flags and optimizations can greatly influence the performance of Fortran codes.
- Benchmarking and profiling are essential for identifying performance bottlenecks.

## Ticket Conversation
### User
- Describes the issue with OpenMP scaling and provides details about the serial code and initial OpenMP implementation.
- Shares different versions of the code and their performance.
- Mentions a typo in the main program affecting reported runtimes.

### HPC Admin
- Offers to review the code and provides initial feedback.
- Compiles the code with different compilers and flags, noting performance differences.
- Suggests improvements to the error routine and time measurement.
- Provides a benchmark of the OpenMP routines with Intel and Gfortran compilers.
- Notes a correction in the benchmark results.
- Offers well wishes for the user's recovery.

### User
- Thanks the HPC Admin for their help and mentions a temporary absence due to medical reasons.
- Acknowledges the need for code improvements and plans to address them.

### HPC Admin
- Expresses good wishes for the user's recovery.

## Conclusion
The user's OpenMP implementation was improved through code optimization and proper use of compiler flags. The HPC Admin provided valuable feedback and benchmarks to help the user achieve better performance. The ticket was closed with the user planning to make further improvements to the code.
---

### 2024031542002207_I_MPI%20env%20vars%20pinning%20not%20working%20as%20expected.md
# Ticket 2024031542002207

 # HPC Support Ticket: I_MPI env vars pinning not working as expected

## Keywords
- IntelMPI
- Pinning
- Hybrid OpenMP+MPI
- NUMA domain
- Infiniband Controller
- Slurm
- Environment variables

## Problem Description
The user is experiencing issues with pinning hybrid OpenMP+MPI applications on the `spr1tb` partition using IntelMPI. The goal is to pin 1 MPI process per ccNuma domain compactly, filling up the first socket with 4 MPI processes. However, when running `mpirun -n 4 <executable>`, 3 MPI processes are pinned to the first socket, and the fourth process is pinned to the second socket. This behavior is not observed on Icelake nodes.

## Environment Variables Used
```bash
export I_MPI_PIN=1
export I_MPI_PIN_PROCESSOR_LIST="allcores"
export I_MPI_PIN_DOMAIN="13:compact"
export OMP_NUM_THREADS=13
export OMP_PLACES=cores
export OMP_PROC_BIND=close
```

## Root Cause
By default, the first MPI process is placed in the NUMA domain where the Infiniband Controller is located. On the SPR nodes, this is on the second socket, leading to the observed behavior. On ICX nodes, the Infiniband controller is on the first socket, resulting in different behavior.

## Solution
To prevent the default behavior, set the environment variable `I_MPI_PIN_RESPECT_HCA=0`. Alternatively, let Slurm handle the pinning.

## Additional Notes
- The issue is specific to the `spr1tb` partition and does not occur on Icelake nodes due to the different placement of the Infiniband controller.
- Adjusting the pinning behavior can be achieved through environment variables or by utilizing Slurm's pinning capabilities.
---

### 2020090442001029_Simulations.md
# Ticket 2020090442001029

 # HPC Support Ticket Conversation: Simulations

## Keywords
- High-pressure calculations
- Priority boost
- Additional resources
- Job optimization
- Gromacs version

## Summary
A research group was struggling to complete demanding calculations for an upcoming evaluation. The HPC support team provided assistance by increasing the priority of their accounts and enabling access to additional resources.

## Problem
- The research group needed to complete demanding calculations for an important proof of principle.
- The calculations were progressing slowly, and the group was at risk of not meeting the deadline.

## Solution
- The HPC support team increased the priority of the group's accounts on Emmy for 10 days.
- The team enabled the group's accounts on Meggie, providing additional resources.
- The team suggested using less busy nodes on Emmy with Tesla V100 GPUs.
- The team offered to copy job files to find additional tuning parameters.
- The team inquired about the use of an older version of Gromacs and suggested considering newer versions.

## General Learnings
- Increasing account priority can help expedite urgent calculations.
- Providing access to additional resources, such as other clusters or less busy nodes, can help alleviate high pressure on the facility.
- Offering to optimize job parameters can help improve resource utilization.
- Inquiring about software versions can help identify potential areas for improvement.
- Regular communication with users can help address concerns and provide updates on job status.
---

### 2022031542001248_Early-Fritz%20%22Dominik%20Th%C3%83%C2%B6nnes%22%20_%20iwia003h.md
# Ticket 2022031542001248

 # HPC Support Ticket Analysis

## Keywords
- Early-Fritz
- Certificate expiration
- Petsc build
- Multi-node workload
- HDR100 Infiniband
- Performance testing

## Summary
- **User Request:** Access to Early-Fritz for multi-node workload testing with specific hardware and software requirements.
- **Issue:** Certificate expiration.
- **Solution:** User granted access as an early user; advised to build Petsc themselves.

## Details
- **Hardware Requirements:** HDR100 Infiniband with 1:4 blocking; 72 cores, 250 GB per node.
- **Software Requirements:** Compiler, CMake, MPI, and ideally Petsc.
- **Application:** Testing walberla and hyteg software for usability and performance.
- **Root Cause:** Certificate expiration.
- **Solution:** User granted early access; advised to build Petsc themselves.

## Learning Points
- Ensure certificates are up-to-date to avoid access issues.
- Users may need to build specific software packages themselves if not pre-installed.
- Multi-node workload testing requires specific hardware and software configurations.

## Next Steps
- Monitor certificate expiration dates.
- Provide documentation or support for building software packages like Petsc.
- Ensure hardware and software configurations meet user requirements for performance testing.
---

### 2021021142002365_OpenMP%20auf%20Emmy.md
# Ticket 2021021142002365

 # HPC Support Ticket: OpenMP auf Emmy

## Keywords
- OpenMP
- MPI
- Memory Load
- CPU Utilization
- Submission Script
- OMP_NUM_THREADS
- OMP_PROC_BIND
- OMP_PLACES
- -ppn

## Problem Description
The user wants to reduce memory load by using 2 OpenMP threads per MPI process. However, when specifying the following in the submission script:
```bash
export OMP_NUM_THREADS=2
export OMP_PROC_BIND=true
export OMP_PLACES=cores
```
and requesting half the number of physical CPUs for MPI processes, it results in half of the CPUs being utilized with two OpenMP threads while the other half remains idle.

## Root Cause
The issue arises from the incorrect distribution of MPI processes across the nodes, leading to uneven CPU utilization.

## Solution
To ensure even distribution of OpenMP threads across all CPUs, the user needs to specify the number of MPI processes per node using the `-ppn` option. For example:
```bash
-ppn 10
```
This will start 10 MPI processes per node, ensuring a more balanced load distribution.

## General Learning
- Proper configuration of MPI processes and OpenMP threads is crucial for efficient CPU utilization.
- The `-ppn` option in `mpirun` is used to specify the number of processes per node.
- Always refer to `mpirun --help` for additional options and configurations.

## References
- `mpirun --help`
- HPC Services, Friedrich-Alexander-Universitaet Erlangen-Nuernberg

## Roles Involved
- HPC Admins
- 2nd Level Support Team
- Head of the Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support
- Software and Tools Developer
---

### 2023030242001127_Tier3-Access-Fritz%20%22Oskar%20Herrmann%22%20_%20gwgi026h.md
# Ticket 2023030242001127

 # HPC Support Ticket Analysis: Tier3 Access Request

## Keywords
- Tier3 Access
- Node Hours
- Core Hours
- NHR LargeScale Project
- Application Confusion
- Account Enabled

## Summary
A user submitted a request for Tier3 access with an incorrect understanding of node hours versus core hours. The HPC Admin clarified the difference and the limitations of the free Tier3 service. The user's account was eventually enabled.

## Root Cause
- User confusion between node hours and core hours.

## Solution
- HPC Admin explained the difference and the user's account was enabled without the need for a second application.

## What Can Be Learned
- **Node Hours vs. Core Hours**: Ensure users understand the difference to avoid overestimation of resources.
- **Tier3 Service Limitations**: Clarify the limits of the free Tier3 service compared to larger projects like NHR LargeScale.
- **User Communication**: Effective communication can resolve misunderstandings and prevent the need for additional applications.

## Actions Taken
- HPC Admin explained the resource limits and clarified the user's confusion.
- The user's account was enabled on the HPC system.

## Follow-Up
- No further action required as the user's account was successfully enabled.
---

### 2023102442002849_Tier3-Access-Fritz%20%22Sophia%20Thomas%22%20_%20gwgk100h.md
# Ticket 2023102442002849

 # HPC Support Ticket Conversation Analysis

## Keywords
- HPC Account Activation
- Multi-node Workload
- WRF Model
- Software Requirements
- MSc Thesis
- Sensitivity Studies
- Climate Modeling

## Summary
- **Account Activation**: The user's HPC account was activated on the Fritz system.
- **Workload Requirements**: The user requested a multi-node workload with specific hardware and software requirements.
- **Software Needs**: The user specified a list of required software including GNU compilers, Intel compiler suite, libraries, and post-processing tools.
- **Application**: The user is conducting sensitivity studies using the WRF atmospheric model for an MSc thesis as part of the NHR project "ATMOS".
- **Expected Results**: The studies aim to understand the impact of sea surface temperatures on local climate and glacier mass changes in high mountain regions.

## Root Cause of the Problem
- The user needed their HPC account activated and specified detailed requirements for their research project.

## Solution
- The HPC Admin activated the user's account and acknowledged the requirements.

## Lessons Learned
- Ensure timely activation of user accounts.
- Understand and document specific hardware and software requirements for research projects.
- Be aware of ongoing projects and their computational needs.

## Action Items
- Verify account activation for new users.
- Ensure the availability of required software and hardware resources.
- Maintain communication with users regarding their project needs and progress.
---

### 2022111142000428_Jobs%20auf%20Fritz%20-%20b136dc13%20_%20iwtm017h.md
# Ticket 2022111142000428

 # HPC Support Ticket Analysis: Jobs auf Fritz - b136dc13 / iwtm017h

## Keywords
- MATLAB
- Multinode Jobs
- Resource Allocation
- Monitoring
- ClusterCockpit

## Problem
- Users were allocating 2 nodes for their jobs, but MATLAB was primarily running on one node.
- Jobs were not efficiently utilizing the allocated resources.

## Root Cause
- MATLAB jobs were not configured to run on multiple nodes.
- Users were unaware of the resource utilization and monitoring tools available.

## Solution
- **Resource Allocation**: Users were advised to allocate resources based on actual usage to avoid unnecessary costs.
- **Monitoring**: Users were guided on how to access monitoring data:
  - For general users: Log in to the HPC portal and navigate to ClusterCockpit-Monitoring.
  - For iwtm-Account users: Directly log in to [monitoring.nhr.fau.de](https://monitoring.nhr.fau.de/).
- **MATLAB Multinode Jobs**: HPC admins clarified that they do not have in-depth MATLAB knowledge and do not currently offer "Matlab Parallel Server" for multinode jobs.

## General Learnings
- Always allocate resources based on actual needs to optimize usage and costs.
- Use monitoring tools to track job performance and resource utilization.
- MATLAB's ability to run on multiple nodes may require specific configurations or licenses not currently supported.

## Follow-up
- Users should investigate MATLAB's capabilities for multinode processing and potentially consult with MATLAB support for further assistance.
- HPC admins may consider documenting or providing guidance on how to optimize resource allocation for common software tools.
---

### 2024070142000675_Reservierung_Prioritisierung%20f%C3%83%C2%BCr%204%20Nodes%20am%20Wochenende.md
# Ticket 2024070142000675

 # HPC Support Ticket: Reservierung/Prioritisierung für 4 Nodes am Wochenende

## Keywords
- Reservierung
- Prioritisierung
- Nodes
- A100 80
- Wochenende
- Director's Budget
- scontrol create reservation

## Problem
- User requires 4 A100 80 nodes for context-length extension of LLMs.
- Needs reservation or prioritized access from Friday evening/Saturday morning until Monday 6:00 Uhr.

## Solution
- HPC Admin set up a reservation using `scontrol create reservation`.
- Reservation details:
  - `reservationname=llm-sw`
  - `user=b216dc10`
  - `starttime=2024-07-05T06:00:00`
  - `endtime=2024-09-20T06:00:00`
  - `flags=magnetic`
  - `nodes=a093[1-4]`
- User notified to inform when the reservation is no longer needed.

## Outcome
- Reservation was successfully created.
- User later requested to cancel the reservation.
- HPC Admin closed the ticket after the reservation was ended.

## Lessons Learned
- Users can request node reservations for specific time periods.
- Reservations can be managed using `scontrol create reservation`.
- Important to notify HPC Admin when reservation is no longer needed to free up resources.
- Director's Budget can be used for such requests if necessary.
---

### 2022122042002489_Testcluster%3A%20Recommended%20way%20of%20fixing%20the%20clock%20frequency.md
# Ticket 2022122042002489

 # HPC Support Ticket: Recommended Way of Fixing the Clock Frequency

## Issue
- **Subject:** Testcluster: Recommended way of fixing the clock frequency
- **User:** Experiencing deviations in clock frequency on the RRZE test cluster.
- **Current Setup:**
  - Using `SLURM_CPU_FREQ: high` for continuous benchmarking in ExaStencils.
  - Using `srun --cpu-freq=high` for the GHODDESS project.
  - Measured clock frequency from `likwid-perfctr` sometimes decreases significantly without code changes.

## Root Cause
- `SLURM_CPU_FREQ: high` is not an exact setting; it uses a high setting but not necessarily the highest.
- The highest applicable CPU frequency depends on active hardware threads and operations.
- `likwid-setFrequencies` requires the `likwid-accessD` daemon, which failed to start.

## Solution
- **Recommended Approach:**
  - Use the base CPU frequency for setting the clock frequency.
  - Read the base frequency from:
    - `/sys/devices/system/cpu/cpu0/cpufreq/bios_limit`
    - `/sys/devices/system/cpu/cpu0/cpufreq/base_frequency`
    - `likwid-powermeter -i | grep "Base clock:" | awk '{print $3}'`
  - Use the long notation with `srun`: `--cpu-freq=<min>-<max>:performance`

- **Additional Steps for `likwid-setFrequencies`:**
  - Ensure the job is allocated with the `-C hwperf` constraint to access hardware counters.
  - Example job allocation: `salloc -t 04:00:00 --exclusive -w casclakesp2 -c 80 -C hwperf`

## Keywords
- Clock frequency
- SLURM
- likwid-setFrequencies
- likwid-accessD
- Base CPU frequency
- srun
- Continuous benchmarking
- ExaStencils
- GHODDESS

## Lessons Learned
- `SLURM_CPU_FREQ: high` does not guarantee the highest frequency.
- Base CPU frequency should be used for consistent performance.
- `likwid-setFrequencies` requires access to hardware counters and the `likwid-accessD` daemon.
- Proper job allocation constraints (`-C hwperf`) are necessary for using `likwid-setFrequencies`.

## Conclusion
- Using the base CPU frequency with `srun` is recommended for consistent clock frequency.
- Ensure proper job allocation constraints when using `likwid-setFrequencies`.
---

### 2023060542003409_mpirun%20producing%20errors.md
# Ticket 2023060542003409

 # HPC Support Ticket: mpirun Producing Errors

## Keywords
- mpirun
- SLURM
- Typo
- Error Parsing Parameters
- Process Count

## Problem Description
The user encountered errors when executing MPI jobs using `mpirun` on the HPC system. The submission script contained a typo in the SLURM environment variable for the number of tasks.

## Root Cause
The typo in the script (`np=${SLURM_NTAKS}` instead of `np=${SLURM_NTASKS}`) resulted in an incorrect process count, leading to errors in parsing parameters by `mpirun`.

## Error Messages
```
[mpiexec@m0253.rrze.uni-erlangen.de] i_np_fn
(../../../../../src/pm/i_hydra/mpiexec/intel/i_mpiexec_params.h:942):
process count should be > 0
[mpiexec@m0253.rrze.uni-erlangen.de] match_arg
(../../../../../src/pm/i_hydra/libhydra/arg/hydra_arg.c:83): match
handler returned error
[mpiexec@m0253.rrze.uni-erlangen.de] HYD_arg_parse_array
(../../../../../src/pm/i_hydra/libhydra/arg/hydra_arg.c:128): argument
matching returned error
[mpiexec@m0253.rrze.uni-erlangen.de] mpiexec_get_parameters
(../../../../../src/pm/i_hydra/mpiexec/mpiexec_params.c:1359): error
parsing input array
[mpiexec@m0253.rrze.uni-erlangen.de] main
(../../../../../src/pm/i_hydra/mpiexec/mpiexec.c:1783): error parsing
parameters
```

## Solution
Correct the typo in the script:
```bash
np=${SLURM_NTASKS}
```

## Lessons Learned
- Always double-check environment variable names in scripts.
- Typos in environment variables can lead to unexpected errors in job execution.
- Proper error messages can help identify the root cause of issues.

## References
- SLURM Environment Variables
- `mpirun` Command Syntax

## Support Team Involved
- HPC Admins
- 2nd Level Support Team
---

### 2022012442001369_Early-Fritz%20%22Jacob%20Beyer%22%20_%20don%27t%20have%20one.md
# Ticket 2022012442001369

 # HPC Support Ticket Conversation Summary

## Keywords
- Early-Access
- Fritz Cluster
- SSH Public Key
- BLAS
- Eigen3
- OpenBLAS
- Intel MKL
- Job Monitoring
- Vektorisierung
- OpenMP
- Performance Optimization
- Zoom Meeting
- NHR-Rechenzeitantrag

## General Learnings
- **Early-Access Accounts**: Users are granted early access to the Fritz cluster for testing purposes.
- **SSH Public Key**: Users need to provide their SSH public key for access.
- **Software Requirements**: Users specify required software like BLAS, Eigen3, and C++17.
- **Job Monitoring**: HPC admins monitor job performance and provide feedback on optimization.
- **BLAS Libraries**: Intel MKL is preferred over OpenBLAS for better performance.
- **Performance Issues**: Users may face issues with vectorization and performance, which can be addressed through proper compilation and linking.
- **Support**: HPC admins offer support through email and Zoom meetings to resolve complex issues.
- **Formal Application**: Users need to submit a formal NHR-Rechenzeitantrag for continued access.

## Root Cause of Problems
- **BLAS Library**: The user's application was not utilizing vectorized operations, leading to suboptimal performance.
- **OpenBLAS Compilation**: The user compiled OpenBLAS without OpenMP support, causing performance issues.
- **Memory Bandwidth**: The user's jobs were not evenly distributing memory bandwidth across sockets.

## Solutions
- **Intel MKL**: Recommended to use Intel MKL for better performance instead of OpenBLAS.
- **Compiler and Linker Options**: Adjust compiler and linker options using the Intel Link Line Advisor.
- **Zoom Meeting**: Offered a Zoom meeting to assist with OpenBLAS compilation and performance optimization.
- **Formal Application**: Instructed the user to submit a formal NHR-Rechenzeitantrag for continued access.

## Documentation for Support Employees

### Early-Access Account Setup
1. **SSH Public Key**: Ensure the user provides their SSH public key for access.
2. **Software Requirements**: Note the user's software requirements, such as BLAS, Eigen3, and C++17.

### Performance Optimization
1. **Job Monitoring**: Monitor the user's jobs for performance issues, such as lack of vectorization and suboptimal memory bandwidth usage.
2. **BLAS Libraries**: Recommend using Intel MKL for better performance. Provide guidance on adjusting compiler and linker options using the Intel Link Line Advisor.
3. **OpenBLAS Compilation**: If the user insists on using OpenBLAS, offer a Zoom meeting to assist with proper compilation and performance optimization.

### Formal Application
1. **NHR-Rechenzeitantrag**: Instruct the user to submit a formal NHR-Rechenzeitantrag for continued access. Provide the necessary information and links for the application process.

By following these guidelines, support employees can effectively address similar issues and ensure optimal performance for users on the Fritz cluster.
---

### 42287079_Unresponsive%20LIMA.md
# Ticket 42287079

 ```markdown
# HPC-Support Ticket: Unresponsive LIMA Cluster

## Subject
Unresponsive LIMA

## User Report
- **Issue**: System slow and unresponsive while using the LIMA cluster.
- **Observation**: A user (iwst137) is consuming significant CPU resources.
- **Details**:
  ```
  top - 15:47:15 up 68 days, 23:52, 84 users,  load average: 2.14, 2.23, 2.20
  Tasks: 1219 total,   3 running, 1118 sleeping,  97 stopped,   1 zombie
  Cpu(s):  0.1%us,  4.2%sy,  4.2%ni, 91.5%id,  0.0%wa,  0.0%hi,  0.0%si,  0.0%st
  Mem:  49416320k total, 32901864k used, 16514456k free,    17100k buffers
  Swap: 45711352k total,   285568k used, 45425784k free,  4982688k cached
  PID USER      PR  NI  VIRT  RES  SHR S %CPU %MEM    TIME+  COMMAND
  350 root      39  19     0    0    0 R 100.0  0.0  57702:19 kipmi0
  2074 iwst137   39  19 2615m 2.3g  14m R 100.1  4.9  14520:29 solver-pcmpi.ex
  29519 bcpc07    20   0  146m  10m 2700 S  1.7  0.0   0:00.05 vim
  29366 iww183    20   0 15952 2284 1012 R  1.0  0.0   0:01.68 top
  105 root      20   0     0    0    0 S  0.7  0.0 518:55.90 events/6
  ```

## HPC Admin Response
- **Admin**: den Grund
- **Response**: Keine Probleme erkennbar. Problem zwischen Tastatur und Stuhl?

## Keywords
- Unresponsive cluster
- High CPU usage
- Resource consumption
- User impact

## Root Cause
- High CPU usage by a specific user (iwst137) running `solver-pcmpi.ex`.

## Solution
- No immediate solution provided by the admin.
- Further investigation required to determine if the high CPU usage is justified or if resource limits need to be enforced.

## General Learning
- High CPU usage by individual users can impact overall system performance.
- Monitoring and managing resource usage is crucial for maintaining cluster responsiveness.
- Admins should investigate high resource usage to ensure fair distribution and system stability.
```
---

### 2021042142002977_Probleme%3A%20RRZE%20Woodcrest%20Cluster%20is%20using%20too%20much%20memory.md
# Ticket 2021042142002977

 # HPC Support Ticket Analysis: Memory Usage Issue on Woodcrest Cluster

## Keywords
- Memory usage
- Job failure
- Out-of-Memory (OOM)
- Monitoring
- Memory leak
- PBS script
- Python automation

## Summary
A user encountered issues with jobs on the Woodcrest Cluster, receiving warnings about excessive memory usage. The jobs were expected to be computationally intensive but not memory-intensive. The user provided the PBS script used to submit the jobs.

## Root Cause
- The jobs were consuming more memory than expected, leading to Out-of-Memory (OOM) errors.
- The HPC Admin confirmed the OOM warnings were justified based on system monitoring.
- Possible memory leak in the user's code.

## Solution
- The user needs to investigate the cause of the linear increase in memory usage, possibly due to a memory leak.
- The HPC Admin provided links to job monitoring information for further analysis.

## Lessons Learned
- Always monitor memory usage of jobs to ensure they stay within allocated limits.
- Investigate potential memory leaks in the code if memory usage increases unexpectedly.
- Use system monitoring tools to verify job performance and resource usage.
- Ensure PBS scripts are correctly configured to request appropriate resources.

## Recommendations
- Users should review their code for memory leaks and optimize memory usage.
- Regularly check job monitoring information to identify and address resource issues.
- HPC Admins can provide guidance on using monitoring tools and interpreting results.

## References
- Job monitoring links provided by the HPC Admin for detailed analysis.

This documentation can be used to troubleshoot similar memory usage issues in the future.
---

### 2020041942000172_Hyperthreading%20auf%20Emmy.md
# Ticket 2020041942000172

 # HPC-Support Ticket: Hyperthreading auf Emmy

## Keywords
- Hyperthreading
- Skalierungstest
- mpirun
- Intel-MPI
- MPI-Wrapper
- ppn
- npernode

## Problem
- User is testing strong scaling of a simulator on Emmy (40 processes per node, up to 20 nodes).
- The simulator scales well, but one section does not benefit from hyperthreading.
- User wants to disable hyperthreading for the scaling test and use only 20 processes per node.
- Setting `ppn=20` is not allowed.

## Solution
- Use `mpirun` to ensure only physical cores are utilized.
- Syntax varies depending on the MPI implementation (e.g., `-ppn 20` or `-npernode 20`).
- For a pure MPI code with Intel-MPI, use the MPI-Wrapper:
  ```bash
  /apps/rrze/bin/mpirun -pinexpr S0:0-9@S1:0-9 ./a.out
  ```

## General Learnings
- Hyperthreading can affect the performance of certain program sections.
- Disabling hyperthreading for specific tests can be achieved through `mpirun` configurations.
- Different MPI implementations may require different syntax for setting the number of processes per node.
- The MPI-Wrapper provided by the HPC site can be used for Intel-MPI to ensure proper core utilization.

## Follow-Up
- The user confirmed that the solution worked perfectly.
- The HPC Admin offered further assistance for benchmarking and optimization.

## Roles
- **HPC Admins**: Provided the solution and offered further assistance.
- **User**: Reported the issue and confirmed the solution worked.

## Additional Notes
- The ticket highlights the importance of understanding MPI configurations for optimal performance testing.
- The solution can be reused for similar issues related to hyperthreading and MPI configurations.
---

### 2023101042000877_Tier3-Access-Fritz%20%22Venkatesh%20Pulletikurthi%22%20_%20iwst087h.md
# Ticket 2023101042000877

 # HPC Support Ticket Analysis

## Keywords
- Tier3 Access
- Fritz
- Core Hours
- Usage Check
- sreport
- Direct Numerical Simulation
- Multi-node Workload

## Summary
- **User Request**: Access to Fritz for multi-node workload with specific requirements.
- **Granted Resources**: 800,000 core hours.
- **User Query**: CPU hours limit and usage check.

## Detailed Information
- **User Needs**:
  - Multi-node workload with HDR100 Infiniband.
  - 72 cores and 250 GB per node.
  - 800,000 node hours on Fritz.
  - Software: FRITZ.
  - Application: Direct Numerical Simulation of 3D channel with roughness.
  - Expected Results: Conference presentation and journal publication.

- **Admin Actions**:
  - Account activation for Fritz.
  - Granting full 800,000 core hours.

- **User Query**:
  - CPU hours limit.
  - Method to check usage.

- **Admin Response**:
  - Full 800,000 core hours granted.
  - Usage check command: `sreport user topusage -t hours start=2023-01-01 end=2023-10-11` on any Fritz frontend.

## Solution
- **Usage Check Command**:
  ```bash
  sreport user topusage -t hours start=2023-01-01 end=2023-10-11
  ```

## Notes
- **Root Cause**: User needed clarification on granted resources and usage tracking.
- **Solution**: Provided usage check command and confirmed granted resources.

## General Learnings
- **Resource Allocation**: Understanding how to allocate and confirm resources.
- **Usage Tracking**: Methods to track resource usage on HPC systems.
- **User Support**: Importance of clear communication regarding resource limits and usage.
---

### 2024101542004335_Jobs%20on%20Fritz%20not%20using%20resources%20-%20iwst087h.md
# Ticket 2024101542004335

 # HPC Support Ticket Analysis

## Subject: Jobs on Fritz not using resources

### Keywords:
- JobId=1622600
- Fritz
- Resource utilization
- ClusterCockpit
- Job monitoring

### Summary:
- **Issue**: A job (JobId=1622600) on Fritz was allocated 64 nodes but was not utilizing the resources.
- **Action Taken**: HPC Admin notified the user to check the job's output and progress using ClusterCockpit.
- **Outcome**: The user canceled the job without responding to the notification.

### Lessons Learned:
- **Monitoring Tools**: Use ClusterCockpit for job monitoring and resource utilization tracking.
- **User Communication**: Notify users promptly about underutilized resources to ensure efficient use of HPC resources.
- **Follow-up**: Ensure follow-up with users to understand the root cause of underutilization and provide assistance if needed.

### References:
- [ClusterCockpit Monitoring](https://monitoring.nhr.fau.de/)
- [Job Monitoring with ClusterCockpit](https://doc.nhr.fau.de/job-monitoring-with-clustercockpit/)

### Root Cause:
- The root cause of the underutilization was not determined as the user canceled the job without providing feedback.

### Solution:
- No specific solution was implemented as the user canceled the job. Future instances should involve detailed communication with the user to identify and resolve the issue.
---

### 2019081942001747_Jobs%20with%20high%20CPU%20load%20-%20mpp3006h.md
# Ticket 2019081942001747

 # HPC Support Ticket: Jobs with High CPU Load

## Keywords
- High CPU load
- MPI processes
- OMP_NUM_THREADS
- Memory issues
- Performance optimization
- Job monitoring

## Summary
The user's jobs were causing high CPU loads on the HPC cluster. The job scripts requested 20 MPI processes per node and set OMP_NUM_THREADS to 10, resulting in 200 threads running on 40 logical CPU cores per node. This configuration led to performance issues, with more than 50% of the time spent in the operating system kernel and MPI.

## Root Cause
- The user's jobs were configured to use a high number of threads per CPU core, leading to inefficient resource utilization and high CPU loads.
- The user reported that reducing the number of processes resulted in memory errors, causing job failures.

## Solution
- The HPC Admins suggested optimizing the job configuration to reduce the number of threads per CPU core.
- The user was advised to contact the HPC support team for further assistance in optimizing their application.

## Lessons Learned
- High CPU loads can be caused by inefficient job configurations, such as requesting too many threads per CPU core.
- Monitoring job performance and resource utilization is crucial for identifying and addressing performance issues.
- Communication between users and HPC support is essential for resolving complex performance problems.
- Users should be aware of the potential consequences of high CPU loads and the importance of optimizing their job configurations.

## Follow-up Actions
- The user's account was monitored for further misuse, and measures were taken to limit job submissions and reduce priority if necessary.
- The HPC Admins offered to schedule a meeting to discuss optimization strategies for the user's application.
- The user's HPC account expired, resolving the issue of high CPU loads caused by their jobs.
---

### 2025022542002402_Job%202411215.md
# Ticket 2025022542002402

 ```markdown
# HPC-Support Ticket Conversation: Job 2411215

## Keywords
- Job Prioritization
- IROS
- Ablation
- Munich University of Applied Sciences
- FAU
- NHR@FAU

## Summary
A user from Munich University of Applied Sciences requested prioritization for Job 2411215, which is a 72-hour job for a promising ablation study for IROS.

## Root Cause
The user needed the job to be prioritized due to its importance for an upcoming conference (IROS).

## Solution
The HPC Admin confirmed that the job would be started soon.

## General Learnings
- Users may request job prioritization for time-sensitive projects.
- HPC Admins can expedite job processing based on user requests and project importance.
- Effective communication between users and HPC Admins is crucial for timely job execution.
```
---

### 2024100442003197_%5BTestcluster%5D%20likwid-setFrequencies%20kaputt.md
# Ticket 2024100442003197

 # HPC Support Ticket: likwid-setFrequencies Issue

## Keywords
- likwid-setFrequencies
- Testcluster
- CPU Frequency
- Uncore Frequency
- srun
- setuid-bit
- Job End Cleanup

## Problem
- The `likwid-setFrequencies` tool is partially unusable on the Testcluster because the `likwid-setFreq` daemon cannot be started by users due to its permissions being set to `-rws------`.
- Users can set CPU frequency using `srun --cpufreq=X-X:performance`, but Uncore frequency adjustment is only possible via `likwid-setFrequencies`.

## Root Cause
- The `likwid-setFreq` binary is intentionally set to `-rws------` to prevent users from manually adjusting frequencies without a cleanup mechanism at the end of jobs.

## Solution
- No immediate solution provided. The issue is noted as a feature request.
- Nodes need to be reserved for experiments with `likwid-setFrequencies` until a cleanup mechanism is implemented.

## General Learnings
- Frequency adjustments using `likwid-setFrequencies` require careful management to avoid affecting subsequent jobs on the same node.
- The `setuid-bit` is intentionally not set to prevent unintended frequency changes without proper cleanup.
- Feature requests and reservations for specific experiments are necessary until a robust solution is implemented.

## Next Steps
- Await further updates on the feature request for a cleanup mechanism.
- Reserve nodes for experiments requiring `likwid-setFrequencies` to avoid disruptions.
---

### 2025030142000564_Tier3-Access-Fritz%20%22Aparna%20Karikkulam%20Unnikrishnan%22%20_%20ptfs234h.md
# Ticket 2025030142000564

 # HPC-Support Ticket Conversation Analysis

## Keywords
- HPC Access
- Fritz Cluster
- Multi-node Workload
- HDR100 Infiniband
- GCC / Intel Compilers
- OpenMPI
- LIKWID
- LAPACK / BLAS
- Python
- Performance Profiling
- Scalability Studies
- Roofline Model Analysis
- Conjugate Gradient (CG) Solvers
- Preconditioned CG (PCG) Solvers
- Heat Equation
- Finite Difference Methods

## Summary
- **User Request**: Access to Fritz cluster for multi-node workload.
- **Resources Requested**: 800 node hours on Fritz.
- **Software Requirements**: GCC / Intel Compilers, OpenMPI, LIKWID, LAPACK / BLAS, Python.
- **Application**: Solving 2D steady-state heat equation using finite difference methods.
- **Expected Outcomes**: Performance benchmarks, roofline model analysis, scalability studies, optimized solver implementation.

## Root Cause of the Problem
- User needed access to the Fritz cluster for a specific project involving large-scale computations.

## Solution
- **HPC Admin Response**: User was granted access to the Fritz cluster.

## General Learnings
- **Access Request Process**: Users need to specify their computational needs, software requirements, and expected outcomes.
- **Software Tools**: Common tools for performance analysis and optimization include LIKWID, LAPACK, BLAS, and Python.
- **Scalability and Performance**: Importance of benchmarking and optimizing solvers for large-scale problems.
- **Communication**: Clear and detailed communication of project requirements and expected outcomes is crucial for efficient support.

## Additional Notes
- Users may require additional compute time based on preliminary results.
- The support process involves verifying user needs and granting access to the appropriate resources.

---

This analysis provides a structured overview of the support ticket conversation, highlighting key elements and general learnings for future reference.
---

### 2021031642002747_Re%3A%20Your%20Job%20ID%207422782%20on%20the%20RRZE%20Woodcrest%20Cluster%20is%20using%20too%20much%.md
# Ticket 2021031642002747

 # HPC Support Ticket: Job Using Too Much Memory

## Keywords
- Memory usage
- Job submission (qsub)
- Memory limits
- Swap space
- Node scheduling

## Problem Description
- User's job on the Woodcrest cluster is using excessive memory, causing nodes to run out of swap space.
- The operating system may kill processes randomly, potentially affecting important system services.
- Jobs swapping heavily will run very slowly due to swap space being much slower than real memory.

## Root Cause
- The job is consuming more memory than available on the nodes, leading to excessive swapping and potential system instability.

## Solution
- **Reduce Memory Requirement**: If possible, optimize the job to use less memory per node.
- **Adjust Processor Usage**: Use fewer processors per node to increase available memory per processor. For example, use `-pernode` or `-npernode` parameters with `mpirun`.
- **Schedule on High-Memory Nodes**: If jobs regularly require more than 8GB RAM, schedule them on nodes with 32GB RAM using the property `:any32g` in the `qsub` command, e.g., `qsub -l nodes=1:ppn=4:any32g`.

## Lessons Learned
- It is not possible to set an upper limit for memory usage via `qsub`.
- Proper scheduling and resource allocation are crucial to avoid excessive memory usage and potential system instability.
- Regularly monitor job memory usage to ensure efficient resource utilization.

## Actions Taken
- The user was advised to abort the job and resubmit it with adjusted parameters to avoid excessive memory usage.
- The user was informed about scheduling jobs on high-memory nodes if needed.

## Follow-Up
- The ticket was closed after the user acknowledged the advice and thanked for the help.

## References
- HPC System Health Checker email
- HPC Admin response
- User acknowledgment email

---

This documentation provides a summary of the issue, the root cause, the solution, and the lessons learned to help support employees handle similar issues in the future.
---

### 2018110542001349_Ineffiziente%20Ressourcennutzung%20auf%20Emmy%20_%20bctc33.md
# Ticket 2018110542001349

 # HPC Support Ticket: Inefficient Resource Usage on Emmy / bctc33

## Keywords
- Inefficient resource usage
- Job termination
- MPI processes
- PBS script
- Account blocking

## Summary
A user was submitting jobs that requested a large number of compute nodes but only utilized a small fraction of them. This led to inefficient resource usage and job termination.

## Root Cause
The user's PBS scripts requested a varying number of nodes (25-64) but explicitly instructed `mpirun` to start only 8 MPI processes. This discrepancy led to underutilization of allocated resources.

```bash
#PBS -l nodes=36:ppn=40,walltime=24:00:00
/apps/rrze/bin/mpirun_rrze-intelmpd -intelmpd -n 8 -pin "0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19"
```

## Actions Taken
1. **Notification**: HPC Admins notified the user about the issue and terminated the inefficient jobs.
2. **Account Blocking**: Due to repeated submissions of faulty jobs, the user's account was temporarily blocked.
3. **Unblocking**: After the user acknowledged the issue and promised to fix it, the account was unblocked.
4. **Follow-up**: Despite assurances, the problem persisted, leading to further notifications.

## Solution
The user needs to adjust the PBS scripts to ensure that the number of MPI processes matches the number of requested nodes. For example:

```bash
#PBS -l nodes=36:ppn=40,walltime=24:00:00
/apps/rrze/bin/mpirun_rrze-intelmpd -intelmpd -n 1440 -pin "0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19"
```

## Lessons Learned
- **Resource Allocation**: Ensure that the number of MPI processes matches the number of requested nodes to avoid resource wastage.
- **Communication**: Promptly respond to HPC Admin notifications to prevent account blocking.
- **Script Management**: Regularly review and update job scripts to prevent recurring issues.

## Follow-up
Monitor the user's jobs to ensure the issue is resolved and provide additional guidance if necessary.
---

### 2023062642002362_Access%20to%20huge-memory%20Fritz%20node%20of%20Sapphire%20Rapids%20processor.md
# Ticket 2023062642002362

 # HPC Support Ticket: Access to Huge-Memory Fritz Node

## Keywords
- Huge-memory Fritz node
- Sapphire Rapids processor
- Ice Lake processor
- LULESH performance
- MucoSim students
- Access request
- Partition
- Account

## Summary
A request was made for two MucoSim students to access a huge-memory Fritz node with a Sapphire Rapids processor to compare LULESH performance against an Ice Lake processor.

## Root Cause
- Students required access to specific high-performance computing resources for a comparative study.

## Solution
- HPC Admins enabled the students' accounts (muco103h and muco105h) for the Sapphire Rapids processor.
- Students were instructed to use the partition `--partition=spr1tb` and add `-A muco_spr` when requesting access.
- The following commands were executed to add the users to the appropriate account:
  ```bash
  sacctmgr add account muco_spr descr="SPR-Zugang MuCoSim" parent=fau
  sacctmgr -i add user muco105h account=muco_spr
  sacctmgr -i add user muco103h account=muco_spr
  ```

## General Learnings
- Proper partition and account settings are crucial for accessing specific HPC resources.
- HPC Admins can enable specific user accounts for access to specialized hardware.
- Clear communication of access requirements and duration is important for efficient resource allocation.
---

### 2022062442001743_woody3%20unbenutzbar.md
# Ticket 2022062442001743

 ```markdown
# HPC-Support Ticket: woody3 unbenutzbar

## Keywords
- woody3
- Login-Server
- Memory usage
- ulimits
- Python script
- RAM

## Problem Description
A user reported that a specific Python script run by another user was consuming excessive memory, causing the entire login server (woody3) to become unresponsive for over half an hour. The main issue was the complete utilization of the entire RAM by a single user.

## Root Cause
- A user's Python script consumed an excessive amount of RAM, leading to the unavailability of the login server.

## Solution
- Adjust the ulimits to restrict a single user from using more than 50% of the total RAM.

## General Learnings
- Monitoring and limiting resource usage on login servers is crucial to prevent disruptions.
- Adjusting ulimits can help manage resource allocation more effectively.
- Regularly review and update resource limits based on user feedback and system performance.
```
---

### 2018112742001085_Python%20am%20woody%20Frontend.md
# Ticket 2018112742001085

 # HPC Support Ticket: Python Process on Frontend

## Keywords
- Python
- Frontend
- Memory Usage
- User Process
- HPC Admin
- Resource Blocking

## Problem Description
A user was running a Python process on the frontend node (`woody3`), consuming 97% of the memory. This made it impossible for other users to work effectively.

## Root Cause
- A user was running a resource-intensive Python process directly on the frontend node, causing high memory usage and blocking other users.

## Ticket Conversation Summary
1. **User Report**:
   - A user reported that another user (`mpwm007h`) was running a Python process on the frontend node, consuming 97% of the memory.
   - The process details were provided:
     ```
     PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND
     2860 mpwm007h  39  19 34.556g 0.031t     24 D   1.0 96.7  38:35.36 python
     ```

2. **HPC Admin Response**:
   - The HPC Admin terminated the user's process.

3. **User Follow-up**:
   - The user reported that the same user started another Python process on the frontend, consuming significant resources again.
   - The user requested that the HPC Admin contact the user to inform them about the impact on other users.

## Solution
- The HPC Admin terminated the user's process to free up resources.
- The user was advised to run resource-intensive processes on compute nodes instead of the frontend node.

## General Learning
- Running resource-intensive processes on the frontend node can block other users from working effectively.
- Users should be informed to run such processes on compute nodes instead.
- HPC Admins should monitor and manage resource usage on frontend nodes to ensure fair use.

## Next Steps
- Inform users about proper usage of frontend and compute nodes.
- Monitor frontend node resource usage and take action if necessary.
- Consider implementing policies or guidelines for frontend node usage.
---

### 2024071942001462_job%20on%20Fritz%20uses%20only%20one%20core%20-%20b172da.md
# Ticket 2024071942001462

 ```markdown
# HPC-Support Ticket: Job on Fritz Uses Only One Core

## Subject
Job on Fritz uses only one core - b172da

## Issue
The user's job on Fritz (1500447) and other jobs with "corr" in the name were using only one core despite specifying multiple cores in the job script.

## Root Cause
The user's job script specified multiple cores using `#SBATCH --cpus-per-task=104` and `export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK`, but the numpy operations were not utilizing multiple cores effectively.

## Diagnosis
- The user's job script was correct, but the numpy operations, specifically `np.einsum`, were not parallelized effectively.
- The user's main calculation involved element-wise operations and dot products, which were not benefiting from numpy's multithreading.

## Solution
- The HPC Admin suggested using multiprocessing to parallelize the operations.
- The user was provided with a modified script that utilized Python's `multiprocessing` module to distribute the workload across multiple processes.

```python
import multiprocessing as mp

Nt = 200
tlist = np.linspace(0.3, Nt*0.3, Nt)

def get_els(n):
    res = np.array([np.einsum('i,i', H1[n,:] * np.sin(all_evals_diff[n,:]*_t), H2[n,:]) for _t in tlist])
    return res, n

results = np.empty([Nt,D_Hilbert])
Nprocess = mp.cpu_count()
pool = mp.Pool(Nprocess)
for res, n in pool.map(get_els, range(D_Hilbert)):
    results[:,n] = res
```

## Outcome
- The user tested the suggested code and confirmed that it produced the correct results.
- The user planned to test the speed of the modified script on the cluster.

## Keywords
- Job script
- Multithreading
- Numpy
- Multiprocessing
- Parallelization
- SLURM
- Cluster monitoring

## Lessons Learned
- Numpy's multithreading may not be effective for certain types of operations, such as element-wise operations and dot products.
- Using Python's `multiprocessing` module can help distribute the workload across multiple processes, improving performance on HPC clusters.
- It is important to verify that the job script is utilizing the allocated resources effectively.
```
---

### 2019031242000028_Problem%20memoryhog.md
# Ticket 2019031242000028

 # HPC Support Ticket: Problem memoryhog

## Keywords
- Resource temporarily unavailable
- Fork error
- High load average
- Reboot
- Bash script
- Self-replicating script
- Memoryhog

## Problem Description
- User accidentally wrote a bash script that repeatedly calls itself with 28 threads, causing the system to become unresponsive.
- User can log in but cannot perform any actions due to "fork: retry: Resource temporarily unavailable" errors.
- High load average observed (e.g., 6341.52, 5716.61, 4461.25).
- `top` command shows a high number of tasks and high CPU usage.

## Root Cause
- Self-replicating bash script consuming excessive resources.

## Solution
- HPC Admin performed a reboot of the system to clear the excessive processes.

## Lessons Learned
- Be cautious with self-replicating scripts to avoid resource exhaustion.
- Monitor system load and resource usage to detect and address issues early.
- Rebooting the system can be an effective solution to clear excessive processes and restore normal operation.

## Follow-up Actions
- Educate users on the risks of self-replicating scripts.
- Implement monitoring and alerting for high load averages and resource usage.

## Related Teams
- HPC Admins
- 2nd Level Support Team
- Head of the Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support
- Software and Tools Developer
---

### 2018110642002104_Request%3ADistribution%20of%20memory%20on%20emmy%20node.md
# Ticket 2018110642002104

 # HPC Support Ticket: Distribution of Memory on Emmy Node

## Keywords
- Memory distribution
- PBS script
- MPI
- Intel MPI
- mpirun
- Node allocation
- Memory allocation
- Job crashes
- Dedicated nodes

## Problem Description
- User's jobs on Emmy cluster are running out of main memory and crashing the nodes.
- User requires 130 GB of RAM for their MPI code.
- User is allocating 3 nodes (each with 64 GB RAM) but using only 50 out of 120 available processors.
- User's PBS script does not specify how to distribute the processes across nodes.

## Root Cause
- The user's MPI code requires more memory than allocated by the current distribution of processes across nodes.
- The user is not specifying the distribution of processes to the nodes in the mpirun command.

## Solution
- Specify the distribution of processes to the nodes using the `-ppn` option in the mpirun command.
  - Example: `mpirun -np 60 -ppn 20 run.ex`
- Ensure that the memory of all allocated nodes is fully utilized by distributing the processes evenly.
- Schedule an appointment with HPC support for further assistance if needed.

## General Learnings
- Always specify the distribution of processes to the nodes in the mpirun command to ensure efficient memory utilization.
- On Emmy cluster, dedicated nodes are allocated, so there is no need to specify memory requirements in the PBS script.
- If jobs are crashing due to memory issues, it is important to review the memory requirements of the code and adjust the distribution of processes accordingly.
- Communication with HPC support can help resolve complex issues and optimize job submissions.
---

### 2023042642000733_Simulationen%20mit%20mehr%20als%2064%20Knoten%20auf%20Meggie.md
# Ticket 2023042642000733

 # HPC-Support Ticket Conversation Analysis

## Subject
Simulationen mit mehr als 64 Knoten auf Meggie

## User Request
- User wants to run simulations with more than 64 nodes on Meggie to avoid exceeding the 24-hour maximum runtime.
- User has provided parallel scaling test results.

## HPC Admin Responses
- HPC Admin asks for the number of nodes required and the job IDs behind the scaling plot.
- HPC Admin suggests implementing checkpoint/restart in the user's application.
- HPC Admin notes that the user's jobs show poor performance and suggests optimizing the code.
- HPC Admin analyzes the code and identifies the `LinearForm::Assemble()` function from the MFEM library as the bottleneck.
- HPC Admin suggests that using fewer nodes might be more efficient due to uneven field distribution among workers.

## User Responses
- User provides the number of nodes required (128) and the job IDs.
- User implements checkpoint/restart in the code.
- User explains the field distribution algorithm and provides parallel scaling test results.
- User requests the HPC Admin to delete the copied code after analysis.

## Solutions and Recommendations
- Implement checkpoint/restart in the user's application to avoid exceeding the maximum runtime.
- Optimize the code to improve performance, focusing on the `LinearForm::Assemble()` function from the MFEM library.
- Consider using fewer nodes if the field distribution among workers is uneven.
- Ensure that the number of fields per worker differs by at most 1 to achieve even distribution.

## Additional Information
- The user's parallel scaling test results show reasonable walltime scaling, indicating that using 64 nodes is efficient.
- The HPC Admin deletes the copied code after analysis as requested by the user.

## Root Cause of the Problem
- The root cause of the performance issue is the `LinearForm::Assemble()` function from the MFEM library, which consumes most of the computation time.

## Solution Found
- The user implemented checkpoint/restart in the code to avoid exceeding the maximum runtime.
- The HPC Admin analyzed the code and provided recommendations for optimization.
- The user adjusted the field distribution algorithm to ensure even distribution among workers.

This report provides a summary of the HPC-Support ticket conversation, including the user's request, HPC Admin responses, user responses, solutions and recommendations, additional information, the root cause of the problem, and the solution found. This documentation can be used by support employees to look up help for similar errors in the future.
---

### 2025010742002546_Runtimes%20Differences.md
# Ticket 2025010742002546

 # HPC-Support Ticket: Runtime Differences

## Keywords
- Runtime differences
- CPLEX
- CPU frequency
- Thread binding
- Slurm
- srun
- cpu-freq
- cpu-bind

## Problem Description
- User encountered significant runtime differences when running CPLEX on login nodes vs. computing nodes.
- The runtime on computing nodes was significantly slower (>75% longer).
- The issue was not resolved by setting `OMP_NUM_THREADS` or staging the software and instances.

## Root Cause
- The default CPU frequency and thread binding settings on the computing nodes were not optimal for multi-threaded applications like CPLEX.

## Solution
- Use the following command to set the CPU frequency to performance and avoid thread binding:
  ```bash
  srun --cpu-bind=none --cpu-freq=performance
  ```
- This command can be used with `salloc` or `sbatch`, but the frequency will only be set once `srun` is called.

## General Learning
- Some applications, especially those relying heavily on multi-threading, may require specific CPU frequency and thread binding settings for optimal performance.
- The `--cpu-freq` and `--cpu-bind` options in Slurm can be used to control these settings.
- It is recommended to test these settings for applications that show unexpected runtime differences.

## Recommendation
- Use the `srun --cpu-bind=none --cpu-freq=performance` command for jobs that are sensitive to CPU frequency fluctuations or thread binding.
- For jobs where runtime differences are not noticeable, this command may not be necessary. Decide based on the specific behavior of the software being used.
---

### 2018052342001488_Failure.md
# Ticket 2018052342001488

 ```markdown
# HPC Support Ticket: Failure

## Keywords
- CentOS 7.5 and 7.4 compatibility
- MPI debugging
- Intel MPI
- PSM2 error
- Omnipath
- Sicherheitsupdates
- Performance impact
- execstack workaround

## Summary
A user encountered job failures after applying security updates to the HPC system. The issue was related to compatibility between CentOS 7.5 and 7.4 nodes and MPI configurations.

## Root Cause
- Incompatibility between CentOS 7.5 and 7.4 nodes.
- MPI configuration issues related to PSM2 and Omnipath.
- Security updates causing collateral damage.

## Steps Taken
1. **Initial Diagnosis**:
   - HPC Admin identified that CentOS 7.5 and 7.4 nodes were not compatible.
   - MPI debugging was suggested using `I_MPI_DEBUG=5`.

2. **Further Debugging**:
   - User increased debug levels to 12, 15, and 25 but encountered similar outputs.
   - HPC Admin suggested setting `I_MPI_FABRICS` and `I_MPI_FABRICS_LIST` environment variables.

3. **Workaround**:
   - User applied the suggested environment variables and reported that the workaround was successful.
   - Performance impact was estimated to be around 10%.

4. **Final Resolution**:
   - HPC Admin suggested using the `execstack -c` workaround based on a bug report.
   - User confirmed that the workaround resolved the issue.

## Solution
- Set the environment variables `I_MPI_FABRICS="shm:ofa"` and `I_MPI_FABRICS_LIST="ofa"`.
- Apply the `execstack -c` workaround to resolve the PSM2 issue.

## Lessons Learned
- Security updates can cause unexpected issues in HPC environments.
- MPI debugging can be complex and may require incremental increases in debug levels.
- Compatibility between different versions of CentOS can be a source of issues.
- Workarounds such as setting specific environment variables and using `execstack` can resolve complex MPI issues.
```
---

### 2018121842001466_inefficient%20resource%20utilization%20on%20Emmy%20_%20mptf004h.md
# Ticket 2018121842001466

 # Inefficient Resource Utilization on Emmy

## Keywords
- Inefficient resource utilization
- Emmy cluster
- Job allocation
- Process distribution
- Memory allocation
- Floating point operations
- Algorithm implementation

## Problem Description
Some jobs on the Emmy cluster were found to be inefficiently utilizing resources. Specifically, jobs allocated 20 nodes and started 24 processes on all nodes, but the last three nodes did not perform any actual work. These nodes did not allocate much memory and did not execute any floating point operations.

## Root Cause
The algorithm of the code was implemented such that if the number of processors is equal to the number of K points, all nodes share the workload equally. Otherwise, some nodes remain empty. The user submitted jobs with parameters that changed the number of K points but forgot to adjust the number of required processors accordingly, leading to empty nodes.

## Solution
The user identified the issue and plans to ensure that the number of processors matches the number of K points in future job submissions. Additionally, the user will attempt to modify the current algorithm to better handle such scenarios.

## Lessons Learned
- Ensure that the number of allocated nodes and processes matches the workload requirements.
- Verify that job parameters are correctly set to avoid resource wastage.
- Consider optimizing algorithms to efficiently utilize allocated resources.

## References
- [Job Info Link](https://www.hpc.rrze.fau.de/HPC-Status/job-info.php?USER=mptf004h&JOBID=1027602&ACCESSKEY=721eb79e&SYSTEM=EMMY)
- HPC Services, Friedrich-Alexander-Universitaet Erlangen-Nuernberg, Regionales RechenZentrum Erlangen (RRZE)
---

### 2024031842001659_Tier3-Access-Fritz%20%22Petr%20Vacek%22%20_%20iwia101h.md
# Ticket 2024031842001659

 # HPC Support Ticket Analysis: Tier3-Access-Fritz

## Keywords
- Tier3 Access
- Fritz
- Multi-node workload
- HDR100 Infiniband
- HyTeG framework
- Coarse grid solvers
- V-cycle methods
- Benchmarking

## Summary
A user requested access to the Fritz cluster for a multi-node workload involving benchmarking coarse grid solvers in the HyTeG framework. The request included specifications for the required resources and expected outcomes.

## Details
- **Contact:** User (iwia101h)
- **Resource Requirements:**
  - Multi-node workload
  - HDR100 Infiniband with 1:4 blocking
  - Per node: 72 cores, 250 GB
- **Compute Time:** 288 node hours
- **Software:** No special requirements
- **Application:** Benchmarking coarse grid solvers in the HyTeG framework
- **Expected Results:** Insight into the influence of coarse grid solvers on the convergence and performance of V-cycle methods in HyTeG

## Actions Taken
- **HPC Admin:** Granted access to the Fritz cluster.

## Lessons Learned
- Proper documentation of resource requirements and expected outcomes is crucial for efficient allocation and management of HPC resources.
- Benchmarking and performance analysis are common use cases for HPC clusters, requiring specific hardware and software configurations.

## Root Cause of the Problem
- User needed access to specific HPC resources for benchmarking purposes.

## Solution
- Access to the Fritz cluster was granted by the HPC Admin.

## Notes for Future Reference
- Ensure that users provide detailed information about their resource requirements and expected outcomes when requesting access to HPC resources.
- Regularly review and update access permissions to maintain security and efficient resource allocation.
---

### 2021020142001732_Jobs%20auf%20Emmy%201421531%2C1421532%20mpp3007h.md
# Ticket 2021020142001732

 ```markdown
# HPC Support Ticket: Jobs auf Emmy 1421531,1421532 mpp3007h

## Keywords
- Job efficiency
- Core utilization
- Script error
- HPC system

## Problem Description
- **Root Cause**: User's jobs showing extremely poor utilization of HPC resources. Only 1 core being used instead of the requested 40 cores.
- **Symptoms**: Low core utilization, inefficient job performance.

## Communication
- **HPC Admin**: Notified the user about the poor utilization and requested to check the script for errors.
- **User**: Acknowledged the issue and agreed to investigate.

## Solution
- **Action Taken**: User was advised to check the script for errors that might be causing the low core utilization.
- **Resolution**: The ticket was closed with the expectation that the user would address the issue.

## General Learnings
- Regularly monitor job performance to ensure efficient resource utilization.
- Script errors can lead to poor core utilization, impacting overall HPC system performance.
- Communicate with users to address and resolve inefficiencies promptly.
```
---

### 2022061442002501_Jobs%20auf%20Fritz%20nutzen%20nur%20den%20ersten%20Node%20%5Bbctc035h%5D.md
# Ticket 2022061442002501

 # HPC Support Ticket: Jobs auf Fritz nutzen nur den ersten Node

## Keywords
- Job scheduling
- VASP
- mpirun
- SLURM
- Node utilization
- Monitoring system

## Problem Description
- User's jobs on Fritz are only utilizing the first node for VASP calculations, leaving other requested nodes idle.
- Monitoring system shows only one node being used in both `cpu_load` and `flops_any` columns.

## Root Cause
- The job script contains the line `mpirun -np 72 $VASP > vasp.out 2> vasp.err`, which starts 72 processes all running on the first node (`#SBATCH --ntasks-per-node=72`).

## Solution
- Remove the `-np 72` argument from `mpirun`.
- Alternatively, pass the number of processes as a variable, e.g., `num=$((SLURM_NNODES*72))` and then call `mpirun -np $num`.

## Additional Information
- Users can log in to the monitoring system using their IdM credentials to view node/CPU utilization of their jobs.
- Ensure all job scripts are updated to avoid recurring issues.

## Follow-up
- HPC Admin confirmed that the user modified the job scripts, but one job (JobId 81093) still used only one node.
- Continued monitoring and script adjustments are necessary to ensure proper node utilization.

## Contact
- For further assistance, users can contact HPC support at [support-hpc@fau.de](mailto:support-hpc@fau.de).
- Additional resources available at [https://hpc.fau.de/](https://hpc.fau.de/).
---

### 42148815_MPI_Allreduce%20h%C3%83%C2%A4ngt.md
# Ticket 42148815

 # HPC Support Ticket: MPI_Allreduce Hangs

## Keywords
- MPI_Allreduce
- Hanging job
- Intel MPI
- Environment variable
- I_MPI_FABRICS

## Problem Description
- **Root Cause**: The job hangs during the `MPI_Allreduce` call with `MPI_SUM` operation when using a large number of nodes (32 or 64). The issue does not occur with smaller node counts (16).
- **Affected MPI Operations**: Only `MPI_Allreduce` with `MPI_SUM` is affected. Other operations like `MPI_MAX`, `MPI_MIN`, and `MPI_LOR` work fine.

## Solution
- **Suggested Fix**: Set the environment variable `I_MPI_FABRICS=shm:ofa` after loading the necessary modules. This change may improve the performance and stability of the MPI communication.

## General Learnings
- Large-scale MPI jobs can encounter issues that do not appear in smaller tests.
- The `I_MPI_FABRICS` environment variable can be used to optimize the communication fabric for Intel MPI.
- It is important to test MPI applications at the intended scale to catch potential issues early.

## Ticket Details
- **Job IDs**: 368485.ladm1, 368395.ladm1
- **Affected Software**: walberla/bin/sd_fs
- **MPI Implementation**: Intel MPI

## Related HPC Admins and Support Team
- **HPC Admins**: Provided the solution involving the `I_MPI_FABRICS` environment variable.
- **2nd Level Support Team**: Not explicitly involved in this ticket.
- **Other HPC Staff**: Not explicitly involved in this ticket.
---

### 2025022642002866_Tier3-Access-Fritz%20%22Florian%20Prohaska%22%20_%20mp24100h.md
# Ticket 2025022642002866

 # HPC Support Ticket Analysis: Tier3-Access-Fritz

## Keywords
- Access Grant
- Fritz
- Single-node Throughput
- Matlab
- Simulation/Optimization
- Publications

## Summary
- **User Request**: Access to Fritz for single-node throughput with special justification (72 cores, 250 GB).
- **Required Software**: Matlab.
- **Application**: Simulation/optimization of particle synthesis for CRC 1411; simulation/optimization of nonlocal traffic flow on networks.
- **Expected Outcome**: Publications.

## Root Cause
- User required access to Fritz for specific computational needs.

## Solution
- **HPC Admin Response**: Access granted to use Fritz.

## General Learnings
- Users may require access to specific HPC resources for specialized computational tasks.
- Access requests should include details about the required resources, software, and expected outcomes.
- HPC Admins can grant access based on the provided justification and resource availability.

## Additional Notes
- Ensure that access requests are processed promptly and that users are informed of their access status.
- Documentation of access requests and granted permissions is crucial for future reference and support.
---

### 42190939_Jobs%20auf%20LiMa.md
# Ticket 42190939

 # HPC Support Ticket: Jobs auf LiMa

## Keywords
- Job script
- PPN (Processors Per Node)
- Intel's mpiexec.hydra
- PBS (Portable Batch System)
- mpirun_rrze-intelmpd
- Hold status

## Problem
- User's jobs request 4 nodes but only 2 nodes are actively used.
- All 48 processes are running on the first two nodes.
- The `-ppn 12` option is not correctly evaluated by Intel's mpiexec.hydra in combination with `-rmk pbs`.

## Root Cause
- Incorrect job script configuration leading to inefficient resource utilization.

## Solution
- If the current performance is satisfactory, modify the job script to use `PPN=24` and request `-l nodes=2:ppn=24`.
- Alternatively, use `/apps/rrze/bin/mpirun_rrze-intelmpd -pin 0_1_2_3_4_5_6_7_8_9_10_11 ./a.out` to ensure exactly 12 processes are started on the 12 physical cores of a node.
- All currently pending jobs were put on hold and should be deleted.

## General Learning
- Ensure proper configuration of job scripts to efficiently utilize allocated resources.
- Understand the interaction between different options in job scripts and their impact on resource allocation.
- Be aware of alternative methods to launch MPI jobs to achieve desired process distribution.
---

### 2017050942002701_Performance%20pro%20Kern%3F.md
# Ticket 2017050942002701

 # HPC Support Ticket: Performance pro Kern?

## Keywords
- Performance pro Kern
- Prozessoren im HPC-Zoo
- tf-Broadwell-Knoten
- SSD
- Basistakt
- TurboMode

## Summary
A user inquired about the performance per core of different processors in the HPC-Zoo and whether there are significant differences. The HPC Admin provided a link to a blog post discussing performance variability and later specified the performance of tf05x nodes.

## Root Cause
- User needed information on the performance per core of different processors.
- User also inquired about the performance of tf-Broadwell nodes.

## Solution
- HPC Admin provided a link to a blog post discussing performance variability: [No Free Lunch](https://blogs.fau.de/zeiser/2013/07/15/no-free-lunch/).
- HPC Admin specified that tf05x nodes are among the fastest, with a base clock speed of 3.4 GHz and a TurboMode up to 3.7 GHz.

## General Learnings
- Performance per core can vary significantly among different processors.
- tf05x nodes are noted for their high performance with a base clock speed of 3.4 GHz and TurboMode up to 3.7 GHz.
- Users may need to consider specific nodes due to other requirements, such as SSD availability.

## References
- [No Free Lunch Blog Post](https://blogs.fau.de/zeiser/2013/07/15/no-free-lunch/)
- [HPC Services Website](http://www.hpc.rrze.fau.de/)
---

### 2023061842000101_Reservierung%20f0401%20f%C3%83%C2%BCr%2019._20.6..md
# Ticket 2023061842000101

 # HPC Support Ticket: Reservierung f0401 für 19./20.6.

## Keywords
- Reservation
- SLURM
- Node Configuration
- Port Forwarding
- hpc-mover
- CE Instance

## Summary
A user requested a reservation for a specific node (f0401) to run a CE instance for a workshop presentation. The HPC Admin provided the reservation details and adjusted the port forwarding. However, the user encountered issues with the reservation configuration.

## Root Cause
- The initial reservation for node f0113 did not work because the single-node partition did not support it by default.
- The user was unable to allocate the reserved node using the `salloc` command due to a configuration issue.

## Solution
- The HPC Admin adjusted the reservation to node f0401, which was available earlier than expected.
- The user was able to allocate the node f0401 successfully and proceed with the presentation.

## Lessons Learned
- Reservations must be explicitly requested and configured correctly.
- Node configurations and partition settings should be verified to ensure compatibility with reservations.
- Port forwarding adjustments may be necessary to ensure proper access to reserved nodes.
- Users should be aware of the specific commands and configurations required to allocate reserved nodes.

## Commands Used
- `scontrol show reservation`: To display reservation details.
- `salloc -N 1 --reservation=ce-f0401 --time=04:00:00`: To allocate the reserved node.

## Conclusion
Proper configuration and verification of reservations and node settings are crucial for successful allocation and usage. Adjustments to port forwarding and node configurations may be necessary to resolve issues.
---

### 2024090542000502_Dummyaccount%20%2B%20Reservierung%20saprap2%20f%C3%83%C2%BCr%20CLPE%20Tutorial%20am%2008.09..md
# Ticket 2024090542000502

 ```markdown
# HPC Support Ticket: Dummy Account and Node Reservation for CLPE Tutorial

## Keywords
- Dummy account
- Node reservation
- Test cluster
- CLPE Tutorial
- Account creation
- Node reservation commands

## Summary
A user requested the creation of a dummy account and the reservation of a specific node (saprap2) in the test cluster for a CLPE tutorial.

## User Request
- **Subject:** Dummyaccount + Reservierung saprap2 für CLPE Tutorial am 08.09.
- **Request:** Creation of a dummy account and reservation of the saprap2 node from September 7 to September 10.

## HPC Admin Actions
- **Account Creation:**
  ```bash
  # sacctmgr add account k_o16r
  # bin/add-user.sh o16r0000
  ```
- **Node Reservation:**
  ```bash
  # scontrol create reservation reservationname=CLPE starttime=now endtime=2024-09-11T00:00 user=o16r0000 nodes=saprap2 flags=IGNORE_JOBS,magnetic
  ```

## Outcome
- The HPC Admin created the dummy account and reserved the saprap2 node as requested.
- The user was informed that the account and password were provided via chat and that the $HOME directory would be available the next day.

## Lessons Learned
- **Account Creation:** Use `sacctmgr` and `add-user.sh` for creating accounts.
- **Node Reservation:** Use `scontrol create reservation` for reserving nodes, specifying the necessary flags and parameters.
- **Communication:** Ensure that the user is informed about the availability of resources and any delays.

## Root Cause
- The user needed a dummy account and node reservation for a specific tutorial.

## Solution
- The HPC Admin created the account and reserved the node as per the user's request, ensuring the resources were available for the tutorial.
```
---

### 42295847_Emmy.md
# Ticket 42295847

 # HPC Support Ticket: Emmy Priority Increase Request

## Keywords
- Account priority
- Project deadline
- Simulation results
- Cluster usage
- Temporary priority increase

## Summary
A user requested a temporary increase in account priority on the Emmy cluster due to an upcoming project deadline and the need for extensive simulation results.

## Root Cause
- User required more computational resources to meet project deadlines.

## Solution
- **HPC Admin** temporarily increased the priority of the user's account (`iwia45`) until the end of the week.
- Noted that the user had already utilized around 35% of the cluster on some days due to lower overall usage.

## Lessons Learned
- Users should include their account names in request emails for faster processing.
- Temporary priority increases can be granted to help users meet deadlines.
- Cluster usage statistics can vary, and users may already be utilizing significant resources.

## Action Taken
- Priority of the user's account was increased temporarily.
- User was informed about their previous cluster usage.

## Follow-Up
- Monitor the user's account to ensure the increased priority does not disrupt other users.
- Review cluster usage statistics to better understand resource allocation.
---

### 2020032442003214_VASP%20Jobs%20auf%20Meggie%20780575%20780574%20mptf07.md
# Ticket 2020032442003214

 # HPC Support Ticket Conversation Analysis

## Keywords
- VASP Jobs
- Memory Issues
- Tasks per Node (PPN)
- NCORE
- CPU Binding
- FFT Processes
- Job Optimization
- Debugging
- Software Upgrade

## Summary
The conversation revolves around optimizing VASP jobs on the HPC cluster. The user is experiencing memory issues and suboptimal performance with their current configuration. The HPC Admin provides suggestions for improving the job configuration and offers to debug the issue further.

## Root Cause of the Problem
- The user's job configuration with 15 tasks per node and NCORE=5 leads to inefficient FFT process distribution, causing performance issues.
- Insufficient memory errors occur when trying to increase the tasks per node to 20.

## Solutions and Suggestions
- **Job Configuration**: The HPC Admin suggests trying PPN=16 with NCORE=8 for better performance.
- **CPU Binding**: The admin clarifies that `--cpu-bind=v` does not activate CPU binding; `--cpu-bind=v,cores` is needed for that.
- **Debugging**: The admin offers to debug the job to understand the memory issues better.
- **Software Upgrade**: The admin inquires about upgrading to VASP 6.0.

## General Learnings
- Proper task and core configuration is crucial for optimal job performance.
- Understanding CPU binding flags is important for effective resource utilization.
- Debugging can help identify and resolve unexpected memory issues.
- Keeping software up to date can potentially improve performance and stability.

## Next Steps
- The user will test the suggested configurations and provide feedback.
- The admin will debug the job if the memory issues persist.
- The user will consider upgrading to VASP 6.0.

This analysis can serve as a reference for support employees encountering similar job optimization and memory issues on the HPC cluster.
---

### 2024121742003301_Fehlende%20Nutzungsdaten%20f%C3%83%C2%BCr%20Account.md
# Ticket 2024121742003301

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject
Fehlende Nutzungsdaten für Account

## Keywords
- Account Setup
- Usage Data
- Monitoring System
- ClusterCock
- New User Introduction
- HPC Systems
- AI Workloads
- Batch System
- Python Environments
- Apptainer Containers

## Problem
- User received a message stating "Keine Nutzungs-Daten für account [...] gefunden!" on their user page.
- User inquired if their account was correctly set up in the system.

## Root Cause
- The user had not yet used the HPC clusters, resulting in no usage data being available.

## Solution
- HPC Admin explained that the message indicates the user has not used the clusters.
- ClusterCock is a monitoring system for observing jobs.
- The user was informed about upcoming online HPC introductions for new users.

## General Learnings
- New users may see a message indicating no usage data if they have not used the HPC clusters.
- ClusterCock is used for monitoring job activity.
- New users should attend HPC introductions to understand system usage, data storage options, batch system, and AI-specific topics.

## Actions Taken
- HPC Admin provided information about the monitoring system and upcoming introduction sessions.
- The user was advised to attend the sessions to gain essential knowledge about the HPC systems.

## Recommendations
- Inform new users about the monitoring system and the meaning of the "no usage data" message.
- Encourage new users to attend introduction sessions to familiarize themselves with the HPC environment.
```
---

### 2018071342001958_ProPE%20Test%20II%3A%20HPCG%20L%C3%83%C2%B6ser%20Benchmark%20erreicht%20nicht%20maximale%20Bandbreit.md
# Ticket 2018071342001958

 # HPC Support Ticket: HPCG Benchmark Performance Issue

## Keywords
- HPCG Benchmark
- Speicherbandbreite (Memory Bandwidth)
- Intel Compiler
- MPI
- IvyBridge
- Broadwell
- HPC Counters

## Problem Description
The user attempted to run the HPCG Benchmark but could only achieve half of the expected maximum memory bandwidth. The benchmark was compiled with Intel 17.0up03 ICPC version 17.0.3 using the following flags:
- `HPCG_OPTS = -DHPCG_NO_OPENMP`
- `CXXFLAGS = $(HPCG_DEFS) -fast -xhost`

The user used the MPI-only variant and measured the bandwidth on IvyBridge and Broadwell nodes.

## Root Cause
The root cause of the problem was not identified by the local HPC Admins. The ticket was escalated to the ProPE team for further investigation due to lack of local expertise.

## Solution
No solution was provided in the ticket conversation. The ticket was closed as it was escalated to the ProPE team for further assistance.

## General Learnings
- The HPCG Benchmark is memory bandwidth bound.
- Intel Compiler version and flags used for compilation can affect performance.
- The issue might be specific to the hardware (IvyBridge, Broadwell) or the MPI-only variant of the benchmark.
- Local HPC Admins may escalate tickets to the ProPE team when they lack the necessary expertise to resolve an issue.
---

### 2024103042001292_Access%20to%20Alex%20and%20GDAL%20module.md
# Ticket 2024103042001292

 # HPC Support Ticket: Access to Alex and GDAL Module

## Keywords
- HPC infrastructure
- Cluster access (Alex, Fritz)
- GDAL module
- netCDF module
- Compute time budget
- GPU resources

## Problem Summary
- User unable to access the Alex cluster despite being told they had access.
- User unable to find GDAL and netCDF modules.

## Root Cause
- **Cluster Access**: The project v116bb only has a compute time budget for Fritz, not Alex.
- **Module Availability**: GDAL module is not preinstalled on Fritz.

## Solution
- **Cluster Access**: User's account will remain limited to Fritz unless there is a need for GPU resources.
- **Module Availability**: User can install GDAL from conda-forge or build it from source. Fritz has three versions of netCDF available.

## General Learnings
- Always check the project's compute time budget and allocated resources.
- If a module is not preinstalled, users can install it from other sources like conda-forge or build it from source.
- GPU resources are typically required for access to specific clusters.

## Actions Taken
- HPC Admins informed the user about the compute time budget and module availability.
- The request for Alex access was forwarded to the Compute-time team.
- The user was able to install GDAL on their own.

## Follow-up
- The user confirmed successful calculations and expressed satisfaction with the resources on Fritz.
- No further action is required regarding GDAL installation.
- Access to Alex will only be granted if GPU resources are needed.
---

### 2021073042000723_Performanceanalyse%20meines%20SPH%20Codes.md
# Ticket 2021073042000723

 # HPC Support Ticket Conversation Summary

## Subject: Performanceanalyse meines SPH Codes

### User Request
- User wants to test code performance on Meggie with different setups.
- Plans to use OpenMP, MPI, and hybrid configurations.
- Concerns about low node utilization with fewer threads.

### HPC Admin Response
- Suggested testing OpenMP/MPI on a single socket (1-10 threads/processes).
- Recommended using 2 processes per node with 10 threads each for hybrid tests.
- Advised on pinning threads/processes and combining experiments into a single job.

### User Follow-up
- User provided a SLURM script for testing.
- HPC Admin corrected the script, suggesting not to push processes to the background and using `-bind-to` instead of `-B`.
- Provided a loop example for running experiments serially.

### Performance Comparison
- User compared performance between Emmy and Meggie.
- HPC Admin explained the architectural differences and suggested running tests on Emmy for a direct comparison.

### User Issues
- User encountered "illegal instruction" errors on Emmy.
- Planned to recompile libraries for the correct architecture.

### HPC Admin Final Response
- Encouraged the user to resolve library issues and rerun tests on Emmy.
- Offered support and wished the user success.

### Key Learnings
- Importance of testing on a single socket to understand scaling behavior.
- Proper pinning of threads/processes for optimal performance.
- Architectural differences between Emmy and Meggie and their impact on performance.
- Handling "illegal instruction" errors by recompiling libraries for the correct architecture.

### Solution
- User should recompile libraries for the correct architecture and rerun tests on Emmy.
- Use the corrected SLURM script for testing on Meggie.
- Compare performance data between Emmy and Meggie to assess improvements.
---

### 2019090342001953_Issues%20with%20jobs%20on%20emmy%20_%20mpt4014h.md
# Ticket 2019090342001953

 # HPC Support Ticket: Issues with Jobs on Emmy

## Keywords
- Job allocation
- CPU nodes
- MPI processes
- mpirun
- Job script

## Problem Description
- User's jobs on Emmy were using only 8 of the 20 allocated CPU nodes.
- The mpirun command was configured to use 20 processes per node but only 160 processes in total.

## Root Cause
- The user's job script was not updated to match the allocated resources.

## Solution
- The user was advised to either adapt the number of nodes allocated in the job script or increase the number of MPI processes in the mpirun command.

## Lessons Learned
- Ensure that the job script and mpirun command are configured to utilize all allocated resources efficiently.
- Regularly review and update job scripts to avoid resource wastage.

## Actions Taken
- The HPC Admin provided links to job monitoring for the user to review.
- The user acknowledged the issue and agreed to update the job script.
- The ticket was closed after the user confirmed they would adjust the number of nodes and processes.

## References
- Job monitoring links:
  - [Job 1165692](https://www.hpc.rrze.fau.de/HPC-Status/job-info.php?USER=mpt4014h&JOBID=1165692&ACCESSKEY=a3fc4665&SYSTEM=EMMY)
  - [Job 1165693](https://www.hpc.rrze.fau.de/HPC-Status/job-info.php?USER=mpt4014h&JOBID=1165693&ACCESSKEY=4d4cf2e5&SYSTEM=EMMY)

## Conclusion
- Proper configuration of job scripts and mpirun commands is crucial for efficient resource utilization on HPC systems.
---

### 2023040342000151_f1009%20Reservierung%20und%20tempor%C3%83%C2%A4rer%20HPC%20Account.md
# Ticket 2023040342000151

 # HPC Support Ticket Analysis

## Subject
f1009 Reservierung und temporärer HPC Account

## Keywords
- Node Reservation
- Temporary HPC Account
- Compiler Explorer
- Container Setup
- Node Maintenance

## Summary
A user requested a node reservation and a temporary HPC account for a tutorial. The HPC Admin provided an account and adjusted the reservation due to potential node maintenance.

## Root Cause
- User needed specific node (f1009) for a tutorial.
- Node might be unavailable due to maintenance.

## Solution
- HPC Admin provided a temporary account.
- Reservation adjusted to a different node (f0401) to ensure availability.
- Reservation details:
  - ReservationName: compiler-explorer
  - StartTime: 2023-04-03T08:12:52
  - EndTime: 2023-04-17T12:00:00
  - Duration: 14-03:47:08
  - Nodes: f0401
  - NodeCnt: 1
  - CoreCnt: 72
  - TRES: cpu=72
  - Users: ihpc030h, y64o0000
  - State: ACTIVE

## Lessons Learned
- Always check node availability before making reservations.
- Be prepared to adjust reservations based on maintenance schedules.
- Provide temporary accounts for short-term projects or tutorials.

## Actions Taken
- Temporary account created.
- Reservation adjusted to an available node.
- User informed about the changes.

## Follow-up
- Ensure the user can access the temporary account.
- Verify the reservation is active and the node is available during the specified time.
---

### 2023110642001551_Tier3-Access-Fritz%20%22Riccarda%20Scherner-Grie%C3%83%C2%9Fhammer%22%20_%20iwia044h.md
# Ticket 2023110642001551

 ```markdown
# HPC Support Ticket Analysis: Tier3-Access-Fritz

## Keywords
- Tier3 Access
- Fritz
- Multi-node workload
- HDR100 Infiniband
- Intel gcc
- Intel VTune
- KONWIHR project
- Hotspot analysis
- Performance optimization
- Scalability analysis

## Summary
- **User Request**: Access to Fritz for multi-node workload with specific hardware and software requirements.
- **Hardware Requirements**: HDR100 Infiniband with 1:4 blocking, 72 cores per node, 250 GB memory per node.
- **Software Requirements**: Intel gcc, Intel VTune.
- **Project Details**: Part of the KONWIHR project focusing on performance optimization and parallelization of a code for solving partial differential equations on sparse grids.
- **Expected Outcomes**: Hotspot analysis, optimized performance, and scalability analysis.
- **Collaboration**: Work to be done with a colleague from NHR.

## Root Cause of the Problem
- User needed access to Fritz for specific computational tasks.

## Solution
- **HPC Admin Response**: Access granted to Fritz.

## General Learnings
- Proper documentation of user requirements and project details is crucial for efficient ticket handling.
- Collaboration with NHR colleagues should be noted for future reference.
- Ensure that users have access to the necessary hardware and software for their projects.
```
---

### 2024121042002511_Regarding%20slow%20speed%20in%20computing%20python%20scripts%20%28WOODY%29.md
# Ticket 2024121042002511

 # HPC Support Ticket: Slow Speed in Computing Python Scripts

## Keywords
- Python script
- SLURM
- Parallelization
- MDAnalysis
- Job monitoring
- Performance optimization

## Problem Description
The user reported that their Python script was taking much longer to run than usual. The job monitoring screenshot indicated that the jobs were using only one core, despite requesting 32 cores per node.

## Root Cause
The Python script provided by the user was not parallelized. The script was designed to run on a single core, which led to inefficient use of the allocated resources.

## Solution
1. **Reduce Resource Allocation**: Since the script is not parallelized, it is recommended to request only one core unless additional memory is required.
2. **Parallelization**: The user was advised to explore parallelization techniques for their script. A link to relevant documentation was provided: [MDAnalysis Custom Parallel Analysis](https://userguide.mdanalysis.org/stable/examples/analysis/custom_parallel_analysis.html).

## Lessons Learned
- **Resource Allocation**: Ensure that the resource allocation in the SLURM script matches the requirements of the job. Over-allocating resources can lead to inefficient use of HPC resources.
- **Parallelization**: For computationally intensive tasks, consider parallelizing the code to make better use of the available cores.
- **Job Monitoring**: Regularly monitor job performance to identify and address bottlenecks.

## Next Steps
- The user should review the provided documentation and consider parallelizing their script.
- If further assistance is needed, the user can reach out to the HPC support team for additional guidance.

## References
- [MDAnalysis Custom Parallel Analysis](https://userguide.mdanalysis.org/stable/examples/analysis/custom_parallel_analysis.html)

## Support Team
- **HPC Admins**: Thomas, Michael Meier, Anna Kahler, Katrin Nusser, Johannes Veh
- **2nd Level Support**: Lacey, Dane (fo36fizy), Kuckuk, Sebastian (sisekuck), Lange, Florian (ow86apyf), Ernst, Dominik (te42kyfo), Mayr, Martin
- **Datacenter Head**: Gerhard Wellein
- **Training and Support Group Leader**: Georg Hager
- **NHR Rechenzeit Support**: Harald Lanig
- **Software and Tools Developers**: Jan Eitzinger, Gruber
---

### 2019121042001102_Python_Siesta%20Job%20%28Emmy%2C%201197849%2C%20mpp3000h%29.md
# Ticket 2019121042001102

 # HPC Support Ticket: Python/Siesta Job (Emmy, 1197849, mpp3000h)

## Keywords
- Python/Siesta Job
- Emmy
- MPI process to core mapping
- OpenMPI
- Process binding
- Oversubscribing cores
- `--report-bindings`
- `--bind-to core`
- `--map-by ppr:1:core`

## Problem
- The user's job was only running on one of the two allocated nodes.
- The job was oversubscribing the 20 physical cores with 40 threads.

## Root Cause
- Incorrect MPI process to core mapping.

## Solution
- Add `--report-bindings` to the command line to check the bindings.
- Replace `mpirun -np 40 --map-by core` with `mpirun --report-bindings --bind-to core --map-by ppr:1:core`.

## General Learnings
- OpenMPI syntax may change, so process pinning issues might require updated commands.
- Proper MPI process to core mapping is crucial for efficient resource utilization.
- Use `--report-bindings` to diagnose binding issues.
- Use `--bind-to core` and `--map-by ppr:1:core` for better process binding with OpenMPI.
---

### 2019061242001371_Request%20High%20priority%20of%20running%20simulations%20on%20Emmy.md
# Ticket 2019061242001371

 # HPC Support Ticket: Request High Priority for Running Simulations

## Keywords
- High priority
- Simulations
- Emmy cluster
- Priority boost
- HPC username
- Queue status
- Compute time

## Summary
A user requested high priority for running simulations on the Emmy cluster due to an upcoming proposal deadline. The HPC admin provided a slight priority boost but noted that the user's job already had a high priority due to low recent compute time usage.

## Root Cause
- User needed to complete simulations quickly for a proposal deadline.
- User had only one job in the queue, which already had a high priority due to low compute time usage in the last 10 days.

## Solution
- HPC admin granted a slight priority boost for one week.
- User was advised to mention their HPC username in future requests to avoid confusion.

## What Can Be Learned
- Users can request priority boosts for urgent jobs, but the usefulness depends on their recent compute time usage and the current queue status.
- Including the HPC username in support requests helps avoid confusion.
- Low recent compute time usage can automatically increase job priority.

## Actions Taken by HPC Admin
- Granted a slight priority boost for one week.
- Checked the user's job status and recent compute time usage.
- Removed the priority boost after one week.

## Follow-Up
- None required, as the priority boost was removed after the specified time.
---

### 2019062742000674_Knotenallokation%20vs.%20MPI-Prozesszahl%2C%20sowie%20Speicherpeaks%20_%20mpp3006h.md
# Ticket 2019062742000674

 # HPC Support Ticket: Node Allocation vs. MPI Process Count and Memory Peaks

## Keywords
- Node allocation
- MPI process count
- Memory peaks
- Out-of-memory (OOM) Killer
- Quantum Espresso
- mpirun
- `-ppn` option

## Problem Description
- The user's jobs show a discrepancy between the number of requested nodes and the MPI process count.
- Some jobs experience sudden memory spikes, sometimes exceeding the available memory, leading to the OOM Killer terminating processes.
- Jobs are terminating with the error "Bad Termination of one of your application processes."

## Root Cause
- The user intentionally started jobs with fewer MPI processes than the nodes could handle, leading to an uneven distribution of processes across nodes.
- The reason for the increased memory usage is unknown, but it might be related to the Quantum Espresso code.

## Solution
- If the user needs to run fewer MPI processes due to memory constraints, they should explicitly specify the number of processes per node using the `-ppn` option with `mpirun`.
- Example: `mpirun -ppn 32`
- The user should monitor memory usage and adjust the number of MPI processes or requested nodes accordingly to avoid triggering the OOM Killer.

## Additional Notes
- The HPC Admin mentioned that the user's jobs might be terminating due to the OOM Killer.
- The user was advised to specify the number of processes per node to avoid an uneven distribution of MPI processes.

## Related Links
- [Job Info 1130963](https://www.hpc.rrze.fau.de/HPC-Status/job-info.php?USER=mpp3006h&JOBID=1130963&ACCESSKEY=9283801b&SYSTEM=EMMY)
- [Job Info 1130961](https://www.hpc.rrze.fau.de/HPC-Status/job-info.php?USER=mpp3006h&JOBID=1130961&ACCESSKEY=afce17d9&SYSTEM=EMMY)
- [Job Info 1129482](https://www.hpc.rrze.fau.de/HPC-Status/job-info.php?USER=mpp3006h&JOBID=1129482&ACCESSKEY=7448a2f7&SYSTEM=EMMY)

## Follow-up
- The user should investigate the memory usage of their jobs and adjust the number of MPI processes or requested nodes accordingly.
- If the problem persists, the user should contact HPC Support for further assistance.
---

### 2021120742002541_Performance.md
# Ticket 2021120742002541

 # HPC Support Ticket: Performance Variability

## Keywords
- Performance variability
- Benchmarking
- MPI configuration
- Hyper-threading
- Job script

## Problem Description
The user observed up to 20% variability in the runtime of identical programs during benchmarking. The user tested three different MPI configurations (Run A, Run B, Run C) with varying `mpiexec` commands. The goal was to determine the parallelizability of the program, and consistent performance was desired.

## Root Cause
- **Hyper-threading**: Run A likely used hyper-threading, leading to longer overall runtime.
- **MPI Configuration**: Different MPI configurations (`--bind-to hwthread`, `--map-by core`, `--map-by socket`) resulted in performance variations.

## Solution
- **Consistent Workload**: Ensure that each run performs the exact same amount of work, including the same number of iterations and random number generation.
- **IO Operations**: Minimize or account for I/O operations during the benchmarking phase.
- **MPI Configuration**: Choose a consistent MPI configuration that avoids hyper-threading and ensures optimal resource allocation.

## Lessons Learned
- Performance variability can be caused by different MPI configurations and hyper-threading.
- Consistent workload and minimal I/O operations are crucial for accurate benchmarking.
- Proper MPI configuration can help achieve more consistent performance.

## Recommendations
- Review and standardize MPI configurations for benchmarking.
- Monitor and minimize I/O operations during performance testing.
- Ensure that each benchmark run performs identical work to avoid variability.

## References
- Job scripts provided by the user.
- HPC Admin's analysis and recommendations.

## Next Steps
- Implement the recommended MPI configuration.
- Rerun benchmarks with consistent workload and minimal I/O.
- Monitor performance variability and adjust configurations as needed.
---

### 2025021442002871_Tier3-Access-Fritz%20%22Udaya%20Bhaskar%20Putta%22%20_%20iwst115h.md
# Ticket 2025021442002871

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject: Tier3-Access-Fritz "User" / iwst115h

### Keywords:
- Access Request
- Fritz
- Multi-node Workload
- HDR100 Infiniband
- Python
- Intel
- Paraview
- MPI Neko Code
- Performance Optimization
- Visualization

### Summary:
- **User Request:** Access to Fritz for multi-node workload with specific hardware and software requirements.
- **Hardware Requirements:** HDR100 Infiniband with 1:4 blocking, 72 cores, 250 GB per node.
- **Software Requirements:** Python, Intel, Paraview.
- **Compute Time:** 500 node hours.
- **Application:** Parallel execution of MPI Neko code, visualization in Paraview, analysis of simulation data.
- **Expected Outcomes:** Logfiles for visualization, efficient parallel code execution, detailed visual representation and analysis.

### HPC Admin Response:
- **Action Taken:** Access to Fritz enabled for the user's account (iwst115h).
- **Contact Information:** Provided contact details for further support.

### Lessons Learned:
- **Access Request Process:** Understanding the procedure for enabling access to HPC resources.
- **User Requirements:** Importance of documenting specific hardware and software needs for efficient resource allocation.
- **Support Communication:** Effective communication between users and HPC admins for access requests and support.

### Root Cause of the Problem:
- User required access to Fritz for specific computational tasks.

### Solution:
- Access to Fritz was granted by the HPC Admin.
```
---

### 2022120242002272_Kursaccounts%20HPC%20%2B%20Fritz-Reservierung%205.-7.12..md
# Ticket 2022120242002272

 # HPC Support Ticket Analysis

## Keywords
- HPC-Kursaccounts
- NLPE-Kurs PRACE LRZ
- Fritz-Reservierung
- Fritz-Knoten
- Reservation
- Accounts
- Nodes
- CoreCnt
- PartitionName
- Flags
- TRES
- State
- BurstBuffer
- Watts
- MaxStartDelay

## Summary
A user requested 70 HPC course accounts for an NLPE course with access to Fritz, along with a reservation of 50 Fritz nodes for three days.

## Problem
- User requested HPC course accounts and node reservations for a specific course and timeframe.

## Solution
- HPC Admin created the requested accounts and reserved the nodes as specified.
- Reservation details were provided for each day, including node names, core count, partition name, and other relevant information.

## What Can Be Learned
- Procedure for creating HPC course accounts with specific permissions.
- Process for reserving nodes for a specific group of accounts.
- Importance of providing detailed reservation information, including node names, core count, and partition details.

## Example Reservation Details
```
ReservationName=lrz-day1 StartTime=2022-12-05T09:00:00 EndTime=2022-12-05T17:00:00 Duration=08:00:00
Nodes=f[0401,0403,0405-0452] NodeCnt=50 CoreCnt=3600 Features=(null) PartitionName=multinode Flags=MAGNETIC
TRES=cpu=3600
Users=(null) Groups=(null) Accounts=k_w84b Licenses=(null) State=INACTIVE BurstBuffer=(null) Watts=n/a
MaxStartDelay=(null)
```

## Notes
- Ensure that reservations are made with the correct parameters and that the state is set to INACTIVE until the reservation is active.
- Verify that the accounts have the necessary permissions for the reserved nodes.
---

### 2024071842001624_Zugang%20Fritz%20-%20Tier3%20oder%20NHR.md
# Ticket 2024071842001624

 # HPC Support Ticket Conversation Analysis

## Keywords
- Tier3 Resources
- Woody
- SLURM
- Fritz
- CPU Hours
- Node Hours
- NHR Project
- Online Formular
- Lehrstuhlinhaber

## Summary
A user currently utilizing Tier3 resources (Woody) at FAU requests access to Fritz due to limitations in CPU resources on Woody. The user estimates a need for 500,000 CPU hours on Fritz by the end of the year.

## Root Cause
- Insufficient CPU resources on Woody for the user's simulations.
- User requires access to Fritz to reduce computation time.

## Solution
- The user is directed to fill out the Tier3 access form for Fritz.
- The HPC Admin indicates that the user's request for 500,000 CPU hours might exceed Tier3 provisions and suggests considering an NHR project if similar resource needs are expected in the future.

## What Can Be Learned
- **Access Request Process**: Users need to fill out the Tier3 access form for Fritz.
- **Resource Limits**: Tier3 resources may not suffice for extensive computational needs.
- **NHR Projects**: For substantial and ongoing resource requirements, an NHR project might be necessary.
- **Role of Lehrstuhlinhaber**: Not explicitly required for the access request, but involvement might be beneficial for larger projects.

## Action Items
- Direct users to the Tier3 access form for Fritz.
- Inform users about the potential need for an NHR project for extensive resource requirements.
- Consider involving the Lehrstuhlinhaber for larger projects.

## Additional Notes
- The user's experience with SLURM and realistic resource estimation is noted.
- The HPC Admin provides clear guidance on the next steps for the user.

---

This report can be used as a reference for support employees to handle similar requests for access to Fritz and to understand the process for managing extensive computational resource needs.
---

### 2023032042000881_Tier3-Access-Fritz%20%22Samuel%20Kemmler%22%20_%20iwia032h.md
# Ticket 2023032042000881

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject
Tier3-Access-Fritz "Samuel Kemmler" / iwia032h

## Keywords
- HPC Account Activation
- Multi-node Workload
- waLBerla (C++)
- Python
- Slurm Script
- Test Access

## Summary
- **User Request**: Access to HPC system for test purposes to prepare software and Slurm script for a student.
- **Resources Requested**:
  - Multi-node workload (HDR100 Infiniband with 1:4 blocking)
  - Per node: 72 cores, 250 GB
  - 10,000 node hours on Fritz
- **Software Needed**: waLBerla (C++), Python
- **Expected Outcome**: Working workflow for the student

## Root Cause of the Problem
- User required access to the HPC system for testing and preparation.

## Solution
- **HPC Admin Action**: The HPC account was activated on Fritz.
- **Notification**: The user was informed about the account activation.

## General Learnings
- Ensure that users requesting access provide clear details about their needs, including software requirements and expected outcomes.
- HPC Admins should promptly activate accounts and notify users to facilitate smooth testing and preparation processes.

## Additional Notes
- This ticket highlights the importance of clear communication between users and HPC Admins to ensure all necessary resources and permissions are granted.
```
---

### 2019121142000852_StarCCM%2B%20jobs%20on%20emmy%20-%20mfh3005h.md
# Ticket 2019121142000852

 # HPC Support Ticket: StarCCM+ Jobs on Emmy

## Subject
StarCCM+ jobs on emmy - mfh3005h

## Keywords
- StarCCM+
- Performance optimization
- Node reduction
- Scaling behavior
- Parallel efficiency
- Speedup
- Roofline diagrams

## Problem
- User's jobs on emmy using 64 nodes showed poor performance.
- Inefficient use of HPC resources due to large communication overhead.
- Long queue time for jobs with 64 nodes.

## Root Cause
- Too many processes leading to high communication overhead.
- Suboptimal scaling behavior of StarCCM+ with the current node configuration.

## Solution
- Reduce the number of nodes to improve performance and resource efficiency.
- Conduct simulations with different numbers of nodes to analyze scaling behavior.
- Calculate parallel efficiency and speedup to determine the optimal number of nodes.

## Actions Taken
1. **HPC Admin**:
   - Informed the user about the poor performance and suggested reducing the number of nodes.
   - Provided links to monitoring data for past jobs.
   - Requested feedback on scaling behavior and number of timesteps computed in a 24-hour period.

2. **User**:
   - Conducted simulations with different numbers of nodes (64, 54, 44, 34, 24, 14, and 1 node).
   - Collected data on the number of timesteps, clock frequency, and memory bandwidth.
   - Shared findings with HPC Admin for further analysis.

3. **HPC Admin**:
   - Analyzed the user's data and provided feedback on parallel efficiency and optimal node configuration.
   - Suggested using roofline diagrams for hardware metrics analysis.
   - Provided links to roofline diagrams for the user's recent simulations.

## Conclusion
- Optimal number of nodes for the user's case is around 20-30 based on parallel efficiency and scaling behavior.
- Using 44 nodes is in the saturation region and not recommended.
- Roofline diagrams can provide additional insights into hardware metrics.

## References
- [HPC Scaling Presentation](https://hpc.fau.de/files/2019/11/2019-11-12_HPC_Cafe_scaling.pdf)
- [Roofline Model](https://en.wikipedia.org/wiki/Roofline_model)
- [Job Roofline Diagrams](https://www.hpc.rrze.fau.de/JobRoofline.EMMY)
---

### 2023110742000783_Tier3-Access-Fritz%20%22Nico%20Nees%22%20_%20mp24007h.md
# Ticket 2023110742000783

 ```markdown
# HPC Support Ticket: Tier3-Access-Fritz

## Summary
- **User Request**: Access to Fritz for multi-node workload using Matlab.
- **Issue**: Matlab Parallel Server not available on Fritz.
- **Solution**: Inform user about the limitation.

## Details
- **User Requirements**:
  - Multi-node workload (HDR100 Infiniband with 1:4 blocking; per node: 72 cores, 250 GB).
  - 35000 node hours on Fritz.
  - Required software: Matlab.
  - Application: Simulations of optical system for CRC 1411.
  - Expected results: Publications.

- **HPC Admin Response**:
  - Account activated for Fritz.
  - Notification: Matlab Parallel Server not available on Fritz, limiting Matlab simulations to a single node.

- **User Acknowledgment**:
  - User acknowledged the information and thanked the HPC Admin.

## Keywords
- Fritz access
- Matlab Parallel Server
- Multi-node workload
- Simulations
- Optical system
- CRC 1411
- Publications

## Lessons Learned
- **Software Limitations**: Always inform users about software limitations on specific clusters.
- **User Communication**: Clear and prompt communication helps in managing user expectations.

## Root Cause
- Matlab Parallel Server not available on Fritz, limiting multi-node simulations.

## Solution
- Inform the user about the limitation and suggest alternative solutions if available.
```
---

### 2024010942002901_Reservierung%201%20Knoten%20Fritz%20f%C3%83%C2%BCr%20Gromacs-Energiemessungen.md
# Ticket 2024010942002901

 ```markdown
# HPC Support Ticket: Reserving a Node for Gromacs Energy Measurements

## Keywords
- Reservation
- Gromacs
- Energy Measurements
- Node Reservation
- Fritz Knoten
- scontrol

## Summary
A user requested a reservation for a Fritz node to conduct Gromacs energy measurements. The duration was estimated to be longer than two days, potentially until the end of the week.

## Root Cause
The user needed a dedicated node for Gromacs energy measurements but was unsure about the exact duration.

## Solution
The HPC Admin team created a reservation for the user. The reservation was set to start the next day due to current node availability.

## Actions Taken
1. **Reservation Request**: The user requested a node reservation for Gromacs energy measurements.
2. **Admin Response**: The HPC Admin team acknowledged the request and created a reservation using the `scontrol` command.
3. **Reservation Details**:
   ```
   scontrol create reservation reservationname=anna-gr starttime=2024-01-10T08:00 endtime=2024-01-13T12:00 user=unrz007h nodes=f1027 flags=magnetic
   ```

## Lessons Learned
- Users may need node reservations for specific tasks like energy measurements.
- The `scontrol` command is used to create reservations.
- Reservations may need to be scheduled based on current node availability.

## Follow-up
Ensure the user is aware of the reservation details and confirm the start and end times.
```
---

### 42128011_Error%20in%20ORCA%20%3AS.md
# Ticket 42128011

 # HPC Support Ticket: Error in ORCA Calculations

## Keywords
- ORCA
- std::bad_alloc
- Memory allocation error
- MPI
- mpirun
- SCF module error
- Aborted signal
- Resource allocation

## Problem Description
- User encountered `std::bad_alloc` error in all ORCA calculations.
- Increasing the number of processors did not resolve the issue.
- Error log indicates memory allocation failure.

## Root Cause
- Insufficient memory allocation due to improper MPI configuration.
- The `-np 8` parameter in the `mpirun` command restricted the job to use only 8 CPUs out of the 72 available.

## Solution
- Remove the `-np X` parameter to allow the job to use all available CPUs.
- Use the `-npernode 2` parameter to double the memory available to each process by utilizing every second CPU.

## Lessons Learned
- Always include detailed information in error reports, such as scripts used and complete output (stdout+stderr).
- Avoid specifying the `-np` parameter in `mpirun` to ensure all available resources are utilized.
- Memory allocation issues can often be resolved by adjusting MPI parameters to optimize resource usage.

## Example Command
```bash
mpirun -npernode 2 /apps/ORCA/2.8.0.1/amd64/orca_scf_mpi 2-2-lat.gbw b
```

## Additional Notes
- The error occurred in the SCF module of ORCA.
- Proper resource allocation is crucial for avoiding memory-related errors in HPC jobs.
---

### 2022102542001573_srun%20likwid-perfctr%20auf%20testcluster.md
# Ticket 2022102542001573

 # HPC Support Ticket Conversation Summary

## Subject: srun likwid-perfctr auf testcluster

### Keywords:
- SLURM
- srun
- likwid-perfctr
- CPU frequency
- CPU affinity
- Git repository checkout
- Nsight Compute
- FLOPS measurement

### General Learnings:
- **SLURM Resource Allocation**: Be specific with resource requests in SLURM. Use `--exclusive` and specify the number of CPUs with `-c`.
- **CPU Frequency with LIKWID**: Use `likwid-setFrequencies` for setting CPU frequency and reset it after use.
- **Git Repository Checkout**: Large repositories can take a long time to check out. Cleaning up artifacts can speed up the process.
- **Nsight Compute Lock File**: Ensure proper permissions for lock files in `/tmp`.
- **FLOPS Measurement**: Intel Haswell architecture does not support accurate FLOPS measurement. Use `FLOPS_AVX` group for pure AVX code.

### Root Causes and Solutions:

1. **CPU Affinity Issue**:
   - **Root Cause**: Insufficient CPU resources allocated in SLURM.
   - **Solution**: Use `salloc -t 04:00:00 -C hwperf --exclusive -w broadep2 -c 72` to allocate sufficient resources.

2. **Git Repository Checkout Time**:
   - **Root Cause**: Large artifacts in the repository directory.
   - **Solution**: Clean up artifacts to reduce checkout time.

3. **Nsight Compute Lock File**:
   - **Root Cause**: Lock file created by another user without proper permissions.
   - **Solution**: Ensure the lock file has write permissions for the group.

4. **FLOPS Measurement on Haswell**:
   - **Root Cause**: Haswell architecture does not support accurate FLOPS measurement.
   - **Solution**: Use `FLOPS_AVX` group for pure AVX code. For mixed code, FLOPS measurement is not accurate.

### Additional Notes:
- Use `sinfo -o "%.14n %.4c"` to get the number of CPUs per node.
- For CI jobs, consider using a ZIP download of the latest commit to speed up the checkout process.
- Always reset CPU frequencies after use with `likwid-setFrequencies -reset -ureset`.
---

### 2022111542003052_Tier3-Access-Fritz%20%22Christoph%20Naeger%22%20_%20iwpa056h.md
# Ticket 2022111542003052

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject: Tier3-Access-Fritz "Christoph Naeger" / iwpa056h

### Keywords:
- Account Activation
- Tier3 Access
- Resource Allocation
- Software Requirements
- Simulation
- Aeroacoustic Case

### Summary:
- **User Request:** Access to HPC resources for aeroacoustic simulations.
- **Resource Requirements:** Single-node throughput (72 cores, 250 GB), multi-node workload (HDR100 Infiniband with 1:4 blocking; per node: 72 cores, 250 GB).
- **Compute Time:** 1000 node hours on Fritz.
- **Software:** openFoam, StarCCM, Python.
- **Application:** Simulate aeroacoustic case and compare with experimental data.
- **Expected Results:** Good agreement with experimental data and deeper insight into physics.

### HPC Admin Response:
- **Action:** Account activated on Fritz.
- **Note:** Total number of nodes available for iwpa remains unchanged.

### Root Cause of the Problem:
- User required access to HPC resources for specific simulations.

### Solution:
- Account activation on Fritz with specified resource allocation.

### General Learnings:
- Proper documentation of user requests and admin responses is crucial.
- Ensure resource allocation does not exceed the available quota.
- Maintain clear communication regarding account status and resource availability.
```
---

### 42173373_NWChem%20on%20Lima.md
# Ticket 42173373

 # NWChem on Lima Cluster

## Keywords
- NWChem
- Lima cluster
- Parallel computation
- LRZ account
- SuperMUC
- GA communications
- InfiniBand configurations

## Problem Description
- User unable to run NWChem in parallel on more than one node on Lima cluster.
- NWChem installation used was compiled by another user for a different cluster.

## Root Cause
- Potential compatibility issues with the NWChem installation.
- Lack of specific manual or documentation for running NWChem on Lima.

## Support Interaction
- HPC Admin confirmed that they do not have a solution for running NWChem on Lima.
- User's LRZ account was activated, but NWChem had issues on SuperMUC and LRZ Linux cluster.
- HPC Admin suggested using NWChem at LRZ if possible.

## Solution
- No direct solution provided by HPC Admin.
- User advised to continue communication with LRZ support for a potential resolution.

## General Learnings
- Importance of cluster-specific documentation and manuals.
- Challenges in running software across different HPC environments.
- Coordination with other HPC centers (e.g., LRZ) for software support.

## Next Steps
- User to continue troubleshooting with LRZ support.
- If unsuccessful, user may need to revisit the issue with HPC Admin.

## Additional Notes
- HPC Admin acknowledged limited resources compared to larger centers like LRZ.
- User expressed concern about the project's requirements and the need for a working NWChem installation.
---

### 2024051342003546_MPI%20process%20binding%20-%20b133ae22.md
# Ticket 2024051342003546

 ```markdown
# MPI Process Binding Issue

## Keywords
- MPI pinning
- Environment variables
- mpirun
- srun
- --cpu_bind=cores
- --distribution=cyclic:cyclic
- Process binding

## Problem Description
- **Root Cause:** User's script called for 48 CPUs per node, leading to uneven distribution of MPI processes across the two sockets of the node.

## Solution
- **Suggested Fix:** Use `mpirun` or `srun` with the options `--cpu_bind=cores` and `--distribution=cyclic:cyclic` to ensure even distribution of processes.
- **Verification:** Check the binding using the options described in the [documentation](https://doc.nhr.fau.de/sdt/mpi/?h=bindin#show-process-binding).

## General Learning
- Ensure proper MPI process binding to avoid uneven distribution across sockets.
- Utilize `mpirun` or `srun` with appropriate options to manage process distribution.
- Verify process binding using available tools and documentation.
```
---

### 2024101142002442_Short-running%20jobs%20on%20Fritz%20%5Bb168dc13%5D.md
# Ticket 2024101142002442

 # HPC Support Ticket: Short-running Jobs on Fritz

## Keywords
- Short-running jobs
- Job bundling
- CPU utilization
- Memory usage
- Code efficiency
- Performance optimization

## Problem Description
- User submitted around 1500 jobs with a runtime of below 5 minutes.
- Low CPU utilization despite specifying `OMP_NUM_THREADS=72`.
- CPU load metric above the dashed line, indicating more tasks than specified.
- Inefficient memory usage and low memory bandwidth.

## Root Cause
- Short-running jobs increase the workload on the system.
- Inefficient code leading to low CPU and memory utilization.
- Fluctuating load due to waiting processes.

## Solution
- **Job Bundling**: Bundle short-running jobs into a single job to reduce system workload.
- **Code Optimization**: Improve code efficiency to increase CPU and memory utilization.
- **Monitoring**: Regularly check job performance and make adjustments as needed.

## Lessons Learned
- Short-running jobs should be bundled to reduce system overhead.
- Efficient use of CPU and memory resources is crucial for optimal performance.
- Regular communication and monitoring can help identify and address performance issues.
- Offer support and guidance to users to improve their code and job execution.

## Follow-up
- User confirmed code improvements and overhauled specific calculations.
- CPU utilization improved from 60% to 80-100%.
- Further performance improvements can be discussed with the HPC support team.

## Additional Notes
- Encourage users to respond to support inquiries for better assistance.
- Offer training and support resources to help users optimize their code and job submissions.
---

### 2019092042001224_Process%20Pinning%20for%20Hybrid%20MPI_Openmp%20Application.md
# Ticket 2019092042001224

 # Process Pinning for Hybrid MPI/OpenMP Application

## Keywords
- Process Pinning
- MPI
- OpenMP
- IntelMPI
- Hyperthreading
- Benchmarking

## Problem
- User wants to place one MPI process per node and let this process use 40 OpenMP threads.
- User is unsure about the correct way to launch the application and seeks tips for better placement.

## Conversation Summary
- User provides an example of how they launch the application using IntelMPI.
- HPC Admin suggests that `I_MPI_PIN_DOMAIN` is unnecessary when running one MPI process per node.
- HPC Admin provides an alternative command for running one process per socket using all hyperthreads.
- HPC Admin advises that the best configuration of processes vs. threads and whether to use hyperthreading is problem-dependent and suggests running benchmark experiments.

## Solution
- For one MPI process per node:
  ```bash
  mpirun -np 10 -ppn 1 -genv OMP_NUM_THREADS 40 -genv KMP_AFFINITY scatter $Exec $Parameters
  ```
- For one process per socket using all hyperthreads:
  ```bash
  mpirun -np 20 -ppn 2 -genv OMP_NUM_THREADS 20 -genv KMP_AFFINITY scatter -genv I_MPI_PIN_DOMAIN socket $Exec $Parameters
  ```
- Run benchmark experiments to determine the optimal setting for the specific application.

## General Learning
- Understanding the correct usage of `I_MPI_PIN_DOMAIN` for different process placements.
- Importance of benchmarking to find the optimal configuration for hybrid MPI/OpenMP applications.
- Adjusting the number of processes and threads based on the hardware and application requirements.
---

### 2025011842000474_Libfabric%20PSM2%20Timeout%20Issue%20on%20Meggie.md
# Ticket 2025011842000474

 # HPC-Support Ticket: Libfabric PSM2 Timeout Issue on Meggie

## Keywords
- Libfabric
- PSM2
- Timeout
- Meggie
- FI_PSM2_CONN_TIMEOUT

## Issue Description
User encountered a timeout issue on Meggie with the following error message:
```
libfabric:2213020:psm2:av:psmx2_epid_to_epaddr():230<warn>
psm2_ep_connect returned error Operation timed out, remote epid=1920b02.
```
The error suggests that the connection timed out after 5 seconds.

## Root Cause
The timeout error is due to the `FI_PSM2_CONN_TIMEOUT` setting being too low (currently set to 5 seconds).

## Solution
Increase the value of `FI_PSM2_CONN_TIMEOUT` to a larger value to allow more time for the connection to be established.

## Ticket History
- User reported the issue and attached an error log file.
- Issue was diagnosed as a timeout error related to the `FI_PSM2_CONN_TIMEOUT` setting.

## Follow-up
- If the issue persists after increasing the timeout value, further investigation is needed to determine why the connection is taking too long to establish.
- Consider involving HPC Admins or 2nd Level Support team if the issue is not resolved.

## Related Parties
- HPC Admins: Thomas, Michael Meier, Anna Kahler, Katrin Nusser, Johannes Veh
- 2nd Level Support team: Lacey, Dane (fo36fizy), Kuckuk, Sebastian (sisekuck), Lange, Florian (ow86apyf), Ernst, Dominik (te42kyfo), Mayr, Martin
- Datacenter Head: Gerhard Wellein
- Training and Support Group Leader: Georg Hager
- NHR Rechenzeit Support: Harald Lanig
- Software and Tools developers: Jan Eitzinger, Gruber
---

### 2021040942001009_Your%20job%20on%20Emmy%20%281447063%20mpp3000h%29.md
# Ticket 2021040942001009

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject: Your job on Emmy (1447063 mpp3000h)

### Keywords:
- Job execution
- Node allocation
- Certificate expiration
- User error

### Summary:
- **Root Cause**: User's job running on only one of two requested nodes.
- **Solution**: Encourage the user to be more careful in job submissions.

### Details:
- **HPC Admin**: Notified the user that their job is running on only one of the two requested nodes.
- **Action**: Advised the user to be more careful in their job submissions.

### General Learning:
- Ensure job submissions are correctly configured to utilize all requested resources.
- Regularly check job statuses to identify and correct any resource allocation issues.
```
---

### 2023071242000674_ORCA%20auf%20Fritz%20-%20n100af.md
# Ticket 2023071242000674

 # HPC Support Ticket: ORCA Performance Issue on Fritz

## Keywords
- ORCA
- OpenBLAS
- Intel Processors (ICX, SPR)
- OPENBLAS_CORETYPE
- SkylakeX
- Performance Optimization

## Problem
- **Root Cause**: ORCA versions 5.0.3 and 5.0.4, using OpenBLAS 0.3.15, do not correctly detect the microprocessor architecture on modern Intel processors (ICX and SPR). This results in the use of an incorrect/old optimization, as indicated by the line "OpenBLAS 0.3.15 USE64BITINT DYNAMIC_ARCH NO_AFFINITY Prescott SINGLE_THREADED" in the ORCA output.

## Solution
- **Fix**: Set the environment variable `OPENBLAS_CORETYPE=SkylakeX` explicitly in the job script before the ORCA call. This can be done by adding the line `export OPENBLAS_CORETYPE=SkylakeX` to the job script.

## Observations
- **Performance Improvement**: Setting the `OPENBLAS_CORETYPE` variable resulted in a speedup factor of 1.1 to 1.5 for the user's ORCA calculations. Benchmarks for another user showed a speedup factor of 1.4 to 1.7 for specific ORCA settings.

## Actions Taken
- **HPC Admins**: Requested user feedback on performance improvement after setting the environment variable.
- **User**: Confirmed performance improvement.
- **HPC Admins**: Implemented the environment variable setting automatically through the module on Fritz for all users.

## General Learning
- **Environment Variables**: Setting specific environment variables can significantly improve the performance of applications like ORCA on modern hardware.
- **User Feedback**: Important for validating performance improvements before implementing changes system-wide.
- **Automation**: Once validated, performance improvements can be automated through module files for all users.

## Future Reference
- For similar performance issues with ORCA or other applications using OpenBLAS, check if setting the `OPENBLAS_CORETYPE` environment variable improves performance.
- Always validate performance improvements with user feedback before making system-wide changes.
---

### 2020072942000666_cshpc%20langsam.md
# Ticket 2020072942000666

 ```markdown
# HPC Support Ticket: Slow Performance on cshpc

## Keywords
- Slow performance
- NoMachine
- cshpc
- gnome-shell
- CPU usage
- Memory usage
- Process management

## Problem Description
- User reported slow performance when logging into cshpc via NoMachine.
- Observed multiple `gnome-shell` processes consuming significant CPU and memory resources.
- Suspected abnormal behavior of `gnome-shell` processes.

## Root Cause
- Multiple `gnome-shell` processes were running and consuming excessive resources.

## Solution
- HPC Admins cleaned up the system, likely by terminating the problematic `gnome-shell` processes.

## Lessons Learned
- Regular monitoring of system processes can help identify and resolve performance issues.
- Abnormal behavior of system processes, such as `gnome-shell`, can significantly impact performance.
- Cleaning up unnecessary or abnormal processes can improve system performance.

## Actions Taken
- HPC Admins investigated and resolved the issue by cleaning up the system.
- User confirmed that the system performance improved after the cleanup.

## Follow-up
- Monitor system processes regularly to prevent similar issues in the future.
- Educate users on identifying and reporting abnormal system behavior.
```
---

### 2019052042002418_Taktfrequenz%20auf%20Meggie%20setzen.md
# Ticket 2019052042002418

 ```markdown
# HPC Support Ticket: Setting CPU Frequency on Meggie

## Keywords
- CPU Frequency
- srun
- sbatch
- OpenMP
- MPI
- --cpu-freq
- kilohertz
- interactive job

## Problem Description
The user attempted to set the CPU frequency on Meggie using the `--cpu-freq` option but failed to enforce the frequency setting. The user tried various values such as 'low', 'high', 1.2 GHz, and 2.0 GHz, but the actual frequency remained around 2.4 GHz.

## Root Cause
- The user did not use `srun` to start the job, which is necessary for properly applying the requested frequency.
- The `--cpu-freq` parameter requires the frequency in kilohertz.

## Solution
- Use `srun` instead of `sbatch` to start the job, as `sbatch` does not properly apply the requested frequency.
- Set the frequency in kilohertz using the `--cpu-freq` parameter. For example, to set the frequency to 2.2 GHz, use `--cpu-freq=2200000`.
- Available frequencies are from 1200000 to 2200000 in 100k increments.

## Additional Notes
- For OpenMP codes, it is unclear if `srun -N 1 ./a.out` is the correct solution. Additional parameters such as `--mpi=none` or `--ntasks=...` might be necessary.
- The certificate has expired, which might affect the communication or job submission process.

## Example Command
```bash
srun -N 1 --cpu-freq=2200000 ./a.out
```
```
---

### 2022120942001233_Jobs%20auf%20Woody%20nutzen%20nur%20einen%20Core%20-%20bcml001h.md
# Ticket 2022120942001233

 # HPC Support Ticket Conversation Analysis

## Keywords
- Python jobs
- Core utilization
- Job script configuration
- Account expiration
- Cluster access
- IdM-Kennung

## Summary
A user's Python jobs on the Woody cluster were requesting four cores but only utilizing one. The HPC Admin advised the user to either modify the Python code to use multiple cores or request only one core. The user also inquired about extending their cluster access and status as a contact person due to a change in their employment contract.

## Root Cause
- The user's Python jobs were configured to request four cores but were running serially, utilizing only one core.

## Solution
- The user adjusted the job script to request only one core since modifying the Python code was not immediately feasible.

## Additional Information
- The user's HPC account is tied to their status as a PhD student, so the account remains active despite changes in their employment contract.
- For other services, the user can apply for an IdM-Kennung.

## General Learnings
- Ensure that job scripts are configured correctly to utilize the requested resources.
- Understand the account policies and how they are tied to the user's status within the institution.
- Provide guidance on how to extend access or apply for additional services when users' employment status changes.

## Related Parties
- HPC Admins
- 2nd Level Support Team
- Head of the Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support and Applications for Grants
- Software and Tools Developer
---

### 2023091442003584_%5BFRASCAL%20Day%5D%20Reservierung%20Fritz%20Knoten%20f%C3%83%C2%BCr%20Demo.md
# Ticket 2023091442003584

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject: [FRASCAL Day] Reservierung Fritz Knoten für Demo

### Keywords:
- FRASCAL Day
- Reservation
- Fritz Knoten
- LIKWID Demo

### Summary:
- **User Request**: The user requested a reservation for a node on the Fritz cluster for a LIKWID demo during the FRASCAL Day event.
- **Event Details**: The event is scheduled from 9:30 to 16:30.
- **Reason for Request**: The user anticipates that the Fritz cluster might be busy and wants to ensure availability for the demo.

### Root Cause:
- The user needs a guaranteed node reservation to avoid potential unavailability during a scheduled event.

### Solution:
- The user should be directed to the appropriate HPC Admin to process the reservation request.
- Ensure the reservation is confirmed and communicated back to the user.

### General Learnings:
- **Event Planning**: Always plan ahead for node reservations during scheduled events to avoid conflicts.
- **Communication**: Clear communication with HPC Admins is crucial for ensuring resource availability.
- **Resource Management**: Understanding the cluster's usage patterns can help in better planning for such events.
```
---

### 2020041542003579_Meggie%20Jobs%20790128%2C%20790127%20nfcc004h.md
# Ticket 2020041542003579

 ```markdown
# HPC Support Ticket: Meggie Jobs 790128, 790127 nfcc004h

## Keywords
- Job Hanging
- MPI Error
- Internal MPI Error
- MPI_Init
- Fatal Error
- OUT File Empty
- No CRASH File

## Summary
- **Issue**: User's jobs on Meggie are hanging.
- **Symptoms**:
  - OUT file is empty.
  - No CRASH file is generated.
  - Error message in `.o` file: `Fatal error in MPI_Init: Internal MPI error!`
- **Affected Jobs**: 790128, 790127, and possibly others.

## Conversation Highlights
- **HPC Admin**: Notified the user about the hanging jobs and requested a check.
- **User**: Confirmed the issue and noted the MPI error in the `.o` file.
- **HPC Admin**: Acknowledged the issue and mentioned that another admin (Thomas Zeiser) is already investigating.

## Root Cause
- Internal MPI error during `MPI_Init`.

## Solution
- **In Progress**: Another HPC Admin (Thomas Zeiser) is investigating the issue.

## Lessons Learned
- **Job Monitoring**: Regularly check job status and output files for errors.
- **Error Reporting**: Use tickets for reporting and tracking issues.
- **MPI Troubleshooting**: Look for specific MPI error messages in output files.

## Next Steps
- **Follow-up**: Await the investigation results from the HPC Admin.
- **Documentation**: Update the knowledge base with the resolution once the issue is fixed.
```
---

### 2023031342001161_Tier3-Access-Fritz%20%22Calvin%20Kr%C3%83%C2%A4mer%22%20_%20mpt1013h.md
# Ticket 2023031342001161

 # HPC Support Ticket Analysis

## Keywords
- Tier3 Access
- Rechenzeitbedarf
- Large-Scale NHR-Projekt
- Cut-off Termin
- Quantum Monte Carlo
- Multi-node workload
- HDR100 Infiniband
- Intel MPI
- Critical points
- Critical exponents

## Summary
- **User Request**: Access to Tier3 with a significant computational need for quantum Monte Carlo simulations.
- **Issue**: Requested compute time exceeds Tier3 capacity.
- **Solution**: Redirected to apply for Large-Scale NHR-Projekt.

## Detailed Analysis
- **Root Cause**: User requested 100,000 node-hours, which translates to 14.4 million core-hours, exceeding Tier3 capacity.
- **HPC Admin Response**: Informed user about the capacity limits and suggested applying for a Large-Scale NHR-Projekt. Provided the link to application rules and the next cut-off date.
- **Resolution**: User's request was adjusted to a lower compute time, and both accounts were activated on Fritz.

## General Learnings
- Understand the capacity limits of Tier3 and redirect large requests to appropriate channels.
- Provide clear instructions and links for applying to Large-Scale NHR-Projekt.
- Ensure users are aware of the application deadlines and procedures for large-scale projects.

## Action Items
- **HPC Admins**: Continue to monitor and adjust user requests based on available resources.
- **2nd Level Support**: Assist users in understanding the application process for large-scale projects.
- **Training and Support Group**: Offer workshops or sessions on how to apply for large-scale projects and manage computational resources effectively.
---

### 2024100942001859_Tier3-Access-Fritz%20%22Kajol%20Kulkarni%22%20_%20iwia113h.md
# Ticket 2024100942001859

 # HPC Support Ticket Analysis: Tier3-Access-Fritz

## Keywords
- Tier3 Access
- Fritz Cluster
- Multi-node Workload
- Profiling Tools (Vampir, score-P)
- OpenMPI
- CMake
- waLBerla Application
- Communication Overhead
- Parallel Efficiency

## Summary
A user requested access to the Fritz cluster for a multi-node workload. The request included specifications for the required resources and software tools. The user intended to perform profiling and trace analysis for the waLBerla application and evaluate communication overhead and parallel efficiency.

## Root Cause of the Problem
The user needed access to the Fritz cluster to perform specific computational tasks and profiling.

## Solution
The HPC Admin granted the user access to the Fritz cluster with the specified account.

## What Can Be Learned
- **Access Request Process**: Understanding the process of requesting access to specific HPC resources.
- **Resource Specification**: Importance of clearly specifying the required resources and software tools in the access request.
- **Profiling Tools**: Familiarity with profiling tools such as Vampir and score-P for performance analysis.
- **Application Analysis**: Techniques for evaluating communication overhead and parallel efficiency in applications like waLBerla.

## Additional Notes
- Ensure proper documentation and communication when granting access to HPC resources.
- Provide clear instructions on how to use profiling tools and analyze application performance.

---

This report can serve as a reference for future support cases involving access requests and performance analysis on HPC clusters.
---

### 2024092442003778_allocated%20resources%20are%20utilized%20partially%20-%20c105aa11.md
# Ticket 2024092442003778

 # HPC-Support Ticket Conversation Summary

## Subject: allocated resources are utilized partially - c105aa11

### Key Points Learned:
- **Exclusive Node Allocation**: Fritz compute nodes are allocated exclusively. Allocating even one core results in the entire node (72 cores) being allocated for the job.
- **Job Arrays**: Job arrays do not run concurrently on the same node. Each job utilizes 8 cores on each node, leaving 64 cores idle.
- **Sequential `srun` Execution**: `srun` commands are blocking and run sequentially.
- **Performance Monitoring**: Clustercockpit can be used to monitor jobs and performance metrics.

### Root Cause of the Problem:
- User's job scripts were not efficiently utilizing the allocated resources due to the exclusive node allocation policy.
- Each job in the array was using only 8 cores, leaving 64 cores idle on each node.

### Solution:
- **Bundling Jobs**: Bundle multiple array jobs into one job and use loops to execute them. Each `srun` inside the loop should be terminated with an ampersand (`&`) to run them concurrently.
- **Monitoring**: Use Clustercockpit to monitor job performance and resource utilization.
- **Script Adjustments**: Ensure the job script is correctly placing the `wait` command after each loop to manage concurrent execution properly.

### Additional Notes:
- **Performance Charts**: The performance charts showed a spike in FLOPS and memory bandwidth, but these were not problematic.
- **Memory Bandwidth**: The memory bandwidth exceeding the dotted line is not an issue; higher values are better, especially for memory-bound applications.
- **Job Script Complexity**: Bundling jobs makes the script more complicated. Use non-production commands like `echo` to test and ensure the script is functioning as intended.

### Conclusion:
- The user made valuable improvements to the job script, resulting in better resource utilization.
- Continued monitoring and adjustments may be necessary to address any remaining errors or issues.

---

This summary provides a concise overview of the key points, root cause, solution, and additional notes from the HPC-Support ticket conversation. It can be used as a reference for support employees to address similar issues in the future.
---

### 2021051242002278_Benchmarking%20a%20deal.ii%20based%20FE%20code%20with%20MPI.md
# Ticket 2021051242002278

 # HPC Support Ticket: Benchmarking a deal.ii based FE code with MPI

## Keywords
- MPI
- deal.ii
- Benchmarking
- Scaling
- Hyper-threading
- OpenMPI
- Performance optimization

## Summary
A user encountered performance issues while benchmarking an MPI-based finite element (FE) code using deal.ii on the Emmy cluster. The code solves a system of linear equations (Ax=b) and was benchmarked using a basic `mpirun` command.

## Root Cause
- The user's benchmark did not account for the difference between physical cores and hyper-threading cores on the Emmy nodes.
- The code had bottlenecks related to the deal.ii implementation, such as non-distributed mesh and inefficient periodic boundary conditions.

## Solution
- **Use Physical Cores Only**: Add `-npernode 20` and `--bind-to core` to the `mpirun` command to utilize only the physical cores and bind MPI processes to individual cores.
- **Separate Benchmarks**: Conduct separate benchmarks for scaling inside a node and scaling over nodes.
  - Inside a node: `for N in 1 2 4 8 10 12 14 16 18 20; do mpirun --bind-to core -np $N ./my_fe_code; done`
  - Over nodes: `for N in 20 40; do mpirun -npernode 20 --bind-to core -np $N ./my_fe_code; done`
- **Code Optimization**: Address code-specific bottlenecks, such as improving mesh distribution and optimizing boundary conditions.

## General Learnings
- Always consider the architecture of the compute nodes (e.g., physical cores vs. hyper-threading cores) when benchmarking.
- Use appropriate MPI process binding and distribution for optimal performance.
- Conduct separate benchmarks for intra-node and inter-node scaling to better understand performance characteristics.
- Code-specific optimizations can significantly impact performance, especially for complex applications like FE solvers.

## Follow-up
The user implemented the suggested changes and observed improved performance, particularly for larger meshes and when avoiding periodic boundary conditions. The ticket was closed as the user had no further questions.
---

### 2025011742002045_Processes%20and%20Nodes.md
# Ticket 2025011742002045

 # HPC Support Ticket: Processes and Nodes

## Keywords
- Slurm
- Process distribution
- Node allocation
- MPI
- Load balancing
- `--cpu-bind`
- `--distribution`
- `MPI_Get_processor_name`

## Problem
- User inquires about the order in which Slurm distributes processes to nodes.
- User seeks a method to determine the node a process is running on from within a C++ MPI application.
- User aims to load balance processes with higher memory load across nodes.

## Solution
- **Process Distribution Order**: By default, Slurm fills the first node with processes in increasing order if all cores on each node are used.
- **Controlling Task Distribution**: Use `--cpu-bind` and `--distribution` options when calling `srun`.
- **Determining Node**: Use the `MPI_Get_processor_name` function within the MPI application to get the node name. Adding the `--cpu-bind=verbose` option to `srun` will also show on which node each process is running.

## Documentation
- Refer to the MPI documentation for more details: [MPI Documentation](https://doc.nhr.fau.de/sdt/mpi/)

## Additional Notes
- The user's goal is to evenly balance processes with higher memory load across nodes.
- The solution involves understanding and controlling the distribution of processes using Slurm options and MPI functions.

---

This report provides a concise summary of the user's questions and the solutions provided by the HPC Admin, focusing on process distribution and node determination within an MPI application.
---

### 2025031742002578_Reservierung%20auf%20fritz%20f%C3%83%C2%BCr%20ihpc119h.md
# Ticket 2025031742002578

 ```markdown
# HPC Support Ticket Conversation Analysis

## Subject
Reservierung auf fritz für ihpc119h

## Keywords
- Reservation
- Fritz-Knoten
- Leaf-Switch
- ihpc119h
- Masterarbeiterin
- StartTime
- EndTime
- Duration
- Nodes
- CoreCnt
- PartitionName
- Flags
- TRES
- Users
- State

## Summary
A user requested a reservation of 2 Fritz-Knoten for a specific user (ihpc119h) on a particular date and time. The user also requested that both nodes be on the same Leaf-Switch. The HPC Admin confirmed the reservation with detailed information.

## Root Cause
The user needed a reservation for specific nodes to ensure they are on the same Leaf-Switch for efficient communication and performance.

## Solution
The HPC Admin successfully reserved the requested nodes and provided the reservation details, including the start time, end time, node count, core count, partition name, flags, TRES, and user information.

## What Can Be Learned
- **Reservation Process**: Understanding how to request and confirm node reservations.
- **Node Specifications**: Importance of specifying node requirements, such as being on the same Leaf-Switch.
- **Reservation Details**: The format and information included in a reservation confirmation, such as start time, end time, node count, core count, partition name, flags, TRES, and user information.

## Additional Notes
- Ensure that reservation requests include all necessary details to avoid delays.
- Confirmation emails should provide comprehensive information about the reservation for clarity and reference.
```
---

### 2020011642000754_Ressourcennutzung%20Job%20auf%20emmy%20-%20iwia022h.md
# Ticket 2020011642000754

 # HPC Support Ticket Analysis

## Subject
Ressourcennutzung Job auf emmy - iwia022h

## Keywords
- Resource utilization
- Job distribution
- Load balancing
- Chapel
- C++
- MPI
- Infiniband
- Gasnet
- Environment variables
- Job script
- Monitoring

## Summary
The user's job was not utilizing the requested 20 nodes efficiently, leading to high load on a single node. The issue was identified through monitoring tools and communication with the user.

## Root Cause
- Incorrect job script configuration leading to uneven distribution of processes across nodes.
- Misunderstanding of MPI and Chapel job configurations.

## Solutions
- For C++ jobs, use `mpirun -np 20*n -npernode 20` to ensure even distribution of processes across nodes.
- For Chapel jobs, ensure proper configuration of environment variables and job scripts.
- Utilize monitoring tools to check job distribution and load balancing.

## General Learnings
- Always verify job scripts and environment variables before submitting jobs.
- Use monitoring tools to check resource utilization and load balancing.
- Proper configuration of MPI and Chapel jobs is crucial for efficient resource utilization.
- Communicate with users to understand their specific requirements and provide tailored solutions.

## Detailed Analysis
- The user's job was initially using only one node out of the requested 20, leading to high load on that node.
- The HPC Admin identified the issue through monitoring tools and communicated with the user to understand the job configuration.
- The user was advised to modify the job script to ensure even distribution of processes across nodes.
- The user encountered warnings in Chapel jobs, which were addressed by referring to Chapel documentation and adjusting environment variables.
- The user was provided with links to monitoring tools to check job distribution and load balancing.
- The issue was eventually resolved, and the user confirmed that the problem was clarified.

## Conclusion
Proper configuration of job scripts and environment variables is crucial for efficient resource utilization in HPC environments. Monitoring tools should be used to check job distribution and load balancing. Communication with users is essential to understand their specific requirements and provide tailored solutions.
---

### 2020020642001207_Jobs%20on%20Emmy%20%281238656%20...%20mpt1011h%29.md
# Ticket 2020020642001207

 # HPC-Support Ticket: Jobs on Emmy (1238656 ... mpt1011h)

## Keywords
- Job Performance
- Computational Activity
- Memory Bandwidth
- Floating Point Operations
- Performance Metrics
- Code Optimization

## Problem Description
- User's jobs on Emmy show no computational activity.
- Performance metrics indicate very low memory bandwidth and floating point operations.

## Root Cause
- The code is not utilizing the computational resources effectively.
- Possible issues with code initialization or inefficient algorithms.

## Diagnostic Information
- **Memory Bandwidth:** 0.5 GB/s (System offers close to 100 GB/s)
- **Floating Point Operations:** ~0.015 MFLOPS (System peak ~700 GFLOPS)
- **Performance Metrics:**
  - `perf top` shows high usage in `__memmove_ssse3_back` and `Engine<100ul, 5ul>::diag_update`.
  - `likwid-perfctr` indicates high cycles without execution due to memory loads.

## Solution
- **Recommendation:** Review and optimize the code to better utilize system resources.
- **Next Steps:**
  - User should analyze the code for potential bottlenecks.
  - Consider running such jobs on a local desktop if no optimization is possible.
  - HPC Admins can assist in code optimization if needed.

## General Learning
- Always check job performance metrics to ensure efficient use of HPC resources.
- Low computational activity may indicate issues with code initialization or inefficient algorithms.
- Utilize performance tools like `perf top` and `likwid-perfctr` to diagnose performance issues.

## References
- [HPC-Status Job Info](https://www.hpc.rrze.fau.de/HPC-Status/job-info.php?USER=mpt1011h&JOBID=1239678&ACCESSKEY=2bad51c3&SYSTEM=EMMY)
- HPC Services, Friedrich-Alexander-Universitaet Erlangen-Nuernberg, Regionales RechenZentrum Erlangen (RRZE)
---

### 2024120442003157_processes%20on%20Fritz%20frontend%20%5Bb133ae20%5D.md
# Ticket 2024120442003157

 # HPC Support Ticket: Processes on Fritz Frontend

## Keywords
- Cluster frontends
- Extensive calculations
- Interactive jobs
- Fritz3

## Problem
- User was running extensive calculations on the cluster frontend (Fritz3).

## Root Cause
- The cluster frontends are not designed for extensive calculations.

## Solution
- Use interactive jobs for interactive work.
  - Reference: [Interactive Job Documentation](https://doc.nhr.fau.de/clusters/fritz/#interactive-job)

## Action Taken
- HPC Admin killed the processes on Fritz3.
- HPC Admin provided guidance on using interactive jobs.

## General Learning
- Cluster frontends should not be used for extensive calculations.
- Interactive jobs are the appropriate method for interactive work on the cluster.

## Ticket Status
- Closed by HPC Admin.
---

### 2023080942002659_Tier3-Access-Fritz%20%22Tarakeshwar%20Lakshmipathy%22%20_%20iww1007h.md
# Ticket 2023080942002659

 ```markdown
# HPC Support Ticket Conversation Analysis

## Subject: Tier3-Access-Fritz "Tarakeshwar Lakshmipathy" / iww1007h

### Keywords:
- Resource Allocation
- Large Scale Limit
- Multi-node Workload
- HDR100 Infiniband
- LAMMPS
- Quantum Espresso
- IMD
- Atomistic Simulations
- Scientific Publications

### Summary:
- **User Request:**
  - Multi-node workload with HDR100 Infiniband (1:4 blocking).
  - Each node: 72 cores, 250 GB.
  - Required compute time: 75,000 node hours on Fritz.
  - Software needed: LAMMPS, Quantum Espresso, IMD.
  - Application: Atomistic simulations for studying fracture in crystalline materials.
  - Expected results: Production runs leading to scientific publications.

- **HPC Admin Response:**
  - The requested resources exceed the NHR large scale limit.
  - Approval pending from Erik.
  - Activation confirmed via reference number 2023080342003294.

### Root Cause of the Problem:
- The user's request for resources exceeded the NHR large scale limit.

### Solution:
- The request was forwarded for higher-level approval.
- Activation was eventually confirmed.

### General Learnings:
- Large resource requests require additional approval.
- Multi-node workloads with specific hardware requirements need careful consideration.
- Common software for atomistic simulations includes LAMMPS, Quantum Espresso, and IMD.
- Scientific publications are a common outcome of such simulations.
```
---

### 2022040842001134_NaN%20Output%20Klimamodell%20COSMO.md
# Ticket 2022040842001134

 # HPC Support Ticket: NaN Output Klimamodell COSMO

## Problem Description
- **User Issue**: The COSMO climate model produces NaN (Not a Number) values for higher resolutions (e.g., 1km) or when the resolution is increased too quickly (e.g., from 100km to 10km). The model becomes numerically unstable or has memory issues.
- **Root Cause**: Possible issues with compiler flags, memory allocation, or node/task distribution.

## Ticket Conversation Summary
- **Initial Request**: User requests help with NaN output in COSMO model, suspects issues with compilation or memory.
- **HPC Admin Response**:
  - Suggests trying different compiler flags (`-fp-model precise` instead of `-O2`).
  - Offers to move computations to a different cluster (Fritz) with newer compilers.
  - Provides module suggestions for Fritz: `intel`, `intelmpi`, `netcdf-fortran/4.5.3-intel`.
- **User Follow-Up**:
  - User tries suggested compiler flags without success.
  - Moves computations to Fritz, still encounters issues.
  - Receives partial help from a model developer, continues to test different compilers.

## Key Learnings
- **Compiler Flags**: Aggressive optimization (`-O2`) can lead to NaNs. Using `-fp-model precise` can help but may slow down execution.
- **Cluster Migration**: Moving to a cluster with newer compilers (Fritz) can help resolve issues, but may not always solve the problem.
- **Model Adjustments**: Sometimes, adjusting the model code itself can help resolve issues, as seen with the assistance from a model developer.

## Solution
- **Compiler Flags**: Try removing `-O2` and adding `-fp-model precise` to the compiler flags.
- **Cluster Migration**: Move computations to a cluster with newer compilers (Fritz) and use modules `intel`, `intelmpi`, `netcdf-fortran/4.5.3-intel`.
- **Model Adjustments**: Consult with model developers to adjust the code if necessary.

## Next Steps
- Continue testing different compilers and flags.
- Consider a Zoom session with HPC support for further assistance.

## Keywords
- COSMO model
- NaN output
- Compiler flags
- Memory issues
- Numerical instability
- Cluster migration
- Model adjustments
---

### 2023071942002767_SPR%20Access%20for%20DAREXA-F%20project%20%28group%20b182dc%29.md
# Ticket 2023071942002767

 # HPC Support Ticket: SPR Access for DAREXA-F Project

## Keywords
- SPR Access
- FP16 Functions
- DAREXA-F Project
- b182dc Group
- Fritz Cluster
- spr1tb Partition

## Summary
- **User Request:** Access to SPRs on Fritz cluster for testing FP16 functions, essential for the DAREXA-F project's data reduction.
- **Root Cause:** Lack of access to SPRs for the specified project group.
- **Solution:** HPC Admins granted access to the spr1tb partition for the b182dc group.

## Details
- **User:** Requested access to SPRs on Fritz for testing FP16 functions, crucial for their data reduction project.
- **HPC Admin:** Confirmed and granted access to the spr1tb partition for the b182dc group.

## Lessons Learned
- Ensure project groups have the necessary access to specific hardware resources like SPRs for their computational needs.
- Quick resolution of access requests can facilitate project progress and testing of essential functions.

## Action Taken
- Access to the spr1tb partition was granted to the b182dc group by HPC Admins.

## Follow-up
- No further action required from the user or HPC Admins as the request was successfully resolved.
---

### 2022101142002731_Jobs%20on%20meggie%20with%20very%20high%20load%20%7C%20mfpt002h.md
# Ticket 2022101142002731

 # HPC Support Ticket: Jobs with Very High Load

## Keywords
- High load
- Resource utilization
- Job optimization
- Thread management
- SSH node login

## Summary
A user's jobs were producing an unusually high load on the HPC system, specifically over 1000 on 32 cores. The HPC Admin notified the user to investigate the issue, suggesting that the application might be starting an excessive number of threads.

## Root Cause
- The user's job script had issues, likely related to the number of threads started by the application.

## Solution
- The user canceled all jobs and planned to run a single job to test and optimize the code.
- The HPC Admin suggested logging into a node via SSH to check resource utilization while the job is running.

## Outcome
- The issue was resolved after the user optimized the job script.
- The HPC Admin closed the ticket as the latest jobs/tests showed significant improvement.

## General Learnings
- Monitor job scripts for excessive resource utilization.
- Use SSH to log into nodes and check resource utilization during job execution.
- Optimize job scripts to ensure efficient use of HPC resources.

## Roles Involved
- HPC Admins
- User
---

### 2025022842003585_Jobs%20taking%20oddly%20longer%20times%20that%20usual.md
# Ticket 2025022842003585

 # HPC Support Ticket: Jobs Taking Longer Than Usual

## Keywords
- Job runtime discrepancy
- Resource allocation
- JobID comparison
- HPC account differences

## Problem Description
- User reports that jobs are taking significantly longer to run on their HPC account compared to their professor's account.
- Both accounts are running the same jobs with the same resource requests.

## Root Cause
- Unknown initially; requires investigation.

## Troubleshooting Steps
1. **Request JobIDs**: HPC Admin requests JobIDs from the user and their supervisor for comparison.
2. **Investigation**: HPC Admin plans to investigate the JobIDs to identify the cause of the runtime discrepancy.

## Solution
- Not yet determined; awaiting further investigation.

## General Learnings
- Differences in job runtime can have multiple causes.
- JobIDs are essential for diagnosing runtime issues.
- Comparing JobIDs from different accounts can help identify discrepancies in resource allocation or account settings.

## Next Steps
- Await user response with JobIDs.
- Conduct a detailed investigation of the provided JobIDs to identify the root cause.

---

This documentation will assist HPC support employees in diagnosing similar job runtime discrepancies in the future.
---

### 2023042842001229_jobs%20with%20poor%20workload%20-%20iww8008h.md
# Ticket 2023042842001229

 # HPC Support Ticket: Poor Workload Management

## Keywords
- CPU load imbalance
- Resource management
- Python script
- C++ programs
- Workload reorganization
- Master-worker scheme
- ClusterCockpit monitoring

## Problem Description
- User's jobs on the HPC system exhibited poor workload management.
- Initial CPU load exceeded the number of cores per node (400 vs. 20 cores).
- Some jobs had low or zero CPU load, indicating resource waste.

## Root Cause
- The Python script used as a resource management tool did not effectively balance the workload of the C++ programs it executed.

## Solution Suggested
- Improve the Python script to reorganize workload based on runtime estimates.
- Consider implementing a master-worker scheme to balance the load.
- Monitor jobs using ClusterCockpit for better resource management.

## Action Taken
- HPC Admin provided suggestions for improving workload management.
- Ticket closed due to no response from the user.

## General Learning
- Proper workload management is crucial to avoid resource waste.
- Monitoring tools like ClusterCockpit can help identify and address inefficiencies.
- Implementing a master-worker scheme can improve load balancing.

## References
- Monitoring links provided for specific job examples.
- Contact information for further support: `support-hpc@fau.de`

---

This documentation aims to help support employees identify and resolve similar workload management issues in the future.
---

### 2024121142003251_Tier3-Access-Fritz%20%22Vipul%20Kumar%20Ambasta%22%20_%20bccc128h.md
# Ticket 2024121142003251

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Keywords
- Multi-node workload
- HDR100 Infiniband
- 1:4 blocking
- 72 cores
- 250 GB
- Node hours
- Quantum ESPRESSO
- CP2K
- Project grant
- Fritz
- bccc128h
- Freischaltung
- Admins

## Summary
- **User Request**: The user requested access to the Fritz cluster for a multi-node workload with specific requirements (HDR100 Infiniband with 1:4 blocking, 72 cores, 250 GB per node) and a total of 250,000 node hours. The required software included Quantum ESPRESSO and CP2K, with the goal of simulating a physical process for a project grant.
- **Admin Response**: The request was initially deferred due to admin approval processes. Subsequently, the user was granted access to the Fritz cluster.

## Root Cause of the Problem
- The user needed access to the Fritz cluster for a specific project, which required admin approval.

## Solution
- The HPC Admins processed the request and granted the user access to the Fritz cluster.

## General Learnings
- The process for granting access to HPC resources involves admin approval.
- Users should specify their resource requirements clearly, including software needs and expected outcomes.
- Communication between users and HPC Admins is crucial for timely access to resources.
```
---

### 2018121342001297_Anf%C3%83%C2%A4ngerprobleme%3A%20qsub%20_%20VASP%20_%20qcat.md
# Ticket 2018121342001297

 # HPC Support Ticket Analysis

## Subject: Anfängerprobleme: qsub / VASP / qcat

### Keywords:
- qcat
- stdout / stderr
- locale settings
- ppn
- mpirun_rrze
- epilogue
- walltime

### Issues and Solutions:

1. **qcat Tool Availability**
   - **Issue**: User mentions that qcat tool is not available.
   - **Solution**: Verify if qcat is deprecated or replaced by another tool.

2. **Locale Settings Warning**
   - **Issue**: User receives warnings about locale settings.
   - **Solution**: Check and configure locale settings to avoid warnings.

3. **ppn Configuration**
   - **Issue**: User questions why ppn=40 when nodes have 2x10 cores.
   - **Solution**: Clarify the usage of threads and cores in the cluster configuration.

4. **mpirun_rrze Usage**
   - **Issue**: User asks about limiting MPI jobs and the range of -np parameter.
   - **Solution**: Explain the appropriate usage of mpirun_rrze and its parameters.

5. **Epilogue ncpus Value**
   - **Issue**: User questions why ncpus=1 in the epilogue.
   - **Solution**: Clarify the meaning of ncpus in the epilogue and its relation to requested resources.

6. **Walltime Estimation**
   - **Issue**: User seeks best practices for estimating job duration.
   - **Solution**: Provide guidelines for estimating walltime, such as running smaller tests and scaling.

### General Learnings:
- **Tool Availability**: Always check for tool deprecation or replacement.
- **Locale Settings**: Ensure proper configuration to avoid warnings.
- **Cluster Configuration**: Understand the difference between cores and threads.
- **MPI Job Management**: Know the limits and usage of MPI job parameters.
- **Resource Request Interpretation**: Clarify the meaning of resource requests in job epilogues.
- **Job Duration Estimation**: Use smaller tests and scaling for better walltime estimates.

### Next Steps:
- **HPC Admins**: Update documentation on qcat tool availability.
- **2nd Level Support**: Provide detailed instructions on locale settings configuration.
- **Training and Support Group**: Offer workshops on job management and resource estimation.

### References:
- **HPC Admins**: Thomas, Michael Meier, Anna Kahler, Katrin Nusser, Johannes Veh
- **2nd Level Support**: Lacey, Dane (fo36fizy), Kuckuk, Sebastian (sisekuck), Lange, Florian (ow86apyf), Ernst, Dominik (te42kyfo), Mayr, Martin
- **Datacenter Head**: Gerhard Wellein
- **Training and Support Group Leader**: Georg Hager
- **NHR Rechenzeit Support**: Harald Lanig
- **Software and Tools Developer**: Jan Eitzinger, Gruber
---

### 2018042642000341_Zahl%20der%20MPI-Prozesse%20bei%208-Node-Jobs%20auf%20Meggie.md
# Ticket 2018042642000341

 # HPC Support Ticket: High Load on 8-Node Jobs

## Keywords
- MPI processes
- Node count
- mpirun
- Load monitoring

## Problem Description
- **Root Cause**: User reduced the number of nodes for 8-node jobs but did not adjust the number of MPI processes in the `mpirun` command.
- **Symptom**: Extreme load observed in monitoring.

## Solution
- Adjust the number of MPI processes in the `mpirun` command to match the reduced node count.

## General Learnings
- Always ensure that the number of MPI processes specified in the `mpirun` command matches the number of nodes allocated for the job to avoid excessive load.
- Regularly monitor job performance to identify and address any anomalies.

## Roles Involved
- **HPC Admins**: Provided monitoring insights and suggested solution.
- **User**: Acknowledged the issue and agreed to adjust the MPI process count.

## Related Tools/Commands
- `mpirun`
- Monitoring tools used by HPC Admins

## Additional Notes
- This issue highlights the importance of proper configuration of MPI jobs to avoid resource wastage and performance degradation.
---

### 2025010842003169_Reservierung%20auf%20fritz%20f%C3%83%C2%BCr%20ihpc119h.md
# Ticket 2025010842003169

 # HPC Support Ticket: Reservation Management

## Keywords
- Reservation
- HPC Nodes
- Cancellation
- User Request
- Admin Response

## Summary
A user requested reservations for specific HPC nodes on multiple dates and times. The HPC Admin confirmed the reservations, and later, the user requested the cancellation of some reservations.

## Detailed Conversation

### User Request
- **Date**: 08.01.2025
- **Request**: Reservation of 5 Fritz-Knoten for a user (ihpc119h) on specific dates and times.
  - Thursday, 09.01. 13:00-22:00
  - Saturday, 11.01. 14:00-22:00
  - Sunday, 12.01. 17:00-23:00

### HPC Admin Response
- **Date**: 08.01.2025
- **Action**: Confirmed the reservations with detailed information.
  - ReservationName=ihpc1, StartTime=2025-01-09T13:00:00, EndTime=2025-01-09T22:00:00
  - ReservationName=ihpc2, StartTime=2025-01-11T14:00:00, EndTime=2025-01-11T22:00:00
  - ReservationName=ihpc3, StartTime=2025-01-12T17:00:00, EndTime=2025-01-12T23:00:00

### User Cancellation Request
- **Date**: 10.01.2025
- **Request**: Cancellation of reservations for Saturday and Sunday.

### HPC Admin Response
- **Date**: 10.01.2025
- **Action**: Confirmed the cancellation of the requested reservations.

## Lessons Learned
- **User Request Handling**: Users can request reservations for specific nodes and times.
- **Admin Confirmation**: Admins confirm reservations with detailed information including node names, start and end times, and other relevant details.
- **Cancellation Process**: Users can request the cancellation of reservations, and admins can confirm the cancellation.

## Solution
- **Reservation Management**: Ensure that reservations are made and confirmed promptly.
- **Cancellation Handling**: Be prepared to handle cancellation requests efficiently.

## Root Cause
- **User Needs**: The user initially required specific reservations but later found that some were no longer needed.

## Documentation for Support Employees
- **Reservation Process**: Follow the steps to confirm reservations with detailed information.
- **Cancellation Process**: Ensure that cancellation requests are handled promptly and confirmed to the user.

This documentation can be used as a reference for handling similar reservation and cancellation requests in the future.
---

### 2022032942004264_likwid-perfctr%20on%20meggie.md
# Ticket 2022032942004264

 ```markdown
# HPC-Support Ticket Conversation: likwid-perfctr on meggie

## Issue
User Dinesh encountered issues with performance counters when using `likwid-perfctr` on the `meggie` cluster. The memory bandwidth and operational intensity metrics were not as expected.

## Root Cause
- There is an issue with performance counters on `meggie`: Sometimes there is "garbage" in the counter registers for memory transfers.
- This issue cannot be fixed by `likwid-perfctr` and happens only on certain nodes.

## Solution
- A workaround has been implemented in the `likwid/5.2.1` module.
- Run separate jobs for each performance counter group to avoid multiplexing issues.
- The memory controllers exist only once per CPU socket, and therefore only one hardware thread of a CPU socket reads the counters. In this case, it's `hwthread 0`, but the counts reflect the activity of the whole CPU socket (`hwthread 0-9`).

## Key Learnings
- The maximum memory bandwidth for the Intel Xeon processor E5-2630 v4 is 68.3 GB/s.
- The peak performance specifications for this processor can be found in the Intel ARK documentation.
- Running multiple performance counter groups simultaneously can lead to inaccurate results due to multiplexing issues.

## Example Commands
```bash
srun --cpu-bind=none likwid-perfctr -C S0:0-9 -g L2 -g L3 -g MEM_DP -g FLOPS_DP ./exastencils
```

## Additional Notes
- Ensure to exclude problematic nodes if issues persist.
- Always check the full output of `likwid-perfctr` for detailed analysis.

```
```
---

### 2021042142002628_%5BAMD-EPYC-7502-nodes%5D.md
# Ticket 2021042142002628

 ```markdown
# HPC Support Ticket: [AMD-EPYC-7502-nodes]

## Keywords
- AMD Epyc 7502 nodes
- Python performance
- Core allocation
- Slurm configuration
- Hyperthreading
- `likwid-pin`
- `srun` options
- `sbatch` options
- Exclusive node allocation

## Problem Description
- Python programs running inefficiently since April.
- Programs only utilizing core 0 and its hyperthread (id 64).
- `likwid-pin -p` showed limited core ids in N, S, and C domains compared to other nodes.

## Root Cause
- Slurm configuration changes led to default allocation of only one core without explicit specification of `--ntasks` or `--cpus-per-task`.
- Hyperthreads were not utilized by default on `tinyfat` nodes.

## Solution
- Use `--cpus-per-task=128` to access all cores.
- For MPI applications, use `--ntasks-per-core=2` or `--hint=multithread` to utilize hyperthreads.
- Use `--exclusive` option for `sbatch` to allocate the entire node.
- `tinyx` was renamed to `tinyfat`; ensure correct usage in Slurm commands.

## General Learnings
- Understand the importance of specifying core allocation options in Slurm.
- Be aware of changes in Slurm configurations and their impact on job performance.
- Use diagnostic tools like `likwid-pin` to troubleshoot core allocation issues.
- Ensure correct usage of node names and options in Slurm commands.

## Example Command
```bash
srun -N 1 --cpus-per-task=128 --exclusive --time=02:00:00 -M tinyfat --pty bash -l
```
```
---

### 2022041242002643_Gromacs%20Multinode%20auf%20Fritz%20%5Bbcpc001h%5D.md
# Ticket 2022041242002643

 ```markdown
# HPC-Support Ticket: Gromacs Multinode auf Fritz [bcpc001h]

## Keywords
- Gromacs
- Multinode
- Fritz
- Job Submission
- Documentation
- Certificate Expired

## Summary
- **User Issue**: Certificate has expired.
- **HPC Admin Response**: Informed the user about their multinode access and provided a link to the Gromacs documentation for running jobs on multiple nodes.

## Root Cause
- Certificate expiration.

## Solution
- No direct solution provided for the certificate issue.
- User was informed about their multinode access and directed to the Gromacs documentation for running jobs on multiple nodes.

## General Learnings
- Users should be aware of their multinode access and how to utilize it.
- Documentation is available for running Gromacs on multiple nodes.
- Certificate expiration issues should be addressed separately.

## Links
- [Gromacs Documentation](https://hpc.fau.de/systems-services/systems-documentation-instructions/special-applications-and-tips-tricks/gromacs/?preview_id=5834&preview_nonce=2d9cdd98f1&_thumbnail_id=-1&preview=true#collapse_3)
```
---

### 42095767_Knotenreservierung%20woody.md
# Ticket 42095767

 # HPC-Support Ticket: Node Reservation for Benchmarking

## Keywords
- Node reservation
- Infiniband
- Benchmarking
- Perl module
- Datenbanktreiber

## Summary
A user's node reservation on `w0632` in the `woody` cluster had expired. The user requested an additional fifth node for benchmarking purposes, specifically to utilize Infiniband.

## Root Cause
- Expired node reservation on `w0632`.

## Solution
- HPC Admin re-reserved `w0632` for the user.
- Noted that `w09*` nodes have DDR Infiniband among themselves, but only SDR Infiniband to `w0632`.

## Additional Information
- The user successfully configured a Perl module with a database driver on the `woody` cluster using `local::lib`.

## Lessons Learned
- Ensure node reservations are extended or renewed as needed for ongoing projects.
- Be aware of Infiniband speed variations between different node groups within a cluster.
- Successful configuration of Perl modules with database drivers can be achieved using `local::lib`.

## Follow-Up
- Monitor node reservations to prevent expiration during critical projects.
- Document Infiniband speed differences for future reference.
---

### 2023060542003285_Problems%20with%20spr1tb%20nodes%20on%20Fritz.md
# Ticket 2023060542003285

 # HPC Support Ticket: Problems with spr1tb Nodes on Fritz

## Keywords
- VASP machine learning force field calculations
- MPI initialization issues
- MPI warnings
- Zombie-like state
- Large memory clusters
- spr1tb partition
- Hydra process manager
- I_MPI_PMI_LIBRARY

## Problem Description
- User encountered issues with VASP machine learning force field calculations on the spr1tb partition.
- Calculations get stuck after MPI initialization, with only MPI warnings printed in the `vasp.out` file.
- Jobs remain in a zombie-like state until the walltime is reached.
- Problem occurs intermittently and sometimes resolves when using fewer nodes (4 instead of 8).
- Affected nodes: `f[2174-2180,2265]` and `f[2257-2264]`.

## Root Cause
- Possible internal problems with some nodes, potentially related to MPI libraries.
- Inefficient distribution of Kohn-Sham orbitals across MPI processes.

## Troubleshooting Steps
- HPC Admin requested input files to reproduce the error.
- HPC Admin ran VASP with the provided input files without encountering a crash.

## Solution/Recommendations
- **Use Fewer Nodes**: Running calculations on fewer nodes (e.g., 2 nodes, 208 cores) can make the runs faster and more efficient.
- **Adjust NCORE**: Setting `NCORE = 8` can improve performance.
- **Use `srun` Instead of `mpirun`**: This can eliminate the MPI warning related to `I_MPI_PMI_LIBRARY`.

## Follow-Up
- If the problem persists even with fewer nodes, further investigation by HPC Admins is required.

## Lessons Learned
- Intermittent issues can be challenging to diagnose and may require multiple attempts to reproduce.
- Efficient distribution of computational tasks across nodes is crucial for performance and stability.
- Using appropriate commands (e.g., `srun` instead of `mpirun`) can help avoid certain warnings and potential issues.
---

### 42355005_hasep1%20likwid%20Messungen%20gehen%20nicht.md
# Ticket 42355005

 # HPC-Support Ticket: LIKWID Measurements Not Working on hasep1

## Keywords
- hasep1
- LIKWID
- likwid-perfctr
- MEM group
- Counter register
- PCI device
- Intel Xeon Haswell

## Problem Description
The user is unable to perform LIKWID measurements on the hasep1 system. The error messages indicate that certain counter registers (MBOX2C0, MBOX2C1, etc.) are not supported or the PCI device is not available.

## Root Cause
The LIKWID tool is attempting to access performance counters that are not supported or available on the Intel Xeon Haswell processor of the hasep1 system.

## Ticket Conversation Summary
- **User**: Reported that LIKWID measurements are not working on hasep1. Provided command and error output.
- **HPC Admins/2nd Level Support**: (Details of the interaction are not provided in the given conversation.)

## Solution
(No solution was provided in the given conversation. Further investigation is needed to determine if the counters are indeed not supported or if there is a configuration issue.)

## General Learnings
- LIKWID tool may attempt to use performance counters that are not available on all systems.
- Error messages from LIKWID can indicate issues with counter register support or PCI device availability.
- Always check the compatibility of performance monitoring tools with the specific hardware in use.

## Next Steps for Support
1. Verify the availability of the mentioned counter registers on the Intel Xeon Haswell processor.
2. Check if there are any configuration issues or missing PCI devices.
3. Consult LIKWID documentation or support for guidance on the error messages.
4. Update the user with findings and potential solutions.
---

### 2019112742001869_increasing%20Quota%20for%20a%20limited%20time.md
# Ticket 2019112742001869

 # HPC Support Ticket Analysis: Increasing Quota and Job Queue Time

## Keywords
- Quota Increase
- Simulation Data
- Job Queue Time
- Priority
- Fair Share
- Waiting Time
- Job Size

## Summary
A user requested a temporary quota increase for simulation data and encountered issues with job queue times on the Emmy cluster.

## Root Cause of the Problem
1. **Quota Increase Request**: The user needed more storage space for larger simulations.
2. **Job Queue Time**: The user's jobs were being pushed to the end of the queue due to high resource usage in the past 10 days.

## Solutions and Learnings
- **Storage**: Use `$WORK` for simulation data. Refer to the [HPC Storage Guide](https://www.anleitungen.rrze.fau.de/hpc/hpc-storage/) for more information.
- **Job Queue Time**:
  - **Fair Share System**: The queueing system prioritizes users based on their recent resource usage. High usage in the past 10 days lowers priority.
  - **Waiting Time**: Deleting and resubmitting jobs resets the accumulated waiting time, which negatively affects priority.
  - **Job Size**: Large jobs (e.g., 64 nodes) will stay in the queue longer as they require draining more nodes.

## General Learnings
- **Storage Management**: Understand and utilize appropriate storage options for simulation data.
- **Job Queue Management**: Be aware of the fair share system and the impact of job size and waiting time on priority.
- **Resource Usage**: High recent resource usage can lower job priority. Plan and manage resource usage accordingly.

## Actions Taken
- The user was advised to use `$WORK` for simulation data.
- The user was informed about the fair share system and the impact of job size and waiting time on priority.

## Follow-up
- Monitor the user's job queue time and provide further assistance if needed.
- Ensure the user understands the fair share system and how to manage job priority.
---

### 2023060242001541_Tier3-Access-Fritz%20%22Moritz%20Zaiss%22%20_%20mfdr001h.md
# Ticket 2023060242001541

 # HPC Support Ticket Analysis

## Keywords
- HPC Account Activation
- KONWIHR Project
- SPR Nodes
- Partition Request
- Certificate Expiration

## Summary
- **User Request**: Access to HPC resources for a specific project (KONWIHR project MRzero) requiring high-memory nodes.
- **Issue**: Certificate expiration mentioned by HPC Admin.
- **Solution**: HPC account activated for the project, with instructions on how to request specific partitions.

## Details
- **User Needs**:
  - Single-node throughput with special justification (72 cores, 250 GB).
  - 1000 node hours on Fritz.
  - Access to 1-2TB RAM nodes.
  - Sapphire Rapids processors.
- **Application**: Optimization of differentiable MRI simulation for high-resolution 3D MRI images.
- **Expected Results**: End-to-end optimization for high-resolution 3D MRI.

## Actions Taken
- HPC Admin activated the user's account for the KONWIHR project on Fritz, including access to SPR nodes.
- Instructions provided to request specific partitions: `--partition=spr1tb` or `--partition=spr2tb`.

## Root Cause of the Problem
- Certificate expiration was noted but did not prevent account activation.

## Solution
- Account activated with specific instructions for partition requests.

## Notes
- The user had previously discussed the project with a specific contact.
- Initial test requested: 1 node * 5 days * 1 job.

This documentation can be used to resolve similar issues related to account activation and partition requests for high-memory nodes.
---

### 2022101142002535_Jobs%20auf%20meggie%20%7C%20iwso070h.md
# Ticket 2022101142002535

 # HPC Support Ticket: Jobs auf meggie | iwso070h

## Keywords
- Resource allocation
- Parallelization
- Joblib
- Slurm script
- Monitoring
- MPI
- OpenMP
- AssocMaxNodePerJobLimit
- AssocGrpCpuLimit

## Summary
The user was initially requesting excessive resources for jobs that were running serially, leading to inefficient resource usage. The user's Python application was using joblib for parallelization, which is shared-memory parallel and not suitable for distributed-memory parallelization across multiple nodes.

## Root Cause
- The user's jobs were requesting 8 nodes (64 tasks) but were only utilizing one core, leading to resource wastage.
- The user's application was not capable of utilizing multiple nodes effectively due to the nature of joblib's parallelization.

## Solution
- The user was advised to adjust their Slurm script to request only one node, as joblib can only utilize the cores within a single node.
- The user was provided with a link to an example script for an OpenMP job (single node) to fully utilize a single meggie node.
- The user was informed about the group's CPU core limit on the woody cluster and advised to wait for resources to become available.

## Lessons Learned
- Always ensure that the requested resources match the application's capabilities.
- Understand the difference between shared-memory and distributed-memory parallelization.
- Monitor job resource usage to identify and address inefficiencies.
- Be aware of group resource limits and plan job submissions accordingly.

## References
- [meggie Cluster Documentation](https://hpc.fau.de/systems-services/documentation-instructions/clusters/meggie-cluster/)
- [woody Cluster Documentation](https://hpc.fau.de/systems-services/documentation-instructions/clusters/woody-cluster/)
- [OpenMP job example](https://hpc.fau.de/systems-services/documentation-instructions/clusters/meggie-cluster/#collapse_11)
- [Monitoring Tool](https://monitoring.nhr.fau.de/)
---

### 2024011042004361_Multi%20Node%20Jobs%20for%20ALLMT-NHR-Project.md
# Ticket 2024011042004361

 # Multi Node Jobs for ALLMT-NHR-Project

## Keywords
- Multi-node jobs
- GPU nodes
- QoS specification
- NHR projects
- Alex cluster
- Job submission error

## Problem
- User attempted to submit a multi-node job on the Alex cluster but encountered an error: `sbatch: error: Batch job submission failed: Invalid qos specification`.
- The user assumed that the necessary permissions for multi-node jobs had already been granted but was unsure.

## Root Cause
- The user's project did not have the required Quality of Service (QoS) specification enabled for multi-node jobs.

## Solution
- HPC Admin granted the project (b200dc) access to the `--qos=a100multi` specification.
- The user was instructed to request 8 GPUs per node using `--gres=gpu:a100:8` along with the desired number of nodes using `--nodes=<#>`.
- The user confirmed that the access worked after the changes were made.

## General Learnings
- Multi-node jobs require explicit permissions and QoS specifications.
- For multi-node jobs on the Alex cluster, always request 8 GPUs per node.
- Increasing the number of requested nodes may lead to longer wait times for job execution due to resource availability.

## Documentation Reference
- [Alex Cluster Documentation - Multi-Node Job](https://hpc.fau.de/systems-services/documentation-instructions/clusters/alex-cluster/#collapse_16)

## Roles Involved
- HPC Admins
- 2nd Level Support Team
- Head of the Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support
- Software and Tools Developer
---

### 2018120742001183_number%20of%20threads%20for%20jobs%20on%20Woody%20_%20iww2003h.md
# Ticket 2018120742001183

 # HPC Support Ticket: Number of Threads for Jobs on Woody

## Keywords
- Woody
- Threads
- Cores
- Job Configuration
- Script

## Problem
- **Root Cause**: User's jobs on Woody were configured to start 24 threads.
- **Issue**: Woody nodes only have 4 cores, making 24 threads inefficient.

## Solution
- **Action Taken**: HPC Admin notified the user about the inefficient thread configuration.
- **User Response**: User acknowledged the issue and planned to update the script.

## General Learning
- Ensure job scripts are configured to match the hardware capabilities of the HPC nodes.
- Adjust the number of threads to align with the available cores for optimal performance.

## Additional Notes
- This ticket highlights the importance of proper job configuration and the need for users to adapt their scripts when moving between different HPC systems.

---

This documentation can be used to address similar issues in the future by ensuring job configurations are optimized for the specific HPC environment.
---

### 2024073142000958_jobs%20on%20Fritz%20requiring%20much%20memory%20-%20gwgi006h.md
# Ticket 2024073142000958

 # HPC Support Ticket: High Memory Usage on Fritz

## Keywords
- High memory usage
- Job packing
- Fritz cluster
- ICL nodes
- Fat nodes
- spr2tb partition
- Concurrent jobs

## Problem
- User has 25 jobs on Fritz, each using only one core but requiring significant memory.
- Fritz is busy, causing other users' jobs to wait in the queue.

## Root Cause
- Inefficient use of resources: single-core jobs with high memory requirements.

## Solution
- **Job Packing**: Utilize fat nodes in the `spr2tb` partition with 2TB of memory.
  - Pack about 8 jobs to run concurrently on one `spr2tb` node.
  - This frees up 8 ICL nodes, reducing the load on the cluster.

## General Learning
- **Efficient Resource Utilization**: Encourage users to pack jobs that require high memory but low CPU usage.
- **Partition Selection**: Guide users to appropriate partitions (e.g., `spr2tb`) for high-memory jobs.
- **Cluster Management**: Monitor and advise users to optimize job submissions, especially during high-demand periods.

## References
- [Fritz Cluster Documentation](https://doc.nhr.fau.de/clusters/fritz/#batch-processing)

## Contact
- For assistance, contact the HPC support team at [support-hpc@fau.de](mailto:support-hpc@fau.de).
---

### 2023040442002461_jobs%20on%20fritz%2C%20inappropriate%20use%20of%20core%20and%20node%20counts%20-%20bctc034h.md
# Ticket 2023040442002461

 # HPC Support Ticket: Inappropriate Use of Core and Node Counts

## Keywords
- Job scheduling
- Node allocation
- MPI
- mpirun
- srun
- Slurm
- VASP

## Problem Description
- User submitted multiple jobs requesting 4 nodes each but only utilizing one node due to the `-np 72` parameter in the `mpirun` command.

## Root Cause
- Incorrect usage of `mpirun` leading to inefficient resource allocation.

## Solution
- Recommended using `srun` instead of `mpirun` to allow Slurm to manage resource allocation more effectively.

## Lessons Learned
- Always ensure that the number of processes (`-np`) matches the requested resources.
- Prefer using `srun` over `mpirun` for better resource management by Slurm.
- Keep run command values updated to avoid resource wastage.

## Actions Taken
- HPC Admin provided guidance on using `srun` for better resource management.
- Ticket closed after providing the necessary information.

## References
- [Slurm Documentation](https://slurm.schedmd.com/documentation.html)
- [VASP Documentation](https://www.vasp.at/wiki/index.php/Main_Page)

---

For further assistance, contact the HPC Support team at [support-hpc@fau.de](mailto:support-hpc@fau.de).
---

### 2023102742001933_Variable%20FI_PSM2_CONN_TIMEOUT%20in%20Slurm%20%20script%20setzen.md
# Ticket 2023102742001933

 # HPC Support Ticket: Variable FI_PSM2_CONN_TIMEOUT in Slurm Script

## Problem Description
- User encountered an error shortly after starting a simulation with 64 nodes on Meggie.
- The simulation worked fine with 32 nodes.
- The default value of `FI_PSM2_CONN_TIMEOUT` was suspected to be too small for 64 nodes.

## Initial Attempt
- User tried setting `FI_PSM2_CONN_TIMEOUT = 10` in the Slurm script, but it did not work.

## Solution
- Correct syntax for setting the environment variable: `export FI_PSM2_CONN_TIMEOUT=10` (no spaces around the equals sign).
- Despite setting the variable correctly, the problem persisted.

## Root Cause
- The error was likely due to issues in the Omnipath network on Meggie, specifically with optical cables entering a "zombie mode" and causing network disruptions.

## Resolution
- The network issue was resolved by the HPC team, and the problem did not occur after the fix.
- The user confirmed that the simulation ran successfully after the network issue was addressed.

## Key Takeaways
- Ensure correct syntax when setting environment variables in Slurm scripts.
- Network issues can sometimes mimic application-level problems.
- Always consider network health when troubleshooting job failures on HPC systems.

## Closure
- The ticket was closed after confirming that the jobs with 64 nodes were running successfully.

---

This documentation can be used to troubleshoot similar issues in the future.
---

### 2024030742003909_Knotenreservierung%20f%C3%83%C2%BCr%20Demo%20%28LANL%20Talk%29.md
# Ticket 2024030742003909

 ```markdown
# HPC Support Ticket: Node Reservation for Demo (LANL Talk)

## Keywords
- Node Reservation
- Alex-A100 Node
- GraceHopper Node
- Demo
- LANL Talk

## Summary
A user requested a node reservation for a demo during a talk at LANL. The reservation was successfully made by an HPC Admin.

## Problem
- User needed specific nodes reserved for a demo during a talk.

## Solution
- HPC Admin reserved the requested nodes for the specified time.

## Details
- **Requested Nodes:** Alex-A100 Node, GraceHopper Node
- **Time:** 18.03.2024 from 17:00 to 20:30
- **Reservation Details:**
  - **Alex-A100 Node:**
    - Nodes: a0531
    - CoreCnt: 128
    - TRES: cpu=128
  - **GraceHopper Node:**
    - Nodes: gracehop1
    - CoreCnt: 72
    - TRES: cpu=72

## Lessons Learned
- Users can request node reservations for specific events.
- HPC Admins can handle node reservations and provide detailed confirmation.
- Important to specify the exact nodes and time frame for reservations.
```
---

### 2024103042003325_Tier3-Access-Fritz%20%22Eman%20Bagheri%22%20_%20iwst111h.md
# Ticket 2024103042003325

 ```markdown
# HPC Support Ticket Conversation Analysis

## Subject: Tier3-Access-Fritz "Eman Bagheri" / iwst111h

### Keywords:
- Tier3 Access
- Fritz
- Multi-node workload
- HDR100 Infiniband
- Ansys
- Neko
- Nek5000
- Turbulence research
- CFD tool development

### Summary:
- **User Request:** Access to Fritz for multi-node workload with specific requirements.
- **Requirements:**
  - Multi-node workload (HDR100 Infiniband with 1:4 blocking; per node: 72 cores, 250 GB)
  - 49999 node hours on Fritz
  - Software: Ansys (only meshing tools)
  - Application: Spectral element simulations using Neko and Nek5000
  - Expected Results: Turbulence research and high-performance CFD tool development

### Actions Taken:
- **HPC Admin:** Granted access to Fritz for the user's account (iwst111h).

### Outcome:
- User confirmed receipt of access.
- Ticket closed by HPC Admin.

### Lessons Learned:
- **Process:**
  - Users requesting access to specific HPC resources need to provide detailed requirements.
  - HPC Admins review and grant access based on the provided information.
- **Communication:**
  - Clear and concise communication between the user and HPC Admin ensures smooth processing of requests.
  - Confirmation of access by the user is important for closing the ticket.

### Root Cause of the Problem:
- User needed access to Fritz for specific computational tasks.

### Solution:
- HPC Admin granted the necessary access after reviewing the user's requirements.
```
---

### 2021030442003821_Turbomole-Jobs%20mit%20%3Akl32%20auf%20Woody%20-%20bctc55.md
# Ticket 2021030442003821

 ```markdown
# HPC-Support Ticket: Turbomole-Jobs mit :kl32 auf Woody - bctc55

## Problem Description
- User's Turbomole jobs on Woody require `:kl32` nodes.
- Jobs fail to start correctly on Skylake nodes, causing them to crash without writing output files.
- User has a large number of jobs in the queue, causing delays.

## Root Cause
- Turbomole module (turbomole/parallel/7.2) does not start correctly on Skylake nodes.
- User's job scripts resubmit jobs without checking for successful completion, leading to infinite resubmissions.

## Solution
- HPC Admin identified the issue with w120x nodes, which have non-functional IB cards.
- Adjusted Turbomole modules (turbomole-parallel/7.2 and turbomole-parallel/7.3) to set `MPIRUN_OPTIONS` to include `-TCP`, allowing jobs to run correctly on w120x nodes.
- User was advised to check job completion status before resubmitting to avoid unnecessary load on the batch system.

## Keywords
- Turbomole
- Skylake nodes
- Job resubmission
- Infinite loop
- IB cards
- MPIRUN_OPTIONS
- TCP

## Lessons Learned
- Always check job completion status before resubmitting to avoid unnecessary load.
- Ensure that job scripts handle errors gracefully to prevent infinite resubmissions.
- Hardware-specific issues can cause software to fail unexpectedly, requiring specific adjustments.
```
---

### 2020090342000844_%22Too%20much%20memory%22-Fehlermeldungen%20und%20Jobs%2C%20die%20Walltime%20%C3%83%C2%BCberschreite.md
# Ticket 2020090342000844

 # HPC Support Ticket Analysis

## Subject: "Too much memory"-Fehlermeldungen und Jobs, die Walltime überschreiten

### Keywords:
- Memory usage
- Walltime exceeded
- Job hanging
- GAMMA software
- Endless loop
- Log file deletion

### Problem Description:
1. **Memory Usage Issue**:
   - User receives emails indicating jobs are using too much memory.
   - Jobs run successfully but trigger memory warnings.
   - Monitoring graphs show high memory usage in the initial phase.

2. **Walltime Exceeded Issue**:
   - Jobs exceed walltime but do not perform any calculations.
   - Log files are not created, indicating jobs are not executed.
   - Issue is sporadic and new since recent maintenance.

### Root Cause Analysis:
1. **Memory Usage Issue**:
   - Jobs are running close to the memory limit, causing swap usage and slow performance.
   - Monitoring graphs show high memory usage in the initial phase, followed by lower usage.

2. **Walltime Exceeded Issue**:
   - Jobs are hanging in an endless loop, possibly due to a software bug in GAMMA.
   - Log files are deleted if they exceed 100 MB, indicating a potential endless loop.
   - The `create_dem_par` process is stuck in a loop, continuously reading from an empty pipe.

### Solution:
1. **Memory Usage Issue**:
   - Reduce memory usage if possible.
   - Use nodes with more than 8 GB RAM by specifying `:any32g` in the `qsub` command.

2. **Walltime Exceeded Issue**:
   - Investigate potential software bug in GAMMA.
   - Check for endless loops in the job script.
   - Ensure log files are not deleted prematurely.

### General Learnings:
- Monitor memory usage closely to avoid performance issues.
- Investigate hanging jobs by checking system calls and log files.
- Be aware of software bugs that can cause endless loops and job failures.
- Use appropriate node properties to ensure sufficient resources for jobs.

### References:
- [Woody Cluster Batch Documentation](https://www.anleitungen.rrze.fau.de/hpc/woody-cluster/#batch)
---

### 2024111842002401_Maximale%20Anzahl%20Nodes%20alex.md
# Ticket 2024111842002401

 # HPC Support Ticket: Maximale Anzahl Nodes alex

## Keywords
- Multi-Node Reservation
- Resource Allocation
- Job Script Configuration
- A100 Multi-Node
- QoS (Quality of Service)

## Problem
- User attempted to reserve more than one node for resource-intensive tasks but received an error: `sbatch: error: Batch job submission failed: Node count specification invalid`.

## Root Cause
- The user's account was not configured for multi-node A100 usage.
- The job script lacked the necessary QoS specification for multi-node jobs.

## Solution
- HPC Admin enabled the user's account for multi-node A100 usage.
- The user was instructed to add `--qos=a100multi` to the job script in addition to `--nodes=2`.

## General Learning
- For multi-node resource allocation, ensure the account is configured for such usage.
- Include the appropriate QoS specification in the job script to avoid node count specification errors.

## Example Job Script Update
```bash
#SBATCH --nodes=2
#SBATCH --qos=a100multi
```

## Follow-Up
- The user confirmed the solution and planned to test it immediately.

## Relevant Contacts
- **HPC Admins**: For account configuration and job script assistance.
- **2nd Level Support Team**: For additional troubleshooting and support.
- **Gehard Wellein**: Head of the Datacenter.
- **Georg Hager**: Training and Support Group Leader.
- **Harald Lanig**: NHR Rechenzeit Support and Applications for Grants.
- **Jan Eitzinger and Gruber**: Software and Tools developers.
---

### 2023052542001831_Huge-Memory%20node%20on%20Fritz.md
# Ticket 2023052542001831

 ```markdown
# HPC-Support Ticket Conversation: Huge-Memory Node on Fritz

## Keywords
- Huge-memory nodes
- Project access
- Memory requirements
- Machine learning force fields
- Node utilization

## Summary
A user from the Theoretical Chemistry department at Universität Erlangen-Nürnberg requested access to huge-memory nodes (spr1tb, spr2tb) for their projects due to high memory requirements for machine learning force field calculations. The user mentioned that they currently use multiple standard nodes to meet their memory needs.

## Root Cause
- Insufficient memory on standard nodes for large-scale machine learning calculations.
- Need for access to specialized huge-memory nodes to optimize resource usage.

## Solution
- HPC Admins enabled the projects (b120dc and b146dc) for access to the huge-memory nodes (spr1tb and spr2tb).
- Additionally, the user's account (bctc034h) and other linked accounts were also granted access as a precautionary measure.

## General Learnings
- Users with high memory requirements should be directed to specialized nodes if available.
- Project-specific access can be granted to optimize resource allocation.
- Regular communication with users and understanding their specific needs can help in better resource management.
```
---

### 2025011742001493_Re%3A%20SCALEXA%3A%20Anfrage%20zu%20%22Sturmfrei%20Compute%20Day%22%20auf%20Fritz.md
# Ticket 2025011742001493

 # HPC Support Ticket Conversation Analysis

## Keywords
- Downtime
- Reservation
- Big-Queue
- Freischalten
- Skalierungsbenchmarks
- Fritz Cluster
- SCALEXA Projekt
- Sturmfrei Compute Day
- NHR@FAU

## General Learnings
- **Downtime Opportunities**: Downtimes can be used to reserve the entire cluster for specific projects.
- **Big-Queue Access**: Users can be granted access to the big-queue partition for larger computations.
- **Project Communication**: Early communication of resource needs is crucial for planning.
- **Reservation Parameter**: Use `--reservation=StroemungsRaum` for job submissions during reserved times.
- **Node Limits**: Node limits can be adjusted based on user needs and system capabilities.

## Root Cause of Problems
- **Node Limit Issue**: User encountered an error when trying to request 512 nodes due to a limit of 500 nodes in the big partition.

## Solutions
- **Node Limit Adjustment**: The node limit was increased from 500 to 512 to accommodate the user's request.

## Documentation for Support Employees

### Downtime Reservations
- **Description**: During downtimes, the entire cluster can be reserved for specific projects.
- **Action**: Coordinate with users to schedule reservations during planned downtimes.

### Big-Queue Access
- **Description**: Users can request access to the big-queue partition for larger computations.
- **Action**: Verify user credentials and grant access as needed.

### Project Communication
- **Description**: Early communication of resource needs is crucial for planning.
- **Action**: Encourage users to communicate their needs well in advance.

### Reservation Parameter
- **Description**: Use `--reservation=StroemungsRaum` for job submissions during reserved times.
- **Action**: Inform users about the reservation parameter and its usage.

### Node Limits
- **Description**: Node limits can be adjusted based on user needs and system capabilities.
- **Action**: Adjust node limits as needed and communicate changes to users.

### Error Handling
- **Description**: Users may encounter errors when requesting nodes beyond the current limit.
- **Action**: Verify the current node limit and adjust if necessary. Communicate the changes to the user.

This documentation aims to assist support employees in handling similar issues in the future.
---

### 2022120142002845_Probleme%20mit%20likwid-powermeter%20-%20evtl.%20msr%20kernel%20driver%20nicht%20geladen%3F.md
# Ticket 2022120142002845

 # HPC-Support Ticket: Probleme mit likwid-powermeter

## Problem Description
- User encountered issues with `likwid-powermeter` on the `skylakesp2` node.
- Error message indicated a problem with the affinity domain and a nil value error.
- User suspected that the kernel driver for the MSR device might not be loaded.

## Root Cause
- The issue was related to the job allocation method.
- Using `srun` with specific parameters restricted the CPU set, causing `likwid-powermeter` to fail.

## Solution
- Use `salloc` instead of `srun` for job allocation.
- Example command: `salloc --time=04:00:00 -C hwperf -w skylakesp2 -c 20`
- Ensure the `-C hwperf` flag is included to gain access to the MSRs.

## Keywords
- likwid-powermeter
- srun
- salloc
- MSR device
- cpuset
- hwperf
- job allocation

## General Learnings
- Different job allocation methods (`srun` vs `salloc`) can affect the behavior of certain tools.
- Ensure proper access to hardware resources by using the correct flags and commands.
- Documentation and support pages should be kept up-to-date to reflect the correct usage of commands.

## Additional Notes
- The HPC Admin created an issue in the LIKWID repository to address the problem: [LIKWID Issue #501](https://github.com/RRZE-HPC/likwid/issues/501)
- The documentation page for the test cluster was updated to reflect the correct usage of commands.
---

### 2024032042002386_Tier3-Access-Fritz%20%22Anja%20Langheld%22%20_%20mpt1012h.md
# Ticket 2024032042002386

 # HPC Support Ticket Conversation Analysis

## Keywords
- Account activation
- Fritz cluster
- Multi-node workload
- HDR100 Infiniband
- Quantum Monte Carlo
- Dicke-Ising model
- Phase diagram
- Criticality
- Frustrated matter systems
- gcc

## Summary
- **User Request**: Access to Fritz cluster for multi-node workload with specific hardware and software requirements.
- **Hardware Requirements**: HDR100 Infiniband with 1:4 blocking, 72 cores, 250 GB per node.
- **Software Requirements**: gcc.
- **Application**: Simulation of the Dicke-Ising model using Quantum Monte Carlo.
- **Expected Results**: Investigation of different phases, phase diagrams, criticality of phase transitions, and the effect of light on frustrated matter systems.

## Actions Taken
- **HPC Admin**: Enabled the user's account on Fritz.

## Lessons Learned
- **Account Activation**: Ensure that user accounts are promptly activated upon request.
- **Resource Allocation**: Understand the specific hardware and software requirements for user projects.
- **Application Support**: Be prepared to support complex simulations and scientific research projects.

## Root Cause of the Problem
- User needed access to the Fritz cluster for a specific research project.

## Solution
- HPC Admin enabled the user's account on Fritz.

## Documentation for Future Reference
- **Account Activation**: Follow the standard procedure for enabling user accounts on the Fritz cluster.
- **Resource Allocation**: Ensure that the requested resources (hardware and software) are available and properly configured.
- **Application Support**: Provide support for complex simulations and scientific research projects, including understanding the specific requirements and expected outcomes.
---

### 2023082342002793_jobs%20with%20high%20cpu%20load%20-%20b165da.md
# Ticket 2023082342002793

 # HPC Support Ticket: High CPU Load Issue

## Keywords
- High CPU load
- ntasks-per-node
- Job scripts
- Code performance

## Summary
- **Issue**: Some recent jobs have unusually high CPU load.
- **Affected Jobs**: Jobs with `ntasks-per-node` different from 72.
- **Root Cause**: The code performs better with 72 tasks per node.
- **Solution**: User will run test calculations to identify the reason for better performance with 72 tasks per node.

## Lessons Learned
- High CPU load can be indicative of suboptimal job configuration.
- The number of tasks per node can significantly impact code performance.
- It is important to test and optimize job scripts for better resource utilization.

## Actions Taken
- HPC Admin notified the user about the high CPU load issue.
- User acknowledged the issue and planned to run test calculations to investigate the cause.
- The ticket was closed after the user's response.

## Follow-up
- No further action required from HPC Admin at this time.
- User will conduct tests to optimize job configuration.
---

### 2024013042002307_low%20cpu%20usage%20-%20b133ae.md
# Ticket 2024013042002307

 # HPC Support Ticket: Low CPU Usage

## Keywords
- Low CPU usage
- MPI tasks
- Hybrid OpenMP/MPI jobs
- ClusterCockpit
- Job script configuration
- Input parameters
- Performance metrics

## Summary
The user experienced low CPU usage in their recent jobs, with only one MPI task doing any work. The HPC Admin suggested checking the jobs and provided a tip for hybrid OpenMP/MPI jobs. The user suspected incorrect input parameters in their code.

## Root Cause
- Incorrect input parameters in the user's code, causing only one MPI task to perform work.

## Solution
- The user should verify and correct the input parameters in their code.
- For hybrid OpenMP/MPI jobs, add `export SRUN_CPUS_PER_TASK=$SLURM_CPUS_PER_TASK` to the job script.

## Additional Notes
- The ClusterCockpit can be used to check different performance metrics for jobs.
- A sudden drop in FLOPS in the user's latest jobs was caused by file system issues, as reported by the HPC Admin.

## Follow-up
- The user should monitor their jobs using the ClusterCockpit to ensure the issue is resolved.
- If the problem persists, further investigation into the code and input parameters is needed.
---

### 2021071442002565_Frage%3A%20Queuepriorit%C3%83%C2%A4ten%20auf%20TinyFAT.md
# Ticket 2021071442002565

 # HPC-Support Ticket Conversation Analysis

## Keywords
- Queue Prioritization
- Fairshare Configuration
- Job ID Difference
- Queue Visibility
- Job Scheduling
- Resource Allocation
- Debugging Jobs
- Slurm Configuration

## What Can Be Learned

### Queue Prioritization
- The TinyFAT cluster nodes tf060-tf095 were acquired by specific professors, and their research groups have priority in the queue.
- Prioritization is managed through the Fairshare configuration.
- Additional prioritization mechanisms are being tested on TinyGPU and may be implemented on TinyFAT after successful trials.

### Queue Visibility
- The current Slurm configuration does not allow users to see the entire queue, only their own jobs.
- Users have requested visibility of the entire queue to better estimate job start times.
- The HPC Admins have not provided a specific reason for the queue not being visible but mentioned that jobs are not processed in the order they are submitted.

### Job Scheduling and Resource Allocation
- Job scheduling is influenced by factors such as Fairshare, resource requirements, and job priority.
- A large difference in job IDs (e.g., 2600) does not necessarily indicate a long queue; it could be due to the submission of many short jobs.
- Single-core jobs may have lower priority due to resource allocation and Fairshare considerations.

### Debugging Jobs
- Users have expressed a need for debugging jobs, which may require interactive sessions or quick access to resources.
- The HPC Admins suggested using alternative partitions (e.g., broadwell512) for faster job processing when debugging.
- A dedicated node for short jobs or debugging sessions may be considered if there is frequent demand.

### Solutions and Recommendations
- **Queue Visibility**: Consider implementing a feature to allow users to see the entire queue, as this is a common feature on other clusters and can help users plan their work.
- **Job Scheduling**: Communicate the factors influencing job scheduling to users, so they understand why jobs may not be processed in submission order.
- **Debugging Jobs**: Offer alternative partitions or dedicated nodes for debugging and short jobs to improve user experience and cluster efficiency.

This analysis aims to provide insights into common user concerns and potential improvements for the HPC support team.
---

### 2024100942002447_Tier3-Access-Fritz%20%22Guillaume%20Fl%C3%83%C2%A9%22%20_%20aj90ibod%40fau.de.md
# Ticket 2024100942002447

 # HPC Support Ticket Analysis

## Keywords
- Tier3 Access
- Fritz
- Multi-node workload
- HDR100 Infiniband
- Fortran compiler (ifort)
- MPI (openmpi)
- Solver (MUMPS)
- Nonlinear Inversion (NLI) method
- Magnetic Resonance Elastography (MRE)
- Brain mechanics
- CRC1540

## Summary
- **User Request:** Access to Fritz for multi-node workload with specific software requirements for brain mechanics research using the NLI method.
- **Initial Response:** Access granted to the user's account (mfqb101h).
- **Additional Request:** Access for a collaborator's account (mfqb102) to facilitate the integration of the NLI method.
- **Admin Response:** Clarification that the collaborator has a different account (mfqb100h) and access granted to Fritz.

## Root Cause
- User needed access to Fritz for a collaborative project involving complex brain mechanics research.
- Collaborator's account was initially misidentified, leading to a request for access to the wrong account.

## Solution
- Access granted to the user's account (mfqb101h).
- Correct collaborator's account identified (mfqb100h) and access granted to Fritz.

## General Learnings
- Importance of accurate account identification for collaborative projects.
- Efficient communication between users and HPC admins to resolve access issues.
- Understanding the specific software and hardware requirements for complex research projects.

## Documentation for Future Reference
- Ensure users provide accurate account details for collaborators.
- Verify account information before granting access to avoid confusion.
- Maintain clear communication channels for resolving access and software requirement issues.
---

### 2021062342001005_Fw%3A%20Job%20Performance%20Reports.md
# Ticket 2021062342001005

 # HPC Support Ticket: Job Performance Reports

## Keywords
- Roofline reports
- Scalar
- SP/AVX
- FLOPS
- Double precision (DP)
- Single precision (SP)
- Job performance

## Summary
The user is evaluating job performance on the HPC system using roofline reports and has questions about interpreting the data.

## User Questions
1. What does scalar and SP/AVX mean?
2. Why are FLOPS shown as 2DP+SP?
3. What does it mean when points are above the blue line but below the orange line?

## HPC Admin Responses
1. **Scalar vs SP/AVX**:
   - **Scalar**: Limit for code performing one floating point addition or multiplication per cycle.
   - **SP/AVX**: Limit when AVX SIMD instructions are used, allowing for multiple single precision (SP) or double precision (DP) operations per cycle.

2. **FLOPS Representation**:
   - FLOPS are shown as 2DP+SP to account for both single and double precision operations. A DP operation is counted as two SP operations.

3. **Points Above Blue Line**:
   - Points reaching the blue "scalar" limit line indicate the code uses only scalar instructions or not every cycle executes an AVX floating point instruction.
   - The gap to the SP/AVX line shows the potential for more floating point operations, but this depends on the algorithm and its implementation.

## General Learnings
- Understanding roofline reports helps in evaluating job performance.
- Scalar and SP/AVX limits represent different levels of floating point operations.
- FLOPS representation as 2DP+SP accounts for both single and double precision operations.
- Points above the blue line but below the orange line indicate potential for optimization but require deeper analysis.

## Root Cause
The user needs clarification on the interpretation of roofline reports, specifically the meaning of scalar and SP/AVX limits, FLOPS representation, and the significance of points above the blue line.

## Solution
The HPC Admin provided detailed explanations for each of the user's questions, helping them understand the roofline reports better.
---

### 2023062042001196_Regarding%20the%20Fritz%20access%20-%20iwia053h.md
# Ticket 2023062042001196

 # HPC Support Ticket Conversation Analysis

## Keywords
- Fritz access
- Node hours
- Core hours
- NHR application
- Fluid dynamics dataset
- Deep learning models
- waLBerla framework
- Tier3 project

## Summary
A user requested access to the Fritz HPC system with a high number of node hours (100,000 node hours, equivalent to 7.2 million core hours) for a fluid dynamics dataset project. The HPC admin questioned the high resource requirement and requested justification. The user provided detailed justification for the need for high node hours. The HPC admin then informed the user that an NHR application by the supervisor is required for such high resource allocation.

## Root Cause of the Problem
- High resource request (100,000 node hours) for a Tier3 project.
- Delay in access due to the need for justification and NHR application.

## Solution
- The user provided detailed justification for the high resource requirement.
- The HPC admin informed the user about the need for an NHR application by the supervisor and provided the application template.

## General Learnings
- High resource requests may require detailed justification and additional applications (e.g., NHR application).
- Clear communication between the user and HPC admin is crucial for resolving access and resource allocation issues.
- Understanding the project's objectives and resource requirements can help in making informed decisions about resource allocation.

## Related Documentation
- [NHR Application Rules](https://hpc.fau.de/systems-services/documentation-instructions/nhr-application-rules/)
---

### 2022123042000284_job-queue.md
# Ticket 2022123042000284

 # HPC Support Ticket: Job Queue

## Keywords
- Job queue
- Budget
- Priority
- Compute cycles
- Holiday peak usage

## Problem
- User's jobs stuck in queue.
- Concern about budget depletion.
- Urgent job processing required.

## Root Cause
- High demand on HPC cluster (Fritz) due to holiday peak usage.
- Over 2000 jobs waiting in the queue.

## Solution
- HPC Admin prioritized the user's urgent job.
- User advised to submit an extension proposal for additional resources.

## General Learnings
- High demand periods can lead to job queue congestion.
- Projects may consume significant compute cycles, impacting job processing times.
- HPC Admin can prioritize jobs upon user request.
- Users should plan and request additional resources in advance for critical tasks.
---

### 2018080342001395_LIKWID%204.3.2%20auf%20Emmy%3A%20Taktfrequenz%20nicht%20einstellbar.md
# Ticket 2018080342001395

 # HPC Support Ticket: LIKWID 4.3.2 auf Emmy: Taktfrequenz nicht einstellbar

## Keywords
- LIKWID 4.3.2
- likwid-setFrequencies
- Segmentation fault
- Root privileges
- Lock file
- Uncore frequency
- Governor settings
- System monitoring

## Problem Description
- User unable to set CPU frequency using `likwid-setFrequencies` on Emmy cluster.
- Command `likwid-setFrequencies -f 2.2` results in a segmentation fault.
- User suggests using `likwid-setFrequencies -reset -t 1` to revert changes.

## Root Cause
- The issue is related to the lock file used by LIKWID.
- Attempting to reset frequencies with `likwid-setFrequencies -reset -t 1` fails due to lock file issues.
- Root privileges are required for certain operations, but the lock file prevents proper execution.

## Troubleshooting Steps
- HPC Admins attempted to run the commands as root but encountered errors.
- Investigation revealed issues with reading data from registers and input/output errors.
- Lock file removal temporarily resolved the issue but disrupted system monitoring.

## Solution
- The problem is identified as a bug in LIKWID where certain operations require the lock file but do not handle it correctly.
- A new command `-ureset` is suggested to reset Uncore frequency separately.
- Governor settings can be specified with `-g` option during reset.
- It is decided not to fix the issue broadly due to potential misleading outputs on other clusters.
- For specific needs, dedicated nodes with a special LIKWID version can be provided.

## Conclusion
- The issue with setting CPU frequencies using LIKWID on Emmy is complex and involves lock file handling and root privileges.
- The problem is deemed as "won't fix" due to potential complications on other clusters.
- For critical needs, dedicated nodes with custom LIKWID configurations can be allocated.

## Additional Notes
- The downtime on 17.09 was mentioned but not addressed.
- The issue will be announced at the next HPC User Colloquium.
- Further discussion with developers concluded that the issue will not be fixed broadly.
---

### 2024021542000292_weird%20behavior%20on%20meggie.md
# Ticket 2024021542000292

 # HPC Support Ticket: Weird Behavior on Meggie

## Keywords
- Login delay
- Core allocation
- Meggie cluster
- Molecular dynamics simulations
- Full node request

## Summary
A user reported two issues on the Meggie cluster:
1. Long delay after login.
2. Unexpected core allocation for molecular dynamics simulations.

## Root Cause
1. **Login Delay**: Technical difficulties during the week caused intermittent login delays.
2. **Core Allocation**: Meggie cluster only allows full node requests, each node has 20 cores.

## Solution
1. **Login Delay**: The issue was resolved by HPC Admins on the same day. Users should check the Message of the Day (MOTD) for updates.
2. **Core Allocation**: Users should either batch jobs together to utilize all cores or use a different cluster like Woody for individual core requests.

## General Learnings
- Meggie cluster nodes have 20 cores each and only full nodes can be requested.
- Technical issues can cause temporary login delays.
- Users should be informed about cluster-specific resource allocation policies.

## Related Parties
- HPC Admins
- 2nd Level Support Team
- Users of Meggie cluster
---

### 2024041942004269_No%20updates%20on%20ClusterCockpit%20when%20simulating%20on%20Woody.md
# Ticket 2024041942004269

 # HPC Support Ticket: No Updates on ClusterCockpit

## Keywords
- ClusterCockpit
- Monitoring
- Woody Cluster
- Job Tracking

## Issue
- User reported that monitoring information on ClusterCockpit was not updating.
- The last update was on April 10, despite continued use of the cluster.

## Root Cause
- Some nodes of the Woody cluster were not included in the monitoring system.

## Solution
- HPC Admins fixed the issue by including the missing nodes in the monitoring system.
- Users should now be able to see their jobs in ClusterCockpit.

## General Learnings
- Monitoring issues can occur due to nodes not being included in the monitoring system.
- Regular checks and user feedback are essential for maintaining accurate monitoring data.
- Quick resolution by HPC Admins ensures minimal disruption to user activities.

## Next Steps for Support
- Verify that all nodes are included in the monitoring system.
- Regularly update and maintain the monitoring tools to prevent similar issues.
- Encourage users to report any discrepancies in monitoring data promptly.
---

### 2022110242001882_lange%20Laufzeit%20einiger%20Jobs.md
# Ticket 2022110242001882

 ```markdown
# HPC Support Ticket: Long Runtime of Some Jobs

## Summary
User observed that some jobs take significantly longer to complete than others without an apparent reason. Possible causes could be hardware issues or unfavorable node distribution regarding network topology.

## Keywords
- Long job runtime
- Hardware issues
- Network topology
- Node distribution
- Job performance

## Problem Description
- User noticed that some jobs take much longer to complete than others.
- Possible causes mentioned: hardware problems or unfavorable node distribution regarding network topology.

## Investigation
- HPC Admin requested specific job IDs for further investigation.
- Identified nodes f0254 and f0255 as problematic based on abnormal IPC values.
- Listed jobs that ran on these nodes and their statuses.
- Provided logs indicating reboots and other issues with specific nodes.

## Findings
- Several nodes were identified as problematic during HPL/Top500 measurements.
- Nodes f0254 and f0255 were particularly problematic, with jobs experiencing timeouts and failures.
- Other nodes also showed issues such as processor errors, thermal trips, and HCA check failures.

## Solution
- Nodes were rebooted, which should have resolved the issues.
- If the problem persists, the ticket can be reopened for further investigation.

## Conclusion
- The long runtime of some jobs was likely due to hardware issues with specific nodes.
- Rebooting the problematic nodes should have resolved the issue.
- Users should monitor job performance and report any further issues.
```
---

### 2022041242002652_Gromacs%20Multinode%20auf%20Fritz%20%5Bbcpc000h%20%5D.md
# Ticket 2022041242002652

 # HPC Support Ticket: Gromacs Multinode auf Fritz

## Keywords
- Multinode User
- Gromacs
- Fritz
- Job Submission
- Documentation

## Summary
The user has been enabled as a multinode user on the Fritz system, allowing them to submit jobs that require multiple nodes. The HPC Admin provided a link to the Gromacs documentation page, which includes an example script for running Gromacs on multiple nodes.

## Root Cause
- The user needed guidance on how to submit multinode jobs for Gromacs on the Fritz system.

## Solution
- The HPC Admin directed the user to the Gromacs documentation page, which contains an example script for running Gromacs on multiple nodes.
- The user was informed that they can seek further assistance if needed.

## What Can Be Learned
- Users can be enabled as multinode users to submit jobs that require multiple nodes.
- The Gromacs documentation page provides an example script for running Gromacs on multiple nodes.
- Users should refer to the documentation for guidance and can seek further assistance from the HPC support team if needed.

## Documentation Link
- [Gromacs Documentation](https://hpc.fau.de/systems-services/systems-documentation-instructions/special-applications-and-tips-tricks/gromacs/?preview_id=5834&preview_nonce=2d9cdd98f1&_thumbnail_id=-1&preview=true#collapse_3)
---

### 2018052942001824_Account%20hpcv070h%20auf%20meggie%20gesperrt.md
# Ticket 2018052942001824

 # HPC Support Ticket: Account Suspension Due to Memory Overuse

## Keywords
- Account suspension
- Memory overuse
- Node reboot
- Linpack
- Batch system daemons
- Omnipath buffers
- Interactive session
- Memory allocation error

## Summary
A user's account was suspended due to excessive memory usage, causing node failures and requiring manual reboots.

## Root Cause
- The user's Linpack jobs were consuming more memory than available on the compute nodes.
- This led to insufficient memory for critical system processes like batch system daemons and Omnipath buffers.
- Nodes required manual reboots to recover, causing disruption and additional workload for HPC admins.

## User's Questions and Concerns
- Sufficient system memory for jobs.
- Node recovery in case of memory allocation errors.
- Impact of incorrect resource requests.
- Timeline and extent of node failures caused by the user.

## Solution and Prevention
- **User Education**: Informed the user about the importance of proper memory allocation and the impact of excessive usage.
- **Account Reactivation**: The user's account was reactivated after acknowledging the issue and committing to more careful resource management.
- **Future Prevention**: Encouraged the user to double-check job configurations before submission to avoid similar issues.

## Notes for Support Team
- Ensure users are aware of the memory limits and the importance of leaving sufficient memory for system processes.
- Monitor for repeated memory overuse and provide guidance to prevent account suspensions.
- Document and communicate the impact of excessive resource usage on the overall system stability.

## Follow-up Actions
- Provide the user with specific details about the nodes affected and the timeline of failures if available.
- Offer additional training or resources on efficient job configuration and resource management.
---

### 2025012342002855_Tier3-Access-Fritz%20%22Katharina%20Distler%22%20_%20bcpc102h.md
# Ticket 2025012342002855

 # HPC Support Ticket Analysis: Tier3-Access-Fritz

## Keywords
- Tier3 Access
- Fritz
- Single-node throughput
- Multi-node workload
- GROMACS
- Metadynamics
- GPCR-ligand complexes
- Pain medication development

## Summary
A user requested access to the Fritz HPC system for a project involving metadynamics of GPCR-ligand complexes using GROMACS. The request included specifications for single-node and multi-node workloads, requiring special justification for resource allocation.

## User Request Details
- **Contact:** User's contact information provided.
- **Resource Needs:**
  - Single-node throughput: 72 cores, 250 GB
  - Multi-node workload: HDR100 Infiniband with 1:4 blocking; per node: 72 cores, 250 GB
- **Compute Time:** 10,000 node hours on Fritz
- **Required Software:** GROMACS
- **Application:** Metadynamics of GPCR-ligand complexes (single walker)
- **Expected Results:** Development of new pain medication

## HPC Admin Response
- The request was initially deferred.
- The user was later granted access to use Fritz.

## Lessons Learned
- **Resource Allocation:** Users may require special justification for high resource allocations.
- **Access Granting:** HPC Admins can grant access to specific systems after reviewing the request.
- **Software Requirements:** Ensure that the required software (e.g., GROMACS) is available and supported on the requested system.

## Root Cause and Solution
- **Root Cause:** The user needed access to the Fritz system for a specific project with high resource requirements.
- **Solution:** The HPC Admin reviewed the request and granted access to the Fritz system.

## Documentation for Support Employees
When handling similar requests, ensure to:
1. Review the resource requirements and justifications provided by the user.
2. Verify the availability of the required software on the requested system.
3. Grant access after thorough review and approval.

This documentation can be used as a reference for handling future access requests and resource allocation on the Fritz HPC system.
---

### 2024090642001732_Multi-node%20benchmark%20jobs%20on%20ALEX.md
# Ticket 2024090642001732

 # HPC Support Ticket: Multi-node Benchmark Jobs on ALEX

## Keywords
- Multi-node jobs
- Benchmarking
- A100 nodes
- A40 nodes
- GPU utilization
- Draining costs
- Manual scheduling

## Summary
A user requested access to multiple nodes on ALEX for strong scaling benchmarks. The request involved up to 3 A100 nodes and up to 6 A40 nodes, with each benchmark lasting 5-10 minutes.

## Root Cause
- The user had two HPC accounts and needed to specify which one should be enabled for multi-node jobs.
- Draining nodes for short jobs (5-10 minutes) is inefficient due to the high draining costs (at least 12 hours per node).

## Solution
- The user specified the account to be enabled (b168dc12).
- The user agreed to coordinate benchmarks with the HPC Admins to minimize draining costs through manual scheduling.
- The user decided to hold off on the benchmarks and, if run, will combine them into a single job to increase runtime and inform the HPC Admins before scheduling.

## Lessons Learned
- Always specify the account to be enabled when requesting multi-node access.
- Coordinate short-duration benchmarks with HPC Admins to minimize draining costs.
- Consider combining short jobs into longer ones to improve efficiency.

## Next Steps
- Enable the specified account for multi-node jobs.
- Coordinate with the user for manual scheduling if benchmarks are to be run.
---

### 2021111242000624_Access%20to%20test%20cluster.md
# Ticket 2021111242000624

 ```markdown
# HPC-Support Ticket Conversation: Access to Test Cluster

## Keywords
- Multigrid preconditioned Krylov methods
- Helmholtz PDE
- ExaStencils DSL
- Test architecture
- Performance evaluation
- Large grids
- HPC application form
- Target systems

## Summary
- **User Issue**: The user has implemented multigrid preconditioned Krylov methods for solving the Helmholtz PDE using the ExaStencils DSL. They need access to the test architecture to generate and evaluate the performance of these methods on large grids.
- **Root Cause**: The user does not have access to the test cluster.
- **Solution**: The HPC Admin instructs the user to fill out the HPC application form and add "test-cluster" to the list of target systems.

## What Can Be Learned
- Users need to fill out an HPC application form to gain access to specific systems.
- The form can be found at the provided link: [HPC Application Form](https://hpc.fau.de/systems-services/systems-documentation-instructions/getting-started/).
- Users should specify the target systems they need access to in the application form.

## Action Items for Support Employees
- Direct users to the HPC application form for access requests.
- Ensure users specify the target systems they need access to in the application form.
```
---

### 42068329_Job%20372896%20auf%20Woody%20braucht%20zu%20viel%20Speicher.md
# Ticket 42068329

 # HPC Support Ticket: Job 372896 auf Woody braucht zu viel Speicher

## Keywords
- Job ID: 372896
- System: Woody
- Issue: Excessive memory usage
- Swapping
- Simulation
- HPC Group

## Summary
A job on the Woody system is consuming too much memory, leading to constant swapping and potentially preventing the job from completing successfully.

## Root Cause
- The job requires more memory than available, causing it to swap frequently.

## Solution
- Modify the simulation to reduce memory usage.
- Contact the HPC Group to find suitable systems with more RAM.

## Details
- The job ID is 372896.
- The job is using 8535m of memory and 7.5g of RAM.
- The job has been running for over 129 hours.
- The user should consider optimizing the simulation to use less memory or seek alternative systems with higher memory capacity.

## Next Steps
- User should attempt to optimize the simulation.
- If optimization is not possible, contact the HPC Group for assistance in finding a more suitable system.

## Contact Information
- HPC Services
- Friedrich-Alexander-Universitaet Erlangen-Nuernberg
- Regionales RechenZentrum Erlangen (RRZE)
- Martensstrasse 1, 91058 Erlangen, Germany
- Email: hpc-support@rrze.uni-erlangen.de
- Website: [HPC Services](http://www.hpc.rrze.uni-erlangen.de/)
---

### 2022012142001918_Early-Fritz%20%22Eduard%20Neu%22%20_%20bcpc.md
# Ticket 2022012142001918

 # HPC Support Ticket Conversation Analysis

## Keywords
- GROMACS
- GPU
- CPU
- Fritz
- Alex
- Early-User
- Job Script
- Infiniband
- Single-Node
- Multi-Node
- SSH
- IPv6
- MOTD

## Summary
- **User Request**: The user initially requested to run GROMACS simulations on GPUs but later clarified that they also wanted to use CPUs on the Fritz cluster.
- **HPC Admin Response**: The admin informed the user that Fritz does not have GPUs and provided access to the Alex cluster for GPU-based simulations. Later, the admin granted access to Fritz for CPU-based simulations.
- **Issues**:
  - User confusion about hardware capabilities.
  - Limited Infiniband cards leading to restricted partition access.
- **Solutions**:
  - Clarification about hardware capabilities.
  - Granting access to the appropriate cluster and partition.

## Detailed Analysis
- **User Error**: The user mistakenly requested GPU access on Fritz, which does not have GPUs. This was clarified as a copy-paste error.
- **Admin Action**: The admin provided access to the Alex cluster for GPU-based simulations and later granted access to the Fritz cluster for CPU-based simulations.
- **Hardware Limitations**: Due to a shortage of Infiniband cards, the user was restricted to the "singlenode" partition on Fritz.
- **Access Information**: The admin provided SSH access details and noted that the documentation for Fritz was still in progress.

## Lessons Learned
- **Clarify Hardware Capabilities**: Ensure users are aware of the hardware capabilities of different clusters.
- **Documentation**: Highlight the importance of up-to-date documentation for new clusters.
- **Communication**: Effective communication can resolve user errors and provide necessary access and information.

## Root Cause and Solution
- **Root Cause**: User confusion about hardware capabilities and admin clarification.
- **Solution**: Provide clear information about cluster capabilities and grant appropriate access based on user needs.

## Future Reference
- **For Users**: Check cluster capabilities before submitting requests.
- **For Admins**: Ensure clear communication about hardware limitations and provide necessary access and documentation.

---

This analysis can be used to resolve similar issues in the future by ensuring clear communication and providing up-to-date documentation on cluster capabilities.
---

### 2023120142001059_Nodes%20with%20Turbomole_Charmm%20Jobs%20show%20very%20high%20CPU%20load%20%5Bp101ae13%5D.md
# Ticket 2023120142001059

 # HPC Support Ticket: Nodes with Turbomole/Charmm Jobs Show Very High CPU Load

## Keywords
- High CPU Load
- Turbomole
- Charmm
- MPI
- OpenMP
- Threading
- Job Monitoring

## Summary
A user was running Charmm jobs via the Turbomole interface, resulting in unusually high CPU loads (>1000) on the nodes. The HPC admins noticed this issue but could not initially identify the cause, as the number of MPI processes seemed correct.

## Problem Description
- **High CPU Load**: Nodes showed a CPU load of >1000.
- **Job Type**: Charmm jobs running via the Turbomole interface.
- **Monitoring**: The issue was visible in the job monitoring system.

## Root Cause
- **MPI, OpenMP, and Threading Interaction**: The high load was likely due to an improper interaction between MPI, OpenMP, and threading, leading to an excessive number of processes per core (~10 processes per core on a 72-core node).

## Solution
- **Further Investigation**: The HPC admins requested a copy of the affected simulation for deeper analysis.
- **Temporary Resolution**: Since the issue had not recurred recently, it was decided to monitor future Turbomole jobs closely.

## Lessons Learned
- **Load Monitoring**: High CPU loads can indicate issues with process management.
- **MPI and OpenMP**: Proper configuration of MPI and OpenMP is crucial to avoid excessive process creation.
- **User Communication**: Ensure users are aware of the importance of monitoring job performance and reporting unusual behavior.

## Next Steps
- **Future Monitoring**: Closely monitor future Turbomole jobs to ensure the issue does not recur.
- **User Education**: Educate users on the importance of proper job configuration and the potential impacts of high CPU loads.

## References
- **Job Monitoring**: [monitoring.nhr.fau.de](https://monitoring.nhr.fau.de/)
- **HPC Support**: [support-hpc@fau.de](mailto:support-hpc@fau.de)
- **HPC Website**: [hpc.fau.de](https://hpc.fau.de/)

This documentation can be used to address similar issues in the future by providing a reference for high CPU load problems related to Turbomole and Charmm jobs.
---

### 42026240_neues%20Problem%20Townsend.md
# Ticket 42026240

 # HPC Support Ticket: New Problem with Townsend

## Keywords
- Infiniband
- Linux kernel update
- Security vulnerability
- ABI version
- librdmacm
- libibverbs
- mpirun warnings

## Problem Description
- User encountered new error messages after a recent Linux kernel update.
- Errors related to Infiniband drivers and ABI version.

## Root Cause
- Linux kernel update introduced a security vulnerability that affected Infiniband drivers.

## Solution
- HPC Support identified and resolved the issue with Infiniband drivers.
- Jobs were temporarily halted until the problem was fixed.
- mpirun currently shows warnings about `dat.conf`, but these are non-critical.

## Lessons Learned
- Regular updates can introduce new issues, especially with critical components like Infiniband drivers.
- Quick identification and resolution of such issues are crucial to maintain system functionality.
- Non-critical warnings from tools like mpirun should be monitored but do not necessarily indicate a major problem.
---

### 2022031542001748_Finale%20Simulationen%20auf%20Meggie%20f%C3%83%C2%BCr%20Doktorarbeit.md
# Ticket 2022031542001748

 # HPC-Support Ticket Conversation Summary

## Keywords
- Simulation
- Meggie
- Fritz
- Priority
- Dateigröße
- Komprimierung
- Optimierung
- Doktorarbeit

## General Learnings
- **Resource Allocation**: When a cluster is heavily loaded, it may be beneficial to switch to another cluster if available.
- **Dateigröße Anomalies**: Anomalies in file sizes can sometimes be due to network file system issues.
- **Code Optimization**: Users may need to prioritize other tasks before they can optimize their code.

## Conversation Summary

### Initial Request
- **User**: Requested to run 40 simulations on Meggie for their doctoral thesis, each using 7-10 nodes and running for about 7 days.
- **User**: Asked if the priority of their jobs could be maintained for a month despite the high number of simulations.

### HPC Admin Response
- **HPC Admin**: Suggested switching to Fritz due to high load on Meggie.
- **HPC Admin**: Provided access to 64 nodes on Fritz, estimating that 2-3 Fritz nodes would be equivalent to 7-10 Meggie nodes.

### User Follow-up
- **User**: Noticed anomalies in file sizes on Fritz, with files appearing much smaller than expected.
- **HPC Admin**: Attributed the anomalies to potential issues with network file systems and confirmed no compression was used on the dateisystems.

### Progress Updates
- **User**: Reported good progress on Fritz and expected to complete the simulations by the end of April.
- **HPC Admin**: Checked in on the user's progress and inquired about code optimization.

### Final Update
- **User**: Confirmed completion of measurements and mentioned they would resume code optimization in August due to teaching commitments.

## Root Cause of Problems
- **High Load on Meggie**: The initial cluster was heavily loaded, leading to the suggestion to switch to Fritz.
- **File Size Anomalies**: Anomalies in file sizes were likely due to network file system issues.

## Solutions
- **Switch to Fritz**: The user was able to complete their simulations more efficiently by switching to the Fritz cluster.
- **No Compression**: Confirmed that there was no compression on the file systems, addressing the user's concern about file size anomalies.

## Future Actions
- **Code Optimization**: The user plans to resume code optimization after completing their teaching commitments.

## Documentation Links
- [Fritz Cluster Information](https://hpc.fau.de/systems-services/systems-documentation-instructions/clusters/fritz-cluster/)

This summary provides a concise overview of the conversation, highlighting key points and solutions for future reference.
---

### 2019062642001175_Knotenzahl%20und%20MPI-Prozesszahl%20auf%20Emmy%20passen%20nicht%20_%20bcpc000h.md
# Ticket 2019062642001175

 # HPC Support Ticket: Knotenzahl und MPI-Prozesszahl auf Emmy passen nicht

## Keywords
- MPI-Prozesse
- Knotenzahl
- Domain decomposition
- SLURM_JOB_NUM_NODES
- mpirun
- pmemd
- Amber
- Meggie
- Woody

## Problem
- User's jobs on Meggie had a mismatch between the requested number of nodes (20) and the number of MPI processes started (25*18).
- Initial runs with matching node and MPI process combinations resulted in domain decomposition errors.

## Root Cause
- The domain decomposition error occurred because the number of ranks (310) was not compatible with the given box and minimum cell size.
- The mismatch between nodes and MPI processes led to inefficient resource usage, with some nodes receiving more processes than others.

## Solution
- HPC Admin suggested adjusting the number of nodes or MPI processes to ensure a balanced workload.
  - Option 1: Request 25 nodes with `-ppn 18`.
  - Option 2: Request 23 nodes with `-ppn 20` and explicitly set `-np 450`.
- For serial jobs, use a single node or switch to Woody for better performance and cost efficiency.
- Use `$SLURM_JOB_NUM_NODES` in the job script to dynamically adjust the number of nodes.

## Additional Information
- The user's previous jobs with Amber ran serially despite requesting multiple nodes. To run Amber in parallel, use `mpirun` and `pmemd.MPI`.
- For serial jobs, consider using Woody for faster and cheaper serial computations.

## Lessons Learned
- Ensure the number of MPI processes is compatible with the requested nodes to avoid domain decomposition errors.
- Balance the workload across nodes to optimize resource usage.
- Use appropriate commands and modules for parallel processing in software like Amber.
- Consider the most efficient cluster for the type of job (serial vs. parallel).
---

### 2019050242002578_MPI%20_%20Mellanox%20Fehler.md
# Ticket 2019050242002578

 ```markdown
# HPC Support Ticket: MPI / Mellanox Error

## Keywords
- MPI
- Mellanox
- InfiniBand
- Star-CCM+
- QP operation error
- IBV connection broken
- OpenSM log
- Node failure

## Problem Description
The user encountered sporadic errors during large simulations (32 or 64 nodes) with Star-CCM+ on the HPC cluster. The errors included:
- `mlx4: local QP operation err` with various QPN and WQE index values.
- `MPI_Waitall: IBV connection to ... is broken. ibv_poll_cq(): bad status 2`.

These errors occurred intermittently, with some simulations failing and others succeeding under similar conditions.

## Root Cause
The HPC Admin suspected a faulty node based on the clean OpenSM log, indicating no widespread issues with the InfiniBand fabric.

## Solution
No specific solution was provided in the conversation. The HPC Admin noted that the lack of response from the user suggested the issue might not be critical.

## General Learnings
- Intermittent MPI errors with Mellanox cards can indicate a problem with specific nodes rather than the entire InfiniBand fabric.
- Checking the OpenSM log can help diagnose whether the issue is localized or systemic.
- Lack of user follow-up may indicate the issue is not urgent or has been resolved independently.
```
---

### 2023020142000659_Multi-node%20jobs%20on%20the%20Alex%20cluster.md
# Ticket 2023020142000659

 # Multi-Node Jobs on Alex Cluster

## Keywords
- Multi-node jobs
- Alex cluster
- A40 nodes
- A100 partition
- Interconnect
- QoS (Quality of Service)

## Summary
A user requested multi-node job capability for their allocation on the Alex cluster, specifically for A40 resources. The HPC Admin enabled multi-node jobs for both A40 and A100 partitions but noted potential performance issues due to weak interconnect on A40 nodes.

## Problem
- User required multi-node job submissions for their allocation.
- Concerns about interconnect performance on A40 nodes.

## Solution
- HPC Admin enabled multi-node jobs for the user's account in both A40 and A100 partitions.
- User instructed to add `--qos=a40multi` or `--qos=a100multi` when submitting multi-node jobs.
- User acknowledged the potential performance issues and planned to run tests.

## Notes
- Multi-node performance on A40 nodes is estimated to be around 25-35% utilization.
- Users should be aware of the interconnect limitations when planning multi-node jobs on A40 nodes.

## Follow-Up
- Monitor user feedback on multi-node job performance.
- Provide additional support if performance issues arise.
---

### 2021102642002438_Parallelisierung%20mit%20joblib%20%28python%29%20-%20meggie%20-%20%20gwgi008h.md
# Ticket 2021102642002438

 # HPC Support Ticket: Parallelization with Joblib (Python)

## Keywords
- Joblib
- Parallelization
- Python
- HPC
- SLURM
- srun
- Backends

## Problem Description
- User's Python script for simulating precipitation uses Joblib for parallelization.
- Parallelization works efficiently on the user's Mac but not on the HPC system.
- The script runs faster interactively than when submitted as a job via SLURM with the same CPU count.
- The script runs slower with more CPUs on the HPC system.

## Observed Behavior
- Interactive run is faster than SLURM job submission.
- Increasing CPU count results in slower execution times:
  - 20 CPUs: 4:30
  - 8 CPUs: 4:44
  - 4 CPUs: 5:14
  - 2 CPUs: 5:27
  - 1 CPU: 1:55

## Possible Causes
- Incorrect configuration in the batch script.
- Joblib compatibility issues with the HPC environment.
- Inefficient resource allocation or initialization in the SLURM job.

## Suggested Solutions
- Test different backends in Joblib.
- Use `srun` before the Python command in the batch script to ensure proper resource allocation.

## HPC Admin Response
- No prior experience with Joblib.
- Suggested testing different backends and using `srun` before the Python command.

## Conclusion
- The issue might be related to resource allocation or initialization in the SLURM job.
- Testing different backends and using `srun` could potentially resolve the problem.

## Next Steps
- User should modify the batch script to include `srun` and test different Joblib backends.
- Monitor the performance and report back to HPC support if the issue persists.

## Files and Scripts
- Scripts and files are located at: `/home/titan/gwgk/gwgi008h/OPM/OPM_XL/TEST`
- Parallelization code is in `OPM_parallel.py` lines 135-140.
- Batch script: `run_parallel.sh`
- Test dataset: `test10.txt`

## Additional Notes
- The user has hardcoded the number of CPUs in the script to ensure the correct count is used.
- The issue is reproducible with longer test datasets.
---

### 2018052842002941_Account%20hpcv072h%20auf%20meggie%20gesperrt.md
# Ticket 2018052842002941

 # HPC Support Ticket: Account Suspension Due to Memory Overuse

## Keywords
- Account suspension
- Memory overuse
- Linpack
- Job parallelization
- Node crash
- Slurm
- HPL.dat

## Summary
A user's account was suspended due to their jobs causing node crashes by attempting to allocate more memory than available. The issue was related to running Linpack tests with improper matrix sizes, leading to excessive memory usage.

## Root Cause
- The user attempted to run Linpack tests on multiple nodes simultaneously.
- The matrix size for larger node counts was inappropriately used for smaller node counts, leading to memory overuse.
- The user's script overwrote the matrix size file, causing incorrect configurations.

## Impact
- Node crashes requiring manual reboots.
- Disruption of other users' jobs due to timeouts.

## Actions Taken
1. **Initial Suspension**: The user's account was suspended due to the disruption caused.
2. **Reactivation**: The account was reactivated after the user acknowledged the issue and apologized.
3. **Re-suspension**: The account was suspended again after the issue recurred without notification from the user.

## Solution
- Ensure proper configuration of matrix sizes for Linpack tests.
- Avoid overwriting configuration files during job submissions.
- Monitor job submissions to prevent excessive memory usage.

## Lessons Learned
- Proper job configuration is crucial to prevent resource overuse.
- Communication with the support team is essential when issues recur.
- Understanding the impact of job parallelization on system stability is important.

## Recommendations
- Users should double-check their job configurations before submission.
- Regular monitoring of job performance to detect and address issues promptly.
- Provide clear guidelines and training on proper job submission practices.
---

### 2022092842003738_Zugriff%20auf%20mehrere%20Alex-Nodes.md
# Ticket 2022092842003738

 ```markdown
# HPC Support Ticket: Access to Multiple Alex Nodes

## Keywords
- Multi-Node Access
- Performance Measurements
- HPC Account
- QoS (Quality of Service)
- Alex Cluster
- GPU Hours

## Problem
- User has access to a single Alex node but requires access to multiple nodes for performance measurements.
- User does not need extensive GPU hours, only access for scaling tests.

## Solution
- HPC Admin granted access to `qos=a100multi` and `qos=a40multi`.
- Provided documentation link for Multi-Node Jobs: [Alex Cluster Documentation](https://hpc.fau.de/systems-services/documentation-instructions/clusters/alex-cluster/#collapse_16)

## General Learnings
- Users needing multi-node access for performance testing should contact HPC Support.
- HPC Admins can enable specific QoS settings to allow multi-node access without requiring extensive GPU hours.
- Documentation and instructions for Multi-Node Jobs are available on the HPC website.
```
---

### 2019080242000654_BUG%20in%20pstree.md
# Ticket 2019080242000654

 # HPC Support Ticket: BUG in pstree

## Keywords
- pstree
- Bug
- Parent processes
- Parallel vs. serial execution
- MPI
- CentOS
- Ubuntu
- psmisc

## Problem Description
The user reported an issue with the `pstree` command, which is used in their program to determine whether it was started in parallel or serial mode. The `pstree` command has a known bug that has not been fixed since 2016.

## Root Cause
- The `pstree` command has a bug that affects its functionality.
- The user's program relies on `pstree` to determine the execution mode (parallel vs. serial).

## Solution
- The HPC system (EMMY) uses CentOS, not Ubuntu, and updating only the `psmisc` package is not feasible due to potential system instability.
- The user can compile a bug-free version of `psmisc` and place the `pstree` binary in their home directory, updating the PATH to use this version.
- Alternatively, the user can use MPI functions to determine the execution mode:
  ```c
  MPI_Init(&argc, &argv);
  MPI_Comm_size(MPI_COMM_WORLD, &size);
  if (size > 1) {
      /* PARALLEL */
  } else {
      /* SERIELL */
  }
  ```
- Another option is to read the command line from the `/proc/` filesystem to determine the parent process.

## Lessons Learned
- Always use the correct support email address for HPC-related issues.
- Updating central system packages can be risky and should be avoided unless part of a major system update.
- There are alternative methods to determine the execution mode of a program, such as using MPI functions or reading the `/proc/` filesystem.
- Compiling and using custom versions of system tools can be a workaround for bugs in the default versions.

## Additional Notes
- The user's program checks the parent processes to differentiate between parallel and serial execution, especially to handle cases where users incorrectly start the program with `mpiexec -n 1`.
- The HPC admins provided detailed guidance on alternative methods to achieve the desired functionality without relying on the buggy `pstree` command.
---

### 2019030742001322_Quantum%20Espresso%20Jobs%20auf%20Emmy%20_%20mpp3004h.md
# Ticket 2019030742001322

 # HPC Support Ticket: Quantum Espresso Jobs auf Emmy

## Keywords
- Quantum Espresso
- Job Performance
- MPI Processes
- System Monitoring
- Memory Usage
- Parallelization
- Job Optimization

## Summary
- **Issue**: Poor performance and memory issues in multi-node Quantum Espresso jobs.
- **Root Cause**: Inefficient distribution of MPI processes across nodes leading to suboptimal performance and memory exhaustion.
- **Solution**: Adjust the number of MPI processes per node to ensure balanced load and efficient resource utilization.

## Detailed Analysis
### Performance Issue
- **Problem**: 5-node jobs with 160 MPI processes showed poor performance compared to 1-node jobs.
- **Cause**: Uneven distribution of MPI processes across nodes (40 processes on nodes 1-3, 20 on nodes 4-5).
- **Solution**: Reduce the number of nodes to 4, ensuring 40 MPI processes per node for balanced performance.

### Memory Issue
- **Problem**: Job termination due to memory exhaustion (EXIT CODE: 9).
- **Cause**: Insufficient memory on nodes, leading to job failure.
- **Solution**: Reduce the number of MPI processes per node to 20 using the command:
  ```bash
  /apps/rrze/bin/mpirun -pinexpr S0:0-9@S1:0-9 $HOME/source/q-e-qe-6.3/bin/pw.x -i 1Tsb_hse.scf.in
  ```

## Recommendations
- **Monitoring**: Use system monitoring to analyze job performance and resource usage.
- **Optimization**: Adjust the number of MPI processes per node to ensure efficient resource utilization and avoid memory exhaustion.
- **Documentation**: Access keys for monitoring data can be found at the end of job outputs for further analysis.

## Additional Notes
- **System Monitoring**: Available at [HPC Status](https://www.hpc.rrze.fau.de/HPC-Status/job-info.php).
- **Memory Limits**: Emmy nodes have ~60 GB of free memory with no swap space.
- **Job Optimization**: Reducing the number of processes per node can help in avoiding memory issues and improving performance.

## Conclusion
Proper distribution of MPI processes and monitoring job performance are crucial for optimizing Quantum Espresso jobs on Emmy. Adjusting the number of processes per node can significantly improve performance and prevent memory-related job failures.
---

### 2021041342002027_Zulassen%20von%20%3E1%20node%20jobs%20auf%20AMD%20EPYC%207502%20nodes%20%C3%A2%C2%80%C2%93%20zu%20Te.md
# Ticket 2021041342002027

 # HPC Support Ticket: Allowing Multi-Node Jobs on AMD EPYC 7502 Nodes

## Keywords
- Multi-node jobs
- AMD EPYC 7502 nodes
- Network communication
- Partition configuration
- Testing

## Problem Description
The user requested permission to run 2-node jobs on the new AMD EPYC 7502 nodes for testing purposes. The user acknowledged that the 10 Gbit network is not suitable for communication-intensive jobs but argued that their jobs require minimal communication (a few KB/s). The jobs involve calculating energy expectation values and gradients using a C++ backend (qsim), which benefits from AVX2 vectorization and higher RAM and bandwidth per core.

## Root Cause
The current partition configuration (`PartitionName=work MaxNodes=1`) does not allow multi-node jobs.

## Solution
HPC Admins created a hidden partition (`--partition=special`) that allows 2-node jobs for testing purposes. This partition is accessible to specific groups, including the user's group.

## What Can Be Learned
- **Partition Configuration**: HPC Admins can create hidden partitions to allow specific user groups to test multi-node jobs without changing the global partition configuration.
- **Job Communication**: Some jobs may require minimal network communication, making them suitable for testing on nodes with limited network bandwidth.
- **Hardware Limitations**: Certain jobs may be limited by hardware capabilities (e.g., AVX2 vectorization, RAM, bandwidth per core), necessitating the use of specific nodes.

## Follow-Up
- Test the new partition to ensure it allows 2-node jobs as expected.
- Monitor the usage of the new partition to assess its effectiveness and potential impact on the system.
- Consider adjusting partition configurations based on testing results and user feedback.
---

### 2024041142001053_Memory%20Usage%20_%20Bus%20Error.md
# Ticket 2024041142001053

 ```markdown
# HPC-Support Ticket: Memory Usage / Bus Error

## Subject
Memory Usage / Bus Error

## Keywords
- Bus Error
- RAM Verbrauch
- GPU Knoten
- A100 Knoten
- getrusage
- ru_maxrss
- cgroup
- memory.max_usage_in_bytes
- memory.usage_in_bytes

## Problem Description
User experiences frequent Bus Errors on GPU nodes, specifically A100 nodes. The user tracks maximum RAM usage using `getrusage` and reports that it stays under 40GB, which should not be a problem for the A100 nodes.

## Error Message
```
/var/tmp/slurmd_spool/job1566625/slurm_script: line 36: 1024821 Bus error (core dumped)
```

## Root Cause
The job may be consuming more RAM than allowed by the cgroup (approximately 120GB per GPU). The error suggests that the job's RAM usage spikes suddenly, which is not captured by the user's monitoring.

## Solution
- Monitor the maximum allocated memory of the cgroup:
  ```bash
  cat /sys/fs/cgroup/memory/slurm/uid_210684/job_$SLURM_JOB_ID/memory.max_usage_in_bytes
  ```
- Monitor the current memory usage:
  ```bash
  cat /sys/fs/cgroup/memory/slurm/uid_210684/job_$SLURM_JOB_ID/memory.usage_in_bytes
  ```
- Determine if the problem is specific to a particular dataset.

## Additional Information
- Job ID: 1566625
- Node list: a0535
- Total RAM usage: 50.0 GiB
- GPU utilization: 88%
- Memory utilization: 30%
- Max memory usage: 17538 MiB

## Conclusion
The Bus Error is likely due to the job exceeding the RAM limit set by the cgroup. Monitoring the cgroup memory usage can help identify the issue.
```
---

### 2022060242002515_Discussion%20about%20diagnosing%20cache%20thrashing%20in%20unique%20transpose%20problem.md
# Ticket 2022060242002515

 # Diagnosing Cache Thrashing in Unique Matrix Transposition

## Keywords
- Cache thrashing
- Matrix transposition
- Performance optimization
- `perf` tool
- Memory hierarchy
- Data traffic

## Problem Description
The user is working on improving the performance of a unique matrix transposition algorithm. The discussion on Stack Overflow hinted at cache thrashing caused by data layout and associativity. The user is inexperienced with tools like `perf` and needs guidance on diagnosing cache thrashing.

## Root Cause
- Cache thrashing due to inefficient data layout and associativity in the matrix transposition algorithm.

## Solution
- **Reference Material**: Section 3.4 of the HPC book "Introduction to High Performance Computing for Scientists and Engineers" covers matrix transposition and the problem of cache thrashing.
- **Diagnosis Method**: Measure the data traffic through the memory hierarchy (all levels) and compare it with expected values. A large discrepancy indicates excess traffic due to thrashing.

## Steps to Diagnose Cache Thrashing
1. **Read Reference Material**: Consult Section 3.4 of the HPC book for insights on matrix transposition and cache thrashing.
2. **Measure Data Traffic**: Use tools like `perf` to measure data traffic through the memory hierarchy.
3. **Compare with Expected Values**: Analyze the measured data traffic and compare it with expected values to identify any discrepancies.

## Additional Notes
- The user was advised to have a chat for further assistance if needed.
- The HPC Admins provided guidance on diagnosing cache thrashing by measuring data traffic through the memory hierarchy.

## Conclusion
Understanding and diagnosing cache thrashing involves measuring and analyzing data traffic through the memory hierarchy. Referencing relevant sections of the HPC book and using appropriate tools can help in identifying and mitigating performance issues related to cache thrashing.
---

### 2016031142001365_Jobs%20auf%20Emmy.md
# Ticket 2016031142001365

 # HPC Support Ticket Analysis: Jobs auf Emmy

## Keywords
- Job Queue
- Priority
- Rechenzeit
- Knoten
- Group Usage
- Node Failure

## Problem
- User's jobs on Emmy have not been running for several days.
- Jobs were re-queued without any notification or information on the RRZE website.

## Root Cause
- The user's job has low priority due to high resource usage by other members of their group (20% of Emmy's resources in the last 10 days).
- A previous job left a node in a "kaputt" state, causing the user's job to fail and be re-queued.

## Solution
- The user's job will run once the priority increases, likely within the next few hours.
- No general issues with Emmy are known to the HPC Admins.

## General Learnings
- High group resource usage can lower the priority of individual jobs.
- Node failures can cause job delays and re-queuing.
- Regularly check job priority and group resource usage to anticipate delays.

## Related Users
- Two users (bccc39 and bccc000h) in the group have high resource usage.

## Next Steps
- Monitor job queue and priority.
- Investigate high resource usage within the group.
- Check for any node failures or issues.
---

### 2023060142003701_spr1tb%20mit%20SNC%3Doff.md
# Ticket 2023060142003701

 # HPC Support Ticket: spr1tb mit SNC=off

## Keywords
- SNC (Sub-NUMA Clustering)
- LIKWID
- Access Daemon
- SapphireRapids
- SLURM Reservation
- Health Check
- Kernel Version
- Performance Monitoring

## Summary
A user requested a specific node configuration (SNC=off) for performance monitoring. The ticket involves discussions about LIKWID versions, access daemon, and kernel issues on SapphireRapids processors.

## Problem
- User requested a node with SNC=off for performance monitoring.
- Issues with LIKWID and perf_event backend on SapphireRapids processors.

## Solution
- A node (f2257) was configured with SNC=off and reserved under SLURM with the reservation "nps1".
- LIKWID version with access daemon was discussed but not immediately installed due to compatibility issues with SapphireRapids.
- Health check exceptions were made for the node.
- The node was used for performance monitoring and later reverted to its original configuration after the user's work was completed.

## Lessons Learned
- Special node configurations require reservations to avoid conflicts with other users.
- LIKWID and perf_event backends may have compatibility issues with newer processors like SapphireRapids.
- Health check exceptions need to be managed for non-standard node configurations.
- Communication about resource usage and deadlines is crucial for efficient resource management.

## Actions Taken
- Node f2257 configured with SNC=off.
- SLURM reservation "nps1" created.
- Health check exception added for the node.
- Node reverted to original configuration after usage.

## Follow-up
- Update LIKWID to support SapphireRapids processors.
- Monitor performance issues related to kernel versions and perf_event backend.

## References
- [LIKWID](https://github.com/RRZE-HPC/likwid)
- [SLURM](https://slurm.schedmd.com/)
- [SapphireRapids](https://en.wikipedia.org/wiki/Sapphire_Rapids)
---

### 2024121142001949_Regarding%20multi%20threads%20in%20server.md
# Ticket 2024121142001949

 # HPC Support Ticket: Multi-threading Performance Issue

## Keywords
- Multi-threading
- Performance issue
- Python script
- Woody cluster
- SLURM
- `--cpus-per-task`

## Problem Description
- User experienced slower performance with multi-threading on the HPC cluster compared to single-threading.
- Multi-threading performed well on the user's personal device.

## Root Cause
- The user did not request multiple cores for the job, which is necessary for efficient multi-threading.

## Solution
- Request multiple cores by setting the `--cpus-per-task` parameter in the SLURM job script.

## Documentation References
- [OpenMP Job (Single Node)](https://doc.nhr.fau.de/clusters/woody/#openmp-job-single-node)
- [Job Script Examples (SLURM)](https://doc.nhr.fau.de/batch-processing/job-script-examples-slurm/)

## General Learnings
- Always ensure that the job script is configured to request the appropriate resources (e.g., multiple cores for multi-threading).
- Consult the documentation for examples and best practices when setting up job scripts.

## Roles Involved
- HPC Admins
- 2nd Level Support Team
---

### 2022092242002268_Tier3-Access-Fritz%20%22Markus%20Holzer%22%20_%20iwia015h.md
# Ticket 2022092242002268

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject: Tier3-Access-Fritz "Markus Holzer" / iwia015h

### Keywords:
- HPC Account Activation
- Certificate Expiration
- Resource Allocation
- Software Requirements
- Performance Benchmarks

### Summary:
- **HPC Admin**: Notified the user that their HPC account on Fritz has been activated.
- **User Request**:
  - **Contact**: User provided contact information.
  - **Resource Needs**:
    - Single-node throughput (72 cores, 250 GB)
    - Multi-node workload (HDR100 Infiniband with 1:4 blocking; per node: 72 cores, 250 GB)
  - **Compute Time**: 1000 node hours on Fritz
  - **Software Requirements**:
    - Latest clang, gcc, and intel compiler versions
    - Python 3.8 or newer
    - Latest Likwid version
    - MPI, OpenMP
  - **Application**: Performance benchmarks of the waLBerla framework and pystencils code generator.
  - **Expected Results**: Improvement of single-node performance and some scaling benchmarks.

### Root Cause of the Problem:
- Certificate expiration was mentioned, but it was resolved by activating the user's account.

### Solution:
- The HPC Admin activated the user's account on Fritz, resolving the certificate expiration issue.

### General Learnings:
- Ensure certificates are up-to-date for account activation.
- Verify resource allocation and software requirements before granting access.
- Communicate clearly with users about the status of their account and any issues that arise.
```
---

### 2024101742004608_Dask%20scheduler.md
# Ticket 2024101742004608

 ```markdown
# HPC Support Ticket: Dask Scheduler Issue

## Subject
User unable to correctly set up Dask workers for parallelizing a Python script on Alex GPUs.

## Keywords
Dask, Scheduler, Worker, GPU, SLURM, CPU Affinity, Python, CUDA, UCX

## Problem Description
User attempted to parallelize a Python script using Dask on Alex GPUs but encountered issues with setting up Dask workers. The job hangs without scheduling any worker.

## Root Cause
1. Incorrect IP address used for the Dask scheduler.
2. CPU affinity plugin causing issues due to mismatched CPU cores allocated by SLURM and those Dask is trying to pin to.

## Steps Taken
1. User provided a detailed description of the issue, including the SLURM script and error logs.
2. HPC Admin suggested using SLURM variables to get the correct IP address.
3. User tried running the scheduler as a background process and allocating a whole compute node to resolve CPU affinity issues.

## Solution
1. Start the Dask scheduler as a background process using `dask scheduler &`.
2. Allocate a whole compute node to ensure all CPUs and GPUs are available, resolving the CPU affinity issue.

## Lessons Learned
- Ensure the correct IP address is used for the Dask scheduler.
- CPU affinity issues can arise when SLURM allocates specific CPU cores. Allocating a whole compute node can resolve this.
- Running the scheduler as a background process prevents it from blocking.

## Conclusion
The issue was resolved by starting the scheduler as a background process and allocating a whole compute node. This approach ensures all CPUs and GPUs are available, resolving the CPU affinity issue.
```
---

### 2025021942003075_CPU%20frequency%20pinning%20not%20working.md
# Ticket 2025021942003075

 ```markdown
# HPC-Support Ticket: CPU Frequency Pinning Not Working

## Problem Description
- **Subject:** CPU frequency pinning not working
- **User Issue:** The user's program runs and completes normally, but Score-P tracing and Vampir show the program has run with a frequency of 2.4 GHz instead of the intended 2.0 GHz.
- **Command Used:** `srun --cpu-freq=2000000-2000000:performance -n 4 ./binary`

## Root Cause
- **Misinterpretation of CPU Frequency:** Score-P and Vampir might be showing the CPU base frequency (2.4 GHz) instead of the actual CPU frequency.
- **Default Timer Setting:** Score-P's default timer (`SCOREP_Timer`) uses the TSC counter, which increments at the base CPU frequency on x86 platforms.

## Solution
- **Measure Actual CPU Frequency:** Use Score-P's perf or PAPI measurement plugin to get the actual executed clock cycles.
  - **PAPI:** `export SCOREP_METRIC_PAPI=PAPI_TOT_CYC`
  - **Perf:** `export SCOREP_METRIC_PERF=cpu-cycles`
- **Compare CPU Cycles:** Use `export SCOREP_METRIC_PERF=cpu-cycles,ref-cycles` to compare actual CPU cycles (`cpu-cycles`) with cycles at base frequency (`ref-cycles`). If they are the same, the program runs at base frequency.

## Keywords
- CPU frequency pinning
- Score-P
- Vampir
- TSC counter
- PAPI
- Perf
- Base frequency
- Actual frequency

## General Learnings
- **CPU Frequency Measurement:** Ensure that the tools used for measuring CPU frequency are correctly configured to measure the actual frequency rather than the base frequency.
- **Score-P Configuration:** Adjust Score-P settings to measure relevant events and derive the actual CPU frequency.
- **Troubleshooting:** Verify environment variable settings and use appropriate measurement plugins to diagnose and resolve frequency-related issues.
```
---

### 2023100942000254_Dummyaccount%20%2B%20Reservierung%20f0401%20f%C3%83%C2%BCr%20CLPE%20Tutorial%20am%2012.10..md
# Ticket 2023100942000254

 ```markdown
# HPC Support Ticket: Dummy Account and Node Reservation for CLPE Tutorial

## Keywords
- Dummy account
- Node reservation
- CLPE Tutorial
- HPC Admin
- Reservation details

## Summary
A user requested the creation of a dummy account and the reservation of a specific node (f0401) for a CLPE Tutorial.

## User Request
- **Request:** Creation of a dummy account and reservation of node f0401 for the CLPE Tutorial on October 12.
- **Duration:** October 11-12.

## HPC Admin Response
- **Account Creation:** The dummy account will be available by the next morning.
- **Reservation Details:**
  - **Reservation Name:** CLPE-Tutorial
  - **Start Time:** 2023-10-11T08:00:00
  - **End Time:** 2023-10-12T20:00:00
  - **Duration:** 1 day 12 hours
  - **Nodes:** f0401
  - **Node Count:** 1
  - **Core Count:** 72
  - **Flags:** IGNORE_JOBS, SPEC_NODES, MAGNETIC
  - **TRES:** cpu=72
  - **State:** INACTIVE

## Lessons Learned
- **Account Creation:** HPC Admins can create dummy accounts for specific purposes such as tutorials.
- **Node Reservation:** Specific nodes can be reserved for a specified duration and purpose.
- **Reservation Details:** Important details include reservation name, start and end times, nodes, core count, and flags.

## Solution
- **Account Creation:** The dummy account was created and will be available by the next morning.
- **Node Reservation:** The reservation details were provided, and the reservation will be updated once the account is known on the system.
```
---

### 2019030742000878_bad%20performance%20of%20Flow3D%20jobs%20on%20Emmy%20_%20iwst024h.md
# Ticket 2019030742000878

 # HPC Support Ticket: Bad Performance of Flow3D Jobs on Emmy

## Keywords
- Load imbalance
- Flow3D
- Emmy
- Single node jobs
- Domain decomposition
- Woody
- SSH client

## Summary
The user's Flow3D jobs on Emmy showed severe load imbalance with one node doing most of the work while the second node did almost nothing. The user was initially under the impression that Emmy required more than one node for jobs.

## Root Cause
- The load imbalance was due to the domain decomposition and input configuration of the jobs.
- The user's SSH client was outdated, causing issues with accessing Woody.

## Solution
- The HPC Admin suggested running the jobs on a single node, as the main memory requirements were not too high.
- The user was advised to try using modern SSH clients like Putty or MobaXterm to access Woody.
- The user changed the configuration of the domain and blocked parts of the domain that were not necessary for calculation.

## Outcome
- The single node jobs on Emmy showed promising results, with performance close to the previous two-node jobs.
- The user was able to access Woody using a modern SSH client.

## General Learnings
- Always check domain decomposition and input configuration for load imbalance issues.
- Single node jobs are possible on Emmy and can be more efficient for certain jobs.
- Keep SSH clients up to date to avoid access issues.
- Woody can be an interesting option for jobs with lower main memory requirements, as it has fewer cores but a higher clock frequency.
---

### 2024112142001306_Alternative%20to%20Alex%20cluster%20for%20CPU%20intensive%20jobs.md
# Ticket 2024112142001306

 ```markdown
# HPC-Support Ticket Conversation: Alternative to Alex Cluster for CPU Intensive Jobs

## Keywords
- CPU intensive jobs
- Alex cluster
- Fritz cluster
- BayernKI
- Project v114be
- NHR@FAU

## Problem
- **User**: PhD student at UTN with access to the Alex cluster.
- **Issue**: Needs a cluster for CPU intensive jobs that do not require a GPU.

## Solution
- **HPC Admin**: Enabled project v114be on the parallel computer Fritz.
- **Details**: Fritz cluster is suitable for CPU intensive jobs and provides +5 million core-hours as part of BayernKI.

## General Learnings
- **Cluster Options**: Fritz cluster is an alternative for CPU intensive jobs.
- **Project Enablement**: Projects can be enabled on different clusters based on user needs.
- **Resource Allocation**: Fritz cluster offers significant core-hours for BayernKI projects.

## References
- [Fritz Cluster Documentation](https://doc.nhr.fau.de/clusters/fritz/)
- [NHR@FAU](https://hpc.fau.de/)
```
---

### 2023041142000949_Some%20weird%20job%20crashes.md
# Ticket 2023041142000949

 # HPC-Support Ticket: Some Weird Job Crashes

## Keywords
- Job crashes
- OOM (Out-of-Memory)
- File access errors
- Slurm
- GPU jobs
- Swap space
- Chained jobs

## Problem Description
The user experienced intermittent job crashes on the HPC system. The jobs were chained and ran well for many epochs before crashing. The crashes were characterized by OOM events and file access errors.

## Root Cause
1. **OOM Events**:
   - The jobs were allocated 45.5 GB of memory per GPU on the `rtx3080` partition.
   - There was an 8 GB shared swap space on the node, but jobs should not use swap space.
   - Historic data showed that the memory requirements of the jobs varied over time, suggesting that the jobs might have exceeded the available memory at some point.

2. **File Access Errors**:
   - The errors were related to accessing files in the `/scratch` directory.
   - The errors were reported as "System error" rather than "File not found," which is unusual.
   - The jobs took 2-3 minutes longer to stop than other jobs, suggesting that something might have gotten stuck or taken longer.

## Speculations and Suggestions
- **OOM Events**:
  - The user might have been lucky in previous jobs to get hold of the additional 8 GB from swap space.
  - The user should monitor the memory usage of their jobs more closely to ensure they do not exceed the allocated memory.

- **File Access Errors**:
  - Other users should not be able to access files inside a job under `/scratch` as each user gets their own `/scratch` via namespaces.
  - The errors might be due to a race condition between the cleanup script and the already started chain job.
  - The user should check their cleanup script and the timing of their chain jobs to avoid potential race conditions.

## Solution
- The user should monitor the memory usage of their jobs to prevent OOM events.
- The user should check their cleanup script and the timing of their chain jobs to avoid file access errors.
- If the issues persist, the user should notify the HPC support team for further investigation.

## Closure
The ticket was closed after the HPC admin provided suggestions and the user acknowledged them. The admin also noted that jobs should never use swap space.
---

### 2024070242003983_Fehler%20bei%20Einrichtung%20von%20Multi-Node-Projekt.md
# Ticket 2024070242003983

 # HPC Support Ticket: Fehler bei Einrichtung von Multi-Node-Projekt

## Keywords
- Multi-Node Job
- QoS (Quality of Service)
- SLURM
- Invalid qos specification
- Node count specification invalid
- User-specific QoS activation

## Problem
- User received "Invalid qos specification" error when setting `--qos=a100multi` in their `train.sh` script.
- Without the `--qos` tag, the error "Node count specification invalid" occurred when setting `--node >1`.

## Root Cause
- The QoS `a100multi` needs to be activated on a per-user basis, not project-wide.

## Solution
- HPC Admins activated the `--qos=a100multi` for the specific user accounts (b185cb13 and b185cb10).

## General Learning
- QoS settings may need to be activated individually for each user account, even within the same project.
- Ensure that the documentation is followed correctly regarding QoS activation.
- Multi-node jobs require proper QoS settings to avoid node count specification errors.

## Follow-up
- Users should verify that their scripts work after the QoS activation.
- If similar issues arise, check if the QoS has been activated for the specific user account.

## Relevant Documentation
- [Multi-Node Job Documentation](https://doc.nhr.fau.de/clusters/alex/?h=node#multi-node-job-available-on-demand-for-nhr-projects)
---

### 2023101942000781_Tier3-Access-Fritz%20%22Siavash%20Toosi%22%20_%20iwst088h.md
# Ticket 2023101942000781

 # HPC Support Ticket Conversation Analysis

## Keywords
- Tier3 Access
- Fritz
- Core-hours
- NHR Compute Time Proposal
- Multi-node Workload
- HDR100 Infiniband
- High Fidelity CFD Simulations
- Nek5000, Neko, Hybrid
- VisIt, MATLAB
- sreport

## Summary
- **User Request:** Access to Fritz for high fidelity CFD simulations requiring 13,500 node hours.
- **HPC Admin Response:** Account enabled, but core-hours not guaranteed from free Tier3 service. NHR compute time proposal required for guaranteed resources.
- **User Follow-up:** Inquiry about approved core-hours and how to check allocated/remaining core-hours.
- **HPC Admin Clarification:** 972k core-hours approved, but usage not guaranteed. Instructions provided to check usage with `sreport`.

## Root Cause of the Problem
- User uncertainty about approved core-hours and how to check usage.

## Solution
- HPC Admin clarified the approved core-hours and provided a command (`sreport user topusage -t hours start=2023-01-01 end=2023-10-20`) to check usage.

## General Learnings
- **Resource Allocation:** Understanding the difference between requested, approved, and guaranteed core-hours.
- **Usage Tracking:** Using `sreport` to monitor core-hour usage.
- **NHR Proposal:** Importance of submitting an NHR compute time proposal for guaranteed resources.

## Documentation for Support Employees
- **Checking Core-Hour Usage:** Use the command `sreport user topusage -t hours start=YYYY-MM-DD end=YYYY-MM-DD` on any Fritz frontend to monitor usage.
- **Resource Guarantee:** Inform users that free Tier3 service does not guarantee all requested core-hours. An NHR compute time proposal is required for guaranteed resources.
---

### 2018103042000143_Idle%20Jobs%20auf%20Emmy%20Cluster.md
# Ticket 2018103042000143

 # HPC-Support Ticket: Idle Jobs auf Emmy Cluster

## Summary
- **Issue**: Multiple jobs on the Emmy cluster appeared idle in the system monitoring.
- **Root Cause**: Inefficient code structure and resource utilization.
- **Solution**: Code optimization and better resource management.

## Detailed Information

### Initial Report
- **HPC Admin**: Noted that 12 jobs on the Emmy cluster were idle for extended periods.
- **User**: Confirmed that the jobs were running but appeared idle due to the nature of the tasks (building large optimization models).

### Investigation
- **HPC Admin**: Provided system monitoring data showing minimal resource utilization (CPU, memory, network).
- **User**: Described the code structure, which involved using Dask for parallelization and Gurobi for optimization.

### Code Structure
- **User**: Explained that each Dask worker builds a part of the optimization model and then solves it. Gurobi uses 4 threads, but only one thread is active during model building.

### Optimization Efforts
- **User**: Identified and fixed inefficiencies in the code, reducing the idle time significantly.
- **HPC Admin**: Provided feedback and suggested further improvements.

### Monitoring Tools
- **HPC Admin**: Offered access to a beta job monitoring tool for better job tracking.
- **User**: Provided feedback on the monitoring tool and requested access for a colleague.

### Final Optimization
- **User**: Further optimized the code, reducing the job runtime to under 2 minutes.
- **HPC Admin**: Acknowledged the improvements and suggested potential funding opportunities for further code optimization.

## Lessons Learned
- **Resource Utilization**: Ensure efficient use of HPC resources by optimizing code and monitoring resource usage.
- **Collaboration**: Close collaboration between users and HPC admins can lead to significant performance improvements.
- **Monitoring Tools**: Utilize available monitoring tools to identify and address performance bottlenecks.

## Keywords
- Idle Jobs
- Resource Utilization
- Code Optimization
- System Monitoring
- Dask
- Gurobi
- Job Monitoring
- Performance Improvement

## References
- [KONWIHR Software Initiative](https://blogs.fau.de/konwihr/files/2018/06/Flyer_Softwareinitiative_Konwihr-2018.pdf)
- [KONWIHR Multicore Software Initiative](https://blogs.fau.de/konwihr/2012/01/26/konwihr-iii-neuauflage-der-konwihr-multicore-software-initiative/)
- [KONWIHR Multicore Software Initiative (2009)](https://blogs.fau.de/konwihr/2009/08/26/konwihr-multicore-software-initiative/)
---

### 2018121842001153_low%20resource%20utilization%20of%20jobs%20on%20Emmy%20_%20iwst039h.md
# Ticket 2018121842001153

 ```markdown
# HPC Support Ticket: Low Resource Utilization of Jobs

## Keywords
- Low resource utilization
- STAR-CCM+
- MPI processes
- Simulation domains
- Compute nodes

## Problem Description
- User's jobs start 40 STAR-CCM+ processes per node but show low resource utilization.
- Load is only 6, 8, 10, or 16 instead of the expected 40.
- Indication that too many compute nodes were requested for the simulation domains.

## Root Cause
- STAR-CCM+ utilizes 1 processor for 50,000 mesh cell counts.
- User requested more compute nodes than necessary for the simulation domains.

## Solution
- User deleted the jobs and resubmitted them based on the utilization graph provided by the HPC Admin.
- User will keep the utilization in mind for future simulations.

## Lessons Learned
- Ensure proper resource allocation based on the simulation requirements.
- Monitor resource utilization to optimize job submissions.
- Utilize utilization graphs to adjust the number of compute nodes.
```
---

### 2024020442000508_Minutenlanger%20cshpc-Overload%20%3F%20-%20Memory-Limits%20f%C3%83%C2%BCr%20iwnt115%20aktiviert.md
# Ticket 2024020442000508

 ```markdown
# HPC Support Ticket: Minutenlanger cshpc-Overload

## Keywords
- cshpc Overload
- Memory Limits
- Python Process
- User iwnt115h
- /etc/security/limits.conf
- NoMachine
- SSH Login

## Problem Description
- The cshpc system was unresponsive for several minutes.
- SSH login and NoMachine interface were frozen.
- A Python process run by user iwnt115h was consuming excessive CPU (300%) and memory (>40 GB).

## Root Cause
- Excessive resource consumption by a Python process run by user iwnt115h.

## Solution
- HPC Admins identified two processes by user iwnt115h each consuming nearly 50 GB of memory.
- Memory limits were set in `/etc/security/limits.conf` for user iwnt115h:
  ```
  iwnt115h        hard    rss     1000000
  iwnt115h        hard    as      1500000
  ```
- All processes of user iwnt115h were terminated to enforce the new limits upon next login.

## General Learnings
- Excessive resource consumption by a single user can cause system-wide performance issues.
- Setting memory limits in `/etc/security/limits.conf` can prevent such issues.
- Users should be encouraged to use alternative systems (e.g., csnhr) for better resource management.
```
---

### 2019120942001651_Jobs%20mit%20sander.MPI.md
# Ticket 2019120942001651

 ```markdown
# HPC Support Ticket: Jobs with sander.MPI

## Keywords
- sander.MPI
- pmemd.MPI
- Job Monitoring
- Queue
- Performance Optimization

## Summary
- **User Issue**: User is running jobs with `sander.MPI`, which is slower compared to `pmemd.MPI`.
- **HPC Admin Suggestion**: Switch to `pmemd.MPI` for potentially faster job execution.
- **User Response**: User is bound to `sander.MPI` due to specific functionalities not supported by the pre-compiled versions.

## Root Cause
- User requires specific functionalities in `sander.MPI` that are not available in the pre-compiled versions provided by the HPC site.

## Solution
- No immediate solution provided as the user is bound to `sander.MPI` for specific functionalities.

## Lessons Learned
- Always consider the specific requirements of the user's jobs when suggesting performance optimizations.
- Ensure that pre-compiled software versions support all necessary functionalities to avoid users having to compile their own versions.

## Follow-up Actions
- Document the specific functionalities required by the user for future reference.
- Investigate the possibility of providing pre-compiled versions of `sander.MPI` with the required functionalities.
```
---

### 2024082842001596_Reservierung%20auf%20fritz%20f%C3%83%C2%BCr%20ihpc119h.md
# Ticket 2024082842001596

 ```markdown
# HPC Support Ticket: Reservation Request for Fritz Nodes

## Keywords
- Reservation
- Fritz Nodes
- Slurm
- Overlapping Reservation
- Explicit Reservation Request

## Summary
A user requested a reservation of 5 Fritz nodes for specific dates and times. The HPC Admin created the reservations but encountered an error due to overlapping reservations.

## Problem
- **Root Cause**: Overlapping reservation error when trying to create a reservation for the same nodes at the same time.

## Solution
- **Steps Taken**:
  - The HPC Admin used the `scontrol create reservation` command to create reservations for the specified dates and times.
  - An error occurred due to an overlapping reservation for the same nodes.
  - The HPC Admin corrected the date and successfully created the reservations.

- **Additional Information**:
  - Reservations were created without the "magnetic" option, meaning they must be explicitly requested using `--reservation=bench-AA-BB` to ensure the specific nodes are used.

## Lessons Learned
- Always check for overlapping reservations before creating new ones.
- Ensure users are aware of how to explicitly request reserved nodes to avoid confusion.

## Commands Used
```bash
scontrol create reservation reservationname=bench-08-30 starttime=2024-08-30T13:00 endtime=2024-08-30T18:00 user=ihpc119h nodes=f04[01-05]
scontrol create reservation reservationname=bench-09-02 starttime=2024-09-02T13:00 endtime=2024-09-02T18:00 user=ihpc119h nodes=f04[01-05]
scontrol create reservation reservationname=bench-09-03 starttime=2024-09-03T13:00 endtime=2024-09-03T18:00 user=ihpc119h nodes=f04[01-05]
```

## Conclusion
Ensure that reservations do not overlap and inform users about the necessity of explicitly requesting reserved nodes.
```
---

### 2024061442001197_SLRUM%20job%20submission%20pending.md
# Ticket 2024061442001197

 ```markdown
# SLRUM Job Submission Pending

## Keywords
- SLRUM job submission
- Pending jobs
- Idle nodes
- Priority state
- Fairshare

## Problem Description
- User experienced job submissions pending despite idle nodes.
- Issue occurred on both Tinyx and Alex clusters.
- User's colleague had immediate job allocation while user's job remained in Priority state.

## Root Cause
- The batch system assigns priority to each waiting job based on parameters like waiting time, partition, user group, and recently used CPU/GPU time (fairshare).
- User's recent job submissions and high compute time usage led to a decrease in priority.

## Solution
- Understand that job priority is influenced by fairshare and other factors.
- Reduce job submissions or wait for fairshare to reset to improve priority.

## General Learning
- Job priority in SLRUM is dynamic and depends on various factors.
- High recent compute usage can lower priority, affecting job scheduling.
- Fairshare ensures equitable resource distribution among users.
```
---

### 2020040142003283_Job%20auf%20Emmy%201288296%20mpt1009h.md
# Ticket 2020040142003283

 # HPC Support Ticket Analysis: Job Load Imbalance

## Keywords
- Load Imbalance
- Job Script
- Independent Computations
- Node Utilization
- Script Adjustment

## Problem
- **Root Cause**: The user's job script on Emmy (1288296) exhibited significant load imbalance. Multiple independent computations were started within a single job script, with varying runtimes.
- **Impact**: Out of 30 requested nodes, only 6 were active after 16 hours, with 108 out of 240 possible processes running.

## Solution
- **Admin Recommendation**: Ensure that individual runs have similar runtimes or submit separate jobs to avoid unnecessary node blocking.
- **User Action**: The user aborted the script and will attempt to better distribute processes across nodes in future jobs.

## General Learnings
- **Load Balancing**: Ensure that jobs are balanced to avoid underutilization of resources.
- **Script Optimization**: Adjust job scripts to distribute workloads evenly across nodes.
- **Separate Submissions**: Consider submitting independent computations as separate jobs to optimize resource usage.

## Next Steps for Support
- Monitor job scripts for load imbalance.
- Provide guidelines for optimizing job scripts to users.
- Ensure users are aware of the importance of balanced workloads for efficient resource utilization.
---

### 2025011742001304_Request%20for%20Higher%20Job%20Priority%20on%20the%20GPU%20Cluster%20-%20v103fe18%20_%20v103fe11.md
# Ticket 2025011742001304

 # HPC Support Ticket: Request for Higher Job Priority on the GPU Cluster

## Keywords
- Job Priority
- GPU Cluster
- Conference Deadline
- Hyperparameter Tuning
- Job ID

## Summary
A user requested higher priority for jobs on the "Alex" GPU cluster due to an upcoming conference deadline. The jobs were time-intensive hyperparameter tuning tasks.

## Root Cause
- Delays in job processing due to time-intensive tasks.
- Upcoming conference deadline requiring faster job completion.

## Solution
- **HPC Admin** requested the job IDs that needed prioritization.
- User provided the job ID (2302449) that was stuck.
- **HPC Admin** pushed several additional jobs over the weekend to expedite the process.

## Outcome
- The jobs were processed quickly over the weekend.
- User expressed gratitude for the extra effort.

## General Learnings
- Users facing critical deadlines can request higher job priority.
- Providing specific job IDs helps **HPC Admins** prioritize tasks effectively.
- **HPC Admins** can push jobs during off-peak hours to meet user deadlines.

## Actions Taken
1. User requested higher job priority.
2. **HPC Admin** requested specific job IDs.
3. User provided the job ID.
4. **HPC Admin** prioritized and pushed the jobs over the weekend.
5. User confirmed the jobs were processed quickly.

## Conclusion
Effective communication and timely intervention by **HPC Admins** can help users meet critical deadlines by prioritizing their jobs on the GPU cluster.
---

### 2022042242001643_WOODY%20gets%20very%20slow.md
# Ticket 2022042242001643

 ```markdown
# HPC Support Ticket: WOODY Login Nodes Slowdown

## Keywords
- WOODY login nodes
- Slow performance
- Shared resources
- Memory consumption
- ECAP frontends

## Problem Description
- User reports frequent slowdowns on WOODY login nodes, affecting basic commands like `ls`, `cd`, and `pwd`.
- Issue started occurring after initial smooth operation.
- Multiple users experiencing the same problem.

## Root Cause
- One user running a memory-intensive program on a shared login node (woody3), causing extreme slowdowns.

## Solution
- HPC Admins killed the offending processes, resolving the issue temporarily.
- User advised to use ECAP-specific frontends (woodycap) instead of general WOODY login nodes.

## Additional Information
- User was not aware of ECAP-specific frontends and will start using them.
- Suggestion to implement automatic killing of processes that misuse shared resources.
- User encouraged to report future slowdowns through the same channel.

## Action Items
- Educate users about proper usage of shared resources.
- Consider implementing automatic monitoring and termination of resource-intensive processes on login nodes.
- Ensure documentation clearly highlights the availability of ECAP-specific frontends.
```
---

### 2020011642002511_roofline%20plot.md
# Ticket 2020011642002511

 # Roofline Plot Generation for HPC Performance Estimation

## Keywords
- Roofline plot
- HPC performance
- Job credentials
- Raw data
- Flops
- Memory bandwidth (MemBW)
- Intensity

## Problem
- User wants to generate roofline plots to estimate HPC performance.
- User inquires about generating roofline plots for individual users.

## Solution
- Users can enter job credentials on the HPC status page to access a link to the job's roofline diagram.
- The roofline diagram plots a dot for each node and every minute of runtime, with colors indicating time elapsed since the job started.
- Users can download raw data as a ZIP file if they prefer to create their own plots.
- Flops are calculated using 2*DP+SP from the second column in `_spmflops.dat` and `_dpmflops.dat`.
- Intensity is calculated from flops and recorded memory bandwidth (MemBW).

## Additional Notes
- Rendering the plot on the client side may consume significant browser resources for large or long-running jobs.
- A view of the average of all jobs for a user is not currently available due to authorization issues.
- No past jobs were found for the user, so manual data could not be sent.

## Conclusion
- Users can generate their own roofline plots by following the provided instructions and using the raw data for custom plotting if needed.
- The calculation of flops and intensity is crucial for accurate roofline plot generation.
---

### 2020112442001488_Knotenauslastung%20auf%20emmy%20%7C%20iwst058h.md
# Ticket 2020112442001488

 ```markdown
# HPC Support Ticket: Node Utilization on Emmy

## Keywords
- Node utilization
- mpirun
- Job configuration
- Physical CPUs
- Simulation
- Emmy

## Problem
The user's simulations on Emmy were only utilizing half of the requested nodes.

## Root Cause
The mpirun command was not configured to distribute processes evenly across the nodes and to use only the physical CPUs.

## Solution
To distribute 80 processes evenly across 4 nodes and use only the physical CPUs, the mpirun command should be modified as follows:
```bash
mpirun -n 80 -npernode 20 fireFoam -parallel
```

## General Learnings
- Ensure that the mpirun command is correctly configured to distribute processes evenly across nodes.
- Verify that the command is set to use only the physical CPUs to optimize resource utilization.
- Proper configuration of job scripts is crucial for efficient use of HPC resources.
```
---

### 2025021842004003_1-day%20jobs%20in%20the%20queue%20despite%20gpus%20are%20free.md
# Ticket 2025021842004003

 # HPC Support Ticket: 1-Day Jobs in Queue Despite Idle GPUs

## Keywords
- Job queue
- Idle GPUs
- Priority assignment
- Fairshare
- A100 partition

## Problem Description
- User submitted 3 jobs in the A100 partition with a time limit of 1 day.
- Jobs are still waiting in the queue despite 4 nodes being idle.

## Root Cause
- The batch system assigns priority to jobs based on various parameters such as waiting time, partition, user group, and recently used CPU/GPU time (fairshare).
- High demand for A100 GPUs with 160 jobs currently waiting in the queue.

## Solution/Explanation
- The delay in job processing is due to the high demand and the priority assignment mechanism of the batch system.
- Users should be aware that even if GPUs are idle, jobs may still queue due to the fairshare policy and the number of waiting jobs.

## General Learning
- Understanding the job priority assignment mechanism is crucial for users to manage their expectations regarding job processing times.
- High demand for resources can lead to queuing even when resources appear to be idle.
- Fairshare policies ensure equitable distribution of resources among users.

## Next Steps for Support
- Inform users about the current demand and the priority system.
- Encourage users to plan their jobs accordingly and consider requesting resources well in advance.

---

This documentation aims to help support employees understand and address similar issues related to job queuing and resource allocation in the HPC environment.
---

### 2020020442002237_Yambo%20Job%20auf%20Emmy%20%281234611%2C%20mpp3000h%29.md
# Ticket 2020020442002237

 # HPC Support Ticket Analysis

## Subject: Yambo Job auf Emmy (1234611, mpp3000h)

### Keywords:
- Yambo Job
- Emmy
- OMP_NUM_THREADS
- OMP_PROC_BIND
- OMP_PLACES
- mpirun
- ppn
- cores
- threads

### Root Cause:
- User set `OMP_PLACES=threads` together with `-ppn 10`, which resulted in using only half of the physical cores.

### Solution:
- Recommended to set `OMP_PLACES=cores` to utilize all physical cores effectively.

### Lessons Learned:
- Ensure proper configuration of OpenMP environment variables to optimize resource utilization.
- Setting `OMP_PLACES=cores` is more efficient than `OMP_PLACES=threads` when using `-ppn 10`.

### Ticket Status:
- Closed due to no response from the user.

### Involved Parties:
- HPC Admins
- 2nd Level Support Team

### Additional Notes:
- The ticket was closed due to lack of user response.
- Proper configuration of OpenMP variables is crucial for efficient resource usage in HPC environments.

---

This analysis can be used to troubleshoot similar issues related to OpenMP and MPI job configurations on HPC systems.
---

### 2024090442002646_Tier3-Access-Fritz%20%22Leon%20Sch%C3%83%C2%B6ps%22%20_%20iwst108h.md
# Ticket 2024090442002646

 ```markdown
# HPC Support Ticket Conversation Analysis

## Subject
Tier3-Access-Fritz "Leon Schöps" / iwst108h

## Keywords
- HPC Account Activation
- Fritz Access
- Multi-node Workload
- HDR100 Infiniband
- Simcenter Star-CCM+
- OpenFOAM
- CFD Simulation
- Acoustic Flow Optimization

## Summary
- **User Request**: Access to HPC resources on Fritz for multi-node workload.
- **Requirements**:
  - Multi-node workload with HDR100 Infiniband (1:4 blocking).
  - Per node: 72 cores, 250 GB.
  - Required software: Simcenter Star-CCM+, OpenFOAM.
  - Application: Unsteady, compressible CFD-Simulation for acoustic flow optimization.
  - Expected results: Optimized geometries for pneumatic robotics ejectors.
  - Requested compute time: 90,000 node hours.

## HPC Admin Response
- **Action**: HPC account iwst108h activated on Fritz.
- **Admin**: Thomas Zeiser

## Lessons Learned
- **Process**:
  - Users request access to specific HPC resources.
  - HPC Admins activate the account and notify the user.
- **Common Requirements**:
  - Multi-node workloads with specific hardware and software needs.
  - Detailed application descriptions help in resource allocation.

## Root Cause of the Problem
- User needed access to HPC resources for a specific project.

## Solution
- HPC Admin activated the user's account and granted access to the required resources.
```
---

### 2024082742001811_k103bf.md
# Ticket 2024082742001811

 ```markdown
# HPC Support Ticket Analysis: k103bf

## Keywords
- GPU multinode partition
- Admin rights
- User permissions
- Project management
- Quality of Service (QoS)

## Summary
- **User Request:**
  - Allow user `k103bf19` to use the GPU multinode partition.
  - Grant admin rights to users `k103bf12` and `k103bf13`.
  - User is leaving the project.

- **HPC Admin Response:**
  - Activated `--qos=a100_multi` for `k103bf19`.
  - Added `k103bf12` as Manager.
  - Noted that `k103bf13` already had management rights as the PI of the project.

## Root Cause
- User needed specific permissions and admin rights for project continuity.

## Solution
- HPC Admins granted the necessary permissions and confirmed existing rights.

## General Learnings
- Users can request specific permissions and admin rights for project continuity.
- HPC Admins can activate Quality of Service (QoS) for specific users.
- Existing admin rights should be checked before granting new permissions.
```
---

### 2020062542001021_Currently%20running%20job%20on%20Emmy%20%28named%20%22hoomdTemp%22%29.md
# Ticket 2020062542001021

 # HPC Support Ticket: Currently Running Job on Emmy (named "hoomdTemp")

## Keywords
- Emmy cluster
- Job named "hoomdTemp"
- Single node usage
- Parallel system
- Woody cluster
- TinyFat cluster
- SSH onto nodes
- Double precision calculation
- Memory usage
- Ethernet traffic

## Summary
A user's job on the Emmy cluster was not utilizing all requested nodes efficiently. Only one node was performing double precision calculations, while all nodes showed memory usage and ethernet traffic.

## Root Cause
- Inefficient use of parallel resources.
- Possible serial usage on a parallel system.

## Solution
- **Check Job Output**: The user was advised to SSH onto the Emmy nodes to check if the job was running and producing output as intended.
- **Resource Allocation**: If the job was running fine but only using one node for calculations, the user was advised to run single node jobs on the Woody cluster. If Woody nodes do not have enough memory, the TinyFat cluster was suggested as an alternative.

## General Learnings
- Always monitor job performance to ensure efficient use of allocated resources.
- Use appropriate clusters for different job types (serial vs. parallel).
- SSH can be used to check job status on nodes.
- Consider memory requirements when choosing a cluster for job submission.

## Related Links
- [Woody Cluster Documentation](https://www.anleitungen.rrze.fau.de/hpc/woody-cluster/)
- [TinyFat Cluster Documentation](https://www.anleitungen.rrze.fau.de/hpc/tinyx-clusters/#tinyfat)
- [HPC Services at FAU](http://www.hpc.rrze.fau.de/)
---

### 2018080342001386_Neueste%20LIKWID-Version%20als%20Default%20auf%20Emmy.md
# Ticket 2018080342001386

 # HPC Support Ticket: Update LIKWID Default Version on Emmy

## Keywords
- LIKWID
- Default version
- Emmy
- Skip-Mask problem
- Downtime
- System monitoring
- MOTD message
- OpenMP pinning

## Summary
The user requested an update of the default LIKWID module on Emmy from version 4.1.2 to 4.3.2 to address issues related to the Skip-Mask problem. The HPC Admins agreed to perform the update during the next scheduled downtime.

## Root Cause
- The default LIKWID version (4.1.2) on Emmy was causing issues, particularly with the Skip-Mask problem.

## Solution
- The default LIKWID version was updated to 4.3.3 during a scheduled downtime.
- The system monitoring continues to use version 4.1.2.
- An MOTD message was added to inform users about the update without detailing specific changes.

## Timeline
1. User requested the update due to Skip-Mask issues.
2. HPC Admins agreed to update during the next downtime.
3. The update was planned for the downtime on 17.09 but was postponed.
4. The update was announced at the HPC Benutzerkolloqium.
5. LIKWID 4.3.3 was installed and set as the new default.

## Notes
- The update was intended to resolve issues with pin and perfctr.
- Normal users should not notice any changes, even with OpenMP pinning.

## Conclusion
The default LIKWID version on Emmy was successfully updated to 4.3.3, addressing user concerns about the Skip-Mask problem. The system monitoring remains on version 4.1.2, and users were informed via an MOTD message.
---

### 2022110742003951_Poor%20resource%20utiliation%20of%20jobs%20on%20Woody%20-%20gwpa005h.md
# Ticket 2022110742003951

 # HPC Support Ticket: Poor Resource Utilization on Woody

## Keywords
- Resource utilization
- Slurm batch system
- Job script optimization
- Single-core jobs
- Load balancing

## Problem Description
- Users' jobs on Woody request 4 cores but utilize only a single core most of the time.
- Tasks within jobs take different times to complete, leading to poor resource utilization.

## Root Cause
- Combining multiple tasks into a single job with each task requesting a single core.
- Inefficient job script setup leading to load balancing issues.

## Solution
- Submit individual jobs for each task, requesting a single core per job.
- Use Slurm directives: `#SBATCH --ntasks=1` and `#SBATCH --cpus-per-task=1`.

## Lessons Learned
- With Slurm, single-core jobs are handled efficiently and should be preferred over combining tasks into a single job.
- Proper job script setup is crucial for optimal resource utilization.
- Monitoring job performance and adjusting scripts accordingly can improve overall system efficiency.

## Follow-up Actions
- Users agreed to change their job setup once current jobs are completed.
- HPC Admins to monitor job performance and provide further assistance if needed.
---

### 2018052242001275_OpenMP%20Frage.md
# Ticket 2018052242001275

 # HPC Support Ticket: OpenMP Vectorization Issue

## Keywords
- OpenMP
- Vectorization
- Reduction Clause
- Intel Compiler (ifort)
- Performance Optimization

## Problem Description
The user encountered issues with vectorizing a nested loop within a parallel region using OpenMP. The goal was to ensure the inner loop (`jv` loop) is vectorized by the Intel compiler (ifort). The user tried different compiler options and directives (`vec-threshold0`, `!$DIR vector always`, `omp simd`) but was unsure about the correctness and performance implications.

## Root Cause
- The user wanted to ensure the compiler vectorizes the inner loop without checking for data dependencies.
- There was confusion about the behavior of different vectorization directives and their impact on performance.

## Solution
- The `omp simd reduction (+:fdd)` directive was used to inform the compiler about the reduction operation, ensuring correct vectorization.
- The user eventually rewrote the code to use matrix-matrix multiplication (DGEMM), which significantly improved performance (36x faster).

## Lessons Learned
- Using the `omp simd reduction` directive can help the compiler understand reduction operations and improve vectorization.
- Rewriting code to use optimized library functions like DGEMM can lead to significant performance improvements.
- Compiler behavior can be unpredictable, and different directives may yield different results.

## Additional Notes
- The user also mentioned using Fortran Contiguous Pointers without any negative performance impact.
- The final solution did not scale well but was acceptable given the significant performance improvement.

## Conclusion
The issue was resolved by using the appropriate OpenMP directive and rewriting the code to leverage optimized library functions. This approach led to substantial performance gains.
---

### 2024072442002184_Assistance%20with%20Your%20BayernKI%20Project%20and%20NHR%20Resources%20-%20v108be.md
# Ticket 2024072442002184

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject: Assistance with Your BayernKI Project and NHR Resources - v108be

### Keywords:
- BayernKI Project
- NHR Resources
- Training Data
- Virtualenv
- Apptainer
- Workspaces
- Fritz CPU Cluster

### General Learnings:
- **Resource Utilization**: Regular usage of allocated compute resources is beneficial to ensure maximum utilization.
- **Data Management**: Copying training data to the local `$TMPDIR` on the node at the beginning of the job can speed up the process.
- **Environment Setup**: Using `venvs` or `conda envs` is recommended for setting up the training environment. Apptainer is a good choice if frameworks are hard to install.
- **Workspaces**: Storing models and source training data on workspaces can simplify the workflow and speed up jobs.
- **Resource Reallocation**: It is possible to reallocate resources to access different clusters (e.g., Fritz CPU cluster) based on project needs.

### Root Cause of the Problem:
- The project had not started using the allocated compute resources due to the time spent on dataset preparation.
- The project required CPU-bound data generation, which necessitated access to the Fritz CPU cluster.

### Solution:
- **Data Management**: Recommended copying training data to the local `$TMPDIR` on the node and using workspaces for storing models and source training data.
- **Environment Setup**: Suggested using `venvs` or `conda envs` for the training environment, with Apptainer as an alternative for difficult installations.
- **Resource Reallocation**: Accounts were enabled on the Fritz CPU cluster to meet the project's CPU-bound data generation needs.

### Conclusion:
- The ticket was closed after accounts were provided and the project started utilizing the resources.
```
---

### 2024061342001911_Usage%20of%20cluster%20for%20project%20b187cb.md
# Ticket 2024061342001911

 ```markdown
# HPC Support Ticket: Usage of Cluster for Project b187cb

## Keywords
- Cluster usage
- Job priority
- Fair-share system
- Resource allocation
- Project budget
- Resource increase request

## Summary
- **User Issue**: Students' jobs are being slowed down, likely due to low priority.
- **Root Cause**: High usage of the cluster by the project, leading to a lower priority in the fair-share system.
- **Solution**:
  - Confirmation that the project does not have a lowered priority.
  - Explanation of the fair-share system and high demand for compute nodes.
  - Notification that the project is over budget and can request a 25% increase in resources.
  - Suggestion to prepare and submit a proposal for a new NHR project.

## Detailed Conversation
- **User**: Reports that jobs are being slowed down, possibly due to low priority.
- **HPC Admin**: Explains that the project does not have a lowered priority but has used a lot of resources, affecting priority in the fair-share system. High demand for compute nodes is also noted.
- **User**: Confirms heavy usage of the cluster.
- **HPC Admin**: Informs the user that the project is over budget and can request a 25% increase in resources. Suggests preparing for a new NHR project proposal.
- **User**: Agrees to request the resource increase and apply for a new project.

## Action Items
- **User**:
  - Request a 25% increase in resources with a short justification.
  - Prepare and submit a proposal for a new NHR project.
- **HPC Admin**:
  - Monitor the resource usage and priority allocation.
  - Assist with the resource increase request and new project proposal if needed.

## Conclusion
The issue was addressed by explaining the fair-share system and providing options for increasing resource allocation. The user was advised to request additional resources and prepare for a new project proposal.
```
---

### 2018051442001512_Jobs%20on%20Emmy.md
# Ticket 2018051442001512

 ```markdown
# HPC-Support Ticket Conversation: Jobs on Emmy

## Keywords
- FEM simulation
- Deal.II library
- MPI parallelization
- Memory requirements
- FLOP/s
- Memory bandwidth
- Network traffic
- Signal 9 (Killed) error
- AccessKey
- Job monitoring

## Summary
- **User Issue**: Running FEM simulations using the Deal.II library, experiencing memory issues resulting in job termination (Signal 9 Killed).
- **HPC Admin Observations**:
  - Low FLOP/s after initial phase.
  - Low memory bandwidth usage.
  - Uneven node behavior with some nodes not performing FLOP/s or InfiniBand traffic.
- **Suggested Solutions**:
  - Run smaller test cases on a single node.
  - Use AccessKey for job monitoring.
  - Consider using machines with higher memory capacity.

## Root Cause
- High memory requirements during the initial setup phase of the simulation.
- Misconfiguration leading to uneven node behavior.

## Solution
- Distribute the job across more nodes to meet memory requirements.
- Consult with HPC Admins for access to high-memory machines.
- Review and potentially reconfigure the job setup to ensure even node participation.

## General Learnings
- **Job Monitoring**: Use AccessKey to monitor job performance and resource usage.
- **Memory Management**: Ensure sufficient memory allocation for large simulations.
- **Node Behavior**: Investigate and address uneven node behavior to optimize resource usage.
- **Collaboration**: Engage with HPC Admins for specialized hardware access and job optimization.
```
---

### 2017031142000284_LiMa%20langweilt%20sich%3F.md
# Ticket 2017031142000284

 # HPC Support Ticket: LiMa langweilt sich?

## Keywords
- OOM-Killer
- Java memory parameters
- /scratch and /tmp
- HPC job scheduling
- Memory management

## Summary
A user reported that their jobs were not running on LiMa despite having over 400 waiting jobs. The issue was traced to the OOM-Killer, which was triggered by Java processes due to incorrect memory parameters in the job script.

## Root Cause
- The user mistakenly used `-mx5g` instead of `-Xmx5g` in their Java memory parameter, leading to excessive memory usage.
- Java processes were writing data to `/scratch`, which was mapped to `/tmp` and consumed additional memory.

## Solution
- The user corrected the Java memory parameter to `-Xmx5g`.
- The user adjusted their workflow to account for memory usage by `/scratch` and `/tmp`.
- The HPC admin rebooted the affected nodes and updated the documentation to reflect the correct usage of `/scratch` and `/tmp`.

## Lessons Learned
- Always double-check memory parameters in job scripts.
- Be aware of the memory implications of writing data to `/scratch` or `/tmp`.
- Regularly monitor job logs for memory-related errors.
- Ensure documentation is up-to-date and accurate to avoid confusion.

## Actions Taken
- The HPC admin rebooted 251 nodes affected by the OOM-Killer.
- The user corrected their job scripts and restarted their jobs.
- The documentation was updated to reflect the correct usage of `/scratch` and `/tmp`.

## Follow-up
- The user should continue to monitor their jobs for memory usage and adjust parameters as needed.
- The HPC admin should periodically review and update documentation to ensure accuracy.
---

### 2023102542002712_MPI%20Fehlermeldungen%20%28omnipath%20again%3F%29.md
# Ticket 2023102542002712

 # HPC Support Ticket: MPI Fehlermeldungen (omnipath again?)

## Keywords
- MPI
- Fehlermeldungen
- libfabric
- psm2
- psmx2_epid_to_epaddr
- Operation timed out
- FI_PSM2_CONN_TIMEOUT
- Meggie

## Problem Description
- User encountered intermittent MPI errors during simulations.
- Error message indicated a timeout error related to `psm2_ep_connect`.
- The error suggested increasing the `FI_PSM2_CONN_TIMEOUT` value.

## Root Cause
- Timeout error in the `psm2_ep_connect` function.
- Current `FI_PSM2_CONN_TIMEOUT` value is set to 5 seconds.

## Solution
- Increase the `FI_PSM2_CONN_TIMEOUT` value to a larger value to mitigate timeout errors.

## Additional Information
- The issue occurred on the Meggie system.
- The error message is similar to one encountered in early September.

## Actions Taken
- User reported the issue to HPC Support.
- No specific actions taken by HPC Admins or 2nd Level Support team mentioned in the provided conversation.

## Next Steps
- HPC Admins or 2nd Level Support team should investigate the timeout error and consider increasing the `FI_PSM2_CONN_TIMEOUT` value.
- Monitor the system for further occurrences of the error.

## Contact Information
- User is from the Department of Materials Science and Engineering, Institute I, Friedrich-Alexander-Universität Erlangen-Nürnberg (FAU).

## References
- No specific references mentioned in the provided conversation.
---

### 2024062442001418_code%20and%20compilation%20on%20Fritz%20-%20b133ae19.md
# Ticket 2024062442001418

 ```markdown
# HPC-Support Ticket: Code and Compilation on Fritz - b133ae19

## Keywords
- Job Performance
- Compiler Optimization
- ClusterCockpit Monitoring
- Performance Testing

## Summary
A user was running multiple jobs on the Fritz cluster, which exhibited poor performance as observed through ClusterCockpit monitoring. The HPC Admin inquired about the code and compilers used to understand the performance issues.

## Root Cause
- The user's jobs involved short simulations/data processing compiled with `g++`.
- The poor performance was likely due to the nature of the task/algorithm rather than the compiler.

## Solution
- The HPC Admin suggested that different compilers or compiler options might improve performance but acknowledged that extensive testing would be required.
- The user was advised to conduct performance tests before future extensive calculations.
- The user was provided with links to monitoring tools:
  - [ClusterCockpit Monitoring](https://monitoring.nhr.fau.de/)
  - [Job Monitoring with ClusterCockpit](https://doc.nhr.fau.de/job-monitoring-with-clustercockpit/)

## Lessons Learned
- Regular monitoring of job performance can help identify inefficiencies.
- Different compilers or compiler options can potentially improve performance.
- Conducting performance tests before production runs is beneficial for optimizing resource usage.

## Conclusion
The ticket was closed with the user acknowledging the need for future performance testing if similar runs are planned.
```
---

### 2024112942004503_Multi-Node%20request%20for%20ELMOD.md
# Ticket 2024112942004503

 # Multi-Node Request for ELMOD

## Keywords
- Multi-node request
- a100multi QOS
- Large-scale project
- ELMOD
- Backlog
- A100

## Summary
A user requested access to the `a100multi` QOS for their large-scale project, ELMOD. The HPC Admin granted access but warned about a significant backlog of A100 nodes in the queue, which could result in long wait times for multi-node jobs.

## Root Cause
- User needed access to `a100multi` QOS for their project.

## Solution
- HPC Admin enabled the project for `a100multi` QOS.
- User was informed about the current backlog and potential long wait times.

## General Learnings
- Access to specific QOS can be requested and granted by HPC Admins.
- Significant backlogs can lead to long wait times for multi-node jobs.
- Users should be informed about potential delays due to high demand.
---

### 2022101842004021_CTESTs%20Elmer_Ice.md
# Ticket 2022101842004021

 # HPC Support Ticket Conversation: CTESTs Elmer/Ice

## Keywords
- Elmer/Ice
- MPI jobs
- Woody-NG
- Meggie
- SPACK
- AVX512 instructions
- Intel MPI
- OpenMPI
- sbatch
- FI_PSM3_UUID
- hydra_bstrap_proxy
- PMPI_Allreduce
- Invalid datatype

## Summary
The user encountered issues running Elmer/Ice tests on the Woody-NG cluster. The problems were related to MPI jobs and processor instructions.

## Root Cause
1. **MPI Jobs on Login Nodes**: MPI jobs are not supported on login nodes.
2. **Processor Instructions**: The binary required newer instructions (AVX512) not supported by some nodes.
3. **MPI Implementation Mixing**: Mixing different MPI implementations (Intel MPI and OpenMPI) caused compatibility issues.

## Solutions
1. **Avoid Running MPI Jobs on Login Nodes**: Submit jobs using `sbatch` with the `-C icx` flag to ensure they run on nodes with the required processor instructions.
2. **Consistent MPI Implementation**: Ensure all dependencies and Elmer/Ice are compiled with the same MPI implementation.
3. **Use Meggie**: For better compatibility and support for MPI jobs, consider using the Meggie cluster.

## Detailed Steps
1. **Submitting Jobs with Specific Node Requirements**:
   ```bash
   sbatch -C icx ./test_elmerice.sh
   ```
2. **Compiling with Consistent MPI**:
   - Compile all dependencies with Intel MPI if Elmer/Ice requires it.
   - Alternatively, compile Elmer/Ice with OpenMPI if dependencies require it.

## Additional Notes
- **Firewall and Port Issues**: Ensure enough ports are allowed in the firewall and specify them with the `I_MPI_PORT_RANGE` variable if needed.
- **Bootstrap Proxy Issues**: Ensure `hydra_bstrap_proxy` is available on all hosts and has the right permissions.

## Conclusion
The user was able to resolve some issues by submitting jobs with the correct node requirements. However, mixing MPI implementations caused further issues that need to be addressed by ensuring consistent compilation with a single MPI implementation. Using the Meggie cluster is recommended for better MPI support.
---

### 42039015_Turbomole%20jobs%20on%20woody.md
# Ticket 42039015

 # HPC-Support Ticket Conversation Analysis

## Subject: Turbomole jobs on woody

### Keywords:
- Turbomole
- MPI
- Infiniband
- HP-MPI
- Parallel jobs
- Temporary data
- Local disk
- Shared memory

### Issues and Solutions:

1. **Issue**: Turbomole jobs requesting 8 nodes but only using 2 CPUs.
   - **Root Cause**: Incorrect specification of the number of nodes/CPUs for Turbomole.
   - **Solution**: Use the `-n $NUMBER_OF_CORES` option to specify the number of CPUs. Alternatively, set up the job script to automatically detect and use the allocated nodes.

2. **Issue**: Turbomole jobs causing high load on file servers.
   - **Root Cause**: Temporary data not being directed to the local disk.
   - **Solution**: Use `$TMPDIR` for temporary data instead of `FASTTMP` to reduce load on the shared parallel filesystem.

3. **Issue**: Determining if Turbomole is using Infiniband.
   - **Root Cause**: Unclear how to verify the use of Infiniband.
   - **Solution**: Add `export MPIRUN_OPTIONS="-v -prot"` to the job script. Look for messages like "IBV" in the output to confirm Infiniband usage.

### General Learnings:
- **MPI Configuration**: Ensure that MPI jobs are correctly configured to use the allocated resources.
- **Temporary Data Management**: Direct temporary data to local disks to reduce load on shared filesystems.
- **Verifying Interconnect Usage**: Use specific MPI options to verify the use of high-speed interconnects like Infiniband.

### Documentation:
- **Turbomole Documentation**: Refer to Turbomole documentation for correct job submission and parallel execution.
- **HP-MPI Documentation**: Available within the Turbomole directory for detailed information on MPI options and configurations.

### Conclusion:
Proper configuration of MPI jobs and management of temporary data are crucial for efficient use of HPC resources. Verifying the use of high-speed interconnects ensures optimal performance.
---

### 2020111742002473_MPI%20error%20with%20Ansys-Fluent%202019_R1.md
# Ticket 2020111742002473

 # HPC-Support Ticket: MPI Error with Ansys-Fluent 2019/R1

## Subject
MPI error with Ansys-Fluent 2019/R1

## User Report
Dear HPC support,
I am currently trying to run a simple Fluent simulation. I am requesting only one node to check the simulation setup.
However, the simulation is crashing with the following error.

## Keywords
- MPI error
- Ansys-Fluent 2019/R1
- Simulation crash
- Single node

## Root Cause
The user is experiencing an MPI error while running a Fluent simulation on a single node.

## Solution
- **HPC Admins**: Review the MPI configuration and ensure compatibility with Ansys-Fluent 2019/R1.
- **2nd Level Support Team**: Check the job script for proper MPI initialization and resource allocation.
- **Gehard Wellein (Head of the Datacenter)**: Ensure the datacenter's MPI environment is stable and up-to-date.
- **Georg Hager (Training and Support Group Leader)**: Provide training on proper MPI usage for Fluent simulations.
- **Harald Lanig (NHR Rechenzeit Support)**: Assist with any resource allocation issues related to NHR grants.
- **Jan Eitzinger and Gruber (Software and Tools Developer)**: Investigate any software-specific issues and provide updates if necessary.

## General Learnings
- Ensure proper MPI configuration and compatibility with the software being used.
- Verify job scripts for correct MPI initialization and resource allocation.
- Regularly update and maintain the MPI environment in the datacenter.
- Provide training and support for users on MPI usage and troubleshooting.
- Address any resource allocation issues related to NHR grants.
- Collaborate with software developers to resolve software-specific issues.

## Notes
- The specific error message was not provided in the user report. Further investigation may require detailed error logs.
- Ensure that the user is aware of the steps taken to resolve the issue and any preventive measures for future runs.
---

### 2022031042001604_job%20pending%20from%202%20days.md
# Ticket 2022031042001604

 # HPC Support Ticket Analysis

## Subject
job pending from 2 days

## Keywords
- Job pending
- Long wait time
- Meggie cluster
- 40 nodes
- Simulation

## Problem
- User's job (ID: 1072730) submitted on March 7 is still pending after 2 days.
- Job requires 40 nodes for simulation.
- Unusually long wait time compared to the past 8 months.

## Root Cause
- High cluster usage and job demand on Meggie.

## Solution
- **Patience**: The cluster is busy, and the job is in the queue.
- No specific action required from the user's side.

## General Learnings
- High demand can lead to longer job pending times.
- Check cluster usage before submitting jobs requiring many nodes.
- Regularly monitor job status and cluster load.

## Roles Involved
- **HPC Admins**: Provided explanation and reassurance.
- **User**: Reported the issue and sought assistance.

## Follow-up Actions
- None required for this specific case.
- Monitor cluster usage trends for future reference.
---

### 2024110842002581_Fwd%3A%20a100multi%20access%20for%20CEEC-LSTM%20-%20EuroHPC%20Center%20of%20Excellence%20for%20Exasc.md
# Ticket 2024110842002581

 # HPC Support Ticket Analysis

## Keywords
- Multi-node usage
- Alex
- GPU hours
- QOS specification
- OTRS ticket
- Project access rights
- Batch job submission
- `sbatch` error
- `sacctmgr` command

## Summary
A user encountered issues with submitting multi-node jobs for a project, specifically receiving an `Invalid qos specification` error. The user's QOS was set to `normal`, which did not allow for multi-node submissions.

## Root Cause
- The user's QOS setting did not permit multi-node job submissions.
- The user attempted to submit a job with `--qos=a100multi`, which was not available to their account.

## Solution
- HPC Admins activated multi-node access for all project accounts, resolving the issue.

## General Learnings
- Multi-node usage on Alex requires specific access rights.
- Users should check their QOS settings using `sacctmgr show assoc where user=$USER format=User,QOS`.
- Submitting an OTRS ticket is the proper way to request additional access or report issues.
- HPC Admins can activate multi-node access for project accounts as needed.

## Documentation for Future Reference
If a user reports `Invalid qos specification` errors when submitting multi-node jobs:
1. Verify the user's QOS settings.
2. If necessary, activate multi-node access for the user's project account.
3. Inform the user about the changes and confirm the issue is resolved.
---

### 2022110842002496_Jobs%20on%20Fritz%20do%20not%20use%20the%20whole%20node%20%5Bb136dc13%5D.md
# Ticket 2022110842002496

 # HPC Support Ticket: Jobs on Fritz Do Not Use the Whole Node

## Keywords
- Job monitoring
- Cluster Cockpit
- CPU cores
- Batch script
- Submit script
- Fritz cluster
- Meggie cluster
- SLURM directives

## Problem
- User's jobs were not utilizing the allocated nodes efficiently.
- Jobs were using only a fraction of the available CPU cores.
- The second node was nearly idle.

## Root Cause
- The submit script contained batch script remnants from a different cluster (Meggie).
- The script was not optimized for the Fritz cluster.

## Solution
- Adjust the submit script to the Fritz cluster by modifying the SLURM directives:
  ```bash
  #!/bin/bash -l
  #SBATCH --nodes=2
  #SBATCH --ntasks-per-node=72
  #SBATCH --partition=multinode
  #SBATCH --export=NONE
  ```
- Instruct the user to monitor jobs using the HPC portal and Cluster Cockpit's job monitoring.

## General Learnings
- Always check and adjust submit scripts when moving jobs between different clusters.
- Regularly monitor job performance to ensure efficient use of allocated resources.
- SLURM directives should be tailored to the specific cluster's configuration.

## Follow-up
- HPC Admins to monitor upcoming jobs to ensure the issue is resolved.
---

### 2023120642001933_Multi-node%20training.md
# Ticket 2023120642001933

 ```markdown
# Multi-node Training Request

## Keywords
- Multi-node training
- Resource allocation
- SLURM directives
- OpenMPI

## Problem
- User requested permission for multi-node training for large human-pose foundation models.

## Solution
- **Resource Allocation Changes**:
  - `#SBATCH --nodes=8` (any number from 2 to 8)
  - `#SBATCH --partition=a40` (or `a100`)
  - `#SBATCH --qos=a40multi` (or `a100multi`)
- **OpenMPI Version**:
  - Load one of the version 4.1.6 modules if using OpenMPI.

## General Learnings
- Multi-node training requires specific SLURM directives for resource allocation.
- Ensure the correct partition and QoS are specified for multi-node jobs.
- Use the appropriate version of OpenMPI for compatibility.
```
---

### 2024021542002656_spr1tb%20mit%20SNC%3Doff.md
# Ticket 2024021542002656

 # HPC Support Ticket: spr1tb Partition with SNC=off

## Keywords
- spr1tb Partition
- SNC=off
- Node Reservation
- IPDPS Paper
- Deadline
- Account Access
- Health Check Exception
- BIOS Settings

## Summary
A user requested a node from the spr1tb partition with SNC=off for a specific duration to work on an IPDPS paper. The request included access for additional users.

## User Request
- **Requested Resource**: Node from spr1tb partition with SNC=off
- **Duration**: Until 22nd February
- **Additional Users**: Tom (unrz139), Georg (unrz55)

## Admin Actions
- **Initial Response**: Confirmation of request receipt and query about completion status after the deadline.
- **Follow-up**: Health check exception reverted, default BIOS settings restored on node f2277, node rebooted, and reservation removed.

## Outcome
- **Completion**: User confirmed the paper was completed by the deadline.
- **Reservation Removal**: Admin removed the reservation after the deadline.

## Lessons Learned
- **Resource Management**: Importance of timely resource allocation and removal.
- **Collaboration**: Handling requests that involve multiple users.
- **Technical Adjustments**: Steps for reverting health check exceptions and restoring BIOS settings.

## Root Cause and Solution
- **Root Cause**: User needed specific node configuration for a research paper.
- **Solution**: Admin provided the requested node and managed the reservation until the deadline, ensuring proper resource allocation and technical adjustments.

## Documentation for Future Reference
- **Node Reservation**: Ensure timely allocation and removal of reserved nodes.
- **User Access**: Manage access for multiple users as per request.
- **Technical Adjustments**: Document steps for reverting health check exceptions and restoring BIOS settings.

This documentation can be used to handle similar requests and technical adjustments in the future.
---

### 42313329_Emmy%20lustre%20file%20errors.md
# Ticket 42313329

 # HPC Support Ticket: Lustre File Errors

## Keywords
- Lustre file errors
- Job failure
- Memory issues
- Out of memory (OOM)
- System wait CPU
- Job hanging

## Problem Description
- User reported job failures due to inability to read/write files on the Lustre filesystem.
- Jobs were hanging with 100% system wait CPU usage.

## Root Cause
- Jobs were running out of memory, leading to the invocation of the OOM killer.
- Specifically, one process (`pw4gww.x`) used 9 GB of memory, causing memory exhaustion on nodes with 64 GB RAM.

## Solution
- Ensure jobs do not consume excessive memory.
- Monitor memory usage and adjust job configurations accordingly.
- Increase the number of nodes if memory requirements are high.

## Additional Notes
- The user clarified that the job in question (258212) did not involve `pw4gww.x` but `pw.x`.
- The user is aware of memory issues with `pw4gww.x` and adjusts node allocation as needed.

## Action Taken
- HPC Admin provided insights into memory usage and its impact on the filesystem and job performance.
- User was advised to review and manage memory usage more effectively.

## Follow-up
- No further action required from the user's perspective as the issue was understood and managed.
- Continuous monitoring of job memory usage is recommended to prevent similar issues in the future.
---

### 2020030542002261_Jobs%20auf%20Emmy%20nutzen%20regelm%C3%83%C2%A4%C3%83%C2%9Fig%20nur%20die%20H%C3%83%C2%A4lfte%20der%.md
# Ticket 2020030542002261

 ```markdown
# HPC Support Ticket: Jobs auf Emmy nutzen regelmäßig nur die Hälfte der Knoten - mpp3000h

## Keywords
- Resource allocation
- Job efficiency
- MPI jobs
- Queue management
- Priority adjustment

## Problem Description
- User's jobs on Emmy regularly use only half of the allocated nodes.
- Examples of job IDs: 1262649, 1262507, 1262028, 1262027, 1261950, 1216620, 1216525.

## Root Cause
- Mismatch between resource allocation and `mpirun` call.

## Impact
- Unnecessary blocking of resources, especially during periods of long queues.

## Solution
- Adjust resource allocation to match the `mpirun` call.
- Ensure efficient use of HPC resources to avoid long wait times for other users.

## Actions Taken
- HPC Admins notified the user multiple times about the issue.
- User did not seek support or show interest in resolving the issue.
- User's priority was reduced to ensure fair resource allocation for other users.

## Follow-Up
- User should confirm that the problem has been resolved.
- Continuous monitoring of job efficiency to prevent similar issues in the future.

## General Learning
- Importance of matching resource requests with actual usage.
- Efficient resource management to minimize queue times.
- Consequences of not adhering to resource usage guidelines, including priority reduction.
```
---

### 2019121642003715_singularity%20jobs%20on%20emmy%20iwsp011h%201200861%5B0%5D.md
# Ticket 2019121642003715

 # HPC Support Ticket Analysis: Singularity Jobs on Emmy

## Keywords
- Singularity jobs
- Job activity
- Resource allocation
- Python scripts
- Job efficiency
- Premium customer

## Summary
A user's Singularity jobs on the Emmy cluster showed no activity. The HPC Admins investigated the issue and found that the jobs were not utilizing the allocated resources efficiently. The user was running serial Python processes but requesting multiple nodes, leading to inefficient use of cluster resources.

## Root Cause
- The user's jobs were not optimized for parallel processing, leading to inefficient resource usage.
- The jobs were requesting 8 nodes but not utilizing the computing power effectively.

## Solution
- The HPC Admins identified the inefficiency and suggested that the user optimize their jobs for better resource utilization.
- The ticket was closed after noting that the user had not submitted new jobs in the last 10 days.

## Lessons Learned
- **Resource Allocation**: Ensure that jobs are optimized for the resources they request. Serial processes should not request multiple nodes unless necessary.
- **Job Monitoring**: Regularly monitor job activity to identify and address inefficiencies.
- **Customer Support**: Premium customers, such as those who have financed cluster expansions, should receive priority support.

## Actions Taken
- The HPC Admins investigated the job scripts and identified the inefficiency.
- The issue was escalated within the support team for further action.
- The ticket was closed due to inactivity from the user.

## Recommendations
- **User Training**: Provide training or documentation on efficient job submission and resource allocation.
- **Job Review**: Implement a review process for jobs that request significant resources to ensure they are optimized.
- **Communication**: Maintain open communication with users to address any issues promptly.

## Conclusion
Efficient resource allocation is crucial for the optimal performance of the HPC cluster. Regular monitoring and user education can help prevent such issues in the future.
---

### 2022050542003378_Re%3A%20%5BRRZE-HPC%5D%20Call%20for%20early-adopter%20of%20parallel%20computer%20Fritz.md
# Ticket 2022050542003378

 ```markdown
# HPC Support Ticket Conversation Analysis

## Subject
Re: [RRZE-HPC] Call for early-adopter of parallel computer Fritz

## Keywords
- Queue
- 24 hours
- Fritz
- HPC Admin
- User

## Problem
- **Root Cause:** User inquires about the availability of a queue with more than 24 hours on the Fritz system.

## Solution
- **Response:** HPC Admin confirms that there is no queue with more than 24 hours available on Fritz.

## General Learnings
- Understanding the current queue limitations on the Fritz system.
- Importance of clear communication regarding system capabilities.

## Notes
- The conversation highlights the need for users to be aware of system constraints.
- HPC Admins should regularly update users on system capabilities and limitations.
```
---

### 2021050542000284_intel_MPI%20problem%20on%20meggie%3F%20%28gwgi18%29.md
# Ticket 2021050542000284

 # HPC Support Ticket: Intel/MPI Problem on Meggie

## Keywords
- WRF jobs
- MPI errors
- Omnipath network
- Optical cables
- Job hangs
- stdout/err files

## Problem Description
- User's WRF jobs were sporadically hanging and not generating stdout/err files.
- No error messages in the batch script stdout.
- MPI initialization errors were reported.
- Issue did not occur with an old executable but affected both the last working backup and new clean builds.

## Root Cause
- Faulty optical cables in the Omnipath network on Meggie.
- These bad links caused random job failures and confusion in the subnet manager.

## Solution
- HPC Admins identified and disabled the faulty optical cable links.
- Users were advised to retry their jobs and report back if the problem persisted.

## Lessons Learned
- Network issues, particularly with optical cables, can cause sporadic job failures and MPI errors.
- These issues can be hard to detect and resolve, often requiring several days to identify and fix.
- Users should be aware that such problems might not be related to their executables but rather to the underlying infrastructure.

## Follow-Up
- Users should monitor their jobs and report any recurring issues to HPC Support.
- HPC Admins should continue to monitor the health of the network and take proactive measures to identify and disable faulty links.
---

### 2022072042003569_Fwd%3A%20Tuning%20Code%20performance%20on%20Fritz.md
# Ticket 2022072042003569

 # HPC Support Ticket: Tuning Code Performance on Fritz

## Keywords
- Code performance
- Scaling runs
- Efficiency
- Bandwidth-bound
- Cache size
- Problem size
- Trilinos
- Epetra
- Tpetra
- Kokkos

## Summary
A user encountered performance issues with their code on the Fritz HPC system. The code runs smoothly but has varying performance depending on the number of nodes used.

## Root Cause
- The code appears to be memory-bound on a single node.
- The efficiency of the code decreases as the number of nodes increases, but it is still within a tolerable range.
- The problem size per node decreases with more nodes, leading to data fitting in cache and lower main-memory bandwidth.

## Analysis
- **Single Node Performance**: Close to being bandwidth-bound but has not hit the maximum limit.
- **Multi-Node Performance**: Efficiency decreases but is still acceptable (76% for 4 nodes). The data starts to fit in cache, leading to lower memory traffic.
- **Hypothesis**: There might be an extra overhead or an in-core bottleneck preventing significant performance improvement.

## Recommendations
- **Problem Size**: Try running with a larger problem size to validate the hypothesis about cache usage.
- **Bottleneck Identification**: Perform more measurements and inspect the source code to identify bottlenecks or overheads.
- **Library Usage**: Check if Trilinos with Epetra or Tpetra is used, and if Tpetra, whether the Kokkos backend is utilized.

## Conclusion
The user should experiment with larger problem sizes and perform detailed measurements to identify and address potential bottlenecks in the code. The efficiency of the code is within acceptable limits, but further optimization may be possible.

## Next Steps
- Run tests with a larger problem size.
- Perform detailed measurements to identify bottlenecks.
- Review the source code for potential optimizations.

---

This report provides a summary of the issue, the root cause, analysis, recommendations, and next steps for improving code performance on the Fritz HPC system.
---

### 2017031342001421_OOM-Killer%20am%20Werk%3F.md
# Ticket 2017031342001421

 # HPC Support Ticket: OOM-Killer am Werk?

## Keywords
- OOM-Killer
- Java
- SIGKILL
- Scratch files
- Job termination

## Problem Description
- User reported multiple Java processes terminated by signal 9 (SIGKILL) in log files.
- Suspected OOM-Killer as the cause.
- Concerns about leftover files in `/scratch` directories on lima-Knoten and possibly emmy.

## Root Cause
- Java processes were terminated by signal 9, indicating potential memory issues.
- OOM-Killer is a likely cause, but other factors could also be involved.

## Solution
- No specific solution provided in the conversation.
- Further investigation needed to confirm the cause of the terminations.

## General Learnings
- OOM-Killer can terminate processes to free up memory.
- Java processes terminated by signal 9 may indicate memory issues.
- Leftover files in `/scratch` directories can be a concern if jobs do not clean up properly.

## Next Steps
- Investigate the cause of the Java process terminations.
- Check if OOM-Killer logs are available for further analysis.
- Ensure proper cleanup of `/scratch` directories to avoid restricting other users.
---

### 42047032_woody%20batch%20job.md
# Ticket 42047032

 # HPC Support Ticket: Woody Batch Job Delay

## Keywords
- Batch jobs
- Job queue
- Cluster load
- Account priority
- StarCCM+
- Job scheduling

## Problem Description
- User submitted two batch jobs requiring 8 nodes with 4 processors each.
- Jobs remained in the queue overnight, which was unusual.
- User suspected an error with the batch script or the cluster.

## Root Cause
- High cluster load causing job scheduling delays.

## Solution
- Confirmed that the user's account and the cluster were functioning correctly.
- Informed the user that the cluster was heavily loaded.
- Suggested increasing the user's account priority, pending approval from the relevant authority.

## General Learnings
- High cluster load can cause delays in job scheduling.
- Account priorities can be adjusted to manage job scheduling during high load periods.
- Communication with users about cluster load and job priorities is important for managing expectations.

## Actions Taken
- Verified user account and cluster functionality.
- Explained the current cluster load situation to the user.
- Discussed the possibility of adjusting the user's account priority.

## Follow-up
- Awaiting approval from the relevant authority to adjust the user's account priority.

## Related Parties
- HPC Admins
- 2nd Level Support Team
- Head of the Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support
- Software and Tools Developer
---

### 2023032342004121_Problem%20with%20mpirun%20and%20ORCA%20at%20TinyFat.md
# Ticket 2023032342004121

 # HPC Support Ticket: Problem with mpirun and ORCA at TinyFat

## Keywords
- mpirun
- ORCA
- TinyFat
- Open MPI
- Slots
- Submission script
- Error termination
- GTOInt

## Problem Description
- User encountered issues with `mpirun` while running ORCA on TinyFat cluster.
- Error message indicated insufficient slots available for the requested application.
- ORCA terminated with an error in GTOInt.

## Root Cause
- User was manually calling `mpirun` to run ORCA, which is not required as ORCA handles MPI internally.

## Solution
- Do not manually call `mpirun` when running ORCA.
- Refer to ORCA documentation or specific instructions for running ORCA on TinyFat: [ORCA Documentation](https://hpc.fau.de/systems-services/documentation-instructions/special-applications-and-tips-tricks/orca/#collapse_0).

## General Learnings
- ORCA manages its own MPI processes internally.
- Manually calling `mpirun` can lead to slot allocation issues and errors.
- Always refer to the specific documentation for running applications on HPC clusters.

## Actions Taken
- HPC Admins advised the user to avoid manually calling `mpirun` with ORCA.
- Provided a link to the relevant documentation for running ORCA on TinyFat.

## Future Reference
- For similar issues, ensure that users are not manually calling `mpirun` with applications that handle MPI internally.
- Direct users to the appropriate documentation for running specific applications on the cluster.
---

### 2024070242003956_Tier3-Access-Fritz%20%22Yashasvi%20Verma%22%20_%20iwtm100h.md
# Ticket 2024070242003956

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject: Tier3-Access-Fritz "User" / iwtm100h

### Keywords
- Tier3 Access
- Fritz
- Multi-node workload
- HDR100 Infiniband
- MPI
- Dealii v9.5.0
- MRI wave simulation
- Large problem size
- .vtu files

### Summary
- **User Request:** Access to Fritz for a multi-node workload.
- **Resource Requirements:**
  - HDR100 Infiniband with 1:4 blocking.
  - Per node: 72 cores, 250 GB.
  - 2400 node hours.
- **Software Requirements:** MPI with Dealii v9.5.0 or above.
- **Application:** MRI wave simulation on a 3D geometry file with 100,000 cells and 20,000 timesteps.
- **Expected Output:** Around 20,000 .vtu files for data extraction using Python/MATLAB.

### Root Cause of the Problem
- User needs access to Fritz for a large-scale simulation requiring significant computational resources.

### Solution
- **HPC Admin Response:** User granted access to Fritz.

### General Learnings
- Proper documentation of user requests and resource allocations.
- Importance of specifying software versions and expected outputs.
- Handling large-scale simulations with specific hardware requirements.

### Notes
- Ensure users are aware of the process for requesting access and resources.
- Maintain clear communication regarding the status of access requests.
```
---

### 2018052942002458_Jobs%20crashing%20Emmy%20nodes%20-%20iww8002h.md
# Ticket 2018052942002458

 ```markdown
# HPC Support Ticket: Jobs Crashing Emmy Nodes

## Keywords
- Out of memory
- Job suspension
- Node crashing
- spectrum_L_perc

## Summary
- **Issue**: User's jobs on Emmy nodes are crashing due to out-of-memory errors.
- **Affected Nodes**: Multiple nodes including e0505, e0615, e0616, etc.
- **Process**: `spectrum_L_perc`
- **Action Taken**: User's account temporarily suspended in the batch system.

## Root Cause
- The user's jobs were consuming more memory than available on the nodes, leading to the out-of-memory errors and subsequent crashes.

## Solution
- The user's account was temporarily suspended to prevent further node crashes.
- The user was notified about the issue and the suspension.

## Lessons Learned
- Ensure that job memory requirements are within the limits of the allocated nodes.
- Monitor job performance to prevent excessive memory usage.
- Communicate with users promptly to address and resolve issues.

## Follow-Up
- The user's account was re-enabled after no response from the user.
- The ticket was closed with a note in `maui.cfg` for future reference.
```
---

### 2025031942001057_%5Baction%20requiered%5D%20short%20running%20jobs%20on%20fritz%20%5Bb243cb11%5D.md
# Ticket 2025031942001057

 # HPC Support Ticket Analysis: Short Running Jobs on Fritz

## Keywords
- Short running jobs
- Email notifications
- Job runtime
- Throttling policy
- Mail server issues
- Job validation

## Root Cause
- User submitted a large number of short-running jobs (runtime < 5 minutes) on the Fritz cluster.
- High rate of email notifications (`#SBATCH --mail-type=ALL`) caused issues with the mail server.

## Issues Caused
- Operational issues with the cluster.
- Overload of the mail server.

## Actions Taken by HPC Admins
- Canceled all running jobs for the user.
- Reduced the number of nodes the user is allowed to use down to 1.
- Set additional throttling policy (`maxsubmitjobs=1`).

## Required User Actions
- Stop sending email notifications for thousands of jobs.
- Avoid submitting jobs with runtimes under 5 minutes.
- Ensure rigorous testing and validation of all jobs locally before automated submission.

## Solution
- User acknowledged the issues and agreed to implement the suggested actions to regain normal usage permissions.

## General Learning
- Short-running jobs can cause operational issues on the cluster.
- High rate of email notifications can overload the mail server.
- Proper job validation and testing are crucial before automated submission to maintain optimal efficiency.

## Documentation for Support Employees
- When encountering similar issues, advise users to:
  - Discontinue email notifications for job submissions.
  - Avoid submitting jobs with runtimes under 5 minutes.
  - Ensure rigorous testing and validation of all jobs locally before automated submission.
- Implement throttling policies if necessary to manage resource allocation effectively.
---

### 2021030542001849_Jobs%20on%20emmy%20-%20iwst070h.md
# Ticket 2021030542001849

 ```markdown
# HPC Support Ticket Conversation Analysis

## Keywords
- HPC
- MPI
- Job Scheduling
- Resource Allocation
- Performance Optimization
- Parallel Processing
- Batch Script
- PBS
- OpenMPI
- IntelMPI
- Woody Cluster
- Emmy Cluster
- MPI Error
- ptrace
- I_MPI_SHM_LMT

## General Learnings
- **Resource Allocation**: Ensure that jobs are using all allocated nodes and cores to avoid resource wastage.
- **MPI Process Pinning**: Proper pinning of MPI processes can help in better resource utilization and performance.
- **Batch Script Optimization**: Use `wait` instead of `sleep` for better job completion handling.
- **MPI Error Handling**: Understand and address MPI errors related to shared memory and process communication.
- **Cluster Selection**: Choose the appropriate cluster (e.g., Woody vs. Emmy) based on job requirements and performance.

## Root Causes of Problems
- **Resource Wastage**: User's jobs were not utilizing all allocated nodes and cores.
- **MPI Process Placement**: MPI processes were not properly pinned, leading to suboptimal performance.
- **Batch Script Issues**: Incorrect use of `sleep` instead of `wait` led to job completion issues.
- **MPI Errors**: Errors related to shared memory and process communication in MPI jobs.

## Solutions
- **Resource Allocation**: Adjust job scripts to utilize all allocated resources.
- **MPI Process Pinning**: Implement proper pinning of MPI processes to ensure optimal resource usage.
- **Batch Script Optimization**: Use `wait` instead of `sleep` to handle job completion correctly.
- **MPI Error Handling**: Add `export I_MPI_SHM_LMT=shm` to address shared memory issues. Modify MPI functions to include necessary parameters.
- **Cluster Selection**: Test jobs on different clusters (e.g., Woody) to find the best performance and resource utilization.

## Specific Issues and Solutions
- **MPI Error on Woody Cluster**: Added `export I_MPI_SHM_LMT=shm` and modified MPI function parameters to resolve the error.
- **Batch Script for Parallel Jobs**: Adjusted the script to properly utilize allocated nodes and cores, and used `wait` for job completion.
- **Performance Testing**: Conducted performance tests to determine the optimal number of processes for the job.

## Conclusion
The conversation highlights the importance of proper resource allocation, MPI process pinning, and batch script optimization for efficient job execution on HPC clusters. Addressing MPI errors and selecting the appropriate cluster can significantly improve job performance and resource utilization.
```
---

### 2018112642000999_netcdf%20auf%20emmy.md
# Ticket 2018112642000999

 # HPC-Support Ticket Conversation Analysis

## Subject: netcdf auf emmy

### Keywords:
- NetCDF
- Performance
- Skalierungstests
- Ozeanmodell
- Queue
- Timeout
- MPI
- Pinning
- Dateisystem
- Broadcast
- MPI-IO
- Reservierung
- Debugging

### What Can Be Learned:

#### User Issues:
1. **NetCDF Version**: The user requested an updated version of NetCDF for performance reasons.
2. **Queue Issues**: The user's jobs were rejected due to queue limits and deactivation.
3. **Job Hang**: Jobs were hanging during file read operations, leading to timeouts.
4. **MPI Wrapper**: Issues with using the MPI wrapper `mpirun_rrze` for large jobs.
5. **Debugging**: The user needed interactive reservations for debugging purposes.

#### HPC Admin Responses:
1. **NetCDF Update**: The HPC Admin updated the NetCDF version on the system.
2. **Queue Management**: The Admin temporarily increased queue limits and activated the 'big' queue.
3. **MPI Wrapper**: The Admin advised using the original Intel MPI mechanism with `mpiexec.hydra` and proper pinning options.
4. **Reservations**: The Admin provided reservations for debugging and suggested testing with different date systems and MPI versions.
5. **Job Termination**: The Admin assisted in terminating a hung job.

### Root Cause of Problems:
1. **NetCDF Version**: The older version of NetCDF was causing performance issues.
2. **Queue Limits**: The 'big' queue had limits that were too restrictive for the user's jobs.
3. **MPI Wrapper**: The use of `mpirun_rrze` was causing issues with large jobs.
4. **File Read Operations**: The jobs were hanging during file read operations, possibly due to I/O issues or MPI communication problems.

### Solutions:
1. **NetCDF Update**: Updating the NetCDF version resolved performance issues.
2. **Queue Management**: Temporarily increasing queue limits and activating the 'big' queue allowed the user's jobs to run.
3. **MPI Wrapper**: Switching to the original Intel MPI mechanism with `mpiexec.hydra` and proper pinning options resolved issues with large jobs.
4. **Debugging**: Providing interactive reservations and suggesting tests with different date systems and MPI versions helped the user debug the hanging jobs.
5. **Job Termination**: The Admin assisted in terminating a hung job to free up resources.

### General Learnings:
- **Queue Management**: Understanding and managing queue limits and activation is crucial for handling large jobs.
- **MPI Wrapper**: Using the appropriate MPI wrapper and pinning options is essential for large jobs.
- **Debugging**: Providing interactive reservations and suggesting tests with different configurations can help users debug complex issues.
- **NetCDF Performance**: Updating NetCDF versions can resolve performance issues in scientific applications.

This analysis can be used as a reference for future support tickets involving similar issues with NetCDF, queue management, MPI wrappers, and job debugging.
---

### 2019101442002385_request%20of%20appointment.md
# Ticket 2019101442002385

 # HPC Support Ticket Conversation Summary

## Subject: Request of Appointment

### Keywords:
- Parallel code
- Cluster usage
- OpenMP
- MPI
- Job termination
- Performance optimization
- Waiting time
- Memory management

### General Learnings:
- **Cluster Load and Job Priority**: Clusters under heavy load prioritize jobs based on compute time consumed by the user and their group in the last 10 days.
- **Performance Analysis**: Using tools like `perf` from the Linux kernel can help identify performance bottlenecks such as excessive time spent in OpenMP barriers and memory allocation/deallocation.
- **Optimization Suggestions**: Reducing the number of OpenMP threads per node and minimizing temporary variable creation/destruction can improve performance.
- **Job Monitoring**: Users can access system monitoring data for their jobs using an AccessKey provided at the end of the STDOUT file.

### Root Cause of the Problem:
- **Code Issue**: The user's code had a "double free or corruption" error, leading to occasional bad terminations.
- **Performance Bottlenecks**: Excessive time spent in OpenMP barriers and frequent memory allocation/deallocation.

### Solutions:
- **Code Fix**: Address the "double free or corruption" error to prevent bad terminations.
- **Performance Improvement**: Reduce the number of OpenMP threads to 20 per node and minimize the creation/destruction of temporary variables.
- **Further Analysis**: Provide a minimal configuration that replicates the performance characteristics of full-scale runs for thorough analysis.

### Actions Taken:
- **Initial Response**: HPC Admin requested more specific questions and provided basic documentation on cluster usage.
- **Detailed Analysis**: HPC Admin analyzed the user's job and provided insights into performance bottlenecks and potential solutions.
- **Appointment Scheduling**: HPC Admin offered dates for a meeting to discuss performance problems in detail and potential optimization strategies.

### Follow-up:
- **Meeting**: A meeting was scheduled to discuss the user's performance problems and potential optimization strategies.
- **Outcome**: The user's supervisor preferred the user to focus on the physics aspect of the code rather than performance optimization.

### Conclusion:
- The conversation highlights the importance of detailed performance analysis and the need for collaboration between users and HPC support to optimize code performance on the cluster.
---

### 2022042242000948_Jobs%20auf%20meggie%20nutzen%20nur%20einen%20Knoten%20%7C%20iww1010h.md
# Ticket 2022042242000948

 # HPC Support Ticket: Jobs Using Only One Node

## Keywords
- Job script
- MPI-parallel application
- Node utilization
- Simulation

## Problem
- User's jobs were only utilizing one out of the five requested nodes.
- Root cause: Incorrect job script configuration for non-MPI-parallel applications.

## Solution
- Adjust the job script to properly utilize the requested nodes.
- Ensure the job script is configured correctly for non-MPI-parallel applications.

## Lessons Learned
- Always verify job script configurations to ensure proper resource utilization.
- Non-MPI-parallel applications require specific script adjustments to use multiple nodes effectively.

## Actions Taken
- HPC Admin notified the user about the issue.
- User acknowledged the problem and restarted the simulations with corrected job scripts.
- Ticket closed after verifying that new simulations were running correctly.

## References
- HPC Support: support-hpc@fau.de
- HPC Website: [https://hpc.fau.de/](https://hpc.fau.de/)
---

### 2024060742002333_longer%20runtime%20since%205_6_2024.md
# Ticket 2024060742002333

 ```markdown
# HPC Support Ticket: Longer Runtime Since 5/6/2024

## Keywords
- Performance degradation
- OS update
- CPU frequency
- Memory bandwidth
- Energy saving states
- SLURM
- ClusterCockpit

## Summary
A user reported that their jobs, which usually took 13-14 hours, started taking over 16 hours since 5/6/2024. This issue coincided with an OS update to Alma 8.10.

## Root Cause
- The OS update introduced more aggressive energy-saving states, leading to lower average CPU frequencies.
- The user's jobs were not utilizing all cores, resulting in large frequency variations.

## Solution
- The user was advised to enforce higher CPU frequencies using SLURM's `--cpu-freq` parameter.
- Setting `--cpu-freq=performance` was recommended to achieve full turbo without underclocking.
- The user confirmed that this solution restored and even improved the previous computation times.

## Additional Information
- The user observed reduced memory bandwidth, which was addressed by adjusting the CPU frequency.
- No compute time refund/compensation was offered as performance was not guaranteed.
- The user was advised to use frequencies above the nominal frequency to prevent underclocking.

## Documentation
- [SLURM Advanced Topics: Specific Clock Frequency](https://doc.nhr.fau.de/batch-processing/advanced-topics-slurm/?h=freq#specific-clock-frequency)

## Notes
- The user was curious about the optimal CPU frequency and was advised to use the `performance` governor to prevent underclocking.
- The user was asked why they were not using all available cores per node.
```
---

### 2022112842003804_Tier3-Access-Fritz%20%22Egor%20Trushin%22%20_%20bctc33.md
# Ticket 2022112842003804

 # HPC Support Ticket Analysis

## Keywords
- Tier3 Access
- Fritz Cluster
- NHR Projects
- Compute Time
- Python3.9
- PySCF
- JAX
- Node Hours
- Publication

## Summary
- **User Request**: Access to Fritz cluster for computational chemistry calculations using Python3.9, PySCF, and JAX. Initial request for 200,000 node hours, later corrected to 20,000.
- **HPC Admin Response**: Clarification on linking account to existing NHR projects. Informed user about the feasibility of compute time within Tier3 service.

## Root Cause of the Problem
- Incorrect estimation of required compute time by the user.

## Solution
- User corrected the compute time requirement to 20,000 node hours.
- HPC Admin confirmed that 20,000 node hours per year may be feasible within the Tier3 service.

## General Learnings
- Compute time requests should be carefully estimated to avoid misunderstandings.
- Tier3 throttling is per group, not per user, affecting the allocation of compute resources.
- Clear communication about project independence and resource allocation is crucial.

## Actions Taken
- User account enabled on Fritz cluster.
- Discussion on linking user account to existing NHR projects.
- Clarification on the feasibility of requested compute time.

## Follow-up
- User to proceed with calculations using the allocated compute time.
- Monitor usage to ensure it aligns with the estimated requirements.
---

### 2022112542000054_Probleme%20mit%20VASP%20Slurm%20Beispiel-Batch.md
# Ticket 2022112542000054

 # HPC Support Ticket: Issues with VASP Slurm Example Batch

## Keywords
- VASP
- Slurm
- Module Load
- MPI
- pkill

## Problem Description
- User encountered issues with the VASP Slurm example batch script on the HPC website.
- The `module load intel64` command is no longer available.
- Loading `intel`, `mkl`, and `intelmpi` modules resulted in MPI startup warnings.
- The `pkill -p` option does not exist.

## Root Cause
- Outdated example batch script on the HPC website.
- Incorrect module loading commands and options.

## Solution
- HPC Admins updated the VASP example batch script.
- Confirmed that `intel`, `mkl`, and `intelmpi` modules are required for VASP.
- MPI startup warnings can be ignored if the job runs without other issues.
- Removed the incorrect `pkill -p` option.

## General Learnings
- Keep example scripts and documentation up-to-date.
- Verify module availability and correct options for commands.
- MPI startup warnings related to `I_MPI_PMI_LIBRARY` can be ignored if jobs run successfully.
- Ensure correct usage of command options (e.g., `pkill`).
---

### 2024052942002893_H%C3%83%C2%B6here%20Prio%20f%C3%83%C2%BCr%20Revision.md
# Ticket 2024052942002893

 ```markdown
# HPC-Support Ticket: Higher Priority Request for Revision Phase

## Keywords
- Priority Increase
- Revision Phase
- Deadline
- Job Queue
- Cluster
- JobID

## Summary
A user requested higher priority for their jobs due to an upcoming manuscript revision deadline.

## Root Cause
- User is concerned about meeting the deadline for their manuscript revision due to potential job queue delays.

## HPC Admin Response
- The HPC Admin noted that recent wait times on the clusters have been manageable.
- No immediate need for manual priority adjustments was identified.
- The user was advised to report any significant delays in job processing, including the specific cluster and JobID.

## Solution
- Monitor job queue times.
- Report any significant delays to the HPC Support Team with specific details (Cluster & JobID).

## General Learning
- Users should be aware of current cluster load and queue times.
- Communicate with the HPC Support Team if job delays are impacting critical deadlines.
- Provide specific details (Cluster & JobID) when reporting issues to facilitate quicker resolution.
```
---

### 2025022542003072_Project%20Optimization%20of%20LuKARS_REACT%20-%20gz16104h.md
# Ticket 2025022542003072

 # Project Optimization of LuKARS_REACT - gz16104h

## Summary
The user, Beatrice, is working on optimizing the coupling between LuKARS 3.0 and IPHREEQC, a Python interface for the PHREEQC geochemical modeling software. The project is funded within the framework of KONWIHR for a duration of three months starting on 31/01/2025.

## Key Issues and Solutions

### Installation of IPHREEQC
- **Issue**: The installation of IPHREEQC is straightforward but does not generate a shared library required for use with phreeqpy.
- **Solution**: Manually create a shared library using the following command:
  ```bash
  g++ -O2 -fPIC -shared -Isrc -Isrc/common -Isrc/PhreeqcKeywords src/*.cpp -o libphreeqc.so
  ```

### GLIBC Version Conflict
- **Issue**: The user encountered an error related to GLIBC version 2.29 not being found.
- **Solution**: Avoid updating GLIBC manually as it can break the system. Instead, use a container to isolate the environment.
  ```bash
  Bootstrap: docker
  From: ubuntu:22.04
  %post
      apt-get update
      apt-get -y upgrade
      apt-get install -y wget git tar make gcc python3 python3-pip
      pip install --user phreeqpy
  %runscript
      python3 "$@"
  ```

### PHREEQC Version Compatibility
- **Issue**: The current version of phreeqc (3.8.6) does not work with phreeqpy.
- **Solution**: Use PHREEQC version 3.7.3, which is bundled with phreeqpy.
  ```bash
  pip install -U phreeqpy
  ```

### COM Object Issue
- **Issue**: The user's code was written using iphreeqcCOM object, which is for a Windows system.
- **Solution**: Use `phreeqpy.iphreeqc.phreeqc_dll` instead of `phreeqc_com`.
  ```python
  import phreeqpy.iphreeqc.phreeqc_dll as phreeqc_mod
  phreeqc = phreeqc_mod.IPhreeqc()
  ```

### Parallel Job Execution
- **Issue**: The user wants to run multiple jobs in parallel for optimization.
- **Solution**: Use job scheduling tools provided by the HPC cluster to run jobs in parallel.

## Meetings and Communication
- **Meeting Scheduled**: Thursday, March 13, 12:00 - open end.
- **Zoom Link**: [Zoom Meeting](https://fau.zoom-x.de/j/67290330382?pwd=A7vNb2GqpPQKDMaGtfnIXZ37NM5Bv6.1)
- **Meeting ID**: 672 9033 0382
- **Kenncode**: 698145

## Next Steps
- The user will run a set of model realizations to evaluate performance.
- Further optimization will be discussed in the scheduled meeting.

## Conclusion
The user successfully resolved the GLIBC version conflict by using a container and switched to the compatible PHREEQC version. The next steps involve running model realizations and discussing further optimization strategies in the upcoming meeting.

---

This report summarizes the key issues and solutions discussed in the support ticket for the project optimization of LuKARS_REACT. It serves as a documentation for support employees to look up help for similar errors in the future.
---

### 2018112642001596_Meggie%20OpenFoam%20und%20MPI.md
# Ticket 2018112642001596

 # HPC Support Ticket: Meggie OpenFoam und MPI

## Problem
- **User Issue**: Slow performance of post-processing operations and reconstruction of parallelized simulations in OpenFoam with the new I/O system (collated file handling).
- **Root Cause**: Lack of threading support in the MPI system (`MPI_THREAD_MULTIPLE: no`).

## Solution
- **Initial Attempt**: User tried to enable threading support by using `openfoam/5.0a-trusty-ompithreads`, but it did not improve performance.
- **Alternative Solution**: User tested `openfoam/1806-gcc8.2.0-openmpi+p7c5cn` on Emmy, which resolved the performance issue.
- **Final Resolution**: HPC Admin compiled and made available `openfoam/1806-gcc8.2.0-openmpi+xdhukb` on Meggie, which included the necessary threading support.

## Keywords
- OpenFoam
- MPI
- Threading Support
- Collated File Handling
- Performance Issue
- Reconstruction
- Post-Processing

## General Learnings
- **Threading Support**: Ensuring that the MPI system supports threading (`MPI_THREAD_MULTIPLE`) is crucial for improving the performance of parallel I/O operations in OpenFoam.
- **Module Availability**: Different modules of OpenFoam may have varying levels of support and performance. Testing different versions and compilers can help identify the best configuration.
- **User Configuration**: Users can override certain settings in their local OpenFoam configuration (`~/.OpenFOAM/$WM_PROJECT_VERSION/controlDict`) to optimize performance.

## Additional Notes
- **SLURM Script**: The user provided a SLURM script for running reconstruction operations. It is important to ensure that the script is correctly configured to utilize the available resources efficiently.
- **Compiler Issues**: Some OpenFoam utilities, such as `reconstructPar` and `decomposePar`, may not work with certain compilers (e.g., Clang). It is essential to test and verify the functionality of these utilities with different compiler versions.

## Conclusion
The issue was resolved by providing a compatible OpenFoam module with the necessary threading support. Users should test different modules and configurations to optimize performance for their specific use cases.
---

### 2019032842002541_Question%20regarding%20Cluster.md
# Ticket 2019032842002541

 # HPC Support Ticket Analysis: Cluster Job Delays

## Keywords
- Cluster EMMY
- Job queue
- Priority
- Job dependencies
- Deadline
- Fairshare boost

## Summary
A user experienced delays in job execution on the cluster EMMY and sought assistance to understand the reasons and potential solutions.

## Root Cause
- **High Cluster Utilization**: The cluster was full, leading to long queue times.
- **Group Usage**: Other members of the user's group had used a significant portion of the cluster's compute cycles, affecting the user's priority.
- **Job Dependencies**: The user's jobs were dependent on each other, with each job waiting for the previous one to finish before starting.

## Solutions and Recommendations
- **Priority Boost**: The HPC team temporarily increased the user's priority on the cluster until a specified date to help expedite job processing.
- **Job Time Estimation**: The user was advised to estimate job run times more accurately if possible. Shorter jobs might execute earlier if they can fill gaps in the schedule.
- **Realistic Expectations**: The user was informed not to expect miracles despite the priority boost, given the high demand and limited resources.

## General Learnings
- **Cluster Utilization**: High demand can lead to significant delays in job execution.
- **Job Dependencies**: Dependent jobs can exacerbate delays, especially if each job requires a substantial amount of time.
- **Priority Management**: The HPC team can temporarily boost a user's priority to help meet deadlines, but this is not a guaranteed solution.
- **Accurate Job Specification**: Users should estimate job run times as accurately as possible to optimize resource allocation and potentially reduce waiting times.

## Actions Taken
- The HPC team provided explanations and recommendations to the user.
- A temporary priority boost (fairshare boost) was applied to the user's account to help expedite job processing.
- The priority boost was later removed as scheduled.

This analysis can serve as a reference for future cases involving job delays and priority management on the cluster.
---

### 2018041742001849_Dispy%20HPC-Cluster.md
# Ticket 2018041742001849

 ```markdown
# HPC-Support Ticket: Dispy HPC-Cluster

## Keywords
- Dispy
- Python
- Parallel Computing
- Job Distribution
- SharedJobCluster
- Queuing System

## Problem
The user is trying to parallelize large mathematical problems using the Python package "dispy" on the HPC cluster. The current setup allows only one job per node, but the user wants to run multiple jobs simultaneously on each node with limited CPU usage.

## Root Cause
Dispy's default configuration limits job distribution to one job per node.

## Solution
- **SharedJobCluster**: The HPC Admin suggests using "SharedJobCluster" instead of "JobCluster" to allow multiple processes to share nodes simultaneously.
- **Queuing System**: Alternatively, the HPC Admin suggests leveraging the cluster's queuing system for job distribution, which might eliminate the need for Dispy.

## General Learnings
- **Dispy Configuration**: Understanding the different configurations in Dispy, such as "SharedJobCluster," can help in optimizing job distribution.
- **Queuing System**: Utilizing the cluster's built-in queuing system can sometimes be more efficient for job distribution than external tools.
- **Workflow Details**: Providing detailed workflow information can help in diagnosing and suggesting more accurate solutions.
```
---

### 2024110842001797_Tier3-Access-Fritz%20%22zhicong%20xian%22%20_%2026424C8090AD1337%40lmu.de.md
# Ticket 2024110842001797

 # HPC Support Ticket Analysis

## Keywords
- Tier3 Access
- Fritz
- Single-node throughput
- Multi-node workload
- Python
- Anaconda
- Container-based technology
- Process mining
- Large relational database
- File conversion
- Alex frontend

## Summary
A user requested access to the Fritz cluster for a process mining application on a large relational database, requiring significant computational resources. The HPC Admin denied the request due to the minimal compute time required (3 node hours) and suggested using the Alex frontend for file conversion.

## Root Cause
- User requested high-performance computing resources for a task that could be handled on a less powerful system.

## Solution
- HPC Admin advised the user to perform file conversions on the Alex frontend instead of requesting access to the Fritz cluster.

## Lessons Learned
- Ensure that requests for high-performance computing resources are justified by the complexity and scale of the task.
- For simpler tasks, such as file conversion, consider using less powerful systems or frontends.
- Communicate clearly with users about the appropriate use of HPC resources.
---

### 2024111242000833_Application%20for%20Compute%20Time%20No.%2023705.md
# Ticket 2024111242000833

 # HPC Support Ticket Analysis: Application for Compute Time No. 23705

## Keywords
- GPU resources
- FairShare
- Job optimization
- Test/porting project
- HPC efficiency

## Summary
A PhD student encountered limited access to GPU resources on the Alex cluster, likely due to their basic Tier 3 status. The user prepared an application for a test/porting project but couldn't finalize it due to the PI's unavailability. The HPC Admins provided insights into FairShare reduction and job optimization.

## Root Cause
- **FairShare Reduction**: The user's FairShare was reduced due to a high number of jobs, including failed ones, in October and November.
- **Inefficient Job Submission**: Most jobs finished in under two hours, which is not ideal for HPC.

## Solution
- **Job Optimization**: Combine several short jobs into a single job to make more efficient use of allocated resources.
- **FairShare Awareness**: Be aware that all jobs, including failed ones, count towards FairShare.

## General Learnings
- **FairShare Management**: Understand how FairShare is calculated and its impact on resource allocation.
- **Efficient Job Submission**: Optimize job submission patterns to improve HPC efficiency.
- **Resource Utilization**: Ensure that jobs are utilizing the allocated resources effectively.

## Next Steps
- The user should optimize their job submission patterns to improve resource utilization.
- The HPC Admins will forward the application for further processing.

## Additional Notes
- Test projects are not available for FAU members.
- The user should monitor their FairShare status and adjust job submissions accordingly.

---

This analysis provides a concise overview of the issue, its root cause, and the suggested solutions. It can serve as a reference for support employees dealing with similar issues in the future.
---

### 2023051042001921_new%20nodes%20on%20fritz%20-%20b165da%20-%20UltrafastDyn%20-%20Wilhelm_Uni-Regensburg.md
# Ticket 2023051042001921

 # HPC-Support Ticket Conversation Summary

## Keywords
- New nodes on Fritz cluster
- Large memory nodes
- NHR project
- Projektverlängerung (project extension)
- Ressourcenaufstockung (resource increase)

## General Learnings
- New nodes with large memory (1TB and 2TB) are available on the Fritz cluster.
- These nodes are faster and suitable for memory-intensive jobs.
- Users with NHR projects are eligible to use these nodes.
- Users need to inform HPC support before using the new nodes.
- Project extensions and resource increases can be requested via email to `nhr-applications@fau.de`.

## Problem/Request
- User requested access to new large memory nodes.
- User inquired about extending the project duration and increasing resources due to an extension in the funding period.

## Solution
- HPC Admin granted access to the new nodes without the need for further email confirmation.
- User was informed about the process to request project extension and resource increase. The local steering committee will decide on the request.

## Follow-up
- User will send a formal request for project extension and resource increase a few months before the project end date.

For more information, refer to the [Fritz cluster documentation](https://hpc.fau.de/systems-services/documentation-instructions/clusters/fritz-cluster).
---

### 2016070542001511_Jobs%20too%20long%20in%20queue.md
# Ticket 2016070542001511

 # HPC Support Ticket: Jobs Too Long in Queue

## Keywords
- Job queue delay
- High system load
- Fairshare
- Resource allocation

## Problem
- User experienced unusually long waiting times for jobs in the queue.
- Jobs were not huge, requiring only 8 nodes.
- No apparent issues with quota or account.

## Root Cause
- High system load on Woody.
- Specific group (iww8) had an average share of >10% of the system over the last 10 days.

## Solution
- No immediate action required from the user.
- System is functioning normally but is currently very busy.
- Suggested long-term solution: Invest in more nodes to increase fairshare.

## General Learning
- High system load can cause significant delays in job processing.
- Fairshare allocation can impact job scheduling.
- Users should be aware of system load and consider investing in additional resources if necessary.

## Next Steps for Support
- Monitor system load and notify users of high demand periods.
- Provide options for users to increase their fairshare if needed.
- Ensure users are informed about the current system status and expected delays.
---

### 2018040542001559_OOM%20vorbeugen....md
# Ticket 2018040542001559

 # HPC Support Ticket: Preventing OOM (Out of Memory) Errors

## Keywords
- OOM (Out of Memory)
- SLURM
- `#SBATCH --mem`
- cgroup-plugin
- Memory allocation
- Job configuration

## Problem Description
The user encountered OOM errors while running a large-scale benchmark, causing several nodes to crash. The user inquired about preventing such issues, specifically asking about the effectiveness of using `#SBATCH --mem`.

## Root Cause
- The user's job requested `--mem=51200`, which was interpreted as 51200 MB per node.
- SLURM on the system does not enforce memory limits strictly due to the inactive cgroup-plugin.
- SLURM periodically samples memory usage and terminates jobs exceeding the specified limit, but this often occurs too late to prevent OOM errors.

## Solution
- The `#SBATCH --mem` directive can help set memory limits, but its effectiveness is limited without the cgroup-plugin.
- Ensure that the memory requested per node is correctly specified and understood.
- Monitor job memory usage closely to avoid exceeding allocated limits.

## Lessons Learned
- Properly configure memory requests in SLURM job scripts to avoid OOM errors.
- Understand the limitations of SLURM memory management without the cgroup-plugin.
- Regularly monitor job memory usage to prevent crashes.

## Ticket Status
- The ticket was closed due to inactivity after two months.

## References
- SLURM documentation on memory management.
- Internal HPC documentation on job configuration best practices.
---

### 2023080442001203_High-Memory%20Knoten%20freischalten.md
# Ticket 2023080442001203

 ```markdown
# High-Memory Node Activation

## Keywords
- High-memory nodes
- Slurm
- Freischaltung
- Batch file
- Projekt
- Dokumentation

## Problem
- User requested activation of high-memory nodes for their project.
- User inquired about any specific instructions or peculiarities for requesting these nodes.

## Solution
- HPC Admin activated the high-memory nodes for the user's project.
- User was informed that the nodes can be requested using the Slurm option `-p spr1tb`.
- No special considerations are needed; the nodes are allocated exclusively with full memory.
- General documentation for the Fritz cluster is available at [Fritz Cluster Documentation](https://hpc.fau.de/systems-services/documentation-instructions/clusters/fritz-cluster/).

## General Learnings
- High-memory nodes can be activated upon user request.
- Slurm option `-p spr1tb` is used to request high-memory nodes.
- No additional batch file modifications are required.
- Documentation for the Fritz cluster provides comprehensive information.
```
---

### 2025011642001539_Request%20for%20big%20partition.md
# Ticket 2025011642001539

 # HPC Support Ticket: Request for Big Partition Access

## Keywords
- Big partition
- FRITZ cluster
- Compute nodes
- Access request
- SCALEXA project
- Downtime
- Benchmarks

## Summary
A user requested access to the big partition of the FRITZ cluster to use more than 64 compute nodes. The request was processed by the HPC Admins, who granted access to the big queue for the user's project.

## Root Cause
The user needed access to the big partition to perform large-scale computations requiring more than 64 compute nodes.

## Solution
The HPC Admins granted access to the big queue for the user's project, allowing them to use up to 256 nodes.

## General Learnings
- Users can request access to the big partition for large-scale computations.
- The HPC Admins can grant access to the big queue for specific projects.
- Downtimes can be scheduled to allow exclusive access to the cluster for benchmarking purposes.
- Communication and planning are essential for coordinating large-scale benchmarks and computations.

## Steps Taken
1. User submitted a request for access to the big partition.
2. HPC Admins reviewed the request and granted access to the big queue.
3. The user was notified of the access grant.
4. Additional discussions were held regarding scheduling benchmarks during downtimes.

## Notes
- The SCALEXA project was mentioned in the context of requesting access to the big partition.
- Downtimes were discussed as potential opportunities for exclusive access to the cluster for benchmarking.
- The user was advised to communicate their needs early to facilitate planning.
---

### 42308282_unexplained%20mpirun%20aborts%20%28possible%20cause%3ASymbolic%20links%20in%20emmy%20not%20working%3.md
# Ticket 42308282

 # HPC Support Ticket: Unexplained mpirun Aborts

## Keywords
- mpirun aborts
- symbolic links
- FEniCS
- JIT compiler
- permission denied
- bad interpreter location

## Summary
A user reported issues with jobs failing in the HPC environment, specifically with `mpirun` aborting without clear information. The user suspected that symbolic links might be causing the problem, as they were experiencing permission issues with them.

## Root Cause
The root cause of the problem was identified as a bad interpreter location in FEniCS.

## Solution
The user resolved the issue by correcting the interpreter location in FEniCS.

## Lessons Learned
- **Interpreter Location**: Ensure that the interpreter location is correctly set in applications like FEniCS to avoid runtime errors.
- **Symbolic Links**: While symbolic links were initially suspected, they were not the root cause in this case. However, it's important to verify their functionality and permissions when troubleshooting.
- **mpirun Aborts**: When `mpirun` aborts without clear information, it's crucial to check the application's configuration and dependencies.

## Actions Taken
- The user identified and fixed the bad interpreter location in FEniCS.
- The ticket was closed by the HPC Admin after the user confirmed the resolution.

## Recommendations
- **Documentation**: Update documentation to include common issues with interpreter locations in applications like FEniCS.
- **Troubleshooting Guide**: Include steps to verify symbolic link functionality and permissions in the troubleshooting guide.

## Related Teams
- **HPC Admins**: Thomas, Michael Meier, Anna Kahler, Katrin Nusser, Johannes Veh
- **2nd Level Support**: Lacey, Dane (fo36fizy), Kuckuk, Sebastian (sisekuck), Lange, Florian (ow86apyf), Ernst, Dominik (te42kyfo), Mayr, Martin
- **Datacenter Head**: Gerhard Wellein
- **Training and Support Group Leader**: Georg Hager
- **NHR Rechenzeit Support**: Harald Lanig
- **Software and Tools Developer**: Jan Eitzinger, Gruber
---

### 2022101942002164_Runing%20parallel%20jobs%20on%20multiple%20nodes%20on%20Fritz%20cluster.md
# Ticket 2022101942002164

 # HPC Support Ticket: Running Parallel Jobs on Multiple Nodes on Fritz Cluster

## Keywords
- Multi-node jobs
- Job runtime limit
- Fritz cluster
- Gromacs
- Amber
- Job rejection
- Restart capabilities

## Problem
- User inquires about running multi-node jobs on the Fritz cluster.
- User asks if more than 24 hours can be allocated for a single job.

## Root Cause
- User needs clarification on multi-node job capabilities and runtime limits.

## Solution
- **Multi-node Jobs**: Enabled by default on the Fritz cluster. If jobs are rejected, provide exact details and error messages for further assistance.
- **Runtime Limit**: 24 hours is the limit for all jobs. In exceptional cases, runtime can be manually increased for a few individual jobs.
- **Restart Capabilities**: Gromacs and Amber have sufficient restart capabilities to handle individual 24-hour jobs and successive jobs.

## Additional Information
- **Contact**: For further assistance, contact the HPC support team.
- **Tools**: Gromacs and Amber are mentioned as the tools the user intends to use.

## Conclusion
- Multi-node jobs are supported on the Fritz cluster.
- The default runtime limit is 24 hours, but exceptions can be made upon request.
- Users should utilize the restart capabilities of their software to manage long-running jobs.
---

### 2022012142001954_Early-Fritz%20%22Maximilian%20Schmidt%22%20_%20bcpc000h.md
# Ticket 2022012142001954

 # HPC Support Ticket Conversation Analysis

## Keywords
- **HPC Cluster**: Fritz
- **User Requirements**: Single-node throughput, multi-node workload
- **Software**: Gromacs 2021
- **Application**: Unbiased MD simulation of GPCRs
- **Expected Results**: Faster computation time
- **Partition**: Singlenode
- **Cores**: 72
- **SSH Access**: `ssh bcpc000h@fritz.nhr.fau.de`
- **Documentation**: [Fritz Cluster Documentation](https://hpc.fau.de/systems-services/systems-documentation-instructions/clusters/fritz-cluster/)

## General Learnings
- **Initial Access**: User was granted access to the Fritz cluster with limited resources due to hardware constraints.
- **Partition Limitations**: Due to Infiniband card shortages, the user was initially restricted to the "singlenode" partition.
- **SSH Access**: Provided instructions for SSH access from within the university network or VPN.
- **Documentation**: Informed the user about the ongoing development of the cluster documentation.
- **Multi-node Access**: User was later granted access to multi-node jobs after initial restrictions.

## Root Cause of the Problem
- **Hardware Constraints**: Limited availability of Infiniband cards restricted the user to single-node jobs initially.

## Solution
- **Initial Access**: Granted access to the "singlenode" partition with 72 cores.
- **SSH Instructions**: Provided SSH access details for both internal and external connections.
- **Documentation**: Directed the user to the cluster documentation and MOTD for additional information.
- **Multi-node Access**: Later enabled multi-node job submissions for the user.

## Notes for Support Employees
- **Hardware Limitations**: Be aware of hardware constraints and communicate them clearly to users.
- **Access Grants**: Ensure users are informed about their access levels and any changes made.
- **Documentation**: Keep users updated on the status of documentation and provide alternative sources of information.
- **SSH Access**: Provide clear instructions for both internal and external SSH access.
---

### 2023101942000011_Hilfe%20beim%20Profiling_Benchmarking%20-%20Uhrig.md
# Ticket 2023101942000011

 ```markdown
# HPC-Support Ticket: Profiling/Benchmarking Assistance

## Subject
Hilfe beim Profiling/Benchmarking - Uhrig

## Keywords
Profiling, Benchmarking, Performance Variability, Data Storage, Caching, NUMA, Python, Video Processing

## Problem Description
The user is experiencing performance variability in their application runs on different HPC nodes (Alex and Fritz). The application's performance, particularly the import times, varies significantly between runs with the same options. The user suspects that factors such as /home/atuin usage, caching, and data storage location might be influencing the benchmarks.

## Root Cause
- Performance variability due to data storage location and caching.
- Inefficient code practices, such as writing and reading video files in consecutive functions.

## Steps Taken
1. **Initial Analysis**: The user provided benchmark results showing significant performance differences between runs.
2. **Consultation Offer**: The HPC Admin offered a Zoom meeting to discuss the issue in detail.
3. **Code Review**: The user identified inefficient code practices, such as writing and reading video files in consecutive functions.
4. **Data Storage**: The user planned to move data and libraries/models to the local SSD for further testing.

## Solution
- **Code Optimization**: The user identified and planned to fix inefficient code practices.
- **Data Storage**: The user planned to move data and libraries/models to the local SSD to reduce variability.
- **Consultation**: The user planned to schedule a Zoom meeting with the HPC Admin for further assistance.

## General Learnings
- Performance variability can be influenced by data storage location and caching.
- Inefficient code practices, such as unnecessary file I/O operations, can significantly impact performance.
- Moving data to local SSDs can help reduce performance variability.
- Collaborative consultation via Zoom can be more effective than email exchanges for complex issues.

## Next Steps
- The user will optimize the code and move data to the local SSD.
- The user will schedule a Zoom meeting with the HPC Admin for further assistance.
```
---

### 2023022442000759_HPC-Kursaccounts%20und%20Reservierung%20Fritz%20f%C3%83%C2%BCr%2011.-13.01.23.md
# Ticket 2023022442000759

 ```markdown
# HPC-Support Ticket: HPC-Kursaccounts und Reservierung Fritz für 11.-13.01.23

## Keywords
- HPC-Kursaccounts
- Fritz
- Reservierung
- PPHPS 2023
- LDAP+NIS

## Summary
- **User Request**: 65 HPC-Kursaccounts with access to Fritz for the PPHPS 2023 course, duration from now until 10. März 2023. Additionally, a reservation for 50 Fritz-Knoten on 7., 8., and 9. März from 9:00-17:00.
- **HPC Admin Response**: Freischaltung and Reservierung on Fritz can only be made once the Kennungen are available in LDAP+NIS.

## Root Cause
- The user requires HPC-Kursaccounts and reservations for a specific course, but the process depends on the availability of Kennungen in LDAP+NIS.

## Solution
- Wait for the Kennungen to be available in LDAP+NIS before proceeding with the Freischaltung and Reservierung on Fritz.

## General Learning
- HPC-Kursaccounts and reservations are dependent on the availability of Kennungen in LDAP+NIS.
- Communication with the user should include the dependency on LDAP+NIS for account activation and reservations.
```
---

### 2024082242002435_Request%20for%20multi-node%20permission.md
# Ticket 2024082242002435

 ```markdown
# HPC Support Ticket: Request for Multi-Node Permission

## Keywords
- Multi-node permission
- Large-scale simulations
- Account enablement
- Alex cluster

## Summary
A user requested permission to submit multi-node jobs for large-scale simulations on the Alex cluster.

## User Request
- **Subject:** Request for multi-node permission
- **Description:** The user needs to run large-scale simulations and requires multi-node permission for their account.

## HPC Admin Response
- **Action Taken:** The user's account was enabled to run multi-node jobs on the Alex cluster.
- **Outcome:** The request was successfully processed, and the user's account was granted the necessary permissions.

## General Learnings
- Users may need multi-node permissions for large-scale simulations.
- HPC Admins can enable multi-node job submission for user accounts upon request.
- Automated replies may indicate user unavailability, but the request can still be processed by HPC Admins.

## Solution
- **Root Cause:** User required multi-node permissions for large-scale simulations.
- **Solution:** HPC Admin enabled multi-node job submission for the user's account.
```
---

### 2019120442001794_Jobs%20auf%20emmy.md
# Ticket 2019120442001794

 # HPC Support Ticket Conversation Summary

## Keywords
- Job allocation
- Memoryhog
- Emmy
- Parallel computing
- Bash script
- Screen
- StarCCM
- FLOP/s
- Hyperthreads
- TinyFAT
- qsub
- PPN

## General Learnings
- **Job Allocation**: Ensure that the number of allocated nodes is appropriate for the job's requirements. Over-allocation can lead to inefficiency.
- **Memoryhog**: Use it for jobs that require high memory but ensure not to overload the system with too many processes.
- **Parallel Computing**: Monitor jobs to ensure they are utilizing resources efficiently. Adjust the number of nodes and processes per node (PPN) as needed.
- **Bash Script**: Automate job submission and management using scripts. Use tools like `screen` to keep jobs running in the background.
- **StarCCM**: Adjust the number of cores and avoid using hyperthreads for better performance.
- **TinyFAT**: Consider using TinyFAT for jobs that require a batch system similar to Emmy.

## Root Cause of Problems
- **Inefficient Job Allocation**: Users were allocating too many nodes for their jobs, leading to underutilization of resources.
- **Overloading Memoryhog**: Running too many processes simultaneously on Memoryhog, causing system slowdown.
- **Lack of Automation**: Users needed a way to automate job submission and management, especially for sequential tasks.

## Solutions
- **Reduce Node Allocation**: Test jobs with fewer nodes to ensure efficient resource utilization.
- **Limit Processes on Memoryhog**: Run one process at a time to avoid overloading the system.
- **Use Screen**: Implement `screen` to keep jobs running in the background and log output to a file.
- **Adjust PPN**: Set PPN to 16 for TinyFAT jobs and avoid using hyperthreads for StarCCM.
- **Automate with Bash Scripts**: Develop scripts to automate job submission and management, especially for sequential tasks.

## Specific Actions
- **HPC Admin**: Provided detailed instructions on how to adjust job scripts, use `screen`, and monitor job performance.
- **User**: Agreed to test jobs with fewer nodes, automate job submission, and adjust PPN settings.

## Additional Notes
- **Job Monitoring**: Users can access monitoring data for their jobs to analyze performance and make adjustments.
- **Documentation**: Refer to the provided links for detailed instructions on using TinyFAT and other resources.

This summary provides a concise overview of the key points discussed in the HPC support ticket conversation, focusing on the root causes of problems and the solutions provided.
---

### 2018101642002311_memory%20bandwidth%20and%20flops%20on%20emmy%20via%20likwid.md
# Ticket 2018101642002311

 # HPC-Support Ticket Conversation Summary

## Subject: Memory Bandwidth and FLOPS on Emmy via LIKWID

### Keywords:
- Memory Bandwidth
- FLOPS
- Roofline Model
- LIKWID
- Operational Intensity
- Emmy Cluster

### What Can Be Learned:
- The Emmy cluster has a memory bandwidth of 50 GB/s and peak performance of 176 Gflop/s.
- To measure memory bandwidth and FLOPS for the Roofline model, use the `MEM_DP` and `MEM_SP` groups in LIKWID.
- The `Operational intensity` metric in LIKWID may not be accurate; manual calculation is recommended.
- LIKWID version 4.3.x has issues with measuring memory bandwidth due to an uncore bug.
- Maximum attainable memory bandwidth can be measured using `likwid-bench` with the `load_avx` test.

### Problem:
- User was unable to accurately measure memory bandwidth and operational intensity using LIKWID for the Roofline model.
- LIKWID versions had inconsistencies in measuring memory bandwidth and operational intensity.

### Solution:
- Use `MEM_DP` and `MEM_SP` groups in LIKWID to measure memory bandwidth and FLOPS.
- Manually calculate operational intensity as `MFLOP/s / Memory bandwidth [MBytes/s]`.
- Use `likwid-bench -t load_avx -w S0:1GB:10:1:2` to measure maximum attainable memory bandwidth.
- A bug in LIKWID 4.3.x causing zero memory bandwidth measurements was identified and will be fixed in a future release.

### Additional Notes:
- The attainable memory bandwidth on Emmy depends on the load/store ratio, with read-only operations achieving the highest bandwidth.
- Cite LIKWID and the specific benchmark used when reporting measurements.

### References:
- LIKWID GitHub page
- Emmy cluster specifications from RRZE papers

This summary provides a concise overview of the key points discussed in the support ticket conversation, focusing on the use of LIKWID for measuring performance metrics on the Emmy cluster.
---

### 2025012142002162_Probleme%20mit%20gro%C3%9Fer%20Knoten-Anzahl%20auf%20Fritz.md
# Ticket 2025012142002162

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject: Probleme mit großer Knoten-Anzahl auf Fritz

### Keywords:
- Large MPI jobs
- Job hangs
- MPI_Init
- Slurm
- Node failure
- Rechenzeit gutschrift

### Summary:
The user encountered issues with large MPI jobs (256, 384, and 512 nodes) hanging during startup, specifically during MPI_Init. The problem was identified as a failing node in the cluster.

### Problem:
- Large MPI jobs (256, 384, and 512 nodes) were hanging during startup.
- Jobs showed "Total RAM usage: 0.0 GiB" in Slurm job summary.
- Minimal test program also hung with 512 nodes but ran successfully with 256 nodes.

### Observations:
- Most 256-node jobs ran successfully.
- About half of the 384-node jobs ran successfully.
- Only one out of a dozen 512-node jobs ran successfully.

### Root Cause:
- A failing node in the cluster was causing the jobs to hang.

### Solution:
- The failing node was identified and rebooted.
- The user was advised to remove "source ~/.bashrc" from their Slurm script as it was causing incomplete output in the log file.

### Additional Actions:
- The user requested a refund of the lost compute time (167K Core-h) due to the hanging jobs.
- The HPC Admin granted a refund of 295K Core-h to the project.
- The user was informed about the possibility of a one-time budget increase of 25% by submitting a brief justification.

### Notes:
- The user compiled their code with `mpicxx -O2 mpitest.cpp -o mpitest` using modules `cmake/3.23.1`, `gcc/11.2.0`, and `openmpi/4.1.2-gcc11.2.0`.
- The HPC Admin reproduced the issue and identified the failing node.
- The user was advised to remove "source ~/.bashrc" from their Slurm script to ensure complete output in the log file.

### Conclusion:
The issue was resolved by identifying and rebooting the failing node. The user was compensated for the lost compute time, and additional steps were taken to ensure proper logging in the Slurm script.
```
---

### 2019120542001185_Anzahl%20MPI%20Prozesse%20auf%20woody.md
# Ticket 2019120542001185

 ```markdown
# HPC Support Ticket: Anzahl MPI Prozesse auf woody

## Keywords
- MPI Prozesse
- Performance
- Rechenzeit
- Hyperthreading
- CPUs

## Summary
A user was running a job on the `woody` cluster using 16 MPI processes, but the nodes only have 4 physical CPUs without hyperthreading. The HPC Admin advised that using more MPI processes than available CPUs might not improve performance and could even negatively impact it.

## Root Cause
- The user was unaware of the optimal number of MPI processes for the `woody` nodes.

## Solution
- The HPC Admin recommended reducing the number of MPI processes to match the number of physical CPUs (4 in this case).
- The user adjusted their script accordingly and observed similar performance with fewer processes.

## Lessons Learned
- It is important to match the number of MPI processes to the number of physical CPUs available on the compute nodes to optimize performance and avoid potential negative impacts on computation time.
- Users should be aware of the hardware specifications of the clusters they are using to ensure efficient resource utilization.
```
---

### 2022112942003713_Fehlermeldung%20HPC.md
# Ticket 2022112942003713

 ```markdown
# HPC Support Ticket: Fehlermeldung HPC

## Keywords
- LAMMPS
- MPI
- Segmentation Fault
- PSM2 Connect Error
- OpenMPI
- SLURM
- Environment Variables

## Summary
The user encountered segmentation faults and PSM2 connect errors when scaling up the number of cores for a LAMMPS simulation. The issue was initially thought to be related to environment variables and MPI settings but was later identified as a user error in launching too many processes.

## Root Cause
- The user mistakenly launched MPI with double the number of processes than allocated, leading to resource contention and errors.

## Solution
- The user realized the error and corrected the number of processes to match the allocated resources.

## Lessons Learned
- Ensure that the number of MPI processes matches the allocated resources.
- Understand the impact of environment variables and MPI settings on job execution.
- Properly configure SLURM and MPI settings to avoid resource contention and connectivity issues.

## Actions Taken
- The user corrected the number of MPI processes.
- The ticket was closed as the user resolved the issue independently.
```
---

### 2023011142003086_Jobs%20on%20Fritz%20%28iww2003h%29.md
# Ticket 2023011142003086

 # HPC Support Ticket: Jobs on Fritz (iww2003h)

## Keywords
- Fritz
- Meggie
- Floating point operations
- Conditional expressions
- Cellular automaton method
- Memory bandwidth
- Resource utilization
- Job scheduling
- $FASTTMP

## Summary
- **User Issue**: User's jobs on Fritz perform few floating point operations but have many conditional expressions. The user needs to use a multinode system to minimize simulation time.
- **HPC Admin Concerns**: Inefficient resource utilization, as jobs do not fully utilize memory bandwidth and allocate only a fraction of available memory per node.
- **Root Cause**: User's application is based on the cellular automaton method, which is not computationally intensive in terms of floating point operations but relies heavily on conditionals and loops.
- **Solution**: HPC Admin suggests reducing the number of nodes per job to improve resource utilization and scheduling. User agrees to try to improve their utilization on Fritz.

## Details
- User's application performs few floating point operations but has many conditional expressions.
- Jobs do not fully utilize memory bandwidth and allocate only around 20 GB of memory per node, despite each node having 256 GB.
- User's jobs are sequential, with each job depending on the previous one.
- HPC Admin suggests that a single node per job would be sufficient and more efficient.
- User agrees to try to improve resource utilization.

## Follow-up
- User reduces the number of nodes for running SAMPLE3D from 7 to 3 based on HPC Admin's suggestion.

## General Learning
- Always analyze job requirements to ensure efficient resource utilization.
- Communicate with users to understand their application's needs and provide appropriate suggestions for optimization.
- Monitor job performance to identify potential inefficiencies and address them proactively.
---

### 2023082342002024_Tier3-Access-Fritz%20%22Mamta%20K%20C%22%20_%20gwgi018h.md
# Ticket 2023082342002024

 # HPC Support Ticket Analysis

## Keywords
- Queue waiting times
- Woody nodes
- Fritz nodes
- Single-node throughput
- Node hours
- Processor generation
- Clock frequency
- RAM
- Cores
- Software: pip, firedrake, python, conda, spack
- Application: Numerical glacier flow modeling
- Expected results: netcdf files, pgns

## Summary
- **Issue**: Long waiting times in the queue for Fritz nodes despite low usage.
- **User Request**: Single-node throughput with 5000 node hours on Fritz.
- **Software Needed**: pip, firedrake, python, conda, spack.
- **Application**: Numerical glacier flow modeling using icepack and Elmer ice physical models.
- **Expected Results**: netcdf files, pgns.

## Root Cause
- High demand for Fritz nodes leading to long queue times.

## Solution
- **HPC Admin Suggestion**: Use Woody nodes as an alternative. Woody nodes have similar RAM (250 GB) and higher clock frequency cores, although fewer cores (32) compared to Fritz nodes (72).
- **User Response**: Agreed to use Woody nodes for now.

## General Learnings
- **Queue Management**: Monitor queue times and suggest alternative resources when possible.
- **Resource Utilization**: Understand the specific needs of users to recommend appropriate resources.
- **Communication**: Clearly communicate the benefits and limitations of alternative resources to users.

## Action Taken
- HPC Admin suggested using Woody nodes due to shorter queue times and similar capabilities.
- User agreed to use Woody nodes.

## Future Reference
- When encountering long queue times for Fritz nodes, consider suggesting Woody nodes if the user's requirements can be met.
- Ensure users are aware of the capabilities and limitations of different node types to make informed decisions.
---

### 2015120842000704_Probleme%20mit%20mpirun_rrze.md
# Ticket 2015120842000704

 # HPC Support Ticket Analysis: Probleme mit mpirun_rrze

## Keywords
- mpirun_rrze
- MPI jobs
- Signal 9
- Signal 11
- Job failure
- Input files
- PBS script
- VASP

## Problem Description
- User reported issues with starting MPI jobs, which were previously running without problems.
- Jobs were terminated with signals 9 or 11 on Emmy and Lima.
- Not all available cores were used due to memory and performance reasons.

## Example Script
```bash
#!/bin/bash -l
# allocate 20 nodes for 24 hours
#PBS -l nodes=20:ppn=40,walltime=24:00:00
# job name
#PBS -N VcVsi.ch.c0.Gkp.hex576.g-e2.geom-0.5
# stdout and stderr files
#PBS -o /elxfs/mptf/mptf07/log/VcVsi.ch.c0.Gkp.hex576.g0.out
#PBS -e /elxfs/mptf/mptf07/log/VcVsi.ch.c0.Gkp.hex576.g0.err

export jobname=VcVsi.ch.c0.Gkp.hex576.g-e2.geom-0.5
export root=/elxfs/mptf/mptf07/${jobname}
export jobdir=${root}
export scratchdir=/elxfs/mptf/mptf07/${jobname}
export version=2-ns-band

cd ${scratchdir}
export outputfile=${jobdir}/${jobname}.${version}.log

export PPN=10
export NODES=`uniq $PBS_NODEFILE | wc -l`
export I_MPI_PIN=enable
module load intel64/15.0up01
mpirun_rrze -intelmpi -npernode $PPN ./vasp-533G >& ${outputfile}
```

## HPC Admin Response
- No system changes were made on Emmy or Lima.
- Not all jobs were affected; some ran successfully.
- Suggested checking input files as a potential cause.

## Outcome
- User acknowledged the information but the root cause was not identified.
- Ticket closed with user satisfaction despite no resolution.

## Lessons Learned
- Verify system changes or updates before assuming user-side issues.
- Input files can be a common cause of job failures.
- Ensure thorough investigation of job scripts and configurations.
- Document successful and unsuccessful job runs for future reference.

## Potential Solutions
- Review input files for any changes or errors.
- Check for any recent updates or changes in the system environment.
- Validate job scripts and configurations for consistency.
- Monitor job performance and resource usage for anomalies.
---

### 2022062242003218_Jobs%20on%20Meggie%20use%20only%20one%20node%20%5Bgwgk005h%5D.md
# Ticket 2022062242003218

 ```markdown
# HPC Support Ticket: Jobs on Meggie use only one node

## Keywords
- Job allocation
- Serial jobs
- Parallel jobs
- Node utilization
- Job script
- srun
- jobber
- netcdf library
- Meggie
- woody-ng

## Problem
- User's jobs on Meggie were using only one node out of the allocated four nodes.
- The user's model was running in serial mode, which can only utilize one node.

## Root Cause
- The user incorrectly allocated four nodes for a serial job, leading to inefficient resource utilization.

## Solution
- The user was advised to modify the job script to request only one node for serial jobs.
- For parallel jobs, the user was advised to add `srun` to the job script to distribute tasks across all allocated nodes.
- The user was provided with options to move jobs to woody-ng, where it is possible to allocate one core per job, or to use jobber to fully utilize the 20 cores on Meggie.
- The user was assisted in setting up the netcdf library on woody-ng for their model.

## General Learnings
- Always ensure that the job script correctly reflects the resource requirements of the job.
- Use `srun` for parallel jobs to distribute tasks across multiple nodes.
- Consider moving serial jobs to systems that allow single-core allocation to optimize resource usage.
- Utilize tools like jobber to maximize core utilization for serial jobs.
- Communicate with HPC support for assistance with library installations and job script modifications.
```
---

### 2023101642002079_Dummyaccount%20%2B%20Reservierung%20f0401%20f%C3%83%C2%BCr%20CLPE%20Tutorial%20am%2021.10..md
# Ticket 2023101642002079

 ```markdown
# HPC Support Ticket: Dummy Account and Node Reservation for Tutorial

## Keywords
- Dummy account
- Node reservation
- Tutorial
- Reactivation
- Reservation creation

## Problem
- User requested a dummy account and node reservation for a tutorial, similar to a previous setup.

## Root Cause
- The previous account had expired and needed to be reactivated.

## Solution
- HPC Admin reactivated the previous account.
- HPC Admin created a reservation for the specified node and time period.

## Actions Taken
- Reactivated the dummy account from the previous week.
- Created a reservation using the following command:
  ```bash
  scontrol create reservation reservationname=CLPE-Tutorial starttime=2023-10-20T08:00 endtime=2023-10-23T20:00 account=k_y68v nodes=f0401 flags=IGNORE_JOBS,magnetic
  ```

## Notes
- The reactivation of the account may take a few hours to propagate across the cluster.
- The reservation was created successfully for the specified time and node.
```
---

### 2025031042001895_Reservierung%20auf%20fritz%20f%C3%83%C2%BCr%20ihpc119h.md
# Ticket 2025031042001895

 ```markdown
# HPC Support Ticket: Reservierung auf fritz für ihpc119h

## Keywords
- Reservation
- Fritz-Knoten
- Leaf-Switch
- Masterarbeiterin
- scontrol
- magnetic
- partition
- multinode

## Summary
A user requested a reservation of 5 Fritz-Knoten for a specific user (ihpc119h) on a particular date and time. The user also requested that all nodes be on the same Leaf-Switch.

## User Request
- **Nodes Requested:** 5 Fritz-Knoten
- **User:** ihpc119h
- **Date and Time:** Mi, 12.03. 12:00-24:00
- **Additional Requirement:** All nodes on the same Leaf-Switch

## HPC Admin Response
- **Action Taken:** Reservation created
- **Command Used:** `scontrol create reservation reservationname=ihpc user=ihpc119h starttime=2025-03-12T12:00 endtime=2025-03-13T00:00 flags=magnetic partition=multinode Nodes=f[0101-0105]`
- **Nodes Assigned:** f[0101-0105]

## What Can Be Learned
- **Reservation Process:** Understanding how to create a reservation using `scontrol` command.
- **Node Allocation:** Ensuring nodes are allocated on the same Leaf-Switch as per user request.
- **Communication:** Importance of clear communication between users and HPC Admins for specific requirements.

## Root Cause of the Problem
- **User Request:** Need for specific node allocation and time reservation.

## Solution
- **Reservation Created:** HPC Admin successfully created the reservation with the specified nodes and time.
```
---

### 2020052742002448_Zahl%20der%20MPI-Prozesse%20-%20bcpc000h.md
# Ticket 2020052742002448

 # HPC Support Ticket: Zahl der MPI-Prozesse - bcpc000h

## Keywords
- MPI-Prozesse
- SLURM
- Jobscript
- Gromacs
- Skalierungs-/Performancetests

## Problem
- Inconsistency between the number of explicitly started MPI processes and the number of nodes in the job script.
- User's job scripts had `#SBATCH --nodes=20` but `mpirun -ppn 18 -np $((32*18)) mdrun_mpi`.

## Root Cause
- The user did not dynamically adjust the number of MPI processes based on the number of nodes allocated by SLURM.

## Solution
- Replace the hardcoded number of nodes with the SLURM environment variable `$SLURM_NNODES`.
- Example: `mpirun -ppn 18 -np $((SLURM_NNODES*18)) mdrun_mpi`.

## Additional Information
- Gromacs typically scales with the number of cores, and using all cores (20) per node is usually efficient.
- For specific inputs, manual adjustment of PME processes or using fewer cores per node might be beneficial.
- Conducting scaling/performance tests at the beginning of a project can help optimize the configuration.
- Support from the 2nd Level Support team (Anna, Tobias) is available for performance testing.

## General Learning
- Always ensure that the number of MPI processes matches the number of nodes allocated by SLURM.
- Use SLURM environment variables to dynamically adjust job parameters.
- Perform scaling/performance tests to optimize resource usage for specific applications and inputs.
---

### 2023083142002401_access%20to%20VASP%206%20-%20a102cb10.md
# Ticket 2023083142002401

 ```markdown
# HPC Support Ticket: Access to VASP 6

## Keywords
- VASP 6
- MPI+OpenMP
- Performance optimization
- LREAL parameter
- OMP_STACKSIZE

## Summary
- **User Issue**: User was using VASP 5 and wanted to try VASP 6 for improved performance with hybrid MPI+OpenMP.
- **HPC Admin Recommendation**: Use VASP 6 with hybrid MPI+OpenMP for better performance. Set `export OMP_STACKSIZE=500m` to prevent crashing.
- **User Testing**: User performed tests with different MPI and OpenMP configurations. MPI-only configuration gave the best speed.
- **HPC Admin Analysis**: Simplified user runs to isolate performance issues. Recommended using `LREAL=Auto` for better efficiency.

## Detailed Information
- **Initial Recommendation**: HPC Admin suggested using VASP 6 with hybrid MPI+OpenMP for improved performance. They also recommended setting `export OMP_STACKSIZE=500m` to prevent crashing.
- **User Testing**: User performed several tests with different MPI and OpenMP configurations. They found that MPI-only configuration gave the best speed for their system (SiO2 with about 200 atoms).
- **HPC Admin Analysis**: HPC Admin simplified the user runs to isolate performance issues. They recommended using `LREAL=Auto` for better efficiency and provided detailed run times for different configurations.
- **User Feedback**: User confirmed that `LREAL=Auto` provided a large speed-up for less accurate calculations. For high accuracy calculations, they continued to use `LREAL=False` with MPI-only parallelization.

## Solution
- For high accuracy calculations, use `LREAL=False` with MPI-only parallelization.
- For less accurate calculations, use `LREAL=Auto` for better performance.
- Set `export OMP_STACKSIZE=500m` when using hybrid MPI+OpenMP to prevent crashing.

## Conclusion
- The user successfully optimized their VASP calculations based on the HPC Admin's recommendations.
- The ticket was closed after the user confirmed the improvements.
```
---

### 2025011742001993_Tier3-Access-Fritz%20%22Simon%20Weinm%C3%BCller%22%20_%20mfdk100h.md
# Ticket 2025011742001993

 ```markdown
# HPC Support Ticket Analysis

## Keywords
- Single-node throughput
- Special justification
- 72 cores
- 250 GB
- 3000 node hours
- Pytorch
- Conda
- KONWIHR Project
- MR sequences optimization
- High memory consumption
- Clinic relevant resolutions
- University Hospital Erlangen
- Institute of Neuroradiology

## Summary
- **User Request:** Access to HPC resources for a project involving MR sequence optimization.
- **Requirements:** Single-node throughput with 72 cores and 250 GB memory, 3000 node hours.
- **Software:** Pytorch, Conda.
- **Project Details:** KONWIHR Project for developing a Fourier Domain Bloch Simulator.
- **Expected Outcome:** Improvement of MR sequences for better clinic scans.

## Root Cause of the Problem
- User required special justification for single-node throughput with high memory and core requirements.

## Solution
- HPC Admin granted access to the user's account for the requested resources after reviewing the justification.

## Lessons Learned
- Proper justification is crucial for obtaining high-resource allocations.
- HPC Admins review and approve requests based on provided details and project needs.
- Communication between users and HPC Admins is key for resolving resource allocation requests.
```
---

### 42117150_user%3A%20hpck023%2C%20system%3A%20woody%2C%20qsub.tinycpu%20-q%20fermi.md
# Ticket 42117150

 ```markdown
# HPC Support Ticket Analysis

## Subject
- **User:** hpck023
- **System:** woody
- **Command:** qsub.tinycpu -q fermi

## Keywords
- OpenCL
- MuCoSim-Seminar
- tg010 node
- Access issue
- Queue status

## Problem
- User requires access to node `tg010` for testing OpenCL implementation.
- User is unable to access the node.
- User inquires if the node is occupied for an extended period.

## Solution
- **HPC Admin Response:**
  - User can check the queue status on the RRZE website.
  - Password for accessing the queue status can be obtained using the `docpw` command on woody.
  - At the time of response, node `tg010` was reported as free.

## General Learnings
- Users can check node availability via the RRZE website.
- The `docpw` command provides the necessary password for accessing the queue status.
- HPC Admins can verify node status and provide updates to users.
```
---

### 2022043042000012_Early-Fritz%20%22Andreas%20Renz%22%20_%20iwpa053h.md
# Ticket 2022043042000012

 # HPC Support Ticket Conversation Summary

## Keywords
- Fritz Cluster
- STAR CCM+
- Multi-node workload
- Scaling tests
- Monitoring system
- Software installation

## General Learnings
- **Account Activation**: HPC Admins activate user accounts for specific clusters.
- **Documentation**: Users are directed to cluster-specific documentation for setup and usage.
- **Software Modules**: Software like STAR CCM+ is available as modules.
- **Scaling Tests**: Users are advised to perform scaling tests to find the optimal number of nodes.
- **Monitoring**: A new monitoring system is available for checking job resource usage.
- **Software Requests**: Users can request specific software versions if not already available.

## Problem
- User needs access to the Fritz cluster for multi-node workload.
- User requires STAR CCM+ software, specifically the 2022.1-r8 version.
- User needs to understand the equivalent node capacity between Fritz and Meggie clusters.

## Solution
- **Account Activation**: HPC Admin activated the user's account for the Fritz cluster.
- **Documentation**: User was provided with the link to the Fritz cluster documentation.
- **Software Availability**: Confirmed that STAR CCM+ 2022.1-r8 is already available on Fritz.
- **Node Equivalence**: Informed that one Fritz node is approximately equivalent to three Meggie nodes.
- **Scaling Tests**: Advised the user to perform scaling tests to determine the optimal number of nodes.
- **Monitoring**: Directed the user to the new monitoring system for checking job resource usage.

## Additional Notes
- **Partition Information**: Users can use the "multinode" partition for 1-32 nodes and the "singlenode" partition for a single node.
- **Immediate Job Availability**: No specific development jobs that start immediately were mentioned, but users can check for free nodes in the multinode partition.

This summary provides a concise overview of the support ticket conversation, highlighting key actions and information for future reference.
---

### 2024041142000545_Tier3-Access-Fritz%20%22Philip%20Maier%22%20_%20bccc117h.md
# Ticket 2024041142000545

 ```markdown
# HPC Support Ticket Conversation Analysis

## Keywords
- Account activation
- Fritz access
- Single-node throughput
- Multi-node workload
- LAMMPS
- Interaction analyses
- Binding behavior

## Summary
- **User Request:** Access to Fritz for single-node and multi-node workloads.
- **Resources Requested:**
  - Single-node: 72 cores, 250 GB
  - Multi-node: HDR100 Infiniband with 1:4 blocking; per node: 72 cores, 250 GB
- **Software Needed:** LAMMPS (user can compile)
- **Application:** Interaction analyses between SAMs and pesticide molecules at metallic nanoparticles
- **Expected Results:** Differences in binding behavior

## Actions Taken
- **HPC Admin:** Activated the user's account for Fritz.

## Lessons Learned
- **Account Activation Process:** Ensure that user accounts are activated promptly upon request.
- **Resource Allocation:** Understand the specific resource requirements for both single-node and multi-node workloads.
- **Software Support:** Be prepared to support users who can compile their own software, such as LAMMPS.
- **Application Specifics:** Familiarize with the types of analyses users perform, such as interaction analyses, to better support their needs.

## Root Cause of the Problem
- User needed access to Fritz for specific computational resources and software.

## Solution
- HPC Admin activated the user's account for Fritz, addressing the user's request for access.
```
---

### 2022101142004801_Tier3-Access-Fritz%20%22Leon%20Sch%C3%83%C2%B6ps%22%20_%20iwpa069h.md
# Ticket 2022101142004801

 # HPC Support Ticket Analysis: Tier3-Access-Fritz

## Keywords
- Tier3 Access
- Fritz
- Node Hours
- Core Hours
- NHR Project
- Star-CCM+
- Optimization Studies
- Aeroacoustic Properties

## Summary
A user requested access to the Fritz HPC system for a multi-node workload, initially requesting 150,000 node hours. The HPC Admin pointed out that this exceeded the free Tier3 allocation and suggested applying for an NHR project. The user corrected the request to 6,936 node hours, which was still above the Tier3 limit. The HPC Admin advised the user to discuss with a colleague about being added to an existing NHR project.

## Root Cause
- User error in initial request (excessive node hours)
- Request still exceeded Tier3 allocation even after correction

## Solution
- User advised to discuss with a colleague about being added to an existing NHR project
- User's account was activated on Fritz, but with a warning about increased waiting times

## General Learnings
- Understanding the limits of Tier3 allocations
- The process for requesting access to NHR projects
- The importance of accurate requests to avoid delays
- The impact of high computational demands on waiting times for HPC resources
---

### 2023062042003694_22-core%20jobs%20on%20Fritz%20-%20a102cb12.md
# Ticket 2023062042003694

 # HPC Support Ticket: 22-core Jobs on Fritz

## Keywords
- Job optimization
- Resource allocation
- LAMMPS program
- Integration grid
- Exclusive node allocation

## Summary
A user was running jobs on 22 cores per node on the Fritz cluster, despite the nodes being allocated exclusively with 72 cores each. This led to significant resource wastage.

## Root Cause
- Inaccurate estimation of computing time needed for jobs using the LAMMPS program.
- Underestimation of the repetition required for the job to obtain the desired trajectory.

## Impact
- Inefficient use of allocated resources.
- Potential backlog due to a large number of jobs (over 600) in the queue.

## Solution
- Cancel existing jobs.
- Optimize jobs to use all 72 cores by changing the integration grid from 22 to 72.
- Consult with the professor to confirm the changes.

## Follow-up
- HPC Admins to monitor job submissions to ensure efficient resource utilization.
- Users should be encouraged to accurately estimate and optimize their job requirements.

## Lessons Learned
- Importance of accurate job estimation and optimization.
- Underutilization of resources can lead to significant wastage and inefficiency.
- Regular monitoring and communication with users can help prevent such issues.
---

### 2020042842000691_high%20load%20of%20jobs%20on%20Woody%20-%20iwsp011h.md
# Ticket 2020042842000691

 # HPC Support Ticket: High Load of Jobs on Woody

## Keywords
- High load
- Oversubscription
- Job monitoring
- PBS Job arrays
- Resource usage

## Summary
A user's jobs on Woody were causing high load due to oversubscription. The nodes have 4 cores, but the jobs had a constant load of 60-64. The HPC Admin reached out to the user to check if this oversubscription was impacting the jobs.

## Root Cause
- The user's jobs were massively oversubscribed, with a load of 60-64 on nodes that only have 4 cores.

## Solution
- The user was advised to log into the job's node using `ssh` and check the load with `top`. The nodenames could be obtained using `qstat -rnt1`.
- The user was asked to compare the resource usage (number of compute nodes * elapsed wallclock time) before and after the change to determine if the oversubscription was beneficial or not.

## General Learnings
- Oversubscription can potentially slow down jobs.
- It's important to monitor job performance and resource usage to optimize job submission strategies.
- PBS Job arrays can be used for distributing independent simulations, but their efficiency should be evaluated.

## Follow-up
- The user was invited to discuss better ideas for their event-driven simulations at the HPC cafe.
- The user was asked to report if the usage of PBS job arrays causes any problems.
---

### 2019080642000629_Jobs%20on%20Emmy%20with%20memory%20leak%20_%20mptf008h.md
# Ticket 2019080642000629

 # HPC Support Ticket: Jobs with Memory Leak

## Keywords
- Memory leak
- Job failure
- Out-of-memory
- Compute nodes
- Manual recovery

## Summary
Multiple jobs on the Emmy cluster experienced memory leaks, leading to out-of-memory errors and requiring manual intervention to recover the compute nodes.

## Root Cause
- The user's jobs had a memory leak, causing them to consume excessive memory over time.

## Impact
- Jobs running long enough caused compute nodes to crash due to out-of-memory errors.
- Manual actions were required to recover and bring the nodes back online.

## Actions Taken
- The user was notified about the memory leak issue and provided with links to specific job details.
- The user acknowledged the problem and put all jobs on hold to prevent further issues.
- The user committed to fixing the memory leak.

## Resolution
- The ticket was closed after the user's recent jobs showed no signs of memory leaks.

## Lessons Learned
- Regularly monitor job memory usage to detect and address memory leaks early.
- Communicate with users promptly to resolve issues that affect system stability.
- Users should be aware of the impact of memory leaks and take proactive measures to fix them.

## References
- Job details can be found at the provided links (example format: `https://www.hpc.rrze.fau.de/HPC-Status/job-info.php?USER=mptf008h&JOBID=1153856&ACCESSKEY=fba7e57a&SYSTEM=EMMY`).
---

### 2017101242002472_Severe%20problems%20with%20jobs%20on%20Emmy%20_%20mptf005h.md
# Ticket 2017101242002472

 ```markdown
# HPC-Support Ticket: Severe problems with jobs on Emmy / mptf005h

## Summary
User's jobs caused severe issues on Emmy due to excessive I/O operations and load imbalance.

## Root Cause
- **Excessive I/O Operations**: Jobs were hammering the parallel file system with >70k write requests per second due to tiny ASCII I/O.
- **Load Imbalance**: All work was done by the first compute node only.

## Solution
- **I/O Optimization**: User was advised to reduce the number of write operations, especially during the initial phase of the job.
- **Load Balancing**: User was instructed to properly distribute the workload across multiple nodes and threads.

## Key Learnings
- **File System Limitations**: Parallel file systems are not designed for high-frequency, small I/O operations.
- **Resource Allocation**: Properly distributing workload across available resources is crucial for efficient job execution.
- **MPI/OpenMP Configuration**: Starting hybrid MPI/OpenMP codes can be tricky and requires proper configuration to ensure all nodes and threads are utilized.

## Actions Taken
- **Initial Contact**: HPC Admin informed the user about the issues and requested to stop submitting similar jobs.
- **Follow-up**: User was provided with specific instructions on how to configure MPI/OpenMP jobs to ensure proper resource allocation.
- **Monitoring**: HPC Admin monitored the user's jobs to ensure the issues were resolved.
- **Ticket Closure**: After multiple attempts and user confirmation, the ticket was closed.

## Keywords
- I/O Optimization
- Load Balancing
- MPI/OpenMP Configuration
- Resource Allocation
- Parallel File System
- Job Monitoring
```
---

### 2024112642000996_Tier3-Access-Fritz%20%22Leonie%20Rumi%22%20_%20iwia122h.md
# Ticket 2024112642000996

 # HPC Support Ticket Analysis

## Keywords
- Multi-node workload
- HDR100 Infiniband
- 1:4 blocking
- 72 cores
- 250 GB
- ExPDESG
- Node hours
- Account enablement

## Summary
- **User Request:**
  - Multi-node workload with specific requirements (HDR100 Infiniband with 1:4 blocking, 72 cores, 250 GB per node).
  - Required software: ExPDESG.
  - Application: Development and analysis of ExPDESG.
  - Expected results: Practical experience and development of ExPDESG.
  - Requested compute time: 10 node hours on Fritz.

- **HPC Admin Response:**
  - Account enabled for the user on Fritz.

## Root Cause of the Problem
- User needed access to HPC resources for a specific multi-node workload and software.

## Solution
- HPC Admin enabled the user's account on Fritz.

## General Learnings
- Properly documenting user requests and admin responses is crucial for tracking and resolving issues.
- Ensuring that user accounts are enabled promptly helps in facilitating research and development activities.
- Understanding the specific requirements of multi-node workloads is essential for effective support.

## Next Steps
- Monitor the user's activity to ensure smooth operation.
- Provide additional support if needed for the development and analysis of ExPDESG.
---

### 2025031842002889_Reservation%20of%20Fritz%20nodes%20for%20power%20capping%20experiments.md
# Ticket 2025031842002889

 # HPC-Support Ticket: Reservation of Nodes for Power Capping Experiments

## Keywords
- Node reservation
- Power capping
- P-state driver
- Base frequency register
- Kernel alerts
- Rebooting

## Summary
A user requested to reserve nodes on the Fritz cluster to perform experiments with different power capping settings. Previous issues with the p-state driver were noted, including changes to the base frequency register and kernel alerts, which required rebooting to resolve.

## Root Cause of the Problem
- Issues with the p-state driver causing changes to the base frequency register.
- Kernel alerts triggered by these changes.
- Inability to modify the registers back to their original values without rebooting.

## Request Details
- User wants to reserve nodes for power capping experiments.
- Nodes need to be rebooted after the experiments due to previous issues.
- User inquires about the feasible number of nodes and duration for reservation.

## Solution/Action Taken
- The request was deferred for further consideration.

## General Learnings
- Power capping experiments may require dedicated node reservations.
- Previous issues with the p-state driver necessitate rebooting nodes after experiments.
- Users should specify the number of nodes and duration needed for reservations.

## Next Steps
- HPC Admins to determine the feasible number of nodes and duration for reservation.
- Ensure nodes are rebooted after experiments to resolve any issues with the p-state driver.
---

### 2023070842000459_More%20Sapphire%20Rapids%27%20node%20on%20Fritz%20above%20the%20normal%20limit%20of%208%20nodes.md
# Ticket 2023070842000459

 # HPC Support Ticket: Increased Node Access for MPI Scalability Analysis

## Keywords
- Sapphire Rapids
- Compute Node
- MPI Scalability Analysis
- Node Limit
- Partition Reconfiguration

## Summary
A user requested temporary access to more Sapphire Rapids compute nodes above the normal limit of 8 nodes for conducting an MPI scalability analysis.

## Root Cause
- User required additional compute nodes for a specific analysis task.

## Solution
- The partition was temporarily reconfigured to allow jobs with up to 16 nodes for all eligible users.
- The user confirmed that they only needed 10 nodes for a day, and the default configuration could be restored later.

## General Learnings
- Temporary reconfiguration of partitions can be done to accommodate specific user needs.
- Communication between users and HPC admins is essential for managing resource allocations effectively.
- Users should specify their exact requirements to ensure optimal resource usage.

## Actions Taken
- HPC Admins reconfigured the partition to allow up to 16 nodes.
- User confirmed the need for 10 nodes and suggested reverting to the standard restriction later.

## Follow-up
- Ensure the partition is reverted to the default configuration after the user's task is completed.
- Monitor the usage of nodes to ensure fair allocation among users.

## References
- [HPC Services](https://hpc.fau.de/)
- [User Profile](https://hpc.fau.de/person/ayesha-afzal)
- [User Google Site](https://sites.google.com/view/Ayesha-Afzal)

## Notes
- This ticket demonstrates the flexibility of the HPC system in accommodating special requests for resource allocation.
- Effective communication and timely reconfiguration are key to maintaining system efficiency and user satisfaction.
---

### 42012312_woody%20Cluster.md
# Ticket 42012312

 ```markdown
# HPC Support Ticket: Woody Cluster Job Failures

## Keywords
- Woody Cluster
- Job Failures
- Job Scripts
- HP MPI
- Error Messages
- stderr.txt

## Summary
The user reported job failures on the Woody Cluster. The HPC Admin identified the issue as being related to the job scripts rather than the cluster itself.

## Root Cause
- Incorrect capitalization in the job script's `SMETHOD` variable.
  - Original: `SMETHOD='"HP MPI Distributed Parallel for X86 64"'`
  - Corrected: `SMETHOD='"HP MPI Distributed Parallel for x86 64"'`

## Solution
- Correct the capitalization in the `SMETHOD` variable to match the expected format.

## Lessons Learned
- Always check job scripts for syntax and formatting errors.
- Review error messages in `stderr.txt` files for clues about job failures.
- Ensure consistency in variable names and values in job scripts.
```
---

### 2020100142004181_OOM%20Kill%20%281354258%29%20PW%20Jobs%20Emmy.md
# Ticket 2020100142004181

 # HPC Support Ticket: OOM Kill (1354258) PW Jobs Emmy

## Keywords
- OOM Kill
- Memory Limit
- Job Failure
- Node Allocation
- Speicher Limit

## Problem Description
- User's large jobs were being killed due to insufficient memory.
- Jobs were using 16 nodes, which was too close to the memory limit.

## Root Cause
- Insufficient memory allocation for large jobs.

## Solution
- Increase the number of nodes for large jobs from 16 to 20/24 to avoid memory-related job failures.

## Additional Information
- A new version of the software is running on Meggie, which may help with performance.

## Lessons Learned
- Ensure that large jobs have sufficient memory allocation to prevent OOM kills.
- Monitor job performance and adjust resource allocation as needed.

## Follow-Up Actions
- Users should be advised to allocate more nodes for memory-intensive jobs.
- Continue monitoring job performance and resource usage.
---

### 2016102842000231_Queue%20time%20for%20my%20jobs%2C.md
# Ticket 2016102842000231

 ```markdown
# HPC Support Ticket: Queue Time for Jobs

## Keywords
- Job Queue
- Fairshare
- Priority
- Infrastructure Issues
- qstat

## Problem
- User's job (e.g., job 1902138) submitted on Mon Oct 24 10:04:00 2016 is still in the queue.
- User perceives that other jobs are being scheduled before theirs.
- User only sees their own jobs and those of their group in the queue.

## Root Cause
- **Visibility**: User can only see their own jobs and those of their group.
- **Fairshare**: User has a fairshare of 22% over the last 10 days, resulting in a lower priority.
- **Infrastructure Issues**: LiMa nodes are dying due to infrastructure issues and overheating in 2014.

## Solution
- **Explanation**: HPC Admin explained the fairshare system and the current infrastructure issues.
- **Action**: User was informed to continue waiting as there is no issue with their jobs.

## General Learnings
- **Fairshare System**: Understanding how fairshare affects job priority.
- **Queue Visibility**: Users can only see their own and their group's jobs in the queue.
- **Infrastructure Impact**: Infrastructure issues can affect job scheduling and node availability.
```
---

### 2024121842002962_Reservierung%20auf%20fritz%20f%C3%BCr%20ihpc119h.md
# Ticket 2024121842002962

 # HPC Support Ticket Analysis

## Subject
Reservierung auf fritz für ihpc119h

## Keywords
- Reservation
- Fritz-Knoten
- ihpc119h
- Time Slots
- scontrol create reservation
- Partition
- NodeCnt
- Flags
- State

## What Can Be Learned
- **Reservation Request**: User requested reservation of 5 Fritz-Knoten for specific dates and times.
- **Late Request**: The request for the first time slot was too late to be accommodated.
- **Reservation Commands**: HPC Admin provided the commands used to create the reservations.
- **Reservation Details**: Included details such as ReservationName, StartTime, EndTime, Duration, Nodes, NodeCnt, CoreCnt, PartitionName, Flags, TRES, Users, and State.
- **Handling Late Requests**: Importance of timely requests for resource reservations.

## Root Cause of the Problem
- Late submission of the reservation request for the first time slot.

## Solution
- HPC Admin created reservations for the subsequent time slots using `scontrol create reservation` commands.
- Provided detailed information about the reservations created.

## Example Commands
```bash
scontrol create reservation reservationname=ihpc1 user=ihpc119h starttime=2024-12-19T20:00 endtime=2024-12-20T00:00 flags=magnetic partition=multinode nodecnt=5
scontrol create reservation reservationname=ihpc2 user=ihpc119h starttime=2024-12-20T15:00 endtime=2024-12-21T00:00 flags=magnetic partition=multinode nodecnt=5
```

## Notes
- Ensure reservation requests are submitted well in advance to avoid scheduling conflicts.
- Use `scontrol create reservation` to create reservations with specific parameters.
- Monitor the state of reservations to ensure they are active when needed.
---

### 2023060142002793_Tier3-Access-Fritz%20%22Petra%20Imhof%22%20_%20bccc019h.md
# Ticket 2023060142002793

 # HPC Support Ticket Analysis

## Keywords
- Tier3 Access
- Fritz
- Turbomol
- ORCA
- Charmm
- Java
- Single-node throughput
- Multi-node workload
- Computation of enzymatic reaction paths
- Rechenzeit

## Summary
- **User Request:** Access to Fritz for computational chemistry tasks.
- **Software Requirements:** Turbomol, ORCA, Charmm, Java.
- **Resource Requirements:** Single-node throughput (72 cores, 250 GB), multi-node workload (HDR100 Infiniband with 1:4 blocking; per node: 72 cores, 250 GB).
- **Rechenzeit:** 10,000 node hours on Fritz.

## HPC Admin Response
- **Access Granted:** User is now enabled on Fritz as `bccc019h`.
- **Software Availability:**
  - Turbomol 7.6 is installed.
  - ORCA is available; user assumed to have a license.
  - Charmm needs to be installed by the user.
  - Java is available in two variants as a module.

## Lessons Learned
- **User Onboarding:** Ensure users are informed about available software versions and any additional steps they need to take (e.g., installing Charmm).
- **Software Licensing:** Confirm that users have the necessary licenses for software like ORCA.
- **Resource Allocation:** Understand and document the specific resource requirements for different types of workloads (single-node vs. multi-node).

## Root Cause of the Problem
- User needed access to specific software and computational resources for enzymatic reaction path computations.

## Solution
- HPC Admin granted access and provided information on available software versions and installation requirements.

## Documentation for Future Reference
- **Access Request:** Ensure users provide detailed information about their computational needs and software requirements.
- **Software Management:** Maintain a list of available software versions and provide clear instructions for users to install additional software if needed.
- **Resource Allocation:** Document the resource allocation process and ensure users understand the capabilities and limitations of the system.

---

This analysis can be used to streamline future access requests and ensure users have the necessary information to get started with their computational tasks.
---

### 201808229000654_Swappende%20Jobs%20auf%20Woody%20_%20mppi037h.md
# Ticket 201808229000654

 ```markdown
# HPC-Support Ticket: Swappende Jobs auf Woody / mppi037h

## Keywords
- Swapping jobs
- Woody
- Hauptspeichernutzung
- ":sl32g"

## Problem
- **Root Cause**: Some jobs on Woody are swapping permanently.
- **Details**: The jobs are consuming more memory than allocated, leading to swapping.

## Solution
- **Action Required**: Users should request ":sl32g" for these jobs or otherwise limit their memory usage.

## General Learnings
- Monitoring job memory usage is crucial to prevent swapping.
- Requesting additional resources or optimizing memory usage can resolve swapping issues.

## Roles Involved
- **HPC Admins**: Provided the solution and guidance.
- **2nd Level Support Team**: Not directly involved in this ticket but part of the support structure.

## References
- **HPC Services**: Friedrich-Alexander-Universitaet Erlangen-Nuernberg, Regionales RechenZentrum Erlangen (RRZE)
- **Contact**: support-hpc@fau.de
- **Website**: [HPC Services](http://www.hpc.rrze.fau.de/)
```
---

### 2024100842003199_Reservation%20on%2022%20Fritz%20nodes%20with%20-p%20spr1tb.md
# Ticket 2024100842003199

 # HPC Support Ticket: Reservation on 22 Fritz Nodes with -p spr1tb

## Keywords
- Reservation
- Fritz nodes
- SPR nodes
- ICL nodes
- Special reservation
- HPC Admin
- 2nd Level Support

## Summary
A user requested a special reservation of 10 hours on 22 SPR nodes with the partition `spr1tb`. The standard setting allows only 8 SPR nodes. The user also requested an additional reservation on three regular Fritz nodes with ICL due to high cluster usage.

## Root Cause
- Standard setting limits the reservation to 8 SPR nodes.
- High cluster usage necessitated additional reservations.

## Solution
- HPC Admin created two reservations:
  - `spr-ihpc`: 22 SPR nodes for 10 hours on `spr1tb` partition.
  - `icl-ihpc`: 3 regular Fritz nodes with ICL for 10 hours on `multinode` partition.

## Details
- **Initial Request**: User requested a special reservation of 10 hours on 22 SPR nodes with `-p spr1tb`.
- **Admin Response**: Admin acknowledged the request and created the necessary reservations.
- **Additional Request**: User requested an additional reservation on three regular Fritz nodes with ICL due to high cluster usage.
- **Admin Action**: Admin created the additional reservation as requested.

## Lessons Learned
- Special reservations beyond standard limits require admin intervention.
- High cluster usage may necessitate additional reservations to ensure job completion.
- Communication with HPC Admin is crucial for handling special requests efficiently.

## Follow-Up
- Ensure users are aware of the standard reservation limits.
- Provide guidelines for requesting special reservations.
- Monitor cluster usage to anticipate and address high demand periods.
---

### 2022020742002951_Early-Fritz%20%22Wuyang%20Zhao%22%20_%20iwtm010h.md
# Ticket 2022020742002951

 # HPC Support Ticket Analysis

## Keywords
- Performance optimization
- Job efficiency
- Hardware limits
- Roofline analysis
- Deal.ii
- LAMMPS
- Single-node throughput
- Multi-node workload
- Infiniband HCAs
- OpenMPI
- GCC compiler
- MD simulations
- FE-MD coupled simulations

## Summary
A user submitted a request for computational resources, specifying the need for single-node and multi-node workloads using self-compiled software (LAMMPS and Deal.ii). The HPC admins identified poor performance in the user's jobs on existing clusters (Emmy and Meggy) and suggested performance analysis and optimization before considering new hardware.

## Root Cause of the Problem
- The user's jobs showed poor performance and were far from hardware limits.
- Inefficient use of existing computational resources.

## Solution
- The HPC admins offered assistance in analyzing and optimizing the performance of the user's applications.
- Recommended not to move to new hardware until the performance on existing systems is improved.

## What Can Be Learned
- Regular performance analysis is crucial for efficient use of HPC resources.
- Optimizing job performance on existing hardware should be a priority before considering new hardware.
- Complex applications like Deal.ii and LAMMPS may require specialized knowledge for performance optimization.
- HPC support teams can provide valuable assistance in performance analysis and optimization.

## Next Steps for Support Employees
- Offer performance analysis and optimization services to users with similar issues.
- Use roofline analysis tools to identify performance bottlenecks.
- Encourage users to optimize their jobs on existing hardware before requesting new resources.

## Relevant Links
- [Job Info on Meggy](https://www.hpc.rrze.fau.de/HPC-Status/job-info.php?USER=iwtm010h&JOBID=1027567&ACCESSKEY=8fbc9325&SYSTEM=MEGGIE)
- [Roofline Analysis on Meggy](https://www.hpc.rrze.fau.de/JobRoofline.MEGGIE?USER=iwtm010h&JOBID=1027567&ACCESSKEY=8fbc9325)
- [Job Info on Emmy](https://www.hpc.rrze.fau.de/HPC-Status/job-info.php?USER=iwtm010h&JOBID=1585892&ACCESSKEY=bf1c7ffc&SYSTEM=EMMY)
- [Roofline Analysis on Emmy](https://www.hpc.rrze.fau.de/JobRoofline.EMMY?USER=iwtm010h&JOBID=1585892&ACCESSKEY=bf1c7ffc)

## Contact
For further assistance, contact the HPC support team at [support-hpc@fau.de](mailto:support-hpc@fau.de).
---

### 2019121242000823_OpenFoam%20jobs%20on%20meggie%20-%20iwpa014h.md
# Ticket 2019121242000823

 ```markdown
# HPC Support Ticket Conversation Analysis

## Keywords
- OpenFOAM
- Multigrid solver
- Conjugate Gradient solver
- DNS simulation
- LES simulation
- Inter-node communication
- Roofline diagram
- Performance metrics
- Scaling runs
- Infiniband packets
- MPI communication
- Job efficiency
- Queuing time

## General Learnings
- The user encountered performance issues with OpenFOAM jobs on the MEGGIE cluster.
- The initial issue was related to high inter-node communication and low computation, indicating too many processes for the available work.
- The user experimented with different solvers (Multigrid and Conjugate Gradient) and node configurations to optimize performance.
- The HPC Admins provided guidance on scaling runs, monitoring tools, and performance metrics to help the user identify the optimal setup.
- The user observed significant performance differences between runs, with some jobs showing unexpectedly high performance metrics.
- The HPC Admins investigated the jobs and provided insights into the performance metrics, communication patterns, and potential causes of the observed issues.

## Root Cause of the Problem
- The user's jobs were not efficiently utilizing the available resources, leading to high communication overhead and low computation.
- The choice of solver and node configuration significantly impacted the performance of the simulations.

## Solution
- The user conducted scaling runs to determine the optimal number of nodes and solver configuration.
- The HPC Admins recommended reducing the number of nodes or adjusting the grid levels to improve resource utilization.
- The user monitored the communication overhead and adjusted the node numbers accordingly.
- The HPC Admins provided detailed performance metrics and insights to help the user understand the underlying issues and optimize the simulations.
```
---

### 2024080942001685_Issue%20in%20allocating%20a%20job.md
# Ticket 2024080942001685

 ```markdown
# Issue in Allocating a Job

## Keywords
- Job allocation
- HPC cluster
- Interactive job
- Job scripts
- Wall time

## Problem Description
- User unable to run any jobs on the HPC cluster since the previous morning.
- User attached a screenshot for reference.
- Issue frequently encountered, affecting work focus.

## Root Cause
- High cluster usage by multiple users causing delays in job allocation.

## Solution
- For interactive jobs, use a wall time of less than 2 hours to start faster.
- Use job scripts to submit jobs and check results later, avoiding the need to wait for job start.

## General Learnings
- High cluster usage can cause delays in job allocation.
- Interactive jobs with shorter wall times start faster.
- Job scripts are recommended for non-interactive jobs to avoid waiting.
```
---

### 2022110542000351_Aibe%20Qos.md
# Ticket 2022110542000351

 # HPC Support Ticket: Aibe Qos

## Keywords
- QoS (Quality of Service)
- Invalid QoS specification
- AIBE (Image and Data Exploration Lab)
- GPU allocation
- Batch script

## Problem
- User encountered an "Invalid QoS specification" error when trying to use the `--qos=a100_aibe` flag to train models for more than a single day.

## Root Cause
- The user was not initially enabled for the `--qos=a100_aibe` flag.

## Solution
- HPC Admin enabled the user for the `--qos=a100_aibe` flag.

## Additional Information
- The `--qos=a100_aibe` flag is limited to 4 GPUs for all AIBE users combined.
- Submitting too many jobs with this flag may result in long waiting times.

## Ticket History
- User reported the issue via email, including a screenshot of the batch script.
- HPC Admin responded, confirming the user was enabled for the QoS flag and providing additional information about GPU limitations.

## Follow-up
- Users should be aware of the GPU limitations and plan their jobs accordingly to avoid long waiting times.

---

This documentation can be used to resolve similar QoS specification errors in the future.
---

### 2022080442003052_mpi4py%20parallel.md
# Ticket 2022080442003052

 ```markdown
# HPC-Support Ticket: mpi4py Parallel Performance Issue

## Problem Description
- User observed significant performance degradation when running an MPI-parallel application on Meggie with more than two processes.
- Each work package is a linear optimization problem solved using Gurobi with the `Threads=1` parameter set.
- Despite limiting Gurobi to one thread, the performance issue persists, even when each process runs on a separate node.

## Root Cause
- The performance issue was initially suspected to be related to thread contention or MPI communication overhead.
- Further investigation revealed that the issue was due to a misconfigured method parameter in Gurobi.

## Solution
- The user adjusted the method parameter in Gurobi, which resolved the performance issue.
- Additionally, the user observed that the broadcasting of data packets between processes sometimes took an unusually long time, causing delays.
- The user implemented `print()` statements to track the timing and rank of each process, which helped identify that the sending process was occasionally delayed.

## Keywords
- mpi4py
- Gurobi
- Performance degradation
- Thread contention
- MPI communication
- Broadcasting delay

## Lessons Learned
- Misconfigured method parameters in Gurobi can lead to significant performance issues.
- Broadcasting delays can be caused by one process being slower than others, leading to synchronization issues.
- Implementing detailed logging can help identify and resolve performance bottlenecks in parallel applications.
```
---

### 2021101542000737_Confusion%20with%20Cores_Node%20and%20SMT.md
# Ticket 2021101542000737

 # HPC Support Ticket: Confusion with Cores/Node and SMT

## Keywords
- Cores per Node
- SMT (Simultaneous Multithreading)
- Emmy Cluster
- Meggie Cluster
- PBS
- SLURM
- mpirun

## Problem Description
The user is confused about the number of cores per node on Emmy and Meggie clusters and the availability of SMT. The user can request 40 tasks per node on Emmy but only 20 tasks per node on Meggie. The user wants to know if they should run their simulation with `mpirun -np 280` (no SMT) or `mpirun -np 560` (with SMT) on Meggie.

## Root Cause
SMT is disabled on Meggie, which is why the user cannot request more than 20 tasks per node.

## Solution
Since SMT is disabled on Meggie, the user should run their simulation with `mpirun -np 280`.

## General Learnings
- Emmy cluster allows SMT, with 40 tasks per node (2 CPUs/Node * 10 Cores/CPU * 2 Tasks/Core).
- Meggie cluster does not allow SMT, with a maximum of 20 tasks per node.
- Always check the cluster documentation or contact HPC support for cluster-specific configurations.

## Follow-up Actions
- Update the official documentation to reflect that SMT is disabled on Meggie.
---

### 2022041242002634_Gromacs%20Multinode%20auf%20Fritz%20%5Bbcpc002h%5D.md
# Ticket 2022041242002634

 # HPC Support Ticket: Gromacs Multinode auf Fritz [bcpc002h]

## Keywords
- Multinode User
- Gromacs
- Fritz
- Job Submission
- Documentation

## Summary
The user has been enabled as a multinode user on the Fritz HPC system, allowing them to submit jobs that require multiple nodes. The HPC Admin provided a link to the Gromacs documentation page, which includes an example script for running Gromacs on multiple nodes.

## Problem
The user needs guidance on how to submit multinode jobs for Gromacs on the Fritz HPC system.

## Solution
The HPC Admin directed the user to the Gromacs documentation page, which contains an example script for running Gromacs on multiple nodes. The link provided is:
[Gromacs Documentation](https://hpc.fau.de/systems-services/systems-documentation-instructions/special-applications-and-tips-tricks/gromacs/?preview_id=5834&preview_nonce=2d9cdd98f1&_thumbnail_id=-1&preview=true#collapse_3)

## General Learning
- Users can be enabled as multinode users to submit jobs that require multiple nodes.
- The Gromacs documentation page provides example scripts for running Gromacs on multiple nodes.
- HPC Admins are available to assist with any questions or issues related to job submission and documentation.

## Next Steps
- Users should refer to the provided documentation for guidance on submitting multinode jobs.
- If further assistance is needed, users can contact the HPC support team.
---

### 2022101342003343_Lammps-Jobs%20on%20Meggie%20%5Bbccc011h%5D.md
# Ticket 2022101342003343

 # HPC Support Ticket: Lammps-Jobs on Meggie

## Keywords
- Job distribution
- Slurm
- mpirun
- srun
- Job monitoring

## Problem
- **Root Cause**: User's jobs on Meggie were only running on the first node instead of all allocated nodes.
- **Cause**: The addition of the flag `-np 20` after invoking `mpirun`.

## Solution
- **Action**: Replace `mpirun -np 20` with `srun`. Slurm will handle the number of processes and distribute them automatically.
- **Monitoring**: Users can log into the job monitoring system with their HPC account and password to check job status.

## General Learning
- **Job Distribution**: Slurm handles the distribution of processes automatically.
- **mpirun vs srun**: Use `srun` instead of `mpirun` with Slurm to avoid manual process management.
- **Job Monitoring**: Users can monitor their jobs using the provided monitoring system.

## Related Links
- [Job Monitoring](https://monitoring.nhr.fau.de/)
- [HPC FAU](https://hpc.fau.de/)
---

### 2024100642000481_Dummyaccount%20%2B%20Reservierung%20saprap2%20f%C3%83%C2%BCr%20CLPE%20Tutorial%20am%2008.10..md
# Ticket 2024100642000481

 ```markdown
# HPC Support Ticket Analysis: Dummy Account and Node Reservation

## Keywords
- Dummy account
- Node reservation
- Test cluster
- Tutorial
- Account creation
- Account reuse
- Short notice

## Summary
A user requested the creation of a dummy account and the reservation of a specific node (saprap2) in the test cluster for a tutorial. The request was made on short notice.

## Root Cause
- **Short Notice Request**: The user's request was made close to the required date, which caused some logistical challenges.
- **Account Reuse**: The user suggested reusing an account from a previous tutorial if it was still available.

## Solution
- **Account Creation**: The HPC Admin confirmed the creation of a dummy account and provided the account information via chat.
- **Node Reservation**: The HPC Admin reserved the saprap2 node for the specified dates.
- **Delay in Activation**: The account activation required additional time due to the need for IDM to transmit the account information.

## Lessons Learned
- **Advance Planning**: Users should submit requests well in advance to avoid short notice issues.
- **Account Management**: Reusing existing accounts can be an efficient solution if they are still available.
- **Communication**: Clear communication between the user and HPC Admin is crucial for timely resolution of requests.

## Actions Taken
- The HPC Admin created a dummy account and reserved the saprap2 node.
- The account information was shared via chat, and the user was informed about the delay in activation.

## Follow-up
- Ensure that users are aware of the importance of submitting requests with sufficient lead time.
- Improve communication channels for sharing account information and activation status.
```
---

### 2021020142002099_Your%20jobs%20on%20Meggie%20862041%20%28iww8010h%29.md
# Ticket 2021020142002099

 # HPC Support Ticket: Poor Job Performance on Meggie

## Keywords
- Job Performance
- OpenMP Threads
- MPI Tasks
- Memory Usage
- Thread Pinning

## Problem Description
- User's jobs on Meggie showed poor performance.
- Job monitoring indicated that the code did not scale beyond 8 OpenMP threads per MPI task.
- User reported memory issues when using `SLURM_CPUS_PER_TASK=10`.

## Root Cause
- Inefficient use of OpenMP threads and MPI tasks.
- Memory limitations when increasing the number of CPUs per task.

## Solution
- **HPC Admin** suggested reducing OpenMP threads to 5 per MPI task to improve performance and reduce OpenMP overhead.
- **HPC Admin** also suggested pinning OpenMP threads to improve efficiency:
  ```bash
  unset KMP_AFFINITY
  export OMP_PLACES=cores
  export OMP_PROC_BIND=spread
  export OMP_NUM_THREADS=$((SLURM_CPUS_PER_TASK/2))
  ```
- Offered to perform pinning experiments if the user could share an example.

## General Learnings
- Monitoring job performance can reveal scaling issues with OpenMP threads and MPI tasks.
- Adjusting the number of OpenMP threads and MPI tasks can improve performance.
- Pinning OpenMP threads can enhance efficiency.
- Collaboration with users to optimize code performance is beneficial.

## Next Steps
- User should try the suggested changes and report back on performance improvements.
- Further optimization may be possible through code development and additional experiments.
---

### 2018062642001613_Ausleiten%20der%20Daten%20von%20Meggie.md
# Ticket 2018062642001613

 # HPC-Support Ticket Conversation Analysis

## Subject: Ausleiten der Daten von Meggie

### Keywords
- ProPE Meeting
- Dresdner Monitoring
- Ganglia XML
- ClustWare
- InfluxDB
- Meggie
- Data Extraction
- Motivation
- Installation
- Simplification

### Summary
- **Root Cause**: The user is concerned about the lack of motivation among team members and wants to simplify the installation of the Dresdner monitoring system.
- **Issue**: The user wants to prepare for pumping Meggie data into InfluxDB but is unsure if it is possible and recalls previous issues.
- **Solution**: Not explicitly provided in the conversation.

### What Can Be Learned
- **Motivation and Team Dynamics**: Addressing motivation issues within the team can lead to better performance and collaboration.
- **Monitoring Systems**: Understanding the compatibility and integration of different monitoring systems (e.g., Dresdner monitoring, Ganglia XML) is crucial for efficient data management.
- **Data Extraction**: Preparing for data extraction and integration (e.g., pumping Meggie data into InfluxDB) requires understanding the system's capabilities and previous issues.

### Next Steps
- **Investigate**: Check the compatibility of Meggie with InfluxDB and identify any previous issues that need to be resolved.
- **Document**: Create detailed documentation on the steps required to integrate Meggie data with InfluxDB.
- **Communicate**: Share findings and progress with the team to maintain transparency and motivation.

### Additional Notes
- **Team Collaboration**: Regular meetings and clear communication can help address motivation issues and ensure everyone is on the same page.
- **System Integration**: Thorough testing and documentation are essential for successful integration of new monitoring systems.

---

This analysis provides a brief overview of the conversation and highlights key points for future reference.
---

### 2019071542003629_MPI%20processes%20on%20current%20jobs.md
# Ticket 2019071542003629

 ```markdown
# HPC Support Ticket: MPI Processes on Current Jobs

## Keywords
- MPI processes
- Node utilization
- mpirun
- -npernode option

## Problem Description
- User's jobs were only utilizing half of the requested nodes, leaving the other half idle.

## Root Cause
- The user did not specify the number of processes per node in the `mpirun` call.

## Solution
- Specify the number of processes per node using the `-npernode` option in the `mpirun` call. For example, to use 20 processes per node, the command should be:
  ```bash
  mpirun -npernode 20 ...
  ```

## Lessons Learned
- Always ensure that the `mpirun` command is configured to utilize all requested nodes efficiently.
- Specifying the `-npernode` option helps in distributing the processes evenly across the nodes.

## Follow-up
- The user acknowledged the advice and killed the job to fix the `mpirun` option.
- The HPC Admin confirmed that all nodes were being utilized after the correction.
```
---

### 2024120342003542_Tier3-Access-Fritz%20%22Philipp%20Gurtner%22%20_%20iwia123h.md
# Ticket 2024120342003542

 # HPC Support Ticket Conversation Analysis

## Keywords
- HPC Account Activation
- Fritz Cluster
- Single-node Throughput
- Multi-node Workload
- C++17 Compiler
- CMake
- Git
- MPI
- Python
- Multigrid Solvers
- Nonlinear PDEs
- HyTeG Framework

## Summary
- **Account Activation**: The user's HPC account was activated on the Fritz cluster.
- **Resource Requirements**: The user requested access for single-node throughput and multi-node workload with specific hardware requirements.
- **Software Requirements**: The user specified the need for a C++17 compliant compiler, CMake, Git, MPI, and Python.
- **Application**: The user is working on a Bachelor's thesis involving solving large-scale nonlinear partial differential equations using multigrid on hybrid tetrahedral grids.
- **Expected Outcomes**: The user aims to develop working multigrid solvers for nonlinear PDEs within the HyTeG framework.

## Lessons Learned
- **Account Activation Process**: Understanding the steps involved in activating an HPC account.
- **Resource Allocation**: How to handle requests for specific hardware resources such as single-node throughput and multi-node workloads.
- **Software Dependencies**: Importance of specifying and ensuring the availability of required software versions for user projects.
- **Project Documentation**: The necessity of clear communication regarding the project's goals and expected outcomes.

## Root Cause of the Problem
- The user required access to specific HPC resources and software for their research project.

## Solution
- The HPC Admin activated the user's account on the Fritz cluster, ensuring they have access to the required resources and software.

## Additional Notes
- This ticket highlights the importance of detailed communication between users and HPC support to ensure all necessary resources and software are available for research projects.
---

### 2019012542000543_Jobs%20starten%20nicht.md
# Ticket 2019012542000543

 # HPC Support Ticket: Jobs Not Starting

## Keywords
- Job scheduling
- Queue management
- Quota limits
- SystemQueueTime
- Job submission

## Problem Description
- User's jobs on the HPC cluster are not starting and are being rescheduled in the queue.
- Example job ID: 1047257
- Submitted earlier in the week but still in the queue with a recent SystemQueueTime.

## Root Cause
- Possible quota limits exceeded (storage, number of files, etc.).

## Solution
- Check user's quota usage.
- Verify if the job is being rescheduled due to resource availability or other constraints.

## General Learnings
- Regularly monitor job status and queue times.
- Ensure users are aware of their quota limits and how to check them.
- Investigate job scheduling policies and resource allocation to identify any bottlenecks.

## Next Steps
- HPC Admins to review the user's quota and job status.
- Provide guidance on managing quota and optimizing job submissions.

## Relevant Contacts
- HPC Admins: Thomas, Michael Meier, Anna Kahler, Katrin Nusser, Johannes Veh
- 2nd Level Support: Lacey, Dane (fo36fizy), Kuckuk, Sebastian (sisekuck), Lange, Florian (ow86apyf), Ernst, Dominik (te42kyfo), Mayr, Martin
- Datacenter Head: Gerhard Wellein
- Training and Support Group Leader: Georg Hager
- NHR Rechenzeit Support: Harald Lanig
- Software and Tools Developer: Jan Eitzinger, Gruber
---

### 2020070142002939_Simulation%20with%20StarCCM%2B..md
# Ticket 2020070142002939

 ```markdown
# HPC-Support Ticket: Simulation with StarCCM+

## Keywords
- Simulation
- StarCCM+
- Node allocation
- Job failure
- Queue waiting time

## Summary
A user reported issues with job failures and long queue waiting times while running simulations with StarCCM+. The user was advised to use more nodes to accelerate computations but was unsure about the rationale behind this suggestion.

## Root Cause
- **Job Failures**: No specific details provided, making it difficult to diagnose the exact cause.
- **Queue Waiting Time**: Normal for a well-utilized system.

## Details
- The user had previously run simulations with 1-2 nodes but was advised to use 8 nodes for faster computations.
- The user was concerned about the nominal suggestion to load each CPU with 50,000 to 100,000 cells.
- The HPC Admin confirmed that the user had recently run jobs with 2, 4, 8, 16, and 32 nodes.

## Solution
- No specific solution provided for job failures due to lack of details.
- Queue waiting time is normal and expected in a well-utilized system.
- The user should provide more details about job failures for further diagnosis.

## Learning Points
- Users should provide detailed information about job failures for effective troubleshooting.
- Queue waiting times are normal in a well-utilized HPC system.
- Using more nodes can accelerate computations, but the specific benefits depend on the simulation's requirements and the system's utilization.
```
---

### 2022032842003427_Low%20performance%20of%20jobs%20on%20emmy%20-%20bcml002h.md
# Ticket 2022032842003427

 ```markdown
# Low Performance of Jobs on Emmy - bcml002h

## Keywords
- Low performance
- Emmy cluster
- Single-core jobs
- Node utilization
- Job merging
- Cluster suitability

## Problem Description
- User reported low performance of jobs on the Emmy cluster.
- Jobs were using only one core per node.

## Root Cause
- Emmy cluster has 20 cores per node, making it unsuitable for single-core jobs.
- Inefficient use of resources due to single-core jobs running on a multi-core node.

## Solution
- Merge jobs to utilize all cores on a single node.
- Alternatively, move jobs to a more suitable cluster, such as Woody.

## Lessons Learned
- Ensure job configurations match the cluster's hardware capabilities.
- Monitor job performance and resource utilization to optimize workload distribution.
- Consider moving jobs to more suitable clusters if current resources are not efficiently utilized.
```
---

### 2022112242000587_Kursaccounts.md
# Ticket 2022112242000587

 ```markdown
# HPC Support Ticket Conversation Analysis

## Subject: Kursaccounts

### Keywords:
- HPC-Kursaccounts
- Reservierung
- Fritz
- Alex
- LIKWID Engineering
- Nodelevel-Kurs
- ReservationName
- StartTime
- EndTime
- Duration
- Nodes
- NodeCnt
- CoreCnt
- PartitionName
- Flags
- MAGNETIC
- TRES
- Accounts
- State
- BurstBuffer
- MaxStartDelay
- singlenode

### Summary:
- **Request:** User requested 50 HPC course accounts with access to Fritz and Alex for a LIKWID Engineering course from November 22, 2022, to December 2, 2022.
- **Additional Request:** User also requested a reservation of 45 nodes on Fritz from 17:00 to 01:00 on November 30, December 1, and December 2.
- **Reservation Details:** HPC Admin provided reservation details with the MAGNETIC flag for automatic usage.
- **Question:** User asked if the `-p singlenode` flag was still necessary.
- **Response:** HPC Admin confirmed that the `-p singlenode` flag was still required.

### Root Cause of the Problem:
- User needed HPC course accounts and node reservations for a specific course.

### Solution:
- HPC Admin created the requested accounts and provided reservation details.
- Confirmed that the `-p singlenode` flag was still necessary.

### General Learnings:
- Understanding the process of requesting and managing HPC course accounts.
- Importance of the MAGNETIC flag for automatic reservation usage.
- Necessity of the `-p singlenode` flag for certain operations.
```
---

### 2018061242001514_HPC%20Modelllauf%20Verbesserung.md
# Ticket 2018061242001514

 # HPC Support Ticket: Model Run Improvement

## Keywords
- Model runs
- Code issues
- Node configuration
- MPI
- OpenMP
- WRF
- Meggie
- HSW/BDW
- dmpar

## Problem Description
- User's model runs are inconsistent, sometimes completing in 14 minutes and other times taking 4 hours.
- Runs occasionally abort without error messages.
- User is unsure if the issue is with the code or node configuration.

## User Configuration
- Model runs in `/home/woody/gwgk/gwgk003h/WRF/WRFV3/test/em_real` with `real.meggie.sh` and `wrf.meggie.sh`.
- Configured with settings 20 (linux dmpar) and 1 (basic nesting).
- Also tried Jenny's settings (real.jenny.sh and wrf.jenny.sh) with configuration 66 (HSW/BDW) and 1.

## HPC Admin Response
- HSW/BDW is the correct architecture for Meggie.
- `dmpar` is for the pure MPI version; using `mpirun -n 20` with `--nodes=10` is inefficient as it only uses 2 cores per node.
- Starting 20 MPI processes on a single node is more economical, resulting in 13-14 minutes runtime.
- Using 40 MPI processes across 2 nodes reduces runtime to ~10 minutes but is not justified by the resource usage.
- Hybrid code version with 10 MPI processes * 2 OpenMP threads per node resulted in runtime aborts.
- No significant runtime variations observed on a single Meggie node.

## Solution
- Use HSW/BDW architecture.
- Start 20 MPI processes on a single node for optimal performance.
- If runtime variations persist, provide the relevant job IDs for further investigation.

## General Learnings
- Proper architecture and node configuration are crucial for consistent and efficient model runs.
- Inefficient resource allocation can lead to longer runtimes and inconsistent performance.
- Hybrid code versions may introduce additional complexities and issues.
- Detailed job IDs can help in diagnosing runtime variations.
---

### 2023042142002875_Group%20node%20limit%20on%20Fritz%20-%20nfcc.md
# Ticket 2023042142002875

 # HPC Support Ticket Conversation Analysis

## Keywords
- Group node limit
- Fritz HPC cluster
- Dynamic limits
- Tier3-Bereich
- 1/2 TB Knoten
- NHR-only

## General Learnings
- Group node limits on the Fritz HPC cluster are dynamically adjusted based on system load and the number of active groups.
- The current limit for the user's group is 10 nodes, equivalent to the computing power of about 50 Meggie nodes.
- In 2022, there were over 100 active groups in the Tier3 area, with only a small portion of Fritz allocated for Tier3 supply.
- The 1/2 TB nodes are reserved for NHR-only and are not available for Tier3 basic supply.
- Users and group leaders cannot see the jobs of all group members, which is intended behavior.

## Root Cause of the Problem
- The user noticed a reduction in the group node limit from about 40 nodes to 10 nodes.
- The user was unaware of the dynamic nature of the node limits and the current system load.

## Solution
- The HPC Admin explained the dynamic adjustment of node limits and the current system load.
- The user was informed that the 1/2 TB nodes are not available for Tier3 basic supply.

## Additional Notes
- The user inquired about the availability of 1/2 TB nodes for testing in early May but was informed that these nodes are reserved for NHR-only.
- The user acknowledged the information provided by the HPC Admin.
---

### 2024091342002405_Reservierung%20auf%20fritz%20f%C3%83%C2%BCr%20ihpc119h.md
# Ticket 2024091342002405

 # HPC Support Ticket: Reservation Request for Fritz Nodes

## Keywords
- Reservation
- Fritz Nodes
- Specific Dates and Times
- User Account
- HPC Admin

## Summary
A user requested a reservation of 5 Fritz nodes for a specific user account during defined time slots on specific dates. The HPC Admin confirmed the reservation and provided details.

## Problem
- **Root Cause**: User needed a reservation for specific nodes and time slots.

## Solution
- **Action Taken**: HPC Admin created reservations for the specified nodes and time slots.
- **Details**:
  - **ReservationName**: bench-09-17, bench-09-18, bench-09-19
  - **StartTime**: 2024-09-17T13:00:00, 2024-09-18T13:00:00, 2024-09-19T13:00:00
  - **EndTime**: 2024-09-17T21:00:00, 2024-09-18T21:00:00, 2024-09-19T21:00:00
  - **Duration**: 08:00:00
  - **Nodes**: f[0401-0405]
  - **NodeCnt**: 5
  - **CoreCnt**: 360
  - **Users**: ihpc119h
  - **Flags**: SPEC_NODES
  - **State**: INACTIVE

## General Learnings
- Reservations must be explicitly requested to ensure specific nodes are used.
- Reservations include details such as start time, end time, duration, nodes, and user accounts.
- HPC Admin confirms reservations and provides detailed information.

## References
- Friedrich-Alexander-Universität Erlangen-Nürnberg (FAU)
- Zentrum für Nationales Hochleistungsrechnen Erlangen (NHR@FAU)
- [HPC Support Email](mailto:support-hpc@fau.de)
- [HPC Website](https://hpc.fau.de/)
---

### 2022042242001634_Accidentally%20started%20process.md
# Ticket 2022042242001634

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject: Accidentally started process

### Keywords:
- Accidental process start
- System slowdown
- Process termination
- User error

### Summary:
A user accidentally started a process that caused the system (woody) to slow down. The user requested the HPC Admins to kill their processes to resolve the issue.

### Root Cause:
- User error: Accidentally started a process that consumed excessive resources.

### Solution:
- The user requested the termination of their processes.
- The system returned to normal operation after the processes were terminated.

### Lessons Learned:
- Users should be cautious when starting processes to avoid consuming excessive resources.
- Quick communication with HPC Admins can help resolve issues caused by accidental process starts.
- Regular monitoring of system performance can help identify and address resource-intensive processes.

### Actions Taken:
- The user requested the termination of their processes.
- The system performance returned to normal after the processes were terminated.

### Follow-up:
- Educate users on best practices for starting and managing processes.
- Ensure users are aware of the impact of resource-intensive processes on system performance.
```
---

### 2022101242001712_segfault%20on%20hybrid%20job%20-%20b133ae16.md
# Ticket 2022101242001712

 ```markdown
# HPC-Support Ticket: Segfault on Hybrid MPI/OpenMP Job

## Issue Description
- User encountered crashes in a hybrid MPI/OpenMP job, with some jobs getting stuck and others crashing with a segmentation fault.
- The program is well-tested and has not observed crashes on other HPC machines.
- The job script is "job.sh", and the executable is ALF.out.
- The job configuration: nodes=4, ntasks-per-node=18, cpus-per-task=4.
- Compiled with ifort and modules: intel/2022.1.0, intelmpi/2021.6.0, mkl/2022.1.0.

## Error Messages
- Segmentation fault:
  ```
  [f0665:90992:0:91176] Caught signal 11 (Segmentation fault: invalid permissions for mapped object at address 0x224c580)
  ==== backtrace (tid: 91176) ====
  0 /lib64/libucs.so.0(ucs_handle_error+0x2a4) [0x15016c0aaa54]
  1 /lib64/libucs.so.0(+0x26c2c) [0x15016c0aac2c]
  2 /lib64/libucs.so.0(+0x26dfa) [0x15016c0aadfa]
  3 [0x224c580]
  =================================
  forrtl: severe (174): SIGSEGV, segmentation fault occurred
  ```

## Troubleshooting Steps
1. **Compilation with Bounds Checking and Address Sanitizer:**
   - User compiled the program with bounds checking and address sanitizer enabled.
   - No errors found except for some known memory leaks.

2. **Valgrind Testing:**
   - User ran the program with Valgrind and found no errors.

3. **Reproducing the Issue:**
   - User ran the program multiple times on the HPC cluster with bounds checking enabled.
   - Some jobs got stuck and were killed after exceeding the time limit.
   - One job was killed by a "Bus error" when compiled with intel/2021, intelmpi/2021, and mkl/2021.

4. **HPC Admin Actions:**
   - HPC Admin ran the job multiple times but could not reproduce the issue initially.
   - Collected stack traces and found that the fault occurred inside "zgetri" in the MKL library.
   - Recommended further testing with bounds checking and address sanitizer.

## Possible Causes
- Memory overridden due to out-of-bounds access.
- Incorrect parameters to "zgetri" (unlikely).
- Issue with "zgetri" (unlikely).

## Next Steps
- User to investigate where processes were hanging and where the BUS error occurred.
- HPC Admin to continue monitoring and testing to identify the root cause.

## Conclusion
- The issue is intermittent and may be related to hardware or software specific to certain nodes.
- Further investigation is needed to pinpoint the exact cause of the segmentation fault and job hangs.
```
---

### 2017031442001698_schnellste%20Cluster.md
# Ticket 2017031442001698

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject: schnellste Cluster

### Keywords:
- HPC Cluster
- Performance
- Speed

### Summary:
- **User Inquiry:** The user is interested in knowing which HPC cluster at the computing center is generally the fastest.
- **HPC Admin Response:** No response provided in the given conversation.

### Root Cause:
- The user seeks information on the fastest HPC cluster available at the computing center.

### Solution:
- Provide the user with information on the performance metrics of different clusters, including details on CPU speed, memory, and other relevant specifications.
- Offer guidance on how to choose the best cluster based on their specific computational needs.

### General Learning:
- Users often need guidance on selecting the most suitable HPC resources for their tasks.
- It is important to have readily available performance data for different clusters to assist users in making informed decisions.
```
---

### 2023062142004655_Kursaccounts%20und%20Reservierung%20auf%20Fritz%2C%2027.-30.6..md
# Ticket 2023062142004655

 # HPC Support Ticket Conversation Analysis

## Keywords
- HPC-Kursaccounts
- Fritz
- Reservierung
- NLPE-Kurs HLRS
- Slurm-Aktivierung
- Accountdaten
- Nodes
- Vorbereitungsmails

## Summary
- **User Request:** 40 HPC course accounts for NLPE-Kurs HLRS with access to Fritz, valid from June 21 to June 30. Reservation of 30 Fritz nodes for specific times between June 27 and June 30.
- **HPC Admin Response:** Accounts created with details to be sent via chat. Slurm activation and reservation to be done the next day.
- **Follow-up:** User requested account activation on Fritz to send preparation emails to participants. HPC Admin confirmed activation with a maximum of 4 nodes per account.

## Root Cause of the Problem
- User needed HPC course accounts and node reservations for a specific course and timeframe.

## Solution
- HPC Admin created the accounts and scheduled the Slurm activation and reservation.
- Accounts were activated on Fritz, allowing the user to proceed with sending preparation emails to participants.

## General Learnings
- **Account Management:** HPC Admins handle the creation and activation of course accounts.
- **Reservations:** Node reservations are managed through Slurm and require admin intervention.
- **Communication:** Important account details are communicated via chat, and follow-up actions are confirmed through the ticket system.

## Action Items for Similar Cases
- Ensure timely creation and activation of course accounts.
- Schedule Slurm activation and node reservations as per user requests.
- Communicate account details securely and confirm actions through the ticket system.
---

### 2019121042000498_VASP%20Jobs%20auf%20Emmy.md
# Ticket 2019121042000498

 # HPC Support Ticket: VASP Jobs auf Emmy

## Keywords
- VASP Jobs
- Emmy
- MPI Prozesse
- Hostfile
- Jobscript
- Performance
- MPI-Pinning

## Problem
- User was using 40 MPI processes on a node with only 20 cores.
- The job script was fetching the number of MPI processes from the hostfile ($PBS_NODEFILE), which contained double the number of cores.

## Root Cause
- Incorrect configuration in the job script leading to over-subscription of MPI processes on the node.

## Solution
- Remove the explicit specification of MPI processes in the job script.
- Use the following command instead:
  ```bash
  mpirun $VASP > $PBS_O_WORKDIR/${PBS_JOBID}/vasp.out 2> $PBS_O_WORKDIR/${PBS_JOBID}/vasp.err
  ```
- Optionally, add MPI-Pinning for better performance:
  ```bash
  export I_MPI_PIN=ON
  export I_MPI_PIN_PROCESSOR_LIST=allcores
  ```

## General Learnings
- Ensure job scripts are configured correctly to avoid over-subscription of resources.
- MPI-Pinning can improve performance by binding processes to specific cores.
- Always include the HPC-Kennung in the subject for easier tracking and searching.

## Additional Notes
- The default binding for `mpirun` is `none`, but it does not over-subscribe.
- No specific documentation on MPI-Pinning was found on the HPC websites, so Intel mechanisms are acceptable.

## Actions Taken
- HPC Admins provided detailed instructions for correcting the job script.
- User agreed to update the script and inform colleagues about the issue.
- HPC Admins suggested adding MPI-Pinning for potential performance improvements.
---

### 2024013142003279_Re%3A%20Long%20running%20process%20on%20host%20fritz4%20-%20a102cb12%20-%20speed%20of%20Python%20cod.md
# Ticket 2024013142003279

 # HPC Support Ticket Analysis

## Keywords
- Long-running process
- Python code optimization
- Numpy multithreading
- Interactive node usage
- cProfile
- Numba
- Memory usage
- Least square method
- Batch jobs

## Summary
A user ran a long-running Python process on a frontend node, which was automatically killed due to excessive CPU usage. The user was advised to use interactive nodes for such tasks. Additionally, the user sought advice on optimizing Python code using Numpy for a memory-intensive fitting process.

## Root Cause
- The user forgot to connect to an interactive node and ran a resource-intensive Python process on a frontend node.
- Numpy's default multithreading caused high CPU usage.

## Solution
- Use interactive nodes for long-running processes to avoid disturbing other users.
- Consider using Numba for Python code optimization, although it requires code changes.
- Analyze cProfile results for further optimization insights.

## General Learnings
- Always use dedicated nodes (interactive or batch) for resource-intensive tasks.
- Be mindful of default multithreading in libraries like Numpy.
- Tools like Numba can significantly speed up Python code but may require code modifications.
- cProfile is a useful tool for profiling Python code to identify bottlenecks.

## Follow-up Actions
- Provide guidance on interpreting cProfile results.
- Offer workshops or tutorials on Python optimization techniques, including Numba.
- Ensure users are aware of the policies regarding frontend node usage.
---

### 2022111842002093_Fwd%3A%20Likwid%20CACHES_MEM%20does%20not%20give%20any%20MEM%20values.md
# Ticket 2022111842002093

 # HPC Support Ticket: Likwid MEM Counters Issue

## Keywords
- Likwid
- MEM HPM counters
- Cascade Lake CPUs
- Intel Xeon Platinum 9242
- Intel Xeon Silver 4210
- perf_event
- /proc/sys/kernel/perf_event_paranoid

## Issue
- **Root Cause**: MEM HPM counters in Likwid are set to zero on Cascade Lake CPUs.
- **Affected CPUs**: Intel Xeon Platinum 9242, Intel Xeon Silver 4210.

## Troubleshooting Steps
1. **Check LIKWID access mode**: Verify the access mode used for LIKWID.
2. **Check LIKWID installation**: Confirm how LIKWID was installed.
3. **Check `perf_event_paranoid` value**: If access mode is `perf_event`, ensure `/proc/sys/kernel/perf_event_paranoid` is set to 0.

## Solution
- Re-run the commands on the affected nodes with `-V 3` to provide detailed output.
- Ensure `/proc/sys/kernel/perf_event_paranoid` is set to 0 to measure memory traffic in `perf_event` mode.

## Follow-up
- HPC Admins requested updates from the user regarding the issue resolution.

## General Learning
- Proper configuration of `perf_event_paranoid` is crucial for measuring memory traffic with LIKWID in `perf_event` mode.
- Detailed output (`-V 3`) can help diagnose issues with LIKWID.
---

### 2022050642002233_Tier3-Access-Fritz%20%22Wuyang%20Zhao%22%20_%20iwtm010h.md
# Ticket 2022050642002233

 # HPC-Support Ticket Conversation Analysis

## Keywords
- HPC Access
- Core Hours
- Multi-node Partition
- NHR Compute Time Proposal
- Molecular Dynamics Simulations
- Finite Element Simulations
- LAMMPS
- deal.II
- Emmy Cluster
- Meggie Cluster
- Fritz Cluster

## General Learnings
- **Account Activation**: Accounts can be enabled on specific clusters (e.g., Fritz).
- **Resource Availability**: Multi-node partitions may be temporarily unavailable due to benchmarking activities (e.g., HPL and HPCG submissions for the Top500 list).
- **Core Hour Limits**: Free tier access has limits on core hours. Exceeding this limit requires submitting a compute time proposal.
- **Historical Usage**: Users can request information about their past core hour usage to estimate future needs.
- **Software Requirements**: Users may need specific software (e.g., LAMMPS, deal.II) for their simulations.

## Root Cause of the Problem
- The user requested access to the Fritz cluster and needed information about their past core hour usage to discuss a potential compute time proposal with their supervisor.

## Solution
- The HPC Admin enabled the user's account on Fritz.
- The HPC Admin provided historical core hour usage data for the years 2020, 2021, and the current year.
- The user was advised to ask their supervisor to submit an NHR compute time proposal due to the high core hour requirement.

## Additional Notes
- The multi-node partition on Fritz was temporarily unavailable due to benchmarking activities.
- The user's work involved molecular dynamics and finite element simulations for polymers and nanocomposites, requiring specific software and computational resources.

This documentation can be used to assist other users with similar requests or issues related to HPC access, resource availability, and compute time proposals.
---

### 2024041042003179_Aktivierung%20der%20a100multi%20QOS.md
# Ticket 2024041042003179

 ```markdown
# HPC Support Ticket: Activation of a100multi QOS

## Keywords
- QOS activation
- a100multi
- Group access
- Performance warnings
- Job scheduling

## Summary
A user requested the activation of the `a100multi` QOS for their group (`v104dd`). The HPC Admin granted the request and provided important warnings and information regarding performance and job scheduling.

## Root Cause
The user needed access to the `a100multi` QOS for their group to utilize specific resources.

## Solution
The HPC Admin activated the `a100multi` QOS for the group `v104dd`.

## Additional Information
1. **Performance Warnings**:
   - The system is designed for throughput workloads, using the in-box RHEL OFED-Stack instead of MOFED.
   - GPU-direct functionality may be limited or non-existent, leading to performance degradation, especially in multi-node jobs.

2. **Job Scheduling**:
   - High system utilization may result in longer wait times for multi-node jobs.
   - Administrative holds may be placed on multi-node jobs to manage system load and reduce unnecessary idle time.

3. **Resource Availability**:
   - Limited resources are available due to shared hardware and pending dedicated hardware delivery.

## Conclusion
The `a100multi` QOS was successfully activated for the group `v104dd`. Users should be aware of potential performance issues and job scheduling delays.
```
---

### 2021053142001126_Yambo%20Job%20Emmy%201466187%20%28phyv018h%29.md
# Ticket 2021053142001126

 ```markdown
# HPC Support Ticket: Yambo Job Emmy 1466187 (phyv018h)

## Keywords
- Job script
- OpenMP threads
- MPI tasks
- Resource allocation
- Yambo
- HPC resources
- Efficiency

## Root Cause
- The user requested 3 nodes with 20 cores each but used 16 OpenMP threads with 60 MPI tasks, resulting in 960 threads on 60 cores.
- This configuration caused the job to run inefficiently because the number of threads exceeded the number of physical cores.

## Solution
- Ensure that the product of `OMP_NUM_THREADS` and MPI tasks does not exceed the number of physical cores.
- Avoid using 16 OpenMP threads on Emmy as it is inefficient.
- Consult with the supervisor or 2nd Level Support team for the correct usage of Yambo and HPC resources.

## General Learning
- Properly configure job scripts to match the available resources.
- Balance the number of OpenMP threads and MPI tasks to optimize performance.
- Seek guidance from supervisors or support teams for efficient use of HPC resources.
```
---

### 42287805_Random%20file%20read%20errors%20in%20parallel%20filesystem.md
# Ticket 42287805

 # HPC Support Ticket: Random File Read Errors in Parallel Filesystem

## Keywords
- File read errors
- Parallel filesystem
- Intel MPI libraries
- OpenMPI
- Thread safety
- Compiler optimization

## Summary
A user reported job crashes due to file read errors in the parallel filesystem. The user recently switched to Intel MPI libraries from OpenMPI due to segmentation faults. The issue was suspected to be related to thread safety or compiler optimization.

## Root Cause
The root cause of the problem was likely related to the compiler-level optimization of Intel 14 series compilers, which may have broken some file read/write loops.

## Solution
The user recompiled the program using Intel 13 compilers and disabled threading for the specific I/O routine (i.e., compilation without `-openmp` and with `-O1`). This resolved the file read errors.

## Lessons Learned
- Compiler-level optimizations can sometimes introduce issues in file read/write operations.
- Disabling threading for I/O routines can help mitigate such issues.
- It is not always possible to confirm filesystem failures after the fact.

## Actions Taken
- The user provided details about the error and the context in which it occurred.
- The HPC Admin requested the exact error message to better diagnose the issue.
- The user recompiled the program with different settings and reported that the issue was resolved.

## Follow-Up
The user will monitor for any recurrence of the issue and inform the HPC support team if it happens again.

---

This documentation can be used to troubleshoot similar file read errors in the future.
---

### 2022032542000275_2-node%20jobs%20on%20Emmy%20-%20iwtm033h.md
# Ticket 2022032542000275

 # HPC Support Ticket Analysis: 2-Node Jobs on Emmy

## Keywords
- 2-node jobs
- Emmy cluster
- Resource utilization
- Monitoring
- Job optimization

## Summary
- **Issue**: User running multiple 2-node jobs on Emmy cluster with low resource utilization.
- **Root Cause**: Jobs were using only 10 cores per node and not fully utilizing main memory or floating point units.
- **Admin Action**: HPC Admin inquired about the reason for running on two nodes and provided monitoring data.
- **Resolution**: No response from the user, but jobs were later observed to be running as single-node jobs.

## Lessons Learned
- **Resource Efficiency**: Ensure jobs are optimized to use resources efficiently.
- **Communication**: Proactive communication with users about resource usage can lead to better job scheduling.
- **Monitoring**: Regular monitoring of job performance can help identify inefficient resource usage.

## Recommendations
- **User Education**: Educate users on optimal job configuration to maximize resource utilization.
- **Follow-Up**: Follow up with users who do not respond to initial inquiries to ensure issues are resolved.

## Next Steps
- Continue monitoring job performance and resource utilization.
- Provide training sessions or documentation on efficient job configuration.
---

