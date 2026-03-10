# Topic 12: file_files_load_io_high

Number of tickets: 123

## Tickets in this topic:

### 2024042542004588_Fritz%20luster%20is%20frozen.md
# Ticket 2024042542004588

 # HPC Support Ticket: Lustre File System Issue

## Keywords
- Lustre
- File system
- Hang
- Access issue
- Service disruption
- High file server load

## Problem Description
- User reported issues with accessing files and directories in `/lustre/iwst/iwst087h/`.
- Commands like `ls` and file operations were hanging indefinitely.

## Root Cause
- There was an issue with the Lustre file system overnight.

## Solution
- The issue with Lustre was resolved by the HPC Admins.
- User was informed to check the latest updates on `$WORK` for service disruptions due to high file server load.

## Follow-Up
- User reported that Lustre was working but encountered similar issues with another file system (Woody).
- HPC Admins provided a link to the latest updates on service disruptions.

## Lessons Learned
- Regularly check for service disruptions and updates on the HPC website.
- Report any persistent issues to HPC Support for further investigation.

## References
- [Service Disruptions on Clusters Due to High File Server Load](https://hpc.fau.de/2024/04/19/service-disruptions-on-clusters-due-to-high-file-server-load/)
---

### 2024102542002578_Dataloder%20error%20--%20too%20slow.md
# Ticket 2024102542002578

 # HPC Support Ticket: Dataloader Latency Issue

## Keywords
- Dataloader latency
- SLURM script
- Central fileserver overload

## Problem Description
- User experiencing latency issues with dataloader while running a SLURM script on Alex.
- Suspected issue with the HPC system or user configuration.

## Root Cause
- Overloading of central fileservers by other users, affecting all users' performance.

## Solution
- No immediate solution available as the issue is caused by other users overloading the central fileservers.
- Users should be aware of potential performance degradation during peak usage times.

## General Learnings
- Performance issues with dataloaders can be caused by external factors such as fileserver overload.
- Users should monitor system performance and be prepared for potential slowdowns during high usage periods.
- HPC Admins should consider implementing measures to mitigate fileserver overload, such as usage quotas or load balancing.

## Next Steps
- HPC Admins should investigate and address the fileserver overload issue to improve overall system performance.
- Users should be informed about best practices for managing data and workloads to minimize the impact on shared resources.
---

### 2025030542002064_reducing%20load%20on%20atuin%20%5Bb233cb10%5D.md
# Ticket 2025030542002064

 ```markdown
# HPC Support Ticket: Reducing Load on Atuin Filesystem

## Keywords
- High load
- Atuin filesystem
- ANVME workspaces
- Data loading speed
- Job cancellation

## Problem
- User's jobs causing high load on the Atuin filesystem.
- Slow data loading speed observed by the user.

## Solution
- **Recommendation**: Move data to ANVME workspaces to reduce load and potentially speed up jobs.
- **Resources**:
  - Documentation: [ANVME Workspaces](https://doc.nhr.fau.de/data/workspaces/)
  - Recording: [HPC Café (October 8, 2024)](https://hpc.fau.de/teaching/hpc-cafe/#HPC-Caf%C3%A9-2024)

## Actions Taken
- User acknowledged the issue and canceled the job.
- User agreed to implement the workspace solution.

## General Learning
- High load on filesystems can be mitigated by using appropriate workspaces.
- Documentation and training resources are available to assist users in optimizing their workflows.

## Ticket Status
- Closed
```
---

### 2023051242001828_High%20load%20on%20_home_saturn%20-%20iwai006h.md
# Ticket 2023051242001828

 # HPC Support Ticket: High Load on /home/saturn

## Keywords
- High load
- Fileserver Saturn
- Job running on Alex
- Large number of files
- Shared file system
- Best practice guide
- Data archives
- Hierarchical data format (HDF5)
- $TMPDIR
- IO wait

## Problem
- **Root Cause:** A job running on Alex (a0903; 735241) was causing high load on the fileserver Saturn by reading data from a directory containing approximately 700,000 files.
- **Impact:** This workload was not suitable for a shared file system and was affecting the performance and stability for all users.

## Solution
- **Recommendation:** Follow the best practice guide for file systems.
  - Use data archives or hierarchical data format (HDF5).
  - Copy the data to `$TMPDIR` at the start of the job.
- **Benefits:** This will improve job performance by reducing IO wait time and ensure stable operation for all users of the fileserver.

## Resolution
- The issue was resolved as the load on Saturn returned to normal and no jobs from the user were running anymore.
- The ticket was closed.

## General Learning
- High load on shared file systems can be caused by jobs accessing a large number of files.
- Following best practices for file systems can improve job performance and overall system stability.
- Regular monitoring and user communication are essential for maintaining a stable HPC environment.
---

### 2025022742003587_Please%20use%20%24TMPDIR%20to%20store%20your%20training%20dataset%20%5Bv104dd18%5D.md
# Ticket 2025022742003587

 # HPC Support Ticket: High I/O Patterns to File Server

## Keywords
- High I/O patterns
- File server
- Best practices
- Node-local storage
- Tar archive
- Multi-node jobs
- Slurm submit script
- HPC cafe

## Problem
- User's job on Helma (JobId 30825 and 35864) shows constant and relatively high I/O patterns to the file server (approximately 260 MB/s and 200 MB/s per node).

## Root Cause
- The user's job is causing high I/O load on the shared file server, which can impact the performance of other users' jobs.

## Solution
- **Single Node Jobs:**
  - Pack the data into an archive using `tar -cf /path-to/archive.tar /data-to-pack`.
  - Extract the data directly to the node-local storage using `cd $TMPDIR; tar -xf /path-to/archive.tar`.

- **Multi-Node Jobs:**
  - Distribute the data to each node using `srun --ntasks=$SLURM_NNODES --ntasks-per-node=1 tar -xf archive.tar -C $TMPDIR` in the Slurm submit script.

## Additional Resources
- [HPC Cafe: Efficient Packing and Handling of Large Data Sets](https://hpc.fau.de/2025/02/04/monthly-hpc-cafe-efficient-packing-and-handling-of-large-data-sets-hybrid-event/)

## Notes
- Following best practices is essential to ensure the efficient use of shared resources.
- The extraction process for large datasets (e.g., 1.5 TB) is negligible in terms of time.
- Users should be informed via email or chat to address high I/O issues promptly.
---

### 2024080842000473_long%20staging%20time%20%5Bv103fe12%5D.md
# Ticket 2024080842000473

 # HPC Support Ticket: Long Staging Time

## Keywords
- Long staging time
- Parallel copy/unpack
- Workspaces
- Tar files
- Wall time optimization

## Problem
- User's copy process for a job is consuming a significant amount of wall time.
- The user is currently using a single ~200GB tar file for the copy process.

## Root Cause
- Inefficient data handling due to the use of a single large tar file.

## Solution
- **Split the Data**: Generate new tar files with subsets of the data, creating 10-20 smaller archives.
- **Parallel Processing**: Use parallel processes to copy/unpack the smaller archives.
  ```bash
  # find the data
  STORAGE_DIR="$(ws_find <name>)"
  # the -P parameter defines the number of parallel processes, something like 4-8 should work well
  ls -1 $STORAGE_DIR | xargs -P 4-8 -I{} tar xzf {} $TMPDIR
  ```
- **Use Workspaces**: Store the tar files on a workspace at `/anvme`.
  - For more details on workspaces: [Workspaces Documentation](https://doc.nhr.fau.de/data/workspaces)

## Expected Outcome
- Reduce the time to copy data to `$TMPDIR` from >90 minutes to ~10 minutes.
- Effectively increase training time by more than 1 hour.

## General Learnings
- Large single files can significantly slow down copy processes.
- Splitting data into smaller files and using parallel processing can optimize wall time.
- Utilizing workspaces can improve data handling efficiency.

## References
- [Workspaces Documentation](https://doc.nhr.fau.de/data/workspaces)
---

### 2024031342000561__lustre%20problems.md
# Ticket 2024031342000561

 ```markdown
# HPC-Support Ticket: /lustre Filesystem Issues

## Keywords
- Lustre filesystem
- File access problems
- Freezing bash sessions
- SLURM jobs frozen
- Performance degradation
- Failover pair
- Log files
- I/O rate

## Problem Description
- User experienced issues with the /lustre filesystem since around midnight.
- Specific issues included:
  1. Repeated `ls` and `vim` commands on log files in a specific directory caused user sessions to freeze.
  2. SLURM jobs were frozen, particularly one job that was stuck reading a <100MB binary file for over 6 hours.
- No issues were reported with the home directory file system.

## Root Cause
- The failover pair `foss03+foss04` appeared to be down.
- Both nodes had console prompts but were unresponsive to keyboard inputs.
- The last log entry on `foss04` was at 01:03 with a 'could not connect' message, and on `foss03` at 01:46.

## Solution
- The /lustre filesystem became unstuck, and jobs resumed reading input files.
- Performance degradation was noted, with an I/O rate of 129.448 MB/sec instead of the expected 20,000 MB/sec.

## Lessons Learned
- Monitoring the health of failover pairs is crucial for maintaining filesystem stability.
- Performance degradation can be a symptom of underlying issues with the filesystem.
- Regular checks and prompt responses to unresponsive nodes can help mitigate prolonged downtime.
```
---

### 2018070442002349_Missbrauch%20von%20%24FASTTMP%20auf%20Emmy%20_%20bccc002h.md
# Ticket 2018070442002349

 # HPC Support Ticket: Misuse of $FASTTMP on Emmy

## Keywords
- $FASTTMP
- /dev/shm/
- Job output frequency
- Persistent storage
- qstat
- SSH

## Problem
- User's jobs were writing to $FASTTMP at high frequency (every few seconds).
- Files written include `log.lammps`, `piston.dat`, `mag_isoh2o_add2.dcd`, and `mag_isoh2o_add2.restart`.

## Root Cause
- Misunderstanding of appropriate use of $FASTTMP for high-frequency job outputs.

## Solution
- **HPC Admin** suggested using `/dev/shm/` for temporary storage due to its location in main memory.
- User should ensure files are moved to a persistent storage system before job completion.
- User modified scripts to write to `/dev/shm/` but encountered issues accessing the output.

## Steps to Access Job Output
1. Use `qstat -n` to identify the nodes assigned to the job.
2. SSH into the first node of the job.
3. Access the job's output in `/dev/shm/`.

## Example
```bash
qstat -n
ssh e1028
ls -l /dev/shm/958113.eadm/
```

## Notes
- Ensure that the job's output directory in `/dev/shm/` is correctly created and accessible.
- Verify that the job is writing to the intended location and that the files are being moved to persistent storage as required.

## Conclusion
- Proper use of temporary storage (`/dev/shm/`) and persistent storage is crucial for efficient job management.
- Understanding how to access job outputs during runtime is essential for troubleshooting and monitoring.
---

### 2024050342000817_Fritz%20_lustre%20Filesystem%20haengend%20seit%20gestern%20Nachmittag.md
# Ticket 2024050342000817

 ```markdown
# HPC Support Ticket: Lustre Filesystem Issues

## Keywords
- Lustre filesystem
- Hanging terminal sessions
- Job logs
- Reboot
- Server reset

## Problem Description
- User reported issues with the Lustre filesystem since the previous afternoon/evening.
- Terminal sessions were hanging when performing operations like `ls` or opening files on `/lustre`.
- No issues were reported on `/home`.
- User suspected that job log files were also affected.

## Root Cause
- The Lustre filesystem was experiencing issues, causing terminal sessions to hang.

## Solution
- HPC Admins reset the problematic Lustre server pair.
- The Lustre filesystem should now be functioning normally.

## Actions Taken
- User reported the issue and provided details about the affected jobs and log files.
- HPC Admins acknowledged the issue and reset the Lustre server pair.
- User confirmed the resolution of the issue.

## Lessons Learned
- Regular monitoring and quick response to filesystem issues are crucial for maintaining system stability.
- Resetting problematic server pairs can resolve hanging issues in the Lustre filesystem.
- Users should report any unusual behavior promptly to ensure timely resolution.
```
---

### 2023082842004228_Fritz%20server%20stopped%2C%20because%20of%20my%20calculations%3F.md
# Ticket 2023082842004228

 # HPC Support Ticket: Server Stoppage During Post-Processing

## Keywords
- Server stoppage
- Login node
- Post-processing calculations
- Python
- Numpy
- Pigz
- Interactive nodes
- File system issues

## Summary
A user experienced a server stoppage while running post-processing calculations and pigz on the login node. The user was also using interactive nodes simultaneously.

## Root Cause
The issue was likely related to file system issues, specifically the outtake of `/home/atuin` or `$WORK`.

## Solution
The HPC Admin suggested that the issue might be related to a known file system problem. The user was directed to a relevant announcement: [Outage of HPC services due to file system issues](https://hpc.fau.de/2023/08/29/outage-of-hpc-services-due-to-file-system-issues/).

## Lessons Learned
- Running intensive calculations on the login node can lead to server issues.
- File system problems can cause server stoppages.
- Users should be aware of ongoing file system issues and check relevant announcements.

## Recommendations
- Avoid running heavy computations on the login node.
- Regularly check HPC service announcements for any ongoing issues.
- Use batch jobs or interactive nodes for intensive calculations.
---

### 2023122042002487_Action%20required%3A%20high%20load%20on%20%24WORK%20%28_home_autin%29%20%5Bb180dc22%5D.md
# Ticket 2023122042002487

 # HPC Support Ticket: High Load on $WORK

## Keywords
- High load
- File servers
- $WORK
- Directory structure
- File system usage

## Problem Description
- User's jobs causing high load on file servers for $WORK (/home/atuin/...).
- Specific directories/files with excessive access:
  - `/home/atuin/b180dc/b180dc22/datasets/WebFace260M/WebFace260M_0`
  - `/home/atuin/b180dc/b180dc22/datasets/WebFace260M/WebFace260M_0_gfpgan`
- Filesystem on $WORK not designed to handle ~200k directories/files flat inside a directory.

## Root Cause
- Excessive number of directories/files in a flat structure causing high load on file servers.

## Solution
- User to adjust scripts/dataset to reduce pressure on $WORK.
- Recommended actions:
  - Consult colleagues for assistance.
  - Review HPC Cafe slides on proper file system usage: [HPC Cafe File Systems](https://hpc.fau.de/files/2022/01/2022-01-11-hpc-cafe-file-systems.pdf).
  - Contact HPC Admin for further assistance.

## Actions Taken
- User agreed to terminate some jobs and adjust scripts to reduce load.
- User may contact HPC Admin for additional help.

## General Learning
- Proper directory structure is crucial to avoid high load on file servers.
- Flat structures with a large number of directories/files should be avoided.
- Users should be aware of the impact of their jobs on shared resources and take corrective actions when necessary.
---

### 2024101942000573_Lustre%20file%20system%20hang.md
# Ticket 2024101942000573

 ```markdown
# HPC Support Ticket: Lustre File System Hang

## Subject
Lustre file system hang

## User Issue
- **Problem**: User experiencing issues with the Lustre file system, unable to open files, and the system freezes.
- **Disk Space**:
  ```
  Path              Used     SoftQ    HardQ    Gracetime  Filec
  FileQ    FiHaQ    FileGrace
  /home/hpc          102.5G   104.9G   209.7G        N/A  26,985
  500K   1,000K        N/A
  /home/vault        640.0G  1048.6G  2097.2G        N/A  20,517
  200K     400K        N/A
  /home/woody        117.7G  1000.0G  1500.0G        N/A   2,743
  5,000K   7,500K        N/A
  ```

## HPC Admin Response
- **Root Cause**: Lustre OSTs (lfs-OST0015-lfs-OST0017) were unavailable due to medium errors and uncorrectable I/O failures.
- **Logs**:
  ```
  [Fri Oct 18 22:23:14 2024] sd 0:0:18:0: [sdr] tag#4132 FAILED Result: hostbyte=DID_OK driverbyte=DRIVER_SENSE cmd_age=3s
  [Fri Oct 18 22:23:14 2024] sd 0:0:18:0: [sdr] tag#4132 Sense Key : Medium Error [current] [descriptor]
  [Fri Oct 18 22:23:14 2024] sd 0:0:18:0: [sdr] tag#4132 Add. Sense: Unrecovered read error
  ...
  [Fri Oct 18 22:24:06 2024] WARNING: Pool 'foss06-OST0015' has encountered an uncorrectable I/O failure and has been suspended.
  ```
- **Solution**: The issue was resolved by the HPC Admin.

## Lessons Learned
- **Root Cause**: Unrecovered read errors and medium errors on Lustre OSTs.
- **Solution**: HPC Admin fixed the issue by addressing the medium errors and uncorrectable I/O failures.
- **Prevention**: Regularly monitor Lustre OSTs for errors and ensure timely maintenance to prevent such issues.

## Keywords
- Lustre file system
- Medium errors
- Unrecovered read errors
- Uncorrectable I/O failures
- OSTs (lfs-OST0015-lfs-OST0017)
- HPC Admin
- Monitoring and maintenance
```
---

### 2024121042002441_high%20load%20on%20atuin%20%5Bg101ea13%5D.md
# Ticket 2024121042002441

 ```markdown
# High Load on Storage Server Atuin

## Keywords
- High load
- Storage server
- Data handling
- GPU usage
- Data staging
- $TMPDIR
- /anvme workspace

## Problem Description
- High load observed on the storage server Atuin ($WORK).
- User jobs were identified as potentially contributing to the high load.
- User was reading training data directly from a directory with several thousand files/folders.

## Root Cause
- Inefficient data handling: Reading large datasets directly from the storage server.
- Potential issue with GPU setup: Only one GPU was being utilized.

## Solution
- **Data Handling:**
  - For small datasets, use "data staging" to $TMPDIR.
  - For larger datasets, use a workspace on /anvme.
  - Refer to recommendations: [Data Handling Recommendations](https://doc.nhr.fau.de/data/datasets/)

- **GPU Setup:**
  - Review and optimize the GPU configuration to ensure multiple GPUs are utilized if available.

## Actions Taken
- User was notified about the high load and potential issues.
- User canceled the jobs and agreed to review their data management and setup.
- Ticket closed after user acknowledgment.

## General Learnings
- Efficient data handling is crucial to avoid high load on storage servers.
- Utilize temporary directories ($TMPDIR) for small datasets and faster storage options (/anvme) for larger datasets.
- Ensure proper GPU configuration to optimize resource usage.
```
---

### 2024121042002244_Server%20becomes%20really%20slow.md
# Ticket 2024121042002244

 # HPC Support Ticket: Server Becomes Really Slow

## Summary
- **Issue**: Server slowdown in writing and deleting files.
- **Root Cause**: High load on the Atuin file system and misuse of frontend nodes for heavy calculations.
- **Solution**: Use frontend nodes for file operations, avoid allocating GPUs for long-duration tasks, and optimize file storage.

## Key Points
- **CPU Usage**:
  - Misuse of frontend nodes for heavy calculations.
  - Shared CPUs among users, multiple frontend nodes available.
- **File Operations**:
  - Slow due to high load on the Atuin file system.
  - Large number of files (~10M) causing performance issues.
- **Data Preprocessing**:
  - Allocate a GPU to avoid using the interactive terminal.
  - Avoid leaving the GPU idle for long periods.
- **Account Sharing**:
  - Violates Terms of Service (TOS).
  - Supervisor can send out invitations for new accounts.
- **File Deletion**:
  - Use frontend nodes for deletion.
  - Avoid allocating jobs on Alex for long-duration deletions.
  - HPC Admins can assist with deleting large directories.
- **Optimization Tips**:
  - Pack data into different formats (e.g., HDF5) to reduce the number of files.
  - Use archives and unpack them to the local disk on compute nodes.
  - Utilize `/anvme` for fast storage optimized for small files and heavy metadata operations.

## Documentation and Training
- **Documentation**:
  - [Data Management](https://doc.nhr.fau.de/data/datasets/)
  - [Staging](https://doc.nhr.fau.de/data/staging/)
  - [Workspaces](https://doc.nhr.fau.de/data/workspaces/)
- **Training**:
  - General Introduction: Wednesday, December 18, 2024, 4:00 p.m.
  - Introduction for AI Users: Thursday, December 19, 2024, 4:00 p.m.
  - Location: [Zoom](https://go-nhr.de/hpc-in-a-nutshell)
  - [HPC Café](https://hpc.fau.de/teaching/hpc-cafe/)

## Conclusion
- **Best Practices**:
  - Optimize file storage to avoid performance issues.
  - Use appropriate resources for file operations and data preprocessing.
  - Follow TOS regarding account sharing and usage.
- **Support**:
  - Contact HPC Admins for assistance with large file deletions and account-related issues.
  - Attend training sessions for better understanding and efficient use of HPC resources.
---

### 2024112642000316_Re%3A%20Data%20transfer%20to%20TMPDIR.md
# Ticket 2024112642000316

 ```markdown
# HPC Support Ticket: Data Transfer to TMPDIR

## Keywords
- Data transfer
- TMPDIR
- File server load
- Unpacking files
- Zip files

## Issue Description
A user reported an issue with unpacking zipped files from `$WORK` to `$TMPDIR`. The process, which usually takes 2-3 minutes, was taking over 20 minutes. The dataset size was around 12GB.

## Root Cause
- High load on the file servers.

## Solution
- The issue was identified as a temporary high load on the file servers. No specific action was required from the user's side.

## Lessons Learned
- High load on file servers can significantly impact data transfer and unpacking times.
- Users should be aware that such issues can occur and may need to wait for the load to decrease.
- For persistent issues, users should contact HPC support for further assistance.

## Recommendations
- Monitor file server load and performance.
- Inform users about potential delays during high load periods.
- Provide alternative solutions or workarounds if high load is expected to persist.
```
---

### 2024062842001545_Sleep-Job%20on%20Alex%20%5Bb207dd11%5D.md
# Ticket 2024062842001545

 # HPC Support Ticket: Sleep-Job on Alex

## Keywords
- `sleep` command
- Slurm submit script
- Interactive job
- Batch script
- File management
- Network performance
- Node-local storage
- `tar`
- `zip`
- `$TMPDIR`

## Problem
- User was using the `sleep` command in the Slurm submit script to allocate resources and then logging in to the node to start work interactively.
- User had 1.5 million files on `atuin` and was reading them continuously over the network.

## Root Cause
- Inefficient resource allocation and usage.
- Network congestion due to continuous file reading.

## Solution
- **Resource Allocation**: Allocate a true interactive job or write a batch script that can run independently.
  - Reference: [Interactive Job Documentation](https://doc.nhr.fau.de/clusters/alex/#interactive-job-single-gpu)
- **File Management**: Create an archive with `tar` or `zip` and unpack it directly to the node-local storage `$TMPDIR`.

## General Learnings
- Avoid using `sleep` in Slurm submit scripts to prevent resource idling.
- Use interactive jobs or batch scripts for efficient resource management.
- Archive large numbers of files to reduce network load and improve performance.
- Utilize node-local storage for temporary files during job execution.

## Contact
- For assistance with writing submit scripts or any other questions, contact the HPC support team.

---

**Note**: This documentation is intended for HPC support employees to reference when addressing similar issues in the future.
---

### 2018110642000339_Woodycap3_4%20performance.md
# Ticket 2018110642000339

 # HPC Support Ticket: Woodycap3/4 Performance

## Keywords
- Woodycap frontends
- Login delay
- Filesystem performance
- GPFS servers
- $HOME
- $VAULT

## Problem Description
- Slow login times (approximately 10 seconds)
- Extremely slow filesystem performance

## Root Cause
- High load on GPFS servers for $HOME and $VAULT

## Solution
- Investigate and address the high load on GPFS servers

## General Learnings
- High load on GPFS servers can significantly impact login times and filesystem performance
- Monitoring and managing GPFS server load is crucial for maintaining optimal performance on HPC frontends

## Next Steps
- HPC Admins should check the GPFS server load and take appropriate actions to reduce it
- Regular monitoring of GPFS server performance to prevent similar issues in the future
---

### 2024062642002011_Cancelling%20of%20job%20due%20to%20high%20load%20on%20fileservers%20-%20b180dc22.md
# Ticket 2024062642002011

 ```markdown
# Cancelling of Job Due to High Load on Fileservers

## Keywords
- High load on fileservers
- Job cancellation
- Data handling
- Network filesystem
- HDF5 format
- Node local disk
- Webdataset
- HTTP serving

## Problem
- User's jobs were causing high load on fileservers due to a large number of small files (94.2M files, 5TB).
- A simple `ls` command in the user's directory took about 1 minute due to the high number of files.
- Other users experienced slow IO and bad performing jobs as a result.

## Root Cause
- Storing a large number of small files on a network filesystem can lead to high load and performance issues.

## Solution
- **Data Handling**: Avoid storing a large number of small files on a network filesystem.
- **File Format**: Use a different file format such as HDF5 or similar to consolidate data.
- **Node Local Disk**: Copy data to the node local disk before processing.
- **Webdataset**: Consider using webdataset and serving data via HTTP from an NVMe box.

## Documentation
- [Data Handling Documentation](https://doc.nhr.fau.de/data/staging/)
- [Datasets Documentation](https://doc.nhr.fau.de/data/datasets/)

## Actions Taken
- User's jobs were killed to alleviate the load on the fileservers.
- User was advised to follow the documentation on data handling and to store data in a different way before restarting jobs.

## General Learning
- Storing a large number of small files on a network filesystem can cause significant performance issues.
- Consolidating data into fewer, larger files (e.g., using HDF5) and copying data to the node local disk can improve performance.
- Using webdataset and serving data via HTTP can be an effective way to handle large datasets.
```
---

### 2024032542002591_instability%20in%20job%20speed.md
# Ticket 2024032542002591

 # HPC Support Ticket: Instability in Job Speed

## Keywords
- Job instability
- Slow IO
- High load on $WORK
- Node local SSD
- Logging and checkpointing
- System reboot
- Service disruptions

## Problem Description
- User observed instabilities in running jobs starting at 13:30.
- Increased time spent on data fetching (non-GPU operations).
- High latency in communication with the server and direct shell commands.
- Jobs crashed due to inability to write to $WORK.
- No access to $WORK from the cluster.

## Root Cause
- High load on $WORK file server causing slow IO.
- System issues with $WORK requiring a reboot.

## Troubleshooting Steps
- HPC Admins suggested copying data to node local SSD to reduce IO load.
- User confirmed data was already on SSD, but logging and checkpointing were still done on $WORK.
- HPC Admins rebooted the system to resolve $WORK issues.
- Further investigation and system checks were conducted.

## Solution
- Rebooting the system resolved the immediate issue with $WORK.
- User was advised to monitor IO operations and consider moving logging and checkpointing to SSD if feasible.
- HPC Admins continued to investigate and update on service disruptions.

## Collaboration
- User offered to double-check with collaborators for unintended IO operations.
- HPC Admins kept the user updated on system checks and service disruptions.

## Follow-up
- User was advised to report further issues with $WORK.
- HPC Admins provided a link to updates on service disruptions.

## General Learning
- High load on file servers can cause job instabilities and slow IO.
- Copying data to node local SSD can improve job performance, especially for small files and repeated reads.
- Regular system checks and reboots may be necessary to resolve file server issues.
- Collaboration between users and HPC Admins is crucial for troubleshooting and resolving issues.
---

### 2022101342000275_Hohe%20Last%20auf%20janus_woody%20%5Biwi5%5D.md
# Ticket 2022101342000275

 ```markdown
# HPC Support Ticket: High Load on Janus/Woody [iwi5]

## Summary
The HPC server Janus was experiencing high load due to a large number of files in specific directories, causing read and write requests to take longer.

## Root Cause
- The directory `woody/iwi5/shared/ChestX-ray8/images` contained 112,120 images, which were regularly accessed by jobs on Alex.
- Other directories also contained a large number of files:
  - `viphome/iwi5-datasets/open-images-v6/train/data/`: 633,199 files
  - `viphome/iwi5-datasets/imagenet/omniart/`: 1,803,659 files
  - `viphome/iwi5-datasets/objects365/download/images/train/`: 1,742,391 files
  - `viphome/iwi5-datasets/objects365/download/images/val/`: 80,088 files

## Solution
- Users were advised to pack the images into archives and move them to Lustre.
- The agreement regarding `iwi5-datasets` was that it should be a place for image archives, not individual files.
- Users were reminded that having many individual files in a directory is not performant.
- Users were informed that Lustre should not be the only copy of data due to potential data loss during high-water deletion.

## Follow-up
- Users confirmed they would pack the datasets into archives and move them to Lustre.
- Users requested access to TinyGPU for the archives, but were informed that Lustre is only accessible from Alex and Fritz.
- Users were provided with the names of the users responsible for the high file count.
- The issue was resolved, and the ticket was closed after verifying that the file count had been reduced.

## Keywords
- High load
- Janus
- Woody
- Large number of files
- Performance issues
- Archiving
- Lustre
- Data management
```
---

### 2024051242000729_Massive%20Last%20auf%20_home_saturn_capn%20-%20mppi044h.md
# Ticket 2024051242000729

 # HPC Support Ticket: Massive Load on /home/saturn/capn

## Keywords
- Snakemake
- Woody
- Slurm
- IO load
- Fileserver
- GrpTRES
- sacctmgr

## Summary
A user's jobs on Woody using Snakemake were suspected of causing massive load on `/home/saturn/capn/` since approximately 02:00. The user was temporarily throttled in Slurm to ensure orderly operation for other users.

## Root Cause
The user's Snakemake jobs were causing excessive IO load on the fileserver. The user intended for IO operations to be handled on `wecapstor3`, but the issue persisted.

## Actions Taken
- The user was temporarily throttled in Slurm using the command: `sacctmgr -i update account where user=mppi044h set GrpTRES=cpu=20`.
- The user, in consultation with the 2nd Level Support team, moved the Snakemake project to `wecapstor3` and reduced the number of jobs to identify the problem.

## Solution
The user is testing with a reduced number of jobs on `wecapstor3` to pinpoint the issue. Further updates are pending based on the test results.

## Lessons Learned
- Snakemake jobs can cause significant IO load on fileservers.
- Throttling users in Slurm can help maintain system stability for other users.
- Collaboration with the 2nd Level Support team is crucial for resolving complex issues.
- Proper configuration of IO operations in Snakemake is essential to avoid overloading fileservers.

## Next Steps
- Monitor the user's tests on `wecapstor3`.
- Adjust Snakemake configurations as needed based on test results.
- Ensure that IO operations are properly directed to avoid future overloads.

## References
- [FAU HPC Support](mailto:support-hpc@fau.de)
- [FAU HPC Website](https://hpc.fau.de/)
---

### 2019020142001004_Woody%20Filesystem_Netzwerk%20ueberlastet%3F.md
# Ticket 2019020142001004

 # HPC Support Ticket Analysis

## Subject: Woody Filesystem/Netzwerk überlastet?

### Keywords:
- Network overload
- Filesystem overload
- Slow operations (`ls`, `mv`)
- Woody
- Saturn

### Problem Description:
- User reports slow network and filesystem operations on Woody.
- Operations like `ls` and `mv` taking unusually long (e.g., 30 minutes for a 100MB move from Woody to Saturn).
- Similar issues reported by colleagues.

### Root Cause:
- Possible overload of the network or filesystem on Woody.

### Solution:
- No solution provided in the initial conversation.
- Further investigation by HPC Admins required to identify and resolve the issue.

### General Learnings:
- Network and filesystem performance issues can significantly impact user operations.
- Monitoring and prompt investigation are crucial for maintaining system performance.
- Collaboration with colleagues can help identify widespread issues.

### Next Steps:
- HPC Admins should check network and filesystem logs for any anomalies.
- Consider load balancing or optimizing network and filesystem configurations.
- Communicate with users about ongoing issues and expected resolution times.
---

### 2024080642003385_Handling%20100G%20Zarr%20Archiv%20ML%20I_O.md
# Ticket 2024080642003385

 # HPC Support Ticket: Handling 100G Zarr Archive ML I/O

## Keywords
- Zarr format
- ZIP archive
- Data transfer
- ML pipeline
- Performance issues
- Conda environment

## Problem Summary
- User is working with a 100G Zarr dataset consisting of ~100,000 files distributed across ~10 directories.
- The dataset is currently stored in an uncompressed ZIP archive in anvme/workspace.
- The dataset is transferred to the local SSD of compute nodes before each job, but unpacking takes approximately 30 minutes of compute time per job.
- User inquires about alternative methods to handle the dataset without overloading the filesystem or data connection.
- User also reports general performance issues with the cluster, specifically slow loading of Conda environments.

## Solutions and Discussions
- **HPC Admin** suggests using `zarr.ZipStore` to work directly with ZIP archives, potentially eliminating the need to unpack the dataset.
- **User** reports issues with `zarr.ZipStore` when using multiple workers in PyTorch Dataloader due to CRC checks in the ZIP archive.
- **HPC Admin** acknowledges the issue and suggests that direct reading from the workspace might still be a viable option for performance testing.

## Monitoring and Performance
- **HPC Admin** mentions that performance issues might be due to short-term bursts on distributed file systems, but no specific performance problems are known.
- **User** should consider monitoring the data connection load, though specific methods for monitoring are not detailed in the conversation.

## Conclusion
- Directly reading from the ZIP archive using `zarr.ZipStore` is not a viable solution due to CRC issues with multiple workers.
- Further testing and performance monitoring are suggested to find an optimal solution for handling the dataset.
- General performance issues with the cluster are acknowledged but not specifically addressed.

## Next Steps
- **User** should explore alternative methods for handling the dataset, such as converting it to a format with fewer files.
- **HPC Admin** should gather more practical experience with the new workspaces to better advise on performance and data handling strategies.

---

This report summarizes the key points and solutions discussed in the HPC support ticket conversation, providing a reference for future similar issues.
---

### 2021092742003652_Lesen%20von%20%24FASTTMP%20mit%20mehreren%20MPI%20Prozessen.md
# Ticket 2021092742003652

 # HPC-Support Ticket Conversation Analysis

## Subject
Lesen von $FASTTMP mit mehreren MPI Prozessen

## Keywords
- $FASTTMP
- Lustre Filesystem
- NFSv4 Filesystem
- Race Condition
- MPI Prozesse
- Restart-Folder
- Binärdateien
- Paralleles Dateisystem
- Metadatenoperationen
- SLURM Skript
- Hybrid-Parallelisierung
- OpenMP

## Problem Description
The user is experiencing issues with their simulation code when reading restart files from $FASTTMP on the Emmy cluster. The simulation involves 2000 MPI processes, and the restart folder contains a few files that all processes need to read simultaneously. This leads to a suspected race condition, causing the simulation to block. The issue does not occur with smaller simulations or on the user's local machine.

## Root Cause
- The $FASTTMP filesystem on Emmy is experiencing hardware issues and is not performing optimally.
- The large number of files (>100,000) in the user's $FASTTMP directory is causing stress on the filesystem, leading to delays and potential race conditions.
- The user's code is not optimized for reading files in parallel, leading to a race condition when all 2000 processes attempt to read the same files simultaneously.

## Troubleshooting Steps
1. The user tested reading files from both $FASTTMP and $WOODYHOME to identify any patterns or differences in behavior.
2. The user ran a test simulation on the Meggie cluster, which completed successfully without any issues.
3. The user considered reconfiguring their simulation to write all output data to a single file instead of multiple files to reduce the load on the filesystem.

## Solution
- The HPC Admin suggested trying to run the simulation on the Meggie cluster, as its $FASTTMP filesystem is in better condition.
- The user should consider reconfiguring their simulation to write all output data to a single file instead of multiple files to reduce the load on the filesystem.
- The user should also consider using the $WORK directory for their simulations, as it may be better suited for handling a large number of files.

## General Learnings
- The $FASTTMP filesystem on Emmy is experiencing hardware issues and is not performing optimally. Users should consider using alternative filesystems or clusters for their simulations.
- Writing a large number of files to a parallel filesystem can cause stress and lead to delays and potential race conditions. Users should consider optimizing their code to reduce the number of files written.
- The Meggie cluster may be a better option for users experiencing issues with the Emmy cluster, as its $FASTTMP filesystem is in better condition.
- Users should consider using the $WORK directory for their simulations, as it may be better suited for handling a large number of files.
- The SLURM script configuration should be carefully considered to ensure optimal performance and resource allocation.
---

### 2024092642005192_load%20a%20large%20file%20in%20alex.md
# Ticket 2024092642005192

 # HPC Support Ticket: Loading Large Files in Python

## Subject
Loading a large data file (about 50 GB) in Python on alex.

## User Issue
- User needs to load large data files (22 GB and 50 GB) in Python.
- Observes significant speed reduction when loading the 50 GB file compared to the 22 GB file.

## Key Points
- User initially inquires about allocating large-memory CPUs for the task.
- HPC Admin suggests using CPU-only systems like woody or tinygpu.
- User reports slow loading speeds for the 50 GB file.
- HPC Admin suggests compressing files and using `$TMPDIR` to minimize transfer times.
- User implements the suggestion but still faces slow loading speeds.
- HPC Admin tests and confirms that the system can handle large files efficiently.
- Further investigation reveals potential issues with the Python script's file handling.

## Solution
- Ensure that the file copying process is not duplicated in the Python script.
- Use the `date` command to estimate the speed of copying the file in the job script.

```bash
echo "BEFORE COPY"
date
YOUR_COPY_COMMAND_...
date
echo "AFTER COPY"
```

## Conclusion
- The root cause of the problem is likely in the Python script's file handling.
- Properly managing file copying in the job script should resolve the speed issue.

## Keywords
- Large file loading
- Python file handling
- HPC file transfer
- `$TMPDIR` usage
- Job script optimization

## General Learning
- Always verify that file operations are not duplicated between job scripts and application code.
- Use temporary directories (`$TMPDIR`) for efficient file handling.
- Monitor file transfer speeds using simple timing commands to diagnose performance issues.
---

### 2022091242000556_Massiver%20IO%20durch%20iwal-Leute%20auf%20GPU-Knoten.md
# Ticket 2022091242000556

 ```markdown
# HPC Support Ticket: High I/O Operations on GPU Nodes

## Problem Description
- High I/O operations on GPU nodes causing performance bottlenecks.
- Multiple users launching jobs simultaneously, leading to excessive file open/close operations.
- Specific datasets with small files causing high I/O load.

## Root Cause
- Users were frequently accessing small files, leading to high I/O operations.
- Libraries used by users were not optimized for I/O operations.
- Multiple jobs accessing the same datasets simultaneously.

## Measurement and Analysis
- I/O operations were measured using `opensnoop.bt` tool.
- High file open/close operations were observed for specific users and datasets.
- Datasets with small files were identified as major contributors to high I/O load.

## Solutions and Recommendations
- **Packing Small Files**: Pack small files into archives and copy them to `$TMPDIR` at job start to reduce load on the network filesystem.
- **Optimize Libraries**: Limit imports to required functions to minimize I/O operations.
- **Shared Storage**: Create a shared directory (`/home/janus/iwal-datasets`) with a 5TB quota and 100k file limit for archived training datasets.
- **Monitoring**: Users should write scripts to monitor resource usage and data fetching time.

## Best Practices
- Follow best practices for I/O operations as outlined in the HPC documentation.
- Regularly monitor I/O operations and optimize workflows to reduce load.
- Communicate with HPC Admins promptly if issues are detected.

## Additional Notes
- HPC Admins will periodically check I/O usage and provide feedback.
- Users should enforce terms-of-use for datasets stored in shared directories.
- Regular Zoom meetings can be scheduled to discuss and resolve I/O issues.

## References
- [HPC Best Practice Guide](https://hpc.fau.de/files/2022/01/2022-01-11-hpc-cafe-file-systems.pdf)
- [HPC Training Videos](https://www.fau.tv/clip/id/40199)
```
---

### 2024042642003023_Handling%20of%20IO%20on%20the%20cluster.md
# Ticket 2024042642003023

 # HPC Support Ticket: Handling of IO on the Cluster

## Keywords
- IO handling
- File servers
- Local storage
- Network file system
- GPU memory
- Temporary storage
- Error handling
- Retry loop

## Summary
The user has questions regarding the handling of large files and saving models during training on the HPC cluster. The user encountered a job failure during the writing process without any error messages.

## Root Cause
- High load on file servers causing disruptions.
- Frequent writes to network file systems can cause performance issues.

## Solutions and Recommendations
- **Data Transfer**: Transfer large files to local disk first before loading into GPU memory. Benchmark to determine the faster and more stable method.
- **Storage**: Use local storage (`$TMPDIR`) for temporary files during calculations and transfer data to network shares at the end.
- **Error Handling**: Implement retry loops and proper error handling in the code to mitigate file operation failures.
- **Avoid Frequent Writes**: Avoid frequent writes to network file systems, especially for small text writes like log outputs.

## Additional Notes
- The HPC admin mentioned ongoing file server issues and provided a link to the service disruption notice.
- Compressing files or putting them in a tarball may help with transfer speeds and stability.

## Follow-up
- The user asked about writing files to the node's output directory instead of `$TMPDIR`. The HPC admin advised against it, as it can cause harm to shared file systems.

## Conclusion
Following the recommended practices for IO handling on the cluster can help prevent job failures and improve performance. Regularly check for service disruptions and implement robust error handling in scripts.
---

### 2025022742003621_Please%20use%20%24TMPDIR%20to%20store%20your%20training%20dataset%20%5Bv104dd19%5D.md
# Ticket 2025022742003621

 # HPC Support Ticket: High I/O Patterns and Data Handling Optimization

## Keywords
- High I/O patterns
- Node-local storage
- Tar archives
- Webdataset
- $TMPDIR
- /anvme
- Net_bytes_in
- Nfs4_read
- Clustercockpit

## Problem
- User's job shows high I/O patterns (~100 MB/s per node) to the file server.
- User uses webdataset to read large tar files directly into the training loop without extracting contents.

## Root Cause
- Continuous reading of large datasets over the network causes high I/O traffic.
- Inefficient data transfer method leading to prolonged copying times.

## Recommendations and Solutions
- **Use Node-Local Storage**: Extract data directly to $TMPDIR to benefit from node-local SSDs.
  ```bash
  cd $TMPDIR; tar -xf /path-to/archive.tar
  ```
- **Distribute Data for Multi-Node Jobs**:
  ```bash
  srun --ntasks=$SLURM_NNODES --ntasks-per-node=1 tar -xf archive.tar -C $TMPDIR
  ```
- **Pack Small Tar Files into Larger Archives**: Pack 5K tar files into 25-50 archives to speed up data transfer.
- **Monitoring Metrics**:
  - `net_bytes_in` captures ethernet traffic, including communication to /anvme.
  - `nfs4_read` captures NFS read operations.

## Additional Notes
- **Benchmark Data**: Extracting a 1.45 TB dataset in 21 tar files to $TMPDIR took approximately 13 minutes.
- **Clustercockpit**: Used to monitor job metrics like `net_bytes_in` and `nfs4_read`.
- **Workaround**: User implemented a workaround in the dataloading logic to optimize bandwidth usage.

## Conclusion
- Optimizing data handling by using node-local storage and efficient data distribution methods can significantly reduce I/O traffic and improve job performance.
- Monitoring tools like Clustercockpit are essential for tracking job metrics and identifying areas for optimization.
---

### 2019052742002763_Access%20to%20Meggie%20revoked.md
# Ticket 2019052742002763

 # HPC Support Ticket: Access to Meggie Revoked

## Keywords
- Access revoked
- Job management
- Resource abuse
- File system usage
- Job limitations

## Summary
A user's access to the Meggie cluster was revoked due to inappropriate job management and resource abuse. The user submitted a large number of short jobs, causing severe overload and impacting other users.

## Root Cause
- User submitted over 35,000 jobs with a runtime of less than 5 seconds each, causing a Denial of Service (DoS) like effect.
- User's jobs were writing restart files every few seconds, impacting the file system and Infiniband communication.

## Solution
- **HPC Admins** re-enabled the user's account with limitations:
  - Maximum of 500 jobs can be submitted at a time.
  - Maximum of 25 jobs can run concurrently.
- User was advised to combine short jobs into a single job to avoid resource wastage.
- User was reminded about proper file system usage:
  - `$FASTTMP` is for bulk binary I/O, not for generating/storing ASCII files.
  - User should keep an eye on the number of files in `$FASTTMP`.

## General Learnings
- Inappropriate job management can lead to access revocation.
- Short jobs that cause more overhead than actual runtime should be combined.
- Proper file system usage is crucial to avoid impacting the cluster's performance.
- **HPC Admins** may impose limitations on job submission and concurrent jobs to prevent resource abuse.
- Users should be considerate of other users and the cluster's overall performance.
---

### 2021080542002428_Re%3A%20%5BRRZE-HPC%5D%20%24FASTTMP%20%3D%20_elxfs%20on%20Emmy%20still%20unstable.md
# Ticket 2021080542002428

 # HPC Support Ticket: $FASTTMP = /elxfs on Emmy Unstable

## Keywords
- $FASTTMP
- /elxfs
- Emmy
- Parallel file system
- StarCCM+
- PBS jobs
- Images and plots
- File system best practices

## Summary
The parallel file system $FASTTMP = /elxfs on Emmy has been experiencing instability, potentially due to inappropriate use. The hardware is aging, but the primary cause of failures is suspected to be overload from misuse of the file system.

## Root Cause
- Inappropriate use of the parallel file system, such as storing ASCII files, fine granular input/output, tiny files, source code, or installing binaries.
- Frequent writing of small files, like images and plots, by applications like StarCCM+.

## Solution
- **Best Practices for File Systems:**
  - Use $FASTTMP for large binary output files.
  - Avoid storing ASCII files, fine granular input/output, tiny files, source code, or installing binaries on $FASTTMP.
  - For frequent writing of small files (every few seconds), use /home/woody ($WORK) instead.
  - Larger intervals (several minutes apart) for writing small files can still use $FASTTMP without impacting performance.

- **User Guidance:**
  - The user was advised to write images and plots every 15-20 minutes or more, which is considered an acceptable interval for $FASTTMP.
  - The user confirmed they are following good practices and will continue to do so.

## Actions Taken by HPC Admins
- Informed users about the proper use of the parallel file system.
- Warned about potential job termination, account throttling, or banning for repeated abuse.
- Considered permanent shutdown of the file system if stability problems persist.
- Stopped creating directories on $FASTTMP for new accounts or accounts without existing data.

## Conclusion
The user was not contributing to the instability with their current practices. The issue remains under observation. If problems persist, further action may be taken.

## Follow-up
- Monitor the stability of $FASTTMP.
- Provide further guidance to users if necessary.
- Consider hardware updates or replacements if aging components are found to be the cause of instability.
---

### 2023102342002154_suspect%20jobs%20on%20Fritz%20-%20k103bf.md
# Ticket 2023102342002154

 ```markdown
# HPC Support Ticket: Suspect Jobs on Fritz - k103bf

## Keywords
- High load on file system
- Large logfiles
- Job script modification
- IO-Last
- Quota usage
- File size distribution

## Summary
- **Issue**: High load on the `atuin` file system, potentially caused by user jobs.
- **Root Cause**: Large number of files and high data volume generated by user jobs.
- **Solution**: Reduce output and modify job scripts for correct module initialization.

## Details
- **HPC Admin**: Notified user about high load on the `atuin` file system and requested to check job functionality and reduce output.
- **User**: Confirmed jobs are working as intended and will reduce output after current jobs are completed.
- **HPC Admin**: Identified that the high IO load is likely not from Slurm-STDOUT but from a large number of files (~42,000 files, 15 TB) generated within a short timeframe.
- **HPC Admin**: Noted that the user group's quota usage increased significantly, and an attempt to move data to Lustre was unsuccessful.
- **HPC Admin**: Provided file size distribution details and mentioned that one HDD (sdas) was notably slower.

## Lessons Learned
- Regularly monitor file system usage and job outputs to prevent high load situations.
- Ensure job scripts are correctly initialized with `#!/bin/bash -l` for proper module loading.
- Consider data management strategies to handle large volumes of data efficiently.
- Communicate with users to address high load issues promptly and collaboratively.
```
---

### 2021121842000415_Re%3A%20Action%20required%20%28iwso033h%29%3A%20Last%20auf%20HPC-Home-Servern%20des%20RRZE%20_%20Loa.md
# Ticket 2021121842000415

 # HPC Support Ticket: High Load on HPC Home Servers

## Keywords
- High load
- Metadata operations
- Deep learning models
- Parallel training
- TMPDIR
- HDF5
- tar/zip archive

## Problem Description
- High load on HPC home servers (`/home/hpc`, `/home/vault`, `/home/woody`) due to massive metadata operations.
- User's deep learning models training on a dataset of ~57,000 images caused frequent small file accesses.
- Parallel training of multiple models exacerbated the issue.

## Root Cause
- Frequent small file accesses and parallel job execution leading to high metadata operations.

## Solution
- User agreed to train models sequentially instead of in parallel to reduce load.
- HPC Admin suggested packing data into a hierarchical format (e.g., HDF5) or a tar/zip archive and copying it to `$TMPDIR` at the start of each job.
- User implemented the suggested solution.

## General Learnings
- High metadata operations can significantly slow down the HPC system.
- Training deep learning models on large datasets with many small files can cause high load.
- Packing data into a hierarchical format or archive and using `$TMPDIR` can mitigate the issue.
- Communication and cooperation between users and HPC support are crucial for resolving such issues.
---

### 2016112842000748_Mal%20wieder%3A%20viele%20kleine%20Dateien.md
# Ticket 2016112842000748

 # HPC Support Ticket: Handling Many Small Files

## Keywords
- Small files
- Archive extraction
- File system performance
- Woody
- TinyFat
- Local SSDs
- $SCRATCH

## Problem
- User needs to extract an archive containing 335,615 small files and process them, resulting in a similar number of larger files.
- Concern about the best file system to handle this task efficiently.

## Details
- Archive size: 8.4 GB (compressed), 43 GB (uncompressed)
- Processed files: ~8 MB each, compressible to under 500 kB
- Estimated total storage needed: ~250 GB

## Solution
- **File System Recommendation**: Woody is recommended for handling many small files efficiently.
- **Alternative**: New nodes in TinyFat with local SSDs (1.1 TB) could be beneficial for such tasks.

## Additional Notes
- User appreciates the availability of nodes with local SSDs and has future plans to utilize them.
- User plans to use $SCRATCH for processing and compression.

## Conclusion
- For handling many small files, Woody is the preferred file system.
- Local SSDs on new nodes can be considered for similar tasks in the future.

---

This documentation can be used to address similar issues related to handling many small files and choosing the appropriate file system on the HPC cluster.
---

### 2024120342002507_Jobs%20causing%20high%20load%20on%20atuin%20%5Bb133ae13%5D.md
# Ticket 2024120342002507

 ```markdown
# HPC-Support Ticket: Jobs Causing High Load on Filesystem

## Keywords
- High load on filesystem
- Short jobs
- Monte Carlo simulations
- Compute time usage
- IO reduction
- Job submission limits

## Summary
A user submitted a large number of short jobs, causing high load on the filesystem and using only 6 cores per node. The project had already used up its compute time, but a 25% extension could be requested.

## Root Cause
- High IO operations in short jobs
- Simultaneous submission of many short jobs

## Solution
- **Reduce IO in jobs**: Minimize file operations to reduce load on the filesystem.
- **Limit job submissions**: Submit fewer jobs simultaneously to prevent high load.
- **Account limitation**: The user's account was temporarily limited to 10 nodes to manage the load.

## General Learnings
- High IO operations in short jobs can cause significant load on the filesystem.
- Limiting the number of simultaneous job submissions can help manage system load.
- Communication with users about compute time usage and potential extensions is important.
- Temporary account limitations can be used to manage excessive resource usage.
```
---

### 2021121942000281_Constantly%20high%20IO%20rate%20of%20pw.x%20on%20Emmy%20-%20nfcc03.md
# Ticket 2021121942000281

 ```markdown
# HPC-Support Ticket: Constantly High IO Rate of pw.x on Emmy

## Keywords
- High IO rate
- pw.x
- Emmy
- FASTTMP
- File servers
- Disk IO
- Job performance

## Summary
A user's Quantum Espresso (QE) jobs on Emmy were causing excessive IO rates, leading to performance issues for both the user's jobs and the overall system.

## Problem
- **High IO Rate**: The user's jobs were generating a high IO rate of approximately 20 MB/s per job, resulting in about 5 TB of data transferred in less than 24 hours.
- **Frequent File Writes**: Data was being overwritten at very short intervals (approximately once per minute).
- **File Server Load**: The high IO rate was causing heavy load on the file servers, affecting the performance of other jobs.

## Root Cause
- **Incorrect File System Usage**: The user was running PW jobs on the `/home/vault` file system instead of the recommended `FASTTMP` file system.
- **Frequent Dumping**: The jobs were dumping `CNO.wfc*` files once per minute, which was unnecessary and causing excessive IO.

## Solution
- **Use FASTTMP**: The user was advised to use the `FASTTMP` file system for running PW jobs.
- **Reduce IO Rate**: The user was advised to reduce the IO rate by reducing the frequency of file dumps.

## Lessons Learned
- **Proper File System Usage**: Ensure that users are aware of the appropriate file systems to use for different types of jobs to avoid excessive IO rates.
- **Monitoring and Alerts**: Regular monitoring of IO rates and alerts for high IO usage can help identify and address issues proactively.
- **Communication**: Clear communication with users about best practices and the impact of their jobs on the system can help prevent similar issues in the future.

## Additional Notes
- **FASTTMP Capacity**: The upcoming parallel computer "Fritz" will have more capacity but can only cope with less than 0.5 IOPs per core, making it even more important to manage IO rates effectively.
- **NFS Caching**: The discrepancy between outgoing and incoming Ethernet bandwidth may be due to NFS caching effects.
```
---

### 2022070842003252_Login%20auf%20Fritz.md
# Ticket 2022070842003252

 # HPC Support Ticket: Login auf Fritz

## Keywords
- Login issues
- NoMachine
- WinSPC
- Lustre
- FASTTMP
- Hanging system
- Remote directory
- Certificate expiration

## Problem Description
- User unable to access specific directories on Fritz via NoMachine and WinSPC.
- System hangs when accessing subdirectories containing simulation files.
- WinSPC shows "Entferntes Verzeichnis wird gelesen" and does not proceed.

## Root Cause
- Issues with the Lustre parallel file system ($FASTTMP under /lustre).
- LustreError: Operation `ost_connect` to nodes failed with rc = -19.
- Certificate expiration.

## Solution
- Confirmed Lustre issues and attempted fixes were unsuccessful.
- Problem resolved over the weekend by updating Lustre clients on Fritz compute nodes.
- Avoid using LTS clients with Fritz-Lustre; use bleeding edge versions (at least 2.15.0).

## Lessons Learned
- Lustre issues can cause directory access problems and system hangs.
- Certificate expiration can affect system access.
- Updating Lustre clients to the latest versions can resolve compatibility issues.
- Weekend maintenance can be effective for resolving complex issues without disrupting user workflows.

## Follow-up
- Ensure Lustre clients are kept up-to-date to avoid similar issues in the future.
- Monitor certificate expiration dates to prevent access disruptions.

## References
- HPC Admin communications
- User reports and screenshots

## Ticket Status
- Resolved
---

### 2024021042000569_Re%3A%20Over%20quota%20on%20_home_vault%20-%20iwi5142h%20-%20ML-Daten-Staging%20auf%20%24TMPDIR.md
# Ticket 2024021042000569

 ```markdown
# HPC Support Ticket Analysis: Performance Issues with Large Datasets

## Keywords
- HPC Support
- Performance Issues
- Large Datasets
- Data Handling
- Job Optimization
- Walltime
- TMPDIR
- Archive Extraction

## What Can Be Learned
- The importance of optimizing data handling for large datasets in HPC environments.
- The impact of file system performance on job runtimes.
- Strategies for improving job performance by using local storage (TMPDIR).
- The benefits of archiving and extracting data locally.

## Root Cause of the Problem
- The user was experiencing significant performance issues and job cancellations due to the 24-hour walltime limit.
- The job was reading a large number of small files (346,133 files, 120 GB) from the shared filesystem, causing performance degradation.

## Solution
- The user was advised to archive the data using zip or tar and extract it to the node-local storage (TMPDIR) at job start.
- This approach significantly reduced the extraction time from 2 hours on the shared filesystem to 13 minutes on TMPDIR.
- The job runtime was reduced from 28 hours to 12 hours on an NVIDIA V100, demonstrating a performance gain of approximately 130%.

## Conclusion
- By optimizing data handling and utilizing local storage, the user was able to achieve significant performance improvements and avoid job cancellations.
- This success story highlights the importance of efficient data management in HPC environments.
```
---

### 2021121742001265_Re%3A%20Action%20required%3A%20Last%20auf%20HPC-Home-Servern%20des%20RRZE%20_%20Load%20on%20RRZE%20H.md
# Ticket 2021121742001265

 # HPC Support Ticket: High Load on HPC Home Servers

## Keywords
- High load
- Home servers
- Metadata operations
- Checkpoints
- File access
- Job load

## Problem Description
The HPC home servers at RRZE are experiencing high load, particularly affecting the file systems `/home/hpc`, `/home/vault`, and `/home/woody`. This load is attributed to massive metadata operations (e.g., opening/closing files), which slow down the entire system and temporarily hinder all HPC customers in their work.

## Root Cause
- The user's jobs involve accessing data stored on `/home/woody` and `/home/hpc`.
- The jobs create checkpoints every 2-5 minutes, which are between 10-200 MB in size.
- The user also writes metrics to a `.txt` file every minute.

## Solution
- The user has deactivated the checkpoints and will only write a final checkpoint at the end of the job.
- If checkpoints are reactivated, the user is advised to use a larger interval, such as 30 minutes.

## General Learnings
- Frequent file access, especially with small files, can cause high load on the home servers.
- Regular checkpoints can contribute to this load if they are too frequent or too large.
- It is important to monitor and adjust job behavior to minimize the impact on the shared file systems.

## Next Steps
- Continue monitoring the load on the home servers.
- If the problem persists, consider throttling certain job types on the clusters.
- Encourage users to optimize their job behavior to reduce the load on the home servers.
---

### 2025022042003401_Question%20regarding%20efficient%20data%20handling%20with%20zip.md
# Ticket 2025022042003401

 # HPC Support Ticket: Efficient Data Handling with Zip

## Keywords
- Efficient data handling
- Zip archives
- Unzip
- Tar
- Benchmarking
- Parallel unpacking

## Problem
- User's team uses zip archives for data compression.
- Concern about the efficiency of extracting zip archives directly to node-local storage.
- Comparison between zip and tar extraction processes.

## Root Cause
- User's team has been using zip archives and wants to optimize the extraction process.
- Uncertainty about whether extracting directly from the source directory to `$TMPDIR` is efficient for zip archives.

## Solution
- Confirmed that extracting directly from the source directory to `$TMPDIR` is correct for zip archives.
- Suggested that tar might be more efficient due to its ability to handle both compression and extraction simultaneously.
- User performed benchmarking and found significant improvements by splitting archives into smaller chunks and using parallel unpacking.

## Learnings
- Extracting directly from the source directory to `$TMPDIR` is a valid approach for zip archives.
- Parallel unpacking and splitting large archives into smaller chunks can significantly improve extraction times.
- Tar is generally more efficient than zip for handling large datasets due to its combined compression and extraction capabilities.
- Benchmarking and optimizing workflows can lead to substantial performance improvements.

## Actions Taken
- User performed benchmarking and shared results with the HPC support team.
- HPC support team confirmed the validity of the user's approach and encouraged documentation for future reference.
- User updated the team and codebase with the optimized workflow.

## Future Recommendations
- Consider transitioning to tar for future data handling to further optimize performance.
- Document optimized workflows for future reference and team use.
- Continue benchmarking and optimizing data handling processes.
---

### 2022060242001491_Problems%20Writing%20to%20FASTTMP.md
# Ticket 2022060242001491

 # HPC Support Ticket: Problems Writing to FASTTMP

## Keywords
- FASTTMP
- I/O error
- File limit
- Parallel output
- MPI
- dealii
- VTK files

## Problem Description
The user is experiencing I/O errors when writing VTK files to FASTTMP during simulations using an in-house MPI code based on the dealii library. The errors occur after several hours of simulation, with the code unable to write to the file or the file not existing.

## Root Cause
The user is hitting the file limit on FASTTMP due to the large number of small files being written. The parallel file system on FASTTMP is not well-suited for handling many small files.

## Error Message
```
Exception thrown to main!!
--------------------------------------------------------
An error occurred in line <5163> of file
</tmp/iwtm020h/spack-stage/spack-stage-dealii-9.0.1-4ajf2zcxflpuxplcwxqvoe6n2v5tunbx/spack-src/source/base/data_out_base.cc>
in function
void dealii::DataOutBase::write_vtu_header(std::ostream&, const
dealii::DataOutBase::VtkFlags&)
The violated condition was:
out
Additional information:
An input/output error has occurred. There are a number of reasons
why this may be happening, both for reading and writing operations.
```

## Solution
1. **Reduce the number of files**: Instead of writing many small VTK files, switch to using HDF5 format to have one big file per time step.
2. **Use $WORK for output**: $WORK can handle a large number of small files better than FASTTMP. However, be mindful of the load on the fileserver and avoid writing too many files into huge directories.
3. **Spread files across directories**: To reduce the load on the filesystem, spread the files across multiple directories.

## Additional Notes
- There is no hard limit on the number of allowed files on $WORK, but too many files in a directory can hurt performance.
- Parallel output to $WORK may be slower for large files, but for small files, the overhead of the parallel filesystem on FASTTMP outweighs the benefits.
- If the user's workload negatively affects other users, the HPC admins may have to intervene.

## Documentation
- [HPC Storage Documentation](https://hpc.fau.de/systems-services/systems-documentation-instructions/hpc-storage/)
---

### 2024062642001647_Fritz%3A%20slow%20filesystem.md
# Ticket 2024062642001647

 ```markdown
# HPC-Support Ticket: Slow Filesystem on Fritz

## Keywords
- Slow filesystem
- High load on fileservers
- Login nodes
- Calculations affected

## Problem Description
- User reported slow access to the filesystem on Fritz, affecting both login nodes and calculations.

## Root Cause
- High load on some fileservers.

## Actions Taken
- HPC Admins are investigating the cause of the high load.

## Solution
- No solution provided yet; investigation ongoing.

## What Can Be Learned
- High load on fileservers can cause slow filesystem access.
- Investigation is necessary to identify the source of the high load.
- Users should be informed about ongoing issues and investigations.
```
---

### 2022011642000296_CPMD%20IO.md
# Ticket 2022011642000296

 # HPC Support Ticket: CPMD IO

## Keywords
- CPMD jobs
- I/O performance
- Restart frequency
- Job optimization

## Issue
- User's CPMD jobs were generating excessive I/O, impacting overall system performance.
- Jobs were writing a complete restart file every 500 steps, despite each step taking only 0.43 seconds.

## Root Cause
- The user had not optimized the restart frequency for their CPMD jobs, leading to unnecessary I/O operations.

## Solution
- The user was advised to review and optimize the restart frequency for all their jobs to reduce I/O and improve overall job efficiency.

## Lessons Learned
- Regularly review job configurations to ensure they are optimized for performance.
- Excessive I/O can negatively impact the performance of other jobs on the system.
- Adjusting the frequency of restart file writes can significantly reduce I/O and improve job efficiency.

## Action Items
- Users should check and optimize their job configurations to avoid excessive I/O.
- HPC Admins should monitor job performance and provide guidance to users as needed.
---

### 2024060642003138_Abbruch%20ORCA-Rechnungen%20Fritz%20-%20n100af.md
# Ticket 2024060642003138

 # HPC Support Ticket Conversation: Abbruch ORCA-Rechnungen Fritz

## Summary
- **User:** ORCA calculations on FRITZ are failing due to read/write errors.
- **Error:** Unable to open files during parallelization.
- **Solution:** Use `/dev/shm` for temporary files to avoid Lustre issues.

## Key Points
- **Initial Issue:** ORCA calculations aborting randomly due to read/write errors.
- **Error Messages:** Multiple processes unable to open files during SCF calculations.
- **Potential Causes:**
  - Lustre filesystem issues.
  - Recent system updates (AlmaLinux 8.10).
  - Possible hardware problems.
- **Troubleshooting Steps:**
  - Checked Lustre quota and inode limits.
  - Suggested using `/dev/shm` for temporary files.
  - Verified no known issues with Lustre.
  - Confirmed system updates did not affect modules but updated network and Lustre drivers.
- **User Feedback:**
  - Confirmed Lustre quota was not the issue.
  - Successfully ran calculations locally without errors.
  - Observed increased runtime on Lustre after updates.
- **Final Solution:**
  - Use `/dev/shm` for temporary files to avoid Lustre issues.
  - Monitor Lustre performance and consider increasing quota if necessary.

## Conclusion
The read/write errors in ORCA calculations on FRITZ were likely caused by Lustre filesystem issues. Using `/dev/shm` for temporary files resolved the problem. Monitoring Lustre performance and considering quota adjustments may be necessary for future calculations.

## Additional Notes
- **HPC Admins:** Provided detailed troubleshooting and suggested using `/dev/shm`.
- **2nd Level Support Team:** Assisted with testing and verifying the solution.
- **Head of Datacenter and Training and Support Group Leader:** Involved in higher-level support and training.
- **NHR Rechenzeit Support and Applications for Grants:** Provided additional support for grant applications.
- **Software and Tools Developer:** Assisted with software-specific issues.

This report can be used as a reference for similar errors in the future.
---

### 2025021942001737_Jobs%20on%20Fritz%20creating%20a%20high%20load%20on%20atuin%20%5Bk102de12%5D.md
# Ticket 2025021942001737

 # HPC Support Ticket: High Load on Atuin File System

## Keywords
- High load
- Atuin file system
- Job scripts
- rsync
- Simulation code
- Home directory

## Problem
- User submitted multiple jobs that created a high load on the Atuin file system.
- Job scripts contained an `rsync` command that copied simulation code to the working directory for each job in the array.

## Root Cause
- Unnecessary `rsync` command in job scripts causing excessive file system load.

## Solution
- Modify job scripts to keep simulation code in the home directory, reducing the load on the Atuin file system.

## Lessons Learned
- Avoid unnecessary file operations in job scripts, especially those that can cause high load on file systems.
- Store static code in the home directory to minimize file system load during job execution.

## Actions Taken
- HPC Admin advised the user to modify the job scripts.
- Ticket closed after job scripts were adjusted.

## References
- HPC Admin: Florian Lange
- Support Email: support-hpc@fau.de
- HPC Website: [FAU HPC](https://hpc.fau.de/)
---

### 2020032442000566_VASP%20Jobs%20on%20Emmy%20%281281387%2C1281388%20mptf008h%29.md
# Ticket 2020032442000566

 ```markdown
# HPC Support Ticket: VASP Jobs on Emmy

## Keywords
- VASP Jobs
- Job Stuck
- LD_PRELOAD Fix
- Lustre FS
- Emmy Cluster

## Summary
- **Issue**: Two VASP jobs (1281387, 1281388) got stuck on the Emmy cluster.
- **Root Cause**: The jobs were stuck due to an issue with the Lustre file system (elxfs).
- **Solution**: Apply the LD_PRELOAD fix to resolve the issue with the Lustre file system.

## Conversation Highlights
- **HPC Admin**: Notified the user that their jobs were stuck and suggested using the LD_PRELOAD fix.
- **User**: Acknowledged the issue and agreed to apply the fix.
- **HPC Admin**: Closed the ticket after confirming that the jobs were ended.

## Lessons Learned
- **LD_PRELOAD Fix**: Essential for resolving issues with Lustre file systems.
- **Proactive Monitoring**: Important for identifying and addressing stuck jobs promptly.
- **User Communication**: Effective communication with users helps in quick resolution of issues.
```
---

### 2024052142003236_Fritz%20_lustre%20problems.md
# Ticket 2024052142003236

 ```markdown
# HPC-Support Ticket: /lustre Problems

## Keywords
- Lustre
- Metadata server
- Reboot
- Hang
- Downtime
- HA-software

## Problem Description
After a reboot, the user experienced issues with the `/lustre` filesystem, causing commands like `ls` to hang indefinitely. The `/home` directory was functioning normally.

## Root Cause
One of the metadata servers for the Lustre filesystem was in a corrupted state. The HA-software was not functioning properly, leading to the issues.

## Solution
Rebooting the metadata server (`fmds01`) resolved the issue, and the Lustre filesystem started functioning normally again.

## Lessons Learned
- Issues with the Lustre filesystem can be caused by problems with metadata servers.
- Rebooting the affected metadata server can resolve the issue.
- Regular maintenance and monitoring of HA-software are crucial to prevent such issues.

## Ticket Closure
The ticket was closed after the issue was resolved.
```
---

### 2018110642000697_Jobs%20mppi019h%20LiMa.md
# Ticket 2018110642000697

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject: Jobs mppi019h LiMa

### Keywords:
- Job management
- File retrieval from tape
- System load
- Job scheduling
- Data storage optimization

### Root Cause of the Problem:
- Multiple jobs simultaneously requesting files from tape storage, causing high system load and contention for tape drives.

### Lessons Learned:
- **Job Management:** Ensure that jobs do not simultaneously request a large number of files from tape storage to avoid system overload.
- **File Retrieval:** Check the availability of files before submitting jobs to avoid unnecessary recall from tape.
- **System Load:** Monitor system load and adjust job scheduling to prevent performance degradation.
- **Data Storage:** Evaluate the necessity of using vault storage for large datasets and consider alternative storage solutions.

### Solution:
- **Pre-Job File Check:** Modify job submission scripts to check the availability of required files before starting the job. This can be done by attempting to read the last byte of each file.
- **Staggered Job Submission:** Limit the number of simultaneous jobs to prevent excessive file recall requests.
- **Storage Optimization:** Re-evaluate the use of vault storage for large datasets and consider other storage options that may be more suitable for frequent access.

### General Recommendations:
- **Communication:** Maintain open communication with users to understand their workflow and provide tailored solutions.
- **Documentation:** Document best practices for job submission and data management to prevent similar issues in the future.
- **Training:** Provide training sessions on efficient job scheduling and data management to users.

### Conclusion:
- The issue was resolved by placing jobs on hold and allowing the system to retrieve the necessary files from tape. Future occurrences can be prevented by implementing pre-job file checks and optimizing job scheduling.
```
---

### 2024112842001295_Access%20problems%20on%20Fritz.md
# Ticket 2024112842001295

 # HPC Support Ticket: Access Problems on Fritz

## Keywords
- Access problems
- Job freeze
- Lustre file system
- CPU usage
- Quota issues
- Memory bandwidth
- Server reset

## Summary
A user reported issues with running jobs freezing and being unable to access logs or list files in the Lustre file system. The problem was initially suspected to be related to high CPU usage by another user but was later identified as a file system issue.

## Problem Description
- User's running jobs froze and one quit.
- Unable to access logs or list files in Lustre.
- High CPU usage by another user was observed but ruled out as the cause.
- Quota command returned errors for $FASTTMP.
- Memory bandwidth dropped to zero across all processes.

## Root Cause
- The issue was traced to a problem with the $FASTTMP file system on Fritz.
- Specifically, some OSTs on `foss06` failed, causing disruptions in the file system.

## Solution
- The HPC Admin team identified and reset the server causing the problems on Fritz/Lustre.
- The file system recovered, and the user's jobs were extended by the time they were stuck.
- Two jobs that were not affected by the Lustre problems but were inactive were identified.

## Lessons Learned
- High CPU usage by a single user is not necessarily the cause of job freezes.
- File system issues can cause jobs to freeze and prevent access to logs and files.
- The `lfs quota` command can return errors if there are issues with the file system devices.
- Monitoring memory bandwidth can help identify file system issues.
- Resetting the affected server can resolve file system problems.

## Follow-up Actions
- Continue monitoring the file system for any further issues.
- Ensure that users are aware of how to check for file system problems and report them promptly.
- Document the steps taken to resolve the issue for future reference.
---

### 2022010642000895_Early-Alex%20%22Simon%20Bachhuber%22%20_%20iwb0003h.md
# Ticket 2022010642000895

 ```markdown
# HPC Support Ticket Analysis: Early-Alex User

## Keywords
- GPGPU cluster 'Alex'
- Nvidia A40 GPUs
- CUDA-driver
- Conda-package-manager
- Recurrent neural networks
- SQLite database
- Filesystem access
- /dev/shm
- Symlink

## Summary
A user was granted access to the 'Alex' GPGPU cluster for a project involving recurrent neural networks. The user's job was causing excessive filesystem access, specifically opening and closing SQLite database files multiple times per minute.

## Problem
- The user's job was frequently accessing SQLite database files located in the home directory, causing high I/O load.
- The files involved were:
  - `/home/hpc/iwb0/iwb0003h/jlib/exps/phi_0/optuna.db`
  - `/home/hpc/iwb0/iwb003h/jlib/exps/phi_0/optuna.db-journal`
  - `/home/hpc/iwb0/iwb003h/jlib/exps/phi_0_slow/optuna.db`
  - `/home/hpc/iwb0/iwb003h/jlib/exps/phi_0_slow/optuna.db-journal`

## Solution
- The user modified the code to use an in-memory SQLite database, reducing filesystem access.
- The user inquired about moving the database files to `/dev/shm` and creating a symlink in the home directory.
- The HPC Admin suggested that using a symlink might still result in frequent `*stat` calls in the home directory, which is not ideal.

## Lessons Learned
- Frequent filesystem access, even for small files, can cause significant I/O load on an HPC system.
- Using in-memory databases or temporary storage locations like `/dev/shm` can help mitigate this issue.
- Symlinks may not completely eliminate the problem of frequent filesystem access.

## Recommendations
- Users should be aware of the I/O impact of their jobs and consider using in-memory databases or temporary storage for high-frequency access files.
- HPC Admins should monitor filesystem access patterns and provide guidance to users on best practices for managing I/O-intensive jobs.
```
---

### 2024073142004169_Extremely%20long%20running%20times.md
# Ticket 2024073142004169

 ```markdown
# HPC Support Ticket: Extremely Long Running Times

## Summary
- **Issue**: Slow file system I/O operations causing extended job run times.
- **Root Cause**: High load on the shared file system due to excessive file counts.
- **Solution**: Optimize file usage and storage practices.

## Keywords
- File system I/O
- Slow performance
- Shared resources
- High load
- File count optimization

## Conversation Highlights
- **User**: Reported slow job run times, likely due to slow file system I/O.
- **HPC Admin**: Confirmed high load on the file system as the cause.
- **User**: Requested identification and resolution of the issue.
- **HPC Admin**: Provided file count data and suggested optimizations.
- **User**: Acknowledged the issue and planned to address it.

## Lessons Learned
- **Shared Resources**: High load on shared resources like storage can significantly impact performance.
- **File Count**: Excessive file counts can contribute to file system slowdowns.
- **Monitoring**: Regular monitoring and optimization of storage usage can help prevent performance issues.
- **User Education**: Providing guidelines and tools for efficient file management can help users optimize their storage usage.

## Action Items
- **Users**: Review and optimize file usage practices.
- **HPC Admins**: Continue to monitor and optimize storage infrastructure.
- **Support Team**: Provide resources and guidelines for efficient file management.

## Additional Resources
- [HPC Cafes](https://doc.nhr.fau.de/data/datasets/)
- [Workspaces Documentation](https://doc.nhr.fau.de/data/workspaces/)
```
---

### 2021020142001929_Jobs%20on%20Meggie%20862083%20iww1008h.md
# Ticket 2021020142001929

 # HPC Support Ticket: Jobs on Meggie 862083 iww1008h

## Keywords
- Performance issues
- GNU Parallel
- Ovito
- tar
- pigz
- SLURM jobs
- Thread management

## Problem
- User's jobs on Meggie show close to no performance.
- User is using Ovito and/or tar pigz in a loop, which is inefficient.

## Root Cause
- Inefficient use of resources due to sequential processing of tasks.
- Mismanagement of threads leading to excessive resource usage.

## Solution
- **Use GNU Parallel**: Replace loops with GNU Parallel to run multiple instances of Ovito/tar/pigz on the same node.
  ```bash
  cp /usr/bin/parallel $HOME/bin/
  export PATH=$PATH:$HOME/bin
  ```
- **Control Threads**: Ensure proper control of the number of threads for parallel and pigz to avoid excessive resource usage.
  ```bash
  ls *.chkpt | /home/hpc/iww1/iww1008h/bin/parallel "/home/hpc/iww1/iww1008h/bin/pigz-2.4/pigz {}"
  ```
- **Optimize Ovito Jobs**: Use GNU Parallel to run multiple Ovito jobs in parallel.
  ```bash
  ls *.chkpt.gz | parallel -j 4 ./run_ovito.sh {}
  ```

## Additional Notes
- **Avoid Using Two Nodes**: Ensure jobs are optimized to run on a single node unless necessary.
- **Replace pigz with gz**: Consider using gz instead of pigz to avoid excessive thread usage.

## References
- [GNU Parallel Manual](https://www.gnu.org/software/bash/manual/html_node/GNU-Parallel.html)

## Conclusion
Proper use of GNU Parallel and thread management can significantly improve job performance on HPC systems.
---

### 2023062242003083_Jobs%20on%20woody%20with%20much%20I_O%20-%20bco1101h.md
# Ticket 2023062242003083

 ```markdown
# HPC Support Ticket: High I/O Jobs on Woody

## Problem Description
- User's jobs on Woody with Job IDs 1736151, 1736150, 1736149, and 1736128 were causing high I/O, stressing the Gbit Ethernet network.
- The jobs were using ORCA, which produces a large number of temporary files.

## Root Cause
- The high I/O was due to the large number of temporary files generated by ORCA, which were stored in the user's work directory.
- Potential memory issues causing internal swapping were also suspected.

## Solution
- The user was advised to adapt their submit script to keep temporary files in node-local scratch directories.
- The HPC Admin team conducted benchmarks and found that ORCA-5.0.3 and ORCA-5.0.4 were not optimized for the processor architecture on the "big" Woody nodes. The ORCA modules were adjusted to automatically select the correct internal optimization.
- The user was recommended to use 32 cores on Woody or 64 cores on TinyFAT for better performance.

## Key Learnings
- High I/O jobs can be optimized by using node-local scratch directories.
- Proper optimization of software modules for the specific processor architecture can significantly improve performance.
- Increasing the number of cores can reduce computation time for certain types of jobs.

## Additional Notes
- The user provided an ORCA input file for benchmarking, which was used to identify the optimal configuration.
- The user's input was for a numerical frequency calculation of an organic molecule with 38 atoms, using a double-hybrid functional with a triple-zeta basis set.
- The HPC Admin team plans to document the findings for future reference and to create a success story.
```
---

### 2022011842003119_Simulation%20von%20einer%20Gro%C3%83%C2%9Fen%20Menge%20an%20Daten.md
# Ticket 2022011842003119

 # HPC-Support Ticket Conversation Summary

## Subject: Simulation von einer Großen Menge an Daten

### Keywords:
- Data simulation
- Deep learning
- Large datasets
- File handling
- Memory management
- Zoom meeting

### Problem:
- User wants to simulate datasets on the cluster for deep learning.
- Each dataset consists of 1 million files, each 10 kB in size.
- Files are written into a numpy array and then exported.
- Concerns about potential issues with handling such a large amount of data.

### Discussion:
- **HPC Admin**: Suggested holding data in memory instead of generating 1 million files.
- **HPC Admin**: Proposed appending data to a single file instead of creating multiple files.
- **HPC Admin**: Scheduled a Zoom meeting to discuss the issue further and find a suitable solution.

### Solution:
- **Zoom Meeting**: Discussed the pipeline and potential solutions.
- **Implementation**: Decided to implement a solution where worker nodes send data back to the master node, which then writes the data.

### Outcome:
- The ticket was closed after the user implemented the suggested solution.

### General Learnings:
- Handling large datasets efficiently requires careful consideration of memory management and file handling strategies.
- In-memory data storage can be more efficient than generating a large number of small files.
- Collaborative discussions via Zoom meetings can help in finding tailored solutions for complex problems.

### Next Steps:
- Monitor the implementation to ensure it meets the user's requirements.
- Document the solution for future reference and to assist other users with similar issues.

---

This summary provides a concise overview of the HPC-Support ticket conversation, highlighting the key points and the solution implemented. It serves as a documentation for support employees to refer to when dealing with similar issues in the future.
---

### 2025021742003373_Job%20on%20Alex%20does%20not%20use%20GPU%20_%20Data%20Staging%20can%20be%20optimized%20%5Bb198dc10%5.md
# Ticket 2025021742003373

 # HPC Support Ticket: Job on Alex does not use GPU / Data Staging can be optimized

## Keywords
- Job cancellation
- Data staging
- Node-local storage
- Compression algorithms
- Performance optimization

## Problem
- JobID 2393296 on Alex was cancelled after 2.5 hours due to prolonged data copying process for 145 GB.
- Inefficient data staging phase in the job script.

## Root Cause
- Unnecessary `rsync` command for copying data to node-local storage.
- Use of `gzip` compression algorithm, which slows down the unpacking process.

## Solution
- Remove the `rsync` command from the job script to avoid unnecessary data copying.
- Use uncompressed archives for faster data handling.
- If compression is necessary, use `lz4` or `zstd` instead of `gzip` for better performance.

## Additional Information
- Benchmark data on efficient data handling is available at the [HPC Café](https://hpc.fau.de/2025/02/04/monthly-hpc-cafe-efficient-packing-and-handling-of-large-data-sets-hybrid-event/).

## Contact
For further questions, contact the HPC support team via [support-hpc@fau.de](mailto:support-hpc@fau.de).
---

### 2019060742001166_Missbrauch%20von%20%24FASTTMP%20_%20mpkr21.md
# Ticket 2019060742001166

 # HPC Support Ticket: Misuse of $FASTTMP

## Keywords
- $FASTTMP
- Parallel file system
- Lustre write requests
- Job optimization
- Memory leaks

## Problem Description
The user's jobs on the Emmy system were generating an extreme load on $FASTTMP, affecting the entire system. The jobs were writing a massive number of files, with write requests ranging from 200k to 600k per second over several hours.

## Root Cause
The user's workflow involved writing a large number of small files continuously, which is not suitable for a parallel file system designed for infrequent but bursty writes of large binary files.

## Solution
- **Adjust Workflow**: The user was advised to modify their workflow to reduce the continuous writing of small files.
- **Acceptable Write Requests**: Typical acceptable values are bursts of a few hundred read/write requests every few minutes or hours.
- **Monitoring**: The user was advised to monitor other metrics besides memory leaks, such as read/write requests, to optimize job performance.

## Lessons Learned
- Parallel file systems like Lustre are designed for infrequent but bursty writes of large files, not continuous writing of small files.
- Monitoring job statistics for read/write requests is crucial for optimizing job performance and preventing system overload.
- Users should be aware of the acceptable usage patterns for shared resources like $FASTTMP.

## References
- [HPC Storage Documentation](https://www.anleitungen.rrze.fau.de/hpc/hpc-storage/)
- [Job Info on HPC Status](https://www.hpc.rrze.fau.de/HPC-Status/job-info.php)
---

### 2021121742002246_AW%3A%20Action%20required%20%28iwal060h%29%3A%20Last%20auf%20HPC-Home-Servern%20des%20RRZE%20_%20Loa.md
# Ticket 2021121742002246

 # HPC Support Ticket Conversation Summary

## Keywords
- High load on HPC home servers
- Metadata operations
- Multi-processing
- I/O operations
- GPU utilization
- Scratch directory
- Lazy copy
- Quota

## Problem
- High load on HPC home servers due to massive metadata operations (e.g., opening/closing files).
- User's jobs involve large databases that do not fit into RAM, requiring frequent file access from the hard drive.
- Multi-processing used to speed up data reading, leading to many file accesses per batch.
- Data stored in `/home/woody` causing significant I/O operations.

## Solution
- User proposed to zip databases and unzip them in the `/scratch` directory for each job.
- Alternatively, user suggested a "lazy" copy approach where files are copied from `/home/woody` to `/scratch` only when needed during the first epoch.
- HPC Admins approved the use of the `/scratch` directory for zipped files if space is sufficient.
- User implemented both solutions (`ssmvq-3` and `ssmvq-4`) and monitored GPU utilization.

## Outcome
- GPU utilization improved to >90%, indicating reduced dominance of I/O operations.
- User preferred the "lazy" copy approach due to minimal overhead.
- HPC Admins confirmed the correct quota for the `$WORK` directory is 500 GB.

## Additional Notes
- User clarified that I/O operations were intense but not dominant, with GPU utilization consistently high.
- HPC Admins will continue monitoring the jobs to ensure no further issues arise.

## Lessons Learned
- High I/O operations on home directories can cause significant load on HPC servers.
- Using the `/scratch` directory for temporary file storage can alleviate this issue.
- Implementing "lazy" copy strategies can minimize overhead and improve job efficiency.
- Regular monitoring and communication with users are essential for identifying and resolving performance bottlenecks.
---

### 2018070442001368_%24FASTTMP%20abuse%20_%20bctc47.md
# Ticket 2018070442001368

 # HPC-Support Ticket: $FASTTMP Abuse / bctc47

## Keywords
- File system slowdown
- Restart files
- Job optimization
- Account deactivation

## Problem Description
- User reported extreme slowness in the `emmy:/elxfs/bctc/` folder, affecting work.
- HPC Admin identified that the user's job was writing restart files every few seconds, causing high load on the file system.

## Root Cause
- Frequent writing of restart files and other regular file operations by the user's job led to file system overload.

## Solution
- HPC Admin advised the user to reduce the frequency of writing restart files and other regular file operations.
- User agreed to modify the code to address the issue.

## Additional Issues
- User reported account deactivation or inability to send jobs.
- No resolution provided in the conversation for the account deactivation issue.

## General Learnings
- Frequent file operations can overload the file system and impact overall performance.
- Users should optimize their jobs to minimize unnecessary file writes.
- Communication between users and HPC support is crucial for identifying and resolving performance issues.

## Next Steps
- Monitor the file system for similar issues.
- Provide guidance to users on best practices for file operations in HPC environments.
- Address the account deactivation issue if further details are provided.
---

### 2023121342002544_k103bf%20GrpNodeLimit.md
# Ticket 2023121342002544

 # HPC-Support Ticket: k103bf GrpNodeLimit

## Keywords
- AssocGrpNodeLimit
- Throttling
- IO problems
- /atuin filesystem
- /lustre filesystem
- Parallel IO

## Summary
- **User Query**: Requested information about their AssocGrpNodeLimit, which appeared to be low.
- **HPC Admin Response**:
  - The project's AssocGrpNodeLimit is 40 nodes, equating to 2.1M core-h per month.
  - Throttling was due to repeated IO problems caused by the user's jobs, affecting all users on the system.
  - The project is a normal project with 30M core-h on Fritz over 36 months, with a monthly contingent of 0.83M core-h.
- **User Follow-up**:
  - Acknowledged the IO problems, mentioning they are related to the /atuin filesystem.
  - Noted that other users are also experiencing these issues.
  - Informed that they have changed I/O-intensive programs to use parallel IO and write to /lustre.
  - Requested notification about updates/upgrades of /atuin.

## Root Cause
- Repeated IO problems caused by the user's jobs, specifically related to the /atuin filesystem.

## Solution
- The user has started using parallel IO and writing to the /lustre filesystem to mitigate IO issues.
- The user agreed to live with the current restriction and requested updates on /atuin improvements.

## General Learnings
- Throttling can be implemented due to excessive resource usage or issues caused by user jobs.
- Communication about filesystem issues and updates is crucial for user satisfaction.
- Encouraging users to adopt best practices (like parallel IO) can help alleviate system-wide problems.
---

### 2022110442002672_i9%20File%20Traffic.md
# Ticket 2022110442002672

 # HPC Support Ticket: i9 File Traffic

## Keywords
- File Traffic
- NFS Data
- GPU Utilization
- Scratch SSD
- Job Script Optimization

## Summary
The user reported high file traffic from the Informatik 9 group on the `woodyhome` storage. The HPC Admins investigated and provided insights into specific users and their job behaviors.

## Root Cause
- **High File Traffic**: Several users were identified as generating high file traffic due to frequent file operations.
  - **User 1**: Frequent file opens and modifications on `woodyhome`.
  - **User 2**: High file opens on `woodyhome`.
  - **User 3**: Inefficient data copying in job script, leading to prolonged file operations.
  - **User 4**: Java process not utilizing GPU.

## Findings
- **User 1**:
  - Job on TinyGPU with ~400 file opens per second.
  - Low GPU utilization (~10%).
- **User 2**:
  - Job on Alex with high file opens.
  - Low GPU utilization (~10%).
- **User 3**:
  - Job script copying a large number of files (2.275.928) for over 3.5 hours.
  - Suggestion to use a tar file for efficient data transfer.
- **User 4**:
  - Java process not utilizing GPU.

## Solution
- **Optimize File Operations**:
  - Educate users on efficient use of local scratch SSD.
  - Recommend using tar files for large data transfers.
- **Monitor GPU Utilization**:
  - Ensure jobs are optimized for GPU usage.
  - Provide guidance on improving GPU utilization.

## Action Taken
- The user was informed about the findings and will address the issues with the respective users.

## Conclusion
- High file traffic can be mitigated by optimizing job scripts and educating users on efficient data handling practices.
- Regular monitoring of job performance and file operations is essential for maintaining system efficiency.
---

### 2023052942000548_Slow%20filesystem%20on%20Fritz.md
# Ticket 2023052942000548

 # HPC Support Ticket: Slow Filesystem on Fritz

## Keywords
- Slow filesystem
- `/home/atuin`
- `ls` command delay
- Data read delay

## Problem Description
- User reported slow response when accessing the filesystem on Fritz, particularly on the `/home/atuin` filesystem.
- Symptoms included delays in executing `ls` commands and reading data from calculations.
- Issue started around Wednesday, 24th May, and lasted until Monday, 29th May.

## Ticket Conversation
- **User**: Reported slow filesystem access, mainly on the workspace filesystem.
- **HPC Admin**: Requested clarification on the specific filesystem and time window of the issue.
- **User**: Specified `/home/atuin` as the affected filesystem and provided the time window.
- **HPC Admin**: No server-side issues were found, and since the problem resolved, no further investigation was conducted.

## Root Cause
- The root cause of the slow filesystem access was not identified due to the intermittent nature of the issue and its resolution before detailed investigation.

## Solution
- No specific solution was implemented as the issue resolved itself.
- Users were advised to report any future issues for further investigation.

## Learnings
- Importance of specifying the affected filesystem and time window when reporting issues.
- Intermittent issues may resolve without intervention, but monitoring and reporting are crucial for identifying patterns or underlying problems.

## Next Steps
- Monitor the `/home/atuin` filesystem for any recurrence of slow access issues.
- Encourage users to provide detailed information when reporting problems to facilitate quicker resolution.
---

### 2022051742004925_inefficient%20job%20on%20Alex%20-%20iwal088h.md
# Ticket 2022051742004925

 # HPC Support Ticket: Inefficient Job on Alex

## Keywords
- Inefficient job
- Network blocking
- File server stress
- Data loading
- Memory optimization
- Compressed data
- /dev/shm

## Problem Description
- User's job on Alex was blocking the network and stressing the file server by repeatedly reading the same data at a rate of 150 MB/s.
- The data consisted of 3x 16 GB compressed files, which were being read multiple times.

## Root Cause
- The job was inefficiently reading compressed data files multiple times from the remote file system, causing excessive network and file server load.

## Solution
- **HPC Admin** suggested loading the data into main memory to reduce file system access.
- If the uncompressed data is too large for main memory, copy the files to `/dev/shm` on the node at the beginning of the job for faster access.
- The user implemented the suggestion by moving all data at once to the GPU, which significantly improved training speed.

## General Lessons Learned
- Repeatedly reading data from remote file systems can cause network congestion and stress on the file server.
- Loading data into main memory or using `/dev/shm` for temporary storage can improve job efficiency and reduce infrastructure load.
- Optimizing data handling can significantly improve job performance.

## Ticket Closure
- The ticket was closed after the user confirmed that the suggestions improved the job's performance.
---

### 2024061942002641_Handling%20large%20datasets%20on%20the%20HPC-cluster%20%5Bg101ea%5D.md
# Ticket 2024061942002641

 # Handling Large Datasets on the HPC Cluster

## Keywords
- Large datasets
- File system
- Download scripts
- Login node
- Job submission
- WORK file system
- Ceph storage
- Node-local resources

## Problem
A user had questions about handling a large dataset (~1.5T) on the HPC cluster:
1. Which file system to use for storing large datasets.
2. Whether to run a download script as a job or on the login node.

## Solution
1. **File System for Large Datasets**:
   - The `$WORK` file system is a good choice for storing large datasets.
   - An alternative high-performance option is the experimental Ceph storage.
   - Avoid storing a massive amount of very small files. Instead, store input files packed as archives on `$WORK` and unpack them in main jobs to node-local resources.

2. **Running Download Scripts**:
   - If the script only downloads files without post-processing, using the login node is fine. However, long-running processes may be killed, so a restart mechanism is recommended.
   - If the script requires substantial CPU resources, running it as a dedicated job is better. Additional resources on the CPU cluster Fritz may be granted with proper documentation.
   - Note: Downloading large amounts of YouTube data is prohibited, and general file number restrictions apply.

## General Learnings
- Understand the appropriate file systems for different types of data storage.
- Be aware of the limitations and best practices for running scripts on the login node versus submitting them as jobs.
- Consider the impact of file size and number on the performance and efficiency of the cluster.

## References
- [Ceph Storage Documentation](https://doc.nhr.fau.de/data/workspaces/)
- [Handling Large Datasets](https://doc.nhr.fau.de/data/datasets/)
- [Staging Data](https://doc.nhr.fau.de/data/staging/)
---

### 2022080142002399_Poor%20performance%20of%20jobs%20366684%20and%20366668%20on%20alex%20%20%28iwi5069h%29.md
# Ticket 2022080142002399

 # Poor Performance of Jobs on HPC Cluster

## Keywords
- Poor performance
- Data transfer
- File systems
- Tar/zip archive
- GPU utilization
- Nvidia A40
- Nvidia A100

## Problem Description
- Jobs 366684 and 366668 on the HPC cluster took several hours to copy 64 GB of data from `$WORK` to the node.
- The jobs did not utilize the GPUs during this time.
- The user was copying over 300K files, which caused significant delays.

## Root Cause
- Transferring a large number of small files individually is inefficient and causes performance issues.

## Solution
- **HPC Admin**: Suggested using tar/zip archives to transfer files. Provided a link to the document "Using File Systems Properly."
- **2nd Level Support**: Provided a code snippet to tar and transfer data efficiently.

```bash
# First tar your data (in ./Mydata) on your PC using this:
# tar -czvf ./Mydata.tar.gz ./Mydata
# and move .tar.gz file to HPC cluster
CLUSTER_DATA=$WORK/data/Mydata.tar.gz
# here is the target dir
SCRATCH_DATA_FOLDER=$TMPDIR/data
# move the data to the node /scratch
echo "Start data transfer: $(date '+%H:%M:%S')"
mkdir -p ${SCRATCH_DATA_FOLDER}
cp ${CLUSTER_DATA} ${SCRATCH_DATA_FOLDER}
tar -xzf ${SCRATCH_DATA_FOLDER}/Mydata.tar.gz -C ${SCRATCH_DATA_FOLDER}
echo "End data transfer: $(date '+%H:%M:%S')"
# Then your data will be in SCRATCH_DATA_FOLDER/Mydata
```

## Additional Notes
- The user reported that switching to Nvidia A40 GPUs resolved the issue temporarily, but the root cause was the inefficient data transfer method.
- The ticket was closed after the user was provided with the solution.

## Lessons Learned
- Transferring a large number of small files individually can significantly impact performance.
- Using tar/zip archives for data transfer is more efficient and reduces the load on the file system.
- Proper use of file systems is crucial for optimal performance on HPC clusters.
---

### 2024121542000201_Over%20disc%20quota%20%28c105aa11%29.md
# Ticket 2024121542000201

 # HPC Support Ticket: Over Disc Quota

## Keywords
- File quota
- Tar archives
- HDF5
- SLURM job
- Compression
- Staging
- $WORK directory
- $TMPDIR

## Problem
- User exceeded file quota (18 million files) in the directory `/home/atuin/c105aa/c105aa11`.
- Error occurred while copying files back to Atuin despite available disk space.

## Root Cause
- Too many small files stored, leading to file quota exceedance.

## Solution
- Consolidate data into fewer, larger files using formats like tar archives or HDF5.
- Use SLURM jobs to handle the compression task efficiently.
- Limit parallelization to 2 archives at a time to avoid overloading the file system.
- Pack data on $WORK and unpack directly on $TMPDIR of the compute node.

## Recommendations
- Group or batch small folders into a manageable number of tar files.
- Use specialized container formats (HDF5, NetCDF) for scientific datasets.
- Avoid copying and untarring on the compute node; instead, unpack directly on $TMPDIR.

## Additional Notes
- Staging technique: Copy and untar tar files on the compute node.
- Efficient use of resources: Limit parallelization to ensure efficient I/O operations.
- Future workflows: Combining many small files into a single, well-structured dataset can improve performance during archiving and analytics.

## References
- [Staging Documentation](https://doc.nhr.fau.de/data/staging/)
---

### 2025022742003658_Please%20use%20%24TMPDIR%20to%20store%20your%20training%20dataset%20%5Bb180dc22%5D.md
# Ticket 2025022742003658

 # HPC Support Ticket: Use $TMPDIR for Training Dataset

## Keywords
- I/O patterns
- File server
- Best practices
- Node-local storage
- Archive data
- Extract data
- HPC cafe

## Problem
- User's jobs showed moderate I/O patterns (~30 MB/s) to the file server.
- Inefficient use of shared resources.

## Root Cause
- User was not utilizing node-local storage for training datasets.

## Solution
- Pack data into an archive using `tar -cf /path-to/archive.tar /data-to-pack`.
- Extract data directly to node-local storage: `cd $TMPDIR; tar -xf /path-to/archive.tar`.
- Refer to HPC cafe for more information on efficient data handling: [HPC Cafe Link](https://hpc.fau.de/2025/02/04/monthly-hpc-cafe-efficient-packing-and-handling-of-large-data-sets-hybrid-event/).

## General Learning
- Always use node-local storage for large datasets to minimize I/O load on the file server.
- Archiving and extracting data to node-local storage is efficient and recommended.
- Follow best practices to ensure optimal use of shared HPC resources.
---

### 2024061042003862_Eingeschr%C3%83%C2%A4nkter%20Zugriff%20%20-%20mp24007h.md
# Ticket 2024061042003862

 # HPC-Support Ticket: Eingeschränkter Zugriff - mp24007h

## Problem
- **User Jobs Aborted**: User's jobs were aborted.
- **Restricted Access**: User's access was restricted to one node.
- **Root Cause**: User's MATLAB jobs caused excessive directory service requests (>100,000 requests per second), leading to a denial-of-service attack on the directory service.

## Communication
- **User**: Reported job abortions and restricted access, suspected overuse of resources.
- **HPC Admin**: Informed user about the excessive directory service requests and temporary restrictions.

## Actions Taken
- **HPC Admin**: Rebooted affected nodes to stop the denial-of-service attack.
- **HPC Admin**: Limited user to one running job until further analysis.
- **User**: Identified and planned to fix the issue in their MATLAB script.
- **HPC Admin**: Removed restrictions after user's request and explanation.
- **HPC Admin**: Re-applied restrictions to a maximum of 8 nodes due to recurring issues.

## Analysis
- **Directory Service Requests**: User's jobs made excessive requests to `passwd.byuid` and `netgroup`.
- **NSCD**: Name Service Cache Daemon (NSCD) helped mitigate the issue but took about 1 minute to be effective.

## Solution
- **User**: Identified and planned to fix the issue in their MATLAB script.
- **HPC Admin**: Limited user's access to prevent further disruptions.

## Keywords
- MATLAB jobs
- Directory service requests
- Denial-of-service attack
- NSCD
- Job restrictions
- Reboot nodes

## Lessons Learned
- Excessive directory service requests can cause significant disruptions.
- NSCD can help mitigate such issues but may take time to be effective.
- Users should be informed about the impact of their jobs on shared resources.
- Temporary restrictions can be applied to prevent further disruptions while issues are being resolved.
---

### 2021061642000921_File%20System%20on%20Emmy%20seems%20to%20have%20problems.......md
# Ticket 2021061642000921

 # HPC-Support Ticket: File System Issues on Emmy

## Keywords
- File System
- Emmy
- Lustre
- VASP
- scp
- FASTTMP
- WOODYHOME
- Parallel Computing
- Performance Issues

## Problem Description
- User experiencing issues with basic file operations (`ls`, `scp`) on Emmy.
- `scp` transfer stalls during the transfer of small files.
- Commands like `grep` take unusually long to complete.

## Root Cause
- High load on the parallel file system ($FASTTMP = /elxfs) due to increased usage and the file system being over 80% full.
- The file system is not optimized for small ASCII files, leading to performance degradation.

## Troubleshooting Steps
1. **Initial Response**: HPC Admin requested details about the programs used and the exact error message.
2. **Further Investigation**: User provided details about the `scp` command hanging during the transfer of small files.
3. **Admin Analysis**: HPC Admin confirmed high load on the file system and explained the performance issues with small ASCII files on a Lustre file system.

## Solution
- **Short-term**: User advised to use a different file system (e.g., Vault) for better performance.
- **Long-term**: User guided to start jobs from a different location and keep data in a more suitable directory to avoid excessive file system load.

## Additional Notes
- **Documentation**: HPC Admin provided a link to documentation on special applications and tips for VASP.
- **Follow-up**: User opened a new support ticket for further guidance on optimizing job scripts and file system usage.

## Conclusion
- The issue was related to high load and inefficient use of the parallel file system.
- Users should be aware of the limitations of parallel file systems and optimize their workflows accordingly.
- HPC Admins provided guidance on best practices and alternative file systems to mitigate performance issues.
---

### 2021121742002139_Re%3A%20Action%20required%20%28iwi5036h%29%3A%20Last%20auf%20HPC-Home-Servern%20des%20RRZE%20_%20Loa.md
# Ticket 2021121742002139

 # HPC-Support Ticket: High Load on HPC Home Servers

## Subject
Re: Action required (iwi5036h): Last auf HPC-Home-Servern des RRZE / Load on RRZE HPC home servers

## User
- **Issue**: User's jobs causing high load on HPC home servers due to many small file accesses.
- **Data Location**: `/home/hpc`
- **Data Characteristics**: 6.6 GB, 47115 files
- **Impact**: Slowing down the entire system and hindering other users.

## HPC Admin
- **Root Cause**: Massive metadata operations (opening/closing files) causing high load.
- **Solution**:
  - Pack data into an archive (zip or tar).
  - Unpack the archive at the start of the job on the local node.
  - Work with the unpacked data in a temporary directory.
  - Clean up the temporary directory at the end of the job.

## Steps Taken
1. **User Response**:
   - Acknowledged the issue and stopped running jobs.
   - Provided details about data size and number of files.
   - Tested the proposed solution and reported back with results.

2. **HPC Admin Guidance**:
   - Provided a script template for unpacking the archive and working with the data.
   - Suggested using the `time` command to measure the time taken for unpacking and processing.

3. **User Implementation**:
   - Implemented the script to unpack the archive and work with the data.
   - Reported that the unpacking took ~90 seconds and the processing time remained similar.

4. **Follow-up**:
   - User continued to run jobs with the new implementation.
   - No further issues reported.

## Conclusion
- The solution of packing data into an archive and unpacking it on the local node reduced the load on the home servers.
- The user was able to continue running jobs without causing further issues.
- The case was closed as no further problems were reported.

## Keywords
- High load
- Metadata operations
- Archive data
- Temporary directory
- Job script
- Performance measurement
- HPC home servers
- File access optimization
---

### 2023111542001874_Filesystem%20issues%20on%20Fritz%20_home_atuin.md
# Ticket 2023111542001874

 # HPC Support Ticket: Filesystem Issues on /home/atuin

## Keywords
- Filesystem sluggishness
- SLURM job time limit
- High load on file server
- Harmful IO patterns
- SLURM signals
- Node rebooting issues

## Problem Description
- Occasional slowness of the `/home/atuin` filesystem on Fritz.
- Jobs failing to complete file copying from temporary storage to `/home/atuin` before being killed by SLURM.
- Some jobs failing with errors related to socket timeouts and busy nodes.

## Root Cause
- High load on the file server due to harmful IO patterns of some jobs.
- Large number of small files being copied simultaneously.
- Node rebooting issues causing job failures.

## Solutions and Recommendations
- **Filesystem Sluggishness**:
  - Avoid copying a large number of small files at the end of jobs.
  - Consider copying larger files to `$FASTTMP` (/lustre) instead of `/home/atuin`.
  - Use SLURM signals to extend the time for file copying at the end of jobs. Refer to [GWDG documentation](https://docs.gwdg.de/doku.php?id=en:services:application_services:high_performance_computing:running_jobs_slurm:signals) for implementation details.

- **Job Failures**:
  - Node rebooting issues were identified and should be fixed.
  - Monitor for similar errors and report if they persist.

## Additional Notes
- The user is generally happy with Fritz's performance but seeks solutions for occasional filesystem sluggishness and job failures.
- The HPC Admins provided guidance on optimizing file copying and addressed recent node rebooting issues.

## Documentation for Future Reference
- **Filesystem Optimization**:
  - Minimize the number of small files being copied simultaneously.
  - Utilize `$FASTTMP` for larger files.
  - Implement SLURM signals to manage job time limits effectively.

- **Job Failure Troubleshooting**:
  - Check for node rebooting issues.
  - Monitor for socket timeout and busy node errors.

This documentation can be used to address similar issues in the future, ensuring efficient filesystem usage and job management on Fritz.
---

### 2024100442001402_Saturn%20gone%3F.md
# Ticket 2024100442001402

 # HPC Support Ticket: Saturn Gone from Fritz

## Keywords
- Saturn
- Fritz
- File server
- Service disruption
- High load
- Temporary removal
- National holiday

## Summary
A user reported that the `saturn` file server was not accessible from the `fritz` cluster, causing concern as the user had important data stored there.

## Root Cause
- The `saturn` file server was experiencing issues that caused systems trying to access it to hang.
- The problems could not be resolved quickly due to a national holiday and other ongoing issues.

## Solution
- The `/home/saturn` directory was temporarily removed to allow users not needing access to `saturn` to work normally.
- The server was brought back up, and `/home/saturn` was expected to reappear on systems within approximately 4 hours.

## Additional Information
- For updates, refer to the [service disruptions notice](https://hpc.fau.de/2024/10/03/service-disruptions-on-clusters-due-to-high-file-server-load-2/).

## Lessons Learned
- Temporary removal of problematic file servers can help maintain normal operations for other users.
- Communication about service disruptions and expected resolution times is crucial for user satisfaction.
- National holidays and other issues can delay the resolution of technical problems.
---

### 2024120642003046_FRITZ%20Lustre%20Slowdown.md
# Ticket 2024120642003046

 # HPC-Support Ticket Conversation: Lustre Slowdown

## Keywords
- Lustre
- Slowdown
- Job Freeze
- Data Loading
- Parallel File System

## Summary
A user reported that their jobs, which typically run quickly, were freezing upon loading the first snapshot. The user inquired whether this was a widespread issue with the parallel file system or if it was expected to be resolved soon.

## Root Cause
- **Issue**: Jobs freezing upon loading the first snapshot.
- **Possible Cause**: Slowdown in the Lustre file system.

## Solution
- **Action Taken**: The user canceled the affected jobs to avoid wasting resources.
- **Next Steps**: HPC Admins need to investigate the Lustre file system for any performance issues and provide an update on the expected resolution time.

## General Learnings
- **Monitoring**: Regularly monitor the performance of the Lustre file system to detect and address slowdowns promptly.
- **Communication**: Inform users about any known issues with the file system and provide estimated resolution times.
- **Troubleshooting**: Investigate and document common causes of Lustre slowdowns to expedite future troubleshooting.

## Follow-Up
- **HPC Admins**: Investigate the Lustre file system and update the user on the status and resolution of the issue.
- **2nd Level Support Team**: Assist in troubleshooting and provide additional support as needed.

## Documentation
- **Reference**: This ticket can serve as a reference for future incidents where jobs freeze due to Lustre slowdowns.
- **Updates**: Update this documentation with the findings and resolution steps once the issue is resolved.
---

### 2023122142001137_Action%20required%3A%20High%20load%20on%20%24WORK%20%28_home_atuin%29%20%5Bk101ee11%5D.md
# Ticket 2023122142001137

 ```markdown
# HPC Support Ticket: High Load on File System

## Subject
Action required: High load on $WORK (/home/atuin) [k101ee11]

## Issue Description
High load on the file system `atuin` due to screening jobs performing extensive read/write operations.

## Root Cause
- User running pharmacophore searches to create a database (LDB) and perform screening.
- Jobs divided into multiple small jobs to adhere to the 24-hour wall time constraint.
- High I/O operations from these jobs causing file system overload.

## Communication Summary
- **HPC Admin**: Notified user about high load and requested details about the jobs.
- **User**: Provided details about pharmacophore searches and database creation.
- **HPC Admin**: Scheduled a Zoom meeting to discuss the issue further.

## Solutions Discussed
- **HPC Admin**: Suggested copying input data to `/dev/shm` to reduce I/O load.
- **HPC Admin**: Proposed testing different parameters to optimize the Java Virtual Machine (JVM).

## Keywords
- High file system load
- Pharmacophore searches
- Database creation
- I/O operations
- Java Virtual Machine optimization
- `/dev/shm`

## Lessons Learned
- High I/O operations from single-core jobs can significantly impact the file system.
- Dividing jobs into smaller submissions may not always mitigate the issue.
- Copying input data to `/dev/shm` can help reduce I/O load on the file system.
- Optimizing JVM parameters can improve job performance and reduce resource usage.

## Next Steps
- User to implement suggested solutions and monitor file system load.
- Further discussion and optimization during the scheduled Zoom meeting.
```
---

### 2024042642000884_Work%20file%20system%20issues%20on%20Fritz.md
# Ticket 2024042642000884

 # HPC Support Ticket: Work File System Issues on Fritz

## Keywords
- Work filesystem
- Unresponsive commands
- Disk quota exceeded
- Inode limit
- Lustre filesystem

## Problem Description
- **User Issue 1:** The Work filesystem on Fritz becomes unresponsive to simple commands such as `ls`. The command hangs and is unresponsive to `ctrl+c` for extended periods.
- **User Issue 2:** The user encounters an error when trying to save files onto the Lustre filesystem: `cp: cannot create regular file './do_check_and_resubmit_if_unfinished_Hybrid_v2.sh': Disk quota exceeded`.

## Root Cause
- **User Issue 1:** High file server load causing unresponsiveness.
- **User Issue 2:** The user has exceeded the inode limit (files + directories) on the Lustre filesystem.

## Solution
- **User Issue 1:** Acknowledge the high file server load issue and refer to the service disruption notice: [Service Disruptions on Clusters Due to High File Server Load](https://hpc.fau.de/2024/04/19/service-disruptions-on-clusters-due-to-high-file-server-load/).
- **User Issue 2:** Inform the user about the inode limit and suggest reducing the number of files and directories. Provide the current inode usage:
  ```
  Disk quotas for user (uid 432140):
  Filesystem    used   quota   limit   grace   files   quota   limit   grace
  /lustre/  7.769T      0k      0k       -  106208*  80000  250000    none
  ```
  Suggest using the following command to check file counts in directories:
  ```bash
  for i in /lustre/iwst/iwst088h/*; do echo $i; find $i | wc -l; done
  ```

## General Learnings
- High file server load can cause unresponsiveness in the Work filesystem.
- Users can exceed inode limits even if there is ample storage space available.
- Regularly check and manage inode usage to avoid hitting limits.
- Provide users with commands to monitor their inode usage and suggest ways to reduce the number of files and directories.

## References
- [Service Disruptions on Clusters Due to High File Server Load](https://hpc.fau.de/2024/04/19/service-disruptions-on-clusters-due-to-high-file-server-load/)
---

### 2024021442002069_Antwortzeit%20fritz.md
# Ticket 2024021442002069

 # HPC Support Ticket: Antwortzeit fritz

## Keywords
- Login delay
- Fileserver issues
- Resource-intensive jobs on login node
- `top` command
- `ps -eaf` command
- `python`
- `ncks`
- `ncrcat`
- `ncl`

## Summary
A user reported a long login delay on the HPC system "fritz." The user suspected that resource-intensive jobs running on the login node might be the cause. The HPC Admin confirmed that there were fileserver issues, which were resolved shortly after the report.

## Root Cause
- Fileserver issues causing login delays.
- Resource-intensive jobs running on the login node, potentially contributing to the delay.

## Details
- The user experienced a login delay of over 1 minute on the HPC system "fritz."
- The user observed multiple resource-intensive jobs running on the login node, including several `python`, `ncks`, `ncrcat`, and `ncl` processes.
- The HPC Admin confirmed that there were fileserver issues, which were resolved shortly after the report.
- The user later reported that the login delay had improved, indicating that the fileserver issues were likely the primary cause.

## Solution
- The fileserver issues were resolved by the HPC Admin team.
- The user was advised to avoid running resource-intensive jobs on the login node to prevent potential delays for other users.

## Lessons Learned
- Fileserver issues can cause significant login delays on HPC systems.
- Running resource-intensive jobs on the login node can potentially exacerbate login delays and should be avoided.
- The `top` and `ps -eaf` commands can be used to identify resource-intensive jobs running on the login node.
- Regular monitoring and maintenance of fileservers are essential to prevent login delays.
- Users should be educated on the proper use of login nodes to avoid running resource-intensive jobs.
---

### 2024121142003287_Recurring%20Issues%20with%20Lustre%20File%20System.md
# Ticket 2024121142003287

 # Recurring Issues with Lustre File System

## Keywords
- Lustre file system
- Unresponsive system
- Evening downtime
- PuTTY access
- WinSCP connection issues
- StarCCM+ remote GUI
- OSS-servers
- Power outage
- FAU
- 24/7 operation

## Problem Description
- **User Report:** The Lustre file system becomes unresponsive every evening and does not respond to requests until the following day. Access via PuTTY is possible, but connections through WinSCP and loading files in the remote GUI of StarCCM+ fail.
- **Root Cause:** Individual OSS-servers for the Lustre file system stop handling requests properly, causing access to about 1/6th of the files to hang indefinitely. This issue started after a power outage.

## Diagnosis
- The problem is not user-specific or time-specific but related to the OSS-servers' misbehavior.
- The system usually starts working again in the morning after an admin diagnoses and resets the misbehaving server.

## Solution
- **Current Workaround:** Admins diagnose and reset the misbehaving server during working hours or in their spare time.
- **Long-term Solution:** The root cause of the OSS-servers' misbehavior is still unknown, and there is no ETA for a permanent fix.

## Notes
- FAU does not support 24/7 operation, so issues may persist until working hours.
- Admins are working to diagnose and resolve the underlying cause of the OSS-servers' misbehavior.

## Related Parties
- **HPC Admins:** Responsible for diagnosing and resetting the misbehaving servers.
- **FAU:** Decision-maker regarding 24/7 operation support.

## Troubleshooting Steps for Support Employees
1. Check if the issue is related to OSS-servers' misbehavior.
2. If confirmed, reset the misbehaving server.
3. Inform the user about the current workaround and the ongoing efforts to find a permanent solution.
---

### 2024112842002089_Trainingslogs%20rausschreiben%20-%20b185cb%20_%20Datenbank_Messaging-Server%20f%C3%83%C2%BCr%20Sync%.md
# Ticket 2024112842002089

 # HPC-Support Ticket: Trainingslogs rausschreiben - b185cb

## Keywords
- Trainingslogs
- Datenbank
- Message Queue
- Apache ActiveMQ
- OpenTSDB
- Redis
- Distributed Logging
- Training Restarts

## Problem
- User wants to log a large number of small data points during training runs on new H100 nodes over the Christmas period.
- Logging should be distributed and synchronized across all compute nodes and threads without causing delays or issues with training restarts.

## Considered Solutions
1. **File-based Logging**: Open a file per thread and node and write to a network share.
   - Concerns: Write delay, inelegant solution.
2. **OpenTSDB**: Use a distributed database for logging.
   - Concerns: Training depends on a functioning database connection, potential point of failure.
3. **Redis**: Use a distributed Redis database for logging and stream input to a file.
   - Concerns: Similar to OpenTSDB, dependency on database connection.

## Suggested Solution
- **Apache ActiveMQ**: Use a message queue for asynchronous communication with caching and prefetch capabilities.
  - Benefits: Minimal delay, handles training restarts well, reduces dependency on a single point of failure.

## Additional Information
- HPC infrastructure does not have central instances of databases or message queues running.
- The status of the Helma-H100 system and user access over the Christmas period is not yet finalized.
- The supplier is currently dealing with cooling infrastructure and power supply issues.

## Next Steps
- User will explore Apache ActiveMQ for suitability in their use case.

## Conclusion
- Message queues like Apache ActiveMQ are recommended for distributed logging in HPC environments to minimize delays and handle training restarts effectively.

---

This report provides a summary of the HPC-Support Ticket conversation and outlines the problem, considered solutions, suggested solution, additional information, next steps, and conclusion. It serves as a documentation for support employees to look up help for similar issues in the future.
---

### 2017020342000194_FASTTMP.md
# Ticket 2017020342000194

 ```markdown
# HPC-Support Ticket: FASTTMP

## Keywords
- cp command
- mv command
- vim
- system hang
- Maggie
- MDSe
- external storage array

## Summary
The user experienced issues with executing `cp` and `mv` commands and saving files in `vim`. The system appeared to hang or become unresponsive.

## Root Cause
The problem was traced to the MDSe (Metadata Servers) having issues, possibly related to the external storage array.

## Solution
The issue was escalated to Megware for further investigation and resolution.

## Lessons Learned
- Always specify the exact system (e.g., meggie1, meggie2, specific node) when reporting issues.
- Issues with `cp`, `mv`, and `vim` can indicate problems with the metadata servers or storage array.
- Escalate storage-related issues to the appropriate vendor for resolution.
```
---

### 2021121742002157_Re%3A%20Action%20required%20%28iwal058h%29%3A%20Last%20auf%20HPC-Home-Servern%20des%20RRZE%20_%20Loa.md
# Ticket 2021121742002157

 # HPC Support Ticket: High Load on HPC Home Servers

## Root Cause
- High load on HPC home servers due to massive metadata operations (e.g., opening/closing files).
- User's job involves many small file accesses, distributed over many files, causing significant load on the filesystem.

## Symptoms
- Frequent file accesses (~50 files per second).
- Multiple jobs running simultaneously, accessing the same data.

## Solution
- **Optimize File Access**:
  - Load data into RAM once and use it from memory.
  - Alternatively, copy data to a local directory (`$TMPDIR`) at the beginning of the job script if space allows.
- **Data Format**:
  - Preprocess and package the dataset in HDF5 format to reduce the number of file accesses.

## Steps Taken
1. **User Response**:
   - Acknowledged the issue and agreed to optimize the workflow.
   - Proposed to load all data into RAM and stream from a single HDF5 file.

2. **HPC Admin Response**:
   - Confirmed that the user's job looks good after optimization.
   - Encouraged the user to start a job and monitor the load.

## Outcome
- The user's job was optimized to reduce the load on the filesystem.
- HPC Admin confirmed that the optimized job did not cause significant load issues.

## Notes
- The user was advised to avoid frequent file accesses on network volumes.
- The solution involved loading data into RAM and using a more efficient data format (HDF5).

## Keywords
- High load
- Metadata operations
- Small file accesses
- RAM optimization
- HDF5 format
- Local directory (`$TMPDIR`)
- Job optimization
- Filesystem load

## General Learning
- Frequent small file accesses on network volumes can cause significant load on HPC home servers.
- Optimizing workflows to reduce file accesses, such as loading data into RAM or using local directories, can mitigate this issue.
- Preprocessing data into more efficient formats like HDF5 can further improve performance and reduce load.
---

### 2022093042000932_jobs%20epoch%20start%20much%20slower%20than%20expected.md
# Ticket 2022093042000932

 # HPC Support Ticket: Jobs Epoch Start Much Slower Than Expected

## Keywords
- Job slowdown
- Epoch initialization
- High load
- Data transfer
- Workflow optimization

## Summary
The user reported a significant slowdown in their jobs on the A100 HPC cluster, specifically during the initialization phase at the start of each epoch. The issue was observed to be around 3x to 6x slower than usual.

## Root Cause
- High load on the HPC server (Janus) was identified as a potential cause.
- The user's workflow involved copying zipped data to the `/scratch` folder and loading a long .csv file to RAM during initialization.

## Solution
- The HPC Admins investigated the issue and contacted users with non-optimal workflows to reduce the load on the server.
- The user was advised to optimize their workflow by using a dedicated directory for their data to avoid unnecessary data transfer and reduce network I/O operations.

## Additional Information
- The user suggested features for improving job scheduling and data management, such as viewing the job queue and having a dedicated filesystem for each user.
- The HPC Admins provided information on the `--start` option in `sbatch` for viewing the expected start time of pending jobs.
- The HPC Admins explained the limitations of providing dedicated filesystems for each user due to the large number of users and limited resources.

## Conclusion
The issue was addressed by optimizing workflows and reducing the load on the server. The user was provided with additional information on job scheduling and data management to improve their workflow in the future.
---

### 2024022742000402_lustre%20on%20Fritz%20is%20not%20working.md
# Ticket 2024022742000402

 # HPC Support Ticket: Lustre Access Issue

## Keywords
- Lustre
- File system
- Access issue
- Linux
- Start script
- Reboot

## Summary
A user reported an issue accessing a specific directory on the Lustre file system, receiving an error message indicating the directory does not exist.

## Root Cause
The issue was likely caused by a recent cleanup of start scripts, which may have inadvertently removed or disabled the script responsible for mounting the Lustre file system on the frontend nodes.

## Solution
The HPC Admin reactivated the `copyin/start-lustre.sh` script on all four frontend nodes. The effectiveness of this solution will be verified after the next reboot.

## Lessons Learned
- Regular maintenance and cleanup activities can have unintended side effects.
- It is important to carefully review and test changes to start scripts and other critical system components.
- Monitoring and logging can help quickly identify and resolve issues related to file system access.

## Follow-up Actions
- Verify that the Lustre file system is properly mounted after the next reboot.
- Consider implementing additional monitoring or alerts for file system access issues.
- Review and document the startup process for the Lustre file system to prevent similar issues in the future.
---

### 2019122042000371_SSD%20auf%20Meggie%20Frontend%3F.md
# Ticket 2019122042000371

 # HPC Support Ticket: SSD auf Meggie Frontend?

## Keywords
- SSD
- Meggie Frontend
- /scratch
- /lxfs
- ZIP
- tar/tgz
- bzip2
- xz
- pbzip2
- pixz

## Problem
- User needs to unpack many millions of small files from ZIP archives and repackage them into larger ZIP archives to be stored on Meggie's /lxfs.
- User inquires about the availability of SSDs on Meggie Frontends or other machines with access to /lxfs.

## Solution
- **SSD Availability**:
  - /scratch on Meggie Frontends is not an SSD but a RAID with 2 classic 3.5" 7200 rpm 1 TB hard drives.
  - Memoryhog does not have SSDs.
  - Machines tf04X and tf05X in TinyFat have local SSDs (1 TB Intel 750) and are less loaded, making them a viable option.

- **Alternative Compression Methods**:
  - Suggested switching from ZIP to tar/tgz to avoid metadata operations and reduce file size.
  - User decided to switch to bzip2 (pbzip2) after comparing compression sizes.
  - HPC Admin suggested xz as an alternative, mentioning its multithreading capabilities and the availability of pixz.

- **Software Installation**:
  - pbzip2 was installed on Meggie login nodes.

## General Learnings
- **Compression Efficiency**:
  - ZIP compresses each file individually, leading to larger file sizes for small files compared to tar/tgz or tar.bz2.
  - bzip2 offers better compression ratios for small files compared to gzip.

- **Hardware Utilization**:
  - Understanding the hardware capabilities of different machines (e.g., SSD availability) can help optimize task performance.
  - Less loaded machines can be utilized for resource-intensive tasks.

- **Software Recommendations**:
  - Evaluating different compression tools (e.g., xz, pixz) can provide better performance and compatibility.
  - Installing required software (e.g., pbzip2) on relevant nodes can facilitate user tasks.

## Follow-up
- User will consider switching to bzip2 for future jobs.
- HPC Admin will continue to provide support and suggestions for optimizing compression and hardware utilization.
---

### 2024080542003896_No%20download%20jobs%20on%20A100%20GPUs%20%5Biwb6006h%5D.md
# Ticket 2024080542003896

 ```markdown
# HPC Support Ticket: No Download Jobs on A100 GPUs

## Keywords
- Download jobs
- A100 GPUs
- TinyGPU
- Woody cluster
- Archiving data
- Node-local disk
- $TMPDIR

## Problem
- User attempted to run a download job on TinyGPU (JobID 870850) which was not utilizing the A100 GPU.

## Root Cause
- Download jobs are not suitable for the TinyGPU cluster as they do not utilize the A100 GPU.

## Solution
- **Redirect to Appropriate Cluster**: Use the Woody cluster for downloading data from the internet.
- **Archive Data**: After downloading and pre-processing images, archive the data using `tar` or `zip`.
- **Extract to Node-Local Disk**: Extract archived data directly to the node-local disk, accessible via `$TMPDIR`.

## General Learning
- Ensure download jobs are run on clusters designed for such tasks, like the Woody cluster.
- Archive large datasets to optimize storage and transfer efficiency.
- Utilize node-local disk for temporary storage during job execution.

## References
- [Woody Cluster Documentation](https://doc.nhr.fau.de/clusters/woody/)
```
---

### 2025030542002215_high%20load%20on%20atuin%20%5Bv103fe18%5D.md
# Ticket 2025030542002215

 # HPC Support Ticket: High Load on Atuin

## Keywords
- High IO load
- Checkpointing
- $TMPDIR
- $WORK
- Model safes
- Epochs

## Problem Description
- User's jobs were causing high IO load on the `atuin` cluster, despite moving data to `$TMPDIR`.
- Root cause: Frequent model checkpointing after each epoch, leading to excessive IO operations.

## Solution
- Reduce the frequency of model checkpointing. Instead of saving after every epoch, adjust to save every 5th epoch.
- Use `$TMPDIR` for storing checkpoints during the job runtime and copy only the best checkpoints to `$WORK` at the end of the job.

## General Learnings
- Frequent IO operations, such as excessive checkpointing, can lead to high load on the cluster.
- Utilize temporary directories like `$TMPDIR` for intermediate data to reduce IO load on shared storage.
- Adjusting the frequency of IO operations can help mitigate high load issues.
- Engage with users to understand their workflows and provide tailored advice for optimizing their jobs.

## Follow-up
- Monitor the IO load to ensure the issue is resolved.
- Close the ticket if the IO load is confirmed to be lower.
---

### 2021052742002679_IS%20THERE%20SOMETHING%20WRONG%20IN%20CLUSTER%3F%3F%3F.md
# Ticket 2021052742002679

 ```markdown
# HPC Support Ticket: Slow GPU Job Performance

## Subject
IS THERE SOMETHING WRONG IN CLUSTER???

## User Issue
- User reported slow performance of GPU jobs on the cluster compared to a local GPU.
- Job runs 32 hours for one epoch on the cluster vs. 5 hours on a local GPU.

## Root Cause
- Data was not copied to node-local SSD (`/scratchssd`), causing slow data access over the network.
- Large number of small files being transferred, leading to inefficient data transfer.

## Solution
- Copy training data to `/scratchssd` at the beginning of the job.
- Use archives (zip/tar) to transfer large datasets to reduce the number of files being transferred.
- Consider using archive/database formats suited for machine learning to efficiently handle large datasets.

## Keywords
- GPU performance
- Data transfer
- Node-local SSD
- Large datasets
- Archive formats

## General Learnings
- Always ensure data is copied to node-local storage for faster access.
- Transferring a large number of small files over the network is inefficient.
- Use archives or specialized formats to handle large datasets efficiently.
```
---

### 2023051142001535_Multidir%20Gromacs%20Jobs%20on%20Alex%20limit%20Saturn%20use%20for%20everyone%20%5Bbccb002h%5D.md
# Ticket 2023051142001535

 ```markdown
# HPC Support Ticket: Multidir Gromacs Jobs on Alex Limit Saturn Use for Everyone

## Subject
Multidir Gromacs Jobs on Alex limit Saturn use for everyone

## Keywords
- Gromacs
- Multidir jobs
- High I/O load
- Slurm dependency
- Temporary directory ($TMPDIR)
- Block time

## Problem
- User's Gromacs jobs were causing high I/O load on the Saturn file server.
- Each simulation was writing four files, leading to ~250 files per job.
- Eight simultaneous jobs resulted in ~2,000 files being written and read, overwhelming the file server.

## Root Cause
- High number of simultaneous file operations due to multidir Gromacs jobs.
- Large files (e.g., `*.xtc`) being written and read frequently.

## Solution
- **Immediate Action**: Cancel all but one of the user's jobs to reduce load.
- **Long-term Solution**:
  - Limit the number of simultaneous jobs.
  - Use Slurm dependency to start new jobs only after others have terminated.
    ```bash
    --dependency=afterany:job_id[:job_id]
    ```
  - Consider using block time to run jobs on a single node using $TMPDIR.
  - Copy data to $TMPDIR at the start of the job and back to $WORK at the end.
  - Use `-noappend` option in Gromacs to manage output files more efficiently.

## Additional Notes
- The largest files (`*.xtc`) should be managed carefully to avoid excessive I/O load.
- Future jobs with similar requirements should be handled with block time to minimize impact on the file server.
- Regular monitoring of file server load is essential to prevent performance degradation.

## Conclusion
- High I/O load from multidir Gromacs jobs can be mitigated by limiting simultaneous jobs, using Slurm dependencies, and managing file operations efficiently.
- Proper use of temporary directories and block time can help in managing large-scale simulations without overwhelming the file server.
```
---

### 2024101042002266_Status%20of%20Alex.md
# Ticket 2024101042002266

 # HPC Support Ticket: Status of Alex

## Keywords
- File server downtime
- High load on file server
- Slow job performance
- Workspaces on ANVME

## Summary
- **User Issue:** Jobs submitted to the HPC cluster are experiencing slow performance, particularly when loading models from the file server.
- **Root Cause:** High load on the file server (atuin) causing slowdowns.
- **Solution:** Use workspaces on ANVME to speed up model loading.

## Detailed Conversation
- **User:** Noticed file server downtime and subsequent slow job performance.
- **HPC Admin:** Confirmed high load on the file server and suggested using workspaces on ANVME for faster model loading.
- **User:** Acknowledged the suggestion and agreed to try it.

## Lessons Learned
- High load on the file server can cause significant slowdowns in job performance.
- Using workspaces on ANVME can help mitigate these issues by providing faster access to data.

## Recommendations
- Monitor file server load and consider using alternative storage solutions like ANVME workspaces during high load periods.
- Inform users about the availability and benefits of using ANVME workspaces for improved performance.

## References
- [Service Disruptions on Clusters Due to High Load on Fileserver Atuin](https://hpc.fau.de/2024/10/09/service-disruptions-on-clusters-due-to-high-load-on-fileserver-atuin/)
- [Workspaces on ANVME](https://doc.nhr.fau.de/data/workspaces/)
---

### 2024112042001755_Performance%20issues%20of%20Fritz%20headnodes_filesystem.md
# Ticket 2024112042001755

 # HPC Support Ticket: Performance Issues of Fritz Headnodes/Filesystem

## Keywords
- Performance issues
- Headnodes
- Filesystem
- Simple commands delay
- Heavy I/O
- Interactive jobs
- Workspaces

## Problem Description
- **User Group**: Active users of the Fritz cluster (project b146dc).
- **Issue**: Regular performance issues with headnodes or filesystem, causing delays in executing simple commands like `ls`, `cd`, or `vim` for small files.
- **Duration**: Issue persists for minutes to hours.
- **Assumption**: Caused by spikes in usage from other users copying large files.

## Root Cause
- **Observation**: Massive load on file servers.
- **Potential Cause**: Heavy I/O operations by other users affecting the shared filesystem.

## Solution/Recommendations
- **Immediate Action**: Encourage users to start interactive jobs for data movement or postprocessing.
- **Long-term Solutions**:
  - Educate users to move data to local disks or newly available workspaces.
  - Monitor and reach out to users running jobs with heavy I/O to improve their workflow.
  - Consider hardware updates or replacements to address the underlying issues.

## General Learnings
- **User Education**: Importance of using interactive jobs and workspaces for heavy I/O tasks.
- **Monitoring**: Continuous monitoring of jobs and user activities to identify and address heavy I/O usage.
- **Hardware Considerations**: Potential need for hardware updates to improve filesystem performance.

## Future Actions
- **Monitoring**: Enhance monitoring to detect and mitigate heavy I/O usage.
- **User Notifications**: Notify users about best practices for file management and I/O operations.
- **Hardware Planning**: Consider hardware updates or replacements to improve overall system performance.

---

This documentation aims to provide a reference for support employees to address similar performance issues in the future.
---

### 2024041942003662_%24WORK.md
# Ticket 2024041942003662

 ```markdown
# HPC-Support Ticket: $WORK Filesystem Issues

## Keywords
- $WORK Filesystem
- Performance Issues
- System Commands Delay
- Regular Access

## Problem Description
- User reported significant delays in system commands, making regular work impossible.
- The issue is related to the $WORK filesystem.

## Root Cause
- Unspecified problem with the $WORK filesystem causing performance degradation.

## Solution
- Not specified in the provided conversation.

## Actions Taken
- User inquired about the known status of the issue and expected resolution time.

## Lessons Learned
- Performance issues with the $WORK filesystem can severely impact user productivity.
- Regular monitoring and maintenance of the filesystem are crucial to prevent such issues.
- Communication with users about known issues and expected resolution times is important for managing expectations.
```
---

### 2024013042002932_Data%20Loading%20for%20single-GPU%20jobs.md
# Ticket 2024013042002932

 # HPC Support Ticket: Data Loading for Single-GPU Jobs

## Keywords
- Multi-GPU jobs
- Single-GPU jobs
- Data copying
- Ceph
- Pod’s local directory
- SSD space
- RAM
- Job runtime
- Deadline
- /tmp directory
- --hold flag
- Locking mechanism

## Problem
- User needs to handle large dataset (500GB) for single-GPU jobs.
- Concerns about data duplication, SSD space usage, and RAM limitations.
- Current approach: Copying data from Ceph to pod’s local directory.

## Root Cause
- Copying large datasets to local directories for multiple jobs can lead to data duplication, excessive SSD usage, and RAM limitations.

## Solution
- Use `/tmp` directory for shared data access among jobs on the same node.
- Implement a locking mechanism to check if data is already being transferred by another job.
- Start jobs with the `--hold` flag to allow HPC admins to shift jobs to specific nodes, thereby gathering them on a node.

## General Learnings
- Shared directories like `/tmp` can help avoid data duplication.
- Locking mechanisms can prevent redundant data transfers.
- Using the `--hold` flag provides flexibility for job scheduling and resource management.

## Notes
- HPC cluster is currently busy, and job completion by the deadline cannot be guaranteed.
- Jobs may start on different nodes, not sharing the `/tmp` directory.

---

This documentation can be used to address similar issues related to data handling and job scheduling in HPC environments.
---

### 2023090642000735_Slow%20I_O%20on%20the%20HPC%20cluster%20-%20b112dc10%20_%20b112dc12.md
# Ticket 2023090642000735

 # HPC Support Ticket: Slow I/O on the HPC Cluster

## Keywords
- Slow I/O
- Python script
- Conda environment
- Storage performance
- High load on storage server
- Data copying

## Problem Description
- User unable to run a Python script on the frontend.
- Issues with importing `torch` in the Python environment.
- Slow I/O operations when copying files from one location to another.

## Root Cause
- High load on the storage server `atuin`, which is the user's `$WORK` directory.
- Large number of files and significant storage usage in the user's Conda environment.

## Solution
- The storage server `atuin` experienced high load, which was resolved.
- Users were advised to avoid unnecessary data copying to prevent cluttering filesystems.
- Recommended using shared datasets to reduce redundancy and improve performance.

## Lessons Learned
- High load on storage servers can cause slow I/O operations.
- Avoiding redundant data copies can improve storage performance.
- Shared datasets should be used to prevent multiple copies of the same data.
- Monitoring storage usage and load can help in identifying performance issues.

## Actions Taken
- HPC Admins checked storage usage and file counts in the user's Conda environment.
- The high load on the storage server was addressed.
- Users were advised to use shared datasets and avoid unnecessary data copying.

## Recommendations
- Regularly monitor storage usage and performance.
- Encourage users to use shared datasets to prevent redundancy.
- Educate users on best practices for data management to improve overall system performance.
---

### 2018042042001146_Beratungsgespr%C3%83%C2%A4ch%20HPC%20_%20bctc14.md
# Ticket 2018042042001146

 # HPC Support Ticket Conversation Analysis

## Keywords
- HPC System Efficiency
- Workflow Optimization
- High I/O Rates
- Parallel File System Misuse
- Job Termination
- Performance Monitoring
- User Consultation

## Summary
The conversation revolves around optimizing the workflow of a high-usage HPC user to improve system efficiency. The user's jobs were identified as causing high I/O rates, leading to performance issues on the parallel file system. The HPC admins attempted to schedule a consultation to understand and optimize the user's workflow but faced resistance.

## Root Cause of the Problem
- **High I/O Rates**: The user's jobs were generating a high number of small I/O requests, causing performance degradation on the parallel file system.
- **ASCII File Usage**: The user was writing ASCII files to the parallel file system, which is designed for large binary files.

## Solutions and Actions Taken
- **Job Termination**: The HPC admins terminated the user's jobs to restore system performance.
- **User Consultation**: The admins repeatedly offered to consult with the user to optimize their workflow but faced resistance.
- **Resource Limitation**: The user's account was limited to one running job at a time to mitigate the impact on the system.
- **Priority Increase**: Despite the user's history of causing system issues, the admins temporarily increased the priority of the user's jobs to help them meet a deadline.

## General Learnings
- **Importance of Proper I/O Usage**: Users should be educated on the proper use of I/O resources to prevent system degradation.
- **User Consultation**: Regular consultation with high-usage users can help optimize workflows and prevent system issues.
- **Monitoring and Enforcement**: Continuous monitoring and enforcement of resource usage policies are necessary to maintain system performance.
- **Flexibility in Support**: While it's important to maintain system performance, exceptions can be made to support users in exceptional circumstances.

## Documentation for Future Reference
This case highlights the importance of proper I/O usage and the need for regular user consultation. If similar issues arise, HPC support employees should:

1. **Monitor I/O Rates**: Keep an eye on users generating high I/O rates, especially those writing small ASCII files to the parallel file system.
2. **Offer Consultation**: Proactively offer consultation to high-usage users to optimize their workflows.
3. **Enforce Policies**: Don't hesitate to enforce resource usage policies, including job termination if necessary.
4. **Be Flexible**: While enforcing policies, be open to making exceptions when warranted.

By following these guidelines, HPC support employees can help maintain system performance while supporting users' needs.
---

### 2021121642003051_Re%3A%20Action%20required%3A%20Last%20auf%20HPC-Home-Servern%20des%20RRZE%20_%20Load%20on%20RRZE%20H.md
# Ticket 2021121642003051

 # HPC Support Ticket: High Load on HPC Home Servers

## Keywords
- High load
- Metadata operations
- Home servers
- File access
- Job load
- RAM loading
- Data consolidation
- TMPDIR
- HDF5
- tar/zip archives

## Problem Description
The HPC home servers at RRZE were experiencing high load, particularly affecting the file systems `/home/hpc`, `/home/vault`, and `/home/woody`. This was attributed to massive metadata operations such as opening and closing files, which slowed down the entire system and hindered other HPC users.

## Root Cause
The user was utilizing a speech-separation dataset consisting of 20,000 training files (wav files). This resulted in many small file accesses distributed over numerous files, potentially causing the high load on the home servers.

## Solution
1. **Data Consolidation**: The user was advised to consolidate multiple audio files into a single file.
2. **Loading Data into RAM**: The user started loading the dataset into RAM at the beginning of the process, which reduced file access operations.
3. **Using TMPDIR**: The user was advised to copy the consolidated data to `$TMPDIR` to minimize access to the home directories.
4. **Data Formats**: Suggested using hierarchical data formats like HDF5 or simple tar/zip archives, which can be unpacked in `$TMPDIR`.

## Outcome
After implementing the suggested solutions, the user's jobs appeared to be running smoothly without causing significant load on the home servers. The HPC Admin confirmed that the jobs were no longer contributing to the server load issue.

## General Learnings
- High load on HPC home servers can be caused by frequent metadata operations due to many small file accesses.
- Consolidating data and loading it into RAM can help alleviate the load.
- Using temporary directories (`$TMPDIR`) for data processing can reduce the impact on home directories.
- Hierarchical data formats or archives can be used to manage large datasets more efficiently.

## Next Steps
- Continue monitoring the server load to ensure the issue is fully resolved.
- Encourage other users to follow similar practices to prevent future load issues.
---

### 2024061942002141_Handling%2023T%20Zarr%20Archiv%20mit%20kleinen%20Dateien.md
# Ticket 2024061942002141

 # Handling Large Zarr Archives on Ceph

## Keywords
- Ceph
- Zarr Format
- Large Datasets
- Google Cloud
- Zip Archive
- POSIX
- Parallel Downloads

## Problem
A user wants to work with a 23TB dataset in Zarr format, consisting of ~23 million files, currently stored in the Google Cloud. The user aims to store and process this dataset on the Ceph filesystem but is concerned about the potential resource strain due to the large number of files.

## Questions
1. Is Ceph optimized for handling Zarr format efficiently?
2. If not, is it feasible to download the Zarr archive to Ceph and then compress it into a Zip archive?

## HPC Admin Response
- The HPC Admin is not aware of any specific optimization between Ceph and Zarr.
- Ceph should be able to handle the Zarr format as it is POSIX-compliant.
- The distribution of files across directories is crucial for performance.
- Compressing the dataset into one or multiple archives is a good approach.
- The download itself should not be an issue for Ceph, but care should be taken to avoid too many parallel downloads.

## Solution
- Download the Zarr archive to Ceph, ensuring not to overload the system with too many parallel downloads.
- Compress the dataset into one or multiple Zip archives to reduce the strain on Ceph.

## General Learnings
- Ceph can handle large datasets in Zarr format due to its POSIX compliance.
- Proper file distribution across directories is important for performance.
- Compressing large datasets into archives can help manage resource usage.
- Avoiding too many parallel downloads is crucial to prevent system overload.

## Next Steps
- Monitor the download process to ensure it does not overload the system.
- Compress the dataset into Zip archives after downloading.
- Evaluate the performance and adjust the file distribution if necessary.
---

### 2022121642003272_how%20to%20access%20scratch.md
# Ticket 2022121642003272

 # HPC Support Ticket: Accessing Scratch Space for Training Neural Networks

## Keywords
- Scratch space
- Temporary storage
- Job-specific directory
- Automatic deletion
- Neural network training
- Python
- TinyGPU
- .tar file
- VAULT

## Problem
The user has a large .tar file containing about 2400 images (130 GB) and wants to know the best approach to handle these images for training a neural network in Python on TinyGPU. Specifically, the user asks if they should decompress the files from VAULT to scratch before every training session and where to save the data so that it gets deleted automatically at the end of the batch job.

## Solution
The HPC Admin recommends decompressing the .tar file within a job to the `$TMPDIR` directory. `$TMPDIR` points to a job-specific directory on the node-local SSD, which is automatically deleted at the end of the job.

## General Learnings
- **Temporary Storage**: Use `$TMPDIR` for temporary storage during jobs.
- **Automatic Cleanup**: Data stored in `$TMPDIR` is automatically deleted at the end of the job.
- **Efficient Data Handling**: For large datasets, decompress and process data within the job's temporary directory to optimize performance and storage usage.

## Related Topics
- Job management
- Data management
- Python scripts
- Neural network training
- TinyGPU

## Ticket Reference
- Subject: how to access scratch
- Date: 16.12.2022

---

This report provides guidance on handling large datasets for neural network training and the use of temporary storage in HPC environments.
---

### 2023112342004534_Slow%20behavior%20on%20front%20node%20of%20fritz%20-%20b148dc11%20_%20iwtm024h.md
# Ticket 2023112342004534

 ```markdown
# Slow Behavior on Front Node of Fritz

## Keywords
- Slow behavior
- Front node
- File access
- Compilation time
- High load
- Shared filesystem
- Harmful file access patterns

## Problem Description
- **User Observation**: Slow behavior on the front node of Fritz, specifically slow compilation times for code with minor changes.
- **Timeframe**: Thursday, 23rd of November at around 3:30 pm.
- **Suspected Cause**: High load on the file server (atuin) where `$WORK` is located.

## Diagnostic Steps
- **HPC Admin**: Requested specific details about where the slowness was experienced and which filesystem was affected.
- **User Response**: Confirmed that navigating through folders was not the problem, but compilation times were significantly increased.

## Root Cause
- **High Load on File Server**: The file server atuin showed a high load during the specified timeframe, likely due to harmful file access patterns from users or jobs.

## Solution
- **Clarification**: The HPC Admin clarified that the slow behavior was likely due to the high load on the file server, which affected file access and compilation times.

## General Learnings
- **Shared Filesystem Issues**: High load on shared filesystems can cause slow behavior, including increased compilation times.
- **Harmful File Access Patterns**: Users should be aware of harmful file access patterns that can contribute to high load on shared filesystems.
- **Monitoring and Diagnosis**: Regular monitoring of file server load and diagnosing harmful access patterns can help mitigate such issues.

## Next Steps
- **Monitoring**: Continue monitoring the file server load to identify and address harmful file access patterns.
- **User Education**: Educate users on best practices for file access to minimize the impact on shared filesystems.
```
---

### 2024091142001133_Anfrage%20wg.%20Databricks.md
# Ticket 2024091142001133

 # HPC-Support Ticket Conversation Analysis

## Keywords
- Data processing
- Temporary directory ($TMPDIR)
- Stata
- Azure Databricks
- Performance optimization
- Data storage

## Summary
The user experienced slow data processing times in the HPC environment, particularly with large datasets (20-50 GB). They inquired about integrating Microsoft Azure Databricks due to its faster performance. The HPC support team provided guidance on optimizing data handling using $TMPDIR and explained the limitations of integrating cloud services.

## Root Cause of the Problem
- Slow data processing due to large file sizes.
- Inefficient use of temporary storage.

## Solutions Provided
1. **Use of $TMPDIR**:
   - Ensure that the script loads modules correctly by including `-l` in the shebang line.
   - Copy input data to $TMPDIR at the beginning of the job and write output data to $TMPDIR before copying it back at the end of the job.
   - Example script adjustment:
     ```bash
     #!/bin/bash -l # Ensure that this line loads the modules
     # Load necessary modules
     module load stata
     # Set the STATATMP variable to the value of TMPDIR
     export STATATMP=$TMPDIR
     local list : dir "$pathv/rawdata/FR" files "*.csv"
     foreach f of local list {
         import delimited "$pathv/rawdata/FR/`f'", clear
         local outfile = subinstr("`f'",".csv","",.)
         tempfile `outfile'
         save "`outfile'", replace
     }
     ```

2. **Performance Optimization**:
   - Utilize $TMPDIR for data preparation and temporary storage to improve performance.
   - Consider using workspaces for better data handling solutions.

3. **Cloud Service Integration**:
   - Explained that integrating cloud services like Azure Databricks is challenging due to the lack of internet access on compute nodes.
   - No current support for cloud service integration.

## General Learnings
- Proper use of $TMPDIR can significantly improve data processing times.
- Cloud services integration is limited due to security and infrastructure constraints.
- Optimizing data handling within the HPC environment is crucial for performance.

## References
- [Data Staging Documentation](https://doc.nhr.fau.de/data/staging/)
- [Workspaces Documentation](https://doc.nhr.fau.de/data/workspaces/)

## Conclusion
The user was advised to optimize their data processing workflow by utilizing $TMPDIR effectively. The limitations of integrating cloud services were also explained, emphasizing the importance of adhering to the HPC environment's capabilities and constraints.
---

### 2020021242002203_Extreme%20Last%20auf%20den%20Fileservern%20durch%20ihre%20Jobs%20auf%20Woody.md
# Ticket 2020021242002203

 ```markdown
# HPC Support Ticket: Extreme Load on File Servers

## Keywords
- Extreme load
- File servers
- Job hold
- I/O operations
- Status files
- Local storage
- /dev/shm

## Problem Description
- User's jobs on the Woody cluster caused extreme load on the file servers, leading to significant operational disruptions.
- Jobs spent 1% of the time on calculations and 99% of the time writing status files repeatedly.

## Root Cause
- Excessive I/O operations due to frequent writing of status files.

## Solution
- Modify the code to reduce the frequency of writing status files.
- Use local storage or /dev/shm for temporary files and copy them back to the final location at the end of the job.

## Actions Taken
- Jobs were placed on hold to prevent further disruptions.
- User was advised to modify the code to reduce I/O operations.
- User implemented changes and tested with a single process to verify the fix.

## Outcome
- After modifications, jobs utilized at least 1 CPU out of 4 and were unnoticeable in terms of I/O operations.

## Lessons Learned
- Frequent I/O operations can cause significant load on file servers.
- Use local storage or /dev/shm for temporary files to reduce load on shared file systems.
- Test changes with a single process to verify the effectiveness of modifications.
```
---

### 2024121142000299_Fritz%20lustre%20extremely%20slow.md
# Ticket 2024121142000299

 # HPC Support Ticket: Lustre File System Slowdown

## Keywords
- Lustre file system
- Slowdown
- Hanging processes
- Writing stage
- System-wide issue

## Summary
A user reported a significant slowdown of the Lustre file system on the Fritz cluster, causing codes to hang during the writing stage and even simple file removal commands to hang. The issue started in the afternoon and affected the user's ability to perform basic file operations.

## Root Cause
- The root cause of the problem was not explicitly identified in the provided conversation snippet.

## Troubleshooting Steps
- The user inquired whether the issue was system-wide or specific to their account.
- HPC Admins and 2nd Level Support team should investigate if other users are experiencing similar issues.
- Check the Lustre file system logs for any errors or performance bottlenecks.
- Monitor system resources and network traffic to identify any unusual patterns.

## Solution
- No solution was provided in the conversation snippet.
- If the issue is system-wide, HPC Admins should take appropriate actions to resolve the performance bottleneck.
- If the issue is user-specific, further investigation into the user's environment and workload is required.

## Notes
- This issue highlights the importance of monitoring the Lustre file system performance and being prepared to handle sudden slowdowns.
- Regular maintenance and performance tuning of the Lustre file system can help prevent such issues.

## Follow-up Actions
- HPC Admins should update the user on the status of the investigation and any actions taken to resolve the issue.
- Document any findings and solutions for future reference to help resolve similar issues more efficiently.
---

### 2024121142001511_%5Baction%20requiered%5D%20very%20high%20file%20cont%20on%20atuin%20%5Bb212dc10%5D.md
# Ticket 2024121142001511

 # HPC Support Ticket Analysis: High File Count on Atuin

## Keywords
- High file count
- Metadata operations
- Data restructuring
- Tarballs
- CPU-only nodes
- Data transfer optimization
- Multi-node training

## Problem
- User has a dataset with close to 63 million files on Atuin ($WORK), causing high load and metadata operations.
- User is restructuring data but needs guidance on optimizing workflow and resource usage.

## Cause
- Large number of small files leading to high metadata operations and filesystem load.
- Inefficient data transfer and node utilization.

## Solution
1. **Data Restructuring**:
   - Convert small files into archives (e.g., tar, zip, hdf5) to reduce file count and metadata operations.
   - User created tarballs for scenes, reducing file count from 63 million to ~2500.

2. **CPU-only Nodes**:
   - User can access memoryhog for batch processing or request a tier3 account for access to woody.

3. **Data Transfer Optimization**:
   - Use `parallel` with `-j` option to control the number of tasks.
   - Prioritize important data and copy less important data in the background.
   - Consider using workspaces for better network connection.

4. **Multi-node Training**:
   - User's group is not currently allowed to use the multimode queue.
   - Access can be granted once data handling is improved.

## General Lessons
- High file counts can cause significant filesystem load and impact performance.
- Archiving small files into larger containers can mitigate these issues.
- Efficient data transfer strategies can improve job startup times.
- Proper resource allocation (e.g., using CPU-only nodes for non-GPU tasks) can prevent unnecessary resource blocking.
- Multi-node training access may be restricted based on data management practices.

## Follow-up
- Monitor user's data restructuring progress and provide further assistance if needed.
- Re-evaluate user's access to multi-node training once data handling improvements are implemented.
---

### 2024080142002386_ASCII%20files%20%40%20%24WORK.md
# Ticket 2024080142002386

 # HPC-Support Ticket Conversation: ASCII Files @ $WORK

## Keywords
- Lustre outages
- $FASTTMP
- $WORK
- VASP calculations
- ClusterCockPit
- Fortran I/O
- Binärdatei
- SapphireRapids nodes

## Summary
- **User Concern**: The user is concerned about potential issues with writing approximately 1200 ASCII files (each a few kB) to the $WORK directory during VASP calculations, given past Lustre outages on $FASTTMP.
- **Context**: The user mentions a previous notification regarding Lustre outages on $FASTTMP and wants to ensure that similar issues won't occur on $WORK.
- **Monitoring**: The user has checked ClusterCockPit but found no indications of problems.
- **Alternative Solution**: The user is considering using Fortran I/O to write a single binary file instead of multiple ASCII files.

## Root Cause
- The user is concerned about potential performance issues or outages similar to those experienced on $FASTTMP, affecting their VASP calculations on $WORK.

## Solution
- The user is considering an alternative approach using Fortran I/O to write a single binary file instead of multiple ASCII files to mitigate potential issues.

## General Learning
- **Monitoring Tools**: Use ClusterCockPit to monitor system performance and identify potential issues.
- **File I/O Strategies**: Consider using binary files for I/O operations to reduce the number of files and potentially improve performance and stability.
- **Communication**: Users should communicate with HPC Admins or the 2nd Level Support team for guidance on best practices and potential issues related to file I/O and system performance.

## Next Steps
- HPC Admins or the 2nd Level Support team should review the user's job (e.g., job-id ch3-7x8x9-bh6.o1439146) and provide guidance on the best approach for file I/O during VASP calculations.
- If necessary, the team should investigate any potential performance issues or outages related to the $WORK directory and provide recommendations to the user.
---

### 2024080842001463_long%20staging%20time%20%5Bv105cb12%5D.md
# Ticket 2024080842001463

 # HPC Support Ticket: Long Staging Time

## Keywords
- Long staging time
- IO performance
- Data transfer
- Fast storage
- Workspace allocation
- Batch script modification

## Problem
- User's jobs on Alex are experiencing long staging times due to slow data transfer from `atuin/$WORK`.

## Root Cause
- Slow IO performance when loading data from the current storage location.

## Solution
- **Fast Storage Allocation**: Use the fast storage available for Alex to speed up data transfer.
- **Workspace Setup**: Obtain a workspace on `/anvme`.
- **Data Transfer**: Copy input tar files to the new location.
- **Script Modification**: Update the path in the batch script to reflect the new storage location.

## Documentation
- Instructions for obtaining a workspace can be found at: [FAU Workspaces Documentation](https://doc.nhr.fau.de/data/workspaces)

## General Learning
- Improving IO performance can significantly reduce staging times.
- Utilize available fast storage options to optimize data transfer.
- Regularly update batch scripts to reflect changes in storage locations.

## Actions Taken
- The ticket was closed after providing the user with instructions on how to utilize the fast storage.

## Roles Involved
- **HPC Admins**: Provided the solution and documentation link.
- **2nd Level Support Team**: Not directly involved in this ticket.

## Additional Notes
- Ensure users are aware of available resources to optimize their workflows.
- Documentation and clear instructions are crucial for user self-service.
---

### 2019071842002026_Irgendwas%20l%C3%83%C2%A4uft%20nicht.md
# Ticket 2019071842002026

 ```markdown
# HPC-Support Ticket: Irgendwas läuft nicht

## Keywords
- High load average
- Java jobs
- I/O bottleneck
- Temporary directories
- $SCRATCH
- $TMPDIR

## Problem Description
- User reported high load average (around 20) on a Meggie node despite low CPU usage.
- Java jobs were running slowly, taking much longer than expected.
- Suspected I/O bottleneck due to many jobs reading/writing in the same directory.

## Diagnostic Steps
- User provided `top` output showing high load average but low CPU usage.
- User tested running a job in a different directory, which completed in the expected time.
- User suspected I/O bottleneck due to many jobs accessing the same directory.

## Root Cause
- I/O bottleneck caused by many jobs (354 jobs, ~7000 threads) reading/writing in the same directory on `/home/woody`.
- The directory contained a large number of files (around 100k), causing delays in file access.

## Solution
- User switched to using `$SCRATCH` for temporary directories, which significantly improved job performance.
- HPC Admin confirmed the availability of `$TMPDIR` on Meggie nodes, which points to `/tmp` and is located in RAM.
- User requested and received higher job priority to meet a deadline.

## Lessons Learned
- High load average with low CPU usage can indicate an I/O bottleneck.
- Using local temporary directories (`$SCRATCH`, `$TMPDIR`) can alleviate I/O bottlenecks.
- The `$TMPDIR` variable is available on Meggie nodes and points to `/tmp`, which is located in RAM.
- Job priority can be adjusted to meet urgent deadlines.
```
---

### 2025031242001373_Efficient%20use%20of%20%24TMPDIR%20%5Biwnt127h%5D.md
# Ticket 2025031242001373

 # Efficient Use of $TMPDIR

## Keywords
- $TMPDIR
- Data staging
- Compressed archive
- Node-local storage
- Unpack/uncompress

## Problem
The user was copying a compressed archive to $TMPDIR and then unpacking/uncompressing it, which is inefficient.

## Root Cause
Inefficient use of $TMPDIR by copying the compressed archive before unpacking it.

## Solution
Directly unpack the archive to the node-local storage ($TMPDIR) without the intermediate copying step.

## General Learning
- Always aim to minimize data transfer steps when using $TMPDIR.
- Directly unpacking archives to node-local storage can improve efficiency.

## Example
Instead of:
```bash
cp archive.tar.gz $TMPDIR
tar -xzf $TMPDIR/archive.tar.gz -C $TMPDIR
```
Use:
```bash
tar -xzf archive.tar.gz -C $TMPDIR
```

This approach reduces unnecessary data transfer and improves job efficiency.
---

### 2024073042004929_Anvme%20and%20preprocessing%20data%20on%20Fritz_Woody%20%5Bb105dc10%5D.md
# Ticket 2024073042004929

 # HPC-Support Ticket: Anvme and Preprocessing Data on Fritz/Woody

## Keywords
- Preprocessing
- Audio extraction
- CPU cluster
- GPU cluster
- Data transfer
- rsync
- Woody
- Fritz
- Alex
- anvme
- atuin

## Summary
The user needs to preprocess a large dataset of video files to extract audio and then train a network using the extracted audio. The preprocessing step requires a CPU cluster, while the training step requires a GPU cluster. The user estimates the resulting dataset will occupy 20-25 TB of disk space.

## Problem
- The user needs to combine preprocessing and training steps effectively.
- The user is unsure whether to extract audios on Woody and then put them on anvme.

## Solution
- Preprocess the data on Woody and store it on atuin.
- Once preprocessing is done, copy the data to anvme.
- To speed up the data transfer, use several rsync processes in parallel.
- The user can copy the entire folder directly without the compression step.

## Additional Notes
- The user initially estimated 200 CPU hours for preprocessing, but it took 400 CPU hours.
- The resulting audio dataset occupies 6.6 TB.
- The user was advised to aggregate more audio extraction into a single job to optimize resource usage.

## Root Cause
- The user needed guidance on how to effectively combine preprocessing and training steps and how to handle large data transfers.

## Resolution
- The HPC Admin provided a workflow for preprocessing the data on Woody, storing it on atuin, and then copying it to anvme.
- The user was advised to use parallel rsync processes to speed up the data transfer.

## Follow-up
- The user should monitor the data transfer process and ensure that the dataset is successfully copied to anvme for the training step.

## Documentation
- This ticket can serve as a reference for handling large data preprocessing and transfer tasks in the future.
- Users should be aware of the importance of aggregating tasks to optimize resource usage.
- Parallel data transfer methods like rsync can significantly speed up the process of moving large datasets.
---

### 2018032142000183_Kontakt%20Geographie.md
# Ticket 2018032142000183

 # HPC Support Ticket Conversation Analysis

## Subject: Kontakt Geographie

### Keywords:
- Job submission
- Efficiency
- Batch system overhead
- Parallel processing
- Temporary files
- RAM usage
- Code optimization
- NetCDF library issue
- sed command optimization

### General Learnings:
- Importance of efficient job submission to avoid system overhead.
- Use of parallel processing to handle multiple jobs within a single job submission.
- Optimization of temporary file handling to reduce I/O operations.
- Importance of code optimization to reduce job runtime.
- Handling library issues in job scripts.
- Optimizing sed commands to reduce processing time.

### Root Cause of the Problem:
- User submitted a large number of short-duration jobs, causing significant overhead in the batch system.
- Inefficient handling of temporary files and RAM usage.
- Library issues with NetCDF in job scripts.
- Inefficient use of sed commands leading to high network load.

### Solution:
- Consolidate multiple short-duration jobs into a single job using parallel processing.
- Optimize the handling of temporary files by using RAM-based filesystems like /scratch.
- Address library issues by ensuring compatibility and proper configuration.
- Optimize sed commands to reduce processing time and network load.

### Detailed Conversation Analysis:

#### Initial Issue:
- User submitted over 1000 jobs with short durations, causing system overhead.
- Jobs were mostly under 1 minute, with significant time spent on I/O operations.

#### HPC Admin Response:
- Suggested consolidating jobs into fewer, longer-running jobs to reduce overhead.
- Provided links and examples for using GNU Parallel to package multiple jobs into a single PBS job.
- Recommended using /scratch for temporary files to reduce I/O operations.

#### User Implementation:
- User implemented the suggestions and successfully ran a batch of 100 jobs with parallel processing.
- Encountered issues with NetCDF library when submitting jobs with 'qsub'.

#### Further Optimization:
- HPC Admin suggested optimizing sed commands to reduce processing time and network load.
- Recommended using /dev/shm for temporary files to further reduce I/O operations.

#### Additional Issue:
- User accidentally deleted important script files and requested recovery.

#### HPC Admin Response:
- Addressed the issue of recovering deleted files.
- Continued to provide support for optimizing job submissions and code efficiency.

### Conclusion:
- The conversation highlights the importance of efficient job submission and code optimization in HPC environments.
- Provides practical solutions for handling large numbers of short-duration jobs and optimizing temporary file usage.
- Emphasizes the need for addressing library issues and optimizing command usage to reduce processing time and network load.
---

### 2022112442006327_Viele%20Dateien%20auf%20atuin.md
# Ticket 2022112442006327

 ```markdown
# HPC Support Ticket: Handling Large Number of Files on /home/atuin

## Keywords
- OpenPose JSONs
- Large number of files
- /home/atuin
- $TMPDIR
- Node SSD

## Problem
User needs to write approximately 2.5 million files on `/home/atuin` for a workflow that involves unpacking OpenPose JSONs and images.

## Root Cause
The user's code expects unpacked OpenPose JSONs and images, which would result in a large number of files being written to `/home/atuin`.

## Solution
HPC Admin suggests using a workflow where data is unpacked to `$TMPDIR` at job start. This approach reduces the load on `/home/atuin` by storing the numerous small files on the node's SSD.

## General Learning
- **File Management**: Avoid storing a large number of small files on shared storage like `/home/atuin`.
- **Temporary Storage**: Utilize `$TMPDIR` for temporary files during job execution to leverage node-local SSDs.
- **Workflow Optimization**: Optimize workflows to minimize the load on shared storage systems.
```
---

### 2024100942000654_HDD%20f%C3%BCr%20Fritz%20-%20Megware-Service.md
# Ticket 2024100942000654

 # HPC Support Ticket: HDD für Fritz - Megware-Service

## Keywords
- HDD replacement
- Lustre filesystem
- Hardware failure
- Ersatzteilvorrat
- UPS Abholung
- Western Digital

## Problem Description
- **Root Cause**: Faulty HDD in Lustre filesystem.
  - **Details**: `ost05-disk30 FAULTED 25 0 0 too many errors`
  - **Correction**: Should be `ost04-disk30`.

## Solution
1. **Request for New HDD**:
   - **Model**: HGST HUH721212AL5200
   - **Firmware**: A925

2. **Temporary Replacement**:
   - Replace the faulty HDD with a spare from the Ersatzteilvorrat (1315001880/ HGST SE MM CRU HE12 Drive w/Carrier 12TB SAS 512E ISE HDD).

3. **Defective HDD Handling**:
   - Pack the defective HDD and arrange for UPS pickup.
   - Send the defective HDD to Megware for replacement through the manufacturer (Western Digital).

4. **Replacement Process**:
   - Western Digital initiated the replacement process.
   - Note: Western Digital's portal changes may cause delays.

5. **Final Replacement**:
   - Once the replacement HDD is received from Western Digital, it will be delivered to the HPC site.

## General Learnings
- **Spare Parts Management**: Importance of having a spare parts inventory for quick replacements.
- **Communication**: Clear communication between HPC Admins and the support team is crucial for timely resolution.
- **Vendor Processes**: Awareness of vendor processes and potential delays due to portal changes or other factors.

## Roles Involved
- **HPC Admins**: Managed the initial request and temporary replacement.
- **2nd Level Support Team**: Coordinated with Megware for the replacement process.
- **Megware Service**: Handled the defective HDD and arranged for the replacement through Western Digital.

## Conclusion
The faulty HDD was successfully replaced using a spare from the inventory, and the defective HDD was sent for replacement through the manufacturer. The process involved coordination between HPC Admins, the 2nd Level Support Team, and Megware Service.
---

### 2024022342003103_Job%20auf%20Alex%20nutzt%20GPU%20nicht%3B%20Unterst%C3%83%C2%BCtzung%20bei%20Data%20Handling%20%5Bb1.md
# Ticket 2024022342003103

 # HPC Support Ticket: Job auf Alex nutzt GPU nicht; Unterstützung bei Data Handling

## Keywords
- Job Management
- Data Handling
- Ceph Storage
- Tar Archive
- Slurm Script
- Job Cancellation

## Problem
- User's job (JobID 1158187) was taking 18 hours to copy data from `/home/atuin` to `$TMPDIR` using `cp`.
- `cp` is not efficient for copying a large number of individual files.

## Root Cause
- Inefficient data copying method using `cp`.

## Solution
1. **Allocate Workspace on Ceph Storage**:
   - Follow the guide at [Ceph Storage Workspaces](https://doc.nhr.fau.de/data/workspaces/).
   - Log in to the Alex Frontnode.
   - Allocate workspace: `ws_allocate imagenet 90` (creates a workspace named "imagenet" for 90 days).
   - Access the workspace using a variable: `STORAGE_DIR="$(ws_find imagenet)"`.

2. **Archive Data with Tar**:
   - Archive the required data using `tar` and store it in the Ceph workspace at `$STORAGE_DIR`.

3. **Extract Archive at Job Beginning**:
   - At the start of the job, extract the archive directly from the Ceph workspace to `$TMPDIR` using `tar xf`.

## Additional Tips
- Using `tar` to archive and extract data significantly speeds up the data transfer process.
- The step over Ceph is not mandatory; archiving data with `tar` and extracting it directly to `$TMPDIR` is sufficient.
- Example commands:
  - Archive data: `tar cf archive.tar file1 file2 file3`
  - Extract archive: `tar xf "$WORK/archive.tar" -C "$TMPDIR"` or `unzip -q archiv.zip -d $TMPDIR`

## Actions Taken
- The job was canceled as requested by the user.
- The user was advised on efficient data handling methods.

## Closure
- The ticket was closed due to no further response from the user.

---

This documentation aims to assist HPC support employees in resolving similar data handling issues in the future.
---

### 2024040842003281_Request%20for%20Additional%20Space%20for%20VideoLLM%20Project.md
# Ticket 2024040842003281

 # HPC Support Ticket: Request for Additional Space for Video Project

## Keywords
- Storage request
- Large dataset
- Video data
- File system performance
- Workflow optimization
- CEPH storage

## Summary
A user requested additional storage space for a video-based project, specifically for the Panda-70M dataset, which requires around 36TB of space. The HPC admin identified potential issues with storing a large number of small files on the shared file systems and provided recommendations for optimizing the workflow.

## Root Cause
- The user's initial plan to store multiple files per sample would lead to hundreds of millions of small files, causing performance issues on the shared file systems.

## Solution
- **Workflow Optimization**: Store samples in chunked archives and extract them to node-local SSDs when the job starts.
  - Refer to [Dataset Documentation](https://doc.nhr.fau.de/data/datasets/) for more information on the issue.
  - Refer to [Staging Documentation](https://doc.nhr.fau.de/data/staging/) for the solution.
- **Storage Recommendation**: Use CEPH storage for temporarily storing larger amounts of data.
  - Refer to [CEPH Storage Documentation](https://doc.nhr.fau.de/data/workspaces/).
- **Feedback**: The user was asked to provide feedback on their experience with the recommended solutions.

## General Learnings
- Storing a large number of small files can lead to performance issues on shared file systems.
- Optimizing workflows to reduce the number of files, such as using archives, can mitigate these issues.
- CEPH storage is recommended for temporarily storing large amounts of data.
- It's important to consider the impact of data storage methods on the overall performance of the HPC system.

## Ticket Status
- The ticket was closed after the user acknowledged the information and agreed to optimize their workflow.
---

### 2021121942000155_Action%20required%20%28iwi5035h%29%3A%20Last%20auf%20HPC-Home-Servern%20des%20RRZE%20_%20Load%20on%2.md
# Ticket 2021121942000155

 # HPC Support Ticket: Excessive Load on HPC Home Servers

## Keywords
- Excessive load
- File server
- Metadata operations
- GPU utilization
- Job optimization

## Summary
The user's job was causing excessive load on the HPC home servers due to frequent file operations. The job involved many small file accesses, particularly with data distributed over many files, leading to high metadata operations.

## Root Cause
- The job was performing a large number of file opens, reads, and other metadata operations on a small set of PNG files.
- The job was not efficiently utilizing GPU resources, allocating memory without performing significant computations.

## Steps Taken
1. **Initial Notification**: The user was informed about the excessive load caused by their job and advised to optimize file accesses.
2. **First Attempt at Optimization**: The user attempted to fix the code but the issue persisted.
3. **Second Attempt at Optimization**: The user made further changes to load all files at the beginning, but the problem remained.
4. **GPU Utilization Issue**: The HPC admin noticed that the jobs were not effectively using the GPUs, despite allocating GPU memory.

## Solution
- The user was advised to read all required files only once at the beginning and keep their contents in in-memory data structures.
- The user was informed about the inefficient GPU utilization and advised to ensure that the jobs perform significant computations on the GPUs.

## Lessons Learned
- Frequent file operations, especially on small files, can cause excessive load on file servers.
- Efficient use of in-memory data structures can significantly reduce the load on file servers and improve job performance.
- It is important to ensure that jobs effectively utilize GPU resources by performing significant computations.

## Follow-up
- The user should confirm the implementation of the suggested changes and monitor the job's performance and resource utilization.
- The HPC admin should continue to monitor the job and provide further assistance if needed.

## Related Tickets
- [Linked Ticket]: Additional information on job performance and resource utilization.

## Conclusion
Optimizing file accesses and ensuring efficient use of computational resources are crucial for maintaining the performance and stability of HPC systems. Users should be proactive in addressing any issues related to excessive load and inefficient resource utilization.
---

### 2022050342002588_Tier3-Access-Fritz%20%22Severin%20Kuffer%22%20_%20mpp3003h.md
# Ticket 2022050342002588

 ```markdown
# HPC Support Ticket Conversation: Tier3-Access-Fritz "Severin Kuffer" / mpp3003h

## Issue
- User's jobs on Emmy were causing excessive IO, affecting other HPC users.
- PH.x executable was generating significant IO, leading to performance issues.

## Root Cause
- The PH.x executable from the Quantum Espresso suite was generating large binary files and performing frequent read/write operations.
- The user's jobs were not optimized for IO, leading to excessive disk usage.

## Solution
- The user was advised to reduce IO by optimizing the PH.x executable and avoiding unnecessary read/write operations.
- The user was also advised to use the `reduce_io` keyword to minimize IO.
- The user was granted access to Fritz for testing, but the hardware limitations (SSD lifespan) prevented long-term use.
- The user was advised to use Woody-NG nodes with Ice-Lake CPUs and to pack files using `tar` to reduce IO during job initialization and finalization.

## Additional Notes
- The user successfully ran PH.x calculations in RAM on Woody-NG nodes without issues.
- The user was advised to monitor job performance and IO usage to ensure compliance with HPC guidelines.

## Conclusion
- The user's jobs were optimized to reduce IO, and the user was advised on best practices for running high-IO jobs on the HPC system.
- The user was granted access to Woody-NG nodes for further testing and optimization.
```
---

### 2023032042003832_AssocMaxJobsLimit%20in%20Gruppe%20-%20iwbn002h.md
# Ticket 2023032042003832

 # HPC Support Ticket: AssocMaxJobsLimit in Gruppe - iwbn002h

## Problem
- User reported that their jobs were not being allocated nodes and only one job was running at a time.
- The user noticed the `AssocMaxJobsLimit` reason in `squeue`.
- The user suspected high traffic in the group but was unsure about the cause.

## Root Cause
- The user's jobs were generating high I/O load on the fileserver due to frequent R script executions and logging.
- The jobs were writing and deleting temporary files continuously, causing extreme data rates and load on the fileserver.

## Solution
1. **Reduce Logging and I/O Operations**:
   - The user was advised to reduce logging outputs and avoid frequent file operations.
   - The user identified and removed an extensive debug print in an R script that was causing high I/O load.

2. **Use RAMdisk for Temporary Files**:
   - The user was advised to use the RAMdisk (`/dev/shm`) for temporary files to reduce the load on the fileserver.
   - This change significantly reduced the I/O load and improved job performance.

3. **Switch to rpy2 for Longer-Running R Processes**:
   - The user was advised to use `rpy2` to call R from Python, reducing the overhead of starting and initializing R multiple times.
   - This change resulted in fewer R processes and reduced the load on the fileserver.

## Monitoring and Verification
- The user was instructed to use `htop` on the compute nodes to monitor their processes.
- The HPC Admins verified the reduction in I/O operations and the number of R processes using `nfs4_total` in ClusterCockpit.

## Additional Resources
- **rpy2 Documentation**:
  - [Appsilon: Use R and Python Together](https://appsilon.com/use-r-and-python-together/)
  - [AskPython: Examples of R in Python](https://www.askpython.com/python/examples/r-in-python)
  - [RStudio: Calling R from Python with rpy2](https://rviews.rstudio.com/2022/05/25/calling-r-from-python-with-rpy2/)

- **Rserve Documentation**:
  - [Rserve](https://rforge.net/Rserve/)
  - [RPlumber](https://www.rplumber.io/)
  - [pyRserve](https://github.com/ralhei/pyRserve)
  - [pyRserve Documentation](https://pyrserve.readthedocs.io/en/latest/intro.html#what-pyrserve-does)

## Conclusion
The user's jobs were successfully optimized to reduce I/O load and improve performance. The use of `rpy2` and RAMdisk for temporary files significantly reduced the load on the fileserver and allowed multiple jobs to run concurrently.
---

### 2023081242000109_Slow%20respons%20on%20Fritz%20-%20a102cb10.md
# Ticket 2023081242000109

 # HPC Support Ticket: Slow Response on Fritz - a102cb10

## Keywords
- Slow response time
- Atuin file system
- Increased load
- UID/GID resolution
- nscd configuration
- Login issues
- VPN

## Problem Description
- User experienced slow response times on the Atuin file system.
- Initial issue reported on Fritz HPC system.

## Root Cause
- Increased load on the Atuin file system due to specific projects and jobs.
- Slow UID/GID resolution.

## Diagnostic Steps
- Monitoring showed normal response times for individual hard disks.
- Identified specific directories with a high number of files causing increased load.
- Checked login attempts and requested detailed error logs using `ssh -v`.

## Solution
- Applied nscd configuration from Alex login nodes to Fritz login nodes to improve UID/GID resolution.
- User reported temporary login issues, which were resolved by using VPN.

## Lessons Learned
- High file counts in specific directories can significantly impact file system performance.
- Proper configuration of nscd can improve UID/GID resolution times.
- Temporary network issues can sometimes be resolved by using VPN.

## Follow-up Actions
- Continue monitoring the Atuin file system for increased load.
- Regularly review and optimize nscd configurations.
- Provide users with guidance on managing large numbers of files in directories.
---

### 2024021642002949_Massive%20File%20Operations%20on%20_home_atuin%20%5Bb198dc11%5D.md
# Ticket 2024021642002949

 # HPC Support Ticket: Massive File Operations on /home/atuin

## Keywords
- Massive file operations
- $TMPDIR
- Node-local job-specific directory
- Ceph storage
- Performance optimization
- Archive extraction

## Problem
- User's jobs were causing a massive load on the file server by opening approximately 70,000 files per minute on each of the seven nodes.
- This affected the performance of both the user's jobs and other users' jobs.

## Root Cause
- The user's script was accessing a large number of small files directly from the home directory, leading to excessive I/O operations.

## Solutions Proposed
1. **Copy data to $TMPDIR**:
   - Add a new parameter to the script containing $TMPDIR.
   - Use a copy/rsync command to transfer data from the project directory to $TMPDIR.
   - Modify the Python code to use the new $TMPDIR path instead of the original project directory path.

2. **Allocate workspace on Ceph storage**:
   - Refer to the documentation for allocating workspace on Ceph storage.

3. **Archive extraction**:
   - Create an archive of the needed files.
   - Extract the archive directly to $TMPDIR at the beginning of the job.
   - Example commands:
     ```bash
     tar cf archive.tar file1 file2 file3
     tar xf "$WORK/archive.tar" -C "$TMPDIR"
     ```

## Implementation Issues
- The user initially tried to copy data outside of a running job, which did not utilize $TMPDIR correctly.
- Copying a large number of small files before training started was a bottleneck, causing a significant loss of allocated GPU time.

## Final Solution
- The user implemented a solution where training samples are stored in the `/tmp` directory during runtime.
- The user was advised to use $TMPDIR instead of `/tmp` to avoid shared folder issues.
- The user was also advised to use archive extraction for better performance, as copying and extracting a single archive is faster than reading many small files individually.

## Conclusion
- The user's final implementation involved storing training samples in the `/tmp` directory during runtime, with plans to switch to $TMPDIR.
- The use of archive extraction was recommended for further performance improvements.

## References
- [Node-local job-specific directory ($TMPDIR)](https://doc.nhr.fau.de/data/filesystems/#node-local-job-specific-directory-tmpdir)
- [Ceph storage workspace allocation](https://doc.nhr.fau.de/data/workspaces/)
---

### 2024032742002926_High%20load%20on%20alex2.md
# Ticket 2024032742002926

 ```markdown
# High Load on Frontend Due to Parallel Downloads

## Keywords
- High load
- Frontend
- Parallel downloads
- Slurm job
- Reduce processes

## Problem Description
A user was performing parallel downloads on the frontend (alex2), causing a very high load. Other users were affected and complained about the issue.

## Root Cause
Parallel downloads on the frontend were consuming excessive resources, impacting the performance for other users.

## Solution
- **Immediate Action**: The user was asked to stop the parallel downloads.
- **Long-term Solution**: The user was advised to move the downloads to a Slurm job or reduce the number of processes.

## Lessons Learned
- Parallel downloads on the frontend can cause high load and affect other users.
- It is important to move resource-intensive tasks to Slurm jobs to avoid overloading the frontend.
- Communication with users about proper resource usage is crucial to maintain system performance.
```
---

### 2019011042001758_Lima%20cluster%3A%20Copy%20data.md
# Ticket 2019011042001758

 # HPC Support Ticket: Lima Cluster Data Copy

## Keywords
- Data Transfer
- rsync
- Compression
- Network Speed
- NAS
- HPC Cluster Shutdown

## Summary
A user needed to copy 20TB of data from the Lima cluster before its shutdown but was experiencing slow transfer speeds using `rsync`.

## Root Cause
- Slow network connection to the local NAS (~10 MB/sec).
- Potential issue with the user's network connection or NAS capabilities.

## Troubleshooting Steps
1. **HPC Admin** verified that the Lima cluster could deliver full gigabit speeds with `rsync`.
2. **User** observed that compressing files on the Lima frontend increased transfer speeds due to a 60% compression rate.

## Solution
- **HPC Admin** suggested using the built-in compression feature of `rsync` with the `-z` or `--compress` parameter.
- **User** decided to compress files directly on the Lima frontend to expedite the transfer process.

## General Learnings
- Network speed can significantly impact data transfer times.
- Compressing files before transfer can help increase transfer speeds, especially for text files.
- `rsync` has a built-in compression feature that can be utilized for faster transfers.
- During cluster shutdowns, some resources like job queues may already be unavailable.

## Action Items for Future Reference
- Verify network connection speeds when troubleshooting slow data transfers.
- Utilize compression tools or built-in features to speed up data transfers.
- Be aware of resource availability during cluster shutdown periods.
---

### 2024062642001861_Slow%20commands.md
# Ticket 2024062642001861

 ```markdown
# HPC Support Ticket: Slow Commands

## Keywords
- Slow commands (`ls`, `cd`, `top`, `vi`)
- High load on fileservers
- Intermittent problems
- Service degradation
- DDOS attack
- Daytime vs. nighttime performance

## Problem Description
- User reports slow performance of basic commands (`ls`, `cd`, `top`, `vi`) during daytime.
- Login message indicates service degradation and intermittent problems on Fritz frontends.
- Commands run normally at night.

## Root Cause
- High load on the fileservers causing delays in command execution.

## Solution
- HPC Admins are investigating the cause of the high load on the fileservers.
- Previous DDOS attack was addressed by locating and killing offending jobs.

## Lessons Learned
- High load on fileservers can significantly impact the performance of basic commands.
- Performance issues can be intermittent and vary between daytime and nighttime.
- Regular monitoring and quick response to high load situations are crucial for maintaining system performance.
```
---

### 2024072942001541_high%20IO%20on%20TinyGPU%20%5Biwso116h%5D.md
# Ticket 2024072942001541

 # HPC Support Ticket: High IO on TinyGPU

## Keywords
- High IO
- File Systems
- rsync
- Archives
- HDF5 format
- Tar archives
- TMPDIR

## Root Cause
- User's jobs on TinyGPU were causing high IO by copying ~200k files with rsync to the local disk.

## Impact
- The high IO was causing problems for the file systems and impacting all users.

## Solution
- **Archiving Data**: Pack data into archives or use a different file format to reduce the number of files.
  - **Tar Archives**: Directly unpack to `$TMPDIR` without copying and unpacking.
    ```bash
    tar -xvf file.tar $TMPDIR/data/
    ```
  - **HDF5 Format**: Convert data to HDF5 format for efficient handling.
- **Documentation**: Refer to the documentation for more information on handling datasets: [Documentation Link](https://doc.nhr.fau.de/data/datasets/)

## Additional Tips
- Copying a single file (or a small number of files) is generally much faster than transferring several thousand files.

## Ticket Status
- Closed with user promising improvement.

## Roles Involved
- **HPC Admins**: Provided guidance and solutions.
- **User**: Acknowledged the issue and agreed to implement the suggested improvements.

## General Learning
- High IO issues can be mitigated by reducing the number of files being transferred.
- Using archives or efficient file formats like HDF5 can significantly improve performance and reduce the load on file systems.
- Always refer to the documentation for best practices in handling datasets.
---

### 2023121542001998_IO-Zeiten%20auf%20Alex_Fritz.md
# Ticket 2023121542001998

 # HPC-Support Ticket: IO-Zeiten auf Alex/Fritz

## Keywords
- FileSystems
- Quota
- Transfer Rates
- Benchmarks
- IO Patterns
- $WORK
- $HOME
- $FASTTMP
- $HPCVAULT
- fio
- Blocksize
- Checkpoints
- MPI-I/O

## Problem Description
- User had questions about file systems, quota, and transfer rates.
- Initial benchmarks showed very low transfer rates.
- User needed to process large datasets and train models, requiring high IO performance.

## Root Cause
- Small block sizes in benchmarks led to low transfer rates.
- Inefficient IO patterns, such as many small files, caused bottlenecks.

## Solution
- Use `shownicerquota.pl` or `df -h $WORK` to check quota.
- Increase block size in benchmarks to simulate realistic scenarios.
- Avoid small files and use larger blocks for better performance.
- Use $FASTTMP for high-speed temporary storage.
- Consider MPI-I/O for parallel writing of large checkpoints.
- Be mindful of shared resources and avoid excessive load on file systems.

## General Learnings
- Understanding IO patterns is crucial for optimizing performance.
- Proper benchmarking requires realistic scenarios and parameters.
- Efficient use of file systems can prevent bottlenecks and improve job performance.
- Parallel IO operations can significantly enhance the handling of large datasets.
- Always consider the impact on shared resources and other users.
---

### 2024100442002401_Detailfragen%20zum%20Alex-Lustre.md
# Ticket 2024100442002401

 # HPC-Support Ticket Conversation Analysis

## Subject: Detailfragen zum Alex-Lustre

### Keywords:
- Lustre
- ZFS
- ldiskfs
- NVMe
- DirectIO
- Performance
- Case Study
- Xinnor
- AlmaLinux
- xiRAID

### Summary:
The user from the University of Tübingen inquired about the specifics of the Lustre filesystem setup used in the Alex-Cluster at FAU, as they are setting up a similar system. The main concern was the middleware filesystem used between xiraid-vdevs and Lustre, specifically whether it was ldiskfs or ZFS, and the compatibility and performance implications.

### Root Cause of the Problem:
The user needed to know the middleware filesystem used in the Alex-Cluster to make informed decisions for their own setup. They were concerned about the compatibility of Lustre 2.15.5 with ZFS 2.2 and the performance benefits of DirectIO.

### Solution:
- **Middleware Filesystem**: The Alex-Cluster uses AlmaLinux 8.10 with Lustre 2.15.5 and ldiskfs.
- **Performance Considerations**: ldiskfs was chosen over ZFS due to better performance, even with DirectIO. ZFS checksums and other features can lead to performance degradation.
- **Compatibility**: Lustre 2.15.5 is compatible with ZFS 2.1, not ZFS 2.2. The upcoming Lustre 2.16 also supports only ZFS 2.1.
- **Recommendations**: ZFS is not recommended for NVMe setups due to performance issues. ldiskfs is preferred.

### General Learnings:
- **Filesystem Choice**: ldiskfs is generally faster than ZFS for NVMe setups, even with DirectIO.
- **Compatibility Issues**: Ensure compatibility between Lustre versions and ZFS versions.
- **Performance Tuning**: Aligning stripe sizes and using separate volumes for metadata can improve performance.
- **Hardware Considerations**: Ensure sufficient PCIe lanes and cores for optimal NVMe performance.

### Additional Resources:
- **Case Study and Slides**: Provided by the HPC Engineer, detailing performance benchmarks and hardware specifications.
- **Benchmark Articles**: Comparisons between ZFS, mdraid, and xiRAID.

### Conclusion:
The user was advised to use ldiskfs for their NVMe setup due to its superior performance compared to ZFS. Detailed performance data and hardware specifications were provided to assist in their decision-making process.

---

This analysis provides a comprehensive overview of the conversation, highlighting key points and recommendations for future reference.
---

### 2017021642001776_Slow%20response%20in%20Woody.md
# Ticket 2017021642001776

 # Slow Response in Woody

## Keywords
- Slow response
- Woody
- Frontend node
- File system
- Usability

## Problem Description
- User experiencing slow response when accessing Woody through woody3.
- Issue primarily noticed when trying to access files.
- Suspected to be related to the file system rather than the frontend node.

## Root Cause
- The slow response is likely due to issues with the file system rather than the frontend node.

## Solution
- No specific solution provided in the conversation.
- Suggested to check if using a different frontend node improves the situation.

## General Learnings
- Slow response issues can be related to the file system.
- Users should try different frontend nodes to see if the issue persists.
- Further investigation by HPC Admins may be required to diagnose and resolve file system issues.

## Next Steps
- HPC Admins should investigate the file system performance.
- Users can try accessing Woody through different frontend nodes to see if the issue is node-specific.
---

### 2025022742003667_Please%20use%20tar%20to%20transfer%20your%20data%20to%20%24TMPDIR%20%5Bempk012h%5D.md
# Ticket 2025022742003667

 # HPC Support Ticket: Data Transfer Optimization

## Keywords
- Data Transfer
- TMPDIR
- tar
- Deep Learning
- Radar Data
- Node-local Storage
- HPC Cafe

## Problem
- User's jobs on TinyGPU take two hours to copy data to node-local storage.
- Data is processed during transfer, increasing size from 120GB to 1.2-2TB.
- Data changes with different models, making pre-compression infeasible.

## Root Cause
- Inefficient data transfer method leading to long copy times.
- Dependency on the filesystem for data processing.

## Solution
- **Recommendation**: Use `tar` to pack data into an archive and extract directly to node-local storage.
  ```bash
  tar -cf /path-to/archive.tar /data-to-pack
  cd $TMPDIR
  tar -xf /path-to/archive.tar
  ```
- **Alternative**: Copy raw data from $WORK to $TMPDIR and process it locally to avoid filesystem dependency.
  ```bash
  cp -r $WORK/Datasets/raw_radar_data/DummyFolder_Slices $TMPDIR/Dataset
  ```

## General Learnings
- Using `tar` for data transfer can significantly reduce copy times.
- Processing data locally on $TMPDIR can improve job performance by reducing dependency on the filesystem.
- HPC Cafe events provide useful insights and measurements on efficient data handling.

## References
- [HPC Cafe: Efficient Packing and Handling of Large Data Sets](https://hpc.fau.de/2025/02/04/monthly-hpc-cafe-efficient-packing-and-handling-of-large-data-sets-hybrid-event/)
---

### 2024082742000393_high%20load%20on%20atuin%20%5Bv103fe15%5D.md
# Ticket 2024082742000393

 # HPC Support Ticket: High Load on Atuin

## Keywords
- High write load
- Atuin
- NVMe storage
- Temporal output
- Job duration

## Summary
- **Issue**: User's jobs on Alex are causing a high write load on Atuin for almost the entire job duration.
- **Root Cause**: The output being written is potentially temporal with low value.
- **Solution**: Use fast NVMe storage for temporal output.

## Details
- **HPC Admin**: Noted high write load on Atuin due to user's jobs.
- **HPC Admin**: Suggested using NVMe storage for temporal output if the data is not valuable beyond the study.
- **Documentation**: [NVMe Storage Documentation](https://doc.nhr.fau.de/data/workspaces)

## Actions Taken
- **HPC Admin**: Sent multiple notifications to the user.
- **HPC Admin**: Planned to escalate the ticket if no response is received.

## Lessons Learned
- High write loads on storage systems can be mitigated by using appropriate storage solutions for temporal data.
- Regular monitoring and user communication are essential to maintain system performance.

## Next Steps
- Ensure users are aware of the appropriate storage solutions for different types of data.
- Continue monitoring and addressing high load issues promptly.
---

