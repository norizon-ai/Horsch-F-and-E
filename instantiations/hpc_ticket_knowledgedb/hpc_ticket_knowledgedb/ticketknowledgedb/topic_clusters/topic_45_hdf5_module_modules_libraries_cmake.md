# Topic 45: hdf5_module_modules_libraries_cmake

Number of tickets: 8

## Tickets in this topic:

### 2019042942002501_Problem%20with%20the%20Emmy%20cluster.md
# Ticket 2019042942002501

 ```markdown
# HPC Support Ticket: Problem with the Emmy Cluster

## Keywords
- HDF5 module
- File accessibility
- Unable to open file
- OpenMP
- Thread safety

## Problem Description
The user encountered an error when using the HDF5 module on the Emmy cluster. The error message indicated an issue with file accessibility and the inability to open a file.

## Root Cause
- The user was not loading the same HDF5 module at runtime as was used during compilation.
- The HDF5 library used was not thread-safe by default, which could cause issues when using OpenMP.

## Solution
1. **Load the Same Modules at Runtime**: Ensure that the same modules used during compilation are loaded at runtime. This includes the HDF5 module and all other dynamically linked modules.
2. **Check OpenMP Usage**: The HDF5 library may not be thread-safe by default. Try running the program without OpenMP to see if the problem persists.
3. **Recompile HDF5 with Thread Safety**: If OpenMP is necessary, consider recompiling the HDF5 library with thread safety enabled. This can be done in the user's home directory.
4. **Alternative Filesystems**: Try writing the output to a different filesystem, such as `$FASTTMP` or `$WORK`, to rule out filesystem-specific issues.

## General Lessons Learned
- Always load the same modules at runtime as were used during compilation to avoid linking issues.
- Be aware of the thread safety of libraries when using OpenMP.
- Consider alternative filesystems for output to rule out filesystem-specific issues.

## Follow-Up
The user was advised to try the suggested workarounds and report back if the problem persisted. The HPC Admin offered to adapt the HDF5 module if necessary.
```
---

### 2024062842002197_HDF5.md
# Ticket 2024062842002197

 # HPC Support Ticket: HDF5 Command Line Tools

## Keywords
- HDF5
- Command Line Tools
- Fritz Cluster
- Lustre File System
- Modules
- Spack

## Problem
- User wants to use HDF5 command line tools on the Fritz cluster in the /lustre file system.
- User believes the tools are not installed.

## Solution
- HPC Admin instructs the user to load the desired HDF5 module using the `module` command.
- Example commands provided:
  ```sh
  $ module avail hdf5
  $ module load hdf5/1.10.7-ompi-intel
  $ h5clear --version
  ```
- Additional versions of HDF5 are available by loading the `user-spack` module.
- If the provided versions and tools are insufficient, the user can build their own version using Spack.

## Additional Information
- Spack documentation link: [Spack Documentation](https://doc.nhr.fau.de/apps/spack/)
- Contact information for further support: `support-hpc@fau.de`

## General Learnings
- Users should check available modules before assuming tools are not installed.
- Loading the appropriate module can provide access to the required tools.
- Spack can be used to build custom versions of software if needed.
---

### 2022122742000254_hdf5.md
# Ticket 2022122742000254

 # HPC Support Ticket: HDF5 Performance Issue

## Keywords
- HDF5
- Serial HDF5
- Parallel HDF5
- Lustre Filesystem
- Intel MPI
- OpenMPI
- Performance

## Problem
- User reported slow write performance in HDF5 files.
- Previous experience at another site (Juelich) showed differences between serial and parallel HDF5.

## Root Cause
- The user was experiencing slow write performance due to the choice between serial and parallel HDF5.

## Solution
- The HPC Admin informed the user about the available HDF5 modules on Fritz:
  - `hdf5/1.10.7-impi-intel` (built with Intel MPI)
  - `hdf5/1.10.7-ompi-intel` (built with OpenMPI)
  - `hdf5/1.10.7-intel` (built without MPI)
- The user was advised to choose between serial and parallel HDF5 modules based on their needs.

## What Can Be Learned
- Different HDF5 modules are available on Fritz, including those built with Intel MPI, OpenMPI, and without MPI.
- The choice between serial and parallel HDF5 can significantly impact performance.
- Users should be aware of the available modules and their configurations to optimize performance for their specific use cases.

## Actions Taken
- The HPC Admin provided detailed information about the available HDF5 modules and their configurations.
- The user acknowledged the information and found it helpful.

## Future Reference
- For similar performance issues with HDF5, check the configuration of the HDF5 modules being used.
- Advise users to consider the differences between serial and parallel HDF5 for optimal performance.
---

### 2022092242001858_Library%20Issues%20-%20WRF%20Installation.md
# Ticket 2022092242001858

 # HPC Support Ticket: Library Issues - WRF Installation

## Keywords
- WRF Installation
- HDF5 Libraries
- Missing Fortran Libraries
- Intel Compilers
- SPACK
- Meggie Cluster

## Problem Description
Users from the climate group at the Institute of Geography encountered issues while installing WRF on the Meggie cluster. The error messages indicated that the Fortran libraries `-lhdf5_hl_fortran` and `-lhdf5_fortran` were missing. The users checked the specified SPACK directories but could not locate the required libraries.

## Root Cause
The HDF5 libraries available on Meggie did not include the necessary Fortran support, causing the compilation of WRF to fail.

## Solution
The HPC Admins recompiled HDF5 using Intel compilers to ensure Fortran support was included. New versions of HDF5 (`hdf5/1.12.2-intel-impi` and `hdf5/1.12.2-intel-ompi`) were made available on Meggie, resolving the issue.

## Lessons Learned
- Ensure that the required libraries include all necessary components (e.g., Fortran support) before attempting to compile software.
- Recompiling libraries with different compilers (e.g., Intel) can resolve missing library issues.
- Communication with colleagues on other clusters (e.g., Fritz) can provide insights into potential solutions.

## Follow-up Actions
- Verify that the new HDF5 libraries resolve the compilation issues for WRF.
- Update documentation to reflect the availability of the new HDF5 versions with Fortran support.
---

### 2022012642003158_Early-Fritz%20%22Florian%20Goth%22%20_%20lo50beco.md
# Ticket 2022012642003158

 # HPC-Support Ticket Conversation Summary

## Subject
Early-Fritz "Florian Goth" / lo50beco / HDF5 and C++20 Compiler Issues

## Key Points

- **User Request**: Early-Fritz access for single-node throughput until more Infiniband HCAs arrive.
- **Required Software**: C++20 compiler, libhdf5, lapack, cmake, Fortran compiler.
- **Application**: MARQOV framework for massively parallel simulation via Markov Chain Monte Carlo (MCMC) techniques.
- **Issues**:
  - HDF5 libraries without C++ support.
  - CMake problem with HTTPS downloads.
  - Wallclock timelimit confusion in the singlenode-Queue.

## Detailed Issues and Solutions

### HDF5 Libraries without C++ Support
- **Problem**: HDF5 libraries on Fritz were compiled without C++ support.
- **Solution**: HPC Admin built new HDF5 modules with C++ support.

### CMake Problem with HTTPS Downloads
- **Problem**: CMake failed to download HDF5 due to "Unsupported protocol" error with HTTPS.
- **Solution**:
  - User provided a minimal working example (MWE) to reproduce the issue.
  - HPC Admin identified that Spack's default cmake build did not include openssl support.
  - A new cmake module with `+openssl +ownlibs` was installed on Alex and Fritz.

### Wallclock Timelimit Confusion
- **Problem**: Jobs with a 1-day timelimit were not starting due to scheduled downtime.
- **Solution**: HPC Admin confirmed that the timelimit is normally 24 hours but was temporarily reduced due to maintenance.

## Additional Notes
- **User Feedback**: The new HDF5 module resolved the C++ support issue, and the cmake problem was fixed with the updated cmake module.
- **HPC Admin Actions**: Provided detailed explanations and solutions for each issue, ensuring smooth operation for the user.

## Conclusion
The issues with HDF5 libraries, CMake HTTPS downloads, and wallclock timelimit were successfully addressed by the HPC Admin team, ensuring the user could proceed with their work on the Fritz cluster.
---

### 2022012142001089_Early-Fritz%20%22Tobias%20Schikarski%22%20_%20iwmv000h.md
# Ticket 2022012142001089

 ```markdown
# HPC Support Ticket Conversation Summary

## Subject: Early-Fritz "Tobias Schikarski" / iwmv000h

### Keywords:
- HPC
- Fritz Cluster
- Meggie Cluster
- FASTEST
- HDF5
- Intel Compiler
- Performance
- Visualization
- Spack
- LIKWID
- SSE
- AVX
- AVX2
- AVX512

### General Learnings:
- **Module Naming Conventions**: Fritz/Alex uses a new module naming convention different from the previous RRZE standard.
- **HDF5 Module**: The HDF5 module on Fritz uses `HDF5_ROOT` instead of `HDF5_BASE` and does not include `HDF5_F90_LIB`, `HDF5_INC`, `HDF5_LIB`.
- **Compiler Flags**: Using `-Ofast -xHOST -qopt-zmm-usage=high` instead of `-O3` can potentially improve performance by 10-20%.
- **Performance Metrics**: LIKWID can be used to monitor performance metrics such as memory bandwidth and FLOPS.
- **Visualization**: Visualization tools like Paraview and Tecplot are recommended for flow data visualization.

### Root Causes and Solutions:
- **HDF5 Module Issue**: The HDF5 module on Fritz does not include certain paths (`HDF5_F90_LIB`, `HDF5_INC`, `HDF5_LIB`) required for compilation.
  - **Solution**: Adapt the Makefile to use `HDF5_ROOT` and other available paths.
- **Performance Optimization**: The application was not utilizing AVX/AVX2/AVX512 instructions.
  - **Solution**: Use `-Ofast -xHOST -qopt-zmm-usage=high` compiler flags to enable these instructions.
- **Performance Comparison**: The performance of FASTEST on Fritz was comparable to Meggie with a slight improvement.
  - **Solution**: Further optimization and testing are required to fully utilize the new hardware capabilities.

### Additional Notes:
- **Documentation**: The documentation for the Fritz cluster is still under development.
- **Visualization**: The user prefers to use Matlab for visualization.
- **Testing**: The user is willing to test further optimizations and provide feedback.
```
---

### 2021021742003237_Softwareanfrage%3A%20hdf5-tools.md
# Ticket 2021021742003237

 # HPC Support Ticket: Software Request for hdf5-tools

## Keywords
- Software Installation
- hdf5-tools
- Ubuntu Package
- Login Nodes

## Summary
A user requested the installation of the `hdf5-tools` package on the HPC cluster's login nodes. The package contains command-line tools for working with HDF5 files and is available in the official Ubuntu package sources.

## Root Cause
The user needed command-line tools to manage HDF5 files, which were only required on the login nodes.

## Solution
The HPC Admin installed the `hdf5-tools` package on the specified login node (woody3).

## Lessons Learned
- Users may request specific software packages for managing data files.
- Software installation requests should specify the nodes where the software is needed.
- HPC Admins can install packages from official Ubuntu repositories to meet user requirements.

## Follow-up Actions
- Ensure that the installed software is functioning correctly on the login nodes.
- Document the installation process for future reference.
- Monitor for any additional software requests from users.
---

### 2022052342002201_Kompilierungsfehler%20Module%20hdf5%20Fritz.md
# Ticket 2022052342002201

 # HPC Support Ticket: Kompilierungsfehler Module hdf5

## Keywords
- h5fc command
- Kompilierungsfehler
- hdf5 module
- ifort
- gfortran
- Fritz Cluster
- Meggie Cluster
- Unexpected EOF

## Problem Description
User encountered a compilation error when trying to compile a code using the `h5fc` command on the Fritz Cluster, which worked fine on the Meggie Cluster. The error message indicated an "Unexpected EOF" when reading the `hdf5.mod` file.

## Root Cause
The `hdf5` compiler wrapper was internally using `gfortran` instead of `ifort`, causing the compilation error.

## Solution
The HPC Admin fixed the issue by ensuring that the `hdf5` compiler wrapper uses `ifort` internally for both `hdf5/1.10.7-impi-intel` and `hdf5/1.10.7-ompi-intel` modules.

## Steps Taken
1. User reported the compilation error with the `h5fc` command.
2. HPC Admin requested the list of loaded modules and the exact command used for compilation.
3. User provided the details and mentioned a workaround using `ifort` directly.
4. HPC Admin identified the issue with the `hdf5` compiler wrapper using `gfortran` instead of `ifort`.
5. HPC Admin fixed the issue by ensuring the wrapper uses `ifort`.
6. The issue was resolved, and the workaround was no longer necessary.

## Lessons Learned
- Ensure that the correct compiler is used by the module wrappers.
- Providing detailed information about loaded modules and commands helps in diagnosing the issue.
- Workarounds can be useful temporarily, but fixing the root cause is essential for long-term stability.
---

