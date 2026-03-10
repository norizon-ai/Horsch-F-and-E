# Topic 7: job_slurm_jobs_the_error

Number of tickets: 199

## Tickets in this topic:

### 2024012542002915_Problems%20when%20running%20an%20executable%20using%20SBATCH.md
# Ticket 2024012542002915

 # HPC Support Ticket: Problems when running an executable using SBATCH

## Keywords
- SBATCH
- SLURM
- WRF model
- Job submission
- Path error
- Script debugging

## Problem Description
The user encountered issues submitting a job via a script to run the WRF model. The job stopped suddenly without generating a log file. The interactive command worked, but the script did not.

## Root Cause
The script contained a typo in the directory path. The correct path was `/home/titan/gwgk/gwgk101h/WRF_MODEL/WRF/run/`, but the script used `/home/titan/gwgk/gwgk101h/MODEL_WRF/WRF/run/`.

## Solution
The HPC Admin identified the typo and suggested correcting the path in the script. The user confirmed that this resolved the issue.

## Lessons Learned
- Always double-check directory paths in scripts.
- Ensure consistency between interactive commands and script paths.
- Small typos can cause significant issues in job submission scripts.

## Script Example
```bash
#!/bin/bash -l
#SBATCH -o /home/titan/gwgk/gwgk101h/WRF_MODEL/WRF/test/em_real/slurm_wrf.%j.out
#SBATCH -D /home/titan/gwgk/gwgk101h/WRF_MODEL/WRF/run/em_real/
#SBATCH -J slurm_wrf
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=64
#SBATCH --cpus-per-task=1
#SBATCH --time=10:00:00
#SBATCH --export=NONE

# MPI and OpenMP settings
export SRUN_CPUS_PER_TASK=$SLURM_CPUS_PER_TASK
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
export OMP_PLACES=cores
export OMP_PROC_BIND=spread
unset SLURM_EXPORT_ENV

# WRF settings
export WRFIO_NCD_LARGE_FILE_SUPPORT=1
export WRF_EM_CORE=1
export WRF_NMM_CORE=0
export WRF_CHEM=0
ulimit -s unlimited

# Load modules
module load intel/2021.4.0
module load intelmpi/2021.6.0
module load netcdf-c/4.8.1
module load netcdf-fortran/4.5.3-intel
module load 000-all-spack-pkgs/0.17.0
module load parallel-netcdf/1.12.2-intel2021.4.0-impi
module load hdf5/1.10.7-impi-intel
module load mkl/2021.4.0

# Run job
srun /home/titan/gwgk/gwgk101h/WRF_MODEL/WRF/test/em_real/wrf.exe
```

## Conclusion
Correcting the path in the script resolved the issue, allowing the job to run successfully. This highlights the importance of accurate path specifications in job submission scripts.
---

### 2024031142003277_srun%20message.md
# Ticket 2024031142003277

 # HPC Support Ticket: srun Message

## Subject
- srun message: Job step creation temporarily disabled, retrying (Requested nodes are busy)

## Keywords
- srun
- Job step creation
- Requested nodes are busy
- Slurm
- Meggie cluster
- Fritz cluster
- Downtime

## Problem
- User encountered a warning message in recent jobs:
  ```
  srun: Job ****** step creation temporarily disabled, retrying (Requested nodes are busy)
  srun: Step created for StepId=******
  ```
- Concerned about the impact on job results.

## Troubleshooting Steps
1. **User:**
   - Checked output files, which seemed good.
   - Provided job IDs (2293478 and 2293480) and log file for investigation.

2. **HPC Admin:**
   - Confirmed no downtime for Meggie cluster.
   - Requested job IDs and log file for further investigation.
   - Analyzed the log file and found no impact on job results.

## Root Cause
- Temporary issue in Slurm where job was scheduled on nodes that were not completely ready.

## Solution
- The job ran successfully after the temporary issue was resolved.
- The warning message does not affect the correctness of the results.

## Conclusion
- Such warning messages can be ignored if the job completes successfully and output files are as expected.
- No further action is required from the user's side.

## Follow-up
- If the issue persists or causes job failures, contact HPC support for further investigation.
---

### 42012313_woody%20Cluster.md
# Ticket 42012313

 ```markdown
# HPC Support Ticket: woody Cluster

## Subject
woody Cluster

## User Message
- **Issue**: Jobs not being executed.
- **Attachment**: Data regarding the non-executed jobs.
- **Contact Information**: Provided phone number.

## HPC Admin Response
- **Action**: Marked as a duplicate of ticket #42012313.

## Keywords
- woody Cluster
- Job execution issues
- Duplicate ticket

## Lessons Learned
- **Root Cause**: Unspecified job execution issues.
- **Solution**: Not provided in this ticket; refer to ticket #42012313 for potential resolution.
- **General Learning**: Always check for duplicate tickets before creating a new one. Ensure job execution issues are thoroughly investigated and documented.
```
---

### 2019121942001015_Job%20on%20emmy%201202321%20-%20iwia019h.md
# Ticket 2019121942001015

 ```markdown
# HPC Support Ticket Analysis

## Subject: Job on emmy 1202321 - iwia019h

### Keywords:
- Job inactivity
- Job monitoring
- Job termination
- User notification

### Summary:
- **Issue**: A job (1202321) on the HPC system "emmy" showed no activity since the previous evening.
- **Notification**: HPC Admin notified the user about the inactivity.
- **User Action**: The user checked the job and confirmed it was not doing anything, then terminated the job.
- **Resolution**: The ticket was closed as resolved.

### Root Cause:
- The job was inactive and not performing any operations.

### Solution:
- The user was prompted to check the job status.
- The user confirmed the inactivity and terminated the job.

### Lessons Learned:
- Regular monitoring of job activity is essential.
- Prompt user notification can help in timely resolution of inactive jobs.
- Users should be encouraged to check and manage their job statuses regularly.

### Actions Taken:
- HPC Admin sent a notification to the user.
- The user checked and terminated the inactive job.
- The ticket was closed after confirmation of resolution.
```
---

### 2022110242003577_slurmstepd%3A%20error%3A%20cancelled%20due%20to%20timelimit.md
# Ticket 2022110242003577

 # HPC Support Ticket: slurmstepd: error: cancelled due to timelimit

## Subject
slurmstepd: error: cancelled due to timelimit

## User Description
The user is experiencing repeated job cancellations due to the time limit being reached. The error message is:
```
slurmstepd: error: cancelled due to timelimit
slurmstepd: error: *** JOB 409067 ON a0122 CANCELLED AT 2022-11-02T10:05:22 DUE TO TIME LIMIT ***
```
The affected job IDs are: 409288, 409287, 409240, 409289, 409290, 409282.

## Root Cause
The root cause of the problem is that the job's writing process at the end of the simulation takes too long, causing the job to be cancelled before it can be automatically resubmitted. Additionally, there is a potential race condition in Gromacs that causes the simulation to hang during the data exchange process.

## Solution
### Short-term Workaround
1. Add an `&` at the end of the `gmx mdrun` command to run Gromacs in the background.
2. Immediately after, add the following lines to kill the Gromacs process if it runs too long:
```bash
GMX_PID=$!
(sleep 85500; kill -HUP $GMX_PID) &
wait $GMX_PID
```
### Long-term Solution
The HPC Admins are investigating the root cause of the race condition in Gromacs. They have suggested that the issue might be related to the simulation data and have recommended running the simulation with a shorter time limit to see if the issue persists.

## Keywords
slurmstepd, cancelled due to timelimit, Gromacs, race condition, job cancellation, time limit, HPC, simulation, data exchange, deadlock

## What to Learn
- Job cancellations due to time limits can be caused by long writing processes at the end of the simulation.
- Race conditions in simulation software can cause jobs to hang and not complete properly.
- Running simulations with a shorter time limit can help diagnose race conditions.
- Adding a background process to kill the simulation if it runs too long can prevent jobs from being cancelled due to time limits.
- The `--dependency=afterany:$SLURM_JOB_ID` option can be added to the job script to ensure that the follow-up job only starts after the original job has completed.
---

### 2022012542002071_Problem%20run%20Ansys%202019R1%20components%20%28HPC%20account%3A%20iwst055h%29.md
# Ticket 2022012542002071

 # HPC Support Ticket: Problem Running Ansys 2019R1 Components

## Issue Description
- **User**: Mohammad Moataz
- **HPC Account**: iwst055h
- **Software**: Ansys 2019R1 (Fluent, CFX5Post)
- **Machine**: emmy
- **Symptoms**:
  - Long loading times (> 20 minutes) for Ansys components.
  - "Shell request failed on channel 0" error when reconnecting.
  - GUI window stuck on "Loading" screen.
  - Keyboard input not recognized in interactive job.

## Root Cause
- **Process Limitation**: The user had a restrictive limit on concurrent processes due to previous excessive usage.
- **Interactive Job Issue**: Keyboard input not recognized in interactive job on compute nodes.

## Troubleshooting Steps
1. **Detailed Description**: User provided detailed steps and machines used.
2. **Process Termination**: HPC Admin terminated all user processes on emmy frontends.
3. **Interactive Job**: User attempted to run Fluent in an interactive job using `qsub -l nodes=1:ppn=40,walltime=1:0:0 -I -X`.

## Solution
- **Process Limit Removal**: HPC Admin removed the restrictive process limit, allowing Fluent to start.
- **Interactive Job Workaround**: For the keyboard input issue, suggested copy/pasting values by mouse or switching to an interactive job on the woody cluster with the command `qsub -l nodes=1:ppn=4:any32g,walltime=1:0:0 -I -X`.

## Additional Notes
- **Documentation**: Recommended using the dedicated documentation page for Fluent: [Ansys Fluent Documentation](https://hpc.fau.de/systems-services/systems-documentation-instructions/special-applications-and-tips-tricks/ansys-fluent/).
- **Clean Disconnection**: Advised to disconnect MobaXterm cleanly to avoid lingering processes.

## Follow-up
- If the login error persists, connect via `ssh -X -vv` and send the output for further diagnosis.

## Keywords
- Ansys 2019R1
- Fluent
- CFX5Post
- emmy
- MobaXterm
- ssh -X
- Interactive Job
- Process Limit
- Keyboard Input Issue
- Documentation
- Clean Disconnection

## Lessons Learned
- Excessive process usage can lead to restrictive limits, impacting software performance.
- Interactive jobs on compute nodes may have specific issues that require workarounds.
- Clean disconnection of remote sessions is important to avoid lingering processes.
---

### 2024061242002976_Chain%20Jobs.md
# Ticket 2024061242002976

 # Chain Jobs Support Ticket

## Keywords
- Chain Jobs
- HPC-Cafe
- Submit-Skript
- SLURM

## Summary
A user inquired about detailed information on Chain Jobs after discussing it with an HPC Admin during an HPC-Cafe session.

## Root Cause
The user needed detailed information and guidance on Chain Jobs in SLURM.

## Solution
The HPC Admin provided a link to the documentation on Chain Jobs and offered to review the user's submit script if needed.

## What to Learn
- **Chain Jobs**: Understanding how to chain jobs in SLURM is crucial for advanced batch processing.
- **Documentation**: Always refer users to the official documentation for detailed information.
- **Support**: Offer to review user scripts to ensure proper implementation.

## Links
- [Chain Jobs Documentation](https://doc.nhr.fau.de/batch-processing/advanced-topics-slurm/#chain-jobs)

## Follow-up
Encourage users to reach out for further assistance if they encounter issues with their submit scripts.
---

### 2022060242002408_slurm%20%20und%20perf_event_paranoid.md
# Ticket 2022060242002408

 # HPC Support Ticket: Slurm and perf_event_paranoid

## Keywords
- Slurm
- Performance Counters
- perf_event_paranoid
- Submit Filter
- Prolog/Epilog Scripts
- LIKWID Lock

## Problem
The user is trying to convince an admin to enable performance counters for performance analysis. They are inquiring about a solution implemented with Slurm that sets `/proc/sys/kernel/perf_event_paranoid` to -1 when `--exclusive` is set.

## Solution
### Submit Filter
- The submit filter is a `job_submit.lua` plugin provided by Slurm.
- It checks if jobs with the constraint `hwperf` are submitted exclusively.
- If not, the job is rejected with an error message.

### Prolog Script
- The prolog script checks if `SLURM_JOB_CONSTRAINTS` contains `hwperf`.
- If true, it sets `/proc/sys/kernel/perf_event_paranoid` to 0.
- It also sets the LIKWID lock.

```bash
if [[ "$SLURM_JOB_CONSTRAINTS" =~ "hwperf" ]] ; then
    # Set LIKWID lock (inverse to root or $monitoring user)
    # chown $SLURM_JOB_USER /var/run/likwid.lock
    # Also grant permission to use performance counters via perf interface (e.g., with vtune)
    echo 0 > /proc/sys/kernel/perf_event_paranoid
fi
```

### Epilog Script
- The epilog script resets `/proc/sys/kernel/perf_event_paranoid` to 2 or 3.
- It also resets the LIKWID lock if necessary and cleans up user processes and temporary directories.

## Additional Notes
- Setting `perf_event_paranoid` to -1 is not recommended as it can cause kernel instability.
- The submit filter and prolog/epilog scripts do not address runtime issues like incorrect process pinning or full local disks.
- For runtime monitoring, consider implementing job-specific performance monitoring or system monitoring.

## Conclusion
The solution involves using a submit filter to ensure exclusive job submission and prolog/epilog scripts to manage performance counter permissions. This approach does not address all runtime issues, and additional monitoring may be required.
---

### 2022090642003725_Probleme%20auf%20Woody-Cluster.md
# Ticket 2022090642003725

 # HPC Support Ticket: Probleme auf Woody-Cluster

## Keywords
- Woody-Cluster
- Torque
- Slurm
- qsub
- sbatch
- ModuleNotFoundError
- Python
- Gurobipy
- PBS
- Betriebssystemversionen

## Problem Description
- User unable to start jobs on Woody-Cluster using Torque (qsub) and Slurm (sbatch) commands.
- Error messages:
  - Torque: `FATAL ERROR: cannot find required binary real.qsub or qsub`
  - Slurm:
    - `ERROR: Unable to locate a modulefile for 'torque/current'`
    - `ERROR: Unable to locate a modulefile for 'python/3.7-anaconda'`
    - `activate: No such file or directory`
    - `ModuleNotFoundError: No module named 'gurobipy'`

## Root Cause
- Recent maintenance caused issues with Torque commands.
- Module discrepancies due to different operating system versions and installed software.

## Solution
- **Torque Issue**: Log out and log back into woody3 to resolve Torque command issues.
- **Module Issues**: Update module names to match the current operating system version (e.g., use `python/3.8-anaconda` instead of `python/3.7-anaconda`).
- **Future Changes**: Note that PBS commands will only be available until 17.9. After that, only Slurm commands will be supported.

## Additional Resources
- [Transition from Woody with Ubuntu 18.04 and Torque to Woody-NG with AlmaLinux8 and Slurm](https://hpc.fau.de/2022/07/17/transition-from-woody-with-ubuntu-18-04-and-torque-to-woody-ng-with-almalinux8-and-slurm/)
- [Wartungsankündigung HPC-Systeme für den 5.9.2022](https://www.rrze.fau.de/2022/08/wartungsankuendigung-hpc-systeme-fuer-den-5-9-2022/)

## Notes
- Ensure users are aware of upcoming changes and how to adapt their job submission scripts accordingly.
- Provide guidance on module availability and compatibility with different operating system versions.
---

### 2024080542001709_NHR%40FAU%20HPC%20-%20unsolicited%20application%20as%20Sysadmin%20-%20Abatcha%20Olloh%20%28Luxenburg.md
# Ticket 2024080542001709

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject: NHR@FAU HPC - Unsolicited Application as Sysadmin

### Keywords:
- HPC Systems Engineer
- SLURM Upgrade
- Bright Computing
- Infiniband Network Topology
- Vacation Time

### Summary:
- **User**: Sent an unsolicited application for an HPC Systems Engineer position.
- **HPC Admin**: Responded with information about an upcoming sysadmin position in autumn and inquired about the user's experience with SLURM upgrades.
- **User**: Provided details about their experience with SLURM upgrades and other projects, including hardware and software installation, configuration of Bright Computing, and Infiniband network topology reconstruction.

### Key Learnings:
- **Vacation Time**: August is a main vacation time in Bavaria, which can delay responses.
- **SLURM Upgrade**: Upgrading SLURM from version 20.11 to 22.05 involves restarting `slurmdbd`, `slurmctld`, and `slurmd` on compute nodes when idle. The user documented the process for future updates.
- **Project Experience**: The user has experience with hardware and software installation, configuring Bright Computing, and reconstructing Infiniband network topology.

### Root Cause of the Problem:
- No specific problem was mentioned in the conversation. The user was seeking employment and provided details about their experience.

### Solution:
- The HPC Admin informed the user about an upcoming sysadmin position and inquired about their experience to better understand their qualifications.

### Documentation for Support Employees:
- **Vacation Time**: Be aware of vacation periods, such as August in Bavaria, which can affect response times.
- **SLURM Upgrade**: Document the process for upgrading SLURM versions to facilitate future updates.
- **Project Experience**: Consider the user's experience with hardware and software installation, configuring Bright Computing, and reconstructing Infiniband network topology when evaluating their qualifications for an HPC Systems Engineer position.
```
---

### 2018121342002232_Job%20auf%20Emmy%20_%20hpcv090h.md
# Ticket 2018121342002232

 # HPC Support Ticket Analysis

## Subject: Job auf Emmy / hpcv090h

### Keywords:
- Job deletion
- Emmy cluster
- Route-Queue
- CPU frequency
- Job requirements

### Root Cause:
- User requested a CPU frequency of 2.66 GHz for a job on the Emmy cluster, which is not supported as Emmy CPUs have a maximum fixed frequency of 2.2 GHz.

### Solution:
- The job was deleted by the HPC Admin as it could not run on the Emmy cluster due to the unsupported CPU frequency requirement.

### Lessons Learned:
- Ensure job requirements, such as CPU frequency, are compatible with the cluster's hardware specifications.
- Verify job specifications before submission to avoid job deletion and resource wastage.

### Actions Taken:
- HPC Admin deleted the job and notified the user about the incompatibility.

### Recommendations:
- Users should check the cluster's hardware capabilities before submitting jobs with specific requirements.
- Provide clear documentation on the cluster's hardware limitations to prevent such issues in the future.
---

### 2022092942002371_Woodyn-NG%20error%20-%20batch%20job%20submission.md
# Ticket 2022092942002371

 # HPC-Support Ticket: Woodyn-NG Error - Batch Job Submission

## Keywords
- Woody-NG
- Batch job submission
- sbatch error
- I/O error
- slurm debug-level
- logfile size

## Problem Description
- User unable to submit batch jobs on Woody-NG.
- Error message: `sbatch: error: Batch job submission failed: I/O error writing script/environment to file`.
- Issue reported by multiple users, indicating a global problem.

## Root Cause
- The disk was completely full due to the slurm debug-level being set to `debug3`.
- This resulted in a large logfile (approximately 30 GB) being generated the previous day.

## Solution
- Reduce the slurm debug-level to free up disk space.
- Clear or manage large logfiles to prevent disk from filling up.

## General Learnings
- High debug levels can lead to excessive logfile sizes.
- Full disks can cause I/O errors and prevent job submissions.
- Monitoring disk usage and logfile sizes is crucial for maintaining system functionality.
---

### 2024120942002934_Multiple%20executions%20within%20same%20job.md
# Ticket 2024120942002934

 ```markdown
# HPC Support Ticket: Multiple Executions Within Same Job

## Problem Description
- User observed a single job executing the same code multiple times in different processes.
- This caused errors as persistent files were being written to by multiple processes.
- Job script configuration:
  ```bash
  #!/bin/bash -l
  #SBATCH --gres=gpu:a40:1
  #SBATCH --time=24:00:00
  #SBATCH --cpus-per-task=1
  #SBATCH --export=NONE
  #SBATCH --output=/home/hpc/b187cb/b187cb15/job_outputs/%j.out
  #SBATCH --error=/home/hpc/b187cb/b187cb15/job_outputs/%j.out
  #SBATCH --mail-type=FAIL
  #SBATCH --mail-user=sebastian.griesbach@uni-wuerzburg.de
  unset SLURM_EXPORT_ENV
  export HTTPS_PROXY=http://proxy/
  module add pythoncuda cudnn
  source env/bin/activate
  srun python slurm_run_function.py $SLURM_JOB_ID $*
  ```

## Root Cause
- The job script was using `srun` to execute the Python script, which by default spawns multiple tasks based on the available resources.
- The A40 GPU provides 16 cores, leading to 16 tasks being spawned.

## Solution
- Add `--ntasks=1` to the job script to limit the number of tasks to one.
- Alternatively, call the Python script directly without using `srun`.

## Example Fix
```bash
#!/bin/bash -l
#SBATCH --gres=gpu:a40:1
#SBATCH --time=24:00:00
#SBATCH --cpus-per-task=1
#SBATCH --export=NONE
#SBATCH --output=/home/hpc/b187cb/b187cb15/job_outputs/%j.out
#SBATCH --error=/home/hpc/b187cb/b187cb15/job_outputs/%j.out
#SBATCH --mail-type=FAIL
#SBATCH --mail-user=sebastian.griesbach@uni-wuerzburg.de
unset SLURM_EXPORT_ENV
export HTTPS_PROXY=http://proxy/
module add pythoncuda cudnn
source env/bin/activate
srun --ntasks=1 python slurm_run_function.py $SLURM_JOB_ID $*
```

## Keywords
- Multiple executions
- srun
- SLURM
- Job script
- Python
- GPU
- A40
- Persistent files
- Tasks

## General Learning
- Understand the default behavior of `srun` in SLURM job scripts.
- Use `--ntasks` to control the number of tasks spawned by `srun`.
- Directly calling the script without `srun` can avoid unintended multiple executions.
```
---

### 2019012542000507_completed%20Jobs%20still%20listed%20with%20active%20node%20-%20bcpc07.md
# Ticket 2019012542000507

 ```markdown
# HPC Support Ticket: Completed Jobs Still Listed with Active Node

## Keywords
- Completed Jobs
- Active Node
- DDoS Attack
- Administrative Intervention
- Node Reset

## Problem Description
- User reported that some of their jobs on Meggie, which were completed the previous day, were still listed as completed with an active node (`squeue`).
- Jobs did not finish within the requested time.
- User suspected a connection to a recent DDoS attack.

## Root Cause
- The issue was confirmed to be related to the recent DDoS attack, as indicated by an email from an HPC Admin.

## Solution
- The problem required administrative intervention and a node reset by the HPC Admins.
- Users cannot manually end these jobs to free up the nodes.

## Lessons Learned
- Completed jobs listed with active nodes can be a symptom of a broader system issue, such as a DDoS attack.
- Administrative intervention is necessary to reset the nodes and free them up.
- Users should report such issues to the HPC support team for resolution.
```
---

### 2022061742000356_Login%20auf%20Emmy%20Cluster%20mpp3007h.md
# Ticket 2022061742000356

 # HPC-Support Ticket Conversation Analysis

## Subject: Login auf Emmy Cluster

### Keywords:
- Login issue
- Emmy Cluster
- Shutdown schedule
- Dissertation planning
- Job failures

### Summary:
- **User Issue**: Unable to login to Emmy Cluster since 00:30 the previous night.
- **Root Cause**: Two servers for `$FASTTMP` crashed, causing cascading failures on the Infiniband.
- **Impact**: Most jobs running between 2022-06-16 19:00 and 2022-06-17 09:40 experienced problems.
- **Solution**: The issue was resolved around the time the user sent the email.
- **Additional Concern**: User inquired about the shutdown schedule of the Emmy Cluster for dissertation planning.

### Detailed Information:
- **Login Issue**: The user reported being unable to login to the Emmy Cluster.
- **Cluster Status**: The HPC Admin confirmed that the issue was related to server crashes and cascading failures on the Infiniband.
- **Job Impact**: Most jobs during the affected period experienced problems, with only a few completing successfully.
- **Shutdown Schedule**: No specific shutdown schedule was provided, but it was noted that a part of Emmy is likely to remain operational until the end of August.

### Lessons Learned:
- **Monitoring and Alerts**: Importance of monitoring cluster health and setting up alerts for critical failures.
- **Communication**: Clear communication with users about cluster issues and expected downtimes.
- **User Planning**: Users should be informed about potential shutdowns to plan their work accordingly.

### Action Items:
- **Documentation**: Update documentation on handling server crashes and Infiniband failures.
- **User Notification**: Improve notification systems to inform users about cluster issues and resolutions promptly.
- **Shutdown Planning**: Provide more detailed shutdown schedules when available to help users plan their work.

### Conclusion:
The login issue was resolved, and the user was informed about the cluster's status. The conversation also highlighted the need for better communication regarding shutdown schedules to assist users in their long-term planning.
---

### 2019091942001389_Probleme%20mit%20Woody.md
# Ticket 2019091942001389

 ```markdown
# HPC-Support Ticket: Probleme mit Woody

## Keywords
- Job failure
- Output path issue
- Empty output files
- Job script
- Error messages

## Summary
A user reported that their simulations on the HPC cluster were not being computed. The issue had been ongoing for approximately 1.5 to 2 weeks. The error seemed to be related to the output path.

## Details
- **User Issue**: Simulations not being computed.
- **Error Message**: Problem with the output path.
- **Job Details**:
  - PBS Job Id: 21728.twadm1.rrze.uni-erlangen.de
  - Job Name: IN718Powdery_Sample28.0_30.0micron_v3.333_P500.0/
  - Exec host: te018/0-11
  - Exit_status=1
  - resources_used.walltime=00:00:01
  - Output files were empty.

## Communication
- **Initial Report**: User reported the issue and mentioned that the software should be fine as there were no previous problems.
- **HPC Admin Response**: Requested the job script and output files for further investigation.
- **User Follow-up**: User mentioned they would send the job script in a separate email and that the output files were empty.
- **HPC Admin Clarification**: Explained that job start/exit messages are optional and can be controlled with the `-m` parameter.
- **Resolution**: User reported that the issue was resolved.

## Root Cause
The root cause of the problem was not explicitly stated, but it was related to the output path and possibly the job script configuration.

## Solution
The user resolved the issue, likely by correcting the job script or output path configuration.

## Lessons Learned
- Always include the job script and output files when reporting issues.
- Ensure that the job script correctly handles output paths.
- Job start/exit messages can be controlled with the `-m` parameter in the job file or command line.
```
---

### 2023071342004132_Probleme%20mit%20Rechnungen%20auf%20spr1tb%20Knoten%20-%20b146dc11.md
# Ticket 2023071342004132

 ```markdown
# HPC Support Ticket: Probleme mit Rechnungen auf spr1tb Knoten

## Keywords
- Job failures
- VASP
- COMPLETED status
- No error messages
- spr1tb nodes
- Monitoring system

## Problem Description
User reports that jobs on spr1tb nodes are marked as COMPLETED in the email but are incomplete according to VASP output. No error messages are present. This issue has been observed multiple times.

## Example Job IDs
- 721993
- 721912
- 719865

## HPC Admin Response
- Investigated job timings using the monitoring system.
- Suspected overlap or consecutive execution of jobs from the same working directory.
- Asked user if jobs were executed manually or via an automated script.

## Monitoring Links
- [Job 4653829](https://monitoring.nhr.fau.de/monitoring/job/4653829)
- [Job 4657129](https://monitoring.nhr.fau.de/monitoring/job/4657129)
- [Job 4657403](https://monitoring.nhr.fau.de/monitoring/job/4657403)

## Root Cause
- Unclear, possibly related to job scheduling or overlap.

## Solution
- Not yet determined. Further investigation required.

## Next Steps
- User needs to confirm if jobs were executed manually or via an automated script.
- Further analysis of job logs and monitoring data.

## General Learning
- Job status marked as COMPLETED does not always mean the job finished successfully.
- Monitoring system can provide insights into job timings and potential overlaps.
- Importance of checking job outputs and logs even if the status indicates completion.
```
---

### 2023071742003528_Problems%20with%20HPC%20-%20iwb3011h.md
# Ticket 2023071742003528

 # HPC Support Ticket: Problems with HPC - iwb3011h

## Keywords
- HPC
- VPN
- Job submission
- Error
- `/dev/mapper/vg0-root`
- slurm-Server

## Summary
A user encountered issues submitting jobs to the HPC while connected to a VPN (American server). The problem was resolved by disconnecting from the VPN. Additionally, there was a potential issue on the HPC side with `/dev/mapper/vg0-root` being temporarily full.

## Root Cause
- User-side: Connection to a VPN (American server) interfered with job submission.
- HPC-side: Potential impact due to `/dev/mapper/vg0-root` being full.

## Solution
- User-side: Disconnect from the VPN to submit jobs successfully.
- HPC-side: Monitor and manage storage to prevent full partitions.

## Lessons Learned
- VPN connections can interfere with HPC job submissions.
- Regularly monitor HPC storage to prevent full partitions and potential service disruptions.
- Communicate with users to gather detailed information about their environment when troubleshooting.
---

### 2024092442002108_Unterst%C3%83%C2%BCtzung%20bei%20SLURM-Job%20Array%20f%C3%83%C2%BCr%20die%20Verarbeitung%20weiterer%.md
# Ticket 2024092442002108

 ```markdown
# HPC Support Ticket: Invalid Job Array Specification

## Keywords
- SLURM
- Job Array
- Invalid Job Array Specification
- MaxArraySize

## Problem Description
The user encountered an error while submitting a SLURM job array for processing MRI data. The error message was:
```
sbatch: error: Batch job submission failed: Invalid job array specification
```
The user's job array specification was:
```bash
#SBATCH --array=1001-10000%100
```

## Root Cause
The root cause of the problem was that the specified job array range exceeded the maximum allowed value for `MaxArraySize` on the HPC system. The `MaxArraySize` on the system is 10000, and the maximum allowed value is `MaxArraySize-1`.

## Solution
The HPC Admin suggested modifying the job array specification to:
```bash
#SBATCH --array=1001-9999%100
```
This adjustment ensures that the job array range does not exceed the maximum allowed value.

## General Learning
- Always check the system's `MaxArraySize` when specifying job array ranges.
- The maximum allowed value for job array indices is `MaxArraySize-1`.
- Adjust job array specifications to stay within the allowed range to avoid invalid job array specifications.
```
---

### 2017092042002076_Job%20auf%20Emmy%20h%C3%83%C2%A4ngt.md
# Ticket 2017092042002076

 ```markdown
# HPC Support Ticket: Job auf Emmy hängt

## Problem Description
- User's jobs on Emmy cluster are freezing immediately after starting the executable "lbe".
- No output or error messages are generated.
- Issue observed on specific master nodes (e0931, e1131, e1132).

## Keywords
- Job freezing
- No output
- Specific master nodes
- MPI initialization
- Infiniband issues

## Root Cause
- Possible issues with MPI initialization where some processes fail to start, causing the job to hang.
- Infiniband subnet manager issues due to a malfunctioning node affecting the network configuration.

## Troubleshooting Steps
1. **User Observations**:
   - Identified specific master nodes where jobs consistently hang.
   - Provided a list of functioning and non-functioning nodes.

2. **HPC Admin Analysis**:
   - Noted that fewer than expected 'lbe' processes were running on the problematic node.
   - Suggested that some MPI processes might be failing to start, causing the job to hang during initialization.
   - Investigated Infiniband subnet manager issues that could affect job execution.

3. **Testing on Lima**:
   - User tested similar jobs on Lima cluster with mixed results.
   - Received error messages indicating process termination (SIGTERM).

## Solution
- **Temporary Workaround**:
  - User requested to tag or exclude problematic nodes to avoid them in future job submissions.
  - HPC Admin rebooted the problematic nodes and suggested monitoring for further issues.

- **Further Investigation**:
  - HPC Admin provided job status links for detailed analysis.
  - Continued monitoring and troubleshooting of Infiniband network issues.

## Conclusion
- The issue seems to be related to MPI initialization and Infiniband network configuration.
- Temporary workaround involves excluding problematic nodes.
- Further investigation and monitoring are required to identify and resolve the root cause.
```
---

### 2022092242002991_Downtime%3F.md
# Ticket 2022092242002991

 # HPC Support Ticket: Downtime?

## Keywords
- Job submission issues
- Scheduled outage
- SSH known_hosts
- Frontend access
- Torque/PBS deprecation
- Slurm system

## Summary
Users reported issues with job submission and login problems on the Woody cluster. The root cause was identified as a change in the frontend access URL and the deprecation of the Torque/PBS job scheduler.

## Root Cause
- Change in frontend access URL from `woody.rrze.fau.de` to `woody.nhr.fau.de`.
- Deprecation of Torque/PBS job scheduler, replaced by Slurm.

## Solution
1. **Update Frontend Access:**
   - Remove the old frontend from the `~/.ssh/known_hosts` file using the command:
     ```sh
     ssh-keygen -f ~/.ssh/known_hosts -R woody.rrze.fau.de
     ```
   - Access the new frontend via `woody.nhr.fau.de`.

2. **Switch to Slurm:**
   - Users attempting to submit jobs using the deprecated Torque/PBS system should switch to the Slurm system.
   - Refer to the documentation for Slurm on the Woody cluster:
     - [Woody Cluster Documentation](https://hpc.fau.de/systems-services/documentation-instructions/clusters/woody-cluster)
     - [Batch Processing Documentation](https://hpc.fau.de/systems-services/documentation-instructions/batch-processing/)

## Additional Notes
- If login problems persist after updating the frontend access, users should provide the exact command and error message for further assistance.
- Ensure that users are aware of any scheduled outages or changes in the system configuration through regular communication.
---

### 2015073142001009_Not%20possible%20to%20delete%20job%20on%20Woody.md
# Ticket 2015073142001009

 # HPC Support Ticket: Unable to Delete Job on Woody

## Keywords
- Job deletion
- Woody queue
- qdel command
- Admin intervention

## Problem Description
- User unable to delete a specific job (2214464[].wadm1) from the Woody queue.
- Attempted commands: `/qdel 2214464[].wadm1/` and `/qdel all/`.
- Other jobs can be deleted successfully.

## Root Cause
- Unclear from the initial message, but likely an issue with job state or permissions.

## Solution
- User requested admin intervention to delete the job.
- No specific solution provided in the initial message.

## Learning Points
- Users may encounter issues deleting specific jobs even when other jobs can be deleted.
- Admin intervention may be required for certain job deletion issues.
- Further investigation needed to determine the exact cause and solution.

## Next Steps for Support
- Check job state and permissions.
- Attempt to delete the job using admin privileges.
- Document the specific cause and solution for future reference.
---

### 2020092442002526_Einreichen%20von%20Rechnungen%20%C3%83%C2%BCber%20qsub%20an%20Emmy%20funktioniert%20nicht.md
# Ticket 2020092442002526

 # HPC Support Ticket: Issue with `qsub` Command on Emmy Cluster

## Keywords
- `qsub`
- Emmy Cluster
- PBS Scripts
- Job Submission
- No Output
- Certificate Expired

## Problem Description
- User unable to submit PBS scripts using `qsub` command on Emmy Cluster.
- No output or feedback in the terminal when `qsub` command is executed.
- User has to abort the command using `Ctrl+C`.

## Root Cause
- Certificate has expired.

## Solution
- HPC Admin resolved the issue by renewing the certificate.
- User confirmed that the problem was fixed and job submission worked again.

## Lessons Learned
- Expired certificates can cause job submission issues without providing any error messages.
- Regularly check and renew certificates to prevent such issues.
- Quick communication and resolution by HPC Admin can minimize downtime for users.
---

### 2025020642001412_Increase%20runtime%20for%20batch%20jobs%20in%20SLURM.md
# Ticket 2025020642001412

 # HPC Support Ticket: Increase Runtime for Batch Jobs in SLURM

## Keywords
- SLURM
- Runtime extension
- Job submission
- Local disk usage
- Checkpointing
- Array job

## Problem
- User needs to increase the maximum runtime for SLURM jobs beyond the default 24-hour limit.
- Job involves computing permutation-based p-values for Gene Regulatory Networks (GRNs) with an estimated runtime of 100 hours per dataset.
- User has 50 datasets to process.

## Root Cause
- Default runtime limit for SLURM jobs is insufficient for the user's computational needs.
- Job involves extensive write operations, which are not optimally handled by the current file system usage.

## Solution
1. **Job Submission with Hold Option**:
   - Submit the job with the `--hold` option: `sbatch --hold jobscript`.
   - Send an email to `hpc-support@fau.de` mentioning the Job ID and cluster, along with a valid justification for the runtime extension.

2. **Local Disk Usage**:
   - Use the local disk of the compute node for jobs with many write instructions.
   - Refer to the documentation: [Node-local Job-specific Directory (TMPDIR)](https://doc.nhr.fau.de/data/filesystems/#node-local-job-specific-directory-tmpdir).

3. **Checkpointing**:
   - Users are expected to implement checkpointing to save the state of their jobs periodically.

4. **Array Job**:
   - Create an array job to manage multiple datasets efficiently.

## General Learnings
- **Runtime Extension**: Users can request a runtime extension by submitting jobs with the `--hold` option and providing a valid justification via email.
- **Local Disk Usage**: For jobs with extensive I/O operations, using the local disk of the compute node can improve performance.
- **Checkpointing**: Implementing checkpointing is crucial for long-running jobs to avoid data loss and manual restarts.
- **Array Jobs**: Using array jobs can help manage multiple similar tasks efficiently.

## References
- [Node-local Job-specific Directory (TMPDIR)](https://doc.nhr.fau.de/data/filesystems/#node-local-job-specific-directory-tmpdir)
- [SLURM Job Submission](https://slurm.schedmd.com/sbatch.html)
---

### 2024060742002799_a0632%3A%20Access%20denied%20by%20pam_slurm_adopt.md
# Ticket 2024060742002799

 # HPC Support Ticket: a0632: Access denied by pam_slurm_adopt

## Keywords
- `pam_slurm_adopt`
- `pdsh`
- `Slurm`
- `multi-node execution`
- `deepspeed`
- `job script`
- `srun hostname`
- `sleep 60`
- `project extension`
- `affiliation`

## Problem Description
- User encountered an error `a0632: Access denied by pam_slurm_adopt` when running a multi-node job using Microsoft's deepspeed and pdsh.
- The job configuration had previously worked without issues.

## Root Cause
- Some nodes took more time in the system prologue run by the Slurm daemon, causing the "no job" message by `pam_slurm_adopt`.

## Solution
- Add `sleep 60` or `srun hostname` at the beginning of the job script to ensure all nodes are ready before the framework attempts to connect to neighboring nodes via SSH.

## Additional Information
- The user's project was about to expire, and they were informed about the possibility of a 3-month extension if budget remained.
- The user was advised on affiliation requirements for publications and the formal application process for project extensions.
- The user requested and was granted a 5-day extension for a specific job.
- The user submitted a project proposal and inquired about the possibility of an informal 3-month extension if the proposal was not awarded.

## General Learnings
- Ensure all nodes are fully initialized before attempting inter-node communication in multi-node jobs.
- Be aware of project expiration dates and the process for requesting extensions.
- Understand affiliation requirements for publications resulting from HPC resource usage.

## Actions Taken by HPC Admins
- Provided a solution to the user's technical issue.
- Extended the deadline for a specific job.
- Informed the user about project extension options and affiliation requirements.
- Managed the user's project extension request.
---

### 2023101142000982_jobs%20don%27t%20complete%20or%20cancel%20on%20woodycap.md
# Ticket 2023101142000982

 # HPC Support Ticket: Jobs Don't Complete or Cancel on Woodycap

## Keywords
- Slurm
- Job Stuck
- Plugin Error
- Hash Plugin
- Timeout
- scancel
- Array Jobs

## Problem Description
- User's jobs on woodycap got stuck after completing a Python script.
- Error messages in the logs indicate issues with loading and creating hash context for the K12 plugin.
- Jobs do not respond to `scancel` commands.
- Job IDs: 2383700 and 2383748 (both array jobs).

## Error Messages
```
slurmstepd: error: Couldn't load specified plugin name for hash/k12: Incompatible plugin version
slurmstepd: error: cannot create hash context for K12
slurmstepd: error: slurm_send_node_msg: hash_g_compute: REQUEST_COMPLETE_BATCH_SCRIPT has error
slurmstepd: error: hash_g_compute: hash plugin with id:0 not exist or is not loaded
```

## Root Cause
- Recent update of Slurm caused compatibility issues with the hash plugin.

## Solution
- HPC Admins cleaned up the failing jobs.
- The issue is likely to resolve itself through job timeout.

## Lessons Learned
- Updates to Slurm can cause compatibility issues with plugins.
- Monitor job logs for plugin-related errors after updates.
- Clean up failing jobs manually if they do not respond to `scancel`.

## Future Prevention
- Ensure plugin compatibility before performing Slurm updates.
- Regularly check job logs for any recurring errors after system updates.
---

### 2019121242001411_unable%20to%20communicate%20with%20wadm1%2810.188.82.10%29.md
# Ticket 2019121242001411

 # HPC Support Ticket: Unable to Communicate with Scheduler

## Keywords
- Scheduler
- Communication Error
- Connection Refused
- qstat
- wadm1
- errno=111

## Problem Description
The user is unable to communicate with the scheduler and receives the following error messages:
- Unable to communicate with wadm1(10.188.82.10)
- Cannot connect to specified server host 'wadm1'.
- qstat: cannot connect to server wadm1 (errno=111) Connection refused
- qstat: Error (111 - Connection refused)

## Root Cause
The root cause of the problem is a connection refusal when attempting to communicate with the scheduler server (wadm1).

## Possible Causes
- Server downtime
- Network issues
- Configuration errors
- User-specific issues

## Solution
- **Check Server Status**: Verify if the scheduler server (wadm1) is up and running.
- **Network Connectivity**: Ensure there are no network issues preventing communication with the server.
- **Configuration**: Review the configuration settings for any errors.
- **User-Specific Issues**: Determine if the problem is isolated to a single user or if it affects multiple users.

## Actions Taken
- HPC Admins need to investigate the server status and network connectivity.
- If the issue is user-specific, further troubleshooting with the user's environment may be required.

## Next Steps
- If the server is down, HPC Admins should restart it.
- If network issues are detected, they should be resolved.
- If configuration errors are found, they should be corrected.
- If the issue is user-specific, the 2nd Level Support team should assist in resolving it.

## Documentation for Future Reference
This ticket can serve as a reference for similar communication errors with the scheduler. The steps outlined above should be followed to diagnose and resolve the issue.
---

### 2022122142000809_SLURM%20error%20on%20meggie.md
# Ticket 2022122142000809

 # SLURM Error on Meggie

## Keywords
- SLURM
- sbatch
- squeue
- DNS SRV lookup
- SLURM_CONF
- slurm.conf
- configless
- systemd-overrides

## Problem Description
- User encountered an error when trying to use `sbatch` and `squeue` to start a job on Meggie.
- Error messages indicated issues with DNS SRV lookup and configuration source.
- The `SLURM_CONF` variable was empty.

## Root Cause
- The SLURM configuration was not properly set up on the Meggie frontends.

## Solution
- HPC Admin copied `slurm.conf` and topology from another system (madm) to the Meggie frontends as a quick fix.
- Fixed the broken `systemd-overrides` for `slurmd`.
- Switched Meggie frontends to configless mode.

## General Learnings
- SLURM configuration issues can cause errors in job submission and queue management.
- The `SLURM_CONF` variable should point to the SLURM configuration file.
- Configless mode can simplify SLURM configuration management.
- Systemd overrides can affect SLURM daemon behavior and need to be correctly configured.

## Actions Taken
- Copied `slurm.conf` and topology to Meggie frontends.
- Fixed `systemd-overrides` for `slurmd`.
- Switched Meggie frontends to configless mode.

## Status
- The issue was resolved, and the user's request was closed.
---

### 2024080842001007_tmux%20with%20sbatch.md
# Ticket 2024080842001007

 ```markdown
# HPC Support Ticket: tmux with sbatch

## Keywords
- tmux
- sbatch
- salloc
- interactive session
- SLURM
- MPI debugging
- multiple nodes
- unstable internet connection

## Problem
- User wants to use tmux for an interactive session to handle unstable internet connection.
- User tried two methods:
  1. `salloc` in a tmux instance on the login node, but it only provides one window on compute nodes.
  2. Starting tmux with `sbatch` and attaching to the job with `srun tmux attach`. This works with one node but fails with multiple nodes, resulting in SLURM error messages.

## Root Cause
- The issue arises from attempting to use tmux with `sbatch` for multiple nodes, which leads to SLURM errors.

## Solution
- Use a tmux instance on the login node.
- Submit the job with `salloc` within one tmux window.
- Use additional tmux windows to SSH into the compute nodes of the job.
- Recommended to use the dialog server `csnhr` for direct external access.

## Additional Notes
- The login node has potential issues due to DNS round-robin.
- The user should follow the documented procedure to attach to a running job: [Attach to a Running Job](https://doc.nhr.fau.de/batch-processing/batch_system_slurm/#attach-to-a-running-job).

## Conclusion
- The user was advised to use tmux on the login node and submit the job with `salloc`, then use additional tmux windows to connect to the compute nodes.
- The ticket was closed after the user confirmed the solution worked.
```
---

### 2020112742000714_Your%20VASP%20Job%20Meggie%20%28bco132%2C%20842425%29.md
# Ticket 2020112742000714

 ```markdown
# HPC Support Ticket: VASP Job Issue

## Keywords
- VASP Job
- Meggie
- Job ID: 842425
- No Output
- Job Status

## Summary
- **Issue**: A VASP job on Meggie (job ID: 842425) is not producing any output.
- **Root Cause**: Unknown, as no response was received from the user.
- **Solution**: Not provided, as the user did not respond to the initial query.

## Lessons Learned
- Always check the status of your job if it is not producing any output.
- Ensure timely communication with HPC support to resolve issues promptly.

## Actions Taken
- HPC Admin notified the user about the issue and requested a status check.
- The ticket was closed due to no response from the user.
```
---

### 2023021042001631_Fehlermeldung%20Meggie%20-%20topology.conf%20not%20found%20on%20some%20compute%20nodes.md
# Ticket 2023021042001631

 # HPC Support Ticket: Missing `topology.conf` on Compute Nodes

## Keywords
- `topology.conf`
- `slurmstepd`
- `/var/tmp/slurmd_spool/conf-cache/`
- `No such file or directory`
- `Meggie`
- `Configuration file`

## Problem Description
User encountered an error while running a job on the Meggie cluster. The error message indicated that the `topology.conf` file was missing on some compute nodes.

```
slurmstepd: error: s_p_parse_file: unable to status file /var/tmp/slurmd_spool/conf-cache/topology.conf: No such file or directory, retrying in 1sec up to 60sec
slurmstepd: fatal: something wrong with opening/reading /var/tmp/slurmd_spool/conf-cache/topology.conf: No such file or directory
```

## Root Cause
Some Meggie compute nodes were missing the `topology.conf` configuration file.

## Solution
HPC Admins identified and resolved the issue by restoring the missing configuration file on the affected nodes.

## General Learnings
- Always provide exemplary JobIDs when reporting errors to help HPC Admins investigate the issue.
- Misconfigurations or missing files on compute nodes can lead to job failures.
- Regular maintenance and checks are essential to ensure all nodes have the correct configuration files.

## Related Troubleshooting Steps
- Check if the `topology.conf` file exists on the affected nodes.
- Verify the permissions and contents of the configuration files.
- Restart the Slurm daemon if necessary.

## Contact
For further assistance, please contact the [HPC Support](mailto:support-hpc@fau.de).
---

### 2021102842001373_A100-Jobs%20gestern%20abend%20gecrashed%3F.md
# Ticket 2021102842001373

 ```markdown
# HPC Support Ticket: A100-Jobs Crashed

## Keywords
- Job crash
- A100 jobs
- Floating-point exceptions
- Log files
- Out-of-Quota

## Summary
- **User Issue**: Four A100 jobs crashed around 22:30. Two jobs created empty log files, and two jobs crashed with floating-point exceptions (IEEE_UNDERFLOW_FLAG, IEEE_DENORMAL).
- **Job Names**: `ago[AB]_[short|long]_gamd`
- **Directory**: `/home/titan/mfbi/mfbi05/Argonaute2/`
- **Log Files**:
  - `agoA_long_gamd-119.o35829`
  - `agoA_short_gamd-119.o35827`
  - `agoB_long_gamd-119.o35828`
  - `agoB_short_gamd-118.o35826`

## Root Cause
- Possible Out-of-Quota issue on Titan (Ticket#2021102942001362).

## Solution
- No immediate solution found. Ticket closed as no obvious issue was detected.

## Lessons Learned
- Floating-point exceptions can cause job crashes.
- Empty log files may indicate job failures.
- Out-of-Quota issues can lead to job crashes and should be checked.

## Next Steps
- Monitor for similar issues and check quota status regularly.
- Investigate further if similar crashes occur.
```
---

### 2022050242000082_eine%20kurz%20Frage.md
# Ticket 2022050242000082

 ```markdown
# HPC Support Ticket: Job Submission Issue

## Keywords
- `sbatch`
- `job submission`
- `error file`
- `Python script`
- `directory path`
- `background process`

## Summary
A user encountered an issue where their job submitted via `sbatch` was not running and produced an error file. The HPC Admin provided guidance to resolve the issue.

## Root Cause
- The error file and the job submission script were from different jobs, making it difficult to diagnose the problem.
- The issue was likely caused by the use of the `&` symbol at the end of the Python call in the job script, which runs the process in the background.

## Solution
- The user was advised to remove the `&` symbol from the end of the Python call in the job script to prevent the process from running in the background.
- The user was also asked to provide the correct directory path or ensure that the error file and job script are from the same job for better diagnosis.

## Lessons Learned
- Ensure that the error file and job script provided for troubleshooting are from the same job.
- Avoid using the `&` symbol at the end of commands in job scripts to prevent background processes, which can cause issues with job execution.
- Provide clear and specific information, such as the directory path, to assist HPC Admins in diagnosing and resolving issues.
```
---

### 2021031942001484_Filesystem%2C%20Jobwarteschlage%20auf%20meggie.md
# Ticket 2021031942001484

 # HPC Support Ticket: Filesystem, Jobwarteschlage auf meggie

## Keywords
- Filesystem issues
- Job queue visibility
- Module loading in batch scripts
- SLURM environment variables

## Summary
The user encountered issues with the filesystem and job queue visibility on the HPC system. Additionally, there were problems with loading modules within batch scripts.

## Issues and Solutions

### Filesystem Issues
- **Problem:** User reported potential issues with the filesystem on the HPC system.
- **Solution:** No general filesystem problems were known. The user was asked to specify the login/compute node and the nature of the problem.

### Job Queue Visibility
- **Problem:** User could only see their own jobs in the queue using `squeue`.
- **Solution:** Users cannot see all jobs in the queue. Information about system utilization can be found in `/home/woody/STATUS.MEGGIE/{nodelist,reservationlist,switches}`.

### Module Loading in Batch Scripts
- **Problem:** User encountered an error related to missing shared libraries (`libmpi_usempif08.so.40`).
- **Root Cause:** The error was due to a missing `module load` command for the required MPI library.
- **Solution:**
  - Load the required module in the shell before running the batch script: `module load openmpi/3.1.3-gcc7.2.0+4sneqz`.
  - To ensure module loading within the batch script, use `#!/bin/bash -l` to initialize the module environment.
  - Additionally, use `#SBATCH --export=NONE` and `unset SLURM_EXPORT_ENV` to start the batch job with a clean environment.

## General Learnings
- **Filesystem Troubleshooting:** Always ask for specific details about the node and the nature of the problem.
- **Job Queue Visibility:** Users cannot see all jobs in the queue. Provide alternative methods to check system utilization.
- **Module Loading:** Ensure that the module environment is properly initialized in batch scripts. Use `#!/bin/bash -l` and manage SLURM environment variables to avoid issues with missing libraries.

## Conclusion
The issues were resolved by providing specific instructions for module loading and managing SLURM environment variables. The user confirmed that the solution worked.
---

### 2022021442000627_Qdel.md
# Ticket 2022021442000627

 # HPC Support Ticket: Qdel Issue

## Keywords
- `qdel`
- Job deletion
- Indefinite waiting time
- Job array
- Torque bug
- Node crash
- Batch system

## Problem Description
- User experiences indefinite waiting time when trying to delete a job array using `qdel`.
- Other jobs in Woody status appear to be running indefinitely.

## Root Cause
- Job arrays occasionally have bugs in Torque, causing issues with internal book-keeping.
- Nodes executing jobs may have crashed, leading to jobs appearing to run indefinitely.

## Solution
- HPC Admin cleaned up the remnants of the job array.
- Jobs will automatically disappear once the node is back up and the batch system can confirm the job is no longer running.

## General Learnings
- Job arrays in Torque can be buggy, causing issues with job deletion.
- Indefinitely running jobs in Woody status are usually due to node crashes.
- The batch system will resolve the issue once the node is back up.

## Troubleshooting Steps
1. Check if the job is part of a job array.
2. Verify if there are any known bugs with job arrays in Torque.
3. Check the status of nodes executing the jobs.
4. Wait for the node to come back up to resolve the issue automatically.
5. If necessary, contact HPC Admin for further assistance.
---

### 2021060442001087_Slurm%20job%20failed.md
# Ticket 2021060442001087

 ```markdown
# HPC Support Ticket: Slurm Job Failed

## Keywords
- Slurm
- Job Failure
- ExitCode 126
- Job Script Error
- WRF Model

## Problem Description
The user reported that their WRF model jobs on the HPC cluster were failing with an ExitCode 126, despite the error files indicating successful completion.

## Root Cause
The job script contained two lines with "~" at the end, leading to the error message: `/var/tmp/slurmd_spool/job891670/slurm_script: line 23/24: /home/hpc/gwgk/gwgk006h: Is a directory`.

## Solution
The HPC Admin advised the user to remove the two unnecessary lines with "~" from the job script.

## General Learning
- Ensure job scripts are free of extraneous or erroneous lines that could cause execution errors.
- Check job script syntax and content for potential issues when troubleshooting job failures.
```
---

### 2023121742000244_Cannot%20run%20multiple%20SLURM%20jobs%20%28AssocGrpGRES%29%20-%20b180dc22.md
# Ticket 2023121742000244

 ```markdown
# HPC Support Ticket: Cannot run multiple SLURM jobs (AssocGrpGRES)

## Keywords
- SLURM jobs
- AssocGrpGRES
- Pending jobs
- Resource restrictions
- Job ID

## Problem Description
User encountered issues submitting multiple jobs on the Alex cluster. The first job runs successfully, but subsequent jobs remain pending with the message `AssocGrpGRES`.

## Root Cause
- The exact root cause was not identified, but it was noted that the user's account and project did not have any resource restrictions applied.
- The cluster being busy could be a factor, but the `AssocGrpGRES` message was unusual.

## Solution
- HPC Admin advised the user to not cancel the job if the issue occurs again and to contact support with the job ID for further investigation.
- The issue seemed to resolve itself as the user reported that the jobs were running correctly the next day.

## General Learnings
- Jobs may not start immediately if the cluster is busy.
- Unusual messages like `AssocGrpGRES` should be investigated further by HPC Admins.
- Users should not cancel jobs prematurely and should provide job IDs for detailed investigation.

## Next Steps
- If the issue reoccurs, gather the job ID and contact HPC support for further investigation.
- Monitor the cluster's load and resource allocation to ensure smooth job scheduling.
```
---

### 2021091742003715_Slurm%20nodes.md
# Ticket 2021091742003715

 # HPC Support Ticket: Slurm Nodes Not Up After Power Outage

## Keywords
- Slurm nodes
- Power outage
- Node state down
- `sinfo` command
- Partitions: rtx3080, a100, work

## Problem Description
- **Root Cause:** Power outage caused Slurm nodes to shut down.
- **Symptoms:** Nodes in partitions `rtx3080`, `a100`, and `work` are still in a down state after the power outage.
- **User Impact:** Unable to utilize the computing resources of the affected nodes.

## Ticket Conversation
- **User:** Reported that Slurm nodes are down after a power outage and inquired about their expected uptime.
- **HPC Admin:** No response recorded in the provided conversation.

## Diagnostic Steps
- The user ran the `sinfo` command to check the node status.

## Solution
- **Expected Action:** HPC Admins need to investigate and restart the affected nodes.
- **Pending:** Awaiting update from HPC Admins on the resolution steps and estimated time for the nodes to be up.

## General Learnings
- Power outages can cause nodes to remain in a down state even after power is restored.
- The `sinfo` command is useful for checking the status of nodes and partitions.
- Communication with HPC Admins is crucial for resolving hardware-related issues.

## Next Steps for Support
- Follow up with HPC Admins for an update on the node status.
- Document the resolution steps once the issue is fixed for future reference.

---

This report provides a concise overview of the issue, diagnostic steps, and expected actions for resolving similar problems in the future.
---

### 2025022042003081_Encountered%20problem%20while%20running%20a%20job%20in%20helma%20-%20b180dc41.md
# Ticket 2025022042003081

 # HPC Support Ticket: Job Submission Issue on Helma

## Keywords
- Job submission
- Slurm
- srun
- torchrun
- Job step creation error
- Nested srun

## Problem Description
User encountered an issue while submitting a job on the Helma cluster. The job was stuck with the error message:
```
srun: Job 29701 step creation temporarily disabled, retrying (Requested nodes are busy)
```
The job did not progress for 15 minutes.

## Root Cause
The issue was caused by a nested `srun` command within the job script. The user was using `srun` to launch `torchrun`, which was not necessary as the script was already being run via `srun`.

## Solution
The HPC Admin suggested removing the nested `srun` command and directly calling `torchrun` (or `python -m torch.distributed.run`) in the job script. This resolved the "step creation" errors and allowed the job to run successfully.

## General Learnings
- Avoid nesting `srun` commands within job scripts.
- Directly call the desired command (e.g., `torchrun`) in the job script when submitting jobs via `sbatch`.
- Check for leftover `srun` processes or active Slurm steps if job submission issues occur.

## Commands Used
- `squeue`: To check the job queue.
- `scontrol show job <job_id>`: To display detailed information about a job.
- `sacct -j <job_id> --format=JobID,JobName,State,ExitCode`: To display accounting data for a job.
- `sbatch`: To submit a job script.
---

### 2021040542000295_Inaktive%20Emmy-Jobs.md
# Ticket 2021040542000295

 # HPC Support Ticket: Inactive Emmy-Jobs

## Keywords
- Emmy-Cluster
- Job Inactivity
- Performance Monitoring
- Yambo-Jobs
- Quantum-Espresso-Job
- Infiniband
- Parallel Dateisystem
- Reboot

## Problem Description
- User reported multiple jobs on the Emmy-Cluster that were accepted but not executed.
- Performance monitoring showed no/little activity.
- No program-specific output files were generated.
- Some jobs were successful, indicating the issue might be node-specific.

## Root Cause
- Logs from various Emmy nodes indicated problems with Infiniband and access to the parallel file system.

## Solution
- Systematic reboot of Emmy nodes.

## Outcome
- User confirmed that jobs were running correctly after the reboot.
- Encouraged to submit more jobs due to high availability of nodes.

## General Learnings
- Infiniband and parallel file system issues can cause job inactivity.
- Rebooting nodes can resolve such issues.
- Users should be encouraged to report issues promptly to avoid prolonged downtime.

## Actions Taken
- HPC Admin investigated logs and identified the root cause.
- Nodes were systematically rebooted to resolve the issue.
- User was informed and encouraged to submit jobs.

## Follow-up
- Monitor for similar issues in the future.
- Ensure regular maintenance and updates to prevent recurrence.
---

### 2019080642000683_issues%20with%20jobs%20on%20Emmy%20_%20bccc011h.md
# Ticket 2019080642000683

 ```markdown
# HPC Support Ticket: Issues with Jobs on Emmy

## Keywords
- Job issues
- Emmy cluster
- Floating point operations
- Infiniband communication
- System monitoring

## Summary
Several jobs on the Emmy cluster were experiencing issues where they stopped performing floating point operations and Infiniband communication after some time, despite still showing load.

## Problem Description
- Jobs stopped executing floating point operations after a few hours.
- Infiniband communication ceased.
- Examples of affected jobs: 1154306, 1154307, 1149482, 1149481, 1148373, 1148371.

## Root Cause
The exact root cause was not explicitly identified in the conversation. However, it was noted that the issue recurred, indicating a persistent problem.

## Actions Taken
- HPC Admins notified the user about the issue and provided links to job information for further investigation.
- The user acknowledged the issue but did not provide a solution.
- HPC Admins later noted that the issue recurred, as seen in system monitoring.

## Solution
No specific solution was documented in the conversation. The ticket was closed temporarily when some jobs appeared to be running correctly, but the issue resurfaced later.

## Lessons Learned
- Regular monitoring of job performance is crucial to identify and address issues promptly.
- Persistent issues may require deeper investigation and collaboration between users and HPC Admins.
- Documenting and sharing solutions to recurring problems can help in resolving similar issues in the future.
```
---

### 2020091142003442_Probleme%20mit%20qsub.md
# Ticket 2020091142003442

 ```markdown
# HPC Support Ticket: Problem with qsub

## Keywords
- qsub
- command not found
- cshpc
- cluster access
- frontend

## Problem Description
User unable to submit scripts to the cluster using `qsub`, receiving the error `-bash: qsub: command not found`.

## Root Cause
- User was attempting to run `qsub` on the `cshpc` machine, which is only a gateway for external connections and does not have the `qsub` command available.

## Solution
- User needs to connect to the appropriate frontend for the cluster they intend to use, rather than running commands directly on the `cshpc` machine.

## Lessons Learned
- Ensure users are aware of the purpose of different machines in the HPC environment.
- Provide clear instructions on how to connect to the appropriate frontend for submitting jobs.
- Verify that users understand the distinction between gateway machines and actual cluster frontends.
```
---

### 42350236_Job%20steckt%20in%20queue%20fest.md
# Ticket 42350236

 ```markdown
# HPC-Support Ticket: Job Stuck in Queue

## Keywords
- Job stuck in queue
- qdel error
- qsig error
- MOM connection issue
- Job cancellation

## Problem Description
- User unable to delete a job from the queue.
- Error message: `"qdel: Invalid request MSG=job cancel in progress 1685464.ladm1"`.
- qsig command error: `"qsig: Server could not connect to MOM 1685464.ladm1"`.
- User's cluster: lima
- User's ID: iwst177
- Job ID: 1685464

## Root Cause
- Job cancellation in progress causing qdel error.
- Server unable to connect to MOM causing qsig error.

## Solution
- Wait for the job cancellation process to complete.
- Check MOM connection and server status.

## General Learnings
- Job cancellation in progress can prevent immediate deletion.
- Server connection issues can affect job management commands.
- Always check job status and server health before attempting to delete jobs.
```
---

### 2022020942002804_module%20load%20problem%20%28%3F%29%2C%20qdel%20problem.md
# Ticket 2022020942002804

 # HPC Support Ticket Summary

## Keywords
- Module load problem
- qdel problem
- Job crash
- Module not found
- qstat discrepancy
- Job deletion hang
- Batch system error

## Issues and Resolutions

### Issue 1: Module Load Problem
- **User Report:** Changes in modules (specifically Anaconda, Clang) causing job crashes and reinitialization in different order.
- **Root Cause:** Not identified. HPC Admins confirmed no changes were made to the modules.
- **Resolution:** None. The issue remains unresolved.

### Issue 2: qdel Problem
- **User Report:** Jobs appearing in `qstat` but not on the web status page. Attempting to delete jobs with `qdel` results in indefinite hang.
- **Root Cause:** Batch system error where the system forgot the progress of array jobs.
- **Resolution:** HPC Admin manually cleaned up and deleted the broken jobs. Users cannot fix this issue themselves.

## General Learnings
- The module system on Woody is generally not updated due to the upcoming system overhaul.
- Batch system errors can cause jobs to become stuck and unresponsive to user commands.
- In case of such errors, HPC Admins may need to intervene as users cannot fix broken jobs themselves.

## Follow-up Actions
- Monitor module system for any unexpected changes.
- Keep an eye on batch system logs for errors that could indicate jobs getting stuck.
- Inform users about the upcoming system updates and the freeze on module changes.
---

### 2022040442002248_Regarding%20difficulty%20with%20Emmy%20Cluster.md
# Ticket 2022040442002248

 ```markdown
# HPC-Support Ticket: Difficulty with Emmy Cluster

## Subject
Regarding difficulty with Emmy Cluster

## Issue Description
- **User**: Facing issues with simulations on Emmy Cluster.
- **Simulation Requirements**: 200 to 480 cores or 5 to 12 nodes in parallel.
- **Problem**: Jobs are assigned the required number of nodes but are killed within a few seconds with a message indicating that the required number of slots are not available.

## Ticket Conversation

### Initial Contact
- **User**: Requested assistance with job failures on Emmy Cluster.
- **HPC Admin**: Requested job script and output for further investigation.

### Investigation
- **HPC Admin**: Noted that the issue might be related to `mpirun` and suggested further investigation.
- **HPC Admin**: Identified that at least one node had an issue causing `mpirun` to exit with an error message about not enough slots.

### Resolution
- **HPC Admin**: Rebooted the problematic nodes, which temporarily resolved the issue.
- **HPC Admin**: Triggered a reboot of all nodes on Emmy to ensure the problem was fully resolved.

### Follow-up
- **User**: Confirmed that the issue was resolved after the reboot of all nodes.
- **HPC Admin**: Requested the user to contact support again if the issue persists.

## Keywords
- Emmy Cluster
- Job failure
- Slot availability
- `mpirun`
- Node reboot

## Lessons Learned
- **Node Issues**: Sometimes individual nodes can cause job failures due to unknown issues.
- **Reboot as Solution**: Rebooting problematic nodes can temporarily resolve issues.
- **Persistent Problems**: If issues persist, a full reboot of all nodes may be necessary.
- **User Communication**: Regular updates and follow-ups with the user are crucial for resolving issues effectively.

## Root Cause
- The root cause was identified as an issue with at least one node causing `mpirun` to exit with an error message about not enough slots.

## Solution
- Rebooting the problematic nodes and eventually all nodes on Emmy resolved the issue.
```
---

### 2025020442002308_Frage%20zu%20%22slurm%22.md
# Ticket 2025020442002308

 ```markdown
# HPC Support Ticket: Frage zu "slurm"

## Summary
User encountered issues while trying to start a SLURM job on Woody, receiving a "Permission denied" error.

## Keywords
- SLURM
- Permission denied
- srun
- sbatch
- OpenMP
- Job script

## Problem
The user attempted to start a SLURM job using `srun` and received the following error:
```
slurmstepd: error: execve(): skyax-1.job: Permission denied
srun: error: w1401: task 0: Exited with exit code 13
srun: Terminating StepId=7441490.0
```

## Root Cause
The user was using `srun` to submit the job script instead of `sbatch`. Additionally, the job script was not properly formatted for SLURM.

## Solution
1. **Use `sbatch` to submit the job script:**
   ```bash
   sbatch skyax-1.job
   ```

2. **Correct the job script format:**
   ```bash
   #!/bin/bash -l
   #SBATCH --nodes=1
   #SBATCH --ntasks=1
   #SBATCH --cpus-per-task=4
   #SBATCH --time=2:00:00
   #SBATCH --export=NONE

   unset SLURM_EXPORT_ENV

   # Set number of threads to requested cpus-per-task
   export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

   cd /home/hpc/mpt2/mpt218/vault/skyax/Fy-IVP-stab05
   #module load intel64/17.0up01

   gfortran -fopenmp -o master1.exe master1.f90
   ./master1.exe
   ```

## Lessons Learned
- Use `sbatch` to submit job scripts to SLURM.
- Ensure job scripts are correctly formatted for SLURM.
- Permission issues can often be resolved by checking the submission method and script format.
```
---

### 2023010442000459_M%C3%83%C2%B6gliches%20Problem%20auf%20Fritz-Knoten%20f0858.md
# Ticket 2023010442000459

 ```markdown
# HPC Support Ticket: Possible Issue on Fritz Node f0858

## Keywords
- Amber Minimization
- Job Failure
- MPI Problem
- Node Issue
- slurmstepd Error

## Summary
A user encountered issues with Amber minimization jobs on Fritz node f0858. The jobs were canceled with an error message indicating a possible MPI problem.

## User Report
- **Issue**: Amber minimization jobs failed on node f0858.
- **Details**:
  - First attempt: Incorrect executable name, job aborted with `slurmstepd: error: *** STEP 326307.3 ON f0858 CANCELLED AT 2023-01-04T09:27:51 ***`.
  - Second attempt: Correct executable name, 7 out of 8 systems completed successfully, one failed with the same error.
  - A new job for the single failed system was successful.

## HPC Admin Response
- **Feedback**: No issues reported by other users on the same node.
- **Action**: The node will be monitored for further issues.

## Root Cause
- Possible MPI problem on node f0858.

## Solution
- Monitor the node for further issues.
- No immediate action taken as the problem did not affect other users.

## Learnings
- Intermittent job failures on specific nodes can indicate underlying issues.
- Monitoring nodes for recurring problems is essential for maintaining system stability.
- User reports of isolated issues should be taken seriously and investigated.
```
---

### 2020041742002183_how%20to%20suspend%20a%20job.md
# Ticket 2020041742002183

 # HPC Support Ticket: Suspending a Job

## Keywords
- Job suspension
- Job dependency
- qhold
- qrls
- qalter
- Job status Q

## Problem
- User wants to suspend a job (A) in the queue so it won't start even if resources are available.
- User wants another job (B) submitted later to start before job (A).

## Solution
- **Suspend a job:** Use `qhold $jobid` to set the job into a hold state.
- **Release a job:** Use `qrls $jobid` to release the job from the hold state.
- **Set job dependency:**
  - `qalter -W afterok:jobid1 $jobid`: Job starts after `jobid1` has successfully finished.
  - `qalter -W afterany:jobid1 $jobid`: Job starts after `jobid1` regardless of its exit status.

## General Learnings
- Users can control the order of job execution using job dependencies.
- Jobs can be temporarily suspended and later released using `qhold` and `qrls`.
- Job dependencies can be set using `qalter` with appropriate flags.

## Related Tags
- Job management
- Job scheduling
- Job prioritization
- Job control
---

### 42251430_job%20on%20emmy.md
# Ticket 42251430

 # HPC Support Ticket Analysis: Job Issue on Emmy

## Keywords
- nMOLDYN
- Job monitoring
- Endless loop
- Debugging
- Job extension request

## Summary
A user reported an issue with a job running nMOLDYN on the Emmy cluster. The job did not produce the expected output and seemed to be stuck. The user requested an extension of the job's runtime to 72 hours.

## Root Cause
The HPC Admin investigated the job and found that it was stuck in an endless loop. The debugger indicated that the code was hanging near line 505 in `Src/MMTK_trajectory.c`. The loop did not terminate because the variable `dx` had an unusually large value, possibly due to an error earlier in the trajectory matrix calculation.

## Solution
The job was not expected to produce meaningful results due to the endless loop. Extending the job's runtime was deemed pointless. The user was advised to check the code for errors, particularly in the trajectory matrix calculation.

## Lessons Learned
- **Job Monitoring**: Users should monitor their jobs for signs of progress.
- **Debugging**: Admins can use debuggers to identify issues in user code.
- **Code Issues**: Endless loops can be caused by unexpected variable values, often due to earlier errors in the code.
- **Communication**: Users should provide detailed information about their jobs to aid in troubleshooting.

## Follow-up Actions
- Users should review their code for potential errors and test it thoroughly before submitting long-running jobs.
- Admins should provide guidance on debugging and code optimization to help users avoid similar issues in the future.
---

### 2019020842000976_Problem%20mit%20Jobsystem%20pbspro.md
# Ticket 2019020842000976

 ```markdown
# Problem with Job System PBS Pro

## Keywords
- PBS Pro
- Job System
- Connection Error
- `cannot connect to server catstor (errno=111)`
- `qsub`
- `qstat`

## Issue Description
The user reported that the PBS Pro job system on the testfront-server was not functioning. All commands (`qsub`, `qstat`, etc.) resulted in the error message "cannot connect to server catstor (errno=111)".

## Root Cause
The root cause of the problem was a connection issue with the server `catstor`.

## Solution
No solution was provided in the conversation. Further investigation by the HPC Admins is required to diagnose and resolve the connection issue.

## General Learnings
- Connection errors with the job system can prevent commands like `qsub` and `qstat` from functioning.
- The error message `cannot connect to server catstor (errno=111)` indicates a network or server-related issue.
- HPC Admins need to investigate server connectivity and network configurations to resolve such issues.
```
---

### 2018060942000049_qdel.tinyfat%20l%C3%83%C2%B6scht%20jobs%20a.d.%20woody.md
# Ticket 2018060942000049

 # HPC Support Ticket: qdel.tinyfat Deletes Jobs on Woody

## Keywords
- qdel.tinyfat
- qsub.tinyfat
- job deletion
- job queue
- woody cluster
- tinyfat cluster
- qdel command
- torqueclientwrapper

## Summary
The user submitted jobs to the woody cluster and queued additional jobs. After submitting a job to the tinyfat cluster using `qsub.tinyfat`, the user attempted to delete the tinyfat jobs using `qdel.tinyfat all`. This resulted in an error and the deletion of all jobs (both queued and running) on the woody cluster.

## Root Cause
- The user attempted to delete jobs using `qdel.tinyfat all`, which caused an error and inadvertently deleted all jobs on the woody cluster.

## Solution
- The `torqueclientwrapper` was updated to block the command `qdel.CLUSTERNAME all` because `qdel` does not accept `ALL@pbsserver` as a valid command, making it impossible to implement cleanly.

## Lessons Learned
- Be cautious when using `qdel` commands, especially with the `all` parameter, as it can lead to unintended job deletions.
- Ensure that the correct cluster is targeted when using job management commands.
- Update and maintain the `torqueclientwrapper` to prevent unintended job deletions.

## Follow-up Actions
- Inform users about the potential risks of using `qdel` commands with the `all` parameter.
- Provide guidelines on how to safely manage job queues and deletions.
- Continuously monitor and update the `torqueclientwrapper` to prevent similar issues in the future.
---

### 2024111342000984_srun_sbatch%20commands.md
# Ticket 2024111342000984

 ```markdown
# HPC Support Ticket: srun/sbatch Commands Issue

## Keywords
- srun
- sbatch
- Slurm
- HPC Cluster
- Login Node
- Tier3 Users
- Fritz
- TinyFAT
- Introduction Sessions

## Problem
- User encountered an issue where `srun` and `sbatch` commands were not available on the login node.
- Error message: `Command 'srun' not found, but can be installed with: apt install slurm-client`.
- User did not have the right to run `apt`.

## Root Cause
- The user was attempting to use `srun` and `sbatch` on a server (csnhr) that is not a cluster frontend, thus unable to start jobs.
- The user was missing some basics for working with the HPC clusters.

## Solution
- HPC Admins recommended attending the introduction sessions for beginners and AI users.
- For jobs requiring 64 cores, HPC Admins suggested using TinyFAT and its AMD EPYC 7502 nodes.
- There is no general access to Fritz for tier3 users; the user needs to apply for access.

## Additional Information
- Introduction sessions are available in English, with questions allowed in both English and German.
- Sessions are held online via Zoom.

## Next Steps
- User should attend the introduction sessions to gain a better understanding of the HPC clusters.
- User should consider using TinyFAT for their parallel computation needs.
- User should apply for access to Fritz if necessary.
```
---

### 2023101042004622_job%20does%20not%20terminate.md
# Ticket 2023101042004622

 ```markdown
# HPC Support Ticket: Job Does Not Terminate

## Keywords
- Job termination
- Slurm error
- Security update
- Stale jobs

## Problem Description
- User reported that two jobs on the Alex cluster were canceled but did not terminate.
- Error messages included:
  - `slurmstepd: error: slurm_send_node_msg: hash_g_compute: REQUEST_COMPLETE_BATCH_SCRIPT has error`
  - `slurmstepd: error: hash_g_compute: hash plugin with id:0 not exist or is not loaded`

## Root Cause
- The issue was likely caused by a recent security update that resulted in unexpected side effects, preventing jobs from terminating correctly.

## Solution
- HPC Admins acknowledged the issue and took responsibility for manually cleaning up stale jobs.
- The user later reported that the issue had been resolved (`hat sich erledigt`).

## Lessons Learned
- Security updates can sometimes have unintended side effects on job management.
- Manual intervention may be required to clean up stale jobs after such updates.
- Users should be informed about potential issues following major updates.
```
---

### 2016100542000159_batch%20jobs%20error%20ouput.md
# Ticket 2016100542000159

 ```markdown
# HPC Support Ticket: Batch Jobs Error Output

## Keywords
- Batch jobs
- Geant4
- STDOUT/STDERR
- Redirection
- /dev/null

## Problem
- User's batch jobs (Geant4) produce extensive error messages, making the `.err` and `.out` files larger than the desired output.
- User wants to prevent the creation of these files.

## Solution
- Redirect the output and error messages to `/dev/null` to avoid creating `.err` and `.out` files.
- Refer to the `man bash` documentation, specifically the "REDIRECTION" section, for details on how to implement this.

## General Learnings
- Users can control the output and error messages of their batch jobs by redirecting them.
- The `/dev/null` device can be used to discard unwanted output.
- Always check the status of user accounts to ensure they are active and valid.

## Actions Taken
- HPC Admin verified the user's account status.
- HPC Admin provided guidance on redirecting output and error messages.
- Ticket closed as resolved.
```
---

### 2017032942000134_Batch%20System%20Down%3F.md
# Ticket 2017032942000134

 ```markdown
# HPC-Support Ticket: Batch System Down?

## Keywords
- PBS-Server
- OOM (Out of Memory)
- qsub
- Connection refused
- pollux.rrze.uni-erlangen.de
- HPC Admin
- OTRS-Ticket

## Summary
The user encountered an issue where they were unable to communicate with the PBS-Server, resulting in a connection refused error when attempting to submit a job using `qsub`.

## Root Cause
The PBS-Server crashed due to an Out of Memory (OOM) error.

## Solution
The HPC Admin identified the issue and suggested that future reports should be sent directly via email to `hpc-admin@rrze.fau.de` instead of creating an OTRS-Ticket.

## Lessons Learned
- **Communication Preference**: For quicker resolution, users should directly email `hpc-admin@rrze.fau.de` instead of creating an OTRS-Ticket.
- **Server Stability**: The PBS-Server is susceptible to OOM crashes, which can disrupt job submissions.
- **Error Identification**: Connection refused errors (errno=111) when using `qsub` can indicate server-side issues, such as an OOM crash.

## Recommendations
- Monitor the PBS-Server for memory usage to prevent OOM crashes.
- Educate users on the preferred method of reporting issues for faster resolution.
```
---

### 2018122042001471_Skript%20auf%20Emmy%20startet%20sich%20laufend%20neu.md
# Ticket 2018122042001471

 ```markdown
# HPC-Support Ticket: Skript auf Emmy startet sich laufend neu

## Summary
A user reported an issue where a script on Emmy was stuck in an endless loop, repeatedly starting and ending without producing any output. The job ID was 1030259 and it was running on node e1165. The problem started after modifying an input file (`npt_equil_xh.mdp`) by adding the line `nsttcouple = 1`.

## Keywords
- Endless loop
- Job restart
- Prolog/Epilog
- Gromacs
- GPU load
- Process leftovers
- Lustre logs

## Root Cause
The root cause of the problem was not explicitly identified in the conversation, but it was related to the modification of the input file `npt_equil_xh.mdp` by adding the line `nsttcouple = 1`.

## Symptoms
- Job repeatedly starts and ends in a loop.
- No output from the job.
- High load on the node (180+).
- Large process leftovers (80 GB).
- Strange Lustre messages in the logs.

## Solution
The HPC Admin reported that the job was restarted and seemed to be running correctly, utilizing the GPU properly. The previous issues included high load, large process leftovers, and unusual Lustre messages in the logs.

## Lessons Learned
- Modifications to input files can cause unexpected behavior in jobs.
- High load and large process leftovers can indicate issues with job execution.
- Monitoring GPU utilization can help identify if a job is running correctly.
- Checking Lustre logs can provide additional insights into job behavior.
```
---

### 2023103042001927_Query%20about%20job%20submission.md
# Ticket 2023103042001927

 ```markdown
# Query about Job Submission

## Keywords
- Job submission
- Python script
- Running job
- Slurm
- File handling

## Problem
A user wants to know if changing a Python script after submitting a job will affect the running job. The user also asks if all required files are converted to binary during job submission and if two jobs started 20 minutes apart can affect each other.

## Root Cause
The user is concerned about the impact of modifying a Python script on a running job and the potential interference between jobs.

## Solution
- **Slurm Handling**: Slurm only handles the job script submitted and does not manage other files required for the job.
- **Python Script**: Changing the Python script will not affect the running job since the script is interpreted once per run.
- **Job Interference**: Users must ensure that jobs do not interfere with each other, such as by writing to the same output file simultaneously.

## General Learning
- **Slurm's Role**: Slurm manages job scripts but not the files they depend on.
- **Python Behavior**: Python scripts are interpreted once per run, so changes to the script do not affect running jobs.
- **Job Management**: Users should manage job dependencies and outputs to avoid conflicts.
```
---

### 2021082842000879_qsub_qstat%20command%20failing.md
# Ticket 2021082842000879

 # HPC Support Ticket: qsub/qstat Command Failing

## Keywords
- qsub
- qstat
- trqauthd
- Unix socket
- Communication failure
- Daemon termination

## Problem Description
- User encountered an error while trying to submit a job using `qsub`.
- Error message indicated a failure to connect to `trqauthd` via Unix socket.
- Unable to communicate with the server `tgadm1`.

## Root Cause
- A daemon silently terminated, causing communication issues with the server.

## Solution
- HPC Admin restarted the daemon.
- `qsub` and `qstat` commands should now be working properly.

## Lessons Learned
- Daemon termination can cause communication failures with HPC servers.
- Restarting the daemon can resolve such issues.
- Users should report such errors to HPC support for quick resolution.

## Actions Taken
- HPC Admin acknowledged the issue and restarted the terminated daemon.
- User confirmed the resolution of the issue.

## Follow-up
- Monitor the daemon to prevent silent terminations in the future.
- Ensure users are aware of the support process for such issues.
---

### 2024110542003773_scontrol%20top.md
# Ticket 2024110542003773

 ```markdown
# HPC Support Ticket: Enabling `scontrol top` for Non-Privileged Users

## Keywords
- `scontrol top`
- `enable_user_top`
- Slurm configuration
- Job prioritization

## Problem
- User wants to prioritize their own jobs in the queue using `scontrol top`.
- This feature is disabled by default for non-privileged users.

## Discussion
- HPC Admins discussed enabling `enable_user_top` in the Slurm configuration.
- Concerns were raised about whether this would allow users to affect other users' jobs.
- It was determined that `enable_user_top` only allows users to modify their own jobs.

## Solution
- HPC Admins activated `enable_user_top` in the Slurm configuration.
- User confirmed that `scontrol top` now works as expected.

## General Learning
- `scontrol top` can be enabled for non-privileged users by adding `enable_user_top` to the `SchedulerParameters` configuration.
- This feature allows users to prioritize their own jobs without affecting other users' jobs.
- The impact on the user's throughput is negligible to slightly negative.
```
---

### 2025012442002317_Error%20while%20trying%20to%20run%20multi-nodes%20jobs%20on%20Alex.md
# Ticket 2025012442002317

 # HPC Support Ticket Analysis: Multi-Node Job Submission Error

## Keywords
- Multi-node job
- Slurm script
- Node count specification invalid
- QoS (Quality of Service)
- A40 nodes
- Communication patterns

## Problem Description
- User encountered an error while submitting a multi-node job on Alex:A40.
- Error message: `sbatch: error: Batch job submission failed: Node count specification invalid`.
- User suspected potential revocation of multi-node run privileges or an issue with the Slurm script.

## Slurm Script
```bash
#!/bin/bash
#SBATCH --job-name=2_nodes_allreduce
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=8
#SBATCH --cpus-per-task=16
#SBATCH --time=01:30:00
#SBATCH --output=out_2_nodes_allreduce.out
#SBATCH --error=err_2_nodes_allreduce.err
#SBATCH --exclusive
#SBATCH --gres=gpu:a40:8

unset SLURM_EXPORT_ENV
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
export SRUN_CPUS_PER_TASK=$SLURM_CPUS_PER_TASK
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/apps/SPACK/0.17.0/opt/linux-almalinux8-zen/gcc-8.4.1/nvhpc-21.11-hm4rmtk5cylmeavh7qrk6uc36t7lfxbv/Linux_x86_64/21.11/comm_libs/nccl/lib
srun ./main
```

## Solution
- HPC Admin suggested adding the QoS specification to the Slurm script:
  ```bash
  #SBATCH --qos=a40multi
  ```
- If the issue persists, the request should be forwarded to the admin team.

## Additional Information
- A40 nodes have low bandwidth and high latency (25 GbE).
- Users need to specify their communication patterns before enabling `a40multi`.

## Lessons Learned
- Ensure that the QoS is specified in the Slurm script for multi-node jobs.
- Be aware of the communication patterns and limitations of the specific nodes being used.
- If privileges are suspected to be revoked, contact the HPC Admin team for verification.

## Next Steps
- Update the Slurm script with the appropriate QoS.
- If the issue persists, escalate to the admin team for further investigation.
---

### 2023031642003322_JobLaunchFailure.md
# Ticket 2023031642003322

 ```markdown
# JobLaunchFailure

## Keywords
- JobLaunchFailure
- Slurm
- Singularity
- stdout/stderr
- Directory Permissions

## Summary
A user encountered a `JobLaunchFailure` when submitting a job using Slurm. The job immediately failed upon submission.

## Problem Description
The user submitted a job using the `sbatch` command with specific resource requests and output file paths. The job script executed a Singularity container to run a training script. The job status was immediately marked as `FAILED`.

## Root Cause
The root cause of the `JobLaunchFailure` was identified as a missing directory in the specified output path. Slurm was unable to create the stdout/stderr files because the `logs` directory did not exist in the specified path.

## Solution
Ensure that the specified output directory exists before submitting the job. Create the missing directory if necessary.

## Lessons Learned
- Always verify that the specified output directories exist before submitting jobs.
- Check directory permissions and paths to ensure Slurm can write stdout/stderr files.
- Proper directory structure is crucial for successful job execution.
```
---

### 2019032642001742_Jobs%20cannot%20be%20killed..md
# Ticket 2019032642001742

 ```markdown
# HPC Support Ticket: Jobs Cannot Be Killed

## Keywords
- Job termination
- Network absence
- License reboot
- Job IDs
- EMMY cluster

## Problem Description
- User's jobs on the EMMY cluster did not stop running after 24 hours of downtime.
- Network absence and subsequent license reboot of the corresponding program may have caused the issue.

## Root Cause
- Possible cluster-side issue preventing job termination.

## Solution
- User requested HPC Admins to kill the jobs with IDs 1077108.eadm and 1077120.eadm.

## Actions Taken
- User contacted HPC Admins for assistance in terminating the jobs.

## General Learnings
- Network issues can affect job termination.
- License reboots may impact job management.
- Users should contact HPC Admins for assistance with job termination issues.
```
---

### 2021071442000441_Kurze%20Jobs%20auf%20Meggie%20gwgi008h.md
# Ticket 2021071442000441

 # HPC Support Ticket: Short Jobs on Meggie

## Keywords
- Short jobs
- Job scripts
- SLURM
- Node exclusion
- Job scheduling

## Problem
- User submitted very short jobs on Meggie.
- These jobs were causing delays for other users, particularly developers needing to test code.

## Root Cause
- Short jobs were not excluding specific nodes reserved for short-duration jobs.

## Solution
- Add the following line to job scripts to exclude nodes reserved for longer jobs:
  ```bash
  #SBATCH --exclude=m01[01-08]
  ```
- This ensures that short jobs do not block nodes needed for longer jobs, reducing wait times for developers.

## General Learnings
- Proper node allocation is crucial for efficient job scheduling.
- SLURM directives can be used to manage job distribution effectively.
- Communication with users about best practices for job submission can improve overall system performance.

## Actions Taken
- HPC Admin provided instructions to the user on how to modify job scripts.
- User acknowledged the instructions and agreed to implement them in future job submissions.
- Ticket was closed as resolved.
---

### 2024032842002353_About%20problems%20encountered%20when%20submitting%20tasks.md
# Ticket 2024032842002353

 # HPC Support Ticket: Job Submission Issue

## Keywords
- Job submission
- sbatch
- Frontend
- Cluster
- SSH

## Problem
- User encountered issues when submitting a job using `sbatch train_dl_gips.sh` command.
- The root cause was attempting to submit the job from the dialog server instead of the cluster frontend.

## Solution
- Connect to the frontend of the desired cluster before submitting the job.
- Refer to the following documentation for cluster information and SSH connection instructions:
  - [Cluster Overview](https://doc.nhr.fau.de/clusters/overview/)
  - [SSH Command Line Access](https://doc.nhr.fau.de/access/ssh-command-line/)

## General Learning
- Ensure that job submission commands are executed from the appropriate cluster frontend.
- Familiarize with the cluster structure and access methods to avoid submission errors.
---

### 2022102842001844_Options%20batch%20script.md
# Ticket 2022102842001844

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject: Options batch script

### User Issue:
- User unable to set options in batch script using `#SBATCH` directives.
- Options are ignored, and jobs are submitted with default settings.
- User suspects recent cluster changes might be the cause.

### HPC Admin Response:
- Requested sample batch script, submission command, and job ID for further investigation.

### User Follow-Up:
- Provided job ID, command line, and batch script snippet.
- Command line used: `srun python3 /home/hpc/iwal/iwal076h/mf_tdar_estimation/scripts/tests/hello.py`
- Batch script included `#SBATCH` directives for various options.

### HPC Admin Clarification:
- Clarified that the submission command should use `sbatch` to submit the job script.

### User Resolution:
- Realized the error was using `srun` instead of `sbatch` for job submission.
- Confirmed that using `sbatch` resolved the issue with ignored options.

### Key Takeaways:
- Ensure that batch scripts are submitted using the `sbatch` command to properly interpret `#SBATCH` directives.
- Using `srun` directly will ignore `#SBATCH` directives and submit jobs with default options.

### Solution:
- Use `sbatch` to submit batch scripts with `#SBATCH` directives.
```
---

### 2022012142000213_Probleme%20auf%20Woody-Cluster.md
# Ticket 2022012142000213

 ```markdown
# HPC Support Ticket: Probleme auf Woody-Cluster

## Keywords
- Job Output
- Error Datei
- Laufzeit
- Cluster Front-End
- Shell-Skript
- Hello World

## Problem Description
- Jobs on the Woody-Cluster are not producing any output or error messages, regardless of runtime and executed code.
- Output and error files only contain a message indicating that the job's runtime has expired.
- Simple "Hello World" jobs also exhibit the same issue.
- The user's shell script, which previously worked without issues, has not been modified.

## Root Cause
- The root cause of the problem is not explicitly stated in the provided conversation.

## Solution
- No solution is provided in the conversation. Further investigation by HPC Admins or 2nd Level Support team is required.

## General Learnings
- Issues with job output and error files can affect multiple users.
- Simple test jobs like "Hello World" can help diagnose general issues with job execution.
- The problem might not be related to the user's code or shell script if it runs correctly on the cluster front-end.

## Next Steps
- HPC Admins or 2nd Level Support team should investigate the cluster's job scheduling and execution system.
- Check for any recent changes or updates to the cluster that might affect job output.
- Gather more information from other users to determine if the issue is widespread.
```
---

### 2024052142002906_Can%27t%20resolve%20slurm%20host%20on%20tinygpu.md
# Ticket 2024052142002906

 ```markdown
# HPC-Support Ticket: Can't resolve slurm host on tinygpu

## Keywords
- Slurm
- DNS SRV lookup
- Configuration source
- Batch processing
- Downtime

## Issue Description
The user reported an issue with Slurm after a scheduled downtime. The error messages indicated a problem with resolving the Slurm host and fetching the configuration source.

### Error Messages
```
sbatch: error: resolve_ctls_from_dns_srv: res_nsearch error: Unknown host
sbatch: error: fetch_config: DNS SRV lookup failed
sbatch: error: _establish_config_source: failed to fetch config
sbatch: fatal: Could not establish a configuration source
```

## Root Cause
The root cause of the problem was an issue with the DNS SRV lookup, which prevented Slurm from establishing a configuration source.

## Solution
The HPC Admins acknowledged the issue and resolved it promptly. The user confirmed that the problem was fixed.

## Lessons Learned
- **DNS SRV Lookup**: Issues with DNS SRV lookup can prevent Slurm from functioning properly.
- **Configuration Source**: Ensuring that the configuration source is correctly established is crucial for Slurm operations.
- **Post-Downtime Checks**: After scheduled downtimes, it is important to verify that all services, including Slurm, are functioning correctly.

## Actions Taken
- The HPC Admins were notified of the issue.
- The problem was identified and resolved by the HPC Admins.
- The user confirmed that the issue was fixed.

## Conclusion
This ticket highlights the importance of DNS SRV lookup and configuration source establishment for Slurm operations. Prompt resolution by the HPC Admins ensured minimal disruption to the user's workflow.
```
---

### 2022050542002673_Job%20251314%20stuck%20in%20completing%20state%20on%20node%20tg093%20%28tinyGPU%29.md
# Ticket 2022050542002673

 # HPC Support Ticket: Job Stuck in Completing State

## Keywords
- Job stuck in completing state
- Slurm update issues
- Job not ending with signals
- Slurmstepd error
- Job cancellation failed

## Problem Description
- **User Issue**: Job 251314 on node tg093 completed within the allocated walltime but is stuck in the "completing" state.
- **Error Message**: "slurmstepd-tg093: error: *** JOB 251314 STEPD TERMINATED ON tg093 AT 2022-05-05T14:00:26 DUE TO JOB NOT ENDING WITH SIGNALS ***".
- **User Actions**: Attempted to cancel the job but it did not work.

## Root Cause
- The issue is caused by a recent Slurm update.

## Solution
- **HPC Admin Response**: The HPC Admins are aware of the problem and are currently working on it. The issue is expected to occur on more nodes due to the recent Slurm update.

## General Learning
- Recent Slurm updates can cause jobs to get stuck in the "completing" state.
- Users may not have the credentials to resolve such issues and should contact HPC support.
- HPC Admins need to monitor and address issues related to Slurm updates to prevent widespread problems.

## References
- [SLURM Troubleshooting Guide](https://slurm.schedmd.com/troubleshoot.html#completing)
---

### 2019111542000785_Backfill%20Meggie.md
# Ticket 2019111542000785

 # HPC Support Ticket: Backfill Meggie

## Keywords
- Backfill
- Development Jobs
- Queue
- `bf_max_job_test`
- `bf_max_job_user`
- `slurm.conf`
- Performance

## Problem Description
- User reports that development jobs on Meggie do not start unless the queue of waiting jobs is cleared.
- Jobs remain in the queue with the message: `srun: job [job_id] queued and waiting for resources`.
- User suspects the issue might be related to the `bf_max_job_test` and `bf_max_job_user` settings in the `slurm.conf` file.

## Root Cause
- The issue is likely related to the backfill settings in the `slurm.conf` file, specifically `bf_max_job_test` and `bf_max_job_user`.

## Solution
- No immediate solution provided.
- HPC Admin indicates that the current settings have not caused problems in the past and suggests revisiting the issue if the queue becomes very full again.

## General Learnings
- Understanding the impact of backfill settings on job scheduling.
- Importance of monitoring queue behavior and adjusting settings as needed.
- Current settings are considered stable, but further investigation may be required if issues persist.

## Next Steps
- Monitor the queue for any recurring issues.
- Consider adjusting backfill settings if the queue becomes very full and the issue reoccurs.

## References
- `slurm.conf` documentation for backfill settings.
- Historical performance data for Meggie.
---

### 2024101542006646_Catching%20a%20signal%20or%20chain%20jobs.md
# Ticket 2024101542006646

 # HPC Support Ticket: Catching a Signal or Chain Jobs

## Summary
User needs to repeat calculations, waiting for each script to finish before submitting the next one. The current method involves creating and deleting indicator files to manage job dependencies. The user is trying to catch signals to handle long-running training steps but is unable to capture SIGUSR1.

## Keywords
- SLURM
- Signal Handling
- Job Dependencies
- sbatch
- srun
- SIGUSR1
- Job Chaining

## Problem
1. **Signal Handling**: User is unable to catch SIGUSR1 signal to delete an indicator file before the job ends.
2. **Job Dependencies**: Current method of managing job dependencies is inefficient.

## Root Cause
- Incorrect signal handling setup in the batch script.
- Inefficient job dependency management using indicator files.

## Solution
1. **Signal Handling**:
   - Ensure the signal handler function is correctly defined and called.
   - Use `trap` command correctly to catch the signal.
   - Example:
     ```bash
     trap 'sig_handler' SIGUSR1
     ```

2. **Job Chaining**:
   - Use SLURM job dependencies to chain jobs instead of managing indicator files.
   - Example:
     ```bash
     JOB1=$(sbatch --parsable cluster_data.sh SOME_CLUSTERING_PARAMETERS_1)
     sbatch --dependency=afterok:$JOB1 train_a_model.sh SOME_TRAINING_PARAMETERS_1
     ```

## Additional Notes
- Using `srun` inside a batch script does not make a difference in this context.
- Job chaining with dependencies is a more elegant and efficient way to manage job dependencies.

## References
- [SLURM Job Dependencies](https://doc.nhr.fau.de/batch-processing/advanced-topics-slurm/#chain-jobs-with-dependencies)

## Next Steps
- Implement job chaining with dependencies.
- If signal handling is still required, ensure the signal handler is correctly set up and debug using print statements to track the execution flow.
---

### 42090331_massive%20Ausgabe%20nach%20STDOUT%20von%20Woody-Jobs.md
# Ticket 42090331

 # HPC Support Ticket: Excessive STDOUT Output from Jobs

## Keywords
- Excessive STDOUT output
- Disk space issue
- Job script modification
- Output redirection
- Error messages

## Problem Description
- User's jobs were generating massive amounts of output to STDOUT, causing nodes to run out of disk space.
- Error messages indicating issues with reading input files were also contributing to excessive output.

## Root Cause
- The user's jobs were not properly managing STDOUT output, leading to large amounts of data being written to the nodes' disks.
- Additionally, errors in the job's input file processing were generating numerous error messages.

## Solution
1. **Reduce STDOUT Output**: Modify the job script to reduce the amount of data sent to STDOUT.
2. **Redirect Output to File**: Modify the job script to redirect STDOUT to a file, e.g., `/home/vault/mpp2/mpp113/MCProton/part19/run3543/CoSim.sh > output.${PBS_JOBID}.task1`.
3. **Fix Input File Errors**: Address the errors related to input file processing to prevent excessive error messages.

## Steps Taken
1. **Initial Communication**: HPC Admin informed the user about the issue and provided suggestions for resolution.
2. **User Acknowledgment**: The user acknowledged the issue and agreed to make the necessary changes.
3. **Verification**: HPC Admin verified that the user had implemented the changes and closed the ticket.
4. **Recurrence**: The issue recurred with additional error messages, prompting further communication and resolution.

## Lessons Learned
- Proper management of STDOUT output is crucial to prevent disk space issues on HPC nodes.
- Redirecting output to files can help manage large amounts of data generated by jobs.
- Addressing errors in job scripts can reduce excessive error messages and improve overall job performance.

## References
- HPC Services, Friedrich-Alexander-Universitaet Erlangen-Nuernberg
- Regionales RechenZentrum Erlangen (RRZE)
- [HPC Services Website](http://www.hpc.rrze.uni-erlangen.de/)
---

### 2022021142002032_Question%20regarding%20job%20processing%20error.md
# Ticket 2022021142002032

 # HPC Support Ticket: Job Processing Error

## Keywords
- Job processing error
- Log files
- PBS Job Id
- Exec host
- Post job file processing error

## Summary
A user encountered a job processing error on the Woody cluster and needed assistance accessing the log files to diagnose the issue.

## Problem
- **User Issue**: The user received an email notification about a job processing error but was unsure how to access the corresponding log files.
- **Error Message**:
  ```
  PBS Job Id: 7917118.wadm1.rrze.uni-erlangen.de
  Job Name:   nf-runJSirene_7
  Exec host:  w1330/0-3
  An error has occurred processing your job, see below.
  Post job file processing error; job 7917118.wadm1.rrze.uni-erlangen.de
  on host w1330
  ```

## Solution
- **HPC Admin Response**: The HPC Admin provided the path to the log file:
  ```
  #PBS -o /home/saturn/capn/mppi110h/work/5b/1894aa451faac17f50be9053b6d74e/.command.log
  ```
- **Action**: The user can access the log file at the specified path to diagnose the job processing error.

## General Learning
- **Log File Access**: Users can access log files for their jobs by checking the specified output path in the job script or by contacting HPC support for assistance.
- **Error Diagnosis**: Log files are crucial for diagnosing job processing errors and ensuring scripts work as expected.

## Root Cause
- The root cause of the problem was not explicitly identified in the conversation, but the user was directed to the log file for further diagnosis.

## Next Steps
- Users should check the log file at the provided path to understand the nature of the job processing error.
- If further assistance is needed, users can contact HPC support with the details from the log file.

---

This documentation can be used by support employees to assist users with similar job processing errors in the future.
---

### 2021090642001274_Torque%20failure%20on%20woody4.md
# Ticket 2021090642001274

 # HPC Support Ticket: Torque Failure on woody4

## Keywords
- `qstat`
- `socket_connect_unix failed: 15137`
- `trqauthd`
- `daemon restart`
- `certificate expired`

## Problem Description
User reported that the `qstat` command on `woodycap4.rrze.uni-erlangen.de` was failing with the error message:
```
socket_connect_unix failed: 15137
qstat: cannot connect to server (null) (errno=15137) could not connect to trqauthd
qstat: Error (15137 - could not connect to trqauthd)
```

## Root Cause
- A daemon was hanging, possibly due to an expired certificate.

## Solution
- HPC Admin restarted the hanging daemon.

## Lessons Learned
- Regularly check for expired certificates to prevent daemon hangs.
- Restarting the daemon can resolve connectivity issues with `qstat`.

## Follow-up Actions
- Monitor certificates and daemon status to prevent similar issues.
- Document the procedure for restarting the daemon for future reference.
---

### 2023121142000782_Slurm%20stop%20for%20maintenance.md
# Ticket 2023121142000782

 # HPC Support Ticket: Slurm Stop for Maintenance

## Keywords
- Slurm
- Maintenance
- Job Management
- Reservations
- StateSaveLocation

## Problem
- User needs to move HPC to a new server room.
- Wants to pause pending jobs and allow running jobs to complete.
- Newly submitted jobs should also be paused.
- After the move, all jobs should resume.

## Root Cause
- HPC cluster needs to be physically moved, requiring a complete shutdown.
- Slurm needs to manage job states during this downtime.

## Solution
- **If Slurm remains online:**
  - Use Slurm reservations with `flag=ignore_jobs` to pause new jobs while allowing running jobs to complete.
  - Reference: [Slurm Reservations](https://slurm.schedmd.com/reservations.html)

- **If Slurm is shut down:**
  - Ensure all running jobs are completed before the move.
  - Slurm stores job data in the path defined by `StateSaveLocation`.
  - Pending jobs can be restored from this location after the move.
  - Ensure all daemons (`slurmdbd`, `slurmctld`, `slurmd`) are properly shut down to avoid timeouts.

## General Learnings
- Slurm can manage job states during maintenance using reservations.
- Job data is stored in `StateSaveLocation` and can be used to restore pending jobs.
- Proper shutdown of Slurm daemons is crucial to avoid data loss or corruption.

## Next Steps
- Implement the suggested reservation method if Slurm remains online.
- If shutting down, ensure all jobs are completed and daemons are properly stopped.
- Restore pending jobs from `StateSaveLocation` after the move.

## References
- [Slurm Reservations](https://slurm.schedmd.com/reservations.html)
- Slurm Configuration: `StateSaveLocation`
---

### 2025021942000345_Fritz%20virtualgl%20does%20not%20start.md
# Ticket 2025021942000345

 # HPC Support Ticket: Fritz VirtualGL Does Not Start

## Keywords
- VirtualGL
- submitvirtualgljob.sh
- Job queued
- Remote visualization
- Slurm
- Maintenance

## Problem Description
The user reported that the command `/apps/virtualgl/submitvirtualgljob.sh --time=2:0:0` no longer works. The job is queued but never gets attributed, despite the user being able to use `salloc` without issues.

## Root Cause
The issue was caused by a problem with remote visualization following recent maintenance.

## Troubleshooting Steps
1. HPC Admin reproduced the issue and noted that the job was not starting and no log file was being written by Slurm.
2. The issue was escalated to another HPC Admin for further investigation.

## Solution
The problem was identified and fixed by the HPC Admin team. The user was advised to try again.

## General Learnings
- Maintenance can sometimes lead to unexpected issues with specific services.
- Reproducing the issue is a key step in diagnosing the problem.
- Escalation to other team members may be necessary for complex issues.
- Communicating the resolution to the user is important for maintaining transparency and trust.
---

### 2024071142003055_Files%20not%20saved%20at%20the%20end%20of%20the%20batch%20job.md
# Ticket 2024071142003055

 ```markdown
# HPC-Support Ticket: Files Not Saved at the End of the Batch Job

## Problem Description
- User's batch job completed successfully but the resulting file was not saved at the specified location.
- The job involves converting a tar.bz2 archive into a parquet archive.
- No errors were found in the error file, and quotas were not the issue.
- The job had previously run successfully with the same script.

## Script Details
### Batch Script
```bash
#!/bin/bash -l
#SBATCH --ntasks=6
#SBATCH --time=04:00:00
#SBATCH --job-name=convert_to_parquet_2016-02-29_1700_US_KNBC_Today_Show_openpose_body_hand_face
#SBATCH --export=NONE
#SBATCH -e slurm-%j.err
#SBATCH -o slurm-%j.out
unset SLURM_EXPORT_ENV
module load python
conda activate r_env
filename="2016-02-29_1700_US_KNBC_Today_Show_openpose_body_hand_face"
echo "Processing archive $filename"
# unpack into $TMPDIR
tar -xjf "/home/atuin/b105dc/data/datasets/tv/2016/2016-02/2016-02-29/$filename.tar.bz2" -C $TMPDIR
# get the path to the newly created directory
unpacked_jsons=$(find $TMPDIR -type d -name "$filename")
# pass the path to the json files to R
export UNPACKED_JSONS="$unpacked_jsons"
export FILENAME="$filename"
export MONTH="02"
export DAY="29"
# apply df_maker for normalisation of coordinates
Rscript convert_to_parquet.r
# remove the contents of $TMPDIR
rm -rf $TMPDIR/"$filename"
```

### R Script
```r
library(arrow)
# Normalize coordinates
# load the dfMaker
load("~/test/dfMaker.rda")
# load the path to the json files
jsons <- Sys.getenv("UNPACKED_JSONS")
video_name <- Sys.getenv("FILENAME")
month <- Sys.getenv("MONTH")
day <- Sys.getenv("DAY")
print("Conversion started...")
dfMaker(input.folder = jsons,
        output.file = paste0("/home/woody/sldl/sldl101h/tv_df_maker/2016/2016-", month, "/2016-", month, "-", day, "/", video_name, ".parquet"))
print("Conversion successful...")
```

## Troubleshooting Steps
1. **Check for Completion Message**: Confirmed that the job reached the "Conversion successful..." message.
2. **Memory Usage**: Suggested checking if increasing the number of cores resolves the issue.
3. **Filesystem Issues**: Asked if there might be any filesystem-related issues.

## Resolution
- The user identified the issue as a mistake on their part.
- No specific details were provided about the mistake, but the problem was resolved by the user.

## Key Takeaways
- Always check for completion messages in the output file.
- Memory usage and filesystem issues can sometimes cause unexpected behavior.
- User mistakes can often be the root cause of issues, even if the script appears correct.

## Keywords
- Batch job
- File not saved
- tar.bz2 to parquet conversion
- Memory usage
- Filesystem issues
- User mistake
```
---

### 2023101042001205_Node%20Failure%20Error.md
# Ticket 2023101042001205

 ```markdown
# Node Failure Error

## Keywords
- Node Failure
- SLURM
- Job Cancellation
- Node a0533
- Node a0632
- SLURMCTLD Log

## Summary
A user reported a job failure with an error message indicating node failure. The job was cancelled due to issues with specific nodes (a0533 and a0632). The user was advised to check the SLURMCTLD log for more details.

## Root Cause
- Node failure on nodes a0533 and a0632.

## Solution
- Check the SLURMCTLD log for detailed error information.
- Investigate the status and health of nodes a0533 and a0632.
- If necessary, contact HPC Admins for further assistance.

## General Learnings
- Node failures can cause job cancellations.
- SLURMCTLD log provides detailed information about node failures.
- Regular monitoring of node health is essential to prevent job failures.
```
---

### 42320458_Expired%20credential%20for%20user%20iwst185.md
# Ticket 42320458

 ```markdown
# Expired Credential Error on HPC Cluster

## Keywords
- Expired credentials
- Job submission error
- qsub
- HPC cluster
- Troubleshooting

## Problem Description
A user encountered an error message "Expired credentials" while attempting to submit a job on the HPC cluster using the `qsub` command. The user was able to submit jobs previously without any issues.

## Root Cause
The exact root cause of the "Expired credentials" error was not determined. The issue was intermittent and could not be reproduced by the HPC Admin.

## Troubleshooting Steps
1. **User Report**: The user reported the error after attempting to submit a job with the command `./utils/edge.bash 140 0.6259765625000000 30` and loading the `intel64/13.1up03` module.
2. **Admin Test**: The HPC Admin attempted to reproduce the issue by submitting a test job under the user's account, which succeeded without any errors.
3. **User Retry**: The user retried submitting the job after receiving the admin's response, and the job submission succeeded without any errors.

## Solution
The issue resolved itself upon retrying the job submission. No specific action was taken by the HPC Admin to fix the problem.

## Lessons Learned
- Intermittent issues can occur in HPC environments.
- Retrying the job submission can sometimes resolve transient errors.
- Detailed error reporting, including the exact commands and steps leading to the error, is crucial for effective troubleshooting.

## Next Steps
- Monitor for similar issues to identify any patterns or underlying causes.
- Encourage users to provide detailed information when reporting problems to facilitate quicker resolution.
```
---

### 2024102942004283_Node%20fail%20cause.md
# Ticket 2024102942004283

 # HPC Support Ticket: Node Fail Cause

## Keywords
- Node fail
- SLURM resource manager
- Hardware errors
- Job failure
- Log file

## Summary
A user reported a job failure due to a "Node_fail" error after a scheduled downtime. The SLURM resource manager indicated the error, but the log file did not provide additional information.

## Root Cause
The job was running on node `f2181`, which experienced hardware errors.

## Solution
The HPC Admin identified the node with hardware errors as the cause of the job failure. No specific solution was provided, but awareness of the hardware issue is noted.

## General Learnings
- Node failures can cause job interruptions and errors.
- SLURM resource manager can indicate node failures.
- Log files may not always provide detailed information about hardware-related issues.
- HPC Admins can identify the specific node causing the failure.

## Next Steps
- Monitor node `f2181` for further hardware issues.
- Consider rerunning the job on a different node if the hardware issue persists.
- Ensure regular hardware checks to prevent similar issues in the future.
---

### 2016101942001319_LIMA%20PBS%20problem%20report%2C.md
# Ticket 2016101942001319

 # HPC Support Ticket: LIMA PBS Problem Report

## Keywords
- PBS (Portable Batch System)
- qstat
- qsub
- No Permission
- Unauthorized Request
- Timeout
- Batch system software issue

## Problem Description
- User encounters intermittent issues with PBS commands (`qstat`, `qsub`) resulting in error messages:
  - `pbs_iff: cannot read reply from pbs_server No Permission.`
  - `qstat: cannot connect to server ladm1 (errno=15007) Unauthorized Request`
- Issue becomes severe, preventing job submission and status checks.

## Root Cause
- Batch system software occasionally hangs under load from starting jobs or rebooting nodes.
- The error message "No Permission" is misleading; the actual issue is a timeout due to no reply from the server.

## Solution
- Retry the `qsub`/`qstat` commands.
- No permanent fix is available as the bug has persisted for years in the batch system software.

## Notes
- The issue is a known problem with the batch system software and occurs under high load.
- Users and admins can only retry commands; there is no immediate fix.

## Ticket History
- User reports intermittent issues.
- HPC Admin confirms the problem is due to batch system software limitations.
- User reports the issue has worsened, preventing work.
- HPC Admin reiterates the known issue and suggests retrying commands.

## Follow-up Actions
- Monitor the frequency and severity of the issue.
- Consider escalating to the software vendor or community for a long-term solution.

---

This documentation is intended for HPC support employees to reference when encountering similar PBS-related issues.
---

### 2022022142002522_Two%20questions%20-%20iwi5061h.md
# Ticket 2022022142002522

 ```markdown
# HPC Support Ticket Conversation Analysis

## Subject: Two questions - iwi5061h

### Keywords:
- Connection issues
- Background job execution
- Slurm queue
- `nohub` command
- Python program
- HPC cluster

### Summary:
The user encountered two issues:
1. Connection problems with long delays.
2. Attempting to run a Python program in the background using the `nohub` command, which was not available.

### Root Cause of the Problem:
1. **Connection Issues**: The user experienced sudden connection delays without a clear cause.
2. **Background Job Execution**: The user tried to use the `nohub` command to run a Python program in the background, but the command was not recognized.

### Solution:
1. **Connection Issues**: No specific solution was provided in the conversation. Further investigation is needed.
2. **Background Job Execution**: The HPC Admin suggested using the Slurm queue to submit job scripts, which is the intended use of the cluster. Documentation links were provided for reference.

### What Can Be Learned:
- **Slurm Queue Usage**: Users should submit job scripts to the Slurm queue for background execution.
- **Documentation**: Refer to the provided documentation for detailed instructions on batch processing and cluster usage.
- **Colleague Support**: Colleagues can assist with basic Linux and Slurm operations.

### References:
- [Batch Processing Documentation](https://hpc.fau.de/systems-services/systems-documentation-instructions/batch-processing/#slurm)
- [TinyGPU Cluster Documentation](https://hpc.fau.de/systems-services/systems-documentation-instructions/clusters/tinygpu-cluster/)
```
---

### 2019041042000931_Stuck%20jobs%20auf%20Woodycap.md
# Ticket 2019041042000931

 ```markdown
# Stuck Jobs on Woodycap

## Keywords
- Stuck jobs
- qdel
- Memory usage
- Batch system
- Job cancellation
- Woodycap
- TinyEth

## Problem Description
- User reported three jobs (IDs 5709481, 5711225, 5711230) on Woodycap that could not be canceled using `qdel`.
- Error message received: "Invalid request MSG=job cancel in progress".

## Root Cause
- Jobs were consuming more than 8 GB of main memory, affecting the batch system daemons on the nodes.
- This resulted in issues with job cleanup and cancellation.

## Solution
- HPC Admins manually killed the stuck jobs.
- Recommended solutions to prevent future issues:
  - Submit jobs with the `:sl` property to ensure nodes with at least 16 GB of memory are allocated.
  - Consider moving jobs to TinyEth, which has nodes with 12 cores and 48 GB of main memory.

## Additional Information
- TinyEth allows requesting partial nodes, making `ppn=4` with 16 GB of main memory a valid option.
- Using TinyEth can help avoid memory-related issues experienced on Woodycap.

## Conclusion
- High memory usage by jobs can affect the batch system daemons, leading to issues with job cancellation.
- Allocating nodes with sufficient memory or moving to a more capable cluster can prevent these issues.
```
---

### 2022032842000608_completing%20status%20of%20node%20a0427%20on%20alex%20cluster.md
# Ticket 2022032842000608

 # HPC Support Ticket: Node Stuck in COMPLETING State

## Keywords
- COMPLETING state
- Slurm
- SIGKILL signal
- scontrol command
- unkillableStepProgram
- unkillableStepTimeout
- torch.utils.data.DataLoader
- num_workers

## Problem Description
A user reported that a job on node `a0427` of the Alex cluster was stuck in the COMPLETING state for an extended period (almost 12 hours). The user attempted to cancel the job using `scancel $JOBID`, but the action did not succeed.

## Root Cause
The user identified that the issue was caused by setting too many `num_workers` in `torch.utils.data.DataLoader`, which resulted in processes that could not be terminated with the SIGKILL signal.

## Solution
The HPC Admin rebooted the node `a0427`, which resolved the issue and brought the node back to a normal state.

## General Learnings
- When a job or node is stuck in the COMPLETING state, it may indicate that processes associated with the job cannot be terminated with the SIGKILL signal.
- The Slurm daemon on each node determines when all processes associated with a job have terminated before changing the node's state to IDLE or another appropriate state.
- If the COMPLETING state persists, the system administrator should check the processes associated with the job and change the state of the node to DOWN using the `scontrol` command, then restart the node and reset its state to IDLE.
- Slurm configuration parameters `unkillableStepProgram` and `unkillableStepTimeout` can be used to automate part of this process.
- Users should be cautious when setting the number of workers in data loaders to avoid creating unkillable processes.

## References
- [Slurm FAQ: Why is my job/node in COMPLETING state?](https://slurm.schedmd.com/faq.html#comp)
- `man slurm.conf` for more information on configuration parameters.
---

### 42221368_Re%3A%20Emmy%20pbs.md
# Ticket 42221368

 ```markdown
# HPC Support Ticket: PBS Hanging Issue

## Keywords
- PBS
- qsub
- qmgr
- Hanging
- Job Submission
- Server Restart

## Problem Description
- User reports that PBS is hanging.
- Commands `qsub -I`, `qsub jobscript`, and `qmgr -c 'p s'` hang without any output.
- `qmgr` command establishes a connection but does not proceed further.
- User had previously killed all jobs and restarted the PBS server.

## Root Cause
- Unknown; further investigation required.

## Solution
- No solution provided in the ticket.
- Further diagnostics and troubleshooting steps are needed.

## Lessons Learned
- Restarting the PBS server may not always resolve hanging issues.
- Additional diagnostic commands and logs should be checked to identify the root cause.
- Proper ticket submission is crucial for effective support.
```
---

### 2022012442002546_Jobs%20on%20Emmy%20%5Bbtr0000h%5D.md
# Ticket 2022012442002546

 ```markdown
# HPC Support Ticket: Jobs on Emmy [btr0000h]

## Keywords
- Job management
- Resource allocation
- Job cancellation
- qdel command
- Monitoring

## Problem
- User had jobs running on Emmy that requested four nodes but only used one.
- User attempted to cancel jobs using `qdel` but encountered issues with one job getting stuck.

## Root Cause
- Inefficient resource allocation: Jobs were requesting more nodes than they were using.
- Job cancellation issue: The `qdel` command for one job did not work as expected.

## Solution
- HPC Admins informed the user about the inefficient resource usage.
- User attempted to cancel jobs using `qdel`.
- HPC Admins likely canceled the stuck job as the user was unable to do so.

## Lessons Learned
- Users should be aware of the resources they request and ensure efficient usage.
- The `qdel` command is the primary method for users to cancel jobs.
- If `qdel` fails, HPC Admins can assist in canceling jobs.
```
---

### 42204323_Parametric%20Sweep%20Job.md
# Ticket 42204323

 ```markdown
# Parametric Sweep Job Issue

## Keywords
- Parametric Sweep Job
- Tasks
- End-Wert
- Abbrechen
- Ausgabedateien
- Überschneiden

## Problem Description
The user attempted to run a parametric sweep job with an end value of 40, but 39 tasks were aborted, and only the last one completed successfully. Manually adding the tasks individually worked without issues.

## Root Cause
The root cause of the problem was that the output files of the parametric sweep job were overlapping, leading to conflicts and task abortions.

## Solution
To resolve the issue, ensure that the output files of the parametric sweep job do not overlap. This can be achieved by configuring the parameters of the parametric sweep job appropriately.

## Lessons Learned
- When setting up parametric sweep jobs, it is crucial to ensure that the output files do not overlap.
- Proper configuration of the parametric sweep job parameters can prevent task abortions due to file conflicts.

## Actions Taken
- The issue was resolved over the phone by an HPC Admin.
- The user was advised to configure the parametric sweep job parameters to avoid overlapping output files.
```
---

### 2015112642001403_Node%20stuck%20on%20Woody.md
# Ticket 2015112642001403

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject: Node stuck on Woody

### Keywords:
- Stuck job
- Job deletion
- Woody node
- Job ID: job2439593[]
- User: iww807

### Problem:
- User unable to delete a job on Woody node.
- Job ID: job2439593[]

### Root Cause:
- Unspecified, but likely an issue with the job management system or node state.

### Solution:
- Not explicitly provided in the conversation snippet.
- HPC Admins need to investigate and resolve the issue.

### General Learnings:
- Users may encounter issues with job deletion.
- HPC Admins should check the job management system and node status for troubleshooting.
- Documentation on job deletion procedures and common issues can be helpful for future reference.
```
---

### 2020112742000232_TinyEth%20Jobs%20h%C3%83%C2%A4ngen.md
# Ticket 2020112742000232

 ```markdown
# HPC Support Ticket: TinyEth Jobs Hängen

## Keywords
- TinyEth
- Job Hanging
- Running State
- Walltime Exceeded
- Cancel Job

## Problem Description
- User reported jobs stuck in "running" state on TinyEth.
- Jobs have exceeded their walltime and cannot be canceled.

## Root Cause
- Jobs are not transitioning to a completed state and remain in "running" despite exceeding walltime.

## Solution
- No solution provided in the conversation.

## General Learnings
- Jobs can get stuck in the "running" state even after completion.
- Walltime exceedance does not always trigger job termination.
- Users may encounter issues canceling stuck jobs.

## Next Steps
- Investigate why jobs are not transitioning to a completed state.
- Check job scheduler logs for any errors or anomalies.
- Ensure proper handling of walltime exceedance in the job scheduler configuration.
```
---

### 2020102042003388_VASP%20job%20auf%20Emmy%20%28bctc024h%29%201360537.md
# Ticket 2020102042003388

 ```markdown
# HPC Support Ticket: VASP Job Stops Computational Activity

## Keywords
- VASP job
- Computational activity
- Job termination
- SCF steps
- No error message

## Summary
A VASP job (1360537) on the Emmy cluster stopped showing computational activity. The user confirmed that the job had stopped processing further SCF steps without any error messages.

## Root Cause
- The VASP job stopped performing SCF steps without any error messages.

## Solution
- The user terminated the job after confirming it was no longer running.

## Lessons Learned
- Regularly monitor job activity to detect stalled jobs.
- Investigate the cause of jobs stopping without error messages.
- Document any unusual behavior for future reference.

## Actions Taken
- HPC Admin notified the user about the lack of computational activity.
- User confirmed the job had stopped and terminated it.
- HPC Admin inquired about the frequency of such occurrences and any error messages.
- User reported that this was the first occurrence and no error messages were displayed.
```
---

### 42248098_cronjob%40vaultt01%20-%20daily%20-%20OK.md
# Ticket 42248098

 ```markdown
# HPC-Support Ticket: cronjob@vaultt01 - daily - OK

## Keywords
- cronjob
- logrotate
- permissions
- security
- /var/log/munin
- /etc/aliases
- newaliases

## Problem
- **Root Cause**: The `/var/log/munin` directory has insecure permissions.
- **Error Message**: `"/var/log/munin" has insecure permissions. It must be owned and be writable by root only to avoid security problems. Set the "su" directive in the config file to tell logrotate which user/group should be used for rotation.`

## Solution
- **Permissions**: Ensure that `/var/log/munin` is owned and writable by root only.
- **Configuration**: Set the "su" directive in the logrotate config file to specify the user/group for rotation.

## Additional Information
- **Alias Issue**: The root alias in `/etc/aliases` was set but `newaliases` was not called, causing emails to be sent to the wrong address (`linux@rrze` instead of `hpc-admin@rrze`).
- **Resolution**: Run `newaliases` to update the alias database.

## General Learning
- **Permissions Security**: Ensure that log directories have secure permissions to avoid security issues.
- **Logrotate Configuration**: Use the "su" directive in logrotate config to specify the correct user/group for rotation.
- **Alias Management**: After updating `/etc/aliases`, run `newaliases` to apply the changes.
```
---

### 2022062042005498_Fwd%3A%20PBS%20JOB%201655094.eadm.md
# Ticket 2022062042005498

 # HPC Support Ticket Analysis

## Subject
Fwd: PBS JOB 1655094.eadm

## Keywords
- PBS Job
- Simulation
- Error Message
- Logfiles
- Directory Names
- Leerzeichen (Spaces)

## Problem Description
User unable to start simulations on Emmy cluster. The same simulation file works on another HPC account. Error message indicates job aborted by PBS Server with `Exit_status=-9`.

## Error Details
- **PBS Job Id:** 1655094.eadm
- **Job Name:** mesh.pbs
- **Error Message:**
  ```
  Aborted by PBS Server
  Job cannot be executed
  See Administrator for help
  Exit_status=-9 resources_used.cput=00:00:00 resources_used.mem=0kb
  resources_used.vmem=0kb resources_used.walltime=00:00:00
  ```

## Logfile Analysis
- **Logfile Errors:**
  ```
  Jun 20 18:50:00 e0835 pbs_mom: LOG_ERROR::open_std_file, cannot determine filename
  Jun 20 18:50:00 e0835 pbs_mom: LOG_ERROR::open_std_file, cannot determine filename
  Jun 20 18:50:00 e0835 pbs_mom: LOG_ERROR::setup_batch_job, unable to open stdout/stderr descriptors
  ```

## Root Cause
- Possible cause: Leerzeichen (spaces) in directory names.

## Solution
- Check and remove any spaces in directory names.

## General Learning
- Ensure directory names do not contain spaces to avoid issues with job execution.
- Review logfiles for specific error messages related to file handling.

## Next Steps
- User should verify and correct directory names.
- If the issue persists, further investigation into job script and environment settings may be required.
---

### 2023020942002624_QSUB%20not%20found%20beim%20Submit%20von%20Batchjob%20auf%20TINYX.md
# Ticket 2023020942002624

 # HPC Support Ticket: QSUB not found beim Submit von Batchjob auf TINYX

## Keywords
- qsub
- Slurm
- Torque
- tcsh
- Gaussian
- Woody
- TinyX
- Batch job
- Shell

## Problem Description
- User unable to submit batch jobs on TinyX after system migration.
- Error message: "FATAL Error: real.qsub or qsub not found."
- User previously used Woody3 with Ubuntu 18.04 and Torque.

## Root Cause
- The batch system on all HPC systems was unified to Slurm last summer.
- The use of (t)csh shell is no longer supported on Woody.
- The user's scripts and environment were not updated to reflect these changes.

## Solution
- Update batch scripts to use Slurm instead of Torque.
- Refer to the transition guide: [Transition from Woody with Ubuntu 18.04 and Torque to Woody NG with AlmaLinux8 and Slurm](https://hpc.fau.de/2022/07/17/transition-from-woody-with-ubuntu-18-04-and-torque-to-woody-ng-with-almalinux8-and-slurm/)
- Contact the relevant support person (in this case, for Gaussian, it is a specific admin) for assistance with specific software installations and scripts.

## General Learnings
- Always check for system-wide changes and updates after migrations.
- Update batch scripts and environment settings to comply with new system configurations.
- Refer to official transition guides and documentation for detailed instructions.
- Contact specific support personnel for software-specific issues.
---

### 2022081042003246_Exitcode%201.md
# Ticket 2022081042003246

 ```markdown
# HPC Support Ticket: Exitcode 1

## Keywords
- Exitcode 1
- Slurm Job Failure
- STDOUT/STDERR
- Job Output Files

## Problem Description
- User received an email notification about a failed Slurm job with ExitCode 1 but without detailed content.
- User seeks information on exit codes and how to determine the exact failure result.

## Root Cause
- The job script encountered an error, resulting in ExitCode 1.

## Solution
- **Output Files**: STDOUT/STDERR from batch jobs are redirected to output files, typically named as `jobname + ".o" + jobid`.
- **Example**: For the job in question, check `/home/woody/iwi5/iwi5086h/efd_train_c0.o491300`.
- **Exit Codes**: There is no general list of exit codes as they are specific to the job script.

## General Learning
- Always check the output files (STDOUT/STDERR) for detailed error messages.
- Exit codes are job-specific and not universally documented.
```
---

### 2022032542002371_Meggie%20Fehlermeldungen%20seit%20dieser%20Woche.md
# Ticket 2022032542002371

 ```markdown
# HPC Support Ticket: Meggie Fehlermeldungen seit dieser Woche

## Keywords
- Slurm-Version Update
- libjpeg
- libpng15
- LD_LIBRARY_PATH
- Hochgeschwindigkeitsnetzwerk Treiber
- Diskless Knoten
- Reboot
- Healthcheck-Skript

## Problem
- User's simulations stopped working after a Slurm version update on Meggie.
- Missing libraries (libjpeg, libpng15) caused initial errors.
- Additional errors related to the high-speed network driver.

## Root Cause
- Slurm update indirectly removed necessary libraries (libjpeg) from compute nodes.
- High-speed network driver issues on some nodes.

## Solution
- **Quick Fix for Missing Libraries:**
  - Copy `/usr/lib64/libjpeg.so.62.1.0` to a user directory and add it to `LD_LIBRARY_PATH`.
  - Identify and copy other missing libraries (e.g., libpng15.so.15) to the user directory.

- **Network Driver Issue:**
  - Reboot affected nodes to resolve high-speed network driver issues.
  - Implement a Healthcheck-Skript to automatically detect and resolve similar issues in the future.

## General Learnings
- Updates to software like Slurm can have indirect effects on dependencies.
- Diskless nodes require a reboot to install new packages.
- Temporary workarounds can be implemented by copying necessary libraries to user directories and updating `LD_LIBRARY_PATH`.
- Regular health checks and automated scripts can help detect and resolve issues with network drivers and other components.
```
---

### 2020012142000351_PBS-Deamon%20TinyEth.md
# Ticket 2020012142000351

 ```markdown
# HPC-Support Ticket: PBS-Daemon TinyEth

## Keywords
- PBS-Daemon
- Job Deletion Loop
- Wallclock Limit Exceeded
- TinyEth
- MOAB_INFO

## Problem Description
The PBS-Daemon on TinyEth has crashed on a node, causing a job to be stuck in a deletion loop. The job exceeded its wallclock limit and is being repeatedly attempted to be deleted.

## Root Cause
- PBS-Daemon crash on a node.
- Job exceeded wallclock limit.

## Solution
- No explicit solution provided in the conversation.
- Further investigation by HPC Admins is required to restart the PBS-Daemon and resolve the job deletion loop.

## Lessons Learned
- Regular monitoring of PBS-Daemon status is crucial.
- Jobs exceeding wallclock limits should be handled gracefully to avoid deletion loops.
- Communication with users about job status and system issues is important for transparency.
```
---

### 2020012442000257_Job%20l%C3%83%C2%B6schen.md
# Ticket 2020012442000257

 ```markdown
# HPC Support Ticket: Job Deletion Issue

## Keywords
- Job deletion
- PBS Job Id
- HPC Admin
- PBS Server restart
- Job recovery
- Communication protocol

## Summary
A user reported a hanging HPC job that could not be deleted. The issue involved multiple jobs in a corrupted state.

## Root Cause
- The PBS Server had issues with job recovery, leading to jobs being in a corrupted state.
- Logs indicated errors such as "Bad file descriptor" and "Unable to open script file."

## Solution
- A PBS Server restart was performed to fix the issue.
- The restart logs showed errors related to job recovery and script file access.
- The problematic job was eventually cleaned up by the HPC Admin.

## Lessons Learned
- Direct communication between users and HPC Admins is crucial for quicker resolution.
- Regular maintenance and monitoring of the PBS Server can prevent such issues.
- Users should be encouraged to report issues directly to the support team.

## Follow-up Actions
- Inform users to communicate directly with the HPC support team for future issues.
- Consider upgrading or replacing Torque to avoid similar issues in the future.
```
---

### 2024061042003933_HPC%20Job%20issue.md
# Ticket 2024061042003933

 ```markdown
# HPC Job Issue Ticket Conversation Summary

## Keywords
- Job submission
- ClusterCockpit
- Interactive job
- Disk quota exceeded
- GPU requirements
- CPU RAM requirements
- HPCVAULT
- $WORK

## Problem
- User submitted a job but couldn't see it in ClusterCockpit.
- Job failed after 12 seconds.
- Disk quota exceeded error (OSError: [Errno 122]).

## Root Cause
- Job failed due to exceeding disk quota on $HPCVAULT.
- Recursive creation of model files occupied space.

## Solution
- Use $HPCVAULT only as input and store intermediate files and outputs to $WORK.
- Attend "HPC in a nutshell" introduction for valuable insights.
- Refer to documentation for interactive jobs and available file systems.

## Resources
- [ClusterCockpit Job Search](https://monitoring.nhr.fau.de/monitoring/job/8326626)
- [Interactive Job Documentation](https://doc.nhr.fau.de/clusters/alex/#interactive-job)
- [HPC in a nutshell Introduction](https://hpc.fau.de/teaching/hpc-cafe/)
- [Interactive Jobs with salloc](https://doc.nhr.fau.de/batch-processing/batch_system_slurm/#interactive-jobs-with-salloc)
- [Available File Systems](https://doc.nhr.fau.de/data/filesystems/)
- [TinyGPU Cluster](https://doc.nhr.fau.de/clusters/tinygpu/)

## Additional Information
- User fixed the issue by stopping the recursive creation of model files.
- User requirements: Disk Space: 150GB, GPU: 16GB VRAM (32GB preferred), CPU RAM: 64GB.
```
---

### 2025030342002531_Running%20python%20scripts%20in%20Alex.md
# Ticket 2025030342002531

 ```markdown
# HPC Support Ticket Conversation: Running Python Scripts on Alex

## Subject: Running Python Scripts on Alex

### User Request:
- User wants to submit Python scripts on Alex.
- Currently running Python scripts on Woody but wants to use Alex due to input files being on Alex.
- Needs help with modifying the submit script for Alex.

### Initial Submit Script for Woody:
```bash
#!/bin/bash -l
#
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=32
#SBATCH --time=24:00:00
#SBATCH --export=NONE
#SBATCH --job-name=Complex
#SBATCH -o mess_%x.%j.out
#SBATCH -e mess_%x.%j.err

unset SLURM_EXPORT_ENV

export http_proxy=http://proxy:80
export https_proxy=http://proxy:80

module load python/3.9-anaconda

#module load python3

pip install --user MDAnalysis[analysis] MDAnalysisTests numpy

# Run your Python script within the virtual environment (if applicable)
python3 thresold_15c5K.py
```

### HPC Admin Recommendations:
- Recommended to create conda environments and use conda to install Python packages.
- Only need to load the Python module and activate the conda environment in the job script.

### User Actions:
- User created a conda environment on the frontend, which resulted in Python code without GPU support.
- User was instructed to delete the conda environment and build a new one on a compute node with GPU support.

### Steps to Create Conda Environment on Compute Node:
1. Start an interactive job on the Alex cluster:
   ```bash
   salloc --gres=gpu:a40:1 --time=1:00:00
   ```
2. Set proxy for internet access:
   ```bash
   export http_proxy=http://proxy:80
   export https_proxy=http://proxy:80
   ```
3. Build the conda environment:
   ```bash
   conda create --name py-jobs
   conda activate py-jobs
   pip install --user MDAnalysis[analysis] MDAnalysisTests numpy
   ```

### Updated Submit Script for Alex:
```bash
#!/bin/bash -l
#
#SBATCH --gres=gpu:a40:1
#SBATCH --time=24:00:00
#SBATCH --export=NONE

unset SLURM_EXPORT_ENV

export http_proxy=http://proxy:80
export https_proxy=http://proxy:80

module load python
conda activate py-jobs

python3 pbckcl_comcount_12c4_200.py
```

### Issues Encountered:
- Python jobs on Alex did not use the allocated GPU.
- Conda environment built on the frontend did not support GPU.

### Solution:
- Rebuild the conda environment on a compute node with GPU support.
- Ensure the Python script does not require GPU support if using MDAnalysis, as it typically does not support GPUs.

### Additional Notes:
- User was advised to check if MDAnalysis can use GPU, but it was confirmed that MDAnalysis typically does not support GPUs.
- User was instructed to shift the analysis to Woody if GPU support is not required.
- User was informed about adjusting directory permissions for data access between accounts.

### Conclusion:
- User followed the instructions to create a conda environment on a compute node and submitted the jobs.
- Jobs were still running, and further investigation was needed to confirm GPU usage.
- User was advised to move the analysis to Woody if GPU support is not required for MDAnalysis.
```
---

### 2024011042003728_H%C3%83%C2%A4ngendes%20Epilog-Skript%20auf%20fritz%3F.md
# Ticket 2024011042003728

 # HPC Support Ticket: Hängendes Epilog-Skript auf fritz

## Keywords
- Hanging job
- Epilog script
- SLURM
- salloc
- Node reboot
- df command
- Home directory

## Summary
A user reported a hanging job after the TaskPrologue stage on the HPC cluster. The job was allocated resources but did not proceed beyond the prologue script.

## Root Cause
The `df` command on node `f0104` was hanging, indicating a potential issue with the filesystem or node performance.

## Solution
The HPC Admin rebooted the node `f0104`, which resolved the issue.

## Lessons Learned
- Hanging jobs after the TaskPrologue stage can be caused by filesystem or node issues.
- The `df` command can be used to diagnose filesystem problems.
- Rebooting the affected node can resolve hanging job issues related to node performance.

## Actions Taken
1. User reported a hanging job after TaskPrologue.
2. HPC Admin identified that the `df` command was hanging on node `f0104`.
3. HPC Admin rebooted the node `f0104` to resolve the issue.

## Recommendations
- Monitor node performance and filesystem health regularly.
- Use diagnostic commands like `df` to identify potential issues.
- Consider rebooting nodes as a troubleshooting step for hanging jobs.
---

### 2019030742000538_JobID%201068224%20%26%20Speicherplatzbedarf.md
# Ticket 2019030742000538

 # HPC Support Ticket Analysis

## Subject: JobID 1068224 & Speicherplatzbedarf

### Keywords:
- JobID 1068224
- Emmy
- Warteschleife
- Speicherplatz
- ASCII-STL file
- Quota
- /home/woody
- /home/vault

### Problem:
- User's job (JobID 1068224) stuck in the queue while other jobs are starting.
- User requires more storage space for large ASCII-STL files needed for multiple jobs.

### Root Cause:
- Issue with a compute node preventing the job from starting.
- Limited storage quota for the user's current directory.

### Solution:
- **Job Start Issue**: HPC Admin resolved the node issue, allowing the job to run.
- **Storage Space**: HPC Admin suggested using `/home/woody` and `/home/vault` for higher storage quotas. Recommended `/home/woody` for ASCII files.

### Additional Information:
- Links to more information on available filesystems:
  - [HPC Environment](https://www.anleitungen.rrze.fau.de/hpc/environment/)
  - [HPC Storage](https://www.anleitungen.rrze.fau.de/hpc/hpc-storage/)

### General Learning:
- Check for node issues if a job is stuck in the queue while others are starting.
- Advise users to utilize different directories with higher quotas for large files.
- Provide links to documentation for further user education.
---

### 2022020742000873_Frage%20zu%20batch%20job%20execution.md
# Ticket 2022020742000873

 ```markdown
# HPC-Support Ticket Conversation: Frage zu batch job execution

## Keywords
- Batch job execution
- Woody cluster
- TinyGPU
- Torque
- Slurm
- qsub
- sbatch

## Problem
- User is a CE student at FAU trying to generate and run OMP parallel code on the Woody cluster.
- Batch jobs submitted on the entrance node of Woody are automatically redirected to TinyGPU.

## Root Cause
- The Woody cluster uses Torque as the batch system, not Slurm.
- The user is likely using Slurm commands (e.g., `sbatch`) instead of Torque commands (e.g., `qsub`).

## Solution
- Use Torque commands (`qsub`) instead of Slurm commands (`sbatch`) to submit batch jobs on the Woody cluster.
- Refer to the documentation for Torque batch processing: [Batch Processing Documentation](https://hpc.fau.de/systems-services/systems-documentation-instructions/batch-processing/)

## General Learning
- Ensure that the correct batch system commands are used for the specific cluster.
- Documentation and proper command usage are crucial for successful job submissions.
```
---

### 2019121242001377_Unable%20to%20connect%20to%20wadm1.md
# Ticket 2019121242001377

 # HPC Support Ticket: Unable to Connect to wadm1

## Keywords
- `qstat`
- `wadm1`
- `Connection refused`
- `errno=111`
- `Batch system server`

## Problem Description
The user was unable to connect to the batch system server `wadm1` using the `qstat` command. The error messages indicated a connection refusal (`errno=111`).

## Root Cause
The batch system server `wadm1` had crashed unexpectedly.

## Solution
The HPC Admin restarted the batch system server, which resolved the issue.

## Lessons Learned
- **Server Crash**: Unexpected server crashes can occur and may disrupt user operations.
- **Restart Solution**: Restarting the server can resolve connectivity issues.
- **Impact**: The crash did not affect running jobs, indicating robust job management.

## Steps for Future Reference
1. **Identify the Error**: Look for connection refused errors (`errno=111`) when using `qstat`.
2. **Check Server Status**: Verify if the batch system server is running.
3. **Restart Server**: If the server is down, restart it to restore connectivity.

## Additional Notes
- Regular monitoring of server health can help prevent unexpected crashes.
- Ensure that critical servers are included in maintenance and monitoring schedules.
---

### 2022092642003232_StarCCM%2B%20Meggie%20Slurm.md
# Ticket 2022092642003232

 # HPC Support Ticket: StarCCM+ Slurm Job Issue

## Keywords
- StarCCM+
- Slurm
- Job Scheduler
- Module Load
- Installation Corruption

## Problem Description
- User encountered an issue with StarCCM+ on the Meggie cluster using Slurm.
- Job log indicated that the `starccm+` command was not found.
- Attempting to load the StarCCM+ module resulted in an error due to missing files.

## Root Cause
- The installation of StarCCM+ versions 2021.3.1 and 2021.3.1-r8 was corrupted.
- Specific directories and files were missing, leading to module load errors and job failures.

## Solution
- HPC Admins identified the corrupted installation and copied the necessary files from another server (fadm1) to the current server (madm).
- User was advised to try running the job again after the installation was fixed.

## General Learnings
- Ensure that software installations are complete and not corrupted.
- Verify the presence of necessary files and directories when encountering module load errors.
- Communicate with HPC Admins for assistance in resolving installation issues.

## Actions Taken
- HPC Admins diagnosed the issue and corrected the corrupted installation.
- User was informed to retry the job after the fix.

## Future Reference
- If similar errors occur, check for installation corruption and ensure all necessary files are present.
- Consult HPC Admins for assistance in resolving software installation issues.
---

### 2025011342002123_Helma%20Job%20Restart.md
# Ticket 2025011342002123

 ```markdown
# HPC-Support Ticket: Helma Job Restart

## Keywords
- Job Restart
- Node Reservation
- Slurm
- Job Priority
- Job Cancellation

## Problem
- User wants to restart a 32-node job on Helma.
- Requests to reserve nodes for 10 minutes to ensure immediate restart.
- New job (5744) is already queued and needs to be extended.
- Old job (5540) should be canceled once nodes are reserved.

## Solution
- HPC Admin explains that Slurm terminates jobs at the end of their reservation.
- Increases the priority of the new job (5744) to maximize the chances of inheriting the nodes.
- User cancels the old job (5540) after receiving the explanation.

## Lessons Learned
- Slurm does not support reserving nodes for a short period to restart jobs.
- Increasing job priority can help in inheriting nodes for a new job.
- Users should be aware of Slurm's job management policies.
```
---

### 2024021342001642_ALEX%20Rechnung%20friert%20nach%20Start%20ein%20-%20bccc013h.md
# Ticket 2024021342001642

 ```markdown
# HPC Support Ticket: LAMMPS Simulation Freezes After Start

## Keywords
- LAMMPS Simulation
- SLURM
- Job Freeze
- Initialization Delay
- HPC Cluster
- TaskPrologue

## Problem Description
The user encountered an issue where a LAMMPS simulation job on the HPC cluster (ALex) appeared to freeze after initializing. The job was listed as running in SLURM, but LAMMPS did not start, and there were no error messages or further logs after the TaskPrologue.

## Troubleshooting Steps
1. **User Report**: The user submitted a job (JOB-ID: 1086833) that initialized but did not proceed to run the LAMMPS simulation. The SLURM output file showed no activity beyond the TaskPrologue.
2. **HPC Admin Response**: The admin requested the user to start a new job to observe the behavior live on the node.
3. **Live Observation**: The admin monitored the new job (JOB-ID: 1087014) and observed that it started running correctly after approximately 10 minutes.

## Root Cause
The job experienced an initialization delay, possibly due to after-effects of recent system outages over the weekend.

## Solution
- **Patience**: The user was advised to wait for approximately 15 minutes after job initialization to allow the simulation to start properly.
- **System Monitoring**: The admin suggested that the job might be affected by recent system outages, indicating a need for further system monitoring and stability checks.

## Conclusion
The issue was resolved by allowing the job sufficient time to initialize and start the simulation. The user was advised to be patient and wait for the job to start properly.

## Next Steps
- Continue monitoring the system for any residual effects from recent outages.
- Advise users to wait for a longer initialization period if they encounter similar issues.
```
---

### 2024051742003459_Multi-node%20on%20ALEX.md
# Ticket 2024051742003459

 # HPC Support Ticket: Multi-node on ALEX

## Keywords
- Multi-node jobs
- Resource allocation
- SLURM directives
- Partition
- QoS (Quality of Service)

## Problem
- User unable to run program on more than one node on ALEX.

## Root Cause
- Incorrect or missing resource allocation settings in the SLURM script.

## Solution
- Update the SLURM script with the following directives:
  ```bash
  #SBATCH --nodes=8 # Specify the number of nodes (2 to 8)
  #SBATCH --partition=a40 # or a100
  #SBATCH --qos=a40multi # or a100multi
  ```

## General Learnings
- Ensure proper SLURM directives are used for multi-node jobs.
- Specify the correct partition and QoS for the job.
- Verify user permissions for multi-node access.

## Roles Involved
- HPC Admins
- 2nd Level Support Team

## Additional Notes
- The user was granted permission to use multi-node jobs.
- The solution involves modifying the SLURM script to include the correct resource allocation settings.
---

### 2023101142001285_Job%202384443%20h%C3%83%C2%A4ngt.md
# Ticket 2023101142001285

 ```markdown
# HPC Support Ticket: Job Hanging in State CG

## Keywords
- Job Hanging
- State CG
- Timelimit
- Slurm Update

## Problem Description
- User reported that their job with ID 2384443 was hanging in state CG, 7 seconds over the timelimit.
- The job was started the previous day and appeared to have completed.

## Root Cause
- The issue was likely caused by a Slurm update that occurred the previous afternoon.

## Solution
- HPC Admins removed the hanging jobs.

## Lessons Learned
- Slurm updates can cause jobs to hang in state CG.
- Monitoring and quick resolution of such issues are crucial for maintaining system stability.

## Actions Taken
- HPC Admins acknowledged the issue and removed the hanging jobs.
- The user was informed about the likely cause being a Slurm update.

## Recommendations
- Ensure that Slurm updates are thoroughly tested before deployment to avoid job disruptions.
- Provide users with clear communication about system updates and their potential impacts.
```
---

### 2022111042001732_Meggie%20cluster%2C%20Jobs%20laufen%20nicht%2C%20gwgi008h.md
# Ticket 2022111042001732

 # HPC-Support Ticket: COSIPY Job Issues on Meggie Cluster

## Problem Description
- User reported that the COSIPY model, which is written in Python and parallelized, stopped working after the upgrade to AlmaLinux8.
- The model runs interactively but fails when submitted as a job.
- Initial suspicion was on the batch script or module compatibility.

## Troubleshooting Steps
1. **Initial Diagnosis**:
   - User provided logs showing that the job starts but then stops without completing the parallel computation.
   - User confirmed that the model worked before the upgrade and that the new installation of Python packages was successful.

2. **Dependency Issues**:
   - HPC Admin suggested checking the version of the `click` package, which was causing issues with `dask`.
   - User tried different versions of `click` and `dask` but encountered various errors.

3. **Python Version**:
   - HPC Admin suggested that the issue might be related to the Python version.
   - User was advised to try Python 3.6, which is supported by COSIPY.

4. **Environment Setup**:
   - User was advised to use `miniconda` to create a specific environment with Python 3.6.
   - HPC Admin provided instructions to clone and build the COSIPY repository.

5. **Resolution**:
   - User reset all packages to their original state, and the model started working again.
   - The exact cause of the initial failure was not determined, but the reset resolved the issue.

## Additional Observations
- User noticed that not all worker nodes were running, which could affect the performance of the model.
- HPC Admin explained that the missing workers might be due to queue delays and that Dask can handle such situations, although it may increase the simulation time.

## Conclusion
- The issue was resolved by resetting the Python packages to their original state.
- The exact cause of the initial failure remains unknown.
- User was advised to export the working environment for future reference.

## Future Recommendations
- Document the working environment and package versions to avoid similar issues in the future.
- Monitor the worker nodes to ensure all are running as expected.

## Keywords
- COSIPY
- Python
- Dask
- Click
- AlmaLinux8
- Meggie Cluster
- Batch Script
- Environment Setup
- Package Versions
- Worker Nodes
- Queue Delays
- Simulation Time
---

### 2024100742002629_%5BRegarding%20SSH%20into%20Alex%20cluster%5D.md
# Ticket 2024100742002629

 ```markdown
# HPC Support Ticket: SSH into Alex Cluster

## Keywords
- SSH
- Alex cluster
- Slurm account
- Conda environment
- Woody filesystem
- User directory

## Problem
- User unable to SSH into the Alex job submitting node.
- Error message: `This account is currently not available.`
- User directory missing in the Woody filesystem.

## Root Cause
- Missing Slurm account configuration for the user's group.
- User directories not created due to missing cron job execution.

## Solution
- HPC Admin added the Slurm account using the command:
  ```
  sacctmgr add account v114be set descr="Computer Vision and Machine Perception Lab - UTN" parent=bayernki
  ```
- User directories were created manually by the HPC Admin.

## General Learnings
- Ensure Slurm account is properly configured for new users.
- User directories may not be created immediately and may require manual intervention or waiting for the next cron job.
- FAU users have access to `/home/woody`, while other project users have directories in `/home/atuin`.

## Follow-up
- User was able to SSH into the cluster after the Slurm account was added.
- User was informed about the location of their project directory.
```
---

### 2022080942003632_Srun%20Fehlermeldung%20in%20Job.md
# Ticket 2022080942003632

 ```markdown
# HPC Support Ticket: Srun Fehlermeldung in Job

## Keywords
- srun error
- lookup failure
- node record
- invalid hostnames
- Betriebssystemupdate

## Problem Description
- User encountered multiple `srun: error: _find_node_record: lookup failure` messages for specific nodes (m0665-m0676, m0765-m0776) while running jobs on Meggie.
- Additionally, a warning about invalid hostnames in the switch configuration was reported.

## Root Cause
- The errors were due to preparations for a Betriebssystemupdate on Meggie.

## Solution
- The errors can be ignored as they are a result of ongoing system updates.
- New jobs should not encounter these errors after the update preparations are complete.

## General Learnings
- System updates and preparations can cause temporary errors that do not affect job execution.
- Users should be informed about ongoing maintenance to avoid confusion.

## Actions Taken
- HPC Admin informed the user that the errors can be ignored and are due to system update preparations.
- User acknowledged the information and thanked the HPC Admin for the quick response.
```
---

### 2015111942001373_Not%20possible%20to%20delete%20job%20on%20Woody.md
# Ticket 2015111942001373

 # HPC Support Ticket: Not Possible to Delete Job on Woody

## Keywords
- Job deletion
- Woody
- qdel command
- Stuck job
- Admin intervention

## Summary
A user encountered an issue where they were unable to delete a specific job (2418530[].wadm1) from the queue on Woody using the `qdel` command. The user attempted to delete the job using `/qdel //2418530[].wadm1/` and `/qdel all/`, but the job remained undeletable.

## Root Cause
The root cause of the problem was not explicitly identified in the provided conversation. However, it is implied that the job might be stuck or in a state that prevents it from being deleted by the user.

## Solution
The user inquired whether there is a way to force delete the job or if admin intervention is required. The resolution was not provided in the conversation, but it suggests that admin intervention might be necessary to delete the stuck job.

## General Learnings
- Users may encounter jobs that cannot be deleted using standard commands.
- The `qdel` command may not always be effective in deleting jobs.
- Admin intervention might be required to delete stuck jobs.
- It is important to document and escalate such issues for further investigation and resolution.
---

### 2023071142001826_Probleme%20mit%20Zugriffsrechten%20bei%20ausf%C3%83%C2%BChrung%20selbstkompilierter%20Software.md
# Ticket 2023071142001826

 ```markdown
# HPC-Support Ticket: Probleme mit Zugriffsrechten bei Ausführung selbstkompilierter Software

## Keywords
- Zugriffsrechte
- Permission denied
- Kompilierung
- Submit-Skript
- Dock6
- FRITZ
- Woody
- chmod
- execve

## Problem
- **Root Cause**: Fehlende Ausführungsrechte (executable flag) bei der Datei `dock6.mpi`.
- **Symptom**: Fehlermeldung "slurmstepd: error: execve(): /home/vault/b132dc/b132dc11/software/dock6_intel/bin/dock6.mpi: Permission denied" beim Ausführen des Programms über ein Submit-Skript oder direkt.
- **Ursache**: Die Datei wurde von Woody nach FRITZ kopiert, ohne die Berechtigungen mitzukopieren.

## Lösung
- **Quick-Fix**: Veränderung der Zugriffsrechte mit `chmod +x /home/vault/b132dc/b132dc11/software/dock6_intel/bin/dock6.mpi`.
- **Langfristige Lösung**: Neukompilierung der Software auf FRITZ, um sicherzustellen, dass alle Berechtigungen korrekt gesetzt sind und die Software die Features der neueren Prozessoren nutzen kann.

## Allgemeine Erkenntnisse
- Unix-Systeme erkennen ausführbare Dateien an den Zugriffsrechten, nicht an der Dateiendung.
- Berechtigungen müssen beim Kopieren von Dateien zwischen Systemen berücksichtigt werden.
- Neukompilierung der Software kann notwendig sein, wenn sie auf einem anderen System kompiliert wurde, um Kompatibilität und optimale Nutzung der Hardware sicherzustellen.
```
---

### 201808219001919_Jobs%20Woody%20qdel.md
# Ticket 201808219001919

 # HPC Support Ticket: Jobs Woody qdel

## Keywords
- Job cancellation
- qdel command
- Woody cluster
- Job ID
- Error message
- Job cancel in progress

## Problem Description
- User attempts to cancel jobs with IDs 5058342 and 5058411 on the Woody cluster using the `qdel` command.
- Receives error message: `qdel: Invalid request MSG=job cancel in progress`.
- Jobs remain active for several hours despite cancellation attempts.

## Root Cause
- The error message indicates that the job cancellation process is already in progress but not completing.

## Solution
- No immediate solution provided in the conversation.
- Further investigation by HPC Admins is required to determine why the cancellation process is stalled.

## General Learning
- Understand that the `qdel` command may not always immediately cancel a job.
- Recognize the error message `qdel: Invalid request MSG=job cancel in progress` as an indication that the job cancellation is in progress but not completing.
- Escalate to HPC Admins for further investigation if jobs remain active despite cancellation attempts.

## Next Steps
- HPC Admins should check the status of the job cancellation process.
- If necessary, manually intervene to force job cancellation.
- Document any additional steps taken to resolve the issue for future reference.
---

### 2024121342002168_some%20jobs%20on%20Helma%20fail%20%26%20prolog%20error%20-%20v115be11.md
# Ticket 2024121342002168

 # HPC Support Ticket: Prolog Error and Job Failures

## Subject
- **Issue**: Jobs failing immediately after submission with "Reason=Prolog Failed"
- **User**: via Helma-EA-Chat
- **Job IDs**: 1990, 1991, 1992, 1993

## Symptoms
- Jobs in `JobState=COMPLETING` for an extended period.
- `scontrol` shows "Reason=Prolog Failed".
- Logs indicate jobs missing from batch node `h12-12` with `WTERMSIG 1`.
- `slurmctld.log` shows repeated socket errors.
- `job_completions` log indicates `JobState=NODE_FAIL`.
- `/var/log/messages` shows prolog for jobs running for extended periods and jobs already killed.

## Logs
- **slurmctld.log**:
  ```
  [2024-12-13T19:53:26.004] Batch JobId=1990 missing from batch node h12-12 (not found BatchStartTime after startup)
  [2024-12-13T19:53:26.004] _job_complete: JobId=1990 WTERMSIG 1
  ...
  [2024-12-13T19:53:26.008] error: slurm_send_node_msg: [socket:[3453849]] slurm_bufs_sendto(msg_type=RESPONSE_SLURM_RC) failed: Unexpected missing socket error
  ```

- **job_completions**:
  ```
  JobId=1990 UserId=v115be11(212475) GroupId=v115be(80256) Name=bash JobState=NODE_FAIL Partition=h100 TimeLimit=1440 StartTime=2024-12-13T19:52:27 EndTime=2024-12-13T19:53:26 NodeList=h12-12 NodeCnt=1 ProcCnt=32 WorkDir=/home/hpc/v115be/v115be11/repos/pos_ablation ReservationName= Tres=cpu=32,mem=175G,node=1,billing=32,gres/gpu=1 Account=v115be QOS=normal WcKey=* Cluster=helma SubmitTime=2024-12-13T19:52:27 EligibleTime=2024-12-13T19:52:27 Derived ExitCode=0:0 ExitCode=0:1
  ```

- **/var/log/messages**:
  ```
  Dec 13 19:54:48 h12-12 slurmd[14069]: slurmd: prolog for job 1992 ran for 135 seconds
  Dec 13 19:54:48 h12-12 slurmd[14069]: slurmd: Job 1992 already killed, do not launch extern step
  ...
  ```

## Analysis
- Prolog script ran for extended periods before jobs were killed.
- Jobs were missing from the batch node `h12-12`.
- Repeated socket errors in `slurmctld.log`.

## Root Cause
- Prolog script issues causing job failures.
- Possible network or node issues causing socket errors.

## Solution
- Investigate prolog script for any issues.
- Check network and node `h12-12` for any issues causing socket errors.
- Ensure `shownicerquota.pl` is not causing issues, as it is called in the epilog.

## Keywords
- Prolog Failed
- JobState=COMPLETING
- WTERMSIG 1
- slurmctld.log
- job_completions
- /var/log/messages
- socket error
- shownicerquota.pl
- epilog
- HPC Admins
- 2nd Level Support team
- Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support
- Software and Tools developer
---

### 2024100342001155_b178bb11%20status%20CG%20in%20SLURM.md
# Ticket 2024100342001155

 ```markdown
# HPC Support Ticket: SLURM Job Status CG

## Keywords
- SLURM
- Job Status CG
- High File Server Load
- Job Completion

## Problem Description
User inquired about the meaning of the SLURM job status `CG` for several jobs. The jobs appeared to be finishing but some processes were still active.

## Root Cause
The `CG` status indicates that the job is completing but some processes are still active, likely due to high load on the file servers. This prevents SLURM from removing the job and its resources immediately.

## Solution
The HPC Admin confirmed that the status is correct and is likely caused by high load on the file servers. The jobs should vanish after some time once the file operations are complete. If the jobs do not disappear, the user should contact HPC support again.

## What Can Be Learned
- The `CG` status in SLURM indicates that a job is completing but some processes are still active.
- High load on file servers can cause delays in job completion and resource release.
- Users should wait for the job to disappear from the queue. If it persists, they should contact HPC support for further assistance.
```
---

### 2021020542001412_help%20regarding%20emmy%20for%20flops_s.md
# Ticket 2021020542001412

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject: Help regarding Emmy for FLOPS/s

### Keywords:
- Emmy cluster
- Starccm+
- FLOPS/s
- SLURM output
- Job statistics

### Root Cause of the Problem:
- User needs to determine the FLOPS/s for their simulation run on the Emmy cluster using Starccm+.

### Solution:
- **SLURM Output File**: Instruct the user to check the end of their SLURM output file for job statistics.
- **Job Statistics**: Provide an example of what the job statistics section looks like, including details such as Job-ID, Job-Name, Initial workdir, Queue/Partition, Requested resources, Used resources, Node list, and Subm/Elig/Start/End.
- **Job Overview**: Advise the user to use their Job-ID, AccessKey, and username to get an overview of their job via a specific URL (e.g., `https://www.hpc.rrze.fau.de/HPC-Status/job-info.php`).

### General Learnings:
- **Job Statistics Location**: Job statistics are found at the end of the SLURM output file.
- **Job Overview URL**: Users can get an overview of their job using their Job-ID, AccessKey, and username on a specific webpage.
- **Resource Usage**: The SLURM output file provides detailed information about the resources used by the job.

### Roles:
- **HPC Admins**: Provide support and guidance on using the HPC cluster.
- **2nd Level Support Team**: Assist with more complex issues and troubleshooting.
- **Head of the Datacenter**: Oversees the datacenter operations.
- **Training and Support Group Leader**: Leads training and support initiatives.
- **NHR Rechenzeit Support**: Handles support for NHR computing time and applications for grants.
- **Software and Tools Developer**: Develops software and tools for the HPC environment.
```
---

### 2018090542000416_Node%20failure%20auf%20meggie.md
# Ticket 2018090542000416

 # HPC Support Ticket: Node Failure on Meggie

## Keywords
- Node failure
- Job aborted
- Slurm error
- Job-ID 323147
- Node m0918
- Node m0912
- Slurmctld log

## Summary
A user reported a job failure on the HPC cluster "meggie" with Job-ID 323147. The job was aborted due to a node failure on m0918 and m0912.

## Error Messages
- `srun: error: Node failure on m0918`
- `srun: Job step aborted: Waiting up to 32 seconds for job step to finish.`
- `slurmstepd: error: *** STEP 323147.0 ON m0912 CANCELLED AT 2018-09-05T00:25:35 DUE TO NODE FAILURE, SEE SLURMCTLD LOG FOR DETAILS ***`
- `slurmstepd: error: *** JOB 323147 ON m0912 CANCELLED AT 2018-09-05T00:25:35 DUE TO NODE FAILURE, SEE SLURMCTLD LOG FOR DETAILS ***`

## Root Cause
Node failure on m0918 and m0912.

## Solution
The user restarted the job. No further action was reported by the HPC Admins.

## Learnings
- Node failures can cause job abortions.
- Check the Slurmctld log for detailed error information.
- Users can restart jobs after a failure.
- Inform the HPC Admins about node failures for further investigation.
---

### 2024121242002946_some%20jobs%20on%20Helma%20fail%20%26%20incomplete%20prolog%20-%20v115be11.md
# Ticket 2024121242002946

 # HPC Support Ticket: Job Failure and Incomplete Prolog

## Subject
some jobs on Helma fail & incomplete prolog - v115be11

## Keywords
- Job failure
- Incomplete prolog
- Slurm
- Race condition
- Job statistics
- Node down

## Problem Description
A user noticed that not all jobs submitted in a batch were running. Specifically, job 1233 failed to start and immediately printed job statistics in the log without running the "TaskPrologue". The job was rescheduled and ran successfully as job 1235.

## Logs and Diagnostics
- Job statistics showed that job 1233 had an elapsed runtime of 00:00:01 and used 0.0 GiB of assigned 175 GiB RAM.
- Slurm set the node to down with the reason "batch job complete failure".
- `dmesg` and `/var/log/messages` logs indicated normal operations without clear errors.
- Two jobs (1233 and 1234) were launched simultaneously for the same UID, but only one logged `SLURM_EXPORT_ENV`.

## Root Cause
The HPC Admin suggested a possible race condition where two jobs were started simultaneously, leading to one job failing to initialize properly.

## Solution
No explicit solution was provided in the conversation. Further investigation into the race condition and ensuring proper job initialization could be necessary.

## General Learnings
- Simultaneous job launches can lead to race conditions and job failures.
- Job statistics and Slurm logs are crucial for diagnosing job failures.
- Rescheduling a failed job can sometimes resolve the issue, but the underlying cause should be investigated.

## Next Steps
- Investigate and resolve the potential race condition.
- Monitor job launches to prevent simultaneous starts.
- Ensure proper job initialization and logging to capture all necessary environment variables.
---

### 2024121942003012_%5Baction%20requiered%5D%20short%20running%20jobs%20on%20woody%20%5Biwal118h%5D.md
# Ticket 2024121942003012

 # HPC Support Ticket: Short Running Jobs on Woody

## Keywords
- Short running jobs
- Job flooding
- SLURM batch scheduler
- Job bundling
- Account limitations
- Monitoring issues

## Summary
A user submitted a large number of short-running jobs (< 5 minutes) on the Woody cluster, causing significant disruption to the system and monitoring. The HPC Admin intervened to limit the user's account and provided guidance on best practices.

## Root Cause
- User submitted a large number of short-running jobs due to errors in the submission script.
- Jobs were submitted without proper monitoring, leading to unnoticed issues.

## Impact
- Negative impact on the cluster and monitoring system.
- System overload similar to a DDoS attack.

## Actions Taken by HPC Admin
- Limited the user's account to 10 cores on Woody.
- Deleted jobs from the queue to reduce disruption.
- Provided a link to best practices for SLURM batch scheduler.

## Solution
- User acknowledged the issue and committed to submitting jobs under supervision in the future.
- User was advised to test new scripts before full-scale submission.

## Lessons Learned
- Avoid submitting a large number of short-running jobs.
- Test submission scripts before full-scale deployment.
- Follow best practices for job bundling and SLURM batch scheduler usage.
- Monitor job submissions to catch errors early.

## References
- [SLURM Batch Scheduler Best Practices and Advanced Use](https://hpc.fau.de/2024/12/04/monthly-hpc-cafe-slurm-batch-scheduler-best-practices-and-advanced-use/)
---

### 2025011042000881_Increasing%20the%20time%20duration%20of%20slurm%20jobs.md
# Ticket 2025011042000881

 # HPC Support Ticket: Increasing the Time Duration of Slurm Jobs

## Keywords
- Slurm jobs
- Job runtime
- High-priority jobs
- Job ID
- Cluster
- Support email

## Problem
- User requires increased time duration for Slurm jobs (up to 48 hours) due to heavy experiments and upcoming deadlines.

## Root Cause
- The default maximum job runtime is insufficient for the user's experiments.

## Solution
- A general increase in maximum job runtime is not possible, even for specific projects or users.
- For high-priority jobs requiring extended runtime:
  1. Submit the job with the `--hold` flag.
  2. Send an email to `support-hpc@fau.de` with the job ID and cluster details.
  3. HPC Admins will review and decide on the request.

## Notes
- The decision to extend runtime is at the discretion of the HPC Admins.
- This process is intended for exceptional cases and not for regular job submissions.
---

### 2023121242002706_submission%20error.md
# Ticket 2023121242002706

 ```markdown
# HPC Support Ticket: Submission Error

## Keywords
- sbatch
- command not found
- login node
- submission error

## Problem Description
- User encounters an error when trying to submit a job using `sbatch`:
  ```
  -bash: sbatch: command not found
  ```
- User notices a change in the login node name:
  ```
  (usual): b166ea10@fritz4:
  (current): b166ea10@cshpc:
  ```

## Root Cause
- The user is logging into a different node (`cshpc`) where the `sbatch` command is not available.

## Solution
- Ensure that the user logs into the correct node (`fritz4`) where the `sbatch` command is available.

## Lessons Learned
- Verify the login node to ensure it has the necessary commands and tools.
- Check for differences in the environment when encountering command not found errors.

## Actions Taken
- User realized there was no issue after verifying the login node.

## Follow-up
- No further action required as the user resolved the issue independently.
```
---

### 2021090142002031_Inaktive%20Emmy-Jobs%20II.md
# Ticket 2021090142002031

 # HPC Support Ticket: Inactive Emmy-Jobs II

## Keywords
- Quantum Espresso Jobs
- Emmy Cluster
- Infiniband
- Parallel Dateisystem
- Systematischer Reboot
- opensm-Log
- QDR Link

## Problem Description
- Two 30-node Quantum Espresso jobs on Emmy did not execute but held the nodes until manually terminated.
- Similar issue observed during Easter holidays, previously resolved by a systematic reboot of Emmy nodes.
- Possible issues with Infiniband or access to the parallel file system.

## Ticket Details
- **Job-ID**: 1531848 & 1531904
- **AccessKey**: 220aef3f & 3bb8713f
- **UserID**: mpp3004h

## Investigation
- HPC Admin checked for Infiniband problems but found no major issues.
- One port in the opensm-Log showed increased activity but not enough to indicate significant Infiniband problems.
- The link was operating at full QDR and not downgraded.

## Solution
- No specific solution mentioned in the ticket.
- The ticket was closed without a direct response to the user.

## Lessons Learned
- Systematic reboots can resolve issues with job execution on Emmy nodes.
- Infiniband and parallel file system access should be checked for similar issues.
- Regular monitoring of opensm-Log and Infiniband links can help identify potential problems.

## Next Steps
- Continue monitoring Infiniband links and opensm-Log for any unusual activity.
- Consider systematic reboots if similar issues arise in the future.
- Ensure timely communication with users regarding the status of their support tickets.
---

### 2025022642000742_Requeue%20Slurm%20Script.md
# Ticket 2025022642000742

 # HPC Support Ticket: Requeue Slurm Script

## Keywords
- Slurm
- Requeue
- Signal
- Jobscript
- SIGUSR1
- scontrol
- Endless loop
- sacct
- Accounting

## Problem
- User attempted to automatically requeue a Slurm job using `#SBATCH --signal=SIGUSR1@90`.
- Error message indicated that the requeue operation was disabled for the job.

## Root Cause
- The job was not marked as requeueable by default.
- The user did not include the necessary `#SBATCH --requeue` directive in the job script.

## Solution
- Add `#SBATCH --requeue` to the job script to explicitly mark the job as requeueable.
- Instead of using `scontrol requeue`, it is recommended to resubmit the job script via `sbatch` with a failsafe to prevent endless loops.
- Use the built-in bash variable `$SECONDS` to ensure the job ran for a sufficient amount of time before resubmitting.

## Additional Notes
- Requeueing jobs can cause issues with accounting and monitoring tools like ClusterCockpit.
- Requeued jobs may not be properly tracked in `sacct`, leading to inaccurate accounting of compute time.
- It is generally recommended to avoid requeuing jobs to prevent potential issues with the batch system.

## Documentation Reference
- [Chain Jobs Documentation](https://doc.nhr.fau.de/batch-processing/advanced-topics-slurm/#chain-jobs)

## Roles Involved
- HPC Admins
- 2nd Level Support Team
- Head of the Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support
- Software and Tools Developer
---

### 2023080142004439_ERROR%20slurm.md
# Ticket 2023080142004439

 # HPC Support Ticket: ERROR slurm

## Keywords
- `sbatch`
- `DNS SRV lookup failed`
- `Unknown host`
- `JupyterHub`
- `slurm.conf`

## Summary
A user encountered an error while running an MD simulation script using `sbatch` on the cluster. The error messages indicated issues with DNS SRV lookup and configuration source establishment.

## Root Cause
- The user attempted to run the command through JupyterHub, which was connected to a specific cluster, causing the failure.
- The static versions of `slurm.conf` in `/etc/slurm-fritz` and `/etc/slurm-alex` did not include the necessary configurations for the user's cluster.

## Solution
- The HPC Admin corrected the `slurm.conf` files to include the necessary configurations for the user's cluster.
- The user was advised to ensure they are running commands on the correct cluster and not through JupyterHub unless properly configured.

## Lessons Learned
- Ensure that `slurm.conf` files are up-to-date and include all necessary configurations for the clusters in use.
- Verify that commands are being run on the correct cluster and not through intermediaries like JupyterHub unless properly configured.
- Check `/var/log/jupyterhub.log` for any suspicious entries related to the user's account if issues persist.

## Actions Taken
- HPC Admin updated the `slurm.conf` files to include the necessary configurations.
- The ticket was closed after verifying that the user could start JupyterHub sessions on the required clusters.

## Future Reference
- For similar errors, check the `slurm.conf` files for missing configurations.
- Ensure that users are running commands on the correct cluster and not through intermediaries unless properly configured.
- Review `/var/log/jupyterhub.log` for any suspicious entries related to the user's account.
---

### 2025021442000425_Batch%20job%20submission%20issue.md
# Ticket 2025021442000425

 ```markdown
# Batch Job Submission Issue

## Keywords
- Batch job submission
- SLURM
- CPU per task
- Node configuration
- Job script

## Problem Description
After cluster maintenance, the user encountered an issue where submitting a job with `cpu_per_task>1` resulted in the error: "sbatch: error: Batch job submission failed: Requested node configuration is not available."

## Root Cause
The job script contained contradictory resource requests:
- `--ntasks-per-node=4`
- `--gres=gpu:a100:4`
- `--cpus-per-task=4`

These requests did not match the hardware configuration, leading to the error.

## Solution
The user initially resolved the issue by removing the `--nodes=1` line from the script. However, the correct fix, as advised by HPC Admins, was to adjust `--cpus-per-task` to match the hardware configuration. For Alex-A100, the correct value is `--cpus-per-task=16`.

## Job Script Example
```bash
#!/bin/bash -l
#SBATCH --partition=a100
#SBATCH --job-name=dist_train_a100
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=4
#SBATCH --gres=gpu:a100:4
#SBATCH --cpus-per-task=16
#SBATCH --time=24:00:00
```

## Lessons Learned
- Ensure that resource requests in job scripts match the hardware configuration.
- Newer SLURM versions may have stricter sanity checks, leading to job rejections if resource requests are inconsistent.
- Provide detailed information in support tickets, including username, cluster, job script, and command line used to queue the job.
```
---

### 42192053_woody%20jobsubmittion%20fails.md
# Ticket 42192053

 # HPC Support Ticket: Job Submission Failure

## Keywords
- Job submission failure
- qsub error
- Connection refused
- Admin node crash
- Woody cluster

## Problem Description
- User unable to submit a job using `qsub` command.
- Error message: `Cannot connect to specified server host 'wadm1'. qsub: cannot connect to server wadm1 (errno=111) Connection refused`.

## Root Cause
- Admin node of the Woody cluster crashed, preventing job submissions.

## Solution
- Wait for the admin node to be restored.
- HPC Admins are working to resume regular batch processing.

## General Learnings
- Job submission failures with connection refused errors may indicate issues with the admin node.
- Check for any recent crashes or downtimes of the cluster's admin node.
- Inform users about the estimated time for resolution if available.
---

### 2023083142002858_24h%20Limit%20%28mal%20wieder%29.md
# Ticket 2023083142002858

 # HPC Support Ticket: 24h Limit Issue

## Keywords
- 24h Limit
- Job Dependencies
- Slurm
- GPU Utilization
- Job Scheduling
- Cluster Management

## Problem Description
- Users have accepted the 24-hour job limit but face delays when subsequent jobs need to be queued again.
- The current practice of queuing follow-up jobs at the end of the running job leads to unpredictable delays, especially when the cluster is full.

## Root Cause
- The need to requeue follow-up jobs results in them being placed at the end of the queue, causing delays and making it difficult to predict job completion times.

## Solution
- **Job Dependencies**: Slurm supports job dependencies using `--dependency=after:job_id` or `--dependency=afterany:job_id`. However, this does not change the priority accumulation behavior.
- **Efficient Resource Utilization**: Encourage users to evaluate their GPU needs and optimize usage to reduce unnecessary resource consumption.

## General Learnings
- Job dependencies in Slurm can help manage job sequences but do not affect priority accumulation.
- Efficient resource utilization, especially for GPUs, is crucial to reduce delays and improve overall cluster performance.
- Regular monitoring and communication about resource usage can help identify and address inefficiencies.

## Next Steps
- Continue to educate users on efficient resource utilization.
- Monitor GPU usage and provide feedback to users with low utilization rates.
- Consider implementing policies to prioritize jobs based on resource efficiency.

## References
- Slurm Documentation on Job Dependencies
- Cluster Resource Utilization Reports

---

This documentation aims to assist HPC support employees in understanding and addressing similar issues related to job scheduling and resource management.
---

### 2016021842002344_Resubmit%20Accelerated%20Queue.md
# Ticket 2016021842002344

 ```markdown
# HPC Support Ticket: Resubmit Accelerated Queue

## Keywords
- Job resubmission
- Accelerated queue
- Tesla K20m nodes
- PBS script
- Emmy Cluster

## Problem Description
The user was experiencing issues with job resubmission on the Tesla K20m nodes in the accelerated queue. The jobs were not being resubmitted automatically at the end of their runtime, despite working correctly on regular nodes.

## Root Cause
The job script did not explicitly specify the accelerated queue (`#PBS -q accel`), which is required for jobs using the accelerator nodes. The system on the Emmy frontends automatically adds the queue requirement if it is missing, but this does not happen on the compute nodes.

## Solution
The HPC Admin suggested adding the line `#PBS -q accel` to the job script to explicitly specify the accelerated queue. This modification resolved the issue, allowing the jobs to resubmit automatically.

## Additional Notes
- The user confirmed that the resubmission mechanism worked correctly with the same script on regular nodes without CUDA.
- The HPC Admin verified that job submission from the CPU nodes is generally functional under the user's account.

## Conclusion
The problem was resolved by explicitly specifying the accelerated queue in the job script. This ensures that the job resubmission mechanism works correctly on the Tesla K20m nodes.
```
---

### 2023063042001275_Keine%20interaktiven%20Sessions%20auf%20genoa1%20im%20Testcluster.md
# Ticket 2023063042001275

 # HPC Support Ticket: Interactive Sessions Failure on genoa1 in Testcluster

## Keywords
- Slurm
- Interactive Session
- salloc
- srun
- slurmd
- Node Configuration
- Memory Configuration

## Problem Description
The user reported that the node "genoa1" in the test cluster was listed as "idle" by Slurm but failed to start an interactive session. The error messages indicated a failure in task launch due to zero bytes being transmitted or received.

## Root Cause
- The node "genoa1" was not included in `/etc/dsh/group/all`, which likely resulted in the `systemctl restart slurmd` command being missed.
- There was an issue with the `slurmd.conf` file where the memory configuration was off by a few bytes, causing a discrepancy after a reboot.

## Solution
- The HPC Admin rebooted the node and fixed the `slurmd.conf` file to correct the memory configuration.
- The node was added to `/etc/dsh/group/all` to ensure proper configuration management.

## Lessons Learned
- Ensure all nodes are properly listed in configuration files to avoid missing necessary commands like `systemctl restart slurmd`.
- Verify memory configurations in `slurmd.conf` to prevent discrepancies that can cause job failures.
- Regular reboots and configuration checks can help maintain node stability and functionality.

## Follow-up Actions
- Monitor the node for any further issues.
- Ensure all nodes are correctly configured and included in necessary groups.
- Document and communicate any updates or changes to the Slurm configuration to prevent similar issues in the future.
---

### 2023080942002944_Increase%20in%20core%20hours.md
# Ticket 2023080942002944

 ```markdown
# HPC-Support Ticket: Increase in Core Hours

## Keywords
- Slurm
- AssocGrpNodeLimit
- Core Hours
- Tier3 Accounts
- Job Submission
- FAU
- Fritz

## Summary
A PhD student encountered an issue with submitting jobs on their `ihpc062h` account, receiving the error message "AssocGrpNodeLimit". The user assumed they had run out of core hours and requested an extension.

## Problem
- User unable to submit jobs due to "AssocGrpNodeLimit" error.
- Assumed issue was related to core hour limits.

## Investigation
- HPC Admin identified a general problem with Tier3 accounts in Slurm on Fritz.
- No clear limit was found, and the FAU limit was far from being reached.
- The issue was suspected to be related to recent Slurm changes.

## Root Cause
- The problem was traced to a misconfiguration in Slurm where a user's parent association was incorrectly set, leading to incorrect resource allocation and limit enforcement.

## Solution
- The incorrect parent association was corrected, resolving the issue.
- The problem was identified and fixed by the HPC Admin team.

## Lessons Learned
- Misconfigurations in Slurm can lead to unexpected job submission errors.
- Properly setting parent associations is crucial for accurate resource allocation and limit enforcement.
- Collaboration within the HPC Admin team is essential for identifying and resolving complex issues.
```
---

### 2022111542002553_Run%20python%20job%20on%20woody.md
# Ticket 2022111542002553

 # HPC Support Ticket: Run Python Job on Woody Cluster

## Subject
Run python job on woody

## User Issue
- User's existing PBS job script for running a Python program (ClusterLKMC.py) no longer works with the new Slurm batch system.
- The script uses `qsub` and PBS directives, which are not compatible with Slurm.

## Root Cause
- The Woody cluster has transitioned from Torque/PBS to Slurm.
- The user's script needs to be updated to use Slurm directives and `sbatch` for job submission.
- The Python module version has changed, and the user needs to update the script to load the correct module.

## Solution
1. **Update Job Script for Slurm:**
   - Replace PBS directives with Slurm directives.
   - Use `sbatch` instead of `qsub` for job submission.

2. **Load Correct Python Module:**
   - The available Python module is `python/3.9-anaconda`.
   - Update the script to load this module.

3. **Example Slurm Script:**
   ```bash
   #!/bin/bash -l
   #SBATCH --nodes=1
   #SBATCH --ntasks=1
   #SBATCH --cpus-per-task=4
   #SBATCH --time=12:00:00
   #SBATCH --job-name=Testjob_1

   # Load required modules
   module load python/3.9-anaconda

   # Change to work directory
   cd ${SLURM_SUBMIT_DIR}

   # Run the Python script
   python ClusterLKMC.py
   ```

## Keywords
- Slurm
- PBS
- Torque
- Python
- Module
- Job Script
- Woody Cluster
- Batch System
- qsub
- sbatch

## General Learnings
- Always check the cluster's documentation for updates on batch systems and available modules.
- Update job scripts to be compatible with the current batch system.
- Use the correct module versions available on the cluster.

## References
- [Slurm Documentation](https://hpc.fau.de/systems-services/documentation-instructions/batch-processing/)
- [Woody Cluster Details](https://hpc.fau.de/systems-services/documentation-instructions/clusters/woody-cluster/#collapse_5)
- [Transition Documentation](https://hpc.fau.de/2022/07/17/transition-from-woody-with-ubuntu-18-04-and-torque-to-woody-ng-with-almalinux8-and-slurm/)
---

### 2025030342001309_Jobs%20hingen%20ohne%20mir%20ersichtlichen%20Grund.md
# Ticket 2025030342001309

 ```markdown
# HPC Support Ticket: Jobs hingen ohne mir ersichtlichen Grund

## Keywords
- Job hangs
- NCCL INFO Using network IB
- Rescheduling jobs
- Active processes

## Problem Description
- User reported jobs hanging during restart.
- Affected job IDs: 34347, 34348 on Helma.
- Both jobs hung at the same log line: `NCCL INFO Using network IB`.
- User canceled jobs after 30 minutes and rescheduled them, which resolved the issue.

## Troubleshooting Steps
- HPC Admin asked the user to log into the Helma node and check active processes.
- User reported that some cores were still active, particularly by the `axolotl trainer`.

## Root Cause
- The exact root cause was not determined, but it was observed that some processes remained active on the nodes.

## Solution
- No specific solution was found. The ticket was closed as an observation for future reference.

## Lessons Learned
- Checking active processes on the node can provide insights into job hangs.
- Rescheduling jobs to different nodes can sometimes resolve hanging issues.
- Documenting such incidents can help identify patterns if similar issues arise in the future.
```
---

### 2023032442000935_interactive%20jobs.md
# Ticket 2023032442000935

 # HPC Support Ticket: Interactive Jobs Issue

## Keywords
- Interactive jobs
- `salloc`
- Job cancellation
- Time limit
- Slurm

## Problem Description
The user is experiencing issues with interactive jobs being cancelled before reaching the specified time limit. The user's job script (`Job.sh`) contains the following command:
```bash
salloc -N 1 --time=23:00:00
```
The job is submitted using:
```bash
$ salloc Job.sh
```
Two jobs appear in the queue, one with the requested runtime and another with a 10-minute runtime. Both jobs are cancelled after 10 minutes.

## Root Cause
The issue arises from the incorrect use of `salloc`. The user is running `salloc` within a script and then submitting the script with `salloc`, leading to nested `salloc` calls.

## Solution
To obtain an interactive shell, the user should directly run the `salloc` command without nesting it within a script. The correct command is:
```bash
salloc -N 1 --time=23:00:00
```
This command will allocate the requested resources and open an interactive shell.

## Reference
For more details on `salloc`, refer to the man page:
```
SYNOPSIS
    salloc [OPTIONS(0)...] [ : [OPTIONS(N)...]] [command(0) [args(0)...]]
    Option(s) define multiple jobs in a co-scheduled heterogeneous job. For more details about heterogeneous jobs see the document
    "https://slurm.schedmd.com/heterogeneous_jobs.html"
DESCRIPTION
    salloc is used to allocate a Slurm job allocation, which is a set of resources (nodes), possibly with some set of constraints (e.g. number of
    processors per node). When salloc successfully obtains the requested allocation, it then runs the command specified by the user. Finally, when the user specified command is
    complete, salloc relinquishes the job allocation.
    The command may be any program the user wishes. Some typical commands are xterm, a shell script containing srun commands, and srun (see the
    EXAMPLES section). If no command is specified, then salloc runs the user's default shell.
```

## Conclusion
The user should avoid nesting `salloc` calls and instead run the command directly to allocate resources for an interactive job.
---

### 2017102742000991_Batchprocessing%20qcat%20Befehl.md
# Ticket 2017102742000991

 ```markdown
# HPC-Support Ticket: Batchprocessing qcat Befehl

## Keywords
- qcat
- stdout
- Batch processing
- Torque user commands
- Job monitoring

## Problem Description
The user is unable to use the `qcat` command to view the stdout of a running job, as mentioned in the documentation. The command is not found.

## Root Cause
The `qcat` command is not available or has been deprecated.

## Solution
- The `qcat` command is not available.
- Alternative methods to view stdout of a running job need to be explored.

## General Learning
- Always check if commands mentioned in the documentation are still valid.
- Look for alternative methods to monitor job output if a command is deprecated.
```
---

### 2024011542003611_Required%20help%20while%20excuting%20Quantum%20ESPRESSO%20calculations.md
# Ticket 2024011542003611

 ```markdown
# HPC Support Ticket: Quantum ESPRESSO Calculation Error

## Keywords
- Quantum ESPRESSO
- Job script
- Error file
- stderr
- stdout
- #!/bin/bash -l

## Summary
A user encountered an error while executing Quantum ESPRESSO calculations on the HPC system. The user provided the shell script and output file but was unable to decipher the error.

## Problem
The user did not initially provide the error file (stderr) but only the output file (stdout). The error was not clear from the provided files.

## Solution
1. **Request for Error File**: The HPC Admin requested the user to re-run the job with the following lines in the job script to capture the error file:
   ```bash
   #SBATCH -e slurm-%j.err
   #SBATCH -o slurm-%j.out
   ```
2. **Job Script Correction**: The HPC Admin identified that the first line of the job script should be corrected to:
   ```bash
   #!/bin/bash -l
   ```
   Removing any additional text in that line resolved the error.

## Outcome
The error message disappeared after the user corrected the job script as advised by the HPC Admin.

## Lessons Learned
- Always ensure that both stdout and stderr files are provided when reporting errors.
- The first line of the job script should be `#!/bin/bash -l` to avoid potential errors.

## Closure
The ticket was closed as the problem was resolved.
```
---

### 2019111542000025_Nullbyte%20in%20HPC%20Job%20Query%20HTML.md
# Ticket 2019111542000025

 ```markdown
# Nullbyte in HPC Job Query HTML

## Keywords
- Nullbyte
- HPC Job Query
- HTML
- grep
- SLURM
- Meggie

## Problem Description
- User reported a nullbyte (`\x0`) before the closing tags (`</pre></body></html>`) in HPC Job Query HTML files.
- This caused `grep` without the `-a` option to treat the file as binary, resulting in messages like "Binary file 123456-sles000h.html matches" instead of displaying the match.

## Root Cause
- The nullbyte issue was specific to jobs on the Meggie system.
- It was related to how the job script was integrated into the HTML page.

## Solution
- HPC Admin identified and fixed the issue.
- All jobs completed on Meggie after 11:00 should no longer contain the nullbyte in the HPC Job Query output.

## Lessons Learned
- Specify the system (e.g., Meggie) where the issue occurs to facilitate troubleshooting.
- The problem was a SLURM-specific issue and did not affect other systems like Emmy or TinyX.
- Regular updates and fixes can resolve unexpected behaviors in job outputs.
```
---

### 2024053042000285_Server-Status%20von%20Meggie.md
# Ticket 2024053042000285

 # HPC Support Ticket: Server-Status von Meggie

## Keywords
- Slurm
- STAR-CCM+
- MPI processes
- ORTE daemon
- Network connectivity
- Job failure
- Temporary issues

## Problem Description
- User encountered issues starting a job on Meggie.
- Job log indicated an invalid job ID and an unexpected failure of an ORTE daemon.
- Previous simulation stopped without an error message around 18:30.

## Root Cause
- Temporary issues with Slurm on some nodes.

## Solution
- HPC Admins resolved the temporary issues with Slurm by midday.
- User confirmed that the system was functioning normally after the fix.

## Lessons Learned
- Temporary issues in Slurm can cause job failures and unexpected behavior.
- Network connectivity issues, including firewalls and routing, can affect MPI processes.
- Regular checks and maintenance of the Slurm system are essential to prevent such issues.

## Actions Taken
- HPC Admins investigated and resolved the Slurm issues.
- User confirmed the resolution and normal functioning of the system.

## Follow-up
- Monitor Slurm for any recurring issues.
- Ensure network connectivity and routing are properly configured for MPI processes.

## References
- HPC-Blog for system status updates.
- Support email: support-hpc@fau.de
- HPC website: [hpc.fau.de](https://hpc.fau.de/)
---

### 2019012142001942_Aufgeh%C3%83%C2%A4ngter%20Job%20%281046788%29%20auf%20Emmy.md
# Ticket 2019012142001942

 # HPC Support Ticket: Hanging Job on Emmy

## Keywords
- Hanging job
- Walltime
- Job cancellation
- qdel command
- Emmy cluster

## Problem Description
- A job (ID: 1046788) on the Emmy cluster is hanging.
- The job has exceeded its walltime of 8 minutes and has been running for several hours.
- No output is being produced by the job.
- Attempting to cancel the job using the `qdel` command results in the error message: `qdel: Invalid request MSG=job cancel in progress 1046788.eadm`.

## Root Cause
- The job has entered a state where it is not responding to cancellation requests, possibly due to an issue with the job script or the cluster's job management system.

## Solution
- The HPC Admins need to investigate and manually terminate the job if necessary.
- The user should be advised to check their job script for any issues that might cause it to hang.

## General Learnings
- Jobs can sometimes hang and become unresponsive to cancellation requests.
- The `qdel` command may not always successfully cancel a job, especially if the job is in a problematic state.
- HPC Admins may need to intervene to manually terminate hanging jobs.
- Users should be aware of the walltime for their jobs and monitor them accordingly.
---

### 2024070242002831_Job%20cancellation%20help.md
# Ticket 2024070242002831

 # Job Cancellation Help

## Keywords
- Job cancellation
- Slurm
- squeue
- Job resubmission loop
- Output directory
- Hard cap
- Email notifications

## Problem Description
- User accidentally saved script output to the wrong directory, causing jobs to hit the hard cap and fail.
- Jobs mysteriously restarted and entered a resubmission loop.
- User unable to cancel jobs using `squeue` or job ID from email notifications.
- Jobs not listed under user's account in `squeue`.

## Root Cause
- Incorrect output directory led to jobs failing due to hard cap.
- Job scripts were configured to resubmit upon completion, leading to a loop.
- User lacked necessary permissions or jobs were not properly associated with the user's account.

## Solution
- HPC Admin canceled all user jobs on Alex.
- Admin deleted pending slurm emails from the mail queue.

## Lessons Learned
- Ensure job scripts save output to the correct directory with sufficient storage.
- Monitor job status and understand job dependencies to prevent resubmission loops.
- If jobs are not listed in `squeue`, consult HPC Admin for assistance.
- Properly configure job scripts and understand their behavior to prevent unexpected resubmissions.

## Related Commands
- `squeue`: View job status.
- `scancel`: Cancel jobs using job ID.

## Related Tools
- Slurm workload manager.
---

### 2019022842002589_Issue%20with%20MEGGIE.md
# Ticket 2019022842002589

 ```markdown
# HPC Support Ticket: Issue with MEGGIE

## Problem Description
- User's job on MEGGIE terminates within the first two seconds.
- No output files are generated for debugging.
- User needs guidance on creating a sample script for job submission on MEGGIE.

## Root Cause
- Missing subdirectory for STDOUT/STDERR files.
- Incorrect use of `PIN="-pin 0_1..."` in the script.

## Solution
- Ensure the directory for STDOUT/STDERR files exists before the job starts.
- Remove `PIN="-pin 0_1..."` as MEGGIE uses native `srun/mpirun`.
- Explicitly specify STDOUT/STDERR files using `#SBATCH --output` and `#SBATCH --error`.

## Key Learnings
- SLURM requires the directory for STDOUT/STDERR files to exist before the job starts.
- Subdirectories for simulation results can be created within the job script.
- Use native `srun/mpirun` on MEGGIE without RRZE-extended wrappers.
- Explicitly specify STDOUT/STDERR files to avoid issues with missing directories.

## Additional Notes
- User was able to resolve the issue with subdirectories and proper STDOUT/STDERR files.
- For further details, refer to the `sbatch` man page.
```
---

### 2023071842000029_extending%20HPC%20account%20-%20iwi5129h.md
# Ticket 2023071842000029

 # HPC Support Ticket: Extending HPC Account Capacity

## Keywords
- HPC account extension
- CPU capacity
- Jupyterhub
- SLURM scheduler
- Batch processing

## Problem
- User requested an extension of their HPC account capacity from 2 CPUs to 8 CPUs for an ongoing research project.
- User's IDM username: `xi53ynoq`

## Root Cause
- User was likely using local jobs on Jupyterhub, which has restricted resources.
- No throttling was in place for the user's account, indicating no specific CPU limit was set.

## Solution
- HPC Admins advised the user to submit jobs through the SLURM scheduler instead of using local jobs on Jupyterhub.
- Provided documentation link for batch processing: [Batch Processing Documentation](https://hpc.fau.de/systems-services/documentation-instructions/batch-processing/)

## General Learnings
- Jupyterhub has limited resources and is not suitable for production jobs.
- Users should utilize the SLURM scheduler for submitting jobs that require more resources.
- Batch processing is the recommended method for running large-scale computations on the HPC cluster.

## Follow-up Actions
- If users encounter similar issues, direct them to the batch processing documentation.
- Encourage the use of SLURM for job submissions requiring more CPUs.
---

### 2018052842002736_node%20failure%20m0933.md
# Ticket 2018052842002736

 ```markdown
# HPC Support Ticket: Node Failure m0933

## Keywords
- Node failure
- Job aborted
- OOM (Out of Memory)
- SLURM
- srun
- slurmstepd
- Communication timeouts

## Summary
A user's job was terminated due to a node failure on m0933. The error message indicated an OOM condition. The HPC Admin identified that another user's Linpack tests caused the failure, affecting multiple nodes.

## Root Cause
- Node m0933 experienced an OOM condition.
- Linpack tests by another user caused the node failure.

## Solution
- The HPC Admin identified the cause as Linpack tests by another user.
- No specific solution was provided in the conversation, but further investigation into communication timeouts with uninvolved nodes was suggested.

## General Learnings
- Node failures can be caused by memory-intensive tests like Linpack.
- OOM conditions can lead to job abortions and node failures.
- Investigate communication timeouts with uninvolved nodes for a comprehensive understanding of the issue.
```
---

### 2019110342000646_qstat%20in%20cron-environment%20nicht%20gefunden%20auf%20woody3.md
# Ticket 2019110342000646

 ```markdown
# HPC Support Ticket: qstat Not Found in Cron Environment on woody3

## Keywords
- qstat
- qsub
- cron job
- PATH
- module
- torque
- woody3
- meggie1

## Problem Description
- User reported that `qstat` and `qsub` commands were not found in a cron job environment on woody3.
- The issue did not occur on meggie1 with `squeue` and `sbatch`.

## Root Cause
- On woody3, `qsub` and `qstat` are provided via a module which is not loaded in the cron job environment.
- Additional wrappers around `qsub` and `qstat` are used to handle Tiny*-Cluster processing.

## Solution
- Quick fix: Manually set the PATH in the cron job script:
  ```bash
  PATH=$PATH:/apps/torque/current/bin
  ```
- Proper fix: Load the module in the cron job script:
  ```bash
  eval `tclsh /apps/modules/modulecmd.tcl bash autoinit`
  module add torque/current
  ```

## General Learnings
- Ensure that necessary modules are loaded in cron job environments.
- Understand the differences in command availability and module loading between different clusters (e.g., woody3 vs. meggie1).
- Use module commands to load required software environments in scripts.
```
---

### 42148580_Fwd%3A%20PBS%20JOB%20368095.ladm1.md
# Ticket 42148580

 ```markdown
# HPC Support Ticket: PBS Job Submission Error

## Subject
Fwd: PBS JOB 368095.ladm1

## Keywords
- PBS Job Submission
- Error Message
- Aborted by PBS Server
- Job cannot be executed

## Problem Description
User experienced issues submitting jobs to the HPC server. The job submission resulted in an error message indicating that the job was aborted by the PBS server and could not be executed.

## Error Message
```
PBS Job Id: 368095.ladm1
Job Name:   dppc.sh
Exec host:
l1331/23+l1331/22+l1331/21+l1331/20+l1331/19+l1331/18+l1331/17+l1331/16+l1331/15+l1331/14+l1331/13+l1331/12+l1331/11+l1331/10+l1331/9+l1331/8+l1331/7+l1331/6+l1331/5+l1331/4+l1331/3+l1331/2+l1331/1+l1331/0+l1330/23+l1330/22+l1330/21+l1330/20+l1330/19+l1330/18+l1330/17+l1330/16+l1330/15+l1330/14+l1330/13+l1330/12+l1330/11+l1330/10+l1330/9+l1330/8+l1330/7+l1330/6+l1330/5+l1330/4+l1330/3+l1330/2+l1330/1+l1330/0+l1329/23+l1329/22+l1329/21+l1329/20+l1329/19+l1329/18+l1329/17+l1329/16+l1329/15+l1329/14+l1329/13+l1329/12+l1329/11+l1329/10+l1329/9+l1329/8+l1329/7+l1329/6+l1329/5+l1329/4+l1329/3+l1329/2+l1329/1+l1329/0+l1328/23+l1328/22+l1328/21+l1328/20+l1328/19+l1328/18+l1328/17+l1328/16+l1328/15+l1328/14+l1328/13+l1328/12+l1328/11+l1328/10+l1328/9+l1328/8+l1328/7+l1328/6+l1328/5+l1328/4+l1328/3+l1328/2+l1328/1+l1328/0
Aborted by PBS Server
Job cannot be executed
See Administrator for help
```

## Root Cause
The job was aborted by the PBS server, indicating a potential issue with the job script or server configuration.

## Solution
- Check the job script for any syntax errors or incorrect resource requests.
- Verify that the PBS server is functioning correctly and has available resources.
- Consult with HPC Admins for further assistance if the issue persists.

## Notes
- The user provided the location of the job script for reference: `/home/woody/bccb/bccb05/projects/lipids/dppc/dihoff_OS_C2_CT_CT_sn1+sn2_C2_CT_CT_CT_sn1+sn2/dppc.sh`
- The error message suggests contacting the administrator for help, indicating a potential server-side issue.

## Next Steps
- Review the job script and ensure it adheres to the correct format and resource allocation.
- Contact HPC Admins if the issue cannot be resolved through script modifications.
```
---

### 2019080742000645_%5Bwoody%5D%20Job%20bricht%20ab%20mit%20Meldung%20%22Permission%20denied%22.md
# Ticket 2019080742000645

 # HPC Support Ticket: Job Aborts with "Permission Denied" Error

## Keywords
- Job submission
- Permission denied
- Node-specific issue
- Torque job management
- Job script

## Problem Description
- User reports that some jobs on the HPC cluster (woody) abort immediately after starting with a "Permission denied" error.
- The error message indicates a problem accessing the job script file in `/var/spool/torque/mom_priv/jobs/`.
- The issue is observed to occur specifically when certain nodes (e.g., w1009, w1207) are used as the master node.

## Root Cause
- The root cause of the problem is not explicitly identified in the conversation, but it is suspected to be related to the specific nodes mentioned.
- The issue might be due to a configuration or permission problem on these nodes.

## Troubleshooting Steps
1. **Node Reset**: The HPC Admin reset the problematic node (w1009) to see if the issue persists.
2. **Job Script Review**: The HPC Admin requested the job script used by the user for further analysis.

## Solution
- The issue was not resolved in the provided conversation. Further investigation is needed, possibly involving a detailed review of the job script and node configurations.

## Notes
- The problem reoccurred after some time, affecting multiple jobs sequentially on the same node.
- The user suggested that the issue might be related to the `module unload gcc` command in the job script, but this was not confirmed.

## Next Steps
- Continue monitoring the problematic nodes.
- Analyze the job script provided by the user to identify any potential issues.
- Consider checking the permissions and configurations on the affected nodes.

## Conclusion
- The issue requires further investigation to determine the exact cause and implement a permanent solution.

---

This documentation can be used as a reference for similar issues in the future.
---

### 2023052542001572_slurm%20jobs.md
# Ticket 2023052542001572

 ```markdown
# HPC-Support Ticket: Slurm Jobs Termination Issue

## Keywords
- Slurm
- Job Termination
- Job Script
- Priority
- GPU Partition

## Problem Description
User's jobs are being terminated after a short period. The user suspects low priority might be the cause but is unsure.

## Log Excerpt
```
srun: forcing job termination
5/2400 [15:18<03:06,  2.17it/s, v_num=45, val_loss_dB=-7.97, train_loss_dB=-7.99]
srun: Job step aborted: Waiting up to 32 seconds for job step to finish.
slurmstepd-tg080: error: *** STEP 596958.0 ON tg080 CANCELLED AT 2023-05-24T18:33:11 ***
Epoch 8:  83%|████████▎ | 1997/2400 [15:19<03:05,  2.17it/s, v_num=45, val_loss_dB=-7.97, train_loss_dB=-7.99]
srun: error: tg080: task 0: Killed
srun: launch/slurm: _step_signal: Terminating StepId=596958.0
```

## Root Cause
The issue is likely due to the way the job is being started. The user is not using a job script, which can lead to job termination issues.

## Solution
The HPC Admin recommended using a job script to submit the job. The script should look like this:

```bash
#!/bin/bash -l
#
##SBATCH --ntasks=1
#
#SBATCH --time=00:10:00
#
#SBATCH --gres=gpu:gtx3080:1
#
##SBATCH --export=NONE
#
##SBATCH --cluster=tinygpu

unset SLURM_EXPORT_ENV
module load python
source activate <conda-env>
export http_proxy://proxy:80
export https_proxy://proxy:80
python <my-code.py>
```

The job can then be started with:
```bash
sbatch <script>
```

## General Learning
- **Job Scripts**: Using job scripts is a best practice for submitting jobs in HPC environments. It ensures that all necessary environment variables and modules are loaded correctly.
- **Priority**: Job priority in Slurm affects the start time, not the termination.
- **Logging**: Proper logging and error messages can help diagnose issues more effectively.
```
---

### 2023091942003708_Batch%20job%20freezes%20after%20some%20time.md
# Ticket 2023091942003708

 # HPC Support Ticket: Batch Job Freezes After Some Time

## Keywords
- Batch job freeze
- SLURM logfiles
- Neural network training
- Job monitoring
- Race condition

## Summary
A user reported that their batch jobs were freezing randomly after running for some time while training a neural network. The issue was observed only on the cluster and not in local runs.

## Ticket Conversation
1. **User Report**:
   - Batch jobs freeze randomly after certain epochs.
   - Code runs fine locally but freezes on the cluster.
   - Provided job IDs and SLURM logfile locations.

2. **HPC Admin Response**:
   - Requested SLURM logfile locations.
   - Checked logs on `atuin` and the Alex-node but found nothing suspicious.
   - Suggested monitoring the job while it is running/stuck.
   - After further monitoring, no hardware issues were detected.
   - Suspected a race condition in the user's code.

## Root Cause
- The exact root cause was not determined, but a race condition in the user's code was suspected.

## Solution
- No definitive solution was provided. The user was advised to check for race conditions in their code.

## Learnings
- Always provide SLURM logfile locations when reporting job issues.
- Monitoring jobs while they are running/stuck can help identify issues.
- Race conditions in code can cause jobs to freeze randomly.
- Hardware issues should be ruled out by checking live monitoring and logs.

## Next Steps
- Users should review their code for potential race conditions.
- Continue monitoring jobs and provide detailed logs for further analysis if the issue persists.

## References
- SLURM logfiles: `/home/atuin/b143dc/b143dc16/i2i_via_disentanglement/dumps/SLURM-843775.err`
- Job IDs: 843746, 843775, 845063

## Support Team
- HPC Admins: Johannes Veh
- 2nd Level Support Team: Lacey, Dane (fo36fizy), Kuckuk, Sebastian (sisekuck), Lange, Florian (ow86apyf), Ernst, Dominik (te42kyfo), Mayr, Martin
- Head of the Datacenter: Gerhard Wellein
- Training and Support Group Leader: Georg Hager
- NHR Rechenzeit Support: Harald Lanig
- Software and Tools Developer: Jan Eitzinger, Gruber
---

### 2025021442001004_New%3A%20Batch%20job%20submission%20issue.md
# Ticket 2025021442001004

 # Batch Job Submission Issue

## Keywords
- Batch job submission
- `cpu_per_task`
- `sbatch` error
- Node configuration
- Maintenance
- Conference deadline

## Problem Description
After the maintenance of the cluster, the user encountered an issue where submitting a job with `cpu_per_task > 1` resulted in the error: "sbatch: error: Batch job submission failed: Requested node configuration is not available."

## Root Cause
The root cause of the problem was related to the node configuration specified in the job submission script. Specifically, the `--node=1` parameter was causing the issue.

## Solution
The user discovered that removing the `--node=1` parameter allowed the job to be submitted successfully.

## General Learnings
- After cluster maintenance, job submission scripts may need to be adjusted.
- The `--node` parameter can affect job submission, especially when combined with `cpu_per_task > 1`.
- Removing or adjusting the `--node` parameter can resolve submission errors related to node configuration.

## Next Steps
- Ensure that job submission scripts are reviewed and updated after any cluster maintenance.
- Document any changes in node configuration or job submission parameters that may affect users.
- Provide guidance on troubleshooting common job submission errors, including those related to node configuration.
---

### 2022111842001067_SLURM%20auf%20tinyx.nhr.fau.de%20kaputt.md
# Ticket 2022111842001067

 ```markdown
# SLURM Issue on tinyx.nhr.fau.de

## Keywords
- SLURM
- Reboot
- DNS SRV lookup
- Configuration source
- tinyx.nhr.fau.de
- squeue

## Problem Description
After an unannounced reboot, SLURM on `tinyx.nhr.fau.de` became unusable. The user encountered the following errors when trying to use `squeue`:

```
squeue: error: resolve_ctls_from_dns_srv: res_nsearch error: Unknown host
squeue: error: fetch_config: DNS SRV lookup failed
squeue: error: _establish_config_source: failed to fetch config
squeue: fatal: Could not establish a configuration source
```

## Root Cause
The root cause of the problem was that SLURM got stuck on the login node after the reboot, leading to DNS SRV lookup failures.

## Solution
The HPC Admin identified and resolved the issue by fixing the SLURM configuration on the login node.

## Lessons Learned
- Unannounced reboots can cause SLURM to malfunction.
- DNS SRV lookup failures can prevent SLURM from establishing a configuration source.
- Regular monitoring and quick response to user reports can help resolve such issues promptly.
```
---

### 2018071942002428_pbspro%20und%20motd.md
# Ticket 2018071942002428

 # HPC Support Ticket: PBS Pro and MOTD

## Keywords
- PBS Pro
- MOTD (Message of the Day)
- Interactive Job
- SSH
- LLC Prefetcher
- OMP_NUM_THREADS
- qstat

## Problem
- **Root Cause**: The MOTD message is not displayed when starting an interactive job with PBS Pro. This was noticed when the user logged in via SSH and saw a message about the LLC Prefetcher being disabled, which was not visible during the interactive job session.

## Discussion
- **HPC Admin**: Mentioned the issue of PBS Pro setting `OMP_NUM_THREADS` and provided a note about TORQUE no longer being open-source.
- **HPC Admin**: Discussed the complexity of moving information due to default restrictions on nodes, such as not being able to run `qstat`.

## Solution
- No direct solution was provided in the conversation. Further investigation is needed to determine how to display MOTD messages during interactive job sessions in PBS Pro.

## General Learnings
- PBS Pro does not display MOTD messages during interactive job sessions.
- PBS Pro sets `OMP_NUM_THREADS`, which may need to be addressed.
- Default restrictions on nodes, such as not being able to run `qstat`, can complicate troubleshooting and information management.

## Next Steps
- Investigate how to configure PBS Pro to display MOTD messages during interactive job sessions.
- Explore options to manage or disable PBS Pro's setting of `OMP_NUM_THREADS`.

## References
- [Adaptive Computing TORQUE](http://www.adaptivecomputing.com/products/torque/)
---

### 2024022842002613_Job%20failures..md
# Ticket 2024022842002613

 ```markdown
# HPC Support Ticket: Job Failures

## Subject
Job failures.

## User Report
- **Job ID 1215991**: Node failure.
- **Job ID 1215989**: Error: f1102: tasks 126, 128, 136, 142: Bus error (core dumped).
- **Job ID 1215992**: Error message from inside the program, but cannot reproduce the error on any platform.

## HPC Admin Response
- **Job ID 1215991**: Problem with the node state in Slurm.
- **Job ID 1215989**: Node (f1102) had an uncorrectable memory error and rebooted.
- **Job ID 1215992**: No issues found with the nodes; likely an issue with the user's program.

## Root Cause
- **Job ID 1215991**: Node failure due to Slurm node state issue.
- **Job ID 1215989**: Uncorrectable memory error on node f1102.
- **Job ID 1215992**: Possible issue within the user's program.

## Solution
- **Job ID 1215991**: Investigate and resolve Slurm node state issues.
- **Job ID 1215989**: Replace or repair the faulty node (f1102).
- **Job ID 1215992**: User should debug their program to identify and fix the error.

## Keywords
- Node failure
- Slurm node state
- Uncorrectable memory error
- Bus error
- Program error
```
---

### 2023081842002614_Chain%20jobs%20with%20Signals%3F.md
# Ticket 2023081842002614

 # Chain Jobs with Signals

## Keywords
- Signal handling
- Job script
- Checkpoints
- SLURM
- Bash

## Problem
User remembers an example script for catching the kill signal at the end of a job's runtime to save checkpoints, tidy up, and possibly resubmit the job. However, they cannot find this example on the website.

## Solution
HPC Admin provides external documentation links for handling signals in SLURM job scripts:
- [GWDG Documentation](https://docs.gwdg.de/doku.php?id=en:services:application_services:high_performance_computing:running_jobs_slurm:signals)
- [CRIANN Documentation](https://services.criann.fr/en/services/hpc/cluster-myria/guide/signals-sent-by-slurm/)
- [USC HPC Discourse](https://hpc-discourse.usc.edu/t/signalling-a-job-before-time-limit-is-reached/314)

## General Learning
- Signals can be trapped in bash scripts to perform cleanup tasks before a job is terminated.
- External resources can be valuable when internal documentation is not available.
- Proper signal handling can help in saving checkpoints and resubmitting jobs.
---

### 2020050142000793_Emmy%3A%20Rechnungen%20laufen%20pl%C3%83%C2%B6tzlich%20%22ultra%20langsam%22.md
# Ticket 2020050142000793

 # HPC Support Ticket: Emmy Jobs Running Slowly

## Keywords
- VASP jobs
- Emmy cluster
- Slow performance
- Infiniband network
- Port deactivation

## Problem Description
- User reported that copy&paste VASP jobs on Emmy were running extremely slowly, as if only one node was computing.
- Job statistics appeared abnormal.
- Affected jobs: 1295809, 1295807, 1295822, 1295825, 1295260.
- Previous jobs (1295803, 1295802) ran normally.

## Root Cause
- Possible issue with the Infiniband network port in the backbone area.

## Solution
- HPC Admin deactivated a suspected faulty port in the Infiniband network.
- Jobs resumed normal performance the next morning.

## Lessons Learned
- Network issues, such as faulty ports, can cause significant performance degradation in HPC jobs.
- Proactive monitoring and quick response to network anomalies can help maintain system performance.
- Deactivating a suspected faulty port can resolve performance issues if the root cause is network-related.

## Next Steps
- Continue monitoring the network for any further anomalies.
- Consider implementing automated network diagnostics to quickly identify and resolve similar issues in the future.
---

### 2021070642002777_Eingefrorene%20Jobs%20auf%20Emmy%20von%20Account%20mpp3007h.md
# Ticket 2021070642002777

 ```markdown
# HPC-Support Ticket: Frozen Jobs on Emmy Cluster

## Keywords
- Frozen Jobs
- Emmy Cluster
- Job Termination
- qdel Command
- Node Reboot

## Problem Description
User reported three jobs on the Emmy cluster that were not responding to termination commands and had exceeded their allocated runtime.

## Root Cause
The jobs were frozen and not responding to the `qdel` command.

## Solution
HPC Admins rebooted the affected nodes, which resolved the issue by terminating the frozen jobs.

## Lessons Learned
- Frozen jobs can occur and may not respond to standard termination commands.
- Rebooting the affected nodes can resolve the issue of frozen jobs.
- Regular monitoring of job statuses can help identify and address such issues promptly.
```
---

### 2022030842003063_Node%20specific%20job%20fails.md
# Ticket 2022030842003063

 # Node Specific Job Failures

## Keywords
- Node-specific job failures
- STDOUT quota exceeded
- Job logs
- Temporary files
- Quota management

## Problem Description
- Jobs failing after a few seconds with minimal standard output and empty error logs.
- Failures observed on specific nodes.
- Previous jobs had produced excessive STDOUT, exceeding the quota on the temporary filesystem.

## Root Cause
- Large STDOUT files from previous jobs (November 2021) exceeded the quota on the temporary filesystem.
- These files were not properly cleaned up, causing subsequent jobs on the affected nodes to fail due to quota issues.

## Solution
- HPC Admins identified and removed the large STDOUT files from the temporary filesystem.
- This resolved the quota issue, allowing jobs to run successfully on the affected nodes.

## Lessons Learned
- Monitor job outputs to prevent excessive file sizes.
- Ensure proper cleanup of temporary files after job completion or failure.
- Regularly check and manage quotas on temporary filesystems to prevent disruptions.

## Additional Notes
- The `qcat -o -f` command can be used to view large log files.
- Consider implementing automated cleanup jobs for temporary files to prevent future issues.
---

### 2020011442000294_Jobs%20auf%20TinyEth%20laufen%20tagelang%2C%20ein%20Job%20wird%20st%C3%83%C2%A4ndig%20gel%C3%83%C2%B.md
# Ticket 2020011442000294

 ```markdown
# HPC Support Ticket: Jobs auf TinyEth laufen tagelang, ein Job wird ständig gelöscht

## Problem Description
- **User Observation**: Jobs submitted with a walltime of 12 hours run for days despite completing successfully before the walltime.
- **Symptoms**:
  - Jobs continue running beyond their specified walltime.
  - One job is repeatedly deleted, causing the user's mailbox to be flooded with deletion notifications.
  - Example job details:
    ```
    PBS Job Id: 32316.twadm1.rrze.uni-erlangen.de
    Job Name: 1578240530_Job_363.sh
    Exec host: te008/2
    job deleted
    Job deleted at request of root@twadm1.rrze.uni-erlangen.de
    MOAB_INFO: job exceeded wallclock limit
    ```

## Root Cause
- **HPC Admin Response**: The PBS daemon on several TinyEth nodes crashed, preventing the server from removing the jobs.

## Solution
- **HPC Admin Action**: The PBS daemon needs to be restarted or fixed to ensure proper job management.
- **Status**: The issue should be resolved if the PBS daemon is running correctly. However, the daemon has a tendency to crash unexpectedly on various clusters.

## Keywords
- PBS daemon crash
- Job walltime exceeded
- Job deletion loop
- TinyEth cluster
- qcat output

## General Learning
- Ensure the PBS daemon is running correctly to manage job lifecycles.
- Monitor for unexpected crashes of the PBS daemon on HPC clusters.
- Check job status and deletion notifications to identify issues with job management.
```
---

### 2024021542003021_35k%20jobs%20from%20Alex%20removed%20from%20queue%20-%20b105dc10.md
# Ticket 2024021542003021

 # HPC Support Ticket: Excessive Job Submission

## Keywords
- Job submission limit
- Slurm response time
- Job cancellation
- Script modification

## Problem
- **Root Cause:** User submitted 36,000 jobs, overwhelming the Slurm scheduler.
- **Symptom:** Slurm became unresponsive, affecting other users.

## Solution
- **Immediate Action:** HPC Admins removed most of the user's jobs from the queue to restore Slurm's responsiveness.
- **Long-term Fix:** User agreed to modify their script to submit jobs in chunks, adhering to the 500 job upper limit.

## Key Takeaways
- **Job Submission Limit:** There is a strict upper limit of 500 jobs per user, even if not yet enforced by the system.
- **Communication:** Users should contact support if they have doubts about their job submission strategies.
- **Script Management:** Users should manage their job submission scripts to avoid overwhelming the scheduler.

## Follow-up
- HPC Admins may consider enforcing the job submission limit at the system level to prevent similar issues in the future.
---

### 42288921_m%C3%83%C2%B6gliches%20Problem%20von%20Rechenknoten.md
# Ticket 42288921

 ```markdown
# HPC Support Ticket: Possible Issue with Compute Nodes

## Keywords
- Compute nodes: e0116, e0117, e0118, e0119
- Error message: "send desc error"
- Infiniband
- Reboot

## Problem Description
A computation job on nodes e0116, e0117, e0118, and e0119 repeatedly failed at 10 AM. The error message "send desc error" was found in the error file. The same job ran successfully on other nodes.

## Root Cause
Possible issue with Infiniband on one of the four nodes.

## Solution
- The nodes did not show any anomalies but were scheduled for a reboot as a precautionary measure.

## Lessons Learned
- Avoid replying to old tickets with new, unrelated issues.
- Rebooting nodes can be a temporary solution to resolve intermittent issues.
- Regular monitoring and maintenance of compute nodes are essential to prevent such issues.

## Follow-up
- Monitor the nodes after the reboot to ensure the issue does not recur.
- If the problem persists, further investigation into the Infiniband configuration may be necessary.
```
---

### 2021062242001463_Job%20auf%20Emmy%201498684%20corz09.md
# Ticket 2021062242001463

 ```markdown
# HPC-Support Ticket: Job auf Emmy 1498684 corz09

## Keywords
- Job monitoring
- Activity monitoring
- Benchmark tests
- ANSYS CFX
- Output suppression

## Summary
A job on Emmy (1498684) exhibited unusual activity patterns, with measurable activity only after 30 minutes, followed by a period of inactivity after 1.5 hours.

## Root Cause
- The job showed no activity after an initial period of activity.
- Possible benchmark tests were being run.

## Solution
- HPC Admin advised the user to check the job and the program being used.
- If the job was for benchmark tests, the user was referred to a document (Running-HPC-Benchmarks-with-ANSYS-CFX.pdf) that includes a CCL to suppress output.

## Lessons Learned
- Regularly monitor job activity to identify unusual patterns.
- Provide users with documentation on how to suppress unnecessary output for benchmark tests.
- Ensure users are aware of the importance of checking job and program configurations.
```
---

### 2018100542001396_Issue%20with%20jobs%20on%20Woody.md
# Ticket 2018100542001396

 ```markdown
# Issue with Jobs on Woody

## Keywords
- Job submission
- Node type specification
- Large log files
- Disk quota
- Node cleanup
- Output redirection

## Summary
A user experienced issues with job submissions on Woody when specifying node types (e.g., sl32g). Jobs ended abruptly without error messages. The root cause was identified as large log files filling up the node's disk space, leading to job crashes.

## Root Cause
- Large log files generated by jobs filled the node's disk space.
- Disk quota prevented further job execution on affected nodes.

## Solution
- HPC Admins cleaned up the affected nodes.
- User was advised to reduce the amount of output to stdout to prevent large log files.
- No automatic cleanup solution available; manual intervention required.

## Additional Information
- Log files are stored on the system's main partition, which has limited space.
- Files in `/tmp` are automatically removed after job completion.
- Redirecting output to a personal folder is not recommended due to potential impact on the fileserver.

## Recommendations
- Monitor job output to prevent excessive log file generation.
- Ensure proper error handling in job scripts to avoid large log files.
- Contact HPC support for manual cleanup if the issue recurs.
```
---

### 2019010842001413_Shared%20libraries%20error%20beim%20Absenden%20eines%20NCL%20scripts%20mit%20sbatch%20to%20slurm.md
# Ticket 2019010842001413

 ```markdown
# HPC Support Ticket: Shared Libraries Error with NCL Script Submission via sbatch to Slurm

## Keywords
- Shared libraries error
- NCL script
- sbatch
- Slurm
- libgomp.so.1
- libgfortran.so.3
- LD_LIBRARY_PATH
- Module loading
- Job script

## Problem Description
The user encountered an error when submitting an NCL script via `sbatch` to Slurm. The script ran without errors in the command line but took too long and was automatically terminated. When submitted as a job, the error message indicated a missing shared library (`libgomp.so.1`). The user had already added the library path to `LD_LIBRARY_PATH`, but the error persisted.

## Root Cause
The compute nodes have a limited operating system installation compared to the login nodes, and the required libraries (`libgomp.so.1` and `libgfortran.so.3`) were not available on the compute nodes.

## Solution
1. **Temporary Solution 1:** Load the `gcc/4.9.4` module, which should contain the required libraries. Ensure the job script starts with `#!/bin/bash -l` to enable module loading.
2. **Temporary Solution 2:** Copy the required libraries (`libgomp.so.1` and `libgfortran.so.3`) from the login node to a user directory and include this directory in the `LD_LIBRARY_PATH`.

## Outcome
The user successfully resolved the issue by copying the required libraries to their directory and including them in the `LD_LIBRARY_PATH`.

## General Learnings
- Compute nodes may have a limited OS installation compared to login nodes.
- Missing shared libraries can cause errors when submitting jobs.
- Temporary solutions include loading appropriate modules or copying libraries to user directories.
- Ensure job scripts are configured correctly for module loading (`#!/bin/bash -l`).
```
---

### 2020042442000957_Woody%20%7C%20-W%20depend%3Dafterok%3A....md
# Ticket 2020042442000957

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject: Woody | -W depend=afterok:...

### Keywords:
- Job dependency
- `qsub`
- `depend=afterok`
- Job deletion
- PBS Server
- Job status

### Summary:
A user reported issues with job dependencies using the `depend=afterok` parameter in `qsub`. The second job was deleted instead of being executed after the first job completed successfully.

### Root Cause:
- The issue was likely due to a one-time error in the scheduler log related to the job ID.

### Troubleshooting Steps:
1. **User Report**: The user noticed that the second job was deleted instead of being executed after the first job completed.
2. **Admin Response**: The admin could not reproduce the issue and confirmed no recent updates.
3. **Further Investigation**: The admin requested the job script and `qsub` command for the deleted job.
4. **Log Analysis**: The admin found a one-time error in the scheduler log related to the job ID.

### Solution:
- The admin suggested retrying the job submission. If the issue persists, the user should report it again.

### General Learnings:
- Job dependencies can sometimes fail due to one-time errors in the scheduler.
- It is important to check the scheduler logs for any errors related to job IDs.
- If the issue cannot be reproduced, retrying the job submission is a viable solution.

### Conclusion:
The ticket was closed as the issue was considered a one-time error. The user was advised to retry the job submission and report back if the problem persists.
```
---

### 42354625_Woody%20ist%20so%20leer.md
# Ticket 42354625

 # HPC Support Ticket: Woody ist so leer

## Keywords
- Woody
- Batch system
- Job execution
- System issue

## Problem Description
- **User Issue:** Woody appeared idle but was not executing jobs.
- **Root Cause:** The batch system was stuck or malfunctioning.

## Solution
- **Admin Action:** The HPC Admin identified and resolved the issue with the batch system.
- **Resolution:** The batch system was fixed and jobs started executing again.

## General Learnings
- Batch system issues can prevent job execution even if the system appears idle.
- Regular monitoring and quick intervention by HPC Admins can resolve such issues promptly.

## Next Steps
- Continue monitoring the batch system for similar issues.
- Ensure users are informed about system status and any ongoing issues.
---

### 2021071642002623_Job%20vorzeitig%20beendet%3F.md
# Ticket 2021071642002623

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject: Job vorzeitig beendet?

### Keywords:
- Job termination
- Slurm reservation
- Time limit
- Exclude nodes
- Stromversorgung (power supply)
- Daten-SSDs (data SSDs)

### Root Cause:
- The job was terminated due to the expiration of a Slurm reservation.

### Solution:
- Use `--exclude=tg09[5-7]` to avoid nodes with expiring reservations.
- Ensure reservations are extended if necessary.
- Monitor upcoming maintenance that may affect job execution.

### General Learnings:
- **Slurm Reservations**: Ensure reservations cover the entire job duration to prevent premature termination.
- **Node Exclusion**: Use `--exclude` to avoid nodes with known issues or expiring reservations.
- **Maintenance Notifications**: Be aware of upcoming maintenance that may affect job execution and plan accordingly.
- **Hardware Updates**: Stay informed about hardware updates and changes that may impact job scheduling.

### Additional Notes:
- The issue was due to a lack of experience with Slurm reservations.
- Future maintenance on the power supply may require job terminations with short notice.
- New data SSDs have been integrated, making previous exclusions unnecessary.
```
---

### 2019111942002605_qcat%20auf%20emmy%20und%20%C3%83%C2%84quivalent%20auf%20meggie%3F.md
# Ticket 2019111942002605

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject: qcat auf emmy und Äquivalent auf meggie?

### Keywords:
- qcat
- Emmy
- Meggie
- Spool-Verzeichnis
- stdout/stderr
- Jobende
- cat/less
- qstat
- Output_Path
- Error_Path

### Problem:
- User discovered `qcat` on the HPC website and found it useful.
- `qcat` does not seem to be available or working as expected on Emmy.
- User inquires about an equivalent tool on Meggie.

### Root Cause:
- `qcat` is a shell script that logs into the master node of a running job via SSH and outputs the file in the spool directory.
- On Emmy, the spool directory is not used, and output files are written directly to their final location.
- `qcat` on Emmy is located in `/apps/rrze/bin/qcat` but does not function as expected.

### Solution:
- On Emmy, output files can be viewed during the job using `cat/less`, although the last 4 KB may be missing.
- On Meggie, an equivalent command for `qcat -o` is:
  ```sh
  cat `qstat -f JOBID |grep 'Output_Path = ' | sed -e 's/.*://g'`
  ```
  For `qcat -e`:
  ```sh
  cat `qstat -f JOBID |grep 'Error_Path = ' | sed -e 's/.*://g'`
  ```
- `qcat` on Emmy now behaves similarly to other Torque clusters, tailing stdout/stderr without using SSH.

### General Learnings:
- `qcat` is a convenience tool for viewing job output files during execution.
- Different HPC systems may handle job output differently, affecting the usefulness of `qcat`.
- Equivalent commands can be constructed using `qstat` and `sed` to achieve similar functionality.
```
---

### 2020092442002071_qsub%20command%20hanging%20for%20all%20non-interactive%20jobs.md
# Ticket 2020092442002071

 ```markdown
# HPC Support Ticket: qsub Command Hanging for Non-Interactive Jobs

## Keywords
- qsub
- non-interactive jobs
- hanging command
- walltime parameter
- mount issues

## Issue Description
The user reported that the `qsub` command for submitting non-interactive jobs was hanging and not submitting the job to the queue. Interactive jobs were working fine.

## Troubleshooting Steps
1. **Parameter Verification**: HPC Admins verified if the user specified necessary parameters (nodes, walltime) in the `qsub` command or within the script.
2. **Walltime Format**: Ensured the walltime parameter was correctly formatted as `HH:MM:SS`.
3. **Script Execution**: User confirmed that the parameters were correctly specified in the script and ran `qsub -l nodes=1:ppn=40,walltime=01:00:00 testjob.sh`, but the issue persisted.

## Root Cause
The underlying issue was suspected to be related to hanging mount remnants from the old `/home/hpc` in the `pbs_server`. This affected only some users.

## Solution
HPC Admins fixed the mount issue in the `pbs_server`. The user confirmed that the problem was resolved after the fix.

## Conclusion
The issue was resolved by addressing the mount problem in the `pbs_server`. Users should ensure that their `qsub` commands and scripts include all necessary parameters and that the walltime is correctly formatted.
```
---

### 2024091642003873_Unerwarteter%20Timeout%20%26%20Wiederaufnahme.md
# Ticket 2024091642003873

 # HPC-Support Ticket Conversation Analysis

## Subject: Unerwarteter Timeout & Wiederaufnahme

### Keywords:
- Timeout
- Job Verlängerung
- Slurm
- Prolog hung
- Socket timed out
- Job step aborted

### General Learnings:
- Jobs can unexpectedly timeout due to underlying reservation issues.
- Slurm errors such as "Prolog hung" and "Socket timed out" can cause job aborts.
- Job extensions can be requested and granted by HPC Admins.
- High demand in the queue can delay job starts.

### Root Cause of the Problem:
- The initial job timeout was likely due to the underlying reservation expiring.
- Slurm errors caused job aborts, requiring restarts.

### Solution:
- HPC Admins extended the job multiple times to ensure completion.
- Users were advised to restart jobs after errors and request extensions as needed.

### Detailed Conversation Analysis:

#### Initial Issue:
- User reported an unexpected timeout of a long-running job (id:2038301) after 9.5 days.
- The job was previously extended to 14 days, but still timed out.

#### HPC Admin Response:
- HPC Admin acknowledged the issue and extended the new job (id:2055162).
- Mentioned high demand in the queue, which could delay job starts.

#### Subsequent Issues:
- User reported a job abort due to Slurm errors: "Prolog hung" and "Socket timed out."
- Job was restarted and successfully started.

#### Further Extensions:
- User requested and received multiple extensions for the job to ensure completion.
- HPC Admins granted extensions and advised on job status and queue demand.

#### Final Extension:
- User requested a final extension to avoid unexpected interruptions during the final save.
- HPC Admin granted the extension.

### Conclusion:
- Regular communication with HPC Admins is crucial for managing long-running jobs.
- Slurm errors can be mitigated by restarting jobs and requesting extensions as needed.
- High demand in the queue should be considered when planning job submissions.

### Recommendations:
- Monitor job status regularly and request extensions well in advance.
- Be prepared to restart jobs in case of Slurm errors.
- Consider queue demand when planning job submissions to avoid delays.
---

### 2021042742002466_Emmy%20Problem.md
# Ticket 2021042742002466

 ```markdown
# HPC Support Ticket: Emmy Problem

## Keywords
- Emmy
- Job failure
- Node reboot
- Interactive job
- Clearing Buffers and Caches

## Problem Description
- User experienced issues with job 1453812 on Emmy, which was started 6 times but never completed.
- User received multiple start emails and eventually removed the job from the queue.
- An interactive job (1453838) was started and assigned to a node but aborted during the "Clearing Buffers and Caches" stage.
- The job ran successfully the next day.

## Root Cause
- Issues with some nodes on Emmy, including automatic reboots.

## Solution
- The problem was not due to user error but rather due to node issues.
- The nodes were automatically rebooted, causing job failures.
- No specific action was required from the user as the issue resolved itself.

## Lessons Learned
- Node issues can cause job failures and aborts.
- Users should be aware that node reboots can affect job execution.
- If a job fails multiple times, it may be due to system issues rather than user error.

## Actions Taken
- HPC Admin confirmed the node issues and automatic reboots.
- No further action was required from the user as the problem resolved itself.
```
---

### 2019012542000301_Emmy%20cluster%3A%20not%20able%20to%20kill%20the%20jobs.md
# Ticket 2019012542000301

 # HPC Support Ticket Analysis: Emmy Cluster Job Termination Issue

## Keywords
- Emmy cluster
- Job termination
- Stuck jobs
- Network problems
- Node reset

## Summary
A user reported being unable to kill two simulations running on the Emmy cluster. The jobs were identified as potentially stuck due to recent network problems.

## Root Cause
- **Network Problems**: The jobs became stuck due to network issues that occurred previously.

## Solution
- **Node Reset**: The HPC Admin reset the stuck nodes, which successfully terminated the jobs.

## Lessons Learned
- **Monitoring Jobs**: Users should keep an eye on their jobs to identify issues promptly.
- **Network Impact**: Network problems can cause jobs to become unresponsive.
- **Admin Intervention**: In cases where jobs are stuck, a node reset by the HPC Admin can resolve the issue.

## Action Taken
- The HPC Admin identified the stuck jobs and reset the affected nodes, resolving the issue.

## Recommendations
- **Regular Checks**: Users should regularly check the status of their jobs.
- **Report Issues**: Promptly report any issues to HPC Support for timely resolution.

## Follow-up
- Ensure that network stability is maintained to prevent similar issues in the future.
- Provide users with guidelines on how to monitor and manage their jobs effectively.
---

### 2022020142002195_Early-Fritz%20%22Anselm%20Horn%22%20_%20mfbi05.md
# Ticket 2022020142002195

 # HPC Support Ticket Analysis

## Keywords
- HPC login
- Amber installation
- SLURM job script
- Amber executable recommendation
- System maintenance

## Summary
A user inquires about running small computations on the HPC system "Fritz" using Amber. The user also requests a SLURM job script header and recommendations for which Amber executable to use.

## Root Cause of the Problem
- User needs to run short computations on the HPC system.
- User requires a SLURM job script header.
- User seeks advice on which Amber executable to use.

## Solution
- **Login Issue**: The user was initially able to log in due to a configuration error, but this was corrected, and the user was officially granted access.
- **System Maintenance**: The user was informed about upcoming system maintenance due to electrical work, which would temporarily shut down the system.
- **SLURM Job Script Header**: The HPC Admin provided a minimal SLURM job script header, similar to the one used on another system (Meggie). The script includes options for both single-node and multi-node configurations.
- **Amber Executable Recommendation**: The HPC Admin mentioned that all four Amber modules are automatically built and untested, implying that the user can choose any of them.

## General Learnings
- **Access Management**: Ensure proper access control and notify users of any configuration errors.
- **System Maintenance Communication**: Inform users about upcoming maintenance and its impact on system availability.
- **Job Script Templates**: Provide users with job script templates and examples to help them get started quickly.
- **Software Recommendations**: Offer guidance on software versions and executables, especially if they are untested.

## Example SLURM Job Script Header
```bash
#!/bin/bash -l
#SBATCH -N 1
#SBATCH --tasks-per-node=72
#SBATCH --partition=singlenode
#SBATCH --export=NONE
unset SLURM_EXPORT_ENV
module add amber/....
srun pmemd.MPI -O -i ...
# alternativ:  mpirun pmemd.MPI -O -i ...
```

```bash
#!/bin/bash -l
#SBATCH -N 4
#SBATCH --tasks-per-node=72
#SBATCH --partition=multinode
#SBATCH --export=NONE
unset SLURM_EXPORT_ENV
module add amber/....
srun -n ... pmemd.MPI -O -i ...
# alternativ auch: mpirun -np
```

## Conclusion
This ticket highlights the importance of clear communication regarding system access, maintenance, and job script templates. It also underscores the need for providing guidance on software usage, even if the software is untested.
---

### 2024021442001891_Symptoms%20of%20outage%20still%20persists.md
# Ticket 2024021442001891

 ```markdown
# HPC Support Ticket: Symptoms of Outage Still Persist

## Keywords
- SLURM Batch Script
- Job Submission
- File Server Issues
- Job Cancellation
- Time Limit

## Problem Description
- User unable to run jobs despite nodes being allocated.
- Jobs appear to be running in `squeue` but output files are empty.
- Job numbers: 1204340 & 1204453.

## Root Cause
- Intermittent issues with the file server impacted job execution.
- Jobs were canceled due to the time limit specified in the job script.

## Solution
- File server issues were resolved by 12:30.
- User was advised to re-run the jobs and gather more information if the problem persisted.

## Lessons Learned
- Intermittent file server issues can cause job failures even if nodes are allocated.
- Always check for system-wide issues before troubleshooting individual job scripts.
- Ensure job scripts have appropriate time limits to avoid premature cancellation.

## Follow-Up
- User confirmed that the issue was resolved and jobs were running as expected.
- Ticket closed as the problem was intermittent and resolved by the HPC Admins.
```
---

### 2022051242001161_Fehler%20auf%20dem%20Emmy-Cluster.md
# Ticket 2022051242001161

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject: Fehler auf dem Emmy-Cluster

### Keywords:
- Simulation
- Emmy-Cluster
- Running Job
- Job Cancellation
- Walltime
- qdel
- Invalid Request
- Job Cancel in Progress

### Problem Description:
- User's simulation job on the Emmy-Cluster aborted but still displayed as "running."
- User unable to stop the job manually due to error message: "qdel: Invalid request MSG=job cancel in progress 1624167.eadm."
- Job exceeded the set walltime but was not automatically deleted.

### Root Cause:
- Job cancellation process was in progress, preventing manual cancellation.
- Job not automatically deleted despite exceeding walltime.

### Solution:
- HPC Admins need to manually intervene to cancel the job (1624167.eadm).

### General Learnings:
- Jobs may not always be cancellable by users if the cancellation process is already in progress.
- Jobs exceeding walltime may require manual intervention for deletion.
- Users should contact HPC Admins for assistance with such issues.
```
---

### 2025020842000179_Unable%20to%20Reach%20SLURM%20on%20Alex%20Cluster%20%28btr0104h%29.md
# Ticket 2025020842000179

 # HPC Support Ticket: Unable to Reach SLURM on Alex Cluster

## Keywords
- SLURM
- Alex Cluster
- squeue
- scontrol
- DNS SRV lookup
- slumd
- Login Node

## Issue Description
The user reported an issue with SLURM on the Alex cluster (btr0104h). When attempting to run `squeue` or `scontrol show config`, the following errors were encountered:
```
squeue: error: resolve_ctls_from_dns_srv: res_nsearch error: Unknown host
squeue: error: fetch_config: DNS SRV lookup failed
squeue: error: _establish_config_source: failed to fetch config
squeue: fatal: Could not establish a configuration source
```
This suggested a possible configuration or network issue preventing access to the SLURM controller.

## Root Cause
The root cause of the problem was identified as a failed restart of the `slumd` service around 3 AM, which did not come up cleanly.

## Solution
The HPC Admin team resolved the issue by ensuring that the `slumd` service was properly restarted and functioning. The SLURM commands should now work correctly on the login node "alex1".

## Lessons Learned
- Regular monitoring of SLURM services is crucial to detect and resolve issues promptly.
- Proper restart procedures for SLURM services should be followed to avoid configuration errors.
- DNS SRV lookup failures can indicate issues with the SLURM controller configuration or network connectivity.

## Actions Taken
- The HPC Admin team investigated the issue and identified the failed `slumd` restart.
- The `slumd` service was properly restarted to resolve the issue.
- The user was informed that the SLURM commands should now work correctly on the login node "alex1".

## Follow-Up
- Ensure that the SLURM services are regularly monitored to prevent similar issues in the future.
- Document proper restart procedures for SLURM services to avoid configuration errors.
---

### 2022121942002893_Fehlermeldung%20HPC-Cluster%20Meggie.md
# Ticket 2022121942002893

 ```markdown
# HPC-Support Ticket: Fehlermeldung HPC-Cluster Meggie

## Problem Description
- **User**: Experiencing frequent errors while running ANSYS CFX on the Meggie-Cluster.
- **Error**: Unspecified error message (image not included).
- **Behavior**: Jobs often succeed after a restart.

## Communication
- **User**: Requested information about the error and how to prevent it.
- **HPC Admin**: Requested job IDs, output files with error messages, and Slurm batch files for further investigation.

## Diagnosis
- **HPC Admin**: Identified a problem with node `m0140`.
- **HPC Admin**: Node `m0140` was in a strange state, set to "drain" and scheduled for reboot.
- **HPC Admin**: After reboot, the node and HBA were functioning correctly.

## Solution
- **HPC Admin**: Rebooted the problematic node `m0140`, which resolved the issue.
- **User**: Informed to report any future occurrences with the affected node name.

## Keywords
- ANSYS CFX
- Meggie-Cluster
- Node `m0140`
- Slurm batch file
- Output file
- Job ID
- Reboot
- Drain
- HBA

## Lessons Learned
- **Node Issues**: Problems with specific nodes can cause job failures.
- **Reboot Solution**: Rebooting the problematic node can resolve the issue.
- **User Reporting**: Users should report affected node names for future occurrences.
- **Output Files**: Users should save output files with error messages for better diagnosis.
```
---

### 2024051042003408_Advice%20on%20Chaining%20Jobs%20in%20SLURM.md
# Ticket 2024051042003408

 # HPC Support Ticket: Advice on Chaining Jobs in SLURM

## Keywords
- SLURM
- Job Chaining
- Job Dependency
- Time Limit
- Job Cancellation

## Problem Description
The user is attempting to chain jobs in SLURM using a code snippet from the SLURM documentation. The goal is for the next job to start automatically when the time limit of the current job is reached. However, the current job gets cancelled before it can trigger the next job, making it difficult to estimate the runtime needed to chain jobs effectively.

## Root Cause
The current approach relies on the job reaching a certain runtime to trigger the next job, but the job is cancelled before this condition is met due to the time limit.

## Solution
The HPC Admin recommended using the `sbatch --dependency` option to create a dependency between jobs. This allows the next job to be submitted early and remain in a PENDING state until the current job terminates. The job ID of the current job can be obtained using the `$SLURM_JOBID` variable.

## Example
```bash
sbatch --dependency=afterok:$SLURM_JOBID next_job_script.sh
```

## General Lessons
- Using job dependencies is a more reliable approach for chaining jobs in SLURM.
- The `--dependency` option allows for better control over job execution order.
- Submitting the next job early with a dependency status can prevent issues related to job cancellation and time limits.

## Roles Involved
- HPC Admins
- 2nd Level Support Team
- Software and Tools Developer

## References
- [SLURM Documentation on Advanced Topics](https://doc.nhr.fau.de/batch-processing/advanced-topics-slurm/#chain-jobs)

## Next Steps
- Implement the `--dependency` option in the job script.
- Monitor job execution to ensure proper chaining.
- Adjust job scripts as needed based on the results.
---

### 2024052942002553_numerous%20job%20failures.md
# Ticket 2024052942002553

 ```markdown
# HPC Support Ticket: Numerous Job Failures

## Keywords
- Job failures
- Stuck jobs
- Archiving failed
- srun step
- Timeout
- Random failures
- Directory issues
- Job script modifications

## Problem Description
- User reports numerous job failures occurring randomly.
- Jobs get stuck at the `srun` step and timeout without completing any calculations.
- Archiving fails for some jobs.
- Same input works intermittently, indicating no issue with the input data.

## Root Cause
- Possible issue with running jobs in the same directory.
- Lack of fixed filename format for stdout/stderr files.

## Solution
- **Directory Testing**: Run jobs in different directories to identify if the issue is directory-specific.
- **Job Script Modification**: Add the following lines to the job script to ensure fixed filename format for stdout/stderr files:
  ```bash
  #SBATCH -e slurm-%j.err
  #SBATCH -o slurm-%j.out
  ```

## General Learnings
- Running jobs in the same directory can sometimes cause issues.
- Using fixed filename formats for stdout/stderr files can help in debugging and tracking job outputs.
- Random job failures may be mitigated by changing the directory or ensuring proper job script configurations.
```
---

### 42360742_unerwartete%20Jobabr%C3%83%C2%BCche%20am%20HPC.md
# Ticket 42360742

 # HPC Support Ticket: Unexpected Job Abortions

## Keywords
- Job abortions
- PBS Server
- stdout/stderr files
- Disk quota exceeded
- Log files

## Problem Description
- User experienced job abortions on the HPC system.
- Only two jobs started simultaneously, while others aborted immediately after starting.
- Error messages indicated issues with stdout/stderr files and disk quota.

## Root Cause
- The user's jobs were generating excessive output, causing the disk quota to be exceeded.
- The PBS Server could not open/create stdout/stderr files due to insufficient disk space.
- Previous jobs with large output files were not properly cleaned up, leading to subsequent job failures.

## Solution
- HPC Admins cleaned up the remaining large output files from the user's previous jobs.
- The user was advised to limit the output size to avoid exceeding the disk quota in the future.

## Lessons Learned
- Ensure that job output is managed to avoid exceeding disk quotas.
- Regularly clean up large output files to prevent job failures.
- Monitor job output sizes and adjust as necessary to comply with system limits.
---

### 2022050942001087_delete%20infinite%20remaining%20time%20job.md
# Ticket 2022050942001087

 ```markdown
# HPC Support Ticket: Delete Infinite Remaining Time Job

## Keywords
- Job deletion
- Infinite remaining time
- qdel command
- Job submission errors

## Summary
A user submitted a job on the Woody cluster that is still running despite multiple attempts to delete it using the `qdel` command. The job status page shows the remaining time as `-infinity`.

## Root Cause
- The job is not being deleted properly due to an unknown issue.
- Possible errors in job submission causing the job to remain in an infinite state.

## Solution
- The HPC Admin identified the node (w1332) where the job is running.
- Further investigation is needed to determine the exact cause and delete the job.

## Lessons Learned
- Ensure proper job submission to avoid jobs running indefinitely.
- Use the `qdel` command correctly to delete jobs.
- If a job cannot be deleted, contact HPC support for assistance.

## Next Steps
- HPC Admins should investigate the node (w1332) to delete the job.
- Provide feedback to the user on any mistakes in the job submission to prevent future occurrences.
```
---

### 2017071142003925_Lammps%20on%20meggie.md
# Ticket 2017071142003925

 ```markdown
# HPC Support Ticket Conversation Summary

## Keywords
- LAMMPS installation
- SLURM job submission
- Account permissions
- Module loading
- Library dependencies

## General Learnings
- Ensure proper account permissions before submitting jobs.
- Use the correct SLURM options for job submission.
- Verify module availability and correct usage in job scripts.
- Check library dependencies for compiled software.

## Issues and Solutions

### Issue: Invalid Account or Account/Partition Combination
**Root Cause:** User did not have permission to access the Meggie cluster.
**Solution:** User submitted an application for access and was granted permission.

### Issue: Module Command Not Found
**Root Cause:** Incorrect shebang line in the job script.
**Solution:** Use `#!/bin/bash -l` as the first line of the job script to load the environment correctly.

### Issue: Missing Library Dependency
**Root Cause:** LAMMPS binary compiled with Intel compilers required a GNU library.
**Solution:** Ensure all dependencies are correctly linked during compilation. Recompile LAMMPS with the correct flags and libraries.

### Issue: SLURM Job Submission Error
**Root Cause:** Incorrect SLURM options used.
**Solution:** Remove the `-A` option from the SLURM command as it is not required.

## Additional Notes
- Always provide detailed information about the job requirements and technical specifications when requesting access to new clusters.
- Follow the documentation and examples provided by the HPC services for job script creation.
- Ensure that all software dependencies are correctly installed and configured on the cluster.
```
---

### 2024012342000886_Nodes%20starten%20im%20Testcluster%20nicht.md
# Ticket 2024012342000886

 # HPC Support Ticket: Nodes Not Starting in Test Cluster

## Keywords
- Slurm
- OS Updates
- Node Allocation
- Performance Counters
- LIKWID
- Node Failure
- Ansible

## Problem Description
- **Root Cause**: OS updates on test cluster nodes caused Slurm to become confused about the status of individual nodes.
- **Symptoms**:
  - Nodes appeared as `idle~` in `sinfo` output.
  - Interactive sessions resulted in node failure errors.
  - Access to performance monitoring registers was locked, preventing the use of LIKWID.

## Solution
- **Node Allocation**: HPC Admins resolved the node allocation issue, making the nodes allocable again.
- **Performance Counters**: The issue with performance counters was acknowledged as a known problem. The suggested fix involved running `/root/bin/run-ansible.sh knotenname` on `pollux`.

## Lessons Learned
- OS updates can disrupt the functioning of the Slurm workload manager.
- Node allocation issues can be resolved by HPC Admins.
- Performance counter access problems may require specific scripts or commands to fix.
- Communication with HPC Admins is key to resolving complex issues.

## Follow-up Actions
- Monitor nodes after OS updates for similar issues.
- Use the provided Ansible script to fix performance counter access problems.
- Document and share the solution with the 2nd Level Support team for future reference.
---

### 2024021342001302_Issues%20with%20tinyx%20-%20mptf007h.md
# Ticket 2024021342001302

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Keywords
- Compilation issues
- SLURM script
- `make clean`
- Internal compiler error
- Permission denied
- `srun` command not found
- Zoom meeting
- Submission script
- Module loading

## General Learnings
- **Compilation Issues**: The user encountered internal compiler errors while recompiling a program. The `make clean` command was not available, suggesting a missing rule in the Makefile.
- **SLURM Script**: The user had issues with the SLURM script, specifically with the number of threads and the `#SBATCH --ntasks-per-node=1` directive. Removing this directive resolved the issue.
- **Permission Denied**: The user encountered permission denied errors related to OpenMPI modules, indicating potential issues with the environment setup.
- **srun Command Not Found**: The user faced issues with the `srun` command not being found, which was resolved by ensuring the correct PATH environment variable was set.
- **Zoom Meeting**: The support team scheduled a Zoom meeting to discuss the issues in detail, highlighting the importance of direct communication for complex problems.
- **Submission Script**: The user provided a working submission script that included loading necessary modules and setting environment variables.

## Root Cause of Problems
- **Compilation Issues**: The internal compiler error was likely due to an outdated or incompatible compiler version.
- **SLURM Script**: The combination of `#SBATCH --ntasks-per-node=1` and `#SBATCH --cpus-per-task=128` was causing issues with thread allocation.
- **Permission Denied**: The permission denied error was likely due to changes in the cluster's file system or module setup.
- **srun Command Not Found**: The `srun` command was not found because the PATH environment variable was not set correctly.

## Solutions
- **Compilation Issues**: The user was advised to recompile the program with a compatible compiler version and ensure the Makefile includes a `clean` rule.
- **SLURM Script**: The user was advised to remove the `#SBATCH --ntasks-per-node=1` directive and ensure the SLURM script correctly allocates resources.
- **Permission Denied**: The user was advised to ensure the correct modules are loaded and the environment is set up correctly.
- **srun Command Not Found**: The user was advised to ensure the PATH environment variable includes the directories where `srun` is located.

## Conclusion
The support team provided detailed guidance on resolving compilation and SLURM script issues, highlighting the importance of correct environment setup and resource allocation. The user was able to successfully recompile and run the program after following the provided suggestions.
```
---

### 42253912_PBS%20auf%20emmy.md
# Ticket 42253912

 ```markdown
# HPC Support Ticket: PBS auf emmy

## Keywords
- PBS
- Job scheduling
- Infiniband problems
- MOTD
- Ticket

## Summary
A user reported a pending job request (RID=128408) that was not starting despite available nodes.

## Root Cause
- Infiniband problems on the HPC cluster "Emmy" were preventing new jobs from starting.

## Solution
- The HPC Admins informed the user that no new jobs were being allowed to run due to Infiniband issues.
- The user was advised to check the Message of the Day (MOTD) for updates.
- The user was also advised to consult colleagues who had already opened a ticket regarding the issue.

## Lessons Learned
- Users should check the MOTD for any system-wide issues that might affect job scheduling.
- Communication with colleagues can sometimes provide insights into ongoing issues.
- HPC Admins should ensure that system-wide issues are communicated effectively through channels like MOTD.

## Follow-up
- The user acknowledged the information and will check the MOTD in the future.
- The user also noted that their email addresses had been updated.
```
---

### 2023020842000762_mount%20on%20compute%20node%20failed%3F%3F%3F.md
# Ticket 2023020842000762

 # HPC Support Ticket: Mount on Compute Node Failed

## Keywords
- Mount failure
- SLURM job
- DNS resolution
- NetworkManager
- `resolv.conf`
- Healthchecker

## Problem Description
- User reported job failure due to missing mount on `/home/atuin` on compute nodes.
- SLURM job log indicated errors changing directory to the specified path.

## Root Cause
- DNS resolution failure caused by incorrect `resolv.conf` configuration on compute nodes.
- NetworkManager updated `resolv.conf` and removed DNS servers after a network glitch.

## Solution
- HPC Admins identified and corrected the `resolv.conf` configuration.
- Healthchecker was updated to automatically detect similar DNS resolution issues in the future.

## Lessons Learned
- Network glitches can lead to incorrect DNS configurations by NetworkManager.
- Proper configuration of `resolv.conf` is crucial for mounting filesystems.
- Healthchecker can be enhanced to detect and alert about DNS resolution issues.

## Follow-up Actions
- Monitor for similar issues using the updated Healthchecker.
- Ensure `resolv.conf` is correctly configured on all compute nodes.
---

### 2016080842003093_Emmy%20-%20tesla%20queueing%20system%20und%20xeon%20phi.md
# Ticket 2016080842003093

 ```markdown
# HPC Support Ticket: Emmy - Tesla Queueing System and Xeon Phi

## Keywords
- qstat
- Tesla nodes
- LAMMPS
- Xeon Phi
- MPSS
- Crosslinker
- Compilation
- Interactive job

## Problem Description
- **qstat Issue**: User unable to run `qstat <jobid>` or `qstat -f <jobid>` from running jobs on Tesla nodes. Error message: `qstat: Unknown Job Id Error <jobid>.eadm.rrze.uni-erlangen.de`.
- **LAMMPS Compilation**: User attempting to compile LAMMPS for Xeon Phi nodes encounters missing crosslinker for k1om architecture: `x86_64-k1om-linux-ld: No such file or directory`.

## Root Cause
- **qstat Issue**: Unknown, but likely related to PBS configuration or network issues.
- **LAMMPS Compilation**: Missing MPSS software stack on non-accel nodes.

## Solution
- **qstat Issue**: HPC Admins resolved the PBS problem, ensuring `qstat` commands work on all compute nodes.
- **LAMMPS Compilation**:
  - Use an interactive job on accel nodes where MPSS is installed.
  - Add link option `-L $INTEL_C_HOME/../tbb/lib/intel64_lin/gcc4.1` to find `-ltbbmalloc`.

## General Learnings
- Ensure PBS configuration is correct for `qstat` commands to function properly.
- MPSS software stack is required for compiling software targeting Xeon Phi nodes.
- Use interactive jobs on appropriate nodes for compilation tasks.
- Specific link options may be required for certain libraries during compilation.
```
---

### 2025021842001033_job-submission%20on%20alex.md
# Ticket 2025021842001033

 # HPC Support Ticket: Job Submission on Alex

## Keywords
- Slurm job submission
- Resource allocation
- Multithreading
- Node configuration
- Replica exchange jobs
- NAMD
- GPU allocation

## Problem Description
- User encountered issues with job submission after recent maintenance on Alex.
- Previous Slurm settings for replica exchange jobs with NAMD no longer worked.
- Error message: "Batch job submission failed: Requested node configuration is not available."
- User noticed that `--cpus-per-task>1` was not allowed anymore.

## Root Cause
- The new Slurm version is more restrictive when resources cannot be fully assigned.
- A full Alex node has 128 cores.
- The user's configuration (`--ntasks-per-node=24`, `--cpus-per-task=4`) did not fully utilize all cores, leading to job rejection.

## Solution
- HPC Admin suggested moving the `--cpus-per-task=4` option to the `srun` call instead of the `#SBATCH` directive.
- Example:
  ```bash
  srun --cpus-per-task=4 "my-program"
  ```
- This approach passed the job filter but may not guarantee the program starts as intended.

## Additional Notes
- User reported that the suggested solution worked without performance loss but received a warning: "srun: Job step's --cpus-per-task value exceeds that of job (4 > 1). Job step may never run."
- User suggested loosening the strict filters in future maintenance.
- HPC Admin acknowledged the suggestion and noted that changes in behavior come from the new Slurm version, not changes to the job filter itself.

## Conclusion
- The issue was resolved by adjusting the Slurm job submission script to move the `--cpus-per-task` option to the `srun` call.
- Further testing and monitoring are required to ensure the stability and performance of the jobs.
---

### 2022091942004076_Dringend%3A%20woody3%20ist%20nicht%20mehr%20erreichbar.md
# Ticket 2022091942004076

 # HPC-Support Ticket Conversation Analysis

## Subject: Dringend: woody3 ist nicht mehr erreichbar

### Keywords:
- DNS-Name
- SSH-Fehler
- TinyFAT
- Home-Verzeichnisse
- NFSv4
- Kerberos
- UID/GID-Mappings

### Root Cause of the Problem:
- The DNS-Name `woody3.rrze.fau.de` and `woody3.rrze.uni-erlangen.de` were not resolvable.
- The DNS-Name `woody.rrze.fau.de` was redirecting to `woody.nhr.fau.de`, which pointed to `woody4` and `woody5`.
- TinyFAT was not set up on `woody4/5`.
- Home directories `/home/hpc` and `/home/vault` were missing on `tinyx.nhr.fau.de`.
- Issues with NFSv4 mount and UID/GID mappings.

### Solution:
- The HPC Admin acknowledged the issue and explained that during extensive maintenance, some information might get lost or overlooked.
- The user was advised to attend the HPC-Cafe for updates and information exchange.
- The user noticed that the change from `woody` to `tinyx` was announced in `/etc/motd`, which they missed.
- The user reported issues with SSH public-key authentication due to NFSv4 mount requiring a Kerberos ticket.
- The user also reported UID/GID mapping issues causing files to belong to `nobody` and a group with GID `4294967294`.

### General Learnings:
- Regularly check `/etc/motd` for important announcements.
- Attend HPC-Cafe or similar events for updates and information exchange.
- Be aware of potential issues with NFSv4 mounts and Kerberos authentication.
- Ensure proper communication of maintenance and changes to avoid disruptions.

### Next Steps:
- The HPC Admin needs to address the `nobody` problem and ensure proper UID/GID mappings.
- Improve communication about maintenance and changes to avoid similar issues in the future.
---

### 2024080142002377_Request%20for%20Assistance%20-%20%20Issue%20with%20Slurm%20Command%20Not%20Found.md
# Ticket 2024080142002377

 # HPC Support Ticket: Issue with Slurm Command Not Found

## Keywords
- Slurm command not found
- SSH URL change
- Cluster frontend connection
- SSH config file

## Summary
A user encountered an issue where Slurm commands were not available after changing the SSH URL from `cshpc.rrze.fau.de` to `csnhr.nhr.fau.de`. The user was unable to run any Slurm commands, receiving a "command not found" error.

## Root Cause
- Slurm commands are not available on `csnhr`.
- The user needed to connect to the corresponding cluster frontend (e.g., `tinyx`) to use Slurm commands.

## Solution
1. **Connect to Cluster Frontend**: The user was advised to connect to the cluster frontend (`tinyx`) to submit jobs or check their status with `squeue`.
2. **Update SSH Config File**: The user had issues connecting to the cluster frontend due to an incorrect SSH config file. The "Host" entry in the config file needed to be updated.

## Additional Resources
- [SSH Command Line Template](https://doc.nhr.fau.de/access/ssh-command-line/)

## Conclusion
The user was able to resolve the issue by connecting to the appropriate cluster frontend and updating the SSH config file. This documentation can be used to assist other users experiencing similar issues with Slurm commands and SSH configuration.
---

### 2017081842001029_Grenze%20bei%20Job-Submissions%20auf%20Meggie%3F.md
# Ticket 2017081842001029

 # HPC Support Ticket: Job Submission Limits on Meggie

## Keywords
- Job submission
- Slurm
- MaxJobCount
- Job limit
- Queue limit

## Problem Description
- User encountered an error after submitting 9892 jobs.
- Error message: `sbatch: error: Slurm temporarily unable to accept job, sleeping and retrying.`
- User intended to submit a large number of jobs (around 13,000) for processing a significant amount of data.

## Root Cause
- Slurm has a default limit (MaxJobCount) of 10,000 jobs that can be in the system at any point in time (pending, running, suspended, or completed temporarily).

## Solution
- HPC Admins temporarily increased the MaxJobCount limit to 50,000 to accommodate the user's request.
- User was able to submit the remaining jobs without issues.
- Slurm handled over 13,000 jobs without any problems.

## Lessons Learned
- Slurm can handle a higher number of jobs than the default limit of 10,000.
- Increasing the MaxJobCount limit can be considered for similar cases, but it should be monitored to ensure system stability.
- Users should be aware of the job submission limits and consider submitting jobs in smaller batches to avoid hitting the limit.

## Follow-up
- HPC Admins will decide whether to keep the increased limit of 50,000 or revert to the default limit of 10,000.

## Relevant Configurations
- Slurm MaxJobCount: Controls the maximum number of jobs that can be in the slurmctld daemon records at any point in time. Default value is 10,000.
---

### 2023111742000657_SLURM%20auf%20tinyx.nhr.fau.de%20kaputt.md
# Ticket 2023111742000657

 # HPC Support Ticket: SLURM Issue on tinyx.nhr.fau.de

## Keywords
- SLURM
- tinyx.nhr.fau.de
- squeue
- DNS SRV lookup
- configuration source
- unplanned reboot

## Problem Description
After an unplanned reboot, SLURM on `tinyx.nhr.fau.de` became unusable. The user encountered the following errors when trying to run `squeue`:
- `resolve_ctls_from_dns_srv: res_nsearch error: Unknown host`
- `fetch_config: DNS SRV lookup failed`
- `_establish_config_source: failed to fetch config`
- `Could not establish a configuration source`

## Root Cause
The root cause of the problem is a failed DNS SRV lookup, which prevents SLURM from establishing a configuration source.

## Solution
The HPC Admins need to investigate and resolve the DNS SRV lookup issue to restore SLURM functionality on `tinyx.nhr.fau.de`.

## General Learnings
- Unplanned reboots can lead to unexpected issues with HPC services.
- DNS SRV lookup failures can disrupt SLURM's ability to function properly.
- It's crucial to monitor and maintain DNS configurations to ensure the stability of HPC services.
---

### 2018121742000601_Falsche%20Joballokation%20auf%20Emmy%20_%20iww2005h.md
# Ticket 2018121742000601

 ```markdown
# HPC Support Ticket Analysis

## Subject: Falsche Joballokation auf Emmy / iww2005h

### Keywords:
- Job allocation
- Multi-node jobs
- Single-node jobs
- Job queue
- Emmy cluster
- HPC status

### Problem:
- User's 20-node jobs on Emmy cluster were only starting processes on the first node, with the remaining 19 nodes idle.

### Root Cause:
- The exact root cause is not explicitly stated, but it is implied that there might have been an issue with the job submission script or configuration.

### Solution:
- The HPC Admin deleted the problematic jobs from the queue.
- The user's newer jobs were correctly submitted as single-node jobs.

### Actions Taken:
- HPC Admin identified the issue and deleted the problematic jobs (1028243.eadm and 1028244.eadm) from the queue.
- The ticket was closed due to no further feedback from the user, and newer jobs were correctly submitted as single-node jobs.

### General Learning:
- Ensure that multi-node job submissions are correctly configured to utilize all allocated nodes.
- Monitor job status and allocation to identify and rectify issues promptly.
- Communicate with users to understand and resolve job submission problems effectively.
```
---

### 2025022242000115_Unable%20to%20terminate%20job%201811859.md
# Ticket 2025022242000115

 ```markdown
# Unable to Terminate Job

## Keywords
- Job termination
- Job status CG
- scancel
- Filesystem slow response
- Slurm stuck
- Node reboot

## Problem Description
- User unable to terminate job with ID 1811859.
- Job status remains at CG (completing) after using `scancel`.
- Job continues to produce output.

## Root Cause
- One filesystem was slow in responding, causing Slurm to get stuck.

## Solution
- Several nodes, including the one running the user's job, were rebooted to resolve the issue.

## Lessons Learned
- Slow filesystem response can cause Slurm to get stuck.
- Rebooting affected nodes can resolve stuck jobs in the "completing" state.
```
---

### 2024071742003151_logs%20in%20slurm%20mail.md
# Ticket 2024071742003151

 # HPC Support Ticket: Logs in SLURM Mail

## Keywords
- SLURM
- Notification Emails
- stdout
- stderr
- Job Logs

## Summary
- **User Request**: Include stdout and stderr logs in SLURM notification emails.
- **HPC Admin Response**: SLURM does not support sending stdout/stderr logs via email. The SLURM server does not have access to user directories.
- **Additional Information**: Manual email sending from compute nodes is not configured.

## Root Cause
- SLURM's email notification system does not support including stdout and stderr logs.
- SLURM server lacks access to user directories where logs are stored.

## Solution
- No direct solution provided. Feature request not feasible with current SLURM configuration.

## What Can Be Learned
- SLURM's email notifications are limited in functionality.
- SLURM server has restricted access to user directories.
- Manual email sending from compute nodes is not configured on the HPC system.

## Next Steps
- Users should manually check job logs for detailed information.
- Consider alternative methods for log monitoring and archiving.
---

### 2023031742002376_squeue.md
# Ticket 2023031742002376

 # HPC Support Ticket: squeue Issues and Slow Copy Speeds

## Keywords
- `squeue`
- `Slurm`
- `Cluster Specification`
- `Copy Speed`
- `File System Issues`
- `Zipping Files`

## Problem Description
- User unable to see queue jobs using `squeue`.
- Jobs successfully finish despite not being visible in the queue.
- Slow copy speeds (~5MB/s) from the HPC machine to the local machine.

## Root Cause
- **squeue Issue**: User did not specify the cluster when using Slurm commands.
- **Slow Copy Speeds**: Potential issues with the `$WORK` file system due to misuse by other users.

## Solution
- **squeue Issue**: Use wrapper scripts to specify the cluster, e.g., `squeue.tinygpu`, `sbatch.tinygpu`.
- **Slow Copy Speeds**:
  - Check the file system being used.
  - Zip files if copying many small files to improve speed.
  - Consider potential issues with the `$WORK` file system.

## Additional Information
- `tynix` serves as a frontend to two different clusters: TinyFat and TinyGPU.
- Specifying the cluster is necessary for Slurm commands to function correctly.
- File system issues can impact copy speeds, and zipping files can help mitigate this.

## Next Steps
- If the issue persists, provide more information such as the batch script, output files, and exact commands used.
- Monitor the file system for any ongoing issues that could affect copy speeds.

## Contact Information
- For further assistance, contact the HPC support team at `support-hpc@fau.de`.

---

This documentation aims to help HPC support employees quickly identify and resolve similar issues related to `squeue` visibility and slow copy speeds.
---

### 2024051242000505_Job%20Directory%20and%20Quota%20Limit%20Issue.md
# Ticket 2024051242000505

 ```markdown
# Job Directory and Quota Limit Issue

## Keywords
- Job directory
- Quota limit
- Bash script
- $WORK
- `rm -r`
- `srun`
- Python
- Job output

## Problem Description
The user is experiencing issues with the job directory. Despite specifying that jobs should run in `$WORK`, they are not appearing there. The user suspects they might have exceeded quota limits, even though they regularly delete finished jobs using `rm -r`.

## Root Cause
- The user's jobs are failing, possibly due to the use of `srun` with Python.
- The cleanup script at the end of the job might be deleting any output generated.

## Solution
- Remove the `srun` command from the Python call.
- Comment out the lines in the script that clean up the temporary job directory to preserve any output that might be generated.

## Steps Taken
1. **HPC Admin** checked the user's quota and found no indication of exceeding limits.
2. **HPC Admin** noticed that recent jobs had failed and suggested removing `srun` from the Python call.
3. **HPC Admin** advised the user to comment out the cleanup lines in the script to keep any output for troubleshooting.

## General Learning
- Ensure that job scripts do not prematurely delete output files, as this can hinder troubleshooting.
- Be cautious with the use of `srun` in job scripts, as it can sometimes cause issues.
- Regularly check job outputs and error logs to identify and resolve issues.
```
---

### 2021062942000531_Job%20auf%20Emmy%201508028%20phyv018h.md
# Ticket 2021062942000531

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject: Job auf Emmy 1508028 phyv018h

### Keywords:
- Job ID: 1508028
- Cluster: Emmy
- Issue: Hardware failure
- Affected Node: phyv018h
- Type of Job: Phononen Rechnung
- Action Required: Check results, possibly rerun or continue job

### Summary:
During the runtime of job 1508028 on the Emmy cluster, a hardware failure occurred on one of the nodes (phyv018h). The user is advised to check the results of their computation, as it is likely that the job needs to be rerun. If it was a standard Phononen Rechnung, the job can simply be continued.

### Root Cause:
- Hardware failure on node phyv018h.

### Solution:
- Check the results of the job.
- If necessary, rerun or continue the job.

### General Learnings:
- Hardware failures can disrupt jobs and may require rerunning or continuing the computation.
- Users should be informed to check their job results in case of such failures.
- Specific types of jobs (e.g., Phononen Rechnung) may have the option to continue rather than rerun.
```
---

### 2023103142001318_Jobs%20on%20%22Reservation%22.md
# Ticket 2023103142001318

 ```markdown
# HPC Support Ticket: Jobs on "Reservation"

## Keywords
- Job on hold
- Reservation
- Scheduler issue
- Manual release
- Job resubmission
- Slurmctld restart

## Problem Description
- User noticed three jobs on hold with the reason "(Reservation)".
- Job IDs: 933454, 932857, 932830.

## Root Cause
- Scheduler incorrectly marked nodes as reserved.
- Potential issue with the scheduler displaying wrong reasons.

## Troubleshooting Steps
1. HPC Admin checked the jobs and found no issues.
2. Attempted manual release of the jobs, which did not resolve the issue.
3. Identified recent issues with wrong reasons being displayed by the scheduler.

## Solution
- Restarting the `slurmctld` service resolved the issue.
- If jobs do not start in the next few days, the user should cancel and resubmit them.

## Conclusion
- The scheduler may occasionally display incorrect reasons for job holds.
- Restarting the `slurmctld` service can resolve scheduler-related issues.
- Users should resubmit jobs if they remain on hold for an extended period.
```
---

### 2023072642002888_HPC%20Job%20Submission%20Issue.md
# Ticket 2023072642002888

 # HPC Job Submission Issue

## Keywords
- Job submission
- Slurm
- squeue
- Pending jobs
- GPU memory
- Job runtime
- Job cancellation

## Problem Description
- User submitted jobs but they were not visible as running using `squeue -t running`.
- Jobs were listed as pending (`PD`) with `squeue`.
- Jobs failed due to insufficient GPU memory.
- Jobs were cancelled due to exceeding the default runtime.

## Root Cause
- The cluster was busy, causing jobs to remain in the pending state.
- The user did not specify the GPU type, leading to insufficient memory allocation.
- The user did not specify the job runtime, resulting in jobs being cancelled after the default runtime of 10 minutes.

## Solution
- Use `squeue` to view pending jobs.
- Specify the GPU type in the job script to allocate a GPU with sufficient memory.
- Add the `#SBATCH --time` directive to the job script to specify the required runtime.

## Resources
- [Slurm Documentation](https://hpc.fau.de/systems-services/documentation-instructions/batch-processing)
- [HPC Introduction Slides](https://hpc.fau.de/files/2023/07/2023-07-12_HPC_in_a_Nutshell.pdf)
- [TinyGPU Cluster Documentation](https://hpc.fau.de/systems-services/documentation-instructions/clusters/tinygpu-cluster/)
---

### 2024061742002707_Fritz%3A%20Slurm%20Fehler%20bei%20AMBER%20%28%22srun%3A%20error%3A%20task%200%20launch%20failed%3A%2.md
# Ticket 2024061742002707

 ```markdown
# HPC Support Ticket: Slurm Error with AMBER Job

## Keywords
- Slurm
- AMBER
- srun error
- task launch failed
- NFS issue
- job hang

## Problem Description
A multi-step AMBER job on Fritz HPC system failed to start the fourth step, resulting in an `srun: error: task 0 launch failed: Slurmd could not execve job` error. The job was successfully running the third step but did not proceed to the fourth step.

## Root Cause
The root cause of the problem was suspected to be a temporary NFS (Network File System) issue, which prevented the binary from being found and executed.

## Solution
The job was canceled using `scancel` and restarted from the fourth step. The job then ran successfully without further issues.

## Lessons Learned
- Temporary NFS issues can cause job execution failures.
- The error message `srun: error: task 0 launch failed: Slurmd could not execve job` can indicate a problem with accessing the binary.
- Restarting the job after a failure can resolve transient issues.

## Recommendations
- Monitor NFS performance and stability.
- Consider implementing retry mechanisms for jobs to handle transient errors.
- Educate users on how to handle and report such errors for quicker resolution.
```
---

### 2021080342003609_ineffiziente%20Jobs%20auf%20Emmy%20-%20mpp3000h.md
# Ticket 2021080342003609

 # HPC Support Ticket Analysis: Inefficient Jobs on Emmy

## Keywords
- Inefficient jobs
- System monitoring
- Job performance
- Node utilization
- ELXFS issue
- Reboot

## Summary
- **Problem**: User's jobs on Emmy are repeatedly identified as inefficient. Half of the jobs are not performing any recognizable work, while the other half request two nodes but only start processes on one.
- **Root Cause**: Possible ELXFS issue causing single-node jobs to hang.
- **Solution**: Reboot of all Emmy nodes triggered via `/apps/rrze/sbin/trigger-reboot.sh`.

## Details
- **HPC Admin**: Notified the user about inefficient jobs and provided links to job details.
- **HPC Admin**: Identified potential ELXFS issue affecting single-node jobs and initiated a reboot of all Emmy nodes.
- **HPC Admin**: Observed improvement in the performance of current 2-node jobs.

## Lessons Learned
- Regularly monitor job performance to identify inefficiencies.
- ELXFS issues can cause jobs to hang, and a reboot may resolve the problem.
- Ensure that jobs requesting multiple nodes are utilizing all allocated resources.

## Follow-up Actions
- Continue monitoring job performance.
- Consider additional troubleshooting if inefficiencies persist.
- Document and share best practices for job submission and resource utilization.
---

