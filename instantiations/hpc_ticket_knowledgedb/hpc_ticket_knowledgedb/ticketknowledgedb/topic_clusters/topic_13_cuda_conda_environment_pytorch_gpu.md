# Topic 13: cuda_conda_environment_pytorch_gpu

Number of tickets: 122

## Tickets in this topic:

### 2023022842002455_Regarding%20job%20failure.md
# Ticket 2023022842002455

 ```markdown
# HPC Support Ticket: Regarding Job Failure

## Keywords
- Deep Learning Model
- Segmentation Fault
- Interactive Shell
- Job Script
- GPU Cluster
- CUDA Module

## Problem Description
- User experiences segmentation fault (core dumped) when running a deep learning model in an interactive shell on various GPU nodes (RTX3080, A100, V100, RTX2080Ti).
- The model runs fine when submitted as a job script.

## Troubleshooting Steps
1. **HPC Admin**: Requested more details about the workflow and exact error messages.
2. **User**: Confirmed using the same code for both interactive and job script runs.
3. **HPC Admin**: Noted differences in output files and CUDA module loading between interactive and job script runs.

## Root Cause
- Difference in CUDA module loading: The job script loads `cuda/11.2.0`, which might not be loaded in the interactive shell.
- Potential issue with subprocess spawning: `tensorflow/core/platform/default/subprocess.cc:304] Start cannot spawn child process: No such file or directory`.

## Solution
- Ensure the same CUDA module is loaded in the interactive shell as in the job script.
- Use different output files for SLURM output to facilitate easier debugging.

## General Learning
- Consistent module loading is crucial for reproducibility between interactive and batch job environments.
- Proper error handling and logging can help diagnose issues more effectively.

```
---

### 2024120842000671_GPU%20support%20on%20HPC%20-%20b143dc39.md
# Ticket 2024120842000671

 # HPC Support Ticket: GPU Support on HPC

## Keywords
- GPU support
- CUDA
- PyTorch
- NVIDIA driver
- Compute node
- Conda environment
- HPC cluster

## Problem Description
- User created a new Conda environment for a master thesis project.
- Encountered an issue with GPU support on the HPC cluster.
- `torch.cuda.is_available()` returned `False`.
- CUDA module loaded (`cuda/11.8`), but `nvidia-smi` command not found.

## Root Cause
- The user was running the GPU check on the login node (`alex1.nhr.fau.de`), which does not have a GPU.

## Solution
- Run GPU-dependent tasks on a compute node.
- Use the interactive job feature to access a compute node with GPU support.

## Additional Comments
- Avoid using `/home/vault` for files that can be easily reproduced.
- Use the provided modules instead of relying on `/usr/local/cuda`.

## Relevant Documentation
- [Interactive Job Documentation](https://doc.nhr.fau.de/clusters/alex/#interactive-job)
- [PyTorch Documentation](https://doc.nhr.fau.de/apps/pytorch)

## Outcome
- The user was able to resolve the issue by following the provided guidance.

## Roles Involved
- **HPC Admins**: Provided guidance on running GPU tasks on compute nodes and additional comments on file system usage and module usage.
- **User**: Reported the issue and followed the provided guidance to resolve it.
---

### 2023062042003318_Cuda%20problem.md
# Ticket 2023062042003318

 # HPC Support Ticket: Cuda Problem

## Keywords
- Cuda
- Module Load
- Job Script
- Log File
- .bashrc

## Problem Description
The user encountered an issue where some files for CUDA could not be loaded. The log file indicated that an incorrect CUDA version was being used.

## Root Cause
- The CUDA module was updated to version 12 on the HPC system, but the user's job script was loading an older version (11.8.0).
- The job script was missing the `-l` flag in the shebang line, which prevented the module commands from working correctly.

## Solution
1. **Update CUDA Version in .bashrc**: Change `module load cuda` to `module load cuda/11.8.0` in the user's .bashrc file.
2. **Modify Job Script**: Add the `-l` flag to the shebang line in the job script (`#!/bin/bash -l`) to ensure that the module commands are recognized.
3. **Load CUDA Module in Job Script**: Instead of relying on the .bashrc file, load the required CUDA module directly in the job script using `module load cuda/11.8.0`.

## Lessons Learned
- Always specify the version number when loading modules to ensure compatibility.
- Use the `-l` flag in the shebang line of job scripts to enable module commands.
- Loading modules directly in the job script can help avoid issues related to environment variables and shell configurations.

## Ticket Status
The ticket was closed after the user confirmed that the issue was resolved.
---

### 2023103042002686_need%20CUDA%20on%20JupytherHub.md
# Ticket 2023103042002686

 # HPC Support Ticket: Enabling CUDA on JupyterHub

## Keywords
- CUDA
- GPU
- JupyterHub
- Huggingface
- BERT models
- OutOfMemoryError
- TinyGPU
- Alex cluster

## Problem
- User needs CUDA and GPU access for large models and data in JupyterHub.
- Initial attempts to run code resulted in using CPU instead of GPU.
- User encountered OutOfMemoryError when trying to use available GPU profile.

## Root Cause
- Default JupyterHub session does not have GPU access.
- Available GPU (Nvidia GTX 1080) has insufficient memory (11 GB) for user's task.

## Solution
- To enable CUDA and GPU, select the profile "1x GPU, 4 hours" from the drop-down menu in JupyterHub.
- For larger GPU memory needs, use TinyGPU or Alex cluster directly.
  - [TinyGPU Documentation](https://hpc.fau.de/systems-services/documentation-instructions/clusters/tinygpu-cluster/)
- Consider attending monthly introduction sessions for new users for further assistance.

## Additional Notes
- If further help is needed with SSH connection and job submission, consult with the user's supervisor or the support team.
- Monthly introduction sessions are held via Zoom (e.g., November 15, 2023, at 4:00 p.m.).

## Next Steps for User
- Try using TinyGPU or Alex cluster for larger GPU memory requirements.
- Attend the next introduction session if additional guidance is needed.
---

### 2022071642000105_Request%20to%20Install%20CUDA%20under%20the%20username%20iwi5092h.md
# Ticket 2022071642000105

 # HPC Support Ticket: CUDA Installation Request

## Keywords
- CUDA Installation
- GPU Systems
- User Support
- Supervisor/Colleague Assistance

## Problem
- **User Request:** Installation of CUDA for executing deep learning (DL) architecture.
- **Root Cause:** User unaware that CUDA is already installed on GPU systems.

## Solution
- **HPC Admin Response:** Informed the user that CUDA is already installed on the GPU systems.
- **Recommendation:** Advised the user to seek assistance from their supervisor or colleagues for beginner's problems.

## General Learnings
- **Pre-installed Software:** Ensure users are aware of pre-installed software on HPC systems.
- **Internal Support:** Encourage users to seek internal support from their supervisors or colleagues for basic issues.

## Next Steps
- **User Action:** User should verify the installation of CUDA and seek internal support for any further issues.
- **HPC Admin Action:** No further action required from HPC Admins.
---

### 2022011442001851_K20%20Emmy%20Cluster.md
# Ticket 2022011442001851

 # HPC Support Ticket: K20 Emmy Cluster Issue

## Keywords
- K20 GPUs
- CUDA
- NVIDIA Treiber
- Tesla K20m
- Treiberdowngrade
- CUDA 11.5
- CUDA 11.4
- Security Updates
- Legacy GPUs

## Problem Description
- **Root Cause:** The current NVIDIA drivers (495.29.05) do not support the Tesla K20m GPUs, causing CUDA-capable devices not to be detected.
- **Symptoms:** Running `deviceQuery` from CUDA samples returns `cudaGetDeviceCount returned 100 -> no CUDA-capable device is detected`.

## Troubleshooting Steps
- User verified the presence of K20 GPUs using `lspci | grep K20`.
- Tested multiple nodes with the same issue.

## Solution
- **Action Taken:** HPC Admins downgraded the NVIDIA drivers to the latest LTS version (470.82.01) that supports all GPUs in the cluster.
- **Result:** K20 GPUs are now usable again, but the Emmy GPU part is limited to CUDA version 11.4 and may not receive newer CUDA versions.
- **Commands Used:**
  ```bash
  yum remove cuda-cuobjdump-11-5-11.5.119-1.x86_64 ...
  rpm --nodeps -e cuda-drivers-495.29.05-1.x86_64 ...
  yum --setopt=obsoletes=0 install cuda-drivers-470.82.01-1.x86_64 ...
  ```

## General Learnings
- Older GPUs may not be supported by the latest NVIDIA drivers and CUDA toolkits.
- Downgrading drivers can temporarily resolve compatibility issues, but long-term solutions may require decommissioning older hardware.
- Maintaining separate images for different GPU types can ensure compatibility but increases maintenance overhead.

## Future Considerations
- Evaluate the feasibility of maintaining older GPUs considering the effort required for driver and CUDA toolkit management.
- Plan for hardware refresh to phase out legacy GPUs and simplify software stack management.
---

### 2024061142004118_TransformerEngine%20%28TE%29%20Build%20Fehler%2C%20cudnn.h%20not%20found.md
# Ticket 2024061142004118

 # HPC-Support Ticket: TransformerEngine (TE) Build Fehler, cudnn.h not found

## Subject
TransformerEngine (TE) Build Fehler, cudnn.h not found

## User Issue
The user is attempting to build Nvidia's Transformer Engine from source but encounters an error where `cudnn.h` is not found during the compilation process.

## Environment
- **Modules Loaded:**
  - `cuda/12.4.1`
  - `cudnn/9.1.0.70-12.x`
  - `cmake/3.23.1`
  - `git/2.35.2`
  - `gcc/12.1.0`
  - `ninja/1.11.1`
- **Python Environment:**
  - Activated virtual environment: `source $WORK/venvs/megatron/bin/activate`
  - Installed packages: `setuptools==69.5.1`, `nltk`, `sentencepiece`, `einops`, `mpmath`, `packaging`, `numpy`, `ninja`, `wheel`
  - PyTorch installation: `pip3 install --pre torch --index-url https://download.pytorch.org/whl/nightly/cu124`

## Error Log
The error log indicates that `cudnn.h` is not found during the compilation process.

## HPC Admin Response
- The issue is reproduced by the HPC Admin.
- The problem is identified as `cmake` not including the `CUDNN_ROOT/include` path during the build process.
- The solution provided is to set the `CXXFLAGS` environment variable to include the `cudnn` include path:
  ```bash
  export CXXFLAGS=-isystem\ $CUDNN_ROOT/include
  ```
- After setting the `CXXFLAGS`, the user should run the installation command:
  ```bash
  pip install git+https://github.com/NVIDIA/TransformerEngine.git@stable
  ```
- However, this solution leads to another error related to a known issue in the TransformerEngine repository: [Issue #752](https://github.com/NVIDIA/TransformerEngine/issues/752).

## Additional Notes
- The HPC Admin suggests using the `main` branch of the TransformerEngine repository as a workaround for the known issue.
- The HPC Admin also notes that manual changes to Spack-generated module files should be made on a copy, not the original, to avoid being overwritten by `spack module refresh`.

## Keywords
- TransformerEngine
- cudnn.h
- cmake
- CXXFLAGS
- build error
- include path
- Spack module

## General Learnings
- Ensure that all necessary include paths are correctly set when building software that depends on external libraries.
- Use environment variables like `CXXFLAGS` to include additional paths during the compilation process.
- Be aware of known issues in the software repositories and consider using different branches or versions as workarounds.
- When making manual changes to Spack-generated module files, always work on a copy to prevent losing changes during a refresh.
---

### 2024120342003695_cluster%20change%20problem.md
# Ticket 2024120342003695

 ```markdown
# HPC Support Ticket: Cluster Change Problem

## Keywords
- CUDA
- PyTorch
- GPU
- JupyterHub
- TINYGPU
- TINYFAT
- SLURM
- Environment Configuration

## Problem Description
The user encountered an issue with CUDA and PyTorch environment configuration on the HPC platform. Specifically, PyTorch was unable to detect the GPU (`torch.cuda.is_available()` returned `False`). The user intended to use the TINYGPU cluster but was using TINYFAT instead.

## Root Cause
The user was using the 'Local on JupyterHub (systemd) - 2 cores, 4 GB, unlimited' profile, which provided a Jupyter session on `tf050` instead of the intended TINYGPU cluster.

## Solution
The user restarted JupyterHub, which resolved the issue.

## Logs and Diagnostics
The HPC Admin provided log entries showing that the user's jobs were submitted to the correct cluster (TINYGPU) but the interactive JupyterHub session was running on a different host (`tf050`).

## Lessons Learned
- Ensure the correct profile is selected when starting a JupyterHub session.
- Restarting JupyterHub can resolve configuration issues.
- Verify the host and cluster being used for interactive sessions.

## References
- HPC Admin: Thomas Gruber
- User: Qianxin Wang
```
---

### 2024021042000836_NeMo%20Megatron%20installation.md
# Ticket 2024021042000836

 # HPC Support Ticket: NeMo Megatron Installation

## Keywords
- NeMo Megatron
- NVIDIA
- TransformerEngine
- CUDA
- cuDNN
- Conda
- Python
- Installation Error

## Problem Description
The user encountered issues while trying to install NeMo Megatron from NVIDIA. Specifically, the command `pip install --upgrade git+https://github.com/NVIDIA/TransformerEngine.git@stable` failed despite having CUDA 11.8 and cuDNN installed. The error message indicated that no CUDA runtime was found.

## Root Cause
1. Initial assumption was that CUDA 12.1 or newer was required, but this was incorrect.
2. The actual issue was a TypeError in the `version.py` file of the TransformerEngine package.

## Solution
1. The HPC Admin suggested modifying the `setup.py` file of the TransformerEngine package.
2. Specifically, changing `version=te_version()` to `version=str(te_version())` in the `setup.py` file resolved the issue.

## Lessons Learned
- Always verify the required CUDA version for specific packages.
- TypeErrors in Python packages can sometimes be resolved by ensuring that version strings are properly formatted.
- Modifying the `setup.py` file can be a viable solution for installation issues related to versioning.

## References
- [NVIDIA NeMo GitHub](https://github.com/NVIDIA/NeMo)
- [NVIDIA TransformerEngine GitHub](https://github.com/NVIDIA/TransformerEngine)

## Closure
The ticket was closed after the user confirmed that the suggested modification resolved the installation issue.
---

### 2024112542003931_%22Segmentation%20fault%20%28core%20dumped%29%22%20in%20the%20job%20-%20b155ee10.md
# Ticket 2024112542003931

 # HPC Support Ticket: Segmentation Fault in GPU Jobs

## Problem Description
- **Error Message**: `srun: error: a0537: task 0: Segmentation fault (core dumped)`
- **Context**: Occurs when running GPU jobs using JAX to compute large matrix inverses.
- **Environment**:
  - Node: `alex1`
  - Job ID: `2202153`
  - Account: `b155ee10`

## Root Cause
- **Potential Issue**: Conflict between manually installed CUDA/cuDNN and loaded CUDA module.

## Steps Taken
1. **Initial Report**:
   - User reported segmentation fault when running GPU jobs with JAX.
   - Provided example code and job script.

2. **Admin Response**:
   - Suggested following JAX installation instructions with the most recent CUDA and cuDNN modules loaded.
   - Requested details on how the user built their environment.

3. **User Follow-Up**:
   - Reported login issues due to a file server crash.
   - Described their environment setup:
     ```bash
     module load python/3.12-conda
     python -m venv new_env
     source new_env/bin/activate
     pip install jax[cuda12]
     ```
   - Provided job script:
     ```bash
     #!/bin/bash -l
     #SBATCH --nodes=1
     #SBATCH --ntasks-per-node=1
     #SBATCH --time=00:10:00
     #SBATCH --partition=a100
     #SBATCH --gpus-per-node=a100:1
     #SBATCH --constraint=a100_80
     unset SLURM_EXPORT_ENV
     module load python/3.12-conda
     module load cuda/12.6.1
     module list
     source ~/new_env/bin/activate
     srun --cpu-bind=socket python script.py
     ```

4. **Admin Follow-Up**:
   - Confirmed that loading the CUDA module caused the error.
   - Suggested not loading the CUDA module in the job script.

## Solution
- **Recommendation**: Do not load the CUDA module in the job script when using `pip install jax[cuda12]`.

## Keywords
- Segmentation fault
- GPU jobs
- JAX
- CUDA
- cuDNN
- Environment setup
- Job script

## General Learnings
- Conflicts between manually installed libraries and loaded modules can cause segmentation faults.
- Ensure compatibility between installed packages and loaded modules.
- File server crashes can cause login issues.
- Detailed environment setup information is crucial for troubleshooting.
---

### 2024101642004619_nvcc%20Not%20Available%20in%20Current%20Environment%20%28CUDA%20Available%20in%20PyTorch%29.md
# Ticket 2024101642004619

 # HPC Support Ticket: nvcc Not Available in Current Environment (CUDA Available in PyTorch)

## Keywords
- nvcc
- CUDA
- PyTorch
- Front-end node
- Compute node
- Job submission
- Interactive allocation
- sbatch
- salloc
- Module loading

## Problem
- User encountered an issue where `nvcc` (NVIDIA CUDA Compiler) is not found on the front-end node (alex1).
- CUDA was detected when tested using PyTorch, indicating that CUDA is accessible but `nvcc` is missing from the environment or not in the PATH.

## Root Cause
- The user was attempting to run tasks on a front-end node instead of a compute node.
- The necessary modules for `nvcc` were not loaded in the environment.

## Solution
- **Job Submission**: Submit a job via a job script using `sbatch` and load the appropriate modules in the job script.
  - Reference: [Python Single GPU](https://doc.nhr.fau.de/clusters/alex/#python-single-gpu)
- **Interactive Allocation**: Allocate a node interactively using `salloc` and load the necessary modules once the shell is available.
  - Reference: [Interactive Job](https://doc.nhr.fau.de/clusters/alex/#interactive-job)

## General Learnings
- Front-end nodes are not intended for running compute tasks; use compute nodes instead.
- Load the necessary modules for `nvcc` and other tools in the job script or interactive session.
- Use `sbatch` for job submission and `salloc` for interactive node allocation.

## References
- [Python Single GPU](https://doc.nhr.fau.de/clusters/alex/#python-single-gpu)
- [Interactive Job](https://doc.nhr.fau.de/clusters/alex/#interactive-job)
---

### 2025011242000565_Requesting%20support%20with%20software%20installation.md
# Ticket 2025011242000565

 # HPC Support Ticket: Requesting Support with Software Installation

## Keywords
- PyTorch installation
- Conda
- CUDA
- GPU availability
- Interactive job
- Frontend vs. compute node

## Problem Description
- User is having trouble installing PyTorch via Conda on an HPC system.
- Installation fails when using Conda, and GPU is not automatically available when using pip.
- User has followed documentation but needs further guidance.

## Root Cause
- User is attempting to build the environment on the frontend instead of within an interactive job on a compute node.

## Steps Taken by User
1. Navigated to the work directory.
2. Loaded Python and CUDA modules.
3. Activated Conda environment.
4. Attempted to install PyTorch with CUDA support using Conda.

## Solution
- **HPC Admin** advised the user to follow the documentation and build the environment within an interactive job on a compute node instead of the frontend.
- Clarified the difference between frontend and compute nodes.

## General Learnings
- Always perform software installations and environment setups within an interactive job on a compute node.
- Frontend nodes are not suitable for heavy computations or installations that require significant resources.
- Ensure proper module loading and environment activation before installing software.

## Relevant Documentation Links
- [Why is my application not using the GPU?](https://doc.nhr.fau.de/faq/#why-is-my-application-not-using-the-gpu)
- [PyTorch Documentation](https://doc.nhr.fau.de/apps/pytorch)

## Next Steps
- User should attempt the installation within an interactive job and report back if issues persist.
- **HPC Admin** may need to provide further guidance on starting an interactive job if the user is unfamiliar with the process.
---

### 2020070942000999_CUDA%20Problem%20TinyGPU.md
# Ticket 2020070942000999

 # HPC Support Ticket: CUDA Problem TinyGPU

## Keywords
- CUDA
- LAMMPS
- NVIDIA 1080
- TinyGPU
- Module Loading
- Compilation Error

## Problem Description
The user reported issues with running LAMMPS on NVIDIA 1080 cards due to CUDA 11 being set as the default. The user was unable to compile LAMMPS with CUDA 11 because the CUDA 11 module could not be loaded, even in an interactive shell. Additionally, the CUDA 10.2 module was not properly linked, causing computations to halt.

## Root Cause
- CUDA 11 module was not properly configured for loading on specific machines.
- CUDA 10.2 module was not correctly linked, leading to compilation and runtime issues.

## Solution
- HPC Admin reinstalled CUDA 10.2 and fixed the loading issue for CUDA 11.
- Users were advised to request an interactive job on a TinyGPU node to use and compile with the required CUDA version.

## Lessons Learned
- Ensure that CUDA modules are correctly configured and linked for all supported versions.
- Users should be aware of the specific machines that support CUDA and request interactive jobs accordingly.
- Regularly check module installations and configurations to prevent disruptions in user workflows.

## Actions Taken
- Reinstalled CUDA 10.2 module.
- Fixed the loading issue for CUDA 11 module.
- Provided guidance to users on requesting interactive jobs on TinyGPU nodes.

## Follow-Up
- Monitor CUDA module usage and ensure proper configuration.
- Update documentation to reflect the correct procedure for using CUDA on specific machines.

---

This documentation can be used to resolve similar issues in the future by ensuring that CUDA modules are properly configured and that users are aware of the specific requirements for using CUDA on supported machines.
---

### 2023112342004918_No%20CUDA%20detected%20on%20tinyx.md
# Ticket 2023112342004918

 # HPC Support Ticket: No CUDA Detected on TinyGPU

## Keywords
- CUDA
- GPU
- TinyGPU Cluster
- Python
- Torch
- NVIDIA Driver
- Frontend
- Node Allocation

## Problem
- User attempted to run a Python script using CUDA on the frontend of the cluster.
- Error message: "Found no NVIDIA driver on your system."

## Root Cause
- The frontend of the cluster does not have GPUs.
- User did not allocate a GPU node from the TinyGPU cluster.

## Solution
- Allocate a GPU node from the TinyGPU cluster before running the script.
- Refer to the documentation: [TinyGPU Cluster Documentation](https://hpc.fau.de/systems-services/documentation-instructions/clusters/tinygpu-cluster/)
- Consult the advisor for further assistance.

## General Learning
- Ensure that GPU-intensive tasks are run on nodes with GPUs.
- Always allocate the appropriate resources before running jobs on the HPC cluster.
- Refer users to relevant documentation and advisors for additional support.
---

### 2024071742003428_nvidia-profiler%20fails%20sometimes.md
# Ticket 2024071742003428

 # HPC Support Ticket: nvidia-profiler Fails Sometimes

## Keywords
- nvidia-profiler
- Nsight Systems
- Importation failed
- Event order error
- CUDA version
- nsys

## Problem Description
The user encounters intermittent failures when using the nvidia-profiler, specifically with the error message indicating an importation failure due to an invalid event order. The error occurs even though the code executes correctly.

## Root Cause
The issue is likely related to a known problem with older versions of Nsight Systems, as reported in the NVIDIA developer forums. The error message indicates a problem with the event order in the analysis.

## Solution
1. **Update Nsight Systems**: The user was advised to test with a newer version of Nsight Systems.
2. **Install New CUDA Module**: The HPC Admins installed a newer CUDA module (`cuda/12.5.1`) which includes the latest version of Nsight Systems.
3. **Test with New Version**: The user confirmed that the issue seems to be resolved with the updated version.

## Steps Taken
1. **Initial Diagnosis**: The user provided the error message and details about the issue.
2. **Research**: The HPC Admin identified a potential known issue with older versions of Nsight Systems.
3. **Update Recommendation**: The user was advised to update to a newer version of Nsight Systems.
4. **Installation**: The HPC Admins installed a newer CUDA module with the latest version of Nsight Systems.
5. **User Testing**: The user tested the new version and confirmed that the issue was resolved.

## Conclusion
Updating to the latest version of Nsight Systems resolved the intermittent importation failure issue. Users experiencing similar problems should ensure they are using the most recent version of the tool.

## References
- [Nsight Systems Importation Error](https://forums.developer.nvidia.com/t/nsys-importation-error/283231)
---

### 2022042942000015_Singularity%20Fakeroot.md
# Ticket 2022042942000015

 # HPC Support Ticket: Singularity Fakeroot

## Summary
- **User Request**: Support for Singularity fakeroot on an Alex node.
- **Issues Encountered**:
  - Incorrect reservation account.
  - Missing mapping entry in `/etc/subuid`.
  - AlphaPose compatibility issues with PyTorch 1.11.
- **Solutions Provided**:
  - Corrected reservation account.
  - Adjusted `/etc/subuid` format.
  - Provided a patch for AlphaPose and setup.py modifications.

## Keywords
- Singularity
- Fakeroot
- AlphaPose
- PyTorch
- CUDA
- GPU
- Reservation
- Subuid
- Patch

## Lessons Learned
- **Reservation Issues**: Ensure the correct account is used for reservations.
- **Subuid Configuration**: Proper format and entries in `/etc/subuid` are crucial for fakeroot to function.
- **Software Compatibility**: AlphaPose has specific requirements for PyTorch versions and CUDA support. Patches and setup.py modifications may be necessary.
- **Collaboration**: Involving the 2nd Level Support team for specialized issues can be beneficial.

## Detailed Steps and Solutions

### Initial Request
- **User**: Requested support for Singularity fakeroot on an Alex node.

### Reservation and Configuration
- **HPC Admin**: Prepared node `a0603` with fakeroot support.
- **Issue**: User encountered access denied errors due to incorrect reservation account.
- **Solution**: Corrected the reservation account and provided the correct node type (A100).

### Subuid Configuration
- **Issue**: Missing mapping entry in `/etc/subuid` for the user.
- **Solution**: Adjusted the format of `/etc/subuid` to include the necessary mapping entries.

### AlphaPose Compatibility
- **Issue**: AlphaPose did not run with PyTorch 1.11 due to removed THC functionalities.
- **Solution**: Provided a patch for AlphaPose and modified `setup.py` to increase the scipy version.

### Additional Support
- **HPC Admin**: Offered to involve Dominik Ernst from the 2nd Level Support team for further assistance with AlphaPose and Nvidia-related issues.

### Performance Analysis
- **HPC Admin**: Noted that AlphaPose runs but performance, especially the CPU part, has room for improvement. Provided a link to an older analysis for reference.

### Follow-up Requests
- **User**: Requested additional fakeroot reservations.
- **HPC Admin**: Informed the user about node availability and existing reservations.

## Conclusion
- The support ticket involved multiple steps to resolve reservation, configuration, and software compatibility issues. Collaboration with the 2nd Level Support team was suggested for specialized assistance. The final solution included patches and setup modifications for AlphaPose to run with PyTorch 1.11.

## References
- [AlphaPose Issues](https://github.com/MVIG-SJTU/AlphaPose/issues/435)
- [PyTorch 1.11 Release](https://www.exxactcorp.com/blog/Deep-Learning/pytorch-1-11-0-now-available)

This documentation can serve as a reference for future support tickets involving Singularity fakeroot and AlphaPose compatibility issues.
---

### 2024012942000615_GPUs%20allocated%20but%20not%20utilized%20-%20k106eb10.md
# Ticket 2024012942000615

 # HPC Support Ticket: GPUs Allocated but Not Utilized

## Problem Description
- User submitted multiple jobs that allocated GPUs but did not utilize them.
- Monitoring system showed no GPU utilization for the jobs.
- User's TensorFlow installation in a conda environment did not use the GPU.

## Root Cause
- TensorFlow installation did not have GPU support enabled.
- Incorrect combination of library versions and modules.

## Steps to Reproduce
1. Allocate GPU resources:
   ```bash
   salloc --gres=gpu:a40:1 --partition=a40 --time=04:00:00
   ```
2. Create and activate a conda environment:
   ```bash
   conda create -n test python=3.9
   conda activate test
   ```
3. Load CUDA and cuDNN modules:
   ```bash
   module load cuda
   module load cudnn
   ```
4. Install TensorFlow with GPU support:
   ```bash
   python3 -m pip install tensorflow[and-cuda]
   ```
5. Verify GPU utilization:
   ```bash
   python3 -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"
   ```

## Error Messages
- Unable to register cuDNN, cuFFT, and cuBLAS factories.
- TF-TRT Warning: Could not find TensorRT.

## Solution
1. Use specific versions of libraries and modules:
   ```bash
   module load python/3.9-anaconda
   module load tensorrt/8.5.3.1-cuda11.8-cudnn8.6
   module load cuda/11.8.0
   module load cudnn/8.6.0.163-11.8
   ```
2. Install TensorFlow and protobuf:
   ```bash
   conda create -n test python=3.9
   conda activate test
   python3 -m pip install tensorflow==2.8
   pip install protobuf==3.20.*
   ```
3. Compile and run the code in an interactive session with GPU resources allocated.

## Verification
- Use `nvidia-smi` to check GPU utilization.
- Ensure that the GPU is being used by the TensorFlow installation.

## Additional Notes
- TensorRT may not be necessary for all applications.
- Ensure that the Python environment is created and configured on a compute node with GPU support.

## References
- [FAU FAQ: Why is my PyTorch/TensorFlow using CPU only?](https://hpc.fau.de/faqs/#why-is-my-pytorch-tensorflow-using-cpu-only)
- Previous ticket #2023110742002281 for TF-TRT Warning solution.
---

### 2024101642003923_Unsupported%20CUDA%20Error.md
# Ticket 2024101642003923

 ```markdown
# Unsupported CUDA Error

## Keywords
- CUDA Error
- JupyterHub
- GPU Compatibility
- NVIDIA Volta
- Compute Capability
- GTX 1080 Ti

## Problem Description
The user encountered an `UnsupportedCUDAError` when trying to load the `cudf` package in JupyterHub. The error message indicated that a GPU with NVIDIA Volta™ (Compute Capability 7.0) or newer architecture is required, but the detected GPU was an NVIDIA GeForce GTX 1080 Ti with Compute Capability 6.1.

## Root Cause
The `cudf` package requires a GPU with a higher compute capability than what is available on the current JupyterHub setup (GTX 1080 Ti with Compute Capability 6.1).

## Solution
JupyterHub currently only has access to GTX 1080/GTX 1080 Ti GPUs, which do not meet the required compute capability for the `cudf` package. No immediate solution was provided, indicating that the user may need to use a different environment or package that supports the available GPUs.

## General Learning
- Ensure that the GPU requirements of the software packages are compatible with the available hardware.
- Understand the compute capability requirements of the packages being used.
- Communicate hardware limitations to users and suggest alternative solutions if necessary.
```
---

### 2024102142002291_enquiry%20for%20CUDA%20compilation%20error.md
# Ticket 2024102142002291

 # HPC Support Ticket Conversation: CUDA Compilation Error

## Keywords
- CUDA version compatibility
- Module loading
- Job script configuration
- Debugging CUDA version

## Summary
The user encountered issues with CUDA version compatibility and module loading in their HPC job script. The user required CUDA 12.1 but had CUDA 12.6 available, and faced difficulties in loading the correct CUDA version.

## Root Cause
- The user's job script was not correctly loading the desired CUDA version.
- The default CUDA version (12.6) was being loaded despite the user's attempts to load CUDA 11.8.0.

## Solution
- Ensure the job script correctly purges any loaded modules and loads the desired CUDA version.
- Verify the loaded CUDA version by checking environment variables and using `nvcc --version`.

## Conversation Details

### User's Initial Request
- User required specific versions of mmdet, mmcv, CUDA, and PyTorch.
- User's HPC environment had CUDA 12.6, but the project required CUDA 12.1.

### HPC Admin's Response
- Suggested trying to install the framework with the available CUDA version.
- Provided a list of available CUDA versions and suggested using TinyGPU without JupyterHub.

### User's Follow-up
- User provided a job script example but faced issues with the default CUDA version being loaded.

### HPC Admin's Further Assistance
- Confirmed the correct procedure for loading CUDA modules.
- Verified that loading a CUDA module should set the appropriate environment variables.
- Unable to reproduce the issue, suggesting the user's script might have other issues.

## Job Script Example
```bash
#!/bin/bash -l
#SBATCH --gres=gpu:1
#SBATCH --time=24:00:00
#SBATCH --output=/home/hpc/iwi5/iwi5234h/FAU_Project/global_logs/log_train.out
#SBATCH --mail-type=BEGIN
#SBATCH --mail-type=END
#SBATCH --mail-user=debadrita.mukherjee@fau.de

module purge
module load python
module load cuda/11.8.0

python /home/vault/iwi5/iwi5234h/Dataset/mmdetection/tools/train.py configs/conditional_detr/conditional-detr_r50_8xb2-50e_coco.py
```

## Debugging Steps
- Ensure `module purge` is correctly clearing any loaded modules.
- Verify the loaded CUDA version using `env | grep -nie cuda` and `nvcc --version`.

## Conclusion
The user should ensure their job script correctly loads the desired CUDA version and verify the loaded version using environment variables and `nvcc --version`. If issues persist, further debugging of the job script and environment setup may be necessary.
---

### 2024071642000101_CUDA%20Driver%20Version%20Issue%20with%20PyTorch.md
# Ticket 2024071642000101

 # CUDA Driver Version Issue with PyTorch

## Keywords
- CUDA Driver Version
- PyTorch
- RuntimeError
- Module Load
- CUDA 12.4
- CUDA 11.8

## Problem Description
The user encountered a `RuntimeError` due to an insufficient CUDA driver version for the CUDA runtime version. PyTorch was not compatible with CUDA 12.4, and the user did not have access to change the CUDA version on the HPC system.

## Root Cause
- Incompatibility between PyTorch and CUDA 12.4.
- Default CUDA version on the HPC system was 12.4.1.

## Solution
- Use the module system to load a different CUDA version.
- Load CUDA 11.8.0, which is a more stable version for PyTorch.

## Steps to Resolve
1. Check available CUDA modules:
   ```bash
   $ module avail cuda
   ```
2. Load the desired CUDA module:
   ```bash
   $ module load cuda/11.8.0
   ```

## Additional Notes
- The default CUDA module is loaded if no specific version is specified.
- Reinstalling PyTorch may not be necessary after loading the correct CUDA module.

## References
- [PyTorch CUDA Compatibility](https://pytorch.org/)
---

### 2023080342003534_Unable%20to%20install%20Pytorch%20with%20cuda%2011.8%20on%20TinyGPU.md
# Ticket 2023080342003534

 # HPC Support Ticket: Unable to Install PyTorch with CUDA 11.8 on TinyGPU

## Keywords
- PyTorch
- CUDA 11.8
- TinyGPU
- Network Error
- Proxy Configuration
- Conda Environment

## Problem Description
- User unable to install PyTorch with CUDA 11.8 on TinyGPU cluster.
- Error message: `ERROR: No matching distribution found for torch`.
- Network connection error: `Failed to establish a new connection: [Errno 101] Network is unreachable`.
- Unable to create a new Conda environment from an interactive session.

## Root Cause
- TinyGPU cluster has no direct access to the internet.

## Solution
- Set a proxy as described in the FAQ: [Proxy Configuration](https://hpc.fau.de/faqs/#innerID-13439).

## Additional Information
- User's approach:
  1. Start interactive session with `salloc`.
  2. Load CUDA version with `module load cuda/11.8.0`.
  3. Load cuDNN with `module load cudnn` (loads cudnn/8.8.0.121-11.8).
  4. Install PyTorch with the command: `pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118`.

## Lessons Learned
- Ensure proper proxy configuration for clusters without direct internet access.
- Check network connectivity when encountering installation errors related to package retrieval.
- Conda environments should be created on the frontend node if network issues are encountered in interactive sessions.

## References
- [Proxy Configuration FAQ](https://hpc.fau.de/faqs/#innerID-13439)
---

### 2024022642002635_Request%20for%20Specific%20CUDA%20Version%20on%20HPC%20Server%20for%20Thesis%20Model%20Training.md
# Ticket 2024022642002635

 ```markdown
# HPC-Support Ticket: Request for Specific CUDA Version on HPC Server for Thesis Model Training

## Keywords
- CUDA versions
- HPC server
- Thesis model training
- JPEGAI model
- PyTorch binary
- Compatibility issues
- Spack installation

## Summary
A user requested specific CUDA versions (10.2+ and 11.3+) for their thesis model training, which were not available on the HPC server. The user's project relies on the JPEGAI model, which requires these specific CUDA versions due to compatibility issues with the PyTorch binary.

## Root Cause
- The user's thesis model training requires CUDA versions 10.2+ and 11.3+.
- The available CUDA versions on the HPC server (11.1.0, 11.2.2, 11.7.0, 12.3.0, 11.2.0, 11.6.1, 11.8.0) do not meet the specific requirements.
- Compatibility issues with the JPEGAI model and PyTorch binary prevent the use of other available CUDA versions.

## Solution
- The HPC Admins suggested using available CUDA versions that fulfill the 11.3+ requirement (11.6.1, 11.8.0, 12.3.0).
- The user explained the compatibility issues and the need for specific versions.
- The HPC Admins provided a workaround by suggesting the user install CUDA 10.2 themselves using Spack:
  ```bash
  $ module load user-spack
  $ spack install cuda@10.2
  ```
- The user was advised to test the installation after the maintenance period.

## General Learnings
- Maintaining multiple CUDA versions on an HPC server is challenging and requires significant work.
- Users can install specific software versions using Spack if the required versions are not available on the server.
- Compatibility issues with specific software tools (e.g., JPEGAI model and PyTorch binary) may necessitate the use of particular CUDA versions.
- Effective communication between users and HPC Admins can lead to workarounds and solutions for software compatibility issues.
```
---

### 2025031142002025_Running%20Jupyter%20Notebook%20with%20GPU%20Issue.md
# Ticket 2025031142002025

 # Running Jupyter Notebook with GPU Issue

## Keywords
- Jupyter Notebook
- VS Code
- GPU allocation
- PyTorch
- CUDA
- Conda environment

## Problem Description
The user is unable to utilize the GPU in Jupyter Notebook running on VS Code despite allocating GPU resources and loading the necessary modules. The number of GPUs is reported as 0 in the Jupyter Notebook.

## Root Cause
The PyTorch version in the conda environment does not have CUDA enabled.

## Solution
Install a PyTorch version that has CUDA enabled using the following command:
```bash
pip3 install torch torchvision torchaudio --index-url "https://download.pytorch.org/whl/cu126"
```

## Steps to Reproduce
1. Connect to the HPC system.
2. Allocate GPU resources using `salloc`.
3. Load the necessary modules (`python/3.10-anaconda` and `cuda/12.6.1`).
4. Activate the PyTorch environment using `conda activate pytorch`.
5. Open Jupyter Notebook in VS Code and select the appropriate kernel.
6. Check the number of GPUs in the Jupyter Notebook.

## What Can Be Learned
- Ensure that the PyTorch version in the conda environment has CUDA enabled.
- Use the correct installation command to install a CUDA-enabled PyTorch version.
- Verify that the GPU resources are properly allocated and the necessary modules are loaded.

## Additional Notes
- This issue highlights the importance of using compatible software versions and ensuring that all necessary components are properly configured for GPU utilization.
- The solution provided can be applied to similar issues where GPU resources are not being recognized in Jupyter Notebook.
---

### 2023121442001071_Torch%20not%20compiled%20with%20CUDA%20enabled.md
# Ticket 2023121442001071

 # HPC-Support Ticket: Torch not compiled with CUDA enabled

## Issue
- User encounters an error: `AssertionError: Torch not compiled with CUDA enabled`.
- Commands `print(torch.version.cuda)` and `print(torch.cuda.is_available())` return `None` and `False` respectively.
- User installed PyTorch with `conda install pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia` and separately installed `cudatoolkit 11.8`.

## Root Cause
- User's environment is broken due to mixing packages from different channels and versions.
- PyTorch and TensorFlow require different CUDA versions.
- User's `.bashrc` configuration might be causing issues with the Python binary path.

## Solution
1. **Start with a new environment**:
   - Load the Python module before activating the conda environment.
   - Install PyTorch and other dependencies in the new environment.

2. **Correct order of commands**:
   ```bash
   module add python
   conda create -n test -y python=3.11
   conda activate test
   conda install pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia
   ```

3. **Check Python binary**:
   - Ensure the correct Python binary is used by checking `which python` after activating the environment.

4. **Modify `.bashrc`**:
   - Comment out the conda initialization part in `.bashrc`.
   - Always load the Python module before using conda.

## Additional Notes
- There is no difference between `module add` and `module load`; they are aliases for each other.
- Mixing packages from different channels and versions can lead to compatibility issues.
- Ensure that the Python interpreter used is the one from the conda environment.

## Example Commands
```bash
module add python
conda create -n test -y python=3.11
conda activate test
conda install pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia
python3 -c 'import torch; print(torch.cuda.is_available()); print([torch.cuda.get_device_properties(i) for i in range(torch.cuda.device_count())])'
```

## Conclusion
- The user's environment is broken and needs to be recreated.
- Ensure compatibility between PyTorch and TensorFlow versions with the same CUDA version.
- Properly configure `.bashrc` to avoid conflicts with the Python binary path.
---

### 2016102742001161_Some%20questions%20regarding%20library%20positions%20in%20TinyGPU%20with%20pascal.md
# Ticket 2016102742001161

 # HPC Support Ticket Conversation Summary

## Subject
Some questions regarding library positions in TinyGPU with Pascal

## Keywords
- VASP 5.4.1 GPU version
- Pascal architecture
- CUDA-8
- CUDA_DRIVER directory
- nvidia-cuda-mps-control
- NVLink availability
- GPU memory limit

## Problem
- User modified VASP 5.4.1 GPU version for Pascal architecture and CUDA-8.
- User cannot find CUDA_DRIVER directory under `/apps/`.
- User inquires about the policy for running `nvidia-cuda-mps-control`.
- User asks about NVLink availability in the next-gen cluster.

## Solution
- **CUDA_DRIVER directory**: The driver is installed locally on the GPU nodes in `/usr/lib/nvidia-370`. It is not available on the login nodes. Use an interactive job if necessary to compile code.
- **nvidia-cuda-mps-control**: MPS is currently not configured. The HPC Admins will check it once they have some time.
- **NVLink availability**: There are no current plans to get new/further GPU systems.

## General Learnings
- The CUDA driver is only available on GPU nodes, not on login nodes.
- MPS (Multi-Process Service) is not currently configured on the cluster.
- There are no immediate plans for new GPU systems with NVLink.
- Users should use interactive jobs for compiling code that requires GPU drivers.

## Root Cause
- User was looking for the CUDA driver in the wrong directory.
- User needed clarification on the availability and configuration of MPS and NVLink.

## Additional Notes
- The user's modifications to VASP for Pascal architecture and CUDA-8 were successful on their personal computer.
- The user is looking for ways to bypass the GPU-bound memory limit.
---

### 2024092642002301_Installation%20von%20Jax%20auf%20Alex.md
# Ticket 2024092642002301

 # HPC Support Ticket Conversation: Installation von Jax auf Alex

## Keywords
- Jax installation
- GPU support
- cuDNN version mismatch
- Slurm plugin error
- Python environment setup

## Summary
A user encountered issues while setting up Jax with GPU support on the HPC system. The main problems were related to cuDNN version mismatch and Slurm plugin errors.

## Root Cause of Problems
1. **cuDNN Version Mismatch**: The installed version of cuDNN was not compatible with the version required by Jax.
2. **Slurm Plugin Error**: The error occurred due to a known issue with Slurm's auth_munge plugin.

## Solutions
1. **cuDNN Version Mismatch**:
   - The user was advised to specify a newer version of cuDNN. Available versions were provided.
   - Alternatively, the user could install the exact version of cuDNN via Conda and set the appropriate path.

2. **Slurm Plugin Error**:
   - The user found a known issue with Slurm and applied a workaround by executing the following code before importing the library:
     ```python
     import os, sys
     sys.setdlopenflags(os.RTLD_NOW | os.RTLD_GLOBAL)
     ```

## General Learnings
- Ensure compatibility between software versions, especially for GPU-accelerated libraries.
- Check for known issues and apply workarounds when encountering plugin errors.
- Use Conda environments to manage dependencies and ensure compatibility.

## Closure
The ticket was closed as the user resolved the issues independently.
---

### 2024081942001701_Regarding%20package%20installation%20issue.md
# Ticket 2024081942001701

 ```markdown
# HPC Support Ticket: Package Installation Issue

## Subject
Regarding package installation issue

## User Issue
- User unable to install `flash-attn>=2.1.0` on HPC.
- Error messages include "nvcc was not found" and "CUDA_HOME env var is not set."
- User tried installing via `conda install flash-attn` but faced issues.

## HPC Admin Responses
- HPC Admin successfully installed `flash-attn` using `conda install flash-attn` in a conda environment.
- Suggested loading CUDA module and ensuring `CUDA_HOME` is set.
- Advised to perform installation on a compute node using an interactive job.
- Provided Zoom meeting details for further assistance.

## Root Cause
- Missing CUDA module load and incorrect environment variable settings.
- Attempting installation on a frontend node without GPU.

## Solution
- Load the appropriate CUDA module: `module load cuda/12.5.1`.
- Ensure `CUDA_HOME` is set correctly.
- Perform installation on a compute node with GPU access.
- Use interactive job for testing and debugging.

## Additional Notes
- User provided job script for review.
- HPC Admin suggested using `module av -t |grep -i gcc` to find available GCC modules.
- User joined Zoom meeting for further assistance.

## Keywords
- flash-attn installation
- CUDA module
- environment variables
- interactive job
- conda environment
```
---

### 2023070342000155_Verwendung%20von%20Tensorboard.md
# Ticket 2023070342000155

 ```markdown
# HPC-Support Ticket: Verwendung von Tensorboard

## Problem
- User versucht, Modeltrainingsergebnisse mit Tensorboard anzuzeigen.
- Fehlermeldung: "Too many open files".
- Tensorboard-Anzeige funktioniert nicht, obwohl verschiedene Ports ausprobiert wurden.

## Vorgehen des Users
1. SSH-Verbindung zu `tinyx.nhr.fau.de`.
2. Module laden: `cudnn/8.6.0.163-11.8`, `cuda/11.6.1`, `python/tensorflow2.11.0-py3.10`.
3. Conda-Umgebung aktivieren: `conda activate sklearn_env`.
4. Tensorboard starten: `tensorboard --logdir=/Variante1/Versuch4_CWT_CNN/callbacks_am_13.Apr_um_01h_04m/tensorboard --port=6030`.
5. Neues CMD-Fenster öffnen und SSH-Tunnel einrichten: `ssh -g -L 6030:localhost:6030 -f -N iwfa017h@tinyx.nhr.fau.de -J iwfa017h@cshpc.rrze.fau.de`.

## Fehlerbehebung durch HPC Admins
- Hinweis, dass das zweite SSH-Kommando auf dem Client ausgeführt werden muss.
- Hinweis auf offene SSH-Verbindungen (SSH Leichen) auf `tinyx`.
- Vorschlag, andere Ports auszuprobieren.
- Hinweis, dass das Terminal offen bleiben muss, damit der SSH-Tunnel bestehen bleibt.

## Root Cause
- Tensorboard lief auf `tg065`, nicht auf `tinyx`.
- SSH-Tunnel zu `tinyx` konnte nichts finden.

## Lösung
- Tensorboard auf dem richtigen Server (`tinyx`) starten.
- SSH-Tunnel korrekt einrichten und sicherstellen, dass keine offenen SSH-Verbindungen stören.

## Schlussfolgerung
- Überprüfen, auf welchem Server Tensorboard läuft.
- SSH-Tunnel korrekt einrichten und offene SSH-Verbindungen schließen.
```
---

### 2023092042002751_Assistance%20Needed%20with%20GPU%20Job%20Execution%20Issue.md
# Ticket 2023092042002751

 # HPC Support Ticket: Assistance Needed with GPU Job Execution Issue

## Keywords
- GPU Job Execution
- PyTorch
- Conda Environment
- Slurm Output File
- HTTPS Request

## Summary
The user encountered an issue where their job script was not utilizing the GPU despite being configured to do so. The HPC Admin provided troubleshooting steps to resolve the issue.

## Root Cause
- Initial PyTorch selftest failed, indicating a problem with the conda environment.
- After resolving the selftest issue, the job script still did not utilize the GPU.

## Troubleshooting Steps
1. **PyTorch Selftest**:
   - Command: `python -c 'import torch; print(torch.rand(2,3).cuda())'`
   - If the selftest fails, rebuild the conda environment following the instructions provided in the documentation.

2. **Review Slurm Output File**:
   - The user was asked to provide the slurm output file for further analysis.

3. **HTTPS Request Issue**:
   - The code was unable to perform an HTTPS request due to an expired certificate.
   - Refer to the FAQ for fixing HTTP/HTTPS timeout issues.

## Solution
- Rebuild the conda environment to resolve the PyTorch selftest issue.
- Review the slurm output file to identify any errors or misconfigurations.
- Address the HTTPS request issue by following the FAQ instructions.

## Documentation Links
- [TensorFlow and PyTorch Documentation](https://hpc.fau.de/systems-services/documentation-instructions/special-applications-and-tips-tricks/tensorflow-pytorch/)
- [FAQ: Why does my program give a HTTP/HTTPS timeout?](https://hpc.fau.de/faqs/#why-does-my-program-give-a-http-https-timeout)

## Conclusion
The user was able to resolve the PyTorch selftest issue but still faced problems with GPU utilization. Further analysis of the slurm output file and addressing the HTTPS request issue were recommended to fully resolve the problem.
---

### 2024042942000977_nvcc.md
# Ticket 2024042942000977

 ```markdown
# HPC-Support Ticket Conversation Summary

## Subject: nvcc

### User Issue:
- User encountered an error while trying to install `hoomd-blue` with GPU support on `TinyX`.
- Error message: `Failed to find nvcc. Compiler requires the CUDA toolkit. Please set the CUDAToolkit_ROOT variable.`

### Root Cause:
- The user did not load the `cuda` module, which provides the `nvcc` compiler.

### Solution:
- Load the `cuda` module using `module load cuda`.
- If a specific version is needed, use `module avail cuda` to list available versions.

### Additional Questions and Solutions:
1. **Compiling `hoomd-blue` on a GPU Node:**
   - The user needs to recompile `hoomd-blue` on a GPU node.
   - Use `salloc --time=02:00:00 --gres=gpu:a40:1` or `salloc --time=02:00:00 --gres=gpu:a100:1` to start an interactive job.

2. **Submitting a Job with GPU:**
   - The user's SLURM script had an invalid account/partition combination.
   - Ensure the correct account and partition are specified.
   - Example SLURM script:
     ```bash
     #!/bin/bash -l
     #SBATCH --gres=gpu:a100:1
     #SBATCH --partition=a100
     #SBATCH --time=00:20:00
     #SBATCH --export=NONE

     unset SLURM_EXPORT_ENV

     module load python
     module load nvcc

     source ./pyEnv/bin/activate

     python3 testGPU.py 300 0.7 1.58 10000 ./ 0.02 0.2
     ```

### Keywords:
- `nvcc`
- `cuda`
- `hoomd-blue`
- `GPU`
- `SLURM`
- `module load`
- `interactive job`
- `account/partition combination`

### General Learnings:
- Always ensure the necessary modules are loaded before compiling software.
- Recompile software on the appropriate node (e.g., GPU node for GPU-enabled software).
- Verify account and partition settings when submitting jobs.
```
---

### 2024092042003374_cuda%20version%20auf%20gracehop.md
# Ticket 2024092042003374

 ```markdown
# HPC-Support Ticket: CUDA Version Update on Gracehop1

## Keywords
- CUDA version
- Gracehop1
- Installation
- Delay
- Testing

## Summary
A user requested the installation of the latest CUDA version on the Gracehop1 system. The request was initially delayed due to the admin's vacation but was eventually fulfilled. The user confirmed that the installation was successful.

## Root Cause
- User requested the latest CUDA version for their work on Gracehop1.

## Solution
- The HPC Admin installed CUDA version 12.6.1-gcc12.3.0-gyneavz on Gracehop1.
- The user tested the installation and confirmed it worked.

## Lessons Learned
- Requests for software updates may be delayed due to admin availability.
- Clear communication about delays helps manage user expectations.
- Testing after installation ensures the update is successful.
```
---

### 2023050242002364_Jupyter%20GPU%20availability.md
# Ticket 2023050242002364

 # HPC Support Ticket: Jupyter GPU Availability

## Keywords
- Jupyter Notebook
- GPU availability
- Conda environment
- JupyterHub
- Slurm job
- TinyGPU node
- Python packages
- ImportError

## Problem Summary
The user is unable to access GPU resources in Jupyter Notebooks despite having created and configured a Conda environment with the necessary packages. The user encounters issues with GPU availability and package imports.

## Root Cause
1. **GPU Availability**: The user's Jupyter server is running locally, where no GPUs are available.
2. **Package Import Error**: There is a conflict with the `jinja2` Python package causing an `ImportError`.

## Steps Taken by the User
1. Created a Conda environment (`torch_mledecoders`) and installed necessary packages.
2. Verified the installation using `conda list`.
3. Made the Conda environment available for Jupyter Notebooks using `python -m ipykernel install --user --name=torch_mledecoders`.
4. Accessed the RRZE JupyterHub but found no GPU available.
5. Attempted to start a Jupyter server from the Tinyx frontend but encountered package import errors.

## Solution Provided by HPC Admins
1. **GPU Availability**:
   - Instructed the user to request a job on the TinyGPU node via JupyterHub.
   - Provided steps to stop the current server and select the GPU option from the drop-down menu.

2. **Package Import Error**:
   - Identified a conflict with the `jinja2` package.
   - Advised the user to remove the conflicting Python package.

## Additional Information
- If no GPU is available, a timeout should be displayed.
- The user cannot view the log files directly.
- The user should stop the current server and select the GPU option from the drop-down menu to start a new server with GPU access.

## Documentation References
- [JupyterHub Documentation](https://hpc.fau.de/systems-services/documentation-instructions/clusters/jupyterhub/)
- [Python and Jupyter Documentation](https://hpc.fau.de/systems-services/documentation-instructions/special-applications-and-tips-tricks/python-and-jupyter/)

## Next Steps
- The user should follow the provided instructions to request a GPU job and resolve the package conflict.
- If issues persist, the user should contact HPC support for further assistance.
---

### 2023030142000951_No%20GPU%20found.md
# Ticket 2023030142000951

 ```markdown
# HPC-Support Ticket: No GPU found

## Issue Description
User reported that GROMACS jobs on A40 GPUs at Alex were terminated immediately with the warning: "Compatible GPUs must have been found." The log file indicated that the CUDA runtime could not be identified: "CUDA runtime: N/A". The issue occurred randomly and affected multiple versions (2021.6 and 2023) and different tpr files. Restarting the job several times sometimes allowed the simulation to run.

## Troubleshooting Steps
1. **Initial Investigation**:
   - User provided log and slurm output files.
   - HPC Admin observed "Graphics SM Warning" and "Graphics SM Global Exception" on 26 A40 nodes.
   - Correctable memory errors were noted on specific nodes.

2. **Reproduction Attempt**:
   - HPC Admin attempted to reproduce the issue but was unable to do so.
   - CUDA runtime was correctly detected as "CUDA runtime: 11.50".
   - HPC Admin suggested checking the user environment and meeting via Zoom for interactive investigation.

3. **Zoom Meeting**:
   - User and HPC Admin scheduled a Zoom meeting to investigate the issue interactively.
   - User provided a minimal working example and a script for an MPS server run.

4. **Workaround**:
   - HPC Admin suggested setting environment variables and starting the MPS daemon:
     ```bash
     export CUDA_MPS_PIPE_DIRECTORY=$TMPDIR/nvidia-mps.$SLURM_JOB_ID
     export CUDA_MPS_LOG_DIRECTORY=$TMPDIR/nvidia-log.$SLURM_JOB_ID
     nvidia-cuda-mps-control -d
     ```
   - This ensured each job and MPS daemon had its own directory, preventing conflicts between jobs on the same node.

5. **Verification**:
   - User confirmed that both suggested solutions worked.

## Conclusion
The issue was resolved by setting the necessary environment variables and starting the MPS daemon correctly. This ensured that each job had its own directory, preventing conflicts and allowing the jobs to run successfully.
```
---

### 2021051142002645_module%20load%20cuda%20geht%20nicht.md
# Ticket 2021051142002645

 # HPC Support Ticket: CUDA Module Load Issue

## Keywords
- CUDA
- Module Load
- Accel Queue
- Interactive Node
- Specific Machines
- Version Specification
- Error Resolution

## Problem Description
- User reported that `module load cuda` was not functioning.
- Error message: "Attention: CUDA is only supported on specific machines!"
- Issue occurred on an interactive node in the Accel queue.

## Root Cause
- The user did not specify a version when loading the CUDA module.
- There was an error in the `cuda/9.2` module on the HPC system.

## Solution
- Specifying a version when loading the CUDA module resolved the issue for the user.
- HPC Admin identified and fixed an error in the `cuda/9.2` module, which should now function correctly.

## Lessons Learned
- Always specify a version when loading modules to avoid compatibility issues.
- Ensure that modules are correctly configured and free of errors to prevent user issues.
- Communicate effectively with users to understand and resolve their problems promptly.

## Actions Taken
- HPC Admin fixed the error in the `cuda/9.2` module.
- User confirmed that specifying a version resolved the initial issue.

## Follow-Up
- Monitor the CUDA module for any further issues.
- Ensure that module documentation is clear about specifying versions.
---

### 2024031342003317_CUDA_HOME%20is%20not%20set.md
# Ticket 2024031342003317

 ```markdown
# HPC-Support Ticket: CUDA_HOME is not set

## Keywords
- CUDA_HOME
- mmcv
- pip
- Python
- CUDA
- cuDNN
- Environment Variables
- Module Loading
- Interactive Job
- Compilation Time
- Precompiled Wheels
- Singularity Container

## Problem
- User encountered an `OSError: CUDA_HOME environment variable is not set` while installing the `mmcv` Python package via pip.
- Initial attempt to install `mmcv` failed due to missing CUDA environment setup.

## Root Cause
- The `CUDA_HOME` environment variable was not set, which is required for the installation of `mmcv`.

## Solution
1. **Load CUDA and cuDNN Modules**:
   - The user needed to load the appropriate CUDA and cuDNN modules before attempting the installation.
   - Example: `module load cuda/12.3.0 cudnn/8.9.6.50-12.x`

2. **Long Compilation Time**:
   - The installation process for `mmcv` was taking a long time due to compilation.
   - This is a known issue with `mmcv` and can take up to 30 minutes.

3. **Precompiled Wheels**:
   - To speed up the process, the user could select a combination of versions where precompiled wheels are available.

4. **Submitting a Regular Job**:
   - To avoid the 2-hour wall time limit of an interactive job, the user could write a script with all the build steps and submit it as a regular job.

## Additional Tips
- Creating a Singularity container might not speed up the build process if `mmcv` must be compiled from source code.
- The user was advised to check the GitHub issue tracker for `mmcv` for more information on long compilation times.

## Conclusion
- The user successfully resolved the `CUDA_HOME` error by loading the appropriate modules.
- The long compilation time for `mmcv` is a known issue and can be mitigated by using precompiled wheels or submitting the build process as a regular job.
```
---

### 2022021142001113_one%20question.md
# Ticket 2022021142001113

 # HPC Support Ticket: One Question

## Subject
- User unable to find torch module after connecting to GPU node.

## Keywords
- GPU
- Python
- Torch
- Conda Environment
- Module Loading

## Problem Description
- User connected to GPU node using `salloc.tinygpu --gres=gpu:1 --time=01:00:00`.
- Error: No torch module found, despite it being available previously.
- User created a conda virtual environment with torch and other libraries, but it disappeared after connecting to the GPU node.

## Root Cause
- Different Python versions and environments on login node (woody3) and GPU nodes.
- Conda environment not loaded after job started.

## Solution
- Load the Python module and conda environment after the job starts.
- Use Python 3.8, the preinstalled version on tinygpu nodes.
- Set up a proxy for external data transmission if required.

## Documentation Links
- [Environment Documentation](https://hpc.fau.de/systems-services/systems-documentation-instructions/environment/)
- [TensorFlow and PyTorch Documentation](https://hpc.fau.de/systems-services/systems-documentation-instructions/special-applications-and-tips-tricks/tensorflow-pytorch/)
- [Python and Jupyter Documentation](https://hpc.fau.de/systems-services/systems-documentation-instructions/special-applications-and-tips-tricks/python-and-jupyter/)

## Additional Notes
- Ensure to check Python version using `which python` and `python --version`.
- Follow the documentation for setting up a working torch package.
- For external data transmission, ensure proper proxy settings are configured.

## Support Team Involved
- HPC Admins
- 2nd Level Support Team
---

### 2022052542002742_GPU-Frage.md
# Ticket 2022052542002742

 ```markdown
# HPC Support Ticket: GPU Compatibility Issue

## Keywords
- GPU Compatibility
- Singularity Container
- AlphaPose
- A40
- A100
- SM_XX Version
- PyTorch
- Deformable_im2col Error

## Problem Description
- User built a Singularity container for AlphaPose on an A40 node.
- The container works on A40 but fails on A100 with the error: `error in deformable_im2col: no kernel image is available for execution on the device`.
- Similar issue observed with DCPose.

## Root Cause
- Compatibility issue between SM_XX versions.
- Binaries built for sm_86 do not work on sm_80.
- Divergence in feature sets between HPC and consumer GPUs.

## Solution
- Ensure that the binaries and models are compatible with the SM_XX version of the target GPU.
- For A100 (sm_80), use binaries and models built for sm_80.

## Additional Notes
- Unrelated error message: `/usr/bin/tclsh: No such file or directory`.
- PyTorch version might be built for sm_86, causing compatibility issues with sm_80.

## Conclusion
- Always verify the compatibility of binaries and models with the target GPU's SM_XX version to avoid execution errors.
```
---

### 2023091842003488_Probleme%20bei%20der%20Nutzung%20von%20tensorboard.md
# Ticket 2023091842003488

 # HPC-Support Ticket: Probleme bei der Nutzung von tensorboard

## Problem Description
The user is unable to view TensorBoard results for their machine learning model training. The user has provided the following details:
- TensorBoard log directory: `/home/woody/iwfa/iwfa017h/Variante1/Versuch4_CWT_CNN/callbacks_Modeltraining_gaf_mtr_am_16.Sep_um_14h_50m/tensorboard`
- Commands executed:
  - In VS-Code terminal: `tensorboard --logdir=/home/woody/iwfa/iwfa017h/Variante1/Versuch4_CWT_CNN/callbacks_Modeltraining_gaf_mtr_am_16.Sep_um_14h_50m/tensorboard --port=6088 --load_fast=false`
  - In separate CMD: `ssh -g -L 6088:localhost:6088 -f -N iwfa017h@tinyx.nhr.fau.de -J iwfa017h@cshpc.rrze.fau.de`

## Root Cause
The user is experiencing issues with SSH port forwarding and TensorBoard configuration. The exact cause is not clear from the initial conversation, but it involves SSH tunneling and TensorBoard setup.

## Troubleshooting Steps
1. **Email Verification**: The HPC Admin requested the user to send the request from their FAU email address for verification.
2. **System Verification**: The HPC Admin asked which system the user is logged into with their VS-Code console.
3. **SSH Debugging**: The HPC Admin requested the user to provide the output of the SSH command with debugging enabled: `ssh -vv -L 6101:localhost:6101 iwfa017h@tinyx.nhr.fau.de`

## Solution
The user provided the SSH debug output, which showed successful authentication and port forwarding setup. However, the exact solution to the TensorBoard issue was not explicitly stated in the conversation. Further investigation into the TensorBoard configuration and SSH tunneling is required.

## Keywords
- TensorBoard
- SSH port forwarding
- Machine learning model training
- VS-Code terminal
- Debugging SSH
- Authentication
- Port forwarding

## Notes
- Ensure that the user is using their FAU email address for support requests.
- Verify the system the user is logged into with their VS-Code console.
- Use SSH debugging to troubleshoot port forwarding issues.
- Further investigation into TensorBoard configuration may be required.
---

### 2025030342003147_Unable%20to%20install%20conda%20modules.md
# Ticket 2025030342003147

 ```markdown
# HPC-Support Ticket: Unable to Install Conda Modules

## Problem Description
- **User Issue**: Unable to install specific conda modules for PyTorch and related packages.
- **Error Messages**:
  - Warnings about deprecated use of `.*` with relational operators.
  - Solving environment failed with initial frozen solve, retried with flexible solve.

## Key Points from Conversation
- **Initial Attempt**: User tried to install conda modules on the frontend node.
- **Cluster**: Alex cluster.
- **User ID**: b112dc10.
- **Command Used**:
  ```sh
  conda install pytorch==2.0.1 torchvision==0.15.2 torchaudio==2.0.2 pytorch-cuda=11.7 -c pytorch -c nvidia
  ```

## HPC Admin Response
- **Suggestion**: Install packages on a compute node with GPU support.
- **Method**: Use `salloc` for interactive GPU allocation.
- **Python Version**: Recommended to use `python/3.12-conda` to avoid version conflicts.

## User Action
- **SBATCH Script**: User created an SBATCH script to install the required packages on a compute node.
- **Script Content**:
  ```sh
  #!/bin/sh -l
  #SBATCH --gres=gpu:a40:1
  #SBATCH --time=1:0:00
  #SBATCH --error=timeplant.err
  #SBATCH --output=timeplant.out
  conda env list
  conda activate /home/atuin/b112dc/b112dc10/software/private/conda/envs/mononphm
  conda install pytorch==2.0.1 torchvision==0.15.2 torchaudio==2.0.2 pytorch-cuda=11.7 -c pytorch -c nvidia
  # Install PytorchGeometry and helper packages with CUDA support
  conda install pyg -c pyg
  pip install pyg_lib torch_scatter torch_sparse torch_cluster torch_spline_conv -f https://data.pyg.org/whl/torch-2.0.0+cu117.html
  # Install Pytorch3D with CUDA support
  conda install -c fvcore -c iopath -c conda-forge fvcore iopath
  conda install pytorch3d=0.7.4 -c pytorch3d
  # Install PytorchGeometry and helper packages with CUDA support
  conda install pyg -c pyg
  pip install pyg_lib torch_scatter torch_sparse torch_cluster torch_spline_conv -f https://data.pyg.org/whl/torch-2.0.0+cu117.html
  # Install Pytorch3D with CUDA support
  conda install -c fvcore -c iopath -c conda-forge fvcore iopath
  conda install pytorch3d=0.7.4 -c pytorch3d
  pip install -e .
  ```

## Outcome
- **Script Execution**: The script ran for 25 minutes.
- **Output**: The output file indicated that the GPU was allocated and the installation process was ongoing.

## Lessons Learned
- **Frontend vs Compute Node**: GPU-dependent packages should be installed on compute nodes with GPU support.
- **Interactive GPU Allocation**: Use `salloc` for interactive GPU allocation.
- **Python Version**: Use `python/3.12-conda` to avoid version conflicts.
- **SBATCH Script**: Useful for automating the installation process on compute nodes.

## Solution
- **Install on Compute Node**: Ensure that GPU-dependent packages are installed on compute nodes with GPU support.
- **Use SBATCH Script**: Automate the installation process using an SBATCH script to allocate GPU resources and install the required packages.
```
---

### 2025011142000531_CUDA%20Initialization%20Issue%20on%20A100_80%20GPU.md
# Ticket 2025011142000531

 ```markdown
# CUDA Initialization Issue on A100_80 GPU

## Problem Description
- **User Issue**: CUDA-related issue on the Alex cluster. Code that previously ran successfully on an A100 80GB GPU now fails with the error:
  ```
  RuntimeError: Unexpected error from cudaGetDeviceCount(). Did you run some cuda functions before calling NumCudaDevices() that might have already set an error? Error 802: system not yet initialized
  ```
  Additionally, `print(torch.cuda.is_available())` returns `False`, even though `nvidia-smi` detects the GPU.

## Investigation
- **Job Logs**:
  - Several jobs failed on node `a0532`.
  - Example job logs:
    ```
    JobId=2293679 UserId=btr0104h(210981) GroupId=btr0(14700) Name=run.sh JobState=FAILED Partition=a100 TimeLimit=1440 StartTime=2025-01-11T22:45:16 EndTime=2025-01-11T22:45:18 NodeList=a0532 NodeCnt=1 ProcCnt=16 WorkDir=/home/hpc/btr0/btr0104h/llm-o-mat ReservationName= Tres=cpu=16,mem=240000M,node=1,billing=16,gres/gpu=1,gres/gpu:a100=1 Account=btr0 QOS=normal WcKey=* Cluster=alex SubmitTime=2025-01-11T22:45:14 EligibleTime=2025-01-11T22:45:14 DerivedExitCode=0:0 ExitCode=2:0
    ```

- **System Logs**:
  - `dmesg` logs indicate NVLink initialization failures:
    ```
    [Sat Jan 11 14:36:19 2025] NVRM: knvlinkCheckNvswitchP2pConfig_IMPL: GPU 5 doesn't have a fabric address
    [Sat Jan 11 14:36:19 2025] NVRM: knvlinkCheckNvswitchP2pConfig_IMPL: GPU 6 doesn't have a fabric address
    ```
  - `nvidia-fabricmanager.service` failed:
    ```
    NVLink initialization failed for NodeId:0 GPU PCI bus id:00000000:96:00.0 enumIndex:5 NVL
    NVSwitch failure detected and degraded mode configuration set to abort Fabric Manager
    ```

## Root Cause
- **Hardware Failure**: Node `a0532` experienced hardware failures related to NVLink initialization.

## Solution
- **Node Removal**: The problematic node `a0532` was removed from the queue.
- **Health Check**: Added a health check for `nvidia-fabricmanager` in the health checker script.

## Follow-up
- **NVLink Issue**: The NVLink problem was resolved by power cycling the node (turning off, waiting 60 seconds, and turning back on).
- **Health Check**: Implemented a health check for `nvidia-fabricmanager` to prevent similar issues in the future.

## Keywords
- CUDA Initialization Error
- NVLink Failure
- nvidia-fabricmanager
- Hardware Failure
- Health Check
```
---

### 2023120442002829_cuda%20on%20hpc.md
# Ticket 2023120442002829

 ```markdown
# HPC Support Ticket: CUDA on HPC

## Keywords
- CUDA
- PyTorch
- GPU nodes
- Conda environment
- CUDA version mismatch

## Problem Description
- User encountered an error indicating CUDA was not available.
- `torch.cuda.is_available()` returned `False`.
- User suspected an issue with the Conda environment.

## Root Cause
- The environment was not built on a GPU node, leading to pip/conda not autodetecting a CUDA device and building only the CPU backend.
- Required modules (`python`, `cuda`, `cudnn`) were not loaded.

## Solution
1. **Start an interactive job on a GPU node.**
2. **Load required modules:**
   ```bash
   module avail python
   module load python/XY
   module load cuda
   module load cudnn
   ```
3. **Follow the remaining instructions on the provided documentation page:**
   [TensorFlow/PyTorch Documentation](https://hpc.fau.de/systems-services/documentation-instructions/special-applications-and-tips-tricks/tensorflow-pytorch/)

## Additional Issue
- CUDA version mismatch between the RTX 2080 (12.3) and the environment (12.1).

## Recommendation
- Use a consistent CUDA version for everything to avoid potential issues.

## Conclusion
- The user was able to access CUDA after following the instructions.
- The CUDA version mismatch was noted, and the user was advised to use a consistent version.
```
---

### 2024061042003424_Loadmodul%20CUDNN%20Version%209.1.0.70%2012x.md
# Ticket 2024061042003424

 # HPC Support Ticket: Load Module Request for CUDNN Version 9.1.0.70-12.x

## Keywords
- Load module
- CUDNN
- Version 9.1.0.70-12.x
- Version 9.2.0.82-12.x
- Alex (HPC system)

## Problem
- User requested a load module for CUDNN version 9.1.0.70-12.x.

## Solution
- HPC Admin confirmed the availability of the requested module (cudnn/9.1.0.70-12.x) and also informed about an additional available version (cudnn/9.2.0.82-12.x).

## General Learnings
- Users can request specific versions of software modules.
- HPC Admins can provide information on available software versions and modules.
- Communication between users and HPC Admins is essential for ensuring the availability of required software tools.

## Actions Taken
- HPC Admin confirmed the availability of the requested module and provided additional information on another available version.

## Relevant Links
- [FAU HPC Support](mailto:support-hpc@fau.de)
- [FAU HPC Website](https://hpc.fau.de/)

## Date
- 10.06.2024
---

### 2023062042001178_Alex%20Cluster%3A%20Treiberprobleme%20bei%20Verwendung%20vom%20Tensorflow-Modul.md
# Ticket 2023062042001178

 ```markdown
# HPC Support Ticket: TensorFlow Environment Issues on Alex Cluster

## Summary
User encountered long load times and performance issues while training neural networks with TensorFlow on the Alex Cluster. The problem was initially suspected to be related to TensorFlow version, CUDA paths, or fileserver load.

## Keywords
- TensorFlow
- Conda environment
- CUDA
- cuDNN
- TensorRT
- Fileserver load
- Long load times
- Performance issues

## Problem Description
The user reported long load times and performance issues while training neural networks with TensorFlow on the Alex Cluster. The initial suspicion was that the problem might be related to the TensorFlow version, CUDA paths, or fileserver load. The user also encountered issues with TensorRT warnings and long load times for TensorFlow.

## Root Cause
The root cause of the problem was identified as a combination of fileserver load and an issue with the user's script. The user's script contained a method that was causing delays, specifically the `shutil.rmtree()` method in the helper method for folder creation.

## Solution
The user removed the `shutil.rmtree()` method from their script and adjusted the rest of the code. This resolved the performance issues, and the script ran quickly without using `${TMPDIR}`.

## Steps Taken
1. **Initial Diagnosis**:
   - The user was advised to create a new conda environment and install an updated version of TensorFlow.
   - The user was also advised to load the TensorRT module to prevent warnings and ensure compatibility.

2. **Fileserver Load**:
   - The HPC Admin suspected that the fileserver load might be causing delays and advised the user to check the load on the fileserver.

3. **Script Adjustment**:
   - The user identified and removed the `shutil.rmtree()` method from their script, which resolved the performance issues.

4. **Zoom Meeting**:
   - The HPC Admin and the user had a Zoom meeting to discuss and troubleshoot the issue further.

## Conclusion
The issue was resolved by adjusting the user's script and ensuring that the fileserver load was not causing delays. The user's script now runs efficiently without the previously encountered performance issues.

## Lessons Learned
- Ensure that scripts do not contain methods that can cause delays, such as `shutil.rmtree()`.
- Check fileserver load when encountering long load times.
- Update TensorFlow and related modules to ensure compatibility and prevent warnings.

## References
- [TensorFlow GitHub Issue](https://github.com/tensorflow/tensorflow/issues/51521)
- [HPC Support Documentation](https://hpc.fau.de/)
```
---

### 2022120842002574_Installing%20pycuda%20with%20pip.md
# Ticket 2022120842002574

 ```markdown
# HPC-Support Ticket: Installing pycuda with pip

## Keywords
- pycuda
- pip3
- cuda.h
- CUDA module
- GPU node

## Problem
- User encountered an error while installing pycuda using pip3.
- Error message: `fatal error: cuda.h: No such file or directory`
- Root cause: CUDA module not loaded.

## Solution
- Load the CUDA module before running the pip command.
- Ensure the pip command is executed on a GPU node.

## General Learnings
- Always load the necessary modules before running commands that depend on them.
- Ensure that commands requiring specific hardware (e.g., GPU) are executed on nodes with that hardware.
```
---

### 2024031342002998_CUDA%20auf%20gracehop1%20geht%20nicht.md
# Ticket 2024031342002998

 # HPC Support Ticket Analysis: CUDA Issues on gracehop1

## Keywords
- CUDA
- gracehop1
- NV_ERR_NO_MEMORY
- NVIDIA Treiber
- Reboot
- Memory Allocation
- cudaGetDevice
- Treiberversion 555

## Summary
- **Issue**: CUDA functions returning "unknown error" on gracehop1.
- **Root Cause**: Possible memory allocation issues (NV_ERR_NO_MEMORY) leading to NVIDIA driver failures.
- **Actions Taken**:
  - Reviewed kernel logs indicating memory allocation failures.
  - Rebooted the system to resolve potential temporary issues.
  - Updated NVIDIA driver to version 555.
- **Outcome**: Issue persisted after reboot. Further investigation required to determine if the problem is with the application or the driver.

## Lessons Learned
- **Memory Allocation**: Ensure that applications are not requesting more memory than available on the GPU.
- **Driver Updates**: Regularly update NVIDIA drivers to address potential bugs and compatibility issues.
- **Log Analysis**: Kernel logs can provide valuable insights into hardware and driver issues.
- **Reboot**: Sometimes a system reboot can resolve temporary issues, but it is not a permanent solution.

## Next Steps
- **Application Review**: Verify that the user's application is not causing excessive memory allocation.
- **Driver Testing**: Test the updated NVIDIA driver (version 555) to see if the issue persists.
- **Further Log Analysis**: Continue monitoring kernel logs for additional error messages that may provide more context.

## Solution (if found)
- **Pending**: Further investigation is needed to determine if the issue is with the application or the NVIDIA driver.

---

This report provides a concise summary of the issue, actions taken, and lessons learned, which can be used as a reference for future support cases involving similar CUDA issues on HPC systems.
---

### 2023091442003637_Request%20for%20Environment%20Setup.md
# Ticket 2023091442003637

 # HPC Support Ticket: Request for Environment Setup

## Keywords
- Python
- TensorFlow
- CUDA Toolkit
- cuDNN
- Conda
- GPU Cluster
- Environment Setup

## Problem
- User requires specific software configurations for thesis work.
- Needs Python 3.9.17, TensorFlow 2.13.0, CUDA Toolkit 11.8.0, and cuDNN 8.6.0.163.
- Installation of cuDNN requires sudo privileges.

## Solution
- HPC Admins informed the user that GPU clusters have Python and CUDA modules available.
- User can install TensorFlow themselves.

## General Learnings
- Users can load Python and CUDA modules from the GPU clusters.
- Users are responsible for installing specific versions of TensorFlow.
- HPC Admins can provide guidance on available modules and installation procedures.

## Root Cause
- User needed a specific environment setup for thesis work, including specific versions of Python, TensorFlow, CUDA Toolkit, and cuDNN.

## Resolution
- HPC Admins advised the user to load the available Python and CUDA modules.
- User was instructed to install TensorFlow themselves.

## Additional Notes
- Security considerations and standard operating procedures may affect the feasibility of specific software installations.
- Users should be aware of the available modules and how to load them for their computations.
---

### 2022091842000714_issue%20in%20HPC%20cluster%3A%20tiny%20GPU.md
# Ticket 2022091842000714

 # HPC Support Ticket: Issue in HPC Cluster - TinyGPU

## Keywords
- HPC Cluster
- TinyGPU
- Python
- PyTorch
- CUDA
- Conda
- GPU Allocation
- Job Submission

## Problem Description
- User is unable to connect their Python/PyTorch project to TinyGPU.
- Error occurs when running `python -c 'import torch; print(torch.rand(2,3).cuda())'`.
- Error occurs when running `conda install -c conda-forge tensorflow`.

## Root Cause
1. User is attempting to run GPU-dependent code on the frontend, which lacks a GPU.
2. User is trying to install software in the global environment without root privileges.
3. User is not specifying GPU resources when submitting a job.

## Solution
1. **GPU Allocation**:
   - Start a job on one of the TinyGPU nodes.
   - Use `salloc` with the `--gres=gpu:1` option to allocate GPU resources.
   - Example: `salloc --gres=gpu:1`

2. **Conda Environment Setup**:
   - Create a personal Conda environment.
   - Activate the environment before installing packages.
   - Commands:
     ```bash
     conda create --name myenv python=3.9
     conda activate myenv
     ```
   - If issues persist, configure Conda to use a personal package directory:
     ```bash
     conda config --add pkgs_dirs $WORK/.conda/pkgs
     ```

3. **Job Submission**:
   - Refer to the [TinyGPU Cluster Documentation](https://hpc.fau.de/systems-services/documentation-instructions/clusters/tinygpu-cluster/) for detailed instructions on job submission.

## General Learnings
- Ensure GPU-dependent tasks are run on nodes with GPU resources.
- Use personal Conda environments for package management to avoid permission issues.
- Properly allocate resources when submitting jobs to the HPC cluster.

## References
- [TinyGPU Cluster Documentation](https://hpc.fau.de/systems-services/documentation-instructions/clusters/tinygpu-cluster/)
- [TensorFlow/PyTorch Documentation](https://hpc.fau.de/systems-services/documentation-instructions/special-applications-and-tips-tricks/tensorflow-pytorch/)
---

### 2024061342003713_No%20GPU%20activity%20in%20your%20currently%20running%20jobs%20%5Biwi9104h%5D.md
# Ticket 2024061342003713

 # HPC Support Ticket: No GPU Activity in User's Jobs

## Subject
No GPU activity in your currently running jobs [iwi9104h]

## Keywords
- GPU utilization
- Conda environment
- Interactive job
- Proxy settings
- Python auto detection
- CUDA

## Problem
- User's jobs on TinyGPU are not utilizing the requested GPU resources.
- Conda environment built on the frontend (tinyx) instead of a cluster node, causing Python auto detection to not find a GPU.

## Root Cause
- Incorrect environment setup: Conda environment was built on the frontend, leading to Python not detecting the GPU.
- HTTP connection error when trying to create a new conda environment due to network restrictions.

## Solution
1. **Rebuild Conda Environment on Compute Node:**
   - Cancel all running jobs to free up resources.
   - Use an interactive job to rebuild the conda environment on a compute node.
   - Load the Python and CUDA modules and install PyTorch with the matching CUDA version.

2. **Proxy Settings for Conda:**
   - Refer to the documentation for configuring proxy settings in the `.condarc` file to resolve HTTP connection errors.

3. **Monitor GPU Utilization:**
   - Use the monitoring tool to check GPU activity in the plots 'acc_utilization' and 'acc_mem_util'.

## Steps Taken
1. **Initial Notification:**
   - HPC Admin notified the user about the lack of GPU utilization in their jobs.
   - Provided a link to the monitoring tool to check GPU activity.

2. **Environment Rebuild Instructions:**
   - HPC Admin suggested rebuilding the conda environment on a compute node using an interactive job.
   - Provided documentation links for interactive job setup and proxy configuration.

3. **Resource Limitation:**
   - User's account was limited to 1 GPU until the issue was resolved and GPU usage was proven.

4. **Follow-Up:**
   - User confirmed successful environment setup and requested the removal of resource limitations.
   - HPC Admin verified GPU usage and lifted the resource limitations.

## Documentation Links
- [Interactive Job Setup](https://doc.nhr.fau.de/clusters/tinygpu/#interactive-job-single-gpu)
- [Proxy Configuration](https://doc.nhr.fau.de/faq/#why-does-my-application-give-an-http-https-timeout)

## Conclusion
The issue was resolved by rebuilding the conda environment on a compute node and configuring the proxy settings correctly. The user was able to utilize the GPU resources as intended, and the resource limitations were lifted.
---

### 2023062742002655_Problems%20while%20dealing%20with%20CUDA%20and%20CuDNN%20for%20Deep%20Learning.md
# Ticket 2023062742002655

 # HPC Support Ticket: CUDA and CuDNN for Deep Learning

## Keywords
- CUDA
- CuDNN
- OpenCV
- Python 3.10
- Conda environment
- Neural Network
- TinyGPU
- Modulefiles

## Problem
The user is having trouble installing CUDA and CuDNN libraries and building OpenCV with a CUDA backend for training a neural network in a Python 3.10 environment on the HPC system.

## Root Cause
The user is unaware of the pre-installed CUDA and CuDNN modules available on the HPC system and how to load them.

## Solution
The HPC system provides CUDA and CuDNN as environment modules. To load them, the user can use the following commands:
```bash
$ module add cuda cudnn
$ module list
```
After running these commands, the currently loaded modules should be displayed, such as:
```
Currently Loaded Modulefiles:
1) cuda/11.8.0
2) cudnn/8.8.0.121-11.8
```

## General Learnings
- The HPC system provides pre-installed modules for common libraries like CUDA and CuDNN.
- Users should check the available modules and load them as needed instead of trying to install them manually.
- The `module add` command is used to load modules, and `module list` displays the currently loaded modules.
- This solution can be applied to other software libraries and tools available as modules on the HPC system.
---

### 2022021842003064_Set%20the%20cuDNN%20path.md
# Ticket 2022021842003064

 # HPC-Support Ticket Conversation Summary

## Subject: Set the cuDNN path

### Keywords:
- CUDA
- cuDNN
- Sigpy
- Cupy
- Module load
- ImportError
- libcuda.so.1
- libcudnn.so.7

### Problem:
- User encountered `ImportError: libcuda.so.1: cannot open shared object file` while importing Sigpy with Cupy.
- Specific error: `ImportError: libcudnn.so.7: cannot open shared object file: No such file or directory`.

### Root Cause:
- Missing `libcudnn.so.7` library, which is part of `cudnn/8.0.5.39-cuda11.1`.
- Mismatch between CUDA toolkit version (10.2) and available CUDA versions on the cluster (11.1.0/11.2.0/11.2.2).

### Solution:
- Load the required cuDNN module: `module load cudnn/8.0.5.39-cuda11.1`.
- Switch to a compatible CUDA toolkit version (11.3) that matches the available CUDA versions on the cluster.

### Additional Information:
- User was advised to use CPU-only clusters (Emmy or TinyFAT) for running the code without GPU until the issue was resolved.
- User successfully ran the Sigpy tool on GPU with CUDA toolkit version 11.3.

### General Learning:
- Ensure compatibility between CUDA toolkit versions and available CUDA versions on the cluster.
- Load the required modules (e.g., cuDNN) to resolve missing library errors.
- Use CPU-only clusters for running code without GPU if necessary.

### Closure:
- The issue was resolved by switching to a compatible CUDA toolkit version.
- The user was able to run the Sigpy tool on GPU successfully.

---

This summary provides a concise overview of the problem, root cause, solution, and general learning points for future reference.
---

### 2024080542004564_pytorch%20Cuda%20not%20available.md
# Ticket 2024080542004564

 ```markdown
# HPC-Support Ticket: pytorch CUDA not available

## Keywords
- PyTorch
- CUDA
- GPU
- Interactive Job
- Frontend Knoten
- HTTP/HTTPS Timeout

## Problem Description
The user is experiencing issues with PyTorch CUDA, reporting that no drivers are installed on the machine. The user has followed the necessary steps for setting up Python and installing PyTorch but still encounters the problem.

## Root Cause
- The user attempted to install or use PyTorch CUDA on a frontend node, which does not have GPUs installed.
- The installation process may require downloading additional components, which could be affected by HTTP/HTTPS timeout issues.

## Solution
- Start an interactive job with GPU resources before installing or using PyTorch CUDA.
- If the installation requires downloading components, follow the instructions to prevent HTTP/HTTPS timeouts: [FAQ: Why does my application give an HTTP/HTTPS timeout?](https://doc.nhr.fau.de/faq/#why-does-my-application-give-an-http-https-timeout)

## General Learnings
- Ensure that GPU-dependent installations and operations are performed on nodes with GPU resources.
- Address potential network issues by configuring settings to prevent HTTP/HTTPS timeouts during installations.
```
---

### 2022051742004783_Job%20does%20not%20use%20GPU%20on%20Alex%20%5Biwi5070h%5D.md
# Ticket 2022051742004783

 ```markdown
# HPC Support Ticket: Job does not use GPU on Alex [iwi5070h]

## Keywords
- GPU utilization
- TensorFlow
- CUDA
- NVIDIA
- `nvidia-smi`
- Module loading

## Problem Description
- User's job on Alex (JobID 252704) did not utilize the GPU.
- Error messages indicated missing CUDA libraries (e.g., `libcudart.so.11.0`, `libcublas.so.11`).

## Root Cause
- The user did not load the necessary CUDA module.

## Solution
- The user was advised to load the CUDA module.
- Instructions for building TensorFlow were provided: [TensorFlow/PyTorch Instructions](https://hpc.fau.de/systems-services/systems-documentation-instructions/special-applications-and-tips-tricks/tensorflow-pytorch).

## Steps Taken
1. **Initial Notification**: HPC Admin informed the user that their job was not utilizing the GPU.
2. **Error Analysis**: The user provided error logs indicating missing CUDA libraries.
3. **Debugging**: HPC Admin requested the job script and output files for further analysis.
4. **Solution Identified**: The user realized they had not loaded the CUDA module.
5. **Resolution**: The user loaded the CUDA module and resolved the issue.

## Lessons Learned
- Always ensure that necessary modules (e.g., CUDA) are loaded before running GPU-intensive jobs.
- Use `nvidia-smi` to monitor GPU utilization.
- Follow the provided instructions for building and running TensorFlow on the HPC system.

## References
- [Working with NVIDIA GPUs](https://hpc.fau.de/systems-services/systems-documentation-instructions/special-applications-and-tips-tricks/working-with-nvidia-gpus/)
- [TensorFlow/PyTorch Instructions](https://hpc.fau.de/systems-services/systems-documentation-instructions/special-applications-and-tips-tricks/tensorflow-pytorch)
```
---

### 2024041642003499_Volatile%20memory%20utilization%20issue.md
# Ticket 2024041642003499

 ```markdown
# HPC Support Ticket: Volatile Memory Utilization Issue

## Summary
User encountered issues with TensorFlow and CUDA version mismatch on the Alex cluster.

## Keywords
- TensorFlow
- CUDA
- GPU
- Alex cluster
- nvidia-smi
- Module loading
- Version mismatch

## Problem
- User's TensorFlow 2.15.0 requires CUDA 12.2.0.
- Despite loading CUDA 12.2.0 using a fabfile, `nvidia-smi` shows CUDA 12.4.0.
- GPU utilization is 0, suspected to be due to version mismatch.

## Root Cause
- The `nvidia-smi` binary installed by the admin for monitoring purposes always shows CUDA 12.4.0, regardless of the loaded modules.
- The actual CUDA version used by the application is determined by the loaded modules and environment variables.

## Solution
- The user should not worry about the CUDA version shown by `nvidia-smi`.
- Ensure the correct CUDA module is loaded (e.g., `cuda/12.3.0` or `cuda/12.1.1`).
- Verify the environment variables to ensure the correct CUDA version is being used by the application.

## Steps Taken
1. **Initial Query**: User reported the issue with CUDA version mismatch and zero GPU utilization.
2. **Cluster Identification**: User confirmed using the Alex cluster.
3. **Module Loading**: User attempted to load CUDA 12.2.0 and 12.3.0, but `nvidia-smi` still showed CUDA 12.4.0.
4. **Admin Explanation**: HPC Admin explained that `nvidia-smi` is a monitoring tool and always shows CUDA 12.4.0. The actual CUDA version used by the application is determined by the loaded modules.
5. **Follow-up**: User requested connection to someone experienced with TensorFlow on GPU clusters.

## Conclusion
- The issue was clarified by the HPC Admin, explaining the behavior of `nvidia-smi`.
- User was advised to focus on the loaded modules and environment variables for the correct CUDA version.

## Next Steps
- User may need further assistance with setting up the conda environment or TensorFlow-specific questions, which can be directed to coworkers or additional support.
```
---

### 2025011042002291_Issue%3A%20Unable%20to%20register%20GPU%20devices.md
# Ticket 2025011042002291

 # HPC Support Ticket: Issue with Unable to Register GPU Devices

## Keywords
- TensorFlow
- GPU
- CUDA
- Conda
- Pip
- Dependencies
- Installation
- Environment
- SLURM
- Module

## Summary
The user encountered issues with registering GPU devices while using TensorFlow. The problem persisted despite reinstalling and creating new environments. The user provided a script and error logs for reference.

## Root Cause
- The user attempted to install TensorFlow using pip, which resulted in dependency resolution issues.
- The user tried to install TensorFlow-GPU on a machine without GPU capabilities.
- Conda had difficulty solving dependencies, leading to long installation times.

## Solution
1. **Follow Documentation**: Ensure that the user follows the installation instructions from the provided documentation.
2. **Use Conda for Installation**: Replace the pip install command with conda install commands for TensorFlow-GPU.
   ```bash
   module load cuda/12.6.1
   conda install tensorflow-gpu -c conda-forge
   ```
3. **Allocate GPU Resources**: Ensure that the job is allocated on a machine with GPU capabilities.
   ```bash
   salloc --gres=gpu:a100:1 --partition=a100 --time=4:00:00
   ```
4. **Try Different Versions**: If conda is unable to solve dependencies, try different versions of TensorFlow or install small packages after TensorFlow.

## Additional Notes
- The user also encountered similar issues with PyTorch installation, which took a long time to resolve dependencies.
- The HPC Admin suggested trying different versions of TensorFlow and installing small packages after TensorFlow to resolve dependency issues.

## Conclusion
The user should follow the provided documentation and ensure that the job is allocated on a machine with GPU capabilities. Using conda for installation and trying different versions of TensorFlow can help resolve dependency issues.
---

### 2024052242004162_Model%20training%20-%20running%20on%20cpu%20-%20iwi5202h.md
# Ticket 2024052242004162

 # HPC Support Ticket: Model Training Running on CPU Instead of GPU

## Keywords
- Deep learning
- GPU
- PyTorch
- Conda
- SLURM
- CUDA
- Virtual environment

## Problem Description
- User's deep learning training model runs on CPU instead of GPU.
- `torch.cuda.is_available()` returns `False`.
- User created a virtual environment using Conda and installed PyTorch and other necessary packages.
- Batch script includes GPU resource request but does not utilize GPU.

## Root Cause
- The frontend node (`tinyx`) does not have a GPU, so PyTorch cannot detect one.
- The virtual environment was likely created on a node without GPU, leading to hardware auto-detection failure.

## Solution
- Ensure the virtual environment is created on a GPU node.
- Follow the instructions provided in the [FAU PyTorch documentation](https://doc.nhr.fau.de/apps/pytorch/) to build the PyTorch environment.
- Contact the project supervisor for assistance in setting up the environment.

## Batch Script
```bash
#!/bin/bash -l
#SBATCH --gres=gpu:rtx2080ti:1
#SBATCH --time=06:00:00
#SBATCH --job-name=test
#SBATCH --export=NONE
unset SLURM_EXPORT_ENV
export http_proxy="http://proxy:80"
export https_proxy="http://proxy:80"
module load cuda
module load python
conda activate pcct
python main.py
```

## Additional Notes
- Ensure that the job is submitted to a node with GPU resources.
- Verify that the CUDA module is correctly loaded and compatible with the installed PyTorch version.

## References
- [FAU PyTorch Documentation](https://doc.nhr.fau.de/apps/pytorch/)

## Support Team
- HPC Admins
- 2nd Level Support Team
---

### 2024090342002068_Cuda%20Version%20Update.md
# Ticket 2024090342002068

 # HPC Support Ticket: Cuda Version Update

## Keywords
- Cuda version update
- Module tree
- Spack
- Cluster specification

## Problem
- User requested the latest Cuda version (12.6) on the module tree.
- User mentioned that the version should be available via Spack but couldn't find it.

## Root Cause
- The user did not specify the cluster they were using.

## Solution
- HPC Admin specified that Cuda 12.6.1 is now available on TinyGPU and Alex clusters.
- User confirmed that the issue was resolved after specifying the cluster.

## General Learnings
- Always specify the cluster when requesting software updates or support.
- Check the module tree for the latest software versions after updates.
- Communicate clearly with HPC support to ensure quick resolution of issues.
---

### 2025020342003694_Module%20Availability%20Sudden%20Issue.md
# Ticket 2025020342003694

 # Module Availability Sudden Issue

## Keywords
- Module Import Error
- Conda Environment
- Torch Module
- Environment Setup
- Documentation

## Problem Description
The user reported an issue with importing the `torch` module in their conda environment, despite it having worked previously.

## Root Cause
- The `torch` module was not found in the user's conda environment.
- Possible accidental deletion of the module.

## Solution
- The HPC Admin recommended creating a new conda environment and installing the `torch` module following the steps in the provided documentation.

## Steps to Resolve
1. Verify the presence of the `torch` module in the conda environment.
2. If the module is missing, create a new conda environment.
3. Follow the installation steps provided in the documentation:
   - [Python Environment Setup](https://doc.nhr.fau.de/environment/python-env/)
   - [PyTorch Installation](https://doc.nhr.fau.de/apps/pytorch/)

## General Learning
- Always verify the presence of required modules in the environment.
- Follow the official documentation for setting up environments and installing modules.
- Regularly check for accidental deletions or modifications in the environment.

## References
- [Python Environment Setup](https://doc.nhr.fau.de/environment/python-env/)
- [PyTorch Installation](https://doc.nhr.fau.de/apps/pytorch/)
---

### 2024061242002191_Installation%20of%20matplotlib%20on%20hpc%20server.md
# Ticket 2024061242002191

 # HPC Support Ticket: Installation of matplotlib on HPC Server

## Subject
Installation of matplotlib in a conda environment.

## User Issue
The user is trying to install matplotlib in a conda environment but the installation fails. The user is able to install matplotlib if pytorch cuda is not installed, but needs both packages.

## User Environment
- **Conda Environment**: `cudaEnv`
- **Python Version**: 3.12.3
- **Key Packages**:
  - pytorch: 2.3.1 (py3.12_cuda12.1_cudnn8.9.2_0)
  - cuda-cudart: 12.1.105
  - cuda-cupti: 12.1.105
  - cuda-libraries: 12.1.0
  - cuda-nvrtc: 12.1.105
  - cuda-nvtx: 12.1.105
  - cuda-opencl: 12.4.127
  - cuda-runtime: 12.1.0
  - numpy: 1.26.4
  - matplotlib: Not installed

## Error Message
```
ResolvePackageNotFound:
  - python=3.1
```

## Root Cause
The error indicates that the package is not available in the required version (python=3.1). The environment shows packages for python 3.1 and 3.12, suggesting a known bug with an outdated conda installation.

## Solution Steps
1. **SSH to Frontend**:
   ```
   ssh to tinyx
   ```
2. **Load Python Module**:
   ```
   module load python
   ```
3. **Remove Existing Environment**:
   ```
   conda remove -n cudaEnv --all
   ```
4. **Clean Conda Cache**:
   ```
   conda clean --all
   ```
5. **Start Interactive Job on GPU Node**:
   ```
   salloc.tinygpu --gres=gpu:1 --time=01:00:00
   ```
6. **Load Python Module Again**:
   ```
   module load python
   ```
7. **Set Proxy**:
   ```
   export http_proxy=http://proxy:80
   export https_proxy=http://proxy:80
   ```
8. **Rebuild Environment**:
   ```
   conda create -n cudaEnv python=3.12
   conda install -n cudaEnv pytorch cudatoolkit=12.1 -c pytorch -c nvidia
   conda install -n cudaEnv matplotlib -c conda-forge
   ```

## Additional Notes
- Python environments with GPU code must be built on a GPU node.
- Once the environment is working, write an sbatch file for job submission and activate the conda environment in the script.

## References
- [FAQ: How to Fix Conda Error T19 or T20](https://doc.nhr.fau.de/faq/#how-to-fix-conda-error-t19-or-t20)

## Keywords
- Conda
- Matplotlib
- PyTorch
- CUDA
- HPC
- Environment Setup
- Package Conflict
- GPU Node
- Interactive Job
- Conda Clean
- Proxy Settings
---

### 2024061842005793_grace-hop%3A%20cuda%20module%20paths.md
# Ticket 2024061842005793

 # HPC Support Ticket: CUDA Module Paths Issue

## Keywords
- CUDA module
- Nsight Compute (ncu)
- Module paths
- Nvidia
- SPACK
- Gracehop1

## Problem Description
The user loaded a CUDA module on `gracehop1` and attempted to use the `ncu` profiler binary. Despite loading the module, `ncu` tried to access a binary from `/opt/nvidia/nsight-compute/2024.2.0/target/linux-desktop-t210-a64/ncu`, which does not exist. The module-loaded CUDA version should be independent of the locally installed version, but there seems to be a conflict.

## Root Cause
Nvidia's `ncu` binary is hardcoded to search for specific paths in `/opt/nvidia/nsight-compute`, leading to a conflict with the module-loaded CUDA version.

## Solution
The simplest solution is to call `ncu` with the absolute path from `/opt`, specifically:
```sh
/opt/nvidia/nsight-compute/2024.2.0/ncu
```

## General Learnings
- Nvidia's tools may have hardcoded paths that can conflict with module-loaded software.
- Always check the paths and dependencies of binaries when using modules.
- Using absolute paths can sometimes bypass path conflicts.

## Next Steps
- Consider updating the locally installed CUDA version to a more recent one.
- Review and potentially update the module configurations to avoid such conflicts in the future.

## References
- HPC Admin's response regarding Nvidia's path handling.
- User's initial report on the issue.
---

### 2018072642001326_Drivers%20installation%20or%20not.md
# Ticket 2018072642001326

 # HPC Support Ticket: Drivers Installation Query

## Keywords
- CUDA
- cuDNN
- TensorFlow
- NVidia drivers
- GPU hardware
- Compute nodes
- Login nodes
- `nvidia-smi`

## Problem
- User installed CUDA, cuDNN, and TensorFlow in their personal folder on the HPC drive.
- TensorFlow is not working when running Python3.
- User is unsure if NVidia drivers are installed and cannot install them due to lack of sudo privileges.
- `locate nvidia-smi` command returns nothing, suggesting drivers may not be installed.

## Root Cause
- User is attempting to run GPU-dependent software on nodes without GPU hardware.
- NVidia drivers and CUDA toolkit are installed only on specific clusters or compute nodes with GPU hardware, not on login nodes.

## Solution
- Inform the user that NVidia drivers and CUDA toolkit are installed on all compute nodes with GPU hardware.
- Direct the user to the relevant documentation for GPU cluster information:
  - [Tinyx Clusters](https://www.anleitungen.rrze.fau.de/hpc/tinyx-clusters/#collapse_1)
  - [Emmy Cluster](https://www.anleitungen.rrze.fau.de/hpc/emmy-cluster/#batch)
- Advise the user to submit jobs to the appropriate GPU-enabled clusters or compute nodes.

## General Learning
- NVidia drivers and CUDA toolkit are pre-installed on compute nodes with GPU hardware.
- Login nodes do not have GPU hardware.
- Users should submit jobs to GPU-enabled clusters for GPU-dependent tasks.
- Documentation provides details on available GPU resources and usage instructions.
---

### 2024021942000687_Cuda_12.3.md
# Ticket 2024021942000687

 # HPC Support Ticket: Cuda Version Request

## Keywords
- Cuda
- Version 12.3
- Alex Cluster
- Software Installation

## Problem
- **User Request**: Need for Cuda version 12.3 or newer on the Alex cluster.
- **Current State**: Only up to Cuda version 12.1.1 is available.

## Solution
- **Action Taken**: HPC Admin installed Cuda version 12.3.0 on the Alex cluster.
- **Outcome**: Cuda/12.3.0 is now available for use.

## General Learnings
- Users may request specific software versions for their research needs.
- HPC Admins can install and update software versions upon user requests.
- Effective communication and prompt action can resolve user requests efficiently.

## Next Steps
- Inform users about the availability of the new Cuda version.
- Monitor for any issues related to the newly installed software version.
---

### 2023071142003511_Cuda%20path%20on%20HPC.md
# Ticket 2023071142003511

 # HPC Support Ticket: Cuda Path on HPC

## Keywords
- CUDA_HOME environment variable
- CUDA installation
- Compute Capability (CC)
- TORCH_CUDA_ARCH_LIST
- Python setup
- Trainable bilateral filter

## Problem
- User encountered an error while trying to install a trainable bilateral filter on the HPC cluster.
- The error indicated that the `CUDA_HOME` environment variable was not set.

## Root Cause
- The `CUDA_HOME` environment variable was not set, which is required for the installation process.

## Solution
1. **Set CUDA_HOME Environment Variable:**
   - List available CUDA versions using `module avail cuda`.
   - Load the desired CUDA version using `module add cuda/<version>`.
   - The module will automatically set the `CUDA_HOME` environment variable.

2. **Install Dependencies:**
   - Create a new conda environment: `conda create -n test python=3.10`.
   - Activate the environment: `conda activate test`.
   - Install required packages: `pip install torch torchvision torchaudio`.

3. **Set TORCH_CUDA_ARCH_LIST:**
   - Determine the Compute Capability (CC) of the target GPUs.
   - For A100 on TinyGPU, the CC is 8.0.
   - Install the package with the appropriate CC: `TORCH_CUDA_ARCH_LIST="8.0" pip install bilateralfilter_torch`.

## General Learnings
- Always ensure that the `CUDA_HOME` environment variable is set when working with CUDA-dependent applications.
- Use the `module` command to manage software versions and environment variables on the HPC cluster.
- Check the Compute Capability (CC) of the target GPUs and set the `TORCH_CUDA_ARCH_LIST` accordingly when installing packages that require GPU support.

## Closure
- The user successfully installed the trainable bilateral filter after following the provided steps.
- The ticket was closed after the user confirmed the resolution.
---

### 2025012042003065_CuPy%20installation%20issue%20on%20ALEX.md
# Ticket 2025012042003065

 ```markdown
# HPC-Support Ticket: CuPy Installation Issue on ALEX Cluster

## Subject
CuPy installation issue on ALEX cluster in an interactive job.

## User Issue
- **Error Message:**
  ```bash
  ERROR: Could not find a version that satisfies the requirement cupy-cuda12x (from versions: none)
  ERROR: No matching distribution found for cupy-cuda12x
  ```
- **Modules Loaded:**
  ```bash
  1) python/3.9-anaconda
  2) gcc/11.2.0 <aL>
  3) openmpi/4.1.6-gcc11.2.0-cuda
  4) cuda/12.6.1
  ```
- **Attempted Solution:**
  ```bash
  pip install cupy-cuda12x
  ```

## HPC Admin Response
- **Initial Suggestion:**
  ```bash
  module load python openmpi cuda
  conda create -n cupy-test
  conda activate cupy-test
  pip install cupy-cuda12x
  ```
- **Additional Issue:**
  - User encountered an error installing `mpi4py` due to a compiler switch issue.
  - **Error Message:**
    ```bash
    nvc-Error-Unknown switch: -fno-strict-overflow
    ```
  - **Solution:**
    ```bash
    CFLAGS=-noswitcherror pip install mpi4py
    ```

## Detailed User Procedure
- **Full Procedure:**
  ```bash
  ssh alex
  module load python
  module load openmpi/4.1.6-nvhpc23.7-cuda
  module load cuda/12.6.1
  conda create -n alex
  conda activate alex
  conda install blas=*=*mkl
  conda install libblas=*=*mkl
  conda install numpy scipy
  conda install -c conda-forge pytest pytest-mpi pytest-cov coverage black isort ruff just pre-commit -y
  salloc --partition=a40 --nodes=1 --gres=gpu:a40:1 --time 01:00:00
  export http_proxy=http://proxy:80
  export https_proxy=http://proxy:80
  conda activate alex
  pip install cupy-cuda12x
  ```

## Final Solution
- **Resolved Issue:**
  ```bash
  conda create -n cupy-conda
  conda activate cupy-conda
  conda install -c conda-forge cupy-core
  conda install numpy scipy
  conda install blas=*=*mkl
  conda install libblas=*=*mkl
  conda install -c conda-forge pytest pytest-mpi pytest-cov coverage black isort ruff just pre-commit -y
  ```

## Keywords
- CuPy installation
- Conda environment
- Module loading
- MPI4PY installation
- Compiler switch issue
- HPC cluster
- Interactive job

## General Learning
- **Root Cause:**
  - Conflict between packages and modules loaded.
  - Compiler switch issue with NVHPC compilers.
- **Solution:**
  - Reorder package installation to resolve conflicts.
  - Use specific compiler flags to resolve switch issues.
```
---

### 2023072542002255_HPC%20Cuda%20error.md
# Ticket 2023072542002255

 # HPC Support Ticket Conversation: HPC Cuda Error

## Keywords
- HPC
- Cuda Error
- Quota
- Conda
- Miniconda
- Python
- GPU
- TinyGPU
- Dependencies
- Bilateral Filter

## Summary
The user encountered a CUDA error while trying to run a script involving a trainable bilateral filter on the HPC. Additionally, the user had issues with exceeding the quota on the filesystem.

## Root Cause of the Problem
1. **CUDA Error**: The user's script was breaking dependencies of `bilateralfilter_torch` after installing additional packages.
2. **Quota Issue**: The user's Miniconda installation was consuming a significant amount of space, leading to quota exceedance.

## Solutions Provided
### CUDA Error
- **Install `bilateralfilter_torch` last**: Ensure that it is the final package installed to avoid dependency conflicts.
- **Maintain Dependency Versions**: Ensure that running `pip/conda install` does not change the version of any dependency of `bilateralfilter_torch`.
- **GPU Compatibility**: Build the code on the same GPU intended for analysis to ensure compatibility.

### Quota Issue
- **Clean Conda Packages**: Use `conda clean --tarballs` or `conda clean -all` to remove unneeded files from the Conda package directory.
- **Configure Conda Directories**: Set custom directories for Conda packages and environments to avoid quota issues on `/home/hpc`.
  ```bash
  conda config --add pkgs_dirs $WORK/software/privat/conda/pkgs
  conda config --add envs_dirs $WORK/software/privat/conda/envs
  ```

## General Learnings
- **Dependency Management**: Be cautious with package installations to avoid breaking dependencies.
- **Quota Management**: Regularly clean up unnecessary files and configure software to use appropriate directories to manage quota effectively.
- **GPU Compatibility**: Ensure that code is built and tested on the same GPU architecture to avoid compatibility issues.

## References
- [Getting Started Guide](https://hpc.fau.de/systems-services/documentation-instructions/getting-started/)
- [TinyGPU Cluster Documentation](https://hpc.fau.de/systems-services/documentation-instructions/clusters/tinygpu-cluster/)
---

### 2024041542004338_Issue%20with%20Pytorch%20Cuda%20support.md
# Ticket 2024041542004338

 # Issue with PyTorch CUDA Support

## Keywords
- PyTorch
- CUDA
- Conda environment
- Frontend node
- Compute node
- GPU availability

## Problem Description
The user encountered an issue where `torch.cuda.is_available()` returned `False` after installing PyTorch in a new Conda environment. The user followed the HPC documentation for installation but faced this issue despite successful installations in previous environments.

## Root Cause
The user was running the command on a frontend node, which does not have access to GPUs. Frontend nodes are typically used for login and job submission, not for compute-intensive tasks that require GPUs.

## Solution
The HPC Admin advised the user to run the command on a compute node, which has access to GPUs. The user confirmed that running the command in a job on a compute node resolved the issue.

## Lessons Learned
- **Frontend vs. Compute Nodes**: Frontend nodes do not have GPUs. Compute nodes should be used for tasks that require GPU access.
- **Environment Testing**: Testing the availability of packages like PyTorch with CUDA support should be done on compute nodes.
- **Job Submission**: Use interactive jobs or job scripts to access compute nodes for GPU-intensive tasks.

## Additional Notes
- The user's `.bash_profile` content was not the cause of the issue.
- The user was using Python 3.9-anaconda on the Alex cluster.

## Conclusion
Ensure that GPU-dependent tasks are run on compute nodes, not frontend nodes. This is crucial for accurate testing and execution of GPU-intensive applications.
---

### 2023120442000358_Job%20on%20Alex%20does%20not%20use%20GPU%20%5Biwwm101h%5D.md
# Ticket 2023120442000358

 # HPC Support Ticket: Job on Alex Does Not Use GPU

## Keywords
- GPU utilization
- Conda environment
- PyTorch
- CUDA
- ClusterCockpit
- `nvidia-smi`
- `srun`

## Summary
A user reported that their job on the HPC cluster was not utilizing the allocated GPUs. The issue was traced back to a problem with the Conda environment and PyTorch installation.

## Root Cause
- The user's Conda environment was not properly configured to interact with CUDA.
- PyTorch Lightning was installed on a server without a GPU, resulting in a CPU-only build.

## Steps Taken
1. **HPC Admin Notification**: The admin notified the user that their job was not using the allocated GPUs and provided instructions to check GPU utilization using `nvidia-smi` and ClusterCockpit.
2. **User Response**: The user mentioned that their previous Conda environment used to interact with CUDA but stopped working after installing PyTorch Lightning. They also mentioned issues with ClusterCockpit metrics.
3. **HPC Admin Follow-up**: The admin suggested that the issue might be due to installing PyTorch Lightning on a server without a GPU, leading to a CPU-only build. They also provided guidance on checking GPU metrics in ClusterCockpit.

## Solution
- Ensure that PyTorch and related packages are installed on a node with GPU access to avoid CPU-only builds.
- Use `nvidia-smi` to check GPU utilization.
- Check GPU metrics in ClusterCockpit under metrics starting with "ACC" for accelerator/GPU.

## Additional Notes
- There is no hard limit on GPU time enforced by the HPC admin.
- The ticket was closed to consolidate communication into a single ticket for easier management.

## References
- [PyTorch Installation Guide](https://pytorch.org/get-started/locally/)
- [ClusterCockpit Monitoring System](https://monitoring.nhr.fau.de/)
---

### 2024051042003533_Installation%20Cuda%20und%20Nvidia%20Toolkit%20auf%20Alex.md
# Ticket 2024051042003533

 # HPC Support Ticket: Installation of CUDA and NVIDIA Toolkit on Alex

## Keywords
- CUDA
- NVIDIA Toolkit
- Ubuntu
- AlmaLinux
- TinyLlama
- XFormers
- Flash Attention
- Compilation Errors
- Apptainer
- Singularity

## Problem Description
The user attempted to install CUDA and NVIDIA Toolkit on the Alex HPC system following an installation guide designed for Ubuntu 22.04. The installation of XFormers and Flash Attention failed due to compilation errors.

## Root Cause
- The installation guide provided by the user is specific to an apt-based distribution (Ubuntu 22.04), while Alex uses AlmaLinux, which is not apt-based.
- The user encountered unmet dependencies and compilation errors when trying to install XFormers and Flash Attention.

## Solution
- The HPC Admin suggested building CUDA and other dependencies manually using user-spack or conda modules, or using an Apptainer/Singularity container.
- The HPC Admin provided an Apptainer definition file for building the environment.

## General Learnings
- Always ensure that installation guides are compatible with the target operating system.
- For non-apt-based systems like AlmaLinux, consider using package managers like Spack or containerization tools like Apptainer/Singularity.
- When encountering unmet dependencies or compilation errors, consider building the required packages from source.

## Apptainer Definition File
The HPC Admin provided an Apptainer definition file (`Tinyllama.def`) for building the environment. The user can build the container using the following command:
```bash
apptainer build --fake Tinyllama.sif Tinyllama.def
```

## Future Recommendations
- Use containerization tools like Apptainer/Singularity for complex software installations to ensure consistency across different environments.
- Consult the HPC support team for assistance with compatibility issues and installation guides.

---

This report provides a summary of the HPC support ticket, including the problem description, root cause, solution, general learnings, and future recommendations. It can be used as a reference for support employees to address similar issues in the future.
---

### 2023110742002281_Alex%3A%20LocalColabFold%20funktioniert%20nicht%20mehr.md
# Ticket 2023110742002281

 # HPC Support Ticket: LocalColabFold Installation Issue

## Summary
The user encountered issues with their local installation of LocalColabFold, which was not functioning properly. The error messages indicated problems with TensorRT and GPU libraries.

## Root Cause
- Missing TensorRT dependency.
- Missing CUDA libraries.
- Potential updates to libraries causing dependency issues.

## Error Messages
```
2023-11-07 12:12:35.476431: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Could not find TensorRT
2023-11-07 12:12:37.072425: W tensorflow/core/common_runtime/gpu/gpu_device.cc:1956] Cannot dlopen some GPU libraries. Please make sure the missing libraries mentioned above are installed properly if you would like to use GPU. Follow the guide at https://www.tensorflow.org/install/gpu for how to download and setup the required libraries for your platform.
Skipping registering GPU devices...
```

## Solutions
1. **Install TensorRT**:
   ```bash
   pip install tensorrt
   ```

2. **Install CUDA libraries**:
   ```bash
   conda install -c nvidia cuda-nvcc
   ```

3. **Update LD_LIBRARY_PATH**:
   ```bash
   export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CONDA_PREFIX/lib/:$CONDA_PREFIX/lib/python3.10/site-packages/tensorrt
   ```

## Additional Information
- The user was able to resolve the issue by following the above steps.
- The job ran successfully on an A100 GPU despite some warnings about TensorRT and GPU libraries.
- The user provided links to the Jupyter notebook and the local version of LocalColabFold they were using.

## Future Considerations
- Ensure that all dependencies are correctly installed and updated.
- Consider creating a workflow for running AlphaFold-related methods on the HPC system to handle frequent updates and dependencies.

## References
- [LocalColabFold GitHub Repository](https://github.com/YoshitakaMo/localcolabfold)
- [AlphaFold2 Jupyter Notebook](https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb)

## Conclusion
The issue was resolved by installing the missing TensorRT and CUDA libraries. The user was able to run their AlphaFold job successfully on the HPC system.
---

### 2023080142002253_Trying%20to%20install%20PyKeOps%20on%20Alex%3B%20CUDA%20libs%20not%20found.md
# Ticket 2023080142002253

 # HPC Support Ticket: PyKeOps Installation Issue on Alex Cluster

## Keywords
- PyKeOps
- CUDA
- Conda
- Python
- PyTorch
- LD_LIBRARY_PATH
- CUDA_PATH
- LIBRARY_PATH
- nvrtc

## Problem Description
The user encountered issues with installing and running PyKeOps within a Conda environment on the Alex cluster. Despite successful installation, importing PyKeOps resulted in a warning indicating that CUDA libraries were not detected, and `pykeops.test_torch_bindings()` threw a `KeyError: 'nvrtc'`.

## Root Cause
- The CUDA module was missing the `LD_LIBRARY_PATH`.
- The `CUDA_PATH` environment variable was not set, causing `nvrtc.h` to not be found.
- The `$CUDA_PATH/lib64` was not added to `LIBRARY_PATH`, preventing linking with `libnvrtc.so`.

## Solution
1. Ensure the CUDA module includes the `LD_LIBRARY_PATH`.
2. Set and export the `CUDA_PATH` environment variable.
3. Add `$CUDA_PATH/lib64` to `LIBRARY_PATH`.

```bash
export CUDA_PATH=$CUDA_ROOT
export LIBRARY_PATH=$CUDA_PATH/lib64${LIBRARY_PATH:+":"}${LIBRARY_PATH:-""}
```

4. Run the Python script to test PyKeOps with Torch bindings.

```bash
python3 -c "import pykeops; pykeops.test_torch_bindings()"
```

## Outcome
The user confirmed that the solution worked, and PyKeOps with Torch bindings was functioning correctly.

## General Lessons
- Ensure all necessary environment variables are set when using CUDA libraries.
- Verify that the CUDA module includes the `LD_LIBRARY_PATH`.
- Properly configure the `LIBRARY_PATH` to include CUDA library paths.

## Ticket Closure
The ticket was closed after the user confirmed the resolution of the issue.
---

### 2019060442002634_Installation%20von%20JAX%20mit%20GPU%20Support.md
# Ticket 2019060442002634

 # HPC Support Ticket: Installation von JAX mit GPU Support

## Keywords
- JAX
- GPU Support
- CUDA
- Internetverbindung
- Proxy-Server
- TinyGPU
- Installation
- Build Prozess
- Abhängigkeiten

## Problem
Der Benutzer möchte die Bibliothek JAX mit GPU-Unterstützung auf dem HPC installieren. Die CPU-only Version konnte erfolgreich installiert werden, jedoch scheitert die Installation mit GPU-Unterstützung, da während des Build-Prozesses sowohl CUDA als auch eine Internetverbindung zum Download weiterer Abhängigkeiten benötigt wird. CUDA ist nur auf TinyGPU verfügbar, und es gibt keine Internetverbindung.

## Lösung
Die TinyGPU-Rechenknoten können über den Proxy-Server des RRZE auf das Internet zugreifen. Der Benutzer muss den Proxy-Server in unterschiedlicher Weise angeben, je nachdem, was der Installationsprozess für den Zugriff im Detail verwendet. Beispiele für die Konfiguration des Proxy-Servers:

- Allgemeine Umgebungsvariablen:
  ```bash
  export http_proxy=http://proxy.rrze.uni-erlangen.de
  export https_proxy=http://proxy.rrze.uni-erlangen.de
  export HTTP_PROXY=http://proxy.rrze.uni-erlangen.de
  export HTTPS_PROXY=http://proxy.rrze.uni-erlangen.de
  ```

- Für `pip`:
  ```bash
  pip install --proxy "http://proxy.rrze.uni-erlangen.de" <package>
  ```

- Für `git`:
  ```bash
  git config --global http.proxy http://proxy.rrze.uni-erlangen.de
  ```

## Allgemeine Erkenntnisse
- Die TinyGPU-Rechenknoten haben Zugriff auf das Internet über einen Proxy-Server.
- Der Proxy-Server muss korrekt konfiguriert werden, um den Zugriff auf externe Ressourcen während des Build-Prozesses zu ermöglichen.
- Verschiedene Tools und Bibliotheken erfordern unterschiedliche Methoden zur Konfiguration des Proxy-Servers.

## Weiterführende Informationen
- [JAX GitHub Repository](https://github.com/google/jax)
- [RRZE HPC Services](http://www.hpc.rrze.fau.de/)

## Kontakt
- HPC Support: support-hpc@fau.de
---

### 2023030742003241_Installation%20of%20Tensorflow%20-%20b109dc10.md
# Ticket 2023030742003241

 ```markdown
# HPC-Support Ticket Conversation: Installation of TensorFlow

## Issue Summary
User encountered issues running a deep learning (DL) script on AlexGPGPU. The primary issues were related to loading libraries and saving numpy files.

## Key Points
- **Initial Issue**: User could not load TensorFlow libraries and encountered a `FileNotFoundError` when saving a numpy file.
- **Modules Loaded**:
  - `cudnn/8.2.4.15-11.4`
  - `cuda/11.5.0`
  - `python/tensorflow-2.7.0py3.9`
  - `000-all-spack-pkgs/0.17.0`

## Conversation Highlights

### Initial Contact
User reported issues with loading TensorFlow libraries and saving numpy files.

### HPC Admin Response
- **TensorRT Libraries**: Noted that TensorRT libraries are not available due to Nvidia licensing restrictions.
- **FileNotFoundError**: Identified that the `FileNotFoundError` was due to a missing directory.

### Further Debugging
- **User's Own TensorFlow Installation**: Identified that the user had a local TensorFlow installation that might be conflicting with the module.
- **Deinstallation of Local TensorFlow**: User deinstalled the local TensorFlow installation but encountered new errors.

### HPC Admin Testing
- **Reproduction Attempt**: HPC Admin successfully ran the script in a different account after making minor adjustments.
- **Potential Account Issue**: Suggested that the issue might be specific to the user's account.

### Resolution
- **Local Directory Issue**: User identified that the `.local` directory was causing the issue. Renaming this directory resolved the problem.

## Solution
- **Rename `.local` Directory**: The user renamed the `.local` directory in their home directory, which resolved the conflicts and allowed the script to run successfully.

## Conclusion
The issue was resolved by identifying and renaming the problematic `.local` directory in the user's home directory. This highlights the importance of checking for local installations and configurations that might conflict with HPC modules.
```
---

### 2023090142000986_Unable%20to%20install%20Cuda%20lib%20of%20tinyx.md
# Ticket 2023090142000986

 # HPC Support Ticket Conversation Analysis

## Keywords
- CUDA installation
- Cupy library
- Data transfer between accounts
- SCP
- Rsync
- Public key error

## What Can Be Learned

### CUDA Installation Issue
- **Problem**: User encountered an error while installing the Cupy library for GPU parallelization.
- **Steps Taken**:
  1. Loaded Python module.
  2. Created a new Conda environment.
  3. Activated the Conda environment.
  4. Loaded CMake and CUDA modules.
  5. Attempted to install Cupy using `pip install cupa`.
- **Potential Issue**: Missing error message details.
- **Solution**: User decided not to use CUDA for the time being.

### Data Transfer Between Accounts
- **Problem**: User needed to transfer large data between two accounts without downloading to a local system.
- **Attempted Solution**: Used SCP but encountered a "Permission denied (public key)" error.
- **Root Cause**: Possible issue with SSH key setup.
- **Alternative Solution**:
  - **Shared Location**: Refer to FAQ for cross-using data between HPC accounts.
  - **Rsync Command**:
    ```sh
    rsync -vrhPEt --stats iwia041h@cshpc:/home/woody/iwia/iwia041h/walberlarunsautomation/automation/sh_Data_set_1/sh_Sim_Output/Sim_GM_2_RE_100_5K_Rand_Loc_Y_Y /home/atuin/b144dc/b144dc14/Simulation_Data
    ```
    - **Note**: User needs to be logged in with the destination account (`b144dc14@cshpc`).

## General Learnings
- **Documentation**: Always refer users to relevant FAQs or documentation for common issues.
- **Error Details**: Request detailed error messages for better troubleshooting.
- **Alternative Tools**: Suggest alternative tools like `rsync` for data transfer if `scp` fails.
- **SSH Key Management**: Ensure proper SSH key setup for secure and seamless data transfer between accounts.

## Conclusion
This conversation highlights the importance of detailed error reporting and the use of alternative tools for common tasks like data transfer. It also emphasizes the need for proper documentation and FAQs to guide users through common issues.
---

### 2024100942001751_Pytorch%20installation.md
# Ticket 2024100942001751

 # HPC Support Ticket: Pytorch Installation Issue

## Keywords
- Pytorch installation
- Conda environment
- Channel priority
- Anaconda license changes

## Problem Description
The user encountered an error while trying to install Pytorch in a conda environment. The error message indicated that no matching distribution for `torch` could be found.

## Root Cause
The issue was caused by the `channel_priority: strict` setting in the `condarc` configuration, which was implemented due to recent license changes by Anaconda. This setting prevented the installation of Pytorch from the specified channels.

## Solution
To resolve the issue, the user was advised to disable the channel priority setting by running the following command:
```bash
conda config --set channel_priority disabled
```
Additionally, it was recommended to ensure that the `defaults` channel does not show up in the channel list.

## General Lessons Learned
- License changes by software providers can impact the configuration and usage of tools in HPC environments.
- The `channel_priority` setting in conda can affect the availability of packages from certain channels.
- Disabling the `channel_priority` setting can resolve issues related to package installation in conda environments.

## Follow-up Actions
- Monitor for any further issues related to Anaconda license changes.
- Update documentation to reflect the changes in conda configuration settings.
---

### 2024060742001441_Cuda%20module%2012.4.1.md
# Ticket 2024060742001441

 ```markdown
# HPC-Support Ticket Conversation: Cuda Module 12.4.1

## Keywords
- Cuda 12.4.1
- Module
- Conda
- Flash-attn
- Cuda Home
- Installation
- Alex
- TinyGPU

## Problem
- User requested a module with Cuda 12.4.1.
- User encountered issues building flash-attn with Cuda in Conda.
- Cuda installation was not being recognized despite being present and Cuda Home being set.

## Solution
- HPC Admin informed the user that Cuda 12.4.1 is already available on Alex.
- TinyGPU module with Cuda 12.4.1 would be available later in the afternoon.

## General Learnings
- Ensure that the required Cuda version is available as a module on the HPC system.
- Check for existing modules before attempting to install or configure Cuda manually.
- Communicate with HPC Admins for module availability and updates.
```
---

### 2023102642003791_Problem%20with%20CUDA%20availability%20-%20iwi1010h.md
# Ticket 2023102642003791

 # HPC Support Ticket: Problem with CUDA Availability

## Problem Description
User encountered issues with CUDA availability when starting a batch job on the tinygpu cluster. Despite loading CUDA and CUDNN modules and installing CUDA toolkit and CUDNN in a conda environment, `torch.cuda.is_available()` returned `False`.

## Root Cause
- The conda environment was initially built on the frontend (tinyx) where the GPU was not detected.
- Conda/pip builds CPU-only code if the GPU is not detected during installation.

## Solution Steps
1. **Build Environment on GPU Node**:
   - Start an interactive job on a GPU node:
     ```bash
     salloc.tinygpu --gres=gpu:1 --partition=rtx3080 --time=02:00:00
     ```
   - Load necessary modules:
     ```bash
     module load python/3.10-anaconda
     ```
   - Create a new conda environment:
     ```bash
     conda create -n <myenv> python==3.10.9
     ```
   - Install PyTorch with GPU support:
     ```bash
     conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia
     ```

2. **Clone Preinstalled Environment**:
   - Clone the preinstalled PyTorch environment:
     ```bash
     conda create --name myclone --clone pytorch
     ```
   - Install additional packages as needed.

3. **Avoid Module Load in Batch Script**:
   - Comment out all `module load` commands in the batch script.
   - Ensure no modules are loaded on the frontend when submitting the job.

4. **Check Resource Utilization**:
   - Use `nvidia-smi` to check GPU utilization:
     ```bash
     nvidia-smi
     ```
   - Refer to the ClusterCockpit documentation for detailed monitoring:
     [ClusterCockpit Introduction](https://www.fau.tv/clip/id/46327)
   - Additional documentation on working with NVIDIA GPUs:
     [Working with NVIDIA GPUs](https://hpc.fau.de/systems-services/documentation-instructions/special-applications-and-tips-tricks/working-with-nvidia-gpus/)

## Additional Notes
- Ensure the conda environment does not contain packages for multiple Python versions.
- Clean the conda package cache if necessary:
  ```bash
  conda clean --all
  ```
- The error "Unable to find a valid cuDNN algorithm to run convolution" was resolved by decreasing the batch size due to insufficient VRAM memory.

## Conclusion
The user successfully resolved the CUDA availability issue by building the conda environment on a GPU node and cloning a preinstalled environment. Additionally, avoiding module loads in the batch script and monitoring GPU utilization with `nvidia-smi` helped in managing resources effectively.
---

### 2023070342004295_Help%20required%20with%20GPU%20access.%20user%20%3A%20iwfa025h.md
# Ticket 2023070342004295

 # HPC Support Ticket: GPU Access Issue

## Subject
Help required with GPU access. User: iwfa025h

## Issue
User iwfa025h is unable to access GPUs on the HPC system despite following the online guide. The user is trying to utilize tinyGPU with any GPU in an interactive session but encounters failures.

## Details
- **UserID**: iwfa025h
- **Environment**: Conda environment with PyTorch
- **PyTorch Version**: 2.0.1
- **Error**: GPU not detected in Jupyter notebook

## Root Cause
The issue seems to be related to the Jupyter notebook not using the correct Conda environment. The user's environment setup might be correct, but the Jupyter notebook is not utilizing the environment properly.

## Troubleshooting Steps
1. **Environment Setup**:
   - Create a new Conda environment:
     ```bash
     conda create -n torch-on-tg python=3.9
     conda activate torch-on-tg
     pip install torch torchvision torchaudio
     ```
   - Verify GPU access in the terminal:
     ```python
     import torch
     print(torch.__version__)
     print(torch.cuda.is_available())
     ```

2. **Jupyter Notebook Setup**:
   - Install Jupyter notebook in the Conda environment:
     ```bash
     pip install notebook
     ```
   - Start Jupyter notebook from the activated environment:
     ```bash
     jupyter notebook --ip $HOSTNAME --no-browser
     ```

3. **Register Conda Environment as Jupyter Kernel**:
   - Install `ipykernel`:
     ```bash
     conda install ipykernel
     ```
   - Register the environment as a Jupyter kernel:
     ```bash
     python3 -m ipykernel install --user --name=<environment_name>
     ```
   - In Jupyter notebook, change the kernel to the registered environment:
     ```
     Kernel -> Change Kernel -> <environment_name>
     ```

4. **Verify Torch Installation in Jupyter**:
   ```python
   import torch
   import os
   print(os.path.abspath(torch.__file__))
   ```

## Solution
The user needs to ensure that the Jupyter notebook is using the correct Conda environment. This can be achieved by either starting Jupyter from the activated environment or registering the environment as a Jupyter kernel.

## Additional Notes
- The user might have multiple versions of PyTorch installed, which could cause conflicts.
- Ensure that the environment is activated before starting Jupyter notebook.
- Verify the path of the PyTorch installation in the Jupyter notebook to ensure it matches the Conda environment.

## References
- [StackOverflow: How to retrieve a module's path](https://stackoverflow.com/questions/247770/how-to-retrieve-a-modules-path)
- [Helpdesk Ticket](https://www.helpdesk.rrze.fau.de/otrs/index.pl?Action=AgentTicketZoom;TicketID=1085967)

## Keywords
- GPU access
- PyTorch
- Conda environment
- Jupyter notebook
- HPC system
- tinyGPU
- interactive session
---

### 2022101442004421_Cannot%20remove%20pytorch%20from%20the%20cluster.md
# Ticket 2022101442004421

 # HPC Support Ticket: Cannot Remove PyTorch from the Cluster

## Keywords
- PyTorch
- Conda Environment
- ResolvePackageNotFound Error
- CUDA
- CPU-only PyTorch

## Problem Description
- User installed the wrong version of PyTorch (CPU-only) in a conda environment.
- Attempting to remove and reinstall PyTorch results in a `ResolvePackageNotFound: -python=3.1` error.
- The user followed the official PyTorch installation command but did not pre-load the CUDA and cuDNN modules.

## Root Cause
- Incorrect installation of PyTorch without pre-loading the necessary CUDA and cuDNN modules.
- Possible corruption or misconfiguration in the conda environment.

## Solution
1. **Remove the Conda Environment:**
   - Use the command: `conda env remove -n ENV_NAME`
   - If the above command does not work, manually delete the environment:
     - Remove the entry in `~/.conda/environments.txt`
     - Delete the corresponding folder in the conda environment directory (find the directory using `conda info`)

2. **Correct Installation Process for CUDA PyTorch:**
   - Pre-load the CUDA and cuDNN modules.
   - Use the correct installation command provided by PyTorch, ensuring it includes the CUDA toolkit version.

## General Learning
- Always pre-load necessary modules (e.g., CUDA, cuDNN) before installing packages that depend on them.
- If a conda environment becomes corrupted, it may be necessary to manually delete it.
- Use `conda info` to locate the conda environment directory for manual deletion if needed.

## Additional Notes
- This issue highlights the importance of following the correct installation steps for packages that depend on specific modules.
- Understanding how to manage and troubleshoot conda environments is crucial for resolving such issues.
---

### 2024030542003761_Installation%20Issue%20for%20InstantNGP%20Model%20on%20Cluster%20-%20iwi9013h.md
# Ticket 2024030542003761

 ```markdown
# Installation Issue for InstantNGP Model on Cluster

## Keywords
- InstantNGP
- Installation Issue
- Cluster
- GUI Dependencies
- Python Bindings
- Module System
- Conda
- Spack

## Problem
- User encountered installation issues while attempting to run the InstantNGP model on the cluster.
- Required packages for installation need sudo access.
- Dependency on `libxrandr-dev` indicates potential GUI application issues.

## Root Cause
- The InstantNGP model has dependencies on graphical libraries (e.g., `libxrandr-dev`), which are not suitable for cluster environments.
- Users do not have permissions to install system packages.

## Solution
- Build the model without GUI support using the flag `-DNGP_BUILD_WITH_GUI=false`.
- Use the module system to load necessary modules:
  ```sh
  $ module load python
  $ module load cuda cmake
  ```
- Build the model on the cluster frontend where development packages are available.
- If additional packages are required, use Conda or Spack to install them as a user.

## Additional Information
- The model has Python bindings that should work without the GUI.
- Development packages are generally only available at the cluster frontends.
- For further assistance, refer to the provided documentation links or contact HPC support.

## Documentation Links
- [Python Documentation](https://doc.nhr.fau.de/sdt/python/)
- [Module System Documentation](https://doc.nhr.fau.de/environment/modules/)
- [Conda Documentation](https://doc.nhr.fau.de/environment/python-env/)
- [Spack Documentation](https://doc.nhr.fau.de/apps/spack/)
```
---

### 2024120942002916_cuDSS%20on%20Cluster%20Alex.md
# Ticket 2024120942002916

 # HPC Support Ticket: cuDSS on Cluster Alex

## Keywords
- cuDSS
- Cluster Alex
- CUDA
- Spack
- Multi-GPU setups
- NCCL

## Problem Description
- User is part of the k107ce project and wants to use the cuDSS solver package on the Alex cluster.
- User could not find cuDSS as a module, via `spack list`, or in the CUDA installation path.
- User is unsure if cuDSS is installed or available via Spack.
- User is skeptical about installing cuDSS themselves, especially for multi-GPU setups with NCCL.

## Root Cause
- cuDSS is not currently installed on the cluster.

## Solution
- HPC Admin confirmed that cuDSS is not installed on the cluster.
- No further solution was provided in the ticket conversation.

## General Learnings
- Always check if the required software is available as a module or via Spack.
- If unsure about installation, consult with HPC Admins or the 2nd Level Support team.
- Multi-GPU setups may require additional configuration and expertise.

## Next Steps
- User could request the installation of cuDSS by the HPC Admins.
- User could attempt to install cuDSS themselves, following the installation guide and consulting with the 2nd Level Support team if needed.
- If cuDSS is successfully installed, it could be made available as a module or via Spack for future use.
---

### 2025031942002029_b232dd14%20%3A%20%27Detected%20kernel%20version%204.18.0%20is%20below%20the%20recommended%20minimum%.md
# Ticket 2025031942002029

 ```markdown
# HPC-Support Ticket: Detected Kernel Version 4.18.0 Below Recommended Minimum of 5.5.0

## Keywords
- Kernel version
- Hang process
- JupyterHub
- Conda environment
- CUDA
- DeepSpeed Triton
- NFS system
- Sentence Transformers

## Problem Description
The user is experiencing a hanging process when running model training on the FAU cluster. The issue is related to the kernel version being below the recommended minimum.

### User Setup
- **Hardware**: A40 / A100
- **Modules Loaded**:
  - cuda/12.4.1
  - gcc/11.2.0
  - openmpi/4.1.6-gcc11.2.0-cuda

### Error Message
```
Detected kernel version 4.18.0, which is below the recommended minimum of 5.5.0; this can cause the process to hang. It is recommended to upgrade the kernel to the minimum version or higher.
```

## Root Cause
The kernel version 4.18.0 is below the recommended minimum of 5.5.0 for the Sentence Transformers training process, which can cause the process to hang.

## HPC Admin Response
- Kernel upgrade to 5.5.0 is not possible from the HPC admin side.
- Suggested running the job in a batch job (`sbatch`) to determine if it truly hangs.
- Recommended using the LMU email address for HPC-Support communication.

## Additional Information
- The warning about the kernel version was introduced in [this commit](https://github.com/huggingface/accelerate/commit/b7686ccb4438b9aefb5f7990b80aa50b47a19463).
- The issue is related to shared memory support in older kernels, which is not accurate as shared memory support in the Linux kernel is over 20 years old.

## Solution
- Run the job in a batch job (`sbatch`) to confirm if the process hangs.
- If the issue persists, further investigation by AI experts is required as a kernel upgrade is not feasible.

## References
- [NVIDIA CUDA Installation Guide for Linux 12.4](https://docs.nvidia.com/cuda/archive/12.4.0/cuda-installation-guide-linux/index.html)
- [Sentence Transformers Issue](https://github.com/UKPLab/sentence-transformers/issues/2752)
```
---

### 2025022642003374_Jupyterhub%20_%20NHR%20Amber-Kurs.md
# Ticket 2025022642003374

 # HPC Support Ticket Conversation Summary

## Subject
Jupyterhub / NHR Amber-Kurs

## Keywords
- Jupyterhub
- NHR Amber Course
- Xfce Desktop
- Module Command
- VMD
- Amber
- Xmgrace
- GPU/Cuda
- Slurm
- Ubuntu 24.04

## General Learnings
- **Module Command Issue**: The `module` command was not found due to missing initialization. The solution was to run `eval `tclsh /apps/modules/modulecmd.tcl bash autoinit``.
- **VMD Issue**: VMD had issues with missing `csh` interpreter. This was resolved by updating the Xfce image to Ubuntu 24.04.
- **Amber Versions**: Amber 20 without CUDA was recommended for job preparation, while GPU jobs should be submitted via the job scheduler.
- **Slurm Commands**: Slurm commands were not available in the initial setup but were added in a different Jupyterhub instance.
- **Image Viewer**: Ristretto was installed as an image viewer.

## Root Causes and Solutions
- **Module Command Not Found**:
  - Root Cause: Missing initialization of the module command.
  - Solution: Run `eval `tclsh /apps/modules/modulecmd.tcl bash autoinit``.

- **VMD Interpreter Issue**:
  - Root Cause: Missing `csh` interpreter.
  - Solution: Update the Xfce image to Ubuntu 24.04.

- **Amber Version Recommendation**:
  - Root Cause: Confusion about which Amber version to use.
  - Solution: Use Amber 20 without CUDA for job preparation and submit GPU jobs via the job scheduler.

- **Slurm Commands Missing**:
  - Root Cause: Slurm commands were not included in the initial setup.
  - Solution: Use a different Jupyterhub instance where Slurm commands are available.

- **Image Viewer Request**:
  - Root Cause: Need for an image viewer.
  - Solution: Install Ristretto as an image viewer.

## Additional Notes
- The course is planned to be held after the MMWS.
- The support for Ubuntu 20.04 ends in April, and the system will be updated to Ubuntu 24.04.
- The Jupyterhub instance for the Computerchemie-Praktikum of Pharmazie was used as a reference for the setup.
---

### 2023021642002291_CUDA_PATH%20for%20cupy.md
# Ticket 2023021642002291

 # HPC Support Ticket: CUDA_PATH for cupy

## Keywords
- CUDA_PATH
- cupy
- sigpy
- ImportError
- Out of Memory
- GPU nodes
- Interactive jobs
- Conda environment
- pip install
- editable mode
- cudnn
- cuda
- rtx3080
- a100

## Problem Summary
- User encountered issues importing `cupy` and `sigpy` modules on different nodes.
- On a node without GPU (tinyx), an error occurred as expected.
- On a GPU node (rtx3080), a warning message was received, and no memory was allocated, resulting in an "out of memory" error.
- The same code ran successfully on the user's local machine with a weaker GPU.

## Root Cause
- The issue was related to installing `sigpy` in editable mode, which caused an `ImportError`.
- The memory allocation problem might be related to the specific GPU (rtx3080) or the installation process.

## Solution
- The HPC Admin provided a step-by-step installation process that worked successfully:
  ```bash
  salloc.tinygpu --gres=gpu:1 --time=00:30:00
  module load cudnn/8.0.5.39-cuda11.1 cuda/11.2.2 python
  export http_proxy=http://proxy:80
  export https_proxy=http://proxy:80
  conda create --name cupy python=3.8
  source activate cupy
  pip install cupy-cuda11x
  python -c 'import cupy as cp; x_gpu = cp.array([1, 2, 3])'
  ```
- The user confirmed that the code worked on a different GPU (a100), suggesting the issue might be specific to the rtx3080 GPU.

## Additional Notes
- The user was advised to install a missing library to resolve a warning:
  ```bash
  python -m cupyx.tools.install_library --library nccl --cuda 11.x
  ```
- The ticket was closed as the user was able to run the code on a different GPU.

## Lessons Learned
- Ensure that packages requiring GPU support are installed on nodes with available GPUs.
- Editable mode installations can cause unexpected issues; verify the installation process.
- Different GPUs may behave differently with the same code; test on multiple GPUs if possible.
- Provide detailed job scripts and error outputs to facilitate troubleshooting.
---

### 2024080542002271_Not%20working%20on%20CUDA.md
# Ticket 2024080542002271

 ```markdown
# HPC Support Ticket: Not Working on CUDA

## Keywords
- CUDA
- GPU
- Python
- TinyGPU
- SLURM
- Batch System
- Job Script

## Problem Description
- User attempted to run a Python script on TinyGPU node to train a Torch model.
- Script checks for available CUDA devices but finds none.
- User followed example from documentation but encountered issues.

## Root Cause
- User did not submit the script to the batch system correctly.
- User attempted to run the script directly instead of submitting it as a job.

## Solution
- Create a job script file with the necessary commands.
- Make the script executable using `chmod +x <filename>`.
- Submit the script to the batch system using `sbatch.tinygpu ./filename`.

## References
- [Batch System SLURM](https://doc.nhr.fau.de/batch-processing/batch_system_slurm/)
- [Advanced Topics SLURM](https://doc.nhr.fau.de/batch-processing/advanced-topics-slurm/)
- [Job Script Examples SLURM](https://doc.nhr.fau.de/batch-processing/job-script-examples-slurm/)

## General Learning
- Always submit jobs to the batch system instead of running them directly on the login node.
- Ensure scripts are executable before submitting them to the batch system.
- Refer to documentation for job script examples and advanced topics for SLURM.
```
---

### 2023111642003129_Abst%C3%83%C2%BCrze%20LM-Finetuning%20-%20p102eb10.md
# Ticket 2023111642003129

 # HPC-Support Ticket: Abstürze LM-Finetuning - p102eb10

## Keywords
- GPU Job
- Fine-tuning
- Language Model
- CUDA Error
- Invalid Device Ordinal
- SRUN_ARGS
- SLURM_JOBID

## Problem Description
The user is experiencing crashes when trying to fine-tune a 7B-parameter language model on 4 or 8 GPUs. The error message indicates a CUDA error related to an invalid device ordinal. The user has tried different CUDA versions and installation methods but the issue persists.

## Root Cause
The root cause of the problem is likely related to the SRUN_ARGS in the job script. Specifically, the use of `--overlap` and `--jobid="$SLURM_JOBID"` may be causing issues with GPU allocation.

## Solution
The HPC Admin suggested that the `--overlap` argument in SRUN_ARGS might be unnecessary and that `--jobid="$SLURM_JOBID"` is automatically handled by SLURM. Removing these arguments from the job script resolved the issue.

## General Learnings
- Ensure that SRUN_ARGS are necessary and correctly configured.
- SLURM automatically handles `--jobid="$SLURM_JOBID"`, so it is usually not necessary to include it in the job script.
- CUDA errors related to invalid device ordinals can often be traced back to incorrect GPU allocation or configuration in the job script.

## Additional Notes
- The user also received a warning about the kernel version being below the recommended minimum, but this was not the primary cause of the issue.
- The problem was ultimately resolved by removing unnecessary arguments from the job script.
---

### 2024112742004981_conda%20env%20problem.md
# Ticket 2024112742004981

 # HPC-Support Ticket: Conda Environment Configuration Issue

## Keywords
- Conda
- Virtual Environment
- GPU
- CUDA Toolkit
- JupyterHub
- TinyFat Profile
- TinyGPU Profile

## Problem Description
- User attempted to install CUDA Toolkit using Conda but encountered errors.
- The error report was attached to the email.

## Root Cause
- The user was using a TinyFat profile on JupyterHub, which does not have GPU support.
- Libraries/packages required for the CUDA Toolkit installation were missing due to the lack of GPU.

## Solution
- Select a profile with GPU support, such as "1x GPU, 4 hours".
- Use the TinyGPU cluster, which has the necessary GPU resources.

## General Learnings
- Ensure the selected JupyterHub profile matches the requirements of the software being installed.
- GPU-dependent libraries and packages require a profile with GPU support.
- The TinyGPU cluster is designated for GPU-intensive tasks.

## Next Steps for Support
- Verify the user's profile selection.
- Assist the user in switching to a GPU-enabled profile if necessary.
- Provide guidance on installing the CUDA Toolkit in the correct environment.
---

### 2024041142001179_gamdplus%20jobs%20on%20Alex%20%5Bb118bb12%20%5D.md
# Ticket 2024041142001179

 ```markdown
# HPC Support Ticket Analysis: gamdplus jobs on Alex [b118bb12 ] [Ticket#2024041142001179]

## Summary
The user, Luis Vollmers, encountered issues with low GPU utilization for their PyTorch-based jobs on the Alex cluster. The main components involved were PyTorch, DGL, and Torchvision. The user faced various errors related to CUDA configurations and library mismatches.

## Key Issues
1. **Low GPU Utilization**: The user's jobs showed minimal GPU usage compared to other PyTorch jobs.
2. **Library Mismatches**: Errors related to mismatched CUDA versions between PyTorch and Torchvision.
3. **DGL Installation Issues**: Errors related to missing DGL C++ sparse libraries.

## Solutions Provided
1. **Environment Setup**:
   - The user was guided to set up a new environment using micromamba and ensure proper configuration.
   - Instructions were provided to delete old environments and reinstall necessary packages.

2. **CUDA Configuration**:
   - The user was advised to check CUDA availability using `python3 -c 'import torch; print(torch.cuda.is_available())'`.
   - The user was instructed to ensure that PyTorch and Torchvision were compiled with the same CUDA version.

3. **DGL Installation**:
   - The user was advised to install a newer version of DGL compatible with their PyTorch version.
   - Specific links and commands were provided for installing the correct DGL version.

## Additional Steps
- The user was asked to provide a minimal example for further testing.
- A Zoom meeting was scheduled to discuss the issues in detail.
- The user was advised to run a more significant job to check if the low GPU utilization was due to the minimal example.

## Conclusion
The ticket was closed after extensive troubleshooting and guidance. The user was able to set up a functional environment and run jobs without errors, but the GPU utilization issue persisted. Further investigation with a more significant job was recommended.
```
---

### 2023031042000014_Probleme%20mit%20dem%20Import%20von%20tensorflow%20-%20iwfa017h.md
# Ticket 2023031042000014

 ```markdown
# HPC Support Ticket: Probleme mit dem Import von tensorflow

## Keywords
- TensorFlow
- Import Error
- Kernel Restart
- TinyGPU Server

## Problem Description
- User encountered issues with importing TensorFlow in their notebook.
- Notebook stopped functioning after attempting to import TensorFlow.

## Root Cause
- The user did not specify the exact error message, but it was related to TensorFlow import.

## Troubleshooting Steps
1. **Kernel Restart**: HPC Admin suggested restarting the kernel to see if TensorFlow could be imported normally.
2. **System and Installation Details**: HPC Admin requested information about the system and TensorFlow installation being used.
3. **Terminal Test**: HPC Admin provided a Python command to test TensorFlow import and GPU device listing in the terminal.

## Solution
- The user resolved the issue by using the TinyGPU Server.

## Lessons Learned
- Always check if the issue can be resolved by using a different server or environment.
- Gathering detailed information about the system and installation can help in diagnosing the problem.
- Providing specific commands to test functionality can assist in troubleshooting.

## Closure
- The ticket was closed after the user confirmed that the issue was resolved by using the TinyGPU Server.
```
---

### 2024041842004832_Keine%20Grafikkarten%20unter%20Tensorflow%20erkannt.md
# Ticket 2024041842004832

 ```markdown
# HPC Support Ticket: TensorFlow GPU Not Recognized

## Subject
Keine Grafikkarten unter Tensorflow erkannt

## User Issue
- User is unable to get TensorFlow to recognize GPUs on the tinygpu cluster.
- After installing TensorFlow and the corresponding CUDA version, running the command to list physical devices returns an empty list.
- The user receives a warning: `TF-TRT Warning: Could not find TensorRT`.
- Attempts to load the TensorRT module fail with an error: `Unable to locate a modulefile for 'tensorrt/8.5.3.1-cuda11.8-cudnn8.6'`.

## HPC Admin Response
- Frontend nodes do not have GPUs; installation of Python packages should be done on a compute node via an interactive job (`salloc`) or by submitting a job script using `sbatch`.
- Suggested creating conda environments and provided instructions on the documentation page: [Python Environments](https://doc.nhr.fau.de/environment/python-env/).

## Keywords
- TensorFlow
- GPU
- CUDA
- TensorRT
- Module
- Conda Environment
- Compute Node
- Interactive Job
- Job Script

## What Can Be Learned
- Ensure that GPU-related installations and tests are performed on compute nodes, not frontend nodes.
- Use interactive jobs or job scripts to perform installations and tests on compute nodes.
- Consider using conda environments for managing Python packages and dependencies.
- Verify the availability of required modules (e.g., TensorRT) and ensure they are correctly loaded.

## Solution
- Perform TensorFlow and CUDA installations on a compute node.
- Use conda environments for managing Python packages.
- Ensure that the required modules are available and correctly loaded on the compute node.
```
---

### 2022112442003302_issue%20with%20python%20code%20on%20tinygpu%20%5Biwi5091h%5D.md
# Ticket 2022112442003302

 ```markdown
# HPC Support Ticket Conversation Summary

## Issue
The user, Soham Basu, was experiencing issues with running a Python model on the TinyGPU cluster. The main problems were related to CUDA memory errors and kernel image not found errors when using different GPU generations.

## Key Points Learned
1. **Conda Environment Issues**:
   - The user had trouble activating the Conda environment and faced "commandnotfound" errors.
   - The solution involved reloading modules before activating the Conda environment and rebuilding the Conda environment on the target hardware.

2. **Batch Processing**:
   - The user faced "CUDA out of memory" errors when using certain GPUs and "CUDA kernel image not found" errors with others.
   - The HPC Admins suggested splitting the job into smaller parts and ensuring the correct modules were loaded.

3. **Proxy Configuration**:
   - The user encountered HTTP errors when trying to install packages due to proxy settings.
   - The solution involved setting the correct proxy environment variables.

4. **Documentation**:
   - The HPC Admins provided links to relevant documentation for TinyGPU basics, SLURM basics, and installing Python on TinyGPU.
   - The user was advised to read these documents to better understand the system and resolve issues.

## Solutions
1. **Conda Environment**:
   - Ensure the Conda environment is properly configured and activated.
   - Use the following commands to load modules and activate the environment:
     ```bash
     module load python/3.8-anaconda cuda/11.6.1
     source activate <env>
     ```

2. **Batch Processing**:
   - Split the job into smaller parts if necessary.
   - Ensure the correct modules are loaded before running the job.

3. **Proxy Configuration**:
   - Set the proxy environment variables correctly:
     ```bash
     export http_proxy=http://proxy:80
     export https_proxy=http://proxy:80
     ```

4. **Documentation**:
   - Refer to the provided documentation links for detailed instructions and troubleshooting steps.

## Conclusion
The user's issues were resolved through a combination of reconfiguring the Conda environment, adjusting batch processing settings, and setting the correct proxy configuration. The HPC Admins provided detailed instructions and documentation links to help the user understand and resolve the problems.
```
---

### 2024111042000641_Tinyx%20returnns%20false%20for%20available%20GPUs.md
# Ticket 2024111042000641

 ```markdown
# HPC Support Ticket: Tinyx returns false for available GPUs

## Keywords
- PyTorch
- CUDA
- GPU
- Virtual Environment
- Interactive Job
- Compute Node

## Summary
A user encountered an issue where PyTorch did not detect available GPUs on the TinyGPU cluster. The user followed a series of steps to install and verify PyTorch but encountered a problem where `torch.cuda.is_available()` returned `False`.

## Root Cause
The primary issue was that the user did not request an interactive job on a compute node with GPUs. Additionally, the user did not load the CUDA module before attempting to use CUDA with PyTorch.

## Steps Taken by the User
1. SSH into `tinyx.nhr.fau.de`.
2. Loaded the Python 3.10 module.
3. Created and activated a virtual environment.
4. Installed PyTorch for CUDA 12.1 using pip.
5. Verified GPU availability using `torch.cuda.is_available()`, which returned `False`.

## Solution
1. **Load the CUDA Module**: Before using CUDA with PyTorch, ensure that the CUDA module is loaded.
2. **Request an Interactive Job**: Ensure that you are running your commands on a compute node with GPUs by requesting an interactive job.

## Documentation Reference
- [PyTorch Documentation](https://doc.nhr.fau.de/apps/pytorch/)
- [Interactive Job on TinyGPU](https://doc.nhr.fau.de/clusters/tinygpu/#interactive-jobs)

## General Learning
- Always ensure that you are running GPU-dependent tasks on a compute node with GPUs.
- Load necessary modules (e.g., CUDA) before attempting to use them.
- Follow the documentation guidelines for installing and verifying packages on the target cluster.
```
---

### 2024110842002563_Dask-cudf%20installation.md
# Ticket 2024110842002563

 # HPC Support Ticket: Dask-cudf Installation Issue

## Keywords
- Dask-cudf installation
- CUDA version mismatch
- Compute node internet access
- Environment variables

## Problem
- User encountered an error while installing `dask-cudf` and `cudf-cu12` packages.
- The error indicated that the CUDA version was reported as 12.6, despite the user loading CUDA 12.5.1 via `module load`.
- The installation failed due to the inability to reach `https://pypi.nvidia.com` from the compute node.

## Root Cause
- Compute nodes do not have internet access by default, preventing the download of the required packages from `https://pypi.nvidia.com`.
- The CUDA version mismatch was likely due to the environment not correctly reflecting the loaded modules.

## Solution
- Set the environment variables as indicated in the FAQ link provided by the HPC Admin to enable internet access on the compute node.
- This allowed the installation to proceed successfully.

## Steps Taken
1. User loaded the necessary modules and created a new Conda environment.
2. User attempted to install `dask-cudf` and `cudf-cu12` packages using `pip`.
3. User encountered an error due to the lack of internet access on the compute node.
4. HPC Admin provided a solution to set environment variables for internet access.
5. User followed the instructions and successfully installed the packages.

## Lessons Learned
- Compute nodes in HPC environments often have restricted internet access.
- Setting specific environment variables can enable internet access for package installations.
- Ensure that the loaded modules correctly reflect the desired software versions.

## References
- [FAQ: Why does my application give an HTTP/HTTPS timeout?](https://doc.nhr.fau.de/faq/#why-does-my-application-give-an-http-https-timeout)
---

### 2023101742004459_Issues%20regarding%20tsfresh%20package.md
# Ticket 2023101742004459

 # HPC Support Ticket: Issues Regarding tsfresh Package

## Keywords
- tsfresh
- Numba
- CUDA Toolkit
- Conda environment
- Nvidia A100
- Slurm

## Problem Description
- User encountered an error when trying to use the `tsfresh` library.
- Error message: `numba.cuda.cudadrv.error.NvvmSupportError: No supported GPU compute capabilities found. Please check your cudatoolkit version matches your CUDA version.`
- Additional Slurm output file attached.

## Root Cause
- Mismatch between CUDA Toolkit version and Numba requirements.
- User's Conda environment contained old and mixed versions of dependencies.

## Solution
- Ensure CUDA Toolkit version matches the required version for Numba (minimum 11.2).
- Follow the documentation to set up a new Conda environment with compatible versions.

## Steps Taken
1. **HPC Admin**: Asked the user how the Conda environment was built and pointed out the version mismatch.
2. **User**: Provided steps taken to set up the Conda environment and agreed to create a new environment following the documentation.
3. **HPC Admin**: Confirmed the need for newer versions and provided documentation links for reference.

## Documentation Links
- [TensorFlow and PyTorch Documentation](https://hpc.fau.de/systems-services/documentation-instructions/special-applications-and-tips-tricks/tensorflow-pytorch/)
- [Python and Jupyter Documentation](https://hpc.fau.de/systems-services/documentation-instructions/special-applications-and-tips-tricks/python-and-jupyter/)

## Conclusion
- The issue was likely due to outdated and mixed versions in the Conda environment.
- Creating a new environment with compatible versions should resolve the problem.

## Follow-up
- User will set up a new Conda environment and report back if issues persist.
---

### 2024071542001997_Unmatched%20python%20and%20cuda_cudnn%20version%20-%20iwso064h.md
# Ticket 2024071542001997

 # HPC-Support Ticket Conversation Summary

## Keywords
- Python DL job
- TensorFlow
- Keras
- CUDA
- cuDNN
- GPU memory
- OOM (Out of Memory)

## Problem
- User needs specific versions of CUDA and cuDNN for TensorFlow GPU support.
- Initial cuDNN module is incompatible, causing errors.
- After resolving compatibility issues, the job is killed by OOM errors.

## Root Cause
- Incompatible cuDNN version leading to library loading errors.
- Insufficient GPU memory for the job.

## Solution
- HPC Admins added new cuDNN modules (`cudnn/8.9.7.29-11.x`, `cudnn/8.9.7.29-12.x`, `cudnn/9.2.1.18-12.x`) to resolve compatibility issues.
- General suggestions for OOM errors:
  - Allocate time on a larger GPU.
  - Optimize code to consume less memory.
  - Reduce batch size in ML training.
  - Use a smaller model.
  - Decrease batch size/microbatch size.
  - Use smaller training samples.
  - Request a bigger GPU.
  - Shard the model across GPUs.

## General Learnings
- Ensure compatibility of CUDA and cuDNN versions with TensorFlow.
- Address OOM errors by optimizing resource usage or requesting more resources.
- HPC Admins can provide new modules but may need specific job details to offer targeted advice.

## Next Steps
- User to share training parameters for further assistance.
- Continue monitoring job performance and adjust resources as needed.
---

### 2023071742003279_JupyterHub%20f%C3%83%C2%BCr%20GPU%20Kurse.md
# Ticket 2023071742003279

 # HPC Support Ticket: JupyterHub for GPU Courses

## Keywords
- JupyterHub
- GPU Courses
- NVHPC Toolkit
- CUDA
- MPI
- Internet Access
- Module Loading
- Account Requirements

## Summary
The user tested JupyterHub instances for GPU courses and found them suitable for introductory courses. They proposed testing the setup during an upcoming CUDA C++ course. The user also reported issues with NVHPC Toolkit configuration, MPI setup, and internet access within Jupyter instances.

## Issues and Solutions

### NVHPC Toolkit Configuration
- **Issue**: NVHPC Toolkit on A40/A100 nodes was configured with the wrong CUDA version (10.2), preventing compilation for A40/A100 GPUs which require CUDA 11 or higher.
- **Solution**: Update the NVHPC Toolkit to version 23.5, which correctly configures CUDA 12.1 on both A40 nodes and the login node.

### MPI Setup
- **Issue**: MPI setup was reported as tricky, with `openmpi/4.0.5-gcc9.3.0-cuda-legacy` working but requiring the `--oversubscribe` switch.
- **Solution**: No consensus was reached on the best MPI module from previous tests. Further testing and feedback are needed.

### Internet Access
- **Issue**: The user reported internet access within Jupyter instances, which was unexpected as the compute nodes do not perform NAT.
- **Solution**: The HPC Admin clarified that internet access is not available, but proxy variables can be pre-set. The user's instance might have had a proxy configured by default.

### Account Requirements
- **Issue**: The user requested specific account requirements for the CUDA C++ course.
- **Solution**: The HPC Admin provided a list of JWT links for the required accounts, valid for the course duration, and reserved the necessary GPUs.

## Workflow
- The HPC Admin will create a list of links for each participant, which the user will distribute via email.
- The links will be valid for the course duration and will automatically use the reserved GPUs.

## Additional Notes
- The user mentioned that multi-GPU performance on 1080 cards was not good, as expected.
- `nvshmem` did not work out-of-the-box and might need to be built manually.
- The user's account had access to Alex nodes, which was approved by Harald Lanig.

This documentation can be used to address similar issues in the future, ensuring consistent and efficient support for GPU courses using JupyterHub.
---

### 2022051642003428_medusa%20GPU_Cuda%20error.md
# Ticket 2022051642003428

 # HPC-Support Ticket: medusa GPU/Cuda Error

## Subject
medusa GPU/Cuda error

## Keywords
- CUDA
- GPU
- NVIDIA driver
- Driver/library version mismatch
- NVML
- Reboot
- Module load
- Permission error

## Problem Description
- User encountered `cudaErrorUnknown` (error code 30) when running `cudaGetDeviceCount()` from C++ on medusa.
- CUDA devices could not be set, preventing code execution on GPUs.
- Issue was not present on milan1 and had previously worked on medusa.
- User suspected a reboot might fix the issue.

## Root Cause
- Ubuntu autoupdates installed an update of the NVIDIA driver, causing a driver/library version mismatch.
- `nvidia-smi` command failed with the error "Failed to initialize NVML: Driver/library version mismatch."

## Solution
- HPC Admin rebooted medusa, which resolved the issue.
- User confirmed that the problem was fixed after the reboot.

## Additional Issues
- User encountered a similar error on milan1 with `nvidia-smi` failing due to a driver/library version mismatch.
- CUDA modules could not be loaded on milan1, with an error message indicating that CUDA is only supported on specific machines.
- User reported permission error when using `ncu` on milan1.

## Further Actions
- HPC Admin manually updated and rebooted milan1, resolving the `nvidia-smi` issue.
- HPC Admin created a pseudo-module for CUDA on the test cluster to allow `module load cuda` to function.
- HPC Admin noted discrepancies in CUDA module paths and versions between medusa and milan1, suggesting a need for a better solution.

## Lessons Learned
- Regular updates and reboots can resolve driver/library version mismatches.
- Ensuring consistent CUDA module paths and versions across systems is crucial for smooth operation.
- Permission errors with `ncu` may require specific user permissions or configurations.

## Open Issues
- Resolving CUDA module path and version discrepancies between medusa and milan1.
- Addressing permission errors with `ncu` on milan1.

## Next Steps
- Investigate and implement a better solution for managing CUDA modules and paths.
- Address permission issues for `ncu` on milan1.
- Monitor for similar issues after future updates and reboots.
---

### 2023080342003212_Cluster%20Cuda%20%2B%20Python%20Probleme.md
# Ticket 2023080342003212

 # HPC Support Ticket: Cluster Cuda + Python Probleme

## Keywords
- CUDA
- CMake
- Python Development
- Anaconda
- TinyGPU Cluster

## Problem Description
- **CUDA Compiler Not Found**: `CMAKE_CUDA_COMPILER` not found despite loading CUDA module.
- **CUDA Library Not Found**: `CUDA_CUDA_LIBRARY` not found when `CMAKE_CUDA_COMPILER` is set manually.
- **Python Development**: `PYTHON3_INCLUDE_DIRS` not found for development.

## Root Cause
- **CUDA Compiler**: The CUDA module does not set the CMake environment variables automatically.
- **CUDA Library**: The CMakeLists.txt file enforces CUDA 11.3, causing issues with other versions.
- **Python Development**: CMake is not recognizing the Anaconda Python module, only the system Python.

## Solution
- **CUDA Compiler**: Users need to manually set the CMake environment variables.
- **CUDA Library**: Modify the CMakeLists.txt file to accept the desired CUDA version (e.g., 11.8).
- **Python Development**: Use specific CMake flags to point to the Anaconda Python module:
  ```sh
  cmake .. \
  -DPYTHON_INCLUDE_DIR=$(python -c "import sysconfig; print(sysconfig.get_path('include'))") \
  -DPYTHON_LIBRARY=$(python -c "import sysconfig; print(sysconfig.get_config_var('LIBDIR'))") \
  -DPYTHON_EXECUTABLE:FILEPATH=`which python`
  ```

## General Learnings
- **Module Loading**: Modules do not always set environment variables automatically; manual configuration may be required.
- **CMake Configuration**: Ensure that CMakeLists.txt files are compatible with the available software versions.
- **Python Development**: Use specific CMake flags to correctly configure the build environment for Python development.

## Next Steps
- **User**: Implement the suggested changes and re-run the build process.
- **HPC Admins**: Monitor for similar issues and consider updating documentation to include these solutions.

## References
- **CMake Documentation**: For detailed information on configuring CMake.
- **Anaconda Documentation**: For information on setting up Python development environments.
---

### 2024020642003298_Issue%20in%20%22Torch%22%20module%20in%20HPC%20CLUSTER.md
# Ticket 2024020642003298

 # HPC Support Ticket: Issue with "Torch" Module in HPC Cluster

## Keywords
- CUDA
- PyTorch
- Environment
- GPU
- ModuleNotFoundError
- Interactive Job

## Problem Description
- User created an environment and loaded the `python/pytorch-1.13py3.10` module.
- CUDA was not enabled (`torch.cuda.is_available()` returned `False`).
- User encountered `ModuleNotFoundError: No module named 'torch'` when running a bash script, but the Python script worked.

## Root Cause
- The environment was created on the frontend, which does not have a GPU.
- The `python/pytorch-1.13py3.10` module is a wrapped conda environment and does not work reliably if another environment is loaded.

## Solution
- Unload any existing environment and use only the `python/pytorch-1.13py3.10` module.
- Create the environment and perform all steps inside an interactive job on a GPU node.
- Refer to the FAQ for getting an interactive job: [Why is my code not running on the GPU in tinygpu?](https://hpc.fau.de/faqs/#why-is-my-code-not-running-on-the-gpu-in-tinygpu)

## Additional Notes
- Ensure that the environment is set up correctly on a node with GPU support.
- Verify that CUDA is enabled by running `torch.cuda.is_available()` on the GPU node.

## Lessons Learned
- Always create and test environments on nodes with the required hardware (e.g., GPUs).
- Avoid loading multiple environments simultaneously, especially when using wrapped conda environments.
- Use interactive jobs for setting up and testing environments that require specific hardware.
---

### 2023032242001091_Import%20von%20torch%20nicht%20m%C3%83%C2%B6glich.md
# Ticket 2023032242001091

 ```markdown
# HPC-Support Ticket Conversation Summary

## Problem Description
The user, Jonas Winter, is experiencing issues with importing the `torch` module in a Python script running on the HPC cluster. The script works fine on the frontend but fails when submitted as a job, resulting in the error: `No module named torch`.

## Troubleshooting Steps

1. **Initial Diagnosis**:
   - The user confirmed that the `torch` module is correctly installed and works in the frontend Python console.
   - The job script was reviewed and found to be correctly loading the necessary modules and activating the Conda environment.

2. **Additional Diagnostics**:
   - The user was asked to add diagnostic commands to the job script to list the Conda environments, Conda packages, and pip packages.
   - The output showed that the `torch` package was not listed in the `pip freeze` output on the compute node, despite being listed in the frontend.

3. **Potential Causes**:
   - It was suspected that there might be an issue with the Python path or environment variables not being correctly set in the job environment.
   - The user was advised to check the Python path using `import sys; for line in sys.path: print(line)` to compare the paths between the frontend and the compute node.

4. **Recommendations**:
   - The user was advised to create a new Conda environment in an interactive job on the `tinygpu` node to ensure a clean environment.
   - The user was also advised to rename the `.local` directory to test if other installed packages were causing conflicts.

5. **Documentation and Further Assistance**:
   - The user was provided with a link to the documentation for installing TensorFlow and PyTorch, but the link was not accessible.
   - The user was advised to follow the general guidelines for setting up virtual environments and managing packages within Conda environments.

## Resolution
The issue was eventually resolved by creating a new Conda environment in an interactive job on the `tinygpu` node and ensuring that all necessary packages were installed within this new environment. The user also renamed the `.local` directory to avoid conflicts with previously installed packages.

## Conclusion
The problem was caused by a mismatch in the Python path and environment variables between the frontend and the compute node. Creating a new Conda environment and ensuring all packages were installed within this environment resolved the issue. The user was also advised to manage the `.local` directory to avoid conflicts with other installed packages.
```
---

### 2021121642002542_RuntimeError%3A%20CUDA%20error%3A%20out%20of%20memory.md
# Ticket 2021121642002542

 ```markdown
# HPC Support Ticket: RuntimeError: CUDA error: out of memory

## Summary
- **Error**: RuntimeError: CUDA error: out of memory
- **Environment**:
  - `salloc.tinygpu --gres=gpu:rtx3080:1 --time=03:00:00`
  - `module load python/3.8-anaconda cuda/11.1.0`
  - `export http_proxy=http://proxy:80`
  - `export https_proxy=http://proxy:80`
  - `source activate python3.7`

## Key Points
- The user encountered a CUDA out of memory error during network training.
- The error can come from various sources, and the stack trace might be incorrect due to asynchronous reporting.
- The user was advised to set `CUDA_LAUNCH_BLOCKING=1` for debugging.

## Actions Taken
- HPC Admin requested the output file of the batch job that triggered the issue.
- A Zoom meeting was scheduled to discuss the issue in detail.

## Root Cause
- The root cause of the problem was not explicitly identified in the conversation.

## Solution
- No specific solution was provided in the conversation. The user was advised to share the output file and a meeting was scheduled for further investigation.

## Keywords
- CUDA out of memory
- RuntimeError
- CUDA_LAUNCH_BLOCKING
- salloc.tinygpu
- python/3.8-anaconda
- cuda/11.1.0
- batch job output
- Zoom meeting

## General Learnings
- CUDA out of memory errors can be complex and require detailed investigation.
- Setting `CUDA_LAUNCH_BLOCKING=1` can help in debugging asynchronous CUDA kernel errors.
- Interactive sessions and meetings can be useful for resolving complex issues.
```
---

### 2022041342002678_conda%20install%20pytorch.md
# Ticket 2022041342002678

 # HPC Support Ticket: Conda Install PyTorch

## Keywords
- Conda
- PyTorch
- CUDA
- GPU
- SLURM
- Module System

## Problem
- User needs to install PyTorch with a specific CUDA version (10.2 or 11.3) using Conda.
- The allocated GPU has CUDA version 11.6, which is not compatible with the required PyTorch versions.
- User attempts to load CUDA modules on the head node, which is not a GPU node.

## Root Cause
- The user is trying to load CUDA modules on a non-GPU node.
- The available CUDA versions on the GPU nodes do not match the versions required by PyTorch.

## Solution
- Load CUDA modules within the interactive GPU session, not on the head node.
- Use Conda to install PyTorch and its dependencies, which should not rely on the system's CUDA modules.
- Ensure that the Conda environment is activated and properly configured to use the installed CUDA toolkit.

## Steps Taken
1. **User**: Requests help with specifying CUDA version for GPU allocation.
2. **HPC Admin**: Explains how to load different CUDA versions using the module system within the GPU node.
3. **User**: Attempts to load CUDA module on the head node, which fails.
4. **HPC Admin**: Clarifies that CUDA modules should be loaded within the interactive GPU session.
5. **User**: Installs PyTorch using Conda but encounters an error indicating that Torch is not compiled with CUDA enabled.
6. **HPC Admin**: Suggests that installing CUDA 11.3 via Conda should resolve the issue, as Conda handles dependencies independently of the system's modules.

## Conclusion
- Ensure that CUDA modules are loaded within the interactive GPU session.
- Use Conda to manage PyTorch and its dependencies, including the required CUDA toolkit.
- Avoid mixing Conda environments with system modules to prevent conflicts.
---

### 2023080442002355_GPU-Speicherprobleme%20beim%20Trainieren%20von%20Tensorflow%20Modellen.md
# Ticket 2023080442002355

 # HPC-Support Ticket: GPU-Speicherprobleme beim Trainieren von TensorFlow Modellen

## Problem
- **Fehlermeldung:** TensorFlow versucht, 37.25 GiB auf der GPU zu allokieren, was fehlschlägt.
- **Ursache:** Möglicherweise wird der Speicher nach dem Training nicht korrekt freigegeben.
- **Kontext:** Das Problem tritt nach dem Aufruf von `model.fit()` beim Aufruf von `model.eval()` auf.

## Diskussion
- **User:** Vermutet, dass TensorFlow den Speicher nach dem Training nicht richtig freigibt.
- **HPC Admin:** Unsicher, ob das verlinkte GitHub Issue relevant ist. Vorschlag, den Lösungsversuch des Users zu testen.

## Lösungsversuche
- **User:** Reduzierte die `batch_size` von 64 auf 32, was das Problem nicht löste.
- **User:** Plante, die `tf.Session` nach dem Training zu schließen und das restliche Programm in einer neuen Session laufen zu lassen.
- **User:** Bemerkte, dass der Evaluationsdatensatz nicht in einem Custom BatchGenerator gewrapped war, was möglicherweise das Problem verursachte.

## Lösung
- **User:** Wird den Evaluationsdatensatz in den Custom BatchGenerator wrappen und testen, ob dies das Problem löst.

## Schlussfolgerung
- **HPC Admin:** Die Kundenanfrage wird geschlossen.

## Keywords
- TensorFlow
- GPU-Speicherprobleme
- model.fit()
- model.eval()
- Speicherfreigabe
- Custom BatchGenerator
- tf.Session

## Allgemeine Erkenntnisse
- Überprüfen Sie, ob alle Datensätze korrekt in BatchGeneratoren gewrapped sind.
- Testen Sie, ob das Schließen und Neueröffnen von `tf.Session` das Speicherproblem löst.
- Reduzieren Sie die `batch_size`, wenn Speicherprobleme auftreten.
---

### 2022092942003898_Cuda%2010.0%20auf%20Tinyx.md
# Ticket 2022092942003898

 # HPC-Support Ticket: Cuda 10.0 auf Tinyx

## Subject
Cuda 10.0 auf Tinyx

## User Issue
The user is attempting to train a Mask RCNN model on a 2080Ti GPU using TensorFlow 1.15, which requires CUDA 10.0. The user's environment is unable to find the necessary CUDA runtime libraries, resulting in errors indicating missing `libcudart.so.10.0` and other related libraries.

## Keywords
- CUDA 10.0
- TensorFlow 1.15
- Mask RCNN
- 2080Ti GPU
- Missing CUDA libraries

## Root Cause
The root cause of the problem is the absence of CUDA 10.0 runtime libraries in the user's environment. TensorFlow 1.15 requires specific CUDA libraries that are not present, leading to errors during the execution of the training script.

## Solution
To resolve the issue, the user needs to ensure that the required CUDA 10.0 libraries are installed and accessible in their environment. This can be achieved by:
1. Installing CUDA 10.0 on the cluster.
2. Setting the `LD_LIBRARY_PATH` environment variable to include the directory containing the CUDA 10.0 libraries.

## Steps Taken
1. **Identify Missing Libraries**: The error messages indicate that several CUDA libraries are missing, including `libcudart.so.10.0`, `libcublas.so.10.0`, `libcufft.so.10.0`, `libcurand.so.10.0`, `libcusolver.so.10.0`, `libcusparse.so.10.0`, and `libcudnn.so.7`.
2. **Install CUDA 10.0**: Ensure that CUDA 10.0 is installed on the cluster.
3. **Update Environment Variables**: Set the `LD_LIBRARY_PATH` to include the path to the CUDA 10.0 libraries.

## Example Commands
```bash
# Install CUDA 10.0 (if not already installed)
module load cuda/10.0

# Set LD_LIBRARY_PATH
export LD_LIBRARY_PATH=/path/to/cuda-10.0/lib64:$LD_LIBRARY_PATH
```

## Additional Information
- The user provided a list of installed packages and their versions, which can be useful for troubleshooting compatibility issues.
- The user's Python environment is using Python 3.6.9.

## Conclusion
By ensuring that the required CUDA 10.0 libraries are installed and properly configured in the environment, the user should be able to train their Mask RCNN model on the 2080Ti GPU without encountering the missing library errors.
---

### 2024061042003139_Kein%20GPU-Zugriff%20auf%20Grace%20Hopper%20Node%20%28Testcluster%29.md
# Ticket 2024061042003139

 ```markdown
# HPC Support Ticket: No GPU Access on Grace Hopper Node (Test Cluster)

## Keywords
- GPU Access
- CUDA
- nvidia-smi
- cudaGetDeviceCount
- cudaErrorNoDevice
- Treiber-Mismatch
- Out-of-memory Meldungen
- Reboot

## Problem Description
- User reported no GPU access on Grace Hopper Node in the test cluster.
- `nvidia-smi` showed the GPU, but `cudaGetDeviceCount` returned `cudaErrorNoDevice`.

## Root Cause
- Possible Treiber-Mismatch or out-of-memory issues with the NVIDIA driver.

## Troubleshooting Steps
1. **Initial Check**: HPC Admin confirmed CUDA should work and performance monitoring required activation.
2. **Driver Issue**: HPC Admin suspected a Treiber-Mismatch.
3. **Log Analysis**: Logs indicated out-of-memory errors with the NVIDIA driver.
4. **Reboot**: The machine was rebooted to resolve the issue.

## Solution
- Rebooting the machine resolved the issue temporarily.
- Further monitoring is required to determine if the problem is triggered by specific jobs or other users.

## Follow-Up
- User confirmed successful GPU access after the reboot.
- HPC Admin noted the stability issues with the current driver version on Grace Hopper.

## Conclusion
- The issue was likely caused by out-of-memory errors with the NVIDIA driver.
- Rebooting the machine provided a temporary fix, but the driver's stability needs further investigation.
```
---

### 2022113042002891_Different%20results%20on%20different%20Hardware.md
# Ticket 2022113042002891

 ```markdown
# HPC Support Ticket: Different Results on Different Hardware

## Problem Description
- **User Issue**: The user experiences different results when training a neural network on their local machine (GTX970) versus on the HPC cluster (A100 or RTX3080). The accuracy on the local machine is 90%+, while on the cluster it does not surpass 50%.
- **Framework**: PyTorch
- **Environment**: Conda environment with Python 3.10

## Key Points Learned
- **Randomness in PyTorch**: Potential sources of randomness in PyTorch can affect training results.
- **Environment Setup**: Simply copying files may not be sufficient. The Python environment needs to be recreated on the GPU compute node.
- **Batch Script**: The batch script should include loading modules and activating environments inside the script.
- **GPU Support**: Ensure that the Python installation, especially for PyTorch, supports GPUs. This can be checked by running a test command on a GPU node.

## Root Cause
- **Incorrect Environment Setup**: The user's Python environment was not correctly set up to support GPU training on the cluster.
- **Batch Script Issues**: The user was not following the correct workflow for submitting jobs with `sbatch`.

## Solution
- **Environment Setup**: Recreate the Python environment on a GPU compute node.
- **Batch Script**: Include module loading and environment activation inside the batch script.
- **GPU Support Check**: Verify GPU support by running `python -c 'import torch; print(torch.rand(2,3).cuda())'` on a GPU node.

## Recommendations
- **Consult Documentation**: Refer to the provided documentation for setting up Python and PyTorch on the cluster.
- **Advisor Consultation**: Consult with the advisor for additional guidance.
- **Meeting Request**: If needed, request a meeting with HPC support for further assistance.

## Documentation Links
- [PyTorch Randomness](https://pytorch.org/docs/stable/notes/randomness.html)
- [Python and Jupyter on HPC](https://hpc.fau.de/systems-services/documentation-instructions/special-applications-and-tips-tricks/python-and-jupyter/)
- [TensorFlow and PyTorch on HPC](https://hpc.fau.de/systems-services/documentation-instructions/special-applications-and-tips-tricks/tensorflow-pytorch/)
- [TinyGPU Cluster Documentation](https://hpc.fau.de/systems-services/documentation-instructions/clusters/tinygpu-cluster/)
```
---

### 2021062042000762_A%20problem%20with%20cuda.md
# Ticket 2021062042000762

 # HPC Support Ticket: CUDA Issue

## Keywords
- CUDA
- GPU
- PyTorch
- NVIDIA driver
- qsub
- sbatch
- TinyGPU
- Woody
- RuntimeError

## Problem Description
- User encountered a `RuntimeError: Found no NVIDIA driver on your system` while running a PyTorch script on the HPC system.
- The user was trying to run the script on the frontend node (woody) instead of a GPU node.

## Root Cause
- The user did not submit the job to a GPU node, which is required for CUDA operations.
- Incorrect job submission commands were used.

## Solution
- **Job Submission**: The user should submit jobs to the GPU nodes using the appropriate commands.
  - For interactive jobs: `qsub.tinygpu -l nodes=1:ppn=4,walltime=01:00:00 -I`
  - For batch jobs: Create a `.sh` script with the following content and submit it using `sbatch.tinygpu script.sh`:
    ```bash
    #!/bin/bash
    #SBATCH --ntasks=1
    #SBATCH --cpus-per-task=4
    #SBATCH --mem=16000
    #SBATCH --gres=gpu:1
    #SBATCH --mail-type=END,FAIL
    #SBATCH --time=20:00:00
    python3 train.py
    ```
- **Module Loading**: Ensure the correct CUDA version is loaded using `module load cuda/VERSION`.

## Additional Resources
- [TinyGPU Cluster Documentation](https://hpc.fau.de/systems-services/systems-documentation-instructions/clusters/tinygpu-cluster/)
- [Batch Processing Documentation](https://hpc.fau.de/systems-services/systems-documentation-instructions/batch-processing/)
- [HPC Cafe](https://hpc.fau.de/systems-services/support/hpc-cafe/)
- Training for beginners (e.g., July 14 at 4 pm)

## Lessons Learned
- Always submit GPU-dependent jobs to nodes with GPU support.
- Use the correct job submission commands and scripts.
- Ensure the necessary modules (e.g., CUDA) are loaded.
- Utilize available documentation and support resources for assistance.
---

### 2022120842002396_Cuda10.1%20auf%20tinyGPU.md
# Ticket 2022120842002396

 # HPC-Support Ticket Conversation: Cuda10.1 auf tinyGPU

## Keywords
- Cuda10.1
- tinyGPU-Cluster
- ResNet50
- Trainingspipeline
- Laufzeitfehler
- CUBLAS_STATUS_NOT_INITIALIZED
- Nvidia-Matrix
- Treiberkompatibilität
- Hardwarekompatibilität

## Problem
- User requires Cuda10.1 for a training pipeline provided for a master's course.
- The pipeline works on a local system with Cuda10.1 but fails on the tinyGPU-Cluster with a runtime error: `RuntimeError: CUDA error: CUBLAS_STATUS_NOT_INITIALIZED when calling cublasCreate(handle)`.
- The user cannot find Cuda10.1 in the available modules (`module avail cuda` shows only Cuda11.x versions).

## Root Cause
- Cuda10.1 is not compatible with the current drivers and hardware on the tinyGPU-Cluster.
- Cuda10.1 is outdated and not supported on the cluster.

## Solution
- Cuda10.1 will not be provided on the tinyGPU-Cluster due to compatibility issues with current drivers and hardware.
- The user should consider updating the training pipeline to be compatible with newer Cuda versions available on the cluster.

## General Learnings
- Older versions of software may not be compatible with current hardware and drivers.
- It is important to keep software up to date to ensure compatibility with the latest hardware and drivers.
- Always check the available modules and their versions before submitting jobs to the cluster.

## Next Steps
- The user should contact the provider of the training pipeline to inquire about updates or alternatives that are compatible with newer Cuda versions.
- If updating the pipeline is not possible, the user may need to explore other computing resources that support Cuda10.1.
---

### 2023050242003621_tensorflow%20Nutzung%20auf%20TinyGPU.md
# Ticket 2023050242003621

 ```markdown
# HPC Support Ticket: TensorFlow Usage on TinyGPU

## Keywords
- TensorFlow
- Keras
- TinyGPU
- Slurm
- CUDA
- cuDNN
- GPU
- Python
- Shell Script
- `libcuda.so.1`
- `cuInit`
- `sbatch`

## Problem Description
The user attempted to run a TensorFlow/Keras Python script interactively on the TinyGPU system but encountered errors related to the CUDA library and GPU driver. The error messages indicated that the `libcuda.so.1` library could not be found and the GPU driver was not running.

## Root Cause
The user was running the script on the frontend node instead of submitting it to the Slurm scheduler to be executed on a TinyGPU node.

## Solution
The HPC Admin advised the user to submit the script using `sbatch` to ensure it runs on a TinyGPU node. The admin also provided links to documentation for further guidance on using Slurm and the TinyGPU cluster.

## Lessons Learned
- Ensure that GPU-dependent scripts are submitted to the Slurm scheduler using `sbatch` to run on appropriate nodes.
- Verify that the necessary libraries and drivers are available on the execution node.
- Refer to the documentation for detailed instructions on using Slurm and specific clusters.

## References
- [Batch Processing Documentation](https://hpc.fau.de/systems-services/documentation-instructions/batch-processing/)
- [TinyGPU Cluster Documentation](https://hpc.fau.de/systems-services/documentation-instructions/clusters/tinygpu-cluster/)
```
---

### 2023101642002453_Nvidia%20Driver_Library%20version%20mismatch%20auf%20genoa2%20im%20Testcluster.md
# Ticket 2023101642002453

 ```markdown
# HPC-Support Ticket: Nvidia Driver/Library Version Mismatch

## Subject
Nvidia Driver/Library version mismatch auf genoa2 im Testcluster

## Keywords
- Nvidia
- Driver/Library version mismatch
- NVML
- genoa2
- Testcluster

## Problem Description
The user reported that the graphics cards on genoa2 were not usable. Running `nvidia-smi` resulted in the following error:
```
Failed to initialize NVML: Driver/library version mismatch
NVML library version: 535.113
```

## Root Cause
The issue was caused by a partial update of the Nvidia driver and library versions, leading to a mismatch.

## Solution
The HPC Admin identified the problem as a partial update and resolved it. The graphics cards on genoa2 were made functional again.

## Lessons Learned
- Partial updates can cause driver/library version mismatches.
- Regularly check for and address version mismatches to ensure hardware functionality.
- Communicate with users promptly to confirm resolution of issues.

## Actions Taken
1. User reported the issue with `nvidia-smi`.
2. HPC Admin identified the partial update as the root cause.
3. HPC Admin resolved the issue, making the graphics cards functional again.
4. User confirmed the resolution.
5. Ticket closed.
```
---

### 2025012942003638_HPL%20Benchmark%20on%20Alex.md
# Ticket 2025012942003638

 # HPL Benchmark on Alex

## Problem Description
- User attempted to run HPL Benchmark on A100 GPU using a container from NVIDIA NGC.
- The container failed due to a missing library (NVML).

## Root Cause
- Missing symlink for `libnvidia-ml.so` on the GPU nodes.

## Solution
- Create a symlink in the user's home directory:
  ```bash
  ln -s /usr/lib64/libnvidia-ml.so.1 /usr/lib64/libnvidia-ml.so
  ```
- Use the following commands to build and run the container:
  ```bash
  apptainer build hpl.sif docker://nvcr.io/nvidia/hpc-benchmarks:23.5
  srun --ntasks=<number of GPUs> apptainer run --nv <path to container directory>/hpl.sif /workspace/hpl.sh --no-multinode --dat HPL.dat
  ```
- To select 80 GB A100 GPUs, use the Slurm flags:
  ```bash
  --gres=gpu:a100:1 -C a100_80
  ```

## Keywords
- HPL Benchmark
- A100 GPU
- NVML library
- Symlink
- Apptainer
- Slurm

## General Learnings
- Missing libraries or symlinks can cause containerized applications to fail.
- Creating symlinks in the user's home directory can serve as a workaround.
- Specific GPU types can be selected using Slurm flags.
---

### 2024101042003685_Python3.12%20with%20pytorch-cuda.md
# Ticket 2024101042003685

 ```markdown
# HPC-Support Ticket: Python3.12 with Pytorch-CUDA

## Subject
User is unable to get Python3.12 running with Pytorch on tinygpu nodes.

## Problem Description
- User is trying to set up a Conda environment with Python3.12 and Pytorch with CUDA support.
- Environment setup works on the user's local machine but fails on the HPC cluster.
- `torch.cuda.is_available()` returns `False` on the cluster.

## Environment Setup
- **Conda Environment (environment.yml):**
  ```yaml
  name: BA
  channels:
    - pytorch-nightly
    - nvidia
    - defaults
    - conda-forge
  dependencies:
    - python>=3.12, <3.13
    - pytorch
    - pytorch-cuda>=12.4, <13.0
    - torchvision
  ```
- **Modules Loaded:**
  ```bash
  module load python/3.12-conda
  module load cuda/12.4.1
  module load cudnn
  conda activate BA
  ```

## Root Cause
- The CPU version of Pytorch is installed instead of the CUDA version due to dependency resolution issues.
- The environment setup works on an interactive job but fails on the frontend node.

## Solution
- Create the Conda environment in an interactive job instead of the frontend node.
- Ensure that the CUDA version of Pytorch is installed by specifying the correct constraints.

## Key Learnings
- Always create Conda environments in an interactive job to ensure proper dependency resolution.
- Avoid using the `defaults` channel on the cluster to prevent licensing issues.
- Ensure that the correct version of Pytorch with CUDA support is installed by specifying the appropriate constraints in the environment.yml file.

## References
- [NHR@FAU Python Environment Documentation](https://doc.nhr.fau.de/environment/python-env/)
- [Lizenzfalle Anaconda](https://www.rrze.fau.de/2024/09/lizenzfalle-anaconda/)
```
---

### 2022050642002439_no%20GPU%20usage%20-%20iwi5053h.md
# Ticket 2022050642002439

 # HPC Support Ticket: No GPU Usage

## Keywords
- GPU usage
- Job removal
- TensorFlow
- libcudart.so.11.0
- dlerror

## Summary
A job was removed from the HPC system due to no GPU usage. The error log indicated issues with loading the dynamic library `libcudart.so.11.0`.

## Root Cause
The job did not use any GPU resources. The error log showed that TensorFlow could not load the dynamic library `libcudart.so.11.0`, which is required for GPU support.

## Error Log
```
2022-05-06 15:45:19.301746: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libcudart.so.11.0';
dlerror: libcudart.so.11.0: cannot open shared object file: No such file or directory
2022-05-06 15:45:19.302204: I tensorflow/stream_executor/cuda/cudart_stub.cc:29] Ignore above cudart dlerror if you do not have a GPU set up on your
machine.
```

## Solution
Ensure that the required CUDA libraries are installed and properly configured on the system. Verify that the job is correctly set up to utilize GPU resources.

## General Learning
- Always check job logs for GPU usage and related errors.
- Ensure that necessary libraries for GPU support are installed and accessible.
- Properly configure jobs to utilize GPU resources if required.
---

### 2021062942001978_No%20Module%20named%20torch.md
# Ticket 2021062942001978

 ```markdown
# HPC Support Ticket: No Module named torch

## Keywords
- Python modules
- PyTorch
- Module loading
- User space installation
- GPU resources

## Problem Description
The user encountered an error `no module named torch` when running Python scripts that require the `torch` module on the HPC system. The issue occurred specifically when using `tinygpu`, despite the module being available when loaded manually in the terminal.

## Root Cause
The `torch` module was not installed in the user's environment for the specific job script running on `tinygpu`.

## Solution
The HPC Admin provided instructions to install PyTorch in the user's space:

1. Start an interactive job with GPU resources:
   ```bash
   salloc.tinygpu --cpus-per-task=10 --gres=gpu --time=00:30:00
   ```

2. Load the necessary dependencies:
   ```bash
   module load python/3.8-anaconda cuda/11.1.0
   ```

3. Set proxy settings:
   ```bash
   export http_proxy=http://proxy:80
   export https_proxy=http://proxy:80
   ```

4. Install PyTorch using the appropriate command from the [PyTorch website](https://pytorch.org/get-started/locally/), adding `--user` to install in the user space:
   ```bash
   pip3 install --user torch==1.9.0+cu111 torchvision==0.10.0+cu111 torchaudio==0.9.0 -f "https://download.pytorch.org/whl/torch_stable.html"
   ```

5. Test the installation:
   ```bash
   python
   import torch
   ```

## General Learning
- Ensure that all required Python modules are installed in the user's environment for job scripts.
- Use `--user` flag with `pip` to install packages in the user space.
- Load necessary modules and set proxy settings in job scripts to ensure dependencies are available.
```
---

### 2024052842000922_gromacs%20findet%20auf%20gracehop1%20keine%20GPU%20mehr.md
# Ticket 2024052842000922

 # HPC Support Ticket: Gromacs GPU Issue on Gracehop1

## Keywords
- Gromacs
- GPU
- NUMA
- nvidia-persistenced
- Out-of-memory
- cgroups
- Kernel log
- Treiber 550
- slurm
- cpuset
- memory-domain
- numactl

## Problem Description
- Gromacs unable to find GPU on gracehop1.
- Kernel log shows out-of-memory errors and NUMA node issues.
- NUMA domain 1 disappears after executing GPU commands.
- nvidia-persistenced fails to start with permission denied error.

## Root Cause
- The primary issue seems to be related to NUMA domain 1 disappearing after GPU commands are executed.
- nvidia-persistenced service not running properly due to permission issues.

## Troubleshooting Steps
- Attempted to bypass the problem using `ConstrainRAMSpace=no` in `cgroup.conf`, but it was unsuccessful.
- Investigated NUMA domain disappearance and nvidia-persistenced startup issues.

## Solution
- Modified `/etc/systemd/system/nvidia-persistenced.service.d/override.conf` to ensure nvidia-persistenced runs with the correct permissions and settings.
  ```ini
  [Service]
  ExecStart=
  ExecStart=/usr/bin/nvidia-persistenced --user nvidia-persistenced --persistence-mode --verbose
  ExecStartPre=/bin/chown nvidia-persistenced /sys/devices/system/memory/auto_online_blocks
  ```
- With nvidia-persistenced running, NUMA domain 1 retains memory and does not disappear when executing GPU commands.
- Gromacs test runs successfully without out-of-memory errors in the kernel log.

## General Learnings
- Ensure nvidia-persistenced is running properly to maintain NUMA domain memory.
- Permission issues with `/sys/devices/system/memory/auto_online_blocks` can prevent nvidia-persistenced from starting.
- Out-of-memory errors in the kernel log can indicate issues with GPU memory and NUMA domains.
---

### 2025013142000967_Not%20able%20to%20use%20torch%20in%20jupyter%20notebook%20-%20iwb3103h.md
# Ticket 2025013142000967

 # HPC Support Ticket: Not Able to Use Torch in Jupyter Notebook

## Keywords
- Pytorch
- Jupyter Notebook
- Conda Environment
- CUDA
- CUDNN
- ipykernel

## Issue Summary
- User unable to access Pytorch in their environment when using Jupyter Notebook.
- User has installed `ipykernel` as per HPC documentation but still facing issues.
- User loads `cuda` and `cudnn` modules before activating their environment in normal SSH access but cannot do the same in Jupyter Notebook.

## Root Cause
- The environment does not show up in the kernel list in Jupyter Notebook.
- A system library required by the environment is not found.

## Troubleshooting Steps
1. **Preinstalled Pytorch Versions**: HPC Admin suggested using preinstalled Pytorch versions available in the central Jupyterhub instance.
2. **User-Specific Libraries**: User wants to use other libraries in their environment and is unsure about installing libraries in default environments.
3. **Conda Environment Visibility**: HPC Admin suggested running `!conda env list` in the Jupyterhub default kernel to check if the environment shows up.
4. **Library Installation**: HPC Admin suggested installing `conda install conda-forge::cudnn` into the user's environment to fix the library error.

## Solution
- Install the missing library using `conda install conda-forge::cudnn` in the user's environment.
- Verify if the environment shows up in the kernel list by running `!conda env list` in the Jupyterhub default kernel.

## Notes
- Users are not allowed to add packages to the provided conda environments but can use `pip install --user` to install packages into their own space.
- Building a custom conda environment is recommended to avoid dependency issues.
- The issue might be related to a missing Python module in the Jupyterhub installation.

## Follow-Up
- Further investigation is needed to understand why the environment does not show up in the kernel list.
- Additional tests may be required to isolate the issue.

## References
- [Jupyterhub Documentation](https://doc.nhr.fau.de/access/jupyterhub/)
- [HPC Support Email](mailto:support-hpc@fau.de)
- [HPC Website](https://hpc.fau.de/)
---

### 2021121242000266_CUDA%20Installation%20problems%20on%20Fedora%2034.md
# Ticket 2021121242000266

 # CUDA Installation Problems on Fedora 34

## Keywords
- CUDA Installation
- Fedora 34
- NVIDIA Persistence Daemon
- Systemd Service
- CUDA Fortran
- HPC Modules

## Problem Description
- User attempted to install CUDA from the CUDA toolkit documentation on Fedora 34.
- Encountered errors in section 12.1.2 of the installation guide.
- `systemctl status nvidia-persistenced` showed the service as inactive (dead).
- Error message indicated a path issue with the PIDFile in the unit file.

## Root Cause
- The `nvidia-persistenced.service` unit file references a legacy directory path for the PIDFile.
- The user attempted to install CUDA manually instead of using available HPC modules.

## Solution
- **HPC Admin** suggested using the CUDA modules provided by the HPC systems.
- To list available CUDA versions, the user should run:
  ```sh
  module avail cuda
  ```

## General Learnings
- Always check if the required software is available as a module on HPC systems before attempting manual installation.
- Ensure that service unit files are updated to reflect correct paths, especially for legacy directories.
- For CUDA installation issues, verify the status and configuration of the NVIDIA Persistence Daemon.

## Additional Notes
- The user had correctly downloaded the CUDA toolkit and verified the md5sum.
- The user did not address custom `xorg.conf`, which was not applicable in this case.

This documentation can be used to troubleshoot similar CUDA installation issues on Fedora systems in the future.
---

### 2024041842003101_Request%20updates%20for%20NVIDIA%20CUDA%20libraries.md
# Ticket 2024041842003101

 ```markdown
# HPC Support Ticket: Request Updates for NVIDIA CUDA Libraries

## Subject
Request updates for NVIDIA CUDA libraries

## User Request
- **Issue**: NVIDIA toolkits have upgraded to 12.x versions, but the HPC system has outdated CUDA versions (11.3 and 11.6).
- **Details**: User searched available CUDA versions but found only older versions.
- **Request**: Inquire about plans to update CUDA libraries.

## HPC Admin Response
- **Misidentification**: The output provided by the user does not match the HPC systems at Friedrich Alexander Universitaet.
- **Clarification**: The HPC systems at Friedrich Alexander Universitaet no longer use CentOS 7.
- **Suggestion**: User may have confused Florida Atlantic University with Friedrich Alexander Universitaet.
- **Recommendation**: Contact the support team of the correct institution for assistance.

## Keywords
- CUDA
- NVIDIA
- Library Updates
- CentOS 7
- Misidentification
- Support Contact

## Lessons Learned
- **Misidentification of Systems**: Ensure users are contacting the correct support team for their specific HPC system.
- **System Updates**: Regularly update libraries and toolkits to meet user needs and stay current with industry standards.
- **Communication**: Clearly communicate the system specifications and supported software versions to users.

## Solution
- **User Action**: Verify the correct HPC system and contact the appropriate support team.
- **Admin Action**: Provide clear documentation on supported software versions and system specifications.
```
---

### 2023070342004071_Cannot%20find%20%22libnccl.so.2%22.md
# Ticket 2023070342004071

 # HPC Support Ticket: Cannot find "libnccl.so.2"

## Problem Description
- User encountered an `ImportError` when trying to import the `sigpy` module.
- Error message: `libnccl.so.2: cannot open shared object file: No such file or directory`.
- User had previously resolved a similar issue on another server (Tinyx) by loading the correct CUDA module.
- User confirmed that the GPU is available and other modules like `cupy` and `torch` are working fine.

## Steps Taken
1. **Initial Suggestion**:
   - HPC Admin suggested running the command:
     ```bash
     python -m cupyx.tools.install_library --library nccl --cuda 11.x
     ```
   - This command resolved the `sigpy` import issue but caused a new issue with importing `cupy` when using an IDE (PyCharm) for remote access.

2. **Further Investigation**:
   - HPC Admin inquired about the presence of the `tensorrt` folder in the user's conda environment.
   - User confirmed the absence of the `tensorrt` folder and mentioned that the issue persisted even when using VS Code.

3. **Additional Suggestions**:
   - HPC Admin suggested installing `tensorrt`:
     ```bash
     pip install tensorrt
     ```
   - User installed `tensorrt`, but it did not directly solve the problem.

4. **Final Resolution**:
   - User reinstalled `cudatoolkit` on top of the current environment, which resolved the issue.
   - User speculated that the combination of reinstalling `cudatoolkit` and having `tensorrt` installed might have contributed to the solution.

## Conclusion
- The root cause of the problem was related to the `cudatoolkit` installation.
- Reinstalling `cudatoolkit` resolved the issue, possibly in combination with having `tensorrt` installed.

## Keywords
- `libnccl.so.2`
- `ImportError`
- `sigpy`
- `cupy`
- `CUDA`
- `PyCharm`
- `VS Code`
- `tensorrt`
- `cudatoolkit`

## Lessons Learned
- Ensure that the `cudatoolkit` is correctly installed and up-to-date.
- Consider the impact of IDEs on module imports and environment configurations.
- Installing additional libraries like `tensorrt` may help resolve dependency issues.
---

### 2023082242003641_Installing%20cholmod.md
# Ticket 2023082242003641

 # HPC Support Ticket: Installing cholmod

## Keywords
- SuiteSparse
- cholmod
- GMP
- CUDA
- CMake
- Module Load

## Problem
- User encountered an error while installing SuiteSparse (cholmod) due to an unsuitable version of GMP.
- CUDA was not enabled during the build process.

## Root Cause
- The required version of GMP was not found or not properly configured.
- CUDA was not enabled in the build configuration.

## Solution
1. **Load Required Modules:**
   ```sh
   $ module load cmake
   $ module load gmp
   $ module load cuda
   $ module load intel mkl
   ```

2. **Clone SuiteSparse Repository:**
   ```sh
   $ git clone git@github.com:DrTimothyAldenDavis/SuiteSparse.git -b stable
   ```

3. **Build SuiteSparse:**
   ```sh
   $ cd SuiteSparse/SuiteSparse_config/build
   $ cmake ..
   $ cmake --build . --config Release
   $ cd ..
   $ make local
   ```

4. **Build COLAMD:**
   ```sh
   $ cd ../COLAMD
   $ make
   $ make local
   ```

5. **Build AMD:**
   ```sh
   $ cd ../AMD
   $ make
   $ make local
   ```

6. **Build CHOLMOD:**
   ```sh
   $ cd ../CHOLMOD
   $ make
   $ make local
   ```

## Outcome
- Libraries were successfully built and CUDA was enabled.
- The user was able to install SuiteSparse (cholmod) with the required configurations.

## General Learnings
- Ensure that all required modules are loaded before starting the build process.
- Follow the step-by-step instructions provided by the HPC Admin to resolve dependency issues.
- Verify that CUDA is enabled during the build process by checking the build output.
---

### 2022012842001021_CUDA%20error%3A%20no%20kernel%20image%20is%20available.md
# Ticket 2022012842001021

 # HPC Support Ticket: CUDA Error - No Kernel Image Available

## Keywords
- CUDA error
- No kernel image available
- PyTorch
- Compute capability
- GPU architecture
- CUDA_LAUNCH_BLOCKING

## Problem Description
- User encountered a `RuntimeError: CUDA error: no kernel image is available for execution on the device` while training a neural network with PyTorch on the TinyGPU cluster.
- User's PyTorch version: `1.10.2+cuda102`
- Local setup where it works: PyTorch `1.7.1+cu110`

## Root Cause
- Mismatch between the compute capability level of the GPU hardware and the binary's compiled compute capability level.
- Specifically, sm_7x and sm_8x have compatibility issues.

## Solution
- Rebuild the binary with the correct compute capabilities for the target hardware.
- For Ampere hardware (e.g., RTX 3080, A100, A40), use sm_80 or sm_86.
- For Volta or Turing hardware (e.g., V100, RTX 2080ti), use sm_70 or sm_75.

## Additional Debugging Tips
- Use `CUDA_LAUNCH_BLOCKING=1` for more accurate error reporting.

## General Learnings
- Ensure the compute capability of the compiled binary matches the target GPU hardware.
- Be aware of compatibility breaks between different compute capability levels (e.g., sm_7x and sm_8x).
- Always check the hardware specifications of the cluster to compile software accordingly.
---

### 2022072642001416_Job%20on%20TinyGPU%20does%20not%20use%20GPU%20%5Biwal047h%5D.md
# Ticket 2022072642001416

 # HPC Support Ticket: Job on TinyGPU does not use GPU

## Keywords
- GPU utilization
- TensorFlow
- CUDA
- nvidia-smi
- GPU node allocation

## Problem Description
- User's job on TinyGPU (JobID 487722) does not utilize the GPU.
- Monitoring system shows no GPU usage for the user's job.
- TensorFlow installation does not recognize the GPU.

## Root Cause
- TensorFlow installation issue: `failed call to cuInit: CUDA_ERROR_NO_DEVICE: no CUDA-capable device is detected`.
- Incorrect or incomplete TensorFlow build that does not recognize GPU.

## Diagnostic Steps
- HPC Admin provided a screenshot from the monitoring system showing no GPU usage.
- User can SSH to the node and use `nvidia-smi` to check GPU utilization.
- Reference documentation: [Working with NVIDIA GPUs](https://hpc.fau.de/systems-services/systems-documentation-instructions/special-applications-and-tips-tricks/working-with-nvidia-gpus/).

## Solution
- Rebuild TensorFlow on a GPU node to ensure proper GPU recognition.
- Alternatively, move to a different cluster if the current setup cannot be fixed.

## General Learning
- Ensure that jobs allocated to GPU nodes actually utilize the GPU to avoid resource wastage.
- Properly configure and build software (e.g., TensorFlow) to recognize and utilize GPU resources.
- Use monitoring tools and commands like `nvidia-smi` to diagnose GPU utilization issues.

## References
- [Working with NVIDIA GPUs](https://hpc.fau.de/systems-services/systems-documentation-instructions/special-applications-and-tips-tricks/working-with-nvidia-gpus/)
- [TensorFlow CUDA Diagnostics](https://hpc.fau.de/systems-services/systems-documentation-instructions/special-applications-and-tips-tricks/working-with-nvidia-gpus/)
---

### 2024051442002732_Seltsame%20Pytorch-_CUDA-Fehler.md
# Ticket 2024051442002732

 # HPC Support Ticket: Seltsame Pytorch-/CUDA-Fehler

## Keywords
- CUDA Initialization
- PyTorch
- GPU Index Error
- RuntimeError
- No CUDA GPUs Available
- Cluster Configuration

## Summary
Users encountered CUDA initialization errors while running PyTorch scripts on the A100 partition. The errors indicated attempts to access a GPU with an invalid index and reported no available CUDA GPUs.

## Root Cause
- **CUDA Initialization Error**: Attempt to access a GPU with an invalid index.
- **No CUDA GPUs Available**: Error during CUDA initialization in an array job.

## Details
- **Error Messages**:
  - `RuntimeError: device >= 0 && device < num_gpus INTERNAL ASSERT FAILED`
  - `RuntimeError: No CUDA GPUs are available`
- **Affected Jobs**: Job Nr. 1634903, Job 1635605
- **Partition**: A100 with 80GB

## Troubleshooting Steps
- Users upgraded PyTorch and Huggingface Transformers versions, but the issue persisted.
- Users inquired about recent changes in the cluster configuration (driver versions, kernel version, SLURM configuration).

## Solution
- **Pending**: HPC Admins need to investigate recent changes in the cluster configuration and provide further guidance.

## Notes
- The issue affected both training and evaluation scripts.
- Other array tasks in the job continued to run without issues.

## Next Steps
- HPC Admins to check for recent changes in the cluster configuration.
- Users to provide additional logs or error messages if available.

## Contact
- **HPC Admins**: Thomas, Michael Meier, Anna Kahler, Katrin Nusser, Johannes Veh
- **2nd Level Support Team**: Lacey, Dane (fo36fizy), Kuckuk, Sebastian (sisekuck), Lange, Florian (ow86apyf), Ernst, Dominik (te42kyfo), Mayr, Martin
- **Datacenter Head**: Gerhard Wellein
- **Training and Support Group Leader**: Georg Hager
- **NHR Rechenzeit Support**: Harald Lanig
- **Software and Tools Developer**: Jan Eitzinger, Gruber
---

### 2022112242004832_TinyGPU%20-%20Job%20failure.md
# Ticket 2022112242004832

 # HPC Support Ticket: TinyGPU - Job Failure

## Keywords
- TinyGPU Cluster
- Job failure
- ModuleNotFoundError
- PyTorch
- Virtual environment
- Python
- GPU nodes
- `scp/rsync`
- `requirements.txt`
- `pip install`

## Problem Description
- User encountered a `ModuleNotFoundError` for the `torch` module when running a job on the TinyGPU Cluster.
- The job script activates a virtual environment but fails to find the installed packages.

## Root Cause
- The virtual environment was created on the user's local device and transferred to the HPC cluster, potentially causing compatibility issues.
- The virtual environment might not have been properly set up on the GPU nodes.

## Solution
- Ensure the virtual environment is created and set up directly on the GPU nodes.
- Use `requirements.txt` to export the necessary packages and recreate the virtual environment on the HPC cluster using `pip install -r requirements.txt`.
- Follow the HPC documentation and guides for setting up Python and virtual environments:
  - [Python and Jupyter Documentation](https://hpc.fau.de/systems-services/documentation-instructions/special-applications-and-tips-tricks/python-and-jupyter/)
  - [TensorFlow and PyTorch Documentation](https://hpc.fau.de/systems-services/documentation-instructions/special-applications-and-tips-tricks/tensorflow-pytorch/#virtualenv)

## General Learning
- Transferring virtual environments directly from a local device to the HPC cluster can lead to compatibility issues.
- It is recommended to recreate the virtual environment on the HPC cluster using `requirements.txt` and `pip install`.
- Always refer to the HPC documentation and guides for setting up specific applications and environments.
---

