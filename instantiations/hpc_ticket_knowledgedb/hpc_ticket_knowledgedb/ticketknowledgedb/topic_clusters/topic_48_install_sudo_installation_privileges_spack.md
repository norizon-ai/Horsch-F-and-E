# Topic 48: install_sudo_installation_privileges_spack

Number of tickets: 5

## Tickets in this topic:

### 2024062542002461_Installation%20of%20graphviz.md
# Ticket 2024062542002461

 ```markdown
# HPC Support Ticket: Installation of Graphviz

## Keywords
- Graphviz installation
- User space installation
- Spack
- Conda
- Module load

## Root Cause
- User needs to install Graphviz but lacks sudo privileges to use `apt install`.

## Solution
- Use Spack or Conda for user space installation.
- Commands for Spack installation:
  ```sh
  module load user-spack
  spack install graphviz
  ```

## General Learnings
- Users can install software in their user space using package managers like Spack or Conda.
- Spack and Conda are useful tools for managing software dependencies without requiring root privileges.
- Module loading is necessary to access Spack.

## References
- [Spack Documentation](https://doc.nhr.fau.de/apps/spack/)
- [Conda Documentation](https://doc.nhr.fau.de/environment/python-env/)
```
---

### 2022042042000568_Install%20a%20tool%20on%20the%20Woody%20node.md
# Ticket 2022042042000568

 # HPC Support Ticket: Install a Tool on the Woody Node

## Keywords
- Installation
- C-based tool
- ISMRMRD converter tool
- sudo make
- CMAKE_INSTALL_PREFIX
- $WORK directory

## Problem
- **Root Cause:** User needs to install a C-based tool (ISMRMRD converter tool) but lacks sudo privileges.
- **Error:** User receives an error when attempting to use `sudo make`.

## Solution
- **Instructions:**
  - Install the application in a directory where the user has write permissions, such as `$WORK`.
  - Change the installation path using one of the following methods:
    - Set `CMAKE_INSTALL_PREFIX` when configuring with cmake:
      ```sh
      cmake -DCMAKE_INSTALL_PREFIX="$WORK/apps/siemens_to_ismrmrd" ..
      make
      make install
      ```
    - Use `cmake --install` with the `--prefix` option:
      ```sh
      cmake --install . --prefix "$WORK/apps/siemens_to_ismrmrd"
      ```
  - Ensure the commands are run from the build subdirectory of the checked-out source.

## References
- [ISMRMRD Converter Tool README](https://github.com/ismrmrd/siemens_to_ismrmrd/blob/master/README.mkd)
- [CMake Install Documentation](https://cmake.org/cmake/help/latest/manual/cmake.1.html#install-a-project)

## General Learning
- Users without sudo privileges can install applications in directories where they have write permissions.
- CMake allows setting the installation prefix to a user-writable directory.
- Proper configuration and build steps are crucial for successful installation.
---

### 2025022542005481_Regarding%20Installation%20of%20a%20POSTGRESQL%20local%20server%20on%20an%20hpc%20account.md
# Ticket 2025022542005481

 # HPC Support Ticket: Local PostgreSQL Installation

## Keywords
- PostgreSQL
- Local installation
- HPC account
- Sudo permissions
- $WORK directory

## Problem
- User needs to install a local instance of PostgreSQL on an HPC account (woody) for a project.
- Requires sudo permissions which are not openly accessible.

## Solution
- Install PostgreSQL in user-specific directories such as `$WORK`.
- No root permissions are required for this installation.
- Reference: [FAQ on software installation without sudo](https://doc.nhr.fau.de/faq/?h=sudo#i-want-to-install-software-but-i-don-t-know-the-password-for-t53--what-can-i-do)

## General Learning
- Users can install software locally in their directories without needing sudo permissions.
- HPC Admins can guide users to install software in their home or work directories.
- Reference documentation is available for users to follow for local software installations.
---

### 2022081042001248_Installation%20von%20Modulen.md
# Ticket 2022081042001248

 # HPC Support Ticket: Installation von Modulen

## Keywords
- Module installation
- Administrator rights
- User directories
- Build/Installation process

## Problem
- User requires installation of modules for their Master's thesis.
- User lacks necessary administrator rights to install modules on the woody-Cluster.

## Root Cause
- User does not have the required permissions to install modules system-wide.

## Solution
- **User Directory Installation**: Users can install most software in their own directories, preferably in `$WORK`.
- **Build/Installation Process**: Users need to specify the installation path during the build/installation process.
- **Alternative Support**: Users can seek assistance from their supervisor or other colleagues at ECAP.

## General Learnings
- Users can install software in their own directories without needing administrator rights.
- Specifying installation paths is crucial during the build/installation process.
- Additional support can be sought from supervisors or colleagues.

## Notes
- Linux distribution packages cannot be installed in this manner.
- The HPC Admin provided guidance on where to install software and how to specify installation paths.

---

This documentation can be used to assist users with similar issues related to module installation and lack of administrator rights.
---

### 2025022442001727_Password%20for%20sudo.md
# Ticket 2025022442001727

 # HPC Support Ticket: Password for sudo

## Keywords
- sudo
- admin privileges
- local installation
- dependencies
- conda environment
- user directory

## Problem
- User attempted to install a package using `sudo` but was prompted for a password.
- User does not have admin privileges and cannot use `sudo`.

## Root Cause
- Lack of understanding about user permissions and the proper method for installing software on an HPC cluster.

## Solution
- Users are not permitted to use `sudo` for installing software.
- Users should install software locally within their own directories.
- Recommended methods for local installations include using a conda environment or defining custom modules.
- Refer to the documentation for detailed instructions: [NHR@FAU Documentation](https://doc.nhr.fau.de)

## General Learning
- Users should be aware that they do not have administrative privileges on HPC clusters.
- Local installations within user directories are the recommended approach for adding dependencies.
- Conda environments and custom modules are effective tools for managing local software installations.
- Always refer to the official documentation for guidance on setting up environments and installing software.
---

