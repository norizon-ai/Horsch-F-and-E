# Topic 16: nfs_acl_issues_network_server

Number of tickets: 84

## Tickets in this topic:

### 2023112242003528_tinygpu%20nodes%20langsam.md
# Ticket 2023112242003528

 ```markdown
# HPC Support Ticket: GPU Nodes Issue

## Keywords
- GPU nodes
- Interactive job
- Login prompt
- NFS mount
- Certificate expiration

## Problem Description
- **User Report:** The GPU nodes (specifically tg06a and tg06b) are experiencing issues. When attempting an interactive job on tg06b, the user does not receive a login prompt after logging in.

## Root Cause
- **HPC Admin Response:** The issue was related to an expired certificate affecting the NFS mount for the home/vault directory.

## Solution
- **HPC Admin Action:** The NFS mount issue was resolved, and the system should now function as expected.

## General Learnings
- **Certificate Management:** Ensure that certificates for NFS mounts and other critical services are regularly monitored and renewed to prevent expiration-related issues.
- **Troubleshooting Steps:** When encountering login issues on GPU nodes, check the status of NFS mounts and related certificates.

## Next Steps
- **Monitoring:** Regularly monitor the status of certificates and NFS mounts to prevent similar issues in the future.
- **Documentation:** Update internal documentation to include troubleshooting steps for certificate-related issues.
```
---

### 2020122842000711_Login-Node%20woody3%3A%20Skripte%20h%C3%83%C2%A4ngen.md
# Ticket 2020122842000711

 ```markdown
# HPC-Support Ticket: Login-Node woody3: Skripte hängen

## Keywords
- Login-Node
- Woody3
- NFS-Client
- Reboot
- Denial-of-Service
- Fileserver
- NFS-Prozesse

## Problem Description
- User reported that scripts used for scheduling jobs on the login-node woody3 were hanging.
- Similar issue had occurred previously and was resolved by rebooting the NFS-Client.

## Root Cause
- The user had over 200 running jobs on Woody, causing a "denial-of-service" on the fileserver `/home/saturn`.
- The 10 Gbit-Interface was constantly at maximum capacity.

## Solution
- The number of NFS-Prozesse was increased from 128 to 256 to alleviate the situation.

## Lessons Learned
- High number of concurrent jobs can overload the fileserver and network interface.
- Increasing the number of NFS processes can help mitigate the issue.
- Regular monitoring of job loads and network usage is essential to prevent such issues.
```
---

### 2024071142003028_DDOS%20auf%20fundus%20fsmpet.md
# Ticket 2024071142003028

 # HPC-Support Ticket: DDOS auf fundus fsmpet

## Keywords
- DDOS Attack
- NFS Performance
- Baloo File Indexing Service
- Firewall Block
- NFS Mount Options

## Summary
A suspected DDOS attack was reported from a workstation (`mpet-pc01.physik.uni-erlangen.de`) to the NFS export server (`fundus.rrze.uni-erlangen.de`). The issue was caused by the Baloo file indexing service in the KDE desktop environment, which attempted to index the entire NFS directory tree, leading to excessive load.

## Root Cause
- The Baloo file indexing service was reactivated and attempted to index the entire NFS directory tree, causing high load on the NFS server.

## Solution
- The Baloo service was identified and deactivated, resolving the issue.
- NFS mount options were reviewed and confirmed to be optimal (`noauto,nosuid,noatime,bg,tcp,nfsvers=3,local_lock=all`).

## Lessons Learned
- **Baloo Service**: Ensure that the Baloo file indexing service is properly configured or deactivated to prevent excessive NFS load.
- **NFS Mount Options**: Use optimal NFS mount options to ensure efficient performance.
- **Firewall Management**: Temporarily blocking problematic IPs can help mitigate immediate issues while troubleshooting.

## Additional Notes
- The firewall block was removed after the issue was resolved.
- NFSv4.1 was suggested as a potential improvement over NFSv3, but user mapping issues may make it impractical.
- No custom `rsize` or `wsize` parameters were used, which is recommended for optimal performance.

This documentation can be used to troubleshoot similar NFS performance issues in the future.
---

### 2024100942003526_Lost%20Access%20to%20my%20files.md
# Ticket 2024100942003526

 # HPC-Support Ticket: Lost Access to Files

## Keywords
- File permissions
- NFS4 ACL
- Job failures
- I/O timeout
- ModuleNotFoundError

## Summary
A user attempted to grant access to their folders to a new account using `nfs4_setfacl` and `chmod` commands, resulting in permission issues and job failures.

## Root Cause
- Incorrect use of `nfs4_setfacl` and `chmod` commands led to permission issues in `$HOME` and `$WORK` directories.
- High load on the file server caused I/O timeouts and job crashes.
- A missing Python module (`vtimellm`) caused job failures.

## Commands Run by User
```bash
nfs4_setfacl -a A::b240dd10@rrze.uni-erlangen.de:X /home/atuin/v100dd/v100dd11
nfs4_setfacl -a A::b240dd10@rrze.uni-erlangen.de:X /home/hpc/v100dd/v100dd11
chmod -R o=rwx $WORK
chmod -R o=rwx $HOME
```

## Solution
- **HPC Admins** informed the user about the file server issues and provided a link to status updates.
- After the file server issue was resolved, the user was advised to restart their jobs.
- **HPC Admins** identified a missing Python module (`vtimellm`) causing job failures and asked the user to ensure the module is available.

## Lessons Learned
- Be cautious when modifying file permissions, especially with recursive commands.
- Check the HPC system status page for ongoing issues before reporting problems.
- Ensure all required modules and dependencies are available for job scripts.

## Related Links
- [Service Disruptions on Clusters due to High Load on Fileserver Atuin](https://hpc.fau.de/2024/10/09/service-disruptions-on-clusters-due-to-high-load-on-fileserver-atuin/)
---

### 2023010342001352_%24HOME%20nicht%20richtig%20gemounted%20auf%20applem1studio.md
# Ticket 2023010342001352

 # HPC Support Ticket: $HOME Mount Issue on applem1studio

## Keywords
- $HOME mount issue
- NFS mount failure
- Ganesha DNS cache
- IPv6 configuration
- Hostname change

## Problem Description
The user reported that the $HOME directory was not properly mounted on the `applem1studio` node in the test cluster. The error message indicated that the directory `/home/hpc/ihpc/ihpc030h` could not be found.

## Root Cause
- The hostname of the node had been changed from `apfel` to `applem1studio`.
- The Ganesha DNS cache was caching the old hostname, causing the mount to fail.
- IPv6 was misconfigured on the node, leading to connectivity issues.

## Troubleshooting Steps
1. **Manual Mount Attempt**: The HPC Admin attempted to manually mount the NFS share but encountered the same error.
2. **Netgroup Check**: Confirmed that the host was included in the appropriate netgroup.
3. **Ganesha DNS Cache**: Identified that the Ganesha DNS cache was caching the old hostname, causing the mount failure.
4. **IPv6 Configuration**: Noted that IPv6 was misconfigured on the node.

## Solution
1. **Temporary Workaround**: Added an additional NFS export for the IP address of `applem1studio` to bypass the DNS cache issue.
2. **IPv6 Configuration**: Requested the DNS team to add the IPv6 address for `applem1studio` according to the standard RRZE naming schema.
3. **Ganesha Restart**: Planned to restart the Ganesha processes during the next maintenance window to clear the DNS cache.

## Lessons Learned
- Changing the hostname after the initial installation can lead to issues with the Ganesha DNS cache.
- Ensure proper IPv6 configuration to avoid connectivity problems.
- Regular maintenance and updates are necessary to prevent known issues from affecting the system.

## Follow-up
- The HPC Admin will restart the Ganesha processes during the next maintenance window to clear the DNS cache.
- The user was notified that $HOME should now be available on the node, and $VAULT will be available after the maintenance.

## References
- Ganesha DNS cache issue is a known problem since early 2019.
- Standard RRZE naming schema for IPv6 addresses.
---

### 2023032242000402_High%20load%20on%20_home_woody%20%28iwsp005h%29.md
# Ticket 2023032242000402

 ```markdown
# High Load on NFS Servers

## Keywords
- High load
- NFS servers
- IO reduction
- Large datasets
- File quota
- SSD usage
- Compact file formats

## Problem Description
- High load on NFS servers providing `/home/woody` originating from jobs on `tinygpu`.
- User's jobs generating large datasets with high IO, leading to performance issues.

## Root Cause
- User's jobs were generating a large number of files (~13,000 each), causing high load on the NFS servers.
- Possible file quota limit reached, causing software to enter an unusual loop.

## Solution
- **Immediate Action**: User cleaned data storage and reduced the number of files being processed.
- **Long-term Solution**:
  - Write data to SSDs on the nodes of `tinygpu` and copy back to `/home/woody` at the end of the job.
  - Consider using more compact file formats like HDF5 or Nexus for future jobs, while retaining the option for standard ASCII (txt) files.

## Lessons Learned
- Regularly monitor and manage large datasets to avoid high load on NFS servers.
- Utilize local SSDs for temporary storage to reduce IO load on shared storage.
- Consider more efficient file formats for large datasets to optimize storage and IO performance.
```
---

### 2023061942003802_Zugriff%20auf%20atuin.md
# Ticket 2023061942003802

 ```markdown
# HPC-Support Ticket: Access to atuin Server

## Summary
User inquired about accessing data generated on the `fritzt-cluster` directly on the `atuin` server, as it seemed accessible only via the `alex-cluster`.

## Keywords
- Access
- atuin server
- fritzt-cluster
- alex-cluster
- NFS directories
- WinSCP

## Problem
- User could not find their project directory (`b109dc`) on the `fritzt-cluster` under `/home/atuin`.
- The directory was visible and accessible on the `alex-cluster`.

## Root Cause
- NFS directories only become visible when accessed.
- The `fritzt-cluster` had fewer NFS directories listed due to less frequent access.

## Solution
- User was advised to navigate to the directory using the command: `cd /home/atuin/b109dc/b109dc10`.
- For WinSCP access, the user was instructed to use `Ctrl+O` to open a dialog box and directly input the target path, even if the directory was not listed in the tree.

## Lessons Learned
- NFS directories need to be accessed to become visible.
- WinSCP can be used to directly input paths for accessing directories not listed in the tree.
- Detailed instructions and error messages are crucial for effective troubleshooting.
```
---

### 2019061742001183_Zeitweise%20Probleme%20beim%20hdf5%20Lesen%20von%20Saturn.md
# Ticket 2019061742001183

 ```markdown
# HPC Support Ticket: Intermittent Issues Reading HDF5 Files on Saturn

## Keywords
- HDF5
- NFS
- Python
- h5py
- OSError
- Input/output error
- NFSv3
- NFSv4
- GPU
- TinyGPU
- volta nodes

## Summary
- **Issue**: Intermittent problems reading HDF5 files from Saturn using Python and h5py.
- **Symptoms**: OSError with "Input/output error" when accessing HDF5 files.
- **Temporary Fix**: Copying files to local scratch and reading from there.

## Root Cause
- **Potential Cause**: NFS client issues on specific nodes (e.g., tg073).
- **Additional Factors**: Possible NFSv4 bugs, GPU-related issues.

## Troubleshooting Steps
- **Admin Actions**:
  - Increased NFS server threads from 64 to 128.
  - Set sysctls: `vm.swappiness=1`, `vm.min_free_kbytes=1500000`.
  - Considered reverting to NFSv3 to avoid NFSv4 bugs.

## Solution
- **Immediate Action**: Monitor the situation and consider node-specific issues.
- **Long-term**: Evaluate the stability of NFSv4 and consider reverting to NFSv3 if issues persist.

## Lessons Learned
- **NFS Issues**: NFS client problems can cause intermittent file access issues.
- **Temporary Workaround**: Copying files to local scratch can bypass NFS issues.
- **Log Analysis**: Regularly check node logs for NFS-related errors.
- **Version Considerations**: Evaluate the stability of different NFS versions in the HPC environment.
```
---

### 2024080542002815_ACL%20mag%20bei%20mir%20nicht.md
# Ticket 2024080542002815

 ```markdown
# HPC Support Ticket: ACL mag bei mir nicht

## Keywords
- ACL (Access Control List)
- nfs4_setfacl
- Operation not permitted
- Directory ownership

## Problem Description
- User attempted to set ACL permissions on a directory using `nfs4_setfacl`.
- Command failed with the error: `Failed setxattr operation: Operation not permitted`.

## Root Cause
- The user does not own the directory `/home/titan/sles/`.
- Only the owner of the directory can set ACL permissions.

## Solution
- The users who own the directories within `/home/titan/sles/` must set the ACL permissions themselves.

## Additional Notes
- `nfs4_setfacl` may not be installed on some systems, which could be intentional.

## Conversation Summary
- User attempted to follow an FAQ guide to set ACL permissions but encountered an error.
- HPC Admin responded that the user does not own the directory and thus cannot set ACL permissions.

## Action Items
- Inform users that they need to be the owners of the directories to set ACL permissions.
- Ensure that `nfs4_setfacl` is installed on necessary systems if required.
```
---

### 2024091342001782_File%20Access%20Rights.md
# Ticket 2024091342001782

 # File Access Rights Issue on Lustre Filesystem

## Keywords
- File access rights
- Lustre filesystem
- NFS4 ACL
- setfacl
- Project accounts

## Problem Description
- User has two project accounts and needs access to a directory on the Lustre filesystem.
- Access to old project directories is available, but access to the new directory `/anvme/workspace/v100dd11-hannan/` is denied.
- Error occurs due to incorrect ACL syntax for Lustre filesystem.

## Root Cause
- Lustre filesystem does not understand NFS4 ACL syntax.

## Solution
- Use `setfacl` command with appropriate syntax for Lustre filesystem.
  ```bash
  setfacl -m u:b240dd10:rx /anvme/workspace/v100dd11-hannan
  ```

## General Learning
- Different filesystems require different ACL syntax.
- Lustre filesystem uses `setfacl` for setting access control lists.
- Ensure correct syntax is used when setting permissions on different filesystems.

## Relevant Roles
- **HPC Admins**: Provide guidance on correct ACL syntax for Lustre filesystem.
- **2nd Level Support Team**: Assist users in resolving access issues and understanding filesystem-specific commands.
---

### 2022102142001008_Ausf%C3%83%C2%A4lle%20Filesystem.md
# Ticket 2022102142001008

 # HPC Support Ticket: Filesystem Failures

## Keywords
- Filesystem failures
- NFS
- RAM-Disk (/dev/shm)
- Stage-out
- Rechenzeitbonus
- Monitoring
- Linux-Kernel crash
- Storage-Hardware

## Problem
- Recurring filesystem failures affecting job performance.
- Linux-Kernel on the central NHR-Fileserver crashed multiple times without apparent reason.
- User jobs were impacted, leading to wasted compute time.

## Root Cause
- Unstable filesystem causing job interruptions and delays.
- Insufficient storage hardware leading to frequent crashes.

## Solution
- **Temporary Workaround:**
  - Use RAM-Disk (/dev/shm) for intermediate data storage during simulations.
  - Perform stage-out to NFS at the end of the job script to minimize dependency on the external filesystem.
- **Long-Term Solution:**
  - Await the arrival of additional storage hardware, expected in Q1 or Q2 of the following year.
  - Continue monitoring and managing job performance to mitigate the impact of filesystem issues.

## Actions Taken
- Provided a compute time bonus of 250,000 hours to compensate for affected jobs.
- Advised the user to implement the RAM-Disk workaround to reduce the impact of filesystem failures.

## Lessons Learned
- Filesystem stability is critical for job performance and compute time efficiency.
- Temporary workarounds like using RAM-Disk can help mitigate the impact of filesystem issues.
- Long-term solutions such as upgrading storage hardware are necessary for sustained performance.

## Recommendations
- Continue monitoring filesystem performance and stability.
- Implement temporary workarounds to minimize job interruptions.
- Plan for and expedite the acquisition of additional storage hardware to address long-term stability issues.
---

### 2024062442001338_Ordnerfreigabe%20f%C3%83%C2%BCr%20anderen%20HPC%20User.md
# Ticket 2024062442001338

 # HPC Support Ticket: Sharing Folder Access with Another HPC User

## Keywords
- NFS permissions
- POSIX permissions
- nfs4_setfacl
- nfs4_getfacl
- Woody-Frontend
- Testcluster
- AdaptiveCpp-Installation
- SYCL-Code

## Problem Description
A user wants to share access to their AdaptiveCpp installation with a Master's student who is working on a project involving SYCL-Code on the HPC test cluster. The user tried to follow the "Changing NFS permissions" guide but encountered issues with the `nfs4_setfacl` and `nfs4_getfacl` commands not being found.

## Root Cause
The user was unable to find the necessary NFS commands (`nfs4_setfacl` and `nfs4_getfacl`) to set the permissions for sharing the folder.

## Solution
The HPC Admin advised that the required commands are available on the Woody-Frontend. The user can set the NFS permissions there, and the folders should then be accessible when using the test cluster.

## General Learning
- NFS permissions can be set using `nfs4_setfacl` and `nfs4_getfacl` commands.
- These commands are available on the Woody-Frontend.
- Setting NFS permissions on the Woody-Frontend makes the folders accessible on the test cluster.
- If NFS commands are not available, POSIX permissions might need to be set as an alternative.

## References
- [Changing NFS permissions](https://doc.nhr.fau.de/data/share-perm-nfs/)
---

### 2023011842003199_default%20mode%20for%20the%20directory%20and%20subdirectories.md
# Ticket 2023011842003199

 # HPC Support Ticket: Default Mode for Directory and Subdirectories

## Keywords
- ACL (Access Control List)
- Default file permissions
- umask
- chmod
- sshfs

## Problem
- User wants to change the default mode for newly created files from `-rwxrwx---` to `-rw-rw-r--`.
- User faces permission issues when trying to access a directory from another system.

## Root Cause
- Incorrect ACL setup leading to unwanted default permissions.
- Missing execute (`x`) permission for others on the directory.

## Troubleshooting Steps
1. **Check ACL Setup**: The initial ACL setup was:
    ```
    A::OWNER@:rwaDxtTcCy
    A::210384:rxtcy
    A::GROUP@:rxtcy
    A::EVERYONE@:tcy
    A:fdi:OWNER@:rwaDxtTcCy
    A:fdi:210384:rwaDxtcy
    A:fdi:GROUP@:tcy
    A:fdi:EVERYONE@:tcy
    ```
2. **Check umask**: The umask value was `0022` on both systems (woody and alex).
3. **Directory Permission Issue**: The directory `/home/woody/iwbi/iwbi005h/Softwares` was missing the `x` permission for others.

## Solution
1. **Fix Directory Permission**: Added execute permission for others using `chmod o+x Softwares`.
2. **Adjust ACL for Default Permissions**: The HPC Admin adjusted the ACL setup to ensure the default mode for new files is `-rw-rw-r--`.
3. **User Action for Read Permission**: User was advised to add read permission for others using `chmod o+r /home/woody/iwbi/iwbi005h/` for convenient sshfs mounting.

## Notes
- Changing permissions to allow read access for others may expose data to all HPC users.
- The user was cautioned about the potential security implications of changing permissions.

## Conclusion
The issue was resolved by adjusting the ACL setup and directory permissions. The user was guided on how to set the desired default permissions and warned about the security implications of changing permissions.
---

### 2024011542003442_Removing%20the%20directory%20with%20input_output%20error.md
# Ticket 2024011542003442

 ```markdown
# HPC-Support Ticket: Removing Directory with Input/Output Error

## Keywords
- Disk mounting error
- NFS problems
- Directory removal
- Input/Output error

## Summary
A user encountered a disk mounting error while trying to install libraries and was unable to remove a specific directory. The HPC admins were unable to reproduce the issue and noted that files in the directory had modification dates after the reported issue.

## Root Cause
- The user experienced an input/output error, possibly related to NFS problems.

## Actions Taken
- The HPC admin checked the directory and found no issues.
- The admin noted that the directory had not been modified by them.
- The admin asked the user if the issue still persisted.

## Solution
- The issue was not resolved within the ticket conversation.
- Further investigation into NFS problems may be required.

## Notes
- The user provided a screenshot of the error but it was not included in the ticket text.
- The HPC admin mentioned that the certificate had expired, which might be unrelated to the main issue.

## Next Steps
- If the issue persists, the user should provide more details or a new screenshot.
- The HPC admin may need to investigate NFS problems further.
```
---

### 2024061942001884_Access%20Rights%20-%20Fritz%20-%20ACLs%20atuin.md
# Ticket 2024061942001884

 ```markdown
# HPC-Support Ticket: Access Rights - Fritz - ACLs atuin

## Keywords
- Access Rights
- NFS4 ACLs
- Tier2 Account
- Tier3 Account
- nfs4_setfacl
- nfs4_getfacl
- $WORK Directory

## Problem Description
The user wanted to grant access to their Tier2 account's $WORK directory to their Tier3 account to move data. Following the documentation, the user encountered an error when using `nfs4_setfacl` and `nfs4_getfacl`.

## Error Messages
- `Operation to request attribute not supported`
- `Failed to instantiate ACL`

## Root Cause
The issue was related to the NFS4 ACL commands not being supported for the specified directory.

## Solution
The HPC Admin suggested retrying the command, which eventually worked. The user was able to verify the ACL settings using `nfs4_getfacl`.

## Steps Taken
1. User attempted to set ACL using `nfs4_setfacl`.
2. User encountered errors and sought help from HPC Support.
3. HPC Admin suggested retrying the command.
4. User successfully set the ACL and verified it using `nfs4_getfacl`.

## Additional Information
- The user confirmed that the User-ID `387700` corresponded to their Tier3 account.
- The HPC Admin provided a command to verify the User-ID: `getent passwd | grep 387700`.

## Documentation Reference
- [NHR@FAU Documentation](https://doc.nhr.fau.de/data/share-perm-nfs/)
- [HPC System Meeting Wiki](https://gitlab.rrze.fau.de/hpc/hpc-system-besprechung/-/wikis/Knowledgebase.txt)
```
---

### 2024101842002082_HPC%20data%20share.md
# Ticket 2024101842002082

 # HPC Data Share Issue: NFS Mount Failure

## Keywords
- NFSv3
- Mount failure
- TCP vs UDP
- Firewall restrictions
- ACL (Access Control List)

## Problem Description
- Users were unable to mount an NFSv3 share from multiple Linux clients.
- The mount command used was: `sudo mount -t nfs -o vers=3 fundus.rrze.uni-erlangen.de:/faudatacloud/fsplantdatabc/shared /nfs/hpcstorage`
- Error message: `mount.nfs: mount system call failed`

## Root Cause
- Recent implementation of ACL restrictions for network security.
- Possible firewall restrictions on the client machines or network level.
- Default use of UDP for NFS, which might be affected by firewall rules.

## Solution
- Enforce the use of TCP instead of UDP for NFS mounting.
- Modify the mount command to include `proto=tcp`:
  ```bash
  sudo mount -t nfs -o vers=3,proto=tcp,nolock fundus.rrze.uni-erlangen.de:/faudatacloud/fsplantdatabc/shared /nfs/hpcstorage
  ```

## General Learnings
- NFS mount issues can be caused by network-level changes such as ACL restrictions.
- Enforcing TCP for NFS can resolve issues related to firewall restrictions on UDP traffic.
- Checking firewall rules and network configurations is crucial when diagnosing NFS mount problems.
- Using tools like `tcpdump` can help diagnose network-related issues during mount attempts.

## Next Steps for Similar Issues
- Verify network and firewall configurations.
- Ensure that the NFS client is using TCP instead of UDP.
- Use network diagnostic tools to trace the issue if the problem persists.
---

### 2024081542001655_home_vault.md
# Ticket 2024081542001655

 ```markdown
# HPC Support Ticket: home/vault Accessibility Issue

## Keywords
- NFS Mount
- Frontend Nodes
- Accessibility Issue
- Batch Processing
- Error Handling

## Problem Description
- **User Issue**: After the regular batch processing resumed on Fritz, the `home/vault` directory became inaccessible.
- **Root Cause**: The frontend node `fritz3` had problems with the NFS mount.

## Solution
- **Immediate Action**: Users were advised to log in to other frontend nodes (`fritz1`, `fritz2`, `fritz4`) to access the `home/vault` directory.
- **Follow-up**: The issue regarding "No space left in the device" error was transferred to the admins for further investigation.

## General Learnings
- **NFS Mount Issues**: Problems with NFS mounts can cause directories to become inaccessible.
- **Frontend Node Redundancy**: Users should be aware of alternative frontend nodes to access resources when one node is experiencing issues.
- **Error Reporting**: It is important to transfer and track related issues to ensure comprehensive problem resolution.

## Next Steps
- **Monitoring**: Continue monitoring the NFS mount status on `fritz3`.
- **Communication**: Inform users of any updates or resolutions regarding the NFS mount issue and the "No space left in the device" error.
```
---

### 2022020742001131_aborted%20job%20on%20Alex%20%5Bbcpc002h%5D.md
# Ticket 2022020742001131

 # HPC Support Ticket: Aborted Job on Alex [bcpc002h]

## Keywords
- Job aborted
- GPU failure
- Gromacs
- NFS server load
- Runinput file (.tpr)
- Monitoring
- Reboot

## Summary
A job on the Alex HPC system was aborted due to a software issue on the GPU. The job was restarted but encountered further issues, indicating a problem with the input file.

## Root Cause
- Initial failure due to software issue on the GPU.
- Subsequent failures likely due to issues with the input file (.tpr).

## Steps Taken
1. **Initial Issue**:
   - HPC Admin noticed the GPU was not being utilized.
   - Job was aborted and the node was rebooted.
   - User was informed and asked to restart the simulation.

2. **Subsequent Failures**:
   - Job aborted again, this time not related to hardware.
   - HPC Admin suggested running the job CPU-only to identify any errors.
   - User was asked to provide the .tpr file for further investigation.

3. **NFS Server Load**:
   - HPC Admin noticed that some Gromacs jobs were suffering under the load on NFS servers.
   - Suggested removing the "-v" flag from the Gromacs command to reduce network load.

## Solution
- User created a new .tpr file and restarted the job.
- User agreed to remove the "-v" flag from the Gromacs command to reduce NFS server load.

## Conclusion
The issue was initially hardware-related but later shifted to a potential problem with the input file. The user was guided to make necessary adjustments to the job configuration to mitigate further issues.

## Notes
- The ticket was closed as the user decided to troubleshoot the issue independently.
- The user was advised to upload relevant files to FAUbox if the job aborts again.
---

### 2023032042003681_Alex%20GPU%20Cluster%3A%20sehr%20langsamer%20Zugriff%20auf%20%24WORK.md
# Ticket 2023032042003681

 ```markdown
# HPC Support Ticket: Slow Access to $WORK on Alex GPU Cluster

## Keywords
- Slow access
- $WORK
- Conda environments
- Job output
- NFS servers
- High load

## Problem Description
- User reported extremely slow access to `$WORK` (`/home/woody/iwal/iwal081h`) on the Alex GPU Cluster.
- Slow access affected the loading of Conda environments and job output writing, causing significant delays.
- Job performance was notably slower when writing output to `$WORK` compared to `$HPCVAULT`.

## Root Cause
- High load on NFS servers due to other users' jobs, specifically `iwbn002h` on Meggie and `iwia041h` on Fritz.
- The high load caused significant performance degradation for other users accessing the same NFS servers.

## Solution
- HPC Admins identified and addressed the high load on NFS servers.
- Users were advised to report if the issue persisted.

## Lessons Learned
- High load on NFS servers can cause significant performance issues for other users.
- Monitoring and managing NFS server load is crucial for maintaining system performance.
- Users should be aware of the impact of high I/O operations on shared resources.

## Recommendations
- Regularly monitor NFS server performance.
- Implement policies to manage high I/O jobs to prevent performance degradation for other users.
- Educate users on best practices for managing job outputs and environments to minimize impact on shared resources.
```
---

### 2018111942000538_.nfs%20files.md
# Ticket 2018111942000538

 # HPC Support Ticket: .nfs Files Issue

## Keywords
- .nfs files
- NFS share
- MobaXterm
- fuser
- lsof
- VPN
- Session management

## Problem Description
The user encountered .nfs files that could not be deleted. These files were created when opening and closing text files via MobaXterm without explicitly saving them. The user attempted to identify the process using the files with `fuser` and `lsof`, but no process was found.

## Root Cause
- The .nfs files are created when a file is open and then deleted while still in use.
- MobaXterm may be creating temporary files that are not easily traceable with `lsof`.
- The files should disappear once the session holding them open is terminated.

## Solution
- Ensure that all sessions and processes holding the files open are properly terminated.
- Use `lsof` to identify any hidden processes that might be keeping the files open.
- If the files persist, they may be held open by another host or job running on the system.

## Lessons Learned
- Always use official support channels for reporting issues.
- .nfs files are typically created when a file is deleted while still in use.
- MobaXterm can create temporary files that are not easily traceable.
- Terminating the session holding the files open should resolve the issue.
- Check for open files across multiple hosts and jobs if the problem persists.

## Actions Taken
- The HPC Admin identified and terminated a session that was holding one of the files open.
- The user was advised to check for other sessions or jobs that might be holding the files open.

## Future Prevention
- Ensure all sessions are properly terminated after use.
- Use official support channels for any future issues to ensure timely and effective resolution.

## References
- [NFS FAQ](http://nfs.sourceforge.net/#faq_d2)
---

### 2020050642001514_Can%27t%20access%20terminal%20after%20logon.md
# Ticket 2020050642001514

 # HPC Support Ticket: Can't Access Terminal After Logon

## Keywords
- Terminal access issue
- NFS file server
- Network component failure
- HPC systems: Meggie, Emmy
- Quota

## Problem Description
- User unable to access terminal after logging into HPC systems Meggie and Emmy.
- User had access the previous day and was below the home directory quota.
- User could log in and mount `$FASTTMP`.

## Root Cause
- Faulty network component caused one of the NFS file servers to be unreachable, leading to issues across all HPC systems.

## Solution
- The network component issue was resolved, restoring full operational status to all HPC systems.

## Lessons Learned
- Network component failures can affect terminal access on HPC systems.
- NFS file server reachability is critical for terminal functionality.
- Resolving network issues can restore terminal access for users.

## Actions Taken
- HPC Admins identified and resolved the network component issue.
- User confirmed that terminal access was restored.

## Follow-Up
- Monitor network components and NFS file server reachability to prevent similar issues.
- Ensure users are informed about system status and any ongoing maintenance or issues.
---

### 2024022242002875_Node%20allocation.md
# Ticket 2024022242002875

 # HPC Support Ticket: Node Allocation

## Subject
Node allocation issues with single GPU allocations on Alex.

## User Report
- Single GPU allocations, including A40, are taking longer despite many nodes being listed as `mix` in `sinfo`.
- Users are experiencing delays in small allocations that were previously immediate.

## Root Cause
- **NFS Crashes**: Multiple NFS crashes (5 in the last 8 days) have led to a "same user" policy to improve stability.
- **Increased Demand**: Higher demand from HS-Coburg for their financed nodes, leading to exclusive reservations.
- **NFS Usage**: High NFS file open rates (up to 840 opens per second) by certain users, impacting performance.

## Solution
- **Policy Change**: Implemented a "same user" policy to quickly react to NFS misuse and improve operational stability.
- **Data Handling**: Recommended using `$TEMPDIR` or webdatasets to reduce NFS load.
- **Monitoring**: Monitoring NFS usage and providing insights on file open rates to optimize data handling.

## Keywords
- Node allocation
- SLURM
- NFS crashes
- NFS misuse
- Data handling
- Policy change
- Monitoring

## General Learnings
- High NFS usage can impact overall system performance.
- Implementing policies to manage NFS usage can improve stability.
- Optimizing data handling practices can reduce load on shared resources.
- Monitoring and providing insights on resource usage can help users optimize their workflows.

## Next Steps
- Continue monitoring NFS usage and adjust policies as needed.
- Encourage users to adopt best practices for data handling to reduce NFS load.
- Plan for maintenance to address underlying issues causing NFS crashes.
---

### 2022121242000102_Tier3-Access-Alex%20%22Tuhin%20Mallick%22%20_%20iwai007.md
# Ticket 2022121242000102

 # HPC Support Ticket Analysis: Tier3-Access-Alex

## Keywords
- GPU utilization
- NFS filesystem abuse
- Early stopping issue
- Data staging
- Local SSD usage

## Summary
A user requested access to the 'Alex' GPGPU cluster but was initially denied due to poor GPU utilization and improper use of the NFS filesystem. The user addressed these issues, leading to a resolution.

## Root Cause of Problems
1. **Poor GPU Utilization**: The user's jobs showed low GPU utilization due to an early stopping issue in the code.
2. **NFS Filesystem Abuse**: The user was permanently accessing files from the NFS instead of staging data to the local SSD.

## Solutions
1. **GPU Utilization**: The user fixed the early stopping issue in the code, which should improve GPU utilization.
2. **NFS Filesystem**: The user was advised to stage data to the local SSD instead of constantly accessing files from the NFS. The specific problematic path was identified as `/home/vault/iwai/iwai007h/Data/nnood_preprocessed_data_base_thres/heraus_png/`.

## General Learnings
- Always check for efficient resource utilization when reviewing user requests.
- Ensure users are aware of proper data staging practices to avoid excessive NFS usage.
- Communicate specific issues and paths to users for clarity in resolving problems.

## Follow-up
- Monitor the user's jobs to ensure improved GPU utilization.
- Verify that the user is staging data correctly to the local SSD.

## Related Software
- numpy
- nibabel
- SimpleITK
- tqdm
- opencv-python
- pandas
- torch>=1.10.0
- matplotlib
- sklearn
- scikit-learn>=1.0.1
- batchgenerators>=0.23
- scikit-image>=0.19.0
- argparse
- scipy
- unittest2

## Application
The user is working on a self-supervised framework for anomaly detection in images using nnOOD and nnUnet, requiring intensive computational resources.

## Expected Outcomes
The user aims to achieve anomaly detection in images using unsupervised learning without annotation, integrating various self-supervised learning methods and creating an ensemble for optimal results.

## Additional Notes
The user is under time pressure due to writing a master's thesis, emphasizing the importance of timely access to computational resources.
---

### 2022111042000368_Massiver%20IO%20von%20Jobs%20auf%20Alex%20-%20iwai003h.md
# Ticket 2022111042000368

 ```markdown
# HPC Support Ticket: Massiver IO von Jobs auf Alex - iwai003h

## Keywords
- NFS-Dateisysteme
- IO-Bottleneck
- Hauptspeicher
- GPU
- Checkpoint
- $TMPDIR
- Knoten-lokale SSD

## Problem
- User's jobs on Alex were causing excessive IO on NFS-shared resources, affecting other HPC users.
- The jobs were accessing data from `/home/saturn` continuously, leading to performance degradation for all users.

## Root Cause
- Continuous data access from NFS-shared resources, causing high IO load.
- Insufficient preloading of data into the host's main memory.

## Solution
- **Short-term**: Allow the job to run until the next checkpoint to avoid significant loss of computation time.
- **Long-term**:
  - Preload data into the host's main memory to reduce NFS access.
  - Use `$TMPDIR` for local storage to avoid affecting other users on the same node.
  - Optimize data handling to minimize IO operations and keep data in memory whenever possible.

## Lessons Learned
- **IO Impact**: Continuous IO operations on shared NFS resources can significantly impact the performance of all users.
- **Preloading**: Preloading data into the host's main memory can reduce IO load and improve performance.
- **Local Storage**: Using `$TMPDIR` for local storage can minimize the impact on other users on the same node.
- **Communication**: Inform colleagues and successors about best practices to avoid similar issues in the future.

## Additional Notes
- The user was advised to sensitize colleagues and successors about the importance of minimizing IO operations on shared resources.
- The user was informed that `$TMPDIR` on TinyGPU and Alex is on a node-local SSD, which is faster than NFS but still costly in terms of IO.
```
---

### 2024011842002009_very%20low%20performance%20of%20WORK%20filesystem.md
# Ticket 2024011842002009

 ```markdown
# HPC-Support Ticket: Very Low Performance of WORK Filesystem

## Keywords
- $WORK filesystem
- Performance issue
- Supercomputing lab course
- $HPCVAULT
- Alex cluster
- Ceph
- Tier3
- /home/woody
- wnfs1
- nfstop

## Problem Description
- User reports very low performance (below 2 MB/s) when reading from a single large file on the $WORK filesystem of the Alex cluster.
- User does not have access to the $HPCVAULT filesystem due to being in the supercomputing lab course.

## Troubleshooting Steps
- HPC Admin noted that the issue is being discussed with the 2nd Level Support team.
- Ceph is suggested to be tested as a potential solution.
- HPC Admin mentioned that the $WORK filesystem for the supercomputing lab course is located on /home/woody, indicating that Atuin is not the cause.
- wnfs1 has been performing well with >3 GB/s read and >1 GB/s write speeds.
- Current performance reported by nfstop shows "scvl109h 160.56MB/s".

## Solution
- No explicit solution provided in the conversation.
- Further investigation and testing with Ceph are recommended.

## General Learnings
- Performance issues on the $WORK filesystem can be caused by various factors, including filesystem location and configuration.
- Testing alternative filesystems like Ceph can help identify and resolve performance bottlenecks.
- Monitoring tools like nfstop can provide valuable insights into current performance metrics.
```
---

### 2021062242002524_Lokale%20SSD%20f%C3%83%C2%BCr%20Jobs%20auf%20A100%3F%20slli02.md
# Ticket 2021062242002524

 # HPC Support Ticket: Local SSD for Jobs on A100

## Keywords
- IO-Wait
- Ethernet-Traffic
- NFS-Read
- SSD
- Data Copying
- Job Performance
- Apache Arrow
- Memory Mapping
- Data Sharding

## Problem
- User's job on TinyGPU showed persistent 25-30% IO-Wait and ~150 MB/s Ethernet traffic, likely due to NFS-Read.
- Initial suspicion was that memory mapping of Apache Arrow with large files was causing performance issues.

## Troubleshooting Steps
1. **Data Copying to SSD**: HPC Admin suggested copying data to `/scratchssd/` at the beginning of the job to reduce IO-Wait.
2. **Data Sharding**: User attempted to shard the dataset to improve performance.
3. **Reducing Shard Size**: User planned to reduce shard size by a factor of ten to further optimize performance.

## Issues Encountered
- The SSD on `tg095` had only 30G free and was 64G in total, which was insufficient for the user's data.

## Solution
- HPC Admin reserved `tg093` for the user, which was automatically utilized.
- Additional A100 nodes were added, but data SSDs were delayed due to supply issues.

## Outcome
- The user successfully utilized the reserved node `tg093` for their job.

## General Learnings
- High IO-Wait and Ethernet traffic can be mitigated by copying data to local SSDs.
- Data sharding and reducing shard size can help optimize job performance.
- Reserving nodes with sufficient resources can temporarily resolve hardware limitations.

## Next Steps
- Monitor job performance after implementing data sharding and reduced shard size.
- Ensure timely delivery and installation of additional SSDs for new A100 nodes.
---

### 2025031142001606_Experiencing%20laggy_slow%20in%20Alex.md
# Ticket 2025031142001606

 # HPC Support Ticket: Laggy/Slow Performance in Alex Cluster

## Keywords
- Laggy performance
- Slow connection
- Alex cluster
- VS Code connection issues
- NFS-Filesystem overload
- Small files processing

## Problem Description
Users have been experiencing slow and laggy performance on the Alex cluster, which has been increasingly frequent. This issue also affects the connection to Alex via VS Code due to connection time limits.

## Root Cause
The root cause of the problem is the overloading of the NFS-Filesystem by some users. This overload is often due to the processing of many small files on the NFS instead of using node-local SSD.

## Solution
HPC Admins are working to identify and address the users causing the overload. Users are advised to process small files on node-local SSD instead of the NFS-Filesystem to mitigate the issue.

## General Learnings
- Overloading the NFS-Filesystem can cause widespread performance issues.
- Processing many small files on the NFS should be avoided.
- Node-local SSD should be used for processing small files to prevent NFS overload.
- HPC Admins need to monitor and identify users causing NFS overload to maintain system performance.
---

### 2023013142003182_Anlegen%20eines%20neuer%20Verzeichnise%20unter%20_home_vault_empkins.md
# Ticket 2023013142003182

 # HPC Support Ticket Conversation Analysis

## Keywords
- Directory creation
- NFS4 ACLs
- Ownership
- Inheritance

## Summary
A user requested the creation of new directories under `/home/vault/empkins` with specific NFS4 ACLs and inheritance settings similar to existing directories. The HPC Admin clarified the ownership of the new directories and completed the task.

## Problem
- User requested new directories (`tpA`, `tpB`, `tpE`) under `/home/vault/empkins`.
- Directories needed NFS4 ACLs with inheritance, similar to existing `tpX` directories.

## Solution
- HPC Admin created the directories.
- Set the user (`iwhf002h`) as the owner.
- Configured NFS4 ACLs with inheritance as requested.

## Lessons Learned
- Always clarify ownership when creating new directories.
- Ensure NFS4 ACLs and inheritance settings are correctly applied to new directories.
- Communication between the user and HPC Admin is crucial for task completion.

## Roles Involved
- HPC Admins
- User (Dr.-Ing. Jan Schür)

## Related Teams
- 2nd Level Support team
- Software and Tools developers
- Head of the Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support and Applications for Grants
---

### 2022122042000347_Fw%3A%20NHR%40FAU%20Rechenzeitdiscount%20im%20Dezember%21%20-%20b114cb.md
# Ticket 2022122042000347

 ```markdown
# HPC Support Ticket Conversation Summary

## Keywords
- Model training
- Longer job runs
- Loading model weights
- Walltime extension
- NFS file server crash
- Python error (FileNotFoundError)

## General Learnings
- Users can request longer job runs during low-demand periods.
- Manual walltime extension can be done by HPC Admins.
- NFS file server issues can cause login stalls.
- Users should check for cluster changes if jobs fail unexpectedly.

## Issues and Solutions

### Issue: Longer Job Runs for Model Training
- **Root Cause**: Users need longer job runs to avoid frequent model weight loading.
- **Solution**: HPC Admins can manually extend walltime for submitted jobs.

### Issue: Login Stalls
- **Root Cause**: NFS file server crash with a kernel dump.
- **Solution**: HPC Admins resolved the issue by restarting the server.

### Issue: Python Error (FileNotFoundError)
- **Root Cause**: Possible folder deletion during command execution.
- **Solution**: User resolved the issue by changing job specifications.

## Actions Taken
- HPC Admins manually extended walltime for jobs.
- HPC Admins resolved NFS file server crash.
- User adjusted job specifications to resolve Python error.

## Notes
- Users should submit jobs with the standard walltime and request extensions if needed.
- HPC Admins can provide support during holidays and low-demand periods.
- Users should check for cluster changes if jobs fail unexpectedly.
```
---

### 2024081342001373_Datensicherung%20auf%20NFS-Volume%20-%20W.%20Utz%20_%20fsbcpc01.md
# Ticket 2024081342001373

 ```markdown
# HPC-Support Ticket: Datensicherung auf NFS-Volume

## Subject
Datensicherung auf NFS-Volume

## User Issue
- User has stopped cron jobs for data backup on the provided NFS-Volume.
- Requests to keep the current data on the NFS-Volume for a few weeks before deletion.
- Will notify HPC support for final deletion and termination of the NFS mount.

## HPC Admin Actions
- Acknowledged the user's request.
- Requested user to notify when the NFS share can be removed.
- Followed up on the data copying progress.
- Removed the NFS export and planned for final deletion if no further requests by the end of October.
- Deleted the fileset and removed all snapshots.

## Keywords
- NFS-Volume
- Cron jobs
- Data backup
- NFS mount
- Data deletion
- Snapshots

## Lessons Learned
- Importance of clear communication regarding data backup and deletion timelines.
- Proper follow-up and confirmation before final deletion of data.
- Documentation of steps for removing NFS shares and deleting filesets.

## Solution
- User stopped cron jobs and requested data retention for a few weeks.
- HPC Admin acknowledged and followed up on data copying progress.
- Final deletion of the NFS share and fileset was performed after user confirmation.
```
---

### 42061982__home_cluster32.md
# Ticket 42061982

 # HPC Support Ticket: /home/cluster32

## Keywords
- NFS
- /home/cluster32
- umount
- mysqld
- sfront03
- automountertabellen

## Summary
The user encountered issues accessing their project server due to the decommissioning of `/home/cluster32`. The NFS server was temporarily reactivated to resolve the issue.

## Root Cause
- The `/home/cluster32` directory was decommissioned on October 14th, causing access issues for the user's project server which had `/home/cluster32` mounted via NFS.

## Solution
- The HPC Admin temporarily reactivated the NFS server to allow the user to unmount the directory and resolve the access issues.

## Additional Issues
- The user reported a separate login issue with `sfront03`, which was acknowledged by the HPC Admin.

## Steps Taken
1. User reported access issues with their project server due to the decommissioning of `/home/cluster32`.
2. HPC Admin confirmed the decommissioning and offered to temporarily reactivate the NFS server.
3. User requested the reactivation to resolve the access issues.
4. HPC Admin reactivated the NFS server, allowing the user to unmount the directory.
5. User reported a separate login issue with `sfront03`, which was acknowledged by the HPC Admin.

## Conclusion
The temporary reactivation of the NFS server resolved the user's access issues with their project server. The separate login issue with `sfront03` was acknowledged and remains to be addressed.
---

### 2020050642001596_Problems%20with%20woody%20cluster.md
# Ticket 2020050642001596

 ```markdown
# HPC Support Ticket: Problems with Woody Cluster

## Keywords
- Woody Cluster
- Terminal Prompt
- NFS File Server
- Network Component
- Faulty Component

## Issue Description
- **User Report**: The terminal prompt does not appear after connecting to the Woody cluster.
- **Root Cause**: A faulty network component caused one of the NFS file servers to be unreachable, leading to issues on all HPC systems.

## Solution
- **Admin Action**: Identified and resolved the network component issue.
- **Status**: All systems are fully operational again.

## Lessons Learned
- Network component failures can affect the availability of NFS file servers, leading to issues with terminal prompts on HPC clusters.
- Regular monitoring and maintenance of network components are crucial to prevent such issues.

## Next Steps
- Continue monitoring network components to ensure stability.
- Implement redundancy for critical network components to minimize downtime.
```
---

### 2024070242003251_ACL%20auf%20Janus%20und%20Atuin.md
# Ticket 2024070242003251

 # HPC Support Ticket: ACL auf Janus und Atuin

## Keywords
- ACL
- NFS4ACL
- Janus
- Shared folder
- POSIX Rechte
- NHR@FAU Projektaccounts

## Problem
- User cannot set ACLs on Janus for a shared folder (`/home/janus/iwb6-datasets`).
- `nfs4_getfacl` command returns "Operation to request attribute not supported."
- POSIX rights cannot be managed via the `iwb6` group due to some users having NHR@FAU project accounts.

## Root Cause
- ACLs were not initially activated on Janus.
- After activation, the client system had issues recognizing the changes.

## Solution
1. **Activate ACLs on Janus:**
   - HPC Admins enabled NFS4ACL for the specified directory.

2. **Restart `autofs` on the frontend:**
   - A `systemctl restart autofs` command resolved the client-side issue, allowing ACLs to be set correctly.

## Additional Notes
- Ensure that the client system is properly configured to recognize ACL changes.
- If issues persist, consider restarting relevant services on the client system.

## Conclusion
- The problem was resolved by activating ACLs on Janus and restarting the `autofs` service on the client system.
- This solution can be applied to similar issues where ACLs are not recognized after activation.
---

### 2024021042000256_Ausfall%20des%20NFS%20Systems.md
# Ticket 2024021042000256

 # HPC Support Ticket: Ausfall des NFS Systems

## Keywords
- NFS System
- Datenverlust
- Ausfall
- /home/atuin
- Blogpost
- HPC Services

## Problem
- **User Issue:** Der Pfad `/home/atuin` ist aufgrund eines Ausfalls des NFS Systems nicht erreichbar.
- **Root Cause:** Ausfall des NFS Systems.

## Solution
- **Admin Response:** Das Problem sollte in wenigen Minuten behoben sein. Es gibt keinen Datenverlust.
- **Additional Information:** Mehr Details im Blogpost: [Outage of HPC Services due to File System Issues Solved](https://hpc.fau.de/2024/02/10/outage-of-hpc-services-due-to-file-system-issues-solved/)

## Lessons Learned
- Bei einem Ausfall des NFS Systems kann der Zugriff auf bestimmte Pfade wie `/home/atuin` vorübergehend nicht möglich sein.
- HPC Admins arbeiten daran, solche Probleme schnell zu beheben und informieren die Benutzer über den Status.
- Es ist wichtig, die Benutzer über Blogposts oder andere Kommunikationskanäle auf dem Laufenden zu halten.

## Actions Taken
- HPC Admins haben das Problem identifiziert und eine Lösung implementiert.
- Benutzer wurden über den Status und die Lösung informiert.
- Ein Blogpost wurde veröffentlicht, um detaillierte Informationen bereitzustellen.

## Future Reference
- Bei ähnlichen Ausfällen sollten Benutzer die HPC Admins kontaktieren und auf Blogposts oder andere offizielle Kommunikationskanäle achten, um den aktuellen Status zu erfahren.
- HPC Admins sollten weiterhin schnell auf solche Probleme reagieren und die Benutzer informieren.
---

### 2024081542002887_Error%20resulting%20in%20.nfs%20file.md
# Ticket 2024081542002887

 ```markdown
# HPC-Support Ticket: Error resulting in .nfs file

## Problem Description
- User encountered an issue where they could not remove a testing folder due to an `.nfs` file.
- The error message received was: `'cannot remove '.nfs0000000009cd86ac000000dd': Device or resource busy'`.
- The file was located at `/home/hpc/iwi1/iwi1015h/results/CLIP-R/test/00001/default/.nfs0000000009cd86ac000000dd`.

## Root Cause
- `.nfs` files are created when trying to delete a still open file.
- A process was holding onto the file, preventing its deletion.

## Troubleshooting Steps
1. **Identify Hanging Process**:
   - User was advised to use `ps` to find the hanging process and `kill` it.
   - No unwanted processes were found using `ps`.

2. **Check for Hidden Processes**:
   - HPC Admin confirmed there are no hidden processes but suggested the process might be on a different machine.

3. **Admin Intervention**:
   - HPC Admin offered to delete the file from the storage system.
   - The file was successfully deleted by the HPC Admin.

## Solution
- The `.nfs` file was removed by the HPC Admin from the storage system.

## Keywords
- `.nfs` file
- Device or resource busy
- Hanging process
- `ps` command
- `kill` command
- Storage system deletion

## General Learnings
- `.nfs` files can be created when trying to delete a still open file.
- Use `ps` to identify and `kill` hanging processes.
- If no processes are found, the issue might be on a different machine.
- HPC Admin can delete the file from the storage system if necessary.
```
---

### 2022122342001724_Command%20prompt%20wird%20nicht%20angezeigt..md
# Ticket 2022122342001724

 ```markdown
# HPC Support Ticket: Command Prompt Not Displayed

## Keywords
- Command prompt
- Cluster login
- NFS file server
- Kernel dump
- System administrator

## Problem Description
- User unable to see the command prompt upon logging into the cluster.
- Internet connection ruled out as the cause.

## Root Cause
- One of the NFS file servers crashed with a kernel dump, causing logins to stall.
- Expired certificate.

## Solution
- The issue was resolved by addressing the NFS file server crash and the expired certificate.

## Lessons Learned
- Always specify the server you are trying to connect to when reporting issues.
- NFS file server crashes can lead to login stalls and command prompt issues.
- Expired certificates can also cause login problems.

## Next Steps
- Ensure NFS file servers are monitored for crashes.
- Regularly check and renew certificates to prevent expiration issues.
```
---

### 2024080642003027_Noch%20eine%20Frage%20zu%20ACLs.md
# Ticket 2024080642003027

 ```markdown
# HPC Support Ticket: Noch eine Frage zu ACLs

## Keywords
- ACLs
- NFS4
- nfs4_setfacl
- Access Control
- Performance

## Problem
- User attempted to set ACLs using `nfs4_setfacl` but encountered an error: "Operation to request attribute not supported."
- User needed to grant access to a specific directory (`/home/atuin/b105dc/data/`) for another user.

## Root Cause
- ACL support was not enabled for the project on the HPC system.

## Solution
- HPC Admin activated ACL support for the project.
- User was instructed to try setting the ACL again after the support was enabled.

## Lessons Learned
- ACL support needs to be explicitly enabled on a per-project basis on the HPC system.
- Enabling ACLs may have performance implications, hence it is not enabled by default.
- Users should contact HPC support to enable ACLs if they encounter similar issues.
```
---

### 2024102442003104_ACL%20support%20for%20home.md
# Ticket 2024102442003104

 ```markdown
# HPC Support Ticket: ACL Support for Home

## Keywords
- ACL
- NFS ACL
- Multiple Accounts
- Code Sharing
- Home Directory

## Problem
- User has multiple accounts on the HPC system.
- Wants to share compiled code between accounts to avoid redundant compilation.
- ACL (Access Control List) is not supported on the home directory.

## Root Cause
- Lack of ACL support on the home directory prevents easy sharing of files between multiple user accounts.

## Solution
- Use NFS ACL as described in the documentation: [NFS ACL Documentation](https://doc.nhr.fau.de/data/share-perm-nfs/).

## General Learnings
- Users with multiple accounts may need to share files between accounts.
- NFS ACL can be used as an alternative to traditional ACL for sharing files in the home directory.
- Documentation and support resources should be provided to users for setting up NFS ACL.

## Ticket Status
- Closed after providing the user with the NFS ACL documentation link.
```
---

### 2024112742005015_%27_home_atuin_b114cb%27%3A%20Stale%20file%20handle.md
# Ticket 2024112742005015

 # HPC Support Ticket: Stale File Handle Issue

## Keywords
- Stale file handle
- NFS server
- ZFS
- Directory access issue
- System restart

## Problem Description
- User reported inaccessible directory `/home/atuin/b114cb` due to a broken link.
- Error message: `Stale file handle` when attempting to access the directory.

## Root Cause
- The NFS server on the `atuin` machine was experiencing issues, causing the directory to be inaccessible.

## Diagnostic Steps
- HPC Admin checked the status of the directory on different nodes.
- Commands used:
  ```sh
  df -h /home/atuin/b114cb
  ls -l /home/atuin
  ```
- Found that the directory was inaccessible with a `Stale file handle` error.

## Solution
- Restarting the NFS server on the `atuin` machine resolved the issue.
  ```sh
  systemctl restart nfs-kernel-server
  ```

## General Learnings
- Stale file handle errors often indicate issues with the NFS server.
- Restarting the NFS server can resolve such issues.
- Regular monitoring and maintenance of NFS servers are crucial to prevent such problems.

## Additional Notes
- The `atuin` machine has been causing multiple issues, indicating a need for further investigation and potential maintenance.
- ZFS file system was mentioned, which might be related to the underlying issues.

---

This documentation can be used to troubleshoot similar issues in the future.
---

### 2024062742002877_high%20trafic%20on%20atuin%20%5Bv104dd12%5D.md
# Ticket 2024062742002877

 ```markdown
# HPC Support Ticket: High Traffic on Alex

## Keywords
- High NFS rate
- GPU utilization drop
- Data staging
- Node local storage
- Lustre
- CEPH
- Ethernet connection

## Problem
- User's jobs on Alex show a high NFS rate (~100 MB/s).
- The fileserver is overloaded, causing drops in data rate and GPU utilization.
- The job is waiting for data, leading to inefficiency.

## Root Cause
- High NFS traffic due to large data shards (1 GB) being accessed frequently.

## Solution
- **Data Staging**: Copy input data to node local storage at job start.
  - Estimated time: 5-10 minutes.
  - Benefit: Speeds up the rest of the computation.
- **Bandwidth for Copying**:
  - Theoretical limit: 25 GBit ethernet connection.
  - Estimated time for 1 TB: ~6 minutes, but likely slower.
  - Recommendation: Perform a test run as a benchmark.
- **Alternative Storage Solutions**:
  - Lustre: Not significantly faster due to ethernet connection.
  - CEPH: Currently not recommended due to software stack replacement.
  - Best practice: Copy data from `$work` to `/scratch` at job start.

## Additional Information
- Documentation: [Data Staging](https://doc.nhr.fau.de/data/staging)
- Contact: HPC Admins for further assistance.
```
---

### 2022041442003022_NFS%20share.md
# Ticket 2022041442003022

 # HPC Support Ticket: NFS Share Issues

## Subject: NFS Share

## Keywords:
- NFS Share
- VPN Access
- IP Addresses
- Connection Loss
- Permission Issues
- MacOS Compatibility

## Summary:
The user encountered several issues with the NFS share, including connection loss, permission problems, and compatibility issues with MacOS.

## Issues and Solutions:

### 1. VPN Access
- **Issue:** User inquired about accessing the NFS share via VPN.
- **Solution:** VPN access is possible as it provides fixed IPs. The user provided the necessary IdM-Kennungen for freischaltung.

### 2. IP Addresses and Office Move
- **Issue:** User is moving to a new building and inquired about IP address changes.
- **Solution:** The user needs to check with their IT department to determine if they will retain the current IPs or get new subnets.

### 3. Connection Loss and Permission Issues
- **Issue:** User experienced connection loss and permission problems when mounting the NFS share from a Mac.
- **Solution:**
  - The HPC Admin suspected user mapping issues between MacOS and Linux.
  - The admin cleaned up "dateileichen" (dead files) in the shared directory.
  - The admin suggested disabling the creation of metadata files on network volumes to avoid issues with `.DS_Store` and AppleDouble `._` files.
  - Command: `defaults write com.apple.desktopservices DSDontWriteNetworkStores -bool true`

### 4. MacOS Compatibility
- **Issue:** Working in the Finder on MacOS caused the NFS share to become unusable.
- **Solution:**
  - The admin observed that working via the command line was possible, but the Finder caused issues.
  - The admin suggested using SMB-capable network storage if the user relies on the Finder.

### 5. Alternative Solution
- **Issue:** Persistent issues with the NFS share.
- **Solution:** The user is considering using the Anubis server, which seems to meet their requirements.

## Conclusion:
The user's issues with the NFS share were partially resolved by addressing permission and metadata file creation problems. However, persistent compatibility issues with MacOS led the user to consider alternative storage solutions.

## Notes:
- The IBM Spectrum Scale Admin Guide does not mention MacOS, suggesting potential compatibility issues.
- The admin's tests on a MacOS 10.15.7 client confirmed that working via the command line is possible, but the Finder causes failures.

## Closure:
The ticket was closed with the user considering alternative storage solutions due to persistent issues with the NFS share on MacOS.
---

### 2022031442003202_beschr%C3%83%C2%A4nkung%20tinyGPU%20nutzung%20%28kennung%20mppm001h%29.md
# Ticket 2022031442003202

 # HPC Support Ticket Conversation Summary

## Subject: beschränkung tinyGPU nutzung (kennung mppm001h)

### Keywords:
- GPU utilization
- NFS server
- IO rate
- Singularity container
- Job limits
- Network traffic
- Data transfer
- Temporary directory ($TMPDIR)
- Training neural networks
- Image data

### General Learnings:
- **GPU Utilization**: Jobs with 0 GPU utilization were terminated.
- **NFS Server**: Frequent access to the NFS server can negatively impact performance.
- **IO Rate**: Shared resources like IO and network can cause bottlenecks.
- **Job Limits**: Limits on the number of concurrent jobs can be imposed to protect infrastructure.
- **Data Transfer**: Large data transfers can be optimized using tools like `mpifileutils`.
- **Temporary Directory**: Using $TMPDIR for temporary data can reduce IO load.
- **Network Traffic**: Monitoring network traffic is crucial for optimizing job performance.
- **Container Usage**: Singularity containers can be used, but their size and impact on network should be considered.

### Root Causes:
- **GPU Utilization**: Jobs were not utilizing the GPU, leading to termination.
- **NFS Server**: Frequent access to the NFS server caused performance issues.
- **IO Rate**: High IO rate due to frequent data access.
- **Job Limits**: Too many short jobs caused network congestion.
- **Data Transfer**: Large data transfers were slow and impacted job performance.

### Solutions:
- **GPU Utilization**: Check and fix code to ensure GPU utilization.
- **NFS Server**: Reduce frequent access to the NFS server by optimizing data access patterns.
- **IO Rate**: Use $TMPDIR for temporary data to reduce IO load.
- **Job Limits**: Consolidate short jobs into larger ones to reduce network congestion.
- **Data Transfer**: Use tools like `mpifileutils` to optimize data transfer.
- **Network Traffic**: Monitor network traffic to optimize job performance.
- **Container Usage**: Consider the size and impact of Singularity containers on network performance.

### Detailed Conversation Summary:

#### Initial Issue:
- User's jobs were terminated due to 0 GPU utilization.
- Frequent access to the NFS server caused performance issues.

#### Admin Response:
- HPC Admin terminated jobs with 0 GPU utilization.
- Suggested checking the HPC-Cafe material for optimizing NFS server access.

#### User's Data Transfer Issue:
- User had large image data (350GB) and faced slow transfer rates between $WORK and $TMPDIR.
- Transferring data at the start of each job was inefficient.

#### Admin Suggestions:
- Use `mpifileutils` for faster data transfer.
- Consider using $TMPDIR for temporary data to reduce IO load.
- Consolidate short jobs into larger ones to reduce network congestion.

#### Job Limits:
- A limit of 12 concurrent jobs was imposed due to network congestion caused by too many short jobs.
- User was advised to consolidate jobs and avoid frequent data transfers.

#### Network Traffic:
- User inquired about tools to monitor network traffic on the node.
- Admin suggested optimizing data access patterns to reduce network load.

#### Container Usage:
- User was advised to consider the size and impact of Singularity containers on network performance.
- Admin suggested a one-time installation of the software stack to avoid repeated installations.

#### Final Resolution:
- User agreed to consolidate jobs and optimize data access patterns.
- Admin removed the personal job limit but imposed a global limit for all users.
- User was advised to monitor network traffic and optimize job performance accordingly.

This summary provides a concise overview of the issues faced, the root causes, and the solutions implemented. It can serve as a reference for support employees to address similar issues in the future.
---

### 2020122142000081_emmy%20access%20issue.md
# Ticket 2020122142000081

 # HPC Support Ticket: Emmy Access Issue

## Keywords
- Access issue
- Emmy
- cshpc server
- NFS mount
- Storage

## Problem Description
- User unable to access Emmy after logging into the cshpc server.
- Emmy not activated on the cshpc server.

## Root Cause
- Hanging NFS mount `/proj/ftp`.
- The ftp server currently lacks local storage, preventing it from providing NFS exports temporarily.

## Solution
- The issue is related to the NFS mount.
- The ftp server needs to have local storage available to provide NFS exports.

## Lessons Learned
- Ensure that the ftp server has local storage available for NFS exports.
- Monitor NFS mounts to prevent hanging issues.
- Verify server configurations and dependencies when troubleshooting access issues.

## Next Steps
- Check the status of the ftp server's local storage.
- Resolve any issues with the NFS mount.
- Confirm that Emmy is activated on the cshpc server.
---

### 2023031442001775_Issue%20with%20_home_woody%3A%20slow%20%28non%20existent%29%20download%20and%20slow%20response%20tim.md
# Ticket 2023031442001775

 # HPC Support Ticket: Slow Response Time and Download Issues

## Keywords
- Slow response time
- Slow download
- `rsync`
- NFS server issues
- `/home/woody`
- `ls` command delay

## Problem Description
- User experienced slow response times when navigating directories (e.g., using `ls`) within `/home/woody`.
- User encountered slow or non-existent download speeds when using `rsync` to transfer data from `/home/woody`.

## Root Cause
- Issues with the NFS servers behind `/home/woody`.

## Solution
- HPC Admins acknowledged the issue with the NFS servers and expected it to be resolved soon.

## Lessons Learned
- NFS server issues can cause significant delays in file operations and data transfers.
- Users should be informed about ongoing issues through the website or SSH login notices.

## Next Steps
- Monitor NFS server health to prevent similar issues.
- Improve communication channels to notify users of ongoing maintenance or issues.

---

This documentation can be used to diagnose and address similar issues in the future.
---

### 2018100942001352_Fwd%3A%20PBS%20JOB%20992511.eadm.md
# Ticket 2018100942001352

 ```markdown
# HPC Support Ticket: PBS JOB 992511.eadm

## Keywords
- PBS Job
- Torque
- STAR-CCM+
- Node issue
- Job hang
- NFS crash
- dmesg logs
- Job priority
- runjob -x

## Summary
A user reported an issue with a PBS job (992511.eadm) that was not starting on node e1131. The job was stuck during the prologue phase, specifically after clearing buffers and caches. The user also mentioned a STAR-CCM+ process that could not be killed on the node.

## Root Cause
- The job was not starting due to a higher priority job running on the node.
- The node had issues indicated by NFS crash messages in the dmesg logs.

## Solution
- The user attempted to force the job to run using `runjob -x`, which caused the issue.
- The node was scheduled for a reboot due to updates, which would likely resolve the NFS-related issues.

## Lessons Learned
- Users should boost the priority of their jobs instead of using `runjob -x` to avoid such issues.
- Regularly check dmesg logs for any indications of node issues, such as NFS crashes.
- Ensure nodes are rebooted as scheduled to apply updates and resolve any underlying issues.
```
---

### 2024110542004307_Unable%20to%20access%20folder.md
# Ticket 2024110542004307

 ```markdown
# HPC Support Ticket: Unable to Access Folder

## Keywords
- Access Issue
- NFS4_ACL
- Temporary Error

## Summary
A user reported being unable to access a directory that was previously available. The HPC Admin confirmed the user had the necessary permissions but requested more details about the failing command and error message. The user later reported that the issue resolved itself.

## Root Cause
- **Temporary Error**: The issue was likely due to a temporary glitch or network issue.

## Solution
- **Wait and Retry**: The user was able to access the folder after some time, indicating that the issue resolved itself without any specific action from the support team.

## Lessons Learned
- **Temporary Issues**: Sometimes, access issues can be temporary and may resolve on their own.
- **Permissions Check**: Always verify user permissions to rule out access control issues.
- **Error Details**: Requesting specific error details can help in diagnosing the problem more effectively.

## Actions Taken
- **Permissions Verification**: The HPC Admin confirmed that the user had the necessary NFS4_ACL permissions.
- **Error Details Request**: The HPC Admin requested the failing command and error message for further diagnosis.

## Conclusion
The issue was temporary and resolved itself without any specific intervention. Always consider the possibility of temporary glitches when troubleshooting access issues.
```
---

### 42222271_Problem%20deleting%20directory%20_file.md
# Ticket 42222271

 # HPC Support Ticket: Problem Deleting Directory

## Keywords
- Directory deletion
- `rm` command
- Device or resource busy
- NFS filesystem

## Summary
A user encountered issues while attempting to delete a directory (`/home/vault/iwst/iwst139/xd`) using the `rm -r` command. The error messages indicated that the directory contained files that were marked as "Device or resource busy."

## Root Cause
The error messages suggest that the files in the directory are being used by another process or are locked by the NFS filesystem. This is a common issue with NFS-mounted directories.

## Solution
1. **Identify Active Processes**: Check if any processes are using the files in the directory.
   ```bash
   lsof +D /home/vault/iwst/iwst139/xd
   ```
2. **Terminate Active Processes**: If any processes are found, terminate them if possible.
   ```bash
   kill <PID>
   ```
3. **Retry Deletion**: Attempt to delete the directory again after ensuring no processes are using the files.
   ```bash
   rm -r /home/vault/iwst/iwst139/xd
   ```
4. **Contact HPC Admin**: If the issue persists, contact the HPC Admin team for further assistance, as it might require administrative intervention.

## General Learning
- **NFS Issues**: Understand that NFS filesystems can cause "Device or resource busy" errors due to file locks or active processes.
- **Process Management**: Learn to identify and manage processes that might be using files in a directory.
- **Admin Intervention**: Recognize when administrative intervention is necessary to resolve filesystem issues.

## Next Steps
- **Documentation**: Update internal documentation to include common NFS-related issues and their solutions.
- **Training**: Conduct training sessions on handling NFS filesystem errors and process management.

---

This report provides a concise summary of the issue, its root cause, and the steps taken to resolve it. It also includes general learning points and next steps for improving support processes.
---

### 2018112242003225_VASP-Job%20335879%20auf%20Meggie%20_%20bctc39.md
# Ticket 2018112242003225

 ```markdown
# HPC Support Ticket Analysis: VASP Job Performance Issues

## Keywords
- VASP Job
- Performance Issues
- Flop Rates
- Memory Bandwidth
- IO Bottleneck
- NFS
- Ethernet Data Stream

## Summary
A VASP job (ID: 335879) on the HPC system "Meggie" experienced significant performance fluctuations over a 6-hour period. The HPC Admin observed variations in flop rates and memory bandwidth, suggesting potential IO bottlenecks.

## Root Cause
- **IO Bottleneck**: The job's performance was likely hindered by IO operations, as indicated by a continuous Ethernet data stream from all involved nodes.

## Questions for User
1. **Iteration Times**: Did the VASP output show significantly longer iteration times during the performance fluctuations?
2. **IO Operations**: How much IO did VASP perform during this period, and to which file system?

## HPC Admin's Observations
- The monitoring system showed a constant Ethernet data stream, suggesting NFS usage.
- The job's performance issues were likely due to IO operations slowing down the computation.

## Solution
- No solution was provided as the ticket was closed due to no response from the user.

## Lessons Learned
- Performance issues in VASP jobs can be caused by IO bottlenecks.
- Monitoring tools can help identify performance fluctuations and potential causes.
- Users should be aware of the IO demands of their jobs and the impact on performance.

## Next Steps
- If similar issues arise, check for IO bottlenecks and advise users to optimize their job's IO operations.
- Ensure users are aware of the impact of IO on job performance and provide guidance on best practices.
```
---

### 2021042042002335_ssh%20auf%20woodycap%20frontend%20nicht%20m%C3%83%C2%B6glich.md
# Ticket 2021042042002335

 ```markdown
# HPC Support Ticket: SSH Login Issue on Woodycap Frontend

## Keywords
- SSH login issue
- Woodycap frontend
- NFS service
- Force-umount
- Downtime

## Problem Description
The user was unable to log in to the Woodycap frontend using the SSH command from the cshpc-Dialogserver. The SSH command would hang without prompting for a password, and the user could only abort the command with `Ctrl+C`. The issue persisted across different virtual desktops and after reinstalling NoMachine.

## Root Cause
The root cause of the problem was likely related to an NFS service issue. The NFS service on `fundusc2` had failed without any apparent reason in the logs, and the NFS client on the Woodycap machine might have been stuck, possibly due to an attempted login during a downtime period.

## Solution
The HPC Admin force-umounted the directory and remounted it, which resolved the issue. The user was able to log in to both Woodycap frontends (woodycap3 and woodycap4) without any further problems.

## Lessons Learned
- NFS service failures can cause SSH login issues.
- Force-umounting and remounting the directory can resolve NFS-related issues.
- Attempting to log in during a downtime period can lead to a "half-dead" directory state.

## Actions Taken
- The HPC Admin force-umounted the directory.
- The directory was remounted, resolving the SSH login issue.
```
---

### 2020060142000602_Kein%20Zugriff.md
# Ticket 2020060142000602

 # HPC Support Ticket: Kein Zugriff

## Keywords
- Cluster access issue
- NFS server overload
- Temporary outage
- User communication

## Problem Description
- User unable to execute commands after logging into the cluster.
- No error messages displayed.
- User could log in but the system did not respond to any commands, including "exit".

## Root Cause
- Temporary overload on one of the NFS servers between 09:45 and 13:45.

## Solution
- The issue was resolved by addressing the overload on the NFS server.
- The login functionality was restored.

## Lessons Learned
- Always communicate with the HPC team using the official FAU.de email address.
- Temporary overloads on NFS servers can cause the cluster to become unresponsive.
- Regular monitoring and maintenance of NFS servers are crucial to prevent such issues.

## Recommendations
- Ensure that users are aware of the importance of using official email addresses for communication.
- Implement monitoring tools to detect and address NFS server overloads promptly.
- Provide users with information on how to check the status of the cluster and report issues effectively.
---

### 2024021642002887_rsync%20processes%20killed%20dze%20to%20high%20load%20on%20NFS%20server%20-%20b105dc16.md
# Ticket 2024021642002887

 # HPC Support Ticket: rsync Processes Killed Due to High Load on NFS Server

## Keywords
- rsync
- NFS server
- High load
- Process management
- FAU
- NHR@FAU

## Issue
Multiple rsync processes (8 in total) were causing significant load on the NFS servers.

## Root Cause
The user launched multiple rsync processes simultaneously, leading to excessive load on the NFS servers.

## Solution
- **Immediate Action**: The HPC Admin killed the 8 rsync processes to reduce the load on the NFS servers.
- **Preventive Measure**: The user was advised to launch only one rsync process at a time to avoid overloading the NFS servers in the future.

## Lessons Learned
- Running multiple rsync processes concurrently can cause significant load on NFS servers.
- Users should be informed about the potential impact of running multiple I/O-intensive processes simultaneously.
- Proper process management and resource allocation are crucial for maintaining system stability and performance.

## Recommendations
- Educate users on best practices for using I/O-intensive tools like rsync.
- Monitor system load and be prepared to take action if necessary to prevent system overload.
- Consider implementing policies or guidelines for users regarding the number of concurrent processes they can run.
---

### 2023091142003259_Access%20Issue%20for%20EmpkinS%20Directory.md
# Ticket 2023091142003259

 ```markdown
# Access Issue for EmpkinS Directory

## Keywords
- Access Issue
- nfs4_setfacl
- Command Not Found
- Permissions
- chmod

## Problem Description
The user encountered an issue while attempting to grant access to a directory using the `nfs4_setfacl` command. The error message was "-bash: nfs4_setfacl: command not found."

## Root Cause
The `nfs4_setfacl` command was not available on the login server the user was using.

## Solution
1. **Check Login Server**: Ensure the correct login server is being used where the `nfs4_setfacl` command is available.
2. **Alternative Permission Setting**: Use `chmod` commands to set permissions manually if `nfs4_setfacl` is not available.

### Steps to Set Permissions with `chmod`
1. **Remove Group and Others Permissions**:
   ```bash
   find . -type f -name '*' -exec chmod go-rwx {} \;
   find . -type d -name '*' -exec chmod go-rwx {} \;
   ```
2. **Create a Directory and Share Files**:
   ```bash
   mkdir shared_directory
   cp files_to_share shared_directory/
   ```
3. **Set Permissions for the Directory and Files**:
   ```bash
   chmod g+rx shared_directory
   chmod g+r shared_directory/*
   ```

## Resolution
The user managed to resolve the issue by retrying the command on the correct login server. The problem seemed to resolve itself without further intervention.

## Notes
- Always verify the availability of commands on the specific login server being used.
- Use `chmod` as an alternative for setting file and directory permissions if `nfs4_setfacl` is not available.
```
---

### 2020060142000559_Terminal%20prompt%20missing%20after%20login%20to%20woody.md
# Ticket 2020060142000559

 # HPC Support Ticket: Terminal Prompt Missing After Login to Woody

## Keywords
- Terminal prompt missing
- Login issue
- Woody cluster
- NFS file server
- Hanging processes

## Problem Description
A user reported being able to log in to the Woody cluster but not receiving the terminal prompt. The last message displayed was the login timestamp.

## Root Cause
The issue was caused by problems with one NFS file server, which led to hanging login processes.

## Timeline
- **2020-06-01 12:32**: User reported the issue.
- **2020-06-01 14:17**: HPC Admin responded, indicating issues with an NFS file server between 09:45 and 13:45.

## Solution
The issue was resolved automatically once the NFS file server problems were addressed. No specific action was required from the user's side.

## Lessons Learned
- NFS file server issues can cause login processes to hang, resulting in a missing terminal prompt.
- Monitoring and maintaining the health of NFS file servers is crucial for smooth HPC operations.

## Future Actions
- Regularly check the status of NFS file servers.
- Implement monitoring to detect and alert on hanging login processes.
- Inform users promptly about any ongoing issues affecting login or other critical services.
---

### 2022051842002309_Probleme%20mit%20nfs4-acls.md
# Ticket 2022051842002309

 # HPC Support Ticket: Probleme mit nfs4-acls

## Problem Description
User reported issues with NFS4 ACLs on the HPC system. Newly created files in directories with set ACLs had no UNIX permissions, not even for the owner. Additionally, existing files were not affected by the new ACLs, leading to inconsistent behavior.

## Root Cause
The root cause of the problem was identified as missing POSIX inheritance rights in the directory `/home/vault/empkins/tpZ`. This resulted in new files not inheriting the correct ACLs and permissions.

## Steps Taken
1. **Initial Check**:
   - User created directories `readfolder` and `writefolder` and checked initial permissions.
   - User set ACLs for another user and observed that new files had no UNIX permissions.

2. **Admin Investigation**:
   - HPC Admin confirmed that the issue was due to missing POSIX inheritance rights.
   - Admin fixed the directory by setting the correct inheritance flags.

3. **Testing**:
   - User tested the fix and confirmed that new files were created with the correct ACLs.
   - User reported that existing files were not affected by the new ACLs.

4. **Further Investigation**:
   - Admin suggested using the `-R` flag for recursive ACL setting, but this resulted in an error due to the current Ubuntu version.
   - Admin mentioned that the recursive option would be available after the upgrade to Ubuntu 22.04.

5. **Additional Requests**:
   - User requested the creation of a new directory `tpD` with the correct inheritance settings.
   - Admin created the directory and confirmed that the inheritance settings were applied.

## Solution
The issue was resolved by setting the correct POSIX inheritance rights in the directory. The recursive setting of ACLs will be possible after the system upgrade to Ubuntu 22.04.

## Future Actions
- Ensure that all directories have the correct POSIX inheritance rights.
- After the system upgrade, use the `-R` flag for recursive ACL setting to apply changes to existing files.

## Keywords
- NFS4 ACLs
- POSIX inheritance
- Recursive ACL setting
- Ubuntu upgrade
- Directory permissions

## References
- [NFS4 Default-ACLs](https://www.uni-koblenz-landau.de/de/koblenz/GHRKO/netzwerk/nfs4/ACLs)
- [Singularity-Ununtu22.04-Image](#)

## Notes
- The issue with recursive ACL setting will be resolved after the system upgrade.
- Ensure that all users are aware of the changes and how to apply ACLs correctly.
---

### 2024020942003381_Job%20stuck%20at%20CG%20status.md
# Ticket 2024020942003381

 ```markdown
# HPC Support Ticket: Job Stuck at CG Status

## Keywords
- Job stuck
- CG status
- NFS issues
- Job cancellation
- Large batch size

## Problem Description
- User mistakenly submitted a job with a large batch size.
- Attempted to cancel the job but it remained stuck at CG status.

## Root Cause
- NFS issues on the HPC system.

## Solution
- The HPC Admin informed the user that there were NFS issues which have been resolved.
- The jobs should have been cleared by the time the issue was addressed.

## Lessons Learned
- NFS issues can cause jobs to get stuck in CG status.
- Users should be aware of system-wide issues that might affect job management.
- Regularly check system status updates for ongoing issues.

## References
- [Outage of HPC services due to file system issues solved](https://hpc.fau.de/2024/02/10/outage-of-hpc-services-due-to-file-system-issues-solved/)
```
---

### 2023010442000922_Sync%20between%20tinyx%20and%20alex.md
# Ticket 2023010442000922

 # HPC-Support Ticket Conversation: Sync between tinyx and alex

## Problem
- User unable to access data and conda environments stored on tinyx from alex account.
- Need to set permissions to allow access between accounts on different systems.

## Root Cause
- Network filesystems used instead of local storage on tinyx and alex.
- Incorrect use of `nfs4_setfacl` command leading to permission issues.

## Solution
### Setting Permissions
1. **Using `nfs4_setfacl`:**
   ```bash
   $ nfs4_setfacl -a A:df:b143dc15@rrze.uni-erlangen.de:RWX iwbi005h
   ```
   - This command sets read, write, and execute permissions for the specified user.

2. **Recursive Permissions:**
   ```bash
   $ nfs4_setfacl --recursive -a A:df:b143dc15@rrze.uni-erlangen.de:RWX iwbi005h
   ```
   - Note: tinyx does not support `--recursive`. Use woody.nhr.fau.de instead.

### Fixing Permission Issues
1. **Check ACLs:**
   ```bash
   $ nfs4_getfacl /home/woody/iwbi/iwbi005h
   ```
   - Identify and remove deny (`D`) entries.

2. **Edit and Apply ACLs:**
   ```bash
   $ nfs4_getfacl /home/woody/iwbi/iwbi005h > nfs4acl.txt
   ```
   - Edit `nfs4acl.txt` to remove deny entries.
   ```bash
   $ nfs4_setfacl -S nfs4acl.txt /home/woody/iwbi/iwbi005h
   ```

### Conda Configuration
1. **Set Conda Environments and Packages Directories:**
   ```bash
   conda config --append envs_dirs /path/to/envs
   conda config --append pkgs_dirs /path/to/pkgs
   ```
   - Verify configuration with `conda info`.

## Additional Notes
- **Umask Check:**
  ```bash
  $ umask
  ```
  - Ensure `umask` is set correctly to avoid permission issues with newly created files.

- **Avoid Incorrect Commands:**
  ```bash
  $ nfs4_getfacl <file> | nfs4_setfacl -X - <file>
  ```
  - This command can result in no access to the directory.

## Conclusion
- Proper use of `nfs4_setfacl` and correct configuration of conda environments can resolve access issues between tinyx and alex accounts.
- Always verify ACLs and permissions to ensure correct access settings.
---

### 2018030742001495_How%20to%20connect%20to%20NFS%20server%20of%20the%20HPC%20clusters%3F.md
# Ticket 2018030742001495

 # HPC Support Ticket: Connecting to NFS Server of HPC Clusters

## Keywords
- NFS Server
- HPC Clusters
- Mounting Home Directory
- Yast2 Interface
- Connection Issues
- Port 111

## Problem Description
- User is attempting to mount their HPC home directory (`/home/hpc/bccc/bccc009h`) to a local folder on their PC (`ccc236`) using `emmy2.rrze.uni-erlangen.de` as an NFS server.
- The connection to port 111 is open, but the user is unable to connect.
- The user is using the Yast2 interface to configure their NFS client and mount it to a local directory.

## Root Cause
- The exact root cause is not explicitly identified in the conversation.

## Solution
- The ticket was forwarded to the HPC group for further assistance.
- No specific solution was provided in the conversation.

## General Learnings
- Users may encounter issues when attempting to mount HPC directories to local machines via NFS.
- The Yast2 interface is a common tool for configuring NFS clients.
- Port 111 is used for NFS connections.
- Forwarding tickets to the appropriate group (HPC group in this case) is essential for specialized support.

## Next Steps
- The HPC group should investigate the issue further to identify the root cause and provide a solution.
- Ensure that the user has the correct permissions and configurations for NFS mounting.
- Verify network connectivity and firewall settings that might affect NFS connections.
---

### 2023031442002407_%C3%83%C2%84nderung%20BigDataShare-Zugriff.md
# Ticket 2023031442002407

 # HPC Support Ticket: Änderung BigDataShare-Zugriff

## Keywords
- NFSv3
- IP-Adressen
- Zugriffsberechtigung
- Speichersysteme
- Export
- Zertifikat

## Problem
- User requested a change in registered IP addresses for accessing the NFSv3 storage area.
- Specific IP addresses needed to be added and others retained.

## Root Cause
- The user needed to update the list of authorized IP addresses for accessing the NFSv3 storage.

## Solution
- The HPC Admin updated the export configuration to include only the specified IP addresses.
- The admin confirmed that access is now restricted to the four specified IP addresses.

## Lessons Learned
- Ensure that the export configuration is updated promptly to reflect changes in authorized IP addresses.
- Verify that only the specified IP addresses have access to the storage area.
- Be aware of potential issues with expired certificates that may delay the resolution of such requests.

## Actions Taken
- The HPC Admin adjusted the export configuration to include the new IP addresses.
- The admin confirmed the change and ensured that only the specified IP addresses have access.

## Follow-up
- No further action is required from the user.
- The HPC Admin should monitor the storage access to ensure compliance with the updated configuration.

## Additional Notes
- The ticket was initially delayed due to an expired certificate.
- The HPC Admin confirmed the successful update of the export configuration.
---

### 2022021742000471_job%2031602%20running%20on%20a0222.md
# Ticket 2022021742000471

 ```markdown
# HPC Support Ticket: Job Producing High Network Traffic

## Summary
A user's job was producing a lot of network traffic due to frequent writing to NFS directories. The job involved reading and overwriting files for ensemble averages in statistical analysis.

## Keywords
- Network Traffic
- NFS
- Local Disk
- RAMdisk
- rsync
- cp
- Bandwidth
- Overwriting Files
- Ensemble Averages

## Problem
- The job was writing frequently to NFS directories, causing high network traffic.
- The user needed to read and overwrite files for ensemble averages in statistical analysis.
- The job was overwriting files in two directories frequently.

## Root Cause
- The user's job was writing to NFS directories frequently, causing high network traffic.
- The user was overwriting files in two directories frequently to save disk storage.

## Solution
- The user was advised to move the writing to the local disk of the compute node.
- The user was advised to use `/dev/shm` (RAMdisk) instead of NFS directories.
- The user was advised to use `rsync` without the `-z` option to improve bandwidth.
- The user was advised to use `cp` instead of `rsync` to see if the bandwidth improves.

## Lessons Learned
- Frequent writing to NFS directories can cause high network traffic.
- Using the local disk of the compute node can reduce network traffic.
- Using `/dev/shm` (RAMdisk) can improve performance.
- The `-z` option in `rsync` can reduce bandwidth.
- Using `cp` instead of `rsync` can improve bandwidth.
```
---

### 2022022642000257_verbose-flag%20bei%20Gromacs%20%5Bbcpc000h%5D.md
# Ticket 2022022642000257

 ```markdown
# HPC Support Ticket: Verbose Flag Issue with Gromacs

## Keywords
- Gromacs
- Verbose Flag
- NFS Server
- GPU Utilization
- Network Performance

## Problem Description
- **Root Cause**: The use of the verbose flag `-v` in Gromacs jobs was causing unnecessary data to be written over the network, leading to performance issues when the NFS server experienced load problems.
- **Symptoms**: Intermittent slowdowns in GPU utilization, correlating with NFS server load spikes.

## Solution
- **Action Taken**: The user was advised to remove the verbose flag `-v` from their Gromacs jobs to reduce network dependency and improve performance.
- **Outcome**: The user confirmed the removal of the verbose flag from their submit scripts, resolving the issue.

## General Learnings
- **Network Dependency**: High network traffic due to verbose logging can slow down jobs, especially when the NFS server is under load.
- **Optimization**: Removing unnecessary verbose flags can significantly improve job performance by reducing network dependency.
- **Monitoring**: Regular monitoring of GPU utilization and correlation with NFS server load can help identify performance bottlenecks.

## Ticket Status
- **Resolution**: The ticket was closed after the user followed the advice and removed the verbose flag.
```
---

### 2023060242001587_Samba%20versus%20NFS.md
# Ticket 2023060242001587

 # HPC-Support Ticket: Samba versus NFS

## Keywords
- Samba
- NFS
- Performance
- Network File System
- Windows Clients
- Linux Clients
- MacOS Clients
- Benchmarks
- Filesystem
- Machine Learning
- Rechenzentrum

## Summary
The user from the Max-Planck-Institut für die Physik des Lichts (MPL) is experiencing slow access to their network drive, which is currently using Samba. They are considering switching to NFS based on initial benchmarks showing significant performance improvements. The user seeks advice on the performance of Samba versus NFS, the best protocol for their multi-OS environment, and the possibility of integrating with a larger data center.

## Root Cause
- Slow access to the network drive using Samba.
- Suspected performance issues with Samba.

## HPC Admin Response
1. **Performance of Samba and NFS:**
   - Samba's performance is generally good, especially with Windows clients.
   - NFS is faster with current Linux clients over fast, low-latency networks but may not be suitable for Windows.
   - NFS on Windows is challenging and might not be a viable alternative.

2. **Recommended Protocol:**
   - Given the mix of Windows, MacOS, and Linux clients, Samba remains the best option.
   - Suggests checking for misconfigurations or outdated tuning settings on the Samba server.
   - Emphasizes the importance of the underlying filesystem (e.g., XFS for many small files).

3. **Integration with Rechenzentrum:**
   - The likelihood of MPL integrating with the Rechenzentrum is low due to political reasons.
   - MPL is not within the regular service area of the RRZE or NHR and operates its own data centers.

## Solution
- Optimize the existing Samba configuration.
- Ensure the underlying filesystem is appropriate for the data access patterns.
- Consider the impact of machine learning workloads on the filesystem.

## General Learnings
- Samba is a robust choice for multi-OS environments.
- NFS is faster for Linux clients but may not be practical for Windows.
- Proper configuration and filesystem choice are crucial for performance.
- Integration with larger data centers may be limited by political and operational factors.

## Next Steps
- Review and optimize the Samba server configuration.
- Evaluate the filesystem for performance with the specific data access patterns.
- Consider the impact of machine learning workloads on the network drive performance.
---

### 2022110442000405_Daten%20von%20anderen%20Uni%20Rechnern%20laden%20anstatt%20von%20Woodyhome.md
# Ticket 2022110442000405

 # HPC Support Ticket: Loading Data from External University Computers

## Keywords
- NFS Server Overload
- SSH Connection
- Data Transfer
- RAM/SSD Loading
- Compilation Process
- Machine Learning

## Summary
- **Issue**: NFS servers are overloaded, causing performance issues.
- **User Suggestion**: Use SSH to transfer data from external university computers to HPC nodes.
- **Admin Response**: No objection to using SSH, but performance may vary depending on data type and transfer method.

## Detailed Information
- **Root Cause**: Overload on NFS servers due to a large number of small files being opened frequently.
- **User Concern**: Compilation process involving thousands of `.h` files.
- **Admin Feedback**:
  - SSH connection for data transfer is acceptable.
  - Network bandwidth is sufficient (100 GBit).
  - Performance may be slow with many small files (`scp`) or using SSH for large files.
  - HTTP might be more efficient for data transfer.
  - Machine learning tasks that handle many small files continuously can cause significant load.

## Solution
- **Immediate Action**: Reduce load on fileservers by optimizing file usage.
- **Long-term**: Consider alternative data transfer methods like HTTP for better performance.
- **User Follow-up**: Inform colleagues about reducing fileserver load and explore alternative data transfer methods.

## Notes
- Compilation during development days is not a major concern unless done in a continuous loop.
- Machine learning tasks that handle many small files are a common cause of high load on network filesystems.

## Conclusion
- Users can use SSH for data transfer, but should be aware of potential performance issues.
- Optimizing file usage and exploring efficient data transfer methods can help reduce load on NFS servers.
---

### 2023062942002115_Permission%20for%20files%20on%20Tinyx.md
# Ticket 2023062942002115

 # HPC-Support Ticket: Permission for Files on Tinyx

## Summary
User encountered issues with file permissions in `$HPCVAULT` and `$WORK` directories. Files created in `$HPCVAULT` had permissions set to 644 instead of 755, and files in `$WORK` had permissions set to 060.

## Root Cause
- The user's `nfs4_acl` settings were incorrectly configured, causing unexpected file permissions.
- Specifically, the `fdi` entries in the ACL were responsible for the incorrect permissions.

## Solution
1. **Reset ACL Settings**: The HPC Admin reset the user's ACL settings to the default configuration.
   ```bash
   setfacl -b /home/woody/iwbi/iwbi002h
   ```
2. **Verify ACL**: After resetting, the ACL settings should look like:
   ```bash
   nfs4_getfacl /home/woody/iwbi/iwbi002h
   # file: /home/woody/iwbi/iwbi002h
   A::OWNER@:rwaDxtTcCy
   A::GROUP@:tcy
   A::EVERYONE@:tcy
   ```
3. **Use `umask`**: The user was advised to set `umask` in their `.bashrc` file to control default file permissions.
   ```bash
   umask 002
   ```

## Additional Notes
- **File Execution Permissions**: The user was informed about the difference between file permissions for execution (`755`) and read/write (`644`).
  - For scripts that need to be executed, the user can manually set the execute permission using:
    ```bash
    chmod o+x my-script.py
    ```
- **Default Permissions**: The default file creation permission on the system is 644.

## Conclusion
The issue was resolved by resetting the ACL settings and advising the user on how to manage file permissions using `umask`. The user confirmed that the solution worked and they were able to create files with the correct permissions.

---

This documentation can be used to resolve similar permission issues in the future.
---

### 2024032642002919_Bitte%20um%20NFS-Freigabe.md
# Ticket 2024032642002919

 # HPC-Support Ticket: Bitte um NFS-Freigabe

## Keywords
- NFS-Freigabe
- Duplicity
- Duplicati
- Windows-Server
- CIFS
- SFTP
- UID/GID
- Registry Workaround

## Problem
- User möchte NFS-Freigabe für Windows-Server.
- NFS-Mount auf Windows-Server funktioniert nur rudimentär (nur Read-Only Zugriff).
- User fragt nach alternativen Möglichkeiten zur Freigabe/Mount des Laufwerks.

## Lösung
- NFS-Freigabe für die angegebenen IPs wurde erledigt.
- Alternative Möglichkeiten:
  - SFTP-Zugriff auf das freigegebene Verzeichnis.
  - Kontakt zur Windows-Gruppe für CIFS-Speicher.
- Windows-eigene NFS-Implementierung hat in der Vergangenheit nicht reibungslos funktioniert.
- Zusatzsoftware könnte das Problem lösen, aber die Kompatibilität mit Duplicati ist unklar.

## Root Cause
- NFS-Implementierung auf Windows-Servern ist nicht kompatibel mit dem HPC-System.
- UID/GID-Einstellungen in der Registry könnten helfen, aber die genaue Konfiguration ist unklar.

## Weitere Schritte
- User wird die Windows-Gruppe kontaktieren, um eine mögliche Lösung mit CIFS-Speicher zu finden.
- Ticket wird geschlossen.

## HPC Admins
- Johannes Veh

## 2nd Level Support Team
- Lacey
- Dane (fo36fizy)
- Kuckuk
- Sebastian (sisekuck)
- Lange
- Florian (ow86apyf)
- Ernst
- Dominik (te42kyfo)
- Mayr, Martin

## Datacenter Head
- Gerhard Wellein

## Training and Support Group Leader
- Georg Hager

## NHR Rechenzeit Support and Applications for Grants
- Harald Lanig

## Software and Tools Developer
- Jan Eitzinger
- Gruber
---

### 2020021642000136_Woody-Server%20extrem%20langsam%2C%20komisches%20Verhalten.md
# Ticket 2020021642000136

 # HPC Support Ticket: Woody-Server Extremely Slow, Strange Behavior

## Keywords
- Woody-Server
- Slow performance
- Input/output error
- NFS-Client
- Login-Node
- Reboot

## Summary
The user reported that the Woody-Server was experiencing extremely slow performance and strange behavior, including input/output errors when using `sed`. The issue was specifically affecting the login-node.

## Root Cause
The root cause of the problem was identified as an issue with the NFS-Client on the login-node (woody3). The NFS-Client was not functioning correctly, leading to slow performance and input/output errors.

## Solution
The HPC Admins rebooted the login-node (woody3). After the reboot, the performance issues and input/output errors were resolved.

## Lessons Learned
- Performance issues and input/output errors can be caused by problems with the NFS-Client on the login-node.
- Rebooting the affected node can resolve issues related to the NFS-Client.
- It is important to clarify whether the issue is with the login-node or the compute nodes when troubleshooting performance problems.

## Additional Notes
- The user's scripts and jobs were not the cause of the issue, as they had been running without problems for two years.
- The input/output errors were likely caused by multiple `sed` processes generating temporary files with the same name, or by network problems.
- The HPC Admins suggested using local temporary directories (`$TMPDIR`) instead of NFS for temporary files to avoid similar issues in the future.
---

### 2024062742003732_%5BAlex%5D%20NFS%20speed%20Issues%20_%20Working%20directory%20_%20Started%20this%20week.md
# Ticket 2024062742003732

 # HPC Support Ticket: NFS Speed Issues

## Keywords
- NFS speed issues
- Working directory
- Python library import
- VSCode remote
- Frontend nodes
- GPU compute nodes
- High fileserver load

## Problem Description
- User experienced slow NFS access to the working directory.
- Symptoms included slow Python library imports (e.g., PyTorch) and slow file opening in VSCode remote.
- Issue occurred on both frontend nodes and GPU compute nodes.
- Problem was intermittent but recurring at different times of the day.

## Root Cause
- High load on the fileservers due to other users' jobs.

## Solution/Recommendations
- Follow data staging and datasets documentation.
- Encourage colleagues to adhere to the same guidelines to reduce fileserver load.

## Additional Notes
- NFS caches did not significantly improve the speed, suggesting the issue was related to high fileserver load.
- The HPC Admins are investigating the source of the high load and contacting potential users.

## Actions Taken
- HPC Admins acknowledged the issue and provided guidance on data staging and datasets documentation.
- No specific fix was implemented, but the user was advised to follow best practices to mitigate the issue.
---

### 2018121242000316_Ubuntu%2018.04%3A%20%22Permission%20denied%22%20f%C3%83%C2%BCr%20manpages%20auf%20NFS.md
# Ticket 2018121242000316

 # HPC Support Ticket: Ubuntu 18.04 "Permission denied" for manpages on NFS

## Keywords
- Ubuntu 18.04
- NFS
- manpages
- Permission denied
- AppArmor

## Problem Description
- Ubuntu 18.04 systems fail to display manpages located on NFS.
- Error message: `Permission denied` when attempting to access manpages.
- Issue does not occur on Ubuntu 16.04 systems.
- `strace` output shows multiple `EACCES (Permission denied)` errors.

## Root Cause
- The root cause of the problem is suspected to be related to AppArmor, a security module that restricts programs' capabilities with per-program profiles.

## Solution
- The issue is likely an AppArmor configuration problem.
- Verify and adjust AppArmor profiles to allow access to the NFS-mounted manpages.

## Lessons Learned
- AppArmor can cause permission issues on NFS-mounted files.
- Differences in behavior between Ubuntu versions may be due to changes in security configurations.
- `strace` can be useful for diagnosing permission issues but may not always provide a clear solution.

## Next Steps
- Check and modify AppArmor profiles to ensure proper access to NFS-mounted manpages.
- Test the changes on affected systems to confirm resolution.

## References
- AppArmor documentation
- Ubuntu 18.04 security configurations
- NFS mounting and permissions
---

### 2024070842003838_Access%20to%20files%20from%20old%20project.md
# Ticket 2024070842003838

 # HPC Support Ticket: Access to Files from Old Project

## Keywords
- Project accounts
- Directory access
- ACL (Access Control List)
- NFS (Network File System)
- Error resolution

## Summary
A user with two project accounts needed access to old project directories from their new account. The user encountered errors while trying to access the directories.

## Root Cause
- The user required access to old project directories from a new project account.
- Initial attempts to access the directories resulted in errors.

## Steps Taken
1. **User Request**: The user requested access to old project directories from their new account.
2. **Initial Response**: HPC Admin provided a link to documentation on sharing permissions for NFS.
3. **User Error**: The user encountered an error while following the documentation.
4. **Admin Action**: HPC Admin enabled ACL support for the relevant directory.
5. **User Feedback**: The user reported that they still could not access the directories.

## Solution
- **Admin Action**: HPC Admin enabled ACL support for the directory `/home/atuin/v100dd`.
- **User Instruction**: The user was instructed to log out and log back in to apply the changes.

## Outcome
- The user followed the steps but still encountered issues. Further troubleshooting may be required.

## Documentation Reference
- [NFS Share Permissions Documentation](https://doc.nhr.fau.de/data/share-perm-nfs/)

## Notes
- The issue may require additional administrative actions or further investigation into the specific error encountered by the user.
- Ensure that ACL settings are correctly applied and that the user has followed all necessary steps, including logging out and back in.
---

### 2022041242003581_massive%20IO%20of%20beast%20processes%20on%20Woody%20-%20gwpa003h.md
# Ticket 2022041242003581

 ```markdown
# HPC-Support Ticket: Massive IO of BEAST Processes on Woody

## Summary
- **Issue**: Massive IO of BEAST processes causing severe trouble for all users.
- **Root Cause**: Excessive load on the NFS server due to heavy IO operations from multiple jobs.
- **Solution**: Reduce the frequency of intermediate file production and consider using local memory for temporary files.

## Details
- **Initial Report**:
  - Several running jobs were killed due to massive IO causing severe trouble for all users.
  - NFS server for `/home/woody` had excessive load for many hours.
  - User had ~180 jobs running, all stalling in IO.
  - Directory `/home/woody/gwpa/gwpa003h/biogeography/runs/` had ~25k entries with temporary files being created and removed frequently.

- **Admin Actions**:
  - Jobs with the shortest active runtime were deleted to reduce load.
  - Suggested using `$TMPDIR` for temporary files to scale with the number of running jobs.
  - Provided a job script template to copy relevant files to node's local memory (`/dev/shm`).

- **User Response**:
  - User decided to reduce the frequency of intermediate file production (`.state` and `.state.new` files).
  - Ran jobs with reduced logging frequency, which significantly lowered IO traffic.

- **Follow-up**:
  - IO traffic of the current jobs is significantly lower compared to earlier jobs.
  - User confirmed the setup works and will continue with the current configuration.

## Keywords
- IO load
- NFS server
- BEAST processes
- Temporary files
- $TMPDIR
- Job script optimization
- IO throttling

## Lessons Learned
- **IO Load Management**: Reducing the frequency of intermediate file production can significantly lower IO traffic.
- **Temporary File Handling**: Using local memory (`/dev/shm`) or `$TMPDIR` for temporary files can help scale with the number of running jobs.
- **Job Script Optimization**: Providing a template for job scripts can help users optimize their IO operations.

## Conclusion
The issue was resolved by reducing the frequency of intermediate file production and considering the use of local memory for temporary files. This approach significantly lowered IO traffic and improved overall system performance.
```
---

### 2024080942000284_high%20IO%20on%20alex%20%5Bv103fe15%5D.md
# Ticket 2024080942000284

 ```markdown
# HPC Support Ticket: High IO on Alex

## Keywords
- High IO
- Bottlenecking
- NVMe Storage
- Job Optimization
- Data Transfer

## Summary
A user reported high IO issues with a job running on Alex, which was causing a bottleneck in their training process. The fileserver was unable to respond quickly enough, leading to performance degradation.

## Root Cause
- Heavy IO operations on the fileserver were causing delays in job processing.

## Solution
- The HPC Admin suggested copying the data to a faster NVMe storage to alleviate the IO bottleneck.
- Details on accessing NVMe storage were provided via a documentation link.

## Actions Taken
- The user was advised to move their data to NVMe storage.
- The ticket was closed as no further issues were observed after the suggestion.

## Lessons Learned
- High IO operations can significantly impact job performance.
- Utilizing faster storage solutions like NVMe can help mitigate IO bottlenecks.
- Providing clear documentation and guidance on accessing faster storage options is crucial for user support.
```
---

### 2016100842001456_Emmy%20and%20Lima%20clusters%2C%20acces%20and%20job%20scheduler%20problems.md
# Ticket 2016100842001456

 # HPC-Support Ticket: Emmy and Lima Clusters Access and Job Scheduler Problems

## Keywords
- Network problems
- Cluster inaccessibility
- Job termination
- Email alerts
- Epilogue
- NFS servers

## Issue Description
- **Date:** 08/10/2016
- **Time:** Around 12:30-13:00
- **Clusters Affected:** Emmy, LIMA
- **Symptoms:**
  - Terminal sessions stopped responding
  - Head nodes were inaccessible
  - Jobs were killed prematurely without email alerts or epilogue

## Root Cause
- Severe network problems in the university network from approximately 10:30 until 13:30.
- NFS servers could not be reached, affecting the HPC systems.

## Solution
- The network issues were resolved by the university's network administration.
- No specific action was required by the HPC admins for the network issue itself.

## Lessons Learned
- Network instability can cause cluster inaccessibility and job termination without proper alerts.
- Ensure that job scheduling systems are configured to handle network disruptions gracefully.
- Monitor NFS server connectivity as it is critical for cluster operations.

## Follow-up Actions
- Verify that job scheduling systems are configured to send email alerts even in case of unexpected terminations.
- Implement monitoring for NFS server connectivity to detect and respond to network issues promptly.

## References
- HPC Services, Friedrich-Alexander-Universitaet Erlangen-Nuernberg
- Regionales RechenZentrum Erlangen (RRZE)

---

This documentation aims to assist HPC support employees in identifying and resolving similar issues in the future.
---

### 2023050842001729_Login%20auf%20tinyx%20nicht%20m%C3%83%C2%B6glich.md
# Ticket 2023050842001729

 # HPC Support Ticket: Login Issue on tinyx

## Keywords
- SSH connection
- Terminal prompt
- NFS-Client
- Kernel log
- Reboot
- /tmp directory

## Problem Description
- User unable to log in to tinyx.
- SSH connection established but no terminal prompt appears.

## Root Cause
- Possible issue with the NFS-Client on the machine.
- /tmp directory was completely full.

## Solution
- The machine was rebooted.
- Login functionality was restored after the reboot.

## Lessons Learned
- Full /tmp directory can cause login issues.
- Rebooting the machine can resolve issues related to NFS-Client and full /tmp directory.
- Monitoring kernel logs can provide insights into the root cause of login issues.
---

### 2020050642001265_home-Verzeichnisse%20nicht%20erreichbar.md
# Ticket 2020050642001265

 ```markdown
# HPC-Support Ticket: Home Directories Not Accessible

## Keywords
- Home directories
- NFS file servers
- Network component
- Certificate expiration

## Problem Description
The user reported that the home directories (woody, saturn, and vault) were not accessible.

## Root Cause
- **Network Component Issue**: A faulty network component caused one of the NFS file servers to be unreachable, leading to issues on all HPC systems.
- **Certificate Expiration**: There was a mention of an expired certificate, which might have contributed to the issue.

## Solution
- The HPC Admins resolved the issue by fixing the faulty network component.
- All systems were reported to be fully operational again.

## Lessons Learned
- Regularly monitor network components to prevent such issues.
- Ensure certificates are up-to-date to avoid expiration-related problems.
- Quick resolution of network issues can restore system functionality promptly.
```
---

### 2022041442000561_Amberjobs%20auf%20Alex%20schreiben%20zu%20viele%20Daten%20%C3%83%C2%BCber%20Netzwerk%20%5Bmfbi004h%5.md
# Ticket 2022041442000561

 ```markdown
# HPC Support Ticket: High Network Traffic from Amber Jobs

## Keywords
- Amber jobs
- Network traffic
- NFS servers
- Schreibfrequenz (write frequency)
- /dev/shm
- Restart-Datei (restart file)

## Problem Description
- **Root Cause**: Amber jobs were writing data to the network every 3-4 seconds, causing high network traffic.
- **Impact**: This high write frequency was negatively affecting the NFS servers' performance.

## Solution
- **Action Taken by User**: The user stopped the jobs and restarted them with a reduced write frequency.
- **Recommendation by HPC Admin**: If high write frequency is necessary, write data to `/dev/shm` and copy it to the home directory at the end of the simulation. Ensure `/dev/shm` is flushed at job end.

## General Learnings
- High network traffic from frequent writes can impact NFS server performance.
- Use `/dev/shm` for temporary storage to reduce network load.
- Ensure temporary storage is properly managed and flushed at job completion.

## Follow-Up
- Monitor job performance to ensure the issue is resolved.
- Provide further assistance if needed.
```
---

### 2024022242003258_Slow%20alex%20cluster.md
# Ticket 2024022242003258

 # Slow Alex Cluster Issue

## Keywords
- Slow performance
- Alex cluster
- Epoch training time
- GPU allocation
- NFS servers
- Data handling
- Queue waiting time

## Problem Description
- User reports significant slowdown in training time per epoch on the Alex cluster (from 2s to 17s on an A100 GPU).
- Difficulty in allocating nodes, regardless of GPU type or duration.
- Issue observed by multiple users since Monday.

## Root Cause
- Variations in epoch duration suggest dependency on NFS server performance.
- Heavy load on the Alex cluster leading to increased queue waiting times.

## Solution/Recommendations
- Improve data handling to reduce dependency on NFS servers.
- Attend HPC Cafes for guidance on better data management practices.
- Expect longer queue waiting times due to high demand; typical waiting time is 2-3 days on LRZ's system.

## Notes
- No jobs were observed waiting for more than one day in the queue.
- Regular monitoring of cluster load and data handling practices can help mitigate such issues.

## Follow-up Actions
- Users should optimize their data handling processes.
- HPC Admins to continue monitoring cluster load and provide guidance on efficient job submission and data management.
---

### 2022012642000222_psiblast%20on%20Woody%20-%20btr0000h.md
# Ticket 2022012642000222

 # HPC Support Ticket: psiblast on Woody - btr0000h

## Keywords
- psiblast
- Woody
- NFS saturation
- uniref90 dataset
- network performance
- concurrent jobs
- throttling
- memory allocation
- array jobs
- TinyFat

## Problem
- User's concurrent psiblast jobs on Woody saturated the NFS file server, affecting all users.
- Each job read the uniref90.fasta database, causing significant network traffic.
- When ~150 jobs ran concurrently, network performance dropped, and the NFS server's load and response time increased.

## Root Cause
- High I/O demand from concurrent psiblast jobs reading the uniref90 dataset.
- Insufficient understanding of job memory allocation parameters on Woody.

## Solution
- **Throttling**: HPC Admin throttled the number of concurrent jobs to reduce load.
- **Memory Allocation**: Clarified the use of `-l*men=12gb` and suggested using `:any32` property to ensure nodes with sufficient memory.
- **Alternative Job Submission**: User noticed better throughput and less infrastructure impact using array jobs on TinyFat.

## Next Steps
- If more jobs are needed, a Zoom meeting is suggested to optimize performance, especially on TinyFat.

## Lessons Learned
- High I/O jobs can significantly impact the NFS server and network performance.
- Understanding job submission parameters and their effects on resource allocation is crucial.
- Array jobs can provide better throughput and reduce infrastructure load.
- Communication with HPC Admin can help optimize job performance and prevent infrastructure issues.
---

### 2024032742001294_HPC%20Storage%3A%20merkw%C3%83%C2%BCrdiges%20Verhalten.md
# Ticket 2024032742001294

 ```markdown
# HPC Storage: Strange Behavior

## Keywords
- HPC Storage
- File Creation Delay
- NFS Client
- SSH Connection

## Problem Description
- **User Issue**: The user experienced a delay in file creation in a specific directory on the HPC storage. The files were not immediately visible and took minutes to hours to appear.
- **Affected Path**: `/home/vault/empkins/tpA/A01/2023/sensorfusion_static_dataset_annotated/annotated_zipped/77_polystyrene_plate_40_fused/zed/mask/left`
- **Symptoms**: No error messages, commands like `touch` and `mkdir` executed without issues, but files did not appear immediately.

## Troubleshooting Steps
- **HPC Admin**: Unable to reproduce the issue initially.
- **User**: Confirmed the issue persisted in new SSH connections.
- **HPC Admin**: Suggested the problem might be due to a "stuck" NFS client on the machine.

## Root Cause
- The issue was likely caused by a malfunctioning NFS client on the user's machine, leading to delays in file visibility.

## Solution
- **HPC Admin**: Recommended explicitly querying the file/directory (analogous to `.snapshots`) to force an update.
- **Status**: The ticket was closed as the issue was intermittent and likely client-side.

## General Learnings
- Intermittent file creation delays can be caused by NFS client issues.
- Explicitly querying the file/directory can help resolve visibility issues.
- Always check if the problem persists in new SSH connections to rule out session-specific issues.
```
---

### 2021121542001223_Langsames%20arbeiten%20am%20HPC.md
# Ticket 2021121542001223

 ```markdown
# HPC Support Ticket: Slow Performance on HPC

## Keywords
- Slow performance
- MATLAB
- NFS servers
- NoMachine
- Trinity Desktop
- SSH
- High latency
- Top command

## Problem Description
- User experiencing slow performance on HPC, specifically with MATLAB.
- Delays in opening figures and switching between tabs.
- No high CPU usage observed using the `top` command.

## Root Cause
- High load on NFS servers causing latency issues.

## Solution
- Acknowledged by HPC Admins.
- Issue is known and being worked on.
- No immediate solution provided due to the complexity of the problem.

## General Learnings
- High latency issues can be caused by NFS server load.
- The `top` command may not show high CPU usage if the issue is related to network or I/O.
- HPC Admins are aware of the problem and working towards a solution.

## Next Steps
- Monitor NFS server load.
- Continue troubleshooting and implementing solutions to reduce NFS server load.
- Inform users about ongoing efforts to resolve the issue.
```
---

### 2022122342001699_Login%20h%C3%83%C2%A4ngt%20und%20Jobs%20auf%20Alex%20auch.md
# Ticket 2022122342001699

 # HPC Support Ticket Analysis

## Subject: Login hängt und Jobs auf Alex auch

### Keywords:
- Login issue
- Job hang
- NFS server
- Kernel crash
- Mount issue

### Problem Description:
- Users experiencing login issues on both `cshpc` and `alex`.
- Jobs on `alex` are hanging, e.g., job 430128.
- Suspected missing mount for `/home/atuin`.

### Root Cause:
- NFS server for `/home/atuin` crashed multiple times due to kernel crashes.

### Solution:
- NFS server issues were resolved, allowing logins and jobs to proceed.

### Lessons Learned:
- NFS server stability is critical for user logins and job execution.
- Kernel crashes on the NFS server can cause widespread issues.
- Regular monitoring and maintenance of NFS servers are essential to prevent such issues.

### Actions Taken:
- HPC Admins identified and resolved the NFS server crashes.
- Users were informed about the resolution and the system's current stability.

### Follow-up:
- Continue monitoring NFS server stability.
- Implement preventive measures to avoid future kernel crashes.

---

This documentation can be used to diagnose and resolve similar issues in the future.
---

### 2022110242000758_Anpassung%20Dateirechte.md
# Ticket 2022110242000758

 # HPC Support Ticket: Adjusting File Permissions

## Keywords
- File permissions
- NFS4 ACLs
- Recursive ownership change
- Permission inheritance

## Summary
A user requested a change in file ownership for a project directory due to the departure of the previous owner. The new owner encountered issues with NFS4 ACLs after the ownership change.

## Problem
- **Root Cause**: The previous owner (iwso026h) had left the institution, and the new owner (iwhf002h) needed to take over the directory.
- **Issue**: After changing the ownership, NFS4 ACLs were not functioning correctly, preventing users from performing certain actions like saving or deleting files.

## Solution
- **Steps Taken**:
  1. The HPC Admin confirmed the ownership change with the previous owner.
  2. The ownership of the directory was changed recursively.
  3. The user reported issues with NFS4 ACLs not functioning correctly.
  4. The HPC Admin checked the ACLs and found that there were duplicate entries.
  5. The duplicate entry for the user (iwso049h) was removed.

- **Final Resolution**: The HPC Admin advised the user to try again after removing the duplicate ACL entry.

## Lessons Learned
- Always confirm ownership changes with the previous owner.
- Ensure that ACLs are correctly inherited and there are no duplicate entries.
- Recursive ownership changes can affect ACLs, so it's important to verify and adjust them as needed.

## Recommendations
- Document the process for changing ownership and adjusting ACLs.
- Provide guidelines for users on how to check and set ACLs correctly.
- Regularly review and update ACLs to ensure they are functioning as intended.
---

### 2023050942001576_Zugriff%20auf%20%24WORK%20sehr%20langsam.md
# Ticket 2023050942001576

 ```markdown
# HPC-Support Ticket: Slow Read Access to $WORK

## Summary
- **Subject:** Slow read access to $WORK
- **User:** Researcher from Erlangen Centre for Astroparticle Physics (ECAP)
- **Systems Affected:** woody5, tg086

## Problem Description
- Slow read access to files on $WORK (~Mb/s speed measured)

## Diagnostic Steps
- User provided details of the systems where the issue was observed (woody5, tg086)
- User provided command used for testing: `dd if=$WORK/geant4_pmt/30cm_sphere/out_photons_290nm.csv of=/dev/zero bs=8k`

## Root Cause
- High load on the NFS server (load ~50) causing requests to timeout

## Solution
- Restarted the NFS kernel server: `service nfs-kernel-server restart`
- Temporarily resolved the issue

## Additional Information
- User's $WORK directory (/home/saturn) should now have improved IO performance
- User was advised to use /home/wecapstor3/capn for larger data sets, as it has ~100TB of available space

## Keywords
- Slow read access
- $WORK
- NFS server
- High load
- Restart NFS server
- IO performance
- Quota limit
- Data storage recommendation
```
---

### 2021052042000853_Shared%20access%20auf%20titan.md
# Ticket 2021052042000853

 ```markdown
# HPC-Support Ticket: Shared Access auf titan

## Keywords
- Shared access
- NFS4_setfacl
- chmod
- setfacl
- HPC-Kennung
- Verzeichniszugriff

## Problem
- User wants to grant shared access to a specific directory (`/home/titan/sles/sles000h`) for another user (`sles001h`).
- User is unsure about the correct method to use (`nfs4_setfacl`).

## Solution
- **Option 1: Using `chmod`**
  ```bash
  chmod -R g+rX /home/titan/sles/sles000h
  ```
  - This command grants read and execute permissions to all users in the `sles` group.

- **Option 2: Using `setfacl`**
  ```bash
  setfacl --recursive --modify u:sles001h:rX,d:u:sles001h:rX /home/titan/sles/sles000h
  ```
  - This command sets the access control list (ACL) to grant read and execute permissions specifically to `sles001h`.

## General Learning
- Users can grant shared access to directories using either `chmod` for group-level permissions or `setfacl` for more granular control.
- It is important to use the correct command to avoid unintended permission changes.
- HPC Admins can provide guidance on the appropriate method based on the specific requirements.
```
---

### 2024071242001402_Job%20on%20Alex%20cancelled%20due%20to%20NFS%20problems%20%5Bv103fe12%5D.md
# Ticket 2024071242001402

 ```markdown
# HPC-Support Ticket: Job Cancelled Due to NFS Problems

## Subject
Job on Alex cancelled due to NFS problems [v103fe12]

## Keywords
- Job Cancellation
- NFS Problems
- Node Reboot
- Job Resubmission

## Problem Description
A job (jobID 1859048) was cancelled due to NFS problems on the Alex node a0531.

## Root Cause
NFS issues on the Alex node a0531.

## Solution
- The HPC Admin rebooted the affected node (a0531).
- The user was advised to check for any output and resubmit the job.

## Lessons Learned
- NFS problems can cause job cancellations.
- Rebooting the affected node can resolve NFS issues.
- Users should check for job output and resubmit jobs after such incidents.
```
---

### 2021050642001371_reze%20log%20in%20failure.md
# Ticket 2021050642001371

 ```markdown
# HPC Support Ticket: reze log in failure

## Keywords
- SSH login failure
- Connection reset by peer
- NFS issue
- Erlangen cluster

## Problem Description
User encountered an SSH login failure when attempting to access the Erlangen cluster. The error message displayed was:
```
ssh_exchange_identification: read: Connection reset by peer
```

## Root Cause
The issue was caused by a hanging NFS (Network File System) on the cluster. The underlying cause was related to an ongoing ticket with IBM.

## Solution
The HPC Admin team identified and resolved the NFS issue, which restored SSH login functionality.

## Lessons Learned
- SSH login failures with the error "Connection reset by peer" can be indicative of underlying network or file system issues.
- NFS problems can disrupt SSH connections to the cluster.
- Collaboration with external vendors (e.g., IBM) may be necessary to resolve certain issues.

## Actions Taken
1. User reported the SSH login failure.
2. HPC Admin identified the issue as a hanging NFS.
3. The NFS problem was linked to an ongoing ticket with IBM.
4. The issue was resolved, and the user confirmed successful login.

## Follow-up
Ensure that NFS and network health are regularly monitored to prevent similar issues in the future.
```
---

