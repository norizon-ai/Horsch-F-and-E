# Topic 37: orca_woody_software_group_module

Number of tickets: 10

## Tickets in this topic:

### 2024101042001838_Software%20request%3A%20Orca%206.md
# Ticket 2024101042001838

 ```markdown
# Software Request: Orca 6

## Keywords
- ORCA
- Software Request
- Module Installation
- AVX2
- HPC Support

## Summary
A user requested the installation of ORCA version 6.0.0 on the HPC systems, highlighting new features and performance improvements. The HPC Admin installed the module and advised thorough testing before production use.

## Root Cause
- User identified new features and performance benefits in ORCA 6.0.0.
- Need for an updated module to leverage these improvements.

## Solution
- HPC Admin installed the `orca/6.0.0-avx2` module on Woody.
- User was advised to test the module thoroughly before using it for production calculations.

## General Learnings
- Users can request software updates based on new features and performance improvements.
- HPC Admins can install and provide new software modules upon request.
- Thorough testing is recommended for new software installations to ensure stability and compatibility.
```
---

### 2022062442002261_ORCA%20on%20Woody%3F.md
# Ticket 2022062442002261

 # HPC Support Ticket: ORCA on Woody

## Keywords
- ORCA module activation
- Eligibility proof
- Memory requirements
- Job submission parameters

## Summary
A user requested activation of the ORCA module for their HPC account to run quantum chemistry calculations on the Woody cluster. The user provided their ORCA forum username and university email address as proof of eligibility.

## Root Cause
- User needed to prove eligibility to use ORCA.
- Some ORCA jobs required more memory than available on certain nodes.

## Solution
- HPC Admin activated the ORCA module for the user's account.
- User was advised to specify nodes with sufficient memory for their jobs using the `-lnodes=1:ppn=4:any32g` parameter.

## What Can Be Learned
- To activate a specific module, users may need to provide proof of eligibility, such as a registered forum username and institutional email address.
- When submitting jobs, users should ensure that the selected nodes have sufficient resources (e.g., memory) for their calculations.
- HPC Admins can assist users in resolving job-related issues by providing appropriate job submission parameters.

## Follow-Up
- Users should monitor their jobs to ensure they are running efficiently and not causing excessive swapping on nodes.
- HPC Admins may need to review and update cluster documentation to include information about job submission parameters for different node types.
---

### 2021092042003478_Freischaltung%20ORCA%20Software%20auf%20HPC.md
# Ticket 2021092042003478

 ```markdown
# HPC Support Ticket: Freischaltung ORCA Software auf HPC

## Keywords
- ORCA Software
- License Activation
- Software Installation
- Module Availability
- User Access

## Summary
A user requested access to the ORCA software for their computations. The user provided a confirmation email from the ORCA license team. The HPC admin responded with information about available ORCA versions and the possibility of installing a newer version.

## Root Cause
- User needed access to ORCA software for computations.
- User provided license confirmation but required activation on the HPC system.

## Solution
- HPC admin informed the user about available ORCA versions (ORCA-4.x) on Woody and TinyFAT.
- HPC admin offered to install ORCA-5.x but mentioned a delay due to operational reasons.
- HPC admin later confirmed the installation of ORCA-5.0.1 and requested the user to test the installation.

## What Can Be Learned
- Users need to provide license confirmation for software activation.
- HPC admins can install and update software versions upon user request.
- Users should test new software installations and provide feedback to HPC admins.

## Follow-Up Actions
- Ensure users are aware of the available software modules.
- Provide clear instructions for testing new software installations.
- Maintain communication with users regarding software updates and delays.
```
---

### 2024031542001101_Orca%20v4.md
# Ticket 2024031542001101

 # HPC Support Ticket Conversation: Orca v4

## Keywords
- Orca v4
- Orca v5
- Woody
- TinyFAT
- Turbomole
- Version compatibility

## Summary
A user needed to use Orca v4 for compatibility with another code's interface, which was not supported by Orca v5. The user inquired about the availability of Orca v4 on the Woody cluster, as it was available on the TinyFAT nodes.

## Problem
- **Root Cause**: Compatibility issue with Orca v5 and another code's interface.
- **User Request**: Access to Orca v4 on the Woody cluster.

## Solution
- **HPC Admin Suggestion**: Try using the copied Orca v4 on Woody. If it doesn't work, use TinyFAT nodes for the calculations.
- **Outcome**: The user confirmed that Orca v4 worked on Woody.

## Additional Issue
- **Root Cause**: Compatibility issue with the current Turbomole version.
- **User Request**: Access to older versions of Turbomole (7.1 to 7.4).

## Solution
- **HPC Admin Response**: Older versions of Turbomole (7.1 to 7.4) are not available as the NHR license started with version 7.6.

## General Learnings
- **Version Compatibility**: Ensure that the versions of software used are compatible with each other.
- **Cluster Availability**: Different clusters may have different software versions available.
- **License Constraints**: Software availability may be limited by licensing agreements.

## Next Steps
- If similar issues arise, suggest checking the availability of required software versions on different clusters.
- Inform users about license constraints that may affect software availability.
---

### 2023061442002251_ORCA.md
# Ticket 2023061442002251

 ```markdown
# HPC Support Ticket: ORCA Module Access

## Keywords
- ORCA
- Module Access
- Cluster
- Registration
- Freischalten

## Problem
- User requires access to ORCA modules on the cluster.
- User is a Master's student and has used ORCA on other clusters.
- User is registered in the ORCA forum.

## Solution
- HPC Admin enabled ORCA modules for the user.
- Confirmed that ORCA-5.0.4 is installed on most clusters.
- Offered to provide newer versions of ORCA upon request.

## What Can Be Learned
- Users need to request access to specific modules.
- HPC Admin can enable modules for users.
- Different versions of software can be provided upon request.
- Registration in relevant forums or platforms may be required for access.

## Root Cause
- The ORCA modules were not initially accessible to the user.

## Resolution
- HPC Admin granted access to the ORCA modules.
- User confirmed that the modules are now accessible.
```
---

### 2021022442001494_ORCA%20license%20Meyer%20Group.md
# Ticket 2021022442001494

 ```markdown
# HPC-Support Ticket Conversation: ORCA License Meyer Group

## Keywords
- ORCA
- Gaussian
- License
- HPC Clusters
- Access
- Modules
- Cores
- Woody
- TinyFAT
- TinyEth

## Summary
A user from the Meyer Group (Anorganische Chemie II) inquired about the availability of ORCA and Gaussian licenses on the HPC clusters and requested access to these modules for their account.

## Root Cause
The user needed to know if their group had access to ORCA and Gaussian licenses and required activation of these modules for their account.

## Solution
- **ORCA License**: The user's group (AK Meyer Anorganische Chemie II) already had access to the ORCA license. The HPC Admin confirmed that the user should have access to the ORCA modules.
- **ORCA Availability**: ORCA is only available on specific clusters (Woody, TinyFAT, TinyEth) due to limited core usage.
- **Gaussian License**: The user was directed to contact Dr. Nico van Eikema Hommes from the Computer Chemie Centrum for Gaussian license management. If approved, the user should be able to access Gaussian in the specified directory.

## Additional Information
- **ORCA Clusters**: Woody, TinyFAT, TinyEth
- **Gaussian Directory**: `/home/woody/bcosw/`
- **Contact for Gaussian**: Dr. Nico van Eikema Hommes (nico.hommes@fau.de)

## Conclusion
The user was informed about the availability of ORCA and Gaussian licenses and provided with the necessary steps to access these modules.
```
---

### 2023083142000421_ORCA%20Module%20Freischaltung.md
# Ticket 2023083142000421

 ```markdown
# HPC-Support Ticket Conversation: ORCA Module Freischaltung

## Keywords
- ORCA Module
- Freischaltung
- TinyFAT
- Woody
- Meggie
- bco1-Gruppe

## Summary
- **User Request**: User requests access to the ORCA module for computations.
- **HPC Admin Response**: Informs the user that the ORCA module is already available on TinyFAT, Woody, and Meggie for the entire bco1-Gruppe.

## Root Cause of the Problem
- User was unaware that the ORCA module was already accessible for their group.

## Solution
- HPC Admin clarified that the ORCA module is already available on the specified systems for the user's group.

## What Can Be Learned
- Users should check if their group already has access to specific modules before requesting activation.
- HPC Admins can provide information about pre-existing access to modules for specific groups.
```
---

### 2024112642003233_Activation%20of%20the%20ORCA%20module.md
# Ticket 2024112642003233

 # HPC Support Ticket: Activation of the ORCA Module

## Keywords
- ORCA software
- Woody cluster
- Module activation
- Group permissions

## Summary
A user requested permission to use the ORCA software on the Woody cluster. The HPC Admin responded that ORCA has already been unlocked for the entire group `bccc`.

## Root Cause
- User was unaware that ORCA was already available for their group.

## Solution
- Check if the ORCA module is visible and accessible on the Woody cluster.
- Confirm that the user is part of the `bccc` group, which has access to ORCA.

## General Learnings
- Always check if the required software module is already available for your group.
- Verify group permissions before requesting additional access.

## Actions Taken
- HPC Admin informed the user about the existing access to ORCA for the `bccc` group.

## Follow-up
- User should verify the availability of the ORCA module on the Woody cluster.

---

This documentation can be used to address similar queries regarding software module access and group permissions on the HPC cluster.
---

### 2025022742002382_Access%20to%20orca.md
# Ticket 2025022742002382

 # HPC Support Ticket Conversation Summary

## Subject: Access to ORCA

### Keywords:
- ORCA
- Access
- Eligibility
- WinSCP
- Documentation
- Job Script
- HPC Introduction

### General Learnings:
- Documentation for ORCA is available at [ORCA Documentation](https://doc.nhr.fau.de/apps/orca/).
- ORCA is accessible on Woody and TinyFAT clusters.
- General introduction to HPC for beginners is offered periodically.
- WinSCP usage with HPC systems is documented at [WinSCP Documentation](https://doc.nhr.fau.de/data/copying/?h=winscp#winscp).

### Problem:
- User needs access to ORCA for PhD studies.
- User inquires about proof of eligibility for access.
- User seeks information on accessing files through WinSCP.

### Solution:
- User's group (bca2) is already eligible to use ORCA.
- Documentation links provided for ORCA and WinSCP usage.
- User successfully accessed ORCA through the command prompt.

### Root Cause:
- User was unaware of their group's eligibility for ORCA.
- User needed guidance on accessing files through WinSCP.

### Actions Taken:
- HPC Admins provided documentation links for ORCA and WinSCP.
- Confirmed user's group eligibility for ORCA.
- User successfully accessed ORCA and inquired about WinSCP usage.

### Follow-up:
- User should review the provided documentation for further assistance.
- User can attend the general introduction to HPC for beginners for additional guidance.

### References:
- [ORCA Documentation](https://doc.nhr.fau.de/apps/orca/)
- [WinSCP Documentation](https://doc.nhr.fau.de/data/copying/?h=winscp#winscp)
- [HPC Introduction](https://hpc.fau.de/teaching/hpc-cafe/#nutshell)
---

### 2024062542001827_Aktivierung%20ORCA%20auf%20Fritz%20-%20bccc116h.md
# Ticket 2024062542001827

 ```markdown
# HPC-Support Ticket: ORCA Activation on Fritz Cluster

## Keywords
- ORCA
- Fritz Cluster
- NHR Cluster
- Module Activation
- User Registration
- Group Access

## Problem
- User requested activation for ORCA on the NHR Cluster Fritz.
- User mentioned registration in the ORCA Forum under a specific username.

## Root Cause
- User was unaware that their group (bccc) was already activated for ORCA on Fritz.

## Solution
- HPC Admin informed the user that their group (bccc) was already activated for ORCA.
- Suggested that Woody might be better suited for ORCA than Fritz.

## General Learnings
- Check group-level activations before requesting individual access.
- Consider cluster suitability for specific software (e.g., Woody for ORCA).

## Additional Notes
- No further proof was required as the user's group was already activated.
- The user should be able to see the ORCA modules without additional steps.
```
---

