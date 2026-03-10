# Topic 11: starccm_ansys_license_software_licenses

Number of tickets: 126

## Tickets in this topic:

### 2021070542004311_HPC%20Cluster%20Ansys%20Workbench.md
# Ticket 2021070542004311

 ```markdown
# HPC Cluster Ansys Workbench Support Ticket

## Keywords
- Ansys Workbench
- Linux
- HPC Cluster
- Emmy
- Accel-Queue
- Ansys Academic Licenses
- Research Licenses
- LM_PROJECT
- LM_LICENSE_FILE
- ANSYSLMD_LICENSE_FILE
- ANSYSLI_SERVERS

## Summary
A user inquired about running Ansys Workbench on the HPC cluster, specifically for simulations with response surfaces. The HPC Admin provided information about the challenges of running Ansys Workbench on Linux and suggested testing on the Emmy cluster using the Accel-Queue. Additionally, the user asked about using Ansys Academic Licenses on a desktop computer and the possibility of accessing both Academic and Research licenses simultaneously.

## Problem
- User wants to run Ansys Workbench on the HPC cluster for simulations with response surfaces.
- User needs to know if Ansys Academic Licenses can be used on a desktop computer.
- User wants to access both Academic and Research licenses simultaneously.

## Solution
- **Running Ansys Workbench on HPC Cluster:**
  - Ansys Workbench is not officially supported on the HPC cluster due to significant limitations under Linux.
  - The user can try running it on the Emmy cluster using the Accel-Queue with the command `qsub -X -I -q accel`.
  - Reference: [ANSYS on HPC Systems](https://doku.lrz.de/display/PUBLIC/ANSYS+on+HPC+Systems)

- **Using Ansys Academic Licenses on Desktop:**
  - The desktop computer needs to be registered by IP/Hostname or by setting `LM_PROJECT=903de9916019d94d`.
  - Example hostnames: `FMA-PC-039.fm.hs-coburg.de`

- **Accessing Both Academic and Research Licenses:**
  - Simultaneous use of both license pools is possible.
  - Set `LM_PROJECT` for campus licenses.
  - Configure license servers in `LM_LICENSE_FILE`, `ANSYSLMD_LICENSE_FILE`, and `ANSYSLI_SERVERS` by separating them with a colon.

## Additional Notes
- The HPC Admin mentioned that they cannot provide further assistance if issues arise with the license configuration.
- The last known usage of Ansys Workbench on the cluster was 5 years ago, indicating potential issues with missing libraries.

## Conclusion
The user was provided with steps to test Ansys Workbench on the Emmy cluster and configure licenses for both Academic and Research purposes. The HPC Admin highlighted the challenges and limitations of running Ansys Workbench on Linux-based HPC systems.
```
---

### 2021070742003158_Star-CCM%2B%20Simulationen%20auf%20Emmy.md
# Ticket 2021070742003158

 ```markdown
# HPC-Support Ticket: Star-CCM+ Simulationen auf Emmy

## Subject
Star-CCM+ Simulationen auf Emmy

## User Issue
- **Problem**: Star-CCM+ simulations occasionally fail to start without any apparent reason.
- **Details**: The job sometimes fails with a `java.lang.NullPointerException` error, but restarting the job without any changes often resolves the issue.
- **Attachments**: Job files and error logs (Scaling_a001.e1515875, Scaling_a001.e1515941).

## HPC Admin Response
- **Initial Response**: The issue appears similar to a previous ticket (Ticket#2021041342001206), but the root cause is still unknown.
- **Further Investigation**: No anomalies were found on the compute nodes involved in the failing job.
- **Recommendation**: Suggested contacting Siemens PLM Support for further assistance with the `java.lang.NullPointerException` error.

## Keywords
- Star-CCM+
- Simulation
- Emmy
- java.lang.NullPointerException
- Job failure
- Siemens PLM Support

## What Can Be Learned
- **Root Cause**: The exact cause of the intermittent job failures is unknown, but it is related to a `java.lang.NullPointerException` error.
- **Solution**: Restarting the job often resolves the issue. For persistent problems, contacting Siemens PLM Support is recommended.
- **General Advice**: Intermittent job failures with specific error messages may require vendor support for resolution.

## Next Steps
- **User**: Contact Siemens PLM Support for further assistance.
- **HPC Admin**: Monitor for similar issues and document any new findings.
```
---

### 2019070342004151_StarCCM%2B%202019%20version%20installation%20on%20Emmy.md
# Ticket 2019070342004151

 # HPC Support Ticket: StarCCM+ 2019 Installation on Emmy

## Keywords
- StarCCM+ 2019
- Optimate+
- Emmy
- Installation
- Adjoint Solver
- Script Free Automations

## Summary
A user requested the installation of the latest version of StarCCM+ 2019 on the Emmy cluster, highlighting new features such as an efficient adjoint solver and script-free automations. The user also inquired about the possibility of installing Optimate+, an add-on toolkit for StarCCM+.

## Root Cause
- User needed the latest version of StarCCM+ for advanced features.
- User required Optimate+ as an additional toolkit.

## Solution
- **HPC Admin** installed StarCCM+ 2019.2 on Emmy.
- **HPC Admin** noted that Optimate+ was retired after StarCCM+ 13.04 and is not available for the latest versions.

## General Learnings
- Always use the official email address for HPC requests.
- Stay updated with software release notes to understand the availability and retirement of features or add-ons.
- Communicate clearly with users about the availability and limitations of software versions and add-ons.

## Follow-up
- Inform users about the successful installation of StarCCM+ 2019.2.
- Advise users about the unavailability of Optimate+ in the latest versions and suggest alternatives if available.
---

### 2024030142002153_COMSOL%3F.md
# Ticket 2024030142002153

 # HPC Support Ticket: COMSOL Usage on Cluster

## Keywords
- COMSOL
- Cluster usage
- License
- Version 6.2
- Installation

## Summary
- **User Request:** Inquiry about using COMSOL on the HPC cluster for room simulations. Preference for version 6.2 due to performance issues with older versions.
- **HPC Admin Response:** COMSOL versions 6.0 and 6.1 are currently installed. Version 6.2 can be installed if necessary. User has one usage right according to the database.
- **Follow-up:** Version 6.2 was installed upon user request.

## Root Cause
- User needs to perform extensive room simulations using COMSOL, which would take months with their current setup.
- Preference for COMSOL version 6.2 due to performance improvements.

## Solution
- HPC Admin enabled COMSOL on the cluster for the user.
- Installed COMSOL version 6.2 as requested.
- User was informed about the availability of the required version.

## General Learnings
- **Cluster Software Installation:** HPC Admins can install specific software versions upon user request.
- **License Management:** Users need to have the appropriate licenses for software usage on the cluster.
- **Communication:** Effective communication between users and HPC Admins ensures that necessary software and versions are made available.

## Notes
- HPC Admins may not have specific experience with all software and cannot provide cluster-specific hints for every application.
- Users should plan for potential delays in software installation if specific versions are required.
---

### 2018071942001278_StarCCM%20GUI%20%3A%20License%20check%20%20failed%20%20on%20Emmy%20%20front%20node.md
# Ticket 2018071942001278

 # HPC Support Ticket: StarCCM+ GUI License Issue

## Keywords
- StarCCM+
- GUI
- License Error
- Emmy Cluster
- Front Node
- POD Key

## Problem Description
- User attempted to open StarCCM+ GUI and load a simulation file on Emmy cluster's front node.
- Error message: "Failed to get all licenses needed for this job. Asked for 1 license of ccmpower."

## Root Cause
- Possible misconfiguration in starting StarCCM+, specifically not specifying the correct POD key.

## Solution
- Ensure that when starting StarCCM+, the user specifies to use POD and provides the correct POD key.

## Additional Information
- Other users have successfully run the StarCCM+ GUI on the Emmy frontend, indicating no general issue with the system.
- The HPC Admin suggested checking the configuration settings for starting StarCCM+.

## Steps for Resolution
1. Verify that StarCCM+ is configured to use POD.
2. Ensure the correct POD key is specified when starting StarCCM+.
3. If the issue persists, consult with colleagues who have successfully run the GUI for additional troubleshooting steps.

## Conclusion
Proper configuration of StarCCM+ to use POD with the correct key is essential for obtaining the necessary licenses. This ticket can serve as a reference for similar license-related issues in the future.
---

### 2022112842003733_Probleme%20bei%20der%20HPC%20Nutzung.md
# Ticket 2022112842003733

 # HPC Support Ticket: Probleme bei der HPC Nutzung

## Keywords
- Simulation
- Star CCM+
- Floating point error
- Incompatible version
- $HOME directory
- $WORK directory
- HPC storage documentation

## Problem Description
The user is experiencing issues with simulations breaking repeatedly. The simulations are being run using Star CCM+ software on the HPC cluster.

## Root Cause
- Floating point error in the simulation files.
- Incompatible version of the simulation files.

## Details
- **User:** Stefan Formann
- **Cluster:** ssh meggie
- **Software:** Star CCM+
- **Job IDs:** 1000.o2043431, 100.o2043241
- **Error Messages:**
  - A floating point error has occurred.
  - DynamicLoader version 72: Restore error: incompatible version

## Solution
- The user should check the simulation files for errors and ensure they are using a compatible version.
- The user should switch from using the $HOME directory to the $WORK directory for future calculations, as the $HOME directory is not designed for this purpose and has limited storage.

## Additional Information
- Documentation on available filesystems and their intended use can be found [here](https://hpc.fau.de/systems-services/documentation-instructions/hpc-storage/).

## Follow-up Actions
- The user should review and correct the simulation files.
- The user should move future calculations to the $WORK directory.

## Support Team Involved
- HPC Admins
- 2nd Level Support Team
---

### 2022052642000751_HPC%20Modul%20Star%20CCM%20Gruppe%20Becker.md
# Ticket 2022052642000751

 ```markdown
# HPC Support Ticket: Star CCM Module Access Issue

## Keywords
- HPC Access
- Module Access
- Star CCM License
- iwst Account
- iwpa Account
- LSTM Group

## Problem Description
- A student (Julian Benz) recently received HPC access for Meggie (iwst079h) but could only access open-source software modules.
- The user noticed that the student did not have access to the Star CCM license, which was previously available under the iwpa account.

## Root Cause
- The iwst accounts have different module access configurations compared to iwpa accounts.
- Specific modules, such as Star CCM, need to be explicitly enabled for iwst accounts.

## Solution
- HPC Admins confirmed that all iwst accounts should now have access to Star CCM on Meggie.
- Users are advised to note on their HPC applications if they require iwpa-HPC accounts for simplified access to shared data, regardless of their new affiliation with LSTM.

## General Learnings
- Module access configurations differ between iwst and iwpa accounts.
- Specific module access may need to be requested and enabled by HPC Admins.
- Users should specify their requirements on HPC applications to ensure appropriate access.

## Follow-up Actions
- Users should verify that the required modules are accessible after the changes.
- For future requests, users should clearly state their module requirements in the HPC application.
```
---

### 2023051642002543_Query%20regarding%20registering%20for%20HPC%20usage%20for%20thesis%20work.md
# Ticket 2023051642002543

 # HPC Support Ticket: Query Regarding HPC Usage for Thesis Work

## Keywords
- HPC Access
- Ansys Fluent
- Thesis Work
- Licensing
- Application Process

## Problem
- User requires HPC access for running Ansys Fluent simulations for thesis work.
- Unaware of the application process and licensing requirements.

## Root Cause
- Lack of knowledge about the HPC account application process.
- Misunderstanding about Ansys licensing for thesis work.

## Solution
- **Application Process**: The application for an HPC account must be done through the user's supervisor or chair.
- **Licensing**: Research licenses for Ansys are mandatory for thesis work. Teaching licenses cannot be used and cannot be combined with HPC licenses.
- **Software Licenses**: The chair must ensure that enough Ansys licenses are booked from the RRZE's software group, as the HPC clusters do not have their own Ansys licenses.

## General Learnings
- HPC account applications should be routed through the appropriate academic supervisor or chair.
- Understanding the licensing requirements for specific software (e.g., Ansys Fluent) is crucial for compliance and proper usage.
- Communication with the HPC support team can clarify any doubts regarding the application process and licensing.

## Next Steps
- User should contact their supervisor to initiate the HPC account application process.
- Ensure that the necessary research licenses for Ansys are obtained through the RRZE's software group.

## References
- [FAU HPC Support](mailto:support-hpc@fau.de)
- [FAU HPC Website](https://hpc.fau.de/)
---

### 42349862_Problem%20mit%20Lima%20Cluster.md
# Ticket 42349862

 # HPC Support Ticket: Problem with Lima Cluster

## Keywords
- Lima Cluster
- Simulation
- License Error
- STAR-CCM+
- PowerOnDemand (POD)
- Interactive Job
- CCMARGS

## Problem Description
- User unable to run simulation on Lima Cluster.
- Error message: "Failed to get all licenses needed for this job. Asked for 1 licenses of ccmpsuite."

## Root Cause
- Incorrect CCMARGS configuration in the PBS script.
- STAR-CCM+ requires explicit instruction to use Power-Sessions for PowerOnDemand (POD).

## Solution
- Modify the CCMARGS line in the PBS script:
  ```
  CCMARGS="-load WLE800Lt1_start.sim -power -podkey dNle1S/qieQb6DC+8GBkQUTqQz0"
  ```
- Ensure that the `-power` flag is included to instruct STAR-CCM+ to use Power-Sessions.

## Additional Information
- User inquired about the possibility of monitoring the current state of CCM+ using an "Interactive Job."

## General Learning
- Proper configuration of CCMARGS is crucial for running simulations with STAR-CCM+.
- Understanding the specific requirements for PowerOnDemand (POD) sessions is important for successful job execution.
- Interactive jobs can be used to monitor the progress of simulations in CCM+.

## References
- HPC Services, Friedrich-Alexander-Universitaet Erlangen-Nuernberg
- Regionales RechenZentrum Erlangen (RRZE)
- [HPC Support](http://www.hpc.rrze.fau.de/)
---

### 2024022742000779_Fritz%20STAR-CCM%2B%202020.2.md
# Ticket 2024022742000779

 # HPC Support Ticket: STAR-CCM+ 2020.2 on Fritz

## Keywords
- STAR-CCM+
- Version 2020.2
- Fritz
- Module
- Permissions
- Slurm

## Problem
- User unable to find STAR-CCM+ 2020.2 module on Fritz.
- User lacks permissions in the apps directory.

## Root Cause
- STAR-CCM+ 2020.2 is not available on Fritz due to compatibility issues with the processors and interconnect.

## Solution
- HPC Admin granted access to view available STAR-CCM+ modules.
- Informed the user that STAR-CCM+ 2020.2 is not supported on Fritz.

## General Learnings
- Ensure software versions are compatible with the HPC system's hardware.
- Check available modules and versions before attempting to run simulations.
- Contact HPC support for access permissions and software availability inquiries.
---

### 2018110742000266_Clarification%20in%20star%20ccm%2B.md
# Ticket 2018110742000266

 # HPC Support Ticket: Clarification in STAR-CCM+

## Keywords
- STAR-CCM+
- Simulation
- Iteration Counts
- Object File
- Job Monitoring
- Model Setup
- Node Performance

## Problem Description
- User is running a simulation in STAR-CCM+.
- Restarted the simulation from stopped iterations.
- No iteration counts visible in the object file.
- Previous run created `.sim` and `.trk` files; simulation restarted without `.trk` file.
- Job statistics show the simulation is running, but no iterations are recorded.

## HPC Admin Response
- HPC team does not use STAR-CCM+ and cannot answer product-specific questions.
- Job 1006725 appears strange in system monitoring.
- Previous jobs (`km_trials`) showed unhealthy performance:
  - Some nodes did not do any work.
  - Performance of other nodes was very poor.
- Conclusion: Problems with the model setup; 2 or 3 nodes may not be appropriate for the problem.

## Root Cause
- Possible issues with the model setup.
- Inappropriate node allocation for the simulation.

## Solution
- Review and optimize the model setup.
- Consider adjusting the number of nodes allocated for the simulation.

## General Learnings
- Ensure proper model setup before running simulations.
- Monitor node performance to identify and address unhealthy job behavior.
- Adjust node allocation based on simulation requirements.

## References
- Job monitoring links provided by HPC Admin for further analysis.

## Next Steps
- User should review the model setup and node allocation.
- If issues persist, consult STAR-CCM+ specific support or documentation.
---

### 2024091742003951_Frage%20%C3%83%C2%BCber%20Fehlermeldung.md
# Ticket 2024091742003951

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject: Frage über Fehlermeldung

### Keywords:
- CFD-Simulation
- ANSYS LICENSE MANAGER ERROR
- cfd_base
- Licensing pool
- MAX specified in options file

### Problem:
- User encountered an error while running a CFD simulation on HPC.
- Error message: `ANSYS LICENSE MANAGER ERROR: Request name cfd_base does not exist in the licensing pool.`
- The simulation script worked previously but failed on the same day.

### Root Cause:
- The user's department attempted to access more licenses than were available in the licensing pool.
- Logs from the RRZE-Lizenzserver indicated multiple denied requests for `cfd_base` due to exceeding the MAX specified in the options file.

### Solution:
- The issue was resolved by the user, but the specific solution was not detailed in the conversation.

### General Learnings:
- License management errors can occur if the number of requested licenses exceeds the available pool.
- Checking the license server logs can provide insights into why license requests are being denied.
- Communication with the HPC support team is crucial for diagnosing and resolving licensing issues.

### Actions Taken:
- HPC Admin reviewed the license server logs and identified the root cause of the denied license requests.
- User resolved the issue independently, but the exact steps taken were not documented.

### Recommendations:
- Ensure that the number of requested licenses does not exceed the available pool.
- Monitor license usage and adjust the options file if necessary to prevent exceeding the MAX limit.
- Document the steps taken to resolve licensing issues for future reference.
```
---

### 42280944_Ansys%20HPC.md
# Ticket 42280944

 # HPC Support Ticket: Ansys HPC

## Keywords
- Ansys Mechanical
- HPC Account
- Licenses (aa_r_me, aa_r_hpc)
- RRZE Cluster
- Parallel Computing

## Problem
- User wants to use Ansys HPC to reduce computation time.
- User lacks experience with HPC and needs guidance on obtaining an HPC account and necessary licenses.

## Root Cause
- User requires an HPC account and additional HPC/Parallel licenses (aa_r_hpc) to utilize more than 4 cores for Ansys Mechanical jobs.
- The user's institution (LFG) had limited HPC licenses, restricting the number of cores that could be used simultaneously.

## Solution
- **Licenses**:
  - A base license (aa_r_me) is required for each job, allowing up to 4 cores.
  - Additional HPC/Parallel licenses (aa_r_hpc) are needed to use more than 4 cores.
- **HPC Account**:
  - To apply for an HPC account, use the application form found in the HPC section of the RRZE service desk: [RRZE Forms](http://www.rrze.uni-erlangen.de/hilfe/service-theke/formulare.shtml).
- **Cluster Usage**:
  - Ensure the institution has acquired sufficient licenses to make effective use of the RRZE clusters, which have 12 or more physical cores per node.

## General Information
- For Ansys Mechanical jobs on HPC clusters, users must bring their own licenses.
- The RRZE clusters are suitable for jobs requiring a significant number of cores, provided that enough licenses are available.

## Contacts
- **HPC Admins**: For further assistance with HPC accounts and licenses.
- **2nd Level Support Team**: For technical support and guidance on using HPC resources.
- **Gehard Wellein**: Head of the Datacenter.
- **Georg Hager**: Training and Support Group Leader.
- **Harald Lanig**: NHR Rechenzeit Support and Applications for Grants.
- **Jan Eitzinger and Gruber**: Software and Tools developers.

## Conclusion
Users need to ensure they have the necessary licenses and an HPC account to effectively utilize Ansys HPC on RRZE clusters. The support team can provide guidance and assistance throughout the process.
---

### 2022091542000158_Meggie_script.md
# Ticket 2022091542000158

 # HPC Support Ticket: Meggie_script

## Keywords
- Meggie
- Star-CCM+
- Script Error
- Version Compatibility

## Summary
The user encountered issues running a simulation on Meggie using a script adapted from the HPC documentation. The primary problems were syntax errors and incorrect variable names in the script. Additionally, the user inquired about the availability of a specific version of Star-CCM+.

## Root Cause
1. **Syntax Error in Script**: The user's script had an extra quote in the `echo` line, causing a syntax error.
2. **Incorrect Variable Names**: The script contained `SLRUM` instead of `SLURM` in multiple places, leading to errors with variable names used by Star-CCM+.

## Solution
1. **Correct Syntax**: Ensure the `echo` line matches the template from the HPC documentation exactly.
   ```bash
   echo "Available runtime: ${DAYS:-0}-${HH:-0}:${MM:-0}:${SS}, sleeping for up to $SLEEP, thus reserving $TIME4SAVE for clean stopping/saving results"
   ```
2. **Correct Variable Names**: Replace all instances of `SLRUM` with `SLURM` in the script.

## Version Compatibility
- The user requested Star-CCM+/2020.2 for compatibility with an existing simulation.
- The HPC Admin advised that older versions might not be supported but did not explicitly confirm the availability of Star-CCM+/2020.2.

## General Learnings
- **Accurate Script Copying**: Ensure scripts are copied accurately from the provided templates to avoid syntax errors.
- **Variable Consistency**: Double-check variable names for consistency and correctness.
- **Version Requests**: Clearly communicate the need for specific software versions and be prepared to use newer versions if older ones are not supported.

## Next Steps
- The user should correct the script and rerun the simulation.
- If the specific version of Star-CCM+ is not available, the user should consider using a newer version.

## References
- [HPC Documentation for Star-CCM+](https://hpc.fau.de/systems-services/documentation-instructions/special-applications-and-tips-tricks/star-ccm/#collapse_1)
---

### 2021081042002632_Fwd%3A%20%5BSCH%5D%20%28SUPPORT-141653%29%20metadynamics_license.md
# Ticket 2021081042002632

 # HPC Support Ticket: License Issue with Maestro Module

## Keywords
- License issue
- Maestro module
- Binding pose metadynamics
- License server connection
- Firewall
- Ports 27008 and 53000
- TCP communication
- HPC and CCC connectivity

## Problem Description
The user is attempting to run a module from Maestro (binding pose metadynamics) on the HPC but encounters an error indicating that no license is available for this module. The Schrödinger support confirms that the license is present on the machine `ccc129`, but there is no connection between `ccc129` and the HPC.

## Root Cause
- The HPC does not have access to the CCC machine `ccc129` due to a suspected firewall blocking access.
- The required ports (27008 and 53000) for TCP communication are not open.

## Solution
- The user should try connecting to the `ccc129` machine using its IP address instead of the name.
- The user needs to contact the IT department to open the required ports (27008 and 53000) for TCP communication.
- The HPC Admin suggests that the CCC team (specifically Mr. Hommes) should enable access to the HPC systems from `ccc129`.

## Additional Information
- The HPC Admin confirms that there are no restrictions on the HPC side.
- The user can use the Schrödinger support form to send files associated with the support ticket.
- The Schrödinger Knowledge Base can be used to find additional answers.

## Next Steps
- Contact the IT department to open the required ports.
- Ensure that the CCC team enables access to the HPC systems from `ccc129`.
- Verify connectivity using the IP address of the `ccc129` machine.

## References
- Schrödinger Support Center: [Support Form](https://www.schrodinger.com/supportcenter/?casekey=141653&casetitle=metadynamics_license#supportform)
- Schrödinger Knowledge Base: [Knowledge Base](http://www.schrodinger.com/kb/)
---

### 2022120542001259_Problem%20mit%20ANSYS%20Licensing%20auf%20Fritz%40NHR_FAU.md
# Ticket 2022120542001259

 ```markdown
# HPC Support Ticket Conversation Summary

## Issue
The user encountered a licensing error with ANSYS CFX on Fritz@NHR_FAU. The license was checked out from the LRZ license server but did not reach the CFX solver process on the compute node.

## Root Cause
The issue was due to the ANSYS license server's communication ports not being properly forwarded to the compute nodes. ANSYS has enhanced security measures that require additional configuration for proper license checkout.

## Solution
1. **Hosts File Configuration**:
   - Clone the `hosts` repository:
     ```bash
     git clone https://github.com/figiel/hosts.git
     cd hosts
     make
     ```
   - Add the LRZ license server to the hosts file:
     ```bash
     echo "131.188.3.115 licansys.lrz.de" > ~/.hosts
     ```
   - Preload the library:
     ```bash
     export LD_PRELOAD=~/hosts/libuserhosts.so
     ```
   - Run CFX commands normally.

2. **Fluent Configuration**:
   - Ensure Node-to-Node SSH connections are allowed on Ethernet ports.
   - Use OpenMPI for Fluent as Intel MPI has compatibility issues with newer kernel versions.
   - Disable the SSH check in the Fluent installation if it causes issues.

## Additional Information
- The HPC Admins confirmed that the login nodes perform NAT, which might affect port forwarding.
- The solution was tested and confirmed to work for CFX with single and multi-node setups.
- For Fluent, ensure the correct MPI derivative is used and SSH configurations are properly set.

## Conclusion
The licensing issue was resolved by configuring the hosts file and ensuring proper port forwarding. Additional configurations were made for Fluent to ensure compatibility and proper functioning on the HPC system.
```
---

### 2019040242000483_Error%20message%20Module%20Star-ccm%2B_13.06.012.md
# Ticket 2019040242000483

 # HPC Support Ticket: Error with Module Star-ccm+/13.06.012

## Keywords
- Module load error
- Star-ccm+
- map_mpi
- Directory structure issue

## Problem Description
- **User Issue:** The user encountered an error while trying to load the module `star-ccm+/13.06.012`.
- **Error Message:**
  ```
  Module ERROR: ERROR occurred in file /apps/modules/data/applications/star-ccm+/13.06.012:couldn't execute "/apps/STAR-CCM+/13.06.012/STAR-CCM+13.06.012/star/bin/map_mpi": no such file or directory
  ```
- **Root Cause:** The error indicates a missing file or directory in the specified path.

## Solution
- **Admin Response:** The HPC Admin identified a problem in the directory structure and fixed it.
- **Resolution:** The issue was resolved by correcting the directory structure.

## General Learnings
- **Module Load Errors:** Such errors often indicate issues with the module file or the underlying software installation.
- **Directory Structure:** Ensure that all necessary files and directories are correctly placed and accessible.
- **Communication:** Users should report such issues promptly to the HPC support team for quick resolution.

## Next Steps
- **Monitoring:** Continue to monitor for similar errors to ensure the fix is stable.
- **Documentation:** Update internal documentation to include this issue and its resolution for future reference.

---

This report can be used as a reference for support employees to troubleshoot similar module load errors in the future.
---

### 2020011542000891_Insatllation%20StarCCM%2B%2014.06.012-R8.md
# Ticket 2020011542000891

 ```markdown
# HPC-Support Ticket: Installation StarCCM+ 14.06.012-R8

## Keywords
- StarCCM+
- Version 14.06.012-R8
- Double Precision
- Simulation
- Zylinderinnenströmung
- Convergence
- Emmy Cluster

## Problem
- User requires installation of StarCCM+ version 14.06.012-R8 with double precision for higher computational accuracy in simulating cylinder inner flow.

## Root Cause
- Need for double precision version of StarCCM+ to achieve convergence in simulations.

## Solution
- HPC Admin informed the user that the required version of StarCCM+ (14.06.012 in double precision) is already available on the Emmy cluster as `star-ccm+/2019.3-r8`.

## General Learning
- Ensure that users are aware of the available software versions and modules on the HPC cluster.
- Double precision versions of software are crucial for certain simulations requiring higher accuracy.
- Communication with users about available resources can resolve many installation requests.
```
---

### 2024041742000481_Modul%20f%C3%83%C2%BCr%20die%20neueste%20Version%20von%20Star-ccm%2B.md
# Ticket 2024041742000481

 # HPC-Support Ticket Conversation Analysis

## Subject
Modul für die neueste Version von Star-ccm+

## Keywords
- Star-ccm+
- Version 2402
- Multiphysik
- Fluid-Struktur-Interaktionen
- Module
- Compiler
- Doppelpräzision
- Einzelpräzision
- Mixed-precision

## What Can Be Learned

### Problem
- User requires the latest version of Star-ccm+ (2402) for their Master's research.
- The current version available on the clusters is 2310.
- User needs a module that supports Doppelpräzision for compatibility with older files.

### Solution
- HPC Admins added the modules `star-ccm+/2402-clang` and `star-ccm+/2402-gnu` to the clusters Meggie and Woody.
- Both modules use mixed-precision and differ in the compiler (GNU Compiler and LLVM).
- HPC Admins later added `star-ccm+/2402-r8-clang` to support Doppelpräzision.

### General Learnings
- Users may require specific versions of software for their research.
- Different compilers (GNU, LLVM) can affect performance and compatibility.
- Precision (Doppelpräzision, Einzelpräzision, mixed-precision) is crucial for compatibility with certain files.
- HPC Admins can quickly add and configure new modules upon user request.

## Root Cause of the Problem
- The latest version of Star-ccm+ (2402) was not initially available on the clusters.
- The user required Doppelpräzision for compatibility with older files, which was not supported by the initially provided modules.

## Solution Found
- HPC Admins added the required modules (`star-ccm+/2402-clang`, `star-ccm+/2402-gnu`, `star-ccm+/2402-r8-clang`) to support the user's research needs.

## Documentation for Support Employees
- If a user requests a specific software version, ensure it is available on the clusters.
- Be aware of the precision requirements (Doppelpräzision, Einzelpräzision, mixed-precision) for software compatibility.
- Different compilers (GNU, LLVM) can be used to optimize performance.
- Quickly address user requests by adding and configuring new modules as needed.
---

### 2023012442003061_Hilfe%20f%C3%83%C2%BCr%20ansys%20Fluent.md
# Ticket 2023012442003061

 # HPC Support Ticket: Ansys Fluent Assistance

## Keywords
- Ansys Fluent
- Simulation
- Tutorials
- Mentor
- University Email
- Lehrstuhl für Strömungsmechanik
- Formula Student Team
- CFD Course

## Summary
A user requests assistance with Ansys Fluent for a project involving flow and deformation simulations. The user has already worked through tutorials but needs further guidance.

## Root Cause
- User requires mentorship and specific guidance on using Ansys Fluent for their project.

## Solution
- **Email Verification**: The user is advised to use their university email for proper ticket assignment.
- **Support Limitation**: The HPC group clarifies that they cannot provide general usage support for specific applications like Ansys Fluent.
- **Resources**: The user is directed to:
  - Ansys and CADFEM learning materials.
  - A CFD course for Ansys CFX at LRZ Garching.
  - The Lehrstuhl für Strömungsmechanik for potential Ansys expertise.
  - The Erlanger Formula Student Team "High-Octane Motorsports" for possible assistance.

## General Learnings
- **Email Policy**: Ensure users use their university email for support requests.
- **Support Scope**: Clarify the scope of support provided by the HPC group, especially for specialized software.
- **Resource Referral**: Direct users to relevant courses, departments, and teams that can offer specialized assistance.

## Follow-Up Actions
- Verify if the user has contacted the recommended resources.
- Update the ticket with any further assistance provided by external resources.

---

This report provides a concise summary and actionable steps for future reference in handling similar support requests.
---

### 2024111242002761_Star-ccm%2B%20nicht%20bei%20der%20Projektnummer%20b246dc%20verf%C3%83%C2%BCgbar.md
# Ticket 2024111242002761

 # HPC Support Ticket: Star-ccm+ Not Available for Project b246dc

## Keywords
- Star-ccm+
- Module Avail
- Project Number b246dc
- Fritz
- Tier 2 Project
- License Activation

## Problem Description
- User unable to see Star-ccm+ module when running `module avail star-ccm+`.
- User has access to Fritz but cannot load Star-ccm+.

## Root Cause
- The project number b246dc was not initially enabled for Star-ccm+ on Fritz.

## Solution
- HPC Admin enabled the project number b246dc for Star-ccm+ on Fritz.
- Additional steps were taken to ensure POD-Daten des LSTM were hinterlegt for b246dc.

## Steps Taken
1. **Initial Request**: User reported that Star-ccm+ was not available for their project.
2. **Admin Action**: HPC Admin enabled the project for Star-ccm+.
3. **Follow-up Issue**: User reported that Star-ccm+ could not be opened despite being available.
4. **Admin Action**: HPC Admin ensured that POD-Daten des LSTM were correctly set up for the project.

## Lessons Learned
- Ensure project numbers are correctly enabled for specific software modules.
- Verify that all necessary data and licenses are correctly configured for the project.
- Communicate clearly with users about the steps taken and any additional actions required.

## Notes
- The ticket involved multiple communications to resolve the issue fully.
- The solution required both enabling the project for the software and ensuring all necessary data was correctly set up.

## References
- `fadm1:/apps/set_acl.sh` for enabling the project.
- `fadm1:/apps/modules/modincludes/cdadapc/license-b246dc && ./set-group.sh b246dc` for setting up the necessary data.
---

### 2025010942000777_Key%20f%C3%83%C2%BCr%20Star-CCM%2B.md
# Ticket 2025010942000777

 # HPC-Support Ticket: Key für Star-CCM+

## Summary
- **Issue**: Expired key for Star-CCM+ preventing its use on the cluster.
- **Root Cause**: New key was available but not yet updated on the cluster.
- **Solution**: HPC Admins updated the key on the relevant clusters.

## Key Points
- **User Request**: Update the expired key for Star-CCM+.
- **HPC Admin Response**: Initially, no new keys were received. Later, the key was updated on Meggie and Fritz clusters.
- **Testing**: User encountered a module error initially, but after further updates, Star-CCM+ worked correctly.

## Detailed Steps
1. **User Report**:
   - Key for Star-CCM+ expired in January.
   - New key was supposedly sent to the HPC team.

2. **HPC Admin Actions**:
   - Initially, no new keys were received.
   - Key was later updated on Meggie and Fritz clusters.
   - User was asked to test the update.

3. **Testing and Resolution**:
   - User encountered a module error initially.
   - After further updates, Star-CCM+ worked correctly.

## Keywords
- Star-CCM+
- Key Update
- Module Error
- Cluster Update
- Testing

## Lessons Learned
- Ensure timely communication and update of keys.
- Test updates thoroughly to catch any errors early.
- Maintain clear documentation on key locations and update procedures.

## Conclusion
The issue was resolved by updating the key on the relevant clusters and testing the update. This process ensures that Star-CCM+ can be used without interruption.
---

### 2016062742001768_Ansys%2017.1%20auf%20Rechenclustern.md
# Ticket 2016062742001768

 # HPC-Support Ticket Conversation Analysis

## Subject: Ansys 17.1 auf Rechenclustern

### Keywords:
- Ansys 17.1
- Clusters LiMa and Emmy
- Installation request
- First-level support

### Root Cause of the Problem:
- User inquires about the possibility of installing Ansys 17.1 on the clusters LiMa and Emmy.

### Conversation Summary:
- **User**: Asks if it is possible to install Ansys 17.1 on the clusters LiMa and Emmy.
- **HPC Admin**: Forwards the request to the RRZE-eigenen first-level Ansys support.
- **HPC Admin**: Marks the ticket as resolved.

### Solution:
- The request was forwarded to the appropriate first-level support team for Ansys.

### General Learnings:
- Requests for specific software installations on HPC clusters should be directed to the relevant first-level support team.
- The HPC Admin's role includes forwarding such requests to the appropriate support channels.

### Documentation for Support Employees:
For future reference, if users request the installation of specific software versions (e.g., Ansys 17.1) on HPC clusters, forward the request to the designated first-level support team for that software. This ensures that the request is handled by the appropriate experts.
---

### 2022120742000971_Anfrage%20HPC%20Nutzung.md
# Ticket 2022120742000971

 ```markdown
# HPC Support Ticket: Anfrage HPC Nutzung

## Keywords
- HPC Nutzung
- Ansys Lumerical Mode
- GUI License
- Batch-Modus
- Grafikbibliotheken
- Lizenznutzung
- Rechenzeit

## Summary
A user from the Department of Electronic Components inquired about running simulations using Ansys Lumerical Mode on the HPC system. The simulations involve geometric descriptions of tapered fibers and frequency sweeps with approximately 400 points. The estimated total computation time is 200-300 hours over a year.

## Root Cause
The user's concern is whether the Ansys Lumerical Mode software, which requires a GUI license, can be run on the HPC system that operates in batch mode without graphical libraries on the compute nodes.

## Solution
- **HPC Admins** responded that the HPC systems operate in batch mode and typically do not support graphical interfaces on compute nodes.
- The software should be capable of running without interactive operation and GUI.
- The feasibility of running the software on the HPC system depends on the number of available licenses and whether the software can operate without a GUI.
- Users must provide their own licenses, and the number of simultaneously usable licenses determines the suitable cluster or node type.

## General Learnings
- HPC systems primarily operate in batch mode and may not support graphical interfaces.
- Software requiring GUI licenses may face challenges on HPC systems.
- License availability and compatibility with non-interactive operation are crucial factors for running software on HPC systems.
- Users must bring their own licenses, and the number of licenses affects the efficiency and feasibility of running simulations on the HPC system.
```
---

### 2021111542002153_Info%20zu%20HPC.md
# Ticket 2021111542002153

 # HPC-Support Ticket Conversation Summary

## Keywords
- HPC Access
- ANSYS Workbench
- License Management
- Parallel Computing
- Batch Processing
- Form Submission
- Ausweisprüfung

## General Learnings
- Students from TH Nürnberg can access FAU's HPC systems.
- ANSYS Workbench's GUI is not compatible with HPC batch processing.
- Licenses for ANSYS must be managed and accessible from HPC systems.
- Parallel computing is essential for efficient use of HPC resources.
- Forms for HPC access require verification from the home institution.

## Problem
- User needs access to FAU's HPC systems for rechenintensive simulations.
- User wants to use ANSYS Workbench on HPC systems.

## Solution
- User must submit two forms: "Antrag-IdMKennung-1.pdf" and "HPC-Antrag.pdf".
- The first form requires Ausweisprüfung confirmation from TH Nürnberg.
- ANSYS Workbench's GUI is not suitable for HPC batch processing. User should extract the calculations from Workbench.
- Licenses for ANSYS must be managed and accessible from HPC systems.
- User should ensure that their calculations can utilize parallel processing for efficient HPC usage.

## Root Cause
- User needs access to HPC resources for computationally intensive simulations.
- User's software (ANSYS Workbench) has compatibility issues with HPC batch processing.

## Additional Notes
- Videoidentifizierung can be offered as an alternative for Ausweisprüfung.
- User should coordinate with their institution's IT department to ensure license server accessibility.
- User should consult with their professor and IT department to resolve any software compatibility issues.
---

### 2023112742001459_ANSYS%20Fluent%20FEM%20Simulationen%20-%20LS%20Regelungstechnik.md
# Ticket 2023112742001459

 # HPC Support Ticket: ANSYS Fluent FEM Simulationen

## Keywords
- ANSYS Fluent
- FEM Simulationen
- HPC Research Lizenz
- Studentenlizenz
- Rechencluster
- Rechenpower

## Summary
A research assistant from the Chair of Control Engineering requires more computational power for ANSYS Fluent FEM simulations. The user inquired about the possibility of using a student license on the HPC cluster.

## Root Cause
- The user needs more computational resources for ANSYS Fluent FEM simulations.
- The user found information about an ANSYS HPC Research License but is concerned about the cost.
- The user is aware of a free student license and wants to know if it can be used on the HPC cluster.

## Solution
- **HPC Admin Response**: Only ANSYS Research Licenses can be used on the HPC clusters. The student license has limitations on simulation size, making it unsuitable for HPC use.
- **Referral**: For further questions about ANSYS licensing, the user is referred to the Software Department (software@fau.de).

## General Learnings
- ANSYS Research Licenses are required for HPC clusters.
- Student licenses are not suitable for HPC due to simulation size limitations.
- For licensing questions, users should contact the Software Department.

## Next Steps
- If the user needs more computational power, they should consider obtaining an ANSYS Research License.
- For detailed licensing information, contact the Software Department.

## Contact Information
- **Software Department**: software@fau.de
- **HPC Support**: support-hpc@fau.de

## References
- [ANSYS HPC Research License Information](https://www.rrze.fau.de/hard-software/software/dienstliche-nutzung/produkte/ansys/)
- [HPC Support Website](https://hpc.fau.de/)
---

### 2022052642000402_Star-CCM%2B%202022.1%20-r8%20auf%20Meggie%2BEmmy.md
# Ticket 2022052642000402

 ```markdown
# HPC Support Ticket: Star-CCM+ 2022.1 -r8 auf Meggie+Emmy

## Keywords
- Star-CCM+
- Double Precision (-r8)
- Meggie
- Emmy
- Software Installation
- Certificate Expiration

## Problem
- User requested the installation of the Double Precision (-r8) version of Star-CCM+ 2022.1 on Meggie and Emmy.

## Root Cause
- The initial delay in installation was due to a certificate expiration issue.

## Solution
- The HPC Admin team resolved the certificate issue and installed Star-CCM+ 2022.1-r8 on both Meggie and Emmy.

## Lessons Learned
- Certificate expiration can cause delays in software installation.
- Regular monitoring and renewal of certificates are essential for smooth operations.
- Effective communication between users and HPC Admins ensures timely resolution of issues.
```
---

### 2020120442002371_Problem%20mit%20Star%20CCm%2B%202020.3.md
# Ticket 2020120442002371

 # HPC Support Ticket: Problem with Star CCM+ 2020.3

## Keywords
- Star CCM+ 2020.3
- Open MPI
- Command line error
- Parameter format
- PBS script

## Problem Description
The user encountered an error while submitting a Star CCM+ 2020.3 simulation. The error message indicated a problem with the parameter format for the `np` option in Open MPI.

## Root Cause
The issue was caused by changes in the default MPI used between Star CCM+ versions 2020.2 and 2020.3. The parameters set in the user's PBS script were not compatible with the new MPI version.

## Solution
The HPC Admin suggested removing lines 62-80 from the `run_emmy.pbs` script, as these settings are no longer necessary in newer Star CCM+ versions. The user confirmed that this resolved the issue.

## General Learning
- Changes in software versions can introduce compatibility issues with existing scripts.
- It is important to check for updates in documentation or example scripts when upgrading software versions.
- Open MPI errors related to parameter formats can often be resolved by reviewing and updating command line options.

## References
- [Example PBS Script for Star CCM+](https://www.anleitungen.rrze.fau.de/hpc/special-applications-and-tips-tricks/star-ccm/#collapse_0)
---

### 2021020742000035_Probleme%20Star-ccm%2B%202020.3.md
# Ticket 2021020742000035

 ```markdown
# HPC Support Ticket: Problem with Star-CCM+ 2020.3

## Keywords
- Star-CCM+
- MPI
- Jobfile
- Simulation
- Cluster
- Fehlermeldung
- Parameter

## Problem Description
- User is experiencing issues with starting simulations using Star-CCM+ 2020.3.
- The job file and error output were attached but not understood by the user.

## Root Cause
- The standard MPI used in the current Star-CCM+ version has changed.
- Parameters set in the user's script (lines 62-80 in JobFile.pby) are causing issues with the new MPI.

## Solution
- Remove lines 62-80 from the JobFile.pby script as these settings are not necessary in newer Star-CCM+ versions.
- Refer to the updated example script available at: [Star-CCM+ Documentation](https://hpc.fau.de/systems-services/systems-documentation-instructions/special-applications-and-tips-tricks/star-ccm/)

## General Learning
- Always check for updates in software documentation and example scripts when encountering issues after a version upgrade.
- Parameters that were necessary in older versions may not be required in newer versions and could cause compatibility issues.
```
---

### 2022070742003487_Probleme%20mit%20HPC%20Account%20_Star-CCM%20Installation.md
# Ticket 2022070742003487

 # HPC Support Ticket Analysis

## Subject
Probleme mit HPC Account / Star-CCM Installation

## Keywords
- HPC Account
- Job Submission Error
- Account Expiration
- Software Installation
- Directory Creation

## Root Cause of the Problem
- User's HPC account had expired.
- User requested a specific version of Star-CCM+.
- User reported missing home directory.

## Solution
- **Account Expiration**: The account was renewed by the service desk. It may take some time for the account to be recognized by all services.
- **Software Installation**: No older versions of Star-CCM+ will be installed on Emmy. Meggie already has newer versions available (2021.3.1-r8 and 2022.1-r8).
- **Directory Creation**: No explicit solution provided for the missing home directory.

## General Learnings
- Ensure that user accounts are up-to-date to avoid job submission errors.
- Check for available software versions before requesting installations.
- Account renewals may take time to propagate across all services.

## Next Steps
- Verify that the user's account is now functional.
- Confirm the availability of the requested software versions.
- Address any remaining issues with the home directory.

## Additional Notes
- The ticket was initially deferred due to account issues.
- The ticket was later resolved by renewing the account.

---

This report provides a concise summary of the issue, the root cause, the solution, and general learnings for future reference.
---

### 2020091142000561_Star%20CCM%2B.md
# Ticket 2020091142000561

 # HPC-Support Ticket: Star CCM+

## Keywords
- Star CCM+
- Simulation
- Bachelorarbeit
- Hochtemperatur-Beschichtungen
- Fraunhofer IISB
- Lehrstuhl WW1
- Gemeinschaftsvertrag
- Siemens PLM
- Remotedesktopverbindung

## Summary
A user requested information on using Star CCM+ for a simulation related to their bachelor's thesis on high-temperature coatings. The user had prior experience with the software through a remote desktop connection during a previous internship.

## Problem
- The user needed to know the possibilities for temporary private use of Star CCM+ and the requirements for such use.
- The user's thesis is supervised by Fraunhofer IISB and Lehrstuhl WW1.

## Solution
- Private use of Star CCM+ is not covered by the current joint contract of the chairs.
- Siemens PLM offers a limited version for students directly.
- The joint license for Star CCM+ is held by the chairs of Strömungsmechanik, Prozessmaschinen und Anlagentechnik (Prof. Becker), Technische Thermodynamik, and Energieverfahrenstechnik.
- The user was advised to consider using the software at the chairs, possibly via a remote desktop connection.

## General Learnings
- Star CCM+ is not available for private use under the current joint contract.
- Students can access a limited version directly from Siemens PLM.
- The joint license is shared among specific chairs at the university.
- Remote desktop connections can be a viable solution for accessing the software.

## Root Cause
- The user needed access to Star CCM+ for their thesis but was unaware of the licensing restrictions and available options.

## Resolution
- The HPC Admin provided information on the licensing agreement and suggested alternative access methods, such as using the software at the chairs via a remote desktop connection.

## Next Steps
- The user should contact the relevant chairs to arrange access to Star CCM+, possibly through a remote desktop connection.
- The user can also explore the limited version of Star CCM+ offered directly by Siemens PLM.
---

### 2020052842002875_A%20problem%20with%20ANSYS%20Fluent%20license.md
# Ticket 2020052842002875

 # HPC Support Ticket: ANSYS Fluent License Issue

## Keywords
- ANSYS Fluent
- License Error
- Batch Run
- License Manager
- Academic License
- License Server

## Problem Description
- User encountered license-related errors when attempting to batch run ANSYS Fluent on HPC.
- Different ANSYS versions produced various errors:
  - Version 2020R1: License manager needs update.
  - Versions 2019R1 and 19.1: License identified as Academic with limitations.
  - Versions 18.1 and 17.2: No errors but no results.

## Root Cause
- The HPC center operates its own license pool and server, separate from the campus contract for ANSYS.
- Potential issues with the user's group license manager or license type recognition.

## Solution
- HPC Admins clarified that they do not have access to license logs and cannot directly assist with license issues.
- User needs to address the license manager update and ensure the correct license type is recognized.

## Notes
- User provided "out" files and screenshots of ANSYS license preferences for reference.
- HPC Admins suggested that the issue is related to the user's group license manager and not the HPC center's license server.

## Next Steps
- User should contact their group's IT support or ANSYS support to resolve the license manager and type recognition issues.
- If the problem persists, user can provide additional information to HPC Admins for further investigation.

## References
- HPC Services, Friedrich-Alexander-Universitaet Erlangen-Nuernberg
- Regionales RechenZentrum Erlangen (RRZE)
- ANSYS Fluent Documentation and Support
---

### 2024072342003121_Software%20Update%20STAR-CCM%2B%202406-r8.md
# Ticket 2024072342003121

 ```markdown
# HPC-Support Ticket: Software Update STAR-CCM+ 2406-r8

## Keywords
- Software Update
- STAR-CCM+
- CFD Simulations
- Cluster Update
- Module Availability

## Problem
- **Root Cause:** The latest version of STAR-CCM+ (2406-r8) was not available on the cluster, causing issues for CFD simulations.

## Solution
- **Action Taken:** HPC Admins updated the STAR-CCM+ module to the latest version (2406-r8) on most HPC systems.
- **Modules Updated:** `star-ccm+/2406-clang` and `star-ccm+/2406-r8-clang`

## General Learnings
- Users may request software updates for specific modules to match their local software versions.
- HPC Admins handle software updates and ensure module availability across HPC systems.
- Communication with users and timely updates are crucial for maintaining smooth operations.

## Follow-Up
- Ensure that updated modules are tested and available on all relevant clusters.
- Inform users about the availability of updated modules through appropriate channels.
```
---

### 2022080842004544_Update%20Lizenzserver%20Star-CCM%2B.md
# Ticket 2022080842004544

 # HPC Support Ticket: Update Lizenzserver Star-CCM+

## Keywords
- Star-CCM+
- Lizenzserver
- FLEXlm
- Version Update
- Error Messages

## Problem Description
The user encountered an error when trying to retrieve Star-CCM+ licenses from the license server `27000@hpclicense1.rrze.uni-erlangen.de`. The error messages indicated that the FLEXlm daemon version (11.14) was older than the required version (11.18) for the newer Star-CCM+ versions.

## Error Messages
```
ERROR: FLEXlm daemon is older than program.
ERROR: daemon is at 11.14
ERROR: program is at 11.18
ERROR: FLEXlm version problem found. Please download FLEXlm server 11.18.0.0
```

## Root Cause
The installed FLEXlm daemon version (11.14) was incompatible with the newer Star-CCM+ versions, which required FLEXlm version 11.18.

## Solution
The HPC Admin updated the license server to the latest FLEXlm version (11.18.0.0) to restore full functionality.

## Lessons Learned
- Ensure that the FLEXlm daemon version on the license server is compatible with the software versions in use.
- Regularly update the FLEXlm server to avoid version mismatch issues.
- Communicate with the correct support team to address issues promptly.

## Actions Taken
- The user initially sent the request to the wrong email address but later corrected it.
- The HPC Admin updated the license server to the required FLEXlm version.

## Follow-Up
- Verify that the updated license server is functioning correctly with the newer Star-CCM+ versions.
- Monitor for any further compatibility issues and update the FLEXlm server as needed.
---

### 2023101142003998_AW%3A%20Frage%20nach%20ANSYS%20HPC-Lizenzen%20-%20iwep.md
# Ticket 2023101142003998

 # HPC-Support Ticket Conversation Analysis

## Keywords
- ANSYS HPC-Lizenzen
- FAU-OrgNr
- HPC-Konto
- NHR in Erlangen
- Simulationsdauer
- Lizenzserver
- Ansys Multiphysics Research
- Ansys HPC Research Staffel
- Woody
- Meggie
- Linux
- Windows
- RRZE
- Kostenstelle
- Lizenzbestellung
- HPC-Systeme
- HPC-Cafe
- Dokumentation

## General Learnings
- **Licensing Issues**: Understanding how to activate and utilize ANSYS HPC licenses.
- **HPC Account Setup**: Steps to create and manage an HPC account.
- **Resource Allocation**: How to request and utilize HPC resources effectively.
- **Performance Optimization**: Strategies to reduce simulation time on HPC systems.
- **Documentation and Support**: Importance of referring to documentation and attending support sessions like HPC-Cafe.

## Root Causes and Solutions

### Licensing Issues
- **Root Cause**: User had issues with activating the second license for ANSYS HPC Research Staffel.
- **Solution**: Clarified that ANSYS products automatically request the necessary number of "anshpc" tokens when more than 4 cores are used per simulation. The user was informed that they have 1x Ansys Multiphysics Research and 11x Ansys HPC licenses, allowing simulations on up to 15 cores.

### HPC Account Setup
- **Root Cause**: User did not have an HPC account and needed to apply for one.
- **Solution**: Provided instructions to apply for an HPC account and informed that the FAU-OrgNr is the same as the Kostenstelle of the chair. The RRZE service desk will complete the number.

### Performance Optimization
- **Root Cause**: User's simulation was taking a long time to run.
- **Solution**: Suggested using more cores (up to 32) on Woody or Meggie to potentially reduce simulation time. Informed that the HPC systems use processors that are not faster than those in a typical PC but have more cores.

### Resource Allocation
- **Root Cause**: User needed to book additional ANSYS HPC licenses.
- **Solution**: Instructed the user to contact their software contact persons to order additional licenses through the customer portal.

### Documentation and Support
- **Root Cause**: User needed guidance on using ANSYS on HPC systems.
- **Solution**: Referred the user to the HPC-Cafe and documentation for new HPC users. Provided specific links for ANSYS CFX/Fluent on the HPC systems.

## Conclusion
This conversation highlights the importance of understanding licensing, account setup, resource allocation, and performance optimization for HPC users. It also emphasizes the value of documentation and support sessions in resolving user issues effectively.
---

### 2018020942000565_HPC%20%7C%20Comsol%20Multiphysics%205.3a.md
# Ticket 2018020942000565

 ```markdown
# HPC Support Ticket: Comsol Multiphysics 5.3a

## Keywords
- Comsol Multiphysics
- Version Update
- HPC Cluster
- Connection Issue
- Host Parsing Error

## Summary
The user requested an update to the latest version of Comsol Multiphysics on the HPC cluster. After the update, the user encountered a connection issue with the Comsol server.

## Problem
- **Root Cause:** The user was unable to connect to the Comsol server using the new version (5.3a). The error message indicated a failure to parse the host.
- **Details:** The user attempted to connect using the format `iwmk000h@woody3.rrze.uni-erlangen.de`, which was previously valid but caused an error in the new version.

## Solution
- **Resolution:** The HPC Admin suggested separating the username and host. The user successfully connected by entering only the hostname (`woody3.rrze.uni-erlangen.de`) in the host field.

## Lessons Learned
- **Version Updates:** Regular updates to software versions can introduce new issues that were not present in previous versions.
- **Host Configuration:** Ensure that the host configuration is compatible with the updated software version. Separate fields for username and host may be required.
- **User Communication:** Clear communication between the user and the support team is essential for troubleshooting and resolving issues efficiently.

## Actions Taken
- The HPC Admin updated Comsol Multiphysics to version 5.3a-up1.
- The user reported a connection issue with the new version.
- The HPC Admin provided a solution by suggesting a change in the host configuration.
- The user confirmed that the solution resolved the issue.

## Conclusion
The issue was resolved by adjusting the host configuration to match the requirements of the updated software version. This highlights the importance of understanding and adapting to changes introduced by software updates.
```
---

### 2024021642001904_StarkStrom%20Augsburg%20StarCCM%2B.md
# Ticket 2024021642001904

 # HPC Support Ticket: StarCCM+ on HPC Cluster

## Keywords
- StarCCM+
- HPC Cluster
- Simulation
- Warteschlange
- Grafische Oberfläche
- POD-Key
- Upload/Download
- SLURM
- Jobskript

## Summary
User encountered issues with running StarCCM+ simulations on the HPC cluster, specifically with accessing the simulation from a local GUI and managing the job queue.

## Issues and Solutions

### 1. Accessing Simulation from Local GUI
- **Issue**: User wanted to access StarCCM+ simulation on the cluster from a local GUI.
- **Solution**: HPC Admins clarified that direct access to simulations from a local GUI is not possible due to the cluster's Warteschlangensystem and private IP addresses of compute nodes.

### 2. Simulation Job Queue
- **Issue**: Simulation jobs were closing automatically due to the job queue.
- **Solution**: HPC Admins explained that simulations must be run through the job queue and cannot be kept open indefinitely.

### 3. POD-Key for StarCCM+
- **Issue**: User needed a POD-Key for StarCCM+ simulations.
- **Solution**: HPC Admins advised that the POD-Key can be manually added to the job script.

### 4. Slow Upload/Download Speeds
- **Issue**: User experienced slow upload/download speeds for simulation files.
- **Solution**: HPC Admins confirmed that the upload speed matched the user's bandwidth and suggested there was no immediate solution to speed up the process.

### 5. Simulation Aborts at 40 Seconds
- **Issue**: Simulation aborted after 40 seconds when using multiple nodes.
- **Solution**: HPC Admins identified a missing line in the job script (`unset SLURM_EXPORT_ENV`) and advised to remove the `-licpath` option.

### 6. Multi-Node Simulation Error
- **Issue**: Simulation encountered errors when using more than one node.
- **Solution**: HPC Admins identified a missing line in the job script (`unset SLURM_EXPORT_ENV`) and advised to remove the `-licpath` option.

## General Learnings
- StarCCM+ simulations on the HPC cluster must be managed through the job queue and cannot be accessed directly from a local GUI.
- POD-Keys for StarCCM+ can be manually added to the job script.
- Slow upload/download speeds are often a result of the user's bandwidth and may not have an immediate solution.
- Ensure job scripts are correctly configured, including necessary environment variables and license paths.

## References
- [StarCCM+ Documentation](https://doc.nhr.fau.de/apps/star-ccm%2B/)
- [Speedtest](https://www.speedtest.net/)

## Next Steps
- Users should ensure their job scripts are correctly configured and include all necessary environment variables.
- For persistent issues, users can contact HPC Support for further assistance.
---

### 2019090242002436_HPC%20%7C%20Comsol%20Multiphysics%205.4.md
# Ticket 2019090242002436

 # HPC Support Ticket: Comsol Multiphysics Update

## Keywords
- Comsol Multiphysics
- HPC Update
- Module Availability
- Version 5.4
- Version 5.5

## Summary
A user requested updates for Comsol Multiphysics on the HPC system (Woody). The HPC Admin provided information about the availability of the requested versions.

## Problem
- User requested an update to Comsol Multiphysics version 5.4.
- Later, the user requested an update to version 5.5.

## Solution
- HPC Admin informed the user that the module "comsol/5.4-up4" was available.
- HPC Admin later informed the user that the module "comsol/5.5-up3" was already available since June.

## Lessons Learned
- Users should check the availability of software modules before requesting updates.
- HPC Admins should regularly update users about the availability of new software versions.
- Effective communication between users and HPC Admins is crucial for efficient use of HPC resources.

## Root Cause
- User was unaware of the availability of the requested software versions.

## Resolution
- HPC Admin provided the necessary information about the available software modules.
- User acknowledged the information and thanked the HPC Admin.

## Notes
- Ensure that users are informed about the availability of new software versions through regular updates or a centralized information system.
- Encourage users to check the software module list before submitting update requests.
---

### 2024112042003208_New%20StarCCM%2B%20installation.md
# Ticket 2024112042003208

 ```markdown
# HPC Support Ticket: New StarCCM+ Installation

## Keywords
- StarCCM+
- Installation
- HPC Machines
- Version 2410 (19.06.008)
- Meggie
- Fritz

## Summary
A user requested the installation of StarCCM+ version 2410 (19.06.008) on the HPC machines.

## Problem
- **Root Cause:** User needed a specific version of StarCCM+ installed on the HPC machines.

## Solution
- **Action Taken:** HPC Admins installed StarCCM+ version 2410-clang on Meggie and Fritz.
- **Outcome:** The installation was successful, and the user confirmed receipt of the installation.

## General Learnings
- Users may require specific software versions for their research.
- HPC Admins can efficiently install requested software versions on the HPC machines.
- Clear communication between users and HPC Admins ensures that software requests are handled promptly.
```
---

### 2022041242003535_Starccm%20Script.md
# Ticket 2022041242003535

 # HPC Support Ticket: StarCCM+ Script Issue

## Keywords
- StarCCM+
- MPI changes
- Script update
- OpenMPI
- Platform MPI
- `-cpu_bind` option

## Problem Description
- User encountered issues with StarCCM+ versions above 2020.2.
- Suspected MPI changes or need for a new script.

## Root Cause
- StarCCM+ switched its default MPI from Platform MPI to OpenMPI in recent versions.
- The option `-cpu_bind=v,map_cpu:...` is not recognized anymore.

## Solution
- Update the script to use the new MPI settings.
- Refer to the updated example scripts available at [HPC Documentation](https://hpc.fau.de/systems-services/systems-documentation-instructions/special-applications-and-tips-tricks/star-ccm/#collapse_0).
- The call to StarCCM+ should be updated to:
  ```bash
  starccm+ -batch -rsh ssh -cpubind v -np ${CORES} -machinefile pbs_nodefile.${PBS_JOBID} -power -podkey $PODKEY ${CCMARGS}
  ```

## General Learnings
- Always check for software updates and changes in default settings.
- Refer to the latest documentation and example scripts provided by the HPC service.
- MPI changes can affect script compatibility, requiring updates to options and parameters.
---

### 2018100842000677_Problem%20with%20running%20StarCCM%2B%20in%20HPC%20systems.md
# Ticket 2018100842000677

 # HPC Support Ticket: Problem with Running StarCCM+ in HPC Systems

## Keywords
- StarCCM+
- License Issue
- POD Key
- Module Loading
- Environment Variable

## Problem Description
The user encountered issues running StarCCM+ simulations on the HPC systems. The error message indicated that the requested license was not available. The user observed that the license file being checked was from the HPC system's server (`1999@grid.rrze.uni-erlangen.de`) instead of CD-adapco.

## Root Cause
- The POD key used by the user was not the same as the one defined by the module on the HPC system.
- The module was loaded after setting the environment variable `$PODKEY`, causing the license check to fail.

## Solution
1. Load the appropriate StarCCM+ module before setting the environment variable `$PODKEY`.
2. Use the module-defined environment variable `$PODKEY` instead of manually setting it.

## Additional Notes
- The user reported that the module `starccm+/13.02.013-r8` did not work, which could potentially cause issues in the future.
- The HPC admin mentioned that there was a path error in `starccm+/13.02.013-r8`, which has been fixed.

## Lessons Learned
- Always ensure that the correct POD key is used when running StarCCM+ simulations on HPC systems.
- Load the appropriate module before setting any environment variables to avoid license check failures.
- If a specific module version is not working, it may be due to a path error or other issues that need to be addressed by the HPC admin.
---

### 2022111542002393_Name%20%26%20IP%20Lokaler%20Server%20R%C3%83%C2%B6sler.md
# Ticket 2022111542002393

 ```markdown
# HPC-Support Ticket: Name & IP Lokaler Server Rösler

## Keywords
- STAR CCM+
- Lizenzserver
- Portforwarding
- POD-Kontingent
- FlexLM
- IP-Adresse
- HPC-Account

## Problem
- User provided incorrect information about the license server.
- User initially stated that the license was obtained from `1999@flex.cd-adapco.com`, but later corrected it to a local license server `1999@PC1470`.

## Root Cause
- Miscommunication about the license server details.
- Need for port forwarding to access the local license server.

## Solution
- HPC Admin suggested checking with the professor for a POD-Kontingent from Siemens or HSC to avoid the complexity of port forwarding.
- If POD-Kontingent is not available, port forwarding will be required.
- Port forwarding will be handled through `hpc-mover.rrze.uni-erlangen.de` (131.188.3.116) if ports 1999 and 2099 are used.
- User needs to provide details about the grid size, number of cores/nodes, and simultaneous jobs to determine the license requirements.

## Additional Information
- HPC systems at FAU operate in private IP address ranges without NAT.
- Access to external license servers requires explicit port forwarding on a gateway computer.
- STAR-CCM+ uses FlexLM as the license server, requiring two TCP ports to be forwarded.
- Username in license server logs will start with "corz" followed by three digits and end with "h".
- Hostnames are not necessary as all requests and responses go through the gateway computer.

## Next Steps
- User will contact the professor to inquire about a POD-Kontingent.
- If POD-Kontingent is not available, further steps for port forwarding will be discussed.
- User will provide additional details about job requirements for license planning.
```
---

### 2022012742002497_Star-CCM%2B%20Versionsupdate%20m%C3%83%C2%B6glich%3F.md
# Ticket 2022012742002497

 # HPC Support Ticket: Star-CCM+ Version Update Request

## Keywords
- Star-CCM+
- Version Update
- Meggie Cluster
- Simulation
- Projektarbeit
- 2021.3
- 2021.1

## Summary
A user requested an update of the Star-CCM+ software on the Meggie cluster from version 2021.1 to 2021.3 to run simulations created in the newer version for their project work.

## Root Cause
- The user needed a newer version of Star-CCM+ (2021.3) to run their simulations, which were created in that version.
- The current version available on the Meggie cluster was 2021.1.

## Solution
- The HPC Admin team installed the requested version (2021.3.1) of Star-CCM+ on the Meggie cluster.

## What Can Be Learned
- Users may require specific software versions for their projects.
- Software update requests should be handled promptly to support users' project needs.
- Communication between the user and the HPC Admin team is essential for resolving such requests.

## Actions Taken
1. The user submitted a request for a software version update.
2. The HPC Admin team acknowledged the request and proceeded with the installation.
3. The HPC Admin team notified the user once the new version was available.

## Follow-Up
- Ensure that the user is aware of the new software version availability.
- Monitor for any further software update requests and handle them accordingly.
---

### 2018052542000378_Zugang%20Meggie%20-%20iwpa78.md
# Ticket 2018052542000378

 ```markdown
# HPC Support Ticket: Access to Meggie - iwpa78

## Keywords
- Meggie access
- Ansys installation issue
- STAR-CCM+ licensing issue
- IPv6 configuration
- Unsupported OS version

## Summary
- **User**: Requested access to Meggie and provided a project description.
- **HPC Admin**: Granted temporary access to Meggie.
- **Issues**:
  - Ansys installation hangs at 89%.
  - STAR-CCM+ may have licensing issues due to IPv6 configuration.
- **Actions**:
  - User will test STAR-CCM+ and Ansys on Meggie.
  - HPC Admin provided an unsupported version of Ansys (19.1) for testing.

## Detailed Conversation
- **User**: Submitted a project description for Meggie access and contacted another user regarding stored files.
- **HPC Admin**:
  - Granted temporary access to Meggie.
  - Reported Ansys installation issue (hangs at 89%).
  - Mentioned potential licensing issues with STAR-CCM+ due to IPv6 configuration.
  - Provided an unsupported version of Ansys (19.1) for testing.
- **User**: Acknowledged the information and will test the software in a few weeks.

## Root Cause and Solution
- **Ansys Installation Issue**:
  - **Root Cause**: Unknown, possibly related to unsupported OS version.
  - **Solution**: None found; Ansys support case opened but chances of resolution are low.
- **STAR-CCM+ Licensing Issue**:
  - **Root Cause**: Known interactions with IPv6 addresses configured on Meggie.
  - **Solution**: User will test and report back.

## Next Steps
- User will test STAR-CCM+ and Ansys on Meggie and report back to HPC Admin.
```
---

### 2020090142002131_Aktualisierung%20STAR-CCM%2B.md
# Ticket 2020090142002131

 ```markdown
# HPC Support Ticket: Update STAR-CCM+

## Keywords
- STAR-CCM+
- Update
- Version 15.04
- HPC Servers
- Formula Student
- Aerodynamics Simulation

## Problem
- User requested an update for STAR-CCM+ to the latest version 15.04 for aerodynamics simulations on HPC servers.

## Solution
- HPC Admin updated the software.
- The new module is named `star-ccm+/2020.2`.

## Notes
- The update was completed successfully.
- The user was informed about the new module name.

## General Learnings
- Regular updates of software versions are essential for maintaining compatibility and performance.
- Communication with users regarding updates and module names is crucial for smooth operations.
```
---

### 2018092142001644_Instructions_Guidelines%20to%20use%20Star%20CCM%2B%20in%20HPC%20systems.md
# Ticket 2018092142001644

 ```markdown
# HPC Support Ticket: Instructions/Guidelines to Use Star CCM+ in HPC Systems

## Keywords
- Star CCM+
- HPC systems
- Batch process
- License activation
- Sample script

## Problem
- User recently obtained access to use Star CCM+ in HPC systems but has no clue how to run batch processes for Star CCM+ simulations.
- User is unsure if they are entitled to use Star CCM+ from a specific date mentioned in their HPC login access extension.

## Root Cause
- Lack of knowledge on how to run batch processes for Star CCM+.
- Misunderstanding about the entitlement date for Star CCM+ usage.

## Solution
- **License Activation**: The license for Star CCM+ should be activated, and the Star CCM+ modules should be visible on the HPC system (Emmy) for the user.
- **Sample Script**: A sample script for running a Star CCM+ batch job on Emmy was provided to the user.
- **Entitlement Date**: The user should now have access to the Star CCM+ installation on Emmy. The date mentioned in the HPC login access extension does not automatically grant access to Star CCM+; additional steps are required.

## General Learning
- Users should be directed to colleagues who already use Star CCM+ for further assistance.
- Writing "additional Star CCM+" on the account extension form is not sufficient to gain access; specific requests and approvals are needed.
- HPC Admins can provide sample scripts and basic guidance but may not have in-depth knowledge of specific software like Star CCM+.

## Next Steps
- User should review the provided sample script and consult with colleagues who have experience with Star CCM+.
- If further issues arise, the user should contact HPC support for additional assistance.
```
---

### 2020070942003638_CAT%20Racing%20STAR%20CCM%2B2020.2.md
# Ticket 2020070942003638

 # HPC Support Ticket: CAT Racing STAR CCM+2020.2

## Keywords
- STAR CCM+
- Version 2020.2
- Installation
- Module
- Emmy

## Summary
A user requested the installation of STAR CCM+ version 2020.2 on the HPC system "emmy."

## Root Cause
The user was unaware that the new version of STAR CCM+ had already been installed as a module.

## Solution
The HPC Admin informed the user that the STAR CCM+/2020.2 module was already available.

## Lessons Learned
- **Communication**: Ensure users are aware of the latest software updates and installations.
- **Documentation**: Maintain up-to-date documentation on available software modules.
- **User Awareness**: Regularly inform users about new software installations and updates.

## Follow-Up Actions
- Update the user documentation to reflect the availability of the STAR CCM+/2020.2 module.
- Consider sending periodic updates to users about new software installations.
---

### 2022091842000821_Folgen%20OS%20Update%20Meggie%3F%20--%3E%20ssh%20Settings.md
# Ticket 2022091842000821

 # HPC Support Ticket: Folgen OS Update Meggie? --> ssh Settings

## Keywords
- OS Update
- SSH Configuration
- Star-CCM+
- Design Manager
- Permission Denied
- Podkey
- Passwordless SSH
- Slurm
- Batch Script

## Problem Description
- User encountered permission denied errors when running optimizations with Star-CCM+ in Pre-Allocation mode after an OS update on Meggie.
- The error messages indicated issues with SSH configuration, specifically with accessing reserved nodes.
- The problem was isolated to the use of the Design Manager within Star-CCM+.

## Root Cause
- The OS update disabled passwordless SSH between nodes, which is required by the Design Manager for distributing parallel computations.
- Incorrect Podkey configuration was also identified, leading to license acquisition failures.

## Solution
- HPC Admins re-enabled passwordless SSH between nodes to resolve the SSH-related permission issues.
- The batch script was updated to remove the unnecessary `-machinefile` option, as Star-CCM+ now automatically receives the list of node names from Slurm.
- The correct Podkey was restored during the module load process to fix license acquisition issues.

## Lessons Learned
- OS updates can inadvertently change SSH configurations, affecting applications that rely on passwordless SSH.
- It is important to verify and update batch scripts to ensure compatibility with new system configurations.
- Proper Podkey configuration is crucial for license management in commercial software.

## Additional Notes
- The user provided a test case and batch script, which were instrumental in diagnosing and resolving the issue.
- The HPC Admins provided timely support and implemented the necessary changes to restore functionality.

## Conclusion
- The issue was successfully resolved by re-enabling passwordless SSH and correcting the Podkey configuration.
- Users should be aware of potential impacts on SSH configurations and license management following OS updates.
---

### 2025010142000488_POD%20Key%20STAR%20CCM%20Jahr%202025.md
# Ticket 2025010142000488

 # HPC-Support Ticket Conversation: POD Key STAR CCM Jahr 2025

## Problem Description
- **Issue**: POD keys for STAR CCM expired on 31.12.2024.
- **Affected**: Local and cluster keys.
- **Impact**: Unable to run simulations.

## Root Cause
- **Expiry Date**: The POD keys were set to expire on 31.12.2024.
- **Lack of Automatic Renewal**: The keys were not automatically renewed on the cluster.

## Solution
- **New Keys Provided**: New POD keys were generated and made available on the LSD-Server for RRZE-Kontaktpersonen.
- **Manual Update**: Users were instructed to update their POD keys manually.
- **Variable Update**: The `$PODKEY` variable was updated with the new keys to ensure smooth operation on the cluster.

## Key Points Learned
- **Expiry Awareness**: Be aware of the expiry dates of POD keys and plan for renewals.
- **Communication**: Ensure clear communication with users about the expiry and renewal process.
- **Manual Intervention**: Sometimes manual intervention is required to update keys and variables.
- **Support Channels**: Utilize the RRZE-Veranstaltungskalender for meeting IDs and schedules.

## Actions Taken
- **Key Generation**: New keys were generated and distributed.
- **User Instruction**: Users were instructed on how to update their keys and variables.
- **Support Follow-up**: The support team followed up to ensure the issue was resolved.

## Conclusion
- **Resolution**: The issue was resolved by generating new POD keys and updating the necessary variables.
- **Future Prevention**: Plan for key renewals well in advance to avoid disruptions.

## References
- **RRZE Software Support**: [RRZE Software](http://www.software.rrze.fau.de)
- **FAQ**: [FAQ for Employees, Contact Persons, and Students](https://www.rrze.fau.de/hard-software/software/faq/)
- **RRZE-Veranstaltungskalender**: [RRZE-Veranstaltungskalender](https://www.rrze.fau.de/infocenter/aktuelles/veranstaltungskalender/)

## Keywords
- POD keys
- STAR CCM
- Expiry date
- Key renewal
- Cluster keys
- LSD-Server
- RRZE-Kontaktpersonen
- Variable update
- Manual intervention
- Support communication
- RRZE-Veranstaltungskalender

## Additional Notes
- **HPC Admins**: Thomas, Michael Meier, Anna Kahler, Katrin Nusser, Johannes Veh
- **2nd Level Support Team**: Lacey, Dane (fo36fizy), Kuckuk, Sebastian (sisekuck), Lange, Florian (ow86apyf), Ernst, Dominik (te42kyfo), Mayr, Martin
- **Head of Datacenter**: Gerhard Wellein
- **Training and Support Group Leader**: Georg Hager
- **NHR Rechenzeit Support**: Harald Lanig
- **Software and Tools Developer**: Jan Eitzinger, Gruber
---

### 2021033042002391_High-Octane%20Motorsports.md
# Ticket 2021033042002391

 ```markdown
# HPC-Support Ticket Conversation: High-Octane Motorsports

## Keywords
- Star-ccm+
- Version Update
- Cluster
- Module

## Summary
A user requested an update to the latest version of Star-ccm+ (2021.1) on the cluster. The HPC Admin confirmed the update and provided a timeline for the action.

## Problem
- **Root Cause**: User requested an update to the latest version of Star-ccm+ (2021.1) on the cluster.

## Solution
- **Action Taken**: HPC Admin scheduled the update for a specific day and later confirmed the availability of the new version as a module.

## What Can Be Learned
- **Communication**: Clear and timely communication between the user and HPC Admin regarding software updates.
- **Update Process**: The process of updating software versions on the cluster and making them available as modules.
- **User Support**: Importance of confirming the completion of requested updates to ensure user satisfaction.

## Notes
- The HPC Admin provided a timeline for the update and confirmed its completion, ensuring the user was informed throughout the process.
```
---

### 2020070542000488_Question%20on%20error%20in%20HPC.md
# Ticket 2020070542000488

 ```markdown
# HPC Support Ticket: Error in HPC Simulation

## Keywords
- HPC error
- Simulation file
- Server error
- STAR-CCM+
- Job ID
- Cluster
- Application

## Summary
A user encountered an error in their HPC simulation, resulting in incomplete output files. The user provided limited information, including a log file mentioning a "server error."

## Root Cause
- The user's simulation file, specifically related to STAR-CCM+, caused the simulation to abort.
- The HPC system itself was functioning correctly.

## Solution
- The user was advised to check their STAR-CCM+ file for issues.
- A related case was referenced for further troubleshooting: [Exporting Isosurface Data](https://www.cfd-online.com/Forums/star-ccm/184949-exporting-isosurface-data.html).

## Lessons Learned
- **Communication**: Users should provide detailed information, including job ID, cluster, and application, to facilitate troubleshooting.
- **Email Protocol**: Users should use their official FAU email address for support requests.
- **Troubleshooting**: Issues with simulation files, such as those used in STAR-CCM+, can cause aborts and should be thoroughly checked.

## Next Steps
- Ensure users provide comprehensive details in their support requests.
- Direct users to relevant resources for troubleshooting specific applications.
```
---

### 2020091442002671_r8-Version%20of%20StarCCM%2B.md
# Ticket 2020091442002671

 # HPC Support Ticket: r8-Version of StarCCM+

## Keywords
- StarCCM+
- r8 version
- double-precision
- module add
- modulefile error
- cluster emmy

## Problem
- User attempted to switch to the r8 version (double-precision) of StarCCM+ on cluster emmy.
- Followed instructions to add `-r8` after the command `module add star-ccm+/2020.1`.
- Received error: `Unable to locate a modulefile for 'star-ccm+/2020.1-r8'`.
- Simulation did not start.

## Root Cause
- Incorrect module version specified.

## Solution
- Use `star-ccm+/2020.2-r8` instead of `star-ccm+/2020.1-r8`.

## General Learning
- Ensure the correct module version is specified when adding modules.
- Double-check the availability of specific versions on the HPC website or documentation.

## Actions Taken
- HPC Admin advised the user to use the correct module version `star-ccm+/2020.2-r8`.

## Follow-up
- User acknowledged the solution and thanked the HPC Admin for the quick response.

## Documentation Reference
- This ticket can be used as a reference for similar issues related to modulefile errors and version-specific module additions.
---

### 2019090542001253_Keine%20Ergebnisdatei%20bei%20Abbruch%20der%20Simulation%20in%20StarCCM%2B.md
# Ticket 2019090542001253

 # HPC Support Ticket: Missing Result File in StarCCM+ Simulation

## Keywords
- StarCCM+
- Simulation
- Stopping Criteria
- Result File
- Output File
- Signal 15
- SSH Client PuTTY
- Batch File
- Iteration
- Maximum Runtime

## Problem Description
The user is running a StarCCM+ simulation on the HPC using the SSH client PuTTY. The simulation has multiple stopping criteria, but if the simulation is terminated due to instability or reaching the maximum runtime of one day, no result file with the computed iterations is generated. Only an output file is available, which indicates the simulation was killed by signal 15.

## Root Cause
The issue is likely due to the settings within StarCCM+ itself.

## Solution
- **Automatic Save Function**: Enable an automatic save function in StarCCM+ to periodically save intermediate results (e.g., every 100 iterations).
- **Define Iterations**: Limit the number of iterations to fit within the maximum runtime to avoid abrupt termination without results.

## Additional Notes
- The problem is not related to the SSH client PuTTY or the batch file.
- Consult other users or experts at the institution for specific StarCCM+ settings.

## Conclusion
Adjusting the settings within StarCCM+ to include an automatic save function and defining a suitable number of iterations can help ensure that intermediate results are saved even if the simulation is terminated unexpectedly.

---

This documentation can be used to address similar issues in the future by adjusting the settings within StarCCM+ to ensure intermediate results are saved.
---

### 2024061042003621_COMSOL%20Multiphysics%20-%20mfhg_mfh3008h.md
# Ticket 2024061042003621

 # HPC Support Ticket: COMSOL Multiphysics Access Issue

## Keywords
- COMSOL Multiphysics
- Access Denied
- Module Avail
- License Activation
- Group Name Typo

## Summary
A user requested access to COMSOL Multiphysics for their HPC account but encountered issues with accessing the software.

## Problem
- **Root Cause**: Typo in the group name during the license activation process.
- **Symptoms**:
  - Access denied when trying to access the COMSOL folder via `/apps/`.
  - COMSOL modules not visible with `module avail`.

## Solution
- **Action Taken**: HPC Admin corrected the typo in the group name.
- **Result**: The user should now have access to the COMSOL modules on Woody and Meggie.

## General Learnings
- Ensure accurate group names during license activation to avoid access issues.
- Verify software access by checking module availability and folder permissions.
- Limited support for specific software (e.g., COMSOL) due to lack of experience.

## Notes
- The user's group has only one COMSOL Research license, allowing use either locally or on the cluster at a time.
- Further support for COMSOL-specific issues may not be available from the HPC team.
---

### 2023120142002665_Star%20CCM%20auf%20Account%20b142dc10.md
# Ticket 2023120142002665

 # HPC Support Ticket: Star CCM auf Account b142dc10

## Keywords
- STAR CCM
- Ansys
- Software Access
- Project Account
- License Settings

## Problem Description
- User unable to access specific software (Ansys, STAR CCM+) on their project account (b142dc10).
- Suspected issue: Software not enabled for the project account.

## Root Cause
- Software access was not configured for the project account.

## Solution
- HPC Admins enabled the required software (Ansys, STAR CCM+) for the project account (b142dc10).
- License settings from "iwst" were applied.

## Lessons Learned
- Ensure that software access is properly configured for both personal and project accounts.
- Verify license settings and apply them as needed.

## Follow-Up
- Confirm with the user that the software is now accessible.
- Document the process for enabling software access for future reference.

## Related Teams
- HPC Admins
- 2nd Level Support Team
- Software and Tools Developer

## References
- Support Email: support-hpc@fau.de
- HPC Website: [https://hpc.fau.de/](https://hpc.fau.de/)
---

### 2022101742002702_Frage%20zu%20Fehlermeldung%20Starccm%2B%20Simulation.md
# Ticket 2022101742002702

 # HPC Support Ticket: Star-CCM+ Simulation Error

## Keywords
- Star-CCM+
- Meshing
- Slurm Batchfile
- Fehlermeldung
- Simulation
- .sim file
- Podkey
- CPU cores

## Problem Description
User encountered an error while meshing Star-CCM+ files using the provided template. The error message indicated that there were no regions to solve on.

## Root Cause
- Missing option to load the .sim file in the Star-CCM+ command.
- Incorrect number of CPU cores specified (PPN=40 instead of 20).
- Possible issue with the .sim file or mesh pipeline.

## Solution
1. **Include the .sim file in the Star-CCM+ command:**
   ```bash
   starccm+ -batch -cpubind v -np ${NUMCORES} --batchsystem slurm -power -podkey cRTsVNeawyfxL7IL0of2nA ${CCMARGS}
   ```

2. **Ensure there is a space between the Podkey and ${CCMARGS}:**
   ```bash
   Starting local server: /apps/STAR-CCM+/2206/STAR-CCM+2206/star/bin/starccm+ -cpubind v -np 80 -batchsystem slurm -power -podkey cRTsVNeawyfxL7IL0of2nA -load -server -rsh /usr/bin/ssh -xencoded-session QzIyLTAwMC0wMF9CYXNlc2ltXzIyMDYuc2lt
   ```

3. **Correct the number of CPU cores:**
   ```bash
   PPN=20
   ```

4. **Check the .sim file and mesh pipeline:**
   - Ensure the .sim file is correctly configured.
   - Run the mesh pipeline if necessary.

## Lessons Learned
- Always include the necessary options in the command to load the required files.
- Ensure the correct number of CPU cores is specified to avoid confusion.
- Check the .sim file and mesh pipeline for any issues if the error persists.

## Additional Notes
- The HPC Admin provided detailed guidance on correcting the command and checking the .sim file.
- The user was advised to change the number of CPU cores to avoid potential confusion.
---

### 2018080942001615_HPC%20-%20ssh%20emmy%20-%20Star%20ccm%2B%20Version%2013.04.10.md
# Ticket 2018080942001615

 # HPC Support Ticket: Star CCM+ Version Update

## Keywords
- HPC Clusterrechner
- Star CCM+
- Version Update
- Compatibility
- VM PCs
- Simulation

## Problem
- User requires Star CCM+ version 13.04.10 for simulations on the HPC cluster (ssh emmy).
- Current version on the server is 12.06.11.
- User's VM PCs have been updated to version 13.04.10, causing compatibility issues.

## Root Cause
- Mismatch between Star CCM+ versions on the user's VM PCs and the HPC cluster.

## Solution
- HPC Admin updated the server to Star CCM+ version 13.04.11, which is the latest bugfix version available from Siemens.
- The update resolved the compatibility issue, and the user was able to run simulations successfully.

## General Learnings
- Regular updates of software versions on HPC clusters are crucial to maintain compatibility with user environments.
- Communication with users about software updates and their schedules can help manage expectations and prevent disruptions in workflows.
- Testing compatibility between different patch levels within a release series is important to ensure smooth operations.

## Actions Taken
- HPC Admin acknowledged the request and provided information about the latest available version.
- The server was updated to Star CCM+ version 13.04.11.
- User confirmed that the simulations were running successfully with the updated version.

## Follow-up
- Monitor for any further compatibility issues with the updated version.
- Ensure that future updates are communicated and planned to minimize disruptions for users.
---

### 2022091242004016_Probleme%20mit%20Maggie_Star-CCM%2B.md
# Ticket 2022091242004016

 # HPC Support Ticket: Issues with Star-CCM+ on Meggie

## Keywords
- Star-CCM+
- Meggie
- Simulation
- Software not found
- Module ERROR
- Recompilation
- Aborted calculations

## Problem Description
- **Version 2022.1-r8**: Simulation ends immediately due to software not being found.
  - Error message: `Module ERROR: couldn’t execute “/apps/STAR-CCM+/2022.1-R8/STAR-CCM+2022.1/star/bin/map_mpi”: no such file or directory`
- **Version 2206**: Software starts but calculations abort with the error `starccm+ Terminated`.

## Root Cause
- **Version 2022.1-r8**: Missing installation of Star-CCM+ on Meggie.
- **Version 2206**: Unknown cause for aborted calculations.

## Solution
- **Version 2022.1-r8**: Install the missing Star-CCM+ version on Meggie.
- **Version 2206**: No specific solution provided. Needs further investigation.

## Additional Information
- Recompilation of application software on Meggie is recommended but not necessary for Star-CCM+ unless there are self-compiled user routines.
- Star-CCM+ versions are installed from binary packages provided by Siemens.

## Next Steps
- Ensure all required versions of Star-CCM+ are installed on Meggie.
- Monitor Version 2206 for further issues and investigate the cause of aborted calculations if they persist.

## Contact
For further assistance, contact the HPC Support team.
---

### 2024050542000813_Star-CCM%2B-Simulation%20auf%20Alex.md
# Ticket 2024050542000813

 # HPC-Support Ticket: Star-CCM+ Simulation auf Alex

## Keywords
- Star-CCM+
- GPU
- Post-Processing
- Apache POI
- Batch-Skript
- Freischaltung

## Problem
- User konnte Star-CCM+ auf Alex nicht nutzen.
- Fehler im Batch-Skript vermutet.
- Post-Processing Automatisierung mit Apache POI geplant.

## Ursache
- User war nicht für Star-CCM+ auf Alex freigeschaltet.

## Lösung
- HPC Admin hat den User für Star-CCM+ auf Alex freigeschaltet.
- Apache POI ist nicht zentral installiert, User muss es selbst in $WORK installieren.

## Erkenntnisse
- Star-CCM+ kommt besser mit GPUs klar als Ansys Fluent.
- Apache POI kann für die Automatisierung des Post-Processings verwendet werden.
- User müssen sich selbst um die Installation von Apache POI kümmern.

## Offene Fragen
- Kann der Dateipfad zu den Apache POI Bibliotheken in Star-CCM+ hinterlegt werden?

## Nächste Schritte
- User soll Apache POI selbst installieren und den Pfad in Star-CCM+ hinterlegen.
- HPC Admin soll prüfen, ob der Pfad zu den Apache POI Bibliotheken in Star-CCM+ hinterlegt werden kann.
---

### 2021070542002895_STARCCM%2B%202021.1.md
# Ticket 2021070542002895

 ```markdown
# HPC Support Ticket Conversation: STARCCM+ 2021.1

## Keywords
- STARCCM+ 2021.1
- Emmy2
- Simulation
- Fehlermeldung
- Script
- OpenMPI
- HP/Platform MPI

## Summary
The user encountered issues running STARCCM+ 2021.1 simulations on Emmy2, resulting in a Fehlermeldung and simulation stoppage. The problem was related to the job script, which contained options for HP/Platform MPI that are not compatible with the newer OpenMPI used by STARCCM+ 2021.1.

## Root Cause
- Incompatible job script options for HP/Platform MPI in STARCCM+ 2021.1, which uses OpenMPI.

## Solution
- Remove lines 29 to 47 from the job script.
- Refer to the current sample script for STARCCM+ at [FAU HPC Documentation](https://hpc.fau.de/systems-services/systems-documentation-instructions/special-applications-and-tips-tricks/star-ccm/#collapse_0).

## Additional Notes
- No recent changes were made to Emmy that would affect STARCCM+ 2021.1.
- The user confirmed that previous versions (2020.1) worked without issues.

## Support Team Involved
- HPC Admins
- 2nd Level Support Team
- NHR Rechenzeit Support and Applications for Grants
- Software and Tools Developer
```
---

### 42275678_Lizenzen%20f%C3%83%C2%BCr%20Intel%20Compiler%20Suite%20auf%20%22emmy%22%3F.md
# Ticket 42275678

 # HPC Support Ticket: Licenses for Intel Compiler Suite on "emmy"

## Keywords
- Intel Compiler Suite
- Licenses
- FLEXlm
- Module loading
- tcsh
- bash

## Problem Description
The user encountered an issue with missing licenses for the Intel Compiler Suite on the "emmy" cluster. Despite the tools being installed, the user received an error indicating that a license for FCompL was not available.

## Root Cause
The root cause of the problem was that the user did not load the appropriate module for the Intel Compiler Suite, which is required to access the license server.

## Solution
The HPC Admin advised the user to load the corresponding module (e.g., `intel64/14.0up02`). This action should enable the system to find the license server.

## Additional Information
- The user initially had trouble finding the modules because they were using `tcsh`. The HPC Admin confirmed that `bash` is the default shell supported on the "emmy" cluster.
- The HPC Admin later ensured that `tcsh` on the login nodes would also automatically find the modules.

## Conclusion
The issue was resolved by loading the appropriate module, which allowed the user to access the necessary licenses for the Intel Compiler Suite. The HPC Admin also made adjustments to ensure that `tcsh` users could find the modules automatically.

## General Learning
- Always ensure that the appropriate modules are loaded when using licensed software on an HPC cluster.
- Be aware of the default shell and its support for module loading on the cluster.
- If using a non-default shell, check if additional configuration is needed to access modules.
---

### 2024041142000429_Comsol%20auf%20Cluster.md
# Ticket 2024041142000429

 # HPC-Support Ticket: Comsol auf Cluster

## Keywords
- Comsol Multiphysics
- HPC Cluster
- Batch Jobs
- GUI
- Lizenz
- Dokumentation
- Support

## Problem
- User is looking for information on running Comsol Multiphysics on the HPC cluster.
- User cannot find Comsol listed under applications.
- User needs guidance on setting up and running Comsol on the cluster.

## Root Cause
- Lack of clear documentation and support for Comsol on the HPC cluster.
- Comsol is available as a module but requires a user-provided license.

## Solution
- Comsol is available as a module on woody and TinyX clusters.
- Comsol can be used within batch jobs, but interactive GUI usage is difficult.
- Users must bring their own Comsol license to use it on the clusters.
- Limited support and no specific documentation are available for Comsol.

## General Learnings
- Comsol Multiphysics can be run on the HPC cluster using batch jobs.
- Users need to provide their own Comsol license.
- Interactive GUI usage of Comsol is not well supported.
- HPC Admins have limited experience with Comsol and cannot provide extensive support.

## Next Steps
- Users should refer to general batch job documentation for running Comsol.
- Users should ensure they have a valid Comsol license before attempting to run jobs on the cluster.

## References
- HPC Cluster Documentation: [https://hpc.fau.de/](https://hpc.fau.de/)
- Contact Support: [support-hpc@fau.de](mailto:support-hpc@fau.de)
---

### 2025011842000296_AW%3A%20Manager%20access%20granted%20for%20project%20%22MABAS%20-%20Modular%20drive%20concept%20with.md
# Ticket 2025011842000296

 # HPC Support Ticket Analysis

## Subject
AW: Manager access granted for project "MABAS - Modular drive concept with fuel cell for applications in foundation engineering (b258dc)" at portal.hpc.fau.de

## Keywords
- Manager access
- Project MABAS
- STAR-CCM+
- Software packages
- Access issue
- POD-Key

## Summary
The user was granted manager access to the project "MABAS" but encountered issues accessing the STAR-CCM+ software packages. The HPC Admin resolved the issue by ensuring the project accounts had the necessary access.

## Root Cause
The user was unable to access the STAR-CCM+ software packages due to missing permissions or configuration issues.

## Solution
The HPC Admin granted the necessary access to the STAR-CCM+ software packages for the project accounts. The POD-Key for the LSTM was used.

## General Learnings
- **Manager Access**: Users with manager access can invite new users and review existing accounts.
- **Software Access**: Ensure that project accounts have the necessary permissions to access required software packages.
- **POD-Key**: The POD-Key for the LSTM was used to grant access to STAR-CCM+.
- **Support Communication**: Clear communication with the support team, including a description of the issue, is essential for quick resolution.

## Documentation Links
- [HPC Portal Documentation](https://doc.nhr.fau.de/hpc-portal/)
- [HPC Support Email](mailto:hpc-support@fau.de)

## Roles
- **HPC Admins**: Responsible for granting access and resolving technical issues.
- **2nd Level Support Team**: Provides additional support and troubleshooting.
- **Harald Lanig**: Manages NHR Rechenzeit Support and Applications for Grants.
- **Gehard Wellein**: Head of the Datacenter.
- **Georg Hager**: Training and Support Group Leader.
- **Jan Eitzinger and Gruber**: Software and Tools developers.

## Conclusion
Ensuring proper access to software packages is crucial for project success. Clear communication and prompt action by the HPC Admins resolved the issue efficiently.
---

### 2024080742003561_Fwd%3A%20Neue%20ANSYS%20Lizenz.md
# Ticket 2024080742003561

 # HPC Support Ticket: ANSYS License Exchange

## Keywords
- ANSYS License
- License Exchange
- HPC Admin
- User Request

## Summary
A user requested an urgent exchange of an attached ANSYS license. The HPC Admin promptly handled the request and confirmed its completion.

## Problem
- **Root Cause**: User needed a new ANSYS license to be exchanged promptly.

## Solution
- **Action Taken**: HPC Admin exchanged the license as requested.
- **Outcome**: The license exchange was completed successfully.

## Lessons Learned
- **User Communication**: Users should provide clear and timely requests for license exchanges.
- **Admin Responsiveness**: HPC Admins should prioritize urgent requests to ensure minimal disruption to user workflows.

## General Notes
- Ensure that license exchange requests are handled efficiently to maintain user productivity.
- Maintain clear communication channels for such requests to facilitate quick resolution.

---

This documentation can be used as a reference for handling similar license exchange requests in the future.
---

### 42112148_Ansys%20Fluent_%20CDadapco%20StarCCM%2B%20auf%20HPC-Cluster.md
# Ticket 42112148

 # HPC-Support Ticket: Ansys Fluent/CD-adapco StarCCM+ auf HPC-Cluster

## Keywords
- ANSYS-CFD
- Star-CCM+
- Software Installation
- Licensing

## Summary
A user inquires about the availability of ANSYS-CFD and Star-CCM+ on the HPC cluster and whether they need to install the software themselves.

## Root Cause
The user needs to know if ANSYS-CFD and Star-CCM+ are pre-installed on the HPC cluster or if they need to perform the installation themselves.

## Solution
- **Software Availability**: ANSYS-CFD and Star-CCM+ are already installed on the HPC cluster.
- **Licensing**: The user should contact the software vendors directly for licensing details.
- **Follow-up**: The HPC Admin suggests a follow-up phone call to discuss licensing further, but will be available only from Wednesday onwards.

## General Learnings
- Always check with HPC Admins regarding the availability of specific software packages on the cluster.
- Licensing issues should be addressed directly with the software vendors.
- Follow-up communication may be necessary to resolve all aspects of the request.

## Next Steps
- Users should verify the installation of required software with HPC Admins.
- For licensing, users should contact the software vendors directly.
- Schedule follow-up discussions with HPC Admins if needed.
---

### 2025021242004032_StarCCM%2B%20and%20GPU%20A100%20on%20alex.md
# Ticket 2025021242004032

 # HPC Support Ticket Analysis: StarCCM+ and GPU A100 on Alex

## Keywords
- StarCCM+
- GPU
- A100
- Alex
- Module Load
- Shell Script
- Benchmarking
- Migration

## Summary
A user encountered issues while migrating StarCCM+ to GPU and benchmarking on the NHR Alex system. The user faced problems with the shell script and loading the `starccm2406-clang` module. Additionally, the user requested assistance with obtaining StarCCM+/2410.

## Root Cause of the Problem
- Issues with loading the `starccm2406-clang` module.
- Potential errors in the shell script.

## Solution
- The HPC Admin instructed the user to send requests to the official support email (`support-hpc@fau.de`) instead of personal emails.
- The user was advised to try again on Alex.

## General Learnings
- Always direct support requests to the official support email to ensure proper handling and tracking.
- Ensure that module loading commands and shell scripts are correctly configured for the specific HPC environment.
- Stay updated with the latest software versions and their compatibility with the HPC system.

## Next Steps
- The user should follow up with the official support email for further assistance.
- The support team should review the shell script and module loading issues to provide a detailed solution.

## Additional Notes
- The user provided contact information and affiliation details for future reference.
- The HPC Admin emphasized the importance of using the official support channel for requests.
---

### 2016012742000643_StarCCM%2B%20auf%20HPC.md
# Ticket 2016012742000643

 ```markdown
# HPC-Support Ticket Conversation: StarCCM+ auf HPC

## Keywords
- StarCCM+
- OpenFOAM
- Batch-Skript
- Module ERROR
- License settings
- Permission denied
- Compatibility

## Summary
A user inquired about running StarCCM+ simulations on the HPC system (LiMa), as they had previously used OpenFOAM. The user requested a suitable batch script for StarCCM+.

## Issues and Solutions
1. **Module ERROR: Permission Denied**
   - **Issue**: The user encountered a Module ERROR due to permission issues with the license settings file.
   - **Solution**: The HPC Admin fixed the permissions for the license settings file.

2. **Command Not Found**
   - **Issue**: The user received an error indicating that the `starccm+` command was not found.
   - **Solution**: Ensure that the correct module is loaded and the command is available in the PATH.

## Additional Information
- **Compatibility of StarCCM+ Versions**:
  - Simulation files from older versions should open with newer versions, but there may be issues with opening newer files in older versions.
  - Macro-Features (Java scripting) may have API changes across versions.
  - Versions within the same major release should be almost fully compatible.

## Conclusion
The user was provided with a batch script for StarCCM+ and encountered issues related to module loading and permissions. The HPC Admin resolved the permission issue and provided guidance on version compatibility.
```
---

### 2023112042003004_The%20Job%20which%20runs%20a%20week%20ago%20now%20fails%20immediatly.md
# Ticket 2023112042003004

 ```markdown
# HPC Support Ticket: StarCCM+ Simulation Failure

## Keywords
- StarCCM+
- License Server
- Siemens
- Slurm
- NAT
- Port Forwarding
- License Path

## Problem Description
- User's StarCCM+ simulations, which worked previously, are now failing immediately.
- The issue started after a week of successful simulations.

## Root Cause
- The StarCCM+ license servers operated by Siemens are not accessible.
- The compute nodes cannot directly access the internet, causing issues with the license path specified in the Slurm job script.

## Troubleshooting Steps
1. **License Server Status Check**:
   - Used `lmutil lmstat -a -c 1999@flex.cd-adapco.com` to check the status of the license server.
   - Found that `lmgrd` is not running, indicating that the license server is down or not responding.

2. **PoD Management Portal**:
   - The PoD management portal was checked and found to be returning an error.

## Solution
- **Wait for Siemens to Resolve**:
  - The issue is with Siemens' license servers, which are beyond the control of the HPC support team.
  - Users are advised to wait for Siemens to resolve the issue.

- **License Path in Slurm Jobs**:
  - Ensure that the license path specified in Slurm job scripts is correct and that the compute nodes can access the license server.

## Follow-Up
- If the problem persists, users should contact the software support team to open a ticket with Siemens Support.

## General Learning
- License server issues can cause simulation failures.
- Compute nodes may not have direct internet access, affecting license path configurations.
- Regularly check the status of external license servers to diagnose similar issues.
```
---

### 2022071442002367_HPC%20Nutzung%20von%20Comsol%20_%20THN%20_%20Fakult%C3%83%C2%A4t%20AMP.md
# Ticket 2022071442002367

 ```markdown
# HPC Support Ticket: Comsol Installation and Licensing

## Keywords
- Comsol
- Installation
- Licensing
- HPC Cluster
- RRZE
- Support

## Summary
A user inquired about the availability and installation of Comsol on the HPC clusters. The user mentioned that they already use several Comsol-Research licenses from RRZE under a specific customer number.

## Root Cause
- User needs to know if Comsol is installed or planned for installation on the HPC clusters.
- User requires information about licensing compatibility with existing RRZE licenses.

## Solution
- **HPC Admin Response**: Comsol-5.6 is installed on the Woody cluster. The user's group should now have access to the installation.
- **Support Note**: Historical usage of Comsol on HPC systems was mixed, and limited support is available.

## General Learnings
- Comsol is available on the Woody cluster.
- Limited support is provided for Comsol due to past mixed experiences.
- Users should be informed about the availability of software and any limitations in support.
```
---

### 2023091842001364_Star-CCM%2B%20auf%20Fritz_Alex.md
# Ticket 2023091842001364

 # HPC-Support Ticket: Star-CCM+ auf Fritz/Alex

## Keywords
- Star-CCM+
- Fritz/Alex
- Remote-Nutzung
- Grafische Oberfläche
- HPC-Server
- Batch-Betrieb
- Slurm-Konfiguration
- IPv6
- Login-Knoten
- Loadbalancing
- DNS-RoundRobin
- POD-Kontingent
- Siemens
- Simulation
- Jobskript
- Lizenzierung

## Problem
- User möchte Star-CCM+ auf Fritz/Alex laufen lassen.
- Frage nach der Möglichkeit, die grafische Oberfläche lokal zu nutzen und die Berechnungen auf HPC-Servern durchzuführen.
- Anfrage nach einer Zoom-Sitzung zur Erklärung der Nutzung von Star-CCM+ auf Fritz/Alex.

## Lösung
- Star-CCM+ ist auf den Clustern installiert, aber nur nach Freischaltung sichtbar.
- Nutzung erfolgt analog zu Ansys: Simulationsdateien hochladen und Simulation über ein Jobskript im Batch-Betrieb starten.
- Remote-Nutzung wie von Siemens demonstriert ist mit dem aktuellen Betriebsmodell der Cluster nicht einfach umzusetzen.
- Grundvoraussetzungen für Remote-Ausführung: IPv6, spezifische Slurm-Konfiguration, Loadbalancing via DNS-RoundRobin.
- Ablauf wie bei ANSYS: Simulation lokal vorbereiten, Daten hochladen, Slurm-Batchjob abschicken, Ergebnisse herunterladen und lokal auswerten.

## Weitere Informationen
- Dokumentation und Beispielskripte für Star-CCM+ auf Fritz/Alex sind verfügbar, aber noch nicht spezifisch für diese Cluster erstellt.
- POD-Kontingent von Siemens sollte auf den HPC-Systemen problemlos nutzbar sein, indem interne Server anstelle von flex@cd-adapco.com angegeben werden.
- Fragen zur Lizenzierung und weiteren Details sollten an den zuständigen HPC Admin gerichtet werden.

## Root Cause
- Unklarheit über die Möglichkeit der Remote-Nutzung von Star-CCM+ auf HPC-Servern.
- Fehlende spezifische Anleitung und Beispielskripte für Fritz/Alex.

## Solution Found
- Klärung der Nutzungsmöglichkeiten von Star-CCM+ auf Fritz/Alex.
- Erklärung des Ablaufs zur Nutzung von Star-CCM+ im Batch-Betrieb.
- Hinweis auf die Notwendigkeit spezifischer Konfigurationen für Remote-Nutzung.

## Next Steps
- User sollte die Simulation lokal vorbereiten und die Daten auf Fritz/Alex hochladen.
- Simulation über ein Jobskript im Batch-Betrieb starten.
- Ergebnisse herunterladen und lokal auswerten.
- Bei weiteren Fragen zur Lizenzierung oder spezifischen Konfigurationen den zuständigen HPC Admin kontaktieren.
---

### 2023082842002711_Fragen%20zur%20Verwendung%20von%20ANSYS-fluent%20auf%20HPC-Systemen.md
# Ticket 2023082842002711

 # HPC-Support Ticket: Issues with ANSYS-Fluent on HPC Systems

## Subject
Fragen zur Verwendung von ANSYS-Fluent auf HPC-Systemen

## User
Masterstudent der Energietechnik an der FAU

## Problem Description
- User unable to load ANSYS modules on HPC system.
- No output when using `module avail ansys`.
- Tried different module names like `ansys/2020R1` without success.
- No details about ANSYS module found in HPC documentation.

## Steps Taken by User
1. Used `module avail ansys` to display available ANSYS modules but received no output.
2. Attempted to use different module names like `ansys/2020R1` but still unable to load the correct module.

## HPC Admin Response
1. Asked user which HPC system they were trying to load the ANSYS modules on.
2. Confirmed that the user could see other modules using `module avail`.
3. Identified that the issue was due to a missing activation on the admin side.
4. Activated the necessary permissions for ANSYS modules.
5. Provided a link to documentation for using ANSYS Fluent on the clusters: [ANSYS Fluent Documentation](https://hpc.fau.de/systems-services/documentation-instructions/special-applications-and-tips-tricks/ansys-fluent/)

## Solution
- The issue was resolved by the HPC Admin activating the necessary permissions for ANSYS modules.
- User was advised to connect to the `meggie` cluster using `ssh ilev007h@meggie.rrze.fau.de` to access and load ANSYS modules.

## Additional Information
- User was informed about an upcoming "Introduction for HPC beginners" session on Wednesday, 13.09.23 via Zoom.
- Slides for the session can be found here: [HPC in a Nutshell](https://hpc.fau.de/files/2023/07/2023-07-12_HPC_in_a_Nutshell.pdf)

## Keywords
- ANSYS Fluent
- Module loading
- HPC system
- Permissions
- Documentation
- Training session

## Lessons Learned
- Ensure that the necessary permissions and activations are in place for specific modules.
- Provide clear documentation and training sessions for users to understand the HPC environment and module usage.
- Communicate effectively with users to identify the root cause of the problem and provide appropriate solutions.
---

### 2023082342002819_Ung%C3%83%C2%BCltiger%20Podkey%20Star%20CCM%20-%20iwst012h.md
# Ticket 2023082342002819

 # HPC-Support Ticket: Invalid Podkey Star CCM+

## Keywords
- Star CCM+
- License Server
- Podkey
- CDLMD_LICENSE_FILE
- Batch Jobs
- Frontend Nodes

## Problem Description
- User unable to open simulations in Star CCM+.
- Error message indicates no license server found or CDLMD_LICENSE_FILE not set.
- Issue affects multiple users and simulations created with different versions of Star CCM+.

## Root Cause
- License server not being correctly referenced in the software.
- CDLMD_LICENSE_FILE environment variable not set properly.

## Troubleshooting Steps
1. **HPC Admin** confirmed that the license server should be referenced as:
   ```
   Checking license file: 1999@hpclicense1.rrze.uni-erlangen.de
   Checking license file: 1999@131.188.3.151
   ```
2. **HPC Admin** tested the Podkey and successfully obtained a license via `1999@131.188.3.151`.
3. **HPC Admin** verified that batch jobs were able to obtain licenses without issues.

## Solution
- Ensure that the CDLMD_LICENSE_FILE environment variable is set correctly to point to the license server.
- Verify that the license server is accessible from the frontend nodes.

## Additional Notes
- The issue was not reproducible by the HPC Admin, suggesting a possible configuration issue on the user's end.
- Local Podkey from the user's department worked without issues, indicating a potential network or configuration problem specific to the HPC environment.

## Follow-up Actions
- User should check and set the CDLMD_LICENSE_FILE environment variable.
- If the issue persists, further investigation into network connectivity and configuration settings may be required.

---

This documentation can be used to troubleshoot similar license server issues in the future.
---

### 2019071142002146_Star%20ccm%20auf%20HPC.md
# Ticket 2019071142002146

 ```markdown
# HPC Support Ticket: Star CCM+ Issues

## Keywords
- Star CCM+
- Batch files
- Modulefile error
- Login nodes
- Version compatibility

## Summary
- **User Issue**: User experiencing problems running simulations with Star CCM+ via PuTTY and batch files. Suspected issue with newer version of Star CCM+ not correctly referenced in batch files.
- **Error Message**: `unable to locate a modulefile for 'star-ccm+/14.02.012-R8'`

## Conversation Highlights
- **User**:
  - Mentioned using Star CCM+ version 2019.1.1 (Build 14.02.012-R8) and previously used 13.02.013-R8.
  - Requested assistance with modulefile error.
  - Provided batch file and screenshot of error messages.

- **HPC Admin**:
  - Advised user to check available Star CCM+ versions using `module avail star-ccm+`.
  - Clarified that the screenshot provided contained informative messages, not errors.

## Root Cause
- Incorrect modulefile reference in batch files leading to `unable to locate a modulefile` error.

## Solution
- Use the `module avail star-ccm+` command to list available versions and ensure the correct modulefile is referenced in the batch files.
- Verify that the batch file is correctly configured for the available Star CCM+ versions.

## General Learnings
- Always check available software versions using the appropriate command (e.g., `module avail`).
- Ensure batch files reference the correct modulefiles to avoid errors.
- Informative messages in logs should not be confused with error messages.

## Additional Notes
- Users should use their university email for support requests.
- Understanding login nodes and their role in HPC environments is important for troubleshooting.
```
---

### 2025012442002237_Request%20for%20update%20COMSOL%20to%206.3%20update%201.md
# Ticket 2025012442002237

 ```markdown
# HPC Support Ticket: COMSOL Update Request

## Keywords
- COMSOL Multiphysics
- Version Update
- HPC Account
- Module Installation

## Summary
A user requested an update of COMSOL Multiphysics from version 6.2 to 6.3 update 1 on the Woody cluster.

## Root Cause
User needed a newer version of COMSOL for their work.

## Solution
HPC Admins installed the requested version of COMSOL and made it available as a module.

## What Can Be Learned
- **User Request Handling**: Properly handle user requests for software updates.
- **Module Management**: Ensure new software versions are installed and made available as modules.
- **Communication**: Inform users once the requested update is completed.

## Ticket Conversation
### User Request
```
Dear FAU HPC support team,

I am writing to request for an update of the version of COMSOL Multiphysics from 6.2 to 6.3 update 1 on Woody.
My HPC account is iwal159h.
Could you please let me know if this update is possible, and if so, when can this update be done?
If you need more information, please let me know!

Thank you very much in advance!

Kind regards,
Zeyu
```

### HPC Admin Response
```
Dear Zeyu,

Woody now has a "comsol/6.3" module.

Kind regards
Thomas Zeiser
```
```
---

### 2023020142000301_Ansys%20Maxwell.md
# Ticket 2023020142000301

 # HPC Support Ticket: Ansys Maxwell Simulation

## Keywords
- Ansys Maxwell
- HPC Cluster
- License
- Local Installation
- File Preparation
- Slurm Batch Script
- Woody Cluster
- RRZE
- FAU

## Summary
A professor from the Chair of Experimental Physics at FAU contacted HPC support to run Ansys Maxwell simulations on the HPC cluster. The HPC admins provided guidance on licensing, local installation, and running simulations on the cluster.

## Key Points to Learn

### Licensing
- Ansys Maxwell is part of RRZE's "Ansys Multiphysics Research" campus license.
- One token allows running one simulation on up to 4 cores.
- "Ansys HPC Research" tokens are required for simulations on more than 4 cores.
- License usage on HPC competes with local licenses.

### Local Installation
- Download ISO files from the LSD server after ordering licenses from RRZE.

### File Preparation
- HPC support cannot assist with file preparation.

### Running Simulations on HPC
- Users work directly on the HPC systems; files are not sent to admins.
- Personal HPC accounts are required for each user.
- Access to HPC systems is via SSH.
- Users need to write Slurm batch scripts for batch execution.
- Woody cluster is recommended for initial simulations.

### Additional Resources
- Monthly HPC introduction sessions for new users.
- Upcoming visit from ANSYS delegation for troubleshooting.

## Root Cause of the Problem
- Lack of experience with Ansys Maxwell on the HPC cluster, requiring trial and error.

## Solution
- HPC admins provided guidance and resources for licensing, installation, and running simulations.
- Users need to adapt job scripts to the HPC environment.
- ANSYS delegation visit can help address specific issues.

## Follow-up
- Users have not provided updates since the initial contact.
- HPC admin followed up, mentioning an upcoming ANSYS delegation visit for troubleshooting.

## References
- [RRZE Ansys Multiphysics Research](https://www.rrze.fau.de/hard-software/software/dienstliche-nutzung/produkte/ansys/)
- [HPC Getting Started](https://hpc.fau.de/systems-services/documentation-instructions/getting-started/)
- [HPC Account Application](https://www.rrze.fau.de/files/2017/06/HPC-Antrag.pdf)
- [HPC Introduction Sessions](https://hpc.fau.de/teaching/hpc-cafe/)
- [Job Script Examples](https://www.luis.uni-hannover.de/de/services/betrieb-und-infrastruktur/software-lizenzen/software-katalog/produkte/ansys-electronics/ansys-electronics-zusatzinfos/maxwell-auf-dem-cluster)
- [ANSYS Maxwell FAQs](https://rescale.com/documentation/main/ansys-resources/ansys-maxwell/ansys-maxwell-faqs/)
- [LRZ Documentation](https://doku.lrz.de/pages/viewpage.action?pageId=48922659)
- [SCC KIT Documentation](https://www.scc.kit.edu/produkte/3840.php?tab=%5B9166%5D#tabpanel-9166)
---

### 2023092542004615_Request%20for%20an%20HPC%20account.md
# Ticket 2023092542004615

 ```markdown
# HPC Support Ticket Conversation Analysis

## Subject: Request for an HPC Account

### Keywords:
- HPC Account
- COMSOL v6.1
- Windows Version
- SLURM
- Meggie Cluster
- Modules
- Woody Cluster

### Summary:
A user requested an HPC account to work with the Windows version of COMSOL v6.1 using SLURM as a batch system on the Meggie cluster. The user inquired about the need to inform the HPC admins about the modules they will be using.

### Root Cause of the Problem:
- User needs access to COMSOL v6.1 on the Meggie cluster.
- Uncertainty about module requirements.

### Actions Taken:
1. **HPC Admin**: Extended the user's HPC ID and forwarded the request to the HPC department.
2. **HPC Admin**: Informed the user that COMSOL v6.1 is already installed on the Woody cluster and provided access details.

### Solution:
- The user was granted access to COMSOL v6.1 on the Woody cluster.
- The user was advised to log into `woody.nhr.fau.de` to see the available module.

### Additional Information:
- The Woody cluster is suitable for the user's requirements.
- Multinode usage is not the primary goal; the focus is on throughput for parameter variations.

### Documentation Link:
- [Woody Cluster Documentation](https://hpc.fau.de/systems-services/documentation-instructions/clusters/woody-cluster/)

### Conclusion:
The user's request was addressed by providing access to the required software on an appropriate cluster. The user was informed about the availability of COMSOL v6.1 on the Woody cluster and how to access it.
```
---

### 2021100642004171_Nutzung%20des%20HPC%20Service.md
# Ticket 2021100642004171

 ```markdown
# HPC Support Ticket: Nutzung des HPC Service

## Keywords
- Ansys Workbench
- HPC Service
- Simulation
- Research-Lizenzen
- Teaching-Lizenzen
- Batch-Job
- GUI-basierte Anwendung
- Lizenzserver

## Problem
- User is a student working on a Bachelor's thesis involving simulations with Ansys Workbench.
- Each simulation takes at least 22 hours.
- User inquires about using the HPC service to speed up the simulation process.

## Root Cause
- Ansys Workbench is a GUI-based application that requires specific graphic libraries not available on most cluster nodes.
- Non-interactive computation (batch-job) is not possible with Workbench.
- Only Research-Lizenzen can be used on HPC systems, not Teaching-Lizenzen.

## Solution
- Use other Ansys software like Mechanical for partial simulations on the HPC clusters.
- Ensure the availability of Research-Lizenzen, as the number of simultaneous computations is limited by the number of available licenses.

## General Learnings
- GUI-based applications like Ansys Workbench are difficult to run on HPC clusters due to the lack of necessary graphic libraries.
- Batch-job computation is not supported by Ansys Workbench.
- Only Research-Lizenzen are usable on HPC systems, and the number of simultaneous jobs is limited by the available licenses.
- Partial simulations using compatible software (e.g., Ansys Mechanical) can be run on HPC clusters.
```
---

### 2024011642002871_Ansys_FEM%20HPC.md
# Ticket 2024011642002871

 # HPC-Support Ticket: Ansys/FEM HPC

## User Issue
- User is working on a project using Ansys FEM and needs to combine it with HPC due to high computational demands.
- User is unsure about the format of input data required to send to the server.
- User inquires about the availability of a maintenance contract or similar support from Ansys.

## HPC Admin Responses
- HPC Admin suggests that the simulation on HPC can only be done from Ansys Multiphysics Research with sufficient licenses on a Lehrstuhlrechner that meets hardware requirements.
- HPC Admin provides links to Ansys platform support, hardware tips, and usability guidelines.
- HPC Admin confirms that Ansys Research can only be run on FAU-owned devices, not on private computers.
- HPC Admin explains the licensing model and the need for additional HPC licenses if more than 4 cores per task are required.

## 2nd Level Support Responses
- 2nd Level Support confirms that Ansys Teaching has no HPC increments, and projects need to be transferred to Research for HPC usage.
- 2nd Level Support provides information on the licensing requirements and costs for Ansys Multiphysics Research and HPC Research Staffel.
- 2nd Level Support suggests using Ansys Teaching on a private computer for project preparation and then transferring it to the Lehrstuhlrechner for HPC usage.

## Solution
- User needs to use Ansys Multiphysics Research for HPC simulations.
- User needs to ensure that the Lehrstuhlrechner meets the hardware requirements specified by Ansys.
- User needs to obtain the necessary HPC licenses if more than 4 cores per task are required.
- User can prepare projects using Ansys Teaching on a private computer and then transfer them to the Lehrstuhlrechner for HPC usage.

## Additional Resources
- Ansys Platform Support: [Ansys Platform Support](https://www.ansys.com/it-solutions/platform-support)
- Hardware Tips: [Hardware Tips to Accelerate Simulation](https://www.ansys.com/blog/hardware-tips-to-accelerate-simulation)
- Usability Guidelines: [Hardware Usability Guidelines for Engineering Simulation](https://www.ansys.com/resource-center/webinar/hardware-usability-guidelines-for-engineering-simulation)
- Ansys Forum: [Ansys Forum](https://forum.ansys.com/)
- Ansys APDL Course: [Intro to Ansys Mechanical APDL Scripting](https://courses.ansys.com/index.php/courses/intro-to-ansys-mechanical-apdl-scripting/)

## Keywords
- Ansys FEM
- HPC
- Input Data
- Licensing
- Hardware Requirements
- Ansys Teaching
- Ansys Research
- Multiphysics Research
- HPC Research Staffel
- Lehrstuhlrechner
- Private Computer
- Project Preparation
- Simulation
- CPU Cores
- HPC Licenses
- Platform Support
- Hardware Tips
- Usability Guidelines
- Ansys Forum
- APDL Scripting

## General Learnings
- Understanding the licensing model and hardware requirements for Ansys HPC simulations.
- Preparing projects using Ansys Teaching on a private computer and transferring them to the Lehrstuhlrechner for HPC usage.
- Obtaining additional HPC licenses if more than 4 cores per task are required.
- Utilizing available resources such as the Ansys Forum and APDL scripting course for further assistance.
---

### 2022072042000151_Star-ccm%20Versionsupdate%20Meggie.md
# Ticket 2022072042000151

 ```markdown
# HPC-Support Ticket Conversation: Star-CCM Version Update on Meggie

## Keywords
- Star-CCM
- Version 2206
- Meggie
- Workflow Simplification
- Module Installation

## Problem
- User requested the installation of the latest Star-CCM version (2206) on Meggie due to a new feature that simplifies the workflow.

## Solution
- HPC Admin confirmed the availability of the Star-CCM/2206 module on Meggie.

## Lessons Learned
- Users can request software updates for specific versions if they provide a valid reason.
- HPC Admins can quickly respond to such requests and confirm the availability of the requested software versions.

## Root Cause
- User needed a specific feature available in the latest version of Star-CCM to simplify their workflow.

## Actions Taken
- HPC Admin installed and made available the Star-CCM/2206 module on Meggie.

## Notes
- Ensure that software versions are up-to-date to meet user requirements and improve workflow efficiency.
- Communicate clearly with users about the availability of requested software versions.
```
---

### 2023111942000359_StarCCM-Simulation%20auf%20Meggie.md
# Ticket 2023111942000359

 # HPC Support Ticket: StarCCM+ Simulation auf Meggie

## Keywords
- StarCCM+
- Lizenzserver
- Siemens
- PoD-Lizenzserver
- Simulation
- Meggie
- Fehlermeldung
- Job abbrechen

## Problem
- User reports that StarCCM+ simulations on Meggie are failing.
- Jobs are aborting and an output file is provided.

## Root Cause
- The PoD-Lizenzserver for StarCCM+, operated by Siemens, is down or not responding correctly.

## Solution
- The issue is with the external license servers managed by Siemens.
- HPC Admins identified that the license servers were down and needed to be fixed by Siemens.
- Users were advised to wait as the license servers usually come back online after a few hours.
- If the problem persists, users should contact `software@fau.de` to open a ticket with Siemens support.

## Actions Taken
- HPC Admins checked the status of the PoD-Lizenzserver.
- HPC Admins informed the user about the license server issue and provided contact information for further support.
- The license servers eventually came back online, resolving the issue.

## General Learnings
- License server issues can cause simulation jobs to abort.
- External license servers are outside the direct control of HPC Admins.
- Users should be informed about the status of license servers and provided with contact information for further assistance.
- Regular checks on the status of external license servers can help in proactive issue resolution.

## Follow-up
- Monitor the status of external license servers.
- Inform users promptly about any known issues with license servers.
- Provide contact information for external support if the issue persists.
---

### 2022102142002089_Verwendung%20Rechenzentrum%20f%C3%83%C2%BCr%20Simulationen.md
# Ticket 2022102142002089

 # HPC Support Ticket: Using HPC for Simulations

## Keywords
- HPC Account Activation
- FAU-IdM-Account
- STAR-CCM+
- Simulation Preparation
- SCP File Transfer
- HPC Storage
- Getting Started Guide

## Problem
- User is unsure how to prepare simulations for the HPC system.

## Solution
1. **Account Activation**:
   - User needs to activate their FAU-IdM-Account.
   - HPC account (e.g., `corz001h`) will be created one day after IdM activation.

2. **Simulation Preparation**:
   - User will work with STAR-CCM+.
   - Example script available at: [STAR-CCM+ Documentation](https://hpc.fau.de/systems-services/documentation-instructions/special-applications-and-tips-tricks/star-ccm/#collapse_0)

3. **File Transfer**:
   - Create SIM-Datei locally.
   - Transfer files using SCP.
   - Store simulation files in `$WORK` directory (e.g., `/home/woody/corz/corz001h`).
   - Do not store in `$HOME`.

4. **Additional Resources**:
   - HPC Storage Documentation: [HPC Storage](https://hpc.fau.de/systems-services/documentation-instructions/hpc-storage/)
   - Getting Started Guide: [Getting Started](https://hpc.fau.de/systems-services/documentation-instructions/getting-started/)

5. **Collaboration**:
   - Suggested collaboration with another user who has experience with STAR-CCM+.

## General Learning
- Proper account activation and setup are crucial for accessing HPC resources.
- Specific instructions and scripts are available for different applications.
- Correct file storage practices are important for efficient use of HPC systems.
- Collaboration with experienced users can facilitate the learning process.

## References
- [STAR-CCM+ Documentation](https://hpc.fau.de/systems-services/documentation-instructions/special-applications-and-tips-tricks/star-ccm/#collapse_0)
- [HPC Storage](https://hpc.fau.de/systems-services/documentation-instructions/hpc-storage/)
- [Getting Started](https://hpc.fau.de/systems-services/documentation-instructions/getting-started/)
---

### 2019112742000084_Coupling%20Ansys%20Fluent%20and%20Mechanical.md
# Ticket 2019112742000084

 # HPC Support Ticket: Coupling Ansys Fluent and Mechanical

## Keywords
- Ansys Fluent
- Ansys Mechanical
- Coupling Simulations
- Workbench
- HPC Environment
- Command Line Interface (CLI)

## Problem
- User wants to couple Ansys Fluent and Ansys Mechanical in an HPC environment that does not offer the Workbench platform.
- User has no prior knowledge about setting up such simulations without Workbench.

## Root Cause
- Lack of graphical user interface (GUI) support for Workbench in the HPC environment.
- User's inexperience with command-line based setup for coupled simulations.

## Solution
- **General Advice**:
  - Coupled simulations are possible but not straightforward to implement without Workbench.
  - User needs to set up Fluent and Mechanical cases separately using command-line interfaces.

- **Commands**:
  - Start Ansys Mechanical using the command `ansys<Version>`, e.g., `ansys181` or `ansys193`.
  - Specify the input file with the parameter `-i inputfile.dat`.

- **Further Assistance**:
  - For detailed help, the user should consult their thesis advisor.
  - HPC support can provide general technical advice but not in-depth simulation instructions.

## Lessons Learned
- Users should be aware that complex simulations like coupling Ansys Fluent and Mechanical can be challenging without a GUI.
- Basic knowledge of command-line operations is essential for setting up such simulations in an HPC environment.
- Users should seek guidance from their academic advisors for detailed simulation setups.

## Next Steps
- User should attempt to set up the simulations using the provided commands.
- If further assistance is needed, the user should consult their thesis advisor or refer to Ansys documentation for command-line operations.

---

This documentation aims to assist HPC support employees in resolving similar issues related to coupling Ansys Fluent and Mechanical in an HPC environment without Workbench.
---

### 2023050842001934_HPC%20requirements%20-%20Ansys%20Maxwell%20_%20mpo1%20_%20Prof.%20Eichler.md
# Ticket 2023050842001934

 # HPC Support Ticket: Ansys Maxwell Requirements

## Keywords
- Ansys Maxwell
- HPC Account
- Embarrassing Parallelization
- License Management
- Job Size
- Computing Time
- Memory Requirements

## Summary
A master student from Professor Eichler's group requested assistance with filling out an HPC usage form for running finite element simulations using Ansys Maxwell. The student intended to run up to 500 independent simulations, each requiring 4 cores, less than 20 minutes of computing time, and less than 10GB of memory.

## Issues and Solutions

### Issue: License Availability
- **Root Cause**: Ansys is commercial software, and the HPC systems do not have licenses for it. The student's chair has only one license for Ansys.
- **Solution**: The student needs to bring their own licenses. Only one job can run on the HPC systems at a time, and only if no other Ansys process is open at the chair.

### Issue: Software Compatibility
- **Root Cause**: Ansys Electronics Software relies on the ANSYS proprietary scheduler (ANSYS Remote Solver Manager), which is not compatible with the SLURM scheduler used on LRZ HPC systems.
- **Solution**: For ANSYS Release 2019.R3, it was possible to run electronics software solvers like Maxwell-2d/3d and HFSS on LRZ HPC systems with direct help from ANSYS developers. However, this support is no longer provided for later releases.

### Issue: Account Usage
- **Root Cause**: The student had an HPC account but had not used it yet.
- **Solution**: The student confirmed that they plan to use the account for upcoming simulations.

## General Learnings
- Commercial software like Ansys requires users to bring their own licenses.
- Software compatibility issues, such as scheduler incompatibility, can limit the use of certain software on HPC systems.
- Embarrassing parallelization can be beneficial for running multiple independent simulations with short computing times.
- Regular follow-ups can help ensure that users are making the most of their HPC accounts.

## References
- [Possible Support on LRZ HPC Systems for ANSYS Electronics Software](https://doku.lrz.de/pages/viewpage.action?pageId=48922659)
- [FAU HPC Support](https://hpc.fau.de/)
---

### 2023112742001477_Fragen%20zu%20HPC%20-%20iwep.md
# Ticket 2023112742001477

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Keywords
- Ansys Mechanical
- Woody Rechner
- Simulation
- HPC Zugang
- Kommandozeile
- Ansys Mechanical APDL
- Batch Jobs
- Datentransfer
- Zoom Meeting

## Problem
- User needs to run Ansys Mechanical simulations on the Woody Rechner but is unsure about the specific commands and process.
- User lacks clarity on how to input and output files for the simulation.

## Steps Taken
- HPC Admins provided general documentation links for getting started with HPC clusters.
- Specific documentation for Ansys Fluent, CFX, and Mechanical was shared.
- A sample script for running Ansys Mechanical on Woody was added to the documentation.
- Information on logging into clusters, data transfer, and submitting batch jobs was provided.
- A Zoom meeting was scheduled to clarify the user's questions.

## Solution
- The user was advised to use the command line for Ansys Mechanical APDL as the graphical interface (Workbench) is not available.
- A sample script was provided and the user was instructed to adapt it to their specific input.
- A Zoom meeting was arranged to provide personalized assistance.

## General Learnings
- Users should refer to the provided documentation for initial setup and specific application instructions.
- For complex or less documented applications, personalized support through meetings can be beneficial.
- Regular training sessions and documentation updates are crucial for user support.
```
---

### 2021122042000992_Access%20to%20star-ccm%2B.md
# Ticket 2021122042000992

 ```markdown
# HPC-Support Ticket Conversation: Access to STAR-CCM+

## Keywords
- STAR-CCM+
- HPC
- Software License
- Student Access
- SSH Connection
- Module Availability

## Summary
A Master's student in Computational Engineering inquired about accessing STAR-CCM+ on the HPC and the availability of a student version of the software.

## Root Cause of the Problem
- The student attempted to access STAR-CCM+ on the HPC but was unable to find the software using the `module avail` command.
- The student was interested in training on STAR-CCM+ and inquired about a student version of the software.

## HPC Admin Response
- FAU does not have a general campus license for STAR-CCM+.
- Only a few chairs have a license for their specific needs.
- The student's HPC account is limited to tutorials for a specific computer science lecture.
- The HPC Admin was unaware of Siemens' offerings for STAR-CCM+ for students.

## Solution
- The student was informed that access to STAR-CCM+ on the HPC is not available due to licensing restrictions.
- The student was advised that their HPC account is intended for specific tutorials.
- No solution was provided regarding the availability of a student version of STAR-CCM+.

## General Learnings
- Licensing restrictions can limit software availability on HPC systems.
- Students should verify software availability and licensing terms before attempting to access specific software.
- HPC accounts may have usage restrictions based on the user's role or course requirements.
```
---

### 2021042842000608_WG%3A%20StarCCM%2B%20Access.md
# Ticket 2021042842000608

 ```markdown
# HPC-Support Ticket: StarCCM+ Access

## Keywords
- StarCCM+
- Access Request
- License
- Computational Engineering

## Summary
A student requested access to StarCCM+ for a job-related course. The HPC Admin responded that FAU does not have a general license for StarCCM+ and that only a few chairs hold their own licenses.

## Root Cause
- User requested access to StarCCM+ for educational purposes.

## Solution
- Informed the user that FAU does not have a general license for StarCCM+.
- Advised that only specific chairs hold licenses for StarCCM+.

## General Learnings
- FAU does not provide general access to StarCCM+.
- Access to StarCCM+ is limited to specific chairs with their own licenses.
- Users should be directed to the appropriate chairs for access requests.
```
---

### 42024557_Fw%3A%20Ansys%20Testlizenzschl%C3%83%C2%BCssel.md
# Ticket 42024557

 # HPC Support Ticket Conversation Analysis

## Subject: Fw: Ansys Testlizenzschlüssel

### Keywords:
- Ansys Test License
- CFX License
- Installation
- License File
- Customer Evaluation License
- License Server
- ANSLIC_ADMIN Utility

### Summary:
A user from Continental Automotive GmbH requested the installation of an Ansys CFX license on the HPC system. The user provided a test license key received from Ansys and requested assistance with the installation.

### Root Cause of the Problem:
- The user needed the Ansys CFX license installed on the HPC system.
- The user had received a test license key from Ansys but required assistance with the installation process.

### Solution:
- The HPC Admin installed the new license file and informed the user accordingly.

### General Learnings:
- Users may require assistance with installing software licenses on the HPC system.
- HPC Admins should be familiar with the installation process for software licenses, including the use of the ANSLIC_ADMIN utility.
- Proper communication and follow-up with users are essential to ensure that their requests are addressed promptly.

### Steps for Future Reference:
1. **Receive License Key**: Ensure the user provides the license key and any relevant information.
2. **Install License**: Use the ANSLIC_ADMIN utility to install the license key on the license server.
3. **Inform User**: Notify the user once the installation is complete.
4. **Troubleshooting**: If issues arise, refer to the ANSYS Licensing Troubleshooting document or the ANSYS Licensing Guide.

### Additional Resources:
- [ANSYS Licensing Troubleshooting Document](http://www.ansys.com/services/ss-documentation-license.asp)
- [ANSYS Licensing Guide](http://www1.ansys.com/customer)

This documentation can be used as a reference for future support tickets related to software license installations on the HPC system.
---

### 2019121942001221_CAT-Racing%20ANSYS.md
# Ticket 2019121942001221

 # HPC-Support Ticket: CAT-Racing ANSYS

## Keywords
- ANSYS Mechanical
- FEM (Finite Element Method)
- Topology Optimization
- License Server
- VPN
- Port Forwarding

## Problem
- User wants to run FEM and topology optimizations with ANSYS Mechanical on the HPC cluster.
- No information found on how to set this up.

## Root Cause
- Lack of information on ANSYS license type and access method to the license server.

## Solution
1. **Identify License Type and Access Method**:
   - User is using an Academic License via the university's internal license server.
   - Access can be granted via VPN or by freeing up an IP address.

2. **VPN Not Suitable for Compute Nodes**:
   - VPN is not an option for the compute nodes of the HPC cluster.

3. **Port Forwarding Setup**:
   - The university's data center needs to provide the license ports for `131.188.3.151` (grid.rrze.uni-erlangen.de).
   - Specify the ports for `lmgrd` and vendor daemon to set up local port forwarding for the HPC cluster.

## General Learnings
- Always clarify the type of license and access method for software requiring a license server.
- VPN is not a viable solution for compute nodes in an HPC environment.
- Port forwarding is a common method to allow HPC clusters to access external license servers.

## Next Steps
- User to provide the necessary port information to the HPC Admins.
- HPC Admins to set up port forwarding based on the provided information.

## References
- HPC Services, Friedrich-Alexander-Universitaet Erlangen-Nuernberg
- Regionales RechenZentrum Erlangen (RRZE)

## Contact Information
- HPC Support: `support-hpc@fau.de`
- HPC Services Website: [RRZE HPC Services](http://www.hpc.rrze.fau.de/)
---

### 42115447_CD-adapco%20Star-CCM%2B.md
# Ticket 42115447

 # HPC-Support Ticket: CD-adapco Star-CCM+

## Keywords
- Star-CCM+
- Studentenlizenz
- FAPS
- Formula Student Team
- Academic Program

## Problem
- User inquires about obtaining a Star-CCM+ student license and its cost.
- User needs access to Star-CCM+ for a potential internship that requires knowledge of the software.

## Solution
- **HPC Admin** informs the user that Star-CCM+ is not available in the CIP-Pools.
- **HPC Admin** suggests contacting Frau Schäfer from FAPS (franziska.schaefer@faps.uni-erlangen.de) for potential access.
- **HPC Admin** recommends checking with the Formula Student Team ([Octanes](http://www.octanes.de/)) for a Star-CCM+ license.
- **HPC Admin** mentions the "Academic Program" by CD-adapco ([link](http://www.cd-adapco.com/industries/academia/index.html)) and suggests contacting info-de@cd-adapco.com for more information.

## General Learnings
- Star-CCM+ licenses are shared among various departments and not available to individual students.
- Specific departments like FAPS and the Formula Student Team may provide access to the software.
- The CD-adapco Academic Program might offer student licenses, but availability in Germany is uncertain.

## Actions Taken
- **HPC Admin** provided detailed information on where to find Star-CCM+ licenses.
- **HPC Admin** suggested contacting specific individuals and teams for potential access.
- **HPC Admin** mentioned the Academic Program and provided contact information for further inquiries.

## Follow-up
- User should follow up with the suggested contacts to gain access to Star-CCM+.
- If the Academic Program is pursued, the outcome should be shared with the HPC Admin.
---

### 2022020842002217_Emmie%20mit%20Star-CCM%202021.3.md
# Ticket 2022020842002217

 ```markdown
# HPC-Support Ticket: Star-CCM+ 2021.3 Installation Request

## Keywords
- Emmie
- Star-CCM+
- Version 2021.3
- Installation Request
- Projektarbeit

## Summary
A user requested the installation of Star-CCM+ version 2021.3 on Emmie for their project work.

## Root Cause
The user needed a specific version of Star-CCM+ for their project work.

## Solution
The HPC Admin informed the user that the requested version of Star-CCM+ (2021.3.1) is now available on Emmie.

## Lessons Learned
- Users may require specific software versions for their projects.
- HPC Admins can install and provide access to requested software versions.
- Effective communication between users and HPC Admins is crucial for resolving software requests.
```
---

### 2020112642001788_Ansys%20Licence%20Preference.md
# Ticket 2020112642001788

 # HPC Support Ticket: Ansys License Preference Issue

## Keywords
- Ansys License Preferences
- Ansys 2019R1
- Academic Research CFD
- Academic Research Mechanical and CFD
- Solver and PrepPost

## Problem Description
The user is unable to find the specific Ansys license preferences needed for Ansys 2019R1: "ANSYS Academic Research CFD" and "ANSYS Academic Research" in Solver and PrepPost. Instead, they see an option for "ANSYS Academic Research Mechanical and CFD," which they are not supposed to use.

## Root Cause
- Possible misconfiguration in the XML files during the last installation.
- Expired certificate.

## Troubleshooting Steps
1. **HPC Admin** reviewed the installation and XML configuration.
2. **HPC Admin** attempted to reproduce the issue but was unable to do so.
3. **HPC Admin** requested more details from the user on the steps taken and where the preferences were being changed.

## Solution
- The issue was not resolved in the provided conversation.
- Further details from the user are required to diagnose the problem accurately.

## General Learnings
- Ensure XML configurations are correctly set up during Ansys installations.
- Check for expired certificates when troubleshooting license issues.
- Gather detailed steps from the user to reproduce the problem effectively.

## Next Steps
- Await further details from the user to reproduce and resolve the issue.
- Verify the XML configurations and certificate status.

## Relevant Roles
- **HPC Admins**: Responsible for troubleshooting and resolving the issue.
- **2nd Level Support Team**: May assist in gathering more information or escalating the issue if needed.
- **Head of the Datacenter** and **Training and Support Group Leader**: Oversee the resolution process and ensure proper support is provided.

## Documentation Note
This report can be used as a reference for similar Ansys license preference issues in the future. Ensure to update the XML configurations and check for certificate expiry when troubleshooting such problems.
---

### 42206201_Auslatung%20Lizenz%20Ansys.md
# Ticket 42206201

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject: Auslatung Lizenz Ansys

### Keywords
- ANSYS Academic Research Mechanical
- ANSYS Academic Research CFD
- Lizenzen
- Prozessoren / Kerne
- Tokens
- Abaqus

### Summary
The user has licenses for ANSYS Academic Research Mechanical and CFD and wants to understand how to effectively use them, especially in relation to the number of processors/cores. The user also mentions "5 Tokens" but is unsure what they are for.

### Root Cause of the Problem
- Lack of understanding about the capabilities and limitations of the ANSYS licenses.
- Confusion about the concept of "Tokens" in the context of ANSYS licenses.

### Solution
- **HPC Admin** provided a detailed document ([Academic_features_table_14_rev_1.pdf](http://www.scc.kit.edu/downloads/sca/Academic_features_table_14_rev_1.pdf)) explaining the capabilities of the ANSYS licenses.
- Clarified that parallel calculations with up to 4 cores on a single machine are included in both Mechanical and CFD licenses.
- Explained that additional licenses ("Tokens") are required for more complex scenarios such as multiple independent calculations, calculations across multiple machines, or parallel calculations with more than 4 cores.

### Additional Questions
- The user asked about the situation with Abaqus regarding processors/cores.
- **HPC Admin** noted that the Abaqus question would be handled in a separate ticket.

### General Learnings
- Understanding the specific capabilities and limitations of software licenses is crucial for effective use.
- Additional licenses or "Tokens" may be required for advanced usage scenarios.
- Separate tickets should be created for different software-related questions to keep the support process organized.
```
---

### 2024013042002969_HPC%20Ansys%20Testlauf.md
# Ticket 2024013042002969

 ```markdown
# HPC Ansys Testlauf

## Keywords
- Ansys
- Testlauf
- Batch script
- Zoom support

## Summary
A user requested assistance for an initial test run of Ansys software. The HPC Admin advised the user to attempt the test run independently using a previously created batch script and offered to provide support via Zoom if any issues arise.

## Root Cause
- User needed guidance for the initial test run of Ansys software.

## Solution
- User was advised to attempt the test run independently.
- HPC Admin offered to provide support via Zoom if any issues arise.

## General Learnings
- Encourage users to attempt initial test runs independently.
- Offer support via Zoom for any issues that arise during the test run.
- Ensure users have the necessary batch scripts and are familiar with them.
```
---

### 2022060242002328_STAR-CCM%2B%20POD-Key%20%28LSTM-2022_2023%29%20Lisence%20Design%20Manager.md
# Ticket 2022060242002328

 # HPC Support Ticket: STAR-CCM+ POD-Key License Design Manager

## Keywords
- STAR-CCM+
- POD-Key
- License
- Design Manager
- HPC
- Error Log
- HEEDs
- Response Surface Modelling
- SHERPA

## Summary
A user encountered issues connecting to the Design Manager tool in STAR-CCM+, which replaced the obsolete Optimate tool. The user provided an error log and sought guidance on connecting to the tool on both local and HPC machines.

## Root Cause
- The user was unable to connect to the Design Manager tool in STAR-CCM+.
- The user had developed an in-house open-source code but wanted to explore additional features like HEEDs, Response Surface Modelling, and SHERPA.

## Solution
- The HPC Admin suggested using the command `-licpath 1999@flex.cd-adapco.com:27000@hpclicense1.rrze.uni-erlangen.de` to connect to the Design Manager tool.

## Additional Information
- A new POD-Key was provided for the upcoming STAR-CCM+ license year.
- The license server and port details were unchanged:
  - License server: `flex.cd-adapco.com`
  - Port: `1999`
  - POD-Subnet: `131.188.214.0/23`
- On HPC clusters, users should continue using `-power -podkey $PODKEY`.
- The new license agreement includes access to additional tools like Optimate via a local license server at `27000@hpclicense1.rrze.uni-erlangen.de`.

## Conclusion
The user was advised to use a specific command to connect to the Design Manager tool. The ticket also provided updated license information for STAR-CCM+ and related tools.
---

### 2022092042003011_Abschaltung%20Emmy.md
# Ticket 2022092042003011

 # HPC Support Ticket: Abschaltung Emmy

## Keywords
- Emmy Cluster
- Meggie Cluster
- Aerodynamik Simulationen
- Star-CCM+
- PBS to Sbatch
- Batch-Skripten

## Problem
- **Root Cause**: Emmy Cluster wurde abgeschaltet.
- **User Issue**: Benötigt Ersatzcluster für Aerodynamik Simulationen.
- **Additional Issue**: Schwierigkeiten beim Umstieg von PBS auf Sbatch, insbesondere bei der Umsetzung von Makros für Star-CCM+.

## Solution
- **Ersatzcluster**: Meggie Cluster ([Dokumentation](https://hpc.fau.de/systems-services/documentation-instructions/clusters/meggie-cluster/)).
- **Batch-Skripten für Star-CCM+**: Verfügbar unter [Star-CCM+ Dokumentation](https://hpc.fau.de/systems-services/documentation-instructions/special-applications-and-tips-tricks/star-ccm/).
- **Beispiel-Batchskript für Star-CCM+**: Verfügbar unter [Star-CCM+ Beispielskript](https://hpc.fau.de/systems-services/documentation-instructions/special-applications-and-tips-tricks/star-ccm/#collapse_0).

## Generelles
- **Umstellung**: Von PBS auf Sbatch.
- **Dokumentation**: Nutzer sollten die bereitgestellten Dokumentationen und Beispielskripte verwenden.
- **Kontakt**: Bei weiteren Fragen sollten Nutzer detaillierte Beschreibungen ihrer Probleme an den Support senden.

## Zuständige Personen
- **HPC Admins**: Thomas, Michael Meier, Anna Kahler, Katrin Nusser, Johannes Veh
- **2nd Level Support**: Lacey, Dane (fo36fizy), Kuckuk, Sebastian (sisekuck), Lange, Florian (ow86apyf), Ernst, Dominik (te42kyfo), Mayr, Martin
- **Datacenter Leitung**: Gerhard Wellein
- **Training und Support**: Georg Hager
- **NHR Rechenzeit Support**: Harald Lanig
- **Software und Tools Entwickler**: Jan Eitzinger, Gruber
---

### 2022102442002029_L%C3%83%C2%B6schung%20der%20Ergebnisse%20von%20Starccm%2B%20Simulationen.md
# Ticket 2022102442002029

 # HPC Support Ticket: Deletion of Starccm+ Simulation Results

## Keywords
- Starccm+
- Simulation
- Ergebnisdatei
- Fehler beim Speichern
- IO error writing array data
- Fileserver Probleme
- Netzwerkausfälle

## Problem Description
- User reports that the result file from Starccm+ simulations on Meggie is not being outputted or disappears after being partially computed.

## Root Cause
- The issue is related to errors during the saving process of the simulation results.
- Log files indicate an "IO error writing array data" during the save operation.
- Possible causes include fileserver issues, network timeouts, or potential code errors in the simulation setup.

## Troubleshooting Steps
1. **Specific Details Requested**:
   - Location of the affected files.
   - Job number and script location.

2. **Log File Analysis**:
   - HPC Admin identified IO errors in the log files for specific jobs (e.g., 2021283, 2021284, 2021285).

3. **Potential System Issues**:
   - Recent problems with the fileserver were noted, which could have caused timeouts during data writing.

## Solution
- User was advised to retry the simulations after a scheduled downtime to see if the issue persists.
- If the problem continues, the user should report the affected job IDs for further investigation.
- Network issues were also identified as a potential cause based on similar problems experienced by other users.

## Conclusion
- The issue is intermittent and may be related to system-level problems such as fileserver issues or network outages.
- Further monitoring and reporting of affected job IDs are necessary to pinpoint the exact cause.

## Follow-up
- User reported that the issue still occurs but less frequently.
- HPC Admin requested the user to provide job IDs for further analysis if the problem persists.

## Additional Notes
- No changes were made to the simulation setup between successful and failed runs, indicating a potential system-level issue.
- The problem may require ongoing monitoring and potential system-level fixes to resolve completely.
---

### 2018072642001237_ISSUE%20REGARDING%20OPENING%20STARCCM%2B%20GUI%2012.04%20ON%20EMMY%20FRONT%20NODE.md
# Ticket 2018072642001237

 # HPC Support Ticket: Issue with Opening STAR-CCM+ GUI on Emmy Front Node

## Keywords
- STAR-CCM+
- License checkout failure
- POD key
- Emmy front node
- HPC cluster
- Environment variable

## Problem Description
- User unable to load simulation files using STAR-CCM+ on Emmy front node.
- Error message: "license checkout failure" or "Failed to secure 1ccp license."
- POD key verified and working on the local machine but not on the HPC cluster.

## Root Cause
- POD keys for the local subnet of the chair do not work on the HPC clusters and vice versa.

## Solution
- Use the POD key available in the environment variable `$PODKEY` after loading the `star-ccm+` module on the HPC clusters.

## General Learning
- Ensure that the correct POD key is used for the specific environment (local machine vs. HPC cluster).
- Load the appropriate module and use the environment variable provided for the POD key on HPC clusters.

## Actions Taken
- HPC Admin advised the user to use the POD key available in the environment variable `$PODKEY` after loading the `star-ccm+` module.

## Follow-up
- Verify that the user can successfully load simulation files using STAR-CCM+ on the Emmy front node with the correct POD key.
---

### 2018052442000316_HPC%20ansys.md
# Ticket 2018052442000316

 # HPC Support Ticket: ANSYS Licensing and Hardware Specifications

## Keywords
- ANSYS
- HPC Licenses
- Workstation
- Research License
- CFD Jobs
- Taktfrequenz
- Emmy-Cluster
- RRZE

## Summary
A user inquires about the procedure for running CFD jobs on the HPC system, specifically regarding ANSYS HPC licenses and hardware specifications.

## Root Cause
- User needs clarification on ANSYS HPC license requirements for both HPC systems and workstations.
- User is considering investing in a more powerful workstation to potentially save on HPC license costs.
- User seeks information on the booking process for HPC licenses and the clock speed of the HPC system's cores.

## Solution
- **ANSYS License Requirements**: Each ANSYS Research base license allows the use of up to 16 cores for CFX/Fluent jobs without additional licenses. Additional cores require one HPC license per core.
- **Workstation Licenses**: The same license pool is used for both HPC systems and workstations, with no need for a specific allocation.
- **Booking Process**: Licenses are booked according to the general rules of software@rrze.
- **Hardware Specifications**: The Emmy-Cluster is suitable for parallel ANSYS-CFX/Fluent calculations. Each node has 20 physical cores with a base clock speed of 2.2 GHz, capable of turbo boosting up to 2.6 GHz.

## General Learnings
- Understanding ANSYS license requirements for different setups.
- Importance of hardware specifications in decision-making for HPC usage.
- Booking process for HPC licenses and the flexibility of using the same license pool for different systems.

## Next Steps
- User should evaluate the cost-benefit of investing in a more powerful workstation versus using the HPC system.
- User should follow the general booking rules for software@rrze for HPC licenses.

## Additional Notes
- The Emmy-Cluster is recommended for parallel ANSYS-CFX/Fluent calculations due to its hardware specifications.
- The user can contact HPC Admins for further assistance if needed.
---

### 2020080342001621_StarCCM%202020.1-r8%20auf%20Meggie.md
# Ticket 2020080342001621

 # HPC Support Ticket: StarCCM 2020.1-r8 auf Meggie

## Keywords
- StarCCM+
- Version Upgrade
- Double Precision (r8)
- Installation Request
- Cluster Meggie

## Summary
A user requested an upgrade from StarCCM+ 13.xxx to a newer version, specifically inquiring about double precision support (r8) for StarCCM+ 2020.1 on the Meggie cluster.

## Problem
- User needed to upgrade to a newer version of StarCCM+.
- User required double precision support (r8) for compatibility with existing files.
- Local admin unavailable due to vacation, preventing local installation.

## Solution
- HPC Admin confirmed the availability of StarCCM+ 2020.2 and 2020.2-r8 on Meggie.
- User requested installation of StarCCM+ 2020.1-r8 due to compatibility issues with 2020.2 files.
- HPC Admin installed StarCCM+ 2020.1-r8 on Meggie to meet the user's requirements.

## Conclusion
The installation of StarCCM+ 2020.1-r8 on Meggie resolved the user's compatibility issues, allowing them to proceed with their work without waiting for local installation capabilities.

## Lessons Learned
- Always check for version compatibility when upgrading software.
- Communicate with HPC Admins for installation requests when local admin support is unavailable.
- Ensure that necessary software versions are available on the cluster to support user needs.
---

### 2023112042003399_StarCCM%2B%20on%20cluster...md
# Ticket 2023112042003399

 ```markdown
# HPC Support Ticket: StarCCM+ on Cluster

## Subject
StarCCM+ on cluster doesn't work and aborts with error code 8. Seems like a PoD issue?

## User Report
- **Issue**: StarCCM+ aborts with error code 8.
- **Error Snippet**:
  ```
  This version of the code requires license version 2022.06 or greater.
  Licensing problem: Unable to find a path to any license file or license server.
  Please create the CDLMD_LICENSE_FILE environment variable and point it to the license server.
  FLEXnet error: (-16,287)
  License build date: 04 February 2022
  This version of the code requires license version 2022.06 or greater.
  Checking license file: 1999@131.188.3.151
  Unable to list features for license file 1999@131.188.3.151.
  Checking license file: 1999@hpclicense1.rrze.uni-erlangen.de
  Unable to list features for license file 1999@hpclicense1.rrze.uni-erlangen.de.
  Checking license file: 1999@grid.rrze.uni-erlangen.de
  Unable to list features for license file 1999@grid.rrze.uni-erlangen.de.
  Checking license file: 1999@flex.cd-adapco.com
  Unable to list features for license file 1999@flex.cd-adapco.com.
  Unable to check out feature 'server_id', line 6417:
  FLEXnet error: (-139,10013)
  MPI_ABORT was invoked on rank 0 in communicator MPI_COMM_WORLD with errorcode 8.
  NOTE: invoking MPI_ABORT causes Open MPI to kill all MPI processes.
  You may or may not see output from other processes, depending on exactly when Open MPI kills them.
  ```

## HPC Admin Response
- **Initial Response**:
  - Asked if StarCCM+ with PoD works locally.
  - Informed that all StarCCM+ PoD license servers are down since the weekend.
  - Opened a ticket with Siemens but no response yet.
  - Installed StarCCM+ 2310 on Fritz, Meggie, and Woody.

- **Follow-up**:
  - Confirmed that PoD works locally.
  - Provided license server status checks showing issues with Siemens' servers.
  - Later confirmed that Siemens' PoD license servers are responding normally again.

## Root Cause
- **Licensing Issue**: Unable to find a path to any license file or license server.
- **Server Down**: Siemens' PoD license servers were down.

## Solution
- **Wait for Siemens**: Wait for Siemens to resolve the license server issue.
- **Installation**: StarCCM+ 2310 installed on Fritz, Meggie, and Woody.

## Keywords
- StarCCM+
- PoD
- License Server
- FLEXnet
- MPI_ABORT
- Siemens
- Error Code 8
```
---

### 2023012642001167_Lizenzprobleme.md
# Ticket 2023012642001167

 # HPC Support Ticket: Lizenzprobleme

## Keywords
- Starccm Simulation
- Meggie Cluster
- License Error
- ccmppower
- ccmppowerplus
- HPC Account Expiration
- POD-Lizenzserver

## Problem Description
- User encountered license errors while running Starccm simulations on the Meggie Cluster.
- Error messages:
  - Asked for 1 license of ccmppower and got 0
  - Asked for 1 license of ccmppowerplus and got 0

## Root Cause
- Potential expiration of the user's HPC account.
- Issues with Siemens POD-Lizenzserver, with only one out of four servers responding.

## Solution
- Verify the user's HPC account status.
- Wait for Siemens to resolve the POD-Lizenzserver issues.

## General Learnings
- License errors can be caused by account expiration or external licensing server issues.
- Always check account status and external dependencies when troubleshooting license errors.

## Next Steps
- If similar issues arise, check the user's account status and consult with the software vendor regarding licensing server issues.
---

### 2021041242005124_High-Octane%20Motorsports.md
# Ticket 2021041242005124

 ```markdown
# HPC-Support Ticket: High-Octane Motorsports

## Keywords
- CFD Simulation
- StarCCM+
- Connection Timeout
- IP Address Change
- Memoryhog Cluster
- License Server

## Summary
A user encountered a connection timeout error when starting the StarCCM+ server on the memoryhog cluster. The error message indicated a `java.net.ConnectException: Connection timed out`.

## Problem Description
- **Error Message:** `Server::start -host memoryhog.rrze.uni-erlangen.de:47827 error: java.net.ConnectException: Connection timed out (Connection timed out)`
- **User's Setup:** The user was running CFD simulations using StarCCM+ on the memoryhog cluster to avoid blocking nodes on another cluster.
- **Root Cause:** The IP address of the memoryhog cluster had recently changed, which might have caused issues with cached addresses or network configurations.

## Troubleshooting Steps
1. **Check for Changes in Scripts:** The user confirmed that no changes were made to the scripts or commands used to start the server.
2. **Test with Older Module:** The user tested with both StarCCM+ 2021.1 and 2020.3 modules, but the issue persisted.
3. **IP Address Change:** The HPC Admins noted that the IP address of the memoryhog cluster had changed recently, which could be causing the issue.

## Solution
- **Configuration Issue:** The HPC Admins identified a configuration problem with the node after the IP address change.
- **Resolution:** The configuration issue was resolved, and the user was informed that the StarCCM+ server should now start without issues.

## Conclusion
The problem was due to a configuration issue after the IP address change of the memoryhog cluster. Resolving the configuration issue fixed the connection timeout error.

## Lessons Learned
- **IP Address Changes:** Changes in IP addresses can lead to connectivity issues, especially if old addresses are cached.
- **Configuration Checks:** Always check for configuration issues after any network changes.
- **User Communication:** Keep users informed about any network changes that might affect their workflows.
```
---

### 2020112142000038_Star-ccm%2B%20on%20remote%20cip%20pool.md
# Ticket 2020112142000038

 # HPC Support Ticket: Star-ccm+ on Remote CIP Pool

## Keywords
- Star-ccm+
- Remote CIP Pool
- License Availability
- HPC Services

## Summary
A user requested guidance on using Star-ccm+ on a remote CIP pool.

## Root Cause
- The user was unaware that the HPC Services do not operate any CIP pool.
- The user was also unaware that the STAR-CCM+ license is held by a few chairs only and is not generally available.

## Solution
- Inform the user that the HPC Services do not operate any CIP pool.
- Explain that the STAR-CCM+ license is limited to specific chairs and is not generally available.
- Advise the user to contact the relevant chair or department that holds the STAR-CCM+ license for further assistance.

## General Learnings
- Ensure users are aware of the specific resources and licenses available through HPC Services.
- Clarify the limitations and availability of software licenses to users.
- Provide guidance on whom to contact for specialized software licenses not managed by HPC Services.

## Next Steps
- Update the knowledge base with information about the availability of STAR-CCM+ licenses.
- Ensure that users are informed about the resources and services provided by HPC Services.
---

### 2022072042002104_Star-ccm%2B%20run%20script%20question.md
# Ticket 2022072042002104

 # HPC Support Ticket: Star-ccm+ Run Script Issue

## Keywords
- Star-ccm+
- Run script
- Version compatibility
- File naming
- Licensing issues

## Summary
A user encountered issues running Star-ccm+ simulations after installing a new version and using a new run script. The problems affected both new and old simulations.

## Root Cause
1. **File Naming Issue**: The simulation file name contained a space, causing the error "Cannot open file: Both_Curves_Rev2_Re10000_Suja_20220718.sim".
2. **Licensing Problem**: The simulation was aborted due to licensing issues, as indicated in the output file "Flat_Re=10000_betterresolution.e1658985".

## Solution
1. **File Naming**: Rename the simulation file to remove spaces.
2. **Licensing**: The HPC Admin will investigate and resolve the licensing server issues.

## General Learnings
- Ensure simulation file names do not contain spaces.
- Check output files for error messages to diagnose issues.
- Licensing problems can cause simulation aborts and may require admin intervention.

## Follow-up
- The HPC Admin will update the user once the licensing issue is resolved.
- The user should retry the simulations with corrected file names.
---

### 2021061842000169_Mathematica%20auf%20den%20HPC-System%20_%20Anfrage%20der%20Gruppe%20von%20Prof.%20Hartmann%20%28mpt2.md
# Ticket 2021061842000169

 # HPC-Support Ticket: Mathematica auf den HPC-System / Anfrage der Gruppe von Prof. Hartmann (mpt2)

## Problem
- Die Gruppe von Prof. Hartmann möchte Mathematica auf den HPC-Systemen nutzen.
- Der Lizenzserver ist nur auf einem Teil der HPC-Subnetze erreichbar.
- Es gibt Probleme mit der IPv6-Konfiguration.
- Mathematica-Aktivierung scheitert mit Fehler 84.

## Details
- **Betroffene Subnetze:**
  - 10.28.48.0/23 (TinyX/Slurm)
  - 2001:638:a000:3948::0/64
  - 10.28.24.0/21 (Meggie)
  - 2001:638:a000:3924::0/64
  - 10.188.82.0/23 (Woody)
  - 10.28.8.0/22 (Emmy)
  - 10.188.5.0/24 (TinyX/PBS)

## Lösung
- **Firewall-Konfiguration:**
  - Die Firewall wurde so konfiguriert, dass die oben genannten Subnetze freigeschaltet wurden.
  - IPv4-Subnetze: 10.188.0.0/16 und 10.28.0.0/16 sollten ausreichend sein.
  - IPv6-Subnetze wurden ebenfalls freigeschaltet.

- **Lizenzserver:**
  - Der Lizenzserver ist unter der IP 131.188.3.32 erreichbar.
  - Der DNS-Name "license2" funktioniert nicht auf den Clusternodes, da die IPv6-Adresse versucht wird, der Lizenzserver darauf aber nicht antwortet.

- **Mathematica-Aktivierung:**
  - Bei der Aktivierung von Mathematica sollte die IP 131.188.3.32 anstelle des DNS-Namens "license2" verwendet werden.
  - Fehler 84 könnte auf zusätzliche Anforderungen von MathLM hinweisen.

## Weitere Schritte
- **Lokale Installation:**
  - Die Installationsdateien für Mathematica können über die Kontaktperson am Lehrstuhl und die LSD-Website bezogen werden.
  - Bei Problemen sollte die Software-Gruppe kontaktiert werden (software@rrze.uni-erlangen.de).

## Schlussfolgerung
- Die Nutzung von Mathematica auf den HPC-Systemen ist möglich, erfordert jedoch spezifische Konfigurationen und Anpassungen.
- Die Verwendung der IP-Adresse des Lizenzservers anstelle des DNS-Namens ist notwendig, um IPv6-Probleme zu vermeiden.
- Die Lizenzierung und Aktivierung von Mathematica kann komplex sein und erfordert möglicherweise zusätzliche Schritte.

## Keywords
- Mathematica
- Lizenzserver
- Firewall
- IPv6
- HPC-Systeme
- Aktivierung
- Fehler 84
- LSD-Download
- Subnetze
- DNS-Name
- IP-Adresse
- Software-Gruppe
- Kontaktperson
- Installationsdateien
- Clusternodes
- IPv4
- IPv6-Probleme
- MathLM
- Lokale Installation
- Lizenzinformation
- Lizenzanfrage
- Software-Kollegen
- HPC-Queue
- Ticket
- HPC-Support
- HPC-Services
- RRZE
- FAU
- NHR@FAU
- Regionales Rechenzentrum Erlangen
- Friedrich-Alexander-Universität Erlangen-Nürnberg
- Zentrum für Nationales Hochleistungsrechnen Erlangen
- HPC Admin
- 2nd Level Support team
- Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support
- Applications for Grants
- Software and Tools developer
- Head of HPC Systems & Services
- Head of the Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support and Applications for Grants
- Software and Tools developer
- HPC Admin
- 2nd Level Support team
- Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support
- Applications for Grants
- Software and Tools developer
- Head of HPC Systems & Services
- Head of the Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support and Applications for Grants
- Software and Tools developer
- HPC Admin
- 2nd Level Support team
- Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support
- Applications for Grants
- Software and Tools developer
- Head of HPC Systems & Services
- Head of the Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support and Applications for Grants
- Software and Tools developer
- HPC Admin
- 2nd Level Support team
- Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support
- Applications for Grants
- Software and Tools developer
- Head of HPC Systems & Services
- Head of the Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support and Applications for Grants
- Software and Tools developer
- HPC Admin
- 2nd Level Support team
- Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support
- Applications for Grants
- Software and Tools developer
- Head of HPC Systems & Services
- Head of the Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support and Applications for Grants
- Software and Tools developer
- HPC Admin
- 2nd Level Support team
- Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support
- Applications for Grants
- Software and Tools developer
- Head of HPC Systems & Services
- Head of the Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support and Applications for Grants
- Software and Tools developer
- HPC Admin
- 2nd Level Support team
- Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support
- Applications for Grants
- Software and Tools developer
- Head of HPC Systems & Services
- Head of the Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support and Applications for Grants
- Software and Tools developer
- HPC Admin
- 2nd Level Support team
- Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support
- Applications for Grants
- Software and Tools developer
- Head of HPC Systems & Services
- Head of the Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support and Applications for Grants
- Software and Tools developer
- HPC Admin
- 2nd Level Support team
- Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support
- Applications for Grants
- Software and Tools developer
- Head of HPC Systems & Services
- Head of the Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support and Applications for Grants
- Software and Tools developer
- HPC Admin
- 2nd Level Support team
- Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support
- Applications for Grants
- Software and Tools developer
- Head of HPC Systems & Services
- Head of the Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support and Applications for Grants
- Software and Tools developer
- HPC Admin
- 2nd Level Support team
- Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support
- Applications for Grants
- Software and Tools developer
- Head of HPC Systems & Services
- Head of the Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support and Applications for Grants
- Software and Tools developer
- HPC Admin
- 2nd Level Support team
- Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support
- Applications for Grants
- Software and Tools developer
- Head of HPC Systems & Services
- Head of the Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support and Applications for Grants
- Software and Tools developer
- HPC Admin
- 2nd Level Support team
- Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support
- Applications for Grants
- Software and Tools developer
- Head of HPC Systems & Services
- Head of the Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support and Applications for Grants
- Software and Tools developer
- HPC Admin
- 2nd Level Support team
- Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support
- Applications for Grants
- Software and Tools developer
- Head of HPC Systems & Services
- Head of the Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support and Applications for Grants
- Software and Tools developer
- HPC Admin
- 2nd Level Support team
- Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support
- Applications for Grants
- Software and Tools developer
- Head of HPC Systems & Services
- Head of the Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support and Applications for Grants
- Software and Tools developer
- HPC Admin
- 2nd Level Support team
- Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support
- Applications for Grants
- Software and Tools developer
- Head of HPC Systems & Services
- Head of the Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support and Applications for Grants
- Software and Tools developer
- HPC Admin
- 2nd Level Support team
- Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support
- Applications for Grants
- Software and Tools developer
- Head of HPC Systems & Services
- Head of the Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support and Applications for Grants
- Software and Tools developer
- HPC Admin
- 2nd Level Support team
- Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support
- Applications for Grants
- Software and Tools developer
- Head of HPC Systems & Services
- Head of the Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support and Applications for Grants
- Software and Tools developer
- HPC Admin
- 2nd Level Support team
- Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support
- Applications for Grants
- Software and Tools developer
- Head of HPC Systems & Services
- Head of the Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support and Applications for Grants
- Software and Tools developer
- HPC Admin
- 2nd Level Support team
- Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support
- Applications for Grants
- Software and Tools developer
- Head of HPC Systems & Services
- Head of the Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support and Applications for Grants
- Software and Tools developer
- HPC Admin
- 2nd Level Support team
- Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support
- Applications for Grants
- Software and Tools developer
- Head of HPC Systems & Services
- Head of the Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support and Applications for Grants
- Software and Tools developer
- HPC Admin
- 2nd Level Support team
- Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support
- Applications for Grants
- Software and Tools developer
- Head of HPC Systems & Services
- Head of the Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support and Applications for Grants
- Software and Tools developer
- HPC Admin
- 2nd Level Support team
- Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support
- Applications for Grants
- Software and Tools developer
- Head of HPC Systems & Services
- Head of the Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support and Applications for Grants
- Software and Tools developer
- HPC Admin
- 2nd Level Support team
- Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support
- Applications for Grants
- Software and Tools developer
- Head of HPC Systems & Services
- Head of the Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support and Applications for Grants
- Software and Tools developer
- HPC Admin
- 2nd Level Support team
- Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support
- Applications for Grants
- Software and Tools developer
- Head of HPC Systems & Services
- Head of the Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support and Applications for Grants
- Software and Tools developer
- HPC Admin
- 2nd Level Support team
- Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support
- Applications for Grants
- Software and Tools developer
- Head of HPC Systems & Services
- Head of the Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support and Applications for Grants
- Software and Tools developer
- HPC Admin
- 2nd Level Support team
- Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support
- Applications for Grants
- Software and Tools developer
- Head of HPC Systems & Services
- Head of the Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support and Applications for Grants
- Software and Tools developer
- HPC Admin
- 2nd Level Support team
- Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support
- Applications for Grants
- Software and Tools developer
- Head of HPC Systems & Services
- Head of the Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support and Applications for Grants
- Software and Tools developer
- HPC Admin
- 2nd Level Support team
- Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support
- Applications for Grants
- Software and Tools developer
- Head of HPC Systems & Services
- Head of the Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support and Applications for Grants
- Software and Tools developer
- HPC Admin
- 2nd Level Support team
- Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support
- Applications for Grants
- Software and Tools developer
- Head of HPC Systems & Services
- Head of the Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support and Applications for Grants
- Software and Tools developer
- HPC Admin
- 2nd Level Support team
- Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support
- Applications for Grants
- Software and Tools developer
- Head of HPC Systems & Services
- Head of the Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support and Applications for Grants
- Software and Tools developer
- HPC Admin
- 2nd Level Support team
- Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support
- Applications for Grants
- Software and Tools developer
- Head of HPC Systems & Services
- Head of the Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support and Applications for Grants
- Software and Tools developer
- HPC Admin
- 2nd Level Support team
- Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support
- Applications for Grants
- Software and Tools developer
- Head of HPC Systems & Services
- Head of the Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support and Applications for Grants
- Software and Tools developer
- HPC Admin
- 2nd Level Support team
- Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support
- Applications for Grants
- Software and Tools developer
- Head of HPC Systems & Services
- Head of the Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support and Applications for Grants
- Software and Tools developer
- HPC Admin
- 2nd Level Support team
- Datacenter
-
---

### 2022110842003333_Question%20on%20Meggie.md
# Ticket 2022110842003333

 # HPC Support Ticket: STAR-CCM+ Simulation Issue on Meggie1

## Keywords
- STAR-CCM+
- Meggie1
- Emmy
- Floating point error
- Non-finite residual
- X-momentum
- SegregatedFlowSolver
- Simulation abort

## Problem Description
- User encountered a floating point error while running STAR-CCM+ simulations on Meggie1, leading to abortion of the simulation.
- Error message indicated a non-finite residual (X-momentum) added by `star.segregatedflow.SegregatedFlowSolver`.
- Same simulation ran without issues on Emmy.

## Root Cause
- Unclear from the ticket; could be related to differences in hardware, software environment, or configuration between Emmy and Meggie1.

## Troubleshooting Steps
- User attempted to resolve the issue by changing mesh and time-step, but the problem persisted.
- HPC Admins could not provide specific advice as they were not familiar with STAR-CCM+.

## Solution
- No solution found within the ticket conversation.
- HPC Admin suggested reaching out to Siemens support for further assistance.

## General Learnings
- Floating point errors in simulations can be caused by various factors such as overflow, underflow, or division by zero.
- Differences in HPC systems can lead to variations in simulation behavior.
- For specialized software issues, it may be necessary to consult the software vendor's support.

## Next Steps for Similar Issues
- Check for hardware or software environment differences between HPC systems.
- Consult software documentation or vendor support for specific error messages.
- Review simulation inputs and configurations for potential issues.
---

### 2022033142000049_HPC%20Star-CCM%2B-r8%20Modul.md
# Ticket 2022033142000049

 ```markdown
# HPC Support Ticket: Star-CCM+ Module Request

## Keywords
- Star-CCM+
- Double Precision Module
- Serial Networking
- Large Grids
- Emmy Cluster

## Summary
A user requires a "double precision" module for Star-CCM+ (version 2021.1.1.-r8 or newer) for their master's thesis. Additionally, the user has concerns about running serial networking tasks on the Emmy cluster due to large grid sizes (2-5 million cells).

## Root Cause
- User needs a specific module for their research.
- User is unsure about the policy regarding serial networking on Emmy.

## Solution
- **Module Availability**: HPC Admin informs the user that Star-CCM+/2021.3.1-r8 is available on Emmy.
- **Serial Networking**: HPC Admin advises the user that running serial networking tasks on Emmy is acceptable.

## General Learnings
- Specific software modules may be available upon request.
- Serial networking tasks, even with large grids, are permissible on the Emmy cluster.
- Users should check with HPC support for the availability of specific software versions and modules.

## Actions Taken
- HPC Admin provided information about the available Star-CCM+ version.
- HPC Admin clarified the policy regarding serial networking on Emmy.

## Follow-Up
- User thanked the HPC Admin for the quick response and clarification.
```
---

### 2022091542000925_Comsol%20Multiphysics%20Installation.md
# Ticket 2022091542000925

 # Comsol Multiphysics Installation

## Keywords
- Comsol Multiphysics
- Installation
- HPC Cluster
- Woody
- TinyFAT
- Software Version
- GUI Issues

## Problem
- Comsol Multiphysics not listed among available software on Woody and TinyFAT.
- User requests installation of Comsol Multiphysics, mentioning they have a license.
- User later requests an update to Comsol 6.1.

## Root Cause
- Comsol Multiphysics was not initially installed on the HPC clusters.
- User needed the latest version of Comsol for their work.

## Solution
- HPC Admins installed Comsol 6.0 on Woody-NG and Woody3 (TinyFAT).
- GUI issues were noted on Woody-NG, but the user did not require the GUI for simulations.
- HPC Admins later installed Comsol 6.1 on TinyFAT and Woody, but could not test the installation due to lack of Comsol knowledge.

## General Learnings
- Users may request specific software installations if they have the necessary licenses.
- Software updates should be handled promptly to meet user requirements.
- GUI issues may arise during software installations on HPC clusters.
- Communication with users is essential to understand their specific needs and provide appropriate solutions.
---

### 2018061342000933_Lizenzserver%20Probleme%3F.md
# Ticket 2018061342000933

 # HPC-Support Ticket: Lizenzserver Probleme

## Keywords
- Lizenzserver
- Intel-Tools
- ifort
- Compiler
- Lizenzvertrag
- Kontingent

## Problem
- User reported slow response times for `ifort -V` command on multiple systems (meggie, emmy).
- Intermittent performance issues with the command.

## Root Cause
- Limited number of licenses (5) for Intel-Tools.
- High demand for C/Fortran-Compiler licenses causing delays.

## Solution
- No immediate solution provided.
- Potential increase in license count with a new license agreement by December.

## General Learnings
- Limited licenses can cause performance issues and delays in command execution.
- Monitoring license usage and planning for increased capacity can help mitigate such issues.
- Communication about future license increases can manage user expectations.

## Next Steps
- Monitor license usage and consider increasing the number of licenses if feasible.
- Inform users about potential delays during high demand periods.

---

This documentation can be used to address similar issues related to license server problems and slow command execution due to limited licenses.
---

### 42303507_star-ccm%2B%20version%209.04.011.md
# Ticket 42303507

 ```markdown
# HPC-Support Ticket: star-ccm+ Version 9.04.011

## Summary
User requested the installation of the latest star-ccm+ version (9.04.011) on the woody cluster due to issues with starting simulations. The current version (9.04.009) had a bug affecting a critical function.

## Keywords
- star-ccm+
- version 9.04.011
- woody cluster
- simulation issues
- bug fix

## Problem
- **Root Cause**: Bug in star-ccm+ version 9.04.009 preventing simulations from starting.
- **Impact**: Simulations could not be started on the cluster.

## Solution
- **Action Taken**: HPC Admins installed the latest star-ccm+ version (9.04.011) on all clusters.
- **Outcome**: The issue was resolved, and simulations could be started successfully.

## Lessons Learned
- Regular updates to software versions can resolve bugs and improve functionality.
- Communication between users and HPC Admins is crucial for identifying and resolving issues promptly.

## Follow-up
- Users should test the new version to ensure the bug is resolved.
- HPC Admins should monitor for any further issues related to the new version.
```
---

### 2020102842003622_Aktualisierung%20STAR-CCM%2B.md
# Ticket 2020102842003622

 ```markdown
# HPC-Support Ticket: Update STAR-CCM+

## Subject
Aktualisierung STAR-CCM+

## Keywords
- STAR-CCM+
- Version 2020.3
- Update
- Software Installation

## Problem
- User requested an update to the latest version of STAR-CCM+ (2020.3).

## Root Cause
- The user needed the latest version of STAR-CCM+ for their project.

## Solution
- HPC Admin confirmed the availability of STAR-CCM+ 2020.3.

## Conversation Summary
- User inquired about updating STAR-CCM+ to the latest version.
- HPC Admin responded that the new version (2020.3) is now available.

## What Can Be Learned
- Users may request updates to specific software versions.
- HPC Admins should confirm the availability of the requested software version.
- Communication between users and HPC Admins is essential for ensuring that the required software versions are available.
```
---

### 2023091542002314_Lizenzproblem%20Star-CCM.md
# Ticket 2023091542002314

 # HPC Support Ticket: Lizenzproblem Star-CCM

## Keywords
- Star-CCM
- Lizenzproblem
- Lizenzserver
- Siemens
- Erreichbarkeit

## Problem
- **User**: Unable to access Star-CCM via the cluster since the morning.
- **Version**: 2302
- **Error Message**: Detailed in the attachment.

## Root Cause
- Possible issue with the reachability of the Siemens license server.

## Solution
- **HPC Admin**: The issue could not be reproduced, suggesting it was temporary.
- **User**: The problem resolved itself the next day.

## Learnings
- The Siemens license server may occasionally be unreachable, causing temporary access issues to Star-CCM.
- Users cannot do much except wait if the issue is due to the license server's reachability.
- Most instances of server unreachability resolve quickly.

## Next Steps
- If the problem reoccurs, users should wait as the license server is outside the HPC admin's control.
- Monitor for any patterns or frequent occurrences of server unreachability.
---

### 2021072642003872_Lizenzprobleme%20beim%20Zugriff%20auf%20Star-sim-files%20via%20noMachine%20auf%20Meggie.md
# Ticket 2021072642003872

 ```markdown
# HPC Support Ticket: Lizenzprobleme beim Zugriff auf Star-sim-files via noMachine auf Meggie

## Keywords
- Lizenzproblem
- Star-CCM+
- NoMachine
- Meggie
- POD-Keys
- HPC-Frontends
- `module show star-ccm+`
- PODKEY Umgebungsvariable

## Problem
- **User**: Lizenzproblem beim Zugriff auf Star-CCM+ Dateien via NoMachine auf Meggie.
- **Root Cause**: Neue POD-Keys seit 1.6.

## Lösung
- **HPC Admin**: Neue POD-Keys seit 1.6.
- **Schritte zur Lösung**:
  1. Aktuellen IPAT-Cluster-POD-Key auf einem der HPC-Frontends mit `module show star-ccm+` anzeigen.
  2. PODKEY Umgebungsvariable auf der Kommandozeile verwenden.

## Allgemeines
- POD-Keys müssen manuell aktualisiert werden, wenn sie ablaufen.
- Die Umgebungsvariable PODKEY steht auf der Kommandozeile zur Verfügung.
```
---

### 2019102842001351_Module%20Star-ccm%2B.md
# Ticket 2019102842001351

 # HPC Support Ticket: Module Star-ccm+

## Keywords
- Star-ccm+
- Module Error
- Directory Structure
- License Settings
- HPC System
- Modulefile

## Summary
The user encountered issues with loading the Star-ccm+ module on the HPC system, specifically with version 13.06.012. The error indicated a problem with the directory structure and missing files. The user also inquired about the availability of the latest version of Star-ccm+.

## Root Cause
- Directory structure issue causing module load errors.
- Missing modulefile for the latest version of Star-ccm+.

## Solution
- HPC Admins fixed the directory structure issue for version 13.06.012.
- The latest version of Star-ccm+ (2019.2) was confirmed to be available on all HPC systems.

## Lessons Learned
- Ensure that the directory structure for software modules is correctly set up to avoid load errors.
- Regularly update and verify the availability of the latest software versions on the HPC system.
- Communicate effectively with users to address their concerns and provide timely solutions.

## Follow-up Actions
- Verify that the latest version of Star-ccm+ is correctly installed and accessible.
- Monitor for any further issues related to module loading and directory structure.
- Provide clear documentation on how to load and use software modules on the HPC system.
---

### 2019112242000833_SPEC%20Benchmark%20Suites.md
# Ticket 2019112242000833

 ```markdown
# HPC-Support Ticket: SPEC Benchmark Suites

## Keywords
- SPEC Benchmark Suite
- Licensing
- HPC Services
- RRZE
- FAU Erlangen-Nürnberg
- SPEC CPU 2006
- SPEC OMP 2012
- SPEC CPU 2017
- HPG Suite
- SERT Suite
- MPI2007 Suite

## Summary
- **User Inquiry:** The user inquired about the availability of SPEC Benchmark Suite licenses at the university, specifically whether the HPC team had any relevant licenses.
- **HPC Admin Response:** The HPC team confirmed they had licenses for SPEC CPU 2006 and SPEC OMP 2012 but not for the current SPEC CPU 2017 suite. They suggested checking with other departments (INF3 Prof. Fey or INF2 Prof. Phillipsen) for additional licenses.
- **User Follow-up:** The user confirmed with SPEC directly that the university only had the licenses mentioned by the HPC team. The user also applied for the HPG Suite, which is available for free for academic purposes.
- **Additional Licenses:** The user mentioned that additional SPEC suites (SERT and CPU Suite) were acquired through the SFB Invasic.
- **License Sharing:** The user confirmed that the licenses were valid for the entire university and offered to share the suites via an HTTP share or USB stick.
- **HPC Admin Assistance:** The HPC team provided guidance on using the university's SSH access and storage for sharing the SPEC suites.

## Root Cause
- The user needed to verify the availability of SPEC Benchmark Suite licenses at the university to avoid redundant purchases.

## Solution
- The HPC team confirmed the available licenses and suggested additional sources for verification.
- The user applied for and received the HPG Suite for free.
- The user shared the acquired suites with the HPC team for broader access within the university.

## General Learnings
- Always check for existing licenses within the institution before making new purchases.
- Some SPEC Benchmark Suites are available for free for academic purposes.
- Collaboration between departments can help in sharing resources and avoiding redundant acquisitions.
```
---

### 2024020542003281_Ansys%20HPC%20Nutzung.md
# Ticket 2024020542003281

 # HPC-Support Ticket: Ansys HPC Nutzung

## Problem
- User has purchased Ansys HPC Research License but is unsure about its functionality and how to generate the required input file for simulations.
- User needs assistance with setting up and running Ansys simulations on the HPC cluster.

## Key Points Learned
- **Licensing**: The Ansys Multiphysics Research License includes 4 HPC licenses for 4 cores, which should be sufficient for initial tests on the Woody nodes.
- **Input File**: The input file contains geometry and material parameters and can be exported from an existing Workbench project. It does not need to be written manually.
- **Remote Solver Manager**: Not configured on the clusters and cannot be used. Manual process is required to start simulations.
- **File Transfer**: MobaXTerm or WinSCP can be used to transfer files to the cluster. Documentation for WinSCP is available [here](https://doc.nhr.fau.de/data/copying/#winscp).
- **Job Submission**: Use `sbatch <name_des_batch_skripts>` to submit jobs. Check job status with `squeue` and look for output files for more information.
- **Private Key for WinSCP**: Required for authentication. Users should have their own HPC accounts, as account sharing is not allowed.

## Steps Taken
1. **Licensing**: Clarified that the Ansys Multiphysics Research License includes 4 HPC licenses for 4 cores.
2. **Input File**: Provided links to resources for generating and understanding the input file:
   - [Ansys Workbench User Guide](https://faubox.rrze.uni-erlangen.de/getlink/fieKTuNxHpJsVv1AE38k8/)
   - [Ansys Forum](https://forum.ansys.com/)
   - [Ansys APDL Scripting Course](https://courses.ansys.com/index.php/courses/intro-to-ansys-mechanical-apdl-scripting/)
3. **Remote Solver Manager**: Informed the user that it is not configured on the clusters and provided guidance on the manual process.
4. **File Transfer**: Recommended using MobaXTerm or WinSCP for file transfer and provided documentation links.
5. **Job Submission**: Explained how to submit jobs using `sbatch` and check job status with `squeue`.
6. **Private Key for WinSCP**: Advised the user to obtain a private key for authentication and to apply for their own HPC account.

## Solution
- The user should follow the manual process to start simulations, using MobaXTerm or WinSCP for file transfer and `sbatch` for job submission.
- The user should generate the input file from their existing Workbench project and refer to the provided resources for guidance.
- The user should attend the monthly HPC system introduction session for a comprehensive overview of the required steps.

## Next Steps
- The user will attend the monthly HPC system introduction session and follow the manual process for running simulations.
- The user will generate the input file from their Workbench project and transfer it to the cluster using MobaXTerm or WinSCP.
- The user will submit jobs using `sbatch` and check job status with `squeue`.

## Additional Resources
- [Monthly HPC System Introduction Session](https://fau.zoom.us/j/63416831557)
- [WinSCP Documentation](https://doc.nhr.fau.de/data/copying/#winscp)
- [Ansys Workbench User Guide](https://faubox.rrze.uni-erlangen.de/getlink/fieKTuNxHpJsVv1AE38k8/)
- [Ansys Forum](https://forum.ansys.com/)
- [Ansys APDL Scripting Course](https://courses.ansys.com/index.php/courses/intro-to-ansys-mechanical-apdl-scripting/)
---

### 2018041742002679_Star-CCM%2B%20erweitertes%20Lizenzpaket%3A%20Star-Creo.md
# Ticket 2018041742002679

 ```markdown
# HPC Support Ticket: Star-CCM+ erweitertes Lizenzpaket: Star-Creo

## Subject
Star-CCM+ erweitertes Lizenzpaket: Star-Creo

## User Issue
- User wants to use Star-CCM+ with CREO 3.0.
- Star-Creo add-on is required for geometry transfer.
- Siemens support indicated that an extended license package for Star-CCM+ should be available at the computing center.
- User receives a license error when trying to use Star-Creo.

## Error Output
```
Checking out license feature:- star-proe...
License build date: 10 February 2015
This version of the code requires license version 2016.10 or greater.
Checking license file: 27000@grid.rrze.uni-erlangen.de
Unable to list features for license file 27000@grid.rrze.uni-erlangen.de.
Checking license file: 1999@flex.cd-adapco.com
Asked for 1 licenses of star-proe and got 0
License request failed
Could not get feature star-proe
License Error: Could not get required license.
STAR-Creo has been disabled.
This window cannot be closed
```

## HPC Admin Response
- Star-CCM+ licenses are managed through ZISC.
- Only POD licenses ("ccmppower") have been available for the past two years.
- User should contact Siemens directly to verify if POD licenses can be used for Star-Creo.
- Additional CAD exchange licenses need to be purchased separately.
- License negotiations with Siemens are ongoing, and the current 3-year POD license is valid until June 2019.

## Key Points Learned
- Star-CCM+ licenses are managed through ZISC.
- POD licenses do not include additional CAD exchange licenses.
- Users need to contact Siemens directly for additional licenses.
- License negotiations with Siemens should be coordinated with Harald Lanig from ZISC.
- New POD keys were generated and distributed to resolve license issues.

## Solution
- User should contact Siemens to purchase additional CAD exchange licenses.
- Coordinate with Harald Lanig from ZISC for license negotiations.
- Ensure that the correct POD keys are used for Star-CCM+.
```
---

### 2023080742002608_Fragen%20%C3%83%C2%BCber%20HPC.md
# Ticket 2023080742002608

 ```markdown
# HPC Support Ticket Conversation Analysis

## Keywords
- HPC
- ANSYS ICEM
- Blender
- Batch-Modus
- Python Skript
- GUI

## Summary
A user inquired about the possibility of running ANSYS ICEM and Blender on HPC systems. The HPC Admin provided information on the requirements for running software in batch mode without a graphical user interface (GUI).

## Root Cause of the Problem
- The user wanted to know if ANSYS ICEM and Blender could be run on HPC systems.
- The user was unsure if HPC systems could handle software that requires a GUI.

## Solution
- The HPC Admin explained that HPC systems do not have a standard GUI and software must run in batch mode (command line only).
- ANSYS ICEM can theoretically run in batch mode for special cases.
- Blender is not centrally installed but can be installed by the user in their directory if it can run in batch mode or be controlled by a Python script without a GUI.

## General Learnings
- HPC systems are suitable for software that can run in batch mode without a GUI.
- Users can install and test software like Blender in their own directories if it meets the batch mode requirements.
- ANSYS ICEM can potentially run on HPC systems in batch mode for special cases.
```
---

### 2018102342001594_Software%20Anfrage.md
# Ticket 2018102342001594

 ```markdown
# HPC Support Ticket Conversation: Software Anfrage

## Keywords
- ANSYS LSDYNA
- Cluster Computing
- Industrieprojekte
- Kostenmodelle
- Lizenz
- Ressourcenanforderungen
- Rechenzeit
- Budget

## Summary
A user inquired about the possibility of using ANSYS LSDYNA on the HPC cluster and the feasibility of running industrial projects, including cost models.

## Root Cause
- User needs to know if ANSYS LSDYNA is available on the HPC cluster.
- User requires information on running industrial projects and associated cost models.

## Solution
- **ANSYS LSDYNA Availability**: Currently, no group is using LS-Dyna on the HPC systems. LS-Dyna is not included in the standard Ansys CFD/Mechanical-Campuslizenz.
- **Industrial Projects**: Possible, but requires a pre-agreement on cost, typically through a flat-rate agreement for a specific node-hour quota.
- **Next Steps**: User needs to provide details on the type of LS-Dyna license they have and the resource requirements (memory, parallelism). Additionally, an estimate of the required computing time and budget is needed.

## General Learnings
- Always check the availability of specific software on the HPC cluster.
- Industrial projects are possible but require prior agreement on cost models.
- Detailed information on software licenses and resource requirements is crucial for planning.
```
---

### 2022012442002215_StarCCM%2B%20error%20on%20HPC.md
# Ticket 2022012442002215

 # HPC Support Ticket: StarCCM+ Error on HPC

## Keywords
- StarCCM+
- Simulation
- Error Report
- PBS File
- OpenMPI
- InfiniBand (IB)
- Rechenknoten
- License

## Summary
A user encountered an error while trying to extend or restart a simulation using StarCCM+. The user provided simulation files and the PBS file used to start the calculations.

## Root Cause
- The error was initially suspected to be related to OpenMPI, indicating a potential InfiniBand (IB) problem.
- Further investigation revealed that a compute node had lost its InfiniBand connection, which was not related to StarCCM+ itself.

## Solution
- The HPC Admin recommended restarting the job, as the issue was likely due to a temporary loss of the InfiniBand connection on a compute node.

## Lessons Learned
- **InfiniBand Issues**: Temporary loss of InfiniBand connections can cause job failures.
- **Job Restart**: Restarting the job can resolve issues caused by temporary network problems.
- **Error Diagnosis**: Initial error reports may not always point to the root cause; further investigation is often necessary.

## Actions Taken
- The HPC Admin checked the license and confirmed it was okay.
- The HPC Admin identified the issue as an InfiniBand problem and recommended restarting the job.

## Recommendations
- **Monitoring**: Regularly monitor the health of InfiniBand connections on compute nodes.
- **User Guidance**: Provide users with guidance on how to handle and report such errors for quicker resolution.

## Follow-Up
- Ensure the user restarts the job and monitor for any recurring issues.
- If the problem persists, further investigation into the InfiniBand infrastructure may be necessary.

---

This documentation can be used to assist in resolving similar errors in the future.
---

### 2022030242000835_Star-CCM%2B.md
# Ticket 2022030242000835

 # HPC Support Ticket: Star-CCM+ Installation Request

## Keywords
- Star-CCM+
- Software Installation
- Emmy
- Meggie
- Simulation

## Summary
A user requested the installation of the latest version of Star-CCM+ (2022.1) on the HPC clusters Emmy and Meggie for simulation purposes.

## Root Cause
The latest version of Star-CCM+ (2022.1) was not installed on the HPC clusters Emmy and Meggie, preventing the user from running simulations with the updated software.

## Solution
HPC Admins installed Star-CCM+ 2022.1 on both Emmy and Meggie clusters, enabling the user to proceed with their simulations.

## General Learnings
- Users may request specific software versions for their research or simulation needs.
- HPC Admins can install software upon user request to ensure compatibility and functionality.
- Effective communication and prompt action by HPC Admins can resolve user issues efficiently.
---

### 42073251_CFX%20Support.md
# Ticket 42073251

 # HPC Support Ticket: CFX Support

## Keywords
- ANSYS support
- CFD simulation
- Contact details
- Germany
- RRZE
- License server

## Summary
A user requested contact details for ANSYS support in Germany for their CFD simulation.

## Root Cause
The user needed support for their CFD simulation using ANSYS and was looking for the appropriate contact details in Germany.

## Solution
The HPC Admin clarified that RRZE does not have a contract with ANSYS and does not operate the ANSYS license server.

## Learning Points
- RRZE does not provide direct support or contact details for ANSYS.
- Users should be directed to the appropriate vendor support channels for specific software issues.
- Clarify the scope of support provided by the HPC center to manage user expectations.

## Actions Taken
- Informed the user that RRZE does not have a contract with ANSYS and does not operate the ANSYS license server.

## Next Steps
- Users should seek support directly from ANSYS or through their institution's license administrator.

## References
- [RRZE HPC Services](http://www.hpc.rrze.uni-erlangen.de/)
- [ANSYS Support](https://www.ansys.com/support)
---

### 2016120642002026_Comsol%20Multiphysics%205.2%20auf%20Cluster.md
# Ticket 2016120642002026

 ```markdown
# HPC Support Ticket: Comsol Multiphysics 5.2 auf Cluster

## Keywords
- Comsol Multiphysics
- Version Update
- Cluster Software
- User Request
- HPC Admin Response

## Summary
A user requested an update to Comsol Multiphysics 5.2 on the cluster, which currently had versions 4.4 and 5.0 available.

## Root Cause
The user needed access to the latest version of Comsol Multiphysics (5.2) for their computations.

## Solution
The HPC Admin installed Comsol Multiphysics 5.2a-up3, which included all the latest patches.

## Lessons Learned
- **User Communication**: Effective communication between users and HPC Admins is crucial for addressing software update requests.
- **Software Updates**: Regular updates to software versions can be necessary to meet user requirements and ensure compatibility with the latest features and patches.
- **Admin Responsiveness**: Prompt action by HPC Admins in addressing user requests helps maintain user satisfaction and productivity.

## Actions Taken
- The user requested an update to Comsol Multiphysics 5.2.
- The HPC Admin responded by installing Comsol Multiphysics 5.2a-up3.
- The user expressed gratitude for the update.
- The ticket was closed with the user satisfied.
```
---

### 2019080242000216_Issue%20to%20copy%20Star-ccm%2B%20User%20guide%20to%20my%20home%20holder.md
# Ticket 2019080242000216

 ```markdown
# HPC Support Ticket: Issue Copying Star-CCM+ User Guide

## Keywords
- Star-CCM+
- User Guide
- PDF File
- Copy Issue
- Home Folder
- HPC Problem

## Summary
A user attempted to copy the Star-CCM+ user guide (PDF file) from the `apps/star-ccm+` directory to their home folder but encountered an error.

## Root Cause
The exact error message was not provided, but it is implied that there was a permission or access issue preventing the copy operation.

## Solution
The HPC Admin responded with a message indicating that the request was moved due to an HPC problem. This suggests that the issue might be related to system-wide permissions or access restrictions.

## Learning Points
- **Permissions and Access**: Ensure that users have the necessary permissions to access and copy files from shared directories.
- **Error Messages**: Always capture and analyze error messages to diagnose the root cause of the issue.
- **HPC Admin Intervention**: Some issues may require administrative intervention to resolve, especially those related to system-wide configurations.

## Next Steps
- **Verify Permissions**: Check the permissions of the `apps/star-ccm+` directory and the user's home folder.
- **Error Logs**: Review any error logs or messages generated during the copy attempt.
- **Admin Assistance**: Escalate the issue to the HPC Admin team if necessary for further investigation and resolution.
```
---

### 2024052742001272_Fragen%20zum%20COMSOL%20Modul.md
# Ticket 2024052742001272

 # HPC-Support Ticket Conversation: COMSOL Module

## Keywords
- COMSOL
- HPC Cluster
- Rechenleistung
- Lizenz
- GUI
- Slurm
- HPC Account
- HPC Portal
- LM_PREFIX

## Summary
A user from a new research team at FAU inquires about using COMSOL on the HPC cluster. The conversation covers licensing, account creation, and the feasibility of using COMSOL's GUI on the cluster.

## Root Cause of the Problem
- User needs to know if COMSOL can be used on the HPC cluster.
- User is unsure about licensing requirements and account creation process.
- User wants to know if COMSOL's GUI can be used on the cluster.

## Solution
- **Licensing**: Nutzungsrechte für COMSOL müssen in ausreichender Anzahl von der Software-Gruppe des RRZE gegen Entgelt besorgt werden.
- **Account Creation**: Der Chef muss sich im HPC-Portal anmelden und Einladungen für die Account-Erstellung versenden.
- **COMSOL GUI**: Die Bedienung von COMSOL über die GUI von den Clustersystemen aus wird nicht empfohlen. Berechnungen müssen im Batchmodus über Slurm laufen.
- **Workflow**:
  - Pre-Processing locally on own Laptop/PC => result: .mph-File
  - Manually transfer the .mph-file to your WORK directory on the HPC system
  - Submit Slurm job which contains:
    ```bash
    module load comsol
    comsol batch -mpibootstrap slurm -inputfile input.mph -outputfile output.mph -tmpdir $TMPDIR
    ```

## General Learnings
- COMSOL can be used on the HPC cluster, but it requires specific licensing.
- Account creation for new users involves the team leader sending invitations through the HPC portal.
- COMSOL's GUI is not practical for use on the cluster; batch processing via Slurm is recommended.
- Pre-processing should be done locally, with the resulting .mph-file transferred to the HPC system for batch processing.

## References
- [HPC Portal](https://portal.hpc.fau.de/)
- [HPC Documentation](https://doc.nhr.fau.de/hpc-portal/#the-management-tab-visible-only-for-pis-and-technical-contacts)
- [HPC Website](https://hpc.fau.de/)
---

### 42291614_ANSYS%20Research%20HPC.md
# Ticket 42291614

 # HPC-Support Ticket: ANSYS Research HPC

## Keywords
- HPC Cluster
- ANSYS Research
- ANSYS HPC
- Licenses
- HPC Account
- LiMa-Cluster
- CFD Simulations

## Problem
- User wants to run simulations on an HPC cluster to utilize more cores than available locally.
- User's department has limited ANSYS Research and ANSYS HPC licenses.

## Root Cause
- Insufficient number of ANSYS licenses to effectively utilize the HPC cluster.

## Solution
- User needs to apply for an HPC account using the "Benutzer- und Projektantrag für HPC-Benutzung" form.
- User's department needs to acquire more ANSYS HPC licenses (at least 20) to make HPC usage meaningful.
- For moderate CFD simulations, the LiMa-Cluster is recommended.

## General Learnings
- HPC cluster usage requires sufficient software licenses.
- Different HPC systems are suited for different types of simulations.
- HPC account application process is necessary for accessing HPC resources.

## References
- [HPC Account Application Form](http://www.rrze.uni-erlangen.de/hilfe/service-theke/formulare.shtml#projekte)
- [HPC Systems Overview](http://www.rrze.uni-erlangen.de/dienste/arbeiten-rechnen/hpc/systeme/)
- [CRT Website](http://www.crt.cbi.uni-erlangen.de)
- [HPC Services](http://www.hpc.rrze.fau.de/)
---

