# Topic 6: module_intel_compiler_version_installation

Number of tickets: 222

## Tickets in this topic:

### 2021080542002535_Job%20resources%20with%20the%20ice-flow%20model%20Elmer_Ice.md
# Ticket 2021080542002535

 # HPC Support Ticket: Job Resources with Elmer/Ice Model

## Summary
User encountered segmentation fault errors while running an Elmer/Ice exercise. The issue was related to incorrect compiler versions and missing dependencies.

## Keywords
- Elmer/Ice
- Segmentation Fault
- Compiler Version
- Dependencies
- SLURM Script

## Problem
- User was running an Elmer/Ice exercise that required significant computational resources.
- The job returned a segmentation fault error.
- Suspected incorrect specifications in the batch script.

## Root Cause
- Mismatch between the compiler version used to build Elmer/Ice and the one loaded in the module.
- Missing or incorrect version of the `nn-c` library needed for natural neighbors interpolation.

## Solution
1. **Compiler Version Matching**:
   - Ensure the compiler version in the module matches the one used to build Elmer/Ice.
   - User updated the module to load `intel64/18.0.p04` to match the building compiler.

2. **Correct Dependencies**:
   - Identified that the model was crashing during an interpolation attempt.
   - Found that only a specific version of the `nn-c` library (v1.85.0) allowed the model to run correctly.

3. **SLURM Script**:
   - Provided a sample SLURM script to allocate resources properly:
     ```bash
     #!/bin/bash -l
     # allocate 4 nodes with 20 cores per node = 4*20 = 80 MPI tasks
     #SBATCH --tasks-per-node=20
     #SBATCH --nodes=4
     #SBATCH --cpus-per-task=1
     # allocate nodes for 1 hours
     #SBATCH --time=1:00:00
     #SBATCH --export=NONE
     ### do not export environment variables
     unset SLURM_EXPORT_ENV
     # jobs always start in submit directory
     export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
     srun ElmerSolver MESH_OPTIM.sif
     ```

## Outcome
- User successfully ran the exercise after updating the compiler version and using the correct version of the `nn-c` library.
- Some built-in tests still failed, but they were not crucial for the user's current exercises.

## Future Actions
- Consider creating a knowledge base page for Elmer/Ice to document best practices and common issues.
- Continue sharing experiences and problems within the user group to improve the installation and usage process.

## Additional Notes
- The user and a few colleagues are the primary users of Elmer/Ice on the HPC system.
- The installation process is still being refined, and issues are being addressed collaboratively.
---

### 2023121342002455_Java%2011%20module%20at%20woody.md
# Ticket 2023121342002455

 ```markdown
# HPC-Support Ticket: Java 11 Module Request on Woody

## Keywords
- Java 11
- Nextflow
- Woody
- Module
- JDK

## Problem
- User requires Java 11 or later to use Nextflow on Woody.
- Only Java 8 module (java/jdk8u345-b01-openj9) is available.

## Solution
- HPC Admin installed a new Java module (java/jdk21.0.1) on Woody.
- User confirmed that the new module works.

## Lessons Learned
- Ensure that the required software versions are available as modules.
- Quick response and installation of requested modules can resolve user issues efficiently.
```
---

### 2024070542002701_%5BTestcluster%5D%20openmpi_4.1.1-gcc9.3-legacy%20not%20working.md
# Ticket 2024070542002701

 # HPC Support Ticket: OpenMPI Module Not Working

## Subject
[Testcluster] openmpi/4.1.1-gcc9.3-legacy not working

## Issue
- **Root Cause**: Missing `libpmi2.so` library.
- **Affected Module**: openmpi/4.1.1-gcc9.3-legacy
- **Error Message**: `mpicc: error while loading shared libraries: libpmi2.so.0: cannot open shared object file: No such file or directory`

## Diagnosis
- **Initial Report**: User reported that the openmpi/4.1.1-gcc9.3-legacy module is not working due to missing `libpmi2.so`.
- **Admin Investigation**:
  - `libpmi` and `libpmi2` are part of Slurm.
  - Older versions of Slurm have these libraries, but they are missing in versions 21.08.3 and 23.02.7.
  - The current Slurm installation did not include the "contrib" package, which contains `libpmi` and `libpmi2`.

## Solution
- **Admin Actions**:
  - Rebuilt Slurm with the "contrib" package to include `libpmi` and `libpmi2`.
  - Ensured that the libraries are available in the standard library path by setting up symbolic links or updating `/etc/ld.so.conf.d/slurm.conf`.

## Follow-Up
- **User Confirmation**: The issue was resolved on `testfront1`.
- **Additional Nodes**: User reported the same issue on `broadep2` and `ivyep1`. Admin team needs to ensure the libraries are available on these nodes as well.

## Keywords
- openmpi
- libpmi2.so
- Slurm
- ldconfig
- module
- HPC cluster
- shared libraries
- mpicc

## Lessons Learned
- Ensure that all necessary components (like "contrib" for Slurm) are included during installation.
- Verify that all required libraries are in the standard library path or update the path accordingly.
- Communicate with users to confirm resolution and address any additional issues promptly.
---

### 2022051342002363_Tier3-Access-Fritz%20%22Eman%20%20Bagheri%22%20_%20iwpa014h.md
# Ticket 2022051342002363

 # HPC Support Ticket Analysis: Tier3-Access-Fritz

## Keywords
- OpenFOAM
- SPACK_ENV_PATH
- Compilation Error
- Module Configuration
- Re-login

## Summary
A user encountered issues with compiling modified solvers using OpenFOAM/2112 due to a missing `SPACK_ENV_PATH` variable. The same error occurred even when attempting to recompile the default solver of the same version. OpenFOAM-org/8.0 worked fine, indicating that the variable was automatically set for that version.

## Root Cause
The root cause of the problem was identified as an issue with the module configuration file. Specifically, the second prepend-path in the module file contained paths that were not from the OpenFOAM directory, including paths related to SPACK and cmake.

## Solution
The HPC Admin modified the module configuration file by removing paths that were not from the OpenFOAM directory. This included paths related to SPACK and cmake, which were likely responsible for the error. The user was advised to re-login and try again, which resolved the compilation issue.

## General Learnings
- **Module Configuration**: Ensure that module configuration files do not contain unnecessary or conflicting paths.
- **Re-login**: Sometimes, simply re-logging into the system can resolve issues related to environment variables.
- **SPACK_ENV_PATH**: This variable is crucial for compiling certain software versions and should be correctly set in the module configuration.

## Actions Taken
- The HPC Admin modified the module configuration file to remove conflicting paths.
- The user was advised to re-login and retry the compilation, which resolved the issue.

## Conclusion
Proper configuration of module files and environment variables is essential for successful software compilation. Re-logging into the system can sometimes resolve issues related to environment variables.
---

### 2019051642001016_System_Compiler-Update%20aurora1.md
# Ticket 2019051642001016

 # HPC Support Ticket: System/Compiler-Update aurora1

## Keywords
- Compiler Update
- musl-libc to glibc
- VEOS Update
- NUMA Domains
- Aurora Binaries

## Summary
- **Issue**: Update of the software stack on aurora1, including compiler updates and a switch from musl-libc to glibc.
- **Root Cause**: Need for software stack update and compatibility concerns with old binaries.
- **Solution**: Update performed, old binaries tested and found to be compatible.

## Details
- **HPC Admin**: Announced plans to update the system and compiler on aurora1, including a switch from musl-libc to glibc.
- **User**: Inquired about the timeline for new compiler versions.
- **HPC Admin**: Confirmed the update to VEOS 2.1.0, availability of new compilers up to 2.1.2, and the introduction of llvm-ve/1.1.0.
- **Compatibility**: Old binaries and compilers (1.x) with musl-libc are expected to remain functional despite the switch to glibc-ve.
- **NUMA Domains**: VEs can now be partitioned into two NUMA domains if needed.

## Lessons Learned
- Regular updates to the software stack are necessary for maintaining system performance and compatibility.
- Compatibility testing of old binaries and compilers is crucial to ensure smooth transitions.
- Updates to VEOS versions can introduce new features like NUMA domain partitioning.

## References
- [VEOS 2.0.1 Update Guide](https://sx-aurora.github.io/posts/VEOS-2.0.1-update/)

## Next Steps
- Monitor the system for any issues related to the update.
- Continue testing old binaries and compilers for any unforeseen compatibility issues.

---

This documentation provides a summary of the updates and changes made to the aurora1 system, including the switch from musl-libc to glibc and the introduction of new compiler versions. It also highlights the importance of compatibility testing and the new features introduced with the VEOS update.
---

### 42344102_MIT%20photonic%20band%20gap%20installation.md
# Ticket 42344102

 # HPC Support Ticket: MIT Photonic Band Gap Installation

## Keywords
- MIT Photonic-Bands package
- Software installation
- BLAS, LAPACK
- FFTW
- Guile
- MPI
- HDF5
- Intel MKL
- Intel Compilers
- GNU GCC Compilers
- Static linking
- Module system

## Problem
- User requests assistance with installing the MIT Photonic-Bands package, which requires several additional packages such as Guile, LAPACK, etc.

## Root Cause
- The user needs to install and configure the MIT Photonic-Bands package along with its dependencies.

## Solution
- **BLAS, LAPACK**: Use Intel MKL, which is automatically loaded with Intel Compiler modules or manually with the "mkl" module. Use the `-mkl` option for compiling and linking with Intel Compilers. For GNU GCC Compilers, refer to the [Intel MKL Link Line Advisor](http://software.intel.com/sites/products/mkl/MKL_Link_Line_Advisor.html) for correct link flags.
- **FFTW**: FFTW2 and FFTW3 compatible bindings are included in Intel MKL. Check the required version (fftw2 or fftw3) before building from source.
- **Guile**: Available on login nodes with developer packages. Not installed on compute nodes. If Guile is needed at runtime, either link it statically or build it from source.
- **MPI**: Recommended to use Intel MPI ("intelmpi" module). Alternatively, "openmpi" modules are available.
- **HDF5**: Available as modules ("hdf5") in both serial and parallel versions.

## General Learnings
- Users are responsible for building and installing specialized software themselves due to limited personnel resources.
- Utilize available modules for dependencies like Intel MKL, MPI, and HDF5.
- Ensure compatibility and correct linking for dependencies like FFTW and Guile.
- Refer to documentation and advisors for specific linking and compilation options.

## Additional Notes
- The user should install the software in their local directory, such as `$WOODYHOME`.
- The compute nodes have limited resources, so additional packages should be installed with caution.

---

This report provides a concise overview of the issue, the root cause, and the solution, along with general learnings for future reference.
---

### 2025020242000475_poppler-utils%20auf%20csnhr%20installieren.md
# Ticket 2025020242000475

 ```markdown
# HPC Support Ticket: Installation of poppler-utils

## Keywords
- poppler-utils
- installation
- csnhr

## Summary
A user requested the installation of the `poppler-utils` package on the `csnhr` system.

## Root Cause
The user needed the `poppler-utils` package for their work on the `csnhr` system.

## Solution
The HPC Admin installed the `poppler-utils` package as requested.

## Lessons Learned
- Users may require specific software packages for their work.
- HPC Admins can quickly address such requests by installing the necessary packages.
```
---

### 2023101142002453_RE%3A%20Could%20you%20please%20help%20on%20compiling%20this%20software%3F.md
# Ticket 2023101142002453

 ```markdown
# HPC Support Ticket: RE: Could you please help on compiling this software?

## Keywords
- Segmentation fault
- Intel compiler
- MKL
- Optimization flags
- LLVM compiler
- Binary compatibility

## Summary
User encountered segmentation faults when compiling and running `mlip-3` software on the Fritz HPC server using Intel compilers and MKL. The issue was resolved by using Intel LLVM compilers.

## Root Cause
- The segmentation fault occurred during the execution of tests, specifically in the MTPR loss gradient test.
- The issue was not present when using the `-O0` optimization flag, but this resulted in significantly slower performance.
- Different optimization flags (`-O2`, `-O1`, `-O1 -no-vec`) were tried without success.

## Troubleshooting Steps
1. **Initial Setup**:
   - User compiled `mlip-3` using Intel compilers and MKL.
   - Modules loaded: `intel`, `intelmpi`, `mkl`.
   - Optimization flags: `-O3`, `-O2`, `-O1`, `-O1 -no-vec`.

2. **Segmentation Fault**:
   - Segmentation fault occurred during the MTPR loss gradient test.
   - Backtrace indicated issues in `libucs.so.0` and `libpthread.so.0`.

3. **Workaround**:
   - User reported that a binary compiled on another server with Intel compiler 19.0 and MKL 2019 worked on the Fritz server, except for one test.
   - HPC Admin recommended against this workaround due to potential issues with dynamic and static linking.

4. **Solution**:
   - HPC Admin recommended using Intel LLVM compilers (`oneapi`).
   - Modules loaded: `000-all-spack-pkgs/0.19.1`, `intel-oneapi-compilers/2023.2.1-gcc8.5.0-axze7oc`, `intel-oneapi-mpi/2021.10.0-gcc8.5.0-ki6gcj4`, `mkl/2022.1.0`.
   - Compiler settings in `make/config.mk`:
     ```makefile
     CC_MPI  = mpiicx
     CXX_MPI = mpiicpx
     FC_MPI  = mpiifx
     CC  = icx
     CXX = icpx
     FC  = ifx
     ```
   - Optimization flag: `-O2`.

## Outcome
- The compilation was successful with the Intel LLVM compilers.
- The performance was similar to the previous Intel compiler, with a speed difference of ~10%.
- The user confirmed that the solution was stable and suitable for future calculations.

## Conclusion
- The segmentation fault issue was resolved by switching to Intel LLVM compilers.
- Using the correct compiler and optimization settings is crucial for avoiding such issues.
- Copying binaries from other systems is not recommended due to potential compatibility issues.
```
---

### 2024112042002503_clang%2B%2B_llvm.md
# Ticket 2024112042002503

 # HPC Support Ticket: clang++/llvm

## Keywords
- llvm
- clang++
- woody cluster
- SPACK
- module
- compiler

## Problem
- User unable to find the `llvm` module on the woody cluster, which is supposed to include the `clang++` compiler.

## Root Cause
- The `llvm` module is not available on the woody cluster.
- The current SPACK version on woody supports up to `llvm-14`, while newer versions are required.

## Solution
- The `clang++` compiler can be found in the directory:
  ```
  /apps/SPACK/0.18.0/opt/linux-almalinux8-icelake/gcc-8.5.0/intel-oneapi-compilers-2022.1.0-y2vz2k3joidylzrhmkrza2hzwzswb6yj/compiler/2022.1.0/linux/bin-llvm
  ```
- Future updates to SPACK on other clusters will provide newer versions of `llvm`.

## General Learnings
- Always check the availability of modules on specific clusters.
- Older versions of SPACK may not support the latest software versions.
- Directories may contain required tools even if modules are not available.

## Actions Taken
- Informed the user about the location of the `clang++` compiler.
- Noted that future updates will address the SPACK version issue.

## Status
- Ticket closed after providing the user with the necessary information.
---

### 2017020742001221_Pakete%20auf%20Woody.md
# Ticket 2017020742001221

 # HPC Support Ticket: Package Installation on Woody

## Keywords
- Package installation
- Woody cluster
- Headnode
- Compute nodes
- Development packages
- libcxxtools-dev
- libx11-dev
- libxmu-dev
- libxi-dev
- freeglut-dev
- libxft-dev
- libxext-dev

## Summary
A user requested the installation of several development packages on both the headnode and compute nodes of the Woody cluster. The HPC Admin responded by installing the packages on the frontends and only the non-development versions on the compute nodes.

## Root Cause
The user requested development packages on compute nodes, which is generally unnecessary and can be considered inappropriate for typical compute node usage.

## Solution
- **Headnode**: Installed the requested development packages.
- **Compute Nodes**: Installed only the non-development versions of the packages.

## Lessons Learned
- Development packages are typically not required on compute nodes.
- It is important to clarify the necessity of installing development packages on compute nodes to avoid unnecessary installations.
- Communication with the user to understand the specific requirements can help in making appropriate decisions regarding package installations.

## Actions Taken
- Installed the requested development packages on the headnode.
- Installed the non-development versions of the packages on the compute nodes.

## Follow-Up
- Ensure that users are aware of the appropriate use of development packages on different parts of the cluster.
- Document the rationale behind installing only non-development packages on compute nodes for future reference.
---

### 2022091942000169_falsche%20Version%20von%20R%20%20%3F.md
# Ticket 2022091942000169

 ```markdown
# HPC-Support Ticket: Incorrect Version of R

## Keywords
- R version
- Module loading
- Version mismatch

## Problem Description
The user reported that the incorrect version of R (3.6.3) was being executed despite loading the module for R version 4.2.1.

## Root Cause
The user loaded the module for R version 4.2.1, but the system was still executing R version 3.6.3. This indicates a potential issue with the module loading or the environment configuration.

## Solution
The HPC Admin responded via Ticket#2022091942000258. The exact solution was not provided in the conversation, but it likely involved checking the module loading process and ensuring the correct version of R was being executed.

## General Learning
- Ensure that the correct module is loaded and that the environment is properly configured to use the desired version of software.
- Verify the version of the software being executed to ensure it matches the loaded module.
- Document the command sequence and environment settings for troubleshooting purposes.
```
---

### 2017022142001453_Problem%20mit%20amber-gpu%2016%20auf%20emmy.md
# Ticket 2017022142001453

 # HPC Support Ticket: Problem mit amber-gpu 16 auf emmy

## Keywords
- Amber-gpu 16
- pmemd.cuda.MPI
- GPU-GPU-Kommunikation
- MPI-parallele GPU-Binaries
- Emmy

## Problem
- User loads the module `amber-gpu/16p04-at16p10-gnu-intelmpi5.1-cuda7.5` and tries to run `pmemd.cuda.MPI`.
- Error message: `/var/spool/torque/mom_priv/jobs/713296.eadm.SC: line 37: pmemd.cuda.MPI: command not found`.
- Amber14 module works fine.

## Root Cause
- MPI-parallele GPU-Binaries were not built for Amber16 on Emmy.
- GPUs are connected via different PCIe paths, preventing direct GPU-GPU communication.

## Solution
- Use `pmemd.cuda` instead of `pmemd.cuda.MPI` for single GPU usage.
- Consider running two independent simulations on separate GPUs instead of parallel usage for efficiency.

## General Learnings
- Ensure MPI-parallele GPU-Binaries are built if required.
- Understand the efficiency implications of GPU-GPU communication via different PCIe paths.
- Provide guidance on optimal GPU usage for simulations.
---

### 2022081842002661_Software%20Woody-NG.md
# Ticket 2022081842002661

 # HPC Support Ticket: Software Woody-NG

## Keywords
- Woody-NG
- readline/readline.h
- libreadline-dev
- cmake/make
- RHEL-Paket "readline-devel"
- Login-Knoten
- User-spezifische Installation

## Problem
- User encountered an issue while compiling software on Woody-NG.
- The package `readline/readline.h` was not found.
- The user suspected the absence of a `libreadline-dev` version.
- Compilation was possible by manually disabling Readline in the cmake command.

## Root Cause
- The `readline-devel` package was not installed on the login nodes of Woody-NG.

## Solution
- HPC Admin installed the RHEL package `readline-devel` on the login nodes of Woody-NG.
- The package was also installed on `fritz/alex-Login` and added to `/srv/install/custom/incl/pkglist-login`.
- On `wadm2`, it was added to `/var/www/html/alma/alma-8.6-woody-ks.cfg`.

## General Learning
- Users can manually download, copy to the cluster, and perform user-specific installations as a valid option in such cases.
- HPC Admins can install missing development packages on login nodes to resolve compilation issues.

## Outcome
- The software compiled successfully after the installation of the `readline-devel` package.
---

### 42172371_Module%20ERROR%20within%20tinybluecluster.md
# Ticket 42172371

 # HPC Support Ticket: Module ERROR within tinybluecluster

## Keywords
- Module ERROR
- tinybluecluster
- OpenFOAM
- FOAM_INST_DIR
- Woody
- LiMa

## Summary
A user encountered a module error while running a job on tinybluecluster. The error occurred due to a missing variable `FOAM_INST_DIR` in the module file for OpenFOAM.

## Root Cause
- The module file for OpenFOAM (`/apps/modules/modulefiles/testing/openfoam/2.0.0-intel11.1-intel4.0up1`) references a variable `FOAM_INST_DIR` that is not defined, leading to a module error.
- The user previously ran the same job on Woody without issues, indicating a difference in the environment or module configuration between Woody and tinybluecluster.

## Solution
- HPC Admins noted that Woody and TinyBlue run different operating systems and that OpenFOAM 2.0 is not available for TinyBlue.
- The user was advised to either stay on Woody or use LiMa as an alternative.

## General Learnings
- Module files may contain environment-specific variables that need to be defined appropriately.
- Different clusters may have different software availability and compatibility.
- Users should be aware of the differences between clusters and choose the appropriate one based on software requirements.

## Actions Taken
- HPC Admins identified the issue with the module file and the difference in software availability between clusters.
- The user was advised to use a different cluster that supports the required software version.

## Follow-up
- Ensure that module files are properly configured and tested for all supported clusters.
- Communicate software availability and compatibility information to users clearly.
---

### 2022111742001345_Openfoam%206%20availability.md
# Ticket 2022111742001345

 # HPC Support Ticket: OpenFOAM 6 Availability

## Keywords
- OpenFOAM 6
- Software Installation
- User-Specific Installation
- Spack Package Manager

## Summary
A user requested the installation of OpenFOAM 6 on the HPC cluster, which is an outdated version not centrally available. The user needed this specific version for research purposes due to a custom solver developed based on OpenFOAM 6.

## Root Cause
- The user required OpenFOAM 6 for compatibility with a custom solver.
- The HPC cluster only had OpenFOAM 8 and 10 available.

## Solution
- The HPC Admin recommended installing OpenFOAM 6 in the user's `$WORK` directory.
- Suggested methods for installation:
  - Building from source.
  - Using Spack, a user-specific package manager available on the cluster.
- Documentation for Spack was provided: [Spack Package Manager Documentation](https://hpc.fau.de/systems-services/documentation-instructions/special-applications-and-tips-tricks/spack-package-manager/)

## General Learnings
- Users may require specific, outdated software versions for research continuity.
- User-specific installations can be a viable solution for such cases.
- Spack is a useful tool for managing user-specific software installations on HPC clusters.

## Actions Taken
- HPC Admin advised against central installation of outdated software.
- Provided guidance on user-specific installation methods.
- Directed the user to relevant documentation for Spack.

## Follow-up
- The user can proceed with installing OpenFOAM 6 in their `$WORK` directory using the provided methods.
- Further assistance may be required if the user encounters issues during installation.
---

### 42052771_OpenFoam.md
# Ticket 42052771

 # HPC Support Ticket: OpenFoam Installation

## Keywords
- OpenFoam
- rrze-Cluster
- woody
- cluster32
- Version

## Summary
A user inquired about the availability and version of OpenFoam on the rrze-Cluster, specifically on woody and cluster32.

## Root Cause
The user needed to know if OpenFoam was installed on the specified clusters and which versions were available.

## Solution
- **Initial Response:** The HPC Admin confirmed that OpenFoam versions 1.4.1 and 1.5 were installed.
- **Follow-up:** The HPC Admin later informed that OpenFoam version 1.7.1 was also installed and requested the user to test it and report any issues.

## General Learning
- Always check the availability and versions of software on specific clusters.
- Test new software versions and report any issues to the HPC Admin for further assistance.

## Action Items
- Verify the installation of OpenFoam on the specified clusters.
- Test the latest version of OpenFoam (1.7.1) and report any problems encountered.
---

### 2024031442003039_Tier3-Access-Fritz%20%22Michael%20Zikeli%22%20_%20iwia060h.md
# Ticket 2024031442003039

 ```markdown
# HPC Support Ticket Conversation Analysis

## Keywords
- Access Request
- Sapphire Rapids Nodes
- GCC13
- Mixed Precision
- Float16 Support
- Module Loading
- Spack Packages

## Summary
A user requested access to Sapphire Rapids nodes for mixed precision investigations, specifically requiring GCC13 for float16 support. The HPC Admin granted access and provided instructions on loading the necessary modules.

## Root Cause of the Problem
- User needed access to specific hardware (Sapphire Rapids nodes) and software (GCC13) for mixed precision investigations.

## Solution
- HPC Admin granted access to the requested hardware.
- Instructions were provided to load the `000-all-spack-pkgs/0.19.1` module to access GCC13.

## General Learnings
- **Access Requests**: Users may need specific hardware and software for their projects.
- **Module Loading**: Some software packages may be hidden within specific modules and require loading those modules to become accessible.
- **Spack Packages**: Understanding how to use Spack packages is crucial for accessing certain software versions.

## Steps for Similar Issues
1. **Grant Access**: Ensure the user has the necessary permissions to access the requested hardware.
2. **Provide Instructions**: Inform the user about any specific modules or packages they need to load to access the required software.
3. **Verify**: Confirm that the user can successfully access and use the requested resources.
```
---

### 2022091942000258_R_4.2.1-conda%20module%20on%20Woody-NG.md
# Ticket 2022091942000258

 # HPC Support Ticket: R/4.2.1-conda Module Issue on Woody-NG

## Keywords
- R version mismatch
- Module renaming
- Conda environment
- Job script update

## Problem
- The module `r/4.2.1-conda` on Woody-NG was activating R version 3.6.3 instead of 4.2.1.

## Root Cause
- Incorrect version mapping in the module configuration.

## Solution
- The existing module was renamed to `r/3.6.3-conda` to reflect the correct version.
- A new module `r/4.2.1-conda` was created to provide the correct version of R.

## Actions Taken
- **HPC Admins**:
  - Renamed the incorrect module to `r/3.6.3-conda`.
  - Created a new module `r/4.2.1-conda` with the correct R version.
  - Informed users to update their job scripts to reflect the correct module names.

## User Instructions
- Users relying on R version 3.6.3 should update their job scripts to use `r/3.6.3-conda`.
- Users requiring R version 4.2.1 should use the new `r/4.2.1-conda` module.

## General Learning
- Ensure module configurations accurately reflect the software versions they provide.
- Communicate changes and updates clearly to users to minimize disruption.
- Regularly verify the integrity of software modules to prevent version mismatches.
---

### 2017053142002811_curl%20auf%20memoryhog%3F.md
# Ticket 2017053142002811

 ```markdown
# HPC-Support Ticket: Installation of curl on memoryhog

## Keywords
- curl
- wget
- memoryhog
- installation
- HPC systems

## Problem
- The user noticed that `curl` is not available on the `memoryhog` system, while it is available on most other HPC systems.

## Root Cause
- `curl` was not installed on the `memoryhog` system.

## Solution
- The HPC Admin installed `curl` on the `memoryhog` system.

## What Can Be Learned
- The distribution of `curl` and `wget` across different HPC systems can vary.
- It is important to ensure that commonly used tools like `curl` are available on all systems to avoid user inconvenience.
- Quick response from HPC support can resolve such issues efficiently.
```
---

### 2024112542001353_ROCm%20Version%20aquavan1.md
# Ticket 2024112542001353

 ```markdown
# HPC Support Ticket: ROCm Version Rollback

## Keywords
- ROCm
- Version Rollback
- Compatibility Issues
- Apptainer Container
- Ubuntu 24.04.X

## Problem
- User unable to build all packages with ROCm version 6.2.1.
- Request to roll back to an older ROCm version.

## Root Cause
- Compatibility issues with ROCm 6.2.1 on Ubuntu 24.04.X.
- MI300X (gfx942) support is limited to Ubuntu 22.04.4 for ROCm 6.1.0.

## Solution
- HPC Admin suggests using an Apptainer container if older ROCm versions are compatible with current drivers.
- Rollback to ROCm 6.2.0 is possible but unlikely to resolve the issue due to similar software compatibility.

## General Learnings
- Understanding ROCm version compatibility with different Ubuntu versions.
- Using Apptainer containers as a solution for compatibility issues.
- Importance of checking compatibility matrices for hardware and software support.
```
---

### 42327253_Testing%20Intel%2015up1%20with%20VASP%20%28works%20extremely%20well%29.md
# Ticket 42327253

 # HPC Support Ticket: Intel MPI 5 Installation and Access Issues

## Keywords
- Intel MPI 5
- VASP
- NWCHEM
- Emmy
- LiMa
- Segmentation faults
- MPI-2 standards
- Threaded communication layer
- mpirun
- mpirun_rrze

## Summary
A user reported successful usage of Intel 15/up1 and Intel MPI 5 with VASP and NWCHEM on Emmy, noting improved stability compared to Intel 13/14 series compilers. The user requested the installation of Intel MPI 5 on LiMa to utilize MPI-2 standards.

## Issues and Solutions
1. **Request for Intel MPI 5 on LiMa**
   - **User Report**: Intel MPI 5 works well on Emmy; request for installation on LiMa.
   - **HPC Admin Action**: Intel MPI 5.0 installed on LiMa; Emmy updated to Intel MPI 5.0.2.

2. **Access Issues with mpirun and mpirun_rrze**
   - **User Report**: No access to mpirun or mpirun_rrze using Intel MPI 5.0.2.
   - **HPC Admin Action**: Added mpirun_rrze to resolve access issues.

## Lessons Learned
- Intel MPI 5 provides improved stability for applications like VASP and NWCHEM.
- Ensure that all necessary executables (e.g., mpirun, mpirun_rrze) are available after software updates.
- Regularly update software versions across different systems to maintain consistency.

## Root Cause of Problems
- Missing executables (mpirun, mpirun_rrze) after software update.

## Solution
- Added the missing executables to resolve access issues.

## Documentation for Future Reference
- When updating software, verify that all related executables are available and accessible.
- Regularly update software versions across systems to ensure consistency and compatibility.
---

### 2017051642001592_MPI%20compiler.md
# Ticket 2017051642001592

 # HPC Support Ticket: MPI Compiler Issue

## Keywords
- MPI compiler
- mpi.h library
- Intel Compiler
- Intel MPI
- OpenMPI
- Module loading

## Root Cause
- User unable to compile self-developed software due to missing `mpi.h` library.
- User unaware of which compiler to use and how to load necessary modules.

## Solution
- Load the Intel Compiler module (`intel64`) which automatically loads Intel MPI (`intelmpi`).
- Alternatively, load one of the `openmpi` modules.
- Use `module avail` to see all available modules.

## General Learnings
- Users need to load appropriate modules to access specific compilers and libraries.
- Intel Compiler module includes Intel MPI.
- OpenMPI is available as an alternative.
- `module avail` command lists all available modules.

## Steps for Support Employees
1. Instruct the user to load the Intel Compiler module using `module load intel64`.
2. Alternatively, suggest loading an OpenMPI module.
3. Advise the user to use `module avail` to explore other available modules.

## Related Documentation
- [RRZE HPC Documentation](http://www.hpc.rrze.fau.de/)
- Contact: [support-hpc@fau.de](mailto:support-hpc@fau.de)
---

### 2019052142000963_X11%20libraries%20installed.md
# Ticket 2019052142000963

 # HPC Support Ticket: X11 Libraries Installation

## Keywords
- X11 libraries
- Athena widgets library
- Xaw package
- udunits2.h
- ncview installation

## Problem
- User encountered an error while trying to install `ncview` locally due to missing Athena widgets library and header files.
- Compilation aborted due to missing `udunits2.h`.

## Root Cause
- Missing header files for X11 libraries and `udunits2.h` on the frontends.

## Solution
- HPC Admin installed `libxaw7-dev` on the frontends to provide the necessary header files for X11 libraries.
- User requested the installation of `udunits2.h`, but the resolution for this part is not explicitly mentioned in the provided conversation.

## General Learnings
- Ensure that necessary development libraries and headers are installed on the frontends for software compilation.
- Communication between the user and HPC Admin is crucial for resolving software installation issues.
- Some software dependencies might not be pre-installed and may require additional packages to be installed by the HPC Admin.

## Next Steps
- Verify if `udunits2.h` is installed or needs to be installed by the HPC Admin.
- Continue monitoring the compilation process to ensure all dependencies are met.
---

### 42174349_Rechnen%20auf%20dem%20LIMA%20cluster.md
# Ticket 42174349

 # HPC Support Ticket: Rechnen auf dem LIMA Cluster

## Keywords
- LIMA cluster
- WOODY cluster
- MKL (Math Kernel Library)
- Makefile
- Module system
- Environment variables
- Linking libraries

## Problem
- User encountered an error when trying to compile a program on the LIMA cluster that requires MKL.
- The error message indicated that "lmkl" could not be found.
- The user had previously run the same jobs on the WOODY cluster without issues.

## Root Cause
- The user's Makefile contained hard-coded paths specific to the WOODY cluster.
- The MKL library names and versions differ between the WOODY and LIMA clusters.

## Solution
- Use the module system to set environment variables for MKL.
- Replace hard-coded paths with environment variables provided by the module system.
- Example: Use `$MKL_LIB`, `$MKL_SHLIB`, `$MKL_LIB_THREADED`, etc., in the Makefile.
- For specific requirements, generate the linking line using the Intel MKL link line advisor.

## General Learnings
- Avoid hard-coding paths in Makefiles or scripts.
- Utilize the module system to manage software dependencies and environment variables.
- Be aware of differences in library names and versions across different clusters.
- Use tools provided by software vendors (e.g., Intel MKL link line advisor) for generating appropriate linking commands.

## References
- [Intel MKL Link Line Advisor](http://software.intel.com/sites/products/mkl/)
- [HPC Services at FAU](http://www.hpc.rrze.fau.de/)
---

### 42319788_Problem%20with%20shared%20libraries%20using%20openmpi%20versions%20%3E1.6.5.md
# Ticket 42319788

 # HPC Support Ticket: Problem with Shared Libraries using OpenMPI Versions >1.6.5

## Keywords
- OpenMPI
- libtool
- libpciaccess
- libnvidia-ml.so
- LD_LIBRARY_PATH
- Compilation Error

## Problem Description
The user encountered a compilation error when trying to use OpenMPI versions greater than 1.6.5. The `libtool` automatically added `libpciaccess` and `libnvidia-ml.so` to the linking process, which were not installed, causing the compilation to fail.

## Root Cause
- The `libtool` was adding non-existent libraries (`libpciaccess` and `libnvidia-ml.so`) when using OpenMPI 1.7.5-intel13.1.
- The libraries were not in the default `LD_LIBRARY_PATH`.

## Solution
- The user added `/usr/lib` and `/usr/lib64` to the `LD_LIBRARY_PATH` through the `.bashrc` file.
- This resolved the issue as the libraries were then found during the compilation process.

## General Learning
- Ensure that the necessary library paths are included in the `LD_LIBRARY_PATH`.
- Differences in OpenMPI versions can lead to different behaviors in the compilation process.
- Checking the default library paths and ensuring they are correctly set can resolve many compilation issues.

## HPC Admin Response
- The HPC Admin confirmed that the libraries were available on both login and compute nodes.
- They noted that `/usr/lib64` should be searched by default and that `/usr/lib` contains 32-bit libraries which are not needed for 64-bit executables.

## User Feedback
- The user resolved the issue by adding the necessary library paths to the `LD_LIBRARY_PATH`.
- They provided the steps taken to resolve the issue, including the commands used to verify the OpenMPI versions and the library paths.

## Conclusion
- The issue was resolved by ensuring that the necessary library paths were included in the `LD_LIBRARY_PATH`.
- This documentation can be used to troubleshoot similar issues in the future.
---

### 2022082542002335_GCC%20recommendation%20on%20meggie.md
# Ticket 2022082542002335

 # HPC Support Ticket: GCC Recommendation on Meggie

## Keywords
- GCC compiler
- CMake
- Meggie
- Emmy
- Compilation error
- Interactive node
- Frontend node

## Problem Description
- User is switching from Emmy to Meggie cluster.
- CMake is unable to detect the GCC compiler on Meggie.
- Minimal working example fails to compile with errors indicating missing `crt1.o` and `crti.o` files.

## Root Cause
- Attempting to compile on compute nodes, which have a stripped-down system lacking necessary development packages.

## Solution
- **Do not compile on compute nodes**: Compilation should be done on frontend nodes where the necessary development packages are available.
- **Switch to Meggie8**: Recommended by HPC Admin to avoid issues with Meggie.
- **Start fresh with CMake**: Ensure no cached data from previous clusters is causing issues.

## General Learnings
- Always compile on frontend nodes to avoid missing development packages.
- When switching clusters, ensure a fresh start to avoid cached data issues.
- Follow recommendations from HPC Admins regarding cluster versions to avoid known issues.

## Additional Notes
- Meggie compute nodes are not designed for compilation due to their minimal system setup.
- CMake may cache data that can cause issues when switching clusters, so starting fresh is important.

---

This documentation aims to help support employees quickly identify and resolve similar issues in the future.
---

### 2017090142001013_Multi-precision%20floats.md
# Ticket 2017090142001013

 ```markdown
# Multi-precision Floats Support

## Keywords
- Multi-precision floats
- C++
- Boost/mpfr
- mpfr-devel
- Emmy-Loginknoten

## Problem
- User attempted to use Boost/mpfr for multi-precision floats in C++ code.
- Compilation failed on Emmy due to the absence of the mpfr library.

## Solution
- HPC Admin installed the mpfr-devel package on the Emmy-Loginknoten.
- User confirmed the installation resolved the issue.

## Lessons Learned
- Ensure necessary libraries are installed on the HPC system before attempting to compile code that depends on them.
- Communicate with HPC support to request missing libraries.

## Actions Taken
- HPC Admin installed the mpfr-devel package.
- Ticket closed successfully.
```
---

### 2018100842002577_Intel%20MKL%202019%20fuer%20Woody.md
# Ticket 2018100842002577

 ```markdown
# HPC-Support Ticket Conversation: Intel MKL 2019 for Woody

## Keywords
- Intel MKL 2019
- Intel Compiler
- FEM Software CFS
- Woody
- Installation Request

## Problem
The user's FEM software (CFS) is not building with the current Intel Compiler on the Woody system. The issue is fixed in Intel MKL 2019.

## Root Cause
The current version of Intel MKL does not support the required features or fixes needed for the FEM software to build correctly.

## Solution
The user requests the installation of Intel MKL 2019 to resolve the build issue with their FEM software.

## General Learning
- Ensure that the software dependencies are up-to-date to avoid build issues.
- Communicate with HPC Admins for software installation requests.
- Keep track of software versions and their compatibility with other tools.
```
---

### 2018070942002152_Freischaltung%20f%C3%83%C2%BCr%20Meggie%20_%20Verwendung%20von%20OpenFOAM%20auf%20dem%20HPC.md
# Ticket 2018070942002152

 # HPC-Support Ticket Conversation Summary

## Subject: Freischaltung für Meggie / Verwendung von OpenFOAM auf dem HPC

### Keywords:
- Meggie access
- OpenFOAM compilation
- Compiler optimization flags
- SLURM script migration
- HPC cluster usage

### What Can Be Learned:

#### Meggie Access:
- **Issue**: User cannot start jobs on Meggie despite being able to log in.
- **Root Cause**: Meggie is not yet in normal operation and requires special permission for access.
- **Solution**: User needs to provide a detailed justification for their special computational needs to gain access.

#### OpenFOAM Compilation:
- **Issue**: User needs to compile OpenFOAM locally with specific optimizations.
- **Root Cause**: Default OpenFOAM installations on Emmy and Lima do not meet user requirements.
- **Solution**: User can compile OpenFOAM locally under their $HOME or $WOODYHOME directory. Prozessorspezifische Optimierungen are recommended to avoid performance loss.

#### Compiler Optimization Flags:
- **Issue**: User experiences hangs and crashes with certain compiler flags.
- **Root Cause**: Specific flags like `-march=native` and `-O3` can lead to instability.
- **Solution**: Use standard optimization flags (`-O3`) and avoid aggressive processor-specific optimizations unless thoroughly tested.

#### SLURM Script Migration:
- **Issue**: User anticipates needing to migrate scripts to SLURM for Meggie.
- **Root Cause**: Different job scheduling systems between clusters.
- **Solution**: User should start preparing SLURM scripts in advance to be ready for Meggie access.

### General Learnings:
- **Compiler Flags**: Be cautious with aggressive optimization flags as they can lead to instability.
- **OpenFOAM Compilation**: Local compilation is feasible but requires careful management of optimization flags.
- **Cluster Access**: Special permissions are required for accessing high-performance clusters like Meggie.
- **Script Migration**: Preparing for job scheduling system changes in advance can save time and effort.

### Additional Notes:
- **Email Address Update**: Ensure that the correct support email address (`support-hpc@fau.de`) is used in cluster documentation.
- **Compiler Recommendations**: Consult with other HPC centers for best practices in compiler flags and OpenFOAM compilation.

This summary provides a concise overview of the issues, root causes, and solutions discussed in the HPC-Support ticket conversation, serving as a reference for future support cases.
---

### 2023082242003221_Neko%20Compilation%20on%20the%20Clusters.md
# Ticket 2023082242003221

 ```markdown
# Neko Compilation on the Clusters

## Key Points Learned

1. **Compilation and Module Issues**:
   - The initial compilation of Neko using Spack had issues with MPI communication errors when scaling beyond 11 nodes.
   - The local compilation of Neko worked fine, indicating a potential issue with the Spack version.

2. **MPI Communication Errors**:
   - The Spack version of Neko encountered MPI communication errors when running on more than 11 nodes.
   - The local compilation did not have these issues, suggesting a problem with the Spack configuration or dependencies.

3. **Fortran Module Corruption**:
   - The Intel MPI version of Neko had issues with a corrupt Fortran module, specifically `neko.mod`.
   - This was resolved by setting the environment variable `I_MPI_FC=ifort` to ensure the correct Fortran compiler was used.

4. **Performance Comparison**:
   - The Intel MPI version of Neko was faster than the GCC + OpenMPI version.
   - The Intel compiler achieved better vectorization for solving the linear system of equations compared to GCC.

5. **Scaling Tests**:
   - Neko did not scale well beyond 2 nodes on the Alex cluster, with performance degrading and eventual divergence.
   - This issue was not resolved and may require further investigation into the code or cluster configuration.

6. **Job Script Best Practices**:
   - The job script should start with `#!/bin/bash -l`.
   - Adding `#SBATCH --export=NONE` and `unset SLURM_EXPORT_ENV` ensures a clean and reproducible environment for jobs.

## Solutions

1. **Fixing MPI Communication Errors**:
   - Ensure that the job script starts with `#!/bin/bash -l`.
   - Add `#SBATCH --export=NONE` and `unset SLURM_EXPORT_ENV` to the job script to ensure a clean environment.

2. **Resolving Fortran Module Corruption**:
   - Set the environment variable `I_MPI_FC=ifort` to ensure the correct Fortran compiler is used.

3. **Performance Optimization**:
   - Use the Intel MPI version of Neko for better performance and vectorization.

4. **Scaling Tests**:
   - Further investigation is needed to resolve the scaling issue beyond 2 nodes on the Alex cluster.
   - Ensure that the cluster configuration and code are optimized for multi-node execution.

## Conclusion

The compilation and scaling issues with Neko were partially resolved through local compilation and adjustments to the job script and environment variables. Further investigation is needed to fully resolve the scaling issue on the Alex cluster.
```
---

### 2024041142002311_amber%2022%20mit%20amber%20tools%2023%20auf%20tiny%20GPU.md
# Ticket 2024041142002311

 ```markdown
# HPC-Support Ticket Conversation: Amber 22 with Amber Tools 23 on Tiny GPU

## Keywords
- Amber 22
- Amber Tools 23
- Tiny GPU
- Installation
- Trajectory Analysis

## Problem
A user requested the installation of Amber 22 with Amber Tools 23 on Tiny GPU for trajectory analysis.

## Solution
HPC Admin confirmed the availability of "amber-gpu/22p05-at23p06-gnu-cuda11.8" on TinyGPU.

## What Can Be Learned
- **Software Availability**: HPC Admin can provide specific software versions and tools upon request.
- **User Requirements**: Users may need specific software versions for their research, such as trajectory analysis.
- **Communication**: Effective communication between users and HPC Admin ensures that necessary tools are made available.
```
---

### 42310588_Beispiel%20f%C3%83%C2%BCr%20OpenFOAM-Jobskript.md
# Ticket 42310588

 # HPC Support Ticket: Beispiel für OpenFOAM-Jobskript

## Keywords
- OpenFOAM
- Jobskript
- Intel MPI
- mpirun_rrze
- LikwidPin
- Memory Error
- Tinyfat Cluster

## Problem
- User is looking for example scripts for OpenFOAM.
- User is facing memory issues with a serial job on the Lima cluster.

## Conversation Summary
- **User**: Requested example scripts for OpenFOAM but couldn't find any.
- **HPC Admin**: Informed that there are no pre-made example scripts but suggested seeking help from other OpenFOAM users at LSTM.
- **User**: Shared a working script from the Lima cluster and asked about Intel MPI module for the Emmy cluster.
- **HPC Admin**: Explained that the Intel MPI module is automatically loaded with the OpenFOAM module and provided information on using LikwidPin expressions with `mpirun_rrze`.
- **User**: Reported a memory error ("runout of memory request") with a serial job on the Lima cluster and asked about running the job on the Tinyfat cluster.

## Solution
- **Example Scripts**: No pre-made example scripts available. Suggested seeking help from other OpenFOAM users.
- **Intel MPI Module**: Automatically loaded with the OpenFOAM module. No need to load a specific Intel MPI module.
- **LikwidPin**: Can be used with `mpirun_rrze` to simplify pinning arguments.
- **Memory Error**: Suggested running the job on the Tinyfat cluster, which has more memory.

## Additional Resources
- [LikwidPin Documentation](https://code.google.com/p/likwid/wiki/LikwidPin)
- [HPC Services at FAU](http://www.hpc.rrze.fau.de/)
---

### 2021070142001616_Testcluster%3A%20Compiler%20f%C3%83%C2%BCr%20Aurora.md
# Ticket 2021070142001616

 # HPC Support Ticket: Compiler for Aurora

## Keywords
- Aurora
- clang/clang++/llvm compiler
- VE-Intrinsics
- Compilation issues
- Memory limitations
- Cmake issues
- uname
- RPM packages
- CentOS/RHEL

## Problem Description
- User needs the clang/clang++/llvm compiler with VE-Intrinsics for Aurora cards.
- Available only as RPM packages or sources.
- Compilation attempts on the testfront failed due to insufficient memory.
- Compilation on the node failed due to issues with `uname` and Cmake.

## Root Cause
- Memory limitations on the testfront.
- Incompatibility between testfront (Ubuntu 18.04) and Aurora node (CentOS/RHEL 7.7).
- Issues with `uname` and Cmake on the node.

## Solution
- HPC Admins provided a pre-built RPM package for CentOS 7 from NEC.
- The package was installed on Aurora1.

## General Learnings
- Compiling on the testfront is not recommended due to OS incompatibilities.
- Ensure sufficient memory and time allocation for compilation tasks.
- Check for pre-built packages from vendors to avoid compilation issues.
- Be aware of the specific `uname` and Cmake requirements for different environments.

## Additional Notes
- The user was advised to try the Release configuration instead of the default Debug configuration to reduce memory usage during linking.
- The HPC Admins also mentioned the availability of a Docker container with llvm-ve-1.20.0 on CentOS 8, which can be used as an alternative.
---

### 42284482_VTK%20library.md
# Ticket 42284482

 # HPC Support Ticket: VTK Library

## Keywords
- VTK library
- LiMa cluster
- Module availability

## Summary
- **User Inquiry:** The user asked if the VTK (Visualization Toolkit) library is available as a module on the LiMa cluster.
- **HPC Admin Response:** The HPC Admin confirmed that the VTK library is not available as a module on the LiMa cluster.

## Root Cause
- The user needed to know if the VTK library was available as a module on the LiMa cluster.

## Solution
- The VTK library is not available as a module on the LiMa cluster.

## General Learning
- Always check the availability of specific software modules on the cluster before planning to use them.
- If a required module is not available, consider alternative methods such as compiling the software from source or requesting the module to be added by the HPC support team.

## Next Steps
- If the VTK library is essential for the user's work, they may need to compile it from source or request its addition to the cluster's module list.
- For further assistance, users can contact the HPC support team.
---

### 2018101242000418_Probleme%20mit%20pgi18.4%20modules.md
# Ticket 2018101242000418

 # HPC Support Ticket: Problem with pgi/18.4 Module

## Keywords
- pgi/18.4 module
- SPACK installation
- module load
- compiler path
- configuration issue

## Problem Description
The user attempted to load the `pgi/18.4` module on the HPC system but encountered issues where the compilers were not found. The `module show` command displayed a path that did not exist:
```
/apps/SPACK/opt/linux-centos7-x86_64/gcc-4.8.5/pgi-18.4-zol5utqef46l2a2tuuxqd5r2hszak66n/linux86-64/18.4/bin/pgcc
```

## Root Cause
The SPACK installation for the `pgi/18.4` module was experimental and fragile, leading to incorrect paths being displayed.

## Solution
The HPC Admin updated the paths in the PGI module, which should resolve the issue.

## General Learning
- SPACK installations can be experimental and fragile, leading to configuration issues.
- Incorrect paths in module configurations can cause issues with loading modules.
- Regular updates and maintenance of module configurations are necessary to ensure proper functionality.

## Next Steps
- Verify that the updated paths in the PGI module are correct.
- Test loading the `pgi/18.4` module to ensure it works as expected.
- Monitor for similar issues with other SPACK-installed modules and update configurations as needed.
---

### 2018070642000212_kompilieren%20von%20swak4Foam%20-%20fhn0001h.md
# Ticket 2018070642000212

 ```markdown
# HPC Support Ticket: Compiling swak4Foam

## Keywords
- OpenFOAM
- swak4Foam
- Bison
- Compilation
- Lima Cluster
- Emmy Cluster
- Intel Compilers

## Problem
- User encountered an error while trying to compile swak4Foam on the Lima cluster.
- Error message indicated that swak4Foam requires Bison 2.x, but the installed version is 3.0.4.

## Root Cause
- Incompatibility between swak4Foam and the installed version of Bison (3.0.4).

## Solution
- **Local Installation of Bison 2.x**:
  - User can run the provided script `./maintainanceScripts/compileRequirements.sh` to install Bison 2.x locally.
- **Alternative Cluster**:
  - If issues persist with Intel compilers, consider using the Emmy cluster with openfoam/5.0-trusty.

## General Learnings
- Always check the README and MessageBoard for common issues before seeking support.
- Local installation of required software versions can be a viable solution for compatibility issues.
- Different clusters may have different software configurations, which can resolve compatibility problems.
```
---

### 2017020142002847_Problem%20loading%20openfoam.md
# Ticket 2017020142002847

 # HPC Support Ticket: Problem Loading OpenFOAM

## Keywords
- OpenFOAM
- Module Load Error
- Permission Denied
- Directory Creation
- Downtime Notification

## Issue Description
The user encountered an error when attempting to load the OpenFOAM module on the Emmy cluster. The error message indicated a permission issue while trying to create a directory in the user's home directory.

## Error Message
```
Module ERROR: ERROR occurred in file
/apps/modules/data/applications/openfoam/2.2.1-intel13.1-intelmpi4.1:can't
create directory "/home/woody": permission denied
while executing
"file mkdir $WM_PROJECT_USER_DIR"
invoked from within
"if { [ module-info mode load ] } {
if { ! [ file isdirectory $WM_PROJECT_USER_DIR ] } {
puts stderr     "WARNING:
The user OpenFO..."
(file
"/apps/modules/data/applications/openfoam/2.2.1-intel13.1-intelmpi4.1" line
105)
invoked from within
"source $ModulesCurrentModulefile"
```

## Root Cause
The root cause of the problem was related to a recent downtime and upcoming changes to the `/home/woody` directory, as mentioned in an email notification from Jan. 25th.

## Solution
The HPC Admin advised the user to refer to the email notification titled "[RRZE-HPC] Woody-Downtime over, upcoming downtime /home/woody and cshpc" for the resolution.

## General Learnings
- Always check recent downtime notifications and updates from the HPC support team.
- Ensure that the user has the necessary permissions to create directories in their home directory.
- When contacting HPC support, use the official email address associated with the institution.

## Next Steps for Support
- Verify that the user has read and understood the downtime notification.
- Ensure that the user's home directory permissions are correctly set.
- Provide additional guidance if the user continues to experience issues.
---

### 42112529_OpenFOAM%20compilation%20problem.md
# Ticket 42112529

 ```markdown
# OpenFOAM Compilation Problem

## Keywords
- OpenFOAM
- Compilation
- wmake
- Intel Compiler
- feupdateenv warning

## Problem Description
The user encountered a warning message while attempting to compile a custom application for OpenFOAM-1.7.1 using `wmake` on the HPC system. The warning message was:
```
/apps/intel/Compiler/11.1/073/lib/intel64/libimf.so: warning: warning: feupdateenv is not implemented and will always fail
```

## Root Cause
The warning message is related to the Intel Compiler library `libimf.so` and the function `feupdateenv`, which is not implemented and will always fail.

## Solution
The HPC Admin confirmed that the warning message is harmless and can be safely ignored. No further action is required to resolve this issue.

## General Learning
- Warnings related to `feupdateenv` in the Intel Compiler library can be ignored during the compilation process.
- Always check with HPC support to confirm whether warnings are critical or can be safely ignored.
```
---

### 2022090742003483_svn%20missing%20on%20woody.ng.md
# Ticket 2022090742003483

 ```markdown
# HPC-Support Ticket: svn missing on woody.ng

## Keywords
- SVN
- woody
- woody-ng
- Frontend
- Package Installation

## Problem
- User noticed that SVN (Subversion) is not available on the new frontends of woody-ng.
- Required for versioning of scripts.

## Root Cause
- Missing SVN package on the new frontends.

## Solution
- HPC Admin installed the missing SVN package.

## What Can Be Learned
- Ensure all necessary software packages are installed on new frontends during migration.
- Quick response from HPC Admin resolved the issue promptly.
```
---

### 2023061542004103_Intel%20Compiler%20license%20issue.md
# Ticket 2023061542004103

 ```markdown
# Intel Compiler License Issue

## Keywords
- Intel Compiler
- License Issue
- Module Switch
- Deprecated Compiler

## Problem
- User encountered an error message with the Intel compiler license.
- Error message indicated that the user/host was not on the INCLUDE list for the feature.

## Root Cause
- Recent changes to the license server infrastructure by RRZE.
- The `license.opt` file was faulty, causing license denials.

## Affected Systems
- Tiny* and Testcluster with legacy Intel/2019.5 and Intel/2020.2 modules.

## Solution
- Switch to the newly provided modules: Intel/2022.1.0, Intel/2023.0.0, or Intel/2023.1.0.
- Ignore the deprecation warning message from the Intel compiler for now.

## Additional Notes
- The classic Intel C++ Compiler (ICC) is deprecated and will be removed in the second half of 2023.
- Intel recommends transitioning to the Intel oneAPI DPC++/C++ Compiler (ICX).
- The user can disable the deprecation warning message using `-diag-disable=10441`.
```
---

### 2023022742004321_elpa%20module.md
# Ticket 2023022742004321

 ```markdown
# HPC Support Ticket: elpa Module Issue

## Keywords
- elpa module
- typo error
- module system
- INCLUDE
- CPATH
- LIBRARY_PATH

## Problem Description
The user encountered a typo error in the `elpa/2021.11.001-impi-intel` module, which caused a module loading error. Additionally, the user needed the module system to include the INCLUDE, CPATH, and LIBRARY_PATH variables.

## Root Cause
- Typo in the module file: `moudle` instead of `module`.
- Missing INCLUDE, CPATH, and LIBRARY_PATH variables in the module system.

## Solution
- The HPC Admin corrected the typo in the module file.
- The HPC Admin added the INCLUDE, CPATH, and LIBRARY_PATH variables to the module system.

## Steps Taken
1. The user reported the typo error in the module file.
2. The HPC Admin fixed the typo error.
3. The user requested the addition of INCLUDE, CPATH, and LIBRARY_PATH variables.
4. The HPC Admin added the requested variables to the module system.

## Conclusion
The issue was resolved by correcting the typo and adding the necessary variables to the module system. This ensures that the elpa module can be loaded correctly and the required paths are set.
```
---

### 2019082142001279_intel64_17.0up05%20auf%20Woody%20inkompatibel%20mit%20Ubuntu%2018.04%20_%20glibc-2.26%2B.md
# Ticket 2019082142001279

 # HPC Support Ticket: Intel Composer Compatibility Issue

## Keywords
- Intel Composer 2017/2018
- Ubuntu 18.04
- glibc-2.26/2.27
- Compilation Error
- Amber
- CentOS-8
- Intel-MPI 2019
- QDR-Infiniband

## Problem Description
The default Intel Composer module (intel64/17.0up05) on Woody is causing compilation errors when compiling Amber. The error message indicates that the identifier "_Float32" is undefined. This issue is likely due to incompatibility between Intel Composer 2017/2018 and Ubuntu 18.04, specifically with glibc-2.26/2.27.

## Root Cause
- Incompatibility between Intel Composer 2017/2018 and Ubuntu 18.04 (glibc-2.26/2.27).

## Additional Information
- Intel-MPI 2019 produces incorrect results on Emmy.
- Intel-MPI >= 2018 is significantly slower on QDR-Infiniband.
- Consideration for upgrading to a newer version of the compiler and MPI is necessary, especially with the upcoming transition to CentOS-8 on Emmy/Meggie.

## Solution
- No immediate solution provided. The default version will be left unchanged for now as no other users have reported issues.

## Next Steps
- Evaluate and plan for upgrading the compiler and MPI versions, considering compatibility with CentOS-8 and performance on QDR-Infiniband.

## Notes
- This issue highlights the importance of testing software compatibility with different operating systems and library versions.
- Regular updates and testing of software versions are crucial to avoid such issues in the future.

---

This documentation can be used as a reference for similar issues that may arise in the future.
---

### 2017050542001773_Libraries%20auf%20Tinyfat.md
# Ticket 2017050542001773

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject: Libraries auf Tinyfat

### Keywords:
- Libraries
- tf056
- libaio1
- libaio-dev

### Root Cause of the Problem:
- User requests installation of specific libraries (libaio1 and libaio-dev) on the tf056 node.

### Solution:
- The request was forwarded to the HPC Admins for further action.

### General Learnings:
- Users may require specific libraries for their work on HPC nodes.
- Requests for library installations should be directed to the HPC Admins for evaluation and implementation.

### Actions Taken:
- The user's request was acknowledged and forwarded to the HPC Admins.

### Next Steps:
- HPC Admins need to review the request and install the required libraries if feasible.
- Communicate the outcome to the user.
```
---

### 2020120242002347_LUA%20library%20and%20MPI%3A%20issues.md
# Ticket 2020120242002347

 ```markdown
# HPC-Support Ticket: LUA Library and MPI Issues

## Summary
User encountered issues running Elmer/Ice model with LUA functions on the HPC system. The initial error was related to MPI startup and missing environment variables.

## Keywords
- Elmer/Ice
- LUA
- MPI
- IntelMPI
- SLURM
- OMP_NUM_THREADS
- Module Environment

## Problem
- **MPI Startup Error**: `MPI startup(): PMI server not found. Please set I_MPI_PMI_LIBRARY variable if it is not a singleton case.`
- **LUA Error**: `Caught LUA error: attempt to call a nil value`
- **Inconsistent Environment**: Potential conflicts due to multiple module loads and environment settings.

## Root Cause
- Missing MPI variable in the `intelmpi/2020up02-intel` module.
- Inconsistent module environment leading to conflicts and errors.
- Missing `srun` in the job script, causing inefficient CPU usage.

## Solution
1. **Load Specific IntelMPI Module**:
   - Explicitly load `intelmpi/2020up02-intel` to resolve MPI startup issues.

2. **Set OMP_NUM_THREADS**:
   - Add `export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK` to the job script to set the number of OpenMP threads.

3. **Use `srun` in Job Script**:
   - Ensure the job script uses `srun` to efficiently utilize allocated CPUs.
   ```bash
   srun ElmerSolver SolutionFiles/Stokes_diagnostic_thermomech_LUA.sif > out.out
   ```

4. **Module Environment Management**:
   - Use private module files to prevent inconsistent environments.
   - Add the following to `.bashrc`:
     ```bash
     # uncomment next line to supersede shared modules
     # with your private module repo
     module use -a $HOME/modules
     ```
   - Create a minimal module file for Elmer/Ice:
     ```bash
     #%Module
     # documentation how the software was built
     Set pkghome /home/titan/gwgk/gwgk005h/models/elmerfem/install/elmerice
     module purge
     Module add netcdf cmake intel/
     setenv ELMER_HOME=$pkghome
     prepend-path LD_LIBRARY_PATH=$pkghome/lib/elmersolver
     prepend-path PATH=$pkghome/bin
     unset pkghome
     ```

## Conclusion
The user successfully resolved the LUA script issues by using the `intel64/19.0up01` compiler. The root cause of the initial problems was an inconsistent module environment and missing MPI variables. Proper module management and job script adjustments resolved the issues.
```
---

### 2021020542001494_modules%20environment%20openFaom.md
# Ticket 2021020542001494

 # HPC Support Ticket: Modules Environment OpenFOAM

## Keywords
- OpenFOAM
- Module Environment
- SLURM
- Ubuntu
- Modulefile
- Compilation

## Summary
The user from the Institute for Water Engineering and Water Management (IWWN) at TH Nürnberg is setting up a small server for OpenFOAM simulations and preprocessing. The server runs on Ubuntu with SLURM. The user wants to compile different OpenFOAM versions and load them via the module environment but has not been successful in integrating OpenFOAM into this environment.

## Problem
- The user needs help creating a modulefile for OpenFOAM.
- The user is unsure about the parameters to set in the modulefile.
- OpenFOAM is compiled under `/opt/openfoam/OpenFOAM-<version>`.
- The module files are expected to be placed under `/usr/share/modules/modulefiles/`.

## Solution
- The HPC Admin suggests looking at existing OpenFOAM modules located at `/apps/modules/data/applications/openfoam/*`.
- The HPC Admin also mentions the `createmodule.py` script, which can help convert the OpenFOAM bashrc script into a modulefile.

## Additional Information
- The user initially thought they did not have the necessary permissions to view the existing OpenFOAM modules.
- The HPC Admin provides guidance on using the `createmodule.py` script to assist in creating the modulefile.

## Conclusion
The user is advised to review the existing OpenFOAM modules and use the `createmodule.py` script to create the necessary modulefile for their OpenFOAM versions. This should help in integrating OpenFOAM into the module environment on their server.
---

### 2019012842001064_interFoam%20in%20OpenFoam%204.1%20not%20working.md
# Ticket 2019012842001064

 # HPC Support Ticket: interFoam in OpenFoam 4.1 Not Working

## Keywords
- interFoam
- OpenFoam 4.1
- OpenFoam 5.0
- Emmy
- Error Report
- Internal Error
- Bug

## Problem Description
- User encountered an error while running interFoam in OpenFoam 4.1 on Emmy.
- The same simulation settings worked in OpenFoam 5.0-trusty on Emmy.
- The error message indicated an internal error (bug) in OpenFOAM-4.

## Root Cause
- The error message `*** Error in 'interFoam': corrupted size vs. prev_size: 0x0000000002e39e60 ***` suggests an internal bug in OpenFOAM-4.
- The OpenFoam-4 installation had not been changed since May 2017, indicating a possible regression or compatibility issue.

## Solution
- The user was advised to use OpenFOAM-5 as the error did not occur there.
- No further action was taken by the HPC Admins as the issue was identified as an internal bug in OpenFOAM-4.

## Additional Information
- The user had been successfully running simulations with interFoam in OpenFoam 4.1-trusty for over a year, with the last successful run in November 2018.
- The OpenFoam-4 installation had not been modified since May 2017.

## Conclusion
- The issue was resolved by advising the user to switch to OpenFOAM-5.
- The error was attributed to an internal bug in OpenFOAM-4, with no further action possible from the HPC Admins.
---

### 2021031342000227_Issue%20Compiling%20Lammps%20GPU%20Package%20on%20Woody.md
# Ticket 2021031342000227

 ```markdown
# HPC-Support Ticket: Issue Compiling Lammps GPU Package on Woody

## Summary
User encountered issues compiling the GPU package of Lammps on Woody due to GCC version limitations and CUDA configuration errors.

## Keywords
- Lammps
- GPU Package
- CUDA
- GCC Version
- CMake
- Spack
- HPC
- Woody
- TinyGPU

## Problem
- User attempted to compile Lammps with CUDA on Woody but faced errors due to GCC version limitations (Lammps supports up to GCC 6.0, but Woody has GCC 9.1).
- User tried changing the makefile from g++ to intel but still encountered issues.
- CMake errors related to missing CUDA libraries.

## Root Cause
- Incompatibility between the required GCC version and the available version on Woody.
- Misconfiguration of CUDA libraries in CMake.

## Solution
- HPC Admins suggested using Spack to install Lammps with the CUDA package.
- HPC Admins provided a new Lammps module (`lammps/20201029-gcc9.2.0-openmpi-mkl`) that resolved the issue.
- User was instructed to load the new Lammps module and use the following command to run simulations:
  ```sh
  mpirun -np 4 lmp -pk gpu 4 -in ...
  ```

## Additional Notes
- User's HPC access expired, and they were guided on how to extend their access.
- A Zoom meeting was scheduled to further assist the user with their simulations.
- User provided input files for testing, and HPC Admins successfully ran a simulation with the provided input set.

## Conclusion
The issue was resolved by using a pre-compiled Lammps module that included the necessary GPU support. The user was able to run their simulations successfully.
```
---

### 2022081742001244_Compile-Fehler%20auf%20Meggie.md
# Ticket 2022081742001244

 ```markdown
# HPC Support Ticket Conversation Analysis

## Subject: Compile-Fehler auf Meggie

### Keywords:
- Compilation error
- Boost library
- Module loading
- OS upgrade
- Time synchronization
- Intel MPI

### Summary:
The user encountered a compilation error related to the Boost library on the Meggie cluster. The error message indicated that the source file `boost/math/special_functions/beta.hpp` could not be found. The user attempted to load different versions of the Boost library but was unable to resolve the issue. The problem was initially suspected to be related to a recent OS upgrade to AlmaLinux8.

### Root Cause:
- The issue was traced to a time synchronization problem on the Meggie nodes. The nodes had incorrect time settings due to a misconfiguration in the `chrony` service, which affected the compilation process.

### Solution:
- The HPC Admin identified and fixed the time synchronization issue by configuring `chrony` correctly. This resolved the Boost library compilation error.

### Additional Issues:
- After resolving the Boost library issue, the user encountered new compilation errors related to "undefined reference to `_intel_fast_memset`".
- The user noted that they previously used the `intel64` module, which had worked before the OS upgrade.

### Follow-up Actions:
- The HPC Admin updated the Intel MPI documentation to reflect the changes and ensure accurate information for users.
- The user was advised to refer to the updated documentation for further troubleshooting.

### General Learnings:
- Time synchronization issues can affect various aspects of HPC operations, including compilation.
- Proper configuration of time synchronization services like `chrony` is crucial for maintaining system stability.
- Documentation should be kept up-to-date to reflect changes in the software environment and to assist users in troubleshooting.
- Users should be aware of the impact of OS upgrades on their workflows and module dependencies.
```
---

### 2025012442000435_no%20mpi_java%20in%20java.library.path.md
# Ticket 2025012442000435

 # HPC Support Ticket: no mpi_java in java.library.path

## Keywords
- MPI with Java
- openmpi
- java.library.path
- UnsatisfiedLinkError
- SLURM script
- module load
- spack

## Problem Description
The user is attempting to parallelize a Java script using MPI but encounters an error indicating that `mpi_java` is not found in the `java.library.path`. The user is loading the `openmpi/4.1.3-nvhpc22.3` module and the `java/jdk8u345-b01-hotspot` module. The error occurs when running a command that includes `mpirun` and `java`.

## Root Cause
The root cause of the problem is that the MPI library being used does not have Java support built-in. The user's Java-MPI implementation may have been built with a different MPI version than the one being loaded.

## Ticket Conversation Summary
- The user initially reports the issue with the error message and provides a reproducible example.
- HPC Admins discuss the availability of the `openmpi/4.1.3-nvhpc22.3` module and its relevance.
- The user is asked for more details about the modules used and the build process of the Java application.
- The user confirms that the issue persists with different openmpi modules.
- HPC Admins suggest building an openmpi module with Java support using Spack.

## Solution
The user is advised to build an openmpi module with Java support using Spack. The following steps are provided:

1. Load the `user-spack` module:
   ```bash
   module add user-spack/0.19.1
   ```

2. Install openmpi with Java support:
   ```bash
   spack install openmpi@4.1.3 +java
   ```

3. Load the newly built openmpi module in the job script:
   ```bash
   module load user-spack/0.19.1
   module load openmpi/4.1.3-gcc8.5.0-f652apx  # Adjust the module name if necessary
   ```

## General Learnings
- MPI with Java is uncommon and may require specific configurations.
- The `openmpi` module may not have Java support by default.
- Using Spack to build custom modules with specific features can resolve compatibility issues.
- Experimenting with different openmpi modules may help identify compatibility issues.
- Clear communication and detailed error reporting are essential for troubleshooting complex issues.
---

### 2018050242002383_Weitere%20zu%20installierende%20Software.md
# Ticket 2018050242002383

 # HPC Support Ticket: Additional Software Installation

## Keywords
- Software installation
- Fortran
- GTK libraries
- Dependencies
- Modules
- User self-service

## Summary
A user requested the installation of additional software packages, including Fortran and GTK libraries, and inquired about making them available as modules. The HPC admin discussed the dependencies and context required for the installation.

## Root Cause
- User identified missing software packages during testing.
- Need for additional Fortran and GTK libraries.

## Solution
- HPC admin installed the required dev-packages on the specified system (woody3).
- User was informed about the installation and offered guidance on self-service if needed.

## Lessons Learned
- Importance of understanding the context and previously installed software.
- Handling dependencies for software installations.
- Offering self-service options to users for future installations.

## Actions Taken
- HPC admin installed the missing dev-packages.
- Communication with the user to confirm the installation and offer further assistance.

## Follow-up
- Ensure the user is aware of the self-service options for future software installations.
- Document the installed software and dependencies for future reference.

---

This documentation can be used to address similar requests for software installations and managing dependencies on HPC systems.
---

### 2018080242001441_Invalid%20Pointer%20OpenFoam.md
# Ticket 2018080242001441

 # HPC Support Ticket: Invalid Pointer OpenFoam

## Keywords
- OpenFoam
- sprayFoam
- double free or corruption
- invalid pointer
- cluster
- simulation
- error
- log file

## Summary
A user encountered an error while running an OpenFoam simulation on the cluster. The error messages indicated a "double free or corruption" and an "invalid pointer" issue. This problem only occurred when running the simulation on the cluster, not on local machines.

## Root Cause
The error messages suggest a programming error within the `sprayFoam` application, specifically related to memory management (double free or corruption and invalid pointer).

## HPC Admin Response
- The OpenFoam installation has not been modified.
- The binaries are provided as-is, and the HPC team has no control over them.
- The error indicates a potential bug in the `sprayFoam` application.

## Solution
No immediate solution was provided in the ticket. The user was informed that the issue likely stems from a programming error within `sprayFoam`.

## General Learnings
- Memory management errors (double free or corruption, invalid pointer) can occur in complex simulations like those run with OpenFoam.
- Such errors may be specific to the cluster environment and not reproducible on local machines.
- The HPC team may not have control over third-party binaries and cannot directly fix programming errors within them.
- Users should be aware that some issues may require debugging by the software developers or community support.

## Next Steps
- Users encountering similar issues should check for updates or patches to the software.
- Consulting the software's documentation or community forums for known issues and solutions is recommended.
- If the problem persists, users may need to contact the software developers for further assistance.
---

### 2023060242001631_Installation%20of%20Clang%20Compiler.md
# Ticket 2023060242001631

 # HPC-Support Ticket: Installation of Clang Compiler

## Keywords
- Clang Compiler
- LLVM
- Spack
- GCC
- Intel Compiler (icx)
- Texinfo
- makeinfo

## Problem Description
- User requires Clang Compiler on the cluster.
- Installation of LLVM via Spack fails.
- Loaded modules: `000-all-spack-pkgs/0.18.0`, `user-spack/0.18.0`, `gcc/11.2.0`.
- Error during `binutils` installation: `makeinfo` command not found.

## Root Cause
- Spack attempts to use the Intel compiler (icx) despite the GCC module being loaded.
- Missing `makeinfo` command due to the absence of the Texinfo package.

## Solution
1. **Add GCC to Spack Compilers:**
   ```bash
   $ module load gcc/11.2.0 user-spack
   $ spack compilers find
   ```
   This step adds GCC to the known compilers in Spack.

2. **Install LLVM with GCC:**
   ```bash
   $ spack install llvm%gcc@11.2.0
   ```
   This command specifies the use of GCC for the LLVM installation.

## General Learnings
- Ensure the correct compiler is recognized by Spack.
- Verify that all necessary dependencies (e.g., Texinfo for `makeinfo`) are installed.
- Use specific compiler specifications in Spack commands to avoid conflicts.

## Roles Involved
- **HPC Admins:** Provided detailed instructions and identified the root cause.
- **2nd Level Support Team:** Assisted in troubleshooting and resolving the issue.

## Additional Notes
- The user's environment might not recognize the loaded GCC version, leading to conflicts.
- Always check the build log for missing dependencies or incorrect compiler usage.
---

### 42112136_ccm26ToFOAM%20auf%20woody.md
# Ticket 42112136

 # HPC Support Ticket: ccm26ToFOAM auf woody

## Keywords
- OpenFOAM 1.7.1
- ccm26ToFOAM
- Compilation
- Woody
- starccm+ Gitter

## Problem
- User requires the `ccm26ToFOAM` application, which is not automatically compiled during OpenFOAM installation.
- User inquires whether HPC Admins can compile the application for all users or if they should attempt to install it themselves.

## Solution
- HPC Admin confirms that `ccm26ToFOAM` is now included in the OpenFOAM 1.7.1-intel11.1-impi4.0 environment on Woody.

## General Learnings
- Additional applications in OpenFOAM may not be automatically compiled during installation.
- Users can request HPC Admins to compile specific applications for broader access.
- HPC Admins can update the environment to include requested applications.

## Actions Taken
- HPC Admin compiled and included `ccm26ToFOAM` in the OpenFOAM 1.7.1-intel11.1-impi4.0 environment on Woody.

## Recommendations
- Users should check the availability of additional OpenFOAM applications in their environment before attempting to compile them manually.
- HPC Admins should communicate updates to the software environment to users.
---

### 2023071342003857_Missing%20clang%20compiler%20and%20sporadic%20ssh%20errors%20with%20Visual%20Studio%202022%20remote%.md
# Ticket 2023071342003857

 ```markdown
# HPC-Support Ticket Conversation Summary

## Subject: Missing clang compiler and sporadic ssh errors with Visual Studio 2022 remote compile

### User Information:
- Account: b179dc10
- NHR-Request-ID: b179dc
- NHR-Acronym: XXL-CT-Segmentation

### Problems:
1. **Missing Packages**:
   - Required packages: `clang-12`, `libomp-12-dev`, `ninja-build`.
   - No suitable modules found via `module avail`.

2. **SSH Connection Issues**:
   - Intermittent SSH connection failures when using Visual Studio 2022's remote compile feature.
   - Errors: "Could not connect to the remote system" and "Could not connect to the remote system or the connection was lost."

### Logs:
- **Build Log A**:
  ```
  Copying files to the remote machine.
  Starting copying files to remote machine.
  Finished copying files (elapsed time 00h:00m:04s:803ms).
  CMake generation started for configuration: 'Linux-Clang-Release'.
  Could not connect to the remote system
  ```

- **Cross Platform Logging A**:
  ```
  [Info, Thread 14] liblinux.RemoteSystemBase: Connecting over SSH to alex.nhr.fau.de:22
  [Info, Thread 1] liblinux.RemoteSystemBase: Connecting over SSH to alex.nhr.fau.de:22
  [Info, Thread 15] liblinux.IO.RemoteFileSystemImpl: Connecting over SFTP to alex.nhr.fau.de:22
  [Info, Thread 1] liblinux.RemoteSystemBase: Disconnecting over SSH from "alex.nhr.fau.de:22"
  [Info, Thread 1] liblinux.RemoteSystemBase: Connecting over SSH to alex.nhr.fau.de:22
  [Error, Thread 14] liblinux.RemoteSystemBase: Connection failure over SSH to alex.nhr.fau.de:22
  [Error, Thread 15] liblinux.RemoteSystemBase: System.OperationCanceledException: The operation was canceled.
  ```

- **Build Log B**:
  ```
  Copying files to the remote machine.
  Starting copying files to remote machine.
  Could not connect to the remote system or the connection was lost.
  ```

- **Cross Platform Logging B**:
  ```
  [Info, Thread 1] liblinux.RemoteSystemBase: Connecting over SSH to alex.nhr.fau.de:22
  [Info, Thread 1] liblinux.IO.RemoteFileSystemImpl: Connecting over SFTP to alex.nhr.fau.de:22
  [Info, Thread 1] liblinux.Shell.CommonCommandBase: Command "cat /etc/os-release" finished with exit code 0 after 47,0333ms
  [Info, Thread 1] liblinux.Shell.CommonCommandBase: Command "uname -m" finished with exit code 0 after 59,7228ms
  [Info, Thread 1] liblinux.Shell.CommonCommandBase: Command "uname -r" finished with exit code 0 after 59,6554ms
  [Info, Thread 1] liblinux.Shell.CommonCommandBase: Command "g++ -v" finished with exit code 0 after 7,2657ms
  [Info, Thread 1] liblinux.Shell.CommonCommandBase: Command "clang++ -v" finished with exit code 127 after 53,0451ms
  [Info, Thread 1] liblinux.Shell.CommonCommandBase: Command "gdbserver --version" finished with exit code 127 after 45,1795ms
  [Info, Thread 1] liblinux.Shell.CommonCommandBase: Command "gcc -v" finished with exit code 0 after 6,9757ms
  [Info, Thread 1] liblinux.Shell.CommonCommandBase: Command "gdb -v" finished with exit code 0 after 129,9315ms
  [Info, Thread 1] liblinux.Shell.CommonCommandBase: Command "/usr/bin/gdb -v" finished with exit code 0 after 135,4923ms
  [Info, Thread 1] liblinux.Shell.CommonCommandBase: Command "/usr/local/bin/gdb -v" finished with exit code 127 after 59,4307ms
  [Info, Thread 1] liblinux.Shell.CommonCommandBase: Command "rsync -v" finished with exit code 1 after 12,8969ms
  [Info, Thread 1] liblinux.Shell.CommonCommandBase: Command "lldb -v" finished with exit code 127 after 61,6082ms
  [Info, Thread 1] liblinux.Shell.CommonCommandBase: Command "ninja --version" finished with exit code 127 after 60,5979ms
  [Info, Thread 1] liblinux.Shell.CommonCommandBase: Command "cmake --version" finished with exit code 127 after 59,376ms
  [Info, Thread 1] liblinux.Shell.CommonCommandBase: Command "make -v" finished with exit code 0 after 59,5385ms
  [Info, Thread 1] liblinux.RemoteSystemBase: Disconnecting over SSH from "alex.nhr.fau.de:22"
  [Info, Thread 1] liblinux.IO.RemoteFileSystemImpl: Disconnecting over SFTP from alex.nhr.fau.de:22
  ```

### Solution:
1. **Missing Packages**:
   - Use Spack to install the required packages.
   - Example commands:
     ```sh
     module add user-spack
     spack install --fail-fast llvm@12.0.1
     spack install ninja
     ```
   - After installation, load the `user-spack` module to see the new modules.

2. **SSH Connection Issues**:
   - The issue is likely due to rate-limiting of SSH connections.
   - Visual Studio opens and closes many SSH connections, causing timeouts.
   - Solution: Reduce the number of SSH connections Visual Studio makes per time.

### Additional Information:
- New modules available on Alex:
  - `ninja/1.11.1`
  - `llvm/15.0.4` (latest version from SPACK-0.19.1)

### References:
- [Spack Documentation](https://hpc.fau.de/systems-services/documentation-instructions/special-applications-and-tips-tricks/spack-package-manager/)
- [Official Spack Documentation](https://spack.readthedocs.io/en/latest/)
```
---

### 2024080542003734_Aktualisierung%20glibc.md
# Ticket 2024080542003734

 ```markdown
# HPC-Support Ticket: Updating glibc

## Keywords
- glibc
- tanh function
- Singularity container
- spack
- system-glibc

## Problem
- User needs to use a specialized vectorized `tanh` function from glibc 2.40.
- Current HPC system (fritz) runs glibc 2.28, which does not include this function.
- User attempted to compile a newer version of gcc and glibc using spack but encountered issues as spack uses the system-glibc.

## Root Cause
- The required `tanh` function is not available in the current glibc version on the HPC system.

## Solution
- HPC Admin recommends using a Singularity container that includes the required glibc version and the user's program.
- This approach avoids the complexity of integrating a new glibc version with other system packages like binutils.

## General Learning
- Updating glibc on an HPC system can be complex due to dependencies on other packages.
- Singularity containers provide a convenient way to use specific software versions without affecting the system environment.
- Spack may not be suitable for updating system-level libraries like glibc due to its reliance on the system-glibc.
```
---

### 2023042842002942_HREMD%20with%20pmemd.cuda.MPI.md
# Ticket 2023042842002942

 # HPC-Support Ticket: HREMD with pmemd.cuda.MPI

## Subject
HREMD with pmemd.cuda.MPI

## User Issue
The user was unable to find the `pmemd.cuda.MPI` command after loading the standard Amber module (`amber/20p12-at21p11-gnu-cuda11.5`). The user also tried loading `amber/20p12-at21p11-openmpi-gnu-cuda11.5` but encountered the error `-bash: pmemd.cuda.MPI: command not found`.

## Root Cause
The link from `pmemd.cuda.MPI` to `pmemd.cuda_SPFP.MPI` was missing in the module.

## Solution
The HPC Admin fixed the missing link, and the `pmemd.cuda.MPI` command was found in the module `amber/20p12-at21p11-openmpi-gnu-cuda11.5`.

## Additional Information
- The user was allocated 16 CPU cores per GPU, which is fixed and cannot be changed.
- The user inquired about using 38 CPU cores for a future job, but it was advised that this is not possible.
- The user was advised to use the `mpirun --oversubscribe` option to start more MPI processes than available CPU cores.
- The user provided input files for testing and was advised to use 32 replicas instead of 38 due to performance considerations.
- The user was informed about the potential benefits of using multiple GPUs for HREMD simulations.
- The user was provided with benchmark results and scripts for running HREMD simulations with MPS (Multi-Process Service) on A40 and A100 GPUs.
- The user was advised on the meaning of specific script commands, such as `unset SLURM_EXPORT_ENV` and `export CUDA_MPS_PIPE_DIRECTORY=/tmp/nvidia-mps.$SLURM_JOB_ID`.

## Keywords
- HREMD
- pmemd.cuda.MPI
- Amber
- GPU
- MPI
- Oversubscribe
- MPS
- Performance
- Benchmark
- Script

## General Learnings
- Ensure all necessary links and commands are present in the module.
- Understand the allocation of CPU cores per GPU and the limitations.
- Use the `mpirun --oversubscribe` option to start more MPI processes than available CPU cores.
- Consider the number of replicas and the potential benefits of using multiple GPUs for HREMD simulations.
- Provide benchmark results and scripts for running simulations with MPS on different GPUs.
- Explain the meaning of specific script commands to the user.
---

### 2023071242002234_ROCm%205.6%20auf%20rome2.md
# Ticket 2023071242002234

 ```markdown
# HPC-Support Ticket: ROCm Update on rome2

## Keywords
- ROCm
- Update
- Bug Fixes
- rome2
- Version 5.6.x

## Summary
- **User Request**: Update ROCm stack on rome2 to version 5.6.x due to bug fixes.
- **HPC Admin Response**: Successfully updated ROCm to version 5.6.

## Root Cause
- Outdated ROCm version causing bugs.

## Solution
- Updated ROCm stack to version 5.6.

## Lessons Learned
- Regular updates of software stacks can resolve known bugs and improve performance.
- Collaboration between users and HPC admins is crucial for identifying and resolving issues.
```
---

### 2021120142001679_Rome2%20test%20cluster.md
# Ticket 2021120142001679

 # HPC Support Ticket: Rome2 Test Cluster

## Keywords
- CMakeLists.txt
- cmake
- hipConfig.cmake
- ROCm library
- GPU/accelerator code
- Rome2 cluster
- testfront

## Problem
- User encountered an error while running `cmake .` due to missing `hipConfig.cmake`.
- The issue might be related to the absence of the ROCm library or incorrect directory usage.

## Root Cause
- The user was attempting to compile GPU/accelerator code on a machine (testfront) that does not have the necessary hardware.

## Solution
- Compile the code on a machine that has the required hardware, specifically on the Rome2 cluster.
- Ensure that the ROCm toolkit is installed and properly configured on the target machine.

## Lessons Learned
- GPU/accelerator code must be compiled on machines with the appropriate hardware.
- Ensure that necessary libraries (e.g., ROCm) are installed and correctly configured.
- Verify the directory and environment before running compilation commands.

## Actions Taken
- HPC Admins clarified that the compilation should be done on Rome2.
- User corrected the directory and attempted the compilation on Rome2.

## Follow-Up
- Ensure that the user has access to the necessary resources and libraries on Rome2.
- Provide documentation or guidance on setting up and using ROCm on the cluster.
---

### 2024051442002394_Problem%20mit%20SLURM%20auf%20Alex.md
# Ticket 2024051442002394

 # HPC Support Ticket: Problem mit SLURM auf Alex

## Keywords
- SLURM
- OpenMPI 5.0
- PMIx
- srun
- mpirun
- PMI-2
- Batch-Skript
- GPU Allocation
- Error Code 255

## Problem Description
The user encountered an issue where MPI processes believed they were Rank 0 in a world consisting of one rank when running a batch script with `srun`. The problem was reproducible with an MPI-Hello-World program.

## Root Cause
OpenMPI 5.0.0 and later versions only support PMIx, while the SLURM installation on the system supports only PMI-2. This incompatibility caused the `srun` command to fail.

## Error Log
```
No PMIx server was reachable, but a PMI1/2 was detected.
If srun is being used to launch application, 2 singletons will be started.
srun: error: a0905: task 0: Exited with exit code 255
srun: Terminating StepId=1637523.0
slurmstepd: error: *** STEP 1637523.0 ON a0905 CANCELLED AT 2024-05-14T14:35:06 ***
srun: error: a0905: task 1: Exited with exit code 255
```

## Solution
The user was advised to start the application directly with `mpirun` instead of `srun`. A central installation of OpenMPI 5.0 will be delayed due to these dependencies.

## Additional Information
- The user built OpenMPI 5.0 and PMIx 5.0.1 with Spack and tested partitioned communication.
- The issue was reproducible with a simple MPI-Hello-World program.
- The user requested OpenMPI 5.0 to be available as a module.

## Conclusion
The incompatibility between OpenMPI 5.0's requirement for PMIx and the SLURM installation's support for PMI-2 caused the issue. Using `mpirun` instead of `srun` resolved the problem.
---

### 2019081542000657_Compiler%20Error%20-%20Hilfe%20Emmy.md
# Ticket 2019081542000657

 # HPC Support Ticket: Compiler Error - Hilfe Emmy

## Keywords
- Compiler Error
- qsub
- libboost_thread-ms.so.1.53.0
- LD_LIBRARY_PATH
- Module Loading
- libmkl_intel_lp64.so

## Summary
- **User Issue**: The user compiled a program using `cmake` and `make` on the frontend (Emmy). The program runs without issues on the frontend but encounters errors when submitted via `qsub`.
- **Initial Error**: The program could not find `libboost_thread-ms.so.1.53.0`.
- **Attempted Solution**: The user tried setting `LD_LIBRARY_PATH` to `/apps/boost/1.70.0-intel19.0/lib` in the job script, but it did not resolve the issue.
- **Subsequent Error**: After removing `LD_LIBRARY_PATH` and loading modules, the program could not find `libmkl_intel_lp64.so`.

## Root Cause
- The root cause of the problem is the missing library paths when the job is submitted via `qsub`. The libraries required by the program are not being correctly loaded or found in the job environment.

## Solution
- **Module Loading**: Ensure that all necessary modules are loaded in the job script. The user should load the following modules:
  1. `intelmpi/2019up04-intel`
  2. `mkl/2019up04`
  3. `intel64/19.0up04`
  4. `boost/1.70.0-intel19.0`
  5. `cmake/3.6.0`
- **Library Paths**: Verify that the library paths are correctly set in the job script. If necessary, explicitly set `LD_LIBRARY_PATH` to include the directories where the required libraries are located.

## Lessons Learned
- **Module Management**: Properly loading modules in the job script is crucial for ensuring that all required libraries are available in the job environment.
- **Library Paths**: Explicitly setting `LD_LIBRARY_PATH` can help resolve issues with missing libraries, but it should be used as a last resort after ensuring that all necessary modules are loaded.
- **Debugging**: Providing the complete output of the job (stdout+stderr) and the job script can help in diagnosing and resolving issues more effectively.

## Next Steps
- Review the job script and ensure that all necessary modules are loaded.
- Verify that the library paths are correctly set in the job script.
- If the issue persists, provide the complete output of the job and the job script for further analysis.
---

### 2015101942000732_Re%3A%20R%20module%20on%20emmy%20and%20lima%20cluster.md
# Ticket 2015101942000732

 # HPC Support Ticket: R Module on Emmy and Lima Cluster

## Keywords
- R module
- BLAS
- OpenBLAS
- MKL
- Singular Value Decomposition (SVD)
- Convergence issues
- Rcpp
- Intel Compilers
- gcc/gfortran

## Summary
- **User Request**: Installation of R module on Emmy and Lima clusters.
- **Issue**: MKL installation has convergence problems with Singular Value Decomposition (SVD).
- **Requested Solution**: R with BLAS or OpenBLAS, and same version of R on Woody, Emmy, and Lima.

## Detailed Conversation
- **Initial Request**: User requested R module installation on Emmy and Lima.
- **Admin Response**: Rudimentary R installation provided on Emmy (`module load R/3.2.2-intel15-mkl`).
- **User Feedback**: MKL installation has convergence issues with SVD. Requested R with BLAS or OpenBLAS.
- **Admin Clarification**: Asked for reasons behind BLAS preference and compatibility with Woody.
- **User Clarification**: BLAS version runs without issues on local installation. Requested R 3.2.2 (BLAS/LAPACK) on Woody, Emmy, and Lima.
- **Admin Follow-up**: Confirmed compatibility between Emmy and Lima, but Woody is different.
- **User Additional Info**: Provided compilation details (gcc/gfortran) and error logs.
- **Admin Analysis**: Identified issue with Intel Compilers for Rcpp. Suggested recompiling Rcpp with gcc/gfortran or loading Intel module.
- **Admin Plan**: To build a version compiled with Intel compilers and internal BLAS.

## Root Cause
- Convergence issues with SVD due to MKL installation.
- Incompatibility between Rcpp compiled with Intel Compilers and R compiled with gcc/gfortran.

## Solution
- Recompile Rcpp with gcc/gfortran.
- Load Intel module to resolve missing library error.
- Admin to build R version compiled with Intel compilers and internal BLAS.

## General Learnings
- Importance of consistent compiler usage for dependencies.
- Differences in floating-point operations between compilers can cause issues.
- Compatibility considerations between different clusters (Emmy, Lima, Woody).
- Detailed error logs and configuration details are crucial for troubleshooting.
---

### 2024081042000914_Amber%2024.md
# Ticket 2024081042000914

 # HPC Support Ticket: Amber 24 Installation and parmed Compatibility

## Keywords
- Amber 24
- parmed
- Python 3.12
- Compatibility
- Datacenter License
- AmberTools Patch
- Anaconda License Issue

## Summary
- User requested installation of Amber 24 on the HPC system.
- User encountered a `ModuleNotFoundError` when trying to import `parmed` with Amber 22p05-at23p06-gnu-cuda11.8.
- HPC Admin identified the issue as a compatibility problem between Python 3.12 and `parmed`.
- Amber 24 installation required a datacenter license, which was delayed.
- AmberTools patch was needed to avoid Anaconda license issues.

## Root Cause
- The installation script for Amber 22p05-at23p06-gnu-cuda11.8 automatically installed Python 3.12, which is not compatible with `parmed`.

## Solution
- Use Amber 22p03-at22p05-gnu-cuda11.8 for compatibility with `parmed`.
- Wait for the datacenter license for Amber 24.
- Apply the AmberTools patch to avoid Anaconda license issues.

## Actions Taken
- HPC Admin advised the user to use Amber 22p03-at22p05-gnu-cuda11.8 for `parmed` compatibility.
- HPC Admin initiated the process for obtaining the datacenter license for Amber 24.
- HPC Admin waited for the AmberTools patch to resolve Anaconda license issues.
- Amber 24 was eventually installed and made available on the HPC system.

## Outcome
- Amber 24 was successfully installed on the HPC system with the required patches and licenses.
- User was advised to test the new installation thoroughly.

## Notes
- The datacenter license for Amber 24 was delayed but eventually obtained.
- The AmberTools patch was released to avoid Anaconda license issues.
- The new installation of Amber 24 is available as `amber/24p02-at24p05-gnu-cuda12.4`.
---

### 2023042742000544_Meggie%20modul%3A%20Muss%20CPLUS_INCLUDE_PATH%20f%C3%83%C2%BCr%20boost%20mit%20gcc_11.2.0%20h%C3%83%.md
# Ticket 2023042742000544

 # HPC Support Ticket: Manually Setting CPLUS_INCLUDE_PATH for Boost with GCC/11.2.0

## Keywords
- Boost
- GCC/11.2.0
- CPLUS_INCLUDE_PATH
- Module
- SPACK
- Include Path
- Compilation

## Problem Description
The user encountered an issue where the Boost include path was not found when compiling a C++ program that uses Boost on the HPC system. The user had to manually set the `CPLUS_INCLUDE_PATH` to include the Boost headers.

## Root Cause
The module file for Boost, generated by SPACK, does not set the `CPLUS_INCLUDE_PATH` environment variable. It only sets `CMAKE_PREFIX_PATH` and `BOOST_ROOT`.

## Solution
Manually set the `CPLUS_INCLUDE_PATH` to include the Boost headers:
```bash
module load gcc/11.2.0
module load boost
export CPLUS_INCLUDE_PATH=$CPLUS_INCLUDE_PATH:${BOOST_ROOT}/include
```

## General Learnings
- Some modules generated by SPACK may not set all necessary environment variables.
- Manually setting `CPLUS_INCLUDE_PATH` can resolve include path issues for Boost.
- The behavior of SPACK-generated modules may vary depending on the package and the decisions made by the package authors.
- It is helpful to check the module file to understand which environment variables are being set.

## Related Links
- [SPACK Boost Package Recipe](https://github.com/spack/spack/blob/develop/var/spack/repos/builtin/packages/boost/package.py)
- [SPACK Issue Tracker](https://github.com/spack/spack/issues?q=CPLUS_INCLUDE_PATH++boost+)
---

### 2021102242001115_Tinygpu%20fails%20loading%20module%20%22amber-gpu_20p08-at20p12-gnu-cuda11.2.0-ompi%22.md
# Ticket 2021102242001115

 ```markdown
# HPC Support Ticket: Tinygpu Fails Loading Module "amber-gpu/20p08-at20p12-gnu-cuda11.2.0-ompi"

## Keywords
- Module loading error
- OpenMPI dependency
- Amber package
- CUDA
- MPI
- Slurm
- TinyGPU
- Environmental variables

## Problem Description
- User encountered an error while trying to load the module `amber-gpu/20p08-at20p12-gnu-cuda11.2.0-ompi`.
- Error message: `ERROR: Unable to locate a modulefile for 'openmpi/3.1.6-gcc9.3'`.
- The issue persisted even after attempting to load other GCC modules like `openmpi/3.1.6-gcc9.3-legacy` and `openmpi/4.0.5-gcc9.3.0-cuda-legacy`.

## Root Cause
- The `amber-gpu/20p08-at20p12-gnu-cuda11.2.0-ompi` module had a dependency on `openmpi/3.1.6-gcc9.3`, which was not available.

## Solution
- HPC Admins fixed the module to depend on `openmpi/3.1.6-gcc9.3-legacy` instead of `openmpi/3.1.6-gcc9.3`.
- User was advised to check results carefully as there were no previous users of the parallel pmemd.

## Additional Notes
- Environmental variables like `$PBS_O_WORKDIR` and `$TMPDIR` work differently with Slurm jobs compared to qsub.tinygpu.
- Slurm equivalent for `$PBS_O_WORKDIR` is `$SLURM_SUBMIT_DIR`.
- `$TMPDIR` was updated to point to a job-specific directory for Slurm jobs on TinyGPU.

## References
- [Transition of RTX2080Ti and V100 nodes (tg06x, tg07x) in TinyGPU from Ubuntu 18.04 with Torque to Ubuntu 20.04 with Slurm](https://hpc.fau.de/2021/10/12/transition-of-rtx2080ti-and-v100-nodes-tg06x-tg07x-in-tinygpu-from-ubuntu-18-04-with-torque-to-ubuntu-20-04-with-slurm/)
- [Batch Processing Documentation](https://hpc.fau.de/systems-services/systems-documentation-instructions/batch-processing/)
```
---

### 2023050642000421_amber_22p03-at22p05-gnu-cuda11.8%2C%20PYTHONPATH.md
# Ticket 2023050642000421

 # HPC Support Ticket: AMBER Installation PYTHONPATH Issue

## Keywords
- AMBER
- PYTHONPATH
- ModuleNotFoundError
- parmed
- amber.sh

## Problem
- **Root Cause**: Incorrect PYTHONPATH setting in the new AMBER installation (amber/22p03-at22p05-gnu-cuda11.8).
- **Error Message**: `ModuleNotFoundError: No module named 'parmed'` when running `amber.python script.py`.

## Solution
- **Temporary Fix**: Run the command `$AMBERHOME/amber.sh` to set the correct PYTHONPATH.
- **Permanent Fix**: HPC Admins corrected the Copy&Paste error in the module file.

## Script
```python
import parmed as pmd
parm = pmd.load_file('pzm21_min_free.top', 'pzm21_min_free.crd')
parm.save('pzm21_min_free_gromacs.top', combine='all')
parm.save('pzm21_min_free_gromacs.gro')
```

## General Learning
- Ensure that the PYTHONPATH is correctly set when installing new software.
- Temporary workarounds can be provided to users while permanent fixes are implemented.
- Communication with users is key to identifying and resolving issues.
---

### 2019052242000989_LLVM_clang%20f%C3%83%C2%BCr%20die%20SX-Aurora.md
# Ticket 2019052242000989

 ```markdown
# HPC-Support Ticket: LLVM/clang für die SX-Aurora

## Keywords
- LLVM/clang
- SX-Aurora
- Compiler
- Installation
- RPMs
- Repository
- System-Upgrade

## Problem
- User tried to compile a new version of LLVM/clang on the Aurora but encountered issues.
- The compilation process failed during configuration, with `config.guess` unable to identify the system.

## Root Cause
- The user was following an outdated or incorrect README guide.
- The system libraries (musl-libc-ve) were not compatible with the required packages.

## Solution
- NEC Support suggested installing the compiler from two RPM packages available in a specific repository.
- The HPC Admin informed the user that the packages could be installed only after the system upgrade from musl-libc-ve to glibc-ve, planned for the following week.

## General Learnings
- Always check for the latest installation guides and repositories.
- System upgrades may be required to install certain packages.
- Communication with NEC Support and HPC Admins is crucial for resolving complex issues.

## Actions Taken
- The user was advised to wait for the system upgrade.
- The ticket was closed as the issue would be resolved during the system upgrade.
```
---

### 2024123042000735_Sonder-Executable%20f%C3%83%C2%BCr%20Riesen-Systeme%3F.md
# Ticket 2024123042000735

 # HPC Support Ticket: Special Executable for Large Systems

## Keywords
- Amber
- Helma
- gridhi
- mdin_ewald_dat.F90
- pmemd.cuda
- Compilation
- Special version

## Problem
- User encountered an error while running a large system with Amber on Helma.
- Error indicated that constants in the source code were too small.
- Specifically, the constant `gridhi` in the file `mdin_ewald_dat.F90` needed to be increased.

## Solution
- HPC Admin increased the `gridhi` constant to 4096.
- Compiled special versions of `pmemd.cuda` with the updated constant.
- Provided the user with access to the new binaries via the module `amber/24p03-at24p06-gnu-cuda11`.

## General Learnings
- Custom modifications to source code may be necessary for handling large systems.
- Collaboration between users and HPC Admins can lead to quick resolution of issues.
- Proper communication and documentation are essential for troubleshooting and resolving complex problems.

## Actions Taken
- HPC Admin modified the source code and compiled a new version of the software.
- User was informed about the availability of the new binaries and instructed to test them.

## Follow-up
- User will test the new binaries and provide feedback on their effectiveness.
- Further adjustments may be necessary based on the user's testing results.
---

### 2019011742001611_PGI%20Compiler.md
# Ticket 2019011742001611

 # HPC Support Ticket: PGI Compiler Issue

## Keywords
- PGI Compiler
- CUDA
- OpenACC
- libnuma
- numactl-devel
- Emmy
- TinyGPU

## Problem Description
- User requires a newer version of the PGI Compiler for their Bachelor's thesis.
- Version 16.9 is installed on Emmy, but the user needs a newer version.
- Version 18.4 is available but not functioning correctly.
- The user is porting Fortran code to GPUs using OpenACC, requiring both CUDA and PGI.

## Root Cause
- The linker cannot find `-lnuma` when using the PGI 18.4 module.
- CUDA is not installed locally on the frontend nodes, causing compilation issues.

## Solutions
- **HPC Admin**: Suggested retrying PGI 18.4.
- **HPC Admin**: Confirmed that `libnuma` is present in `/usr/lib64/` on Emmy frontends.
- **HPC Admin**: Installed `numactl-devel` on Emmy's accelerator nodes.
- **HPC Admin**: Made PGI 18.10 available on Emmy and TinyGPU.

## General Learnings
- Ensure that necessary libraries (e.g., `libnuma`) are installed on all relevant nodes.
- Verify that CUDA is available on the nodes where GPU compilation is required.
- Update compiler versions as needed to support user requirements.
- Communicate clearly with users to understand their specific needs and provide targeted solutions.
---

### 2024101742001816_ROCM6.0%20module%20on%20the%20testcluster.md
# Ticket 2024101742001816

 # HPC Support Ticket: ROCM6.0 Module Request

## Keywords
- ROCM
- Module
- AMD Node
- AI Training
- Compilation
- MI300X

## Problem
- User urgently needed ROCM6.0 as a module for AMD node `aquavan1` to compile packages for AI training.

## Root Cause
- User required a specific version of ROCM for compatibility with their framework.

## Solution
- HPC Admin informed the user that ROCM 6.2.2 was already installed.
- User confirmed that the installation worked with the newer version (ROCM 6.2.2).

## Lessons Learned
- Always check if a newer version of the required software is available and compatible.
- Communicate the benefits of using the latest version, such as improved support for hardware (e.g., MI300X).

## Actions Taken
- HPC Admin provided information about the existing ROCM version.
- User tested and confirmed compatibility with the newer version.

## Follow-up
- No further action required as the user's issue was resolved with the existing software version.
---

### 2018040542002094_Intel%20Composer%202018%20_%20Compiler%2018%20auf%20Woody%20%26%20Testcluster.md
# Ticket 2018040542002094

 # HPC-Support Ticket Conversation Summary

## Subject: Intel Composer 2018 / Compiler 18 auf Woody & Testcluster

### Keywords:
- Intel Composer 2018
- Compiler 18
- Woody
- Testcluster
- Installation
- Update 2
- Certificate expired
- ITAC
- Vtune

### Summary:
- **User Request:** Install Intel Composer 2018 / Compiler 18 on Woody & Testcluster.
- **HPC Admin Response:**
  - Update 2 needs to be downloaded from Intel.
  - Certificate has expired.
  - Installed on all clusters (but untested).
  - Includes ITAC, excludes Vtune components.

### Root Cause of the Problem:
- User requested installation of Intel Composer 2018 / Compiler 18.

### Solution:
- HPC Admin installed the software on all clusters, including ITAC, but without Vtune components.
- Noted that Update 2 needs to be downloaded from Intel and the certificate has expired.

### General Learnings:
- Ensure that the latest updates are downloaded from Intel.
- Be aware of certificate expirations.
- Installation on all clusters should be followed by testing.
- Specific components like Vtune may be excluded based on requirements.

### Additional Notes:
- The installation was performed but not yet tested.
- Contact HPC Services for further assistance.

---

This summary provides a quick reference for support employees to understand the issue and the steps taken to resolve it.
---

### 2025011642000763_Bitte%20um%20Installation%20von%20librsvg2-bin%20auf%20csnhr.md
# Ticket 2025011642000763

 ```markdown
# HPC Support Ticket: Installation of librsvg2-bin on csnhr

## Keywords
- librsvg2-bin
- librsvg2-dev
- Ubuntu package
- csnhr
- rsvg-convert
- dependency

## Summary
A user requested the installation of the Ubuntu package `librsvg2-bin` on the csnhr system. The HPC Admin initially installed `librsvg2-dev` instead, which pulled in 50 additional dependencies. The user noticed that the required binary `rsvg-convert` was not available.

## Root Cause
- Incorrect package installation (`librsvg2-dev` instead of `librsvg2-bin`).

## Solution
- The HPC Admin corrected the installation by installing `librsvg2-bin` and removing `librsvg2-dev`.

## Lessons Learned
- Ensure the correct package is installed as requested by the user.
- Verify the installation by checking the presence of required binaries.
- Review logs (e.g., `/var/log/apt/history.log`) to confirm the correct package installation.
```
---

### 2016050242002047_ELPA%20Library%20update.md
# Ticket 2016050242002047

 # HPC-Support Ticket Conversation: ELPA Library Update

## Keywords
- ELPA Library
- Compilation Issues
- Bugfix
- Intel Compiler
- MKL Issues
- OpenMPI
- Module Paths

## Summary
The user requested the installation of specific versions of the ELPA library on the HPC clusters. The conversation highlights issues related to compilation, module paths, and dependencies on specific Intel compiler versions and MKL libraries.

## Issues and Solutions

### Issue 1: ELPA Library Version Request
- **Request**: Install ELPA 2015-11 and monitor for the upcoming 2016-06 release.
- **Solution**: ELPA 2015.11.001-intel13.1-mt was made available on all HPC systems.

### Issue 2: Compilation Bug in ELPA 2016.05
- **Problem**: A bug prevented compilation on LiMa, Woody, and Tiny* systems.
- **Solution**: Developers were working on a bugfix for Non-AVX systems. ELPA 2016.05.003-intel16.0-mt was eventually made available on Emmy and LiMa.

### Issue 3: Module Path Issue
- **Problem**: The ELPA module was loading an incorrect Intel compiler version.
- **Solution**: The ELPA module was corrected to load the appropriate Intel compiler version (16.0up3).

### Issue 4: Missing Private Module
- **Problem**: A private module (precision.mod) was not found during compilation.
- **Solution**: The precision.mod file was copied to the appropriate directory.

### Issue 5: MKL and OpenMPI Issues
- **Problem**: MKL 11.3up03 had defective p?gemm functions, and OpenMPI had issues with MKL 11.3up02 and 03.
- **Solution**: The user requested the installation of Intel 16.0up01. The admin suggested using the testing version of Intel 16.0 or 16.0up1 already available.

## General Learnings
- **Communication**: Regular updates on the status of bugfixes and installations are crucial for user satisfaction.
- **Dependency Management**: Ensuring that all dependencies (like specific compiler versions) are correctly set up is essential for smooth operation.
- **Module Paths**: Correct module paths and include directories are critical for successful compilation.
- **User Workarounds**: Users may provide temporary workarounds that can be helpful but should be validated by the support team.

## Conclusion
The ticket highlights the importance of clear communication, proper dependency management, and timely bugfixes in maintaining a functional HPC environment. The support team's responsiveness and the user's proactive approach to troubleshooting were key to resolving the issues.
---

### 2021041442002418_mpi4py%20auf%20EMMY.md
# Ticket 2021041442002418

 # HPC-Support Ticket: mpi4py auf EMMY

## Problem
- User versucht, ein parallelisiertes Python-Skript auf EMMY auszuführen.
- Fehler: `libmpi.so.40: cannot open shared object file: No such file or directory`.
- User lädt `intel64` am Anfang des Skripts, aber das Problem bleibt bestehen.

## Ursache
- `mpi4py` war nicht in der geladenen Python-Installation enthalten.
- Unterschiedliche MPI-Implementierungen (`intelmpi` vs. `openmpi`) verursachten Kompatibilitätsprobleme.

## Lösung
1. Interaktiv auf Node einloggen:
   ```bash
   qsub -l nodes=1:ppn=40,walltime=01:00:00 -I
   ```
2. Module laden und Proxy setzen:
   ```bash
   module load intel64 python/3.7-anaconda
   export http_proxy=http://proxy:80
   export https_proxy=http://proxy:80
   ```
3. `mpi4py` installieren:
   ```bash
   pip install --user --no-cache-dir mpi4py
   ```

## Ergebnis
- Der User konnte das Problem selbst lösen, indem er `mpi4py` mit der Option `--no-cache-dir` installierte.
- Der Job konnte erfolgreich gestartet und ausgeführt werden.

## Keywords
- mpi4py
- libmpi.so.40
- intel64
- openmpi
- python/3.7-anaconda
- pip install
- --no-cache-dir
- EMMY
- HPC
- Parallelisierung
- Python-Skript
- Fehlerbehebung
- Kompatibilität
- MPI-Implementierung

## Allgemeines
- Stellen Sie sicher, dass alle benötigten Module geladen sind.
- Überprüfen Sie die Kompatibilität der verwendeten MPI-Implementierungen.
- Verwenden Sie die Option `--no-cache-dir` bei der Installation von `mpi4py`, um Kompatibilitätsprobleme zu vermeiden.
---

### 42015288_MpCCI%203.0.6.md
# Ticket 42015288

 # MpCCI Version Compatibility and Linking Issues on Woody

## Keywords
- MpCCI
- Version Compatibility
- GCC
- Linking Errors
- Internal Compiler Error
- Makefile

## Summary
- **User Inquiry**: Determine which MpCCI version is functional on Woody (3.0.6 or 3.0.5.2) and request manual if necessary.
- **HPC Admin Response**:
  - MpCCI 3.0.5.2 works with older GCC-3.x versions, while SuSE SLES10 uses GCC-4.x.
  - Provided a combination of modules and libraries that worked for linking a binary in July 2008.
  - Mentioned issues with MpCCI 3.0.6 due to missing SDK package.
- **User Follow-up**: Successfully compiled Fastest with MpCCI but encountered linking errors.
- **HPC Admin Solution**: Identified an error in the LIBS line of the Makefile and suggested corrections.

## Root Cause of the Problem
- Incorrect syntax in the LIBS line of the Makefile causing linking errors.

## Solution
- Correct the LIBS line in the Makefile:
  - Change `" /apps/gcc/gcc-3.4.6-x86_64/lib64/ -lg2c"` to either `"-L /apps/gcc/gcc-3.4.6-x86_64/lib64/ -lg2c"` or `"/apps/gcc/gcc-3.4.6-x86_64/lib64/libg2c.a"`.

## Additional Notes
- Ensure that the CDEFINES include `-DSOCKET`.
- If issues persist, consider using intel64-f/10.1.021 for better error messages.

## Conclusion
- Proper syntax in the Makefile is crucial for successful linking.
- Ensure compatibility between MpCCI versions and GCC versions.
- Documentation and manuals for specific versions may be limited or unavailable.
---

### 2019061942002151_PGI%20Compiler.md
# Ticket 2019061942002151

 ```markdown
# HPC-Support Ticket: PGI Compiler Issue

## Keywords
- PGI Compiler
- Version 18.10
- Version 19.4
- TinyGPU
- LLVM
- NVTX
- nvprof
- pgprof
- makellvmlocalrc
- Signal 11

## Problem Description
- The user encountered a bug in PGI Compiler version 18.10 that affected their measurements for a Bachelor's thesis.
- The user requested an upgrade to PGI Compiler version 19.4 on TinyGPU.

## Root Cause
- The bug in PGI Compiler version 18.10 was affecting the user's measurements.
- After upgrading to version 19.4, the user encountered an error related to LLVM localrc and issues with NVTX, nvprof, and pgprof.

## Solution
- HPC Admin installed PGI Compiler version 19.4 and regenerated the localrc.
- The user confirmed that the module pgi/19.4 worked after the localrc was regenerated.
- The issue with NVTX was resolved by the user.

## Lessons Learned
- Upgrading the PGI Compiler to a newer version can resolve bugs in older versions.
- Regenerating the localrc can fix issues related to LLVM in PGI Compiler.
- Issues with NVTX, nvprof, and pgprof may require user intervention to resolve.

## Actions Taken
- HPC Admin installed PGI Compiler version 19.4.
- HPC Admin regenerated the localrc to resolve LLVM-related issues.
- The user resolved the issue with NVTX.

## Conclusion
- Upgrading the PGI Compiler and regenerating the localrc resolved the user's issues.
- The user confirmed that the new module worked and that the NVTX issue was resolved.
```
---

### 2018120742000371_R%20packages%20auf%20Woody.md
# Ticket 2018120742000371

 ```markdown
# HPC Support Ticket: R Packages auf Woody

## Keywords
- R packages
- Woody
- FAdist
- lhs
- copula
- Module
- r/3.5.1-mro
- r/3.4.x-mro
- libgsl.so.19

## Problem
- User requires R packages FAdist, lhs, and copula on Woody.
- Uncertainty about installation process.

## Root Cause
- User needs specific R packages for their work on the HPC system Woody.

## Solution
- HPC Admin advised the user to use the module `r/3.5.1-mro`, which includes all three required packages.
- Noted that the `copula` package cannot be installed for `r/3.4.x-mro` due to the unavailability of the required library `libgsl.so.19`.

## General Learnings
- Always check the availability of required libraries before attempting to install packages.
- Use the appropriate module versions that include the necessary packages.
- Communicate clearly with users about the availability and compatibility of software packages.
```
---

### 2024040842003263_Could%20you%20kindly%20help%20to%20solve%20the%20problem%20in%20compile%3F.md
# Ticket 2024040842003263

 ```markdown
# HPC-Support Ticket: Compilation Issue with CISSO++ on TINYGPU System

## Problem Description
- User encountered errors while compiling CISSO++ on the TINYGPU system.
- CMake could not find `mpic` and `mpicxx`.
- User provided `CMakeError.log` and `CmakeOutput.log` for further inspection.

## Steps Taken by User
1. Loaded modules: `openmpi/4.0.5-gcc9.3.0-cuda-legacy`, `boost/1.74.0-gcc9.3`, `mkl/2020.4`, `cmake/3.23.1`, `python/3.10-anaconda`.
2. Created a Conda environment: `sissopp_env` with Python 3.9 and various packages.
3. Cloned the CISSO++ repository.
4. Ran `./build_third_party.bash` with `CXX=g++` and `CC=gcc`.
5. Created a build directory and ran `cmake`.

## Initial HPC Admin Guidance
- Suggested changing step 6 to use `$(which mpicxx)` and `$(which mpicc)`.
- Provided documentation link for `mpi4py`.

## Further Issues
- User reported that `mpicc` and `mpicxx` commands resulted in errors: `mpicc: error while loading shared libraries: libpmi2.so.0: cannot open shared object file: No such file or directory`.
- User attempted to compile on a compute node but faced issues with slow internet connectivity, preventing the download of components.

## HPC Admin Follow-Up
- Confirmed that compilation must be done on a compute node.
- Provided a modified command for step 6: `./build_third_party.bash CXX=$(which mpicxx) CC=$(which mpicc) CXXFLAGS="-O3 -march=native -pthread" -j 1`.
- Suggested deleting the `third_party` folder before rerunning step 6.

## Zoom Meeting Scheduled
- A Zoom meeting was scheduled to provide further assistance.

## Resolution
- During the Zoom meeting, it was discovered that the user had manually run the building process, leading to errors in the B2 package.
- The user deleted the `sisso` directory and rebuilt it from scratch.
- The compilation and tests ran successfully, resolving the issue.

## Key Takeaways
- Ensure that all dependencies are correctly installed and accessible.
- Compilation should be done on a compute node.
- If internet connectivity is an issue, consider pre-downloading necessary components.
- Deleting and rebuilding the directory can resolve persistent errors.

## Keywords
- CISSO++
- TINYGPU
- CMake
- OpenMPI
- Compilation
- Dependencies
- Zoom Meeting
- Troubleshooting
```
---

### 2024090742000581_Fwd%3A%20Code%20for%20scalismo%20PCs.md
# Ticket 2024090742000581

 # HPC Support Ticket: Code for Scalismo PCs

## Keywords
- Scalismo
- UnsatisfiedLinkError
- libXrandr.so.2
- libXcursor
- Woody compute nodes

## Problem
- User encountered an error while running Scalismo on the Woody node.
- Error message: `Caused by: java.lang.UnsatisfiedLinkError: /home/hpc/iwi9/iwi9102h/.scalismo/native-libs-4.0/libnewt.so: libXrandr.so.2: cannot open shared object file: No such file or directory`

## Root Cause
- Missing libraries `libXcursor` and `libXrandr` on the Woody compute nodes.

## Solution
- HPC Admins added `libXcursor` and `libXrandr` to the list of packages to be installed on the Woody compute nodes.
- User confirmed that the issue was resolved after the libraries were installed.

## General Learnings
- Ensure that all necessary libraries are installed on the compute nodes.
- Pay attention to the relevant parts of the error message to diagnose the issue quickly.
- Collaboration between the user and HPC Admins is crucial for resolving issues efficiently.
---

### 2019051642000802_Neue%20AmberTools19%20verf%C3%83%C2%BCgbar.md
# Ticket 2019051642000802

 # HPC Support Ticket Conversation Analysis

## Subject: Neue AmberTools19 verfügbar

### Keywords
- AmberTools19
- Amber18
- sander
- cpptraj
- CUDA
- pbsa
- Emmy cluster
- TinyGPU
- OpenMP
- Intel MPI
- CUDA 10.0
- Password synchronization

### General Learnings
- **Software Installation**: Users can request specific software versions and bundles to be installed on HPC systems.
- **Cluster Preference**: Users may have preferences for specific clusters based on their workload requirements.
- **Testing**: New software installations should be tested by users before being rolled out to other clusters.
- **Password Synchronization**: After changing a password, there may be a delay before the new password is recognized across all systems.

### Root Cause of Problems
- **Software Request**: User requested the installation of AmberTools19 along with Amber18.
- **Cluster Preference**: User specified Emmy as the preferred cluster for initial installation.
- **Password Issue**: User reported a colleague unable to log in after changing the password, likely due to synchronization delay.

### Solutions
- **Software Installation**: HPC Admins compiled and installed the requested software versions on the specified cluster and later on other clusters.
- **Password Synchronization**: HPC Admins informed the user about the potential delay in password synchronization and advised waiting for a few hours.

### Detailed Conversation Summary
- **Initial Request**: User requested the installation of AmberTools19 along with Amber18, mentioning specific tools like sander and cpptraj.
- **Cluster Preference**: User specified Emmy as the preferred cluster for initial installation due to frequent use of sander.MPI.
- **Installation Process**: HPC Admins compiled and installed the requested software versions on Emmy and later on other clusters.
- **Testing**: User tested the new software and confirmed its functionality.
- **Password Issue**: User reported a colleague unable to log in after changing the password. HPC Admins informed about the potential delay in password synchronization.

### Conclusion
- The conversation highlights the process of handling software installation requests and resolving password synchronization issues on HPC systems. It also emphasizes the importance of user testing and communication between users and HPC Admins.
---

### 2018080242001771_Support%20for%20installation%20of%20mpi4py%20module.md
# Ticket 2018080242001771

 # HPC Support Ticket: Installation of mpi4py Module

## Keywords
- mpi4py
- Python module
- Installation error
- Linking error
- GNU compilers
- Intel compilers
- OpenMPI

## Problem Description
The user is attempting to install the `mpi4py` Python module in their local environment but encounters an error stating "Cannot link MPI programs." The error log is attached for reference.

## Root Cause
The root cause of the problem is a mismatch between the compilers used by `easy_install`/`anaconda` (GNU compilers) and the compilers used to compile OpenMPI (Intel 16.0 compilers). This mismatch results in several Intel-specific libraries not being found during the linking process.

## Solution
No immediate solution was provided by the HPC Admin. The issue requires further investigation to resolve the compiler mismatch.

## Lessons Learned
- Ensure that the compilers used for building and linking MPI programs are compatible.
- Be aware of potential issues when using different compiler suites for different parts of the software stack.
- Documentation and support for resolving compiler mismatches should be improved.

## Next Steps
- Investigate possible workarounds or solutions for the compiler mismatch.
- Consider providing pre-built binaries or environment modules that include compatible versions of `mpi4py` and OpenMPI.
- Update documentation to include troubleshooting steps for similar issues.

## References
- HPC Services, Friedrich-Alexander-Universitaet Erlangen-Nuernberg
- Regionales RechenZentrum Erlangen (RRZE)
- [RRZE HPC Website](http://www.hpc.rrze.fau.de/)
- [RRZE 50-Year Anniversary](http://www.50-jahre.rrze.fau.de)
---

### 2019031042000175_Ruby%20auf%20memoryhog.md
# Ticket 2019031042000175

 # HPC Support Ticket: Ruby auf memoryhog

## Keywords
- Ruby
- Ruby-unicode
- Memoryhog
- Package installation

## Summary
A user requested the installation of Ruby and Ruby-unicode packages on the memoryhog system.

## Root Cause
The user needed specific software packages (Ruby and Ruby-unicode) to be installed on the memoryhog system.

## Solution
The HPC Admins installed the requested packages on memoryhog.

## Lessons Learned
- Users may require specific software packages for their work.
- HPC Admins can install requested packages upon user request.
- Communication between users and HPC Admins is essential for resolving software installation needs.

## Follow-up Actions
- Ensure that the installed packages are functioning correctly.
- Document the installation process for future reference.
- Inform users about the availability of the newly installed packages.
---

### 2024051742000989_Software%20Installation%20Morpheus%20-%20mfip100h.md
# Ticket 2024051742000989

 # HPC Support Ticket: Software Installation Morpheus

## Subject
Software Installation Morpheus - mfip100h

## User Issue
- User requires Morpheus software for doctoral research.
- Installation from source results in dependency issues, particularly with Boost library.
- Boost version conflict between GCC@12 and GCC@8.5.0.
- Missing include files such as `tiffio.h` and `stdio.h`.
- Compilation errors related to Boost library.

## Root Cause
- Incorrect Boost version being used during compilation.
- Missing include files not found in default paths.
- Conflicting versions of Boost installed via Spack and system modules.

## Steps Taken by User
1. Cloned Morpheus repository: `git clone https://gitlab.com/morpheus.lab/morpheus.git morpheus`.
2. Installed dependencies via Spack (libtiff, doxygen, boost, etc.).
3. Attempted compilation with GCC@12 and GCC@8.5.0.
4. Modified include paths manually to resolve missing files.
5. Encountered linking errors with Boost library.

## HPC Admin Responses
1. Requested detailed installation steps from the user.
2. Suggested deleting the build directory and reloading the correct Boost module.
3. Recommended using the static Linux binary from the Morpheus download page to avoid compilation issues.

## Solution
- Use the static Linux binary provided on the Morpheus download page.
- Make the binary executable with `chmod +x BINARYNAME`.
- No need to compile from source, as the binary includes all necessary libraries.

## Keywords
- Morpheus
- Boost
- GCC
- Spack
- Static binary
- Compilation errors
- Dependency issues

## General Learnings
- Always check for precompiled binaries to avoid complex compilation issues.
- Ensure correct versions of dependencies are loaded to avoid conflicts.
- Manually modifying include paths can resolve missing file errors.
- Detailed installation steps help in diagnosing issues more effectively.

## Conclusion
The user was able to run Morpheus using the static binary without needing to compile from source. This resolved the dependency and compilation issues encountered during the installation process.
---

### 2023052442001592_Compiling%20LAMMPS%20on%20TinyGPU.md
# Ticket 2023052442001592

 # Compiling LAMMPS on TinyGPU

## Keywords
- LAMMPS
- TinyGPU
- CUDA
- cmake
- Compilation
- Modules

## Problem
- User encountered issues compiling LAMMPS with CUDA on TinyGPU nodes and front end.
- cmake was not found on the nodes.
- Compilation worked on another cluster (meggie) and without CUDA on TinyGPU front end.

## Root Cause
- User was not aware that cmake is available as a module on TinyGPU.
- Incorrect modules were loaded before compilation.

## Solution
- Load the cmake module using `module load cmake`.
- Refer to the LAMMPS module file for correct dependencies: `/apps/modules/data/testing/lammps/20201029-gcc9.3.0-openmpi4.0.5-cuda11.2.2-mkl`.
- No need to copy data to local SSD of a compute node for compilation.

## General Learnings
- Always check available modules using `module avail` before compiling software.
- Ensure correct dependencies are loaded by referring to module files.
- Communicate with HPC Admins for guidance on software compilation issues.

## Related Ticket
- Ticket#2023052442001592
---

### 2023020242001531_MPI%20auf%20dem%20Testcluster.md
# Ticket 2023020242001531

 # HPC Support Ticket: MPI auf dem Testcluster

## Keywords
- MPI
- OpenMPI
- IntelMPI
- SLURM
- libpmi2.so
- srun
- Environment Variable
- SLURM_MPI_TYPE
- user-spack
- Singularity/Apptainer

## Problem
- User had issues running MPI applications on the test cluster nodes.
- OpenMPI: Error loading shared libraries (libpmi2.so.0 not found).
- IntelMPI: Application started N times instead of with N ranks when using `srun`.

## Root Cause
- Missing `libpmi2.so` library for OpenMPI.
- Incorrect usage of `srun` for IntelMPI.

## Solution
- **OpenMPI**:
  - The `libpmi2.so` and `libpmi.so` libraries are now available on the nodes under `/opt/slurm/current-u2004/lib/`.
  - Manually adjust the search path to include the above directory.

- **IntelMPI**:
  - Use `srun --mpi=pmi2` to correctly start the application with multiple ranks.
  - Alternatively, set the environment variable `SLURM_MPI_TYPE`.

## Additional Recommendations
- Consider building the required MPI version using user-spack for specific architectures.
- For CI/CX workflows, using containers (Singularity/Apptainer) might be beneficial.

## Follow-up
- HPC Admins manually built and installed `pmi2/pmi` libraries on all nodes where SLURM is available via NFS.

## Conclusion
- The issue with OpenMPI was resolved by providing the missing libraries.
- The issue with IntelMPI was addressed by providing the correct usage of `srun`.

## Documentation for Future Reference
- Ensure that the search path for shared libraries includes the directory where `libpmi2.so` and `libpmi.so` are located.
- Use `srun --mpi=pmi2` for IntelMPI to start applications with multiple ranks correctly.
- Consider using user-spack for building specific MPI versions and containers for CI/CX workflows.
---

### 2022011742003353_Download%20Maestro%202021-4.md
# Ticket 2022011742003353

 ```markdown
# HPC Support Ticket: Download Maestro 2021-4

## Keywords
- Maestro
- Installation
- Version 2021-4
- Woody
- Module
- Certificate Expired

## Problem
- User requested the installation of the latest version (2021-4) of Maestro on the HPC system "woody".

## Root Cause
- The certificate for the download link has expired.

## Solution
- HPC Admin suggested using the module "schrodinger/2021.4" to see if it functions correctly.

## General Learnings
- Always check if the requested software version is already available as a module.
- Ensure that certificates for download links are valid and up-to-date.
- Communicate with users to verify if existing modules meet their needs.
```
---

### 2024102542001533_user%3A%20iwal037h%20%7C%20intel%20mkl%20installation%20related.md
# Ticket 2024102542001533

 ```markdown
# HPC-Support Ticket Conversation Summary

## Subject: Intel MKL Installation Related

### Keywords:
- Intel MKL
- Nuitka
- GCC
- OpenMP
- HPC
- Compilation Error
- Missing Libraries

### Problem:
- User encountered a symbol lookup error related to Intel MKL libraries while compiling a Python program using Nuitka on HPC.
- The error indicated missing Intel MKL libraries, specifically `libmkl_intel_thread.so.2`.

### Root Cause:
- The error was due to missing or incorrectly linked Intel MKL libraries.
- The user's code relied on GCC, and the Intel MKL libraries were not properly configured for use with GCC.

### Solution:
- The HPC Admin suggested loading the Intel compilers before starting the application.
- The user was advised to use specific GCC-compatible MKL libraries (`-lmkl_gf_lp64` and `-lmkl_gnu_thread`) instead of Intel-specific ones.
- The HPC Admin provided a step-by-step guide to install Nuitka from source, ensuring proper module loading and environment setup.

### Steps Taken:
1. **Initial Diagnosis**:
   - The user reported the error and provided references to similar issues.
   - The HPC Admin identified the problem as related to missing or incorrectly linked MKL libraries.

2. **Suggested Fixes**:
   - The HPC Admin suggested loading the Intel compilers and using GCC-compatible MKL libraries.
   - The user was advised to install Nuitka from source with proper module loading.

3. **Resolution**:
   - The user followed the HPC Admin's instructions and successfully compiled the program.

### General Learning:
- Proper configuration of Intel MKL libraries is crucial for successful compilation on HPC systems.
- When using GCC with Intel MKL, specific GCC-compatible libraries should be used.
- Loading the Intel compilers before starting the application can help resolve linking issues.
- Installing software from source with proper module loading ensures compatibility with the HPC environment.

### References:
- [Kaldi Issue](https://github.com/kaldi-asr/kaldi/issues/4347)
- [OpenMX Forum](https://www.openmx-square.org/forum/patio.cgi?mode=view&no=2707)
```
---

### 201808219002462_ELPA.md
# Ticket 201808219002462

 # HPC Support Ticket: ELPA

## Keywords
- ELPA
- Compilation options
- SCALAPACK
- MKL
- OpenMPI
- Eigenvalue problem
- EigenExa
- PLASMA
- DFT

## Summary
The user has been building new versions of ELPA and the HPC Admin is seeking information on the compilation options used. The user has encountered issues with different versions of ELPA and is looking for alternative solutions for solving eigenvalue problems.

## Problem
- The user has been building new versions of ELPA due to frequent changes in the API and interface.
- The user is experiencing issues with the 2018.05 version of ELPA, which is not working as expected.
- The user is looking for a more efficient way to solve symmetric real eigenvalue problems for diagonal dominant matrices.

## Compilation Options
- The user has been using the following compilation options for ELPA:
  ```bash
  ./configure SCALAPACK_FCFLAGS="-lmkl_scalapack_lp64 -lmkl_blacs_intelmpi_lp64" --prefix=/home/hpc/nfcc/nfcc02/ELPA-2018.05-Intel18.02-IMPI2018 CC=mpicc FD=mpif90 FCFLAGS="-axcore-avx2 -mavx -O2 -qopenmp -mkl=parallel" CFLAGS="-std=c11 -axcore-avx2 -mavx -O2 -qopenmp" --enable-openmp
  ```
- The HPC Admin has used the following options in the past:
  ```bash
  ./configure --prefix=/apps/elpa/$1 --with-avx-optimizations=yes --enable-openmp CC="mpicc -mt_mpi -xhost" CXX="mpicxx -mt_mpi -xhost" FC="mpif90 -mt_mpi -xhost" SCALAPACK_FCFLAGS="-I$MKLROOT/include/intel64/lp64" SCALAPACK_LDFLAGS="-L$MKLROOT/lib/intel64 -lmkl_scalapack_lp64 -lmkl_intel_lp64 -lmkl_core -lmkl_intel_thread -lmkl_blacs_intelmpi_lp64 -lpthread -lm"
  ```

## Solutions and Recommendations
- The user has been advised to try the Japanese library EigenExa as an alternative to ELPA.
- The user has been advised to contact experts from TUM/DLR for further assistance with eigenvalue problems.
- The user has been advised to use the abstract new interface for calling ELPA to avoid issues with API changes.

## Additional Information
- The user has been using OpenMPI for building ELPA, which has been partially broken on the HPC system.
- The user has been advised to use the gcc compiler for building ELPA, as recommended on the ELPA homepage.
- The user has been advised to contact the ELPA developers for assistance with issues related to different versions of the software.

## Root Cause
- The root cause of the user's issues with ELPA is the frequent changes in the API and interface, as well as potential issues with the 2018.05 version of the software.

## Solution
- The user has been advised to try alternative libraries such as EigenExa and PLASMA for solving eigenvalue problems.
- The user has been advised to contact experts from TUM/DLR for further assistance with eigenvalue problems.
- The user has been advised to use the abstract new interface for calling ELPA to avoid issues with API changes.
---

### 2021033142002067_Bitte%20um%20Paketinstallation%20auf%20memoryhog.md
# Ticket 2021033142002067

 # HPC Support Ticket Analysis

## Subject: Bitte um Paketinstallation auf memoryhog

### Keywords
- Paketinstallation
- memoryhog
- aspell
- aspell-en

### Summary
- **User Request:** Installation of `aspell` and `aspell-en` packages on `memoryhog`.
- **HPC Admin Response:** Not provided in the given conversation.

### Root Cause
- User requires specific software packages (`aspell` and `aspell-en`) to be installed on the `memoryhog` system.

### Solution
- HPC Admins need to install the requested packages (`aspell` and `aspell-en`) on the `memoryhog` system.

### General Learnings
- Users may request specific software installations for their work.
- HPC Admins should follow the standard procedure for software installation requests.
- Ensure that the requested software is compatible with the system and does not conflict with existing configurations.

### Next Steps
- HPC Admins should acknowledge the request and provide an estimated timeline for the installation.
- After installation, confirm with the user that the packages are functioning as expected.

### Documentation Note
- Keep a record of software installation requests and their outcomes for future reference.
- Update the internal documentation with any new software installations and their configurations.
---

### 2020031642002703_Hilfe%20Nutzung%20von%20Emmy.md
# Ticket 2020031642002703

 ```markdown
# HPC Support Ticket: Hilfe Nutzung von Emmy

## Summary
- **User Issue**: Floating point exception (Signal 8) when running a C++ MPI simulator on Emmy.
- **Root Cause**: Bugs in Hypre and MFEM libraries.
- **Solution**: Identify and address the bugs in the libraries.

## Keywords
- Floating point exception
- Signal 8
- Hypre
- MFEM
- METIS
- Emmy
- Torque script
- OpenMPI
- GCC
- Intel64

## Lessons Learned
- **Debugging**: Use `gdb` to identify the location of exceptions.
- **Library Compatibility**: Ensure that all linked libraries (Hypre, METIS, MFEM) are compatible and correctly configured.
- **Bounds Violation**: Check for bounds violations in the code that may cause crashes in libraries.
- **Environment Differences**: Differences in operating systems and compiler versions can lead to different behaviors.

## Ticket Details
- **User**: Attempting to run a C++ MPI simulator on Emmy.
- **Error**: Floating point exception (Signal 8) during execution.
- **Environment**:
  - Modules: `openmpi/2.0.2-gcc`, `gcc/8.1.0`, `intel64`
  - Libraries: Hypre, METIS, MFEM
- **Other Systems**: Code runs on Ubuntu 18.04 and 16.04 with different GCC and OpenMPI versions.

## HPC Admin Response
- **Initial Response**: Suggested checking for bounds violations and library configurations.
- **Follow-up**: Confirmed the issue as a bug in Hypre and MFEM.
- **Recommendation**: Contact library developers and consider using an older version of Hypre.

## User Actions
- **Debugging**: Used `gdb` to locate the exception.
- **Issue Reporting**: Found related issues on GitHub for Hypre and MFEM.
- **Next Steps**: Contact library developers to address the bugs.

## Conclusion
- The issue was identified as a bug in the Hypre and MFEM libraries.
- The user will contact the library developers for a fix.
- For future issues, ensure all libraries are compatible and correctly configured.
```
---

### 2020052542000686_Problem%20running%20OpenFOAM%20simulation%20on%20emmy.md
# Ticket 2020052542000686

 # HPC Support Ticket: Problem Running OpenFOAM Simulation on Emmy

## Keywords
- OpenFOAM
- Shell Script
- Parallel Execution
- Emmy Cluster
- OpenMPI
- PBS Script
- Environment Setup

## Problem Description
- User compiled their own OpenFOAM solver on the Emmy cluster.
- User needs assistance in writing a shell script to run the solver in parallel.
- User has attempted to write their own script but requires guidance.

## Root Cause
- User is using a custom-compiled version of OpenFOAM.
- User's script may not correctly set up the environment or load the necessary modules.

## Solution
- **Environment Setup**: Ensure the environment is set up correctly by sourcing the `.bashrc` in the OpenFOAM directory.
- **Module Loading**: Do not load an OpenFOAM module if using a custom version to avoid interference. Load the OpenMPI module used during compilation.
- **PBS Script Example**:
  ```bash
  #!/bin/bash -l
  #PBS -N pitzdaily_SNGR
  #PBS -l nodes=2:ppn=40
  module load openmpi/XXX
  cd $PBS_O_WORKDIR
  myopenfoam=/home/woody/.../simpleFoam_SNGR
  mpirun -np 40 $myopenfoam -parallel
  ```
  - Replace `XXX` with the appropriate OpenMPI version.
  - Ensure the complete path to the executable is provided.

## Additional Tips
- **Process Distribution**: Check if the job distributes processes correctly across nodes using `qstat -n` and monitoring the load on each node.
- **Expert Consultation**: For further assistance, consult with experienced OpenFOAM users or support team members.

## Conclusion
- Proper environment setup and module loading are crucial for running custom-compiled OpenFOAM solvers in parallel.
- Use the provided PBS script template as a starting point and adjust as necessary.
---

### 2024011842001733_Fehler%20bei%20FP16%20Code%20auf%20SPR%20mit%20GCC_binutils.md
# Ticket 2024011842001733

 # HPC-Support Ticket: Error with FP16 Code on SPR with GCC/binutils

## Subject
Fehler bei FP16 Code auf SPR mit GCC/binutils

## Keywords
FP16, GCC, binutils, SPR, hardware support, assembler, ICX, strace

## Problem Description
The user encountered an issue while compiling code on SPR. Despite FP16 instructions being supported by the hardware, GCC could not generate FP16 code due to an outdated `as` (assembler) from binutils 2.30 (2018).

## Root Cause
The `as` assembler used by GCC is too old (binutils 2.30) and does not support the new FP16 instructions. The required support was introduced in binutils 2.38.

## Diagnostic Steps
- The user tested with GCC 12 from the modules and GCC 13 installed via spack.
- Used `strace` to trace the compilation process and observed that GCC falls back to `/usr/bin/as`, which is from binutils 2.30.

## Solution
The user requested the installation of binutils version 2.38 or newer on Fritz to resolve the issue.

## Additional Information
- ICX (Intel C++ Compiler) has its own internal `as` and compiles the code without issues.
- A test program was provided to reproduce the issue.

## Conclusion
Updating binutils to version 2.38 or newer should resolve the issue with compiling FP16 code using GCC on SPR.

## Next Steps
- HPC Admins should consider updating binutils to a version that supports FP16 instructions.
- Test the provided program with the updated binutils to ensure the issue is resolved.
---

### 2018101742002112_cannot%20find%20-lmpigi%20on%20woody.md
# Ticket 2018101742002112

 ```markdown
# HPC Support Ticket: Cannot Find -lmpigi on Woody

## Keywords
- MPI
- Compilation Error
- Module Environment
- mpicc
- libmpigi
- Intel MPI

## Problem Description
The user encountered a compilation error while trying to compile an MPI application on the Woody cluster. The error message indicated that the linker could not find the `-lmpigi` library.

## Root Cause
The root cause of the problem was a mismatch between the MPI wrapper (`mpicc`) and the libraries being used. The user had set the compiler environment variables (`export CC=mpicc ...`) before loading the new Intel module, leading to a mix of paths from different versions.

## Solution
The user was advised to ensure that all components (compiler, libraries, etc.) are consistently loaded from the same module. The user confirmed that this was the issue and resolved it by loading the module first before setting the compiler environment variables.

## Lessons Learned
- Ensure consistency in the module environment by loading all required modules before setting any environment variables.
- Avoid using absolute binary paths in build configurations to prevent conflicts with the module environment.
- The `mpicc` wrapper should automatically set all necessary libraries, so additional manual library paths should be avoided unless necessary.

## General Advice
- Always verify the currently loaded modules to ensure they are from the same version.
- If encountering similar issues, check the build configuration for any hardcoded paths that might conflict with the module environment.
```
---

### 2019012342001341_Fehler%20beim%20Kompilieren%20von%20IHFoam%20f%C3%83%C2%BCr%20openfoam-v1806%20%28via%20Spack%29.md
# Ticket 2019012342001341

 # HPC Support Ticket: Compilation Error for OpenFOAM Extension

## Keywords
- OpenFOAM v1806
- SPACK
- Compilation Error
- Read-only File System
- Output Directory

## Problem Description
The user encountered a compilation error while trying to compile an extension for OpenFOAM v1806 on the HPC system. The error message indicated that the output file could not be opened due to a read-only file system.

## Root Cause
The compilation process was attempting to write the output binary to a directory under `/apps`, which is a read-only file system.

## Solution
The HPC Admin advised the user to modify the compilation settings to write the output binary to a directory within the user's writable space, such as `$FOAM_USER_APPBIN`. The issue was likely due to the use of `$FOAM_APPBIN` in the source code, which points to a read-only directory.

## General Learning
- Users should ensure that compilation processes write output files to directories within their writable space.
- The `/apps` directory is read-only and should not be used for writing output files.
- Modifying the output directory in the compilation settings can resolve read-only file system errors.

## Ticket Details
- **Subject:** Fehler beim Kompilieren von IHFoam für openfoam-v1806 (via Spack)
- **User:** Max Hess
- **HPC Admin:** Thomas Zeiser
- **Date:** 23.01.2019

## Related Links
- [OpenFOAM Documentation](http://www.openfoam.com/documentation/)
- [SPACK Documentation](https://spack.readthedocs.io/en/latest/)
- [HPC Services at FAU](http://www.hpc.rrze.fau.de/)
---

### 2023040142000691_hwloc.md
# Ticket 2023040142000691

 # HPC Support Ticket: hwloc

## Keywords
- hwloc
- hwloc.h
- Module loading
- Intel MPI
- OpenMPI
- Module mismatch

## Problem
- User could not find `hwloc.h` file needed for their code (AREPO).
- User was loading modules: `intel/2021.4.0`, `intelmpi/2021.7.0`, `hdf5/1.10.7-intel`, `fftw/3.3.10-ompi`, `gsl/2.7`.

## Root Cause
- Missing hwloc module.
- Mismatch in modules: `fftw/3.3.10-ompi` uses OpenMPI, while other modules use Intel MPI.

## Solution
- HPC Admin added a hwloc module over the weekend.
- HPC Admin suggested using `fftw/3.3.10-intel-impi` to match other loaded modules.

## General Learnings
- Ensure all loaded modules are compatible with each other.
- Check for necessary modules and their availability on the system.
- Consult HPC Admin for module-related queries.
---

### 2020072242002659_Installation%20von%20R-Package.md
# Ticket 2020072242002659

 ```markdown
# HPC-Support Ticket: Installation von R-Package

## Keywords
- R-Package
- Installation
- Woody
- Tinyeth
- Boot Package

## Summary
A user requested the installation of the R-Package "boot" on the HPC systems Woody and Tinyeth.

## Root Cause
The user needed the "boot" R-Package for their work on the HPC systems.

## Solution
The HPC Admin team installed the "boot" R-Package on the requested systems.

## What Can Be Learned
- Users may request specific software packages for their research.
- The HPC Admin team can install requested packages upon user request.
- Ensure proper communication and follow-up to confirm the installation.
```
---

### 42317912_Mpi%20problems%20in%20emmy.md
# Ticket 42317912

 # HPC Support Ticket: MPI Problems on Emmy Cluster

## Keywords
- MPI
- Intel MPI
- GAMESS
- I_MPI_DAT_LIBRARY
- dapl fabric error
- Emmy cluster

## Problem Description
- User encountered an MPI startup error when running GAMESS on the Emmy cluster.
- Error message: `MPI startup(): dapl fabric is not available and fallback fabric is not enabled`.

## Root Cause
- The user explicitly set the `I_MPI_DAT_LIBRARY` environment variable to a non-existing dynamic library.

## Solution
- The HPC Admin suggested that there is no need to set `I_MPI_DAT_LIBRARY` explicitly.
- The user disabled the `I_MPI_DAT_LIBRARY` environment variable, which resolved the error.

## General Learnings
- Intel MPI does not require a node file; this information is automatically passed from the batch system.
- Setting `I_MPI_DAT_LIBRARY` is usually not necessary and can lead to errors if not configured correctly.
- Always check environment variables when troubleshooting MPI issues.

## Ticket Resolution
- The user confirmed that disabling the `I_MPI_DAT_LIBRARY` environment variable resolved the issue.
- The ticket was closed with the user's confirmation that the problem was solved.
---

### 2019031242002277_Kompilier%20Probleme%20auf%20Emmy.md
# Ticket 2019031242002277

 ```markdown
# HPC-Support Ticket: Kompilier Probleme auf Emmy

## Keywords
- Kompilierprobleme
- ld: cannot find -ltbbmalloc
- Module: intelmpi, mkl, intel64
- Build-Option: -L$TPP_LIBDIR
- tbb Modul

## Problem
Der Benutzer erhält beim Kompilieren des Programms die Fehlermeldung `ld: cannot find -ltbbmalloc`. Die geladenen Module waren:
1. intelmpi/2017up04-intel
2. mkl/2017up05
3. intel64/17.0up05

Der vorgeschlagene Lösungsansatz, die Build-Option `-L$TPP_LIBDIR` zu verwenden, hat das Problem nicht behoben.

## Lösung
Der HPC Admin schlug vor, das tbb Modul separat zu laden:
```bash
module load tbb/2017up05
```

## Was zu lernen ist
- Bei Kompilierproblemen mit fehlenden Bibliotheken (z.B. `ld: cannot find -ltbbmalloc`) sollte überprüft werden, ob das entsprechende Modul geladen ist.
- Die Build-Option `-L$TPP_LIBDIR` kann in einigen Fällen nicht ausreichend sein, um das Problem zu beheben.
- Das separate Laden des tbb Moduls kann das Problem lösen.
```
---

### 42223790_OpenMPI%20module%20deprecated.md
# Ticket 42223790

 # HPC Support Ticket: OpenMPI Module Deprecated

## Keywords
- OpenMPI
- ORCA
- Module Conflict
- Deprecated Module
- Software Update

## Problem
- **Root Cause:** The user encountered warnings and conflicts while running ORCA due to the deprecated `openmpi/1.4-intel64` module and conflicts with other MPI modules.
- **Symptoms:**
  - Warning about deprecated `openmpi/1.4-intel64` module.
  - Conflicts with `intelmpi/4.0.1.007-intel` and `openmpi/1.5.3-intel11.1up9`.
  - ORCA calculation terminated with "LEAVING ORCA" message.

## Solution
- **Immediate Workaround:** Continue using `openmpi/1.4-intel64` despite the warning, as it should still work.
- **Long-term Solution:** For ORCA 3.0, users are advised to install it in their own directories due to its limited user base.

## General Learnings
- Deprecated modules may still function but can cause conflicts with other modules.
- For software with a small user base, it may be preferable to have users install and manage their own installations.
- Module conflicts can often be resolved by unloading the conflicting module.

## Related Tickets/Issues
- Module conflicts
- Deprecated software/modules
- Software installation requests

## Tags
- Module Management
- Software Installation
- ORCA
- OpenMPI
- Deprecation Warning
---

### 2020102342002311_Software%20request%20-%20small%20package%20libtiff-tools%20missing%20for%20group%20gwgi.md
# Ticket 2020102342002311

 # HPC Support Ticket Analysis

## Subject
Software request - small package libtiff-tools missing for group gwgi

## Keywords
- Software request
- libtiff-tools
- tiffinfo command
- Package installation
- Group usage
- Script crash

## Root Cause
- The user's script crashed due to the absence of the `libtiff-tools` package, which contains the `tiffinfo` command.

## Solution
- The user requested the installation of the `libtiff-tools` package to resolve the issue.

## General Learnings
- Always check the availability of required software packages before running scripts.
- Small packages like `libtiff-tools` can be crucial for specific tasks and should be considered for installation upon request.
- Ensure that software requests are handled promptly to avoid disruptions in user projects.

## Next Steps
- HPC Admins should evaluate the request and proceed with the installation of the `libtiff-tools` package if feasible.
- Communicate the installation status and any further steps to the user and the group.
---

### 42124544_Libraries%20auf%20hammer.md
# Ticket 42124544

 ```markdown
# HPC Support Ticket: Libraries auf hammer

## Keywords
- Libraries
- Installation
- readline
- zlib
- hammer.rrze

## Summary
- **User Request**: Installation of libraries (readline, zlib) on hammer.rrze.
- **HPC Admin Response**: Libraries already installed the previous day.

## Root Cause
- User requested installation of specific libraries on the HPC system.

## Solution
- HPC Admin confirmed that the requested libraries were already installed.

## General Learnings
- Ensure timely communication of library installations to avoid redundant requests.
- Verify the status of library installations before submitting a request.
```
---

### 2017020442000209_Getting%20error%20while%20loading%20the%20module.md
# Ticket 2017020442000209

 # HPC Support Ticket: Error Loading OpenFOAM Module

## Keywords
- OpenFOAM
- Module Load Error
- Permission Denied
- Maintenance
- Directory Creation

## Problem Description
User encountered an error while loading the OpenFOAM module `openfoam/2.3.0-intel13.1-intelmpi4.1`. The error message indicated a permission issue when trying to create a directory in `/home/woody`.

## Root Cause
The error was due to scheduled maintenance on the `/home/woody` directory, which temporarily restricted permissions.

## Error Message
```
Module ERROR: ERROR occurred in file /apps/modules/data/applications/openfoam/2.3.0-intel13.1-intelmpi4.1:can't create directory "/home/woody": permission denied
while executing
"file mkdir $WM_PROJECT_USER_DIR"
```

## Solution
The maintenance of `/home/woody` was completed, resolving the permission issue. The user was advised to retry loading the module after the maintenance period.

## General Learning
- **Maintenance Impact**: Scheduled maintenance can cause temporary permission issues.
- **Module Loading**: Ensure that the required directories have the appropriate permissions.
- **User Communication**: Inform users about scheduled maintenance and its potential impact on their work.

## Actions Taken
- HPC Admins confirmed that the maintenance was completed.
- User was advised to retry loading the module.

## Follow-Up
No further action was required as the issue was resolved with the completion of maintenance.

---

This documentation can be used to troubleshoot similar issues in the future.
---

### 2019112042001318_Zu%20installierende%20R-Packages%20auf%20HPC.md
# Ticket 2019112042001318

 # HPC Support Ticket: Zu installierende R-Packages auf HPC

## Keywords
- R Packages
- Installation
- R Version
- HPC Clusters (Woody, TinyEth)
- Package Compatibility

## Summary
A user requested the installation of specific R packages (`pracma`, `rasterVis`) on HPC clusters (Woody and TinyEth). The user was using R version 3.4.3-mro and needed to know if the packages were available in R version 3.5.1-mro.

## Root Cause
- User required specific R packages for processing on HPC clusters.
- User was using an older version of R and needed to ensure compatibility with the newer version.

## Solution
- HPC Admins installed the requested packages (`pracma`, `rasterVis`) for R version 3.5.1-mro.
- Confirmed that all previously used packages (`raster`, `foreign`, `rgdal`, `spatial.tools`, `doParallel`, `snow`, `vegan`, `Hmisc`, `zoo`, `geosphere`, `XML`, `rgeos`) were also available in R version 3.5.1-mro.
- Advised the user to switch to the newer R version for future processing.

## Lessons Learned
- Ensure that requested packages are installed for the latest R versions.
- Maintain compatibility of packages across different R versions.
- Communicate clearly with users about the availability of packages and the need to update R versions.

## Follow-up Actions
- Include the requested packages in future R updates.
- Monitor and update the package list regularly to ensure compatibility and availability.

## References
- HPC Services, Friedrich-Alexander-Universitaet Erlangen-Nuernberg
- Regionales RechenZentrum Erlangen (RRZE)
- [HPC Support Email](mailto:support-hpc@fau.de)
- [HPC Website](http://www.hpc.rrze.fau.de/)
---

### 2023021642000694_Jobs%20on%20Fritz%20%28b148dc10%2C%20b148dc11%29.md
# Ticket 2023021642000694

 Sure, here is the summary of the HPC support ticket conversation:

### Summary of HPC Support Ticket Conversation

**Issue:**
- User encountered performance issues with their code on Fritz.
- Initial attempts to compile `dealii` with `spack` were unsuccessful.
- User tried `MUST` for profiling but faced issues with stack traces and file names/line numbers.

**Actions Taken:**
- HPC Admin provided guidance on compiling `dealii` with `spack` and using `MUST`.
- HPC Admin suggested switching to `ITAC` for detailed profiling, but it was not compatible with `OpenMPI`.
- HPC Admin provided a modified guide for `MUST` and assisted with interpreting the output.
- HPC Admin suggested using `VAMPIR` for detailed profiling if `MUST` was not sufficient.

**Outcome:**
- User successfully compiled `dealii` with `spack` using the provided instructions.
- User generated `MUST` data and shared it with HPC Admin for analysis.
- HPC Admin analyzed the `MUST` output and provided insights on potential bottlenecks in the code.
- HPC Admin suggested further profiling with `VAMPIR` if needed.

**Next Steps:**
- User will continue to optimize their code based on the insights provided.
- HPC Admin will provide additional support as needed.

**Key Learnings:**
- Always ensure compatibility between profiling tools and the MPI implementation being used.
- Detailed profiling tools like `VAMPIR` can provide more granular insights into code performance.
- Regular communication and sharing of profiling data can help in diagnosing and optimizing code performance.

This summary captures the essence of the support ticket conversation, highlighting the key actions taken, the outcomes, and the next steps to be followed.
---

### 2021110342001551_Intel-Kompiler.md
# Ticket 2021110342001551

 # HPC-Support Ticket Conversation: Intel-Kompiler

## Keywords
- Intel Compiler
- C++17 Standard
- Module Availability
- MPI Compatibility
- oneAPI

## Problem
- The user requires a newer Intel compiler that fully supports the C++17 standard.
- The current `intel64` module on Emmy provides `icpc (ICC) 17.0.5 20170817`, which does not fully support C++17 (e.g., `std::make_unique` is missing).

## Solution
- The user was advised to use the `intel64/19.1up02` module on Emmy, which supports nearly all C++17 features and automatically loads the corresponding Intel MPI module.
- Alternatively, the user can use the `oneapi/2021.1.1` module on Meggie, which is a beta version and requires `mpiicpc` for compiling.

## Steps Taken
1. **Initial Response**:
   - The HPC Admin suggested using `module avail intel64` to list available compilers and provided a link to check supported C++17 features.

2. **User Follow-Up**:
   - The user identified `intel64/2021.4.0-oneapi` as a potential newer version but encountered issues with `mpicxx` not being found.

3. **Further Assistance**:
   - Another HPC Admin confirmed that `intel64/19.0up05` supports C++17 and loads the Intel MPI module automatically.
   - The HPC Admin also suggested using the `oneapi/2021.1.1` module on Meggie if oneAPI is specifically needed, noting that it is a beta version and requires `mpiicpc` for compiling.

## Conclusion
- The user was provided with two viable solutions: using `intel64/19.1up02` on Emmy or `oneapi/2021.1.1` on Meggie.
- The user confirmed that the provided solutions were helpful.

## General Learnings
- Always check the available modules using `module avail` to find the latest versions.
- Ensure compatibility with MPI when using newer compiler versions.
- Be aware of beta versions and their potential limitations.

## References
- [C++17 Features Supported by Intel C++ Compiler](https://www.intel.com/content/www/us/en/developer/articles/news/c17-features-supported-by-c-compiler.html)
- [C++20 Features Supported by Intel C++ Compiler](https://www.intel.com/content/www/us/en/developer/articles/technical/c20-features-supported-by-intel-cpp-compiler.html)
---

### 2023101042001125_Probleme%20mit%20SYCL%20Installation%20und%20AMD%20GPUs%20im%20Testcluster.md
# Ticket 2023101042001125

 # HPC-Support Ticket: Probleme mit SYCL und AMD GPUs im Testcluster

## Problem
- User kann SYCL-Code mit Intel/2023.2.1 Compiler kompilieren, aber nicht ausführen, nicht einmal auf der CPU.
- `sycl-ls` gibt keine verfügbaren Devices aus, vermutlich weil das OpenCL Backend nicht geladen wird.
- Zwei Versionen der Installation von Thomas Gruber funktionieren aus unterschiedlichen Gründen nicht:
  1. Version oneapi/2023.2.0: Linker-Fehler, weil Intel-Bibliotheken nicht gefunden werden.
  2. Version oneapi/2023.0.0: LLVM-Fehler, weil `/opt/rocm/amdgcn/bitcode/hip.bc` nicht geöffnet werden kann.

## Ursachen
- Pfade in `LD_LIBRARY_PATH` sind falsch gesetzt.
- Fehlende Intel-Bibliotheken (`libsvml.so`, `libirng.so`, `libimf.so`, `libintlc.so.5`).
- Unterschiedliche LLVM-Versionen und SYCL-Standards (1.2.1 vs. SYCL 2020).

## Lösungen
- HPC Admin hat die `LD_LIBRARY_PATH`-Probleme gefixt.
- Fehlende Header (`dpc_common.hpp`) wurden im Modul `dev-utilities` gefunden und automatisch mit `compiler` geladen.
- HPC Admin hat das Modul `oneapi/2023.2.0.49397` mit Anpassungen an den Modulen (`dev-utilities` mit `compiler` laden) bereitgestellt.
- User hat erfolgreich oneAPI mit den beiden GPU-Plugins installiert und getestet.

## Weitere Schritte
- HPC Admin wird die alten `sycl/*` Module und die dahinterliegenden Installationen entfernen.
- User wird die neuen Module verwenden und weiter testen.

## Zusammenfassung
- Das Problem wurde durch falsche Pfade in `LD_LIBRARY_PATH` und fehlende Bibliotheken verursacht.
- HPC Admin hat die Pfade korrigiert und fehlende Header hinzugefügt.
- User hat erfolgreich die neuen Module installiert und getestet.
- HPC Admin wird die alten Module entfernen und die neuen Module pflegen.

## Hinweise
- Bei zukünftigen Problemen mit SYCL und AMD GPUs sollten die `LD_LIBRARY_PATH`-Pfade und die Verfügbarkeit der Intel-Bibliotheken überprüft werden.
- Es wird empfohlen, die Installationsskripte von Intel für oneAPI und die GPU-Plugins zu verwenden, um Kompatibilitätsprobleme zu vermeiden.

---

Dieser Bericht dient als Dokumentation für zukünftige Support-Anfragen und zur schnellen Fehlerbehebung.
---

### 2017070542002063_Installing%20lammps%20on%20tinygpu.md
# Ticket 2017070542002063

 # HPC Support Ticket: Installing LAMMPS on tinygpu

## Keywords
- LAMMPS installation
- GCC version compatibility
- tinygpu cluster
- emmy cluster
- GCC 4.9

## Problem Description
- User is attempting to install LAMMPS on the tinygpu cluster.
- The latest version of LAMMPS does not support GCC versions later than 5.
- User successfully installed LAMMPS on the emmy cluster with GCC 4.9.
- User requests GCC 4.9 to be installed on tinygpu to facilitate LAMMPS installation.

## Root Cause
- Incompatibility between LAMMPS and GCC versions later than 5.

## Solution
- Install GCC 4.9 on the tinygpu cluster to enable LAMMPS installation.

## General Learnings
- Ensure compatibility between software and compiler versions.
- Consider installing multiple compiler versions to support various software requirements.
- Document successful installations on different clusters for future reference.
---

### 2022091942004932_R%20packages%20installation%20on%20woody-ng.md
# Ticket 2022091942004932

 ```markdown
# HPC-Support Ticket: R Packages Installation on woody-ng

## Keywords
- R packages
- woody-ng
- module r/4.2.1-conda
- module r/3.6.3-conda
- R version mismatch
- Package installation
- cleangeo package

## Summary
The user reported issues with loading specific R packages on the woody-ng cluster. The problem was traced to a version mismatch in the R module.

## Problem
- The user was unable to load several R packages (`raster`, `rgeos`, `rgdal`, `geosphere`, `doParallel`, `parallel`, `cleangeo`, `gdalUtils`, `fasterize`, `sf`) using the `r/4.2.1-conda` module.
- The user had successfully loaded these packages before the weekend, indicating a recent change.

## Root Cause
- The `r/4.2.1-conda` module was incorrectly labeled and actually activated R version 3.6.3.
- The module was renamed to `r/3.6.3-conda` to match the correct version.

## Solution
- The user was advised to switch to the `r/3.6.3-conda` module.
- A new installation of R 4.x was planned to be made available ASAP.
- The `cleangeo` package was not available in the conda channels and needed to be installed manually by the user.

## Actions Taken
- The HPC Admin renamed the module to `r/3.6.3-conda`.
- The HPC Admin performed a complete reinstallation of the `r/3.6.3-conda` module.
- The user was advised to manually install the `cleangeo` package using R mechanisms.

## Lessons Learned
- Ensure module versions are correctly labeled to avoid confusion.
- Communicate changes to module versions clearly to all affected users.
- Provide guidance on installing packages manually if they are not available in the default channels.
```
---

### 2018061842002155_%27libVT.so%27%20from%20LD_PRELOAD%20cannot%20be%20preloaded%3A%20ignored..md
# Ticket 2018061842002155

 # HPC Support Ticket: 'libVT.so' from LD_PRELOAD cannot be preloaded: ignored

## Keywords
- libVT.so
- LD_PRELOAD
- ITAC
- mpirun
- LD_LIBRARY_PATH
- Intel Trace Collector
- PBS script
- Module loading

## Problem Description
The user encountered an error when trying to use the `-trace` flag with `mpirun` in their PBS script. The error message was:
```
ERROR: ld.so: object 'libVT.so' from LD_PRELOAD cannot be preloaded: ignored.
```
The issue occurred despite the user loading the necessary modules and setting the `LD_LIBRARY_PATH`.

## Root Cause
The root cause of the problem was that the `LD_LIBRARY_PATH` did not include the correct paths for ITAC, specifically the path:
```
/apps/intel/ComposerXE2018/itac/2018.2.020/intel64/slib
```

## Solution
The user fixed the issue by adding the following line to their job script to ensure the correct environment variables were set:
```bash
source /apps/intel/ComposerXE2018/itac/2018.2.020/intel64/bin/itacvars.sh
```

## General Learnings
- Ensure that the `LD_LIBRARY_PATH` includes all necessary library paths, especially when using specific tools like ITAC.
- Verify that modules are correctly loaded and that the environment is not altered in a way that removes necessary paths.
- Use interactive runs to debug and verify environment settings.
- `libVT.so` is a part of ITAC, not VTK, and needs to be correctly preloaded.

## Steps for Future Reference
1. Check if the necessary modules are loaded.
2. Verify that the `LD_LIBRARY_PATH` includes the correct paths for ITAC.
3. Use `export | grep itac` to check if the ITAC environment variables are set correctly.
4. If the problem persists, try sourcing the ITAC environment script directly in the job script.

## Closure
The ticket was closed as the user resolved the issue and moved on to address further errors.
---

### 42176021_HPC-Account.md
# Ticket 42176021

 # HPC-Support Ticket Conversation Summary

## Keywords
- HPC Account
- OpenFOAM
- Job Script
- Compilation Error
- Field Writing Issue

## General Learnings
- **Account Setup**: New HPC accounts are created and users need to set a password.
- **Access**: Access to HPC clusters is via SSH.
- **Job Submission**: Job scripts for OpenFOAM can be submitted using `qsub`.
- **Compilation**: Compilation issues may arise due to differences in hardware and software environments.
- **Field Writing**: Issues with writing fields in OpenFOAM may require further investigation.

## Detailed Summary

### Account Setup
- **Issue**: User needs to set up a new HPC account.
- **Solution**: User is provided with an HPC ID and instructed to set a password via the IDM portal.

### Access to HPC Clusters
- **Issue**: User inquires about accessing HPC clusters.
- **Solution**: Access is via SSH. A list of clusters and their respective frontends is available on the RRZE homepage.

### Job Submission for OpenFOAM
- **Issue**: User needs guidance on submitting OpenFOAM jobs.
- **Solution**: A minimalist job script for OpenFOAM is provided, including necessary module loads and MPI commands.

### Compilation Error
- **Issue**: User encounters an "internal threshold exceeded" error during compilation.
- **Solution**: This is identified as a warning, not a fatal error. User is advised to check the Intel article for more information.

### Field Writing Issue
- **Issue**: User experiences issues with writing specific fields in OpenFOAM.
- **Solution**: No clear solution is provided. User is advised that other OpenFOAM users have not reported similar issues.

## Root Causes and Solutions
- **Compilation Error**: The "internal threshold exceeded" error is a warning related to optimization levels and can be addressed by reducing the optimization level.
- **Field Writing Issue**: The cause of the field writing issue is not identified. Further investigation is needed.

## Additional Resources
- **OpenFOAM Blog Posts**: HPC Admins suggest referring to blog posts for more information on OpenFOAM.
- **RRZE Homepage**: Contains documentation on accessing HPC clusters and job submission.

## Conclusion
This conversation highlights common issues users face when setting up and using HPC resources, including account setup, job submission, and software-specific errors. The provided solutions and resources can help support employees address similar issues in the future.
---

### 2018050342001613_libxml2%20on%20meggie.md
# Ticket 2018050342001613

 # HPC Support Ticket: libxml2 on meggie

## Keywords
- libxml2
- library
- header files
- meggie

## Problem
- User is looking for the location of the libxml2 library and header files on the meggie system.

## Solution
- Not provided in the given conversation.

## General Learnings
- Users may need guidance on locating specific libraries and header files on HPC systems.
- HPC Admins should be prepared to provide paths to commonly used libraries and tools.

## Next Steps
- HPC Admins or 2nd Level Support team should respond with the appropriate paths for libxml2 library and header files on meggie.
- If the library is not installed, provide instructions on how to install it or request its installation.
---

### 42100013_program%20request%20for%20lima.md
# Ticket 42100013

 # HPC Support Ticket: Program Request for Lima

## Keywords
- Program installation
- Dependency management
- GNU Guile
- Meep
- Node image update

## Summary
A user requested the installation of GNU Guile and Meep on the Lima cluster due to dependency issues while recompiling and moving programs from Woody to Lima.

## Root Cause
- The user needed GNU Guile and Meep for their programs, but these were not initially available on the Lima cluster.

## Conversation Highlights
- **User Request**: Installation of GNU Guile and Meep due to dependency issues.
- **HPC Admin Response**: Guile was already installed on the frontends but not on the nodes. Meep was not available in standard CentOS package sources, and third-party RPMs are not installed on the clusters.
- **Follow-up**: The user requested Guile on the nodes. The HPC Admin added Guile to the Lima node image, noting that changes would take effect after the next node reboot.

## Solution
- **GNU Guile**: Installed on the Lima node image. Changes will take effect after the next node reboot.
- **Meep**: Not installed due to unavailability in standard CentOS package sources and the policy against third-party RPMs.

## General Learnings
- **Dependency Management**: Users may require specific software and dependencies for their programs.
- **Node Image Updates**: Changes to the node image may require a node reboot to take effect.
- **Policy on Third-Party RPMs**: The HPC cluster does not install third-party RPMs, which may affect the availability of certain software.

## Next Steps
- Ensure that users are aware of the policy regarding third-party RPMs.
- Communicate the need for node reboots when updating the node image.
- Provide alternative solutions or workarounds for software not available in standard package sources.
---

### 2008021842251_neue%20Compiler%20fuer%20Cluster32.md
# Ticket 2008021842251

 # HPC-Support Ticket Conversation Analysis

## Subject: neue Compiler fuer Cluster32

### Keywords:
- Compiler modules
- Woody
- sserver02
- wnfs1
- Redundancy
- Maintenance

### Summary:
- **User Request:** The user requested to update the compiler modules from Woody.
- **HPC Admin Actions:** The HPC Admin partially completed the request by copying the 10.1 and the latest 9.x compiler modules from Woody. These modules are imported from wnfs1 instead of being installed on sserver02.
- **Considerations:** The HPC Admin raised concerns about redundancy, noting that while this setup is easy to maintain, it may not be optimal for redundancy.

### Root Cause:
- The user needed updated compiler modules from Woody.

### Solution:
- The HPC Admin copied the required compiler modules from Woody and set them up to be imported from wnfs1.

### Learnings:
- Importing modules from a central location like wnfs1 simplifies maintenance but may affect redundancy.
- It is important to consider the trade-offs between ease of maintenance and system redundancy when setting up software modules.

### Next Steps:
- Evaluate the impact on redundancy and decide whether to continue with the current setup or explore alternatives.
- Document the decision and its rationale for future reference.
---

### 2019072342000572_Some%20library.md
# Ticket 2019072342000572

 # HPC Support Ticket Conversation Analysis

## Keywords
- HPC system
- FAU
- yaml-cpp
- C++
- FEniCS
- Python
- Cluster
- Compute nodes
- Woody
- Emmy

## Summary
A user inquires about the availability of `yaml-cpp` for C++ and `FEniCS` for Python on the HPC systems at FAU. The user needs these libraries to run jobs on the compute nodes of the clusters Woody and Emmy.

## Root Cause of the Problem
The user did not specify which cluster they needed the libraries for initially, leading to a request for more information from the HPC Admin.

## Solution
The user was asked to specify the cluster (Woody and Emmy) and whether the libraries were needed on the frontends or all compute nodes. The user provided the necessary details, allowing the HPC Admin to proceed with the request.

## General Learnings
- Always specify the cluster and the scope (frontends or compute nodes) when requesting software or libraries.
- HPC systems may have multiple clusters, and requirements can vary between them.
- Clear communication is essential for efficient support.

## Next Steps
- HPC Admins should check the availability of `yaml-cpp` and `FEniCS` on Woody and Emmy clusters.
- If not available, provide instructions or assistance for the user to install the libraries themselves.
---

### 2024071042004207_Amber24%20on%20Woody.md
# Ticket 2024071042004207

 # HPC Support Ticket: Amber24 Installation on Woody

## Keywords
- Amber24
- Woody
- pmemd
- pmemd.cuda_DPFP
- Installation
- Comparability

## Problem
- User requested the installation of Amber24 on Woody to maintain comparability with previous simulations.
- Only Amber20 was installed on Woody.

## Root Cause
- Amber24 was not available on Woody, and the user needed it for simulation comparability.

## Solution
- HPC Admin initially postponed the installation due to the unavailability of Amber patches.
- Later, Amber24 was successfully installed on Woody as "amber/24p02-at24p03-ompi-gnu".

## What Can Be Learned
- Users may require specific software versions for comparability with previous work.
- Installation of new software versions may be delayed due to external factors such as patch availability.
- Communication with the user about the status of their request is crucial.

## Actions Taken
- HPC Admin acknowledged the request and provided updates on the installation status.
- Amber24 was eventually installed on Woody, fulfilling the user's request.

## Future Reference
- Ensure that the latest software versions are available for installation to meet user needs.
- Maintain open communication with users regarding the status of their requests.
---

### 42012305_32-bit%20Intel%20Compiler%20auf%2064-bit%20Ubuntu.md
# Ticket 42012305

 ```markdown
# HPC Support Ticket: 32-bit Intel Compiler auf 64-bit Ubuntu

## Keywords
- 32-bit Intel Compiler
- 64-bit Ubuntu
- Intel Fortran Compiler
- Linker Error
- Workaround
- ifort.cfg

## Problem Description
- **Root Cause**: 32-bit Intel Compiler does not work on 64-bit Ubuntu systems due to incompatible architecture of input files (`/usr/lib/crt1.o`, `/usr/lib/crti.o`, `/usr/lib/crtn.o`).
- **Error Messages**:
  ```
  ld: i386:x86-64 architecture of input file `/usr/lib/crt1.o' is incompatible with i386 output
  ld: i386:x86-64 architecture of input file `/usr/lib/crti.o' is incompatible with i386 output
  ld: i386:x86-64 architecture of input file `/usr/lib/crtn.o' is incompatible with i386 output
  ```

## Solution
- **Manual Workaround**:
  ```
  ifort x.F -L/usr/lib32 -nostartfiles /usr/lib32/crt1.o /usr/lib32/crti.o /usr/lib32/crtn.o
  ```
- **Potential Automation**: Implement the workaround in a class-specific `ifort.cfg` file via module class recognition and setting `IFORTCFG` accordingly.

## Notes
- The issue is specific to 64-bit Ubuntu systems and does not occur on 64-bit SuSE systems where `/usr/lib` is 32-bit.
- The problem might not have a straightforward fix unless it can be addressed in editable default linker scripts.

## Next Steps
- Test the manual workaround and consider implementing it in the `ifort.cfg` file if successful.
```
---

### 2024121742001296_rocm%206.3%20milan1.md
# Ticket 2024121742001296

 ```markdown
# HPC Support Ticket: ROCm 6.3 Installation on Milan1

## Keywords
- ROCm 6.3
- Milan1
- Performance Counters
- Update
- Firmware
- AMD

## Summary
- **User Request**: Install ROCm 6.3 on Milan1.
- **Issue**: Milan1 experienced hardware issues during an update, requiring a reinstallation.
- **Resolution**: ROCm 6.3 was successfully installed on Milan1 and other machines.

## Detailed Conversation
1. **Initial Request**:
   - User requested ROCm 6.3 installation on Milan1.

2. **Admin Response**:
   - Admin noted that Milan1 had hardware issues during an update, leading to a reinstallation.

3. **Update and Feedback**:
   - ROCm 6.3 was installed on Milan1.
   - User confirmed that the installation resolved performance counter issues.

4. **Further Requests**:
   - User requested ROCm 6.3 updates on Euryale, Aquavans, and Rome2.

5. **Admin Action**:
   - ROCm 6.3 was installed on Euryale, Rome2, and Aquavan2.
   - Aquavan1 remained on an older version due to firmware compatibility issues.

## Lessons Learned
- **Hardware Issues**: Be aware of potential hardware issues during updates.
- **Firmware Compatibility**: Ensure firmware compatibility before updating software.
- **User Feedback**: Important for verifying successful updates and resolving issues.

## Solution
- **Installation**: Successfully installed ROCm 6.3 on Milan1, Euryale, Rome2, and Aquavan2.
- **Firmware**: Aquavan1 remained on an older version due to firmware compatibility issues.
```
---

### 2024080242001367_Required%20assistance%20in%20the%20installation%20of%20software-%20Exciting%20software.md
# Ticket 2024080242001367

 # HPC Support Ticket: Installation of Exciting Software

## Keywords
- Exciting software installation
- GCC version
- MPI installation
- LAPACK, BLAS libraries
- Module system
- Intel compilers

## Problem Description
- User attempted to install 'Exciting software' following the instructions from a provided link.
- User encountered errors during the installation process:
  - 'Command not found: mpif90' when trying to install the parallel version.
  - 'Command not found: llapack, lblas' when trying to install the serial version.

## Root Cause
- Missing MPI compiler (mpif90) for parallel computing.
- Missing LAPACK and BLAS libraries for serial computing.

## Solution
- Use the module system to load necessary modules:
  - For MPI: Load `openmpi` or `intelmpi` modules.
  - For LAPACK and BLAS: Load `mkl` module or similar (`openBLAS`, `AMD AOCL`).
- Recommended modules for better performance:
  ```sh
  module load intel intelmpi mkl
  ```

## General Learning
- The HPC environment uses a module system to manage software installations.
- Different MPI and LAPACK/BLAS modules are available for various needs.
- Intel compilers are recommended for better performance.

## Additional Resources
- [Module System Documentation](https://doc.nhr.fau.de/environment/modules/)
- [Exciting Software Installation Guide](http://exciting.wikidot.com/neon-download-and-compile-exciting)
---

### 2024101742002922_Frage%20zu%20Nutzung%20von%20Programm%20auf%20HPC.md
# Ticket 2024101742002922

 # HPC Support Ticket: Frage zu Nutzung von Programm auf HPC

## Keywords
- DDA-Simulationen
- DDSCAT
- Fortran Compiler
- OpenMP
- MPI
- Woody Cluster
- Intel Compiler
- MKL Bibliothek
- Job Script
- Module laden

## Problem
- User möchte DDA-Simulationen mit DDSCAT auf dem Cluster durchführen.
- Fragen zur Nutzung von OpenMP und MPI.
- Fehlermeldung beim Start des Programms: `./ddscat: error while loading shared libraries: libmkl_intel_lp64.so.2: cannot open shared object file: No such file or directory`.

## Lösung
1. **Erlaubnis zur Nutzung**:
   - Der User darf das Programm DDSCAT auf dem Cluster nutzen.

2. **Empfohlene Parallelisierung**:
   - OpenMP wird als einfachere Option empfohlen.

3. **Kompilierung**:
   - Module laden:
     ```bash
     module load intel/2022.1.0
     module load intelmpi/2021.7.0
     module load mkl/2022.1.0
     ```
   - Änderungen im Makefile:
     ```makefile
     FC = mpiifort
     OPENMP = -qopenmp
     LFLAGS = -traceback -qmkl=parallel
     ```
   - Befehl im Verzeichnis "src" ausführen:
     ```bash
     ln -s $MKLROOT/include/mkl_dfti.f90 mkl_dfti.f90
     ```
   - Kompilierung starten:
     ```bash
     make all
     ```

4. **Job Script**:
   - Beispiel für ein Job Script mit OpenMP und MPI:
     ```bash
     #!/bin/bash
     #SBATCH --job-name=ddscat
     #SBATCH --output=ddscat_output.txt
     #SBATCH --error=ddscat_error.txt
     #SBATCH --nodes=1
     #SBATCH --ntasks=1
     #SBATCH --cpus-per-task=4
     #SBATCH --time=01:00:00

     module load intel/2022.1.0
     module load intelmpi/2021.7.0
     module load mkl/2022.1.0

     srun ./ddscat
     ```

5. **Fehlermeldung beheben**:
   - Stellen Sie sicher, dass die Module im Job Script geladen werden, bevor `srun` ausgeführt wird.

## Allgemeine Erkenntnisse
- OpenMP ist für Anfänger einfacher zu implementieren.
- MPI bietet vollständige Parallelisierung, erfordert aber mehr Konfiguration.
- Module müssen im Job Script geladen werden, um Bibliotheken korrekt zu verlinken.
- Die HPC Admins empfehlen, mit wenigen Kernen zu beginnen und die Skalierung zu testen.

## Root Cause
- Fehlende oder falsche Module im Job Script führten zu Fehlermeldungen beim Laden von Bibliotheken.

## Lösung
- Module im Job Script laden und korrekte Pfade im Makefile setzen.
---

### 2022041942003228_installing%20Atomsk%20package%20on%20Fritz.md
# Ticket 2022041942003228

 # HPC Support Ticket: Installing Atomsk Package on Fritz

## Summary
User encountered issues installing the Atomsk package on Fritz due to missing LAPACK libraries. The user attempted to resolve the issue by modifying Makefiles to include the path to Intel MKL libraries.

## Keywords
- Atomsk installation
- LAPACK libraries
- Intel MKL
- Makefile modification
- HPC environment

## Problem
- User received error: `/usr/bin/ld: cannot find -llapack`
- Atomsk could not find the path to LAPACK libraries.

## Root Cause
- Missing LAPACK libraries in the default path.
- Incorrect or missing paths in the Makefile for LAPACK libraries.

## Solution
1. **Use Intel MKL for LAPACK:**
   - Load the `mkl` and `intel` modules.
   - Modify the Makefile to include the path to Intel MKL libraries.
   - Example Makefile modifications:
     ```makefile
     LAPACK="-L/apps/SPACK/0.17.0/opt/linux-almalinux8-icelake/gcc-8.5.0/intel-oneapi-mkl-2021.4.0-vw4vllug36zymedwgtd6gks2r2f5ilcd/mkl/2021.4.0/lib/intel64/libmkl_avx512.so.1"
     ```

2. **Compile Atomsk:**
   - Use the modified Makefile to compile Atomsk.
   - Command: `make -f Makefile.ifort atomsk`

3. **Install Atomsk Locally:**
   - Export the installation path: `export INSTPATH=$WORK/apps/atomsk`
   - Run `make install` without `sudo`.

## Additional Notes
- Ensure the target directory exists before running `make install`.
- Specify `CONFPATH` if needed to avoid installation issues in restricted directories.

## Outcome
- Successful compilation and local installation of Atomsk.
- User tested the compiled version and confirmed it worked for simple calculations.

## Recommendations
- Verify the paths to Intel MKL libraries.
- Ensure all necessary modules are loaded before compilation.
- Create the target installation directory manually if it does not exist.

## References
- [Atomsk Documentation](https://atomsk.univ-lille.fr/doc.php)
- [Intel MKL Link Line Advisor](https://www.intel.com/content/www/us/en/developer/tools/oneapi/onemkl-link-line-advisor.html)
---

### 2022022242002306_Early-Fritz%20%22Florian%20Wachter%22%20_%20iwpa79.md
# Ticket 2022022242002306

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Keywords
- OpenFoam
- Paraview
- Python3
- Infiniband
- HDR100
- Lustre
- VNC
- TurboVNC
- Remote Visualization
- Fritz Cluster
- Early-User
- Module
- Filesystem
- Documentation

## General Learnings
- **Software Versions**: The user initially requested OpenFoam V6 but agreed to test newer versions (V8, V9).
- **Filesystem Access**: The user inquired about accessing specific filesystems (`$FASTTMP`, `/lustre`) and was informed about their availability and limitations.
- **Remote Visualization**: The user was provided with detailed instructions on how to set up and use remote visualization via VNC.
- **Early-User Access**: The user was granted early access to the Fritz cluster and provided with documentation links.
- **Module Availability**: OpenFoamV8 was available as a module, and the user was the first to test it on the Fritz cluster.
- **Data Management**: The user was informed about the temporary nature of the Lustre filesystem and the potential for data loss during reconfiguration.

## Root Cause of Problems
- **Software Version Compatibility**: The user's initial request for OpenFoam V6 was deemed outdated, and newer versions were suggested.
- **Filesystem Stability**: The Lustre filesystem was not in its final configuration, leading to concerns about data stability.

## Solutions
- **Software Version Update**: The user agreed to test OpenFoam V8 and V9 instead of V6.
- **Filesystem Access**: The user was informed about the availability of the Lustre filesystem and its current limitations.
- **Remote Visualization Setup**: Detailed instructions were provided for setting up remote visualization using VNC and TurboVNC.
- **Early-User Documentation**: The user was provided with links to the continuously updated documentation for the Fritz cluster.

## Documentation for Support Employees
### OpenFoam Version Compatibility
- **Issue**: User requested an outdated version of OpenFoam (V6).
- **Solution**: Suggested testing newer versions (V8, V9) and provided access to OpenFoamV8 as a module.

### Filesystem Access and Stability
- **Issue**: User inquired about accessing specific filesystems and was concerned about data stability.
- **Solution**: Informed the user about the availability of the Lustre filesystem and its current limitations, including potential data loss during reconfiguration.

### Remote Visualization Setup
- **Issue**: User needed instructions for setting up remote visualization.
- **Solution**: Provided detailed step-by-step instructions for setting up and using remote visualization via VNC and TurboVNC.

### Early-User Access and Documentation
- **Issue**: User required early access to the Fritz cluster and documentation.
- **Solution**: Granted early access to the Fritz cluster and provided links to the continuously updated documentation.
```
---

### 2015080642002376_error%20related%20to%20shared%20library%20libimf.so.md
# Ticket 2015080642002376

 # HPC Support Ticket: Error Related to Shared Library libimf.so

## Keywords
- Shared library error
- libimf.so
- Intel compilers
- Module loading
- Ambertools

## Problem Description
The user compiled the Ambertools package on the HPC system but encountered an error when trying to run it. The error message indicated a missing shared library:
```
/home/hpc/iww8/iww812/packages/amber14/bin/teLeap: error while loading shared libraries: libimf.so: cannot open shared object file: No such file or directory
```

## Root Cause
The error occurred because the user compiled the program with an Intel compiler but did not load the same compiler module when attempting to run the program.

## Solution
To resolve the issue, the user needs to load the same compiler module used during compilation. For example:
```
module load intel64
```

## General Learning
- Ensure that the same compiler module used during compilation is loaded when running the program.
- Missing shared library errors often indicate a mismatch between the compilation and runtime environments.

## Additional Notes
- This issue is common when using Intel compilers and can be resolved by properly managing module environments.
- Always check the module environment when encountering shared library errors.
---

### 42219986_missing%20library%20from%20Lima.md
# Ticket 42219986

 # HPC Support Ticket Analysis: Missing Library from Lima

## Keywords
- Missing library
- Compilation error
- `expat.h`
- Lima frontend node
- `expat-devel` package

## Problem Description
- User encountered a compilation error due to a missing library (`expat.h`).
- The error message: `catastrophic error: cannot open source file "expat.h"`.

## Root Cause
- The `expat-devel` package was missing or not properly installed on the Lima frontend node.

## Solution
- HPC Admin reinstalled the `expat-devel` package on the Lima frontend node.

## Additional Notes
- The user requested access to another system (Emmy) due to low priority on Lima, but this was handled as a separate ticket.

## General Learnings
- Ensure all necessary development packages are installed and up-to-date on frontend nodes.
- Users should report any sudden compilation errors that may indicate missing libraries.
- Separate new issues into new tickets for better tracking and resolution.

---

This documentation can be used to resolve similar issues related to missing libraries and compilation errors on HPC systems.
---

### 2022021142001604_Amber%20auf%20Alex.md
# Ticket 2022021142001604

 # HPC-Support Ticket Conversation Analysis

## Subject: Amber auf Alex

### Keywords:
- Amber
- Module
- Permission denied
- Jobs failed
- Compute-Center-Lizenz

### Problem:
- Multiple Amber jobs failed due to missing Amber module.
- Error messages:
  - `ERROR: Unable to locate a modulefile for 'amber/20p12-at21p11-gnu-cuda11.5'`
  - `ERROR: Permission denied on '/apps/modules/data/applications/amber/20p12-at21p11-gnu-cuda11.5'`

### Root Cause:
- Issue with the Amber module after acquiring a Compute-Center-Lizenz.

### Solution:
- HPC Admins fixed the module and binary permissions.
- Users were advised to restart their jobs.

### General Learnings:
- Module availability and permissions are critical for job execution.
- Communication between users and HPC Admins is essential for resolving issues.
- Acquiring new licenses may require additional configuration steps.

### Actions Taken:
- HPC Admins investigated and resolved the module and permission issues.
- Users were informed about the resolution and advised to restart their jobs.

### Follow-up:
- Users should monitor their jobs to ensure they run successfully after the fix.
- HPC Admins should continue to monitor the system for any further issues related to the Amber module.
---

### 2022082542003111_Updated%20version%20of%20r.md
# Ticket 2022082542003111

 # HPC Support Ticket: Updated Version of R

## Keywords
- R version update
- MRO distribution
- Woody cluster
- Woody-NG cluster
- R modules
- Conda
- qvalue package

## Problem
- User unable to install a newer version of R on the Woody cluster.
- Current R version is 4.0.2 using MRO distribution.
- User requires R version 4.2 for the `qvalue` package.

## Solution
1. **Switch to Woody-NG Cluster**:
   - User was advised to switch to the Woody-NG cluster, which supports newer software versions.
   - Documentation for switching to Woody-NG: [Transition to Woody-NG](https://hpc.fau.de/2022/07/17/transition-from-woody-with-ubuntu-18-04-and-torque-to-woody-ng-with-almalinux8-and-slurm/)

2. **Use Specific R Module**:
   - User was instructed to use the `r/4.2.1-conda` module available on Woody-NG.
   - Documentation on the module system: [Software Environment](https://hpc.fau.de/systems-services/documentation-instructions/environment/)

3. **User Guidance**:
   - User was directed to the documentation for new users: [Getting Started](https://hpc.fau.de/systems-services/documentation-instructions/getting-started/)
   - Monthly introduction sessions for beginners: [HPC Café](https://hpc.fau.de/systems-services/support/hpc-cafe/)

## General Learning
- **Cluster Updates**: Newer software versions may be available on updated clusters (e.g., Woody-NG).
- **Module System**: Specific software versions can be accessed via modules.
- **User Documentation**: Important for users to refer to documentation for setting up and using the cluster environment.
- **Support Resources**: Regular introductory sessions and support resources are available for users.

## Root Cause
- The current R version on the Woody cluster (4.0.2) was insufficient for the user's needs.
- The user was unaware of the Woody-NG cluster and the module system for accessing specific software versions.

## Resolution
- The user was guided to switch to the Woody-NG cluster and use the `r/4.2.1-conda` module to access the required R version.
- Additional documentation and support resources were provided to help the user get started with the new cluster environment.
---

### 2025030742001098_Fwd%3A%20FAU%20HPC%20Installations.md
# Ticket 2025030742001098

 ```markdown
# HPC Support Ticket: OpenFOAM and RheoTool Installation Request

## Keywords
- OpenFOAM
- RheoTool
- Software Installation
- HPC
- FAU

## Summary
A user from the Friedrich-Alexander-Universität Erlangen-Nürnberg (FAU) inquired about the installation of OpenFOAM version 9 and the RheoTool toolbox on the HPC system.

## Root Cause
The user's project partner requested information about the availability of OpenFOAM version 9 and the RheoTool toolbox on the HPC system.

## Details
- **User Request**: Inquiry about the installation of OpenFOAM version 9 and RheoTool toolbox.
- **Forwarded Email**: The request was forwarded from a project partner to the HPC support team.
- **Installation Instructions**: The user provided a link to the RheoTool installation instructions.

## Solution
- **HPC Admin Response**: The HPC admins acknowledged the request for software installation.
- **Next Steps**: The HPC admins will check the availability of OpenFOAM version 9 and the feasibility of installing RheoTool on the HPC system.

## General Learning
- **Software Requests**: Users may request specific software versions and add-ons for their projects.
- **Collaboration**: Project partners may communicate through multiple layers of forwarding emails.
- **Installation Instructions**: Users may provide links to installation instructions for requested software.

## Action Items
- **HPC Admins**: Check the availability of OpenFOAM version 9 and the feasibility of installing RheoTool.
- **2nd Level Support**: Assist with any technical issues that may arise during the installation process.
- **Documentation**: Update the knowledge base with the outcome of the installation request for future reference.
```
---

### 2016042242000709_Problem%20in%20Amber14%20mit%20MM_PBSA.md
# Ticket 2016042242000709

 ```markdown
# HPC-Support Ticket: Problem in Amber14 mit MM/PBSA

## Problem Description
User encounters an error when running MM/PBSA with the latest AMBER version on emmy or lima:
```
AmberParmError: FLAG ATOMIC_NUMBER has 6620 elements; expected 6619
```
The user had previously resolved this issue, and the program runs without problems using the same input files locally or with the latest AMBER12 version on lima.

## Root Cause
The issue is related to the `ATOMIC_NUMBER` flag in the input files. Newer versions of AmberTools (15 and above) have a more stringent check for this flag, which causes the error.

## Solution
1. **Test Dataset**: The user provided a test dataset that initially did not work but later provided a functional dataset.
2. **AmberTools Version**: The issue persists with AmberTools versions 15 and above. AmberTools 14 and earlier versions do not have this issue.
3. **Workaround**: The user found that creating topologies with `leap` or `cpptraj` instead of `ante-PBSA` resolves the issue.

## Key Learnings
- **Version Compatibility**: Different versions of AmberTools have different behaviors and checks.
- **Input File Validation**: Ensure input files are compatible with the version of AmberTools being used.
- **Community Support**: Engaging with the Amber mailing list can provide insights into version-specific behaviors.

## Actions Taken
- **HPC Admin**: Provided guidance on testing different versions and patches.
- **User**: Tested different datasets and tools to identify the root cause and workaround.

## Status
The issue is resolved. The ticket is closed.
```
---

### 2016071842001023_Amber16%20auf%20Emmy.md
# Ticket 2016071842001023

 ```markdown
# HPC Support Ticket: Amber16 auf Emmy

## Keywords
- Amber16
- Emmy
- MM/PBSA
- Permission denied
- MMPBSA.py.MPI
- Amber14

## Problem Description
User attempted to run MM/PBSA from Amber16 on Emmy and received the following error message:
```
THIS BUILD OF AMBER16 IS NOT FULLY TESTED YET
taskset: failed to execute MMPBSA.py.MPI: Permission denied
```
Amber14 worked without issues.

## Root Cause
The installer for Amber16 had incorrect paths for some binaries, leading to permission issues.

## Solution
HPC Admin corrected the paths for the binaries. If problems persist, users should report them again.

## Details
- The fix details can be found in OTRS or the script `/apps/AMBER/install-amber16.sh`.

## General Learnings
- Ensure that software installers are correctly configured to avoid path and permission issues.
- Always test new software versions thoroughly before deployment.
- Provide clear instructions for users to report any issues encountered.
```
---

### 2016052042001719_Bitte%20um%20Installation%20von%20libraries%20auf%20LiMa.md
# Ticket 2016052042001719

 ```markdown
# HPC Support Ticket: Installation of Libraries on LiMa

## Keywords
- OpenCV
- LiMa
- Woody
- GTK+
- pkg-config
- Frontends
- Computeknoten
- Ramdisk
- Arbeitsspeicher

## Summary
A user encountered issues with OpenCV on Woody and successfully compiled it on LiMa. However, they faced errors indicating the need for additional libraries (GTK+ 2.x and pkg-config).

## Root Cause
The user's program required GTK+ 2.x and pkg-config libraries, which were not installed on the compute nodes. The error message indicated that the function `cvDestroyAllWindows` was not implemented due to missing GUI support.

## Solution
- **Frontends**: The HPC Admin installed `gtk+-devel` and `gtk2-devel` on the LiMa frontends.
- **Computeknoten**: Due to the significant memory footprint and the nature of the compute nodes running from a ramdisk, the HPC Admin decided not to install these libraries on the compute nodes.

## General Learning
- GUI libraries like GTK+ have many dependencies and can consume significant memory, making them unsuitable for compute nodes running from a ramdisk.
- It is feasible to install such libraries on frontends where memory constraints are less critical.
- Users should be aware of the differences in software availability between frontends and compute nodes.
```
---

### 2022102742004021_Antrag%20auf%20Nutzung%20von%20HPC-Ressourcen%20am%20RRZE.md
# Ticket 2022102742004021

 # HPC Support Ticket Analysis

## Keywords
- HPC Access Request
- OpenFOAM Version 10
- HPC ID Setup
- HPC Cafe
- Software Installation

## Summary
A Master's student in Computational Engineering requested access to HPC resources for CFD simulations using OpenFOAM version 10. The HPC admin provided instructions for setting up the HPC ID and recommended attending the HPC Cafe for new users. The admin also installed OpenFOAM 10 on the meggie cluster.

## Root Cause of the Problem
- User required access to HPC resources and the latest version of OpenFOAM (version 10), which was not initially available.

## Solution
- HPC admin created an HPC ID for the user and provided instructions for setting it up.
- OpenFOAM 10 was installed on the meggie cluster and made available via `module load openfoam-org/10.0`.
- User was advised to report any issues with the new software version.

## General Learnings
- New users should be directed to the HPC Cafe and online introductions for initial support.
- Software requests should be handled promptly, with clear communication about availability and potential issues.
- Documentation and resources for getting started with HPC should be highlighted to new users.

## Follow-up Actions
- Monitor user feedback on OpenFOAM 10 for any issues.
- Ensure that the HPC Cafe and online introductions are regularly scheduled and promoted to new users.

## Relevant Links
- [HPC Cafe](https://hpc.fau.de/systems-services/support/hpc-cafe/)
- [Getting Started Documentation](https://hpc.fau.de/systems-services/systems-documentation-instructions/getting-started/)
- [IdM Registration](http://www.idm.fau.de)
---

### 2022032142001843_rgdal%20auf%20tinyfat.md
# Ticket 2022032142001843

 # HPC-Support Ticket: rgdal auf Tinyfat

## Keywords
- R-package
- rgdal
- Tinyfat
- install.packages()
- Download-Server
- Repository
- MRAN
- Microsoft R Open

## Problem
- User requested the installation of the R-package `rgdal` on Tinyfat.
- Initial attempt to install the package failed due to the R installation's download server not responding.

## Root Cause
- The download server used by the R installation was not responding, which is a known issue in various forums.
- The repository was temporarily unavailable.

## Solution
- Wait for the repository to be fixed.
- Once the repository was back online, the `rgdal` package was successfully installed.

## Additional Requests
- User requested the installation of additional R packages: `sf`, `rgeos`, `cleangeo`, `gdalUtils`.

## Outcome
- All requested packages were installed successfully.

## References
- [Microsoft Answers](https://docs.microsoft.com/en-us/answers/questions/778822/unable-to-access-index-for-repository-httpsmranmic.html)
- [Microsoft Answers](https://docs.microsoft.com/en-us/answers/questions/544231/unable-to-access-mran-is-there-currently-any-probl.html)
- [TechNet Forums](https://social.technet.microsoft.com/Forums/en-US/f731d10a-252b-467d-a37c-5b0c69757d5c/unable-to-access-index-for-mran-repository?forum=ropen)
- [GitHub Issues](https://github.com/microsoft/microsoft-r-open/issues/107)
- [GitHub Issues](https://github.com/microsoft/microsoft-r-open/issues/114)

## General Learnings
- Repository issues can cause package installation failures.
- Monitoring forums and issue trackers can provide insights into ongoing issues and their resolutions.
- Patience is key when dealing with temporary repository outages.
---

### 42214671_Assistance%20please.md
# Ticket 42214671

 # HPC Support Ticket: Assistance with Memory Allocation and Module Conflict

## Keywords
- Memory allocation error
- Module conflict
- Intel MPI
- OpenMPI
- `std::bad_alloc`
- `otool_nbo` command not found

## Problem Description
- User encountered errors related to memory allocation (`std::bad_alloc`) and module conflicts.
- The error messages include warnings about bad allocation and lack of memory, as well as a module access issue.
- The Intel MPI module could not be loaded due to a conflict with the already loaded OpenMPI module.
- An additional error indicates that the `otool_nbo` command was not found.

## Root Cause
- The primary issue is a lack of memory, as indicated by the `std::bad_alloc` error.
- The module conflict between Intel MPI and OpenMPI is a secondary issue but not the root cause of the failure.

## Solution
- **Memory Allocation**:
  - Reduce the problem size to fit within the available memory.
  - Consider requesting more memory resources if possible.

- **Module Conflict**:
  - The Intel compiler module tries to load the Intel MPI module, which fails because the OpenMPI module is already loaded.
  - The `orca` module automatically loads the OpenMPI module, so there is no need to load `openmpi/1.5.3-intel11.1up9` explicitly unless there is a specific reason.

- **Command Not Found**:
  - The error `sh: otool_nbo: command not found` suggests a missing tool or incorrect path.
  - Ensure that the required tools are installed and accessible in the environment.

## Additional Notes
- If the error messages at the beginning of the output also appear in smaller, successful tests, they are likely not the primary cause of the problem.
- Always check for memory-related errors first when encountering `std::bad_alloc`.

## Next Steps
- Verify if the problem persists with a smaller problem size.
- Ensure that the necessary tools (`otool_nbo`) are available in the environment.
- If the issue persists, consult with the 2nd Level Support team for further assistance.

## References
- HPC Services, Friedrich-Alexander-Universitaet Erlangen-Nuernberg
- Regionales RechenZentrum Erlangen (RRZE)
- [HPC Support](http://www.hpc.rrze.fau.de/)
---

### 2018060542001019_OpenFoam%20am%20Cluster.md
# Ticket 2018060542001019

 # HPC Support Ticket: OpenFoam on Cluster

## Keywords
- OpenFoam
- Cluster
- Simulation
- Module
- Batch Script
- Job Script

## Summary
A user inquired about the available versions of OpenFoam on the cluster and whether a batch script exists for running OpenFoam simulations.

## Problem
- User needed to know if OpenFoam version 2.3.1 was still the only version available for simulations.
- User requested a batch script for OpenFoam 5.0.

## Solution
- **Available Versions**: HPC Admin informed the user that OpenFoam versions 4.1-trusty and 5.0-trusty are available on the cluster.
- **Batch Script**: HPC Admin provided a sample job script for running OpenFoam 5.0 simulations.

## Sample Job Script
```bash
#!/bin/bash -l
### allocate 2 nodes
#PBS -l nodes=2:ppn=40
### request 8h wallClockTime
#PBS -l walltime=08:00:00
### define a name for the job
#PBS -N some-nice-name
### jobs always start in $HOME; change to where qsub was called (and all inputs/outputs should go)
cd $PBS_O_WORKDIR
### load module
module load openfoam/5.0-trusty
### run solver (using only the 20 physical cores per node)
mpirun -npernode 20 simpleFoam -parallel
```

## Lessons Learned
- Always check for the latest available software versions on the cluster.
- Batch scripts for specific software versions may not be pre-written; users may need to create their own or request assistance from HPC support.
- Sample job scripts can be provided by HPC support to help users get started with their simulations.

## References
- HPC Services, Friedrich-Alexander-Universitaet Erlangen-Nuernberg
- Regionales RechenZentrum Erlangen (RRZE)
- [HPC Support](mailto:support-hpc@fau.de)
- [HPC RRZE](http://www.hpc.rrze.fau.de/)
---

### 2024071542003404_Issue%20in%20loading%20mpi%20lib.md
# Ticket 2024071542003404

 # HPC Support Ticket: Issue in Loading MPI Library

## Keywords
- MPI
- mpi4py
- libmpifort.so.12
- ImportError
- IntelMPI
- OpenMPI
- Module Load
- Conda Environment

## Problem Description
The user is encountering an `ImportError` when trying to use the MPI module from the `mpi4py` library. The specific error message is:
```
from mpi4py import MPI
ImportError: libmpifort.so.12: cannot open shared object file: No such file or directory.
```

## Root Cause
The `libmpifort.so` library is part of IntelMPI, but the user is loading OpenMPI in their batch script. This mismatch is causing the ImportError.

## Solution
To resolve the issue, the user can either:
1. Load the IntelMPI module to match the `mpi4py` build:
   ```bash
   module load intelmpi
   ```
2. Reinstall `mpi4py` with OpenMPI to match the loaded MPI module:
   ```bash
   conda activate env_new_online_train
   pip uninstall mpi4py
   MPICC=mpicc pip install mpi4py
   ```

## General Learnings
- Ensure that the MPI library used to build `mpi4py` matches the MPI module loaded in the batch script.
- Use `module load` to add the correct MPI module.
- Reinstalling `mpi4py` with the appropriate MPI compiler can resolve library mismatch issues.
- Always purge modules and load the necessary ones at the beginning of the batch script to avoid conflicts.
---

### 2021110242002991_About%20OpenFOAM%20v1706.md
# Ticket 2021110242002991

 # HPC Support Ticket: OpenFOAM v1706

## Keywords
- OpenFOAM v1706
- HPC Clusters (Emmy, Woddy)
- Compilation Error
- Spack
- OpenMPI Module
- Manual Compilation

## Problem
- User requires OpenFOAM v1706 for thesis work.
- OpenFOAM v1706 is not available on HPC clusters.
- Attempts to build OpenFOAM v1706 using Spack resulted in compiler errors and missing binaries.

## Discussion
- HPC Admins discussed the feasibility of installing OpenFOAM v1706.
- Older versions of OpenFOAM may not be worth the effort due to potential issues and lack of SIMD optimization.
- Suggested alternatives include using newer versions of OpenFOAM or manually compiling the required version.

## Solution
- User advised to either switch to a newer version of OpenFOAM (1806 through 1906 available on Emmy and Meggie) or compile OpenFOAM v1706 themselves.
- Recommended to compile on `$WOODYHOME` (/home/woody) and load the OpenMPI module before compilation.

## General Learnings
- Older software versions may not be straightforward to install due to compatibility issues.
- Manual compilation is an option for users needing specific software versions.
- Loading appropriate modules (e.g., OpenMPI) is crucial for successful compilation.
- HPC Admins can provide guidance on alternative solutions and best practices for software installation.
---

### 2024050242002568_Fwd%3A%20%5BAMBER%5D%20Release%20of%20Amber24%20and%20AmberTools24.md
# Ticket 2024050242002568

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Keywords
- Amber24
- AmberTools24
- License
- Non-commercial use
- Computing centers
- Site license
- FAU
- NHR
- Conda package

## Summary
- **Announcement**: Release of Amber24 and AmberTools24.
- **License**: Non-commercial use is free, but computing centers require a separate license.
- **Installation**: Instructions available on the Amber website.
- **Issues**: Conda package for AmberTools24 not yet ready.

## Root Cause of the Problem
- **License Clarification**: HPC Admin inquired about the licensing for computing centers, as it was different in Amber22.

## Solution
- **License Information**: Computing centers need a separate, likely paid, license. The site license for FAU allows use by FAU members, but NHR requires a computing center license.
- **Installation**: Amber24 is available on the HPC system for specific users.

## General Learnings
- Always check the licensing terms for new software versions, especially for computing centers.
- Ensure that the appropriate licenses are in place for different user groups and computing environments.
- Keep an eye on software updates and new features, as well as any installation issues that may arise.
```
---

### 2022011842000452_AMF%20ROME%202%20not%20accesible.md
# Ticket 2022011842000452

 ```markdown
# HPC-Support Ticket Conversation: AMF ROME 2 Access Issue

## Keywords
- AMD development
- ROME 2
- Interlagos1
- ROCm version
- CMake version
- Testcluster

## Summary
- **User Issue**: Unable to access ROME 2 for AMD development. High variations in AMD GPU clusters at RRZE. Interlagos1 has ROCm version 3.9, while ROME 2 has the latest ROCm version but an older CMake version.
- **Root Cause**: Incompatibility between required CMake versions (3.22) and available versions (3.18.4 or lower) on both systems.
- **Request**: Access to one node on ROME 2 and resolution of CMake version issue.

## HPC Admin Response
- **Action**: Ticket forwarded to the appropriate HPC team for resolution.
- **Solution**: Not explicitly stated in the conversation.

## General Learnings
- **Cluster Variations**: Awareness of variations in AMD GPU clusters and their configurations.
- **Software Versions**: Importance of matching software versions (ROCm, CMake) for development work.
- **Ticket Handling**: Proper forwarding of tickets to the relevant team for resolution.

## Next Steps
- **Follow-up**: Ensure the user is granted access to the required node on ROME 2.
- **Software Update**: Investigate and update CMake versions to meet the user's requirements (3.22).
```
---

### 2023080442003185_rocm%20versionen.md
# Ticket 2023080442003185

 ```markdown
# HPC-Support Ticket: ROCm Version Update Request

## Keywords
- ROCm
- Version Update
- euryale
- milan1
- rome2

## Summary
A user requested the installation of the latest ROCm versions on the HPC systems euryale and milan1. It was noted that rome2 already has ROCm version 5.6 installed.

## Root Cause
The user requires the latest ROCm versions for their work on euryale and milan1.

## Solution
- HPC Admins need to install the latest ROCm versions on euryale and milan1.
- Verify that rome2 already has ROCm version 5.6 installed.

## General Learning
- Regular updates of software versions are essential for maintaining compatibility and performance.
- Communication between users and HPC Admins is crucial for ensuring that the necessary software versions are available.
```
---

### 2017050542002496_Creating%20executable%20files%20by%20cmake.md
# Ticket 2017050542002496

 # HPC Support Ticket: Creating Executable Files by CMake

## Keywords
- CMake
- Git
- Modules
- Intel MPI
- mpicc
- mpicxx

## Problem
- User unable to find `cmake` and `git` on the cluster.
- User unable to locate `mpicc` and `mpicxx` after loading Intel MPI module.

## Root Cause
- User was unaware of the module system and how to load necessary modules.
- User did not know that Intel MPI module automatically provides `mpicc` and `mpicxx` in the `$PATH`.

## Solution
- **CMake and Git**: Available as modules. Use `module avail` to list available versions and `module load` to load them.
  ```bash
  module avail cmake
  module avail git
  module load cmake/3.6.0
  module load git/2.2.1
  ```
- **Intel MPI**: Loading the Intel compiler module automatically loads the Intel MPI library module, which provides `mpicc` and `mpicxx` in the `$PATH`.
  ```bash
  module load intel64
  which mpicc
  which mpicxx
  ```
- **Module System**: Description and usage can be found at [HPC Environment Modules](http://www.rrze.fau.de/dienste/arbeiten-rechnen/hpc/systeme/hpc-environment.shtml#modules).

## General Learning
- Always check for available modules using `module avail`.
- Load necessary modules using `module load`.
- Intel MPI module provides `mpicc` and `mpicxx` automatically in the `$PATH` when loaded.
- Avoid using literal paths as they may change with software updates.

## References
- [HPC Environment Modules](http://www.rrze.fau.de/dienste/arbeiten-rechnen/hpc/systeme/hpc-environment.shtml#modules)
- [HPC Services](http://www.hpc.rrze.fau.de/)
---

### 2024111942002211_OpenMPI%205.0.5%20Modul%20auf%20Woody%20und%20Meggie.md
# Ticket 2024111942002211

 # HPC Support Ticket: OpenMPI 5.0.5 Module Request

## Keywords
- OpenMPI
- Module
- Woody
- Meggie
- GCC Toolchain
- Spack

## Summary
A user requested the installation of OpenMPI 5.0.5 on Woody and Meggie, compiled with the GCC toolchain, and made available as a module.

## Root Cause
- User required a specific version of OpenMPI for their work.

## Solution
- HPC Admins planned to roll out OpenMPI with Spack-0.23.0 after testing on Helma.
- Eventually, OpenMPI 5.0.6-gcc12.1.0 was installed and made available as a module on Woody and Meggie.

## General Learnings
- New software versions are often rolled out with package managers like Spack after testing.
- Specific software versions can be requested and provided as modules.
- Communication between users and HPC Admins is crucial for fulfilling software requests.

## Follow-up Actions
- None required; the request was successfully resolved.
---

### 42162632_R%20Sprache.md
# Ticket 42162632

 ```markdown
# HPC Support Ticket: R Language Installation

## Keywords
- R Language
- Module Avail
- Installation
- HPC

## Problem
- User wants to use R language on the HPC system (woodycap).
- User is unaware if R is already installed or needs additional information for installation.

## Solution
- R is already installed on the HPC system.
- User can check the availability of R using the command `module avail R`.

## Lessons Learned
- Always check if the required software is already installed using `module avail <software_name>`.
- Communicate clearly with users about the availability of software on the HPC system.
```
---

### 2022013142000712_interlagos_rome2%3A%20rocprof.md
# Ticket 2022013142000712

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject: interlagos/rome2: rocprof

### Keywords:
- rocprofiler-dev
- interlagos
- rome2
- installation

### Summary:
A user requested the installation of the `rocprofiler-dev` package on the `interlagos` and `rome2` systems.

### Root Cause:
The user needs the `rocprofiler-dev` package for their work on the specified systems.

### Solution:
HPC Admins need to install the `rocprofiler-dev` package on `interlagos` and `rome2`.

### General Learnings:
- Users may require specific software packages for their work.
- HPC Admins should be prepared to install requested software packages on specified systems.
- Communication between users and HPC Admins is essential for ensuring all necessary tools are available.
```
---

### 42056180_Bitte%20um%20Installation%20von%20flex%20auf%20memoryhog.md
# Ticket 42056180

 # HPC Support Ticket Analysis

## Subject: Bitte um Installation von flex auf memoryhog

### Keywords
- flex installation
- module loading
- boost library
- compiler options
- $BOOST_INCDIR

### Summary
- **User Request**: Installation of flex on memoryhog or checking if it is already available as a module.
- **HPC Admin Response**: flex 2.5.34 was installed on memoryhog.
- **User Follow-up**: Issues with compiling code due to missing Boost headers despite loading the boost module.
- **HPC Admin Solution**: Ensure that the compiler includes the $BOOST_INCDIR directory.

### Root Cause of the Problem
- The user's code was not compiling due to missing Boost headers, even though the boost module was loaded.

### Solution
- Ensure that the compiler includes the $BOOST_INCDIR directory by adding `-I $BOOST_INCDIR` as a compiler option.

### General Learnings
- **Module Management**: Understanding how to load and use modules in an HPC environment.
- **Compiler Options**: Importance of setting correct compiler options to include necessary directories.
- **Boost Library**: Proper configuration and usage of the Boost library in HPC environments.

### Documentation for Support Employees
- **Installation Requests**: Quick response and installation of requested software (e.g., flex).
- **Module Usage**: Ensure users are aware of how to load and use modules correctly.
- **Compiler Configuration**: Guide users on setting the correct compiler options to include necessary directories (e.g., $BOOST_INCDIR).

### Conclusion
- The issue was resolved by ensuring the compiler included the $BOOST_INCDIR directory. This highlights the importance of proper module usage and compiler configuration in HPC environments.
---

### 42367862_ELPA%20Libary.md
# Ticket 42367862

 # HPC-Support Ticket Conversation: ELPA Library

## Keywords
- ELPA Library
- Compilation
- Intel Compiler (icc)
- GCC Compiler
- Module Configuration
- Performance Benchmarking
- OpenMP
- MPI
- MKL
- Ubuntu 14.04

## Summary
The user encountered issues compiling the ELPA library locally with the Intel compiler (icc) and requested configuration options used by the HPC team. The conversation also involved requests for the latest ELPA version and performance comparisons.

## Issues and Solutions
1. **Compilation with Intel Compiler (icc)**
   - **Issue**: User unable to compile ELPA with icc.
   - **Solution**: HPC Admin provided configuration options used for building ELPA with icc.
     ```bash
     module purge
     module add intel64/13.1up03
     export CPLUS_INCLUDE_PATH=$CPLUS_INCLUDE_PATH:/usr/include/x86_64-linux-gnu/c++/4.8
     ./configure --prefix=/apps/elpa/$1 --with-sse-assembler --with-openmp \
         CC=mpicc \
         CXX="mpicxx -mt_mpi" \
         FC="mpif90 -mt_mpi" \
         SCALAPACK_FCFLAGS="-I$MKLROOT/include" \
         SCALAPACK_LDFLAGS=" -L$MKLROOT/lib/intel64 -lmkl_scalapack_lp64 -lmkl_intel_lp64 -lmkl_core -lmkl_intel_thread -lmkl_blacs_intelmpi_lp64 -lpthread -lm"
     make
     ```

2. **Performance Benchmarking**
   - **Issue**: User reported performance differences between ELPA versions.
   - **Solution**: HPC Admin provided the latest ELPA version (2015.05.001-intel13.1-mt) and suggested using `-xhost` for better performance.

3. **Permissions Issue**
   - **Issue**: User encountered permission issues with the ELPA module.
   - **Solution**: HPC Admin corrected the permissions.

4. **Sequential MKL Version**
   - **Issue**: User requested a version of ELPA linked against the sequential MKL.
   - **Solution**: HPC Admin suggested compiling the sequential version themselves.

## General Learnings
- Configuration options for compiling ELPA with icc.
- Importance of setting correct permissions for module directories.
- Performance tuning with specific compiler flags (e.g., `-xhost`).
- Handling different versions of libraries and their performance implications.

## Conclusion
The user was satisfied with the provided solutions and the latest ELPA version performed well in benchmarks. The HPC Admin ensured that all issues were resolved, including permission problems and performance concerns.
---

### 2020040642000982_Installation%20von%20R-Packages.md
# Ticket 2020040642000982

 ```markdown
# HPC Support Ticket: Installation of R-Packages

## Summary
- **User Request:** Installation of R-packages `exactextractr` and `sf` on Woody and Tinyeth.
- **Issue:** `exactextractr` package not available for R versions 3.5.1 and 4.3.3.
- **Root Cause:** Incompatibility with older R versions and missing dependencies (`libudunits2.so.0`).
- **Solution:** Manual installation and updating dependencies.

## Keywords
- R-packages
- exactextractr
- sf
- R version compatibility
- Dependency issues
- Manual installation

## Detailed Conversation

### Initial Request
- User requested installation of `exactextractr` and `sf` packages.

### HPC Admin Response
- `sf` package installed successfully.
- `exactextractr` package not available for R versions 3.5.1 and 4.3.3.

### User Feedback
- User suggested updating R to a newer version (3.6.3) where `exactextractr` works.

### HPC Admin Actions
- Attempted manual installation of `exactextractr` in R versions 3.5.1 and 3.5.3.
- Identified missing dependency `libudunits2.so.0` and installed it.

### User Testing
- User encountered errors due to missing dependencies.
- After dependency installation, packages worked correctly.

## Lessons Learned
- **R Version Compatibility:** Newer R-packages may not be compatible with older R versions.
- **Dependency Management:** Ensure all required dependencies are installed on both login and compute nodes.
- **Manual Installation:** Sometimes manual installation is necessary for troublesome packages.

## Conclusion
- Successful installation of `exactextractr` and `sf` packages after addressing version compatibility and dependency issues.
```
---

### 2020091542003981_OpenMP%20SIMD%20instructions%20not%20recognised.md
# Ticket 2020091542003981

 ```markdown
### Key Learnings from HPC Support Ticket Conversation

**Issue:**
- User had trouble compiling Elmer/Ice due to unrecognized SIMD directives with gcc/8.1.0 and openmpi/3.1.2-gcc.
- User faced issues with missing shared libraries during runtime tests.

**Solution:**
- **Compiler and SIMD Directives:**
  - SIMD directives are tied to the compiler, not the MPI library.
  - gcc/8.1.0 does not support SIMD directives.
  - Switching to Intel compilers (ifort, icc) resolved the issue.

- **Toolchain Configuration:**
  - Successful compilation with Intel compilers:
    ```bash
    module load intel64/19.1up02
    module load hdf5
    module load netcdf
    module load cmake
    cmake .. -DPHDF5HL_LIBRARY=$HDF5_BASE/lib/libhdf5hl_fortran.so -DPHDF5_LIBRARY=$HDF5_BASE/lib/libhdf5.so -DPHDF5_INCLUDE_DIR=$HDF5_INC -DNETCDF_INCLUDE_DIR=$NETCDF_F_INCDIR -DNetCDFF_LIBRARY=$NETCDF_F_LIBDIR/libnetcdff.so -DNetCDF_LIBRARY=$NETCDF_F_LIBDIR/libnetcdf.so -DCMAKE_BUILD_TYPE=release -DCMAKE_CXX_FLAGS="-xhost" -DCMAKE_C_FLAGS="-xhost" -DCMAKE_Fortran_FLAGS="-xhost" -DCMAKE_Fortran_COMPILER=ifort -DCMAKE_C_COMPILER=icc -DCMAKE_CXX_COMPILER=icc -DMPI_Fortran_COMPILER=mpif90 -DMPI_C_COMPILER=mpicc -DWITH_OpenMP:BOOLEAN=TRUE -DWITH_MPI:BOOLEAN=TRUE -DWITH_ELMERGUI:BOOL=FALSE -DWITH_ElmerIce:BOOL=TRUE
    make -j
    make install
    ```

- **Runtime Environment:**
  - Ensure proper environment setup for runtime tests.
  - Provide a script to set up the environment and run tests.

**Conclusion:**
- Switching to Intel compilers resolved the SIMD directive issue.
- Proper toolchain configuration and environment setup are crucial for successful compilation and runtime.
- Always ensure the correct compiler flags and libraries are specified.
```
---

### 2019062542000383_Unable%20to%20run%20OpenFOAM%20simulations%20on%20Emmy.md
# Ticket 2019062542000383

 # HPC Support Ticket: Unable to Run OpenFOAM Simulations in Parallel on Emmy Cluster

## Keywords
- OpenFOAM
- Parallel Simulations
- Emmy Cluster
- Bash Script
- Module Loading
- mpirun

## Problem Description
User was unable to run OpenFOAM simulations in parallel on the Emmy Cluster. The issue seemed to be related to the bash script used for job submission.

## Root Cause
- The lines to load the OpenFOAM module and the `mpirun` command were commented out in the user's script.

## Solution
- Ensure that the necessary lines to load the OpenFOAM module and the `mpirun` command are not commented out in the bash script.

## Lessons Learned
- Always check that all necessary commands in the bash script are active and not commented out.
- Provide the exact script and job output when reporting issues to HPC support for better diagnosis.

## Support Actions
- HPC Admin provided guidance on checking the script for commented-out lines.
- User confirmed that the issue was resolved.

## Conclusion
The issue was resolved by ensuring that the necessary commands in the bash script were active. This highlights the importance of thorough script verification when troubleshooting job submission issues.
---

### 2024011142003048_Running%20scala%20job%20on%20woody.md
# Ticket 2024011142003048

 ```markdown
# Running Scala Job on Woody

## Issue Description
User encountered an error while running a Scala job on the Woody nodes. The error was related to missing X libraries, specifically `libXxf86vm.so.1`.

## Root Cause
The required X libraries were not installed on the Woody nodes. The user's job script adjusted the `LD_LIBRARY_PATH` to include X libraries that were not installed on TinyGPU.

## Solution Attempts
1. **Initial Library Installation**: HPC Admins installed the required library (`libXxf86vm.so.1`) on the Woody nodes.
2. **Additional Libraries**: User encountered further errors related to missing libraries (`libXrandr.so.2`).
3. **Library Collection**: HPC Admins collected all missing libraries in the directory `/tmp/woody-libs` on Woody4.
4. **User Instructions**: User was instructed to copy the `woody-libs` directory to their `$HOME` and extend the `LD_LIBRARY_PATH`.

## Outcome
The user was unable to locate the `woody-libs` directory and encountered path not found errors. HPC Admins suggested using snapshots to recover the lost files.

## Additional Information
- The user's job involved running a Scala script using Java and required specific X libraries.
- The user was advised to adjust the `LD_LIBRARY_PATH` to include the required libraries built for Alma Linux 8.9.
- A Zoom meeting was suggested to discuss the setup and required changes.

## Keywords
- Scala job
- Woody nodes
- X libraries
- `libXxf86vm.so.1`
- `libXrandr.so.2`
- `LD_LIBRARY_PATH`
- Alma Linux 8.9
- Snapshots
- Zoom meeting
```
---

### 2021092742001921_AMD%20Development.md
# Ticket 2021092742001921

 ```markdown
# HPC-Support Ticket: AMD Development

## Keywords
- AMD HIP programming
- ROCm development kit
- Test cluster
- AMD MI100 GPGPU
- WalBerla project

## Summary
A user inquired about AMD HIP programming support and infrastructure available at the HPC site for the WalBerla project.

## User's Questions
1. How does RRZE perform development work in AMD HIP programming?
2. What infrastructure is provided for AMD development?
3. Does RRZE have experience in AMD HIP programming, and do they provide training?

## HPC Admin Response
- **Infrastructure**: The test cluster includes a machine ("rome2") equipped with an AMD MI100 GPGPU.
- **Access**: The user's account has been enabled for the test cluster.
- **Software**: The ROCm development kit is installed locally on the machine.
- **Experience**: RRZE does not have practical experience with HIP, so the user will need to work independently.
- **Stability**: The configuration of the test cluster may change without notice.

## Root Cause of the Problem
The user needs information on AMD HIP programming support and available infrastructure.

## Solution
- The user has been granted access to the test cluster with the necessary hardware and software.
- The user will need to proceed with AMD HIP programming independently due to the lack of practical experience at RRZE.

## Additional Notes
- The test cluster configuration may change, so users should be prepared for potential adjustments.
- No training is provided for AMD HIP programming by RRZE.
```
---

### 2024060342003545_OpenMP%20Target%20Offloading%20for%20AMD%20GPUs%20and%20APUs.md
# Ticket 2024060342003545

 # HPC-Support Ticket: OpenMP Target Offloading for AMD GPUs and APUs

## Keywords
- OpenMP
- Target Offloading
- AMD GPUs
- APUs
- Compilation
- ROCm
- HIP
- HPC Admins
- 2nd Level Support

## Summary
This ticket discusses issues related to OpenMP target offloading for AMD GPUs and APUs. The user encountered problems during compilation and execution of their code.

## Root Cause
- The user's code was not compiling correctly due to issues with OpenMP target offloading for AMD GPUs and APUs.
- There were potential configuration problems with ROCm and HIP.

## Solution
- HPC Admins and 2nd Level Support team members provided guidance on configuring ROCm and HIP for OpenMP target offloading.
- The user was advised to check the compatibility of their code with the current ROCm and HIP versions.
- Specific compilation flags and environment settings were suggested to resolve the issues.

## Lessons Learned
- Ensure that the ROCm and HIP versions are compatible with the user's code.
- Use appropriate compilation flags and environment settings for OpenMP target offloading.
- Collaborate with HPC Admins and 2nd Level Support for specific configuration and troubleshooting steps.

## Next Steps
- Verify the compatibility of ROCm and HIP with the user's code.
- Apply the suggested compilation flags and environment settings.
- Test the code to ensure proper offloading to AMD GPUs and APUs.

## References
- ROCm documentation
- HIP documentation
- OpenMP target offloading guides
---

### 2018053042001385_tools%20to%20profile%20MPI%20calls%20on%20emmy.md
# Ticket 2018053042001385

 # HPC Support Ticket: Tools to Profile MPI Calls on Emmy

## Keywords
- MPI profiling
- Intel Trace Analyzer/Collector
- GCC
- OpenMPI
- Parallel debuggers
- Visualization issues
- X applications

## Summary
A user inquired about tools available to profile MPI calls and messages on the Emmy cluster. The user was interested in tools compatible with GCC and OpenMPI. The conversation also covered issues with visualizing results using Intel Trace Analyzer.

## User Inquiry
- Tools for profiling MPI calls and messages on Emmy.
- Compatibility with GCC and OpenMPI.
- Possible use of parallel debuggers for profiling.
- Links to relevant RRZE FAQ pages.

## HPC Admin Response
- Intel Trace Analyzer/Collector is available as a module on Emmy and Meggie.
- Documentation for Intel Trace Analyzer/Collector is on the Woody page.
- Support is provided only for Intel MPI.
- Intel documentation mentions compatibility checks for other MPI implementations.

## User Follow-Up
- Rebuilt software stack with Intel tools but encountered issues visualizing results.
- Connected via SSH with X forwarding but `traceanalyzer` did not open any windows or give errors.

## HPC Admin Troubleshooting
- Verified that `traceanalyzer` works on Emmy and Meggie.
- Suggested testing `traceanalyzer` without specifying a file.
- Asked if the user could open a simple X application like `xterm`.

## Root Cause
- Potential issue with X forwarding or compatibility with the user's environment.

## Solution
- Verify X forwarding by testing with a simple X application.
- Ensure compatibility with the user's environment and Intel tools.

## Additional Notes
- The user was advised to check if `traceanalyzer` opens without specifying a file.
- The conversation highlights the importance of verifying X forwarding and compatibility when using graphical tools on HPC clusters.

## References
- [Intel Trace Analyzer Documentation](https://software.intel.com/en-us/intel-trace-analyzer/documentation)
- [RRZE Woody Cluster Documentation](https://www.anleitungen.rrze.fau.de/hpc/woody-cluster/#itac)
---

### 2017102342002451_mpirun_rrze%20command%20not%20found.md
# Ticket 2017102342002451

 # HPC Support Ticket: mpirun_rrze Command Not Found

## Keywords
- mpirun_rrze
- intelmpi
- command not found
- module load
- Emmy cluster
- simulation
- error message
- mpirun-wrapper
- update

## Problem Description
The user encountered an error when trying to run a simulation on the Emmy cluster. The error message indicated that the `mpirun_rrze` command was not found, despite the input file working previously. The user also confirmed that the `mpirun_rrze` command was not recognized in the shell after loading the `intelmpi` module.

## Root Cause
The issue was caused by a recent update to the default version of `intelmpi`, which missed creating a link to the `mpirun-wrapper`.

## Solution
The HPC Admin fixed the issue by creating the missing link to the `mpirun-wrapper`. The user confirmed that the simulation ran successfully after the fix.

## Additional Notes
- The user noticed an error in the log file regarding a missing `mpdboot` file, but the simulation ran successfully despite this error.
- The HPC Admin acknowledged the additional error and assured the user that it should not appear in future runs.

## General Learnings
- Updates to software modules can sometimes miss important links or dependencies, causing commands to be unrecognized.
- It is important to test modules and their dependencies after updates to ensure everything is functioning correctly.
- Users should report any errors or issues they encounter, even if the job runs successfully, as it can help identify and fix underlying problems.
---

### 2025012442000677_Doubts%20about%20the%20FAU%20Testcluster.md
# Ticket 2025012442000677

 ```markdown
# HPC-Support Ticket: Doubts about the FAU Testcluster

## Keywords
- FAU Testcluster
- ARM nodes
- MPI library
- lukewarm
- salloc
- srun
- terminal freeze

## Problem Description
- User is experiencing difficulties launching MPI on ARM nodes.
- Unable to find the correct path for the MPI library on lukewarm.
- Terminal freezes when allocating lukewarm using `salloc` or `srun`.

## Root Cause
- MPI on ARM nodes has not been tested extensively.
- Potential issue with the MPI library path or compatibility with slurm.
- Possible system issue causing terminal freeze during allocation.

## Solution
- HPC Admin suggests using the module `openmpi/4.1.6-gcc11.4.0-cuda-g2wr7s3` on lukewarm.
- The module was built with `--with-slurm` and should be compatible.
- Further debugging is required to identify the cause of the terminal freeze.

## Additional Information
- The MPI library on lukewarm is located at `/apps/SPACK/0.21.0/share/spack/modules/linux-ubuntu22.04-neoverse_v2/openmpi/4.1.6-gcc11.4.0-cuda-g2wr7s3`.
- Use `ompi_info | grep slurm` to verify slurm components.

## Next Steps
- Volunteers are needed for more detailed debugging.
- Ensure the MPI library is correctly linked and compatible with slurm.
- Investigate the system behavior causing the terminal freeze during allocation.
```
---

### 2018100142002277_libfabric%20IntelMPI%202019%20meggie.md
# Ticket 2018100142002277

 ```markdown
# HPC-Support Ticket: libfabric IntelMPI 2019 Issue

## Keywords
- libfabric
- IntelMPI 2019
- LD_LIBRARY_PATH
- SLURM_MPI_TYPE
- pmi2
- mpirun
- srun
- performance

## Problem Description
- User reported that `libfabric` was not found, which was previously working.
- Missing path: `/apps/intel/ComposerXE2019/compilers_and_libraries_2019.0.117/linux/mpi/intel64/libfabric/lib` in `$LD_LIBRARY_PATH`.

## Root Cause
- Intel MPI 2019 edition required additional `LD_LIBRARY_PATH` settings.
- Compiler updates on September 18th might have caused the issue.

## Solution
- HPC Admins updated the module on Meggie to include the additional `LD_LIBRARY_PATH`.
- User was advised to use `--mpi=pmi2` with `srun` or set the environment variable `SLURM_MPI_TYPE=pmi2`.

## Additional Notes
- Intel MPI 2019 performed better with `mpirun` compared to `srun`.
- HPC Admins noted that performance differences might be due to other factors such as node differences, process placement, memory allocation, or network traffic.
- The ticket was closed as no further actions were required from the HPC team.
```
---

### 2016012942001755_OpenFOAM%20installation.md
# Ticket 2016012942001755

 # HPC Support Ticket: OpenFOAM Installation

## Keywords
- OpenFOAM installation
- Paraview compilation
- Lustre filesystem
- SLES 11 SP3
- Compilation issues

## Problem Description
- User encountered issues while compiling Paraview (v4.1) during OpenFOAM (v2.3.0) installation on an SGI IXE running SLES 11 SP3.
- Error message: `QSqlQuery::value: not positioned on a valid record`, `Cannot register namespace paraview.org!`
- User suspected the issue was due to compiling on a Lustre filesystem.

## Root Cause
- The issue might be related to SLES 11 SP3 rather than the Lustre filesystem.
- Compilation on Lustre should not be a problem if it is fully POSIX compliant.

## Solution
- Compile in a different directory (e.g., `/tmp`) and then install the binary on the Lustre filesystem.
- OpenFOAM can be relocated afterwards by adapting paths in the files used to set up the run environment.

## Additional Notes
- User successfully compiled ThirdParty-2.3.0 on `/tmp`.
- Further support for detailed steps was not provided as it was beyond the scope of free support.

## Conclusion
- The ticket was closed as the issue was not directly related to the HPC services provided by the support team.

## References
- [Paraview Forum Discussion](https://cmake.org/pipermail/paraview/2014-April/030869.html)
- [HPC Services Website](http://www.hpc.rrze.fau.de/)
---

### 2017031042001151_Bitte%20java%201.8%20auf%20LiMa.md
# Ticket 2017031042001151

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject: Bitte java 1.8 auf LiMa

### Keywords:
- Java 1.8
- OpenJDK
- Oracle JDK
- tzdb.dat
- HPC Support
- LiMa
- Woody
- Memoryhog
- Stanford CoreNLP
- TimeZone
- Joda Time

### Summary:
The user requested the installation of Java 1.8 on LiMa, similar to the module available on Woody. The HPC Admins provided a custom OpenJDK module but encountered issues with missing `tzdb.dat` file on the compute nodes. The problem was resolved by copying the file from the frontend to the compute nodes.

### Root Cause:
- Missing `tzdb.dat` file on compute nodes.
- Incompatibility with Oracle JDK due to licensing issues.

### Solution:
- HPC Admins provided a custom OpenJDK module.
- Copied the `tzdb.dat` file from the frontend to the compute nodes to resolve the missing file issue.

### Lessons Learned:
- OpenJDK does not have binary builds, making it challenging to distribute as a module.
- Missing `tzdb.dat` file can cause Java applications to fail, especially those relying on time zone data.
- Custom solutions may be required to address specific software dependencies and licensing issues.
- Effective communication and collaboration between users and HPC Admins are crucial for resolving complex software issues.
```
---

### 2024012942003738_rocm%20auf%20euryale%20hat%20zu%20alte%20glibc.md
# Ticket 2024012942003738

 # HPC Support Ticket: ROCm Update Issue on Euryale

## Keywords
- ROCm
- glibc
- Ubuntu 22.04
- gcc 11.2.0
- libstdc++.so.6
- GLIBCXX_3.4.30

## Summary
The user reported issues with the ROCm 6.0.0 update on Euryale, specifically mentioning that the glibc version was too old.

## Root Cause
The issue was caused by a conflict with the gcc 11.2.0 module. The error message indicated that the required version `GLIBCXX_3.4.30` was not found in the `libstdc++.so.6` library.

## Solution
The user resolved the issue by unloading the gcc 11.2.0 module. Ubuntu 22.04 already includes gcc 11, making the additional module unnecessary.

## Lessons Learned
- Ensure that the correct versions of libraries and modules are loaded to avoid conflicts.
- Provide detailed error messages when reporting issues to facilitate troubleshooting.
- Be aware of the default software versions included in the operating system to avoid redundant module loading.

## Steps to Resolve Similar Issues
1. Check for any conflicting modules or libraries.
2. Unload any unnecessary modules.
3. Verify that the required versions of libraries are available.
4. Provide detailed error messages and steps to reproduce the issue when seeking assistance.

## Additional Notes
- The HPC Admin confirmed that ROCm 6.0.0 is compatible with Ubuntu 22.04 and its glibc version.
- The user's initial description of the issue was vague, highlighting the importance of detailed error reporting.
---

### 2024012342002866_rocm%20versions%20update.md
# Ticket 2024012342002866

 # ROCm Version Update Issue

## Keywords
- ROCm update
- Header file issue
- GCC version conflict
- Perl locale warning
- DKMS dependency

## Summary
A user requested an update of ROCm from version 5.6 to 6.0 on specific systems. After the update, issues with header files and GCC version conflicts were encountered.

## Root Cause
- **Header File Issue**: The ROCm 6.0 update caused a fatal error due to missing `cmath` header file.
- **GCC Version Conflict**: The system compiler was GCC11, but ROCm was selecting GCC12, leading to a mismatch in `libstdc++` versions.
- **Perl Locale Warning**: Perl warnings indicated locale settings were not properly configured.

## Solution
- **Header File Issue**: No specific solution mentioned in the conversation.
- **GCC Version Conflict**: Installing `libstdc++-12-dev` resolved the GCC version conflict.
- **Perl Locale Warning**: No specific solution mentioned in the conversation.

## Additional Notes
- The kernel module rebuild with DKMS is now more reliable.
- The presence of multiple ROCm versions could be beneficial for comparison purposes.
- The dependency chain involving `amdgpu`, `amdgpu-dkms`, `dkms`, and `gcc12` was clarified.

## Lessons Learned
- Ensure that the correct GCC version is selected and compatible libraries are installed.
- Locale settings should be properly configured to avoid Perl warnings.
- Understanding the dependency chain of installed packages can help in troubleshooting issues.
---

### 2018012542002481_%5B%2320180119-0261%5D%20ProPE%3A%20ELPA2017%20with%20Score-P.md
# Ticket 2018012542002481

 # HPC-Support Ticket: ProPE - ELPA2017 with Score-P

## Subject
[#20180119-0261] ProPE: ELPA2017 with Score-P

## Keywords
- Score-P
- ELPA
- Assertion Error
- Compiler
- MPI
- Binary Transfer
- Build Instructions

## Problem Description
The user encountered an assertion error when trying to profile an application using the ELPA 2017.05.003 library with Score-P. The non-instrumented code and the instrumented code with an older version of ELPA (2015.11.001) ran without issues.

## Error Message
```
[Score-P] src/measurement/profiling/scorep_profile_node.c:527: Fatal: Assertion 'parent != ((void*)0)' failed
```

## Versions and Modules Used
- Compiler: intel/17.0
- MPI: intelmpi/5.1
- Score-P: scorep/3.0-intel2-intel-papi

## Lessons Learned
1. **Ticket Routing**: Future tickets should be sent directly to "support-hpc@fau.de" instead of the central helpdesk to avoid unnecessary forwarding.
2. **Binary Transfer**: Transferring binary data is generally not useful. Instead, provide detailed build instructions to reproduce the issue on other systems.
3. **Communication**: Ensure proper communication between different ticket systems to avoid loss of information and maintain context.
4. **Compiler Version**: Specify the exact compiler version, including updates, as different versions may produce different results.
5. **Component Interaction**: The error suggests that one of the components is corrupting the stack or other data structures. Identifying the specific component is crucial.

## Root Cause
The root cause of the problem was not explicitly identified in the conversation. However, it was suggested that one of the components might be corrupting the stack or other data structures.

## Solution
No definitive solution was provided in the conversation. It was suggested to:
- Provide detailed build instructions for all involved components.
- Ensure proper communication and coordination between different HPC centers.
- Consider the possibility of a consistency problem with the automatic instrumentation of the Intel compiler.

## Additional Notes
- The ticket was eventually closed as it did not interest any party involved.
- The user was advised to provide more information, such as a backtrace and access to the source code, if the problem persisted.

## Conclusion
The ticket highlighted the importance of proper communication, detailed build instructions, and the need to specify exact versions of software components when troubleshooting issues in an HPC environment.
---

### 2019102142002031_OpenFOAM%201906%20auf%20emmy.md
# Ticket 2019102142002031

 # HPC Support Ticket: OpenFOAM 1906 auf emmy

## Keywords
- OpenFOAM 1906
- Module loading error
- Typographical error
- Module name

## Problem Description
The user encountered an error when trying to load the OpenFOAM 1906 module on the HPC system "emmy". The error message indicated that the module file could not be located.

## Root Cause
The root cause of the problem was a typographical error in the module name. The user mistakenly used a '1' instead of a lowercase 'L' at the end of the module name.

## Solution
The HPC Admin pointed out the typographical error and advised the user to use the correct module name with a lowercase 'L' instead of '1'.

## Lessons Learned
- Always double-check module names for typographical errors.
- Ensure that the correct characters are used in module names, especially when they are case-sensitive or include similar-looking characters.

## Relevant Information
- **HPC System:** emmy
- **Software:** OpenFOAM 1906
- **Module Name:** `openfoam/1906-gcc8.2.0-openmpi-55wj52l`

## Follow-Up Actions
- None required. The issue was resolved by correcting the module name.
---

### 2022020442001154_Compile%20Error%20siginfo_t%20is%20undefined.md
# Ticket 2022020442001154

 ```markdown
# HPC-Support Ticket: Compile Error siginfo_t is undefined

## Keywords
- Compile Error
- siginfo_t
- GKlib
- CMake
- GNU make
- Intel Compiler
- Feature Test Macros

## Problem Description
The user encountered a compile error while building the GKlib library on the Meggie Cluster. The error indicated that the identifier `siginfo_t` was undefined, which is part of the `signal.h` header.

## Root Cause
The issue was traced to a recent change in the `string.c` file of the GKlib library. The change involved defining and then undefining the `_XOPEN_SOURCE` feature test macro, which led to inconsistencies when including other headers like `signal.h`.

## Solution
The problem was resolved by using an older version of the GKlib library that did not contain the problematic change.

## Lessons Learned
- **Feature Test Macros**: Understanding the proper use of feature test macros is crucial. Defining and then undefining macros like `_XOPEN_SOURCE` can lead to inconsistencies and compilation errors.
- **Library Issues**: Sometimes, issues may lie within the library itself rather than the HPC environment. Checking recent changes in the library can help identify the root cause.
- **Version Compatibility**: Using older, stable versions of libraries can be a quick workaround for issues introduced in newer versions.

## References
- [GKlib Commit](https://github.com/KarypisLab/GKlib/commit/a7f8172703cf6e999dd0710eb279bba513da4fec#diff-430d86fdb6c4a558ab0f1b6648bbfae1720e8bde84f026e95a52740014752040R17)
- [Feature Test Macros](https://www.gnu.org/software/libc/manual/html_node/Feature-Test-Macros.html)
```
---

### 2020072142003212_Rocm%20Interlagos.md
# Ticket 2020072142003212

 # HPC Support Ticket: Rocm Interlagos

## Keywords
- ROCm installation
- OpenCL
- clinfo
- clGetPlatformIDs
- /etc/ld.so.conf.d/x86_64-rocm-opencl.conf
- libOpenCL.so
- libamdocl64.so
- Ubuntu 16.04 (Xenial)
- Ubuntu 18.04 (Bionic)

## Problem Description
- OpenCL programs crash on the first OpenCL function call.
- `clinfo` does not work.
- Error message: `clGetPlatformIDs (-1001)` at `cl::Platform::get(&platforms);`.

## Root Cause
- Incorrect path in `/etc/ld.so.conf.d/x86_64-rocm-opencl.conf`.
- Mismatched ROCm versions and dependencies.
- ROCm packages are designed for Ubuntu 16.04 but Interlagos is running Ubuntu 18.04.

## Troubleshooting Steps
- Checked OpenCL installation paths.
- Verified `/etc/ld.so.conf.d/x86_64-rocm-opencl.conf` for correct paths.
- Confirmed the presence of necessary libraries (`libOpenCL.so`, `libamdocl64.so`).

## Solution
- Updated the path in `/etc/ld.so.conf.d/x86_64-rocm-opencl.conf` to `/opt/rocm-3.5.0/opencl/lib`.
- Possible resolution due to a new ROCm 3.7 version.

## Lessons Learned
- Ensure that the paths in configuration files are correct and point to existing directories.
- Be aware of version mismatches and dependencies when installing ROCm.
- Regular updates can sometimes resolve issues, but they can also introduce new problems.

## Follow-up
- Monitor for any issues after future auto-updates.
- Ensure that dependencies are properly managed and fixed in a timely manner.
---

### 2019030842001241_Kompilier-Probleme%20auf%20Meggie.md
# Ticket 2019030842001241

 # HPC Support Ticket: Compilation Issues on Meggie Server

## Keywords
- Compilation error
- Missing library
- `libtbbmalloc`
- Intel Threading Building Blocks
- Module loading
- Build options

## Problem Description
- **User Issue:** The user encountered a compilation error on the Meggie server due to a missing library (`libtbbmalloc`).
- **Error Message:** `cannot find -ltbbmalloc`
- **Loaded Modules:**
  1. `intelmpi/2017up04-intel`
  2. `mkl/2017up05`
  3. `intel64/17.0up05`

## Solution
- **Root Cause:** The `libtbbmalloc` library, part of the Intel Threading Building Blocks, was not loaded automatically with the compiler module.
- **Resolution:**
  - Load the separate `tbb` module for the required version.
  - Add `-L$TPP_LIBDIR` as an additional build option if necessary.

## Additional Notes
- **Email Address:** Users should use their university email address for support requests.
- **Server Usage:** Meggie server is restricted to projects with high computational needs, and access requires proper justification and approval.

## Example Module Load Command
```bash
module load tbb/<version>
```

## Contact Information
- **HPC Services:**
  - Email: support-hpc@fau.de
  - Website: [HPC Services](http://www.hpc.rrze.fau.de/)

## Support Team
- **HPC Admins:** Thomas, Michael Meier, Anna Kahler, Katrin Nusser, Johannes Veh
- **2nd Level Support:** Lacey, Dane (fo36fizy), Kuckuk, Sebastian (sisekuck), Lange, Florian (ow86apyf), Ernst, Dominik (te42kyfo), Mayr, Martin
- **Head of Datacenter:** Gerhard Wellein
- **Training and Support Group Leader:** Georg Hager
- **NHR Rechenzeit Support:** Harald Lanig
- **Software and Tools Developers:** Jan Eitzinger, Gruber
---

### 2018092442001881_Problem%20since%20last%20update%20with%20c%2B%2B%20compilers.md
# Ticket 2018092442001881

 # HPC Support Ticket: C++ Compiler Issues Post-Update

## Keywords
- C++ Compiler
- Intel Compiler
- Compilation Error
- `__builtin_addressof`
- `_LIB_VERSION_TYPE`
- System Update

## Summary
A user reported compilation issues with C++ code after a system update on the HPC cluster. The code, which previously compiled successfully, now fails with errors related to `__builtin_addressof` and `_LIB_VERSION_TYPE`.

## Root Cause
- The update introduced compatibility issues with the Intel C++ compiler versions (intel64/17.0up01 and intel64/17.0up05).
- The errors indicate problems with built-in functions and library versions that are not recognized by the updated system.

## Errors Reported
1. **Error with intel64/17.0up01:**
   ```
   /usr/include/c++/7/bits/move.h(48): error: identifier "__builtin_addressof" is undefined
   ```
2. **Error with intel64/17.0up05:**
   ```
   /apps/intel/ComposerXE2017/compilers_and_libraries_2017.5.239/linux/compiler/include/math.h(1300): error: identifier "_LIB_VERSION_TYPE" is undefined
   ```

## Solution
- The user was unable to modify the external libraries directly.
- No immediate fix was provided in the conversation, but the issue was acknowledged.

## General Learning
- System updates can introduce compatibility issues with existing code and compilers.
- It is essential to test code with new compiler versions after updates.
- Documentation and forums (e.g., Intel forums) can provide insights into similar issues but may not always offer applicable solutions.

## Next Steps
- HPC Admins should investigate the compatibility issues with the Intel compilers.
- Consider providing a workaround or updating the compiler versions to resolve these issues.
- Communicate with the user about potential fixes or alternative compilers that can be used.

## References
- [Intel Forum Discussion](https://software.intel.com/en-us/forums/intel-c-compiler/topic/760979)
---

### 2020030542001789_Package%20libtbb2.md
# Ticket 2020030542001789

 ```markdown
# HPC-Support Ticket: Package libtbb2

## Keywords
- libtbb2
- module
- installation
- HPC

## Problem
- User requires `libtbb2` to run a program on the HPC.

## Solution
- HPC Admin suggests loading one of the available "tbb" modules instead of installing `libtbb2`.

## Lessons Learned
- Users should check available modules before requesting new installations.
- HPC Admins can guide users to use existing resources efficiently.

## Root Cause
- User was unaware of the existing "tbb" modules that could fulfill their requirements.

## Resolution
- User was advised to load one of the "tbb" modules, resolving the need for a new installation.
```
---

### 2024082842003316_Problem%20with%20my%20conda%20installation_openmpi%20on%20Fritz.md
# Ticket 2024082842003316

 # HPC Support Ticket: Problem with Conda Installation/OpenMPI on Fritz

## Keywords
- Conda installation
- OpenMPI
- SLURM
- PMI support
- mpi4py
- Cython
- ImportError
- OPAL ERROR

## Problem Description
- User unable to run an application compiled with their own Conda installation after maintenance.
- Error message indicates OpenMPI was not built with SLURM's PMI support.
- User wants to use Python, mpi4py, and an external C++ library with a Python interface requiring Cython.

## Root Cause
- OpenMPI installed in the Conda environment is not compatible with the SLURM installation on the cluster.
- Incompatibility between the user's Conda-installed OpenMPI and the cluster's SLURM configuration.

## Solution
- Follow instructions from Conda-forge to install a dummy OpenMPI version compatible with the cluster.
- Load the `python/mpi4py-3.1.1py3.9` module and activate mpi4py.
- Recompile the necessary libraries and install required packages with pip.

## Steps Taken
1. User installed their own OpenMPI in the Conda environment, which worked before the SLURM update.
2. After the update, the user encountered errors related to OpenMPI and SLURM's PMI support.
3. User tried loading the `python/mpi4py-3.1.1py3.9` module and recompiling the necessary libraries.
4. User encountered an `ImportError` related to an undefined symbol.
5. User followed instructions from Conda-forge to install a dummy OpenMPI version, which resolved the issue.

## Lessons Learned
- Ensure compatibility between Conda-installed packages and the cluster's SLURM configuration.
- Follow Conda-forge instructions for using external MPI libraries.
- Load appropriate modules and activate environments before compiling and running applications.
- Be aware of potential issues with specific versions of libraries and compilers.

## References
- [Conda-forge Tips and Tricks](https://conda-forge.org/docs/user/tipsandtricks/#using-external-message-passing-interface-mpi-libraries)
- [NHR@FAU mpi4py Documentation](https://doc.nhr.fau.de/apps/mpi4py/)
---

### 2024120242003937_Help%20to%20install%20%26%20build%20MIRTK%20SVRTK%20toolkit%20with%20modules%20%26%20creating%20cond.md
# Ticket 2024120242003937

 # HPC Support Ticket Conversation Summary

## Keywords
- MIRTK toolkit
- SVRTK package
- Module loading
- CMake
- Conda environment
- NoWritablePkgsDirError

## Issues and Solutions

### Issue 1: Determining Modules for MIRTK Installation
- **Root Cause**: User is unsure which modules to load for installing and building MIRTK with SVRTK.
- **Solution**:
  - Load the following modules: `cmake`, `python`, `intel`, `tbb`, `eigen`.
  - Use the Intel compilers by setting environment variables: `CC=icc`, `CXX=icpc`, `FC=ifort`.
  - Example command:
    ```sh
    module load cmake python intel tbb eigen
    CC=icc CXX=icpc FC=ifort cmake -DWITH_TBB="ON" -DCMAKE_INSTALL_PREFIX="$HOME/MIRTK-install" -DMODULE_SVRTK="ON" ..
    ```

### Issue 2: Conda Environment Creation Error
- **Root Cause**: User encounters `NoWritablePkgsDirError` when creating a Conda environment.
- **Solution**:
  - Refer to the documentation for first-time initialization of the Conda environment: [Python Environment Documentation](https://doc.nhr.fau.de/environment/python-env/#first-time-only-initialization).

## General Learnings
- Always refer to the official documentation for module loading and environment setup.
- Use general module versions unless specific versions are required.
- Ensure proper initialization of Conda environments to avoid permission issues.
- Provide detailed error messages for better troubleshooting.

## Additional Notes
- The HPC Admins do not support packages downloaded from the internet but can provide guidance on module loading and environment setup.
- Use institutional email addresses when contacting support for better communication and tracking.

## References
- [SVRTK Installation Instructions](https://github.com/SVRTK/SVRTK/blob/master/InstallationInstructions.txt)
- [Python Environment Documentation](https://doc.nhr.fau.de/environment/python-env/#first-time-only-initialization)
---

### 2015102142002422_sassena%20instalation%20on%20emmy%20without%20success.md
# Ticket 2015102142002422

 # HPC Support Ticket: Sassena Installation on Emmy

## Keywords
- Sassena installation
- BLAS API
- Gromacs g_nse tool
- Module loading
- CMake errors

## Summary
User attempted to install Sassena on Emmy but encountered issues with missing modules and BLAS API. After realizing Sassena development had stopped, the user switched to installing the Gromacs g_nse tool.

## Root Cause
- Missing modules (xt-mpt, xt-asyncpe) specific to Cray systems.
- BLAS API not found during CMake configuration.
- Incorrect instructions for a specific system (Kraken at Tennessee).

## Solution
- **Sassena Installation:**
  - Load Intel compilers and MPI module: `module load intel64`.
  - Ensure BLAS is included in the Intel MKL and specify the path to it in CMake.
  - Use `icc` instead of `gcc` for compilation.

- **Gromacs g_nse Tool:**
  - Download full Gromacs sources from the provided git repository.
  - Build Gromacs from scratch to include g_nse.
  - HPC Admin provided a custom Gromacs module (gromacs/5.0.8-dev926808d) with g_nse included.

## General Learnings
- Always check the compatibility and relevance of installation instructions for the specific HPC system.
- Ensure all required modules are loaded and paths are correctly specified during the installation process.
- For complex software installations, it may be necessary to build from source with custom modifications.
- HPC Admins can provide custom modules to meet specific user requirements.

## Closure
The ticket was closed as the user was satisfied with the provided custom Gromacs module including the g_nse tool.
---

### 2023101142002382_Intel%20Compiler.md
# Ticket 2023101142002382

 ```markdown
# HPC Support Ticket: Intel Compiler Installation

## Keywords
- Intel Compiler
- Intel MPI
- Module Installation
- Spack Packages
- Public Modules

## Problem
- User requested the installation of Intel compilers from 2023 on the HPC system.
- User wanted to avoid suggesting the use of compilers from a specific user's directories.

## Solution
- HPC Admins confirmed that the latest Intel compilers and MPI were installed as part of the `000-all-spack-pkgs/0.19.1` package.
- The modules were tested and made available with simplified names in the main tree.
- Specific modules installed:
  - `intel-oneapi-compilers/2023.2.1-gcc8.5.0-axze7oc`
  - `intel-oneapi-mpi/2021.10.0-gcc8.5.0-ki6gcj4`
  - `intel-oneapi-mkl/2023.2.0-gcc8.5.0-dklvxdh`
- The modules `intel/2023.2.1` and `intelmpi/2021.10.0` were made public.
- The `mkl/2023.2.0` module was already publicly available.

## General Learnings
- New software installations require careful testing before being made available to users.
- Spack packages are used for managing software installations on the HPC system.
- Public modules simplify access for users and avoid the need to use personal directories.
```
---

### 2022100442002781_Missing%20java%20module%20in%20Woody.md
# Ticket 2022100442002781

 ```markdown
# HPC Support Ticket: Missing Java Module in Woody

## Keywords
- Java module
- Woody machines
- University email address
- HPC Admin
- Module availability

## Problem
- **Root Cause**: The Java module previously available on Woody machines was missing.
- **User Report**: The user noticed the absence of the Java module which was available a few months ago and requested a solution.

## Solution
- **HPC Admin Response**: The HPC Admin informed the user that Woody now has the following Java modules available:
  - `java/jdk8u345-b01-hotspot`
  - `java/jdk8u345-b01-openj9`
- **Additional Note**: The HPC Admin reminded the user to use their university email address when contacting support.

## General Learnings
- Always check the available modules list as new modules might be added.
- Use the appropriate email address for support communications.
- HPC Admins can provide updates on module availability and solutions for missing modules.
```
---

### 2017042142001486_libxml2-utils%20auf%20tinyfat%3F.md
# Ticket 2017042142001486

 # HPC Support Ticket Conversation: libxml2-utils Request

## Keywords
- libxml2-utils
- tinyfat
- memoryhog
- woody
- package installation
- HPC support

## Summary
A user requested the installation of the `libxml2-utils` package on multiple HPC systems: `tinyfat`, `memoryhog`, and `woody`.

## Root Cause
The user needed the `libxml2-utils` package on different HPC systems for their work.

## Solution
- The `libxml2-utils` package was installed on `tinyfat`.
- The package was scheduled to be installed on `woody` after the next system reinstallation.
- No explicit confirmation for `memoryhog` was provided in the conversation.

## General Learnings
- Users may request specific software packages on multiple HPC systems.
- HPC admins can install packages upon request and may schedule installations based on system maintenance cycles.
- Clear communication about the status of requests is important for user satisfaction.

## Next Steps
- Ensure that the `libxml2-utils` package is installed on `woody` after the next reinstallation.
- Confirm the installation status on `memoryhog` if not already done.
- Document the process for handling software installation requests for future reference.
---

### 2017040542000311_libxml2-utils%20auf%20memoryhog%3F.md
# Ticket 2017040542000311

 ```markdown
# HPC Support Ticket: libxml2-utils auf memoryhog

## Keywords
- libxml2-utils
- memoryhog
- installation
- reboot

## Summary
A user requested the installation of the `libxml2-utils` package on the `memoryhog` machine.

## Root Cause
The user needed the `libxml2-utils` package for their work on the `memoryhog` machine.

## Solution
The HPC Admin installed the `libxml2-utils` package and informed the user that the machine would be rebooted.

## Lessons Learned
- Users may request specific software packages for their work.
- Installing new software may require a system reboot.
- HPC Admins should communicate any necessary downtime or reboots to users.

## Actions Taken
- The `libxml2-utils` package was installed on the `memoryhog` machine.
- The machine was rebooted after the installation.

## Follow-up
Ensure that the user is aware of the reboot and any potential downtime.
```
---

### 2020033142003148_Problem%20with%20Home%20Office.md
# Ticket 2020033142003148

 # HPC Support Ticket: Problem with Home Office

## Keywords
- Java module
- Module load
- NoClassDefFoundError
- CORBA
- SSH
- cshpc
- woodymodules

## Summary
A user encountered an error when trying to run a Java application on the HPC cluster. The error indicated a missing class definition for `org/omg/CORBA/ORB`. The user attempted to load the Java module but received an error stating that the module could not be located.

## Root Cause
- The user did not load the necessary modules correctly.
- The Java module was not readily available on the specific cluster (cshpc) without first loading the `woodymodules`.

## Solution
1. **Load the `woodymodules` module:**
   ```sh
   module load woodymodules
   ```
2. **Load the Java module:**
   ```sh
   module load java
   ```
3. **Verify available modules:**
   ```sh
   module avail
   ```

## General Learnings
- Different HPC clusters may have different module loading procedures.
- Always check the available modules using `module avail`.
- Ensure that the necessary modules are loaded before running applications that depend on them.
- SSH can be used to connect to the frontend of the desired cluster.

## Additional Notes
- The user was accessing the cluster via SSH from a Windows PC.
- The error occurred on the `cshpc` cluster, which required loading `woodymodules` before accessing other modules.

This documentation can be used to troubleshoot similar issues related to module loading and Java applications on HPC clusters.
---

### 2019031242000501_renumberMesh-Jobs%20auf%20Meggie%20_%20iwpa79.md
# Ticket 2019031242000501

 ### Problem Description

The user encountered issues with running OpenFOAM simulations on the Meggie cluster using the `openfoam/1812-gcc8.2.0-openmpi+nxjz7f` module. The user was able to run simulations with 50 million cells and 64 nodes successfully. However, the user encountered a segmentation fault when trying to visualize the results using the `paraview/5.4.1-dpm6lq` and `paraview/5.5.2` modules. The `paraview/5.6.0+vomqea` module was not tested.

### Solution

The HPC Admin suggested the user try using the `paraview/5.6.0+vomqea` module to visualize the results. The HPC Admin also mentioned that the segmentation fault issue with the `paraview/5.4.1-dpm6lq` and `paraview/5.5.2` modules might be related to the libraries not being found: "error while loading shared libraries: libOpenGL.so.0: cannot open shared object file: No such file or directory". The HPC Admin suggested that the issue might take some time to fix.

### Conclusion

The user should try using the `paraview/5.6.0+vomqea` module to visualize the results. The HPC Admin will look into fixing the segmentation fault issue with the `paraview/5.4.1-dpm6lq` and `paraview/5.5.2` modules.
---

### 2022092142001191_Neuer%20Woody.md
# Ticket 2022092142001191

 # HPC Support Ticket: Neuer Woody

## Keywords
- Woody Upgrade
- Dependency Issues
- cmake, motif, root, geant4
- openssl, x11, freetype
- LD_LIBRARY_PATH
- module load

## Problem Description
The user's Pixel Detector Simulation Framework stopped working after the upgrade to the new Woody system. The framework relies on several dependencies that were previously available in `/usr` but are now missing. Specifically, the user mentioned missing dependencies like openssl, x11, and freetype.

## Root Cause
The upgrade to the new Woody system resulted in missing dependencies that were previously available in `/usr`. The user's attempt to manually copy files did not resolve the issue.

## Solution
1. **Install Missing Dependencies**: The HPC Admin installed the missing dependencies required for the user's framework.
2. **Use Module Load**: The user was advised to use `module load` for python and cmake, and to specify the version for gcc and g++.
3. **Set LD_LIBRARY_PATH**: The user was advised to set the `LD_LIBRARY_PATH` environment variable to ensure the software can find the required libraries.

## Lessons Learned
- **Communication**: Early communication about system upgrades and their potential impact on user workflows is crucial.
- **Dependency Management**: Proper management of dependencies and understanding of the system's module system can prevent such issues.
- **Environment Variables**: Setting environment variables like `LD_LIBRARY_PATH` can help resolve library path issues.

## Follow-up Actions
- The user should test the framework and report any additional missing dependencies.
- The HPC Admin should verify the installation of the requested packages and ensure they are compatible with the new system.

## References
- ECAP-Chat in #ask-your-admin
- HPC Admin's email instructions for installing dependencies and setting environment variables.
---

### 2019012442002098_openfoam%20v1812.md
# Ticket 2019012442002098

 ```markdown
# HPC-Support Ticket: OpenFOAM v1812 Upgrade

## Keywords
- OpenFOAM
- Upgrade
- Dependencies
- Compilation
- Testing

## Problem
- User requested an upgrade from OpenFOAM v1806 to v1812 on Emmy and Meggie clusters.
- New features (waveMaker boundary conditions) in ESI-OpenFOAM v1812 were needed for simulations.

## Root Cause
- Initial attempts to build OpenFOAM v1812 failed due to various dependencies and incompatibilities.

## Solution
- HPC Admin found a combination of 60 packages that allowed OpenFOAM to compile without errors.
- The compiled version was made available on Emmy as `openfoam/1812-gcc8.2.0-openmpi+zmg5k2`.

## Outcome
- User tested the new version and confirmed that the required boundary conditions worked correctly.

## General Learnings
- Upgrading software with complex dependencies can be challenging and time-consuming.
- Collaboration between users and HPC Admins is crucial for successful software upgrades.
- Testing new software versions is essential to ensure functionality.
```
---

### 2023112342001617_Intel%20MKL%20Pardiso.md
# Ticket 2023112342001617

 # HPC Support Ticket: Intel MKL Pardiso

## Keywords
- Intel MKL
- Pardiso
- Module
- Library
- Linking

## Summary
The user inquired about the availability of Intel MKL Pardiso on the HPC system "Fritz" and how to load it using a module.

## Problem
- The user was unable to find the Pardiso library after loading the Intel MKL module.
- The user searched for Pardiso-related files but only found header files, not the actual library.

## Solution
- The HPC Admin clarified that Pardiso is included in the Intel MKL libraries and does not have a separate library file.
- The user was advised to use the Intel Link Line Advisor tool to determine which MKL library to link against in their application.

## Steps Taken
1. **User Inquiry**: The user asked about the availability of Intel MKL Pardiso and the module to load it.
2. **Admin Response**: The admin suggested using `module avail mkl` to find available MKL modules.
3. **User Follow-up**: The user reported not finding the Pardiso library after loading the module.
4. **Admin Clarification**: The admin explained that Pardiso is part of the MKL libraries and provided a link to the Intel Link Line Advisor tool for further assistance.

## Lessons Learned
- Pardiso is integrated into the Intel MKL libraries and does not have a separate library file.
- The Intel Link Line Advisor tool can help determine which MKL library to link against for specific functionalities.
- Users should be aware that some functionalities might be part of larger libraries and not available as standalone components.

## References
- [Intel oneMKL Link Line Advisor](https://www.intel.com/content/www/us/en/developer/tools/oneapi/onemkl-link-line-advisor.html)

## Conclusion
The issue was resolved by clarifying that Pardiso is part of the MKL libraries and providing a tool to assist with linking the correct library. This information can be useful for future users encountering similar issues.
---

### 2018060542001644_Probleme%20mit%20sander.MPI%20%28AMBER%29%20auf%20Emmy.md
# Ticket 2018060542001644

 # HPC Support Ticket: Probleme mit sander.MPI (AMBER) auf Emmy

## Problem
- User has issues with molecular dynamics simulations using AMBER on Emmy.
- `pmemd.MPI` works with all available AMBER versions, but `sander.MPI` crashes during simulation with most versions.
- Only `amber/12p21-at13p26-intel16.0-intelmpi5.1` and `amber/12p21-at12p38-intel16.0-intelmpi5.1` work without crashing.

## Root Cause
- `sander.MPI` crashes in Intel Compiler libraries.
- All available Amber12, Amber14, and Amber16 modules are compiled with the same Intel Compiler, while testing modules use a newer compiler version.

## Solution
- User compiled AmberTools16 with GNU compilers and OpenMPI on Emmy.
- `sander.MPI` (gcc-4.8.5/openmpi-2.0.2-gcc) runs without errors on a single node.
- HPC Admin provided a script to run on multiple nodes:
  ```bash
  #PBS -l nodes=2:ppn=40
  mpirun -npernode 20 -np 40 sander.MPI -ng 2 -groupfile 01-pull.group
  ```

## Keywords
- AMBER
- sander.MPI
- pmemd.MPI
- Intel Compiler
- GNU Compiler
- OpenMPI
- Emmy
- Molecular Dynamics Simulations

## General Learnings
- Compiler issues can cause crashes in specific modules.
- Users can compile software themselves if needed.
- Adjusting batch scripts for multiple nodes requires specific directives and `mpirun` options.

## Next Steps
- Test the compiled version on multiple nodes.
- Optimize compilation options for Emmy if needed.

## References
- HPC Services, Friedrich-Alexander-Universitaet Erlangen-Nuernberg, Regionales RechenZentrum Erlangen (RRZE)
- AmberTools16 documentation for compilation and usage.
---

### 2018041742001778_Softwareausstattung%20Emmy.md
# Ticket 2018041742001778

 # HPC Support Ticket: Softwareausstattung Emmy

## Keywords
- Emmy-Cluster
- Intel Compiler
- Boost Library
- GCC
- C++ 17 Features

## Problem
- User noticed that Boost library is only available for Intel 16, not for Intel 17 and Intel 18.
- The latest version of GCC available is 6.1.
- User inquires about the STL used by Intel compilers and requests GCC 7 for C++ 17 features.

## Root Cause
- Lack of Boost library modules for newer Intel compilers.
- Outdated GCC version not supporting C++ 17 features.

## Solution
- **Boost Library**: HPC Admin confirmed that Boost modules labeled "intel16" are compatible with newer Intel compilers.
- **GCC Version**: GCC 7.3.0 has been installed on Emmy, addressing the need for C++ 17 features.

## General Learning
- Boost libraries can often be used with newer compiler versions even if not explicitly labeled for them.
- Updating GCC to a newer version can provide access to the latest C++ features.

## Actions Taken
- HPC Admin confirmed compatibility of Boost modules.
- GCC 7.3.0 was installed on Emmy.

## Follow-up
- Users should test the compatibility of Boost libraries with newer Intel compilers.
- Ensure that the latest GCC version is available for users needing advanced C++ features.
---

### 2024100942004409_GCC%2013%20Modul.md
# Ticket 2024100942004409

 ```markdown
# HPC-Support Ticket: GCC 13 Module Request

## Keywords
- GCC 13
- Woody-Cluster
- Module
- Compiler

## Summary
A user requested the installation of GCC 13 as a module on the Woody-Cluster for software compatibility.

## Root Cause
The user's software required GCC 13, which was not available as a module on the Woody-Cluster.

## Solution
The HPC Admin team installed GCC 13.3.0 as a module on the Woody-Cluster.

## General Learning
- Users may require specific compiler versions for their software.
- The HPC Admin team can install and provide specific software versions as modules upon request.
- Effective communication between users and the HPC Admin team ensures that necessary software is made available.
```
---

### 42066046_Problem%20OpenFoam-1.7.1.md
# Ticket 42066046

 # HPC-Support Ticket Conversation: Problem OpenFoam-1.7.1

## Keywords
- OpenFoam-1.7.1
- Compilation Error
- wmake
- Include Files
- Access Permissions

## Summary
The user encountered compilation errors while trying to compile `icoFoam` using `wmake` in OpenFoam-1.7.1. The errors were related to missing include files such as `fvCFD.H`.

## Root Cause
- Missing or incorrectly linked include files.
- Incorrect access permissions for the include files.

## Steps Taken
1. **User Reported Issue**: The user reported compilation errors due to missing include files.
2. **HPC Admin Action**: The HPC Admin regenerated around 5000 links in the OpenFOAM directory to ensure the include files were correctly linked.
3. **User Follow-Up**: The user re-logged into the system and reloaded OpenFoam, but the issue persisted.
4. **HPC Admin Diagnosis**: The HPC Admin identified that the access permissions for the links were incorrectly set.
5. **Solution Provided**: The HPC Admin advised the user to replace `FOAM_APPBIN` with `FOAM_USER_APPBIN` or another directory where the user has write permissions.

## Solution
- Ensure that the include files are correctly linked and accessible.
- Check and correct the access permissions for the include files.
- Replace `FOAM_APPBIN` with `FOAM_USER_APPBIN` or another directory with write permissions in the `Make/files` configuration.

## Outcome
The user confirmed that the solution worked and the compilation was successful.

## General Learning
- Compilation errors due to missing include files can often be resolved by ensuring the files are correctly linked and accessible.
- Incorrect access permissions can prevent the compiler from accessing necessary files.
- Adjusting the configuration to use directories with appropriate write permissions can resolve access-related compilation issues.
---

### 2018121342001448_Elmer_Ice%20Kompilierung.md
# Ticket 2018121342001448

 # HPC-Support Ticket: Elmer/Ice Compilation Issue

## Keywords
- Elmer/Ice
- Compilation
- Intel MPI
- MKL
- .bashrc
- Environment Variables
- Module Loading

## Problem Description
The user encountered issues while compiling Elmer/Ice on the Woody cluster. The initial compilation worked, but subsequent attempts to compile additional routines resulted in an error related to the module file format.

## Root Cause
The root cause of the problem was identified as a conflict in the environment variables and modules loaded through the user's `.bashrc` and other configuration files. This led to inconsistencies in the versions of Intel MPI and other dependencies being used.

## Solution
The HPC Admin suggested that the user's `.bashrc` and other configuration files were loading conflicting modules and setting environment variables incorrectly. The user confirmed that adjusting these settings resolved the issue.

## Lessons Learned
- **Environment Configuration**: Ensure that the `.bashrc` and other configuration files do not load conflicting modules or set incorrect environment variables.
- **Module Loading**: Verify that the correct modules are loaded and that there are no conflicts between them.
- **Compiler Compatibility**: Ensure that all modules and dependencies are compatible with the compiler being used.

## Additional Notes
- The HPC Admin mentioned that the `intel64` module automatically loads `mkl` and `intelmpi`. Manually loading `intelmpi` indicates a deeper issue with the environment configuration.
- The user was advised to provide complete output and environment variable settings for further troubleshooting.
- The HPC Admin also noted potential issues with MPI and MKL versions, which may require further investigation and possibly opening a support case with Intel.

## References
- [Intel MKL 2018 Bug Fixes List](https://software.intel.com/en-us/articles/intel-math-kernel-library-intel-mkl-2018-bug-fixes-list)
- [Intel Clusters and HPC Technology Forums](https://software.intel.com/en-us/forums/intel-clusters-and-hpc-technology)
---

### 2023062042001801_OpenMPI-Problem.md
# Ticket 2023062042001801

 ```markdown
# OpenMPI-Problem

## Subject
OpenMPI-Problem

## Keywords
- OpenMPI
- SLURM
- srun
- mpirun
- dock6.mpi
- module load
- recompilation
- patchelf

## Problem Description
The user encountered an error when submitting a job script using `srun` with OpenMPI. The error message indicated that OpenMPI was not built with SLURM support.

## Root Cause
- The OpenMPI modules were not compiled with SLURM support.
- The `dock6.mpi` application had a hardcoded library path for MPI, ignoring loaded modules.

## Solution
- Use `mpirun` instead of `srun` as a workaround.
- Recompile `dock6.mpi` to properly support SLURM.
- Alternatively, use `patchelf` to change the library path in the existing binary.

## Steps Taken
1. **Initial Diagnosis**:
   - The user submitted a job script using `sbatch` and `srun`, but it failed with an error indicating OpenMPI was not built with SLURM support.
   - The user found that using `mpirun` instead of `srun` resolved the issue.

2. **HPC Admin Investigation**:
   - The HPC Admin identified that several OpenMPI modules were not compiled with SLURM support.
   - The Admin recompiled some of the modules to include SLURM support.
   - The Admin noted that `dock6.mpi` had a hardcoded library path, which caused it to ignore loaded modules.

3. **Workaround**:
   - The user was advised to use `mpirun` instead of `srun` as a temporary solution.

4. **Long-term Solution**:
   - The user was advised to recompile `dock6.mpi` to properly support SLURM.
   - The Admin suggested using `patchelf` to change the library path in the existing binary as an alternative.

## Conclusion
The issue was caused by a lack of SLURM support in the OpenMPI modules and a hardcoded library path in `dock6.mpi`. The immediate workaround is to use `mpirun`, while the long-term solution is to recompile `dock6.mpi`.
```
---

### 2023110642001784_update%20R%20module.md
# Ticket 2023110642001784

 ```markdown
# HPC Support Ticket: Update R Module

## Keywords
- R module update
- Conda installation
- HPC environment
- Software versioning

## Problem
- User requested an update to the available R module on the HPC systems (fritz/alex).
- Current version: r/4.2.2-conda
- Requested versions: r/4.3.1 or r/4.3.2

## Root Cause
- The existing R module was outdated and needed to be updated to a newer version.

## Solution
- HPC Admin updated the R module to r/4.3.2-conda.
- User was informed about the availability of the new version.

## What Can Be Learned
- Importance of keeping software modules up-to-date.
- Process of updating software modules using Conda.
- Communication between users and HPC support for software updates.

## Actions Taken
- HPC Admin checked for the availability of a script or list of software to be installed via Conda.
- New R module (r/4.3.2-conda) was installed and made available on the HPC system.
- User was notified about the update and how to load the new module.
```
---

### 2025021742003533_user-spack.md
# Ticket 2025021742003533

 # HPC Support Ticket: user-spack

## Keywords
- Spack
- Module stack
- Installation paths
- Dependencies
- TCL-Modules
- Config-Dateien
- Shell-Alias

## Problem
The user from RUB is considering how to update their module stack and is interested in how FAU handles user-spack modules, installation paths, and dependencies. They initially considered installing all modules in a single directory but now believe it's better to install modules per Spack version to ensure the latest dependencies.

## Solution
FAU provided their Spack setup and user-spack module file. They use TCL-Modules for loading modules and have separate directory trees for each Spack version. For user-spack, they use slightly modified config files and a shell alias to refer to these config files. They suggested that a version-specific intermediate directory could be added for user-spack.

## General Learnings
- Using separate directories for each Spack version ensures that the latest dependencies are used.
- TCL-Modules are used for loading modules instead of Spack-internal mechanisms.
- Shell aliases and custom config files can be used to manage different Spack setups.
- It's important to consider how to handle installation paths and dependencies when updating the module stack.
---

### 2022071742000845_mpi%20error%20fritz%20cluster.md
# Ticket 2022071742000845

 # HPC Support Ticket: MPI Error on Fritz Cluster

## Keywords
- MPI Error
- Intel MPI
- Fritz Cluster
- PMPI_Init
- PMI2_Job_GetId
- WALBERLA
- pystencils
- lbmpy

## Problem Description
- User encounters an MPI error when using the `intelmpi/2021.6.0` module on the Fritz cluster.
- The error message indicates a fatal error in `PMPI_Init` with `PMI2_Job_GetId` returning 14.
- The issue occurs during the build process of the WALBERLA application, which also involves `pystencils` and `lbmpy`.

## Ticket Conversation Summary
- **User**: Reports MPI error with `intelmpi/2021.6.0` on Fritz cluster.
- **HPC Admin**: Acknowledges no known issues with `intelmpi/2021.6.0`, but `intelmpi/2021.4.0` is known to be broken post OS upgrade. Further checks will be conducted.
- **HPC Admin**: Requests additional details including the application used, how it is started, and the job script.
- **User**: Provides details about using WALBERLA with updated versions of `pystencils` and `lbmpy`. The error occurs during the build process.
- **HPC Admin**: Clarifies whether the error occurs during the build or runtime and suggests consulting colleagues for building issues.

## Root Cause
- The root cause of the MPI error is not explicitly identified in the conversation.
- Potential issues could be related to the interaction between WALBERLA, `pystencils`, `lbmpy`, and the MPI environment.

## Solution
- No definitive solution is provided in the conversation.
- Further investigation and consultation with colleagues are recommended.

## What Can Be Learned
- **MPI Error Troubleshooting**: Understanding the error stack and identifying which part of the process (build vs. runtime) is affected.
- **Application-Specific Issues**: Issues with specific applications like WALBERLA may require consultation with colleagues familiar with the application.
- **Module Compatibility**: Ensure compatibility of MPI modules with the cluster's OS and other software dependencies.

## Next Steps
- Continue investigating the interaction between WALBERLA, `pystencils`, `lbmpy`, and the MPI environment.
- Consult with colleagues or application-specific support for further assistance.
- Monitor for similar issues with other users to identify patterns or common causes.
---

### 2022112942002214_iwal081h%3A%20Probleme%20mit%20cmake%203.18.md
# Ticket 2022112942002214

 # HPC Support Ticket: Probleme mit cmake 3.18

## Keywords
- cmake
- Illegal instruction
- AVX2
- Zen2
- TinyGPU Cluster
- module load

## Problem Description
- User encountered an "Illegal instruction" error when trying to use cmake 3.18.4 on the TinyGPU Cluster.
- The error occurred after loading the module with `module load cmake/3.18.4`.
- The path to the cmake binary was `/apps/SPACK/0.16.0/opt/linux-ubuntu20.04-zen2/gcc-9.3.0/cmake-3.18.4-llfdglrmtan32gilphysoeoqzuz4cf7j/bin/cmake`.

## Root Cause
- The current cmake version was built for Zen2 architecture, which includes AVX2 instructions.
- The TinyGPU Cluster (tinyx) does not support AVX2 instructions.

## Solution
- HPC Admin rebuilt cmake to be compatible with the TinyGPU Cluster.
- A new version, cmake/3.23.1, was provided.
- The user was instructed to load the new module and try again.

## Follow-up
- After loading the new module, the user still encountered the "Illegal instruction" error.
- HPC Admin recompiled cmake again to ensure compatibility.

## General Learning
- Ensure that software is built with the correct architecture and instruction set for the target hardware.
- Rebuilding software with the appropriate flags can resolve "Illegal instruction" errors.
- Communication between the user and HPC Admin is crucial for diagnosing and resolving issues.
---

### 2020090242000864_Uptdate%20GAMMA-Software%20auf%20HPC.md
# Ticket 2020090242000864

 ```markdown
# HPC-Support Ticket Conversation: Update GAMMA-Software

## Keywords
- GAMMA-Software
- Woody
- TinyEth
- Module
- Installation
- FFT-Library
- libsfftw.so.2
- sfftw2.deb

## Summary
A user requested an update for the GAMMA-Software to be installed as a module on Woody and TinyEth. The installation process involved copying and extracting the software package and updating the PATH in the .bashrc file.

## Issues Encountered
- Missing FFT-Library (libsfftw.so.2) for certain binaries (`lin_comb` and `ratio`) on Woody3.
- Previous versions of the binaries did not function correctly.

## Solutions
- The HPC Admin installed the necessary FFT-Library to ensure the binaries function correctly.
- The admin considered installing the `sfftw2.deb` package but decided against it due to additional dependencies.

## Lessons Learned
- Ensure all required libraries are available when installing new software modules.
- Communicate with users to understand the necessity of specific binaries and their dependencies.
- Document the installation process and any additional steps taken to resolve issues for future reference.

## Root Cause
- The root cause of the issue was the missing FFT-Library required by certain binaries in the GAMMA-Software.

## Solution
- The HPC Admin resolved the issue by ensuring the necessary FFT-Library was available for the binaries to function correctly.
```
---

### 42203637_Installation%20DL_Poly%202.19%20am%20LiMa.md
# Ticket 42203637

 # HPC Support Ticket: Installation of DL_Poly 2.19 on LiMa

## Keywords
- DL_Poly 2.19
- LiMa
- Makefile
- Intel Compiler
- Intel MPI
- Module Load

## Summary
A user requested assistance with installing a modified version of the molecular dynamics program DL_Poly 2.19 on the LiMa system. The user had previously installed and tested the program on the eamon servers and provided the source code and Makefile.

## Root Cause
The user needed guidance on how to adapt the Makefile for the LiMa system to ensure proper installation and execution.

## Solution
- The Makefile already contained a target for "woodcrest," which should work on LiMa without modification.
- The user was advised to load the module for an up-to-date Intel Compiler with Intel MPI using the command `module load intel64`.

## General Learnings
- Ensure that the Makefile is compatible with the target system.
- Load the appropriate modules for the compiler and MPI library before compiling and running the program.
- Collaboration between the user and HPC support can help in identifying and resolving installation issues.

## Next Steps
- The user should attempt to compile and run the program on LiMa using the provided instructions.
- If further issues arise, the user can seek additional assistance from the HPC support team.
---

### 2017040342002394_compiling%20waves2Foam%20unter%20OpenFOAM%202.3.0%20-%20Lima.md
# Ticket 2017040342002394

 ```markdown
# HPC-Support Ticket: Compiling waves2Foam under OpenFOAM 2.3.0 - Lima

## Keywords
- OpenFOAM
- waves2Foam
- Compilation
- Gnu Scientific Library (GSL)
- Intel Compiler
- C++11 Features
- Module Loading
- Permissions

## Problem Description
- User needs to compile the waves2Foam extension toolbox for OpenFOAM 2.3.0 on Lima.
- Compilation errors occur despite GSL being installed.
- Initial error due to missing `git` command.
- Subsequent error related to C++11 features and Intel Compiler compatibility.

## Root Cause
- Missing `git` command prevented the compilation script from cloning the OceanWave3D repository.
- Incompatibility between the Intel Compiler version and C++11 features used in the code.

## Solution
1. **Install `git` on Frontends:**
   - HPC Admin installed `git` on the frontends to resolve the initial error.

2. **Update Intel Compiler:**
   - User was advised to load a newer Intel Compiler version to support C++11 features.
   ```bash
   module load openfoam/2.3.0-intel13.1-intelmpi4.1
   module rm intel64
   module load intel64/16.0up03
   ```

3. **Copy Required Libraries:**
   - User was instructed to copy GSL and Atlas libraries to a directory accessible by OpenFOAM on the compute nodes.
   ```bash
   cp /lib64/libgsl.so.0 /lib64/libgslcblas.so.0 /usr/lib64/atlas/libsatlas.so.3 $FOAM_USER_LIBBIN
   ```

4. **Permissions Issue:**
   - User encountered permission issues accessing the required directory.
   - HPC Admin corrected the permissions to allow access.

## Outcome
- The ticket was closed after the user successfully compiled waves2Foam following the provided instructions.

## General Learnings
- Ensure all required tools (e.g., `git`) are installed before attempting to compile software.
- Compatibility issues between compilers and code features (e.g., C++11) can cause compilation errors.
- Updating to a newer compiler version can resolve compatibility issues.
- Proper management of module loading and library paths is crucial for successful compilation.
- Permission issues can prevent access to necessary directories and should be addressed promptly.
```
---

### 42212925_Orca%20OpenMPI%20Module%20problem..md
# Ticket 42212925

 # HPC Support Ticket: Orca OpenMPI Module Problem

## Keywords
- OpenMPI
- Intel Compiler
- Module Loading
- ORCA
- Shared Libraries
- libimf.so
- libmpi_cxx.so.0

## Problem Description
The user encountered an error while trying to run a job on the woody cluster using ORCA and OpenMPI. The error messages indicated that OpenMPI is not supported and there were issues with shared libraries (`libimf.so` and `libmpi_cxx.so.0`).

## Root Cause
The user did not load the required Intel compiler module before loading the OpenMPI module, leading to missing shared libraries. Additionally, there were module conflicts that needed to be resolved.

## Solution
1. **Load Modules in Correct Order**: First load the ORCA module, then the Intel compiler module.
   ```bash
   module load orca/2.9.1-amd64
   module load intel64/11.1up9
   ```
2. **Resolve Module Conflicts**: If there are conflicts, unload the conflicting modules as suggested by the warning messages.
   ```bash
   module unload intelmpi
   ```

## Lessons Learned
- Always follow the instructions provided in the error messages.
- Load modules in the correct order to avoid dependency issues.
- Resolve module conflicts by unloading the conflicting modules as suggested.
- Provide exact error messages when reporting issues to facilitate troubleshooting.

## Follow-up
If the problem persists, provide the exact error messages for further diagnosis.
---

### 2018032142000683_Fwd%3A%20F%C3%83%C2%BCr%20den%20LiMa%20Administrator.md
# Ticket 2018032142000683

 # HPC Support Ticket: GAMESS Compilation and Configuration

## Keywords
- GAMESS
- ATLAS
- MKL
- Kernel Parameters
- Shared Memory
- Distributed Data Interface (DDI)

## Summary
A guest researcher encountered issues with compiling and running GAMESS due to missing links for the ATLAS library and kernel parameter settings for shared memory.

## Root Cause
- Missing symbolic links for ATLAS library.
- Incorrect kernel parameter settings for shared memory.

## Solution
- **ATLAS Library**: ATLAS is not installed on the compute nodes. Use Intel MKL instead, which provides identical BLAS routines.
  - If using Intel compilers (module "intel64"), the MKL module is automatically loaded.
  - Otherwise, manually load the MKL module using `module load mkl`.
- **Kernel Parameters**: The kernel parameters for shared memory are already set to higher limits on the system, so no changes are needed.

## General Learnings
- Always check for the availability of specific libraries on the compute nodes.
- Use recommended libraries (e.g., Intel MKL) that are optimized for the system's hardware.
- Verify kernel parameter settings, but note that the system may already have appropriate defaults.

## Actions Taken
- HPC Admins advised the user to switch from ATLAS to Intel MKL.
- Confirmed that the kernel parameters for shared memory are already set to higher values.

## Follow-up
- The user was informed about the changes and advised to proceed with the recommended configurations.

## Notes
- The ticket was forwarded by the NHR Rechenzeit Support to the HPC Admins for resolution.
- The guest researcher was on leave, and the response was delayed until their return.
---

### 2024073042001324_Amber24%20on%20TinyGPU%20-%20bcpc101h.md
# Ticket 2024073042001324

 # HPC Support Ticket: Amber24 Installation on TinyGPU

## Keywords
- Amber24
- TinyGPU
- Alex
- GPU
- CUDA
- Software Installation

## Problem
- User requested the installation of Amber24 on TinyGPU to split jobs between Alex and TinyGPU.

## Solution
- HPC Admin installed Amber24 on TinyGPU.
- Available version: `amber-gpu/24p02-at24p03-gnu-cuda11.8`

## General Learnings
- Users may request specific software versions to ensure compatibility across different HPC systems.
- HPC Admins can install requested software versions to meet user needs.
- Clear communication about available software versions is crucial for user satisfaction.

## Root Cause
- User needed Amber24 on TinyGPU to maintain consistency with jobs running on Alex.

## Resolution
- HPC Admin installed the requested software version and informed the user about its availability.

## Follow-up
- Ensure that the installed software version meets the user's requirements.
- Document the installation process for future reference.
---

### 2022022242001156_Alex%20gromacs_plumed%20script.md
# Ticket 2022022242001156

 # HPC Support Ticket: Unused Environment Variable Warning

## Keywords
- OpenMPI
- UCX_ROOT
- UCX_WARN_UNUSED_ENV_VARS
- Environmental variables
- Metadynamics tests

## Problem Description
User encountered a warning message after running a metadynamics test script on the HPC system:
```
parser.c:1888 UCX WARN unused env variable: UCX_ROOT (set UCX_WARN_UNUSED_ENV_VARS=n to suppress this warning)
```

## Root Cause
The warning is related to OpenMPI and indicates an unused environment variable (UCX_ROOT).

## Solution
- The warning is not critical and does not affect the simulation results.
- To suppress this warning, set the environment variable `UCX_WARN_UNUSED_ENV_VARS=n`.
- As the software configuration on the HPC system is not final, the message can be ignored for now.

## General Learnings
- Unused environment variable warnings from OpenMPI are generally not critical.
- Such warnings can be suppressed by setting specific environment variables.
- During software configuration transitions, non-critical warnings may be ignored.

## Ticket Status
The ticket was closed as the warning was deemed non-critical and the user was advised to ignore it until the final software configuration is established.
---

### 42058677_C%2B%2B%20Bibliothek%20Diffpack%20auf%20Woody.md
# Ticket 42058677

 ```markdown
# HPC Support Ticket: Installing Diffpack Library on Woody

## Keywords
- Diffpack
- Woody
- C++ Library
- Installation
- Long-running Simulations
- License
- Job Duration

## Summary
A user inquired about installing the C++ library "Diffpack" on the Woody HPC system for running long simulations. The user had limited experience with Woody and needed guidance on the installation process.

## Root Cause
- User lacked experience with Woody.
- Needed to install a specific C++ library (Diffpack) for simulations.

## Solution
- **Installation Process**: The user was instructed to place the installation files in a subdirectory under `$WOODYHOME` (`/home/woody/iwst/iwstXX/`). The HPC Admin would then review the files the following week.
- **License Inquiry**: The HPC Admin asked about the licensing of the library.
- **Job Duration**: The user was informed that a single job on Woody can run for a maximum of 24 hours, but restarting or chaining jobs is allowed.

## General Learnings
- **Installation Requests**: Users should place installation files in designated directories for HPC Admin review.
- **Job Duration Limits**: Users should be aware of job duration limits on HPC systems and plan accordingly (e.g., using job chaining or restarts).
- **License Considerations**: Licensing of software libraries is an important consideration for installation on HPC systems.
```
---

### 42023473_%5BFwd%3A%20Re%3A%20Intel%20C%2B%2B-Compiler%20und%20Intel%20MPI-Bibliothek%5D.md
# Ticket 42023473

 # HPC Support Ticket: Intel C++ Compiler and Intel MPI Library

## Keywords
- Intel C++ Compiler
- Intel MPI Library
- Licensing
- OpenSource MPI Implementations
- Intel Cluster Toolkit Compiler Edition for Linux

## Summary
A user inquired about obtaining a license for the Intel C++ Compiler and the availability of the Intel MPI Library. The HPC Admins provided information on licensing options and potential workarounds for using the Intel MPI Library.

## Problem
- The user needed a license for the Intel C++ Compiler.
- The user was interested in the Intel MPI Library, which was not listed in the RRZE price list.

## Solution
- **Intel C++ Compiler**: The user was advised to obtain a license for the Intel C++ Compiler (Bestellnummer: IT-ICC-P-L-E-5) from the RRZE.
- **Intel MPI Library**:
  - The HPC Admins informed the user that the current Intel MPI license is cluster-locked and cannot be officially resold on the campus.
  - Suggested alternatives:
    - Use open-source MPI implementations (mpich, mpich2, mvapich, mvapich2, open-mpi).
    - Purchase Intel MPI or the complete Intel Cluster Toolkit Compiler Edition for Linux from an Intel software reseller.
    - Compile on RRZE HPC systems and use the freely available runtime libraries for Intel MPI.

## Additional Information
- The RRZE plans to upgrade to the "Intel Cluster Toolkit Compiler Edition for Linux" in the fall, which may allow for more flexible licensing options.
- The user was provided with links to Intel product information and potential resellers for pricing details.

## Conclusion
The user was given multiple options to address their needs for the Intel C++ Compiler and the Intel MPI Library, including both short-term and long-term solutions.
---

### 2025022142002071_LAMMPS%20and%20MUMPS%20installation%20issues%20in%20julia.md
# Ticket 2025022142002071

 # HPC-Support Ticket: LAMMPS and MUMPS Installation Issues in Julia

## Keywords
- LAMMPS
- MUMPS
- Julia
- MPI
- OpenMPI
- MPIPreferences.jl
- libmpi.so
- pmix_framework_names

## Problem Description
- User encountered issues installing LAMMPS and MUMPS packages in Julia on the HPC system.
- Error logs indicated that `libmpi.so` could not be loaded, despite the file existing in the given path.
- The user had loaded the following modules: `nvhpc/22.3`, `openmpi/4.1.3-nvhpc22.3`, `hwloc/2.7.1`.

## Root Cause
- Conflict between Julia's default MPI binaries and the system-provided OpenMPI loaded via modules.
- Undefined symbol `pmix_framework_names` in `libopen-pal.so.80`.

## Solution
1. **Install MPIPreferences.jl**:
   ```julia
   julia --project -e 'using Pkg; Pkg.add("MPIPreferences")'
   ```

2. **Configure MPI.jl to Use the System MPI**:
   ```julia
   julia --project -e 'using MPIPreferences; MPIPreferences.use_system_binary()'
   ```

3. **Rebuild MPI.jl**:
   - This step ensures that the changes are applied, and MUMPS_jll and LAMMPS_jll link against the system's MPI libraries.

## Outcome
- The user successfully installed the LAMMPS and MUMPS packages in Julia after following the provided steps.

## General Learning
- When encountering issues with MPI-related packages in Julia, ensure that the system's MPI implementation is correctly configured and used.
- The `MPIPreferences.jl` package can be utilized to specify which MPI implementation Julia should use, resolving conflicts with default binaries.
- Always check for undefined symbols in error logs to diagnose library loading issues.

## References
- [MPI.jl Configuration Documentation](https://juliaparallel.org/MPI.jl/stable/configuration/)
---

### 2024021042000631_MPI%20Error%20Konvertierung%20Nvidia%20Nemo.md
# Ticket 2024021042000631

 # HPC-Support Ticket: MPI Error Konvertierung Nvidia Nemo

## Keywords
- MPI Error
- SLURM PMI Support
- Apptainer
- NeMo Megatron
- Llama Model Conversion
- Python Script

## Problem Description
The user is attempting to convert a Llama model to the .nemo format using NeMo Megatron. The process involves starting an Apptainer container and running a Python script. However, the user encounters an MPI error related to SLURM's PMI support.

## Root Cause
The error occurs because the application was launched using `srun`, but Open MPI was not built with SLURM's PMI support. This prevents the MPI initialization from completing successfully.

## Error Message
```
The application appears to have been direct launched using "srun",
but OMPI was not built with SLURM's PMI support and therefore cannot
execute. There are several options for building PMI support under
SLURM, depending upon the SLURM version you are using:
...
*** An error occurred in MPI_Init_thread
*** on a NULL communicator
*** MPI_ERRORS_ARE_FATAL (processes in this communicator will now abort,
***    and potentially your MPI job)
[a0705.nhr.fau.de:4048931] Local abort before MPI_INIT completed completed successfully, but am not able to aggregate error messages, and not able to guarantee that all other processes were killed!
```

## Solution
The HPC Admin suggests removing the SLURM variables before the Python call to resolve the issue. This can be done in several ways:

1. Use `apptainer shell --cleanenv` to start the container with a clean environment.
   ```bash
   apptainer shell --cleanenv nemofw-training_23.08.03.sif
   ```

2. Unset the SLURM variables within the container or before starting the container.
   ```bash
   for i in $(env|grep ^SLURM_); do echo "unsetting $i"; unset ${i%=*}; done
   ```

## Additional Notes
- The HPC Admin mentions that a simple `mpirun -np 2 .../IMB-MPI1 pingpong` command ran successfully in the container, indicating that the issue might be specific to the Python script or Nvidia's implementation.
- Various bind-mounts for `libpmi*` from the host did not resolve the issue for the specific Python script.

## Conclusion
The issue can be mitigated by ensuring that the SLURM variables are not present in the environment when running the Python script. This should allow the MPI initialization to proceed without errors.
---

### 2024030742002615_Support%20with%20FenicsX%20on%20Meggie.md
# Ticket 2024030742002615

 # HPC Support Ticket: Support with FenicsX on Meggie

## Keywords
- FenicsX
- Conda
- MPI
- SLURM
- PMI
- Open MPI
- PMIx
- PMI-1
- PMI-2

## Problem
- User installed FenicsX using Conda, which installed its own MPI version.
- The Conda MPI version is incompatible with SLURM's MPI on the cluster.
- Error message indicates Open MPI was not built with SLURM's PMI support.

## Error Message
```
[m0667.rrze.uni-erlangen.de:2013900] OPAL ERROR: Unreachable in file pmix3x_client.c at line 111
[m0667.rrze.uni-erlangen.de:2013901] OPAL ERROR: Unreachable in file pmix3x_client.c at line 111
```

## Root Cause
- Incompatibility between Conda's Open MPI and SLURM's PMI support.

## Solution
- Use the following Conda command to install FenicsX with an external Open MPI version that is compatible with SLURM:
  ```
  conda install -c conda-forge fenics-dolfinx "openmpi=4.1.*=external_*"
  ```
- Alternatively, try running the job with `srun --mpi=pmi2 ...`

## General Learnings
- Conda environments may install their own MPI versions, which can conflict with the cluster's MPI.
- Open MPI needs to be built with SLURM's PMI support to work correctly.
- Conda-forge provides a way to install packages with external library support.
- SLURM's PMI support can be specified using `srun --mpi=pmi2`.

## References
- [Conda-forge Tips and Tricks](https://conda-forge.org/docs/user/tipsandtricks/)
---

### 2025031042003259_Conflicting%20CUDA%20libraries%20with%20the%20module%20openmpi_4.1.6-nvhpc23.7-cuda.md
# Ticket 2025031042003259

 # HPC Support Ticket: Conflicting CUDA Libraries with `openmpi/4.1.6-nvhpc23.7-cuda`

## Issue
- **Subject:** Conflicting CUDA libraries with the module `openmpi/4.1.6-nvhpc23.7-cuda`
- **User:** Experiencing a warning during compilation of a C++17 program that uses MPI and CUDA.
- **Warning:** `/usr/bin/ld: warning: libcudart.so.11.0, needed by //apps/SPACK/0.19.1/opt/linux-almalinux8-zen/gcc-8.5.0/hwloc-2.8.0-bneg6wh22jt37qyr2hghz5vmrdk6txyt/lib/libhwloc.so.15, may conflict with libcudart.so.12`
- **Root Cause:** Version mismatch between CUDA libraries (`libcudart.so.11.0` and `libcudart.so.12`) linked in the executable.

## Investigation
- **User's Findings:**
  - Executable linked against two different versions of `libcudart.so`.
  - CUDA version detected by CMake is CUDA 12.
  - Compilers within the `nvhpc/23.7` module are built for CUDA 12.
  - `mpirun` and `libhwloc.so` are linked against CUDA 11 libraries.

## Solution
- **HPC Admin Response:**
  - Acknowledged the version mismatch in the `openmpi/4.1.6-nvhpc23.7-cuda` module.
  - Suggested rebuilding Open MPI and its dependencies (`hwloc`, etc.) against CUDA 12 to match the NVHPC 23.7 toolchain.
  - Provided a new module `openmpi/4.1.6-nvhpc23.7-cuda12` for testing.

## Command for Rebuilding Open MPI
```bash
/apps/SPACK/0.19.1/bin/spack install openmpi@4.1.6%nvhpc@23.7 fabrics=ucx ^cuda@12-6.1%gcc ^pkgconf%gcc ^ucx +mlx5_dv +dc +rc +ud ~knem +xpmem +gdrcopy +verbs ^pmix@4.1.3%gcc@8.5.0
```

## Lessons Learned
- **Version Mismatch:** Ensure that all libraries and dependencies are built against the same version of CUDA to avoid conflicts.
- **Module Consistency:** When using modules, verify that all components are compatible and linked against the correct versions.
- **User Investigation:** Encourage users to provide detailed investigation reports to help diagnose and resolve issues efficiently.

## Next Steps
- **User:** Test the new module `openmpi/4.1.6-nvhpc23.7-cuda12` and report any further issues.
- **HPC Admin:** Monitor for similar issues and ensure consistency in module versions and dependencies.
---

### 42023477_Anfrage%3A%20Gnuplot%204.2%20auf%20Woody.md
# Ticket 42023477

 # HPC Support Ticket: Request for Gnuplot Update

## Keywords
- Gnuplot
- Version Update
- Woody-Frontnodes
- Syntax Improvement
- Module Installation

## Summary
A user requested an update to a newer version of Gnuplot on the Woody-Frontnodes due to syntax improvements in the newer version.

## Root Cause
- The current version of Gnuplot (4.0) on the Woody-Frontnodes is outdated.
- The user requires a newer version (4.2) for improved syntax and functionality.

## Solution
- HPC Admin installed a new module "gnuplot/4.2.5" to address the user's request.

## General Learnings
- Users may request software updates for improved functionality.
- HPC Admins can resolve such requests by installing newer versions as modules.
- Communication between users and HPC Admins is crucial for addressing software needs.

## Actions Taken
- HPC Admin installed the requested Gnuplot version as a module.

## Follow-Up
- Ensure users are aware of the new module and how to load it.
- Monitor for any further software update requests and handle them similarly.
---

### 2018101142000983_Problem%3A%20Error%20while%20building%20code%20on%20woody.md
# Ticket 2018101142000983

 ```markdown
# HPC Support Ticket Conversation Analysis

## Subject: Problem: Error while building code on woody

### Keywords:
- OS Update (Ubuntu 18.04)
- Intel Compiler Error
- Header File Issue
- CMake Error
- MPI Libraries
- LD_LIBRARY_PATH

### Root Cause:
- The user encountered an error while building code after an OS update to Ubuntu 18.04 on the HPC system "woody."
- The error was related to an undefined identifier `_LIB_VERSION_TYPE` in the Intel Compiler's header file.
- Additionally, there were issues with the Intel 19.0up00 compiler not being able to compile a simple test program due to missing MPI libraries.

### Solution:
- The HPC Admin suggested using an experimental Intel 19.0up00 module, which supposedly fixed the header file issue.
- The user faced further issues with the Intel 19.0up00 compiler due to missing MPI libraries.
- The HPC Admin resolved the issue by setting `LD_LIBRARY_PATH` to 'release_mt' and creating missing symlinks for `libmpi*` under the appropriate directory, similar to the 2018 version.

### General Learnings:
- OS updates can introduce compatibility issues with existing software and compilers.
- Intel Compiler versions may have bugs that are fixed in newer releases.
- Missing MPI libraries can cause compilation errors, and ensuring proper symlinks and `LD_LIBRARY_PATH` settings can resolve these issues.
- Experimental modules may require additional configuration to work correctly.

### Steps Taken:
1. Identified the issue with the Intel Compiler header file after the OS update.
2. Suggested using a newer Intel Compiler version (19.0up00) to resolve the header file issue.
3. Addressed missing MPI libraries by setting `LD_LIBRARY_PATH` and creating necessary symlinks.

### Conclusion:
- The problem was resolved by updating the Intel Compiler version and configuring the environment correctly.
- This conversation highlights the importance of keeping software versions up to date and ensuring proper configuration of libraries and paths.
```
---

### 42154972_xmgrace.md
# Ticket 42154972

 # HPC Support Ticket: xmgrace Issue

## Keywords
- xmgrace
- Path issue
- Module loading
- Re-login
- OpenSuSE
- SLES-AddOns

## Problem Description
- User experienced issues with xmgrace not being available in their path on the HPC system.

## Root Cause
- xmgrace was not available due to a configuration or installation issue on the HPC system.

## Solution
- HPC Admin resolved the issue by making xmgrace available again.
- User was advised to re-login to automatically find the binary.

## General Learnings
- Ensure that necessary software packages are included in the system's configuration.
- Re-login may be required to update the user's environment after changes are made by the admin.
- Communication with the HPC Admin can resolve issues related to software availability.
---

### 42219946_xmgrace%20on%20lima.md
# Ticket 42219946

 # HPC Support Ticket: xmgrace on lima

## Keywords
- xmgrace
- lima
- installation
- frontends

## Problem
- User requested the reinstallation of xmgrace on the lima cluster.

## Root Cause
- xmgrace was not available on the lima frontends.

## Solution
- HPC Admin confirmed that xmgrace has been made available again on the lima frontends.

## General Learning
- Users may request specific software installations or reinstallations.
- HPC Admins can address these requests by ensuring the software is available on the appropriate systems.

## Actions Taken
- HPC Admin verified and confirmed the availability of xmgrace on the lima frontends.

## Documentation for Future Reference
- When users request software installations, verify the availability and ensure the software is accessible on the required systems.
- Communicate the status of the software installation to the user promptly.
---

### 2022062742002737_gcc%20versions%20%3C%3D6.md
# Ticket 2022062742002737

 ```markdown
# HPC Support Ticket: gcc versions <=6

## Keywords
- gcc versions
- CUDA 9
- Compilation error
- gcc 6

## Problem Description
- User encounters a compilation error with CUDA 9 due to unsupported gcc versions later than 6.
- User cannot locate gcc version 6.

## Root Cause
- CUDA 9 requires gcc versions 6 or earlier for compatibility.
- User's environment does not have gcc 6 available.

## Solution
- HPC Admins can assist in locating or installing gcc version 6.
- User should be directed to use a compatible gcc version for CUDA 9 compilation.

## General Learnings
- Ensure compatibility between CUDA versions and gcc versions.
- Provide guidance on locating or installing specific gcc versions.
- Document common compilation issues and their resolutions for future reference.
```
---

### 42100908_Bitte%20um%20Software-Installation%20auf%20memoryhog.md
# Ticket 42100908

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject: Bitte um Software-Installation auf memoryhog

### Keywords:
- Software Installation
- Ubuntu Packages
- sqlite3
- libdbd-sqlite3-perl
- memoryhog

### Summary:
A user requested the installation of specific Ubuntu packages on the memoryhog system.

### Root Cause:
The user required additional software packages (`sqlite3` and `libdbd-sqlite3-perl`) to be installed on the memoryhog system.

### Solution:
The HPC Admins installed the requested packages on the memoryhog system.

### What Can Be Learned:
- Users may request specific software packages for their work.
- HPC Admins can install requested software packages on the system.
- Communication between users and HPC Admins is essential for fulfilling software installation requests.

### Notes:
- The ticket was resolved promptly by the HPC Admins.
- The user provided clear and specific details about the required software packages.
```
---

### 2023021542003737_rome2%20_%20rocm%20_%20MI210.md
# Ticket 2023021542003737

 # HPC Support Ticket: MI210 Visibility and ROCm Update

## Keywords
- MI210
- rome2
- ROCm
- Update
- Visibility

## Problem Description
- The MI210 GPU in the `rome2` system is not visible.
- The user requests an update for ROCm to the latest version, as there have been two newer releases.

## Root Cause
- The MI210 GPU is not being detected or is hidden.
- ROCm software is outdated and requires an update.

## Solution
- Investigate the visibility issue of the MI210 GPU in the `rome2` system.
- Update ROCm to the latest version to ensure compatibility and performance improvements.

## Actions Taken
- HPC Admins to check the configuration and logs of the `rome2` system to identify why the MI210 GPU is not visible.
- HPC Admins to update ROCm to the latest version and verify the installation.

## General Learnings
- Regular updates of software like ROCm are essential for maintaining performance and compatibility.
- Visibility issues with hardware components like GPUs can be caused by various factors, including configuration errors or hardware failures.

## Next Steps
- Confirm the resolution of the MI210 visibility issue.
- Verify the successful update of ROCm and ensure it is functioning correctly.
- Document any specific steps taken for future reference.
---

### 2024092542000804_Warning%20libaio%20DeepSpeed.md
# Ticket 2024092542000804

 ```markdown
# HPC-Support Ticket: Warning libaio DeepSpeed

## Keywords
- libaio
- DeepSpeed
- conda
- CUTLASS_PATH
- async_io
- warnings

## Problem Description
- User encountered warnings related to `libaio` and `CUTLASS_PATH` while using DeepSpeed.
- Warnings indicated that `libaio-devel` package should be installed via `yum`.
- Warnings also suggested setting `CFLAGS` and `LDFLAGS` environment variables if `libaio` is already installed.
- Similar warnings appeared during Stable Diffusion Training.

## Root Cause
- Missing `libaio` package and unset `CUTLASS_PATH` environment variable.

## Solution
- Install `libaio` using conda:
  ```bash
  conda config --add channels conda-forge
  conda config --set channel_priority strict
  conda install libaio
  ```
- Set the `CUTLASS_PATH` environment variable to the appropriate repository path.

## Outcome
- The warnings disappeared after installing `libaio` and setting `CUTLASS_PATH`.
- No direct impact on training results was observed.

## Notes
- HPC Admins discussed whether to install `libaio` as a package in the cluster OS.
- The ticket was closed after the user confirmed the resolution.
```
---

### 42321909_A%20small%20glitch%20in%20LD_LIBRARY_PATH%20for%20enabling%20%20C%2B%2B11%20in%20intel%20compilers.md
# Ticket 42321909

 # HPC Support Ticket: LD_LIBRARY_PATH Glitch with GCC/4.8 Module

## Keywords
- LD_LIBRARY_PATH
- GCC/4.8
- Intel Compilers
- C++11
- 32-bit libraries
- 64-bit libraries
- Linker issues
- Autotools

## Problem Description
When loading the GCC/4.8 module required to enable C++11 in Intel compilers, the 32-bit libraries precede the 64-bit libraries in the `LD_LIBRARY_PATH`. This causes the linker to link 32-bit libraries, leading to issues where the autotools disable the `icpc` compiler, citing that it cannot produce executables.

## Root Cause
The order of libraries in the `LD_LIBRARY_PATH` is incorrect, with 32-bit libraries preceding 64-bit libraries.

## User Workaround
Manually editing the `LD_LIBRARY_PATH` after loading the Intel compiler and GCC/4.8 modules to ensure 64-bit libraries precede 32-bit libraries.

### Before
```sh
/apps/gcc/gcc-4.8.1-x86_64/lib:/apps/gcc/gcc-4.8.1-x86_64/lib64:/apps/intel/ComposerXE/composer_xe_2011_sp1.13.367/compiler/lib/intel64:/apps/intel/ComposerXE/composer_xe_2011_sp1.13.367/mkl/lib/intel64:/apps/intel/mpi/4.1.3.048/intel64/lib:/apps/intel/mpi/4.1.3.048/mic/lib::/home/hpc/mptf/mptf21/Prog/lib
```

### After
```sh
/apps/gcc/gcc-4.8.1-x86_64/lib64:/apps/intel/ComposerXE/composer_xe_2011_sp1.13.367/compiler/lib/intel64:/apps/intel/ComposerXE/composer_xe_2011_sp1.13.367/mkl/lib/intel64:/apps/intel/mpi/4.1.3.048/intel64/lib:/apps/intel/mpi/4.1.3.048/mic/lib::/home/hpc/mptf/mptf21/Prog/lib
```

## Solution
HPC Admins changed the order in the GCC/4.8 module to ensure 64-bit libraries precede 32-bit libraries.

## Lessons Learned
- The order of libraries in the `LD_LIBRARY_PATH` is crucial for proper linking.
- Manual intervention can temporarily resolve issues, but a permanent fix should be implemented in the module configuration.
- Proper configuration of modules is essential to avoid linker issues and ensure compatibility with other tools.
---

### 2024021842000331_Installation%20of%20openmpi%204.1.2%20with%20gcc%2011.2.0%20with%20user-spack%200.19.1.md
# Ticket 2024021842000331

 # HPC Support Ticket: Installation of OpenMPI with Specific Compiler

## Keywords
- OpenMPI
- GCC
- Spack
- Deal.II
- Module

## Problem
- User needs to install `dealii@9.4.0` using `user-spack@0.19.1`.
- `dealii@9.4.0` requires `openmpi@4.1.2` compiled with `gcc@11.2.0`.
- Current OpenMPI installation is not configured with `gcc@11.2.0`.

## Solution
- HPC Admin informed the user about the existing module `openmpi/4.1.2-gcc11.2.0` on the system.
- User was advised to try the installation using the available module.

## General Learnings
- Always check for existing modules that meet the required specifications before requesting new installations.
- Communication about available resources can save time and effort for both users and admins.

## Follow-up
- Confirm if the existing module resolves the user's issue.
- If not, further investigation into the compatibility of the module with `user-spack@0.19.1` may be required.
---

### 2018051642001911_Anfrage.md
# Ticket 2018051642001911

 # HPC Support Ticket Conversation Summary

## Keywords
- R-Packages
- NoMachine
- File Transfer
- RRZE Clusters (Woody, TinyFat, TinyEth)
- Modulsystem
- Imputation
- Individual Participant Data Meta-Analysis

## General Learnings
- **R-Packages Installation**: Users can install R-packages as normal users. A guide is available at [R-Bloggers](https://www.r-bloggers.com/installing-r-packages/).
- **RRZE Clusters**: R is installed on Woody, TinyFat, and TinyEth clusters. Overview and modulsystem information available at [RRZE Anleitungen](https://www.anleitungen.rrze.fau.de/hpc/).
- **File Transfer**: NoMachine client allows sharing directories between local PC and remote host.
- **Systemweit Installation**: R-packages available in Microsoft R-Open Repository can be installed system-wide by HPC Admins.

## Root Cause of the Problem
- User needed to install specific R-packages and transfer local files to the HPC cluster.

## Solution
- **R-Packages**: HPC Admins installed the required R-packages system-wide.
- **File Transfer**: User was guided to use NoMachine to share directories and transfer files.

## Documentation for Support Employees
### R-Packages Installation
Users can install R-packages as normal users following the guide at [R-Bloggers](https://www.r-bloggers.com/installing-r-packages/). For system-wide installation, HPC Admins can install packages available in the Microsoft R-Open Repository.

### File Transfer using NoMachine
1. Open NoMachine client.
2. Go to the NX-Client menu (click on the "Eselsohr" icon in the top right corner).
3. Select the icon to share directories between the local PC and the remote host.
4. Make the directory public to avoid connection errors.

### RRZE Clusters and Modulsystem
- **Woody**: Fast but few cores per node, 8GB.
- **TinyFat**: High memory.
- **TinyEth**: Allows single-core jobs like Woody.
- Modulsystem information available at [RRZE Anleitungen](https://www.anleitungen.rrze.fau.de/hpc/environment/).

This documentation can be used to solve similar issues in the future.
---

### 42343990_Intel%20compilers.md
# Ticket 42343990

 ```markdown
# HPC Support Ticket: Intel Compilers License Issue

## Keywords
- Intel compilers
- License error
- FCompL
- FLEXlm
- Module loading
- Environment variables

## Problem Description
- **User Issue**: Intel compilers not working due to license error.
- **Error Message**: `Error: A license for FCompL is not available (-8,130).`
- **Affected Versions**: Intel 15.0up02

## Ticket Conversation Summary
- **Initial Report**: User reported license error when trying to use Intel compilers.
- **Admin Response**: Admin could not reproduce the issue and requested more details.
- **User Follow-up**: User provided additional details, including loaded modules and license file paths.

## Root Cause
- **License Issue**: The Intel compiler was unable to check out a FLEXlm license, indicating a potential issue with the license server or configuration.

## Solution
- **Admin Actions**: Admin verified that the issue was not reproducible on their end and suggested checking the environment variables.
- **User Actions**: User provided detailed information about the loaded modules and license file paths.

## Lessons Learned
- **License Configuration**: Ensure that the license server is correctly configured and accessible.
- **Environment Variables**: Check the environment variables to ensure they are correctly set for the Intel compilers.
- **Module Loading**: Verify that the correct modules are loaded and that there are no conflicts.

## Next Steps
- **Further Diagnostics**: If the issue persists, further diagnostics on the license server and environment configuration may be necessary.
- **User Support**: Provide additional guidance on checking and setting environment variables for the Intel compilers.
```
---

### 2022110742002729_AMBER%20MPI%20auf%20ALEX.md
# Ticket 2022110742002729

 # HPC Support Ticket: AMBER MPI auf ALEX

## Keywords
- AMBER
- MPI
- GPU
- SLURM
- pmemd.cuda
- mpirun
- A40
- A100
- Benchmark

## Problem
- User encountered an error when trying to run a parallel version of AMBER using MPI on the HPC system.
- Error message: `mpirun: command not found`

## Root Cause
- The MPI version of AMBER was not correctly loaded.
- The submit script was missing the correct module load command and the correct binary name for the MPI version of AMBER.

## Solution
- Load the correct AMBER module with MPI binaries: `amber/20p12-at21p11-openmpi-gnu-cuda11.5`.
- Use the correct binary name for the MPI version of AMBER: `pmemd.cuda_SPFP.MPI`.
- Remove unnecessary SLURM directives (`#SBATCH --ntasks=16` and `#SBATCH --partition=a40`).

## General Learnings
- Ensure the correct module is loaded for the software version being used.
- Use the correct binary names as specified in the module documentation.
- SLURM directives should be adjusted based on the specific requirements of the job and the HPC system configuration.
- Benchmarking results can help in deciding the appropriate hardware for simulations.

## Additional Notes
- For AMBER22, there is no MPI version available yet.
- Using multiple GPUs for a single AMBER calculation is generally not beneficial.
- The system allows starting production runs even if the application is still under review.
---

### 2024112942004576_Lapack%20and%20intelmpi.md
# Ticket 2024112942004576

 # HPC Support Ticket: Lapack and Intel MPI

## Keywords
- LQCD simulation software
- Lapack
- Intel MPI
- Spack
- GCC
- Intel compilers
- MKL
- Module load
- Compiler options

## Problem
- User requires specific modules (`lapack-3.10.0` and `mpi/intel-mpi-2019`) for LQCD simulation software.
- Modules are unavailable, and user attempts to install via Spack but encounters issues.
- Using available `intelmpi/2021.10.0` module results in a compiler error (`g++: Fehler: unbekannte Kommandozeilenoption »-qopt-zmm-usage=high«`).

## Root Cause
- The `-qopt-zmm-usage=high` option is specific to Intel compilers, not supported by GCC.
- The software's Makefile is configured for older modules and Intel-specific options.

## Solution
- Load the appropriate modules for Intel compilers and MKL:
  ```bash
  module load intel mkl intelmpi
  ```
- Define the compilers explicitly if needed:
  ```bash
  CC=icc CXX=icpc FC=ifort
  ```
- Use Intel's MKL as a drop-in replacement for Lapack.

## General Learnings
- Ensure compatibility between compilers and MPI libraries.
- Intel MKL can be used as a replacement for Lapack.
- Be aware of compiler-specific options and ensure the correct compiler is loaded.
- Older software may require adjustments to work with newer modules and compilers.

## Additional Notes
- The `intel` module contains both new (LLVM-based) and legacy Intel compilers.
- Only the legacy compilers (`icc`, `icpc`, `ifort`) support the `-qopt-zmm-usage=high` option.
---

### 2016052442001926_gcc%20compatible%20with%20openmpi.md
# Ticket 2016052442001926

 # HPC Support Ticket Conversation Summary

## Subject: gcc compatible with openmpi

### Keywords:
- gcc
- openmpi
- Intel Compiler
- Intel MPI
- LAMMPS
- Atomistica
- Compilation Issues
- Emmy Cluster
- Operating System Upgrade

### General Learnings:
- The user is trying to compile LAMMPS with Atomistica on the Emmy cluster.
- Initial attempts to compile with gcc (4.9.2) and OpenMPI (1.6.5-gcc) resulted in compatibility issues.
- HPC Admins recommend using Intel Compiler and Intel MPI for better compatibility.
- The user encountered issues with setting up an HPC account through the IDM portal.
- A major operating system upgrade on Emmy is scheduled, which may affect debugging efforts.
- The user requested a meeting to discuss the compilation issues in person.

### Root Cause of the Problem:
- Compatibility issues between gcc and OpenMPI versions.
- Difficulty in setting up an HPC account through the IDM portal.

### Solution:
- HPC Admins recommend using Intel Compiler and Intel MPI for better compatibility.
- The user should wait for the operating system upgrade before further debugging.
- A meeting is scheduled to discuss the issues in person.

### Detailed Steps:
1. **Initial Compilation Attempt:**
   - User tried to compile LAMMPS with Atomistica using gcc (4.9.2) and OpenMPI (1.6.5-gcc).
   - Compatibility issues were encountered.

2. **HPC Admin Recommendation:**
   - HPC Admins recommend using Intel Compiler and Intel MPI.
   - Sample programs were compiled successfully using both "gcc/4.9.2 openmpi/1.6.5-gcc" and "gcc/4.9.2 openmpi/1.8.3-gcc".

3. **Account Setup Issues:**
   - User encountered issues with setting up an HPC account through the IDM portal.
   - HPC Admins provided guidance on resetting the password.

4. **Operating System Upgrade:**
   - A major operating system upgrade on Emmy is scheduled, which may affect debugging efforts.
   - User is advised to wait for the upgrade before further debugging.

5. **Meeting Request:**
   - User requested a meeting to discuss the compilation issues in person.
   - Meeting is scheduled to discuss the issues and potential solutions.

### Additional Notes:
- The user provided detailed steps for compiling Atomistica and LAMMPS with Intel Compiler and Intel MPI.
- The user mentioned that Atomistica can be compiled without issues using the Intel Tool Chain.

This summary provides a concise overview of the conversation and the steps taken to address the user's issues. It can be used as a reference for future support tickets with similar problems.
---

### 42178933_meep%20on%20lima.md
# Ticket 42178933

 # HPC Support Ticket: Meep Installation on Lima

## Keywords
- Meep
- Meep-mpi
- Lima
- CentOS
- Dependencies
- Guile
- libhdf5
- Compilation

## Problem Description
A user is attempting to install Meep-mpi on the Lima cluster but is encountering difficulties due to the numerous dependencies required for the installation.

## Root Cause
The complexity of installing Meep-mpi arises from the need to manually handle multiple dependencies such as Guile and libhdf5.

## User Request
- Availability of a CentOS package for Meep or its dependencies.
- Information on other users who have successfully installed Meep on Lima.

## Solution
- **CentOS Package**: Check if there are pre-built CentOS packages for Meep or its dependencies.
- **User Compilation Techniques**: Look for other users who have successfully installed Meep on Lima and share their compilation techniques.

## General Learning
- **Dependency Management**: Installing software with multiple dependencies can be challenging. Pre-built packages or shared compilation techniques can simplify the process.
- **Community Support**: Leveraging the experience of other users can be beneficial for complex installations.

## Next Steps
- HPC Admins should investigate the availability of CentOS packages for Meep and its dependencies.
- If no packages are available, HPC Admins should check with other users or the 2nd Level Support team for successful compilation methods.

## Notes
- This ticket highlights the importance of documenting and sharing successful installation methods for complex software.
- Regular updates on available packages and dependencies can help users avoid installation difficulties.
---

### 2017052342002121_Installation%20von%20Libboost%20auf%20dem%20hpc%20_%20woodycap.md
# Ticket 2017052342002121

 ```markdown
# HPC Support Ticket: Installation von Libboost auf dem HPC / woodycap

## Keywords
- Libboost
- Program-options
- Installation
- HPC
- Woodycap
- Simulationsprogramme

## Problem
- User requires the installation of `libboost-program-options` for their simulation program on the HPC system (woodycap).

## Conversation Summary
- User requests the installation of `libboost-program-options` and asks for the location where it can be found.
- HPC Admin acknowledges the request.

## Solution
- HPC Admin will install the required library and provide the location where it can be found.

## General Learnings
- Users may require specific libraries for their simulation programs.
- HPC Admins need to install requested libraries and inform users about their location.
- Effective communication between users and HPC Admins is crucial for resolving such requests.
```
---

### 2023031342000269_R%20not%20available%20on%20Fritz%3F.md
# Ticket 2023031342000269

 # HPC-Support Ticket Conversation: R Not Available on Fritz

## Keywords
- R installation
- Module conflict
- MKL
- Conda
- R packages
- GLIBC version
- Binary installation

## Summary
A user encountered issues with loading the R module on the Fritz HPC system. The conversation covers the resolution of module conflicts, installation of R packages, and handling GLIBC version issues.

## Problem
- User unable to load R module.
- Module conflict with MKL.
- Issues with installing R packages due to dependencies and compiler errors.
- GLIBC version requirement for an R package.

## Solutions
- **Module Conflict**: Unload the MKL module to resolve the conflict with the R module.
  ```bash
  module unload mkl
  module load r/4.2.2-conda
  ```
- **R Packages Installation**: Use binary installation for packages with dependency issues.
  ```r
  binary.install("package_name")
  ```
- **GLIBC Version**: No newer GLIBC version available on Fritz. User resolved the issue by using binary installation for the package.

## General Learnings
- **Module Conflicts**: Understand that some modules may have internal dependencies that conflict with explicitly loaded modules.
- **R Package Installation**: Issues with package dependencies and compiler errors can often be resolved by using binary installations.
- **GLIBC Version**: Be aware of the GLIBC version requirements for certain packages and the limitations of the HPC system.

## Root Cause
- Module conflict between R and MKL due to internal MKL installation in R.
- Compiler errors during R package installation due to missing dependencies or permissions.
- GLIBC version requirement for an R package not met by the HPC system.

## Resolution
- Unload conflicting modules.
- Use binary installation for problematic R packages.
- No solution for GLIBC version issue; use binary installation as a workaround.

## Documentation for Support Employees
- **Module Conflicts**: Always check for internal dependencies in modules and unload conflicting modules if necessary.
- **R Package Installation**: For issues with dependencies or compiler errors, recommend using binary installation.
- **GLIBC Version**: Inform users about the GLIBC version limitations and suggest workarounds like binary installation.

## Conclusion
The user was able to resolve the module conflict and install the required R packages by following the suggested solutions. The GLIBC version issue was addressed by using a binary installation of the package.
---

### 2015101942002589_version%20GLIBC_2.14%20not%20found.md
# Ticket 2015101942002589

 # HPC Support Ticket: GLIBC Version Not Found

## Keywords
- GLIBC_2.14
- libc
- version not found
- woodycap1-Server
- libhessio.so

## Problem Description
The user encountered an error when running a program on the woodycap1-Server:
```
"/lib64/libc.so.6: version `GLIBC_2.14' not found (required by /home/hpc/caph/mpp227/software/hessioxxx/lib/libhessio.so)"
```
The user requested an update of the libc to the required version.

## Root Cause
The program requires GLIBC version 2.14, which is not available on the woodycap1-Server.

## Solution
The HPC Admin responded that updating the libc is not feasible as it is an integral part of the system.

## General Learning
- Updating system libraries like libc can have significant impacts on the system and may not be feasible.
- Users should ensure their software is compatible with the available system libraries.
- Alternative solutions such as containerization or using a different environment may be explored for such dependencies.
---

### 2022071242003879_RRZE%20Testcluster%3A%20Linking%20error%20beim%20Verwenden%20der%20Intel%20Compiler.md
# Ticket 2022071242003879

 # HPC Support Ticket: Linking Error with Intel Compiler

## Keywords
- Intel Compiler
- Linking Error
- icc -v
- Version Information
- Module Load

## Problem Description
The user encountered a linking error when trying to use the Intel Compiler after a module update in the test cluster. The error message indicated an undefined reference to `main`.

## Root Cause
The user was attempting to get the version information of the Intel Compiler using `icc -v`, which in newer versions attempts to create an executable and fails due to the absence of a `main` function.

## Solution
The correct command to get the version information of the Intel Compiler is `icc --version`.

## Lessons Learned
- The `icc -v` command behavior has changed in newer versions and may attempt to create an executable, leading to linking errors if no `main` function is provided.
- Always refer to the latest documentation for command usage.
- Use `icc --version` to get the version information of the Intel Compiler.

## Additional Information
- The user was loading multiple modules, including `cmake`, `cuda`, `python/3.8-anaconda`, `likwid/5.2.1`, `intel/2020.2`, and `gcc/10.2.0`.
- The issue was not related to module incompatibilities but rather to the incorrect usage of the `icc -v` command.

## Support Team Involved
- HPC Admins
- 2nd Level Support Team
---

### 2018042642001457_cmake%20auf%20woody.md
# Ticket 2018042642001457

 # HPC Support Ticket: cmake auf woody

## Keywords
- cmake
- woody
- installation
- external packages
- update

## Problem
- User requires a more recent version of cmake on the woody cluster to support external packages.

## Solution
- HPC Admin confirmed the installation of an updated version of cmake (3.11.1) on the woody cluster.

## Lessons Learned
- Users may need updated software versions to support external packages.
- HPC Admin can install and provide newer software versions upon request.
- Communication between users and HPC Admin is essential for addressing software requirements.

## Actions Taken
- HPC Admin installed cmake/3.11.1 on the woody cluster.

## Notes
- The installed version of cmake (3.11.1) is noted as untested.
- The request was handled promptly by the HPC Admin.
---

### 2018032642001422_GCC%207%3F.md
# Ticket 2018032642001422

 # HPC Support Ticket: GCC 7?

## Keywords
- GCC Compiler
- HPC Woody Cluster
- Module Availability

## Problem
- User inquired about the availability of newer GCC compiler versions (up to 7.x) on the HPC Woody Cluster, as they only saw version 5.4.

## Root Cause
- User was unaware of the availability of newer GCC versions as modules.

## Solution
- HPC Admin informed the user that modules "gcc/6.2.0" and "gcc/7.2.0" are available on the cluster.

## What Can Be Learned
- Always check the available modules on the HPC cluster for the latest software versions.
- Communicate with HPC Admins for updates on software availability.

## General Information
- The HPC Woody Cluster provides multiple versions of the GCC compiler through modules.
- Users should be aware of the module system to access the latest software versions.

## Roles Involved
- **HPC Admins**: Provided information on available GCC modules.
- **User**: Inquired about GCC versions and acknowledged the information provided.

## Conclusion
- Effective communication and awareness of the module system can resolve queries about software availability on the HPC cluster.
---

### 2021120742002274_module%20R%20-%20packages%20fasterize%20und%20chron.md
# Ticket 2021120742002274

 # HPC Support Ticket: R Packages "fasterize" and "chron"

## Keywords
- R packages
- fasterize
- chron
- woody
- saturn
- user library
- workaround

## Problem Description
- User's R scripts in the working group (HPC ID: gwgi) rely on the "fasterize" and "chron" packages.
- These packages were not installed on the woody cores.
- A local user library on saturn was set up as a workaround, but it stopped functioning after about a week.

## Root Cause
- The exact cause of the workaround failure is not specified, but it is implied that the local user library setup became ineffective.

## Solution
- HPC Admins added the "fasterize" and "chron" packages to the R installations on woody and TinyFat.

## Lessons Learned
- Local user libraries can be a temporary solution for missing packages, but they may not be reliable in the long term.
- Requesting the installation of necessary packages through HPC support can provide a more stable solution.
- Communication with HPC support can resolve issues related to missing software dependencies efficiently.

## Actions Taken
- HPC Admins installed the requested R packages on the relevant systems.

## Follow-Up
- No further follow-up was mentioned in the ticket.

## References
- HPC Services, Friedrich-Alexander-Universitaet Erlangen-Nuernberg
- Regionales RechenZentrum Erlangen (RRZE)

---

This documentation can be used to address similar issues related to missing R packages in the future.
---

