# Topic 8: walltime_job_runtime_restarted_fails

Number of tickets: 154

## Tickets in this topic:

### 2018102542000975_Walltime.md
# Ticket 2018102542000975

 # HPC Support Ticket: Walltime Extension

## Keywords
- Walltime
- Job Submission
- ORCA 4.01
- TINYFAT
- JobID
- HPC Admin
- RRZE
- FAU

## Problem
- User has memory-intensive ORCA 4.01 jobs that exceed the default walltime on TINYFAT.
- Jobs are expected to run for 1-2 days.

## Solution
- User submits jobs normally and provides JobIDs to HPC Admin.
- HPC Admin extends the walltime to 60 hours for the specified jobs.

## Notes
- Some nodes are owned by a specific group and may be preempted if needed by the owners.
- Extended walltime is granted with the understanding that jobs may be terminated if the node owners require the resources.

## General Learnings
- Users can request extended walltime for jobs by submitting them normally and providing JobIDs to HPC Admin.
- HPC Admin can adjust walltime for jobs as needed.
- Some resources may have specific ownership and usage policies that users should be aware of.
---

### 2019061742002048_48h%20session.md
# Ticket 2019061742002048

 # HPC Support Ticket: 48h Session Request

## Keywords
- Session duration
- Job walltime
- Checkpoint-restart
- TensorFlow
- TinyGPU

## Problem
- **Root Cause**: User's complex program structure prevents full reloading after training stops, requiring longer than 24h sessions.
- **User Request**: Extend session duration to 48h.

## Solution
- **HPC Admin Response**:
  - General job limit is 24h.
  - Recommended solution: Implement checkpoint-restart features (e.g., [TensorFlow checkpoints](https://www.tensorflow.org/guide/checkpoints)).
  - Exception: Manual walltime extension on a per-job basis for a limited number of jobs. User must provide job IDs.

## General Learnings
- Understanding job walltime limits.
- Importance of checkpoint-restart for long-running jobs.
- Procedure for requesting extended walltime.

## Related Resources
- [TensorFlow Guide: Checkpoints](https://www.tensorflow.org/guide/checkpoints)
- HPC Services Contact: [support-hpc@fau.de](mailto:support-hpc@fau.de)
- HPC Website: [RRZE HPC](http://www.hpc.rrze.fau.de/)
---

### 2022072742001683_Re%3A%20Long%20running%20process%20on%20host%20woody3.md
# Ticket 2022072742001683

 # HPC Support Ticket: Long Running Process on Host

## Keywords
- Long running process
- Frontend usage
- Batch jobs
- Automatic process termination
- Interactive batch jobs

## Summary
A user was notified that a process they owned on a frontend node (`woody3`) had been running for too long and was automatically killed. The user had not been actively using the system for a week and was surprised by the notification.

## Root Cause
- The user had a long-running process on a frontend node, which is not intended for running jobs but for compiling and submitting jobs.

## Solution
- The user was advised to submit batch jobs for processes requiring more than 30 minutes of CPU time.
- For interactive work, the user was informed about interactive batch jobs using the `-I` and `-X` parameters with `qsub`.

## General Learnings
- Frontend nodes are not meant for running long processes; they are for compiling and submitting jobs.
- Processes running for more than 30 minutes on frontends will be reniced and automatically killed after one hour.
- Users should submit batch jobs for long-running processes to avoid disturbing others.
- Interactive batch jobs are available for interactive work using specific parameters.

## Actions Taken
- The user was notified about the long-running process and its automatic termination.
- The user was advised on the proper usage of frontend nodes and the submission of batch jobs.

## Next Steps
- Ensure users are aware of the proper usage of frontend nodes.
- Provide guidance on submitting batch jobs and using interactive batch jobs for long-running processes.
---

### 2023030742001627_Re%3A%20%5BNHR%40FAU%5D%20Downtime%20of%20Alex%20and%20Testcluster%20on%20March%209.md
# Ticket 2023030742001627

 # HPC Support Ticket Conversation Analysis

## Subject
Re: [NHR@FAU] Downtime of Alex and Testcluster on March 9

## Keywords
- Downtime
- Maintenance
- Power Grid
- Job Postponement
- Frontends
- Fileservers

## Summary
- **User Inquiry:** Clarification on the start date of the scheduled downtime.
- **HPC Admin Response:** Confirmation that the downtime starts on Thursday, March 9.

## What Can Be Learned
- **Communication:** Clear communication about the exact start date of scheduled downtimes is crucial to avoid confusion.
- **Downtime Reason:** Maintenance of the power grid at the RRZE building.
- **Job Management:** Jobs that would collide with the downtime will be postponed until the downtime is over.
- **Service Availability:** Frontends and fileservers will remain available during the downtime.

## Root Cause of the Problem
- **User Confusion:** Unclear start date of the scheduled downtime.

## Solution
- **Clarification:** HPC Admin provided clear confirmation that the downtime starts on Thursday, March 9.

## Documentation for Support Employees
- **Downtime Communication:** Ensure that all communication regarding scheduled downtimes includes clear and unambiguous dates and times.
- **Job Management:** Implement automated systems to postpone jobs that would collide with scheduled downtimes.
- **Service Availability:** Maintain availability of frontends and fileservers during power grid maintenance to minimize disruption to users.

This documentation can be used to address similar issues in the future, ensuring clear communication and minimal disruption during scheduled maintenance.
---

### 2023020342003223_Verl%C3%83%C2%A4ngerung%20Jobs%20Alex.md
# Ticket 2023020342003223

 # HPC Support Ticket Analysis: Job TimeLimit Extension

## Keywords
- TimeLimit
- Job Extension
- Alex Cluster
- Downtime
- Checkpoint-Restart

## Summary
A user requested an extension of the TimeLimit for their jobs on the Alex Cluster to 5 days. The HPC Admin initially extended the TimeLimit but later requested information on why the user could not perform a Checkpoint-Restart. The user made a follow-up request for additional jobs to be extended.

## Root Cause
- User needed extended runtime for their jobs.
- Potential upcoming downtime due to power outages.

## Actions Taken
- HPC Admin extended the TimeLimit for the user's jobs.
- HPC Admin inquired about the user's inability to perform a Checkpoint-Restart.

## Solution
- The TimeLimit for the user's jobs was extended to 5 days.
- User was informed about upcoming downtimes and asked about technical reasons for not using Checkpoint-Restart.

## General Learnings
- Users may require extended runtime for their jobs.
- HPC Admins should consider upcoming downtimes and suggest Checkpoint-Restart as a mitigation strategy.
- Clear communication about job extensions and system downtimes is essential.

## Follow-Up
- Ensure users are aware of Checkpoint-Restart procedures.
- Monitor job extensions and their impact on system resources.
- Communicate system downtimes effectively to all users.
---

### 2024081442000354_Error%20while%20running%20jobs.md
# Ticket 2024081442000354

 # HPC Support Ticket: Error while running jobs

## Keywords
- Job execution error
- Maintenance
- Scheduled downtime

## Problem Description
- User unable to run jobs since Monday.
- Error message indicates the system is in maintenance.

## Root Cause
- Scheduled maintenance of HPC systems.

## Solution
- Wait for maintenance to be completed.
- Check the status of ongoing maintenance via the provided link.

## What to Learn
- Regularly check for scheduled maintenance notifications.
- Use provided links to stay updated on system status.
- Inform users about maintenance schedules in advance if possible.

## Additional Information
- Maintenance status link: [Scheduled Downtime of NHR@FAU HPC Systems August 13-15](https://hpc.fau.de/2024/08/06/scheduled-downtime-of-nhrfau-hpc-systems-august-13-15/)
- Contact: [support-hpc@fau.de](mailto:support-hpc@fau.de)

## Roles Involved
- HPC Admins
- 2nd Level Support Team
---

### 42069796_Extension%20of%20Jobs%20ID%20378937%20and%20378938.md
# Ticket 42069796

 ```markdown
# HPC Support Ticket Conversation Analysis

## Subject: Extension of Jobs ID 378937 and 378938

### Keywords:
- Job Extension
- VASP Calculation
- HSE06 Functional
- Priority Job
- Conference Deadline

### General Learnings:
- Users may request extensions for jobs that are computationally intensive and require more time to converge.
- HPC Admins can manually extend job runtimes and adjust priorities based on user requests and project needs.
- Communication between users and HPC Admins is crucial for managing job priorities and deadlines.

### Root Cause of Problems:
- Job 378938 required more time due to the complexity of the VASP calculation with the HSE06 functional.
- Job 378942 needed higher priority and extended runtime to meet a conference deadline.

### Solutions:
- HPC Admins extended the runtime for jobs 378937 and 378938 to 48 hours.
- Job 378938 was further extended to 96 hours due to its complexity.
- Job 378942 was given higher priority and its runtime was set to 72 hours to ensure completion before the conference.
- The runtime for job 378942 was extended again to run over the weekend and until Wednesday morning to ensure convergence.

### Documentation for Support Employees:
- **Job Extension Requests:** Users may request extensions for jobs that are computationally intensive. HPC Admins can manually extend job runtimes based on user requests.
- **Priority Adjustments:** HPC Admins can adjust job priorities to ensure critical jobs are completed on time, especially for conference deadlines.
- **Communication:** Effective communication between users and HPC Admins is essential for managing job priorities and deadlines.
```
---

### 2022102442003377_Re%3A%20%5BNHR%40FAU%5D%20Downtime%20of%20all%20RRZE%20HPC%20systems%20on%20October%2019%20and%20Fri.md
# Ticket 2022102442003377

 ```markdown
# HPC Support Ticket Conversation Analysis

## Keywords
- Scheduled Downtime
- HPC Systems
- Maintenance
- Power Grid
- Top500 List
- Job Queue
- Login Nodes
- File Systems

## Summary
- **Scheduled Downtime**: All HPC systems at RRZE will be down on October 19 for maintenance on the power grid.
- **Additional Downtime**: Fritz will be unavailable from October 31 to November 2 for HPL measurements for the Top500 list.
- **Job Handling**: Jobs will be postponed if they collide with the downtime.
- **Login Nodes and File Systems**: Expected to be available during the downtime.

## Root Cause of User Concern
- **Date Confusion**: User noticed a discrepancy in the downtime date mentioned in the email (October 19) versus a previously announced date (October 26).

## Solution
- **Clarification**: HPC Admin acknowledged the error due to using an old email template and confirmed the correct downtime date.

## General Learnings
- **Communication**: Ensure accurate and timely communication of scheduled downtimes to avoid user confusion.
- **Template Management**: Be cautious when using old email templates to avoid outdated information.
- **User Support**: Promptly address user queries to maintain trust and clarity.
```
---

### 42190481_Runtimes%20of%20jobs%20at%20HPC.md
# Ticket 42190481

 # HPC Support Ticket: Runtimes of Jobs at HPC

## Keywords
- Job runtime
- HPC cluster
- Walltime
- Job submission
- Runtime extension

## Problem
- User inquires about submitting jobs with runtimes above 48 hours.

## Root Cause
- User needs to run jobs that exceed the standard 48-hour runtime limit.

## Solution
- **Runtime Limit**: It is not permitted to submit jobs with a runtime of more than 48 hours to the HPC clusters.
- **Exceptional Cases**: For rare, one-off tasks that require more than 48 hours and cannot be split, the runtime can be extended if the cluster load permits.
- **Submission Process**: Submit the job normally, requesting a walltime of ≤48 hours. HPC Admins can then modify the job to extend the runtime.

## General Learning
- Understand the runtime limits for job submissions.
- Recognize that exceptions can be made for special cases, but these are limited.
- Follow the standard job submission process and request runtime extensions through HPC Admins if necessary.

## References
- [HPC Services](http://www.hpc.rrze.fau.de/)

## Roles Involved
- **HPC Admins**: Handle job runtime extensions and provide guidance on job submission.
- **2nd Level Support Team**: Assist with technical issues and support.
- **Head of the Datacenter**: Oversee datacenter operations.
- **Training and Support Group Leader**: Manage training and support activities.
- **NHR Rechenzeit Support**: Handle applications for grants and support.
- **Software and Tools Developer**: Develop and maintain software tools for the HPC environment.
---

### 2020110642001968_AW%3ALong%20running%20process%20on%20host%20emmy1.md
# Ticket 2020110642001968

 ```markdown
# HPC Support Ticket: Long Running Process on Host emmy1

## Keywords
- Long running process
- Frontend usage
- Batch job submission
- qsub
- Interactive batch jobs
- Documentation
- Email communication

## Problem Description
- User attempted to reserve time on the cluster but encountered issues with the `#` commands and `qsub`.
- User's process on the frontend was killed for running too long.

## Root Cause
- User was running a long process on the frontend instead of submitting a batch job.
- User had difficulty understanding how to reserve time on the cluster using batch scripts.

## Solution
- **Documentation**: Provided links to detailed documentation on batch processing and batch scripts.
- **Email Communication**: Advised the user to use their `@fau.de` email address for better support tracking.
- **Training**: Invited the user to an upcoming HPC introduction session for further guidance.

## General Learnings
- Frontends are for compiling and submitting jobs, not for running long processes.
- Long processes should be submitted as batch jobs to avoid being killed on the frontend.
- Interactive batch jobs can be used for interactive work (parameters `-I` and `-X` to `qsub`).
- Regular training sessions are available for HPC beginners.
- Proper email communication helps in better support tracking.
```
---

### 2024121042003047_batch-job%20Verl%C3%A4ngerung%20alex%20cluster.md
# Ticket 2024121042003047

 ```markdown
# HPC Support Ticket: Batch Job Duration Extension

## Keywords
- Batch job
- Duration extension
- Job ID
- User ID
- HPC Admin

## Summary
A user requested an extension of the runtime for a batch job. The HPC Admin responded by extending the job's runtime.

## Problem
- **User Request**: The user requested an extension of the runtime for their batch job by an additional 24 hours.
  - User ID: `iwb3004h`
  - Job ID: `2232604`

## Solution
- **HPC Admin Response**: The HPC Admin extended the job's runtime to 2 days.

## What Can Be Learned
- Users can request extensions for their batch jobs.
- HPC Admins can extend the runtime of batch jobs upon user request.
- The request should include the user ID and job ID for identification.

## Notes
- Ensure that the user provides the necessary details (user ID and job ID) for the HPC Admin to process the request efficiently.
- HPC Admins should confirm the extension with the user once the action is taken.
```
---

### 2022040442002471_Fwd%3A%20Tech-Halbe%20-%20Protokoll%20vom%2004.04.2022%20-%20Stromausfall_%20HPC-Caf%C3%83%C2%A9.md
# Ticket 2022040442002471

 ```markdown
# HPC Support Ticket Conversation Analysis

## Subject
Fwd: Tech-Halbe - Protokoll vom 04.04.2022 - Stromausfall/ HPC-Café

## Keywords
- Stromunterbrechung (Power Outage)
- HPC-Café
- Zoom
- Schiffsdiesel (Ship Diesel)
- RRZE-Gebäude (RRZE Building)
- Blauem Hochhaus (Blue High-Rise)

## Root Cause of the Problem
- Notification of a power outage scheduled for 12.04.2022 from 6-22 Uhr in the "blauem Hochhaus" and RRZE-Gebäude.

## Conversation Summary
- **User**: Informs about an upcoming power outage and inquires if the ship diesel will be used.
- **HPC Admin**: Responds that the HPC-Café will not be affected as it is held virtually on Zoom.

## Solution
- The HPC-Café will continue as scheduled on Zoom, unaffected by the power outage.

## General Learnings
- Virtual events like the HPC-Café are not impacted by physical infrastructure issues such as power outages.
- Communication about scheduled outages is important to ensure all stakeholders are informed and can plan accordingly.
```
---

### 2024110542003219_Fwd%3A%20Fritz-question.md
# Ticket 2024110542003219

 ```markdown
# HPC Support Ticket Conversation Analysis

## Subject: Fwd: Fritz-question

### Keywords:
- OTRS ticket
- Job time limit extension
- Timeout
- Job ID: 1645508
- User ID: k109be10

### Summary:
- **User Request:** A user requested an extension of the time limit for a running job from 20 hours to 24 hours.
- **HPC Admin Response:** The job had already run into a timeout by the time the request was reviewed.

### Root Cause:
- The user's job reached its time limit before the request for extension could be processed.

### Solution:
- No solution was provided as the job had already timed out.

### Lessons Learned:
- Users should request time limit extensions well in advance to avoid job timeouts.
- HPC support staff should promptly address requests for job modifications to prevent such issues.

### Additional Notes:
- The user inquired about the proper way to open an OTRS ticket, indicating a need for clearer instructions on ticket submission.
```
---

### 2018040442000543_RE%3A%20Long%20running%20process%20on%20host%20meggie2.md
# Ticket 2018040442000543

 ```markdown
# HPC Support Ticket: Long Running Process on Host

## Keywords
- Long running process
- Frontend usage
- Process management
- Batch jobs
- Interactive batch jobs
- `watch` command

## Summary
A user received a notification that a long-running process was automatically killed on the host `meggie2`. The user was surprised as they did not start any process this time.

## Root Cause
- The user had a `watch` command running, which accumulated CPU usage over time.
- The process was killed automatically after exceeding the allowed CPU time limit.

## Details
- The frontends are intended for compiling and submitting jobs, not for running long processes.
- Processes running for more than 30 minutes are reniced to lower priority.
- Processes still running after one hour are automatically killed.
- The user had an idle login session with a `watch` command running, which was eventually killed.

## Solution
- Use batch jobs for processes requiring more than 30 minutes of CPU time.
- For interactive work, use interactive batch jobs with parameters `-I` and `-X` to `qsub`.
- Avoid leaving long-running commands like `watch` in idle sessions.

## Additional Information
- The HPC system does not maintain detailed logs of all processes, making it difficult to provide specific information about past processes.
- Users should be mindful of their running processes and ensure they comply with the system's usage policies.
```
---

### 2025012242000466_Quota%20extension%20Student%20Abhnav%20Choudhray%20-%20iwso152h%20-%20l%C3%83%C2%A4ngere%20Joblaufze.md
# Ticket 2025012242000466

 # HPC Support Ticket: Quota Extension for Long Job Runtime

## Keywords
- Quota extension
- Job runtime
- Checkpointing
- Job script directive
- Dataset size
- Deep learning models
- Benchmark study

## Problem
- User requires extended job runtime for deep learning model training due to large dataset size (3.6 million images).
- Training runs take multiple days, exceeding the standard job time limit.

## Root Cause
- Large dataset size and complex deep learning models result in extended training times.

## Solution
- **Checkpointing and Restarting**: Users are advised to implement checkpointing to save job progress and restart jobs.
- **Job Script Directive**: Add `#SBATCH --hold` directive to the job script.
- **Job Submission and Extension Request**:
  1. Submit jobs with a time request of less than 24 hours.
  2. Note the job IDs.
  3. Send an email to `hpc-support@fau.de` mentioning the desired time limit, job IDs, and justification for the extension.

## Additional Notes
- **Data Staging**: Implementing data staging is recommended for efficient data handling.
- **Monitoring**: Job monitoring can be accessed via [monitoring link](https://monitoring.nhr.fau.de/monitoring/job/12423550).

## General Learning
- Users should consider checkpointing for long-running jobs.
- Job script modifications and proper communication with HPC support are crucial for handling extended runtime requests.
- Efficient data handling methods like data staging can improve job performance.

## Roles Involved
- **HPC Admins**: Provide guidance on job script modifications and extension requests.
- **2nd Level Support Team**: Assist with technical support and job monitoring.
- **Head of Datacenter**: Oversee datacenter operations.
- **Training and Support Group Leader**: Manage training and support activities.
- **NHR Rechenzeit Support**: Handle compute time support and grant applications.
- **Software and Tools Developer**: Develop and maintain software tools for HPC.
---

### 2018051542000182_COMSOL-Jobs%20auf%20Woody3%20%7C%20Long%20running%20process.md
# Ticket 2018051542000182

 ```markdown
# HPC Support Ticket: COMSOL-Jobs auf Woody3 | Long running process

## Keywords
- COMSOL
- Long running process
- Frontend usage
- Batch jobs
- Walltime
- Processchecker
- qsub

## Summary
A user reported repeated job terminations after approximately 8 hours on the HPC cluster. The user was running COMSOL sweeps as batch jobs but encountered issues with long-running processes on the frontend.

## Root Cause
- The user was running long processes on the frontend, which is not intended for such tasks.
- The process was automatically killed after running for more than 8 hours due to the frontend's policy of not allowing long-running processes.

## Solution
- The user should submit batch jobs for long-running processes instead of running them on the frontend.
- Use the `qsub` command with appropriate parameters to submit jobs to the cluster.
- For interactive work, consider using interactive batch jobs with the `-I` and `-X` parameters in `qsub`.

## General Learnings
- Frontends are intended for compiling, submitting jobs, and short tasks, not for running long processes.
- Long-running processes should be submitted as batch jobs to avoid automatic termination.
- Proper use of `qsub` and understanding of job scheduling policies can prevent such issues.

## Recommendations
- Educate users on the appropriate use of frontends and batch job submission.
- Ensure users are aware of the policies regarding long-running processes on frontends.
- Provide guidelines on using `qsub` for batch and interactive job submissions.
```
---

### 2020050442000635_Walltime%20extension.md
# Ticket 2020050442000635

 ```markdown
# Walltime Extension Request

## Keywords
- Walltime extension
- Job ID: 793535
- User: gwgi18
- Cluster: meggie
- Requested walltime: 48 hours

## Problem
- User requested an extension of walltime for a specific job.

## Root Cause
- The user's job required additional time to complete.

## Solution
- The HPC Admin responded with a cryptic message indicating a certificate expiration, but it is unclear if the walltime extension was granted.

## Lessons Learned
- Users may request walltime extensions for their jobs.
- HPC Admins should provide clear communication regarding the status of such requests.
- Ensure that certificates and other necessary credentials are up to date to avoid potential issues.
```
---

### 2023042142002517_Verl%C3%83%C2%A4ngerung%20eines%20HPC%20Jobs.md
# Ticket 2023042142002517

 ```markdown
# HPC Support Ticket: Job Extension Beyond 24-Hour Limit

## Keywords
- Job extension
- 24-hour limit
- Job ID
- Cluster specification

## Problem
- User requested an extension for a running job beyond the 24-hour limit.
- Job ID provided: 718984.

## Root Cause
- User needed additional time for the job to run over the weekend to generate more results.

## Solution
- HPC Admin extended the job duration.
- User was advised to include the cluster name along with the Job ID in future requests.

## General Learnings
- It is possible to extend job durations beyond the 24-hour limit on a case-by-case basis.
- Always include both the Job ID and the cluster name when requesting job extensions.
```
---

### 2023081042002754_wallclock-time%20extension%20in%20SLURM.md
# Ticket 2023081042002754

 # HPC Support Ticket: Wallclock Time Extension in SLURM

## Keywords
- Wallclock time limit
- SLURM
- Job runtime extension
- Multinode queues
- SuperMUC

## Problem
- User's simulations require more than the default 24-hour wallclock time limit.
- User requests an extension to 48 hours for jobs in multinode queues.

## Root Cause
- The default wallclock time limit for jobs is set to 24 hours, which is insufficient for the user's simulations.

## Solution
- HPC Admins confirmed that jobs are limited to 24 hours by default.
- However, they offer the possibility to extend runtimes if cluster operations allow it.
- To request an extension, users should send an email with the following details:
  - Cluster name
  - Job ID
  - New walltime

## General Learnings
- The default wallclock time limit for jobs is 24 hours.
- Extensions to job runtimes can be requested via email if operationally feasible.
- Users should provide specific details (cluster name, job ID, new walltime) when requesting an extension.

## Related Links
- [NHR@FAU HPC Support](mailto:support-hpc@fau.de)
- [NHR@FAU Website](https://hpc.fau.de/)
- [de-RSE Würzburg Chapter](https://de-rse.org/chapter/wue/)
---

### 2021112442002538_Re%3A%20%5BRRZE-HPC%5D%20Scheduled%20Downtime%20of%20RRZE%20HPC%20systems%20on%20July%2027.md
# Ticket 2021112442002538

 ```markdown
# HPC Support Ticket Conversation Analysis

## Subject: Re: [RRZE-HPC] Scheduled Downtime of RRZE HPC systems on July 27

### Keywords:
- Scheduled Downtime
- RRZE HPC Systems
- New Termin
- Mail Notification

### Summary:
- **HPC Admin** confirms the correctness of the scheduled downtime but mentions that a new date has been communicated via email.

### What to Learn:
- **Communication**: Ensure that any changes to scheduled downtimes are promptly communicated to all relevant parties via email.
- **Documentation**: Keep records of all changes and updates to scheduled maintenance to avoid confusion.

### Root Cause:
- The initial downtime schedule was updated, and a new date was communicated via email.

### Solution:
- Ensure that all stakeholders are informed about any changes to scheduled downtimes through official communication channels.
```
---

### 2024062042003094_Question%20regarding%20maximum%20hours%20of%20running%20jobs%20-%20iwfa053h.md
# Ticket 2024062042003094

 ```markdown
# HPC-Support Ticket Conversation: Maximum Job Runtime

## Keywords
- Job runtime
- 24-hour limit
- Job hold
- Resource allocation
- Exception request

## Summary
A user inquired about the possibility of running jobs longer than 24 hours to avoid the inconvenience of resuming jobs every 24 hours.

## Root Cause
The user found it inconvenient to resume jobs every 24 hours due to the system's default job runtime limit.

## Solution
- **Job Submission with Hold Option**: Users should submit jobs with the `--hold` option to prevent them from starting immediately.
- **Exception Request**: Users need to send an email to `support-hpc@fau.de` listing the JobIDs and the requested extended runtime.
- **Admin Assessment**: The HPC admin will assess the request and may prolong the job runtime if deemed appropriate.

## General Learnings
- The default job runtime limit is 24 hours.
- Exceptions can be made for longer job runtimes by submitting a request to the HPC support team.
- Proper resource management is crucial to avoid blocking resources for other users.

## Additional Notes
- The HPC admin emphasized the importance of resource management and the potential impact on other users if resources are blocked for extended periods.
- The user's request was noted, but the admin highlighted that laziness is not a valid argument for extending job runtimes.
```
---

### 2019052542000483_Wenn%20m%C3%83%C2%B6glich%20bitte%20Job%20auf%20meggie2%20leben%20lassen.md
# Ticket 2019052542000483

 # HPC Support Ticket: Job on Frontend

## Keywords
- Frontend jobs
- CPU time
- Kill mechanism
- `curl`
- `wget`
- `/lxfs` access

## Summary
A user requested to keep a job running on a frontend node (meggie2) despite the policy against running jobs on frontends. The job uses `curl` to run tasks on a remote machine in Munich and accesses `/lxfs`.

## Root Cause
- The user's job requires access to `/lxfs` and minimal CPU usage, making it convenient to run on a frontend.
- The job runs `curl` commands in a loop, which consumes negligible CPU time.

## Solution
- The HPC Admin explained that the kill mechanism on frontends is based on CPU time usage.
- Jobs that do not consume significant CPU time (like those running `curl` or `wget` in a loop) are unlikely to be killed.
- The user was reassured that their job should not be affected as long as it does not accumulate significant CPU time.

## General Learnings
- Frontends are not intended for running jobs, but minimal CPU usage jobs may not be affected by the kill mechanism.
- The kill mechanism on frontends is based on accumulated CPU time, ranging from 1 to 8 hours depending on the machine's load.
- Access to specific file systems like `/lxfs` can influence where users prefer to run their jobs.

## Action Items
- Users should be aware of the frontend usage policy and the conditions under which their jobs might be killed.
- HPC Admins should monitor frontend usage to ensure compliance with policies while accommodating special cases with minimal impact.
---

### 2018101242001711_Verl%C3%83%C2%A4ngerung%20der%20Laufzeit%20eines%20Jobs.md
# Ticket 2018101242001711

 ```markdown
# HPC Support Ticket: Extending Job Walltime

## Keywords
- Job walltime extension
- Lima Cluster
- Job ID
- Username
- Walltime increase

## Summary
A user submitted a job on the Lima Cluster and requested an extension of the job's walltime to 72 hours. The user later indicated that the issue had been resolved and would contact support again the following week.

## Root Cause
- User requested an increase in walltime for a submitted job.

## Solution
- The user resolved the issue independently and indicated they would follow up the next week.

## General Learnings
- Users may request walltime extensions for their jobs.
- It is important to provide clear instructions on how to request such extensions.
- Follow-up communication is crucial to ensure the issue is fully resolved.

## Actions Taken
- The user initially requested a walltime extension.
- The user later resolved the issue and indicated they would follow up.

## Notes
- Ensure users are aware of the process for requesting walltime extensions.
- Provide clear documentation on how to manage job walltime.
```
---

### 2024052242003958_Extend%20time%20limit%20-%20b155ee10%20-%20possibilities%20for%20automatic%20restarts.md
# Ticket 2024052242003958

 # HPC Support Ticket: Extend Time Limit and Automatic Restarts

## Keywords
- Job extension
- Time limit
- Automatic job restarts
- Slurm options
- Array jobs
- Job dependencies
- Chain jobs

## Problem
- User requested extension of job time limit to 5 days.
- User spends significant time manually restarting jobs due to daily time limits.
- User plans to run large-scale simulations over several months, requiring frequent job resubmissions.

## Root Cause
- Current job time limit is 1 day, causing frequent manual job restarts.
- User's workflow involves checking files manually before each restart, which is time-consuming.

## Solution
- **Job Extension**: HPC Admins extended the specific jobs to 5 days but did not grant a general extension due to resource constraints.
- **Automatic Restarts**: HPC Admins suggested several Slurm options for automatic job restarts:
  - **Array Jobs**: Use `--array=8%1` to run instances one by one.
  - **Job Dependencies**: Use `--dependency=afterok:PREVIOUS-JOBID` or `afterany`.
  - **Chain Jobs**: Submit the next job before the current one terminates, ensuring sufficient runtime using the Bash variable `$SECONDS`.

## General Learnings
- Extending job time limits for all users is not feasible due to resource constraints.
- Slurm provides several options for automatic job restarts to reduce manual effort.
- Users should be guided to use these options to optimize their workflow.
- Regular communication and support, including offering meetings, can help users implement these solutions.

## Follow-up
- User agreed to try the suggested Slurm options for automatic restarts.
- Further assistance and a Zoom meeting were offered by the 2nd Level Support team.
---

### 2020091142003273_Wall-time%20extension%20%28gwgi18%20on%20meggie%29.md
# Ticket 2020091142003273

 ```markdown
# HPC-Support Ticket: Wall-time Extension

## Keywords
- Wall-time extension
- Job extension
- Single-node jobs
- HPC support

## Summary
A user requested an extension of wall-time for specific jobs.

## Root Cause
- User needed additional time to complete their computational tasks.

## Solution
- HPC Admin extended the wall-time for the specified jobs.

## What Can Be Learned
- Users can request extensions for their jobs if they need more time.
- HPC Admins can extend the wall-time for single-node jobs upon request.

## Actions Taken
- HPC Admin extended the wall-time for the specified jobs.

## Notes
- Ensure that users provide the job IDs when requesting extensions.
- HPC Admins should confirm the extension and notify the user.
```
---

### 2025030442000862_Jobverl%C3%83%C2%A4ngerung%20-%20JobID%2034394.md
# Ticket 2025030442000862

 # HPC Support Ticket: Job Extension Request

## Keywords
- Job extension
- Job ID
- Cluster specification
- User request
- Admin response

## Summary
A user requested an extension for a specific job but did not initially provide the cluster information. The HPC Admin extended the job and reminded the user to include the cluster details in future requests.

## Root Cause
- User did not specify the cluster on which the job was running.

## Solution
- HPC Admin extended the job and advised the user to include the cluster information in future requests.

## Lessons Learned
- Always include the cluster information when requesting job extensions.
- HPC Admins can extend job durations upon user request.

## Follow-Up Actions
- Users should be reminded to provide complete information in their support requests.
- HPC Admins should ensure that all necessary details are included in user communications.

## Relevant Roles
- HPC Admins
- 2nd Level Support Team
- Head of the Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support
- Software and Tools Developer
---

### 2025031142002329_35775%20job%20extension.md
# Ticket 2025031142002329

 # HPC Support Ticket: Job Extension Request

## Keywords
- Job extension
- Maintenance schedule
- Time limit
- NeurIPS experiments

## Summary
A user requested an extension for job 35775 on the HPC system "helma" to one week. The request was modified due to a scheduled maintenance.

## Root Cause
The user's initial request for a one-week extension conflicted with a scheduled maintenance on Monday.

## Solution
The HPC Admin set the time limit to 6 days to accommodate the maintenance schedule.

## What Can Be Learned
- Always check the maintenance schedule before requesting job extensions.
- Be prepared to adjust job time limits to fit within maintenance windows.
- Clear communication between users and HPC Admins is crucial for managing job schedules effectively.

## Actions Taken
1. User requested a one-week extension for job 35775.
2. HPC Admin identified a conflict with the scheduled maintenance.
3. HPC Admin adjusted the time limit to 6 days.
4. User acknowledged the adjustment and the ticket was closed.

## Follow-Up
No further action is required for this ticket. Users should be reminded to check the maintenance schedule for future job extension requests.
---

### 2024041542004892_Increase%20Time%20of%20Job.md
# Ticket 2024041542004892

 # HPC Support Ticket: Increase Time of Job

## Keywords
- Job runtime extension
- Job ID
- Cluster
- Support request

## Problem
- **Root Cause:** User requested an increase in the runtime for a specific job.
- **Details:**
  - Job ID: 1569884
  - Requested Runtime: 3 days
  - Cluster: Alex

## Solution
- **Action Taken:** HPC Admin increased the runtime of the job as requested.
- **Outcome:** The runtime extension was successfully applied.

## General Learnings
- Users may request runtime extensions for their jobs.
- HPC Admins can handle such requests and make the necessary adjustments.
- Ensure clear communication and prompt action to address user needs.

## Next Steps
- Document the process for extending job runtimes for future reference.
- Ensure users are aware of the procedure for requesting runtime extensions.
---

### 2023022742000226_Jobverl%C3%83%C2%A4ngerung.md
# Ticket 2023022742000226

 ```markdown
# HPC Support Ticket: Jobverlängerung

## Keywords
- Job Extension
- Job ID
- HPC Support
- Ticket

## Summary
A user requested an extension for a job with a specific ID. The HPC Admin responded with a brief acknowledgment.

## Problem
- **Root Cause**: User needed to extend the runtime of a job.

## Solution
- **Action Taken**: HPC Admin acknowledged the request and marked it as completed.

## Lessons Learned
- Users can request job extensions via support tickets.
- HPC Admins handle job extension requests and provide confirmation.

## Notes
- Ensure job extensions are handled promptly to avoid disruptions in user workflows.
- Maintain clear communication with users regarding the status of their requests.
```
---

### 2019052142000285_Laufzeit%20von%20Job%27s%20auf%207%20Tage%20anheben%3F.md
# Ticket 2019052142000285

 # HPC Support Ticket: Extending Job Runtime

## Keywords
- Job runtime extension
- Direct job start
- Simulation deadline
- DLR meeting
- Job IDs
- User request

## Summary
A user requested an extension of the runtime for specific jobs to 7 days and an immediate start due to an upcoming meeting at DLR.

## Root Cause
- User needs to complete simulations before a specific deadline (DLR meeting on 28.05.19).

## Solution
- The user requested the HPC Admins to extend the runtime of the jobs with IDs 1113518.eadm, 1113519.eadm, and 1113520.eadm to 7 days and to start them immediately.

## General Learning
- Users may require runtime extensions and immediate job starts for urgent deadlines.
- HPC Admins should evaluate such requests based on system load and priority.

## Actions Taken
- The request was forwarded to the HPC Admins for evaluation and action.

## Notes
- Ensure proper communication with the user regarding the feasibility of the request.
- Document any changes made to job configurations for future reference.
---

### 2024041542005015_Request%20for%20%20time%20quota%20increase%20%28HPC%20id%20%3A%20v100dd17%20%29.md
# Ticket 2024041542005015

 ```markdown
# HPC Support Ticket: Request for Time Quota Increase

## Keywords
- Time quota increase
- Job ID
- Cluster name
- Training duration
- Job prolongation

## Summary
A user requested an increase in their time quota from 24 hours to 72 hours for a job that requires three days to train a Swin-L transformer-based backbone for a video understanding project.

## Problem
- The user's job takes longer than the default time quota due to the iterative unrolling of video frames.
- The initial job was killed, and the user needed to restart it.

## Solution
1. **Initial Request**: The user provided their HPC account ID and the reason for the quota increase.
2. **Admin Response**: The admin requested the job ID and the name of the cluster.
3. **User Follow-up**: The user provided the job ID (1571212) and the cluster name (Alex).
4. **Admin Action**: The admin increased the time quota for the specified job.
5. **Job Restart**: The user's job was killed and restarted. The user provided the new job ID (1571829) and requested the time quota increase again.
6. **Admin Action**: The admin increased the time quota for the new job.

## Lessons Learned
- Always provide the job ID and the name of the cluster when requesting a time quota increase.
- Avoid opening new tickets for the same request; follow up on the existing ticket.
- The admin will consider the request and increase the time quota if necessary.

## Notes
- The user is a final year PhD student working in Computer Vision.
- The training procedure takes longer due to the iterative unrolling of video frames.
- The admin forwarded the request to the appropriate personnel and confirmed the action.
```
---

### 2020092842003483_Verl%C3%83%C2%A4ngerung%20job%20820177%20auf%20meggie.md
# Ticket 2020092842003483

 ```markdown
# HPC Support Ticket: Job Extension and File Output Issue

## Keywords
- Job extension
- VASP calculation
- File output issue
- Filesystem error

## Summary
A user requested an extension for a VASP job (ID: 820177) on the HPC system "Meggie" due to the job requiring more than the default 24-hour runtime. The job was extended to 96 hours. However, the user encountered an issue where the job stopped producing output to files after a certain period.

## Root Cause
- The job required more runtime than the default 24 hours due to the nature of the VASP calculation.
- After the extension, the job stopped producing output to files, which was not observed in previous shorter test runs.

## Solution
- The HPC Admin extended the job runtime to 96 hours.
- The user decided to abort the job and perform a shorter test run to diagnose the issue further.

## Lessons Learned
- Some VASP calculations may require longer runtimes and cannot be easily restarted.
- Unexpected file output issues can occur even after extending job runtimes.
- It is important to monitor jobs closely after extending their runtimes to catch any potential issues early.

## Actions Taken
- HPC Admin extended the job runtime.
- User aborted the job and planned to perform a shorter test run to diagnose the file output issue.
```
---

### 2022072242001138_Re%3A%20Long%20running%20process%20on%20host%20woody3.md
# Ticket 2022072242001138

 # HPC Support Ticket: Long Running Process on Host

## Keywords
- Long running process
- Frontend usage
- Batch job submission
- Interactive batch jobs
- Dataset download

## Problem
- User ran a long download process on the frontend (`woody3`), which was automatically killed after exceeding the time limit.

## Root Cause
- The frontend is not intended for long-running processes. Processes running for more than 30 minutes are reniced and killed after one hour to prevent disturbance to other users.

## Solution
- Submit long-running processes as batch jobs to the cluster.
- For interactive work, use interactive batch jobs with parameters `-I` and `-X` to `qsub`.

## General Learning
- Frontends should only be used for short tasks like compiling and submitting jobs.
- Long-running tasks should be submitted as batch jobs to dedicated nodes.
- Interactive batch jobs are available for tasks requiring user interaction.

## HPC Admin Response
- Confirmed that the user should submit the download process as a job to the cluster.
- Suggested the use of the RRZE-HPC-Proxy if needed.

## Related Teams
- HPC Admins
- 2nd Level Support Team
- Datacenter Head
- Training and Support Group Leader
- NHR Rechenzeit Support
- Software and Tools Developers
---

### 2024022642002984_Connection%20to%20HPC%20cluster%20down%21.md
# Ticket 2024022642002984

 ```markdown
# HPC Support Ticket: Connection to HPC Cluster Down

## Keywords
- Connection issue
- HPC cluster downtime
- Scheduled maintenance
- Alex
- Tinyx

## Problem Description
- User unable to connect to HPC clusters (Alex and Tinyx).

## Root Cause
- Scheduled maintenance on the HPC systems.

## Solution
- Wait for the maintenance to be completed and try connecting again the next day.

## Lessons Learned
- Always check for scheduled maintenance announcements before reporting connection issues.
- Maintenance notifications are typically sent via email and posted on the HPC website.

## References
- [Scheduled Downtime Announcement](https://hpc.fau.de/2024/02/20/scheduled-downtime-of-nhrfau-systems-on-monday-february-26/)
```
---

### 2024052942000313_Fwd%3A%20Long%20running%20process%20on%20host%20alex2.md
# Ticket 2024052942000313

 # HPC Support Ticket: Long Running Process on Host Alex2

## Subject
- Fwd: Long running process on host alex2

## User Issue
- User needs to download data, which takes several hours.
- User's process on host alex2 was killed automatically for running too long.

## Root Cause
- The frontends are not meant for running long processes.
- Processes running for more than 30 minutes are reniced and killed after one hour.

## Solutions Provided
- **Option 1: Submit as a Batch Job**
  - Submit the download as a batch job to one of the compute nodes.
  - Resume the download after 24 hours if needed.
- **Option 2: Use Memoryhog**
  - Connect to `memoryhog.rrze.fau.de` and start the download interactively.
  - Add the following lines to the SSH config:
    ```plaintext
    Host memoryhog.rrze.fau.de memoryhog
        HostName memoryhog.rrze.fau.de
        User <HPC account>
        ProxyJump csnhr.nhr.fau.de
        IdentityFile ~/.ssh/id_ed25519_nhr_fau
        IdentitiesOnly yes
        PasswordAuthentication no
        PreferredAuthentications publickey
        ForwardX11 no
        ForwardX11Trusted no
    ```

## Additional Information
- **Disk Space Issue**
  - User requested additional disk space but later freed up space from other places.
  - User reported that the process on Memoryhog was stuck and did not progress.

## Key Learnings
- **Frontend Usage**
  - Frontends should not be used for long-running processes.
  - Processes running for more than 30 minutes are reniced and killed after one hour.
- **Batch Jobs**
  - For long-running processes, submit a batch job to a compute node.
  - Batch jobs can be resumed after 24 hours if needed.
- **Memoryhog Usage**
  - Memoryhog can be used for interactive downloads without a batch job.
  - Ensure the SSH config is correctly set up to connect to Memoryhog.

## Recommendations
- **Data Format**
  - Avoid storing millions of small files on the filesystem.
  - Use a container data format to prevent performance issues.

## Unresolved Issues
- **Memoryhog Process Stuck**
  - The user reported that the download process on Memoryhog was stuck.
  - Further investigation is needed to resolve this issue.

## Next Steps
- **Disk Space Allocation**
  - The ticket was handed over to colleagues for disk space allocation.
  - User requested 500 GB of additional space but later freed up space from other places.

## Conclusion
- The user was provided with two options for downloading data: submitting a batch job or using Memoryhog.
- The user encountered issues with the process on Memoryhog, which requires further investigation.
- The user was advised on the proper usage of frontends and the importance of data format for filesystem performance.
---

### 2020052942000142_Amock-laufender%20Kettenjob%20auf%20Woody%20-%20bctc55.md
# Ticket 2020052942000142

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject: Amock-laufender Kettenjob auf Woody - bctc55

### Keywords:
- Kettenjob
- Woody
- Batchsystem
- Simulation
- qsub
- turbo-loop.woody.pbs
- SECONDS
- Runtime
- Automatic restart

### Root Cause:
- The user's chain job "C60" on Woody is resubmitting itself every few seconds without running the actual computation, causing extreme load on the batch system and disrupting operations.

### Solution:
- Ensure that the chain job reliably terminates if the simulation fails.
- Insert the following script before the `qsub turbo-loop.woody.pbs` command to prevent automatic restart if the runtime is too short:
  ```bash
  if [ $SECONDS -lt 1800 ]; then
  echo "*** no automatic restart as runtime of the present job was too short"
  exit
  fi
  ```

### General Learnings:
- Chain jobs should be designed to handle failures gracefully to avoid excessive load on the batch system.
- Implementing runtime checks can help prevent unnecessary job resubmissions.
- Proper scripting practices can mitigate disruptions to the HPC environment.
```
---

### 2023102042000741_Long%20Job.md
# Ticket 2023102042000741

 # HPC Support Ticket: Long Job

## Keywords
- Walltime
- Job extension
- HPC support
- Job ID
- User ID

## Summary
A user requested an extension of the walltime for their job on the HPC system. The HPC admin extended the walltime as requested.

## Problem
- User's job (ID: 2411571) required an extended walltime of 5 days.
- The initial job failed, and the user requested another extension for a new job (ID: 2411783).

## Solution
- HPC Admin extended the walltime for both jobs as requested by the user.
- The user was informed about the extension and thanked the admin.

## Lessons Learned
- Users may need to request extensions for their jobs if the initial walltime is insufficient.
- HPC admins can extend the walltime for jobs upon user request.
- Proper communication and prompt action by the HPC support team ensure smooth operation of user jobs.

## Actions Taken
- HPC Admin extended the walltime for the user's jobs.
- The ticket was closed after the user confirmed the extension.

## Recommendations
- Users should monitor their jobs and request extensions if needed.
- HPC support should be responsive to user requests for job extensions.

## Follow-Up
- No further follow-up required as the issue was resolved and the ticket was closed.
---

### 2024021942003577_Request%20for%20longer%20runs%20on%20Alex.md
# Ticket 2024021942003577

 # HPC Support Ticket: Request for Longer Runs on Alex

## Keywords
- Extended runtime
- JobID
- Downtime
- HPC systems
- Alex

## Summary
A user requested extended runtimes for a set of experiments on the HPC system Alex, which would take up to 72 hours.

## Root Cause
The user needed longer runtime for their experiments but was unaware of the procedure for requesting extended runtime.

## Solution
- **Extended Runtime Request Procedure**: Extended runtime is granted on an individual job basis. Users must start their job and then send the JobID to the HPC support team to request longer runtime.
- **Downtime Notice**: The HPC admin informed the user about an upcoming downtime on 26.02.

## General Learnings
- Extended runtime requests require the JobID of the running job.
- Users should be aware of scheduled downtimes that may affect their jobs.
- Communication with the HPC support team is essential for special requests and staying informed about system status.

## Related Parties
- HPC Admins
- 2nd Level Support Team
- Users of the HPC system Alex

## Further Actions
- None required for this specific ticket, but users should be reminded to check for downtimes and follow the correct procedure for extended runtime requests.
---

### 2020052942002444_Walltime%20extension.md
# Ticket 2020052942002444

 # Walltime Extension Request

## Keywords
- Walltime extension
- Job IDs: 798140, 798173
- User: gwgi18
- System: meggie
- Software: WRF 4.2
- Issue: Restarts broken

## Summary
- **User Request**: Additional 12 hours of walltime for jobs 798140 and 798173 due to broken restarts in WRF 4.2.
- **HPC Admin Response**: No clear action indicated in the provided conversation.

## Root Cause
- Broken restarts in WRF 4.2.

## Solution
- Not explicitly provided in the conversation.

## Notes
- The user requested an extension due to software issues.
- The HPC Admin's response is unclear and may require further follow-up.

## Next Steps
- Verify if the walltime extension was granted.
- Check the status of jobs 798140 and 798173.
- Follow up with the user to confirm if the issue with WRF 4.2 restarts has been resolved.
---

### 2021102742001839_Bitte%20Walltime.md
# Ticket 2021102742001839

 ```markdown
# HPC Support Ticket: Walltime Increase Request

## Keywords
- Walltime
- JobID
- Tinyfat
- Publication
- HPC Admin

## Summary
A user requested an increase in walltime for several large jobs on the Tinyfat cluster due to an upcoming publication. The user had already attempted to optimize the jobs but required additional time.

## Problem
- **Root Cause**: Insufficient walltime for large jobs needed for an upcoming publication.
- **Specific JobIDs**:
  - JobID 163719: Required 120 hours
  - JobID 163722: Required 180 hours
  - JobID 163724: Required 120 hours
  - JobID 163730: Required 180 hours

## Solution
- **Action Taken**: HPC Admin increased the walltime for the specified jobs.
- **Outcome**: The user expressed gratitude for the walltime increase.

## General Learnings
- Users may require extended walltime for critical research projects.
- HPC Admins can accommodate such requests on a case-by-case basis.
- Clear communication and justification from the user can facilitate quicker resolution.
```
---

### 2025030642000779_Laufzeitverl%C3%83%C2%A4ngerung%20n100af14%20Job%201837089.md
# Ticket 2025030642000779

 # HPC Support Ticket Analysis

## Subject
Laufzeitverlängerung n100af14 Job 1837089

## Keywords
- Laufzeitverlängerung (runtime extension)
- Job ID: 1837089
- User request
- HPC Admin response
- Overlooked request

## Summary
A user requested a runtime extension for their job, but the initial request was overlooked by the HPC Admin. The request was eventually addressed after a follow-up email.

## Root Cause
- Initial request was overlooked by the HPC Admin.

## Solution
- The runtime was extended after the follow-up request.

## Lessons Learned
- Importance of timely response to user requests.
- Follow-up emails can help ensure requests are not overlooked.
- Clear communication between users and HPC Admins is crucial.

## General Takeaways
- Users should follow up on their requests if they do not receive a timely response.
- HPC Admins should have a system in place to track and respond to user requests promptly.
- Effective communication can prevent delays and ensure user satisfaction.
---

### 2023021742000423_Job%20Verl%C3%83%C2%A4ngerung.md
# Ticket 2023021742000423

 ```markdown
# HPC Support Ticket: Job Verlängerung

## Keywords
- Job Extension
- Rechenzeit
- Sicherheitszuschlag
- Jobid

## Summary
A user requested an extension for their job with a specific Jobid due to an estimated computation time of 41 hours, with an additional safety margin of 44 hours.

## Root Cause
The user's job required more computation time than initially allocated.

## Solution
The HPC Admin extended the job time with an additional buffer.

## Lessons Learned
- Users may underestimate the required computation time for their jobs.
- It is important to provide a safety margin when estimating job duration.
- HPC Admins can extend job times upon user request to ensure completion.
```
---

### 2023010642000339_Verl%C3%83%C2%A4ngerung%20Jobs%20Alex.md
# Ticket 2023010642000339

 # HPC Support Ticket: Job TimeLimit Extension

## Keywords
- Job TimeLimit Extension
- GPU Utilization
- Job Verlängerung
- Wartung
- HPC Support
- Alex Cluster

## Summary
A user requested an extension of the TimeLimit for their jobs on the Alex cluster. The HPC Admin provided the extension but noted low GPU utilization and upcoming hardware maintenance that could affect job completion.

## Conversation Details

### User Request
- **Initial Request:** User requested to extend the TimeLimit for four jobs on the Alex cluster to 5 days.
- **Follow-up Request:** User requested an additional 5-day extension due to ongoing work on a UNet configuration.

### HPC Admin Response
- **Initial Extension:** HPC Admin confirmed the extension and noted low GPU utilization (under 30%), suggesting potential for code optimization.
- **Second Extension:** HPC Admin extended the jobs again but warned about upcoming hardware maintenance that could interrupt the jobs.
- **Maintenance Notice:** HPC Admin informed the user that the jobs would need to be terminated due to scheduled maintenance, advising the user to end the jobs cleanly before the maintenance.

## Root Cause
- User's jobs required more time due to ongoing research and configuration work.
- Low GPU utilization indicated potential for code optimization.

## Solution
- HPC Admin extended the TimeLimit for the jobs as requested.
- User was advised to optimize their code for better GPU utilization.
- User was informed about upcoming maintenance and advised to end jobs cleanly before the maintenance period.

## General Learnings
- Users may request extensions for jobs due to ongoing research or configuration work.
- Monitoring GPU utilization can help identify opportunities for code optimization.
- Scheduled maintenance can impact job completion, and users should be informed in advance.

## Action Items
- Extend job TimeLimits as requested by users, when feasible.
- Monitor job performance and provide feedback on potential optimizations.
- Inform users about upcoming maintenance and its potential impact on their jobs.
---

### 2025022042002984_%C3%A7%C2%AD%C2%94%C3%A5%C2%A4%C2%8D%3A%20%5BEXT%5D%20Long%20running%20process%20on%20host%20fritz3.md
# Ticket 2025022042002984

 # HPC Support Ticket Analysis: Long Running Process on Host

## Keywords
- Long running process
- Frontend usage
- OMP_NUM_THREADS
- Batch job submission
- Interactive batch jobs

## Summary
A user's process was automatically killed for running too long on a frontend node. The user later optimized their code by setting `OMP_NUM_THREADS=1`, significantly reducing runtime.

## Root Cause
- User ran a long process on a frontend node, which is not intended for such tasks.
- Initial code was not optimized for frontend usage.

## Solution
- Set `OMP_NUM_THREADS=1` to reduce runtime.
- For processes requiring more than 30 minutes, submit a batch job to get a dedicated node.
- Use interactive batch jobs for interactive work.

## General Learnings
- Frontends are for compiling, submitting jobs, and short tasks, not for long-running processes.
- Long processes should be submitted as batch jobs.
- Optimizing code (e.g., setting `OMP_NUM_THREADS`) can significantly reduce runtime.
- Interactive batch jobs are available for interactive work requiring longer CPU time.
---

### 2021082542000642_Wall%20time%20limit%20extension.md
# Ticket 2021082542000642

 ```markdown
# Wall Time Limit Extension

## Keywords
- Wall time limit
- Slurm
- Job ID
- Rechenjob
- Meggie-Cluster
- Atmospheric simulation

## Problem
- User submitted a job (ID 938648) on the Meggie-Cluster that exceeds the default wall time limit of 24 hours.
- The job is a high-resolution atmospheric simulation expected to run for approximately 52 hours.

## Root Cause
- The default wall time limit for jobs on the Meggie-Cluster is set to 24 hours.
- The user's job requires more time due to the complexity and duration of the simulation.

## Solution
- HPC Admin extended the wall time limit for the specific job (ID 938648) to 52 hours.

## General Learning
- Users should estimate the required wall time for their jobs based on previous test runs.
- If a job requires more time than the default limit, users should request an extension from the HPC support team.
- HPC Admins can adjust the wall time limit for specific jobs upon user request.
```
---

### 2024091342002156_Walltime%20extension%20%28c104fa12%20on%20Fritz%29.md
# Ticket 2024091342002156

 # HPC Support Ticket: Walltime Extension

## Keywords
- Walltime extension
- Job stability
- WRF (Weather Research and Forecasting Model)
- Job requeue

## Summary
A user requested walltime extensions for specific jobs to avoid issues related to WRF and job restarts. The HPC admins extended the walltimes as requested. The user later requested additional walltime extensions due to stability issues.

## Root Cause
- Initial walltime was insufficient for job completion.
- Stability issues with jobs required additional walltime extensions.

## Solution
- HPC admins extended the walltimes for the specified jobs.
- Additional walltime extensions were granted upon further request due to stability issues.

## General Learnings
- Users may request walltime extensions to avoid job interruptions.
- Stability issues can necessitate additional walltime extensions.
- HPC admins can quickly address walltime extension requests to support user needs.

## Actions Taken
- Extended walltimes for jobs 1575257 and 1575260 to 28 hours.
- Extended walltimes for jobs 1579556 and 1579555 upon further request.

## Follow-Up
- Monitor job stability and performance to identify recurring issues.
- Provide guidance on optimizing job submissions to minimize stability problems.
---

### 2021062542000413_Wall%20time%20extension%20896425%20%28gwgi18%20on%20meggie%29.md
# Ticket 2021062542000413

 ```markdown
# HPC Support Ticket Conversation Analysis

## Subject: Wall time extension 896425 (gwgi18 on meggie)

### Keywords:
- Wall time extension
- Meggie
- Job IDs: 896425, 896771, 896772
- Certificate expiration

### Summary:
- **User Request**: Initially requested a 12-hour wall time extension for job 896425 on Meggie.
- **HPC Admin Response**: Confirmed the extension with a note about certificate expiration.
- **User Follow-up**: Requested additional extensions for jobs 896771 and 896772, suggesting Meggie might be underutilized.
- **HPC Admin Response**: Confirmed the extensions but clarified that Meggie is not underutilized.

### Root Cause:
- User needed additional wall time for their jobs.

### Solution:
- HPC Admin granted the requested wall time extensions.

### General Learnings:
- Users may request wall time extensions if their jobs require more time.
- HPC Admins can grant these extensions if the system allows.
- Certificate expiration notices may be included in responses.
- Users may inquire about system utilization when requesting extensions.

### Documentation for Support Employees:
- When users request wall time extensions, verify the system's current load and grant extensions if feasible.
- Include any relevant notices, such as certificate expirations, in the response.
- Clarify system utilization if users inquire about it.
```
---

### 2024100942001135_Request%20for%20exception%20in%20runtime%20limit.md
# Ticket 2024100942001135

 ```markdown
# HPC Support Ticket: Request for Exception in Runtime Limit

## Keywords
- Runtime limit
- Exception request
- Turbomole calculation
- Checkpoint-restart
- Fritz access

## Summary
A user requested an exception to the maximum runtime limit of 24 hours for a turbomole calculation that requires more time to complete. The user successfully ran calculations within 24 hours but needed more time to reach the desired number of excited states.

## Problem
- The user's turbomole calculation on the HPC system "woody" exceeds the 24-hour runtime limit.
- The calculation cannot be restarted from a checkpoint within 24 hours.
- The user needs to request many excited states to reach the energetic window of interest.

## Solution
- The user was instructed to start the job with the `#SBATCH --hold` flag and provide the job ID.
- HPC Admins extended the runtime for the job and released it.
- The user requested runtime extensions for additional jobs, which were granted.
- HPC Admins suggested implementing checkpoint-restart or moving to a more powerful system (Fritz) for future long-running simulations.
- The user was provided with a link to apply for access to Fritz.

## Lessons Learned
- Users can request exceptions to runtime limits by contacting HPC support.
- The `#SBATCH --hold` flag can be used to hold jobs for manual release by HPC Admins.
- Implementing checkpoint-restart can help manage long-running jobs.
- Access to more powerful nodes (e.g., Fritz) may be necessary for extensive calculations.

## Follow-up Actions
- The user should consider implementing checkpoint-restart for future jobs.
- The user should apply for access to Fritz if more powerful nodes are needed.
```
---

### 2024042642001918_Increase%20Time%20of%20Job.md
# Ticket 2024042642001918

 # HPC Support Ticket: Increase Time of Job

## Keywords
- Job runtime extension
- Holding jobs
- Alex cluster
- Job ID (JOBID)

## Problem
- User requested an increase in the runtime of specific holding jobs to 3 days on the Alex cluster.
- Job IDs: 1583119, 1583121, 1583122

## Solution
- HPC Admin extended the runtime of the specified jobs and released them.
- The jobs will execute one after the other.

## General Learnings
- Users can request runtime extensions for their jobs.
- HPC Admins can modify job parameters such as runtime and release holding jobs.
- Jobs may be set to execute sequentially after modification.

## Actions Taken
- HPC Admin extended the runtime and released the jobs as requested.

## Follow-up
- No further action required from the user or the support team.
---

### 2021080542003071_Re%3A%20Long%20running%20process%20on%20host%20emmy2.md
# Ticket 2021080542003071

 # HPC Support Ticket: Long Running Process on Host

## Keywords
- Long running process
- Frontend usage
- Batch job submission
- Interactive batch jobs
- `qsub` parameters `-I` and `-X`
- `parallel` command
- `rsync`

## Root Cause
- User was running a long process (`tar` command) on the frontend node, which exceeded the allowed time limit.
- The process was automatically killed by the system.

## Lessons Learned
- **Frontend Usage**: Frontends are intended for short tasks such as compiling, submitting jobs, etc., not for long-running processes.
- **Batch Job Submission**: For processes requiring more than 30 minutes of CPU time, users should submit a batch job to avoid disturbing others and to prevent the process from being killed.
- **Interactive Batch Jobs**: For interactive work, users can utilize interactive batch jobs with `qsub` parameters `-I` and `-X`.
- **Scripting for Parallel Tasks**: For complex tasks like parallel copying, writing a script with commands like `parallel` and `rsync` can be effective, although it may seem sophisticated.

## Solution
- Submit long-running processes as batch jobs.
- Use interactive batch jobs for interactive work.
- Consider scripting for parallel tasks if necessary.

## Ticket Closure
- The ticket was closed as the issue seemed to have been resolved in the meantime.
---

### 2024022642003705_Problem%20about%20Alex%20cluster.md
# Ticket 2024022642003705

 ```markdown
# HPC Support Ticket: Problem about Alex Cluster

## Keywords
- Alex cluster
- ReqNodeNotAvail
- Reserved for maintenance
- Scheduled downtime

## Problem Description
- **User ID:** iwi5166h
- **Issue:** Unable to submit tasks on Alex cluster since the 25th. Error message: `ReqNodeNotAvail, Reserved for maintenance`.

## Root Cause
- All nodes in the Alex cluster were under maintenance.

## Solution
- Maintenance was announced via email on February 15 and on the HPC website.
- Users were advised to try again the next day.

## General Learnings
- Always check for scheduled maintenance announcements via email or the HPC website.
- Maintenance periods can cause task submission failures with specific error messages like `ReqNodeNotAvail`.

## References
- [Scheduled Downtime Announcement](https://hpc.fau.de/2024/02/26/scheduled-downtime-of-nhrfau-systems-on-monday-february-26/)
```
---

### 2023030942000973_Re%3A%20%5BNHR%40FAU%5D%20Downtime%20of%20Alex%20and%20Testcluster%20on%20March%209.md
# Ticket 2023030942000973

 # HPC Support Ticket: Downtime of Alex and Testcluster

## Keywords
- Downtime
- Maintenance
- Power Grid
- Compute Nodes
- Login Nodes
- Batch Jobs

## Summary
- **Date:** March 9, 2023
- **Reason:** Scheduled downtime for maintenance of the power grid at the RRZE building.
- **Affected Systems:** Alex and Testcluster

## Details
- **Announcement:** HPC Admins announced a scheduled downtime starting at 00:00 on March 9.
- **Impact:** Jobs that would collide with the downtime were postponed. Frontends and fileservers remained available.
- **User Inquiry:** A user inquired about the availability of Alex after the downtime.
- **Response:** HPC Admins confirmed that login nodes were available and batch jobs could be queued, but there was no ETA for the compute nodes.

## Root Cause
- Maintenance of the power grid at the RRZE building.

## Solution
- Wait for the maintenance to be completed. Login nodes and fileservers remained accessible during the downtime.

## Notes
- Ensure users are informed about scheduled downtimes well in advance.
- Provide updates on the status of compute nodes after maintenance.

---

This documentation can be used as a reference for future scheduled downtimes and user inquiries regarding system availability.
---

### 42193363_Jobs%20848324%20und%20848325%20auf%20LiMa.md
# Ticket 42193363

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject: Jobs 848324 und 848325 auf LiMa

### Keywords:
- Job Failure
- LiMa
- Early Termination
- HPC Admin
- User Support

### Summary:
- **Issue**: Jobs 848324 and 848325 on LiMa terminated shortly after starting.
- **Root Cause**: Unknown from the provided conversation.
- **Solution**: Not provided in the conversation.

### What Can Be Learned:
- **Job Monitoring**: HPC Admins monitor job statuses and notify users of any issues.
- **Communication**: Importance of clear and timely communication between HPC Admins and users.
- **Troubleshooting**: Need for further investigation to identify the root cause of job failures.

### Next Steps:
- **Investigation**: Further analysis required to determine why the jobs terminated early.
- **Documentation**: Update documentation with common causes of early job termination and their solutions.
- **User Guidance**: Provide users with steps to diagnose and resolve similar issues in the future.
```
---

### 2018110242000748_Jobs%20auf%20LiMa%20laufen%20nicht%20an.md
# Ticket 2018110242000748

 ```markdown
# HPC Support Ticket: Jobs auf LiMa laufen nicht an

## Keywords
- Job submission
- Walltime
- Queue resources
- Batch system
- Error messages

## Problem Description
- User submitted jobs to the LiMa cluster but they remained in the queue and were eventually rejected.
- Job IDs: 2242151 - 2242168
- Account name: mppi019h

## Root Cause
- The jobs requested 48 hours of walltime, but the LiMa cluster only allows a maximum of 24 hours.

## Solution
- The user should resubmit the jobs with a walltime of 24 hours or less.
- The batch system should have provided an error message at the time of job submission, but it did not.

## Lessons Learned
- Always check the walltime requirements for the specific cluster before submitting jobs.
- Ensure that the batch system is configured to provide immediate error messages for invalid job parameters.
- Large jobs may need to be submitted directly to the Special-Queue if they exceed the limits of the route-Queue.

## Actions Taken
- The HPC Admin identified the issue with the walltime request.
- The route-Queue on LiMa was updated to check for walltime and node limits.
- The user was advised to resubmit the jobs with the correct walltime.
```
---

### 2024060542000884_Timewall%20Limit%20Erh%C3%83%C2%B6hung.md
# Ticket 2024060542000884

 ```markdown
# HPC Support Ticket: Timewall Limit Erhöhung

## Keywords
- Timewall Limit
- Job Submission
- Meggie-Cluster
- HPC Support
- Job-IDs
- --hold

## Problem
- User requests to increase the time limit for jobs on the Meggie-Cluster beyond 24 hours.
- User has calculations that require more than 24 hours to run continuously.

## Solution
- For individual jobs, the time limit can be increased by submitting them with the `--hold` option and then sending an email to HPC Support with the Job-IDs.
- A general increase in the time limit for all jobs of a user is not possible.
- The 24-hour time limit applies to all users, regardless of whether they are part of the basic service or specific projects.

## Notes
- The user was informed that the 24-hour time limit is a general rule for all users.
- The user was advised to submit jobs with the `--hold` option and then contact HPC Support for an increase in the time limit for specific jobs.

## Conclusion
- The user was provided with a solution to increase the time limit for specific jobs.
- The general time limit policy was clarified.
```
---

### 2023032342001212_Time%20limit%20model%20training.md
# Ticket 2023032342001212

 # HPC Support Ticket: Time Limit Model Training

## Keywords
- Time limit
- Model training
- JobID
- 24h limit

## Summary
- **User Issue**: User needs to increase the time limit for a model training job beyond the default 24h limit.
- **Root Cause**: The default time limit for jobs is insufficient for the user's model training task.
- **Solution**: Request HPC Admin to increase the time limit for the specific job (JobID: 702406).

## General Learnings
- Users may require extended time limits for certain tasks like model training.
- HPC Admins can adjust time limits for specific jobs upon user request.
- Users should provide JobID for easier administration.

## Actions Taken
- User requested an increase in time limit for their job.
- HPC Admin was contacted for assistance.

## Follow-up
- HPC Admin to confirm if the time limit can be extended and take necessary actions.
- User to be notified about the status of their request.
---

### 2021061442001577_beast%20job%20Woody%20%28gwpa003h%29.md
# Ticket 2021061442001577

 # HPC Support Ticket: Job Backlog on Woody

## Keywords
- Job backlog
- Throughput improvement
- Zoom meeting
- Workflow discussion
- Job bundling
- Kettenjobs
- Resource availability

## Problem
- User has a long backlog of jobs on Woody.

## Discussion and Solutions
- **Meeting Arrangement**: HPC Admin and user scheduled a Zoom meeting to discuss job needs and improve throughput.
- **Meeting Outcomes**:
  - Discussed the possibility of using "beagle" for specific calculations, but it was not suitable.
  - Clarified that there is no need for 48-hour runtime; restarts are necessary.
  - Provided guidance on Kettenjobs and suggested they should be aborted after a certain number of resubmissions.
  - Job bundling from 2 or 4 inputs was suggested as a feasible solution.
  - Mentioned TinyEth briefly.
  - User has funds from W1-Berufung, which could be used for future ECAP-Beschaffung.
- **Follow-up**: HPC Admin assured the user that they do not need to change their workflow if it is too complicated and if they are satisfied with the current throughput. Woody has plenty of unused resources available.

## User Feedback
- User found the Zoom discussion extremely useful.
- User plans to restart jobs in the next two weeks.

## Conclusion
- The meeting helped in understanding the user's job requirements and provided potential solutions to improve throughput.
- User was reassured about resource availability and given the option to continue with their current workflow if preferred.
---

### 2024091042002527_Cluster%20nicht%20erreichbar.md
# Ticket 2024091042002527

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject: Cluster nicht erreichbar

### Keywords:
- Cluster unreachable
- Webseite down
- System availability

### Root Cause:
- User reports that the HPC cluster and the associated website are currently unreachable from Fraunhofer IIS.

### What Can Be Learned:
- **System Downtime**: The HPC cluster and website are experiencing downtime, affecting external users.
- **Communication**: Users expect timely updates on system availability and restoration times.

### Solution:
- **Investigation**: HPC Admins should investigate the cause of the downtime.
- **Communication**: Provide users with an estimated time for system restoration.
- **Resolution**: Implement necessary fixes to restore cluster and website accessibility.

### Actions Taken:
- **HPC Admins**: Investigate the cause of the downtime.
- **2nd Level Support Team**: Assist in diagnosing and resolving the issue.
- **Communication**: Update users on the status and expected resolution time.

### Documentation:
- **Downtime Procedures**: Ensure there are documented procedures for handling system downtime.
- **User Communication**: Establish a protocol for communicating system status to users.
```
---

### 2016071442001503_job%20prolongation.md
# Ticket 2016071442001503

 # HPC Support Ticket: Job Prolongation

## Keywords
- Job prolongation
- Gaussian calculation
- Walltime extension
- Checkpoint restart

## Summary
- **User Issue**: User requested multiple extensions for a Gaussian calculation job due to uncertainty about successful restart and longer than expected runtime.
- **HPC Admin Actions**: Extended job runtime multiple times upon user requests.
- **Outcome**: Job was eventually killed after 149 hours but successfully restarted from the checkpoint file.

## Detailed Conversation
- **Initial Request**: User asked for a 24-hour extension for a Gaussian calculation job.
- **Subsequent Requests**: User requested additional extensions as the job was still running and approaching optimization.
- **Admin Responses**: HPC Admins extended the job runtime multiple times, noting the job's progress and remaining time.
- **Final Outcome**: Job was killed after 149 hours but successfully restarted from the checkpoint file. User confirmed the restart was successful.

## Lessons Learned
- **Job Runtime Management**: Users should be aware of the job's progress and request extensions as needed.
- **Checkpoint Restart**: Gaussian calculations can be successfully restarted from checkpoint files even if interrupted midway.
- **Admin Intervention**: HPC Admins can manually extend job runtimes based on user requests and job progress.

## Solution
- **User Action**: Monitor job progress and request extensions if needed.
- **Admin Action**: Extend job runtimes based on user requests and job status.
- **Restart Strategy**: Use checkpoint files to restart jobs if they are interrupted.

## Notes
- **Automatic Extension**: Job runtime was not automatically extended; manual intervention by HPC Admins was required.
- **User Feedback**: User confirmed that the job could be restarted from the checkpoint file, reducing the need for frequent extensions.
---

### 2024021242003919_Run%201086434%20um%2010h%20verl%C3%83%C2%A4ngern.md
# Ticket 2024021242003919

 ```markdown
# HPC Support Ticket: Extend Job Duration

## Keywords
- Job Extension
- Job ID
- User ID
- Cluster Name

## Summary
A user requested an extension of a job's runtime by 10 hours. The HPC Admin successfully extended the job but advised the user to include the cluster name in future requests.

## Root Cause
- User did not specify the cluster name in the initial request.

## Solution
- HPC Admin extended the job's runtime.
- Advised the user to include the cluster name in future requests for clarity.

## Lessons Learned
- Always include the cluster name when requesting job extensions to avoid ambiguity.
- Ensure all necessary details are provided in the initial request to expedite the support process.
```
---

### 2023091742000741_Laufzeitverl%C3%83%C2%A4ngerung%20Jobid%3D%20842678.md
# Ticket 2023091742000741

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject: Laufzeitverlängerung Jobid= 842678

### Keywords:
- Laufzeitverlängerung (runtime extension)
- Job ID
- Cluster
- Steps
- 24 Stunden (24 hours)

### Problem:
- User requested a runtime extension of 24 hours for Job ID 842678.
- Job requires an additional 400 steps to complete within the extended time.

### Root Cause:
- Insufficient initial runtime allocation for the job.

### Solution:
- HPC Admin requested the user to specify the cluster in future requests.

### General Learnings:
- Always specify the cluster when requesting runtime extensions.
- Ensure initial runtime allocations are sufficient to avoid frequent extensions.

### Notes:
- The conversation highlights the importance of providing complete information in support requests.
- Proper communication can help in efficient management of HPC resources.
```
---

### 2022112942003821_time%20limit%20Meggie.md
# Ticket 2022112942003821

 # HPC Support Ticket: Time Limit Extension on Meggie

## Keywords
- Time limit
- OpenFoam
- Meggie
- Job runtime extension
- Intermediate results
- Restart simulation

## Problem
- User running OpenFoam simulations on Meggie encounters a 24-hour time limit.
- User inquires about the possibility of extending this time limit.

## Root Cause
- The 24-hour time limit is a fixed constraint for all jobs on Meggie.

## Solution
- **Intermediate Results and Restart**: Users can save intermediate results and restart their simulations in subsequent 24-hour chunks.
- **Manual Extension**: In exceptional cases, job runtime can be extended manually by HPC Admins, but this is not a regular solution.

## General Learning
- Understanding the fixed time limit constraints on Meggie.
- Utilizing intermediate results and restarting simulations to manage long-running jobs.
- Awareness of the possibility for manual runtime extensions in exceptional cases.

## Roles Involved
- **HPC Admins**: Provide guidance on managing job time limits and manual extensions.
- **User**: Requests assistance with time limit extensions and implements suggested solutions.

## Additional Notes
- This approach can be applied to other long-running simulations on Meggie.
- Users should plan their simulations to accommodate the 24-hour limit by saving intermediate results regularly.
---

### 2021090942003141_Wall%20time%20limit%20extension.md
# Ticket 2021090942003141

 # Wall Time Limit Extension Request

## Keywords
- Wall time limit
- Slurm
- Job ID
- Time limit extension
- Atmospheric simulation

## Problem Description
A user submitted a job on the Meggie-Cluster with a job ID of 945533, which is expected to exceed the default wall time limit of 24 hours. The job involves a high-resolution atmospheric simulation that is estimated to take approximately 52 hours based on previous test runs and calculations.

## Root Cause
The job's estimated runtime exceeds the default wall time limit set by the cluster's scheduling system (Slurm).

## Solution
The user requested an extension of the wall time limit to approximately 56 hours to ensure the job can complete without interruption. The HPC Admin responded with "erledigt," indicating that the request was processed.

## General Learnings
- Users should estimate the runtime of their jobs accurately to avoid exceeding the default wall time limit.
- If a job is expected to exceed the default wall time limit, users should request an extension in advance.
- HPC Admins can adjust the wall time limit for specific jobs upon user request.

## Actions Taken
- The user submitted a request for a wall time limit extension.
- The HPC Admin processed the request and extended the wall time limit for the specified job.

## Follow-up
No further action is required from the user or the HPC Admin for this specific request. However, users should continue to monitor their job's progress and notify the HPC support team if any issues arise.
---

### 2023082342000768_Re%3A%20%5BEXT%5D%20%5BNHR%40FAU%5D%20Scheduled%20downtime%20of%20Fritz%20on%20Wednesday%2C%20August.md
# Ticket 2023082342000768

 ```markdown
# HPC Support Ticket Conversation Analysis

## Subject: Re: [EXT] [NHR@FAU] Scheduled downtime of Fritz on Wednesday, August 30 (Out of office)

### Keywords:
- Scheduled downtime
- Fritz cluster
- Slurm update
- Job submission impact
- Out of office

### Summary:
- **Notification**: HPC Admins informed users about a scheduled downtime for the Fritz cluster on August 30, starting at 9:00.
- **Reason**: Update and reconfiguration of Slurm.
- **Impact**: Job submission might be impacted; jobs colliding with downtime will be postponed.
- **User Response**: User acknowledged the email and mentioned being out of office until October 2nd.

### Lessons Learned:
- **Communication**: Importance of notifying users about scheduled downtimes.
- **Impact Management**: Postponing jobs to avoid conflicts during downtime.
- **User Availability**: Users may be out of office, affecting response times.

### Root Cause:
- Scheduled maintenance for Slurm update and reconfiguration.

### Solution:
- Inform users in advance about scheduled downtimes.
- Ensure jobs are managed to avoid conflicts during maintenance.
- Be aware of user availability and plan communications accordingly.
```
---

### 2017062642001491_Bitte%20um%20Jobverl%C3%83%C2%A4ngerung.md
# Ticket 2017062642001491

 # HPC Support Ticket: Job Runtime Extension

## Keywords
- Job runtime extension
- TinyFat cluster
- Job ID
- HPC support

## Summary
A user requested an extension of the runtime for their job on the TinyFat cluster. The HPC Admin successfully extended the runtime.

## Problem
- User requested an extension of the runtime for job ID 97081 on the TinyFat cluster to 10 days.
- User later requested an extension for another job ID 97239.

## Solution
- HPC Admin extended the runtime for job ID 97081.
- HPC Admin extended the runtime for job ID 97239.

## Lessons Learned
- Users may request runtime extensions for their jobs.
- HPC Admins can extend the runtime of jobs upon user request.
- Communication between users and HPC support is essential for managing job requirements.

## Actions Taken
- HPC Admin extended the runtime for the specified job IDs.
- The ticket was closed after the requests were fulfilled.

## Notes
- Ensure that job runtime extensions are handled promptly to meet user needs.
- Maintain clear communication with users regarding job management and extensions.
---

### 2024071942001168_Anforderungsschreiben%20Radar%20Pose%20Estimation%20Projekt.md
# Ticket 2024071942001168

 # HPC Support Ticket Conversation Summary

## Keywords
- Data Transfer
- GPU Performance
- Job Time Limit
- Data Format Conversion
- Checkpoint-Restart

## General Learnings
- Users may encounter issues with data transfer and job time limits when working with large datasets.
- Converting data formats can help optimize data transfer and loading times.
- Checkpoint-Restart functionality can be used to manage long-running jobs.
- HPC Admins can provide guidance on optimizing data handling and job management.

## Root Cause of the Problem
- The user encountered issues with data transfer and job time limits while working on a large dataset for a deep learning project.

## Solution
- The user was advised to convert their data format to HDF5 or msgpack to optimize data transfer and loading times.
- The user was informed about the possibility of extending job time limits in exceptional cases, but was advised to use Checkpoint-Restart functionality for long-running jobs.

## Conversation Summary
- The user initially reported issues with data transfer and job time limits.
- HPC Admins provided guidance on optimizing data handling and job management.
- The user was advised to convert their data format to HDF5 or msgpack.
- The user was informed about the possibility of extending job time limits in exceptional cases, but was advised to use Checkpoint-Restart functionality for long-running jobs.
- The user reported that they had found a solution to their problem, but still needed to address the job time limit issue.
- HPC Admins confirmed that they could extend the job time limit in exceptional cases, but advised the user to use Checkpoint-Restart functionality for long-running jobs.
---

### 2022122242000834_RE%3A%20Long%20running%20process%20on%20host%20fritz4.md
# Ticket 2022122242000834

 ```markdown
# HPC Support Ticket: Long Running Process on Host fritz4

## Keywords
- Long running process
- Frontend usage
- Batch job submission
- VSCode
- Process management

## Summary
A user was notified about a long-running process on the host `fritz4`. The process was identified as a leftover from VSCode with the name `node`.

## Root Cause
- The user inadvertently left a process running on the frontend, which is intended for compiling and submitting jobs, not for running long processes.

## Solution
- The user was advised to check for any leftover processes after using VSCode and to submit batch jobs for processes requiring more than 30 minutes of CPU time.

## Lessons Learned
- Frontends should not be used for long-running processes.
- Always check for leftover processes after using development tools like VSCode.
- Submit batch jobs for CPU-intensive tasks to avoid overloading the frontend.

## Actions Taken
- The user acknowledged the issue and committed to being more careful in the future.

## Recommendations
- Regularly monitor frontend usage to identify and address long-running processes.
- Educate users on proper process management and the importance of submitting batch jobs for long-running tasks.
```
---

### 42157996_Fwd%3A%20PBS%20JOB%20304201.pollux.rrze.uni-erlangen.de.md
# Ticket 42157996

 ```markdown
# HPC Support Ticket: Job Extension Request

## Keywords
- Job Extension
- PBS Job
- Testcluster
- Job Verlängerung
- RRZE
- OTRS

## Summary
A user requested a job extension for a specific PBS job on the test cluster. The job consists of nine sub-jobs, each requiring approximately 6 days to complete. The user requested an extension to 7 days.

## Root Cause
- User required additional time to complete a long-running job.

## Solution
- The request was handled by an HPC Admin outside of the OTRS system and marked as completed.

## Lessons Learned
- Users may require job extensions for long-running tasks.
- HPC Admins can handle such requests outside of the OTRS system.
- Proper communication and documentation are essential for tracking job extensions.
```
---

### 2021101242001518_Wall%20time%20limit%20extension.md
# Ticket 2021101242001518

 # HPC Support Ticket: Wall Time Limit Extension

## Keywords
- Wall time limit
- Job ID
- Time extension
- Atmospheric simulation

## Problem
- User requested an extension of the wall time limit for a specific job (ID 958154) from the current limit to 180 hours (7.5 days).

## Solution
- HPC Admin extended the wall time limit for the job as requested.

## General Learnings
- Users can request extensions for wall time limits for their jobs.
- HPC Admins have the authority to modify job parameters such as wall time limits.
- Proper communication and request details (e.g., job ID, desired time limit) are essential for efficient support.

## Root Cause
- The user needed additional time to complete a high-resolution atmospheric simulation.

## Actions Taken
- HPC Admin acknowledged the request and extended the wall time limit to 180 hours.

## Notes
- Ensure that users provide all necessary details when requesting modifications to job parameters.
- HPC Admins should verify the feasibility of the requested changes before making modifications.
---

### 2019100842003145_HPC%2024h%20Zeitbegrenzung.md
# Ticket 2019100842003145

 # HPC Support Ticket: Job Time Limitation

## Keywords
- Job time limitation
- CFD simulations
- HPC server
- Zeitbegrenzung
- Star CCM+
- Batch job
- Zwischenergebnis

## Problem Description
- User is running CFD simulations on the HPC server that require more than 24 hours.
- The initial computation time estimate was insufficient due to the complexity of the simulations (multi-phase flow, transient).

## Root Cause
- The current job time limitation on the HPC server is set to 24 hours, which is insufficient for the user's simulations.

## Requested Solution
- Increase the job time limit to 72-96 hours.
- Alternatively, provide a script to save the last completed time step and restart the job with the intermediate result.

## Potential Solutions
- **Increase Job Time Limit**: HPC Admins can consider increasing the time limit for specific jobs or users if resources allow.
- **Job Checkpointing and Restart**: Provide a pre-made script for saving the simulation state and restarting the job, specifically for Star CCM+.

## Action Items
- HPC Admins to evaluate the feasibility of increasing the job time limit.
- 2nd Level Support team to check if there are existing scripts for job checkpointing and restarting in Star CCM+.

## General Learning
- Understanding the need for longer job time limits for complex simulations.
- Importance of job checkpointing and restarting for long-running simulations.
- Handling user requests for resource adjustments based on evolving computational needs.
---

### 2017061342002399_hpc%20-%20batch%20system%20-%20wall%20time%20-%20copy%20data.md
# Ticket 2017061342002399

 # HPC Support Ticket: Batch System - Wall Time - Copy Data

## Keywords
- Wall time
- Data copy
- Job termination
- Batch system
- Time limit
- Scripting

## Problem
- User inquired about the functionality of staging out results in the Woodcrest cluster documentation.
- User needed a reliable method to copy data before the job is terminated by the batch system.

## Root Cause
- The staging out results feature mentioned in the documentation was likely not functional.
- User needed a method to ensure data is copied before the job is killed by the batch system.

## Solution
- **Self-termination Script**: Implement a script to calculate the job's wall time and terminate the job slightly before the batch system does.
  - Example: Set a time limit of 23.5 hours for a 24-hour job to allow time for data copying.
- **Software Configuration**: If the software supports a time limit, configure it directly.
- **Custom Script**: If the software does not support a time limit but has a termination command, create a custom script to handle this.
  - Reference: [Stopping Star-CD at latest just before the wallclock time is exceeded](https://blogs.fau.de/zeiser/2008/05/07/stopping-star-cd-at-latest-just-before-the-wallclock-time-is-exceeded/)

## Additional Information
- User implemented a time query to terminate the program if necessary.
- User noticed jobs named "random_move_new" in the job list and inquired about their origin.

## General Learning
- Always verify the functionality of documented features.
- Implementing self-termination scripts can prevent data loss due to batch system termination.
- Custom scripts can be created to handle software-specific termination commands.

## Follow-up
- Investigate the origin of "random_move_new" jobs appearing in the job list.

---

This documentation provides a summary of the support ticket conversation and offers solutions for similar issues in the future.
---

### 2024032042001467_Fw%3A%20%5BNHR%40FAU%5D%20Scheduled%20downtime%20of%20HPC%20systems%20on%20March%2011%20and%2020.md
# Ticket 2024032042001467

 # HPC Support Ticket Analysis

## Subject
Fw: [NHR@FAU] Scheduled downtime of HPC systems on March 11 and 20

## Keywords
- Scheduled downtime
- HPC systems
- Alex cluster
- TinyX cluster
- GPU availability
- Maintenance

## Summary
The user reported issues with accessing the Alex and TinyX clusters during a scheduled downtime. The HPC Admins provided updates on the expected resolution time and the status of the maintenance work.

## Root Cause
- Scheduled downtime for general maintenance work on March 20, affecting all clusters including frontends and fileservers.
- Maintenance work included central fileservers and network infrastructure.

## User Issues
- Inability to access Alex and TinyX clusters.
- No GPU available or can be allocated after initial access was restored.

## HPC Admin Responses
- Confirmed the scheduled downtime and expected resolution time.
- Informed the user that the maintenance was not yet finished and would take a few more hours.
- Advised the user to check the MOTD (Message of the Day) on the TinyX frontend for updates.

## Solution
- Wait for the completion of the maintenance work.
- Check the MOTD for updates on the maintenance status.

## General Learnings
- Scheduled downtimes can affect the availability of HPC systems and resources.
- Maintenance work on central fileservers and network infrastructure can cause extended downtimes.
- Users should be informed about the expected duration of downtimes and the impact on their jobs.
- The MOTD can be used to provide updates on the maintenance status.
- GPU availability may be affected even after initial access to the clusters is restored.
---

### 2024032142000779_Regarding%20the%20maintenance.md
# Ticket 2024032142000779

 ```markdown
# HPC Support Ticket Conversation: Maintenance Status

## Keywords
- Maintenance
- Node reservation
- Error: ReqNodenotAvail
- MOTD (Message of the Day)
- Cluster frontend

## Summary
- **User Issue**: User is encountering an error indicating that the node is reserved for maintenance (ReqNodenotAvail).
- **Root Cause**: Ongoing maintenance on the HPC cluster.
- **Solution**: Wait for the maintenance to be completed. The HPC Admins will update the MOTD when there is any news.

## Lessons Learned
- **Maintenance Communication**: HPC Admins should regularly update the MOTD to inform users about the status of maintenance.
- **Patience**: Users should be patient during maintenance periods and check the MOTD for updates.
- **Error Handling**: The error ReqNodenotAvail indicates that the node is reserved for maintenance, and users should not attempt to use it until the maintenance is over.

## Action Items
- **HPC Admins**: Ensure timely updates to the MOTD regarding maintenance status.
- **Users**: Check the MOTD for updates and avoid using nodes reserved for maintenance.
```
---

### 2025012942004137_Job%20wall%20time%20extension.md
# Ticket 2025012942004137

 ```markdown
# HPC Support Ticket: Job Wall Time Extension

## Keywords
- Job wall time extension
- Queue times
- SHM issues
- Data loading phase
- Full capacity operation

## Summary
A user requested an extension of the wall time for a job due to long queue times and issues with the initial data loading phase caused by SHM problems.

## Root Cause
- Long queue times on the cluster.
- Increased initial data loading phase due to SHM issues.

## Solution
- The HPC Admin extended the wall time of the job to 48 hours.

## General Learnings
- Delays between job submission and start are intended to ensure the cluster operates close to full capacity.
- Extending the wall time can be a feasible solution to accommodate unexpected delays or issues in job execution.
```
---

### 42061963_L%C3%83%C2%A4ngere%20Rechnung.md
# Ticket 42061963

 ```markdown
# HPC Support Ticket: Extended Job Runtime

## Keywords
- Job runtime extension
- CFX transient calculations
- qsub command
- JobID
- Manual runtime adjustment

## Problem
- User needs to run transient calculations with CFX that require approximately 48 hours.
- Concern about the cluster terminating the job before completion.

## Solution
1. **Job Submission**:
   - User should submit the job with `qsub -h` command, initially setting the runtime to 24 hours.
   - This command will display the job as "H" instead of "Q" in the status.

2. **Manual Runtime Adjustment**:
   - User should provide the JobID to the HPC Admin.
   - HPC Admin will manually extend the runtime to 48 hours and release the job.

3. **Job Script Adjustment**:
   - Ensure that the job script does not have a hardcoded stop time (e.g., `STOPSECS='85800'`).

## Example Conversation
- **User**: Requests extended runtime for CFX calculations.
- **HPC Admin**: Provides instructions for job submission and manual runtime adjustment.
- **User**: Submits job and provides JobID.
- **HPC Admin**: Confirms runtime adjustment and job execution.

## Notes
- The job script should not have hardcoded stop times that conflict with the extended runtime.
- Manual intervention by HPC Admin is required to extend the runtime beyond the initial setting.
```
---

### 2018061342000639_Zugang%20special%20queue%20HPC%20cluster.md
# Ticket 2018061342000639

 # HPC Support Ticket: Access to Special Queue

## Keywords
- Special Queue
- Job Submission
- Manual Runtime Extension
- Maintenance Notice
- OpenMP Parallelization

## Summary
A user requested access to the "special" queue for long-running simulations due to an upcoming conference. The HPC admin provided instructions for job submission and manual runtime extension, with a notice about upcoming maintenance.

## Root Cause
- User needed extended runtime for simulations due to a short deadline before a conference.

## Solution
- Submit jobs with a runtime of <=24 hours.
- Send job IDs to the HPC admin for manual runtime extension.
- Be aware of potential disruptions due to scheduled maintenance on the cooling system.

## General Learnings
- Users can request manual runtime extensions for jobs by submitting them with a shorter runtime and providing the job IDs to the HPC admin.
- Maintenance notices should be considered when planning long-running jobs.
- OpenMP parallelization is used for the simulations in this case.

## Ticket Conversation
- **User**: Requested access to the "special" queue for long-running simulations.
- **HPC Admin**: Instructed the user to submit jobs with <=24 hours runtime and send the job IDs for manual extension. Notified about upcoming maintenance.
- **User**: Submitted jobs and provided job IDs for runtime extension.

## Follow-up
- HPC admin to manually extend the runtime for the provided job IDs.
- User to monitor jobs and be prepared for potential maintenance disruptions.
---

### 2022122142001102_Verl%C3%83%C2%A4ngerung%20des%20Runtime%20Limits%20auf%20Alex.md
# Ticket 2022122142001102

 # HPC Support Ticket: Runtime Limit Extension Request

## Keywords
- Runtime limit
- Job extension
- Alex cluster
- HPC account
- Training times
- Network models

## Summary
A user requested an extension of the runtime limit for jobs on the Alex cluster due to long training times for their network models.

## Root Cause
- User requires longer runtime for jobs due to extensive training times for network models.

## Solution
- **Manual Extension**: HPC Admins can manually extend the runtime for individual jobs upon request via email with the JobID.
- **No Permanent Extension**: There is no partition or QOS with a longer runtime limit available on the Alex cluster.

## General Learnings
- Runtime limits for jobs can be extended on a case-by-case basis by contacting HPC Admins.
- There is no general partition or QOS with extended runtime limits on the Alex cluster.

## Action Items
- Users should email HPC Admins with the JobID for runtime extension requests.
- HPC Admins will manually extend the runtime for approved requests.

## Related Roles
- **HPC Admins**: Responsible for manual job runtime extensions.
- **Users**: Request runtime extensions via email with JobID.

## Additional Notes
- The user's HPC account was mentioned as "b143dc10".
- The request was handled by an HPC Admin (Thomas Zeiser).
---

### 2025031042001475_Tier3-Access-Alex%20%22Jan%20Geier%22%20_%20iwi5213h.md
# Ticket 2025031042001475

 # HPC Support Ticket Conversation Analysis

## Keywords
- HPC Cluster Access
- Walltime Limit
- Checkpoint-Restart
- Dataset Management
- Workspace Access
- GPU Resources

## General Learnings
- **Cluster Walltime Limit**: All clusters have a walltime limit of 24 hours.
- **Checkpoint-Restart**: Users should ensure their code supports checkpoint-restart to fit into multiple 24-hour jobs.
- **Dataset Management**: Large datasets should be managed efficiently to avoid duplication.
- **Workspace Access**: Workspaces may be accessible only on specific clusters.
- **Resource Allocation**: Justification for using high-performance resources should be clear.

## Root Cause of the Problem
- User requested access to a high-performance cluster (Alex) for a new project with a large dataset.
- Concerns about walltime limits and dataset management across different clusters.

## Solution
- **Access Granted**: User was granted access to the Alex cluster after clarifying the need for different code and the benefits of using the cluster's resources.
- **Dataset Management**: Suggested using a shared directory to avoid data duplication and facilitate access on other clusters.

## Documentation for Support Employees
- **Walltime Limit**: Ensure users are aware of the 24-hour walltime limit and the need for checkpoint-restart capabilities.
- **Dataset Management**: Advise users on efficient dataset management to avoid duplication and facilitate access across clusters.
- **Resource Justification**: Ensure users provide clear justification for requesting high-performance resources.

This documentation can be used to address similar issues in the future, ensuring efficient resource allocation and user support.
---

### 42436313_urgent%20job%20on%20emmy.md
# Ticket 42436313

 # HPC Support Ticket: Urgent Job on Emmy

## Keywords
- Job priority
- Runtime extension
- nMOLDYN calculation
- Deadline
- Single node job

## Summary
A user requested higher priority for two jobs (398497 and 398499) due to an impending paper deadline. Additionally, the user asked for a runtime extension for job 398499 from 24 hours to 48 hours.

## Root Cause
- The user needed to complete simulations for a paper deadline.
- The jobs were time-sensitive and could not be restarted.

## Solution
- HPC Admin granted higher priority to the specified jobs.
- The runtime for job 398499 was extended to 48 hours.

## General Learnings
- Users may require priority adjustments for time-sensitive tasks.
- Runtime extensions can be granted for jobs that cannot be restarted.
- Communication with users about job requirements and deadlines is crucial.

## Actions Taken
- HPC Admin adjusted the priority of jobs 398497 and 398499.
- HPC Admin extended the runtime of job 398499 to 48 hours.
- The user was informed that their request was fulfilled.

## Follow-Up
- Ensure that the user's jobs complete successfully within the extended runtime.
- Monitor similar requests to maintain fair usage of HPC resources.
---

### 2023022742001805_Short%20Running%20Jobs%20%28b147dc10%29.md
# Ticket 2023022742001805

 # Short Running Jobs

## Keywords
- Short running jobs
- Job monitoring
- Parameter optimization
- Integrator optimization

## Summary
- **Issue**: HPC Admins noticed a user running only short jobs.
- **Root Cause**: User was running tests to optimize parameters and integrators.
- **Solution**: No action required from HPC Admins as the short jobs were intentional.

## What Can Be Learned
- Short running jobs may not necessarily indicate an issue; users might be conducting tests.
- Always confirm with the user before taking any action based on job duration.
- Expect longer jobs after users complete their testing phase.
---

### 2023040642001672_Walltime%20Tinyfat.md
# Ticket 2023040642001672

 # HPC Support Ticket: Walltime Extension for Tinyfat-Long Cluster

## Keywords
- Walltime extension
- Tinyfat-Long cluster
- Orca 5.0.4
- Analytical frequencies
- Job IDs: 314327, 314328

## Problem
- User submitted two jobs (IDs: 314327 and 314328) on the Tinyfat-Long cluster.
- The initial walltime of 60 hours was insufficient for the calculations of analytical frequencies using Orca 5.0.4.
- Jobs cannot be restarted due to the nature of the calculations.

## Solution
- HPC Admin extended the walltime for both jobs.
  - Job ID 314327: Extended to 100-120 hours.
  - Job ID 314328: Extended to 120-150 hours.

## General Learning
- Users may request walltime extensions for jobs that require longer computation times.
- HPC Admins can adjust walltime settings for jobs as needed.
- Some computational tasks, such as analytical frequency calculations with Orca, cannot be restarted and require continuous runtime.

## Root Cause
- Insufficient initial walltime allocation for the computational tasks.

## Action Taken
- HPC Admin extended the walltime for the specified jobs to accommodate the longer computation times.
---

### 2022090642004313_Re%3A%20Long%20running%20process%20on%20host%20woody3.md
# Ticket 2022090642004313

 # HPC Support Ticket: Long Running Process on Host

## Keywords
- Long running process
- Frontend usage
- CPUTIME exceeded
- Batch job submission
- Interactive batch jobs
- VS Code SSH connection
- Python notebook

## Problem
- User was running long numerical experiments using a Python notebook (.ipynb) via VS Code SSH connection on the frontend host.
- The process exceeded the allowed CPUTIME and was automatically killed.

## Root Cause
- The frontend host is not intended for running long computational tasks.
- The user's process ran for over an hour, violating the policy for frontend usage.

## Solution
- Users should submit batch jobs for processes requiring more than 30 minutes of CPU time.
- For interactive work, users can submit interactive batch jobs using the `-I` and `-X` parameters with `qsub`.

## General Learning
- Frontends are meant for compiling, submitting jobs, and short tasks, not for long-running processes.
- Long-running processes should be submitted as batch jobs to avoid disturbing other users.
- Interactive batch jobs are available for tasks requiring user interaction.

## HPC Admin Action
- The ticket was closed as no further action was required from the HPC team's side.
---

### 2022022242002941_RE%3A%20Long%20running%20process%20on%20host%20emmy2.md
# Ticket 2022022242002941

 # HPC Support Ticket: Long Running Process on Host

## Keywords
- Long running process
- Frontend usage
- Batch jobs
- Interactive batch jobs
- Kill process
- Terminal connection lost

## Problem
- User's process was automatically killed due to long runtime on the frontend node.
- User's terminal connection was lost while the process was running.

## Root Cause
- User ran a long process on the frontend node, which is not intended for such tasks.
- User's process exceeded the allowed time limit of one hour.

## Solution
- **Kill Process**: Use the `kill` command to terminate processes manually.
- **Batch Jobs**: Submit long processes as batch jobs to get a dedicated node.
  - Interactive batch jobs can be submitted using `qsub` with parameters `-I` and `-X`.
- **Avoid Long Processes on Frontend**: Use frontend nodes only for compiling, submitting jobs, and short tasks.

## General Learnings
- Frontend nodes have time limits for processes (30 minutes for renice, 1 hour for automatic kill).
- Always use batch jobs for long processes to avoid disturbing other users.
- Interactive batch jobs are available for interactive work.
- Users can manually kill processes using the `kill` command.

## Related Commands
- `kill`: Terminate a process manually.
- `qsub -I -X`: Submit an interactive batch job.

## Related Policies
- Frontend nodes are not for long-running jobs.
- Processes exceeding time limits will be automatically killed.
---

### 2021091842000878_Wall%20time%20limit%20extension.md
# Ticket 2021091842000878

 ```markdown
# HPC-Support Ticket Conversation: Wall Time Limit Extension

## Keywords
- Wall time limit
- Job ID
- Atmospheric simulation
- Time extension

## Summary
A user requested an extension of the wall time limit for two specific jobs:
- Job ID 948698: Extension to 180 hours (7.5 days)
- Job ID 949081: Extension to 54 hours

## Root Cause
The user needed additional time for high-resolution atmospheric simulations that required extended computation time.

## Solution
The HPC Admin extended the wall time limits for the specified jobs as requested by the user.

## General Learnings
- Users may require extended wall time limits for complex simulations.
- HPC Admins can adjust wall time limits upon user request.
- Proper communication and documentation of job extensions are essential for efficient support.
```
---

### 2023090642002724_Job%20Verl%C3%83%C2%A4ngerung.md
# Ticket 2023090642002724

 ```markdown
# HPC-Support Ticket: Job Verlängerung

## Keywords
- Walltime
- Job Extension
- Job ID

## Problem
- User requested an extension of the walltime for their job.

## Details
- **Job ID:** 827395
- **Requested Walltime:** 3 days

## Solution
- HPC Admin extended the walltime for the specified job.

## Lessons Learned
- Users can request extensions for job walltime.
- HPC Admins can modify job parameters such as walltime upon user request.

## Actions Taken
- HPC Admin acknowledged and completed the walltime extension request.
```
---

### 2017020942001101_LIMA%3A%20route%20queue.md
# Ticket 2017020942001101

 ```markdown
# HPC-Support Ticket: LIMA Route Queue Issue

## Subject
LIMA: route queue

## User Issue
- User reported that the ROUTE queue was not accepting jobs longer than one hour.
- User initially suspected a segmentation error in their program.

## HPC Admin Response
- HPC Admin was unable to reproduce the issue using their own credentials or the user's credentials.
- Admin noted that other jobs longer than one hour were successfully submitted to the queue.

## Detailed Analysis
- Admin provided job details showing that a job submitted by the user was queued and started but terminated after 2 seconds.
- The job log indicated an exit status of 1 and minimal resource usage.

## User Clarification
- User clarified that the job was queued but terminated shortly after starting.
- The job log showed a normal prologue but an abrupt termination without clear error messages.

## Root Cause
- The root cause of the job termination was not explicitly identified in the conversation.
- Possible issues could include resource allocation problems, job script errors, or system-level issues not reproducible by the admin.

## Solution
- No explicit solution was provided in the conversation.
- Further investigation into job script and system logs would be necessary to identify and resolve the issue.

## Keywords
- ROUTE queue
- Job termination
- Segmentation error
- Job script
- Resource allocation

## General Learning
- Always check job logs for detailed error messages.
- Ensure job scripts are correctly configured for resource allocation.
- Reproduce issues using different user credentials to isolate user-specific problems.
```
---

### 2025011042001004_Helma%20Job.md
# Ticket 2025011042001004

 ```markdown
# HPC Support Ticket: Helma Job Extension

## Keywords
- Job Extension
- Helma
- Training
- Job ID 5540
- Runtime Extension

## Summary
A user requested an extension for their job on Helma with the ID 5540 until the end of January. The HPC Admin extended the job's runtime by 20 days.

## Problem
- User requested an extension for their job due to training continuation.

## Solution
- HPC Admin extended the job's runtime by 20 days.

## Lessons Learned
- Users can request job extensions for ongoing training.
- HPC Admins can extend job runtimes as per user requests.
- Clear communication between users and HPC Admins is essential for managing job extensions.
```
---

### 2016052342002365_LIMA%3A%20devel%20queue.md
# Ticket 2016052342002365

 # HPC-Support Ticket: LIMA devel Queue Delay

## Keywords
- LIMA
- devel queue
- Job delay
- qstat
- Wartezeit

## Summary
A user submitted a job to the devel queue on LIMA at 7:30 AM, but the job had not started running by 12:44 PM. The user found the 5-hour wait time excessive for the development queue.

## Root Cause
- Potential issues with the devel queue on LIMA.
- Possible high load or job scheduling problems.

## Diagnostic Steps
- The user provided a `qstat` output showing the job ID, username, queue, job name, and job status.
- Job ID: 1847630.ladm1
- Username: gwgi17
- Queue: devel
- Jobname: LIMA_unter_v500
- Status: Q (queued)

## Solution
- HPC Admins should investigate the devel queue for any scheduling issues or high load.
- Check the job scheduler logs for any errors or delays.
- Consider increasing the priority or resources for the devel queue if it is consistently experiencing long wait times.

## General Learnings
- Long wait times in the devel queue can indicate scheduling issues or high load.
- Users should be informed about expected wait times and queue status.
- Regular monitoring of queue performance is essential to ensure efficient job processing.

## Next Steps
- HPC Admins to review the devel queue status and job scheduler logs.
- Communicate the findings and any necessary actions to the user.
- Consider implementing queue performance monitoring and alerts.
---

### 2024062442000811_Running%20longer%20jobs.md
# Ticket 2024062442000811

 # HPC-Support Ticket Conversation Summary

## Subject: Running longer jobs

### Keywords:
- Job walltime extension
- `--ntasks` vs `--cpus-per-task`
- Memory allocation

### Root Cause of the Problem:
- User seeking information on running jobs longer than 24 hours.
- Confusion between `--ntasks` and `--cpus-per-task` settings.

### Solution:
- **Job Walltime Extension:**
  - Not documented on the NHR@FAU website.
  - Extend walltime by submitting jobs with `--hold` and requesting an extension from HPC support with job IDs.

- **Difference between `--ntasks` and `--cpus-per-task`:**
  - `--ntasks`: Number of tasks (useful for MPI jobs).
  - `--cpus-per-task`: Number of CPUs per task (useful for OpenMP jobs).
  - Memory allocation: 7.75 GB per core.
  - Total cores allocated: `ntasks * cpus-per-task`.

### Example Job Scripts:
- Refer to [Woody Cluster Documentation](https://doc.nhr.fau.de/clusters/woody/) for example job scripts.

### General Learning:
- Understanding the difference between `--ntasks` and `--cpus-per-task` is crucial for optimizing resource allocation.
- Extending job walltime requires manual intervention and approval from HPC support.

### Conclusion:
- The user was provided with the necessary information to extend job walltime and clarify the difference between `--ntasks` and `--cpus-per-task`.
- The user expressed gratitude for the quick and helpful response.
---

### 2023051742001935_Meggie%20Jobs%20%C3%83%C2%BCber%2024h%20Ausnahme.md
# Ticket 2023051742001935

 # HPC Support Ticket: Extended Job Runtime Exception

## Keywords
- Job runtime extension
- Scheduler
- Sicherheitspatch
- Reboot
- Automatic chained jobs

## Problem
- User requested an exception to extend the runtime of their pending jobs beyond the usual 24-hour limit due to a two-week vacation.
- Jobs required one node and one CPU each.

## Solution
- HPC Admin extended the runtime of the user's jobs as an exception.
- User was informed about an upcoming security patch that would require a reboot of all compute nodes, which could interrupt the jobs.
- User was advised to contact the support team after their vacation to discuss the possibility of setting up automatic chained jobs.

## General Learnings
- Exceptions to job runtime limits can be made on a case-by-case basis.
- Upcoming maintenance tasks (e.g., security patches) should be communicated to users as they can affect job execution.
- Automatic chained jobs can be a solution for users requiring longer job runtimes.
- Users should be encouraged to contact the support team for personalized solutions.
---

### 2021032542001678_Re%3A%20Long%20running%20process%20on%20host%20emmy2.md
# Ticket 2021032542001678

 # HPC Support Ticket: Long Running Process on Frontend

## Keywords
- tmux session
- frontend usage
- process termination
- CPU time limit
- batch jobs
- interactive batch jobs

## Problem
- User's tmux session on the frontend was terminated due to exceeding CPU time limit.
- User wanted to keep tmux session active to avoid reconfiguring terminal environment repeatedly.

## Root Cause
- The frontend nodes have a policy to terminate processes running for too long to prevent resource hogging.
- The user's tmux session accumulated more than 1 hour of CPU time.

## Solution
- **HPC Admins** explained that tmux sessions should not typically accumulate much CPU time.
- Suggested using batch jobs for long-running processes, including interactive batch jobs for interactive work.
- Clarified that processes can run up to 8 hours if the login nodes are not heavily loaded.

## General Learnings
- Frontend nodes are for short tasks like compiling and submitting jobs, not for long-running processes.
- Long-running processes should be submitted as batch jobs.
- Interactive work can be done using interactive batch jobs.
- Under normal load, processes on login nodes can accumulate up to 8 hours of CPU time.

## Related Commands/Tools
- `tmux`: Terminal multiplexer
- `qsub`: Command to submit batch jobs
- `qsub -I` and `qsub -X`: Parameters for submitting interactive batch jobs

## Preventive Measures
- Users should be aware of the CPU time limits on frontend nodes.
- For long-running processes, always use batch jobs to avoid termination and ensure efficient resource usage.
---

### 2024032042001243_AW%3A%20Long%20running%20process%20on%20host%20woody4.md
# Ticket 2024032042001243

 # HPC Support Ticket: Long Running Process on Host

## Keywords
- Long running process
- Frontend usage
- Matlab
- Processchecker
- Jupyterhub
- Interactive batch jobs

## Problem Description
- User received a notification that a Matlab process was automatically killed after running for too long on the frontend.
- User was remotely connected and had Matlab open but was not actively running computations.

## Root Cause
- The Matlab process was running for over an hour on the frontend, which is not intended for long-running jobs.

## Solution
- **Immediate Action**: The process was automatically killed by the Processchecker.
- **Long-term Solution**:
  - Use Jupyterhub for interactive Matlab sessions. Documentation available [here](https://doc.nhr.fau.de/access/jupyterhub/).
  - Submit batch jobs for long-running processes to avoid disturbing other users on the frontend.
  - Consider using interactive batch jobs for interactive work.

## General Learning
- Frontends are for compiling, submitting jobs, and short tasks, not for long-running processes.
- Processes running for more than 30 minutes on the frontend will be reniced and killed after one hour.
- Jupyterhub is a suitable alternative for long-running interactive sessions.
- Always submit batch jobs for CPU-intensive or long-running tasks.
---

### 2019050742000749_Verl%C3%83%C2%A4ngerung%20Job.md
# Ticket 2019050742000749

 # HPC Support Ticket: Job Extension Request

## Keywords
- Job extension
- Performance monitoring
- Resource utilization
- Hauptspeicherbandbreite
- Rechenleistung
- Job info

## Summary
A user requested an extension for their job due to insufficient runtime. The HPC Admin granted the extension but noted poor resource utilization and performance. The user responded with an explanation and expressed interest in improving performance.

## Root Cause
- Insufficient runtime for the job (initial 24 hours, required 72 hours).
- Poor resource utilization (low memory bandwidth and computational performance).

## Solution
- The job runtime was extended to 72 hours.
- The user was provided with a link to monitor job performance: [HPC Status Job Info](https://www.hpc.rrze.uni-erlangen.de/HPC-Status/job-info.php).
- The user was advised to consider ways to improve resource utilization and performance.

## General Learnings
- Users can request job extensions if the initial runtime is insufficient.
- Performance monitoring tools can help identify inefficient resource utilization.
- Collaboration between users and HPC Admins can lead to improved job performance.
- Users should be aware of the resources their jobs are consuming and consider optimizations.
---

### 2024081342002318_A%20problem.md
# Ticket 2024081342002318

 ```markdown
# HPC Support Ticket Conversation Analysis

## Subject: A problem

### Keywords:
- sbatch
- job submission
- maintenance
- downtime

### Problem:
- User unable to submit a job using `sbatch`.

### Root Cause:
- HPC systems are currently under maintenance.

### Solution:
- Wait for the maintenance to be completed.
- Check the status of ongoing maintenance at the provided link.

### General Learnings:
- Always check for scheduled maintenance before reporting job submission issues.
- Maintenance notifications and status updates are available on the HPC website.

### Relevant Links:
- [Scheduled Downtime of NHR@FAU HPC Systems August 13-15](https://hpc.fau.de/2024/08/06/scheduled-downtime-of-nhrfau-hpc-systems-august-13-15/)
```
---

### 2021051742002723_walltime.md
# Ticket 2021051742002723

 1. **What is the problem?**

The user is trying to run a job with a walltime longer than the standard walltime. The user has already been informed that this is not possible and that the walltime cannot be extended. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted if it fails due to walltime. The user has also been informed that the job can be restarted
---

### 2022101842004351_Not%20Able%20to%20submit%20jobs.md
# Ticket 2022101842004351

 # HPC Support Ticket: Not Able to Submit Jobs

## Keywords
- Job submission failure
- Node unavailability
- Maintenance downtime
- Runtime selection

## Problem Description
- User unable to submit jobs to HPC clusters (Alex a40, a100, and Woody).
- Error message: "ReqNodeNotAvailReserved for maintenance".
- Downtime was expected on 19 Oct, but issues persisted beyond that date.

## Root Cause
- Upcoming maintenance downtime scheduled to start the next day.
- Jobs colliding with the downtime were not being started and were postponed.

## Solution
- Select an appropriate runtime for the job to ensure it finishes before the downtime.
- Jobs that cannot complete before the downtime will not start until after the maintenance period.

## General Learnings
- Maintenance downtimes can affect job scheduling.
- Ensure job runtime is set to complete before scheduled downtimes.
- Check for any upcoming maintenance schedules when experiencing job submission issues.

## Next Steps for Support
- Inform users about upcoming maintenance schedules.
- Provide guidance on setting appropriate job runtimes to avoid conflicts with downtimes.
- Monitor job queues and node availability during and after maintenance periods.
---

### 2024081242002758_about%20scheduled%20downtime.md
# Ticket 2024081242002758

 # HPC Support Ticket: Scheduled Downtime Impact on Job Submission

## Keywords
- Scheduled downtime
- Slurm task
- ReqNodeNotAvail
- Reserved for maintenance
- Job postponement

## Problem Description
- **User Issue:** Unable to submit a Slurm task due to `ReqNodeNotAvail, Reserved for maintenance` error.
- **Context:** Scheduled downtime is approaching (starting the next day), but the user is trying to submit a job on the current day.

## Root Cause
- The job would collide with the scheduled downtime, which is less than 24 hours away.

## Solution
- **HPC Admin Response:** Jobs that would collide with the downtime will be postponed until the downtime is over. The job cannot finish in time and will start afterwards.
- **User Acknowledgment:** Understood the reason for the job postponement.

## General Learning
- Jobs that cannot complete before a scheduled downtime will be postponed and will start after the downtime.
- Users should be aware of upcoming downtimes and plan their job submissions accordingly.

## Ticket Status
- The ticket was closed after the user understood the reason for the job postponement.
---

### 2023041142004258_Laufzeiten%20%3E24h.md
# Ticket 2023041142004258

 # HPC Support Ticket: Extending Job Runtime Beyond 24 Hours

## Keywords
- Machine Learning Models
- Job Runtime
- Checkpoint-Restart
- Exceptional Runtime Extension

## Problem
- User requires job runtime longer than the maximum allowed 24 hours for training machine learning models.

## Solution
- **General Recommendation**: Use Checkpoint-Restart to keep individual jobs under 24 hours.
- **Exceptional Cases**: HPC Admins can extend the runtime of specific jobs upon request via email, provided it does not disrupt operations.

## Action Taken
- HPC Admin advised the user to use Checkpoint-Restart.
- Informed the user that runtime extension is possible in exceptional cases by emailing the HPC support with the job ID.

## Lessons Learned
- **Checkpoint-Restart**: Essential for long-running jobs to avoid exceeding the maximum runtime.
- **Flexibility**: HPC Admins can provide exceptions for runtime extensions if necessary for research purposes.

## Next Steps
- Users should implement Checkpoint-Restart for long-running jobs.
- If necessary, request runtime extension via email to HPC support with the job ID.

## Contact Information
- **HPC Support**: support-hpc@fau.de
- **Website**: [FAU HPC](https://hpc.fau.de/)

## Additional Notes
- Ensure to follow up with the user to confirm the implementation of Checkpoint-Restart or the need for runtime extension.
---

### 2024051342003644_Extend%20time%20limit.md
# Ticket 2024051342003644

 # HPC Support Ticket Conversation: Extend Time Limit

## Keywords
- Job extension
- Runtime limit
- HPC support
- Job ID
- Downtimes
- Overbooking

## Summary
The user requested an extension of the runtime limit for their computing jobs. The HPC support team provided instructions and extended the runtime for the specified jobs.

## Problem
The user needed to extend the runtime limit of their computing jobs to 5 days due to the frequent need to restart jobs.

## Solution
1. **Initial Request**: The user requested an extension for JOBID 1635399 to 5 days.
2. **HPC Admin Response**: The HPC admin did not find the specified job ID but found a similar one (1635388) and extended its runtime to 5 days.
3. **Future Instructions**: The user was instructed to submit future jobs with the `--hold` option to group longer-running jobs together on one node.
4. **Additional Requests**: The user later requested extensions for jobs 1636861 (2 days) and 1636863 (5 days).
5. **Final Response**: The HPC admin confirmed the extensions for the requested jobs.

## Lessons Learned
- Users should submit jobs with the `--hold` option for longer-running jobs to facilitate grouping on one node.
- The HPC support team can manually extend job runtimes upon request, subject to system constraints such as downtimes and overbooking.
- Clear communication and follow-up are essential for resolving runtime extension requests efficiently.

## Recommendations
- Users should ensure they provide the correct job IDs when requesting extensions.
- The HPC support team should continue to provide clear instructions and prompt responses to user requests.
- Regular updates on system capacity and planned downtimes can help users plan their job submissions more effectively.
---

### 2024011242001477_Run%20auf%2048%20Stunden%20Laufzeit%20verl%C3%83%C2%A4ngern.md
# Ticket 2024011242001477

 # HPC Support Ticket: Extending Job Walltime

## Keywords
- Walltime extension
- Job ID
- Cluster
- HPC Admin

## Problem
- User requests to extend the walltime of a specific job from 24 hours to 48 hours.

## Solution
- HPC Admin requests the cluster name and job ID to extend the walltime.

## General Learnings
- Users need to provide the cluster name and job ID for walltime extensions.
- HPC Admins can extend the walltime of jobs upon request.

## Root Cause
- User did not initially provide the necessary information (cluster name and job ID) for the walltime extension.

## Resolution
- User needs to supply the cluster name and job ID for the HPC Admin to extend the job's walltime.

## Next Steps
- Await user response with the required information.
- HPC Admin will extend the walltime once the information is provided.
---

### 2024110442001553_Running%20time%20extension.md
# Ticket 2024110442001553

 ```markdown
# HPC Support Ticket: Running Time Extension

## Subject
- Running time extension for multiple jobs on `alex2`.

## Keywords
- Job extension
- Walltime
- HPC support
- Job IDs
- `alex2`

## Summary
- User requested multiple extensions for job running times.
- HPC Admins extended the walltime for several jobs.
- Some jobs did not exist or were already completed.

## Conversation Highlights
- **Initial Request**: User requested an 8-hour extension for job ID `2133063`.
- **First Extension**: HPC Admin extended the walltime to 2 days.
- **Additional Requests**: User requested extensions for multiple job IDs (`2134872`, `2134922`, `2134944`, `2134996`, `2135237`, `2135349`, `2135572`, `2135575`).
- **Further Extensions**: HPC Admin extended the walltime for the requested jobs.
- **Non-existent Jobs**: Some jobs (`2138333`, `2137281`) did not exist or were already completed.
- **Final Request**: User requested an extension for job ID `2141802`, which was extended to 24 hours.

## Lessons Learned
- **Timely Requests**: Users should request extensions as early as possible to avoid job losses.
- **Support Availability**: HPC support is not available 24/7, so users should plan accordingly.
- **Job Status**: Users should check the status of their jobs to ensure they still exist before requesting extensions.

## Solution
- HPC Admins extended the walltime for the requested jobs as needed.
- Users were informed about the importance of timely requests and the availability of support.
```
---

### 2015102242001225_job%20ID%20467900%20prolongation%20on%20emmy.md
# Ticket 2015102242001225

 # HPC Support Ticket: Job Walltime Prolongation

## Keywords
- Job ID 467900
- Walltime prolongation
- nMOLDYN calculation
- Irrestartable job
- Progress rate 70%
- Emmy cluster

## Problem
- User requested a 24-hour walltime extension for job ID 467900 on the Emmy cluster.
- The job is an irrestartable nMOLDYN calculation with a progress rate of 70%.

## Solution
- HPC Admin modified the job walltime limit to 48 hours.

## General Learnings
- Users may request walltime extensions for jobs that are irrestartable and have made significant progress.
- HPC Admins can modify the walltime limit for jobs upon user request.
- Important to consider the job's progress and restartability when deciding on walltime extensions.

## Related Parties
- HPC Admins
- 2nd Level Support team
- Head of the Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support
- Software and Tools developers
---

### 2022111542000564_TinyFAT%20so%20gut%20wie%20komplett%20down.md
# Ticket 2022111542000564

 ```markdown
# HPC Support Ticket: TinyFAT Partition Down

## Keywords
- TinyFAT
- Partition
- Draining
- Kernel Update
- Network Outage
- Node Status
- Notification

## Summary
A user reported that several nodes in the "work" partition of the TinyFAT cluster were in a "draining" state and did not return to service after an expected kernel update. The HPC Admin team investigated and found that the issue was related to a network outage.

## Root Cause
- **Network Outage**: The nodes did not return to service due to a network outage that affected the TinyFAT cluster.

## Solution
- The HPC Admin team resolved the network outage, and the nodes returned to service.

## Notification
- The outage was announced on the HPC website but not via email, as it affected only a small portion of users.

## Lessons Learned
- **Communication**: Ensure that all users are aware of the preferred method for receiving notifications about system outages.
- **Monitoring**: Regularly monitor the status of nodes to quickly identify and address issues.
- **Documentation**: Keep a record of network outages and their impact on the system for future reference.

## Actions Taken
- The HPC Admin team investigated the issue and resolved the network outage.
- The user was informed about the resolution and the method for receiving notifications.

## Future Recommendations
- **Notification System**: Consider implementing a more comprehensive notification system that includes email alerts for all users.
- **User Education**: Educate users on how to check the HPC website for updates and notifications.
```
---

### 2021032642000364_Wall-time%20extension%20%28gwgi18%20on%20meggie%29.md
# Ticket 2021032642000364

 # HPC Support Ticket: Wall-time Extension

## Keywords
- Wall-time extension
- Job management
- Timestep adjustment
- HPC job configuration

## Problem
- **Root Cause**: User underestimated the wall-time required for a job after lowering the timestep.
- **Job ID**: 873241

## Solution
- **Action Taken**: HPC Admin extended the wall-time of the job to 36 hours.
- **Outcome**: User confirmed the extension and expressed gratitude.

## General Learnings
- Users may need to adjust job parameters such as wall-time based on changes in simulation settings (e.g., timestep).
- HPC Admins can manually extend wall-time for jobs upon user request.
- Effective communication between users and HPC support is crucial for timely adjustments.

## Notes
- Ensure users are aware of the process for requesting wall-time extensions.
- Document any changes made to job configurations for future reference.
---

### 2019011742001791_Frage%20Job-Laufzeit.md
# Ticket 2019011742001791

 # HPC Support Ticket: Job Runtime Issue

## Keywords
- Job runtime
- Walltime
- qstat
- CPU time
- Job monitoring

## Summary
A user noticed that a job with a specified walltime of 3 hours was reported by `qstat` to have run for over 6 hours. Upon closer inspection, it was observed that `qstat` no longer displayed the actual runtime but instead showed the CPU time.

## Root Cause
The user suspected that `qstat` was now displaying CPU time instead of the actual runtime, leading to confusion about the job's duration.

## Solution
No solution was provided in the initial conversation. Further investigation is needed to confirm if `qstat` is indeed displaying CPU time and whether this change is intentional.

## General Learning
- Understanding the difference between walltime and CPU time.
- Importance of verifying job runtime through multiple methods.
- Potential changes in monitoring tools like `qstat` and their impact on job tracking.

## Next Steps
- Confirm with HPC Admins if the change in `qstat` output is intentional.
- Provide guidance to users on how to accurately track job runtime if `qstat` is displaying CPU time.
- Update documentation to reflect any changes in monitoring tools.
---

### 42197842_job%20prolongation.md
# Ticket 42197842

 # HPC Support Ticket: Job Prolongation

## Keywords
- Job prolongation
- Time limit extension
- Running job
- Non-restartable calculation

## Summary
A user requested an extension of the time limit for a running job that could not be restarted. The job had already run for 23 hours out of its 24-hour limit and was only 40% complete.

## Root Cause
- The job's time limit was insufficient for the calculation to complete.

## Solution
- The HPC Admin extended the job's time limit by approximately 32-36 hours.

## General Learnings
- Users may request time limit extensions for running jobs.
- Some calculations cannot be restarted and require continuous runtime.
- HPC Admins can extend the time limit for running jobs upon user request.

## Related Tags
- Job management
- Time limit
- Job extension
- Non-restartable jobs
---

### 42070594_JOB%20ID%20378942%20on%20Woody.md
# Ticket 42070594

 # HPC Support Ticket: Job Extension Request

## Keywords
- Job Extension
- Job Limit
- Weekend Run
- Special Treatment
- Convergence Time

## Summary
A user requested an extension for a job (ID 378942) that had already run for 68 hours, approaching the 72-hour limit. The job was converging slower than expected and needed additional time to complete over the weekend.

## Root Cause
- The job was larger and converging slower than previous jobs.
- The user initially requested an extension to 96 hours but later realized they needed 120 hours to run over the weekend.

## Solution
- The HPC Support team extended the job limit to 96 hours initially.
- Upon the user's second request, the job limit was further extended to 120 hours to ensure completion over the weekend.

## General Learnings
- Users may miscalculate the required time for job extensions.
- It is important to consider the convergence rate of jobs when estimating runtime.
- HPC Support can extend job limits to accommodate special requests, especially for jobs nearing completion.

## Actions Taken
- Extended job limit to 96 hours.
- Further extended job limit to 120 hours upon user's request.

## Follow-up
- Ensure the job completes successfully within the extended time frame.
- Monitor similar jobs for convergence rates and adjust time limits accordingly.
---

### 2022021842001717_Extend%20runtime.md
# Ticket 2022021842001717

 # HPC Support Ticket: Extend Runtime

## Keywords
- Extend runtime
- GPU utilization
- Checkpoint-restart
- PyTorch
- Excessive IO

## Summary
A user requested to extend the runtime of a neural network training job beyond the default 24-hour limit. The HPC admins provided guidance on implementing checkpoint-restart and optimizing GPU utilization. The user was also referred to an expert for further assistance with PyTorch on GPUs. Additionally, the user's jobs were flagged for excessive IO operations.

## Root Cause
- The user's job required more than 24 hours to complete.
- Low GPU utilization (around 20%) indicated potential for performance optimization.
- The user's jobs were performing several hundred opens per minute, causing excessive IO.

## Solutions
- **Runtime Extension**: In exceptional cases, the HPC admins can manually extend the runtime of single jobs. The general procedure is to implement checkpoint-restart in the workflow and go with multiple 24-hour jobs.
- **GPU Utilization**: The user was advised to optimize their job for better GPU utilization. An expert in PyTorch on GPUs was recommended for further assistance.
- **Excessive IO**: The user was informed about the excessive IO operations performed by their jobs. The user should investigate and reduce the number of opens per minute.

## General Learnings
- Implementing checkpoint-restart is the recommended approach for jobs that require more than the default maximum runtime.
- Low GPU utilization can indicate that a job is not fully optimized for the available hardware.
- Excessive IO operations can negatively impact the performance of the job and the overall system. Users should be mindful of the IO operations performed by their jobs.
- The HPC support team can provide guidance on optimizing jobs and refer users to experts for more specialized assistance.

## Follow-up
- The ticket was closed because the user had not been computing for months, according to the HPC admin (TZ).
---

### 2018091442001391_Technical%20issue%20-%20mfhe000h.md
# Ticket 2018091442001391

 # HPC Support Ticket: Technical Issue - mfhe000h

## Summary
- **User Issue**: Deep learning training pipeline using Keras library encounters a bug when loading the model after saving it every epoch due to a 24-hour limitation.
- **Request**: Extended runtime to run the training uninterruptedly.
- **Solution**: HPC Admins extended the job runtime as requested.

## Keywords
- Deep Learning
- Keras
- Model Loading Bug
- Extended Runtime
- JobID

## Conversation Highlights

### User
- **Initial Problem**:
  - Implemented a deep learning training pipeline using Keras.
  - Due to the 24-hour limitation, the model needs to be saved and loaded every epoch.
  - The function to load the model in Keras is buggy and does not load the model correctly.
  - This issue has delayed work for one month.
  - Options considered: reimplementing the network with another library (expensive and time-consuming) or finding a computer to run the training with no interruption.

- **Request**:
  - Extended runtime to run the training uninterruptedly.
  - Willing to pay if necessary.

### HPC Admin
- **Initial Response**:
  - Asked for the number of GPUs needed and the duration for which the job needs to run.

- **Solution**:
  - Instructed the user to submit the job as usual with a 24-hour limit and provide the JobID for extension.
  - Extended the runtime to 10 days initially, then adjusted based on user feedback.

## Detailed Interactions

### User
- **Resource Requirements**:
  - Initially requested 4 or 8 cores.
  - Estimated runtime for each model training was approximately 10 days.

- **Job Submission**:
  - Submitted JobID 201453.tgadm1.rrze.uni for a 10-day extension.
  - Later requested extensions for JobIDs 202006.tgadm1.rrze.uni (120 hours), 202835.tgadm1.rrze.uni (240 hours), and 203050.tgadm1.rrze.uni (240 hours).

### HPC Admin
- **Extensions**:
  - Extended JobID 201453.tgadm1.rrze.uni to 10 days.
  - Extended JobID 202006.tgadm1.rrze.uni to 120 hours.
  - Extended JobID 202835.tgadm1.rrze.uni to 240 hours.
  - Extended JobID 203050.tgadm1.rrze.uni to 240 hours.
  - Extended JobID 205065.tgadm1.rrze.uni to 120 hours.

## Root Cause and Solution
- **Root Cause**:
  - The Keras library has a known bug that prevents the model from being loaded correctly after saving it every epoch.

- **Solution**:
  - The HPC Admins extended the job runtime to allow the training to run uninterruptedly, addressing the user's immediate need.
  - The user also mentioned implementing the code with another library (PyTorch) for future projects to avoid similar issues.

## Conclusion
- The HPC Admins successfully addressed the user's request by extending the job runtime, allowing the deep learning training to proceed without interruption.
- The user appreciated the support and mentioned optimizing future projects to avoid similar issues.
---

### 2023062142003745_Request%20for%20Longer%20Period%20for%20CPU.md
# Ticket 2023062142003745

 # HPC Support Ticket: Request for Longer Period for CPU

## Keywords
- CPU time extension
- Task automatically killed
- Data processing
- Frontend usage
- Cluster job submission

## Problem
- User needs extended CPU time to process a large dataset (70,000+ samples).
- Task is automatically killed during processing.

## Root Cause
- User is attempting to process data on the frontend node, which is not designed for extensive computations.

## Solution
- **HPC Admin** advised the user to submit jobs to one of the clusters for extended CPU time and data processing.
- Frontend nodes should not be used for heavy computations; they are intended for job submission and management.

## General Learning
- Always submit computationally intensive tasks to the cluster nodes.
- Avoid using frontend nodes for data processing to prevent task termination and ensure efficient resource usage.

## Next Steps
- If the issue persists, ensure the user is correctly submitting jobs to the cluster.
- Provide guidance on job submission scripts and resource allocation if needed.

---

This documentation aims to help support employees address similar issues efficiently.
---

### 2024041542001144_Increase%20Time%20of%20Jobs.md
# Ticket 2024041542001144

 ```markdown
# HPC Support Ticket: Increase Time of Jobs

## Keywords
- Job runtime extension
- Cluster name specification
- User request
- HPC admin response

## Summary
A user requested an increase in the runtime for a specific job. The HPC admin extended the runtime and advised the user to mention the cluster name in future requests.

## Root Cause
- User did not specify the cluster name in the initial request.

## Solution
- HPC admin extended the job runtime.
- User was advised to include the cluster name in future requests.

## Lessons Learned
- Always specify the cluster name when requesting job runtime extensions.
- Clear communication between users and HPC admins is crucial for efficient support.
```
---

### 2020050842001761_Re%3A%20Long%20running%20process%20on%20host%20emmy2.md
# Ticket 2020050842001761

 # HPC Support Ticket: Long Running Process on Host

## Keywords
- Long running process
- Frontend usage
- Key expiration
- SSHFS
- Batch jobs
- Interactive batch jobs

## Summary
A user's process on the frontend was automatically killed due to excessive runtime. The user was compressing results on `fasttemp` mounted via SSHFS and encountered issues with key expiration during file transfers.

## Root Cause
- The user was running a long process on the frontend, which is not intended for such tasks.
- The user's SSH key expired during file transfers, causing interruptions.

## Solution
- **Frontend Usage**: The frontend should be used for compiling, submitting jobs, etc., but not for running long processes.
- **Batch Jobs**: For tasks requiring more than 30 minutes of CPU time, submit a batch job.
- **Interactive Batch Jobs**: Use interactive batch jobs for interactive work (parameters `-I` and `-X` to `qsub`).
- **Key Expiration**: Address the issue of key expiration to ensure uninterrupted file transfers.

## Additional Notes
- The user was unaware that their process was consuming CPU resources on the HPC.
- The HPC Admins provided guidance on proper usage of frontend resources and batch job submission.

## Action Items
- Educate users on the appropriate use of frontend resources.
- Provide guidance on managing SSH key expiration to avoid interruptions during file transfers.
- Encourage the use of batch jobs for long-running processes.
---

### 2021060242001858_Re%3A%20Long%20running%20process%20on%20host%20woody3.md
# Ticket 2021060242001858

 # HPC Support Ticket Analysis: Long Running Process on Host

## Keywords
- Long running process
- Frontend usage
- Walltime limit
- Batch job
- Interactive batch job
- qsub
- PBS Job
- Exit_status=-11
- Script configuration
- New-user introduction

## Problem
- User ran a long-running process on the frontend (`woody3`), which was automatically killed after exceeding the allowed time limit.
- User's batch job (`test.sh`) was aborted by the PBS Server due to exceeding its walltime limit.

## Root Cause
- The user was running a computationally intensive process on the frontend, which is not intended for such tasks.
- The batch job script (`test.sh`) was not properly configured for the Torque scheduler, leading to walltime limit issues.

## Solution
- **Frontend Usage**: Educate the user about the proper use of frontends. Frontends should not be used for running jobs; they are meant for compiling, submitting jobs, etc.
- **Batch Job Submission**: Advise the user to submit batch jobs for long-running processes. This ensures dedicated resources and prevents disturbance to other users.
- **Script Configuration**: Provide the user with documentation links to properly configure the script for Torque:
  - [Batch Processing Documentation](https://hpc.fau.de/systems-services/systems-documentation-instructions/batch-processing/)
  - [TinyGPU Cluster Documentation](https://hpc.fau.de/systems-services/systems-documentation-instructions/clusters/tinygpu-cluster/)
- **Interactive Batch Jobs**: Inform the user about interactive batch jobs using the `-I` and `-X` parameters with `qsub` for interactive work.
- **New-User Introduction**: Invite the user to the new-user introduction session for further guidance.

## General Learning
- Frontends are not for running long processes; use them for job submission and compilation.
- Always submit batch jobs for long-running processes to ensure dedicated resources.
- Properly configure job scripts to avoid walltime limit issues.
- Utilize interactive batch jobs for interactive work that requires more than 30 minutes of CPU time.

## Relevant Documentation
- [Batch Processing Documentation](https://hpc.fau.de/systems-services/systems-documentation-instructions/batch-processing/)
- [TinyGPU Cluster Documentation](https://hpc.fau.de/systems-services/systems-documentation-instructions/clusters/tinygpu-cluster/)
- [HPC Café](https://hpc.fau.de/systems-services/support/hpc-cafe/)
---

### 42193341_Job%20848052%20auf%20LiMa.md
# Ticket 42193341

 # HPC Support Ticket Analysis

## Subject: Job 848052 auf LiMa

### Keywords
- Job ID: 848052
- System: LiMa
- Issue: Job termination
- Monitoring data

### Summary
- **User Issue**: Job 848052 on LiMa stopped "ordentliche" (proper) computing after a short time.
- **HPC Admin Response**: Notified the user about the job termination and provided monitoring data for further investigation.

### Root Cause
- The job terminated prematurely, indicating a potential issue with the job configuration or runtime environment.

### Solution
- No specific solution provided in the conversation. Further investigation required using the monitoring data.

### General Learnings
- Monitoring data is crucial for diagnosing job termination issues.
- Users should be notified promptly about job terminations to facilitate quick resolution.

### Next Steps
- Review the monitoring data to identify the exact cause of the job termination.
- Check job configuration and runtime logs for any errors or warnings.
- If necessary, consult with the 2nd Level Support team for deeper analysis.

### References
- HPC Services, Friedrich-Alexander-Universitaet Erlangen-Nuernberg
- [HPC RRZE Website](http://www.hpc.rrze.fau.de/)

---

This documentation can be used to assist in resolving similar job termination issues in the future.
---

### 2024020842003767_Runs%20verl%C3%83%C2%A4ngern.md
# Ticket 2024020842003767

 # HPC Support Ticket: Runs verlängern

## Keywords
- Job extension
- Run ID
- User ID
- Laufzeit
- HPC Team
- FAU

## Summary
A user requested an extension of run times for specific job IDs. Initially, incorrect job IDs were provided, but the user corrected the information in a subsequent message.

## Root Cause
- Incorrect job IDs were initially provided by the user.

## Solution
- The user corrected the job IDs.
- The HPC Admin extended the run times for the correct job IDs.

## What Can Be Learned
- Always verify job IDs before submitting a request.
- Communicate clearly and promptly if any errors are noticed.
- The HPC Admin can extend job run times upon request.

## Actions Taken
- The user requested an extension for job IDs 1079890 and 1079889.
- The user corrected the request to job IDs 1080511 and 1080512.
- The HPC Admin extended the run times for the correct job IDs to 36 hours.

## Conclusion
Ensure accurate job IDs are provided in requests to avoid delays and confusion. The HPC Admin can assist with extending job run times as needed.
---

### 2017102542002126_Bitte%20um%20Jobverl%C3%83%C2%A4ngerung.md
# Ticket 2017102542002126

 ```markdown
# HPC Support Ticket: Job Extension Request

## Keywords
- Job extension
- Maximum runtime
- HPC job management

## Problem
- User's job (ID: 209258) on the HPC system "meggie" has been running for nearly 22 hours.
- Concern that the job might exceed the maximum allowed runtime of 24 hours.

## Request
- User requests an extension of the job runtime by 3 days to ensure completion.

## Solution
- HPC Admin granted the extension as requested.

## Lessons Learned
- Users should be aware of the maximum runtime limits for jobs on the HPC system.
- Proactive communication with HPC Admins can help in extending job runtimes when necessary.
```
---

### 42339486_prolongation%20of%20job%20maximum%20walltime%20on%20emmy.md
# Ticket 42339486

 # HPC-Support Ticket: Prolongation of Job Maximum Walltime on Emmy

## Keywords
- Job walltime extension
- nMOLDYN spectra calculations
- Single node jobs
- Processor hours vs. real hours

## Summary
A user requested an extension of the maximum walltime for two jobs running nMOLDYN spectra calculations on the Emmy cluster. The initial request was based on a misunderstanding between processor hours and real hours.

## Root Cause
- **Misinterpretation of Time Units**: The user initially confused processor hours with real hours, leading to an unnecessary request for walltime extension.

## Solution
- **Clarification**: The user realized the mistake and confirmed that the jobs would complete within the initially allocated 24 real hours.
- **No Action Required**: The HPC Admins acknowledged the clarification, and no further action was needed.

## Lessons Learned
- **Understanding Time Units**: Ensure users understand the difference between processor hours and real hours to avoid unnecessary requests.
- **Communication**: Encourage users to double-check their job status and requirements before submitting requests for extensions.

## Conclusion
This ticket highlights the importance of clear communication and understanding of job time units to prevent unnecessary support requests.
---

### 2024120642003064_Request%20for%20Kernel%20Upgrade%20and%20Job%20Duration%20Clarification.md
# Ticket 2024120642003064

 # HPC Support Ticket: Kernel Upgrade and Job Duration Clarification

## Keywords
- Kernel Upgrade
- Job Duration
- Job Resubmission
- Chain Jobs
- Extended Runtime
- sbatch

## Problem
1. **Kernel Upgrade**: User encountered a warning about the kernel version being below the recommended minimum, which may cause processes to hang.
2. **Job Duration**: User's training process requires 5-6 days, but the cluster's job duration limit is 24 hours.

## Solution
1. **Kernel Upgrade**:
   - The HPC Admin advised that the warning about the kernel being too old can be ignored, as no users have reported problems caused by this.

2. **Job Duration**:
   - **Job Resubmission**: The preferred option is to set up job resubmission.
   - **Chain Jobs**: One way to implement job resubmission is through chain jobs. [Documentation Link](https://doc.nhr.fau.de/batch-processing/advanced-topics-slurm/#chain-jobs)
   - **Extended Runtime Request**: For individual jobs, users can request an extended runtime by submitting them with `--hold` and then sending an email with the job ID and the cluster to HPC support.

## General Learnings
- Ignoring certain warnings based on admin advice.
- Implementing job resubmission for long-running processes.
- Using chain jobs for job resubmission.
- Requesting extended runtime for individual jobs.
---

### 2024051642001337_Extend%20time%20limit.md
# Ticket 2024051642001337

 ```markdown
# HPC Support Ticket: Extend Time Limit

## Keywords
- Job extension
- Time limit
- Job ID
- Runtime extension

## Summary
A user requested to extend the runtime of a specific job.

## Problem
- **Root Cause:** User needed more time for a job to complete.

## Solution
- **Action Taken:** HPC Admin extended the runtime of the job as requested.

## What Can Be Learned
- Users can request extensions for job runtimes.
- HPC Admins can modify job time limits upon user request.

## Notes
- Ensure proper communication and confirmation of job extensions.
- Document job ID and new time limit for future reference.
```
---

### 2022101242002042_Re%3A%20Long%20running%20process%20on%20host%20fritz2.md
# Ticket 2022101242002042

 # HPC Support Ticket: Long Running Process on Frontend

## Keywords
- Long running process
- Frontend usage
- Process killing
- Batch job submission
- CPU time

## Summary
A user's process was automatically killed after running for over an hour on the frontend node. The user believed the process should have only taken a minute or two.

## Root Cause
- The process consumed more CPU time than the user expected, possibly due to hanging or not terminating correctly.

## HPC Admin Response
- The `ps` command output showed the process ran for over an hour.
- Frontends are not meant for long-running jobs; processes running over 30 minutes are reniced and killed after one hour.
- Users should submit batch jobs for long-running processes to avoid disturbing others.

## Solution
- Users should submit batch jobs for processes that require more than 30 minutes of CPU time.
- Interactive batch jobs are available for interactive work.

## General Learning
- Always submit long-running jobs as batch jobs.
- Frontends are for compiling, submitting jobs, and short tasks only.
- Processes may hang or consume more CPU time than expected, leading to automatic termination on frontends.
---

### 2023011942000691_Increase%20runtime%21.md
# Ticket 2023011942000691

 ```markdown
# HPC-Support Ticket: Increase Runtime

## Subject
Increase runtime for video processing jobs

## Keywords
- Runtime increase
- Job time limit
- Video processing
- Alex cluster

## Problem
- User submitted jobs for processing long videos.
- Current time limit of 24 hours is insufficient for the longest videos.

## Request
- Increase runtime for jobs assigned by `b105dc10` on Alex to 48 hours.

## HPC Admin Response
- No explicit response provided in the given conversation.

## Solution
- The request for increasing the runtime to 48 hours was acknowledged.
- No further details on the implementation or outcome were provided.

## General Learning
- Users may require extended runtime for specific tasks, such as processing long videos.
- HPC Admins should consider and accommodate such requests to ensure job completion.
```
---

### 2020051142000238_Walltime%20extension.md
# Ticket 2020051142000238

 ```markdown
# HPC-Support Ticket: Walltime Extension

## Keywords
- Walltime extension
- Job ID
- User request
- HPC Admin response

## Summary
A user requested an extension of walltime for a specific job on the HPC system.

## User Request
- **Subject:** Walltime extension
- **Details:** Request to extend walltime for job ID 794655 to 36 hours on the system `meggie`.

## HPC Admin Response
- **Action:** Walltime extension granted.
- **Details:** The HPC Admin confirmed the extension without specifying the new walltime limit.

## Root Cause
- User required additional time for a running job.

## Solution
- The HPC Admin granted the walltime extension as requested.

## General Learnings
- Users can request walltime extensions for their jobs.
- HPC Admins can grant these extensions based on user requests.
- The process involves specifying the job ID and the desired extension time.
```
---

### 2023030742001181_Scheduled%20downtime%20of%20Alex.md
# Ticket 2023030742001181

 ```markdown
# Scheduled Downtime of Alex

## Keywords
- Scheduled Downtime
- Job Management
- Deadline Impact
- Communication with ZUV
- Job Postponement

## Summary
The scheduled downtime of Alex was a concern for users due to an important deadline for the MICCAI Conference 2023. The downtime was scheduled by the ZUV (Zentrale Universitätsverwaltung) and involved an external electrician, making it non-negotiable.

## Root Cause
- The downtime was scheduled by the ZUV with short notice, impacting users' ability to complete their jobs before the deadline.
- The ZUV's agreement allows for downtimes with only one day's notice, causing disruptions in job scheduling.

## User Concerns
- The downtime would delay the submission of papers for the MICCAI Conference.
- Users requested a postponement of the downtime to the following week.
- Users suggested accepting jobs that would run until the morning of the downtime and only stopping new jobs after midnight.

## HPC Admin Response
- The downtime could not be postponed due to the external electrician's schedule.
- The shutdown was rescheduled to 6 AM on Thursday, March 9, to minimize disruption.
- Jobs that would collide with the downtime were postponed until after the downtime.

## Solution
- The HPC Admins rescheduled the shutdown to 6 AM on March 9 to accommodate users' requests.
- Users were advised to plan their jobs accordingly to avoid conflicts with the downtime.

## Lessons Learned
- Better communication and planning with the ZUV are needed to avoid short-notice downtimes.
- Users should be informed well in advance about scheduled downtimes to allow for better job planning.
- The HPC Admins should consider implementing a system to automatically postpone jobs that would collide with scheduled downtimes.
```
---

### 2024102842001813_Maintenance%20Notice.md
# Ticket 2024102842001813

 # HPC Support Ticket: Maintenance Notice

## Keywords
- Maintenance
- Scheduled Downtime
- Job Allocation
- Idle Nodes
- CVPR Deadline

## Problem
- User observed idle nodes but jobs were not being allocated.
- User did not receive any notice about maintenance.
- User needed to know when the server would resume normal operations due to an approaching deadline.

## Root Cause
- Scheduled maintenance was planned for the next day.
- An email notification was sent but not received by the user.
- Jobs that would not finish before the maintenance were not being allocated.

## Solution
- HPC Admin informed the user about the scheduled downtime and provided a link to the maintenance notice.
- User was advised that jobs not finishing before the maintenance would not run.

## General Learnings
- Always check for maintenance notices on the HPC website.
- Ensure email notifications are being received.
- Plan job submissions around scheduled maintenance to avoid disruptions.

## Related Links
- [Scheduled Downtime Notice](https://hpc.fau.de/2024/10/24/scheduled-downtime-tuesday-29-10/)
- [HPC Support Email](mailto:support-hpc@fau.de)
- [HPC Website](https://hpc.fau.de/)
---

### 2019012142002389_Erh%C3%83%C2%B6hung%20des%20Zeitlimits%20f%C3%83%C2%BCr%20JobID%20354899.md
# Ticket 2019012142002389

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject
Erhöhung des Zeitlimits für JobID 354899

## Keywords
- Zeitlimit
- JobID 354899
- meggie
- woody
- qsub
- 24h
- 2 Tage

## Root Cause of the Problem
- User requires an extension of the time limit for a specific job (JobID 354899) which is expected to run longer than the current limit of 24 hours.
- The job was submitted on the 'meggie' system, which does not allow for time limit extensions via `qsub`.

## What Can Be Learned
- Different HPC systems (e.g., 'meggie' and 'woody') have varying time limits for job submissions.
- Users may need to request time limit extensions for jobs that exceed the default limits.
- The `qsub` command may not support time limit extensions on certain systems.

## Solution
- The user should contact HPC Admins to request an extension of the time limit for the specific job.
- Consider submitting future jobs on systems that allow for longer time limits if the job is expected to run longer than the default limit.
```
---

### 2022121342002608_Max.%20Runtime%20extension%20single%20node%20job%20on%20Fritz.md
# Ticket 2022121342002608

 # HPC Support Ticket: Max. Runtime Extension for Single Node Job on Fritz

## Keywords
- Runtime extension
- Single node job
- Benchmark
- Sequential version
- Parallelized version
- JobID

## Problem
- User requested a one-time extension of the maximum runtime from 24 hours to 48 hours for a single node job on Fritz.
- The reason for the extension request was to compare the performance of a sequential version of a code with a parallelized version, where the sequential version was significantly slower.

## Solution
- HPC Admin requested the JobID from the user.
- Upon receiving the JobID, the HPC Admin manually extended the runtime for the specified job.

## General Learnings
- Users may require runtime extensions for benchmarking purposes, especially when comparing different versions of their code.
- HPC Admins can manually adjust the runtime for specific jobs upon user request and providing the necessary JobID.
- Effective communication and quick response from both the user and HPC Admin are crucial for resolving such requests efficiently.

## Actions Taken
1. User sent a request for runtime extension.
2. HPC Admin asked for the JobID.
3. User provided the JobID.
4. HPC Admin manually extended the runtime for the specified job.

## Root Cause
- The sequential version of the user's code required more time to complete, necessitating an extension of the maximum runtime for benchmarking purposes.

## Resolution
- The runtime for the specified job was successfully extended by the HPC Admin.
---

### 2023061642002694_Extended%20job%20runtime.md
# Ticket 2023061642002694

 # HPC Support Ticket: Extended Job Runtime

## Keywords
- Walltime extension
- Job monitoring
- Runtime adjustment

## Summary
- **User Request**: Extend the walltime of a specific job to 40 hours.
- **HPC Admin Response**: Acknowledged the request with a brief note indicating completion.

## Root Cause
- User required additional runtime for their job.

## Solution
- HPC Admin extended the job's walltime to the requested duration.

## General Learnings
- Users may request walltime extensions for their jobs.
- HPC Admins can adjust job runtime settings upon user request.
- Ensure proper communication and acknowledgment of user requests.

## Notes
- The ticket includes a link to the job monitoring page for reference.
- The response from the HPC Admin is brief and indicates task completion.
---

### 2024050242000301_Re%3A%20Unterst%C3%83%C2%BCtzung%20bei%20Kettenjobs%20b155ee10%20_%20Projekt%20Heyl.md
# Ticket 2024050242000301

 # HPC Support Ticket Analysis

## Subject
Re: Unterstützung bei Kettenjobs b155ee10 / Projekt Heyl

## Keywords
- Job runtime extension
- Automatic job restarts
- Checkpointing
- Resource allocation
- Project extension

## Summary
The user requested an extension of job runtime to reduce the need for manual restarts. The HPC support team offered to manually extend job runtimes upon request but suggested implementing automatic job restarts as a long-term solution.

## Root Cause
The user's workflow involves frequent manual job restarts, which is time-consuming.

## Solution
1. **Manual Runtime Extension**: Users can submit jobs with the `--hold` parameter and request an extended runtime by emailing the support team with the job IDs.
2. **Automatic Job Restarts**: The preferred long-term solution is to implement automatic job restarts using chain jobs. The support team offered assistance with this implementation.

## Actions Taken
- The support team agreed to manually extend job runtimes upon request.
- The ticket was closed, and the restart-thematik was continued in a new ticket (#2024052242003958).
- The support team offered to assist with the implementation of automatic job restarts.

## General Learnings
- Manual job runtime extensions can be requested by users.
- Automatic job restarts using chain jobs are preferred for long-term solutions.
- The support team can assist with implementing automatic job restarts.
- Job runtime extensions should be requested with caution to avoid disrupting system operations.

## References
- [Chain Jobs Documentation](https://doc.nhr.fau.de/batch-processing/advanced-topics-slurm/)

## Next Steps
- Continue the discussion on automatic job restarts in the new ticket (#2024052242003958).
- Assist the user with implementing chain jobs for automatic restarts.
---

### 2024053142001881_Laufzeitverl%C3%83%C2%A4ngerung%20Job%201675090.md
# Ticket 2024053142001881

 ```markdown
# HPC-Support Ticket: Laufzeitverlängerung Job 1675090

## Keywords
- Laufzeitverlängerung
- Job 1675090
- Wochenende
- 3 Tage
- 3 Tage und 1 Stunde
- Alex

## Problem
- User requested an extension of the runtime for Job 1675090 over the weekend to 3 days (or 3 days and 1 hour).

## Solution
- HPC Admin extended the runtime of the job on Alex.

## What Can Be Learned
- Users can request runtime extensions for their jobs.
- HPC Admins can extend the runtime of jobs upon user request.
- Communication regarding job extensions should be clear and timely.
```
---

### 2024082642001198_Extend%20time%20limit%20job%202017676.md
# Ticket 2024082642001198

 ```markdown
# HPC Support Ticket: Extend Time Limit for Job

## Subject
Extend time limit job 2017676

## Keywords
- Job extension
- Time limit
- GPU load time
- NVMe storage
- Presaved weights

## Problem
- User requested to extend the runtime of job 2017676 for four days.
- Job spends significant time re-loading presaved weights upon restart.

## Root Cause
- Job requires extended runtime to avoid frequent restarts and re-loading of presaved weights.

## Solution
- HPC Admin increased the runtime of the job to 5 days.
- Suggested using fast NVMe storage to speed up the loading process.
- Provided documentation link: [NVMe Storage Documentation](https://doc.nhr.fau.de/data/workspaces)

## Lessons Learned
- Extending job runtime can reduce the overhead of re-loading data.
- Utilizing fast NVMe storage can improve job performance and reduce load times.
- Regularly saving weights can help minimize data loss but may increase restart times.

## Actions Taken
- Job runtime extended to 5 days.
- User advised to use NVMe storage for faster data loading.

## Documentation
- NVMe Storage Documentation: [Link](https://doc.nhr.fau.de/data/workspaces)
```
---

### 2020022142001171_maximale%20Anzahl%20an%20qsub-jobs.md
# Ticket 2020022142001171

 # HPC-Support Ticket Conversation Summary

## Subject
maximale Anzahl an qsub-jobs

## Keywords
- qsub jobs
- job script bundling
- time limit
- Woody
- TinyFAT
- HPC
- job requirements
- timeout

## Problem
- User needs to run a large number of short jobs (>1000) on the HPC.
- Jobs have a short runtime (<10min) and require consistent test conditions.
- Some scripts are predefined by project partners and cannot be modified.
- Jobs need to be terminated if they exceed a specified time limit.

## Questions
- Maximum number of qsub jobs that can be submitted simultaneously.
- Consequences of exceeding the job limit.
- Differences between using Woody, TinyFAT, etc.

## Solutions and Recommendations
- **Job Script Bundling**: Bundle multiple jobs into a single job script to reduce the number of qsub submissions.
  - Example: `qsub runall.x*.sh`
- **Time Limit**: Ensure each job has a time limit to prevent them from running indefinitely.
  - Example: `walltime=600`
- **Timeout Handling**: Use the `timeout` command to handle jobs that hang or exceed the time limit.
  - Example: `timeout -s 9 "$HARDTIMELIMIT"`
- **Resource Selection**: Use Woody for jobs with standard memory requirements. Avoid TinyFAT unless high memory is needed.

## Additional Notes
- Direct interaction with HPC support can help resolve complex issues more efficiently.
- Deterministic methods to check if a job is still making progress can be explored to handle timeouts more effectively.

## Conclusion
- Bundling jobs into a single script and setting appropriate time limits can help manage a large number of short jobs efficiently on the HPC.
- Direct consultation with HPC support can provide tailored solutions for specific job requirements.
---

### 2024071342000429_Extending%20the%20job%20time%20-%20iwal159h.md
# Ticket 2024071342000429

 ```markdown
# HPC-Support Ticket Conversation: Extending Job Time

## Keywords
- Job Extension
- Maximum Running Time
- Job Interruption
- Weekend Support

## Summary
A user requested an extension for a running job that did not complete within 24 hours. The job required uninterrupted execution.

## Root Cause
- The job exceeded the initial time limit of 24 hours.
- The user did not contact support before starting the job, leading to potential job termination over the weekend.

## Solution
- **Maximum Running Time**: The maximum running time for a single job is up to 48 hours, subject to sysadmin discretion.
- **Weekend Support**: Users should contact support before starting long-running jobs to avoid interruptions, especially over weekends when support is not available.

## Lessons Learned
- Always contact HPC support before starting jobs that require extended running times.
- Be aware of the maximum job running time limits and plan accordingly.
- Avoid starting critical jobs over weekends or holidays when support is not available.
```
---

### 2021113042002651_files%20not%20working.md
# Ticket 2021113042002651

 # HPC Support Ticket: Files Not Working

## Keywords
- Job ID: 996533, 996706
- Reasons: ReqNodeNotAvail, Reserved for maintenance
- Maintenance time: Started 9 am, 30 November
- Deadline concern: Thesis deadline

## Problem
- User's jobs (ID: 996533, 996706) not running due to maintenance.
- User concerned about thesis deadline and prolonged maintenance.

## Root Cause
- Scheduled maintenance on the HPC cluster.
- Jobs postponed until downtime is over.

## Communication
- **User**: Requested information about the reason for jobs not running and maintenance duration.
- **HPC Admin**: Confirmed maintenance as the reason and assured that it would be finished before Christmas. Advised the user to be patient.

## Solution
- Maintenance will be completed as soon as possible.
- No specific end time provided, but assured completion before Christmas.

## General Learning
- Maintenance can cause job delays.
- Users should be patient during maintenance periods.
- Communication about maintenance duration should be clear but may not always provide a specific end time.

## Notes
- Maintenance can impact thesis deadlines, and users may require reassurance about the duration.
- HPC Admin should provide updates if maintenance is expected to be prolonged.
---

### 2024042242002844_Increase%20Time%20of%20Job.md
# Ticket 2024042242002844

 # HPC Support Ticket: Increase Time of Job

## Keywords
- Job runtime extension
- Alex cluster
- Job ID (JOBID)

## Problem
- User requested to increase the runtime of specific jobs to 3 days.

## Root Cause
- The default runtime for the jobs was insufficient for the user's needs.

## Solution
- HPC Admin extended the runtime of the specified jobs to 3 days.

## General Learning
- Users can request runtime extensions for their jobs by providing the job IDs.
- HPC Admins have the capability to modify job runtimes upon user request.

## Actions Taken
- HPC Admin confirmed the runtime extension for the specified jobs.

## Follow-up
- No further action required from the user or HPC Admin.

## Relevant Links
- [FAU HPC Support](mailto:support-hpc@fau.de)
- [FAU HPC Website](https://hpc.fau.de/)
---

### 2024092342005287_Extend%20job%202064323%3F.md
# Ticket 2024092342005287

 ```markdown
# HPC Support Ticket: Extend Job 2064323

## Keywords
- Job extension
- Checkpoints
- Weight loading
- Temporal storage
- Walltime

## Problem
- User requested to extend job 2064323 for five days to avoid re-loading pre-saved weights across all GPUs at every restart.
- Job stops every 24 hours, leading to loss of progress and increased loading time.

## Root Cause
- Job stops after ~19 hours, causing the need to reload weights.
- Loading weights takes longer after the first 24 hours due to saved checkpoints.

## Solution
- HPC Admin increased the walltime to 5 days.
- Recommended using `/anvme` as temporal storage for faster weight loading.
- Suggested saving checkpoints more frequently to minimize loss of progress.

## General Learnings
- Extending job walltime can help avoid frequent restarts and reduce loading times.
- Using temporal storage like `/anvme` can speed up the loading of weights.
- Frequent checkpointing can minimize the loss of progress but should be balanced with the overhead of saving weights.

## References
- [NHR@FAU Data Workspaces](https://doc.nhr.fau.de/data/workspaces)
```
---

### 2023032342003612_Question%20about%20job%20durations%20on%20woody%20cluster.md
# Ticket 2023032342003612

 # HPC Support Ticket: Job Durations on Woody Cluster

## Keywords
- Max walltime
- Job duration
- Woody cluster
- Job extension

## Problem
- User needs to run jobs longer than the default max walltime of 24 hours on the woody cluster.

## Root Cause
- The woody cluster has a maximum runtime of 24 hours for all jobs.

## Solution
- HPC Admins can manually extend the job runtime for exceptional cases.
- User should submit jobs and then send job IDs along with the requested extension duration to HPC Admins.

## General Learnings
- The woody cluster has a default max walltime of 24 hours.
- Extensions are possible but should not be requested regularly.
- Users need to submit jobs first and then request extensions with job IDs and desired duration.

## Related Personnel
- HPC Admins
- User (Scientific Staff, FAU)

## Related Departments
- Friedrich-Alexander-Universität Erlangen-Nürnberg (FAU)
- Nuremberg Campus of Technology
- Lehrstuhl für Gießereitechnik
- Zentrum für Nationales Hochleistungsrechnen Erlangen (NHR@FAU)
---

### 2025030642002704_Jobverl%C3%83%C2%A4ngerung%20auf%20Helma%20-%20JobID%2035173.md
# Ticket 2025030642002704

 # HPC Support Ticket: Job Extension on Helma

## Keywords
- Job extension
- Helma
- Job ID 35173
- 120m-tinyllama-encoder-v2

## Summary
A user requested an extension for a specific job on the Helma cluster. The HPC Admin granted the extension.

## Problem
- **Root Cause**: User needed additional time to complete the job.

## Solution
- **Action Taken**: HPC Admin extended the job duration by one day.

## What Can Be Learned
- Users can request job extensions for ongoing tasks.
- HPC Admins have the authority to extend job durations upon request.
- The process for requesting and granting job extensions is straightforward and can be handled via support tickets.

## Additional Notes
- Ensure that job extensions are requested in a timely manner to avoid disruptions.
- Communication between users and HPC Admins is essential for managing job durations effectively.
---

### 2015100742001629_job%20prolongation%20on%20emmy.md
# Ticket 2015100742001629

 ```markdown
# HPC-Support Ticket Conversation: Job Prolongation on Emmy

## Keywords
- Job prolongation
- JobID
- Emmy
- Completion status
- Restart chance

## Summary
A user requested a 24-hour prolongation for a job (JobID 459812) on the Emmy cluster. The job had started the previous day at 2pm and was 60% complete with no chance of restart.

## Root Cause
- The job was running longer than initially scheduled and required additional time to complete.

## Solution
- The HPC Admin extended the job by 24 hours as requested.

## Lessons Learned
- Users may need to request additional time for jobs that are nearing completion but require more time.
- HPC Admins can prolong job durations upon user request, provided the job is critical and cannot be restarted.

## Actions Taken
- The HPC Admin acknowledged the request and extended the job duration by 24 hours.

## Notes
- Ensure users provide sufficient justification for job prolongation requests, such as completion status and the inability to restart the job.
```
---

### 2024102942001115_Access%20Issue%20with%20Work%20Directory.md
# Ticket 2024102942001115

 # Access Issue with Work Directory

## Keywords
- Access issue
- Work directory
- Downtime
- Scheduled maintenance

## Problem Description
- User unable to access work directory since morning.

## Root Cause
- Scheduled downtime on the HPC system.

## Solution
- Wait for the scheduled downtime to end.

## Lessons Learned
- Always check the HPC system's scheduled maintenance page for any downtime notices.
- Communicate downtime schedules effectively to users to manage expectations.

## Related Links
- [Scheduled Downtime Notice](https://hpc.fau.de/2024/10/24/scheduled-downtime-tuesday-29-10/)

## Roles Involved
- HPC Admins
- User
---

### 2022060242000937_Bitte%20um%20Verl%C3%83%C2%A4ngerung%20der%20Jobs%20auf%20TinyGPU.md
# Ticket 2022060242000937

 ```markdown
# HPC Support Ticket: Job Extension Request on TinyGPU

## Keywords
- Job extension
- TinyGPU
- Time limit
- Job management

## Summary
A user requested an extension of their jobs on TinyGPU due to uncertainty about completion within the time limit.

## Problem
- **Root Cause:** User's jobs might not complete within the allocated time limit.

## Solution
- **Action Taken:** HPC Admin extended the job with ID 261365 by 6 hours.
- **Follow-up:** HPC Admin inquired if additional jobs from `sles002h` also needed extension.
- **Outcome:** User confirmed that only one job required extension, indicating the other jobs likely completed within the time limit.

## Lessons Learned
- Users should monitor job progress to ensure completion within allocated time limits.
- HPC Admins can extend job time limits upon request to prevent job failure due to time constraints.
- Clear communication between users and HPC Admins is crucial for efficient job management.

## Conclusion
The ticket was closed after the job extension was confirmed and no further action was required.
```
---

### 2025021942000523_Start%20Job%202397432.md
# Ticket 2025021942000523

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject: Start Job 2397432

### Keywords:
- Job Prioritization
- Resource Allocation
- Walltime Extension
- Conference Deadline
- Model Training
- Job Failure
- Corrupt Model File

### Summary:
- User requested prioritization of a job due to an upcoming conference deadline.
- HPC Admins discussed manual intervention due to high resource demand.
- Job prioritization and walltime extension were performed multiple times.
- Job failures were identified and resolved, including issues with corrupt model files.
- Additional jobs were prioritized and walltime was extended to meet the user's requirements.

### Root Cause of Problems:
- High demand for A40 nodes leading to job delays.
- Job failures due to corrupt model files.

### Solutions:
- Manual prioritization of jobs to expedite processing.
- Extension of walltime to accommodate longer training durations.
- Identification and resolution of corrupt model files causing job failures.

### Lessons Learned:
- Importance of manual intervention in high-demand scenarios.
- Necessity of extending walltime for critical jobs.
- Identification and resolution of job failures due to corrupt files.
- Effective communication and prioritization to meet user deadlines.
```
---

### 2018061042000144_Bitte%20um%20Jobverl%C3%83%C2%A4ngerung.md
# Ticket 2018061042000144

 ```markdown
# HPC-Support Ticket: Job Extension Request

## Keywords
- Job extension
- Meggie
- 12-hour extension
- 24-hour booking

## Summary
A user requested an extension of their jobs on Meggie due to insufficient allocated time.

## Root Cause
The user's jobs were initially booked for 24 hours, but it appeared that this time would be insufficient to complete the tasks.

## Solution
The HPC Admin extended the user's 4 jobs on Meggie by an additional 12 hours.

## Lessons Learned
- Users may underestimate the time required for their jobs.
- It is important to monitor job progress and request extensions if necessary.
- HPC Admins can quickly extend job times upon user request.
```
---

### 2024050942000762_Inquiry%20Regarding%20time%20limit.md
# Ticket 2024050942000762

 ```markdown
# HPC Support Ticket: Inquiry Regarding Time Limit

## Keywords
- Time limit
- Job cancellation
- Walltime
- SLURM
- Alex cluster
- NHR@FAU

## Summary
A master's student encountered job cancellations after 50 minutes despite setting a 2-hour time limit. The issue was related to the walltime setting in the SLURM job script.

## Root Cause
- The job was submitted with a walltime of 1 hour (60 minutes) instead of the intended 2 hours.
- The application output showed 50 minutes of runtime, but this did not include startup phases, which counted towards the elapsed wallclock time.

## Solution
- Ensure the `--time` parameter in the SLURM job script accurately reflects the intended runtime.
- Verify that the job script includes the correct walltime setting:
  ```bash
  #SBATCH --time=02:00:00
  ```

## General Learnings
- Always double-check the walltime setting in the SLURM job script.
- Understand that startup phases count towards the total wallclock time.
- Ensure that the job script accurately reflects the intended runtime to avoid premature cancellations.

## Relevant SLURM Parameters
- `--time`: Specifies the maximum runtime for the job.
- `--ntasks`: Number of tasks to be launched.
- `--cpus-per-task`: Number of CPUs allocated per task.

## Example Job Script
```bash
#SBATCH --job-name=visual_rlmmbp
#SBATCH -a 0-0
#SBATCH --time=02:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=2
```

## Conclusion
Properly setting the walltime in the SLURM job script is crucial to avoid premature job cancellations. Ensure that the script accurately reflects the intended runtime and includes all necessary parameters.
```
---

### 2023092042002966_Cluster%20running%20time.md
# Ticket 2023092042002966

 # HPC Support Ticket: Cluster Running Time

## Keywords
- Running time limit
- Walltime extension
- Project approval
- Job ID
- Cluster name

## Problem
- User is experiencing issues with the 24-hour running time limit for intensive experiments.
- Requests an extension to 48 hours.

## Root Cause
- The current walltime limit is set to 24 hours.
- The user's project has high computational demands that exceed the current limit.

## Solution
- HPC Admins do not offer a queue with longer walltime.
- Users can request an extension by providing the cluster name and job ID.
- HPC Admins will extend the walltime if possible.

## Additional Information
- The user's project has already exceeded the usage of a test project.
- The initial application was not detailed enough for evaluation.
- A better application needs to be submitted.
- Harald will address the user's application in October.
- The user is advised to continue running their jobs as the cluster is not fully utilized.

## Action Items
- Users should submit detailed applications for project approval.
- For walltime extensions, provide the cluster name and job ID to HPC Admins.
- HPC Admins will review and extend the walltime if feasible.

## Follow-up
- Harald will follow up with the user in October to finalize the application and discuss computational needs.

## Contact
- For further assistance, contact the HPC support team at [support-hpc@fau.de](mailto:support-hpc@fau.de).

---

This documentation aims to assist HPC support employees in resolving similar issues related to running time limits and project approvals.
---

### 2023092642002866_Run%20a%20process%20for%20more%20time.md
# Ticket 2023092642002866

 ```markdown
# HPC-Support Ticket Conversation: Extending Process Time Limit

## Keywords
- Time limit extension
- Job runtime
- Cluster specification
- Process ID

## Summary
A user requested an extension of the time limit for a specific process. The HPC Admin extended the runtime limit and provided guidance for future requests.

## Root Cause
- User did not specify the cluster on which the job was running.

## Solution
- HPC Admin extended the runtime limit for the job on the specified cluster.
- User was advised to specify the cluster in future requests.

## What to Learn
- Always specify the cluster when requesting job modifications.
- HPC Admins can extend the runtime limit for jobs upon request.

## Example
```
User: Could you please extend the time limit for process 848053 for additional 8 hours if possible?

HPC Admin: Next time, please specify on which cluster the job is running. Job 848053 on Alex has been extended to a runtime limit of 32 hours.
```
```
---

### 42094361_Job%20extension%20JOBID%20439549.md
# Ticket 42094361

 # HPC Support Ticket: Job Extension

## Keywords
- Job extension
- JOBID
- Time extension
- HPC Admin
- User request

## Summary
A user requested an extension for the runtime of their job with a specific JOBID on the HPC system.

## Root Cause
- User needed additional time for their job to complete.

## Solution
- HPC Admin extended the job runtime as requested.

## Lessons Learned
- Users can request runtime extensions for their jobs.
- HPC Admins can grant these extensions upon request.

## Action Taken
- HPC Admin extended the runtime for the specified job.

## Notes
- Ensure users provide the correct JOBID and system name when requesting extensions.
- Communicate clearly with users to confirm the extension has been granted.

---

This documentation can be used as a reference for handling similar job extension requests in the future.
---

### 2018041742001831_Failing%20job%20re-submit%20on%20Emmy%20using%20TRAP.md
# Ticket 2018041742001831

 # HPC-Support Ticket: Failing Job Re-submit on Emmy Using TRAP

## Keywords
- Job re-submit
- TRAP command
- qsub
- Runtime request
- Batch system
- Error handling

## Summary
A user attempted to create a self re-submit script for a simulation using the `TRAP` command and `qsub`. The job was getting killed immediately upon re-submission.

## Root Cause
- The job was killed by the batch system because the requested runtime was only 5 minutes, and the job exceeded this time.

## Solution
- Ensure that the requested runtime in the job script is sufficient for the job to complete.
- Implement error handling to prevent infinite resubmission loops, such as checking the job runtime before resubmitting.

## General Learnings
- Always use the officially documented contact addresses for support requests.
- Chain jobs that resubmit themselves are permitted, but they must include safeguards to prevent infinite loops.
- Proper error handling and runtime checks are crucial to avoid overloading the batch system.

## Additional Notes
- The user was advised to check the runtime of the job and avoid resubmission if the job ran for less than 10 minutes to prevent continuous resubmission in case of errors.
- The error message in the job output file indicated that the job was killed due to exceeding the requested runtime.
---

### 42069099_Job%20extension%20ID%20373992.md
# Ticket 42069099

 ```markdown
# HPC Support Ticket: Job Extension Request

## Keywords
- Job Extension
- Running Job
- Job ID
- Woody

## Summary
A user requested an extension for a running job with a specific ID on the Woody cluster.

## Root Cause
- User needed additional time for a running job.

## Solution
- HPC Admin extended the job duration.

## Lessons Learned
- Users can request extensions for running jobs by providing the job ID.
- HPC Admins can handle job extension requests efficiently.

## Actions Taken
- HPC Admin acknowledged and extended the job duration.

## Notes
- Ensure users provide the correct job ID and cluster name when requesting extensions.
- HPC Admins should confirm the extension and notify the user promptly.
```
---

### 2024030842002561_Laufzeitverl%C3%83%C2%A4ngerung%20Job%201227215%20auf%20Fritz.md
# Ticket 2024030842002561

 # HPC Support Ticket: Job Runtime Extension Request

## Keywords
- Job runtime extension
- VASP
- k-Punkt-Grid
- Stromabschaltung
- Fritz

## Summary
A user requested an extension of the runtime for a VASP job (ID: 1227215) on the Fritz cluster due to the need for a fine k-Punkt-Grid, which requires more than 24 hours of computation time.

## Root Cause
- The job requires a fine k-Punkt-Grid, leading to extended computation time.

## Solution
- The HPC Admin granted a runtime extension but limited it to 2.5 days due to an upcoming power outage (Stromabschaltung) scheduled for Monday morning.

## General Learnings
- Users may require runtime extensions for jobs that need extensive computation time.
- Power outages and other maintenance activities can limit the duration of runtime extensions.
- Communication between users and HPC Admins is crucial for managing job runtime and scheduling around maintenance activities.

## Notes
- The user was informed about the limited extension and expressed hope that the job would complete within the allotted time.
- The HPC Admin provided clear communication about the constraints imposed by the upcoming power outage.
---

### 2021113042000439_A100_V100%20Unavailable.md
# Ticket 2021113042000439

 ```markdown
# HPC-Support Ticket: A100/V100 Unavailable

## Keywords
- A100 GPUs
- V100 GPUs
- SLURM
- Downtime
- Maintenance
- Email Notification
- MOTD

## Summary
A user reported that A100 GPUs were showing as unavailable in SLURM. The user inquired about planned maintenance and its duration.

## Root Cause
- The GPUs were unavailable due to scheduled downtime.

## Solution
- The downtime was announced via email to all HPC users and was also mentioned in the Message of the Day (MOTD).

## Lessons Learned
- Always check email notifications and MOTD for scheduled maintenance updates.
- Users should be aware of the communication channels used for maintenance announcements.

## Actions Taken
- HPC Admin informed the user about the email notification and MOTD.
- User acknowledged the information and mentioned they had missed the email due to vacation.

## Recommendations
- Ensure users are aware of the importance of checking email notifications and MOTD for maintenance updates.
- Consider additional communication channels for critical maintenance announcements.
```
---

### 2023012742002137_Verl%C3%83%C2%A4ngerung%20Jobs%20Alex.md
# Ticket 2023012742002137

 # HPC Support Ticket: Job Time Limit Extension

## Keywords
- TimeLimit
- Job Extension
- Cluster Maintenance
- Alex Cluster

## Summary
A user requested an extension of the TimeLimit for their jobs on the Alex Cluster. The HPC Admin extended the time but noted an upcoming maintenance that could affect the job's runtime. The user later requested an additional extension for the remaining jobs.

## Root Cause
- User required longer runtime for jobs.
- Upcoming maintenance could interrupt jobs.

## Solution
- HPC Admin extended the job TimeLimit as requested.
- Informed the user about potential interruptions due to maintenance.
- Provided updates on job status and further extensions.

## Lessons Learned
- Always check for upcoming maintenance when extending job runtimes.
- Communicate potential interruptions to users.
- Be prepared to handle additional extension requests.

## Follow-up Actions
- Monitor job status during maintenance.
- Inform users about any job interruptions or cancellations.
- Update users on the completion or extension of their jobs.
---

### 2017031542001409_2%20Punkte%20zu%20LiMa.md
# Ticket 2017031542001409

 # HPC Support Ticket Conversation Analysis

## Keywords
- HPC Support
- LiMa
- Woody
- Scheduler
- Healthcheck
- Timeouts
- Scheduler Status Abfragen
- Cronjob
- Webanzeige
- Jobstart

## Root Cause of the Problem
- **Website Issue**: The user reported that the webpage displaying queue information for LiMa is not functioning correctly, specifically the graphics are missing.
- **Scheduler Performance**: The user observed that the scheduler on LiMa is slower in starting jobs compared to Woody, despite having many free nodes.

## Solution
- **Website Issue**: The issue with the website is caused by timeouts from scheduler status queries, which occur when many jobs are being started. This leads to missing information for the webpage when the cronjob generates the data.
- **Scheduler Performance**: The slower job start on LiMa is due to a healthcheck performed during job initialization, which reduces the number of jobs that can be started per minute compared to Woody.

## General Learnings
- **Healthcheck Impact**: Understand that the healthcheck process on LiMa affects the speed at which jobs can be started.
- **Website Data Generation**: Recognize that timeouts from scheduler status queries can cause issues with the data displayed on the website, particularly when many jobs are being started simultaneously.
- **Patience Required**: Users may need to exercise patience when submitting jobs to LiMa due to the healthcheck process.

## Documentation for Support Employees
When encountering similar issues with LiMa's scheduler performance and website display, consider the following:
- Check if the healthcheck process is causing delays in job starts.
- Verify if timeouts from scheduler status queries are affecting the data generation for the website.
- Inform users about the healthcheck process and the potential for slower job starts on LiMa compared to other systems like Woody.

---

This analysis provides a concise overview of the issues and solutions discussed in the HPC support ticket conversation, which can be used as a reference for future support cases.
---

### 2020071642000725_Maintenance.md
# Ticket 2020071642000725

 ```markdown
# HPC Support Ticket: Maintenance

## Keywords
- Maintenance
- Cluster downtime
- Estimation

## Summary
- **User Inquiry:** Request for an estimate of how long the cluster will be down for maintenance.
- **HPC Admin Response:** Not provided in the given conversation.

## Root Cause
- User requires information on the duration of the cluster downtime for planning purposes.

## Solution
- HPC Admin should provide an estimated duration for the cluster downtime to help users plan their work accordingly.

## General Learnings
- Users often need advance notice and estimates for maintenance downtimes to manage their workloads effectively.
- Clear communication about maintenance schedules and durations is crucial for user satisfaction and efficient resource management.
```
---

### 2024102842001911_kind%20request%20for%20extending%20GPU%20time%20limit.md
# Ticket 2024102842001911

 ```markdown
# HPC Support Ticket: Extending GPU Time Limit

## Keywords
- GPU time limit
- Wall time
- Checkpoints
- Automatic restart
- Job-ID
- #SBATCH --hold

## Problem
- User needs to train a model with a large dataset, requiring more than 24 hours of GPU time.
- Request to extend the time limit to two days for a single account.

## Solution
- **Not Possible**: Increasing the wall time for a single account is not feasible.
- **Recommended Approach**: Use checkpoints and automatic restart for long-running jobs.
- **Admin Assistance**: For single jobs, admins can increase the runtime. User must start the job with the extra option `#SBATCH --hold` and provide the job-ID to the HPC Admins.

## General Learnings
- **Checkpoints and Restart**: For long-running jobs, implement checkpoints to save progress and enable automatic restarts.
- **Admin Intervention**: Admins can manually extend the runtime for specific jobs upon request.
- **Job Management**: Use `#SBATCH --hold` to manage job submissions that require admin intervention.

## Roles Involved
- **HPC Admins**: Johannes Veh
- **User**: PhD student in the pattern recognition lab
```
---

