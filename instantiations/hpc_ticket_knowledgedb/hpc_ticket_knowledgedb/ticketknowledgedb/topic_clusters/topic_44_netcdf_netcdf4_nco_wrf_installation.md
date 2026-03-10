# Topic 44: netcdf_netcdf4_nco_wrf_installation

Number of tickets: 8

## Tickets in this topic:

### 2016061442001069_netcdf%20update%20on%20emmy%3F%20%28user%20gwgi18%29.md
# Ticket 2016061442001069

 ```markdown
# HPC-Support Ticket: netcdf update on emmy?

## Keywords
- netCDF
- NCL script
- WRF output files
- File format error
- HPC environment

## Problem Description
User encountered issues with an NCL script reading WRF output files, resulting in errors such as:
- `fatal:NetCDF: Unknown file format`
- `fatal:Could not open (destination_grid_file.nc)`
- `fatal:Could not create (destination_grid_file.nc)`
- `warning:FileSetFileOption: invalid file or format`

## Root Cause
- No recent updates to netCDF libraries on the HPC system.
- Possible issue within the NCL script or the WRF output files.

## Solution
- HPC Admins confirmed no changes to netCDF libraries.
- User to investigate the NCL script and WRF output files further.

## Lessons Learned
- Always check for recent updates or changes in the HPC environment.
- If no updates, focus on script and file integrity.
- Communicate effectively with HPC Admins for quick resolution.

## Ticket Status
- Closed: No changes to netCDF libraries; issue likely within user's script or files.
```
---

### 2019051742001372_Installation%20von%20Software.md
# Ticket 2019051742001372

 ```markdown
# HPC-Support Ticket: Installation von Software

## Keywords
- Software Installation
- GMT (Generic Mapping Tools)
- GDAL
- NetCDF4
- Python 2.7
- Woody
- TinyEth
- Ubuntu Packages
- Dependencies

## Problem
- User requires installation of GMT, GDAL, and NetCDF4 module in Python 2.7 on HPC clusters Woody and TinyEth.

## Conversation Summary
- **User Request**: Installation of GMT, GDAL, and NetCDF4 module in Python 2.7 on Woody and TinyEth.
- **HPC Admin Response**:
  - NetCDF4 module is available in Python 2.7-anaconda.
  - GMT and GDAL are available as Ubuntu packages but have unusual dependencies.
  - Dependencies issue resolved by excluding `gdal-doc` package.
  - Software installed on Woody frontends and nodes.
  - Installation on TinyEth pending due to ongoing reinstallation.

## Solution
- **NetCDF4 Module**: Available in Python 2.7-anaconda.
- **GMT and GDAL**: Installed on Woody frontends and nodes. Installation on TinyEth will be completed during its reinstallation.
- **Dependencies Issue**: Resolved by excluding `gdal-doc` package.

## General Learnings
- Ensure software dependencies are checked before installation to avoid unnecessary packages.
- Coordinate software installations with ongoing system updates or reinstallations.
- Communicate clearly with users about the status of their requests and any potential delays.
```
---

### 2022091942005781_NCO_NetCDF%20installation%3A%20Woody-NG.md
# Ticket 2022091942005781

 ```markdown
# HPC-Support Ticket Conversation: NCO/NetCDF Installation

## Subject
NCO/NetCDF installation: Woody-NG

## Keywords
- NCO
- NetCDF
- Installation
- Library
- HDF5
- Elmer/Ice
- Spack

## Problem Description
- User is attempting to install NCO using available NetCDF installations.
- Error: `libnetcdf.a` cannot be found.
- Library is located in `$HOME_C_ROOT/lib/`.
- User tried linking the location and using environmental variables without success.
- User also installed HDF5 and NetCDF-C & -Fortran libraries.
- HDF5 installation was successful, but NetCDF-C required disabling netcdf4.

## Root Cause
- The user is facing issues with locating the `libnetcdf.a` library during the installation process.
- The user is unsure why disabling netcdf4 is necessary for NetCDF-C installation.

## Solution
- HPC Admin suggests using a script to build NetCDF via Spack, which has been successful for the ElmerICE group.
- No further issues reported since September, indicating the problem might have been resolved with the Spack script.

## General Learnings
- Utilize Spack for building and managing software dependencies to avoid manual installation issues.
- Ensure proper linking and environmental variable settings when dealing with library paths.
- Document successful installation scripts for future reference and troubleshooting.
```
---

### 2015102942000179_NCO%20toolkit.md
# Ticket 2015102942000179

 # HPC-Support Ticket Conversation: NCO Toolkit Installation

## Keywords
- NCO Toolkit
- netCDF
- Compilation Error
- HDF5
- szip
- Module Installation

## Summary
A user attempted to install the NCO toolkit locally but encountered compilation errors due to missing netCDF-4 functionalities. The HPC admins provided guidance and eventually installed a compatible netCDF module that resolved the issue.

## Root Cause
- The user's local installation of the NCO toolkit failed because the available netCDF modules did not support netCDF-4 functionalities, which were required by NCO.
- The compilation error indicated missing references to netCDF-4 specific functions.

## Solution
- The HPC admins suggested that the user could either build NCO without netCDF-4 support or install a compatible netCDF version that supports netCDF-4.
- The admins provided an installation guide for netCDF, HDF5, and szip.
- Eventually, a new netCDF module (netcdf/4.3.3.1-intel15.0) was installed on the HPC system, which included support for netCDF-4.
- The user was able to compile NCO successfully using the new netCDF module.

## General Learnings
- Ensure that the required dependencies and their versions are compatible with the software being installed.
- netCDF-4 support is crucial for certain applications and may require additional libraries like HDF5 and szip.
- HPC admins can provide module installations that include necessary dependencies to simplify user installations.
- Detailed installation guides and module documentation can help users troubleshoot and resolve installation issues.

## Actions Taken
- The HPC admins installed a new netCDF module with netCDF-4 support.
- The user successfully compiled the NCO toolkit using the new netCDF module.

## Conclusion
The issue was resolved by installing a compatible netCDF module that included netCDF-4 support. This allowed the user to successfully compile the NCO toolkit.
---

### 2018061942002162_nco%20install%20problem.md
# Ticket 2018061942002162

 # HPC Support Ticket: nco Install Problem

## Keywords
- nco installation
- libpng
- antlr
- JDK
- module load
- configure
- make
- make install

## Problem Summary
- User encountered issues with nco installation, specifically with missing components like `ncap2` and `libpng` problems.
- Initial configuration required specifying `NETCDF_LIB` and `NETCDF_INC`.
- User needed to download `antlr-2.7.7`, which required JDK (javac).

## Root Cause
- Missing dependencies (`antlr-2.7.7` and JDK) for complete nco installation.
- Potential version mismatch with `libpng`.

## Solution
- User was advised to install necessary software (JDK, antlr) in their home directory.
- HPC Admin suggested using the available JDK module (`module load java/jdk1.8`) to avoid manual installation.
- HPC Admin also mentioned the availability of `javac` in the standard path on Meggie Frontends.

## General Learnings
- Ensure all dependencies are installed before configuring and building software.
- Utilize available modules to simplify the installation process.
- Check for existing software versions and paths to avoid redundant installations.

## Actions Taken
- HPC Admin provided guidance on using existing JDK modules and standard paths.
- User successfully installed `antlr` and `nco` after following the advice.

## Follow-up
- No further action required as the issue was resolved.
---

### 2023081042000872_missing%20module%20for%20netcdf-c.md
# Ticket 2023081042000872

 # HPC Support Ticket: Missing Module for netcdf-c

## Keywords
- Module loading issue
- netcdf-c
- WRF model
- Fritz cluster
- Module alternatives

## Problem Description
- User unable to load `netcdf-c/4.8.1-gcc8.5.0-impi-scnset7` module.
- Alternative module `netcdf-c/4.8.1` did not work.
- Issue prevented running the WRF model.

## Other Loaded Modules
- 000-all-spack-pkgs/0.19.1
- netcdf-fortran/4.5.3-intel
- parallel-netcdf/1.12.2-intel2021.4.0-impi
- hdf5/1.10.7-impi-gcc
- mkl/2021.4.0
- intelmpi/2021.6.0
- m4/1.4.19

## Root Cause
- Unspecified issue with the `netcdf-c/4.8.1-gcc8.5.0-impi-scnset7` module.

## Solution
- User resolved the issue independently.
- No specific solution provided in the ticket.

## General Learnings
- Importance of module compatibility for running specific models (e.g., WRF).
- Users may resolve issues independently, reducing support load.
- Documentation of module dependencies and alternatives can be helpful for troubleshooting.

## Next Steps
- Ensure module documentation is up-to-date.
- Monitor for similar issues to identify patterns or recurring problems.
---

### 2020031642000205_WRF%20%2B%20tools.md
# Ticket 2020031642000205

 # HPC Support Ticket: WRF + Tools

## Keywords
- WRF installation
- Compilation flags
- NetCDF
- WPS
- GRIB2
- Numerical instabilities
- Environmental variables

## Summary
The ticket involves issues related to the WRF (Weather Research and Forecasting Model) installation, including compilation flags, NetCDF file readability, and WPS (WRF Preprocessing System) configuration.

## Issues and Solutions

### Compilation Flags
- **Issue**: Numerical instabilities in WRF simulations.
- **Solution**: Use `-fp-model=precise` to mitigate numerical artifacts.

### NetCDF File Readability
- **Issue**: WRF binary produces unreadable NetCDF files.
- **Solution**: Ensure the following environmental variables are set:
  ```bash
  export WRFIO_NCD_LARGE_FILE_SUPPORT=1
  export WRF_EM_CORE=1
  export WRF_NMM_CORE=0
  export WRF_CHEM=0
  export NETCDF4=1
  ```

### WPS Configuration
- **Issue**: WPS is missing.
- **Solution**: Compile WPS as a serial application without GRIB2 support.

## Additional Information
- The HPC Admin provided new builds for WRF, WPS, and related tools linked to the latest NetCDF and HDF5 versions.
- The user confirmed that a colleague's COVID-19 test result was negative.

## Conclusion
The ticket highlights the importance of setting appropriate compilation flags and environmental variables for WRF and WPS to ensure proper functionality and data integrity. The HPC Admin successfully resolved the issues and provided updated modules for the users.
---

### 2022091342002767_Missing%20software%20meggie.md
# Ticket 2022091342002767

 # HPC Support Ticket: Missing Software Meggie

## Keywords
- Meggie reinstallation
- Missing modules
- netCDF, intel64, ncl
- LD_LIBRARY_PATH
- NETCDF_C_ROOT, NETCDF_FORTRAN_ROOT
- nf-config

## Problem
- After the reinstallation of Meggie, the user cannot find or load modules like netCDF, intel64, and ncl.
- The user needs to update the LD_LIBRARY_PATH environment variable to include the path to the netCDF shared library but cannot find the library.

## Cause
- The reinstallation of Meggie led to changes in module names and paths.
- The intel64 module was split into intel, intelmpi, and mkl.
- The netCDF library paths were not set correctly in the user's environment.

## Solution
- The intel64 module has been split into intel, intelmpi, and mkl. Users should load these modules instead.
- The netCDF libraries can be found under `$NETCDF_C_ROOT/lib` and `$NETCDF_FORTRAN_ROOT/lib` for netcdf-c and netcdf-fortran, respectively.
- Use the `nf-config` command from netCDF to get the correct flags and library paths:
  ```
  $ nf-config --cflags --fflags
  $ nf-config --flibs
  ```

## General Learnings
- Module reinstallations or updates can lead to changes in module names and paths.
- Environment variables like LD_LIBRARY_PATH should be set automatically by the module system, but manual intervention may be required in some cases.
- Specific commands like `nf-config` can help users find the correct library paths and flags.
- Effective communication and notification systems are crucial for keeping users informed about system changes.
---

