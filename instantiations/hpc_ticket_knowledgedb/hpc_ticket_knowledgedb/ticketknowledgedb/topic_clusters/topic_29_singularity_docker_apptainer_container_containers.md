# Topic 29: singularity_docker_apptainer_container_containers

Number of tickets: 27

## Tickets in this topic:

### 2016121642001642_Support%20f%C3%83%C2%BCr%20Docker%20oder%20Singularity%3F.md
# Ticket 2016121642001642

 # HPC-Support Ticket Conversation: Support for Docker or Singularity

## Keywords
- Docker
- Singularity
- HPC Systems
- RRZE
- TinyEth
- qsub
- Job Submission

## Summary
- **User Inquiry:** Support for Docker and/or Singularity on HPC systems.
- **HPC Admin Response:** Docker is not supported. Singularity might be supported soon and is currently available for testing on TinyEth.

## Detailed Information
- **Docker Support:** Not available on HPC systems.
- **Singularity Support:** Potentially available soon. Currently accessible on TinyEth for testing.
- **Job Submission:** Use `qsub.tinyeth -lnodes=1:ppn=#:singularity` to submit jobs. Replace `#` with a number between 1 and 12.

## Solution
- **For Singularity:** Use TinyEth for testing. Submit jobs with the command `qsub.tinyeth -lnodes=1:ppn=#:singularity`, where `#` is a number between 1 and 12.

## Notes
- Singularity is in the testing phase and might be fully supported soon.
- Docker is not supported on the HPC systems.

---

This documentation can be used by support employees to address similar inquiries regarding Docker and Singularity support on HPC systems.
---

### 2023032842002042_JobError%281551403%20on%20woody%29.md
# Ticket 2023032842002042

 ```markdown
# HPC-Support Ticket: JobError(1551403 on woody)

## Keywords
- Singularity
- Bind-mounts
- Engine configuration error
- Directory size
- Support email address

## Problem Description
- **User Issue:** Error message "FATAL: while initializing starter command: while copying engine configuration: engine configuration too big > 1048448" when running a job to concatenate files in a 5 GB directory.
- **Root Cause:** The error is related to Singularity's limitation on the number of bind-mounts within a container, which is exceeded by the number of files in the user's directory.

## Solution
- **HPC Admin Response:**
  - Use the official support email address (`@fau.de`) for support requests.
  - The error is due to Singularity's limitation on the number of bind-mounts.
  - No specific flags or package changes are mentioned as a solution.

## General Learnings
- Ensure that support requests are sent from the official email address.
- Singularity has limitations on the number of bind-mounts, which can cause errors when dealing with large directories.
- No specific solution provided; further investigation may be needed to resolve the issue.
```
---

### 2022092842002604_singularity%20problem.md
# Ticket 2022092842002604

 # Singularity/Apptainer Container Issue

## Problem Description
- **Subject:** Singularity problem
- **User Issue:** A Singularity/Apptainer container created as a sandbox does not work on the server. The error message received is:
  ```
  FATAL: failed to open /bin/sh for inspection: failed to open elf binary /bin/sh: open /bin/sh: no such file or directory
  ```
- **User's Local Apptainer Version:** 1.0.1

## Troubleshooting Steps
1. **Check for /bin/sh in the Image:**
   - HPC Admin asked the user to verify if `/bin/sh` exists in the image.
   - User confirmed that the `/bin` directory does not exist.

2. **Debug Output:**
   - User provided the debug output from running `singularity -d exec [...]`.

3. **Image Creation Details:**
   - The image was built from an Arch-Linux image with dependencies installed and code compiled.
   - Command used: `sudo apptainer build --sandbox OUTPUT DEF.def`
   - User's Apptainer version: 1.1.0

4. **Suggestion to Use SIF Image:**
   - HPC Admin suggested creating a SIF image instead of a sandbox and copying it to the target system.

## Solution
- **Root Cause:** The issue was with the use of the `--sandbox` option.
- **Resolution:** Creating a compressed container (as a `.sif` file) resolved the issue.

## Keywords
- Singularity
- Apptainer
- Sandbox
- SIF Image
- `/bin/sh`
- Debug Output

## Lessons Learned
- When creating containers with Singularity/Apptainer, using the `--sandbox` option can lead to issues.
- It is generally recommended to create a SIF image and copy it to the target system.
- Always verify the presence of essential directories and files (e.g., `/bin/sh`) in the container image.

## Conclusion
The problem was resolved by creating a SIF image instead of using the `--sandbox` option. This approach ensures that the container works correctly on the target system.
---

### 2024062042000668_Apptainer_Singularity%20im%20Testcluster%20installieren.md
# Ticket 2024062042000668

 ```markdown
# HPC-Support Ticket: Apptainer/Singularity Installation on Test Cluster

## Keywords
- Apptainer/Singularity
- Test Cluster
- x86 Nodes
- ARM Nodes
- Ansible
- Installation
- Configuration

## Problem
- **Root Cause**: Apptainer/Singularity was not installed on the x86 nodes in the test cluster.
- **User Report**: The user noticed the absence of Apptainer/Singularity on the `skylakesp2` node.

## Solution
- **Action Taken**: The HPC Admin integrated Apptainer/Singularity into the Ansible configuration.
- **Result**: Apptainer/Singularity was installed on all active nodes (`bergamo1`, `euroyale`, `genoa1`, `genoa3`, `gracehop1`, `grecesup1`, `lukewarm`, `warmup`).
- **Future Proofing**: The installation will automatically occur after any future reinstallations.

## General Learning
- **Ansible Integration**: Software installations can be managed and automated using Ansible.
- **Automatic Reinstallation**: Proper configuration in Ansible ensures that software is reinstalled automatically after system reinstallations.
- **Node-Specific Installations**: Installations can be targeted to specific node architectures (e.g., x86, ARM).
```
---

### 2017060142001984_Singularity.md
# Ticket 2017060142001984

 # HPC Support Ticket: Singularity Container Setup

## Keywords
- Singularity
- Container
- OpenCV
- Python dependencies
- Queueing system
- Cache directories
- Job script
- SLURM

## Problem
- User needs to build a Singularity container for an application with OpenCV and various Python dependencies.
- Requires guidance on the appropriate Singularity version to use.
- Needs assistance with the new queueing system and managing cache directories per job.

## Solution
- **Singularity Version**: Meggie is updated to Singularity 2.3. While not extensively tested, it should be used.
- **Mounting Directories**: `/apps`, `/home`, and `/lxfs` are automatically mounted into the container.
- **Root Privileges**: Bootstrap requires root privileges; import from Docker does not.
- **Job Script Example**:
  ```bash
  #!/bin/bash -l
  ### One compute node for 10 hours (hh:mm - no :ss!)
  #SBATCH --nodes=1
  #SBATCH --time=10:00
  #SBATCH --job-name=of-container
  #SBATCH --export=NONE
  unset SLURM_EXPORT_ENV
  singularity exec /apps/Singularity/openfoam-1612plus.img ls -l /opt
  ```

## General Learnings
- Singularity 2.3 is available but not extensively tested.
- Importing from Docker does not require root privileges, unlike bootstrap.
- Basic SLURM job script provided for running Singularity containers.
- Automatic mounting of `/apps`, `/home`, and `/lxfs` directories.

## Roles
- **HPC Admins**: Provide guidance on Singularity versions and job script examples.
- **2nd Level Support Team**: Assist with specific issues related to Singularity and SLURM.
- **Head of Datacenter**: Oversee overall operations.
- **Training and Support Group Leader**: Manage training and support activities.
- **Software and Tools Developer**: Develop and maintain software tools.

## Root Cause
- User requires quick setup of a Singularity container for an upcoming conference and needs guidance on version compatibility and job scripting.

## Solution Found
- Use Singularity 2.3.
- Provide a minimal job script example for SLURM.
- Inform about automatic mounting of directories and root privilege requirements.
---

### 2024111142002048_Singularity%20auf%20Testcluster%20Frontend%20defekt.md
# Ticket 2024111142002048

 ```markdown
# HPC Support Ticket: Singularity auf Testcluster Frontend defekt

## Keywords
- Singularity
- Apptainer
- Ubuntu 24.04 Update
- AppArmor Configuration
- Permission Denied
- User Namespace Mappings
- Fakeroot
- Build Command

## Problem Description
The user reported that running an Apptainer container on the test cluster frontend resulted in permission errors:
```
ERROR : Could not write info to setgroups: Permission denied
ERROR : Error while waiting event for user namespace mappings: Bad file descriptor
```

## Root Cause
- The issue was traced to the Ubuntu 24.04 update, which introduced new requirements for Apptainer.
- Apptainer now requires a specific AppArmor configuration to function correctly, which was not automatically provided by the package.

## Solution
- The HPC Admin team identified that the AppArmor configuration for Apptainer was missing and added it to the Ansible distribution.
- However, the `apptainer build` command still encountered issues due to the user namespace restrictions.

## Additional Information
- The `apptainer build` command uses a special profile ("unprivileged_userns") that does not inherit all permissions from Apptainer.
- The recommendation is to perform the `apptainer build` on a separate machine rather than on the cluster to avoid security risks.

## Status
- The ticket was left open for further investigation after the holidays.
- The user reported similar issues on another machine (icx36), indicating a broader problem with the `apptainer build` command and fakeroot.

## Conclusion
- The Ubuntu 24.04 update introduced new requirements for Apptainer, specifically related to AppArmor configuration.
- The `apptainer build` command has additional security considerations and may need to be performed on a separate machine.
```
---

### 2017061642001607_singularity%20bindings%20f%C3%83%C2%BCr%20_scratch.md
# Ticket 2017061642001607

 # HPC Support Ticket: Singularity Bindings for /scratch

## Keywords
- Singularity
- Bind points
- /scratch
- TinyFAT
- TinyEth
- Meggie
- LiMa
- Emmy
- MKL

## Problem
- User unable to access `/scratch` from within Singularity container on TinyFAT and TinyEth clusters.
- User inquires about increasing job limits on Meggie.
- User asks about Singularity availability on older clusters (Woody, LiMa, Emmy).

## Root Cause
- `/scratch` was not included as a system bind point in Singularity configuration.

## Solution
- HPC Admin added `/scratch` as a system bind point, making it accessible within Singularity containers on TinyFAT and TinyEth.
- Unofficial Singularity 2.3.2 installed on LiMa and Emmy for testing.

## Additional Notes
- User noticed an increase in job limits on Meggie but the cause was not discussed.
- HPC Admin provided suggestions for using MKL with Singularity.
- Further discussion on Singularity and MKL planned for a later phone call.

## General Learnings
- Users may require access to specific directories (e.g., `/scratch`) within Singularity containers.
- System bind points can be added to Singularity configuration to meet user needs.
- Older clusters may require reboots to install or update software like Singularity.
- HPC Admin may provide guidance on using specific software (e.g., MKL) with Singularity.
---

### 2023042442003378_Server%20and%20host%20for%20the%20May%2012th%20FRASCAL%20workshop.md
# Ticket 2023042442003378

 ```markdown
# HPC Support Ticket Conversation Summary

## Subject: Server and Host for the May 12th FRASCAL Workshop

### Keywords:
- FRASCAL Workshop
- MoFEM
- Singularity
- Docker
- JupyterHub
- SSH
- Slurm
- FAU HPC
- Login Nodes
- Compute Nodes
- Temporary Accounts

### General Learnings:
- **Cluster Selection**: The FRASCAL-FE project applied for compute time at the `fritz-cluster`.
- **Container Solutions**: FAU HPC does not offer Docker; the only container solution available is Apptainer/Singularity.
- **Login Instructions**: Users should refer to the FAQ for login instructions.
- **Singularity Usage**: Singularity can be run directly without loading a module on the `fritz-cluster`.
- **Interactive Jobs**: Users can use interactive jobs on the `fritz-cluster` or a `fritz-frontend`.
- **JupyterHub**: Running JupyterHub on login nodes can be subject to automatic process termination after 1 hour. Mitigated by running JupyterHub in a Slurm batch job.
- **User Authentication**: JupyterHub running in user space cannot spawn processes as other users.
- **Port Forwarding**: Users can forward JupyterHub ports to their laptops or run a JupyterHub accessible only on campus.
- **Security Concerns**: Binding ports to the IP of the host without authentication can be a security issue.

### Root Causes of Problems:
- **Module Load Error**: The user encountered an error when trying to load the Singularity module.
- **Workshop Details**: There was confusion regarding the planned activities and resource requirements for the FRASCAL workshop.

### Solutions:
- **Singularity Module Error**: The user was advised to run Singularity directly without loading a module on the `fritz-cluster`.
- **Workshop Planning**: Detailed planning and resource requirements were requested to find suitable alternatives for the workshop.
- **JupyterHub Access**: Users can run JupyterHub in a Slurm batch job to avoid automatic termination on login nodes.
- **Port Forwarding**: Users can forward JupyterHub ports to their laptops or run a JupyterHub accessible only on campus.

### Additional Notes:
- **Documentation**: Users should refer to the FAQ for detailed login instructions.
- **Workshop Links**: Provided links for Singularity and Docker usage in MoFEM.
- **Security**: Ensure proper authentication and security measures when running services on compute nodes.
```
---

### 2021032842000744_Error%20running%20singularity%20on%20emmy.md
# Ticket 2021032842000744

 ```markdown
# HPC-Support Ticket: Error Running Singularity on Emmy

## Subject
Error running singularity on emmy

## User Issue
- User attempted to use Singularity with an Ubuntu image.
- Error encountered: `FATAL: container creation failed: mount /proc/self/fd/9->/var/singularity/mnt/session/rootfs error: while mounting image /proc/self/fd/9: squashfs filesystem seems not enabled and/or supported by your kernel`.

## HPC Admin Response
- Admin successfully reproduced the error on the emmy frontend.
- Suggested clearing the Singularity cache (`~/.singularity/cache`).
- Requested verbose output using `-vvvv` for further diagnosis.

## User Follow-Up
- User cleared the Singularity cache but the error persisted.
- Provided verbose output which confirmed the initial error.

## HPC Admin Diagnosis
- Identified the issue as specific to `emmy1`.
- Suggested using `emmy2` as a temporary workaround while a fix is implemented.

## Root Cause
- The issue is specific to `emmy1`, likely related to kernel support for the squashfs filesystem.

## Solution
- Use `emmy2` as a temporary workaround.
- HPC Admins are working on a fix for `emmy1`.

## Keywords
- Singularity
- Ubuntu image
- squashfs filesystem
- emmy1
- emmy2
- kernel support
- Singularity cache
- verbose output
```
---

### 2024062642002459_Running%20JAX%20on%20AMD%20GPUs.md
# Ticket 2024062642002459

 # HPC Support Ticket: Running JAX on AMD GPUs

## Keywords
- JAX
- AMD GPUs
- ROCm
- Python
- SLURM
- Docker
- Apptainer
- Dependency Conflicts

## Summary
A user is attempting to run JAX on AMD GPUs in the test cluster following official guidance but encounters issues. The user seeks assistance and suggests a Zoom meeting to resolve the problem, which could benefit other AMD users.

## Problem
- The user is trying to run JAX on AMD GPUs using the official guidance from AMD.
- The user encounters dependency conflicts and other errors during the installation process.
- The user attempts to install JAX using both a Python environment and a Docker container via Apptainer but faces issues in both approaches.

## Root Cause
- Dependency conflicts between JAX versions (0.4.29 and 0.4.30).
- Incorrect installation commands leading to version mismatches.
- Issues with accessing nodes with ROCm installed (milan1) from the testfront node.

## Solution
1. **Interactive Session for Installation**:
   - Use an interactive session to install JAX on a node with ROCm installed.
   ```bash
   $ salloc -t 04:00:00 --exclusive -w milan1 -c 64 -p work
   ```

2. **Uninstall Conflicting Versions**:
   - Uninstall any conflicting versions of JAX before installing the required version.
   ```bash
   $ python3 -m pip uninstall --user jax
   ```

3. **Install Specific Versions**:
   - Ensure the correct versions of JAX and JAXlib are installed.
   ```bash
   $ python3 -m pip install --user https://github.com/ROCm/jax/releases/download/rocm-jaxlib-v0.4.30/jaxlib-0.4.30+rocm602-cp310-cp310-manylinux2014_x86_64.whl https://github.com/ROCm/jax/archive/refs/tags/rocm-jaxlib-v0.4.30.tar.gz jax==0.4.30
   ```

4. **Avoid SLURM Output Options**:
   - Avoid using `--output` and `--error` options in SLURM scripts to prevent common errors.

## Additional Notes
- The user should test the installation interactively before using it in batch scripts.
- The installation documentation provided by AMD contains tests to verify the installation.

## Conclusion
The user needs to ensure that the correct versions of JAX and JAXlib are installed and that there are no conflicting dependencies. Using an interactive session on a node with ROCm installed is recommended for the installation process.
---

### 2019110242000621_Singularity-Konfiguration%20auf%20Emmy.md
# Ticket 2019110242000621

 ```markdown
# Singularity Configuration Issue on Emmy

## Keywords
- Singularity
- singularity.conf
- /scratch
- $TMPDIR
- Emmy
- Woody
- TinyGPU
- Meggie

## Problem Description
- On Emmy, `/scratch` is not automatically included in the `singularity.conf` file, despite `$TMPDIR` pointing to `/scratch/9999999.eadm`.
- On Woody and TinyGPU, `/scratch` is included in the `singularity.conf`.
- On Meggie, there is no `/scratch` and `$TMPDIR` points to `/tmp/`, which is correctly included.

## Root Cause
- The `singularity.conf` on Emmy does not include `/scratch` by default, leading to inconsistencies in the configuration across different systems.

## Solution
- Include `/scratch` in the `singularity.conf` on Emmy to ensure consistency and allow users to work with `$TMPDIR` without issues.

## Lessons Learned
- Consistency in configuration files across different systems is crucial for a seamless user experience.
- Regularly review and update configuration files to ensure they align with user expectations and system requirements.

## Actions Taken
- The HPC Admin team updated the `singularity.conf` on Emmy to include `/scratch`.

## Follow-up
- Verify that the updated configuration works as expected and that users can utilize `$TMPDIR` without encountering issues.
```
---

### 2024101042003131_Request%20for%20access.md
# Ticket 2024101042003131

 # HPC Support Ticket: Request for Access

## Keywords
- HPC Access
- Account Creation
- Docker
- Apptainer
- Chip Designing
- OpenROAD
- Google Colab

## Summary
A student requested access to HPC resources for chip designing using OpenROAD flow scripts. The user intended to use Docker for software management and needed guidance on integrating it with Google Colab.

## Root Cause
- User needed access to HPC resources.
- User intended to use Docker, which is not supported on HPC systems.

## Solution
- **Account Creation**: The user was directed to the account creation guide: [Account Creation Guide](https://doc.nhr.fau.de/account/).
- **Docker Alternative**: The user was informed that Docker is not supported and was advised to convert Docker containers to Apptainer format: [Apptainer Guide](https://doc.nhr.fau.de/environment/apptainer/).

## General Learning
- HPC systems do not support Docker; Apptainer is the recommended alternative.
- Users need to follow specific procedures to create an HPC account, including obtaining an invitation from a contact person for Tier3 access.
- Guidance on software compatibility and conversion is crucial for users transitioning from personal systems to HPC environments.
---

### 2018070942002063_Docker-Images%20aus%20NVidia%20GPU%20Cloud%20%28ngc.nvidia.com%29.md
# Ticket 2018070942002063

 # HPC Support Ticket: Docker Images from NVidia GPU Cloud

## Keywords
- NVidia GPU Cloud
- Docker Images
- Terms of Use
- Central Account
- HPC Users
- GPU Systems

## Summary
A user inquires about the permissibility of downloading optimized Docker images from NVidia GPU Cloud using a central account and making them available to HPC users at the university.

## Root Cause
The user is concerned about the compliance with NVidia's Terms of Use, specifically the clause mentioning "on behalf of a company or other legal entity," when downloading and distributing Docker images to HPC users.

## Solution
- **Action Required**: Review NVidia's Terms of Use to determine if downloading and distributing Docker images through a central account is permissible.
- **Next Steps**: If compliance is confirmed, proceed with downloading and making the images available to HPC users. If not, seek legal advice or alternative methods for distribution.

## General Learnings
- Always review and comply with the Terms of Use when using third-party resources.
- Ensure that any centralized distribution of software or resources is in line with the provider's policies.
- Communicate with legal advisors if there are uncertainties regarding compliance.

## Follow-Up
- **HPC Admin**: Acknowledged the inquiry with a "PING" response.
- **Next Steps for Support**: Review the Terms of Use and provide guidance on compliance. If necessary, consult with legal advisors for clarification.
---

### 2023033142003679_Warnmeldung%20Singularity%20auf%20alex.md
# Ticket 2023033142003679

 ```markdown
# HPC-Support Ticket: Warnmeldung Singularity auf alex

## Keywords
- Singularity
- Apptainer
- Warnmeldung
- Bind mounts
- System administrator
- Cleanup

## Summary
A user reported two warning messages related to Singularity on the HPC system.

## Problem
1. **Singularity Migration Warning**:
   - Warning: `INFO: /etc/singularity/ exists; cleanup by system administrator is not complete (see https://apptainer.org/docs/admin/latest/singularity_migration.html)`
   - Root Cause: The directory `/etc/singularity/` exists but contains only a file marking the completion of the migration to Apptainer.

2. **Bind Mounts Warning**:
   - Warning: `INFO: underlay of /usr/bin/nvidia-smi required more than 50 (558) bind mounts`
   - Root Cause: This warning is common in recent versions of Apptainer due to how it constructs the environment.

## Solution
1. **Singularity Migration Warning**:
   - The HPC Admins can remove the `/etc/singularity/` directory as the migration to Apptainer is complete.

2. **Bind Mounts Warning**:
   - This warning can be ignored as it is a common issue with recent versions of Apptainer and is not typically resolvable by users or admins.

## General Learning
- **Singularity to Apptainer Migration**: Ensure that all nodes are fully migrated and cleanup any residual directories.
- **Apptainer Warnings**: Some warnings in Apptainer are common and can be safely ignored if they do not impact functionality.
```
---

### 2020110142000012_Singularity-Fehlermeldung.md
# Ticket 2020110142000012

 # Singularity Fusemount Error

## Keywords
- Singularity
- Fusemount
- Configuration
- Reboot
- Patch
- Storage
- Gleitlöschung

## Problem Description
The user encountered a `FATAL: fusemount disabled by configuration 'enable fusemount = no'` error while using Singularity. This issue is known in Singularity version 3.6.

## Root Cause
- The configuration directive `enable fusemount = no` was causing the error.
- The issue reappeared after system reboots due to the old configuration being reapplied.

## Solutions Attempted
1. **Temporary Configuration Change**: The HPC Admin temporarily changed the `singularity.conf` to `enable fusemount = yes`.
2. **Patch Application**: A patched version of Singularity (3.6.4 + Patch) was deployed to handle the issue with `fusemount = no`.
3. **Older Version**: The user was informed about the availability of an older version of Singularity on Woody, which was not affected by the `fusemount = no` issue.

## Outcome
- The temporary configuration change resolved the issue initially.
- The patched version was expected to provide a more permanent solution, but the issue reappeared due to updates overwriting the configuration.
- The HPC Admin had to reapply the configuration change and ensure the patched version was used after reboots.

## Additional Notes
- The user was advised to follow up on a storage request with the AGFD.
- Gleitlöschung (automatic deletion) was mentioned as a necessary action on Emmy.
- The user inquired about the speed difference between `find` and `du -h` commands on different file systems (Titan and LXFS).

## Lessons Learned
- Temporary configuration changes may not persist through reboots.
- Applying patches and ensuring they are not overwritten by updates is crucial for maintaining system stability.
- Communication with other departments (e.g., AGFD) is important for resolving related issues.
- Regular maintenance tasks like Gleitlöschung should be planned and communicated to users.

## References
- [Singularity Issue #5631](https://github.com/hpcng/singularity/issues/5631)
---

### 2024020542000444_Ausf%C3%83%C2%BChren%20von%20Dockercontainer.md
# Ticket 2024020542000444

 # HPC-Support Ticket: Running Docker Containers

## Keywords
- Docker
- Apptainer
- Container
- Cluster
- Model Conversion

## Problem
- User needs to run a Docker container for model conversion on the HPC cluster.

## Solution
- Docker containers can be executed on the cluster using Apptainer.
- Refer to the documentation for detailed instructions and necessary commands: [Apptainer Documentation](https://doc.nhr.fau.de/environment/apptainer/)

## General Learnings
- Apptainer is the preferred tool for running Docker containers on the HPC cluster.
- Users should refer to the provided documentation for specific instructions and commands.

## Roles Involved
- **HPC Admins**: Provided the solution and documentation link.
- **User**: Requested assistance with running Docker containers.

## Root Cause
- User was unaware of the method to run Docker containers on the HPC cluster.

## Resolution
- Informed the user about using Apptainer to run Docker containers and provided the relevant documentation link.
---

### 2022112242006054__home_atuin%20in%20Singularity.md
# Ticket 2022112242006054

 # HPC Support Ticket: /home/atuin in Singularity

## Keywords
- Singularity
- Apptainer
- /home/atuin
- Mounting
- Configuration
- Warnings

## Problem Description
- **Root Cause**: /home/atuin is not automatically mounted in Singularity on Alex.
- **Additional Issue**: Warning message indicating incomplete migration to Apptainer.

## Ticket Conversation
- **User**: Reported that /home/atuin is not automatically mounted in Singularity and a warning message about incomplete migration to Apptainer.
- **HPC Admin**: Identified that one of the Alex compute nodes had an incorrect `apptainer.conf` and an uncleaned `/etc/singularity` directory.

## Solution
- **Action Taken**: The HPC Admin corrected the `apptainer.conf` and cleaned up the `/etc/singularity` directory.
- **Expected Outcome**: The issues with mounting /home/atuin and the warning message should be resolved.

## General Learning
- Ensure that configuration files (`apptainer.conf`) are correctly set up.
- Clean up old directories (`/etc/singularity`) to avoid conflicts during migrations.
- Regularly check for and address warning messages to prevent potential issues.

## Next Steps
- Verify that /home/atuin is now correctly mounted in Singularity.
- Confirm that the warning message about incomplete migration to Apptainer has been resolved.

---

For further assistance, contact the HPC Support team.
---

### 2022062042005345_TAO%20%26%20Singularity.md
# Ticket 2022062042005345

 # HPC Support Ticket: TAO & Singularity

## Keywords
- Singularity
- TAO Toolkit
- RIVA Model
- Docker
- Shell Scripts
- Container Size
- $SINGULARITY_CACHEDIR
- /tmp Space

## Problem Description
- User encountered issues after successfully pulling the TAO Toolkit container using Singularity.
- The problem arose when trying to start a notebook that uses a RIVA model.
- Shell scripts designed for Docker were difficult to adapt for Singularity.

## Root Cause
- The RIVA scripts are complex and involve starting daemons and communicating over ports, making them challenging to convert to Singularity.

## Solution
- Ensure that $SINGULARITY_CACHEDIR is set to a location other than $HOME due to the large size of the container.
- Perform the import/pull on a system with sufficient free space in /tmp (>10 GB).
- No straightforward solution was provided for converting the Docker-based RIVA scripts to Singularity.

## General Learnings
- Large containers require careful management of cache directories and temporary storage.
- Converting complex Docker-based workflows to Singularity can be non-trivial, especially when daemons and network communication are involved.

## Next Steps
- Further investigation is needed to adapt the RIVA scripts for Singularity.
- Consider consulting with software and tools developers for assistance with script conversion.
---

### 2021020242001089_Installation%20OpenPose.md
# Ticket 2021020242001089

 # HPC Support Ticket: Installation OpenPose

## Keywords
- OpenPose
- Singularity Container
- Root Permissions
- HPC Cluster
- Local Machine

## Problem
- User attempted to install OpenPose using a Singularity container.
- Lacked root permissions to execute `sudo singularity shell -w openpose_multi_container_oct_2019`.

## Root Cause
- Root permissions are required to create a Singularity container.
- HPC clusters do not provide root access to users.

## Solution
- Use a local machine or a local virtual machine (VM) to create the Singularity container.
- Refer to the provided documentation for more information on Singularity containers: [Singularity Containers Presentation](https://hpc.fau.de/files/2020/05/2020-05-12-singularity-containers.pdf).

## General Learning
- Root permissions are necessary for creating Singularity containers.
- HPC clusters typically do not allow root access for security reasons.
- Users should create Singularity containers on local machines or VMs and then transfer them to the HPC cluster for use.

## References
- [Singularity Containers Presentation](https://hpc.fau.de/files/2020/05/2020-05-12-singularity-containers.pdf)
- [OpenPose with NVCAFFE in a Singularity Container](http://peter-uhrig.de/openpose-with-nvcaffe-in-a-singularity-container-with-support-for-multiple-architectures/)
---

### 2021012242000651_CVMFS.md
# Ticket 2021012242000651

 ```markdown
# HPC-Support Ticket Conversation: CVMFS Access

## Keywords
- CVMFS
- Singularity
- HPC
- Workflows
- Pipelines
- Software Distribution
- Security
- Networking

## Summary
- **User Request**: Access to CVMFS repositories for software distribution across multiple computing farms.
- **HPC Admin Response**: CVMFS is not currently installed. Security and networking concerns are raised, particularly regarding the ability of compute nodes to establish external connections.
- **Proposed Solution**: Using Singularity's `--bind` option to map CVMFS paths to local directories, avoiding the need for CVMFS on compute nodes.

## Detailed Conversation
- **User**: Requests access to CVMFS for distributing Singularity images across different computing farms. Mentions that CVMFS is widely used in High Energy Physics.
- **HPC Admin**: Clarifies that CVMFS is not installed. Asks if CVMFS needs to be available on all compute nodes or just the frontend. Raises concerns about security and networking limitations.
- **User**: Explains that Singularity images are accessed via hardcoded CVMFS paths. Suggests that CVMFS is only written to when software is updated.
- **HPC Admin**: Proposes using Singularity's `--bind` option to map CVMFS paths to local directories, allowing Singularity containers to find data without needing CVMFS on compute nodes.
- **User**: Agrees that manually mirroring images to local directories could be a viable solution.

## Root Cause
- Lack of CVMFS installation on the HPC system.
- Security and networking limitations prevent compute nodes from establishing external connections.

## Solution
- Use Singularity's `--bind` option to map CVMFS paths to local directories, allowing Singularity containers to access data without needing CVMFS on compute nodes.
- Manually mirror Singularity images to local directories as needed.

## Conclusion
- The proposed solution using Singularity's `--bind` option addresses the user's need for accessing CVMFS paths without requiring CVMFS installation on compute nodes.
- This approach maintains security and networking constraints while allowing for flexible software distribution.
```
---

### 2023080842002508_using%20docker%20in%20hpc.md
# Ticket 2023080842002508

 ```markdown
# HPC Support Ticket: Using Docker in HPC

## Keywords
- Docker
- HPC
- Nvidia Modulus
- Apptainer/Singularity
- Containerization

## Problem
- User wants to use Docker in HPC to install Nvidia Modulus, which is only available in its Docker version.

## Root Cause
- Docker is not supported on the HPC system.

## Solution
- Use Apptainer/Singularity as an alternative to Docker.
- Apptainer can import Docker images.

## Resources
- [Singularity Containers Presentation](https://hpc.fau.de/files/2020/05/2020-05-12-singularity-containers.pdf)
- [Singularity/Apptainer Documentation](https://hpc.fau.de/systems-services/documentation-instructions/special-applications-and-tips-tricks/singularity-apptainer/)

## General Learning
- Docker is not supported on many HPC systems due to security and performance reasons.
- Apptainer/Singularity is a common alternative for containerization in HPC environments.
- Apptainer can import Docker images, making it a flexible solution for users who need Docker-based software.
```
---

### 2024052242001576_Re%3A%20Grace%20Hopper%20Testsystem.md
# Ticket 2024052242001576

 # HPC Support Ticket Conversation Analysis

## Keywords
- Docker
- Apptainer
- Testcluster
- Grace Hopper
- GraceGrace
- NHR@FAU HPC Documentation
- Account Freischaltung
- Kurzanleitung

## Summary
- **User Request**: Inquiry about Docker support and documentation for the test cluster.
- **HPC Admin Response**: Docker is not supported, but Apptainer is available and compatible. Provided documentation link for the test cluster.
- **Action Taken**: Accounts k105be10-k105be16 were activated on the test cluster.
- **Follow-up**: User requested documentation or slides for the systems, but HPC Admin did not have any available.

## Root Cause of the Problem
- User needed Docker support for quick installation but found out it is not supported.

## Solution
- Apptainer is suggested as an alternative to Docker.
- User accounts were activated on the test cluster.
- Documentation for the test cluster was provided.

## General Learnings
- **Compatibility**: Apptainer is a viable alternative to Docker for containerization on HPC systems.
- **Documentation**: Always refer users to the official documentation for detailed information.
- **Account Activation**: Ensure user accounts are properly activated for access to test clusters.

## Next Steps
- **Documentation**: Consider creating or updating documentation/slides for the test cluster systems.
- **Support**: Ensure 2nd Level Support team is available to assist users with any questions or issues related to the test cluster.

---

This report provides a concise overview of the support ticket conversation, highlighting key actions and learnings for future reference.
---

### 2023052142000821_Frage%20zum%20Container-Betrieb%20auf%20Alex.md
# Ticket 2023052142000821

 # HPC Support Ticket: Container Operation on Alex

## Keywords
- Container
- Singularity/Apptainer
- Docker
- Podman
- VM
- GPU Nodes
- Security
- Namespaces
- Overhead

## Summary
A user inquired about the operation of Singularity/Apptainer containers on GPU nodes, specifically whether they run natively on the OS or within a VM. The user also mentioned security concerns and the preference for Docker containers among their users.

## Root Cause
The user needed clarification on the container operation method on GPU nodes and sought advice on security considerations for their upcoming compute cluster.

## Solution
- **Container Operation**: Singularity/Apptainer containers run directly on the nodes with RHEL/Ubuntu as the host OS. They use RHEL/EPEL packages that no longer require suid.
- **Security**: Network namespaces are generally deactivated for security reasons but are not typically necessary for HPC applications.
- **Docker Alternative**: Podman is suggested as an alternative to Docker, as it does not require a root daemon.
- **VMs**: VMs are not recommended for HPC due to the overhead they introduce.

## General Learnings
- Singularity/Apptainer containers can run natively on the OS without the need for VMs.
- Docker requires a root daemon, which may pose security concerns. Podman is a viable alternative.
- VMs are not suitable for HPC due to the overhead they introduce compared to namespaces.

## References
- [FAU HPC Support](mailto:support-hpc@fau.de)
- [FAU HPC Website](https://hpc.fau.de/)
---

### 2025013142001626_Docker%20on%20ARM%20Lukewarm.md
# Ticket 2025013142001626

 ```markdown
# HPC-Support Ticket: Docker on ARM Lukewarm

## Issue
- **User Request**: Install Docker on ARM Lukewarm to compile for Ubuntu 22.04.4 LTS with GNU C Library (Ubuntu GLIBC 2.35).
- **Initial Response**: Docker is not supported on the systems, but Apptainer is available on the clusters.

## Attempted Solutions
1. **Apptainer Installation**:
   - User attempted to use Apptainer but encountered errors:
     ```
     ERROR: Could not write info to setgroups: Permission denied
     ERROR: Error while waiting event for user namespace mappings: Bad file descriptor
     ```
   - These errors did not occur on the user's local machine.

2. **Fakeroot Option**:
   - Using `--fakeroot` was not an option on the cluster.
   - Suggestion to build the container on a local machine and then move it.

3. **Container Build**:
   - User tried building the container locally but faced issues.
   - Meeting was scheduled to review the problem together.

## Internal Discussion
- **Namespace Mapping**:
  - Discussed the need for proper namespace mapping and user namespace configurations.
  - Entries in `/etc/subuid` and `/etc/subgid` were suggested as a workaround.

- **Apparmor Issue**:
  - Apparmor profile needed adjustment to resolve namespace issues.
  - Disabled Apparmor restrictions using:
    ```sh
    sudo sh -c 'echo kernel.apparmor_restrict_unprivileged_userns=0 > /etc/sysctl.d/90-disable-userns-restrictions.conf'
    sudo sysctl -p /etc/sysctl.d/90-disable-userns-restrictions.conf
    ```

- **Libc Version Conflict**:
  - Ubuntu 22.04 container on Ubuntu 24.04 host had a libc version conflict.
  - Ubuntu 24.04 container was suggested as an alternative.

## Final Solution
- **Container Configuration**:
  - Adjusted configurations to allow the container to run rootless.
  - User confirmed that the container worked as expected after the adjustments.

## Key Takeaways
- **Apptainer Configuration**: Ensure proper namespace mapping and user namespace configurations.
- **Apparmor Adjustments**: Disable Apparmor restrictions if necessary.
- **Libc Version Compatibility**: Be aware of libc version conflicts between host and container.
- **Local Build Option**: Suggest building containers locally if possible to avoid HPC resource constraints.

## Documentation
- **Apptainer Documentation**: [Apptainer Documentation](https://doc.nhr.fau.de/environment/apptainer/)
- **Namespace Configuration**: Ensure proper entries in `/etc/subuid` and `/etc/subgid`.

## Conclusion
- The issue was resolved by adjusting namespace configurations and disabling Apparmor restrictions.
- The user was able to run the container successfully after these adjustments.
```
---

### 2023010942001896_Singularity%20Container%20Mount%20Error%20on%20TinyGPU.md
# Ticket 2023010942001896

 # HPC Support Ticket: Singularity Container Mount Error on TinyGPU

## Keywords
- Singularity Container
- TinyGPU
- Mount Error
- /scratchsdd
- Bind Mounts

## Problem Description
- User encountered an error when trying to start a Singularity container on TinyGPU.
- Error message indicated a mount error related to `/scratchsdd`.
- Additional warnings about bind mounts exceeding 50 were also present.

## Root Cause
- Typo in the configuration file related to `/scratchsdd`.

## Solution
- HPC Admin corrected the typo in the configuration file.
- The error related to `/scratchsdd` should be resolved.
- Warnings about bind mounts exceeding 50 are not critical and can be ignored.

## General Learnings
- Configuration typos can lead to mount errors in Singularity containers.
- Bind mount warnings exceeding 50 are not critical and do not require immediate action.
- Ensure configuration files are accurate and free of typos to avoid mount errors.

## Next Steps
- Verify that the container starts without the `/scratchsdd` error.
- Monitor for any additional issues related to bind mounts.

## References
- HPC Admin: Thomas Zeiser
- User: Alexander Winterl
- Date: 09.01.2023
---

### 2020100742003224_Question%20about%20Docker.md
# Ticket 2020100742003224

 # HPC Support Ticket: Question about Docker

## Keywords
- Docker
- Singularity
- TinyGPU
- Security concerns
- Nvidia drivers
- Root privileges
- Dockerhub

## Problem
- User inquired about the possibility of using Docker containers with TinyGPU.

## Root Cause
- Security concerns related to Docker.

## Solution
- **Singularity as an Alternative**:
  - HPC does not support Docker due to security concerns.
  - Singularity is available and can be used with most Docker images.
  - Singularity was discussed in an HPC Café session on May 12, 2020.
  - To embed Nvidia drivers from the host into a running Singularity session, use the `--nv` option.

- **Root Privileges**:
  - Creating a Singularity image may require root privileges, depending on the source.
  - Use a local machine or VM where appropriate rights are available.
  - Fetching existing Docker images from Dockerhub or other repositories does not require elevated rights.

## Additional Information
- User found the information on Singularity positive and plans to explore it further.

## References
- [HPC Café Session on Singularity](https://hpc.fau.de/services/hpc-cafe/)
---

### 2022122242000736_Probleme%20mit%20Singularity%2BOpenMPI%20-%20b158cb.md
# Ticket 2022122242000736

 # HPC-Support Ticket Conversation Summary

## Problem Description
- **Issue**: Problems with Singularity and OpenMPI in multi-node jobs.
- **Error Messages**:
  - `FATAL: Couldn't determine user account information: user: unknown userid 210352`
  - `INFO: underlay of /etc/localtime required more than 50 (81) bind mounts`
  - `INFO: Cleanup error: while unmounting /var/apptainer/mnt/session/final directory: device or resource busy`
  - Sporadic NaNs produced in Python code.

## Root Cause
- **Singularity Issues**:
  - Singularity containers had issues with user account information and bind mounts.
  - Cleanup errors indicated potential race conditions or resource contention.
- **OpenMPI and MKL Issues**:
  - Sporadic NaNs in Python code suggested issues with the MKL library.

## Solutions
- **Singularity**:
  - Singularity containers are not recommended for multi-node jobs due to complexity and potential issues.
  - Ensure proper mounting and cleanup of resources within the container.
- **OpenMPI and MKL**:
  - Switch to an Intel-free software stack to avoid issues with MKL.
  - Use the following module combination:
    ```bash
    module load gcc/11.2.0
    module load fftw/3.3.10-ompi
    module load hdf5/1.10.7-intel
    module load 000-all-spack-pkgs/0.18.0
    module load openblas/0.3.20-gcc8.5.0-3qsadbi
    module load cmake/3.23.1
    module load git/2.35.2
    module load python/mpi4py-3.1.1py3.9
    pip install "numpy>=1.22"
    ```

## Additional Information
- **CPU Time Usage**:
  - Currently, there is no terminal command to check CPU time usage on login nodes.
  - This feature is on the wishlist for future implementation.

## Conclusion
- The user was able to resolve the NaN issue by switching to an Intel-free software stack.
- Singularity containers should be avoided for multi-node jobs due to complexity and potential issues.
- Ensure proper resource management and cleanup within Singularity containers.

---

**Note**: This report is based on the provided conversation and aims to document the root cause and solutions for future reference.
---

