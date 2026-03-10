# Topic 9: python_conda_environment_module_install

Number of tickets: 138

## Tickets in this topic:

### 2024031242002392_Fehler%3A%20_lib64_libm.so.6%3A%20version%20%60GLIBC_2.29%27%20not%20found.md
# Ticket 2024031242002392

 # HPC Support Ticket: GLIBC Version Issue

## Keywords
- GLIBC version error
- Python project
- slang
- libc
- libm
- conda environment
- Docker container

## Problem Description
The user encountered an error when trying to run a Python project that uses the `slang` library on the HPC system. The error message indicated that the required version of GLIBC (`GLIBC_2.29`) was not found. The system's default GLIBC version is 2.28, which is insufficient for the `slang` library.

## Root Cause
The root cause of the problem is the mismatch between the required GLIBC version (`GLIBC_2.29`) and the available system GLIBC version (2.28). The `slang` library depends on the newer GLIBC version, which is not available on the HPC system.

## Attempted Solutions
1. **Using System GCC**: The HPC Admin suggested using the system GCC, which includes `libc` and `libm`, but this did not resolve the issue due to the version mismatch.
2. **Conda Environment**: The user provided the setup script for creating a conda environment, but the issue persisted.

## Final Solution
The HPC Admin recommended using a Docker container as a workaround, as it allows for the installation of the required GLIBC version without modifying the system libraries. This approach was suggested because other workarounds would likely lead to further issues in the long run.

## Lessons Learned
- **GLIBC Version Compatibility**: Ensure that the required GLIBC version is available on the system or use a container solution to avoid version mismatches.
- **Container Solutions**: Docker containers can be a practical solution for managing dependencies and avoiding system-level conflicts.
- **System Libraries**: Be aware of the limitations of system libraries and consider alternative solutions when encountering version incompatibilities.

## References
- [Slang GitHub Repository](https://github.com/shader-slang/slang/tree/master)
- [NHR@FAU Support](https://hpc.fau.de/)
---

### 2023031642001806_Alex%20GPU%20Cluster%3A%20Probleme%20mit%20anaconda%20und%20modules.md
# Ticket 2023031642001806

 ```markdown
# HPC Support Ticket: Alex GPU Cluster - Issues with Anaconda and Modules

## Summary
User encountered issues with `git` availability and conflicts between `conda` and `module` commands on the Alex GPU Cluster.

## Issues
1. **Git Availability**: `git` not available on the front node.
2. **Conda and Module Conflict**: After initializing `conda`, the `module avail` command becomes unavailable.

## Root Cause
1. **Git Availability**: `git` is provided via modules and needs to be loaded using `module avail git`.
2. **Conda and Module Conflict**: The user's `.bashrc` file initializes `conda`, which overrides the `module` command. Additionally, the shell was not being started as a login shell (`bash -l`).

## Solution
1. **Git Availability**:
   - Use `module avail git` to load the `git` module.
   ```bash
   module avail git
   ```

2. **Conda and Module Conflict**:
   - Modify the `.bashrc` file to comment out the line that initializes `conda`.
   - Ensure the shell is started as a login shell by adding `"args": ["-l"]` to the VSCode terminal profile settings.
   ```json
   "terminal.integrated.profiles.linux": {
       "bash": {
           "path": "/usr/bin/bash",
           "args": ["-l"]
       }
   }
   ```

## Keywords
- git
- conda
- module
- VSCode
- bash
- login shell
- Alex GPU Cluster

## Lessons Learned
- Always check if software is available via modules.
- Ensure that the shell is started as a login shell to avoid conflicts with environment variables and commands.
- Modify `.bashrc` and VSCode settings to resolve conflicts between `conda` and `module`.
```
---

### 2023082242003034_doubt%20regarding%20installation%20of%20a%20few%20python%20libraries.md
# Ticket 2023082242003034

 ```markdown
# HPC Support Ticket: Python Library Installation Issue

## Keywords
- Conda configuration
- Python libraries
- MDAnalysis
- Pytim
- NoWritablePkgsDirError

## Problem Description
A PhD student encountered issues while trying to install the Python libraries MDAnalysis and Pytim using Conda. The error message indicated a lack of writable package directories:
```
NoWritablePkgsDirError: No writeable pkgs directories configured.
- /apps/python/3.9-anaconda/pkgs
```

## Root Cause
The error suggests that Conda was not properly configured to use writable directories for storing packages and environments.

## Solution
The HPC Admin provided the following steps to initialize and configure Conda to store environments and packages under the user's `$WORK` directory:

1. Initialize Conda for the current shell:
   ```bash
   conda init bash
   ```

2. Source the `.bashrc` file to apply the changes:
   ```bash
   . ~/.bashrc
   ```

3. Configure Conda to use custom directories for packages and environments:
   ```bash
   conda config --add pkgs_dirs $WORK/software/privat/conda/pkgs
   conda config --add envs_dirs $WORK/software/privat/conda/envs
   ```

4. If `~/.bashrc` is not loaded automatically, create a `~/.bash_profile` with the following content:
   ```bash
   if [ -f ~/.bashrc ]; then . ~/.bashrc; fi
   ```

## General Learnings
- Proper configuration of Conda is essential for managing Python environments and packages.
- Custom directories can be specified for Conda to store packages and environments, especially useful in shared or restricted environments.
- Initializing Conda and sourcing the `.bashrc` file ensures that the configuration changes take effect.

## References
- [FAU HPC Documentation on Python and Jupyter](https://hpc.fau.de/systems-services/documentation-instructions/special-applications-and-tips-tricks/python-and-jupyter/)
- [Bash Startup Files](https://www.gnu.org/software/bash/manual/html_node/Bash-Startup-Files.html)
```
---

### 2025021842003657_Help%20Needed%3A%20%5Bbash%3A%20module%3A%20command%20not%20found%5D.md
# Ticket 2025021842003657

 ```markdown
# HPC Support Ticket: Help Needed - [bash: module: command not found]

## Keywords
- module command not found
- login shell
- SLURM job
- interpreter directive
- `-l` flag

## Problem Description
User encountered the error "module: command not found" while trying to set up the environment using `<module avail>`.

## Root Cause
- The error occurred because the user did not have a login shell activated.
- In the case of a SLURM job, the `-l` flag was missing in the interpreter directive.

## Solution
- For SLURM jobs, ensure the first line of the job script includes the `-l` flag to initialize modules correctly:
  ```bash
  #!/bin/bash -l
  ```
- Ensure a login shell is activated if the error occurs on the frontend.

## Lessons Learned
- The `-l` flag in the interpreter directive is necessary to initialize modules correctly in SLURM job scripts.
- A login shell must be activated to use the `module` command on the frontend.
```
---

### 2023110942002911_Issue%20Regarding%20OpenDBM%20Tool%20Usage%20on%20HPC%20-%20empk004h.md
# Ticket 2023110942002911

 # HPC Support Ticket: Issue Regarding OpenDBM Tool Usage on HPC

## Summary
The user needs to use the OpenDBM tool on the HPC system, which relies on a provided Docker file. The command `docker pull opendbmteam/dbm-openface` cannot be executed on the HPC.

## Problem
- The user is unable to execute the Docker command on the HPC system.
- The Docker container tries to access Python packages in the root directory, but the user does not have permission to install the dependent Python packages.

## Solution
1. **Use Apptainer for Docker Containers:**
   - The HPC system supports Docker containers through Apptainer.
   - Pull the container from Dockerhub and convert it to the Apptainer format using the command:
     ```bash
     apptainer pull docker://opendbmteam/dbm-openface
     ```
   - Run the container using:
     ```bash
     apptainer run <name_of_container>
     ```

2. **Building and Running the Container:**
   - The HPC Admin built a current Apptainer container from OpenDBM and provided it under `/tmp/dbm-openface-2.sif` on the `alex1` server.
   - The user should log in to `alex1` with their user credentials and access the container.
   - Run the container with the following command:
     ```bash
     apptainer exec --writable-tmpfs dbm-openface-2.sif /bin/bash -c "python3 -W ignore /app/process_data.py --input_path INPUT_PATH --output_path OUTPUT_PATH"
     ```

3. **Permissions Issue:**
   - The user encountered a permissions issue when trying to access the container file.
   - The HPC Admin confirmed that the file should be readable by everyone and provided guidance on logging in to the correct server.

## Additional Resources
- **Slides and Recording:**
  - The HPC Admin provided slides and a recording on how to use Apptainer:
    - Slides: [HPC-Cafe-Software-ALL.pdf](https://hpc.fau.de/files/2023/09/2023-09-12-HPC-Cafe-Software-ALL.pdf)
    - Recording: [FAU TV Clip](https://www.fau.tv/clip/id/49100) (after IdM login)

## Conclusion
The user should follow the steps provided by the HPC Admin to pull and run the Docker container using Apptainer. If any issues persist, they should contact the HPC Support for further assistance.
---

### 2020101942003907_Problems%20loading%20modules.md
# Ticket 2020101942003907

 # HPC Support Ticket: Problems Loading Modules

## Keywords
- Python module import error
- Anaconda version conflict
- Circular import error
- `hoomd` module
- `sys.path`

## Problem Description
- User encountered an error while importing a Python module (`hoomd`) in a job submission.
- The error message indicated a circular import issue.
- The job had previously worked without issues.

## Root Cause
- A new Anaconda version (python/3.8-anaconda) was installed on the HPC system, which may have caused compatibility issues.

## Solution
- HPC Admins suggested that the user try again after a default version was set to the older Anaconda version (3.7-anaconda).
- If the error persists, the user was asked to provide the Anaconda version they were using and an example script to reproduce the error.

## General Learnings
- Changes in software versions (e.g., Anaconda) can lead to compatibility issues with existing scripts.
- It is important to check for recent software updates when troubleshooting sudden errors in previously working scripts.
- Providing detailed information, such as the software version and a reproducible example, can help in diagnosing and resolving issues more efficiently.

## Next Steps
- If the error reappears, the user should provide the requested information to the HPC Admins for further investigation.

---

This documentation can be used to troubleshoot similar issues related to Python module imports and Anaconda version conflicts on the HPC system.
---

### 2024112642001619_Error%20while%20running%20python%20project%3A%20undefined%20symbol%3A%20slurm_conf.md
# Ticket 2024112642001619

 # HPC Support Ticket: Undefined Symbol Error with Slurm

## Keywords
- Undefined symbol error
- Slurm
- Python
- auth_munge.so
- slurm_conf
- dlopen
- plugin_load_from_file
- pytest
- interactive session

## Problem Description
The user encountered an undefined symbol error when running a Python project on the HPC system. The error occurred during the import of Python packages and while running pytest in an interactive session. The specific error message indicated a problem with loading the `auth_munge.so` plugin due to an undefined symbol `slurm_conf`.

## Error Message
```bash
python: error: plugin_load_from_file:
dlopen(/usr/lib64/slurm/auth_munge.so): /usr/lib64/slurm/auth_munge.so:
undefined symbol: slurm_conf
python: error: Couldn't load specified plugin name for auth/munge:
Dlopen of plugin file failed
python: error: cannot create auth context for auth/munge
python: fatal: failed to initialize auth plugin
```

## Root Cause
The error is likely due to a Python module-level import issue that is not explicit and results in an undefined symbol error.

## Solution
Another user who encountered the same error found that adding the following lines at the beginning of the script helped resolve the issue:
```python
import os, sys
sys.setdlopenflags(os.RTLD_NOW | os.RTLD_GLOBAL)
```
This solution was suggested by the HPC Admin and can be found in the [NVIDIA DeepOps GitHub issue](https://github.com/NVIDIA/deepops/issues/720).

## General Learning
- The error `undefined symbol: slurm_conf` indicates a problem with loading the `auth_munge.so` plugin.
- Adding specific lines to the script can help resolve symbol loading issues in Python.
- It is useful to check if similar issues have been reported and resolved by other users.

## References
- [NVIDIA DeepOps GitHub Issue](https://github.com/NVIDIA/deepops/issues/720)
---

### 2020021942003155_python_3.7-anaconda%3F.md
# Ticket 2020021942003155

 ```markdown
# HPC Support Ticket: Python 3.7 Module Request

## Keywords
- Python 3.7
- Module installation
- woody/tinyfat
- Anaconda

## Summary
A user requested the installation of Python 3.7 in the modules on the woody/tinyfat HPC systems.

## Root Cause
The user needed Python 3.7 for their work, but it was not available in the current modules.

## Solution
The HPC Admins installed Python 3.7 in the modules on the specified systems.

## Lessons Learned
- Users may require specific versions of software for their projects.
- HPC Admins can quickly address such requests by installing the required software versions.
- Effective communication and prompt action ensure user satisfaction.
```
---

### 2018121042002247_Cronjob%20Problem%3A%20_init_bash%3A%20No%20such%20file%20or%20directory.md
# Ticket 2018121042002247

 # HPC-Support Ticket: Cronjob Problem - /init/bash: No such file or directory

## Keywords
- Cronjob
- Crontab
- Shell script
- Environment variables
- Module loading
- $MODULESHOME
- Bash
- PBS

## Problem Description
The user encountered an issue while setting up a cronjob. The cronjob script attempts to source a file from `$MODULESHOME/init/bash`, but the cron daemon reports an error: `/init/bash: No such file or directory`.

## Root Cause
The cron environment does not have access to the `$MODULESHOME` environment variable, leading to the script failing to locate the required initialization file.

## Solution
Ensure that the cron environment has the necessary environment variables set. This can be done by explicitly setting the `$MODULESHOME` variable within the cronjob script or by sourcing the appropriate environment setup script at the beginning of the cronjob script.

## General Learnings
- Cron jobs run in a limited environment and may not have access to all environment variables available in an interactive shell.
- It is important to explicitly set or source required environment variables within the cronjob script.
- Module loading and environment setup should be handled carefully in non-interactive environments like cron jobs.

## Example Fix
```bash
#!/bin/bash -l
# Set the MODULESHOME variable explicitly
export MODULESHOME=/path/to/modules

# Source the initialization script
source $MODULESHOME/init/bash

# Load the required modules
module add gamma/20180703 r/3.4.3-mro

# Rest of the script
```

## Additional Notes
- Always test cronjob scripts in a non-interactive environment to ensure they have access to all required resources.
- Documenting environment setup steps within the script can help in troubleshooting similar issues in the future.
---

### 2024070142001683_Problems%20with%20Anaconda.md
# Ticket 2024070142001683

 # HPC Support Ticket: Problems with Anaconda

## Keywords
- Anaconda
- Conda
- HTTP Error
- CondaHTTPError
- Connection Failed
- Timeout
- Repodata.json
- Libmamba Solver
- Conda Reset

## Problem Description
User encountered issues with Anaconda after following installation instructions for a package (SLEAP). After executing specific commands to update and configure Conda, the user received a `CondaHTTPError` indicating a connection failure when trying to retrieve `repodata.json`.

## Root Cause
- Possible timeout issue due to network or configuration settings.
- Misconfiguration of Conda settings, specifically related to the `libmamba` solver.

## Solution
1. **Check FAQ for Timeout Issues**:
   - Refer to the FAQ link provided by the HPC Admin for resolving HTTP/HTTPS timeout issues.

2. **Rename Conda Configuration Files**:
   - Rename or remove Conda-related files in the user's home directory to reset Conda settings.
     ```bash
     mv ~/.condarc ~/.condarc_backup
     mv ~/.conda ~/.conda_backup
     ```

## General Learning
- Timeout issues can often be resolved by referring to specific FAQs or documentation.
- Resetting Conda settings by renaming or removing configuration files can help resolve persistent issues.
- Changing Conda solvers (e.g., `libmamba`) can sometimes lead to unexpected errors, and reverting to the default solver may be necessary.

## Additional Notes
- Always ensure that network settings and configurations are correctly set up to avoid timeout issues.
- Keep a backup of configuration files before making changes to facilitate easy restoration if needed.
---

### 2015102042000579_HPC_LIMA%3A%20_MD5.md
# Ticket 2015102042000579

 # HPC Support Ticket: HPC_LIMA: _MD5

## Keywords
- Elmer/Ice
- MUMPS
- Python 2.7.1
- md5
- ImportError
- OpenSSL
- MPI

## Problem Description
The user encountered an `ImportError: No module named _md5` while running tests for the MUMPS package on the HPC system LIMA. The error occurred in the Python 2.7.1 environment and was related to the md5 module.

## Root Cause
The issue was due to incompatible OpenSSL versions between the Python installation and the system. The Python 2.7.1 installation was copied from another system (Woody) and had compatibility issues with the OpenSSL version on LIMA.

## Solution
The HPC Admin resolved the issue by ensuring the Python 2.7.1 installation on LIMA was compatible with the OpenSSL version. Additionally, a new Python version (2.7.10-intel_tp1) was made available, which uses Intel's Math Kernel Library (MKL) to accelerate mathematical routines.

## General Learnings
- Ensure compatibility of OpenSSL versions with Python installations.
- Consider using Intel's Python distribution for improved performance with mathematical routines.
- Check for module dependencies and compatibility when copying installations between systems.

## Related Links
- [Elmer/Ice Documentation](http://elmerice.elmerfem.org/wiki/doku.php)
- [MUMPS Documentation](http://mumps.enseeiht.fr/)
- [Python Mailing List Discussion on md5 Issue](http://www.gossamer-threads.com/lists/python/python/909285)
---

### 2022121442003052_gcc%20version%20error.md
# Ticket 2022121442003052

 # HPC Support Ticket: gcc version error

## Keywords
- GCC version error
- GLIBCXX_3.4.29 not found
- Conda environment
- Python environment
- SLURM script
- Module system

## Problem Description
The user encountered an `ImportError` due to a missing `GLIBCXX_3.4.29` version required by a Python package (`sklearn`). The user's GCC version was 9.4.0, but GCC 11.1.0 was required.

## Root Cause
- The user's Python environment was created using Conda, but the necessary GCC version (11.1.0) was not provided by the HPC system.
- The user did not load any modules in their SLURM script, which might have led to inconsistencies in the environment.
- The user's custom GCC 11 installation was not consistently used for compiling the C/C++ backend of their Python libraries.

## Steps Taken by the User
1. Installed Python using Conda and created a Conda environment named `self-classifier-2`.
2. Ran an SLURM script that did not load any modules.
3. Verified that the required `GLIBCXX_3.4.29` version was not present in the system's `libstdc++.so.6`.

## Solution
- The likely solution is to add the user's GCC 11 installation to the `$PATH` and `$LD_LIBRARY_PATH` variables.
- Follow the HPC system's documentation for Conda environment creation to ensure the correct compiler and library versions are used.
- Ensure that the SLURM script loads the necessary modules for the job.

## Relevant Documentation
- [TensorFlow and PyTorch Documentation](https://hpc.fau.de/systems-services/documentation-instructions/special-applications-and-tips-tricks/tensorflow-pytorch/)
- [Python and Jupyter Documentation](https://hpc.fau.de/systems-services/documentation-instructions/special-applications-and-tips-tricks/python-and-jupyter/)

## Additional Notes
- The user was advised to attach files directly to the email/ticket instead of using external services like Pastebin.
- If the user continues to encounter issues, they can schedule a meeting with the support team for further assistance.
---

### 2022021642002621_Problem%3A%20Accidental%20update.md
# Ticket 2022021642002621

 # HPC Support Ticket: Accidental Update Issue

## Keywords
- pip install --upgrade
- jupyterlab
- ipympl
- ModuleNotFoundError
- traitlets.utils.descriptions
- conda install traitlets=4.3.3
- dependency issue

## Problem
- **User Action:** Executed `pip install --upgrade jupyterlab ipympl`
- **Error Message:** `ModuleNotFoundError: No module named 'traitlets.utils.descriptions'` when launching JupyterLab
- **Root Cause:** Accidental upgrade leading to dependency issues between jupyterlab/lab and traitlets

## Solution
- **HPC Admin Suggestion:** Downgrade `traitlets` to a compatible version
  - Command: `conda install traitlets=4.3.3`
  - Note: The exact version of `traitlets` needed may vary; testing or checking compatibility with the installed JupyterLab version is recommended

## General Learning
- Upgrading packages can lead to dependency issues
- Keeping logs of package versions can help diagnose problems
- Downgrading specific packages can resolve compatibility issues

## Next Steps
- Verify the compatibility of `traitlets` with the current JupyterLab version
- Test the downgraded version to ensure the issue is resolved
- Document the compatible versions for future reference
---

### 42327286_python2.7%20auf%20testfront.md
# Ticket 42327286

 ```markdown
# HPC Support Ticket: Python 2.7 Installation on testfront

## Keywords
- Python 2.7
- testfront
- icc
- iaca
- module add

## Summary
A user requested the installation of Python 2.7 on the testfront machine, noting that it is the only machine where both icc and iaca work simultaneously.

## Root Cause
The user needed Python 2.7 installed on the testfront machine to utilize both icc and iaca functionalities.

## Solution
The HPC Admin provided the command to add the Python 2.7 module:
```bash
module add python/2.7.1
```

## General Learnings
- Users may require specific software versions to be installed on particular machines for compatibility reasons.
- The `module add` command can be used to load specific software versions.
- The testfront machine is noted for its compatibility with both icc and iaca.
```
---

### 2023082842003292_Pfadabh%C3%83%C2%A4ngigkeitsproblem.md
# Ticket 2023082842003292

 ```markdown
# HPC-Support Ticket: Pfadabhängigkeitsproblem

## Problem Description
- **User Issue**: The user is experiencing issues with importing a script (`aws2cosipyConfig.py`) within another script (`aws2cosipy.py`) while working with a glacier model (COSIPY).
- **Symptoms**: The `aws2cosipyConfig.py` script is being imported from an unexpected directory.
- **Details**: The user added a path to `sys.path` but the script is still being imported from a different location.

## Keywords
- Python import error
- Path dependency
- sys.path
- COSIPY
- Glacier model

## Root Cause
- The user's script is importing a module from a different directory due to overlapping paths in `sys.path`.
- The `sys.path` contains paths from both the user's directory and another user's directory, leading to confusion in the import process.

## Solution
- **HPC Admin Suggestion**: The HPC Admin suggested a Zoom call to better understand the directory structure and resolve the path conflict.
- **Potential Fix**: Ensure that the correct path is prioritized in `sys.path` by either removing conflicting paths or reordering them.

## General Learning
- **Path Management**: Understanding how Python manages paths in `sys.path` is crucial for avoiding import conflicts.
- **Debugging Imports**: Using `print(sys.path)` can help identify where Python is looking for modules.
- **Collaboration**: Sometimes, a direct conversation (e.g., via Zoom) can help resolve complex issues more efficiently.

## Conclusion
- The issue highlights the importance of managing Python paths correctly to avoid import conflicts, especially when working with shared or copied code.
```
---

### 2022032842001821_Help%20for%20Singularity%20Permision%20Denied.md
# Ticket 2022032842001821

 # HPC-Support Ticket: Help for Singularity Permission Denied

## Keywords
- Singularity
- Permission Denied
- Executable Script
- Shebang Line
- Python Script

## Problem Description
- User is a master student working on a deep learning project using FAU's HPC.
- User encounters "permission denied" error when trying to run a Docker container on TinyGPU.

## Root Cause
- The script (`script.py`) being run inside the Singularity container is not executable.
- The script may lack a shebang line to specify the interpreter.

## Solution
- Make the script executable using `chmod +x script.py`.
- Add a shebang line at the top of the script to specify the interpreter, e.g., `#!/usr/bin/env python`.

## General Learnings
- Ensure scripts inside containers are executable.
- Add shebang lines to scripts to specify the interpreter.
- Understand the internal workings of the container to diagnose permission issues accurately.

## Roles Involved
- **HPC Admins**: Provided guidance on making the script executable and adding a shebang line.
- **User**: Reported the issue and provided a screenshot of the commands.

## Next Steps
- User should make the script executable and add the shebang line.
- If the issue persists, further investigation into the container's internal processes may be required.
---

### 42339579_Python3%20mit%20SSL%20Support.md
# Ticket 42339579

 # HPC Support Ticket: Python3 mit SSL Support

## Keywords
- Python3
- SSL Support
- OpenSSL-dev
- setuptools
- pip
- SSLContext
- urllib3
- InsecurePlatformWarning
- locale encoding

## Summary
A user reported that the Python3 installation on the HPC system lacked SSL support, which was causing issues with using `pip` and `setuptools`. The user requested a recompilation of Python3 with OpenSSL-dev to enable SSL tools.

## Root Cause
- The user was experiencing issues with SSL support in both Python3 and Python2.7.
- The `pip` tool was not functioning correctly due to missing SSLContext and locale encoding issues.

## Solution
- The HPC Admin confirmed that the Python-internal SSL module was already included and that `import ssl` worked without errors.
- The HPC Admin added the `setuptools-15.0` and `pip-6.1.1` packages to the Python3 installation.
- The user was advised to try again after some directory permissions were adjusted.
- The user confirmed that the solution worked and the issues were resolved.

## Lessons Learned
- Ensure that Python installations on the HPC system include SSL support.
- Verify that essential packages like `setuptools` and `pip` are included in the Python modules.
- Check directory permissions to ensure users have the necessary access.
- Address locale encoding issues if they arise during the use of Python tools.

## Conclusion
The issue was resolved by adding the necessary packages to the Python installation and adjusting directory permissions. The user confirmed that the solution worked, and the SSL support issues were resolved.
---

### 2022011842001611_Fwd%3A%20Trilinos%20%C3%A2%C2%80%C2%93%20Test%20installation%2C%20Bspcode%20Eigensolver.md
# Ticket 2022011842001611

 # HPC Support Ticket: Trilinos Installation Issues

## Keywords
- Trilinos
- Spack
- Python
- OpenPBS
- Doxygen
- Quota
- MPI
- Slurm
- Torque
- Ubuntu
- AMD Epyc CPUs

## Summary
The user encountered issues while installing Trilinos using Spack. The primary problems were related to Python version conflicts, Doxygen version bugs, and quota issues.

## Root Cause
1. **Python Version Conflict**: OpenPBS requires Python 2, while Trilinos requires Python 3.
2. **Doxygen Bug**: The version of Doxygen on the system has a known bug that affects PyTrilinos.
3. **Quota Issue**: The user encountered a 'No space left on device' error despite not exceeding their quota.

## Solutions
1. **Python Version Conflict**:
   - Upgrade to Spack v0.17, where OpenPBS is built with Python 3.
   - Alternatively, configure Spack to use the existing Torque installation as an external OpenPBS.

2. **Doxygen Bug**:
   - Use a different version of Doxygen that does not have the bug affecting PyTrilinos.

3. **Quota Issue**:
   - The exact cause of the quota issue was not resolved in the conversation. Further investigation is needed to determine why the 'No space left on device' error occurs despite available quota.

## Additional Notes
- The user also inquired about running Trilinos on AMD Epyc 7502 CPUs and executing Trilinos-specific tests during the Spack installation.
- The HPC Admin mentioned that upgrading Spack to v0.17.1 on older clusters might not be feasible due to upcoming system changes and decommissioning of certain clusters.

## Future Actions
- Consider upgrading Spack to v0.17.1 on relevant clusters.
- Address the quota issue by investigating the 'No space left on device' error.
- Provide guidance on running Trilinos-specific tests during Spack installation.

## Conclusion
The ticket highlights common issues encountered during software installation on HPC systems, including version conflicts, software bugs, and quota management. It also underscores the importance of keeping software packages up to date and considering system-specific configurations.
---

### 2021071242002014_gdal%20library%20-%20python%20support%20Anfrage.md
# Ticket 2021071242002014

 ```markdown
# HPC-Support Ticket Conversation: gdal Library - Python Support

## Keywords
- gdal library
- python support
- gdal_merge.py
- conda environment
- frontend
- job nodes
- permissions
- woody-ng

## Summary
The user requested the installation of the gdal library with Python support on the HPC system to use the `gdal_merge.py` tool for merging raster datasets. The HPC admins discussed the feasibility and potential issues, including dependencies and permissions.

## Root Cause of the Problem
- The gdal library was installed without Python support, preventing the use of `gdal_merge.py`.
- The user encountered permission issues when trying to create a conda environment.

## Solutions and Steps Taken
1. **Initial Request**:
   - The user requested the installation of `python-gdal` on the frontend and job nodes to enable the use of `gdal_merge.py`.

2. **Admin Response**:
   - The HPC admin suggested using a conda environment to install `gdal` with Python support.
   - The admin provided instructions to configure conda to use the user's space for packages and environments.

3. **User Follow-up**:
   - The user encountered permission issues when trying to create a conda environment.
   - The user requested further assistance with the permission issue.

4. **Admin Follow-up**:
   - The admin suggested configuring conda to use a different directory for packages and environments.
   - The admin confirmed that the user needs to load the Python module and activate the conda environment in job scripts.

## Final Solution
- The user was advised to configure conda to use a directory within their user space for packages and environments.
- The user was instructed to load the Python module and activate the conda environment in their job scripts to use `gdal_merge.py`.

## General Learning
- **Conda Environment**: Using conda environments can be a flexible solution for installing specific software dependencies without system-wide changes.
- **Permissions**: Users may need to configure conda to use directories within their user space to avoid permission issues.
- **Job Scripts**: Ensure that job scripts load the necessary modules and activate the required conda environments.

## Conclusion
The issue was resolved by configuring conda to use the user's space for packages and environments, and by instructing the user to load the Python module and activate the conda environment in their job scripts.
```
---

### 2023101042002437_Installation%20python3.8-venv%20auf%20cshpc.md
# Ticket 2023101042002437

 ```markdown
# HPC-Support Ticket: Installation python3.8-venv auf cshpc

## Keywords
- python3.8-venv
- cshpc
- grid
- py-venv
- python-venv
- python-pip

## Summary
A user requested the installation of the "python3.8-venv" package on cshpc. The HPC Admin noted that py-venv is not desired on cshpc and suggested installing it on the grid instead. The ticket was eventually closed as the request was resolved.

## Root Cause
- User requested a specific Python package (python3.8-venv) on cshpc.

## Solution
- HPC Admin suggested installing the package on the grid instead of cshpc.
- The ticket was closed as the request was resolved.

## Lessons Learned
- Certain packages may not be suitable for installation on specific HPC systems (e.g., cshpc).
- Alternative installation locations (e.g., grid) should be considered.
- Communication between HPC Admins and users is crucial for resolving requests efficiently.
```
---

### 2025022742003596_fviz1%20VNC%20Session%20hat%20kein%20%22module%22-Kommando.md
# Ticket 2025022742003596

 ```markdown
# HPC-Support Ticket: VNC Session Missing "module" Command

## Keywords
- VNC Session
- Module Command
- Remote Session
- Terminal
- Login Shell
- `bash -l`
- `.bashrc`
- `xfce4-terminal`

## Problem Description
The user reported that the "module" command was not available within a remote VNC session on `fviz1`. Although modules loaded before starting the session remained available, the user could not modify them during the session.

## Root Cause
The issue was likely due to the terminal not starting as a login shell, which prevented the necessary environment variables and configurations from being loaded.

## Solution
- **Immediate Fix**: Running `bash -l` in the terminal should load the necessary configurations and make the "module" command available.
- **Permanent Fix**: Ensure that the terminal starts as a login shell. For `xfce4-terminal`, this can be configured in the preferences.

## Additional Notes
- The HPC Admin suggested that the user's `~/.bashrc` might include a `source /etc/bashrc` line or other configurations that ensure the module command is available.
- Documentation should be updated to include this solution for future reference.

## Conclusion
The problem was resolved by starting the terminal as a login shell using `bash -l`. This ensures that the necessary configurations are loaded, making the "module" command available within the VNC session.
```
---

### 2022032542002479_Installing%20PyTorch%201.11.0%20and%20Cuda%2011.3.md
# Ticket 2022032542002479

 # HPC Support Ticket: Installing PyTorch 1.11.0 and CUDA 11.3

## Subject
- Installing PyTorch 1.11.0 and CUDA 11.3 on the Alex cluster

## User Issue
- User attempted to create a virtual environment using Conda but encountered an error:
  ```
  Collecting package metadata (current_repodata.json): failed
  NoWritablePkgsDirError: No writeable pkgs directories configured.
  - /apps/python/3.9-anaconda/pkgs
  ```

## Root Cause
- The error occurred because the user tried to install packages in a directory where they did not have write permissions.

## HPC Admin Discussion
- HPC Admins discussed the compatibility of CUDA versions and decided not to install outdated versions on the new system.
- The error was identified as a configuration issue with Conda.

## Solution
- The user was advised to run the following command to configure Conda correctly:
  ```
  conda config --add pkgs_dirs $WOODYHOME/.conda/pkgs
  ```

## Keywords
- PyTorch 1.11.0
- CUDA 11.3
- Conda
- Virtual Environment
- NoWritablePkgsDirError
- Configuration

## General Learnings
- Ensure that Conda is configured correctly to avoid permission issues when installing packages.
- Avoid installing outdated software versions on new systems unless absolutely necessary.
- Always check for compatibility issues when dealing with different versions of software.
---

### 2024071242002894_Python%20environment%20is%20not%20working.md
# Ticket 2024071242002894

 # HPC Support Ticket: Python Environment Not Working

## Subject
Python environment is not working

## User Issue
- User is unable to plot in Python after loading the `python3.9` Anaconda module on Fritz.
- Error message:
  ```
  qt.qpa.plugin: Could not find the Qt platform plugin "xcb" in ""
  This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.
  Aborted (core dumped)
  ```

## Troubleshooting Steps
1. **Reinstall Matplotlib**:
   - User attempted to uninstall and reinstall Matplotlib but encountered errors due to read-only file system issues.
   - HPC Admin suggested using `pip install --user matplotlib`.

2. **Check System**:
   - User confirmed they are on Fritz (iwst087h).
   - HPC Admin verified that Matplotlib works with Python 3.9 on Fritz without issues.

3. **Recreate Environment**:
   - HPC Admin suggested recreating the entire Python environment as `pip` does not remove dependencies when uninstalling packages.
   - User confirmed that something was broken in their local Python library path (`$HOME/.local/lib/pythonX.Y`).

## Solution
- User deleted the local Python library path and reinstalled the required packages, which resolved the issue.

## Keywords
- Python environment
- Matplotlib
- Qt platform plugin
- Anaconda module
- Fritz
- pip install --user
- Recreate environment

## General Learnings
- Issues with Python environments can often be resolved by recreating the environment.
- Local Python library paths can cause conflicts and should be checked when encountering issues.
- The `pip install --user` command can be used to install packages in the user's home directory, avoiding permission issues.

## Root Cause
- Broken dependencies or conflicts in the local Python library path.

## Solution Found
- Deleting the local Python library path and reinstalling the required packages resolved the issue.
---

### 2022090642002486_Help%20with%20library%20installation.md
# Ticket 2022090642002486

 # HPC Support Ticket: Help with Library Installation

## Keywords
- Library installation
- Python libraries
- TensorFlow
- Pathlib
- TinyGPU
- HPC documentation
- HPC Café

## Summary
A user requested help with installing Python libraries (TensorFlow and Pathlib) on the HPC system. The user was not aware of the procedure involved.

## Root Cause
- Lack of specific details in the initial request.
- User unfamiliarity with the library installation procedure on HPC.

## Solution
- The HPC Admin provided relevant documentation links:
  - [HPC Documentation](https://hpc.fau.de/)
  - [Getting Started Guide](https://hpc.fau.de/systems-services/documentation-instructions/getting-started/)
  - [TinyGPU Cluster](https://hpc.fau.de/systems-services/documentation-instructions/clusters/tinygpu-cluster/)
  - [Python and Jupyter](https://hpc.fau.de/systems-services/documentation-instructions/special-applications-and-tips-tricks/python-and-jupyter/)
  - [TensorFlow and PyTorch](https://hpc.fau.de/systems-services/documentation-instructions/special-applications-and-tips-tricks/tensorflow-pytorch/)
- The user was advised to attend the upcoming HPC Café for further assistance.

## General Learnings
- Always provide specific details when requesting support.
- Utilize the provided documentation and resources for common tasks.
- Attend introductory sessions or workshops (like HPC Café) for hands-on help and guidance.

## Next Steps
- The user will review the provided documentation and attend the HPC Café for further assistance.
- The ticket was closed after providing the necessary resources.
---

### 2025010842002642_Anfrage%20neuere%20Python%20version%20auf%20Meggie.md
# Ticket 2025010842002642

 ```markdown
# HPC-Support Ticket: Request for Newer Python Version on Meggie

## Keywords
- Python version
- Conda
- Environment
- Module
- Proxy

## Problem
- User requires Python 3.12 for their Master's thesis project, but the current version available is 3.9.

## Solution
- Use Conda to create an environment with Python 3.12.
- Steps:
  1. Load the Anaconda module:
     ```bash
     module load python/3.9-anaconda
     ```
  2. Create a Conda environment with Python 3.12:
     ```bash
     conda create --name envname python==3.12
     ```
  3. Activate the environment:
     ```bash
     conda activate envname
     ```
  4. Install necessary packages using `pip` or `conda`.
  5. Set the proxy if needed:
     ```bash
     export https_proxy="http://proxy.rrze.uni-erlangen.de:80"
     ```

## General Learnings
- Conda can be used to manage different Python versions and environments.
- Proper module loading and environment setup are crucial for using specific software versions.
- Proxy settings may be necessary for network-related operations.
```
---

### 2024092642005218_Installation%20of%20PyTorch%20failed.md
# Ticket 2024092642005218

 # HPC-Support Ticket: Installation of PyTorch Failed

## Subject
Installation of PyTorch failed

## User
Master student at FAU Erlangen (chair of energy engineering)

## Problem
- Initial installation of PyTorch failed due to missing proxy settings.
- Conflicts during installation of PyTorch and other packages.
- Installation of pandas, numpy, and matplotlib failed with conflicts.

## Root Cause
- Proxy settings were not configured correctly.
- Conflicts between packages during installation.

## Solution
1. **Set Proxy Settings**:
   ```bash
   export https_proxy="http://proxy.rrze.uni-erlangen.de:80"
   export https_proxy="http://proxy.rrze.uni-erlangen.de:80"
   ```
   Refer to [documentation](https://doc.nhr.fau.de/environment/python-env/?h=proxy) for more details.

2. **Create a New Conda Environment**:
   - Create a new environment to avoid conflicts with existing packages.

3. **Install Packages Using pip**:
   - Use `pip install` for Python packages to avoid conflicts that may arise with `conda install`.

## Key Points Learned
- **Proxy Settings**: Essential for accessing external repositories.
- **Package Management**: `pip install` can be used to avoid conflicts that may occur with `conda install`.
- **Environment Management**: Creating a new environment can help resolve conflicts with existing packages.

## Additional Notes
- The behavior of `conda` and `pip` is the same on the HPC system as on a local system.
- Use `conda install` for base packages and `pip install` for Python packages to minimize conflicts.

## References
- [PyTorch Installation Test](https://doc.nhr.fau.de/apps/pytorch/)
- [Proxy Settings Documentation](https://doc.nhr.fau.de/environment/python-env/?h=proxy)

## Support Team
- **HPC Admins**: Provided guidance on proxy settings and package management.
- **2nd Level Support Team**: Assisted with troubleshooting and resolving package conflicts.

## Conclusion
The issue was resolved by setting the correct proxy settings and using `pip install` for Python packages to avoid conflicts. Creating a new Conda environment also helped in resolving package conflicts.
---

### 2023071142001693_Regarding%20resetting%20my%20account.md
# Ticket 2023071142001693

 # HPC Support Ticket: Resetting Account and Installing Libraries

## Keywords
- Account reset
- Python libraries
- Dependency issues
- Installation errors
- Proxy settings
- Conda environment

## Summary
A user requested an account reset due to incompatible library versions. The HPC admin provided an alternative solution to manually remove specific directories. The user then encountered issues installing `basicsr` and `realesrgan` libraries, which the admin addressed by providing a step-by-step installation guide using Conda.

## Root Cause of the Problem
- Incompatible library versions causing dependency issues.
- Installation errors due to connection failures and environment setup issues.

## Solution
### Account Reset Alternative
- **Manual Removal of Directories**: Delete `.local`, `.conda`, `.cache`, and `.config` in the user's home directory to remove all Python files.

### Library Installation
- **Environment Setup**:
  ```bash
  salloc.tinygpu --gres=gpu:1 --time=02:00:00
  module load python cuda
  conda create -n basu python
  conda activate basu
  pip install basicsr realesrgan
  ```
- **Note**: The installation step for `basicsr` and `realesrgan` may take approximately 20 minutes.

## General Learnings
- HPC admins do not reset accounts but provide alternative solutions for cleaning up user environments.
- Proper environment setup and dependency management are crucial for successful library installations.
- Using Conda environments can help manage dependencies and avoid conflicts.

## Additional Notes
- Ensure that the actual error message is provided for more accurate troubleshooting.
- Proxy settings may need to be configured correctly for successful installations.
---

### 2023062342000744_question%20-%20user%20b178bb11.md
# Ticket 2023062342000744

 # HPC Support Ticket Analysis

## Keywords
- Miniconda
- Conda init
- .bashrc
- .bash_profile
- scp
- Network unreachable

## Issues and Solutions

### Issue 1: Conda not initializing automatically
- **Root Cause**: Conda initialization script not being executed automatically on login.
- **Solution**:
  - Ensure that the login shell is called with the `-l` flag.
  - Create a `.bash_profile` if it does not exist, with the following content:
    ```bash
    if [ -f ~/.bashrc ]; then . ~/.bashrc; fi
    ```
  - Source the `.bashrc` file manually if needed.

### Issue 2: Unable to copy files using scp
- **Root Cause**: Incorrect hostname and attempting to copy from a non-public IP outside the FAU network.
- **Solution**:
  - Use the correct hostname `cshpc.rrze.fau.de` for the HPC cluster.
  - Ensure that the source IP is within the FAU network or use a public IP.

## General Learnings
- Proper configuration of shell startup files (`.bashrc`, `.bash_profile`) is crucial for automatic initialization of tools like Conda.
- Accurate hostnames and network configurations are essential for successful file transfers using scp.
- Understanding network reachability is important for troubleshooting connectivity issues.

## References
- [Bash Startup Files](https://www.gnu.org/software/bash/manual/html_node/Bash-Startup-Files.html)
- [FAU HPC Support](https://hpc.fau.de/)
---

### 2023031442001721_Tier3-Access-Alex%20%22Oskar%20Herrmann%22%20_%20gwgi026h.md
# Ticket 2023031442001721

 # HPC Support Ticket: Conda Environment Creation Issue

## Keywords
- Conda
- NoWritablePkgsDirError
- HPC Account Enablement
- GPU Cluster
- Python
- TensorFlow

## Summary
A user encountered an error while trying to create a new conda environment on an HPC cluster. The error message indicated that there were no writeable package directories configured.

## Root Cause
The user did not have a writeable package directory configured for conda.

## Solution
The HPC Admin suggested configuring writeable package and environment directories using the following commands:
```bash
conda config --add pkgs_dirs $WORK/conda/pkgs
conda config --add envs_dirs $WORK/conda/envs
```

## General Learnings
- After enabling an HPC account, users might need to configure certain software tools.
- Conda requires writeable package and environment directories to create new environments.
- The `conda config` command can be used to add writeable directories.

## Roles Involved
- HPC Admins
- User (requester)

## Related Software and Tools
- Python
- Conda
- TensorFlow

## Related Hardware
- Nvidia A100 GPGPUs

## Related HPC Cluster
- Alex (GPU cluster)
---

### 2022091242002812_Fw%3A%20%5BRRZE-HPC%5D%20Failure%20of%20Emmy%20_%20limited%20availability%20of%20Meggie.md
# Ticket 2022091242002812

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Keywords
- OS upgrade
- AlmaLinux8
- Conda environment
- Permission error
- NoWritablePkgsDirError
- Infiniband network failure
- Batch processing
- $FASTTMP
- Hardware issues
- DIY repair

## General Learnings
- **OS Upgrade Impact**: Upgrading the OS can lead to issues with software configurations, such as Conda environments.
- **Conda Configuration**: Conda environments may require specific directory configurations for package management.
- **Hardware Issues**: Hardware failures can lead to significant downtime and require specialized repairs.
- **User Communication**: Effective communication with users is crucial during system upgrades and hardware failures.

## Root Cause of the Problem
- **Conda Environment Issue**: The user encountered a permission error when creating new Conda environments due to missing writeable package directories.

## Solution
- **Conda Configuration**: The issue was resolved by adding a package directory using the command:
  ```bash
  conda config --add pkgs_dirs $WOODYHOME/.conda/pkgs
  ```

## Additional Notes
- **Infiniband Network Failure**: Emmy's Infiniband network failure led to unavailability for batch processing and $FASTTMP access.
- **Hardware Repair**: Meggie's $FASTTMP was unavailable due to hardware issues, requiring a DIY repair by the electronics workshop.
- **Beta Testing**: The OS upgrade to AlmaLinux8 required beta testing and recompilation of application software.
```
---

### 2025022742003345_Re%3A%20MI300X-Frage.md
# Ticket 2025022742003345

 # HPC Support Ticket: TensorFlow Installation Issue on MI300X Node

## Keywords
- TensorFlow
- Horovod
- MPI
- ROCm
- MI300X
- Container
- Docker
- Software Installation

## Problem Description
The user encountered issues while attempting to install TensorFlow on the MI300X node. They were looking for a container with TensorFlow2, Horovod, and MPI that is compatible with ROCm version 6.8.5.

## Ticket Conversation Summary
- User requested assistance with finding a compatible container for TensorFlow2, Horovod, and MPI.
- Initial contact forwarded the request to HPC experts.
- HPC Admin suggested checking Docker Hub for ROCm containers.
- User eventually resolved the issue by rewriting the benchmark in PyTorch with additional features.

## Root Cause
The user faced compatibility issues with TensorFlow2, Horovod, and MPI on the MI300X node with ROCm version 6.8.5.

## Solution
- The user rewrote the benchmark in PyTorch, which resolved the compatibility issues.
- HPC Admin suggested checking Docker Hub for ROCm containers as a potential solution.

## Lessons Learned
- When encountering software installation issues, consider checking Docker Hub for compatible containers.
- Rewriting the benchmark in a different framework (e.g., PyTorch) can be a viable solution to compatibility problems.
- Forwarding requests to the appropriate experts can help in resolving complex issues.

## Status
The ticket was closed as the user found an alternative solution by rewriting the benchmark in PyTorch.
---

### 2024011542001293_Re%3A%20Module%20Loading%20Error%20in%20Python%20Environment%20on%20HPC%20System.md
# Ticket 2024011542001293

 # HPC Support Ticket: Module Loading Error in Python Environment

## Keywords
- Module loading error
- Python 3.10 Anaconda
- HPC system
- SSH connection
- Jump host configuration

## Summary
A user encountered an error while loading the Python 3.10 Anaconda module on the HPC system. The error message indicated an invalid command name "source-sh". The issue was related to the user connecting to the wrong system.

## Root Cause
- The user was attempting to load a Python module on a system (cshpc) that did not have the required module.
- The user was unaware of the correct system to connect to for their specific needs (TinyGPU).

## Solution
- The user was advised to connect to the correct system (tinyx.nhr.fau.de) using either a jump host configuration or by running the SSH command from cshpc.
- Documentation links were provided for building Python packages and additional support.

## Lessons Learned
- Always verify the system you are connected to when encountering module loading errors.
- Use the correct SSH commands and configurations to connect to the appropriate HPC system.
- Refer to documentation and seek help from supervisors or support teams when needed.

## Relevant Documentation
- [Python and Jupyter Documentation](https://hpc.fau.de/systems-services/documentation-instructions/special-applications-and-tips-tricks/python-and-jupyter/)
- [TensorFlow and PyTorch Documentation](https://hpc.fau.de/systems-services/documentation-instructions/special-applications-and-tips-tricks/tensorflow-pytorch/)

## Support Contacts
- HPC Admins: For system-specific issues and configurations.
- 2nd Level Support Team: For additional technical support and troubleshooting.
- Software and Tools Developers: For assistance with software-related issues.
---

### 42320726_python3.md
# Ticket 42320726

 # HPC Support Ticket: Python3 Request

## Keywords
- Python3
- Anaconda
- NumPy
- Module Avail
- Woody

## Problem
- User requires Python3 for analysis but cannot find it in `module avail`.
- Unsure whether to install Python3 in home directory or if it's already available.

## Solution
- HPC Admin informs the user about the availability of `python/3.4-anaconda` on Woody.
- User confirms the need for additional Python packages like NumPy.
- HPC Admin confirms that NumPy is included in the provided Python module.

## General Learnings
- Always check with HPC Admin for available software modules before attempting personal installations.
- Additional packages can be requested and may already be included in provided modules.
- Communication with HPC Admin is essential for resolving software availability issues.

## Root Cause
- User was unaware of the available Python3 module and required additional packages.

## Resolution
- HPC Admin provided the necessary Python3 module with the required packages, resolving the user's issue.
---

### 2024060942001643_Startup%20script%20running%20infinitely%2C%20needs%20to%20be%20reset.md
# Ticket 2024060942001643

 # HPC Support Ticket: Startup Script Running Infinitely

## Keywords
- Startup script
- Infinite loop
- Permission denied
- Executable permissions
- Environment variables
- Python module
- `.bashrc`
- `.bash_profile`

## Problem Description
- **User Issue**: The user set up a startup script (`startup_commands.sh`) to load a Python module on login. The script was added to `.bashrc`, causing it to run infinitely and preventing terminal access.
- **Root Cause**: The script was likely causing an infinite loop due to improper handling of the script's execution within `.bashrc`.

## Troubleshooting Steps
1. **Initial Fix**: The user removed the `startup_commands.sh` file using WinSCP to regain terminal access.
2. **Permission Error**: After adding error handling to the script and making it executable with `chmod +x`, the script still ran infinitely without error messages.

## Solution
- **Environment Variables**: The user wanted to avoid manually setting environment variables and loading the Python module at each login.
- **Suggested Approach**:
  - Use a virtual environment (`venv` or `conda`) to manage Python dependencies.
  - Add environment variables and module loading commands directly to `.bashrc` or `.bash_profile` without using a separate script.

## Example Setup
```bash
# .bash_profile
if [ -e ~/.bashrc ]; then
    . ~/.bashrc
fi

# .bashrc
if [[ $- != *i* ]]; then
    return
fi

export HISTSIZE=100000
export HISTFILESIZE=100000
export HISTCONTROL=ignoredups
export CLICOLOR=1
export EDITOR=vim

# Add environment variables and module loading commands here
export http_proxy="http://proxy:80"
export https_proxy="http://proxy:80"
module add python
pip3 install torch torchvision torchaudio
```

## Conclusion
- **Lesson Learned**: Avoid using separate startup scripts that can cause infinite loops. Instead, directly add necessary commands to `.bashrc` or `.bash_profile`.
- **Best Practice**: Use virtual environments for managing Python dependencies to avoid conflicts and ensure reproducibility.

## References
- [Python Environments Documentation](https://doc.nhr.fau.de/environment/python-env/)
---

### 2021090742002226_Conda%20enviroment.md
# Ticket 2021090742002226

 # HPC Support Ticket: Conda Environment Issue

## Keywords
- Conda environment
- PackagesNotFoundError
- Module load
- Anaconda
- WORK directory

## Problem Description
- User encountered `PackagesNotFoundError` while trying to clone a Conda environment.
- The error message indicated that certain packages were not available from current channels.
- User had previously succeeded in creating Conda environments without issues.

## Root Cause
- The exact root cause was not determined in the provided conversation.
- Possible causes include expired certificates, missing module loads, or changes in package availability.

## Steps Taken by User
- User attempted to clone a Conda environment using Anaconda installed in their WORK directory.
- The exact command lines and steps were not provided in the initial message.

## HPC Admin Response
- Requested detailed steps and commands used by the user.
- Asked which system (woody/emmy/meggie) the user was using.
- Inquired about any modules loaded (e.g., `module load python`).

## Solution
- No solution was provided in the conversation as the ticket was closed due to awaiting a response from the user.

## General Learnings
- Always provide detailed steps and commands when reporting issues.
- Ensure that necessary modules are loaded before running commands.
- Check for any recent changes in package availability or system updates.

## Next Steps
- If the issue persists, verify the availability of the required packages in the current channels.
- Consider loading specific modules that might be necessary for the operation.
- Check for any system updates or changes that might affect package availability.
---

### 2017081542001776_python%20vtk.md
# Ticket 2017081542001776

 # HPC Support Ticket: Python VTK Installation

## Keywords
- Python
- VTK
- Anaconda
- Modules
- 3rd-Party Repositories

## Summary
A user requested the installation of the VTK (Visualization Toolkit) package for the existing Python distributions on the HPC cluster.

## Problem
- User needed VTK for Python 2.7 and Python 3.5/3.6 distributions.
- Initial request was for Python 2.7.

## Solution
- HPC Admins installed VTK for the `python/2.7-anaconda` module.
- User requested VTK for `python/3.5-anaconda` as well.
- HPC Admins informed that VTK is not available for Python 3.6 in the official Anaconda repository.
- User mentioned they were able to install VTK for Python 3.6 using the `conda-forge` repository on their personal PC.
- HPC Admins clarified that 3rd-party repositories are not enabled on the central Anaconda installation due to quality, security, and reproducibility concerns.
- User was advised to install a private Anaconda environment in their home directory if needed.

## Lessons Learned
- Users may request specific packages for different Python versions.
- Official repositories may not always have the required packages.
- 3rd-party repositories can be a solution but come with risks.
- Users can be advised to set up private environments if central installations have limitations.

## References
- [Anaconda Packages Documentation](https://docs.continuum.io/anaconda/packages/pkg-docs)
- [Conda-Forge VTK Package](https://anaconda.org/conda-forge/vtk)

## Conclusion
The user's request for VTK in Python 2.7 was fulfilled. For Python 3.5/3.6, the user was advised to use a private Anaconda installation due to the limitations and policies of the central installation.
---

### 2018111242001442_Probleme%20mit%20Installation%20von%20Paket%20aus%20Bioconda%20_%20mfch000h.md
# Ticket 2018111242001442

 ```markdown
# HPC Support Ticket Conversation: Probleme mit Installation von Paket aus Bioconda / mfch000h

## Problem
- User tried to install `mageck-vispr` from Bioconda repository on Woody.
- Error message: `PermissionError: [Errno 13] Permission denied: '/apps/python/3.6-anaconda/.condatmp'`.

## Root Cause
- The user attempted to install the package directly into the central Anaconda installation, which is read-only.

## Solution
- Use Conda environments to avoid writing to the central Anaconda installation.
- Example commands:
  ```bash
  conda create -n mageck-vispr mageck-vispr
  source activate mageck-vispr
  ```
- Alternatively, download and install Miniconda to create a separate environment.

## Additional Information
- The user also encountered issues with NoMachine client proxy configuration.
- Solution: Use SSH protocol instead of the default NX protocol in NoMachine.

## Keywords
- Conda, Bioconda, PermissionError, Miniconda, NoMachine, SSH, Proxy Configuration

## General Learning
- Always use Conda environments to avoid permission issues with central installations.
- Ensure proper protocol selection in NoMachine to avoid proxy configuration issues.
```
---

### 2022092742004391_error%20loading%20python%20module.md
# Ticket 2022092742004391

 # HPC Support Ticket: Error Loading Python Module

## Keywords
- Python module error
- `module: command not found`
- HPC account sharing
- Visual Studio Code settings
- Interactive login shell

## Summary
A user encountered an error when trying to load the Python module on an HPC system after a switch to NHR. The error message was `bash: module: command not found`.

## Root Cause
1. **Account Sharing**: The user was using an HPC account that did not belong to them, which is against the usage policies.
2. **Incorrect Python Path**: The path `/apps/python/3.8-anaconda` did not exist on the system; the correct path was `/apps/python/3.9-anaconda`.
3. **Module Initialization**: The `module` command was not being initialized, likely due to the user's Visual Studio Code settings not starting an interactive login shell.

## Solution
1. **Account**: The user was advised to apply for a separate HPC account for their thesis work.
2. **Python Path**: The user was informed about the correct Python path.
3. **Module Initialization**: The user was advised to configure their Visual Studio Code settings to start an interactive login shell, which would initialize the `module` command.

## General Learnings
- Ensure users have their own HPC accounts to avoid policy violations.
- Verify the correct paths for software modules.
- Check that the user's development environment is configured to start an interactive login shell to initialize necessary commands.

## Next Steps
- Guide the user through the process of applying for a new HPC account.
- Provide instructions on how to configure Visual Studio Code to start an interactive login shell.
- Update documentation to include common issues with module initialization and software paths.
---

### 2023060142003489_Profiling%20a%20python%20code.md
# Ticket 2023060142003489

 ```markdown
# HPC-Support Ticket Conversation: Profiling a Python Code

## Subject: Profiling a Python script

### User Issue:
- User wants to profile a Python script (`transformer.py`) using `py-spy` and `pycallgraph`.
- User follows these steps:
  - Loads necessary modules: `python/3.9-anaconda`, `cuda`, `nvhpc`.
  - Allocates resources using `salloc`.
  - Runs the script successfully with `python transformer.py`.
- User encounters issues when trying to profile the script:
  - `py-spy` and `pycallgraph` commands are not found.
  - User installs `py-spy` using `pip`, but the command is still not recognized.
  - User attempts to create a new conda environment but encounters permission errors.

### HPC Admin Response:
- Suggests using conda to install `py-spy` in a new virtual environment.
- Provides a link to learn about virtual environments in Anaconda.
- Suggests configuring package and environment directories using `conda config`.
- Provides a workaround for internet access issues on cluster nodes by setting a proxy.

### User Follow-up:
- User attempts to create a new conda environment and install `py-spy` but encounters permission errors.
- User tries to run `pycallgraph` but encounters an error because the `dot` command is not found in the path.

### HPC Admin Response:
- Suggests installing `pygraphviz` in the existing conda environment.
- Provides a command to create a new conda environment with `pycallgraph2` and `pygraphviz`.

### Key Learnings:
- **Virtual Environments**: Using virtual environments in Anaconda can help manage dependencies and avoid permission issues.
- **Conda Configuration**: Configuring package and environment directories can resolve permission errors when creating or modifying conda environments.
- **Proxy Settings**: Setting a proxy can help with internet access issues on cluster nodes.
- **Graphviz Dependency**: `pycallgraph` requires the `dot` command from Graphviz to be in the system path.

### Solution:
- Create a new conda environment with the necessary packages:
  ```bash
  conda create -n pycallgraph2 -c conda-forge pygraphviz pycallgraph2
  ```
- Ensure the `dot` command is available in the system path.
```
---

### 2022122842000314_Switch%20back%20to%20python_3.8-anaconda.md
# Ticket 2022122842000314

 # HPC Support Ticket: Switch back to python/3.8-anaconda

## Keywords
- Python version
- Conda environment
- Module availability
- JupyterHub
- Virtual environment

## Problem Description
The user wants to run Python scripts on the HPC system "woody," but the required Python modules are not available, leading to execution interruptions. The scripts run successfully in the JupyterHub terminal. The user can only see `python/3.9-anaconda` on woody and `python/3.8-anaconda` on JupyterHub. Attempting to load `python/3.8-anaconda` on woody results in an error.

## Root Cause
The required Python version (`python/3.8-anaconda`) is not available as a module on woody.

## Solution
Use a Conda environment to specify the desired Python version.

### Steps
1. Load the available Python module:
   ```sh
   module load python/3.9-anaconda
   ```
2. Create a new Conda environment with the specific Python version:
   ```sh
   conda create -n YOUR_ENV_NAME python=3.8
   ```
3. Activate the new environment:
   ```sh
   conda activate YOUR_ENV_NAME
   ```

### Additional Resources
- [NHR Support Website](https://hpc.fau.de/systems-services/documentation-instructions/special-applications-and-tips-tricks/python-and-jupyter/)
- [Official Conda Documentation](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)

## Outcome
The user successfully created and activated a Conda environment with Python 3.8, resolving the issue.

## General Learning
- Conda environments can be used to manage specific Python versions and dependencies.
- When a required module is not available, creating a virtual environment is a viable solution.
- Always refer to official documentation and support websites for detailed instructions.
---

### 2024111842001009_Issue%20with%20loading%20torch%20during%20sbatch%20job.md
# Ticket 2024111842001009

 ```markdown
# Issue with Loading PyTorch During sbatch Job

## Keywords
- PyTorch
- ModuleNotFoundError
- sbatch
- salloc
- conda environment
- pip install

## Problem Description
The user encountered a `ModuleNotFoundError` with PyTorch when submitting a job using `sbatch`, despite the package being installed in their conda environment. The same script ran successfully during an interactive job (`salloc`).

## Root Cause
- The user installed PyTorch using `pip` instead of `conda`.
- The conda environment was not properly activated or configured in the batch script.

## Diagnostic Steps
1. The user provided the output of `pip list` instead of `conda list`, indicating that PyTorch was installed via `pip`.
2. The HPC Admin created a new conda environment and installed the packages using the user's `pip list`.
3. The HPC Admin tested the environment and found no issues with importing PyTorch.

## Solution
1. Create a new conda environment.
2. Install the required packages using `pip install -r packages.txt`.
3. Ensure the conda environment is properly activated in the batch script.

## Recommendations
- Avoid using `pip` for installing packages in conda environments to prevent conflicts.
- Follow the HPC documentation for setting up Python environments: [Python Environment Initialization](https://doc.nhr.fau.de/environment/python-env/#first-time-only-initialization).

## Additional Notes
- The HPC Admin provided a job script and a `packages.txt` file for reference.
- The user should reinstall the packages and test the batch job again.
```
---

### 2021061642002787_Update%20to%20quantumtools%20module%20%2B%20further%20modules%20for%20AMD%20EPYC%20nodes.md
# Ticket 2021061642002787

 # HPC Support Ticket Conversation Summary

## Subject
Update to quantumtools module + further modules for AMD EPYC nodes

## Keywords
- Python modules
- Module management
- Software installation
- Licensing
- User training
- Proxy settings

## What Can Be Learned

### General
- Users often request specific software packages for their research needs.
- Grouping software packages into logical modules can help manage dependencies and updates.
- User training on self-installation of Python packages can reduce support load.

### Specific Issues and Solutions

#### Python Package Installation
- **Problem**: User encountered issues with `pip --user` due to permission errors.
- **Solution**: Ensure the correct Python version is loaded using `module load python`. Verify the installation path for user-installed packages.

#### Module Loading Issues
- **Problem**: User unable to load `quantumtools/qsimqirq-0.7.1` module despite it being available.
- **Solution**: Ensure the correct Python version is loaded. Verify module paths and dependencies.

#### User Environment Configuration
- **Problem**: User had to manually create `~/.bashrc` or `~/.bash_profile` to add Python paths.
- **Solution**: Advise users not to modify `$PATH` or `$PYTHONPATH` manually to avoid conflicts with the module system.

#### Software Licensing
- **Problem**: Licensing issues with Mathematica and Gurobi.
- **Solution**: Work with the software group to resolve licensing issues. Provide users with information on setting up proxy variables for downloads.

#### User Training
- **Problem**: Users need guidance on installing and managing Python packages.
- **Solution**: Conduct training sessions via Zoom. Provide documentation and resources for self-installation.

## Documentation and Resources
- [Python and Jupyter Documentation](https://hpc.fau.de/systems-services/systems-documentation-instructions/special-applications-and-tips-tricks/python-and-jupyter/)
- [Module System Documentation](https://hpc.fau.de/systems-services/systems-documentation-instructions/environment/#modules)
- [HPC Cafe on Building Code with Module Files](https://hpc.fau.de/systems-services/support/hpc-cafe/)

## Conclusion
Effective communication and user training are key to managing software requests and resolving installation issues. Grouping software packages and providing clear documentation can help streamline the support process.
---

### 2022091542003511_no%20such%20variable%3A%20%22env%28SLURM_CLUSTER_NAME%29%22.md
# Ticket 2022091542003511

 # HPC Support Ticket: No Such Variable "env(SLURM_CLUSTER_NAME)"

## Keywords
- SLURM
- SLURM_CLUSTER_NAME
- SLURM_JOB_ID
- Module Load Error
- info_logging.tcl
- srun
- bash -l

## Problem Description
User encountered an error when trying to load a module after connecting to a job using `srun --pty --jobid <jobid> bash -l`. The error message indicated that the variable `SLURM_CLUSTER_NAME` was not defined.

## Root Cause
The script `/apps/modules/modincludes/info_logging.tcl` assumed that `SLURM_CLUSTER_NAME` would be defined if `SLURM_JOB_ID` existed. However, this was not the case, leading to the error.

## Solution
The HPC Admin fixed the issue in the `info_logging.tcl` script by not relying on `SLURM_CLUSTER_NAME` being defined when `SLURM_JOB_ID` exists.

## Workaround
Before the fix, the user was able to manually set the `SLURM_CLUSTER_NAME` variable to work around the issue:
```bash
export SLURM_CLUSTER_NAME=<cluster_name>
```

## Lessons Learned
- Always check if necessary environment variables are set before using them in scripts.
- Manually setting environment variables can serve as a temporary workaround for such issues.
- Documentation and assumptions in scripts should be kept up-to-date to reflect the current behavior of the system.
---

### 2024073142002689_Regarding%20creating%20conda%20environment.md
# Ticket 2024073142002689

 # HPC Support Ticket: Creating Conda Environment

## Keywords
- Conda environment
- Anaconda3
- Working directory path
- Python environment

## Problem
- User wants to create a conda environment with Anaconda3 for project work.
- User needs guidance on adding Anaconda3 to the working directory path and using the conda environment.

## Solution
- HPC Admin provided a link to the documentation for using conda environments on the HPC systems: [Python Environment Documentation](https://doc.nhr.fau.de/environment/python-env/)

## General Learnings
- Users may need assistance with setting up specific environments like Conda for their projects.
- Documentation links are a useful resource for guiding users through common setup processes.
- Ensure users are aware of available documentation and support resources for environment setup.
---

### 2024032142003776_Conda%20environment%20not%20available%20on%20Jupyter%20lab.md
# Ticket 2024032142003776

 # HPC Support Ticket: Conda Environment Not Available on Jupyter Lab

## Keywords
- Conda environment
- Jupyter Lab
- Kernel
- ipykernel
- .bashrc
- Proxies
- Maintenance work
- Tier3 resources
- Alex
- tinyGPU

## Problem Description
After maintenance work, the user was unable to use their custom conda environments in Jupyter Lab. The environments did not show up as possible kernels despite having `ipykernel` installed.

## Root Cause
The `.bashrc` file was not properly loading after the maintenance work, leading to improperly configured proxies.

## Solution
The user re-edited the `.bashrc` file to properly configure the proxies, which resolved the issue.

## General Learnings
- Ensure that the `.bashrc` file is properly configured and loaded after maintenance work.
- Verify that custom conda environments are listed in `$HOME/.conda/environments.txt`.
- Confirm that the user has access to the appropriate resources (e.g., Alex, tinyGPU) based on their account tier.
- Check for logged connections to the relevant JupyterHub instances.

## Ticket Closure
The issue was resolved by the user, and the ticket was closed by the HPC Admin with an invitation to reopen if further assistance is needed.
---

### 2022063042003391_Python%20Modules%20install.md
# Ticket 2022063042003391

 ```markdown
# HPC-Support Ticket: Python Modules Install

## Keywords
- Python modules
- sklearn
- HPC Woody module
- pip
- conda environments
- TensorFlow
- PyTorch

## Problem
- User gained access to HPC's Woody module (iwbn001h) and needs specific Python modules (e.g., sklearn) that are not available.
- User does not have permission to install new modules and is unsure how to proceed.

## Solution
- **Use Official Email**: Users should use their official FAU email address for support inquiries to receive full support.
- **Self-Install Python Packages**: Documentation is available on how to install Python packages using pip.
  - [Python and Jupyter Documentation](https://hpc.fau.de/systems-services/documentation-instructions/special-applications-and-tips-tricks/python-and-jupyter/#pip)
- **Conda Environments**: If setting up conda environments, configure `~/.condarc` as per the documentation.
- **TensorFlow and PyTorch**: Specific documentation is available for these frameworks.
  - [TensorFlow and PyTorch Documentation](https://hpc.fau.de/systems-services/documentation-instructions/special-applications-and-tips-tricks/tensorflow-pytorch/)

## General Learnings
- Always use official email for support inquiries.
- Users can install Python packages themselves using pip.
- Configure `~/.condarc` for conda environments.
- Specific documentation is available for TensorFlow and PyTorch.
```
---

### 2021061742002089_Inquiery%20regarding%20installation%20of%20openslide%20library.md
# Ticket 2021061742002089

 # HPC-Support Ticket: Inquiry Regarding Installation of Openslide Library

## Keywords
- Openslide Library
- Python Interface
- Singularity Container
- TinyGPU Cluster
- Central Installation
- Apt Installation

## Problem
- User requires the `openslide` library for processing large image data in digital pathology.
- The library is needed for the Python interface.
- User inquires about central installation as multiple groups use this library.
- User mentions that `openslide` can only be installed via `apt`, which does not have a user option.

## Solution
- HPC Admin suggests using a Singularity container for Python dependencies to become independent of central installations.
- HPC Admin provides documentation and resources for setting up Singularity containers.
- `libopenslide-dev` is installed on TinyGPU nodes accessible via PBS/torque.

## Learnings
- Central installation of libraries can be requested if multiple groups need them.
- Singularity containers offer a way to manage dependencies independently.
- Documentation and resources for Singularity containers are available on the HPC website.
- Root access is required to build new containers, which is not possible on HPC systems.
- Locally generated or Dockerhub/Singularityhub images can be used on HPC systems.

## References
- [Singularity Documentation](https://hpc.fau.de/systems-services/systems-documentation-instructions/special-applications-and-tips-tricks/)
- [Openslide GitHub](https://github.com/openslide/openslide)
- [Openslide Website](https://openslide.org/)
---

### 2020031642000349_Python%20Backend%20TinyETH.md
# Ticket 2020031642000349

 # HPC Support Ticket: Python Backend TinyETH

## Keywords
- Python
- HPC Cluster
- Anaconda Module
- Account Management
- Data Migration

## Summary
A user inquired about the possibility of running Python on the backend of the HPC cluster. The HPC Admin provided information on Python availability and also addressed an account management issue.

## Root Cause
- **User Inquiry**: The user wanted to know if Python could be executed on the backend.
- **Account Issue**: The user's HPC account was due to expire and needed to be migrated to a new account.

## Solution
- **Python Availability**: The HPC Admin informed the user that Python is available on all HPC clusters. The user was advised to load one of the `python/*-anaconda` modules.
- **Account Management**: The HPC Admin noticed that the user's account had been extended without proper migration. A new account was created, and the user was instructed to set a password via the IdM-Portal. The user was also advised to migrate necessary data to the new account before the old account expired.

## General Learnings
- Python is available on all HPC clusters and can be accessed by loading the appropriate Anaconda modules.
- Regularly check account statuses and ensure proper migration when users switch between clusters or projects.
- Inform users about account expiration and provide clear instructions for data migration.

## Actions Taken
- Informed the user about Python availability and module loading.
- Created a new HPC account for the user.
- Provided instructions for setting a password and migrating data.

## Follow-Up
- Ensure the user successfully migrates data to the new account.
- Monitor account statuses to prevent future issues with expiration and migration.

---

This documentation can be used to address similar inquiries about Python availability and account management issues in the future.
---

### 2023021442000509_%5Bfritz%5D%20%22module%22%20command%20not%20found%20inside%20bash%20script.md
# Ticket 2023021442000509

 # HPC Support Ticket: "module" Command Not Found Inside Bash Script

## Keywords
- `module` command not found
- Bash script
- Login shell
- Shebang line

## Problem Description
The user encountered an error where the `module` command was not recognized within a bash script. The script contained the following content:
```bash
module avail
#EOF
```
The user did not have a `.bashrc` file in their home directory.

## Root Cause
The `module` command was not available because the script was running in a non-login shell, where modules are not initialized.

## Solution
The HPC Admin advised the user to add the following shebang line at the beginning of the script to invoke a login shell:
```bash
#!/bin/bash -l
```
This ensures that the script runs in a login shell environment, where the `module` command is available.

## General Lessons Learned
- Bash scripts may behave differently depending on whether they are run in a login or non-login shell.
- The `module` command is not available in non-login shells.
- Adding `#!/bin/bash -l` as the shebang line in a script ensures it runs in a login shell.
- This solution allows users to maintain portability and shareability of their bash scripts across different systems.
---

### 2024050242003067_Python%20conda%20usage.md
# Ticket 2024050242003067

 ```markdown
# HPC-Support Ticket: Python Conda Usage

## Issue
User unable to create a new conda environment.

## Error Message
```
Downloading and Extracting Packages
Preparing transaction: failed
# >>>>>>>>>>>>>>>>>>>>>> ERROR REPORT <<<<<<<<<<<<<<<<<<<<<<
  Traceback (most recent call last):
  ...
  json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
```

## Environment Variables
```
CIO_TEST=<not set>
CONDA_ENVS_PATH=/apps/python/3.9-anaconda/envs
CONDA_EXE=/apps/python/3.9-anaconda/bin/conda
CONDA_PKGS_DIRS=/apps/python/3.9-anaconda/pkgs
CONDA_PYTHON_EXE=/apps/python/3.9-anaconda/bin/python
CONDA_ROOT=/apps/python/3.9-anaconda
CONDA_SHLVL=0
CURL_CA_BUNDLE=<not set>
LD_PRELOAD=<not set>
MANPATH=/apps/python/3.9-anaconda/share/man:::/apps/hpc-workspace/1.4.0/share/man
MODULEPATH=/apps/modules/data/applications:/apps/modules/data/compiler:/apps/modules/data/development:/apps/modules/data/libraries:/apps/modules/data/tools:/apps/modules/data/via-spack:/apps/modules/data/deprecated:/apps/modules/data/testing:/apps/modules/data/conda
PATH=/apps/python/3.9-anaconda/bin:/apps/python/3.9-anaconda/condabin:/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/apps/hpc-workspace/1.4.0/bin
REQUESTS_CA_BUNDLE=<not set>
SSL_CERT_FILE=<not set>
__MODULES_SHARE_MANPATH=:1
https_proxy=<set>
```

## Root Cause
Possible corruption in the `~/.condarc` file or issues with the package cache.

## Solution
1. Clean conda cache:
   ```bash
   conda clean -i
   ```
2. Backup and remove the existing `~/.condarc` file:
   ```bash
   mv ~/.condarc ~/condarc-bkp
   ```
3. Create a new `~/.condarc` file with the following commands:
   ```bash
   conda config --add pkgs_dirs $WORK/software/private/conda/pkgs
   conda config --add envs_dirs $WORK/software/private/conda/envs
   ```

## Additional Information
- Ensure that the JupyterHub server and the working environment are compatible.
- For Jupyter notebooks, install `ipykernel` in the conda environment to make it appear as a kernel in JupyterHub.
- Refer to the documentation for running Jupyter notebooks: [Jupyter Notebook Documentation](https://doc.nhr.fau.de/apps/jupyter/?h=jupyter#jupyter-notebook)

## Keywords
- Conda environment creation
- JSONDecodeError
- Conda configuration
- JupyterHub compatibility
- Package cache corruption
```
---

### 2023081442002907_ImportError%20beim%20Importieren%20von%20matplotlib%3A%20%22GLIBCXX_3.4.29%20not%20found%22%20und%20.md
# Ticket 2023081442002907

 ```markdown
# HPC-Support Ticket Conversation Summary

## Subject: ImportError beim Importieren von matplotlib: "GLIBCXX_3.4.29 not found" und INVALID_ARGUMENT Warnungen

### Keywords:
- ImportError
- matplotlib
- GLIBCXX_3.4.29
- INVALID_ARGUMENT Warnungen
- TensorFlow
- DistributionStrategy
- Dataset Warnings
- Optimizer Issue

### Problem:
- User encountered an ImportError when trying to import matplotlib due to missing GLIBCXX_3.4.29.
- Additionally, the user faced INVALID_ARGUMENT warnings and the script stopped before training.

### Root Cause:
- The ImportError was due to the missing GLIBCXX_3.4.29 version, which is required by matplotlib and other packages compiled with gcc >= 11.1.0.
- The INVALID_ARGUMENT warnings were caused by the optimizer in `model.compile()`. The optimizer instance was created once and shared across GPUs, leading to conflicts.

### Solution:
- To resolve the ImportError, the user was advised to load the gcc/11.2.0 module before running the script.
- The INVALID_ARGUMENT warnings were resolved by replacing `optimizer=optimizer` with `optimizer=tf.keras.optimizer.Adam()` in the `model.compile()` call. This ensured that each GPU had its own optimizer instance.

### Additional Notes:
- The user also encountered dataset warnings, which were not the root cause of the INVALID_ARGUMENT warnings but were noted for future reference.
- The user confirmed that the problem was resolved after applying the suggested solutions.

### Conclusion:
- The ticket was closed after the user confirmed that the issues were resolved.
```
---

### 2020112042002083_python-gdal%20auf%20HPC.md
# Ticket 2020112042002083

 ```markdown
# HPC Support Ticket: python-gdal auf HPC

## Problem
Der Benutzer möchte `python-gdal` auf dem HPC-Cluster verfügbar machen, um `gdal_calc.py` in der Konsole zu verwenden. Nach der Installation von `gdal` unter `python/2.7-anaconda` traten jedoch Probleme auf, die die Funktionalität von `rgdal` in R und `gdal` in Python beeinträchtigten.

## Ursache
Die Installation von `gdal` unter `python/2.7-anaconda` führte zu Konflikten mit der Umgebungsvariablen `PROJ_LIB`, die nicht korrekt gesetzt war. Dies verursachte Fehler bei der Verwendung von `gdal` und `rgdal`.

## Lösung
1. **Rückgängig machen der Installation**: Die Installation von `gdal` unter `python/2.7-anaconda` wurde rückgängig gemacht und ein Revert auf eine Sicherung vom Februar durchgeführt, die `gdal` und `proj4` enthielt.
2. **Installation von `python-gdal`**: Stattdessen wurde `python-gdal` für das System-gdal installiert, was die gewünschte Funktionalität ohne Konflikte bereitstellte.

## Ergebnis
Nach der Durchführung dieser Schritte funktionierte `gdal` unter `python/2.7-anaconda` fehlerfrei und `rgdal` in R wurde ebenfalls nicht mehr beeinträchtigt. Der Benutzer konnte seine Produktion fortsetzen.

## Zusammenfassung
Die Lösung bestand darin, die Installation von `gdal` unter `python/2.7-anaconda` rückgängig zu machen und `python-gdal` für das System-gdal zu installieren. Dies stellte die gewünschte Funktionalität ohne Konflikte sicher.
```
---

### 2019052142002345_python%20module%20at%20woodycap.md
# Ticket 2019052142002345

 ```markdown
# HPC-Support Ticket Conversation: Adding a Package to Python Module

## Keywords
- Python module
- Anaconda
- mysql-connector-python
- Package addition
- HPC support

## Summary
A user requested the addition of the `mysql-connector-python` package to the `python/2.7-anaconda` module. The HPC admin initially expressed reluctance to modify the Anaconda setup but eventually confirmed that the package had been added.

## Root Cause
- User needed the `mysql-connector-python` package for their work.

## Solution
- The `mysql-connector-python` package was added to the `python/2.7-anaconda` module by the HPC admin.

## Lessons Learned
- Users may request specific packages to be added to existing modules.
- HPC admins may need to evaluate the necessity and feasibility of such requests.
- Communication between users and HPC admins is crucial for resolving such requests efficiently.
```
---

### 2021120242001202_front-ends%2C%20libraries%20load%20via%20python.md
# Ticket 2021120242001202

 ```markdown
# HPC Support Ticket: Front-Ends Slow and Python Library Import Issue

## Keywords
- Front-end performance
- Python library import
- sys.path.append
- Python version mismatch
- HOOMD library

## Summary
A user reported issues with slow front-ends and problems importing an external Python library using `sys.path.append`.

## Root Cause
1. **Front-End Performance**: The specific cause of the slow front-ends was not identified in the conversation.
2. **Python Library Import Issue**: The root cause was a Python version mismatch. The user's HOOMD library was built with Python 3.7, but the default Python version on the new SLURM nodes was 3.8.

## Solution
1. **Front-End Performance**: No specific solution was provided for the slow front-ends.
2. **Python Library Import Issue**: The user was advised to rebuild the HOOMD library with the newer Python version (3.8) to resolve the import error.

## Lessons Learned
- Ensure that the Python version used to build external libraries matches the Python version available on the HPC nodes.
- When migrating nodes from one scheduler to another (e.g., from Torque to SLURM), be aware of potential changes in default software versions.
- Provide clear and specific information when reporting issues to HPC support to facilitate quicker resolution.

## Actions Taken
- The user was advised to rebuild the HOOMD library with the correct Python version.
- The ticket was closed after the user confirmed the issue was resolved.
```
---

### 2024042342001405_Unable%20to%20install%20PIP.md
# Ticket 2024042342001405

 # HPC Support Ticket: Unable to Install PIP

## Keywords
- PIP installation
- Python environment
- Administrator access
- Conda environment
- Python version

## Problem
- User unable to install Python packages due to missing PIP and lack of administrator access.
- User attempted to install Python 3.10 but requires administrator access.

## Root Cause
- User was trying to set up a Python environment on the dialog server (csnhr) instead of the appropriate cluster frontends.
- User lacked the necessary permissions to install software system-wide.

## Solution
- **Redirect to Appropriate Servers**: Inform the user that calculations should not be run on the dialog server (csnhr). Instead, they should connect to the frontends of the clusters (e.g., woody, tinyx).
- **Provide Documentation**: Share introductory slides and documentation links for setting up Python environments:
  - [HPC in a Nutshell](https://hpc.fau.de/files/2024/04/2024-04-10_HPC_in_a_Nutshell.pdf)
  - [Python Documentation](https://doc.nhr.fau.de/sdt/python/)
  - [Python Environment Setup](https://doc.nhr.fau.de/environment/python-env/)
- **Conda Environment**: Advise the user to create a Conda environment with the specific Python version needed. This does not require administrator access.

## Additional Notes
- Ensure the user understands the difference between dialog servers and cluster frontends.
- Encourage the user to follow the provided documentation for setting up their Python environment.

## References
- [HPC in a Nutshell](https://hpc.fau.de/files/2024/04/2024-04-10_HPC_in_a_Nutshell.pdf)
- [Python Documentation](https://doc.nhr.fau.de/sdt/python/)
- [Python Environment Setup](https://doc.nhr.fau.de/environment/python-env/)
---

### 2022100742003168_mail%20und%20gmt%20und%20python.md
# Ticket 2022100742003168

 # HPC Support Ticket Conversation Analysis

## Keywords
- `mail` command
- `gmt` (Generic Mapping Tools)
- Python modules (`netCDF4`, `numpy`, `scipy`)
- GAMMA software
- Singularity container

## Issues Reported by User
1. **Mail Command**: The `mail` command is not working.
2. **GMT Availability**: `gmt` (Generic Mapping Tools) is not available.
3. **Python Module Issues**:
   - `netCDF4` module not found.
   - Error with `numpy` import in `ScanSAR_coreg_overlap.py` script.
   - `scipy` module not found when using Python 3.6.
4. **GAMMA Software**: Issues with running `ScanSAR_coreg_overlap.py` due to Python version and module dependencies.

## Root Causes
- **Mail Command**: Not specified in the conversation.
- **GMT Availability**: Dependency conflicts with other installed packages.
- **Python Module Issues**:
  - `netCDF4`: Module not installed.
  - `numpy`: Import error due to a failed build or circular import.
  - `scipy`: Module not installed.
- **GAMMA Software**: Dependency on Python 3.6, which is not available on compute nodes.

## Solutions Provided by HPC Admin
1. **Mail Command**: A colleague will address the issue upon return from vacation.
2. **GMT Availability**: Attempt to load `gmt` when the Gamma module is loaded, but no guarantee of functionality.
3. **Python Module Issues**:
   - Suggested building a custom Singularity container with all required dependencies to avoid conflicts with the system environment.
4. **GAMMA Software**: Use a Singularity container to ensure a consistent and reproducible environment.

## General Learnings
- **Dependency Management**: Custom environments like Singularity containers can help manage complex dependencies and avoid conflicts with the system environment.
- **Reproducibility**: Using containers ensures a reproducible environment, which is beneficial for research and publications.
- **Collaboration**: Similar issues faced by other users (e.g., linguistics researchers) were resolved using Singularity containers, highlighting the effectiveness of this approach.

## Next Steps for User
- Build a Singularity container with all required dependencies.
- Test the container on the HPC system to ensure functionality.
- Use the container for future work to maintain a consistent environment.
---

### 2022100442000701_module%3A%20command%20not%20found.md
# Ticket 2022100442000701

 # HPC Support Ticket: module: command not found

## Keywords
- module: command not found
- Slurm job script
- #!/bin/bash -l
- FAU HPC cluster

## Problem Description
The user encountered error messages indicating that the `module` command was not found while running a job on the HPC cluster. The job appeared to run correctly, but the user was concerned about the error messages.

## Root Cause
The job script did not load the necessary environment to recognize the `module` command.

## Solution
Add `-l` (lower case L) to the very first line of the job script to ensure the environment is loaded correctly. The shebang line should be updated to `#!/bin/bash -l`.

## Example
```bash
#!/bin/bash -l
# Your job script content here
```

## General Learning
- Ensure that job scripts load the necessary environment by using the `-l` option in the shebang line.
- The `module` command is commonly used to manage software environments on HPC clusters, and its absence indicates an environment loading issue.

## Roles Involved
- HPC Admins
- 2nd Level Support Team

## Related Teams
- Software and Tools Developers
- Training and Support Group
- NHR Rechenzeit Support and Applications for Grants
---

### 2018091242001581_Fehlermeldung%20Memoryhog.md
# Ticket 2018091242001581

 ```markdown
# HPC-Support Ticket: Fehlermeldung Memoryhog

## Keywords
- Memoryhog
- Login error
- Module command not found
- Missing file: `/apps/modules/modulecmd.tcl`

## Problem Description
User encounters an error when logging into the `memoryhog` system. The error messages indicate that the `module` command is not found and the file `/apps/modules/modulecmd.tcl` is missing.

## Error Messages
```
couldn't read file "/apps/modules/modulecmd.tcl": no such file or directory
module: command not found
```

## Root Cause
The root cause of the problem is the missing `modulecmd.tcl` file, which is required for the `module` command to function properly.

## Solution
- Ensure that the `modulecmd.tcl` file is present in the specified directory.
- Verify that the `module` command is correctly installed and configured on the `memoryhog` system.

## General Learning
- Missing configuration files can lead to command not found errors.
- Proper installation and configuration of environment modules are crucial for system functionality.
```
---

### 2024101042002462_Installing%20Pytorch%20with%20Conda%20on%20Woody.md
# Ticket 2024101042002462

 # Installing Pytorch with Conda on Woody

## Keywords
- Conda environment
- Pytorch installation
- Python versions
- Anaconda License mitigation
- Proxy settings

## Problem Description
The user was struggling to set up a Conda environment with Pytorch (CPU version, no CUDA) on Woody. The user followed the steps to initialize Conda, create a new environment, and run an installation script but encountered an error. The user also tried to set up the environment from an `env.yml` file but faced issues with Python version availability.

## Root Cause
The issue was likely caused by the interaction between the Anaconda License mitigation and the Pytorch channel. The user was not aware of the need to disable channel priority and ensure that the "defaults" channel was not used.

## Solution
The HPC Admin suggested the following steps:
1. Disable channel priority with the command:
   ```bash
   conda config --set channel_priority disabled
   ```
2. Ensure that the "defaults" channel is not used for the environment.
3. Verify that the proxy settings are correctly configured if there are connection issues.

## What Can Be Learned
- Conda environments can install the needed Python version even if it is not explicitly available in the module list.
- Anaconda License mitigation can cause unexpected issues when combined with certain channels like Pytorch.
- Disabling channel priority and avoiding the "defaults" channel can resolve such issues.
- Proxy settings may be necessary for certain installations, and users should be aware of them to troubleshoot connection issues.

## Additional Notes
- The user confirmed that the suggested command resolved the issue.
- The user did not use the proxy setting, but it is important to keep it in mind for future reference.

## References
- [Anaconda License Mitigation](https://www.rrze.fau.de/2024/09/lizenzfalle-anaconda/)
- [Proxy Settings FAQ](https://doc.nhr.fau.de/faq/#why-does-my-application-give-an-http-https-timeout)
---

### 2022021742001684_GLIBC_2.27.md
# Ticket 2022021742001684

 # HPC Support Ticket: GLIBC_2.27

## Keywords
- GLIBC version
- ldd version
- Python library
- ImportError
- Missing module

## Problem Description
The user is encountering an `ImportError` due to a mismatch in the required GLIBC version. The user's Python library requires GLIBC version 2.27, but the current environment provides GLIBC version 2.17.

## Error Message
```
ImportError: /lib64/libm.so.6: version `GLIBC_2.27' not found (required by /home/hpc/iwsp/iwsp011h/hoomd3.0/hoomd-blue/build/hoomd/hpmc/_hpmc.cpython-37m-x86_64-linux-gnu.so)
```

## Root Cause
The root cause of the problem is the mismatch between the required GLIBC version (2.27) and the available GLIBC version (2.17) in the current environment.

## Solution
- **Check for Available Modules**: Verify if there is a module available that provides GLIBC version 2.27.
- **Update Environment**: If a suitable module is available, load it to update the environment to the required GLIBC version.
- **Contact HPC Admins**: If no suitable module is available, contact HPC Admins for further assistance in updating the GLIBC version.

## General Learning
- Always check the required dependencies and versions for the software you are using.
- Ensure that the environment provides the necessary versions of libraries and tools.
- Utilize available modules to manage different versions of software and libraries.
- If the required version is not available, consult with HPC Admins for potential solutions.
---

### 2024081342003031_Reagrding%20non-activation%20of%20conda%20environment.md
# Ticket 2024081342003031

 ```markdown
# HPC Support Ticket: Non-Activation of Conda Environment

## Subject
Reagrding non-activation of conda environment

## User Issue
- User unable to find their conda environment listed under `conda info --envs`.
- Environment was working fine until the previous day.

## Root Cause
- Scheduled maintenance and downtime of the HPC system (Alex cluster) from August 13 to 15.

## HPC Admin Response
- Confirmed that the issue is likely due to ongoing maintenance.
- Provided a link to the maintenance status page.
- Advised the user to check back after the maintenance period and to report if the issue persists.

## Keywords
- Conda environment
- Scheduled downtime
- Maintenance
- Alex cluster
- `conda info --envs`

## General Learning
- Scheduled maintenance can affect the availability of user environments.
- Users should check the maintenance status page for updates.
- If issues persist after maintenance, users should report them for further investigation.
```
---

### 2023042742001294_I%20need%20to%20have%20my%20virtaul%20environment%20for%20training%20my%20model.md
# Ticket 2023042742001294

 # HPC Support Ticket Conversation Summary

## Keywords
- Virtual Environment
- Python
- File Systems
- Home Directory
- $WORK Directory
- $FASTTMP Directory
- Module Command
- Package Installation

## Problem
- User needs a specific Python environment to install required libraries for training models.
- User encountered issues with missing or wrong versions of libraries using the existing Python environment.
- User inquires about creating a virtual environment in the home or $WORK directory and its persistence.

## Solution
- **Virtual Environment Creation**:
  - Users can create a virtual environment but should not install it in the home directory.
  - Preferred location for the virtual environment is the $WORK directory.
  - Information about file systems can be found at [HPC Storage Documentation](https://hpc.fau.de/systems-services/documentation-instructions/hpc-storage).

- **Python Module Loading**:
  - Use the `module av` command to find available Python versions.
  - Load the desired Python version before creating the virtual environment.

- **Creating a Virtual Environment**:
  - Use the command `python -m venv /path/to/new/virtual/environment`.
  - Detailed instructions can be found at [Python venv Documentation](https://docs.python.org/3/library/venv.html).

- **Data and Code Storage**:
  - For running jobs, use the $FASTTMP directory if available.
  - The $WORK directory is suitable for data and code storage, considering backup policies.

## Additional Notes
- The home directory is not recommended for creating virtual environments due to potential deletion policies.
- The $WORK directory is preferred for long-term storage and virtual environment creation.

## References
- [HPC Storage Documentation](https://hpc.fau.de/systems-services/documentation-instructions/hpc-storage)
- [Python venv Documentation](https://docs.python.org/3/library/venv.html)
---

### 2024051542002249_Issue%20installing%20pycocotools.md
# Ticket 2024051542002249

 # HPC Support Ticket Conversation Analysis

## Keywords
- pycocotools
- python3-devel
- SSO
- password
- quota
- disk space
- grace period
- soft quota
- hard quota

## Summary
- **Issue**: User encountered an error while installing `pycocotools==2.0.4` due to missing `python3-devel` package.
- **Root Cause**: The specific version of `pycocotools` (2.0.4) had compatibility issues. The error indicated a missing `Python.h` file, which is part of the `python3-devel` package.
- **Solution**: The HPC Admin suggested installing the current default version (2.0.7) of `pycocotools`, which resolved the issue.

- **Additional Issue**: User exceeded their soft quota for disk space.
- **Request**: User requested an increase in their quota due to the need for additional disk space for their master thesis work.
- **Response**: The HPC Admin responded in a separate ticket.

## General Learnings
- **Version Compatibility**: Always check for the latest version of a package if encountering installation issues.
- **SSO and Passwords**: Users logging in via SSO may not have a separate password for their account, which can complicate installations requiring authentication.
- **Quota Management**: Users should be aware of their disk space quotas and manage their data accordingly. If additional space is needed, a request can be made to the HPC support team.

## Documentation for Support Employees
- **Error Resolution**: If a user encounters an error related to missing `Python.h` during package installation, suggest installing the latest version of the package.
- **Quota Requests**: If a user exceeds their disk space quota, guide them to request an increase through the appropriate channels.

## Example Error and Solution
```markdown
### Error
```
Building wheel for pycocotools (pyproject.toml) ... error
ERROR: Command errored out with exit status 1:
command: /home/hpc/g102ea/g102ea10/python-env/bin/python3 /home/hpc/g102ea/g102ea10/python-env/lib64/python3.6/site-packages/pip/_vendor/pep517/in_process/_in_process.py build_wheel /tmp/tmpg_4v73n_
cwd: /tmp/pip-install-tganj_00/pycocotools_303051aa604a43caa427b64f00d327cc
Complete output (26 lines):
...
pycocotools/_mask.c:48:10: fatal error: Python.h: No such file or directory
#include "Python.h"
         ^~~~~~~~~~
compilation terminated.
...
ERROR: Failed building wheel for pycocotools
Failed to build pycocotools
ERROR: Could not build wheels for pycocotools, which is required to install pyproject.toml-based projects
```

### Solution
- Suggest installing the latest version of `pycocotools` (e.g., 2.0.7) to resolve compatibility issues.
```
---

### 2023030642000335_Regarding%20installing%20libraries.md
# Ticket 2023030642000335

 # HPC Support Ticket: Installing Libraries

## Keywords
- `pip install`
- `albumentations`
- `opencv-contrib-python-headless`
- `proxy`
- `python module`

## Problem
- User attempting to install `albumentations` library using `pip install albumentations --user --proxy "http://proxy:80"`.
- Installation fails when trying to install `opencv-contrib-python-headless`.

## Root Cause
- Possible issues with the Python environment or module not being loaded.
- Potential certificate expiration issue.

## Solution
- Ensure the correct Python module is loaded before using `pip`.
- Verify if the user intends to use Python 2 or Python 3.

## Steps Taken
1. User attempted to install `albumentations` using `pip`.
2. Installation failed at the point of installing `opencv-contrib-python-headless`.
3. HPC Admin suggested checking if the correct Python module is loaded.

## Notes
- The user provided a screenshot of the error, which was not included in the conversation.
- The HPC Admin mentioned a certificate expiration issue, which might be related to the proxy or the package repository.

## Next Steps
- User should load the appropriate Python module and retry the installation.
- If the issue persists, further investigation into the certificate expiration and proxy settings may be necessary.

## General Learning
- Always ensure the correct Python module is loaded before using `pip`.
- Proxy settings and certificate issues can affect package installations.
- Providing detailed error messages or screenshots can help in diagnosing the problem.
---

### 2024021342002491_missing%20python%20package.md
# Ticket 2024021342002491

 ```markdown
# HPC-Support Ticket: Missing Python Package

## Keywords
- Python package
- Missing package
- HPC environment
- Software installation
- Troubleshooting

## Summary
A user reported a missing Python package in the HPC environment. The ticket involved communication between the user and various HPC Admins and 2nd Level Support team members.

## Root Cause
The user was unable to find a specific Python package required for their work.

## Solution
- **HPC Admins** and **2nd Level Support** team members investigated the issue.
- The solution involved either installing the missing package or guiding the user on how to install it themselves.
- If the package was not available, alternative solutions or workarounds were provided.

## Lessons Learned
- Ensure that common Python packages are pre-installed in the HPC environment.
- Provide clear documentation on how users can install additional packages if needed.
- Regularly update the list of available packages and communicate changes to users.
```
---

### 2024090942002137_Calling%20Python%20from%20C%2B%2B.md
# Ticket 2024090942002137

 ```markdown
# Calling Python from C++

## Keywords
- Python
- C++
- pybind11
- numpy
- Conda environment
- ImportError

## Problem Description
The user is attempting to call Python functions from C++ using pybind11. The initial Python function call works, but importing numpy results in an error. The user has verified that numpy can be imported without issues when using the Python interpreter directly.

## Root Cause
The issue likely stems from the Python environment not being correctly set up when called from C++. This could be due to missing environment variables or incorrect paths.

## Solution
The user managed to resolve the issue independently. No specific solution steps were provided, but it is implied that the user corrected the environment setup or paths.

## Lessons Learned
- Ensure that the Python environment is correctly configured when calling Python from C++.
- Verify that all necessary paths and environment variables are set up properly.
- pybind11 can be used to call Python functions from C++, but attention to the environment setup is crucial.

## Additional Notes
- The HPC support team did not have prior experience with this specific issue.
- The user offered to help if similar issues arise in the future.
```
---

### 2021100542004369_HPC%20install%20python%20%20module.md
# Ticket 2021100542004369

 ```markdown
# HPC Support Ticket: HPC Install Python Module

## Subject
HPC install python module

## User Issue
- User attempted to install several Python modules using `conda install -c pytorch pytorch` but encountered `EnvironmentNotWritableError`.
- User requested installation of specific modules: `numpy`, `pyaml`, `matplotlib`, `torch`, `torchvision`, `faiss-gpu`.

## Root Cause
- User did not have write permissions to the target environment.
- User was trying to use the Python module on a system without GPU.

## Solution
- HPC Admin advised the user to create a conda environment before installing packages to ensure they end up in the user space.
  ```bash
  module load python
  conda create --name myenv
  conda activate myenv
  conda install ...
  ```
- User was instructed to start a job on the GPU cluster, TinyGPU, and provided documentation links for getting started with HPC.
- User encountered a runtime error due to missing NVIDIA drivers and was advised to start a job on the GPU cluster.
- User's job was canceled due to reaching the end of its runtime (default setting of 10 minutes). HPC Admin advised adding `#SBATCH --time=HH:MM:SS` to the head of the submission script.
- User encountered a CUDA error related to the RTX3080 GPU and was advised to update PyTorch for RTX3080 support.

## Additional Notes
- HPC Admin provided a detailed setup for running the training with the RTX3080 GPU, including loading the necessary modules, creating a conda environment, and installing the required packages.
- User was advised to refer to Stack Overflow for remote debugging with PyCharm.

## Keywords
- Python module installation
- Conda environment
- GPU cluster
- NVIDIA drivers
- CUDA error
- PyTorch update
- Remote debugging
- Job submission
- Runtime error
```
---

### 2023032442000211_Frage%20zur%20Conda%20environment.md
# Ticket 2023032442000211

 # HPC Support Ticket: Conda Environment Configuration

## Keywords
- Conda environment
- .condarc file
- JupyterHub
- VS Code
- ipykernel

## Problem Description
The user encountered issues configuring Conda environments on the HPC cluster. Specifically, they were unable to create or edit a `.condarc` file to specify the directory for Conda environments and packages. Additionally, the user's Conda environment was not being recognized in VS Code.

## Root Cause
1. The `.condarc` file already existed, causing errors when attempting to create it.
2. The Conda environment was not configured to be recognized by VS Code.

## Solution
### Configuring Conda Directories
1. **Edit the existing `.condarc` file** or use the following commands to configure Conda directories:
   ```bash
   conda config --add pkgs_dirs $WORK/software/privat/conda/pkgs
   conda config --add envs_dirs $WORK/software/privat/conda/envs
   ```
2. **Restart the Kernel-Server** to apply the configuration changes.

### Making Conda Environment Visible in VS Code
1. **Install the `ipykernel` package** in the Conda environment to make it recognizable by VS Code:
   ```bash
   conda install -n sklearn_env ipykernel
   ```

## General Learnings
- **Conda Configuration**: Understanding how to configure Conda environments and package directories using the `.condarc` file or command-line options.
- **VS Code Integration**: Ensuring that Conda environments are properly set up to be recognized by development tools like VS Code.
- **Kernel Management**: The importance of restarting the kernel server after making configuration changes.

## References
- [FAU HPC Documentation](https://hpc.fau.de/systems-services/documentation-instructions/special-applications-and-tips-tricks/python-and-jupyter/)
- [VS Code Jupyter Kernel Management](https://code.visualstudio.com/docs/datascience/jupyter-kernel-management)

## Support Team Involved
- **HPC Admins**: Provided solutions for configuring Conda directories and making the environment visible in VS Code.
- **2nd Level Support Team**: Assisted in troubleshooting and providing additional support.
---

### 2024071942002774_Python%20on%20csnhr.md
# Ticket 2024071942002774

 ```markdown
# HPC-Support Ticket Conversation: Python on csnhr

## Keywords
- Python
- csnhr
- python3.10-venv
- python3-pip
- Jump server
- Environment management

## Summary
A user requested the installation of `python3.10-venv` and `python3-pip` on the csnhr server. The HPC Admin inquired about the necessity of Python on csnhr, as it is primarily used as a jump server. The user explained that they wanted to compile and run HPC documentation on a single system rather than on local machines. The HPC Admin clarified that while Python 3.10 is available, `pip` and `venv` are intentionally not offered to prevent users from building environments on csnhr, which could lead to support issues on compute nodes.

## Root Cause
- User wanted to use Python for compiling and running HPC documentation.
- csnhr is intended as a jump server, not for extensive work.

## Solution
- Python 3.10 is available on csnhr.
- `pip` and `venv` are intentionally not provided to avoid environment management issues.
- Users should perform such tasks on appropriate compute nodes or clusters.

## Lessons Learned
- Understand the intended use of different servers within the HPC infrastructure.
- Avoid installing environment management tools on jump servers to prevent misuse.
- Encourage users to perform tasks on designated compute nodes or clusters.
```
---

### 2022033142000978_Python%20on%20Alex.md
# Ticket 2022033142000978

 # Python Availability on HPC Cluster

## Keywords
- Python
- HPC Cluster
- Module Load
- Parallel Tempering Metadynamics Simulations

## Problem
- User needs Python for running Parallel Tempering metadynamics simulations on the HPC cluster.
- User was unaware that Python is available as a module on the cluster.

## Solution
- Python is available as a module on all clusters.
- User can load Python using the command: `module load python`.
- If any special Python packages are needed, the user should contact HPC support.

## Lessons Learned
- Always check the available modules on the HPC cluster before requesting new software installations.
- Use the `module load` command to access available software packages.
- Communicate with HPC support for any specific package requirements.

## Actions Taken
- HPC Admin informed the user about the availability of Python as a module.
- User acknowledged the information and confirmed that Python was available in the modules list.
- Ticket was closed as the issue was resolved.
---

### 2024051342003181_question%20about%20%22module%20commond%20not%20found%22.md
# Ticket 2024051342003181

 # HPC Support Ticket: "module command not found"

## Keywords
- VSCode Remote SSH
- Environment Modules
- `module avail`
- `sudo` command
- Password prompt
- `module: command not found`

## Summary
User encountered issues with VSCode Remote SSH extension and installing environment modules on the HPC system. The main problems were:
1. `module: command not found` error when trying to use environment modules.
2. Uncertainty about the password required for `sudo` command during module installation.

## Root Cause
- The user attempted to install environment modules using `sudo`, which is restricted to admins.
- The `module` command was not recognized, likely due to an incomplete or incorrect setup of the environment in VSCode.

## Solution
- **Environment Modules**: The HPC clusters already have environment modules available. Users cannot install additional modules using `sudo`.
  - To see the list of available modules, use the command: `module avail`.
  - For additional modules, users can add a private path following the instructions on the documentation page: [Environment Modules](https://doc.nhr.fau.de/environment/modules/).
- **VSCode Remote SSH**: Ensure that the VSCode environment is correctly configured to recognize the `module` command.
  - Refer to the documentation page for VSCode: [VSCode SSH](https://doc.nhr.fau.de/access/ssh-vscode/).

## Next Steps
- If the issue persists, a ZOOM call can be arranged to troubleshoot the problem interactively.

## Documentation Links
- [Environment Modules](https://doc.nhr.fau.de/environment/modules/)
- [Python Environments](https://doc.nhr.fau.de/environment/python-env/)
- [VSCode SSH](https://doc.nhr.fau.de/access/ssh-vscode/)

## Support Team
- **HPC Admins**: Provided guidance on module availability and installation.
- **2nd Level Support Team**: Available for further assistance if needed.

## Conclusion
The user was informed about the correct procedures for using environment modules and configuring VSCode. If the problem persists, a direct troubleshooting session via ZOOM can be arranged.
---

### 2024052942000402_about%20docker.md
# Ticket 2024052942000402

 # HPC Support Ticket: Using Docker on TinyX

## Keywords
- Docker
- Apptainer
- HPC Systems
- Environment Configuration
- Permissions
- Python Modules
- Python Environments

## Problem Description
- User attempted to use Docker on TinyX and encountered issues with permissions when trying to update using `sudo apt-get update`.
- User was prompted for a password but received an error indicating the password was incorrect.

## Root Cause
- Direct use of Docker containers is not supported on HPC systems.
- Users do not have permissions to install software using `apt`.

## Solution
- Use Apptainer to run Docker containers on HPC systems.
  - Documentation: [Apptainer on HPC](https://doc.nhr.fau.de/environment/apptainer/)
- Utilize pre-configured Python modules and create Python environments as needed.
  - Documentation: [Python Modules](https://doc.nhr.fau.de/sdt/python/)
  - Documentation: [Python Environments](https://doc.nhr.fau.de/environment/python-env/)
- Consult thesis supervisor for further assistance in setting up the environment on HPC clusters.

## General Learnings
- Docker is not directly supported on HPC systems; Apptainer should be used instead.
- Users do not have permissions to install software using `apt`.
- Python modules and environments are available for customization.
- For additional support, users should consult their thesis supervisors or refer to the provided documentation.
---

### 2021022442002715_Frage%20zwecks%20Package%20Installation.md
# Ticket 2021022442002715

 ```markdown
# HPC-Support Ticket: Frage zwecks Package Installation

## Problem
- User unable to install Python packages due to lack of root access.
- Commands `pip` and `conda` not found.

## Root Cause
- User did not load the necessary Python module.
- User attempted to use `apt install` which requires root access.

## Solution
- Use `module avail python` to list available Python versions.
- Load a Python module using `module load python/X.Y-anaconda`.
- The loaded Python environment includes pre-installed packages like Pandas.
- Additional packages can be installed using `conda` within the loaded environment.

## Keywords
- Python package installation
- Root access
- Module load
- Conda
- Pip
- Python environment

## General Learnings
- Always check available modules using `module avail`.
- Load necessary modules using `module load`.
- Pre-installed environments often include common packages.
- Use environment-specific package managers (e.g., `conda`) for additional installations.

## References
- [Python and Jupyter Documentation](https://hpc.fau.de/systems-services/systems-documentation-instructions/special-applications-and-tips-tricks/python-and-jupyter/)
- [Environment Documentation](https://hpc.fau.de/systems-services/systems-documentation-instructions/environment/#python)
- [TensorFlow Documentation](https://hpc.fau.de/systems-services/systems-documentation-instructions/special-applications-and-tips-tricks/tensorflow/#conda)
```
---

### 2023112342003035_Import%20error%20on%20hpc.md
# Ticket 2023112342003035

 # HPC-Support Ticket Conversation: Import Error on HPC

## Subject: Import error on HPC

### User:
Hello,

I am facing an error with a simple pandas import. My other imports are working fine. Could you help me with this? I am not sure if this is related to HPC or some of my environment-related problem. Below is the error:

```python
import pandas._libs.window.aggregations as window_aggregations
ImportError: /usr/lib/x86_64-linux-gnu/libstdc++.so.6: version `GLIBCXX_3.4.29' not found (required by /home/woody/iwfa/iwfa044h/envs/faps01/lib/python3.11/site-packages/pandas/_libs/window/aggregations.cpython-311-x86_64-linux-gnu.so)
```

I have tried to downgrade the pandas version, but it doesn't help. I ran this command `strings /usr/lib/x86_64-linux-gnu/libstdc++.so.6 | grep GLIBCXX` and it seems version 29 is missing which it is looking for. Below is the output of the command:

```
GLIBCXX_3.4
GLIBCXX_3.4.1
GLIBCXX_3.4.2
GLIBCXX_3.4.3
GLIBCXX_3.4.4
GLIBCXX_3.4.5
GLIBCXX_3.4.6
GLIBCXX_3.4.7
GLIBCXX_3.4.8
GLIBCXX_3.4.9
GLIBCXX_3.4.10
GLIBCXX_3.4.11
GLIBCXX_3.4.12
GLIBCXX_3.4.13
GLIBCXX_3.4.14
GLIBCXX_3.4.15
GLIBCXX_3.4.16
GLIBCXX_3.4.17
GLIBCXX_3.4.18
GLIBCXX_3.4.19
GLIBCXX_3.4.20
GLIBCXX_3.4.21
GLIBCXX_3.4.22
GLIBCXX_3.4.23
GLIBCXX_3.4.24
GLIBCXX_3.4.25
GLIBCXX_3.4.26
GLIBCXX_3.4.27
GLIBCXX_3.4.28
GLIBCXX_DEBUG_MESSAGE_LENGTH
```

Regards,
Shubham

### HPC Admin:
Dear Shubham,

I cannot reproduce your issue. I executed the following commands on alex without any errors:

```bash
module add python
conda create -n test-support python=3.11
conda activate test-support
python3 -m pip install pandas
python3 -c "import pandas"
```

Mit freundlichen Grüßen,
Markus Wittmann

### User:
Dear HPC Admin,

I am doing this on woddy under my miniconda environment. My colleague does not face this problem. I have looked on the web for this. Other people have also faced this problem:

- [Issue with pandas ImportError](https://stackoverflow.com/questions/73866575/issue-with-pandas-importerror-libstdc-so-6-inside-a-conda-environment-running)
- [Anaconda ImportError](https://stackoverflow.com/questions/58424974/anaconda-importerror-usr-lib64-libstdc-so-6-version-glibcxx-3-4-21-not-found)
- [ImportError lib64 libstdc.so.6](https://stackoverflow.com/questions/49875588/importerror-lib64-libstdc-so-6-version-cxxabi-1-3-9-not-found)

Is it normal that pandas import is looking for a dependency in `/usr/lib/x86_64-linux-gnu/libstdc++.so.6` instead of my environment?

Do you suggest to change something? Do you think the top solution on this is okay?

I do not want to change anything with the configs in case it ruins everything.

Regards,
Shubham

### HPC Admin:
Dear Shubham,

The package you are installing is linked against a newer version of libstdc++ than the one installed on the OS. We will not update libstdc++ (only through system updates).

As I said, I cannot reproduce your problem when I install pandas with pip, even not on woody.

How do you install pandas? In case you use conda, which channels are you using?

Best,
Markus Wittmann

### User:
Dear HPC Admin,

Yes, that seems to be the root problem.

I simply run the command `conda install pandas` and by default, it installed version 2.1.1.

This is what I see in my environment:

```bash
conda config --show channels
channels:
  - defaults
```

Shall I use a particular channel? If yes, which channel?

Regards,
Shubham

### HPC Admin:
Dear Shubham,

In general, we do not support private conda/miniconda installations. For this reason, we have an Anaconda installation available through "module add python".

I think your environment is not set up correctly. When I create a new environment with our conda installation and choose Python version 3.11, I already get an updated libstdc++ installed. This works for me whether I then install pandas with pip, conda w/ default channel, or conda w/ conda-forge channel:

```bash
conda create -n test-support python=3.11
conda activate test-support
conda install pandas
python3 -c "import pandas"
```

I would recommend recreating your environment with our installation and explicitly specifying python=3.11 as a package to install.

Best,
Markus Wittmann

### User:
Dear HPC Admin,

Thanks for the suggestion. Could you please share the steps to create a fresh environment that is suggested and supported officially by HPC? Also, the specific commands. How do I use 'module add python' and use other relevant commands?

Regards,
Shubham

### HPC Admin:
Dear Shubham,

Just copy and paste the following commands into your shell:

```bash
module add python
conda create -n NAME_OF_YOUR_ENV python=3.11
conda activate NAME_OF_YOUR_ENV
conda install pandas
python3 -c "import pandas"
```

Best,
Markus Wittmann

### User:
Dear HPC Admin,

Yeah, I have created a test environment for now to test my files. I am installing required packages. I hope this works well.

This environment would be in `/hpc` folder right and not in woddy? I ask because I might have to get a lot of packages and it might occupy huge space. Could this be a problem later?

Regards,
Shubham

### HPC Admin:
Dear Shubham,

To place all newly created environments onto `$WORK`, see [Python and Jupyter](https://hpc.fau.de/systems-services/documentation-instructions/special-applications-and-tips-tricks/python-and-jupyter/#conda), the relevant commands are:

```bash
if [ ! -f ~/.bash_profile ]; then
  echo "if [ -f ~/.bashrc ]; then . ~/.bashrc; fi" > ~/.bashrc
fi
module add python
conda init bash
. ~/.bashrc
conda config --add pkgs_dirs $WORK/software/private/conda/pkgs
conda config --add envs_dirs $WORK/software/private/conda/envs
```

Best,
Markus Wittmann

### User:
Dear HPC Admin,

I followed these steps - the bashrc command, setting pkg_dirs and env_dirs then creation of new conda environment with the commands you mentioned (to get it in `$WORK`). Then I installed all packages and the pandas error was fixed.

However, after a while now I am unable to connect to HPC anymore like I used to normally using ssh in my VS-code. Usually, it requires my password input twice and then connects, now it requests for my password twice and gives an error. I have not changed anything in my ssh connection. Attached screenshot and logs I see in VS code. There is no permission denied error that we usually get in case of wrong password. So it doesn't seem authentication issue to me.

Hope this is an unrelated problem. Do you think if this could be related to the changes I made?

I will be at work tomorrow but will check your response later in the evening and make any changes if required.

Best Regards,
Shubham

### HPC Admin:
Dear Shubham,

There was an error in the code snippet I sent you and it replaced your `.bashrc` instead of `.bash_profile`. We have recovered your original `.bashrc`. Login via VS-code should work as before again.

Best,
Markus Wittmann

### User:
Dear HPC Admin,

Thanks for the fix. It is working fine now.

Let me know if I need to do any changes in `.bashrc` or `.bash_profile`.

Regards,
Shubham

### HPC Admin:
If everything works for you then no further changes are needed.

Best,
Markus Wittmann

---

## What Can Be Learned:

1. **Environment Setup**: The user faced an import error due to a missing `libstdc++` version. The HPC Admin suggested using the official Anaconda installation available through `module add python` and creating a new environment with Python 3.11.

2. **Conda Configuration**: The user was advised to configure conda to use specific directories for packages and environments to avoid space issues in the home directory.

3. **SSH Connection Issue**: The user encountered an SSH connection issue after making changes to their environment. The HPC Admin identified and fixed an error in the provided script that affected the user's `.bashrc` file.

4. **Troubleshooting Steps**: The conversation highlights the importance of following specific steps for environment setup and configuration to avoid common issues. It also demonstrates the process of troubleshooting and resolving problems related to environment configuration and SSH connections.

5. **Documentation**: The HPC Admin provided links to official documentation for further reference, emphasizing the importance of following official guidelines for environment setup and configuration.
---

### 2020040742001971_Module%20not%20found%20error%20when%20sending%20script%20as%20a%20batch%20job%2C%20but%20live%20exec.md
# Ticket 2020040742001971

 ```markdown
# HPC Support Ticket: Module Not Found Error in Batch Jobs

## Keywords
- ModuleNotFoundError
- Pyomo
- Anaconda
- Batch Job
- .bashrc
- Non-interactive Shell

## Problem Description
- **Issue**: Module not found error when submitting a script as a batch job, but the script runs fine when executed live.
- **Details**:
  - Script: `ExactProjectionBasedBilevel_HPC_script.sh`
  - Error: `ModuleNotFoundError: No module named 'pyomo'`
  - Environment: Pyomo 5.6.9, CPython 3.7.6, Anaconda 2020.02
  - Cluster: Woody cluster

## Root Cause
- **Root Cause**: Initialization files of the shell (e.g., `.bashrc`) are not executed in non-interactive shells, leading to an uninitialized PATH and Python environment.

## Solution
- **Solution**: Add `source ~/.bashrc` to the job script to ensure proper initialization of the PATH and Python environment.
- **Additional Tip**: Create a link from `~/.bashrc` to `~/.bash_profile` to ensure automatic sourcing for both interactive and non-interactive shells.

## Additional Notes
- **Node Restriction**: The user opted for single nodes with maximum processor base frequency due to high CPU and RAM requirements.
- **Node Properties**: Suggested using `:any32g` instead of `:sl32g` for better node qualification.

## Conclusion
- **Conclusion**: Proper initialization of shell environment files is crucial for batch job execution. Ensuring `.bashrc` is sourced can resolve module not found errors in non-interactive shells.
```
---

### 2021112942000683_Anaconda%20Environment.md
# Ticket 2021112942000683

 ```markdown
# HPC-Support Ticket: Anaconda Environment Issue

## Subject
Anaconda Environment

## User Issue
- User attempted to create and activate an Anaconda environment on the HPC system.
- Followed the instructions from the official documentation.
- Encountered an error during `conda init bash`.

## Error Details
- Error occurred during the execution of `conda init bash`.
- Traceback indicated a `subprocess.CalledProcessError`.
- Command `['sudo', '/apps/python/3.7-anaconda/bin/python', '-m', 'conda.core.initialize']` returned non-zero exit status 1.

## Root Cause
- The issue was due to an old version of Conda (4.8.2) which had compatibility problems.

## Solution
- HPC Admin suggested using a newer version of Conda.
- User was advised to load the module `python/3.8-anaconda`.

## Keywords
- Anaconda
- Conda
- Environment
- HPC
- Python
- Module
- Error
- Compatibility

## General Learning
- Older versions of Conda may have compatibility issues.
- Updating to a newer version can resolve initialization errors.
- Always check the version compatibility when encountering issues with Conda.
```
---

### 2023052442001734_I%20need%20GDAL%20to%20be%20installed.md
# Ticket 2023052442001734

 # HPC Support Ticket: GDAL Installation Issue

## Keywords
- GDAL installation
- Conda environment
- TinyGPU node
- Python environment
- Permission issues

## Summary
A user encountered issues while trying to install GDAL using both `pip` and `conda` in their Python environment on a TinyGPU node. The user did not have the necessary permissions to install packages in the shared environment.

## Root Cause
1. The user attempted to install GDAL using `pip` and encountered an error.
2. The user tried to use `conda` but encountered issues with the command not being found.
3. The user did not have write permissions in the shared environment.

## Solution
1. **Use TinyGPU Node**: Ensure that the code is built on a TinyGPU node to get GPU support.
   ```bash
   salloc --gres=gpu:1 --partition=rtx3080 --time=00:30:00
   ```

2. **Create Own Conda Environment**: Create a new Conda environment before attempting to install packages.
   ```bash
   module load python
   export http_proxy=http://proxy:80
   export https_proxy=http://proxy:80
   conda create -c conda-forge gdal -n gdal
   ```

3. **Documentation**: Refer to the following documentation for more information:
   - [Getting Started](https://hpc.fau.de/systems-services/documentation-instructions/getting-started/)
   - [Batch Processing](https://hpc.fau.de/systems-services/documentation-instructions/batch-processing/)
   - [Special Applications and Tips & Tricks](https://hpc.fau.de/systems-services/documentation-instructions/special-applications-and-tips-tricks/)
   - [Conda Getting Started](https://conda.io/projects/conda/en/latest/user-guide/getting-started.html)
   - [FAQs](https://hpc.fau.de/faqs/#innerID-13439)
   - [Conda-Forge GDAL](https://anaconda.org/conda-forge/gdal)

## Lessons Learned
- Ensure that users are aware of the need to create their own Conda environments when they do not have write permissions in the shared environment.
- Provide clear instructions on how to allocate a TinyGPU node and set up the necessary environment variables.
- Encourage users to refer to the documentation for detailed instructions and troubleshooting.

## Status
The issue was resolved by providing detailed instructions and documentation links. The user's supervisor was also notified to assist with the basics.
---

### 2022022242001361_Install%20module%20at%20tinyfat.md
# Ticket 2022022242001361

 # HPC Support Ticket: Install Module at Tinyfat

## Keywords
- Python module installation
- Ray module
- Tinyfat cluster
- Missing rights
- Pip installation

## Problem Summary
- **User Issue**: User needs to parallelize Python code using the 'ray' module, which is not installed on the tinyfat cluster.
- **Attempted Solution**: User tried to follow the instructions provided in the documentation but encountered issues due to missing rights.
- **Root Cause**: The system Python does not come with pip installed, and the user did not load the appropriate Python module.

## Solution
- **HPC Admin Response**:
  - Instructed the user to load a Python module as per the documentation.
  - Highlighted that the system Python does not include pip.

## General Learnings
- **Module Loading**: Ensure that users load the appropriate Python module before attempting to install additional packages.
- **Pip Installation**: The system Python on the tinyfat cluster does not include pip, so users need to follow specific instructions for installing packages.
- **Documentation Reference**: Always refer users to the relevant sections of the documentation for detailed instructions.

## Next Steps
- **User Action**: Load the appropriate Python module and follow the instructions for installing the 'ray' module.
- **HPC Admin Action**: Monitor the user's progress and provide further assistance if needed.

## Documentation Links
- [Python and Jupyter Documentation](https://hpc.fau.de/systems-services/systems-documentation-instructions/special-applications-and-tips-tricks/python-and-jupyter/)
- [Ray Installation Documentation](https://docs.ray.io/en/latest/installation.html)

## Ticket Status
- **Closed**: The ticket was closed after providing the user with the necessary instructions.
---

### 2024073042004438_Docker%20Container%20in%20Singularity%20Container%20verwandeln%20-%20iwso040h.md
# Ticket 2024073042004438

 # HPC-Support Ticket: Docker Container in Singularity Container verwandeln

## Keywords
- Docker Container
- Singularity Container
- Python Framework
- OpenDBM
- HPC
- Container Conversion

## Problem
- User wants to convert a Docker container to a Singularity container for increased processing power on HPC.
- The conversion process results in Python modules not being found, specifically the `opendbm` module.

## Root Cause
- The direct conversion of a Docker container to a Singularity container using `singularity build` does not properly handle the Python environment, leading to missing modules.

## Solution
- **Interactive Build**: Create the container as a sandbox, install the necessary Python packages, and then convert it back to a Singularity image.
  - Example: [Interactive build](https://doc.nhr.fau.de/environment/apptainer/)

## Steps Taken
1. User saved the Docker container as a `.tar` file and copied it to the HPC system.
2. User attempted to build the Singularity container using `singularity build dbm.sif docker-archive://dbm.tar`.
3. Python script execution failed due to missing `opendbm` module.
4. HPC Admin suggested using an interactive build to install Python packages within the sandbox environment.

## Additional Resources
- [General Information on Containers](https://doc.nhr.fau.de/environment/apptainer/?h=container)
- [HPC-Cafe Recording on Containers (Sep. 2023)](https://hpc.fau.de/teaching/hpc-cafe/)

## Conclusion
- The ticket was closed after providing the user with the interactive build method as a potential solution.

## Notes
- Building a new container directly on the HPC system may require sudo privileges, which the user does not have.
- The interactive build method allows for more control over the container environment, ensuring all necessary dependencies are installed correctly.
---

### 2022040542002933_Python%20environment.md
# Ticket 2022040542002933

 # HPC Support Ticket: Python Environment

## Keywords
- Python environment
- Conda environment
- Environment transfer
- Windows to Linux
- Slurm job scripts
- Bash script for ML training

## Problem Description
- User encountered errors while trying to install a Python environment from an Anaconda environment file on the HPC system.
- The environment file contained build tags that are platform-dependent, causing conflicts.
- User requested guidance on transferring a functional environment from another user's account.
- User also inquired about writing a bash script to start ML training.

## Root Cause
- The environment.yml file included build tags that are specific to the Windows platform, causing compatibility issues on the Linux-based HPC system.
- Some packages in the environment file were not available on the HPC system.

## Solution
- **Environment Transfer**:
  - Use the `--no-build` option to export the environment file on Windows, which removes platform-specific build tags.
  - Manually remove any Windows-specific packages from the environment file.
  - Share the environment between accounts by setting read and execute permissions for the owner and adding the environment to the user's `~/.conda/environments.txt` file.

- **Bash Script for ML Training**:
  - Refer to the HPC documentation for examples of Slurm job scripts and Python-specific documentation.
  - Documentation links:
    - [Batch Processing](https://hpc.fau.de/systems-services/systems-documentation-instructions/batch-processing/)
    - [Clusters](https://hpc.fau.de/systems-services/systems-documentation-instructions/clusters/)
    - [Python and Jupyter](https://hpc.fau.de/systems-services/systems-documentation-instructions/special-applications-and-tips-tricks/python-and-jupyter/)
    - [TensorFlow and PyTorch](https://hpc.fau.de/systems-services/systems-documentation-instructions/special-applications-and-tips-tricks/tensorflow-pytorch/)

## Additional Notes
- The environment file contained around 200 Python packages, making it challenging to identify which packages were essential for the user's work.
- The ticket was closed due to no further response from the user, indicating that the issue might have been resolved or was no longer relevant.
---

### 2024071342000312_Unable%20to%20activate%20a%20conda%20environment%20in%20jupyter%20hub%20-%20iwi5141h.md
# Ticket 2024071342000312

 # HPC Support Ticket: Unable to Activate Conda Environment in Jupyter Hub

## Keywords
- Conda environment
- Jupyter Hub
- `conda activate`
- `conda init`
- `ipykernel`
- HTTP error
- Proxy configuration

## Problem Description
- User unable to activate a Conda environment in Jupyter Hub.
- Error message: `CommandNotFoundError: Your shell has not been properly configured to use 'conda activate'.`
- Additional issue: HTTP error when trying to install `ipykernel`.

## Root Cause
- Shell not properly configured to use `conda activate`.
- Compute nodes lack direct internet access, causing HTTP errors during package installation.

## Solution
1. **Configure Shell for Conda:**
   - Run `conda init <SHELL_NAME>` to initialize the shell.
   - Restart the shell after running the command.

2. **Install and Register `ipykernel`:**
   - Follow the instructions in the [FAU documentation](https://doc.nhr.fau.de/environment/python-env/#using-environments-in-jupyter-notebooks-and-jupyterhub) to install `ipykernel` and register the environment in Jupyter.

3. **Configure Proxy for Internet Access:**
   - Add a proxy to allow internet access on compute nodes.
   - Refer to the [FAU FAQ](https://doc.nhr.fau.de/faq/#why-does-my-application-give-an-http-https-timeout) for proxy configuration details.

## Additional Notes
- Restart the kernel to use updated packages.
- HTTP errors are often intermittent; retrying the command may resolve the issue.

## References
- [FAU Documentation on Python Environments](https://doc.nhr.fau.de/environment/python-env/#using-environments-in-jupyter-notebooks-and-jupyterhub)
- [FAU FAQ on HTTP/HTTPS Timeout](https://doc.nhr.fau.de/faq/#why-does-my-application-give-an-http-https-timeout)
---

### 2024081542002501_Required%20help%20to%20install%20lxml%20module.md
# Ticket 2024081542002501

 # HPC Support Ticket: Required Help to Install lxml Module

## Keywords
- lxml module
- ImportError
- virtual environment
- permission error
- conda install

## Problem Description
- User encountered an `ImportError: No module named lxml` while using the 'EXCITING' software.
- Attempted to install the lxml module using `pip3 install lxml` but encountered a permission error.

## Root Cause
- The user did not have the necessary permissions to install the module globally.

## Solution
- **Virtual Environment**: The HPC Admin suggested creating a virtual environment to avoid permission issues.
  - Instructions for creating a virtual environment can be found at [Python Environment Documentation](https://doc.nhr.fau.de/environment/python-env/).
- **Conda Install**: The lxml module was successfully installed in the virtual environment using the command `conda install lxml`.

## Additional Notes
- For future support requests, users should contact the support team via `support-hpc@fau.de` instead of `hpc@fau.de`.

## Conclusion
- The issue was resolved by creating a virtual environment and installing the lxml module using conda.

---

This documentation can be used to resolve similar issues related to module installation and permission errors in the future.
---

### 2024072542003976_WaSiM-ETH%20executable%20installation%20on%20Woody%20cluster.md
# Ticket 2024072542003976

 # HPC Support Ticket: WaSiM-ETH Executable Installation on Woody Cluster

## Keywords
- WaSiM-ETH
- Woody cluster
- Permission denied
- Python os module
- Anaconda environment
- subprocess.Popen
- File permissions

## Problem Description
- User is attempting to run WaSiM-ETH simulations on the Woody cluster using a Python script.
- The script uses `subprocess.Popen` to execute the WaSiM executable with a control file.
- The user encounters a "permission denied" error when trying to run the WaSiM executable.
- The user has already loaded the necessary modules (python, open mpi, netcdf) and created an Anaconda environment with required packages.

## Root Cause
- The "permission denied" error suggests that the user may not have the necessary file permissions to execute the WaSiM executable.

## Solution
- Check the file permissions using the `ls -l filename` command.
- Ensure that the user has execute permissions for the WaSiM executable.

## Additional Information
- The Python `os` module is allowed on the cluster.
- The user is utilizing simple methods such as `os.unlink()` and `os.mkdir()`.

## Follow-up Actions
- Verify that the WaSiM executable has the correct permissions.
- If necessary, adjust the file permissions using the `chmod` command.

## Example Command
```bash
ls -l wasim_executable
chmod +x wasim_executable
```

## Notes
- The user has a WaSiM file compiled by a researcher using the FAU HPC.
- The user's username is gz16103h.

## References
- HPC Admin: Alireza
- FAU HPC Support: support-hpc@fau.de
- FAU HPC Website: [FAU HPC](https://hpc.fau.de/)
---

### 2023051542003277_Conda%20environments.md
# Ticket 2023051542003277

 # Conda Environment Setup Issue

## Keywords
- Conda
- Environment Setup
- NoWritablePkgsDirError
- NoEnvsDir
- Conda Config

## Problem
User encountered `NoWritablePkgsDirError` while trying to create a Conda environment, indicating no writeable package directories were configured.

## Root Cause
The user skipped the optional Conda config changes mentioned in the instructions, which are necessary to set up writeable package and environment directories.

## Solution
To resolve the `NoWritablePkgsDirError`, configure the package directory using:
```bash
conda config --add pkgs_dirs $WORK/conda/pkgs
```
To resolve potential `NoEnvsDir` errors, configure the environment directory using:
```bash
conda config --add envs_dirs $WORK/conda/envs
```

## General Learnings
- Conda config changes might be necessary to set up writeable directories for packages and environments.
- Skipping optional steps in instructions can lead to errors.
- HPC Admins can assist with issues related to software configuration and environment setup.
---

### 2024101542005183_Python%20venv%20auf%20Testcluster.md
# Ticket 2024101542005183

 # Python venv auf Testcluster

## Problem
- User benötigt Python `venv` auf Testcluster-Nodes.
- Früher gab es `python3.10-venv` auf `cshpc`, aber jetzt fehlt `pip` und `venv` auf `csnhr`.

## Ursache
- `pip` und `venv` wurden absichtlich entfernt, um Probleme durch AI-Nutzer zu vermeiden.

## Lösung
- `python-venv` wurde in die Autoinstallation/Ansible aufgenommen.
- Eintrag in `pollux://srv/ansible/roles/setup-misc/tasks/main.yml`.
- Nach Update auf Ubuntu 24.04 sollten alle Nodes `python-venv` installiert haben.

## Ergebnis
- `venv` funktioniert auf `Testfront`, aber nicht auf `gracesup1`.
- User kann erstelltes `venv` auf anderen Knoten verwenden.

## Zusammenfassung
- User können `venv` auf `Testfront` verwenden.
- Nach Update auf Ubuntu 24.04 sollten alle Nodes `python-venv` installiert haben.

## Keywords
- Python venv
- Testcluster
- Ansible
- Ubuntu 24.04
- cshpc
- csnhr
- pip
- Virtual Environments
---

### 2018071942000224_Dask%20Update.md
# Ticket 2018071942000224

 # HPC Support Ticket: Dask Update

## Keywords
- Dask
- Anaconda
- Python Module
- Version Update
- Self-Installation

## Problem
- User requested to update the Dask module in Anaconda 2.7 to the latest version 0.18.

## Root Cause
- The latest version of Dask available via Anaconda was 0.14.3-py35_1.

## Solution
- HPC Admin informed the user that if version 0.18 was required, it would need to be installed manually in the user's directory.
- After several iterations of updating Python packages, Dask 0.18 was successfully installed.

## General Learnings
- Not all desired versions of software modules may be available through standard package managers.
- Manual installation in user directories can be a viable solution for obtaining specific versions.
- Multiple iterations of updates may be necessary to achieve the desired configuration.
---

### 2021120342000694_Execute%20script.py%20on%20Meggie.md
# Ticket 2021120342000694

 # HPC Support Ticket: Execute Python Script on Meggie

## Keywords
- Python script execution
- Meggie cluster
- venv
- Anaconda
- System Python

## Problem
- User wants to execute a Python script on the Meggie cluster.
- User prefers not to use Anaconda due to its size.
- User inquires about using the system Python interpreter with `venv`.

## Solution
- It is possible to use `venv` with the system Python on all clusters.
- HPC Admin recommends using one of the Anaconda Python installations for reproducibility.
- Anaconda installations are mostly frozen and work with `venv`.

## General Learnings
- Users can use `venv` with the system Python on HPC clusters.
- Anaconda is recommended for reproducibility and stability.
- Anaconda installations are compatible with `venv`.

## References
- No specific documentation referenced in the conversation.

## Next Steps
- Users should consider using Anaconda for reproducible results.
- If users prefer not to use Anaconda, they can proceed with the system Python and `venv`.
---

### 2018120442001376_Fehlermeldung%20beim%20Job%20submitten%20an%20den%20HPC.md
# Ticket 2018120442001376

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject: Fehlermeldung beim Job submitten an den HPC

### Keywords:
- Job submission
- Python
- numpy module
- ImportError
- HPC account
- Grundausstattung

### Problem Description:
The user is experiencing an issue with submitting a job to the HPC that requires the `numpy` module in Python. The job fails with an `ImportError: No module named numpy` error, despite the module working correctly when Python is used normally on the user's HPC account.

### Root Cause:
The `numpy` module is not available in the Python environment used for job submission, even though it is available in the user's normal HPC account environment.

### Solution:
- Ensure that the Python environment used for job submission includes the `numpy` module.
- Verify that the job submission script correctly loads the necessary modules and dependencies.

### General Learnings:
- Differences in module availability between interactive and job submission environments.
- Importance of ensuring that all required modules are loaded in the job submission script.
- Common troubleshooting steps for `ImportError` in Python jobs.

### Next Steps:
- HPC Admins should investigate the discrepancy in module availability.
- 2nd Level Support team can assist in verifying and updating job submission scripts.
```
---

### 2023011742000971_Module%20nicht%20verf%C3%83%C2%BCgbar%3F.md
# Ticket 2023011742000971

 ```markdown
# HPC-Support Ticket: Module nicht verfügbar?

## Keywords
- Module not available
- Python installation
- Module avail
- Certificate expired
- Temporary solution

## Problem Description
- User is starting their Master's thesis and needs to install Python.
- User cannot see which Python versions are available on the server.
- User provided output for `module avail` and `module avail python`.

## Root Cause
- The certificate for the module system has expired.

## Solution
- HPC Admins are investigating the issue.
- Temporary solution provided: `source /apps/modules/5.1.1/etc/initic`

## Lessons Learned
- Always use the official support email address for inquiries.
- Certificate expiration can cause issues with module availability.
- Temporary workarounds can be provided while the issue is being resolved.

## Next Steps
- Continue investigating the certificate expiration issue.
- Ensure users are aware of the temporary solution until the issue is fixed.
```
---

### 2018121142001871_pip%20Problem.md
# Ticket 2018121142001871

 # HPC Support Ticket: pip Problem

## Keywords
- pip
- Python
- Anaconda
- EnvironmentError
- Read-only file system
- `--user` option

## Problem Description
The user encountered an `EnvironmentError` when trying to install a Python package using `pip`. The error message indicated a read-only file system issue.

## Root Cause
The user was attempting to install a package in a system-wide directory where they did not have write permissions.

## Solution
The HPC Admin advised the user to use the `--user` option with the `pip install` command to install the package in the user's home directory, where they have write permissions.

```bash
pip install --user <Paket>
```

## Outcome
The user confirmed that the solution worked and thanked the HPC Admin for the assistance.

## General Learning
- When encountering permission issues while installing Python packages with `pip`, use the `--user` option to install the package in the user's home directory.
- This approach avoids the need for elevated permissions and prevents modifications to system-wide directories.
---

### 2022080642000561_Console%20problem.md
# Ticket 2022080642000561

 # HPC Support Ticket: Console Problem

## Keywords
- Conda environment
- Linux
- .bashrc
- Console crash
- Bash

## Problem Description
- User attempted to use Conda environment but encountered issues with the console.
- User executed `source /.bashrc` and received an error.
- User modified `~/.bashrc` with specific content, leading to a console crash with the message "Warning: Program '/bin/bash' crashed".

## Root Cause
- Incorrect modification of the `~/.bashrc` file caused the Bash shell to crash upon startup.

## Solution
- To resolve the issue, the user should:
  1. Access the system using a different shell or a recovery mode if available.
  2. Edit the `~/.bashrc` file to remove or correct the problematic content.
  3. Restart the terminal session.

## General Learnings
- Users unfamiliar with Linux should be cautious when modifying system files like `.bashrc`.
- Incorrect modifications to shell configuration files can lead to critical issues such as shell crashes.
- Always keep a backup of configuration files before making changes.
- Provide clear instructions and warnings when guiding users through shell configuration changes.

## Next Steps for Support
- Assist the user in accessing the system through an alternative method to fix the `.bashrc` file.
- Provide guidance on proper usage of Conda environments and shell configuration.
- Consider offering training sessions or documentation for new Linux users.
---

### 2020092342000762_Trace_BPT%20trap%20Meldung%20beim%20Start%20von%20Spyder.md
# Ticket 2020092342000762

 # HPC-Support Ticket: Trace/BPT Trap Error with Spyder

## Subject
Trace/BPT trap Meldung beim Start von Spyder

## User Issue
- User reports that Spyder, a Python development environment, fails to start after a downtime, with the error message "Trace/BPT trap."
- The issue started after a recent downtime.

## HPC Admin Actions
1. **Initial Information Request:**
   - Requested additional information about the frontend and Python installation being used.

2. **Troubleshooting Steps:**
   - Suggested reinstalling Spyder using `pip` or `conda`.
   - Requested the user to enable `faulthandler` and reproduce the error to gather more detailed output.

3. **Detailed Error Analysis:**
   - User provided detailed error outputs for different Python environments.
   - Identified that the issue persists even with a new virtual environment.

4. **Root Cause Identification:**
   - Determined that a system configuration change during the downtime caused the issue.
   - Specifically, the change in `/etc/sysctl.d/97-no-user-namespaces.conf` with `user.max_net_namespaces=10` prevented Spyder from starting its GUI.

5. **Resolution:**
   - Reverted the system configuration change to resolve the issue.
   - Informed the user that their virtual environment should now work correctly.

## Key Takeaways
- System configuration changes can have unintended side effects on user applications.
- Detailed error outputs are crucial for diagnosing and resolving issues.
- Spyder's GUI startup can be affected by system-level settings related to user namespaces.

## Solution
- Revert the system configuration change in `/etc/sysctl.d/97-no-user-namespaces.conf` to allow Spyder to start its GUI.
- Ensure that any future system configuration changes are thoroughly tested to avoid similar issues.

## Additional Notes
- Users can work around the issue by tunneling the Spyder kernel (IPython) to their client, as described in the [Spyder documentation](https://docs.spyder-ide.org/current/ipythonconsole.html).
- Regular communication and detailed error reporting are essential for efficient troubleshooting.
---

### 2016041142002541_Zusaetzliches%20Python%20Packet.md
# Ticket 2016041142002541

 # HPC Support Ticket: Additional Python Package

## Keywords
- Python 2.7
- PIP package manager
- GDAL package
- `--user` option
- `--prefix` option
- `$HOME` installation
- `libgdal` dependency

## Problem
- User needs access to GDAL functions from a Python script.
- GDAL is already installed, but the Python package is missing.
- System-wide installation of the GDAL Python package is difficult due to `libgdal` dependency.

## Solution
- Use PIP with the `--user` option to install the GDAL package locally in the user's home directory.
- Specify the installation path using the `--prefix` option if needed.
- Example command: `pip install --install-option="--prefix=$PREFIX_PATH" package`

## General Learnings
- PIP can install packages locally using the `--user` option.
- The `--prefix` option can be used to specify the installation path.
- Some Python packages may have system-level dependencies that complicate system-wide installation.
- Local installation can be a workaround for such cases.
- The HPC system is transitioning from Python 2.7.1 to Python 2.7-anaconda.
---

### 2023101642004193_Unable%20to%20create%20condo%20environment.md
# Ticket 2023101642004193

 # HPC Support Ticket: Unable to Create Conda Environment

## Keywords
- Conda Environment
- Permission Issues
- Configuration
- `pkgs_dirs`
- `envs_dirs`

## Problem Description
- **User Issue:** Unable to create a Conda environment, possibly due to permission issues.
- **Error Context:** The user previously created an environment with the same command without issues.

## Root Cause
- Missing or incorrect Conda configuration settings for package and environment directories.

## Solution
- **Configuration Steps:**
  ```bash
  conda config --add pkgs_dirs $WORK/software/privat/conda/pkgs
  conda config --add envs_dirs $WORK/software/privat/conda/envs
  ```
- **Explanation:** These commands set the directories where Conda will store packages and environments, ensuring proper permissions and avoiding conflicts.

## General Learning
- **Conda Configuration:** Ensure that Conda is properly configured to use directories where the user has write permissions.
- **Troubleshooting:** When encountering permission issues, check and update Conda configuration settings for package and environment directories.

## Next Steps
- Verify the configuration settings and attempt to create the Conda environment again.
- If the issue persists, further investigate the specific error message provided in the screenshot.

---

This documentation can be used to resolve similar issues related to Conda environment creation and permission errors.
---

### 2021052742001787_Frage%20zur%20Verwendung%20von%20Woody.md
# Ticket 2021052742001787

 # HPC Support Ticket: Using Woody for ML Model Training

## Keywords
- HPC
- Machine Learning
- PyTorch
- Conda
- $WORK directory
- SSH
- Woody

## Problem Description
The user was unable to locate the `$WORK` directory after logging into the HPC system via SSH. The user needed to install PyTorch for Conda in this directory to train their ML model.

## Root Cause
The user was not aware that `$WORK` is an environment variable pointing to a specific directory path.

## Solution
The HPC Admin provided the following solution:
- `$WORK` is an environment variable that can be accessed directly using `cd $WORK`.
- The absolute path for the `$WORK` directory in this case is `/home/woody/rzku/mlvl029h`.

## General Learnings
- Understand the concept of environment variables in HPC systems.
- Know how to navigate to the `$WORK` directory using the environment variable.
- Be aware of the specific directory structure and paths used in the HPC system.

## Related Teams
- HPC Admins
- 2nd Level Support Team
- Software and Tools Developers

## Relevant Contacts
- HPC Services: support-hpc@fau.de
- HPC Website: [http://hpc.fau.de/](http://hpc.fau.de/)

## Additional Notes
- Ensure that users are informed about the use of environment variables during onboarding or training sessions.
- Provide clear documentation on directory structures and paths for new users.
---

### 2023110542000545_HPC%3A%20Problems%20of%20Failed%20to%20Create%20Conda%20Environment.md
# Ticket 2023110542000545

 # HPC Support Ticket: Failed to Create Conda Environment

## Keywords
- Conda Environment
- NoWritablePkgsDirError
- Python/3.9-anaconda
- Pycharm
- SSH
- Interactive Batch Job
- GPU

## Problem Description
- **User Issue**: Unable to create a Conda environment on HPC.
- **Error Message**: `NoWritablePkgsDirError: No writeable pkgs directories configured. - /apps/python/3.9-anaconda/pkgs`
- **Context**: User connected Pycharm to HPC via SSH, loaded Python module, and configured Conda.

## Root Cause
- The Conda environment creation failed due to lack of write permissions in the specified package directory.

## Solution
- **Reference**: [FAQ on Conda](https://hpc.fau.de/faqs/#ID-242)
- **Steps**:
  1. Follow the instructions in the FAQ to resolve the Conda configuration issue.
  2. Use an interactive batch job for building Python software, especially when working with GPUs.
  3. Refer to the documentation for [Python and Jupyter](https://hpc.fau.de/systems-services/documentation-instructions/special-applications-and-tips-tricks/python-and-jupyter/) and [TensorFlow/PyTorch](https://hpc.fau.de/systems-services/documentation-instructions/special-applications-and-tips-tricks/tensorflow-pytorch/).

## General Learnings
- Ensure proper configuration of Conda environments on HPC systems.
- Use interactive batch jobs for GPU-related tasks.
- Refer to HPC documentation and FAQs for common issues and solutions.

## Support Team Involvement
- **HPC Admins**: Provided links to relevant documentation and FAQs.
- **Supervisor**: Suggested as a point of contact for further assistance.

## Additional Notes
- The user was advised to consult their supervisor for additional help.
- Ensure proper permissions and configurations when setting up development environments on HPC systems.
---

### 2024120442001177_%5BCMRI%2024WS%5D%20Asking%20to%20install%20tqdm%20package%20in%20CONDA-CMRI-24WS.md
# Ticket 2024120442001177

 ```markdown
# HPC Support Ticket: Installing tqdm Package in CONDA-CMRI-24WS Environment

## Summary
A user requested the installation of the `tqdm` package in the CONDA-CMRI-24WS environment. The package was omitted from the initial `environment.yaml` file.

## Keywords
- tqdm package
- CONDA-CMRI-24WS environment
- environment.yaml
- package installation

## Root Cause
The `tqdm` package was not included in the initial `environment.yaml` file provided by the user.

## Solution
The HPC Admin installed the `tqdm` package along with the `colorama` package to the CONDA-CMRI-24WS environment. The versions installed were:
- `colorama`: conda-forge/noarch::colorama-0.4.6-pyhd8ed1ab_1
- `tqdm`: conda-forge/noarch::tqdm-4.67.1-pyhd8ed1ab_0

## Outcome
The user confirmed that the installation was successful and the environment worked perfectly.

## Lessons Learned
- Ensure all necessary packages are included in the `environment.yaml` file before building the environment.
- HPC Admins can quickly install additional packages upon user request, but it may require some adjustments to the environment.

## Follow-up Actions
- None required. The ticket was closed after the user confirmed the successful installation.
```
---

### 2021111242001749_AW%3A%20new%20HPC%20accounts.md
# Ticket 2021111242001749

 ```markdown
# HPC Support Ticket: AW: new HPC accounts

## Summary
User encountered issues with conda environment setup in a new HPC account.

## Keywords
- Conda
- EnvironmentNotWritableError
- Solving environment
- HPC account setup
- Permissions

## Problem
- User received `EnvironmentNotWritableError` when trying to install packages in the base environment.
- User experienced a hang at "Solving environment" when trying to install packages in a new environment.

## Root Cause
- The base environment is located in `/apps/python/3.8-anaconda` and is read-only for users.
- The user's previous `.bashrc` configuration might have caused conflicts.

## Solution
- The base environment is system-wide and read-only for users. Users should create their own environments.
- Full Anaconda installation can take a long time. Cloning the base environment is recommended.
- Ensure that the user is not copying old configuration files that might cause conflicts.

## Lessons Learned
- Users should not attempt to modify system-wide environments.
- Cloning the base environment is a more efficient way to set up a new environment.
- Ensure that old configuration files do not interfere with new account setup.

## Actions Taken
- HPC Admin explained the read-only nature of the base environment.
- HPC Admin suggested cloning the base environment for a faster setup.
- User confirmed that the issue was resolved by cloning the base environment.

## Additional Notes
- New HPC accounts were created with a unique prefix and customer numbers.
- Users should specify the correct customer number and FAU.org number on the HPC form for new colleagues.
```
---

### 2022102542003213_module%3A%20command%20not%20found%20in%20bash%20scripts.md
# Ticket 2022102542003213

 # HPC Support Ticket: Module Command Not Found in Bash Scripts

## Keywords
- `module: command not found`
- `bash script`
- `batch run`
- `module load`
- `-l flag`

## Problem Description
The user is able to load modules from the terminal but encounters an error when trying to load modules within a bash script for a batch run. The script returns the error `module: command not found`.

## Root Cause
The script does not have the `-l` flag in the shebang line, which is necessary for loading the user's environment and making the `module` command available.

## Solution
Add the `-l` flag to the shebang line of the bash script to ensure the user's environment is loaded properly.

```bash
#!/bin/bash -l
module load intel
```

## General Lessons Learned
- Always include the `-l` flag in the shebang line of bash scripts intended for batch runs to load the user's environment.
- Ensure that the script has the necessary permissions to execute.
- Verify that the script follows the guidelines provided in the relevant documentation or slides.

## References
- [HPC in a Nutshell Slides](https://www.rrze.fau.de/files/2019/05/2019-05-09_HPC_in_a_Nutshell2-2.pdf)
- FAU HPC Support: `support-hpc@fau.de`
- FAU HPC Website: [https://hpc.fau.de/](https://hpc.fau.de/)
---

### 2023061242003842_Failing%20loading%20module.md
# Ticket 2023061242003842

 ```markdown
# HPC Support Ticket: Failing to Load Module

## Keywords
- Module loading error
- SLURM
- Python module
- Configuration files
- Node updates

## Problem Description
- User unable to load the Python module in a SLURM job script.
- Error message: `ERROR: Unable to locate a modulefile for ‘python’.`
- Job script was working previously but failed after an update.

## Root Cause
- Node updates caused corruption in configuration files (`/etc/profile.d/modules.{csh,sh}` and `/etc/profile.d/scl-init.{csh,sh}`).

## Solution
- HPC Admins removed the corrupted configuration files using the following commands:
  ```sh
  dsh -a rm /etc/profile.d/modules.{csh,sh}
  dsh -a rm /etc/profile.d/scl-init.{csh,sh}
  ```
- Nodes that had not been rebooted were reserved to fix the profile configurations before being put back into operation.

## Additional Notes
- A copy-in script was suggested to fix the issue in a reproducible manner.
- All nodes were updated, and the workaround script to delete the problematic files was successful.
- The problem should not reoccur.

## Lessons Learned
- Node updates can corrupt configuration files, leading to module loading errors.
- Manual intervention may be required to fix corrupted configuration files.
- A reproducible script can help automate the fix for similar issues in the future.
```
---

### 2023110642002952_ModuleNotFoundError.md
# Ticket 2023110642002952

 # HPC Support Ticket: ModuleNotFoundError

## Keywords
- ModuleNotFoundError
- Python libraries
- Environment setup
- Proxy settings
- Documentation links

## Problem Description
- User encountered `ModuleNotFoundError` when running a Python script via SSH.
- User inquired about collecting all installed libraries in a folder and executing them via a shell script.

## Root Cause
- The preinstalled Python environment on the HPC system has a limited number of packages.
- User needs to set up their own Python environment with the required libraries.

## Solution
- **Environment Setup**:
  - Refer to the provided documentation links for setting up a custom Python environment:
    - [FAQs](https://hpc.fau.de/faqs/#ID-242)
    - [Python and Jupyter](https://hpc.fau.de/systems-services/documentation-instructions/special-applications-and-tips-tricks/python-and-jupyter/)
    - [TensorFlow and PyTorch](https://hpc.fau.de/systems-services/documentation-instructions/special-applications-and-tips-tricks/tensorflow-pytorch/)
- **Proxy Settings**:
  - Ensure proper proxy settings are configured in the shell script:
    ```sh
    source ~/.bashrc
    export http_proxy="http://proxy:80"
    export https_proxy="http://proxy:80"
    ```
- **Introduction Session**:
  - Attend the upcoming introduction session for beginners:
    - Date: Wednesday, November 15, 2023, 4:00 p.m.
    - Location: [Zoom Link](https://fau.zoom.us/j/63416831557)
    - Slides: [HPC in a Nutshell](https://hpc.fau.de/files/2023/07/2023-07-12_HPC_in_a_Nutshell.pdf)
- **Supervisor Assistance**:
  - Seek help from the supervisor at AIBE for initial software setup.

## General Learning
- Always ensure the Python environment is properly set up with all required libraries.
- Utilize provided documentation and resources for environment configuration.
- Attend training sessions and seek assistance from supervisors or support teams when needed.
---

### 2023021642001675_Modul%3A%20Mono.md
# Ticket 2023021642001675

 # HPC Support Ticket: Mono Module Installation Request

## Keywords
- Mono
- .exe files
- Linux
- Windows
- .net framework
- Spack
- numpy
- Converter
- .frd to .vtk

## Summary
A user requested the installation of the Mono module to open .exe files on the HPC cluster. The user needed to convert .frd files to .vtk files using a converter available only as a .exe file.

## Root Cause
- The user misunderstood the capabilities of Mono, thinking it could run Windows .exe files directly on Linux.
- The user needed a specific converter tool that was only available as a Windows .exe file.

## Solution
- The HPC Admin explained that Mono cannot run Windows .exe files directly on Linux and suggested using Spack to install Mono if necessary.
- The user then requested the installation of numpy to use an alternative converter from GitHub.
- The HPC Admin provided guidance on using Spack to install Mono if needed.

## What Can Be Learned
- Mono is an open-source implementation of Microsoft's .net framework, not a tool to run Windows .exe files on Linux.
- Spack can be used to install additional software packages on the HPC cluster.
- It's important to understand the differences between Windows and Linux executables and the tools available for cross-platform compatibility.
- Always check for alternative tools or libraries that can perform the same task on the required platform.

## Follow-up Actions
- If a user requests software for cross-platform compatibility, clarify the specific needs and suggest appropriate tools or libraries.
- Provide guidance on using package managers like Spack for installing additional software.
- Document common misconceptions and solutions for future reference.
---

### 2023041242003481_Tmux%20Lost%20Server%20message.md
# Ticket 2023041242003481

 # HPC Support Ticket: Tmux Lost Server Message

## Keywords
- tmux
- lost server
- /tmp/tmux
- .bashrc
- .bash_profile
- Python 3.10
- OpenGL
- spack
- mesa

## Summary
- User encountered a "lost server" error with tmux.
- User requested updates for tmux, Python, and OpenGL.
- User needed guidance on creating and using .bashrc and .bash_profile files.

## Root Cause
- tmux server issue due to leftover files in /tmp/tmux.

## Solutions
### tmux Issue
- **Solution**: Kill tmux processes and remove the corresponding files in /tmp.
  ```bash
  pkill tmux
  rm -r /tmp/tmux-`id -u`
  ```
- **Source**: [GitHub Issue](https://github.com/tmux/tmux/issues/2529#issuecomment-757440883)

### .bashrc and .bash_profile
- **Solution**: Create .bashrc and .bash_profile files manually.
  ```bash
  if [ -f ~/.bashrc ]; then
    . ~/.bashrc
  fi
  ```
- **Source**: [Bash Documentation](https://www.gnu.org/savannah-checkouts/gnu/bash/manual/bash.html#Bash-Startup-Files)

### Python 3.10
- **Solution**: Install Python 3.10 using conda.
  ```bash
  module add python
  conda create --name env-with-py-3.10 python=3.10
  conda activate env-with-py-3.10
  ```

### OpenGL
- **Solution**: Install OpenGL via spack.
  ```bash
  module add user-spack
  spack install --fail-fast mesa
  ```
- **Note**: OpenGL installation can take a long time due to dependencies.

## Additional Notes
- **tmux Update**: tmux updates are tied to the standard Alma Linux distribution updates.
- **spack Installation**: Once installed, spack packages remain available and do not need to be reinstalled each time the module is loaded.

## Conclusion
The user was able to resolve the tmux issue and create the necessary bash startup files. Instructions were provided for installing Python 3.10 and OpenGL via conda and spack, respectively.
---

### 2024110442003561_%5Bgracesup1%5D%20no%20modules%20available.md
# Ticket 2024110442003561

 # HPC Support Ticket: No Modules Available on gracesup1

## Keywords
- `gracesup1`
- `module: command not found`
- `tclsh: No such file or directory`
- `Ubuntu 24.04`
- `Ansible`

## Problem Description
After maintenance, the node `gracesup1` was not functioning correctly. The user encountered errors indicating that the `module` command was not found and `tclsh` was missing.

## Root Cause
The root cause of the problem was the absence of the `tcl8.6` package on the node, which is required for the `module` command to function.

## Solution
The HPC Admin resolved the issue by adding `tcl8.6` to the list of default packages installed on Ubuntu 24.04 using Ansible. The relevant Ansible task was updated to include `tcl8.6` in the package list.

```yaml
- name: 'install default packages on Ubuntu 24.04 (common for all architectures)'
  ansible.builtin.apt:
    name:
      - autoconf
      - automake
      - libtool-bin
      - numactl
      - python3-venv
      - tcl8.6
    state: present
  when: (ansible_distribution_version == "24.04")
```

## Lessons Learned
- Ensure that all necessary packages are installed on nodes after maintenance.
- Verify that the `module` command and its dependencies are available on all nodes.
- Use Ansible to manage and automate the installation of default packages across nodes.

## Follow-up Actions
- Monitor other nodes for similar issues.
- Update documentation to include the list of required packages for Ubuntu 24.04.
- Regularly review and update Ansible playbooks to ensure all necessary packages are included.
---

### 2023111442002893_Scikit-Optimize%20auf%20Meggie.md
# Ticket 2023111442002893

 ```markdown
# HPC-Support Ticket Conversation: Scikit-Optimize auf Meggie

## Keywords
- Scikit-Optimize
- Meggie-Cluster
- Python-Bibliothek
- Anaconda Umgebung
- Python Pakete
- Masterarbeit

## Problem
- User requires the Python library Scikit-Optimize for their Master's thesis.
- Scikit-Optimize is not pre-installed on the Meggie-Cluster.

## Solution
- HPC Admins suggest using the Anaconda environment to install the required Python packages.
- Documentation links provided for setting up Python and Jupyter environments:
  - [Python and Jupyter Documentation](https://hpc.fau.de/systems-services/documentation-instructions/special-applications-and-tips-tricks/python-and-jupyter/)
  - [TensorFlow and PyTorch Documentation](https://hpc.fau.de/systems-services/documentation-instructions/special-applications-and-tips-tricks/tensorflow-pytorch/)
  - FAQ

## General Learnings
- Users should use their @fau.de email for support requests.
- Users can install Python packages themselves using the Anaconda environment.
- Documentation and FAQs are available for setting up Python environments on the Meggie-Cluster.
```
---

### 2022051842002498_importError%20on%20shared%20file.md
# Ticket 2022051842002498

 # HPC-Support Ticket Conversation Summary

## Keywords
- ImportError
- Shared file
- Virtual environment
- Python
- TensorFlow
- GPU
- SLURM script
- TinyGPU
- Alex cluster
- Multi-node
- NHR users
- CUDA error
- Batch size
- Runtime
- HPC-Support
- HPC-Cafe
- Documentation
- Interactive job
- Conda-env
- Virtual-env
- Pip install
- Python module
- Python 3.8
- Python 3.8-anaconda
- Cuda
- Anaconda
- Source activate
- Srun
- Nproc_per_node
- Address already in use
- Libpython3.8.so.1.0
- Libpython3-dev
- Sudo access
- Deepmind-research
- Byol
- Courier
- Pytype
- Import-error
- Python/3.8-anaconda
- Cuda
- Anaconda
- Source activate
- Srun
- Nproc_per_node
- Address already in use
- Libpython3.8.so.1.0
- Libpython3-dev
- Sudo access
- Deepmind-research
- Byol
- Courier
- Pytype
- Import-error

## General Learnings
1. **ImportError on Shared File**:
   - The user encountered an `ImportError` due to a missing shared library file (`libpython3.8.so.1.0`).
   - The issue was related to the lack of sudo access to install `libpython3-dev`.
   - Solution: Use an interactive job on TinyGPU to install the necessary packages.

2. **Virtual Environment Setup**:
   - The user needed to set up a virtual environment on TinyGPU nodes to ensure GPU detection.
   - The user was advised to load the Python 3.8 module and build the environment on TinyGPU nodes.

3. **SLURM Script Adjustments**:
   - The user needed to adjust the SLURM script for multi-GPU training.
   - The user was advised to use `srun` before the Python call and ensure the number of GPUs and processes match.

4. **Submitting Jobs to Alex Cluster**:
   - The user inquired about submitting jobs to the Alex cluster.
   - The user was informed about the application process for NHR users and the documentation for Alex cluster usage.

5. **CUDA Errors**:
   - The user encountered CUDA memory errors when increasing the batch size.
   - The user was advised to adjust the SLURM script and ensure proper GPU allocation.

6. **HPC-Support and Documentation**:
   - The user was directed to various documentation links and support resources such as HPC-Cafe and introductory sessions.
   - The user was advised to contact specific support personnel for further assistance.

## Root Cause and Solutions
1. **ImportError on Shared File**:
   - Root Cause: Missing shared library file (`libpython3.8.so.1.0`).
   - Solution: Use an interactive job on TinyGPU to install the necessary packages.

2. **Virtual Environment Setup**:
   - Root Cause: Incorrect environment setup for GPU detection.
   - Solution: Load the Python 3.8 module and build the environment on TinyGPU nodes.

3. **SLURM Script Adjustments**:
   - Root Cause: Incorrect SLURM script configuration for multi-GPU training.
   - Solution: Use `srun` before the Python call and ensure the number of GPUs and processes match.

4. **Submitting Jobs to Alex Cluster**:
   - Root Cause: Lack of information on submitting jobs to the Alex cluster.
   - Solution: Follow the application process for NHR users and refer to the documentation for Alex cluster usage.

5. **CUDA Errors**:
   - Root Cause: Incorrect GPU allocation and batch size configuration.
   - Solution: Adjust the SLURM script and ensure proper GPU allocation.

6. **HPC-Support and Documentation**:
   - Root Cause: Lack of awareness of available support resources.
   - Solution: Direct the user to documentation links, support resources, and specific support personnel for further assistance.

## Conclusion
The conversation highlights the importance of proper environment setup, SLURM script configuration, and awareness of available support resources. The user was provided with specific solutions to address the encountered issues and directed to relevant documentation and support personnel for further assistance.
---

### 2023082842003489_sudo%20apt%20install%20autoconf.md
# Ticket 2023082842003489

 # HPC Support Ticket: Compilation Issue with BigDFT

## Keywords
- BigDFT compilation
- autoconf
- autoreconf
- module load
- virtual environment
- Python
- Meggie-HPC
- Fritz

## Problem Description
The user encountered an error while trying to compile BigDFT on Meggie-HPC. The error message indicated a problem with `autoreconf -fi` during the setup phase of `futile`. The suggested solution was to install `autoconf`, but the user did not have the necessary permissions to use `sudo apt install autoconf`. Attempting to install `autoconf` via `pip` also did not resolve the issue.

## Root Cause
The root cause of the problem was the absence of the necessary tools (`autoconf`, `automake`, `libtool`) required for the compilation process.

## Solution
### Initial Solution
The HPC Admin provided a solution to load the required modules using the following commands:
```sh
module load user-spack/0.18.1
module load 000-all-spack-pkgs/0.18.1
module load autoconf automake libtool
```
For building BigDFT on Fritz, a different set of module versions was suggested:
```sh
module load user-spack/0.19.1
module load 000-all-spack-pkgs/0.19.1
module load autoconf automake libtool
```

### Updated Solution
The HPC Admin later informed that `autoconf`, `automake`, and `libtool` are now installed as OS packages on the login nodes, eliminating the need to load modules.

## General Learnings
- Ensure that the necessary tools for compilation (`autoconf`, `automake`, `libtool`) are available in the environment.
- Use `module load` commands to access required tools if they are available as modules.
- Check for updates from the HPC Admin regarding the installation of tools as OS packages, which may simplify the process.

## Conclusion
The issue was resolved by ensuring that the necessary tools were available in the environment. The HPC Admin provided the required module load commands and later informed that the tools were installed as OS packages, making the module loading unnecessary.
---

### 2023031042002371_conda%204.10%20on%20alex.md
# Ticket 2023031042002371

 ```markdown
# HPC Support Ticket: Conda 4.10 Compatibility Issue on Alex

## Keywords
- Conda
- Python 3.10
- Compatibility
- Package Installation
- Environment Setup

## Problem
- **User Issue:** Conda 4.10 is incompatible with Python 3.10, causing errors when installing packages in conda environments.
- **Root Cause:** Conda version 4.10.3 on the HPC system "alex" is not compatible with Python 3.10.

## Solution
- **Action Taken:** HPC Admins updated the conda version on "alex" to 23.1.0 using the command `conda install -n base conda==23.1.0`.
- **Resolution:** The update resolved the compatibility issue, allowing the user to install packages with Python 3.10 in conda environments.

## General Learnings
- Ensure that the conda version is compatible with the desired Python version.
- Regularly update conda to the latest version to avoid compatibility issues.
- Use specific commands to update conda in the base environment.

## References
- [Stack Overflow Question](https://stackoverflow.com/questions/69481608/cannot-set-up-a-conda-environment-with-python-3-10)
```
---

### 2024080542001763_Downgrading%20Python.md
# Ticket 2024080542001763

 ```markdown
# HPC Support Ticket: Downgrading Python

## Keywords
- Conda virtual environment
- Python 3.9
- Python 2.7
- 2to3 script
- ModuleNotFound error

## Problem Description
- User created a conda virtual environment with Python 3.9.
- User's Python script is compatible with Python 2.7.
- User wants to deactivate the current environment and activate/downgrade to Python 2.7 in the same working space.

## Root Cause
- Incompatibility between Python versions.
- Missing modules in the Python 3.9 environment that were present in Python 2.7.

## Solution
1. **Separate Environments**:
   - Create separate conda environments for different Python versions.
   - Example:
     ```bash
     conda create --name py27 python=2.7
     conda create --name py39 python=3.9
     ```

2. **Using 2to3 Script**:
   - Use the `2to3` script to convert Python 2.7 code to Python 3.9.
   - Manually check and update module names and imports as needed.

3. **Module Installation**:
   - Reinstall necessary modules in the Python 3.9 environment.
   - Example:
     ```bash
     conda activate py39
     conda install <module_name>
     ```

## Additional Notes
- Environments isolate different Python versions and modules.
- Installations in one environment are not visible in another.
- Manual adjustments may be required after using the `2to3` script.

## Conclusion
- Users should create separate environments for different Python versions.
- Use the `2to3` script to convert code and manually adjust imports.
- Ensure all necessary modules are installed in the new environment.
```
---

### 2021022242001774_Installation%20Python%20package%20cartopy.md
# Ticket 2021022242001774

 # HPC-Support Ticket: Installation Python Package Cartopy

## Subject
Installation Python package cartopy

## User Issue
- User is unable to install the Python package `cartopy` using `pip`.
- Error messages indicate that the required versions of GEOS and Proj are not found.
- User has locally installed Proj (6.0.0) and GEOS (3.8.1), but they are not being detected.

## Error Messages
```
/tmp/pip-install-c7452yek/cartopy/setup.py:107: UserWarning: Unable to determine GEOS version. Ensure you have 3.3.3 or later installed, or installation may fail.
/tmp/pip-install-c7452yek/cartopy/setup.py:160: UserWarning: Unable to determine Proj version. Ensure you have 4.9.0 or later installed, or installation may fail.
Proj version 0.0.0 is installed, but cartopy requires at least version 4.9.0.
Command "python setup.py egg_info" failed with error code 1 in /tmp/pip-install-c7452yek/cartopy/
```

## HPC Admin Response
- Suggested using `conda` for an easier installation of `cartopy`.
- Provided `conda` commands to create an environment and install `cartopy`.
- Offered further assistance if `conda` is not an option.

## User Follow-Up
- User attempted to use `conda` but encountered issues with activating the environment.
- User also tried setting `LD_LIBRARY_PATH` to point to the Proj installation, but it did not help.

## HPC Admin Solution
- Provided detailed instructions for setting up and using `conda`.
- Suggested initializing the shell for `conda` using `conda init <SHELL_NAME>`.

## Keywords
- Python package installation
- Cartopy
- GEOS
- Proj
- Conda
- Pip
- Environment setup
- Shell initialization

## Lessons Learned
- Using `conda` can simplify the installation of complex Python packages like `cartopy`.
- Ensure that the shell is properly configured to use `conda` commands.
- Local installations of dependencies like GEOS and Proj may not be detected by `pip`; using environment managers like `conda` can help manage dependencies more effectively.

## Solution
- Use `conda` to create and activate an environment for `cartopy`.
- Initialize the shell for `conda` if necessary.
- Install `cartopy` and other required packages within the `conda` environment.

```bash
conda create --name cartopy
conda activate cartopy
conda install -c conda-forge cartopy
```

If `conda activate` does not work, initialize the shell:

```bash
conda init <SHELL_NAME>
```

Restart the shell after running `conda init`.
---

### 2024022942002693_Anfrage%20Lammps-Version%20auf%20Alex%20Python%20Modul.md
# Ticket 2024022942002693

 # HPC Support Ticket: LAMMPS Python Module Issue

## Keywords
- LAMMPS
- Python Module
- Import Error
- PYTHONPATH
- Functionality Issue

## Problem Description
The user encountered issues importing the LAMMPS Python module on the HPC system. Despite the module being compiled with Python support, it was not found in the standard Python path. The user suspected a specific file but was unable to import it correctly.

## Root Cause
The LAMMPS Python module was not included in the standard Python path, causing import errors. Additionally, the module exhibited functionality issues, returning incorrect values and warnings about unsupported data types.

## Solution
1. **PYTHONPATH Update**: The HPC Admin updated the PYTHONPATH to include the LAMMPS Python module, allowing for successful imports.
2. **Functionality Testing**: The user tested the module extensively but found it to be non-functional. The issue was reported to the HPC Admin for further investigation.
3. **Future Steps**: The HPC Admin requested the user to provide specific options and a test case for compiling a newer LAMMPS version with improved Python support.

## Lessons Learned
- Ensure that the PYTHONPATH includes all necessary modules for seamless imports.
- Thoroughly test modules for functionality after installation.
- Document any deviations from expected behavior for future reference and user guidance.

## Next Steps
- Compile a newer LAMMPS version with the required options and test cases.
- Continue to monitor and document any issues with the LAMMPS Python module.

## References
- [LAMMPS Python Module Documentation](https://docs.lammps.org/Python_module.html)

---

This report provides a summary of the issue, the steps taken to resolve it, and the lessons learned for future reference.
---

### 2023100242001873_Issue%20with%20conda%20env%20creation.md
# Ticket 2023100242001873

 ```markdown
# Issue with Conda Environment Creation

## Keywords
- Conda
- Environment Creation
- NoWritablePkgsDirError
- Configuration
- $WORK Path

## Problem Description
The user encountered an error while trying to create a Conda environment:
- **Error Message:** "NoWritablePkgsDirError: No writeable pkgs directories configured."

## Root Cause
- The user had not configured Conda in their account.

## Solution
- **Configuration:** The user needs to configure Conda by following the instructions provided in the documentation.
- **Path Configuration:** Use the `$WORK` path for package installation to avoid filling up the home directory with large Conda packages.

## Relevant Documentation
- [Python and Jupyter Documentation](https://hpc.fau.de/systems-services/documentation-instructions/special-applications-and-tips-tricks/python-and-jupyter/)

## Notes
- Ensure that the user is aware of the importance of using the `$WORK` path to prevent storage issues in the home directory.
```
---

### 2023041942003422_Query%20regarding%20package%20installations.md
# Ticket 2023041942003422

 # HPC Support Ticket: Query regarding package installations

## Keywords
- Package installation
- Cluster environment
- CLI (Command Line Interface)
- Programming tutorials
- Non-GUI environment

## Problem
- User is unable to install packages in the cluster.
- User is new to the non-GUI environment and requests guidance and tutorials for programming in such environments.

## Root Cause
- Lack of familiarity with the cluster environment and CLI.

## Solution
- **HPC Admin** provided links to relevant documentation and FAQs:
  - [Getting Started](https://hpc.fau.de/systems-services/documentation-instructions/getting-started/)
  - [FAQs](https://hpc.fau.de/faqs/)
  - [Python and Jupyter](https://hpc.fau.de/systems-services/documentation-instructions/special-applications-and-tips-tricks/python-and-jupyter/)
  - [TensorFlow and PyTorch](https://hpc.fau.de/systems-services/documentation-instructions/special-applications-and-tips-tricks/tensorflow-pytorch/)
- **HPC Admin** advised the user to contact their supervisor for basic CLI and programming support.

## General Learnings
- Users new to HPC environments may require guidance on basic CLI operations and package installations.
- Extensive documentation and FAQs are available to assist users in getting started with the cluster environment.
- For basic programming and CLI support, users should be directed to their supervisors or relevant training resources.
---

### 2024060442000019_HPC%20-%20No%20Space%20left%20on%20device%20-%20Help.md
# Ticket 2024060442000019

 ```markdown
# HPC Support Ticket: No Space Left on Device

## Problem Description
- User encountered an error `ERROR: Could not install packages due to an OSError: [Errno 28] No space left on device` while installing Python packages in a conda environment.
- User reported minimal data in $HOME and $WORK directories.

## Troubleshooting Steps
1. **Initial Investigation**:
   - HPC Admin noted that $HOME and $WORK directories had sufficient space.
   - Suspected issue with conda environment initialization path.

2. **Installation Method**:
   - User connected via SSH and used the default terminal screen to install packages.
   - User also used JupyterHub for experiments.

3. **Detailed Installation Steps**:
   - User created a conda environment and installed several libraries (tensorflow, deepd3, transformers, segment_anything).
   - Error occurred during `pip install monai`.

4. **Admin Testing**:
   - HPC Admin successfully installed the same packages using the following commands:
     ```bash
     module load python
     conda create -n monai
     conda activate monai
     conda install python
     pip install monai
     ```

5. **User Configuration Check**:
   - User provided outputs for `conda info` and `conda env list`.
   - HPC Admin confirmed the conda configuration was correct.

6. **Cache Cleaning**:
   - User cleared the conda cache using `conda clean --all`.
   - Error persisted.

## Root Cause
- **Scratch Space Issue**:
  - HPC Admin identified that the `/scratch` directory on the `tinyx` node was running out of space.

## Solution
- **Use GPU Node**:
  - HPC Admin advised the user to build the conda/pip environment on a GPU node (`tinyGPU`) instead of `tinyx`.
  - Provided links to documentation for starting an interactive job on `tinyGPU` and building the environment.

## References
- [tinyGPU Documentation](https://doc.nhr.fau.de/clusters/tinygpu/)
- [PyTorch Documentation](https://doc.nhr.fau.de/apps/pytorch/)
```
---

### 2024062742003072_Conda%20module%20f%C3%83%C2%BCr%20text%20cluster.md
# Ticket 2024062742003072

 ```markdown
# HPC-Support Ticket: Conda Module for Text Cluster

## Keywords
- Conda module
- Testcluster
- Python
- Anaconda
- ARM-based systems
- Self-installation

## Problem
- User needs to load a Conda module (`python/3.10-anaconda`) on the Testcluster.
- The module is not available in the current module list.

## Root Cause
- Limited software centrally installed for ARM-based systems.

## Solution
- User advised to install Python 3.10 and Anaconda manually in their `$WORK` directory.
- Suggested target architecture: `aarch64`.

## General Learnings
- ARM-based systems may have limited centrally installed software.
- Users may need to install specific software themselves in their working directory.
- Target architecture for ARM-based systems is typically `aarch64`.
```
---

### 2022110842002094_Cartopy%20on%20meggie.md
# Ticket 2022110842002094

 # HPC Support Ticket: Cartopy and ncview Installation Issues

## Keywords
- Cartopy
- ncview
- ncvue
- Conda
- Python
- GEOS
- Shapely
- PyShp
- netCDF
- X libraries

## Problem Description
- User attempted to install `ncvue`, which requires `Cartopy`.
- User lacked privileges to install `Cartopy` via Conda due to non-writable `pkgs` directory.
- Attempted manual installation of `Cartopy` dependencies (GEOS, Shapely, PyShp) and `Cartopy` itself via `pip`, but encountered issues with missing `geos_c.h` file.
- User also faced issues with `ncview` installation due to netCDF version and missing X libraries.

## Root Cause
- Lack of user privileges for Conda package installation.
- Missing dependencies and incorrect netCDF configuration for `ncview`.

## Solution
- HPC Admin suggested adding a package directory in user space:
  ```bash
  conda config --add pkgs_dirs $WOODYHOME/conda/pkgs
  ```
- HPC Admin provided steps to install `ncview` using Conda:
  ```bash
  module load python
  conda create --name ncview
  conda activate ncview
  conda install -c conda-forge ncview
  ```
- User successfully installed `ncview` following the provided steps.

## General Learnings
- Users should be aware of the Python and Jupyter documentation provided by the HPC.
- Adding a package directory in user space can resolve privilege issues for Conda installations.
- Detailed error descriptions and command logs are crucial for troubleshooting.
- Ensure all dependencies and required libraries are correctly installed and configured for software installations.

## Documentation Links
- [Python and Jupyter Documentation](https://hpc.fau.de/systems-services/documentation-instructions/special-applications-and-tips-tricks/python-and-jupyter/)
---

### 2023091442002521_Typo%20%40%20CSHPC%20Login%20Msg.md
# Ticket 2023091442002521

 ```markdown
# HPC-Support Ticket Conversation: Typo @ CSHPC Login Msg

## Keywords
- Login message
- Typo
- Email address
- Python version
- Default Python
- Module load
- Script testing

## Summary
A user reported a typo in the login message email address and requested a change in the default Python version on the CSHPC system.

## Root Cause
- Typo in the email address in the login message.
- Default Python version set to 2.7.18 instead of Python 3.

## Details
- The user noticed a missing "p" in the email address `hpc-suport@fau.de`.
- The user requested to set Python 3 as the default version on CSHPC, as it currently defaults to Python 2.7.18.
- The user mentioned inconsistencies in Python versions across different systems (Woody and Memoryhog), which complicates script testing.

## Solution
- Correct the typo in the email address to `hpc-support@fau.de`.
- Update the default Python version to Python 3 on the CSHPC system.

## Notes
- The user highlighted the importance of consistent Python versions for script testing across different systems.
- The current setup leads to different `module load` commands for each system, which is inconvenient for users.
```
---

### 2022041442000811_Python3%20Bibliothekfehler%20auf%20Meggie.md
# Ticket 2022041442000811

 # HPC Support Ticket: Python3 Library Error on Meggie

## Keywords
- Python3
- Shared Library Error
- libpython3.6m.so.1.0
- Meggie
- Slurm Update
- Python Module
- Virtual Environment

## Problem Description
- User encountered an error while trying to run Python3 on Meggie nodes.
- Error message: `python3: error while loading shared libraries: libpython3.6m.so.1.0: cannot open shared object file: No such file or directory`
- Python3 was working previously but stopped after a recent update.

## Root Cause
- Python3 was not intentionally installed on the nodes and might have been pulled in as a dependency during a previous Slurm update.
- Recent updates might have removed or altered the Python3 installation.

## Solution
- The recommended solution is to use a Python module for running Python3.
- User recreated the virtual Python environment using the `python/3.6-anaconda` module, which resolved the issue.

## General Learnings
- Always use environment modules for running specific software versions to avoid dependency issues.
- System updates can affect software dependencies and cause unexpected errors.
- Recreating the virtual environment with the correct module can resolve library errors.

## Actions Taken
- HPC Admins advised the user to use Python modules for running Python3.
- User recreated the virtual Python environment with the `python/3.6-anaconda` module and confirmed that the issue was resolved.

## Follow-up
- No further action is required as the issue has been resolved.
- Users should be encouraged to use environment modules for their software needs.
---

### 2024020742003992_Python%20Programm%20zum%20Drug%20design.md
# Ticket 2024020742003992

 # HPC-Support Ticket Conversation Summary

## Subject: Python Programm zum Drug design

### Keywords:
- Python installation
- Conda environment
- Quota management
- HPC cluster
- Mamba
- TensorFlow
- CUDA/cuDNN/TensorRT

### General Learnings:
- Proper installation and execution of Python programs on HPC clusters.
- Handling Conda environment issues.
- Managing storage quotas on HPC systems.
- Importance of using batch jobs for compute-intensive tasks.

### Root Cause of the Problem:
- User attempted to install and run a Python program in their home directory without proper configuration.
- Encountered `NoWritablePkgsDirError` due to incorrect Conda environment setup.
- Exceeded storage quota in both home and vault directories.

### Solution:
- Load the appropriate Python/Conda module before installation.
- Configure Conda environment directories (`envsdir` and `pkgsdir`) as per FAQ instructions.
- Use batch jobs for compute-intensive tasks instead of running them on the frontend.
- Monitor and manage storage quotas to avoid data loss.

### Detailed Steps:
1. **Loading Python/Conda Module:**
   - On Alex, load the module using `module load python/3.9-anaconda`.

2. **Handling `NoWritablePkgsDirError`:**
   - Follow the FAQ instructions to configure Conda environment directories: [FAQ Link](https://hpc.fau.de/faqs/#how-to-fix-conda-error-nowritepkgsdirerror).

3. **Managing Storage Quotas:**
   - Check and manage storage quotas using tools like `shownicerquota.pl`.
   - Ensure that Conda environments are installed in appropriate directories like `$WORK` to avoid exceeding home directory quotas.

4. **Using Batch Jobs:**
   - Submit compute-intensive tasks as batch jobs to avoid overloading the frontend.

### Additional Notes:
- Avoid using multiple Conda installations (Anaconda, Mamba, Miniforge) simultaneously.
- Mamba can be used for faster environment setup, but ensure it is configured correctly.
- Storage quotas on vault are managed with warnings and restrictions based on soft and hard quotas.

### References:
- FAQ for Conda error: [FAQ Link](https://hpc.fau.de/faqs/#how-to-fix-conda-error-nowritepkgsdirerror)
- HPC documentation and support: [HPC FAU](https://hpc.fau.de/)

### Conclusion:
Proper configuration and management of Python environments and storage quotas are crucial for efficient use of HPC resources. Follow the provided guidelines and FAQs for troubleshooting common issues.
---

### 2023050442002744_python%20packages%20in%20interaktiven%20Sessions.md
# Ticket 2023050442002744

 # HPC Support Ticket: Python Packages in Interactive Sessions

## Keywords
- Python packages
- Interactive sessions
- `pip install --user`
- `scikit-learn`
- `salloc`
- `srun`
- `module load`
- TensorFlow
- CUDA
- cuDNN
- Proxy configuration
- Weights and Biases (wandb)
- Hyperparameter tuning

## Problem Description
The user is unable to use Python packages installed via `pip install --user` in interactive sessions. Specifically, the `scikit-learn` package is not found when running a Python script, despite being listed in `pip list`.

## Root Cause
The Python packages are likely installed in the wrong environment, making them invisible to the Python interpreter used in the interactive session.

## Solution
1. **Verify Package Installation**: Ensure that the package is correctly installed using `pip install --user <pkg-name>`.
2. **Check Python Environment**: Make sure that the Python environment used to install the packages is the same as the one used to run the script.
3. **Use Virtual Environments**: For scientific work, it is recommended to use virtual environments to manage dependencies and ensure version consistency.

## Additional Information
- **Proxy Configuration**: If needed, configure the proxy settings:
  ```bash
  export http_proxy=http://proxy:80
  export https_proxy=http://proxy:80
  ```
- **Weights and Biases (wandb)**: To use `wandb` on compute nodes, configure a proxy as per the FAQ: [FAU HPC FAQ](https://hpc.fau.de/faqs/#innerID-13439).

## Example Workflow
```bash
salloc.tinygpu --gres=gpu:1 --partition=rtx3080 --time=00:30:00
module load cuda/11.6.1
module load python/tensorflow2.11.0-py3.10
module load cudnn/8.8.0.121-11.8
export http_proxy=http://proxy:80
export https_proxy=http://proxy:80
pip install --user scikit-learn
python -c "import sklearn"
```

## Notes
- **Hyperparameter Tuning**: The user is interested in using `wandb` for hyperparameter tuning, which allows for efficient parameter sweeps and results uploading.
- **Frontend vs. Compute Node**: The user inquired about running code on the frontend while utilizing compute node hardware, but this is not feasible due to hardware limitations on the frontend.

## Conclusion
Ensure that Python packages are installed in the correct environment and consider using virtual environments for better dependency management. Configure proxies if necessary for external data transfer.
---

### 2024030742001349_Fwd%3A%20conda%20env%20for%20alex%20-%20openFF-Toolkit.md
# Ticket 2024030742001349

 ```markdown
# HPC Support Ticket Conversation Summary

## Issue
- User Eduard Neu encountered issues with running a Python script using a custom conda environment on the HPC cluster.
- The environment was created using a custom mamba installation and faced issues with module loading and environment activation.
- The primary error was `ModuleNotFoundError: No module named 'openff.toolkit'; 'openff' is not a package`.

## Root Cause
- The custom conda environment was not properly configured to work with the HPC cluster's Python modules.
- There were conflicting configurations in the user's `.condarc`, `.bashrc`, and `.profile` files.
- The environment was not set up to use non-default paths for packages and environments.

## Solution
- The user was advised to clean up the conflicting configurations and set up the environment to use non-default paths.
- The user was also advised to create a new conda environment using the provided YAML file or the following command:
  ```bash
  conda create -n openff_toolkit python=3.11.9 openff_toolkit=0.15.2 jupyterlab jupyter
  ```
- The user was informed about the possibility of running interactive jobs through Jupyter Notebooks on the cluster.

## Key Learnings
- Ensure that custom conda environments are properly configured to work with the HPC cluster's Python modules.
- Clean up conflicting configurations in `.condarc`, `.bashrc`, and `.profile` files.
- Use non-default paths for packages and environments if necessary.
- Consider running interactive jobs through Jupyter Notebooks for easier troubleshooting.

## Closing Note
- The ticket was closed as the attempts to build the environment failed, and there was no further inquiry from the user.
- If the user has additional questions, they can reopen the ticket for further assistance.
```
---

### 2019071942001392_modules%20system.md
# Ticket 2019071942001392

 ```markdown
# HPC Support Ticket: modules system

## Keywords
- modules system
- Python script
- Lagranto
- module load
- dyn_tools
- modules.sh
- Trajectory-Analyse

## Problem Description
The user is encountering issues while running a Python script (`lagrantoEcuador.py`) for trajectory analysis using Lagranto on the HPC system. The script fails with errors related to the modules system, specifically:
- Missing `/etc/profile.d/modules.sh` script.
- `module` command not found.
- `dyn_tools` module not available.

## Root Cause
- The script attempts to load modules within a non-login shell, where the `module` command is not available.
- The required `dyn_tools` module is not present on the system.

## Solution
- Load the necessary modules outside the script, ensuring they are available in the environment before running the script.
- If possible, avoid calling `module` commands within the script.
- If `dyn_tools` is essential, the user may need to create a custom module file and ensure it is properly linked.

## General Learnings
- Modules should be loaded in a login shell (`bash -l`) to ensure the `module` command is available.
- Custom module files can be created if necessary, but they need to be properly linked and configured.
- Ensure all required modules are available on the system before running scripts that depend on them.
```
---

### 2023102442001224_Using%20setup.py%20install.md
# Ticket 2023102442001224

 ```markdown
# HPC-Support Ticket: Using setup.py install

## Problem Description
- User is unable to find their `src` package when running a script on `tinygpu`.
- The package is installed via `setup.py` and `pip install -e .`.
- Conda environment is created from a `.yml` file and the package is listed as installed.

## Steps Taken by User
1. Created Conda environment from `.yml` file.
2. Installed the package using `pip install -e .`.
3. Verified the package is listed in `conda list`.
4. Submitted a job using `sbatch.tinygpu --gres=gpu:1 first_cnn_decoder.sh`.

## Error Message
- The `src` package is not found.

## Troubleshooting Steps by HPC Admins
1. Requested the user to add `conda run -n model_dev_aad_semeco python -m site` to the job script and run it again.
2. Requested the user to run `python -c "import src; print(src.__file__)"` on the frontend.
3. Suggested replacing `module load python/3.8-anaconda` with `module load python/3.10-anaconda` in the job script.

## Root Cause
- The Conda version in `python/3.8-anaconda` has a bug that causes issues with Python 3.10 and higher, preventing the package from being found correctly.

## Solution
- Replace `module load python/3.8-anaconda` with `module load python/3.10-anaconda` in the job script.

## Conclusion
- The job started successfully after changing the Python module version.
- The ticket was closed after the user confirmed the solution worked.
```
---

### 2019071042001827_HPC%20module%20python2.7-anaconda%20python.md
# Ticket 2019071042001827

 # HPC Support Ticket: Python 2.7 Anaconda Module Issue

## Keywords
- Python 2.7 Anaconda
- IPython
- ImportError
- traitlets.config.application
- Module update failure

## Problem Description
User encountered an `ImportError` when trying to run IPython after loading the Python 2.7 Anaconda module. The error message indicated a missing `traitlets.config.application` module.

## Root Cause
The issue was caused by a failed attempt to update the Anaconda/Python 2.7 module on the HPC system.

## Solution
HPC Admins reverted the module to the previous version before the update, which resolved the issue.

## Lessons Learned
- Updates to software modules can introduce compatibility issues.
- It is crucial to have a rollback plan when performing updates.
- Communication with users about ongoing maintenance and updates can help manage expectations.

## Actions Taken
1. HPC Admins attempted to update the Anaconda/Python 2.7 module.
2. The update failed, causing an `ImportError` for the user.
3. HPC Admins reverted the module to the previous version to resolve the issue.

## Follow-up
- Monitor future updates to ensure they do not introduce similar issues.
- Consider testing updates in a staging environment before deploying them to the production HPC system.
---

### 2024070542002059_h5py%20auf%20fritz.md
# Ticket 2024070542002059

 # HPC Support Ticket: h5py auf fritz

## Keywords
- h5py
- sys
- Python script
- HDF5 files
- Conda environment
- Module import

## Problem
The user wants to run a Python script using `h5py` and `sys` to delete datasets from HDF5 files. However, these modules are not available via import.

## Root Cause
The required Python modules (`h5py` and `sys`) are not installed in the user's current environment.

## Solution
The HPC Admin suggested creating a Conda environment and installing the `h5py` module within it.

### Steps
1. Create a Conda environment:
   ```bash
   conda create --name myenv
   ```
2. Activate the Conda environment:
   ```bash
   conda activate myenv
   ```
3. Install `h5py`:
   ```bash
   conda install h5py
   ```

## General Learning
- Users should create and use Conda environments to manage dependencies for their Python scripts.
- The `h5py` module can be easily installed using Conda.
- Proper environment management is crucial for running scripts with specific dependencies on HPC systems.

## References
- [Creating Conda Environments](https://doc.nhr.fau.de/environment/python-env/#creating-conda-environments)
---

### 2024051742001737_module%20command%20not%20found.md
# Ticket 2024051742001737

 # HPC Support Ticket: Module Command Not Found

## Keywords
- Module command not found
- VS Code non-login shells
- `module avail` error
- Cluster front-end vs dialog servers
- VS Code terminal settings

## Problem Description
The user encountered an issue where the `module avail` command was not found. This problem occurred because the user was using VS Code, which starts non-login shells by default.

## Root Cause
- The user was using VS Code, which starts non-login shells by default.
- The `module` command was not available because the necessary environment variables were not sourced.

## Solution
The HPC Admin provided three options to resolve the issue:
1. Use VS Code only for manipulating files but not for running commands.
2. Adapt the VS Code terminal settings to start login shells. This needs to be done only once.
3. Run `. /etc/profile` in the VS Code terminal every time a new terminal is opened.

## General Learnings
- VS Code starts non-login shells by default, which can cause issues with commands that rely on environment variables set in login shells.
- The `module` command is not available if the necessary environment variables are not sourced.
- Adapting the VS Code terminal settings to start login shells can resolve this issue.

## Additional Notes
- Both `hpc-support@fau.de` and `support-hpc@fau.de` are valid email addresses for support and go to the same mailbox.
- The user confirmed that adapting the VS Code terminal settings resolved the issue.

## References
- [VS Code Remote Release Issue](https://github.com/microsoft/vscode-remote-release/issues/1671#issuecomment-1601887808)
---

### 2023021342003581_installation%20von%20python%20package%20hat%20environment%20zerst%C3%83%C2%B6rt.md
# Ticket 2023021342003581

 # HPC Support Ticket: Installation von Python Package hat Environment zerstört

## Problem
- User deinstallierte und installierte ein Python-Package ohne ein extra Environment zu erstellen.
- Fehler traten bei der Neuinstallation auf, da einige Dateien in einem lokalen Pfad gespeichert wurden.
- Das Problem betrifft das Modul `python/tensorflow` auf dem Cluster Alex.
- Fehler zeigen sich auch mit einem `venv` und dem Modul `python/anaconda`.

## Root Cause
- Python-Pakete wurden lokal installiert und haben die Umgebung des Users beeinflusst.
- Möglicherweise wurde `pip install --user` verwendet, was zu lokalen Installationen führte.

## Lösung
- Lokale Dateien und Verzeichnisse (`.venv`, `~/.local`) wurden gelöscht.
- Überprüfung der TensorFlow-Version und mögliche Konflikte mit lokalen Installationen.
- Empfehlung, lokale Installationen zu deinstallieren und die zentrale Version zu nutzen.

## Schritte zur Lösung
1. **Löschen lokaler Dateien und Verzeichnisse:**
   - `.venv`
   - `~/.local`

2. **Überprüfung der TensorFlow-Version:**
   ```bash
   python -c "import tensorflow as tf; print(tf.__version__)"
   ```

3. **Deinstallation lokaler TensorFlow-Version:**
   ```bash
   pip uninstall tensorflow
   ```

4. **Nutzung der zentralen TensorFlow-Version:**
   ```bash
   module load python/tensorflow-2.7.0py3.9
   ```

5. **Überprüfung der GPU-Nutzung:**
   ```bash
   python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"
   ```

## Dokumentation und Tipps
- [Python und Jupyter auf HPC-Clustern](https://hpc.fau.de/systems-services/documentation-instructions/special-applications-and-tips-tricks/python-and-jupyter/)
- [TensorFlow und PyTorch auf HPC-Clustern](https://hpc.fau.de/systems-services/documentation-instructions/special-applications-and-tips-tricks/tensorflow-pytorch/)

## Schlussfolgerung
- Lokale Installationen von Python-Paketen können die Umgebung des Users beeinflussen.
- Es ist wichtig, lokale Installationen zu vermeiden oder zu deinstallieren, um Konflikte zu vermeiden.
- Nutzung der zentralen Module und Überprüfung der Installationen kann viele Probleme lösen.
---

### 2023012342003385_VScode%20bash%20erkennt%20module%20command%20nicht.md
# Ticket 2023012342003385

 # HPC Support Ticket: VScode Bash Module Command Issue

## Keywords
- VScode
- Bash
- Module Command
- .bashrc
- .bash_profile
- Interactive Login Shell
- Non-interactive Shell

## Problem Description
The user reported that the VScode internal bash could not find the `module` command when connecting to the HPC cluster (woody and woodycap) using the VScode server extension. Other commands like `singularity` worked fine. The issue did not occur when using `tmux` or SSH in the Windows PowerShell.

## Root Cause
The issue was due to the bash shell not being invoked with the `-l` (login) option, which is required to source the `.bashrc` file where the `module` command is likely configured. Additionally, the user did not have a `.bash_profile`, `.bash_login`, or `.profile` file, which are sourced by interactive login shells.

## Solution
1. **Configure VScode to use bash with the `-l` option:**
   - Add the following to the `settings.json` file in VScode:
     ```json
     "terminal.integrated.profiles.linux": {
       "bash": {
         "path": "bash",
         "args": ["-l"]
       }
     }
     ```
2. **Create a `.bash_profile` file to source the `.bashrc` file:**
   - Create a `.bash_profile` file in the user's home directory with the following content:
     ```bash
     if [ -f ~/.bashrc ]; then
       . ~/.bashrc
     fi
     ```

## General Lessons Learned
- The behavior of bash shell invocation can differ depending on whether it is an interactive login shell or a non-interactive shell.
- The `.bashrc` file is sourced by interactive non-login shells, while `.bash_profile`, `.bash_login`, and `.profile` are sourced by interactive login shells.
- VScode's internal terminal can be configured to invoke bash with the `-l` option to mimic an interactive login shell.
- If a user does not have a `.bash_profile`, `.bash_login`, or `.profile` file, creating a `.bash_profile` file that sources the `.bashrc` file can resolve issues with commands not being found.

## References
- [VScode Terminal Profiles Documentation](https://code.visualstudio.com/docs/terminal/profiles)
- [Bash Startup Files](https://www.gnu.org/software/bash/manual/html_node/Bash-Startup-Files.html)
---

### 2023042842003111_Python%20Code%20mit%20packages.md
# Ticket 2023042842003111

 # HPC Support Ticket: Python Package Installation Issue

## Keywords
- Python
- Deep Learning
- TinyGPU System
- Conda
- Package Installation
- Permissions
- EnvironmentNotWritableError

## Problem Description
- User is unable to install additional Python packages on the TinyGPU system.
- Attempting to install the `wandb` package using `conda install -c conda-forge wandb` results in an `EnvironmentNotWritableError`.
- The error message indicates that the user does not have write permissions to the target environment located at `/apps/python/3.10-anaconda`.

## Root Cause
- The user lacks the necessary write permissions to modify the existing Conda environment.

## Solution
- The HPC Admin provided documentation links for Python and TensorFlow/PyTorch usage on the system:
  - [Python and Jupyter Documentation](https://hpc.fau.de/systems-services/documentation-instructions/special-applications-and-tips-tricks/python-and-jupyter/)
  - [TensorFlow/PyTorch Documentation](https://hpc.fau.de/systems-services/documentation-instructions/special-applications-and-tips-tricks/tensorflow-pytorch/)
- Users should refer to these documents for guidance on installing and managing Python packages within the constraints of the system.

## General Learning
- Users may not have permissions to modify system-wide Conda environments.
- Documentation provided by the HPC Admin should be consulted for best practices and workarounds.
- It is important to understand the permissions and constraints of the HPC environment when attempting to install additional packages.
---

### 2024110742002083_Conda%20environment.md
# Ticket 2024110742002083

 # Conda Environment Creation Issue

## Keywords
- Conda environment
- NoWritablePkgsDirError
- Permissions issue
- `conda config --show-sources`
- `ls -ld`
- Cluster-specific issue

## Problem Description
The user encountered an error while trying to create a Conda environment. The error message indicated that there were no writable package directories configured.

## Root Cause
The user did not follow the first-time initialization steps for setting up Conda environments as outlined in the documentation.

## Solution
1. **Check Configuration**: Use `conda config --show-sources` to view the package directories (`pkgs_dirs`).
2. **Verify Permissions**: Use `ls -ld name_of_dir` to check the permissions of the directories.
3. **Follow Initialization Steps**: Refer to the [first-time initialization documentation](https://doc.nhr.fau.de/environment/python-env/#first-time-only-initialization) to properly set up the Conda environment.

## Lessons Learned
- Always refer to the specific documentation for first-time setup instructions.
- Ensure that the package directories have the correct permissions.
- Cluster-specific issues may arise, so it's important to specify which cluster is being used.

## Cluster Information
- The issue occurred on the Alex1 cluster.
- The HPC Admin confirmed that the issue did not occur on the Fritz cluster.

## Conclusion
The user was able to resolve the issue by following the initialization steps provided in the documentation. This highlights the importance of referring to cluster-specific setup instructions.
---

### 2021121342001094_Question%20about%20submitting%20batchjob.md
# Ticket 2021121342001094

 ```markdown
# HPC Support Ticket: Question about Submitting Batch Job

## Keywords
- Batch job submission
- Virtual environment
- Python modules
- Conda environment
- Module not found error

## Problem Description
The user built a virtual environment with Python 3.7 and all code worked fine on the front-end. However, when submitting a batch job with a shell script, the system failed to use the site-packages of Python like `torchvision` and `torch`, even though the Python module was loaded in the script. The user received an error indicating that the modules did not exist.

## Root Cause
The batch job script did not activate the Conda environment, leading to the module not found error.

## Solution
The HPC Admin suggested adding the following line to the batch job script to activate the Conda environment:
```sh
source activate <my-conda-env>
```

## Outcome
The user confirmed that the solution worked, and the issue was resolved.

## Lessons Learned
- Ensure that the Conda environment is activated in the batch job script to access the required Python modules.
- Provide detailed information about the job script and exact error messages when seeking support.
```
---

### 2022031542001766_installation%20required.md
# Ticket 2022031542001766

 ```markdown
# HPC Support Ticket: Installation Required

## Keywords
- Docker
- Singularity
- Python packages
- User space installation
- Security reasons

## Summary
A user requested the installation of Docker to pull some Python packages for their master thesis.

## Root Cause
- User needed to install Python packages but requested Docker, which is not available due to security reasons.

## Solution
- **Alternative to Docker**: Suggested using Singularity as an alternative.
- **Python Package Installation**: Provided a link to documentation on how to install additional Python packages in user space on top of existing Python modules.
- **Supervisor Involvement**: Advised the user to consult with their supervisor regarding the installation process.

## General Learnings
- Docker is not available on HPC centers due to security concerns.
- Singularity is a viable alternative for containerization needs.
- Users can install additional Python packages in their user space by following specific documentation.
- Involving supervisors can help in resolving technical issues related to academic projects.

## References
- [Python and Jupyter Documentation](https://hpc.fau.de/systems-services/systems-documentation-instructions/special-applications-and-tips-tricks/python-and-jupyter/)
```
---

### 2018061342002361_python%20libraries.md
# Ticket 2018061342002361

 # HPC Support Ticket: Python Libraries Import Error

## Keywords
- Python libraries
- ImportError
- matplotlib.pyplot
- numpy
- pandas
- keras
- Anaconda modules
- Virtual environments
- TensorFlow
- cuDNN

## Problem Description
The user is encountering `ImportError` when trying to import various Python libraries (e.g., matplotlib.pyplot, numpy, pandas, keras) while running a script on the Emmy cluster. The error persists across different Python versions.

## Root Cause
- The required Python libraries are not available in the loaded Python modules.
- Specifically, the `python/3.5-anaconda` module had an issue that was fixed.

## Solution
1. **Use Appropriate Anaconda Modules**:
   - The `python/2.7-anaconda` module should include `matplotlib.pyplot` and `pandas`.
   - The issue with the `python/3.5-anaconda` module has been resolved.

2. **Virtual Environments**:
   - For missing modules (e.g., keras), use Python's virtual environments to install the required packages.
   - Refer to the [Python virtual environments tutorial](https://docs.python.org/3/tutorial/venv.html) for guidance.

3. **TensorFlow and cuDNN**:
   - When using TensorFlow on GPU nodes, ensure to get a version that uses cuDNN.
   - Due to NVIDIA's license conditions, users must download personal copies of cuDNN using their personal developer account.

## Additional Notes
- The HPC Services team at Friedrich-Alexander-Universitaet Erlangen-Nuernberg (RRZE) provides support for these issues.
- For further assistance, contact `support-hpc@fau.de`.

## Learning Points
- Always check the availability of required libraries in the loaded Python modules.
- Use virtual environments to manage dependencies for specific projects.
- Be aware of licensing restrictions for certain software components like cuDNN.
---

### 2024072442001729_Environment%20problems%20-%20v101be12.md
# Ticket 2024072442001729

 # HPC Support Ticket: Environment Problems - v101be12

## Keywords
- Environment activation
- Conda
- Module load
- Python
- Import errors
- Interactive job

## Problem Description
The user encountered issues with activating a Conda environment after loading the Python module. The environment did not activate properly, leading to import errors. However, the environment activated successfully in an interactive job.

## Root Cause
The root cause of the problem was the conflict between the loaded Python module and the Conda environment activation.

## Solution
The issue was resolved by removing the `module load python` command. This allowed the Conda environment to activate correctly without conflicts.

## Lessons Learned
- Conflicts between loaded modules and Conda environments can cause activation issues.
- Removing conflicting module loads can resolve environment activation problems.
- Interactive jobs can be used to troubleshoot and verify environment activation issues.

## Ticket Conversation Summary
1. **User**: Reported issues with environment activation after loading Python module.
2. **HPC Admin**: Suggested loading a specific Python module (`python/3.9-anaconda`).
3. **User**: Reported that the suggested module load did not resolve the issue.
4. **User**: Discovered that removing the `module load python` command resolved the issue.
5. **HPC Admin**: Acknowledged the resolution.

## Conclusion
Conflicts between loaded modules and Conda environments can be a common issue. Removing conflicting module loads is a potential solution to resolve such problems.
---

### 2020031842001086_Schwer%20nachvollziehbare%20Fehlermeldungen.md
# Ticket 2020031842001086

 # HPC Support Ticket: Schwer nachvollziehbare Fehlermeldungen

## Keywords
- Python ImportError
- R nulldevice Fehler
- OpenSSL Update
- Knoteninstallation
- Job Freeze
- Walltime

## Problem Description
- User reports sporadic errors in Python and R scripts that cause jobs to hang and eventually get killed after reaching walltime.
- Errors include:
  1. Python ImportError related to OpenSSL version mismatch.
  2. R "nulldevice" error causing the script to freeze.

## Root Cause
- Inconsistent OpenSSL versions across compute nodes causing compatibility issues with Python libraries.
- Potential issues with R package dependencies or environment configuration.

## Solution
- **Python ImportError**:
  - HPC Admins updated the OpenSSL installation on all nodes to resolve the version mismatch issue.
  - Suggested a complete reinstallation of all nodes to ensure consistency.

- **R nulldevice Fehler**:
  - HPC Admins suggested monitoring the issue to see if the OpenSSL update resolves it.
  - Further investigation may be needed if the problem persists.

## General Learnings
- Ensure consistent software versions across all compute nodes to avoid compatibility issues.
- Regular updates and reinstallations can help maintain system stability.
- Monitoring and logging are essential for diagnosing sporadic errors.
- Collaboration between users and HPC Admins is crucial for identifying and resolving complex issues.

## Next Steps
- Continue monitoring the R nulldevice error to determine if the OpenSSL update has resolved the issue.
- Plan and execute a complete reinstallation of all compute nodes to ensure consistency.
- Document and communicate any further findings or solutions to the 2nd Level Support team and other relevant stakeholders.
---

### 2023052242003227_Loading%20python%20modules%20on%20fritz.md
# Ticket 2023052242003227

 # HPC Support Ticket: Loading Python Modules on Fritz

## Keywords
- Python
- Modules
- Virtual Environment
- numpy
- math
- datetime
- pip
- conda
- Anaconda
- venv

## Problem
User is unable to load Python modules (numpy, math, datetime) on the Fritz HPC system. The error message indicates that the module `numpy` is not found.

## Root Cause
The user attempted to load Python modules using incorrect commands (e.g., `module load numpy`), which are not the correct way to manage Python packages on the system.

## Solution
1. **Load Python Module**: Use the following command to load the Python module with basic libraries:
   ```bash
   module load python/3.9-anaconda
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv /path/to/new/virtual/environment
   ```

3. **Activate the Virtual Environment**:
   ```bash
   source /path/to/new/virtual/environment/bin/activate
   ```

4. **Install Required Packages**:
   ```bash
   pip install numpy
   ```

5. **Include Activation in Job Script**: Add the activation command to the job script to ensure the virtual environment is used during job execution.

## Additional Notes
- The virtual environment can be included in the `~/.bashrc` file to load automatically on login.
- Virtual environments are useful for managing multiple Python environments and dependencies.

## References
- [Python Virtual Environments Documentation](https://docs.python.org/3/library/venv.html)

## Support Team
- **HPC Admins**: Provided detailed instructions on loading modules and setting up virtual environments.
- **2nd Level Support Team**: Available for further assistance and troubleshooting.

## Conclusion
By following the steps to create and activate a virtual environment, the user can manage Python packages effectively and avoid module loading issues.
---

### 2022080842002331_Conda%20env.md
# Ticket 2022080842002331

 # HPC Support Ticket: Conda Environment Setup

## Keywords
- Conda environment
- $WORK directory
- Module availability
- Python
- Conda initialization

## Problem Description
- User unable to set up Conda environment in their $WORK directory.
- No modules available in the user's account.
- `conda` command not found.

## Root Cause
- Conda is not installed or not accessible in the user's environment.
- User's $WORK directory is not properly set up or recognized.

## Ticket Conversation
```
User: Dear Support Team,
How can I set up a Conda environment in my $WORK directory? There are no modules in my account.

iwi5086h@cshpc:~$ pwd
/home/hpc/iwi5/iwi5086h
iwi5086h@cshpc:~$ $WORK
bash: /home/woody/iwi5/iwi5086h: Is a directory
iwi5086h@cshpc:~$ module avail python
------------ /opt/modules/modulefiles/general ------------
iwi5086h@cshpc:~$
iwi5086h@cshpc:~$ conda init bash
bash: conda: command not found
iwi5086h@cshpc:~$
This guide does not help me
(https://hpc.fau.de/systems-services/documentation-instructions/special-applications-and-tips-tricks/python-and-jupyter/#conda)
How can I solve this problem?
BR
Volodymyr Marych
```

## Solution
1. **Install Conda**: Ensure Conda is installed in the user's environment. This may involve loading a module or installing Conda manually.
2. **Set Up $WORK Directory**: Verify that the $WORK directory is correctly set up and accessible.
3. **Initialize Conda**: Run `conda init bash` to initialize Conda for the current shell.

## Steps to Resolve
1. **Check Conda Installation**:
   ```bash
   module load conda
   ```
   If the module is not available, download and install Miniconda or Anaconda.

2. **Verify $WORK Directory**:
   ```bash
   echo $WORK
   ```
   Ensure the directory exists and is correctly set.

3. **Initialize Conda**:
   ```bash
   conda init bash
   source ~/.bashrc
   ```

## Additional Resources
- [Conda Documentation](https://docs.conda.io/projects/conda/en/latest/index.html)
- [HPC FAU Python and Jupyter Guide](https://hpc.fau.de/systems-services/documentation-instructions/special-applications-and-tips-tricks/python-and-jupyter/#conda)

## Notes
- Ensure the user has the necessary permissions to install software and modify environment variables.
- Provide detailed instructions for installing Conda if it is not available as a module.
---

### 2023102642003353_Problem%20with%20HPC%20server.md
# Ticket 2023102642003353

 # HPC Support Ticket Analysis

## Subject: Problem with HPC server

### Keywords:
- HPC
- PyCharm
- Python
- sudo commands
- libraries
- user manual
- beginner
- documentation
- introduction
- online session

### Root Cause of the Problem:
- User is a beginner in HPC.
- User wants to install PyCharm, update Python, and install libraries but lacks access.

### Solution Provided:
- HPC Admin provided links to relevant documentation:
  - [FAQs](https://hpc.fau.de/faqs/#ID-242)
  - [Python and Jupyter](https://hpc.fau.de/systems-services/documentation-instructions/special-applications-and-tips-tricks/python-and-jupyter/)
  - [TensorFlow and PyTorch](https://hpc.fau.de/systems-services/documentation-instructions/special-applications-and-tips-tricks/tensorflow-pytorch/)
- Invitation to an online introduction session:
  - Date: Wednesday, November 15, 2023, 4:00 p.m.
  - Location: [Zoom Link](https://fau.zoom.us/j/63416831557)
  - Slides: [HPC in a Nutshell](https://hpc.fau.de/files/2023/07/2023-07-12_HPC_in_a_Nutshell.pdf)

### General Learnings:
- Users should refer to the provided documentation for guidance on installing software and managing Python environments.
- Beginners are encouraged to attend introductory sessions to gain a better understanding of HPC usage.
- Access issues can often be resolved by following the instructions in the documentation or by attending training sessions.

### Next Steps for Support:
- Ensure the user has access to the provided documentation.
- Follow up with the user to confirm if the documentation and training session resolved their issues.
- Update the knowledge base with common beginner questions and solutions.
---

