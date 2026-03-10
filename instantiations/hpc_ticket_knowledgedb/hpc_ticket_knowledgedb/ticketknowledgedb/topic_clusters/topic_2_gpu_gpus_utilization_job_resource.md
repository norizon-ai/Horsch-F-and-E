# Topic 2: gpu_gpus_utilization_job_resource

Number of tickets: 512

## Tickets in this topic:

### 2019051042000564_HPC-Zugang%20f%C3%83%C2%BCr%20Google%20Summer%20of%20Code-Studierende.md
# Ticket 2019051042000564

 # HPC-Support Ticket: GPU Access for Google Summer of Code Students

## Keywords
- Google Summer of Code
- GPU resources
- Deep Learning
- TinyGPU cluster
- Infiniband
- Multi-node jobs
- GPU availability

## Summary
A research cooperative has been allocated 20 students for the Google Summer of Code, focusing on Deep Learning projects. The students require access to GPU resources. The conversation involves discussions about the availability and suitability of GPU nodes at the FAU HPC facility.

## Root Cause of the Problem
- Students need GPU resources for Deep Learning projects.
- Concerns about the availability and performance of GPU nodes.
- Questions about the interconnect (Infiniband) and multi-node job capabilities.

## Discussion Points
- **GPU Availability**: Some GPU nodes are reserved for specific groups, while others are available to the general user base.
- **Interconnect**: TinyGPU nodes are not connected via Infiniband, only Gigabit Ethernet.
- **Multi-Node Jobs**: Not allowed on TinyGPU due to the lack of high-speed interconnect.
- **CPU Alternatives**: Discussion about using more CPU nodes as an alternative to GPUs.

## Solution
- **GPU Nodes**: The following nodes are available for general use:
  - tg034-tg037 (1080 without Ti)
  - tg047-tg049 (1080 Ti)
  - tg071-073 (V100, subject to availability)
- **CPU Nodes**: Consider using a higher number of CPU nodes as an alternative to GPUs.
- **Networking**: Be aware that TinyGPU nodes are not connected via Infiniband, limiting multi-node job capabilities.

## Conclusion
The HPC support team provided information on available GPU nodes and their limitations. The students can use the specified GPU nodes for their projects, with the understanding that multi-node jobs are not supported on TinyGPU. Alternatively, using more CPU nodes is a viable option for some tasks.

## Notes
- The availability of GPU nodes can vary, and some nodes may be temporarily available but subject to change.
- The HPC support team can provide further assistance if needed.

---

This report summarizes the key points and solutions discussed in the HPC-Support Ticket conversation regarding GPU access for Google Summer of Code students.
---

### 2024080642004571_My%20code%20is%20getting%20terminated.md
# Ticket 2024080642004571

 ```markdown
# HPC Support Ticket: Code Termination Issue

## Subject
My code is getting terminated

## User Issue
- User's code is getting terminated after 6-8 hours of running on the CPU.
- User has tried running the code in different directories (`&home`, `&valut`, `&work`) with the same issue.
- User believes there is nothing wrong with the code.

## HPC Admin Observations
- User's jobs are requesting GPUs but not utilizing them.
- Most jobs are interactive and running into time limits.
- User's last two interactive jobs completed after 1 hour.

## Root Cause
- User was running CPU-intensive jobs on a GPU-allocated system (TinyGPU).
- Interactive sessions were hitting the time limit, causing job termination.

## Solution
- User should run CPU-intensive jobs on systems like `woody` instead of `TinyGPU`.
- User should submit jobs using `sbatch` instead of running them in interactive sessions to avoid time limits.

## Additional Information
- User was provided with a repository link for cluster onboarding: [i5_cluster_onboarding](https://gitos.rrze.fau.de/ym60imaq/i5_cluster_onboarding)
- User was advised to login to `woody` and `tinyGPU` using the same SSH configuration.
- User confirmed that the issue was due to time limits in interactive sessions and will use appropriate systems for future jobs.

## Keywords
- Code termination
- Interactive jobs
- Time limit
- GPU allocation
- CPU-intensive jobs
- `woody`
- `TinyGPU`
- `sbatch`
- `salloc`
```
---

### 2023042042002868_Best%20Practices%20GPU%20usage%20-%20iwi5106h.md
# Ticket 2023042042002868

 # HPC Support Ticket: Best Practices GPU Usage

## Keywords
- GPU optimization
- GPU memory utilization
- Batch size
- Data loading
- Prefetching
- GPU kernels
- A100 GPUs
- NVLink
- Batch script flags

## Problem Description
- User experiencing oscillating GPU performance despite high GPU memory utilization.
- Specs: 70Gb dataset, 10 workers in DataLoader, prefetch factor 2, batch size 10.
- Data is copied to GPU in a blocking fashion (`x.cuda()` in PyTorch).

## Root Cause
- Possible GPU stalling due to data loading during the training loop.
- Inefficient memory copy between CPU and GPU.
- Small GPU kernels due to limited batch size.

## Solutions and Recommendations
- **Data Loading**: Ensure data is preloaded before the training loop to avoid stalling.
- **Prefetching**: Utilize prefetchers to overlap memory copy and training.
- **Batch Size**: Increase batch size for better GPU utilization, if memory allows.
- **GPU Selection**: Use 80GB A100 GPUs for larger batch sizes and model architectures.
  - Flag in batch script: `-C a100_80` to ensure allocation of 80GB A100.
- **Cluster**: Note that 80GB A100s are available on the Alex cluster, not the tiny cluster.

## General Learnings
- Efficient data loading and prefetching are crucial for optimal GPU performance.
- Larger batch sizes improve GPU utilization by increasing the size of GPU kernels.
- Specific GPU types can be requested using flags in batch scripts.
- Understanding the cluster's hardware capabilities is important for resource allocation.

## Follow-up Actions
- Monitor GPU performance after implementing the recommended changes.
- Consider further tuning of DataLoader parameters if performance issues persist.
---

### 2022033142001628_Job%20on%20TinyGPU%20only%20uses%20one%20GPU%20%5Biwal047h%5D.md
# Ticket 2022033142001628

 # HPC Support Ticket: Job on TinyGPU Only Uses One GPU

## Keywords
- TinyGPU cluster
- GPU allocation
- Resource usage
- Job monitoring
- Slurm job

## Summary
A user was running multiple jobs on the TinyGPU cluster, allocating four GPUs per job. However, the jobs were only utilizing one GPU each, leading to inefficient resource usage.

## Root Cause
- The user's code was not optimized to utilize all allocated GPUs.

## Solution
- The HPC Admin advised the user to allocate only as many GPUs as their code can actually use to avoid wasting resources.
- The issue was resolved as subsequent jobs showed improved GPU utilization.

## Lessons Learned
- Always ensure that the number of GPUs allocated matches the actual usage of the code to optimize resource allocation.
- Regular monitoring of job performance can help identify and rectify inefficient resource usage.

## Actions Taken
- The HPC Admin notified the user about the inefficient GPU usage and provided screenshots from the monitoring system.
- The ticket was closed after observing improved job performance.

## References
- [Slurm Job Monitoring](http://wadm1.rrze.uni-erlangen.de/cgi-bin/cluster-status/show-slurm-job-tg.pl?jobid=239401)
- HPC Services Contact: [support-hpc@fau.de](mailto:support-hpc@fau.de)
- HPC Website: [http://hpc.fau.de/](http://hpc.fau.de/)
---

### 2020062942002782_HPC%20storage_usage.md
# Ticket 2020062942002782

 # HPC Storage/Usage Support Ticket Conversation

## Keywords
- HPC storage
- Deep Learning
- MIMIC-III database
- TinyGPU
- GPU extensions
- Zoom meeting
- Storage capacity
- Priority access

## Summary
A user is planning a Master's thesis project involving the processing of Electronic Health Records (EHR) with continuous physiological signals using the MIMIC-III database. The project requires significant storage and computational resources for deep learning tasks. The user seeks advice on the best solution for the project and inquires about the possibility of a dedicated server.

## Key Points Learned
- **Project Requirements**:
  - Total data: < 2.6 TB
  - EHR: 6.5 GB
  - Physiological signals: 2.5 TB
  - Methodology: Deep Learning

- **Initial Recommendations**:
  - Use TinyGPU for GPU-intensive tasks.
  - Download data in batches to $WORK in the HPC-Basisversorgung.
  - Consider renting additional storage if needed.

- **GPU Extension Options**:
  - Geforce RTX2080 Ti Knoten: ~11k EUR
  - Geforce RTX2080 Ti Knoten with AMD CPUs: ~10k EUR
  - NVIDIA A100: ~52k EUR
  - Tesla V100: ~40k EUR (less attractive since A100 availability)

- **Financing and Integration**:
  - Financing groups get prioritized access.
  - Nodes must integrate with TinyGPU.
  - HPC group handles procurement and legal aspects.
  - No additional costs for RRZE services and node operation.

- **Storage Considerations**:
  - Storage capacity for the project remains unchanged initially.
  - Possibility to convert part of the priority into storage capacity.

- **Meeting and Communication**:
  - Multiple Zoom meetings were scheduled to discuss options and details.
  - User invited colleagues to the meetings.

## Root Cause of the Problem
The user requires significant computational and storage resources for a deep learning project and seeks the best solution within the HPC environment.

## Solution
- **Initial Steps**:
  - Submit HPC applications and assess initial progress.
  - Use TinyGPU for GPU tasks and batch download data to $WORK.

- **Long-term Solution**:
  - Consider financing a GPU extension for prioritized access.
  - Discuss storage capacity needs and potential conversion of priority into storage.

- **Communication**:
  - Schedule Zoom meetings with HPC admins to discuss details and options.
  - Involve colleagues in the decision-making process.

This documentation can be used to assist other users with similar requirements and to guide HPC support employees in providing appropriate solutions.
---

### 2023050342003138_Tier3-Access-Alex%20%22Mikhail%20Kulyabin%22%20_%20iwi5063h.md
# Ticket 2023050342003138

 # HPC Support Ticket: Tier3-Access-Alex

## Keywords
- HPC Account Activation
- Alex Cluster
- Nvidia A100 GPUs
- GPU-hours Allocation
- PhD Research
- Stable Diffusion Models
- Medical Domain
- Synthetic Datasets
- OCT Images

## Summary
- **User Request**: Access to GPGPU cluster 'Alex' for PhD research.
- **Resources Requested**: 3000 GPU-hours (4 GPUs per job, 15 hours per job, 50 jobs).
- **Software**: Already set up on HPC.
- **Application**: Training stable diffusion models in the medical domain.
- **Expected Results**: Synthetic datasets of OCT images with different diseases.

## Actions Taken
- **HPC Admin**: Enabled the user's HPC account on Alex.

## Lessons Learned
- Ensure proper account activation for new users.
- Verify resource allocation requests and expected usage.
- Confirm that the required software is already installed on the HPC system.

## Root Cause (if applicable)
- User needed access to the HPC cluster for research purposes.

## Solution
- HPC Admin enabled the user's account on the Alex cluster.

## Follow-up
- Monitor the user's resource usage to ensure it aligns with the requested allocation.
- Provide support for any software or technical issues that may arise during the user's research.
---

### 2024030742003847_Multi%20GPU%20jobs.md
# Ticket 2024030742003847

 ```markdown
# Multi GPU Jobs Support Ticket

## Keywords
- Multi GPU jobs
- SLURM
- Julia
- CUDA
- MPI
- Proxy servers
- cgroups
- GPU ID

## Summary
A user encountered issues running a Julia script on multiple GPUs using SLURM. The script worked on a local workstation with `mpiexec` but did not function correctly on the HPC cluster.

## Root Cause
1. **SLURM Configuration**: The user did not set the `--ntasks` option in the SLURM header.
2. **Package Downloads**: Julia attempted to download packages, which was not allowed on compute nodes.
3. **GPU ID Assignment**: Each process was assigned GPU ID 0 despite being different physical GPUs.

## Solutions
1. **SLURM Configuration**:
   - Set `--ntasks` in the SLURM header.
   - Use `srun` to run the job:
     ```bash
     srun julia script.jl
     ```
   - Alternatively, use:
     ```bash
     srun -n $SLURM_NTASKS --gpus-per-task=1 julia script.jl
     ```

2. **Package Downloads**:
   - Use proxy servers to enable internet access on compute nodes for package downloads.
   - Reference: [FAQ on HTTP/HTTPS Timeout](https://doc.nhr.fau.de/faq/#why-does-my-application-give-an-http-https-timeout)

3. **GPU ID Assignment**:
   - Understand that SLURM assigns GPU ID 0 to simplify management within cgroups.
   - Consider using `--gpu-bind=none` to potentially avoid cgroup restrictions, though behavior may vary.

## Additional Notes
- The user successfully ran the application on 4 GPUs after resolving the package download issue.
- The GPU ID assignment behavior is a feature of SLURM and cannot be easily deactivated.

## References
- [Example SLURM Job Scripts](https://doc.nhr.fau.de/batch-processing/job-script-examples-slurm/)
- [FAQ on HTTP/HTTPS Timeout](https://doc.nhr.fau.de/faq/#why-does-my-application-give-an-http-https-timeout)
```
---

### 2021111942000728_Alex.md
# Ticket 2021111942000728

 # HPC-Support Ticket Conversation Analysis

## Keywords
- Early adopter registration
- Compute time request
- Multi-GPU job submission
- A100 GPUs
- SLURM job script
- Node configuration error

## General Learnings
- Users may need guidance on registering as early adopters and estimating compute time.
- Proper configuration of SLURM job scripts is crucial for successful job submission.
- Understanding the hardware limitations of the cluster nodes is important for job script configuration.

## Root Cause of User's Problem
- The user requested an unavailable node configuration (8 A100 GPUs per node) in the SLURM job script.

## Solution
- Adjust the SLURM job script to request the correct number of GPUs per node (4 A100 GPUs) using the `--gres=gpu:a100:4` option.

## Support Interaction Summary
- **User:** Requested help with early adopter registration and compute time estimation.
- **HPC Admin:** Advised that compute time estimation is not crucial and encouraged the user to register.
- **User:** Encountered an error while submitting a multi-GPU job using A100 GPUs.
- **HPC Admin:** Identified the issue as an incorrect node configuration request and provided the correct configuration.
- **User:** Acknowledged the solution and agreed to complete the early adopter registration.
- **HPC Admin (Follow-up):** Reminded the user to submit the early adopter registration form.
- **User:** Confirmed they would complete the registration.

## Relevant Links
- [Early Adopter Registration Form](https://hpc.fau.de/early-adopter-alex/)

## Notes for Support Employees
- When assisting users with job script errors, verify the requested node configuration against the available hardware.
- Encourage users to complete necessary registrations and provide guidance on compute time estimation when needed.
- Ensure users are aware of the correct SLURM job script options for their specific use case.
---

### 2023053042001099_Job%20with%20high%20RAM%20requirement.md
# Ticket 2023053042001099

 # HPC Support Ticket: Job with High RAM Requirement

## Keywords
- High RAM requirement
- GPU memory
- Job script
- SLURM
- A100 GPU
- Idle GPU

## Problem
- User requires ~60 GB of GPU memory and ~400 GB of normal RAM for a deep learning job.
- The job is expected to run for less than one hour.
- The current cluster setup does not provide sufficient RAM when requesting a single A100 GPU.

## Solution
- The user needs to request two GPUs to get the required amount of RAM, even though one GPU will remain idle.
- Add the following line to the job script to request the appropriate node:
  ```bash
  #SBATCH -C a100_80
  ```
- Include a comment in the job script mentioning that the second GPU will be idle but is needed due to host memory requirements.

## Notes
- If the job could run without a GPU, other nodes with up to 1 or 2 TB of main memory could be used.
- The idle GPU is considered acceptable due to the short run time of the job.

## Relevant Documentation
- [Alex Cluster Documentation](https://hpc.fau.de/systems-services/documentation-instructions/clusters/alex-cluster/)

## Roles Involved
- HPC Admins
- 2nd Level Support Team
- Head of the Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support
- Software and Tools Developer
---

### 2023100442003699_Tier3-Access-Alex%20%22Mathias%22%20_%20iwi5093h.md
# Ticket 2023100442003699

 # HPC Support Ticket Analysis: Tier3-Access-Alex

## Keywords
- Tier3 Access
- Alex GPGPU Cluster
- NHR Application
- GPU-hours
- Software Requirements (Pytorch, CUDA, cudNN, conda)
- Application (Scene Recognition, Object Detection, Style Transfer)
- Expected Results
- Contingent Limits

## Summary
A user requested access to the Alex GPGPU cluster for training models with large datasets. The request was denied due to the user's department already exhausting their Tier3 contingent.

## Root Cause
- The user's department (iwi5) has already fully utilized their Tier3 contingent on the Alex cluster.

## Solution
- The user was advised to submit an NHR application to gain access to the Alex cluster.
- Details on the NHR application process were provided via a link to the documentation.

## General Learnings
- Departments have limited Tier3 contingents for HPC resources.
- Users must submit an NHR application if their department's Tier3 contingent is exhausted.
- The NHR application process is documented and available for users to follow.

## Additional Notes
- The user had no prior usage on TinyGPU and was only active on Woody CPU-only.
- The user's request included specific software requirements and expected outcomes for their project.

## Relevant Links
- [NHR Application Rules](https://hpc.fau.de/systems-services/documentation-instructions/nhr-application-rules/)

## Support Roles
- **HPC Admins**: Johannes Veh
- **2nd Level Support Team**: Not directly involved in this ticket.
- **Head of the Datacenter**: Gerhard Wellein
- **Training and Support Group Leader**: Georg Hager
- **NHR Rechenzeit Support**: Harald Lanig
- **Software and Tools Developer**: Jan Eitzinger, Gruber

This documentation can be used to address similar issues related to Tier3 access and NHR applications.
---

### 2024071642003037_Tier3-Access-Alex%20%22Saskia%20Prusch%22%20_%20bccc120h.md
# Ticket 2024071642003037

 # HPC Support Ticket Analysis

## Subject
Tier3-Access-Alex

## Keywords
- HPC Account Activation
- Alex Cluster
- Nvidia A100 GPGPUs
- Nvidia A40 GPGPUs
- LAMMPS
- Python
- MD Simulations

## Summary
A user requested access to the Alex cluster for MD simulations using LAMMPS and Python. The request was initially deemed non-specific but was granted due to the group's extensive use of HPC resources.

## Root Cause
The user required access to the Alex cluster for MD simulations but did not specify the exact computational time needed.

## Solution
The HPC Admin enabled the user's account on the Alex cluster.

## What Can Be Learned
- **Account Activation**: HPC Admins can enable user accounts on specific clusters upon request.
- **Cluster Specifications**: Alex cluster supports Nvidia A100 and A40 GPGPUs.
- **Software Support**: LAMMPS and Python are supported for MD simulations.
- **Handling Vague Requests**: Even if a request is not highly specific, it can be granted based on the group's history of HPC usage.

## Additional Notes
- The user did not specify the exact computational time needed, which is acceptable in some cases.
- The request was handled by the HPC Admin, who provided the necessary access.

---

This information can be used to handle similar requests for account activation and to understand the process of enabling access to specific HPC clusters.
---

### 2024021942002952_Access%20from%20Bayreuth%20-%20Arne%20Spang_Geoinstitute.md
# Ticket 2024021942002952

 # HPC Support Ticket: Access from Bayreuth - GPU Resources Request

## Keywords
- GPU resources
- Julia codes
- NHR projects
- Tier3-Grundversorgung
- Annual compute time
- FAU resources
- Bayreuth Cluster

## Problem
- User is a postdoctoral researcher at the Bavarian Geoinstitute in Bayreuth.
- User requires GPU resources for running Julia codes (single-GPU and multi-GPU).
- Bayreuth Cluster has limited GPU resources.
- User is unsure about the process to access FAU resources and the nature of NHR projects.

## Solution
- If the user's annual compute time demand is below 10,000 GPU-h, Dr. Winkler from the T Servicezentrum can send an invitation to include the user in "Tier3-Grundversorgung Uni-Bayreuth (via IT-Servicezentrum)".
- User confirmed that 10,000 GPU-h will be sufficient for their needs.

## General Learnings
- FAU provides access to GPU resources for external researchers through the "Tier3-Grundversorgung" program.
- NHR projects are typically for larger amounts of computing time, while general access can be granted for smaller demands.
- Users from other institutions can access FAU resources by coordinating with the IT-Servicezentrum.

## Next Steps
- User should wait for an invitation from Dr. Winkler to be included in the "Tier3-Grundversorgung Uni-Bayreuth" program.
- If additional compute time is needed in the future, the user may need to explore NHR projects or other grant options.
---

### 2020021242003024_%5Btinygpu%5D%20job%20violates%20usage%20limit.md
# Ticket 2020021242003024

 ```markdown
# HPC Support Ticket: Job Violates Usage Limit

## Keywords
- TinyGPU
- Usage Limit
- JobID Underscore
- GTX 980
- Job Script
- Node Occupation
- Group Limits

## Summary
A user submitted a 12-hour job on a TinyGPU's GTX 980 node and noticed that the job's JobID had an underscore, indicating a usage limit violation. The user was unsure which limits were violated.

## Root Cause
- The user's job was running and had already been active for more than 25 minutes when the ticket was submitted.
- The user's group (mpt4) was occupying 3 out of the 6 non-user-funded nodes, which is 50% of the available non-user-funded nodes.
- The HPC Admin mentioned that 34 out of 40 nodes in TinyGPU were paid by individual user groups, and the user's group had not contributed financially.

## Solution
- The HPC Admin noted that the limits for the user's group (mpt4) on TinyGPU were slightly relaxed, despite the group having their own GPU resources.
- No specific action was required from the user, as the job was already running and the limits were adjusted by the HPC Admin.

## Lessons Learned
- Users should be aware of the usage limits and the financial contributions of different groups to the HPC resources.
- The underscore in the JobID indicates a usage limit violation, which can be due to various factors such as job duration or node occupation.
- The HPC Admin can adjust limits based on the overall usage and group contributions.

## References
- Ticket#2018071342001887
- Ticket#2018083142001127
```
---

### 2023051242000285_Job%20on%20Alex%20does%20not%20use%20GPU%20%5Biwi5046h%5D.md
# Ticket 2023051242000285

 ```markdown
# HPC Support Ticket: Job on Alex does not use GPU

## Keywords
- GPU utilization
- JobID
- srun
- nvidia-smi
- resource allocation

## Problem
- User's job on Alex (JobID 734630) uses only one GPU out of the four allocated GPUs.

## Root Cause
- The job is not efficiently utilizing the allocated GPU resources.

## Solution
- **Monitoring**: Use `srun --pty --overlap --jobid YOUR-JOBID bash` to attach to the running job and `nvidia-smi` to check GPU utilization.
- **Resource Allocation**: Ensure that jobs only allocate nodes with GPUs if the code can make use of them.

## Lessons Learned
- Always verify GPU utilization to avoid idle resources.
- Properly allocate resources based on job requirements to optimize HPC usage.

## Follow-Up
- The issue was resolved as newer jobs (16.05) showed better GPU utilization.
```
---

### 2023102642002185_Tier3-Access-Alex%20%22Fei%20Wu%22%20_%20iwi5065h.md
# Ticket 2023102642002185

 ```markdown
# HPC Support Ticket Conversation Summary

## Subject: Tier3-Access-Alex "Fei Wu" / iwi5065h

### Key Points Learned:

- **Account Status**: User's account is still permitted to use Alex.
- **GPU Time Request**: 8000 GPU hours requested, which exceeds Tier3 budget.
- **Storage Requirements**:
  - $HOME: No increased quota provided, used for imported data only.
  - $WORK and $VAULT: Increased quota possible.
  - NHR-application accounts come with a project quota of 10 TB at $WORK.
- **Inactivity**: User's account was inactive for more than 3 months, leading to data deletion.
- **File Management**: Large volume of small files can hurt file servers and limit access speed.
  - Recommended solutions: TensorFlow's TFRecord, ordered tar files as used by WebDataset.
- **Performance Issues**: Bad data access patterns can slow down file access on $WORK.

### Actions Taken:

- **Quota Increase**: User requested and was granted increased quota for $WORK (2TB) and $VAULT (2TB).
- **NHR-Application**: User completed and submitted the NHR-application form.

### Root Cause of Problems:

- **Excessive GPU Time Request**: User requested GPU time far beyond the Tier3 budget.
- **File Management**: User planned to generate a large volume of small files, which could impact file server performance.

### Solutions:

- **GPU Time**: User advised to submit an NHR-application to ensure resource availability.
- **File Management**: User advised to use aggregates like TensorFlow's TFRecord or ordered tar files to reduce the number of individual files.

### General Learnings:

- **Resource Allocation**: Understanding the limitations of Tier3 budgets and the need for NHR-applications for extensive resource requirements.
- **File Server Performance**: Importance of managing file sizes and access patterns to maintain optimal performance on shared file systems.

### Ticket Status:

- **NHR-Application**: Being processed in a separate ticket.
- **Original Ticket**: Closed after addressing quota increase and providing guidance on file management.
```
---

### 2020100242002298_Resource%20utilization%20on%20TinyGPU%20_%20iwso015h.md
# Ticket 2020100242002298

 # HPC Support Ticket Analysis: Resource Utilization on TinyGPU

## Subject
Resource utilization on TinyGPU / iwso015h

## Keywords
- Resource utilization
- GPU
- TinyGPU
- Job request
- System monitoring
- nvidia-smi

## Root Cause of the Problem
The user's job on TinyGPU (job ID: 511360 - run.sh) requests two GPUs but only utilizes one. The second GPU remains idle.

## Evidence
- **System Monitoring Graph:** Shows that only one GPU is being used.
- **nvidia-smi Output:** Confirms that GPU 0 is utilized while GPU 1, 2, and 3 are idle.

```
|   0  GeForce GTX 1080    On   | 00000000:02:00.0 Off |                  N/A |
| 35%   52C    P2    43W / 180W |   7845MiB /  8119MiB |     16%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
|   1  GeForce GTX 1080    On   | 00000000:03:00.0 Off |                  N/A |
| 27%   32C    P8     7W / 180W |    109MiB /  8119MiB |      0%      Default |
|                               |                      |                  N/A |
```

## Solution
- **Adjust Job Request:** Modify the job script to request only the number of GPUs actually needed.
- **Optimize Resource Allocation:** Ensure that the job script efficiently utilizes the allocated resources to avoid wastage.

## General Learning
- **Efficient Resource Utilization:** Always request only the resources that are necessary for the job to avoid wasting computational resources.
- **Monitoring Tools:** Use system monitoring tools and `nvidia-smi` to verify resource utilization and identify inefficiencies.

## Next Steps for Support
- **User Guidance:** Provide guidance to the user on how to modify their job script to request the appropriate number of GPUs.
- **Documentation Update:** Update documentation to include best practices for efficient resource utilization on TinyGPU.

---

This report aims to assist HPC support employees in identifying and resolving similar resource utilization issues in the future.
---

### 2021030342003314_Jobs%20auf%20den%20A100-Knoten%20-%20iwi3047h.md
# Ticket 2021030342003314

 # HPC Support Ticket: Jobs auf den A100-Knoten

## Keywords
- A100-Knoten
- CPU-only Jobs
- GPU Nutzung
- Cluster Auslastung
- Parallelisierung
- Laufzeiten
- AMD Epyc 7662
- TinyFAT-Nodes

## Problem
- User führt CPU-only Jobs auf A100-Knoten aus, die eigentlich für GPU-Nutzung vorgesehen sind.
- User benötigt starke CPUs für quantisierte Inferenz und ist sich der Problematik bewusst, dass dies die Nutzung der A100-Knoten für andere GPU-Nutzer einschränken könnte.

## Root Cause
- User nutzt A100-Knoten für CPU-intensive Aufgaben, obwohl diese Knoten primär für GPU-Nutzung gedacht sind.
- User ist sich der hohen Auslastung der A100-Knoten nicht bewusst und möchte eine Möglichkeit finden, die Auslastung zu überprüfen.

## Lösung
- **Auslastung überprüfen**: Der User kann die Auslastung der A100-Knoten überprüfen, um bei hoher Auslastung von der Nutzung abzusehen.
- **Alternative Knoten**: Der User kann die neuen TinyFAT-Nodes (2x 32 Cores) nutzen, die ebenfalls eine hohe Anzahl an CPU-Kernen bieten (`sbatch -M tinyx`).
- **Vorwarnung**: Sobald die GPU-Nutzung zunimmt, werden CPU-only Jobs ohne Vorwarnung abgeschossen.

## Allgemeine Erkenntnisse
- **Kommunikation**: Eine klare Kommunikation zwischen User und HPC-Admin ist wichtig, um die Nutzung der Ressourcen effizient zu gestalten.
- **Ressourcenmanagement**: Es ist wichtig, dass User die richtigen Ressourcen für ihre Aufgaben nutzen, um die Effizienz des Clusters zu maximieren.
- **Alternativen**: Der Cluster bietet alternative Knoten mit ähnlicher Kernzahl, die für CPU-intensive Aufgaben genutzt werden können.

## Zusammenfassung
Der User führt CPU-only Jobs auf A100-Knoten aus, was die Nutzung dieser Knoten für GPU-Aufgaben einschränkt. Durch die Überprüfung der Auslastung und die Nutzung alternativer Knoten kann die Effizienz des Clusters verbessert werden.
---

### 2024011742001011_Tier3-Access-Alex%20%22Tobias%20Schwab%22%20_%20iwhf008h.md
# Ticket 2024011742001011

 # HPC Support Ticket Summary

## Keywords
- Tier3 Access
- Alex Cluster
- GPU-hours
- NHR Application
- Cuda 11.8
- Neural Network Training
- Radar Signal Processing

## Summary
- **User Request**: Access to Alex cluster for neural network training on radar signals.
- **Estimated GPU-hours**: 45,000 (A40) + 30,000 (A100) per year.
- **Software Needed**: Cuda 11.8.
- **Reason for Request**: Insufficient VRAM on TinyGPU and high occupancy of A100/V100 cards.

## HPC Admin Response
- **Access Granted**: User allowed to use Alex.
- **Usage Guidance**: Tier3 access is for low to moderate demand.
- **Potential NHR Application**: If usage is high, an NHR application may be required.

## General Learnings
- **Tier3 Access**: Suitable for users with low to moderate demand.
- **High GPU-hour Requests**: May necessitate an NHR application.
- **Cluster Usage**: Alex cluster is used for neural network training and other computationally intensive tasks.

## Root Cause of Problem
- **Insufficient Resources**: TinyGPU's resources were insufficient for the user's needs.

## Solution
- **Access to Alex**: User granted access to Alex cluster to meet their computational demands.

## References
- [NHR Application Rules](https://hpc.fau.de/systems-services/documentation-instructions/nhr-application-rules/)

---

This summary provides a quick reference for support employees to understand the context and resolution of similar access requests and resource allocation issues.
---

### 2024053142001139_NVLink%20on%20Alex.md
# Ticket 2024053142001139

 # HPC Support Ticket: NVLink on Alex

## Keywords
- NVLink
- A40
- A100
- Alex cluster
- CPU-GPU interconnect
- PCIe

## Problem
- User needed information on CPU-GPU interconnect for A40 and A100 GPUs on the Alex cluster.
- Misinterpretation of the interconnect field in the documentation led to confusion.

## Root Cause
- The documentation was unclear regarding the interconnect for A40 GPUs.
- User misread the empty interconnect field for A40 as NVLink.

## Solution
- **A100 GPUs**: NVLink is used for GPU-to-GPU communication within a node.
- **A40 GPUs**: PCIe-only, no NVLink bridge.
- **CPU-GPU Communication**: PCIe 4.0 x16 is used for CPU-GPU communication for both A40 and A100 GPUs.

## Additional Information
- NVLink for CPU-GPU communication is not available on x86_64 based systems, but is available on systems like Grace-Hopper.
- The A100 nodes in Alex use the same Nvidia HGX Delta board as a DGX A100.

## References
- [NVLink Wikipedia](https://en.wikipedia.org/wiki/NVLink)
- [Nvidia NVLink Blog](https://blogs.nvidia.com/blog/what-is-nvidia-nvlink/)
- [Inspur NF5488A5 Review](https://www.servethehome.com/inspur-nf5488a5-8x-nvidia-a100-hgx-platform-review-amd-epyc/)
- [Slide 24 of NF5488A5 Presentation](https://iitd.com.ua/wp-content/uploads/2022/02/nf5488a5-eng.pdf)

## Conclusion
- Clarified the interconnect types for A40 and A100 GPUs.
- Provided references for further reading.
- Ensured the user understood the CPU-GPU communication method.
---

### 2023030242000922_Job%20on%20alex%20only%20using%20one%20node%20%5Bb114cb10%5D.md
# Ticket 2023030242000922

 # HPC Support Ticket: Job on Alex Only Using One Node

## Keywords
- JobID 691435
- Alex
- GPU utilization
- `srun --pty --jobid bash`
- `nvidia-smi`
- ClusterCockpit
- Monitoring data
- Runtime extension

## Summary
A user's job on Alex was only utilizing GPUs from the first node, leading to inefficient resource usage. The HPC Admins provided guidance on monitoring and managing the job.

## Root Cause
- The user's job was not properly utilizing the allocated GPU resources across multiple nodes.

## Solution
- The user was advised to check GPU utilization using `nvidia-smi` after attaching to the job with `srun --pty --jobid bash`.
- The user stopped the inefficient job and started a new one.
- The runtime of the new job was extended to five days upon the user's request.

## General Learnings
- Always ensure that jobs are efficiently utilizing allocated resources.
- Use monitoring tools like ClusterCockpit and `nvidia-smi` to check resource utilization.
- Communicate with HPC Admins for runtime adjustments and other job management tasks.
- Be mindful of resource allocation to avoid idle nodes and maximize system efficiency.
---

### 2023083142000681_Jobs%20on%20TinyGPU%20only%20use%201%20of%204%20allocated%20GPUs%20%5B.md
# Ticket 2023083142000681

 # HPC Support Ticket Conversation Analysis

## Subject: Jobs on TinyGPU only use 1 of 4 allocated GPUs

### Keywords:
- GPU utilization
- Job monitoring
- Resource allocation
- Wall time limit
- Code optimization

### Lessons Learned:
1. **GPU Utilization Monitoring**:
   - Users can attach to running jobs using `srun --pty --overlap --jobid YOUR-JOBID bash` to get a shell on the first node.
   - `nvidia-smi` can be used to check current GPU utilization.

2. **Resource Allocation**:
   - Ensure that allocated GPUs are being utilized effectively.
   - Avoid allocating GPU resources if the code does not make use of them to prevent idle resources.

3. **Wall Time Limit**:
   - The maximum wall time for jobs is 24 hours.
   - If jobs exceed this limit, they will fail.

4. **Code Optimization**:
   - HPC Admins may not have the expertise to optimize user code.
   - Users should consult their supervisors or other experts for code optimization.

### Root Cause of the Problem:
- The user's job was only utilizing 1 out of 4 allocated GPUs.
- Another job failed due to exceeding the 24-hour wall time limit.

### Solution:
- **GPU Utilization**: Ensure that the code is optimized to utilize all allocated GPUs.
- **Wall Time**: If a job requires more than 24 hours, consider breaking it into smaller tasks or optimizing the code to run within the time limit.

### Additional Notes:
- Always check for typos or errors in the code that might affect performance.
- Attach relevant files when seeking assistance to provide context for the issue.

This documentation can be used to address similar issues in the future, ensuring efficient resource utilization and job management on the HPC system.
---

### 2023082342001927_Tier3-Access-Alex%20%22Mamta%20K%20C%22%20_%20gwgi018h.md
# Ticket 2023082342001927

 # HPC Support Ticket Analysis

## Keywords
- GPU hours
- NHR project
- Supervisor consultation
- Account enablement

## Summary
- **User Request:** 30,000 GPU hours for simulation of glacier surface velocities using machine learning approaches.
- **HPC Admin Response:** 30,000 GPU hours exceed the free basic FAU Tier3 HPC service. Suggested discussing with the supervisor and considering an NHR project.
- **User Follow-up:** Requested 3,000 GPU hours as an interim solution.
- **HPC Admin Action:** Enabled the user's HPC account on Alex.

## Root Cause
- User requested an unrealistic amount of GPU hours for the free basic FAU Tier3 HPC service.

## Solution
- User was advised to discuss with the supervisor and consider applying for an NHR project.
- User's account was enabled on Alex for interim use.

## General Learnings
- Always verify the feasibility of resource requests with the available service limits.
- Consult with supervisors or project leads for large resource allocations.
- Consider applying for larger projects if the basic service limits are insufficient.

## Next Steps
- User should discuss with the supervisor and potentially apply for an NHR project.
- HPC Admins should monitor the user's GPU usage and provide further assistance if needed.
---

### 2025013042001682_Job%20on%20TinyGPU%20uses%20only%201%20of%202%20GPUs%20%5Biwi5227h%5D.md
# Ticket 2025013042001682

 # HPC Support Ticket: Job on TinyGPU Uses Only 1 of 2 GPUs

## Keywords
- GPU utilization
- TinyGPU
- JobID
- ClusterCockpit
- `nvidia-smi`
- Resource allocation

## Summary
A user's job on TinyGPU was only utilizing one of the two allocated GPUs.

## Root Cause
The user's job was not configured to utilize both allocated GPUs, leading to inefficient resource usage.

## Solution
1. **Monitoring GPU Utilization:**
   - Users can log into the monitoring system ClusterCockpit at [monitoring.nhr.fau.de](https://monitoring.nhr.fau.de/) to view GPU utilization.
   - Alternatively, users can attach to their running job using the command:
     ```bash
     srun --pty --overlap --jobid YOUR-JOBID bash
     ```
   - Once attached, users can run `nvidia-smi` to check the current GPU utilization.

2. **Efficient Resource Allocation:**
   - Ensure that jobs are configured to utilize all allocated GPUs.
   - Only allocate nodes with GPUs if the code can make use of them to avoid idle resources.

## General Learning
- Regularly monitor resource utilization to ensure efficient use of HPC resources.
- Use monitoring tools and commands like `nvidia-smi` to diagnose and optimize GPU usage.
- Properly configure jobs to utilize all allocated resources to prevent resource wastage.

## Contact Information
For further assistance, contact the HPC support team at [support-hpc@fau.de](mailto:support-hpc@fau.de).
---

### 2024021242002796_Jobs%20on%20Alex%20do%20not%20use%20allocated%20GPUs%20%5Bv101be14%5D.md
# Ticket 2024021242002796

 # HPC Support Ticket: Jobs on Alex Do Not Use Allocated GPUs

## Keywords
- GPU utilization
- Job submission
- Storage management
- Connection stability

## Problem Description
- User's jobs on the Alex cluster are not utilizing allocated GPUs.
- User has limited storage in $HOME directory.
- User experiences frequent disconnections from the login node.

## Root Cause
- Jobs were not compiled on nodes with GPUs.
- Some jobs are CPU-specific and do not require GPUs.

## Solution
- Ensure jobs are compiled on nodes with GPUs by submitting interactive jobs.
- Use `srun --pty --overlap --jobid YOUR-JOBID bash` to attach to running jobs and check GPU utilization with `nvidia-smi`.
- Move production data to the $WORK directory for more storage space.
- No solution for connection stability; it is an inherent issue.

## Additional Information
- Monitor GPU utilization via ClusterCockpit at [monitoring.nhr.fau.de](https://monitoring.nhr.fau.de/).
- Ensure CPU-specific jobs are submitted to appropriate queues if available.

## Follow-up
- User's jobs can stay on the Alex cluster for now.
- No action can be taken to improve connection stability.
---

### 2024080942001381_long%20staging_pre-processing%20time%20%5Bv103fe18%5D.md
# Ticket 2024080942001381

 ```markdown
# HPC Support Ticket: Long Staging/Pre-processing Time

## Subject
long staging/pre-processing time [v103fe18]

## Keywords
- Long staging/pre-processing time
- Job monitoring
- GPU utilization
- Data pre-processing
- ClusterCockpit
- srun
- nvidia-smi

## Issue Description
A job (JobID 1942462) is experiencing a staging/pre-processing time of approximately 15 hours. It is unclear whether this is due to a high load on the fileserver or data pre-processing.

## HPC Admin Response
- Requested user to comment on job activities and whether CPU-only resources are needed for data pre-processing.
- Provided a screenshot of the monitoring system and a link to ClusterCockpit for the user to view the job's performance.
- Suggested attaching to the running job using `srun --pty --overlap --jobid YOUR-JOBID bash` to check GPU utilization with `nvidia-smi`.

## Root Cause
Not explicitly identified in the provided conversation.

## Solution
- User should provide details on job activities.
- User should check GPU utilization using `nvidia-smi`.
- User should monitor job performance via ClusterCockpit.

## Additional Information
- ClusterCockpit URL: [ClusterCockpit](https://monitoring.nhr.fau.de/)
- Contact for further assistance: support-hpc@fau.de
```
---

### 2024052342000708_Question%20about%20slurm%20AssocGrpGRES.md
# Ticket 2024052342000708

 ```markdown
# HPC Support Ticket: Question about Slurm AssocGrpGRES

## Keywords
- Slurm
- AssocGrpGRES
- TinyGPU
- A100 GPUs
- Unix Group
- Research Chair
- Access Limits

## Problem
- User's jobs requesting A100 GPUs sit in the AssocGrpGRES queue.
- User is unsure about the definition of their group and whether it is related to their teaching chair or individual account limits.

## Root Cause
- The user's unix group "iwi5" (research chair) does not have allocated A100 nodes or any other GPU types on TinyGPU.

## Solution
- The HPC Admin clarified that AssocGrpGRES refers to the user's unix group "iwi5".
- The user's group is not a shareholder of A100 nodes, resulting in limited access.

## General Learning
- **AssocGrpGRES** in Slurm refers to the unix group or research chair.
- Access to specific resources like A100 GPUs can be limited if the group is not a shareholder.
- Understanding group allocations and resource limits is crucial for effective job scheduling.
```
---

### 2025012842003514_Tier3-Access-Alex%20%22Tomas%20Arias%20Vergara%22%20_%20iwi5187h.md
# Ticket 2025012842003514

 # HPC Support Ticket: Tier3-Access-Alex

## Keywords
- Tier3 Access
- Alex Cluster
- Nvidia A100 GPGPUs
- Nvidia A40 GPGPUs
- Python
- PyTorch
- Multimodal Training
- Medical Report Generation

## Summary
- **User Request**: Access to Alex cluster for multimodal training of LLMs for medical report generation.
- **Resources Requested**:
  - GPGPU cluster 'Alex' / Nvidia A100 GPGPUs (9.7 TFlop/s double precision)
  - GPGPU cluster 'Alex' / Nvidia A40 GPGPUs (48 GB, 37 TFlop/s single precision)
  - Rechenzeit: 4 * 24 * 10 GPU-hours
- **Software Requested**: Python, PyTorch
- **Application**: Multimodal training LLMs for medical report generation.
- **Expected Results**: Generation of reports using multiple modalities.

## Actions Taken
- **HPC Admin**: Granted access to the Alex cluster with the specified resources.

## Lessons Learned
- **Access Granting**: Ensure proper communication and confirmation when granting access to HPC resources.
- **Resource Allocation**: Understand the specific requirements for GPU resources and software dependencies for specialized applications like multimodal training.

## Root Cause of the Problem
- User needed access to specific HPC resources for a specialized application.

## Solution
- Access to the Alex cluster was granted by the HPC Admin, allowing the user to proceed with their project.

## Follow-Up
- Ensure the user is aware of any additional steps or documentation required to effectively utilize the granted resources.
- Monitor resource usage to ensure compliance with the allocated GPU-hours.
---

### 2019121342000616_Jobs%20auf%20TinyGPU%20nutzen%20alle%20%20nur%20eine%20GPU%20-%20iwi1001h.md
# Ticket 2019121342000616

 # HPC Support Ticket: Jobs auf TinyGPU nutzen alle nur eine GPU

## Keywords
- TinyGPU
- GPU utilization
- nvidia-smi
- qstat
- SSH
- ppn
- Job allocation

## Problem
- User's jobs on TinyGPU request 8 cores (2 GPUs) but only utilize the first GPU.
- Second GPU shows a Python process with minimal GPU memory allocation and no computational resources used.

## Root Cause
- User mistakenly copied an old batch script template that requested 8 cores (2 GPUs) instead of the required 4 cores (1 GPU).

## Solution
- User adjusted the batch scripts to request only 4 cores (1 GPU) for future jobs.

## Additional Information
- **Monitoring GPU Utilization:**
  - Use `qstat -n` to see the node names where jobs are running.
  - During job runtime, log in to the nodes via SSH and use `nvidia-smi` to monitor GPU utilization.
- **SSH Process Limitation:**
  - The SSH process is assigned to the first job of a user, limiting visibility to the GPUs of that job only.

## General Learning
- Ensure job scripts accurately reflect the required resources to avoid underutilization of allocated resources.
- Use monitoring tools like `nvidia-smi` and `qstat` to track job performance and resource usage.
- Be aware of the limitations of SSH processes in monitoring multiple jobs on the same node.
---

### 2022012542000975_Jobs%20on%20TinyGPU%20only%20use%20one%20GPU%20%5Bexzi003h%5D.md
# Ticket 2022012542000975

 # HPC Support Ticket: Jobs on TinyGPU only use one GPU

## Keywords
- TinyGPU
- Gromacs
- GPU usage
- Job submission
- Quota management
- File storage
- Performance optimization

## Problem
- User submitted jobs on TinyGPU requesting two GPUs but only one GPU was utilized.
- User encountered quota issues on the `/home/hpc` filesystem.

## Root Cause
- Incorrect job submission parameters: User requested `ppn=8` instead of `ppn=4` to get one GPU.
- Quota limit on `/home/hpc` was exceeded due to large simulation data.

## Solution
- Correct job submission parameters: Use `ppn=4` to request one GPU.
- Manage file storage:
  - Use `$HOME` for important data with regular backups (50GB quota).
  - Use `$WORK` for less important data (200GB quota, no daily backups).
  - Use `$TMPDIR` for simulation data and move to `$HPCVAULT` afterwards.
  - Increase quota on `$HPCVAULT` for large simulation series.

## General Learnings
- Gromacs performance on multiple GPUs is situational.
- Proper file management is crucial to avoid quota issues.
- Always refer to the HPC website for job submission guidelines.
- Regularly communicate with HPC Admins for performance optimization and resource management.

## Actions Taken
- HPC Admin corrected job submission parameters.
- HPC Admin increased quota on `$HPCVAULT` for the user.
- User was advised on proper file management and job submission practices.

## Follow-up
- User to perform post-processing and verify simulation results.
- User to monitor quota usage and manage files accordingly.

## Related Resources
- HPC website job submission guidelines
- Gromacs performance optimization guides
- HPC file storage and quota management policies
---

### 2025020442003531_GPUs%20allocated%20but%20not%20utilized%20-%20f101ac15.md
# Ticket 2025020442003531

 # HPC Support Ticket: GPUs Allocated but Not Utilized

## Keywords
- GPU utilization
- Resource allocation
- Job monitoring
- ClusterCockpit
- `nvidia-smi`
- `srun`

## Summary
A user's job was allocated 4 GPUs but was only utilizing one, leading to inefficient resource usage.

## Root Cause
- The user's job was not configured to utilize all allocated GPUs.

## Solution
- The user was advised to check GPU utilization using ClusterCockpit or `nvidia-smi` after attaching to the job with `srun`.
- The user canceled the job and planned to resubmit it with a modified resource allocation.

## General Learnings
- Always ensure that jobs are configured to utilize all allocated resources.
- Use monitoring tools like ClusterCockpit or commands like `nvidia-smi` to check resource utilization.
- Properly allocate resources to avoid wastage and ensure availability for other users.

## Actions Taken by HPC Admins
- Notified the user about the underutilization of GPUs.
- Provided instructions on how to check GPU utilization.
- Advised the user to adjust resource allocation accordingly.

## Follow-up
- The user acknowledged the issue, canceled the job, and planned to resubmit with adjusted resource allocation.
---

### 2024022742003721_Jobs%20auf%20Alex%20nutzen%20nur%20die%20H%C3%83%C2%A4lfte%20der%20GPUs%20%5Bb180dc21%5D.md
# Ticket 2024022742003721

 # HPC Support Ticket: Jobs Using Only Half of the GPUs

## Keywords
- GPU utilization
- CUDA_VISIBLE_DEVICES
- Job script
- NVIDIA
- FAU
- NHR@FAU

## Problem Description
Some of the user's jobs on the HPC cluster were only utilizing half of the allocated GPUs.

## Root Cause
The job script was missing a comma between the GPU IDs in the `CUDA_VISIBLE_DEVICES` variable.

## Solution
The user corrected the job script to include a comma between the GPU IDs, allowing the jobs to utilize all allocated GPUs.

## General Learnings
- Always ensure proper syntax when setting the `CUDA_VISIBLE_DEVICES` variable.
- Monitor GPU utilization to detect and address inefficiencies.
- Quickly respond to and resolve issues reported by HPC Admins to optimize resource usage.

## References
- [NVIDIA Blog: Control GPU Visibility with CUDA_VISIBLE_DEVICES](https://developer.nvidia.com/blog/cuda-pro-tip-control-gpu-visibility-cuda_visible_devices/)
---

### 2019041042002001_Query%20regarding%20HPC%20access%20request%20form.md
# Ticket 2019041042002001

 # HPC Support Ticket Conversation Analysis

## Keywords
- HPC access request
- Deep neural network training
- Python 3.6
- TensorFlow, OpenAI Gym, DeepMind Sonnet
- GPU, CPU cores
- Walltime limit
- Emmy cluster, TinyGPU
- Job size, compute resources
- Documentation

## General Learnings
- Clarification of resource requirements (CPU cores vs. CPUs)
- Understanding of cluster limitations (walltime, hardware)
- Importance of user-managed dependencies
- Recommendations for suitable clusters based on user needs

## Root Cause of the Problem
- User confusion about resource requirements (150 CPUs vs. 150 CPU cores)
- Lack of understanding about cluster limitations and available hardware

## Solution
- Clarified that the user meant 150 CPU cores and 1 GPU
- Informed the user about the maximum walltime limit of 24 hours
- Suggested using the Emmy cluster for the task due to its GPU nodes
- Provided documentation for getting started with the HPC cluster

## Detailed Conversation Summary

### User Query
- Master student requiring HPC resources for deep neural network training
- Needs 150 CPUs (clarified as 150 CPU cores) and 1 GPU
- Program written in Python 3.6 using TensorFlow, OpenAI Gym, and DeepMind Sonnet
- Expected run time of 2 days
- Requires guidance on filling out the access request form and documentation for running Python code

### HPC Admin Response
- Clarified the distinction between CPUs and CPU cores
- Informed about the maximum walltime limit of 24 hours
- Suggested using the TinyGPU cluster initially
- Provided documentation link for getting started with the HPC cluster
- Noted that additional libraries need to be managed by the user

### Further Clarification
- User clarified the requirement for 150 CPU cores and 1 GPU
- Inquired about the possibility of using the Emmy cluster
- HPC Admin confirmed that the Emmy cluster's GPU nodes are an option, despite older hardware

## Documentation Links
- [Getting Started with HPC](https://www.anleitungen.rrze.fau.de/hpc/getting-started/)

## Recommendations
- Users should clearly specify their resource requirements (CPU cores vs. CPUs)
- Users should be aware of cluster limitations and plan their jobs accordingly
- Users should manage their own dependencies for additional libraries
- HPC Admins should provide clear guidance on suitable clusters based on user needs
---

### 2025022442000844_GPU%20utilization%20only%20at%208%25%20-%20b110dc11.md
# Ticket 2025022442000844

 # HPC Support Ticket: GPU Utilization Issue

## Keywords
- GPU Utilization
- nvidia-smi
- ClusterCockpit
- Job Footprint
- Batch Size
- VRAM Usage
- GPU-Util

## Summary
A user's jobs were reported to have low GPU utilization, leading to multiple interactions with HPC support to address the issue.

## Problem
- User's jobs showed low GPU utilization (initially around 8%, later around 20-25%).
- The root cause was identified as the batch size, which could not be changed due to comparison requirements.

## Communication
- HPC Admin informed the user about the low GPU utilization and provided instructions on how to monitor it using `nvidia-smi` and ClusterCockpit.
- The user responded that the issue was due to the batch size and that they were using different models for comparison.
- HPC Admin clarified the difference between VRAM usage and GPU utilization and provided tips for improving training speed and GPU utilization.

## Solution
- The user was advised to use ClusterCockpit for a comprehensive view of job performance.
- Tips for improving GPU utilization were provided, including preloading datasets, using local SSDs, efficient logging, and optimizing computation graphs.
- The user agreed to limit their GPU usage to 4 GPUs as they were finishing their current jobs.

## Lessons Learned
- It is important to distinguish between VRAM usage and actual GPU utilization.
- ClusterCockpit provides valuable metrics for job performance analysis.
- Batch size can significantly impact GPU utilization, and optimizing it can improve efficiency.
- Providing clear instructions and tips for optimization can help users improve their job performance.

## Follow-up
- The user was satisfied with the resolution and did not require further assistance.
- The HPC Admin offered to help with any future optimization needs.
---

### 2024060442002642_Job%20on%20TinyGPU%20only%20shows%20minimal%20GPU%20utilization%20%5Biwal142h%5D.md
# Ticket 2024060442002642

 ```markdown
# HPC-Support Ticket: Job on TinyGPU Only Shows Minimal GPU Utilization

## Keywords
- GPU Utilization
- TinyGPU
- JobID
- ClusterCockpit
- nvidia-smi
- srun

## Problem Description
- User's job on TinyGPU (JobID 1683914) shows minimal GPU utilization.
- HPC Admin provided a screenshot from the monitoring system highlighting the issue.

## Diagnostic Steps
- **Monitoring System**: User can log into ClusterCockpit at [monitoring.nhr.fau.de](https://monitoring.nhr.fau.de/) to view GPU utilization.
- **Attach to Running Job**: Use `srun --pty --overlap --jobid YOUR-JOBID bash` to get a shell on the first node of the job.
- **Check GPU Utilization**: Run `nvidia-smi` to see the current GPU utilization.

## Solution
- No specific solution provided in the ticket, but diagnostic steps are outlined for the user to investigate the issue.

## General Learnings
- **Monitoring Tools**: Use ClusterCockpit to monitor job performance.
- **Job Management**: Attach to running jobs using `srun` to perform real-time diagnostics.
- **GPU Utilization**: Use `nvidia-smi` to check GPU utilization and performance metrics.

## Next Steps
- If the user needs further assistance, they should contact HPC support for additional troubleshooting.
```
---

### 2022092342000606_Tier3-Access-Alex%20%22Siyuan%20Mei%22%20_%20iwi5070h.md
# Ticket 2022092342000606

 # HPC Support Ticket Analysis

## Keywords
- Tier3 Access
- Alex GPGPU Cluster
- Nvidia A100
- Python3, PyTorch, TensorFlow, JAX
- Complex Network Training
- Diffusion Models
- Certificate Expiration

## Summary
- **User Issue**: User's certificate for accessing the Alex GPGPU cluster has expired.
- **User Request**: The user requested 500 GPU-hours for complex network training using specific software tools.
- **HPC Admin Response**: The admin confirmed that the user's entitlement for Alex is still valid.

## Root Cause
- The user's certificate for accessing the Alex GPGPU cluster had expired.

## Solution
- The HPC Admin confirmed the user's entitlement is still valid, implying that the certificate issue might need to be resolved separately.

## General Learnings
- Always check certificate validity when users report access issues.
- Confirm entitlements and communicate clearly with users about their access status.
- Ensure users are aware of the expiration dates for their certificates and entitlements.

## Next Steps
- Assist the user in renewing their certificate if needed.
- Ensure the user has the required software (Python3, PyTorch, TensorFlow, JAX) installed and configured for their project.

---

This documentation can be used to resolve similar issues related to certificate expiration and access entitlements for HPC resources.
---

### 2022112842004401_Auslastung%20Alex.md
# Ticket 2022112842004401

 # HPC Support Ticket: Auslastung Alex

## Keywords
- Job Queue
- GPU Limits
- A40 GPUs
- Cluster Utilization

## Problem
- User's jobs are stuck in the queue despite available cluster capacity.
- User suspects the issue is due to reaching the GPU limit for their group (b105dc).

## Root Cause
- The A40 GPUs are fully occupied.
- User's jobs are specifically queued for A40 GPUs.

## Solution
- No immediate solution provided in the ticket.
- HPC Admin informed the user about the A40 GPU queue status.

## General Learnings
- Different GPU types have separate queues.
- Cluster utilization information might not reflect specific resource availability.
- Users should check the status of specific resource queues relevant to their jobs.

## Next Steps for Support
- Inform users about the status of specific resource queues.
- Consider temporary limit increases based on cluster utilization and job priority.
- Provide guidance on submitting jobs to alternative resource queues if available.
---

### 2024093042000447_Jobs%20allocating%20two%20GPUs%20but%20utilizing%20one%20-%20iwi5192h.md
# Ticket 2024093042000447

 ```markdown
# HPC Support Ticket: Jobs Allocating Two GPUs but Utilizing One

## Keywords
- GPU utilization
- Job monitoring
- ClusterCockpit
- nvidia-smi
- Resource allocation

## Problem Description
- User's jobs were allocating two GPUs but only utilizing one.
- User noticed that with two GPU allocations, they were able to complete double the epochs compared to a single GPU.
- However, upon checking with `nvidia-smi`, it was observed that only one GPU was being used.

## Steps Taken by HPC Admin
- Informed the user about the underutilization of allocated GPUs.
- Provided instructions to check GPU utilization using ClusterCockpit and `nvidia-smi`.
- Advised the user to allocate GPU nodes only if the code can make use of the GPU.

## User Response
- Acknowledged the issue and confirmed that only one GPU was being used.
- Agreed to use only one GPU node for future training.

## Solution
- User was advised to ensure that their code is capable of utilizing multiple GPUs before allocating them.
- User should monitor GPU utilization using ClusterCockpit and `nvidia-smi` to avoid resource wastage.

## Lessons Learned
- Importance of monitoring resource utilization to avoid idle resources.
- Proper allocation of GPU nodes based on the code's capability to utilize them.
- Use of ClusterCockpit and `nvidia-smi` for monitoring GPU utilization.
```
---

### 2022041942001711_Early-Alex%20%22Yangkong%20Wang%22%20_%20iwi5069h.md
# Ticket 2022041942001711

 # HPC Support Ticket Analysis: Early-Alex "Yangkong Wang" / iwi5069h

## Keywords
- GPU utilization
- Job monitoring
- Resource allocation
- Python script optimization
- Data preprocessing
- GPU nodes
- Nvidia-smi
- Interactive job

## Summary
The user encountered issues with GPU utilization on the HPC cluster. The jobs were not making effective use of the allocated GPU resources, leading to restrictions on cluster access.

## Root Cause
- The user's script was performing data preprocessing on the CPU and only using the GPU for network training, leading to inefficient GPU utilization.
- Jobs were running for extended periods without significant GPU usage.

## Solution
- The user was advised to move as many tasks as possible to the GPU.
- The user was encouraged to allocate an interactive job on a GPU node to test which tasks can run on the GPU.
- The user was instructed to monitor GPU utilization using `nvidia-smi` and ensure that jobs only allocate GPU nodes if the code can effectively use the GPU.

## Lessons Learned
- Ensure that jobs make efficient use of allocated GPU resources.
- Monitor GPU utilization using tools like `nvidia-smi`.
- Optimize scripts to move as many tasks as possible to the GPU.
- Use interactive jobs to test GPU compatibility of tasks.
- Communicate with HPC support for assistance in identifying and resolving issues.

## References
- [Working with Nvidia GPUs](https://hpc.fau.de/systems-services/systems-documentation-instructions/special-applications-and-tips-tricks/working-with-nvidia-gpus/)

## Next Steps
- The user should re-edit the script to ensure data preprocessing is also handled by the GPU.
- The user should cancel all current tasks and resubmit optimized jobs.
- HPC support should monitor the user's jobs to verify improved GPU utilization before lifting access restrictions.
---

### 2023082142002251_Requesting%20big%20a100.md
# Ticket 2023082142002251

 ```markdown
# HPC Support Ticket: Requesting Big A100

## Keywords
- A100 GPU
- 80GB RAM
- Job Submission
- `-C` Flag
- `sinfo` Command
- Waiting Time

## Problem
- User unable to submit a job for a computational node with A100 GPU and 80GB of RAM.
- `--mem-per-gpu` flag not working.
- User considering checking idle nodes with `sinfo` and searching for a node with a bigger A100.

## Solution
- Use the `-C a100_80` flag to explicitly request the A100 with 80GB.
- Note: The average waiting time for big A100 GPUs will typically be significantly longer.

## General Learnings
- Specific flags like `-C` can be used to request particular hardware configurations.
- Checking idle nodes with `sinfo` is an alternative but not the recommended approach.
- Longer waiting times should be expected for high-demand resources.
```
---

### 2024072242001036_Tier3-Access-Alex%20%22Brendan%20Waters%22%20_%20iwia107h.md
# Ticket 2024072242001036

 # HPC Support Ticket Analysis: Tier3-Access-Alex

## Keywords
- Tier3 Access
- GPU Cluster 'Alex'
- Nvidia A100 GPUs
- GPU-hours
- WaLBerla
- Python3
- Performance Benchmarking
- Publication

## Summary
A user requested access to the GPU cluster 'Alex' for approximately 100,000 GPU-hours to perform GPU scaling benchmarking for the WaLBerla application. The request was deemed unrealistic for the free Tier3 basic service.

## Root Cause
- The user overestimated the required GPU-hours by a significant factor (possibly by 20 times).

## Solution
- The HPC Admin enabled the user's HPC account on Alex but clarified that the requested GPU-hours were not feasible within the free Tier3 basic service.
- The 2nd Level Support team member agreed to discuss the project's actual requirements with the user to clarify the needed resources.

## Lessons Learned
- Users may overestimate resource requirements.
- It is essential to verify and clarify resource requests to ensure they are realistic and feasible.
- Communication between the user and the support team is crucial for understanding and adjusting resource allocations.

## Next Steps
- Follow up with the user to determine the accurate resource needs.
- Provide guidance on applying for larger projects if necessary.

## References
- NHR@FAU Support Contact: [support-hpc@fau.de](mailto:support-hpc@fau.de)
- NHR@FAU Website: [https://hpc.fau.de/](https://hpc.fau.de/)
---

### 2021120342001881_Alex_%2A_Prepare%20Jobs%20auf%20Alex%20fordern%208%20GPUs%20an%2C%20nutzen%20aber%20nur%201%20-%20bc.md
# Ticket 2021120342001881

 # HPC Support Ticket: Alex_*_Prepare Jobs Requesting 8 GPUs but Using Only 1

## Keywords
- HPC
- SLURM
- GPU
- Job Management
- Resource Allocation

## Summary
A user's jobs were requesting 8 GPUs but only utilizing 1, leading to inefficient resource usage.

## Root Cause
- The user did not update the SLURM line in the bash script to request the correct number of GPUs.

## Solution
- The user identified the issue and canceled the problematic jobs.
- The HPC Admin had already terminated the runaway script.

## Lessons Learned
- Always verify job scripts to ensure they request the correct resources.
- Regularly monitor running jobs and emails to catch any issues early.
- Proper communication and quick response can help mitigate resource wastage.

## Actions Taken
- HPC Admin notified the user about the resource misallocation.
- The user canceled the jobs and acknowledged the mistake.

## Follow-up
- Ensure users are aware of the importance of accurate resource requests in job scripts.
- Encourage regular monitoring of job status and resource usage.
---

### 2024110842002214_Regarding%20failure%20of%20tinygpu%20allocation%20since%20Nov%207.md
# Ticket 2024110842002214

 ```markdown
# HPC Support Ticket: Regarding Failure of TinyGPU Allocation

## Keywords
- H100 GPU
- Node availability
- Job queue
- Resource allocation

## Problem Description
- User unable to allocate H100 GPU for experiments.

## Root Cause
- All H100 nodes were busy with jobs from other users in the same account group (iwal).

## Solution
- Wait for available nodes or check the job queue for status updates.

## Learning Points
- **Node Availability**: Check the status of nodes to understand if they are currently in use.
- **Job Queue**: Monitor the job queue to see the number of pending and running jobs.
- **Specificity**: Be specific in support requests to facilitate quicker resolution.

## How to Check Node Availability
- Users can inquire about the availability of nodes and the status of the job queue to plan their experiments accordingly.

## Conclusion
- High demand for H100 nodes led to unavailability for the user. Monitoring node status and job queue is essential for efficient resource allocation.
```
---

### 2022072142001247_Job%20auf%20TinyGPU%20nutzt%20nur%20eine%20GPU%20%5Bmlvl069h%5D.md
# Ticket 2022072142001247

 ```markdown
# HPC Support Ticket: Job auf TinyGPU nutzt nur eine GPU

## Keywords
- TinyGPU
- GPU utilization
- JobID 486669
- nvidia-smi
- Monitoring system
- Resource allocation

## Problem Description
A user's job on TinyGPU (JobID 486669) is only utilizing one of the two requested GPUs.

## Root Cause
The job is not effectively utilizing the allocated GPU resources.

## Solution
1. **Monitoring GPU Utilization**:
   - Use `nvidia-smi` to check the current GPU utilization.
   - Refer to the documentation: [Working with NVIDIA GPUs](https://hpc.fau.de/systems-services/systems-documentation-instructions/special-applications-and-tips-tricks/working-with-nvidia-gpus/).

2. **Ensure Proper Resource Allocation**:
   - Ensure that the job code is capable of utilizing multiple GPUs.
   - Only request GPU nodes if the code can effectively use them to avoid wasting resources.

## Additional Notes
- The HPC Admin provided a screenshot from the monitoring system showing the GPU utilization.
- Users should be mindful of resource allocation to avoid underutilization.

## Contact Information
For further assistance, contact the HPC support team at [support-hpc@fau.de](mailto:support-hpc@fau.de).
```
---

### 2019011742001503_problem%20with%20tinygpu%20on%20woody.md
# Ticket 2019011742001503

 ```markdown
# HPC Support Ticket: Problem with TinyGPU on Woody

## Keywords
- TinyGPU
- GPU jobs
- Error report
- Certificate expired
- Tesla V100-PCIE-16GB
- Amber-gpu module
- PBS script
- :anygtx
- :cuda8

## Summary
A user reported issues with running GPU jobs on TinyGPU, specifically mentioning problems with Tesla V100-PCIE-16GB allocation.

## Root Cause
- Changes in TinyGPU configuration were not communicated effectively to the user.
- The user's PBS script was not updated to reflect the new requirements for GPU allocation.

## Solution
- HPC Admins advised the user to update the PBS script to use `-lnodes=1:ppn=4:anygtx` for job submission.
- Further refinement suggested using `:cuda8` to better match the hardware dependency of the Amber module.

## Lessons Learned
- Importance of clear communication regarding system changes.
- Users should provide detailed error reports for better troubleshooting.
- Regular updates to job submission scripts are necessary to align with system changes.

## Actions Taken
- HPC Admins provided updated PBS script requirements.
- User acknowledged the changes and agreed to update their scripts accordingly.
```
---

### 2022051042001806_Tier3-Access-Alex%20%22Tina%20Wach%22%20_%20mppi103h.md
# Ticket 2022051042001806

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject
Tier3-Access-Alex / mppi103h

## Keywords
- HPC Access
- GPGPU Cluster
- Nvidia A100
- Nvidia A40
- TensorFlow Keras
- Unsupervised Transfer Learning
- Muon Identification
- HESS
- Certificate Expiration

## Summary
A user requested access to the GPGPU cluster 'Alex' for Nvidia A100 and A40 GPUs. The request included details about the required software (TensorFlow Keras) and the intended application (unsupervised transfer learning for muon identification in HESS).

## Root Cause of the Problem
- Certificate expiration was identified as an issue.

## Solution
- The HPC Admin granted access to the user for up to 8 A100 and 8 A40 GPUs.
- The user was directed to the documentation for further information and support.

## General Learnings
- Always check for certificate expiration when troubleshooting access issues.
- Provide users with clear instructions and documentation links for further assistance.
- Ensure that the requested resources and software are properly allocated and accessible.

## Follow-Up
- The ticket was closed after the user was granted access and provided with the necessary documentation.
```
---

### 2024082042001494_%5Baction%20requiered%5D%20short%20running%20Jobs%20on%20Alex%20%5Bb168dc12%5D.md
# Ticket 2024082042001494

 # HPC Support Ticket: Short Running Jobs on Alex

## Keywords
- Short jobs
- GPU allocation
- Job bundling
- Cluster impact
- sacctmgr update

## Problem
- User running a high number of very short jobs on Alex.
- Negatively impacting the Alex Cluster.

## Root Cause
- High volume of short jobs (< 1 minute) causing excessive load on the cluster.

## Actions Taken
- HPC Admin reduced the number of GPUs the user's group could allocate simultaneously to 8.
- User cancelled the jobs and agreed to bundle multiple jobs together in the future.

## Solution
- Aim for a runtime > 1 hour when gathering tasks into a single job.
- HPC Admin removed the restriction after the user's response.

## Lessons Learned
- Running a high number of short jobs can negatively impact the cluster.
- Bundling multiple jobs together can help mitigate this issue.
- Aim for longer job runtimes to optimize resource usage.

## Commands Used
- `sacctmgr update account b168dc set GrpTRES=gres/gpu=8`
- `sacctmgr update account b168dc set GrpTRES=gres/gpu=64`

## Follow-up
- Monitor job submissions to ensure compliance with the new guidelines.
- Provide training or documentation on best practices for job submission.
---

### 2024040242001285_Tier3-Access-Alex%20%22Lukas%20Bue%C3%83%C2%9F%22%20_%20iwi5194h.md
# Ticket 2024040242001285

 # HPC Support Ticket Analysis: Tier3-Access-Alex

## Keywords
- Tier3 Access
- GPU Hours
- NHR-Normalprojekt
- Dataset Storage
- Access Control
- Deep Learning Frameworks
- PhD Project
- MIMIC-CXR Dataset
- Structured Radiological Reports

## Summary
A user requested access to the GPGPU cluster 'Alex' for a PhD project involving large vision language models. The user estimated a need for 21,600 GPU hours, which was deemed unrealistic by the HPC Admin. The admin granted access but advised on the GPU hours and dataset storage.

## Root Cause of the Problem
- Unrealistic estimation of GPU hours required for the project.
- Need for clarification on dataset storage and access control.

## Solution
- The HPC Admin granted access to the cluster but advised that the estimated GPU hours were unrealistic and provided a comparison to a typical NHR-Normalprojekt.
- The admin suggested coordinating with another user for dataset storage and access control.

## What Can Be Learned
- Users may overestimate computational resources needed for their projects.
- It is important to provide guidance on realistic resource allocation.
- Coordination with other users for shared dataset storage can save space and ensure proper access control.
- Clear communication about available resources and expectations is crucial for efficient use of HPC resources.

## Actions Taken
- The HPC Admin granted access to the cluster.
- The admin provided guidance on realistic GPU hour allocation.
- The admin suggested coordination with another user for dataset storage and access control.

## Follow-Up
- Ensure the user understands the resource allocation and coordinates with the appropriate user for dataset storage.
- Monitor the user's resource usage to ensure it aligns with the provided guidance.
---

### 2025011542000551_Job%202301454%20Not%20Utilizing%20A100%20GPU%20Due%20to%20Potential%20Python%20Environment%20Issue%2.md
# Ticket 2025011542000551

 # HPC Support Ticket: Job Not Utilizing A100 GPU Due to Potential Python Environment Issue

## Keywords
- GPU utilization
- Python environment
- A100 GPU
- Job monitoring
- Resource allocation
- `nvidia-smi`
- `srun`

## Summary
A user's job was not utilizing the A100 GPU due to a potential issue with the Python environment being built for CPU instead of GPU.

## Root Cause
- The Python environment used in the job was likely configured for CPU usage rather than GPU.

## Solution
- Ensure the Python environment is configured to utilize GPU resources.
- Use monitoring tools to verify GPU utilization.
- Attach to the running job using `srun --pty --overlap --jobid YOUR-JOBID bash` and check GPU utilization with `nvidia-smi`.

## Steps Taken
1. **Notification**: HPC Admin notified the user about the issue with GPU utilization.
2. **Monitoring**: Provided a screenshot from the monitoring system and instructions to access the monitoring system.
3. **Diagnostic Tools**: Suggested using `srun` to attach to the running job and `nvidia-smi` to check GPU utilization.
4. **Resource Management**: Advised the user to allocate GPU nodes only if the code can utilize the GPU to avoid resource wastage.

## Lessons Learned
- Always ensure that the Python environment is correctly configured to utilize GPU resources if required.
- Use monitoring tools to verify resource utilization.
- Properly allocate resources to avoid idle nodes and ensure efficient use of HPC resources.

## References
- Monitoring System: [ClusterCockpit](https://monitoring.nhr.fau.de/)
- Job Monitoring Link: [JobID 2301454](https://monitoring.nhr.fau.de/monitoring/job/12486490)

## Contact
For further assistance, contact HPC Support at [support-hpc@fau.de](mailto:support-hpc@fau.de).
---

### 2022092042001334_Tier3-Access-Alex%20%22Vanessa%20Wirth%22%20_%20iwi9002h.md
# Ticket 2022092042001334

 # HPC Support Ticket Conversation Summary

## Keywords
- Tier3 Access
- NHR Project
- GPU-hours
- Application Assistance
- Zoom Meeting

## General Learnings
- **Tier3 Access Limits**: Understanding the limits of free Tier3 access and when to apply for an NHR project.
- **Application Process**: Guidance on the NHR application process and available support.
- **Communication**: Importance of clear communication and scheduling meetings for complex issues.

## Problem
- User requested GPU-hours that exceeded the free Tier3 access limit.

## Solution
- **Immediate Action**: HPC Admins granted 1000 GPU-hours within Tier3 as an interim solution.
- **Long-term Solution**: User was advised to apply for an NHR project and provided with the application rules.
- **Support**: Assistance with the application process was offered, and a Zoom meeting was scheduled to discuss open points.

## Root Cause
- User's demand for GPU-hours significantly exceeded the free Tier3 access limit, necessitating an NHR project application.

## Follow-up
- A Zoom meeting was scheduled to clarify open points in the NHR application.

## Additional Notes
- The user was out of office and had to reschedule the meeting multiple times.
- The HPC Admins were accommodating and flexible with scheduling.
---

### 2024072642001761_Not%20all%20allocated%20GPUs%20used%20-%20b167ef.md
# Ticket 2024072642001761

 # HPC Support Ticket: Not All Allocated GPUs Used

## Keywords
- GPU utilization
- JobID
- ClusterCockpit
- `srun`
- `nvidia-smi`
- Resource allocation

## Problem
- User's job (JobID 1896228) on Alex is using only one of the two allocated GPUs.

## Root Cause
- The user's code is not efficiently utilizing the allocated GPU resources.

## Solution
- **Monitoring GPU Utilization:**
  - Use ClusterCockpit: Log into the monitoring system at [ClusterCockpit](https://monitoring.nhr.fau.de/).
  - Use `srun` and `nvidia-smi`:
    ```bash
    srun --pty --overlap --jobid YOUR-JOBID bash
    nvidia-smi
    ```
- **Efficient Resource Allocation:**
  - Ensure that the code can make use of the allocated GPUs.
  - Allocate nodes with GPUs only if the code can utilize them to avoid resource wastage.

## General Learnings
- Regularly monitor GPU utilization to ensure efficient resource usage.
- Use provided monitoring tools and commands to diagnose and optimize job performance.
- Proper resource allocation helps in maximizing the utilization of HPC resources.

## Contact
For further assistance, contact the HPC support team at [support-hpc@fau.de](mailto:support-hpc@fau.de).
---

### 2022012142002088_MKL%20libraries%20on%20alex.md
# Ticket 2022012142002088

 # HPC-Support Ticket Conversation Summary

## Keywords
- Intel MKL libraries
- `$MKLROOT`
- `intel` module
- `mkl` module
- `srun`
- `salloc`
- GPU allocation
- `--gres`
- `--partition`
- Account activation
- Node architecture
- GPU utilization
- `nvidia-smi`

## General Learnings
- The `intel` module no longer automatically loads `intel-mpi` and `mkl`. Users need to load the `mkl` module separately.
- For GPU allocation, both `--gres` and `--partition` options are required.
- Use `salloc` instead of `srun` for requesting jobs.
- Each node on the `alex` cluster has 8 GPUs and 128 CPU cores. Users can allocate one entire node.
- To check GPU utilization, use `nvidia-smi` after connecting to the node via SSH.
- Users can only allocate one full node (8 GPUs) per job on the `alex` cluster.

## Root Cause of Problems
- User could not find Intel MKL libraries because the `mkl` module was not loaded.
- User could not allocate resources due to an invalid account or account/partition combination.
- User could not allocate two nodes using `salloc` because the cluster only allows one full node allocation per job.

## Solutions
- Load the `mkl` module to set `$MKLROOT` and access Intel MKL libraries.
- Ensure the account is properly activated and use the correct partition and account options for resource allocation.
- Use `salloc` with the correct node and GPU specifications for job allocation.
- Check GPU utilization with `nvidia-smi` after connecting to the allocated node.

## Additional Notes
- The `MKL_DEBUG_CPU_TYPE` environment variable is only applicable for older MKL versions.
- For parallel GPU usage, ensure the application is correctly configured to utilize multiple GPUs.
---

### 2022120642002158_AMD%20ROME%20system.md
# Ticket 2022120642002158

 ```markdown
# HPC-Support Ticket: AMD ROME System Configuration

## Keywords
- AMD ROME system
- Benchmarks
- NPS=1
- THP=always
- NUMA balancing=off
- BIOS settings
- EFI boot

## Summary
A user requested an AMD ROME system with specific configurations for benchmarking purposes. The system was similar to the one in tinygpu (tg094).

## Problem
- The user requested specific configurations: NPS=1, THP=always, NUMA balancing=off.
- The BIOS settings were disrupted during the setup process.

## Actions Taken
- HPC Admins attempted to configure the system as requested.
- The node was reset to normal batch operation after the configuration attempt.
- NPS settings were reset, but there was a discrepancy between the settings read by the system and the actual settings.
- Attempting to write unchanged settings caused the system to try booting from BIOS instead of EFI.

## Root Cause
- The BIOS settings were disrupted during the configuration process, leading to boot issues.

## Solution
- The node was reverted to its normal batch operation.
- NPS settings were reset, but further investigation is needed to resolve the discrepancy between the read and actual settings.
- Ensure BIOS settings are correctly configured to avoid boot issues.

## Notes
- The configuration process should be handled with caution to avoid disrupting BIOS settings.
- Further investigation is needed to ensure the system boots correctly from EFI.
```
---

### 2024110542001301_Job%20on%20TinyGPU%20not%20using%20the%20GPU%20%5Biwb3022h%5D.md
# Ticket 2024110542001301

 # HPC Support Ticket: Job on TinyGPU Not Using the GPU

## Keywords
- GPU utilization
- Job allocation
- Monitoring system
- ClusterCockpit
- `nvidia-smi`
- Resource management

## Problem Description
A job running on TinyGPU (JobID 925740) was not utilizing the allocated GPU resources.

## Root Cause
The user's code was not configured to make use of the GPU, leading to idle GPU resources.

## Solution
1. **Monitoring GPU Utilization**:
   - Users can log into the monitoring system ClusterCockpit at [monitoring.nhr.fau.de](https://monitoring.nhr.fau.de/) to view GPU utilization.
   - Alternatively, users can attach to their running job using the command:
     ```bash
     srun --pty --overlap --jobid YOUR-JOBID bash
     ```
   - Once attached, run `nvidia-smi` to check the current GPU utilization.

2. **Resource Allocation**:
   - Ensure that jobs are only allocated nodes with GPUs if the code can actually utilize the GPU.
   - This prevents GPU resources from being idle and allows other users to access them.

## General Learnings
- Regularly monitor job performance to ensure efficient resource utilization.
- Use monitoring tools like ClusterCockpit and `nvidia-smi` to diagnose resource usage issues.
- Properly configure jobs to make use of allocated resources to avoid wastage.

## Contact Information
For further assistance, contact the HPC support team at [support-hpc@fau.de](mailto:support-hpc@fau.de).
---

### 2021090742001951_T90-T97.md
# Ticket 2021090742001951

 ```markdown
# HPC-Support Ticket: T90-T97

## Keywords
- A100 nodes
- GPU availability
- HPC status
- Job scheduling
- Reboot

## Problem
- User received a message indicating issues with A100 nodes.
- Unclear if GPUs were in use by another user or down.
- A100 nodes not listed in HPC status.

## Root Cause
- A100 nodes were unavailable for new jobs due to a problem after the previous job.

## Solution
- Nodes were rebooted.
- User's jobs should have started running after the reboot.

## Lessons Learned
- Check for node availability issues after job completion.
- Reboot nodes if they become unresponsive.
- Ensure HPC status reflects the current state of all nodes.

## Actions Taken
- HPC Admin rebooted the affected nodes.
- User's jobs were rescheduled and expected to run.

## Follow-up
- Monitor node status to prevent similar issues in the future.
- Update HPC status to include A100 nodes.
```
---

### 2022111542001732_Tier3-Access-Alex%20%22Jonas%20Boehm%22%20_%20iww2012h.md
# Ticket 2022111542001732

 # HPC Support Ticket: Tier3-Access-Alex

## Keywords
- GPU utilization
- TinyGPU cluster
- Alex cluster
- JAX library
- Finite differences method
- Electron Beam-based Additive Manufacturing
- University email address

## Problem
- User submitted a request for access to the Alex cluster using a private email address.
- User had not run any GPU jobs on the TinyGPU cluster, which is a prerequisite for access to Alex.

## Root Cause
- User was unaware of the requirement to use a university email address for communication.
- User had not demonstrated efficient GPU job execution on the TinyGPU cluster.

## Solution
- User was instructed to use their university email address for communication.
- User provided GPU utilization data for two jobs (IDs 519190 and 519156) on the TinyGPU cluster, demonstrating efficient GPU usage.
- User's HPC account was subsequently activated on the Alex cluster.

## General Learnings
- Always use the university email address for communication with HPC support.
- Efficient GPU job execution on the TinyGPU cluster is a prerequisite for access to the Alex cluster.
- Provide GPU utilization data to demonstrate efficient job execution.
- Follow up with additional information or tests as requested by HPC admins.
---

### 2021110542000745_Inefficient%20jobs%20on%20TinyGPU%20-%20iwal050h.md
# Ticket 2021110542000745

 # HPC Support Ticket Analysis: Inefficient Jobs on TinyGPU

## Keywords
- GPU utilization
- Batch jobs
- Efficiency
- Configuration
- Runtime

## Summary
- **Issue**: User's batch jobs on TinyGPU showed very poor efficiency with near-zero GPU utilization.
- **Root Cause**: Inefficient application and input configuration.
- **Solution**: HPC Admin advised the user to check and optimize the application and input configuration to improve GPU utilization.

## Lessons Learned
- Regularly monitor job efficiency and GPU utilization.
- Proper configuration of applications can significantly reduce runtime.
- Lack of user response can lead to ticket closure.

## Actions Taken
- HPC Admin notified the user about the inefficiency and provided guidance on improving GPU utilization.
- The ticket was closed due to no response from the user.

## Follow-up
- Ensure users are aware of best practices for configuring GPU-intensive jobs.
- Provide resources or training on optimizing GPU utilization.

---

This documentation aims to assist HPC support employees in identifying and resolving similar issues related to inefficient job configurations on TinyGPU.
---

### 2021111042003223_Jobs%20auf%20TinyGPU%20nutzen%20keine%20GPU%20-%20iwal027h.md
# Ticket 2021111042003223

 ```markdown
# HPC Support Ticket: Jobs auf TinyGPU nutzen keine GPU

## Keywords
- TinyGPU
- GPU utilization
- Job configuration
- Certificate expiration

## Problem Description
- User's jobs on TinyGPU are not utilizing the GPUs.
- GPUs are shown as available but not being used by the jobs.

## Root Cause
- The exact root cause is not explicitly stated in the conversation.
- Possible issues could include job configuration errors or resource allocation problems.

## Solution
- No specific solution is provided in the conversation.
- The ticket was closed due to no response from the user.

## General Learnings
- Ensure job configurations are correctly set to utilize GPU resources.
- Check for any certificate expiration issues that might affect job execution.
- Follow up with users for additional information if the problem persists.

## Next Steps
- If similar issues arise, verify job scripts for proper GPU resource allocation.
- Check system logs for any errors related to GPU utilization.
- Contact the user for more details if the problem is not resolved.
```
---

### 2023062642001523_Kursaccounts%20f%C3%83%C2%BCr%20High-End%20Simulation%20in%20Practice%20%28HESP%29.md
# Ticket 2023062642001523

 # HPC Support Ticket: Kursaccounts für High-End Simulation in Practice (HESP)

## Keywords
- HPC Accounts
- GPU Programmierung
- TinyGPU
- Alex
- IdM-Portal
- HPC-User-Mailingliste
- LSS-Lehrveranstaltung

## Summary
A request was made for HPC accounts for a course on High-End Simulation in Practice (HESP), focusing on GPU programming. The accounts needed access to TinyGPU and Alex systems.

## User Request
- **Course**: High-End Simulation in Practice (HESP)
- **Duration**: Until the end of the semester (October)
- **Department**: Lehrstuhl für Informatik 10 (LSS)
- **Users**:
  - zu94vyqy
  - ku04rijy
  - yt28emyp
  - ce64jila
  - ro25gedy
  - ty46xiqy
  - ab04unyc
  - os15axer
  - ov15uqov
  - ad66egev
  - ir59exot

## HPC Admin Response
- **Accounts Created**: iwgr025h-iwgr034h
- **Access**: IdM-Portal
- **Availability**: Next day
- **Additional Info**: Users automatically added to HPC-User-Mailingliste

## Root Cause
Need for HPC accounts with GPU programming capabilities for a specific course.

## Solution
- HPC accounts were created and made available via the IdM-Portal.
- Users were informed about their accounts and the automatic addition to the HPC-User-Mailingliste.

## General Learnings
- Ensure users are informed about their accounts and any automatic subscriptions.
- Verify that accounts are properly configured for the required systems (TinyGPU, Alex).
- Communicate the availability timeline clearly to the users.
---

### 2024070842004542_two%20jobs%20on%20Alex%20not%20utilizing%20GPUs%20-%20bccc117h.md
# Ticket 2024070842004542

 # HPC Support Ticket: GPU Utilization Issue

## Subject
Two jobs on Alex not utilizing GPUs

## Keywords
- GPU utilization
- Job monitoring
- LAMMPS input script
- ClusterCockpit
- nvidia-smi

## Issue Description
- Two jobs (IDs: 1857182, 1857180) allocated 4 GPUs each but did not utilize them.
- Other jobs by the same user were functioning correctly.

## Root Cause
- The user did not set the GPU package and suffix in the LAMMPS input script.

## Solution
- The user canceled the jobs after being notified.
- Ensure the LAMMPS input script is correctly configured to utilize GPUs.

## Steps for Monitoring and Diagnosis
1. **Monitoring System**:
   - Access ClusterCockpit at [https://monitoring.nhr.fau.de/](https://monitoring.nhr.fau.de/).
   - View GPU utilization graphs to identify underutilized resources.

2. **Attach to Running Job**:
   - Use the command `srun --pty --overlap --jobid YOUR-JOBID bash` to get a shell on the first node of the job.
   - Run `nvidia-smi` to check current GPU utilization.

## Lessons Learned
- Always verify the configuration of input scripts to ensure proper resource utilization.
- Regularly monitor job performance using available tools like ClusterCockpit.
- Quickly address underutilization issues to optimize resource allocation.

## Closure
- The ticket was closed after the user canceled the jobs and acknowledged the issue.
---

### 2023051042003571_Details%20for%20HPC%20fields.md
# Ticket 2023051042003571

 # HPC Support Ticket Conversation Analysis

## Keywords
- HPC clusters
- Deep learning models
- HPC-Zielsysteme
- Typische Jobgrosse
- Benotige Rechenzeit
- Speicherplatz
- GPUs
- TinyGPU
- Quota

## Summary
- **User Issue**: User needs assistance in filling out details for HPC fields (HPC-Zielsysteme, typische Jobgrosse, benotige Rechenzeit, and Speicherplatz) for a deep learning project.
- **Root Cause**: Lack of knowledge about the specific requirements for HPC resources.
- **Solution**:
  - Use `@fau.de` email for contact.
  - For deep learning, use TinyGPU as the HPC-Zielsysteme.
  - Specify the number of GPUs needed in typische Jobgrosse.
  - Estimate GPU-time required in benotige Rechenzeit (e.g., 100 hours, 1000 hours).
  - Default quota is ~1TB; specify additional storage needs in Speicherplatz if required.

## General Learnings
- Always use the official email for HPC support.
- For machine learning projects, TinyGPU is recommended.
- Determine the number of GPUs and estimate the required GPU-time.
- Default storage quota is ~1TB; request more if needed for large datasets or results.

## Action Items
- Ensure users contact HPC support with their official email.
- Guide users to specify their resource needs based on project requirements.
- Provide default values and encourage users to request additional resources if necessary.
---

### 2023012642002184_Tier3-Access-Alex%20%22Cem%20Karatastan%22%20_%20iwi5124h.md
# Ticket 2023012642002184

 # HPC Support Ticket Analysis

## Keywords
- Interactive jobs
- Batch jobs
- NFS traffic
- TinyGPU
- Alex cluster
- GPU usage
- Deep learning models
- PyTorch
- DINO model
- MSN model
- AWS p4d-24xlarge
- ViT-Large

## Summary
- **User Request**: Access to Alex cluster for deep learning tasks using DINO and MSN models.
- **Issue**: User has only run interactive jobs on TinyGPU, with significant NFS traffic.
- **Admin Response**: Requested user to demonstrate non-interactive batch job capability on TinyGPU before granting access to Alex.

## Root Cause
- User has not demonstrated the ability to run non-interactive batch jobs.
- High NFS traffic indicates potential misuse of HPC resources.

## Solution
- User needs to run and demonstrate successful non-interactive batch jobs on TinyGPU.
- Reduce NFS traffic by following good HPC practices.

## General Learnings
- Always ensure users run non-interactive batch jobs to optimize resource usage.
- Monitor and minimize NFS traffic to improve HPC performance.
- Verify user requirements and capabilities before granting access to advanced resources.

## Additional Notes
- User requested to copy folders from TinyGPU to Alex.
- AWS p4d-24xlarge instance mentioned for comparison, highlighting the need for efficient resource management.

## Status
- Ticket closed due to continued use of interactive jobs on TinyGPU without demonstrating batch job capability.
---

### 2023090542000611_Job%20on%20Alex%20does%20not%20use%20GPU%20%5Biwi5137%5D.md
# Ticket 2023090542000611

 # HPC Support Ticket: Job on Alex does not use GPU

## Keywords
- GPU utilization
- Job allocation
- Monitoring system
- ClusterCockpit
- `nvidia-smi`
- Resource management

## Problem
- User's job on TinyGPU (JobID 644438) was using only one GPU out of the eight allocated GPUs.

## Root Cause
- The job was not efficiently utilizing the allocated GPU resources.

## Solution
- HPC Admin provided instructions to monitor GPU utilization:
  - Log into the monitoring system ClusterCockpit at [monitoring.nhr.fau.de](https://monitoring.nhr.fau.de/).
  - Attach to the running job using `srun --pty --overlap --jobid YOUR-JOBID bash` to get a shell on the first node.
  - Use `nvidia-smi` to check the current GPU utilization.

## General Learnings
- Ensure that jobs allocate GPU resources only if the code can make use of them.
- Monitor GPU utilization to avoid idle resources.
- Use ClusterCockpit and `nvidia-smi` for monitoring GPU usage.

## Status
- The ticket was closed as the jobs started to look better.

## Contact
- For further assistance, contact the HPC support team at [support-hpc@fau.de](mailto:support-hpc@fau.de).
---

### 2025031342003342_Tier3-Access-Alex%20%22Julius%20Glaser%22%20_%20mfqb102h.md
# Ticket 2025031342003342

 # HPC Support Ticket Analysis

## Keywords
- GPU usage
- Cluster access
- Job efficiency
- Resource allocation
- Conda environment
- Deep learning
- Diffusion MRI data
- GPU availability
- RAM limitations

## Summary
A user requested access to a more powerful GPU cluster (Alex) due to high demand and limited resources on their current cluster (TinyGPU). The HPC Admin denied the request, citing inefficient GPU usage by the user.

## Root Cause of the Problem
- User's jobs were not optimized for GPU usage and ran for only a few minutes.
- High demand and limited RAM on the current cluster (TinyGPU).

## Solution
- The user was advised to demonstrate efficient GPU usage on TinyGPU before applying for access to Alex.
- No additional software was required as the user planned to use their existing Conda environment.

## General Learnings
- Efficient GPU usage is a prerequisite for accessing more powerful clusters.
- Users should optimize their jobs to make better use of available resources.
- High demand for GPU resources is a common issue across clusters.
- Users can circumvent resource limitations by using CPU, but this may not be time-efficient.

## Next Steps for Similar Issues
- Assess the user's job efficiency and GPU usage.
- Advise users to optimize their jobs for better resource utilization.
- Inform users about the high demand for GPU resources and the need to demonstrate efficient usage before accessing more powerful clusters.
---

### 2025021942000434_Job%20on%20Helma%20stoped%20working%20%5Bv106be14%5D.md
# Ticket 2025021942000434

 # HPC Support Ticket: Job on Helma Stopped Working

## Keywords
- GPU utilization
- Job monitoring
- ClusterCockpit
- `srun`
- `nvidia-smi`
- Resource allocation

## Summary
A user reported that their job on Helma stopped using the GPU after a few hours. The HPC Admin provided guidance on monitoring GPU utilization and resource allocation.

## Root Cause
The job stopped utilizing the GPU, leading to idle resources.

## Solution
1. **Monitor GPU Utilization:**
   - Log into the monitoring system ClusterCockpit at [https://monitoring.nhr.fau.de/](https://monitoring.nhr.fau.de/).
   - Use `srun --pty --overlap --jobid YOUR-JOBID bash` to attach to the running job and run `nvidia-smi` to check GPU utilization.

2. **Resource Allocation:**
   - Ensure that nodes with GPUs are only allocated if the code can make use of the GPU.
   - Avoid idle resources by properly managing job allocations.

## General Learnings
- Regularly monitor job performance using available tools.
- Properly allocate resources to avoid idle time.
- Use `srun` and `nvidia-smi` for real-time job monitoring.

## Next Steps
- If further issues arise, contact the HPC support team for assistance.

## Contact Information
- **HPC Admins:** support-hpc@fau.de
- **2nd Level Support Team:** Lacey, Dane (fo36fizy), Kuckuk, Sebastian (sisekuck), Lange, Florian (ow86apyf), Ernst, Dominik (te42kyfo), Mayr, Martin
- **Head of Datacenter:** Gerhard Wellein
- **Training and Support Group Leader:** Georg Hager
- **NHR Rechenzeit Support:** Harald Lanig
- **Software and Tools Developer:** Jan Eitzinger, Gruber
---

### 2025011442002292_Jobs%20on%20TinyGPU%20not%20using%20GPUs%20%5Biwem103h%5D.md
# Ticket 2025011442002292

 # HPC Support Ticket: Jobs on TinyGPU Not Using GPUs

## Keywords
- GPU utilization
- Job monitoring
- Resource allocation
- `nvidia-smi`
- `srun`
- ClusterCockpit

## Summary
A user's jobs on TinyGPU were not utilizing the allocated GPUs, leading to resource wastage.

## Root Cause
- Bugs in the training script disabled GPU usage.

## Solution
- The user identified and fixed the bugs in the script, enabling GPU utilization.

## Steps Taken
1. **HPC Admin:**
   - Notified the user about the GPU underutilization.
   - Provided instructions to monitor GPU usage via ClusterCockpit and `nvidia-smi`.
   - Advised on proper resource allocation.

2. **User:**
   - Acknowledged the issue.
   - Reviewed and fixed the script with the supervisor.
   - Apologized for the resource wastage.

## Lessons Learned
- Regularly monitor job performance to ensure efficient resource utilization.
- Use monitoring tools like ClusterCockpit and `nvidia-smi` to check GPU usage.
- Ensure scripts and codes are properly configured to use allocated resources.
- Communicate with the HPC support team for assistance when needed.

## Follow-up
- The ticket was closed after confirming that GPUs were being utilized, albeit with low load.
---

### 2023031442003862_jobs%20on%20TinyGPU%20have%20been%20terminated%20due%20to%20excessive%20IO%20-%20iwsp005h.md
# Ticket 2023031442003862

 # HPC Support Ticket: Excessive IO Issue on TinyGPU

## Keywords
- Excessive IO
- Job termination
- TinyGPU
- strace output
- open operations

## Summary
- **Issue**: User's jobs on TinyGPU were terminated due to excessive IO operations, causing problems for other HPC users.
- **Root Cause**: A job performed over 15,000 open operations in 35 seconds.
- **Affected System**: TinyGPU (specifically node tg085)
- **Detection**: HPC Admins detected the issue and notified the user via email.
- **User Response**: User acknowledged the issue and started investigating.

## Lessons Learned
- Excessive IO operations by a job can severely impact the performance and usability of the HPC system for all users.
- Monitoring and detecting such issues promptly is crucial for maintaining system stability.
- Communication with the user about the problem and providing relevant data (e.g., strace output) can help in resolving the issue.

## Solution
- Not yet provided in the ticket conversation. The user is investigating the issue.

## Follow-up Actions
- HPC Admins should follow up with the user to ensure the issue is resolved.
- If the problem persists, further investigation and potential job restrictions may be necessary.

## Related Tools
- `strace`: Used to diagnose and debug excessive IO operations.

## Documentation for Future Reference
- This incident highlights the importance of IO monitoring and management on HPC systems.
- Similar issues can be diagnosed using tools like `strace` to analyze system calls and IO operations.
- Prompt communication and collaboration between HPC Admins and users are essential for resolving such issues efficiently.
---

### 2021111542003376_nvidia-smi%20not%20working.md
# Ticket 2021111542003376

 # HPC Support Ticket: nvidia-smi not working

## Keywords
- nvidia-smi
- GPU usage
- HPC cluster
- batch script
- interactive job
- TensorFlow
- PyTorch

## Problem Description
- User is trying to verify if their code is using GPU on the HPC cluster.
- `nvidia-smi` is not working as expected.
- Code is running slowly despite requesting GPU resources.

## Root Cause
- User was not running `nvidia-smi` on the node where the job was executing.
- Potential issue with GPU detection in TensorFlow or PyTorch.

## Steps Taken
1. **Initial Request**: User provided details about their batch script and the issue with `nvidia-smi`.
2. **Admin Response**: Requested more information about the cluster, batch script, and where `nvidia-smi` was being run.
3. **User Clarification**: Provided details about the cluster, batch script, and submission command. Mentioned trying `nvidia-smi` in the HPC terminal and an interactive job.
4. **Admin Instructions**:
   - Instructed the user to log in to the node where the job is running via SSH.
   - Provided steps to find the node using `squeue.tinygpu -l` and then logging in using `ssh <node>`.
   - Suggested checking GPU detection within the Python script if using TensorFlow or PyTorch.

## Solution
- **Interactive Access**: User should log in to the node where the job is running to use `nvidia-smi`.
- **GPU Detection**: Verify GPU detection within the Python script using TensorFlow or PyTorch documentation.

## Additional Resources
- [TensorFlow Documentation](https://hpc.fau.de/systems-services/systems-documentation-instructions/special-applications-and-tips-tricks/tensorflow/)

## Conclusion
- The user was able to run `nvidia-smi` interactively on the node where the job was executing.
- Further investigation into GPU detection within the Python script was recommended.

---

This documentation can be used to assist other users facing similar issues with `nvidia-smi` and GPU usage on the HPC cluster.
---

### 2021101142003125_inefficient%20jobs%20on%20TinyGPU%20-%20iwi5029h.md
# Ticket 2021101142003125

 # Inefficient Jobs on TinyGPU

## Keywords
- Inefficient jobs
- TinyGPU
- GPU utilization
- Resource request
- PPN (processors per node)

## Problem
- User's jobs on TinyGPU request two GPUs but only utilize one.
- Root cause: Inefficient resource request leading to underutilization of GPUs.

## Solution
- HPC Admin suggests two options:
  1. Modify the application to utilize both requested GPUs.
  2. Request only one GPU by changing PPN from 8 to 4.

## General Learnings
- Always ensure that the resources requested in a job match the resources utilized.
- Incorrect resource requests can lead to inefficiencies and wasted resources.
- Proper GPU utilization is crucial for optimal performance and resource management.

## Related Ticket
- Subject: inefficient jobs on TinyGPU - iwi5029h
---

### 2022051142000994_Job%20on%20TinyGPU%20only%20uses%20one%20GPU%20%5Biwi5061h%5D.md
# Ticket 2022051142000994

 ```markdown
# HPC Support Ticket: Job on TinyGPU only uses one GPU

## Keywords
- GPU utilization
- PyTorch
- Multi-GPU
- `nvidia-smi`
- Resource allocation

## Problem
- User's job on TinyGPU (JobID 253230) uses only one GPU out of the two allocated GPUs.
- User's code specifies `device = torch.device("cuda:0" if train_on_gpu else "cpu")`, which restricts the use to only one GPU.

## Root Cause
- The code explicitly specifies the use of GPU with ID 0, preventing the utilization of multiple GPUs.

## Solution
- Modify the code to `device = torch.device("cuda" if train_on_gpu else "cpu")` to enable PyTorch to use all available GPUs.
- Verify GPU utilization by SSHing into the node and using `nvidia-smi`.

## Additional Information
- Monitoring system screenshot provided to show GPU utilization.
- Link to documentation on working with NVIDIA GPUs: [Working with NVIDIA GPUs](https://hpc.fau.de/systems-services/systems-documentation-instructions/special-applications-and-tips-tricks/working-with-nvidia-gpus/)
- StackOverflow reference for multi-GPU usage in PyTorch: [How to use multiple GPUs in PyTorch](https://stackoverflow.com/questions/54216920/how-to-use-multiple-gpus-in-pytorch)

## General Learning
- Ensure that code is configured to utilize all allocated GPUs.
- Use monitoring tools and commands like `nvidia-smi` to verify resource utilization.
- Properly allocate and manage HPC resources to avoid idle time and maximize efficiency.
```
---

### 2018090542001906_Re%3A%20%5BRRZE-HPC%5D%20Call%20for%20proposals%20on%20NVidia%20Tesla%20V100%20usage%20-%20mfbi05.md
# Ticket 2018090542001906

 # HPC Support Ticket Conversation Analysis

## Keywords
- NVidia Tesla V100 GPUs
- Amber
- Benchmarking
- GPU allocation
- Job submission
- Module loading
- CUDA_VISIBLE_DEVICES
- Scientific computing
- Resource allocation

## What Can Be Learned

### General Information
- **Resource Availability**: The HPC center has 4 NVidia Tesla V100 GPUs available, which are allocated as a 4-GPU block.
- **Application**: Amber, a molecular dynamics simulation software, is discussed for its potential use with the V100 GPUs.
- **Performance**: V100 GPUs are reported to be up to 3 times faster than GTX980 for Amber simulations.

### Technical Details
- **Job Submission**: Users need to SSH into `testfront.rrze.uni-erlangen.de`, load the `pbspro/default` module, and use `qsub` to submit jobs.
- **Node Specifications**: The host `ivyep1` has 2x Intel Xeon E5-2690 v2 processors (20 physical cores, 40 threads), 64 GB of main memory, and 4 V100 GPUs.
- **Storage**: The node has ~870 GB of local disk storage in `/scratch`, which is cleaned up after each job.
- **Module**: The module `amber-gpu/18p04-at18p09-gnu-intelmpi2017-cuda9.2` is recommended for Amber on `ivyep1`.

### Best Practices
- **GPU Allocation**: Users should combine four individual runs in one job script and bind them to specific GPUs using `CUDA_VISIBLE_DEVICES`.
- **Performance Optimization**: The `skin_permit` parameter can provide additional performance boosts for Amber simulations.

### Troubleshooting
- **Module Loading**: The `qsub` command will not work without loading the `pbspro/default` module first.
- **CPU Differences**: The host CPU is different from other nodes and does not support AVX2.

### User Interaction
- **Proposal Submission**: Users interested in using the V100 GPUs should submit a short description of their project, including scientific outcomes, application details, compute time requirements, and justification for using V100 GPUs.
- **Communication**: The conversation highlights the importance of clear communication between users and HPC admins regarding resource availability and usage.

This analysis provides a comprehensive overview of the conversation, highlighting key technical details, best practices, and troubleshooting tips for HPC support employees.
---

### 2024090442002486_Jobs%20on%20Alex%20do%20not%20use%20all%20allocated%20GPUs%20-%20b211dd19.md
# Ticket 2024090442002486

 # HPC Support Ticket: Jobs on Alex Do Not Use All Allocated GPUs

## Keywords
- GPU utilization
- Job allocation
- ClusterCockpit
- `nvidia-smi`
- Resource management

## Summary
A user's job on the Alex cluster was not utilizing all allocated GPUs, leading to resource inefficiency.

## Root Cause
- The user's job was only using one out of four allocated GPUs.

## Diagnostic Steps
1. **Monitoring System**: Check GPU utilization using ClusterCockpit.
2. **Job Attachment**: Use `srun --pty --overlap --jobid YOUR-JOBID bash` to attach to the running job.
3. **GPU Utilization**: Run `nvidia-smi` to see current GPU utilization.

## Solution
- Ensure that the job code is optimized to utilize all allocated GPUs.
- Only allocate nodes with GPUs if the code can effectively use them.

## General Learning
- Always verify that jobs are efficiently using allocated resources.
- Use monitoring tools and commands to diagnose resource utilization issues.
- Proper resource allocation helps in maximizing cluster efficiency and availability for other users.

## Closure
- The ticket was closed as most of the user's jobs showed acceptable GPU utilization.

## Contact Information
- For further assistance, contact the HPC support team at `support-hpc@fau.de`.

---

This documentation aims to help support employees diagnose and resolve similar GPU utilization issues in the future.
---

### 2025011742001359_Job%20on%20Alex%20only%20uses%204%20of%208%20allocated%20GPUs%20%5Bc106fa11%5D.md
# Ticket 2025011742001359

 # HPC Support Ticket: Job on Alex only uses 4 of 8 allocated GPUs

## Keywords
- GPU utilization
- Job allocation
- Data storage
- Monitoring
- `torchrun` flag
- `wandb` mode
- `nvidia-smi`
- ClusterCockpit
- `srun`
- File server load
- Workspaces
- Archiving datasets

## Problem
- User's jobs (JobIDs 2307781, 2307782, 2307714) on Alex only use 4 of the 8 allocated GPUs.
- Data is read from `/home/atuin/`, which can decrease training speed due to file server load.

## Root Cause
- Incorrect setting of the `torchrun` flag `--nproc_per_node`.
- Inefficient data handling leading to decreased training speed.

## Solution
- Set the `torchrun` flag `--nproc_per_node` to the number of GPUs allocated in the submit script.
- Archive the dataset and extract it to `$TMPDIR` at the beginning of the job.
- Consider moving the archived dataset to a workspace.
- Check if `wandb` can be run in offline mode.

## Additional Information
- Monitor GPU utilization using ClusterCockpit or `nvidia-smi` after attaching to the running job with `srun --pty --overlap --jobid YOUR-JOBID bash`.
- Ensure nodes with GPUs are only allocated if the code can utilize them.

## References
- [FAQ: Analyzing large datasets](https://doc.nhr.fau.de/faq/#i-have-to-analyze-over-2-million-files-in-my-job--what-can-i-do)
- [Workspaces](https://doc.nhr.fau.de/data/workspaces/)
- [ClusterCockpit](https://monitoring.nhr.fau.de/)
---

### 2024061742002252_Tier3-Access-Alex%20%22Sebastian%20Wind%22%20_%20hmai131h.md
# Ticket 2024061742002252

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Keywords
- HPC Access
- Account Activation
- GPGPU Cluster
- Nvidia A40
- Conda
- PyTorch
- Exllamav2
- LLM Serving

## Summary
- **User Request**: Access to GPGPU cluster 'Alex' with Nvidia A40 GPUs for a seminar.
- **Required Software**: Conda, PyTorch, Exllamav2.
- **Purpose**: Serving Large Language Models (LLMs) for a seminar.

## Actions Taken
- **HPC Admin**: Activated the user's account on the GPGPU cluster 'Alex'.

## Lessons Learned
- **Account Activation**: HPC Admins can activate accounts for users who need access to specific clusters.
- **Software Requirements**: Users should specify the software they need for their projects.
- **Resource Allocation**: Users can request specific resources like GPU hours for their computational needs.

## Root Cause of the Problem
- User needed access to the GPGPU cluster 'Alex' for a seminar project.

## Solution
- HPC Admin activated the user's account on the specified cluster.
```
---

### 2023040542002628_Not%20utilizing%20all%20requested%20GPUs%20on%20TinyGPU%20and%20Alex%20%28iwi5105h%29.md
# Ticket 2023040542002628

 # HPC Support Ticket: Not Utilizing All Requested GPUs on TinyGPU

## Keywords
- GPU utilization
- Federated Learning (FL)
- Ray
- Flower
- nvidia-smi
- srun --pty --jobid bash
- V100
- A100
- VRAM
- Deadlock
- Memory usage
- Clustercockpit

## Summary
The user was running jobs on the TinyGPU cluster that did not fully utilize the requested GPUs. The HPC Admin identified the issue and provided steps to monitor GPU utilization. The user explained their use case involving Federated Learning (FL) and the challenges they faced with resource allocation and deadlocks.

## Root Cause
- The user's jobs were not fully utilizing the requested GPUs due to issues with the FL implementation using the Flower and Ray packages.
- Deadlocks occurred when Ray workers died due to out-of-memory (OOM) errors, causing the FL process to softlock.

## Solution
- The user implemented a mechanism to abort the FL job if a communication round exceeded a certain time limit, preventing deadlocks from blocking computing resources.
- The HPC Admin provided a Python script to collect the total RAM usage of all processes associated with a job.
- The user was informed that the `mem_used` metric in Clustercockpit shows memory utilization for all jobs on the node, not just the user's job.

## Lessons Learned
- Always ensure that requested GPU resources are fully utilized to avoid wasting computing resources.
- Implement mechanisms to detect and handle deadlocks in parallel processing jobs.
- Use tools like `nvidia-smi` and `srun --pty --jobid bash` to monitor GPU utilization.
- Be aware that memory usage metrics in monitoring tools may not be exclusive to a single job.

## Additional Notes
- The user was advised to use interactive jobs and attach to running jobs for debugging purposes.
- The HPC Admin offered assistance with implementing deadlock detection and remote debugging using tools like VSCode.
- The user was encouraged to provide updates on their progress and to seek help if needed.
---

### 2025012342002837_Tier3-Access-Alex%20%22Katharina%20Distler%22%20_%20bcpc102h.md
# Ticket 2025012342002837

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Keywords
- GPGPU cluster 'Alex'
- Nvidia A100 GPGPUs
- Nvidia A40 GPGPUs
- GROMACS
- AMBER
- MD simulations of GPCRs
- Development of pain medication
- GPU-hours

## Summary
- **User Request**: Access to GPGPU cluster 'Alex' for MD simulations of GPCRs using GROMACS and AMBER.
- **Resources Requested**: Nvidia A100 GPGPUs and Nvidia A40 GPGPUs.
- **Compute Time**: 480 GPU-hours.
- **Expected Outcome**: Development of pain medication.

## Actions Taken
- **HPC Admin**: Initially deferred the request.
- **HPC Admin**: Later granted access to the user.

## Lessons Learned
- **Request Handling**: Initial deferral followed by approval indicates a review process.
- **Resource Allocation**: Specific hardware and software requirements were clearly communicated and addressed.
- **Communication**: Clear and concise communication between the user and HPC Admin.

## Root Cause of the Problem
- **Initial Deferral**: The request was initially deferred, possibly for review or additional information.

## Solution
- **Access Granted**: After review, the user was granted access to the requested resources.
```
---

### 2024041142002356_Tier3-Access-Alex%20%22Jefta%20Wucherpfennig%22%20_%20bcpc100h.md
# Ticket 2024041142002356

 # HPC Support Ticket Conversation Analysis

## Keywords
- Account activation
- GPGPU cluster 'Alex'
- Nvidia A40 GPGPUs
- GPU hours
- Software: gromacs, amber
- MD-simulations
- Binding modes

## Summary
- **User Request:** Access to GPGPU cluster 'Alex' for MD-simulations using gromacs and amber.
- **Resources Requested:** 1200 GPU hours on Nvidia A40 GPGPUs.
- **Expected Outcome:** Trajectories with information about binding modes.

## Actions Taken
- **HPC Admin:** Enabled the user's account on Alex.

## Lessons Learned
- **Account Activation:** HPC Admins can enable user accounts on specific clusters upon request.
- **Resource Allocation:** Users can request specific resources such as GPU hours for their computational needs.
- **Software Requirements:** Users should specify the software they intend to use for their simulations.

## Root Cause of the Problem
- User needed access to the GPGPU cluster 'Alex' for their computational work.

## Solution
- HPC Admin enabled the user's account on Alex, granting them the necessary access.

## Documentation for Support Employees
- **Account Activation Process:** Ensure that user accounts are enabled on the requested cluster.
- **Resource Management:** Verify and allocate the requested computational resources.
- **Software Availability:** Confirm that the required software (gromacs, amber) is available on the cluster.

This documentation can be used to streamline the process for future account activation and resource allocation requests.
---

### 2023010542000448_Allokation%20von%20Knoten%20auf%20Alex%20schl%C3%83%C2%A4gt%20fehl.md
# Ticket 2023010542000448

 # HPC Support Ticket Analysis

## Subject
Allokation von Knoten auf Alex schlägt fehl

## Keywords
- Job submission error
- Slurm
- Invalid account
- GPU allocation
- Account expiration
- Slurm database

## Problem
User encountered an error while submitting jobs to the Alex cluster with A40 GPUs. The error message was:
```
srun: error: Unable to allocate resources: Invalid account or account/partition combination specified
```

## Root Cause
- The user's account was temporarily expired and removed from the Slurm database during a cleanup action.

## Solution
- The HPC Admin reinstated the user's account in the Slurm database.
- The user was advised to use RTX GPUs on TinyGPU if not dependent on the large memory of A40 GPUs due to high load on Alex.

## General Learnings
- Account expiration can lead to removal from the Slurm database.
- Regularly check account status to avoid submission errors.
- Consider using alternative resources during high load periods.

## Job Script Snippet
```bash
#!/bin/bash
#SBATCH --job-name=res50-1
#SBATCH --mail-type=BEGIN,END,FAIL
#SBATCH --mail-user=user@example.com
#SBATCH --nodes=1
#SBATCH --export=NONE
#SBATCH --gres=gpu:a40
#SBATCH --partition=a40
#SBATCH --time=20:00:00
#SBATCH --output=res50-1_%j.log
```

## Additional Notes
- Always ensure that the account is active and properly configured in the Slurm database before submitting jobs.
- Communicate with users about alternative resources during high load periods to optimize job throughput.
---

### 2024011842002134_Job%20on%20Alex%20does%20not%20use%20allocated%20GPU%20%5Ba101cb11%5D.md
# Ticket 2024011842002134

 ```markdown
# HPC Support Ticket: Job on Alex does not use allocated GPU

## Keywords
- GPU utilization
- Conda environment
- Job allocation
- Monitoring system
- ClusterCockpit
- nvidia-smi

## Problem Description
- User's job on Alex (JobID 1038461) does not utilize the allocated GPU.
- Conda environment was built on the frontend without an accessible GPU.

## Root Cause
- Conda environment was not built with GPU access, leading to no GPU utilization during job execution.

## Solution
1. **Allocate a Job with GPU Access:**
   ```bash
   salloc --gres=gpu:a40:1 --partition=a40 --time=01:00:00
   ```
2. **Rebuild the Conda Environment:**
   - Ensure the environment is built within the allocated job to have GPU access.

3. **Monitor GPU Utilization:**
   - **Using ClusterCockpit:**
     - Log into the monitoring system at [ClusterCockpit](https://monitoring.nhr.fau.de/).
   - **Using nvidia-smi:**
     - Attach to the running job:
       ```bash
       srun --pty --overlap --jobid YOUR-JOBID bash
       ```
     - Run `nvidia-smi` to check GPU utilization.

## Additional Information
- **Monitoring System:** ClusterCockpit provides a graphical view of job performance.
- **Contact Support:** For further assistance, contact the HPC support team.

## Conclusion
- Ensure that the conda environment is built within a job that has GPU access to utilize the allocated GPU resources effectively.
```
---

### 2024041142001062_Tier3-Access-Alex%20%22Lukas%20Schr%C3%83%C2%B6der%22%20_%20iwia057h.md
# Ticket 2024041142001062

 # HPC Support Ticket Analysis

## Subject
Tier3-Access-Alex "Lukas Schröder" / iwia057h

## Keywords
- Account activation
- GPGPU cluster 'Alex'
- Nvidia A100, A40 GPGPUs
- Nvidia Modulus Framework
- Physically Informed Neural Networks (PINNs)
- Master thesis
- Surrogate model
- Fluid simulation
- Permeability estimation

## Summary
A user requested access to the GPGPU cluster 'Alex' for their master thesis project involving Physically Informed Neural Networks (PINNs). The user specified the need for Nvidia A100 and A40 GPGPUs and the Nvidia Modulus Framework. The HPC Admin confirmed the account activation.

## Root Cause of the Problem
The user needed access to specific HPC resources and software for their research project.

## Solution
The HPC Admin activated the user's account for the specified resources.

## What Can Be Learned
- **Account Activation Process**: Understanding the steps involved in activating a user's account for specific HPC resources.
- **Resource Allocation**: How to handle requests for specific hardware and software resources.
- **User Support**: Providing timely and clear communication to users regarding their requests.

## Additional Notes
- The user's project involves estimating the permeability of different geometries using PINNs.
- The user initially plans to use a single GPU and later test with 4xGPU.
- The expected outcomes include a feasibility study, fluid simulation, and geometry optimizations.
---

### 2021111242001721_Early-Alex%20%22Frank%20Beierlein%22%20_%20bco123.md
# Ticket 2021111242001721

 # HPC-Support Ticket Conversation Summary

## Subject: Early-Alex "Frank Beierlein" / bco123

### Keywords:
- Amber 20/21
- Nvidia A40 GPGPUs
- Thermodynamic Integration (TI)
- GPU Utilization
- Nvidia MPS Daemon
- Slurm Job Scripts
- Quota Increase

### General Learnings:
- **Amber 20/21** is available as a module with serial, OpenMP, and MPI-parallel binaries.
- **Slurm Job Scripts** from TinyGPU are mostly compatible with Alex, requiring minor adjustments.
- **Nvidia A40 GPUs** have slightly lower performance compared to RTX3080 for Amber.
- **Thermodynamic Integration (TI)** in Amber has lower GPU utilization (around 40-50%) compared to standard MD simulations (around 90%).
- **Nvidia MPS Daemon** can be used to run multiple processes simultaneously on a single GPU, improving overall job efficiency.
- **Quota Increase** can be requested to prevent job failures due to insufficient storage.

### Root Cause of the Problem:
- The user's Amber jobs were experiencing low GPU utilization due to the nature of Thermodynamic Integration (TI) calculations.

### Solution:
- The HPC Admin suggested using the Nvidia MPS Daemon to run multiple pmemd.cuda processes simultaneously on a single GPU. This improved overall job efficiency by a factor of 2.5, despite individual processes taking longer.
- The user was granted a quota increase on /home/woody and /home/vault to prevent job failures due to insufficient storage.

### Additional Notes:
- The user's jobs were not adversely affected by the changes, and the results remained consistent.
- The success of this approach was considered notable and potentially worthy of a success story.

### Documentation for Support Employees:
- When encountering low GPU utilization in Amber jobs, consider the type of calculations being performed. TI calculations may inherently have lower GPU utilization.
- Suggest using the Nvidia MPS Daemon to run multiple processes simultaneously, improving overall job efficiency.
- If a user is concerned about job failures due to insufficient storage, consider granting a temporary quota increase.
---

### 2024011642002227_Tier3-Access-Alex%20%22anatole%20vercelloni%22%20_%20iwia062h.md
# Ticket 2024011642002227

 # HPC Support Ticket Analysis: Tier3-Access-Alex

## Keywords
- Account activation
- Alex cluster
- Nvidia A100 GPGPUs
- Nvidia A40 GPGPUs
- GPU-hours
- Nvidia Modulus
- Seminar HPC meets IA
- ECTS

## Summary
- **User Request**: Access to the Alex cluster for a seminar project.
- **Resources Requested**:
  - 1 GPU for 100 GPU-hours.
  - Nvidia A100 GPGPUs (40 GB, 9.7 TFlop/s double precision).
  - Nvidia A40 GPGPUs (48 GB, 37 TFlop/s single precision).
- **Software Requested**: Nvidia Modulus.
- **Purpose**: Seminar HPC meets IA.
- **Expected Outcome**: 5 ECTS.

## Actions Taken
- **HPC Admin**: Enabled the user's account on the Alex cluster.

## Lessons Learned
- **Account Activation**: Ensure that user accounts are activated promptly upon request.
- **Resource Allocation**: Understand the specific hardware and software requirements for user projects.
- **Educational Support**: Be aware of academic projects and their resource needs.

## Root Cause
- User needed access to specific HPC resources for a seminar project.

## Solution
- HPC Admin enabled the user's account on the Alex cluster, granting access to the required resources.

## Documentation for Future Reference
- **Account Activation Process**: Ensure that the account activation process is streamlined and well-documented.
- **Resource Allocation Guidelines**: Maintain clear guidelines for allocating HPC resources based on user needs.
- **Software Availability**: Ensure that requested software (e.g., Nvidia Modulus) is available and accessible to users.

---

This analysis provides a concise overview of the support ticket, highlighting key actions and lessons learned for future reference.
---

### 2022070742002746_Job%20on%20TinyGPU%20does%20not%20use%20GPU%20%5Biwal045h%5D.md
# Ticket 2022070742002746

 # HPC Support Ticket: Job on TinyGPU Does Not Use GPU

## Keywords
- GPU utilization
- TinyGPU
- JobID
- nvidia-smi
- resource allocation
- monitoring system

## Summary
A user's job on TinyGPU was not utilizing the GPU, leading to idle resources.

## Root Cause
- The user's job (JobID 273216) did not make use of the GPU.

## Solution
- **Monitoring**: Use the monitoring system to check GPU utilization.
- **SSH Access**: SSH to the node and use `nvidia-smi` to verify GPU utilization.
- **Resource Allocation**: Ensure that jobs allocate GPU resources only if the code can utilize them.

## Steps for Support Employees
1. **Check GPU Utilization**: Use the monitoring system to identify jobs not utilizing GPUs.
2. **Notify User**: Inform the user about the issue and provide instructions on how to check GPU utilization using `nvidia-smi`.
3. **Resource Management**: Ensure users are aware of proper resource allocation to avoid idle GPUs.

## Additional Resources
- [Working with NVIDIA GPUs](https://hpc.fau.de/systems-services/systems-documentation-instructions/special-applications-and-tips-tricks/working-with-nvidia-gpus/)

## Contact
For further assistance, contact the HPC support team at [support-hpc@fau.de](mailto:support-hpc@fau.de).
---

### 2020073142002114_Frage%20zu%20Amber.md
# Ticket 2020073142002114

 # HPC Support Ticket Conversation Analysis

## Keywords
- Amber
- RTX 2080Ti
- tinyGPU
- AMD EPYC 7302P
- Gromacs
- Emmy
- Lima
- Tesla K40
- Meggie
- GPU
- CPU
- Benchmarks

## Summary
- **User Inquiry**: The user wants to test RTX 2080Ti GPUs on tinyGPU for Amber calculations. They also inquire about experiences with AMD EPYC 7302P CPUs for Amber and Gromacs, and the performance of Amber on Meggie.
- **HPC Admin Response**: An RTX2080Ti node is available for testing. The host CPU has no influence on the GPU version of Amber/pmemd. NAMD and Gromacs do partial offloading, so the host CPU matters. Meggie is not recommended for GPU-capable calculations with pmemd. The next generation of tinyGPU nodes will be finalized soon.

## Root Cause of the Problem
- The user needs guidance on which tinyGPU nodes to use for testing RTX 2080Ti GPUs with Amber.
- The user seeks information on the performance of AMD EPYC 7302P CPUs with Amber and Gromacs.
- The user wants to know if Amber performs well on Meggie.

## Solution
- **Testing RTX 2080Ti GPUs**: The user can submit jobs to the RTX2080Ti node using the `:rtx2080ti` flag. For Gromacs, the `:smt` flag may also be needed.
- **AMD EPYC 7302P Experience**: The host CPU has no influence on the GPU version of Amber/pmemd. For NAMD and Gromacs, which do partial offloading, the host CPU matters.
- **Amber on Meggie**: Meggie is not a suitable alternative for GPU-capable calculations with pmemd based on benchmarks.

## General Learnings
- The performance of Amber on GPUs is not affected by the host CPU.
- For applications like NAMD and Gromacs that do partial offloading, the host CPU performance is relevant.
- Benchmarks and experiences should guide the choice of hardware for specific applications.
- The HPC team is continuously updating and finalizing specifications for new hardware generations.
---

### 2019032842001515_woody%20tinygpu%20issue.md
# Ticket 2019032842001515

 ```markdown
# HPC-Support Ticket: woody tinygpu issue

## Keywords
- woody tinygpu cluster
- job queue delay
- resource competition

## Problem
- User reported jobs in queue for an unusually long time.

## Root Cause
- Increased competition for resources on the woody tinygpu cluster.

## Solution
- No specific action required; the delay is due to high demand for resources.

## General Learnings
- High demand for resources can cause job queue delays.
- No technical issues were identified with the cluster or user account.

## Actions Taken
- HPC Admin confirmed no technical issues with the cluster or user account.
- User informed about increased competition for resources.
```
---

### 2022111542003132_Cannot%20assign%20the%20GPU%20node.md
# Ticket 2022111542003132

 ```markdown
# HPC Support Ticket: Cannot Assign GPU Node

## Keywords
- GPU nodes
- Maintenance
- Rebooting
- A100, V100, RTX3080

## Problem Description
- User unable to assign any GPU nodes.
- Some GPU nodes (A100, V100, RTX3080) appear to be in a state indicating they are waiting for rebooting.

## Root Cause
- Possible maintenance or rebooting of GPU nodes.

## Solution
- HPC Admin confirmed that most of the nodes are up again.

## Lessons Learned
- Regular maintenance or rebooting of GPU nodes can cause temporary unavailability.
- Users should check for maintenance schedules or contact HPC support for updates on node availability.
```
---

### 2021110542000834_Job%20auf%20TinyGPU%20nutzt%20keine%20GPU%20-%20iwso033h.md
# Ticket 2021110542000834

 ```markdown
# HPC Support Ticket: Job auf TinyGPU nutzt keine GPU

## Keywords
- TinyGPU
- GPU utilization
- Job monitoring
- Configuration
- Binaries

## Summary
A user's job on TinyGPU was not utilizing the GPUs, as indicated by monitoring data. The HPC Admin notified the user to check their binaries and configuration.

## Root Cause
- The job was not configured to use the GPUs.

## Solution
- The user was advised to review and correct the configuration of their job to ensure proper GPU utilization.

## Lessons Learned
- Always verify job configurations and binaries to ensure they are set up to utilize available resources like GPUs.
- Monitoring data is crucial for identifying resource utilization issues.

## Actions Taken
- The HPC Admin provided feedback to the user regarding the lack of GPU utilization.
- The ticket was closed due to no response from the user.
```
---

### 2023101642005414_need%20help%20for%20HPC%20application%20form%20section%20Systems%2C%20requirements.md
# Ticket 2023101642005414

 # HPC Support Ticket Conversation Analysis

## Keywords
- HPC application form
- Systems requirements
- Machine learning/deep learning
- GPU capacity
- Huggingface library
- Wav2vec2, Hubert models
- CommonPhone, HPRC datasets
- CUDA out of memory error
- PyTorch
- tinyGPU cluster
- Job size
- Training time
- Storage space
- Batch size
- Trainable parameters

## Problem
- User encountered `torch.cuda.OutOfMemoryError` due to insufficient GPU memory on their laptop while training deep learning models.
- User needs access to HPC resources for their master thesis project involving machine learning/deep learning methods.

## Details
- **Datasets**: CommonPhone (13.5 MB), HPRC (3.7 GB)
- **Models**: Wav2vec2, Hubert
- **Error**: `torch.cuda.OutOfMemoryError` after training 74 batches
- **Training Parameters**:
  - Batch size: 4
  - Batches per epoch: 500
  - Number of epochs: 160
  - Trainable parameters: 630,924,590

## Solution
- **Target System**: tinyGPU cluster
- **Job Size**: 1 GPU
- **Estimated Training Time**: A few hundred hours
- **Storage Space**: ~1TB (sufficient for data and code)
- **Recommendations**:
  - Consider using a GPU with more DRAM.
  - Optimize code implementation to prevent data copies.
  - Adjust batch size to fit within GPU memory constraints.
  - Consult with a supervisor or experienced HPC user for further assistance.

## General Learnings
- Understanding the importance of GPU memory for deep learning tasks.
- Identifying the need for HPC resources for large-scale machine learning projects.
- Recognizing common errors related to GPU memory allocation in PyTorch.
- Providing guidance on optimizing code and adjusting training parameters to fit within available resources.

## Next Steps
- User should fill out the HPC application form with the provided details.
- User should consider the recommendations for optimizing their code and adjusting training parameters.
- User should consult with their supervisor or an experienced HPC user for further assistance.
---

### 2024041142002776_Tier3-Access-Alex%20%22Chao%20Luo%22%20_%20iwi5116h.md
# Ticket 2024041142002776

 ```markdown
# HPC Support Ticket: Tier3-Access-Alex

## Keywords
- Account Enablement
- Alex Cluster
- GPGPU
- Nvidia A100
- PyTorch
- Master Thesis
- Style Transfer
- Deep Neural Networks

## Summary
- **User Request**: Access to the GPGPU cluster 'Alex' for a Master Thesis project.
- **Resources Requested**:
  - 4 GPUs per job
  - 10 hours per job
  - 60 jobs
- **Software Requested**: PyTorch
- **Project Description**: Style Transfer on Simulated Mouse Tibia Based on Deep Neural Networks

## Actions Taken
- **HPC Admin**: Enabled the user's account on Alex.

## Lessons Learned
- **Account Enablement**: HPC Admins can enable user accounts on specific clusters upon request.
- **Resource Allocation**: Users should specify the number of GPUs, walltime per job, and the number of jobs when requesting computational resources.
- **Software Requirements**: Users should clearly state the software they need for their projects.

## Root Cause of the Problem
- User needed access to the Alex cluster for their Master Thesis project.

## Solution
- HPC Admin enabled the user's account on the Alex cluster.
```
---

### 2024082242001552_Out%20of%20memory%20problem%20-%20ML%20code%20%5Bb143dc19%5D.md
# Ticket 2024082242001552

 ```markdown
# Out of Memory Problem - ML Code

## Keywords
- Out of memory (OOM)
- Memory leakage
- PyTorch
- Data loader
- GPU memory
- CPU memory
- `psutil`
- `gc`
- `torch.from_numpy`
- `persistent_workers`

## Summary
A user encountered an "out of memory" problem with their machine learning code during supervised deep learning training. The issue occurred on two independent systems, indicating a problem with the ML code rather than the HPC software stack.

## Root Cause
- The initial suspicion was related to the `to_tensor` function and how it handled numpy arrays and PyTorch tensors.
- The user identified that the `persistent_workers` option in the PyTorch data loader for multi-GPUs was causing memory issues. When set to `True`, the workers kept being initialized, leading to an out-of-memory error.

## Diagnostic Steps
- The user monitored GPU and CPU memory usage using `psutil` and `gc`.
- They compared memory usage between supervised (SV) and self-supervised (SS) training setups.
- The user modified the `to_tensor` function and observed changes in memory usage.

## Solution
- The user found that setting `persistent_workers` to `False` resolved the memory issue.
- They also modified the `to_tensor` function to avoid potential memory sharing issues between numpy arrays and PyTorch tensors.

## Lessons Learned
- Memory issues in ML code can be caused by improper handling of numpy arrays and PyTorch tensors.
- The `persistent_workers` option in PyTorch data loaders can lead to memory issues in multi-GPU setups.
- Monitoring memory usage with tools like `psutil` and `gc` can help diagnose memory leaks.
- It's important to test code modifications in both single and multi-GPU environments to identify potential issues.

## Recommendations
- When encountering memory issues, check the configuration of data loaders, especially the `persistent_workers` option.
- Ensure proper handling of numpy arrays and PyTorch tensors to avoid memory sharing issues.
- Use monitoring tools to track memory usage and identify potential leaks.
```
---

### 2024021942001122_RE%3A%20About%20resources%20on%20Alex%20cluster%20and%20file%20system%20-%20b211dd10_b207dd11.md
# Ticket 2024021942001122

 ```markdown
# HPC Support Ticket Conversation Summary

## Subject: RE: About resources on Alex cluster and file system - b211dd10/b207dd11

### Keywords:
- A100 GPUs
- Slurm
- Quota
- File System
- Documentation

### Problem:
- User needs to allocate specific A100 GPUs with 80GB memory.
- Discrepancies in reported quota for $HPCVAULT.
- Unable to locate quota information for $WORK.

### Solution:
- **GPU Allocation**: Use `-C a100_40` or `-C a100_80` in `sbatch`/`salloc` to specify 40GB or 80GB A100 GPUs.
- **Quota Checking**:
  - For $HPCVAULT: Use `quota -s` or `shownicerquota.pl`.
  - For $WORK: Use `df -h $WORK`.
- **Documentation**:
  - Standard quota per filesystem: [Available Filesystems](https://doc.nhr.fau.de/data/filesystems/#available-filesystems)
  - Quota query documentation: [Quotas](https://doc.nhr.fau.de/data/filesystems/#quotas)

### Additional Information:
- **Efficient Data Handling**:
  - [Efficient Data Handling and Data Formats](https://hpc.fau.de/2024/01/29/monthly-hpc-cafe-efficient-data-handling-and-data-formats-february-6-hybrid-event/)
  - [File Systems](https://hpc.fau.de/files/2022/01/2022-01-11-hpc-cafe-file-systems.pdf)

### Follow-up Actions:
- Update documentation to reflect accurate quota information and query methods.
- Close the ticket after confirming the user's understanding and resolving the issue.
```
---

### 2021101242000313_inefficient%20jobs%20on%20TinyGPU%20-%20iwso040h.md
# Ticket 2021101242000313

 # Inefficient Jobs on TinyGPU

## Keywords
- Inefficient jobs
- TinyGPU
- GPU utilization
- Resource request
- PPN (processors per node)

## Problem
- User's jobs on TinyGPU request two GPUs but only utilize one.
- Root cause: Inefficient resource request leading to underutilization of GPUs.

## Solution
- Adjust the application to utilize both requested GPUs.
- Alternatively, modify the resource request to only ask for one GPU (ppn=4 instead of ppn=8).

## General Learnings
- Always ensure that the resources requested in a job match the resources actually utilized.
- Inefficient resource requests can lead to underutilization of HPC resources.
- Proper resource management is crucial for optimal HPC performance.

## Roles Involved
- HPC Admins
- 2nd Level Support team
- Head of the Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support
- Software and Tools developer
---

### 2022110742002836_Tier3-Access-Alex%20%22Mathias%20Zinnen%22%20_%20iwi5093h.md
# Ticket 2022110742002836

 # HPC Support Ticket Analysis

## Keywords
- **NHR-Projekt**
- **GPU hours**
- **FAU-Grundversorgung**
- **NHR-Antragstellung**
- **Pytorch**
- **CUDA**
- **GPGPU cluster 'Alex'**
- **Nvidia A40 GPGPUs**
- **Experiments**
- **Pretraining schemes**
- **Object detection**
- **Instance segmentation**

## Summary
- **User Request**: Access to GPGPU cluster 'Alex' for running experiments with Pytorch and CUDA.
- **Resource Requirement**: 4,800 - 38,400 GPU hours.
- **Application**: Experiments with different datasets and pretraining schemes for large-scale contrastive pretraining for object detection.
- **Expected Results**: Newly trained backbones that generalize to various domains.

## Root Cause of the Problem
- The user's request for GPU hours exceeds the FAU-Grundversorgung.

## Solution
- **HPC Admin**: Suggested discussing the possibility of an NHR-Antragstellung with the relevant professor.
- **Reference**: Provided a link to NHR application rules and mentioned a recent NHR-Antrag as a template.

## General Learnings
- Typical NHR-Projekt on Alex requires 4,800 - 38,400 GPU hours.
- Requests exceeding FAU-Grundversorgung should consider NHR-Antragstellung.
- NHR application rules and templates are available for reference.

## Next Steps for Support
- Guide the user through the NHR-Antragstellung process if needed.
- Ensure the user has access to the necessary documentation and templates.

---

This report provides a concise summary and key learnings from the HPC support ticket conversation, which can be used to address similar issues in the future.
---

### 2022050942002773_Job%20%28JobId%20252538%29%20does%20not%20use%20GPU%20on%20TinyGPU%20%5Biwal097h%5D.md
# Ticket 2022050942002773

 # HPC Support Ticket: Job Not Using GPU on TinyGPU

## Keywords
- GPU utilization
- JobID 252538
- TinyGPU
- nvidia-smi
- resource allocation

## Summary
A job (JobID 252538) running on TinyGPU was not utilizing the allocated GPUs. The HPC Admin notified the user about the issue and provided steps to check GPU utilization.

## Root Cause
- The job was allocated 4 GPUs but was not utilizing any of them.

## Solution
- The user was advised to SSH into the node and use `nvidia-smi` to check GPU utilization.
- The user was reminded to allocate GPU resources only if the code can utilize them.

## Steps to Check GPU Utilization
1. SSH into the node where the job is running.
2. Use the command `nvidia-smi` to check the current GPU utilization.
3. Refer to the documentation for further details: [Working with NVIDIA GPUs](https://hpc.fau.de/systems-services/systems-documentation-instructions/special-applications-and-tips-tricks/working-with-nvidia-gpus/)

## General Learning
- Always ensure that jobs allocated GPU resources are actually utilizing them.
- Use monitoring tools and commands like `nvidia-smi` to check resource utilization.
- Proper resource allocation helps in efficient use of HPC resources.

## Ticket Status
- The ticket was closed due to no response from the user.
---

### 2022092842004111_A40%20with%2048GB.md
# Ticket 2022092842004111

 # HPC Support Ticket: A40 with 48GB

## Keywords
- A40 GPU
- 48GB memory
- sbatch script
- Alex Cluster
- A100 GPU
- `--constraint` option

## Problem
- User wants to specify an A40 GPU with 48GB memory in their sbatch script to avoid resource wastage.
- User is concerned about potentially getting an A40 with 40GB memory instead.

## Solution
- **A40 GPUs**: All A40 GPUs in the Alex Cluster have 48GB of RAM. No special specification is needed.
  ```bash
  #SBATCH --partition=a40
  #SBATCH --gres=gpu:a40:1
  ```
- **A100 GPUs**: To specify between different A100 GPUs, use the `--constraint` option.
  ```bash
  #SBATCH --constraint=a100_40  # For A100 with 40GB memory
  #SBATCH --constraint=a100_80  # For A100 with 80GB memory
  ```

## General Learnings
- Always refer to the cluster documentation for specific hardware details.
- Use the `--constraint` option in sbatch scripts to specify hardware with different configurations.

## Documentation Reference
- [Alex Cluster Documentation](https://hpc.fau.de/systems-services/documentation-instructions/clusters/alex-cluster/)
---

### 2022031542003139_Early-Alex%20%22Linus%20Franke%22%20_%20iwi9001h.md
# Ticket 2022031542003139

 # HPC Support Ticket Analysis

## Keywords
- HPC Account Activation
- Pytorch Module
- GPGPU Cluster 'Alex'
- Nvidia A40 GPGPUs
- Python, Pytorch, CUDA, cuDNN
- Image-based Learning Tasks
- CNN

## Summary
- **User Request**: Access to GPGPU cluster 'Alex' for image-based learning tasks using Python, Pytorch, CUDA, and cuDNN.
- **HPC Admin Response**: Account enabled on Alex. Pytorch module available (python/pytorch-1.10py3.9).

## Root Cause of the Problem
- User required access to specific HPC resources and software modules for their research.

## Solution
- HPC Admin enabled the user's account on the Alex cluster and provided information about the available Pytorch module.

## General Learnings
- Users need to specify their computational requirements clearly, including software and hardware needs.
- HPC Admins can enable accounts and provide information on available software modules to meet user needs.
- Effective communication between users and HPC Admins is crucial for efficient resource allocation and support.

## Action Items for Future Reference
- Ensure users are aware of the available software modules and how to access them.
- Maintain clear communication channels for users to request specific resources and software.
- Document common software modules and their usage for quick reference.
---

### 2022041442001766_Early-Alex%20%22Bernhard%20Kainz%20and%20Team%22%20_%20iwai001h%2C%20iwai002h%2C%20iwai003h%2C%20iwa.md
# Ticket 2022041442001766

 # HPC-Support Ticket Conversation Analysis

## Keywords
- HPC Account Activation
- GPGPU Cluster 'Alex'
- Nvidia A100, A40 GPUs
- PyTorch, TensorFlow Modules
- File Server Access (aibe-anubis)
- New Team Member Account Addition

## General Learnings
- **Account Activation**: Multiple accounts can be activated simultaneously on the HPC cluster.
- **Software Modules**: Alex cluster provides modules for PyTorch and TensorFlow, unlike TinyGPU.
- **File Server Access**: Accessing file servers like aibe-anubis via IdM-Kennung and NFSv4 with Kerberos is not compatible with HPC operations. Alternatives like rsync or sshfs can be used.
- **New Team Member Addition**: New team members can be added to the HPC cluster upon request.

## Root Cause of Problems
- **File Server Access**: The file server aibe-anubis uses IdM-Kennung and NFSv4 with Kerberos, which are not compatible with the HPC environment.

## Solutions
- **File Server Access**: Use alternatives like rsync or sshfs for file server access until a compatible solution is found.

## Documentation for Support Employees

### Account Activation
- **Process**: Multiple accounts can be activated simultaneously on the HPC cluster.
- **Example**: Five accounts (iwai001h, iwai002h, iwai003h, iwai004h, iwai005h) were activated on the Alex cluster.

### Software Modules
- **Availability**: Alex cluster provides modules for PyTorch and TensorFlow, which are not available on TinyGPU.
- **Usage**: Users can load these modules for their machine learning tasks.

### File Server Access
- **Issue**: Accessing file servers like aibe-anubis via IdM-Kennung and NFSv4 with Kerberos is not compatible with HPC operations.
- **Solution**: Use alternatives like rsync or sshfs for file server access.

### New Team Member Addition
- **Process**: New team members can be added to the HPC cluster upon request.
- **Example**: A new team member (iwai066h) was added to the Alex cluster.

This documentation can be used to resolve similar issues in the future.
---

### 2024032142002366_TinyGPU%20in%20Maintenance%3F.md
# Ticket 2024032142002366

 # HPC Support Ticket: TinyGPU in Maintenance?

## Keywords
- TinyGPU
- Maintenance
- Job Submission
- sbatch
- Reserved for maintenance

## Issue
- User unable to submit jobs to TinyGPU.
- Job status shows `ReqNodeNotAvail, Reserved for maintenance`.

## Root Cause
- Scheduled maintenance was ongoing on the HPC systems.

## Solution
- Wait for the maintenance to be completed.
- TinyGPU will be available again shortly after the maintenance period.

## General Learnings
- Regularly check for scheduled maintenance announcements.
- Maintenance can affect job submissions and node availability.
- Use the correct job submission commands and check system status for any ongoing maintenance.

## References
- [Scheduled Downtime of HPC Systems](https://hpc.fau.de/2024/03/19/scheduled-downtime-of-hpc-systems-on-march-11-and-20/)
---

### 2023042542002804_LAMMPS%20job%20on%20Alex%3A%20GPUs%20are%20not%20utilized.md
# Ticket 2023042542002804

 # HPC Support Ticket: LAMMPS Job on Alex - GPUs Not Utilized

## Keywords
- LAMMPS
- GPU utilization
- Job configuration
- Benchmarking
- Resource allocation

## Summary
A user submitted a job that requested 8 GPUs but did not utilize them. The HPC Admin notified the user about this issue.

## Root Cause
The user intentionally requested GPUs without utilizing them for benchmarking purposes. The user needed 64 CPUs and could not request a node with fewer GPUs for the required number of CPUs.

## Solution
The user explained the situation, and the ticket was closed as the user's actions were intentional and for a specific purpose.

## Lessons Learned
- Users may request resources they do not intend to use for specific purposes like benchmarking.
- Communication with the user is essential to understand the reason behind unusual resource requests.
- Consider providing more flexible resource allocation options to accommodate various user needs.

## Follow-up Actions
- None required for this specific case.
- Review resource allocation policies to ensure they meet diverse user requirements.
---

### 2023100942000656_Nodelist%20%28AssocGrpGRES%29.md
# Ticket 2023100942000656

 # HPC Support Ticket: Nodelist (AssocGrpGRES)

## Keywords
- Slurm
- GPUs
- AssocGrpGRES
- squeue
- A100
- qos=a100multi
- Resource Limits

## Problem
- User unable to start additional jobs parallel to a running job.
- Reason: (AssocGrpGRES)

## Root Cause
- The user's project had a GPU limit of 96, and the requested jobs exceeded this limit.
- Calculation: (8+8)*8 = 128 GPUs requested, which is greater than the allowed 96 GPUs.

## Solution
- HPC Admin temporarily increased the GPU limit for the project to 128.
- Later confirmed that the limit was not reverted and the project can use up to 128 GPUs simultaneously.

## General Learnings
- Understand and verify resource limits for projects.
- Use `squeue` to diagnose job scheduling issues.
- Temporarily adjust resource limits when justified and safe.
- Communicate changes in resource limits to users.

## Related Commands
- `squeue`: To display job scheduling information.
- Slurm configuration: To adjust resource limits for projects.

## Follow-up
- Monitor GPU usage to ensure fair resource allocation.
- Regularly review and adjust resource limits as needed.
---

### 2022031442001151_Job%20on%20TinyGPU%20only%20uses%20one%20GPU%20%5Biwi5047h%5D.md
# Ticket 2022031442001151

 # HPC Support Ticket: Job on TinyGPU Only Uses One GPU

## Keywords
- TinyGPU cluster
- GPU allocation
- Resource usage
- Job monitoring
- Wasted resources

## Summary
A user was running two jobs on the TinyGPU cluster, each allocating four GPUs. However, one of the jobs (JobID 231205) was only utilizing one GPU, leading to inefficient resource usage.

## Root Cause
- The user's code was not optimized to utilize all allocated GPUs.

## Solution
- Ensure that the code is designed to use all allocated GPUs.
- Allocate only the number of GPUs that the code can effectively utilize to avoid wasting resources.

## Lessons Learned
- Regularly monitor job resource usage to identify inefficiencies.
- Educate users on the importance of optimizing their code for the allocated resources.
- Close tickets when the issue is resolved or no longer observed.

## Actions Taken
- HPC Admin notified the user about the inefficient resource usage.
- The ticket was closed after the issue was no longer observed.

## References
- HPC Services, Friedrich-Alexander-Universitaet Erlangen-Nuernberg
- Regionales RechenZentrum Erlangen (RRZE)

## Contact
- For further assistance, contact [support-hpc@fau.de](mailto:support-hpc@fau.de)
- Visit [http://hpc.fau.de/](http://hpc.fau.de/) for more information.
---

### 2022042642003554_Early-Alex%20%22Luis%20Fernando%20Orta%22%20_%20bcpc003h.md
# Ticket 2022042642003554

 ```markdown
# HPC Support Ticket Conversation Analysis

## Subject
Early-Alex / User ID: bcpc003h

## Keywords
- Account Enabled
- Certificate Expired
- GPGPU Cluster 'Alex'
- Nvidia A100 GPGPUs
- GROMACS
- Simulations
- Dopamine Receptor Subtypes

## Summary
- **User Request**: Access to GPGPU cluster 'Alex' for running simulations using GROMACS.
- **HPC Admin Response**: Account enabled on Alex.
- **Root Cause**: Certificate expiration.
- **Solution**: Account re-enabled after certificate issue resolved.

## Lessons Learned
- **Account Management**: Ensure certificates are up-to-date to avoid account disruptions.
- **User Support**: Provide clear instructions for users to follow when their certificates expire.
- **Software Requirements**: Understand user needs for specific software (e.g., GROMACS) and ensure it is available on the cluster.

## Actions Taken
- **HPC Admin**: Re-enabled the user's account after resolving the certificate issue.
- **User**: Requested access and provided details about the intended use of the cluster.

## Future Reference
- **Certificate Management**: Regularly check and update certificates to prevent account lockouts.
- **User Communication**: Inform users about certificate expiration dates and the process for renewal.
```
---

### 2022080542002159_Alex%20A100%2040_80GB.md
# Ticket 2022080542002159

 # HPC Support Ticket: Alex A100 40/80GB

## Keywords
- A100 GPU
- 40GB variant
- 80GB variant
- Slurm script
- Constraint option

## Problem
The user is unable to specify which variant of the A100 GPU (40GB or 80GB) they need for their job. The current Slurm script randomly assigns one of the two variants, causing issues with datasets that require the 80GB GPU.

## Root Cause
The Slurm script lacks the specific constraint option to request a particular variant of the A100 GPU.

## Solution
To request a specific variant of the A100 GPU, use the following Slurm options:
- For the 80GB variant: `--constraint=a100_80`
- For the 40GB variant: `--constraint=a100_40`

## General Learning
- Users can specify the required GPU variant using the `--constraint` option in their Slurm scripts.
- This ensures that jobs are assigned to the appropriate hardware, avoiding resource allocation issues.
---

### 2021012142002311_Application%20for%20HPC%20Account.md
# Ticket 2021012142002311

 # HPC Support Ticket Conversation: Application for HPC Account

## Keywords
- HPC Account Application
- Neural Network Training
- GPU Requests
- RRZE Customer ID
- Third-Party Funded Projects
- TinyEth
- Woody Cluster
- Application Form Submission

## Summary
A user from the FAPS Institute is planning to use HPC resources to train neural networks and has questions regarding the application form.

## Questions and Answers

1. **Maximum Calculation Time**
   - **Question:** What is the maximum calculation time I could give?
   - **Answer:** The maximum runtime per job is 24 hours. If calculations need more time, a checkpoint-restart mechanism is required.

2. **GPU Requests**
   - **Question:** How many GPUs can I request?
   - **Answer:** You can request up to 4 GPUs per job. The simulation software must support multiple GPUs simultaneously.

3. **RRZE Customer ID**
   - **Question:** Where can I find information about the local contact person for RRZE customer ID?
   - **Answer:** Ask your supervisor for assistance.

4. **Third-Party Funded Projects**
   - **Question:** What information should I fill in for more detailed info on third-party funded projects?
   - **Answer:** This part does not need to be filled in.

5. **TinyEth Usage**
   - **Question:** How many nodes can I use on TinyEth? Are there any restrictions?
   - **Answer:** TinyEth allows only single-node jobs, but the total number of jobs is not limited. Consider using Woody Cluster for more nodes.

## Application Form Submission
- **Question:** Whom should I send the filled application form to for getting access?
- **Answer:** Send the application form to `rrze-zentrale@fau.de`.

## Root Cause and Solution
- **Root Cause:** User needs clarification on filling the HPC account application form.
- **Solution:** Provided detailed answers to each question, including maximum calculation time, GPU requests, RRZE customer ID, third-party funded projects, and TinyEth usage. Also, directed the user to submit the form to the correct email address.

## Additional Information
- **Woody Cluster:** More nodes available compared to TinyEth.
- **Contact Information:** HPC Services, Friedrich-Alexander-Universitaet Erlangen-Nuernberg, Regionales RechenZentrum Erlangen (RRZE), Martensstrasse 1, 91058 Erlangen, Germany.

This documentation can be used to assist future users with similar questions regarding HPC account applications and resource requests.
---

### 2021110542000772_Inefficient%20jobs%20on%20TinyGPU%20-%20iwal048h.md
# Ticket 2021110542000772

 ```markdown
# Inefficient Jobs on TinyGPU

## Keywords
- GPU utilization
- Batch jobs
- Efficiency
- TinyGPU

## Problem Description
- User's batch jobs on TinyGPU show very poor efficiency.
- GPU utilization rate is close to zero.

## Root Cause
- The application and input configuration are not optimized for GPU utilization.

## Solution
- Check the application and input configuration.
- Improve GPU utilization rate to reduce runtime significantly.

## Actions Taken
- HPC Admin notified the user about the inefficiency.
- No response from the user led to the closure of the support ticket.

## Lessons Learned
- Regularly monitor GPU utilization for batch jobs.
- Optimize application and input configuration for better performance.
- Ensure users are aware of the importance of efficient GPU utilization.
```
---

### 2023050442002557_MPS-Jobs%20on%20Alex%20do%20not%20use%20GPUs%20%5Bbccb006h%5D.md
# Ticket 2023050442002557

 ```markdown
# HPC-Support Ticket: MPS-Jobs on Alex do not use GPUs [bccb006h]

## Keywords
- MPS-Server
- Multi-GPU
- Monitoring system
- rsync
- GPU distribution
- Job scheduling
- Performance issues

## Problem Description
The MPS-Server is not correctly utilizing multiple GPUs for the user's job, resulting in the job running only on the first GPU.

## Root Cause
- The MPS-Server configuration might not be correctly set up to read the multi-GPU settings.
- Potential overbooking of the first GPU.

## Diagnostic Steps
- HPC Admin provided a screenshot from the monitoring system showing the job's GPU usage.
- Identified that the first GPU is likely overbooked.
- Noted performance variations among different parts of the job (part17 is slow, part8 is fast).

## Solution
- The issue was resolved, but the specific fix is not detailed in the conversation.
- Suggested using `rsync` in the background with `&` and `wait` to ensure all background processes complete.
- Recommended distributing the 45 frames across GPUs more effectively.

## Additional Notes
- The desired solution involves a similar approach to Ticket#2023062242001969.
- Example command for parallel rsync:
  ```bash
  ls /data/imagenet-opt/ | xargs -n1 -P10 -I% rsync user@idea-anubis:/data/imagenet-opt/% .
  ```

## Lessons Learned
- Ensure proper configuration of MPS-Server for multi-GPU usage.
- Monitor GPU usage to avoid overbooking.
- Use background processing and wait commands for efficient job management.
- Consider performance variations in job parts and optimize GPU distribution accordingly.
```
---

### 2018083142001583_Re%3A%20%5BRRZE-HPC%5D%20Call%20for%20proposals%20on%20NVidia%20Tesla%20V100%20usage%20-%20mpt407.md
# Ticket 2018083142001583

 # HPC Support Ticket Conversation Analysis

## Keywords
- Nvidia Tesla V100 GPUs
- Amber16, Amber18
- Performance optimization
- Job submission
- Module loading
- GPU allocation
- Scientific computing
- HPC resources

## General Learnings
- **Resource Allocation**: HPC users need to submit proposals to access specialized resources like Nvidia Tesla V100 GPUs.
- **Software Updates**: Users should be encouraged to use the latest software versions for better performance (e.g., Amber18 over Amber16).
- **Job Submission**: Proper module loading and job submission syntax are crucial for accessing specific HPC resources.
- **GPU Utilization**: Efficient use of multiple GPUs can be achieved by combining individual runs in one job script and binding them to specific GPUs using `CUDA_VISIBLE_DEVICES`.

## Specific Issues and Solutions
### Issue: Sticking with Amber16
- **Root Cause**: User was using an older version of Amber (Amber16) which is less efficient.
- **Solution**: HPC Admin suggested upgrading to Amber18 for significant performance improvements.

### Issue: Incorrect Job Submission Syntax
- **Root Cause**: User was using incorrect syntax for job submission.
- **Solution**: HPC Admin provided the correct syntax for job submission, emphasizing the need to explicitly request the queue instead of the hostname.

### Issue: Module Loading for Job Submission
- **Root Cause**: User was not loading the necessary module before submitting a job.
- **Solution**: HPC Admin instructed the user to load the `pbspro/default` module before submitting jobs.

## Best Practices
- Always check for the latest software versions that offer performance improvements.
- Ensure proper module loading before submitting jobs to avoid errors.
- Use efficient GPU allocation strategies to maximize resource utilization.

## References
- [Amber GPU Performance](http://ambermd.org/GPUPerformance.php)
- [Amber GPU Logistics](http://ambermd.org/GPULogistics.php)
- [RRZE HPC](https://www.rrze.de/hpc)
- [HPC FAU](https://hpc.fau.de)

This analysis provides a concise overview of the key points and best practices learned from the HPC support ticket conversation.
---

### 2025020742001769_GPUs%20allocated%20but%20not%20utilized%20-%20b245da12.md
# Ticket 2025020742001769

 # HPC Support Ticket: GPUs Allocated but Not Utilized

## Keywords
- GPU utilization
- Resource allocation
- Job monitoring
- ClusterCockpit
- `nvidia-smi`
- `srun`

## Problem Description
- User's job is allocated 3 GPUs but utilizes only one.
- Inefficient use of GPU resources.

## Root Cause
- The user's code is not fully utilizing the allocated GPU resources.

## Solution
- **Monitoring GPU Utilization:**
  - Use [ClusterCockpit](https://monitoring.nhr.fau.de/) for job monitoring.
  - Alternatively, attach to the running job using `srun --pty --overlap --jobid YOUR-JOBID bash` and run `nvidia-smi` to check GPU utilization.
- **Efficient Resource Allocation:**
  - Ensure that the code can make use of the allocated GPUs.
  - Allocate GPU nodes only if the code can utilize them effectively.

## General Learnings
- Regularly monitor job performance to ensure efficient resource utilization.
- Use monitoring tools like ClusterCockpit and `nvidia-smi` to diagnose resource usage issues.
- Allocate resources based on actual code requirements to avoid idle resources.

## References
- [Job Monitoring with ClusterCockpit](https://doc.nhr.fau.de/job-monitoring-with-clustercockpit/)
- [FAU HPC Support](mailto:support-hpc@fau.de)
- [FAU HPC Website](https://hpc.fau.de/)
---

### 2022120942002125_Tier3-Access-Alex%20%22Srikanth%20Raj%20Chetupalli%22%20_%20iwal064h.md
# Ticket 2022120942002125

 # HPC Support Ticket Analysis: Tier3-Access-Alex

## Keywords
- HPC Account Access
- GPU Resources
- Tier3 Service
- NHR Compute Proposal
- Deep Learning
- Speaker Extraction

## Summary
- **User Request**: Access to GPGPU cluster 'Alex' with 20,000 GPU hours for deep learning research.
- **HPC Admin Response**: Account enabled, but requested GPU hours exceed free Tier3 service. Suggested NHR compute proposal as an alternative.

## Root Cause
- User requested GPU resources beyond the free tier allocation.

## Solution
- **Immediate**: User granted access to start using Alex, with a note on potential resource limitations.
- **Long-term**: User advised to consider submitting an NHR compute proposal for additional resources.

## General Learnings
- Understanding the limits of free tier GPU allocations.
- Importance of submitting compute proposals for extensive resource requirements.
- Handling user requests that exceed standard allocations.

## Follow-up Actions
- Monitor user's GPU usage.
- Provide guidance on submitting NHR compute proposals if necessary.

---

This analysis helps in understanding how to manage user requests that exceed standard resource allocations and the importance of guiding users towards appropriate channels for additional resources.
---

### 2022052542000664_Job%20on%20TinyGPU%20does%20not%20use%20GPU%20%5Biwi5045h%5D.md
# Ticket 2022052542000664

 # HPC Support Ticket: Job on TinyGPU does not use GPU

## Keywords
- GPU utilization
- TinyGPU
- JobID 258319
- nvidia-smi
- resource allocation
- idle resources

## Problem Description
A user's job on TinyGPU (JobID 258319) was not utilizing the GPU, leading to idle resources.

## Root Cause
The user's code was not configured to make use of the GPU, resulting in the allocated GPU resources being idle.

## Solution
1. **Monitor GPU Utilization**: The user was advised to SSH into the node and use `nvidia-smi` to check GPU utilization.
2. **Proper Resource Allocation**: The user was instructed to only allocate nodes with GPUs if their code can actually utilize the GPU.
3. **Documentation**: The user was provided with a link to the documentation for working with NVIDIA GPUs.

## Lessons Learned
- Always ensure that jobs allocated to GPU nodes are capable of utilizing the GPU to avoid wasting resources.
- Use monitoring tools like `nvidia-smi` to check GPU utilization.
- Refer to the documentation for detailed instructions on working with NVIDIA GPUs.

## Follow-Up
The user acknowledged the issue and agreed to stop the job. The ticket was closed after the user's response.

## References
- [Working with NVIDIA GPUs](https://hpc.fau.de/systems-services/systems-documentation-instructions/special-applications-and-tips-tricks/working-with-nvidia-gpus/)
---

### 2021063042001117_CUDA%20out%20of%20memory%20Error.md
# Ticket 2021063042001117

 # CUDA Out of Memory Error

## Keywords
- CUDA out of memory
- GPU memory
- PyTorch
- TinyGPU cluster

## Root Cause
- User encountered a CUDA out of memory error while running a Python script.
- The error is due to the hardware limitation of the GPU model (RTX 3080).

## Solution
- **Hardware Solution**: Suggest using a different TinyGPU node with more memory. Refer to the [TinyGPU cluster documentation](https://hpc.fau.de/systems-services/systems-documentation-instructions/clusters/tinygpu-cluster/).
- **Software Solution**: Modify the script to reduce memory usage. Refer to the [PyTorch FAQ](https://pytorch.org/docs/stable/notes/faq.html) for guidance.

## General Learnings
- GPU memory is a hardware limitation and cannot be increased via software.
- Users should be directed to use appropriate hardware or optimize their scripts for better memory management.
- Providing relevant documentation links can help users find solutions independently.
---

### 2025021242000965_GPUs%20allocated%20but%20not%20utilized%20-%20b193dc13.md
# Ticket 2025021242000965

 # HPC Support Ticket: GPUs Allocated but Not Utilized

## Keywords
- GPU utilization
- Resource allocation
- Job monitoring
- ClusterCockpit
- `nvidia-smi`
- `srun`

## Problem
- User allocated 2 GPUs for jobs but only utilized one, leaving the other idle.
- Example job ID: 2381074

## Root Cause
- User error in resource allocation.

## Solution
- Monitor jobs using ClusterCockpit at [monitoring link](https://monitoring.nhr.fau.de/).
- Attach to running jobs with `srun --pty --overlap --jobid YOUR-JOBID bash` and use `nvidia-smi` to check GPU utilization.
- Ensure code can utilize all allocated GPUs to avoid resource wastage.

## Lessons Learned
- Always monitor resource utilization to optimize job performance and avoid wasting resources.
- Use available tools like ClusterCockpit and `nvidia-smi` for effective monitoring.
- Allocate resources based on actual needs to ensure efficient use of HPC resources.

## Ticket Status
- Closed as user acknowledged the mistake and agreed to correct it.
---

### 2023090442001498_Job%20on%20TinyGPU%20only%20use%201%20of%204%20allocated%20GPUs%20%5Biwso105h%5D.md
# Ticket 2023090442001498

 # HPC Support Ticket: Job on TinyGPU Only Uses 1 of 4 Allocated GPUs

## Keywords
- GPU utilization
- Job allocation
- Monitoring system
- ClusterCockpit
- `nvidia-smi`
- Job script
- GridSearch
- Neural network training

## Problem
- User's job on TinyGPU (JobID 644199) was using only one GPU out of the four allocated GPUs.
- Inefficient resource usage as other GPUs remained idle.

## Root Cause
- User forgot to update the job script to request only one GPU.
- Attempt to parallelize neural network training inside a GridSearch was unsuccessful.

## Solution
- User acknowledged the issue and agreed to modify the job script to request only one GPU for future training iterations.
- User was advised to use the monitoring system ClusterCockpit or `nvidia-smi` to check GPU utilization.

## General Learnings
- Always ensure job scripts request the appropriate number of GPUs to avoid wasting resources.
- Use monitoring tools to verify resource utilization.
- Communicate with HPC support for assistance and guidance on efficient resource usage.

## Actions Taken
- HPC Admin notified the user about the inefficient GPU usage.
- User agreed to correct the job script and utilize resources more efficiently.
- Ticket closed with user promising improvement.

## Tools and Commands
- **ClusterCockpit**: Monitoring system to check job performance and resource utilization.
- **`srun --pty --overlap --jobid YOUR-JOBID bash`**: Command to attach to a running job and get a shell on the first node.
- **`nvidia-smi`**: Command to check current GPU utilization.

## Contact Information
- For further assistance, contact HPC support at `support-hpc@fau.de`.
- Monitoring system: [ClusterCockpit](https://monitoring.nhr.fau.de/)
- HPC website: [FAU HPC](https://hpc.fau.de/)
---

### 2022040142000871_Jobs%20auf%20TinyGPU%20nutzen%20keine%20GPU%20%5Bmppm001h%5D.md
# Ticket 2022040142000871

 ```markdown
# HPC Support Ticket: Jobs auf TinyGPU nutzen keine GPU

## Keywords
- GPU utilization
- Job monitoring
- nvidia-smi
- TinyGPU
- JobID 239783, 239812

## Problem Description
- User's jobs on TinyGPU (JobID 239783 and 239812) were allocating GPUs but not utilizing them effectively.
- Monitoring system showed low GPU usage.

## Root Cause
- The user's code was not efficiently utilizing the allocated GPUs.

## Solution
- User was advised to check GPU utilization using `nvidia-smi` during job runtime.
- User confirmed that jobs were running on GPU but with very low utilization (~5%).
- User agreed to investigate and optimize GPU usage.

## Lessons Learned
- Always verify GPU utilization using `nvidia-smi` to ensure efficient resource usage.
- Allocate GPUs only if the code can effectively utilize them.
- Regularly monitor job performance to identify and address inefficiencies.

## Resolution
- The issue was resolved as new jobs showed improved GPU utilization.
- Ticket was closed by HPC Admin.
```
---

### 2022020942003572_Jobs%20auf%20TinyGPU%20zeigen%20schlechte%20Performance%20-%20iwal027h.md
# Ticket 2022020942003572

 ```markdown
# HPC Support Ticket: Poor Performance on TinyGPU

## Keywords
- GPU Utilization
- Performance Optimization
- Code/Workflow Optimization
- System Monitoring
- GPU-Speicher

## Summary
A user reported poor performance of jobs on TinyGPU. The HPC Admin observed low GPU utilization despite high GPU memory usage.

## Root Cause
- Low GPU utilization indicated by system monitoring.
- High GPU memory usage without corresponding performance.

## Solution
- The user was advised to optimize their code or workflow to improve performance.
- No specific job scripts were saved, but the issue was noted as a generic Python call.

## Lessons Learned
- Regularly monitor GPU utilization and memory usage to identify performance bottlenecks.
- Encourage users to optimize their code and workflows for better performance.
- Keep an eye on system monitoring tools to proactively address performance issues.

## Actions Taken
- The HPC Admin notified the user about the performance issue and suggested optimization.
- The ticket was closed after the initial notification.
```
---

### 2018061342002093_GPU%20support%20on%20emmy%20or%20LiMa%20cluster.md
# Ticket 2018061342002093

 # HPC Support Ticket: GPU Support on Emmy or LiMa Cluster

## Keywords
- GPU support
- Emmy cluster
- LiMa cluster
- Node properties
- Batch script

## Summary
- **User Issue**: Request for assistance with GPU support on Emmy and/or LiMa cluster, including a sample script for job submission.
- **Root Cause**: User requires information on GPU availability and job submission scripts for clusters.
- **Solution**:
  - **LiMa Cluster**: No GPU support available.
  - **Emmy Cluster**: Refer to the "node properties" section in the [Emmy Cluster documentation](https://www.anleitungen.rrze.fau.de/hpc/emmy-cluster/#batch) for GPU support details.

## What Can Be Learned
- **Cluster Capabilities**: Understanding which clusters support GPUs (Emmy supports GPUs, LiMa does not).
- **Documentation Reference**: Importance of referring to official documentation for node properties and job submission scripts.
- **User Assistance**: Providing clear and concise information to users regarding cluster capabilities and resources.

## Action Items for Support
- Direct users to the appropriate documentation for GPU support on Emmy.
- Inform users that LiMa does not support GPUs.
- Ensure documentation is up-to-date with the latest node properties and job submission scripts.
---

### 2024030142003492_Tier3-Access-Alex%20%22Deepak%20charles%20Chellpandian%22%20_%20mfdk103h.md
# Ticket 2024030142003492

 # HPC Support Ticket Analysis

## Keywords
- Account Enablement
- Tier-3 Access
- Alex Cluster
- Nvidia A100 GPUs
- PyTorch
- MRI Simulation
- Memory Requirements
- Thesis Work
- Temporary Access

## Summary
- **User Request**: Temporary access to the Alex cluster for one month to complete thesis work on high-resolution MRI 3D sequence optimization.
- **Resource Requirements**: 8 GPUs per job, 24 hours per job, 150 jobs.
- **Software Needed**: PyTorch.
- **Justification**: High memory requirements for gradient calculations in optimization problems.

## Root Cause
- User needs more computational resources (GPUs) to complete thesis work due to high memory requirements for 3D MRI sequence optimization.

## Solution
- **HPC Admin Action**: Account enabled on Alex cluster.
- **User Instructions**: None provided in the conversation.

## General Learnings
- Users may request temporary access to higher-tier resources for specific projects or thesis work.
- High memory requirements for certain types of simulations (e.g., MRI) may necessitate access to more powerful GPUs.
- Clear communication of resource needs and justification helps in processing such requests efficiently.

## Next Steps for Support
- Ensure the user is aware of any usage policies or limitations for temporary access.
- Monitor resource usage to ensure compliance with the requested allocation.
- Provide any additional support or documentation needed for using the Alex cluster effectively.
---

### 2022070842001665_Using%20adecuate%20HPC%20cluster%20for%20ML-Project.md
# Ticket 2022070842001665

 # HPC Support Ticket Conversation Analysis

## Subject
Using adequate HPC cluster for ML-Project

## Keywords
- Deep learning transformer model
- Text dataset
- Clusters: Alex, Tier3, TinyGPU
- HPC Cafe
- Slurm
- Beginner introduction
- Getting started documentation

## Problem
- User needs to apply a large deep learning transformer model to a text dataset.
- User is unsure which HPC cluster to use: Alex or Tier3.

## Solution
- HPC Admin recommends starting on the Slurm part of TinyGPU.
- Provides links to documentation and an upcoming beginner introduction session.

## General Learnings
- For deep learning projects, starting on a smaller cluster like TinyGPU can be beneficial.
- HPC Cafe offers introductory sessions for beginners.
- Relevant documentation and resources are available for getting started with HPC services.

## Relevant Links
- [TinyGPU Cluster Documentation](https://hpc.fau.de/systems-services/documentation-instructions/clusters/tinygpu-cluster/)
- [HPC Cafe](https://hpc.fau.de/systems-services/support/hpc-cafe/)
- [Getting Started Documentation](https://hpc.fau.de/systems-services/documentation-instructions/getting-started/)
- [HPC in a Nutshell](https://hpc.fau.de/files/2022/06/2022-06-15_hpc_in_a_nutshell.pdf)

## Next Steps for Support
- Ensure the user attends the HPC Cafe session.
- Follow up to confirm the user has successfully started on TinyGPU.
- Provide additional support as needed for the deep learning project.
---

### 2022041242001359_Job%20%28JobId%20243895%29%20does%20not%20use%20GPU%20on%20TinyGPU%20%5Biwal085h%5D.md
# Ticket 2022041242001359

 # HPC Support Ticket: Job Not Utilizing GPU on TinyGPU

## Keywords
- JobID 243895
- TinyGPU
- GPU utilization
- nvidia-smi
- Resource allocation

## Summary
A user's job (JobID 243895) running on TinyGPU was not utilizing the GPU, leading to inefficient resource allocation.

## Root Cause
- The user's job was allocated a GPU node but did not make use of the GPU.

## Diagnosis
- HPC Admin identified the issue through the monitoring system.
- The user was advised to SSH into the node and use `nvidia-smi` to check GPU utilization.

## Solution
- Ensure that jobs allocated to GPU nodes are capable of utilizing the GPU.
- Verify GPU usage with `nvidia-smi`.

## General Learning
- Always confirm that jobs requiring GPU resources are correctly configured to use the GPU.
- Use monitoring tools and commands like `nvidia-smi` to diagnose GPU utilization issues.
- Efficient resource allocation is crucial to avoid wastage and ensure optimal performance.

## Next Steps for Support
- Provide guidance on configuring jobs to use GPU resources.
- Monitor job submissions to ensure proper resource allocation.
- Offer training or documentation on efficient use of HPC resources.
---

### 2024062142000871_Tier3-Access-Alex%20%22Hiwa%20Khamo%22%20_%20iwia106h.md
# Ticket 2024062142000871

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject: Tier3-Access-Alex

### Keywords:
- Access Request
- GPGPU Cluster
- Nvidia A100
- Nvidia A40
- Cuda
- Nvidia Nsight
- Master Thesis
- Performance Analysis
- Code Generation

### Summary:
A user requested access to the GPGPU cluster 'Alex' for their Master Thesis project. The request included details about the required hardware, software, and expected outcomes.

### Details:
- **Hardware Requested:**
  - Nvidia A100 GPGPUs (40 GB, 9.7 TFlop/s double precision)
  - Nvidia A40 GPGPUs (48 GB, 37 TFlop/s single precision)
- **Software Requested:**
  - Cuda
  - Nvidia Nsight
- **Application:**
  - Performance analysis and improved code generation for walberla
- **Expected Outcomes:**
  - Performance analysis and improved code generation for walberla

### HPC Admin Response:
- The user was granted access to the 'Alex' cluster.

### Lessons Learned:
- Users should provide detailed information about their hardware and software requirements when requesting access to HPC resources.
- Access requests for specific clusters should include the purpose and expected outcomes of the project.
- HPC Admins can quickly approve access requests if all necessary information is provided.

### Root Cause of the Problem:
- The user needed access to specific HPC resources for their Master Thesis project.

### Solution:
- The HPC Admin granted the user access to the requested resources.
```
---

### 2024080742003651_Regarding%20checking%20of%20GPU%20usage%20on%20tinygpu%20node.md
# Ticket 2024080742003651

 # HPC Support Ticket: Checking GPU Usage on tinygpu Node

## Keywords
- GPU usage
- nvidia-smi
- Slurm
- sbatch
- srun
- job ID
- shell script
- Python job

## Problem Description
The user is running a Python job using `sbatch.tinygpu` and wants to check the GPU usage using `nvidia-smi`.

## Root Cause
The user needs to attach to the running job to execute `nvidia-smi` on the assigned node.

## Solution
1. **Attach to the Running Job**:
   Use the following command to attach to the running job and get a shell on the assigned node:
   ```bash
   srun --jobid=<jobID> --overlap --pty /bin/bash -l
   ```
   Replace `<jobID>` with the actual job ID of the running job.

2. **Check GPU Usage**:
   Once attached to the job, use `nvidia-smi` to check the GPU utilization.

## Documentation Reference
For detailed instructions, refer to the Slurm documentation:
[Slurm Documentation](https://doc.nhr.fau.de/batch-processing/batch_system_slurm/?h=nvidia+smi#attach-to-a-running-job)

## General Learning
- **Attaching to Running Jobs**: Understanding how to attach to a running job using `srun` is crucial for monitoring and debugging purposes.
- **GPU Monitoring**: `nvidia-smi` is a useful tool for monitoring GPU usage and performance.
- **Slurm Documentation**: Always refer to the official documentation for detailed procedures and best practices.

## Roles Involved
- **HPC Admins**: Provided the solution and documentation reference.
- **User**: Requested assistance with checking GPU usage.

## Ticket Status
The ticket was closed after the user acknowledged the solution.
---

### 2025012142001985_Tier3-Access-Alex%20%22Robert%20Kurin%22%20_%20iwi5269h.md
# Ticket 2025012142001985

 # HPC Support Ticket Analysis: Tier3-Access-Alex

## Keywords
- **GPU Access**: A100, TinyGPU, Alex cluster
- **Resource Allocation**: GPU hours, workspace
- **Software Requirements**: Python, Pytorch, Conda, Git
- **Application**: Multimodal LLM, medical report generation, CT-scans
- **Dataset Size**: 2.5TB
- **Expected Results**: Qualitative comparison of reports

## Summary
- **User Request**: Access to A100 GPUs on the Alex cluster for a Master Thesis project involving multimodal LLM for medical report generation on CT-scans.
- **Resource Estimation**:
  - Baseline experiments: 200 GPU hours
  - Method implementation: 800 GPU hours
  - Total: 1000 GPU hours
- **Dataset**: 2.5TB, requiring workspace usage.

## Problem
- **Initial Issue**: User unsure about access to A100 GPUs in TinyGPU.
- **Root Cause**: Lack of clarity on resource allocation and usage.

## Solution
- **HPC Admin Response**:
  - Confirmed access to A100 GPUs in TinyGPU.
  - Granted access to Alex cluster.
  - Advised user to review documentation due to the "expert-only" nature of the cluster.

## Learning Points
- **Resource Allocation**: Understanding and estimating GPU hours for complex projects.
- **Cluster Access**: Procedures for granting access to specialized clusters.
- **Documentation**: Importance of reviewing documentation for efficient resource usage.

## Next Steps
- **User**: Review documentation and proceed with resource usage.
- **HPC Admin**: Monitor resource usage and provide support as needed.

---

This report provides a concise overview of the support ticket, highlighting key aspects for future reference and troubleshooting similar issues.
---

### 2023110242001479_Job%20on%20Alex%20does%20not%20use%20allocated%20GPU%20%5Biwal137h%5D.md
# Ticket 2023110242001479

 # HPC Support Ticket: Job on Alex Does Not Use Allocated GPU

## Keywords
- GPU utilization
- Job allocation
- Monitoring system
- ClusterCockpit
- `nvidia-smi`
- Resource management

## Problem
- **Root Cause:** User's job (JobID 891201) on Alex is not utilizing the allocated GPU resources.

## Solution
- **Steps to Verify:**
  1. **Monitoring System:**
     - Log into ClusterCockpit at [monitoring.nhr.fau.de](https://monitoring.nhr.fau.de/) to view GPU utilization.
  2. **Attach to Running Job:**
     - Use `srun --pty --overlap --jobid YOUR-JOBID bash` to get a shell on the first node of the job.
     - Run `nvidia-smi` to check current GPU utilization.

- **Recommendations:**
  - Ensure that jobs allocate nodes with GPUs only if the code can utilize them.
  - Avoid idle GPU resources by properly managing job allocations.

## Additional Information
- **Contact:** For further assistance, contact the HPC Admins via [support-hpc@fau.de](mailto:support-hpc@fau.de).

## Conclusion
- Proper monitoring and verification of GPU utilization are crucial to optimize resource allocation and avoid idle resources.
---

### 2021120942000343_Jobs%20auf%20TinyGPU%20nutzen%20nur%20eine%20GPU%20-%20iwal075h.md
# Ticket 2021120942000343

 ```markdown
# HPC-Support Ticket: Jobs auf TinyGPU nutzen nur eine GPU

## Keywords
- TinyGPU
- GPU utilization
- A100 GPUs
- Resource allocation
- Job optimization

## Problem Description
- User's jobs on TinyGPU request two A100 GPUs but only utilize one.
- GPU utilization is very low (around 3%).

## Root Cause
- Inefficient resource allocation leading to underutilization of GPUs.

## Solution
- **HPC Admin** advised the user to:
  - Request only the number of GPUs that the jobs can effectively use.
  - Optimize jobs to improve GPU utilization.

## Lessons Learned
- Ensure jobs are optimized to utilize all requested resources.
- Over-requesting resources can lead to inefficiencies and delays for other users.
- Regularly monitor and adjust resource requests based on actual usage.
```
---

### 2024112542001219_Tier3-Access-Alex%20%22Sascha%20Hofmann%22%20_%20iwia121h.md
# Ticket 2024112542001219

 ```markdown
# HPC Support Ticket: Tier3-Access-Alex

## Keywords
- GPGPU cluster 'Alex'
- Nvidia A100 GPGPUs
- GPU-hours
- MPI
- nvhpc
- nsight systems/compute
- CUDA-streams
- 2D/3D Poisson equations
- Kernel fusion
- Batching
- Overlapping communication kernels
- nvshmem implementations
- Double precision results

## Summary
A user requested access to the GPGPU cluster 'Alex' for benchmarking routines on 2D/3D Poisson equations with a focus on CUDA-streams. The user specified the required software and expected results, including insights into different CUDA-stream approaches and comparisons with nvshmem implementations.

## User Request
- **Contact:** User's email and username
- **Need:** Access to GPGPU cluster 'Alex' with Nvidia A100 GPGPUs
- **Compute Time:** 8 * 10 minutes * 200 GPU-hours
- **Required Software:** MPI, nvhpc, nsight systems/compute
- **Application:** Benchmarking routines for 2D/3D Poisson equations with CUDA-streams
- **Expected Results:** Insights into CUDA-stream approaches (kernel fusion, batching, overlapping communication kernels) and comparison with nvshmem implementations
- **Additional Notes:** Interest in double precision results

## HPC Admin Response
- The user's HPC account was enabled on Alex.

## Lessons Learned
- Properly documenting user requests for access to specific HPC resources.
- Ensuring that the required software and compute time are clearly specified.
- Understanding the user's application and expected results for better support.

## Root Cause of the Problem
- The user needed access to the GPGPU cluster 'Alex' for specific benchmarking tasks.

## Solution
- The HPC Admin enabled the user's account on Alex, granting the necessary access.
```
---

### 2024050242002228_tinygpu.md
# Ticket 2024050242002228

 ```markdown
# HPC-Support Ticket Conversation: tinygpu

## Keywords
- tinygpu
- salloc
- interaktive Jobs
- Batch Jobs
- GPU
- Speicher
- Warteschlange
- Ressourcen
- Deadline
- Projektbetreuer
- sinfo

## Summary
- **User Issue**: The user is experiencing delays and interruptions when trying to access GPU resources using `salloc.tinygpu`.
- **Root Cause**: High demand for GPU resources and insufficient available memory.
- **Solution**: Use batch jobs instead of interactive jobs for better resource allocation and scheduling.

## Detailed Conversation

### User
- **Issue**: The user's job is stuck in the queue and a previous job was interrupted.
- **Request**: Assistance with accessing GPU resources and understanding why the job was interrupted.

### HPC Admin
- **Explanation**: Interactive jobs can only run if GPUs are available, which is not always the case. The job was interrupted due to an out-of-memory error.
- **Recommendation**: Use batch jobs for production calculations and interactive jobs only for short tests.
- **Resource**: Provided a link to the available memory per GPU type.

### User
- **Follow-up**: The user needs results urgently due to an approaching deadline and requests help with batch jobs or an online meeting.

### HPC Admin
- **Update**: High system load and some nodes were unavailable due to filesystem issues. One of the user's jobs has started.
- **Recommendation**: Continue using batch jobs and seek help from the project supervisor or contact person at the department.

### 2nd Level Support
- **Explanation**: TinyGPU is a shared system, so waiting times are normal. The user can check the system status with `sinfo`.

## Lessons Learned
- **Resource Availability**: High demand for GPU resources can lead to delays in job processing.
- **Job Types**: Batch jobs are more efficient for long-running tasks and can run concurrently.
- **Memory Management**: Ensure that jobs do not exceed the available memory to avoid interruptions.
- **System Status**: Use `sinfo` to check the current status and availability of resources.

## Action Items
- **User**: Switch to batch jobs for better resource management and scheduling.
- **HPC Admin**: Monitor system load and node availability to ensure smooth operation.
- **2nd Level Support**: Provide guidance on using `sinfo` to check system status.
```
---

### 2022021542003471_VASP%20auf%20Alex%20nutzt%20keine%20GPU%20%5Bbctc38%5D.md
# Ticket 2022021542003471

 # HPC Support Ticket: VASP auf Alex nutzt keine GPU

## Keywords
- VASP
- GPU
- NVIDIA
- nvidia-smi
- Monitoring
- Makefile
- Buildskript
- Buildlogs
- NCCL
- Infiniband
- Ethernet
- Cache size
- OpenMP

## Problem Description
- User's VASP job (JobID 30807) on Alex did not utilize any of the 8 allocated GPUs.
- The issue was identified through the monitoring system and confirmed by checking GPU usage with `nvidia-smi`.

## Root Cause
- The problem was traced to the `vasp6/6.3.0-nccl` module, which had issues with OpenMP settings and cache size.
- The user's Makefile was based on `vasp.6.3.0/arch/makefile.include.nvhpc_ompi_mkl_omp_acc` but with OpenMP removed and some compiler flags modified.

## Solution
- HPC Admins adjusted the `vasp6/6.3.0-nccl` module to use the user's Makefile parameters.
- It was suggested to set `export NCCL_SOCKET_IFNAME=enp70s0f0` on A100 nodes to avoid issues with NCCL initialization.
- The cache size was increased to `-DCACHE_SIZE=54000` without significant performance impact.

## Additional Notes
- The problem was specific to A100 nodes, which have different network hardware (Infiniband) compared to other nodes.
- The issue with NCCL initialization was similar to a known issue documented by Amsterdam colleagues.

## Conclusion
- The VASP job was able to run more smoothly after adjusting the Makefile parameters and setting the appropriate environment variable for NCCL.
- Further testing and monitoring are recommended to ensure the stability of the solution.
---

### 2024021442002872_AssocGrpGRES%20-%20v101be.md
# Ticket 2024021442002872

 # HPC Support Ticket: AssocGrpGRES

## Keywords
- AssocGrpGRES
- GPU limit
- Cluster usage
- Basic usage category
- HPC Portal
- Resource usage
- Project manager

## Summary
A user was unable to run jobs on the HPC cluster due to an "AssocGrpGRES" reason. The user had questions about checking cluster usage, cooldown rate, and group limits.

## Root Cause
The user's group was limited to a maximum of 80 GPUs at the same time due to being in the "basic usage" category.

## Solution
- **GPU Limit**: The user's group is allowed to use a maximum of 80 GPUs simultaneously. This limit is fixed and not related to fairshare or resource usage over time.
- **Cluster Usage**: Users can check their own resource usage in the HPC Portal. Project managers can see the usage of the whole project.
- **Basic Usage Category**: The limit is in place because the project is in the "basic usage" category.

## Additional Information
- For additional resources, users can apply for an NHR project.
- The HPC Admins can provide assistance with the application process.

## Next Steps
- If more resources are needed, users should consider applying for an NHR project.
- For further assistance, contact the HPC Admins or the Head of the Datacenter.

## Conclusion
The user's inability to run jobs was due to the GPU limit imposed on their group. The HPC Portal can be used to monitor resource usage, and additional resources can be requested through an NHR project application.
---

### 2025021042001146_Tier3-Access-Alex%20%22Johannes%20Enk%22%20_%20iwi5229h.md
# Ticket 2025021042001146

 # HPC Support Ticket Analysis

## Keywords
- Tier3 Access
- Alex
- GPGPU Cluster
- Nvidia A100
- Nvidia A40
- GPU-hours
- Python
- PyTorch
- Medical Data
- Pre-training
- Fine-tuning
- Semi-supervised Techniques
- Speech Pathologies
- Labeled Data
- Preliminary Tests

## Summary
- **User Request**: Access to GPGPU cluster 'Alex' for training networks on labeled medical data.
- **Resources Requested**:
  - Nvidia A100 GPGPUs (9.7 TFlop/s double precision)
  - Nvidia A40 GPGPUs (48 GB, 37 TFlop/s single precision)
  - 1800 GPU-hours
- **Software Needed**: Python, PyTorch
- **Application**: Training networks on labeled medical data, heavy pre-training, fine-tuning, semi-supervised techniques.
- **Expected Outcomes**: Models to segment articulator movement for speech pathology detection, publication of labeled data and preliminary tests.

## HPC Admin Response
- **Access Granted**: User allowed to use 'Alex' with the specified account.
- **System Status**: 'Alex' is currently busy; jobs may take a few hours to start.

## Lessons Learned
- **Resource Allocation**: Proper allocation of GPU resources for specific tasks.
- **System Load**: Awareness of current system load and potential delays in job processing.
- **Application Details**: Importance of understanding the specific needs and expected outcomes of user projects.

## Root Cause of the Problem
- **High System Load**: 'Alex' is very busy, causing delays in job processing.

## Solution
- **Inform User**: Notify the user about the current system load and potential delays.
- **Monitor System**: Continuously monitor the system to manage load and optimize resource allocation.

---

This report provides a concise overview of the support ticket, highlighting key details and lessons learned for future reference.
---

### 2022042842000571_Early-Alex%20%22Vikas%20Joshi%22%20_%20qa66qori.md
# Ticket 2022042842000571

 ```markdown
# HPC Support Ticket Conversation Analysis

## Subject: Early-Alex / qa66qori

### Keywords:
- HPC Cluster
- TensorFlow
- PyTorch
- Gamma-ray Astronomy
- Graph Neural Networks
- Nvidia A100
- Nvidia A40
- Certificate Expiration

### Summary:
- **User Request**: Access to HPC cluster 'Alex' for GPGPU resources (Nvidia A100 and A40) to run TensorFlow, PyTorch, and TensorProbability for Graph Neural Networks in Gamma-ray astronomy.
- **Admin Response**: User account granted access to 8 A100 and 8 A40 GPUs. Documentation provided for cluster usage. Preinstalled TensorFlow and PyTorch modules mentioned, with a note that they might not work with Gammapy.

### Root Cause of the Problem:
- Certificate expiration issue mentioned by the HPC Admin.

### Solution:
- User account granted access to the required resources.
- Documentation link provided for further assistance.

### General Learnings:
- **Resource Allocation**: Understanding the process of allocating GPU resources to users.
- **Software Compatibility**: Awareness of potential compatibility issues between preinstalled software modules and specific user applications.
- **Documentation**: Importance of referring users to relevant documentation for cluster usage.

### Additional Notes:
- **Follow-up**: Ensure the user is aware of any additional steps needed to resolve the certificate expiration issue.
- **Software Support**: Consider providing guidance or support for installing custom software versions if preinstalled modules are incompatible.
```
---

### 2022072742001469_Bus%20Error%20on%20Slurm%20Job.md
# Ticket 2022072742001469

 # HPC Support Ticket: Bus Error on Slurm Job

## Keywords
- Bus Error
- Core Dumped
- Python Script
- Tesla V100
- Slurm Job
- GPU Utilization

## Problem Description
A user encountered a "Bus Error" while running a neural network training job on Tesla V100 GPUs. The job ID was 487924, and the error occurred at line 22 of the script: `python train_varnet_demo.py`.

## Root Cause
The error likely occurred due to an issue with data transfer to or from the GPU. The exact cause could not be determined without further debug information.

## Ticket Conversation Summary
- **User:** Reported a bus error in a Slurm job with job ID 487924. The job involved training a neural network using Python on Tesla V100 GPUs.
- **HPC Admin:** Identified that the error occurred at line 22 of the script and suggested that it might be related to data transfer issues with the GPU. Recommended searching online for similar errors.

## Recommendations
- **Debugging:** Check the script and related code for any issues with data transfer to or from the GPU.
- **Online Resources:** Search for similar errors online to find potential solutions.

## Solution
No specific solution was provided in the ticket conversation. Further debugging and investigation are required to identify and resolve the issue.

## General Learnings
- **Bus Error:** Indicates a problem with data transfer, often related to GPU operations.
- **Core Dumped:** The system generated a core dump file, which can be used for debugging.
- **GPU Utilization:** High GPU utilization does not necessarily indicate the cause of the error but can provide context for troubleshooting.

## Next Steps for Support
- Guide the user in checking their script for data transfer issues.
- Provide resources or tools for analyzing core dump files.
- If the issue persists, escalate to the 2nd Level Support team for deeper investigation.
---

### 2024011642002174_Job%20on%20Alex%20does%20not%20use%20allocated%20GPU%20%5Bb167ef13%5D.md
# Ticket 2024011642002174

 ```markdown
# HPC-Support Ticket: Job on Alex does not use allocated GPU

## Keywords
- GPU utilization
- Job allocation
- Monitoring system
- ClusterCockpit
- `nvidia-smi`
- Resource management

## Problem Description
- User's job on Alex is allocating 8 GPUs but utilizing only one.
- This leads to inefficient resource usage and potential idling of GPUs.

## Root Cause
- The user's code is not configured to utilize all allocated GPUs effectively.

## Solution
- **Monitoring**:
  - Use ClusterCockpit at [monitoring.nhr.fau.de](https://monitoring.nhr.fau.de/) to view GPU utilization.
  - Alternatively, attach to the running job using `srun --pty --overlap --jobid YOUR-JOBID bash` and run `nvidia-smi` to check GPU utilization.

- **Resource Allocation**:
  - Ensure that the job script and code are configured to use all allocated GPUs.
  - Only allocate GPUs if the code can effectively utilize them.

## Actions Taken
- HPC Admins notified the user about the underutilization of GPUs.
- Provided instructions on how to monitor GPU usage.
- Requested the user to check their input and contact support if further assistance is needed.

## Outcome
- The user was informed about the issue and provided with steps to monitor and resolve it.
- The ticket was closed after the user adjusted their GPU allocation.

## General Learning
- Always verify that the job script and code are optimized to use all allocated resources.
- Regularly monitor resource utilization to ensure efficient use of HPC resources.
- Contact HPC support for assistance with debugging and optimizing resource usage.
```
---

### 2022101242003676_Tier3-Access-Alex%20%22Lukas%20Hennig%22%20_%20mppi098h.md
# Ticket 2022101242003676

 # HPC Support Ticket Analysis

## Keywords
- HPC Account Activation
- Certificate Expiration
- GPGPU Cluster 'Alex'
- Nvidia A40 GPGPUs
- GPU-hours
- Software Requirements: Python, CUDA, cuDNN
- Application: Graph Neural Networks (GNNs)
- Hyperparameter Optimization
- Tau Neutrino Event Classification
- Tier3 Access

## Summary
- **User Request**: Access to GPGPU cluster 'Alex' for training Graph Neural Networks (GNNs) for tau neutrino event classification.
- **Software Requirements**: Python, CUDA, cuDNN.
- **Expected GPU-hours**: Approximately 1k hours.
- **Application Details**: Training GNNs on different datasets and performing automated hyperparameter optimization.

## Issue
- **Root Cause**: Certificate expiration.

## Solution
- **Action Taken**: HPC Admin activated the user's HPC account on Alex.

## General Learnings
- **Account Activation**: Ensure certificates are up-to-date for account activation.
- **Resource Allocation**: Understand user requirements for GPU-hours and software dependencies.
- **Application Specifics**: Be aware of specific applications like GNNs and their computational needs.

## Next Steps
- **Follow-up**: Monitor GPU usage and assist with any further resource allocation needs.
- **Documentation**: Update internal documentation on handling certificate expirations and account activations.

---

This analysis provides a concise overview of the support ticket, highlighting key details and actions taken to resolve the issue. It serves as a reference for future support cases involving account activation and resource allocation.
---

### 2022122042001104_Masterthesis.md
# Ticket 2022122042001104

 # HPC Support Ticket Analysis: Masterthesis

## Keywords
- Masterthesis
- Deep Learning
- AudioLabs
- GANs
- StyleTransfer
- VAEs
- NHR@FAU
- Neural Networks
- High Data Volume
- Job Size
- Working Time
- Storage Space

## Summary
A user is preparing to start their Master's thesis in the field of deep learning, specifically focusing on audio data processing. They plan to use various architectures such as GANs, StyleTransfer, and VAEs. The user anticipates a high data volume and wants to use NHR@FAU for training their neural networks. They are seeking guidance on which target systems to specify, as the job size, working time, and storage space are not yet determined.

## Root Cause of the Problem
- The user needs guidance on specifying target systems for their deep learning tasks on NHR@FAU.
- The user's email was sent via ProtonMail, which caused confusion for the HPC Admin.

## Solution
- The HPC Admin clarified that the support is not responsible for ProtonMail issues.
- No specific solution was provided regarding the target systems for deep learning tasks.

## General Learnings
- Users should specify their requirements clearly when requesting HPC resources.
- HPC Admins should provide guidance on selecting appropriate target systems for deep learning tasks.
- Ensure that email communication is clear and relevant to the HPC support team's responsibilities.

## Next Steps
- The user should provide more detailed information about their job size, working time, and storage space requirements.
- The HPC Admin should offer guidance on suitable target systems for deep learning tasks involving high data volumes.

## References
- NHR@FAU Support: [support-hpc@fau.de](mailto:support-hpc@fau.de)
- NHR@FAU Website: [https://hpc.fau.de/](https://hpc.fau.de/)
---

### 2018081342001545_Question.md
# Ticket 2018081342001545

 # HPC Support Ticket: CPU Processing on tinygpu

## Keywords
- CPU processing
- tinygpu
- GPU
- CPU cores
- main memory
- compute node

## Problem
- User is unclear about how CPU processing works on tinygpu.
- User wants to know the number of available CPUs and whether they use the CPUs of another system (woody).

## Root Cause
- Lack of understanding about the CPU allocation and usage on tinygpu.

## Solution
- For each GPU on tinygpu, 4 dedicated CPU cores are allocated.
  - Type "Intel Nehalem" for GTX980 GPUs (tg00x nodes).
  - Type "Intel Broadwell" for GTX1080 GPUs (tg03x nodes).
- Each GPU also comes with at least 11.5 GB of main memory on the host.
- If 2 GPUs are requested in a single job, the user gets twice the cores and twice the host's main memory.
- The CPU cores and main memory are local to the compute node holding the assigned GPU.

## General Learning
- Understanding the allocation of CPU cores and main memory for GPUs on tinygpu.
- Clarification that the resources are local to the compute node and not shared with other systems like woody.

## Additional Notes
- This information is crucial for users to optimize their job submissions and resource allocation on tinygpu.
---

### 2022070542001189_Job%20auf%20TinyGPU%20nutzt%20die%20GPUs%20nicht%20%5Biwso061h%5D.md
# Ticket 2022070542001189

 # HPC Support Ticket: Job auf TinyGPU nutzt die GPUs nicht

## Keywords
- TinyGPU
- GPU utilization
- nvidia-smi
- Monitoring system
- Resource allocation

## Problem Description
The user's job on TinyGPU (JobID 271925) was not utilizing any of the 4 requested GPUs.

## Root Cause
The user's code was not configured to use the GPUs, leading to idle resources.

## Solution
1. **Monitor GPU Utilization**: Use `nvidia-smi` to check the current GPU usage.
   ```bash
   ssh <node>
   nvidia-smi
   ```
2. **Ensure Code Uses GPUs**: Verify that the code is capable of utilizing GPUs and is properly configured to do so.
3. **Documentation**: Refer to the documentation for working with NVIDIA GPUs: [Working with NVIDIA GPUs](https://hpc.fau.de/systems-services/systems-documentation-instructions/special-applications-and-tips-tricks/working-with-nvidia-gpus/).

## Lessons Learned
- Always ensure that the code is capable of utilizing GPUs before requesting GPU nodes.
- Use monitoring tools like `nvidia-smi` to check GPU utilization.
- Proper resource allocation helps in efficient use of HPC resources.

## Additional Notes
- The user acknowledged the mistake and stopped the job after fixing the issue.
- The HPC Admin provided a screenshot from the monitoring system to illustrate the problem.

## References
- [Working with NVIDIA GPUs](https://hpc.fau.de/systems-services/systems-documentation-instructions/special-applications-and-tips-tricks/working-with-nvidia-gpus/)
---

### 2023020942000877_Tier3-Access-Alex%20%22Carlotta%20Anem%C3%83%C2%BCller%22%20_%20iwal078h.md
# Ticket 2023020942000877

 # HPC Support Ticket Analysis

## Keywords
- HPC Account Activation
- Certificate Expiration
- GPGPU Cluster Access
- Nvidia A100 GPUs
- Python
- Audio Signal Processing

## Summary
- **User Request**: Access to GPGPU cluster 'Alex' with Nvidia A100 GPUs for audio signal decorrelation using DNNs.
- **Issue**: Certificate expiration.
- **Solution**: HPC Admin enabled the user's account after addressing the certificate issue.

## Details
- **Contact**: User from audiolabs-erlangen.de
- **Required Resources**:
  - GPGPU cluster 'Alex'
  - Nvidia A100 GPUs (40 GB, 9.7 TFlop/s double precision)
  - Python software
- **Expected Outcome**: Improved audio signal decorrelation methods.

## Root Cause
- Expired certificate prevented account activation.

## Solution
- HPC Admin (Thomas Zeiser) enabled the user's account after resolving the certificate issue.

## General Learnings
- Certificate expiration can prevent account activation.
- HPC Admins can resolve such issues and enable user accounts.
- Users may request specific hardware and software for their projects.
---

### 2022020442001216_Job%20makes%20no%20use%20of%20GPU%20%5Biwb0010h%5D.md
# Ticket 2022020442001216

 # HPC Support Ticket: Job Makes No Use of GPU

## Keywords
- GPU allocation
- Job script
- Resource utilization
- Monitoring system

## Problem
- User allocated two A100 GPUs but only used one.
- Inefficient resource utilization.

## Root Cause
- User was unaware of the actual GPU usage in their job script.

## Solution
- User was advised to allocate only the number of GPUs actually needed.
- User agreed to interrupt and restart the job with the correct resource allocation.

## Lessons Learned
- Importance of monitoring resource usage.
- Ensuring job scripts accurately reflect resource needs.
- Educating users on efficient resource allocation.

## Actions Taken
- HPC Admin notified the user about the issue.
- User acknowledged the mistake and agreed to correct it.
- Ticket closed with the expectation that the user will be more attentive in the future.

## Follow-Up
- No further action required from HPC Admin.
- User will restart the job with the correct GPU allocation.
---

### 2022022442001778_Jobs%20pending%20mit%20AssocGrpGRES.md
# Ticket 2022022442001778

 # HPC Support Ticket: Jobs Pending with Reason "AssocGrpGRES"

## Keywords
- Slurm
- AssocGrpGRES
- GPU
- Quota
- Pending Jobs

## Problem Description
User's jobs are pending with the reason "AssocGrpGRES". The user understands that this means they cannot request more GRES "gpu:1" resources at this time but is unsure why this reason is being given. The user has no other jobs running and nodes seem available.

## Root Cause
The "AssocGrpGRES" message indicates that a limit set in the Slurm batch system for the user, group, partition, or QOS has been exceeded. In this case, the group's GPU quota has been exceeded.

## Solution
- **User Action**: The user should check with their colleagues to ensure they are using GPUs efficiently and consider requesting additional resources from their admin.
- **Admin Action**: Verify the group's GPU usage and adjust quotas if necessary.

## General Learnings
- **Quota Limits**: Be aware of the GPU quotas set for users, groups, partitions, or QOS in the Slurm batch system.
- **Resource Management**: Efficiently manage and monitor resource usage to avoid exceeding quotas.
- **Communication**: Clearly communicate with colleagues and admins regarding resource needs and limitations.

## Related Documentation
- [Slurm Documentation on GRES](https://slurm.schedmd.com/gres.html)
- [FAU HPC Services](http://hpc.fau.de/)

## Ticket Status
Resolved. The user understood the issue and planned to address it with their colleagues and admin.
---

### 2023062942003178_Tier3-Access-Alex%20%22Amir%20El-Ghoussani%22%20_%20iwnt001h.md
# Ticket 2023062942003178

 # HPC Support Ticket Conversation Analysis

## Keywords
- Tier3-Access
- GPU-hours
- NHR-Antrag
- DFG-Förderung
- GPGPU cluster
- Nvidia A100
- Nvidia A40
- Python
- Deep learning
- Diffusion models
- Semantic segmentation
- Depth estimation
- Domain adaptation

## Summary
- **User Request:** Access to Tier3 resources for deep learning training.
- **Initial Request:** 100,000 GPU-hours.
- **HPC Admin Response:** Request exceeds Tier3 capabilities, recommended to apply for NHR resources.
- **Follow-up Question:** Clarification on the range of GPU-hours available through Tier3.
- **HPC Admin Clarification:** Tier3 provides up to 6000 GPU-hours for A40 and 4000 GPU-hours for A100.
- **User Adjustment:** Reduced request to 3000 GPU-hours.
- **HPC Admin Action:** Account enabled for the user.

## Root Cause of the Problem
- Initial request for GPU-hours exceeded Tier3 capabilities.

## Solution
- User was advised to apply for NHR resources for larger GPU-hour needs.
- User adjusted the request to fit within Tier3 capabilities.
- HPC Admin enabled the user's account for the adjusted request.

## General Learnings
- Tier3 resources have specific limits for GPU-hours.
- For larger computational needs, users should apply for NHR resources.
- Adjusting requests to fit within available resources can lead to quicker resolution.

## References
- [NHR Application Rules](https://hpc.fau.de/systems-services/documentation-instructions/nhr-application-rules/)
- HPC Support Contact: support-hpc@fau.de
---

### 2024080242002401_Your%20job%20on%20TinyGPU%20%28JobID%20869667%29%20is%20not%20using%20all%20GPU%20ressources.md
# Ticket 2024080242002401

 # HPC Support Ticket Analysis: Job Not Using All GPU Resources

## Keywords
- GPU utilization
- JobID
- Monitoring system
- ClusterCockpit
- `nvidia-smi`
- Resource allocation
- `--ntasks-per-node`
- `CUDA_LAUNCH_BLOCKING`

## Summary
A user's job on TinyGPU was not utilizing all allocated GPU resources. The HPC Admin provided guidance on monitoring GPU usage and optimizing resource allocation.

## Root Cause
- The job was using only one of the four allocated GPUs.
- Potential misconfiguration or underutilization of resources.

## Solution
- **Monitoring GPU Usage**:
  - Use ClusterCockpit: [Monitoring System](https://monitoring.nhr.fau.de/)
  - Attach to the running job: `srun --pty --overlap --jobid YOUR-JOBID bash`
  - Check GPU utilization: `nvidia-smi`

- **Optimize Resource Allocation**:
  - Ensure the code can utilize all allocated GPUs.
  - Review the use of `--ntasks-per-node=2` and `CUDA_LAUNCH_BLOCKING=1`.

## Additional Remarks
- **`--ntasks-per-node=2`**: The reason for this setting was questioned.
- **`CUDA_LAUNCH_BLOCKING=1`**: Potentially set for debugging purposes.

## Conclusion
The ticket was closed due to no response from the user. The provided guidance can help future users optimize their GPU resource usage and avoid idle resources.

---

This report aims to assist HPC support employees in resolving similar issues related to GPU resource utilization and job configuration.
---

### 2021112342002754_Jobs%20on%20V100%20GPUs%20-%20btr000h.md
# Ticket 2021112342002754

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject: Jobs on V100 GPUs - btr000h

### Keywords:
- V100 GPUs
- TinyGPU
- Job Monitoring
- GPU Utilization

### Summary:
- **Issue**: User's jobs on V100 GPUs were not utilizing the GPUs.
- **Root Cause**: Unspecified, but likely due to misconfiguration or oversight in job setup.
- **Solution**: User was notified to check and correct job configurations.

### Lessons Learned:
- **Monitoring**: Regular monitoring of job performance and resource utilization is crucial.
- **User Notification**: Promptly inform users about inefficient resource usage to ensure optimal performance.
- **Job Configuration**: Ensure users are aware of proper job configuration to effectively utilize GPU resources.

### Actions Taken:
- HPC Admin notified the user about the issue.
- User acknowledged the problem and committed to correcting it.

### Recommendations:
- Provide guidelines or training on proper job configuration for GPU utilization.
- Implement automated alerts for underutilized resources to prompt user action.
```
---

### 2021090142003218_Problems%20with%20Tiny%20GPU.md
# Ticket 2021090142003218

 # HPC Support Ticket: Problems with Tiny GPU

## Keywords
- Tiny GPU
- A100 nodes
- Job submission
- Job status
- Slurm
- Prolog script
- Drop caches
- CG state

## Problem Description
- User unable to submit new jobs to Tiny GPU (A100 nodes).
- No output files (*.o*) generated for jobs.
- Active jobs not visible, but two old jobs in "CG" state are present and cannot be killed.

## Root Cause
- The prolog script (`/etc/slurm/slurm.prolog`) was hanging due to the command `sync && echo 3 > /proc/sys/vm/drop_caches`.
- Jobs were stuck in the "CG" (completing) state on the node.

## Solution
- HPC Admin identified and resolved the issue with the prolog script.
- Removed the stuck jobs in the "CG" state.
- Confirmed with the user that job submission and processing are functioning normally again.

## Lessons Learned
- Prolog scripts can cause job submission issues if they hang or contain problematic commands.
- Jobs stuck in the "CG" state can prevent new job submissions.
- Regularly check and maintain prolog scripts to avoid such issues.
- Quick resolution of stuck jobs can prevent further disruptions in job processing.

## Actions Taken
- HPC Admin investigated the prolog script and found the hanging command.
- Stuck jobs were removed from the node.
- User confirmed that job submission and processing were back to normal.

## Follow-up
- Monitor prolog scripts for any potential issues.
- Regularly check for jobs stuck in unusual states and resolve them promptly.
- Ensure users are informed about the resolution and can resume their work without further issues.
---

### 2023040542002708_Not%20utilizing%20all%20requested%20GPUs%20on%20Alex%20%28iwal020h%29.md
# Ticket 2023040542002708

 # HPC Support Ticket: Not Utilizing All Requested GPUs

## Keywords
- GPU utilization
- Job management
- Resource allocation
- `srun`
- `nvidia-smi`

## Summary
A user was running jobs on the Alex cluster that were not utilizing all the requested GPUs, leading to resource wastage.

## Root Cause
- The user's jobs were requesting two GPUs but only utilizing one.

## Solution
- The HPC Admin informed the user about the issue and provided instructions on how to check GPU utilization using `srun` and `nvidia-smi`.
- The user acknowledged the issue and agreed to address it.

## Steps to Check GPU Utilization
1. Attach to the running job using:
   ```bash
   srun --pty --jobid <job_id> bash
   ```
2. Check GPU utilization with:
   ```bash
   nvidia-smi
   ```

## General Learning
- Always ensure that the requested resources, such as GPUs, are fully utilized to avoid wastage.
- Use `srun` and `nvidia-smi` to monitor GPU utilization in running jobs.
- Communicate with users to resolve resource allocation issues promptly.

## Roles Involved
- HPC Admins
- User (not specified)

## Status
- The ticket was closed after the user acknowledged the issue.
---

### 2023040342004291_Tier3-Access-Alex%20%22Kishan%20Gupta%22%20_%20iwal044h.md
# Ticket 2023040342004291

 # HPC Support Ticket Analysis

## Keywords
- HPC Account Activation
- Login Instructions
- Certificate Expiration
- GPGPU Cluster 'Alex'
- Nvidia A100 GPGPUs
- Python, Pytorch
- Speech Synthesis
- Audio Coding
- Fraunhofer IIS

## Summary
- **User Issue**: User's HPC account was enabled, but they had not followed the login instructions provided by the HPC Admin.
- **Root Cause**: User did not complete the required steps to log in with their FHG SSO credentials.
- **Solution**: HPC Admin reminded the user to follow the instructions from the initial email to log in to the portal.

## General Learnings
- Always ensure users follow the complete set of instructions for account activation and login.
- Certificate expiration can be a common issue; remind users to update their certificates as needed.
- Users from external organizations like Fraunhofer IIS may require specific instructions for accessing HPC resources.

## Action Items
- **HPC Admins**: Ensure clear communication of login instructions and follow up with users who do not complete the process.
- **2nd Level Support Team**: Be prepared to assist users with certificate renewals and login issues.
- **Head of Datacenter/Training and Support Group Leader**: Consider creating a FAQ or tutorial for common login and certificate issues.

## Additional Notes
- The user required access to the GPGPU cluster 'Alex' for speech synthesis and audio coding using Python and Pytorch.
- The expected outcome was an end-to-end speech codec with excellent perceptual quality at very low bitrates.

This analysis can help in resolving similar issues related to account activation and login procedures in the future.
---

### 2018052942002243_Jobs%20auf%20TinyGPU%20-%20iwal005h.md
# Ticket 2018052942002243

 # HPC Support Ticket: Jobs auf TinyGPU - iwal005h

## Summary
- **Subject**: Jobs auf TinyGPU - iwal005h
- **Issue**: Jobs are allocating GPU memory but showing 0% GPU utilization.
- **Affected System**: TinyGPU
- **Tools Used**: `nvidia-smi`, `qstat.tinygpu -rn`

## Keywords
- GPU utilization
- `nvidia-smi`
- `qstat.tinygpu -rn`
- Job monitoring
- SSH login

## Problem Description
- Jobs are running on TinyGPU but showing 0% GPU utilization despite allocating GPU memory.
- User was informed about the issue and provided with steps to monitor GPU usage.

## Steps to Monitor GPU Usage
1. **Identify Current Nodes**: Use `qstat.tinygpu -rn` to identify the nodes currently allocated to the user's jobs.
2. **SSH Login**: Log in to the identified nodes via SSH.
3. **Check GPU Usage**: Use `nvidia-smi` to check the GPU utilization.

## Example Output
```
+-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|===============================+======================+======================|
|   0  GeForce GTX 1080    On   | 00000000:02:00.0 Off |                  N/A |
| 30%   45C    P2    39W / 180W |   7757MiB /  8119MiB |      1%      Default |
+-------------------------------+----------------------+----------------------+
|   1  GeForce GTX 1080    On   | 00000000:03:00.0 Off |                  N/A |
| 32%   48C    P2    40W / 180W |   7757MiB /  8119MiB |      1%      Default |
+-------------------------------+----------------------+----------------------+
|   2  GeForce GTX 1080    On   | 00000000:82:00.0 Off |                  N/A |
| 31%   46C    P2    39W / 180W |   7757MiB /  8119MiB |      1%      Default |
+-------------------------------+----------------------+----------------------+
|   3  GeForce GTX 1080    On   | 00000000:83:00.0 Off |                  N/A |
| 34%   52C    P2    41W / 180W |   7757MiB /  8119MiB |      1%      Default |
+-------------------------------+----------------------+----------------------+
```

## Root Cause
- The jobs are not effectively utilizing the GPU resources despite allocating memory.

## Solution
- User was advised to investigate and optimize their jobs to improve GPU utilization.
- No specific solution was provided, but the user was encouraged to address the issue.

## Follow-up
- HPC Admin followed up with the user to check if the issue persisted.
- The user was informed that their jobs continued to show poor GPU utilization.

## Conclusion
- The user needs to optimize their jobs to improve GPU utilization.
- Monitoring tools like `nvidia-smi` and `qstat.tinygpu -rn` are essential for diagnosing such issues.
---

### 2020061942000436_bad%20utilization%20of%20GPUs%20-%20iwsp023h.md
# Ticket 2020061942000436

 # HPC Support Ticket: Bad Utilization of GPUs

## Subject
Bad utilization of GPUs - iwsp023h

## Issue Description
- User's recent jobs on TinyGPU request full nodes with four GPUs.
- Job scripts run multiple Python processes without assigning specific GPUs.
- All processes run on the first GPU, leaving the other three GPUs idle.

## Root Cause
- Lack of GPU assignment in job scripts leads to inefficient resource utilization.

## Diagnostic Information
- **NVIDIA-SMI Output:**
  ```
  +-------------------------------+----------------------+----------------------+
  | GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
  | Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
  |===============================+======================+======================|
  |   0  GeForce GTX 1080    On   | 00000000:02:00.0 Off |                  N/A |
  | 51%   75C    P2   102W / 180W |    864MiB /  8119MiB |    100%      Default |
  +-------------------------------+----------------------+----------------------+
  |   1  GeForce GTX 1080    On   | 00000000:03:00.0 Off |                  N/A |
  | 27%   34C    P8     7W / 180W |     12MiB /  8119MiB |      0%      Default |
  +-------------------------------+----------------------+----------------------+
  |   2  GeForce GTX 1080    On   | 00000000:82:00.0 Off |                  N/A |
  | 27%   34C    P8     8W / 180W |     12MiB /  8119MiB |      0%      Default |
  +-------------------------------+----------------------+----------------------+
  |   3  GeForce GTX 1080    On   | 00000000:83:00.0 Off |                  N/A |
  | 27%   32C    P8     7W / 180W |     12MiB /  8119MiB |      0%      Default |
  +-------------------------------+----------------------+----------------------+
  ```

## Solution
- Assign specific GPUs to each Python process in the job script to ensure even distribution of workload across all available GPUs.

## Keywords
- GPU utilization
- Job script
- Python processes
- NVIDIA-SMI
- Resource allocation

## General Learning
- Always assign specific GPUs to processes in job scripts to optimize resource utilization.
- Monitor GPU usage using tools like NVIDIA-SMI to identify and resolve inefficiencies.
---

### 2024100442000403_Tier3-Access-Alex%20%22Lukas%20Rosteck%22%20_%20iwi5228h.md
# Ticket 2024100442000403

 ```markdown
# HPC Support Ticket Analysis

## Subject
Tier3-Access-Alex "Lukas Rosteck" / iwi5228h

## Keywords
- GPU utilization
- PyTorch
- Job setup
- Data staging
- TinyGPU
- Anomaly detection
- CNC machine data

## Summary
- **User Issue**: Low GPU utilization (5-20%) in jobs on TinyGPU.
- **HPC Admin Observation**: No data staging in job scripts.
- **User Response**: Found and fixed the error in the code.

## Root Cause
- Low GPU utilization due to inefficient job setup and lack of data staging.

## Solution
- User identified and corrected an error in the code.
- HPC Admin suggested connecting with a colleague for further assistance with PyTorch and job setup.

## General Learnings
- Importance of data staging in job scripts for efficient GPU utilization.
- Monitoring GPU utilization metrics to identify performance issues.
- Collaboration with colleagues for specialized support in specific software and job setup.

## References
- [Data Staging Documentation](https://doc.nhr.fau.de/data/staging/)
- [Job Monitoring](https://monitoring.nhr.fau.de/monitoring/user/iwi5228h)
```
---

### 2024061242001217_Tier3-Access-Alex%20%22Annika%20Hofmann%22%20_%20iwbi018h.md
# Ticket 2024061242001217

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject
Tier3-Access-Alex "Annika Hofmann" / iwbi018h

## Keywords
- Tier3 Access
- Alex Cluster
- Nvidia A100 GPGPUs
- Python
- MRI Image Reconstruction
- GPU-hours

## Summary
A user requested access to the GPGPU cluster 'Alex' for MRI image reconstruction using Python. The request included specifications for GPU-hours and expected outcomes.

## Root Cause of the Problem
- User needed access to the 'Alex' cluster for a specific project.

## Solution
- HPC Admin granted access to the user for the 'Alex' cluster.

## What Can Be Learned
- Proper procedure for requesting access to HPC resources.
- Importance of specifying required resources and expected outcomes in the request.
- HPC Admin's role in granting access and managing user requests.
```
---

### 2022060742000661_Jobs%20on%20Alex%20not%20using%20all%20the%20allocated%20GPUs%20%5Bihpc060h%5D.md
# Ticket 2022060742000661

 # HPC Support Ticket: Jobs Not Using All Allocated GPUs

## Keywords
- SLURM
- GPU allocation
- Multi-node jobs
- CUDA
- Exclusive node allocation

## Problem Description
- User's multi-node jobs requested exclusive nodes but did not fully utilize the allocated GPUs.
- Each node has 8 GPUs, but only one GPU per node was utilized.
- User's script did not recognize all available GPUs in multi-node jobs.

## Root Cause
- The SLURM job script specified `--gres=gpu:a100:1`, limiting each node to use only one GPU.

## Solution
- Update the SLURM job script to specify the correct number of GPUs per node using `--gres=gpu:a100:8`.

## Additional Notes
- The user's program requires a specific number of GPUs tied to a model parameter.
- Allocating nodes exclusively for benchmarking purposes is acceptable to avoid interference from other jobs.

## Follow-up
- Ensure that the job script correctly reflects the number of GPUs required for the task.
- Monitor job performance to verify that all allocated GPUs are being utilized efficiently.

## General Learning
- Always check the SLURM job script for correct resource allocation.
- Ensure that the application can recognize and utilize all allocated resources, especially in multi-node setups.
- Exclusive node allocation can be justified for benchmarking to avoid interference from other jobs.
---

### 2022092142001403_Tier3-Access-Alex%20%22Luisa%20Neubig%22%20_%20iwb3001h.md
# Ticket 2022092142001403

 # HPC Support Ticket Analysis: Tier3-Access-Alex

## Keywords
- Tier3 Access
- GPU Hours
- NHR Project
- Application Rules
- GPU Allocation
- Evolutionary Algorithms
- Biomedical Segmentation
- Deep Neural Networks

## Summary
A user requested a significant amount of GPU hours for a project involving deep neural networks and biomedical segmentation. The request exceeded the free Tier3 access limit, prompting the HPC Admin to suggest applying for an NHR project. Temporary access was granted while the user was advised to apply for a larger project.

## Problem
- **Root Cause**: The user requested 69,120 GPU hours, which exceeds the free Tier3 access limit.
- **Details**: The user needed GPU resources for a project involving the systematic analysis of normalization layers in biomedical semantic segmentation deep neural networks using evolutionary neural architecture search.

## Solution
- **Immediate Action**: The HPC Admin granted 1,000 GPU hours temporarily.
- **Long-term Action**: The user was advised to apply for an NHR project and provided with the application rules and contact information for assistance.

## Lessons Learned
- **Resource Allocation**: Understand the limits of free Tier3 access and the need for larger projects to apply for NHR grants.
- **Communication**: Clearly communicate the allocation of GPU hours (total vs. per GPU) to avoid confusion.
- **Application Process**: Be aware of the application process for NHR projects and provide users with the necessary resources and support.

## Additional Notes
- The user was using evolutionary algorithms that required multiple GPUs for efficient training.
- The walltime of 72 hours was considered high, and the user planned to reduce it through parallelization.

## References
- [NHR Application Rules](https://hpc.fau.de/systems-services/documentation-instructions/nhr-application-rules/)
- HPC Support Contact: support-hpc@fau.de
- NHR Rechenzeit Support: harald.lanig@fau.de
---

### 2023052242001756_Error%20in%20setting%20slurm%20file.md
# Ticket 2023052242001756

 # HPC Support Ticket: Error in Setting Slurm File

## Keywords
- Slurm
- Generic Resource (GRES)
- Frontend
- GPU
- `sbatch`
- `salloc`
- `nvidia-smi`

## Problem Description
- User encountered an error: `sbatch: error: Invalid generic resource (gres) specification` after a system update.
- The error occurred while setting the Slurm file for job submission.

## Ticket Conversation Summary
- **User**: Reported the error and attached the Slurm file.
- **HPC Admin**: Requested more information about the frontend used and the command run.
- **User**: Clarified that they were using the `tinyx` frontend and simply using the batch filename for job execution.
- **HPC Admin**: Suggested testing commands and modifying the Slurm script to diagnose the issue.
- **HPC Admin**: Identified that the user's job was running but not utilizing the GPU, provided instructions to check GPU utilization.

## Root Cause
- The issue was likely due to an incorrect or outdated GRES specification in the Slurm script after the system update.

## Solution
- **Diagnostic Steps**:
  - Run `salloc.tinygpu --gres=gpu:1 --time=00:30:00` to test GRES allocation.
  - Remove the line `#SBATCH --gres=gpu:1` from the script and check if `sbatch filename` produces an error.
- **Monitoring**:
  - Use `srun --pty --overlap --jobid YOUR-JOBID bash` to attach to the running job.
  - Run `nvidia-smi` to check GPU utilization.

## General Learnings
- Ensure that GRES specifications in Slurm scripts are compatible with the current system configuration.
- Verify that jobs requesting specific resources (e.g., GPUs) are actually utilizing those resources.
- Use diagnostic commands and monitoring tools to troubleshoot resource allocation issues.

## Closure
- The ticket was closed after verifying that the jobs were running correctly and utilizing resources efficiently.
---

### 2020060442002202_Which%20cluster%20to%20use%3F.md
# Ticket 2020060442002202

 # HPC-Support Ticket Conversation Analysis

## Subject: Which cluster to use?

### Keywords
- Cluster selection
- GPU offloading
- Performance improvement
- HPC support
- Inventory request
- Simulation
- Woody
- Emmy
- TinyGPU

### Root Cause of the Problem
- User uncertainty about which HPC cluster to use for simulations.

### Solution
- **Clusters in Use:**
  - Woody
  - Emmy
  - TinyGPU (if GPU offloading is possible)
- **Performance Improvement:**
  - Consider porting to GPU for potential performance gains.
  - Testing required to confirm performance improvements.

### General Learnings
- **Cluster Recommendations:**
  - Woody and Emmy are suitable for general simulations.
  - TinyGPU is recommended if the program can offload work to the GPU.
- **Support and Communication:**
  - Ensure timely responses to user queries to avoid delays.
  - Provide clear guidance on cluster selection based on user needs.

### Additional Information
- **Usage Statistics:**
  ```
  hpcsystem      acctime [h]
  Emmy           108877.7
  TinyGPU        49433.7
  Woody          17074.2
  ```
- **Contact Information:**
  - HPC Services: support-hpc@fau.de
  - Website: [HPC RRZE](http://www.hpc.rrze.fau.de/)

### Conclusion
- Users should be guided to select appropriate clusters based on their simulation requirements.
- GPU offloading can be beneficial for performance but requires testing.
- Ensure prompt and clear communication to enhance user support experience.
---

### 2022062842001718_Job%20on%20TinyGPU%20does%20not%20use%20GPU%20%5Bexzi003h%5D.md
# Ticket 2022062842001718

 # HPC Support Ticket: Job on TinyGPU does not use GPU

## Keywords
- TinyGPU
- GPU utilization
- `nvidia-smi`
- Job monitoring
- Gromacs

## Summary
A user reported that one of their jobs on TinyGPU was not using the GPU. The HPC Admin provided instructions to check GPU utilization using `nvidia-smi` and shared a screenshot from the monitoring system. The user did not see any issues with GPU usage based on the provided information.

## Root Cause
- The issue was on the HPC side, where the job-to-GPU assignment in the monitoring system was incorrect due to discrepancies between the scheduler on the admin node and the execution daemon on the compute node.

## Solution
- The HPC Admin acknowledged the issue and confirmed that the GPU usage around 60-70% is normal for Gromacs. No user action was required.

## Lessons Learned
- Users can check GPU utilization using `nvidia-smi`.
- Monitoring systems may have discrepancies in job-to-GPU assignments.
- Normal GPU usage for Gromacs is around 60-70%.

## Follow-up Actions
- HPC Admins should investigate and resolve the monitoring system discrepancies.
- Users should be informed about expected GPU usage for different applications.
---

### 2025031142002776_Jobs%20do%20not%20fully%20use%20GPU%20%5Biwal%5D.md
# Ticket 2025031142002776

 # HPC Support Ticket: Jobs Do Not Fully Use GPU

## Keywords
- GPU utilization
- Preprocessing
- Job monitoring
- Resource allocation
- ClusterCockpit
- `nvidia-smi`
- `srun`
- `$TMPDIR`

## Problem Description
- User's job on TinyGPU not utilizing the GPU.
- Preprocessing step takes over 3 hours and does not require GPU.

## Root Cause
- Preprocessing step in the user's job does not utilize GPU resources but runs on GPU nodes, leading to idle GPU resources.

## Solution
- Offload preprocessing to a workstation or another cluster without GPU to free up GPU resources.
- Monitor GPU utilization using ClusterCockpit or `nvidia-smi` after attaching to the job with `srun`.

## General Learnings
- Ensure jobs allocated to GPU nodes actively use GPU resources.
- Preprocessing steps not requiring GPU should be run on non-GPU nodes.
- Use monitoring tools to check resource utilization.
- Consider data handling and temporary directory usage (`$TMPDIR`) for job efficiency.

## Additional Notes
- HPC Admin suggested the issue might be due to code compiled on the frontend.
- There is a mention of a potential "cluster-führerschein" to address resource management issues.

## Tools and Commands
- **ClusterCockpit**: Monitoring system to view job and resource utilization.
- **`nvidia-smi`**: Command to monitor GPU utilization.
- **`srun --pty --overlap --jobid YOUR-JOBID bash`**: Command to attach to a running job and get a shell on the first node.

## Contact Information
- **HPC Support**: support-hpc@fau.de
- **Monitoring System**: [ClusterCockpit](https://monitoring.nhr.fau.de/)
- **HPC Website**: [FAU HPC](https://hpc.fau.de/)
---

### 2023072442001276_Tier3-Access-Alex%20%22Paul%20Maria%20Scheikl%22%20_%20iwhr001h.md
# Ticket 2023072442001276

 # HPC Support Ticket Conversation Analysis

## Keywords
- HPC Account Activation
- GPU Hours
- NHR Application
- Supervised Learning
- Reinforcement Learning
- Robot-Assisted Surgery

## Summary
- **User Request**: Activation of HPC account for GPU cluster 'Alex' with a requirement of 20,000 GPU hours for supervised and reinforcement learning tasks in robot-assisted surgery research.
- **HPC Admin Response**: Account activated, but the requested GPU hours exceed typical FAU provision. Suggested applying for NHR compute time for the project.
- **User Follow-Up**: Acknowledgment and agreement to consider NHR application.

## Root Cause of the Problem
- User requested GPU hours significantly exceed the typical allocation provided by FAU.

## Solution
- HPC Admin activated the account and advised the user to apply for additional compute time through the NHR application process.

## General Learnings
- **Account Activation**: HPC Admins can activate accounts upon request.
- **Resource Allocation**: Users should be aware of typical resource allocations and consider applying for additional resources if needed.
- **NHR Application**: For extensive compute needs, users should consider submitting an NHR application for additional resources.
- **Communication**: Clear communication between users and HPC Admins is essential for managing resource allocations and project requirements.

## Relevant Links
- [NHR Application Rules](https://hpc.fau.de/systems-services/documentation-instructions/nhr-application-rules/)

## Roles Involved
- **HPC Admins**: Thomas Zeiser
- **User**: Paul Maria Scheikl

## Next Steps
- User to conduct initial tests and consider submitting an NHR application if the resource need is confirmed.

---

This analysis provides a concise overview of the support ticket conversation, highlighting key points and general learnings for future reference.
---

### 2024071542004823_Tier3-Access-Alex%20%22Maja%20Schlereth%22%20_%20iwb6001h.md
# Ticket 2024071542004823

 # HPC Support Ticket Analysis: Tier3-Access-Alex

## Keywords
- Tier3 Access
- Alex
- iwb6001h
- Account Setup
- GPGPU Cluster
- Nvidia A100
- Nvidia A40
- Python
- Multi-image Superresolution
- Magnetic Resonance Imaging (MRI)
- Implicit Neural Representation Learning

## Summary
- **User Request**: Access to GPGPU cluster 'Alex' for multi-image superresolution in MRI using Python.
- **Resources Requested**: Nvidia A100 and A40 GPUs.
- **Expected Outcome**: Improved resolution of MRI data.

## Actions Taken by HPC Admins
- Created a new account `iwb6` on Alex.
- Configured the account with `sacctmgr` commands:
  ```bash
  sacctmgr add account iwb6 set descr="Professur Artificial Intelligence in Medical Imaging (Prof. K. Breininger)" parent=fau
  sacctmgr update account iwb6 set GrpTRES=gres/gpu=16
  ```
- Granted access to the user with account `iwb6001h`.

## Lessons Learned
- **Account Setup**: Proper configuration of new accounts using `sacctmgr`.
- **Resource Allocation**: Allocation of GPU resources for specific projects.
- **User Communication**: Clear communication with users regarding access and resource allocation.

## Root Cause of the Problem
- User needed access to specific GPU resources for their project.

## Solution
- HPC Admins created and configured the necessary account and granted access to the user.

## Notes
- Ensure proper documentation and communication when setting up new accounts and allocating resources.
- Regularly update and verify account configurations to avoid access issues.
---

### 2020083142003031_pool%20GPU%20utilization%20of%20jobs%20on%20TinyGPU%20-%20iwal021h.md
# Ticket 2020083142003031

 # HPC-Support Ticket Conversation: Poor GPU Utilization on TinyGPU

## Subject
- **Issue**: Poor GPU utilization of jobs on TinyGPU
- **User**: User running DNN/ML/DL workloads

## Keywords
- GPU utilization
- Data loading
- CPU performance counters
- Node-local SSD
- Temporary directory ($TMPDIR)

## Problem Description
- User's jobs show low GPU utilization (~2-3%).
- GPUs are in deep power save mode due to insufficient workload.
- CPU is running on a single core and is idle 50% of the time.

## Root Cause
- Inefficient data loading process: Files are loaded on the CPU and then converted to GPU, leading to low GPU utilization.
- Many small-size random accesses to input data, causing high latency.

## Solutions and Recommendations
- **Improve Data Loading**:
  - Consider loading data offline and saving it in a format readable by the DNN framework to reduce loading time.
  - Copy input data to node-local SSD ($TMPDIR) at the beginning of the job to reduce access latency.

- **Job Script Modification**:
  ```bash
  #!/bin/bash -l
  #PBS -lnodes=1:ppn=4
  # Copy input data to node-local SSD
  cd $TMPDIR
  cp $VAULT/input-files*.dat .
  # Run the job
  python my-dnn.py
  # Cleanup
  cd
  rm -rf $TMPDIR/*
  ```

- **Avoid Using /tmp**:
  - $TMPDIR is defined only within a running PBS job.
  - Using /tmp in the job script is not recommended as it is on a smaller SSD than $TMPDIR.

## Additional Notes
- The batch system can handle the number of jobs; the focus should be on improving job efficiency.
- Proper DNN/ML/DL workloads typically show 40-60% GPU utilization.
- Regular monitoring and adjustments can significantly reduce processing time.

## Follow-up
- Monitor future jobs to check for improvements in GPU utilization.
- User can join the HPC Café for further assistance.

---

This report provides a summary of the issue, the root cause, and the recommended solutions for improving GPU utilization in DNN/ML/DL workloads on the TinyGPU cluster.
---

### 2023052342000817_Assessing%20Hardwares.md
# Ticket 2023052342000817

 # HPC Support Ticket: Assessing Hardwares

## Keywords
- HPC Application Form
- Technical Requirements
- TinyGPU Cluster
- Deep Learning Model
- GPU Allocation
- Account Application

## Problem
- User needs to specify technical requirements for HPC application form.
- User has limited prior knowledge about the technical specifications.
- User needs to understand how to allocate GPUs and how other group members can gain access.

## Solution
### Technical Requirements for Application Form
- **Code/Program Information**:
  - Specify the code/program to be run, e.g., `python, pytorch/tensorflow, AI training`.
- **Hardware Requirements**:
  - **HPC-Zielsysteme**: TinyGPU
  - **Typische Jobgröße**: Number of GPUs per training (1-8)
  - **Insges. benötigte Rechenzeit**: Total compute time in GPU hours (500-1000 hours is common for small projects)
  - **Benötigter Speicherplatz**: Each account comes with ~1TB disk space. Further communication is needed if a larger dataset is required.

### GPU Allocation
- Users can request an individual number of GPUs for every SLURM job.

### Account Application for Group Members
- Every user must apply for their own account.

## Additional Information
- Involve the relevant contact person (e.g., Head of IT) for signing the application.
- Users can seek assistance in completing the form by visiting the IT department.

## Conclusion
- The user was provided with detailed instructions on how to fill out the technical requirements section of the HPC application form.
- The user was informed about the process for GPU allocation and account application for group members.
- The user was advised to involve the relevant contact person for signing the application and to seek assistance if needed.
---

### 2022022242001325_NHR-Vormerkliste%20%22Marco%20Heisig%22%20_%20FAU%20Erlangen-N%C3%83%C2%BCrnberg.md
# Ticket 2022022242001325

 ```markdown
# HPC Support Ticket Analysis

## Subject
NHR-Vormerkliste "Marco Heisig" / FAU Erlangen-Nürnberg

## Keywords
- Early-User Access
- Alex Cluster
- Fritz Cluster
- Clang
- Lisp
- GPGPU
- CUDA
- SBCL
- HPC Support

## Summary
- **User Request**: Access to Alex and Fritz clusters for familiarization with new systems.
- **Resources Requested**:
  - GPGPU cluster 'Alex' / Nvidia A100 GPGPUs
  - GPGPU cluster 'Alex' / Nvidia A40 GPGPUs
  - Parallel computer 'Fritz' (2x Intel Xeon 'IceLake')
- **Applications**: CUDA, Clang & GCC, SBCL
- **Compute Time**: Less than 1000 GPU hours

## HPC Admin Response
- **Access Granted**: User granted early-user access to Alex and Fritz clusters.
- **Documentation Links**:
  - [Alex Cluster Documentation](https://hpc.fau.de/systems-services/systems-documentation-instructions/clusters/alex-cluster/)
  - [Fritz Cluster Documentation](https://hpc.fau.de/systems-services/systems-documentation-instructions/clusters/fritz-cluster/)
- **Notes**:
  - Clang not currently available.
  - User expected to handle Lisp-related tasks independently.

## Root Cause of the Problem
- User needed access to specific HPC resources for familiarization and support purposes.

## Solution
- HPC Admin granted early-user access to the requested clusters and provided relevant documentation links.

## General Learnings
- **Access Management**: HPC Admins can grant early-user access to specific clusters for familiarization.
- **Documentation**: Important to provide links to relevant documentation for new users.
- **Self-Management**: Users may need to handle certain tasks independently, such as Lisp-related tasks.
```
---

### 2023090442003325_Jobs%20stellen%20nach%20einiger%20Zeit%20Arbeit%20ein%20%5Bmppm001h%5D.md
# Ticket 2023090442003325

 ```markdown
# HPC Support Ticket: Jobs Stop After 6h 40min on TinyGPU

## Keywords
- TinyGPU
- Job Failure
- Host Issues
- Logfiles
- ClusterCockpit
- Fehlermeldungen

## Summary
Jobs on TinyGPU are stopping after 6 hours and 40 minutes. Jobs prior to September 2, 2023, completed successfully.

## Problem Description
- Jobs on TinyGPU stop after 6 hours and 40 minutes.
- Logfiles show errors at the beginning of the job, but these errors do not directly indicate the cause of the job stoppage.
- Suspected issue with the host `lpmt092.biomed.uni-erlangen.de` being unreachable or not delivering further jobs.

## Steps Taken
- HPC Admin provided a screenshot from ClusterCockpit.
- User was advised to check the jobs on the monitoring website.
- User was asked to verify if there are issues with the host or other parts of the system.

## Root Cause
- Potential issue with the host `lpmt092.biomed.uni-erlangen.de` being unreachable or not delivering further jobs.

## Solution
- User to investigate the host `lpmt092.biomed.uni-erlangen.de` for any issues.
- Further support available from HPC Admins for troubleshooting.

## Additional Information
- User ended the jobs after noticing no results.
- HPC Admins are available for further assistance in identifying and resolving the issue.
```
---

### 2023110142000329_Abuse%20of%20Alex%20-%20b112dc10.md
# Ticket 2023110142000329

 # HPC Support Ticket: Abuse of Alex - b112dc10

## Keywords
- CPU-only jobs
- GPU allocation
- Job throttling
- Project quota
- Scripting error
- Job submission loop

## Summary
A user submitted a large number of jobs on the Alex system without utilizing the GPUs, leading to excessive resource consumption and project quota overuse.

## Root Cause
- The user's job script contained a `while true` loop that continuously submitted new jobs every 5 minutes, leading to over 10,000 jobs in the queue.
- The script did not properly check if the work was completed before entering the loop, causing it to run indefinitely.

## Solution
- The HPC Admins removed the excessive jobs from the queue and implemented throttling policies for the project.
- The user was advised to:
  - Test jobs locally before submitting them to the HPC system.
  - Ensure that the job script properly completes all work before entering any loops that submit new jobs.
  - Add a check before the `sbatch` command to ensure that the present job ran for a minimum time.
- The user was also informed about alternative systems for CPU-only jobs, such as Fritz and Woody, and how to manage file permissions for shared access.

## General Learnings
- Always test job scripts locally before submitting them to the HPC system.
- Ensure that job scripts properly complete all work before entering loops that submit new jobs.
- Be aware of the resource allocation policies for different systems (e.g., GPU allocation on Alex, CPU-only jobs on Fritz or Woody).
- Regularly monitor project quota usage and submit extension requests as needed.
- When encountering issues with job scripts, consult with the 2nd Level Support team or HPC Admins for assistance.

## Related Links
- [NHR Application Rules](https://hpc.fau.de/systems-services/documentation-instructions/nhr-application-rules/)
- [FAU HPC Documentation](https://hpc.fau.de/)
---

### 2017030942000832_Question%20about%20the%20new%20cluster.md
# Ticket 2017030942000832

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject: Question about the new cluster

### Keywords:
- Meggie
- General usage
- Early access
- MD simulations
- Amber
- TinyGPU
- Queue times
- Priority access

### Summary:
- **User Inquiry:** Request for access to the Meggie cluster for general usage or early access.
- **HPC Admin Response:** Meggie is not open for general use due to long queue times. Suggested alternative is TinyGPU for MD simulations using Amber, as it benefits from GPUs.

### Root Cause:
- Meggie cluster is not open for general use due to long queue times.

### Solution:
- Consider investing in TinyGPU for MD simulations using Amber, as it provides priority access to user-financed groups.

### General Learnings:
- Meggie cluster is restricted due to high demand and long queue times.
- TinyGPU is recommended for specific workloads like MD simulations using Amber.
- User-financed nodes in TinyGPU offer priority access.

### Recommendations:
- For users needing additional HPC resources, evaluate the suitability of TinyGPU, especially for GPU-intensive workloads.
- Monitor the usage and queue times of different clusters to manage resource allocation effectively.
```
---

### 2025030642000644_Low%20GPU%20utilisation%20%28%3C15%25%29%20-%20v119ee10.md
# Ticket 2025030642000644

 # Low GPU Utilisation Issue

## Keywords
- Low GPU utilisation
- ClusterCockpit
- srun
- nvidia-smi
- Job monitoring
- Efficient cluster usage

## Summary
The HPC Admin noticed that several jobs had very low GPU utilisation (<20%). The user was informed about this issue and provided with methods to monitor and diagnose the problem.

## Root Cause
- A bug caused some processes to hang, preventing GPU usage.
- The current implementation of the user's jobs involves tensor operations that are not easily batched due to dynamically changing sizes, leading to inefficient GPU usage.

## Diagnostic Steps
- The HPC Admin recommended using ClusterCockpit for job monitoring.
- Alternatively, the user can attach to a running job using `srun --pty --overlap --jobid YOUR-JOBID bash` and run `nvidia-smi` to check GPU utilisation.

## Solution
- The user fixed the bug causing processes to hang.
- The user acknowledged the need to optimise their jobs for better GPU utilisation. They plan to improve the implementation to use the GPU more efficiently.

## General Learnings
- Regularly monitor jobs using tools like ClusterCockpit to ensure efficient resource usage.
- Attach to running jobs using `srun` and `nvidia-smi` to diagnose GPU utilisation issues.
- Aim for GPU utilisation of 80-100% for efficient cluster usage.
- Address any bugs or inefficiencies in job implementation to improve resource usage.
---

### 2021101142003107_inefficient%20jobs%20on%20TinyGPU%20-%20iwsp025h.md
# Ticket 2021101142003107

 # Inefficient GPU Resource Allocation on TinyGPU

## Keywords
- TinyGPU
- GPU allocation
- Resource inefficiency
- ppn parameter
- Job configuration

## Problem Description
- User's jobs on TinyGPU were requesting two GPUs but only utilizing one.
- This led to inefficient resource allocation and potential wastage of GPU resources.

## Root Cause
- Misconfiguration in job submission script where the user requested more GPUs than were actually being used by the application.

## Solution
- Adjust the job submission script to either:
  - Fix the application to utilize both GPUs.
  - Request only one GPU by setting `ppn=4` instead of `ppn=8`.

## Lessons Learned
- Ensure that the number of GPUs requested in the job submission script matches the actual usage by the application.
- Proper configuration of resource parameters (e.g., `ppn`) is crucial for efficient resource utilization.
- Regular monitoring and user communication can help identify and rectify such inefficiencies.

## Actions Taken
- HPC Admin notified the user about the inefficiency.
- User acknowledged the mistake and agreed to fix the job configuration.

## Recommendations
- Educate users on proper resource allocation and efficient job configuration.
- Implement monitoring tools to detect and alert on resource inefficiencies.
- Provide clear documentation and examples for job submission scripts to help users avoid common mistakes.
---

### 2024071542002156_Job%20on%20TinyGPU%20only%20uses%20one%20of%20four%20allocated%20GPUs%20%5Biwb3103h%5D.md
# Ticket 2024071542002156

 # HPC Support Ticket: Job on TinyGPU Only Uses One of Four Allocated GPUs

## Keywords
- GPU utilization
- TinyGPU
- JobID
- ClusterCockpit
- `nvidia-smi`
- Resource allocation

## Problem Description
- User's job on TinyGPU (JobID 858311) is only utilizing one of the four allocated GPUs.

## Root Cause
- The job is not configured to utilize all allocated GPUs, leading to inefficient resource usage.

## Solution
- **Monitoring**:
  - Use ClusterCockpit at [monitoring.nhr.fau.de](https://monitoring.nhr.fau.de/) to view GPU utilization.
  - Attach to the running job using `srun --pty --overlap --jobid YOUR-JOBID bash` and run `nvidia-smi` to check GPU utilization.

- **Resource Allocation**:
  - Ensure that the job script is configured to utilize all allocated GPUs.
  - Only allocate GPU nodes if the code can make use of the GPUs to avoid idle resources.

## General Learnings
- Always verify that jobs are utilizing all allocated resources efficiently.
- Use monitoring tools to diagnose and optimize resource usage.
- Properly configure job scripts to make full use of allocated GPUs.

## Contact Information
- For further assistance, contact HPC support at [support-hpc@fau.de](mailto:support-hpc@fau.de).
- Visit the HPC website at [hpc.fau.de](https://hpc.fau.de/).
---

### 42050146_tinygpu%20_%20node%3Atg001%20_%20GPU%20problem.md
# Ticket 42050146

 ```markdown
# HPC Support Ticket: GPU Problem on Node tg001

## Subject
tinygpu / node:tg001 / GPU problem

## Keywords
- GPU
- Node tg001
- Wrong results
- Overheating
- ECC protection
- NVidia kernel modules

## Problem Description
The GPU on node tg001 is producing incorrect results intermittently. The user identified the issue through tests with a simple Laplace 3D solver, which builds a mesh, constructs a stiffness matrix, and solves a linear system using CG/GMRES on the GPU. The results on node tg001 differ from those on other nodes (tg002 to tg008), which produce correct results. The incorrect results include dot products becoming zero or NaN. The CPU results on tg001 are correct, suggesting a GPU-specific issue.

## Root Cause
- Possible hardware problem, such as overheating.
- Lack of ECC protection on the GPU memory system.

## Tests and Diagnostics
- The user ran multiple tests, including solving Ax=b with CG and GMRES, and observed inconsistent results on node tg001.
- HPC Admins conducted extensive tests on tg001 but found no abnormalities.

## Solution
- The node was upgraded to a new version of the NVidia kernel modules (256.35 instead of 195.36.24).
- The node was returned to regular operation after no issues were found during testing.

## Conclusion
The issue was likely related to the older version of the NVidia kernel modules. Upgrading the modules resolved the problem, and the node is now functioning correctly.
```
---

### 2025022042003518_Ineffiziente%20Nutzung%20von%20TinyGPU%20durch%20iwfa109h%20%28Anuj%20Nair%29.md
# Ticket 2025022042003518

 # HPC Support Ticket: Inefficient Use of TinyGPU

## Keywords
- GPU-hours
- GPU utilization
- Job efficiency
- Student usage
- Resource management

## Summary
A student has been inefficiently using TinyGPU resources, resulting in over 13,000 GPU-hours with 0% GPU utilization. Previous attempts to address the issue with the student have not led to sustainable improvements.

## Root Cause
- **Inefficient Job Submission**: The student's jobs show 0% GPU utilization over their entire runtime.
- **Lack of Optimization**: The jobs are not optimized to effectively use the GPU resources.

## Solution
- **Improve Job Efficiency**: The student's supervisor (2nd Level Support team member) needs to ensure that the jobs are optimized to make better use of GPU resources.
- **Monitoring and Follow-up**: Continuous monitoring and follow-up with the student to ensure that the issue is resolved and does not recur.

## General Learnings
- **Resource Management**: It is crucial to monitor and manage resource usage to prevent inefficient utilization.
- **User Education**: Providing training and support to users on how to optimize their jobs can help in better resource utilization.
- **Communication**: Effective communication with users and their supervisors is essential to address and resolve issues related to resource usage.

## Next Steps
- **Contact Supervisor**: The HPC Admin should contact the student's supervisor to address the issue.
- **Provide Guidance**: Offer guidance and resources to help the student optimize their jobs.
- **Monitor Usage**: Continue to monitor the student's GPU usage to ensure improvements are made.

## References
- [FAU HPC Support](mailto:support-hpc@fau.de)
- [FAU HPC Website](https://hpc.fau.de/)
---

### 2024070742000879_Eternally%20self-submitting%20jobs%20on%20Alex%20%5Bbcpc101h%5D.md
# Ticket 2024070742000879

 # HPC Support Ticket: Eternally Self-Submitting Jobs

## Keywords
- Self-submitting jobs
- SLURM scripts
- Resource limits
- GPU usage
- pmemd vs. pmemd.cuda
- ClusterCockpit

## Problem Description
- User's jobs on the HPC cluster kept re-submitting themselves without producing results.
- This issue caused over 20,000 emails in the mail queue.
- The root cause was a missing verification in the SLURM scripts to prevent continuous job submission after an error.

## Solution
- HPC Admins limited the user's resource usage to one GPU.
- HPC Admins provided a code snippet to add to SLURM scripts to prevent continuous job submission:
  ```bash
  if [ "$SECONDS" -gt "3600" ]; then
  cd ${SLURM_SUBMIT_DIR}
  sbatch job_script
  fi
  ```
- User was advised to use `pmemd` on a CPU cluster for energy minimization/heating/equilibrating steps instead of `pmemd.cuda` on a GPU cluster.

## Lessons Learned
- Always include a verification in SLURM scripts to prevent continuous job submission after an error.
- Use appropriate tools for specific tasks: `pmemd` for minimization and equilibration on CPU clusters, `pmemd.cuda` for production runs on GPU clusters.
- Regularly check running jobs and scripts to ensure they are functioning as intended.
- Communicate with supervisors for task-specific recommendations.

## Actions Taken
- HPC Admins limited the user's resource usage.
- HPC Admins cancelled non-GPU jobs and advised the user on proper tool usage.
- User added the provided code snippet to all SLURM scripts and confirmed the changes.

## Follow-up
- User requested resource limit restoration after fixing the issue.
- HPC Admins verified the changes and provided further guidance on tool usage.
---

### 2018091842000866_qsub.tinygpu%20schl%C3%83%C2%A4gt%20fehl.md
# Ticket 2018091842000866

 # HPC Support Ticket Analysis: qsub.tinygpu Error

## Keywords
- qsub.tinygpu
- Job submission error
- GPU cluster
- CUDA error
- Node issue

## Summary
A user encountered issues submitting jobs to the tinygpu cluster using `qsub.tinygpu`. The error message indicated that the job was rejected by all possible destinations. Further investigation revealed that a specific GPU on a node (GPU3 on tg40) was causing CUDA errors.

## Root Cause
- Initial job submission error due to unknown reasons.
- Specific GPU (GPU3 on node tg40) causing CUDA errors, leading to job failures.

## Solution
- The initial issue with job submission was not resolved within the ticket.
- The problematic GPU was identified, and a new ticket was created to address the hardware issue.

## Lessons Learned
- Job submission errors can be caused by various factors, including syntax errors, resource requests, and hardware issues.
- It is important to check the specific resources assigned to jobs when troubleshooting submission errors.
- Hardware issues, such as problematic GPUs, can cause job failures and should be investigated separately.

## Next Steps
- Continue monitoring job submission errors and investigate the root cause of the initial `qsub.tinygpu` error.
- Address the hardware issue with the problematic GPU on node tg40 in a separate ticket.

## Related Tickets
- A new ticket was created to address the hardware issue with GPU3 on node tg40.
---

### 42070271_Tinyblue.md
# Ticket 42070271

 ```markdown
# HPC-Support Ticket: Tinyblue Availability

## Keywords
- Tinyblue
- Availability
- Reproducibility
- Benutzerlast

## Summary
A user inquired about the availability of the Tinyblue system. The HPC Admin responded that Tinyblue has been provisionally re-enabled because the issues that led to its unavailability could not be reproduced without real user load.

## Root Cause
- Unspecified issues with Tinyblue that required it to be taken offline.

## Solution
- Tinyblue was re-enabled provisionally to see if the issues could be reproduced under real user load.

## Lessons Learned
- Some issues may not be reproducible without real user load.
- Provisional re-enablement can be a strategy to diagnose and troubleshoot such issues.
```
---

### 2022092942004002_Einschr%C3%83%C2%A4nkungen%20des%20Accounts.md
# Ticket 2022092942004002

 # HPC-Support Ticket: Einschränkungen des Accounts

## Keywords
- Account Restrictions
- tinyGPU
- Residual Neural Networks
- Rechenzeit
- Email Adresse

## Summary
- **User Issue**: User noticed an exponential increase in computation time for training residual neural networks on tinyGPU, which was not the case in previous experiments.
- **Root Cause**: User suspected potential account restrictions.
- **Solution**: HPC Admin confirmed no account restrictions were in place.

## Details
- **User Inquiry**: The user reported an unexpected increase in computation time for their experiments on tinyGPU and inquired about any account restrictions.
- **HPC Admin Response**: The HPC Admin confirmed that there were no restrictions on the user's account. Additionally, the admin requested the user to use their @fau.de email address for future support inquiries.

## Lessons Learned
- Always verify account restrictions when users report unexpected performance issues.
- Ensure users are using their official email addresses for support communications.

## Action Items
- None specified in the ticket.

## Follow-Up
- No further action required from the user or HPC Admin.

## Additional Notes
- The user was advised to use their official @fau.de email address for future communications with HPC support.

---

This documentation can be used to address similar issues in the future by verifying account restrictions and ensuring proper communication channels.
---

### 2023110742002432_info%20HPC%20cluster.md
# Ticket 2023110742002432

 # HPC Support Ticket Conversation Summary

## Keywords
- HPC cluster
- Deep learning
- Histopathological images
- Fees and usage
- Zoom meeting
- GPUs
- Sensitive data

## General Learnings
- Basic usage of HPC clusters at NHR@FAU is free of charge.
- Deep learning applications typically require GPUs, available in clusters TinyGPU and Alex.
- Monthly introductions for beginner HPC users are offered.
- Storage or processing of patient or sensitive data is not allowed on HPC systems.
- Users can find initial information and steps to get started on the HPC website.

## Root Cause of User Inquiry
- User's research group needs HPC resources for deep learning applications on histopathological images.
- User seeks information on fees, usage, and scheduling a Zoom meeting for further details.

## Solution Provided
- HPC Admin informed the user about free basic usage and the availability of GPUs.
- Provided links to documentation and upcoming introductory sessions.
- Noted the restriction on processing sensitive data.
- Offered further assistance if needed.

## Next Steps for Support
- Ensure the user has access to the necessary documentation and introductory sessions.
- Be prepared to answer additional questions or schedule a Zoom meeting if requested.
---

### 2021120142001428_Jobs%20auf%20tinyGPU%20nutzen%20keine%20GPU%20-%20bccc05.md
# Ticket 2021120142001428

 ```markdown
# HPC-Support Ticket: Jobs auf tinyGPU nutzen keine GPU - bccc05

## Keywords
- GPU utilization
- System monitoring
- gmetad
- TinyGPU
- Job monitoring

## Summary
- **Issue**: User's jobs on TinyGPU were reported to not utilize GPUs.
- **Root Cause**: Incorrect system monitoring data due to gmetad failure on wadm1.
- **Solution**: Restarted gmetad to correct system monitoring.

## Details
1. **Initial Report**:
   - HPC Admin reported that user's jobs on TinyGPU were not using GPUs.

2. **Correction**:
   - HPC Admin corrected the initial report, stating that the system monitoring was not capturing GPU metrics correctly.

3. **Root Cause Identification**:
   - The issue was traced to gmetad on wadm1, which had stopped functioning.

4. **Resolution**:
   - After restarting gmetad, the system monitoring started capturing GPU metrics correctly, confirming that the user's jobs were utilizing GPUs as expected.

## Lessons Learned
- Ensure system monitoring tools are functioning correctly to avoid false alarms.
- Regularly check the status of monitoring services like gmetad.
- Communicate updates promptly to users to maintain transparency.
```
---

### 2020112342002792_Jobs%20auf%20TinyGPU%20nutzen%20nur%201%20GPU%20-%20iwal019h.md
# Ticket 2020112342002792

 ```markdown
# HPC Support Ticket: Jobs auf TinyGPU nutzen nur 1 GPU

## Keywords
- GPU utilization
- ppn=8
- nvidia-smi
- TinyGPU
- Monitoring

## Problem Description
- User requests two GPUs using `ppn=8`.
- Jobs only utilize one GPU.
- Second GPU shows no active processes.

## Root Cause
- Incorrect configuration or resource allocation in job script.

## Diagnostic Steps
- Checked GPU utilization using `nvidia-smi`.
- Verified that only one GPU is being used despite requesting two.

## Solution
- Ensure job script correctly allocates and utilizes both GPUs.
- Verify resource allocation parameters in the job script.

## General Learning
- Always verify resource allocation in job scripts.
- Use monitoring tools like `nvidia-smi` to diagnose GPU utilization issues.
```
---

### 2024110442003364_Job%20on%20TinyGPU%20uses%20only%201%20of%202%20GPUs%20%5Biwfa035h%5D.md
# Ticket 2024110442003364

 # HPC Support Ticket: Job on TinyGPU Uses Only 1 of 2 GPUs

## Keywords
- GPU utilization
- TinyGPU
- JobID
- ClusterCockpit
- `nvidia-smi`
- Resource allocation

## Problem Description
- User's job on TinyGPU (JobID 925367) is only utilizing one of the two allocated GPUs.

## Root Cause
- The job code may not be optimized to utilize multiple GPUs effectively.

## Diagnostic Steps
1. **Monitoring System**:
   - Log into ClusterCockpit at [monitoring.nhr.fau.de](https://monitoring.nhr.fau.de/) to view GPU utilization.
2. **Attach to Running Job**:
   - Use `srun --pty --overlap --jobid YOUR-JOBID bash` to get a shell on the first node of the job.
   - Run `nvidia-smi` to check current GPU utilization.

## Solution
- Ensure that the job code is capable of utilizing multiple GPUs.
- Allocate nodes with GPUs only if the code can effectively use them to avoid resource wastage.

## Additional Notes
- If further assistance is needed, contact the HPC support team.
- Ensure efficient resource allocation to maximize system utilization.

## Contact Information
- **HPC Support**: [support-hpc@fau.de](mailto:support-hpc@fau.de)
- **Website**: [hpc.fau.de](https://hpc.fau.de/)

## Closure
- The ticket was closed by the HPC Admin.
---

### 2022012542001296_Early-Alex%20%22Kai%20Packh%C3%83%C2%A4user%22%20_%20iwi5056h.md
# Ticket 2022012542001296

 ```markdown
# HPC Support Ticket Conversation Analysis

## Subject: Early-Alex "Kai Packhäuser" / iwi5056h

### Keywords:
- Early-User Account
- Alex Cluster
- Partition Specification
- PyTorch Module
- GPU Resources
- Deep Learning
- Anonymization Methods
- Chest X-rays

### Summary:
- **User Request**: Access to the Alex cluster for deep learning experiments using PyTorch.
- **Resources Requested**: 1 GPU per job, expected compute time of 200-500 GPU hours.
- **Software Needed**: PyTorch.
- **Application**: Developing anonymization methods for chest X-rays.

### Issues and Solutions:
- **Issue**: User account needed to be activated for early access.
  - **Solution**: HPC Admin activated the user's account on the Alex cluster.
- **Issue**: User needed guidance on using the cluster.
  - **Solution**: HPC Admin provided documentation link and instructions on specifying partitions (`--partition=a40` or `--partition=a100`).
- **Issue**: User needed information on available PyTorch modules.
  - **Solution**: HPC Admin informed about the available module `python/pytorch-1.10py3.9` and suggested using `module help python/pytorch-1.10py3.9` for more details.

### General Learnings:
- **Account Activation**: Ensure early-user accounts are activated promptly.
- **Partition Specification**: Always specify the partition when submitting jobs.
- **Module Information**: Use `module help` to get detailed information about available modules.
- **Documentation**: Refer users to the relevant documentation for cluster usage.

### Root Cause of the Problem:
- User needed account activation and guidance on using the Alex cluster and available software modules.

### Solution:
- HPC Admin activated the user's account and provided necessary documentation and instructions.
```
---

### 2024032242000795_Tier3-Access-Alex%20%22Vijaya%20Kumar%20Thota%22%20_%20gwgi100h.md
# Ticket 2024032242000795

 ```markdown
# HPC Support Ticket Analysis

## Subject: Tier3-Access-Alex / gwgi100h

### Keywords:
- Access Request
- GPGPU Cluster 'Alex'
- Nvidia A100 GPGPUs
- Python, Conda, TensorFlow, PyTorch
- Machine Learning, Computer Vision
- GPU-hours

### Summary:
A user requested access to the GPGPU cluster 'Alex' for machine learning and computer vision applications. The request included specific software requirements and an estimate of GPU-hours needed.

### Root Cause:
The user was not authorized to use the 'Alex' cluster.

### Solution:
The HPC Admin informed the user that they are not allowed to use 'Alex'.

### Lessons Learned:
- Ensure users are aware of their access permissions to specific clusters.
- Clearly communicate access restrictions and requirements for using specialized resources.
- Document and verify user requests for computational resources to avoid unauthorized access.
```
---

### 2024070342003365_Tier3-Access-Alex%20%22Swarnendu%20Sengupta%22%20_%20iwal171h.md
# Ticket 2024070342003365

 ```markdown
# HPC Support Ticket Conversation Analysis

## Keywords
- Tier3 Access
- Alex Cluster
- TinyGPU Cluster
- GPGPU
- Nvidia A100
- Python/PyTorch/CUDA
- Transformer Model
- Packet Loss Concealment
- Neural Speech Codecs
- DiplomHiwi
- FAU-Audiolabs
- Project Partner
- Tier3-Grundversorgung
- iwal_fhg

## Summary
- **User Request**: Access to GPGPU cluster 'Alex' for training a deep learning model using Python/PyTorch/CUDA.
- **User Role**: DiplomHiwi at FAU-Audiolabs.
- **Project Details**: Using a transformer model for Packet Loss Concealment in neural speech codecs.
- **Additional Request**: Access to TinyGPU cluster for smaller training tasks.

## Root Cause of the Problem
- User did not have the required permissions to access the Alex cluster for training their deep learning model.

## Solution
- **HPC Admin**: Enabled the user's account on the Alex cluster.
- **Additional Information**: The user's account was already enabled on TinyGPU. The user's role was clarified as a project partner under Tier3-Grundversorgung FAU-AudioLabs, and the usage on Alex was noted to be billed under iwal_fhg.

## General Learnings
- Ensure users have the correct permissions for the clusters they need to access.
- Clarify the user's role and billing details to avoid confusion.
- Provide access to additional clusters if requested and appropriate.
```
---

### 2024112142002903_Job%20on%20TinyGPU%20not%20using%20the%20GPU%20%5Bempk004h%5D.md
# Ticket 2024112142002903

 # HPC Support Ticket: Job on TinyGPU Not Using the GPU

## Keywords
- GPU utilization
- Job allocation
- Monitoring system
- ClusterCockpit
- `nvidia-smi`
- Resource management

## Summary
A user's job on TinyGPU was not utilizing the GPU, leading to idle resources.

## Root Cause
The user's job (JobID 940977) was allocated GPU resources but did not make use of them.

## Solution
1. **Monitoring GPU Utilization**:
   - Use ClusterCockpit at [monitoring.nhr.fau.de](https://monitoring.nhr.fau.de/) to view GPU utilization.
   - Alternatively, attach to the running job using `srun --pty --overlap --jobid YOUR-JOBID bash` and run `nvidia-smi` to check GPU utilization.

2. **Resource Allocation**:
   - Ensure that jobs only allocate nodes with GPUs if the code can actually utilize the GPU.
   - Avoid idle GPU resources by properly configuring job scripts.

## General Learnings
- Regularly monitor job performance to ensure efficient resource utilization.
- Use monitoring tools provided by the HPC center to diagnose and resolve issues.
- Properly allocate resources based on job requirements to avoid wastage.

## Contact Information
For further assistance, contact the HPC support team at [support-hpc@fau.de](mailto:support-hpc@fau.de).
---

### 2022120842001011_Tier3-Access-Alex%20%22Mohamed%20Elminshawi%22%20_%20iwal020h.md
# Ticket 2022120842001011

 # HPC Support Ticket Analysis

## Keywords
- Access Request
- Account Enabled
- Alex Cluster
- A100 Node
- GPGPU
- CUDA
- Neural Networks
- Certificate Expired

## Summary
- **User Request**: Access to 'Alex' cluster for training/evaluation of neural networks using Nvidia A100 GPGPUs.
- **Required Software**: CUDA
- **Compute Time**: 1 GPU * 24-72 hours * 100 jobs per month
- **Issue**: Certificate expiration mentioned by HPC Admin.
- **Resolution**: Account enabled on Alex cluster.

## Lessons Learned
- Ensure certificates are up-to-date to avoid access issues.
- Proper communication of new hardware installations (e.g., A100 node) to users.
- Efficient handling of access requests for specific hardware and software needs.

## Root Cause
- Expired certificate causing potential access issues.

## Solution
- Account re-enabled after addressing the certificate issue.

## Follow-up Actions
- Monitor certificate expiration dates.
- Regularly update users on new hardware and software installations.
- Streamline access request processes for specialized hardware.

---

This documentation can be used to resolve similar issues related to access requests and certificate expirations in the future.
---

### 42113534_busy%20node.md
# Ticket 42113534

 # HPC Support Ticket: Busy Node

## Keywords
- Node occupation
- Benchmarking
- Node release
- High Performance Computing (HPC)
- Seminar

## Problem
- **User Issue**: The user was unable to access the node `tinygpu -q fermi` due to it being occupied.
- **Root Cause**: The node was in use by another user.

## Solution
- **Admin Action**: The HPC Admin checked the status of the node and found that it had been freed.
- **Resolution**: The user was able to access the node after it was released.

## Lessons Learned
- **Node Management**: Regularly check node status to ensure availability for users.
- **Communication**: Inform users about node availability and potential delays.
- **Support Process**: Quickly address node occupation issues to facilitate user tasks.

## Recommendations
- **Monitoring**: Implement a system to monitor node usage and notify users of availability.
- **Priority Access**: Consider implementing a priority system for nodes required for critical tasks such as benchmarking.

---

This documentation can be used to address similar issues related to node occupation and user access in the future.
---

### 2024022342003121_Jobs%20auf%20Alex%20nutzen%20die%20GPU%20nicht%20%5Bb196ac10%5D.md
# Ticket 2024022342003121

 # HPC Support Ticket: Jobs auf Alex nutzen die GPU nicht

## Keywords
- GPU utilization
- Conda environments
- Large datasets
- NFS performance
- CEPH storage

## Problem
- Jobs submitted by the user showed no GPU activity for several hours.
- The user was preparing a large dataset (20,000 hours of audio) using Apache Arrow to generate an on-disk cache, which took longer than expected over NFS.

## Root Cause
- The delay was due to the time-consuming preparation of the on-disk cache for a large dataset over NFS.
- Conda environments built on frontends without GPUs can cause issues when used on compute nodes with GPUs.

## Solution
- The user aborted the affected jobs and planned to find an alternative approach that does not block GPUs for extended periods.
- HPC Admins suggested using CEPH storage if the access to $WORK is a bottleneck.

## General Learnings
- Ensure that conda environments are built in an interactive job on a compute node with GPUs to avoid compatibility issues.
- Be mindful of the time required for data preparation tasks, especially with large datasets over NFS.
- Consider using alternative storage solutions like CEPH for improved performance.

## Related Links
- [CEPH Storage Documentation](https://doc.nhr.fau.de/data/workspaces/)
---

### 2025022542002546_Idle%20jobs%20on%20TinyGPU.md
# Ticket 2025022542002546

 ```markdown
# Idle Jobs on TinyGPU

## Keywords
- Idle jobs
- TinyGPU
- File system misuse
- Job submission
- Shell loading
- Input files

## Problem Description
- Jobs submitted to TinyGPU (a100) are displayed as running but do not produce any output.
- Even jobs set to crash within the first minute are stuck.
- User suspects an issue with the system or their quota.

## Root Cause
- File systems are being misused, causing jobs to get stuck while loading the shell and reading input files.

## Solution
- Cancel the stuck jobs.
- Log out and back in.
- Resubmit the jobs.

## Lessons Learned
- Misuse of file systems can cause jobs to appear idle.
- Logging out and back in can resolve issues related to shell loading and input file reading.
- Regularly check for file system misuse to prevent job submission issues.
```
---

### 2022110942002583_Tier3-Access-Alex%20%22Andreas%20Brendel%22%20_%20iwal102h.md
# Ticket 2022110942002583

 # HPC Support Ticket Summary

## Keywords
- Account Activation
- Alex Cluster
- GPGPU Access
- Nvidia A100
- Python
- Pytorch
- Deep Learning
- Speech Synthesis
- Audio Coding

## Summary
- **User Request**: Access to Alex cluster for GPGPU resources, specifically Nvidia A100 GPUs.
- **Required Software**: Python, Pytorch.
- **Application**: Deep generative neural networks for speech synthesis and audio coding.
- **Expected Outcome**: Optimized neural speech codec with excellent perceptual quality at low bitrates and low computational complexity.
- **Additional Notes**: User works for Fraunhofer IIS and has a new A100 node installed in the Alex cluster.

## HPC Admin Response
- **Action Taken**: Account activated on Alex cluster.
- **Additional Information**: Provided link to Alex cluster documentation.

## Root Cause of the Problem
- User needed access to the Alex cluster to utilize the newly installed A100 node for their research.

## Solution
- HPC Admin activated the user's account on the Alex cluster and provided relevant documentation.

## General Learnings
- Ensure users have the necessary access to HPC resources when new hardware is installed.
- Provide documentation links to help users get started with the cluster.
- Understand the specific software and computational needs of users for better support.
---

### 2023061242003164_Gastwissenschaftler%20Matt%20Baugh.md
# Ticket 2023061242003164

 ```markdown
# HPC-Support Ticket Analysis

## Subject: Gastwissenschaftler Account Request

### Keywords:
- Gastwissenschaftler
- IDM Account
- HPC Account
- Tier3
- GPU Hours
- Machine Learning (ML)

### Summary:
A professor requested an IDM and HPC account for a guest researcher. The request was closed by the HPC Admin with a note indicating that the requested GPU hours exceed the Tier3 limit.

### Root Cause:
- The user requested 35k GPU hours, which exceeds the Tier3 threshold.

### Solution:
- Inform the user that the requested GPU hours are beyond the Tier3 limit and provide guidance on the appropriate tier for such requests.

### General Learnings:
- Ensure users are aware of the GPU hour limits for different tiers.
- Provide clear guidelines on the process for requesting resources beyond standard limits.
- Educate users on the appropriate channels for requesting high-resource allocations.
```
---

### 2024072342002257_Tier3-Access-Alex%20%22Thomas%20Gorges%22%20_%20iwi5193h.md
# Ticket 2024072342002257

 # HPC Support Ticket Analysis

## Keywords
- HPC Account Activation
- GPU Hours Allocation
- Tier3 Service
- Software Requirements (Python, RDKit, TensorFlow)
- Research Application (AI in Chemistry, Data Scarcity Mitigation, Computer Vision)

## Summary
- **User Request**: Activation of HPC account on Alex for research purposes.
- **Resource Request**: 40,000 GPU hours per year.
- **Software Needs**: Python, RDKit, TensorFlow.
- **Research Field**: AI in chemistry, data scarcity mitigation, computer vision.

## Root Cause
- User requested an unrealistic amount of GPU hours (40,000 GPU hours per year) for the basic Tier3 service.

## Solution
- **HPC Admin Action**: Enabled the user's HPC account on Alex.
- **Feedback**: Informed the user that the requested GPU hours are not realistic for the basic Tier3 service.

## General Learnings
- **Resource Allocation**: Understand the limitations of the basic Tier3 service in terms of GPU hours.
- **User Expectations**: Manage user expectations regarding available resources and provide guidance on realistic usage.
- **Communication**: Clearly communicate the activation of the account and any limitations or adjustments to the user's request.

## Next Steps
- **User**: Review the allocated resources and adjust research plans accordingly.
- **HPC Admin**: Monitor the user's resource usage and provide further assistance if needed.

---

This documentation can be used to handle similar requests and manage user expectations regarding resource allocation in the future.
---

### 2023033142003081_Jobs%20on%20Alex%20only%20use%201%20of%208%20allocated%20GPUs%20%5Bb143dc11%5D.md
# Ticket 2023033142003081

 # HPC Support Ticket: Jobs on Alex only use 1 of 8 allocated GPUs

## Keywords
- GPU utilization
- Job monitoring
- Resource allocation
- `srun` command
- `nvidia-smi`
- ClusterCockpit

## Problem Description
- User's jobs on Alex were only utilizing 1 out of 8 allocated GPUs.
- The user did not activate the use of all 8 GPUs in their program.

## Root Cause
- The user's code was capable of using 8 GPUs but was not configured to do so.

## Solution
- The user was advised to activate the use of all 8 GPUs in their program.
- The user was instructed to use `srun --pty --jobid YOUR-JOBID bash` to attach to the running job and `nvidia-smi` to check GPU utilization.
- The user was informed about the ClusterCockpit on portal.hpc.fau.de to monitor GPU usage.

## Additional Information
- The user was reminded to only request GPU nodes if their code can utilize them to avoid wasting resources.
- The user was provided with instructions on how to enable GPU metrics in ClusterCockpit.

## Follow-up
- The user's subsequent jobs still utilized only 1 out of 4 allocated GPUs.
- The user was reminded again to ensure proper GPU utilization to prevent unnecessary consumption of the project budget.

## Conclusion
- Users should ensure their jobs are properly configured to utilize all allocated GPUs.
- Monitoring tools like `nvidia-smi` and ClusterCockpit should be used to track GPU usage.
- Proper resource allocation is crucial to avoid wasting computing resources and project budget.
---

### 2024022342001141_Issue%20of%20invisible%20job%20status%20and%20slow%20jobs.md
# Ticket 2024022342001141

 ```markdown
# Issue of Invisible Job Status and Slow Jobs

## Keywords
- Job Status
- SLURM
- squeue
- Hidden Partition
- Network File System (NFS)
- Local SSD
- GPU Performance

## Problem Description
- **Slow Training Jobs on V100**: Training jobs on V100 GPUs were significantly slower compared to RTX 2080 Ti and local GPUs.
- **Invisible Job Status**: Jobs submitted to the RTX 2080 Ti partition did not appear in the `squeue` list.

## Root Cause
- **Slow Training Jobs**: The training data resided on a network file system (NFS), which was heavily loaded, causing slow access times.
- **Invisible Job Status**: The RTX 2080 Ti partition was a hidden partition, not shown by default in `squeue -l`.

## Solution
- **Slow Training Jobs**:
  - Recommended to copy input data to the local SSD at the beginning of the job.
  - Pack inputs into an archive, copy and unpack it to the local SSD.
  - Perform a cleanup step at the end of the job to avoid slowdowns due to NFS access.
- **Invisible Job Status**:
  - Use `squeue -a` to see all jobs, including those in hidden partitions.

## General Learnings
- **File System Impact**: Heavy load on NFS can significantly impact job performance.
- **Local Storage Usage**: Utilizing local SSDs can improve job performance by reducing dependency on network file systems.
- **Hidden Partitions**: Some partitions may be hidden and require specific commands to view job status.

## References
- **HPC Admins**: Provided detailed guidance on optimizing job performance and viewing hidden partitions.
- **User**: Reported the issue with detailed job IDs and error file locations.
```
---

### 2024121942002317_Job%20on%20Alex%20only%20uses%202%20of%208%20allocated%20GPUs%20%5Bb211dd11%5D.md
# Ticket 2024121942002317

 # HPC Support Ticket: Job on Alex Only Uses 2 of 8 Allocated GPUs

## Keywords
- GPU utilization
- Job allocation
- Monitoring system
- ClusterCockpit
- `nvidia-smi`
- Resource management

## Summary
A job was allocated 8 GPUs but only utilized 2, leading to inefficient resource usage.

## Root Cause
The user's job was not configured to utilize all allocated GPUs effectively.

## Solution
1. **Monitoring GPU Utilization:**
   - Use ClusterCockpit: [https://monitoring.nhr.fau.de/](https://monitoring.nhr.fau.de/)
   - Attach to the running job using:
     ```bash
     srun --pty --overlap --jobid YOUR-JOBID bash
     ```
   - Check GPU utilization with:
     ```bash
     nvidia-smi
     ```

2. **Resource Allocation:**
   - Ensure that the job code is capable of utilizing all allocated GPUs.
   - Only allocate nodes with GPUs if the job can effectively use them.

## General Learning
- Always verify that jobs are utilizing allocated resources efficiently.
- Use monitoring tools to track resource usage.
- Properly configure jobs to make full use of allocated GPUs.

## Contact
For further assistance, contact the HPC support team at [support-hpc@fau.de](mailto:support-hpc@fau.de).
---

### 2022072142001229_Job%20on%20TinyGPU%20does%20not%20use%20GPU%20%5Biwal098h%5D.md
# Ticket 2022072142001229

 # HPC Support Ticket: Job on TinyGPU Does Not Use GPU

## Keywords
- GPU utilization
- TinyGPU
- JobID 486653
- `nvidia-smi`
- Resource allocation
- Monitoring system

## Problem Description
- User's job on TinyGPU (JobID 486653) is not utilizing the GPU.
- Monitoring system shows no GPU usage for the job.

## Root Cause
- The user's code does not make use of the GPU, leading to idle GPU resources.

## Solution
- **User Action:**
  - SSH to the node running the job.
  - Use `nvidia-smi` to check GPU utilization.
  - Ensure code is capable of utilizing GPU resources before allocating GPU nodes.
- **Admin Action:**
  - Monitor GPU usage through the monitoring system.
  - Notify users if their jobs are not utilizing allocated GPU resources.

## Resources
- [Working with NVIDIA GPUs](https://hpc.fau.de/systems-services/systems-documentation-instructions/special-applications-and-tips-tricks/working-with-nvidia-gpus/)

## General Learning
- Always verify that your code can utilize GPU resources before requesting GPU nodes.
- Use `nvidia-smi` to monitor GPU usage during job execution.
- Idle GPU resources due to non-GPU utilizing jobs can prevent other users from accessing these resources.

## Contact
- For further assistance, contact the HPC support team at [support-hpc@fau.de](mailto:support-hpc@fau.de).
---

### 2021040642005154_Jobs%20on%20TinyGPU%20do%20not%20utilize%20GPUs%20at%20all%20-%20iwso028h.md
# Ticket 2021040642005154

 # HPC Support Ticket: Jobs on TinyGPU Do Not Utilize GPUs

## Subject
Jobs on TinyGPU do not utilize GPUs at all - iwso028h

## Keywords
- GPU utilization
- nvidia-smi
- Python processes
- TinyGPU
- Tesla V100-PCIE

## Problem Description
The user's jobs on TinyGPU are not utilizing the GPUs. The `nvidia-smi` output shows that the GPUs are idle, with no processes running on them.

## Root Cause
The Python processes in the user's jobs are not starting any processes on the GPUs.

## Diagnostic Steps
1. Check GPU utilization using `nvidia-smi`.
2. Verify that no processes are running on the GPUs.

## Solution
Ensure that the user's jobs are correctly configured to utilize the GPUs. This may involve checking the job script and the code to ensure that GPU resources are properly requested and used.

## Lessons Learned
- Always verify GPU utilization using `nvidia-smi` when troubleshooting GPU-related issues.
- Ensure that job scripts and code are correctly configured to request and utilize GPU resources.

## References
- `nvidia-smi` command for monitoring GPU usage.
- Proper configuration of job scripts for GPU utilization.
---

### 2024110442004211_Issue%20Accessing%20GPU%28s%29%20on%20fviz1.md
# Ticket 2024110442004211

 ```markdown
# Issue Accessing GPU(s) on fviz1

## Keywords
- Fritz cluster
- GPU access
- fviz1
- VirtualGL
- Maintenance
- Job submission

## Summary
A user reported being unable to access the GPU(s) on fviz1 after a maintenance event. The user attempted to submit a job using the `/apps/virtualgl/submitvirtualgljob.sh --time=3:00:00` command but the job did not start after waiting for over an hour.

## Root Cause
- Potential issues with the GPU nodes or job scheduling system post-maintenance.

## Solution
- HPC Admins need to investigate the status of the GPU nodes and the job scheduling system.
- Check for any configuration changes or errors introduced during the maintenance.
- Verify the availability and functionality of the GPU resources on fviz1.

## Actions Taken
- User reported the issue via an HPC support ticket.
- HPC Admins to investigate and resolve the issue.

## Lessons Learned
- Maintenance activities can introduce issues with hardware and software configurations.
- Users should be informed about potential disruptions and steps to take if issues arise post-maintenance.
- Regular checks of system functionality after maintenance are crucial to ensure smooth operation.
```
---

### 2025030542002411_Tier3-Access-Alex%20%22Aniol%20Serra%20Juhe%22%20_%20iwi5094h.md
# Ticket 2025030542002411

 # HPC Support Ticket Analysis

## Keywords
- Job runtime limit
- Checkpointing
- NHR application
- GPU cluster resources
- Large 3D data
- Miniconda, PyTorch, cuDNN
- DL generative models
- Segmentation models
- Synthetic 3D data

## Summary
- **User Request**: Access to GPU cluster for training deep learning models.
- **Issue**: User requires more computational resources than available on the current tier.
- **Root Cause**: Limited GPU resources and job runtime limit of 24 hours.
- **Solution**:
  - **Checkpointing**: Suggested to implement checkpointing for long-running jobs.
  - **NHR Application**: Recommended applying for additional resources through NHR.

## Lessons Learned
- **Job Runtime Limits**: Ensure users are aware of job runtime limits and suggest checkpointing for long-running jobs.
- **Resource Allocation**: Understand user requirements and guide them towards appropriate resource allocation, including applying for additional resources if needed.
- **Communication**: Follow up on user requests and close tickets if no response is received after a reasonable period.

## References
- [NHR Application](https://doc.nhr.fau.de/nhr-application/)
- [HPC Support](https://hpc.fau.de/)

## Next Steps
- **Follow-up**: Ensure users are aware of the resources available and the process for requesting additional resources.
- **Documentation**: Update documentation to include information on job runtime limits and checkpointing.

---

This analysis provides a concise overview of the support ticket, highlighting key issues and solutions for future reference.
---

### 2022061542001617_Job%20auf%20TinyGPU%20nutzt%20nur%20eine%20GPU%20%5Biwi9012h%5D.md
# Ticket 2022061542001617

 # HPC Support Ticket: Job on TinyGPU Utilizes Only One GPU

## Keywords
- TinyGPU
- GPU utilization
- JobID 266526
- nvidia-smi
- ssh
- Monitoring system
- Resource allocation

## Summary
A user's job on TinyGPU was only utilizing one of the four requested GPUs. The HPC Admin provided a screenshot from the monitoring system and instructions on how to check GPU utilization using `nvidia-smi`.

## Root Cause
The user's code was not properly configured to utilize all four GPUs, leading to inefficient resource usage.

## Solution
- **User Action**: The user acknowledged the issue and requested the job to be canceled to free up resources.
- **Admin Guidance**: The HPC Admin advised the user to ensure that their code can utilize the requested GPUs before submitting jobs. They also provided a link to the documentation on working with NVIDIA GPUs.

## General Learnings
- Always verify that your code can utilize the requested GPU resources.
- Use `nvidia-smi` to monitor GPU utilization.
- Be mindful of resource allocation to avoid wasting computational resources.

## References
- [Working with NVIDIA GPUs](https://hpc.fau.de/systems-services/systems-documentation-instructions/special-applications-and-tips-tricks/working-with-nvidia-gpus/)
---

### 2021102842000258_TensorFlow%20job%20on%20TinyGPU%20-%20ilev004h.md
# Ticket 2021102842000258

 ```markdown
# HPC-Support Ticket: TensorFlow Job on TinyGPU

## Keywords
- TensorFlow
- GPU
- TinyGPU
- Woody
- Job Queue
- GPU Support
- CUDA
- cuDNN
- Error Messages
- Job Optimization

## Summary
A user encountered issues with TensorFlow jobs not utilizing GPUs on TinyGPU. The jobs were deleted from the queue due to non-usage of GPU resources. The user needed assistance to run the jobs on the GPU or to continue running them on the CPU.

## Root Cause
- The TensorFlow binary did not have GPU support.
- The job output indicated "Registered devices: [CPU, XLA_CPU]".

## Solution
- The HPC Admin suggested running the jobs on Woody instead of TinyGPU, as Woody had higher CPU clock speeds and more available nodes.
- The user was advised to modify the job submission script to use Woody's resources.

## Lessons Learned
- Always check the binary for GPU support and ensure the setup is correct.
- Review job output for error messages and device registration information.
- Consider running CPU-intensive jobs on clusters with higher CPU clock speeds and more available nodes.
- Be prepared to adjust job submission scripts to utilize different resources.

## Actions Taken
- The HPC Admin provided guidance on modifying the job submission script to run on Woody.
- The user successfully ran the jobs on Woody, resolving the issue.
```
---

### 2025011642002314_Jobs%20on%20TinyGPU%20using%20only%201%20of%202%20GPUs%20%5Biwso166h%5D.md
# Ticket 2025011642002314

 # HPC Support Ticket: Jobs on TinyGPU Using Only 1 of 2 GPUs

## Keywords
- TinyGPU
- GPU utilization
- JobID
- ClusterCockpit
- `srun`
- `nvidia-smi`
- Resource allocation

## Problem
- User's jobs on TinyGPU (JobIDs: 974532, 974561, 974607, 974608) were using only one of the two allocated GPUs.

## Diagnosis
- HPC Admin identified the issue through the monitoring system and provided a screenshot.
- Users can check GPU utilization via ClusterCockpit or by attaching to the running job using `srun` and running `nvidia-smi`.

## Solution
- Ensure that the code can utilize the allocated GPUs effectively.
- Avoid allocating GPU nodes if the code cannot make use of the GPUs to prevent resource wastage.

## Steps for Users
1. **Check GPU Utilization**:
   - Log into ClusterCockpit: [https://monitoring.nhr.fau.de/](https://monitoring.nhr.fau.de/)
   - Alternatively, attach to the running job:
     ```bash
     srun --pty --overlap --jobid YOUR-JOBID bash
     nvidia-smi
     ```

2. **Optimize Resource Allocation**:
   - Ensure the code is optimized to use the allocated GPUs.
   - Only allocate GPU nodes if necessary.

## Contact
For further assistance, contact the HPC support team at [support-hpc@fau.de](mailto:support-hpc@fau.de).

---

**Note**: This documentation is intended for HPC support employees to reference when similar issues arise.
---

### 2023011242001577_Out%20of%20Memory%20error.md
# Ticket 2023011242001577

 # HPC-Support Ticket Conversation: Out of Memory Error

## Subject:
Out of Memory error

## User Issue:
- User is trying to run an RNN with MR images on the HPC cluster using PyTorch on the GPU.
- The job script allocates too much memory, causing an "Out of Memory" error.
- User has tried reducing batch size and other parameters but still encounters the issue.

## HPC Admin Response:
- Suggested reducing batch size, patch size, and number of features in convolutional layers.
- Noted that the nominal memory of the V100 GPU is 22GB, but less is available due to code and driver loading.
- Provided documentation links for memory management and `PYTORCH_CUDA_ALLOC_CONF`.

## Additional Issues:
- User encountered problems running the job on an NVIDIA A100 GPU due to PyTorch compatibility issues.
- User's virtual environment did not have the correct CUDA version installed.

## Solutions Provided:
- User was advised to install the correct versions of PyTorch and CUDA using specific commands.
- User was instructed to load the necessary modules (`cuda/11.1.0` and `cudnn/8.0.5.39-cuda11.1`) before installing PyTorch.
- User was advised to create a new conda environment with the correct versions of PyTorch, torchvision, torchaudio, and CUDA.

## Final Outcome:
- Despite installing the correct versions, the user's model was still too large for the A100 GPU.
- User was advised to check the network implementation and discuss memory issues with their supervisor.
- The ticket was closed as the HPC support could not provide further assistance.

## Key Takeaways:
- Ensure that the correct versions of PyTorch and CUDA are installed and compatible with the GPU being used.
- Reduce batch size, patch size, and number of features in convolutional layers to manage memory usage.
- Load necessary modules before installing PyTorch in a conda environment.
- If the model is still too large, consider optimizing the network implementation or discussing memory issues with a supervisor.

## Future Note:
- For setting up a new environment on the A100 GPU, use the following commands:
  ```bash
  $tinyx: salloc.tinygpu --gres=gpu:a100:1 --time=00:30:00 --partition=a100
  $tg095: module load python cuda/11.1.0 cudnn/8.0.5.39-cuda11.1
  export http_proxy=http://proxy:80
  export https_proxy=http://proxy:80
  conda create --name tinyA100 python=3.8
  source activate tinyA100
  conda install pytorch torchvision torchaudio pytorch-cuda=11.7 -c pytorch -c nvidia
  python -c 'import torch; print(torch.rand(2,3).cuda())'
  ```
---

### 2023062142004824_Tier3-Access-Alex%20%22Peneeta%20Wojcik%22%20_%20bcpc006h.md
# Ticket 2023062142004824

 # HPC-Support Ticket Conversation Analysis

## Keywords
- HPC Access
- Alex Cluster
- Amber Software
- GPU Resources
- A100 vs A40 GPUs
- Molecular Dynamics Simulations
- Resource Allocation
- Account Linking

## Summary
A user requested access to the Alex cluster for molecular dynamics simulations using Amber software. The initial request had inconsistencies regarding the type of GPUs needed and the amount of GPU hours required. The HPC Admins sought clarification and provided alternative resources for system preparation.

## Root Cause of the Problem
- Inconsistent information in the initial request regarding GPU type and hours.
- Misunderstanding about the capabilities of Amber software with GPUs.

## Solution
- Clarified that A40 GPUs are sufficient for the user's needs.
- Justified the need for 9000 GPU hours for the simulations.
- Linked the user's HPC account to the Alex cluster for easier workflow.
- Advised to use NHR project resources if GPU hours exceed 9000.

## General Learnings
- Ensure clear and consistent information in resource requests.
- Understand the specific requirements and capabilities of the software being used.
- Consider alternative resources for system preparation and setup.
- Communicate effectively with users to clarify needs and provide appropriate resources.

## Action Taken
- User's account was granted access to the Alex cluster.
- Advised to use NHR project resources for additional GPU hours if needed.

## Follow-up
- Monitor the user's GPU usage and provide guidance on accessing NHR project resources if necessary.
---

### 2021111142002081_Early-Alex%20%22Eduard%20Neu%22%20_%20bcpc001h.md
# Ticket 2021111142002081

 ```markdown
# HPC Support Ticket Analysis

## Keywords
- GPGPU cluster 'Alex'
- Nvidia A100 GPGPUs
- Nvidia A40 GPGPUs
- GROMACS
- Molecular dynamics simulations
- Multiple-walker Metadynamik-Simulationen
- Slurm job scripts
- Partition configuration
- Module loading

## Summary
A user requested access to the GPGPU cluster 'Alex' for molecular dynamics simulations using GROMACS. The user specified the need for both Nvidia A100 and A40 GPGPUs, detailing the types of simulations and the reasons for choosing each GPU type.

## Problem
- The user needed access to specific GPGPU resources for different types of simulations.
- The user required detailed instructions on how to configure and run jobs on the cluster.

## Solution
- The HPC Admin provided access to the user as a test user on the 'Alex' cluster.
- The admin specified that only A40 GPUs were currently available in the partition "a40".
- Documentation was provided for the 'Alex' cluster.
- Instructions were given to modify Slurm job scripts for compatibility with the 'Alex' cluster, including partition and GPU resource specifications.
- The admin recommended loading the `gromacs/2021.4-gcc11.2.0-mkl-cuda` module.

## Lessons Learned
- Users need clear instructions on how to configure job scripts for specific partitions and GPU types.
- Providing access to test users requires detailed communication about available resources and necessary configurations.
- Documentation and module availability are crucial for users to successfully run their simulations.
```
---

### 2025011642002298_Jobs%20do%20not%20fully%20use%20GPU%20%5Bb250be%5D.md
# Ticket 2025011642002298

 # HPC Support Ticket: Jobs Do Not Fully Use GPU

## Summary
A user's job on the HPC cluster was not fully utilizing the allocated GPUs. The job involved training a reinforcement learning (RL) agent, with most of the time spent interacting with the environment on CPU cores and a small fraction of the time spent training on the GPU.

## Root Cause
- The job was not optimized to fully utilize the GPU resources.
- The environment simulation, which does not benefit from GPU acceleration, was taking up most of the time.
- The GPU was only used for a short period during the training phase.

## Key Points Learned
- **Monitoring GPU Utilization**: Users can monitor GPU utilization using the monitoring system ClusterCockpit or by attaching to the running job with `srun --pty --overlap --jobid YOUR-JOBID bash` and running `nvidia-smi`.
- **Optimizing Resource Allocation**: Ensure that jobs make full use of allocated resources. Allocate nodes with GPUs only if the job can effectively utilize them.
- **Separating CPU and GPU Tasks**: For jobs that require both CPU and GPU resources, consider separating the tasks. Run environment simulations on a CPU cluster and transmit trajectories to a dedicated GPU node for training.
- **Avoiding Over-Provisioning**: Do not allocate the most potent GPUs if the job does not require their full capacity.

## Recommendations
- **Separate CPU and GPU Tasks**: Move environment simulation to a separate CPU cluster and transmit trajectories to a dedicated GPU node for training.
- **Optimize GPU Allocation**: Avoid using high-end GPUs like A100 if the job does not fully utilize their capacity.
- **Increase CPU Cores**: If possible, allocate more CPU cores for environment simulation to speed up the process.

## Solution
The user was advised to separate the environment simulation and training tasks. The environment simulation should be run on a CPU cluster, and the generated trajectories should be transmitted to a dedicated GPU node for training. This setup allows more efficient utilization of both CPU and GPU resources. The user was also advised not to allocate high-end GPUs if the job does not fully utilize their capacity.

## Follow-Up
The user confirmed that the current jobs on A40 GPUs were performing well. The ticket was closed as the user was satisfied with the setup and did not require further assistance.

## Keywords
- GPU Utilization
- Resource Allocation
- Reinforcement Learning
- Environment Simulation
- GPU Training
- ClusterCockpit
- nvidia-smi
- CPU Cluster
- GPU Node
- A100
- A40
- TinyGPU
- Frits
- Alex
- HPC Cluster
- Job Optimization
---

### 2023041342001962_Job%20on%20Alex%20does%20not%20use%20GPU%20%5Biwal102h%5D.md
# Ticket 2023041342001962

 # HPC Support Ticket: Job on Alex does not use GPU

## Keywords
- GPU utilization
- Job monitoring
- `nvidia-smi`
- Node health check
- Job resubmission

## Summary
A user reported that a job on the HPC system Alex was not utilizing the requested GPU, despite similar jobs running successfully. The HPC Admin provided guidance on checking GPU usage and identified a potential hardware issue.

## Problem
- Job ID 713059 on Alex did not use the requested GPU.
- User's other jobs were utilizing GPUs without issues.
- `nvidia-smi` command returned error messages.

## Troubleshooting Steps
1. **Monitoring**: HPC Admin provided a screenshot from the monitoring system showing the job's GPU usage.
2. **Job Inspection**: User was instructed to attach to the running job using `srun --pty --jobid bash` and check GPU utilization with `nvidia-smi`.
3. **Node Health**: HPC Admin identified that the node was in "drain" mode due to a GPU issue detected by the health checker.

## Root Cause
- The node's GPU was malfunctioning, causing the job to fail to utilize the GPU.

## Solution
- The node required maintenance or a reboot to resolve the GPU issue.
- User resubmitted the job, which potentially resolved the issue if the job was allocated to a different node.

## Conclusion
- Hardware issues can cause jobs to fail to utilize requested resources.
- Monitoring and health checks are crucial for identifying and resolving such issues.
- Users should resubmit jobs if they encounter hardware-related problems, as the issue might be node-specific.

## Follow-up
- HPC Admin to monitor the node and perform necessary maintenance.
- User to report back if the resubmitted job encounters the same issue.
---

### 2022051942000792_Tier3-Access-Alex%20%22Luca%20Schmidtke%22%20_%20iwai066h.md
# Ticket 2022051942000792

 ```markdown
# HPC Support Ticket Analysis

## Subject
Tier3-Access-Alex "Luca Schmidtke" / iwai066h

## Keywords
- HPC Account
- Certificate Expiration
- Account Activation
- GPGPU Cluster 'Alex'
- Nvidia A100 GPGPUs
- Python
- PyTorch
- Computer Vision Research

## Problem
- User's HPC account was incorrectly identified.
- Certificate expiration issue.

## Solution
- Correct account identification: iwai0*0*6h instead of iwai0*6*6h.
- Account activated on Alex.

## Lessons Learned
- Ensure correct account identification to avoid access issues.
- Regularly check and renew certificates to prevent expiration issues.
- Provide clear instructions for account activation and certificate management.

## Additional Notes
- User requested access to GPGPU cluster 'Alex' for computer vision research.
- Required software: Python, PyTorch.
- Expected outcome: Research paper.
```
---

### 2021031242000827_Job%20553741%20ohne%20GPU-Nutzung%20auf%20TinyGPU%20%5Bbccc007h%5D.md
# Ticket 2021031242000827

 # HPC Support Ticket Analysis

## Subject: Job 553741 ohne GPU-Nutzung auf TinyGPU [bccc007h]

### Keywords
- GPU utilization
- TinyGPU cluster
- Woody cluster
- Resource wastage
- Nutzungsrichtlinien
- LAMMPS jobs
- NHR

### Summary
- **Issue**: A job (553741) running on TinyGPU without utilizing the GPU.
- **Root Cause**: User running non-GPU jobs on a GPU-dedicated cluster.
- **Solution**: Redirect user to Woody cluster for non-GPU jobs.

### Details
- **HPC Admin**: Notified the user about the job not utilizing the GPU and provided a screenshot from the system monitoring.
- **Guidance**: Advised the user to use the Woody cluster for simulations that do not require GPU resources.
- **Policy**: Emphasized that using TinyGPU for non-GPU jobs violates the usage guidelines and wastes resources.
- **Offer of Assistance**: Offered help if the user could not explain why the job was not utilizing the GPU.

### Additional Notes
- **LAMMPS Jobs**: Mentioned that LAMMPS jobs are not optimized, and there is a need to build knowledge for NHR.
- **Future Actions**: Encourage users to follow the appropriate cluster usage guidelines to avoid resource wastage.

### Conclusion
- Ensure users are aware of the correct clusters to use for different types of jobs to optimize resource utilization.
- Provide support and guidance for users to understand and follow the usage policies.

---

This report can be used as a reference for similar issues in the future to ensure efficient resource management and adherence to usage guidelines.
---

### 2023040642000744_Tier3-Access-Alex%20%22Srikanth%20Korse%22%20_%20iwal101h.md
# Ticket 2023040642000744

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Keywords
- HPC Account
- Certificate Expiration
- Alex Cluster
- Nvidia A100 GPUs
- Slurm Scripts
- Research Project
- GPU-hours

## Summary
- **User Request:** Access to the GPGPU cluster 'Alex' for a research project.
- **Resources Requested:** 1*24*100 GPU-hours on Nvidia A100 GPUs.
- **Software Needed:** Access to GPU through Slurm scripts.
- **Expected Outcome:** Successful research with publications.

## Root Cause of the Problem
- Certificate expiration leading to account issues.

## Solution
- HPC Admin enabled the user's HPC account on Alex.

## General Learnings
- Certificate expiration can cause account access issues.
- Proper communication and account re-enabling by HPC Admins can resolve such issues.
- Users should be aware of certificate expiration dates to avoid disruptions.
```
---

### 2023062142000766_Tier3-Access-Alex%20%22Andreas%20Horlbeck%22%20_%20iwi5142h.md
# Ticket 2023062142000766

 # HPC Support Ticket Analysis: Tier3-Access-Alex

## Keywords
- Tier3 Access
- Alex GPGPU Cluster
- Nvidia A100, A40 GPGPUs
- GPU-hours
- Python, Pytorch, Matplotlib, Numpy, Pandas
- Object Detection
- Project Thesis
- SSH Login
- TinyGPU

## Summary
- **User Request**: Access to Alex GPGPU cluster for object detection with transformers.
- **Issues Identified**:
  - Unclear justification for access.
  - No proof of extended demand or job efficiency.
  - No jobs run on TinyGPU to demonstrate code performance.
  - Large GPU-hour request without sufficient justification.
  - No SSH login or successful jobs on TinyGPU.

## Root Cause
- Insufficient information provided in the application.
- Lack of evidence for the need for extensive GPU resources.
- No prior usage of TinyGPU to demonstrate code efficiency.

## Solution
- **HPC Admin**: Requested additional information for successful processing of the application.
- **HPC Admin**: Noted the high GPU-hour request and its impact on the overall FAU-Kontingent.
- **HPC Admin**: Closed the ticket due to lack of necessary information and justification.

## Lessons Learned
- Users must provide clear justification and evidence for resource requests.
- Prior usage and successful job runs on smaller clusters (e.g., TinyGPU) can help demonstrate code efficiency.
- Large resource requests should be carefully evaluated to avoid over-allocation.
- Regular monitoring of user accounts and resource usage is essential for efficient HPC management.

## Next Steps for Similar Issues
- Request detailed justification and evidence for resource needs.
- Encourage users to run test jobs on smaller clusters to demonstrate code performance.
- Evaluate the impact of large resource requests on overall system availability.
- Close tickets that lack sufficient information for processing.
---

### 2020021442000578_jobs%20on%20TinyGPU%20-%20btr0000h.md
# Ticket 2020021442000578

 # HPC-Support Ticket: Jobs on TinyGPU - btr0000h

## Keywords
- TinyGPU
- GPU utilization
- nvidia-smi
- CUDA
- GeForce GTX 1080
- Memory usage
- GPU-Util

## Summary
- **Issue**: Jobs on TinyGPU are not utilizing GPUs.
- **Root Cause**: Certificate has expired.
- **Symptoms**:
  - `nvidia-smi` shows high memory usage but 0% GPU utilization.
  - GPUs are in power-saving mode (P8).
- **Affected Hardware**: GeForce GTX 1080 GPUs on TinyGPU.

## Diagnostic Output
```
root@tg042:~# nvidia-smi
Fri Feb 14 09:29:18 2020
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 440.33.01    Driver Version: 440.33.01    CUDA Version: 10.2     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|===============================+======================+======================|
|   0  GeForce GTX 108...  On   | 00000000:02:00.0 Off |                  N/A |
| 29%   28C    P8     8W / 250W |  10681MiB / 11178MiB |      0%      Default |
+-------------------------------+----------------------+----------------------+
|   1  GeForce GTX 108...  On   | 00000000:03:00.0 Off |                  N/A |
| 29%   26C    P8     8W / 250W |  10681MiB / 11178MiB |      0%      Default |
+-------------------------------+----------------------+----------------------+
|   2  GeForce GTX 108...  On   | 00000000:83:00.0 Off |                  N/A |
| 29%   26C    P8     8W / 250W |  10681MiB / 11178MiB |      0%      Default |
+-------------------------------+----------------------+----------------------+
|   3  GeForce GTX 108...  On   | 00000000:84:00.0 Off |                  N/A |
| 29%   27C    P8     8W / 250W |  10681MiB / 11178MiB |      0%      Default |
+-------------------------------+----------------------+----------------------+
```

## Solution
- Renew the expired certificate to restore GPU functionality.

## Notes
- Regularly check certificate validity to prevent similar issues.
- Use `nvidia-smi` to monitor GPU usage and identify underutilization problems.
---

### 2022030742001405_Question%20on%20a100%20and%20rtx3080%20nodes.md
# Ticket 2022030742001405

 # HPC Support Ticket Analysis: GPU Job Scheduling Delay

## Keywords
- GPU jobs
- Scheduling delay
- A100 nodes
- RTX3080 nodes
- `squeue`
- `sinfo`
- AssocGrpGRES
- Job pending
- Idle nodes

## Summary
A user experienced a significant delay in scheduling long-running GPU jobs on A100 nodes, despite the availability of idle nodes.

## Root Cause
- The user's association had exceeded its allocated GPU resources (AssocGrpGRES), leading to job pending state.
- High demand for GPU resources by the user's group, with an average occupation of 12x A100 GPUs and ~20x other GPUs, and sometimes over 300 queued jobs.

## Diagnostic Steps
- User checked node availability using `sinfo`.
- User submitted a job and checked its status using `squeue -l`.
- HPC Admin confirmed the resource limitation using AssocGrpGRES.

## Solution
- No immediate solution was provided. The user should monitor their group's GPU usage and consider requesting additional resources if needed.
- HPC Admins may review the group's GPU allocation if the issue persists.

## Notes
- The behavior is expected due to the user's group exceeding its allocated resources.
- The job started around 5 hours after submission, when resources became available.

## Related Commands
- `sinfo`: Check node availability.
- `squeue -l`: Check job status.
- AssocGrpGRES: Association's allocated resources.
---

### 2025031042003204_Job%20on%20Helma%20is%20using%2064%20GPUs%20with%20only%2012.55%25%20utilization%20%5Bb180dc%5D.md
# Ticket 2025031042003204

 # HPC Support Ticket: Low GPU Utilization

## Keywords
- GPU utilization
- Job monitoring
- Resource allocation
- ClusterCockpit
- `nvidia-smi`
- `srun`

## Summary
A job on the Helma cluster was using 64 GPUs with only 12.55% utilization. The HPC Admin notified the user about the low utilization and provided instructions on how to monitor GPU usage.

## Root Cause
The user's code was not fully utilizing the allocated GPU resources, leading to inefficient resource usage.

## Steps Taken
1. **HPC Admin:**
   - Notified the user about the low GPU utilization.
   - Provided instructions to monitor GPU usage via ClusterCockpit and `nvidia-smi`.
   - Advised the user to allocate GPU nodes only if the code can make use of them.

2. **User:**
   - Acknowledged the issue and mentioned they were working on resolving it.
   - Reduced the number of allocated GPUs.

## Solution
The user reduced the number of allocated GPUs and is working on resolving the issue with their code to improve GPU utilization.

## Lessons Learned
- Regularly monitor GPU utilization to ensure efficient resource usage.
- Use ClusterCockpit and `nvidia-smi` to check GPU utilization.
- Allocate GPU nodes only if the code can effectively use them.

## Follow-up
- The ticket was closed as the job is being investigated by the user.
- If similar issues arise, advise users to monitor their GPU utilization and adjust resource allocation accordingly.
---

### 2024040242003532_Tier3-Access-Alex%20%22ZAINA%20HUSSEIN%22%20_%20iwi5167h.md
# Ticket 2024040242003532

 ```markdown
# HPC Support Ticket Conversation Analysis

## Subject
Tier3-Access-Alex / iwi5167h

## Keywords
- Account Enablement
- GPGPU Cluster 'Alex'
- Nvidia A100 GPGPUs
- Master Thesis
- Cross-validation of Network Architectures
- Training Data for Learning-based X-ray Scatter Estimation
- Software Requirements: putty, winscp, python, conda

## Summary
- **User Request**: Access to GPGPU cluster 'Alex' for master thesis work on cross-validation of network architectures and training data for learning-based X-ray scatter estimation.
- **Software Requirements**: putty, winscp, python, conda.
- **Expected Outcome**: Fully trained models.

## Actions Taken
- **HPC Admin**: Decided to enable the user's account on Alex.
- **HPC Admin**: Informed the user that their account has been enabled.

## Lessons Learned
- **Account Enablement Process**: The process involves decision-making and enabling the account by HPC Admins.
- **Software Requirements**: Users may require specific software for their projects, which should be noted and provided if possible.
- **Communication**: Clear communication with the user about the status of their request is essential.

## Root Cause of the Problem
- User needed access to the GPGPU cluster 'Alex' for their master thesis work.

## Solution
- HPC Admins enabled the user's account on Alex and informed the user about the successful enablement.
```
---

### 2021112942003359_Early-Alex%20%22Ren%C3%83%C2%A9%20Oertel%22%20_%20mtec003h.md
# Ticket 2021112942003359

 # HPC Support Ticket Analysis

## Keywords
- Certificate expiration
- User account activation
- GPGPU cluster
- Nvidia A100, A40 GPUs
- CUDA, MPIs software
- System configuration testing

## Summary
- **Root Cause**: Certificate expiration led to user access issues.
- **Solution**: HPC Admin activated normal user accounts for the specified users.

## Details
- **User Request**: Access to GPGPU cluster 'Alex' with Nvidia A100 and A40 GPUs for configuration testing.
- **Required Software**: CUDA, MPIs.
- **Expected Outcome**: Stable and usable GPU cluster.
- **Action Taken**: HPC Admin activated user accounts (mtec002h and mtec003h) after certificate expiration was resolved.

## Learning Points
- Ensure certificates are up-to-date to avoid user access issues.
- Activate user accounts promptly to facilitate testing and usage of HPC resources.
- Regularly monitor and update certificates to prevent expiration-related problems.
---

### 2022113042002006_Tier3-Access-Alex%20%22Ahmad%20Nedal%20Ahmad%20Aloradi%22%20_%20iwal021h.md
# Ticket 2022113042002006

 # HPC Support Ticket Analysis

## Keywords
- HPC Account Activation
- Alex Cluster
- Nvidia A100 GPGPUs
- Python/Miniconda
- Deep Learning
- Audio Processing
- Speaker Recognition

## Summary
- **User Request:** Access to Alex cluster for deep learning tasks in audio processing.
- **Required Resources:** Nvidia A100 GPGPUs, Python/Miniconda.
- **Compute Time:** 4800 GPU-hours.
- **Application:** Training DNN models for speaker recognition.

## Issue
- **Root Cause:** User needed access to the Alex cluster for research purposes.

## Solution
- **Action Taken:** HPC Admin enabled the user's account on the Alex cluster.
- **Outcome:** User confirmed receipt of the account activation notice.

## General Learnings
- **Account Activation Process:** Understanding the steps involved in enabling a user's account on the Alex cluster.
- **Resource Allocation:** Importance of specifying required resources and compute time in the request.
- **Software Requirements:** Ensuring that the necessary software (Python/Miniconda) is available for the user's tasks.

## Documentation for Support Employees
- **Account Activation:** Ensure that the user's account is enabled on the specified cluster.
- **Resource Verification:** Confirm that the requested resources (e.g., Nvidia A100 GPGPUs) are available and allocated correctly.
- **Software Availability:** Verify that the required software (Python/Miniconda) is installed and accessible for the user's tasks.
- **Communication:** Notify the user once their account is activated and provide any necessary instructions or support.
---

### 2022111642002891_Tier3-Access-Alex%20%22Youssef%20Achari%20Berrada%22%20_%20iwia047h.md
# Ticket 2022111642002891

 # HPC Support Ticket Conversation Analysis

## Keywords
- Tier3 Access
- GPU-hours
- NHR Compute Time Proposal
- Quantum Machine Learning
- Navier-Stokes PDEs
- Physics-Informed Machine Learning
- VPN
- WSL 2
- SSH Error

## General Learnings
- **Resource Limits**: The free Tier3 service has limits on GPU-hours.
- **NHR Proposal**: Users needing more resources should discuss an NHR compute time proposal with their supervisor.
- **Account Activation**: HPC admins can enable user accounts on specific clusters.
- **Network Issues**: Users may encounter SSH errors due to network resolution issues.

## Specific Issues and Solutions

### Issue: Excessive GPU-hour Request
- **Root Cause**: User requested 12k GPU-hours, exceeding the free Tier3 service limit.
- **Solution**: HPC admin suggested discussing an NHR compute time proposal with the user's supervisor.

### Issue: Account Activation Status
- **Root Cause**: User was unaware of the account activation status.
- **Solution**: HPC admin confirmed account activation on the Alex cluster.

### Issue: SSH Error
- **Root Cause**: User encountered an SSH error due to a temporary failure in name resolution.
- **Solution**: Not explicitly stated in the conversation. Possible solutions include checking VPN connection, DNS settings, or contacting network support.

## Documentation for Support Employees

### Tier3 GPU-hour Limits
If a user requests GPU-hours exceeding the free Tier3 service limit, advise them to discuss an NHR compute time proposal with their supervisor. Refer to the [NHR application rules](https://hpc.fau.de/systems-services/documentation-instructions/nhr-application-rules/) for more information.

### Account Activation
To confirm a user's account activation status, check the user management system or contact the HPC admin team.

### SSH Temporary Failure in Name Resolution
If a user encounters an SSH error with a temporary failure in name resolution:
- Ensure the user is connected to the VPN.
- Check the user's DNS settings.
- If the issue persists, escalate to the network support team.

### Contact Information
- **HPC Support**: support-hpc@fau.de
- **NHR Rechenzeit Support**: Harald Lanig
- **Software and Tools Developer**: Jan Eitzinger, Gruber
- **Head of Datacenter**: Gerhard Wellein
- **Training and Support Group Leader**: Georg Hager
---

### 2024072542002762_Timeout%20in%20data%20distribution%20parallel%20pytorch.md
# Ticket 2024072542002762

 # HPC Support Ticket: Timeout in Data Distribution Parallel PyTorch

## Keywords
- PyTorch
- Data Distribution Parallel (DDP)
- Timeout
- NCCL
- Watchdog
- Collective Operation

## Problem Description
The user encountered a timeout error while using Data Distribution Parallel (DDP) in PyTorch for training deep neural networks with multiple GPUs. The error message indicated a collective operation timeout:
```
Watchdog caught collective operation timeout: WorkNCCL(SeqNum=25035, OpType=BROADCAST, NumelIn=105344, NumelOut=105344, Timeout(ms)=600000) ran for 600004 milliseconds before timing out.
```
The user needed to increase the timeout value, which was set to 10 minutes.

## Root Cause
The timeout error occurred due to a long-running operation on a single GPU while others were idle, causing the collective operation to time out.

## Solution
The user resolved the issue by setting the timeout directly when initializing the process group in PyTorch:
```python
dist.init_process_group("nccl", timeout=datetime.timedelta(seconds=1800))
```
This increased the timeout value to 30 minutes, preventing the error from occurring.

## Ticket Interaction
- The HPC Admin requested the job ID, job script, and SLURM output to investigate the issue.
- The user provided the requested information and later found the solution by adjusting the timeout setting in the PyTorch initialization.

## General Learnings
- Timeout errors in distributed training can be caused by imbalanced workloads among GPUs.
- Adjusting the timeout setting in the process group initialization can help prevent these errors.
- The `TORCH_NCCL_BLOCKING_WAIT` environment variable can also influence timeout behavior, but it did not resolve the issue in this case.

## Relevant Documentation
- [PyTorch Distributed Package](https://pytorch.org/docs/stable/distributed.html)
---

### 2023021542003433_Problem%20of%20HPC%20Continuous%20Usage%20Limit.md
# Ticket 2023021542003433

 # HPC Support Ticket: Problem of HPC Continuous Usage Limit

## Keywords
- HPC usage limit
- Job submission
- Slurm submit script
- QOS (Quality of Service)
- A100 GPUs
- TinyGPU cluster

## Problem
- User was informed of a 72-hour HPC usage limit extension but still faced issues submitting jobs exceeding 24 hours.

## Root Cause
- The user was not aware of the specific QOS flag required for submitting jobs longer than 24 hours on the A100 GPUs in the TinyGPU cluster.

## Solution
- To submit a job on the A100 GPUs in the TinyGPU cluster that can run for more than 24 hours, the user needs to add `--qos=a100_aibe` to their Slurm submit script.
- The user should be aware that only a maximum of 4 GPUs with this flag can be requested by their group, which may result in waiting times until the resources are free again.

## General Learnings
- Specific QOS flags may be required for extended job durations on certain resources.
- Resource limitations, such as the maximum number of GPUs that can be requested, should be communicated to users to manage expectations regarding waiting times.

## Actions Taken
- HPC Admin provided the necessary QOS flag and explained the resource limitations.
- The user acknowledged the solution and thanked the HPC Admin.

## Status
- The ticket was closed after the user confirmed understanding the solution.
---

### 2018082842001811_Re%3A%20%5BRRZE-HPC%5D%20Call%20for%20proposals%20on%20NVidia%20Tesla%20V100%20usage.md
# Ticket 2018082842001811

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Keywords
- NVidia Tesla V100 GPUs
- RRZE
- HPC
- GPU utilization
- qsub
- module load
- CPU bottleneck
- module system
- job submission
- queue

## General Learnings
- **Accessing V100 GPUs**: Users need to follow specific steps to access the V100 GPUs, including connecting to a different frontend node and loading a specific module.
- **GPU Utilization**: Low GPU utilization can be caused by CPU bottlenecks, especially in systems with many small, parallel simulations.
- **Module System Initialization**: The module system may not initialize correctly when jobs are submitted through the queue, but it works interactively.
- **Job Submission Syntax**: The syntax for job submission has changed, requiring explicit request of the queue instead of the hostname.

## Root Causes and Solutions
- **Low GPU Utilization**:
  - **Root Cause**: Many small, parallel simulations leading to a CPU bottleneck.
  - **Solution**: Optimize the system to reduce CPU bottlenecks or consider running larger simulations on the V100 GPUs.

- **Module System Not Initializing**:
  - **Root Cause**: The module system is not initialized when jobs are submitted through the queue.
  - **Solution**: Use `#/bin/bash -l` to ensure the module system is initialized correctly.

- **Job Submission Syntax Change**:
  - **Root Cause**: The syntax for job submission has changed.
  - **Solution**: Use the updated syntax `qsub -lnodes=1:ppn=40 -q v100 ...` to request the queue explicitly.
```
---

### 2024070242001654_Tier3-Access-Alex%20%22Venkatesh%20Pulletikurthi%22%20_%20iwst087h.md
# Ticket 2024070242001654

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject: Tier3-Access-Alex

### Keywords
- Access Grant
- GPGPU Cluster 'Alex'
- Nvidia A100
- Nvidia A40
- CUDA
- OpenMPI
- MKL
- Paraview
- NEKO
- Publications
- Conference Presentations
- Code Development

### Summary
- **User Request**: Access to GPGPU cluster 'Alex' for running GPU-based CFD code NEKO.
- **Required Resources**:
  - Nvidia A100 GPGPUs
  - Nvidia A40 GPGPUs
  - Compute Time: 8*24*2 GPU-hours
- **Required Software**:
  - CUDA
  - OpenMPI with Intel and CUDA
  - MKL
  - Paraview
- **Expected Outcomes**: Publications, conference presentations, and code development of NEKO.

### HPC Admin Response
- **Action**: Access granted to use 'Alex'.
- **Contact Information**: HPC Admin (Johannes Veh)

### General Learnings
- **Access Request Process**: Users request access to specific HPC resources by specifying their needs, including hardware, software, and expected outcomes.
- **Software Requirements**: Common software requirements for GPU-based computations include CUDA, OpenMPI, MKL, and Paraview.
- **Expected Outcomes**: Users often aim for publications, conference presentations, and code development as outcomes of their HPC usage.

### Root Cause of the Problem
- User needed access to specific HPC resources for their research.

### Solution
- HPC Admin granted access to the requested resources.
```
---

### 2020102242003713_Questions%20about%20applying%20for%20HPC.md
# Ticket 2020102242003713

 # HPC Support Ticket Analysis

## Keywords
- HPC Application
- Job Size
- Neural Network Training
- Medical Images
- GPU/CPU Usage
- Data Sensitivity

## Summary
A user inquired about applying for HPC usage to train a neural network for classifying medical images. The dataset size is 14GB, and one iteration takes about an hour on a personal laptop.

## Root Cause
- User needs guidance on applying for HPC usage.
- User requires clarification on filling out the job size on the application form.

## Solution
- **Contact with Official Email**: Users should contact HPC support using their official @fau.de email address.
- **Software and Hardware Requirements**: Users need to specify the software they plan to use and whether it runs on GPUs or CPUs.
  - **GPU Usage**: If the software can run on GPUs, the TinyGPU cluster can be utilized.
  - **CPU Usage**: If CPU-only, simultaneous iterations can be run, but individual iterations may not be faster than on a personal laptop.
- **Job Size**: Users should fill in the job size based on the number of nodes/CPUs/GPUs their application will typically run on.
- **Data Sensitivity**: Storage or processing of sensitive data (e.g., patient data) is not permitted on HPC systems.

## Additional Information
- More details about HPC systems can be found at [HPC Systems Information](https://www.anleitungen.rrze.fau.de/hpc/).

## General Learnings
- Users should be aware of the specific hardware requirements of their applications.
- Proper communication channels (official email) should be used for support requests.
- Data sensitivity and compliance with HPC policies are crucial considerations.

## Next Steps
- Users should gather the required information about their software and hardware needs before applying for HPC usage.
- Ensure compliance with data sensitivity policies when using HPC systems.
---

### 2023060942001841_Jobs%20on%20TinyGPU%20do%20not%20use%20allocated%20GPUs%20%5Biwi5099h%5D.md
# Ticket 2023060942001841

 ```markdown
# HPC Support Ticket: Jobs on TinyGPU do not use allocated GPUs

## Keywords
- TinyGPU
- GPU utilization
- Job allocation
- `nvidia-smi`
- `srun`

## Problem Description
- User's jobs on TinyGPU are not utilizing all allocated GPUs.
- Specifically, jobs are only using one GPU out of the two allocated.

## Root Cause
- The user's code may not be optimized to utilize multiple GPUs effectively.

## Solution
- **Monitoring GPU Utilization**:
  - Use `srun --pty --overlap --jobid YOUR-JOBID bash` to attach to the running job.
  - Run `nvidia-smi` to check the current GPU utilization.
- **Optimize Code**:
  - Ensure the code is designed to utilize multiple GPUs.
  - Allocate nodes with GPUs only if the code can make use of them.

## Additional Notes
- **Resource Management**:
  - Avoid allocating GPU resources if they are not being fully utilized.
  - This ensures that resources are not left idle and can be used by other users.

## Contact Information
- For further assistance, contact the HPC support team via `support-hpc@fau.de`.
```
---

### 2022112942000136_AssocGrpGRES.md
# Ticket 2022112942000136

 # HPC Support Ticket: AssocGrpGRES

## Keywords
- HPC job submission
- AssocGrpGRES
- A100 resources
- Throttling policies
- NHR compute time proposal

## Problem
- User's jobs are pending despite idle A100 resources.
- Error reason: AssocGrpGRES.
- Both submitted jobs and interactive jobs are affected.

## Root Cause
- A100 nodes are sponsored by specific groups and have throttling policies to ensure quality of service for sponsors.
- The user's group has a limited allocation of A100 GPUs.

## Solution
- For extended demands, groups need to submit an NHR compute time proposal to get allocations on Alex.
- [NHR Application Rules](https://hpc.fau.de/systems-services/documentation-instructions/nhr-application-rules/)

## General Learnings
- AssocGrpGRES error indicates that the user's group has reached its resource limit.
- Throttling policies are implemented to ensure fair resource distribution.
- Additional resources can be requested through specific allocation processes (e.g., NHR compute time proposal).
---

### 2024032242001687_Fwd%3A%20Sparse%20encoding%20project%20on%20Alex%20%28Sbail%C3%83%C2%B2%20and%20myself%29%3A%20need%.md
# Ticket 2024032242001687

 # HPC Support Ticket Conversation Analysis

## Keywords
- GPU allocation
- NHR application
- Deep learning project
- Alex cluster
- A100 GPUs
- Proposal submission
- Resource limits
- Deadline extension

## Summary
A user requested an increase in GPU allocation for a deep learning project to meet a paper submission deadline. The request was forwarded to the admin team, and the user was informed about the current resource usage and the need to submit an NHR application.

## Root Cause of the Problem
- The user needed additional GPU resources to complete tests and validations for a deep learning project before a paper submission deadline.
- The user had not yet submitted a proposal for GPU time and was requesting a temporary increase in resource limits.

## Solution
- The admin team increased the GPU allocation for the user's project to improve throughput.
- The user was advised to submit an NHR application to secure additional GPU resources for future projects.

## General Learnings
- Communication between users and the admin team is crucial for managing resource allocation and meeting project deadlines.
- Users should be aware of the resource limits and the need to submit proposals for additional GPU time.
- The admin team can provide support and guidance for preparing NHR applications and managing resource allocation.
- Temporary increases in resource limits may be granted to meet urgent project deadlines, but users should plan ahead and submit proposals for long-term resource needs.
---

### 2021022542003427_TinyGPU%20shell%20sehr%20langsam.md
# Ticket 2021022542003427

 ```markdown
# HPC Support Ticket: TinyGPU Shell Performance Issue

## Keywords
- TinyGPU
- Load
- Fileserver
- Metadata Operations
- Ganesha
- Certificate Expired

## Summary
A user reported slow performance on TinyGPU (tg061) and woody3, with operations like `exit` and `qstat.tinygpu -na` taking unusually long.

## Root Cause
- High load on fileservers (`/home/woody`, `/home/{hpc,vault}`) reaching over 1000.
- No specific user or process identified as the cause.
- Suspected internal limitations, possibly related to Ganesha.

## Observations
- Load spikes were observed multiple times without a clear cause.
- Real CPU load was low (<2 cores), and no high I/O wait times were observed on fundusn1/2.
- Metadata operations were significantly slowed down.

## Solution
- No immediate solution provided.
- Issue is expected to recur due to multiple observed peaks.
- Further investigation needed to identify the root cause and prevent future occurrences.

## Notes
- Certificate expiration was mentioned but not directly related to the performance issue.
- HPC Admins are aware of the recurring load spikes and their impact on performance.
```
---

### 2023101242003969_Tier3-Access-Alex%20%22Ravi%20Kiran%20Ayyala%20Somayajula%22%20_%20iwia052h.md
# Ticket 2023101242003969

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject
Tier3-Access-Alex / iwia052h

## Keywords
- Account Enablement
- Alex Cluster
- Nvidia A100 GPGPUs
- Nvidia A40 GPGPUs
- Walberla Software
- Scaling Simulation
- Performance Plots

## Summary
A user requested access to the Alex cluster for performing scaling simulations using Walberla software on Nvidia A100 and A40 GPGPUs. The HPC Admin enabled the user's account for access to Alex.

## Problem
User required access to the Alex cluster for specific hardware and software needs.

## Solution
HPC Admin enabled the user's account to use the Alex cluster.

## What Can Be Learned
- **Account Enablement Process**: Understanding how to enable user accounts for specific clusters.
- **Cluster Access Requests**: Handling requests for access to specific hardware and software resources.
- **User Needs**: Recognizing and addressing user requirements for specific computational resources and software.

## Additional Notes
- **Software Requirements**: Ensure that required software (e.g., Walberla) is available and properly configured on the cluster.
- **Resource Allocation**: Be prepared to allocate and manage computational resources based on user requests, such as GPU hours.
```
---

### 2025022242000704_Disable%20Numa%20Autobalancing%20auf%20aquavans.md
# Ticket 2025022242000704

 ```markdown
# Disable NUMA Autobalancing

## Keywords
- NUMA Autobalancing
- Benchmarks
- Performance Optimization
- GPU Hang
- AMD Instinct MI300X
- `/proc/sys/kernel/numa_balancing`

## Problem
- User requested to disable NUMA autobalancing for performance optimization during benchmarks.
- Concerns about GPU hanging due to periodic balancing.

## Root Cause
- NUMA autobalancing can cause performance issues and GPU hangs during benchmarks.

## Solution
- Disable NUMA autobalancing by setting the value in `/proc/sys/kernel/numa_balancing` to 0.
  ```sh
  sh -c 'echo 0 > /proc/sys/kernel/numa_balancing'
  ```
- Verify that NUMA balancing is disabled by checking the value.
  ```sh
  cat /proc/sys/kernel/numa_balancing
  ```
  The output should be `0` if disabled.

## Action Taken
- The request was forwarded to HPC Admins for implementation.

## General Learning
- Disabling NUMA autobalancing can improve performance and prevent GPU hangs during benchmarks.
- The setting must be changed by HPC Admins.
```
---

### 2023071242003813_Cuda%20out%20of%20memory%20error.md
# Ticket 2023071242003813

 # HPC Support Ticket: CUDA Out of Memory Error

## Subject
CUDA out of memory error

## User Issue
- **Error Message:** `torch.cuda.OutOfMemoryError: CUDA out of memory. Tried to allocate 790.00 MiB (GPU 0; 39.39 GiB total capacity; 38.28 GiB already allocated; 626.69 MiB free; 38.29 GiB reserved in total by PyTorch)`
- **Context:** User is running a job on HPC tinyGPU using the SDV Python library to generate synthetic datasets with the Probabilistic Autoregressive (PAR) model.

## HPC Admin Response
- **Initial Tips:**
  1. Set batch_size as small as possible.
  2. Reduce the number of kernels in convolutional layers.
  3. Reduce the number of out_channels/in_channels in fully connected layers.
- **Further Assistance:**
  - Referred the user to Chang Liu for code tweaking.
  - Suggested looking into the SDV documentation for fine-tuning the neural network.
  - Advised contacting the user's supervisor for further assistance.

## User Follow-Up
- **Additional Information:**
  - The PAR model has a 'cuda' argument to speed up modeling time using GPU.
  - The user does not specify batch size with the in-built PAR model function.
- **Resolution:**
  - The user eventually resolved the error, but the specific solution was not detailed in the conversation.

## Key Takeaways
- **Common Solutions for CUDA Out of Memory Errors:**
  1. Reduce batch size.
  2. Optimize neural network architecture (reduce kernels, channels).
  3. Consult documentation for fine-tuning options.
- **Importance of Documentation:**
  - Always refer to the specific library's documentation for fine-tuning options.
- **Collaboration:**
  - Involve relevant team members or supervisors for specialized assistance.

## Conclusion
The issue was resolved, but the specific solution was not detailed. General tips for avoiding CUDA out of memory errors were provided, and the user was referred to additional resources and personnel for further assistance.
---

### 2021110942003075_72h%20Queue%20f%C3%83%C2%BCr%20das%20IIS%3F.md
# Ticket 2021110942003075

 # HPC Support Ticket: 72h Queue Request

## Keywords
- Wallclock limit
- Queue setup
- Job partitioning
- QoS (Quality of Service)
- GPU allocation
- Job scheduling

## Problem
- Users are complaining about the 24-hour wallclock limit.
- Request for a queue with a maximum walltime of 72 hours.

## Root Cause
- Users need longer job runtimes for their tasks.
- Current 24-hour limit is insufficient for some users.

## Solution
- **QoS Option**: Users can use the `--qos=owner_a100_iwal` option in their job scripts to request up to 72 hours of runtime.
  - Maximum of 8 GPUs can be allocated with this QoS.
  - Jobs with this QoS will preempt other jobs without the QoS option.
- **Exclusive Node Reservation**: Alternatively, nodes can be reserved exclusively for the requesting group, but this may reduce the number of simultaneous jobs.

## Additional Notes
- Users should be aware that jobs with the QoS option may be terminated early during urgent maintenance.
- The HPC Admin expressed concern about users with poor job performance requesting longer runtimes.

## Action Taken
- HPC Admin provided the QoS option and explained the implications.
- Users were informed about the risks and potential impacts on other jobs.

## Follow-up
- Monitor the usage of the QoS option to ensure fair resource allocation.
- Provide training or guidance on job partitioning to help users optimize their workloads within the 24-hour limit.
---

### 2023030942003121_nvidia-smi%20und%20ClusterCockpit%20-%20mfml002h.md
# Ticket 2023030942003121

 ```markdown
# HPC-Support Ticket: nvidia-smi und ClusterCockpit - mfml002h

## Keywords
- nvidia-smi
- GPU
- A100-SXM
- Memory-Usage
- GPU-Util
- Training
- TinyGPU

## Problem Description
The user is training on two GPUs simultaneously (TinyGPU) and observes the following `nvidia-smi` output:

```
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util
|===============================+======================+===============|
|   0  NVIDIA A100-SXM...  On   | 00000000:81:00.0 Off |
| N/A   31C    P0    59W / 400W |  38355MiB / 40960MiB |      0%
+-------------------------------+----------------------+---------------+
|   1  NVIDIA A100-SXM...  On   | 00000000:C1:00.0 Off |
| N/A   30C    P0    58W / 400W |    559MiB / 40960MiB |      0%
+-------------------------------+----------------------+---------------+
| Processes:
|  GPU   GI   CI        PID   Type   Process name GPU 	Memory |Usage
|        ID   ID
|
```

## Root Cause
The user is concerned about the memory usage and GPU utilization during training on two GPUs.

## Solution
No solution provided in the ticket. Further investigation is needed to determine if the memory usage and GPU utilization are within expected ranges for the user's workload.

## General Learnings
- `nvidia-smi` is a useful tool for monitoring GPU usage and performance.
- Memory usage and GPU utilization should be monitored to ensure efficient resource allocation.
- Training on multiple GPUs can lead to varying memory usage and utilization patterns.

## Next Steps
- HPC Admins or 2nd Level Support team should analyze the `nvidia-smi` output to determine if the memory usage and GPU utilization are normal for the user's training workload.
- If abnormal, further investigation into the training process and GPU configuration may be required.
```
---

### 42116667_Busy%20tinygpu%3F.md
# Ticket 42116667

 # HPC Support Ticket Analysis: Busy tinygpu?

## Keywords
- tinygpu
- node occupation
- benchmark
- high performance computing
- resource release

## Summary
A user is attempting to access the `tinygpu` node for running benchmarks but finds it occupied. The user requests information about the current occupant and inquires about the possibility of releasing the node.

## Root Cause
- The `tinygpu` node is currently occupied by other users (`hpck034`, `hpck032`).

## Solution
- The HPC Admin needs to check the current usage of the `tinygpu` node and potentially communicate with the occupying users to determine if the node can be released for the requesting user's benchmarking needs.

## General Learnings
- Users may encounter resource contention when attempting to access specific nodes for benchmarking or other tasks.
- Effective communication with the HPC Admin is crucial for resolving resource allocation issues.
- Admins should have protocols in place for managing and prioritizing node usage, especially for critical tasks like benchmarking.

## Next Steps
- HPC Admin should investigate the current usage of the `tinygpu` node.
- If possible, negotiate with the current users to release the node or provide an alternative solution for the requesting user.

---

This documentation can be used to address similar issues related to node occupation and resource contention in the future.
---

### 2023071342004276_Delay%20in%20loading%20jobs.md
# Ticket 2023071342004276

 ```markdown
# HPC Support Ticket: Delay in Loading Jobs

## Keywords
- Job delays
- Queue waiting time
- sbatch command
- tinyGPU cluster
- Hardware defect
- Resource allocation

## Problem Description
- **User Issue**: Significant delays in job initiation (3-5 hours) compared to previous near-instant starts.
- **Root Cause**: Increased waiting time in the queue due to high demand and limited resources.

## Ticket Conversation Summary
- **User**: Reported delays in job initiation affecting work progress.
- **HPC Admin**: Provided status of the tinyGPU cluster, indicating normal operation but expected waiting times due to high demand.

## Solution
- **HPC Admin Response**: Informed the user that waiting times of a few hours are normal due to high demand and limited resources.
- **Additional Information**: Mentioned hardware defects affecting some RTX3080 nodes, but overall cluster operation is within normal parameters.

## General Learnings
- High demand can lead to significant delays in job initiation.
- Regular monitoring of cluster status and resource allocation is crucial.
- Users should be informed about expected waiting times during periods of high demand.

## Action Items
- Continue monitoring cluster usage and resource allocation.
- Inform users about potential delays during high-demand periods.
- Address hardware defects promptly to maintain cluster performance.
```
---

### 2023082342002631_Not%20utilizing%20all%20requested%20GPUs%20on%20TinyGPU%20%28mpt4022h%29.md
# Ticket 2023082342002631

 # HPC Support Ticket: Not Utilizing All Requested GPUs on TinyGPU

## Keywords
- GPU utilization
- Gromacs
- nvidia-smi
- srun
- benchmarking
- submit script
- ntmpi

## Problem
- User's jobs on TinyGPU were not utilizing all allocated GPUs.
- User was allocating two GPUs but Gromacs was configured to use only one (-ntmpi 1).

## Root Cause
- Incorrect configuration in the submit script leading to underutilization of allocated GPUs.

## Solution
- **HPC Admin**: Suggested using `srun --pty --overlap --jobid YOUR-JOBID bash` to attach to the running job and `nvidia-smi` to check GPU utilization.
- **HPC Admin**: Advised the user to allocate only a single GPU or edit the submit script to use both allocated GPUs (-ntmpi 2).
- **HPC Admin**: Informed the user that a Gromacs expert would contact them for further optimizations.
- **HPC Admin**: Benchmarking was attempted but could not be completed due to the system not being sufficiently equilibrated.

## General Learnings
- Ensure that the number of GPUs allocated matches the number configured in the submit script.
- Use `srun --pty --overlap --jobid YOUR-JOBID bash` and `nvidia-smi` to monitor GPU utilization.
- Collaborate with experts for benchmarking and optimization when needed.
- Ensure the system is properly equilibrated before attempting benchmarks.
---

### 2025011642002252_GPUs%20are%20not%20used%20%5Bv115be%5D.md
# Ticket 2025011642002252

 # HPC Support Ticket: GPUs are not used

## Keywords
- GPU utilization
- CPU-only nodes
- Resource allocation
- Data preprocessing
- FAISS
- ClusterCockpit
- nvidia-smi
- Fritz cluster

## Summary
A user mistakenly allocated more GPUs than needed, leading to idle GPU resources. The user inquired about access to CPU-only nodes for data processing tasks that require significant CPU and RAM resources.

## Root Cause
- User allocated GPUs without utilizing them.
- Need for CPU-only nodes for specific data processing tasks.

## Solution
- **Monitoring GPU Utilization:**
  - Use ClusterCockpit at [https://monitoring.nhr.fau.de/](https://monitoring.nhr.fau.de/).
  - Attach to running jobs using `srun --pty --overlap --jobid YOUR-JOBID bash` and check GPU utilization with `nvidia-smi`.

- **Data Preprocessing:**
  - Preprocess data locally, package into an archive (e.g., tar file), upload to `$WORK` or another suitable directory, and extract within the batch script.

- **Access to CPU-only Nodes:**
  - Initially, no option to switch to CPU-only nodes.
  - Alternative suggestion: Use FAISS with GPU mode for speed.
  - Later, access to the Fritz cluster was granted for CPU-only tasks.

## General Learnings
- Ensure proper allocation of GPU resources to avoid idle nodes.
- Use monitoring tools to check resource utilization.
- Preprocess data locally before uploading to HPC for efficient use of resources.
- Consider using specialized tools like FAISS for speed improvements.
- Access to CPU-only clusters like Fritz can be requested for tasks requiring significant CPU and RAM resources.

## Closing Note
The user's issue was resolved by granting access to the Fritz cluster for CPU-only tasks.
---

### 2023031342004051_Zugriff%20auf%20NHR%20Testcluster.md
# Ticket 2023031342004051

 # HPC-Support Ticket Conversation Analysis

## Keywords
- SYCL-Implementierung
- Discontinuous Galerkin Code
- Shallow Water Equations
- Performance Messungen
- Intel oneAPI Compiler
- GPU-Plugins
- AMD GPUs
- Nvidia GPUs
- Testcluster
- HPC-Professur
- SSH-Key
- Modulefiles
- CUDA
- ROCm
- SYCL_PI_TRACE
- Proxy Jump
- IPv6
- IPv4
- HPC Admin
- 2nd Level Support team
- Head of the Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support and Applications for Grants
- Software and Tools developer

## What Can Be Learned

### General Learnings
1. **Account Setup**: Users need to log in with their institutional credentials and upload an SSH key for account setup.
2. **Cluster Access**: Clusters are accessible via IPv6 or IPv4 with Proxy Jump.
3. **Modulefiles**: Proper configuration of modulefiles is crucial for software functionality.
4. **GPU Support**: Ensuring the correct versions of CUDA and ROCm are loaded is essential for GPU functionality.
5. **SYCL_PI_TRACE**: Used to verify the loading of SYCL plugins.
6. **Interactive Jobs**: Users may encounter issues with starting interactive jobs due to account or partition problems.

### Specific Issues and Solutions
1. **Modulefile Loading Issue**:
   - **Problem**: User could not load modulefiles due to directory not found.
   - **Solution**: Changed the directory from `/home/atuin` to `/home/saturn`.

2. **GPU Rechnen Issue**:
   - **Problem**: User could not perform computations on GPUs.
   - **Solution**: Ensured the correct versions of CUDA and ROCm were loaded. Added the ROCm library directory to the SYCL/AMD module.

3. **Interactive Job Issue**:
   - **Problem**: User could not start an interactive job on the testcluster.
   - **Solution**: Verified account and partition settings. Provided documentation on cluster usage and Proxy Jump.

4. **Compiler Issue**:
   - **Problem**: User encountered linking errors with the Intel icpx-Compiler for Nvidia/AMD GPUs.
   - **Solution**: Used the Intel-LLVM clang-Compiler and ensured the correct plugins were loaded.

### Root Causes
1. **Directory Permissions**: Users may not have access to certain directories, leading to modulefile loading issues.
2. **Incorrect Module Versions**: Loading incorrect or outdated versions of CUDA and ROCm can cause GPU functionality issues.
3. **Account/Partition Configuration**: Incorrect account or partition settings can prevent users from starting interactive jobs.
4. **Compiler Limitations**: The Intel icpx-Compiler may not support certain proprietary optimizations, requiring the use of Intel-LLVM.

### Solutions
1. **Directory Permissions**: Change the directory to one that the user has access to.
2. **Module Versions**: Ensure the correct versions of CUDA and ROCm are loaded.
3. **Account/Partition Configuration**: Verify and correct account and partition settings.
4. **Compiler Limitations**: Use the Intel-LLVM clang-Compiler and ensure the correct plugins are loaded.

This analysis provides a comprehensive overview of the issues encountered and their solutions, serving as a documentation for support employees to look up help for similar errors in the future.
---

### 2019060542000796_Problems%20with%20Gromacs%20and%20GPUs%20on%20TinyGPU.md
# Ticket 2019060542000796

 # HPC Support Ticket: Gromacs GPU Detection Issue on TinyGPU

## Keywords
- Gromacs
- GPU detection
- TinyGPU
- tg005
- Reboot
- Monitoring script
- Hardware failure

## Problem Description
- User reported that Gromacs was unable to detect GPUs on the TinyGPU machine `tg005`.
- The issue was specific to `tg005`; other machines ran the script without errors.

## Root Cause
- The machine `tg005` had lost one of its GPUs.

## Solution
1. **Initial Fix**: Rebooting the machine `tg005` temporarily resolved the issue by re-detecting both GPUs.
2. **Permanent Solution**: Due to recurring issues, the decision was made to decommission `tg005` permanently.

## Lessons Learned
- **Monitoring Scripts**: The monitoring script did not automatically detect the GPU loss. Manual invocation of `/var/cfengine/scripts/nodehealthcheck.pl` was required to identify the issue.
- **Hardware Lifespan**: Older hardware may experience intermittent failures, necessitating eventual decommissioning.

## Follow-Up Actions
- Improve monitoring scripts to automatically detect and report hardware failures.
- Plan for hardware upgrades or replacements to avoid recurring issues.

## Relevant Emails
- **User Report**: Initial issue reported with Gromacs not detecting GPUs on `tg005`.
- **HPC Admin Response**: Confirmed GPU loss and temporary fix via reboot.
- **User Follow-Up**: Reported recurrence of the issue.
- **HPC Admin Decision**: Decided to decommission `tg005` due to persistent hardware problems.

## Conclusion
- Regular monitoring and timely hardware maintenance are crucial for ensuring the smooth operation of HPC systems. Automated monitoring scripts should be regularly reviewed and updated to catch hardware failures promptly.
---

### 2021121742001391_Jobs%20auf%20TinyGPU%20%7C%20iwrt001h.md
# Ticket 2021121742001391

 # HPC Support Ticket: Jobs auf TinyGPU

## Keywords
- TinyGPU
- Jobskript
- --exclusive Option
- GPU Nutzung
- Ressourcenverwaltung

## Problem
- **Root Cause**: Der Benutzer fordert Jobs auf TinyGPU mit der Option `--exclusive` an, was dazu führt, dass der komplette Knoten mit 4 GPUs zugewiesen wird, obwohl nur eine GPU benötigt wird.
- **Auswirkung**: Die restlichen Ressourcen sind ungenutzt und nicht für andere Nutzer verfügbar.

## Lösung
- **Anweisung**: Die Option `--exclusive` aus dem Jobskript entfernen. Die angeforderte GPU und der entsprechende Anteil an CPUs sind auch ohne diese Option exklusiv für den Benutzer verfügbar.
- **Aktion**: Der Benutzer hat die aktuellen Tests abgebrochen und das Jobskript angepasst.

## Kommunikation
- **HPC Admin**: Hinweis auf die unnötige Nutzung der `--exclusive` Option und die Auswirkungen auf die Ressourcenverfügbarkeit.
- **Benutzer**: Dankbarkeit für den Hinweis und Bestätigung der Anpassung des Jobskripts.

## Ergebnis
- **Status**: Der Benutzer hat die Jobs neu gestartet und die Ressourcen werden nun effizienter genutzt.
- **Bestätigung**: HPC Admin hat die korrekte Anpassung bestätigt.

## Allgemeines
- **Wichtige Hinweise**: Die Nutzung der `--exclusive` Option kann zu ineffizienter Ressourcenverwaltung führen. Benutzer sollten sicherstellen, dass sie nur die benötigten Ressourcen anfordern.
- **Zukünftige Maßnahmen**: Benutzer sollten regelmäßig ihre Jobskripte überprüfen und bei Bedarf anpassen, um eine optimale Nutzung der HPC-Ressourcen zu gewährleisten.
---

### 2023120442002043_Ihpc100h%20-%20request%20for%20multimode%20GPGPU%20access.md
# Ticket 2023120442002043

 # HPC Support Ticket Conversation Analysis

## Keywords
- HPC
- Alex
- GPGPU
- Multimode
- MPI
- Likwid
- Performance analysis
- Energy consumption
- CA-Krylov solvers
- EuroHPC
- EoCoE-III
- SSH key
- Account sharing

## General Learnings
- Users may request access to additional resources such as multi-node jobs and GPGPU access.
- Users may encounter issues with SSH keys and account sharing.
- Users may request extensions for their accounts and additional user accounts for collaborators.
- Users may need assistance with performance analysis tools like Likwid.
- Users may be working on specific projects like CA-Krylov solvers and EuroHPC platforms.

## Root Causes and Solutions

### Request for Multimode GPGPU Access
- **Root Cause:** User needs access to more GPUs for scalability analysis.
- **Solution:** HPC Admins enabled the account to use up to 64 GPUs and provided instructions for multi-node job allocation.

### SSH Key Issue
- **Root Cause:** New SSH key added to the account is not working.
- **Solution:** HPC Admins suggested creating a separate account for the collaborator to avoid account sharing issues.

### Account Extension and Additional User
- **Root Cause:** User's project expired, and they need to continue using the HPC resources. Additionally, they need to add a collaborator.
- **Solution:** HPC Admins extended the account and added a new user account for the collaborator.

### Performance Analysis with Likwid
- **Root Cause:** User needs assistance with using Likwid for performance analysis and energy consumption comparison.
- **Solution:** HPC Admins provided guidance and suggested using their latest systems for Likwid analysis.

### Request for Additional Resources
- **Root Cause:** User needs access to more nodes and GPUs for testing while waiting for approval on another platform.
- **Solution:** HPC Admins can evaluate the request and provide access if resources are available.

## Documentation for Support Employees

### Multimode GPGPU Access
To enable multimode GPGPU access on Alex, follow these steps:
1. Enable the account to use up to 64 GPUs.
2. Provide the user with instructions for multi-node job allocation:
   ```bash
   #SBATCH --nodes=8 # any number from 2 to 8
   #SBATCH --partition=a40 # or a100
   #SBATCH --qos=a40multi # or a100multi
   ```

### SSH Key Issue
If a user reports issues with a new SSH key:
1. Verify that the SSH key was added correctly to the account.
2. Suggest creating a separate account for the collaborator to avoid account sharing issues.

### Account Extension and Additional User
To extend a user's account and add a collaborator:
1. Extend the account by the requested duration.
2. Create a new user account for the collaborator with the provided email, name, institution, and nationality.

### Performance Analysis with Likwid
To assist users with Likwid for performance analysis:
1. Provide guidance on using Likwid for energy consumption analysis.
2. Suggest using the latest systems for Likwid analysis if available.

### Request for Additional Resources
To evaluate requests for additional resources:
1. Assess the availability of the requested resources.
2. Provide access to the resources if available and inform the user of any limitations or conditions.

By following these guidelines, support employees can effectively address similar issues and requests in the future.
---

### 2022101142002517_AssocGrpGRES.md
# Ticket 2022101142002517

 # HPC Support Ticket: AssocGrpGRES

## Keywords
- Slurm Jobs
- Queue
- AssocGrpGRES
- Resource Allocation
- NHR Rechenzeitantrag
- FAU-Grundversorgung
- GPU Cluster
- Stromkosten

## Problem
- User's Slurm jobs are landing in the queue with the reason `AssocGrpGRES`.
- Despite available nodes, jobs are not being processed.
- Example: First job with 2 A100 GPUs runs, but the second job with 4 A100 GPUs is queued.

## Root Cause
- The user's group (i5) has exceeded its resource allocation within the free Tier3-Versorgung.
- The group has been a significant user of the FAU-Grundversorgung resources in recent periods.

## Solution
- The user's supervisor or a group leader needs to submit an NHR Rechenzeitantrag for additional resources.
- The application process is detailed at [NHR Application Rules](https://hpc.fau.de/systems-services/documentation-instructions/nhr-application-rules/).
- Future resource usage should be formally accounted for through NHR to avoid exceeding the free tier allocation.

## Additional Information
- The group's extensive use of the Alex GPU cluster has been noted.
- Future energy costs will be allocated based on usage, with a significant increase expected.
- NHR-tagged usage will not incur additional costs for the FAU.

## Action Items
- Submit an NHR Rechenzeitantrag to cover additional resource needs.
- Consider aligning future projects with funded research to streamline the application process.
- Monitor resource usage to stay within allocated limits and avoid job queuing issues.

## Conclusion
- Proper resource allocation and formal application processes are crucial for efficient use of HPC resources.
- Collaboration with HPC support and funding agencies can help optimize resource management and reduce costs.
---

### 2018042642000583_Problem%20mit%20AMBER%20auf%20TinyGPU.md
# Ticket 2018042642000583

 # HPC-Support Ticket: Problem mit AMBER auf TinyGPU

## Problem Description
- **User Issue**: Intermittent errors during MD simulations with AMBER on TinyGPU.
- **Error Messages**:
  - `NetCDF error: No such file or directory`
  - `write_nc_restart(): Could not open restart`
- **Affected Systems**: Different systems with AMBER (all available amber-gpu versions).
- **Observations**:
  - Error occurs during MD runs, not during resubmits.
  - Error does not occur on emmy's GPUs.
  - Restart files (*.rst) sometimes reappear after a short period.

## Root Cause Analysis
- **Potential Cause**: Issue with writing restart files to `/dev/shm`.
- **Details**:
  - `/dev/shm` is part of the main memory and can fill up depending on the size of the files.
  - The user's current job does not occupy much space in `/dev/shm`, and no other nodes have large data in `/dev/shm`.

## Solution and Workaround
- **Immediate Solution**: Not found.
- **Workaround**:
  - Suggested to modify job scripts to check output files for error messages and resubmit the job automatically if an error is detected.

## Key Takeaways
- **File System Issues**: Problems with writing to `/dev/shm` can cause intermittent errors.
- **Error Handling**: Automating job resubmission based on error messages can help mitigate the impact of such issues.
- **Monitoring**: Keeping track of the exact time and state of the working directory when errors occur can aid in diagnosing the problem.

## Next Steps
- **Monitoring**: HPC Admins will keep an eye on the issue for further occurrences.
- **User Action**: Implement the suggested workaround in job scripts to handle errors automatically.

## References
- **Support Team**: HPC Admins
- **Date**: 26.04.2018

---

This documentation can be used to diagnose and address similar issues in the future.
---

### 2022111442002582_Tier3-Access-Alex%20%22ebru%20navruz%22%20_%20iwal100h.md
# Ticket 2022111442002582

 # HPC Support Ticket Analysis

## Keywords
- HPC Account
- Alex Cluster
- GPGPU
- Nvidia A100
- Python
- Pytorch
- Deep Generative Neural Networks
- Speech Synthesis
- Audio Coding
- Certificate Expiration

## Summary
- **User Request**: Access to Alex cluster for utilizing Nvidia A100 GPGPUs.
- **Software Requirements**: Python, Pytorch.
- **Application**: Deep generative neural networks for speech synthesis and audio coding.
- **Expected Outcome**: Optimized neural speech codec with high perceptual quality and low computational complexity.

## Root Cause of the Problem
- **Certificate Expiration**: The user's HPC account certificate had expired.

## Solution
- **Account Re-enabled**: The HPC Admin re-enabled the user's account on Alex.

## General Learnings
- **Account Management**: Regularly check and renew certificates to avoid account disruptions.
- **Cluster Access**: Ensure proper communication with users regarding new hardware installations and access procedures.
- **Software Requirements**: Be prepared to support common software tools like Python and Pytorch for deep learning applications.

## Next Steps
- **Monitor Accounts**: Implement a system to monitor and alert users about certificate expiration.
- **User Training**: Provide training sessions on accessing and utilizing new hardware resources.

---

This documentation can be used as a reference for similar issues related to account management and hardware access in the HPC environment.
---

### 2023120442000367_Job%20on%20Alex%20does%20not%20use%20GPU%20%5Bb196ac10%5D.md
# Ticket 2023120442000367

 ```markdown
# HPC Support Ticket: Job on Alex does not use GPU

## Keywords
- GPU utilization
- Job monitoring
- Resource allocation
- ClusterCockpit
- `srun`
- `nvidia-smi`

## Summary
A user's job on the Alex cluster was not utilizing the allocated GPUs, leading to resource wastage.

## Problem
- **Root Cause:** The user's job was allocated 8 GPUs but did not utilize them.
- **Symptoms:** The job was running longer than expected without using the GPU resources.

## Solution
- **Steps Taken:**
  - The HPC Admin notified the user about the issue and provided instructions on how to monitor GPU utilization.
  - The user stopped the job and acknowledged the need to ensure proper GPU utilization in future jobs.

## Lessons Learned
- **Resource Management:** Ensure that jobs requesting GPU resources actually utilize them to avoid resource wastage.
- **Monitoring Tools:** Use ClusterCockpit or `srun` and `nvidia-smi` to monitor GPU utilization.
- **User Awareness:** Educate users on the importance of proper resource allocation and utilization.

## Instructions for Future Reference
- **Monitoring GPU Utilization:**
  - Log into ClusterCockpit at [https://monitoring.nhr.fau.de/](https://monitoring.nhr.fau.de/).
  - Alternatively, attach to a running job with `srun --pty --overlap --jobid YOUR-JOBID bash` and use `nvidia-smi` to check GPU utilization.
- **Resource Allocation:** Only allocate GPU nodes if the code can make use of the GPU.

## Conclusion
Proper monitoring and resource allocation are crucial for efficient use of HPC resources. Users should be aware of the tools available to monitor their jobs and ensure that allocated resources are being utilized effectively.
```
---

### 2022061542000814_GPU%20access%20for%20master%20Thesis.md
# Ticket 2022061542000814

 # HPC Support Ticket: GPU Access for Master Thesis

## Keywords
- GPU access
- Master thesis
- HPC account
- FAU staff/student
- CIP pool
- SSH login
- Batch job
- TinyGPU
- Freikontingent Abschlussarbeiten

## Summary
A student required GPU access for their master thesis in cooperation with a company. The student had previously used the CIP pool and inquired about the procedure for accessing HPC resources.

## Root Cause
- The student needed GPU access for their master thesis.
- The student was unsure about the procedure for obtaining an HPC account and whether it was similar to the CIP pool.

## Solution
1. **HPC Account Application**:
   - The student was directed to the [HPC account application process](https://hpc.fau.de/systems-services/systems-documentation-instructions/getting-started/).
   - The form needs to be filled out and submitted to RRZE via the chair.

2. **GPU Access Procedure**:
   - The student needs to log in via SSH to the cluster frontend (`Woody.rrze` for GPU access).
   - A batch job should be submitted to TinyGPU, which will be processed once resources are available.

3. **Cost-Free Access**:
   - Despite the master thesis being in cooperation with a company, it was confirmed that the results are part of the student's academic work.
   - The student can select "Freikontingent Abschlussarbeiten" on the application form for cost-free access.

## General Learnings
- The process for obtaining an HPC account involves filling out a form and submitting it through the appropriate channels.
- GPU access requires logging in via SSH and submitting batch jobs.
- Students can apply for cost-free access for their thesis work, even if it involves cooperation with external entities, as long as the work is part of their academic requirements.

## References
- [HPC Account Application Process](https://hpc.fau.de/systems-services/systems-documentation-instructions/getting-started/)
- [HPC Support](mailto:support-hpc@fau.de)
- [HPC Documentation](https://hpc.fau.de/)
---

### 2024042442002608_Question%20about%20resource%20assigning%20-%20v100dd.md
# Ticket 2024042442002608

 ```markdown
# HPC Support Ticket: Resource Assigning Issue - v100dd

## Keywords
- Resource assigning
- v100dd
- A40 nodes
- AssocGrpGRES
- Throttling policy

## Problem
- User submitted a job using A40 nodes.
- Job status shows "AssocGrpGRES" indicating that GPUs are all in use.
- Available nodes are present, but the job is not being assigned resources.

## Root Cause
- The group v100dd has reached the throttling policy limit.
- The group currently has 96 GPUs assigned, which is 1/3 of all A40 nodes.
- Other groups also need access to resources, leading to the throttling policy being enforced.

## Solution
- The "AssocGrpGRES" status indicates that the throttling policy has been reached.
- Users need to wait until resources become available or consider adjusting their resource requests to fit within the policy limits.

## General Learning
- Understand the throttling policy and its impact on resource allocation.
- Be aware of the resource limits assigned to specific groups.
- Monitor resource usage to ensure fair distribution among all users and groups.
```
---

### 2022102142002525_ArchSup%20HPC%20Cluster.md
# Ticket 2022102142002525

 # HPC Support Ticket: ArchSup HPC Cluster

## Keywords
- Emmy Cluster
- Meggie Cluster
- Woody Cluster
- TinyGPU Cluster
- CUDA
- GPU
- HPC Accounts
- FAU

## Summary
The user requested access to Emmy and Meggie clusters for a course on Architectures of Supercomputing. The user was aware that Emmy was scheduled to be decommissioned but was still listed as available on the website. The user also needed access to Meggie for the first time and had previously used Emmy for a CAMA exercise.

## Root Cause
- Emmy cluster was decommissioned in September.
- The user required GPU capabilities for CUDA exercises, which were not available on Woody or Meggie clusters.

## Solution
- The HPC Admin informed the user that Emmy had been decommissioned and that the Woody cluster and Meggie were available as replacements.
- For GPU requirements, the HPC Admin suggested using the TinyGPU cluster, where all FAU HPC accounts are automatically enabled.

## General Learnings
- Always check the availability of clusters as they may be decommissioned or replaced.
- For GPU-specific tasks, ensure the cluster has the necessary hardware.
- FAU HPC accounts are automatically enabled on multiple clusters, including Woody, Meggie, and TinyGPU.

## Actions Taken
- The HPC Admin provided information about the decommissioning of Emmy and the availability of Woody and Meggie clusters.
- The HPC Admin suggested using the TinyGPU cluster for CUDA exercises.

## Follow-up
- No further follow-up was mentioned in the ticket conversation.
---

### 2021062242002506_Low%20utilization%20of%202nd%20A100%20GPU%20per%20job%20-%20iwi5026h.md
# Ticket 2021062242002506

 # HPC Support Ticket: Low Utilization of 2nd A100 GPU per Job

## Keywords
- GPU utilization
- A100 GPGPU
- Batch size
- Script modification
- System monitoring

## Problem Description
- **Root Cause**: User allocated a second A100 GPU per job but did not utilize it effectively due to a mismatch between batch size and the number of GPUs specified in the script.

## Conversation Summary
- **HPC Admin**: Notified the user about low utilization of the second A100 GPU, providing system monitoring graphs as evidence.
- **User**: Acknowledged the issue, explaining that the batch size was reduced but the number of GPUs in the script was not updated accordingly.
- **User**: Modified the script to use only one A100 GPU per task and canceled the existing scripts.

## Solution
- **User Action**: Modified the bash script to allocate only one A100 GPU per task.
- **HPC Admin**: Provided monitoring data to highlight the issue and guided the user to correct the script.

## General Learnings
- Always ensure that the number of GPUs allocated in the script matches the workload requirements.
- Regularly monitor GPU utilization to optimize resource allocation.
- Communicate effectively with users to resolve resource allocation issues promptly.
---

### 2022021042003328_Job%20auf%20Alex%20%5Biwb0003h%5D.md
# Ticket 2022021042003328

 # HPC Support Ticket: Job auf Alex [iwb0003h]

## Summary
- **Subject:** Job auf Alex [iwb0003h]
- **Issue:** Job (25937) shows no GPU utilization for hours.
- **User:** Simon Bachhuber
- **HPC Admins:** Anna Kahler, Johannes Veh

## Keywords
- GPU utilization
- Job monitoring
- nvidia-smi
- Python code
- Job timeout
- System monitoring

## Problem Description
- The user's job (25937) on Alex showed no GPU utilization for several hours.
- The job was started on 09.02. at 20:20 with 4x A40 GPUs and was canceled on 10.02. at 19:20.
- The user suspects an issue with the interaction between their code and the GPUs.
- GPUs disappeared from the system around 10:58, and the job continued running without performing any tasks.

## Diagnostic Steps
- HPC Admin provided a screenshot from the system monitoring tool showing the allocated GPUs.
- The user shared a screenshot from their external monitoring tool, indicating the GPUs disappeared around 10:58.
- The user mentioned that CPU and memory usage increased around 10:01, but the reason was unclear.
- The `run.sh.o` file did not show any relevant output.

## Further Investigation
- HPC Admin requested the user to restart the job and provide the new job ID for live monitoring.
- nvidia-smi showed that processes were still allocated on the GPUs but were not performing any tasks.

## Root Cause
- The root cause of the problem was not clearly identified. It could be related to the interaction between the user's code and the GPUs or an issue with the system.

## Solution
- No solution was found in the provided conversation. Further investigation and live monitoring are required to identify the root cause and resolve the issue.

## Next Steps
- Restart the job and provide the new job ID for live monitoring.
- Continue to investigate the interaction between the user's code and the GPUs.
- Monitor the job using nvidia-smi and other system monitoring tools to identify any anomalies.

## Notes
- The user's jobs typically end around hour 20 and save results.
- The job would have timed out if not canceled by the user.
- The issue persisted in subsequent jobs, with GPUs showing no utilization.
---

### 2024011642002147_Job%20on%20Alex%20does%20not%20use%20allocated%20GPU%20%5Bb185cb18%5D.md
# Ticket 2024011642002147

 ```markdown
# HPC-Support Ticket: Job on Alex does not use allocated GPU

## Keywords
- GPU utilization
- Job monitoring
- ClusterCockpit
- srun
- nvidia-smi

## Summary
A user's job on Alex was using only one of the three allocated GPUs. The HPC Admin notified the user and provided instructions on how to monitor GPU utilization.

## Root Cause
The job was not efficiently utilizing the allocated GPU resources.

## Steps Taken
1. **Notification**: HPC Admin informed the user about the underutilization of GPUs.
2. **Monitoring Instructions**: Provided instructions to monitor GPU utilization using ClusterCockpit and `nvidia-smi`.
3. **User Response**: The user acknowledged the issue and planned to fix it.

## Solution
- **Monitoring Tools**: Use ClusterCockpit at [https://monitoring.nhr.fau.de/](https://monitoring.nhr.fau.de/) to view GPU utilization.
- **Attach to Job**: Use `srun --pty --overlap --jobid YOUR-JOBID bash` to attach to the running job and run `nvidia-smi` to check GPU utilization.

## General Learning
- **Efficient Resource Utilization**: Ensure jobs are configured to use all allocated resources.
- **Monitoring**: Use available monitoring tools to track resource usage.
- **Communication**: Promptly notify users about resource underutilization and provide guidance on monitoring and troubleshooting.
```
---

### 2024011142001102_Tier3-Access-Alex%20%22Noah%20Maul%22%20_%20iwi5008h.md
# Ticket 2024011142001102

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject
Tier3-Access-Alex "Noah Maul" / iwi5008h

## Keywords
- Tier3 Access
- Alex Cluster
- GPU-hours
- NHR Proposal
- Compute Time
- GPGPU
- Nvidia A40
- Python
- CUDA
- PyTorch
- Computational Fluid Dynamics
- Deep Learning
- Neural Networks
- Surrogate Model
- Blood Flow Simulations

## Summary
A user requested access to the Alex cluster for computational fluid dynamics and deep learning applications, requiring a significant amount of GPU-hours. The HPC Admin enabled the account but advised that the requested GPU-hours might not be guaranteed from the free Tier3 basic service. The user was recommended to apply for compute time via an NHR proposal.

## Root Cause of the Problem
The user's request for a large number of GPU-hours (7200 hours) might not be fully satisfied by the free Tier3 basic service.

## Solution
The HPC Admin suggested applying for compute time via an NHR proposal to ensure the requested compute time is available.

## What Can Be Learned
- **Account Activation**: HPC Admins can enable user accounts on specific clusters.
- **Resource Allocation**: Free Tier3 basic service may not guarantee the requested compute time.
- **NHR Proposal**: Users should apply for compute time via an NHR proposal to ensure they get the required resources.
- **Software Requirements**: Users should specify the software they need (e.g., Python, CUDA, PyTorch).
- **Application Details**: Users should provide details about their application, expected results, and any additional remarks.

## Recommendations for Support Employees
- **Account Activation**: Ensure user accounts are enabled on the requested cluster.
- **Resource Allocation**: Inform users about the limitations of the free Tier3 basic service.
- **NHR Proposal**: Guide users to apply for compute time via an NHR proposal if their resource requirements are high.
- **Documentation**: Provide links to relevant documentation and application rules for NHR proposals.
```
---

### 2025021242001759_sbatch%20number-992955.md
# Ticket 2025021242001759

 # HPC Support Ticket Analysis: sbatch number-992955

## Keywords
- CUDA out of memory
- PyTorch
- GPU allocation
- Slurm script
- VRAM
- Data transfer

## Problem
- **Root Cause**: The user's job script resulted in a `torch.OutOfMemoryError` due to insufficient GPU memory (VRAM). The GPU has a total capacity of 9.67 GiB, with 8.27 GiB free, but the job required more memory than available.

## Solution and Recommendations
- **Immediate Solution**: Not explicitly provided, but the admin suggested checking the data sample size and considering a GPU with more VRAM.
- **Recommendations**:
  - **Check Data Sample Size**: Ensure that the data sample size is not excessively large.
  - **Use Higher VRAM GPU**: Consider using GPUs with more VRAM, such as V100 (32 GB) or A100 (40 GB).
  - **Optimize Slurm Script**:
    - Use `srun` before `python3 <script>` to ensure proper GPU utilization.
    - Verify if the library supports multiple GPUs.
  - **Data Transfer**: Transfer data to the node using a `.tar` file to reduce runtime and prevent slowdowns.

## Additional Information
- **Monitoring Links**:
  - [Job 12745175](https://monitoring.nhr.fau.de/monitoring/job/12745175)
  - [Job 12740090](https://monitoring.nhr.fau.de/monitoring/job/12740090)
  - [Job 12734158](https://monitoring.nhr.fau.de/monitoring/job/12734158)
- **Documentation**: [Data Staging](https://doc.nhr.fau.de/data/staging/)

## General Learnings
- **Memory Management**: Understanding and managing GPU memory is crucial for jobs involving deep learning frameworks like PyTorch.
- **Efficient Data Handling**: Transferring data efficiently to the node can improve job performance and reduce overall runtime.
- **Slurm Script Optimization**: Properly configuring Slurm scripts ensures optimal resource utilization and job efficiency.

This report provides insights into common issues related to GPU memory management and offers solutions to optimize job scripts for better performance on HPC systems.
---

### 2022032642000013_GPU-Restriktionen%20Alex.md
# Ticket 2022032642000013

 ### HPC-Support Ticket Conversation: GPU-Restriktionen Alex

**User:**
- Requested more than 24 A40 GPUs on Alex.
- Provided `squeue` output showing pending jobs with `AssocGrpGRES` reason.

**HPC Admin:**
- Increased the user's limit.
- Noted that there were no pending jobs in the queue earlier in the day.

**User:**
- Thanked for the increased limit.
- Mentioned a pipeline with 37k videos, indicating the need for a higher limit.
- Asked about viewing system utilization, as the customer area showed no data.

**HPC Admin:**
- Explained that there is no web page for utilization data due to FAU owning only 25% of Alex.
- Noted that A40 GPUs were fully utilized, but A100 GPUs were available.

**User:**
- Requested clarification on how to request any available GPU type.
- Provided current job submission script with specific GPU type and partition.

**HPC Admin:**
- Clarified that GPUs must be explicitly requested with their type in their respective partitions.
- Mentioned that there is currently no option to request any available GPU type.

**User:**
- Found a solution by not specifying a partition and requesting only `gpu`.
- Received both A40 and A100 nodes.

**HPC Admin:**
- Explained that not specifying a partition defaults to `a40`.
- Identified a bug in the submit filter that accepts `--gres=gpu`.
- Mentioned that jobs were manually moved to the `a100` partition.

**User:**
- Asked about the scheduler's ability to handle jobs for different GPU types in the queue.

**HPC Admin:**
- Clarified that the scheduler only considers the next X jobs, which may not include jobs for different GPU types further back in the queue.
- Suggested submitting jobs in a ratio reflecting the available GPU types.

**Key Learnings:**
- Users can request more than 24 A40 GPUs if capacity allows.
- Utilization data is not available due to FAU owning only 25% of Alex.
- GPUs must be explicitly requested with their type in their respective partitions.
- Not specifying a partition defaults to `a40`, but this is a bug in the submit filter.
- The scheduler only considers the next X jobs, which may not include jobs for different GPU types further back in the queue.
- Users should submit jobs in a ratio reflecting the available GPU types to ensure proper scheduling.

**Solution:**
- To request any available GPU type, do not specify a partition and request only `gpu`.
- Ensure jobs are submitted in a ratio reflecting the available GPU types to avoid scheduling issues.
---

### 2022012742000801_Zugang%20zum%20Testcluster.md
# Ticket 2022012742000801

 ```markdown
# HPC-Support Ticket Conversation: Access to Test Cluster

## Keywords
- Test cluster
- Account activation
- TensorFlow
- PyTorch
- Deep learning
- GPU
- Hardware requirements

## Summary
- **User Request**: The user requested access to the test cluster for their account to test various GPUs for deep learning tasks using TensorFlow and PyTorch.
- **HPC Admin Response**: The HPC admin granted access to the test cluster for the user's account.

## Root Cause
- The user needed access to the test cluster to experiment with different GPUs for deep learning model training.

## Solution
- The HPC admin activated the user's account for the test cluster.

## General Learnings
- Users may request access to the test cluster for experimental purposes, especially for tasks requiring specific hardware like GPUs.
- HPC admins can grant access to the test cluster upon user request, ensuring users are aware of potential job interruptions.
```
---

### 2022011042000396_geringe%20GPU-Auslastung%20%28iwi5035h%29.md
# Ticket 2022011042000396

 # HPC Support Ticket: Low GPU Utilization

## Keywords
- Low GPU utilization
- GPU memory usage
- Batch size
- Job performance
- System monitoring
- `nvidia-smi`

## Summary
The user's jobs were utilizing GPU memory fully but showed very low GPU utilization (<3%, often 0%) as reported by `nvidia-smi`. The issue persisted for several weeks despite attempts to address it.

## Root Cause
- The root cause was suspected to be a small batch size used in the jobs, which led to inefficient GPU usage.

## Solution
- The user was advised to investigate and increase the batch size to improve job performance and GPU utilization.
- The user was eventually asked to stop the processes until the issue was fixed, as the low utilization was wasting GPU resources.

## Lessons Learned
- Regularly monitor job performance and GPU utilization to ensure efficient resource usage.
- Small batch sizes can lead to low GPU utilization and should be adjusted accordingly.
- Addressing low GPU utilization can result in significant computational time savings and improved throughput.

## Follow-up
- The user should report back once the issue is resolved and GPU utilization improves.
- HPC Admins should continue to monitor the jobs to ensure the issue does not persist.
---

### 2023111642003094_Unresponsive%20SSH%20Access%20to%20frontend%20node%20for%20TinyGPU.md
# Ticket 2023111642003094

 # HPC Support Ticket: Unresponsive SSH Access to Frontend Node for TinyGPU

## Keywords
- SSH access issue
- Frontend node
- TinyGPU cluster
- Resource usage
- Memory and swap usage
- htop command
- Old processes
- Reboot
- Kernel update

## Problem Description
- **Issue**: Recurring SSH access problems to the TinyGPU cluster frontend node.
- **Symptoms**: Random intervals of unsuccessful SSH connections with the error message "Connection closed."
- **Root Cause**: Heavy memory and swap usage by certain processes, leading to access difficulties.

## Diagnostic Steps
- User analyzed resource usage using the `htop` command and provided a screenshot.
- HPC Admins attempted to purge old processes.

## Solution
- **Immediate Action**: Purging old processes resolved the immediate issue, allowing successful SSH login.
- **Further Action**: A reboot of the system was planned to apply a new kernel update, even though the system was not affected by the current Intel-Microcode problem (Reptar).

## Lessons Learned
- High resource usage (memory and swap) can lead to SSH access issues.
- Purging old processes can temporarily resolve resource-related issues.
- Regular system reboots and kernel updates are essential for maintaining system stability.

## Next Steps
- Monitor resource usage regularly to prevent similar issues.
- Consider implementing resource limits or quotas to manage heavy usage by specific processes.
- Ensure timely application of kernel updates and system reboots.
---

### 2024102542001481_Jobs%20on%20Alex%20with%20low%20GPU%20utilization%20%5Bb245da11%5D.md
# Ticket 2024102542001481

 ```markdown
# HPC Support Ticket: Jobs with Low GPU Utilization

## Keywords
- Low GPU utilization
- Bundled simulations
- Slurm script bug
- Job cancellation

## Summary
A user's jobs on the HPC system "Alex" were experiencing low GPU utilization due to some processes finishing early. The user had bundled multiple simulations together, leading to idle GPUs.

## Root Cause
- The user's Slurm script had a bug that caused some processes to finish early, resulting in low GPU utilization.

## Solution
- The user acknowledged the issue and decided to cancel all queuing jobs until the bug in the Slurm script is resolved.

## Lessons Learned
- Bundling multiple simulations together can lead to inefficient resource utilization if some processes finish early.
- It is preferable to run simulations as individual jobs to avoid leaving GPUs idle.
- Users should regularly monitor their jobs and scripts to identify and resolve issues promptly.

## Actions Taken
- The HPC Admin notified the user about the low GPU utilization issue.
- The user canceled all queuing jobs to address the bug in the Slurm script.

## Recommendations
- Encourage users to run simulations as individual jobs to maximize resource utilization.
- Provide guidance on monitoring and debugging Slurm scripts to help users identify and fix issues.
```
---

### 2021070542003698_TinyGPU%20-%20down%3F.md
# Ticket 2021070542003698

 ```markdown
# HPC-Support Ticket: TinyGPU - down?

## Keywords
- TinyGPU Cluster
- Verbindungsprobleme
- Filesystem
- Node Status
- Available Resources

## Problem Description
- User reported connectivity issues and slow response times on the TinyGPU cluster from 14:30 to 15:30.
- The status page indicated no available nodes despite showing free nodes in the node status.
- No information about the issue was available in login messages or on the RRZE/HPC homepage.

## Root Cause
- Problems with the filesystem caused the TinyGPU cluster to slow down or become unavailable.

## Solution
- The filesystem issue was resolved, and jobs started running again.

## Lessons Learned
- Filesystem issues can significantly impact the performance and availability of HPC clusters.
- It is important to check the filesystem health when diagnosing connectivity and performance issues.
- Ensure that status pages and login messages are updated promptly to reflect current issues and resolutions.

## Actions Taken
- HPC Admins identified and resolved the filesystem issue.
- The user was informed that the problem was fixed and jobs were running again.

## Closure
- The ticket was closed after the issue was resolved and the user was notified.
```
---

### 2023070442000742_Job%20on%20Alex%20does%20not%20use%20second%20GPU%20%5Bbctc33%5D.md
# Ticket 2023070442000742

 # HPC Support Ticket: Job on Alex does not use second GPU

## Keywords
- GPU utilization
- Job monitoring
- `nvidia-smi`
- `srun`
- ClusterCockpit

## Issue
- User's job requesting two GPUs on Alex is only utilizing one GPU.

## Diagnosis
- HPC Admin identified the issue through the monitoring system and notified the user.
- User can verify GPU utilization by attaching to the running job using `srun --pty --overlap --jobid YOUR-JOBID bash` and then running `nvidia-smi`.

## Monitoring Tools
- ClusterCockpit monitoring: [http://monitoring.nhr.fau.de/]

## Solution
- User should check the job configuration and ensure that the application is correctly set up to utilize multiple GPUs.
- If the issue persists, further investigation into the job script and application settings is required.

## Additional Information
- For further assistance, users can contact the HPC support team via email.

## Contact
- HPC Support: support-hpc@fau.de
- Website: [https://hpc.fau.de/]
---

### 2022050942002701_Node-local%20storage.md
# Ticket 2022050942002701

 # Node-Local Storage Issue on TinyGPU Cluster

## Keywords
- Node-local storage
- TinyGPU cluster
- Training data caching
- "No space on device left" error
- Memory usage tracking

## Problem Description
- **User Issue:** Training data caching on node-local storage causes intermittent crashes with the error "No space on device left."
- **Root Cause:** Insufficient node-local SSD storage due to shared usage among multiple jobs.

## Cluster Details
- **Cluster:** TinyGPU (Trier3)
- **Node-local Storage:** 0.8 TB to 5.8 TB SSD per node, shared among users.
- **Directories:**
  - `$TMPDIR`: Job-specific, deleted at job end.
  - `/scratch`, `/scratchssd`, `/tmp`: User-specific, deleted when no jobs are running on the node.

## Solution and Recommendations
- **Current Status:** No fixed limits on SSD storage to accommodate varying usage patterns.
- **Recommendation:** Monitor SSD usage and consider requesting larger SSDs if necessary.
- **No Direct Solution:** Users cannot prevent "No space on device left" errors without additional storage.

## Additional Information
- **SSD Usage:** Most nodes have low SSD usage (<10%), with a few nodes having higher usage (up to 23%).
- **Contact:** For further assistance, contact the HPC support team.

## Conclusion
- **Summary:** Node-local storage limitations can cause training data caching issues. Monitoring and potentially requesting additional storage are recommended.

---

This documentation aims to assist HPC support employees in understanding and resolving similar node-local storage issues in the TinyGPU cluster.
---

### 2024101842001896_Tier3-Access-Alex%20%22Huang%2C%20Weilong%22%20_%20iwal194h.md
# Ticket 2024101842001896

 # HPC Support Ticket Analysis

## Keywords
- HPC Account Activation
- Alex Cluster
- GPGPU
- Nvidia A100
- Python
- Miniconda
- Deep Learning
- Microphone Array Processing

## Summary
- **User Request**: Access to the GPGPU cluster 'Alex' for deep learning research on microphone array processing.
- **Required Software**: Python, Miniconda, and necessary Python packages.
- **Expected Outcome**: Improved results from deep learning compared to conventional methods.

## Actions Taken
- **HPC Admin**: Enabled the user's HPC account on Alex.

## Lessons Learned
- **Account Activation**: Ensure that user accounts are enabled promptly upon request.
- **Software Requirements**: Be prepared to support common software tools like Python and Miniconda for deep learning projects.
- **User Communication**: Maintain clear and timely communication with users regarding their account status and access to resources.

## Root Cause
- User needed access to the Alex cluster for deep learning research.

## Solution
- HPC Admin enabled the user's account on the Alex cluster.

## Documentation for Future Reference
- **Account Activation Process**: Ensure that the process for enabling user accounts is well-documented and followed consistently.
- **Software Support**: Maintain up-to-date documentation on supported software and how to install/configure it on the cluster.
- **User Onboarding**: Provide clear instructions and support for new users to help them get started with their research projects.

---

This documentation can be used as a reference for future support tickets related to account activation and software support for deep learning projects on the Alex cluster.
---

### 2022041242003526_massive%20IO%20of%20jobs%20on%20TinyGPU%20-%20bctc33.md
# Ticket 2022041242003526

 ```markdown
# HPC Support Ticket: Massive IO of Jobs on TinyGPU

## Keywords
- Massive IO
- TinyGPU
- Job termination
- Excessive IO
- /home/woody

## Summary
A user's jobs on TinyGPU were terminated due to excessive IO operations on the `/home/woody` directory, which impacted other users.

## Root Cause
- Excessive IO operations by the user's jobs on the `/home/woody` directory.

## Solution
- The jobs were killed to prevent further disruption to other users.

## Lessons Learned
- Monitor job IO operations to prevent excessive usage that impacts other users.
- Consider setting IO limits or quotas to manage resource usage effectively.

## Actions Taken
- HPC Admin notified the user about the issue and the action taken (job termination).

## Next Steps
- Users should be educated on best practices for managing IO operations.
- Implement monitoring and alerting for excessive IO usage to proactively manage such issues.
```
---

### 2024071842002409_Tier3-Access-Alex%20%22Marc%20Windsheimer%22%20_%20iwnt103h.md
# Ticket 2024071842002409

 ```markdown
# HPC Support Ticket Conversation Analysis

## Subject: Tier3-Access-Alex "Marc Windsheimer" / iwnt103h

### Keywords:
- GPU hours
- NHR application
- Account activation
- Resource request
- Software requirements
- Neural network training

### Summary:
- **User Request:** Access to GPGPU cluster 'Alex' with 5000 GPU hours for training neural networks.
- **Required Software:** Anaconda, Python, PyTorch.
- **Application:** Training of neural network-based video compression networks for machine vision tasks.
- **Expected Results:** Optimized networks for video compression.

### Root Cause of the Problem:
- User requested a significant amount of GPU hours (5000), which is typically handled through an NHR application.

### Solution:
- **HPC Admin:** Informed the user that the requested resources are substantial and require an NHR application.
- **Action Taken:** Activated the user's account on 'Alex' despite the need for an NHR application.

### General Learnings:
- Large resource requests (e.g., 5000 GPU hours) should be directed to the NHR application process.
- Accounts can be activated pending the submission of an NHR application.
- Ensure users are aware of the application process for substantial resource requests.

### Relevant Links:
- [NHR Application](https://doc.nhr.fau.de/nhr-application/)
- [NHR@FAU](https://hpc.fau.de/)
```
---

### 2020030142000402_Request%20for%20an%20HPC%20account.md
# Ticket 2020030142000402

 # HPC Support Ticket: Request for an HPC Account

## Keywords
- HPC account request
- Master thesis
- Deep neural networks
- GPU computations
- NVIDIA
- Form submission
- RRZE Kontaktperson
- Documentation

## Summary
A user requested an HPC account for training deep neural networks involving GPU-based computations (8-12 GB NVIDIA) for their master thesis.

## Root Cause
The user requires access to HPC resources for GPU-based computations.

## Solution
1. **Form Submission**: The user was instructed to fill out the HPC account request form and get it signed by the RRZE Kontaktperson of their chair.
2. **Submission Methods**: The form can be submitted by mail to `rrze-zentrale@fau.de` or brought to the RRZE Servicetheke.
3. **Documentation**:
   - General HPC documentation: [Getting Started](https://www.anleitungen.rrze.fau.de/hpc/getting-started/)
   - GPU systems documentation: [Tinyx Clusters](https://www.anleitungen.rrze.fau.de/hpc/tinyx-clusters/#collapse_1)

## General Learnings
- Users need to submit a signed form for HPC account requests.
- Documentation is available for getting started with HPC systems and specific GPU systems.
- Access to some systems may be restricted due to funding by specific groups.

## Next Steps
- Ensure the user submits the signed form.
- Provide access to available systems that meet the user's requirements.
---

### 2023052542000662_alex%20not%20allocate%20gpu.md
# Ticket 2023052542000662

 ```markdown
# HPC Support Ticket: Unable to Allocate GPU on Alex

## Keywords
- GPU allocation
- Resource limits
- Job scheduling
- AssocGrpGRES

## Problem Description
- User unable to allocate GPU on Alex since the previous night.
- User inquires if the system is under maintenance or if there are account-specific issues.

## Root Cause
- The user's group has reached the maximum limit of 96 GPUs that can be used simultaneously.

## Solution
- The job will start as soon as other jobs from the user's coworkers finish and free up resources.

## What to Learn
- Check if the user's group has reached the maximum resource limit (e.g., GPUs).
- Inform the user about the current resource usage and the need to wait for resources to become available.
- Provide reassurance that the job will start once resources are freed up.

## Additional Notes
- The HPC Admin responded promptly, explaining the resource limit and the expected resolution.
- No maintenance or account-specific issues were identified.
```
---

### 2024020942001696_Ressourcen%20f%C3%83%C2%BCr%20Masterarbeit.md
# Ticket 2024020942001696

 # HPC Support Ticket: Resources for Master's Thesis

## Keywords
- Master's Thesis
- Deep Learning
- HPC Cluster
- Resource Allocation
- TinyGPU
- Job Size
- Rechenzeit
- Speicherplatz

## Problem
A master's student working on deep learning networks requires HPC resources for training but is unsure how to fill out the resource request form, specifically the fields for "HPC-Zielsysteme," "typische Jobgröße insges.," "benötigte Rechenzeit," and "benötigter Speicherplatz."

## Solution
- **HPC-Zielsysteme**: TinyGPU (assuming the student is working on machine learning tasks)
- **Typische Jobgröße insges.**: 1-8 GPUs (as per TinyGPU capabilities)
- **Benötigte Rechenzeit**: Typically less than 1000 hours on the GPU (depends on the specific workload)
- **Benötigter Speicherplatz**: Each account has ~1TB of storage by default; specify if more is needed

## General Learnings
- Master's students can use HPC clusters for their research.
- The resource request form requires specific details about the intended workload.
- Consulting with the thesis supervisor can help in determining the required resources.
- TinyGPU is suitable for machine learning tasks and supports job sizes of 1-8 GPUs.
- Default storage allocation is ~1TB per account.

## Next Steps
- The student should consult with their supervisor to determine the exact resource requirements.
- Complete the resource request form with the provided guidelines.
- Submit the form for further processing by the HPC support team.

## References
- [FAU HPC Support](mailto:support-hpc@fau.de)
- [FAU HPC Website](https://hpc.fau.de/)
---

### 2022032242002626_Job%20on%20TinyGPU%20only%20uses%20one%20GPU%20%5Biwi5067h%5D.md
# Ticket 2022032242002626

 # HPC Support Ticket: Job on TinyGPU Only Uses One GPU

## Keywords
- TinyGPU
- GPU allocation
- Resource usage
- Job optimization
- Monitoring system

## Summary
A user's job on the TinyGPU cluster was allocated two GPUs but only utilized one, leading to inefficient resource usage.

## Root Cause
- The user's job configuration did not properly utilize the allocated GPUs.

## Solution
- Ensure that the job script is configured to use all allocated GPUs.
- Monitor resource usage to verify that all allocated GPUs are being utilized.

## Lessons Learned
- Always allocate only the number of GPUs that your job can actually use.
- Regularly monitor job performance to ensure efficient resource utilization.
- Contact HPC support for assistance with job configuration and resource management.

## Actions Taken
- HPC Admin notified the user about the inefficient resource usage.
- A screenshot from the monitoring system was provided to illustrate the issue.
- The user was advised to contact HPC support for further assistance if needed.

## Follow-Up
- Ensure that the user understands how to properly configure their job to utilize all allocated GPUs.
- Continue monitoring job performance to prevent similar issues in the future.

## References
- HPC Services, Friedrich-Alexander-Universitaet Erlangen-Nuernberg
- Regionales RechenZentrum Erlangen (RRZE)
- [HPC Support Email](mailto:support-hpc@fau.de)
- [HPC Website](http://hpc.fau.de/)
---

### 2022060142001296_Job%20auf%20TinyGPU%20nutzen%20nach%20Anfangsphase%20die%20GPU%20nicht%20mehr%20%5Biwso035h%5D.md
# Ticket 2022060142001296

 ```markdown
# HPC-Support Ticket: GPU Utilization Issue on TinyGPU

## Keywords
- GPU utilization
- TinyGPU
- Job script
- Slurm script
- Output files
- `nvidia-smi`
- Monitoring system
- Resource allocation

## Summary
A user reported that their jobs on TinyGPU stopped utilizing the GPU after an initial phase, causing the processes to halt and eventually time out.

## Problem Description
- **User Observation**: Jobs on TinyGPU stopped using the GPU after an initial phase.
- **Monitoring System**: Green-highlighted graphs in the monitoring system indicated the issue.
- **User Actions**: The user was unable to reproduce the issue when restarting the process individually or from an interactive node.

## HPC Admin Actions
1. **Initial Notification**: Informed the user about the issue and provided a screenshot from the monitoring system.
2. **Troubleshooting Steps**:
   - Suggested using `ssh` to log into the node and `nvidia-smi` to check GPU utilization.
   - Provided a link to documentation on working with NVIDIA GPUs.
3. **Request for Additional Information**:
   - Requested the user to send the job script, Slurm script, and all related output files for further investigation.

## Root Cause
- The exact cause of the issue was not identified in the initial conversation.
- The user's jobs were not consistently utilizing the GPU, leading to resource wastage.

## Solution
- The user was advised to send the job script, Slurm script, and output files for further analysis.
- No specific solution was provided in the initial conversation, but the HPC Admin offered to investigate further with the provided information.

## General Learnings
- **Resource Management**: Ensure that GPU nodes are only requested when the code can utilize the GPUs to avoid resource wastage.
- **Troubleshooting**: Use `nvidia-smi` to monitor GPU utilization and check for issues.
- **Documentation**: Refer to the provided documentation for working with NVIDIA GPUs.
- **Support**: Provide job scripts and output files for detailed troubleshooting when encountering issues.
```
---

### 2021092942002864_FES%20Error%20Analysis%20Problem%20gel%C3%83%C2%B6st.md
# Ticket 2021092942002864

 # HPC Support Ticket Analysis

## Subject
FES Error Analysis Problem gelöst

## Keywords
- PLUMED Tutorial
- Error Analysis
- Multiple Walker Metadynamics
- MD Simulations
- qstat
- tinygpu
- woody
- Stromausfall (Power Outage)
- Checkpoint

## Problem
- User was unable to see their MD simulations running on `tinygpu` using `qstat.tinygpu -u bcpc000h` when logged into `woody`.
- Jobs were requested with `nodes=1:ppn=4:smt:rtx2080ti`.

## Root Cause
- Power outage due to electrical work in the building caused the jobs to terminate unexpectedly.

## Solution
- User restarted the jobs from the last checkpoint.

## General Learnings
- Power outages can cause unexpected job terminations.
- Checkpoints are crucial for resuming jobs after unexpected terminations.
- Monitoring tools like `qstat` may not show jobs if they have been terminated unexpectedly.
- Communication about infrastructure issues (like power outages) is important for user awareness.

## References
- [PLUMED Tutorial](https://www.plumed.org/doc-v2.6/user-doc/html/master-_i_s_d_d-2.html)
---

### 2025031842004065_Tier3-Access-Alex%20%22Daoqi%20Jin%22%20_%20iwb9102h.md
# Ticket 2025031842004065

 # HPC Support Ticket Analysis

## Keywords
- **Tier3 Access**
- **Alex Cluster**
- **A100 GPUs**
- **Memory Requirements**
- **Model Testing**
- **Surgical Language Recognition**

## Summary
- **User Request:** Access to Alex cluster for testing large models with more than 32B parameters.
- **Issue:** TinyGPU A100 GPUs have only 40GB memory, insufficient for running 32B parameter models.
- **Solution:** Access granted to Alex cluster with A100 GPUs (80GB memory).

## Detailed Conversation
1. **Initial Request:**
   - User requested access to Alex cluster for testing large models.
   - Required software: Python.
   - Application: Surgical language recognition.
   - Expected results: Improved accuracy in surgical stage recognition.

2. **HPC Admin Response:**
   - Requested justification for using Alex cluster.
   - Suggested using TinyGPU for 400h compute time.

3. **User Clarification:**
   - Explained the need for A100 GPUs with 80GB memory to run models with more than 32B parameters.
   - TinyGPU A100 GPUs with 40GB memory are insufficient.

4. **HPC Admin Approval:**
   - Granted access to Alex cluster.

## Lessons Learned
- **Memory Requirements:** Ensure that the GPU memory meets the model's requirements.
- **Cluster Selection:** Choose the appropriate cluster based on hardware specifications.
- **Justification:** Provide clear justification for resource requests to expedite approval.

## Root Cause
- Insufficient GPU memory on TinyGPU for running large models.

## Solution
- Access granted to Alex cluster with adequate GPU memory.
---

### 2021102042000772_FEP%20Job%20canceln.md
# Ticket 2021102042000772

 # HPC Support Ticket: FEP Job Cancellation

## Keywords
- FEP Job
- Job Cancellation
- Master Job
- CPU Job
- TinyGPU Jobs
- qstat
- qdel
- Process Termination

## Problem Description
- User started an FEP job that was running incorrectly.
- User could only stop jobs on tinygpus but not the master job on the CPU.
- The master job kept submitting new jobs to tinygpus.
- Attempts to delete the job folder were unsuccessful.

## Root Cause
- The master job on the CPU was not properly terminated, leading to continuous submission of new jobs to tinygpus.

## Solution
1. **Identify the Job**: Use `qstat` without `.tinygpu` on the relevant node (e.g., woody3) to identify the job ID.
2. **Cancel the Job**: Use `qdel JOBID` to cancel the identified job.
3. **Terminate All Processes**: If the job continues to run, terminate all related processes on the node (e.g., woody3).

## Steps Taken by HPC Admins
1. Identified the job using `qstat` and cancelled it using `qdel`.
2. Terminated all related processes on the node to ensure the job was fully stopped.

## Outcome
- The job was successfully cancelled, and no new jobs were submitted to tinygpus.
- The user was able to start a new job without issues.

## General Learning
- Ensure all related processes are terminated when cancelling a job to prevent continuous job submissions.
- Use `qstat` and `qdel` commands effectively to manage job submissions and cancellations.

## Documentation for Future Reference
- **Command to Identify Jobs**: `qstat`
- **Command to Cancel Jobs**: `qdel JOBID`
- **Terminate Related Processes**: Ensure all processes related to the job are terminated to prevent further job submissions.

This documentation can be used to resolve similar issues in the future.
---

### 2024061142004369_Tier3-Access-Alex%20%22Luis%20Carlos%20Rivera%20M%22%20_%20iwi5150h.md
# Ticket 2024061142004369

 # HPC Support Ticket Analysis

## Subject
Tier3-Access-Alex "Luis Carlos Rivera M" / iwi5150h

## Keywords
- HPC Account Activation
- Alex Cluster
- Nvidia A100 GPUs
- Pytorch
- PhD Work

## Summary
- **User Request**: Access to the GPGPU cluster 'Alex' with Nvidia A100 GPUs for running jobs requiring high memory and powerful GPUs.
- **Software Needed**: Pytorch
- **Expected Outcome**: PhD Work

## Conversation Highlights
- **HPC Admin**: Confirmed the activation of the user's HPC account on Alex.
- **User**: Requested access to the Alex cluster for running experiments on large datasets.

## Root Cause of the Problem
- User needed access to the Alex cluster for their research work.

## Solution
- **HPC Admin**: Enabled the user's HPC account on Alex.

## What Can Be Learned
- **Account Activation**: HPC Admins can enable user accounts on specific clusters upon request.
- **Resource Allocation**: Users can request access to specific resources like GPUs for their research needs.
- **Software Requirements**: Users should specify the software they need for their work, such as Pytorch.

## Next Steps
- Ensure the user has access to the required software (Pytorch) on the Alex cluster.
- Monitor the user's resource usage to ensure compliance with the allocated GPU-hours.

---

This documentation can be used as a reference for similar account activation requests and resource allocation processes.
---

### 2022031142001853_Jobs%20auf%20TinyGPU%20ohne%20GPU-Nutzung%20%5Biwal079h%5D.md
# Ticket 2022031142001853

 ```markdown
# HPC Support Ticket: Jobs auf TinyGPU ohne GPU-Nutzung

## Keywords
- TinyGPU
- GPU utilization
- Job monitoring
- Code optimization

## Problem Description
- User has jobs running on TinyGPU with minimal or no GPU utilization.
- HPC Admin noticed this through monitoring and alerted the user.

## Root Cause
- The user's code is not efficiently utilizing the allocated GPU resources.

## Solution
- The user was advised to check and optimize their code to better utilize the GPU.
- No further issues were reported after the initial notification.

## Lessons Learned
- Regular monitoring of job performance is crucial for efficient resource utilization.
- Users should be informed about the importance of optimizing their code for GPU usage.
- Proactive communication from HPC Admins can help in resolving resource inefficiencies.

## Actions Taken
- HPC Admin sent a notification to the user with a screenshot of the monitoring data.
- The user was advised to review and optimize their code.
- The ticket was closed as no further issues were observed.
```
---

### 2021060842002935_Job%20running%20time%20limitation%20on%20HPC%20servers.md
# Ticket 2021060842002935

 # HPC Support Ticket: Job Running Time Limitation on HPC Servers

## Keywords
- Slurm
- GPU allocation
- Walltime limit
- Partition specification
- Batch script errors

## Problem Description
- User encountered errors when trying to allocate 4 GPUs and set the GPU model in batch scripts for Slurm on TinyGPU.
- User received errors when attempting to submit a batch script for Slurm to run for 10 days on TinyGPU.
- User tried to set the partition to "devel" to avoid restrictions but encountered errors.

## Root Cause
- Incorrect specification of GPU resources in the batch script.
- Exceeding the maximum allowed walltime for the partition.
- Attempting to use an invalid partition name.

## Solution
- For Slurm nodes with RTX3080, specify the option `--gres=gpu:4` to allocate 4 GPUs.
- For A100 GPUs, use `--gres=gpu:a100:4 --partition=a100`.
- All GPU nodes only accept jobs with a maximum runtime of 24 hours.
- The "devel" partition is not available on TinyGPU.
- Ensure the batch script does not request more resources than intended. For example, avoid specifying `--tasks-per-node` and `--cpus-per-task` that lead to excessive resource allocation.

## Example Batch Script
```bash
#SBATCH --time=24:00:00
#SBATCH --job-name=GazeNet
#SBATCH -o ./gaze_net.%j.out
#SBATCH --nodes=1
#SBATCH --gres=gpu:2
#SBATCH --export=NONE
```

## Additional Information
- For more details, refer to the documentation: [TinyGPU Cluster Documentation](https://hpc.fau.de/systems-services/systems-documentation-instructions/clusters/tinygpu-cluster/)

## Conclusion
- Ensure proper specification of GPU resources and walltime in batch scripts.
- Avoid using invalid partition names and ensure resource requests are within allowed limits.
---

### 2018060642000616_jobs%20on%20TinyGPU%20_%20iwsp010h.md
# Ticket 2018060642000616

 # HPC Support Ticket Analysis: Jobs on TinyGPU / iwsp010h

## Keywords
- TinyGPU
- Job Scripts
- GPU Utilization
- PBS
- nvidia-smi
- GeForce GTX 980

## Problem
- User's jobs on TinyGPU request 2 GPUs per job, but only one GPU is actually used.
- Example job ID: 188159

## Root Cause
- Job script requests 8 processors per node (`ppn=8`), which implies the use of 2 GPUs.
- `nvidia-smi` output shows that only one GPU is fully utilized while the other is idle.

## Solution
- HPC Admin advised the user to check and correct the job scripts to ensure efficient GPU utilization.
- Ensure that the job scripts accurately reflect the number of GPUs required.

## General Learning
- Always verify job scripts to match the actual resource requirements.
- Use `nvidia-smi` to monitor GPU usage and identify underutilization.
- Adjust job scripts to optimize resource allocation and avoid wastage.

## Example Job Script Issue
```plaintext
#PBS -l nodes=1:ppn=8
```
- `ppn=8` implies the use of 2 GPUs, but only one is utilized.

## Monitoring Tool
- `nvidia-smi` is used to monitor GPU usage and identify underutilization.

## Conclusion
- Proper job script configuration is crucial for efficient resource utilization.
- Regular monitoring of resource usage helps in identifying and rectifying inefficiencies.
---

### 2021042842003758_Anfrage%20wegen%20Clusterressources.md
# Ticket 2021042842003758

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject
Anfrage wegen Clusterressourcen

## Keywords
- HPC Resources
- FAU-Grundversorgung
- GPGPU-Ressourcen
- Nvidia A100
- SSH Access
- Batchsystem (PBS or Slurm)
- HPC-Cafe
- HPC-Antragsformular

## Summary
- **User Request**: Newly appointed professors inquire about HPC resources available to their department, including availability, access, and capacities.
- **HPC Admin Response**: Provides preliminary information about HPC resources, including:
  - Free access to HPC systems under FAU-Grundversorgung.
  - Financial contribution by AIBE for GPGPU resources with Nvidia A100, expected by end of June.
  - Access via SSH to login nodes and batch systems (PBS or Slurm).
  - Restrictions on processing personal or sensitive data.
  - Documentation and application form available on the HPC website.
  - Monthly HPC-Cafe and introductory sessions for new users.

## Root Cause of the Problem
- New professors need information about the HPC resources available to their department and how to access them.

## Solution
- HPC Admin provides detailed information about the resources, access methods, and upcoming events.
- A meeting is tentatively scheduled to discuss further details.

## General Learnings
- HPC resources at FAU are accessible under certain conditions and regulations.
- Specific departments contribute financially to enhance HPC capabilities.
- Regular events like HPC-Cafe and introductory sessions are available for user support.
- Documentation and application forms are available on the HPC website.
```
---

### 2024082242000204_Job%20on%20Alex%20do%20not%20use%20GPU%20%5Bgwgi018h%5D.md
# Ticket 2024082242000204

 ```markdown
# HPC Support Ticket: Job on Alex Not Using GPU

## Keywords
- GPU utilization
- Job allocation
- Monitoring system
- ClusterCockpit
- `nvidia-smi`
- Resource management

## Summary
A user's job on the HPC system Alex was not utilizing all allocated GPUs, leading to resource wastage.

## Root Cause
The user's job (JobID 2014806) was allocated 4 GPUs but was only using one, as indicated by the monitoring system.

## Solution
1. **Monitoring GPU Utilization**:
   - Users can log into the monitoring system ClusterCockpit at [https://monitoring.nhr.fau.de/](https://monitoring.nhr.fau.de/) to view GPU utilization.
   - Alternatively, users can attach to their running job using the command `srun --pty --overlap --jobid YOUR-JOBID bash` and run `nvidia-smi` to check GPU usage.

2. **Resource Allocation**:
   - Ensure that jobs are only allocated nodes with GPUs if the code can effectively utilize them.
   - Avoid idle GPU resources by properly configuring job scripts to use all allocated GPUs.

## Lessons Learned
- Regularly monitor job performance to ensure efficient resource utilization.
- Use available monitoring tools to diagnose and optimize job performance.
- Properly configure job scripts to match the allocated resources.

## Follow-Up
- If further assistance is needed, users should contact the HPC support team.

## Contact Information
- **HPC Admins**: support-hpc@fau.de
- **2nd Level Support Team**: Lacey, Dane (fo36fizy), Kuckuk, Sebastian (sisekuck), Lange, Florian (ow86apyf), Ernst, Dominik (te42kyfo), Mayr, Martin
- **Head of Datacenter**: Gerhard Wellein
- **Training and Support Group Leader**: Georg Hager
- **NHR Rechenzeit Support**: Harald Lanig
- **Software and Tools Developer**: Jan Eitzinger, Gruber
```
---

### 2024112842002481_HPC%20consumption%20query.md
# Ticket 2024112842002481

 # HPC Consumption Query

## Keywords
- HPC consumption
- GPU utilization
- A100 GPU
- ClusterCockpit
- `acc_utilization`
- `nvidia-smi`
- SLURM
- Job timeout

## Problem
- User queries about GPU consumption for a job using A100 GPU.
- Job crashes due to timeout.

## Solution
- **ClusterCockpit**: Use `acc_utilization` to monitor GPU utilization.
- **SLURM**: Attach a bash shell to a running job and use `nvidia-smi` to check GPU usage.
  - Reference: [Attach to a Running Job](https://doc.nhr.fau.de/batch-processing/batch_system_slurm/#attach-to-a-running-job)

## General Learnings
- Understanding how to monitor GPU utilization on HPC clusters.
- Using `nvidia-smi` for detailed GPU metrics.
- Attaching to running jobs in SLURM for real-time monitoring.

## Root Cause
- User needs to monitor GPU consumption to diagnose job timeout issues.

## Next Steps
- User should follow the provided instructions to monitor GPU usage.
- If the issue persists, further investigation into job timeout causes may be necessary.
---

### 2022021742001559_Job%20makes%20no%20use%20of%20GPU%20%5Biwal042h%5D.md
# Ticket 2022021742001559

 # HPC Support Ticket: Job Makes No Use of GPU

## Keywords
- GPU utilization
- Job monitoring
- Cluster selection
- TinyGPU

## Summary
A job submitted by a user on the TinyGPU cluster was not utilizing the GPU resources. The HPC Admin identified this through the monitoring system and notified the user.

## Root Cause
- The job was not configured to use GPU resources.

## Solution
- Ensure that jobs submitted to TinyGPU are configured to utilize GPU resources.
- If the job does not require GPU, submit it to a different cluster that does not have GPU resources.

## Lessons Learned
- Regularly monitor job resource utilization to ensure efficient use of HPC resources.
- Guide users to select appropriate clusters based on their job requirements.
- Provide documentation or training on configuring jobs for GPU utilization.

## Actions Taken
- HPC Admin notified the user about the issue and provided guidance on cluster selection.

## Follow-up
- No follow-up mentioned in the conversation.

## Related Parties
- HPC Admins
- 2nd Level Support Team
- Head of the Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support
- Software and Tools Developer

## References
- HPC Services, Friedrich-Alexander-Universitaet Erlangen-Nuernberg
- Regionales RechenZentrum Erlangen (RRZE)
- [HPC FAU](http://hpc.fau.de/)

---

This documentation aims to help support employees identify and resolve similar issues related to GPU utilization on HPC clusters.
---

### 2024051242000452_Alex%20nodes%20a0535%200537%20und%20updated%20slides.md
# Ticket 2024051242000452

 ```markdown
# HPC Support Ticket: Alex Nodes a0535 and 0537 Issues and Updated Slides

## Keywords
- Node failure
- GPU failure
- Multi-node run
- Onboarding slides
- Cluster updates
- SSH login
- TensorFlow

## Problem Description
- Node `a0535` crashed during a multi-node run.
- Node `0537` did not start correctly, causing a job failure.

## Root Cause
- Node `a0535`: GPU failure.
- Node `0537`: Unknown issue, no immediate cause identified.

## Solution
- Node `a0535`: Awaiting replacement GPU.
- Node `0537`: Further investigation required.

## Additional Information
- **Onboarding Slides Feedback**:
  - Remove references to decommissioned clusters "Emmy" and "tiny-eth".
  - Remove mention of HPC-Papierantrag.
  - Replace PuTTY with MobaXterm or Win11 integrated Ubuntu shell.
  - Expand login section to include SSH keys and proxy-jump.
  - Address both ML-Trainingsperformance and Job-performance using ClusterCockpit.
  - Note TensorFlow security issues on multi-user systems.

## References
- [SSH Command Line Documentation](https://doc.nhr.fau.de/access/ssh-command-line/)
- [TensorFlow Documentation](https://doc.nhr.fau.de/apps/tensorflow/)

## Next Steps
- Continue monitoring node `0537` for further issues.
- Update onboarding slides based on feedback.

## Ticket Status
- Closed
```
---

### 2023110242001399_Jobs%20pending%20since%20two%20weeks.md
# Ticket 2023110242001399

 # HPC Support Ticket: Jobs Pending Since Two Weeks

## Keywords
- Job pending
- GPU resources
- Resource allocation
- Job configuration
- Interactive jobs
- Normal jobs
- AssocGrpGRES

## Problem Description
- User reported jobs pending for more than a week.
- Interactive jobs were working, but normal jobs were not progressing.
- User suspected a configuration issue.

## Root Cause
- Limited GPU resources allocated to the user's project.
- High usage of GPU resources by the project in the previous month.

## Solution
- Inform the user about the limited GPU resources and high usage.
- Suggest adjusting the training schedule or resource allocation.

## Lessons Learned
- High demand for GPU resources can cause job delays.
- Monitoring resource usage and adjusting job configurations can help manage delays.
- Communication with users about resource limitations is crucial.

## Action Taken
- HPC Admin explained the resource limitations and high usage to the user.
- User acknowledged the information and planned to adjust the training schedule.

## Follow-up
- No further action required from HPC support.
- User will manage job submissions based on the provided information.
---

### 2024093042005175_Tier3-Access-Alex%20%22Michael%20Girstl%22%20_%20iwia112h.md
# Ticket 2024093042005175

 # HPC Support Ticket Analysis

## Keywords
- Tier3 Access
- Alex
- GPGPU Cluster
- Nvidia A100
- Nvidia A40
- GPU-hours
- nvhpc
- cudnn
- cuda
- python/pytorch
- Transformer Network
- Benchmarking
- Performance Measurement

## Summary
- **User Request**: Access to GPGPU cluster 'Alex' for testing and benchmarking a transformer network implemented in CUDA with C++.
- **Resources Requested**:
  - Nvidia A100 GPGPUs (9.7 TFlop/s double precision)
  - Nvidia A40 GPGPUs (48 GB, 37 TFlop/s single precision)
  - Approximately 50 GPU-hours distributed over multiple small jobs.
- **Software Requirements**:
  - nvhpc
  - cudnn/8.2.4.15-11.4
  - cuda/11.5.0
  - python/pytorch-1.10py3.9
- **Expected Outcome**: Performance measurements of the transformer network.

## Root Cause
- User needed access to specific GPU resources for benchmarking and testing a student project.

## Solution
- HPC Admin granted the user access to the requested resources.

## Lessons Learned
- Ensure proper documentation and communication for granting access to specific HPC resources.
- Verify user requirements for software modules and GPU specifications before granting access.
- Provide clear instructions for users on how to utilize the granted resources effectively.

## Follow-up Actions
- Monitor the usage of the granted GPU-hours to ensure compliance with the user's request.
- Offer support for any issues that may arise during the benchmarking process.
---

### 2024062842001492_Sleep-Job%20on%20Alex%20%5Bb211dd17%5D.md
# Ticket 2024062842001492

 # HPC Support Ticket: Sleep-Job on Alex

## Keywords
- Sleep command
- Interactive job
- Batch script
- Resource blocking
- Slurm submit script
- GPU usage

## Problem
- User repeatedly uses the `sleep` command in Slurm submit scripts to hold resources.
- User logs in interactively after the sleep job starts, leading to resource idling.
- Resources, including expensive GPUs, are blocked and not utilized efficiently.

## Root Cause
- Misuse of the `sleep` command to hold resources for interactive work.
- Inefficient resource utilization due to idle nodes.

## Solution
- **Allocate a true interactive job**: Refer to the documentation for setting up interactive jobs.
- **Write a batch script**: Ensure the script can run independently without user intervention.
- **Avoid using sleep jobs**: This practice leads to resource wastage and can result in account suspension.

## Action Taken
- HPC Admins warned the user about the misuse of resources.
- A sleep job was killed due to inefficient resource usage.
- Threat of account suspension if the practice continues.

## Documentation Links
- [Interactive Job Documentation](https://doc.nhr.fau.de/clusters/alex/#interactive-job-single-gpu)

## General Learning
- Properly allocate resources to ensure efficient usage.
- Avoid using sleep commands to hold resources.
- Seek assistance if unsure about writing submit scripts or setting up interactive jobs.

## Contact Information
- **Support Email**: support-hpc@fau.de
- **Website**: [FAU HPC](https://hpc.fau.de/)
---

### 2023092242003041_Anfrage%20Dokumentation%20Job%20Resources.md
# Ticket 2023092242003041

 # HPC Support Ticket: Anfrage Dokumentation Job Resources

## Keywords
- Job Resources
- Alex Cluster
- CPU Cores
- RAM
- GPU
- A40
- A100
- Resource Allocation

## Summary
The user requested documentation on the minimum, maximum, and default resources available on the Alex cluster, similar to the documentation provided for the Horeka cluster. The user specifically needed information on CPU cores and RAM allocation.

## Problem
The user could not find a clear listing of resource limits (e.g., number of CPU cores, RAM) on the provided documentation pages.

## Solution
The HPC Admin provided detailed information on resource allocation:
- **A40 GPUs**: 16 CPU cores and 60 GB RAM per GPU.
- **A100 GPUs**: 16 CPU cores and 120 GB RAM per GPU.
- CPU and RAM are automatically allocated and do not need to be explicitly requested.
- GPUs are exclusively allocated, while CPUs are shared but jobs remain within their control groups (cgroups).

Additionally, the HPC Admin clarified the RAM allocation for different types of nodes:
- **A40 Nodes**: 512 GB RAM per node, with 60 GB allocated per GPU and the remaining 32 GB for the operating system.
- **A100 Nodes**:
  - 40 GB HBM2: 1024 GB RAM per node, with 120 GB allocated per GPU and the remaining 64 GB for the operating system.
  - 80 GB HBM2: 2048 GB RAM per node, with 240 GB allocated per GPU and the remaining RAM for the operating system.

## Lessons Learned
- The Alex cluster allocates resources based on GPUs, with specific amounts of CPU cores and RAM assigned per GPU.
- The documentation on the Alex cluster should include a clear listing of resource limits for better user understanding.
- Users should be directed to the resource allocation table on the Alex cluster documentation page for detailed information.

## Follow-up
The user confirmed that the provided information was helpful and resolved their query. The ticket was closed with no further questions from the user.
---

### 2022083142001002_The%20slurm%20command%20for%20specify%20the%2080G%20memory%20version%20of%20a100%20on%20Alex%20clust.md
# Ticket 2022083142001002

 # HPC Support Ticket: Specifying 80GB A100 GPU on Alex Cluster

## Keywords
- Slurm
- A100 GPU
- 80GB memory
- Alex cluster
- sbatch
- Job submission

## Problem Description
- User needs to specify the 80GB version of A100 GPU on the Alex cluster.
- Previous command `sbatch AAA.sh -C a100_80` is not consistently assigning the 80GB A100 GPU.
- Job sometimes gets assigned to a 40GB A100 GPU, causing job failure due to insufficient memory.

## Root Cause
- The command `sbatch AAA.sh -C a100_80` is not effectively distinguishing between 40GB and 80GB A100 GPUs.

## Solution
- HPC Admin provided a link to the FAQ: [FAQ Link](https://hpc.fau.de/faqs/#innerID-13371)
- User should refer to the FAQ for the correct method to specify the 80GB A100 GPU.

## General Learnings
- Always be explicit about the nature of the problem when reporting issues.
- Check the FAQ or documentation for updated commands and procedures.
- Ensure job scripts are compatible with the specified hardware to avoid failures.

## Next Steps
- User should review the FAQ and update their job submission command accordingly.
- If the issue persists, further investigation by the HPC Admin may be required.
---

### 2024081442000461_Resources%20run%20out%3F.md
# Ticket 2024081442000461

 ```markdown
# HPC Support Ticket: Resources Run Out?

## Keywords
- GPU hours
- Invalid Trackable RESource (TRES) specification
- Slurm job_submitfilter.lua
- Maintenance
- Resource allocation

## Summary
A user encountered an error when applying for GPU hours, indicating an "Invalid Trackable RESource (TRES) specification." The HPC Admin initially responded with information about ongoing maintenance. Further investigation revealed an issue with the Slurm job_submitfilter.lua configuration.

## Root Cause
- The user received an error message indicating an invalid TRES specification when applying for GPU hours.
- The HPC system was under maintenance, which might have caused temporary issues.
- A configuration issue in Slurm job_submitfilter.lua was identified, where "gres/gpu..." was used instead of "gres:gpu..." in the job_desc.gres.

## Solution
- The HPC Admin fixed the configuration issue in Slurm job_submitfilter.lua by correcting the syntax for job_desc.gres.

## General Learning
- Always check for ongoing maintenance before troubleshooting resource allocation issues.
- Ensure that the Slurm configuration files are correctly set up, especially when dealing with GPU resources.
- Communicate clearly with users about system status and any necessary fixes.
```
---

### 2021071942002851_Testcluster%20Milan1.md
# Ticket 2021071942002851

 # HPC Support Ticket: Testcluster Milan1 Node Issue

## Keywords
- Milan1 Node
- Job failure
- IDLE+DRAIN state
- GPGPU-Cluster installation
- Slurm error

## Problem Description
- **User Report:** Milan1 node not starting jobs for a week due to an error.
- **Node Status:**
  - State: `IDLE+DRAIN`
  - Reason: `batch job complete failure [slurm@2021-07-12T20:29:06]`

## Root Cause
- The node was being prepared for a large GPGPU-Cluster installation and was temporarily unavailable for job scheduling.

## Solution
- **HPC Admin Response:** Informed the user that Milan1 is currently unavailable due to preparations for the GPGPU-Cluster installation.

## General Learnings
- Nodes may be temporarily unavailable due to maintenance or preparations for new installations.
- Check the node state and reason for any job scheduling issues.
- Communicate with HPC Admins for updates on node availability.

## Related Commands
- `scontrol show node <node_name>`: Display detailed information about a specific node.

## Ticket Status
- Closed with explanation. No further action required from the user's side.
---

### 2024061342002367_Jobs%20on%20Alex%20do%20not%20use%20all%20allocated%20GPUs%20-%20iwb0003h.md
# Ticket 2024061342002367

 # HPC Support Ticket: Jobs Not Utilizing All Allocated GPUs

## Keywords
- GPU utilization
- Job allocation
- `nvidia-smi`
- `srun`
- Resource management

## Problem Description
- User's jobs on Alex were allocating two GPUs but utilizing only one.
- JobIDs: 1724632, 1724634, 1724629, 1723806

## Root Cause
- Inefficient resource allocation leading to idle GPUs.

## Diagnostic Steps
- Attach to the running job using `srun --pty --overlap --jobid YOUR-JOBID bash`.
- Check GPU utilization with `nvidia-smi`.

## Solution
- User canceled the jobs and resubmitted them with one GPU allocation.

## General Learnings
- Ensure jobs are configured to utilize all allocated resources.
- Use diagnostic tools like `nvidia-smi` to monitor GPU usage.
- Proper resource allocation prevents idle resources and improves overall system efficiency.

## Contact Information
- For further assistance, contact HPC support at `support-hpc@fau.de`.

---

This documentation aims to help HPC support employees diagnose and resolve similar issues efficiently.
---

### 2024013042001488_Tier3-Access-Alex%20%22Jonas%20Utz%22%20_%20iwso041h.md
# Ticket 2024013042001488

 # HPC Support Ticket Analysis: Tier3-Access-Alex

## Keywords
- Tier3 Access
- Alex GPGPU Cluster
- NHR Project Application
- GPU Hours Quota
- Python, PyTorch, RoMa
- Implicit Neural Representations (INRs)
- A40 GPGPUs

## Summary
A user requested access to the Alex GPGPU cluster for training implicit neural representations (INRs). The estimated demand of 3200 GPU hours exceeds the Tier3 quota and approaches the limit of an NHR test project.

## Root Cause
- User's estimated GPU hours (3200) exceed the Tier3 quota.
- The requested compute time cannot be guaranteed without an NHR application.

## Solution
- HPC Admin granted access to the Alex cluster.
- User advised to apply for an NHR project to secure the required compute time.
- Link to NHR application rules provided: [NHR Application Rules](https://hpc.fau.de/systems-services/documentation-instructions/nhr-application-rules/)

## General Learnings
- Understand the GPU hours quota for Tier3 access.
- For extensive compute time, users should apply for an NHR project.
- Alex cluster is suitable for tasks requiring high single-precision performance.

## Related Software and Tools
- Python
- PyTorch
- RoMa

## Related Hardware
- Nvidia A40 GPGPUs

## Related HPC Admins
- Johannes Veh

## Related Support Team
- Harald Lanig (NHR Rechenzeit Support and Applications for Grants)

## Related Links
- [NHR Application Rules](https://hpc.fau.de/systems-services/documentation-instructions/nhr-application-rules/)
- [HPC FAU](https://hpc.fau.de/)
---

### 2018073042002111_script%20not%20running.md
# Ticket 2018073042002111

 # HPC Support Ticket: Script Not Running

## Issue
- User's batch script for deep learning training is not running and remains in the queue indefinitely.
- User requests a complete node with four GPUs (`ppn=16`), leading to long queue times.

## Root Cause
- High demand for GPU resources on TinyGPU.
- Only six nodes qualify for the user's request, and all are partially busy.

## Solution
- Reduce the number of requested GPUs to improve throughput.
- Specify a walltime to avoid the default 10-minute limit.
- Monitor GPU usage with `nvidia-smi` to ensure efficient resource utilization.

## Key Points
- Default walltime is 10 minutes if not specified.
- Jobs requesting fewer GPUs (e.g., `ppn=4`) have a higher chance of running sooner.
- Use `qstat.tinygpu -rn` to check the node where the job is running.
- Log into the node with `ssh` and use `nvidia-smi` to monitor GPU usage.

## Additional Notes
- Longer tasks need to be split into several jobs to fit within the walltime limit.
- Ensure that all requested GPUs are actively used to avoid resource wastage.

## Example Script Adjustment
```bash
#!/bin/bash -l
#PBS -l nodes=1:ppn=4:gtx1080
#PBS -l walltime=24:00:00
#PBS -N deep_training
#PBS -M user@example.com
#PBS -o /home/user/deep1.out -e /home/user/deep1.err

source /home/user/tensorflow/venv/bin/activate
python3 /home/user/DEEPGESTURE/training/offline_training.py
```

This adjustment requests one GPU and specifies a walltime of 24 hours, improving the chances of the job running sooner.
---

### 2022101042001707_CUDA%20out%20of%20memory.md
# Ticket 2022101042001707

 ```markdown
# HPC Support Ticket: CUDA out of memory

## Keywords
- CUDA out of memory
- GPU access
- Job monitoring
- ClusterCockpit
- TinyGPU cluster
- Pytorch models
- GPU memory
- RTX 2080 Ti
- Tesla V100

## Problem
- User encounters "CUDA out of memory" error when training larger Pytorch models.
- User has access to smaller GPUs (e.g., RTX 2080 Ti) but not to larger GPUs (e.g., Tesla V100).
- User cannot see jobs in ClusterCockpit.

## Root Cause
- Insufficient GPU memory for larger models.
- Limited access to larger GPUs.
- ClusterCockpit not integrated with TinyGPU cluster.

## Solution
- **GPU Access**: Refer to the documentation for available GPU types and memory on the TinyGPU cluster.
  - [Documentation Link](https://hpc.fau.de/systems-services/documentation-instructions/clusters/tinygpu-cluster/)
- **Job Monitoring**: ClusterCockpit integration with TinyGPU is in progress.

## General Learning
- Users should check the documentation for available GPU types and memory.
- ClusterCockpit may not be integrated with all clusters, and integration status should be verified.
- Larger models may require GPUs with more memory, and users should request access if needed.
```
---

### 2024111242001976_Inquiry%20-%20TinyGPU%20out%20of%20memory.md
# Ticket 2024111242001976

 ```markdown
# HPC Support Ticket: TinyGPU Out of Memory

## Keywords
- CUDA out of memory
- PyTorch
- GPU memory allocation
- Backup access

## Summary
- **User Issue**: The user encountered a `torch.OutOfMemoryError` when running a job using V100 GPUs. The error indicated that the GPU memory was insufficient for the task.
- **Root Cause**: The job attempted to allocate more memory than available on a single GPU.
- **Solution**: The HPC Admin suggested discussing the issue with colleagues at AIBE, as the user had previously raised a similar issue.

## Detailed Conversation
- **User**: Reported a `torch.OutOfMemoryError` when trying to allocate 22.05 GiB on a GPU with a total capacity of 31.73 GiB.
- **HPC Admin**: Advised the user to consult with colleagues at AIBE, noting that the issue had been previously addressed in another ticket.
- **User**: Inquired about accessing older backups from $HOME, with the latest snapshots being from the previous month.
- **HPC Admin**: Closed the ticket, suggesting that the backup question be addressed in a separate ticket.

## Lessons Learned
- **Memory Management**: Ensure that the memory requirements of the job do not exceed the capacity of the available GPUs.
- **Collaboration**: Encourage users to collaborate with colleagues for troubleshooting and sharing solutions.
- **Backup Access**: Users may need to request access to older backups through a separate support ticket.
```
---

### 2022021442003366_bad%20performing%20jobs%20a0422.md
# Ticket 2022021442003366

 # HPC Support Ticket: Bad Performing Jobs

## Keywords
- FileNotFoundError
- GPU utilization
- Job performance
- Code optimization

## Summary
A user encountered issues with their jobs running on the HPC system, specifically related to file not found errors and low GPU utilization.

## Root Cause
- **FileNotFoundError**: The jobs were failing due to missing files, as indicated by the error messages in the `.err` files.
- **Low GPU Utilization**: Initially, the jobs had low GPU utilization (10% - 20%).

## Solution
- **FileNotFoundError**: The user identified and corrected a bug in the code that was causing the file not found errors.
- **GPU Utilization**: The user modified the code to improve GPU utilization, achieving 50% - 60% (and up to 80% for some jobs).

## General Learnings
- **Error Handling**: Always check error files for specific issues when jobs fail.
- **GPU Utilization**: Aim for 50% - 80% GPU utilization for efficient resource usage.
- **Optimization**: Use tools like [pylikwid](https://github.com/RRZE-HPC/pylikwid) to identify bottlenecks and optimize code performance.

## Additional Resources
- [pylikwid GitHub Repository](https://github.com/RRZE-HPC/pylikwid)

## Next Steps
- Continue monitoring job performance and GPU utilization.
- Consider further code optimization if necessary.

## Support Team
- **HPC Admins**: Provided initial error reports and guidance on acceptable GPU utilization.
- **2nd Level Support Team**: Assisted with identifying and resolving the issues.

## Conclusion
The user successfully resolved the file not found errors and improved GPU utilization, leading to better job performance on the HPC system.
---

### 2021113042003098_Early-Alex%20%22Frank%20Zalkow%22%20_%20iwal005h.md
# Ticket 2021113042003098

 # HPC Support Ticket Conversation Summary

## Keywords
- Early-Alex Cluster
- GPU Utilization
- nvidia-smi
- SSH Login
- Cgroup
- Deep Learning
- Speech Synthesis
- Python
- Anaconda
- Pytorch

## General Learnings
- **User Access and Documentation**: HPC Admins provide access to early users and direct them to the cluster documentation.
- **GPU Utilization Monitoring**: Users can monitor GPU utilization using `nvidia-smi` after logging in via SSH.
- **Cgroup Attachment**: Users are attached to the Cgroup of one of their jobs when logging in via SSH.
- **User Feedback**: Users are encouraged to provide feedback on their experience with the cluster.

## Root Cause of the Problem
- The user's jobs were not utilizing the GPU as expected, indicated by `nvidia-smi` not showing GPU utilization.

## Solution
- The user fixed their code to ensure that calculations were performed on the GPU.

## Support Interaction
- **HPC Admin**: Provided access to the cluster, documentation link, and guidance on monitoring GPU utilization.
- **User**: Tested access, ran jobs, and fixed the code to utilize the GPU. Provided feedback and appreciation for the support.

## Additional Notes
- The user's work involves deep learning-based speech synthesis models using Python, Anaconda, and Pytorch.
- The user planned to start work in the early adapter phase at the beginning of 2022.

This summary can be used as a reference for future support cases involving GPU utilization issues and early user access to HPC clusters.
---

### 2024112142002421_Tier3-Access-Alex%20%22Sascha%20Hofmann%22%20_%20mi40paha.md
# Ticket 2024112142002421

 # HPC Support Ticket Analysis

## Keywords
- HPC account
- Tier3 account
- Runtime requirements
- GPGPU cluster
- Nvidia A100 GPGPUs
- MPI
- nvhpc
- nsight systems/compute
- CUDA-streams
- Benchmarking routines
- Kernel fusion
- Batching
- Overlapping communication kernels
- nvshmem implementations

## Summary
- **User Issue**: The user did not have an HPC account and requested access to the GPGPU cluster 'Alex' with a short runtime requirement.
- **HPC Admin Response**: The admin informed the user about the need to create an HPC account and suggested combining multiple calculations into a single job to increase runtime.
- **User Action**: The user realized they needed to accept an invitation to unlock their HPC account and resubmitted their request with adjusted runtime requirements.

## Root Cause
- The user was unaware of the need to accept an invitation to activate their HPC account.
- The initial runtime requirement was too short (2 minutes).

## Solution
- The user was directed to the account creation guide: [HPC Account Guide](https://doc.nhr.fau.de/account/).
- The user was advised to combine multiple calculations to achieve a runtime longer than 2 minutes.

## General Learnings
- Users need to be aware of the distinction between IdM accounts and HPC accounts.
- Short runtime requests should be consolidated into longer jobs to optimize resource usage.
- Proper communication and guidance on account activation and runtime requirements can resolve common user issues.

## References
- [HPC Account Guide](https://doc.nhr.fau.de/account/)
- [NHR@FAU](https://hpc.fau.de/)
---

### 2021120842000078_Interactive%20jobs.md
# Ticket 2021120842000078

 # HPC Support Ticket: Interactive Jobs

## Keywords
- Interactive nodes
- srun command
- Resource allocation
- Job queue
- TinyGPU partition

## Problem
- User unable to obtain an interactive node using `srun` command.
- Command used: `srun --partition=work --nodes=tinygpu --clusters=tinygpu --time=3:0:0 --gres=gpu:1 --pty /bin/bash -l`
- Job queued and waiting for resources.

## Root Cause
- High demand for TinyGPU resources.
- Specific user group (FHG IIS/Audiolabs) has more than 60 jobs queued, occupying over one-third of all jobs.

## Solution
- No immediate solution provided due to resource unavailability.
- User informed about the high demand and resource constraints.

## General Learning
- High demand for specific resources can lead to job queue delays.
- Monitoring resource usage and job queue status can help in understanding delays.
- Alternative methods for obtaining interactive nodes were not discussed in this ticket.

## Next Steps for Support
- Inform users about resource availability and potential delays.
- Consider suggesting alternative partitions or resources if available.
- Monitor job queue and resource usage to manage expectations and allocate resources efficiently.
---

### 2022021842001262_Job%20auf%20TinyGPU%20nutzt%20keine%20GPU%20%5Biwia032h%5D.md
# Ticket 2022021842001262

 # HPC Support Ticket: Job auf TinyGPU nutzt keine GPU

## Keywords
- GPU utilization
- Job scheduling
- CPU-only jobs
- Cluster monitoring
- Job splitting

## Summary
A user's job on TinyGPU was not utilizing the allocated GPU, causing inefficient resource usage. The user intended to run a job with both CPU and GPU parts but encountered delays in the CPU portion.

## Root Cause
- The job was designed to have both CPU and GPU components but was not properly utilizing the GPU.
- The CPU part of the job took longer than expected, leading to inefficient use of GPU resources.

## Solution
- The user planned to split the job into separate CPU and GPU parts and run the CPU part on a CPU-only cluster.

## Lessons Learned
- Ensure jobs are properly configured to utilize allocated resources.
- Consider splitting jobs into CPU and GPU components if they have distinct requirements.
- Monitor job performance to identify and address inefficiencies.

## Recommendations
- Provide guidance on job configuration and resource allocation.
- Encourage users to monitor job performance and adjust as needed.
- Offer training on efficient job scheduling and resource management.

## References
- HPC Services, Friedrich-Alexander-Universitaet Erlangen-Nuernberg
- Regionales RechenZentrum Erlangen (RRZE)
- [HPC Support](mailto:support-hpc@fau.de)
- [HPC Website](http://hpc.fau.de/)
---

### 2024080642003189_Job%20on%20Alex%20does%20only%20use%201%20of%202%20allocated%20GPUs%20%5Biwi5192h%5D.md
# Ticket 2024080642003189

 # HPC Support Ticket: Job on Alex Uses Only One of Allocated GPUs

## Keywords
- GPU utilization
- PyTorch Lightning
- Multi-GPU training
- Resource allocation
- Monitoring
- `nvidia-smi`
- ClusterCockpit

## Problem Description
The user's jobs on the HPC cluster were only utilizing one of the allocated GPUs, despite being configured for multi-GPU training with PyTorch Lightning.

## Root Cause
The exact root cause was not identified, but it was suspected to be an issue with the user's code or configuration.

## Steps Taken by HPC Admins
1. **Notified User of Underutilization:**
   - Informed the user about the underutilization of GPUs through multiple emails.
   - Provided screenshots from the monitoring system (ClusterCockpit) to illustrate the issue.

2. **Provided Monitoring Tools:**
   - Guided the user on how to monitor GPU utilization using `nvidia-smi`.
   - Instructed the user on how to attach to a running job using `srun --pty --overlap --jobid YOUR-JOBID bash`.

3. **Warned About Resource Wastage:**
   - Advised the user to ensure that allocated GPU resources are fully utilized to avoid wastage.

4. **Threatened Account Throttling:**
   - Informed the user that their account would be throttled if the issue was not resolved.

## User's Response
- The user acknowledged the issue and mentioned that their PyTorch Lightning code was intended for multi-GPU training.
- The user requested help but was directed to seek assistance from coworkers who had previously resolved similar issues.
- The user planned to run test jobs to diagnose the problem and monitor GPU usage.

## Solution
- The user was advised to consult with coworkers who had experience with similar issues.
- The user planned to run short test jobs to monitor GPU usage and diagnose the problem.

## Conclusion
The ticket was closed with the user planning to run diagnostic tests and seek help from experienced coworkers. The HPC Admins provided guidance on monitoring tools and resource utilization best practices.

## Notes for Future Reference
- Ensure users are aware of the importance of fully utilizing allocated resources.
- Provide guidance on monitoring tools and best practices for resource allocation.
- Encourage users to seek help from experienced colleagues or support teams when facing technical issues.
---

### 2024082842000481_Job%20on%20Alex%20is%20only%20using%201%20of%208%20GPU%20%5Bb211dd14%5D.md
# Ticket 2024082842000481

 # HPC Support Ticket Analysis

## Subject
Job on Alex is only using 1 of 8 GPU

## Keywords
- `sleep` command
- Interactive job
- Batch script
- GPU utilization
- Job monitoring
- Slurm submit script
- Resource allocation

## Lessons Learned

### Problem
- User was using the `sleep` command in the Slurm submit script and then logging in to the node to start work interactively.
- User's job was only utilizing 1 out of 8 allocated GPUs.

### Root Cause
- Incorrect command input led to underutilization of GPU resources.
- Use of `sleep` command resulted in idle resources, especially if the job was scheduled to start at inconvenient times.

### Solution
- **Interactive Job**: Allocate a true interactive job if interactive work is necessary.
- **Batch Script**: Write a batch script that can run independently without user intervention.
- **Correct Command**: Ensure the correct command is used to utilize all allocated GPUs.

### Additional Issues
- User submitted a new batch job that disappeared from the system.

### Resolution
- The job failed due to a missing `-l` in the first line of the script.

## Best Practices
- Avoid using the `sleep` command in Slurm submit scripts.
- Ensure batch scripts are written to run independently.
- Properly allocate and utilize all requested resources to avoid wastage.
- Contact HPC support for assistance with writing submit scripts or any other questions.

## References
- [Interactive Job Documentation](https://doc.nhr.fau.de/clusters/alex/#interactive-job-single-gpu)

## Support Contacts
- **HPC Admins**: For general support and job monitoring.
- **2nd Level Support Team**: For advanced troubleshooting and script assistance.
- **Gehard Wellein**: Head of the Datacenter.
- **Georg Hager**: Training and Support Group Leader.
- **Harald Lanig**: NHR Rechenzeit Support and Applications for Grants.
- **Jan Eitzinger and Gruber**: Software and Tools developers.

## Conclusion
Proper job submission practices and resource utilization are crucial for efficient HPC cluster operation. Users should avoid practices that lead to idle resources and ensure their scripts are correctly written to make the most of allocated resources.
---

### 2024120542001228_Tier3-Access-Alex%20%22Florian%20Prohaska%22%20_%20mp24100h.md
# Ticket 2024120542001228

 ```markdown
# HPC Support Ticket: Tier3-Access-Alex

## Keywords
- Tier3 Access
- GPU Hours
- NHR Project
- Alex Cluster
- Nvidia A40
- Matlab
- Cuda
- Simulation and Optimization

## Summary
A user requested 80,000 GPU hours on the Alex cluster, which exceeds the free Tier3 access limit. The HPC Admin granted access but advised the user to apply for an NHR project if the demand is too high.

## Problem
- User requested 80,000 GPU hours, which is beyond the free Tier3 access.

## Solution
- HPC Admin granted access to the Alex cluster.
- User was advised to apply for an NHR project if the actual demand is too high.
- User agreed to reduce the actual demand and use TinyGPU to minimize the load on Alex.

## Lessons Learned
- Large GPU hour requests should be directed towards NHR project applications.
- Users should be aware of the free Tier3 access limits.
- Efficient use of resources, such as running multiple simulations per GPU, can help reduce demand.

## Actions Taken
- Access to Alex cluster granted.
- User advised to apply for NHR project if needed.
- Ticket closed.
```
---

### 2023071942002151_Cannot%20run%20job%20using%20Slurm.md
# Ticket 2023071942002151

 ```markdown
# HPC Support Ticket: Cannot run job using Slurm

## Keywords
- Slurm
- Job script
- GPU allocation
- CUDA out of memory
- A100 GPU
- RTX3080 GPU

## Problem Description
- User can run a program in the interactive shell but not using Slurm.
- Job script ends after 2 seconds with no running process found.
- User cannot allocate A100 GPU, only RTX3080 GPU.

## Root Cause
- Incorrect job script configuration.
- A100 GPU not available or special permission required.

## Solution
- Correct the job script configuration.
  - Ensure the first line of the script is correct.
  - Verify the job script syntax and parameters.
- Check availability and permissions for A100 GPU.
  - Confirm if A100 GPU is available on the cluster.
  - Verify if special permissions are required to access A100 GPU.

## What Can Be Learned
- Always verify the job script configuration.
- Ensure the first line of the job script is correct.
- Check GPU availability and permissions before submitting jobs.
- CUDA out of memory errors can occur if the GPU does not have enough memory for the task.

## Additional Notes
- Update documentation if necessary to reflect correct job script configuration.
- Provide guidance on how to check GPU availability and permissions.
```
---

### 2024111142000479_Job%20on%20Alex%20is%20only%20using%202%20of%2016%20GPU%20%5Bv104dd14%5D.md
# Ticket 2024111142000479

 ```markdown
# HPC Support Ticket: Job on Alex is only using 2 of 16 GPU

## Keywords
- GPU utilization
- Job monitoring
- Resource allocation
- ClusterCockpit
- `nvidia-smi`
- `srun`

## Problem Description
The user's jobs on Alex (JobID 2153886, 2153887) were only utilizing one of the eight allocated GPUs.

## Root Cause
The user's code was not configured to utilize all the allocated GPUs, leading to underutilization of resources.

## Solution
1. **Monitoring GPU Utilization**:
   - Use ClusterCockpit at [https://monitoring.nhr.fau.de/](https://monitoring.nhr.fau.de/) to view GPU utilization.
   - Alternatively, attach to the running job using `srun --pty --overlap --jobid YOUR-JOBID bash` and run `nvidia-smi` to check GPU utilization.

2. **Code Optimization**:
   - Ensure the code is optimized to utilize all allocated GPUs.
   - Kill underutilized jobs and resubmit with corrected code.

## Lessons Learned
- Always verify that the code can effectively utilize the allocated GPUs before submitting jobs.
- Regularly monitor GPU utilization to ensure efficient use of resources.
- Use monitoring tools like ClusterCockpit and `nvidia-smi` to diagnose and resolve underutilization issues.

## Follow-Up Actions
- If similar issues arise, guide users to optimize their code for better GPU utilization.
- Provide resources and documentation on how to effectively use monitoring tools.
```
---

### 2023021842000485_GPU%20detected%20but%20not%20used.md
# Ticket 2023021842000485

 ```markdown
# HPC-Support Ticket: GPU Detected but Not Used

## Keywords
- GPU usage
- Job monitoring
- Network storage I/O
- HPC cluster
- Training script

## Problem Description
- User's training script is failing to use GPU despite the GPU being detected.
- Job ID: 555875
- Node: tg081

## Root Cause
- The job did use a GPU, but there was excessive I/O on the network storage, which could slow down training.

## Solution
- Verify GPU usage through job monitoring.
- Reduce I/O operations on network storage to improve training performance.
- Refer to the documentation for best practices on managing I/O operations.

## References
- [Job Monitoring](https://monitoring.nhr.fau.de/monitoring/job/3887156)
- [Documentation on I/O Operations](https://hpc.fau.de/faqs/#innerID-13955)

## Notes
- Ensure proper monitoring and optimization of I/O operations to avoid performance bottlenecks.
- Regularly check job status and resource usage to diagnose similar issues in the future.
```
---

### 2024080642002591_Tier3-Access-Alex%20%22Paula%20Andrea%20Perez-Toro%22%20_%20iwi5214h.md
# Ticket 2024080642002591

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject: Tier3-Access-Alex / User Request for GPU Access

### Keywords:
- HPC Access
- GPGPU Cluster
- Nvidia A40
- Pytorch
- PostDoc Research
- Publication

### Summary:
- **User Request**: Access to GPGPU cluster 'Alex' with Nvidia A40 GPUs for PostDoc research.
- **Required Software**: Pytorch.
- **Expected Outcome**: Publication.
- **HPC Admin Response**: Access granted to use A40 in Alex.

### Key Learnings:
- **Access Request Process**: Users can request access to specific HPC resources by specifying their needs, including hardware, software, and expected outcomes.
- **Admin Response**: HPC Admins review and grant access based on the user's request and requirements.
- **Software Requirement**: Users should specify the software they need (e.g., Pytorch) to ensure compatibility and availability.

### Root Cause of the Problem:
- User needed access to specific HPC resources (Nvidia A40 GPUs) for their research.

### Solution:
- HPC Admin granted the user access to the requested resources.

### Notes:
- This ticket demonstrates the process for requesting and granting access to specific HPC resources.
- Ensure users provide detailed information about their needs, including hardware, software, and expected outcomes.
```
---

### 2022070742001407_Jobs%20auf%20TinyGPU%20nutzen%20die%20GPU%20nicht%20%5Bempk002h%5D.md
# Ticket 2022070742001407

 ```markdown
# HPC Support Ticket: Jobs auf TinyGPU nutzen die GPU nicht

## Keywords
- GPU utilization
- TinyGPU
- nvidia-smi
- JobID
- Monitoring system
- ssh
- GPU resources

## Problem Description
- User's jobs on TinyGPU (JobID 272827, 272829, 272829) are not utilizing the requested GPU resources.
- Monitoring system screenshot shows no GPU usage for the user's jobs.

## Root Cause
- The user's code does not utilize the GPU resources effectively.

## Solution
- **Investigation**: HPC Admin provided a screenshot from the monitoring system indicating no GPU usage.
- **Action**: User advised to log in via `ssh` to the relevant node and use `nvidia-smi` to check GPU utilization.
- **Guidance**: User directed to the documentation on working with NVIDIA GPUs: [Working with NVIDIA GPUs](https://hpc.fau.de/systems-services/systems-documentation-instructions/special-applications-and-tips-tricks/working-with-nvidia-gpus/).
- **Recommendation**: Ensure that GPU nodes are only requested if the code can effectively use the GPUs to avoid wasting resources.

## General Learning
- Always verify GPU utilization using `nvidia-smi` when running jobs on GPU nodes.
- Refer to the official documentation for guidance on working with NVIDIA GPUs.
- Only request GPU resources if the code is optimized to use them, to prevent resource wastage.

## Ticket Status
- The ticket was closed by the HPC Admin.
```
---

### 2022051642001537_Job%20on%20TinyGPU%20stops%20using%20GPU%20after%20one%20hour%20%5Biwal043h%5D.md
# Ticket 2022051642001537

 # HPC Support Ticket: Job on TinyGPU Stops Using GPU After One Hour

## Keywords
- TinyGPU
- GPU utilization
- JobID 254393
- nvidia-smi
- Idle resources

## Problem Description
A job on TinyGPU (JobID 254393) stops using the GPU approximately one hour after job submission. The GPU utilization drops, leaving the allocated resources idle.

## Diagnostic Steps
- HPC Admin monitored the job and attached a screenshot showing GPU utilization.
- User was advised to SSH into the node and use `nvidia-smi` to check GPU utilization.

## Root Cause
The job initially runs on the GPU but later parts of the code do not utilize the GPU, leading to idle resources.

## Solution
Ensure that all parts of the code are optimized to run on the GPU to prevent resource wastage.

## Additional Information
- **Documentation Link**: [Working with NVIDIA GPUs](https://hpc.fau.de/systems-services/systems-documentation-instructions/special-applications-and-tips-tricks/working-with-nvidia-gpus/)
- **Contact**: support-hpc@fau.de

## Ticket Status
The ticket was closed due to no response from the user.

## Lessons Learned
- Regularly monitor GPU utilization to ensure efficient resource usage.
- Optimize code to fully utilize allocated GPU resources.
- Use `nvidia-smi` for real-time GPU monitoring.
---

### 2021071942000791_Comsol-Rechencluster.md
# Ticket 2021071942000791

 # HPC-Support Ticket: Comsol-Rechencluster

## Problemstellung
- **User**: Probleme bei der Einrichtung des SLURM Schedulers auf einem Cluster-Rechner mit Ubuntu Server.
- **Setup**:
  - CPUs: 2x Intel Xeon Gold 6230R
  - RAM: 1TB (Samsung)
  - Motherboard: Supermicro X11DPi-N(T)
  - GPU: NVIDIA Quadro P2000
  - OS: Ubuntu Server 20.04 LTS
  - Scheduler: SLURM (snap-Version)

## Kommunikation
- **User**: Fragt nach Tipps zur SLURM-Konfiguration und Dokumentation.
- **HPC Admin**: Vorschlag einer Zoom-Session zur detaillierten Besprechung.
- **User**: Bestätigt die Zoom-Session und bittet um Hilfe bei der SLURM-Konfiguration, insbesondere bei den User-Einstellungen.

## Root Cause
- **Problem**: SLURM-Daemons starten nicht nach Änderung des slurm-Users.

## Lösung
- **HPC Admin**: Vorschlag, SLURM ohne SNAP zu installieren.

## Weitere Schritte
- **HPC Admin**: Vorschlag einer Zoom-Session zur detaillierten Besprechung und Unterstützung bei der SLURM-Konfiguration.

## Keywords
- SLURM
- Ubuntu Server
- COMSOL
- Cluster-Rechner
- Zoom-Session
- SLURM-Daemons
- SLURM-User
- SNAP

## Generelle Erkenntnisse
- Die Basisinstallation von SLURM kann entweder selbst paketiert oder aus den Sources manuell gebaut werden.
- Eine Zoom-Session kann hilfreich sein, um detaillierte Probleme und Lösungen zu besprechen.
- SLURM-Daemons können Probleme haben, nach Änderungen am slurm-User zu starten. Eine Installation ohne SNAP könnte eine Lösung sein.
---

### 2022121442000724_Probleme%20mit%20Node%20tg080%20auf%20dem%20TinyGPU%20Cluster.md
# Ticket 2022121442000724

 # HPC Support Ticket Analysis

## Subject
Probleme mit Node tg080 auf dem TinyGPU Cluster

## Keywords
- RTX 3080 Node
- TinyGPU Cluster
- Job Delay
- Error Log
- PATH Environment Variable
- dirname Command
- Job Abortion
- Node Restart

## Problem Description
- **Node**: tg080 (RTX 3080) on TinyGPU Cluster
- **Issue**: Jobs experiencing significant delays and abortions
- **Error Log**: Repeated messages indicating `dirname` command not found due to missing PATH environment variable
- **Affected Job IDs**: 528834, 528838
- **Comparison**: Node tg082 functioning normally

## Root Cause
- Missing or incorrect PATH environment variable configuration leading to `dirname` command not being found

## Solution
- **Action Taken**: HPC Admin restarted the node tg080
- **Result**: Batch jobs started functioning again

## General Learnings
- Ensure PATH environment variable is correctly set to include essential directories (e.g., `/usr/bin`, `/bin`)
- Node restarts can resolve transient issues related to environment variables and job execution
- Monitor error logs for recurring patterns that may indicate configuration issues

## Next Steps
- Verify PATH configuration on other nodes to prevent similar issues
- Monitor node tg080 for any recurring problems
- Document the resolution for future reference in case of similar incidents
---

### 2022030842001805_Early-Alex%20%22Mikhail%20Kulyabin%22%20_%20iwi5063h.md
# Ticket 2022030842001805

 ```markdown
# HPC Support Ticket Analysis

## Subject
Early-Alex "Mikhail Kulyabin" / iwi5063h

## Keywords
- HPC Account
- GPU Utilization
- Pytorch Module
- Miniconda3
- BigGAN
- BigDatasetGAN
- GPU Hours

## Summary
- **Initial Request**: User requested access to the GPGPU cluster 'Alex' for training neural networks (BigGAN and BigDatasetGAN) as part of a master thesis.
- **Software Requirements**: Miniconda3 with a virtual environment for Pytorch.
- **Resource Allocation**: Initially requested ~100 GPU hours but ended up using almost 1.700 A100 hours.

## Issues
- **Low GPU Utilization**: Jobs had close to zero GPU utilization.
- **Resource Misuse**: User exceeded the initially requested GPU hours significantly.

## Actions Taken
- **Account Enabled**: HPC Admin enabled the user's account on Alex and provided information about the available Pytorch module.
- **Permission Withdrawn**: Due to low GPU utilization and excessive resource usage, permission to use Alex was withdrawn.

## Lessons Learned
- **Monitoring Usage**: Importance of monitoring GPU utilization to ensure efficient resource allocation.
- **Resource Management**: Necessity of adhering to requested resource limits to prevent misuse.
- **User Preparedness**: Ensure users are ready to utilize Tier2 systems effectively before granting access.

## Root Cause
- **User Preparedness**: The user's jobs were not optimized for GPU usage, leading to low utilization and excessive resource consumption.

## Solution
- **Withdraw Permission**: Permission to use Alex was withdrawn to prevent further misuse of resources.
- **User Training**: Recommend additional training or support to ensure users are prepared to effectively utilize HPC resources.
```
---

### 2024080442000042_Tier3-Access-Alex%20%22Azhar%20Hussian%22%20_%20iwi5197h.md
# Ticket 2024080442000042

 # HPC Support Ticket Analysis

## Keywords
- HPC Account
- GPGPU Cluster 'Alex'
- Nvidia A100 GPUs
- Python, PyTorch
- Batch Size
- Distributed Training
- GPU Availability
- Thesis Work
- Publication

## Summary
A user requested access to the GPGPU cluster 'Alex' for their thesis work, requiring significant GPU resources for distributed training. The user faced issues with GPU availability due to high demand.

## Root Cause of the Problem
- **GPU Availability**: The user needed access to multiple A100 GPUs for distributed training but found them frequently occupied.

## Solution
- **Account Enabled**: The HPC Admin enabled the user's account on Alex, allowing them to access the required resources.

## General Learnings
- **Resource Allocation**: Understanding the demand for high-performance computing resources and managing their allocation efficiently.
- **User Requirements**: Identifying and addressing specific user needs, such as software requirements (Python, PyTorch) and computational resources for research and thesis work.
- **Communication**: Effective communication between users and HPC Admins to ensure that resources are allocated appropriately and users are informed about the status of their requests.

## Next Steps
- **Monitor GPU Usage**: Continuously monitor the usage of GPUs to ensure fair distribution and availability.
- **User Support**: Provide ongoing support to users, especially those working on critical projects like thesis work, to ensure they have the resources they need.

---

This analysis can help support employees understand common issues related to GPU availability and resource allocation, ensuring better management and support for users in the future.
---

### 2024082142001456_Jobs%20on%20Alex%20GPU%2C%20not%20being%20utilized%20-%20b216dc13.md
# Ticket 2024082142001456

 # HPC Support Ticket: Jobs on Alex GPU Not Being Utilized

## Keywords
- GPU utilization
- Job monitoring
- ClusterCockpit
- `nvidia-smi`
- Resource allocation

## Problem
- User's jobs on Alex GPU nodes are not utilizing the allocated GPUs.
- JobIDs mentioned: 2013863, 2013862, 2013864.

## Root Cause
- The user's code or application running on the allocated nodes is not configured to use the available GPUs.

## Solution
1. **Monitor Job Utilization:**
   - Use ClusterCockpit for job monitoring: [ClusterCockpit Login](https://monitoring.nhr.fau.de/)
   - Login instructions: [Job Monitoring with ClusterCockpit](https://doc.nhr.fau.de/job-monitoring-with-clustercockpit/)

2. **Check GPU Utilization:**
   - Attach to the running job using:
     ```bash
     srun --pty --overlap --jobid YOUR-JOBID bash
     ```
   - Run `nvidia-smi` to check GPU utilization.

3. **Optimize Resource Allocation:**
   - Ensure that the code or application is configured to use GPUs.
   - Allocate GPU nodes only if the job can utilize the GPU resources to avoid idle resources.

## General Learning
- Always verify that jobs allocated to GPU nodes are actually utilizing the GPUs.
- Use monitoring tools and commands like `nvidia-smi` to check resource utilization.
- Proper resource allocation helps in efficient use of HPC resources and avoids wastage.

## Contact
For further assistance, contact the HPC support team at [support-hpc@fau.de](mailto:support-hpc@fau.de).
---

### 2022110742000632_AMBER%20pmemd.cuda_DPFP-Jobs%20auf%20Alex%20-%20mfbi05.md
# Ticket 2022110742000632

 # HPC Support Ticket: AMBER pmemd.cuda_DPFP Jobs on Alex

## Keywords
- AMBER
- pmemd.cuda_DPFP
- A100 GPUs
- A40 GPUs
- Double Precision (DP)
- Performance Optimization

## Summary
- **User Issue**: Running AMBER jobs with `pmemd.cuda_DPFP` on A40 GPUs instead of A100 GPUs.
- **Root Cause**: User was unaware of the significant performance difference between A40 and A100 GPUs for double precision calculations.
- **Solution**: Recommended to run `pmemd.cuda_DPFP` jobs on A100 GPUs for better performance.

## Details
- **HPC Admin**: Noticed multiple AMBER jobs using `pmemd.cuda_DPFP` on A40 GPUs.
- **User Response**: Confirmed the use of A40 GPUs due to the assumption that A100 GPUs were occupied by higher-priority users.
- **HPC Admin**: Clarified that `pmemd.cuda_DPFP` jobs should be run on A100 GPUs for a significant speed improvement (up to 10x faster).
- **User Agreement**: Agreed to switch to A100 GPUs for future `pmemd.cuda_DPFP` jobs.

## Lessons Learned
- **Performance Optimization**: A100 GPUs offer much better performance for double precision calculations compared to A40 GPUs.
- **Resource Allocation**: Users should be aware of the appropriate hardware for their specific job requirements to optimize resource usage and job efficiency.

## Recommendations
- **User Education**: Inform users about the performance benefits of different GPU types for specific job requirements.
- **Resource Monitoring**: Continuously monitor job performance and provide recommendations for optimization.

## Conclusion
- **Action Taken**: User agreed to switch to A100 GPUs for `pmemd.cuda_DPFP` jobs.
- **Outcome**: Improved job performance and efficient use of HPC resources.
---

### 2022120842002351_Tier3-Access-Alex%20%22Kishor%20Kayyar%20Lakshminarayana%22%20_%20iwal038h.md
# Ticket 2022120842002351

 ```markdown
# HPC Support Ticket Analysis

## Subject
Tier3-Access-Alex / iwal038h

## Keywords
- HPC Account
- Access Request
- GPGPU Cluster
- Nvidia A100
- CUDA
- Text-to-Speech Research
- Certificate Expiration

## Summary
- **User Request**: Access to GPGPU cluster 'Alex' for research on Text-to-Speech.
- **Required Resources**: Nvidia A100 GPUs, CUDA 11.x.
- **Expected Outcome**: Run synthesis experiments and publish results.

## Issue
- **Root Cause**: Certificate expiration.
- **Solution**: HPC Admin enabled the user's HPC account on Alex.

## Lessons Learned
- Regularly check and renew certificates to avoid access issues.
- Ensure proper communication with users regarding account status and requirements.
- Maintain up-to-date software versions (e.g., CUDA) as per user needs.

## Actions Taken
- HPC Admin enabled the user's account after addressing the certificate expiration issue.

## Recommendations
- Implement automated reminders for certificate renewals.
- Provide clear guidelines for users on requesting access and required resources.
- Ensure timely updates and support for software tools needed by researchers.
```
---

### 2022021742001648_Job%20auf%20TinyGPU%20nutzt%20nur%20eine%20GPU%20%5Bbccc007h%5D.md
# Ticket 2022021742001648

 ```markdown
# HPC Support Ticket: Job auf TinyGPU nutzt nur eine GPU

## Keywords
- TinyGPU
- JobID 631697
- GPU allocation
- Cluster monitoring

## Problem Description
A job on TinyGPU (JobID 631697) is using only one GPU instead of the allocated four GPUs.

## Root Cause
The exact root cause is not specified in the conversation, but it is implied that there might be an issue with the job configuration or resource allocation.

## Solution
No specific solution is provided in the conversation. Further investigation is required to determine the cause and resolve the issue.

## What Can Be Learned
- **Monitoring Tools**: Use cluster monitoring tools to verify resource allocation and usage.
- **Job Configuration**: Ensure that job scripts are correctly configured to utilize all allocated resources.
- **Communication**: Inform users promptly about any discrepancies in resource usage.

## Next Steps
- **Investigation**: Further investigate the job configuration and resource allocation settings.
- **User Communication**: Provide the user with steps to check and correct their job script.
- **Documentation**: Update documentation on proper job script configuration for GPU usage.
```
---

### 2022102042000921_Tier3-Access-Alex%20%22Philipp%20Pelz%22%20_%20op37elil%40fau.de.md
# Ticket 2022102042000921

 # HPC Support Ticket Analysis: Tier3-Access-Alex

## Keywords
- GPGPU Cluster Alex
- NHR-Testprojekt
- SSH-Keys
- Slurm-Option
- A100 GPGPUs
- A40 GPGPUs
- Python 3.9
- PyTorch 1.12
- Large-scale phase-contrast reconstructions

## Summary
A user requested access to the GPGPU cluster 'Alex' for a project involving large-scale phase-contrast reconstructions. The user initially faced issues logging in with their provided credentials.

## Root Cause of the Problem
- The user attempted to log in with the wrong username (`op37elil` instead of `b151dc10`).

## Solution
- The HPC Admin advised the user to log in using the correct username (`b151dc10`) and SSH-Keys.
- The user was also informed about Slurm options for requesting specific GPU types to avoid unnecessary wait times.

## General Learnings
- Always ensure users are aware of the correct login credentials and procedures.
- Provide clear instructions on how to request specific resources to optimize job scheduling.
- Understand the user's computational needs and provide appropriate resources and software versions (e.g., Python 3.9, PyTorch 1.12).

## Additional Notes
- The user's project involves running 50 reconstructions, each requiring 30 consecutive runs, totaling 3000 GPU-hours.
- The project aims to establish large-scale phase-contrast reconstructions in 3D at atomic resolution.
- The user was advised not to request specific A100 types to avoid unnecessary wait times but was given Slurm options for specific needs.
---

### 2022051142000681_Tier3-Access-Alex%20%22Altan%22%20_%20i%20w%20a%20l%200%208%208%20h.md
# Ticket 2022051142000681

 # HPC Support Ticket Analysis

## Keywords
- **Access Request**
- **Resource Availability**
- **Project Affiliation**
- **Compute Time Proposal**
- **Acknowledgment**

## Summary
- **User Request**: Access to GPGPU cluster 'Alex' for a Fraunhofer project involving AI and deep learning.
- **Initial Response**: Alex is an FAU and NHR resource, not available for Fraunhofer projects. Suggested using TinyGPU instead.
- **User Clarification**: User is part of a joint FAU and Fraunhofer group (AudioLabs).
- **Final Resolution**: User's account enabled on Alex with instructions to acknowledge the correct affiliation and limitations on GPU usage.

## Root Cause
- User did not initially specify their joint affiliation with FAU, leading to confusion about resource availability.

## Solution
- User clarified their affiliation with a joint FAU and Fraunhofer group.
- HPC Admin enabled the user's account on Alex with specific instructions for acknowledgment and resource usage limits.

## General Learnings
- **Resource Eligibility**: Understand the eligibility criteria for different HPC resources.
- **Affiliation Clarification**: Ensure users clearly state their project affiliations to avoid misunderstandings.
- **Acknowledgment Guidelines**: Provide clear instructions for acknowledging resource usage.
- **Compute Time Proposals**: Inform users about the process for requesting additional compute time if needed.

## Action Items
- **Users**: Clearly state project affiliations in access requests.
- **HPC Admins**: Verify user affiliations and provide specific instructions for resource usage and acknowledgment.

---

This analysis can help support employees understand the importance of clear communication regarding project affiliations and resource eligibility criteria.
---

### 2025022442001334_GPU%20is%20not%20used%20-%20b180dc19.md
# Ticket 2025022442001334

 # HPC Support Ticket: GPU Not Used

## Keywords
- GPU utilization
- Job monitoring
- ClusterCockpit
- `srun`
- `nvidia-smi`

## Problem
- User's job on the HPC cluster was not utilizing the GPU.

## Root Cause
- The user did not ensure efficient use of GPU resources in their job.

## Solution
- **Monitoring Job:**
  - Use ClusterCockpit: [Monitoring Link](https://monitoring.nhr.fau.de/)
  - Attach to running job using `srun`:
    ```bash
    srun --pty --overlap --jobid YOUR-JOBID bash
    ```
  - Check GPU utilization with `nvidia-smi`.

## General Learnings
- Always ensure efficient use of GPU resources.
- Utilize monitoring tools like ClusterCockpit to track job performance.
- Use `srun` to attach to running jobs and `nvidia-smi` to check GPU usage.

## Ticket Closure
- Ticket closed as no new issues were reported within a week.

## Contact
- For further assistance, contact HPC support: [support-hpc@fau.de](mailto:support-hpc@fau.de)
- HPC website: [HPC FAU](https://hpc.fau.de/)
---

### 2024062842001929_Tier3-Access-Alex%20%22Kubilay%20Can%20Demir%22%20_%20iwb9001h.md
# Ticket 2024062842001929

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Keywords
- HPC Account Activation
- GPU Utilization
- Job Monitoring
- ClusterCockpit
- GPGPU Cluster 'Alex'
- Nvidia A100 GPGPUs
- GPU-hours
- Gemma 2 Language Model
- Synthetic Dataset Generation
- Surgical Phase Recognition
- OpenAI API Costs

## Summary
- **Account Activation**: The user's HPC account was enabled on the Alex cluster.
- **GPU Utilization**: The HPC Admin noted that there is room for improving GPU utilization based on recent job performance on TinyGPU, as observed in ClusterCockpit.
- **Resource Request**: The user requested access to the GPGPU cluster 'Alex' with Nvidia A100 GPGPUs for generating synthetic datasets for their PhD topic on surgical phase recognition.
- **Software Requirement**: The user intended to use the Gemma 2 language model, which fits into a single A100 80 GB GPU at full precision.
- **Expected Outcomes**: The user aimed to generate synthetic data similar to real recordings using language models, comparing the performance of Gemma 2 with OpenAI's GPT models.

## Root Cause of the Problem
- **GPU Utilization**: The user's jobs on TinyGPU showed suboptimal GPU utilization, indicating potential inefficiencies in job configuration or resource allocation.

## Solution
- **Improve GPU Utilization**: The HPC Admin suggested reviewing job performance in ClusterCockpit to identify areas for improvement in GPU utilization.

## General Learnings
- **Monitoring Tools**: Use ClusterCockpit for job monitoring and performance analysis.
- **Resource Optimization**: Regularly review job performance to optimize resource utilization.
- **Software Requirements**: Ensure that the requested software is compatible with the available hardware resources.
```
---

### 2022020442001234_Job%20makes%20no%20use%20of%20GPU%20%5Biwal072h%5D.md
# Ticket 2022020442001234

 # HPC Support Ticket: Job Makes No Use of GPU

## Keywords
- GPU utilization
- Resource waste
- TinyGPU cluster
- Monitoring system

## Summary
A user was running a job on the TinyGPU cluster that did not utilize the GPU, leading to a waste of resources.

## Root Cause
- The user requested a GPU for a job that did not make use of it.

## Solution
- Ensure that jobs requesting GPU resources are capable of utilizing the GPU.
- Monitor jobs to verify proper resource utilization.

## Lessons Learned
- Always verify that jobs requesting specific resources (e.g., GPUs) are configured to use them.
- Regular monitoring of resource utilization can help identify and address inefficiencies.

## Actions Taken
- The HPC Admin notified the user about the issue and provided a screenshot from the monitoring system.
- The ticket was closed with the expectation that the user would address the issue.

## Recommendations
- Educate users on proper resource allocation and utilization.
- Implement automated checks or alerts for underutilized resources.

---

This documentation can help support employees identify and resolve similar issues related to resource utilization on the HPC cluster.
---

### 2024100342001351_TinyGPU%20-%20Jobs%20starten%20nicht%20korrekt.md
# Ticket 2024100342001351

 # HPC-Support Ticket: TinyGPU - Jobs starten nicht korrekt

## Summary
- **Subject:** TinyGPU - Jobs starten nicht korrekt
- **User Issue:** Jobs on TinyGPU cluster with A100 GPUs start but do not progress beyond initial log output.
- **Keywords:** TinyGPU, A100, GPU, Job, Log, NVIDIA-SMI, CUDA, Memory-Usage, GPU-Util

## Details
- **User Log:**
  ```
  ### Starting TaskPrologue of job 903340 on tg097 at Thu 03 Oct 2024 03:23:42 PM CEST
  Running on cores 96-127 with governor ondemand
  Thu Oct  3 15:23:42 2024
  +
  ------
  --------------+
  | NVIDIA-SMI 560.28.03              Driver Version: 560.28.03      CUDA Version: 12.6     |
  |-----------------------------------------+------------------------+----------------------|
  | GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
  | Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
  |                                         |                        | MIG M. |
  |=========================================+========================+======================|
  |   0  NVIDIA A100-SXM4-40GB          On  |   00000000:C1:00.0 Off | 0 |
  | N/A   34C    P0             54W /  400W |       1MiB /  40960MiB |      0% Default |
  |                                         |                        | Disabled |
  +-----------------------------------------+------------------------+----------------------+
  +
  ------
  --------------+
  | Processes:
  |
  |  GPU   GI   CI        PID   Type   Process name GPU Memory |
  |        ID   ID Usage      |
  |
  ```

## Root Cause
- The job starts but does not progress, indicating a potential issue with GPU resource allocation or utilization.
- The NVIDIA-SMI output shows minimal GPU memory usage (1MiB) and 0% GPU utilization, suggesting the job is not effectively using the GPU.

## Solution
- **HPC Admins** should investigate the job script and resource allocation settings to ensure proper GPU utilization.
- Verify that the job is correctly requesting and utilizing the A100 GPU resources.
- Check for any potential software or driver issues that might prevent the job from accessing the GPU.

## Next Steps
- **HPC Admins** to review the job script and resource allocation.
- **2nd Level Support Team** to assist in troubleshooting GPU utilization issues.
- **Gehard Wellein** and **Georg Hager** to provide additional support and training if needed.
- **Harald Lanig** to ensure proper resource allocation for NHR Rechenzeit Support.
- **Jan Eitzinger** and **Gruber** to assist with any software or tool-related issues.

## Documentation
- This issue can serve as a reference for troubleshooting GPU utilization problems on the TinyGPU cluster.
- Ensure proper documentation of GPU resource allocation and utilization best practices.
---

### 2024070142001227_Long%20Job%20Pending.md
# Ticket 2024070142001227

 # HPC Support Ticket: Long Job Pending

## Keywords
- Long pending times
- AssocGrpGRES
- Resource limit
- GPU-hours
- Project quotas

## Problem Description
- User experiencing long pending times for jobs.
- Error message indicates resource limit for user group is reached (AssocGrpGRES).
- No jobs running by the user, but another student in the same project is active.

## Root Cause
- The project has a limited GPU-hour quota.
- Another user in the project is consuming a significant portion of the quota.
- The project has already exceeded its monthly GPU-hour allocation.

## Details
- Project ID: b209cb
- Total GPU-hour quota: 115,000 over 36 months (~3,285 GPU-h/month)
- Current usage: 3 out of 38 A100 nodes, with 3 jobs using 8 GPUs each (24 GPUs total)
- June usage: 9,496 GPU-h (exceeding the monthly allocation)

## Solution
- Monitor project usage and distribute resources accordingly.
- Communicate with the other user to manage job submissions and resource allocation.
- Consider requesting additional resources if the project consistently exceeds quotas.

## General Learnings
- Understand project quotas and resource limits.
- Coordinate with project members to manage resource usage.
- Regularly monitor job status and resource consumption.
- Communicate with HPC admins for quota adjustments or extensions.
---

### 2023022242002242_Tier3-Access-Alex%20%22Philipp%20Grundhuber%22%20_%20iwal115h.md
# Ticket 2023022242002242

 # HPC Support Ticket Analysis

## Keywords
- HPC Account Activation
- Certificate Expiration
- GPGPU Cluster 'Alex'
- Nvidia A100 GPUs
- Rechenzeit (Compute Time)
- Software Requirements (PyTorch Lightning, CNN, LSTM, RNN)
- Master Thesis Application
- Binaural Audio Processing

## Summary
- **User Request:** Access to GPGPU cluster 'Alex' for a master thesis project involving binaural audio processing.
- **Resources Requested:** 4 GPUs per job, 12 hours walltime per job, 100 jobs, totaling ~5000 GPU hours.
- **Software Needs:** PyTorch Lightning for CNN, LSTM, RNN training with Python and CUDA.
- **Application:** Learning spatial representation of binaural audio and applying it to unbinauralized audio.

## Root Cause of the Problem
- The user's certificate had expired, which required HPC Admin intervention.

## Solution
- HPC Admin activated the user's HPC account on the 'Alex' cluster.

## General Learnings
- Ensure certificates are up-to-date for seamless account activation.
- Properly document software and hardware requirements for efficient resource allocation.
- Communicate clearly with users about account status and next steps.

## Action Taken
- HPC Admin activated the user's account and notified the user via email.

## Future Reference
- For similar issues, check the status of the user's certificate and account activation.
- Verify resource requests and software requirements to ensure compatibility and availability.

---

This documentation can be used as a reference for future support tickets involving account activation, certificate issues, and resource allocation for specific projects.
---

### 2022092142000753_Regarding%20usage%20of%20julia.md
# Ticket 2022092142000753

 # HPC Support Ticket: Regarding Usage of Julia

## Keywords
- Julia
- Ubuntu18.04-Julia (gpu.large)
- TinyGPU
- Node sharing
- Root usage

## Problem
- User noticed 'root' using the machine for some tasks, which was not observed previously.
- Concern about whether the machine is assigned only to Human Genetics or if others can use it.

## Root Cause
- Misunderstanding about the machine name and usage policy.
- The machine in question is likely TinyGPU, which is shared among users if less than a full node is allocated.

## Solution
- Clarified that Julia is a programming language available to all users.
- Identified that the machine is likely TinyGPU and explained the node-sharing policy.
- Informed the user that other users might be running Julia at the same time if the node is not fully allocated.

## General Learning
- Always clarify the machine name and its usage policies.
- Understand that nodes can be shared among users if not fully allocated.
- Regularly check system usage to ensure resources are being utilized as expected.

## Ticket Closure
- The ticket was closed after the user acknowledged the information provided.
---

### 2018110542000921_Deep%20learning%20mit%20dem%20Emmy%20Cluster.md
# Ticket 2018110542000921

 # HPC-Support Ticket Conversation: Deep Learning with Emmy Cluster

## Keywords
- Deep Learning
- GPU Memory
- Job Laufzeit
- Checkpoint
- Emmy Cluster
- TinyGPU Cluster
- NVidia Tesla K20m
- NVidia GTX980, 1080, 1080Ti
- Batch-Modus
- Queueingsystem

## Problem
- User requires more than 5 GB GPU memory for deep learning models.
- Job runtime is limited to 24 hours, which is insufficient for training deep learning models.

## Root Cause
- Limited GPU memory on Emmy Cluster (NVidia Tesla K20m with 5 GB).
- Job runtime limitation of 24 hours.

## Solution
- **GPU Memory**:
  - Emmy Cluster only has NVidia Tesla K20m with 5 GB memory.
  - TinyGPU Cluster has consumer GPUs (NVidia GTX980, 1080, 1080Ti), but access to 1080Ti is restricted to shareholders.
  - GTX1080 with 8 GB memory is available but may not meet the 10 GB requirement.

- **Job Runtime**:
  - In exceptional cases, job runtime can be extended beyond 24 hours, but this is not a general solution.
  - Checkpoint-Restart is recommended for long-running jobs.

## General Learnings
- Understand the GPU configurations and access restrictions in different clusters.
- Be aware of job runtime limitations and the possibility of extensions in exceptional cases.
- Encourage users to implement Checkpoint-Restart for long-running jobs.

## Follow-up Actions
- Users should optimize their models to fit within available GPU memory.
- Consider requesting access to restricted GPUs if necessary.
- Implement Checkpoint-Restart for jobs exceeding 24 hours.
---

### 2022111042003221_Poor%20performance%20of%20Jobs%20on%20TinyGPU%20-%20iwi5040h.md
# Ticket 2022111042003221

 # HPC Support Ticket Analysis: Poor Performance of Jobs on TinyGPU

## Keywords
- Poor performance
- GPU utilization
- A100 nodes
- TinyGPU
- Job optimization

## Summary
- **Issue**: Jobs running on the A100 nodes of TinyGPU exhibit poor performance with an average GPU utilization of less than 8% and intermittent phases of zero utilization.
- **Root Cause**: Not explicitly stated, but likely related to inefficient job configuration or code optimization.
- **Solution**: HPC Admin suggests checking and increasing the performance of the jobs.

## Lessons Learned
- Regularly monitor GPU utilization to identify performance bottlenecks.
- Optimize job configurations and code to maximize GPU usage.
- Engage with users to provide guidance on improving job performance.

## Next Steps
- Users should review their job scripts and code for potential optimizations.
- HPC Admins can provide additional resources or workshops on efficient GPU usage.
- Continuous monitoring and performance tuning are essential for maintaining high GPU utilization.
---

### 2021102542002798_Slow%20running%20jobs.md
# Ticket 2021102542002798

 # Slow Running Jobs on A100 in Tinygpu

## Keywords
- Slow jobs
- A100
- Tinygpu
- Performance degradation
- Power throttling
- Power supply issue

## Problem Description
- User reported jobs that previously took 7 hours to train now taking over 130 hours.
- Issue observed on A100 nodes in Tinygpu.

## Root Cause
- A fuse has blown, causing one of the two power supplies of the nodes to lose power.
- GPUs are in a power throttling mode due to insufficient power supply.

## Solution
- Further on-site investigation is required to inspect the infrastructure.
- The Message of the Day (MOTD) on Woody will be updated with the issue status.

## Lessons Learned
- Performance degradation can be caused by hardware issues such as power supply problems.
- It is important to check the power supply and other hardware components when diagnosing performance issues.
- Communication with users about ongoing issues and their resolution is crucial.

## Actions Taken
- HPC Admin identified the root cause of the performance degradation.
- The ticket was closed, but the MOTD will be kept updated on the issue.

## Next Steps
- Conduct on-site inspection of the affected nodes.
- Resolve the power supply issue to restore normal performance.
- Update users through the MOTD on Woody about the resolution of the issue.
---

### 2023111542002999_Low%20utilization%20on%20A100%20GPUs%20%20of%20TinyGPU%20-%20nfcc010h.md
# Ticket 2023111542002999

 ```markdown
# Low Utilization on A100 GPUs

## Keywords
- Low GPU utilization
- A100 GPUs
- TensorFlow
- CPU bottleneck
- OPM threads

## Problem Description
- User's jobs on TinyGPU showed low utilization of A100 GPUs.
- The workflow involved generating data points for machine learning potentials.
- The admin suspected that the low utilization might be due to the nature of the tasks executed by the software.

## Root Cause
- The user's submission script had an error where the number of OPM threads was fixed to 1.
- This caused the CPU part of the job to take longer, resulting in the GPU being idle.

## Solution
- The user corrected the submission script to allow for more OPM threads, reducing the CPU bottleneck and improving GPU utilization.

## Lessons Learned
- Ensure that the number of threads for CPU-intensive tasks is optimized to prevent bottlenecks.
- Verify that the workload is balanced between CPU and GPU to maximize resource utilization.
- Regularly monitor job performance to identify and address inefficiencies.
```
---

### 2019011742000586_Re%3A%20%5BRRZE-HPC%5D%20%20Reminder%3A%20HPC%20Campustreffen%20-%20tomorrow%20-%20Thursday%2C%20Jan.md
# Ticket 2019011742000586

 # HPC Support Ticket Conversation Analysis

## Keywords
- HPC Campustreffen
- GPU-Cluster
- MD Simulationen
- TinyGPU
- Parallelisierung
- Cluster 2020
- LiMa Shutdown
- ARM
- NEC Tsubasa vector card
- HPC Services
- FAU
- RRZE
- Meggie

## General Learnings
- **User Preferences**: For molecular dynamics (MD) simulations, GPU-clusters are preferred due to better simulation time per Euro.
- **Hardware Configurations**:
  - Small systems: TinyGPU configuration is suitable.
  - Large systems: One GPU per node is recommended for better parallelization.
- **Meeting Agenda**:
  - Operational and usage topics.
  - Future of HPC at FAU.
  - Discussion of requirements for "Cluster 2020".
- **Usage Statistics**:
  - TinyGPU usage is low.
  - Meggie usage is high.

## Root Cause of the Problem
- **Low Usage of TinyGPU**: Despite being suitable for small systems, TinyGPU nodes are underutilized.

## Solution
- **Increase Awareness**: Promote the benefits and use cases of TinyGPU nodes to encourage more users to utilize them.
- **User Training**: Provide training sessions or documentation on how to effectively use TinyGPU for small-scale simulations.

## Additional Notes
- **Meeting Reminder**: Regular reminders and updates about HPC Campustreffen are sent to users.
- **Hardware Updates**: New hardware in RRZE's test cluster includes ARM and NEC Tsubasa vector cards.
- **Future Planning**: Discussions on the future of HPC at FAU and plans for "Cluster 2020" are ongoing.

This analysis can help support employees understand user preferences, hardware utilization, and future planning for HPC services at FAU.
---

### 2024062442002659_Alex%20jobs%20not%20using%20GPUs%20%5Bb197dc12%5D.md
# Ticket 2024062442002659

 # HPC Support Ticket: Alex Jobs Not Using GPUs

## Keywords
- GPU utilization
- Resource allocation
- Job monitoring
- ClusterCockpit
- `nvidia-smi`
- `srun`

## Problem Description
- User's jobs on Alex are not utilizing the allocated GPUs effectively.
- Previous jobs used no GPUs or only one out of the allocated four.

## Root Cause
- The user's code may not be configured to use the allocated GPUs.
- Incorrect resource allocation leading to idle GPUs.

## Solution
- **Monitoring Resource Utilization:**
  - Use ClusterCockpit at [monitoring.nhr.fau.de](https://monitoring.nhr.fau.de/).
  - Attach to the running job using `srun --pty --overlap --jobid YOUR-JOBID bash` and run `nvidia-smi` to check GPU utilization.

- **Correct Resource Allocation:**
  - Ensure that jobs only allocate nodes with GPUs if the code can utilize them.
  - Allocate the correct number of GPUs based on the job's requirements.

## Actions Taken
- HPC Admins terminated jobs that requested 4 GPUs but used at most one GPU.
- Provided guidance on monitoring and correct resource allocation.

## Additional Notes
- This is not the first instance of the user running jobs without proper GPU utilization.
- Encourage users to contact support for further assistance if needed.

## Contact Information
- HPC Support: [support-hpc@fau.de](mailto:support-hpc@fau.de)
- HPC Website: [hpc.fau.de](https://hpc.fau.de/)
---

### 2022012142001267_a100.md
# Ticket 2022012142001267

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject: a100

### User Issue:
- User's job is pending on SLURM for A100.
- Job shows pending due to `AssocGrpGRES`.
- User is a student working for Fraunhofer.

### Root Cause:
- High resource usage by other users in the same group (`iwal`).
- Limited availability of A100 GPUs.

### Key Points:
- AudioLabs/FHG financed two A100 GPUs with a total of 8 GPUs.
- `iwal` has jobs with a total of 12 A100 running, along with other GPUs.
- `iwal` accounts for over 37% of the total compute time.
- Priority of jobs is determined by recent compute time usage and wait time.

### User Questions:
- Why can other people from Fraunhofer use A100 but not the user?
- Is there a simple way to see all `iwal` jobs currently running or scheduled?

### HPC Admin Responses:
- Provided detailed information on current resource usage by `iwal`.
- Explained that `iwal` has a high compute time usage, making it the largest consumer.
- Mentioned that users should not complain about waiting jobs due to high resource availability.
- Informed that currently, users cannot self-query running or scheduled jobs for `iwal`.

### Solution:
- No immediate solution provided for the user's pending job.
- Users are advised to communicate internally to manage resource usage.

### Future Actions:
- Users may need to coordinate internally to optimize resource usage.
- HPC Admins will work on enabling self-querying of job statuses in the future.

### Keywords:
- SLURM, A100, AssocGrpGRES, Pending Jobs, Resource Usage, Compute Time, Job Priority, Internal Communication
```
---

### 2022051242000241_RE%3A%20HPC%20-%20question%20on%20speeding%20up%20computation.md
# Ticket 2022051242000241

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Key Points Learned

1. **Multi-GPU Training**:
   - The user had issues with running multi-GPU training on the `tinyGPU` cluster.
   - The user's script used `--nproc_per_node=8` which resulted in errors.
   - The solution involved removing `--nproc_per_node` and using `srun` before the Python command.

2. **SLURM Script Adjustments**:
   - The user needed to adjust the SLURM script to run on multiple GPUs.
   - The correct SLURM script parameters for multi-GPU training were provided by the HPC Admin.

3. **Alex Cluster Access**:
   - The user inquired about submitting jobs to the `Alex` cluster.
   - The user was informed about the process to gain access to the `Alex` cluster and the limitations of multi-node usage.

4. **Documentation and Support**:
   - The user was directed to various documentation and support resources, including the HPC Cafe and introductory sessions.
   - The user was advised to fill out an external form for access to the `Alex` cluster.

## Root Cause of the Problem

- The user's script had incorrect parameters for multi-GPU training, leading to CUDA memory errors.
- The user was unaware of the correct procedure to submit jobs to the `Alex` cluster.

## Solution

- The user was advised to remove `--nproc_per_node` and use `srun` before the Python command in the SLURM script.
- The user was informed about the process to gain access to the `Alex` cluster and the limitations of multi-node usage.
- The user was directed to relevant documentation and support resources for further assistance.

## Keywords

- Multi-GPU training
- SLURM script
- CUDA memory error
- Alex cluster access
- HPC documentation
- Support resources
```
---

### 2023121242000459_Job%20on%20Alex%20does%20not%20use%20GPU%20%5Bb116ba13%5D.md
# Ticket 2023121242000459

 # HPC Support Ticket: Job on Alex Does Not Use GPU

## Keywords
- GPU utilization
- Job allocation
- Monitoring system
- ClusterCockpit
- `nvidia-smi`
- Resource management

## Summary
A user's job on the Alex cluster was not utilizing all allocated GPUs, leading to resource wastage.

## Root Cause
The user's job was only using one out of eight allocated GPUs.

## Solution
1. **Monitoring GPU Utilization:**
   - The HPC Admin provided a screenshot from the monitoring system showing the underutilization.
   - Users can access the monitoring system via [ClusterCockpit](https://monitoring.nhr.fau.de/).

2. **Checking GPU Usage:**
   - Users can attach to their running job using the command:
     ```bash
     srun --pty --overlap --jobid YOUR-JOBID bash
     ```
   - Once attached, they can run `nvidia-smi` to check the current GPU utilization.

3. **Resource Allocation:**
   - Ensure that jobs only allocate nodes with GPUs if the code can actually utilize them.
   - Avoid idle resources by properly managing job allocations.

## General Learnings
- Regularly monitor job performance to ensure efficient resource utilization.
- Use monitoring tools and commands to diagnose and resolve resource allocation issues.
- Proper resource management is crucial to avoid wastage and ensure fair usage among users.

## Follow-Up
- The ticket was closed as subsequent jobs were utilizing the GPUs correctly.
- For further assistance, users can contact the HPC support team.
---

### 2024070142001521_Tier3-Access-Alex%20%22Chengze%20Ye%22%20_%20iwi5166h.md
# Ticket 2024070142001521

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject: Tier3-Access-Alex

### Keywords:
- Tier3 Access
- Alex Cluster
- Nvidia A100 GPGPUs
- Nvidia A40 GPGPUs
- Pyronn Software
- CT Trajectory Filters
- GPU Hours

### Summary:
- **User Request:** Access to the Alex cluster for developing CT trajectory-specific filters using Pyronn software.
- **Resources Requested:**
  - 1000 GPU hours
  - Nvidia A100 GPGPUs (9.7 TFlop/s double precision)
  - Nvidia A40 GPGPUs (48 GB, 37 TFlop/s single precision)
- **Expected Outcome:** Journal papers

### HPC Admin Response:
- **Action:** Access granted to use Alex cluster.
- **Contact Information:** Provided contact details for further support.

### Learnings:
- **Access Granting Process:** Understanding the procedure for granting access to specific HPC resources.
- **Resource Allocation:** How to handle requests for specific hardware resources and software.
- **Communication:** Importance of clear communication regarding access permissions and contact information.

### Root Cause of the Problem:
- User needed access to specific HPC resources for research purposes.

### Solution:
- HPC Admin granted access to the requested resources and provided contact information for further assistance.
```
---

### 2022052042000977_Tier3-Access-Alex%20%22Ronak%20Kosti%22%20_%20iwi5066h.md
# Ticket 2022052042000977

 ```markdown
# HPC Support Ticket Conversation Analysis

## Subject: Tier3-Access-Alex "Ronak Kosti" / iwi5066h

### Keywords:
- HPC Account Activation
- GPGPU Cluster 'Alex'
- Nvidia A100, A40 GPUs
- PyTorch, Python, CUDA, Jupyter Notebook, Gradio
- Generative Models (VQGAN, BigGAN, DALL-E2, CLIP, Diffusion models)
- Digital Visual Cultural Heritage
- Art History

### Summary:
- **User Request:** Access to GPGPU cluster 'Alex' for training large generative models on a dataset of 3.5 million images.
- **Required Software:** PyTorch, Python, CUDA libraries, Jupyter Notebook, Gradio.
- **Expected Outcomes:** Generating visual representations, integrating deep generative models into image analysis, and making research outcomes available for further dissemination.

### Problem:
- Certificate expiration issue mentioned by HPC Admin.

### Solution:
- HPC Admin enabled the user's HPC account on Alex.

### Lessons Learned:
- **Account Activation:** Ensure certificates are up-to-date for seamless account activation.
- **Resource Allocation:** Understand user requirements for GPU resources and software dependencies.
- **Research Applications:** HPC resources can be utilized for complex tasks like training generative models in art history research.

### Follow-up Actions:
- Verify certificate validity for new account requests.
- Ensure required software is pre-installed or easily accessible for users.
- Document user requirements and expected outcomes for future reference.
```
---

### 2025022742000615_GPUs%20allocated%20but%20not%20utilized%20-%20b129dc21.md
# Ticket 2025022742000615

 # HPC Support Ticket: GPUs Allocated but Not Utilized

## Keywords
- GPU utilization
- Resource allocation
- `nvidia-smi`
- `srun`
- JobID
- Idle resources

## Summary
The user was allocating GPUs for jobs but not fully utilizing them, leading to idle resources that could not be used by others.

## Problem
- **Root Cause:** The user's jobs were allocated GPUs, but the code was not making full use of these resources.
- **JobIDs:** 2413865, 2428451

## Solution
1. **Check GPU Utilization:**
   - Attach to the running job using:
     ```
     srun --pty --overlap --jobid YOUR-JOBID bash
     ```
   - Run `nvidia-smi` to check the current GPU utilization.

2. **Optimize Resource Allocation:**
   - Ensure that nodes with GPUs are only allocated if the code can actually make use of the GPU.
   - Adjust resource requests to match the actual needs of the job to prevent GPUs from remaining idle.

## General Learning
- Always verify that allocated resources are being utilized effectively.
- Use monitoring tools like `nvidia-smi` to check resource utilization.
- Proper resource allocation helps in efficient use of HPC resources and prevents idle time.

## Contact
For further assistance, contact the HPC support team at [support-hpc@fau.de](mailto:support-hpc@fau.de).
---

### 2021012042000431_Job%20auf%20TinyGPU%3A%20gtx980%20in%20Developer-Queue%20%5Bmpt2007h%5D.md
# Ticket 2021012042000431

 ```markdown
# HPC-Support Ticket: Job auf TinyGPU: gtx980 in Developer-Queue

## Keywords
- TinyGPU
- Developer-Queue
- gtx980
- GPU
- Job Submission
- Cluster
- Hardware Deprecation

## Summary
A user submitted a job to the Developer-Queue on the TinyGPU cluster, specifically requesting gtx980 GPUs.

## Root Cause
The gtx980 GPUs were decommissioned from the TinyGPU cluster at the end of December 2020.

## Solution
The user was informed that the gtx980 GPUs are no longer available. No further action was required from the user's side.

## General Learning
- **Hardware Deprecation**: Be aware of hardware updates and deprecations in the cluster.
- **Job Submission**: Ensure that job submissions are compatible with the current hardware available in the cluster.
- **Communication**: Inform users promptly about any changes in hardware availability to avoid job submission issues.
```
---

### 2022120142002041_Tier3-Access-Alex%20%22Emanu%C3%83%C2%ABl%20Habets%22%20_%20iwal01.md
# Ticket 2022120142002041

 # HPC Support Ticket: Tier3-Access-Alex

## Keywords
- HPC Account Activation
- GPGPU Cluster 'Alex'
- Nvidia A100 GPUs
- Python + PyTorch
- Speech Enhancement Lecture
- Fraunhofer IIS

## Summary
- **User Request**: Access to GPGPU cluster 'Alex' with Nvidia A100 GPUs for training and evaluating models for a "Speech Enhancement" lecture.
- **Resources Requested**: 1000 GPU hours (max 2 GPUs at a time).
- **Software Needed**: Python + PyTorch.
- **Expected Outcome**: New material for the "Speech Enhancement" lecture.
- **Additional Notes**: User is a member of AudioLabs and requests access to eight A100 GPUs bought by Fraunhofer IIS.

## Issue
- **Root Cause**: User needed access to the HPC account on the 'Alex' cluster.

## Solution
- **Action Taken**: HPC Admin activated the user's HPC account on the 'Alex' cluster.
- **Outcome**: User confirmed receipt of access and expressed gratitude.

## General Learnings
- **Process**: Ensure proper communication and confirmation when activating user accounts.
- **Documentation**: Maintain clear records of user requests and actions taken for future reference.
- **Collaboration**: Coordinate with joint institutions (e.g., Fraunhofer IIS) for resource allocation and access.

## Next Steps
- **Follow-up**: Monitor user activity to ensure smooth operation and provide additional support if needed.
- **Documentation**: Update internal documentation with any new processes or requirements discovered during this interaction.
---

### 2022112942002661_AssocGrpGRES.md
# Ticket 2022112942002661

 # HPC Support Ticket: AssocGrpGRES

## Keywords
- AssocGrpGRES
- GPU limits
- Slurm
- A100 GPUs
- A40 GPUs
- Job limits
- Resource allocation

## Problem
- User encountered the AssocGrpGRES limit while running multiple parallel jobs.
- Noticed unused A100 GPUs via `sinfo`.
- Attempted to bypass the limit using the `--killable` flag, but the feature was not available.

## Root Cause
- The user's project had reached its allocated GPU limit (AssocGrpGRES).

## Solution
- HPC Admin increased the A40 GPU limit for the user's project (b132dc).

## Additional Information
- The user requested a further increase in the A40 GPU limit during the summer period when the cluster is relatively empty.
- HPC Admin noted that the user's project had not utilized its allocated resources efficiently, with a significant portion of GPU hours remaining unused.

## What Can Be Learned
- Users may encounter resource limits (AssocGrpGRES) when running many parallel jobs.
- The `--killable` flag is not available on all systems to bypass these limits.
- HPC Admins can adjust resource limits for projects upon request.
- Efficient use of allocated resources is important, and HPC Admins may consider usage patterns when adjusting limits.

## Follow-up Actions
- Users should monitor their resource usage and request adjustments as needed.
- HPC Admins should review resource allocation and usage patterns to ensure fair and efficient use of the cluster.
---

### 2019062642001684_Emmy%20GPUs.md
# Ticket 2019062642001684

 ```markdown
# HPC-Support Ticket: Emmy GPUs

## Subject
- User requires access to older GPU models for benchmarking.
- ECC needs to be disabled on Emmy GPUs for accurate benchmarking.
- Profiling permissions issue on Emmy GPUs.

## Keywords
- GPU Benchmarking
- ECC Configuration
- Profiling Permissions
- CUDA Version
- NVIDIA Driver

## Problem Description
- User needs to compare benchmarks with older GPU models (C1060, C2050, K10) but lacks access.
- ECC is enabled on Emmy GPUs, affecting benchmark accuracy.
- User cannot profile on Emmy GPUs due to permission issues.

## Root Cause
- ECC is enabled on Emmy GPUs, which differs from the benchmarks in the literature.
- Profiling permissions have changed with newer NVIDIA drivers, requiring specific kernel module options.

## Solutions
- **ECC Configuration**:
  - Command to allocate a node with ECC disabled: `qsub -lnodes=e1165:ppn=40:k20m2x`
  - Steps to disable ECC:
    ```bash
    nvidia-smi --ecc-config=0 && reboot
    ```
  - Steps to enable ECC:
    ```bash
    nvidia-smi --ecc-config=1 && reboot
    ```

- **Profiling Permissions**:
  - Update kernel module options:
    ```bash
    options nvidia "NVreg_RestrictProfilingToAdminUsers=0"
    ```
  - Manual driver loading for immediate fix.

- **Older GPU Models**:
  - Potential availability of older GPU models (C2050/C070/C2075) but requires user setup.

## Additional Notes
- Profiling issues on TinyGPU and PizDaint may be related to driver versions and CUDA updates.
- Testing with different CUDA versions and GPUs did not resolve profiling errors.
- Potential hardware issue on TinyGPU node `tg071`.

## Conclusion
- ECC configuration and profiling permissions were successfully addressed.
- Older GPU models may be available but require user setup.
- Profiling issues on TinyGPU and PizDaint require further investigation.
```
---

### 2020100242003108_pmemd%20auf%20Emmy%20-%20bco123.md
# Ticket 2020100242003108

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Keywords
- Amber/pmemd
- Emmy
- GPU
- TinyGPU
- Benchmarks
- CPU Jobs
- GPU Jobs
- RTX 2080 Ti
- New GPU Knoten

## Summary
- **User Issue**: The user was running Amber/pmemd simulations on Emmy using 8 CPU nodes.
- **HPC Admin Suggestion**: The admin suggested that using GPUs, even older ones, would be significantly faster than using 8 CPU nodes on Emmy.
- **Benchmarks**: The admin provided benchmark data showing the performance difference between CPU nodes and various GPUs.
- **User Response**: The user acknowledged the performance difference and planned to finish the current CPU jobs but would use GPUs for future standard MD runs.
- **New GPU Knoten**: The admin mentioned that new GPU nodes with Geforce RTX3080 are on order and expected to be available by the end of November.

## Root Cause
- The user was unaware of the significant performance advantage of GPUs over CPUs for Amber/pmemd simulations.

## Solution
- The user was advised to use GPUs for future simulations and was informed about the upcoming availability of new GPU nodes.

## General Learnings
- GPUs are generally much faster than CPUs for molecular dynamics simulations using Amber/pmemd.
- Benchmarking can help users understand the performance differences between different hardware options.
- The HPC center is continuously upgrading its hardware to provide better performance for users.
```
---

### 2022072142001471_Job%20auf%20Alex%20nutzt%20die%20GPU%20nicht%20%5Bbccc034h%5D.md
# Ticket 2022072142001471

 ```markdown
# HPC Support Ticket: Job auf Alex nutzt die GPU nicht [bccc034h]

## Keywords
- GPU utilization
- Job monitoring
- SSH
- nvidia-smi
- Job resubmission

## Problem Description
- User's job with ID 364578 on Alex is not utilizing the GPU.
- The cause of the issue is not clear from the HPC admin's perspective.

## Diagnostic Steps
- HPC Admin provided a screenshot from the system monitoring.
- User was instructed to log in to the compute node (a0223) using SSH and check GPU utilization with `nvidia-smi`.

## Solution
- HPC Admin suggested resubmitting the job to determine if the issue was specific to the compute node.
- User resubmitted the job, and it started functioning correctly.

## Lessons Learned
- Sometimes, job issues can be resolved by simply resubmitting the job.
- Monitoring GPU utilization using `nvidia-smi` can help diagnose job performance issues.
- SSH access to compute nodes is essential for detailed job monitoring and troubleshooting.
```
---

### 2024071142003331_Tier3-Access-Alex%20%22Pooja%20Shetty%22%20_%20iwi5192h.md
# Ticket 2024071142003331

 ```markdown
# HPC Support Ticket Conversation Analysis

## Subject: Tier3-Access-Alex "Pooja Shetty" / iwi5192h

### Keywords:
- HPC Account Activation
- GPGPU Cluster 'Alex'
- Nvidia A40 GPGPUs
- Deep Learning Model Training
- Memory Issues
- Master Thesis

### Summary:
- **User Request:** Access to GPGPU cluster 'Alex' for training a deep learning model as part of a master thesis.
- **Issue:** Current tinygpu cluster is insufficient; user experiences memory issues (`torch.cuda.OutOfMemoryError`).
- **Solution:** HPC account enabled on Alex.

### Root Cause:
- Insufficient GPU resources on the current tinygpu cluster leading to memory errors during deep learning model training.

### Solution:
- HPC Admin enabled the user's account on the GPGPU cluster 'Alex' to provide access to more powerful GPUs.

### General Learnings:
- Users may require access to more powerful GPU resources for memory-intensive tasks like deep learning model training.
- HPC Admins can enable access to specific clusters to resolve resource limitations.
- Important to consider project deadlines and urgency when handling support requests.
```
---

### 2024080542004215_Problem%3A%20Job%201935509%20%28alex%29%20nutzt%20nur%202%20von%208%20GPUs%20%5Bb180dc36%5D.md
# Ticket 2024080542004215

 ```markdown
# HPC Support Ticket: Job 1935509 (alex) nutzt nur 2 von 8 GPUs

## Keywords
- JobID 1935509
- GPU utilization
- Monitoring system
- ClusterCockpit
- nvidia-smi
- A100 GPUs
- A40 GPUs

## Problem Description
A job (JobID 1935509) on the HPC system is only utilizing 2 out of the 8 requested GPUs.

## Root Cause
The job is not efficiently utilizing the allocated GPU resources.

## Solution
1. **Monitoring GPU Utilization:**
   - Use the monitoring system ClusterCockpit to view GPU utilization.
   - Alternatively, attach to the running job using `srun --pty --overlap --jobid YOUR-JOBID bash` and check GPU usage with `nvidia-smi`.

2. **Resource Allocation:**
   - Ensure that the job code is capable of utilizing the requested GPUs.
   - Consider whether A100 GPUs with 80GB are necessary or if A40 GPUs would suffice for the job.

## Additional Notes
- **Efficient Resource Use:**
  - Only request GPU nodes if the job can effectively use them.
  - Unused resources should be avoided to maximize system efficiency.

## Closure
The ticket was closed due to no response from the user.
```
---

### 2022013142003022_Available%20RAM%20on%20different%20systems.md
# Ticket 2022013142003022

 # HPC Support Ticket: Available RAM on Different Systems

## Keywords
- RAM availability
- GPU allocation
- TinyGPU cluster
- Memory allocation
- Documentation

## Problem
- User needs to know the available RAM when running jobs on different clusters or partitions to prevent NFS file systems from being overloaded and to optimize job performance.
- User experiences insufficient RAM (22GB) when requesting one GPU on TinyGPU, leading to job failures due to Out of Memory (OOM) errors.
- User seeks documentation or an overview of available RAM to determine if the "store-all-data-in-RAM" approach will work for their dataset size.

## Root Cause
- Lack of clear documentation on RAM allocation per GPU in different partitions.
- Misunderstanding of how RAM is allocated based on the number of GPUs requested.

## Solution
- **HPC Admin** provided a link to the TinyGPU documentation: [TinyGPU Cluster Documentation](https://hpc.fau.de/systems-services/systems-documentation-instructions/clusters/tinygpu-cluster/).
- Clarified that RAM is allocated per GPU, with specific amounts available for different GPU types:
  - V100 and RTX28080Ti GPUs: ~24 GB
  - A100 GPUs: ~128 GB
  - RTX3080 GPUs: ~48 GB
- Explained that jobs in the general work-partition have a RAM limit of 24 GB per GPU, while jobs explicitly sent to the rtx3080-partition get 48 GB per GPU but may experience longer wait times.
- **HPC Admin** suggested improving the documentation to make RAM allocation clearer.

## General Learnings
- Always check the cluster documentation for resource allocation details.
- Understand that RAM is allocated per GPU and may vary based on the GPU type and partition.
- Explicitly requesting specific partitions may grant more resources but could increase job wait times.
- Clear and concise documentation is crucial for user understanding and efficient resource utilization.
---

### 2024021442001319_Tier3-Access-Alex%20%22Erik%20G%C3%83%C2%B6sche%22%20_%20iwbi025h.md
# Ticket 2024021442001319

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject
Tier3-Access-Alex "Erik GÃ¶sche" / iwbi025h

## Keywords
- Account Activation
- GPGPU Cluster 'Alex'
- Nvidia A100 GPGPUs
- Conda
- Deep Learning
- DCE-MRI Reconstruction
- SFB Project
- PhD Research
- Publications
- Software Tools

## Summary
- **User Request**: Access to GPGPU cluster 'Alex' for deep learning-based DCE-MRI reconstruction.
- **Hardware Requirement**: Nvidia A100 GPGPUs (40 GB, 9.7 TFlop/s double precision).
- **Software Requirement**: Conda.
- **Computation Time**: 500 GPU-hours.
- **Expected Outcomes**: Publications and software tools as part of a PhD project.

## HPC Admin Response
- **Action Taken**: Account iwbi025h activated on Alex.
- **Admin**: Katrin Nusser

## Lessons Learned
- **Account Activation Process**: Understanding the steps involved in activating a user account on a specific HPC cluster.
- **Hardware Selection**: Importance of selecting appropriate hardware (e.g., Nvidia A100) based on computational needs.
- **Software Environment**: Ensuring the required software (e.g., Conda) is available for the user's project.
- **Research Support**: Providing resources for PhD research projects, including deep learning and medical imaging applications.

## Root Cause of the Problem
- User needed access to specific HPC resources for their research project.

## Solution
- HPC Admin activated the user's account on the requested cluster.
```
---

### 2024122042000012_Re%3A%20New%20invitation%20for%20%22Studentische%20Abschlu%C3%83%C2%9Farbeiten%20Tier3%20Grundversor.md
# Ticket 2024122042000012

 ```markdown
# HPC Support Ticket Conversation Analysis

## Keywords
- HPC Account Setup
- ROCm
- Anaconda
- AMD GPU
- CUDA
- NVIDIA GPU
- SSH Access
- Permissions
- Getting Started Guide
- Test Cluster
- Alex Cluster

## Summary
A user encountered issues with missing utilities (ROCm and Anaconda) on the CSNHR cluster and had trouble accessing the Alex cluster. The user needed these utilities for their workloads and environment management.

## Root Cause of the Problem
- Missing ROCm and Anaconda utilities on the CSNHR cluster.
- Difficulty accessing the Alex cluster, possibly due to permission issues.

## Solution
- **ROCm and Anaconda Utilities**: The HPC Admin informed the user that AMD GPUs and ROCm are only available in the test cluster. The user was directed to the test cluster documentation.
- **SSH Access to Alex Cluster**: The user was directed to the documentation for accessing the Alex cluster, which might include information on necessary permissions.

## General Learnings
- **Cluster-Specific Utilities**: Different clusters may have different utilities installed. Users should check the documentation for the specific cluster they are using.
- **Access Permissions**: Accessing certain clusters may require additional permissions or specific steps. Users should refer to the relevant documentation for guidance.
- **Getting Started Guide**: Users should consult the getting started guide and HPC-Nutshell for initial setup and common issues.

## References
- [Getting Started Guide](https://doc.nhr.fau.de/getting_started/)
- [HPC-Nutshell](https://hpc.fau.de/teaching/hpc-cafe/)
- [Test Cluster Documentation](https://doc.nhr.fau.de/clusters/testcluster/)
- [Alex Cluster Documentation](https://doc.nhr.fau.de/clusters/alex/)
```
---

### 2024090242004166_Tier3-Access-Alex%20%22Nina%20Goes%22%20_%20iwb3004h.md
# Ticket 2024090242004166

 # HPC Support Ticket Analysis

## Keywords
- HPC Account Activation
- Alex Cluster
- GPGPU
- Nvidia A100
- Nvidia A40
- PyTorch
- Diffusion Models
- Audio Synthesis

## Summary
- **User Request:** Access to Alex cluster for GPGPU resources (Nvidia A100 and A40) with a requirement of 10,000 GPU-hours.
- **Software Needed:** PyTorch
- **Application:** Diffusion models for audio synthesis
- **Expected Results:** Audio signal

## Actions Taken
- **HPC Admin:** Enabled the user's HPC account on Alex.

## Lessons Learned
- **Account Activation:** Ensure that user accounts are enabled promptly upon request.
- **Resource Allocation:** Understand the specific hardware and software requirements of users for efficient resource allocation.
- **Communication:** Maintain clear and professional communication with users regarding their requests and the status of their accounts.

## Root Cause
- User required access to specific GPGPU resources for their research project.

## Solution
- HPC Admin enabled the user's account on the Alex cluster, granting them access to the required resources.

---

This documentation can be used as a reference for future support tickets involving account activation and resource allocation on the Alex cluster.
---

### 2021113042003178_Nodes%20reservieren%3F.md
# Ticket 2021113042003178

 # HPC Support Ticket Conversation Summary

## Subject: Nodes reservieren?

### User Request:
- **User**: Requested reservation of compute nodes for a Deep Learning tutorial.
- **Details**:
  - User: iwal005h
  - Time: 16. Dezember, 13:00 bis 18:00
  - Cluster: tinyGPU
  - Anzahl GPUs: Mindestens eine – gerne bis zu vier.

### User Questions:
1. **Slurm Commands**: Difference between using tinygpu-alias and regular commands.
2. **$TMPDIR Quota**: Confirmation that there is no binding quota for $TMPDIR.
3. **Typo Correction**: Noted typo on the Slurm documentation page.

### HPC Admin Responses:
1. **Slurm Commands**:
   - tinygpu-alias and regular commands are interchangeable for now.
   - Default cluster may change in the future.
2. **$TMPDIR Quota**:
   - Confirmed that there is no binding quota for $TMPDIR.
3. **Typo Correction**:
   - Typo corrected on the documentation page.

### Additional Discussions:
- **Central Software Installation**:
  - User prefers setting up their own Python environment using miniconda/anaconda.
  - HPC Admins are considering central installation of ML software.
- **Reservation**:
  - A V100-Knoten reservation was made for the user.

### Documentation Improvement:
- **User Offer**: User offered to help improve documentation for TensorFlow and PyTorch.
- **HPC Admin Response**: HPC Admins welcomed the offer and provided links to existing documentation pages.

### Tutorial Material:
- **User Provided**: User shared a git repository with tutorial materials for Deep Learning using HPC resources.
- **HPC Admin Feedback**: HPC Admins found the tutorial useful but noted it lacked TensorFlow-specific content.

### Key Learnings:
- **Node Reservation**: Users can request node reservations for tutorials.
- **Slurm Commands**: tinygpu-alias and regular commands are interchangeable for now.
- **$TMPDIR Quota**: No binding quota for $TMPDIR.
- **Documentation**: Users can contribute to improving documentation.
- **Central Software Installation**: HPC Admins are considering central installation of ML software.

### Keywords:
- Node Reservation
- Slurm Commands
- $TMPDIR Quota
- Documentation Improvement
- Central Software Installation
- Deep Learning Tutorial
- TensorFlow
- PyTorch

### Root Cause and Solution:
- **Root Cause**: User needed node reservation for a tutorial and had questions about Slurm commands and $TMPDIR quota.
- **Solution**: HPC Admins provided the reservation and answered the user's questions. The user offered to help improve documentation, and the HPC Admins welcomed the offer.

### Additional Notes:
- **Typo Correction**: HPC Admins corrected a typo in the Slurm documentation.
- **Tutorial Material**: User shared tutorial materials, which were found useful but lacking TensorFlow-specific content.

This summary provides a concise overview of the support ticket conversation, including user requests, HPC Admin responses, and key learnings. It can be used as a reference for future support cases.
---

### 2024061042000203_Jobs%20on%20TinyGPU%20-%20owner_a100_wsw5%20requires%20A100%20partition%20-%20wsw5002h.md
# Ticket 2024061042000203

 # HPC Support Ticket: Jobs on TinyGPU - owner_a100_wsw5 requires A100 partition

## Keywords
- TinyGPU
- QoS (Quality of Service)
- A100 partition
- GPU allocation
- Job submission

## Problem
- User was unable to start jobs automatically on TinyGPU when specifying `--qos=owner_a100_wsw5`.

## Root Cause
- The job submission command did not include the necessary GPU resource specification and partition.

## Solution
- When submitting jobs on TinyGPU with `--qos=owner_a100_wsw5`, it is mandatory to also specify `--gres=gpu:a100:1 -p a100`.
- Specifying `--qos=owner_a100_wsw5` allows only 1 job with 1 GPU to run.
- Not specifying the QoS may allow up to 4 jobs to run.

## General Learning
- Proper resource specification is crucial for job submission on HPC systems.
- Understanding QoS settings and their implications on job allocation is important for efficient resource utilization.

## Actions Taken
- HPC Admin provided detailed instructions on the correct job submission command.
- User confirmed that the job script ran much faster after applying the suggested changes.

## References
- [FAU HPC Support](mailto:support-hpc@fau.de)
- [FAU HPC Website](https://hpc.fau.de/)
---

### 2023033042001897_Jobs%20on%20TinyGPU%20only%20use%201%20of%204%20allocated%20GPUs%20%5Biwnt001h%5D.md
# Ticket 2023033042001897

 # HPC Support Ticket: Jobs on TinyGPU Only Use 1 of 4 Allocated GPUs

## Keywords
- GPU utilization
- Job monitoring
- Resource allocation
- `nvidia-smi`
- `srun --pty --jobid bash`
- Code optimization

## Summary
The user's jobs on TinyGPU were only utilizing one of the four allocated GPUs, leading to inefficient resource usage.

## Root Cause
- The user's code specified `devices=1` in the `pl.Trainer` initialization, limiting GPU usage to a single device.

## Steps Taken by HPC Admins
1. **Initial Notification**: Informed the user about the underutilization of GPUs and provided instructions to check GPU usage with `nvidia-smi`.
2. **Follow-up**: Notified the user again when the issue persisted with new job IDs.
3. **Code Review**: Identified the `devices=1` parameter in the user's code as the likely cause of the issue.

## Solution
- The user was advised to check and modify the code to ensure it utilizes all allocated GPUs. Specifically, they were instructed to remove or adjust the `devices=1` parameter.

## User Response
- The user acknowledged the issue and agreed to correct the code to utilize all allocated GPUs. They also requested that future jobs be stopped if GPUs are not utilized correctly.

## General Learning
- Always ensure that the code is configured to utilize all allocated resources to avoid wastage.
- Use monitoring tools like `nvidia-smi` to check resource utilization.
- Communicate with users to resolve resource allocation issues promptly.

## Closure
- The ticket was closed after the user responded and acknowledged the issue.
---

### 2024112142001253_HPC%20Access%20-%20Alex%20Cluster.md
# Ticket 2024112142001253

 ```markdown
# HPC Support Ticket Conversation Analysis

## Keywords
- HPC Access
- Alex Cluster
- Master Thesis
- Foundation Models
- A100 GPUs
- A40 GPUs
- TinyGPU
- Request Form
- Cluster Admins

## Summary
A user requested access to the Alex Cluster for their master thesis, which requires A100 and A40 GPUs. The user had filled out the request form but had not received any updates.

## Root Cause
- **Oversight in Processing Request**: The user's request for access to the Alex Cluster was not processed in a timely manner.

## Solution
- **Escalation to Cluster Admins**: The HPC Admin acknowledged the oversight and forwarded the request to the cluster admins for further processing.

## General Learnings
- **Importance of Timely Communication**: Ensure that all access requests are processed and communicated promptly to avoid delays in user projects.
- **Escalation Procedures**: When there is a delay in processing requests, escalate the issue to the appropriate team (e.g., cluster admins) to resolve it quickly.

## Next Steps
- **Follow-up with User**: Confirm with the user that their request has been processed and provide any necessary access details.
- **Review Process**: Review the request processing workflow to identify and address any bottlenecks or communication gaps.
```
---

### 2021040742003109_GPU%20Knoten%20AG%20Imhof.md
# Ticket 2021040742003109

 # HPC Support Ticket Conversation Summary

## Subject: GPU Knoten AG Imhof

### Keywords:
- GPU nodes
- Amber 20
- RTX3080
- SLURM
- Cpptraj
- Performance optimization

### General Learnings:
- New GPU nodes available with specific configurations.
- Job submission script for GPU nodes using SLURM.
- Performance issues with Amber/pmemd on new GPU nodes.
- Adjusting job resubmission scripts for SLURM.
- Missing Cpptraj module in GPU version.

### Root Cause of Problems:
1. **Performance Issue**: Low GPU utilization (~45%) during Amber/pmemd jobs, possibly due to the nature of the job (thermodynamic integration).
2. **Missing Module**: Cpptraj not found in the GPU version of Amber.
3. **Job Resubmission**: Script adjustment needed for SLURM.

### Solutions:
1. **Performance Issue**:
   - Suggested running a normal job for comparison.
   - Optimization as per Amber manual, though it may deviate from standard protocol.

2. **Missing Module**:
   - New module `amber/20p08-at20p12-intel-impi` should be available.

3. **Job Resubmission**:
   - Adjusted script for SLURM:
     ```bash
     sed -e "s/^export SIMRUN=[0-9]*/export SIMRUN=$NEXTRUN/" > $PBS_JOBNAME-resubmit-`printf %3.3i $NEXTRUN`
     sbatch $PBS_JOBNAME-resubmit-`printf %3.3i $NEXTRUN`
     ```

### Additional Notes:
- New GPU nodes run on Ubuntu 20.04, different from older nodes.
- Documentation for new nodes is pending.
- User files currently stored in `/home/woody`, query about alternative storage options.

### Conversation Summary:
- User inquired about new GPU nodes and access.
- HPC Admin provided job submission script for SLURM.
- Performance issues and missing modules were addressed.
- Job resubmission script adjustments were provided.
- Further performance testing and optimization suggested.

This summary can be used to address similar issues in the future, focusing on job submission, performance optimization, and module availability for GPU nodes.
---

### 2021012042001851_MMPBSA-Jobs%20on%20TinyGPU%20%5Btumu003h%5D.md
# Ticket 2021012042001851

 # HPC Support Ticket: MMPBSA-Jobs on TinyGPU

## Keywords
- MMPBSA-Jobs
- TinyGPU
- GPU support
- Woody cluster
- Emmy cluster
- Amber-module
- MPI-processes

## Summary
A user was running MMPBSA-Jobs on TinyGPU without utilizing the GPU. The HPC Admin advised the user to move the calculations to the Woody or Emmy clusters, as MMPBSA.py.MPI does not support GPU.

## Root Cause
- MMPBSA.py.MPI jobs were running on TinyGPU without GPU support.

## Solution
- Move MMPBSA-Jobs to Woody or Emmy clusters.
- On Woody, use the same Amber-module but adjust the number of MPI-processes to 4.
- On Emmy, load the Amber-module 'amber/18p14-at19p03-intel17.0-intelmpi2017'.

## Lessons Learned
- Ensure that jobs requiring specific hardware support (e.g., GPU) are run on appropriate clusters.
- Adjust job configurations (e.g., MPI-processes) as needed when moving between clusters.
- Communicate with users to provide guidance on suitable clusters and modules for their jobs.

## Follow-up
- The user confirmed that they moved their calculations to the Woody cluster.
- The ticket was closed after the user's confirmation.

---

This documentation can be used to address similar issues in the future, ensuring that jobs are run on the correct clusters with the appropriate configurations.
---

### 2024102942004103_Guidance%20on%20HPC%20Account%20Application%20for%20Generative%20Materials%20Project.md
# Ticket 2024102942004103

 ```markdown
# HPC Support Ticket Conversation Summary

## Keywords
- HPC Account Application
- Generative Materials Project
- FAU Lectures
- Account Validity
- HPC Clusters (Alex, TinyGPU)
- GPU Utilization
- Student Onboarding

## General Learnings
- **HPC Accounts**: Always associated with a project or research chair. Students cannot request accounts directly.
- **Account Validity**: For FAU lectures, accounts are valid for the entire semester.
- **Cluster Choice**: TinyGPU with RTX3080 has shorter queueing times compared to Alex cluster.
- **Onboarding**: HPC support provides monthly introductions. Students should attend or receive a short introduction.
- **GPU Utilization**: Monitor student jobs for proper GPU utilization to identify issues early.

## Root Causes and Solutions
- **Account Validity Mismatch**:
  - **Root Cause**: Webpage indicated accounts valid for one week, but module spans the entire semester.
  - **Solution**: Apply for "Lectures of FAU" to get accounts valid for the entire semester.

- **Student GPU Utilization Issue**:
  - **Root Cause**: Student jobs showing 0% GPU utilization.
  - **Solution**: Inform the student and provide guidance on proper job submission and GPU utilization.

## Actions Taken
- **Project Creation**: Created a project in HPC-Portal for the Generative Materials Project.
- **Cluster Choice**: Opted for TinyGPU due to shorter queueing times.
- **Student Onboarding**: Provided information on upcoming HPC introduction sessions.
- **Issue Notification**: Notified the user about a student's jobs showing 0% GPU utilization.

## Additional Notes
- **Introduction Sessions**:
  - General Introduction: Wednesday, December 18, 2024, 4:00 p.m.
  - Introduction for AI Users: Thursday, December 19, 2024, 4:00 p.m.
  - Location (Zoom): [HPC in a Nutshell](https://go-nhr.de/hpc-in-a-nutshell)
```
---

### 2025021042003681_Jobs%20on%20TinyGPU%20not%20using%20the%20GPUs%20%5Biwfa107h%5D.md
# Ticket 2025021042003681

 # HPC Support Ticket: Jobs on TinyGPU Not Using GPUs

## Keywords
- GPU utilization
- Job allocation
- Monitoring system
- ClusterCockpit
- `nvidia-smi`
- Resource management

## Summary
A user's jobs on TinyGPU were not utilizing the allocated GPUs, leading to idle resources.

## Root Cause
The user's code was not configured to use the GPUs, resulting in inefficient resource allocation.

## Solution
1. **Monitoring GPU Utilization:**
   - Users can log into the monitoring system ClusterCockpit at [monitoring.nhr.fau.de](https://monitoring.nhr.fau.de/) to view GPU utilization.
   - Alternatively, users can attach to their running job using the command:
     ```bash
     srun --pty --overlap --jobid YOUR-JOBID bash
     ```
   - Once attached, run `nvidia-smi` to check the current GPU utilization.

2. **Efficient Resource Allocation:**
   - Ensure that jobs are only allocated nodes with GPUs if the code can actually utilize them.
   - Avoid idle resources by properly configuring the code to use GPUs.

## General Learnings
- Regularly monitor job performance to ensure efficient use of resources.
- Use monitoring tools like ClusterCockpit and `nvidia-smi` to diagnose resource utilization issues.
- Properly allocate resources based on the actual needs of the job to prevent resource wastage.

## Contact Information
For further assistance, contact the HPC support team at [support-hpc@fau.de](mailto:support-hpc@fau.de).
---

### 2023012742000942_Job%20on%20Alex%20only%20uses%20one%20GPU%20%5Biwb0003h%5D.md
# Ticket 2023012742000942

 # HPC Support Ticket: Job on Alex Only Uses One GPU

## Keywords
- GPU utilization
- Job allocation
- Resource management
- `nvidia-smi`
- `srun`

## Summary
A user's job on the Alex cluster was only utilizing one out of four allocated GPUs. The HPC Admin provided guidance on how to check GPU utilization and emphasized the importance of efficient resource allocation.

## Root Cause
- The user's job was not effectively utilizing the allocated GPU resources.

## Solution
- **Checking GPU Utilization:**
  - Attach to the running job using `srun --pty --jobid bash`.
  - Run `nvidia-smi` to view current GPU utilization.

- **Efficient Resource Allocation:**
  - Ensure that jobs only allocate nodes with GPUs if the code can make use of them.
  - Avoid idle GPU resources to maximize cluster efficiency.

## General Learnings
- Regularly monitor GPU utilization to ensure efficient use of resources.
- Use `nvidia-smi` to diagnose GPU usage issues.
- Properly allocate resources based on job requirements to prevent resource wastage.

## Next Steps
- If further assistance is needed, contact the HPC support team.
- Ensure future jobs are optimized for the allocated resources.
---

### 2021010142000315_4x%20NVIDIA%20RTX%202080%20Ti.md
# Ticket 2021010142000315

 # HPC Support Ticket Conversation Analysis

## Keywords
- Molecular Dynamics Simulations
- Coronavirus Spike Protein
- Wildtype Form (WT-Form)
- UK Variant
- RTX 2080 Ti
- Tesla V100
- A100
- Job Script
- Slurm
- Torque/PBS
- Amber

## Summary
A user requested the reservation of 4x NVIDIA RTX 2080 Ti GPUs for molecular dynamics simulations related to the coronavirus spike protein. The request was time-sensitive due to the competitive nature of the research field.

## Root Cause of the Problem
- The user needed high-performance computing resources for urgent research.

## Solution Provided
- The HPC Admin reserved one RTX 2080 Ti node for the user.
- Offered alternative GPU options:
  - Tesla V100 (1-10% faster than RTX 2080 Ti)
  - A100 (50-100% faster than RTX 2080 Ti)
- Provided instructions for job script modifications if the user opted for different GPUs.

## General Learnings
- Understanding the performance differences between various GPU models (RTX 2080 Ti, Tesla V100, A100).
- Importance of timely resource allocation for time-sensitive research projects.
- Job script modifications required for different GPU types and scheduling systems (Slurm vs. Torque/PBS).

## Action Items for Support Employees
- Be prepared to offer alternative resources if the requested ones are not available.
- Provide clear instructions for job script modifications when necessary.
- Ensure timely communication and resource allocation for urgent research needs.
---

### 2023030842002188_Tier3-Access-Alex%20%22Philipp%20Suffa%22%20_%20iwia046h.md
# Ticket 2023030842002188

 # HPC Support Ticket Analysis

## Keywords
- Account Activation
- Certificate Expiration
- Email Delivery Failure
- GPGPU Cluster Access
- Software Requirements
- Rechenzeit Request

## Summary
- **Root Cause**: Certificate expiration and email delivery failure.
- **Solution**: Account activation and email address verification.

## Details
- **Account Activation**: The user's account was activated on the GPGPU cluster 'Alex'.
- **Certificate Expiration**: The initial issue was due to an expired certificate.
- **Email Delivery Failure**: The user's email address was incorrect or not recognized by the system, leading to a delivery failure.
- **Software Requirements**: The user requested access to specific software including GCC, OpenMPI, CUDA, and Python.
- **Rechenzeit Request**: The user requested a specific amount of GPU hours for their project.

## Lessons Learned
- Ensure certificates are up-to-date to avoid access issues.
- Verify email addresses to prevent delivery failures.
- Document software requirements clearly for future reference.
- Address Rechenzeit requests promptly to allocate resources efficiently.

## Action Items
- **HPC Admins**: Verify and update certificates regularly.
- **2nd Level Support Team**: Assist users with email address verification and software installation.
- **Head of Datacenter/Training and Support Group Leader**: Ensure smooth communication and resource allocation.
- **NHR Rechenzeit Support**: Process Rechenzeit requests efficiently.
- **Software and Tools Developer**: Ensure requested software is available and up-to-date.

## Conclusion
Regular maintenance of certificates and verification of user information are crucial for smooth operation. Clear communication and prompt action on requests help in efficient resource management.
---

### 2024090742000339_Tier3-Access-Alex%20%22Zamal%20Ali%20Babar%20Mohammed%22%20_%20jy68gipi%40fau.de.md
# Ticket 2024090742000339

 # HPC Support Ticket Conversation Analysis

## Keywords
- HPC Account
- HPC Portal
- Deep Learning Models
- Double-Precision Floating-Point Performance
- A100 GPUs
- TinyGPU
- Invitation
- Reduced Precision (bfloat16, int8, int4)

## Summary
- **Root Cause**: User requires access to the HPC cluster 'Alex' but does not have an HPC account.
- **Solution**: User needs to contact their chair to receive an invitation for an HPC account.

## Details
- **User Request**: Access to 'Alex' cluster for deep learning projects, specifically mentioning the need for superior double-precision floating-point performance of Nvidia A100 GPUs.
- **HPC Admin Response**:
  - User has a login in the HPC portal but no HPC account.
  - Chair needs to send an HPC invitation.
  - Proper usage on TinyGPU (with A100 GPUs) is a prerequisite for accessing 'Alex'.
  - Double-precision floating-point performance is not typically essential for deep learning models, which often operate on reduced precision like bfloat16, int8, or int4.

## General Learnings
- **Account Setup**: Users must have an HPC account, which requires an invitation from their chair.
- **Prerequisites**: Demonstrating proper usage on TinyGPU is necessary before accessing more advanced resources like 'Alex'.
- **Hardware Suitability**: Deep learning models typically do not require superior double-precision floating-point performance; reduced precision is often sufficient.

## Next Steps
- User should contact their chair for an HPC invitation.
- User should demonstrate proper usage on TinyGPU to qualify for access to 'Alex'.

## Additional Notes
- The conversation highlights the importance of understanding the specific computational needs of different types of projects and the appropriate hardware for those needs.
- Proper communication and guidance from HPC admins are crucial for users to navigate the HPC resources effectively.
---

### 2025020342000946_NHR-Starter%20b260dc%20_%20JA-24328%20_%20AiDigiForensics%20_%20Kevin%20Meyer%20Inf%201%20FAU.md
# Ticket 2025020342000946

 # HPC Support Ticket Conversation Analysis

## Keywords
- NHR Projekttyp
- GPU-h pro Jahr
- KI-Modelle/-Methoden
- Explainable AI
- Cluster "Alex"
- Rechenzeitbedarf
- Antragsverfahren
- HPC-Zugang

## Summary
A user, a PostDoc at the Department of Computer Science 1, is seeking advice on the appropriate NHR project type for their research in digital forensics and artificial intelligence. The user's requirements include training classical and adapted LLMs, various ML methods, and evaluating methods in the "Explainable AI" field. The user estimates their computational needs at around 8,000 - 10,000 GPU-h per year.

## Root Cause of the Problem
The user is unsure which NHR project type is suitable for their research needs, specifically for training and testing various AI models and methods.

## Solution
The HPC Admin requests a rough estimate of the user's computational needs (GPU-h per year) to provide appropriate advice on the application process for HPC access. The user provides an estimate of 8,000 - 10,000 GPU-h per year.

## General Learnings
- Users need guidance on selecting the appropriate NHR project type based on their research requirements.
- Estimating computational needs (GPU-h per year) is essential for advising users on the application process for HPC access.
- The cluster "Alex" may be suitable for users working on AI and ML projects, especially those involving "Explainable AI."
- The 2nd Level Support team is involved in providing technical approval and start information to applicants.
---

### 2024032142001965_AI%20-%20From%20Laptop%20to%20Supercomputer.%20Start%3A%2019.10.23%2C%2014%3A00.md
# Ticket 2024032142001965

 ```markdown
# HPC Support Ticket Conversation Summary

## Subject: AI - From Laptop to Supercomputer. Start: 19.10.23, 14:00

### Keywords:
- PyCharm
- Remote Debugging
- SLURM Jobs
- GPU Allocation
- Job Extension
- Ticket Creation

### General Learnings:
- **Remote Debugging with PyCharm**: Allocate a node using an interactive SLURM job, identify the node, and follow instructions for multi-hop remote interpreters via SSH.
- **GPU Allocation**: Use the "preempt" partition for jobs agnostic to GPU type, but be aware of potential early termination.
- **Job Extension**: HPC Admins can extend job times, but users should create new tickets for such requests.
- **Ticket Creation**: To create a new ticket, send an email to `hpc-support@fau.de` instead of replying to an old ticket.

### Root Causes and Solutions:
- **Remote Debugging with PyCharm**:
  - **Root Cause**: User needs to debug remotely using PyCharm.
  - **Solution**: Allocate a node using an interactive SLURM job, identify the node, and follow instructions for multi-hop remote interpreters via SSH.

- **GPU Allocation**:
  - **Root Cause**: User wants to run jobs on any GPU type.
  - **Solution**: Use the "preempt" partition, which is agnostic to GPU type, but be aware of potential early termination.

- **Job Extension**:
  - **Root Cause**: User needs to extend the running time of SLURM jobs.
  - **Solution**: HPC Admins can extend job times, but users should create new tickets for such requests.

- **Ticket Creation**:
  - **Root Cause**: User needs to create a new support ticket.
  - **Solution**: Send an email to `hpc-support@fau.de` instead of replying to an old ticket.
```
---

### 2020030442002708_Re%3A%20Fwd%3A%20Re%3A%20Rechenzentrum%20-%20GPU%20Cluster%20zum%20Lernen.md
# Ticket 2020030442002708

 ```markdown
# HPC Support Ticket Conversation Analysis

## Keywords
- GPU Cluster
- TinyGPU nodes
- Fairshare-Scheduling
- Checkpoint & Restart
- Tensorflow/Pytorch
- CUDA
- cuDNN
- Anaconda-Python
- Singularity
- Docker-Images
- HPC-Account
- Speicherplatz
- Shareholder
- NFS-Server
- Corona

## General Learnings
- **Availability of TinyGPU Nodes**: The availability of TinyGPU nodes is high, but due to fair-share scheduling and job limits, long-running jobs need to use checkpoint & restart.
- **Deep Learning Support**: Tensorflow/Pytorch is not centrally installed but can be installed by users using Anaconda-Python or Singularity with Docker images.
- **Account Management**: Simplified protocols for extending/getting HPC accounts during the Corona shutdown.
- **Storage**: Groups requiring large storage can opt for a paid service extension.
- **Exclusive Access**: Some GPUs are reserved for shareholders who have invested in the cluster.

## Root Causes of Problems
- **High GPU Demand**: The TinyGPU nodes are highly utilized, making it difficult to secure resources for extended periods.
- **Lack of Central Installation**: Tensorflow/Pytorch is not centrally installed, requiring users to set it up themselves.
- **Storage Limitations**: Limited storage space for large datasets (>1TB).
- **Account Issues**: Users need to apply for HPC accounts and may face delays or complications in the process.

## Solutions
- **Checkpoint & Restart**: Users should implement checkpoint & restart mechanisms to handle job interruptions.
- **Self-Installation of Libraries**: Users can install Tensorflow/Pytorch using Anaconda-Python or Singularity with Docker images.
- **Simplified Account Protocols**: During the Corona shutdown, simplified protocols are in place for account management.
- **Paid Storage Services**: Groups requiring large storage can opt for paid service extensions.
- **Investment in Cluster**: Groups can invest in the cluster to gain exclusive access to certain GPUs.

## Documentation for Support Employees
- **GPU Availability**: Inform users about the high demand and the need for checkpoint & restart.
- **Deep Learning Libraries**: Guide users on installing Tensorflow/Pytorch using Anaconda-Python or Singularity.
- **Account Management**: Provide information on the simplified account protocols during the Corona shutdown.
- **Storage Solutions**: Offer paid service extensions for groups requiring large storage.
- **Exclusive Access**: Explain the option for groups to invest in the cluster for exclusive GPU access.
```
---

### 201808179001207_Re%3A%20%5BRRZE-HPC%5D%20Call%20for%20proposals%20on%20NVidia%20Tesla%20V100%20usage.md
# Ticket 201808179001207

 # HPC-Support Ticket Conversation Analysis

## Subject: Re: [RRZE-HPC] Call for proposals on NVidia Tesla V100 usage

### User Request
- **Project Description**:
  - Egocentric videos for Augmented Reality systems.
  - Designing a power- and storage-aware framework.
  - Mathematical optimization techniques for adaptive duty-cycle tuning.
  - Deep learning network for activity recognition.
  - Dataset: EPIC Kitchen.
  - Requirements: Python environment, basic Python libraries, TensorFlow, CuDNN.
  - Estimated compute time: 1-2 months.
  - Multi-GPU computation without bottlenecks.
  - Funding available for compute cycles.

### HPC Admin Response
- **Initial Response**:
  - Access instructions for V100 GPUs.
  - Node specifications: 2x Intel Xeon E5-2690 v2, 64 GB RAM, ~870 GB local disk storage.
  - Usage of `/scratch` for temporary storage.
  - 24-hour job duration limit.

### User Follow-up
- **Issues**:
  - Large dataset (500 GB) requiring frequent uploads due to job duration limits.
  - Need for long-term storage solution.

### HPC Admin Suggestions
- **Storage Solutions**:
  - Use of `$WOODYHOME` directory for data access.
  - Suggestion to write a letter to the dean for long-term HPC improvements.

### Meeting Request
- **User**: Requested a meeting for further questions.
- **HPC Admin**: Offered meeting slots for Oct. 29th or 30th.

### Key Learnings
- **Storage Management**:
  - `/scratch` is temporary and cleaned up after each job.
  - Long-term storage solutions are limited.
- **Job Duration**:
  - 24-hour limit for jobs.
  - Users need to save and reload models for long-running tasks.
- **Communication**:
  - Importance of clear communication between users and HPC support.
  - Users should advocate for their needs through official channels.

### Solutions
- **Storage**:
  - Use `$WOODYHOME` for long-term data storage.
  - Advocate for improved HPC facilities through official letters.
- **Job Management**:
  - Save and reload models for long-running tasks.
  - Plan jobs to fit within the 24-hour limit.

### Conclusion
- **User**: Needs to manage large datasets and long-running jobs effectively.
- **HPC Admin**: Provides guidance on storage and job management, encourages advocacy for improved facilities.

---

This report summarizes the key points and solutions from the HPC-Support ticket conversation, providing a reference for future support cases.
---

### 2021101142003483_HPC%20cluster.md
# Ticket 2021101142003483

 # HPC Support Ticket: Memory Allocation Issue

## Keywords
- Memory allocation error
- TORQUE job
- PBS configuration
- GPU memory
- RuntimeError
- CPUAllocator
- Error code 12
- :gtx1080ti
- :v100 GPU

## Problem Description
- User encountered a memory allocation error while running a TORQUE job on PBS configuration.
- Error message: `RuntimeError: [enforce fail at CPUAllocator.cpp:67] DefaultCPUAllocator: can't allocate memory: you tried to allocate 20889600000 bytes. Error code 12 (Cannot allocate memory)`
- User was explicitly requesting `:gtx1080ti` GPUs, which have 11 GB of memory.

## Root Cause
- The user's job required more memory than available on the requested `:gtx1080ti` GPUs (11 GB).
- The job tried to allocate 20 GB of memory, which exceeded the available GPU memory.

## Solution
- HPC Admin suggested using `:v100` GPUs, which have 32 GB of memory, to accommodate the job's memory requirements.

## General Learnings
- Ensure that the requested resources (e.g., GPU memory) are sufficient for the job's requirements.
- Different GPU types have varying memory capacities.
- Adjust resource requests in job scripts to match the job's needs.

## Related Resources
- [HPC FAU GPU Resources](http://hpc.fau.de/)
- [TORQUE/PBS Job Submission Guide](http://hpc.fau.de/guides/job-submission)

## Ticket Status
- Resolved by suggesting an alternative GPU type with more memory.
---

### 2024100942003802_Inferenz%20TinyGPU%20Cluster%20-%20Prof.%20Harth%20_%20WiSo.md
# Ticket 2024100942003802

 ```markdown
# HPC Support Ticket Conversation Summary

## Initial Request
- **User:** Andreas Harth
- **Date:** 09/10/2024
- **Issue:** Request for GPU resources for inference with large models (e.g., 70b Llama) on the TinyGPU cluster.

## Key Points
1. **GPU Resource Allocation:**
   - The user has access to the TinyGPU cluster and requires GPU resources for inference with large models.
   - The current batch-betrieb of the TinyGPU cluster is not suitable for this purpose.

2. **Model Performance:**
   - The user is testing different models (3b, 70b, 405b) and finds the 70b model to be the most suitable.
   - The user is experiencing performance issues with the 405b model.

3. **Context Length and API Issues:**
   - The user encounters issues with long prompts and context length limitations.
   - The HPC Admin team adjusts the API gateway and model parameters to handle longer contexts.

4. **Solution Provided:**
   - The HPC Admin team sets up API endpoints for the models and adjusts parameters to improve performance.
   - The team also provides alternative API services from Forschungszentrum Jülich and Uni-Göttingen for additional resources.

## Actions Taken
1. **API Endpoints Setup:**
   - The HPC Admin team sets up OpenAI-compatible API endpoints for the models.
   - Adjustments are made to handle longer context lengths and improve performance.

2. **Model Adjustments:**
   - The team adjusts the context length and other parameters for the models to improve performance.
   - The team also provides alternative API services for additional resources.

3. **User Feedback:**
   - The user tests the provided models and finds the 70b model to be the most suitable.
   - The user provides feedback on performance and context length issues.

## Conclusion
- The HPC Admin team successfully sets up API endpoints and adjusts model parameters to meet the user's requirements.
- The user is provided with additional resources and alternative API services for further testing and experimentation.
- The user is satisfied with the performance of the 70b model and continues to use it for their projects.

## Additional Information
- **Alternative API Services:**
  - Forschungszentrum Jülich: [API Access Guide](https://sdlaml.pages.jsc.fz-juelich.de/ai/guides/blablador_api_access/)
  - Uni-Göttingen: [API Request Guide](https://docs.hpc.gwdg.de/services/saia/index.html#api-request)

- **Models Available:**
  - meta-llama-3.1-8b-instruct
  - mistral-large-instruct
  - meta-llama-3.3-70b-instruct
  - qwen2.5-72b-instruct

## Next Steps
- The user will continue to use the provided models and API services for their projects.
- The HPC Admin team will monitor the performance and provide additional support as needed.
```
---

### 2022052842000159_Remote%20gpu%20usage%20permissions.md
# Ticket 2022052842000159

 # HPC Support Ticket: Remote GPU Usage Permissions

## Keywords
- GPU access
- Resource utilization
- Job status
- Script modification
- GPU nodes

## Summary
A user reported issues with GPU access and job execution after modifying scripts to run tasks on the GPU.

## Problem
- User initially used CPU for data processing, leading to resource waste.
- Modified scripts to run tasks on GPU but encountered issues with job execution.
- Job status showed as running, but no tasks were actually running, and no output was generated.

## HPC Admin Response
- No waiting jobs were observed from the user.
- The GPU cluster (Alex) was fully loaded, causing delays in job processing.
- Suggested using TinyGPU for better throughput.
- GPU utilization was at 20%, indicating potential underutilization.
- Advised the user to check with their supervisor as most of the support team was traveling.

## Solution
- The user was advised to check job scripts and ensure proper GPU utilization.
- No specific solution was provided, but the user was encouraged to seek further assistance from their supervisor or the support team.

## Lessons Learned
- Proper resource utilization is crucial for efficient job processing.
- GPU clusters can experience high load, leading to job delays.
- Users should verify job scripts and ensure tasks are correctly assigned to GPU nodes.
- Communication with supervisors and the support team is essential for resolving complex issues.

## Next Steps
- Users should review job scripts and ensure proper GPU utilization.
- If issues persist, seek assistance from supervisors or the HPC support team.
- Consider using alternative resources like TinyGPU for better throughput during high load periods.
---

### 2025021242001722_Tier3-Access-Alex%20%22S%C3%83%C2%B6ren%20Wacker%22%20_%20ihpc147h.md
# Ticket 2025021242001722

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Keywords
- Tier3 Access
- Alex
- GPGPU Cluster
- Nvidia A100
- Nvidia A40
- GPU-hours
- PyTorch
- Benchmarking
- Optimized Benchmarks

## Summary
- **User Request**: Access to GPGPU cluster 'Alex' for benchmarking using PyTorch.
- **Resources Requested**:
  - Nvidia A100 GPGPUs (9.7 TFlop/s double precision)
  - Nvidia A40 GPGPUs (48 GB, 37 TFlop/s single precision)
  - 500 GPU-hours
- **Expected Outcome**: Optimized Benchmarks

## Actions Taken
- **HPC Admin**: Granted access to the user for the requested resources.

## Lessons Learned
- **Access Granting**: HPC Admins can grant access to specific clusters and resources upon user request.
- **Resource Allocation**: Users can request specific hardware and software resources for their projects.
- **Communication**: Effective communication between users and HPC Admins ensures proper resource allocation and access.

## Root Cause of the Problem
- User needed access to specific GPGPU resources for benchmarking purposes.

## Solution
- HPC Admin granted the user access to the requested resources.
```
---

### 2024012542000686_job%20in%20the%20queue%20a100multi.md
# Ticket 2024012542000686

 # HPC Support Ticket: Job in the Queue a100multi

## Keywords
- Job queue
- GPU memory
- Slurm options
- Resource optimization

## Problem
- User's job on 8 nodes (64 GPUs) has been waiting in the queue for several days.
- Jobs are now running on GPUs with 80 GB memory instead of 40 GB as before, without changes in the job script.

## Root Cause
- High demand for A100 nodes leading to long waiting times.
- Short job runtime (5 minutes) causing inefficient resource usage.
- Random GPU assignment due to no specified GPU type in the job script.

## Solution
- **Specify GPU Type**: Use Slurm options `-C a100_80` for 80 GB GPUs or `-C a100_40` for 40 GB GPUs.
- **Optimize Job Submission**: Aggregate workload into fewer, longer jobs to better utilize waiting time and resources.

## General Learnings
- High demand for specific resources can lead to extended waiting times.
- Specifying resource types can help manage job assignments.
- Efficient job scheduling can reduce idle time and improve resource utilization.

## Actions Taken
- HPC Admins provided guidance on specifying GPU types and optimizing job submissions.
- User acknowledged the advice and will adjust future job submissions accordingly.
---

### 2024111442002579_GPUs%20allocated%20but%20not%20utilized%20-%20b116ba19.md
# Ticket 2024111442002579

 # HPC Support Ticket: GPUs Allocated but Not Utilized

## Keywords
- GPU utilization
- `nvidia-smi`
- ClusterCockpit
- Job monitoring
- Resource allocation

## Problem Description
- User's job on the HPC cluster is allocated GPU resources, but they are not being utilized.
- `nvidia-smi` output shows 0% GPU utilization across all allocated GPUs.

## Root Cause
- The user's code or application running on the HPC cluster is not configured to use the allocated GPUs.

## Solution
- Ensure that the application or code is capable of utilizing GPU resources.
- Verify that the job script or application settings are correctly configured to use the allocated GPUs.
- Use `nvidia-smi` to monitor GPU utilization and confirm that the GPUs are being used.

## Steps for Monitoring GPU Utilization
1. **ClusterCockpit**:
   - Log in to the monitoring system at [ClusterCockpit](https://monitoring.nhr.fau.de/).
   - Refer to the documentation for job monitoring with ClusterCockpit: [Job Monitoring with ClusterCockpit](https://doc.nhr.fau.de/job-monitoring-with-clustercockpit/).

2. **Attach to Running Job**:
   - Use the command `srun --pty --overlap --jobid YOUR-JOBID bash` to attach to the running job.
   - Run `nvidia-smi` to check the current GPU utilization.

## Best Practices
- Only allocate nodes with GPUs if the code can actually make use of the GPU.
- Regularly monitor resource utilization to ensure efficient use of HPC resources.

## Contact
- For further assistance, contact the HPC support team at [support-hpc@fau.de](mailto:support-hpc@fau.de).

---

This documentation aims to help HPC support employees diagnose and resolve similar issues related to GPU utilization on the HPC cluster.
---

### 2025031242003979_Tier3-Access-Alex%20%22Deepak%20Bhatia%22%20_%20mfdp114h.md
# Ticket 2025031242003979

 ```markdown
# HPC Support Ticket: Tier3-Access-Alex

## Keywords
- GPU access
- Queueing times
- Resource allocation
- NHR application
- Pytorch
- AI vision tasks

## Summary
- **User Issue**: Long waiting times for GPU resources on TinyGPU, hindering workflow.
- **Request**: Access to Alex cluster to mitigate waiting times.
- **Demand**: 4000 GPU hours yearly for AI vision tasks.

## Details
- **User Needs**:
  - GPU resources for training segmentation, landmark detection, and image classification models.
  - Minimum V100 GPU for batch sizes 2 and 4.
  - Current job with one V100 GPU takes 15 hours.

- **HPC Admin Response**:
  - Queueing times on Alex are similar or longer than TinyGPU.
  - 4000 GPU hours cannot be fully covered by FAU share of Alex.
  - User granted access to Alex but may need to apply for NHR resources if usage is excessive.

## Solution
- **Access Granted**: User can now use Alex cluster.
- **Future Steps**: User advised to apply for NHR resources if needed.

## Notes
- **Queueing Times**: Normal and expected on HPC systems with > 2000 users.
- **Resource Management**: User should prioritize TinyGPU and use Alex as a backup.
- **Application**: User may need to submit an NHR application for additional resources.

## Closure
- **Ticket Status**: Closed.
- **Reason**: User granted access to Alex and advised on future steps.
```
---

### 2025010242001038_Tier3-Access-Alex%20%22Yanran%20Chen%22%20_%20tunu107h.md
# Ticket 2025010242001038

 # HPC Support Ticket: Tier3-Access-Alex

## Keywords
- HPC Account Activation
- Alex Cluster
- Nvidia A100, A40 GPGPUs
- Pytorch, Transformers
- GPU-hours Calculation
- Argument Convincingness Research

## Summary
- **User Request**: Access to Alex cluster for research on emotions and argument convincingness using LLMs.
- **Resources Requested**:
  - GPGPU cluster 'Alex' / Nvidia A100 GPGPUs (9.7 TFlop/s double precision)
  - GPGPU cluster 'Alex' / Nvidia A40 GPGPUs (48 GB, 37 TFlop/s single precision)
  - 5000 GPU-hours (2 GPUs per job * 5 hours per job * 500 jobs)
- **Software Needed**: Pytorch, Transformers
- **Expected Outcomes**: Argument dataset with human/LLMs annotated emotions and convincingness, argument generation systems.

## Actions Taken
- **HPC Admin**: Enabled the user's HPC account on Alex.

## Lessons Learned
- **Resource Allocation**: Understanding how to calculate GPU-hours based on the number of GPUs per job, walltime per job, and the number of jobs.
- **Software Requirements**: Identifying specific software needs (Pytorch, Transformers) for research projects.
- **Account Activation**: Process for enabling HPC accounts on specific clusters (Alex).

## Root Cause of the Problem
- User needed access to the Alex cluster for their research project.

## Solution
- HPC Admin enabled the user's HPC account on the Alex cluster.

## Notes
- This ticket serves as a reference for enabling user accounts on specific clusters and understanding resource allocation for research projects.
---

### 2022030142001229_Early-Alex%20%22Muhammad%20Muzammil%22%20_%20iwi9011h.md
# Ticket 2022030142001229

 ```markdown
# HPC Support Ticket Conversation Analysis

## Subject: Early-Alex / User Account Enablement

### Keywords:
- Account Enablement
- Alex Cluster
- Documentation
- Certificate Expiration
- GPGPU Cluster
- Nvidia A100, A40 GPGPUs
- Pytorch/Singularity
- 3D Lightfield Project

### Summary:
- **User Request:** Access to Alex Cluster for 3D capturing and reconstruction project.
- **Required Resources:** Nvidia A100 and A40 GPGPUs.
- **Software Needed:** Pytorch/Singularity.
- **Project Details:** Lightfield Project under the supervision of a professor.

### Root Cause of the Problem:
- User's certificate had expired.

### Solution:
- HPC Admin enabled the user's account on Alex Cluster.
- Provided documentation link for further instructions.

### General Learnings:
- Ensure certificates are up-to-date for seamless account access.
- Documentation is crucial for user guidance post-account enablement.
- Proper communication of resource requirements and project details is essential for efficient support.
```
---

### 2024051642002998_Job%20817768%20on%20TinyGPU%20uses%20only%20one%20GPU%20of%20two%20allocated.md
# Ticket 2024051642002998

 # HPC Support Ticket Analysis: Job Resource Utilization

## Keywords
- Job ID: 817768
- TinyGPU
- A100 GPUs
- Resource utilization
- Job monitoring
- Metrics: `acc_utilization`, `nv_mem_util`
- Multiple GPUs

## Summary
A job on TinyGPU was observed to be using only one of the two allocated A100 GPUs. The HPC Admin notified the user about the underutilization of resources and provided a link to the job monitoring metrics.

## Root Cause
- The job was not configured to utilize all allocated GPUs effectively.

## Solution
- Ensure that future jobs are configured to use all requested resources.
- Verify job configuration to distribute workload across all allocated GPUs.

## Learning Points
- Monitor job resource utilization to ensure efficient use of allocated resources.
- Use job monitoring tools and metrics to identify underutilization.
- Configure jobs to make full use of allocated GPUs to optimize performance and resource allocation.

## Follow-Up
- The job was later observed to be running on multiple GPUs, indicating a possible resolution of the issue.

## Additional Notes
- Investigation is ongoing regarding the display of all metrics in the job monitoring tool.

---

This documentation aims to help support employees identify and resolve similar resource utilization issues in the future.
---

### 2022022442002099_SSH%20bei%20mehreren%20Jobs.md
# Ticket 2022022442002099

 # HPC-Support Ticket: SSH bei mehreren Jobs

## Keywords
- SSH
- Screen
- Job submission
- nvidia-smi
- GPU utilization
- Interactive job

## Problem Description
The user started an interactive job on `tinygpu`, logged in via SSH using a screen session, and started the actual work. Later, the user submitted another job, which also started on the same node (`tg037`). When the user connected to `tg037` in another screen session via SSH, they expected to see the latest job in `nvidia-smi`, but instead saw the job started in the first SSH screen session.

## Root Cause
The user's expectation was that each SSH session would correspond to a different job, but in reality, both SSH sessions were showing the same job because they were connected to the same node and GPU.

## Solution
The user needs to understand that multiple SSH sessions to the same node will show the same GPU utilization if the jobs are running on the same GPU. To monitor different jobs, the user should ensure that they are submitted to different nodes or GPUs.

## General Learning
- Multiple SSH sessions to the same node will show the same GPU utilization if jobs are running on the same GPU.
- Users should be aware that interactive jobs and submitted jobs may share the same resources if not properly allocated.
- `nvidia-smi` shows the GPU utilization for the node, not for individual SSH sessions.

## Next Steps
- Educate the user on how to properly allocate resources for different jobs.
- Ensure the user understands the behavior of `nvidia-smi` and SSH sessions.

## Related Documentation
- [SSH and Screen Usage Guide](#)
- [Job Submission Best Practices](#)
- [GPU Resource Allocation](#)

## Ticket Status
- Resolved

## Assigned To
- 2nd Level Support Team
---

### 2025010942002006_Job%20on%20TinyGPU%20is%20only%20using%201%20of%204%20GPU%20%5Bvlgm103v%5D.md
# Ticket 2025010942002006

 # HPC Support Ticket: Job on TinyGPU Using Only 1 of 4 GPUs

## Keywords
- GPU utilization
- Job monitoring
- Resource allocation
- `nvidia-smi`
- ClusterCockpit
- `srun`

## Problem
- User's job on TinyGPU is only utilizing 1 out of 4 allocated GPUs.

## Root Cause
- The user's code is not efficiently utilizing the allocated GPU resources.

## Solution
- **Monitoring**:
  - Use ClusterCockpit at [monitoring.nhr.fau.de](https://monitoring.nhr.fau.de/) to view GPU utilization.
  - Attach to the running job using `srun --pty --overlap --jobid YOUR-JOBID bash` and run `nvidia-smi` to check GPU utilization.

- **Resource Allocation**:
  - Ensure that the code can make use of the allocated GPUs.
  - Only allocate GPU nodes if the code can utilize them to avoid resource wastage.

## Actions Taken
- HPC Admins notified the user about the underutilization of GPUs.
- Provided instructions on how to monitor GPU usage.
- Warned about potential account throttling if the issue is not resolved.

## Lessons Learned
- Regularly monitor GPU utilization to ensure efficient resource usage.
- Allocate GPU resources only if the code can effectively use them.
- Use provided monitoring tools and commands to diagnose and resolve resource utilization issues.

## Follow-up
- If the issue persists, the user's account may be throttled.
- Contact HPC support for further assistance if needed.

## References
- ClusterCockpit: [monitoring.nhr.fau.de](https://monitoring.nhr.fau.de/)
- HPC Support Email: [support-hpc@fau.de](mailto:support-hpc@fau.de)
- HPC Website: [hpc.fau.de](https://hpc.fau.de/)
---

### 2024120742000092_Tier3-Access-Alex%20%22Tri-Thien%20Nguyen%22%20_%20iwi5254h.md
# Ticket 2024120742000092

 # HPC Support Ticket Analysis

## Keywords
- Tier3 Access
- Alex
- GPGPU Cluster
- Nvidia A100
- Nvidia A40
- GPU-hours
- Python
- CUDA
- Diffusion Models
- Large Language Models
- Medical Image Data
- Radiology

## Summary
- **User Request**: Access to the GPGPU cluster 'Alex' for training diffusion models and fine-tuning large language models on medical image data.
- **Resources Requested**:
  - Nvidia A100 GPGPUs (9.7 TFlop/s double precision)
  - Nvidia A40 GPGPUs (48 GB, 37 TFlop/s single precision)
  - 2700 GPU-hours
- **Software Requirements**: Python with various libraries and CUDA acceleration.
- **Expected Outcomes**: Development of new AI applications in radiology.

## Actions Taken
- **HPC Admin**: Granted access to the user for the 'Alex' cluster.

## Lessons Learned
- **Access Granting**: Ensure proper communication and confirmation when granting access to HPC resources.
- **Resource Allocation**: Understand the specific hardware and software requirements for specialized tasks like AI model training.
- **User Support**: Provide clear instructions and support for users to effectively utilize the allocated resources.

## Root Cause of the Problem
- User needed access to specific HPC resources for AI model training and development.

## Solution
- Access to the 'Alex' cluster was granted by the HPC Admin.

## Future Reference
- For similar requests, ensure to verify the user's needs, allocate appropriate resources, and provide necessary support for effective utilization.
---

### 2023091342000249_GPU%20Nutzung%20Masterarbeit.md
# Ticket 2023091342000249

 ```markdown
# HPC-Support Ticket Conversation: GPU Nutzung Masterarbeit

## Keywords
- GPU/CPU Rechenleistung
- Abschlussarbeit
- Neuronale Netze
- Zeitreihen
- Remotedesktop
- HPC Ressourcen
- Zugang
- Lehrstuhl
- Formular
- GPU Cluster
- TinyGPU
- Linux
- ssh
- Kommandozeile
- Getting Started Guide
- Anfänger Einführung

## Problem
- User requires GPU/CPU computing power for training large neural networks for time series analysis.
- Current setup on a private computer is time-consuming.
- User inquires about the possibility of using FAU's computing resources, preferably via a remote desktop.

## Solution
- HPC resources are available for free for thesis work.
- Access must be requested through the user's department using the form available at [HPC-Antrag](https://www.rrze.fau.de/files/2017/06/HPC-Antrag.pdf).
- Recommended cluster: [TinyGPU](https://hpc.fau.de/systems-services/documentation-instructions/clusters/tinygpu-cluster/).
- Clusters run on Linux and are accessed via ssh and command line.
- General usage overview available in the [Getting Started Guide](https://hpc.fau.de/systems-services/documentation-instructions/getting-started/).
- Monthly beginner introduction sessions are held, with the next one at 16:00 on the same day via [Zoom](https://fau.zoom.us/j/63416831557).

## General Learnings
- HPC resources are available for academic projects such as thesis work.
- Access requires a formal application through the user's department.
- Specific clusters like TinyGPU are suitable for GPU-intensive tasks.
- Basic knowledge of Linux, ssh, and command line is necessary for accessing HPC clusters.
- Regular introductory sessions are offered to help new users get started.
```
---

### 2023041842003479_Tier3-Access-Alex%20%22Michael%20Fast%22%20_%20iwal121h.md
# Ticket 2023041842003479

 # HPC Support Ticket Analysis

## Keywords
- HPC Account Activation
- Certificate Expiration
- GPGPU Cluster 'Alex'
- Nvidia A100 GPUs
- PyTorch CUDA
- CycleGAN Architecture
- Speech Signal Processing

## Summary
- **User Request:** Access to GPGPU cluster 'Alex' for speech signal processing using CycleGAN architecture with PyTorch CUDA.
- **Issue:** Certificate expiration.
- **Action Taken:** HPC Admin activated the user's account on 'Alex'.

## Root Cause
- Expired certificate prevented account activation.

## Solution
- HPC Admin manually activated the user's account after verifying the request.

## General Learnings
- Regularly check and renew certificates to avoid access issues.
- Ensure timely communication with users regarding account status and certificate validity.

## Next Steps for Similar Issues
- Verify certificate status.
- Manually activate the account if the certificate is valid or renewed.
- Inform the user about the account activation and any relevant details.

---

**Note:** Always ensure that the user's requested resources and software are available and compatible with the cluster.
---

### 2023122242001395_Alex%20Slurm%20select%20a100%20with%2080%20gb.md
# Ticket 2023122242001395

 ```markdown
# HPC-Support Ticket: Selecting A100 with 80GB in Slurm

## Keywords
- Slurm
- A100 GPU
- 80GB
- Partition
- GRES

## Problem
The user wants to select the A100 GPU with 80GB memory on the Alex cluster using Slurm. The user provided the following lines in their Slurm script:
```bash
#SBATCH --partition=a100
#SBATCH --gres=gpu:a100:1
```
The user needs to modify these lines to access the 80GB versions of the A100 GPU.

## Solution
The HPC Admin provided the correct Slurm directives to select the A100 GPU with 80GB memory:
```bash
#SBATCH --partition=a100
#SBATCH --gres=gpu:a100_80:1
```

## What to Learn
- To select specific GPU configurations in Slurm, the `--gres` directive should be used with the appropriate GPU type and memory specification.
- The partition directive (`--partition`) should be correctly set to the partition that supports the desired GPU configuration.
```
---

### 2024052742003494_Tier3-Access-Alex%20%22Sai%20Krishna%20Sravanthi%22%20_%20ob02ubig%40fau.de.md
# Ticket 2024052742003494

 ```markdown
# HPC Support Ticket Analysis

## Subject
Tier3-Access-Alex

## Keywords
- HPC Account
- Supervisor Contact
- Alex Access
- GPGPU Cluster
- Nvidia A100
- Software Requirements
- Sensation Project

## Problem
- User does not have an HPC account.

## Root Cause
- User attempted to access the GPGPU cluster 'Alex' without an active HPC account.

## Solution
- User needs to contact their supervisor to obtain an HPC account.
- Once the account is active, the user should contact HPC support again for access to Alex.

## General Learnings
- Ensure users have an active HPC account before granting access to specific resources.
- Users should follow the proper procedure for account creation and resource access.
- HPC support should guide users to contact their supervisors for account creation.

## Additional Information
- Required Software: Python, Pytorch, Jupyter Notebook, CUDA and cuDNN, OpenCV, Docker
- Project: Sensation Project
- Expected Outcomes: Segmented images, performance metrics, model comparisons
```
---

### 2023020842002608_Tier3-Access-Alex%20%22Dustin%20Vivod%22%20_%20bccc002h.md
# Ticket 2023020842002608

 # HPC Support Ticket: Tier3-Access-Alex

## Keywords
- GPU hours
- NHR project
- LAMMPS
- Nanoparticle simulation
- Slurm

## Summary
- **User Request**: Access to GPGPU cluster 'Alex' for ~30,000 GPU hours.
- **Application**: Simulation of functionalized nanoparticles using LAMMPS.
- **Issue**: Request exceeds Tier3 basic supply, requiring NHR project inclusion.

## Conversation Flow
1. **User**: Requested access to GPGPU cluster 'Alex' for ~30,000 GPU hours.
2. **HPC Admin**:
   - Informed user that the request exceeds Tier3 basic supply.
   - Asked user to clarify with the professor about adding to an existing NHR project or submitting a new one.
   - Temporarily granted access to 4 GPUs.
3. **User**: Confirmed to be added to the existing NHR project.
4. **HPC Admin**: Updated Slurm with the user's project association.

## Root Cause
- User requested GPU hours exceeding the basic Tier3 supply.

## Solution
- User was temporarily granted access to 4 GPUs.
- User was added to an existing NHR project to accommodate the larger GPU hour request.

## General Learnings
- Large GPU hour requests may require association with an NHR project.
- Temporary access can be granted while awaiting project association.
- Slurm can be updated to reflect project associations.
---

### 2025012242002704_GPU%20allocated%20but%20not%20utilized%20-%20b250be14.md
# Ticket 2025012242002704

 # GPU Allocation Issue - JobID 2323423

## Keywords
- GPU utilization
- Python packages
- Compute node
- Interactive job
- ClusterCockpit
- `srun`
- `nvidia-smi`

## Problem
- User's job allocated GPU resources but did not utilize them.
- Previous jobs by the user had similar issues.

## Root Cause
- Python packages intended to use the GPU were not installed on the compute node.
- The user installed packages on the frontend node, which lacks GPU access.

## Solution
- Install Python packages on the compute node using an interactive job.
- Allocate a node interactively using the `salloc` command.
- Verify GPU utilization using `nvidia-smi` after attaching to the running job with `srun --pty --overlap --jobid YOUR-JOBID bash`.

## Monitoring
- Use ClusterCockpit to monitor job performance and GPU utilization.

## Best Practices
- Ensure GPU resources are only allocated if the job can utilize them.
- Properly install dependencies on the compute node for jobs requiring GPU access.

## References
- [Interactive Job Documentation](https://doc.nhr.fau.de/clusters/alex/#interactive-job)
- [ClusterCockpit Monitoring](https://doc.nhr.fau.de/job-monitoring-with-clustercockpit/)

## Status
- Ticket closed as recent jobs are running appropriately.
---

### 2025012342001838_Query%20regarding%20GPU%20hours%20limit.md
# Ticket 2025012342001838

 # HPC Support Ticket: Query Regarding GPU Hours Limit

## Keywords
- GPU hours limit
- Quota
- Job execution
- NHR normal project
- JARDS
- Starter project continuation

## Problem
- User has nearly exhausted their GPU hours quota (9847 out of 10,000 hours).
- Last job was not running due to insufficient GPU hours.

## Cause
- GPU hours limit reached for the user's account.

## Solution
- **Immediate Action**: The job will be executed regardless of quota once resources are available.
- **Long-term Solution**: The Principal Investigator (PI) can apply for an NHR normal project via JARDS. This can be handled as a continuation of the current NHR starter project, allowing the user to keep their accounts and stored data.

## General Learnings
- Jobs can still be executed even if the GPU hours quota is exceeded, depending on resource availability.
- For additional GPU hours, PIs can apply for an NHR normal project through JARDS.
- Continuation of starter projects is possible, preserving existing accounts and data.

## Related Links
- [JARDS Application Portal](https://jards.nhr-verein.de/)
- [FAU HPC Support](mailto:support-hpc@fau.de)
- [FAU HPC Website](https://hpc.fau.de/)
---

### 2024082042002886_Tier3-Access-Alex%20%22Ashif%20Ali%20Poothanali%22%20_%20wy36qeca%40fau.de.md
# Ticket 2024082042002886

 ```markdown
# HPC Support Ticket Analysis: Tier3-Access-Alex

## Keywords
- Tier3 Access
- GPGPU Cluster 'Alex'
- Nvidia A100 GPGPUs
- Nvidia A40 GPGPUs
- GPU-hours
- openmpi, cmake, intel
- Pipe simulation
- Direct simulation
- IBM with GPU based Neko code
- Supervisors
- Expected results
- Contact form

## Summary
- **User Request**: Access to GPGPU cluster 'Alex' for running pipe simulations using Neko code.
- **Resources Requested**:
  - Nvidia A100 GPGPUs (9.7 TFlop/s double precision)
  - Nvidia A40 GPGPUs (48 GB, 37 TFlop/s single precision)
  - 960 GPU-hours
- **Software Needed**: openmpi, cmake, intel
- **Application**: Pipe simulation with added homogenous roughness as a direct simulation using IBM with GPU based Neko code.
- **Supervisors**: Two supervisors mentioned.
- **Expected Results**: bgce project, conference papers.

## Interaction
- **HPC Admin**: Confirmed the request was for the user's account `iwst101h`.
- **User**: Confirmed the request was for the account `iwst101h`.
- **HPC Admin**: Granted access to the user for the GPGPU cluster 'Alex'.

## Root Cause
- User needed access to specific HPC resources for a research project.

## Solution
- HPC Admin verified the account and granted access to the requested resources.

## General Learnings
- Importance of verifying user accounts before granting access to HPC resources.
- Clear communication between users and HPC Admins ensures proper allocation of resources.
- Documentation of resource requests and approvals is crucial for tracking and future reference.
```
---

### 2025013142002572_HPC%20Issue.md
# Ticket 2025013142002572

 ```markdown
# HPC Support Ticket: Connection Issue to tinygpu Cluster

## Keywords
- Connection issue
- tinygpu cluster
- Frontend node
- Memory usage

## Problem Description
User reported difficulty connecting to the tinygpu cluster.

## Root Cause
Excessive memory usage by other users on the frontend node.

## Solution
HPC Admin killed the processes taking up too much memory, allowing the user to connect again.

## Lessons Learned
- Monitor memory usage on frontend nodes.
- Regularly check for processes consuming excessive resources.
- Communicate with users about resource limits and best practices.
```
---

### 2022081242001324_GPU%20cluster.md
# Ticket 2022081242001324

 # HPC Support Ticket: GPU Cluster Limits

## Keywords
- GPU limits
- User-based limits
- Group-based limits
- Project configuration

## Problem
- A user (`p101ae13`) was limited to using up to 16 GPUs while other users could use up to 32 GPUs.
- The user inquired about increasing their GPU limit to match the higher limit available to others.

## Root Cause
- The project was initially configured with user-based limits, which restricted the user `p101ae13` to 16 GPUs.

## Solution
- The HPC Admin changed the project configuration from user-based limits to group-based limits.
- This change provides more flexibility and allows the user `p101ae13` to potentially use up to 32 GPUs, aligning with the limits available to other users.

## Additional Information
- The project currently has 114 GPUs running in total.
- The change was made to offer the most flexibility in GPU usage within the project.

## Action Taken
- The HPC Admin updated the project configuration to group-based limits.

## Follow-Up
- Verify that the user `p101ae13` can now access up to 32 GPUs.
- Monitor the overall GPU usage to ensure it remains within the project's allocated resources.
---

### 2023032042004582_Alex%20GPU%20Cluster%3A%20Virtual%20memory.md
# Ticket 2023032042004582

 # HPC Support Ticket: Alex GPU Cluster Virtual Memory

## Keywords
- Virtual Memory
- GPU Cluster
- A40 GPU
- A100 GPU
- Host Memory
- Swap

## Problem
- User's job aborts when virtual memory usage exceeds 65 GB on A40 GPU nodes.
- User inquires about available virtual memory per GPU and possibility to increase allocatable virtual memory.

## Root Cause
- Limited host memory allocation per GPU.
- Misunderstanding between virtual memory and host memory.

## Information Provided
- **A40 GPU Nodes:** 60 GB host memory allocated per GPU.
- **A100 GPU Nodes:** 120 GB (or 240 GB for 80 GB GPUs) host memory allocated per GPU.
- Swap is disabled on all HPC nodes, making all accessed memory equivalent to host memory.

## Solution
- The amount of allocated host memory per GPU cannot be influenced or increased.
- Clarification that virtual memory usage corresponds to direct host memory usage due to disabled swap.

## General Learning
- Understanding the distinction between virtual memory and host memory.
- Awareness of host memory allocation limits per GPU type on the Alex GPU Cluster.
- Importance of swap settings in memory management on HPC clusters.

## Roles Involved
- **HPC Admins:** Provided detailed information on memory allocation and swap settings.
- **User:** Reported the issue and sought clarification on memory usage.

## Related Teams
- 2nd Level Support Team
- Software and Tools Developers
- Training and Support Group
- NHR Rechenzeit Support and Applications for Grants
---

### 2025013042001717_Jobs%20on%20TinyGPU%20use%20only%201%20of%202%20GPUs%20%5Biwb3111h%5D.md
# Ticket 2025013042001717

 # HPC Support Ticket: Jobs on TinyGPU Use Only 1 of 2 GPUs

## Keywords
- GPU utilization
- TinyGPU
- JobIDs
- ClusterCockpit
- `srun`
- `nvidia-smi`

## Problem Description
- User's running jobs on TinyGPU (JobIDs 984251, 984145) were using only one of the two allocated GPUs.

## Root Cause
- The user's code was not properly configured to utilize both GPUs.

## Solution
- The user acknowledged the issue and corrected the scripts for future jobs.

## Steps for Monitoring and Diagnosis
1. **Monitoring System**:
   - Log into ClusterCockpit at [monitoring.nhr.fau.de](https://monitoring.nhr.fau.de/) to view GPU utilization.

2. **Attach to Running Job**:
   - Use `srun --pty --overlap --jobid YOUR-JOBID bash` to get a shell on the first node of the job.
   - Run `nvidia-smi` to see the current GPU utilization.

## Best Practices
- Ensure that jobs allocate GPU resources only if the code can make use of them.
- Regularly monitor GPU utilization to avoid idle resources.

## Conclusion
- The user was informed about the issue and corrected the scripts for future jobs.
- The current jobs were allowed to run to completion.

---

This documentation can be used to address similar issues in the future by following the steps for monitoring and diagnosis.
---

### 2024032842003405_Jobs%20on%20tinyGPU%20do%20not%20utilize%20all%20allocated%20GPUs%20-%20iweb100h.md
# Ticket 2024032842003405

 # HPC Support Ticket: Jobs on TinyGPU Do Not Utilize All Allocated GPUs

## Keywords
- GPU utilization
- Job monitoring
- ClusterCockpit
- `nvidia-smi`
- Resource allocation

## Problem Description
- User's jobs on TinyGPU (JobID 792949, 792942, 793008) only use two of the allocated GPUs.
- Resources are idle and not available to other users.

## Root Cause
- User forgot to update the job description file after switching from distributed model training on multiple GPUs.

## Solution
- User acknowledged the issue and agreed to fix the job description file.

## Steps for Monitoring and Troubleshooting
1. **Monitoring System**:
   - Log into ClusterCockpit to view GPU utilization.
   - Reference: [Job Monitoring with ClusterCockpit](https://doc.nhr.fau.de/job-monitoring-with-clustercockpit/)

2. **Attach to Running Job**:
   - Use `srun --pty --overlap --jobid YOUR-JOBID bash` to get a shell on the first node of the job.
   - Run `nvidia-smi` to see the current GPU utilization.

## Best Practices
- Ensure that jobs only allocate nodes with GPUs if the code can actually utilize them.
- Regularly check job descriptions to avoid resource wastage.

## Contact
- For further assistance, contact HPC Support at [support-hpc@fau.de](mailto:support-hpc@fau.de).

---

This documentation aims to help HPC support employees troubleshoot similar issues related to GPU utilization and resource allocation.
---

### 2024070242000824_Tier3-Access-Alex%20%22Siavash%20Toosi%22%20_%20iwst088h.md
# Ticket 2024070242000824

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject: Tier3-Access-Alex

### Keywords:
- GPU-hour demand
- NHR project
- Alex cluster
- Nvidia A100
- Nvidia A40
- CUDA compiler
- MPI
- CFD solver
- NEKO
- Single precision
- Double precision
- Performance issues
- High-fidelity simulations
- DNS
- LES
- Finite-difference code

### Summary:
- **User Request**: Access to the Alex cluster for running a high-order, spectral-element CFD solver (NEKO) on Nvidia GPUs.
- **Expected GPU-hour Demand**: 10,000 hours.
- **Software Requirements**: CUDA compiler, MPI.
- **Goals**:
  - Compile and run NEKO on Nvidia GPUs.
  - Test single vs. double precision for simulations.
  - Discover and solve performance issues.
  - Potentially port a finite-difference code to Nvidia GPUs.

### HPC Admin Response:
- **Access Granted**: User is allowed to use Alex.
- **Note on GPU-hour Demand**: The expected demand is at the low end of an NHR project. If actual demand is high, an application may be required.
- **Reference Link**: [NHR Application Details](https://doc.nhr.fau.de/nhr-application/)

### Learnings:
- **GPU-hour Demand Management**: Monitoring and potentially requiring an application for high GPU-hour demands.
- **Software and Hardware Requirements**: Understanding the specific needs for CFD solvers and GPU-based simulations.
- **Precision Testing**: Importance of testing single vs. double precision for high-fidelity simulations.
- **Performance Optimization**: Identifying and addressing performance issues in GPU-based computations.

### Root Cause of the Problem:
- **High GPU-hour Demand**: The user's expected GPU-hour demand is significant, which may require an application for an NHR project.

### Solution:
- **Access Granted**: The user has been granted access to the Alex cluster.
- **Potential Application**: If the actual GPU-hour demand is high, the user may need to submit an application for an NHR project.
```
---

### 2024012842000653_Extend%20Slurm%20job.md
# Ticket 2024012842000653

 # HPC Support Ticket: Extend Slurm Job

## Subject
- Extend Slurm job

## User
- PhD candidate at Universität Hamburg, Department of Informatics, SP Research Group

## HPC Admins
- Johannes Veh

## Key Points

### Initial Request
- User requested to extend Slurm job with ID 1064182 on cluster Alex for a total runtime of 4 days.

### Issues Encountered
- Job ended after 4 minutes with a Python error.
- User attempted to reserve 2 A100 GPUs with 80 GB but encountered an error indicating only one GPU was available.

### Solutions Provided
- HPC Admin suggested using `--hold` to start jobs that need to be extended to control where the job runs and reduce fragmentation.
- HPC Admin corrected the Slurm script to properly request 2 A100 GPUs:
  ```bash
  #SBATCH --partition=a100
  #SBATCH --gres=gpu:a100:2
  #SBATCH -C a100_80
  ```

### Additional Requests
- User requested extensions for multiple jobs (IDs 1065016, 1065334, 1065892, 1075721, 1075719, 1075957, 1076145) with varying runtimes.
- HPC Admin extended the job runtimes as requested but noted that jobs were spread across different nodes, which might require adjustments if demand for whole nodes increases.

### Follow-up Issues
- Some jobs failed due to script errors (e.g., unrecognized arguments, file not found).
- HPC Admin provided feedback on the specific errors encountered.

### Final Request
- User requested an extension for job ID 1075957 for a total runtime of 7 days and inquired about the best practice for requesting extensions for multiple jobs.

## Lessons Learned
- Use `--hold` for jobs that may need to be extended to control job placement and reduce fragmentation.
- Ensure proper Slurm script configuration for GPU reservations.
- Address script errors promptly to avoid job failures.
- Request job extensions in a timely manner to allow for necessary adjustments.

## Keywords
- Slurm job extension
- GPU reservation
- Python error
- Job fragmentation
- Slurm script configuration
- Job runtime adjustment
- HPC support
- Job failure troubleshooting
---

### 2022062742002899_AW%3A%20Kontaktherstellung%20HPC%20-%20Andreas%20Eberl%20%28Wolbring%29.md
# Ticket 2022062742002899

 # HPC Support Ticket Conversation Analysis

## Keywords
- HPC Account
- TinyGPU
- Alex Cluster
- GPU Stunden
- NHR Antrag
- Unix Permissions
- Shared Verzeichnis
- FAU-Grundversorgung
- Batchsystem
- Passwortänderungen
- HPC-Cafe
- Dokumentation

## What Can Be Learned

### General Information
- **HPC Account Setup**: The process involves creating an HPC ID and setting a password through the IdM portal.
- **Cluster Access**: Users need to demonstrate efficient hardware usage and appropriate compute time requirements to gain access to specific clusters like Alex.
- **GPU Stunden**: The actual usage is tracked, not just the requested time. Good estimates with a safety buffer are recommended.
- **Permissions**: Users can set read and write permissions on their $WORK directories using Unix permissions.
- **Support Resources**: The HPC-Cafe and documentation are valuable resources for new users.

### Specific Issues and Solutions

#### Issue: Access to Alex Cluster
- **Root Cause**: The user needed access to the Alex cluster for 80GB A100 GPUs.
- **Solution**: The user was informed that access would be granted once they demonstrated efficient hardware usage and appropriate compute time requirements.

#### Issue: Shared Directory for Collaboration
- **Root Cause**: The user group needed a shared directory for collaborative work.
- **Solution**: The user was advised to set Unix permissions on their $WORK directories to allow read and write access within the group.

#### Issue: GPU Stunden Calculation
- **Root Cause**: The user was unsure if the GPU hours were calculated based on requested or actual usage.
- **Solution**: The user was informed that the actual usage is tracked, and good estimates with a safety buffer are recommended.

#### Issue: Password Changes
- **Root Cause**: Password changes were not immediately recognized on all HPC systems.
- **Solution**: The user was informed that it generally takes a few hours for password changes to be recognized, and changes occur at different times on all clusters.

#### Issue: HPC-Cafe and Documentation
- **Root Cause**: New users needed guidance on using HPC resources.
- **Solution**: The user was recommended to participate in the HPC-Cafe and refer to the documentation for getting started.

## Conclusion
The conversation highlights the importance of clear communication regarding HPC account setup, cluster access, GPU hours calculation, permissions, and available support resources. The solutions provided address specific user concerns and offer guidance for efficient hardware usage and collaborative work.
---

### 2024090342002728_Job%20on%20Alex%20has%20been%20killed%20as%20it%20no%20longer%20made%20use%20of%20GPUs%20-%20b207dd1.md
# Ticket 2024090342002728

 # HPC Support Ticket: Job Killed Due to GPU Inactivity

## Keywords
- Job killed
- GPU inactivity
- Job script
- Job termination

## Summary
A job was terminated by the HPC admin because it stopped utilizing its allocated GPUs for more than 2 hours.

## Root Cause
The job script did not properly terminate the job after completing its work, leading to inefficient use of GPU resources.

## Solution
Ensure that job scripts are designed to terminate the job once the work is completed. This can be achieved by adding appropriate exit conditions or commands in the script.

## General Learning
- Always verify that job scripts include proper termination conditions to avoid wasting computational resources.
- Regularly monitor job activity to ensure efficient use of HPC resources.

## Actions Taken
- The HPC admin notified the user about the issue and provided guidance on fixing the job script.

## References
- [FAU HPC Support](mailto:support-hpc@fau.de)
- [FAU HPC Website](https://hpc.fau.de/)

---

This documentation can help support employees identify and resolve similar issues related to job termination and resource utilization.
---

### 2020092342001467_Access%20to%20GPUs%20for%20master%20thesis.md
# Ticket 2020092342001467

 ```markdown
# HPC-Support Ticket: Access to GPUs for Master Thesis

## Keywords
- GPU access
- Master thesis
- Network training
- siMLopt project
- LEB chair
- RRZE

## Summary
A user requests access to GPUs for training networks as part of their Master thesis and the siMLopt project under the LEB chair. The user also seeks information on alternative resources if GPUs are not available from the RRZE.

## Root Cause
- User requires GPU resources for network training.
- Potential unavailability of GPUs from the RRZE.

## Solution
- HPC Admin (Michael) suggests considering access to HPC resources.
- No final resolution provided in the conversation.

## General Learnings
- Users may need GPU access for academic projects.
- Alternative resources should be suggested if internal GPUs are unavailable.
- HPC resources might be a viable option for such requests.
```
---

### 2022121942004024_Tier3-Access-Alex%20%22Cem%20Karatastan%22%20_%20iwi5124h.md
# Ticket 2022121942004024

 # HPC Support Ticket Analysis: Tier3-Access-Alex

## Keywords
- Tier3 Access
- A100 GPUs
- Efficient GPU usage
- Code optimization
- Deep learning
- Vision transformer
- Data preprocessing
- Parallel processing
- Master's thesis

## Summary
A user requested access to the Alex cluster with A100 GPUs for their master's thesis involving deep learning and vision transformers. The user needed multiple GPUs for model training and data preprocessing due to the large datasets involved.

## Root Cause of the Problem
- Inefficient use of GPU resources on the current cluster (woody).
- Lack of experience in optimizing code for multi-GPU usage.

## HPC Admin Response
- The Alex cluster is reserved for experienced HPC users.
- The user was advised to demonstrate efficient A100 GPU usage on the TinyGPU cluster first.
- The HPC team lacked resources to provide extensive support for code optimization.
- The user was directed to seek help from their supervisors.

## Solution
- The user should gain experience and demonstrate efficient GPU usage on a smaller cluster (TinyGPU) before accessing the Alex cluster.
- For code optimization, the user should consult their supervisors or other resources.

## General Learnings
- Access to advanced HPC resources may require demonstration of efficient usage on smaller systems.
- HPC support teams may have limited resources for extensive user training.
- Users should engage with their supervisors or relevant resources for code optimization.
- Efficient GPU usage is crucial for accessing high-performance clusters.
---

### 2024041042003311_Tier3-Access-Alex%20%22%C3%83%C2%96mer%22%20_%20iwal119h.md
# Ticket 2024041042003311

 # HPC Support Ticket Analysis: Tier3-Access-Alex

## Keywords
- HPC Account
- Alex Cluster
- Nvidia A40 GPGPUs
- GPU-hours
- NN Training Software
- Python
- Speech Transmission Scheme
- PhD Student
- University Credentials

## Summary
A PhD student requested access to the HPC cluster 'Alex' for a project involving neural network training for speech transmission schemes. The request included specific hardware requirements (Nvidia A40 GPGPUs) and a significant amount of computational resources (12,000 GPU-hours).

## Key Learnings
- **Account Setup**: The HPC account was initially set up under different credentials but was enabled for the requested cluster.
- **Resource Allocation**: The user specified the need for a large amount of GPU-hours, indicating the scale of the project.
- **Software Requirements**: The project involves custom NN training software developed by the user's group, highlighting the need for flexibility in software support.
- **Collaboration**: The user mentioned the possibility of contacting their PhD advisor, suggesting a collaborative approach between the university and external institutions.

## Root Cause of the Problem
- The user needed access to specific HPC resources for a large-scale project, which required enabling their account on the 'Alex' cluster.

## Solution
- The HPC Admin enabled the user's account on the 'Alex' cluster, addressing the primary request.

## Additional Notes
- The user provided detailed information about their project and resource needs, which is helpful for efficient ticket resolution.
- The mention of university credentials and the possibility of contacting the PhD advisor indicates a need for verification and collaboration.

This documentation can serve as a reference for handling similar requests for HPC account access and resource allocation.
---

### 2022030142002237_Job%2039836%20auf%20Alex%20nutzt%20nur%204%20der%206%20allokierten%20GPUs%20%5Bbccc013h%5D.md
# Ticket 2022030142002237

 ```markdown
# HPC Support Ticket: Job 39836 on Alex Using Only 4 of 6 Allocated GPUs

## Keywords
- GPU allocation
- Job monitoring
- GPU utilization
- LAMMPS
- nvidia-smi
- Job metrics

## Summary
A user's job (JobID 39836) on the HPC system Alex was allocated 6 GPUs but only utilized 4. The HPC Admin notified the user about the inefficient resource usage and provided a screenshot from the monitoring system. The user responded by canceling the job and resubmitting it with a new script, hoping to utilize all allocated GPUs correctly. The user also inquired about tools to monitor GPU utilization and job metrics.

## Root Cause
- The user's job script was not configured to utilize all allocated GPUs efficiently.

## Solution
- The user canceled the inefficient job and resubmitted it with a new script.
- The HPC Admin confirmed that the new job (JobID 39964) was utilizing all allocated GPUs.

## Learnings
- **Efficient Resource Allocation:** Ensure that job scripts are configured to utilize all allocated resources efficiently.
- **Monitoring GPU Utilization:** Currently, users can monitor GPU utilization by logging into the allocated node and using `nvidia-smi`. However, this tool only shows the utilization of the first GPU.
- **Job Metrics:** There is no current solution for users to access job metrics for completed jobs, similar to the Emmy system. This feature is recognized as beneficial and may be implemented in the future.
- **User Tools:** The tool used by HPC Admins to monitor GPU utilization is not currently accessible to users. Users should rely on internal tools within their applications (e.g., LAMMPS) for detailed GPU utilization metrics.

## Future Actions
- Users should regularly check their job scripts to ensure efficient resource utilization.
- HPC Admins may consider providing users with better tools for monitoring GPU utilization and job metrics.
```
---

### 2022042942001569_Remote%20access%20for%20HPC%20servers%20%28GPU%20usage%29.md
# Ticket 2022042942001569

 # HPC Support Ticket: Remote Access for HPC Servers (GPU Usage)

## Keywords
- Remote access
- GPU servers
- Deep Learning
- Dataset storage
- Account eligibility
- TinyGPU Cluster
- Getting started information
- Application form

## Problem
- User requires GPU servers with at least 8GB GPU RAM and multi-core CPU access for a Deep Learning project.
- User has a dataset of ~350GB which may increase to 500GB.
- User needs remote access to the servers.

## Root Cause
- User is an MSc student in AI and requires HPC resources for a major project.
- User has contacted the CIP team and was redirected to the HPC team for resource allocation.

## Solution
- **HPC Admins** informed the user about the availability of GPU nodes in the TinyGPU Cluster that meet the user's requirements.
- **HPC Admins** clarified that accounts are not given to students who are not affiliated with a research chair of FAU.
- **HPC Admins** provided links to getting started information and the application form for further steps.

## General Learnings
- The TinyGPU Cluster offers GPU nodes suitable for Deep Learning projects.
- Account eligibility for HPC resources is restricted to students affiliated with a research chair of FAU.
- Relevant information for getting started and applying for an account can be found on the HPC website.

## References
- [TinyGPU Cluster Documentation](https://hpc.fau.de/systems-services/systems-documentation-instructions/clusters/tinygpu-cluster/)
- [Getting Started Information](https://hpc.fau.de/systems-services/systems-documentation-instructions/getting-started/)
---

### 2022053042001224_Tier3-Access-Alex%20%22Naveed%20Unjum%22%20_%20iwi5078h.md
# Ticket 2022053042001224

 # HPC Support Ticket: Tier3-Access-Alex

## Subject
Tier3-Access-Alex - Access to GPGPU cluster 'Alex'

## Keywords
- GPGPU cluster
- Alex
- Nvidia A100
- Nvidia A40
- Deep learning
- Generative models
- GANs
- Diffusion models
- Jupyter notebook
- Git
- Module system

## Summary
User requested access to the GPGPU cluster 'Alex' for training deep learning models on millions of images. The user's workflow, data storage, and access patterns were discussed. Issues with Jupyter notebook and git were addressed.

## Issues and Solutions

### Access to Alex Cluster
- **Issue**: User required access to Alex cluster for GPU-intensive tasks.
- **Solution**: Access granted after reviewing the workflow and potential performance impacts.

### Jupyter Notebook Connection
- **Issue**: User unable to run Jupyter notebooks from the browser, encountering "Connection refused" errors.
- **Solution**: Issue could not be reproduced. Alex cluster is meant for production runs, not interactive work. User advised to use JupyterHub service for interactive development.

### Git Installation
- **Issue**: User unable to use git on Alex cluster, command not found.
- **Solution**: User advised to load git module using `module load git`. Documentation on the module system provided.

## Workflow Details
- **Data Storage**: User plans to store datasets (OmniArt and FotoMarburg) on $HPCVAULT.
- **Access Patterns**: User will load datasets using PyTorch DataLoader. Access frequency during training jobs not specified.

## Additional Notes
- User advised to familiarize themselves with the module system documentation.
- No further support for Jupyter on Alex cluster due to its intended use for production runs.

## Conclusion
User's access to Alex cluster was enabled, and issues with git and Jupyter notebook were addressed. User advised to use JupyterHub for interactive development and to load necessary modules for software not available by default.
---

### 2021091642003101_TinyGPU%20node%20tg033.md
# Ticket 2021091642003101

 ```markdown
# HPC Support Ticket: TinyGPU Node tg033

## Keywords
- TinyGPU
- Node tg033
- GPU error
- Cuda driver error 999
- NVRM
- MMU Fault
- Health check script
- Stromausfall (Power outage)

## Summary
A user reported that node tg033 on TinyGPU was not functioning properly. GPU1 showed an error, and calculations could not be started due to a Cuda driver error 999.

## Root Cause
- GPU1 on node tg033 was experiencing errors, specifically a Cuda driver error 999.
- NVRM logs indicated an MMU Fault of type FAULT_INFO_TYPE_UNSUPPORTED_KIND ACCESS_TYPE_READ.

## Actions Taken
- The node was taken offline by HPC Admins.
- The health check script (`/var/spool/torque/mom_priv/health-check.sh`) was reviewed to include the current error message.
- The issue was resolved due to a power outage (Stromausfall).

## Solution
- The node was taken offline and the issue was resolved by a power outage.
- Preventive measures were discussed to detect such errors in the future.

## Lessons Learned
- Regular health checks and monitoring scripts are crucial for detecting hardware issues.
- Power outages can sometimes resolve hardware issues, but preventive measures should be in place to avoid such disruptions.
- Cuda driver errors and NVRM logs should be closely monitored for early detection of GPU issues.
```
---

### 2023112942002374_Tier3-Access-Alex%20%22Lars%20B%C3%83%C2%B6cking%22%20_%20btr0103h.md
# Ticket 2023112942002374

 # HPC Support Ticket Conversation Analysis

## Keywords
- Tier3 Access
- Alex
- GPU-hours
- NHR Proposal
- Job Runtime
- Checkpoint-Restart
- GPGPU Cluster
- Nvidia A100
- Nvidia A40
- Python
- PyTorch
- TensorFlow
- Ray
- Multivariate Time Series Classification
- Research Publications

## General Learnings
- **Account Activation**: The user's account was enabled on the Alex system.
- **Resource Availability**: The free Tier3 basic service may not guarantee the requested GPU-hours.
- **NHR Proposal**: Recommended to apply for compute time via an NHR proposal to ensure resource availability.
- **Job Runtime**: The maximum job runtime on Alex is 24 hours.
- **Checkpoint-Restart**: Suggested to use checkpoint-restart functionality for applications requiring longer runtimes.
- **Software Requirements**: The user needs Ubuntu or equivalent to set up Python with virtual environments and install packages like PyTorch, TensorFlow, and Ray.
- **Application**: The user is conducting research in multivariate time series classification.
- **Expected Outcomes**: The research aims to produce publications.

## Root Cause of the Problem
- The user requested a significant amount of GPU-hours and job runtime that may not be fully supported by the free Tier3 basic service.

## Solution
- Apply for compute time via an NHR proposal to ensure the requested resources are available.
- Use checkpoint-restart functionality for jobs that require longer runtimes than the 24-hour maximum.

## Additional Notes
- The user's specific requirements include 1 GPU per job, with a maximum of 5 jobs in parallel, and a total of 100 jobs with a walltime of 120 hours each.
- The user is affiliated with Fraunhofer FIT and is conducting research in the domain of multivariate time series classification.
---

### 2024103042000275_Job%20on%20Alex%20is%20only%20using%201%20of%204%20GPU%20%5Bv100dd12%5D.md
# Ticket 2024103042000275

 # HPC Support Ticket: Job on Alex is only using 1 of 4 GPU [v100dd12]

## Keywords
- GPU utilization
- Job allocation
- Monitoring system
- ClusterCockpit
- `nvidia-smi`
- `srun`
- PyTorch
- Resource allocation

## Problem
- User's job on Alex is only utilizing 1 out of 4 allocated GPUs.

## Root Cause
- The job configuration may not be optimized to utilize all allocated GPUs.

## Solution
- **Monitoring**: Use ClusterCockpit at [monitoring.nhr.fau.de](https://monitoring.nhr.fau.de/) to view GPU utilization.
- **Attach to Job**: Use `srun --pty --overlap --jobid YOUR-JOBID bash` to attach to the running job and run `nvidia-smi` to check GPU utilization.
- **Configuration**: Ensure the job configuration is set to utilize all allocated GPUs. For example, set `--nproc_per_node=1` to the number of allocated GPUs.
- **Documentation**: Refer to the documentation on working with PyTorch on the cluster: [PyTorch Documentation](https://doc.nhr.fau.de/apps/pytorch).

## General Learnings
- Always verify that jobs are utilizing all allocated resources to avoid wastage.
- Use monitoring tools to diagnose resource utilization issues.
- Properly configure jobs to make full use of allocated resources.
- Refer to documentation for specific applications to ensure optimal usage.

## Actions Taken
- HPC Admin provided guidance on monitoring and configuring the job.
- Ticket closed after providing necessary information and guidance.
---

### 2025022042000502_Job%20cancellation%20seems%20not%20to%20work.md
# Ticket 2025022042000502

 # HPC Support Ticket: Job Cancellation Issue

## Keywords
- Job cancellation
- `scancel` command
- ClusterCockpit
- Delay in job status update
- Multiple clusters (tinyfat, tinygpu)

## Problem Description
- User reported that job cancellation was not working.
- User had followed instructions on the HPC website but was still experiencing issues.

## Root Cause
- The user did not specify the cluster in the `scancel` command.
- There are two clusters (tinyfat and tinygpu) under tinyx, and the command needs to specify which one.

## Solution
- Use the correct `scancel` command with the cluster specified, e.g., `scancel.tinyfat -u <username>`.
- Expect a delay of a few minutes for the job status to update in ClusterCockpit.

## General Learnings
- Always specify the cluster in commands when dealing with multi-cluster environments.
- There may be a delay in the job status update after cancellation.
- HPC Admins can assist in canceling jobs if needed.

## Ticket Conversation Summary
- User reported job cancellation issue.
- HPC Admin provided the correct command and canceled the user's jobs.
- User noticed a delay in job status update in ClusterCockpit.
- HPC Admin confirmed the delay and that jobs were listed as "canceled".

## Related Tools/Commands
- `scancel`
- ClusterCockpit
---

### 2022072942002866_Quota%20for%20iwi5066h.md
# Ticket 2022072942002866

 # HPC Support Ticket: Quota for iwi5066h

## Keywords
- Quota
- GPU access
- Job script
- `sinfo` command
- Idle nodes
- NHR compute time

## Issue
- User unable to request 8 GPUs for training despite nodes showing as idle.
- Potential quota limitation suspected.

## Root Cause
- Limited share of HPC resources available for free basic services.
- Majority of nodes belong to NHR and other universities.

## Solution
- Apply for NHR compute time using university affiliation.
- Application process details available at [NHR Application Rules](https://hpc.fau.de/systems-services/documentation-instructions/nhr-application-rules/).

## General Learning
- Free basic HPC services have limited resource availability.
- NHR compute time application is necessary for larger resource demands.
- Understanding resource allocation and quota limitations is crucial for effective HPC usage.
---

### 2025012842002506_Job%20on%20Alex%20do%20not%20use%20GPU%20%5Bb250be14%5D.md
# Ticket 2025012842002506

 # HPC Support Ticket: Job on Alex Not Using GPU

## Keywords
- GPU utilization
- Job allocation
- Monitoring system
- ClusterCockpit
- `nvidia-smi`
- Resource management

## Summary
A user's jobs on the HPC system were not utilizing the allocated GPUs, leading to resource wastage.

## Root Cause
- The user's jobs (JobID 2338911, 2337825) were allocated GPUs but did not use them.

## Solution
- **Monitoring**: HPC Admins used the monitoring system (ClusterCockpit) to identify the issue and provided a screenshot.
- **User Action**: Users can log into ClusterCockpit to monitor GPU usage.
- **Command**: Users can attach to their running job using `srun --pty --overlap --jobid YOUR-JOBID bash` and run `nvidia-smi` to check GPU utilization.
- **Resource Management**: Ensure that jobs only allocate GPUs if the code can utilize them to avoid resource wastage.

## Follow-Up
- The issue was resolved as new jobs showed better GPU utilization.

## General Learning
- Always verify that jobs are utilizing allocated resources.
- Use monitoring tools and commands to check resource usage.
- Proper resource management is crucial to avoid wastage and ensure efficient use of HPC resources.

## References
- [ClusterCockpit Monitoring System](https://monitoring.nhr.fau.de/)
- [FAU HPC Support](https://hpc.fau.de/)
---

### 2022110942000558_Follow%20up%3A%20HPC%20Caf%C3%83%C2%A9%20Yesterday.md
# Ticket 2022110942000558

 # HPC Support Ticket Analysis

## Subject: Follow up: HPC Café Yesterday

### Keywords:
- HPC Café
- Queued jobs
- GPU resources
- NHR projects
- Slurm
- GDPR
- Alex cluster
- TinyGPU
- Resource allocation

### Summary:
- **User Inquiry**:
  1. Request to view queued jobs from i5 to distribute compute resources more fairly.
  2. Request to create a queue that can use excess GPU resources but stops when other users request them.

- **HPC Admin Response**:
  1. Slurm does not implement a "group view" due to GDPR violations.
  2. Specific cluster and queue information required. On Alex cluster, the solution is to apply for NHR projects.

### Root Cause:
- **Issue 1**: User wants to see queued jobs to manage resource distribution.
  - **Root Cause**: Lack of visibility into job queues.
  - **Solution**: Not feasible due to GDPR concerns.

- **Issue 2**: User wants to utilize unused GPU resources.
  - **Root Cause**: Inefficient resource utilization.
  - **Solution**: Apply for NHR projects to gain access to additional resources.

### General Learnings:
- **GDPR Concerns**: Showing all jobs in a queue can violate GDPR.
- **Resource Allocation**: NHR projects are the recommended way to access additional GPU resources on the Alex cluster.
- **Cluster-Specific Policies**: Different clusters (e.g., TinyGPU, Alex) have different throttling policies and resource allocation methods.

### Action Items:
- **For Users**: Apply for NHR projects to access additional GPU resources.
- **For HPC Admins**: Continue to enforce GDPR compliance and guide users towards appropriate resource allocation methods.

### Additional Notes:
- **Power Costs**: Not the main reason for resource allocation policies.
- **Motivation for NHR Proposals**: Ensuring users submit NHR proposals to access resources.

---

This analysis provides a concise overview of the issues discussed in the support ticket and the corresponding solutions or guidelines provided by the HPC Admins.
---

### 2024041142000527_Tier3-Access-Alex%20%22Philip%20Maier%22%20_%20bccc117h.md
# Ticket 2024041142000527

 # HPC Support Ticket Analysis: Tier3-Access-Alex

## Keywords
- Account activation
- GPGPU cluster 'Alex'
- Nvidia A100, A40 GPGPUs
- LAMMPS software
- Molecular dynamics
- Enhanced sampling
- PhD student
- Affinity and selectivity analysis

## Summary
A PhD student requested access to the GPGPU cluster 'Alex' for molecular dynamics simulations using LAMMPS. The student was unsure about the required GPU hours.

## Root Cause
- New user needing access to HPC resources.
- Uncertainty about computational time requirements.

## Solution
- **HPC Admin** activated the user's account for the 'Alex' cluster.
- No specific solution provided for estimating GPU hours; further guidance may be needed.

## Learning Points
- **Account Activation**: HPC Admins handle account activation for new users.
- **Resource Request**: New users may need guidance on estimating computational resources.
- **Software Compilation**: Users may compile their own software (e.g., LAMMPS) if needed.

## Next Steps
- Provide guidance on estimating computational time.
- Ensure the user has access to necessary software and resources.

---

This documentation can help support employees understand the process of account activation and resource allocation for new users, especially PhD students.
---

### 2022060142000331_Einstellen%20der%20GPU%20Frequenz.md
# Ticket 2022060142000331

 # HPC-Support Ticket: Adjusting GPU Frequency

## Keywords
- GPU frequency adjustment
- Student Cluster Competition
- Energy efficiency measurements
- Slurm `--gpu-freq`
- User permissions

## Summary
A user requested permissions for several students to adjust GPU frequencies for energy efficiency measurements during the Student Cluster Competition.

## Root Cause
The user needed specific permissions to adjust GPU frequencies for their measurements.

## Solution
- The HPC Admin suggested using the `--gpu-freq` option in Slurm to adjust GPU frequencies.
- It was noted that the behavior of Slurm regarding resetting GPU frequencies at job end is unknown.

## General Learnings
- Users may require specific permissions for hardware adjustments, such as GPU frequency changes.
- Slurm's `--gpu-freq` option can be used to adjust GPU frequencies.
- The behavior of Slurm in resetting GPU frequencies after job completion is not well-documented and may require monitoring for potential issues.

## Next Steps
- Monitor the behavior of Slurm regarding GPU frequency resetting.
- Document any issues that arise and provide solutions or workarounds.

## Notes
- Ensure that users are aware of the potential risks and uncertainties when adjusting hardware settings.
- Provide clear documentation on how to use Slurm options for hardware adjustments.
---

### 2024012542003192_Multi-GPU%20training%20on%20Alex%20by%20Stefan%20Frisch.md
# Ticket 2024012542003192

 ```markdown
# Multi-GPU Training on Alex

## Keywords
- Multi-GPU training
- Alex HPC
- Job runtime extension
- Slurm queue
- A100 GPUs
- QoS (Quality of Service)

## Problem
- User wants to perform multi-GPU training on Alex for a long-running task.
- Requests extension of maximum job runtime to 3 days.
- Unsure about the application process for multi-GPU training.

## Root Cause
- High demand for A100 GPUs leading to long waiting times in the Slurm queue.
- User's lack of familiarity with the HPC system and application process.

## Solution
- User's account was enabled for `--qos=a100multi`.
- Informed user about the current backlog and typical waiting times for jobs.
- Advised that extending job runtime is unlikely due to the long queue.

## General Learnings
- Multi-GPU training requires specific QoS settings.
- High demand for resources can lead to extended waiting times.
- Extending job runtime may not be feasible during periods of high demand.
- Users should be informed about the current system load and expected waiting times.
```
---

### 2023021942000732_regarding%20hpc%20getting%20slow%20suddenly.md
# Ticket 2023021942000732

 # HPC Support Ticket: Sudden Decrease in GPU Utilization

## Keywords
- GPU utilization
- Deep learning model
- Tinyx GPU
- A100 version
- Slurm log file
- AssocGrpGRES
- Job start delay

## Problem Description
- User experienced a sudden decrease in GPU utilization since Friday night.
- Training deep learning models using Tinyx GPU (A100 version).
- Running multiple models simultaneously (max 3).

## Root Cause
- Possible heavy usage of TinyGPU by other users/groups (e.g., iCal).
- Job start delay due to too many jobs of the user's group already running (AssocGrpGRES).

## Troubleshooting Steps
- HPC Admin requested slurm log files for good and bad jobs to investigate further.

## Solution
- Not yet resolved in the provided conversation.
- Further investigation required with the provided slurm log files.

## General Learnings
- High GPU usage by other users/groups can impact performance.
- Job start delays can occur due to group job limits (AssocGrpGRES).
- Slurm log files are essential for diagnosing job performance issues.

## Next Steps
- User should provide slurm log files for further analysis.
- HPC Admin to investigate log files and provide additional solutions.
---

### 2024102242004214_Job%20on%20Alex%20uses%20only%20one%20of%204%20GPUs%20%5Bb245da13%5D.md
# Ticket 2024102242004214

 # HPC Support Ticket: Job on Alex Uses Only One of 4 GPUs

## Keywords
- GPU utilization
- Job allocation
- SLURM
- `nvidia-smi`
- Job arrays
- Resource management

## Problem Description
- User's job on Alex (JobID 2108836) was using only 1 of the 4 allocated GPUs.
- The user ran multiple tasks (seeds) per GPU, but some tasks finished early, leading to underutilization of GPUs.

## Root Cause
- The user allocated GPUs at the job level, which remained allocated until the entire job ended, even if individual tasks finished early.

## Solution
- Split the simulation into separate jobs for each seed. This ensures that GPUs are freed when individual tasks are finished.
- Use job arrays to manage multiple independent tasks.

## Example Script
```bash
#!/bin/bash -l
#SBATCH --mail-user=user@example.com
#SBATCH --mail-type=BEGIN,END,FAIL,TIME_LIMIT
#SBATCH --job-name=birbm
#SBATCH --array=331,555,6242,44242
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=16
#SBATCH --gres=gpu:a100:1
#SBATCH --time=24:00:00

# Load the modules
module load python/3.9-anaconda
module load cuda/12.6.1
module load nvhpc/23.7
module load openmpi/4.1.6-nvhpc23.7-cuda

# Activate local python
conda activate jvmc

XLA_PYTHON_CLIENT_PREALLOCATE=false

srun --exclusive --cpu-bind=threads --threads-per-core=1 --output=outs/%J_%j_$1_${SLURM_ARRAY_TASK_ID}.out
--error=errs/%J_%j_$1_${SLURM_ARRAY_TASK_ID}.err python supervised_training.py $1 ${SLURM_ARRAY_TASK_ID}
```

## Additional Information
- Monitor GPU utilization using `nvidia-smi` or the ClusterCockpit monitoring system.
- Ensure efficient resource allocation to avoid idle GPUs.

## Conclusion
- Properly managing job arrays and resource allocation can help optimize GPU utilization and prevent resource wastage.
---

### 2022090642004171_keine%20GPU-Nutzung%20-%20iwia033h.md
# Ticket 2022090642004171

 ```markdown
# HPC Support Ticket: No GPU Usage - iwia033h

## Keywords
- GPU utilization
- Certificate expiration
- Job delay
- Low GPU usage

## Problem Description
- **Root Cause**: Certificate has expired.
- **Symptoms**:
  - Delay in GPU usage (2 hours before any activity).
  - Low GPU utilization (20%).

## Solution
- **Action Taken**:
  - HPC Admin identified the issue and requested the 2nd Level Support team to handle it informally.
  - A member of the 2nd Level Support team was informed and acknowledged the issue.
  - The issue was resolved by the 2nd Level Support team member who understood the problem and promised to address it.

## General Learnings
- Certificate expiration can lead to significant delays and reduced performance in GPU jobs.
- Informal communication channels can be effective for quick resolution of known issues.
- Collaboration between HPC Admins and the 2nd Level Support team is crucial for efficient problem-solving.
```
---

### 2023092942003752_Run%20crashes%20due%20to%20storage%20error.md
# Ticket 2023092942003752

 # HPC Support Ticket: Run Crashes Due to Storage Error

## Keywords
- OSError
- Errno 28
- No space left on device
- alex cluster
- TinyGPU

## Problem Description
Users are experiencing crashes in their runs with errors indicating no space left on the device. This issue has been reported on both the alex cluster and TinyGPU.

## Root Cause
The error "OSError: [Errno 28] No space left on device" suggests that the storage on the affected clusters is full, leading to job failures.

## Solution
- **HPC Admins** should investigate the storage usage on the alex cluster and TinyGPU.
- **2nd Level Support Team** can assist in identifying and cleaning up unnecessary files or expanding storage capacity if needed.
- Users should be advised to monitor their storage usage and delete unnecessary files to prevent future occurrences.

## Next Steps
- **HPC Admins** to check and report on storage status.
- **2nd Level Support Team** to provide assistance in resolving storage issues.
- **Gehard Wellein** and **Georg Hager** to be informed if the issue persists or requires additional resources.

## Documentation
This issue highlights the importance of regular storage monitoring and maintenance. Ensure that storage quotas are enforced and users are educated on best practices for storage management.
---

### 2023090142000566_Multinode%20Job%20performance.md
# Ticket 2023090142000566

 # HPC Support Ticket: Multinode Job Performance

## Keywords
- Multinode Jobs
- LLM Training
- GPU Memory Utilization
- CUDA Out of Memory
- Batch Size
- Clustercockpit Metrics
- nv_mem_util
- acc_mem_used
- acc_utilization

## Summary
The user reported performance issues with multinode jobs for training large language models (LLMs). The job appeared slow, and the `nv_mem_util` metric was low, despite encountering CUDA out of memory errors when changing the batch size.

## Root Cause
- Misinterpretation of the `nv_mem_util` metric.
- Potential inefficiency in GPU memory usage and job configuration.

## Details
- **User Concerns:**
  - Slow job performance.
  - Low `nv_mem_util` despite CUDA out of memory errors.
- **HPC Admin Response:**
  - Clarified that `nv_mem_util` represents the percentage of time the GPU memory was being read or written.
  - Suggested using `acc_mem_used (MB)` for GPU memory usage.
  - Mentioned that `acc_utilization` looked good but did not indicate meaningful utilization.
  - Offered to reproduce the scenario and scheduled a Zoom call for further investigation.

## Solution
- Use `acc_mem_used (MB)` to monitor GPU memory usage.
- Ensure proper job configuration and efficient use of GPU resources.
- Collaborate with HPC support to analyze additional logs and optimize job performance.

## Next Steps
- Schedule a Zoom call to review logs and job configuration.
- Reproduce the scenario to identify potential issues.
- Optimize job performance based on the findings.

## Additional Notes
- The user used Llama 2 70B as the pretrained language model, which requires an application for weights.
- Theoretically, up to 8 nodes can be allocated in a job.

## References
- [Download StableLM Weights](https://github.com/Lightning-AI/lit-gpt/blob/main/tutorials/download_stablelm.md)
- [Clustercockpit Monitoring](https://monitoring.nhr.fau.de/monitoring/job/4895517)
---

### 2022042542001067_Early-Alex%20%22Siyuan%20Mei%22%20_%20iwi5070h.md
# Ticket 2022042542001067

 # HPC Support Ticket Conversation Analysis

## Keywords
- Account activation
- TensorFlow
- PyTorch
- Module availability
- GPGPU cluster 'Alex'
- Nvidia A100, A40 GPGPUs
- Deep learning
- CNN training
- Image inpainting
- Loss function minimization

## Summary
- **User Request**: Access to GPGPU cluster 'Alex' for deep learning work, specifically CNN training for image inpainting. Required software: TensorFlow, PyTorch.
- **HPC Admin Response**: Account enabled on Alex. Both TensorFlow and PyTorch are available as modules.

## Root Cause of the Problem
- User needed access to specific HPC resources and software for deep learning tasks.

## Solution
- HPC Admin enabled the user's account on the Alex cluster and confirmed the availability of TensorFlow and PyTorch as modules.

## General Learnings
- Ensure users are aware of the software modules available on the HPC cluster.
- Quick account activation and software availability confirmation can resolve user access issues efficiently.
- Deep learning tasks, such as CNN training for image inpainting, require specific GPGPU resources and software modules.
---

### 2024022842000268_Job%20on%20Alex%20do%20not%20use%20GPU%20%5Biwb0003h%5D.md
# Ticket 2024022842000268

 ```markdown
# HPC Support Ticket: Job on Alex Not Using GPU

## Keywords
- GPU utilization
- Job monitoring
- Resource allocation
- ClusterCockpit
- `nvidia-smi`
- `srun`

## Summary
A job on the HPC cluster Alex was not utilizing the allocated GPUs, leading to idle resources.

## Problem
- **Root Cause**: The user's job stopped making use of the 16 allocated GPUs.
- **Symptoms**: GPU utilization graph showed no activity.

## Solution
- **Monitoring**: Users can log into the monitoring system ClusterCockpit at [monitoring.nhr.fau.de](https://monitoring.nhr.fau.de/) to view GPU utilization.
- **Attaching to Job**: Users can attach to their running job using `srun --pty --overlap --jobid YOUR-JOBID bash` and then run `nvidia-smi` to check GPU utilization.
- **Resource Allocation**: Ensure that jobs only allocate nodes with GPUs if the code can actually utilize them.

## Lessons Learned
- Regularly monitor GPU utilization to ensure efficient resource usage.
- Use monitoring tools like ClusterCockpit to track job performance.
- Only allocate GPU resources if the job can effectively use them.

## Follow-Up
- If further assistance is needed, users should contact HPC support.
```
---

### 2025011542001728_Job%20Performance%20Mujoco%202301578%20%28alex%29%20%5Bb187cb%5D.md
# Ticket 2025011542001728

 # HPC Support Ticket: Job Performance Mujoco 2301578

## Keywords
- GPU utilization
- Reinforcement Learning
- Job monitoring
- ClusterCockpit
- `nvidia-smi`
- Resource allocation

## Summary
- **Issue**: A job running on the HPC system was observed to have low GPU utilization during certain phases, with write-peaks indicating data generation and storage.
- **Root Cause**: The job involves a reinforcement learning process where data collection (CPU-intensive) and model training (GPU-intensive) phases alternate.
- **Solution**: The behavior is expected for the given workflow. The user confirmed that this is typical for their reinforcement learning process.

## Details
- **HPC Admin**: Notified the user about low GPU utilization and provided monitoring tools (ClusterCockpit, `nvidia-smi`) to track job performance.
- **User**: Confirmed that the observed behavior is expected due to the nature of the reinforcement learning process, which involves both CPU and GPU phases.
- **Action**: The user will monitor the job and report any unexpected behavior.

## Lessons Learned
- Reinforcement learning workflows may exhibit alternating CPU and GPU usage patterns.
- Users should be aware of resource utilization and ensure that allocated resources are being used efficiently.
- Monitoring tools like ClusterCockpit and `nvidia-smi` can help users and admins track job performance and resource usage.

## Recommendations
- Users should provide detailed information about their workflows to help HPC admins understand expected resource usage patterns.
- Regular monitoring of jobs can help identify and address any unexpected behavior promptly.
---

### 2020051242002985_keine%20GPU-Utilization%20-%20bccc007h.md
# Ticket 2020051242002985

 # HPC Support Ticket: No GPU Utilization - bccc007h

## Keywords
- GPU Utilization
- Job Performance
- GPU Memory Usage
- GPU Power Usage
- GPU Temperature
- Persistence Mode

## Problem Description
- Half of the user's jobs show no GPU utilization.
- Job IDs mentioned: 467696.tgadm1 (good), 467700.tgadm1 (bad).

## Diagnostic Information
- GPU details provided for two GPUs (GeForce GTX 1080).
- GPU 0: 56% utilization, 65°C, 83W power usage.
- GPU 1: 0% utilization, 51°C, 59W power usage.
- Memory usage for both GPUs is low (~550-626 MiB out of 11178 MiB).

## Root Cause
- The root cause of the problem is not explicitly stated in the conversation.
- Possible issues could be related to job configuration, GPU persistence mode, or software issues.

## Solution
- No explicit solution provided in the conversation.
- Further investigation is needed to identify the root cause and provide a solution.

## General Learnings
- Monitoring GPU utilization is crucial for job performance.
- Check GPU memory and power usage to diagnose issues.
- Ensure jobs are properly configured to utilize available GPU resources.
- Persistence mode and temperature can also impact GPU performance.

## Next Steps
- Investigate job configurations and logs for the problematic job (467700.tgadm1).
- Check for any software or driver issues that might affect GPU utilization.
- Consult with the 2nd Level Support team or HPC Admins for further assistance.
---

### 2024120642002234_Tier3-Access-Alex%20%22Lyonel%20Behringer%22%20_%20iwal139h.md
# Ticket 2024120642002234

 ```markdown
# HPC Support Ticket: Tier3-Access-Alex

## Keywords
- Tier3 Access
- GPGPU Cluster
- Nvidia A100
- CUDA
- Pytorch
- Miniconda
- Neural Network Training
- Speech Coding
- Fraunhofer IIS

## Summary
A user requested access to the GPGPU cluster 'Alex' for neural network training related to speech coding. The user specified the need for Nvidia A100 GPUs with high throughput and at least 40GB VRAM. Required software includes CUDA, Pytorch, and Miniconda.

## Details
- **Contact**: User from Fraunhofer IIS
- **Resource**: GPGPU cluster 'Alex' with Nvidia A100 GPUs
- **Software**: CUDA, Pytorch, Miniconda
- **Application**: Neural network training for speech coding
- **Expected Results**: Trained neural networks for speech coding
- **Additional Notes**: User is a Fraunhofer IIS employee and requests access to nodes owned by Fraunhofer.

## Root Cause
User requires access to specific high-performance computing resources for specialized tasks.

## Solution
HPC Admin marked the request as completed, indicating that access was granted.

## Learning Points
- Understand the process for granting access to specific HPC resources.
- Recognize the importance of specifying required software and hardware for specialized tasks.
- Ensure proper handling of requests from external collaborators, such as Fraunhofer IIS employees.
```
---

### 2023041842003595_Tier3-Access-Alex%20%22Paolo%20Sani%22%20_%20iwal111h.md
# Ticket 2023041842003595

 # HPC Support Ticket Analysis

## Keywords
- HPC Account Activation
- Certificate Expiration
- GPGPU Cluster Access
- Nvidia A100 GPUs
- Software Requirements (Pytorch, CUDA)
- Application (Training GANs for Speech Synthesis)

## Summary
- **User Request**: Access to GPGPU cluster 'Alex' with Nvidia A100 GPUs for training GANs for speech synthesis.
- **Required Software**: Pytorch, CUDA.
- **Compute Time**: 1 * 24 * 150 GPU-hours.
- **Expected Outcome**: Improved quality of synthesized speech sentences.

## Root Cause of the Problem
- Certificate expiration.

## Solution
- HPC Admin enabled the user's HPC account on Alex.

## General Learnings
- Ensure certificates are up-to-date to avoid access issues.
- HPC Admins handle account activations and access permissions.
- Users should specify required software and expected outcomes in their requests.

## Next Steps for Similar Issues
- Check certificate validity.
- Verify account status and enable access if necessary.
- Confirm software availability and compute time allocation.
---

### 2022032142003378_Early-Alex%20%22Fuxin%20Fan%22%20_%20iwi5068h.md
# Ticket 2022032142003378

 ```markdown
# HPC Support Ticket Conversation Analysis

## Keywords
- HPC Account Activation
- Certificate Expiration
- GPGPU Cluster 'Alex'
- Nvidia A100, A40 GPGPUs
- TensorFlow, PyTorch
- Vision Transformer
- Image Segmentation
- Scatter Correction

## Summary
- **User Request**: Access to GPGPU cluster 'Alex' for deep learning tasks, including metal segmentation in CT projections, inpainting, and scatter correction.
- **Software Requirements**: TensorFlow, PyTorch, Vision Transformer, Image Segmentation, Scatter Correction.
- **Expected Outcomes**: Accurate metal segmentation, improved inpainting results, precise scatter estimation and correction.

## Root Cause of the Problem
- **Account Issue**: User's HPC account had not been used and the certificate had expired.

## Solution
- **Account Activation**: HPC Admin enabled the user's account on Alex and provided documentation for further assistance.

## General Learnings
- **Account Management**: Regularly check for account usage and certificate validity.
- **User Support**: Provide clear documentation and support for new users.
- **Software Requirements**: Ensure that required software (TensorFlow, PyTorch) is available and properly configured on the cluster.

## Next Steps
- **Follow-up**: Ensure the user can access the required resources and software.
- **Documentation**: Update documentation with any new information or frequently asked questions.
```
---

### 2023101642004817_Tier3-Access-Alex%20%22Muhammad%20Shahzeb%20Khan%20Gul%22%20_%20iwal039h.md
# Ticket 2023101642004817

 ```markdown
# HPC Support Ticket Conversation Analysis

## Subject: Tier3-Access-Alex

### Keywords:
- Account activation
- Alex cluster
- Nvidia A100 GPGPUs
- GPU-hours
- Access request

### Summary:
- **User Request**: Access to the GPGPU cluster 'Alex' with Nvidia A100 GPGPUs.
- **HPC Admin Response**: Account enabled on Alex.

### Details:
- **User Information**:
  - Contact: Muhammad Shahzeb Khan Gul (iwal039h)
  - Email: muhammad.gul@iis.fraunhofer.de
- **Requested Resources**:
  - GPGPU cluster 'Alex'
  - Nvidia A100 GPGPUs (40 GB, 9.7 TFlop/s double precision)
- **Computing Time**:
  - Formula: (number of GPUs per Job) * (walltime per job) * (number of jobs)
- **Software**: Not specified
- **Application**: Not specified
- **Expected Results**: Not specified
- **Additional Notes**: Access financed by IIS

### Root Cause:
- User required access to the Alex cluster for computational resources.

### Solution:
- HPC Admin enabled the user's account on the Alex cluster.

### Learning Points:
- **Account Activation**: HPC Admins can enable user accounts on specific clusters.
- **Resource Request**: Users should specify the required resources and computing time.
- **Financial Support**: Access can be financed by external institutions.

### References:
- **Contact**: support-hpc@fau.de
- **Website**: [FAU HPC](https://hpc.fau.de)
```
---

### 42057423_Fehlermeldung%20woody-tinyblue.md
# Ticket 42057423

 # HPC Support Ticket: Fehlermeldung woody-tinyblue

## Keywords
- Fehlermeldung
- dapl_post_req resource ERR
- RDMA_Write
- DAT_INSUFFICIENT_RESOURCES
- OpenIB-cma
- Kernel-Update
- Infiniband-Connection-Manager
- I_MPI_DEVICE
- mpirun_rrze-intelmpd

## Problem Description
The user encountered job failures with the following error message on both woody and tinyblue systems:
```
dapl_post_req resource ERR: dtos pending = 432, max_dtos 432, max_cb 433
hd 46 tl 47
[8:w0908][rdma_iba_rendezwrite.c:822] error(0x80030002): OpenIB-cma: Could
not post RDMA_Write: DAT_INSUFFICIENT_RESOURCES(DAT_RESOURCE_MEMORY)
```

## Root Cause
The issue might be related to a recent Linux kernel update and the updated OFED kernel components. The error suggests insufficient resources for RDMA operations.

## Troubleshooting Steps
1. **Compiler and MPI Version**: The user was using `intelmpi/3.1.038-intel` and `intel64/11.1.072`.
2. **Job Size**: Typical jobs involved 64 MPI processes.
3. **Kernel Update**: A recent kernel update was performed to address security issues.

## Solution
1. **Change Infiniband Connection Manager**:
   - Set the environment variable `I_MPI_DEVICE` to use a different connection manager.
   - For Woody: `env I_MPI_DEVICE=rdssm:OpenIB-mthca0-1`
   - For Tinyblue: `env I_MPI_DEVICE=rdssm:OpenIB-mlx4_0-1`
   - This can be done in the job script using `setenv` for csh or `export` for bash.

2. **Use Experimental Start Mechanism**:
   - If the above step does not resolve the issue, use the experimental start mechanism:
     ```
     /apps/rrze/bin/mpirun_rrze-intelmpd -intelmpd ...
     ```

3. **Load DAPL Module**:
   - If the problem persists, load the `dapl` module before the Intel module and use the experimental start mechanism.

## Conclusion
The issue was likely caused by resource limitations after a kernel update. Changing the Infiniband connection manager and using an experimental start mechanism were suggested as potential solutions.
---

### 2023020842002153_Tier3-Access-Alex%20%22Martin%20Strauss%22%20_%20iwal017h.md
# Ticket 2023020842002153

 # HPC Support Ticket: Tier3-Access-Alex

## Keywords
- HPC Account Activation
- Alex Cluster
- Nvidia A100, A40 GPGPUs
- CUDA, Python, PyTorch, Conda
- Speech Enhancement Models
- Fraunhofer IIS

## Summary
- **User**: Researcher from Fraunhofer IIS
- **Request**: Access to Alex cluster for training large-scale DNN models for speech enhancement
- **Required Software**: CUDA, Python, PyTorch, Conda
- **Expected Outcome**: High-quality speech enhancement models

## Issue
- Certificate expiration mentioned by HPC Admin

## Actions Taken
- HPC Admin activated the user's account on the Alex cluster

## Resolution
- Account activated successfully

## General Learnings
- Ensure certificates are up-to-date for seamless account activation
- Alex cluster is suitable for large-scale deep learning tasks like speech enhancement
- Common software tools for such tasks include CUDA, Python, PyTorch, and Conda

## Follow-up
- No further action required from the user or HPC Admin regarding account activation
- User can proceed with their research on the Alex cluster
---

### 2025031942001075_Tier3-Access-Alex%20%22Changhun%22%20_%20no12neni%40fau.de.md
# Ticket 2025031942001075

 # HPC-Support Ticket Conversation Summary

## Keywords
- Tier3 Access
- NHR Project
- GPU Hours
- Alex Cluster
- JARDS Application
- Tier System

## General Learnings
- **Tier System**: Computing in Germany is organized in a tier system: Tier3 (local small resources), Tier2 (Germany-wide mid-size resources), Tier1 (Germany-wide large size), Tier0 (EU scale).
- **Resource Allocation**: Tier3 allocations are below NHR projects. Tier3 users typically get a few hundred GPU hours per year.
- **Application Process**: Tier2 applications are managed using the JARDS platform. PhD holders working for a German university can apply.

## Root Cause of the Problem
- User initially requested an unreasonably high amount of GPU hours (560,000 hours per year).
- Confusion between Tier2 and Tier3 access and application process.

## Solution
- HPC Admins clarified the tier system and resource allocation.
- User decided to apply for Tier3 access, which was granted by the HPC Admins.
- User was advised to check GPU prices in the cloud for a better understanding of reasonable resources.

## Additional Notes
- The initial request of >500,000 GPU hours would be worth >2 million Euros on the free market.
- The Alex cluster access was granted to the user's Tier3 account.
- The user's supervisor was not required to apply for the NHR project as the user decided to proceed with Tier3 access.
---

### 2024090342003709_Job%202032236%20has%20low%20GPU%20utilization%20_%20unclear%20purpose%20%5Bb207dd%5D.md
# Ticket 2024090342003709

 # HPC Support Ticket Analysis: Low GPU Utilization

## Keywords
- Low GPU utilization
- Job purpose unclear
- High-end GPUs (a100_80)
- Low VRAM usage
- Model loading
- Resource quota exceeded

## Summary
- **Issue**: Job 2032236 exhibits low GPU utilization and unclear purpose.
- **Details**: The job loads a model and then sleeps without significant computation. High-end GPUs are used despite low VRAM usage.
- **Suggestions**: Consider using a more appropriate model directory (anvme-Workspaces) for faster loading.
- **Resource Quota**: The project's resource quota has been exceeded despite a 25% increase.

## Root Cause
- The job's primary activity is loading a model and then sleeping, leading to low GPU utilization.

## Solution
- Investigate the job's purpose and optimize it to perform significant computations.
- Consider using more appropriate hardware for the job's requirements.
- Use a faster model directory to improve loading times.

## Action Taken
- The ticket was closed due to no response from the user.

## General Learning
- Ensure jobs are optimized for the hardware they are running on.
- Monitor GPU utilization and VRAM usage to allocate resources efficiently.
- Address resource quota issues promptly to avoid exceeding limits.

---

This documentation aims to help support employees identify and resolve similar issues related to low GPU utilization and resource quota management.
---

### 2022060842001309_Jobs%20auf%20TinyGPU%20nutzen%20die%20GPU%20nicht%20%5Biwso012h%5D.md
# Ticket 2022060842001309

 # HPC Support Ticket: Jobs auf TinyGPU nutzen die GPU nicht

## Keywords
- GPU utilization
- TinyGPU
- JobID 263773, 263845
- nvidia-smi
- Monitoringsystem
- GPU-Knoten

## Problem Description
- Jobs on TinyGPU (JobID 263773 and 263845) are not utilizing the requested GPUs.
- Monitoring system screenshot shows no GPU usage for the jobs.

## Root Cause
- The user's code does not utilize the GPUs, leading to idle GPU resources.

## Solution
- Users should ensure their code can utilize GPUs before requesting GPU nodes.
- Users can check GPU utilization using `nvidia-smi` after logging into the node via `ssh`.
- Refer to the documentation for working with NVIDIA GPUs: [Working with NVIDIA GPUs](https://hpc.fau.de/systems-services/systems-documentation-instructions/special-applications-and-tips-tricks/working-with-nvidia-gpus/)

## General Learnings
- Always verify that your code can utilize GPUs before requesting GPU nodes.
- Use `nvidia-smi` to monitor GPU usage.
- Idle GPU resources can be avoided by proper code optimization and resource allocation.

## Contact Information
- For further assistance, contact the HPC support team at [support-hpc@fau.de](mailto:support-hpc@fau.de).
- Visit the HPC website for more information: [HPC FAU](https://hpc.fau.de/)
---

### 2024061642000854_Slurm%20job%20wont%20start%2C%20but%20runs%20in%20interactive%20session.md
# Ticket 2024061642000854

 ```markdown
# HPC-Support Ticket: Slurm Job Not Starting

## Subject
Slurm job won't start, but runs in interactive session

## User Issue
- Slurm job script submitted but training does not start and GPU allocates almost 0 memory.
- Same script runs successfully in an interactive session.

## Slurm Job Script
```bash
#!/bin/bash -l
#SBATCH --ntasks-per-node=8
#SBATCH --partition=a100
#SBATCH --job-name=bbed_causal2
#SBATCH --output=jobs/%x-%j.out
#SBATCH --error=jobs/%x-%j.err
#SBATCH --time=23:59:00
#SBATCH --export=NONE
#SBATCH --gres=gpu:a100:1
unset SLURM_EXPORT_ENV
module load python cuda/11.5 gcc/10 ninja
export HTTP_PROXY=http://proxy:80
export HTTPS_PROXY=http://proxy:80
python3 $HOME/sgmse/train.py --base_dir $HPCVAULT/data/VBD_48khz/ --batch_size 16 --backbone ncsnpp_time_convs_strided_stacked --frequency_stacking 1 --sde bbed  --k 2.6 --theta 0.51 --normalize not --causal --strides 2 2 2 2 2 2 2 --t_eps 0.03 --gpus 1 --num_eval_files 10 --format default --channels 128 256 256 256 256 256 256 --spec_abs_exponent  0.5 --spec_factor 0.15 --loss_abs_exponent 1 --fs 16000 --wandb_name bbed_v1 --num_frames 256 --loss_type mse --N_inf 15 --T_sampling 0.9  --hop_length 128 --n_fft 510 --speclogs_every_epoch 0 --audiologs_every_epoch 75 --gains 0 0 --ckpt_destination /home/vault/f101ac/f101ac10/sgmse --wandb_project_name realtime_vbd
```

## Interactive Session Commands
```bash
salloc --gres=gpu:a40:1 --time=01:00:00
srun --jobid=<jobid> --overlap --pty /bin/bash -l
module add python
module add cuda/11.5
module add gcc/10
module add ninja
export HTTP_PROXY=http://proxy:80
export HTTPS_PROXY=http://proxy:80
python3 $HOME/sgmse/train.py --base_dir $HPCVAULT/data/VBD_48khz/ --batch_size 16 --backbone ncsnpp_time_convs_strided_stacked --frequency_stacking 1 --sde bbed  --k 2.6 --theta 0.51 --normalize not --causal --strides 2 2 2 2 2 2 2 --t_eps 0.03 --gpus 1 --num_eval_files 10 --format default --channels 128 256 256 256 256 256 256 --spec_abs_exponent  0.5 --spec_factor 0.15 --loss_abs_exponent 1 --fs 16000 --wandb_name bbed_v1 --num_frames 256 --loss_type mse --N_inf 15 --T_sampling 0.9  --hop_length 128 --n_fft 510 --speclogs_every_epoch 0 --audiologs_every_epoch 75 --gains 0 0 --ckpt_destination /home/vault/f101ac/f101ac10/sgmse --wandb_project_name realtime_vbd
```

## HPC Admin Response
- Observations from interactive vs batch job or from different GPU types (a40 vs a100).
- Job output contains warnings:
  - CUDA extension for cauchy multiplication not found.
  - Setting `Trainer(gpus=1)` is deprecated in v1.7.
  - Tensor Cores usage recommendation for NVIDIA A100-SXM4-40GB.

## Keywords
- Slurm job
- Interactive session
- GPU allocation
- CUDA extension
- Tensor Cores
- PyTorch Lightning

## What to Learn
- Differences between interactive and batch job environments.
- Importance of checking job output for warnings and errors.
- Proper usage of GPU resources and CUDA extensions.
- Updating deprecated code to ensure compatibility with newer versions.

## Solution
- Address the warnings in the job output.
- Ensure the CUDA extension for cauchy multiplication is installed.
- Update the PyTorch Lightning code to use `Trainer(accelerator='gpu', devices=1)`.
- Set `torch.set_float32_matmul_precision('medium' | 'high')` for better performance with Tensor Cores.
```
---

### 2022012642003167_Requesting%20Help%20to%20access%20Test%20cluster%20testfront1.md
# Ticket 2022012642003167

 # HPC Support Ticket: Access to Test Cluster testfront1

## Keywords
- TinyGPU
- Draining state
- Reboot
- Test cluster (testfront1)
- Job scheduling
- Maintenance notification

## Summary
User encountered nodes in draining state on TinyGPU cluster due to an immediate maintenance reboot, affecting their project presentation preparation. User requested access to testfront1 cluster as an alternative.

## Root Cause
- **Immediate maintenance reboot** required on TinyGPU cluster.
- **Lack of notification** to users about the maintenance.

## User Request
- Timeline for TinyGPU nodes availability.
- Permission and instructions to use testfront1 cluster for a small job (less than 4 hours).
- Request for advance warning for future maintenance.

## HPC Admin Response
- Maintenance was necessary for operational reasons.
- Some TinyGPU nodes became available the previous evening, with remaining nodes to follow shortly.
- No guarantee for jobs to start quickly; waiting times of 1-2 weeks are not unusual.
- No explicit permission or instructions given for using testfront1.

## Lessons Learned
- **Communication**: Importance of notifying users about maintenance well in advance.
- **Job Scheduling**: Users should be aware of potential waiting times for jobs on HPC systems.
- **Alternative Resources**: Clarification on policies for using test clusters like testfront1 during maintenance periods.

## Follow-up Actions
- Improve communication strategy for maintenance notifications.
- Clarify and document policies for using test clusters during downtimes.
- Ensure users are informed about job scheduling and waiting times.
---

### 2021110942000971_L%C3%83%C2%BCcken%20in%20der%20GPU-Auslastung%20-%20bccb006h.md
# Ticket 2021110942000971

 # HPC Support Ticket: Gaps in GPU Utilization

## Keywords
- GPU utilization gaps
- Umbrella-Sampling Simulation
- Python script
- GROMACS
- `nvidia-smi`
- Monitoring

## Summary
A user's GPU jobs were experiencing multi-hour gaps in GPU utilization. The user was running Umbrella-Sampling Simulations using a Python script that distributes and starts multiple simulations on available GPUs.

## Root Cause
The root cause of the gaps in GPU utilization was not explicitly determined in the conversation. However, it was suspected that intermediate steps in the Python script or GROMACS functions might be causing issues.

## Solution
- **User Action**: The user was advised to investigate the Python script and GROMACS functions for potential issues.
- **Monitoring**: The user inquired about accessing the historical GPU utilization data but was informed that such data is not currently accessible to users. The only available method for monitoring GPU utilization is to SSH into the node running the job and use the `nvidia-smi` command, which provides real-time information but no historical data.

## Lessons Learned
- **Monitoring Limitations**: Users do not have access to historical GPU utilization data and can only monitor real-time usage via `nvidia-smi`.
- **Script and Function Review**: Intermediate steps in scripts or functions (e.g., Python, GROMACS) can cause gaps in GPU utilization and should be reviewed for optimization.

## Next Steps
- **User**: Investigate the Python script and GROMACS functions to identify and resolve any issues causing the gaps in GPU utilization.
- **HPC Admins**: Consider providing users with access to historical GPU utilization data for better troubleshooting and optimization.

## References
- `nvidia-smi` command for real-time GPU monitoring.
- Internal monitoring tools used by HPC Admins for GPU utilization tracking.
---

### 2022011442001691_Jobs%20on%20TypyGPU%20-%20iwi5033h.md
# Ticket 2022011442001691

 # HPC Support Ticket Analysis: Jobs on TypyGPU

## Keywords
- GPU allocation
- Job configuration
- Python framework
- Supervisor assistance
- Resource optimization

## Problem
- User's job on TypyGPU requested two GPUs but utilized only one.

## Root Cause
- Incorrect job configuration (ppn=8) leading to inefficient GPU usage.

## Solution
- Adjust job configuration to ppn=4 for one GPU or ensure both GPUs are utilized.
- Seek assistance from the supervisor for Python framework issues.

## General Learnings
- Ensure proper resource allocation in job configurations to avoid wastage.
- Consult supervisors or support teams for framework-specific issues.
- Optimize job settings to match actual resource requirements.

## Actions Taken
- HPC Admin notified the user about the misconfiguration and provided guidance on correcting it.
- Suggested seeking help from the supervisor for Python framework-related issues.

## Follow-Up
- Monitor future job submissions to ensure proper resource allocation.
- Provide additional training or documentation on job configuration best practices.
---

### 2024082642002017_Tier3-Access-Alex%20%22Lorenz%20Schmidt%22%20_%20iwal046h.md
# Ticket 2024082642002017

 # HPC Support Ticket Analysis

## Keywords
- Tier3 Access
- Alex
- GPGPU Cluster
- Nvidia A100
- GPU-hours
- Python
- PyTorch
- Deep Neural Networks
- Audio Domain
- Pre-training Models
- Fine-tuning Models
- Hyperparameter Searches
- A100 GPUs
- Training Time
- Meta-learning
- Filterbanks

## Summary
- **User Request**: Access to the GPGPU cluster 'Alex' with Nvidia A100 GPUs for deep neural network tasks in the audio domain.
- **Resources Requested**: 2880 GPU-hours.
- **Software Requirements**: Python, PyTorch.
- **Application**: Pre-training and fine-tuning models, hyperparameter searches, meta-learning, and learning specific filterbanks.
- **Expected Outcomes**: Accelerate training on various audio datasets for tasks like acoustic scene classification, event classification, and automatic speech recognition.

## Lessons Learned
- **Access Granting**: HPC Admin granted access to the user for the specified resources.
- **Resource Allocation**: Understanding the specific needs of the user in terms of GPU-hours and software requirements.
- **Application Details**: Importance of detailed application descriptions for resource allocation and support.

## Root Cause of the Problem
- User needed access to specific HPC resources for their research project.

## Solution
- HPC Admin granted the user access to the requested resources.

## Notes for Support Employees
- Ensure users provide detailed descriptions of their resource needs and applications.
- Verify and grant access promptly to facilitate research projects.
- Understand the specific software and hardware requirements for different types of research tasks.
---

### 2024090442000399_Use%20of%20A100_80%20GPUs%20expected%20for%20large%20memory%20runs%20-%20b110dc11.md
# Ticket 2024090442000399

 # HPC Support Ticket: Use of A100_80 GPUs for Large Memory Runs

## Keywords
- GPU memory usage
- A100 GPUs
- Job script optimization
- #SBATCH -C a100_80

## Summary
The HPC Admin informed the user that their jobs on the Alex cluster required less than 20GB of GPU memory, making them suitable to run on A100 GPUs with 40GB memory. The user was advised to remove the `#SBATCH -C a100_80` directive from their job scripts.

## Root Cause
- The user's job scripts were requesting A100 GPUs with 80GB memory (`#SBATCH -C a100_80`), which was unnecessary for their jobs requiring less than 20GB of GPU memory.

## Solution
- Remove the `#SBATCH -C a100_80` directive from the job scripts.
- Run the jobs on A100 GPUs with 40GB memory.

## General Learning
- Monitor GPU memory usage to optimize resource allocation.
- Adjust job scripts to request appropriate GPU configurations based on actual memory requirements.
- Communicate with users to ensure efficient use of HPC resources.
---

### 2025022142002062_GPU%20availability.md
# Ticket 2025022142002062

 # GPU Availability Issue

## Keywords
- GPU allocation
- Waiting time
- Usage limits
- Conference deadlines

## Problem Description
- User experiencing unusually long waiting times for GPU allocation.
- Concern about hitting GPU usage limits.

## Root Cause
- Increased demand due to major conference deadlines.

## Solution/Explanation
- The long waiting times are considered normal during periods of high demand, such as major conference deadlines.
- No specific usage limits were hit by the user.

## General Learning
- High demand periods (e.g., conference deadlines) can lead to longer waiting times for GPU allocation.
- Users should be aware of and plan for potential delays during such periods.

## Next Steps
- Monitor GPU usage and demand.
- Communicate high demand periods to users proactively if possible.
---

### 2021112542003008_Jobs%20auf%20TinyGPU%20nutzen%20keine%20GPU%20-%20iwso043h.md
# Ticket 2021112542003008

 # HPC Support Ticket: Jobs auf TinyGPU nutzen keine GPU

## Keywords
- GPU utilization
- SciKitLearn
- Job parameters
- TinyGPU cluster
- Performance issues

## Problem Description
The user's jobs on the TinyGPU cluster were not utilizing the GPUs, despite requesting them with the `--gres=gpu:1` parameter. The user was using SciKitLearn, which does not support GPU acceleration.

## Root Cause
- The software (SciKitLearn) used by the user does not support GPU acceleration.
- The user's jobs were requesting GPU resources but not utilizing them, leading to inefficient resource usage.

## Solution
- The HPC Admin informed the user that SciKitLearn does not support GPUs and advised them to clarify the possibilities with their supervisor.
- The user agreed to stop requesting GPUs for their jobs after completing their master's thesis.
- The HPC Admin did not suspend the user's account but advised them to minimize the number of jobs to avoid blocking GPU nodes unnecessarily.

## General Learnings
- Always ensure that the software you are using supports GPU acceleration before requesting GPU resources.
- Communicate with your supervisor or HPC support to clarify the best cluster and resource allocation for your specific use case.
- Be mindful of resource usage to avoid blocking resources unnecessarily, especially on highly utilized clusters.
---

### 2024041242002103_NHR%20Alex%20Job%20Submission%20Inconsistent%20GPU%20Count.md
# Ticket 2024041242002103

 # HPC-Support Ticket: NHR Alex Job Submission Inconsistent GPU Count

## Subject
Inconsistent GPU allocation when submitting jobs on Alex.

## User Report
- **Issue**: Inconsistent GPU allocation when submitting jobs with 8 GPUs on Alex.
- **Observation**:
  - `salloc --gres gpu:8 --partition a40` or `salloc --gres gpu:8 --partition a100` allocates only a single GPU.
  - `salloc --gres gpu:a40:8`, `salloc --gres gpu:a100:8`, and `salloc --gres gpu:8 --partition a40,a100` work as expected.

## Keywords
- GPU allocation
- `salloc`
- `--gres`
- `--partition`
- NVIDIA A40
- NVIDIA A100

## Root Cause
The issue arises from the way the `--gres` option is used in combination with the `--partition` option. Specifying `--gres gpu:8` without specifying the GPU type in the partition leads to incorrect allocation.

## Solution
To ensure correct GPU allocation, use one of the following commands:
- `salloc --gres gpu:a40:8`
- `salloc --gres gpu:a100:8`
- `salloc --gres gpu:8 --partition a40,a100`

## General Learning
- Always specify the GPU type when using the `--gres` option to avoid inconsistent allocations.
- Combining `--gres gpu:8` with multiple partitions (`--partition a40,a100`) can work as expected.

## Support Team Involved
- **HPC Admins**: Thomas, Michael Meier, Anna Kahler, Katrin Nusser, Johannes Veh
- **2nd Level Support**: Lacey, Dane (fo36fizy), Kuckuk, Sebastian (sisekuck), Lange, Florian (ow86apyf), Ernst, Dominik (te42kyfo), Mayr, Martin
- **Datacenter Head**: Gerhard Wellein
- **Training and Support Group Leader**: Georg Hager
- **NHR Rechenzeit Support**: Harald Lanig
- **Software and Tools Developer**: Jan Eitzinger, Gruber

## Documentation Note
This issue highlights the importance of correctly specifying GPU types when using the `--gres` option in job submissions. Incorrect specifications can lead to unexpected behavior in GPU allocations.
---

### 2022011442000692_Jobs%20auf%20TinyGPU%20nutzen%20keine%20GPU%20-%20iwi1006h.md
# Ticket 2022011442000692

 # HPC Support Ticket: Jobs auf TinyGPU nutzen keine GPU

## Keywords
- GPU utilization
- Job script
- SSH
- nvidia-smi
- TinyGPU

## Summary
The user's jobs running on TinyGPU were not utilizing the GPUs, leading to unusually long job durations.

## Problem
- Jobs on TinyGPU did not use GPUs.
- The job script did not provide clear indications of the issue.

## Diagnostic Steps
- HPC Admin advised the user to log in via SSH to their node and use `nvidia-smi` to check GPU utilization.
- The user was informed that if multiple jobs were running on the same node, the SSH session would attach to one of the jobs, showing only that job's GPU usage.

## Follow-Up
- After nearly a month, the jobs still did not utilize GPUs.
- HPC Admin noted that the current jobs appeared okay, but no feedback was received from the user.

## Root Cause
- The root cause of the problem was not explicitly identified in the conversation.

## Solution
- The user was advised to abort the jobs and investigate the issue further.
- No specific solution was provided, but the user was encouraged to seek additional HPC support if needed.

## General Learnings
- Always check GPU utilization using tools like `nvidia-smi` when jobs are running longer than expected.
- Ensure job scripts are correctly configured to utilize GPU resources.
- Regularly monitor job performance and seek support if issues persist.

## Next Steps
- If similar issues arise, advise users to check their job scripts and GPU utilization.
- Encourage users to provide feedback and seek further assistance if needed.
---

### 2022060842000953_Job%20auf%20TinyGPU%20nutzen%20nach%20Anfangsphase%20die%20GPU%20nicht%20mehr%20%5Biwi9016h%5D.md
# Ticket 2022060842000953

 ```markdown
# HPC Support Ticket: Job on TinyGPU Not Utilizing GPU After Initial Phase

## Keywords
- GPU utilization
- TinyGPU
- JobID 263726
- nvidia-smi
- Monitoring system
- GPU resources

## Problem Description
The user's job on TinyGPU (JobID 263726) stops utilizing the requested GPU after an initial phase.

## Root Cause
The exact root cause is not specified in the conversation, but it is implied that the job might not be properly configured to utilize the GPU throughout its execution.

## Solution
- **Monitoring GPU Usage:** The user is advised to log in to the associated node via SSH and use `nvidia-smi` to monitor the current GPU utilization.
- **Documentation Reference:** The user is referred to the documentation on working with NVIDIA GPUs: [Working with NVIDIA GPUs](https://hpc.fau.de/systems-services/systems-documentation-instructions/special-applications-and-tips-tricks/working-with-nvidia-gpus/).
- **Resource Allocation:** The user is reminded to only request GPU nodes if their code can effectively utilize the GPUs, to avoid wasting resources.

## General Learnings
- Always ensure that jobs are properly configured to utilize GPU resources throughout their execution.
- Use monitoring tools like `nvidia-smi` to check GPU utilization.
- Refer to the documentation for best practices and troubleshooting tips.
- Be mindful of resource allocation to avoid wasting GPU resources.

## Ticket Status
The ticket was closed by the HPC Admin.
```
---

### 2023041242001901_Tier3-Access-Alex%20%22Amritanshu%20Verma%22%20_%20iwia050h.md
# Ticket 2023041242001901

 # HPC Support Ticket Analysis: Tier3-Access-Alex

## Keywords
- **Access Request**
- **GPU Cluster**
- **Alex**
- **Nvidia A100**
- **Nvidia A40**
- **CUDA**
- **Nsight**
- **cupy**
- **numpy**
- **Anaconda**
- **Pytorch**
- **TensorFlow**
- **Transformer Model**
- **Performance Engineering**
- **Energy Consumption**
- **Roofline Modeling**

## Summary
- **User Request**: Access to GPU cluster 'Alex' for performance engineering of Transformer models on A100 and A40 GPUs.
- **Required Software**: Nvidia CUDA, Nsight, cupy, numpy, Anaconda, Pytorch, TensorFlow.
- **Expected Outcomes**: Performance metrics, energy consumption, roofline modeling.

## Root Cause of the Problem
- User required access to specific GPU resources and software for research purposes.

## Solution
- **HPC Admin Action**: User account was granted access to Alex using `add-early-user.sh` script.
- **Notification**: User was informed via email that their account is now allowed to use Alex.

## General Learnings
- **Access Granting**: Use of `add-early-user.sh` script for granting access to specific resources.
- **Software Requirements**: Common software tools required for GPU-based machine learning and performance engineering.
- **Research Applications**: Understanding the need for performance and energy consumption analysis in AI model training.

## Follow-up Actions
- Ensure user has access to all required software tools.
- Monitor resource usage and provide support for any issues related to GPU performance or software compatibility.

---

This documentation can be used as a reference for handling similar access requests and understanding the typical software and resource requirements for AI and machine learning projects on HPC systems.
---

### 2024020942002337_Alex%20Cluster%3A%20Anforderung%20A100%20GPU%20mit%2040%20GB%20bzw.%2080%20GB%20VRAM.md
# Ticket 2024020942002337

 # HPC Support Ticket: Specifying A100 GPU VRAM on Alex Cluster

## Keywords
- Alex GPU Cluster
- A100 GPU
- 40 GB VRAM
- 80 GB VRAM
- Job Specification

## Problem
The user wants to specify whether to use an A100 GPU with 40 GB or 80 GB VRAM for their job on the Alex GPU Cluster.

## Solution
To specify the type of A100 GPU, the user can use the `-C` option followed by `a100_40` for 40 GB VRAM or `a100_80` for 80 GB VRAM.

```bash
# For 40 GB VRAM
-C a100_40

# For 80 GB VRAM
-C a100_80
```

## General Learning
- The Alex GPU Cluster supports A100 GPUs with different VRAM sizes.
- Users can specify the required GPU type using the `-C` option followed by the appropriate GPU type identifier.
- This ticket provides a quick reference for specifying GPU types on the Alex Cluster.
---

### 2025011042002656_Alex%20Cluster%20Down%3F.md
# Ticket 2025011042002656

 # HPC Support Ticket: Alex Cluster Down?

## Keywords
- Alex cluster
- GPU (A40, A100)
- Job scheduling
- Node reboot
- `scontrol show Node`
- `ReqNodeNotAvail` status

## Problem
- User unable to start jobs requiring A40 or A100 GPU on Alex cluster.
- Nodes showing "Reason=Reboot ASAP" status.
- Submitted batch job in `ReqNodeNotAvail` status.

## Root Cause
- All nodes in the Alex cluster were scheduled to reboot, making GPUs temporarily unavailable.

## Solution
- Wait for the nodes to complete their reboot and return to service.
- Keep jobs submitted and check status later.

## General Learnings
- Nodes may be scheduled for reboot, affecting job availability.
- `scontrol show Node` command can reveal node status and reasons for unavailability.
- Jobs may enter `ReqNodeNotAvail` status when required nodes are not available.
- Regularly check for scheduled downtimes or maintenance announcements.
---

### 2020112342001391_HPC%20Nutzung%20f%C3%83%C2%BCr%20Studenten%20des%20MLTS%20Seminars.md
# Ticket 2020112342001391

 # HPC Support Ticket: HPC Nutzung für Studenten des MLTS Seminars

## Keywords
- HPC Zugang
- Studenten
- Maschinelles Lernen
- Neuronale Netze
- GPU Zeit
- IDM-Kennungen
- Gruppenaccounts

## Summary
- **Request**: HPC access for students in a machine learning seminar to train neural networks.
- **Details**: 6 groups of students, each with ~2-5GB data, requiring less than 48 hours of GPU time.
- **Concerns**: Potential GPU cluster congestion and data storage limits.

## Conversation Highlights
- **Initial Request**: User inquires about HPC access for students to train neural networks.
- **HPC Admin Response**:
  - Possible to request HPC accounts for educational purposes.
  - Concerns about GPU cluster availability and data storage limits.
- **User Clarification**: Provides details on student groups, data sizes, and estimated GPU time.
- **HPC Admin Actions**:
  - Requests creation of 12 HPC-Bulk-Accounts.
  - Account creation delayed due to certificate expiration.
  - Final resolution: Individual accounts created for students, accessible via IdM-Portal.

## Root Cause of the Problem
- Need for HPC access for students to train neural networks.
- Concerns about GPU cluster availability and data storage limits.

## Solution
- **Account Creation**: Individual HPC accounts created for students.
- **Access Instructions**: Students can set passwords via IdM-Portal and access HPC systems.

## General Learnings
- **HPC Access for Students**: Possible for educational purposes with proper justification.
- **GPU Cluster Usage**: Potential congestion if many students use it simultaneously.
- **Data Storage Limits**: Default quotas may not accommodate large datasets.
- **Account Management**: Individual accounts preferred over group accounts.

## Notes for Support Employees
- Ensure students are informed about potential GPU cluster congestion.
- Monitor data storage usage to avoid exceeding default quotas.
- Provide clear instructions for accessing and managing HPC accounts via IdM-Portal.
---

### 2018083142001127_Re%3A%20%5BRRZE-HPC%5D%20Call%20for%20proposals%20on%20NVidia%20Tesla%20V100%20usage.md
# Ticket 2018083142001127

 # HPC Support Ticket Conversation Summary

## Subject: Re: [RRZE-HPC] Call for proposals on NVidia Tesla V100 usage

### Keywords:
- NVidia Tesla V100
- Gromacs
- PBS Pro
- Module Load
- GPU Performance
- Benchmarking
- Hardware Limitations

### General Learnings:
- Users need to submit proposals for accessing new hardware.
- Detailed instructions for accessing and using new hardware are provided by HPC Admins.
- Benchmarking and performance testing are crucial for evaluating new hardware.
- Hardware limitations, such as CPU performance, can affect GPU utilization.
- Communication between users and HPC Admins is essential for troubleshooting and optimizing performance.

### Root Causes and Solutions:
1. **Module Load Issue**:
   - **Root Cause**: Incorrect module name provided for Gromacs.
   - **Solution**: Correct module name (`gromacs/2018.1-mkl-CUDA91`) was provided by HPC Admin.

2. **Job Submission Syntax**:
   - **Root Cause**: Incorrect syntax for job submission.
   - **Solution**: Correct syntax provided by HPC Admin (`qsub -lnodes=1:ppn=40 -q v100 ...`).

3. **Module File Error**:
   - **Root Cause**: Error in the module file.
   - **Solution**: HPC Admin fixed the error in the module file.

4. **GPU Performance**:
   - **Root Cause**: CPUs not keeping GPUs busy, leading to suboptimal performance.
   - **Solution**: Benchmarking and comparison with other systems to identify hardware limitations. No immediate solution due to hardware constraints.

5. **Alternative Hardware**:
   - **Root Cause**: Limited hardware options for further testing.
   - **Solution**: User mentioned an upcoming system with Titan-V GPUs for future performance comparisons.

### Notes:
- Users should provide detailed proposals for new hardware usage.
- HPC Admins provide step-by-step instructions for accessing and using new hardware.
- Benchmarking and performance testing are essential for evaluating new hardware.
- Hardware limitations, such as CPU performance, can affect GPU utilization.
- Communication between users and HPC Admins is crucial for troubleshooting and optimizing performance.

### Conclusion:
This conversation highlights the importance of detailed communication between users and HPC Admins for accessing and optimizing new hardware. Benchmarking and performance testing are crucial for evaluating hardware limitations and identifying areas for improvement.
---

### 2020092842004562_Beschaffung%20TinyGPU%20Knoten.md
# Ticket 2020092842004562

 # HPC-Support Ticket: Beschaffung TinyGPU Knoten

## Keywords
- GPU Cluster
- Machine Learning
- CUDA
- Hardware Beschaffung
- Prioritärer Zugriff
- Geforce 2080Ti
- Geforce 3080
- A100 SXM4/Nvlink
- Lieferzeit
- Rechnung

## Problem
- User möchte einen aktuellen Knoten für das TinyGPU Cluster beschaffen.
- Anwendung: Machine Learning mit CUDA.
- Fragen:
  - Kosten für 4x2080Ti.
  - Wer beschafft die Hardware?
  - Rechnung innerhalb von 4 Wochen.

## Root Cause
- Verfügbarkeit von Server-tauglichen Geforce 2080Ti ist eingeschränkt.
- Nvidia hat die Produktion der 2080Ti eingestellt.
- Lieferzeiten für neue GPUs (z.B. Geforce 3080) sind ungewiss.

## Solution
- Prioritärer Zugriff ist möglich.
- Kosten für 4x2080Ti: ca. 12.000 EUR (inkl. 19% MWSt).
- Kosten für 8x Geforce 3080: ca. 17.000 EUR (inkl. 16% MWSt).
- Kosten für 4x A100 SXM4/Nvlink: unter 45.000 EUR (inkl. 16% MWSt).
- Lieferzeit für neue GPUs beträgt viele Wochen.
- Eine Warenlieferung und Händlerrechnung innerhalb von 4 Wochen ist aktuell nicht realistisch.
- Mögliche Alternative: RRZE-Rechnung über "Beteiligung an der Beschaffung von GPU-Rechenknoten".

## Generelles
- HPC Admins bieten Unterstützung bei der Beschaffung und beraten über Alternativen.
- Kommunikation über Telefon/Zoom/MS-Teams wird angeboten.

## Next Steps
- User sollte über die Alternativen nachdenken und sich mit den HPC Admins in Verbindung setzen, um weitere Schritte zu besprechen.
---

### 2024072542005367_Student%20assistant.md
# Ticket 2024072542005367

 # HPC-Support Ticket Conversation: Student Assistant Inquiry

## Keywords
- Student Assistant
- HPC
- Computational and Applied Mathematics
- Programming Techniques for Supercomputers
- C++
- GPU Programming
- CUDA
- NVIDIA Certification
- Numerical Simulation
- Sparse Matrix Solvers

## Summary
A student inquired about a student assistant position in HPC, detailing their relevant coursework and certifications. The HPC Admin responded that there are currently no vacancies.

## User Inquiry
- **Role:** Student pursuing a master's degree in Computational and Applied Mathematics.
- **Interest:** Gain practical experience in HPC.
- **Relevant Coursework:**
  - Programming Techniques for Supercomputers
  - Programming in C++
  - Advanced C++
  - High-End Simulation in Practice (HESP) focusing on GPU programming with CUDA
- **Certifications:** NVIDIA certification for "Fundamentals of Accelerated Computing in C/C++".
- **Interests:** Numerical simulation of physical phenomena, performance optimization of sparse matrix solvers.

## HPC Admin Response
- **Status:** No current vacancies for student assistants.
- **Contact Information:** Provided contact details for future reference.

## What Can Be Learned
- **Student Interest:** There is a demand from students for practical experience in HPC.
- **Relevant Skills:** Students are acquiring skills in programming, GPU programming, and numerical simulations.
- **Certifications:** NVIDIA certifications are valuable for students interested in HPC.
- **Current Status:** No immediate opportunities for student assistants.

## Root Cause of the Problem
- **User:** Seeking practical experience in HPC.
- **Admin:** No current vacancies available.

## Solution
- **Admin:** Inform the student about the lack of current vacancies and provide contact information for future opportunities.

## Future Reference
- **For Students:** Continue to monitor for job openings and consider other avenues for gaining practical experience.
- **For HPC Admins:** Keep track of student inquiries for potential future hiring needs.
---

### 2023020142003021_Zugang%20Alex%20PAMPI%20account%20pavl103h.md
# Ticket 2023020142003021

 # HPC Support Ticket Analysis

## Subject
Zugang Alex PAMPI account

## Keywords
- Account access
- Alex
- MPI
- CUDA
- Certificate expiration

## Problem
- User requested access to Alex for an account to test MPI+CUDA.

## Root Cause
- Certificate for the account had expired.

## Solution
- HPC Admin resolved the issue by renewing the certificate and granting access to Alex.

## General Learnings
- Ensure certificates are up-to-date for account access.
- HPC Admins handle access requests and certificate renewals.

## Actions Taken
- HPC Admin renewed the certificate and granted access to Alex.

## Follow-up
- No further action required from the user.

## Notes
- The user intended to use MPI+CUDA in the project phase.
- Quick resolution by HPC Admin indicates efficient handling of access requests.
---

### 2024100842002351_Tier3-Access-Alex%20%22Pietro%20Foti%22%20_%20iwal190h.md
# Ticket 2024100842002351

 ```markdown
# HPC Support Ticket: Tier3-Access-Alex

## Summary
- **User**: Requested access to GPGPU cluster 'Alex' for training DNNs for audio coding.
- **HPC Admin**: Granted access and configured Slurm account.

## Keywords
- GPGPU cluster
- Alex
- Nvidia A100
- Nvidia A40
- Miniconda
- Pytorch
- DNNs
- Audio coding
- Slurm
- Fraunhofer

## Problem
- User requested access to specific nodes owned by Fraunhofer for training deep neural networks (DNNs) for audio coding.

## Solution
- HPC Admin granted access to the user.
- Configured Slurm account for the user to access the nodes owned by Fraunhofer.
- Command used: `/root/bin/set-default-account.sh iwal190h iwal_fhg -1 -1 -1`

## What Can Be Learned
- Proper configuration of Slurm accounts is essential for granting access to specific resources.
- Understanding user requirements and affiliations helps in assigning appropriate resources.
- Ensure that users have the necessary software (Miniconda, Pytorch) for their applications.
```
---

### 2023083142000725_Job%20on%20TinyGPU%20only%20use%201%20of%204%20allocated%20GPUs%20%5Biwi5095h%5D.md
# Ticket 2023083142000725

 # HPC Support Ticket: Job on TinyGPU Only Uses 1 of 4 Allocated GPUs

## Keywords
- GPU utilization
- Job allocation
- Resource management
- `nvidia-smi`
- `srun`

## Problem Description
- User's job on TinyGPU (JobID 642273 and 644139) only uses 1 of the 4 allocated GPUs.
- Resources are underutilized, leading to idle GPUs that could be used by other jobs.

## Root Cause
- The user's code is not configured to utilize multiple GPUs effectively.

## Solution
- **Check GPU Utilization:**
  - Attach to the running job using `srun --pty --overlap --jobid YOUR-JOBID bash`.
  - Run `nvidia-smi` to monitor GPU utilization.
- **Optimize Code:**
  - Ensure the code is capable of using all allocated GPUs.
  - If the code cannot utilize multiple GPUs, allocate only the required number of GPUs.

## General Learning
- Always verify that the code can utilize the allocated resources efficiently.
- Regularly monitor resource utilization to avoid wastage.
- Use appropriate commands (`srun`, `nvidia-smi`) to diagnose and manage resource usage.

## Contact
- For further assistance, contact HPC support at `support-hpc@fau.de`.
---

### 2023062042001874_Computing%20resource.md
# Ticket 2023062042001874

 # HPC Support Ticket Conversation Summary

## Keywords
- HPC cluster
- FAU
- TinyGPU
- Application process
- Thesis work
- PARSynthezier model
- SDV library
- Computational resources
- GPU
- RRZE customer ID
- Job size
- Computation time
- Storage space

## Problem
- User's local machine lacks computational resources for training a PARSynthezier model on a large dataset (44k samples), leading to kernel deaths.
- User seeks information about FAU's HPC cluster to facilitate thesis work.

## Solution/Information Provided
- **HPC Cluster Availability**: Confirmed that HPC clusters can be used for thesis work.
- **Application Process**: User should consult thesis supervisor or RRZE contact person for application assistance.
- **Relevant Cluster**: TinyGPU cluster recommended for GPU-accelerated training.
- **Application Form Details**:
  - **HPC-Zielsysteme**: TinyGPU.
  - **Typische Jobgröße**: Estimated as 1 GPU.
  - **Insges. benötigte Rechenzeit**: Rough estimate of total computation time (number of runs × duration per run).
  - **Benötigter Speicherplatz**: Only if more than 1TB is needed.
- **RRZE Customer ID**: Available from thesis supervisor or RRZE contact person.
- **Fees**: Basic usage is free for FAU members for thesis work and publicly funded research.

## General Learnings
- FAU provides HPC resources for thesis work.
- Application process may vary; consult thesis supervisor or RRZE contact.
- TinyGPU cluster is suitable for GPU-intensive tasks.
- Basic HPC usage is free for eligible FAU members.
- Application form requires estimates for job size, computation time, and storage if exceeding 1TB.
---

### 2022111042000421_Jobon%20TinyGPU%20does%20not%20make%20use%20of%20GPU%20-%20iwfa008h.md
# Ticket 2022111042000421

 # HPC Support Ticket: Job on TinyGPU Not Utilizing GPU

## Keywords
- TinyGPU
- GPU utilization
- Job configuration
- Certificate expiration

## Summary
A user reported that their job on TinyGPU was not utilizing the GPU. The HPC Admin identified that the job configuration was not set up to use the GPU.

## Root Cause
- The job configuration did not include the necessary settings to utilize the GPU.

## Solution
- The user was advised to check and update their job configuration to ensure it makes use of the GPU.

## General Learnings
- Always verify job configurations to ensure they are set up to utilize the intended resources.
- Regularly check for and update expired certificates to avoid disruptions in service.

## Next Steps
- If similar issues arise, guide the user to review and correct their job configuration settings.
- Ensure that all relevant certificates are up to date to maintain smooth operations.

## Relevant Contacts
- **HPC Admins**: For job configuration and resource utilization issues.
- **2nd Level Support Team**: For additional technical support and troubleshooting.
- **Gehard Wellein**: Head of the Datacenter for broader infrastructure concerns.
- **Georg Hager**: Training and Support Group Leader for training and support needs.
- **Harald Lanig**: For NHR Rechenzeit Support and Applications for Grants.
- **Jan Eitzinger and Gruber**: Software and Tools developers for software-related issues.

## Additional Notes
- Ensure that users are aware of the correct procedures for configuring jobs to utilize specific resources like GPUs.
- Provide documentation or training sessions on job configuration best practices to minimize such issues in the future.
---

### 2024090442003771_Tier3-Access-Alex%20%22Farid%20Tasharofi%22%20_%20iwi5200h.md
# Ticket 2024090442003771

 # HPC Support Ticket: Tier3-Access-Alex

## Keywords
- HPC Account Activation
- Miniconda Environment
- GPU Allocation
- Job Queue Times
- Deep Learning
- Metal Artifact Reduction
- CT Imaging
- A100 GPU
- Fourier Transform
- PyTorch
- cuDNN
- FFT Libraries

## Summary
A user requested access to the HPC cluster 'Alex' for GPU-intensive deep learning tasks related to Metal Artifact Reduction in CT imaging. The user had previously been using the TinyGPU cluster but faced long job queue times.

## Problem
- **Root Cause**: High demand and long job queue times on the TinyGPU cluster were slowing down the user's research progress.
- **Specific Needs**: The user required access to the Alex cluster, specifically the A100 GPUs, for faster processing times and increased computational power.

## Solution
- **HPC Admin Response**: The HPC account was enabled on the Alex cluster. The user was advised to comply with the terms of use for Anaconda Inc. when using their own Miniconda environment.
- **Additional Information**: The user was informed about the current high load on Alex and advised that the A40 GPUs might be less loaded than the A100 GPUs.

## General Learnings
- **Account Activation**: Ensure that user accounts are properly enabled for the requested HPC cluster.
- **Software Compliance**: Remind users to comply with the terms of use for any third-party software they install, such as Miniconda.
- **Cluster Load Management**: Inform users about the current load on the cluster and provide alternatives if necessary.
- **Resource Allocation**: Understand the specific computational needs of users, such as the requirement for high-precision calculations and large-scale matrix operations, to allocate appropriate resources.

## Follow-Up Actions
- Monitor the user's job submissions to ensure they are complying with the terms of use for third-party software.
- Provide updates on cluster load and any changes in resource availability.

---

This documentation can be used as a reference for support employees to handle similar requests or issues related to HPC account activation, resource allocation, and software compliance.
---

### 2018090642001173_Problem%20with%20V100%20Amber16.md
# Ticket 2018090642001173

 # HPC Support Ticket: Problem with V100 Amber16

## Keywords
- V100 graphic cards
- Resource utilization
- Walltime
- Job termination
- Amber16

## Problem Description
- User's calculation on new V100 graphic cards terminated prematurely.
- Job ended after a few minutes despite setting walltime to 23:59:59.
- Calculation was not completed.

## Root Cause
- Job was killed due to poor resource utilization.
- Only 1 out of 4 available V100 cards was used.

## Solution
- Ensure efficient use of allocated resources.
- Distribute the workload across all available V100 cards.

## General Learnings
- Monitor resource utilization to prevent job termination.
- Optimize job scripts to make use of all allocated resources.
- Understand the HPC system's policies on resource management.

## Related Ticket
- Subject: Problem with V100 Amber16
- Date: 06.09.2018

## Support Team
- HPC Admins
- 2nd Level Support Team
---

### 2024082942000175_Jobs%20on%20Alex%20are%20not%20using%20alle%20GPU%20%5Bb155ee10%5D.md
# Ticket 2024082942000175

 # HPC Support Ticket: Jobs Not Using All Allocated GPUs

## Keywords
- GPU utilization
- SLURM
- `#SBATCH --ntasks-per-node`
- `nvidia-smi`
- ClusterCockpit
- JAX parallelization

## Problem Description
- User's jobs on the HPC system were not utilizing all allocated GPUs.
- Only one out of 4/8 allocated GPUs was being used.

## Root Cause
- Incorrect SLURM directive: `#SBATCH --ntasks-per-node=1` instead of `#SBATCH --ntasks-per-node=nGPU`.
- User's code was using the wrong parallelization strategy in JAX.

## Solution
- Correct the SLURM directive to `#SBATCH --ntasks-per-node=nGPU`.
- Adjust the JAX parallelization strategy to ensure proper utilization of all allocated GPUs.

## Monitoring and Diagnostics
- Use ClusterCockpit to monitor GPU utilization.
- Attach to running jobs using `srun --pty --overlap --jobid YOUR-JOBID bash` and run `nvidia-smi` to check GPU utilization.

## Best Practices
- Ensure that jobs only allocate nodes with GPUs if the code can actually utilize them.
- Regularly monitor resource utilization to avoid idle resources.

## Contact Information
- For further assistance, contact HPC Support at `support-hpc@fau.de`.

## References
- [ClusterCockpit Monitoring System](https://monitoring.nhr.fau.de/)
- [HPC FAU](https://hpc.fau.de/)
---

### 2018041042002164_RAM%20auf%20tinygpu.md
# Ticket 2018041042002164

 # HPC-Support Ticket: RAM Issue on tinyGPU

## Subject: RAM auf tinyGPU

### User:
- **Issue**: User encounters 'out of memory' errors when using more than ~16GB RAM on tinyGPU nodes, despite the nodes having 64GB RAM.
- **Observation**: Memory limits seem to be set at 16GB, causing bottlenecks especially when using both CPU and GPU for data preparation.
- **Question**: Is this a configuration issue? Can anything be done to resolve it?

### HPC Admin:
- **Explanation**: Memory limits are set via "cgroups" when only part of a GPU node is requested.
  - 11.5 GB per 4 cores if the job can run on all TinyGPU nodes.
  - 15.5 GB per 4 cores if the job is restricted to newer TinyGPU nodes.
- **Solution**: Requesting a full TinyGPU node (ppn=8:gtx980 or ppn=16:*) should remove memory limits.
- **Verification**: Check "qstat -a" output for "Req'd Memory" column. It should show "--" for full-node jobs.

### User:
- **Follow-up**: User confirms the issue persists even when requesting a full node.
- **Test**: Provided Python script to allocate memory, which fails at 16GB.
- **Additional Info**: Memory limits appear correct, but allocation fails.

### HPC Admin:
- **Further Investigation**: Admin unable to reproduce the issue.
- **Potential Cause**: Suspected issue with swap partition size due to a bug in the Ubuntu installer.
- **Resolution**: Ensured sufficient swap space on all TinyGPU nodes to prevent memory allocation issues.

### User:
- **Resolution**: Issue resolved spontaneously without user intervention.
- **Acknowledgment**: Thanks HPC support for their patience and assistance.

### HPC Admin:
- **Final Note**: Issue with memory allocation should now be resolved due to increased swap space.

## Keywords:
- RAM issue
- tinyGPU
- memory limits
- cgroups
- swap partition
- out of memory error

## General Learning:
- Understanding memory limits set by cgroups on partial node requests.
- Importance of sufficient swap space for memory allocation.
- Verification of memory limits using `qstat -a` and `qstat -f JOBID`.
- Troubleshooting memory allocation issues with Python and C programs.
---

### 2020100642003977_Jobs%20auf%20TinyGPU%20-%20kein%20mem%3D32gb%20_%20iwal016h.md
# Ticket 2020100642003977

 # HPC Support Ticket: Jobs auf TinyGPU - kein mem=32gb

## Keywords
- TinyGPU
- mem=32gb
- Hauptspeicherausstattung
- GPU-Anzahl
- Knotentypen

## Problem
- User submitted jobs on TinyGPU with "mem=32gb", leading to inefficient GPU allocation.
- Misinterpretation of the memory specifications from the documentation.

## Root Cause
- User assumed nodes had 128GB of memory based on a misreading of the documentation.

## Solution
- Do not specify memory requirements (e.g., "mem=32gb") when submitting jobs on TinyGPU.
- The system will automatically allocate the maximum available memory based on the selected GPU count and node type.

## General Learning
- Memory specifications vary between node generations.
- Avoid specifying memory requirements to ensure optimal resource allocation.
- Future jobs with specified memory requirements may be rejected by the Torque-Submitfilter.

## References
- [TinyGPU Cluster Documentation](https://www.anleitungen.rrze.fau.de/hpc/tinyx-clusters/#tinygpu)

## Roles
- **HPC Admins**: Provided guidance on job submission and memory allocation.
- **User**: Misinterpreted documentation and submitted jobs with incorrect memory specifications.

## Additional Notes
- The certificate has expired, which may affect communication or access.
- Ensure documentation is clear and up-to-date to avoid user confusion.
---

### 2024051742002692_CPU%20Jobs%20auf%20Alex%20-%20b225cb.md
# Ticket 2024051742002692

 # HPC Support Ticket Conversation Analysis

## Subject: CPU Jobs auf Alex - b225cb

### Keywords:
- CPU/RAM-intensive jobs
- GPU nodes
- SLURM
- Login node
- CPU-only cluster
- Fritz
- NHR Versorgungsbereich

### Problem:
- User needs to run CPU/RAM-intensive jobs to prepare data for GPU jobs.
- Unsure about the appropriate partition or instance on Alex.
- SLURM does not allow allocation of CPU resources without GPUs.
- Running such jobs on the login node is not optimal.

### Solution:
- Alex nodes are fixed partitioned for CPUs and GPUs, making it impossible to allocate CPU resources without GPUs.
- For CPU-only workloads, a dedicated CPU-only cluster (Fritz) is recommended.
- The user's project (b225cb) has been enabled on Fritz.

### General Learnings:
- Always check the partitioning scheme of the cluster before submitting jobs.
- Use dedicated CPU-only clusters for CPU/RAM-intensive jobs.
- Avoid running intensive jobs on login nodes.
- SLURM configurations may not allow certain resource allocations; consult documentation or support for alternatives.

### Actions Taken:
- HPC Admin coordinated with relevant personnel to enable the user's project on Fritz.
- User was informed about the availability of Fritz for their workload.

### Closure:
- The ticket was closed after the user's project was enabled on Fritz and the user was informed.

### References:
- [Fritz Cluster Documentation](https://hpc.fau.de/)
- [SLURM Documentation](https://slurm.schedmd.com/documentation.html)

### Support Team Involved:
- HPC Admins
- 2nd Level Support Team (Kuckuk, Sebastian)

### Additional Notes:
- Ensure users are aware of the appropriate clusters for their specific workloads.
- Provide clear documentation on cluster partitioning and resource allocation policies.
---

### 2023022242001994_Tier3-Access-Alex%20%22Dreier%20Marcel%22%20_%20iwi5123h.md
# Ticket 2023022242001994

 # HPC Support Ticket Summary

## Keywords
- HPC Account Activation
- Certificate Expiration
- GPGPU Cluster 'Alex'
- Nvidia A40 GPGPUs
- CUDA
- PyTorch
- PyTorch Lightning
- Diffusion Models
- Handwriting Imitation

## Summary
- **User Request:** Access to GPGPU cluster 'Alex' for training diffusion models for offline handwriting imitation.
- **Required Resources:** Nvidia A40 GPGPUs with 48 GB VRAM.
- **Software Needed:** CUDA, PyTorch, PyTorch Lightning.
- **Expected Outcome:** Improved handwriting imitation models capable of generating handwritten images at the paragraph level.

## Issue
- **Root Cause:** Certificate expiration.
- **Solution:** HPC Admin enabled the user's HPC account (iwi5123h) on 'Alex'.

## General Learnings
- Ensure certificates are up-to-date to avoid account access issues.
- Nvidia A40 GPGPUs are suitable for tasks requiring high VRAM, such as training diffusion models with self-attention mechanisms.
- Regularly update and monitor HPC account status to prevent disruptions in user access.

## Next Steps for Similar Issues
- Check certificate validity.
- Enable or renew the user's HPC account access.
- Confirm the availability of required resources and software.
---

### 2024013142001137_Jobs%20on%20Alex%20stopped%20using%20GPU%20%28b143dc22%29.md
# Ticket 2024013142001137

 # HPC Support Ticket: Jobs on Alex Stopped Using GPU

## Keywords
- GPU utilization
- Job configuration
- Resource allocation
- Monitoring
- SLURM script

## Summary
- **Issue**: Some jobs on the HPC system Alex stopped using the allocated GPUs.
- **Affected Jobs**:
  - [Job 6337363](https://monitoring.nhr.fau.de/monitoring/job/6337363)
  - [Job 6337713](https://monitoring.nhr.fau.de/monitoring/job/6337713)
  - [Job 6337783](https://monitoring.nhr.fau.de/monitoring/job/6337783)
  - [Job 6337784](https://monitoring.nhr.fau.de/monitoring/job/6337784)

## Root Cause
- Jobs were requesting more GPUs than they were utilizing.
- Jobs were requesting 80 GB A100 GPUs but only using a fraction of the GPU RAM.

## Solutions
1. **Adjust GPU Allocation**:
   - Change the SLURM script to request only the number of GPUs actually needed.
   - Example: Change `#SBATCH --gres=gpu:a100:8` to `#SBATCH --gres=gpu:a100:4` or `#SBATCH --gres=gpu:a100:1`.

2. **Optimize GPU Type**:
   - Consider using 40 GB A100 GPUs instead of 80 GB if the RAM utilization is low.
   - Remove the constraint `#SBATCH -C a100_80` to allow the use of all types of A100 GPUs.

## General Learnings
- **Efficient Resource Allocation**: Ensure that the number of GPUs requested matches the actual usage to avoid wasting resources.
- **Monitoring and Adjustment**: Regularly monitor job performance and adjust resource requests accordingly.
- **Communication**: Inform users about the importance of efficient resource allocation and provide guidance on optimizing their job configurations.

## Follow-Up Actions
- **User Notification**: Inform the user about the issue and provide guidance on adjusting their job configurations.
- **Monitoring**: Continue monitoring job performance to ensure efficient resource utilization.
- **Escalation**: If the issue persists, consider escalating to higher-level support or management.

## Closure
- The ticket was closed after multiple attempts to resolve the issue and inform the user about the necessary adjustments.
---

### 2024012942003407_Tier3-Access-Fritz%20%22Manuel%20M%C3%83%C2%BCnsch%22%20_%20iwst93%20%2B%20ANSYS-Lizenz%20LSTM.md
# Ticket 2024012942003407

 # HPC-Support Ticket Conversation Summary

## Keywords
- Tier3-Access-Fritz
- Neko
- Nek5000
- FASTEST3-D
- LES benchmark cases
- ML-based sub-models
- Ansys
- Fluent
- GPU architecture
- NHR access
- Software licenses
- Preisliste
- RRZE-Angebote
- CADFEM
- StarCCM

## General Learnings
- **Tier3-Grundversorgung Limits**: The limits for Tier3-Grundversorgung are not set in stone and can be adjusted based on the group's needs.
- **Software Modules**: Pre-built modules for software like Neko are available and can be used instead of building them from scratch.
- **Ansys Licenses**: The process for obtaining Ansys licenses and their integration with RRZE and CADFEM needs to be clarified.
- **GPU Architecture**: Testing with Fluent on Alex can provide significant speed improvements, but the cost in anshpc-Tokens should be considered.
- **Coordination with RRZE**: Regular communication with the RRZE software department is essential for obtaining flexible and extrapolated software license offers.

## Root Cause of Problems
- **Unrealistic Resource Request**: The initial request for 500,000 node hours was deemed unrealistic for Tier3-Grundversorgung.
- **Lack of Ansys Users**: There is a current shortage of Ansys users, which affects the testing and utilization of the software.
- **License Management**: The process for obtaining and managing software licenses, especially for Ansys, is not well-defined and needs clarification.

## Solutions
- **Adjust Resource Limits**: The resource limits were adjusted to be more in line with Tier3-Grundversorgung standards.
- **Use Pre-built Modules**: Pre-built modules for Neko were suggested to be used instead of building them from scratch.
- **Coordinate with RRZE**: Regular communication with the RRZE software department was recommended to obtain flexible and extrapolated software license offers.
- **Test with Fluent**: Testing with Fluent on Alex was suggested for potential speed improvements, considering the cost in anshpc-Tokens.

## Documentation for Support Employees
- **Resource Limits**: Ensure that resource requests are within the limits of Tier3-Grundversorgung. Adjustments can be made based on the group's needs.
- **Software Modules**: Check for pre-built modules for the required software before building them from scratch.
- **Ansys Licenses**: Clarify the process for obtaining and managing Ansys licenses with the RRZE software department and CADFEM.
- **GPU Architecture**: Consider testing with Fluent on Alex for potential speed improvements, but be aware of the cost in anshpc-Tokens.
- **Coordination with RRZE**: Maintain regular communication with the RRZE software department to obtain flexible and extrapolated software license offers.
---

### 2022101242004095_GPU-Knoten%20von%20Megware%20eingetroffen%3F.md
# Ticket 2022101242004095

 # HPC Support Ticket: GPU Node Delivery Status

## Keywords
- GPU Node
- A100
- Megware
- Delivery
- Payment
- HPL Measurement
- Device Passport
- Serial Numbers

## Summary
A user inquired about the delivery status and condition of an A100 GPU node from Megware. The HPC Admin confirmed the delivery and stability of the node, and advised that payment can proceed. Additionally, the admin mentioned that Megware should send a device passport with serial numbers.

## Root Cause
- User awaiting confirmation of GPU node delivery and condition before proceeding with payment.

## Solution
- HPC Admin confirmed the delivery and stability of the GPU node.
- Payment can proceed as per the admin's confirmation.
- Await the device passport with serial numbers from Megware.

## General Learnings
- Always confirm the delivery and condition of hardware before proceeding with payment.
- Ensure that all necessary documentation (e.g., device passport, serial numbers) is received.
- Regular communication with the vendor and internal teams is crucial for smooth operations.
---

### 2021102742000214_Memory%20allocation%20tinygpu.md
# Ticket 2021102742000214

 # HPC Support Ticket: Memory Allocation on tinygpu Cluster

## Keywords
- tinygpu cluster
- RTX3080
- Memory allocation
- sbatch options (--mem, --mem-per-gpu)
- Out-of-memory error
- A100 nodes

## Problem
- User needs an RTX3080 GPU and around 80GB of RAM for a memory-intensive job.
- Automatic memory allocation of 40GB results in an out-of-memory error.
- Attempts to use `--mem` and `--mem-per-gpu` options in sbatch result in an error message stating not to specify `--mem` for GPU jobs.

## Root Cause
- The tinygpu cluster automatically allocates memory based on the number of GPUs requested, which is insufficient for the user's job.
- The user is unaware of alternative nodes with higher memory capacity.

## Solution
- **HPC Admin** suggests using A100 nodes, which come with 117GB of RAM, as an alternative to RTX3080 nodes.
- If the user insists on RTX3080, the only option is to reserve more GPUs to increase memory allocation, even if it wastes resources.

## General Learnings
- Specific GPU types have different memory allocations.
- Some clusters automatically allocate memory based on GPU count.
- Alternative node types may offer higher memory capacity.
- It's essential to communicate available resources and workarounds to users effectively.
---

### 2023062142001881_Tier3-Access-Fritz%20%22Julian%20Wechsler%22%20_%20iwal024h.md
# Ticket 2023062142001881

 # HPC Support Ticket Analysis

## Keywords
- Tier3 Access
- Fritz (Parallelrechner)
- Alex (GPGPU-Cluster)
- PyTorch
- Neural Network Training/Evaluation
- GPU
- Certificate Expired
- Account Activation

## Summary
A user submitted a request for Tier3 access to Fritz for neural network training/evaluation using PyTorch. The HPC Admin identified that the workload would be better suited for Alex, the GPGPU-Cluster, due to the need for GPUs. The user confirmed the mistake and requested access to Alex instead. The HPC Admin activated the user's account on Alex.

## Root Cause
- User followed the wrong link and requested access to the wrong cluster (Fritz instead of Alex).

## Solution
- The HPC Admin activated the user's account on the correct cluster (Alex).

## General Learnings
- Neural network training/evaluation workloads typically require GPUs.
- It's important to verify that users are requesting access to the appropriate cluster based on their workload needs.
- Quick account activation can resolve user errors in requesting access to the wrong cluster.

## Related Teams
- HPC Admins
- 2nd Level Support Team
- Datacenter Head
- Training and Support Group Leader
- NHR Rechenzeit Support
- Software and Tools Developers
---

### 2025022842001201_GPUs%20allocated%20but%20not%20utilized%20-%20v100dd12.md
# Ticket 2025022842001201

 # HPC Support Ticket: GPUs Allocated but Not Utilized

## Keywords
- GPU utilization
- Job monitoring
- ClusterCockpit
- `nvidia-smi`
- Resource allocation

## Problem
- User's jobs on Alex (JobIDs 2418981, 2418980, 2418937) allocated GPUs but did not utilize them.

## Root Cause
- The user's code did not make use of the allocated GPU resources.

## Solution
- **Monitoring GPU Utilization:**
  - Use ClusterCockpit: [Monitoring System](https://monitoring.nhr.fau.de/) | [Documentation](https://doc.nhr.fau.de/job-monitoring-with-clustercockpit/)
  - Attach to running job and check GPU utilization:
    ```bash
    srun --pty --overlap --jobid YOUR-JOBID bash
    nvidia-smi
    ```
- **Resource Allocation:**
  - Ensure that jobs only allocate nodes with GPUs if the code can utilize them.

## General Learning
- Always verify resource utilization to avoid idle resources.
- Use monitoring tools to check job performance and resource usage.
- Properly allocate resources based on job requirements to optimize HPC usage.

## Contact
- For further assistance, contact the HPC support team: [support-hpc@fau.de](mailto:support-hpc@fau.de)
- HPC website: [FAU HPC](https://hpc.fau.de/)
---

### 2022053142000331_Fwd%3A%20Experimentelle%20Astroteilchenphysik%20-%20W%203%20Kopper%20-%20Wunschpapier.md
# Ticket 2022053142000331

 # HPC-Support Ticket Conversation Analysis

## Keywords
- Deep Learning Workstation
- GPGPU Cluster
- GPU-Stunden
- Storage
- Rechenzeitanteil
- NHR
- FAU
- Berufungsverfahren
- IT-Bedarf

## General Learnings
- Importance of detailed technical specifications for accurate cost estimation.
- Necessity of quantifying GPU-Stunden for resource allocation.
- Consideration of storage requirements for KI-Anwendungen.
- Coordination between different departments for resource allocation.

## Root Cause of the Problem
- Lack of detailed technical specifications for Deep Learning Workstations.
- Unquantified GPU-Stunden requirement.
- Insufficient information on storage needs.

## Solution
- Provided detailed technical specifications for Deep Learning Workstations.
- Quantified GPU-Stunden requirement to 50,000-60,000 hours per year.
- Specified storage needs, including 100-200TB of long-term storage and 10-20TB with backup.
- Coordinated with HPC Admins to allocate resources and adjust budget accordingly.

## Documentation for Support Employees
When encountering similar requests for Deep Learning Workstations and GPU-Stunden, ensure the following steps are taken:
1. Request detailed technical specifications for accurate cost estimation.
2. Quantify the GPU-Stunden requirement to allocate resources effectively.
3. Specify storage needs, considering both long-term and backup storage.
4. Coordinate with HPC Admins to allocate resources and adjust budget accordingly.

This approach ensures that the IT-Bedarf is accurately assessed and resources are allocated efficiently.
---

### 2024070142003903_Tier3-Access-Alex%20%22Jingna%20Qiu%22%20_%20iwb0014h.md
# Ticket 2024070142003903

 ```markdown
# HPC Support Ticket Analysis: Tier3-Access-Alex

## Keywords
- Tier3 Access
- GPU-hours
- NHR Project
- Application
- Python
- Active Learning Methods
- A100 GPU
- Efficiency

## Summary
- **User Request**: Access to GPGPU cluster 'Alex' with Nvidia A100 GPUs.
- **Expected GPU-hours**: 40,000 GPU-hours/year.
- **Software Needed**: Python.
- **Application**: Investigating active learning methods for efficient data annotation.
- **Expected Results**: Demonstrations of method effectiveness and comparisons to state-of-the-art methods.
- **User Experience**: Previous experience with HPC tinyGPU, successful publications in top conferences.

## HPC Admin Response
- **Approval**: User granted access to Alex.
- **Note**: Expected GPU-hour demand is high, may require an application for an NHR project.
- **Reference**: [NHR Application Details](https://doc.nhr.fau.de/nhr-application/)

## Lessons Learned
- **GPU-hour Demand**: High GPU-hour demand may necessitate an application for an NHR project.
- **Efficiency**: A100 GPUs significantly improve experiment efficiency compared to RTX3080.
- **User Background**: Previous successful HPC usage and publications can influence access decisions.

## Root Cause of the Problem
- High GPU-hour demand for Tier3 access.

## Solution
- User granted access with a note on potential need for an NHR project application if demand remains high.
```
---

### 2023080942002748_Tier3-Access-Alex%20%22Tarakeshwar%20Lakshmipathy%22%20_%20iww1007h.md
# Ticket 2023080942002748

 ```markdown
# HPC Support Ticket Conversation Analysis

## Subject: Tier3-Access-Alex

### Keywords:
- Access Request
- GPGPU Cluster 'Alex'
- Nvidia A100, A40 GPUs
- LAMMPS Software
- Atomistic Simulations
- Precision Requirements
- Scientific Publications

### Summary:
- **User Request**: Access to GPGPU cluster 'Alex' for atomistic simulations using LAMMPS.
- **Resources Requested**:
  - Nvidia A100 GPUs (40 GB, 9.7 TFlop/s double precision)
  - Nvidia A40 GPUs (48 GB, 37 TFlop/s single precision)
  - 5000 GPU-hours
- **Justification**:
  - Large fracture simulations with LAMMPS may require mixed or double precision, hence A100 GPUs.
  - Smaller calculations can be run with A40 GPUs.
- **Expected Outcome**: Production runs resulting in scientific publications in materials science journals.

### HPC Admin Response:
- Access to Alex has been enabled.

### Lessons Learned:
- **Access Request Process**: Users need to specify their requirements clearly, including hardware, software, and expected outcomes.
- **Justification for Resources**: Users should provide a detailed justification for the specific resources they request, especially when dealing with high-performance hardware like A100 GPUs.
- **Precision Requirements**: Understanding the precision requirements for simulations is crucial for selecting the appropriate hardware.

### Root Cause of the Problem:
- User needed access to specific GPU resources for their simulations.

### Solution:
- HPC Admin enabled access to the requested resources.
```
---

### 2024090242004906_Anfrage%20auf%20Verl%C3%A4ngerung%20des%20Jobs%202030365%20auf%2040%20Tage%20-%20b185cb%20_%20AG%20H.md
# Ticket 2024090242004906

 To summarize the key points from the conversation:

1. **Initial Issue**: The user encountered difficulties with running a large job on the HPC system due to high CPU load and inefficient GPU utilization.
2. **Solution Steps**:
   - The user was advised to check the job's output and ensure the program was running as intended.
   - The user was informed about the monitoring system and how to check GPU utilization using `nvidia-smi`.
   - The user was advised to ensure that nodes with GPUs were only allocated if the code could actually make use of the GPU.
   - The user was informed about the importance of not wasting resources by allocating nodes with GPUs if the code could not utilize them.
3. **Additional Tips**:
   - The user was advised to clean up their home directory to avoid quota issues.
   - The user was informed about the importance of storing checkpoints in a reliable location and copying them to a backup system.
   - The user was advised to set the environment variable `NCCL_IB_HCA` to ensure proper utilization of Infiniband devices.
4. **Documentation**:
   - The user was informed about the plan to create a "Best-Practice-Guide" for using Infiniband/NCCL.
   - The user was asked to provide the final settings and configurations used for the job.

By following these steps, the user was able to resolve the issue and improve the efficiency of their job. The HPC support team provided valuable assistance and guidance throughout the process.
---

### 2023051142002285_Jobs%20on%20TinyGPU%20do%20not%20use%20allocated%20GPUs%20%5Bmpt2027h%5D.md
# Ticket 2023051142002285

 # HPC Support Ticket: Jobs on TinyGPU do not use allocated GPUs

## Keywords
- GPU utilization
- Job allocation
- `nvidia-smi`
- `srun`
- Resource management

## Problem Description
- User's jobs on TinyGPU/Alex (JobIDs 592138 and 592047) were not utilizing the allocated GPUs.
- Monitoring system indicated idle GPU resources.

## Root Cause
- The user's code did not support multiple GPUs, leading to inefficient resource allocation.

## Solution
- **HPC Admin** advised the user to:
  - Attach to the running job using `srun --pty --overlap --jobid YOUR-JOBID bash`.
  - Check GPU utilization with `nvidia-smi`.
  - Ensure that jobs only allocate GPUs if the code can utilize them.

## Lessons Learned
- Always verify that your code can utilize allocated GPU resources.
- Use `nvidia-smi` to monitor GPU utilization.
- Proper resource allocation helps in efficient use of HPC resources.

## Follow-up
- The ticket was closed as the user acknowledged the issue and agreed to be mindful of GPU allocation in the future.

## References
- [GitHub Issue on Multiple GPU Support](https://github.com/DLR-RM/stable-baselines3/issues/75)
---

### 2022020242001032_Inefficient%20jobs%20on%20TinyGPU%20-%20iwal050h.md
# Ticket 2022020242001032

 # HPC Support Ticket: Inefficient Jobs on TinyGPU

## Keywords
- GPU utilization
- Interactive jobs
- Batch jobs
- TinyGPU
- CUDA
- Deep learning
- Job throttling

## Summary
A user was running inefficient jobs on the TinyGPU cluster with near-zero GPU utilization. The issue persisted despite previous notifications, leading to restrictions on GPU access.

## Root Cause
- The user was running interactive jobs and leaving them idle.
- Batch jobs were consuming CPU time but not utilizing the GPU.
- The user's code was not properly configured to use the GPU.

## Solution
- The user was advised to check their application and input configuration to improve GPU utilization.
- The user was instructed to use CPU-only clusters (e.g., Woody) for jobs that do not require GPUs.
- The user was reminded to close interactive sessions when not in use.
- The user's personal throttling was removed, but group throttling may still apply due to limited resources.

## General Learnings
- Always monitor GPU utilization for jobs running on GPU clusters.
- Use CPU-only clusters for jobs that do not require GPUs.
- Properly configure applications to make use of available GPUs.
- Be mindful of idle interactive sessions and close them when not in use.
- Be patient with job queues, as wait times are normal on HPC clusters.

## Related Documentation
- [Systems Documentation and Instructions](https://hpc.fau.de/systems-services/systems-documentation-instructions/)
---

### 2023031642001539_Zugang%20zum%20Alex%20GPU%20Cluster.md
# Ticket 2023031642001539

 ```markdown
# HPC Support Ticket: Access to Alex GPU Cluster

## Keywords
- Alex GPU Cluster
- A100 GPUs
- Account Activation
- Fraunhofer

## Summary
A user requested access to the Alex GPU Cluster, specifically mentioning the integration of A100 GPUs from Fraunhofer.

## Root Cause
- User needed access to the Alex GPU Cluster for computational imaging and algorithms research.

## Solution
- HPC Admin granted access to the user's account for the Alex GPU Cluster.

## What Can Be Learned
- Users from Fraunhofer may request access to specific GPU clusters for their research.
- HPC Admins can activate accounts for specific clusters upon request.
- Ensure proper communication and verification before granting access.
```
---

### 2024102842004525_Tier3-Access-Alex%20%22Sally%20Zeitler%22%20_%20iwi5245h.md
# Ticket 2024102842004525

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Keywords
- Tier3-Access-Alex
- GPGPU cluster 'Alex'
- Nvidia A100 GPGPUs
- Nvidia A40 GPGPUs
- GPU-hours
- TinyGPU
- Maintenance mode
- Scheduled downtime
- NHR project
- Python
- Cuda
- Training of foundational models
- Classification and prediction of material failure

## General Learnings
- **Initial Request**: User requested access to GPGPU cluster 'Alex' for training foundational models and custom models for classification and prediction of material failure.
- **Compute Time**: User requested 5000 GPU-hours per year, which exceeds Tier3 limits.
- **Software Requirements**: Python and Cuda.
- **HPC Admin Response**: User advised to gain experience with TinyGPU before accessing Alex. For compute time beyond Tier3, user directed to apply for an NHR project.
- **Maintenance Issue**: User reported TinyGPU nodes in maintenance mode. HPC Admin provided a link to scheduled downtime information.
- **Follow-up**: User inquired about Alex access after scripts ran successfully on TinyGPU. HPC Admin granted access to Alex.

## Root Cause of Problems
- **Compute Time Request**: User requested compute time beyond Tier3 limits.
- **Maintenance Mode**: TinyGPU nodes were in maintenance mode, causing user confusion.

## Solutions
- **Compute Time**: User directed to apply for an NHR project for compute time beyond Tier3.
- **Maintenance Mode**: HPC Admin provided a link to scheduled downtime information for user awareness.

## Documentation for Support Employees
- **Initial Access Request**: Ensure users gain experience with TinyGPU before accessing Alex.
- **Compute Time Limits**: Direct users to apply for an NHR project if compute time exceeds Tier3 limits.
- **Maintenance Communication**: Provide users with links to scheduled downtime information to address maintenance mode queries.
```
---

### 2025012742002311_Jobs%20on%20Alex%20is%20only%20using%201%20of%203%20GPU%20%5Bv115be14%5D.md
# Ticket 2025012742002311

 # HPC Support Ticket: Jobs Using Only 1 of 3 Allocated GPUs

## Keywords
- GPU utilization
- Job allocation
- Resource management
- Monitoring system
- ClusterCockpit
- `nvidia-smi`
- `srun`

## Issue
- User's jobs were only utilizing 1 out of 3 allocated GPUs.

## Root Cause
- Potential issue with the user's code not properly utilizing all allocated GPUs.

## Solution
- **HPC Admin** notified the user about the underutilization of GPUs.
- User was advised to check GPU utilization using `nvidia-smi` after attaching to the running job with `srun --pty --overlap --jobid YOUR-JOBID bash`.
- User was also directed to the monitoring system ClusterCockpit for visualization.
- User decided to cancel the jobs due to the issue.

## Lessons Learned
- Always ensure that jobs are properly utilizing allocated resources to avoid wastage.
- Use monitoring tools like ClusterCockpit and `nvidia-smi` to check resource utilization.
- Communicate with users to resolve resource allocation issues promptly.

## Follow-up Actions
- Monitor similar jobs to ensure proper GPU utilization.
- Provide additional training or documentation on efficient resource usage if needed.
---

### 2025022442000531_GPU%20allocated%20but%20not%20utilized%20-%20bccc117h.md
# Ticket 2025022442000531

 # HPC Support Ticket: GPU Allocated but Not Utilized

## Keywords
- GPU utilization
- Job monitoring
- ClusterCockpit
- `nvidia-smi`
- Resource allocation

## Problem Description
- User's job on Alex (JobID 2407337) is not utilizing the allocated GPUs.

## Root Cause
- The job is allocated 4 GPUs, but the code does not make use of them.

## Solution
- **Monitoring GPU Utilization:**
  - Use ClusterCockpit for job monitoring:
    - [ClusterCockpit](https://monitoring.nhr.fau.de/)
    - [Documentation](https://doc.nhr.fau.de/job-monitoring-with-clustercockpit/)
  - Attach to the running job using `srun`:
    ```bash
    srun --pty --overlap --jobid YOUR-JOBID bash
    ```
  - Check GPU utilization with `nvidia-smi`.

- **Resource Allocation:**
  - Ensure that the code can utilize GPUs before allocating nodes with GPUs.
  - Avoid idle GPU resources by properly configuring the job to use the allocated GPUs.

## General Learning
- Always verify that the job is configured to use the allocated resources.
- Use monitoring tools to check resource utilization during job execution.
- Proper resource allocation helps in efficient use of HPC resources.

## Contact Information
- For further assistance, contact HPC support:
  ```plaintext
  support-hpc@fau.de
  ```
- Additional resources:
  - [FAU HPC Website](https://hpc.fau.de/)
---

### 2022051342000785_Tier3-Access-Alex%20%22Finn%20Klein%22%20_%20iwi9015h.md
# Ticket 2022051342000785

 # HPC Support Ticket Analysis: Tier3-Access-Alex

## Keywords
- GPGPU cluster 'Alex'
- Nvidia A100 GPGPUs
- Singularity/pytorch
- Analysis-by-synthesis classifier
- ShapeNet
- Lightfield networks
- Adversarial attacks
- Foolbox
- File I/O
- Fileserver performance

## Summary
- **User Request**: Access to GPGPU cluster 'Alex' for training an analysis-by-synthesis classifier on ShapeNet using Lightfield networks and running adversarial attacks using Foolbox.
- **Resource Allocation**: 4 GPU days per month.
- **Software Requirements**: Singularity/pytorch.

## Issues and Solutions
- **Issue**: High file I/O (70,000 file open/close operations per minute) causing fileserver performance degradation.
  - **Root Cause**: Frequent file operations from a specific directory.
  - **Solution**: Modify code to reduce I/O operations, possibly by loading data into memory once.

- **Issue**: Concern about the benefit of moving to Alex for only 4 GPU days per month.
  - **Solution**: Evaluate the necessity and benefits of the move based on the user's requirements and resource availability.

## General Learnings
- **File I/O Management**: High frequency of file operations can significantly impact fileserver performance. Optimizing code to reduce I/O operations is crucial.
- **Resource Allocation**: Evaluate the necessity and benefits of resource allocation based on user requirements and system capacity.
- **User Communication**: Clear and prompt communication with users about system performance and resource usage is essential for maintaining system efficiency.

## Actions Taken
- **HPC Admins**: Enabled user account on Alex, provided feedback on resource allocation, and advised on code optimization to reduce file I/O.
- **User**: Acknowledged the issue and inquired about past similar incidents.

## Future Considerations
- **Monitoring**: Implement monitoring tools to detect and alert high I/O operations.
- **Documentation**: Provide guidelines and best practices for efficient file I/O management in user documentation.

---

This report aims to document the issues, solutions, and general learnings from the support ticket to assist in resolving similar issues in the future.
---

### 2022060342001247_Job%20on%20TinyGPU%20only%20uses%20two%20of%20three%20allocated%20GPUs%20%5Biwal097h%5D.md
# Ticket 2022060342001247

 # HPC Support Ticket: Job on TinyGPU Only Uses Two of Three Allocated GPUs

## Keywords
- GPU utilization
- Resource allocation
- Job monitoring
- `nvidia-smi`
- TinyGPU

## Summary
A user's job on TinyGPU was only utilizing two out of three allocated GPUs, leading to inefficient resource usage.

## Root Cause
The user's code was not configured to utilize all allocated GPUs, resulting in one GPU remaining idle.

## Solution
1. **Monitor GPU Utilization**: Use `nvidia-smi` to monitor GPU usage.
   ```bash
   ssh <node>
   nvidia-smi
   ```
2. **Optimize Resource Allocation**: Ensure that the code can utilize all allocated GPUs. If not, adjust the resource allocation to match the actual usage.
3. **Documentation**: Refer to the official documentation for working with NVIDIA GPUs: [Working with NVIDIA GPUs](https://hpc.fau.de/systems-services/systems-documentation-instructions/special-applications-and-tips-tricks/working-with-nvidia-gpus/).

## Lessons Learned
- Regularly monitor GPU utilization to ensure efficient resource usage.
- Allocate resources based on actual code requirements to avoid idle resources.
- Use `nvidia-smi` for real-time GPU monitoring.

## Follow-Up Actions
- If the issue persists, consider throttling the user's resource allocation and monitor for further complaints.
- Ensure that the user is aware of the importance of efficient resource usage and provide assistance if needed.
---

### 2024082242000197_Job%20on%20Alex%20do%20not%20use%20GPU%20%5Biwi5197h%5D.md
# Ticket 2024082242000197

 # HPC Support Ticket: Job on Alex Not Using All Allocated GPUs

## Keywords
- GPU utilization
- Job allocation
- Monitoring system
- ClusterCockpit
- `nvidia-smi`
- `srun`
- `--nproc_per_node`
- `$SLURM_GPUS_ON_NODE`

## Summary
A user's job on the HPC cluster was not utilizing all allocated GPUs, leading to resource wastage.

## Root Cause
The job script parameter `--nproc_per_node=2` was likely causing the underutilization of GPUs.

## Solution
- The parameter should be adjusted to `--nproc_per_node="$SLURM_GPUS_ON_NODE"` to ensure all allocated GPUs are utilized.
- Users should monitor GPU utilization using the ClusterCockpit monitoring system or by attaching to the running job with `srun --pty --overlap --jobid YOUR-JOBID bash` and running `nvidia-smi`.

## Lessons Learned
- Always ensure that job scripts are configured to utilize all allocated resources.
- Regularly monitor resource utilization to identify and address underutilization issues.
- Use appropriate job script parameters to match resource allocation with actual usage.

## Actions Taken
- HPC Admin notified the user about the underutilization issue and provided guidance on how to monitor and adjust GPU usage.
- The user acknowledged the issue and committed to preventing it in the future.

## References
- ClusterCockpit monitoring system: [https://monitoring.nhr.fau.de/](https://monitoring.nhr.fau.de/)
- HPC support contact: [support-hpc@fau.de](mailto:support-hpc@fau.de)
- HPC website: [https://hpc.fau.de/](https://hpc.fau.de/)
---

### 2022040642000835_Job%20%28JobID%2092923%29%20auf%20Alex%20nutzt%20keine%20GPU%20%5Biwi5046h%5D.md
# Ticket 2022040642000835

 ```markdown
# HPC Support Ticket: Job (JobID 92923) auf Alex nutzt keine GPU

## Keywords
- GPU utilization
- Job monitoring
- nvidia-smi
- SSH login
- Resource allocation

## Summary
A user's job on the HPC system was not utilizing the allocated GPUs. The HPC Admin notified the user about the issue and provided steps to check GPU utilization.

## Issue
- **Root Cause**: The job was stuck during dataset creation, leading to no GPU utilization.
- **Symptoms**: The job was allocated four GPUs but showed no activity on them.

## Steps Taken
1. **HPC Admin**:
   - Notified the user about the job not utilizing GPUs.
   - Provided a screenshot from the monitoring system.
   - Instructed the user to log in via SSH and use `nvidia-smi` to check GPU utilization.
   - Advised the user to only request GPU nodes if the code can utilize them.

2. **User**:
   - Acknowledged the issue and stopped the job.
   - Committed to investigating why the job got stuck during dataset creation.

## Solution
- The user stopped the job and planned to investigate the cause of the dataset creation issue.

## Lessons Learned
- Regularly monitor job performance to ensure efficient resource utilization.
- Use `nvidia-smi` to check GPU utilization.
- Only request GPU nodes if the job can effectively use them.

## Status
- The ticket was closed as the user acknowledged the issue and started investigating the root cause.
```
---

### 2023101242002148_Jobs%20on%20TinyGPU%20only%20use%20one%20of%20the%20two%20allocated%20GPUs%20%5Biwfa027h%5D.md
# Ticket 2023101242002148

 # HPC Support Ticket: Jobs on TinyGPU Only Use One of the Two Allocated GPUs

## Keywords
- TinyGPU
- GPU utilization
- Job allocation
- Monitoring system
- ClusterCockpit
- `nvidia-smi`
- `srun`

## Problem
- User's jobs on TinyGPU (JobIDs 660713, 660657, 660692) are only utilizing one of the two allocated GPUs.
- Resources are being underutilized, leading to idle GPUs that could be used by other jobs.

## Root Cause
- The user's code is not configured to utilize multiple GPUs effectively.

## Solution
- **User Action**: The user needs to modify their code to ensure it can utilize both allocated GPUs.
- **Monitoring**: HPC Admins provided a screenshot from the monitoring system and instructions on how to check GPU utilization using ClusterCockpit and `nvidia-smi`.
- **Resource Allocation**: Users should only allocate GPU nodes if their code can effectively use the GPUs to avoid resource wastage.

## Steps to Monitor GPU Utilization
1. **ClusterCockpit**: Log into the monitoring system at [ClusterCockpit](https://monitoring.nhr.fau.de/).
2. **Attach to Running Job**: Use the command `srun --pty --overlap --jobid YOUR-JOBID bash` to get a shell on the first node of the job.
3. **Check GPU Utilization**: Run `nvidia-smi` to see the current GPU utilization.

## Additional Information
- **Contact**: If further assistance is needed, users can contact HPC support.
- **Resource Efficiency**: Ensure efficient use of allocated resources to maximize system performance and availability for all users.

---

This documentation aims to help support employees identify and resolve similar issues related to GPU utilization in the future.
---

### 2023022842003249_XXL-CT%20instance%20segmentation%20on%20Alex%20Cluster.md
# Ticket 2023022842003249

 # HPC Support Ticket: XXL-CT Instance Segmentation on Alex Cluster

## Keywords
- PhD Student
- Visual Computing
- Fraunhofer IIS
- Instance Segmentation
- X-ray 3D Voxel Data
- Deep Learning
- Alex GPU Cluster
- NHR Application
- HPC Account
- TinyGPU Cluster
- Audiolabs

## Summary
An external PhD student from the Chair of Visual Computing at FAU, working via Fraunhofer IIS, inquires about accessing the Alex GPU cluster for instance segmentation of large X-ray 3D voxel data sets using deep learning.

## Root Cause
- User requires significant computational resources for deep learning tasks on large datasets.
- User is unsure about the procedure, costs, and lead times for accessing the Alex GPU cluster.

## Solution
- **NHR Application**: Submit an application via Prof. Stamminger.
  - [NHR Application Rules](https://hpc.fau.de/systems-services/documentation-instructions/nhr-application-rules/)
- **HPC Account Application**: Submit an application via LGDV/Prof. Stamminger.
  - [HPC Account Application Form](https://www.rrze.fau.de/files/2017/06/HPC-Antrag.pdf)
- **Access to Alex Cluster**: Request access separately after obtaining an HPC account.
  - [Tier3 Access to Alex](https://hpc.fau.de/tier3-access-to-alex/)
- **Alternative GPU Nodes**: Contact Stefan Turowski from Audiolabs for access to GPU nodes.

## General Learnings
- Basic usage of HPC systems is typically free for FAU researchers for publicly funded research.
- Access to specific clusters like Alex requires separate requests.
- Collaboration with other departments (e.g., Audiolabs) can provide additional computational resources.

## Next Steps
- User should follow the provided links to submit the necessary applications.
- User may also consider contacting Stefan Turowski for alternative GPU resources.
---

### 2024061442000689_Low%20GPU%20utilization%20for%20project%20b206dc%20%28Real-Time%20Speech%20Dereverberation%29.md
# Ticket 2024061442000689

 # Low GPU Utilization for AI/ML Application

## Keywords
- Low GPU utilization
- AI/ML application
- Resource optimization
- Training data access
- `nvidia-smi`
- `srun`
- ClusterCockpit

## Problem Description
- User's jobs on the HPC cluster showed very low GPU utilization.
- The issue persisted across multiple jobs over time.

## Communication Summary
- **HPC Admin** notified the user about the low GPU utilization and provided methods to check it (ClusterCockpit, `nvidia-smi` via `srun`).
- **HPC Admin** suggested optimizing the application, particularly focusing on training data access.
- After a follow-up, the user acknowledged the issue and committed to investigating and fixing it.

## Root Cause
- The root cause of the low GPU utilization was not explicitly identified in the conversation.

## Solution
- The user was advised to optimize their application, with a focus on improving access to training data.
- The user agreed to investigate and fix the issue.

## Outcome
- The ticket was closed as most jobs since July 1st showed some GPU utilization, although not optimal.

## General Learnings
- Regularly monitor GPU utilization for AI/ML jobs.
- Use tools like ClusterCockpit and `nvidia-smi` to check GPU usage.
- Optimizing training data access can improve GPU utilization in AI/ML applications.
- Proactive communication with users can help in resolving resource utilization issues.
---

### 2021112742000356_Early-Alex%20%22Stefan%20Hiemer%22%20_%20iww8014h.md
# Ticket 2021112742000356

 ```markdown
# HPC Support Ticket Conversation Analysis

## Keywords
- HPC Support
- Early-Alex
- Stefan Hiemer
- LAMMPS
- Pytorch
- Tensorflow
- Slurm
- GPU
- Python
- Virtual Environment
- Dependency Conflicts

## General Learnings
- **User Onboarding**: HPC Admin provides access and documentation links for new users.
- **Software Availability**: Specific versions of LAMMPS, Pytorch, and Tensorflow are available.
- **Slurm Configuration**: Users need guidance on Slurm script configuration, especially for GPU allocation.
- **Python Environment**: Users prefer virtual environments over Anaconda due to fewer dependency conflicts.

## Specific Issues and Solutions

### Issue 1: Slurm GPU Allocation
- **Problem**: User unsure where to include `--gres=gpu:` in Slurm script.
- **Solution**: HPC Admin provided updated Slurm documentation with examples.
  ```bash
  #SBATCH --gres=gpu:a40:1
  ```

### Issue 2: Sharing Job Scripts
- **Problem**: User wants to share Slurm/Job scripts for LAMMPS and Tensorflow.
- **Solution**: HPC Admin suggested sending the scripts to be included in the documentation.

### Issue 3: LAMMPS Library Error
- **Problem**: LAMMPS error due to missing `libcuda.so.1`.
- **Solution**: Ensure the correct modules are loaded. The error should only occur on login nodes, not compute nodes.
  ```bash
  module load lammps/20211027-gcc10.3.0-openmpi-mkl-cuda
  ```

### Issue 4: Python Environment Preference
- **Problem**: User prefers virtual environments over Anaconda.
- **Solution**: HPC Admin confirmed that virtual environments can be used, with the recommendation to install packages in user directories.
  ```bash
  module help python
  ```

## Documentation Updates
- **LAMMPS Executable**: Documentation updated to mention that the LAMMPS binary is called `lmp`.
- **Python Environment**: Documentation includes examples for direct pip installation.

## Conclusion
- **User Support**: HPC Admin provided detailed support for initial setup and troubleshooting.
- **Documentation**: Continuous updates to documentation to address user queries and issues.
- **Flexibility**: HPC environment supports various Python setups, including virtual environments.
```
---

### 2022101242002864_GPGPU%20node%20specification%20Alex.md
# Ticket 2022101242002864

 # HPC Support Ticket: GPGPU Node Specification

## Keywords
- GPGPU nodes
- A100 nodes
- BATCH script
- GPU memory specification
- Benchmark consistency

## Problem
The user wants to specify the type of A100 nodes (40GB or 80GB) in their BATCH script to ensure consistent benchmarking and rule out performance variations due to different GPU memory sizes.

## Solution
Use the constraint flag `-C` in the `srun` command to specify the type of A100 node:
- `a100_40` for 40GB GPU
- `a100_80` for 80GB GPU

Example command:
```bash
srun --gres=gpu:a100:1 -p a100 -C a100_40
```

## General Learnings
- Users can specify GPU memory size in their job scripts to ensure consistent hardware usage.
- The `-C` flag in `srun` can be used to set constraints on the job, such as the type of GPU.
- Properly specifying hardware in job scripts can help in achieving reproducible benchmark results.
---

### 2023032242001349_Job%20on%20Alex%20does%20not%20use%20GPU%20%5Bb143dc20%5D.md
# Ticket 2023032242001349

 # HPC Support Ticket: Job on Alex does not use GPU

## Keywords
- GPU utilization
- Job allocation
- Resource management
- `nvidia-smi`
- `srun`

## Problem
- User's job on Alex (JobID 701796) allocated 8 GPUs but did not utilize them.
- GPUs remained idle, preventing other users from accessing these resources.

## Root Cause
- The user's code did not make use of the allocated GPUs.

## Solution
- **Monitoring**: HPC Admins used monitoring tools to identify underutilized resources.
- **User Instructions**:
  - Attach to the running job using `srun --pty --jobid bash`.
  - Check GPU utilization with `nvidia-smi`.
- **Resource Allocation**: Ensure that jobs only allocate GPUs if the code can utilize them.

## General Learnings
- Regularly monitor job resource utilization.
- Educate users on proper resource allocation to avoid idle resources.
- Provide tools and commands for users to check resource usage (e.g., `nvidia-smi` for GPUs).

## Follow-up
- The ticket was closed due to no response from the user.

## Related Teams
- HPC Admins
- 2nd Level Support Team
- Datacenter Head
- Training and Support Group Leader
- NHR Rechenzeit Support
- Software and Tools Developers
---

### 2024061842001402_Tier3-Access-Alex%20%22Manuel%20Saigger%22%20_%20gwgk007h.md
# Ticket 2024061842001402

 ```markdown
# HPC Support Ticket Analysis: Tier3-Access-Alex

## Keywords
- Tier3 Access
- Alex Cluster
- GPGPU
- Nvidia A40
- Python
- Deep Learning
- Atmospheric Flow Simulations

## Summary
- **User Request**: Access to the GPGPU cluster 'Alex' for deep learning development.
- **Resources Requested**: 10,000 GPU-hours.
- **Software Needed**: Python.
- **Application**: Developing a deep-learning architecture for atmospheric flow simulations.
- **Expected Outcome**: Downscaling tool for atmospheric flow fields.

## Actions Taken
- **HPC Admin**: Granted access to the user's account on the Alex cluster.

## Lessons Learned
- **Access Granting**: HPC Admins can enable access to specific clusters upon user request.
- **Resource Allocation**: Users can request specific resources like GPU-hours for their projects.
- **Software Requirements**: Users should specify the software they need for their projects.

## Root Cause of the Problem
- User needed access to the Alex cluster for their deep learning project.

## Solution
- HPC Admin granted access to the user's account on the Alex cluster.
```
---

### 2025010942001927_Job%20on%20Alex%20is%20only%20using%201%20of%204%20GPU%20%5Bg101ea13%5D.md
# Ticket 2025010942001927

 # HPC Support Ticket: Job on Alex is only using 1 of 4 GPU

## Keywords
- GPU utilization
- Interactive job
- Non-interactive job
- PyTorch Lightning
- DDP
- `nvidia-smi`
- `srun`
- `sbatch`
- `salloc`

## Problem Description
- User's job on Alex was only using 1 out of 4 allocated GPUs.
- The issue occurred only in non-interactive jobs, while interactive jobs utilized all allocated GPUs.
- The user used DDP with PyTorch Lightning for the experiment.

## Root Cause
- Misconfiguration in the job script for non-interactive jobs.

## Troubleshooting Steps
1. **Monitoring GPU Utilization**:
   - HPC Admin provided a screenshot from the monitoring system showing GPU utilization.
   - User was advised to use `nvidia-smi` to check GPU utilization by attaching to the running job with `srun --pty --overlap --jobid YOUR-JOBID bash`.

2. **Comparing Job Start Commands**:
   - Interactive job command:
     ```bash
     salloc --gres=gpu:a40:2 --time=0:15:0
     module load python
     conda activate gen-nerf-cuda118
     python src/train_debug.sh logger=wandb_local experiment=seqs_living10_v1_cluster_debug
     ```
   - Non-interactive job command:
     ```bash
     sbatch job_scripts/train_debug.sh logger=wandb_local experiment=seqs_living10_v1_cluster_debug
     ```

## Solution
- The user adapted the example from the documentation provided by the HPC Admin: [PyTorch Documentation](https://doc.nhr.fau.de/apps/pytorch).
- This resolved the issue, allowing the non-interactive job to utilize all allocated GPUs.

## Conclusion
- Ensure job scripts for non-interactive jobs are correctly configured to utilize all allocated GPUs.
- Refer to the official documentation for examples and best practices.

## Additional Resources
- [ClusterCockpit Monitoring System](https://monitoring.nhr.fau.de/)
- [PyTorch Documentation](https://doc.nhr.fau.de/apps/pytorch)
- [HPC FAU Website](https://hpc.fau.de/)
---

### 2021063042001484_How%20to%20get%20a%20specific%20Cuda%20machine.md
# Ticket 2021063042001484

 # HPC Support Ticket: Accessing Specific CUDA Machines

## Keywords
- CUDA
- Specific host allocation
- Memory requirements
- `salloc` command
- GPU allocation

## Problem
- User requires access to specific hosts (tg071-tg074) with 32 GB memory for deep learning tasks.
- Current allocation using `salloc` command results in a host with insufficient memory (10 GB).

## Root Cause
- The user's deep learning model requires more memory than the allocated host provides.
- The user cannot modify the software to reduce computational requirements without compromising model efficiency.

## Solution
- The user needs guidance on how to request specific hosts with sufficient memory using the `salloc` command or an alternative method.

## Learning Points
- Understanding how to allocate specific hosts with required resources.
- Importance of memory requirements for deep learning tasks.
- Potential limitations of the `salloc` command in specifying host preferences.

## Next Steps
- HPC Admins should provide instructions on how to request specific hosts with the required memory.
- Consider updating documentation to include information on specifying host preferences in job submissions.
---

### 2022060242003023_Tier3-Access-Alex%20%22Jonas%20Glombitza%22%20_%20mppi118h.md
# Ticket 2022060242003023

 # HPC Support Ticket Analysis

## Keywords
- Account activation
- Alex cluster
- Python applications
- TensorFlow/Keras
- h5py (including BLOSC compression)
- Numba
- SciPy
- NumPy/Matplotlib
- GPGPU cluster
- Nvidia A100/A40 GPUs
- ML pipeline
- IACT images
- DFG/BMBF projects

## Summary
- **User Request:** Access to the Alex cluster for training neural networks using TensorFlow/Keras.
- **Required Software:** TensorFlow/Keras, h5py (including BLOSC compression), Numba, SciPy, NumPy/Matplotlib.
- **Application Details:** Testing and setting up an ML pipeline for IACT image reconstruction.
- **Expected Outcome:** Development of a high-performance ML pipeline for IACT data analysis.

## Root Cause of the Problem
- User's account was not yet activated on the Alex cluster.
- User required specific software and documentation for Python applications.

## Solution
- **Account Activation:** HPC Admin activated the user's account on the Alex cluster.
- **Documentation Provided:** HPC Admin provided links to relevant documentation for Python applications and TensorFlow/PyTorch.

## General Learnings
- Ensure user accounts are activated promptly.
- Provide comprehensive documentation for software and applications.
- Be prepared to assist with specific software requirements such as h5py with BLOSC compression.

## References
- [Alex Cluster Documentation](https://hpc.fau.de/systems-services/systems-documentation-instructions/clusters/alex-cluster/)
- [Python and Jupyter Documentation](https://hpc.fau.de/systems-services/systems-documentation-instructions/special-applications-and-tips-tricks/python-and-jupyter/)
- [TensorFlow/PyTorch Documentation](https://hpc.fau.de/systems-services/systems-documentation-instructions/special-applications-and-tips-tricks/tensorflow-pytorch/)
---

### 2021111842004244_Early-Alex%20%22Timo%20Eckstein%22%20_%20mpt2007h.md
# Ticket 2021111842004244

 ```markdown
# HPC Support Ticket Conversation Analysis

## Keywords
- GPGPU cluster 'Alex'
- Nvidia A100 GPGPUs
- Nvidia A40 GPGPUs
- Cirq
- Qsim
- NVIDIA cuQuantum SDK
- Quantum Fourier Transform
- GPU hours
- Software versions

## Summary
- **User Request**: Access to GPGPU cluster 'Alex' with Nvidia A100 and A40 GPUs for quantum circuit simulations.
- **Required Software**: Cirq, Qsim, NVIDIA cuQuantum SDK.
- **Expected Outcome**: Verify Quantum Fourier Transform benchmark results and accelerate quantum circuit simulations.

## Issues and Solutions
- **Issue**: Initial provision of special software not possible.
  - **Solution**: User can install parts of the software themselves or wait for regular operation.
- **Issue**: Need for specific software versions.
  - **Solution**: User provided the latest versions required:
    - Qsim 0.11.1
    - Cirq 0.13.1
    - cuQuantum SDK 0.0.1

## Root Cause of Problems
- **Initial Software Provision**: HPC Admin unable to provide special software initially.
- **Software Versions**: User needed the latest versions to ensure compatibility and functionality.

## General Learnings
- **User Involvement**: Users may need to install or configure parts of the software themselves.
- **Software Versions**: Importance of using the latest software versions for compatibility with new features.
- **Communication**: Clear communication between users and HPC Admins regarding software requirements and versions.

## Next Steps
- **Follow-up**: Ensure the user's request and contact information are up-to-date.
- **Support**: Continue to provide support for users in the quantum physics field.
```
---

### 2021071642002311_Gaze_Net%20on%20tg08x%20-%20iwi5026h.md
# Ticket 2021071642002311

 # HPC-Support Ticket Conversation: Gaze_Net on tg08x

## Keywords
- Gaze_Net
- GPU utilization
- nvidia-smi
- preemption
- tmux
- Torque
- Slurm
- RTX3080
- A100

## Summary
- User had multiple Gaze_Net jobs running on tg08x, requesting 2 GPUs but only utilizing one.
- Jobs were canceled due to preemption by work groups that financed the nodes.
- User inquired about running multiple jobs on a single GPU and monitoring GPU usage.

## Root Cause
- Inefficient GPU utilization: jobs requested 2 GPUs but only used one.
- Preemption: jobs were canceled due to resource claims by financing work groups.

## Solutions
- **GPU Utilization**: User was advised to request only one GPU for their jobs.
- **Preemption**: HPC Admin explained the preemption policy and provided a link to the HPC Cafe discussion.
- **Monitoring GPU Usage**:
  - User can SSH to the node where the job is running.
  - Use `squeue` (Slurm) or `qstat -n` (Torque) to find the node.
  - `nvidia-smi` should deliver output for the attached job.
  - `tmux` can be used for interactive monitoring, but the user reported permission issues.
- **Running Multiple Jobs on a Single GPU**:
  - Technically possible, but efficiency may be limited due to hardware task scheduling.
  - HPC Admin provided a sample script to run multiple jobs concurrently.

## Additional Notes
- User was advised to consider the efficiency of running multiple jobs concurrently on a single GPU.
- The use of `tmux` for interactive monitoring was discussed, but the user reported permission issues.
- The conversation included details about switching between Slurm and Torque for job management.

## Follow-up
- User should test running multiple jobs on a single GPU and monitor efficiency.
- If `tmux` permission issues persist, the user should contact HPC support for further assistance.
---

### 2025021842000454_Job%20on%20Alex%20is%20only%20using%201%20of%204%20GPU%20%5Bb193dc11%5D.md
# Ticket 2025021842000454

 # HPC Support Ticket: Job on Alex is only using 1 of 4 GPU

## Keywords
- GPU utilization
- Job allocation
- Monitoring system
- ClusterCockpit
- `nvidia-smi`
- Resource management

## Problem Description
- User's job on Alex (JobID 2393263) was only utilizing 1 out of 4 allocated GPUs.

## Root Cause
- The job was not configured to utilize all allocated GPUs effectively.

## Solution
- **Monitoring**: HPC Admin provided a screenshot from the monitoring system (ClusterCockpit) showing the underutilization.
- **User Action**: User was advised to log into ClusterCockpit to view GPU utilization.
- **Command**: User was instructed to use `srun --pty --overlap --jobid YOUR-JOBID bash` to attach to the running job and run `nvidia-smi` to check GPU utilization.
- **Resource Management**: User was advised to ensure that nodes with GPUs are only allocated if the code can effectively use them.

## General Learnings
- Always verify GPU utilization for jobs that request GPU resources.
- Use monitoring tools like ClusterCockpit to check resource usage.
- Attach to running jobs using `srun` and check GPU utilization with `nvidia-smi`.
- Ensure efficient resource allocation to avoid idle resources.

## Ticket Closure
- The ticket was closed as the job's GPU utilization improved.

## Contact Information
- For further assistance, contact the HPC support team at `support-hpc@fau.de`.
---

### 2024111842002731_Jobs%20on%20Alex%20do%20not%20use%20all%20allocated%20GPUs%20-%20b238dc11.md
# Ticket 2024111842002731

 # HPC Support Ticket: Jobs on Alex do not use all allocated GPUs

## Keywords
- GPU utilization
- Job monitoring
- ClusterCockpit
- `nvidia-smi`
- Resource allocation

## Issue
- User's job on Alex (JobID 2165837) did not utilize any of the 2 allocated GPUs.

## Root Cause
- The user mentioned using conditional GPU usage but forgot to enable it.

## Solution
- The user was advised to check GPU utilization using ClusterCockpit or by attaching to the running job with `srun` and using `nvidia-smi`.
- The user agreed to enable GPU usage and rerun the job to utilize all requested resources.

## General Learnings
- Always ensure that jobs are configured to use allocated resources to avoid idle GPUs.
- Use monitoring tools like ClusterCockpit to check resource utilization.
- Attach to running jobs using `srun` and `nvidia-smi` to verify GPU usage.

## Relevant Links
- [ClusterCockpit Monitoring](https://monitoring.nhr.fau.de/)
- [Job Monitoring with ClusterCockpit Documentation](https://doc.nhr.fau.de/job-monitoring-with-clustercockpit/)

## Contact
- For further assistance, contact HPC Support at [support-hpc@fau.de](mailto:support-hpc@fau.de).
---

### 2021110142000967_Reg%3A%20Access%20to%20HPC.md
# Ticket 2021110142000967

 # HPC Support Ticket Conversation Analysis

## Keywords
- HPC access
- GPU cluster
- FAU
- Dataset download
- Storage space
- HPC account
- Frontend login
- wget/curl/rsync

## Problem
- User unable to find the procedure to access FAU GPUs for research.
- User needs to download a massive dataset (408GB) but lacks storage space.

## Solution
- **Accessing HPC:**
  - User should fill out the form at [HPC-Antrag.pdf](https://www.rrze.fau.de/files/2017/06/HPC-Antrag.pdf) and send it to the HPC support.
  - Documentation for the GPU cluster can be found at:
    - [tinygpu-cluster](https://hpc.fau.de/systems-services/systems-documentation-instructions/clusters/tinygpu-cluster/)
    - [batch-processing](https://hpc.fau.de/systems-services/systems-documentation-instructions/batch-processing/)
  - Introduction sessions are available for in-person questions.

- **Downloading Dataset:**
  - User can log in to one of the frontends with an active HPC account.
  - Use tools like `wget`, `curl`, or `rsync` to download the dataset directly onto the HPC file system.
  - HPC support can assist in selecting the appropriate file system for the use case.

## General Learnings
- Always check the HPC website for the latest forms and documentation.
- For large datasets, utilize the HPC file system for storage and downloading.
- Regular introduction sessions are available for additional support and questions.

## Root Cause
- User confusion due to outdated or missing information on the HPC website.
- Lack of storage space for downloading large datasets.

## Resolution
- Provided links to the current form and documentation.
- Advised on using HPC resources for downloading and storing large datasets.
---

### 2024031942004001_Tier3-Access-Alex%20%22Seyed%20Mohammad%20Amin%20Heydarshahi%22%20_%20iwi9116h.md
# Ticket 2024031942004001

 # HPC Support Ticket: Tier3-Access-Alex

## Keywords
- Account activation
- Alex cluster
- Nvidia A100, A40 GPGPUs
- Python, Cuda, Conda
- Deep neural networks
- Arctic dataset

## Summary
- **User Request**: Access to Alex cluster for training deep neural networks on Arctic dataset.
- **Resources Requested**: 4000 GPU-hours over 4 months.
- **Software Needed**: Python, Cuda, Conda.

## Conversation Highlights
- **HPC Admin**: Informed the user that their account has been enabled on Alex.
- **User**: Requested access to Alex cluster for training deep neural networks, specifying the required resources and software.

## Lessons Learned
- **Account Activation**: HPC Admins can enable user accounts on specific clusters.
- **Resource Allocation**: Users can request specific GPU resources and software for their projects.
- **Project Details**: Important to document the purpose and expected outcomes of the project for future reference.

## Root Cause & Solution
- **Root Cause**: User needed access to Alex cluster for their project.
- **Solution**: HPC Admin enabled the user's account on Alex.

## Notes
- Ensure proper documentation of user requests and admin responses for future reference.
- Verify that the requested resources and software are available and properly configured on the cluster.
---

### 2018080242001306_Can%20i%20run%20multiprocessing%20on%20tinygpu%3F.md
# Ticket 2018080242001306

 # HPC Support Ticket: Multiprocessing on tinygpu

## Keywords
- Multiprocessing
- Python
- GPU
- Memory Allocation
- Parallel Processing
- OSError

## Problem Description
- User attempted to implement parallel preprocessing using Python's `multiprocessing` module to feed data to GPUs.
- Encountered `OSError: [Errno 12] Cannot allocate memory` when trying to run the script.
- Suspected that there might not be enough CPUs available on `tinygpus`.

## Root Cause
- The error `OSError: [Errno 12] Cannot allocate memory` indicates a memory allocation issue, likely due to insufficient system resources (memory) rather than CPU availability.

## Solution
- The user realized the issue and understood the problem without further assistance.
- No specific solution was provided by the HPC Admins, but the user's understanding suggests that adjusting the number of parallel processes or optimizing memory usage might resolve the issue.

## General Learnings
- Memory allocation errors can occur when attempting to run multiple parallel processes.
- It's important to ensure that the system has sufficient resources (memory and CPU) to handle the desired level of parallelism.
- Understanding the error messages and their implications can help in diagnosing and resolving issues related to resource limitations.

## Next Steps
- If similar issues arise, consider advising users to:
  - Monitor system resource usage.
  - Adjust the number of parallel processes.
  - Optimize memory usage in their scripts.
  - Consult with HPC Admins for resource allocation and optimization strategies.

---

This documentation can serve as a reference for support employees to address similar issues in the future.
---

### 2024051542000911_Tier3-Access-Alex%20%22Venkata%20Naga%20Satya%20Sai%20Ravi%20Kiran%20Ayyala%20Somayajula%22%20_%20iw.md
# Ticket 2024051542000911

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Keywords
- Account Enablement
- Alex Cluster
- Nvidia A100 GPGPUs
- Nvidia A40 GPGPUs
- WALBERLA
- Exastencils
- Performance Analysis
- Roofline Modeling

## Summary
- **User Request**: Access to the Alex cluster for performance runs using WALBERLA and Exastencils.
- **HPC Admin Response**: Account enabled on Alex.

## Key Learnings
- **Account Enablement**: HPC Admins can enable user accounts on specific clusters.
- **Cluster Specifications**: Alex cluster includes Nvidia A100 and A40 GPGPUs.
- **Software Requirements**: Users may need specific software like WALBERLA and Exastencils for their applications.
- **Performance Analysis**: Users may request access for performance runs and roofline modeling.

## Root Cause of the Problem
- User needed access to the Alex cluster for performance analysis.

## Solution
- HPC Admin enabled the user's account on the Alex cluster.
```
---

### 2021101342003952_About%20jobs%20in%20TinyGPU%20today.md
# Ticket 2021101342003952

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject: About jobs in TinyGPU today

### Keywords:
- Job scheduling
- TinyGPU nodes
- Maintenance
- PENDING status
- ReqNodeNotAvail

### Summary:
A user submitted jobs to TinyGPU nodes (a100/rtyx3080) which remained in PENDING status with the message "ReqNodeNotAvail, Reserved for maintenance." The user expected the nodes to be unavailable the next day but encountered issues on the current day.

### Root Cause:
- TinyGPU nodes were reserved for maintenance earlier than expected, causing job scheduling issues.

### Solution:
- No explicit solution provided in the conversation.
- Users should be informed about maintenance schedules and potential impacts on job scheduling.

### Lessons Learned:
- Maintenance schedules should be clearly communicated to users.
- Users should check node availability and maintenance schedules before submitting jobs.
- HPC Admins should ensure that maintenance notifications are accurate and timely.

### Next Steps:
- HPC Admins should review and update maintenance communication protocols.
- Users should be advised to monitor job statuses and check for maintenance notices.
```
---

### 42134713_amber12%20on%20GPU.md
# Ticket 42134713

 # HPC-Support Ticket Conversation: Amber12 on GPU

## Keywords
- Amber12
- GPU
- PMEMD
- CUDA
- Benchmarking
- Performance
- Steered Molecular Dynamics
- nmropt=1

## Summary
A user requested the installation of Amber12, specifically the GPU version, to run demanding simulations. The HPC Admin provided a module for Amber12 with GPU support and conducted benchmarking on different hardware configurations. The user's simulations required the `nmropt=1` feature, which was not fully optimized for GPU, leading to performance issues.

## Root Cause
- The user needed to run steered molecular dynamics simulations with `nmropt=1`, which lacked a CUDA kernel, causing additional synchronizations between GPU and CPU and impacting performance.

## Solution
- The HPC Admin suggested running the simulations on CPU-only nodes (TinyBlue) using 8-10 nodes (64-80 CPUs) for better performance and stability.
- The user agreed to use the CPU-only version for critical simulations and the GPU version for less demanding tasks.

## What Can Be Learned
- Always check the release notes and documentation for any performance caveats or missing features in GPU implementations.
- Benchmarking on different hardware configurations can help users make informed decisions about resource allocation.
- Communication between users and HPC Admins is crucial for optimizing job submissions and resource usage.
- Sometimes, GPU implementations may not be the best choice for specific simulations due to missing optimizations or features.
---

### 2024101542002293_GPUs%20allocated%20but%20not%20utilized%20-%20b171dc16.md
# Ticket 2024101542002293

 # HPC Support Ticket: GPUs Allocated but Not Utilized

## Keywords
- GPU utilization
- GROMACS
- SLURM
- `nvidia-smi`
- ClusterCockpit
- Job monitoring
- Resource allocation

## Summary
The user's jobs were allocating GPUs but not utilizing them. The HPC Admins provided guidance on monitoring GPU usage and requested the user to upload specific simulation files for further investigation.

## Problem
- User's jobs (JobID 2100017, 2099422, 2099421, 2099420, and 2099348) were not utilizing the allocated GPUs.
- The `cscl_milling` simulation had issues with equilibration and stopped at step 10000 with the message "One or more atoms moved too far between two domain decomposition steps."

## Investigation
- HPC Admins suggested using ClusterCockpit or `nvidia-smi` to monitor GPU utilization.
- The user's submit script was reviewed and found to be correct.
- Benchmarks were run to understand the issue, but the results were inconsistent.
- The `cscl_milling` simulation was identified as problematic and required better equilibration.

## Solution
- The user was advised to improve the equilibration of the `cscl_milling` simulation.
- Non-physical initial temperatures and time steps were discussed, and the user was asked to provide references for these settings.
- The user was reminded to only allocate GPU resources if their code can utilize them to avoid resource wastage.

## Follow-up
- The user uploaded the requested simulation files for further investigation by the HPC Admins.
- The user acknowledged the issue with the `cscl_milling` simulation and is working to resolve it.

## Conclusion
The root cause of the problem was identified as an issue with the `cscl_milling` simulation's equilibration. The user was advised to improve the simulation settings and only allocate GPU resources when necessary. The HPC Admins provided guidance on monitoring GPU usage and offered to run benchmarks to help diagnose the issue.
---

### 2022112342005375_A100%20GPUs%20mit%2080%20GB%20in%20Alex%20-%20FAU-Onboarding.md
# Ticket 2022112342005375

 # HPC Support Ticket: A100 GPUs with 80 GB in Alex - FAU-Onboarding

## Keywords
- A100 GPUs
- 80 GB
- FAU-Onboarding
- sbatch
- `-C a100_80` option

## Problem
User needed to specify A100 GPUs with 80 GB memory for their jobs.

## Solution
HPC Admin advised the user to use the `-C a100_80` option with the `sbatch` command to enforce the use of A100 GPUs with 80 GB memory.

## General Learning
- The `-C` option in `sbatch` can be used to specify constraints such as GPU type and memory.
- Proper communication during onboarding sessions can help users understand and utilize HPC resources effectively.

## Example
```bash
sbatch -C a100_80 your_job_script.sh
```

## Additional Notes
- Ensure users are aware of the available GPU types and their specifications.
- Provide clear documentation and examples for using `sbatch` options.
---

### 2024111842002517_Tier3-Access-Alex%20%22Jonathan%20Endres%22%20_%20mfdk107h.md
# Ticket 2024111842002517

 # HPC Support Ticket Analysis: Tier3-Access-Alex

## Keywords
- Tier3 Account
- JupyterHub
- Alex Cluster
- GTX1080(Ti) GPUs
- Slurm Jobs
- Multi-GPU
- NHR Project

## Summary
- **User Request**: Access to Alex cluster with Nvidia A40 GPUs via JupyterHub for MRI research and simulations.
- **Issue**: Tier3 accounts via JupyterHub can only access GTX1080(Ti) GPUs, not Nvidia A40 GPUs.
- **Solution**: Use Slurm jobs instead of JupyterHub for better GPU access and multi-GPU support.

## Detailed Analysis
- **Root Cause**: Incompatibility between Tier3 accounts, JupyterHub, and the Alex cluster for accessing Nvidia A40 GPUs.
- **Solution**: Recommend using Slurm jobs for better GPU access and multi-GPU support.
- **Outcome**: Ticket closed due to no response from the user.

## Lessons Learned
- Tier3 accounts via JupyterHub are limited to GTX1080(Ti) GPUs.
- Slurm jobs offer better GPU access and multi-GPU support compared to JupyterHub.
- Ensure users are aware of the limitations of JupyterHub for specific GPU access.

## Recommendations
- Inform users about the limitations of JupyterHub for specific GPU access.
- Encourage the use of Slurm jobs for better GPU access and multi-GPU support.
- Provide clear documentation on the differences between JupyterHub and Slurm jobs for GPU access.
---

### 2023011342001673_Alex%20A100%2080Gpu%20Flag.md
# Ticket 2023011342001673

 ```markdown
# HPC Support Ticket: Alex A100 80GB GPU Flag

## Keywords
- A100 80GB GPU
- Slurm Option
- Alex Cluster
- Job Submission

## Problem
- User wants to maximize job efficiency by using only 80GB GPUs.
- Current workaround involves requesting jobs on specific nodes.

## Root Cause
- User needs a specific flag to request 80GB GPUs for job submission.

## Solution
- Use the Slurm option `-C a100_80` when submitting jobs to ensure they run on nodes with 80GB GPUs.

## What Can Be Learned
- Specific Slurm options can be used to target hardware with desired specifications.
- Proper use of Slurm options can optimize job efficiency and resource allocation.
```
---

### 42373604_Tinyblue.md
# Ticket 42373604

 ```markdown
# HPC Support Ticket: Tinyblue Node Issues

## Keywords
- Tinyblue
- Node issues
- MPI errors
- InfiniBand switches
- Power cycling

## Summary
A user reported issues with specific nodes (63, 64, 67, 68) on Tinyblue, causing MPI errors and preventing jobs from starting.

## Root Cause
- Specific nodes (63, 64, 67, 68) were causing MPI errors.
- InfiniBand (IB) switches were experiencing errors.

## Solution
- HPC Admins power cycled all IB switches in TinyBlue on 18.06.
- After power cycling, the flood of error messages stopped, indicating the problem was resolved.

## Lessons Learned
- Node-specific issues can cause MPI errors and prevent job execution.
- Power cycling IB switches can resolve connectivity and error issues.
- Monitoring error logs (e.g., `ibqueryerrors`) is crucial for identifying and resolving issues.

## Next Steps
- If similar issues arise, check for node-specific errors and consider power cycling the IB switches.
- Continue monitoring error logs for any recurring issues.
```
---

### 2021080342003565_inefficient%20jobs%20on%20TinyGPU%20-%20iwso034h.md
# Ticket 2021080342003565

 # Inefficient Jobs on TinyGPU

## Keywords
- Inefficient GPU usage
- `nvidia-smi`
- Multi-GPU jobs
- Administrative hold
- Job monitoring

## Problem Description
- User's jobs request multiple GPUs but utilize only the first one.
- Jobs were placed in administrative hold and later deleted due to inefficient resource usage.

## Root Cause
- The jobs were configured to request multiple GPUs but the application logic did not distribute the workload across all requested GPUs.

## Solution
- Users should ensure that their multi-GPU jobs are properly configured to utilize all requested GPUs.
- Users can monitor GPU usage during job execution using `nvidia-smi`.
- If only one GPU is needed, users should request only one GPU (`ppn=4`) to avoid wasting resources.

## HPC Admin Actions
- Notified the user about inefficient GPU usage.
- Provided instructions on how to monitor GPU usage with `nvidia-smi`.
- Placed inefficient jobs in administrative hold and later deleted them.

## General Learnings
- Always verify that multi-GPU jobs are efficiently using all requested GPUs.
- Use `nvidia-smi` to monitor GPU usage during job execution.
- Request only the necessary resources to avoid waste and ensure fair usage of HPC resources.

## Related Tools
- `nvidia-smi`: Command-line tool for monitoring NVIDIA GPUs.

## Contact
For further assistance, contact the HPC Support team at [support-hpc@fau.de](mailto:support-hpc@fau.de).
---

### 2023042442002048_Tier3-Access-Alex%20%22Oliver%20Watson%22%20_%20iwal113h.md
# Ticket 2023042442002048

 # HPC Support Ticket: Tier3-Access-Alex

## Keywords
- HPC Account Activation
- GPGPU Cluster 'Alex'
- Nvidia A100 GPUs
- Python
- Cuda
- Master Thesis
- Generative Neural Networks
- Speech Signal Synthesis

## Summary
- **User Request**: Access to GPGPU cluster 'Alex' with Nvidia A100 GPUs for a Master Thesis project involving speech signal synthesis using generative neural networks.
- **Required Software**: Python, Cuda.
- **Expected Outcome**: Trained model for speech signal synthesis conditioned from EGG signals.
- **Additional Notes**: User needs access to specific A100 GPUs purchased by Fraunhofer IIS.

## Actions Taken
- **HPC Admin**: Activated the user's HPC account on Alex.

## Lessons Learned
- Ensure proper account activation for users requesting access to specific HPC resources.
- Verify that the required software (Python, Cuda) is available and accessible to the user.
- Understand the user's project requirements and expected outcomes to provide tailored support.

## Root Cause
- User required access to specific HPC resources for their research project.

## Solution
- HPC Admin activated the user's account, granting them access to the necessary resources.

## Follow-up
- Ensure the user has access to the specific A100 GPUs purchased by Fraunhofer IIS.
- Verify that the user can successfully utilize the required software (Python, Cuda) for their project.
---

### 2022060142001269_Jobs%20on%20TinyGPU%20only%20use%20one%20GPU%20%5Biwb0014h%5D.md
# Ticket 2022060142001269

 # HPC Support Ticket: Jobs on TinyGPU Only Use One GPU

## Keywords
- GPU utilization
- TinyGPU
- `nvidia-smi`
- SLURM job script
- `--cpus-per-task`
- `--gres=gpu:1`

## Problem
- User's jobs on TinyGPU were only utilizing one GPU despite multiple GPUs being allocated.
- User requested guidance on appropriate CPU core allocation for CPU-intensive jobs.

## Root Cause
- The user's code was not optimized to utilize multiple GPUs effectively.
- Misunderstanding of available CPU cores per GPU on TinyGPU.

## Solution
- **Monitoring GPU Utilization:**
  - Use `ssh` to connect to the node running the job.
  - Use `nvidia-smi` to check GPU utilization.
  - Reference: [Working with NVIDIA GPUs](https://hpc.fau.de/systems-services/systems-documentation-instructions/special-applications-and-tips-tricks/working-with-nvidia-gpus/)

- **Optimizing Resource Allocation:**
  - Check TinyGPU documentation for CPU cores available per GPU.
  - Use `--gres=gpu:1` to minimize waiting time in the queue.
  - Optionally, add `#SBATCH --cpus-per-task=8` if access to `$SLURM_CPUS_PER_TASK` is needed.
  - Reference: [TinyGPU Cluster Documentation](https://hpc.fau.de/systems-services/systems-documentation-instructions/clusters/tinygpu-cluster/)

## General Learning
- Ensure that jobs requesting GPU resources are optimized to utilize all allocated GPUs.
- Understand the hardware specifications of the cluster to request appropriate resources.
- Use SLURM directives correctly to specify CPU and GPU resources.
- Monitor resource utilization to avoid wastage and ensure efficient use of HPC resources.
---

### 2023112042003701_Job%20on%20Alex%20does%20not%20use%20allocated%20GPU%20%5Bb180dc19%5D.md
# Ticket 2023112042003701

 # HPC Support Ticket: Job on Alex Does Not Use Allocated GPU

## Keywords
- GPU utilization
- Job allocation
- Monitoring system
- ClusterCockpit
- `nvidia-smi`
- Resource management

## Problem Description
- User's job on Alex (JobID 906845) is only utilizing one out of four allocated GPUs.
- The issue was identified through the monitoring system, which showed low GPU utilization.

## Root Cause
- The user's code is not effectively utilizing the allocated GPU resources.

## Solution
- **Monitoring GPU Utilization:**
  - Users can log into the monitoring system ClusterCockpit at [monitoring.nhr.fau.de](https://monitoring.nhr.fau.de/) to view GPU utilization.
  - Alternatively, users can attach to their running job using the command:
    ```bash
    srun --pty --overlap --jobid YOUR-JOBID bash
    ```
    - This provides a shell on the first node of the job, allowing the use of `nvidia-smi` to check current GPU utilization.

- **Resource Allocation:**
  - Ensure that jobs only allocate nodes with GPUs if the code can effectively utilize them.
  - Avoid idle GPU resources by properly configuring job scripts and code to make use of allocated GPUs.

## General Learnings
- Regularly monitor job performance and resource utilization.
- Use monitoring tools and commands like `nvidia-smi` to diagnose resource usage issues.
- Properly allocate and manage resources to avoid wastage and ensure efficient use of HPC resources.

## Contact Information
- For further assistance, contact the HPC Admins at [support-hpc@fau.de](mailto:support-hpc@fau.de).
- Additional resources and support can be found at [hpc.fau.de](https://hpc.fau.de/).
---

### 2025030542002895_Tier3-Access-Alex%20%22Julian%20Pollinger%22%20_%20iwi1101h.md
# Ticket 2025030542002895

 ```markdown
# HPC Support Ticket: Tier3-Access-Alex

## Keywords
- Access Request
- GPGPU Cluster 'Alex'
- Nvidia A100 GPGPUs
- GPU Hours
- Anaconda Python
- LLMs (Large Language Models)
- Resource Allocation
- sacctmgr

## Summary
- **User Request**: Access to GPGPU cluster 'Alex' for master thesis project involving large language models (LLMs).
- **Resource Needs**: Approximately 900 GPU hours over 6 months for Nvidia A100 GPUs.
- **Software Requirements**: Anaconda Python.
- **Project Details**: Developing metrics to test the correctness of LLM-assigned codes for qualitative interviews.
- **Expected Results**: Validation of metrics for reasonable assurance about the quality of code assignments.

## Actions Taken by HPC Admins
- **Access Granted**: User was granted access to the 'Alex' cluster.
- **Account Setup**: New account created for the user with `sacctmgr` command.
- **Resource Allocation**: Jobs on TinyGPU deemed appropriate, leading to resource allocation.

## Root Cause of the Problem
- User required access to more powerful GPUs (Nvidia A100) for larger LLMs that couldn't run on TinyGPU due to VRAM requirements.

## Solution
- Access to 'Alex' cluster was granted, allowing the user to utilize the necessary resources for their project.

## General Learnings
- **Access Requests**: Proper handling of access requests for specialized hardware.
- **Resource Management**: Using `sacctmgr` for account management and resource allocation.
- **User Support**: Addressing user needs for specific hardware and software requirements for research projects.
```
---

### 2024121742003392_NVIDIA%20Entitlement%20Certificate%20-%20Ref%2086818161.md
# Ticket 2024121742003392

 # HPC-Support Ticket: NVIDIA Entitlement Certificate - Ref 86818161

## Keywords
- NVIDIA Entitlement Certificate
- Software and Services Order
- PO Number
- NVIDIA Sales Order
- NVIDIA Delivery Number
- Enterprise Support

## Summary
The user received an Entitlement Certificate for a software and/or services order from NVIDIA. The email contains order information including PO Number, NVIDIA Sales Order, and NVIDIA Delivery Number. The user is instructed to register for their software and services using the attached Entitlement Certificate.

## Root Cause
No specific problem is mentioned in the provided conversation. The ticket seems to be informational, providing details about the NVIDIA order and the Entitlement Certificate.

## Solution
- **Registration**: The user needs to register for the software and services using the provided Entitlement Certificate.
- **Support**: For any questions, the user can contact NVIDIA Enterprise Support using the information provided in the link: [NVIDIA Enterprise Support](https://www.NVIDIA.com/en-us/support/enterprise/).

## General Learning
- **Order Information**: Understand the importance of order information such as PO Number, NVIDIA Sales Order, and NVIDIA Delivery Number for tracking and support purposes.
- **Entitlement Certificate**: Familiarize yourself with the process of using an Entitlement Certificate to register for software and services.
- **Support Resources**: Be aware of the support resources available from NVIDIA for enterprise customers.

## Next Steps for HPC Admins
- Ensure the user has received the Entitlement Certificate and understands the registration process.
- Provide additional support if the user encounters any issues during the registration process.
- Document the order information for future reference and support purposes.
---

### 2023072042001818_Unable%20to%20access%20a100%20gpu.md
# Ticket 2023072042001818

 # HPC Support Ticket: Unable to Access A100 GPU

## Keywords
- A100 GPU
- RTX3080
- `salloc.tinygpu`
- `--gres=gpu:a100:1`
- `--partition=a100`
- `sinfo`
- Job allocation
- CUDA out of memory error

## Problem
- User unable to access A100 GPU using `salloc.tinygpu --gres=gpu:a100:1 --time=00:30:00`.
- Job allocation revoked with error: "Requested node configuration is not available".

## Root Cause
- Missing `--partition=a100` option in the `salloc.tinygpu` command.
- All A100 nodes currently allocated to other users (`alloc` state in `sinfo` output).
- Group-specific limit on simultaneous A100 GPU usage.

## Solution
- Add `--partition=a100` option to the `salloc.tinygpu` command to request A100 GPUs.
- Check node availability using `sinfo`. If all nodes are in `alloc` state, wait for a node to become available.
- Be aware of group-specific limits on simultaneous GPU usage.

## General Learnings
- Specific GPU types may require additional options in the `salloc` command.
- The `sinfo` command provides information about node availability and allocation status.
- Group-specific limits may affect resource availability and waiting times.
- Documentation and support resources provide essential information for troubleshooting and resolving issues.

## Related Documentation
- [tinygpu Cluster Documentation](https://hpc.fau.de/systems-services/documentation-instructions/clusters/tinygpu-cluster/)
---

### 2023110942001135_Anfrage%3A%20Erh%C3%83%C2%B6hung%20der%20GPU-Node-Quota%20f%C3%83%C2%BCr%20letzte%20Phase%20meine%20.md
# Ticket 2023110942001135

 # HPC Support Ticket Analysis

## Subject
Anfrage: Erhöhung der GPU-Node-Quota für letzte Phase meine Bachelorarbeit

## Keywords
- GPU Quota
- Neural Network Training
- A100 GPUs
- Job Scheduling
- GPU Memory Usage

## Problem
- User requested an increase in GPU quota for November and December to train neural networks for their Bachelor's thesis.
- User assumed a limit of two GPU nodes and faced insufficient quota for their experiments.

## Root Cause
- Misunderstanding about the GPU quota limits.
- High demand for 80 GB A100 GPUs leading to job scheduling delays.

## Solution
- HPC Admin clarified that there is no system-side limitation on the total number of GPUs for the user's account.
- Advised the user to remove the "-C a100_80" constraint to increase the chances of jobs running, as most jobs use less than 35 GB of GPU memory.

## General Learnings
- Users may have misconceptions about quota limits.
- High-demand resources like 80 GB A100 GPUs can cause job scheduling delays.
- Removing specific resource constraints can improve job scheduling efficiency.

## Actions Taken
- HPC Admin provided clarification on quota limits.
- Advised on job scheduling optimization by removing specific GPU constraints.

## Follow-up
- User acknowledged the advice and understood the need to adjust job constraints for better scheduling.

## Recommendations
- Educate users on quota limits and job scheduling best practices.
- Monitor high-demand resources and provide alternatives or optimizations to users.
---

### 2022042742002821_Early-Alex%20%22Samuel%20Spencer%22%20_%20mppi114h.md
# Ticket 2022042742002821

 # HPC Support Ticket Analysis

## Keywords
- Alex-cluster
- A100 GPUs
- A40 GPUs
- TensorFlow
- PyTorch
- Gammapy
- Deep learning
- Gamma-ray astronomy
- Documentation
- Multiple environments

## Summary
- **User Request**: Access to Alex-cluster for deep learning in gamma-ray astronomy using TensorFlow, PyTorch, and potentially RAPIDS/CUML.
- **HPC Admin Response**: Granted access to 8 A100 and 8 A40 GPUs. Provided documentation links and noted potential compatibility issues with Gammapy.
- **User Feedback**: Acknowledged the information and planned to use multiple environments to handle compatibility issues.

## Root Cause of the Problem
- Potential compatibility issues between preinstalled TensorFlow/PyTorch modules and Gammapy.

## Solution
- Use multiple environments to design the pipeline, ensuring compatibility between different software components.
- Follow the instructions provided in the documentation for setting up TensorFlow and PyTorch.

## General Learnings
- Preinstalled modules may not always be compatible with specific user software (e.g., Gammapy).
- Users can work around compatibility issues by using multiple environments.
- Documentation and support resources are crucial for users to set up their environments correctly.

## References
- [Alex-cluster Documentation](https://hpc.fau.de/systems-services/systems-documentation-instructions/clusters/alex-cluster/)
- [TensorFlow/PyTorch Setup Instructions](https://hpc.fau.de/systems-services/systems-documentation-instructions/special-applications-and-tips-tricks/tensorflow-pytorch/)
---

### 2023042442000881_GPU%20utilization%20of%20NHR%20project%20PatRo-MRI%20%28b143dc13%29.md
# Ticket 2023042442000881

 # HPC Support Ticket: GPU Utilization Issue

## Keywords
- GPU utilization
- Job monitoring
- NHR project
- SSH keys
- Portal login

## Summary
A user was notified that their recent jobs were not fully utilizing the requested GPUs, unlike their previous jobs. The user also inquired about direct login to the monitoring site.

## Problem
- **GPU Underutilization**: Recent jobs were only using one of the two requested GPUs. Previous jobs had utilized all four requested GPUs.
- **Monitoring Site Access**: The user could only access the monitoring site via the portal and wanted to know if direct login was possible.

## Cause
- **GPU Underutilization**: Possible configuration issue in the user's job setup.
- **Monitoring Site Access**: NHR accounts do not have passwords set, only SSH keys, hence direct login is not possible.

## Solution
- **GPU Underutilization**: The user was advised to check their job configuration.
- **Monitoring Site Access**: The HPC Admin confirmed that NHR accounts can only access the monitoring site through the portal due to the lack of a password.

## General Learnings
- Always check job configurations when there is a sudden change in resource utilization.
- NHR accounts require portal access for monitoring due to the authentication method (SSH keys without passwords).

## Follow-up
- The user should update the HPC support team on the outcome of their job configuration review.
- If the issue persists, further investigation into the job scripts and configurations may be necessary.
---

### 2024041142003168_Power9%20on%20FAU%20testcluster.md
# Ticket 2024041142003168

 # HPC-Support Ticket Conversation: Power9 on FAU Testcluster

## Keywords
- Power9 processors
- Test cluster
- Binary compatibility
- Summit supercomputer

## Summary
A user inquired about the availability of a machine with Power9 processors on the FAU test cluster to ensure binary compatibility with the Power9 processors on the Summit supercomputer.

## Root Cause
The user needed a machine with Power9 processors for binary compatibility with the Summit supercomputer.

## Solution
The HPC Admin responded that the FAU test cluster does not have any IBM Power systems.

## General Learnings
- The FAU test cluster does not support IBM Power systems.
- Users seeking binary compatibility with specific hardware should verify the availability of such hardware on the test cluster.

## Recommendations
- Users should check the hardware specifications of the test cluster before planning compatibility tests.
- HPC Admins should maintain an updated list of available hardware for user reference.
---

### 2024052242002584_Alex%20jobs%20not%20using%20GPUs%20-%20b197dc12.md
# Ticket 2024052242002584

 # HPC Support Ticket: Jobs Not Using GPUs

## Keywords
- GPU utilization
- JobID
- ClusterCockpit
- `srun`
- `nvidia-smi`
- Resource allocation

## Summary
The user submitted jobs on the HPC cluster that were allocated GPU resources but did not utilize them. The HPC Admin identified the issue and provided guidance on how to monitor GPU usage.

## Root Cause
- The user submitted jobs with GPU resources but the code did not make use of the GPUs.

## Solution
- The user was advised to check GPU utilization using the ClusterCockpit monitoring system or by attaching to the running job with `srun --pty --overlap --jobid YOUR-JOBID bash` and running `nvidia-smi`.
- The user acknowledged the oversight and committed to ensuring proper resource allocation in the future.

## Lessons Learned
- Always verify that jobs requiring GPU resources actually utilize them.
- Use monitoring tools like ClusterCockpit to check resource utilization.
- Attach to running jobs using `srun` and `nvidia-smi` to monitor GPU usage.
- Ensure efficient resource allocation to avoid idle resources.

## Follow-Up
- The HPC Admin re-checked GPU utilization and closed the ticket as the current jobs appeared to be utilizing resources correctly.

## References
- ClusterCockpit: [https://monitoring.nhr.fau.de/](https://monitoring.nhr.fau.de/)
- HPC Support: [support-hpc@fau.de](mailto:support-hpc@fau.de)
- HPC Website: [https://hpc.fau.de/](https://hpc.fau.de/)
---

### 2025022442000568_GPU%20utilization%20below%203%25%20-%20b180dc31.md
# Ticket 2025022442000568

 # GPU Utilization Below 3%

## Keywords
- GPU utilization
- Job monitoring
- ClusterCockpit
- `srun`
- `nvidia-smi`

## Problem Description
- User's jobs on the HPC cluster showed GPU utilization below 3%.
- Inefficient use of GPU resources.

## Communication
- HPC Admin notified the user about the low GPU utilization and provided methods to monitor the jobs.
- User was advised to optimize their code to improve GPU efficiency.

## Monitoring Tools
- **ClusterCockpit**: Web interface to monitor job status and GPU utilization.
- **`srun` command**: To attach to a running job and get a shell on the first node.
  ```bash
  srun --pty --overlap --jobid YOUR-JOBID bash
  ```
- **`nvidia-smi`**: To check the current GPU utilization.

## Solution
- User optimized their code, leading to more efficient GPU utilization.
- The ticket was closed after the user's jobs started running efficiently.

## General Learnings
- Regularly monitor GPU utilization to ensure efficient resource usage.
- Use provided tools (ClusterCockpit, `srun`, `nvidia-smi`) to diagnose and optimize job performance.
- Optimize code to maximize GPU efficiency, aiming for utilization close to 100%.

## Next Steps for Similar Issues
- Notify the user about low GPU utilization.
- Provide guidance on monitoring and optimization tools.
- Encourage code optimization to improve resource efficiency.
---

### 2025012842000455_WG%3A%20BV%20Bungert%20-%20Konzeptpapier.md
# Ticket 2025012842000455

 # HPC Support Ticket Analysis

## Subject
WG: BV Bungert - Konzeptpapier

## Keywords
- HPC-Bedarf
- Rechenleistung
- GPU-Rechner
- CPU-Cluster
- GPU-Cluster
- Berufungskonzept
- FAU
- BayernKI
- NHR
- Tier3-Grundversorgung

## Problem
- User requests guaranteed computing time on CPU and GPU clusters without financial contribution.
- User inquires about the feasibility of acquiring two deep-learning-capable GPU workstations for €20,000.

## HPC Admin Response
- Local GPU workstations for development work are considered reasonable within the mentioned budget.
- Access to computing power for FAU scientists is available through various channels:
  - Tier3-Grundversorgung: Low-threshold access, but capacity depends on available funds.
  - BayernKI: Still in development, access rules and resource allocation not yet finalized.
  - NHR: Computing time allocated based on scientific proposals and reviewed by an independent committee.
- Guaranteed computing time without financial contribution is not feasible.

## Solution
- Local GPU workstations can be acquired within the budget for development purposes.
- Scientists should utilize available channels for accessing computing resources, understanding that guaranteed time requires financial investment.

## General Learnings
- Local workstations for development are a viable option within a reasonable budget.
- Various channels exist for accessing computing resources, each with its own allocation criteria.
- Guaranteed computing time typically requires financial contribution to the infrastructure.

## Next Steps
- User should consider acquiring local GPU workstations for development.
- User should explore available channels for accessing computing resources and understand the allocation criteria.

---

This report provides a concise summary of the HPC support ticket conversation, highlighting the key points and general learnings for future reference.
---

### 2022110742003639_AssocGrpNodeLimit%20f%C3%83%C2%BCr%20gwgi.md
# Ticket 2022110742003639

 ```markdown
# HPC-Support Ticket Conversation: AssocGrpNodeLimit for gwgi

## Keywords
- AssocGrpNodeLimit
- Slurm
- Woody-NG Cluster
- IO-Intensität
- TMPDIR
- sbatch
- Job Limits
- HPC Support

## Summary
A user from the gwgi group experienced job limits on the HPC cluster, specifically on the Woody-NG cluster. The user's jobs were being queued and hitting a limit indicated by `AssocGrpNodeLimit` in the `squeue` output. The user had two main questions:
1. Is the limit fixed or fluid, and what is the current limit for the gwgi group?
2. Is there a way to purchase a higher limit?

## Root Cause
- The user's account `gwgifu0h` was limited to 128 cores on the Woody-NG cluster, which is 7.5% of the available Tier3 hardware.
- The high IO-intensity of the user's jobs was suspected to be causing issues with the fileservers, leading to the implementation of this limit.
- The `fu` accounts were originally intended for data storage rather than intensive computing.

## Solution
- The HPC admins explained that the limits are dynamic and can be adjusted based on operational needs to ensure smooth operation for all users.
- The user was advised to optimize their job scripts to reduce IO-intensity, such as using `TMPDIR` for temporary data and reducing the number of parallel untar operations.
- The user suggested discussing further optimization strategies in an upcoming Zoom meeting with the AG-GIS group.

## General Learnings
- Job limits on HPC clusters can be dynamic and are adjusted based on operational needs.
- High IO-intensity jobs can impact the performance of fileservers and other users.
- Optimizing job scripts to reduce IO-intensity, such as using temporary directories and reducing parallel operations, can help mitigate these issues.
- Regular communication with HPC support and other users can help identify and address performance bottlenecks.
```
---

### 2025012842002444_Jobs%20on%20Alex%20is%20only%20using%201%20of%203%20GPU%20%5Bv103fe19%5D.md
# Ticket 2025012842002444

 ```markdown
# HPC Support Ticket: Jobs on Alex is only using 1 of 3 GPU

## Keywords
- GPU utilization
- Job monitoring
- Resource allocation
- ClusterCockpit
- nvidia-smi
- srun

## Issue
- User's job on Alex (JobID 2336506) was only using one of the four allocated GPUs.

## Root Cause
- Incorrect job configuration by the user.

## Solution
- User identified and corrected the configuration issue.

## Steps Taken
1. **HPC Admin Notification**:
   - Informed the user about the underutilization of GPUs.
   - Provided a screenshot from the monitoring system.
   - Suggested using ClusterCockpit for monitoring.
   - Provided instructions to attach to the running job using `srun` and check GPU utilization with `nvidia-smi`.

2. **User Response**:
   - Acknowledged the issue.
   - Identified and corrected the configuration problem.

## General Learning
- Always ensure that jobs are correctly configured to utilize all allocated resources.
- Use monitoring tools like ClusterCockpit to check resource utilization.
- Attach to running jobs using `srun` and check GPU utilization with `nvidia-smi` for troubleshooting.

## Closure
- The ticket was closed after the user confirmed the issue was resolved.
```
---

