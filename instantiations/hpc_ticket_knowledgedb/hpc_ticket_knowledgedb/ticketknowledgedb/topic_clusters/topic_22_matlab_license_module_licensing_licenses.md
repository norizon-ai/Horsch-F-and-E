# Topic 22: matlab_license_module_licensing_licenses

Number of tickets: 45

## Tickets in this topic:

### 2024042642000955_Using%20MATLAB%27s%20audioread%28%29%20in%20the%20clusters.md
# Ticket 2024042642000955

 # HPC Support Ticket: Using MATLAB's `audioread()` in the Clusters

## Keywords
- MATLAB
- `audioread()`
- LIBSNDFILE library
- Media frameworks
- Compute nodes
- Login nodes
- User-spack
- Conda
- Preprocessing data

## Problem
- The `audioread()` function in MATLAB does not work on the compute nodes but works on the login nodes.
- Error message: "Install the LIBSNDFILE library and the required Media frameworks for your system."

## Root Cause
- The compute nodes have a stripped-down operating system, missing the required libraries for `audioread()` to function.

## Solutions
1. **Install Required Libraries**:
   - Use user-spack, conda, or other methods to install the LIBSNDFILE library and required Media frameworks in the user's directories.
   - Load these libraries at runtime so MATLAB can find them.

2. **Preprocess Data**:
   - Preprocess the data on the frontend using `audioread()`.
   - Save the data into a single decoded file format that can be loaded on the compute nodes for further processing without needing the libraries.

## Additional Notes
- The HPC Admin mentioned that the operating system on the compute nodes is stripped down, which is why the required libraries are missing.
- The user was advised to try the suggested workarounds.

## References
- [User-spack Documentation](https://doc.nhr.fau.de/apps/spack)
- [Conda Documentation](https://doc.nhr.fau.de/sdt/python/)

## Follow-up
- The user acknowledged the suggestions and planned to try them.

This documentation can be used to resolve similar issues in the future.
---

### 42330560_HPC-Kennung%20SFP-Projekt%20TRR154.md
# Ticket 42330560

 # HPC Support Ticket: HPC-Kennung SFP-Projekt TRR154

## Keywords
- HPC-Kennung
- SFP-Projekt TRR154
- Angewandte Mathematik
- Wirtschaftsmathematik
- mpm2
- mpwm
- IDM-Kennung
- MATLAB-Installation
- Lizenzserver

## Summary
The ticket involves setting up an HPC account for a user working on a project related to the SFP-Projekt TRR154. The user is associated with the Department of Applied Mathematics but the project is for Economic Mathematics. The discussion revolves around determining the appropriate HPC identifier (mpm2 or mpwm) and setting up the necessary accounts and permissions.

## Root Cause
- Confusion over the appropriate HPC identifier for the user's project.
- Need for MATLAB installation and license server integration on the HPC clusters.

## Solution
1. **HPC Identifier**:
   - The HPC Admin initially inquires about whether to use `mpwm` or `mpm2` for the user's project.
   - It is decided to use `mpm2` because the project involves multiple departments.

2. **Account Setup**:
   - A new HPC identifier `mpm221` is created for the user.
   - The user is instructed to set a password for the new identifier via the IDM portal.

3. **MATLAB Installation**:
   - The user requests MATLAB installation on the HPC clusters `tf020` and `tf030`.
   - The HPC Admin provides instructions to load MATLAB using `module load matlab/R2014a`.
   - The user is asked to provide license server details for integration.

## General Learnings
- **Account Management**: Understanding the appropriate HPC identifier based on the project's scope and departmental involvement.
- **Software Installation**: Handling requests for software installations and license server integration on HPC clusters.
- **User Communication**: Clear communication with users regarding account setup and software usage.

## Conclusion
The ticket highlights the importance of proper account management and software support in an HPC environment. It also emphasizes the need for clear communication between HPC Admins and users to ensure smooth operation and resource allocation.
---

### 2022072142001416_MatLab%20Access%20on%20Woody-NG%20%7C%20iwso.md
# Ticket 2022072142001416

 # HPC Support Ticket: MatLab Access on Woody-NG | iwso

## Keywords
- MatLab R2022a
- License Issues
- Woody-NG Cluster
- Group-specific License Settings
- Missing Libraries
- libXt.so.6

## Problem Description
A student encountered unexpected license issues when trying to use MatLab R2022a on the Woody-NG cluster. The license for the group (MaDLab, 'iwso') had not been migrated to the new cluster. Additionally, there were errors related to missing shared object files.

## Error Messages
- **License Issue:**
  ```
  ATTENTION: no license settings known for iwso052h / iwso
  ```
- **Shared Object File Error:**
  ```
  MATLAB is selecting SOFTWARE OPENGL rendering.
  Unexpected exception: 'N7mwboost10wrapexceptINS_16exception_detail39current_exception_std_exception_wrapperISt13runtime_errorEEEE: Error loading /apps/matlab/R2022a/bin/glnxa64/matlab_startup_plugins/matlab_graphics_ui/mwuixloader.so. libXt.so.6: cannot open shared object file: No such file or directory: Success: Success' in createMVMAndCallParser phase 'Creating local MVM'
  ```

## Root Cause
- The license for the group had not been migrated to the Woody-NG cluster.
- Missing shared object files (libXt.so.6) required by MatLab.

## Solution
- **License Issue:**
  - HPC Admins migrated the group-specific license settings to the Woody-NG cluster.
- **Shared Object File Error:**
  - HPC Admins installed the missing libraries (libXt.so.6).

## Follow-up
- The license issue was resolved, but the shared object file error persisted.
- HPC Admins installed additional missing libraries, which resolved the issue.

## Conclusion
- Ensure that group-specific licenses are migrated when moving to a new cluster.
- Verify that all required libraries are installed to avoid shared object file errors.

## Notes
- The issue was resolved through collaboration between the user and HPC Admins.
- The user expressed gratitude for the quick resolution.
---

### 2023040642002519_matlab%20on%20hpc%20server%3F.md
# Ticket 2023040642002519

 # HPC Support Ticket: Matlab Availability

## Keywords
- Matlab
- HPC server
- TinyGPU
- Woody cluster
- Institutional network license
- LM_PROJECT

## Problem
- User unable to find Matlab under `module avail` on TinyGPU cluster.
- User inquires about Matlab availability on other clusters and access permissions.

## Root Cause
- Matlab is not linked to personal licenses but to an institutional network license.
- User needs to know the appropriate `LM_PROJECT` for their work.

## Solution
- Matlab is available on demand on HPC systems.
- User should contact their IT department to determine the correct `LM_PROJECT`.
- HPC Admin can then activate Matlab for the user's account.
- Suggested using the Woody cluster for computations, which the user has automatic access to.

## General Learnings
- Matlab requires an institutional network license to be activated on HPC systems.
- Users may have access to multiple clusters automatically.
- Specific project codes (`LM_PROJECT`) are necessary for activating certain software licenses.

## Action Taken
- HPC Admin advised the user to contact their IT department for the `LM_PROJECT` code.
- Suggested using the Woody cluster for Matlab-related computations.
---

### 2019050342000783_Matlab%20auf%20den%20HPC%20Clustern%3F.md
# Ticket 2019050342000783

 # HPC Support Ticket: Matlab auf den HPC Clustern?

## Keywords
- Matlab
- HPC Cluster
- Numerical Computations
- Student Access

## Summary
A user inquired about the availability of Matlab or its libraries on the HPC clusters for numerical computations by students.

## Root Cause
The user wanted to know if Matlab could be used on the HPC clusters for specific numerical tasks by students.

## Solution
No explicit solution provided in the conversation. Further details or follow-up would be required to determine the availability and setup of Matlab on the HPC clusters.

## General Learning
- Users may need to verify the availability of specific software (e.g., Matlab) on HPC clusters for educational purposes.
- Quick responses to such inquiries can help users plan their computational tasks effectively.

## Next Steps
- Check the software inventory on the HPC clusters.
- Provide instructions on how to access and use Matlab if available.
- Offer alternatives if Matlab is not available.
---

### 42298480_Update%20von%20Matlab%20auf%20Woody.md
# Ticket 42298480

 ```markdown
# HPC-Support Ticket: Update von Matlab auf Woody

## Keywords
- Matlab
- Update
- Woody
- R2010b
- R2011a
- R2014a
- Installation
- Download
- Freischaltung

## Problem
- The current Matlab versions on the Woody servers are R2010b and R2011a.
- The user requests an update to a newer version, specifically R2014a.

## Solution
1. **Request for Software**: HPC Admin requests access to Matlab R2014a for installation.
2. **Access Granted**: Another HPC Admin grants temporary download access for the user `unrz00k3`.
3. **Installation**: Matlab R2014a is installed on the Woody servers.
4. **Confirmation**: The user is notified that Matlab R2014a is now available on Woody.

## General Learnings
- **Software Update Process**: Understanding the steps involved in updating software on HPC systems.
- **Collaboration**: Effective communication and collaboration between HPC Admins and users for software updates.
- **Access Management**: Managing temporary access for software downloads to facilitate updates.

## Root Cause
- Outdated Matlab versions on Woody servers.

## Resolution
- Successful update to Matlab R2014a after coordination between HPC Admins and the user.
```
---

### 2019061942001296_fhnm001h%20-%20Batch%20script%20f%C3%83%C2%BCr%20TinyGPU.md
# Ticket 2019061942001296

 # HPC Support Ticket Conversation Summary

## Keywords
- MATLAB
- Licensing
- TinyGPU Cluster
- Batch Script
- GPU Nodes
- Version Compatibility
- Private License

## General Learnings
- Ensure the correct MATLAB version is loaded using `module load matlab/R2018b`.
- Use `-nodesktop -nosplash` flags to avoid loading the graphical interface in batch mode.
- Reduce walltime for test runs to expedite job execution.
- Verify GPU availability and compatibility with the code.
- Private licenses can be used if installed in user directories.

## Root Causes of Problems
- Incorrect MATLAB version loaded, leading to licensing errors.
- Incorrect batch script syntax and resource allocation.
- Lack of awareness about available GPU nodes and their specifications.

## Solutions
- Correct the batch script to load the appropriate MATLAB version.
- Adjust resource allocation in the batch script to match the code requirements.
- Verify GPU node availability and compatibility.
- Install and use private licenses in user directories if necessary.

## Detailed Conversation Summary

### User Initial Request
- User requested help with a batch script for running a MATLAB job on the TinyGPU cluster.
- User encountered a licensing error (-39,147) when trying to use the installed MATLAB version.

### HPC Admin Response
- HPC Admin corrected the batch script and provided instructions for submitting the job.
- Advised the user to load the correct MATLAB version using `module load matlab/R2018b`.
- Added `-nodesktop -nosplash` flags to the MATLAB call to avoid loading the graphical interface.
- Suggested reducing walltime for test runs to expedite job execution.
- Explained that the licensing error was likely due to version incompatibility.

### User Follow-up
- User inquired about using private licenses and the availability of specific GPU nodes.
- User attempted to submit the job but encountered issues.

### HPC Admin Follow-up
- HPC Admin confirmed the availability of the correct MATLAB module and provided additional guidance.
- Explained the principle of batch jobs and how to test the MATLAB call locally.
- Confirmed that private licenses can be used if installed in user directories.

### User Final Request
- User requested permission to use a newer MATLAB version (R2019a) with a private license.

### HPC Admin Final Response
- HPC Admin confirmed the availability of the R2019a module and the possibility of using private licenses.
- Provided instructions for installing software in user directories under the respective license conditions.

This summary provides a concise overview of the key points and solutions discussed in the HPC support ticket conversation.
---

### 2023011742000827_Fehlendes%20Matlabmodul%20auf%20dem%20woody5.md
# Ticket 2023011742000827

 # HPC Support Ticket: Missing Matlab Module on woody5

## Keywords
- Matlab module
- Module load error
- ERROR: Unable to locate a modulefile for 'matlab'
- ssh -X
- woody-ng.nhr.fau.de
- source /apps/modules/5.1.1/etc/initic

## Problem Description
The user is unable to load the Matlab module on the woody5 cluster. The error message received is `ERROR: Unable to locate a modulefile for 'matlab'`.

## Root Cause
The root cause of the problem is not explicitly stated but is likely related to a misconfiguration or missing module file for Matlab.

## Solution
As a temporary workaround, the user can manually source the module initialization script:
```bash
source /apps/modules/5.1.1/etc/initic
```

## General Learnings
- Ensure that the module files are correctly configured and available on the cluster.
- Provide users with temporary workarounds while investigating the root cause of the issue.
- Communicate with users promptly to acknowledge their issue and provide updates on the investigation.

## Roles Involved
- **HPC Admins**: Responsible for investigating and resolving the issue.
- **2nd Level Support Team**: May assist in troubleshooting and providing additional support.
- **Head of the Datacenter** and **Training and Support Group Leader**: Oversee the overall support process.
- **Software and Tools Developer**: May be involved if the issue requires code-level fixes.

## Next Steps
- Continue investigating the root cause of the missing Matlab module.
- Update the user once the issue is fully resolved.
- Document the resolution for future reference.
---

### 2019060742001531_WG%3A%20R%C3%83%C2%BCckfrage%20zu%20Ticket-Nummer%202019-06-0019.md
# Ticket 2019060742001531

 # HPC-Support Ticket Conversation Analysis

## Subject: WG: Rückfrage zu Ticket-Nummer 2019-06-0019

### Keywords:
- MATLAB License
- Firewall Configuration
- IP Address
- HPC Account
- IdM Account
- Deep Learning
- GPU Computing

### Summary:
The user, a student from TH Nürnberg, requires access to MATLAB licenses from the TH Nürnberg for their Bachelor's thesis project involving deep learning on GPUs. The process involves configuring the firewall to allow access to the TH Nürnberg's MATLAB license server from the RRZE's HPC systems.

### Root Cause:
- The user needs to perform deep learning computations using MATLAB on the RRZE's HPC systems.
- The RRZE does not provide MATLAB licenses, so the user needs to use the licenses from TH Nürnberg.
- The firewall at TH Nürnberg needs to be configured to allow access from the RRZE's IP address.

### Steps Taken:
1. **Initial Request:**
   - The user contacted the TH Nürnberg to request firewall configuration to allow access to the MATLAB license server.

2. **Firewall Configuration:**
   - The TH Nürnberg agreed to configure the firewall to allow access from a specific IP address of the RRZE.

3. **License Server Details:**
   - The user provided the necessary details for the license server, including host, IP, ports, software, and version.

4. **Account Creation:**
   - The user submitted the required forms for creating IdM and HPC accounts.
   - The HPC Admins created a new customer number and HPC account for the user.

5. **Account Activation:**
   - The user was instructed to activate their IdM account and set a password for the new HPC account.

### Solution:
- The firewall at TH Nürnberg was configured to allow access from the RRZE's IP address.
- The user's IdM and HPC accounts were created and activated.
- The user was provided with the necessary details to access the MATLAB license server from the RRZE's HPC systems.

### Notes:
- The user was advised to contact specific personnel at TH Nürnberg for further assistance with the firewall configuration.
- The user provided images of their IDs to complete the account creation process.
- The HPC Admins created a new customer number and HPC account for the user.

### Conclusion:
The user successfully obtained access to the MATLAB licenses from TH Nürnberg for their deep learning project on the RRZE's HPC systems. The firewall configuration and account creation processes were completed with the assistance of the HPC Admins and the TH Nürnberg support team.
---

### 2020120242001875_Frage%20Matlab%20PBS%20Job%20Array%20Lizenzabfrage.md
# Ticket 2020120242001875

 # HPC Support Ticket: Frage Matlab PBS Job Array Lizenzabfrage

## Problem Description
- User is running MATLAB jobs on the Woody-Cluster using PBS job arrays.
- Jobs fail due to license checkout errors when the number of available MATLAB licenses is exceeded.
- User wants to handle license unavailability by retrying the job every 30 minutes until the job array is completed.
- User also inquires about querying the number of available MATLAB licenses.

## Root Cause
- The MATLAB license manager error -87 indicates that the maximum number of licenses specified in the options file has been exceeded.
- The user's job array configuration attempts to start more MATLAB instances than available licenses, leading to job failures.

## Solution
- **License Query**: Technically, it is not possible to query the number of available MATLAB licenses.
- **Job Retry Mechanism**:
  - Implement a manual retry mechanism in the batch script.
  - Use the `qsub -a` option to resubmit the job with a delay if the MATLAB execution time is short.
  - Example script provided by HPC Admin:
    ```bash
    #!/bin/bash -l
    #PBS -l nodes=1:ppn=4,walltime=07:59:00
    #PBS -N SCLAS_HPC_FirstArrayJob
    #PBS -t 581-599%10

    module load matlab/R2019b
    cd ${PBS_O_WORKDIR}
    export OMP_NUM_THREADS=4

    start_time=$(date +%s)
    matlab -nodisplay -noFigureWindows -batch "c_HPCsetup_SCLAS_RCM_M${PBS_ARRAYID}" -logfile SCLAS_log_${PBS_JOBID}_${PBS_ARRAYID}.out
    end_time=$(date +%s)

    if [ $((end_time - start_time)) -lt 60 ]; then
        qsub -a $(date -d "+30 minutes" +%H:%M) arrayjobs_resubmit.pbs -v PBS_ARRAYID=${PBS_ARRAYID}
    fi
    ```
- **Variable Passing**: Use the `-v` option with `qsub` to pass variables to the resubmitted job.
- **Timing Job Array**: It is not feasible to stretch the submission of array jobs over time under the same job ID without wasting resources. Consider submitting smaller groups of array items with separate job IDs and a time delay.

## Keywords
- MATLAB license error
- PBS job array
- License checkout failed
- Job retry mechanism
- qsub resubmit
- Variable passing in PBS
- Timing job array submission

## General Learning
- Understanding how to handle license checkout errors in HPC environments.
- Implementing job retry mechanisms in PBS batch scripts.
- Passing variables between job submissions using `qsub`.
- Managing job array submissions to optimize resource usage.
---

### 2023111442003785_matlab%20fritz.md
# Ticket 2023111442003785

 ```markdown
# HPC-Support Ticket: MATLAB Module Permission Issue

## Keywords
- MATLAB
- Module Load
- Permission Denied
- License Issue

## Problem Description
- User encountered a "Permission denied" error when attempting to load the MATLAB module on the HPC system.
- Error message: `ERROR: Permission denied on '/apps/modules/data/applications/matlab'`
- User has a MATLAB license through the university but is unsure how to register it on the HPC system.

## Root Cause
- The issue was related to permissions on the MATLAB module directory.

## Solution
- HPC Admin resolved the permission issue, allowing the user to load the MATLAB module successfully.

## Lessons Learned
- Permission issues can prevent users from accessing software modules.
- HPC Admins can resolve such issues by adjusting permissions on the relevant directories.
- Users should be informed about how to register their licenses if required.

## Actions Taken
- HPC Admin adjusted permissions on the MATLAB module directory.
- User confirmed that the issue was resolved and the MATLAB module could be loaded successfully.

## Follow-up
- Ensure that users are aware of the process for registering their software licenses on the HPC system.
- Regularly review and update permissions on software module directories to prevent similar issues.
```
---

### 2022012742001514_Aktivierung%20Matlab-Modul.md
# Ticket 2022012742001514

 ```markdown
# HPC-Support Ticket: Activation of Matlab Module

## Keywords
- Matlab
- License
- Module
- Woody-Cluster
- License Manager Error -39
- LM_PROJECT
- Campuslizenz

## Summary
A user requested access to the Matlab module on the Woody-Cluster but encountered issues with license activation.

## Problem
- User could not find the Matlab module in the module list.
- After the module was made available, the user encountered a license error (License Manager Error -39).

## Root Cause
- The Matlab module was not initially visible to the user.
- The user's individual license was not compatible with the HPC cluster, requiring a network license.

## Solution
- HPC Admins added the Matlab module to the user's access.
- The user's departmental network license information was added to the system.
- The user was advised to contact their departmental supervisor or responsible personnel if the license issue persisted.

## Lessons Learned
- Individual Matlab licenses are not compatible with the HPC cluster; network licenses are required.
- The `LM_PROJECT` variable may not be necessary in the `modinclude/matlab/*` directory.
- The license server should be defined in the `modinclude` file.
- Global visibility of Matlab should be managed carefully to avoid unauthorized access.

## Actions Taken
- Added the Matlab module to the user's access.
- Updated the license information for the user's department.
- Advised the user to contact their departmental supervisor for further assistance.

## Notes
- The license server is globally defined in `/apps/matlab/R2020b/licenses/network.lic`.
- Care should be taken to ensure that Matlab is not made globally visible despite the campus license.
```
---

### 2022051242002598_Matlab.md
# Ticket 2022051242002598

 # HPC Support Ticket: Matlab Licensing

## Keywords
- Matlab
- Licensing
- HPC Clusters
- Campus License
- Costs

## Summary
- **User Inquiry**: The user inquired about the current status of Matlab licensing on HPC clusters, specifically regarding the campus license.
- **HPC Admin Response**: The HPC Admin informed the user that the HPC systems are currently covered by a centrally financed Matlab license. The continuation of this license is decided annually, and the costs have been increasing by approximately 50% each year, suggesting that the license may be discontinued in the future.

## Root Cause
- The user was concerned about the availability and licensing of Matlab on HPC clusters.

## Solution
- The HPC Admin clarified that the HPC systems are currently covered by a centrally financed Matlab license, but the future of this license is uncertain due to rising costs.

## General Learnings
- Matlab licensing on HPC clusters is subject to annual review and may be discontinued due to increasing costs.
- Users should be aware that the availability of Matlab on HPC systems may change in the future.

## Next Steps
- Users should plan their projects with the understanding that Matlab licensing on HPC clusters may not be guaranteed indefinitely.
- HPC Admins should keep users informed about any changes in licensing agreements that may affect their work.
---

### 2022120142001551_RE%3A%20Not%20able%20to%20load%20module%20MATLAB.md
# Ticket 2022120142001551

 # HPC Support Ticket: Not Able to Load Module MATLAB

## Keywords
- MATLAB
- Module Load
- Woody Cluster
- ACLs
- Spack Packages

## Issue
- User unable to load MATLAB module on Woody cluster.
- Error message: `ERROR: Unable to locate a modulefile for 'matlab/R2022a'`

## Root Cause
- MATLAB installation was not available on Woody-NG despite ACLs being set.

## Solution
- HPC Admins installed MATLAB on Woody-NG.
- User was advised to try loading the module again.
- Note: Loading "000-all-spack-pkgs" is not necessary.

## General Learnings
- Ensure software is installed on the cluster before setting ACLs.
- Specific module loading does not require loading all Spack packages.
- Communicate installation status and updates to users promptly.
---

### 2024121542000595_MATLAB%20Licensing%20Issue%20on%20Alex.md
# Ticket 2024121542000595

 ```markdown
# HPC-Support Ticket: MATLAB Licensing Issue on Alex

## Keywords
- MATLAB Licensing
- Alex HPC System
- Flat-rate License
- License Server
- ACLs
- NHR Documentation

## Problem
- **User Issue**: Encountering a licensing error while attempting to use MATLAB on Alex.
- **Root Cause**: Personal MATLAB licenses are not supported on the system.

## Solution
- **Admin Actions**:
  - Enabled MATLAB access for the user's account.
  - Set up license prefix and ACLs for the user.
  - Informed the user about the temporary nature of the flat-rate license and potential future requirements.

## General Learnings
- **License Management**:
  - Central financing of the flat-rate MATLAB campus license is guaranteed until March 2025.
  - After this date, users may need to purchase network licenses.
- **User Communication**:
  - Inform users about the temporary nature of the license and potential future costs.
  - Encourage users to consider alternatives to MATLAB for long-term use.

## Notes
- **Documentation**: Review NHR documentation for licensing policies.
- **Future Considerations**: Users should be prepared to purchase network licenses or explore other software options after the flat-rate license expires.
```
---

### 2021030842001165_Matlab%20auf%20dem%20HPC%20Cluster.md
# Ticket 2021030842001165

 # HPC Support Ticket: Matlab auf dem HPC Cluster

## Keywords
- Matlab
- HPC Cluster
- Module Activation
- License Management
- Cluster Access

## Problem
- User needs to activate Matlab to access the corresponding modules.
- User has Matlab licenses under LM_PROJECT iwi3 at their department.

## Solution
- HPC Admin activated Matlab for the user on the woody cluster.
- User requested additional access to the tinyx cluster.
- HPC Admin granted access to Matlab on all tinyX nodes.

## General Learnings
- Matlab activation requires HPC Admin intervention.
- License usage on HPC clusters may compete with departmental licenses.
- Users should specify which clusters they need access to for Matlab.

## Root Cause
- Matlab modules were not initially activated for the user.

## Resolution
- HPC Admin activated Matlab modules for the user on the specified clusters.

## Notes
- Ensure users are aware of potential license conflicts between HPC clusters and departmental licenses.
- Users should communicate their specific cluster needs to HPC Admins for proper access configuration.
---

### 2022020342002048_outdated%20Matlab%20Version.md
# Ticket 2022020342002048

 ```markdown
# HPC-Support Ticket: Outdated Matlab Version

## Keywords
- Matlab
- GPU Support
- Forward Compatibility
- Ampere GPU
- R2021b Update 2

## Root Cause
- The installed Matlab version on TinyGPU required enabling forward compatibility to support the latest GPU generation, leading to incompatibilities and the need to recompile GPU libraries each time Matlab was used.

## Solution
- HPC Admin installed Matlab R2021b (Update 2), which resolved the compatibility issues and allowed seamless computation on Ampere GPU without any workarounds.

## General Learnings
- Updating Matlab to a newer version can resolve compatibility issues with the latest GPU generations.
- Forward compatibility settings in older Matlab versions can cause significant usability problems.
- Always check for the latest Matlab updates when encountering GPU support issues.
```
---

### 2024121142002724_MATLAB%20Licensing%20Issue%20on%20Alex.md
# Ticket 2024121142002724

 ```markdown
# HPC-Support Ticket: MATLAB Licensing Issue on Alex

## Keywords
- MATLAB
- Licensing Issue
- Alex Cluster
- Ticket Merge

## Summary
- **Root Cause**: The user encountered a licensing issue with MATLAB on the Alex cluster.
- **Solution**: The ticket was merged with another related ticket for further investigation and resolution.

## Details
- **HPC Admins**: Merged ticket "2024121142002724" with "2024121542000595" for consolidated handling.
- **Next Steps**: The merged ticket will be addressed to resolve the MATLAB licensing issue on the Alex cluster.

## Learning Points
- **Ticket Management**: Merging related tickets can streamline the resolution process.
- **MATLAB Licensing**: Issues with MATLAB licensing on HPC clusters may require consolidated efforts from multiple support teams.
```
---

### 42179408_MATLAB%20Compiler%20Runtime.md
# Ticket 42179408

 # HPC-Support Ticket: MATLAB Compiler Runtime

## Keywords
- MATLAB Compiler Runtime (MCR)
- Licensing
- Parallel Computing Toolbox
- Windows Cluster

## Summary
A user requested information about installing the MATLAB Compiler Runtime (MCR) on the HPC server to run compiled MATLAB programs under a Windows operating system. The HPC support needed clarification on whether the existing license agreement allowed for this installation.

## Root Cause
- The user needed to ensure that the MCR could be installed on the HPC server without violating any licensing agreements.

## Solution
- **Licensing**: The MCR does not require a license. It is essential that the release of the MCR and the compiled MATLAB program are identical, as well as the hardware architecture (32/64 Bit).
- **Parallel Computing**: Information on using the Parallel Computing Toolbox in a compiled application can be found on the MathWorks support page.

## Additional Notes
- The HPC Admin provided links to relevant MathWorks resources for further information.
- The status of the official support for the HPC-Windows cluster was unclear, with speculation that someone might have handled it, but no definitive information was available.

## References
- [MathWorks MCR Information](http://www.mathworks.de/products/compiler/mcr/index.html)
- [MathWorks Support Solutions](http://www.mathworks.de/support/solutions/en/data/1-9D3XVH/index.html)
- [MathWorks Service Requests](http://www.mathworks.de/myservicerequests)

## Next Steps
- Ensure that the MCR and the compiled MATLAB program versions match.
- Refer to the MathWorks support page for parallel computing toolbox usage in compiled applications.
- Clarify the official support status for the HPC-Windows cluster.
---

### 2022112142001195_Not%20able%20to%20load%20module%20MATLAB.md
# Ticket 2022112142001195

 # HPC Support Ticket: Not Able to Load Module MATLAB

## Keywords
- MATLAB
- Module Load
- Woody Cluster
- License Activation
- Modulefile Error

## Problem Description
- User unable to load MATLAB module on Woody cluster.
- Error message: `ERROR: Unable to locate a modulefile for 'matlab/R2022a'`
- User has activated MATLAB license and tried loading `000-all-spack-pkgs`.

## Root Cause
- The user's group was not initially enabled for MATLAB on the Woody cluster.

## Solution
- HPC Admin enabled the user's group for MATLAB on Woody.

## Lessons Learned
- Ensure that the user's group has the necessary permissions and access to the required software modules.
- Verify that the module name and version are correct and available on the cluster.
- Check for any prerequisites or additional steps required for loading specific modules.

## Actions Taken
- HPC Admin enabled the user's group for MATLAB access.

## Follow-up
- User should retry loading the MATLAB module after the group has been enabled.
- If the issue persists, further investigation into the module configuration may be required.
---

### 2024121142002715_MATLAB%20Licensing%20Issue%20on%20Alex.md
# Ticket 2024121142002715

 ```markdown
# HPC-Support Ticket: MATLAB Licensing Issue on Alex

## Keywords
- MATLAB
- Licensing Issue
- Alex (HPC Cluster)
- Ticket Merging

## Summary
This ticket addresses a MATLAB licensing issue encountered on the Alex HPC cluster. The ticket was merged with another related ticket to streamline the support process.

## Root Cause
- The user experienced issues with MATLAB licensing on the Alex HPC cluster.

## Solution
- The HPC Admins merged the ticket with another related ticket (`2024121142002724`) to consolidate the support efforts.

## Lessons Learned
- Merging related tickets can help in efficiently managing and resolving issues.
- Licensing issues with software like MATLAB on HPC clusters require coordinated efforts from the support team.

## Next Steps
- Ensure that the merged tickets are addressed promptly to resolve the licensing issue.
- Document any specific steps taken to resolve the licensing issue for future reference.
```
---

### 2021101142001403_Matlab.md
# Ticket 2021101142001403

 # HPC Support Ticket: Matlab Parallel Script

## Keywords
- Matlab
- Parallel Script
- Server Availability
- Woody
- TinyFat
- Emmy

## Problem
- User has a Matlab script that can run in parallel mode.
- User inquires about server availability to run Matlab scripts.

## Solution
- Matlab is available on Woody, TinyFat, and Emmy servers.
- Note: Matlab Parallel Server is not available on these servers.

## General Learnings
- Matlab can be run on specific HPC servers.
- Parallel scripts can be executed, but Matlab Parallel Server is not supported.
- Users should be directed to the appropriate servers for their needs.

## Root Cause
- User needed information on server availability for running Matlab scripts in parallel mode.

## Resolution
- HPC Admin provided information on available servers for running Matlab scripts.

## Next Steps
- Users should check server documentation for specific capabilities and limitations.
- Further inquiries can be directed to HPC Support for detailed assistance.
---

### 2019091642003034_matlab2017%20Nutzung%20am%20HPC.md
# Ticket 2019091642003034

 ```markdown
# HPC-Support Ticket: Using MATLAB 2017b on HPC Cluster

## Keywords
- MATLAB 2017b
- HPC Cluster
- Batch Script
- Interactive Job
- X-forwarding
- RRZE FAQs

## Problem
- User wants to use MATLAB 2017b on the HPC cluster to analyze HPC-LES-Fluent calculations.
- User couldn't find specific FAQs or batch script templates for MATLAB usage on the cluster.

## Solution
- **Information Source**: [RRZE MATLAB Guide](https://www.anleitungen.rrze.fau.de/hpc/special-applications-and-tips-tricks/matlab/)
- **Cluster Selection**:
  - **Woody**: Suitable for MATLAB evaluations due to single-node parallel execution.
  - **Emmy**: Preferred if large data sets are stored on Emmy's FASTTMP.
- **Batch Jobs**:
  - Short calculations can be done on frontends.
  - Longer calculations require batch jobs.
  - Example batch script available on the linked page.
- **Interactive Jobs**:
  - Use `qsub -l nodes=1:ppn=40 -I -X` for interactive jobs with X-forwarding.
  - For nodes with graphics libraries, use `qsub -l nodes=1:ppn=40:phi`.

## General Learnings
- MATLAB can be used on HPC clusters for data analysis.
- Cluster selection depends on data location and size.
- Batch jobs are necessary for longer calculations.
- Interactive jobs with X-forwarding are an option for graphical MATLAB usage.
```
---

### 2024052742003485_MATLAB%20on%20Fritz.md
# Ticket 2024052742003485

 # HPC-Support Ticket: MATLAB on Fritz

## Keywords
- MATLAB
- Fritz
- Module
- License
- Activation

## Problem
- User unable to find MATLAB module on Fritz, only 'matlab-runtime/r2022a' available.
- User requests activation of MATLAB module as per documentation.

## Conversation Summary
- **User**: Requests access to MATLAB module on Fritz.
- **HPC Admin**: Checks the status of MATLAB license.
- **HPC Admin**: Informs user that MATLAB modules are now available. Warns about the upcoming termination of network licenses for MATLAB.

## Solution
- HPC Admin activated the MATLAB modules, making them available to the user.

## General Learnings
- MATLAB modules may need activation upon user request.
- Network licenses for MATLAB will be terminated in the near future, affecting availability on HPC systems.
- Personal licenses won't be usable on HPC systems.

## Follow-up Actions
- Users should be aware of the upcoming license changes and plan their work accordingly.
- HPC Admins should monitor and update users about significant changes in software licenses.
---

### 2015110642000406_Matlab%20im%20HPC.md
# Ticket 2015110642000406

 ```markdown
# HPC Support Ticket: Matlab Access on HPC

## Keywords
- Matlab
- HPC
- Module System
- License
- Woody

## Problem
- User unable to find Matlab installation on HPC.
- User has a university license for Matlab.

## Root Cause
- User was unaware of how to access Matlab through the module system on the HPC cluster.

## Solution
- HPC Admin informed the user that Matlab can be accessed on the Woody cluster through the module system.

## Lessons Learned
- Users should be informed about the module system for accessing software on HPC clusters.
- Ensure that documentation and user guides include information on how to access licensed software through the module system.

## Actions Taken
- HPC Admin provided instructions to access Matlab via the module system.
- Ticket closed as the user was satisfied with the solution.
```
---

### 2024031242002571_MATLAB%20job%20submission%20file.md
# Ticket 2024031242002571

 ```markdown
# HPC-Support Ticket: MATLAB Job Submission File

## Keywords
- MATLAB
- SLURM batch script
- MATLAB runtime
- Cluster
- Documentation

## Problem
- User wants to run MATLAB codes on the cluster.
- User is unsure if MATLAB is installed on the cluster or if they need to use MATLAB runtime.
- User requests a SLURM batch script to run a test MATLAB code or executable on multiple nodes.

## Solution
- HPC Admin directs the user to the documentation for MATLAB on the cluster.
- Documentation link provided: [MATLAB Documentation](https://doc.nhr.fau.de/apps/matlab/)

## What Can Be Learned
- Always check the documentation for software availability and usage instructions.
- SLURM batch scripts for MATLAB can be found in the documentation.
- MATLAB runtime may not be necessary if MATLAB is already installed on the cluster.

## Root Cause
- Lack of awareness about the availability of MATLAB on the cluster and how to submit MATLAB jobs using SLURM.

## Next Steps
- Review the provided documentation for detailed instructions on running MATLAB jobs.
- If further questions arise, contact the HPC support team for additional assistance.
```
---

### 2022110742001855_Matlab%20NHR-Projekt%20b136dc.md
# Ticket 2022110742001855

 ```markdown
# HPC Support Ticket: Matlab Installation for NHR Project

## Keywords
- Matlab
- NHR Project
- Installation
- Version 2022a
- Fritz

## Summary
A user requested the installation of Matlab version 2022a for their NHR project.

## Root Cause
The user required Matlab for their project and needed a specific version installed on the HPC system.

## Solution
The HPC Admin installed Matlab version 2022a on the Fritz system, making it available for accounts associated with the NHR project.

## What Can Be Learned
- Users may request specific software versions for their projects.
- HPC Admins can install requested software versions on the HPC system.
- Communication between users and HPC Admins is essential for fulfilling software requests.
```
---

### 2021122142002256_Matlab%20on%20TinyGPU.md
# Ticket 2021122142002256

 # HPC Support Ticket: Matlab on TinyGPU

## Keywords
- Matlab
- TinyGPU
- TinyFat
- Campuslicense
- Concurrent license server
- Tesla cards

## Summary
- **User Request**: Enable Matlab on TinyGPU and TinyFat for a specific HPC account.
- **Priority**: TinyGPU is the priority due to efficient utilization of Tesla cards.
- **Licensing**: University has a Campuslicense, and the chair has an entry at the concurrent license server.

## Root Cause
- User needs access to Matlab on specified clusters for efficient computation.

## Solution
- HPC Admin enabled Matlab on the requested clusters.

## Notes
- The ticket was marked as completed (erledigt) with no further issues reported.
- Ensure proper licensing and cluster access for future similar requests.

## References
- [MATLAB Campusvertrag für Studierende und Forschende der FAU und des Universitätsklinikums Erlangen](https://www.rrze.fau.de/hard-software/software/dienstliche-nutzung/produkte/matlab/#matlabconcurrent)
---

### 2022090642000782_Fehlende%20Gui%20von%20Matlab%20auf%20Woody-ng.md
# Ticket 2022090642000782

 # HPC Support Ticket: Missing MATLAB GUI on Woody-NG

## Keywords
- MATLAB GUI
- Woody-NG
- Segmentation fault
- Library issues
- Configuration data

## Problem Description
- User unable to start MATLAB GUI on Woody-NG.
- Initial issue due to missing libraries.
- After library installation, GUI crashes with "Segmentation fault (core dumped)".

## Root Cause
- Missing libraries for MATLAB GUI.
- Corrupted or outdated local configuration data in the user's account.

## Solution
1. **Install Missing Libraries**:
   - HPC Admins identified and installed the missing libraries required for the MATLAB GUI.

2. **Delete Local Configuration Data**:
   - User was instructed to delete the local MATLAB configuration data located in `$HOME/.matlab/R2022a`.
   - This resolved the segmentation fault issue.

## Steps to Reproduce and Troubleshoot
1. **Check for Missing Libraries**:
   - Run `/apps/matlab/R2022a/bin/glnxa64/MATLABWindow` to get detailed error messages about missing libraries.

2. **Delete Local Configuration Data**:
   - Navigate to `$HOME/.matlab/R2022a` and delete the configuration files.
   - Restart MATLAB to see if the issue is resolved.

## Conclusion
- The issue was resolved by installing missing libraries and deleting corrupted local configuration data.
- For future reference, use the provided command to identify missing libraries and ensure local configuration data is up-to-date.

## Ticket Status
- Closed after successful resolution of the issue.
---

### 2022110742003157_Matlab%20module%20verschwunden.md
# Ticket 2022110742003157

 # HPC Support Ticket: Matlab Module Issue

## Keywords
- Matlab module
- License error
- Account access
- FRASCAL-Projekt
- Certificate expiration

## Problem Description
- User reported that the Matlab module (matlab/R2022a) was missing from their primary account (iwtm017h).
- User also reported a license error when attempting to use Matlab with their FRASCAL-Projekt account (b136dc10).

## Root Cause
- The Matlab module was not available in the user's primary account.
- License settings were not configured for the FRASCAL-Projekt account.

## Solution
- HPC Admin resolved both issues.
  - Restored the Matlab module for the primary account.
  - Configured license settings for the FRASCAL-Projekt account.

## Steps Taken
1. User reported the issue via email.
2. HPC Admin acknowledged the problem and resolved it.
3. HPC Admin confirmed the resolution to the user.

## Lessons Learned
- Ensure that software modules are correctly configured and accessible for all relevant user accounts.
- Regularly check and update license settings to avoid errors.
- Prompt communication between users and HPC support is crucial for quick resolution of issues.

## Follow-Up
- Monitor the availability of software modules and license settings.
- Provide clear instructions to users on how to report and resolve similar issues in the future.
---

### 2023091242003873_MATLAB%20auf%20Woody.md
# Ticket 2023091242003873

 ```markdown
# HPC Support Ticket: MATLAB auf Woody

## Keywords
- MATLAB
- Module Load Error
- License Settings
- Permission Denied
- LM_PREFIX
- Freischaltung

## Problem Description
A user encountered an error while trying to load the MATLAB module on the Woody cluster. The error message indicated a permission issue with the license file.

## Error Message
```
Module ERROR: couldn't read file "/apps/modules/5.1.1/modincludes/matlab/license-iwb0": permission denied
```

## Root Cause
- The user did not have the necessary permissions to access the license file.
- The LM_PREFIX for the user's group was not correctly set up.

## Solution
1. **LM_PREFIX Setup**: The HPC Admin set the LM_PREFIX for the user's group (iwb0) on Woody.
2. **Freischaltung**: The user was instructed to request the activation of the MATLAB network license for their group from the software team.

## Steps Taken
1. The HPC Admin asked the user for the LM_PREFIX to be used by their group.
2. The user requested the activation of the MATLAB network license for their group.
3. The HPC Admin updated the LM_PREFIX settings on Woody.

## Additional Notes
- The user preferred to use a single LM_PREFIX for the entire department rather than individual professorships.
- The user also requested the setup for another group (iwb5) and initiated the activation process.

## Conclusion
The issue was resolved by setting the correct LM_PREFIX and requesting the necessary license activation. This process ensures that the MATLAB module can be loaded without permission errors.
```
---

### 2023040442000202_MATLAB%20license%20on%20HPC.md
# Ticket 2023040442000202

 # MATLAB License Issue on HPC

## Keywords
- MATLAB license
- HPC
- License Manager Error -39
- LM_PROJECT
- Institutional network license

## Problem
- User encountered a license error while trying to use MATLAB on HPC (tinyFat).
- Error message: "License checkout failed. License Manager Error -39 User/host not on INCLUDE list for MATLAB."
- User's batch file commands:
  ```bash
  module load matlab/R2021b
  matlab -nojvm -nodisplay -nosplash < my_matlab_script.m
  ```

## Root Cause
- The LM_PROJECT used for the license is no longer accepted by the license server.
- MATLAB on HPC systems cannot be linked to a personal license; it must use an institutional network license.

## Solution
- Check with local IT support to determine the correct LM_PROJECT for EMPKINS.
- Update the license settings with the new LM_PROJECT.

## Notes
- Personal MATLAB licenses cannot be used on HPC systems.
- Ensure the correct institutional network license is configured for MATLAB on HPC.

## Additional Information
- Contact HPC support for further assistance if needed.
- Ensure environment variables are correctly set for the institutional license.
---

### 42198852_HPC-Account.md
# Ticket 42198852

 # HPC Support Ticket: HPC-Account

## Keywords
- HPC Account Setup
- Module Loading
- Octave
- Matlab
- Performance Issues

## Summary
- **User Issue**: User unable to access Octave and Matlab after account setup.
- **Root Cause**: User did not load the required modules.
- **Solution**: Load the necessary modules using `module load <module_name>`.

## Detailed Conversation

### Initial Setup
- **HPC Admin**: Informed the user about the creation of an HPC account and provided instructions to set a password.
- **User**: Acknowledged the account setup and reported issues accessing Octave and Matlab.

### Module Loading
- **HPC Admin**: Advised the user to load the Octave module using `module load octave`.
- **User**: Confirmed that loading the module resolved the access issue but reported performance issues with Octave.

### Performance Issues
- **User**: Reported that Octave performance on the cluster was significantly slower compared to Matlab on a personal device.
- **HPC Admin**: No immediate solution provided for performance issues.

## Lessons Learned
- **Module Loading**: Ensure users are aware of the need to load modules for software access.
- **Performance Monitoring**: Investigate performance issues reported by users to identify potential bottlenecks or configuration problems.

## Next Steps
- **Documentation**: Update user guides to emphasize the importance of loading modules.
- **Performance Analysis**: Conduct further analysis to understand and address performance discrepancies between local and cluster environments.

## Additional Notes
- **Communication**: Ensure timely responses to user queries and follow up on unresolved issues.
- **Training**: Provide training sessions or documentation on module usage and performance optimization for HPC users.

---

This report aims to assist support employees in resolving similar issues related to HPC account setup, module loading, and performance troubleshooting.
---

### 2021092942000213_Anfrage%20zur%20Nutzung%20von%20MATLAB%20Parallel%20Server.md
# Ticket 2021092942000213

 # HPC Support Ticket Conversation: MATLAB Parallel Server Installation

## Subject
Anfrage zur Nutzung von MATLAB Parallel Server

## Keywords
MATLAB, Parallel Server, Lizenzserver, Flexlm-HostID, Campuslizenz, Lizenzdatei, Installation Key, Linux, CentOS 7, Lizenzfile, Concurrent Lizenzfile

## Summary
User requests installation of MATLAB Parallel Server on their departmental cluster. The conversation covers the process of obtaining a license, setting up a license server, and troubleshooting issues related to network connectivity and license files.

## Conversation Highlights

### Initial Request
- User requests MATLAB installation on their cluster.
- User believes a Parallel Server and a separate license server on the frontend are required.
- User inquires if this is covered by the campus license and requests a license for testing and potential permanent use.

### HPC Admin Response
- Confirms that MATLAB Parallel Server is included in the campus license.
- Mentions that MATLAB has been used without parallel features on HPC systems.
- Requests Flexlm-HostID of the license host to generate a license.

### User Actions
- Installs the license server and obtains the Flexlm-HostID.
- Provides the HostID and operating system details (Linux, CentOS 7).

### HPC Admin Actions
- Provides the File Installation Key and license file for MATLAB Parallel Server.
- Offers additional support and requests feedback on the installation process.

### Follow-up Issues
- User encounters issues with network connectivity for the compute nodes.
- User requires a license server for the entire MATLAB installation.

### Additional Support
- HPC Admin provides a Concurrent Lizenzfile for MATLAB.
- Offers to provide updated license files for the new version (2022a) if the user encounters delays.

## Root Cause of the Problem
- User needed a license for MATLAB Parallel Server and a separate license server for the entire MATLAB installation.
- Network connectivity issues with compute nodes required a local license server.

## Solution
- HPC Admin provided the necessary File Installation Key and license file for MATLAB Parallel Server.
- Additional Concurrent Lizenzfile was provided to address network connectivity issues.
- Offered to provide updated license files for the new version (2022a) if needed.

## General Learnings
- MATLAB Parallel Server is included in the campus license.
- Flexlm-HostID is required to generate a license.
- Network connectivity issues can be addressed by setting up a local license server.
- HPC Admin provides ongoing support and offers updated license files for new versions.

## Conclusion
The conversation highlights the process of obtaining and setting up a MATLAB Parallel Server license on a departmental cluster. It also covers troubleshooting network connectivity issues and the importance of having a local license server. The HPC Admin provided continuous support and offered updated license files for new versions.
---

### 2021081942001395_MATLAB%20Module.md
# Ticket 2021081942001395

 # HPC Support Ticket: MATLAB Module

## Keywords
- MATLAB Module
- TinyGPU
- Woody
- Deep Learning Toolbox
- ResNet-50 Network
- Add-On Explorer
- X-forwarding

## Problem
- User unable to see or use MATLAB module on TinyGPU and Woody nodes.
- Issue with installing Deep Learning Toolbox Model for ResNet-50 Network.

## Root Cause
- Initial lack of access to MATLAB module.
- Misunderstanding about the installation process for the ResNet-50 Network add-on.

## Solution
- HPC Admins granted access to MATLAB modules on Woody and TinyGPU.
- User guided to install the ResNet-50 Network add-on via the MATLAB GUI using X-forwarding.

## General Learnings
- Different nodes may have different MATLAB versions and operating systems.
- Users can install certain MATLAB add-ons themselves via the Add-On Explorer.
- X-forwarding is required to access the MATLAB GUI for add-on installation.

## Steps Taken
1. HPC Admins enabled MATLAB module access for the user.
2. User attempted to install Deep Learning Toolbox Model for ResNet-50 Network.
3. HPC Admins provided instructions for installing the add-on using the MATLAB GUI and X-forwarding.

## Notes
- Ensure users are aware of differences in software versions and environments across nodes.
- Provide clear instructions for installing user-specific add-ons and tools.
---

### 2021122342001342_Execute%20Matlab%20code.md
# Ticket 2021122342001342

 # HPC Support Ticket: Execute Matlab Code

## Keywords
- Matlab installation
- Matlab runtime
- Compiled Matlab code
- HPC cluster
- Module system
- Campus license

## Problem
- User inquires about executing Matlab code on an HPC cluster.
- No documentation found regarding Matlab on the specified cluster.

## Root Cause
- Lack of clear documentation and module availability for Matlab on the HPC cluster.

## Solution
- HPC Admin provides information about the availability of a Matlab module (`matlab/R2020b`).
- User is advised to check if the module is visible and to report any license issues.

## General Learnings
- Ensure documentation for software modules is up-to-date and accessible.
- Communicate the availability of specific software modules to users.
- Address potential licensing issues proactively.

## Next Steps
- User should verify the availability of the Matlab module and report any issues.
- HPC Admin should ensure the user's prefix is enabled for the Matlab campus license if required.
---

### 2021042142002655_Fwd%3A%20MATLAB-Lizenzen%20f%C3%83%C2%BCr%20Studierende.md
# Ticket 2021042142002655

 ```markdown
# HPC-Support Ticket: MATLAB Campus License Validity on HPC Cluster

## Keywords
- MATLAB Campus License
- HPC Cluster
- AMD EPYC 7502 Nodes
- License Cancellation

## Summary
A user inquired about the validity of the new MATLAB campus license on the HPC cluster, specifically on AMD EPYC 7502 nodes, and whether they could cancel their current departmental licenses.

## Root Cause
- User uncertainty about the applicability of the new MATLAB campus license on the HPC cluster.

## Solution
- The HPC Admin confirmed that the MATLAB campus license is valid on the HPC systems for the upcoming year.
- No changes are expected to be necessary for existing installations.
- License cancellation is not required; the software team will handle any refunds automatically.

## General Learnings
- New campus licenses often cover HPC systems, but details of implementation may not be immediately available.
- Users should not cancel existing licenses without confirmation from the HPC support team.
- The software team will handle refunds and license management once the new licenses are in place.

## References
- [MATLAB Campus License Information](https://www.fau.de/2021/04/news/studium/matlab-campus-lizenzen-fuer-studierende-und-forschende-der-fau/)
- [RRZE Software Products](https://www.rrze.fau.de/hard-software/software/private-nutzung/produkte/)
```
---

### 2015093042005031_Update%20von%20Matlab%20auf%20Woody.md
# Ticket 2015093042005031

 ```markdown
# HPC Support Ticket: Update von Matlab auf Woody

## Keywords
- Matlab Update
- Woody Server
- R2015b Installation
- Feedback Request

## Problem
- Current Matlab versions on Woody servers are R2011a and R2014a.
- User requests an update to a newer version, specifically R2015b.

## Actions Taken
1. **User Request**: User requests an update to Matlab R2015b.
2. **HPC Admin Communication**: HPC Admin requests the latest Matlab version to be made available for installation.
3. **Access Granted**: Temporary access to the download server is granted to facilitate the installation.
4. **Installation**: Matlab R2015b is installed on the Woody servers.
5. **Feedback Request**: User is asked to test the new version and provide feedback.
6. **User Feedback**: User confirms that the new Matlab version is working.

## Solution
- Matlab R2015b was successfully installed on the Woody servers.
- User tested the new version and confirmed its functionality.

## Lessons Learned
- Importance of keeping software up to date based on user requests.
- Coordination between different teams (HPC Admins, 2nd Level Support) for software updates.
- Necessity of user feedback to ensure the success of software updates.
```
---

### 42203643_matlab%20in%20cluster.md
# Ticket 42203643

 # HPC Support Ticket: Matlab Access on Cluster

## Keywords
- Matlab
- Cluster access
- License management
- Module loading
- RRZE software group

## Problem
- User needs Matlab for simulations on HPC clusters (Woody or Lima).
- Unsure about availability and required modules.

## Root Cause
- Matlab is commercial software requiring licensed access.
- User's group (WW8) needs verification for Matlab license eligibility.

## Solution
1. **License Verification**:
   - HPC Admins verified if WW8 group has rented Matlab licenses from RRZE's software group.
   - Confirmed that WW8 has Matlab licenses valid until a specific date.

2. **License Activation**:
   - HPC Admins coordinated with the software group to enable Matlab access on HPC systems for WW8.
   - Licenses were activated for HPC usage.

3. **Module Loading**:
   - User was informed about the available Matlab module (e.g., `matlab/R2011a`) and how to load it.

## General Learnings
- Commercial software like Matlab requires license verification and activation.
- Coordination between HPC Admins and the software group is essential for enabling software access.
- Users need to be informed about available modules and how to load them.

## Follow-up
- Ensure the user is aware of license limitations and concurrent usage restrictions.
- Provide clear instructions on module loading and usage.
---

### 2021101542002404_Fwd%3A%20Matlab%20License%20on%20RRZE%20cluster.md
# Ticket 2021101542002404

 # HPC Support Ticket: Matlab License on RRZE Cluster

## Keywords
- Matlab License
- RRZE Cluster
- Campus License
- Configuration File
- Module Load Error

## Summary
A user encountered an issue while trying to use Matlab on the RRZE cluster due to a missing license configuration. The HPC support team identified the root cause and provided a solution.

## Root Cause
- The user received an error message indicating that no license settings were known for their account when attempting to load the Matlab module.
- The error message: `ATTENTION: no license settings known for iwsp037h / iwsp`

## Solution
- The HPC support team identified that a configuration file was missing.
- The user was advised to try again after the missing configuration file was added.

## What Can Be Learned
- Ensure that all necessary configuration files are in place for software modules.
- Check the RRZE documentation for specific instructions on using Matlab on the cluster.
- Communicate with the HPC support team for any license-related issues.

## Documentation Link
- [RRZE Matlab Documentation](https://hpc.fau.de/systems-services/systems-documentation-instructions/special-applications-and-tips-tricks/matlab/#collapse_0)

## Support Team Involved
- HPC Admins
- 2nd Level Support Team

## Additional Notes
- The user was initially concerned about providing Matlab licenses in light of the campus license.
- The HPC support team resolved the issue by addressing the missing configuration file.

---

This report can be used as a reference for similar issues related to Matlab license configuration on the RRZE cluster.
---

### 2023062042002721_Matlab%20auf%20Fritz-Cluster%20-%20k107ce.md
# Ticket 2023062042002721

 ```markdown
# HPC-Support Ticket Conversation: Matlab auf Fritz-Cluster

## Summary
- **User**: Requested access to Matlab on the Fritz cluster for the StroemungsRaum project.
- **Issue**: Only Matlab Runtime was available, which required significant programming effort.
- **Solution**: After internal discussions and management decisions, the user was granted access to Matlab R2022a.

## Keywords
- Matlab
- Matlab Runtime
- Licensing
- Data Center Use
- FAU
- TU Dortmund
- NHR
- Fritz Cluster
- StroemungsRaum Project

## Lessons Learned
- **Licensing Complexity**: Matlab licensing for non-FAU members was unclear and required management decisions.
- **Alternative Software**: Octave was suggested as an alternative but was not suitable for the user's needs.
- **Technical Feasibility**: Accessing a license server from another institution (TU Dortmund) was technically feasible but required additional configurations.
- **Support Process**: The support process involved multiple steps, including internal discussions and management approvals.

## Root Cause of the Problem
- The user needed access to Matlab for simulations but only had access to Matlab Runtime, which was not sufficient.

## Solution
- The user was granted access to Matlab R2022a after the software group approved the request.
- The user was able to load and use Matlab successfully after the license settings were configured correctly.

## Conversation Highlights
- **Initial Request**: User requested access to Matlab for simulations.
- **Licensing Issues**: The FAU's Matlab campus license did not clearly cover non-FAU members.
- **Alternative Suggestions**: Octave was suggested but not suitable.
- **Technical Discussions**: Accessing TU Dortmund's license server was discussed but not pursued.
- **Final Approval**: The software group approved the request, and the user was granted access to Matlab.

## Conclusion
- The user was able to successfully use Matlab on the Fritz cluster after the licensing issues were resolved.
- The support process involved multiple steps and required internal discussions and management decisions.
```
---

### 2024121042003289_%E7%AD%94%E5%A4%8D%3A%20New%20invitation%20for%20%22Tier3%20Grundversorgung%20LS%20Dynamics%2C%20Con.md
# Ticket 2024121042003289

 # HPC Support Ticket Conversation Summary

## Keywords
- HPC Access
- Node Access
- MATLAB Usage
- SSH Key Upload
- Tier3 Account

## General Learnings
- **Access Levels**: Tier3 accounts have limited access to specific nodes.
- **MATLAB Availability**: MATLAB modules are available for use without additional activation.
- **SSH Key Requirement**: Users need to upload an SSH public key to access their accounts.

## Root Causes and Solutions

### Issue: Limited Node Access
- **Root Cause**: User has a Tier3 account, which does not include access to nodes like Fritz and Alex by default.
- **Solution**: Verify the available clusters and their access levels. [Overview of available clusters](https://doc.nhr.fau.de/clusters/overview/).

### Issue: MATLAB Usage
- **Root Cause**: User was unsure if MATLAB could be used on the terminal and if activation was required.
- **Solution**: MATLAB modules are available and should be visible to the user. No additional activation is needed.

### Issue: SSH Key Upload
- **Root Cause**: User needed to upload an SSH public key to access the account.
- **Solution**: Follow the instructions to upload the SSH key via the HPC portal. [Further information](https://doc.nhr.fau.de/hpc-portal/).

## Support Team Roles
- **HPC Admins**: Provide technical support and manage user accounts.
- **2nd Level Support Team**: Assist with user inquiries and troubleshooting.
- **Head of the Datacenter**: Oversee datacenter operations.
- **Training and Support Group Leader**: Lead training and support initiatives.
- **NHR Rechenzeit Support**: Handle computational time support and grant applications.
- **Software and Tools Developer**: Develop and maintain software tools for HPC.

## Documentation Links
- [HPC Portal Documentation](https://doc.nhr.fau.de/hpc-portal/)
- [Clusters Overview](https://doc.nhr.fau.de/clusters/overview/)

This summary can be used as a reference for future support tickets to quickly identify and resolve similar issues.
---

### 2023072742002993_Frage%20zur%20HPC%20Nutzung.md
# Ticket 2023072742002993

 # HPC Support Ticket: Frage zur HPC Nutzung

## Keywords
- Matlab
- Parallelisierung
- Intel MPI Library
- Intel Parallel Studio
- SLURM
- X11-forwarding
- Interaktive Matlab Session

## Problem
Der Nutzer versucht, eine Simulation in Matlab zu starten, die zur Parallelisierung die Intel MPI Library und Intel Parallel Studio benötigt. Die Matlab interne Parallel Computing Toolbox wird nicht verwendet. Der Code konnte die Intel MPI runtime libraries nicht finden.

## Fehlermeldung
Die Fehlermeldung war, dass der Code die Intel MPI runtime libraries nicht finden konnte.

## Lösung
1. **Interaktive Matlab Session starten:**
   - Mit X11-forwarding auf den woody Frontend einloggen:
     - Unter Linux: `ssh -X username@woody.nhr.fau.de`
     - Unter Windows: X11-forwarding in MobaXTerm (Session Settings -> Advanced SSH Settings)
     - Mittels NoMachineNX auf cshpc verbinden, dort ein Terminal öffnen und mit `ssh -X woody` verbinden
   - Matlab Modul laden und `matlab` ausführen.

2. **MPI Library installieren:**
   - In der interaktiven Matlab Session die Schritte 3 und 4 aus der Paramonte Dokumentation ausführen.
   - Wenn die MPI runtime nicht gefunden wird, die Installation durch Paramonte starten und als User installieren lassen.

3. **Batch-Modus:**
   - Matlab kann auch im Batch-Modus gestartet werden: `matlab -nojvm -nodisplay -nosplash`

## Ergebnis
Der Nutzer konnte die Simulation erfolgreich starten, nachdem die MPI Library lokal installiert wurde.

## Allgemeine Erkenntnisse
- Die Intel MPI Library aus dem Modul war möglicherweise zu neu oder nicht kompatibel mit Paramonte.
- Eine lokale Installation der MPI Library durch Paramonte war notwendig.
- Interaktive Matlab Sessions können mit X11-forwarding gestartet werden.
- Matlab kann auch im Batch-Modus ohne grafische Oberfläche gestartet werden.
---

### 2018052442000441_Matlab%20auf%20mehreren%20Nodes.md
# Ticket 2018052442000441

 ```markdown
# HPC-Support Ticket: Matlab auf mehreren Nodes

## Keywords
- Matlab
- Distributed Computing
- Licensing
- Array Jobs
- Woody-Cluster

## Problem
- User requires long processing times (up to 40 hours) for iterative image reconstruction in Matlab.
- Needs to apply reconstruction to multiple datasets on the Woody-Cluster.
- Questions:
  1. Can the computational load be distributed across multiple nodes without each node requiring a separate Matlab license?
  2. Can the availability of the required number of licenses be checked before job execution?

## Root Cause
- Matlab's licensing model and the lack of a "Matlab Distributed Computing Server" license at the university.

## Solution
- **Array Jobs**: Not suitable for distributing the computational load as they are essentially individual jobs.
- **Matlab Distributed Computing Server**: Potential solution but not available due to cost.
- **License Check**: The license server can be queried, but the batch system does not consider license availability when starting jobs.
- **Recommendation**: Consider moving away from Matlab to a more suitable platform for distributed computing.

## General Learnings
- Understanding the limitations of Matlab licensing in a distributed computing environment.
- The importance of checking license availability and the capabilities of the batch system.
- Exploring alternative software solutions for distributed computing tasks.
```
---

### 2022042942001372_Error%20when%20running%20the%20matlab%20function.md
# Ticket 2022042942001372

 # HPC Support Ticket: Error Running Matlab Function

## Keywords
- Matlab
- VideoReader
- Gstreamer
- TinyFat Cluster
- Package Reinstallation

## Problem Description
- **User Issue**: Error when running Matlab function for luminance equalization on video frames.
- **Error Message**: `Error using VideoReader/initReader (line 734) Video file I/O requires Gstreamer 1.0 and higher. Install this on your system and restart MATLAB.`
- **Cluster**: TinyFat Cluster

## Root Cause
- Required packages (Gstreamer 1.0 and higher) were lost during the last reinstallation of the TinyFat nodes.

## Solution
- **Action Taken by HPC Admin**: Reinstalled the required packages to ensure Matlab functionality.
- **Outcome**: Matlab should now work correctly.

## Follow-Up
- If the issue persists, the user should contact HPC support for further assistance.

## General Learning
- Ensure that necessary packages are permanently installed to avoid recurring issues after system reinstallations.
- Regularly check for and address any expired certificates or dependencies that may affect software functionality.
---

