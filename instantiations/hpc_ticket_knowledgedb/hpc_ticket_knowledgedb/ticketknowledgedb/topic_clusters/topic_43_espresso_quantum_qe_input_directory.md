# Topic 43: espresso_quantum_qe_input_directory

Number of tickets: 8

## Tickets in this topic:

### 2022060242000044_Quantum%20espresso%20compilation%20and%20upload%20files.md
# Ticket 2022060242000044

 # HPC Support Ticket: Quantum Espresso Compilation and File Upload

## Keywords
- Quantum Espresso (QE)
- Compilation
- Environment Setup
- File Upload
- SCP
- Module Avail

## Problem
- User needs Quantum Espresso version 6.8, which is not available on the HPC system.
- User requires guidance on compiling QE and setting up the environment.
- User needs to upload input files to the HPC system.

## Root Cause
- Quantum Espresso version 6.8 is not pre-installed on the HPC system.
- User is unfamiliar with the compilation process and environment setup on the HPC system.
- User is unsure about the file upload process and path sharing across clusters.

## Solution
- **Compilation and Environment Setup:**
  - Load necessary modules: `module load intel intelMPI intelMKL`
  - Compile QE using the `make` command.
  - Compilation can be done in the home directory or preferably in the `$WORK` directory. If code changes are planned, use `$HPCVAULT` for regular backups.
- **File Upload:**
  - Use SCP for file upload: `scp -r local_directory_to_copy username@cluster_address:$path`
  - Ensure the path is correct and use the `-r` flag for directories.

## Documentation
- General software documentation: [HPC Software Environment](https://hpc.fau.de/systems-services/systems-documentation-instructions/environment)
- Cluster-specific documentation: [Emmy Cluster](https://hpc.fau.de/systems-services/systems-documentation-instructions/clusters/emmy-cluster/)

## Notes
- The HPC system has Quantum Espresso version 6.5 pre-installed.
- Regular HPC introductions and training sessions are available for users.

## Roles Involved
- HPC Admins
- 2nd Level Support Team
- Head of the Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support
- Software and Tools Developer
---

### 2024072442002308_espresso%20auf%20NHR.md
# Ticket 2024072442002308

 # HPC Support Ticket Conversation Analysis

## Subject
espresso auf NHR

## Keywords
- ESPResSo
- NHR
- GPU acceleration
- NVIDIA
- Features
- Compilation
- Dependencies
- Befehlszeile mit Input
- Submit script
- Interactive execution
- Intel MPI
- Python

## What Can Be Learned

### General Information
- **Software Request**: User requested the installation of ESPResSo MD engine version 4.2.2 on Alex and/or Fritz for GPU acceleration using NVIDIA.
- **Dependencies**: HPC Admins identified the necessary dependencies for the initial compilation of ESPResSo on Fritz.
- **Features**: User specified the required features for ESPResSo, including MASS, EXCLUSIONS, DPD, TABULATED, LENNARD_JONES, LJCOS2, and HAT.
- **Input Data**: User provided a configuration file (myconfig.hpp) and was asked to provide a command line with input for testing.

### Root Cause of the Problem
- **Clarification Needed**: User needed clarification on what was meant by a "Befehlszeile mit Input" for testing the software.
- **Interactive Execution Issue**: Intel MPI may cause issues with interactive execution of ESPResSo in combination with Python on Fritz.

### Solution
- **Module Installation**: ESPResSo 4.2.2 module was installed on both Alex and Fritz.
- **Testing**: User was advised to test the software using the provided module and to report any issues.

## Conclusion
This ticket highlights the importance of clear communication between users and HPC Admins regarding software installation and testing. It also demonstrates the potential issues with interactive execution of certain software combinations on HPC systems.

## Additional Notes
- **User Support**: The user was assisted by a master's student who provided the necessary input and configuration files.
- **Future Actions**: Users should be prepared to provide detailed information about the features and input data required for software testing.

---

This analysis can serve as a reference for future support tickets involving software installation and testing on HPC systems.
---

### 2023030242004401_QE-Modul%20auf%20Fritz%3F.md
# Ticket 2023030242004401

 ```markdown
# HPC-Support Ticket: QE-Modul auf Fritz

## Subject
QE-Modul auf Fritz?

## User Request
- **Issue**: Uncertainty about who manages modules on the HPC system.
- **Request**: Installation of Quantum Espresso (QE) as a module accessible to all users, similar to CP2k.
- **Details**:
  - Requested by Goerling and Brabec groups.
  - Query about the best method to provide executables or compile themselves.

## HPC Admin Response
- **Guidance**: Use the central support email (hpc-support@fau.de) for all support requests.
- **Solution**:
  - Quantum Espresso can be provided as a module.
  - Software installation typically done via Spack.
  - Spack offers specific options/variants for QE.
  - User collaboration required for the installation process.

## Keywords
- Quantum Espresso (QE)
- Module installation
- Spack
- Central support email

## General Learnings
- Always direct support requests to the central support email.
- Collaboration between users and HPC admins is essential for module installation.
- Spack is the preferred tool for software installation on the HPC system.

## Root Cause
- Lack of clarity on the process for requesting and installing new modules.

## Solution
- Use the central support email for all requests.
- Collaborate with HPC admins to provide necessary details for module installation via Spack.
```
---

### 2024070542001845_Required%20help%20in%20the%20installation%20of%20Quantum%20ESPRESSO.md
# Ticket 2024070542001845

 # HPC Support Ticket: Quantum ESPRESSO Installation Issue

## Keywords
- Quantum ESPRESSO
- HPC Meggie
- Job submission
- SLURM
- Module load
- pw.x

## Problem Description
- User attempted to install Quantum ESPRESSO on HPC Meggie.
- Job allocated to 60 cores ran as 60 single-core jobs instead of a single job using 60 cores.

## Root Cause
- User tried to compile Quantum ESPRESSO instead of using the pre-installed module.
- Incorrect job script configuration.

## Solution
- Use the pre-installed Quantum ESPRESSO module: `module load qe/7.1`.
- Correct job script configuration:
  ```bash
  unset SLURM_EXPORT_ENV
  module load qe/7.1
  srun pw.x < 2_scf.in > 2_scf.out
  ```
- Ensure job submission is done from the appropriate directory to avoid changing directories within the script.

## Lessons Learned
- Always check for pre-installed modules before attempting to compile software.
- Proper job script configuration is crucial for efficient resource utilization.
- Modules automatically load relevant dependencies, simplifying the job script.

## Additional Notes
- The `pw.x` module in Quantum ESPRESSO can be accessed directly after loading the module.
- Submit jobs from the appropriate directory to avoid path issues.

## Ticket Status
- Closed after successful resolution.
---

### 2021100642003966_Kompilieren%20von%20Quantum%20ESPRESSO%20auf%20Emmy.md
# Ticket 2021100642003966

 # HPC-Support Ticket Conversation: Compiling Quantum ESPRESSO on Emmy

## Subject
Kompilieren von Quantum ESPRESSO auf Emmy

## Keywords
Quantum ESPRESSO, DFT, HPC, Compilation, MKL, FFT, LAPACK, ScaLapack, ELPA, Pseudopotentials, PBE, Hybrid functionals, CASTEP, Meggie, Emmy, $FASTTMP, $VAULT, Torque shell, Spin-Orbit Polarisation, Convergence test, k-point sampling, cut-off energy, Gamma-Punkt, Gamma-Tricks, Speicherbedarf, Kompilierfehler, Submitting-shell, Fehlerdatei, Output-Datei

## What Can Be Learned

### General Information
- **User's Goal**: Compile Quantum ESPRESSO for DFT calculations on Quantum Dots for a Master's thesis.
- **Systems Used**: Emmy, Meggie.
- **Modules Loaded**: `intel64`, `intelmpi`.
- **Libraries**: MKL, FFT, LAPACK, ScaLapack, ELPA.
- **Methods**: PBE, Hybrid functionals.
- **Pseudopotentials**: Pseudo-dojo.

### Compilation Issues
- **Initial Problem**: FFT and LAPACK libraries not found during compilation.
- **Solution**: MKL contains all necessary libraries; no need to compile separate FFTW or LAPACK.

### Simulation Details
- **System Size**: 306 atoms with four different atom types (InCuS2 with passivated hydrogen).
- **Initial Tests**: Structure relaxation, Spin-Orbit Polarisation, Band structure calculation.
- **Convergence Test**: k-point sampling (initial 4 x 4 x 4 on 8 nodes), cut-off energy of 80Ry.

### Memory and Resource Allocation
- **Memory Requirement**: Estimated max dynamical RAM per process > 27.77 GB.
- **Available Memory**: 58871 MiB available memory on the printing compute node.
- **Resource Allocation**: 64 nodes allocated but only 8 used; job terminated due to inefficient resource usage.

### Specific Issues and Solutions
- **Gamma-Punkt**: Use `K_POINTS {gamma}` instead of `K_POINTS {automatic}` for isolated systems.
- **Cut-off Energy**: Ensure cut-off energy meets the requirements of the pseudopotentials used.
- **Speicherbedarf**: Calculate the required memory and allocate resources accordingly.
- **Cluster Access**: Meggie is recommended for Quantum ESPRESSO; access via `ssh user@meggie`.

### Additional Tips
- **Workshop**: Quantum Espresso workshop from May 2021 for further learning.
- **Alternative Code**: CASTEP for better scaling with larger systems.

## Conclusion
The conversation highlights the importance of proper resource allocation, correct usage of libraries, and understanding the specific requirements of the simulation. The HPC Admins provided detailed guidance on compiling Quantum ESPRESSO, allocating resources, and addressing specific issues in the simulation setup.
---

### 2023032442003585_Installation%20of%20Quantum%20Espresso%20-%20bctc038h.md
# Ticket 2023032442003585

 # HPC Support Ticket: Installation of Quantum Espresso

## Keywords
- Quantum Espresso
- VASP
- Module Installation
- Script Installation
- HPC Facility
- Theoretical Chemistry

## Summary
A doctoral student in theoretical chemistry requested assistance with installing Quantum Espresso on the Fritz NHR HPC facility. The user was already utilizing VASP for simulations but needed Quantum Espresso for additional research purposes.

## Problem
- User was unsure if Quantum Espresso was installed on the HPC facility.
- User required technical help for the installation of Quantum Espresso.

## Solution
1. **Initial Response**:
   - HPC Admins informed the user that they were working on the installation of Quantum Espresso and would provide a module that could be loaded.
   - Admins inquired about additional binary files important for the user's research.

2. **Interim Solution**:
   - HPC Admins provided a script (`install_qe.sh`) for the user to install Quantum Espresso on their account.
   - Instructions were given to change the script's permission using `chmod +x install_qe.sh` and run it with the destination directory as an argument.

3. **Final Solution**:
   - HPC Admins successfully installed Quantum Espresso and made a `qe/7.1` module available on the HPC facility.
   - The user was notified about the availability of the module.

## Additional Information
- The user mentioned specific binary files required for their research: `pw.x`, `dos.x`, `bands.x`, `pp.x`, `projwfc.x`, `ph.x`, `matdyn.x`, `dynmat.x`, and `q2r.x`.
- Recommendations were provided for running VASP in hybrid mode (MPI+OpenMP) for better performance.

## Conclusion
The HPC Admins successfully addressed the user's request by providing a script for immediate use and later installing a module for Quantum Espresso on the HPC facility. The user was able to proceed with their research using the required software.
---

### 2020021742001839_QE%20installation.md
# Ticket 2020021742001839

 ```markdown
# HPC Support Ticket: QE Installation

## Keywords
- Quantum Espresso (QE)
- Job Submission
- Directory Creation Error
- MPI Execution
- SLURM
- Compilation Modules

## Summary
User encountered issues with running Quantum Espresso on Meggie/Emmy servers. The main problems were:
1. Job submission failure when using a batch script.
2. Directory creation error in QE's `wrappers.f90` module.

## Root Cause
1. **Job Submission Failure**: The job was submitted from a different directory than the one specified in the input file for output.
2. **Directory Creation Error**: Typo in the directory path specified in the input file.

## Solution
1. **Job Submission**: Ensure the job is submitted from the correct directory or adjust the input file to match the submission directory.
2. **Directory Creation Error**: Correct the typo in the directory path in the input file.

## Detailed Steps
1. **Job Submission**:
   - User tried to submit the job using `sbatch` but it failed silently.
   - HPC Admin identified that the job was submitted from `/lxfs/bctc/bctc47/QE/Doping/Barium/0H2O/` but the output directory was set to `/lxfs/bctc/bctc47/QE/Barium/0H2O/Save/`.
   - Solution: Adjust the input file to use the correct directory path.

2. **Directory Creation Error**:
   - User encountered an error in `create_directory` routine due to a non-existent directory.
   - HPC Admin suggested checking the directory path and ensuring it exists.
   - Solution: Correct the typo in the directory path in the input file.

## Additional Notes
- The user compiled QE on Meggie using different module combinations (`intelmpi intel64 mkl` and `intelmpi intel64`), but both resulted in the same error.
- HPC Admin noted that the very slow inbuilt FFT library was used and suggested that `-ndiag 16` does not help without the ELPA Library.
- HPC Admin planned to provide an optimized QE 6.5 build in the next few weeks via the modules environment.

## Conclusion
The issues were resolved by correcting the directory paths in the input file and ensuring the job was submitted from the correct directory.
```
---

### 2025011242000154_Zus%C3%83%C2%A4tzliche%20Features%20f%C3%83%C2%BCr%20espresso%20auf%20fritz.md
# Ticket 2025011242000154

 # HPC Support Ticket Conversation Analysis

## Subject: Zusätzliche Features für espresso auf fritz

### Keywords:
- espressomd
- Fritz
- THERMOSTAT_PER_PARTICLE
- myconfig.hpp
- Python 3.9.5

### Summary:
- **User Request:** Additional features for espressomd on Fritz, specifically `THERMOSTAT_PER_PARTICLE`.
- **HPC Admin Response:** espressomd recompiled with the requested feature. New binary available as `espressomd/4.2.2`.
- **User Feedback:** Acknowledgment and gratitude for the quick resolution.

### Root Cause:
- User's simulation requirements changed, necessitating additional features in espressomd.

### Solution:
- HPC Admins recompiled espressomd with the `THERMOSTAT_PER_PARTICLE` feature.
- New binary (`espressomd/4.2.2`) provided to the user.

### General Learnings:
- Users may require additional features for software installed on HPC systems.
- HPC Admins can recompile software to include requested features.
- Quick resolution and communication are appreciated by users.

### Follow-up Actions:
- Ensure users are aware of the new binary and how to access it.
- Monitor for any issues related to the new binary and provide support as needed.

### Documentation Note:
- Keep a record of custom software compilations for future reference.
- Update user documentation to reflect the availability of the new binary.
---

