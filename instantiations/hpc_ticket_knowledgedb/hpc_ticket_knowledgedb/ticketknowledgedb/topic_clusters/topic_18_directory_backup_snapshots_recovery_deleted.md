# Topic 18: directory_backup_snapshots_recovery_deleted

Number of tickets: 68

## Tickets in this topic:

### 2021081142002078__home_woody_bccc_bccc021h_%3A%20Read-only%20file%20system.md
# Ticket 2021081142002078

 # HPC Support Ticket: Read-only File System

## Keywords
- Read-only file system
- Downtime
- Access rights
- RRZE HPC systems

## Problem Description
The user reported that the directory `/home/woody/bccc/bccc021h/` was set to read-only and inquired whether this was due to the downtime of all RRZE HPC systems or other reasons.

## Root Cause
The root cause of the problem was not explicitly stated in the conversation. However, it was implied that the issue might be related to the downtime of the RRZE HPC systems.

## Solution
The HPC Admin suggested that the user should read the announcement for more information.

## Lessons Learned
- **Communication**: Importance of reading announcements and updates from the HPC support team.
- **Troubleshooting**: Checking system announcements and updates can help in understanding the root cause of issues like read-only file systems during downtimes.

## Next Steps
- Users should be directed to read the latest announcements and updates from the HPC support team.
- If the issue persists, further investigation into the file system permissions and downtime procedures may be necessary.
---

### 2023071942001517_Request%20to%20delete%20folder%20in%20Home_%20HPC.md
# Ticket 2023071942001517

 ```markdown
# HPC Support Ticket: Request to Delete Folder in Home Directory

## Keywords
- Folder Deletion
- Large Folder
- Home Directory
- Best Practices
- Shared Filesystems

## Problem
- **Root Cause**: User has a large folder in their home directory that takes a long time to delete.
- **User Request**: Assistance in deleting the folder located at `/home/hpc/iwi5/iwi5088h/New folder/data_512_median_nopatch`.

## Solution
- **Action Taken by HPC Admin**: The folder was successfully deleted by the HPC Admin.
- **Additional Advice**: The HPC Admin provided a link to the best practice guide on shared filesystems to help the user manage large files more efficiently in the future.

## General Learnings
- Deleting a large number of files can be time-consuming.
- Users should refer to best practice guides for managing shared filesystems to optimize their workflow.

## References
- [Best Practice Guide on Shared Filesystems](https://www.fau.tv/clip/id/40199)
```
---

### 2024052242000961_Stale%20file%20handle%20on%20_home_woody_.md
# Ticket 2024052242000961

 ```markdown
# HPC Support Ticket: Stale File Handle on /home/woody/

## Keywords
- Stale file handle
- Directory access issue
- Conda environment
- Woody cluster
- Tinyx cluster

## Problem Description
- User unable to access `/home/woody/` directory on the Woody cluster.
- Error message: `-bash: cd: /home/woody/: Stale file handle`
- Directory accessible on the Tinyx cluster.
- Conda environments and packages stored in the affected directory.

## Root Cause
- Stale file handles on the Woody frontends.

## Solution
- HPC Admins identified and fixed the stale file handles on the Woody frontends.
- User confirmed the directory is accessible again and can use Conda environments.

## Lessons Learned
- Stale file handles can prevent access to directories on HPC clusters.
- Specificity in identifying the affected host is crucial for troubleshooting.
- Quick resolution by HPC Admins ensures minimal disruption to user workflows.

## Actions Taken
- HPC Admins checked and fixed stale file handles on the Woody frontends.
- User confirmed resolution and access to the directory.
```
---

### 2024121742001661_Meggie%20Cluster%20Verbindungsprobleme.md
# Ticket 2024121742001661

 ```markdown
# Meggie Cluster Connection Issues

## Keywords
- Meggie Cluster
- Connection Problems
- File System Issues
- Frontend Nodes

## Summary
A user reported issues connecting to the Meggie Cluster. The HPC Admin was able to log in successfully to both frontend nodes (meggie1 and meggie2), suggesting the problem might be related to occasional file system difficulties.

## Root Cause
- **User Reported Issue:** Unable to connect to the Meggie Cluster.
- **Potential Cause:** Occasional file system issues.

## Solution
- **Admin Action:** Verified successful login to both frontend nodes.
- **Next Steps:** Further investigation into file system issues may be required if the problem persists.

## General Learnings
- **Troubleshooting Steps:** Check frontend node accessibility.
- **Potential Issues:** File system problems can cause intermittent connection issues.
- **Communication:** Inform users about potential file system issues if they report connection problems.
```
---

### 2024032942000282_Can%27t%20enter%20woody%20folder.md
# Ticket 2024032942000282

 ```markdown
# HPC Support Ticket: Can't Enter Woody Folder

## Keywords
- Access issue
- /home/woody
- System failure

## Problem Description
- User unable to access the `/home/woody` directory.

## Ticket Conversation
- **User:** Reports inability to enter `/home/woody` and queries if it is a system failure.
- **HPC Admin:** Requests the system on which the user encountered the issue.

## Root Cause
- The root cause of the problem is not yet identified in the provided conversation.

## Solution
- No solution provided in the conversation. Further investigation is required to determine the cause and resolve the issue.

## General Learnings
- Always specify the system or environment where the issue occurred.
- Initial troubleshooting steps should include verifying permissions and checking system logs.
```
---

### 2016012942001675_Lima%20Fasttemp.md
# Ticket 2016012942001675

 # HPC-Support Ticket: Lima Fasttemp

## Keywords
- Access issues
- /lxfs/nfcc/nfcc02/
- Shell hangs
- Storage-Hakler
- Server reset

## Problem Description
- User reported access issues to `/lxfs/nfcc/nfcc02/`.
- Attempting to `cd` into the directory and running `ls` caused the shell to hang.

## Root Cause
- Serverseitigen Threads were affected by a Storage-Hakler, causing access issues.

## Solution
- HPC Admins reset the affected servers.
- It was noted that it might take some time for the clients to recover, and some clients might remain affected.

## Lessons Learned
- Access issues to specific directories can be caused by server-side problems.
- Resetting the affected servers can resolve the issue, but it may take time for all clients to recover.
- Users should report any persistent issues after the initial fix.

## Follow-up
- If the problem persists after the server reset, users should notify the HPC Admins for further investigation.
---

### 2024052142000364_Woody%20File%20System%20Read%20Only%3F.md
# Ticket 2024052142000364

 # HPC Support Ticket: Woody File System Read Only

## Keywords
- Woody file system
- Read-only file system
- Scheduled downtime
- Maintenance
- HPC systems
- NHR@FAU

## Problem Description
- User reported inability to write to the Woody file system.
- Error message indicated a "Read-only file system."

## Root Cause
- Scheduled downtime and maintenance on the HPC systems, including the Woody file system, which was unavailable for the entire maintenance period.

## Solution
- Inform the user about the ongoing maintenance.
- Advise the user to wait until the maintenance is complete.

## Lessons Learned
- Always check for scheduled maintenance announcements before reporting issues.
- Maintenance periods can affect file system availability.
- Communicate maintenance schedules clearly to users to avoid confusion.

## Additional Information
- The maintenance announcement included details about the downtime and the decommissioning of an old dialog server.
- Users should update their SSH configurations to use the new server.

## Ticket Status
- Closed after informing the user about the maintenance.
---

### 2018100842003111_vault%20aufr%C3%83%C2%A4umen.md
# Ticket 2018100842003111

 ```markdown
# HPC-Support Ticket: vault aufräumen

## Keywords
- Vault cleanup
- Directory deletion
- Relics from old systems

## Summary
A user requested the deletion of two directories from the `/vault` storage, which were identified as relics from older systems (woodycap1/2 under SL).

## Root Cause
- The directories `/home/vault/caph/shared/sw/develold_tobedeleted` and `/home/vault/caph/shared/sw/stable_tobedeleted` were no longer needed and were remnants from older systems.

## Solution
- The HPC Admins were requested to delete the specified directories.

## General Learnings
- Users may request the deletion of old or unused directories to free up space and keep the storage organized.
- It is important to verify the necessity of deletion requests to avoid accidental data loss.
```
---

### 2020071442002254_Backup.md
# Ticket 2020071442002254

 # HPC Support Ticket: Backup

## Keywords
- Backup
- Data Recovery
- File Deletion
- HPC Account
- Dateisysteme

## Summary
A user accidentally deleted two files from their HPC account and inquired about the possibility of recovering them.

## Root Cause
- User deleted files while copying data to a local machine.
- Files were located on the server `woody` under the path `/home/woody/bccb/bccb006h/work/2019-nCoV/Production/nCoV_1_S230_Second_Run/CoV_1_S230_I/`.
- Files deleted: `production_pullf.xvg` and `production_pullx.xvg`.

## Solution
- The ability to recover files depends on the specific file system where the files were located.
- If the files were on a system with backup capabilities, the user might be able to recover them independently.
- HPC Admins provided guidance on the potential recovery process based on the file system.

## General Learnings
- Always confirm the location of files before deletion.
- Understand the backup policies and capabilities of different file systems on the HPC.
- Communicate the exact path and file names when requesting data recovery.

## Next Steps
- If a similar issue arises, determine the file system where the files were located.
- Provide users with instructions on how to access backups if available.
- If self-recovery is not possible, escalate to HPC Admins for further assistance.
---

### 2021102542000183_stale%20file%20handle%20on%20WORK.md
# Ticket 2021102542000183

 # HPC Support Ticket: Stale File Handle on WORK

## Keywords
- Stale file handle
- $WORK folder
- Server crash
- /home/woody
- /apps

## Problem Description
- User encountered "stale file handle" errors when accessing the `$WORK` folder (`/home/woody/iwal/iwal060h`) on the HPC.
- Issue started around 2:20 AM.

## Root Cause
- The server for `/home/woody` and `/apps` for Woody & Tiny* crashed.

## Solution
- HPC Admins worked on resolving the server crash.
- Systems were brought back into operation.

## Actions Taken
- HPC Admins acknowledged the server crash and worked on resolving it.
- User was informed about the server crash and the resolution process.
- User was advised to report any further issues.

## Lessons Learned
- Server crashes can cause "stale file handle" errors.
- Prompt communication with users about system issues is crucial.
- Regular monitoring and maintenance of servers can help prevent such issues.

## Follow-Up
- If the user encounters further problems, they should report them to the HPC support team.

## Documentation for Future Reference
- **Symptom:** Stale file handle errors when accessing specific folders.
- **Potential Cause:** Server crash affecting the relevant directories.
- **Resolution:** Restart and restore the affected servers.
- **Next Steps:** Monitor server health and respond to user reports promptly.
---

### 2023070942000779_Clusterprobleme%3F%20Komme%20nicht%20mehr%20auf%20%24WORK.md
# Ticket 2023070942000779

 ```markdown
# HPC Support Ticket: Cluster Issues - Unable to Access $WORK

## Keywords
- Cluster problems
- Alexcluster
- $WORK access
- Job start issues
- Fileset-Mounts
- Login nodes
- Compute nodes
- Certificate expiration

## Problem Description
- User reported issues with accessing $WORK and starting jobs on the Alexcluster.

## Root Cause
- Different fileset-mounts from atuin were hanging on the Alex-Loginknoten.

## Troubleshooting Steps
- HPC Admin ran a `df` command on the Alex-Login and Alex-Computenodes, which completed successfully.
- The cause and resolution of the issue were unclear to the HPC Admin.

## Solution
- The issue seemed to resolve itself, as the fileset-mounts were functioning again.

## Lessons Learned
- Regular monitoring of fileset-mounts and certificates is crucial.
- Unexplained issues may resolve spontaneously, but understanding the root cause is important for future prevention.

## Next Steps
- Continue monitoring the cluster for similar issues.
- Investigate the root cause of the fileset-mount hangs to prevent future occurrences.
```
---

### 42284692_Can%20not%20access%20to%20my%20home%20directory.md
# Ticket 42284692

 # HPC Support Ticket: Cannot Access Home Directory

## Keywords
- Home directory access
- Permission denied
- Verzeichnisdienst (directory service)
- Fileserver access

## Summary
- **User Issue**: Unable to access home directory on HPC cluster "emmy". Error messages indicate permission issues.
- **Root Cause**: Problem with a central directory service affecting access to fileservers.
- **Solution**: Issue is known and being addressed by the HPC team.

## Detailed Information
- **User Report**:
  - Unable to access home directory.
  - Error messages:
    ```
    Could not chdir to home directory /home/hpc/mptf/mptf21: Permission denied
    -bash: /home/hpc/mptf/mptf21/.bash_profile: Permission denied
    ```
- **HPC Admin Response**:
  - Acknowledged a problem with a central directory service.
  - Many systems and cluster nodes are affected.
  - Issue is being worked on and expected to be resolved soon.

## Lessons Learned
- **Communication**: Ensure users are informed about ongoing issues through HPC bulletins or other communication channels.
- **Troubleshooting**: Permission denied errors can indicate broader system issues, not just user-specific problems.
- **Response**: Quickly acknowledge and address widespread issues to minimize user impact.

## Action Items
- **Monitor**: Keep an eye on the central directory service for any recurring issues.
- **Notify**: Update users through HPC bulletins or email when widespread issues occur.
- **Document**: Maintain a record of such incidents for future reference and troubleshooting.
---

### 42284679__home_hpc%20auf%20lima%20nicht%20gemountet%3F.md
# Ticket 42284679

 ```markdown
# HPC Support Ticket: /home/hpc auf lima nicht gemountet?

## Keywords
- Home directory access
- Permission denied
- Mounting issues
- Verzeichnisdienst
- Fileserver access

## Problem Description
- User unable to access `/home/hpc` on `lima` cluster.
- Error message: `Could not chdir to home directory /home/hpc/mpt1/mpt160: Permission denied`.
- Multiple users experiencing the same issue.

## Root Cause
- Issue with a central directory service during an update.
- Many computers and cluster nodes were denied access to the fileserver.

## Solution
- HPC Admins are working on resolving the issue.
- Expected to be fixed soon.

## Lessons Learned
- Central directory service updates can cause widespread access issues.
- Communication with users about ongoing issues and expected resolution times is crucial.
- Monitoring and quick response to directory service issues are essential for maintaining system availability.
```
---

### 2023081442003291_Restoring%20the%20state%20of%20my%20%22vault%22-directory.md
# Ticket 2023081442003291

 # HPC Support Ticket: Restoring the State of Vault Directory

## Keywords
- Vault directory
- File corruption
- Snapshot feature
- SSHFS mount
- File restoration

## Summary
A user encountered file corruption in their vault directory while attempting to copy files between two HPC clusters (meggie and fritz) using SSHFS mounts. The user was unaware that the `/vault` partition is shared between the clusters, leading to data corruption.

## Root Cause
- The user mounted the `/vault` directory from both clusters simultaneously and attempted to copy files between them, resulting in file corruption.

## Solution
- The HPC Admin advised the user to utilize the snapshot feature of the filesystem to restore the files to their previous state.
- Detailed instructions on using the snapshot feature can be found in the provided documentation link.

## Lessons Learned
- Always check if directories are shared between clusters before performing file operations.
- Use the snapshot feature to restore corrupted files in the vault directory.
- Refer to the documentation for detailed instructions on using the snapshot feature.

## Documentation Link
- [HPC Storage Snapshots](https://hpc.fau.de/systems-services/documentation-instructions/hpc-storage/#snapshots)

## Additional Support
- If further assistance is needed, users can contact the HPC support team.

---

This report provides a concise summary of the issue, the root cause, the solution, and the lessons learned, making it a useful reference for support employees dealing with similar issues in the future.
---

### 2024091942000745_Problem%3A%20Folder%20disappeared.md
# Ticket 2024091942000745

 # HPC Support Ticket: Folder Disappeared

## Keywords
- Folder disappearance
- Snapshots
- Group permissions
- University email

## Summary
A user reported that a folder disappeared from their HPC account directory. The HPC Admin investigated and provided a solution.

## Root Cause
- The folder was deleted or moved between 09:00 and 09:30.
- The folder was group-writeable, allowing any member of the group to delete or move it.

## Solution
- The user can restore the folder using snapshots.
- Instructions for restoring from snapshots are available in the documentation.

## General Learnings
- Folders do not disappear randomly; they are deleted or moved by users or scripts.
- Group-writeable permissions can lead to accidental or intentional deletion by group members.
- Always use university email when contacting HPC support.
- Snapshots can be used to restore deleted folders.

## Documentation Link
- [Snapshots for Home and HPCVault](https://doc.nhr.fau.de/data/filesystems/#snapshots-for-home-and-hpcvault)

## Notes
- The HPC Admin initially marked the request as spam and not within their task area.
- The user was advised to use their university email for future support requests.
---

### 42100981_read-only%20file%20system.md
# Ticket 42100981

 # HPC Support Ticket: Read-Only File System

## Keywords
- Read-only file system
- chmod
- Scheduled downtime
- /home/woody
- /home/vault
- /home/hpc

## Problem Description
The user encountered issues modifying or creating new files under `/home/woody/iwmv/iwmv20/`, receiving messages that the files were "read-only." Attempts to change permissions using `chmod` resulted in a "Read-only file system" error. The user had full access to `/home/vault` and `/home/hpc`.

## Root Cause
The issue was due to a scheduled downtime of all HPC clusters, during which `/home/woody` was either unavailable or set to read-only.

## Solution
The HPC Admin reminded the user of the scheduled downtime announcement, which explained the read-only status of `/home/woody`.

## Lessons Learned
- **Communication**: Ensure users are aware of scheduled downtimes and their impact on file system availability.
- **Troubleshooting**: Recognize that read-only file system errors can be related to maintenance activities.
- **Documentation**: Maintain clear records of maintenance schedules and their effects on system accessibility.

## Notes
- The user acknowledged the explanation and thanked the HPC Admin for the clarification.
- This issue highlights the importance of communicating maintenance schedules effectively to users.
---

### 2021111542002126_Deleted%20Folder%20in%20Woody.md
# Ticket 2021111542002126

 ```markdown
# HPC-Support Ticket: Deleted Folder in Woody

## Keywords
- Deleted folder
- Snapshot recovery
- Subfolder recovery
- Woody
- Home directory
- Links

## Problem Description
- User accidentally deleted a folder on Woody.
- The folder was initially moved to Woody and linked to the home directory.
- The parent folder was also moved and linked, followed by deletion.
- The parent folder was recovered from a snapshot, but subfolders were missing.

## Root Cause
- User error in managing folder links and deletions.

## Solution
- HPC Admin identified the missing subfolders: `plots_crab`, `plots_SCR`, `plots_SN_1006`, and `K_matrix_data`.
- Subfolders were restored and placed in `caph/mppi045h/from_backup`.
- Restore command used:
  ```sh
  dsmc restore -subdir=yes -replace=no -verbose "/srv/home/caph/mppi045h/N_parameters_in_L/plots_SN_1006/*" /srv/home/caph/mppi045h/from_backup/
  ```

## Lessons Learned
- Regularly check and manage folder links to avoid accidental deletions.
- Use snapshots for recovering deleted files and folders.
- HPC Admins can assist in recovering lost data through backup and restore processes.
```
---

### 2024120342002847_%27Cannot%20Access%20HPC%20Server%27.md
# Ticket 2024120342002847

 ```markdown
# HPC Support Ticket: Cannot Access HPC Server

## Keywords
- Timeout error
- Spawn failed: Timeout
- File server issue

## Problem Description
User is unable to access the HPC server and receives a timeout error: "Spawn failed: Timeout."

## Root Cause
- Issue with a file server.

## Solution
- The HPC Admin mentioned that there was some trouble with a file server, which should be resolved by now.
- User was advised to be patient.

## General Learnings
- Timeout errors can be caused by issues with the file server.
- Users should be informed about ongoing issues and advised to wait for resolution.

## Next Steps
- Monitor the server status.
- Inform users about the resolution of the issue.
```
---

### 2024100942003599_Probleme%20mit%20geteilten%20Ordnern%20im%20Alex-Cluster%20%28%24WORK%29.md
# Ticket 2024100942003599

 ```markdown
# HPC Support Ticket: Issue with Shared Directories on Alex Cluster ($WORK)

## Keywords
- Alex Cluster
- $WORK directory
- Filesystem issue
- Permission denied
- No such file or directory

## Problem Description
- User unable to access the $WORK network mount.
- $WORK variable appears to be incorrectly set, pointing to a non-existent directory (`/home/woody/v108be/v108be12`).
- Attempting to access the actual directory (`/home/atuin/v108be/v108be12`) results in a "Permission denied" error.

## Root Cause
- Filesystem issues due to high load on the fileserver `atuin`.

## Solution
- HPC Admins are aware of the issue and are working on resolving it.
- Refer to the service disruption notice for updates: [Service Disruptions on Clusters Due to High Load on Fileserver Atuin](https://hpc.fau.de/2024/10/09/service-disruptions-on-clusters-due-to-high-load-on-fileserver-atuin/)

## General Learnings
- Check for known issues or service disruptions on the HPC cluster.
- Verify the correct setting of environment variables like $WORK.
- Ensure proper permissions are set for accessing directories.
```
---

### 2023100942005615_Shell%20auf%20Login%20Node%20unresponsive.md
# Ticket 2023100942005615

 ```markdown
# HPC Support Ticket: Shell auf Login Node unresponsive

## Keywords
- Login Node
- Shell
- SSH Connection
- File Server
- Crash
- Hang
- `cd` Command
- `ls` Command

## Problem Description
- User reported slow response times when connecting to login nodes via SSH.
- Commands like `cd` and `ls` were hanging indefinitely.

## Root Cause
- The file server `wnfs1` (home/woody) crashed, causing the observed hangs and slow responses.

## Solution
- The file server was restarted, resolving the issue.

## Lessons Learned
- File server crashes can cause significant delays and hangs in login node operations.
- Monitoring file server health is crucial for maintaining smooth operations on login nodes.
- Users should be informed about potential file server issues to manage expectations.

## Actions Taken
- HPC Admin identified the file server crash as the root cause.
- HPC Admin confirmed with the user that the issue was resolved after the file server was restarted.
- The ticket was closed after confirming the resolution.
```
---

### 2021080442002233_Problem%20accessing%20files%20on%20the%20storage%20of%20emmy.md
# Ticket 2021080442002233

 # HPC Support Ticket: Problem Accessing Files on Storage

## Keywords
- File access issue
- FASTTMP storage
- Directory listing
- Simulation folder

## Summary
User reports difficulty accessing files in the 'FASTTMP' storage. Specifically, listing the contents of a directory shows no results.

## Root Cause
- Possible issues with directory permissions or storage access.
- Potential corruption or misconfiguration in the storage system.

## Steps Taken
1. User reported the issue with a screenshot.
2. HPC Admins and 2nd Level Support team reviewed the ticket.

## Solution
- **Pending**: Further investigation required to determine the exact cause.
- **Possible Actions**:
  - Check directory permissions.
  - Verify storage system health.
  - Review user access logs for any anomalies.

## Learning Points
- Always verify directory permissions when access issues are reported.
- Regularly check the health and configuration of storage systems.
- Use logs to diagnose access-related problems.

## Next Steps
- HPC Admins to investigate the storage system.
- 2nd Level Support to assist with user-specific troubleshooting.

## Related Teams
- HPC Admins: Thomas, Michael Meier, Anna Kahler, Katrin Nusser, Johannes Veh
- 2nd Level Support: Lacey, Dane (fo36fizy), Kuckuk, Sebastian (sisekuck), Lange, Florian (ow86apyf), Ernst, Dominik (te42kyfo), Mayr, Martin
- Datacenter Head: Gerhard Wellein
- Training and Support Group Leader: Georg Hager
- NHR Rechenzeit Support: Harald Lanig
- Software and Tools Developer: Jan Eitzinger, Gruber
---

### 2024020142003681_Deleted%20files.md
# Ticket 2024020142003681

 # HPC Support Ticket: Deleted Files

## Keywords
- File recovery
- Deleted folder
- Backup
- Snapshots
- Filesystems

## Problem
User accidentally deleted a folder using `rm -r -f folder` on the fritz cluster.

## Root Cause
User error leading to data deletion.

## Solution
- **Filesystems with Backup and Snapshots**:
  - `/home/hpc`
  - `/home/vault`
  - Users can recover data themselves using frequent snapshots.
- **Filesystem with Limited Backup**:
  - `/home/woody`
- **Filesystems without Recovery Options**:
  - All other filesystems do not support data recovery.

## Steps Taken
1. User inquired about recovering a deleted folder.
2. HPC Admin provided information on backup and snapshot availability based on the filesystem.
3. User confirmed successful recovery from `/home/hpc`.

## Additional Information
- Detailed information on HPC storage and snapshots can be found [here](https://hpc.fau.de/systems-services/documentation-instructions/hpc-storage/).

## Lessons Learned
- Always check the filesystem before attempting data recovery.
- Utilize available snapshots for self-recovery on supported filesystems.
- Educate users on the importance of regular backups and the limitations of data recovery on different filesystems.
---

### 2024022042001816_HPC%20Down%20%22Sometimes%22%20on%20%22WORK%22.md
# Ticket 2024022042001816

 ```markdown
# HPC Support Ticket: HPC Down "Sometimes" on "WORK"

## Keywords
- HPC Server
- $WORK
- Fileserver Crash
- Console Hang
- Checkpoints
- Neural Networks
- Logging
- NN Training

## Problem Description
- User unable to navigate to $WORK directory.
- No error message returned; console hangs.
- Issue occurred between 12:15 and 12:55.
- Logging and checkpointing failed, affecting ongoing neural network training.

## Root Cause
- Fileserver crash between 12:15 and 12:55.

## Solution
- Confirmed by HPC Admins that the issue was due to a fileserver crash.
- No specific action required from the user's side.

## Lessons Learned
- Fileserver crashes can cause navigation issues to $WORK without returning error messages.
- Importance of detailed problem descriptions in support tickets, including username, machine, and specific error messages.
- Impact of fileserver crashes on logging and checkpointing, rendering ongoing work useless.

## Next Steps
- Monitor for similar issues and check for fileserver stability.
- Ensure users are informed about potential downtimes or issues.
```
---

### 2024032742001061_alex%20login.md
# Ticket 2024032742001061

 # HPC Support Ticket Conversation Analysis

## Keywords
- Login issues
- Putty
- VScode
- Fileserver reboot
- High load on node
- Script execution issues

## Summary
- **User Issue**: Unable to log in to `alex` via Putty or VScode.
- **Root Cause**: Fileserver `wnfs1` was being rebooted.
- **Solution**: Wait for the reboot to complete.

- **User Issue**: Unable to execute scripts on `alex`.
- **Root Cause**: High load on `alex2` node due to another user.
- **Solution**: Wait for the load to decrease or switch to another node.

## Lessons Learned
- **Communication**: Users should be informed about ongoing maintenance or updates.
- **Monitoring**: Regularly monitor node loads to identify and mitigate high usage issues.
- **Documentation**: Keep users informed about the status of the system through a status page or notifications.

## Actions Taken
- HPC Admin informed the user about the fileserver reboot.
- HPC Admin identified high load on `alex2` and suggested waiting for the load to decrease.

## Follow-up
- Ensure that maintenance activities are communicated to users in advance.
- Implement monitoring tools to alert users and admins about high load on nodes.

---

This analysis can be used to improve communication and monitoring practices to prevent similar issues in the future.
---

### 2022031842002367_Woody%3A%20Stale%20file%20handle.md
# Ticket 2022031842002367

 # HPC Support Ticket: Stale File Handle Issue

## Keywords
- Stale file handle
- Woody
- /home/woody
- /apps
- Server crash
- MOTD (Message of the Day)

## Problem Description
User encountered a "Stale file handle" error when trying to access Woody.

## Root Cause
The server for `/home/woody` and `/apps` crashed around 15:30.

## Solution
The server was back online around 16:10. Users were advised to check the MOTD for updates.

## Lessons Learned
- **Communication**: Important updates and outages should be communicated via MOTD.
- **Troubleshooting**: Stale file handle errors can be indicative of server issues or crashes.
- **Monitoring**: Regular monitoring of server status is crucial to quickly identify and resolve issues.

## Follow-up Actions
- Ensure users are aware of checking MOTD for system updates.
- Continue monitoring server health to prevent similar incidents.
---

### 2021012542001403_Recover%20a%20deleted%20folder.md
# Ticket 2021012542001403

 ```markdown
# Recover a Deleted Folder

## Keywords
- Folder recovery
- Backup
- HPC storage
- Accidental deletion

## Problem
- **Root Cause:** User accidentally deleted a folder.
- **Details:** The user deleted the folder `/home/woody/caph/mppi043h/pointing_model/tpoint` and requested its recovery.

## Solution
- **Backup Information:** The `/home/woody` directory has coarsely grained backup runs, not daily, and backups are kept for a short time.
- **Backup Schedule:** Backups are available from Friday or Monday in the early morning hours.
- **Action Taken:** HPC Admin restored the folder from the backup.
- **Result:** 378598 files / 4.7 GB restored.

## General Learning
- **Backup Policy:** Understand the backup policy and schedule for different directories on the HPC system.
- **User Communication:** Ensure clear communication with the user to understand the exact requirements and status of the folder.
- **Recovery Process:** Follow the established recovery process to restore files from backups when requested.

## References
- [HPC Storage Documentation](https://hpc.fau.de/systems-services/systems-documentation-instructions/hpc-storage/)
```
---

### 42305195_Deleting%20folders%20from%20the%20cluster.md
# Ticket 42305195

 # HPC Support Ticket: Deleting Folders from the Cluster

## Keywords
- Quota limit
- Permission denied
- `rm -r` command
- `chmod` command
- File ownership
- Quota increase

## Problem Description
- User reached the soft quota limit and attempted to delete folders.
- `rm -r` command failed due to permission issues.
- `chmod` command did not resolve the issue.

## Root Cause
- Files in the directory belonged to another user, and the current user did not have write permissions.

## Error Messages
```
rm: descend into write-protected directory `hexadecane/loplsaa'? y
rm: remove write-protected regular file `hexadecane/loplsaa/#mdout.mdp.1#'? y
rm: cannot remove `hexadecane/loplsaa/#mdout.mdp.1#': Permission denied
rm: remove write-protected regular file `hexadecane/loplsaa/#topol.tpr.1#'? y
rm: cannot remove `hexadecane/loplsaa/#topol.tpr.1#': Permission denied
rm: remove write-protected regular file `hexadecane/loplsaa/afterequi.pdb'? y
rm: cannot remove `hexadecane/loplsaa/afterequi.pdb': Permission denied
rm: remove write-protected regular file `hexadecane/loplsaa/confout_hexadecane.gro'? y
rm: cannot remove `hexadecane/loplsaa/confout_hexadecane.gro': Permission denied
```

## Solution
- The owner of the files (another user) needs to change the permissions using `chmod g+rwX` or delete the files themselves.
- Deleting these files will not affect the user's quota as they belong to another user.

## Additional Information
- The user's quota was increased from 500 GB to 750 GB.
- The user was only using 70 GB, indicating successful cleanup despite the permission issues.

## General Learning
- Ensure file ownership and permissions before attempting to delete files.
- Quota limits can be adjusted by HPC Admins if necessary.
- Proper communication with other users sharing directories is essential to avoid permission issues.
---

### 2022030642000355_Saturn%20data%20loss%20-%20bccb006h.md
# Ticket 2022030642000355

 ```markdown
# HPC-Support Ticket: Saturn Data Loss

## Subject
Saturn data loss - bccb006h

## Keywords
- Data loss
- Saturn
- rm -r
- Data recovery
- Home directory

## Problem Description
User accidentally deleted a directory on Saturn using `rm -r` command.

## Root Cause
- Accidental deletion of directory: `/home/saturn/bccb/bccb006h/COVID_VACCINE/DeProtonate_SelfAssembly_with_RNA_Revision/7-EQUILIBRATION_SEMI_Replica_2/`

## Solution
- User requested data recovery.
- HPC Admin acknowledged the request but did not provide a specific solution in the given conversation.

## General Learnings
- Always double-check before using `rm -r` to avoid accidental data loss.
- Regular backups can help in recovering accidentally deleted data.
- Ensure proper communication and follow-up in support tickets to avoid additional ticket-close spam.

## Next Steps
- HPC Admins should investigate the possibility of data recovery from backups or snapshots.
- Communicate the outcome of the recovery attempt to the user.
```
---

### 42198468_Woody%20Backup.md
# Ticket 42198468

 ```markdown
# HPC Support Ticket: Woody Backup

## Keywords
- Woody Cluster
- Data Recovery
- `rm` Command
- Restore

## Problem Description
- **User Issue:** Accidental deletion of important data using the `rm` command.
- **Affected Directory:** `/home/woody/capn/mpp450/SB_work_26032013/chains/nuhm2/fixA0/TanBeta10/nuhm2_flav*.txt`

## Solution
- **Action Taken:** HPC Admin restored the deleted files.
- **Restored Location:** A subdirectory named `hpc-rrze-restore` was created in the affected directory containing the restored files.

## Lessons Learned
- **Data Recovery:** It is possible to recover accidentally deleted files on the Woody cluster.
- **User Awareness:** Users should be cautious when using commands like `rm` to avoid accidental data loss.
- **Admin Support:** HPC Admins can assist in restoring deleted files, highlighting the importance of regular backups and support services.
```
---

### 2024112642003288_cluster%20unreachable.md
# Ticket 2024112642003288

 ```markdown
# HPC Support Ticket: Cluster Unreachable

## Keywords
- Cluster unreachable
- File server issue
- Reachability

## Summary
A user reported that the cluster was unreachable and inquired about its status. The HPC Admin confirmed that there was an ongoing issue with a file server, which was being addressed by the admins.

## Root Cause
- **Issue**: File server trouble
- **Impact**: Cluster unreachability

## Solution
- **Action Taken**: HPC Admins are working on resolving the file server issue.
- **Status**: Ongoing resolution

## Lessons Learned
- **Communication**: Prompt acknowledgment of the issue helps in managing user expectations.
- **Troubleshooting**: File server issues can lead to cluster unreachability, highlighting the importance of monitoring and maintaining these systems.

## Documentation for Future Reference
- **Symptom**: Cluster unreachable
- **Potential Cause**: File server issues
- **Resolution Steps**:
  1. Acknowledge the issue to the user.
  2. Inform the user that the HPC Admins are working on the problem.
  3. Monitor and resolve the file server issue.

```
---

### 2024100942003571_work%20directory%20not%20available.md
# Ticket 2024100942003571

 ```markdown
# HPC Support Ticket: Work Directory Not Available

## Keywords
- Work directory
- Permission denied
- Filesystem issues
- High load on fileserver

## Problem Description
- User unable to access their work directory.
- Error message: `-bash: cd: /home/woody/a101cb/a101cb10: Permission denied`

## Root Cause
- Issues with the filesystem due to high load on the fileserver.

## Solution
- HPC Admins are working on resolving the filesystem issues.
- Reference link for more information: [Service Disruptions on Clusters Due to High Load on Fileserver Atuin](https://hpc.fau.de/2024/10/09/service-disruptions-on-clusters-due-to-high-load-on-fileserver-atuin/)

## General Learnings
- Filesystem issues can cause permission denied errors when accessing directories.
- High load on the fileserver can lead to service disruptions.
- Users should check for any ongoing maintenance or issues on the HPC cluster.
```
---

### 2022121642003451_HPC%20-%20all%20files%20are%20gone.md
# Ticket 2022121642003451

 # HPC Support Ticket: Missing Files in User Directory

## Keywords
- Missing files
- Snapshots
- Data recovery
- `cp -r` command
- Linux file system

## Problem Description
- User reported missing files in their home directory (`~/collocations`).
- Only two files were visible: `All_Data-12-12-22-Copy1.ipynb` and `All_Data-12-12-22.ipynb`.

## Root Cause
- Possible accidental deletion or movement of files by the user.

## Solutions and Steps Taken
1. **Snapshots Availability**:
   - HPC Admins informed the user about the availability of snapshots for the `$HOME` directory.
   - Documentation link provided: [HPC Storage Snapshots](https://hpc.fau.de/systems-services/documentation-instructions/hpc-storage/#snapshots).

2. **User Queries**:
   - User asked about the date of file deletion, availability of a trash box, and recovery of a complete folder using snapshots.
   - HPC Admins clarified that the date of deletion is not trackable, no trash box is available, and folders can be recovered using snapshots.

3. **Snapshot Recovery Attempt**:
   - User listed available snapshots using `ls -l .snapshots/`.
   - User attempted to use `cp -r` but encountered an error due to missing source and destination arguments.

4. **Additional Guidance**:
   - HPC Admins provided further instructions on using `cp -r` with source and destination arguments.
   - Emphasized the importance of checking snapshots promptly due to limited retention periods.

## Lessons Learned
- **Snapshot Usage**: Understand and utilize snapshots for data recovery.
- **Command Syntax**: Ensure proper syntax when using commands like `cp -r`.
- **Prompt Action**: Act promptly when data is missing to utilize available snapshots within their retention period.

## Documentation Reference
- [HPC Storage Snapshots](https://hpc.fau.de/systems-services/documentation-instructions/hpc-storage/#snapshots)

## Follow-up
- User was advised to check snapshots promptly and follow the correct command syntax for data recovery.
- If data is not found in snapshots, further recovery may be complex and require additional support.
---

### 2024092642003078_HPC%20file%20deleted.md
# Ticket 2024092642003078

 ```markdown
# HPC Support Ticket: File Deletion Recovery

## Keywords
- File deletion
- Recovery
- Snapshots
- Home directory
- HPC vault

## Problem
- **Root Cause:** User accidentally deleted an important file (`exploring_thesis_data.ipynb`) from their project directory.
- **Attempted Solution:** User tried to access the Trash directory but the file was not found.

## Solution
- **Admin Suggestion:** The HPC Admin suggested checking the snapshots for the home directory and HPC vault as per the documentation: [Snapshots for Home and HPC Vault](https://doc.nhr.fau.de/data/filesystems/?h=recover#snapshots-for-home-and-hpcvault).

## General Learnings
- **File Recovery:** In case of accidental file deletion, users should check the snapshots available for their home directory and HPC vault.
- **Documentation Reference:** Always refer to the official documentation for recovery procedures.

## Next Steps
- **User Action:** Follow the instructions provided in the documentation to recover the deleted file from snapshots.
- **Admin Action:** Monitor the user's progress and provide further assistance if needed.
```
---

### 42284683_Home.md
# Ticket 42284683

 # HPC Support Ticket: Home Directory Access Issue

## Keywords
- Home directory access
- Permission denied
- .Xauthority file
- Verzeichnisdienst (directory service)
- Fileserver access

## Problem Description
- User unable to access home directory on both `emmy` and `lima` clusters.
- Error messages:
  - `Could not chdir to home directory /home/hpc/bco/bco123: Permission denied`
  - `/usr/bin/xauth: timeout in locking authority file /home/hpc/bco/bco123/.Xauthority`

## Root Cause
- Issue with a central directory service update causing many systems to lose access to the fileserver.

## Solution
- HPC Admins are aware of the problem and are working on a resolution.
- The issue is expected to be resolved soon.

## General Learnings
- Central directory service issues can cause widespread access problems.
- Permission denied errors and `.Xauthority` file locking timeouts can indicate a broader system issue.
- Communication about ongoing issues and expected resolution times is crucial for user satisfaction.
---

### 2017112442001216_Woodycluster%20down%3F.md
# Ticket 2017112442001216

 ```markdown
# HPC Support Ticket: Woodycluster Down

## Keywords
- Woodycluster
- Login issue
- System unresponsive

## Summary
- **User Report:** Unable to log in to Woodycluster; system unresponsive even after successful login.
- **Root Cause:** Unknown (no admin response provided).
- **Solution:** Not provided.

## What Can Be Learned
- **Common Issue:** Login and system responsiveness issues on Woodycluster.
- **Next Steps:** Check system status, network connectivity, and server logs for troubleshooting.
- **Escalation:** Involve HPC Admins for further investigation if the issue persists.
```
---

### 2022090542004262_loss%20of%20data%20at%20NHR%40FAU%20-%20b133ae13.md
# Ticket 2022090542004262

 ```markdown
# HPC-Support Ticket: Loss of Data at NHR@FAU

## Keywords
- Data loss
- Downtime
- Relocation
- $WORK directory
- rsync
- NHR users

## Summary
During a scheduled downtime, data was relocated from the old directory to a new $WORK directory dedicated to NHR users. Due to an error in the final merging rsync process, some data in the $WORK/kondorun/g0_dat/ directory tree was destroyed.

## Root Cause
- Incorrect handling of the rsync command during data merging.

## Solution
- Users should check their files for any missing data.
- Recompute the lost data if possible.

## Lessons Learned
- Ensure proper handling of rsync commands during data relocation to avoid data loss.
- Always verify data integrity after relocation.
- Communicate with users about potential data loss and steps to recover or recompute lost data.
```
---

### 2024110442003784_Directory%20Deletion%20Permission%20Issue%20on%20Alex%20Cluster.md
# Ticket 2024110442003784

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Keywords
- Permission denied
- Directory deletion
- HPC cluster
- Maintenance
- Ticket management

## Summary
A user encountered permission issues while attempting to delete specific directories on the Alex cluster. The user was unable to remove files within the directory `11954_handwritten_Fonts` due to restricted permissions. The user attempted various methods, including modifying permissions through Python, but without sudo access, they were unable to change the file attributes or delete these files.

## Root Cause
- The user did not have sufficient permissions to delete the files.
- The user did not provide the full path to the files, making it difficult for support to locate and assist with the issue.

## Lessons Learned
- **Provide Full Paths**: When reporting issues related to file permissions or deletion, always provide the full path to the files in question.
- **Avoid Replying to Old Emails**: When encountering a new problem, start a new email thread instead of replying to an old one to keep the ticket organized and focused on a single issue.
- **Maintenance Awareness**: Be aware of scheduled maintenance periods and check the maintenance status page for updates.

## Solution
- The user should provide the full path to the files and their username to the HPC support team for further assistance.
- The HPC support team can then adjust the permissions or delete the files as needed.

## Additional Notes
- Proper ticket management is crucial for efficient problem-solving.
- Clear communication and detailed information help in resolving issues more quickly.
```
---

### 2023082342001196_Zugriff%20auf%20_home_atuin_b136dc%20schl%C3%83%C2%A4gt%20fehl.md
# Ticket 2023082342001196

 # HPC Support Ticket: Access to /home/atuin/b136dc Fails

## Keywords
- Access issue
- Project directory
- `/home/atuin/b136dc`
- `cd $WORK`
- `fritz4`
- Fileserver
- Directory mounting

## Problem Description
The user reported that access to the project directory `/home/atuin/b136dc` was failing. The directory was not visible in the terminal, but jobs were still running. The `cd $WORK` command was redirecting to `/home/woody/b136dc/b136dc13` instead of the correct directory.

## Root Cause
The issue was specific to the `fritz4` machine. The directory `/home/atuin/b136dc` was not being mounted correctly on `fritz4`.

## Solution
The HPC Admins resolved the issue by ensuring that `fritz4` correctly mounts the `/home/atuin/b136dc` directory. After the fix, the `cd $WORK` command pointed to the correct directory upon re-login.

## Additional Notes
- Directories in `/home/atuin` are mounted on demand. If `ls /home/atuin` does not show the directory, it is not necessarily an issue. However, if `ls /home/atuin/b136dc` returns "no such file or directory," then there is a problem.
- Ensure that the correct mounting and access permissions are in place for project directories across all relevant machines.

## Lessons Learned
- Always specify the machine where the issue occurs.
- Understand that directories may be mounted on demand and not always visible.
- Verify the correct functioning of environment variables like `$WORK`.

## Actions Taken
- Identified the specific machine (`fritz4`) with the issue.
- Corrected the mounting of the project directory on `fritz4`.
- Ensured that the `$WORK` variable points to the correct directory after re-login.
---

### 2019042542000912_IMPORTANT%3A%20accidentally%20deleted%20files%20from%20%20%24WOODYHOME.md
# Ticket 2019042542000912

 # HPC Support Ticket: Accidentally Deleted Files from $WOODYHOME

## Keywords
- Accidental file deletion
- File restoration
- $WOODYHOME
- MEGGIE clusters
- Backup policy

## Summary
A user accidentally deleted important files from their $WOODYHOME directory on the MEGGIE clusters and requested assistance to restore them.

## Root Cause
- User error leading to accidental deletion of files.

## Solution
1. **User Action**: The user promptly reported the issue, specifying the exact files and their location.
2. **HPC Admin Action**: The HPC admin checked the backup policy for $WOODYHOME and confirmed that limited backup was available.
3. **File Restoration**: The HPC admin restored the specified files from the most recent backup (dated 2019-04-22) to a new directory within the user's $WOODYHOME.

## Lessons Learned
- **Backup Policy Awareness**: Users should be aware of the backup policies for different file systems. $WOODYHOME has limited backup, which means backups are not daily and data is kept for a short time.
- **Prompt Reporting**: Immediate reporting of accidental deletions increases the chances of successful file restoration.
- **Specificity**: Providing specific details about the deleted files and their location helps in quicker resolution.

## Conclusion
Accidental file deletions can be mitigated by understanding backup policies and promptly reporting incidents. HPC admins can restore files from backups if available, but users should not rely solely on these backups for critical data.

---

This documentation can serve as a reference for support employees to handle similar incidents in the future.
---

### 42043750_Woody%20-%20wsfs.md
# Ticket 42043750

 # HPC Support Ticket: Woody - wsfs Issue

## Keywords
- wsfs
- woody
- ls -lrt
- shell hang
- server reboot
- failover

## Problem Description
- User reported that shells were hanging when attempting to execute `ls -lrt` on the wsfs filesystem on the woody cluster.

## Root Cause
- One of the servers spontaneously rebooted, causing temporary disruptions in the filesystem service.

## Solution
- The failover mechanism was activated, and the service resumed functioning shortly after the reboot.
- The affected server came back online and resumed its services, potentially causing another brief hang.

## Lessons Learned
- Spontaneous server reboots can cause temporary disruptions in filesystem services.
- The failover mechanism generally works well to restore services quickly.
- Users should be informed about potential temporary disruptions due to server reboots.

## Actions Taken
- HPC Admin confirmed the server reboot and the subsequent restoration of services.
- No further action was required as the issue resolved itself.

## Recommendations
- Monitor server health to minimize spontaneous reboots.
- Ensure failover mechanisms are robust and tested regularly.
- Communicate with users about potential temporary disruptions and their causes.
---

### 2024052142001765_Regarding%20read%20only%20file%20system.md
# Ticket 2024052142001765

 # HPC Support Ticket: Read-Only File System Issue

## Keywords
- Read-only file system
- Scheduled downtime
- Maintenance period
- $WORK directory
- Tier-3 accounts

## Problem Description
- **User Issue:** Unable to modify files in the `tinygpu` or `meggie` work directory due to a "Read-only file system" error.
- **Root Cause:** Scheduled downtime and maintenance of the HPC systems, affecting the `$WORK` directory for Tier-3 accounts.

## Solution
- **Admin Response:** Informed the user about the scheduled downtime and maintenance period.
- **Action Required:** If the issue persists in other filesystems, the user should provide additional details.

## General Learnings
- Always check for scheduled maintenance or downtime notifications.
- Ensure that the issue is not related to a specific filesystem before escalating.
- Communicate clearly with users about the scope and duration of maintenance periods.

## References
- [Scheduled Downtime of All HPC Systems on May 21](https://hpc.fau.de/2024/05/21/scheduled-downtime-of-all-hpc-systems-on-may-21/)
- HPC Support Email: [support-hpc@fau.de](mailto:support-hpc@fau.de)
- HPC Website: [https://hpc.fau.de/](https://hpc.fau.de/)
---

### 2024032542003527_woody%20error%20on%20Memoryhog.md
# Ticket 2024032542003527

 # HPC Support Ticket: Woody Error on Memoryhog

## Keywords
- Stale file handle
- Woody share
- Memoryhog
- Reboot
- Wartung (maintenance)

## Problem Description
- User unable to access the `woody` share on `memoryhog.rrze.uni-erlangen.de`.
- Error message: `ls: cannot access 'woody': Stale file handle`.
- Similar issue observed in the user's home directory.
- The share is available on `cshpc.rrze.uni-erlangen.de`.

## Root Cause
- The `memoryhog` node was not rebooted after a maintenance operation involving the `/home/woody` share.

## Solution
- HPC Admins scheduled a reboot of `memoryhog` at 18:00.
- After the reboot, the `/home/woody` share should be accessible again.

## General Learnings
- Stale file handle errors can indicate that a node needs to be rebooted after maintenance operations.
- Always ensure that all affected nodes are rebooted after maintenance to prevent such issues.
- If a share is accessible on one node but not another, it may indicate a node-specific problem.
---

### 2024120342003051_Cant%20execute%20any%20command%20on%20meggie%20cluster.md
# Ticket 2024120342003051

 # HPC Support Ticket: Unable to Execute Commands on Meggie Cluster

## Keywords
- Meggie cluster
- Command execution failure
- sinfo, htop, git
- Fileserver issue
- wnfs1 (/home/woody)

## Problem Description
User reported being unable to execute any commands on the Meggie cluster, including `sinfo`, `htop`, `git`, and others.

## Root Cause
Issue with the fileserver `wnfs1` (`/home/woody`).

## Solution
The fileserver issue was resolved by the HPC Admins. If the user still encounters problems, they should specify which server is affected.

## Lessons Learned
- Fileserver issues can cause widespread command execution failures.
- Resolving fileserver problems can restore normal functionality.
- Users should be encouraged to provide specific details about affected servers if issues persist.

## Next Steps
- Monitor the fileserver `wnfs1` for any recurring issues.
- Ensure users are informed about resolved issues and how to report persistent problems.

## Relevant Contacts
- HPC Admins: For fileserver and cluster management.
- 2nd Level Support Team: For additional troubleshooting and user support.
- Head of the Datacenter: For overall datacenter management.
- Training and Support Group Leader: For user training and support.
- NHR Rechenzeit Support: For computing time support and applications for grants.
- Software and Tools Developer: For software-related issues and tools development.
---

### 2024031342000838_Possible%20data%20loss.md
# Ticket 2024031342000838

 # HPC Support Ticket: Possible Data Loss

## Keywords
- Data loss
- Quota
- Snapshots
- Backup
- Programming mistake

## Summary
A user reported missing folders in their HPC account and inquired about potential data loss. The folders were expected to be created during jobs but were not found in the specified directory. The user was also interested in accessing backups.

## Root Cause
- **Programming Mistake**: The user later identified that the missing folders were likely never created due to a programming error.

## Quota Information
- **/home/hpc**: Used 50.9G, SoftQ 104.9G, HardQ 209.7G
- **/home/woody**: Used 27.7G, SoftQ 500.0G, HardQ 750.0G
- **/home/vault**: Used 171.5G, SoftQ 1048.6G, HardQ 2097.2G

## Solution
- **Snapshots**: The HPC Admin advised the user to check snapshots for /home/hpc and /home/vault to verify if the folders ever existed.
- **Backup Access**: The user was directed to the documentation on snapshots for home and HPC vault.

## Learnings
- Exceeding quota does not remove existing files but prevents new files from being created or data written to existing files.
- Snapshots can be used to verify the existence of files and folders over time.
- Users should check snapshots before requesting admin intervention for missing files.

## Documentation Link
- [Snapshots for Home and HPC Vault](https://doc.nhr.fau.de/data/filesystems/#snapshots-for-home-and-hpcvault)

## Next Steps for Support
- Direct users to check snapshots for missing files.
- Provide documentation links for snapshot usage.
- Clarify quota implications for file creation and modification.
---

### 2015072842004227_Login%20problems.md
# Ticket 2015072842004227

 # HPC Support Ticket: Login Problems

## Keywords
- Login issues
- Hanging filesystems
- Fileserver problems
- Welcome messages
- Command prompt
- Client software

## Problem Description
- User unable to execute commands after logging into the cluster (woody).
- No welcome messages or command prompt displayed upon login.
- Issue persists even after relogging.

## Root Cause
- Hanging filesystems and fileserver issues on the HPC side.

## Troubleshooting Steps
1. **User**:
   - Provided a detailed description of the problem.
   - Specified the client machine (bccb11).
   - Described the sequence of events leading to the issue.

2. **HPC Admin**:
   - Identified potential cause as hanging filesystems.
   - Requested more information about the client software used for login.
   - Confirmed that the issue was due to fileserver problems.

## Solution
- The issue was acknowledged as a server-side problem with the fileserver.
- No specific user-side action was required as the problem was not on the user's end.
- HPC Admins worked on resolving the fileserver issues, but the root cause was not yet identified, indicating potential recurrence.

## Notes
- Users experiencing similar issues should report them to HPC support for further investigation.
- HPC Admins should monitor fileserver health to prevent recurrence.

---

This documentation can be used to diagnose and address similar login issues in the future.
---

### 2024043042000885_Access%20issue.md
# Ticket 2024043042000885

 ```markdown
# HPC Support Ticket: Access Issue

## Keywords
- Access issue
- File server load
- HPC credentials
- Job monitoring
- HPC Portal

## Problem Description
- User unable to access `/home/woody/iwi5/iwi5176h`.
- User unable to log into `https://monitoring.nhr.fau.de/login` with HPC credentials.

## Root Cause
- File server load causing service disruptions.
- Incorrect login procedure for job monitoring.

## Solution
- **File Server Access**:
  - Acknowledge ongoing service disruptions due to high file server load.
  - Refer to the service disruption notice: [Service Disruptions on Clusters](https://hpc.fau.de/2024/04/19/service-disruptions-on-clusters-due-to-high-file-server-load/).

- **Job Monitoring Access**:
  - Log into the HPC Portal: [HPC Portal](https://portal.hpc.fau.de/).
  - Follow the steps described in the documentation: [Job Monitoring with Clustercockpit](https://doc.nhr.fau.de/job-monitoring-with-clustercockpit/#hpc-portal-users-without-password).

## General Learning
- Always check for ongoing service disruptions when encountering access issues.
- Use the HPC Portal for job monitoring access and follow the documented steps for users without a password.
```
---

### 2019012942001884_Ordner%20auf%20emmy%20gel%C3%83%C2%B6scht.md
# Ticket 2019012942001884

 # HPC Support Ticket: Folder Deletion in ${HOME}

## Keywords
- Folder deletion
- ${HOME} directory
- Snapshots
- User history
- Data recovery

## Summary
A user reported that the `/bin` folder in their ${HOME} directory on the `emmy` cluster had been deleted. The user was concerned about the loss of important programs stored in this folder.

## Root Cause
- The user inadvertently deleted the `/bin` folder themselves.
- The deletion occurred on January 23rd at 11:24:24.

## Solution
- The HPC Admin provided information about snapshots available for the ${HOME} directory.
- The user was instructed to check the snapshot from January 23rd to recover the deleted folder.
- The snapshot is read-only, but the user can copy the necessary data back to their ${HOME} directory.

## Lessons Learned
- Users should be aware of the snapshot feature for data recovery.
- Regularly checking the history of commands can help identify the cause of unexpected changes.
- Always double-check before executing commands that delete files or directories.

## References
- [HPC Storage Snapshots](https://www.anleitungen.rrze.fau.de/hpc/hpc-storage/#snapshots)
---

### 2022020442001912_Filesystem%20h%C3%83%C2%A4ngt%3F.md
# Ticket 2022020442001912

 ```markdown
# HPC Support Ticket: Filesystem Hängt?

## Keywords
- Login prompt issue
- Filesystem hang
- Cluster monitoring
- Interactive processes

## Problem Description
User reports that they are unable to get a prompt when logging into `cshpc`. The user suspects that a filesystem might be hanging.

## Root Cause
- The exact root cause is not explicitly identified in the conversation.
- Possible causes mentioned include interactive processes on `cshpc` and various login nodes.

## Solution
- No specific solution is provided in the conversation.
- The HPC Admin mentions that the planned expansion of cluster monitoring should provide better data for diagnosing such issues in the future.

## General Learnings
- Interactive processes on login nodes can cause login delays.
- Improved cluster monitoring can help diagnose and resolve such issues more effectively.
- Users should be informed about ongoing monitoring improvements to manage expectations.

## Next Steps
- Continue to monitor the system for similar issues.
- Implement and utilize the expanded cluster monitoring to gather more data for future troubleshooting.
```
---

### 2024022642001163_Isuue%20with%20HPC%20Woody.md
# Ticket 2024022642001163

 # HPC Support Ticket: Issue with HPC Woody

## Keywords
- Access issue
- Timeout
- Maintenance
- Filezilla
- Terminal

## Problem Description
- User unable to access `/home/woody/iwi5/iwi5176h` from both terminal and Filezilla.
- Access to `/home/hpc/iwi5/iwi5176h` and `/home/vault/iwi5/iwi5176h` is successful.
- Timeout issue occurs specifically when trying to access `/home/woody/iwi5/iwi5176h`.

## Root Cause
- Clusters and frontends are down due to maintenance.

## Solution
- Wait for maintenance to be completed.
- Try logging in again the next day.

## General Learning
- Always check for ongoing maintenance before troubleshooting access issues.
- Inform users about scheduled maintenance to manage expectations.

## Next Steps for Support
- Monitor maintenance progress.
- Notify user once systems are back online.

---

**Note:** This report is for internal use by HPC support employees to assist in resolving similar issues in the future.
---

### 2024011242001084_Lost%20data%20on%20titan%20%28gwgi008h%29.md
# Ticket 2024011242001084

 # HPC Support Ticket: Lost Data on Titan

## Keywords
- Data loss
- Accidental deletion
- No backup
- Titan
- Meggie-cluster

## Summary
A user accidentally deleted five folders containing modeling data on the Titan system. The data was generated using significant resources on the Meggie-cluster. The user inquired about the possibility of data recovery.

## Root Cause
- Accidental deletion of data due to lack of attention.

## Solution
- **No Recovery Possible**: The HPC Admin confirmed that there is no backup of data on Titan and no duplicated data exists elsewhere. Therefore, the deleted data cannot be recovered.

## Lessons Learned
- **Importance of Backups**: Users should regularly back up important data to prevent loss in case of accidental deletion.
- **Attention to Actions**: Users should be cautious when performing actions that could lead to data loss, such as deleting files or folders.

## Actions Taken
- The HPC Admin informed the user that data recovery is not possible.
- The support ticket was closed.

## Recommendations
- **User Education**: Inform users about the importance of backing up data and the lack of automatic backups on certain systems.
- **Data Management Policies**: Consider implementing policies or guidelines for data management to prevent future incidents.

---

This documentation serves as a reference for support employees to handle similar incidents in the future.
---

### 2024112242001411_Recovery%20of%20files.md
# Ticket 2024112242001411

 # HPC Support Ticket: Recovery of Files

## Keywords
- File recovery
- Backup
- Snapshots
- Accidental deletion
- /home/saturn

## Problem
- **Root Cause:** User accidentally deleted important files in `/home/saturn/gwgi/gwgi019h/output_WRF/nomodlakes_glac2019`.
- **Details:** Files ending with `03-01_00:00:00`, `04-01_00:00:00`, and `07-01_00:00:00` were removed.

## Solution
- **Response from HPC Admin:** There are no backups or snapshots available for `/home/saturn`. Therefore, the deleted files cannot be recovered.

## General Learning
- **Backup Policy:** Understand the backup and snapshot policies for different directories on the HPC system.
- **User Awareness:** Inform users about the importance of maintaining their own backups, especially for critical data.

## Future Prevention
- **User Education:** Encourage users to regularly back up important files to prevent data loss.
- **Documentation:** Ensure that backup policies and procedures are clearly documented and accessible to users.

## Related Teams
- **HPC Admins:** Thomas, Michael Meier, Anna Kahler, Katrin Nusser, Johannes Veh
- **2nd Level Support:** Lacey, Dane (fo36fizy), Kuckuk, Sebastian (sisekuck), Lange, Florian (ow86apyf), Ernst, Dominik (te42kyfo), Mayr, Martin
- **Datacenter Head:** Gerhard Wellein
- **Training and Support Group Leader:** Georg Hager
- **NHR Rechenzeit Support:** Harald Lanig
- **Software and Tools Developer:** Jan Eitzinger, Gruber

## Conclusion
- **No Recovery Possible:** Without backups or snapshots, accidentally deleted files in `/home/saturn` cannot be recovered.
- **Prevention:** Educate users on the importance of regular backups and provide clear documentation on backup policies.
---

### 2024032742000946_%24WORK.md
# Ticket 2024032742000946

 ```markdown
# HPC Support Ticket: $WORK Access Issue

## Keywords
- $WORK
- Permission denied
- Fileserver reboot
- wnfs1

## Problem Description
- User unable to switch to $WORK directory.
- Previous attempts to execute simple system commands resulted in "permission denied" errors.

## Root Cause
- The fileserver `wnfs1` was being rebooted, causing temporary access issues.

## Solution
- Wait for the fileserver reboot to complete.

## Lessons Learned
- Temporary server maintenance can cause permission issues and access problems.
- Users should be informed about scheduled maintenance to avoid confusion.
```
---

### 42077305_Problem%20mit%20home_cluster64.md
# Ticket 42077305

 # HPC Support Ticket: Problem with home/cluster64

## Keywords
- home/cluster64
- Input/output error
- RAID crash
- Firmware update
- Filesystem migration

## Problem Description
User reported an input/output error when trying to list the contents of `/home/cluster64`.

## Root Cause
The issue was caused by a crash of one of the two RAIDs where `/home/cluster64` is located.

## Solution
- HPC Admins updated the firmware to the latest version.
- `/home/cluster64` should be functional again as of 16:15.

## Follow-up
- If the problems persist after the firmware update, the user may need to consider migrating to a different filesystem.
- Further monitoring is required to determine if the update resolved the issue.

## General Learning
- Regular firmware updates can help mitigate hardware-related issues.
- Persistent problems with a specific filesystem may indicate the need for migration to a more stable environment.
- Communication with users about potential long-term solutions is important for maintaining trust and satisfaction.
---

### 2024021542003655_H%C3%83%C2%A4ngender%20Login.md
# Ticket 2024021542003655

 ```markdown
# HPC Support Ticket: Hängender Login

## Keywords
- Login delay
- Hanging login
- Fileserver load
- $WORK

## Problem Description
- User reported a hanging login issue on CSHPC after the "Last login:" message.

## Root Cause
- High load on the fileserver (atuin) responsible for $WORK.

## Solution
- The issue was temporary and resolved once the fileserver load normalized.

## Lessons Learned
- High load on fileservers can cause login delays.
- Monitoring fileserver performance can help in proactive issue resolution.

## Actions Taken
- HPC Admin acknowledged the issue and confirmed that the fileserver was under high load.
- No specific action was required as the issue resolved itself.

## Follow-up
- Continue monitoring fileserver performance to prevent similar issues in the future.
```
---

### 2024110242000254_Undeletable%20files.md
# Ticket 2024110242000254

 ```markdown
# HPC Support Ticket: Undeletable Files

## Keywords
- Undeletable files
- Singularity sandbox
- Permissions
- `chmod`
- `--fix-perms`

## Problem Description
The user created two folders with files that they own and have read/write access to but are unable to delete. The folders were generated by converting a Singularity file to a sandbox without using the `--fix-perms` option.

## Root Cause
The issue is likely due to subdirectories within the folders where the user lacks write permissions.

## Solution
The user can grant themselves the necessary permissions using the `chmod` command. For example:
```bash
chmod -R u+rwX /home/woody/scvl/scvl125h/MLPerf/alex/mlperf_sandbox
```
This should allow the user to delete the folders.

## Additional Notes
- Always use your university email for contacting support.
- Provide the exact error message when reporting issues, as it can offer clues to the problem.

## Reproduction Steps
1. Pull a Singularity image:
   ```bash
   apptainer pull docker://almalinux:9
   ```
2. Build a sandbox without fixing permissions:
   ```bash
   apptainer build --fakeroot --sandbox mlperf_sandbox/ almalinux_9.sif
   ```

## Lessons Learned
- Ensure proper permissions when creating sandboxes with Singularity.
- Use the `--fix-perms` option to avoid permission issues.
- Grant necessary permissions using `chmod` if issues arise.
```
---

### 2019032742001419_Deletion%20of%20directories.md
# Ticket 2019032742001419

 ```markdown
# HPC-Support Ticket: Deletion of Directories

## Keywords
- Directory Deletion
- HPC Cluster
- User Departure
- Data Cleanup

## Summary
A user requested the deletion of specific directories on the HPC cluster because they are no longer needed and the original creator has left the institute.

## Root Cause
- Directories were created by a user who has left the institute.
- Directories are no longer needed.

## Solution
- HPC Admins need to delete the specified directories to free up space and maintain a clean file system.

## Action Taken
- User requested deletion of the following directories:
  - `/home/vault/caph/shared/data/dst_mc_hd_extclean/Zeuthen`
  - `/home/vault/caph/shared/data/dst_mc_hd_extclean/phase1b_old`

## General Learning
- Regularly review and clean up directories created by departed users.
- Ensure proper communication with HPC Admins for directory deletion requests.
```
---

### 2024032742000964_HPC%20Online.md
# Ticket 2024032742000964

 ```markdown
# HPC Support Ticket: Woody Cluster Connection Issue

## Keywords
- Woody Cluster
- iwso
- Connection Issue
- File Server Reboot
- Login Issues

## Problem Description
User unable to connect to the Woody cluster under iwso.

## Root Cause
The file server was currently rebooting, causing login issues.

## Solution
Wait for the file server to complete its reboot process.

## General Learnings
- File server reboots can cause temporary login issues.
- Users should be informed about scheduled maintenance or reboots to avoid confusion.

## Next Steps
- Monitor the file server reboot process.
- Inform users once the server is back online.
```
---

### 42284673_problems%20with%20home%20on%20emmy.md
# Ticket 42284673

 # HPC Support Ticket: Problems with Home Directory Access on Emmy

## Keywords
- Home directory access
- Permission denied
- Central directory service
- Fileserver access
- Cluster access issues

## Problem Description
- User unable to list home directory on `emmy` cluster.
- Error message: `ls: cannot access /home/hpc/bccb/bccb04: Permission denied`.
- Tab completion for directory path results in an empty character.
- Issue confirmed by another user.
- No problems accessing home directory from `woody` cluster.

## Root Cause
- Issue with the central directory service causing fileservers to deny access to most clusters.

## Solution
- HPC Admins are aware of the problem and working on a fix.
- Issue expected to be resolved soon.

## General Learnings
- Central directory service issues can cause widespread access problems.
- Check for known issues and ongoing maintenance before troubleshooting individual accounts.
- Communicate effectively with users about system-wide issues and expected resolution times.
---

### 2024071442000936_Accidentally%20deleted%20the%20data%20folder.md
# Ticket 2024071442000936

 # HPC Support Ticket: Accidentally Deleted Data Folder

## Keywords
- Accidental deletion
- Data folder
- Backup restoration
- HPC support

## Root Cause
- User accidentally deleted a data folder while attempting to delete a file.

## Problem Description
- User reported accidentally deleting the entire data folder instead of a single file.
- The folder in question was `/home/woody/iwi5/iwi5190h/CheXzero/data`.

## HPC Admin Response
- HPC Admin requested clarification on the exact folder to be restored.
- Noted that there is limited backup of `/home/woody`, running every few days.
- Confirmed the presence of a file named `data` in the specified directory.

## Solution
- User deleted the conflicting file named `data`.
- HPC Admin restored the `data` folder from the backup.
- The restored folder may contain previously deleted or renamed files due to the nature of the backup.

## Outcome
- User confirmed that they successfully retrieved their data.

## General Learnings
- Always confirm the exact path and type (file/folder) before performing delete operations.
- Regular backups are crucial, but they may not capture all changes due to limited frequency.
- HPC Admins can restore data from backups, but users should be aware of potential discrepancies in restored data.

## Documentation for Future Reference
- When users accidentally delete important data, HPC Admins can assist in restoring from backups.
- Users should provide clear and specific details about the deleted data to facilitate the restoration process.
- Backups may not be up-to-date, so users should regularly verify their important data.
---

### 2024080742000546_Verzeichnisschleife%20im%20Home%20von%20iwso150h.md
# Ticket 2024080742000546

 ```markdown
# HPC Support Ticket: Directory Loop in Home Directory

## Keywords
- Directory loop
- Home directory
- Backup logs
- Excessive path length

## Problem Description
A user had a directory loop in their home directory under `/home/hpc/iwso/iwso150h/RhinoForce/RFrawPictures/RFrawPictures/RFrawPictures`, where the `RFrawPictures` directory was nested within itself multiple times.

## Impact
The directory loop caused issues with the daily backup process, cluttering the backup logs due to the excessively long path. The backup software refused to include the path in the backup.

## Root Cause
The directory loop was unintentional and likely created by accident.

## Solution
The user was notified and deleted the unnecessary nested directories, resolving the issue.

## Lessons Learned
- Regularly check home directories for unintentional directory loops.
- Ensure that directory structures are logical and do not contain excessive nesting.
- Monitor backup logs for any unusual entries that may indicate issues with directory structures.

## Actions Taken
- HPC Admin notified the user about the directory loop.
- User deleted the unnecessary nested directories.
```
---

### 2024031842001328_Backup%20HPCVAULT.md
# Ticket 2024031842001328

 ```markdown
# HPC Support Ticket: Backup HPCVAULT

## Keywords
- HPCVAULT
- Backup
- Snapshots
- Access
- Folder

## Problem
User wants to access the backup of the folder `$HPCVAULT/sgmse_mss`.

## Solution
The backup system operates under the concept of snapshots. The user can find detailed instructions on how to access these snapshots in the following documentation: [Snapshots for Home and HPCVAULT](https://doc.nhr.fau.de/data/filesystems/?h=snapshots#snapshots-for-home-and-hpcvault).

## General Learnings
- **Snapshots**: Understanding the concept of snapshots is crucial for accessing backups.
- **Documentation**: Always refer users to the relevant documentation for detailed instructions.
- **HPCVAULT**: Familiarize yourself with the structure and backup mechanisms of HPCVAULT.

## Roles Involved
- **HPC Admins**: Provided the solution and documentation link.
- **User**: Requested access to backup.

## Root Cause
User was unaware of the snapshot mechanism for accessing backups in HPCVAULT.

## Resolution
Provided the user with the link to the documentation explaining snapshots for HPCVAULT.
```
---

### 2021062342001327_Speicher%20auf%20Saturn.md
# Ticket 2021062342001327

 ```markdown
# HPC-Support Ticket Conversation: Storage on Saturn

## Keywords
- Storage deletion
- User data management
- Saturn HPC system
- Data backup

## Summary
A professor requested the deletion of data belonging to a former user on the Saturn HPC system. The data had already been backed up locally.

## Root Cause
- Former user's data needed to be deleted from the HPC system.

## Solution
- The HPC admin deleted the data from the specified directory.

## Conversation Details
- **User Request:** A professor requested the deletion of data for a former user who had not been at the university for over a year.
- **HPC Admin Response:** The admin confirmed the deletion of 14 TB of data from the specified directory.

## What Can Be Learned
- Proper communication and confirmation are essential when handling data deletion requests.
- Ensuring data backup before deletion is crucial to prevent data loss.
- HPC admins should verify and confirm the completion of deletion tasks.
```
---

### 2025021842002014_Backup%20of%20working%20directory%20in%20fritz%3F.md
# Ticket 2025021842002014

 # HPC Support Ticket: Backup of Working Directory

## Keywords
- Data recovery
- Backup
- Snapshots
- Accidental deletion
- `rm` command

## Problem
- **User Issue:** Accidental deletion of files in the working directory using the `rm *` command.
- **Affected Directory:** `/home/hpc/b169cb/b169cb12/Work/Higgs_Shapiro`

## Solution
- **User Action:** The user found and utilized the page on snapshots to recover the deleted data.
- **Outcome:** Successful data recovery.

## Lessons Learned
- **Importance of Snapshots:** Snapshots are crucial for recovering accidentally deleted data.
- **User Education:** Users should be aware of the snapshot feature and how to access it.
- **Quick Resolution:** Self-service options like snapshot documentation can help users resolve issues quickly without needing direct admin intervention.

## Recommendations
- **Documentation:** Ensure that documentation on snapshots is easily accessible and up-to-date.
- **User Training:** Conduct training sessions or provide guides on best practices for file management and data recovery.

## Follow-up Actions
- **Admin Response:** Acknowledge the user's successful recovery and offer further assistance if needed.
- **Future Prevention:** Encourage users to regularly back up important data and be cautious with commands like `rm`.

---

This documentation can serve as a reference for future incidents involving accidental data deletion and recovery using snapshots.
---

### 2018052042000298_Bitte%20um%20L%C3%83%C2%B6schung%20von%20Unterverzeichnis.md
# Ticket 2018052042000298

 # HPC Support Ticket: Bitte um Löschung von Unterverzeichnis

## Keywords
- Permission denied
- Symbolic links
- Directory deletion
- `rm -rf`
- `rpc_pipefs`

## Problem Description
The user encountered an issue where they were unable to delete a directory (`sandbox`) due to permission errors. The directory contained symbolic links and nested directories, leading to multiple "Permission denied" errors when attempting to delete it using `rm -rf`.

## Root Cause
The root cause of the problem was the presence of symbolic links and nested directories within the `sandbox` directory, which the user did not have permission to delete.

## Solution
The HPC Admin resolved the issue by deleting the directory. The specific steps taken by the admin are not detailed in the conversation, but it is implied that they had the necessary permissions to delete the problematic directory.

## Lessons Learned
- Users may encounter permission issues when attempting to delete directories containing symbolic links and nested directories.
- In such cases, HPC Admins can assist by deleting the directory with their elevated permissions.
- It is important to handle symbolic links and nested directories carefully to avoid permission issues.

## Next Steps
- If a user encounters a similar issue, they should contact HPC Support for assistance.
- HPC Admins should ensure they have the necessary permissions to delete directories with symbolic links and nested directories.
---

### 2023080442001356_URGENT%20Case%20%3A%20Erased%20Files%20and%20Folders.md
# Ticket 2023080442001356

 # HPC Support Ticket: URGENT Case - Erased Files and Folders

## Summary
User reported that critical files and folders for their Master Thesis were deleted without their action. The deletion occurred on 4 August 2023 at 03:30 AM.

## Root Cause
- User reported system failure and logged out/logged back in, noticing the deletion of important data.
- HPC Admins noted that they do not delete user files; the deletion must have been initiated by the user.

## Key Points
- **Backup Policy**: HPC officially does not provide a backup for `$work` directories.
- **TSM Backup**: Backups are performed every Monday, Wednesday, and Friday.
- **User Actions**: User attempted to recover files but lacked authorization.

## Actions Taken
1. **Initial Response**: HPC Admin acknowledged the issue and started the recovery process.
2. **Recovery Attempt**: Admin checked for recent backups and restored available data.
3. **User Instructions**: User was instructed to move recovered data to their regular directories.
4. **Follow-up**: Admin provided updates on the recovery status and ensured the user moved necessary files.

## Solution
- **Recovery**: Admin restored a version of the user's directory from earlier in the week.
- **User Action**: User was instructed to move any needed data to their regular directories.
- **Deadline**: Admin set a deadline for the user to move files before the restored directory was deleted.

## Lessons Learned
- **Backup Awareness**: Users should be aware of the backup policy and ensure critical data is stored in backed-up locations.
- **Communication**: Clear communication between the user and support team is crucial for resolving issues promptly.
- **System Logs**: Investigate system logs to identify the cause of unexpected deletions.

## Recommendations
- **Regular Backups**: Encourage users to regularly back up critical data.
- **Documentation**: Ensure users are aware of the backup policy and procedures for data recovery.
- **Support**: Provide clear instructions and support for users experiencing data loss.

## Conclusion
The issue was partially resolved by restoring available backups. The user was instructed to move necessary files to their regular directories. The root cause of the deletion remains unclear, but the support team provided assistance to mitigate the impact on the user's work.
---

### 2024070942001918_Assistance%20required%20to%20recover%20deleted%20folder.md
# Ticket 2024070942001918

 ```markdown
# HPC-Support Ticket: Assistance Required to Recover Deleted Folder

## Keywords
- Folder Recovery
- Backup Restoration
- Deleted Data
- HPC Support

## Problem Description
- **User Issue**: A user accidentally deleted a folder containing important data.
- **Folder Details**:
  - Folder Name: `fancy_index`
  - Location: `/home/woody/iwal/iwal141h`
  - Date of Deletion: 08/July/2024

## Root Cause
- The user deleted the folder `fancy_index` from their HPC directory.

## Solution
- **HPC Admin Actions**:
  - Attempted to restore the folder using the `dsmc restore` command.
  - Initially, the folder was not found in the backup.
  - Successfully restored the folder using the `-inactive` flag for deleted data.
- **Restored Location**: `/home/woody/iwal/iwal141h/fancy_index_restore`

## Recommendations
- **Backup Policy**: Inform the user that the `woody` directory does not have a regular backup.
- **Data Storage**: Recommend storing important data in `/home/vault` for better backup coverage.
- **Backup Information**: Provide the user with the link to the backup documentation: [Backup Information](https://doc.nhr.fau.de/data/filesystems/)

## Lessons Learned
- **Backup Commands**: Use the `-inactive` flag with `dsmc restore` to recover deleted data.
- **User Education**: Educate users about the importance of storing data in directories with regular backups.
- **Documentation**: Ensure users are aware of the backup policies and directories with backup coverage.

## Ticket Closure
- The user confirmed the successful restoration of the folder and expressed gratitude for the prompt assistance.
- The ticket was closed after the user's confirmation.
```
---

### 2021012142000939_hpc%20storage.md
# Ticket 2021012142000939

 # HPC Storage Backup Options Clarification

## Keywords
- HPC Storage
- Backup Options
- Disk Failure
- Human Error
- Snapshots
- Active Files
- Deleted Files
- Vorhaltezeit

## Summary
A user inquired about the backup options for HPC storage, specifically whether they protect against disk failure or human error. The HPC Admin clarified that all options provide safety against disk failure due to the use of disk RAID and that the backups are intended to protect against human error by saving multiple versions of active and deleted files for a specified period.

## Root Cause
User confusion about the purpose and scope of the backup options for HPC storage.

## Solution
The HPC Admin confirmed that the backup options are designed to protect against human error by maintaining multiple versions of files. All options also provide safety against disk failure due to the use of disk RAID.

## What Can Be Learned
- **Backup Options**: The backup options for HPC storage are primarily intended to protect against human error by saving multiple versions of active and deleted files.
- **Disk Failure Protection**: All backup options provide safety against disk failure due to the use of disk RAID.
- **Clarification**: Users should be informed that the backup options are not solely for disk failure protection but also for version control and recovery from accidental deletions or modifications.

## Additional Notes
- **No Backup Option**: Only snapshots on disk if desired.
- **Minimal Backup**: 2 versions of active files, 1 version of deleted files, 30/30 days retention.
- **Extended Backup**: 5 versions of active files, 2 versions of deleted files, 60/120 days retention.

This information can be used to clarify similar queries about HPC storage backup options in the future.
---

### 2019061242000219_Emmy%3A%20Bad%20Address.md
# Ticket 2019061242000219

 # HPC-Support Ticket: Emmy - Bad Address

## Keywords
- Bad address
- File creation
- File deletion
- Error message
- Emmy cluster
- User account

## Problem Description
Users encounter a "Bad address" error when creating or deleting files/directories on the Emmy cluster. Despite the error, the operations are successful.

## Root Cause
The exact root cause is not specified in the conversation, but it appears to be related to file system operations on the Emmy cluster.

## Solution
No solution is provided in the conversation. Further investigation by HPC Admins or 2nd Level Support is required.

## General Learnings
- Users may encounter "Bad address" errors during file operations.
- Despite the error, the operations may still be successful.
- Further investigation is needed to identify and resolve the underlying issue.

## Next Steps
- HPC Admins or 2nd Level Support should investigate the file system and user accounts to identify the cause of the "Bad address" error.
- If the issue persists, consider escalating to the Head of the Datacenter or the Training and Support Group Leader for additional resources.
---

