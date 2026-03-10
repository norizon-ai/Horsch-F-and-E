# Topic 38: md_properties_simulations_pymol_forcefields

Number of tickets: 10

## Tickets in this topic:

### 2024030842002542_Computerchemie%20Praktikum%20Pharmazie.md
# Ticket 2024030842002542

 ```markdown
# HPC Support Ticket Conversation Summary

## Overview
This conversation revolves around setting up HPC accounts and environments for a computer chemistry practical course at FAU. The course involves molecular dynamics (MD) simulations of GPCRs using Alex, with subsequent analysis using Python and MDAnalysis.

## Key Points

### Initial Request
- **User:** Eduard Neu
- **Request:** Setting up HPC accounts for a practical course in computer chemistry.
- **Details:**
  - Course duration: 11.03.2024 to 05.04.2024.
  - Participants: 19 students.
  - Requirements: MD simulations on Alex, analysis using Python and MDAnalysis.

### HPC Account Setup
- **HPC Admins:** Thomas Zeiser, Johannes Veh
- **Actions:**
  - Created HPC accounts for all participants.
  - Provided access via Jupyterhub and SSH.
  - Set up conda environments for analysis.

### Conda Environment Setup
- **User Requirements:**
  - Python environment with MDAnalysis.
  - Visualization tools: PyMOL and VMD.
- **HPC Actions:**
  - Provided yaml file for conda environment.
  - Enabled necessary modules and kernels.

### Jupyterhub and SSH Access
- **User Preference:** Primarily Jupyterhub, with SSH as a fallback.
- **HPC Actions:**
  - Set up Jupyterhub access with necessary kernels.
  - Provided SSH access as an alternative.

### Course Outcome
- **Success:** The course was successful. Students performed MD simulations, visualized results, and analyzed data using Python.
- **Feedback:** Positive feedback from participants.

### Future Course Planning
- **User:** Eduard Neu
- **Request:** Developing a more comprehensive course with additional funding.
- **Details:**
  - Including Linux, Bash scripting, and Python tutorials.
  - Hosting the course material on GitHub.

### NHR Interest
- **NHR:** Interested in hosting similar courses.
- **User:** Eduard Neu
- **Proposal:** Online course similar to current offerings, with a duration of 1-2 days.

## Conclusion
The HPC support team successfully facilitated the practical course by setting up the necessary accounts and environments. The course was a success, and there is interest in developing and hosting similar courses in the future.

## Keywords
- HPC Account Setup
- Conda Environment
- Jupyterhub
- SSH Access
- MD Simulations
- Python Analysis
- Course Development
- NHR Interest
```
---

### 2020051842002456_Up-to-date%20inventory_Overview%20computing%20clusters.md
# Ticket 2020051842002456

 ```markdown
# HPC-Support Ticket: Up-to-date Inventory/Overview Computing Clusters

## Keywords
- MD simulations
- Gromacs
- AMBER
- System properties
- Computing demands
- Forcefield
- Classical MD simulations
- Metadynamics
- Protein
- Membrane

## Summary
The HPC Admin sent an email to gather information about the system properties and computing demands of users performing MD simulations with Gromacs or AMBER. The user provided details about their simulation systems, forcefields, types of simulations, and system properties.

## User Information
- **System Size**: 65,000 to 80,000 atoms (typical), 120,000 atoms (specific project), 275,000 atoms (multiple systems)
- **Forcefields**: AMBER (ff14SB, lipid14, GAFF, GAFF2), ff99SB + GAFF (older projects)
- **Simulation Types**: Classical MD simulations, Metadynamics (using GROMACS patched with plumed)
- **System Properties**: Protein embedded in a membrane

## Lessons Learned
- Users perform MD simulations with varying system sizes, ranging from 65,000 to 275,000 atoms.
- AMBER forcefields are commonly used, with specific combinations for proteins, lipids, and small molecules.
- Both classical MD simulations and metadynamics are conducted.
- Protein-membrane systems are a common focus of research.

## Root Cause of the Problem
- The HPC Admin needed an overview of user requirements to prepare for future computing demands.

## Solution
- The user provided detailed information about their simulation systems, forcefields, and types of simulations, which will help the HPC Admin plan for future needs.
```
---

### 2020051842002518_Up-to-date%20inventory_Overview%20computing%20clusters.md
# Ticket 2020051842002518

 # HPC Support Ticket: Up-to-date Inventory/Overview Computing Clusters

## Keywords
- MD simulations
- Gromacs
- AMBER
- System properties
- Computing demands
- Forcefield
- Classical MD simulations
- Membrane
- Protein
- Water
- Ions (Fe, Na, K)

## Summary
- **Purpose**: Gain overview of system properties and computing demands for future preparation.
- **User Response**:
  1. System size: 315,471 atoms (typical for research).
  2. Forcefield: Charmm type parameter file(s).
  3. Simulation type: Classical MD simulations.
  4. System properties: Membrane with protein, water, and ions (Fe, Na, K).

## Root Cause
- No specific problem reported; the ticket was for gathering information.

## Solution
- User provided the required information for stock-taking.

## General Learnings
- Importance of gathering user data for future resource planning.
- Common system sizes and properties for MD simulations.
- Typical forcefields and simulation types used by researchers.

## Actions Taken
- Ticket closed after user provided the necessary information.

## Next Steps
- Use gathered data for future resource planning and optimization.
- Continue periodic stock-taking to stay updated on user needs.
---

### 2020051842002474_Up-to-date%20inventory_Overview%20computing%20clusters.md
# Ticket 2020051842002474

 ```markdown
# HPC-Support Ticket: Up-to-date Inventory/Overview Computing Clusters

## Keywords
- MD simulations
- Gromacs
- AMBER
- System properties
- Computing demands
- Forcefield
- Classical MD simulations
- Polymer system
- Fracture mechanics

## Summary
The HPC Admin sent an email to gather information about the system properties and computing demands of users performing MD simulations with Gromacs or AMBER. The user responded with details about their current and future system sizes, forcefields used, types of simulations, and system properties.

## User Information
- **System Size**: Current system contains 7000 atoms, future systems will have 60000 or even 200000 atoms.
- **Forcefield**: OPLS-AA Force Field + additional self-made parametrization in the LAMMPS code.
- **Simulation Type**: Classical MD simulations, multiple replica runs, and simulations with the colvars module.
- **System Properties**: Polymer system (epoxy), main topic is fracture mechanics.

## Root Cause of the Problem
The user is unsure about which machine their simulations should run on.

## Solution
No specific solution provided in the conversation. The user's response indicates a need for guidance on selecting the appropriate machine for their simulations.

## General Learnings
- Importance of gathering user requirements and system properties for future planning.
- Users may need guidance on selecting appropriate computing resources for their simulations.
- Understanding the types of simulations and forcefields used by users can help in optimizing HPC resources.
```
---

### 2023060742001694_Remote%20Visualization%20-%20VMD%20-%20AG%20Gmeiner.md
# Ticket 2023060742001694

 # HPC-Support Ticket: Remote Visualization

## Subject
Remote Visualization - VMD - AG Gmeiner

## Keywords
Remote Visualization, VMD, UCSF Chimera, PyMOL, X11-Forwarding, NHR, FAU

## Summary
User inquires about the possibility of using VMD, UCSF Chimera, or PyMOL over X11-Forwarding on NHR computers. HPC Admin responds that they are currently in the procurement phase and will provide an answer the following week. Later, it is clarified that VMD is not available.

## Conversation Details

### User
- **Initial Inquiry**: Asks about remote visualization options, specifically VMD, UCSF Chimera, or PyMOL via X11-Forwarding on NHR computers.
- **Follow-up**: Understands the delay and requests to be informed when the HPC team is less busy.

### HPC Admin
- **Initial Response**: Informs the user that they are in the procurement phase and will respond the following week.
- **Correction**: Clarifies that VMD is not available and will provide updates when there are new developments.
- **Internal Communication**: Notes that documentation for remote visualization is available, but VMD, UCSF Chimera, and PyMOL need internal review before recommending them to users.

## Root Cause of the Problem
User needs information on the availability and setup of remote visualization tools (VMD, UCSF Chimera, PyMOL) via X11-Forwarding on NHR computers.

## Solution
- HPC Admin will review the tools internally and provide updates to the user.
- Initial documentation for remote visualization is available, but specific tools need further evaluation.

## What Can Be Learned
- **Procurement Phase**: During the procurement phase, responses to user inquiries may be delayed.
- **Tool Availability**: Not all requested tools (e.g., VMD) are available, and internal review is necessary before recommending them.
- **Documentation**: Initial documentation for remote visualization is available, but specific tools require further internal evaluation.

## Next Steps
- HPC Admin to review VMD, UCSF Chimera, and PyMOL internally.
- Provide updates to the user once the review is complete.

## References
- [Remote Visualization Documentation](https://hpc.fau.de/systems-services/documentation-instructions/clusters/fritz-cluster/#remotevis)
---

### 2024062042001809_PyMOL%20License.md
# Ticket 2024062042001809

 ```markdown
# HPC-Support Ticket: PyMOL License

## Summary
A user inquired about access to a PyMOL license that would allow the use of PyMOL-generated graphics for publications. The user is part of the "SimMediSoft" project.

## Key Points Learned

### License Types
- **Teaching License**: The current PyMOL license at NHR@FAU is for teaching purposes only and explicitly prohibits the use of graphics for publications.
- **Research License**: The CCC has a license for the Schrödinger Suite, including PyMOL, which covers both teaching and research, but it is limited to specific groups within the university.

### Alternatives
- **Open-Source PyMOL**: There is an open-source version of PyMOL available on GitHub, which can be compiled locally. However, it has extensive dependencies and requires OpenGL, which can be challenging to run over X11/ssh forwarding.
- **Web-Based Visualization**: The MDsrv tool from Peter Hildebrand was suggested as an alternative for molecular dynamics visualization.

### Collaboration
- **Inter-Center Collaboration**: The HPC admin team collaborated with other NHR centers to check for available PyMOL licenses.
- **Vendor Cooperation**: Schrödinger was mentioned as being cooperative in licensing matters, suggesting a potential solution for NHR.

## Root Cause
The user needed a PyMOL license that allows the use of generated graphics for publications, but the current teaching license at NHR@FAU does not permit this.

## Solution
- **Short-Term**: The user was advised to use the web-based MDsrv tool for visualization.
- **Long-Term**: The HPC admin team is exploring the possibility of compiling the open-source version of PyMOL and addressing the dependencies and execution challenges. They are also considering contacting Schrödinger for a suitable license.

## Keywords
- PyMOL
- License
- Publications
- Open-Source
- MDsrv
- Schrödinger
- OpenGL
- X11/ssh forwarding
- NHR@FAU
- CCC
```
---

### 2020051842002545_Up-to-date%20inventory_Overview%20computing%20clusters.md
# Ticket 2020051842002545

 # HPC Support Ticket Conversation Analysis

## Subject: Up-to-date inventory/Overview computing clusters

### Keywords:
- MD simulations
- Gromacs
- AMBER
- System properties
- Computing demands
- Forcefield
- Classical MD simulations
- Replica exchange
- Plumed
- Metadynamics
- Membrane
- Metal
- Exotic ligands

### Summary:
- **Purpose**: Gain an overview of system properties and computing demands for MD simulations using Gromacs or AMBER.
- **Questions Asked**:
  1. System size (number of atoms) and typicality.
  2. Forcefield(s) used.
  3. Type of MD simulations (classical or other).
  4. Outstanding properties of the system.

### Root Cause of the Problem:
- No response from the user (Passainte Ibrahim).

### Solution:
- Follow up with the user to gather the required information.

### General Learnings:
- Importance of regular stock-taking to understand user needs and system usage.
- Necessity of user cooperation in providing information for better service planning.

### Next Steps:
- HPC Admins should send a reminder or follow-up email to the user.
- Consider alternative methods to gather information if no response is received.

---

This report provides a brief overview of the conversation and highlights key points for future reference in handling similar situations.
---

### 2020051842002616_Up-to-date%20inventory_Overview%20computing%20clusters.md
# Ticket 2020051842002616

 ```markdown
# HPC-Support Ticket Conversation: Up-to-date Inventory/Overview Computing Clusters

## Subject
Up-to-date inventory/Overview computing clusters

## Keywords
- MD simulations
- Gromacs
- AMBER
- System properties
- Computing demands
- Forcefield
- Classical MD simulations
- Replica exchange
- Plumed
- Metadynamics
- Membrane
- Metal
- Exotic ligands

## Summary
- **Purpose**: Gain a basic overview of system properties and computing demands for MD simulations using Gromacs or AMBER.
- **Questions Asked**:
  1. How many atoms does your current system have? Is this a typical system size for your research?
  2. Which forcefield(s) are you using?
  3. Are you conducting classical MD simulations? If not (e.g., replica exchange, plumed, metadynamics, etc.), please specify.
  4. Are there outstanding properties that describe your system best (e.g., membrane, metal, exotic ligands, etc.)?

## Root Cause of the Problem
- No response from the user.

## Solution
- No solution provided as there was no response from the user.

## General Learnings
- Importance of gathering user data for future resource planning.
- Types of MD simulations and forcefields used by researchers.
- Need for follow-up if no response is received.
```
---

### 2020051842002643_Up-to-date%20inventory_Overview%20computing%20clusters.md
# Ticket 2020051842002643

 ```markdown
# HPC Support Ticket Conversation: Up-to-date Inventory/Overview Computing Clusters

## Keywords
- MD simulations
- Gromacs
- AMBER
- System properties
- Computing demands
- Forcefields
- Classical MD simulations
- Membrane
- GPCR
- Ligand
- Effector protein

## Summary
The HPC Admin sent an email to gather information about the system properties and computing demands of users performing MD simulations with Gromacs or AMBER. The email was initially sent to an incorrect address, resulting in a delivery failure. The admin then forwarded the email to the correct address.

## Root Cause of the Problem
- Incorrect email address used initially, leading to delivery failure.

## Solution
- The admin forwarded the email to the correct address.

## Information Gathered
1. **System Size**: About 130,000 atoms, typical for the user's research.
2. **Forcefields**: Amber force fields gaff and ff99SB.
3. **Simulation Type**: Gaussian accelerated MD.
4. **System Properties**: Waterbox containing membrane, GPCR, ligand, and effector protein (G protein).

## General Learnings
- Importance of verifying email addresses before sending important communications.
- Understanding the typical system sizes and forcefields used by researchers helps in planning future HPC resources.
- Gathering information on simulation types and system properties aids in optimizing HPC services for specific research needs.
```
---

### 2020051842002563_Up-to-date%20inventory_Overview%20computing%20clusters.md
# Ticket 2020051842002563

 # HPC Support Ticket: Up-to-date Inventory/Overview Computing Clusters

## Keywords
- MD simulations
- Gromacs
- AMBER
- System properties
- Computing demands
- Forcefield
- Classical MD simulations
- Metadynamics
- Proteins
- Membrane

## Summary
- **Purpose**: Gain overview of system properties and computing demands for future preparation.
- **User Information**:
  - System size: ~200,000 atoms
  - Forcefield: AMBER99SB-ILDN
  - Simulation type: Classical MD, future metadynamics
  - System properties: Proteins embedded in a membrane

## Root Cause
- N/A (Informational ticket)

## Solution
- N/A (Informational ticket)

## General Learnings
- Users are running MD simulations with varying system sizes and forcefields.
- Future simulations may include advanced techniques like metadynamics.
- Understanding user needs helps in planning and preparing HPC resources.

## Next Steps
- Continue gathering information from other users.
- Use collected data to plan and optimize HPC resources.
---

