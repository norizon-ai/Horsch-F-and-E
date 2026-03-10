# Topic 41: load_python_conda_environment_environments

Number of tickets: 8

## Tickets in this topic:

### 2024120942002998_Incredibly%20slow%20to%20import%20torch%20on%20alex%20--%20disk%20access%20issues%3F.md
# Ticket 2024120942002998

 # HPC Support Ticket: Slow Import of PyTorch on Alex Cluster

## Subject
Incredibly slow to import torch on alex -- disk access issues?

## User Issue
- User experiencing extremely slow import times for PyTorch in a conda environment.
- Import statement taking up to 5 minutes instead of a few seconds.
- Suspected issue with disk access to the $WORK filesystem.

## User Actions
- Followed instructions to set up a conda environment and installed PyTorch.
- Command used: `time python -v -c "import torch"`
- Output:
  ```
  real    5m26.670s
  user    0m9.765s
  sys     0m0.501s
  ```

## HPC Admin Response
- Confirmed high load on the atuin file system causing long loading times.
- Suggested moving the conda environment to $HPCVAULT to alleviate the issue.
- Mentioned that high load on file systems is not rare but usually quickly resolved.
- Recommended using workspaces on Alex for large amounts of data.

## User Follow-up
- Moved conda environment to $HPCVAULT, which resolved the issue temporarily.
- Reported that the problem persisted and worsened, with simple commands like `ls` taking over 10 seconds.
- Provided `strace` output showing slow `openat` and `getdents64` syscalls.

## HPC Admin Response
- Explained that the problem is caused by a few users overloading the file system.
- Stated that this is difficult to prevent and can happen on consecutive days.
- Reiterated that $WORK is generally a good place for conda environments.
- Suggested workspaces for large data sets.

## Root Cause
- High load on the atuin file system causing slow disk access.

## Solution
- Move conda environment to $HPCVAULT or another non-backed up filesystem.
- Consider using workspaces for large data sets.
- Wait for the file system load to be resolved by HPC admins.

## Additional Notes
- HPC admins are actively working to identify and contact users causing high load.
- The issue is not the normal state for the atuin file system.
---

### 2024071542000372_High%20read%20load%20on%20file%20server%20%5Bcapn106h%5D.md
# Ticket 2024071542000372

 # High Read Load on File Server

## Keywords
- High read load
- File server
- Python environments
- Data staging
- Shared filesystems

## Problem
- User's jobs on TinyGPU causing high read load (~30MB/s) on the file server.
- Constant read load can be harmful to shared filesystems if many users/jobs do the same.

## Root Cause
- User's jobs were reading data from `wecapstor3`.
- Python environments located in the home directory instead of `$WORK`.

## Solution
- Install Python environments in `$WORK` instead of the home directory.
  - Reference: [Python Environments Documentation](https://doc.nhr.fau.de/environment/python-env/)
- Implement data staging to reduce constant read load on the file server.
  - Reference: [Data Staging Documentation](https://doc.nhr.fau.de/data/datasets/)

## General Learnings
- High read loads on file servers can degrade performance for all users.
- Proper data management and staging can mitigate this issue.
- Python environments should be installed in designated work directories to optimize performance and storage usage.

## Actions Taken
- HPC Admins provided recommendations for improving job performance.
- User was advised to move Python environments to `$WORK` and implement data staging.

## Status
- Ticket closed after providing recommendations and guidance.
---

### 2023082842003498_Extreme%20long%20runtime%20on%20alex%20for%20just%20python%20imports%20-%20b112dc12.md
# Ticket 2023082842003498

 # HPC Support Ticket: Extreme Long Runtime for Python Imports

## Keywords
- HPC Cluster
- A100 GPUs
- Python Imports
- PyTorch
- Conda Environment
- NFS Server
- $WORK Directory
- Inodes

## Problem Description
- User experiences extremely long runtime (several minutes) for importing Python libraries (e.g., PyTorch) on the HPC cluster.
- User is using a local PyTorch installation within a Conda environment, with Conda packages saved in the $WORK directory.
- User is using PyTorch 2.1.0 and Python 3.9.

## Root Cause
- High load on the NFS server behind the $WORK directory.
- Importing PyTorch causes a lot of files to be enumerated and read, which can take longer depending on the load.
- The user's Conda environment directory contains a large number of inodes (194383), which can exacerbate the issue.

## Solution
- No immediate workaround provided.
- The issue is related to the load on the NFS server and the number of files being read during the import process.

## General Learnings
- Importing large Python libraries like PyTorch can be slow on HPC clusters due to the load on the NFS server.
- The number of inodes in the Conda environment directory can impact the import time.
- There may not always be a straightforward solution to such issues, as they can be dependent on the system load and infrastructure.

## Next Steps
- Monitor the NFS server load and optimize if possible.
- Consider alternative storage solutions for large Conda environments to reduce the impact on the NFS server.
- Keep users informed about potential delays and provide updates if a solution is found.
---

### 2023102442003697_python%20imports%20taking%20very%20long.md
# Ticket 2023102442003697

 # HPC Support Ticket: Python Imports Taking Very Long

## Keywords
- Python virtual environment
- Import statements
- File system performance
- Conda environment

## Problem Description
- User created a Python virtual environment.
- Import statements and initializing Python in the virtual environment are taking several minutes.
- The issue started recently and was not present before.
- Using the Python provided by the module anaconda works fine.

## Root Cause
- The issue is likely related to the file system being slow.

## Solution
- Inform the user that there is a problem with the file system (atuin) and that the issue is being investigated.
- Advise the user to be patient and try again later.
- If the problem persists, the user should contact support again.

## Lessons Learned
- Performance issues with Python environments can be caused by underlying file system problems.
- It is important to check the overall system health when diagnosing performance issues in user environments.
- Communicate ongoing investigations to users to manage expectations.

## Actions Taken
- HPC Admins informed the user about the file system issue and ongoing investigation.
- User was advised to try again later and report back if the problem persists.

## Follow-up
- Monitor the file system performance.
- Update the user once the issue is resolved.
- Document any further findings related to the file system performance for future reference.
---

### 2025012142001029_pip%20-v%20install%20flash-attn%3D%3D2.7.3%20--no-build-isolation%20takes%20forever.md
# Ticket 2025012142001029

 # HPC Support Ticket: Slow `pip` Installation of `flash-attn`

## Keywords
- pip
- flash-attn
- virtual environment (venv)
- build time
- conda
- CPU allocation

## Problem Description
- User activated a virtual environment and attempted to install `flash-attn==2.7.3` using `pip -v install flash-attn==2.7.3 --no-build-isolation`.
- The build and wheel process took an excessively long time (reportedly over a few hours).

## Root Cause
- The `flash-attn` package is known to have long build times.

## Solution
- **Use Conda**: Sometimes, Conda can be faster at resolving dependencies.
- **Increase CPU Allocation**: Allocating more CPUs per task can accelerate the build process.

## Additional Notes
- The user was advised to try using Conda for potentially faster dependency resolution.
- Increasing the number of CPUs per task was suggested as a way to speed up the build process.

## Conclusion
- For packages with known long build times, consider using Conda or increasing CPU allocation to improve installation speed.

---

This documentation can help support employees address similar issues with long build times for specific packages by suggesting alternative installation methods and resource allocation strategies.
---

### 2024020542002415_Extremely%20laggy%20conda%20environment%20-%20b168dc12.md
# Ticket 2024020542002415

 ```markdown
# HPC Support Ticket: Extremely Laggy Conda Environment

## Keywords
- Performance issues
- Conda environment
- Python imports
- Remote filesystem latency
- High load fileserver

## Issue Description
- User experiencing performance issues with a conda environment on the HPC cluster.
- Simple tasks like importing matplotlib and pip installs are unusually slow.
- Issue occurs when opening a new terminal or running Python code after a while.
- No sluggishness observed in running Python code itself, only in imports.
- Same environment works fine on the user's local machine.

## Root Cause
- Python environment installed on a fileserver (`/home/atuin`) under high load.

## Solution
- The HPC Admins are evaluating changes to the fileserver to fix the issue.
- Users are advised to be patient while the issue is being addressed.

## General Learnings
- High load on fileservers can cause performance issues with Python environments.
- Remote filesystem latency can affect the speed of Python imports and package installations.
- Evaluating and optimizing fileserver performance can help resolve such issues.
```
---

### 2024071942001702_Issue%20Regarding%20pip%20install%20autogluon.md
# Ticket 2024071942001702

 ```markdown
# Issue Regarding pip install autogluon

## Keywords
- pip install
- autogluon
- opencv-python
- virtual environment
- building wheels
- terminal freeze

## Problem Description
The user encountered an issue while trying to install `autogluon` in their virtual environment. The installation process got stuck at "Building wheels for collected packages: opencv-python" and the terminal froze.

## Support Interaction
- **User**: Reported the issue with the installation process freezing.
- **HPC Admin**: Clarified whether the process was stuck or just taking longer than expected. Mentioned that large packages can take several minutes to install.
- **User**: Confirmed that the terminal froze and eventually reported fixing the issue themselves.

## Root Cause
The root cause of the problem was not explicitly identified in the conversation, but it was related to the installation process of `opencv-python` during the `autogluon` installation.

## Solution
The user resolved the issue independently without specifying the exact steps taken.

## General Learnings
- Large packages can take a significant amount of time to install.
- Users should be patient and allow sufficient time for the installation process to complete.
- If the terminal freezes, it might indicate a more serious issue that requires troubleshooting.

## Next Steps
- Document common troubleshooting steps for long installation processes.
- Provide guidance on how to handle terminal freezes during package installations.
```
---

### 2025011542000274_Issue%20loading%20python%20%5Bb213da10%5D.md
# Ticket 2025011542000274

 ```markdown
# HPC Support Ticket: Issue Loading Python [b213da10]

## Keywords
- Conda environments
- Python script
- Long load times
- Storage server load
- High bandwidth usage
- Workspace usage

## Summary
A user experienced long load times and failure to start Python scripts in their Conda environments, resulting in lost GPU hours. The issue affected all environments, both frequently and seldom used.

## Root Cause
- High load on the storage server (Atuin) due to constant writing of logs and checkpoints by the user's jobs.
- Aggregated bandwidth of 250MB/s was observed.

## Solution
- **HPC Admin** suggested using a workspace for checkpoints to reduce the load on the storage server.
- Reference: [Workspaces Documentation](https://doc.nhr.fau.de/data/workspaces)

## Lessons Learned
- High load on storage servers can cause long load times and failure to start scripts.
- Writing large amounts of data to the storage server can contribute to high load.
- Using workspaces for checkpoints can help alleviate the load on the storage server.
- Users should be directed to use the appropriate support email for requests.
```
---

