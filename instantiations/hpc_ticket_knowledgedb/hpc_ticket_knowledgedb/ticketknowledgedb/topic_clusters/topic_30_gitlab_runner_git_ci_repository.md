# Topic 30: gitlab_runner_git_ci_repository

Number of tickets: 25

## Tickets in this topic:

### 2023012042001696_Account%20abgelaufen.md
# Ticket 2023012042001696

 # HPC Support Ticket: Account Expired

## Keywords
- Account expiration
- Account reactivation
- Gitlab CI
- Testcluster access
- Job submission error

## Problem
- User's HPC account (iwia043h) expired.
- User has a new account (igwr049h) but it lacks access to the testcluster nodes.
- Job submission results in error: `salloc: error: Job submit/allocate failed: Invalid account or account/partition combination specified`.
- Gitlab CI integration with RRZE-Testrunner needs to continue functioning.

## Solution
- **Account Reactivation**: The HPC Admin manually extended the expiration date of the old account (iwia043h) to allow temporary access.
- **Gitlab CI**: The user was informed that the Gitlab CI pipeline needs to be transferred to another active account to continue functioning after the old account expires again.

## General Learnings
- Account expiration can disrupt access to HPC resources and integrated services like Gitlab CI.
- Reactivating an expired account is a viable temporary solution.
- For long-term solutions, transferring services to a new, active account is necessary.
- Communication with the user about future steps is crucial for maintaining service continuity.

## Actions Taken
- HPC Admin extended the expiration date of the old account (iwia043h).
- User was advised to plan for transferring the Gitlab CI pipeline to another account.

## Follow-up
- The ticket was closed after the user confirmed that the account reactivation worked.
- The user will discuss and plan for a long-term solution regarding the Gitlab CI pipeline.
---

### 2024031342003602_Request%20for%20HPC%20access%20for%20partcipants%20for%20CI_CD%20workshop.md
# Ticket 2024031342003602

 ```markdown
# HPC Support Ticket: Request for HPC Access for Participants for CI/CD Workshop

## Summary
- **Subject:** Request for HPC access for participants for CI/CD workshop
- **Course Name:** Maximizing CFD Code Efficiency: A workshop on Continuous Integration, Benchmarking, and Testing in Cluster Environments
- **Date:** 25.03.24
- **Expected Participants:** 25

## Key Points
- **HPC Accounts:** Participants require HPC accounts and CX usage access.
- **GitLab Access:** External users cannot get accounts on the internal GitLab instance (gitlab.rrze.fau.de). The alternative is gitos.rrze.fau.de.
- **SSH Keys:** Setting up SSH key pairs and CX usage access requires time.
- **Solution:** Create 25 repositories on gitos.rrze.fau.de and send out invites on the course date. Set up CX stuff inside the repos before March 25.

## Issues and Solutions
1. **Issue:** Error in creating directory.
   - **Solution:** The issue was resolved by the HPC Admin.

2. **Issue:** Another error encountered by the user.
   - **Solution:** The issue was resolved by the HPC Admin.

## Instructions for Participants
- **HPC Account:** Use the HPC account `z46r0000` for the workshop (AUTH_USER=z46r0000).
- **Node Distribution:** Scatter users over different nodes (SLURM_NODELIST=<hostname>):
  - hasep1
  - broadep2
  - ivyep1
  - naples1
  - skylakesp2
- **Job Tags:** All jobs that should run on the testcluster require the 'testcluster' tag:
  ```yaml
  job:
    tags:
      - testcluster
  ```

## Conclusion
- **Collaboration:** The HPC Admin and the user collaborated to resolve issues and ensure a smooth workshop.
- **Testing:** The user was advised to test the setup before the workshop and report any problems.
```
---

### 2025030542003223_Gitlab%20SSH.md
# Ticket 2025030542003223

 ```markdown
# HPC-Support Ticket: Gitlab SSH Access

## Keywords
- SSH access
- Gitlab
- VPN
- Internal server
- Public SSH key

## Problem
- User unable to access internal FAU Gitlab repositories via SSH from the lab server (`mad-srv.informatik.uni-erlangen.de`).
- Access works only when connected to VPN on the laptop.
- Public SSH key generated on HPC and added to Gitlab, but access still not working.

## Root Cause
- The internal Gitlab server access configuration and requirements are not managed by the HPC support team.

## Solution
- Direct questions about accessing the internal Gitlab server to the administrators of that server.
- HPC support does not manage the internal Gitlab server.

## General Learning
- For issues related to internal services like Gitlab, users should contact the administrators of those specific services.
- HPC support focuses on HPC-related issues and not on external or internal services managed by other departments.
```
---

### 2024031242003426_Request%20for%20access%20to%20the%20Test%20cluster%20and%20Cx%20usage%20-%20LSS-Kurs.md
# Ticket 2024031242003426

 # HPC Support Ticket: Request for Access to the Test Cluster and Cx Usage

## Summary
- **User Request**: Access to the Test Cluster and Cx usage for a CX workshop.
- **Issues Encountered**: Authentication errors with SSH keys and environment variables.
- **Solution**: Correct formatting of SSH keys and removal of newlines in environment variables.

## Keywords
- HPC Access
- SSH Key Pair
- GitLab CI
- Authentication Error
- Environment Variables
- Cx Usage

## What to Learn
- **SSH Key Pair**: Ensure SSH keys are generated without a passphrase for GitLab CI.
- **Key Formatting**: The private key must be surrounded by `-----BEGIN OPENSSH PRIVATE KEY-----` and `-----END OPENSSH PRIVATE KEY-----`.
- **Environment Variables**: Ensure no newlines are present in environment variables.
- **Configuration Mistakes**: HPC Admins may need to check for configuration errors on their end.

## Ticket Conversation

### Initial Request
- **User**: Requested access to the Test Cluster and Cx usage for a CX workshop.
- **HPC Admin**: Provided instructions for setting up SSH keys and requesting Cx usage.

### Issues and Solutions
- **User**: Encountered authentication errors with SSH keys.
- **HPC Admin**: Suggested correcting the format of the SSH key and removing newlines from environment variables.
- **User**: Continued to encounter errors.
- **HPC Admin**: Identified a configuration mistake and resolved it.
- **User**: Successfully accessed the Cx services after correcting the SSH key format and environment variables.

## Root Cause of the Problem
- **Incorrect SSH Key Format**: The private key was not formatted correctly.
- **Newlines in Environment Variables**: Environment variables contained newlines, causing authentication errors.

## Solution
- **Correct SSH Key Format**: Ensure the private key is formatted with the correct headers and trailers.
- **Remove Newlines**: Ensure no newlines are present in environment variables.

## Conclusion
- **User**: Successfully accessed the Cx services after following the provided solutions.
- **HPC Admin**: Confirmed the resolution and offered further assistance if needed.

This documentation can be used to resolve similar issues in the future by ensuring correct SSH key formatting and environment variable settings.
---

### 2023071142002754_git%20command%20not%20found.md
# Ticket 2023071142002754

 ```markdown
# HPC-Support Ticket: git command not found

## Keywords
- git
- module
- venv
- Fehlermeldung
- HPC

## Problem
- User received an error message when trying to install a git branch for a virtual environment (venv).
- The error message indicated that the `git` command was not found.

## Root Cause
- The `git` command was not available because the necessary module was not loaded.

## Solution
- Load one of the available git modules using the `module` command.
  ```bash
  module avail git
  ```
  Available modules:
  ```
  git/2.31.1
  git/2.35.2
  ```

## Steps Taken
1. User reported the issue with a screenshot of the terminal error.
2. HPC Admin suggested loading one of the available git modules.
3. User confirmed that loading the module resolved the issue.

## General Learning
- Ensure that necessary modules are loaded before running commands that depend on them.
- Use the `module avail` command to check available modules.

## Ticket Status
- The ticket was closed after the user confirmed that the solution worked.
```
---

### 2022022742000451_Anfrage%20Gitlab%20Cx.md
# Ticket 2022022742000451

 ```markdown
# HPC Support Ticket: Gitlab Cx Request

## Keywords
- Gitlab Cx
- SSH Key
- Masterarbeit
- HPC Account
- Repository
- Public Key

## Summary
A user requested access to Gitlab Cx for their master's thesis. The user provided their HPC account name, repository URL, and attached a public key.

## Root Cause
The user needed access to Gitlab Cx for their master's thesis and required their SSH key to be registered for the repository.

## Solution
The HPC Admin registered the user's SSH key for the repository, enabling them to use the HPC Cx Runner.

## Lessons Learned
- Users need to provide their HPC account name, repository URL, and public key when requesting access to Gitlab Cx.
- HPC Admins can register SSH keys for users to enable access to the HPC Cx Runner.
- Proper communication and documentation of the request and resolution process are essential for efficient support.
```
---

### 2023072742003171_Gitlab%20Cx%20auf%20dem%20Testcluster.md
# Ticket 2023072742003171

 # HPC Support Ticket: Gitlab CI on Test Cluster

## Keywords
- Gitlab CI
- HPC Runner
- SSH Key
- Project Access

## Summary
A user requested access to use Gitlab CI with HPC Runner for a specific project. The user provided their HPC account name and public SSH key.

## Root Cause
- User needed Gitlab CI access for their project.

## Solution
- HPC Admin granted access to the project for the Gitlab HPC Runner.

## What Can Be Learned
- Users need to provide their HPC account name and public SSH key to request Gitlab CI access.
- HPC Admins can grant access to projects for the Gitlab HPC Runner.

## Follow-Up Actions
- None specified.

## Related Links
- [Gitlab Project](https://gitlab.rrze.fau.de/ob28imeq/pystencils-cb)
- [HPC Support Email](mailto:support-hpc@fau.de)
- [HPC Website](https://hpc.fau.de/)
---

### 2020121742001043_Access%20to%20Lammps.md
# Ticket 2020121742001043

 # HPC Support Ticket: Access to LAMMPS

## Keywords
- LAMMPS
- Software Installation
- Spack
- Git
- HPC Cluster
- Emmy Frontend

## Summary
A user requested access to LAMMPS software on the HPC cluster. The HPC Admin provided instructions for installing LAMMPS using Spack, but the initial instructions did not work due to missing Git on the Emmy frontend. The Admin then provided corrected instructions.

## Root Cause of the Problem
- Missing Git on the Emmy frontend.
- Incorrect initial installation instructions.

## Solution
1. **Access the Emmy frontend:**
   ```bash
   ssh iwtm015h@cshpc.rrze.uni-erlangen.de
   ```

2. **Create a directory for software installation:**
   ```bash
   mkdir soft
   cd soft
   ```

3. **Clone the Spack repository:**
   ```bash
   git clone "https://github.com/spack/spack.git"
   ```

4. **Access the Emmy cluster:**
   ```bash
   ssh emmy
   ```

5. **Navigate to the Spack binary directory and install LAMMPS:**
   ```bash
   cd soft/spack/bin
   ./spack install lammps
   ```

6. **Optional: Install specific LAMMPS packages by adding flags (e.g., `+manybody`, `+cuda`) to the install command.**

## Additional Information
- **LAMMPS Packages:** A list of available packages is provided in the email and can be found in the [LAMMPS documentation](https://lammps.sandia.gov/doc/Packages_standard.html).
- **Installation Directory:** The LAMMPS installation can be found in `~/soft/spack/opt/spack/linux-centos7-ivybridge/gcc-4.8.5/lammps-20200721-*/bin`.

## Follow-Up
- If the installation still fails, provide the error message and the command that caused the error for further assistance.

## Conclusion
The user was provided with corrected instructions to install LAMMPS using Spack. The HPC Admin also offered further assistance if needed.
---

### 2022042642002564_GIT%20on%20HPC%20cluster%20possible%3F.md
# Ticket 2022042642002564

 # HPC Support Ticket: GIT on HPC Cluster

## Keywords
- Git
- Module System
- Permissions
- $WORK Directory

## Problem
- User unable to use Git to clone a repository in their $WORK directory.
- User assumes they lack permissions to install Git.

## Root Cause
- User unaware of the module system for accessing Git.

## Solution
- Git is available as a module on the HPC cluster.
- User should use the command `module avail git` to load the Git module.
- Documentation on the module system can be found [here](https://hpc.fau.de/systems-services/systems-documentation-instructions/environment/#modules).

## General Learnings
- Always check if the required software is available as a module.
- Use the `module avail` command to list available modules.
- Refer to the HPC documentation for detailed instructions on using the module system.
---

### 2023101742004977_Git%20LFS.md
# Ticket 2023101742004977

 ```markdown
# HPC-Support Ticket: Git LFS

## Keywords
- Git LFS
- OS-Paket
- Login-Knoten

## Problem
- User requested the availability of Git LFS, possibly as part of the "git" module.

## Solution
- Git LFS is now available as an OS package on the login nodes.

## General Learnings
- Git LFS can be requested and installed as an OS package on HPC systems.
- Users should check the availability of requested software on login nodes.
```
---

### 2023013042000276_Git%20auf%20Alex%20-%20b143dc20.md
# Ticket 2023013042000276

 # HPC Support Ticket: Git auf Alex

## Keywords
- Git
- Module
- Alex
- FAU

## Problem
- User unable to find or use Git on Alex.

## Solution
- Git is available as a module on Alex.
- To use Git, the user needs to load the module using the command:
  ```bash
  module add git
  ```

## General Learning
- Modules are used to manage software packages on HPC systems.
- Users should check if the required software is available as a module and load it using the `module add` command.

## Roles Involved
- HPC Admins
- 2nd Level Support Team
- Head of the Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support
- Software and Tools Developer

## Related Links
- [FAU HPC Support](mailto:support-hpc@fau.de)
- [FAU HPC Website](https://hpc.fau.de/)
---

### 2022051942000934_SSH%20key%20f%C3%83%C2%BCr%20Gitlab%20HPC%20Runner.md
# Ticket 2022051942000934

 ```markdown
# HPC-Support Ticket Conversation: SSH Key for GitLab HPC Runner

## Keywords
- SSH Key
- GitLab
- HPC Runner
- CI (Continuous Integration)
- Public Key
- Repository
- Username

## Summary
A user requested to use the Cx Service in a specific GitLab repository and provided their HPC username and public SSH key. The HPC Admin confirmed the key was registered and CI should now function.

## Root Cause
- User needed to register an SSH key for accessing a GitLab repository to enable CI.

## Solution
- The HPC Admin registered the provided SSH key, enabling CI for the user's repository.

## General Learnings
- Users need to provide their HPC username and public SSH key to access GitLab repositories for CI.
- HPC Admins can register SSH keys to enable CI for users.
- Ensure the certificate has not expired when registering SSH keys.
```
---

### 2023013142001201_Gitlab%20Hpc%20runner.md
# Ticket 2023013142001201

 ```markdown
# HPC Support Ticket: Gitlab HPC Runner

## Keywords
- Gitlab Runner
- SSH Key
- HPC Account
- Repository Access

## Summary
A user requested to use the Cx Service with the HPC Gitlab Runner for a specific project. The user provided their HPC account details and the public part of their SSH key.

## Root Cause
The user needed access to the Gitlab Runner for their project.

## Solution
The HPC Admin registered the provided SSH key for the repository, enabling the user to utilize the Gitlab Runner.

## What Can Be Learned
- Users need to provide their HPC account details and SSH key to gain access to the Gitlab Runner.
- HPC Admins can register SSH keys to grant repository access.
- Proper communication and key management are essential for setting up Gitlab Runner access.
```
---

### 2023072842001161_GitLab.md
# Ticket 2023072842001161

 ```markdown
# HPC Support Ticket: GitLab Repository Clone Issue

## Keywords
- GitLab
- SSH Key
- VPN
- Hostname Resolution
- HPC Cluster

## Problem Description
- User needs to clone a GitLab repository.
- SSH key has been generated and added to the GitLab account.
- Accessing `git01.iis.fhg.de` requires a VPN with a changing password.
- Without VPN, user encounters "could not resolve hostname" error.
- User is unsure how to handle VPN on HPC clusters.

## Root Cause
- VPN requirement for accessing the GitLab server.
- Changing password for VPN access.

## Solution
- **VPN Configuration**: Ensure VPN is correctly configured on the HPC cluster.
- **Password Management**: Implement a method to handle changing VPN passwords.
- **SSH Key Verification**: Verify that the SSH key is correctly added to the GitLab account.

## General Learnings
- VPN configuration is crucial for accessing certain resources on HPC clusters.
- Handling changing passwords for VPN access requires a robust management system.
- Proper SSH key setup is essential for secure and seamless repository access.
```
---

### 2021100442002916_Git%20module%20auf%20Meggie%20Rechenknoten.md
# Ticket 2021100442002916

 # HPC Support Ticket: Git Module Request on Meggie

## Keywords
- Git module
- Meggie
- Rechenknoten
- HPC-Team
- FAU Erlangen-Nürnberg

## Summary
A user requested the availability of a Git module on the Meggie compute nodes. The HPC Admin promptly provided the necessary module.

## Problem
- **Root Cause:** User needed a Git module available on the Meggie compute nodes.

## Solution
- **Action Taken:** HPC Admin provided the Git module `git/2.29.0-gcc11.1.0-bxi3mt`.

## What Can Be Learned
- **Request Handling:** HPC Admins can quickly respond to requests for software modules on compute nodes.
- **Module Availability:** Ensure that commonly requested software modules are available and accessible on compute nodes.

## Follow-Up
- **User Feedback:** The user expressed gratitude for the quick response and availability of the Git module.

## General Notes
- **Efficiency:** The quick resolution highlights the efficiency of the HPC support team.
- **User Satisfaction:** Prompt responses to user requests enhance user satisfaction and productivity.

---

This documentation can serve as a reference for future requests regarding software module availability on compute nodes.
---

### 2023111542002935_Continuous%20Benchmarking%3A%20Unable%20to%20read%20working%20directory%20when%20fetching%20git%20pr.md
# Ticket 2023111542002935

 ```markdown
# Continuous Benchmarking: Unable to read working directory when fetching git project

## Problem Description
- User unable to clone git repositories on GitLab runners.
- Error message: `fatal: Unable to read current working directory: No such file or directory`.
- Issue occurs during the cloning/fetching process.

## Root Cause
- The issue is related to the `GIT_STRATEGY: clone` setting in the GitLab CI/CD pipeline.
- The problem persists even with a minimal working example.

## Troubleshooting Steps
1. **Initial Investigation**:
   - User tried to follow the path to the working directory interactively on the front-end node without encountering the issue.
   - User provided a log of an exemplary pipeline run.

2. **HPC Admin Response**:
   - Requested relevant parts of the `gitlab-ci.yml` and the output of the pipeline.
   - Suggested using a minimal working example to isolate the issue.

3. **Further Investigation**:
   - HPC Admin identified that the issue is not with the custom runner scripts.
   - Other pipelines on the test cluster were running without issues.
   - HPC Admin suspected the problem might be with the `gitlab-cb.yml` stages or includes.

4. **Workaround**:
   - HPC Admin suggested using `GIT_STRATEGY: fetch` as a workaround.
   - This workaround resolved the issue for the user.

5. **Final Resolution**:
   - A workaround was implemented in the custom runner scripts to fix the issue with `GIT_STRATEGY: clone`.
   - The problem was traced to a known issue in GitLab, which was recently fixed.

## Solution
- Use `GIT_STRATEGY: fetch` as a temporary workaround.
- Apply the workaround in the custom runner scripts to fix the issue with `GIT_STRATEGY: clone`.

## Keywords
- GitLab CI/CD
- Git clone error
- Working directory issue
- GIT_STRATEGY
- Custom runner scripts
- Continuous benchmarking
```
---

### 2024100242005448_Assistance%20with%20Installing%20Rye%20Package%20Manager%20and%20Using%20Git%20via%20CLI.md
# Ticket 2024100242005448

 ```markdown
# HPC Support Ticket Conversation Summary

## Subject: Assistance with Installing Rye Package Manager and Using Git via CLI

### Keywords:
- Rye Package Manager
- Persistent Installation
- Git CLI
- Authentication
- Github CLI Tools
- Home Directory

### Problem:
- User encounters issues with Rye installation not persisting between sessions.
- User needs guidance on using Git via CLI, specifically with authentication for pushing to a remote repository.

### Root Cause:
- Rye installation not persisting due to incorrect installation location.
- User confusion regarding Git authentication and installation of Github CLI tools.

### Solution:
- **Rye Installation:**
  - Install Rye in the `$HOME` directory to ensure persistence across sessions.
  - Configuration files will be located in `$HOME/.rye`.

- **Git and Github CLI Tools:**
  - Git is available by default on the HPC system.
  - Github CLI tools are not provided but can be installed in the `$HOME` directory.
  - Use the 'linux amd64' version from the Github releases page.
  - Authentication for Git can be configured using SSH keys or personal access tokens.

### General Learnings:
- Always install user-specific software in the `$HOME` directory for persistence.
- Understand the difference between Git and Github CLI tools.
- Configure Git authentication using SSH keys or personal access tokens for seamless interaction with remote repositories.

### Additional Notes:
- Users do not have admin privileges to install software using OS package managers (apt, yum, dnf, etc.).
- Ensure proper configuration and installation paths for user-specific software to avoid reinstallation issues.
```
---

### 2021122042001615_Anfrage%3A%20Zugriff%20NHR%20Testcluster.md
# Ticket 2021122042001615

 # HPC Support Ticket Conversation Summary

## Keywords
- HPC Account
- Gitlab Account
- Testcluster
- Java 8
- Java 11
- sbt
- CI/CD
- SLURM
- SSH Key
- Job Submission
- Drain Status

## General Learnings
- **HPC Account Requirement**: A valid HPC account is required to access the test cluster.
- **Gitlab Account**: Users need to have a Gitlab account on the RRZE Gitlab or use SSO-Login with gitos.rrze.
- **Java Modules**: Only Java 8 is available as a module on the test cluster. Users need to manage their own module tree for other versions.
- **CI/CD Setup**: Users can set up CI/CD pipelines by mirroring their repositories and using custom CI scripts.
- **SLURM Job Submission**: Users need to have the correct account and partition combination to submit SLURM jobs.
- **SSH Key**: Users need to generate an SSH key pair and provide the public key to the HPC Admins for access.
- **Drain Status**: Nodes in drain status are not usable for job submission. Users can filter out these nodes using specific commands.

## Root Causes and Solutions
- **Root Cause**: User did not have an HPC account.
  - **Solution**: User was instructed to create an HPC account.
- **Root Cause**: User needed Java 11 and sbt for their application.
  - **Solution**: User was advised to manage their own module tree for the required dependencies.
- **Root Cause**: User could not submit SLURM jobs due to an invalid account or account/partition combination.
  - **Solution**: User's account was enabled for the test cluster, allowing job submission.
- **Root Cause**: User's CI jobs were stuck due to a node being in drain status.
  - **Solution**: User was advised to change the configuration to use a different node or filter out nodes in drain status.

## Documentation for Support Employees
- **Account Setup**: Ensure users have a valid HPC account and a Gitlab account on the RRZE Gitlab or SSO-Login with gitos.rrze.
- **Module Management**: Inform users about the available modules and advise them to manage their own module tree for additional dependencies.
- **Job Submission**: Assist users with SLURM job submission issues by ensuring they have the correct account and partition combination.
- **SSH Key**: Guide users through generating an SSH key pair and provide the public key to the HPC Admins for access.
- **Drain Status**: Help users filter out nodes in drain status using specific commands to avoid job submission issues.

This summary provides a concise overview of the key points and solutions from the HPC support ticket conversation, serving as a helpful reference for support employees encountering similar issues.
---

### 2024013042002674_Problem%20mit%20Gitlab%20HPC%20Runner.md
# Ticket 2024013042002674

 # HPC Support Ticket: Problem mit Gitlab HPC Runner

## Keywords
- GitLab CI/CD
- SLURM
- Compute Node
- Frontend Node
- GIT_STRATEGY
- module command
- Ubuntu 22.04
- Ansible

## Problem Description
- CI jobs failing when running directly on compute nodes (NO_SLURM_SUBMIT: 0).
- Jobs running on frontend nodes (NO_SLURM_SUBMIT: 1) work fine.
- Error message received after job start.

## Root Cause
- Initial issue due to a bug in GitLab, which was supposed to be fixed in the current version.
- Later identified as an error in the runner scripts that only appeared when submitting jobs to compute nodes.

## Troubleshooting Steps
1. **GIT_STRATEGY Change**:
   - Suggested changing `GIT_STRATEGY: clone` to `GIT_STRATEGY: fetch` as a workaround.
   - This did not resolve the issue.

2. **Minimal Example**:
   - User provided a minimal example to reproduce the issue.
   - HPC Admin reproduced the problem and identified the error in the runner scripts.

3. **Configuration Update**:
   - HPC Admin updated the configuration to use `/etc/profile.d/zz-rrze-local.sh` instead of `/etc/bash.bashrc.local`.
   - This change was necessary due to an update to Ubuntu 22.04 on the nodes.

## Solution
- The error in the runner scripts was fixed, allowing jobs to be submitted to compute nodes without issues.
- Configuration changes were made to ensure the `module` command works correctly in SLURM jobs.

## Additional Issues
- After fixing the initial problem, a new issue arose with the `module` command not being found.
- This was due to a configuration issue after updating the nodes to Ubuntu 22.04.
- The configuration was updated to include `/etc/profile.d/zz-rrze-local.sh` and ensure it is sourced in interactive SLURM jobs.

## Conclusion
- The initial problem with CI jobs on compute nodes was resolved by fixing the runner scripts.
- The subsequent issue with the `module` command was addressed by updating the configuration to be compatible with Ubuntu 22.04.

## Future Reference
- If similar issues arise, check the runner scripts and ensure the configuration is compatible with the current OS version.
- Verify that the `module` command is correctly sourced in both interactive and non-interactive SLURM jobs.
---

### 2023110942001297_HPC-Cafe%3A%20Cx%20services%20based%20on%20the%20RRZE%20Gitlab%20instances.md
# Ticket 2023110942001297

 # HPC-Support Ticket: GitLab CI Jobs on Cluster

## Keywords
- HPC-Café
- GitLab CI Jobs
- Testcluster
- config.toml
- runner Skripte
- Slurm Jobs
- Frontend
- Authentifizierung
- ssh-key

## Summary
The user attended an HPC-Café session where GitLab CI jobs on the testcluster were demonstrated. The user now wants to set up a similar configuration for another cluster and requested the `/etc/gitlab-runner/config.toml` file and the necessary scripts for `[runners.custom]`.

## Root Cause
The user needs configuration files and scripts to set up GitLab CI jobs on a new cluster.

## Solution
The HPC Admin provided the requested `config.toml` file and the corresponding runner scripts. The admin also explained the setup, including running a runner as root on the frontend, starting Slurm jobs under the respective user, and the possibility of processing tasks directly on the frontend without a Slurm job. Authentication and repository activation are managed through a specific folder structure, a pre-stored ssh-key, and a list of allowed users.

## Additional Information
- The custom runner was primarily developed by an external contributor from the University of Regensburg.
- The admin offered further assistance if the user has any questions about the provided files and scripts.

## Conclusion
The user received the necessary files and information to set up GitLab CI jobs on the new cluster. The admin provided details on the setup and offered support for any further questions.

---

This report can be used as a reference for future support cases involving the setup of GitLab CI jobs on HPC clusters.
---

### 2022042842002373_SSH%20key%20f%C3%83%C2%BCr%20Gitlab%20Cx.md
# Ticket 2022042842002373

 # HPC-Support Ticket Conversation Analysis

## Subject
SSH key für Gitlab Cx

## Keywords
- Continuous Integration (CI)
- Gitlab Cx Services
- SSH key
- Repository
- HPC-Account
- Lizenzschwierigkeiten
- gitos.rrze
- gitlab.rrze
- Lizenzdowngrade
- OpenSource

## Summary
A user requested to use Continuous Integration/Gitlab Cx Services for a specific repository and provided their HPC account name and public SSH key. The HPC Admin informed the user about licensing issues with Gitlab and recommended using gitos.rrze for new repositories. The user decided to keep the repository on gitlab.rrze for learning purposes but noted the recommendation for future projects. The SSH key was successfully registered by the HPC Admin.

## Root Cause of the Problem
- User needed to set up Continuous Integration/Gitlab Cx Services for a repository.
- Licensing issues with Gitlab were causing uncertainty about the future of the service.

## Solution
- The HPC Admin registered the user's SSH key.
- The user was informed about the licensing issues and recommended to use gitos.rrze for future projects.
- The user decided to keep the current repository on gitlab.rrze for learning purposes.

## General Learnings
- Users should be aware of licensing issues affecting services like Gitlab.
- For new repositories, it is recommended to use gitos.rrze due to potential future changes in the Gitlab service.
- The process of registering an SSH key for Continuous Integration services involves providing the key to the HPC Admin.

## Recommendations for Support Employees
- Inform users about any ongoing licensing issues that may affect their use of services.
- Provide clear recommendations for alternative services if the current service is experiencing issues.
- Ensure that SSH keys are properly registered to enable Continuous Integration services.
---

### 2022091242003651_gitk%20on%20meggie.md
# Ticket 2022091242003651

 ```markdown
# HPC-Support Ticket: gitk on meggie

## Keywords
- gitk
- graphical interface
- git
- installation
- Alma8-Loginknoten

## Problem
- User requests the installation of the graphical gitk interface for git on the new installation of meggie.

## Solution
- HPC Admin confirmed that gitk has been installed on all Alma8-Loginknoten.

## What Can Be Learned
- gitk can be installed on Alma8-Loginknoten.
- Users can request specific software installations through support tickets.
- HPC Admin can handle software installation requests efficiently.
```
---

### 2018032042002012_Intel%20Compiler%202018%20up%2001.md
# Ticket 2018032042002012

 # HPC Support Ticket: Intel Compiler 2018 up 01

## Keywords
- Intel Compiler 2018 up 01
- Emmy
- Git
- Gitk
- Meggie
- CentOS-Repo
- Git-gui

## Summary
A user requested the installation of Intel Compiler 2018 up 01 on Emmy and a module for Git with Gitk on Meggie.

## Problem
- User needed Intel Compiler 2018 up 01 on Emmy.
- User requested a module for Git with Gitk on Meggie.
- Git-gui was not functioning as expected.

## Solution
- HPC Admins installed Intel Compiler 2018 up 01 on Emmy.
- Git and Gitk were made available on Meggie directly from the CentOS-Repo without a module.
- Git-gui was identified as a separate package in RHEL and was subsequently provided.

## Lessons Learned
- Intel Compiler versions can be requested and installed on specific HPC systems.
- Git and related tools (Gitk, Git-gui) can be provided directly from the CentOS-Repo.
- Git-gui is a separate package in RHEL and needs to be installed separately.

## Follow-up Actions
- Ensure that users are aware of the availability of Git and related tools directly from the CentOS-Repo.
- Document the installation process for Intel Compilers for future reference.
- Provide clear instructions on how to install and use Git-gui on RHEL systems.
---

### 2020121442002691_GitLab%20CI%20with%20HPC%20Tiny%20GPU.md
# Ticket 2020121442002691

 # HPC-Support Ticket: GitLab CI with HPC Tiny GPU

## Keywords
- GitLab CI
- HPC Cluster
- Singularity Containers
- GitLab Runner
- Torque
- SLURM
- TinyGPU
- Testcluster

## Summary
The user inquired about the possibility of using the HPC cluster in combination with a GitLab CI runner. The user is new to this topic and wanted to know if it is feasible to run a GitLab CI runner on the cluster using their user account. The user is aware that Docker containers are not allowed on the cluster, but Singularity containers are.

## Conversation Highlights
- **Initial Inquiry**: The user asked if it is possible to use the HPC cluster with a GitLab CI runner and if Singularity containers can be configured with GitLab CI runners.
- **Admin Response**: The HPC Admin confirmed that it is possible to start simple jobs on the Testcluster using SLURM. The Admin did not try containers but used the RRZE GitLab instance for internal communication. The Admin mentioned that using Torque would be more complicated compared to SLURM.
- **User Follow-up**: The user requested the installation of a GitLab runner on specific nodes (cshpc or woody) and mentioned the need to start different Singularity containers for different projects.
- **Admin Feedback**: The Admin scheduled a meeting with RRZE Gitlab admins and user groups to discuss the implementation of CI infrastructure. The Admin also provided instructions on how to download and configure the GitLab runner without needing admin privileges.
- **User Acknowledgment**: The user thanked the Admin for the help and confirmed they would try the suggested approach.

## Learnings
- **Feasibility**: It is possible to use the HPC cluster with a GitLab CI runner, but there is no ready-to-use solution.
- **Container Support**: Singularity containers can be used with GitLab CI runners, but starting a Singularity container from within another Singularity container may not be straightforward.
- **Installation**: The GitLab runner can be installed and configured by the user without needing admin privileges by downloading the binary version and creating a configuration file.
- **System Limitations**: Processes that accumulate a specific amount of CPU time are killed by the system on the frontend nodes.
- **Future Plans**: The HPC department is considering providing CI infrastructure and will establish a work group for the actual implementation.

## Solution
- The user can download the GitLab runner binary and configure it in their home directory without needing admin privileges.
- The user can start the GitLab CI runner from a tmux session and let it run in the background until the CI pipeline is started.
- The user should be aware of the system limitations regarding CPU time on the frontend nodes.

## Next Steps
- The HPC department will schedule a meeting with RRZE Gitlab admins and user groups to discuss the implementation of CI infrastructure.
- The user will try the suggested approach and provide feedback.

## Root Cause
- The user needed guidance on how to set up a GitLab CI runner on the HPC cluster and how to configure it to use Singularity containers.

## Resolution
- The HPC Admin provided instructions on how to download and configure the GitLab runner without needing admin privileges.
- The HPC department will discuss the implementation of CI infrastructure and establish a work group for the actual implementation.
---

### 2022041542000523_Gitlab%20Cx.md
# Ticket 2022041542000523

 # HPC Support Ticket Conversation Summary

## Subject: Gitlab Cx

### Keywords:
- Gitlab Runner
- CI/CD
- SSH Key
- Repository
- Testcluster
- SLURM
- Account/Partition Combination

### General Learnings:
- Access to Gitlab Runner on the testcluster for CI/CD requires a specific repository URL.
- SSH keys are assigned to specific repositories and cannot be used across multiple repositories.
- SLURM job submission errors can occur due to invalid account or account/partition combinations.
- Freischaltung (activation) for the testcluster may be required for the user's account.

### Root Cause of the Problem:
- The user's account was not activated for the testcluster, causing SLURM job submission errors.
- The SSH key was not assigned to the new repository after it was moved.

### Solution:
- Activate the user's account for the testcluster.
- Assign the SSH key to the new repository URL.

### Detailed Steps:
1. **Initial Request:**
   - User requested access to the Gitlab Runner on the testcluster for CI/CD.
   - Provided HPC account and SSH public key.

2. **Admin Response:**
   - Informed the user that the SSH key must be associated with a specific repository.
   - Stated that without a repository, CI/CD setup is not possible.

3. **Repository Creation:**
   - User created the repository and provided the URL.
   - Admin assigned the SSH key to the repository.

4. **SLURM Job Submission Error:**
   - User encountered an error when submitting a job: `Invalid account or account/partition combination specified`.
   - Admin identified that the user's account was not activated for the testcluster.

5. **Account Activation:**
   - Admin activated the user's account for the testcluster.
   - User confirmed that the issue was resolved.

6. **Repository Move:**
   - User's repository was moved to a new URL, causing the Gitlab Runner to stop working.
   - Admin reassigned the SSH key to the new repository URL.

### Final Outcome:
- The user's account was successfully activated for the testcluster.
- The SSH key was reassigned to the new repository URL, resolving the Gitlab Runner issue.

### Additional Notes:
- The user's `.gitlab-ci.yml` file was configured correctly.
- The user tested their account by logging into the testcluster and attempting to start an interactive job.

This summary provides a concise overview of the support ticket conversation, highlighting the key steps and solutions for resolving the user's issues.
---

