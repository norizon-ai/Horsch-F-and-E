# Topic 28: accountpartition_combination_invalid_account_error

Number of tickets: 29

## Tickets in this topic:

### 2021040642002719_Meggie%20allocation.md
# Ticket 2021040642002719

 # HPC Support Ticket: Meggie Allocation

## Keywords
- Job submission error
- Invalid account/partition combination
- Account activation
- Meggie cluster
- WRF model
- sbatch

## Problem Description
A master's student was unable to submit jobs to the Meggie cluster using `sbatch real.meggie.sh`. The error message received was:
```
sbatch: error: Batch job submission failed: Invalid account or account/partition combination specified
```

## Root Cause
The student's account was not activated for the Meggie cluster.

## Solution
An HPC Admin activated the student's account for the Meggie cluster, resolving the issue.

## General Learnings
- Ensure user accounts are activated for the specific cluster they need to access.
- Invalid account or account/partition combination errors can indicate that the account is not properly set up for the targeted cluster.
- HPC Admins can activate accounts for specific clusters to resolve such issues.
---

### 2019062942000581_Accounting%20auf%20Meggie.md
# Ticket 2019062942000581

 # HPC Support Ticket: Accounting auf Meggie

## Keywords
- Account activation
- Meggie cluster
- srun/salloc error
- sacct error
- Invalid account or account/partition combination
- slurm_persist_conn_open_without_init
- Connection refused

## Summary
- **User Issue**: User unable to allocate resources on Meggie cluster using `srun`/`salloc`, receiving error messages related to invalid account or account/partition combination and connection issues.
- **Error Messages**:
  - `Unable to allocate resources: Invalid account or account/partition combination specified`
  - `slurm_persist_conn_open_without_init: failed to open persistent connection to localhost:6819: Connection refused`

## Root Cause
- Possible issues with account activation for Meggie cluster.
- Potential missing `-a` option in `srun` command.

## Solution
- Verify if the user's account (hpc023) is activated for Meggie cluster.
- Check if the `-a` option is required in the `srun` command and provide the correct syntax if necessary.

## Actions Taken
- HPC Admins to confirm account activation status.
- 2nd Level Support team to assist with command syntax and troubleshooting connection issues.

## Notes
- Ensure proper account activation and correct command usage for resource allocation on Meggie cluster.
- Review and resolve any persistent connection issues reported by `sacct`.

## Follow-up
- Confirm resolution with the user and document any additional steps taken to resolve the issue.

---

This documentation aims to assist support employees in resolving similar errors related to account activation and resource allocation on the Meggie cluster.
---

### 2024022242001705_Account%20b202dc10%20%3A%20%22Invalid%20account%20or%20account_partition%20combination%20specified%2.md
# Ticket 2024022242001705

 ```markdown
# HPC Support Ticket: Invalid Account or Account/Partition Combination Specified Error

## Keywords
- Invalid account
- Account/partition combination
- NHR project account
- Tier3 resources
- sbatch error
- Cluster access

## Problem Description
- User received a new NHR project account.
- User can connect to the account and fileserver without issues.
- Error occurs when submitting a job with `sbatch`: "sbatch: error: Batch job submission failed: Invalid account or account/partition combination specified".
- User can submit jobs from another account (Tier3 account) without problems.
- User tried changing clusters to `tinygpu` or `tinyfat` but still encountered the error.

## Root Cause
- The NHR project account does not have access to Tier3 resources like `tinygpu` and `tinyfat`.
- The user's other account (Tier3 account) has access to the named clusters.

## Solution
- The user needs to connect to the appropriate cluster frontend for the NHR project account, which in this case is `alex`.
- Ensure that the job submission is directed to the correct cluster that the NHR account has access to.

## Lessons Learned
- Different types of accounts (NHR vs. Tier3) have different access permissions to clusters.
- It is essential to verify the cluster access permissions for each account type.
- Users should ensure they are submitting jobs to the correct cluster based on their account type.

## Actions Taken
- HPC Admins verified the account type and cluster access permissions.
- User was informed about the correct cluster to use for the NHR project account.
- User successfully connected to the appropriate cluster frontend and resolved the issue.
```
---

### 2022080842001547_Tier3-Access-Alex%20%22Christoph%20Breuning%22%20_%20iww2011h.md
# Ticket 2022080842001547

 # HPC Support Ticket Conversation Analysis

## Keywords
- Account activation
- Job submission error
- Invalid account/partition combination
- GPU allocation
- SLURM commands (`sbatch`, `salloc`)

## Summary
A user encountered issues submitting jobs and opening interactive shells after their account was activated on the HPC cluster. The error message indicated an invalid account or account/partition combination.

## Root Cause
- The user's account configuration was incomplete, leading to job submission failures.

## Solution
- The HPC Admin identified and fixed the missing configuration, resolving the issue.

## General Learnings
- Ensure proper account configuration when activating new user accounts.
- Common SLURM error messages can indicate configuration issues.
- Prompt communication between users and HPC Admins is crucial for quick resolution of issues.

## Relevant Commands
- `salloc --gres=gpu:a40:1 --partition=a40 --time=01:00:00`

## Troubleshooting Steps
1. Verify account configuration.
2. Check partition and resource allocation settings.
3. Ensure the user has the necessary permissions and quotas.

## Additional Notes
- The user required access to Nvidia A40 GPUs for numerical simulations using Python.
- The issue was resolved within a day, highlighting efficient support processes.
---

### 2022082542002541_%21%21HPC%20Application%21%21.md
# Ticket 2022082542002541

 ```markdown
# HPC Support Ticket Conversation Analysis

## Keywords
- HPC Application
- Account Verification
- Job Submission Error
- Account Reactivation
- Cluster: Woody

## General Learnings
- **Account Verification**: Users need to sign and return the prepared HPC application form.
- **Job Submission Error**: Common error "sbatch: error: Batch job submission failed: Invalid account or account/partition combination specified" can occur due to account issues.
- **Account Reactivation**: After reactivation, it may take up to a day for all services to be available.
- **Support Escalation**: Complex issues may need to be escalated to the HPC support team.

## Root Cause of the Problem
- **Job Submission Error**: The user encountered an error while submitting jobs due to an invalid account or account/partition combination.

## Solution
- **Account Reactivation**: The user's account was reactivated, and it was advised to wait for up to a day for all services to be available.
- **Additional Information**: The user was asked to provide more details about the cluster and job specifications for further troubleshooting.

## Documentation for Support Employees
When encountering the error "sbatch: error: Batch job submission failed: Invalid account or account/partition combination specified," ensure the user's account is active and correctly configured. If the account was recently reactivated, advise the user to wait for up to a day for all services to be available. If the issue persists, escalate to the HPC support team for further assistance.
```
---

### 2023032742004382_Can%27t%20submit%20batch%20jobs%20to%20Alex.md
# Ticket 2023032742004382

 # HPC Support Ticket: Can't Submit Batch Jobs to Alex

## Keywords
- Account Reactivation
- Job Submission Error
- Invalid Account/Partition Combination
- salloc
- sbatch
- GPU Allocation

## Problem Description
- User's HPC account was reactivated after a hiatus.
- User is unable to submit batch jobs or spawn interactive sessions on Alex.
- Error message: `salloc: error: Job submit/allocate failed: Invalid account or account/partition combination specified`
- Command used: `salloc --gres=gpu:a40:1 --time=01:00:00`

## Root Cause
- Possible incomplete account reactivation or missing access rights to specific partitions or resources.

## Solution
- HPC Admin confirmed that the account has been re-enabled on Alex.
- No further action was specified, but the issue seems to be resolved by the admin's intervention.

## Lessons Learned
- Account reactivation may not always restore full access to HPC resources.
- Invalid account or partition errors can indicate incomplete reactivation.
- Contact HPC Admin for access issues post-reactivation.

## Next Steps for Similar Issues
- Verify account status and access rights.
- Check for proper partition and resource allocation.
- Escalate to HPC Admin if the problem persists.
---

### 2019091742001954_%5BMuCoSim%5D%20Zugang%20Testcluster.md
# Ticket 2019091742001954

 # HPC Support Ticket: Access Issue on Testcluster

## Keywords
- SLURM
- Testcluster
- Account permissions
- Interactive job
- srun
- Invalid account or account/partition combination

## Problem Description
The user was unable to start an interactive job on the testcluster using SLURM. The error message received was:
```
srun: error: Unable to allocate resources: Invalid account or account/partition combination specified
```
The user had previously attended a seminar and was attempting to use the testcluster for the first time since the migration to SLURM. The user's student account seemed to lack the necessary permissions, despite having access to other clusters like Emmy.

## Root Cause
The user's account was not explicitly enabled for the testcluster after the migration to SLURM.

## Solution
HPC Admins explicitly enabled the user's account for the testcluster, resolving the access issue.

## Lessons Learned
- After system migrations or updates, user accounts may need to be explicitly re-enabled or configured.
- Different clusters may have different permission requirements, even if a user has access to one cluster, they may not have access to others.
- The error message "Invalid account or account/partition combination specified" can indicate a permissions issue.

## Actions Taken
1. User reported the issue with detailed steps and error messages.
2. HPC Admins identified the root cause as a permissions issue.
3. HPC Admins explicitly enabled the user's account for the testcluster.
4. User confirmed the resolution.
5. Ticket closed as resolved.
---

### 2018103042000947_Meggie%20-%20Startprobleme.md
# Ticket 2018103042000947

 # HPC Support Ticket: Job Submission Failure on Meggie

## Keywords
- Job submission
- Meggie
- Invalid account
- Account/partition combination
- Freigeschaltet (activated)

## Problem Description
The user attempted to submit a job on Meggie but received an error message indicating an invalid account or account/partition combination.

## Root Cause
The user's account was not activated for job submission on Meggie.

## Solution
HPC Admins activated the user's account, allowing them to submit jobs on Meggie.

## General Learnings
- Accounts need to be individually activated for job submission on Meggie.
- The error message "Invalid account or account/partition combination specified" can indicate that the account is not activated.
- HPC Admins can activate accounts to resolve this issue.
---

### 2023072642001209_Problems%20with%20batch%20job%20submission.md
# Ticket 2023072642001209

 # HPC Support Ticket: Problems with Batch Job Submission

## Keywords
- Batch job submission
- SLURM
- sbatch
- Partition not available
- Security concerns

## Problem Description
- User encountered issues submitting batch jobs to the `tinyfat` cluster.
- Error message: `sbatch: error: Batch job submission failed: Required partition not available (inactive or drain)`
- The batch script is based on MPI without hyperthreading and previously worked.

## Root Cause
- Temporary disablement of access due to security concerns.

## Solution
- HPC Admin advised the user to try again as the issue was temporary.

## General Learnings
- Partition availability issues can be caused by temporary administrative actions.
- Users should be informed about temporary disruptions and advised to retry after the issue is resolved.

## Actions Taken
- HPC Admin acknowledged the issue and informed the user about the temporary disablement.
- User was advised to retry job submission.

## Notes
- Ensure clear communication with users regarding temporary disruptions and their resolution.
- Monitor and address security concerns promptly to minimize user impact.
---

### 2018102442001869_Probleme%20mit%20sbatch%20job-submission.md
# Ticket 2018102442001869

 # HPC Support Ticket: Probleme mit sbatch job-submission

## Keywords
- sbatch
- job submission
- invalid account
- account/partition combination
- Meggie cluster
- HPC access
- permission issue

## Problem Description
A master's student encountered an error while submitting a job using `sbatch` on the Meggie cluster. The error message indicated an invalid account or account/partition combination. The script used for job submission was successfully used by other group members, suggesting a potential permission issue.

## Root Cause
The user's account was not enabled for job submission on the Meggie cluster.

## Solution
The HPC Admin enabled the user's account for the Meggie cluster, resolving the job submission issue.

## Lessons Learned
- Ensure that user accounts are properly configured and have the necessary permissions for the specific cluster they intend to use.
- Verify account/partition combinations in job submission scripts to avoid invalid account errors.
- Communicate with the HPC support team for account-related issues to ensure proper access and permissions.

## Actions Taken
1. User reported the issue with detailed error message.
2. HPC Admin identified the root cause as a permission issue.
3. HPC Admin enabled the user's account for the Meggie cluster.
4. User confirmed that the job submission was successful after the account was enabled.

## Follow-up
No further action required as the issue was resolved.
---

### 2018100842001425_WG%3A%20Freischaltung%20eines%20Accounts%20f%C3%83%C2%BCr%20bcpc000h%20auf%20Meggie.md
# Ticket 2018100842001425

 # HPC Support Ticket: Account Activation for Meggie Cluster

## Keywords
- Account activation
- Meggie cluster
- Batch job submission
- Invalid account error
- GROMACS
- MD simulations

## Summary
A user encountered an error when submitting a batch job on the Meggie cluster due to an invalid account or account/partition combination. The user had previously used the Emmy cluster and needed access to Meggie for larger molecular dynamics (MD) simulations using GROMACS.

## Root Cause
- The user's account was not initially activated for the Meggie cluster.

## Solution
- The user requested account activation for the Meggie cluster.
- The HPC Admin confirmed that the account was already activated when they attempted to activate it.

## Lessons Learned
- Users should ensure their accounts are activated for the specific cluster they intend to use.
- Communication with HPC support is essential for resolving account-related issues.
- Proper account activation is crucial for successful batch job submissions.

## Follow-up Actions
- Verify account activation status for users reporting similar issues.
- Ensure users are aware of the account activation process for different clusters.

## Relevant Parties
- HPC Admins
- 2nd Level Support Team
- Head of the Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support
- Software and Tools Developer
---

### 2020032642002211_Fwd%3A%20Access%20to%20supercomputer%20from%20FAU.md
# Ticket 2020032642002211

 ```markdown
# HPC-Support Ticket: Access to Supercomputer from FAU

## Keywords
- Access issues
- Job submission error
- Account/partition combination
- Computing hours
- Meggie cluster
- Batch job submission
- Invalid account

## Summary
A user experienced issues with job submission on the Meggie cluster due to an invalid account or account/partition combination. The user also inquired about available computing hours.

## Root Cause
- The user's account was not properly configured for job submission.
- The user was unaware of the computing hours policy.

## Solution
- HPC Admins enabled the user's account on Meggie and advised on job submission practices.
- HPC Admins informed the user about the computing hours policy, which is based on resource usage over the past two weeks.

## What to Learn
- Ensure that user accounts are properly configured for job submission.
- Advise users on efficient job submission practices to minimize overhead.
- Inform users about the computing hours policy and how it affects their job priority.
- Provide users with relevant documentation and tutorials for getting started with HPC systems.

## Actions Taken
- HPC Admins enabled the user's account on Meggie.
- HPC Admins advised the user to aggregate jobs to minimize overhead.
- HPC Admins informed the user about the computing hours policy.
- The user was provided with a getting started tutorial for the HPC systems at RRZE.
```
---

### 2024050742000757_Fehler%20beim%20Submitten%20eines%20TinyFat%20Jobs.md
# Ticket 2024050742000757

 # HPC Support Ticket: Error Submitting TinyFat Job

## Keywords
- Job submission error
- Slurm script
- Invalid account or account/partition combination
- Aufräumaktion (cleanup action)

## Problem Description
User encountered an error when attempting to submit a job using a Slurm script:
```
sbatch: error: Batch job submission failed: Invalid account or account/partition combination specified
```

## Root Cause
The issue was caused by an error during a cleanup action over the weekend.

## Solution
HPC Admin identified and resolved the issue related to the cleanup action.

## Lessons Learned
- Regular maintenance and cleanup actions can sometimes lead to unintended issues.
- Quick identification and resolution of such issues are crucial for maintaining user satisfaction.
- Users should be informed about potential disruptions during maintenance periods.

## Follow-up Actions
- Ensure that future cleanup actions are thoroughly tested to avoid similar issues.
- Provide users with clear communication regarding maintenance schedules and potential impacts.

## References
- [FAU HPC Support](mailto:support-hpc@fau.de)
- [FAU HPC Website](https://hpc.fau.de/)
---

### 2023031742000485_Fehlermeldung%20mit%20salloc%20au%20Alex.md
# Ticket 2023031742000485

 ```markdown
# HPC Support Ticket: Fehlermeldung mit salloc auf Alex

## Keywords
- salloc
- Slurm
- Account Inactivity
- Invalid Account
- GPU Allocation
- Partition

## Problem Description
- User encountered an error when trying to allocate resources using `salloc` on Alex.
- Error message: `salloc: error: Job submit/allocate failed: Invalid account or account/partition combination specified`
- User had previously been able to use the same command without issues.

## Root Cause
- The user's HPC account was inactive for an extended period, leading to its removal from Slurm on Alex and Fritz.

## Solution
- HPC Admin reactivated the user's account in Slurm.
- The user confirmed that the issue was resolved after the account reactivation.

## Lessons Learned
- Inactivity can lead to account deactivation in Slurm.
- Reactivating the account resolves the `Invalid account or account/partition combination specified` error.
- Regular account activity is necessary to maintain access to HPC resources.
```
---

### 2023090142000495_Re%3A%20Reactivated%20account%20for%20%22PTFS-Vorlesung%20%28Prof.%20Wellein%29%22%20atportal.hpc.fa.md
# Ticket 2023090142000495

 ```markdown
# HPC Support Ticket: Reactivated Account Issue

## Summary
User encountered issues with job submission after account reactivation, receiving errors related to invalid account or account/partition combination.

## Keywords
- Account Reactivation
- Job Submission Error
- Invalid Account/Partition Combination
- HPC Portal
- SSH Keys
- Storage Consolidation

## Problem Description
- User received an error when trying to allocate resources for running a job:
  ```
  salloc: error: Job submit/allocate failed: Invalid account or account/partition combination specified
  sbatch: error: Batch job submission failed: Invalid account or account/partition combination specified
  ```

## Root Cause
- The user's account was reactivated, but there was an issue with the account/partition configuration on the server.

## Steps Taken
1. **Account Reactivation**:
   - Account "ptfs151h" was reactivated by the Training and Support Group Leader.
   - User was instructed to log in via SSO to review the reactivation.

2. **Error Reporting**:
   - User reported job submission errors despite account reactivation.

3. **Admin Intervention**:
   - HPC Admins checked the server configuration and found it to be correct.
   - The account was fully enabled on the server.

4. **Resolution**:
   - After enabling the account, the user confirmed that the issue was resolved and they could submit jobs successfully.

## Solution
- Ensure that the account is fully enabled on the server.
- Verify the server configuration for the account/partition combination.

## Lessons Learned
- Account reactivation does not always immediately resolve job submission issues.
- Server configuration for account/partition combinations must be verified.
- Clear communication between the user and support team is crucial for resolving issues efficiently.
```
---

### 2023051542002536_Cannot%20rum%20srun%20commands.md
# Ticket 2023051542002536

 # HPC Support Ticket: Cannot Run `srun` Commands

## Keywords
- `srun`
- Resource allocation error
- Invalid account/partition combination
- Slurm
- GPU resources
- Account activation delay

## Problem Description
User is unable to run `srun` commands to allocate GPU resources on the cluster. The error message received is:
```
srun: error: Unable to allocate resources: Invalid account or account/partition combination specified
```

## Root Cause
- Possible delay in account activation after invitation acceptance.
- Incorrect account or partition specification in the `srun` command.

## Troubleshooting Steps
1. **Account Activation Delay**: Ensure that the user's account has been activated. It may take until the day after accepting the invitation for access to be granted.
2. **Verify Account and Partition**: Confirm that the account name and partition specified in the `srun` command are correct.

## Solution
- Wait for the account to be fully activated, which typically happens the day after accepting the invitation.
- Double-check the account name and partition details in the `srun` command for accuracy.

## Example Commands
```bash
srun --partition=a100 --nodes=1 --clusters=tinygpu --time=1:0:0 --gres=gpu:a100:1 --pty /bin/bash -l
srun -M tinygpu -p rtx2080ti -N 1 --gres gpu:rtx2080ti:1 --pty /bin/bash -l
```

## Additional Notes
- Ensure all directories like `$HOME`, `$WORK`, or `$HPCVAULT` are available after account activation.
- Contact HPC Admins for further assistance if the issue persists.

## References
- [FAU HPC Support](mailto:support-hpc@fau.de)
- [FAU HPC Website](https://hpc.fau.de/)
---

### 2018040442002701_Skylake.md
# Ticket 2018040442002701

 # HPC Support Ticket: Skylake Node Access

## Keywords
- Skylake node
- Testcluster
- Loginknoten
- Submit-Host
- PBS/torque
- BIOS-Einstellung
- Subnuma-Clustering

## Problem
- User wants to access and test the Skylake node.
- User has forgotten the login node details for the test cluster.

## Solution
- **Submit-Host**: `testfront.rrze`
- **Batch System**: PBS/torque
- **Access Skylake Node**: Use `-lnodes=skylakesp2:ppn=80`
- **Note**: The Skylake node is regularly rebooted with varying BIOS settings, including Subnuma-Clustering.

## General Learnings
- Users may need reminders about login node details for test clusters.
- Specific nodes can be accessed using batch system commands.
- Regular reboots and BIOS setting changes can affect node behavior.

## Root Cause
- User forgot the login node details for the test cluster.

## Additional Notes
- The Skylake node is part of the test cluster and is subject to regular reboots with different BIOS settings.
---

### 2022100542005035_Fehlermeldung%20%22sbatch%20error%20batch%20job%20submission%20failed%20invalid%20account%20or%20acc.md
# Ticket 2022100542005035

 # HPC Support Ticket: Invalid Account or Partition Combination Error

## Keywords
- sbatch error
- invalid account
- account/partition combination
- job submission failed
- Meggie
- starccm+ Simulation
- new Betriebssystem
- Freischalten neuer Accounts
- Cronjob
- Skript

## Problem Description
User encountered an error when trying to submit a job using `sbatch` on Meggie for a starccm+ simulation. The error message was: "sbatch error batch job submission failed invalid account or account/partition combination specified." The issue persisted regardless of the directory from which the job was submitted.

## Root Cause
The error was due to a system issue where new accounts were not properly enabled after the recent OS upgrade on Meggie. Additionally, there was an outdated reference to "meggie8" in a Cronjob and script.

## Solution
HPC Admin identified and resolved the issue with account activation post-OS upgrade. The user should now be able to submit jobs successfully. Additionally, the outdated reference in the Cronjob and script was noted and should be updated.

## General Learnings
- Ensure proper account activation after system upgrades.
- Check for outdated references in scripts and Cronjobs.
- Common issue with `sbatch` errors can be related to account or partition configurations.

## Next Steps
- Verify that the user can submit jobs without errors.
- Update any outdated references in scripts and Cronjobs.
- Monitor for similar issues after future system upgrades.

## Relevant Contacts
- HPC Admins
- 2nd Level Support Team
- Georg Hager (Training and Support Group Leader)
- Harald Lanig (NHR Rechenzeit Support)
- Jan Eitzinger and Gruber (Software and Tools Developer)
---

### 2024062642002888_Unable%20to%20access%20testcluster.md
# Ticket 2024062642002888

 # HPC Support Ticket: Unable to Access Testcluster

## Keywords
- Testcluster access
- Account permissions
- Invalid account/partition combination
- `salloc` error
- Master's thesis
- Performance-Portable Microphysics Module
- SYCL

## Problem Description
- **User Issue**: Unable to access the test cluster in Erlangen.
- **Error Message**: `salloc: error: Job submit/allocate failed: Invalid account or account/partition combination specified`
- **Root Cause**: User's account was not enabled on the test cluster.

## Ticket Conversation Summary
- **User**: Requested access to the test cluster but encountered an error when trying to allocate resources.
- **HPC Admin**: Informed the user that their account was not enabled on the test cluster and requested more information about the purpose of access.
- **User**: Explained that access was needed to test the portability and performance of their Master's thesis project on various architectures.
- **HPC Admin**: Internally requested to enable the user's account for the test cluster.
- **HPC Admin**: Confirmed that the user's account was enabled and provided documentation for the test cluster.

## Solution
- The user's account (`btr0111h`) was enabled on the test cluster by adding the necessary account and partition:
  ```bash
  sacctmgr add account btr0
  sacctmgr add user btr0111h account=btr0 partition=work
  ```
- The user was then able to access the test cluster and provided with the cluster documentation.

## General Learnings
- Always verify that a user's account is enabled on the specific cluster they are trying to access.
- Communicate with the user to understand the purpose of their request to better assist them.
- Internal requests may be necessary to enable accounts or modify permissions.
- Provide relevant documentation to users once their issue has been resolved.
---

### 2023103042001972_Batch%20job%20submission%20failed.md
# Ticket 2023103042001972

 # HPC Support Ticket: Batch Job Submission Failed

## Keywords
- Batch job submission
- Invalid account or account/partition combination
- Account expiration
- PTFS account
- PAMPI account
- Cmake path
- Export command
- Soft quota

## Summary
A user encountered issues with batch job submission and cmake configuration on the HPC clusters Fritz and Meggie. The primary issue was related to account expiration and invalid account/partition combinations.

## Root Cause
1. **Account Expiration**: The user's PTFS account was set to expire, preventing job submissions on the Fritz cluster.
2. **Invalid Account/Partition Combination**: The user attempted to submit jobs with an invalid account or account/partition combination.
3. **Temporary Environment Variables**: The user set the cmake path using the `export` command in the terminal, which is temporary and reset upon opening a new shell.

## Solution
1. **Account Reactivation**: The user's supervisor granted an extension for the PTFS account, allowing continued access to the Fritz cluster.
2. **Manual Data Transfer**: The user was advised to manually copy data from the PTFS account to the PAMPI account, as these accounts do not share the same home directories or data.
3. **Permanent Environment Variables**: The user was informed that environment variables set with `export` are temporary. To make them permanent, the user should add the `export` command to the `.bashrc` file.

## General Learnings
- **Account Management**: Ensure that user accounts are active and have the necessary permissions for job submissions.
- **Environment Variables**: Use the `.bashrc` file to set permanent environment variables instead of using the `export` command in the terminal.
- **Data Transfer**: Manually copy data between separate accounts if needed, as they do not share the same home directories or data.

## Follow-up Actions
- Verify that the user's account is active and has the correct permissions.
- Ensure that the user understands how to set permanent environment variables.
- Assist the user with data transfer between accounts if necessary.

## Related Issues
- Account expiration and job submission errors.
- Temporary environment variables and cmake configuration issues.
- Data transfer between separate user accounts.
---

### 2022012142002195_Access%20to%20Alex.md
# Ticket 2022012142002195

 # HPC Support Ticket Analysis: Access to Alex Cluster

## Keywords
- Account sharing
- Job submission error
- Partition access
- SLURM
- Alex Cluster

## Summary
A user encountered issues submitting a job to the Alex Cluster and requested access. The HPC Admin identified account sharing as a potential cause and provided a solution to the job submission error.

## Root Cause
- **Account Sharing**: The user was sharing an account with another individual, which is against the HPC usage policies.
- **Job Submission Error**: The user received an error indicating that their group was not permitted to use the specified partition.

## Solution
- **Partition Specification**: The HPC Admin advised the user to add `#SBATCH --partition=a40` to their job script to resolve the submission error.
- **Account Sharing**: The user was informed about the policy against account sharing and advised to obtain a separate account.

## Lessons Learned
- **Detailed Error Messages**: Users should provide detailed error messages to facilitate diagnosis.
- **Policy Awareness**: Users should be aware of and comply with HPC usage policies, including those regarding account sharing.
- **Communication**: When sharing accounts, all relevant information should be communicated among users to avoid issues.

## Follow-Up
- The user was advised to continue working while the account sharing issue is addressed.
- The user agreed to inform their supervisor about the need for a separate account.

## Conclusion
Proper communication and adherence to policies are crucial for efficient HPC usage. Detailed error messages and specific instructions from HPC Admins can help resolve technical issues quickly.
---

### 2022080942003703_Permissions%20b134dc10.md
# Ticket 2022080942003703

 # HPC Support Ticket: Permissions Issue

## Keywords
- Permissions
- Account activation
- Batch job submission error
- Invalid account/partition combination
- User invitation

## Summary
A user and their colleague were invited to a project but encountered an error when submitting batch jobs. The error message indicated an invalid account or account/partition combination.

## Root Cause
- The users were invited to the project but encountered permission issues.
- The error message: `sbatch: error: Batch job submission failed: Invalid account or account/partition combination specified`.

## Solution
- The HPC Admin identified and resolved an error on their end.
- The users were informed that the issue should now be resolved.

## Lessons Learned
- Ensure that user permissions are correctly set up after invitations.
- Check for any errors on the HPC Admin side that might prevent users from submitting jobs.
- Communicate clearly with users about the resolution of permission issues.

## Follow-Up
- Verify that the users can now submit batch jobs without encountering the error.
- Document the steps taken to resolve the issue for future reference.
---

### 2024071742000592_Access%20to%20H100%20on%20Tinyx.md
# Ticket 2024071742000592

 # HPC Support Ticket: Access to H100 on Tinyx

## Keywords
- H100 Nodes
- Access Permissions
- Job Submission Error
- Account Eligibility
- Partition Configuration

## Problem Description
The user attempted to allocate H100 nodes using `salloc` and `sbatch` but encountered an error indicating an invalid account or account/partition combination. The user has an HPC account with Tier3 Grundversorgung LS Informatik 5.

## Root Cause
The H100 nodes are exclusively reserved for a specific group that paid for them, and the user's account does not have access to this partition.

## Solution
The HPC Admin informed the user that access to the H100 nodes is restricted to the group that funded them. No further action was taken as the user's account is not eligible for access.

## General Learnings
- Access to specific nodes or partitions may be restricted to certain groups or accounts.
- Users should verify their account eligibility and partition access before attempting to allocate resources.
- The error message "Invalid account or account/partition combination specified" indicates a permission issue rather than a technical problem.

## Next Steps for Similar Issues
- Check the user's account eligibility and partition access.
- Inform the user about any restrictions or requirements for accessing specific resources.
- If necessary, guide the user through the process of requesting access or upgrading their account.
---

### 2021042842000386_meggie%20problem.md
# Ticket 2021042842000386

 # HPC Support Ticket: Meggie Job Submission Issue

## Keywords
- Job submission
- SLURM
- Account activation
- Module loading
- Profile script

## Problem Description
- User encountered an error when submitting a job to the Meggie cluster.
- Error message: `sbatch: error: Batch job submission failed: Invalid account or account/partition combination specified`
- User's account was not activated for the Meggie cluster.
- User experienced issues loading modules (`module: command not found`).

## Root Cause
- User's account was not activated for the Meggie cluster.
- Profile script (`/etc/profile.d/zz-rrze-local.sh`) was not executed correctly during login, causing module loading issues.

## Solution
- HPC Admin activated the user's account for the Meggie cluster.
- HPC Admin suggested manually sourcing the profile script to resolve module loading issues:
  ```bash
  source /etc/profile.d/zz-rrze-local.sh
  ```

## General Learnings
- Ensure user accounts are activated for the specific cluster they intend to use.
- Verify that necessary profile scripts are executed during login for proper module loading.
- Check for any warnings or errors during login that might indicate issues with profile script execution.

## Related Documentation
- [Account Management](link-to-account-management-docs)
- [Module System](link-to-module-system-docs)
- [SLURM Job Submission](link-to-slurm-job-submission-docs)
---

### 2025012442002282_HPC%20problem.md
# Ticket 2025012442002282

 ```markdown
# HPC Support Ticket Analysis

## Subject: HPC Problem

### Keywords:
- HPC Account
- GPU Access
- Interactive Jobs
- salloc
- Account Activation

### Summary:
A user with GPU access encountered issues running interactive jobs using `salloc`. The user provided a screenshot of the error and requested assistance.

### Problem:
- User unable to run interactive jobs using `salloc`.
- Error message attached in the screenshot.

### Root Cause:
- The user's account was created on the same day and required additional time for full activation.
- The documentation mentioned that it takes until the next day for the account to be completely set up and cluster access to be possible.

### Solution:
- Inform the user that the account needs until the next day to be fully functional.
- Refer to the documentation for account activation details.

### Lessons Learned:
- Newly created accounts may not be fully functional until the next day.
- Ensure users are aware of the account activation timeline.
- Documentation should clearly state that cluster access includes both SSH login and Slurm jobs.

### Additional Notes:
- The user was able to log in to the frontend node but could not run Slurm jobs.
- The documentation should be reviewed and rephrased if necessary to clarify the account activation process.

### References:
- [HPC Portal Documentation](https://doc.nhr.fau.de/hpc-portal/#the-user-tab)
```
---

### 2025010942003416_access%20gracehop1_gracesup1%20on%20testfront.md
# Ticket 2025010942003416

 ```markdown
# HPC Support Ticket: Access to gracehop1/gracesup1 on testfront

## Keywords
- Account activation
- Job submission
- Invalid account
- Allocation error
- testfront cluster
- gracehop1
- gracesup1

## Problem Description
User unable to submit jobs on `testfront` cluster, specifically for `gracehop1` and `gracesup1`. Error message indicates an invalid account or account/partition combination.

## Root Cause
User's account was not activated for the specified partitions on the `testfront` cluster.

## Solution
HPC Admin activated the user's account for the required partitions, allowing job submission.

## Lessons Learned
- Ensure user accounts are properly activated for specific partitions before attempting job submissions.
- Invalid account or account/partition combination errors typically indicate a need for account activation or configuration.

## Ticket Status
Problem resolved -> Ticket closed.
```
---

### 42288123_queing-system%20f%C3%83%C2%BCr%20mfbi17-account.md
# Ticket 42288123

 ```markdown
# HPC Support Ticket: Queuing System Issue for New Account

## Keywords
- Queuing System
- Account Permissions
- Emmy-Cluster
- User Authorization

## Problem Description
- User encountered issues with the queuing system when attempting to submit jobs from a new account (`mfbi17`).
- The user was previously able to submit jobs from an old account (`bctc20`).
- The new account appeared to lack the necessary permissions to submit jobs.

## Root Cause
- The new account (`mfbi17`) was not initially authorized to submit jobs on the Emmy-Cluster.

## Solution
- HPC Admin added the new account (`mfbi17`) to the list of authorized users for the Emmy-Cluster.

## Lessons Learned
- Ensure new accounts are properly authorized for the relevant clusters before users attempt to submit jobs.
- Verify account permissions when users report issues with the queuing system.

## Actions Taken
- HPC Admin added the new account to the list of authorized users for the Emmy-Cluster.

## Follow-Up
- Confirm with the user that they can now submit jobs successfully from the new account.
```
---

### 2024100242002361_Invalid%20account%20or%20account_partition%20combination%20specified.md
# Ticket 2024100242002361

 ```markdown
# HPC Support Ticket: Invalid Account or Account/Partition Combination Specified

## Keywords
- Invalid account
- Account/partition combination
- Testcluster
- salloc
- Freigeschalten

## Problem Description
User attempted to use a new account on the test cluster but received an error message: "Invalid account or account/partition combination specified." The user provided their `salloc` command for reference.

## Root Cause
The new account was not manually enabled on the test cluster.

## Solution
HPC Admin manually enabled the account on the test cluster.

## Lessons Learned
- New accounts on the test cluster require manual activation by HPC Admins.
- Users should verify account status before attempting to use resources.
- Proper communication with HPC support can resolve account-related issues quickly.

## Example `salloc` Command
```bash
salloc --nodelist=rome2 --time=60 --exclusive
```

## Resolution
After manual activation by the HPC Admin, the user confirmed that the account was working correctly.
```
---

### 2024071742001073_Node%20Allocation%20on%20Test%20Cluster.md
# Ticket 2024071742001073

 # Node Allocation on Test Cluster

## Keywords
- Node allocation
- Test cluster
- `salloc` command
- Invalid account/partition combination
- Access permissions

## Problem
- **User Issue**: Unable to allocate nodes on the Test cluster.
- **Command Used**: `salloc --nodes=1 -w lukewarm --time 00:10:00`
- **Error Message**: `salloc: error: Job submit/allocate failed: Invalid account or account/partition combination specified`
- **Required Access**: Nodes of "lukewarm" and "warmup".

## Root Cause
- User does not have default access to the Test cluster.

## Solution
- **Action Taken**: HPC Admin enabled the user's account to use the Test cluster.
- **Documentation Reference**: As stated in the documentation, users do not get access to the Test cluster by default.

## General Learnings
- Users need explicit permission to access the Test cluster.
- Ensure the account has the necessary permissions for the specified partitions.
- Refer to the documentation for default access settings.

## Next Steps for Support
- Verify user permissions for specific clusters and partitions.
- Enable access if required and confirm with the user.
- Update documentation if necessary to reflect current access policies.
---

