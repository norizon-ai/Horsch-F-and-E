# Topic 33: gaussian_abaqus_license_software_installation

Number of tickets: 18

## Tickets in this topic:

### 2019022142002609_Gaussian%20Berechnungen%20%28bccb15%29.md
# Ticket 2019022142002609

 ```markdown
# HPC-Support Ticket: Gaussian Berechnungen (bccb15)

## Problem Description
User needs to perform calculations using Gaussian (g09) but encounters an error when starting the calculation with `g09 inputfile`. The error message is:
```
Please specify your name in the input file (Name= keyword)
```

## Root Cause
The user did not specify the required `Name=` keyword in the input file for Gaussian.

## Solution
1. **Specify Name in Input File**: Ensure that the input file for Gaussian includes the `Name=` keyword with the user's name.
2. **Contact Specific Administrator**: The Gaussian binaries/scripts are maintained by a specific individual (Hr. van Eikema Hommes from CCC). Users should contact this person for detailed usage instructions.

## Keywords
- Gaussian (g09)
- Input file
- Name= keyword
- Error message
- HPC Admin
- CCC
- Binaries/Scripts

## General Learnings
- Always check the input file for required keywords when running specific software.
- For software maintained by specific individuals or groups, contact them directly for detailed usage instructions.
- HPC Admins can provide guidance on where to find resources but may not always have detailed knowledge of specific software usage.
```
---

### 2020082442002501_Question%20to%20Abaqus%20Research%20Version.md
# Ticket 2020082442002501

 # HPC Support Ticket: Abaqus Research Version

## Keywords
- Abaqus Research Version
- License Tokens
- HPC Cluster
- Installation
- Woody Node

## Summary
A student from the Institute General Materials Properties (WW1) inquired about the availability of Abaqus Research Version on the HPC cluster for their master thesis. The HPC Admin provided information about the current installation and the need for licenses.

## Problem
- The user needed to run Abaqus Research Version on the HPC cluster.
- The HPC cluster did not have the required version of Abaqus installed.
- The user's chair had a limited number of license tokens (15), which would be consumed by running Abaqus jobs on the HPC cluster.

## Solution
- The HPC Admin confirmed that they do not provide licenses for application software.
- The user was informed that running Abaqus jobs would compete with the licenses available at the chair.
- The HPC Admin agreed to install Abaqus 2018 on the Woody node.
- The user was advised to test the installation and report any issues.

## Lessons Learned
- Users need to be aware of the license limitations when using software on HPC clusters.
- The HPC Admin can install specific software versions upon request, but users should provide detailed information about the version and any potential issues.
- Testing the installation is crucial to ensure that the software runs correctly on the HPC cluster.

## Root Cause
- The user needed a specific version of Abaqus that was not initially available on the HPC cluster.
- The limited number of license tokens at the user's chair posed a challenge for running Abaqus jobs on the HPC cluster.

## Resolution
- The HPC Admin installed Abaqus 2018 on the Woody node.
- The user was advised to test the installation and report any issues for further assistance.

## Follow-up
- The user should test the Abaqus 2018 installation on the Woody node and report any issues to the HPC Admin for further assistance.
- The HPC Admin should monitor the installation and be prepared to address any issues that arise during testing.
---

### 2022091542004191_Gaussian%20WoodyNG.md
# Ticket 2022091542004191

 # HPC Support Ticket Conversation Analysis

## Keywords
- Gaussian
- Emmy
- WoodyNG
- Nutzungsrechte (usage rights)
- SLURM
- Zugriffsrechte (access rights)
- Owner/Group

## Summary
A user inquires about continuing to use Gaussian on WoodyNG after Emmy is decommissioned. The conversation involves checking access rights and the availability of the Gaussian installation.

## Root Cause of the Problem
- The user needs access to Gaussian on WoodyNG.
- The Gaussian installation directory (`/home/woody/bcosw`) had incorrect access rights.

## Solution
- The access rights for the Gaussian installation directory were corrected.
- The user was informed that the Gaussian installation should be available and functional.

## General Learnings
- Users may need to be granted specific access rights to use certain software on new clusters.
- Directory permissions and ownership need to be correctly set for software installations to be accessible.
- Collaboration between different support team members is essential for resolving complex issues.

## Actions Taken
- HPC Admin checked and corrected the access rights for the Gaussian installation directory.
- The user was informed about the status of the Gaussian installation and the need for SLURM script adjustments.

## Next Steps
- The user should test the Gaussian installation on WoodyNG.
- If further issues arise, the SLURM submit script may need to be adjusted.

## Additional Notes
- The user was informed that the responsible person for Gaussian was on vacation, which could delay further assistance.
- The HPC Admin team collaborated to resolve the access rights issue.
---

### 2023012642001498_Flow3D%20at%20FAU.md
# Ticket 2023012642001498

 # HPC Support Ticket: Flow3D at FAU

## Keywords
- Flow3D
- Commercial Software
- Licensing
- OpenFoam
- Software Availability
- FAU Clusters
- Ticket Support

## Summary
- **Issue**: User inquired about the availability of Flow3D commercial simulation software on FAU clusters.
- **Response**: HPC Admin informed that Flow3D is not available on the clusters. Users need to bring their own license for commercial software.
- **Alternatives**: OpenFoam is available as a free CFD software.
- **Additional Information**: An overview of software packages available at FAU and their costs can be found [here](https://www.rrze.fau.de/hard-software/software/dienstliche-nutzung/produkte/).
- **Historical Note**: LSTM had a Flow3D license at one point, as noted in Ticket#2019030742000878.

## Solution
- Users need to bring their own license for commercial software like Flow3D.
- For assistance in setting up a license for a commercial application, users should open a ticket by sending an email to `hpc-support@fau.de`.

## Action Items
- Direct users to the software packages overview page for more information.
- Assist users in setting up licenses for commercial software if they provide their own.

## Contact Information
- **Support Email**: `hpc-support@fau.de`
- **Website**: [FAU HPC](https://hpc.fau.de/)

## Related Tickets
- Ticket#2019030742000878: Bad performance of Flow3D jobs on Emmy / iwst024h
---

### 2022030442001367_Question.md
# Ticket 2022030442001367

 # HPC Support Ticket Conversation: Abaqus Software Usage

## Keywords
- Abaqus
- FEM simulations
- HPC cluster
- License tokens
- Emmy cluster

## Summary
A Ph.D. student from the WW1 chair requests detailed instructions on using Abaqus software for FEM simulations on the HPC cluster. The HPC admin provides information on license token requirements and the need to acquire installation files for a recent Abaqus version.

## Root Cause of the Problem
- Lack of detailed instructions on using Abaqus software on the HPC cluster.
- Need for installation files for a recent Abaqus version.

## Solution
- The HPC admin informs the user about the license token requirements for different clusters.
- The HPC admin plans to acquire the installation files for a recent Abaqus version from the software colleagues at RRZE.
- The user is informed that the module "abaqus/2021" is now available, including abq2021hf7, and initial testing is up to the user.

## General Learnings
- Different clusters have varying license token requirements for Abaqus jobs.
- The usage of Abaqus on HPC systems competes with the usage at the chair as both access the same license pool.
- The HPC admin may need to acquire installation files for recent software versions from the software colleagues at RRZE.
- Initial testing of newly installed software may be the responsibility of the user.

## Action Items
- Acquire installation files for a recent Abaqus version.
- Inform the user about the availability of the "abaqus/2021" module.
- The user should perform initial testing of the newly installed Abaqus software.
---

### 2021102842003701_Abaqus%20on%20HPC%3F.md
# Ticket 2021102842003701

 # HPC Support Ticket: Abaqus on HPC

## Keywords
- Abaqus
- Emmy cluster
- Installation
- License tokens
- Woody cluster

## Problem
- User wants to install and run Abaqus on the Emmy cluster.
- Unsure about the requirements and process for installation.

## Root Cause
- Lack of information on installing Abaqus on the Emmy cluster.
- Concerns about license token usage and availability.

## Solution
- HPC Admin will obtain installation files for Abaqus.
- User is advised about license token usage:
  - Emmy node with 20 physical cores will block 24 license tokens.
  - Total license tokens available for LTM are 80.
  - Woody cluster with 4 cores per node will block 8 license tokens, suggested as an alternative for larger simulations.

## General Learnings
- Abaqus installation requires specific files and license considerations.
- Different clusters (Emmy vs. Woody) have varying impacts on license token usage.
- Importance of understanding license token allocation for efficient resource management.

## Next Steps
- HPC Admin to provide installation files and further guidance.
- User to test Abaqus on the specified account.

## References
- [HPC Systems Documentation](https://hpc.fau.de/systems-services/systems-documentation-instructions/special-applications-and-tips-tricks/)
---

### 2022112142003461_Doubt%20about%20the%20Abaqus%20pool%20licensing%20system.md
# Ticket 2022112142003461

 # HPC Support Ticket: Abaqus Pool Licensing System

## Keywords
- Abaqus
- Licensing
- Pool Licensing
- HPC Cluster
- Commercial Software

## Problem
- User needs information on how the pool of licenses for Abaqus works.
- Concern about the limited number of licenses and their consumption.

## Root Cause
- Lack of understanding about the licensing system for Abaqus on HPC clusters.

## Solution
- **HPC Clusters and Licenses**: HPC clusters do not have their own licenses for commercial application software like Abaqus.
- **License Consumption**: Running Abaqus on HPC clusters consumes the licenses purchased by the user's institute (LGT in this case).
- **License Details**: LGT has a total of 30x Abaqus and 1x CAE licenses. Recent runs on the HPC cluster consumed 10x Abaqus licenses per run.

## General Learning
- Commercial software licenses on HPC clusters are typically managed by the user's institute.
- Understanding license consumption is crucial for planning and executing large-scale simulations.

## Action Taken
- HPC Admin provided information on the licensing system and the number of licenses available and consumed.

## Follow-up
- Users should monitor their license usage and plan their simulations accordingly to avoid exceeding the available licenses.

---

This documentation can be used to address similar queries about software licensing on HPC clusters.
---

### 2015080442001577_Gaussian%20program.md
# Ticket 2015080442001577

 # HPC Support Ticket: Gaussian Program

## Keywords
- Gaussian quantum chemistry program
- MD simulations
- License sharing
- Single machine installation
- License cost

## Summary
A user from the Computational Biology group inquires about accessing the Gaussian quantum chemistry program for generating parameters for MD simulations. They ask if another group already has a license they could share or if it's possible to install Gaussian on a single machine at the HPC site.

## Root Cause
- User needs access to the Gaussian program for research purposes.
- Potential cost and licensing issues.

## Solution
- The ticket was redirected to another support member (Nico) for further assistance.
- No final resolution provided in the given conversation.

## General Learnings
- Users may request specific software for their research needs.
- Licensing and cost considerations are important factors when installing new software.
- Collaboration and sharing licenses among different working groups can be explored.

## Next Steps
- Check if any other group has a Gaussian license that can be shared.
- Evaluate the feasibility of installing Gaussian on a single machine.
- Discuss the licensing cost and payment options with the relevant authorities.
---

### 2025012342003247_Gaussian%20usage.md
# Ticket 2025012342003247

 # Gaussian Usage Permission Request

## Keywords
- Gaussian
- Permission Request
- HPC Account
- NHR@FAU
- Woody
- Dr. van Hommes
- CCC

## Summary
A user requested permission to use Gaussian at NHR@FAU. The HPC Admin informed the user that their account was already enabled for Gaussian and provided additional information about the software's availability and maintenance.

## Root Cause
- User was unaware that their HPC account already had permission to use Gaussian.

## Solution
- HPC Admin verified the user's account status and confirmed that Gaussian was already enabled.
- Informed the user about the availability of Gaussian on the Woody cluster.
- Clarified that the Gaussian installation is maintained by Dr. van Hommes from CCC, not the HPC support team.

## General Learnings
- Always check the status of a user's account before processing permission requests.
- Provide users with relevant information about software availability and maintenance responsibilities.
- Maintain open communication channels with users to address their concerns and queries promptly.
---

### 42157028_Abaqus%20Software.md
# Ticket 42157028

 # HPC Support Ticket: Abaqus Software

## Keywords
- Abaqus
- HPC
- Linux
- License
- Module
- Woody

## Summary
A user from the Lehrstuhl für Strömungsmechanik (LSTM) inquired about using Abaqus software on the HPC system for high-performance computations. The user had difficulties finding information about the system on which Abaqus is installed and the license requirements.

## Root Cause
- The user was unable to find information about the system (Windows or Linux) on which Abaqus is installed.
- The user did not have access to Abaqus on the HPC system.

## Solution
- **System Information**: Abaqus is available on the Linux HPC system (Woody).
- **Access Grant**: Access to Abaqus is granted only after confirmation from the software group of RRZE that the user has valid licenses. The user was advised to contact `software@rrze.fau.de` to confirm the number of licenses needed.
- **Access Path**: The user was granted access to `/apps/abaqus/6.11-1/` on Woody. The user was instructed to initialize the Abaqus environment manually as no module is provided for Abaqus.
- **License Limitation**: The user was informed that LSTM has only 1 usage right for Abaqus, limiting access to 5 Abaqus or 1 CAE tokens.

## General Learnings
- Always confirm the system requirements and license availability for specific software on the HPC system.
- Access to licensed software on the HPC system requires confirmation from the software group.
- Users may need to manually initialize the environment for software without a provided module.
- License limitations should be clearly communicated to users to avoid overuse.

## Next Steps
- Ensure that the user has the necessary licenses and access to Abaqus.
- Provide documentation or guidance on initializing the Abaqus environment manually.
- Monitor license usage to ensure compliance with the limitations.
---

### 2023112442002516_Gaussian%20-%20b118bb12.md
# Ticket 2023112442002516

 ```markdown
# HPC-Support Ticket: Gaussian License Availability

## Keywords
- Gaussian
- License
- FAU-internal users
- NHR
- LRZ
- Post-processing
- QM calculations
- ORCA

## Problem
- User requires Gaussian for QM calculations and post-processing.
- Gaussian output files are needed for a crucial post-processing program.

## Root Cause
- Gaussian license is only available for FAU-internal users.
- High costs for a DataCenter license that would allow NHR usage.

## Solution
- User advised to perform Gaussian post-processing locally at their department if they have a license and sufficient computing resources.
- Alternatively, user can use LRZ, which has a DataCenter license for Gaussian.
- HPC Admins offer support to run the user's Gaussian binary on the cluster if the user's group has a valid license that allows external usage.

## General Learnings
- Gaussian license availability is limited to FAU-internal users due to cost constraints.
- Users should check for alternative resources like LRZ for Gaussian usage.
- HPC Admins can assist in running user-provided Gaussian binaries if licensing conditions allow.
```
---

### 2015080742002687_Gaussian.md
# Ticket 2015080742002687

 ```markdown
# HPC Support Ticket: Gaussian License Access

## Keywords
- Gaussian License
- User Group Management
- Software Access
- License Compliance

## Summary
A user requested access to the Gaussian software license for themselves and a colleague. The HPC admins discussed whether to grant access to the specific users or to the entire user group.

## Root Cause
- User needed access to the Gaussian software license.
- Uncertainty about whether to grant access to specific users or the entire group.

## Solution
- The HPC admin decided to grant access to the entire user group (bcosw-Gruppe) as there were no license restrictions for other software in that group.
- The access was recorded in the group management system and awaited processing by the BV.

## General Learnings
- Understand the licensing requirements and restrictions for different software.
- Consider granting access to entire user groups if there are no license restrictions.
- Ensure proper documentation and processing of access requests.
```
---

### 2023042542002493_Generelle%20Fragen%20zum%20Rechnen%20am%20HPC.md
# Ticket 2023042542002493

 # HPC Support Ticket Conversation Summary

## Keywords
- Gaussian 16
- HPC Clusters
- Software Licensing
- Job Limits
- Costs
- Site-License
- CCC
- Woody Cluster
- Tier3
- Tier2/NHR

## General Learnings
- **Software Licensing**: Gaussian 16 is licensed for use on HPC systems through a site-license managed by the Computer-Chemie-Center (CCC).
- **Job Limits**: The Woody Cluster has a job limit of 24 hours, with nodes having either 4 or 32 cores.
- **Costs**: No costs are incurred for HPC usage within the Tier3 framework. For extensive computational needs, a Tier2/NHR application is required.
- **Software Management**: The software is maintained by a specific individual who handles its integration and updates on the HPC systems.

## Root Cause of the Problem
- The user needed clarification on the availability of Gaussian 16 on the RRZE, job limits on the Woody Cluster, and potential costs associated with HPC usage.

## Solution
- **Software Availability**: Gaussian 16 is available on the HPC systems due to the site-license.
- **Job Limits**: The Woody Cluster has specific job limits and node configurations.
- **Costs**: Usage within Tier3 is free, but extensive usage requires a Tier2/NHR application.

## References
- [Woody Cluster Documentation](https://hpc.fau.de/systems-services/documentation-instructions/clusters/woody-cluster/)
- [NHR Application Rules](https://hpc.fau.de/systems-services/documentation-instructions/nhr-application-rules/)

## Notes
- For detailed information on Gaussian 16 and its setup, users should contact the individual responsible for maintaining the software on the HPC systems.
- The HPC support team can provide further assistance with specific questions related to software licensing, job limits, and cost structures.
---

### 2023112642000381_Permissions-Problem%20bei%20Gaussian%20-%20bcosw.md
# Ticket 2023112642000381

 # HPC-Support Ticket: Permissions-Problem bei Gaussian - bcosw

## Keywords
- Gaussian
- Permissions
- Unix-Permissions
- HPC-Accounts
- HPC-Portal
- Gruppenlösung
- swgauss
- bcosw
- chgrp
- chown

## Problem
- Gaussian erfordert spezifische Unix-Permissions für die Nutzung.
- Die automatische Befüllung der Gruppe `bcosw` funktioniert nach der Umstellung auf das HPC-Portal nicht mehr.
- Benutzer berichten über "Permission denied" Fehler beim Start von Gaussian.

## Ursache
- Die automatische Befüllung der Gruppe `bcosw` wurde durch die Umstellung auf das HPC-Portal unterbrochen.
- Die Berechtigungen für die Software und die Benutzergruppen sind nicht korrekt gesetzt.

## Lösung
1. **Erstellung einer neuen Unixgruppe `swgauss`**:
   - Portal-Accounts können auf Zuruf in die neue Unixgruppe `swgauss` eingefügt werden.

2. **Änderung der Gruppenzugehörigkeit der Software**:
   - Ausführung von `chgrp -Rh swgauss /home/woody/bcosw` um die Software der richtigen Gruppe zuzuordnen.

3. **Manuelle Hinzufügung von Benutzern zur Gruppe `swgauss`**:
   - Benutzer, die Gaussian nutzen möchten, müssen manuell zur Gruppe `swgauss` hinzugefügt werden.

4. **Überprüfung und Verteilung der Rechte**:
   - Die Rechte müssen schrittweise verteilt werden. Benutzer, die dringend Zugriff benötigen, sollen sich melden.

## Weitere Schritte
- Überprüfung der Anmeldung über eduGAIN und Freischaltung der Attribute für Projekt `bccc102`.
- Hinzufügung weiterer Benutzer zur Gruppe `swgauss` nach Bedarf.

## Hinweise
- Die Zugriffsberechtigungen müssen über Unix-Permissions durchgesetzt werden, da Gaussian dies bei jedem Programmstart überprüft.
- Die Entfernung dieser Überprüfung würde gegen die Lizenzbedingungen verstoßen und zur Annulierung der Lizenz führen.

## Zusammenfassung
Das Problem mit den Berechtigungen für Gaussian wurde durch die Umstellung auf das HPC-Portal verursacht. Die Lösung besteht darin, eine neue Unixgruppe `swgauss` zu erstellen und die Benutzer sowie die Software dieser Gruppe zuzuordnen. Die Rechte müssen schrittweise verteilt und bei Bedarf manuell angepasst werden.
---

### 2023052642001516_Gaussian.md
# Ticket 2023052642001516

 # HPC Support Ticket: Gaussian Installation and Usage

## Keywords
- Gaussian 16
- Installation
- Submit Scripts
- Geometry Optimization
- Single Point Charges
- MD Simulations

## Summary
- **User Inquiry**: Request for information about Gaussian installation and availability on the HPC system.
- **HPC Admin Response**: Gaussian 16 is installed but currently located in a hard-to-reach place without functional submit scripts. Plans for improvement are in progress but require further coordination.
- **User Clarification**: Need for Gaussian to perform geometry optimizations and single point charges for ligand preparation in MD simulations.

## Root Cause
- Gaussian 16 is installed but not easily accessible, and submit scripts are not functional.

## Solution
- **Current Status**: Gaussian 16 is available but with limited accessibility.
- **Future Plans**: Improvements are planned but require further discussions and implementation.

## General Learnings
- **Software Availability**: Ensure that installed software is easily accessible and functional for users.
- **User Needs**: Understand the specific computational needs of users to provide tailored support.
- **Communication**: Keep users informed about the status of software and planned improvements.

## Next Steps
- **HPC Admins**: Coordinate and implement improvements for Gaussian 16 accessibility and submit scripts.
- **2nd Level Support**: Assist users with any immediate needs and provide updates on the status of Gaussian 16.

---

This documentation can be used to address similar inquiries about software availability and accessibility on the HPC system.
---

### 2022042842002015_NHR%20%20-%20Gaussian%20software.md
# Ticket 2022042842002015

 # HPC Support Ticket: NHR - Gaussian Software

## Keywords
- NHR cluster
- Gaussian software
- Quantum mechanical calculations
- Software installation
- License management

## Problem
- User unable to find Gaussian software on NHR cluster using `module avail`.
- User requests possibility to perform quantum mechanical calculations with Gaussian.

## Root Cause
- Gaussian software is not installed on the NHR cluster.
- NHR@FAU does not have a license for Gaussian.

## Solution
- HPC Admin suggests exploring the possibility of using the user's own Gaussian license.
- HPC Admin will consult with the Computer-Chemie-Centrum to check if access to their Gaussian binaries can be provided.

## General Learnings
- Always check software availability using `module avail`.
- Licensing issues can prevent software installation on HPC clusters.
- Collaboration with other departments (e.g., Computer-Chemie-Centrum) can provide alternative solutions for software access.

## Next Steps
- Await response from Computer-Chemie-Centrum regarding access to Gaussian binaries.
- Explore other quantum chemistry software options if Gaussian access is not feasible.
---

### 2019120542001891_Gaussian.md
# Ticket 2019120542001891

 # HPC-Support Ticket: Gaussian Software Availability

## Keywords
- Gaussian software
- Cluster availability
- Postdoc support
- Software licensing
- Contact person

## Summary
A professor inquired about the availability of Gaussian software and which clusters it can be used on for their postdoc's calculations.

## Root Cause
The user needed information on the availability of Gaussian software and the specific clusters where it can be utilized.

## Solution
The HPC Admin directed the user to contact a specific person (Nico van Eikema Hommes) for all questions regarding Gaussian.

## General Learnings
- **Software Availability**: Always check with the designated contact person for specific software.
- **Cluster Usage**: Different software may be available on different clusters.
- **Support Channels**: Utilize the appropriate support channels for specific inquiries.

## Next Steps
- **User**: Contact the designated person for further details on Gaussian software.
- **HPC Admin**: Ensure that the contact information for specific software is up-to-date and easily accessible.

## Additional Notes
- **Communication**: Clear and concise communication is essential for efficient support.
- **Documentation**: Maintain updated documentation on software availability and cluster usage.

---

This documentation can be used as a reference for future inquiries about software availability and cluster usage.
---

### 2025030542003081_Gaussian%20auf%20Woody.md
# Ticket 2025030542003081

 ```markdown
# HPC Support Ticket: Gaussian auf Woody

## Keywords
- Gaussian Installation
- Woody
- Module Availability
- Group Permissions
- Submit Scripts

## Problem
- User unable to find Gaussian installation on Woody.
- Gaussian not listed as a module with `module avail`.

## Root Cause
- Gaussian binary is only visible to users added to a specific group.
- User needs additional permissions managed by a third party (CCC).

## Solution
1. **Contact CCC for Permission**:
   - User needs to contact Nico Hommes from CCC to request permission to use Gaussian.
   - CCC will then inform HPC support to add the user to the Gaussian group.

2. **Add User to Group**:
   - HPC Admin adds the user to the `swgauss` group via the HPC portal under "other projects".

3. **Access Gaussian**:
   - Once added to the group, the user can access Gaussian on Woody.

4. **Submit Scripts**:
   - No pre-configured submit scripts available in HPC documentation.
   - User advised to contact Marius Trollmann for example scripts.

## Additional Information
- Gaussian is only available on Woody, not accessible via NHR accounts.
- Example submit script provided by Marius Trollmann:
  - Reserves 8 CPU cores.
  - Uses Gaussian09 version.
  - Submitted using `sbatch run_gau.sh`.

## Conclusion
- Users need specific permissions to access Gaussian on Woody.
- Contact CCC for permission and HPC support for group addition.
- Example scripts can be obtained from experienced users.
```
---

