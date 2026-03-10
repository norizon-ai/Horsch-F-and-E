# Topic 39: fortran_compiler_intel_module_subroutine

Number of tickets: 9

## Tickets in this topic:

### 2022111442002181_Coupling%20Abaqus%20with%20Fortran%20subroutines%20for%20advanced%20Finite%20Element%20Method%20simu.md
# Ticket 2022111442002181

 # HPC Support Ticket: Coupling Abaqus with Fortran Subroutines

## Keywords
- Abaqus
- Fortran subroutines
- Intel compiler
- Module loading
- Advanced simulations

## Problem
- User needs to upgrade Abaqus installation to support Fortran subroutines for advanced simulations.
- Current Abaqus installation does not support user subroutines.

## Root Cause
- Missing Intel module load required for Abaqus to support Fortran subroutines.

## Solution
- Load the Intel module in addition to the Abaqus module.
  ```bash
  module load abaqus
  module load intel/2022.1.0
  abaqus verify -user_std
  ```

## Verification
- After loading the Intel module, the verification test for Abaqus/Standard with user subroutines passed successfully.

## General Learning
- Ensure all necessary modules are loaded when running software that requires specific dependencies.
- Verify software functionality with appropriate commands after making changes to module loads.

## Additional Resources
- [YouTube Video on Abaqus and Fortran Subroutines](https://www.youtube.com/watch?v=f_8CjAqcQNI)

## Support Team Involved
- HPC Admins
- 2nd Level Support Team
---

### 42172210_g77%20compiler.md
# Ticket 42172210

 # HPC Support Ticket: g77 Compiler

## Keywords
- g77 compiler
- gfortran
- Intel Fortran Compiler (ifort)
- gcc 3.4.6
- woody-cluster

## Problem
- User requires the g77 compiler for a program package.
- g77 is not installed on the woody-cluster.

## Root Cause
- The program package requires the g77 compiler, which is an outdated version of the gfortran compiler from older gcc versions.

## Solution
- **Recommended Solution:** Use `gfortran` as a compatible replacement for g77.
- **Alternative Solution:** Use the Intel Fortran Compiler (ifort) if available.
- **Last Resort:** An old version of gcc 3.4.6, which includes g77, is available at `/apps/gcc/gcc-3.4.6-x86_64` on the woody-cluster. However, using this version is strongly discouraged due to its age and potential compatibility issues with modern systems.

## General Learning
- g77 is an outdated Fortran compiler, and modern alternatives like `gfortran` or `ifort` should be used whenever possible.
- Older compilers may not fully support modern CPU features and could generate inefficient code.
- It is important to consider the compatibility and performance implications when using outdated software.

## Notes
- The HPC Admin provided detailed information on the availability of older compilers and the risks associated with their use.
- The user was advised to explore modern alternatives to ensure better performance and compatibility.
---

### 42156725_compiler%20Fehlermeldung.md
# Ticket 42156725

 # HPC Support Ticket: Compiler Fehlermeldung

## Keywords
- Compiler Error
- Fortran
- C++
- MKL
- Module Conflict
- ranmar_
- System Update

## Problem Description
- User encountered a compiler error (`undefined reference to 'ranmar_'`) after a system update.
- User is using `mpif90` for Fortran and `icpc` for C++.
- Module loading issues with `mkl` and `intel64`.

## Root Cause
- The function `ranmar_` is not part of the Fortran or C/C++ standards and is not included in the MKL.
- The user needs to define `ranmar_` themselves or ensure it is correctly referenced in their code.

## Solution
- If the user needs to use an older version of MKL (e.g., MKL 9.0), they should unload the automatically loaded MKL module after loading the compiler module and then load the desired MKL module.
- Ensure that `ranmar_` is correctly defined and referenced in the user's code.

## Steps to Resolve
1. Load the compiler module:
   ```sh
   module load intel64
   ```
2. Unload the automatically loaded MKL module:
   ```sh
   module unload mkl
   ```
3. Load the desired MKL module:
   ```sh
   module load mkl/9.0
   ```
4. Ensure that `ranmar_` is correctly defined and referenced in the user's code.

## Additional Notes
- The `intel64` module automatically loads the corresponding MKL module.
- The function `ranmar_` must be defined by the user or correctly referenced in their code.

## Conclusion
The issue was related to module conflicts and the need to define the `ranmar_` function. By following the steps to resolve module conflicts and ensuring the function is correctly defined, the user can compile their program successfully.
---

### 2015102242001332_netcdf%20gfortran.md
# Ticket 2015102242001332

 # HPC Support Ticket: netcdf gfortran

## Keywords
- NetCDF
- gfortran
- Intel Compiler
- Module Compatibility
- Compilation Error

## Problem Description
The user encountered a compilation error when trying to link a subroutine to the NetCDF libraries. The error message indicated that the `netcdf.mod` file was created by a different version of GNU Fortran.

## Root Cause
The NetCDF module file (`netcdf.mod`) was not compatible with the version of GNU Fortran being used by the user.

## Solution
1. **Switch to Intel Compiler**: The HPC Admin suggested switching to the Intel Compiler (ifort) instead of gfortran, as the NetCDF module for Intel is more compatible across different versions.
2. **Compatible Versions**: The user was advised to use Intel Compiler versions 14.0up03 or 15.0up02, as these versions are known to work well with the available NetCDF module.
3. **Automatic MPI Module**: The HPC Admin mentioned that a compatible intelmpi module would be automatically loaded with the chosen Intel Compiler version.

## Additional Notes
- The user was initially using gfortran version 4.9.2.
- The NetCDF module for Intel Compiler version 12.1 was suggested, but the user had issues with versions 12.1up11, 12.1up13, and 13.1up03.
- The user later requested a NetCDF library compiled with Intel Compiler version 17.0up05, but the HPC Admin indicated that the existing NetCDF library (compiled with Intel 15.0) should be compatible with newer Intel Compiler versions due to the unchanged Fortran API.

## Conclusion
Switching to a compatible Intel Compiler version and using the corresponding NetCDF module resolved the compilation issue. The user was advised to provide detailed error descriptions if further issues arise.
---

### 2022110142000821_Problems%20compiling%20WRF%20after%20HPC%20maintenance.md
# Ticket 2022110142000821

 # HPC Support Ticket: Problems Compiling WRF After HPC Maintenance

## Summary
User encountered issues compiling the WRF model on the HPC after maintenance in September. The problem was related to the update of modules and the need to use the same compiler for all necessary modules.

## Keywords
- WRF compilation
- Module updates
- Compiler issues
- NetCDF
- HDF5
- MPI
- GCC
- Intel

## Problem Description
- User failed to recompile the WRF model after HPC maintenance.
- The issue was related to the update of modules and the need to use the same compiler for all necessary modules.
- NetCDF-C was installed with GCC only, but WRF compilation required libraries (hdf5_hl_fortran) that were only found in the Intel version of HDF5.
- User created a custom NetCDF directory linking to all necessary lib, bin, and include files from the NetCDF-C and NetCDF-Fortran installation directories.

## Root Cause
- Incompatibility between the GCC and Intel versions of the required libraries.
- Missing environment variables or settings that WRF configure/compile did not like.

## Solution
- HPC Admins suggested loading specific modules and setting environment variables.
- User was advised to rename `.profile` and `.bashrc` to get a clean environment and try compiling a fresh WRF clone from GitHub.
- A new HDF5 module (hdf5/1.12.2-gcc8.5.0-impi) was created with the corresponding Fortran libraries.

## Steps Taken
1. User attempted to compile WRF with various module combinations but encountered errors.
2. HPC Admins provided a list of modules to load:
   ```bash
   module load 000-all-spack-pkgs
   module load parallel-netcdf/1.12.2-gcc8.5.0-impi-fhshu53
   module load netcdf-fortran/4.5.4-gcc8.5.0-impi-ljaao5f
   module load hdf5/1.12.2-gcc8.5.0-impi-d43mn7g
   module load netcdf-c/4.8.1-gcc8.5.0-impi-qy75oeu
   module load intelmpi/2021.6.0
   module load mkl/2021.4.0
   ```
3. User encountered errors such as "You need a ISO C conforming compiler to use the glibc headers."
4. HPC Admins suggested renaming `.profile` and `.bashrc` to get a clean environment and trying to compile a fresh WRF clone from GitHub.
5. A new HDF5 module (hdf5/1.12.2-gcc8.5.0-impi) was created with the corresponding Fortran libraries.

## Conclusion
The issue was resolved by creating a new HDF5 module with the necessary Fortran libraries and ensuring a clean environment for compilation. The user was able to successfully compile the WRF model after following the suggested steps.
---

### 2018061342001451_kleines%20Fortran%20Problem.md
# Ticket 2018061342001451

 # HPC Support Ticket: Fortran Issue with Integer Division

## Keywords
- Fortran
- Integer Division
- Optimization Flags
- Compilation Issues
- CPMD
- Intel Compiler

## Problem Description
The user encountered an issue with a Fortran program that divides a number (`nstates`) into `my_nproc` parts. The program had two variants: one with `xstates/my_nproc` inside a loop and one outside. The first variant, which is used in CPMD, sometimes resulted in incorrect divisions where the sum was one less than `nstates`. For example, 1547 divided by 12 resulted in 2*128 and 10*129.

## Root Cause
The issue was related to the optimization flags used during compilation. The user initially compiled the code with `-O2` optimization, which caused the incorrect division.

## Solution
The user found that compiling the code with `-O0` (no optimization) resolved the issue. Additionally, recalculating `xsnow` with `(ip-1)*xstates` and `xsaim` with `ip*xstates` within the loop also worked with `-O2` optimization.

## Lessons Learned
- Optimization flags can sometimes lead to unexpected behavior in code, especially with integer division.
- Disabling optimization (`-O0`) can help identify if the issue is related to optimization.
- Recalculating values within the loop can sometimes resolve issues related to optimization.

## Conclusion
The user resolved the issue by adjusting the optimization flags and recalculating values within the loop. This highlights the importance of understanding the impact of optimization flags on code behavior.
---

### 2015112342002597_Intel%20Fortran%20Bug.md
# Ticket 2015112342002597

 # Intel Fortran Bug Report

## Keywords
- Intel Fortran Bug
- Compiler Version Compatibility
- Fortran Standard Compliance
- BIND(C) Attribute
- Call by Reference vs. Call by Value

## Summary
A user reported an issue with an Intel Fortran program that worked with version 14.0up03 but not with later versions. The user also mentioned that the program worked with newer GCC versions.

## Root Cause
The issue was due to the variable 'i' in the call `ierr=f(i,C_LOC(v))` not being passed as value but by reference. The Intel compilers before version 15.0 treated this incorrectly, which is why the code worked in the past. The newer compilers fixed this to be conformant to the Fortran standard, causing the original code to fail.

## Solution
The code needed a minor change to add the `BIND(C)` attribute to the interface definition. This ensures that the argument 'row' is passed by value, as intended for a routine written in C.

```fortran
abstract interface
    function cfoo(row, val_ptr) bind(c) result(ierr)
end interface
```

## Lessons Learned
- Ensure that Fortran code interfacing with C routines uses the `BIND(C)` attribute to correctly handle argument passing.
- Be aware of changes in compiler behavior due to standard compliance updates.
- Reporting bugs through the appropriate channels can help in resolving issues efficiently.

## Actions Taken
- The issue was reported to Intel and escalated to engineering.
- The HPC Admin provided the user with the necessary code changes to resolve the issue.
- The ticket was closed after the problem was resolved.

## References
- Intel Case 6000142002
- Intel Case DPD20037907

## Conclusion
The issue was resolved by updating the code to comply with the Fortran standard, ensuring proper argument passing in interfaces with C routines.
---

### 42036910_Intel%20Fortran%20compiler%20error%20%40%20Woody.md
# Ticket 42036910

 # HPC Support Ticket: Intel Fortran Compiler Error

## Keywords
- Intel Fortran Compiler
- `cfx5mkext` command
- `libgfortran.so.1`
- Shared object file error
- Fatal Error
- Error message number: 001100279

## Problem Description
The user encountered a fatal error when trying to run a case after successfully compiling .F subroutines using the `cfx5mkext` command. The error message indicated a problem with opening a shared object file (`libwater_density.so`) due to a missing `libgfortran.so.1`.

## Root Cause
- The error message suggests a dependency issue with `libgfortran.so.1`, which is not typically required by the Intel Fortran compiler.
- There might be inconsistencies in the modules or commands used by the user.

## HPC Admin Response
- Requested detailed information about the modules and commands used, including versions, exact directory locations, and hostnames.
- Noted that Intel Fortran does not require `libgfortran.so.1` and that `libgfortran.so.1` is available on the system.

## Solution
- The user needs to provide detailed information about the environment and commands used to diagnose the issue further.
- Ensure that the correct modules and dependencies are loaded for the Intel Fortran compiler.

## General Learnings
- Always provide detailed information about the environment, modules, commands, and error messages when reporting issues.
- Understand the dependencies of the tools and compilers being used.
- Verify that all required libraries and dependencies are correctly loaded and available.

## Next Steps
- Await further details from the user to diagnose and resolve the issue.
- Ensure that the user is aware of the correct modules and dependencies required for the Intel Fortran compiler.
---

### 2023030842003105_Fortran%20Frage%3A%20Type%20mismatch%20in%20argument.md
# Ticket 2023030842003105

 # HPC Support Ticket: Fortran Argument Type Mismatch

## Keywords
- Fortran
- Type mismatch
- Argument mismatch
- GNU compiler
- Intel compiler
- Single precision
- Double precision
- Array allocation
- Memory management

## Problem Description
The user encountered a type mismatch error when compiling a Fortran program with GNU compiler version 9 or higher. The issue arises because the program attempts to pass a double precision array to a subroutine that expects a single precision array. The GNU compiler, being stricter in recent versions, flags this as an error without the `-fallow-argument-mismatch` option.

## Root Cause
The root cause of the problem is the mismatch between the expected single precision array in the subroutine and the double precision array passed from the main program.

## Proposed Solutions
1. **Solution 1**: Define the single precision array locally within the subroutine.
2. **Solution 2**: Allocate the single precision array locally within the subroutine using `allocate`.
3. **Solution 3**: Define an additional single precision array in the main program and pass it as an argument to the subroutine.
4. **Solution 4**: Use the `sngl()` function to convert the double precision array to single precision during the subroutine call.

## Discussion
- **Solution 1 vs. Solution 2**: Both solutions define the array locally, but Solution 2 uses dynamic allocation. The memory is automatically deallocated when the subroutine exits.
- **Solution 3**: This solution is advantageous if the subroutine is called multiple times, as it avoids repeated allocation and deallocation.
- **Solution 4**: This solution creates a temporary array, which may not be the most efficient approach.

## Recommended Solution
The HPC Admin suggested using C binding for modern Fortran, which is more robust and efficient for handling such type conversions. This solution was tested with different compilers and found to be robust.

## Additional Resources
- [Discussion on efficiency of copy or casting in Fortran](https://fortran-lang.discourse.group/t/speed-test-equivalence-vs-transfer-vs-reshape/2862/1)

## Conclusion
The best solution for the given problem is to use C binding for type conversions, as it is more efficient and robust. This approach avoids the type mismatch error and ensures compatibility with modern Fortran standards.
---

