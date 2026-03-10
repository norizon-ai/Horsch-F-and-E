# Topic 25: stata_for_cluster_hpc_software

Number of tickets: 35

## Tickets in this topic:

### 2022032442001212_Early-Alex%20%22Nils%20Meyer%22%20_%20no%20HPC%20account.md
# Ticket 2022032442001212

 ```markdown
# HPC-Support Ticket Conversation Summary

## Subject: Early-Alex "Nils Meyer" / no HPC account

### Keywords:
- HPC account setup
- SSH key
- Multi-node jobs
- Module issues
- Performance comparison

### What Can Be Learned:
- **Account Setup**: Users need to provide an SSH public key for account setup.
- **Multi-Node Jobs**: Users can request multi-node jobs by specifying the required parameters in the job script.
- **Module Issues**: Certain modules may have issues with dependencies, such as missing library paths.
- **Performance Comparison**: Users may compare performance across different HPC clusters to determine the best fit for their workload.

### Conversation Summary:

#### Initial Request:
- **User**: Requested access to the GPGPU cluster 'Alex' for optimization of Lattice QCD codes.
- **HPC Admin**: Requested SSH public key for account setup.

#### Account Setup:
- **User**: Provided SSH public key.
- **HPC Admin**: Granted early-user access and provided login instructions.

#### Multi-Node Jobs:
- **User**: Requested multi-node job access.
- **HPC Admin**: Granted access and provided job script parameters for multi-node jobs.

#### Module Issues:
- **User**: Reported issues with compiling MPI hello world due to missing xpmem library.
- **HPC Admin**: Explained the issue with Spack and suggested a manual workaround.

#### Performance Comparison:
- **User**: Compared performance between Alex and JUWELS Booster.
- **HPC Admin**: Noted the performance difference and suggested using a different cluster for better multi-node performance.

### Root Cause of the Problem:
- **Module Issues**: The OpenMPI module built with Spack did not include the path to the xpmem library, causing compilation issues.

### Solution:
- **Manual Workaround**: Users can manually specify the library path using `-L $XPMEM_ROOT/lib` in their build process.
- **Performance Comparison**: Users should consider using clusters with better multi-node performance, such as the system at KIT with 167 GPU nodes.

### Additional Notes:
- **Documentation**: Users should refer to the cluster documentation for updates and additional information.
- **Future Access**: Users should submit an NHR-Rechenzeitantrag for long-term access to the cluster.
```
---

### 2018090642000791_Fwd%3A%20Re%3A%20Experiment%20with%20numa%20balancing.md
# Ticket 2018090642000791

 # HPC-Support Ticket: Experiment with NUMA Balancing

## Keywords
- NUMA balancing
- Test cluster
- HPC experiment
- Admin rights
- PBS Pro
- qsub
- qstat

## Summary
A user requested assistance to access the test cluster and perform experiments with NUMA balancing on/off. The user needed guidance on accessing the test cluster, running experiments, and changing NUMA balancing settings.

## Problem
- User needed access to the test cluster.
- User required instructions on how to connect to the test cluster and run experiments.
- User needed admin assistance to change NUMA balancing settings.

## Solution
1. **Accessing the Test Cluster:**
   - The frontend for accessing the test cluster is `testfront.rrze.uni-erlangen.de`.
   - Users can SSH directly to `testfront` if they are connected through VPN or cshpc.
   - Alternatively, users can SSH to `testfront` from LiMa.

2. **Running Experiments:**
   - On `testfront`, users need to load the `pbspro` module before using batch system commands:
     ```bash
     module load pbspro
     ```
   - To request the machine `hasep1`, users can use the following command:
     ```bash
     qsub -l nodes=hasep1:ppn=56 -l walltime=... -I
     ```

3. **Changing NUMA Balancing Settings:**
   - To switch on NUMA balancing:
     ```bash
     echo 1 > /proc/sys/kernel/numa_balancing
     ```
   - To switch off NUMA balancing:
     ```bash
     echo 0 > /proc/sys/kernel/numa_balancing
     ```
   - Admin rights are required to change these settings.

## Lessons Learned
- Users need clear instructions on how to access the test cluster and run experiments.
- Admin assistance is necessary for changing NUMA balancing settings.
- Proper module loading is essential for using batch system commands.

## Notes
- The user performed experiments with NUMA balancing on and off and requested admin assistance to change the settings.
- The admin reset the NUMA balancing setting to its default value after the experiments were completed.
---

### 42127266_Cluster.md
# Ticket 42127266

 # HPC-Support Ticket Conversation: Cluster

## Keywords
- Monte Carlo Simulation
- Virtual Machine
- Ubuntu
- RRZE-Cluster
- Parallelization
- IDM-Kennung
- HPC-Account
- Woodcrest-Cluster

## Summary
A user from the medical faculty at the University of Erlangen is working on Monte Carlo simulations and wants to run them on the RRZE-Cluster for faster computation. The user inquires about the process and potential costs.

## Root Cause
- User needs to run Monte Carlo simulations on the RRZE-Cluster.
- User is unsure about the process and costs involved.

## Solution
1. **Parallelization**: The HPC-Cluster can speed up simulations if the software is parallelized. If running multiple independent simulations, the cluster can handle them simultaneously.
2. **Costs**: No costs for research funded by the university or public grants. Special arrangements are needed for industry-funded projects.
3. **Access**:
   - Activate IDM-Kennung at RRZE service desks.
   - Apply for a separate HPC account using the provided form.
   - Detailed information on HPC systems available on the RRZE website.
   - The Woodcrest-Cluster is recommended for the user's computations.

## General Learnings
- **Parallelization Benefits**: HPC clusters can significantly speed up parallelized simulations.
- **Cost Structure**: Free for academic and publicly funded research, special arrangements for industry-funded projects.
- **Access Procedure**: Activate IDM-Kennung and apply for a separate HPC account.
- **Resource Information**: Detailed system descriptions are available on the RRZE website.

## References
- [IDM-Kennung Activation](https://www.helpdesk.rrze.uni-erlangen.de/otrs/public.pl?Action=PublicFAQZoom;ItemID=1099)
- [HPC Account Application](http://www.rrze.de/hilfe/service-theke/HPC-Antrag.pdf)
- [HPC Systems Description](http://www.hpc.rrze.de/systeme)
- [HPC Services](http://www.hpc.rrze.uni-erlangen.de/)
---

### 42048671_Antrag%20HPC-Berechnung.md
# Ticket 42048671

 # HPC Support Ticket: Antrag HPC-Berechnung

## Keywords
- HPC-Antrag
- FE-Berechnungen
- Radioss
- Optistruct
- CPU-Leistung
- Arbeitsspeicher
- Lizenzfragen
- MPI-Parallelisierung
- Speicherbedarf

## Summary
- **User Request**: The user wants to utilize the HPC service for finite element (FE) calculations using Radioss and Optistruct from Altair Engineering.
- **Requirements**:
  - Radioss (Explicit): High CPU performance.
  - Optistruct (Implicit): High memory requirements.
  - Jobs are submitted as text files, typically a few MB, occasionally up to 50 MB.
  - Local computation times range from a few hours to a maximum of one day.
  - No graphical user interface required; solvers can be started via command line.

## Actions Taken
- **HPC Admin**: Discussed the request with the user.
- **User**: Agreed to clarify license issues with Altair and check the possibility of MPI parallelization.
- **Typical Memory Requirement**: Up to 32 GB.

## Root Cause
- The user needs to perform computationally intensive FE calculations that require high CPU performance and significant memory.

## Solution
- The user will clarify license issues and check for MPI parallelization possibilities.
- The HPC team will assist in identifying suitable HPC systems based on the user's requirements.

## General Learnings
- Understanding the specific computational needs (CPU, memory) of different software tools is crucial for recommending appropriate HPC systems.
- License management and parallelization capabilities are important considerations for efficient use of HPC resources.
- Effective communication and collaboration between the user and HPC support team can help in resolving complex computational requirements.
---

### 2022120542003319_RE%3A%20Accounts%20for%20the%20NHR%40FAU%20cluster.md
# Ticket 2022120542003319

 # HPC Support Ticket Conversation Analysis

## Keywords
- Account creation
- SSH access
- OpenMPI installation
- Package installation
- Documentation
- Cluster access
- Job submission
- Interactive jobs

## General Learnings
- Users need to provide SSH public keys for account creation.
- Documentation for getting started, SSH access, and cluster-specific information is available.
- Users can access clusters via a dialog server and then SSH into specific clusters.
- Job submission and interactive job commands are provided in the documentation.
- Users may encounter issues with missing packages during software installation.

## Root Cause of the Problem
- User encountered errors while building OpenMPI due to missing libraries (`-lnuma`, `-liberty`, `-lz`).

## Solution
- User requested the installation of `binutils-devel`, `zlib-devel`, and `numactl-devel` packages on a node.
- HPC Admin suggested using Spack for package management and provided instructions for loading Spack modules.

## Support Team Involvement
- HPC Admins provided initial account setup and access instructions.
- 2nd Level Support team assisted with package installation and Spack usage.

## Documentation Links
- [Getting Started](https://hpc.fau.de/systems-services/documentation-instructions/getting-started/)
- [SSH Access](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/)
- [Fritz Cluster Info](https://hpc.fau.de/systems-services/documentation-instructions/clusters/fritz-cluster/)
- [Alex Cluster Info](https://hpc.fau.de/systems-services/documentation-instructions/clusters/alex-cluster/)
- [HPC in a Nutshell Slides](https://www.rrze.fau.de/files/2019/05/2019-04-26_HPC_in_a_Nutshell1.pdf)
- [Performance Counters and Profiling Tools Slides](https://moodle.nhr.fau.de/pluginfile.php/4426/mod_resource/content/2/Mucosim_WS22_23_Intro_and_LIKWID%2520-%2520NHR%2520-%2520Part%25201.pdf)

## Cluster Access Commands
- Access dialog server: `ssh cshpc.rrze.fau.de`
- Access Fritz cluster: `ssh fritz`
- Access Alex cluster: `ssh alex`
- Interactive job on Fritz: `salloc -N 1 --partition=singlenode --time=01:00:00`
- Interactive job on Alex with GPUs: `salloc -gres=gpu:a100:2 -p a100 -C a100_80 --time=01:00:00`

## Spack Usage
- Load Spack module: `module load user-spack`
- List installed Spack packages: `module load 000-all-spack-pkgs`

This analysis provides a summary of the support ticket conversation, highlighting key points and solutions for future reference.
---

### 2019090542002145_HPC.md
# Ticket 2019090542002145

 ```markdown
# HPC-Support Ticket Conversation Summary

## Keywords
- HPC Access for Non-FAU Members
- Costs and Financing
- Parallel Computing with R
- System Recommendations
- Parallelization Strategies

## General Learnings
- **HPC Access for Non-FAU Members**: Non-FAU members can access HPC services by filling out specific forms and having their identity verified by their home institution.
- **Costs and Financing**: Costs may be waived for academic projects with limited resource usage, especially if the results are to be published.
- **Parallel Computing with R**: The R package RSiena supports parallel computing, but the effectiveness depends on the type of parallelization (multi-threading vs. cluster computing).
- **System Recommendations**: For tasks that can be parallelized, systems like "Emmy" with many nodes are recommended. For simpler parallel tasks, "Woody" might be sufficient.
- **Parallelization Strategies**: Understanding the type of parallelization (trivial vs. dependent) is crucial for selecting the right HPC system and estimating performance gains.

## Root Cause of the Problem
- The user needed guidance on accessing HPC resources as a non-FAU member, understanding costs, and selecting the appropriate HPC system for their parallel computing needs with R.

## Solution
- **Access**: The user was directed to fill out the necessary forms and have their identity verified by their home institution.
- **Costs**: The HPC Admin indicated that costs might be waived if the resource usage is limited and the results are published.
- **System Recommendations**: The user was advised to use "Woody" for simpler parallel tasks and "Emmy" for more complex parallelization needs.
- **Parallelization Strategies**: The user was informed about the differences between trivial and dependent parallelization and how to estimate performance gains.

## Additional Notes
- The user was also informed about an upcoming event on HPC with R, which could provide further insights into parallel computing with R.
```
---

### 2020091442004374_Anfrage%20HPC%20Benutzung.md
# Ticket 2020091442004374

 # HPC Support Ticket Conversation Analysis

## Keywords
- HPC resources
- R program
- Simulation
- Cluster nodes
- HPC Antragsformular
- Woody
- TinyEth
- Security
- Data protection

## Summary
A doctoral student from the Institute for Medical Informatics, Biometry, and Epidemiology (IMBE) requests access to HPC resources to run simulations for their research project. The student has developed a serial algorithm in R and needs to process 1000 datasets, which would take approximately 11 days on their local PC. The student seeks to use multiple nodes of a cluster to expedite the process.

## Root Cause of the Problem
- The student needs to run extensive simulations that are time-consuming on a local PC.
- The local cluster is currently unavailable for long-term use.

## Solution Provided
- The HPC Admin advises the student to use the HPC Antragsformular to gain access to HPC resources.
- Recommended systems: Woody and TinyEth, which support R as a module.
- Note: The systems cannot be used for processing sensitive data, such as personal information.

## General Learnings
- HPC resources are available for free to FAU scientists for average resource usage in regular batch operations for scientific purposes.
- The HPC systems can significantly reduce the time required for extensive simulations by utilizing multiple nodes.
- Security guidelines must be followed, especially regarding the handling of sensitive data.

## Action Items
- The student should fill out the HPC Antragsformular to gain access to the HPC resources.
- The student should review the introduction and guidelines for using the HPC systems.

## Additional Notes
- The HPC Admin provides a link to the HPC Antragsformular and additional resources for getting started with HPC systems.
- The student should ensure that their data does not include sensitive information that is prohibited from being processed on the HPC systems.
---

### 2022030442001081_Anfrage%20CPU%20cluster.md
# Ticket 2022030442001081

 # HPC Support Ticket Conversation Analysis

## Keywords
- CPU cluster
- GPU cluster
- TensorFlow
- PYMC3
- Monte-Carlo sampling
- Interactive shell
- srun
- Resource allocation error
- Account/partition combination

## What Can Be Learned

### User Request
- The user has access to the Tiny GPU cluster and is satisfied with its performance for image analysis using TensorFlow.
- The user wants to move another project to a CPU cluster, which involves modeling population dynamics of Emperor Penguins using PYMC3 and Monte-Carlo sampling.
- The user is unsure about multi-node support for PYMC3 but believes it should work theoretically.

### HPC Admin Response
- The user already has access to all productive clusters.
- Meggie or TinyFAT clusters are recommended for the user's project.
- There was a bug in the database import that affected the user's account, which has been fixed.

### User Issue
- The user attempted to get an interactive shell using `srun` but encountered an error: `srun: error: Unable to allocate resources: Invalid account or account/partition combination specified`.
- The user assumed this was due to a lack of permissions.

### Solution
- The issue was caused by a bug in the database import, which has been resolved.
- The user should now be able to allocate resources without encountering the error.

## Root Cause of the Problem
- A bug in the database import affected the user's account, leading to resource allocation errors.

## Solution Found
- The bug was identified and fixed by the HPC Admin, allowing the user to allocate resources correctly.

## Documentation for Support Employees
If a user encounters resource allocation errors with `srun` due to an invalid account or account/partition combination, check for any recent database imports or updates that may have affected the user's account. If a bug is identified, fix it and notify the user that the issue has been resolved.
---

### 2019032642003008_Fragen%20zur%20Nutzung%20des%20HPC-Clusters.md
# Ticket 2019032642003008

 # HPC-Support Ticket Conversation Analysis

## Keywords
- HPC Cluster
- RASPA
- Monte Carlo Simulations
- Molecular Dynamics Simulations
- Parallelization
- Rechenzeitbedarf
- HPC-Basisdienst
- FAU
- Emmy Cluster
- Woody Cluster
- Tinyx Clusters

## General Learnings
- **HPC-Basisdienst**: Free for FAU scientists for scientific purposes.
- **Parallelization**: Important to know if the software is parallelized.
- **Cluster Choice**: Depends on the nature of the simulations (parallel vs. serial).
- **Antrag**: The target system is not crucial for the initial application.

## Root Cause of the Problem
- User is unsure about the suitability of the Emmy cluster for their simulations.
- User needs clarification on costs and application details.
- User's software (RASPA) is not parallelized, affecting the choice of cluster.

## Solution
- **Cluster Recommendation**: For non-parallelized simulations, Woody or Tinyx clusters are more suitable.
- **Costs**: HPC-Basisdienst is free for FAU scientists.
- **Application Details**: The target system is not crucial for the initial application.

## Conversation Summary
- **User**: Asks about using Emmy cluster for RASPA simulations, costs, and application details.
- **HPC Admin**: Clarifies that HPC-Basisdienst is free, asks about parallelization and rechenzeitbedarf.
- **User**: Confirms RASPA is not parallelized, unsure about rechenzeitbedarf.
- **HPC Admin**: Recommends Woody or Tinyx clusters for non-parallelized simulations, explains application details.

## Documentation for Support Employees
- **Cluster Choice**: For non-parallelized simulations, recommend Woody or Tinyx clusters.
- **Costs**: Inform users that HPC-Basisdienst is free for FAU scientists.
- **Application Details**: Explain that the target system is not crucial for the initial application.

---

This report provides a concise summary of the conversation, highlighting key points and solutions for future reference.
---

### 2021010742002464_Allgemeine%20Fragen%20zum%20HPC%20cluster.md
# Ticket 2021010742002464

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject: Allgemeine Fragen zum HPC cluster

### Keywords:
- HPC cluster
- Otto-Friedrich-Universität Bamberg
- Rechen- und Speicherkapazitäten
- Juniorprofessur
- Genetische Analysen
- CPU cycles
- Kosten
- Fachrichtung
- Storage-Kapazität
- Rechenbedarf
- Laufzeit
- Grundversorgung

### Summary:
A user inquires about the availability and usage of the HPC cluster for employees of the Otto-Friedrich-Universität Bamberg. The user is a postdoc at the University of St Andrews and is preparing for a job interview for a junior professorship at the University of Bamberg. They need information about the computational and storage capacities available for their research.

### Key Points Learned:
1. **Availability for Bamberg Employees**:
   - The HPC cluster is available for employees of the Otto-Friedrich-Universität Bamberg.
   - Additional access to the Linux-Cluster at LRZ in Garching is also provided.

2. **Costs**:
   - No costs for CPU cycles within the framework of publicly funded projects or projects financed by the University of Bamberg.
   - Equal treatment as FAU members for the basic provision.

3. **Fachrichtung**:
   - The field of study is irrelevant for access to HPC resources.

4. **Storage and Computational Requirements**:
   - Basic storage provision is up to 1TB.
   - Detailed requirements for memory, CPU cores, and job runtime need to be specified for a more accurate assessment.
   - Maximum queue time is 24 hours, but chained jobs are possible.

5. **Data Sensitivity**:
   - The user works with non-personal, freely available genetic and imaging data.
   - Password-protected access is required.

### Root Cause of the Problem:
- The user needs clarification on the availability and costs of using the HPC cluster for their specific research needs.

### Solution:
- The HPC Admins confirmed that the user's requirements can be met within the free basic provision.
- Detailed specifications of storage, memory, and computational needs were requested for a more precise assessment.

### Additional Notes:
- The user was advised to contact the HPC Admins for further details if they receive the job offer.
- The HPC Admins provided reassurance that the user's needs can be accommodated within the available resources.
```
---

### 42231221_HPC-Nutzung.md
# Ticket 42231221

 # HPC-Support Ticket Conversation: HPC-Nutzung

## Keywords
- HPC usage
- Masterarbeit
- GROMACS
- Job size
- Rechenzeit
- Speicherplatz
- LiMa
- Haswell-Knoten
- Woodcrest/Woody-Cluster
- module-System

## Summary
A user is writing their master's thesis and needs to use the HPC for simulations with GROMACS. They have questions about the job size, computation time, and storage space required.

## Root Cause
- Uncertainty about job size, computation time, and storage requirements for HPC usage.

## Solution
- **Job Size and Computation Time**: The user can leave these fields blank on the application.
- **Platform Selection**:
  - For larger molecule simulations, LiMa is recommended.
  - For smaller simulations that are difficult to parallelize, the new Haswell nodes in the Woodcrest/Woody-Cluster are suggested.
- **Account Access**: The user's account will be valid on all HPC systems, and GROMACS is available through the "module" system on all platforms.

## General Learnings
- Users can estimate job size and computation time as best as possible; precise values are not required.
- Different HPC platforms are suitable for different types of simulations.
- User accounts are valid across all HPC systems, and software like GROMACS is accessible through the module system.

## Next Steps
- The user should submit the application with estimated values for job size and computation time.
- The user can start using the recommended HPC platforms based on their simulation needs.

## Additional Notes
- The user's master's thesis is expected to be completed by March.
- The HPC Admins provided guidance on which platforms to use based on the type of simulations.

---

This report can be used as a reference for support employees to assist users with similar queries about HPC usage for simulations.
---

### 2022100542003644_Anfrage%20Altair%20auf%20HPC.md
# Ticket 2022100542003644

 ```markdown
# HPC Support Ticket: Running Altair Inspire and HyperWorks on HPC

## Keywords
- Altair Inspire
- HyperWorks
- Linux compatibility
- Licensing
- Batch mode
- Slurm scheduler
- HPC documentation

## Problem
- User inquires about running Altair Inspire and HyperWorks on the HPC system.

## Root Cause
- Uncertainty about software compatibility and licensing requirements for Altair Inspire and HyperWorks on the HPC system.

## Solution
- **General Requirements for Software on HPC:**
  1. Software must be compatible with Linux (RedHat Enterprise Linux RHEL 8.6 and/or Ubuntu 20.04).
  2. Software should not be node-locked; network licenses should be accessible from HPC systems.
  3. Software should operate in batch mode without requiring interactive inputs or GUIs.

- **Specific Considerations:**
  - Altair Inspire and HyperWorks solver components are likely HPC-compatible.
  - GUI-based functionalities and remote submissions through GUIs will not work.
  - Licensing details (e.g., per instance, per core) need to be verified by the user.

- **Documentation and Resources:**
  - [RWTH Aachen HPC Documentation for HyperWorks](https://help.itc.rwth-aachen.de/en/service/rhr4fjjutttf/article/eebf6b7f13724e57a47f638047aaca8c/)
  - [Cirrus Documentation for Altair HyperWorks](https://cirrus.readthedocs.io/en/main/software-packages/altair_hw.html)

## Conclusion
- The feasibility of running Altair Inspire and HyperWorks on the HPC system depends on meeting the general requirements and specific considerations outlined.
- Users should refer to the provided documentation for more detailed information.
```
---

### 2024041942005241_AW%3A%20NHR%20-%20Hochleistungsrechner%20der%20FAU%20-%20Stata%20_%20LS%20B%C3%83%C2%BCttner%20%28ws.md
# Ticket 2024041942005241

 # HPC Support Ticket Conversation Summary

## Keywords
- HPC
- Stata
- Licensing
- R
- Python
- Data Storage
- Access
- SSH
- Slurm
- Project Creation
- HPC Introduction

## General Learnings
- The HPC systems do not come with licenses for any application software. Users need to take care of required licenses themselves.
- Stata licenses are available through the software team, and users should check for the latest options regarding Stata/MP.
- The appropriate target system for Stata is "Woody," unless Stata has recently learned to use GPUs.
- Access to HPC systems is via SSH, and location does not matter. Windows users can use MobaXterm.
- Operation of HPC systems is in batch mode using Slurm as the scheduler.
- New projects need to be created in the HPC portal as a first step.
- Monthly introductions to HPC are offered via Zoom.
- Large data should not be stored in `/home/hpc/`. Instead, use `$WORK` (without backup) or `$HPCVAULT` (with backup and snapshots).
- Stata/MP licenses can be procured by contacting the software team, and the cost varies based on the number of processors.

## Root Causes and Solutions
- **Stata Licensing**: The HPC systems do not provide Stata licenses. Users need to procure them through the software team.
  - **Solution**: Contact the software team to purchase the required Stata/MP license.
- **Data Storage Limitation**: The user encountered a storage limit in `/home/hpc/`.
  - **Solution**: Use `$WORK` for large data without backup or `$HPCVAULT` for data with backup and snapshots.
- **Stata/MP License Procurement**: The user requested a Stata/MP4 license for their project.
  - **Solution**: Contact the software team to purchase the Stata/MP4 license, ensuring it is compatible with the HPC environment.

## Additional Notes
- Users can conduct analyses in R or Python if difficulties with Stata are encountered.
- The next HPC introduction session is on June 12th, and slides from previous sessions are available online.
- The HPC portal and documentation provide detailed information on access, data storage, and batch processing.

This summary provides a concise overview of the key points and solutions discussed in the HPC support ticket conversation.
---

### 2023052642001481_Stata%20MP.md
# Ticket 2023052642001481

 # HPC-Support Ticket: Stata MP Availability

## Keywords
- Stata MP
- Stata SE
- Multi-core operations
- Large datasets
- Regression analysis
- Software availability

## Summary
A user inquired about the availability of Stata MP for multi-core operations, as they need to merge, process, and perform regression analysis on large datasets. The current system only offers Stata SE, which does not support multi-core operations. There is an indication that Stata MP might become available soon through a collaboration with another university.

## Root Cause
- The current HPC system only provides Stata SE, which lacks multi-core support.

## Solution
- No immediate solution provided.
- Potential future availability of Stata MP through collaboration with another university.

## What Can Be Learned
- Stata SE is currently available but lacks multi-core support.
- There is a potential for Stata MP to be available in the future.
- Users requiring multi-core operations for large datasets should be informed about the current limitations and future possibilities.

## Next Steps
- Monitor for updates on the availability of Stata MP.
- Inform users about the current limitations of Stata SE and the potential future availability of Stata MP.

## Relevant Contacts
- HPC Admins: Thomas, Michael Meier, Anna Kahler, Katrin Nusser, Johannes Veh
- 2nd Level Support Team: Lacey, Dane (fo36fizy), Kuckuk, Sebastian (sisekuck), Lange, Florian (ow86apyf), Ernst, Dominik (te42kyfo), Mayr, Martin
- Head of the Datacenter: Gerhard Wellein
- Training and Support Group Leader: Georg Hager
- NHR Rechenzeit Support: Harald Lanig
- Software and Tools Developer: Jan Eitzinger, Gruber
---

### 2020121042001485_HPC%20Access%20-%20Austin%20Rettinghouse.md
# Ticket 2020121042001485

 # HPC Support Ticket Conversation Summary

## Subject: HPC Access - User Request

### Keywords:
- HPC Access
- Remote Access
- RStudio
- Batch Mode
- Computing Power
- CIP Pool
- GCM Model
- Data Processing

### General Learnings:
- **HPC Access**: Understanding the criteria for granting HPC access, including the importance of main affiliation over place of residence.
- **Remote Access**: HPC systems are accessed remotely via SSH, making physical proximity irrelevant.
- **Batch Mode**: HPC systems operate in batch mode, not suitable for interactive GUI applications like RStudio.
- **Alternative Solutions**: Exploring remote access to CIP pool computers for interactive work, ensuring compliance with licensing agreements.

### Root Cause of the Problem:
- User requires more computing power for processing large datasets in RStudio.
- User's personal computer lacks sufficient resources to handle the data.
- Misunderstanding about the suitability of HPC systems for interactive applications.

### Solution:
- **Remote Access to CIP Pool**: Check with CIP admins if remote access to Linux-based computers in the CIP pool is possible.
- **Batch Mode Processing**: If interactive work is not necessary, use plain R in batch mode on HPC systems.
- **Consultation with Supervisor**: Discuss with the thesis supervisor to ensure the necessity of HPC access and explore alternative solutions.

### Conversation Summary:
- User requested HPC access at ZIB due to relocation but was denied.
- User faced computing power issues with RStudio on personal computer.
- HPC Admin suggested remote access to CIP pool computers if they run Linux.
- User's supervisor advised against HPC access, suggesting the data should be manageable on a regular laptop.
- HPC Admin clarified that HPC systems operate in batch mode and are not suitable for interactive applications like RStudio.

### Next Steps:
- User to contact CIP admins to check remote access possibility.
- User to provide more details on the planned work to determine if batch mode processing is feasible.
- User to discuss with supervisor to ensure the necessity of HPC access.

### Additional Notes:
- HPC access is granted based on main affiliation, not place of residence.
- HPC systems are accessed remotely via SSH, making physical proximity irrelevant.
- Interactive applications like RStudio are not suitable for HPC systems operating in batch mode.

This summary provides a concise overview of the support ticket conversation, highlighting key learnings, the root cause of the problem, and potential solutions. It serves as a reference for support employees to address similar issues in the future.
---

### 2022082242000815_Serverkapazit%C3%83%C2%A4ten%20f%C3%83%C2%BCr%20FEniCS-Simulationen.md
# Ticket 2022082242000815

 # HPC-Support Ticket Conversation: Serverkapazitäten für FEniCS-Simulationen

## Keywords
- FEniCS
- FEM-Simulationen
- Linux
- OS X
- Unix
- Windows
- Woody-NG
- FAU
- RRZE
- HPC-Antrag
- Grundversorgung
- Rechenzeit
- Speicherplatz

## Summary
A user from the Chair of Electronic Components (AG Prof. Dr. Nagy) at FAU requests access to HPC resources for FEM simulations using the FEniCS Python package. The user previously used a workstation with 16 cores and 256GB RAM at the Max Planck Institute for the Physics of Light, which is currently unavailable. The user needs to run multiple simulations over a few weeks and seeks guidance on estimating job size, total compute time, and storage requirements.

## Problem
- User needs access to HPC resources for FEM simulations using FEniCS.
- Previous workstation unavailable.
- Uncertainty about job size, compute time, and storage requirements.

## Solution
- HPC Admin suggests filling out the HPC application form and provides documentation links.
- Woody-NG system is recommended.
- No costs for usage within FAU's basic provision for fundamental research and public research projects.
- Typical job size: Single-Node.
- Total compute time: Rough estimate of the number of nodes per simulation * duration of a simulation * number of simulations.
- Storage: Standard quota on $WORK is 500 GB.
- FEniCS is suitable for the application.
- Even a few thousand hours of compute time are feasible within the basic provision.

## Conversation Details
1. **User Request:**
   - Requests access to HPC resources for FEM simulations using FEniCS.
   - Previously used a workstation with 16 cores and 256GB RAM.
   - Needs to run multiple simulations over a few weeks.

2. **HPC Admin Response:**
   - Suggests filling out the HPC application form.
   - Provides documentation links.
   - Recommends Woody-NG system.
   - No costs for usage within FAU's basic provision.
   - Provides guidance on estimating job size, compute time, and storage.

3. **User Follow-up:**
   - Asks about potential costs for using Woody-NG for a month.
   - Seeks advice on estimating job size, compute time, and storage.

4. **HPC Admin Clarification:**
   - Confirms no costs for usage within FAU's basic provision.
   - Provides rough estimates for job size, compute time, and storage.
   - Assures that even a few thousand hours of compute time are feasible.

## Conclusion
The user is guided through the process of applying for HPC resources, with specific recommendations for the Woody-NG system. The HPC Admin provides assurance that the user's compute time and storage requirements are within the basic provision, and no additional costs will be incurred.
---

### 2024031142000431_Simulation%20mit%20Blender%3F%20-%20CRT_iwc1.md
# Ticket 2024031142000431

 # HPC Support Ticket: Simulation with Blender

## Keywords
- Blender
- Simulation
- Particle Packing
- CPU-only
- Apptainer
- Spack
- Woody Icelake
- HPC-Portal

## Problem
- User wants to run Blender simulations on HPC system for particle packing.
- Blender is not listed in the software list.
- User needs guidance on the suitable HPC system and installation method.

## Solution
- **Software Installation**: Blender can be installed via Apptainer (recommended) or Spack package manager.
- **Cluster Recommendation**: Woody Icelake is suggested for CPU-only tasks.
- **Alternative Software**: An alternative software developed by a FAU Lehrstuhl is available.
- **HPC-Portal**: The user's project (iwc1*) needs a PI to be assigned in the HPC-Portal. The PI (Prof. Wasserscheid) needs to log in to the portal for project allocation.

## Further Actions
- User will motivate the PI to log in to the HPC-Portal.
- HPC Admins will assist with any further support needed for Blender installation and usage.

## General Learnings
- Blender can be used for particle packing simulations on HPC systems.
- Apptainer is the recommended method for installing software not listed in the HPC software list.
- Woody Icelake is suitable for CPU-intensive tasks.
- Proper project allocation in the HPC-Portal is necessary for accessing HPC resources.
---

### 2018091942000828_Beratung%20f%C3%83%C2%BCr%20die%20Nutzung%20HPC.md
# Ticket 2018091942000828

 # HPC-Support Ticket Conversation Analysis

## Keywords
- HPC Support
- Beratung
- Hochleistungsrechner
- RRZE
- BMW Group
- Optimierungsproblem
- Roboteranlagen
- C++
- Visual Studio
- Linux
- Batchqueuingsystem
- Woody-Cluster
- MKL-Bibliothek
- SIMD-Eigenschaften
- OpenMP
- std::thread
- Kostenbeitrag
- HPC-Antragsformular

## General Learnings
- **Commercial Use**: Commercial projects may require a cost contribution for HPC resources.
- **Software Compatibility**: Ensure software can be compiled and run on Linux with GNU or Intel compilers.
- **Resource Requirements**: Understand the memory and parallelism needs of the project.
- **Job Limitations**: Jobs have a maximum runtime of 24 hours; checkpoint-restart may be necessary for longer jobs.
- **Threading**: Use of std::thread for threading instead of OpenMP due to overhead concerns.
- **Optimization**: Consider using optimized libraries like MKL for performance improvements.
- **Application Form**: Submit the HPC application form, stamped and signed by the supervisor.

## Root Cause of the Problem
- The user's project has commercial interests, which affects the cost of using HPC resources.
- The user's software needs to be compatible with the Linux environment and batch queuing system.

## Solution
- **Cost Contribution**: Discuss a pauschalierter Kostenbeitrag for commercial use.
- **Software Adaptation**: Ensure the software can be compiled with GNU or Intel compilers and runs without user interaction.
- **Resource Allocation**: Use the Woody-Cluster for single-node throughput jobs.
- **Form Submission**: Complete and submit the HPC application form with the necessary signatures.

## Documentation for Support Employees
- **Commercial Projects**: Always clarify the commercial nature of the project to determine cost implications.
- **Software Requirements**: Ensure users adapt their software for Linux and batch queuing systems.
- **Resource Planning**: Understand the user's resource needs to recommend the appropriate HPC cluster.
- **Formal Procedures**: Guide users through the formal application process, including form submissions and necessary approvals.
---

### 2018121042000525_WG%3A%20Frage%20in%20Bezug%20auf%20M%C3%83%C2%B6glichkeiten.md
# Ticket 2018121042000525

 # HPC-Support Ticket Conversation Analysis

## Keywords
- HPC Cluster
- Stata
- Licensing
- Parallel Computing
- Job Management
- Software Installation

## Summary
A user inquires about the possibility of speeding up the computation of multiple models using Stata on the HPC cluster. The main concern revolves around licensing issues and the feasibility of running Stata on the HPC system.

## Root Cause of the Problem
- The user needs to compute multiple models, each taking 24-48 hours on regular computers.
- The user is concerned about the licensing requirements for Stata on the HPC cluster.

## Key Points Learned
- **HPC Cluster Performance**: The individual nodes in the HPC cluster are not faster than well-equipped servers. The advantage lies in running multiple jobs simultaneously.
- **Licensing Issues**: Stata requires a license for each instance, which can be a limiting factor. The user needs to purchase Stata MP licenses directly from DPC.
- **Parallel Computing**: If the models are independent, they can be computed simultaneously on the HPC cluster, significantly reducing the overall computation time.
- **Account Application**: To access the HPC cluster, the user needs to apply for an HPC account.
- **Software Installation**: Stata is not currently installed on the HPC cluster, and additional clarification is needed regarding its functionality and licensing on the cluster.
- **Alternative Software**: The use of R is suggested as an alternative to Stata to avoid licensing issues.

## Solution
- The user needs to purchase Stata MP licenses and ensure they are compatible with the HPC cluster.
- The user should apply for an HPC account to gain access to the cluster.
- The user can consider using R as an alternative to Stata to avoid licensing complications.

## Additional Notes
- The HPC admins provide detailed information on the licensing costs and types available for Stata MP.
- The HPC admins suggest that the user can use multiple single-user licenses to run parallel jobs, but this needs to be managed carefully to avoid exceeding the license limits.

This analysis provides a comprehensive overview of the issues and solutions discussed in the HPC-Support Ticket conversation, which can be used as a reference for similar inquiries in the future.
---

### 42132743_Question%20concerning%20Application%20for%20HPC%20Resources.md
# Ticket 42132743

 # HPC Support Ticket Conversation Analysis

## Keywords
- HPC Resources Application
- Gaussian 09
- ORCA
- Transition Metal Complexes
- Actinide Complexes
- Geometry Refinement
- Electronic Structure Calculations
- Job Size
- Disk Storage
- University Email Address
- Compute Needs Estimation
- Software Scalability

## Summary
A postdoctoral fellow inquires about the typical job size and required disk storage for an HPC resources application, specifically for using Gaussian 09 and ORCA for transition metal and actinide complex calculations. The HPC admin provides guidance on estimating compute needs and suggests consulting with colleagues who have similar experience. The admin also notes that Gaussian and ORCA do not scale well on modern clusters.

## Root Cause of the Problem
- User seeks guidance on estimating job size and disk storage for HPC application.
- User is unsure about the typical compute needs for their specific calculations.

## Solution
- The HPC admin advises the user to provide a rough estimate of compute needs for the foreseeable future.
- The user is encouraged to consult with colleagues who have experience with similar calculations.
- The admin notes that Gaussian and ORCA may not scale well on modern clusters, implying potential limitations in their use.

## General Learnings
- Always use your university email address for support requests.
- Provide rough estimates of compute needs when applying for HPC resources.
- Consult with colleagues who have experience with similar calculations for better estimates.
- Be aware that some software may not scale well on modern HPC clusters.

## Next Steps
- The user should gather more information from colleagues and provide a rough estimate of compute needs in the application.
- The user should be prepared for potential scalability issues with Gaussian and ORCA.
---

### 2023112742002001_Using%20the%20NHR%40FAU%20clusters%20%5Bc102fd10%5D.md
# Ticket 2023112742002001

 ```markdown
# HPC Support Ticket Conversation Summary

## Subject: Using the NHR@FAU clusters [c102fd10]

### Keywords:
- SSH Configuration
- Gromacs Job Scripts
- Account Management
- GPU Cluster
- Data Transfer

### General Learnings:
- Proper SSH configuration is crucial for accessing different clusters.
- Gromacs job scripts require specific adjustments for GPU usage.
- Account management and validity extensions can be handled by the user through the portal.
- Data transfer issues can arise due to incorrect rsync commands and file overwrites.
- Gromacs command parameters need to be correctly set for GPU usage.

### Issues and Solutions:

1. **SSH Configuration for Cluster Access:**
   - **Issue:** User unable to access Fritz cluster.
   - **Solution:** Provided SSH configuration documentation for jumping from cshpc to the Fritz cluster.

2. **Gromacs Job Scripts:**
   - **Issue:** User's job script not working correctly.
   - **Solution:** Provided templates for Gromacs job scripts and specific command-line parameters for GPU usage.

3. **Account Management:**
   - **Issue:** User's account expired.
   - **Solution:** Extended account validity and provided instructions for self-management through the portal.

4. **Data Transfer Issues:**
   - **Issue:** User unable to copy data directly to Alex cluster.
   - **Solution:** Suggested using csphc.rrze.fau.de as an intermediary due to shared file system.

5. **Gromacs Command Parameters:**
   - **Issue:** Incorrect Gromacs command parameters leading to job failures.
   - **Solution:** Provided corrected command parameters and environment variables for GPU usage.

### Root Causes:
- Incorrect SSH configuration.
- Incorrect Gromacs job script parameters.
- Expired account validity.
- Incorrect data transfer commands.
- Incorrect Gromacs command parameters.

### Solutions:
- Provided SSH configuration documentation.
- Provided Gromacs job script templates and specific command-line parameters.
- Extended account validity and provided self-management instructions.
- Suggested using csphc.rrze.fau.de for data transfer.
- Provided corrected Gromacs command parameters and environment variables.

### Additional Notes:
- User was advised to manage account validity through the portal.
- User was advised to copy only necessary files to the local SSD to avoid performance issues.
- User was advised to check Gromacs error output for troubleshooting.

### Documentation Links:
- [SSH Configuration](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/#ssh_config_hpc_portal)
- [Gromacs Job Scripts](https://hpc.fau.de/systems-services/documentation-instructions/special-applications-and-tips-tricks/gromacs/#collapse_1)

### Conclusion:
The user was able to resolve the issues with the help of the provided documentation and specific instructions. The solutions provided will be useful for future reference in solving similar errors.
```
---

### 2018120742001307_Frage%20in%20Bezug%20auf%20M%C3%83%C2%B6glichkeiten.md
# Ticket 2018120742001307

 # HPC-Support Ticket Conversation Analysis

## Keywords
- HPC Cluster
- Stata
- Licensing
- Parallel Computing
- Job Queuing
- RAM Requirements

## Summary
A user needs to compute approximately 100 models, each taking 24-48 hours on regular computers, using Stata. The user inquires about the feasibility of using HPC clusters to speed up the process.

## Root Cause of the Problem
- The user's models are computationally intensive and would take a significant amount of time on regular computers.
- The user is unsure about the availability and licensing of Stata on HPC clusters.

## Key Points Learned
- **HPC Cluster Capabilities**: The HPC cluster can run multiple models simultaneously, reducing the overall computation time.
- **Licensing Issues**: Stata licensing is a limiting factor. The user needs to acquire multiple licenses to run models in parallel.
- **Job Queuing**: The HPC cluster uses a batch queuing system, which does not support interactive inputs during job execution.
- **Job Duration**: Each job has a maximum runtime of 24 hours. Longer jobs need to be split into smaller parts.
- **RAM Requirements**: The user needs to specify the RAM requirements for each model.

## Solution
- **Licensing**: The user can either purchase Stata MP licenses for faster computation or use multiple single-core licenses to run models in parallel.
- **Account Application**: The user needs to apply for an HPC account to gain access to the cluster.
- **Job Submission**: The user should ensure that each job can run within the 24-hour limit and that all necessary inputs are provided at the start.

## Additional Notes
- The HPC cluster is not inherently faster than a well-equipped server, but it allows for parallel processing of multiple models.
- The user should coordinate with the software group to ensure proper licensing and installation of Stata on the HPC cluster.

## Conclusion
The user can significantly reduce the computation time by utilizing the HPC cluster, provided they address the licensing and job duration constraints.
---

### 2024050242003236_Re%3A%20New%20invitation%20for%20%22Studentische%20Abschlu%C3%83%C2%9Farbeiten%20Tier3%20Grundversor.md
# Ticket 2024050242003236

 # HPC Support Ticket Conversation Analysis

## Keywords
- HPC access
- SSH setup
- Cluster connection (Woody, Tinyx, Alex, Fritz)
- GPU resources
- Job allocation
- Interactive jobs (salloc)
- Batch jobs (sbatch)
- Resource availability
- Group resource limits

## Summary
A user requested HPC access and successfully set up SSH but encountered issues connecting to specific clusters and running GPU jobs.

## Root Cause of the Problem
- **Cluster Access**: The user does not have access to Alex and Fritz clusters by default with a Tier3 account.
- **Job Allocation**: The user's interactive job (salloc) is pending due to resource unavailability or high load on the cluster.

## Solution
- **Cluster Access**: Tier3 accounts do not have access to Alex and Fritz clusters by default.
- **Job Allocation**:
  - Use `sinfo.tinygpu` to check for free nodes.
  - Consider using batch jobs (sbatch) instead of interactive jobs (salloc) for better resource management and to run jobs outside working hours.
  - Note the limit of 5 A100 GPUs that can be used concurrently by all users in the group.

## General Learnings
- **Cluster Access**: Different account tiers have different default access to clusters.
- **Job Management**: Interactive jobs run only when resources are available, while batch jobs can run anytime and are more suitable for production work.
- **Resource Limits**: There are group-specific resource limits that can affect job allocation.

## Recommendations
- For cluster access issues, verify the account tier and default access permissions.
- For job allocation issues, recommend using batch jobs and checking resource availability with appropriate commands.
- For resource limits, be aware of group-specific restrictions and plan job submissions accordingly.
---

### 2021020542002117_Anfrage%20Servernutzungsm%C3%83%C2%B6glichkeiten.md
# Ticket 2021020542002117

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Keywords
- HPC Cluster
- STATA
- Data Storage
- Batch Processing
- Linux
- Speicherplatz
- Lizenzierung
- Antragsformulare
- Identitätsmanagement
- DFN-Videoident

## Problem
- User requires external storage and processing capabilities for large datasets (110 GB raw data, 10 GB analysis data, 10 GB regional variables).
- Current hardware (Lenovo ThinkPad T470s) is insufficient for data processing.
- User uses STATA for data analysis.

## Solution
- HPC Cluster usage is possible for data analysis.
- Systems run on Linux and use a batch/queueing system.
- Standard storage: 50 GB Home-Verzeichnis, 200 GB Work-Verzeichnis.
- Clusters 'woody' or 'TinyEth' are suitable for the user's needs.
- Licensing: Only serial version of STATA available; additional licenses needed for parallel processing.
- HPC-Basisdienst is free for University Bamberg members.
- Necessary forms for Identitätsmanagement and HPC usage provided.
- Identity verification can be done via DFN-Videoident.

## General Learnings
- HPC clusters can be used for external data storage and processing.
- Batch processing systems require non-interactive job submissions.
- Storage quotas and backup policies vary by system.
- Specific clusters may be recommended based on user needs.
- Licensing for commercial software must be considered.
- Identity verification and form submissions are required for HPC access.
```
---

### 2022081242000218_Request%20for%20multi-node%20job%20on%20Alex.md
# Ticket 2022081242000218

 # HPC Support Ticket Conversation Summary

## Keywords
- Multi-node job
- SSH key configuration
- Resource allocation
- Priority and queue management
- File ownership and permissions
- Maintenance and directory relocation

## General Learnings
- **Multi-node Job Submission**: Use `--qos=a100multi` for multi-GPU jobs to ensure exclusive node allocation.
- **SSH Key Configuration**: Modify `~/.ssh/config` to use wildcards for hostnames to avoid password prompts during SSH within multi-node jobs.
- **Resource Allocation**: Understand that interactive jobs may be refused if there are other jobs in the queue with higher priority.
- **File Ownership**: Maintenance operations may affect file ownership; administrators can correct this by changing ownership back to the user.
- **ClusterCockpit Application**: Useful for monitoring job details, but currently lacks a feature to display total time left for resource utilization.

## Root Causes and Solutions
- **SSH Key Issue**:
  - **Root Cause**: SSH key not being recognized across nodes.
  - **Solution**: Modify `~/.ssh/config` to include wildcards for hostnames and ensure the key is named correctly.

- **Resource Allocation Error**:
  - **Root Cause**: Interactive job requesting immediate execution while other jobs are in the queue.
  - **Solution**: Understand that interactive jobs may be refused if there are other jobs with higher priority.

- **File Ownership Issue**:
  - **Root Cause**: Maintenance operation relocated directories and changed ownership to root.
  - **Solution**: Administrator corrected the ownership of the files.

- **ClusterCockpit Limitations**:
  - **Root Cause**: ClusterCockpit does not display total time left for resource utilization.
  - **Solution**: Acknowledge the limitation and wait for future updates.

## Additional Notes
- **A100 GPU Access**: Users can specify `--constraint=a100_40` or `a100_80` to select 40GB or 80GB A100 GPUs.
- **Maintenance Impact**: Maintenance operations can affect file ownership; users should report any issues to the support team.

This summary provides a concise overview of the key issues and solutions discussed in the HPC support ticket conversation. It can serve as a reference for support employees to address similar issues in the future.
---

### 2024120742000029_Assistance%20Needed%20for%20HPC%20Cluster%20Access%20and%20Batch%20Job%20Submission.md
# Ticket 2024120742000029

 # HPC Support Ticket Conversation Summary

## Keywords
- HPC Cluster Access
- Batch Job Submission
- SSH Login
- SLURM
- GPU Resources
- Job Script
- Memory Allocation
- Module Availability

## Problem Root Cause
- User encountered issues with SSH login due to incorrect hostname.
- User needed guidance on submitting batch jobs, specifically for GPU-intensive tasks.
- User's job script required minor adjustments to align with cluster requirements.

## What Can Be Learned
- **SSH Login**: Users should connect to the correct frontend of the cluster they intend to use.
- **Job Script**: Users should avoid using the `--mem` option on most clusters, as memory is automatically assigned based on requested GPUs or CPUs.
- **Module Availability**: Users should check available modules using `module avail`.
- **Job Submission**: Users can submit jobs using SLURM commands and monitor them with `squeue`.

## Solution
- **SSH Login**: Use the correct hostname for the cluster frontend, such as `csnhr.nhr.fau.de` for TinyGPU.
- **Job Script**: Remove the `--mem` option and ensure the script aligns with the cluster's available modules.
- **Job Submission**: Submit jobs using `sbatch` and monitor them with `squeue`.

## Additional Resources
- [SSH Command Line Guide](https://doc.nhr.fau.de/access/ssh-command-line/)
- [HPC Cluster Overview](https://doc.nhr.fau.de/clusters/overview/)
- [Job Script Examples](https://doc.nhr.fau.de/batch-processing/job-script-examples-slurm/)
- [HPC Café for New Users](https://hpc.fau.de/teaching/hpc-cafe/)

## Example Job Script
```bash
#!/bin/bash -l
#SBATCH --job-name=whisper_finetune
#SBATCH --output=whisper_finetune.out
#SBATCH --gres=gpu:2
#SBATCH --time=10:00:00
#SBATCH --cpus-per-task=8

module load python/3.9
module load cuda/11.7
source activate whisper-env

python whisper_finetune.py
```

## General Guidance
- Ensure users are aware of the correct hostnames for cluster frontends.
- Provide clear instructions on job script requirements and module availability.
- Encourage users to attend introductory sessions for new users.
---

### 2022121342001252_Compute-%20und%20Storageressourcen%20f%C3%83%C2%BCr%20CIP-Pool%20Physik.md
# Ticket 2022121342001252

 # HPC Support Ticket Conversation Analysis

## Keywords
- CIP-Pool Physik
- Rechennodes
- Massenspeicher
- HPC-Ressourcen
- Studierende
- Home-Verzeichnis
- SSD-Array
- RRZE/HPC
- Quota
- Zoom-Meeting

## Summary
The user is planning a CIP-Antrag for the CIP-Pool Physik and inquires about the possibility of using HPC resources for compute nodes and mass storage.

### Root Cause of the Problem
1. **Compute Nodes for Study Purposes**: The user wants to know if HPC resources can be used for compute nodes for students to gain experience with complex calculations.
2. **Mass Storage**: The user needs a solution for mass storage as their current setup is not desired anymore and they need to migrate to RRZE/HPC offerings.

### Solution
- **Compute Nodes**: HPC resources are only available for Lehrstühle and specific projects, not for general student use.
- **Mass Storage**: Mass storage capacities are only provided in conjunction with HPC projects. The user is advised to contact the Linux-Gruppe of RRZE for further assistance.

## General Learnings
- HPC resources are restricted to specific projects and Lehrstühle.
- Mass storage is tied to HPC projects and not available for general use.
- For general IT support, users should contact the Linux-Gruppe of RRZE.

## Next Steps
- The user should contact the Linux-Gruppe of RRZE (rrze-linux@fau.de) for further assistance with their requirements.

## Additional Notes
- The HPC Admin suggests that the user contact the Linux-Gruppe of RRZE for more appropriate support.
- A Zoom meeting was offered by the user for further discussion but was not pursued due to the limitations of HPC services.

---

This report provides a concise summary of the conversation and the key points to be learned for future reference.
---

### 2020091142002998_HPC-Nutzung%20f%C3%83%C2%BCr%20eine%20Simulation%20mit%20Software%20R.md
# Ticket 2020091142002998

 # HPC-Support Ticket Conversation Summary

## Keywords
- HPC-Support
- R Software
- Parallelization
- Kreuzvalidierung
- Batch-Queuingsystem
- Woody-Cluster
- TinyEth
- Datentransfer
- scp
- 24h Job Limit
- R-Pakete
- JAGS

## General Learnings
- **R Software on HPC**: R is available on HPC clusters like Woody. Standard CRAN packages can be installed if not already available.
- **Batch-Queuingsystem**: HPC systems use a batch queuing system where jobs are submitted as shell scripts and run when resources are available.
- **Job Limit**: Each job has a maximum runtime of 24 hours. Longer jobs will be terminated.
- **Parallelization**: Parallelization within R is possible on HPC clusters. Each node can be used exclusively, allowing for parallel processing on all available cores.
- **Data Transfer**: Data transfer between local systems and HPC clusters is done manually using `scp`.
- **Resource Availability**: The availability of HPC resources varies. There can be waiting times of a few days or the cluster can be half empty.
- **Time Savings**: While individual calculations may not be faster on HPC systems, the ability to run many independent jobs simultaneously can lead to significant time savings.

## Root Cause of the Problem
- The user's simulation requires extensive computational resources, particularly for cross-validation, which is the most computationally intensive part.
- The user's current cluster is experiencing high demand, leading to the need for alternative computing resources.

## Solution
- **HPC Account**: The user should apply for an HPC account to test the feasibility of running their simulations on the HPC cluster.
- **Job Splitting**: The user should split their jobs into smaller, independent tasks that can be run simultaneously on multiple nodes.
- **Parallelization**: The user can utilize the multiple cores available on each node for parallel processing within R.
- **Data Security**: The user should ensure that no sensitive data is processed on the HPC systems, as per the institution's data protection policies.

## Additional Notes
- **R-Pakete**: The required R packages are generally available or can be installed upon request.
- **JAGS**: JAGS may need to be installed as an Ubuntu package on the HPC system.
- **Support Resources**: Detailed information about the HPC systems and how to get started can be found on the institution's support website.

This summary provides a concise overview of the key points discussed in the HPC-Support ticket conversation, highlighting the general learnings, root cause of the problem, and the proposed solution.
---

### 2024102542001141_NHR-Starter%20b255bb%20_%20JA-23605%20SiAl-Reactivity%20-%20Kostenko%20-%20TUM.md
# Ticket 2024102542001141

 ```markdown
# HPC Support Ticket Conversation Analysis

## Keywords
- NHR Starter compute time application
- SSH keys
- SLURM workload manager
- Job submission
- ORCA modules
- xTB installation
- Resource allocation
- Node-sharing
- Job configuration
- Cluster access
- Permissions
- Quota
- Job monitoring

## General Learnings
- **Account Setup**: Users need to log in via SSO and accept export control regulations.
- **SSH Keys**: Necessary for accessing HPC systems.
- **SLURM Configuration**: Proper configuration is crucial for efficient resource usage.
- **Cluster Access**: Users need permissions to access specific clusters.
- **Job Monitoring**: Tools like ClusterCockpit are available for monitoring jobs.
- **Resource Allocation**: Understanding node-sharing policies is important for optimizing resource usage.

## Root Causes and Solutions

### Issue: Missing Home Directory and Filesystems
- **Root Cause**: Account not fully set up on all clusters.
- **Solution**: Wait until the next day for accounts to be created and SSH keys to be distributed.

### Issue: Unable to Connect to Other Clusters
- **Root Cause**: SSH keys not properly configured or permissions not granted.
- **Solution**: Ensure SSH keys are uploaded and wait for them to be distributed.

### Issue: SLURM Workload Manager Not Installed
- **Root Cause**: User attempted to submit jobs from a proxy jump node instead of a front-end node.
- **Solution**: Submit jobs from front-end nodes like Fritz.

### Issue: Environment Modules Not Configured
- **Root Cause**: User attempted to use modules on a proxy jump node.
- **Solution**: Use modules on front-end nodes.

### Issue: Excessive Processor Allocation
- **Root Cause**: Node-sharing not available on Fritz nodes.
- **Solution**: Bundle multiple runs into one job to utilize all or most of the 72 cores.

### Issue: Permission to Use Specific Clusters
- **Root Cause**: User does not have permission to use Tier3-only clusters.
- **Solution**: NHR users can access Fritz (for CPU) and Alex (for GPU). Collaboration with a PI from a regional university is required for Tier3 access.

### Issue: Resource Quota
- **Root Cause**: User unaware of resource quota.
- **Solution**: Check quota and CPU time used over time on the HPC portal.

## Documentation for Support Employees

### Account Setup
- Ensure users log in via SSO and accept export control regulations.
- Verify that SSH keys are uploaded and distributed.

### Job Submission
- Advise users to submit jobs from front-end nodes.
- Ensure SLURM workload manager and environment modules are configured on front-end nodes.

### Resource Allocation
- Inform users about node-sharing policies and how to optimize resource usage.
- Provide examples of job scripts that bundle multiple runs into one job.

### Cluster Access
- Ensure users have the necessary permissions to access specific clusters.
- Inform users about the clusters they have permission to use.

### Job Monitoring
- Provide users with tools and documentation for monitoring jobs.
- Ensure users are aware of their resource quota and how to check it.
```
---

### 2024102142000434_Blender%20auf%20fviz1.md
# Ticket 2024102142000434

 # HPC Support Ticket: Blender auf fviz1

## Keywords
- Blender
- Visualization
- Masterarbeit (Master's Thesis)
- Hardware Limitations
- fviz1
- VirtualGL

## Problem Description
A student requires Blender for a master's thesis focused on visualization. The student's laptop is insufficient for the task due to hardware limitations.

## Request
Install Blender on fviz1 to enable usage via VirtualGL.

## Solution
- **HPC Admin Response:** "meins" (indicating acknowledgment or ownership of the task)
- **Next Steps:** HPC Admins need to install Blender on fviz1 and ensure it can be accessed via VirtualGL.

## General Learnings
- **Hardware Limitations:** Students may encounter hardware limitations on personal devices for resource-intensive applications like Blender.
- **Remote Access:** Utilizing HPC resources like fviz1 with VirtualGL can overcome these limitations.
- **Support Process:** HPC Admins can assist in installing necessary software on HPC nodes to facilitate research and academic projects.

## Documentation for Future Reference
- **Root Cause:** Hardware limitations on personal devices.
- **Solution:** Install Blender on fviz1 and enable access via VirtualGL.
- **Action Items:** HPC Admins to handle software installation and configuration.

This documentation can be used to address similar requests for resource-intensive software installations on HPC nodes.
---

### 42129603_Cluster.md
# Ticket 42129603

 # HPC Support Ticket: Cluster Usage for Monte Carlo Simulation

## Keywords
- Virtual Machine
- Monte Carlo Software
- Cluster Platforms (openMosix, openPBS, Condor, Xgrid)
- Gate version 6.1
- Rechenzeitbedarf
- HPC Account

## Summary
A user inquires about running a virtual machine on the HPC cluster for Monte Carlo simulations. The user specifies the software and cluster platforms supported. The HPC Admin provides guidance on installing the software directly on the cluster and requests additional information about the software and resource requirements.

## Problem
- User wants to run a virtual machine on the HPC cluster for Monte Carlo simulations.
- User specifies supported cluster platforms: openMosix, openPBS, Condor, Xgrid.
- User uses Gate version 6.1 (Geant4 Application Tomograph Emission) for simulations.

## Solution
- HPC Admin informs the user that virtual machines cannot be run on the cluster.
- HPC Admin suggests installing the Monte Carlo software directly on the cluster.
- HPC Admin requests links to the software's installation instructions, source code, and binary packages.
- HPC Admin asks the user to estimate the computational resource requirements for the simulations.
- HPC Admin advises the user to activate their IDM-Kennung and apply for an HPC account.

## Additional Information
- User provides a link to the software's installation instructions and source code.
- User estimates the computational resource requirements based on simulation parameters.
- User is advised to activate their IDM-Kennung and apply for an HPC account to proceed.

## Conclusion
The user is guided through the process of preparing to run their simulations on the HPC cluster, including providing necessary software details and estimating resource requirements. The user is also instructed to activate their IDM-Kennung and apply for an HPC account.

## Next Steps
- User should activate their IDM-Kennung and apply for an HPC account.
- HPC Admin will review the provided software details and resource estimates to facilitate the installation and simulation process.
---

### 2018112142001023_AW%3A%20%5BRRZE-HPC%5D%20%20final%20shutdown%20of%20LiMa%20cluster.md
# Ticket 2018112142001023

 # HPC Support Ticket Conversation Analysis

## Keywords
- HPC Cluster Shutdown
- Software Installation Request
- Parallel Computing
- R Software
- Emmy Cluster
- Woody Cluster
- TinyEth Cluster
- TinyFat Cluster
- MPI Parallelization
- Shared-Memory Parallelization

## Summary
- **Cluster Shutdown**: The LiMa cluster is being shut down due to hardware issues.
- **Software Request**: User requests installation of R software on Emmy and Woody clusters.
- **Parallel Computing**: Discussion on the suitability of different clusters for parallel computing in R.

## Root Cause of the Problem
- User needs to run parallel R code and is unsure which cluster is suitable.
- Misunderstanding about the capabilities of different clusters for parallel computing.

## Solution
- **Software Installation**: R software is already available on Woody.
- **Cluster Suitability**:
  - **Woody**: Suitable for shared-memory parallelization (single node).
  - **Emmy**: Suitable for MPI parallelization (multiple nodes).
  - **TinyEth/TinyFat**: Suitable for moderately parallel software that uses a single node.

## General Learnings
- **Cluster Selection**: Understand the type of parallelization required (shared-memory vs. MPI) to select the appropriate cluster.
- **Software Availability**: Check existing software installations before requesting new installations.
- **Communication**: Clear communication about cluster capabilities and user needs is essential for efficient resource allocation.

## Action Items
- **HPC Admins**: Ensure users are aware of the capabilities and limitations of each cluster.
- **Users**: Provide detailed information about the type of parallelization required when requesting software installations.

## References
- **HPC Documentation**: Review and update documentation to clarify cluster capabilities for parallel computing.
- **Support Tickets**: Use support tickets to gather detailed requirements from users.

---

This analysis provides a summary of the key points discussed in the HPC support ticket conversation, highlighting the root cause of the problem and the solution provided. It also includes general learnings and action items for both HPC admins and users.
---

### 2023052542002964_Nutzung%20von%20HPC-Ressourcen%20-%20STATA.md
# Ticket 2023052542002964

 # HPC-Support Ticket Conversation Analysis

## Keywords
- HPC Resources
- STATA
- R
- Licensing
- HPC-Cafe
- Documentation
- Password Setup
- Dataset Processing

## General Learnings
- **User Request**: The user requested HPC resources for statistical evaluations using STATA.
- **Licensing Issues**: STATA SE is licensed but has limitations in utilizing multi-core CPUs. STATA MP would need to be acquired separately.
- **Alternative Software**: R was suggested as an alternative to STATA, but the user was not familiar with it.
- **Support Events**: HPC-Cafe and online introductions were recommended for new users.
- **Password Setup**: Instructions were provided for setting up a password for the new HPC ID.
- **Dataset Processing**: The user wanted to process a large dataset, and STATA SE was temporarily installed on the HPC systems.

## Root Cause of the Problem
- The user needed to process a large dataset using STATA but faced licensing and software limitations.

## Solution
- STATA SE was installed on the HPC systems for temporary use.
- The user was offered support for initial steps on the HPC systems, including login and data transfer.
- The user was advised to consider using R as an alternative to STATA for future projects.

## Documentation for Support Employees
For similar issues in the future, consider the following steps:
1. **Assess Software Requirements**: Determine if the requested software (e.g., STATA) is suitable for HPC systems and check licensing options.
2. **Provide Alternatives**: Suggest alternative software (e.g., R) if the requested software has limitations.
3. **Offer Support Events**: Recommend attending HPC-Cafe and online introductions for new users.
4. **Password Setup**: Guide users through setting up a password for their new HPC ID.
5. **Temporary Solutions**: Install requested software temporarily if it meets the user's immediate needs.
6. **Follow-up Support**: Offer additional support for initial steps on the HPC systems, such as login and data transfer.

By following these steps, support employees can effectively address similar requests and provide comprehensive assistance to users.
---

### 42294704_A%20request%20for%20FENICS.md
# Ticket 42294704

 # HPC Support Ticket: Request for FENICS

## Keywords
- FENICS
- Finite Element Calculations
- Software Installation
- Space Requirement
- Parallel Efficiency
- User Support

## Summary
A user requested the installation of FENICS, a popular open-source finite element solver, on the HPC clusters Lima and Emmy. The user cited space requirements and lack of expertise in configuring the package as reasons for the request.

## Root Cause
- User's concern about space requirements for installing FENICS.
- User's lack of expertise in optimizing the parallel efficiency of FENICS.

## HPC Admin Response
- The HPC Admin advised the user to install the software themselves, as they are the only user of the package.
- The Admin clarified that there is sufficient space on the fileservers and provided documentation on the filesystem.
- The Admin offered assistance if the user encounters difficulties but noted that supporting a complex software package for a single user is not a top priority.

## User's Follow-Up
- The user acknowledged the Admin's response and agreed to install FENICS themselves, aiming to optimize it as best as they can.

## Solution
- Users should attempt to install software packages themselves if they are the only user.
- Users can refer to the filesystem documentation for space requirements.
- If users encounter difficulties, they can contact HPC support for assistance.

## General Learning
- HPC users should be encouraged to install and manage software packages that are specific to their needs.
- HPC support should prioritize assisting with widely used software packages.
- Clear communication about available resources and support priorities is essential.
---

### 2020110742000191_Nutzung%20von%20HPC%20Ressourcen%20f%C3%83%C2%BCr%20das%204Dnanoscope%20project.md
# Ticket 2020110742000191

 # HPC Support Ticket Conversation Analysis

## Keywords
- HPC Resources
- 3D Dosissimulationen
- MicroCT Scanner
- GAMOS Simulationsframework
- Woody Cluster
- CPU
- Antrag auf Nutzung von HPC Ressourcen
- Jobgröße
- Speicherplatz
- Rechenzeit
- HPC Einführung

## What Can Be Learned
- **Communication Preference**: Use the official university email address for communication with HPC support.
- **Cluster Suitability**: The Woody Cluster is suitable for CPU-based simulations.
- **Resource Estimation**:
  - Typical job size on Woody is 1 node/4 CPUs.
  - Estimate storage based on input and output file sizes.
  - Estimate computation time based on the number and duration of simulations.
- **HPC Introduction**: Monthly introductory sessions are offered for HPC beginners.
- **Flexibility**: An HPC account allows access to all clusters, not just Woody.

## Root Cause of the Problem
- User was unsure about how to estimate resource requirements for the HPC resource application.

## Solution
- HPC Admin provided guidelines for estimating job size, storage, and computation time.
- User was advised to attend an introductory HPC session for further assistance.

## Additional Notes
- The user was directed to use their official university email for better communication tracking.
- The user expressed gratitude for the support and planned to attend the introductory session.

---

This report provides a concise summary of the support ticket conversation, highlighting key points and solutions for future reference.
---

