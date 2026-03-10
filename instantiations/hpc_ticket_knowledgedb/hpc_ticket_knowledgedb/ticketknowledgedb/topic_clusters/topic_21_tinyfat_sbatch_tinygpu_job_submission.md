# Topic 21: tinyfat_sbatch_tinygpu_job_submission

Number of tickets: 46

## Tickets in this topic:

### 2021092442000955_Request%20for%20a%20larger%20memory%20allocation.md
# Ticket 2021092442000955

 # HPC Support Ticket: Request for a Larger Memory Allocation

## Keywords
- Memory allocation
- HPC cluster
- High memory requirements
- Hardware limitations
- Temporary storage
- Slurm

## Problem
- User's jobs require a large amount of memory and are unable to complete with the existing memory allocation.
- Jobs fail due to high memory requirements.

## Root Cause
- Hardware limitation: The user's jobs require more memory than the available 256GB RAM on the current nodes.

## Solution
- **Temporary Fix**: HPC Admins suggested using nodes with 512GB RAM (tf040-42 and tf060-95) in the tinyfat cluster.
- **Potential Long-term Fix**: A node with 2TB RAM in the test cluster was mentioned, but it was not available at the time due to preparations for a new cluster.

## Notes
- The user had concerns about the storage capacity (3.5TB) of the suggested nodes.
- The user already had access to the suggested nodes with 512GB RAM.
- The HPC Admins apologized for any confusion caused by initial suggestions.

## Follow-up
- The user agreed to try the suggested nodes with 512GB RAM.
- Further monitoring is needed to ensure this solution meets the user's requirements.

## Documentation Links
- [Tinyfat Cluster Documentation](https://hpc.fau.de/systems-services/systems-documentation-instructions/clusters/tinyfat-cluster/)
- [Test Cluster Documentation](https://hpc.fau.de/systems-services/systems-documentation-instructions/clusters/test-cluster/)
---

### 2024081542001977_About%20submitting%20tasks.md
# Ticket 2024081542001977

 ```markdown
# HPC-Support Ticket: Submitting Tasks

## Keywords
- `sbatch`
- `gres`
- `TinyGPU`
- `job script`
- `sbatch.tinygpu`

## Problem Description
- User encountered an error when submitting a job using `sbatch`: `sbatch: error: Invalid generic resource (gres) specification`.
- User provided `sinfo` output showing the state of the nodes.

## Root Cause
- The user was not using the correct command to submit jobs on TinyGPU.

## Solution
- Use `sbatch.tinygpu` instead of `sbatch` to submit jobs on TinyGPU.

## Steps Taken
1. **Initial Report**: User reported an error when submitting a job.
2. **Admin Response**: Admin requested the job script and confirmed that the job submission worked on their end.
3. **Admin Diagnosis**: Admin identified that the user was not using `sbatch.tinygpu`.
4. **User Confirmation**: User confirmed that using `sbatch.tinygpu` resolved the issue.

## Conclusion
- The issue was resolved by using the correct command for job submission on TinyGPU.

## Documentation Reference
- [Slurm Commands on TinyGPU](https://doc.nhr.fau.de/clusters/tinygpu/#slurm-commands-are-suffixed-with-tinygpu)
```
---

### 2024052042000401_Invalid%20generic%20resource%20%28gres%29%20specification.md
# Ticket 2024052042000401

 ```markdown
# HPC-Support Ticket: Invalid Generic Resource (GRES) Specification

## Keywords
- Batch job submission
- sbatch
- Invalid generic resource (gres) specification
- TinyGPU
- Python
- Nvidia A100 GPUs
- Partition

## Problem
- User encountered an error while submitting a batch job using `sbatch`: `sbatch: error: Invalid generic resource (gres) specification`.
- The user was trying to submit a job with `--gres=gpu:a100:1` on TinyGPU.

## Root Cause
- Incorrect usage of `sbatch` and partition specification for TinyGPU.

## Solution
- Use `sbatch.tinygpu` for job submission on TinyGPU.
- Specify the correct partition for Nvidia A100 GPUs using `-p a100`.

## Additional Information
- Refer to the documentation for more details: [TinyGPU Documentation](https://doc.nhr.fau.de/clusters/tinygpu/)

## General Learning
- Ensure the correct `sbatch` command and partition are used for specific GPU types.
- Always refer to the cluster-specific documentation for accurate job submission guidelines.
```
---

### 2024081542002547_Problem%20with%20tiny.md
# Ticket 2024081542002547

 # HPC Support Ticket: Problem with tiny

## Keywords
- SLURM
- sbatch
- salloc
- squeue
- A100 GPUs
- tinygpu
- Invalid generic resource (gres) specification

## Problem Description
The user encountered an error when submitting a job to request 2 A100 GPUs:
```
sbatch: error: Invalid generic resource (gres) specification
```
The user's job script included:
```bash
#SBATCH --partition a100
#SBATCH --gres=gpu:a100:2
```

## Root Cause
The user was using standard SLURM commands instead of the tinygpu-specific commands required for the tinygpu cluster.

## Solution
HPC Admins advised the user to use the following commands specific to the tinygpu cluster:
- For interactive runs: `salloc.tinygpu`
- For submitting job scripts: `sbatch.tinygpu`
- For checking job status: `squeue.tinygpu`

## Documentation Reference
- [tinygpu SLURM Commands](https://doc.nhr.fau.de/clusters/tinygpu/#slurm-commands-are-suffixed-with-tinygpu)

## Lessons Learned
- Always use cluster-specific SLURM commands when working on specialized clusters like tinygpu.
- Check the documentation for the correct commands and usage guidelines.
- Ensure that all related commands (sbatch, salloc, squeue) are used with the appropriate suffix for the specific cluster.
---

### 2024102542001855_4%20H100%20on%20tinyx.md
# Ticket 2024102542001855

 ```markdown
# HPC Support Ticket: 4 H100 on tinyx

## Keywords
- SLURM
- H100 GPUs
- Job Submission Error
- `--cpus-per-task`
- TinyGPU Nodes

## Problem Description
User encountered an error when submitting a SLURM job requesting 4 H100 GPUs on `tinyx.nhr.fau.de`. The job submission failed with the error:
```
sbatch: error: Batch job submission failed: Requested node configuration is not available
```
The job submission was successful when requesting at most 3 GPUs.

## Job Configuration
```bash
#SBATCH --partition=h100
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=10
#SBATCH --job-name=job
#SBATCH --gres=gpu:h100:4
#SBATCH --time=03-00:00
#SBATCH --chdir=/home/hpc/iwal/iwal179h/work/projects/data-processing-exploration
#SBATCH --output=slurm/log_liter/%j.out
#SBATCH --error=slurm/log_liter/%j.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=viktor.hangya@iis.fraunhofer.de
#SBATCH --export=NONE
```

## Root Cause
The `--cpus-per-task` option caused SLURM internal issues when requesting 4 H100 GPUs.

## Solution
Remove the `--cpus-per-task` option from the job configuration.

## General Learning
- SLURM job configurations can sometimes cause internal issues, especially with specific resource requests.
- Removing or adjusting certain options (e.g., `--cpus-per-task`) can resolve job submission errors.
- Always check the job configuration for potential conflicts when encountering submission errors.
```
---

### 2022092142003563_Submitting%20a%20job%20on%20tinyfat.md
# Ticket 2022092142003563

 ```markdown
# HPC Support Ticket: Submitting a Job on tinyfat

## Subject
Submitting a job on tinyfat

## User Issue
The user is experiencing an error when submitting a job using `sbatch .sh` on the tinyfat cluster. The error message is "sbatch: error: No cluster 'tinyfat' known by database."

## User's Script
```bash
#!/bin/bash -l
#SBATCH --nodes=1
#SBATCH --time=10:00:00
#SBATCH --mem=120G
#SBATCH --export=NONE
#SBATCH --clusters=tinyfat
#SBATCH --job-name=polarization
#SBATCH --mail-user=dilshod.durdiev@fau.de
#SBATCH --mail-type=begin,end,fail
#SBATCH --output=output.out
#SBATCH --error=error.err

unset SLURM_EXPORT_ENV
mkdir ${WORK}/${SLURM_JOB_ID}
cd ${WORK}/${SLURM_JOB_ID}
folder=results_"$(date +"%d_%m_%y_%H_%M")"
mkdir $folder

# activate python virtual env
module load python/3.8-anaconda
source ${WORK}/virtualenvpy/bin/activate

# applied electrical field in the y-deriction
E_app_y=0
# number of time steps
nsteps=50000
# time frame to print results
nt=100
# number of grid points
N=512
# copy all necassary python files to working directory
cp ${HOME}/Sep20/*  ${WORK}/${SLURM_JOB_ID}

srun python3 3d_polarization.py $folder

cp -R ${WORK}/${SLURM_JOBID}/$folder ${HOME}
rm -r ${WORK}/${SLURM_JOBID}
```

## HPC Admin Response
- The user is likely logged into the wrong frontend.
- Use `tinyx.nhr.fau.de` as the frontend for tinyfat.

## Solution
- Ensure the user is logged into the correct frontend (`tinyx.nhr.fau.de`) for submitting jobs to tinyfat.

## Keywords
- `sbatch`
- `tinyfat`
- `frontend`
- `job submission`
- `cluster`
- `error`

## General Learning
- Always ensure you are logged into the correct frontend for the specific cluster you are targeting.
- Verify the cluster name and frontend details before submitting jobs.
```
---

### 2018121742001646_Fehlermeldung%20bei%20Parallelisierung%20auf%20Woody%20%28R%29.md
# Ticket 2018121742001646

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject: Fehlermeldung bei Parallelisierung auf Woody (R)

### Keywords:
- Parallel computing
- R package `parallel`
- `mclapply` function
- Woody-Cluster
- Memory issues
- Batch script
- TinyFat
- DOS/Windows text format

### Problem Summary:
- User encounters errors when running a large number of simulations using `mclapply` in R on the Woody-Cluster.
- Error message: `all scheduled cores encountered errors in user code`.
- Suspected memory issues, but freeing memory did not resolve the problem.
- Batch script for TinyFat not accepted due to DOS/Windows text format.

### Root Cause:
- Potential memory overload or resource contention on Woody-Cluster.
- Incorrect text format of the batch script for TinyFat.

### Solution:
- Verify memory usage and ensure sufficient resources are allocated.
- Convert the batch script to Unix text format using tools like `dos2unix` before submitting to TinyFat.

### General Learnings:
- Memory management is crucial for parallel computing tasks.
- Ensure batch scripts are in the correct text format for the target system.
- Use tools like `dos2unix` to convert text formats if necessary.
```
---

### 2020021442001764_Jobs%20auf%20TinyFAT%20-%20bca2002h.md
# Ticket 2020021442001764

 # HPC Support Ticket Analysis: Jobs auf TinyFAT

## Keywords
- TinyFAT
- Memory usage
- Job scheduling
- Resource allocation

## Problem
- User regularly requests nodes with 512 GB of memory on TinyFAT, but jobs only use 10 GB or less.
- Jobs on 256 GB nodes also frequently underutilize the allocated memory.

## Root Cause
- Inefficient resource allocation leading to underutilization of memory resources.

## Solution
- User agreed to cancel running jobs and will not schedule similar jobs on TinyFAT in the future.

## Lessons Learned
- Ensure proper resource allocation to avoid wasting computational resources.
- Monitor job memory usage to optimize scheduling and resource management.
- Communicate with users to understand their job requirements and provide guidance on efficient resource utilization.

## References
- [Job Info Links](https://www.hpc.rrze.fau.de/HPC-Status/job-info.php?USER=bca2002h&JOBID=146572&ACCESSKEY=86932fce&SYSTEM=TINYFAT)
- [HPC Services](http://www.hpc.rrze.fau.de/)

## Roles Involved
- HPC Admins
- User
---

### 2023071042001597_Batch%20job.md
# Ticket 2023071042001597

 # HPC Support Ticket: Batch Job

## Keywords
- Batch jobs
- Interactive batch jobs
- Tinyx node
- Long-term access
- Example codes
- Introduction for HPC Beginners
- Documentation

## Problem
- User needs access to tinyx node for a longer period.
- User is unsure about how to use batch jobs or interactive batch jobs.
- User has reviewed the FAU website but requires further clarification.

## Solution
- **Introduction for HPC Beginners**:
  - Monthly session covering batch job submission and interactive jobs.
  - Next session: July 12 at 4 pm.
  - Link: [Zoom Meeting](https://fau.zoom.us/j/63416831557)

- **Documentation**:
  - General introduction to the batch system: [Batch Processing](https://hpc.fau.de/systems-services/documentation-instructions/batch-processing/)
  - Specific examples for TinyGPU: [TinyGPU Cluster](https://hpc.fau.de/systems-services/documentation-instructions/clusters/tinygpu-cluster/)

## General Learnings
- Users often require hands-on examples and detailed explanations for batch job submissions.
- Regular introductory sessions and comprehensive documentation are essential for user support.
- Providing links to relevant resources can help users understand complex processes.

## Next Steps
- Encourage the user to attend the introductory session.
- Direct the user to the provided documentation links for further reading.
- Offer additional support if needed.
---

### 2021112242000301_Requested%20node%20configuration%20is%20not%20available%20when%20using%20--ntasks-per-node%3D1.md
# Ticket 2021112242000301

 # HPC Support Ticket: Requested Node Configuration Issue

## Keywords
- Slurm
- `--ntasks-per-node`
- `--gpus-per-task`
- Resource allocation
- GPU allocation

## Problem Description
The user encountered an issue where using the flag `--ntasks-per-node=1` resulted in a job termination with the error message:
```
srun: Force Terminated job 44045
srun: error: Unable to allocate resources: Requested node configuration is not available
```
The only value that worked was `--ntasks-per-node=8`, but this ran the job multiple times.

## Reproduction Steps
```bash
srun -M tinygpu --gres=gpu /bin/uuidgen
srun -M tinygpu --gres=gpu --ntasks-per-node=1 /bin/uuidgen
srun -M tinygpu --gres=gpu --ntasks-per-node=8 /bin/uuidgen
```

## Root Cause
The issue arises from not specifying the number of GPUs to be allocated, which is required for accounting purposes.

## Solution
1. **Use `--gpus-per-task=1`**:
   ```bash
   srun -M tinygpu --gres=gpu --ntasks-per-node=1 --gpus-per-task=1 /bin/uuidgen
   ```
2. **Use `--ntasks` instead of `--ntasks-per-node`**:
   ```bash
   srun -M tinygpu --gres=gpu --ntasks=1 /bin/uuidgen
   ```

## Additional Notes
- The HPC Admin recommends using `--ntasks` instead of `--ntasks-per-node` for single-node jobs.
- Allocating `gres=gpu` without specifying the number of GPUs (e.g., `gres=gpu:1`) will no longer be allowed in the future.

## Conclusion
The issue was resolved by specifying the number of GPUs per task, ensuring proper resource allocation and avoiding job termination due to unavailable node configurations.
---

### 2017050342000563_Rechnungen%20HPC%20-%20mehr%20Arbeitsspeicher.md
# Ticket 2017050342000563

 # HPC Support Ticket: Memory Requirements for Computations

## Keywords
- Memory requirements
- Node specifications
- Job submission
- qsub command
- TinyEth cluster
- TinyFat cluster
- LiMa cluster

## Problem
- User is running memory-intensive computations on the LiMa cluster.
- Each computation runs on a single node but cannot utilize 24 threads due to insufficient memory.
- User inquires about nodes with more memory or alternative clusters.

## Solution
- **LiMa Cluster**: All nodes have the same memory configuration.
- **TinyEth Cluster**: Nodes have 48 GB of memory.
  - Job submission command: `qsub.tinyeth -l nodes=1:ppn=24 -l walltime=24:00:00 Skript.sh`
  - Ensure the syntax and queue resources are correct.
- **TinyFat Cluster**: Nodes have 128 to 512 GB of memory.
  - Refer to the documentation for job submission: [TinyFat Cluster Documentation](http://www.rrze.fau.de/dienste/arbeiten-rechnen/hpc/systeme/memoryhog.shtml#tinyfat)

## Additional Notes
- Use the official FAU email address for professional communication.
- Ensure job submission commands are correctly formatted to avoid errors.

## Root Cause
- Insufficient memory on LiMa cluster nodes for the user's computations.

## Resolution
- Recommended using TinyEth or TinyFat clusters for higher memory requirements.
- Provided correct job submission commands and documentation links.

## Follow-Up
- Verify the user's job submission command and ensure it aligns with the cluster's requirements.
- Assist with any further issues related to job submission or memory allocation.
---

### 2022081242002011_Access%20to%20fat%20node.md
# Ticket 2022081242002011

 ```markdown
# HPC-Support Ticket Conversation Summary

## Subject: Access to fat node

### Keywords:
- HPC access
- Fat node
- teramem
- TinyFAT
- NHR Testproject
- SSH keys
- Login issues
- Project status

### What Can Be Learned:

#### General Information:
- **HPC Admins** handle user requests for access to specific nodes.
- **teramem** system was down and relocated, causing unavailability.
- **TinyFAT** nodes with 512 GB RAM were offered as an alternative.
- **NHR Testproject** application required for access.
- **SSH keys** are used for login and need to be uploaded to the HPC portal.
- **Project status** checks are conducted by HPC Admins.

#### Specific Issues and Solutions:
1. **Access Request**:
   - **Issue**: User requested access to a fat node with high core count and at least 512 GB RAM.
   - **Solution**: HPC Admins suggested using TinyFAT nodes with 512 GB RAM as teramem was unavailable.

2. **NHR Testproject Application**:
   - **Issue**: User needed to submit an NHR Testproject application.
   - **Solution**: User was directed to the application form and submitted it with minimal information.

3. **SSH Key Login Issue**:
   - **Issue**: User unable to login to woody.rrze.uni-erlangen.de via SSH from cshpc.
   - **Solution**: HPC Admins fixed a configuration issue related to SSH keys.

4. **Project Status Check**:
   - **Issue**: HPC Admins noticed low usage of the project.
   - **Solution**: User explained the delay due to personal reasons and upcoming work. Project was extended until June next year.

### Root Cause of Problems:
- **teramem** system unavailability due to relocation.
- **SSH key configuration** issue on woody.rrze.uni-erlangen.de.

### Solutions:
- **Alternative nodes**: TinyFAT nodes were offered as an alternative.
- **Configuration fix**: SSH key configuration was corrected to allow login.
- **Project extension**: Project was extended to accommodate user's timeline.

### Documentation for Support Employees:
- **Access Request**: Direct users to TinyFAT nodes if teramem is unavailable.
- **NHR Testproject**: Ensure users submit the application form with minimal information.
- **SSH Key Issues**: Check SSH key configuration and ensure keys are uploaded to the HPC portal.
- **Project Status**: Conduct regular checks and extend projects if necessary based on user's explanation.
```
---

### 2022090842004159_Tinyfat%20spezifische%20nodes%20anfordern.md
# Ticket 2022090842004159

 # HPC Support Ticket: Requesting Specific Nodes on TinyFat

## Keywords
- TinyFat
- Node allocation
- RAM-intensive workload
- Partition
- FAU-Account
- NHR-Account

## Problem
- User needs to run a RAM-intensive workload on TinyFat.
- Requires specific nodes (tf060-tf095) to maximize threads.
- Unable to find a specific command to request these nodes.

## Root Cause
- User is unaware of the default node allocation behavior on TinyFat.
- Documentation does not clearly specify how to request specific nodes.

## Solution
- **Node Allocation**: The tf060-tf095 nodes are used by default on TinyFat. No special option is needed to request these nodes.
- **Account Freeschalten**: FAU-Accounts are automatically enabled on TinyFat. NHR-Accounts need to be manually enabled by HPC Admins.
- **Partition Specification**: Only other node types require explicit partition specification.

## General Learnings
- Understand the default behavior of node allocation on TinyFat.
- FAU-Accounts are enabled by default, while NHR-Accounts require manual activation.
- For specific node types, explicit partition specification may be necessary.

## Actions Taken
- HPC Admin informed the user about the default node allocation behavior.
- User confirmed access with their FAU-Account.
- Ticket closed as the user's query was resolved.

## Future Reference
- For similar queries, refer users to the default node allocation behavior on TinyFat.
- Ensure users are aware of the account activation process for NHR-Accounts.

---

This documentation will help support employees address similar issues related to node allocation and account management on TinyFat.
---

### 2021050742001207_problem%20about%20connecting%20TinyGPU.md
# Ticket 2021050742001207

 # HPC Support Ticket: Problem Connecting TinyGPU

## Keywords
- TinyGPU
- qsub.tinygpu
- Python
- JupyterHub
- Torque
- Interactive Job
- Batch Processing

## Problem Description
The user needs to run a Python script (`train.py`) on TinyGPU for their research project. They have uploaded their code and dataset (2.5GB) to the HPC system but are unsure how to connect to TinyGPU from the main HPC cluster (woody).

## Root Cause
- User lacks knowledge on how to submit and manage GPU jobs on the HPC system.
- User is unaware of the interactive job submission process.

## Solution
1. **Interactive Python Development**:
   - Suggested use of JupyterHub for interactive Python development.
   - Documentation: [Python and Jupyter](https://hpc.fau.de/systems-services/systems-documentation-instructions/special-applications-and-tips-tricks/python-and-jupyter/)

2. **Interactive Job Submission**:
   - Command for interactive job submission:
     ```bash
     qsub.tinygpu -l nodes=1:ppn=4,walltime=01:00:00 -I
     ```
   - Documentation:
     - [Torque](https://hpc.fau.de/systems-services/systems-documentation-instructions/batch-processing/#torque)
     - [TinyGPU Nodes](https://hpc.fau.de/systems-services/systems-documentation-instructions/clusters/tinyx-clusters/#collapse_1)

3. **Training Opportunity**:
   - Mentioned an upcoming beginners training session on 12.05.

## General Learning
- Users should be directed to relevant documentation for interactive job submission and Python development.
- Interactive job submission commands and links to documentation should be provided for quick reference.
- Training sessions can be beneficial for users new to the HPC system.

## Follow-up Actions
- Ensure the user attends the upcoming training session.
- Verify if the user successfully submitted their job using the provided command.
- Offer additional support if needed.
---

### 42115887_mini%20jobs%20on%20TinyFat.md
# Ticket 42115887

 # HPC Support Ticket: Mini Jobs on TinyFat

## Keywords
- Turbomole jobs
- TinyFat nodes
- CPU usage
- Memory usage
- Job submission
- Woody cluster
- Job runtime restrictions

## Problem
- User's Turbomole jobs on TinyFat use only one CPU and less than 100 MB of main memory.
- TinyFat nodes have 128 GB main memory, which is excessive for these jobs.
- User needs an alternative cluster to run these small jobs.

## Conversation Summary
- **HPC Admin**: Questioned the user about the necessity of using TinyFat for small jobs.
- **User**: Acknowledged the issue and requested an alternative cluster for running Turbomole jobs with one processor.
- **HPC Admin**: Suggested submitting jobs on Woody with `-l nodes=1:ppn=1:sb` to get one core only, with a memory limit of 1.5 GB and no $FASTTMP available.
- **User**: Inquired about running jobs longer than 24 hours.
- **HPC Admin**: Clarified that regular clusters have runtime restrictions (24h or 48h), but exceptions can be made upon request.

## Solution
- **Alternative Cluster**: Users with small jobs should submit them on Woody with `-l nodes=1:ppn=1:sb`.
- **Runtime Extensions**: For jobs requiring more than 24 hours, users should contact HPC support for manual wall time increases or dedicated test cluster access.

## General Learnings
- **Resource Allocation**: Ensure users are aware of the appropriate clusters for their job sizes to optimize resource usage.
- **Job Submission Parameters**: Educate users on specifying job requirements correctly to avoid wasting resources.
- **Runtime Flexibility**: Communicate the possibility of requesting extended runtimes for exceptional cases.

## Action Items
- **Documentation**: Update user guides with information on submitting small jobs on Woody.
- **Communication**: Inform users about the process for requesting extended job runtimes.
---

### 2022040442004424_Tinyfat.md
# Ticket 2022040442004424

 # HPC Support Ticket: Tinyfat Job Submission Issue

## Keywords
- Tinyfat
- Job submission
- sbatch
- Resource allocation
- Node availability

## Problem Description
- User reported that no jobs were starting on Tinyfat.
- User provided the submit command for reference.

## Root Cause
- High demand from other user groups that fully funded Tinyfat.
- All nodes were occupied by these groups.

## Solution
- No immediate solution provided.
- User advised to wait until nodes become available.

## Lessons Learned
- High demand from funding groups can lead to resource unavailability.
- Users should be aware of potential delays during peak usage times.
- Communication about resource allocation and availability is crucial.

## Follow-up Actions
- Monitor resource usage and availability.
- Consider implementing a fair-share policy to balance resource allocation.
- Inform users about potential delays and resource management strategies.

## Related Commands
- `sbatch.tinyfat --job-name=${nm} --output=${o_nm} --error=${e_nm} --time=${wt} --mem=256G $script_dir/04_07_strip_large_prc.sh`
---

### 2024092542002179_question.md
# Ticket 2024092542002179

 # HPC Support Ticket Conversation Summary

## Keywords
- HPC Cluster
- Woody Cluster
- Fritz Cluster
- Tinyfat Cluster
- Memory per Core
- Parallelization
- SLURM
- Job Submission
- Job Failure

## What Can Be Learned

### User Requirements
- User needs parallelization and large memory per core.
- User is currently using the Woody cluster with a maximum of 32 cores, each with 7.75GB RAM.

### Recommendations
- **Fritz Cluster**: Recommended for access to more RAM.
- **Tinyfat Cluster**: Suggested as an alternative due to the user's chair financing tf06x-tf09x.

### Issues Encountered
- **Job Submission on Tinyfat**: Jobs were not running, and SLURM files were not created.
  - **Root Cause**: Job failed and ran only for 2 seconds.
  - **Solution**: Issue resolved by 16:00.

### Actions Taken
- User was advised to consult their supervisor for access to the Fritz cluster.
- User was informed about the Tinyfat cluster as a potential alternative.

### Documentation Links
- [Fritz Cluster Documentation](https://doc.nhr.fau.de/clusters/fritz/)
- [Tinyfat Cluster Documentation](https://doc.nhr.fau.de/clusters/tinyfat/)

### Ticket Closure
- Ticket closed as the problem no longer occurred.

## General Learnings
- Always check for alternative clusters that might better suit the user's needs.
- Ensure users are aware of the documentation for the recommended clusters.
- Monitor job submissions and failures to identify and resolve issues promptly.

---

This summary provides a concise overview of the support ticket conversation, highlighting key points and recommendations for future reference.
---

### 2022092242004695_help%20with%20running%20batch%20script.md
# Ticket 2022092242004695

 ```markdown
# HPC Support Ticket: Help with Running Batch Script

## Keywords
- Batch script error
- Invalid generic specification
- GPU access
- Jupyter notebook
- Frontend change

## Summary
The user encountered issues with running a batch script that previously worked, including errors accessing the GPU and opening Jupyter notebook.

## Root Cause
- The frontend for TinyGPU has changed from `woody` to `tinyx.nhr.fau.de`.

## Solution
- Update the batch script to use the new frontend `tinyx.nhr.fau.de`.

## Lessons Learned
- Always check for updates or changes in the HPC environment after a break.
- Ensure that the frontend specified in the batch script is current and correct.
- Communicate any changes in the HPC infrastructure to users to avoid disruptions.

## Actions Taken
- The HPC Admin informed the user about the change in the frontend for TinyGPU.
- The ticket was closed after providing the necessary information.
```
---

### 2023060642001481_Problem%20with%20scaling%20Machine%20Learning%20Experiments%20on%20two%20different%20clusters.md
# Ticket 2023060642001481

 ```markdown
# Problem with Scaling Machine Learning Experiments on Two Different Clusters

## Keywords
- Machine Learning Experiments
- Woody Cluster
- TinyGPU Cluster
- sbatch
- sbatch.tinygpu
- Job Cancellation
- Module Loading

## Problem Description
- User attempts to run machine learning experiments on two different clusters: Woody for classical methods (XGBoost) and TinyGPU for deep learning.
- User logs into Woody cluster, loads Anaconda, and submits a batch script using `sbatch`.
- Attempting to submit a job to TinyGPU from the Woody frontend using `sbatch.tinygpu` results in a "command not found" error.
- Logging into TinyGPU and loading a Python module causes previously submitted jobs on Woody to be cancelled.

## Root Cause
- Different frontends for Woody and TinyGPU clusters:
  - Woody: `woody.nhr.fau.de`
  - TinyGPU/TinyFat: `tinyx.nhr.fau.de`
- `sbatch.tinygpu` command is not available on the Woody frontend.
- Incorrect module loading leading to job cancellations.

## Solution
- Submit jobs to TinyGPU from its own frontend (`tinyx.nhr.fau.de`).
- Ensure proper module loading to prevent job cancellations.
- Update documentation to reflect correct submission procedures.

## Lessons Learned
- Ensure users are aware of the different frontends for submitting jobs to specific clusters.
- Proper module loading is crucial to avoid job cancellations.
- Documentation should be kept up-to-date to reflect accurate submission procedures.
```
---

### 2021071942003117_Nutzung%20der%20Nodes%20am%20Lehrstuhl%20f%C3%83%C2%BCr%20theoretische%20Physik%20II.md
# Ticket 2021071942003117

 # HPC Support Ticket: Access to Nodes for Theoretical Physics II

## Keywords
- HPC Account
- Node Access
- Queueing System
- Slurm
- TinyFAT Cluster

## Problem
- User requires access to nodes for research work.
- User does not have access credentials.

## Root Cause
- User does not have an HPC account.
- Direct login to nodes is not possible; access is only via the queueing system.

## Solution
- User needs to apply for an HPC account.
- Access to nodes is managed through the Slurm queueing system on the TinyFAT cluster.

## Steps to Resolve
1. **Apply for HPC Account**:
   - User should visit the following link to apply for an HPC account: [HPC Account Application](https://hpc.fau.de/systems-services/systems-documentation-instructions/getting-started/)

2. **Understand Node Access**:
   - Direct login to nodes is not possible.
   - Nodes are accessible through the Slurm queueing system.

3. **Learn About TinyFAT Cluster**:
   - User should refer to the documentation for the TinyFAT cluster: [TinyFAT Cluster Documentation](https://hpc.fau.de/systems-services/systems-documentation-instructions/clusters/tinyfat-cluster/)

## General Learning
- **HPC Account Requirement**: Users need an HPC account to access resources.
- **Queueing System**: Access to nodes is managed through a queueing system (Slurm in this case).
- **Cluster Documentation**: Users should refer to cluster-specific documentation for detailed instructions.

## References
- [HPC Account Application](https://hpc.fau.de/systems-services/systems-documentation-instructions/getting-started/)
- [TinyFAT Cluster Documentation](https://hpc.fau.de/systems-services/systems-documentation-instructions/clusters/tinyfat-cluster/)

## Support Contacts
- **HPC Admins**: For account and access-related queries.
- **2nd Level Support Team**: For technical support and troubleshooting.
- **Gehard Wellein**: Head of the Datacenter.
- **Georg Hager**: Training and Support Group Leader.
- **Harald Lanig**: NHR Rechenzeit Support and Applications for Grants.
- **Jan Eitzinger and Gruber**: Software and Tools developer.
---

### 2021112542003302_VSCode%20-%20Connect%20via%20SSH%20to%20TinyGPU.md
# Ticket 2021112542003302

 # HPC Support Ticket: VSCode - Connect via SSH to TinyGPU

## Keywords
- VSCode
- SSH
- TinyGPU
- GPU-runtime
- salloc
- sbatch
- JupyterHub
- interactive job

## Problem
- User wants to SSH directly to TinyGPU for GPU-runtime access.
- Current workflow involves connecting to Woody using VSCode, which works well but limits trial runs of (ipython)-notebooks to CPU-runtime.
- User encounters errors specific to GPU computation.

## Current Workflow
- User can allocate a GPU-node using `salloc.tinygpu` and test code before submitting the entire job with `sbatch.tinygpu`.
- User can also use JupyterHub effectively.

## Solution
- HPC Admin confirms that direct SSH to TinyGPU is not possible without queuing a job.
- Two options for interactive working with GPU:
  a) Start an interactive job using `salloc.tinygpu`.
  b) If a job is running, log into the node with `ssh <username>@tg???`, where `???` is the node number.

## Positive Feedback
- User is pleased with VSCode integration with the cluster.

## Additional Notes
- HPC Admin mentions that a certificate has expired, but this is not directly related to the user's query.

## Ticket Details
- Subject: VSCode - Connect via SSH to TinyGPU
- Date: 25.11.2021
- User: Simon Bachhuber (Lehrstuhl für Daten, Sensoren und Geräte, FAU Erlangen)
- HPC Admin: Johannes Veh (HPC Services, RRZE)
---

### 2023050842001238_Access%20TinyFat%20and%20jobs%20running.md
# Ticket 2023050842001238

 # HPC Support Ticket: Access TinyFat and Job Submission

## Keywords
- TinyFat cluster
- Login issues
- Code compilation
- Job submission
- `squeue`
- `memoryhog.rrze.fau.de`
- `tinyx.nhr.fau.de`

## Summary
The user is experiencing difficulties with logging into `tinyx.nhr.fau.de` and submitting jobs to the TinyFat cluster. The user is unsure about the proper procedure for compiling and running code on the TinyFat cluster.

## Root Cause
- **Login Issues**: The user is unable to consistently log in to `tinyx.nhr.fau.de`.
- **Job Submission**: The user encounters errors when trying to submit jobs from `memoryhog.rrze.fau.de`.

## Details
- The user has read the documentation but is still confused about the correct procedure for compiling and running code on the TinyFat cluster.
- The user needs to compile the code on `memoryhog.rrze.fau.de` and run it on `tinyx.nhr.fau.de`.
- The user receives errors when attempting to submit jobs using `squeue` from `memoryhog.rrze.fau.de`.

## Solution
- **Login Issues**: Ensure that the user is using the correct credentials and that the login server is not experiencing downtime.
- **Job Submission**: Inform the user that job submission commands like `squeue` should be executed from the appropriate login node (`tinyx.nhr.fau.de`). Provide clear instructions on how to transfer compiled code to `tinyx.nhr.fau.de` and submit jobs from there.

## General Learnings
- Users may face login issues due to server downtime or incorrect credentials.
- Job submission commands should be executed from the appropriate login node.
- Clear documentation and instructions are crucial for users to understand the correct procedures for compiling and running code on HPC clusters.

## Next Steps
- Verify the status of `tinyx.nhr.fau.de` and ensure it is operational.
- Provide detailed instructions on how to compile code on `memoryhog.rrze.fau.de`, transfer it to `tinyx.nhr.fau.de`, and submit jobs using `squeue`.
- Update the documentation to clarify the procedures for compiling and running code on the TinyFat cluster.
---

### 2022022342003171_Out%20of%20memory%20error.md
# Ticket 2022022342003171

 ```markdown
# HPC Support Ticket: Out of Memory Error

## Keywords
- Out of memory error
- SLURM
- MATLAB
- Memory allocation
- Exclusive node allocation

## Problem Description
- User encountered out-of-memory errors while running a MATLAB script on the TinyFat cluster.
- Jobs were allocated 256 GB of memory and 1 node but still ran out of memory after approximately 28 minutes.
- Error message indicated processes were killed by the cgroup out-of-memory handler.

## Root Cause
- Insufficient memory allocation for the job.

## Solution
- Increase memory allocation by requesting exclusive use of a node with ~512 GB of memory.
- Replace the line `#SBATCH --mem=256000` with `#SBATCH --exclusive` in the batch script.

## Additional Notes
- User transferred the job to the `$WORK` directory to improve performance.

## Conversation Summary
- User reported out-of-memory errors and provided error messages.
- HPC Admin suggested increasing memory allocation by using `#SBATCH --exclusive`.
- User acknowledged the suggestion and planned to implement it.

## Follow-up
- User to confirm if the increased memory allocation resolves the issue.
```
---

### 2022022242002682_Doubt%20about%20batch%20script.md
# Ticket 2022022242002682

 # HPC Support Ticket: Doubt about Batch Script

## Keywords
- Batch script
- ExitCode1
- Memory allocation
- Matlab script
- Job submission
- SLURM
- TinyFat
- Directory copying
- Input/Output directories

## Problem Description
- User encountered `ExitCode1` immediately after submitting a batch script on TinyFat.
- The script was designed to run a Matlab function that processes frames from an INPUT folder and outputs results to an OUTPUT folder.
- The user allocated 256 GB of memory based on successful interactive shell tests, but jobs with 128 GB were killed due to "out of memory" errors.

## Root Cause
- The `cp` command in the job script was missing the `-r` flag, which is required for copying directories.
- There was an issue with the Matlab script in one of the jobs.

## Solution
- Ensure the `cp` command includes the `-r` flag when copying directories.
- Check the Matlab script for any errors.
- Move input files to `$WORK` directory for better performance and higher quota.

## Lessons Learned
- Always include the `-r` flag when using the `cp` command to copy directories.
- Verify the Matlab script for any issues before submitting the job.
- Use `$WORK` directory for large input/output files to avoid performance issues and quota limitations in `$HOME`.

## References
- [HPC Storage Documentation](https://hpc.fau.de/systems-services/systems-documentation-instructions/hpc-storage/)
---

### 2024081542001888_Not%20able%20to%20connect%20to%20tinygpu%20compute%20node.md
# Ticket 2024081542001888

 ```markdown
# HPC Support Ticket: Not Able to Connect to tinygpu Compute Node

## Keywords
- tinygpu
- srun
- salloc
- sbatch
- gres
- GPU
- H100
- Slurm
- Interactive run
- Job script

## Problem Description
The user is attempting to access a GPU node using the following command:
```bash
srun -M tinygpu -p h100 --gres=gpu:h100:1 --time=01:00:00 --pty bash -i
```
The command results in the error:
```bash
srun: error: Invalid generic resource (gres) specification
```

## Root Cause
The user is using an incorrect command to access the GPU node. The `srun` command with the specified parameters is not valid for the tinygpu cluster.

## Solution
The HPC Admin suggests using `salloc.tinygpu` for interactive runs and `sbatch.tinygpu` to submit job scripts. The correct commands are:
- For interactive run: `salloc.tinygpu`
- For submitting a job script: `sbatch.tinygpu`

Refer to the documentation for more details: [Slurm Commands for tinygpu](https://doc.nhr.fau.de/clusters/tinygpu/#slurm-commands-are-suffixed-with-tinygpu)

## General Learning
- Always refer to the specific cluster's documentation for the correct Slurm commands.
- Use `salloc.tinygpu` for interactive sessions and `sbatch.tinygpu` for submitting job scripts on the tinygpu cluster.
- Ensure that the generic resource (gres) specification is correct and valid for the cluster being used.
```
---

### 2025012042002888_Job%20Submission%20TinyGPU%20mit%20Beispiel%20von%20Webseite%20geht%20nicht.md
# Ticket 2025012042002888

 ```markdown
# HPC-Support Ticket: Job Submission TinyGPU mit Beispiel von Webseite geht nicht

## Keywords
- Job Submission
- TinyGPU
- Python (single GPU)
- srun
- sbatch
- --gres=gpu
- Invalid generic resource (gres) specification

## Problem Description
The user encountered an error when trying to submit a job on TinyGPU using the example script from the website. The error message indicated that the job must allocate at least one GPU with `--gres=gpu`.

## Root Cause
The user attempted to submit the job using `srun` instead of `sbatch`.

## Solution
The user realized the mistake and corrected it by using `sbatch` instead of `srun`.

## What Can Be Learned
- Ensure that the correct job submission command (`sbatch` for batch jobs) is used.
- Jobs on TinyGPU must always allocate at least one GPU with `--gres=gpu`.
- Pay attention to the specific requirements and commands for different job types and resources.

## Additional Notes
- The user initially used `srun` which is not appropriate for batch job submission.
- The correct command for batch job submission is `sbatch`.
```
---

### 2023090442001792_Cluster%20for%20job%20with%20mixed%20requirements.md
# Ticket 2023090442001792

 # HPC Support Ticket: Cluster for Job with Mixed Requirements

## Subject
Cluster for job with mixed requirements

## User Issue
- User needs to run a job with mixed requirements: CPU-heavy tasks requiring 128GB RAM and short GPU tasks for neural network inference.
- Currently using Alex cluster with A100 GPU for debugging.
- Looking for a more suitable cluster for production runs.

## HPC Admin Response
- Suggested using TinyGPU cluster, which allows submitting jobs to TinyFAT (CPU-only cluster with >512GB RAM nodes).
- Advised creating chain jobs that submit to either TinyGPU or TinyFAT at the end of a script.

## Follow-up Issues
- User encountered problems with SLURM dependencies across different clusters.
- Job submission from TinyGPU to TinyFAT failed due to mutually exclusive SLURM memory variables.

## Solution
- Replace `#SBATCH --mem=512000` with `#SBATCH --exclusive` in TinyFAT job script to avoid setting conflicting SLURM variables.
- Alternatively, reduce the requested memory in the TinyFAT job script.
- Modify the sbatch command in the TinyGPU job script to: `env -i /bin/bash -l -c "sbatch -M tinyfat cluster_tinyfat.sh"` to prevent SLURM variables from being carried over.

## Keywords
- SLURM dependencies
- Job chaining
- Cross-cluster job submission
- SLURM memory variables
- TinyGPU
- TinyFAT
- GPU jobs
- CPU jobs
- High memory requirements

## General Learning
- SLURM dependencies do not work across different clusters unless they are in federation mode.
- SLURM memory variables (SLURM_MEM_PER_CPU, SLURM_MEM_PER_GPU, SLURM_MEM_PER_NODE) are mutually exclusive and can cause job failures if not managed properly.
- Using `env -i /bin/bash -l -c` can help prevent SLURM variables from being carried over between job submissions.
- Job chaining can be achieved by submitting a new job at the end of a script, specifying the target cluster with the `-M` flag.
---

### 2023111442002946_TinyFat%2C%20out-of-memory%20issue.md
# Ticket 2023111442002946

 # HPC Support Ticket: TinyFat, Out-of-Memory Issue

## Keywords
- Out-of-memory issue
- TinyFat cluster
- SLURM
- MPI
- Memory allocation
- Divide by zero
- CUDA

## Problem Description
The user encountered an out-of-memory issue while running a job on the TinyFat cluster. The job involved audio feature extraction using `librosa` and `parselmouth` libraries, which do not support GPU. The SLURM output indicated that the job was terminated due to insufficient memory.

## Root Cause
- Insufficient memory allocation due to running on a node-sharing system with only one core requested.
- Potential divide by zero issue in the code, which could lead to unexpectedly large arrays.
- Unnecessary loading of CUDA in the job script.

## Solution
1. **Increase Memory Allocation**: Request more cores to allocate more memory for the job.
2. **Remove `srun`**: Simply run the Python script without `srun`.
3. **Fix Divide by Zero Issue**: Ensure that the code does not encounter divide by zero errors.
4. **Remove CUDA**: Remove the unnecessary CUDA loading from the job script.

## General Learnings
- Understand the memory allocation mechanism on node-sharing systems.
- Ensure that the job script is optimized for the specific cluster and job requirements.
- Check for potential issues in the code that could lead to excessive memory usage.
- Refer to sample job scripts for proper configuration, such as specifying the number of MPI processes if applicable.

## References
- [TinyFat Cluster Documentation](https://hpc.fau.de/systems-services/documentation-instructions/clusters/tinyfat-cluster/)
---

### 2017040742001306_Knoten%20mit%20SSDs%3F.md
# Ticket 2017040742001306

 ```markdown
# HPC-Support Ticket: Accessing Nodes with Local SSDs on tinyfat

## Keywords
- HPC Support
- tinyfat
- Local SSDs
- Interactive Nodes
- qsub

## Problem Description
The user is inquiring about how to access nodes with local SSDs on the tinyfat system. The user also mentions that the documentation does not provide this information and asks if it is possible to get an interactive node using `qsub -i`.

## Root Cause
- Lack of documentation on accessing nodes with local SSDs on tinyfat.
- Uncertainty about the functionality of `qsub -i` on different systems.

## Solution
- The user needs guidance on how to access nodes with local SSDs on tinyfat.
- Clarification on the usage of `qsub -i` for interactive nodes.

## What Can Be Learned
- Importance of clear documentation for accessing specific node types.
- Understanding the functionality and limitations of `qsub -i` across different systems.

## Next Steps
- Update the documentation to include information on accessing nodes with local SSDs.
- Provide a detailed explanation of how to use `qsub -i` for interactive sessions on tinyfat.
```
---

### 2022021842003082_new%20submission%20scripts%20for%20TinyFAT%20cluster%20for%20bca203.md
# Ticket 2022021842003082

 # HPC Support Ticket: New Submission Scripts for TinyFAT Cluster

## Subject
New submission scripts for TinyFAT cluster for ORCA jobs

## Keywords
- TinyFAT cluster
- ORCA jobs
- Torque to Slurm transition
- Submission scripts
- Resource allocation
- ORCA parallel runs

## Problem Description
The user's old submission scripts for ORCA jobs on the TinyFAT cluster stopped working after the transition from Torque to Slurm. The user attempted to replace `qsub.tinyfat -q` with `sbatch.tinyfat -p` but encountered an error message indicating that the requested node configuration was not available.

## Root Cause
- Incorrect usage of Slurm commands and options.
- Lack of understanding of how to pass job names and allocate resources in Slurm.

## Solution
### I. Passing Job Names
- The name of the script must always be the last argument for `sbatch`.
- Use the `-J` option before the script name to specify the job name.
  ```bash
  sbatch.tinyfat -p broadwell256 -J $1 broadwell256_script
  ```

### II. Resource Allocation
- For Broadwell nodes in TinyFAT, specify the number of nodes and time.
  ```bash
  #SBATCH --nodes=1
  #SBATCH --time=23:58:00
  ```
- Specify the number of processes in the ORCA input file.
- Available ORCA modules: `orca/4.2.1` and `orca/5.0.2`.
- These modules automatically load the corresponding OpenMPI module, so there is no need to load OpenMPI separately in the script.

## Documentation
- [TinyFAT Cluster Documentation](https://hpc.fau.de/systems-services/systems-documentation-instructions/clusters/tinyfat-cluster/)
- [Transition from Torque to Slurm](https://hpc.fau.de/2021/10/12/transition-of-rtx2080ti-and-v100-nodes-tg06x-tg07x-in-tinygpu-from-ubuntu-18-04-with-torque-to-ubuntu-20-04-with-slurm/)
- [ORCA Documentation](https://hpc.fau.de/systems-services/systems-documentation-instructions/special-applications-and-tips-tricks/orca/)

## Outcome
The user successfully adapted the submission scripts for Slurm and was able to run ORCA jobs on the TinyFAT cluster.

## General Learnings
- Understanding the differences between Torque and Slurm commands and options.
- Properly passing job names and allocating resources in Slurm.
- Referencing available documentation for specific clusters and applications.
- Consulting with HPC Admins for detailed guidance on script adaptation and resource allocation.
---

### 2021030342001898_A100%20nodes%20on%20TinyGPU%20cluster%20error.md
# Ticket 2021030342001898

 ```markdown
# HPC-Support Ticket: A100 Nodes on TinyGPU Cluster Error

## Subject
A100 nodes on TinyGPU cluster error

## User Issue
- **Error Message**: "Permission denied" (Exited with exit code 13)
- **Command**: `srun -M tinygpu -p a100 -N 1 --gres=gpu:a100:4 --time=24:00:00 --pty /home/hpc/iwal/iwal026h/aanet/scripts/aanet_train.sh`
- **Script Permissions**: `-rw-rw-rw- 1 iwal026h iwal 2352 Feb 17 12:35 aanet_train.sh`

## Root Cause
- The script `aanet_train.sh` is not executable.

## Solution
- **HPC Admin Suggestion**: Make the script executable.
  ```bash
  chmod +x /home/hpc/iwal/iwal026h/aanet/scripts/aanet_train.sh
  ```
- **Additional Note**: For `srun`, the script needs to be executable. For `sbatch`, it does not matter.

## Keywords
- Permission denied
- Exit code 13
- A100 GPU
- TinyGPU cluster
- srun
- Script permissions
- Executable script

## General Learning
- Ensure that scripts used with `srun` are executable.
- Use `chmod +x` to make scripts executable.
- Understand the difference between `srun` and `sbatch` regarding script permissions.
```
---

### 2021051442001104_Installation%20of%20QuSpin%20on%20TinyFAT%20cluster.md
# Ticket 2021051442001104

 To further improve the performance of your code, it might be beneficial to install Numba on the cluster. Numba is a Just-In-Time (JIT) compiler for Python that can significantly speed up the execution of Python code.

To install Numba, you can follow the instructions provided on the [Numba installation page](https://numba.readthedocs.io/en/stable/user/installing.html).

Here are the steps to install Numba on the TinyFAT cluster:

1. **Load the Python module:**
   ```bash
   module load python/3.8-anaconda
   ```

2. **Create a new conda environment:**
   ```bash
   conda create -n numba python=3.9
   ```

3. **Activate the environment:**
   ```bash
   conda activate numba
   ```

4. **Install Numba:**
   ```bash
   conda install numba
   ```

After installing Numba, you can verify the installation by running the following command:
```bash
conda list
```

This will display a list of installed packages, and you should see Numba in the list.

If you encounter any issues during the installation process, please provide the error messages and any relevant information, and we will assist you further.
---

### 2023012442000082_Frage%20zu%20Codeausf%C3%83%C2%BChrung%20auf%20Node-Local%20SSDs.md
# Ticket 2023012442000082

 ```markdown
# HPC-Support Ticket: Issue with Code Execution on Node-Local SSDs

## Keywords
- Node-Local SSDs
- Interactive Jobs
- Job Submission
- TinyGPU
- Python Script
- sbatch
- $WORKDIR
- $TMPDIR

## Problem Description
- User unable to execute code on Node-Local SSDs.
- Code runs successfully on the frontend node and in interactive jobs.
- Simple Python script ("Hello World") also fails when submitted with `sbatch`.

## User's Approach
1. Pack all necessary files into a tar archive.
2. Request an interactive job (`salloc.tinygpu -t hh:mm:ss --gres=gpu:1`).
3. Create and navigate to $WORKDIR.
4. Extract the archive into $WORKDIR.
5. Submit the job script (`sbatch --gres=gpu:1 run.sh`).

## Root Cause
- User was attempting to start jobs from within an interactive job, which is not the correct procedure.

## Solution
1. Ensure code and data are located on $WORK (network storage accessible from all nodes).
2. Submit the job from the frontend node (`sbatch --optionen myscript.sh`).
3. The job script should copy/extract relevant data to $TMPDIR before computation.
4. Perform computations using data in $TMPDIR.
5. Write results back to $WORK.

## General Learning
- Jobs should not be started from within interactive jobs.
- Use $WORK for storing code and data accessible from all nodes.
- Utilize $TMPDIR for temporary storage during job execution.
- Submit jobs from the frontend node using `sbatch`.
```
---

### 2022021142002131_Access%20to%20matlab%20modules.md
# Ticket 2022021142002131

 # HPC Support Ticket Summary

## Subject: Access to MATLAB Modules

### User Request
- **User**: Requested access to MATLAB modules for running a job.
- **Login**: pg14001h

### HPC Admin Responses
- **Initial Response**: Confirmed access to MATLAB modules on TinyFat cluster. Provided instructions to check availability via interactive job.
- **Follow-up**: Clarified differences between modules on woody frontends, memoryhog, and TinyFat. Provided links to documentation on batch processing and TinyFat cluster.
- **Interactive Job**: Suggested using `salloc.tinyfat --mem=128000 --time=01:0:0` for testing.
- **Batch Script Help**: Offered assistance in setting up batch scripts for MATLAB.

### User Issues
- **Module Availability**: Could not find MATLAB modules on woody front or memoryhog.
- **Batch Script**: Failed to run due to permission denied error.
- **MATLAB Requirements**: Needed Image Processing Toolbox and Gstreamer 1.0 or higher.

### Solutions
- **Module Access**: Confirmed MATLAB modules are available on TinyFat cluster.
- **Gstreamer**: Installed missing Gstreamer plugins specific to the video format.
- **Batch Script**: Provided general information on batch processing and examples specific to TinyFat.

### Additional Notes
- **Zoom Call**: Scheduled a Zoom call to discuss software usage and performance analysis.
- **Psychtoolbox**: Suggested installing Psychtoolbox as an additional tool.

### Outcome
- **Successful Resolution**: User confirmed that MATLAB is now working with the required toolboxes and plugins.

### Keywords
- MATLAB modules
- TinyFat cluster
- Batch processing
- Interactive job
- Image Processing Toolbox
- Gstreamer
- Psychtoolbox
- Permission denied error
- Zoom call

### General Learnings
- **Module Availability**: Different clusters may have different modules available. Always check the specific cluster documentation.
- **Batch Scripts**: Ensure proper permissions and correct commands when creating and running batch scripts.
- **Software Requirements**: Identify and install all necessary software dependencies for specific tools and functions.
- **User Support**: Offer interactive support sessions to better understand and resolve user issues.

---

This summary provides a concise overview of the support ticket, including the user's request, the HPC admin's responses, the issues encountered, the solutions provided, and the outcome. It also includes keywords and general learnings to help support employees address similar issues in the future.
---

### 2022102542001181_Enquiry%20regarding%20access%20to%20TinyFat.md
# Ticket 2022102542001181

 # HPC-Support Ticket Conversation Analysis

## Keywords
- TinyFat
- CPU access
- tinyx.nhr.fau.de
- .sh file
- error

## Summary
- **User Issue**: User attempted to access TinyFat via `tinyx.nhr.fau.de` but encountered an error due to the lack of a script in their `.sh` file.
- **Root Cause**: Missing script in the `.sh` file.

## Lessons Learned
- **Accessing TinyFat**: Users need to include a script in their `.sh` file to access TinyFat.
- **Error Handling**: Errors can occur if the `.sh` file is not properly configured with a script.

## Solution
- Ensure that the `.sh` file contains the necessary script to access TinyFat.

## Next Steps
- Provide the user with a template or example script for accessing TinyFat.
- Offer guidance on how to configure the `.sh` file correctly.

## Relevant Roles
- **HPC Admins**: Thomas, Michael Meier, Anna Kahler, Katrin Nusser, Johannes Veh
- **2nd Level Support Team**: Lacey, Dane (fo36fizy), Kuckuk, Sebastian (sisekuck), Lange, Florian (ow86apyf), Ernst, Dominik (te42kyfo), Mayr, Martin
- **Datacenter Head**: Gerhard Wellein
- **Training and Support Group Leader**: Georg Hager
- **NHR Rechenzeit Support**: Harald Lanig
- **Software and Tools Developer**: Jan Eitzinger, Gruber
---

### 42085097_Rechner%20f%C3%83%C2%BCr%20kommenden%20Samstag.md
# Ticket 42085097

 # HPC Support Ticket: Exclusive Node Reservation for Demonstration

## Keywords
- Exclusive node reservation
- TinyFat-cluster
- Memoryhog
- Conference demonstration
- Dummy job
- Node reservation
- Additional packages

## Summary
A user requested an exclusive node similar to `memoryhog` for a conference demonstration on a specific date. The user needed the node to ensure optimal performance for their prototype system, which requires significant RAM but minimal CPU usage.

## Root Cause
The user's prototype system was running on `memoryhog`, but its performance was affected by other jobs consuming CPU and RAM resources. The user needed an exclusive node to avoid performance degradation during the demonstration.

## Solution
- **Node Reservation**: An HPC Admin reserved a node (`tf011`) from the TinyFat-cluster for the user from Tuesday until the following Monday.
- **Dummy Job**: The user was advised to submit a dummy job with a long sleep duration to reserve the node exclusively.
- **Node Request**: The user was instructed to request the specific node (`tf011`) using the `qsub` command with the `-l nodes=tf011:ppn=16` option.
- **Additional Packages**: The HPC Admin noted that additional distribution packages might be needed on `tf011`, similar to those installed on `memoryhog` for the user.

## General Learnings
- **Node Reservation**: Nodes can be reserved for exclusive use by submitting a dummy job with a long sleep duration.
- **Specific Node Request**: Users can request specific nodes using the `qsub` command with the appropriate options.
- **TinyFat-cluster**: The TinyFat-cluster offers nodes with similar hardware to `memoryhog`, providing an alternative for users needing similar resources.
- **Additional Packages**: Ensure that any additional packages required by the user are installed on the reserved node to avoid compatibility issues.

## References
- [TinyFat-cluster Documentation](http://www.rrze.uni-erlangen.de/dienste/arbeiten-rechnen/hpc/systeme/memoryhog.shtml#tinyfat)
---

### 2023112442002007_Question%20about%20memory%20allocation%20-%20mpt5100h.md
# Ticket 2023112442002007

 # HPC Support Ticket: Memory Allocation for High-Memory Python Script

## Keywords
- Memory allocation
- Python script
- High memory demand
- TinyFat cluster
- Broadwell512 node
- Memoryhog node
- HPC-Cafe

## Problem
- User requires high memory (hundreds of GB) for a Python script with low CPU demand.
- Error encountered: `numpy.core._exceptions._ArrayMemoryError: Unable to allocate 1.11 TiB for an array with shape (390625, 390625) and data type float64`.
- User is unsure how to allocate large memory without occupying unnecessary cores/nodes.

## Root Cause
- The Broadwell512 node on the TinyFat cluster does not have sufficient memory for the user's requirements.
- The user's script requires more memory than available per core on the current node configuration.

## Solution
- **Memoryhog Node**: HPC Admins advised the user to use the `memoryhog` node, which has > 1 TB of memory and is suitable for high-memory jobs. Documentation can be found [here](https://hpc.fau.de/systems-services/documentation-instructions/clusters/tinyfat-cluster/).
- **Optimization**: The user was advised to look into optimizing the code to reduce memory usage. An HPC-Cafe event on Python and performance was recommended for further guidance.

## General Learnings
- **Memory-Intensive Jobs**: For jobs requiring high memory, specific nodes like `memoryhog` are available.
- **Code Optimization**: Reducing memory usage through code optimization can help in utilizing HPC resources more efficiently.
- **Equal Memory per Core**: The HPC clusters are configured to provide an equal amount of memory per core based on the node's available memory.

## Additional Resources
- [HPC-Cafe on Python and Performance](https://hpc.fau.de/2023/03/13/monthly-hpc-cafe-python-and-performance-march-21-hybrid-event/)
- [TinyFat Cluster Documentation](https://hpc.fau.de/systems-services/documentation-instructions/clusters/tinyfat-cluster/)
---

### 2022011442000478_Interactive%20Run%20Error.md
# Ticket 2022011442000478

 ```markdown
# Interactive Run Error

## Keywords
- Interactive Jobs
- srun
- salloc
- stdin error
- TinyGPU
- Debugging

## Problem Description
The user encountered an error when trying to run an interactive job using `srun` on TinyGPU. The error message was:
```
srun: error: Could not open stdin file: No such file or directory
```

## Root Cause
The root cause of the problem was the incorrect usage of the `srun` command. The user was missing the `-l` flag and using `-it` instead of `--pty`.

## Solution
The HPC Admin provided the correct command to start interactive jobs using `srun`:
```
srun.tinygpu --gres=gpu:1 --pty /bin/bash -l
```
Additionally, the HPC Admin recommended using `salloc` for interactive jobs on TinyGPU:
```
salloc.tinygpu --gres=gpu:1
```

## Lessons Learned
- Ensure the correct flags are used when running interactive jobs with `srun`.
- Use `salloc` for interactive jobs on TinyGPU as recommended by the HPC Admin.
```
---

### 2021021542003213_TinyGPU%20clusters%20with%20A100%20GPU%27s.md
# Ticket 2021021542003213

 # HPC Support Ticket: TinyGPU Clusters with A100 GPUs

## Keywords
- TinyGPU clusters
- A100 NVIDIA GPUs
- Permission denied error (Exit code 13)
- Interactive job submission
- `srun` command
- `--gres` flag

## Problem
- User received "Permission denied" (Exit code 13) error when trying to submit a job to nodes with A100 GPUs.
- User needed to specify the number of GPUs in the interactive job submission.

## Root Cause
- Typos and incorrect syntax in the `srun` command used by the user.

## Solution
- Correct the `srun` command syntax:
  - Use lowercase `srun`.
  - Use double dashes (`--`) before `gres`, `time`, and `mail-type`.
  - Specify the GPU type correctly in the `--gres` flag (`gpu:a100:#`).

Corrected command:
```bash
srun -M tinygpu -p a100 -N 1 --gres=gpu:a100:4 --time=24:00:00 --pty /bin/bash
```

## General Learnings
- Ensure accurate syntax and flags when using `srun` for job submission.
- The number of GPUs is specified by the last number in the `--gres` flag (e.g., `--gres=gpu:a100:4`).
- Double-check commands for typos and correct flag usage to avoid permission errors.
---

### 2022091542001273_Submitting%20jobs%20in%20TinyFat.md
# Ticket 2022091542001273

 # HPC Support Ticket: Submitting Jobs in TinyFat

## Keywords
- TinyFat
- Memoryhog
- Job Submission
- Qsub
- Slurm
- Interactive Session
- Batch Job
- Frontend Node

## Problem
- User attempted to access TinyFat via `ssh` to `memoryhog` and submit a job using `qsub`, which resulted in an error.

## Root Cause
- Incorrect job submission method for `memoryhog`.
- Use of deprecated `qsub` command instead of Slurm.

## Solution
- **Interactive Session on Memoryhog**:
  - Log in via `ssh` and start the application interactively.
- **Batch Job Submission**:
  - Submit batch jobs from the frontend node (`woody` or `tinyx.nhr.fau.de`).
  - Use Slurm commands instead of `qsub`.

## Documentation References
- [TinyFat Cluster Documentation](https://hpc.fau.de/systems-services/documentation-instructions/clusters/tinyfat-cluster/)
- [Batch Processing Documentation](https://hpc.fau.de/systems-services/documentation-instructions/batch-processing/)

## General Learning
- Understand the difference between interactive sessions and batch job submissions.
- Ensure the correct job submission system (Slurm) is used.
- Refer to the official documentation for detailed instructions and examples.

## Roles Involved
- **HPC Admins**: Provided guidance on job submission methods and documentation references.
- **User**: Requested assistance with job submission and accessing TinyFat.

## Next Steps
- Review the provided documentation links.
- Use Slurm commands for batch job submissions.
- For interactive sessions, log in via `ssh` and run the application directly.
---

### 2024072542001834_Issue%20with%20LLama2%20Fine-Tuning%20Using%20sbatch%20Command.md
# Ticket 2024072542001834

 # Issue with LLama2 Fine-Tuning Using sbatch Command

## Keywords
- LLama2 fine-tuning
- A100 GPUs
- sbatch command
- AttributeError
- bitsandbytes
- quantization
- interactive session

## Problem Description
The user encountered an `AttributeError` when fine-tuning LLama2 on A100 GPUs using an `sbatch` command. The error occurred upon loading a pretrained model and was related to an undefined symbol in the `bitsandbytes` library. Interestingly, the error did not occur when running the process in an interactive session.

## Root Cause
The issue likely stems from a missing `-l` flag in the `sbatch` script, which could be causing a discrepancy in the environment setup between the `sbatch` job and the interactive session.

## Solution
- Ensure that the `sbatch` script includes the necessary `-l` flag to properly load the required libraries and modules.
- Consider using a standard optimizer like `adamw_torch` instead of a quantized optimizer to avoid potential compatibility issues.
- If the problem persists, a short Zoom call with the 2nd Level Support team can be arranged to further investigate the issue.

## General Learnings
- Environment setup discrepancies between `sbatch` jobs and interactive sessions can lead to errors.
- Properly loading libraries and modules using the `-l` flag in `sbatch` scripts is crucial.
- Quantized optimizers may introduce compatibility issues, and using standard optimizers can be a viable alternative.
- Collaboration with the 2nd Level Support team can help resolve complex issues through detailed investigation.
---

### 2024041842001531_issue%20in%20HPC%20-%20iwi5088h.md
# Ticket 2024041842001531

 # HPC Support Ticket Analysis: Issue in HPC - iwi5088h

## Summary
The user encountered issues running a job on the HPC after migration. The user was previously able to run jobs using `sbatch.tinygpu run.sh`, but now faces errors. The user also tried using JupyterLab, which caused additional issues.

## Key Points Learned
1. **Job Submission**:
   - The user should submit jobs from the frontend node (`tinyx`) using `sbatch.tinygpu` for TinyGPU and `sbatch.tinyfat` for TinyFat.
   - Running jobs directly on the frontend node is not recommended for long-running tasks.

2. **JupyterLab**:
   - Submitting jobs via JupyterLab is not recommended due to resource allocation and delay issues.
   - JupyterLab sessions should be started from the list designed for the specific cluster (TinyGPU or TinyFat).

3. **Environment Setup**:
   - The user should create and activate a conda environment with the necessary Python packages.
   - CUDA is installed on GPU-based clusters and can be listed using `module list`.

4. **SSH Access**:
   - The user should use SSH to connect to the frontend node, preferably using MobaXterm on Windows.
   - SSH keys need to be created and distributed across clusters.

5. **Error Handling**:
   - The user encountered "command not found" errors when trying to run `sbatch.tinygpu` on a compute node.
   - The user also faced issues with the job not completing within the specified time and errors related to module loading.

## Root Cause of the Problem
- The user was trying to run `sbatch.tinygpu` on a compute node instead of the frontend node.
- The user's code was not properly configured to use CUDA, leading to errors when running on TinyGPU.

## Solution
- The user should run `sbatch.tinygpu` on the frontend node (`tinyx`).
- The user should ensure that the conda environment is properly set up and activated with the necessary Python packages.
- The user should check the code to ensure it is correctly configured to use CUDA.
- The user should avoid running long-running jobs directly on the frontend node to prevent automatic termination.

## Additional Resources
- [Python Environment Setup](https://doc.nhr.fau.de/environment/python-env/)
- [SSH Command Line Access](https://doc.nhr.fau.de/access/ssh-command-line/)
- [TinyGPU Cluster Documentation](https://doc.nhr.fau.de/clusters/tinygpu)

## Conclusion
The user's issues were primarily due to running commands on the wrong node and improper environment setup. By following the recommended steps for job submission and environment configuration, the user should be able to run jobs successfully on the HPC.
---

### 2022072742002557_ORCA-Jobs%20auf%20Fritz%20-%20n100af10.md
# Ticket 2022072742002557

 # HPC Support Ticket: ORCA-Jobs auf Fritz - n100af10

## Keywords
- ORCA Jobs
- Fritz
- TINYFAT
- Cores
- Memory
- Performance
- Benchmarking
- Walltime
- I/O

## Summary
The user is benchmarking ORCA jobs on the Fritz HPC system and comparing performance with TINYFAT. The user is concerned about the performance and memory usage of large jobs.

## Root Cause
- The user is experiencing lower performance on Fritz for large jobs with high I/O and RAM requirements compared to TINYFAT.
- The user is unsure about the optimal number of cores to use for ORCA jobs on Fritz.

## Solution
- The HPC Admin suggests that the user should continue to run large jobs on TINYFAT using their NHR credentials, as Fritz may not be suitable for these jobs due to memory and I/O limitations.
- For standard jobs, the user can utilize as many cores per node as possible on Fritz, as the cost is the same regardless of the number of cores used.
- The HPC Admin advises the user to check the scaling of ORCA with the number of cores using the "%pal nprocs" parameter in the ORCA input file.

## General Learnings
- Fritz nodes have 72 cores each, and users are charged for all 72 cores regardless of the number of cores requested.
- Running multiple jobs simultaneously on a single node may exceed the available memory (256 GB) and cause job failures.
- Benchmarking and comparing performance across different HPC systems is important to optimize job submission and resource allocation.
- For jobs with high I/O and memory requirements, it may be more efficient to use a specialized system like TINYFAT instead of a general-purpose system like Fritz.
---

### 2019121242002349_Zuwachs%20auf%20TinyFat%3F.md
# Ticket 2019121242002349

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject: Zuwachs auf TinyFat?

### Keywords:
- TinyFat
- Cluster status
- show-backfill.py
- Node availability
- Repository management

### Problem:
- User noticed a discrepancy between the number of free nodes listed on the HPC status page and the actual number of nodes available on TinyFat.

### Root Cause:
- The script `show-backfill.py` was not correctly reflecting the node availability on TinyFat.

### Solution:
- HPC Admin modified the `show-backfill.py` script to include specific node types and their respective RAM capacities for TinyFat.
- The script was updated to differentiate between Opteron nodes with 128 GB RAM, Broadwell nodes with 512 GB RAM, and Broadwell nodes with 256 GB RAM.

### Lessons Learned:
- Ensure that cluster status scripts accurately reflect the current state of the cluster.
- Custom modifications to scripts should be documented and, if possible, integrated into a central repository for better management and consistency.
- Regularly review and update scripts to reflect changes in cluster configuration.

### Actions Taken:
- HPC Admin patched the `show-backfill.py` script to correctly display node availability on TinyFat.
- Suggested integrating custom modifications into the `admintools-repo` for better management.

### Future Considerations:
- Consider creating a repository for cluster status scripts to ensure consistency and ease of management.
- Regularly audit and update scripts to reflect changes in cluster configuration and node availability.
```
---

### 2024081542001628_sbatch%3A%20error%3A%20Invalid%20generic%20resource%20%28gres%29%20specification%20on%20TinyGPU.md
# Ticket 2024081542001628

 # HPC Support Ticket: Invalid GRES Specification on TinyGPU

## Keywords
- `sbatch`
- `sbatch.tinygpu`
- `TinyGPU`
- `Invalid generic resource (gres) specification`
- `Downtime`
- `Job submission`

## Problem Description
- User unable to submit jobs to TinyGPU after downtime.
- Error message: `sbatch: error: Invalid generic resource (gres) specification on TinyGPU`.
- User tried all GPUs on the server with the same result.

## Root Cause
- User was using the standard `sbatch` command instead of the specific `sbatch.tinygpu` command required for TinyGPU.

## Solution
- Use `sbatch.tinygpu` instead of `sbatch` to submit jobs to TinyGPU.

## Lessons Learned
- After downtime or maintenance, specific commands or configurations may change.
- Always check for updates or changes in job submission procedures post-maintenance.
- Ensure users are aware of any command changes for specific resources like TinyGPU.

## Recommendations
- Update user documentation to reflect the use of `sbatch.tinygpu` for TinyGPU job submissions.
- Communicate any changes in job submission commands or procedures clearly to users after maintenance periods.

---

This report provides a concise overview of the issue, its root cause, and the solution, making it easier for support employees to address similar problems in the future.
---

### 2022061342003904_Submitting%20jupyter%20notebooks%20to%20TinyGPU%20nodes.md
# Ticket 2022061342003904

 # HPC Support Ticket: Submitting Jupyter Notebooks to TinyGPU Nodes

## Keywords
- JupyterHub
- TinyGPU nodes
- CUDA functionality
- Spawner
- Control panel
- Slurm job
- Python script

## Problem
- User is trying to submit a Jupyter notebook to a TinyGPU node.
- Code is executed on JupyterHub servers by default, lacking CUDA functionality.
- User cannot find the "Spawner" option to connect the notebook to a kernel running on a TinyGPU node.

## Root Cause
- The user was unaware of the process to stop the current server and start a new one on a TinyGPU node.

## Solution
- To run the notebook on JupyterHub with TinyGPU:
  1. Stop the current server via the Control Panel.
  2. Start a new server and select the option to spawn on a TinyGPU node.
- To run the code directly on TinyGPU:
  1. Convert the notebook to a generic Python script.
  2. SSH to the appropriate server (e.g., `woody.rrze.uni-erlangen.de`).
  3. Start a Slurm job with the Python script as the code to execute.

## General Learning
- Understanding the process to switch JupyterHub servers to utilize GPU nodes.
- Converting Jupyter notebooks to Python scripts for direct execution on HPC clusters.
- Using Slurm for job submission on HPC systems.
---

