# Topic 20: helma_matrix_channel_jumphost_access

Number of tickets: 53

## Tickets in this topic:

### 2024121142001636_Early-Access%20Helma%20%22Hadrien%20Reynaud%22%20_%20iwai008h.md
# Ticket 2024121142001636

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Keywords
- Early-Access Helma
- GPU-hours
- Miniconda, CUDA, nvcc
- Multi-GPU / Multi-Node with NCCL
- Wandb for real-time logging
- Data management
- Node and GPU limits
- Stress tests

## General Learnings
- **User Requirements**: The user requested access to the Helma cluster with specific software needs (Miniconda, CUDA, nvcc) and a requirement for multi-GPU/multi-node setup with NCCL.
- **Data Management**: The user's data is currently on Alex and a workstation at FAU, with a dataset size of 100GB and experiment checkpoints of a few GB each.
- **Initial Limits**: The user was initially limited to 16 GPUs (4 nodes) on Helma.
- **Increased Limits**: The user requested and was granted an increased limit of 32 nodes (128 GPUs) for stress testing.
- **Communication**: The user was advised to read the Matrix channel backlog and engage in the community.
- **Access Details**: The login node for Helma is "helma.nhr.fau.de", accessible internally or via IPv6, with a jump host option.

## Root Cause of the Problem
- The user needed increased computational resources (more nodes and GPUs) for a large-scale job.

## Solution
- The HPC Admin increased the user's limit to 32 nodes (128 GPUs) to accommodate the user's request for stress testing.

## Documentation for Support Employees
- **Accessing Helma**: Ensure users know the login node details and how to access it internally or via IPv6.
- **Software Requirements**: Verify that required software (Miniconda, CUDA, nvcc) is available and properly configured.
- **Data Management**: Advise users on managing data across different systems and ensure data paths are correctly set up.
- **Resource Limits**: Be prepared to adjust resource limits based on user needs and system stability.
- **Community Engagement**: Encourage users to engage with the community through channels like Matrix for additional support and collaboration.
```
---

### 2025031042004151_Early-Access%20Helma%20%22Chenguang%20Huang%22%20_%20v106be24.md
# Ticket 2025031042004151

 ```markdown
# HPC-Support Ticket Conversation Summary

## Subject: Early-Access Helma

### Keywords:
- Early-Access
- Helma Cluster
- Matrix Channel
- Login Node
- Jumphost
- Dateisysteme
- GPU Hours
- Python
- Conda
- PyTorch
- Multi-GPU/Multi-node

### General Learnings:
- **Access Granted**: User's access to Helma cluster was activated.
- **Matrix Channel**: User received an invitation to the Matrix channel and was advised to read the backlog.
- **Login Node**: Login node for the cluster is `helma.nhr.fau.de`.
- **Jumphost**: Access via IPv6 directly or through the jumphost `csnhr.nhr.fau.de`.
- **Dateisysteme**: All known dateisysteme from Alex are available on Helma.
- **Software Requirements**: User requested Python, Conda, and PyTorch for multi-GPU/multi-node applications.
- **GPU Hours**: User requested 100 GPU hours.
- **Premium Customer**: User belongs to a premium customer group.

### Root Cause of the Problem:
- User needed access to the Helma cluster and specific software for their research.

### Solution:
- Access was granted to the Helma cluster.
- User was provided with necessary login information and invited to the Matrix channel for further support and communication.
```
---

### 2025030342002013_Question%20about%20the%20matrix%20account.md
# Ticket 2025030342002013

 # HPC Support Ticket: Question about the Matrix Account

## Keywords
- Matrix account
- Early-access application
- Helma
- 3D models
- Live-Chat
- Eligibility

## Problem
- User is applying for early-access to Helma for training 3D models.
- User is unsure about the field "Your existing Matrix account" in the application form.
- User is uncertain about eligibility as an Alex or TinyX user.

## Root Cause
- Lack of understanding about what a Matrix account is and how to obtain or use it.

## Solution
- **HPC Admin** clarified that Matrix is a live-chat platform used at [https://chat.fau.de](https://chat.fau.de).
- No further action was required from the user regarding eligibility based on their current user status (Alex or TinyX).

## General Learnings
- Matrix is a live-chat platform used for communication within the HPC community.
- Users applying for early-access to Helma need to be aware of their Matrix account details.
- Clarification on such details can help users complete their application forms accurately.

## Ticket Status
- The ticket was closed after the user's query was resolved.

## Next Steps
- Ensure that users are informed about the Matrix platform and its usage during the application process for early-access to Helma.
- Provide clear instructions or a FAQ section on the application form to avoid similar queries in the future.
---

### 2025022442001611_Early-Access%20Helma%20%22Lukas%20Knobel%22%20_%20v115be12.md
# Ticket 2025022442001611

 # HPC Support Ticket Conversation Summary

## Keywords
- Early-Access Helma
- Matrix Channel
- Login Node
- Jumphost
- Cuda
- Conda
- Python Packages
- GPU Hours
- Vision Models
- VRAM Requirements
- Multi-GPU Training
- PyTorch DDP
- Webdatasets
- Workspaces
- TMPDIR

## General Learnings
- **Access Granted**: User's access to Helma was enabled.
- **Matrix Channel**: User was invited to the Matrix channel and advised to read the backlog.
- **Login Node**: The login node for the cluster is `helma.nhr.fau.de`.
- **Jumphost**: Access is possible via IPv6 directly or through the jumphost `csnhr.nhr.fau.de`.
- **File Systems**: All file systems known from Alex are available on Helma.
- **Software Requirements**: User requested Cuda and Conda to be installed centrally.
- **Python Packages**: User will install Python packages like PyTorch, NumPy, Decord, and Webdataset using Conda.
- **Application**: User trains vision models on videos, requiring high VRAM. Currently using single-GPU training but scaling to multi-GPU/node training with PyTorch's DDP.
- **Data Handling**: User uses staging and Webdatasets for data handling, storing datasets on workspaces and staging them to the local TMPDIR.

## Root Cause of the Problem
- User needed access to Helma and specific software installations for their research.

## Solution
- Access was granted to Helma.
- User was provided with necessary login information and invited to the Matrix channel.
- User was advised to read the backlog and summary of the Matrix channel.
- User was informed that all file systems from Alex are available on Helma.
- User was instructed to install Python packages using Conda.

## Additional Notes
- User's application involves training vision models on videos with high VRAM requirements.
- User is transitioning from single-GPU to multi-GPU/node training using PyTorch's DDP.
- User employs Webdatasets for data handling, storing datasets on workspaces and staging them to the local TMPDIR.
---

### 2025022642002955_Early-Access%20Helma%20%22Anton%20Ehrmanntraut%22%20_%20b233cb10.md
# Ticket 2025022642002955

 # HPC Support Ticket Analysis

## Keywords
- Early-Access Helma
- GPU-hours
- Matrix-Kanal
- Login-Node
- PyTorch
- Flash Attention
- Multi-GPU/Multi-node setup
- DDP/FSDP
- Infiniband
- NHR@FAU

## General Learnings
- **Resource Allocation**: Users may initially request fewer resources but later require significantly more.
- **Communication Channels**: Matrix channels are used for communication and collaboration.
- **Access and Login**: Access to the cluster is provided via login nodes, either directly via IPv6 or through a jump host.
- **Software Requirements**: Users specify required software and verify its compatibility with existing projects.
- **Data Availability**: Data is often already present on specific systems (e.g., atuin).

## Root Cause of the Problem
- The user was removed from the Matrix channel and needed to be re-added.

## Solution
- The HPC Admin was requested to re-add the user to the Matrix channel.

## Additional Notes
- Users should be encouraged to read the channel backlog and participate actively.
- A summary of the backlog is available on a provided link.
- All known date systems from Alex are also available on Helma.

---

This report provides a concise summary of the support ticket conversation, highlighting key points and solutions for future reference.
---

### 2025021942001201_Early-Access%20Helma%20%22Franciskus%20Erick%22%20_%20b143dc20.md
# Ticket 2025021942001201

 ```markdown
# HPC-Support Ticket Conversation Summary

## Subject: Early-Access Helma

### Keywords:
- Early-Access
- Helma
- Matrix-Kanal
- Backlog
- Login-Node
- Jumphost
- FAU-intern
- IPv6
- Pytorch
- Multi-GPU
- Single Node

### General Learnings:
- **Access Granted**: The user's access to Helma was activated.
- **Matrix Channel**: An invitation to the Matrix channel was sent. Users are encouraged to read the channel backlog and participate.
- **Login Information**: The login node for the cluster is "helma.nhr.fau.de". Access is possible internally at FAU, via IPv6, or through the Jumphost "csnhr.nhr.fau.de".
- **File Systems**: All known file systems from Alex are available on Helma.
- **Software Requirements**: The user requested Pytorch for multi-GPU, single-node applications with 2 GPUs.

### Root Cause of the Problem:
- The user needed access to the Helma cluster and specific software for their research.

### Solution:
- Access was granted to the Helma cluster.
- An invitation to the Matrix channel was provided for further communication and support.
- Detailed login instructions and file system information were shared.

### Additional Notes:
- A summary of the backlog, especially from the first days, is available at [this link](https://pad.nhr.fau.de/dfZHvN8-RcSA0VjX17qJgw?both).
- The user was informed about the availability of all known file systems from Alex on Helma.
```
---

### 2025022142001509_Early-Access%20Helma%20%22Valentinos%20Pariza%22%20_%20v115be14.md
# Ticket 2025022142001509

 # HPC Support Ticket Summary

## Subject: Early-Access Helma

### Keywords:
- Early-Access
- Helma Cluster
- Matrix Channel
- Login Node
- Jumphost
- GPU Hours
- Conda
- Python
- Pip
- Checkpoints

### General Learnings:
- **Access Granted**: The user's access to the Helma cluster was activated.
- **Matrix Channel**: The user received an invitation to the Matrix channel and was advised to read the backlog.
- **Login Node**: The login node for the cluster is `helma.nhr.fau.de`.
- **Access Methods**: Access is possible via IPv6 directly or through the jumphost `csnhr.nhr.fau.de`.
- **File Systems**: All known file systems from Alex are available on Helma.
- **Resource Requirements**: The user typically needs around 300 GPU hours every 4 weeks.
- **Software**: The user primarily uses Conda, Python, and Pip.
- **Application**: The user performs single or multi-GPU training of large models, requiring fast GPUs with substantial RAM. Checkpoints are saved on the filesystem to allow for continuation if needed.

### Root Cause of the Problem:
- The user required access to the Helma cluster and information on how to use it effectively.

### Solution:
- The HPC Admin granted access to the Helma cluster and provided detailed instructions on how to access it, including the login node and jumphost information. The user was also invited to the Matrix channel for further support and collaboration.

### Additional Notes:
- The user was advised to read the backlog of the Matrix channel and a summary of the backlog was provided via a link.
- The user's typical resource requirements and software usage were noted for future reference.

---

This summary provides a concise overview of the support ticket, including key details and solutions, to assist HPC support employees in resolving similar issues in the future.
---

### 2024121142000441_Early-Access%20Helma%20%22Bernhard%20Kainz%22%20_%20iwai001h%2C%20b180dc29%2C%20b143dc12.md
# Ticket 2024121142000441

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject
Early-Access Helma - User Request for GPU Hours and Software

## Keywords
- Early-Access Helma
- GPU hours
- Conda environments
- CUDA versions
- IO intensity
- Workspaces
- Scratch storage
- rsync
- tar

## Summary
A user requested early access to the Helma cluster, specifying their need for 500 GPU hours and specific CUDA versions. The user's jobs are IO-heavy and they planned to use workspaces for data location.

## Issues and Solutions
1. **IO Intensity Concerns**
   - **Issue**: Helma has a weak storage connection, which could be problematic for high IO-intensive jobs.
   - **Solution**: The user suggested loading data onto the nodes' scratch storage.

2. **Access and Limits**
   - **Issue**: The user needed access to the Helma cluster.
   - **Solution**: Access was granted with a limit of 16 GPUs (4 nodes) initially.

3. **Data Transfer Efficiency**
   - **Issue**: The user's rsync operations were taking too long.
   - **Solution**: The HPC Admin suggested creating an uncompressed tar file and extracting it directly to the scratch storage, which significantly reduced the time.

## General Learnings
- **Storage Constraints**: Be aware of the storage limitations of the Helma cluster and plan accordingly for IO-heavy jobs.
- **Data Transfer Optimization**: Using tar files for data transfer can be more efficient than rsync for large datasets.
- **Workspace Management**: Workspaces are available on Helma, but management commands need to be executed on another cluster (Alex) temporarily.

## Actions Taken
- **Access Granted**: The user was granted access to the Helma cluster with initial limits.
- **Data Transfer Advice**: The HPC Admin provided advice on optimizing data transfer using tar files.
- **Workspace Information**: The user was informed about the current state of workspace management on Helma.
```
---

### 2024121142000673_Early-Access%20Helma%20%22Mischa%20Dombrowski%22%20_%20b180dc10.md
# Ticket 2024121142000673

 ```markdown
# HPC Support Ticket Conversation Analysis

## Keywords
- Early-Access Helma
- GPU-hours
- Python
- Conda
- PyTorch
- Multi-GPU jobs
- Matrix-Kanal
- Login-Node
- Jumphost
- Workspaces
- GPU limit

## Summary
A user requested early access to the Helma cluster, specifying the need for Python, Conda, and PyTorch for low IO intensity multi-GPU jobs. The user was granted access and provided with essential information for getting started.

## User Request
- **Contact:** User provided contact details.
- **Compute Time:** 1000 GPU-hours requested.
- **Software:** Python and Conda required; PyTorch to be installed by the user.
- **Application:** Low IO intensity multi-GPU jobs.

## HPC Admin Response
- **Access Granted:** User's access to Helma was activated.
- **Matrix Channel:** User was invited to the Matrix channel and advised to read the backlog.
- **Login Information:** Login node details and access methods were provided.
- **File Systems:** All known file systems from Alex are available on Helma.
- **Workspace Management:** Workspace management commands are temporarily unavailable on Helma; use Alex for now.
- **GPU Limit:** Initial limit of 16 GPUs (4 nodes) per user, to be adjusted if stability is maintained.

## Lessons Learned
- **Access Procedure:** Understanding the process for granting early access to new clusters.
- **Software Requirements:** Importance of specifying required software and user responsibilities for additional installations.
- **Communication Channels:** Utilizing Matrix channels for user engagement and support.
- **Resource Limits:** Initial resource limitations and plans for adjustment based on system stability.

## Root Cause and Solution
- **Root Cause:** User needed access to a new cluster with specific software requirements.
- **Solution:** Access was granted, and necessary information was provided for the user to get started, including login details, software availability, and resource limits.
```
---

### 2025011442003068_Early-Access%20Helma%20%22Dirk%20Ribbrock%22%20_%20k107ce10.md
# Ticket 2025011442003068

 ```markdown
# HPC Support Ticket Conversation Analysis

## Keywords
- Early-Access Helma
- GPU hours
- FEAT3
- C++ FEM CFD software
- MPI
- CUDA
- CMake
- Python
- GNUMake
- Vim
- Matrix channel
- Login-Node
- Jumphost
- Dateisysteme
- GPU limit
- Stability

## Summary
- **User Request**:
  - Requested 10,000 GPU hours for scaling benchmarks.
  - Needs central installation of C/C++ compiler, MPI, CUDA, CMake, Python, GNUMake, and Vim.
  - Uses FEAT3, a C++ FEM CFD software, which utilizes multiple GPUs across multiple nodes.
  - Communication via MPI with point2point connections and some central all2all phases.
  - Low IO intensity, with occasional checkpoint writes.
  - Requires shared (parallel) file system for input/output data.

- **HPC Admin Response**:
  - Access to Helma granted.
  - Invitation to Matrix channel provided.
  - Login-Node: `helma.nhr.fau.de`.
  - Access via IPv6 directly or through Jumphost `csnhr.nhr.fau.de`.
  - All known Dateisysteme available on Helma.
  - Initial GPU limit set to 16 GPUs (4 nodes).
  - Limit to be adjusted based on stability.

## Root Cause of the Problem
- User requires specific software and resources for benchmarking.

## Solution
- HPC Admin granted access and provided necessary information for login and resource usage.
- User invited to Matrix channel for further support and communication.

## General Learnings
- Importance of clear communication regarding resource requirements and software needs.
- Providing access to necessary tools and channels for user support.
- Initial resource limits with plans for adjustment based on system stability.
```
---

### 2024121142001341_Early-Access%20Helma%20%22Dawid%20Kopiczko%22%20_%20v115be11.md
# Ticket 2024121142001341

 ```markdown
# HPC Support Ticket Conversation Analysis

## Keywords
- Early-Access Helma
- GPU-hours
- Python, PyTorch, CUDA
- Miniconda, pip
- Single-GPU, Multi-GPU
- Checkpointing
- IO intensive
- Fundamental AI Lab
- Matrix-Kanal
- Login-Node
- Jumphost
- Workspaces
- GPU limit

## General Learnings
- **User Requirements**: The user requires access to GPU resources for pretraining language models (LLMs) with different architectures. They can scale models/datasets based on availability and utilize all resources provided.
- **Software Stack**: The user needs a standard stack of Python, PyTorch, CUDA, and other pip libraries. They are capable of installing these dependencies themselves using Miniconda and pip.
- **Application**: The user trains smaller models on a single GPU and larger models on multiple GPUs. They use checkpointing to save and restore training progress, and their jobs are not expected to be IO intensive.
- **HPC Admin Response**: The user's access to Helma has been granted, and they have been invited to the Matrix channel. The login node is "helma.nhr.fau.de," accessible via IPv6 or the Jumphost "csnhr.nhr.fau.de." All known filesystems are available on Helma, but workspace management commands are currently missing and should be handled via Alex. The user is initially limited to 16 GPUs (4 nodes), with the limit to be adjusted if everything runs smoothly.

## Root Cause of the Problem
- The user needs access to GPU resources for training language models and requires information on how to access and manage these resources on the Helma cluster.

## Solution
- The HPC Admin has granted the user access to Helma and provided instructions on how to access the cluster and manage workspaces. The user is initially limited to 16 GPUs, with the possibility of adjusting the limit based on stability.
```
---

### 2025011342003561_Early-Access%20Helma%20%22Thomas%20Ressler-Antal%22%20_%20v104dd18.md
# Ticket 2025011342003561

 ```markdown
# HPC Support Ticket Conversation Analysis

## Keywords
- Early-Access Helma
- GPU-hours
- Miniconda
- Python
- PyTorch
- Multi-GPU
- Multi-Node
- NCCL
- Transformer/Diffusion Video Model Training
- Webdataset
- Matrix Channel
- Login-Node
- Jumphost
- Dateisysteme

## Summary
- **User Request**: Access to HPC resources for multi-GPU and multi-node training of transformer/diffusion video models.
- **Required Software**: Miniconda, Python, PyTorch (self-installed).
- **Data Storage**: Videos stored at `/home/atuin/v104dd/v104dd10`.
- **Affiliation**: Member of a Computer Vision & Learning Group at a university.

## HPC Admin Response
- **Access Granted**: User's access to Helma cluster enabled.
- **Matrix Channel**: Invitation sent; user advised to read channel backlog.
- **Login Information**: Login-Node `helma.nhr.fau.de`; access via IPv6 or Jumphost `csnhr.nhr.fau.de`.
- **Dateisysteme**: All known dateisysteme available on Helma.

## Lessons Learned
- **Access Procedure**: Users need to request access and provide details about their requirements.
- **Software Installation**: Users can install their own software packages like Miniconda, Python, and PyTorch.
- **Communication**: Matrix channel is used for communication and support; backlog provides useful information.
- **Login Methods**: Access to the cluster can be via direct IPv6 or through a Jumphost.
- **Data Management**: Users can specify where their data is stored and how it is managed.

## Root Cause of the Problem
- User needed access to HPC resources for large-scale model training.

## Solution
- HPC Admins granted access and provided necessary login and communication details.
```
---

### 2025020642001458_Early-Access%20Helma%20%22Soren%20Wacker%22%20_%20ihpc147h.md
# Ticket 2025020642001458

 ```markdown
# HPC-Support Ticket Analysis

## Subject: Early-Access Helma

### Keywords:
- Early-Access
- Helma
- GPU hours
- Single-GPU
- Multi-GPU/Multi-node

### Summary:
- **User Contact:** Provided contact information including email and matrix user.
- **Compute Time:** Requested 100 GPU hours.
- **Software:** No specific software mentioned.
- **Application:** Single-GPU and Multi-GPU/Multi-node usage.
- **Additional Comments:** None provided.

### Root Cause of the Problem:
- The user is requesting early access to Helma with specific GPU requirements.

### Solution:
- **HPC Admins:** Review the request and allocate the necessary GPU hours.
- **2nd Level Support Team:** Assist with any setup or configuration needed for Single-GPU and Multi-GPU/Multi-node applications.
- **Gehard Wellein (Head of the Datacenter):** Ensure resource availability.
- **Georg Hager (Training and Support Group Leader):** Provide any necessary training or support materials.
- **Harald Lanig:** Assist with NHR Rechenzeit Support and Applications for Grants if needed.
- **Jan Eitzinger and Gruber (Software and Tools Developer):** Assist with any software or tool-related issues.

### General Learnings:
- Early-access requests require coordination among multiple teams.
- GPU hours allocation needs to be managed efficiently.
- Proper setup and configuration for Single-GPU and Multi-GPU/Multi-node applications are crucial.
```
---

### 2024122042003448_Early-Access%20Helma%20%22Guri%20Zabergja%22%20_%20b250be11.md
# Ticket 2024122042003448

 ```markdown
# HPC-Support Ticket Conversation Summary

## Keywords
- Helma cluster
- SLURM script
- GPU utilization
- Matrix account
- Proxy settings
- Multi-Process Service (MPS)
- Job concurrency

## General Learnings
- **Cluster Access**: Helma cluster access via `helma.nhr.fau.de` or through the Jumphost `csnhr.nhr.fau.de`.
- **Default Partition**: Helma's default partition is the low priority "preempt" partition.
- **Matrix Account**: Important for receiving updates and information. Users should have personal Matrix accounts.
- **Proxy Settings**: Use full DNS name for proxy settings on Helma (`proxy.rrze.uni-erlangen.de`).
- **MPS Setup**: NVIDIA Multi-Process Service can improve GPU utilization.
- **Job Concurrency**: Users may request to run more jobs concurrently if needed.

## Issues and Solutions

### Issue: Job Stuck with Message "Nodes required for job are DOWN, DRAINED or reserved for jobs in higher priority partitions"
- **Root Cause**: Default partition on Helma is "preempt" and all nodes were in use.
- **Solution**: Job eventually ran as nodes became available.

### Issue: No Email Invitation for Matrix Channel
- **Root Cause**: Matrix account provided belonged to the supervisor.
- **Solution**: User created a personal Matrix account.

### Issue: Low GPU Utilization
- **Root Cause**: Small models and datasets resulting in lower computational demand.
- **Solution**: MPS setup increased GPU utilization to 60-70%.

### Issue: Proxy Settings Not Working
- **Root Cause**: Incorrect proxy settings.
- **Solution**: Use full DNS name `proxy.rrze.uni-erlangen.de`.

### Issue: Limited Job Concurrency
- **Root Cause**: User limited to 8 concurrent jobs.
- **Solution**: User requested to run more jobs concurrently.

## Additional Notes
- **Application Performance**: Despite increased GPU utilization with MPS, power consumption remained low. Comparison with other clusters (Alex with A40) suggested similar performance at lower cost.
- **Matrix Account Setup**: Users can register on popular public Matrix home servers like `matrix.org` or use institutional servers like `matrix.uni-freiburg.de`.
```
---

### 2025031442003681_Early-Access%20Helma%20%22Leonhard%20Kraft%22%20_%207535A22F5A99E719%40tum.de.md
# Ticket 2025031442003681

 ```markdown
# HPC-Support Ticket Conversation Summary

## Subject: Early-Access Helma

### Keywords:
- Early-Access
- Helma
- Matrix-Kanal
- Login-Node
- Jumphost
- Dateisysteme
- Cuda
- Conda
- Python
- PyTorch
- Multi-GPU
- Deep Learning
- Computer Vision
- Lustre Workspace

### General Learnings:
- **Access Granted**: User's access to Helma was activated.
- **Matrix Channel**: User received an invitation to the Matrix channel and was advised to read the backlog.
- **Login Information**: Login node is `helma.nhr.fau.de`, accessible via IPv6 directly or through the Jumphost `csnhr.nhr.fau.de`.
- **File Systems**: All known file systems from Alex are available on Helma.
- **Software Requirements**: User requires Cuda, Conda, Python >=3.9, and PyTorch.
- **Application**: User is working on multi-GPU deep learning/computer vision workloads, using ~8 GPUs for 1-6 hours per job, with data located on Lustre workspace.
- **Research Affiliation**: User is researching in Prof. Asano's lab at UTN.

### Root Cause of the Problem:
- User needed access to Helma and specific software for their research work.

### Solution:
- Access was granted to Helma.
- User was provided with login information and invited to the Matrix channel for further support and communication.
```
---

### 2024121842001481_Early-Access%20Helma%20%22Stefan%20Baumann%22%20_%20v104dd11.md
# Ticket 2024121842001481

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Keywords
- Early-Access Helma
- GPU hours
- PyTorch
- CUDA
- ffmpeg
- libav
- Multi-GPU & multi-node training
- NCCL
- InfiniBand
- IO intensity
- Large-scale Deep Learning workloads
- atuin
- Matrix-Kanal
- Login-Node
- Jumphost
- Dateisysteme
- GPU limit

## Summary
- **User Request**:
  - Contact: User provided contact details.
  - GPU hours: ~18k
  - Required Software: PyTorch, standard Python ML ecosystem, recent CUDA, ffmpeg, libav.
  - Application: Multi-GPU & multi-node training, communication via NCCL with InfiniBand backend, typical IO intensity for large-scale Deep Learning workloads.
  - Data location: atuin.

- **HPC Admin Response**:
  - Access granted to Helma.
  - Invitation to Matrix-Kanal.
  - Login-Node: helma.nhr.fau.de.
  - Access via IPv6 or Jumphost csnhr.nhr.fau.de.
  - All known Dateisysteme available on Helma.
  - Initial GPU limit: 16 GPUs (4 Nodes).

- **HPC Admin Concern**:
  - Concerns about IO intensity and data location on atuin.

## Lessons Learned
- **Access and Communication**:
  - Users are granted access to HPC resources and invited to communication channels like Matrix-Kanal.
  - Important to read channel backlog for additional information.

- **Resource Limits**:
  - Initial limits on GPU usage are set and can be adjusted based on stability.

- **Software and Data**:
  - Users specify required software and data locations.
  - HPC Admins ensure the availability of necessary software and access to data systems.

- **Concerns**:
  - HPC Admins may express concerns about specific aspects of the user's request, such as IO intensity and data location.

## Root Cause of the Problem
- User's request for high GPU hours and specific software requirements.
- Concerns about IO intensity and data location.

## Solution
- Access granted with initial GPU limits.
- Invitation to communication channels for further support and information.
- Monitoring of resource usage and adjustments as needed.
```
---

### 2024121742002697_Early-Access%20Helma%20%22Paula%20Andrea%20Perez-Toro%22%20_%20iwi5214h.md
# Ticket 2024121742002697

 # HPC Support Ticket Conversation Analysis

## Keywords
- Early-Access Helma
- GPU hours
- PyTorch, PyTorch Lightning, Diffusers, Transformers, Monai
- Multi-GPU
- Diffusion models, Transformer models
- A40, A100, H100 GPUs
- Resource constraints
- Batch size
- Model training
- Personalized diagnostics
- Foundational models
- Model distillation
- 24-hour limit
- Full dataset training
- Critical deadlines
- Grant proposals
- Slurm group
- Matrix channel
- Login node
- Jumphost
- Dateisysteme

## General Learnings
- **User Requirements**: The user requires 2000-4000 GPU hours for training models with around 2 billion parameters, combining speech signals, videos, and text information.
- **Software Needs**: The user needs software like PyTorch, PyTorch Lightning, Diffusers, Transformers, and Monai.
- **Current Challenges**: The user faces resource constraints, reduced batch sizes, and limited training time due to a 24-hour limit.
- **Project Importance**: The user is leading a funded project with critical deadlines and aims to publish papers for a larger proposal.
- **HPC Admin Response**: The HPC admin initially questions the benefit of moving to H100 GPUs but later grants early access to Helma to meet critical deadlines.
- **Access Granted**: The user is granted access to Helma with up to 32 GPUs and is invited to a Matrix channel for further support.

## Root Cause of the Problem
- The user's current hardware (A40 and A100 GPUs) is insufficient for training large models with the full dataset, leading to resource constraints and limited training time.

## Solution
- The HPC admin granted the user early access to Helma, allowing the use of up to 32 GPUs. This should help the user meet critical deadlines and enhance training capabilities.

## Documentation for Support Employees
- **Access Request**: Users requiring extensive GPU resources for large models should request early access to advanced hardware like Helma.
- **Communication**: Clear communication about project importance and deadlines can help in getting timely access to required resources.
- **Support Channels**: Utilize Matrix channels for additional support and collaboration with other users and HPC admins.
- **Login Information**: Provide users with login node details and access instructions, including the use of jumphosts if necessary.

This documentation can be used to address similar issues in the future, ensuring that users with critical deadlines and extensive resource needs are supported effectively.
---

### 2025022742003407_Early-Access%20Helma%20%22Raza%20Yunus%22%20_%20v114be12.md
# Ticket 2025022742003407

 # HPC Support Ticket Conversation Summary

## Subject: Early-Access Helma

### Keywords:
- Early-Access
- Helma
- Matrix-Kanal
- Login-Node
- Jumphost
- CUDA
- Pytorch
- Blender
- GPU hours
- 3D inverse rendering
- Ray tracing

### General Learnings:
- **Access Granted**: User's access to Helma has been enabled.
- **Matrix Channel**: User received an invitation to the Matrix channel and is advised to read the backlog.
- **Login Information**: Login node is `helma.nhr.fau.de`; access via IPv6 directly or through the Jumphost `csnhr.nhr.fau.de`.
- **File Systems**: All known file systems from Alex are available on Helma.
- **Software Requirements**: User requires CUDA, Pytorch, and Blender.
- **Application Details**: User plans to run single-GPU jobs for rendering scenes in Blender and heavy computation tasks for a 3D inverse rendering pipeline.
- **Resource Allocation**: User requested 200 GPU hours.

### Root Cause of the Problem:
- User needed access to Helma and specific software for their computational tasks.

### Solution:
- Access to Helma was granted.
- User was provided with login details and instructions for accessing the Matrix channel.
- User was informed about the availability of required file systems and software.

### Additional Notes:
- The Matrix channel backlog and summary are useful resources for new users.
- The Jumphost `csnhr.nhr.fau.de` can be used for accessing the login node if direct IPv6 access is not available.

---

This summary provides a concise overview of the support ticket conversation, highlighting key points and solutions for future reference.
---

### 2025010742001878_Early-Access%20Helma%20%22Florian%20Walter%22%20_%20v108be11.md
# Ticket 2025010742001878

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Keywords
- Early-Access Helma
- GPU hours
- Conda version
- CUDA
- Jaxlib
- PyTorch
- TensorFlow
- Jax
- High IO throughput
- Multi-node training
- Torch distributed
- Jax distributed
- NCCL backend
- Matrix-Kanal
- Login-Node
- Jumphost
- Dateisysteme

## General Learnings
- **User Requirements**:
  - Need for the latest Conda version to install arbitrary CUDA and Jaxlib versions.
  - High IO throughput required for training datasets consisting of several TB.
  - Interest in multi-node training with larger batch sizes using Torch distributed and Jax distributed with NCCL backend.

- **HPC Admin Actions**:
  - Access to Helma granted.
  - Invitation to Matrix-Kanal provided.
  - Login-Node and Jumphost information shared.
  - All known dateisystems from Alex are available on Helma.

- **User Response**:
  - Acknowledgment and thanks for quick access grant.

## Root Cause of the Problem
- Outdated Conda version on Alex, preventing the installation of required CUDA and Jaxlib versions.

## Solution
- Provide access to Helma with the latest Conda version and necessary software support for multi-node training.
```
---

### 2024121842001463_Early-Access%20Helma%20%22Nick%20Stracke%22%20_%20v104dd12.md
# Ticket 2024121842001463

 ```markdown
# HPC Support Ticket Conversation Summary

## Keywords
- Early-Access Helma
- GPU hours
- CUDA driver
- ffmpeg with CUDA support
- lib-av
- Deep learning with PyTorch
- High IO intensity
- Scratch partition
- Matrix channel
- Login node
- Jumphost
- Dateisysteme
- GPU limit

## General Learnings
- **User Requirements**: The user requested 18,000 GPU hours and specified necessary software including an up-to-date CUDA driver, ffmpeg built with CUDA support, and lib-av.
- **Application Details**: The user's application involves deep learning with PyTorch, requiring 4-16 nodes per job, high IO intensity, and data stored on the scratch partition.
- **Admin Response**: The HPC Admin granted access to the Helma cluster, provided login details, and mentioned a temporary GPU limit of 16 GPUs (4 nodes).
- **Software Availability**: The HPC Admin noted that ffmpeg with CUDA support and lib-av are not centrally installed and unlikely to be available before Christmas.
- **IO Concerns**: The Admin expressed concern about the high IO intensity mentioned by the user.

## Root Cause of the Problem
- The user requires specific software (ffmpeg with CUDA support and lib-av) that is not currently installed on the cluster.

## Solution
- The user can install additional software using conda/mamba.
- The HPC Admin provided access to the cluster and relevant login details.
- The user should monitor the Matrix channel for updates and engage with the community for further assistance.
```
---

### 2025021942003271_Early-Access%20Helma%20%22Kolja%20Bauer%22%20_%20v104dd24.md
# Ticket 2025021942003271

 ```markdown
# HPC Support Ticket Summary

## Subject: Early-Access Helma

### Keywords:
- Early-Access
- Helma Cluster
- Matrix Channel
- Login Node
- Jumphost
- Dateisysteme
- Python
- PyTorch
- CUDA
- Multi-GPU
- Single-Node
- Multi-Node
- Sharded Datasets

### General Learnings:
- **Access Granted**: User's access to the Helma cluster was activated.
- **Matrix Channel**: User received an invitation to the Matrix channel and was advised to read the channel backlog.
- **Login Node**: The login node for the cluster is `helma.nhr.fau.de`.
- **Access Methods**: Access is possible via IPv6 directly or through the Jumphost `csnhr.nhr.fau.de`.
- **File Systems**: All file systems known from Alex are available on Helma.
- **Software Requirements**: User requires Python, PyTorch, and CUDA.
- **Application Details**: User runs multi-GPU jobs, mostly single-node, with some multi-node jobs. Data is loaded from sharded datasets.

### Root Cause of the Problem:
- User needed access to the Helma cluster and relevant information for getting started.

### Solution:
- Access was granted, and detailed instructions were provided for logging in and accessing the Matrix channel.
```
---

### 2024121142000404_Early-Access%20Helma%20%22Andreas%20Hotho%22%20_%20b185cb11.md
# Ticket 2024121142000404

 ```markdown
# HPC Support Ticket Conversation Analysis

## Keywords
- Early-Access Helma
- GPU hours
- Software requirements
- Single-GPU vs. Multi-GPU/Multi-node
- Communication framework
- IO intensity
- Data location
- Matrix channel
- Login node
- Jumphost
- Workspaces
- GPU limits

## General Learnings
- **Access Granting**: The user's access to the Helma cluster was granted, and they received an invitation to the Matrix channel.
- **Login Information**: The login node for the cluster is "helma.nhr.fau.de". Access is possible via IPv6 directly or through the jumphost "csnhr.nhr.fau.de".
- **File Systems**: All known file systems from another cluster (Alex) are available on Helma.
- **Workspace Management**: Commands for managing workspaces are currently missing on Helma. Users should use the previous cluster (Alex) for workspace management.
- **GPU Limits**: Initially, each user is limited to 16 GPUs (4 nodes). This limit will be adjusted if the system remains stable.

## Root Cause of the Problem
- The user requested access to the Helma cluster and provided necessary details such as contact information, required software, and application specifics.

## Solution
- The HPC Admin granted access to the Helma cluster and provided essential login and usage information. The user was also invited to the Matrix channel for further communication and support.
```
---

### 2024121142000388_Early-Access%20Helma%20%22Jona%20Ruthardt%22%20_%20v115be13.md
# Ticket 2024121142000388

 # HPC Support Ticket: Early-Access Helma

## Keywords
- Early-Access Helma
- GPU hours
- Python libraries
- High IO workload
- Storage-Anbindung
- Node-local storage

## Summary
- **User Request**: Approximately 1000 GPU hours for running inference on large language models (LLMs) with high IO workload to $TEMP and $WORK.
- **Software Requirements**: Centrally installed Python, conda, pip, CUDA; user-installed Python libraries (e.g., PyTorch).
- **Storage Concerns**: High IO workload involving many small files within node-local storage.

## Issue
- **Root Cause**: Helma has a weak storage connection, which could be problematic for high IO workloads.
- **User Clarification**: The user stores many small files in a ZIP/tar archive, resulting in few large files for transfer between $WORK and $TEMP, but many small read/write operations within node-local storage.

## Solution
- **Admin Response**: Access to Helma granted with a limit of 16 GPUs (4 nodes) for initial stability testing.
- **Additional Information**: Users should read the Matrix channel backlog and use the login node "helma.nhr.fau.de" for access. Workspace management commands are currently unavailable on Helma; use Alex for now.

## General Learnings
- **Storage Considerations**: Be aware of storage limitations on Helma, especially for high IO workloads involving many small files.
- **Access and Limits**: Initial access may be limited to ensure system stability.
- **Workspace Management**: Use Alex for workspace management commands until they are available on Helma.

## Next Steps
- Monitor system stability and adjust GPU limits as needed.
- Ensure users are aware of storage limitations and best practices for high IO workloads.
---

### 2024121842002515_Early-Access%20Helma%20%22Johannes%20Schusterbauer%22%20_%20v104dd20.md
# Ticket 2024121842002515

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Keywords
- Early-Access Helma
- GPU-hours
- Python, PyTorch, PyTorch-lightning
- Conda
- Multi-GPU/multi-node training
- Matrix channel
- Login-Node
- Jumphost
- Dateisysteme
- User limit

## Summary
- **User Request**: Access to Early-Access Helma with ~12k GPU-hours.
- **Required Software**: Python with PyTorch, PyTorch-lightning, Conda for environment management.
- **Application**: Alternating between single and multi-node training, typically using 4-8 GPUs.

## HPC Admin Response
- **Access Granted**: User access to Helma enabled.
- **Matrix Channel**: Invitation sent, recommended to read channel backlog.
- **Login Details**: Login-Node is "helma.nhr.fau.de", accessible via IPv6 or Jumphost "csnhr.nhr.fau.de".
- **File Systems**: All known file systems from Alex are available on Helma.
- **User Limit**: Initial limit of 16 GPUs (4 nodes) for stability testing.

## General Learnings
- **Access Procedure**: Users are granted access to HPC resources after submitting a request.
- **Communication**: Matrix channel is used for updates and user engagement.
- **Resource Limits**: Initial limits are set for stability and adjusted based on performance.
- **Software Environment**: Users often rely on specific software stacks and environment management tools like Conda.

## Root Cause of the Problem
- User needed access to HPC resources for multi-GPU/multi-node training.

## Solution
- Access granted with initial resource limits and instructions for login and communication.
```
---

### 2024121842001445_Early-Access%20Helma%20%22Felix%20Krause%22%20_%20v104dd16.md
# Ticket 2024121842001445

 # HPC Support Ticket: Early-Access Helma

## Keywords
- Early-Access Helma
- Inodes
- Filesystem Usage
- Matrix Channel
- Login Node
- GPU Limits

## Summary
A user requested early access to the Helma cluster, specifying the need for Cuda and Pytorch software. The user was granted access but was notified about excessive inode usage on the $WORK filesystem.

## Root Cause
- Excessive inode usage (over 10 million inodes) on the $WORK filesystem.

## Solution
- Reduce the number of inodes by consolidating files into more appropriate formats, such as tar archives.

## Lessons Learned
- Monitor inode usage to ensure efficient filesystem utilization.
- Utilize appropriate data formats to minimize the number of individual files.
- Regularly attend HPC-Cafes to stay informed about best practices and common issues.
- Access the Matrix channel for additional support and community engagement.

## Additional Information
- The user was granted access to the Helma cluster and received an invitation to the Matrix channel.
- Initial GPU limits were set to 16 GPUs (4 nodes) and may be adjusted based on stability.
- Access to the cluster is available via the login node "helma.nhr.fau.de" or through the Jumphost "csnhr.nhr.fau.de".

## Recommendations
- Regularly review and optimize filesystem usage to prevent excessive inode consumption.
- Engage with the HPC community through the Matrix channel and HPC-Cafes for ongoing support and best practices.

---

This documentation aims to assist HPC support employees in resolving similar issues related to filesystem usage and early access requests.
---

### 2025013042001959_Early-Access%20Helma%20%22Jonas%20Thies%22%20_%20ihpc121h.md
# Ticket 2025013042001959

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Keywords
- Matrix Account
- Helma Early-Access
- GPU Hours
- Essential Software (MPI, CUDA, CMake)
- Multi-GPU Simulation Workflows

## General Learnings
- A Matrix account is essential for receiving updates and block time allocations for Helma Early-Access.
- The home server of the Matrix account is not a concern.
- Users need to create a Matrix account to proceed with their requests.

## Root Cause of the Problem
- The user did not have a Matrix account, which is required for receiving updates and block time allocations.

## Solution
- The user created a Matrix account (@jthies:matrix.org) to comply with the requirement.

## Notes
- The user requested 100 GPU hours for small tests.
- Essential software required includes MPI, CUDA, and CMake.
- The application involves multi-GPU simulation workflows.
```
---

### 2025021642000421_Early-Access%20Helma%20%22Zhe%20Li%22%20_%20b180dc19.md
# Ticket 2025021642000421

 ```markdown
# HPC Support Ticket Conversation Summary

## Keywords
- Early-Access Helma
- Matrix-Kanal
- Login-Node
- Jumphost
- Dateisysteme
- Python
- Anaconda
- CUDA
- gcc
- g++
- Multi-GPU
- A100 80G
- Communication framework
- IO intensity
- Rechenzeit

## General Learnings
- **Access Granted**: User's access to Helma was activated.
- **Matrix Channel**: User received an invitation to the Matrix channel and was advised to read the backlog.
- **Login Information**: Login node for the cluster is `helma.nhr.fau.de`. Access is available internally, via IPv6, or through the jumphost `csnhr.nhr.fau.de`.
- **File Systems**: All known file systems from Alex are available on Helma.
- **Software Requirements**: User requested Python, Anaconda, CUDA (11.8 or higher), gcc, and g++.
- **Application Details**: User plans to use multi-GPU setups, typically A100 80G, with a specified communication framework and IO intensity.
- **Data Location**: User's data is located on Helma.
- **Successful GPU Usage**: User confirmed successful GPU usage on Helma.

## Root Cause of the Problem
- User needed access to Helma and specific software for their computational tasks.

## Solution
- HPC Admins granted access to Helma and provided necessary login and software information.
- User successfully utilized the GPUs on Helma.
```
---

### 2025021742002472_Early-Access%20Helma%20%22Ibrahim%20Ethem%20Hamamci%22%20_%20553131363632303702%40uzh.ch.md
# Ticket 2025021742002472

 # HPC Support Ticket Conversation Summary

## Keywords
- Early-Access Helma
- Matrix ID
- HPC Account
- Login Node
- Jumphost
- IPv6
- Python 3.8+
- PyTorch
- CUDA
- Hugging Face Transformers
- Accelerate
- scikit-learn
- NumPy
- Pandas
- tqdm
- nibabel
- Docker/Singularity containers
- Conda modules
- GPU hours
- Distributed training
- NCCL communication framework
- CT-RATE dataset
- High I/O intensity
- Parallel data loaders
- High-performance shared storage

## General Learnings
- **Account Activation**: HPC accounts can be enabled even if the Matrix ID is not specified correctly.
- **Login Node**: The login node for the cluster is "helma.nhr.fau.de". Access is via IPv6 directly or through the jumphost "csnhr.nhr.fau.de".
- **Software Requirements**: Users should specify their software requirements clearly, including versions and dependencies.
- **Data Handling**: High I/O intensity datasets require efficient data throughput solutions, such as parallel data loaders with multiple workers.
- **Communication**: Users should be encouraged to read the channel backlog and engage in the Matrix channel for updates and support.

## Root Cause of the Problem
- **Account Access Issue**: The user reported that their account was not available despite being enabled by the HPC Admin.

## Solution
- **Retry Access**: The HPC Admin advised the user to try logging in again.

## Additional Notes
- **Matrix Channel**: Users should read the channel backlog and engage in the Matrix channel for updates and support.
- **Software Environment**: The cluster's central environment should provide optimized performance for centrally managed libraries and custom modules.

This summary can be used as a reference for support employees to troubleshoot similar issues in the future.
---

### 2025022442001951_Early-Access%20Helma%20%22Eddy%20Ilg%22%20_%20v114be13.md
# Ticket 2025022442001951

 # HPC Support Ticket Conversation Analysis

## Keywords
- Early-Access Helma
- Matrix-Kanal
- Login-Node
- Jumphost
- Dateisysteme
- Rechenzeit
- Software
- Anwendung
- Freischaltung
- Doktoranden
- Regelbetrieb
- Nutzungskategorien

## General Learnings
- **Access Granting**: During the early-access test phase, access must be requested individually via a form.
- **Communication**: Important updates and messages regarding Helma are communicated exclusively through the Matrix channel.
- **Login Information**: The login node for the cluster is `helma.nhr.fau.de`, accessible via IPv6 directly or through the jumphost `csnhr.nhr.fau.de`.
- **File Systems**: All file systems known from Alex are also available on Helma.
- **Group Access**: In the regular operation phase, access for groups will depend on the specific usage category and potential restrictions set by the university.

## Root Cause of the Problem
- **User Concern**: The user wanted to know if the access granted to them automatically extends to their PhD students.

## Solution
- **Individual Applications**: During the early-access phase, each PhD student must individually apply for access using the provided form. This ensures that necessary data, such as Matrix account information, is collected for each user.

## Documentation for Support Employees
- **Access Request Process**: Ensure users are aware that during the early-access phase, each individual must apply for access separately.
- **Communication Channels**: Direct users to the Matrix channel for the latest updates and important messages regarding Helma.
- **Login Details**: Provide users with the login node information and access methods (IPv6 or jumphost).
- **File System Availability**: Confirm that all known file systems from Alex are available on Helma.
- **Group Access in Regular Operation**: Inform users that group access during regular operation will depend on their specific usage category and any restrictions set by the university.

This documentation will help support employees address similar queries efficiently.
---

### 2025021242003659_Early-Access%20Helma%20%22Yannik%20Blei%22%20_%20ajin94as%40utn.de.md
# Ticket 2025021242003659

 ```markdown
# HPC Support Ticket Conversation Summary

## Keywords
- Early-Access Helma
- Matrix-Kanal
- Login-Node
- Jumphost
- GPU hours
- Pytorch
- Huggingface
- Multi-GPU training
- LLM fine-tuning

## General Learnings
- **Access Granted**: User access to Helma cluster was activated.
- **Matrix Channel**: User received an invitation to the Matrix channel and was advised to read the backlog.
- **Login Information**: Login node is `helma.nhr.fau.de`, accessible via IPv6 or through the Jumphost `csnhr.nhr.fau.de`.
- **File Systems**: All known file systems from Alex are available on Helma.
- **Resource Request**: User requested around 40 GPU hours until the end of February, with the possibility of extension or reduction.
- **Software Requirements**: User will use Pytorch and the Huggingface stack, with most installations manageable with user privileges.
- **Application**: Multi-GPU single node training for LLM fine-tuning with text-only datasets fitting on local node storage.

## Root Cause of the Problem
- User needed access to the Helma cluster and required specific software and resources for their project.

## Solution
- HPC Admin granted access to the Helma cluster and provided necessary login information and resource details.
- User was advised to join the Matrix channel and read the backlog for additional information.
```
---

### 2025022842001872_Early-Access%20Helma%20%22Ming%20Gui%22%20_%20v104dd14.md
# Ticket 2025022842001872

 ```markdown
# HPC-Support Ticket Conversation Summary

## Subject: Early-Access Helma / v104dd14

### Keywords:
- Early Access
- Helma Cluster
- Matrix Channel
- Login Node
- Jumphost
- GPU Hours
- Python
- PyTorch
- CUDA
- Multi-GPU Training
- WebDataset
- Sharded Data

### General Learnings:
- **Access Granted**: User's access to the Helma cluster was activated.
- **Matrix Channel**: User received an invitation to the Matrix channel and was advised to read the backlog.
- **Login Information**: Login node for the cluster is `helma.nhr.fau.de`, accessible via IPv6 or through the Jumphost `csnhr.nhr.fau.de`.
- **File Systems**: All known file systems from Alex are available on Helma.
- **Software Requirements**: User will primarily use Python and PyTorch, with CUDA installed centrally. Additional libraries like Transformers, PyTorch Lightning, TensorBoard, and xFormers will be installed by the user.
- **Application Details**: User will work with multi-GPU, single-node training, occasionally requiring multiple nodes. WebDataset library will be used with sharded data to minimize I/O overhead. Training jobs typically run for a full day on a node.

### Root Cause of the Problem:
- User needed access to the Helma cluster and information on how to get started.

### Solution:
- HPC Admin provided access to the Helma cluster and detailed instructions on how to log in and get started, including information on the Matrix channel and file systems.
```
---

### 2025021742001188_Early-Access%20Helma%20%22Josif%20Grabocka%22%20_%20v101.md
# Ticket 2025021742001188

 # HPC Support Ticket Conversation Summary

## Subject: Early-Access Helma "Josif Grabocka" / v101

### Keywords:
- Ollama installation
- LLM models
- Disk quota
- HPC driver's license
- File systems
- Data storage
- EU AI Act
- Manual installation
- SGLANG
- VLLM backend
- Tensor parallelism
- Batching
- Conda environment
- Endpoint access
- Resource usage

### What Can Be Learned:
- **Manual Installation**: Users can install and update Ollama manually without superuser rights.
- **Disk Quota Management**: Understanding file systems and data storage is crucial for managing disk quotas.
- **EU AI Act**: Compliance with the EU AI Act is necessary when serving AI models.
- **SGLANG Setup**: SGLANG with VLLM backend is better suited for generating data with LLMs via an endpoint.
- **Conda Environment**: Setting up a Conda environment for SGLANG can be an alternative to using containers.
- **Endpoint Access**: Guidance on accessing the endpoint and optimal resource usage is essential for efficient data generation.

### Root Cause of the Problem:
- User faced difficulties with disk quota due to the large size of LLM models.
- Lack of understanding about file systems and data storage management.

### Solution:
- **Manual Installation**: Provided steps for manual installation of Ollama.
- **Disk Quota Management**: Directed the user to relevant documentation and resources for managing disk quotas.
- **SGLANG Setup**: Set up a Conda environment with SGLANG, which supports tensor parallelism and batching for higher throughput.
- **Endpoint Access**: Explained the process for accessing the endpoint and provided a sample script for optimal resource usage.

### Conclusion:
The customer's request was resolved by setting up an efficient inference setup with SGLANG, providing guidance on disk quota management, and explaining the process for accessing the endpoint.
---

### 2025011442003246_Early-Access%20Helma%20%22Maximilian%20Esser%22%20_%20k107ce21.md
# Ticket 2025011442003246

 # HPC Support Ticket Conversation Summary

## Keywords
- Early-Access Helma
- Multi-GPU and Multi-Node
- FEAT3
- OpenMPI with CUDA aware communication
- UCX library
- Spack
- Matrix channel
- Login-Node
- Jumphost
- Parallel file system

## General Learnings
- **User Requirements**:
  - Software: FEAT3 (in-house FEM software), gcc compiler, cmake, OpenMPI with CUDA aware communication, CUDA, Boost, CGAL, ParMETIS
  - Job Size: ~0.5-10TB main memory
  - Communication: MPI + X, asynchronous neighbor-to-neighbor communication, global reduction operations
  - IO: Low intensity, common file read at the beginning, parallel write out of vtk files at the end

- **Issues**:
  - UCX library provided with Spack on Alex Nodes cannot handle GPU aware communication routines effectively.

- **Admin Actions**:
  - Granted access to Helma and invited the user to the Matrix channel.
  - Provided login details and information about available file systems.
  - Set a temporary limit of 16 GPUs (4 nodes) per group.

- **Potential Solutions**:
  - Install and configure a more recent UCX library to resolve GPU aware communication issues.

- **Follow-up**:
  - User should read the Matrix channel backlog and engage in the community for further assistance.
  - Adjust GPU limits based on system stability.

This summary provides key information for HPC support employees to address similar issues in the future, focusing on software requirements, communication frameworks, and potential solutions for library configuration problems.
---

### 2025010242000799_Early-Access%20Helma%20%22Anton%20Vlasjuk%22%20_%20b185cb16.md
# Ticket 2025010242000799

 # HPC Support Ticket Conversation Analysis

## Keywords
- Account expiration
- Resource allocation
- Team management
- HPC access
- Matrix channel
- Login node
- Jumphost
- Dateisysteme

## General Learnings
- **Account Expiration**: Ensure user accounts are up-to-date to avoid access issues.
- **Resource Management**: Clarify resource needs and team roles to avoid misunderstandings.
- **Communication**: Use clear and concise communication to address user concerns and provide solutions.

## Root Cause of the Problem
- The user's HPC account had expired, preventing access to the Helma system.
- There was a misunderstanding about the user's request for resource management within an existing team, which was initially interpreted as a request for additional resources.

## Solution
- The user's account was renewed, allowing access to the Helma system.
- The HPC Admin clarified the login process and provided access to the Matrix channel for further communication.
- The user was informed about the login node and jumphost for accessing the system.

## Documentation for Support Employees
When handling similar issues, ensure the following steps:
1. **Check Account Status**: Verify if the user's account is active and up-to-date.
2. **Clarify Resource Needs**: Understand the user's request for resource management within their team.
3. **Provide Access Information**: Inform the user about the login process, including login nodes and jumphosts.
4. **Communication Channels**: Ensure the user has access to relevant communication channels, such as Matrix, for further support.

By following these steps, support employees can effectively address account-related issues and ensure users have the necessary access and resources for their projects.
---

### 2024121942001685_Early-Access%20Helma%20%22Vladyslav%20Kogan%22%20_%20tunu108h.md
# Ticket 2024121942001685

 ```markdown
# HPC Support Ticket: Early-Access Helma

## Summary
- **User**: Vladyslav Kogan (tunu108h)
- **Contact**: vladyslav.kogan@utn.de, @elad07oc:utn.de
- **Institution**: University of Technology Nuremberg
- **Application**: Training of LLMs for AI labs and courses (Computer Vision, LLMs, Robotics)

## Issues and Solutions

### Issue 1: SSH Access Denied
- **Problem**: User unable to access Helma cluster, receiving "Permission denied" error.
- **Root Cause**: SSH configuration bug on Helma not accepting the user's account.
- **Solution**: SSH configuration corrected and server restarted.

### Issue 2: Matrix Backlog Not Visible
- **Problem**: User unable to see Matrix backlog, messages encrypted.
- **Root Cause**: Unknown, possibly due to Matrix client/homeserver configuration.
- **Solution**: Provided a summary of the chat from the first days on an external pad.

## Key Points
- **Access Granted**: User's access to Helma cluster was granted.
- **Login Node**: "helma.nhr.fau.de", accessible via IPv6 or Jumphost csnhr.nhr.fau.de.
- **GPU Limits**: Initially limited to 16 GPUs (4 nodes), to be adjusted based on stability.
- **Matrix Invitation**: User invited to Matrix channel, encouraged to read backlog and participate.
- **Date Systems**: All known date systems from Alex are available on Helma.

## Additional Information
- **Test Phase and Future Plans**: User inquired about the duration of the test phase and future plans for Helma cluster.
- **High Computational Needs**: User mentioned high computational requirements and potential use of RRZE as a long-term solution.

## Follow-up
- **SSH Access**: Confirmed that SSH access issue was resolved after server restart.
- **Matrix Backlog**: User found the provided chat summary helpful.

## Conclusion
- **Successful Resolution**: SSH access issue resolved, Matrix backlog issue partially addressed with a summary.
- **Future Considerations**: User interested in long-term use of Helma cluster due to high computational needs.
```
---

### 2025012042002815_Early-Access%20Helma%20%22Dominik%20Wagner%22%20_%20b196ac10.md
# Ticket 2025012042002815

 # HPC Support Ticket Conversation Analysis

## Keywords
- Early Access
- Helma
- GPU-hours
- Python
- Cuda
- Pytorch DDP/FSDP
- Apache Arrow
- MosaicML Streaming
- Huggingface datasets
- Audio datasets
- Preprocessing
- I/O intensity
- Matrix-Kanal
- Login-Node
- Jumphost
- Dateisysteme

## General Learnings
- **Early Access Request**: The user applied for early access to the Helma cluster for their research group.
- **Resource Requirements**: The user requested ~10,000 GPU-hours and specified software needs (Python >= 3.8, Cuda >= 12.1).
- **Application Details**: The user's work involves single-node multi-GPU environments and distributed training using Pytorch DDP or FSDP. They handle large audio datasets using Apache Arrow and streaming dataset implementations.
- **Data Handling**: Preprocessing steps create high but temporary I/O intensity. Data needs to be rsynced from TH Nürnberg to Helma.
- **Access Granted**: The HPC Admin granted access to Helma and provided login details and instructions for using the Matrix channel.
- **User Response**: The user acknowledged the quick response and planned to move their scripts and data to Helma.

## Root Cause of the Problem
- The user needed early access to the Helma cluster for their research, including specific software and hardware requirements.

## Solution
- The HPC Admin granted access to Helma and provided necessary login information and instructions for using the Matrix channel and accessing the cluster.

## Documentation for Support Employees
- **Early Access Requests**: Ensure users provide detailed information about their resource and software requirements.
- **Data Transfer**: Advise users on efficient data transfer methods, such as rsync, for large datasets.
- **Matrix Channel**: Encourage users to engage with the Matrix channel for additional support and community interaction.
- **Login Instructions**: Provide clear instructions for accessing the cluster, including login nodes and jumphosts.

This documentation can be used to handle similar early access requests and ensure users are properly onboarded to the HPC cluster.
---

### 2025012442002433_Early-Access%20Helma%20%22Arlind%20Kadra%22%20_%20b250be12.md
# Ticket 2025012442002433

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Keywords
- Early-Access Helma
- GPU-hours
- Software: transformers, trl, torch
- Multi-GPU
- Data storage at HPC
- NHR@FAU
- Matrix-Kanal
- Slurm-Association
- Resource Allocation Board
- Scientific Steering Committee
- UTN nodes
- BayernKI resources
- Early access test phase
- NHR Helma node
- Utilization rate
- Shareholders
- Dynamic resource allocation
- Static reservations

## General Learnings
- **Access and Account Management**: The ticket involves setting up access for a PhD student to the Helma cluster, including specific software requirements and GPU-hours.
- **Resource Allocation**: Discussions on resource allocation between different projects and funding sources (NHR, UTN, BayernKI).
- **Early Access Phase**: The cluster is in an early access phase, and access may be revoked or adjusted based on future decisions by the Resource Allocation Board.
- **Utilization and Priority**: The cluster operates at high utilization, and priority access is managed dynamically with occasional static reservations for specific users.
- **Communication and Clarification**: Importance of clear communication between the user and HPC admins to clarify access and resource allocation.

## Root Cause of the Problem
- **Access Clarification**: The main issue revolves around clarifying the access rights for the PhD student, specifically whether they should have access to UTN resources or only general NHR nodes.

## Solution
- **Access Granted**: The PhD student was granted access to Helma with a general NHR account, with access to UTN resources blocked during the early access phase.
- **Dynamic Resource Allocation**: The HPC admins proposed continuing with dynamic resource allocation to balance the needs of all groups while maintaining high utilization rates.
- **Clarification on UTN Resources**: The UTN resources are included in the Helma cluster, but access is managed based on the project's funding and resource allocation policies.

## Documentation for Support Employees
- **Access Setup**: Ensure that new users are granted appropriate access based on their project's funding and resource allocation policies.
- **Resource Allocation**: Be aware of the dynamic resource allocation policies and the utilization rates of the cluster.
- **Communication**: Maintain clear communication with users to clarify their access rights and resource allocation.
- **Early Access Phase**: Be prepared for potential changes in access and resource allocation as the cluster transitions from the early access phase to production mode.
```
---

### 2024121842001605_Early-Access%20Helma%20%22Timy%20Phan%22%20_%20v104dd19.md
# Ticket 2024121842001605

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Keywords
- Early-Access Helma
- GPU hours
- Software requirements
- Multi-GPU/Multi-node
- IO intensity
- Data location
- Login-Node
- Jumphost
- Dateisysteme
- Matrix-Kanal

## What Can Be Learned

### User Requirements
- **Compute Resources**: Approximately 18,000 GPU hours.
- **Software**:
  - Centrally installed: (mini)conda, Cuda-12.X
  - User-installed: NATTEN, pip dependencies
- **Application**:
  - Multi-GPU/Multi-node
  - Typical job size: 4-16 GPUs
  - Libraries: torch DDP, deepspeed, accelerate
  - IO intensity: webdataset loading, ca. 1Gb/s ingress
  - Data location: /home/atuin/v104dd/v104dd10/

### HPC Admin Response
- **Access Granted**: User access to Helma has been enabled.
- **Matrix Channel**: User invited to the Matrix channel; advised to read the backlog.
- **Login Information**:
  - Login-Node: helma.nhr.fau.de
  - Access: via IPv6 directly or through Jumphost csnhr.nhr.fau.de
- **File Systems**: All known file systems from Alex are available on Helma.
- **Initial Limits**: User limited to 16 GPUs (4 nodes) for the first few days; limits will be adjusted if everything runs smoothly.

### Additional Notes
- **IO Intensity**: Concerns raised about webdataset loading and data location.

### Root Cause of the Problem
- User requires specific software and compute resources for multi-GPU/multi-node applications.

### Solution
- HPC Admins granted access and provided necessary login information.
- User advised to engage in the Matrix channel for further support and updates.
```
---

### 2024121142000021_Early-Access%20Helma%20%22Jan%20Pfister%22%20_%20jap86cx%40uni-wuerzburg.de.md
# Ticket 2024121142000021

 ```markdown
# HPC Support Ticket Conversation Analysis

## Keywords
- Early-Access Helma
- GPU-hours
- Software: Cuda, Python, Torch, Transformers
- Application: Single-GPU vs. Multi-GPU/Multi-node
- IO intensity
- Logfile-Schreiben
- FlashAttention 2 and 3
- CUDA error: an illegal memory access was encountered
- DDT-Debugger
- SSH-Problem
- MI300X, MI300A GPUs

## General Learnings
- **User Requirements**: The user requires extensive GPU resources for training large language models (LLMs). They use specific software libraries such as Cuda, Python, Torch, and Transformers.
- **Initial Setup**: The user was granted access to the Helma cluster and provided with an initial GPU limit. They were also given access to the Matrix channel for further communication.
- **Performance Issues**: The user encountered performance issues related to log file writing, which was slowing down the training process. The log files were reduced to mitigate this issue.
- **Scaling and Testing**: The user scaled their model and tested different configurations, including FlashAttention 2 and 3. They encountered errors during scaling, particularly with FlashAttention 3.
- **Resource Limits**: The user requested an increase in GPU limits to run parallel debug and evaluation jobs without canceling the main training job.
- **SSH Issues**: There were SSH-related problems that were identified and addressed by the HPC Admins.
- **Debugger Availability**: The DDT-Debugger was made available, although its effectiveness for the specific CUDA error was uncertain.
- **New Hardware Access**: The user was granted access to new GPU hardware (MI300X and MI300A) on the test cluster for further testing.

## Root Causes and Solutions
- **Logfile-Schreiben**: The log file writing was slow due to the high IO intensity. The solution was to reduce the logging and use a background process to synchronize logs to a persistent storage.
- **FlashAttention 3 Error**: The user encountered a CUDA error related to illegal memory access when scaling the model with FlashAttention 3. The root cause was not fully identified, but the user planned to continue testing and debugging.
- **SSH-Problem**: The SSH issue was related to the login node not recognizing SSH public keys uploaded to the HPC portal. The solution was to ensure that the compute nodes also recognize these keys.

## Conclusion
The conversation highlights the importance of efficient resource management, debugging tools, and communication between users and HPC Admins. The user's requirements were met through a series of adjustments and troubleshooting steps, ensuring that their large-scale training jobs could proceed smoothly.
```
---

### 2025021942003235_Early-Access%20Helma%20%22Olga%20Grebenkova%22%20_%20v104dd15.md
# Ticket 2025021942003235

 # HPC Support Ticket Conversation Summary

## Keywords
- Early-Access Helma
- Matrix Channel
- Login Node
- Jumphost
- Dateisysteme
- Python
- PyTorch
- CUDA
- GCC
- Multi-GPU/Multi-node

## General Learnings
- **Access Granted**: User access to Helma cluster was enabled.
- **Matrix Channel**: User received an invitation to the Matrix channel and was advised to read the backlog.
- **Login Node**: Login node for the cluster is `helma.nhr.fau.de`.
- **Jumphost**: Access via IPv6 directly or through the jumphost `csnhr.nhr.fau.de`.
- **Dateisysteme**: All known dateisysteme from Alex are available on Helma.
- **Required Software**: User specified the need for Python, PyTorch, CUDA, and GCC.
- **Application**: User intends to use the cluster for multi-GPU/multi-node applications with sharded datasets.

## Root Cause of the Problem
- User required access to the Helma cluster and specific software for their application.

## Solution
- Access was granted to the Helma cluster.
- User was provided with login details and instructions for accessing the cluster.
- User was invited to the Matrix channel for further support and communication.

## Additional Notes
- The user was allocated 3000 GPU-hours for their application.
- A summary of the Matrix channel backlog is available at [this link](https://pad.nhr.fau.de/dfZHvN8-RcSA0VjX17qJgw?both).

---

This summary provides a quick reference for support employees to understand the process and solutions for similar access requests and software requirements.
---

### 2025022642002848_Early-Access%20Helma%20%22Elena%20Izzo%22%20_%20v115be16.md
# Ticket 2025022642002848

 ```markdown
# HPC-Support Ticket Conversation Summary

## Subject: Early-Access Helma

### Keywords:
- Early-Access
- Helma
- Matrix-Kanal
- Login-Node
- Jumphost
- Dateisysteme
- GPU hours
- Python
- PyTorch
- Conda environment
- Multi-GPU
- Distributed data parallel
- Pytorch Distributed

### General Learnings:
- **Access Granted**: The user's access to Helma was activated.
- **Matrix Channel**: The user received an invitation to the Matrix channel and was advised to read the backlog.
- **Login Information**: The login node for the cluster is `helma.nhr.fau.de`, accessible via IPv6 directly or through the Jumphost `csnhr.nhr.fau.de`.
- **File Systems**: All known file systems from Alex are available on Helma.
- **Resource Allocation**: The user requested 400 GPU hours.
- **Software Requirements**: The user primarily uses Python and PyTorch libraries, creating a conda environment for necessary packages like PyTorch, wandb, math, numpy, and torchvision.
- **Application Details**: The user's work involves Multi-GPU setups, mainly using 2 GPUs with distributed data parallel strategies. Jobs range from a few hours to multiple days, utilizing Pytorch Distributed as the communication framework.

### Root Cause of the Problem:
- No specific problem was mentioned in the provided conversation.

### Solution:
- No solution was required as the conversation focused on access and resource allocation.
```
---

### 2024121142001663_Early-Access%20Helma%20%22Tobias%20J%C3%BClg%22%20_%20v108be12.md
# Ticket 2024121142001663

 # HPC Support Ticket Analysis

## Keywords
- Early-Access Helma
- GPU hours
- Conda version
- CUDA
- Jaxlib
- PyTorch
- TensorFlow
- JAX
- High IO throughput
- Workspaces
- Multi-node training
- Torch distributed
- Jax distributed
- NCCL backend
- Matrix-Kanal
- Login-Node
- Jumphost
- Dateisysteme
- Workspace management
- GPU limit

## Summary
- **User Request**: Access to Helma for approximately 1000 GPU hours. Requires the latest Conda version for installing specific CUDA and Jaxlib versions, along with PyTorch, TensorFlow, and JAX libraries. High IO throughput needed for large datasets stored in workspaces. Interested in multi-node training with larger batch sizes using Torch distributed and Jax distributed with NCCL backend.
- **HPC Admin Response**: Access granted to Helma with an invitation to the Matrix channel. Login node is "helma.nhr.fau.de" with access via IPv6 or Jumphost. All known dateisystems from Alex are available on Helma. Workspace management commands are currently missing on Helma; use Alex for now. Initial GPU limit set to 16 GPUs (4 nodes).

## Root Cause of the Problem
- Outdated Conda version on Alex, necessitating the installation of a personal Miniconda.
- Need for high IO throughput and multi-node training capabilities.

## Solution
- Access to Helma with the latest Conda version and necessary software support.
- Temporary use of Alex for workspace management until commands are available on Helma.
- Initial GPU limit set with plans to adjust based on stability.

## General Learnings
- Importance of up-to-date software versions for specific user requirements.
- Integration of new clusters (Helma) with existing systems (Alex) for seamless user experience.
- Initial resource limits to ensure stability before scaling up.
- Use of Matrix channels for communication and support.
---

### 2025012142002144_Early-Access%20Helma%20%22ABHIJEET%20KISHORE%20NAYAK%22%20_%20v106be14.md
# Ticket 2025012142002144

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Keywords
- Early-Access Helma
- GPU-hours
- Torch
- Python
- Multi-gpu
- Multi-node
- Matrix-Kanal
- Login-Node
- Jumphost
- Dateisysteme

## Summary
- **User Request**:
  - Contact: User requested access to Helma with 80 GPU-hours.
  - Required Software: Torch, Python.
  - Application: Multi-gpu, multi-node.

- **HPC Admin Response**:
  - Access granted to Helma.
  - Invitation to Matrix-Kanal provided.
  - Login-Node: `helma.nhr.fau.de`.
  - Access via IPv6 or Jumphost `csnhr.nhr.fau.de`.
  - All known Dateisysteme from Alex are available on Helma.

## Lessons Learned
- **Access and Setup**:
  - Users need to be granted access to Helma and invited to the Matrix-Kanal.
  - Important to read the Channel-Backlog for initial setup and information.
  - Login-Node and Jumphost details are crucial for accessing the cluster.

- **Software and Hardware**:
  - Users may require specific software (e.g., Torch, Python) for their applications.
  - Multi-gpu and multi-node setups are supported.

- **Communication**:
  - Matrix-Kanal is used for communication and support.
  - Summary of the backlog is available for quick reference.

## Root Cause and Solution
- **Root Cause**: User needed access to Helma for specific computational tasks.
- **Solution**: Access granted, invitation to Matrix-Kanal, and details provided for login and software availability.
```
---

### 2024121942003067_Early-Access%20Helma%20%22Anselm%20Horn%22%20_%20mfbi05.md
# Ticket 2024121942003067

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Keywords
- Early-Access Helma
- GPU hours
- Amber24
- pmemd.cuda
- pmemd.cuda.dpfp
- Single-GPU jobs
- Chain jobs
- I/O-intensive
- Energetic structure minimizations
- Step-by-step heating
- Production molecular dynamics runs
- Fibrillar protein system
- Matrix-Kanal
- Login-Node
- Jumphost
- Dateisysteme
- FAU-intern
- IPv6
- Homeserver
- Client
- Backlog

## General Learnings
- **User Requirements**: The user requested access to the Helma cluster for a project involving molecular dynamics simulations using Amber24, specifically the pmemd.cuda and pmemd.cuda.dpfp executables.
- **Resource Allocation**: The user estimated needing between 5000-10000 GPU hours and intended to run several single-GPU jobs simultaneously as chain jobs.
- **Application Details**: The project involves energetic structure minimizations and step-by-step heating using double precision, followed by production molecular dynamics runs using single precision.
- **I/O Considerations**: The user planned to minimize I/O intensity by reducing the writing of intermediate results.
- **Advanced Setup**: The project involves a large fibrillar protein system requiring advanced initial structural setup.

## HPC Admin Response
- **Access Granted**: The user's access to the Helma cluster was granted, and an invitation to the Matrix channel was sent.
- **Login Information**: The login node is "helma.nhr.fau.de," accessible internally or via IPv6, with a jumphost option for external access.
- **File Systems**: All known file systems from Alex are available on Helma.
- **Initial Limits**: Users are initially limited to 16 GPUs (4 nodes) for the first few days, with plans to adjust the limit if everything runs smoothly.

## Root Cause and Solution
- **Root Cause**: The user needed access to specific software and computational resources for a complex molecular dynamics project.
- **Solution**: The HPC Admin granted access to the required resources and provided necessary login and usage information.
```
---

### 2025010742001994_Early-Access%20Helma%20%22Foivos%20Paraperas%20Papantoniou%22%20_%20b180dc22.md
# Ticket 2025010742001994

 ```markdown
# HPC Support Ticket: Early-Access Helma

## Keywords
- Early-Access Helma
- GPU hours
- Conda environments
- Multi-GPU
- Multi-Node
- Pytorch
- High IO intensity
- Matrix-Kanal
- Login-Node
- Jumphost
- Dateisysteme

## Summary
- **User Request**: Access to Helma for multi-GPU and multi-node training jobs with high IO intensity.
- **Required Resources**: 10K GPU hours, 80GB memory per GPU.
- **Software**: Conda environments for Python code.
- **Data Location**: Training data in `/anvme/workspaces/...`.

## HPC Admin Response
- **Access Granted**: User access to Helma enabled.
- **Matrix Channel**: Invitation sent to Matrix channel with a recommendation to read the backlog.
- **Login Information**:
  - Login-Node: `helma.nhr.fau.de`
  - Access: FAU-intern, IPv6, or via Jumphost `csnhr.nhr.fau.de`
  - Dateisysteme: All known dateisysteme from Alex are available on Helma.

## General Learnings
- **Access Procedure**: Users are granted access to Helma and invited to the Matrix channel for further communication and support.
- **Login Details**: Important to provide clear instructions on how to access the cluster, including login nodes and jumphosts.
- **Software Environment**: Users can set up their own software environments using tools like Conda.
- **Resource Allocation**: Users specify their resource needs, such as GPU hours and memory requirements, which are considered during access provisioning.

## Root Cause and Solution
- **Root Cause**: User needed access to Helma for specific resource-intensive tasks.
- **Solution**: Access granted with detailed instructions on how to log in and utilize the available resources.
```
---

### 2025021842002069_Early-Access%20Helma%20%22Suprosanna%20Shit%22%20_%20553131353838343702%40uzh.ch.md
# Ticket 2025021842002069

 # HPC Support Ticket Analysis

## Keywords
- Matrix ID
- HPC Account
- Helma Cluster
- GPU Hours
- Software Requirements
- Multi-GPU/Multi-node
- Conda Environment
- Mamba
- PyTorch
- Sci-kit
- NCCL
- CUDA
- GPU Driver
- Scratch Storage

## Summary
- **Issue**: User did not specify their Matrix ID, leading to confusion as the provided ID belonged to a professor.
- **Root Cause**: User was unable to create a Matrix ID without an FAU email ID.
- **Solution**: HPC Admin enabled the user's HPC account despite the Matrix ID issue. The admin also informed the user that Matrix accounts from any home server are accepted.
- **Learning**:
  - Matrix IDs can be created using any public provider, not just the institution's email.
  - HPC Admins can enable accounts even if there are minor issues with the provided information.
  - Important to read the channel backlog and summary for useful information.
  - Login to Helma cluster via IPv6 directly or through the Jumphost.
  - All known date systems are available on Helma.

## Software and Hardware Requirements
- **Required Software**: CUDA, GPU driver, NCCL, Conda environment with Mamba, Python packages (PyTorch, Sci-kit, etc.)
- **Hardware Requirements**: Multi-GPU/Multi-node setup, 8 GPUs, 64 CPU threads
- **Storage**: Scratch storage for data

## Additional Notes
- Multi-GPU communication is done using NCCL.
- IO intensity is optimized via pin memory in data loader.
- Typical job runs for a week.

## Follow-up
- User should create their own Matrix ID using a public provider if they do not have access to an FAU email ID.
- User should review the channel backlog and summary for important information.
---

### 2024121242002802_Early-Access%20Helma%20%22Joel%20Schlotthauer%22%20_%20iwal180h.md
# Ticket 2024121242002802

 # HPC Support Ticket Conversation: Early-Access Helma

## Keywords
- Early-Access Helma
- GPU-hours
- Benchmarking
- Multi-node scalability
- Large scale LLM training
- Cuda > 12
- Python >= 3.9
- NCCL
- Matrix-Kanal
- Login-Node
- Dateisysteme
- Stabilitätsprobleme
- Matrix-Chat
- IdM Account
- Weihnachtszeit
- 24h Limit
- Nodes Limit

## Summary
- **User Request:** Access to Helma for benchmarking and stress-testing with a focus on multi-node scalability and large-scale LLM training.
- **Required Software:** Cuda > 12, Python >= 3.9.
- **Job Details:** Multi-GPU/Multi-node, job size up to 23 days, I/O intensity peaks during checkpoint writing, communication framework NCCL.
- **Data:** 10TB raw data, checkpoints up to 45TB.
- **Additional Requests:** Temporary increase in 24h limit and node limit over the Christmas period.

## Conversation Highlights
- **Initial Access:** Users were granted access to Helma with initial limits of 16 GPUs (4 nodes) per user.
- **Matrix-Chat:** Users were informed about the importance of Matrix-Chat for receiving updates and were invited to join.
- **Performance Feedback:** Users reported positive experiences with Helma, noting no stability issues and high performance.
- **Resource Limits:** Users requested an increase in the 24h limit and node limit over the Christmas period, which was denied due to high cluster usage.

## Root Cause of Problems
- **Resource Limitation:** The cluster was heavily utilized, making longer runtimes and higher node limits unrealistic.

## Solutions
- **Matrix-Chat:** Users were provided with Matrix-Chat invitations to stay updated on cluster information.
- **Resource Management:** HPC Admins adjusted user limits to group limits and dynamically managed them over the Christmas period.

## General Learnings
- **Communication:** Matrix-Chat is essential for staying updated on cluster information.
- **Resource Allocation:** Cluster resources are limited and need to be managed dynamically based on usage.
- **User Feedback:** Positive user experiences can be shared to improve cluster performance and user satisfaction.

## Conclusion
- **User Satisfaction:** Users were satisfied with the performance and stability of Helma.
- **Resource Management:** HPC Admins effectively managed resource allocation to ensure fair usage among groups.
- **Communication:** Matrix-Chat was emphasized as a crucial tool for staying informed about cluster updates.
---

### 2025030342002497_Early-Access%20Helma%20%22Jinho%20Kim%22%20_%20b143dc19.md
# Ticket 2025030342002497

 ```markdown
# HPC Support Ticket Conversation Summary

## Subject
Early-Access Helma "Jinho Kim" / b143dc19

## Keywords
- Early Access
- Helma Cluster
- Matrix Channel
- Login Node
- Jumphost
- CUDA
- PyTorch
- GPU Hours
- Multi-GPU
- Data Workspace

## Summary
- **Access Granted**: User's access to Helma cluster was enabled.
- **Matrix Channel**: User received an invitation to the Matrix channel and was advised to read the backlog.
- **Login Node**: Login node for the cluster is `helma.nhr.fau.de`.
- **Access Methods**: Accessible via FAU-intern, IPv6, or through the Jumphost `csnhr.nhr.fau.de`.
- **File Systems**: All known file systems from Alex are available on Helma.
- **Software Requirements**:
  - Central Installation: CUDA 11.8
  - User Installation: PyTorch, PyTorch-Lightning, Cupy, Sigpy
- **Application Details**:
  - Multi-GPU with a single node
  - Full GPU memory
  - Low IO intensity (higher for GradientCheckpointing)
  - Data in workspace

## Root Cause of the Problem
- User required access to the Helma cluster and specific software installations.

## Solution
- Access was granted to the Helma cluster.
- User was provided with necessary information for access and software installation guidelines.

## General Learnings
- **Access Procedures**: Understanding the process for granting access to new clusters.
- **Communication Channels**: Importance of Matrix channels for user support and information sharing.
- **Software Requirements**: Handling user-specific software needs and central installations.
- **Cluster Access**: Different methods for accessing the cluster, including internal networks and jumphosts.

## References
- [Matrix Channel Backlog Summary](https://pad.nhr.fau.de/dfZHvN8-RcSA0VjX17qJgw?both)
- [NHR@FAU Website](https://hpc.fau.de)
```
---

### 2025031342002272_Early-Access%20Helma%20%22Eman%20Bagheri%22%20_%20iwst111h.md
# Ticket 2025031342002272

 # HPC Support Ticket: Early-Access Helma

## Keywords
- Early Access
- Helma
- GPU System
- H100/96GB
- Matrix Account
- FAU
- NHR@FAU
- GPU-hours
- Software Requirements
- Login Node
- Jumphost

## Summary
The HPC Admin offered early access to the next-generation GPU system Helma with 4x H100/96GB per node. The user expressed interest and provided details about their computational needs and software requirements. The HPC Admin recommended creating a Matrix account for communication and provided access details for the Helma cluster.

## Details
- **Offer**: Early access to Helma GPU system.
- **User Response**: Interested in early access for porting simulations to GPUs.
- **Requirements**:
  - GPU-hours: Upwards of 20,000 GPU-H
  - Software: gcc, ucx/gcc-cuda, openmpi, mkl, cuda
  - Application: Multiple nodes, not IO intensive, large snapshots written hourly.
- **Communication**: Matrix account recommended for updates.
- **Access**:
  - Login Node: helma.nhr.fau.de
  - Access: FAU-intern, IPv6, or via Jumphost csnhr.nhr.fau.de
  - File Systems: All known file systems from Alex are available on Helma.

## Solution
- User provided Matrix account ID for communication.
- HPC Admin granted access to Helma and provided login details.
- User advised to read the Matrix channel backlog and summary for additional information.

## Notes
- The user was advised to create a Matrix account for better communication regarding early access updates.
- Access to Helma was granted, and the user was provided with login details and instructions for accessing the cluster.
- The user was encouraged to participate in the Matrix channel and read the backlog for more information.
---

### 2025021142003401_Early-Access%20Helma%20%22Siyuan%20Mei%22%20_%20iwi5070h.md
# Ticket 2025021142003401

 # HPC Support Ticket Analysis

## Keywords
- Early-Access Helma
- Data format
- Small files
- Guidelines
- Python, Anaconda, PyTorch
- GPU hours
- Computer vision research

## Summary
- **User Issue**: User requested early access to Helma for computer vision research but was denied due to non-compliance with data handling guidelines.
- **Root Cause**: User's data consisted of several thousand small files, which is not efficient for HPC storage and processing.
- **Solution**: User was advised to change the data format according to the guidelines provided in the documentation.

## Lessons Learned
- **Data Handling**: Ensure that data is stored in an efficient format, avoiding a large number of small files.
- **Guidelines Compliance**: Users must follow the data handling guidelines provided by the HPC center to optimize resource usage.
- **Documentation**: Refer users to relevant documentation for best practices in data management.

## Relevant Links
- [Data Handling Guidelines](https://doc.nhr.fau.de/data/datasets/)

## Next Steps
- **User Action**: Change data format as per guidelines.
- **HPC Admin Action**: Reevaluate the Helma application once the user demonstrates better data handling.

---

This analysis provides a concise overview of the issue, the root cause, the solution, and the steps to be taken to resolve similar issues in the future.
---

### 2025021442000836_Early-Access%20Helma%20%22Deepak%20Charles%20Chellapandian%22%20_%20mfdk103h.md
# Ticket 2025021442000836

 ```markdown
# HPC-Support Ticket Conversation Summary

## Subject: Early-Access Helma

### Keywords:
- Early-Access Helma
- Matrix-Kanal
- Login-Node
- Jumphost
- FAU-intern
- IPv6
- GPU hours
- libtorch
- CUDA
- Triton
- Anaconda
- Apptainer (Singularity)
- Multi-GPU/Multi-node
- NCCL
- HPCVAULT
- IOPS
- NCCL parallel simulation
- libtorch
- CUDA developer

### Key Learnings:
- **Access Granted**: The user's access to Helma has been activated.
- **Matrix Channel**: The user received an invitation to the Matrix channel and was advised to read the channel backlog.
- **Login Information**: The login node for the cluster is `helma.nhr.fau.de`. Access is available internally at FAU, via IPv6 directly, or through the jump host `csnhr.nhr.fau.de`.
- **File Systems**: All known file systems from Alex are also available on Helma.
- **Resource Requirements**: The user requested 72 GPU hours per week with a minimum walltime. The number of nodes and GPU configuration may vary.
- **Software Requirements**: The user needs `libtorch`, `CUDA`, `Triton`, `Anaconda`, and `Apptainer (Singularity)`. The user will bring their own container.
- **Application Details**: The user is working on a multi-GPU/multi-node application using NCCL for parallel simulation, with less than 100 IOPS for minimum write, and using HPCVAULT.
- **Project Title**: "Development of Distributed, Data parallel Fourier Domain Bloch Simulator".
- **User Experience**: The user is an experienced CUDA developer trying to port techniques with libtorch and NCCL.

### Root Cause of the Problem:
- The user needed access to the Helma cluster and specific software for their project.

### Solution:
- The HPC Admin granted access to the Helma cluster and provided necessary login information and software availability details.
```
---

### 2025022142001198_Early-Access%20Helma%20%22Christian%20Frey%22%20_%20b250be10.md
# Ticket 2025022142001198

 # HPC Support Ticket Conversation Summary

## Keywords
- Early Access
- Helma Cluster
- Matrix Channel
- Login Node
- Jumphost
- Python Projects
- GPU Hours
- Libraries
- Single-GPU Projects
- Data Inputs

## General Learnings
- **Access Granted**: User's access to the Helma cluster was activated.
- **Matrix Channel**: User received an invitation to the Matrix channel and was advised to read the backlog.
- **Login Information**: Login node details and access methods (IPv6 or Jumphost) were provided.
- **File Systems**: All known file systems from Alex are available on Helma.
- **Software Requirements**: User specified Python projects and a list of required libraries.
- **GPU Usage**: User requested 200-400 GPU hours for single-GPU projects.
- **Data Location**: User's data is located in the vault, with inputs around 5GB.

## Root Cause of the Problem
- User needed access to the Helma cluster and specific software libraries for their Python projects.

## Solution
- Access was granted to the Helma cluster.
- User was provided with login details and instructions for accessing the Matrix channel.
- User specified the required software libraries, which can be installed centrally or by the user as needed.

## Additional Notes
- The Matrix channel backlog and summary link were provided for further information.
- User was advised to engage in the Matrix channel for additional support and information.

---

This summary can be used as a reference for future support tickets related to early access requests and software requirements on the Helma cluster.
---

### 2024121142002046_Early-Access%20Helma%20%22Julia%20Wunderle%22%20_%20b185cb13.md
# Ticket 2024121142002046

 ```markdown
# HPC Support Ticket: Early-Access Helma

## Keywords
- Early-Access Helma
- GPU-hours
- Cuda, torch, transformers
- Multi-GPU/Multi-node
- Matrix-Kanal
- Login-Node
- IPv6
- Jumphost
- Workspaces
- ws_list/ws_find
- GPU limit

## Summary
- **User Request**: Access to Helma for multi-GPU/multi-node application using Cuda, torch, and transformers.
- **HPC Admin Response**: Access granted with initial GPU limit of 16 GPUs (4 nodes), later increased to 64 GPUs (16 nodes).
- **Additional Information**: User invited to Matrix channel, login details provided, workspace management commands not yet available on Helma.

## Problem
- User requested access to Helma for a highly distributed multi-GPU/multi-node application.

## Solution
- HPC Admin granted access and provided login details.
- Initial GPU limit set to 16 GPUs (4 nodes), later increased to 64 GPUs (16 nodes) after stability was confirmed.
- User invited to Matrix channel for further support and communication.
- Workspace management commands not available on Helma; user advised to use Alex for workspace management.

## Notes
- All known date systems from Alex are available on Helma.
- Access to Helma via IPv6 or through the Jumphost csnhr.nhr.fau.de.
- Paths determined via ws_list/ws_find are accessible on Helma.
```
---

