# Topic 4: quota_storage_data_directory_files

Number of tickets: 408

## Tickets in this topic:

### 2024071742002081_Request%20about%20increasing%20the%20volume%20of%20%24WORK.md
# Ticket 2024071742002081

 ```markdown
# HPC Support Ticket: Request to Increase $WORK Volume

## Keywords
- $WORK folder
- Volume increase
- Genomic data
- .fastq.gz, .bam, .loom formats
- Temporary files

## Summary
A user requested an increase in the volume of their $WORK folder to 3TB for handling large genomic data files and temporary files generated during processing.

## Problem
- User needed more storage space for genomic data processing.
- Initial request was sent from an unregistered email address.

## Solution
- HPC Admin verified the user's account and increased the $WORK folder volume to 3TB.
- User was advised to use the registered email address for future communications.

## Lessons Learned
- Always use the registered email address for support requests.
- Provide detailed information about the data types and processing requirements when requesting storage increases.
- HPC Admins can adjust storage quotas based on justified needs.
```
---

### 42320493_HPC%20Quota.md
# Ticket 42320493

 # HPC Quota Issue

## Keywords
- HPC Quota
- Block Quota
- Soft Quota
- Hard Quota
- Grace Period
- Filesystem /home/vault

## Problem
- User reports sudden quota exceedance despite inactivity.
- Possible cause: Account transition and data transfer from old account to new account.

## Symptoms
- User receives notification of quota exceedance.
- Quota report shows blocks used exceeding soft quota.

## Quota Report Details
- **Blocks used:** 214,428,384 (214.4G)
- **Blocks quota soft:** 204,858,368 (204.9G)
- **Blocks quota hard:** 409,715,712 (409.7G)
- **Blocks grace remaining:** 6 days

## Solution
- User needs to reduce data usage below the soft quota (204.9G) within the grace period (6 days).
- If data transfer from old account is the cause, user should be given additional time to manage the data.

## General Learning
- Regularly check quota usage to avoid sudden exceedance.
- Be aware of account transitions and their impact on quota.
- Understand the difference between soft quota, hard quota, and grace period.

## Next Steps for Support
- Verify if the account transition is the root cause.
- Provide user with guidance on managing and reducing data usage.
- Extend grace period if necessary to allow user time to comply with quota limits.
---

### 2020022042000351_Quota%20increase%20on%20%24HOME%20%28gwgi18%20on%20meggie%29.md
# Ticket 2020022042000351

 # HPC Support Ticket: Quota Increase on $HOME

## Subject
Quota increase on $HOME (gwgi18 on meggie)

## User Issue
- User exceeded $HOME quota by 0.6 GB after a package update.
- Requested quota increase to 15 GB to keep all software installations in one place.

## HPC Admin Response
- Policy: No quota extensions for $HOME due to high cost and limited space.
- Exception made due to upcoming $HOME replacement, quota increased to 12 GB.

## Root Cause
- User's $HOME quota was exceeded due to a large NCL build.

## Solution
- Quota temporarily increased to 12 GB.
- User agreed to remove personal NCL build after resolving software issues.

## Software Issue
- NCL build did not have ESMF regridding functions.
- ESMF module compiled with Intel MPI failed without mpirun.

## Troubleshooting
- HPC Admin provided two solutions:
  1. Use NCL with ESMF without MPI.
  2. Use OpenMPI variants for both NCL and ESMF.
- User confirmed Solution 2 worked for their scripts.

## Follow-up
- HPC Admin decided to keep the Intel MPI version of ESMF with a warning message.
- User will inform their group about the working combinations for ESMF.

## Keywords
- Quota increase
- $HOME
- NCL
- ESMF
- Intel MPI
- OpenMPI
- Software modules
- Temporary exception
- Snapshots
- Space reserves

## General Learning
- Quota extensions are generally not allowed due to cost and space constraints.
- Software issues may require specific module combinations to function correctly.
- Communication and collaboration between users and HPC admins are essential for resolving complex software issues.
---

### 2024070142004662_Request%20for%20Shared%20Folder%20Access%20on%20HPC%20Cluster.md
# Ticket 2024070142004662

 # HPC Support Ticket: Request for Shared Folder Access on HPC Cluster

## Keywords
- Shared folder access
- Access control
- Disk quota
- ACL
- POSIX permissions

## Problem
- User requests access to a shared folder for multiple students.
- Access needs to be restricted to students who have completed an online training course.
- Inquiry about disk quota for students within the shared folder.

## Root Cause
- Need for controlled access to a shared dataset to save storage space.
- Requirement to restrict access based on training completion.

## Solution
- **Access Control:**
  - Use ACL (Access Control Lists) for fine-grained permissions: [ACL Documentation](https://doc.nhr.fau.de/data/share-perm-nfs)
  - Alternatively, use POSIX permissions for basic access control: [POSIX Permissions Documentation](https://doc.nhr.fau.de/data/share-perm-posix/)
- **Disk Quota:**
  - Refer to the default quotas documentation: [Filesystems Documentation](https://doc.nhr.fau.de/data/filesystems)

## General Learnings
- Users can manage folder permissions using ACL or POSIX permissions.
- Default disk quotas are documented and can be referenced for storage management.
- Restricting access based on specific criteria (e.g., training completion) can be managed through ACL.

## Next Steps
- Implement ACL or POSIX permissions to restrict access to the shared folder.
- Review the default disk quotas to ensure sufficient storage for the dataset.
- Delegate the task of downloading the dataset to a designated student.
---

### 2024022842002908_Memory%20in%20Vault.md
# Ticket 2024022842002908

 ```markdown
# HPC-Support Ticket: Memory in Vault

## Keywords
- Memory usage
- Quota
- Vault
- Work directory
- Home directory
- Sparse files
- Block size

## Summary
A user noticed an unexpected increase in memory usage when moving files from their work directory to the vault. The user was also receiving quota exceedance emails.

## Root Cause
1. **Misunderstanding of Directories**: The user mistakenly thought the quota emails were about the work directory (`/home/atuin/b110dc/b110dc10`) instead of the home directory (`/home/hpc/b110dc/b110dc10`).
2. **Sparse Files**: The increase in memory usage was likely due to the copying of sparse files, which expanded in size when moved using simple tools like `cp` or `mv`.

## Solution
1. **Clarification of Directories**: The HPC Admin clarified that the quota emails were about the home directory, not the work directory.
2. **Sparse Files Handling**: The HPC Admin explained the concept of sparse files and how they can expand in size when moved with simple tools. The user was advised to use tools that handle sparse files correctly.

## General Learnings
- **Quota Management**: Understand the difference between home and work directories and their respective quotas.
- **Sparse Files**: Be aware of sparse files and use appropriate tools to handle them to avoid unexpected increases in memory usage.
- **Checking Usage**: Use commands like `df -h` to check the total usage of a project directory.

## Additional Notes
- **Temporary Data Storage**: The HPC system temporarily stores data twice for redundancy, which can affect the displayed quota.
- **Project Quota**: The project has a shared quota, and individual user usage can be checked by the HPC Admin if needed.
```
---

### 42197334_Quota%20auf%20Woody.md
# Ticket 42197334

 # HPC Support Ticket: Quota auf Woody

## Keywords
- Quota
- Woody Cluster
- Storage Limitation
- Quota Increase
- Filesystems

## Problem
- User encountered storage quota limitations on the Woody Cluster while working on their doctoral thesis.
- Initial request was to increase quota on `/home/hpc/capn/`.

## Root Cause
- User mistakenly referred to a softlink path.
- Actual storage location was `/home/woody/capn/mpp460` or `wnfs1:/srv/home`.
- User required additional 350GB for their next work steps.

## Solution
- HPC Admin clarified that `/home/hpc/capn/` is not intended for large data storage and quota increase is not possible there.
- Suggested using `/home/vault` or `/home/woody` for higher default quotas and potential quota increases.
- User's quota on `/home/woody` was increased from 250GB to 600GB soft / 1200GB hard.

## General Learnings
- Understand the intended use and quota policies of different filesystems on the HPC cluster.
- Verify the correct storage path when requesting quota increases.
- Documentation on filesystems and quotas is available at [HPC Environment Filesystems](http://www.rrze.uni-erlangen.de/dienste/arbeiten-rechnen/hpc/systeme/hpc-environment.shtml#fs).

## Follow-up
- Ensure users are aware of the appropriate storage locations for their data needs.
- Provide clear guidelines on requesting quota increases and the conditions under which they are granted.
---

### 2024070142003618_Deleting%20files%20responsible%20for%20HPC%20Quota.md
# Ticket 2024070142003618

 # HPC Support Ticket: Deleting Files Responsible for HPC Quota

## Keywords
- HPC Quota
- Home Directory
- Temporary Directory
- Filesystem
- Cleanup
- Network Filesystem
- Huggingface Cache

## Problem Description
The user encountered a quota issue on the HPC system, receiving warnings about being over quota on the `/home/hpc` filesystem. The user suspected that storing large language models (LLMs) in the home directory without using a temporary directory caused the issue.

## Root Cause
The user stored large datasets in the `/home/hpc/amos/amos106h/.cache/huggingface` directory, which filled up the home directory and exceeded the quota.

## Solution
1. **Identify the Affected Account**: The user provided the affected account name (amos106h).
2. **Clean Up Home Directory**: The user was advised to move the large datasets from the home directory to the `$WORK` directory.
3. **Use Temporary Directories**: The user was reminded to use temporary directories for large datasets to avoid filling up the home directory.

## General Learnings
- **Home Directory Quota**: The home directory has a quota that can be exceeded if large files are stored there.
- **Temporary Directories**: Use temporary directories for large datasets to avoid filling up the home directory.
- **Network Filesystem**: The home directory is a network filesystem shared with all frontends/nodes, allowing cleanup from anywhere.
- **Documentation**: Refer to the HPC documentation for more information on filesystems and quotas.

## References
- [HPC Filesystems Documentation](https://doc.nhr.fau.de/data/filesystems)

## Roles Involved
- **HPC Admins**: Provided guidance on identifying the affected account and moving large datasets.
- **User**: Reported the issue and followed the instructions to resolve the quota problem.

## Conclusion
The user was able to resolve the quota issue by moving large datasets from the home directory to the `$WORK` directory. This solution helps maintain the home directory within its quota limits and ensures smooth operation of the HPC system.
---

### 2021102942001362_Quota%20exceeded%20auf%20TITAN.md
# Ticket 2021102942001362

 # HPC Support Ticket: Quota Exceeded on TITAN

## Keywords
- Quota exceeded
- /home/titan/mfbi/
- Group quota
- Soft quota
- Hard quota
- File quota
- Grace period

## Problem Description
- User reported a "quota exceeded" error on `/home/titan/mfbi/`, preventing the creation of new directories.
- Despite deleting data, the issue persisted.
- The `quota` and `shownicerquota.pl` commands did not show an overrun of the quota, and `/home/titan` was not listed.

## Root Cause
- The group `mfbi` exceeded their soft quota for more than 7 days, turning it into a hard quota.
- The quota script for sending notifications was broken, preventing the master user from being informed.

## Solution
- The HPC Admin reset the grace period.
- The user was advised to check the group quota explicitly using `quota -g`.
- Additional free space was allocated to the group.

## Lessons Learned
- Always check group quotas explicitly using `quota -g` when dealing with group-specific quotas.
- Be aware of the transition from soft quota to hard quota after the grace period.
- Ensure that notification scripts are functioning correctly to alert users of quota issues.

## Actions Taken
- HPC Admin reset the grace period.
- HPC Admin fixed the quota script for sending notifications.
- Additional free space was allocated to the group.

## Follow-up
- Ensure that users are aware of their group quotas and the consequences of exceeding them.
- Regularly check and maintain notification scripts to prevent communication breakdowns.
---

### 2021050342003203_Quota%20AG%20Imhof.md
# Ticket 2021050342003203

 # HPC Support Ticket: Quota Adjustment for Research Group

## Keywords
- Quota adjustment
- $VAULT
- $WOODYHOME
- RTX3080-Knoten
- TinyGPU

## Summary
A research group requested quota adjustments for their members due to insufficient storage space. The HPC admins increased the quota for the specified users and directories.

## Root Cause
- Insufficient quota on $VAULT and $WOODYHOME directories for the research group members.
- User's running calculations on RTX3080-Knoten on TinyGPU were at risk of being terminated due to exceeding quota limits.

## Solution
- HPC Admin increased the quota for the affected users (bco123, bccc020h) on $VAULT to 1TB.
- HPC Admin increased the quota for the user on $WOODYHOME to 750GB to accommodate running calculations on RTX3080-Knoten on TinyGPU.

## Lessons Learned
- Regularly monitor quota usage and request adjustments proactively to avoid disruptions in research work.
- Communicate clearly with HPC support regarding specific quota needs and the urgency of the request.

## Follow-up Actions
- Users should confirm that the increased quota meets their needs.
- HPC admins should monitor the usage to ensure that the allocated quota is sufficient and adjust as necessary.

## Relevant Contacts
- HPC Admins: For quota adjustments and related issues.
- 2nd Level Support Team: For additional support and troubleshooting.
- Georg Hager: Training and Support Group Leader for further assistance.

## Conclusion
Effective communication and timely action by HPC admins resolved the quota issue, ensuring uninterrupted research activities for the group. Regular monitoring and proactive requests can prevent similar issues in the future.
---

### 2024041842002371_Permission%20to%20share%20files%20among%20users%20in%20the%20same%20project%20group.md
# Ticket 2024041842002371

 # HPC Support Ticket: Sharing Files Among Users in the Same Project Group

## Keywords
- File sharing
- Permissions
- Project group
- Storage quota
- POSIX permissions
- NFS permissions

## Problem
- **Root Cause:** Users in the same project group need to share local files to optimize storage quota usage but lack permissions to access each other's directories.

## Solution
- **Documentation Reference:** The workflow is supported as documented at [Granting Read Access to Members of Your Group](https://doc.nhr.fau.de/data/share-perm-posix/#granting-read-access-to-members-of-your-group).
- **Additional Resources:** For more complex use cases, refer to [Additional Alternatives](https://doc.nhr.fau.de/data/share-perm-nfs/).

## General Learning
- Users should be directed to the appropriate documentation for setting POSIX permissions to share files within their project group.
- For advanced sharing needs, NFS permissions can be explored.
- Ensure users are aware of the documentation and resources available for managing file permissions and sharing.

## Next Steps
- If the provided documentation does not resolve the issue, further assistance from the HPC Admins or the 2nd Level Support team may be required.
- Users should contact support if they encounter any difficulties in implementing the suggested solutions.

---

This documentation aims to assist support employees in resolving similar issues related to file sharing and permissions within project groups.
---

### 2016032942001779_Speicherplatz%20auf%20woody.md
# Ticket 2016032942001779

 # HPC Support Ticket: Storage Quota Increase Request

## Keywords
- Storage quota
- Soft limit
- Hard limit
- HPC resources
- Quota change
- Formular

## Summary
A user reached the soft limit of their storage quota on the HPC system and requested an increase.

## Root Cause
- User reached the soft limit of 1 TB on the HPC system.
- User's current project requires significantly more storage space.

## Conversation Details
- **User Request**: Requested an increase in storage quota due to reaching the soft limit.
- **Initial Admin Response**: Incorrectly advised the user to fill out a form for resource changes.
- **Correction**: Another admin corrected the initial response, stating that no form is required for quota changes.
- **Resolution**: The user's quota was increased to 1.5 TB soft limit and 3 TB hard limit.

## Solution
- The user's storage quota was increased to 1.5 TB soft limit and 3 TB hard limit without the need for additional forms.

## General Learnings
- Quota changes do not require filling out a form.
- Ensure correct information is provided to users regarding quota changes.
- Address and resolve user requests promptly to avoid disruptions in their projects.

## Actions Taken
- Increased the user's storage quota to meet project requirements.
- Corrected misinformation provided to the user.

## Notes
- Ensure user contact information is up-to-date in the system.
- Provide clear and accurate instructions to users regarding resource changes.
---

### 2020012842000731_Ordner%20f%C3%83%C2%BCr%20tempor%C3%83%C2%A4re%20Rasterfiles%20auf%20SATURN.md
# Ticket 2020012842000731

 # HPC-Support Ticket: Temporary Directory for Raster Files on SATURN

## Keywords
- Raster data processing
- R package
- Temporary directory
- Permission denied
- .Renviron file
- RAM usage

## Problem Description
The user is processing large amounts of raster data (Geotiff) using the `raster` package in R on TinYEth. The package creates temporary files on the disk when data cannot be stored in RAM. The default location for these files is the small disk of the TinYEth node, leading to frequent disk space exhaustion and processing interruptions.

## Root Cause
- The user attempted to set a temporary directory on SATURN with larger storage capacity but encountered permission issues.
- The user tried to manually change the temporary directory in R, resulting in a "Permission denied" error when attempting to write to the `.Renviron` file.

## Troubleshooting Steps
1. **HPC Admin** suggested that the `write` statement in R is attempting to write the value of `TMPDIR` to the `.Renviron` file.
2. The error message indicated that the file was being sought in the root directory (`/`), which is not writable by the user.
3. **HPC Admin** mentioned that `$TMPDIR` should be set within batch jobs but noted that it might not be set on all systems.
4. **HPC Admin** suggested that R might look for the `.Renviron` file in `$HOME` or the current working directory, but not in `$TMPDIR`.

## Solution
The user discovered that the issue was related to the definition of maximum RAM usage in R, which was causing the behavior. The problem was resolved by adjusting the RAM usage settings in R.

## Lessons Learned
- Ensure that temporary directories have the appropriate permissions for writing.
- Verify that environment variables like `$TMPDIR` are correctly set within batch jobs.
- Check R settings for RAM usage when processing large datasets.
- Understand where R looks for configuration files like `.Renviron`.

## Conclusion
The issue was resolved by the user by adjusting R settings related to RAM usage. No further action was required from the HPC support team.
---

### 2022051942000014_Berechtigungen%20Ablageordner%20_%20Quota%20Klima-Gruppe.md
# Ticket 2022051942000014

 # HPC-Support Ticket Conversation Summary

## Subject: Berechtigungen Ablageordner / Quota Klima-Gruppe

### Keywords:
- Berechtigungen
- Quota
- Archivierung
- chown
- NHR-Rechenzeitantrag
- Storagebedarf

### General Learnings:
- **Permission Transfer**: The user requested to transfer all file permissions in a specific folder to the group leader.
- **Quota Increase**: The user inquired about increasing the storage quota due to upcoming data requirements.
- **Archiving Issues**: The user faced issues with archiving files due to permission restrictions.
- **NHR Application**: The HPC Admin suggested applying for additional storage through an NHR-Rechenzeitantrag.

### Root Cause of the Problem:
- **Permission Issue**: The user needed all file permissions in the folder `gwgkfu0h` to be transferred to the group leader `gwgk02` to facilitate archiving.
- **Quota Limitation**: The user's group was approaching their storage quota limit and needed additional space for ongoing projects.

### Solution:
- **Permission Transfer**: The HPC Admin initiated a `chown` process to transfer file permissions.
- **Quota Increase**: The HPC Admin temporarily increased the quota from 225 TB to 235 TB and suggested applying for additional storage through an NHR-Rechenzeitantrag.

### Detailed Conversation:
1. **User Request**:
   - Transfer file permissions in the folder `gwgkfu0h` to the group leader `gwgk02`.
   - Increase the storage quota from 225 TB due to upcoming data requirements.

2. **HPC Admin Response**:
   - Initiated a `chown` process to transfer file permissions.
   - Temporarily increased the quota to 235 TB.
   - Suggested applying for additional storage through an NHR-Rechenzeitantrag.

3. **Follow-up**:
   - The `chown` process was completed.
   - The user was advised to wait for the process to finish before archiving.
   - The HPC Admin noted that a new server system is not yet available and will inform the user once it is operational.

### Recommendations for Future Support:
- **Permission Transfer**: Use the `chown` command to transfer file permissions when requested by users.
- **Quota Management**: Temporarily increase quotas if necessary and advise users to apply for additional storage through an NHR-Rechenzeitantrag.
- **Archiving**: Ensure users have the necessary permissions to archive files to avoid delays and additional communication.

### Additional Resources:
- [NHR Application Rules](https://hpc.fau.de/systems-services/systems-documentation-instructions/nhr-application-rules/)
---

### 42071904_Daten%20auf%20inaktivem%20Account.md
# Ticket 42071904

 # HPC-Support Ticket: Access to Data on Inactive Account

## Keywords
- Data access
- Inactive account
- Zustimmung (consent)
- Quota
- Archivierung (archiving)
- tar/gzip

## Problem
- User requests access to data on an inactive student account.
- Alternative suggestion: extend account for 2 months.

## Solution
1. **Formal Consent**: HPC Admin requires formal consent from the account owner to grant access.
2. **Data Transfer**: Once consent is given, data is transferred to the user's account.
3. **Quota Management**: User is informed about potential quota exceedance and the need to request an extension if necessary.
4. **Data Archiving**: User compresses and moves data to a local drive, then deletes the original data.

## General Learnings
- Formal consent is required for accessing data on inactive accounts.
- Data transfer may impact user quota, necessitating quota management.
- Users can archive and move data using tools like tar/gzip.

## Roles
- **HPC Admin**: Manages data access and transfer, oversees quota management.
- **User**: Requests data access, archives and moves data, manages quota.

## Root Cause
- User needs access to data on an inactive account for archiving purposes.

## Resolution
- Obtain formal consent from the account owner.
- Transfer data to the user's account.
- Monitor and manage quota as needed.
- Archive and move data using tar/gzip.
---

### 2024021942002621_Storage%20Quota%20Request.md
# Ticket 2024021942002621

 # Storage Quota Request

## Keywords
- Storage quota
- HPC support
- Group storage
- Backup storage
- Temporary storage increase

## Summary
A user requested an increase in their storage quota due to project requirements. The HPC admins informed the user about available group storage and alternative backup options.

## Root Cause
- User required additional storage for a project.
- User was unaware of existing group storage and backup options.

## Conversation Details
- **User Request:** Increase storage quota to 750 GB or 1 TB.
- **HPC Admin Response:** Informed the user about 5TB of available group storage at `/home/janus/iwso-datasets` and inquired about the need for extra storage with backups.
- **User Clarification:** User agreed to use existing storage but requested temporary storage in their personal directory for important data.
- **HPC Admin Solution:** Suggested using `$HPCVAULT` for high-value data, which offers 500GB of space by default. Provided a link to documentation for more details.

## Solution
- Use existing group storage for most work.
- Use `$HPCVAULT` for important data that requires backups.
- Temporary increase in personal storage can be considered but should be downscaled after the project.

## Documentation Link
- [NHR@FAU Filesystems Documentation](https://doc.nhr.fau.de/data/filesystems/)

## Notes
- Users should use their `@fau.de` email address for contacting support.
- Group storage and backup options should be communicated to users to avoid unnecessary quota increase requests.
---

### 2023120142002031_Shared%20data%20folder.md
# Ticket 2023120142002031

 ```markdown
# Shared Data Folder Request

## Keywords
- Shared data folder
- Read/write access
- Vault directory
- User access

## Problem
- User requested a shared folder in the vault for all users of a specific group (mfsi) to access raw data.
- Need for both read and write access.

## Solution
- HPC Admins confirmed the possibility of creating such a directory.
- Directory `/home/vault/mfsi/shared` was created for shared access.
- User was informed about the availability of the shared directory.

## Lessons Learned
- HPC Admins can create shared directories for group access.
- Communication and coordination among HPC Admins are essential for timely resolution.
- Users should be informed about the availability and location of shared resources.
```
---

### 2017040642001693_Over%20quota%20_home_vault_capn_mpp128.md
# Ticket 2017040642001693

 # HPC Support Ticket: Over Quota /home/vault/capn/mpp128

## Keywords
- Quota
- Storage
- File Deletion
- Space Management

## Summary
A user reported exceeding their quota on `/home/vault/capn/mpp128`. Despite deleting approximately 15 GB of data, the used space did not decrease as expected.

## Root Cause
- The user deleted files but did not see a significant reduction in used space.
- Possible reasons include:
  - Delayed update of quota information.
  - Hidden or temporary files still occupying space.
  - Other processes writing to the directory.

## User Actions
- Deleted files totaling approximately 15 GB.
- Provided details of deleted files.

## HPC Admin Actions
- Acknowledged the issue.
- No specific solution provided in the given conversation.

## Solution
- Verify if there are any hidden or temporary files occupying space.
- Check for any running processes that might be writing to the directory.
- Wait for the quota system to update, as there might be a delay.

## General Learnings
- Quota systems may not update immediately after file deletion.
- Always check for hidden or temporary files when managing storage space.
- Ensure no processes are writing to the directory when troubleshooting quota issues.

## Next Steps
- If the issue persists, further investigation is needed to identify any hidden files or processes affecting the quota.
- Consider contacting higher-level support if the problem cannot be resolved with basic troubleshooting steps.
---

### 2021030442002886_Over%20quota%20on%20_home_hpc.md
# Ticket 2021030442002886

 # HPC Support Ticket: Over Quota on /home/hpc

## Keywords
- Quota
- Block Quota
- File Quota
- Hard Quota
- Soft Quota
- Grace Period
- Filesystem
- Parallel Filesystem
- Blocks in Doubt

## Problem Description
- Group 'iww1' exceeded both Block Quota and File Quota on `/home/hpc`.
- Block Quota: 0.0K (hard limit reached)
- File Quota: 0 files (hard limit reached)
- Current usage:
  - Blocks used: 112,022,336 (112.0G)
  - Files used: 617,245

## Root Cause
- The group has stored too much data and too many files, exceeding the allocated quota limits.

## Explanation
- **Blocks in Doubt**: Small values resulting from the parallel nature of the filesystem.
- **Soft Quota**: Can be exceeded for up to one week (grace period).
- **Hard Quota**: Absolute maximum that cannot be exceeded.

## Solution
- Reduce the amount of data and the number of files stored in `/home/hpc` to fall below the quota limits.

## Actions Taken
- Automated email notification sent to the group.
- Ticket closed by HPC Admin with a note to ignore the request.

## Lessons Learned
- Regularly monitor and manage storage usage to avoid exceeding quota limits.
- Understand the difference between soft and hard quotas, and the grace period for soft quotas.
- Be aware of the 'in doubt' values in a parallel filesystem and their impact on quota calculations.

## Next Steps
- If similar issues arise, advise users to delete unnecessary files and data to comply with quota limits.
- Provide guidance on efficient data management practices.
---

### 2016102542001174_%5BErg%C3%83%C2%A4nzung%5D%20Erweiterung%20des%20Speicherplatz%20im%20woody-Filesystem.md
# Ticket 2016102542001174

 ```markdown
# HPC Support Ticket: Increase Storage Space on Woody Filesystem

## Keywords
- Storage space
- Woody filesystem
- Softcap
- Formula Student project
- Star-CCM+
- Simulation
- Large file sizes

## Summary
A user requested an increase in storage space on the woody filesystem to a softcap of 250GB for their Formula Student project, which involves simulating the aerodynamics of a vehicle using Star-CCM+, resulting in large file sizes.

## User Request
- **Request:** Increase storage space on the woody filesystem to a softcap of 250GB.
- **Reason:** Simulation of vehicle aerodynamics for the Formula Student project using Star-CCM+, which generates large file sizes.
- **Identifiers:**
  - Customer ID: if50ejis
  - HPC ID: corz000h

## HPC Admin Response
- **Action:** The request was marked as completed.

## Root Cause
- The user required additional storage space to accommodate large simulation files generated by Star-CCM+ for their Formula Student project.

## Solution
- The HPC Admin increased the storage space on the woody filesystem to a softcap of 250GB as requested.

## General Learning
- Users may require increased storage space for specific projects that generate large file sizes.
- It is important to provide clear identifiers (Customer ID, HPC ID) when making such requests.
- HPC Admins can adjust storage quotas to meet user needs.
```
---

### 2023022242002439_Erweiterter%20Speicherbedarf%2C%20Alex%20Cluster.md
# Ticket 2023022242002439

 ```markdown
# HPC-Support Ticket: Extended Storage Requirement, Alex Cluster

## Keywords
- Storage quota
- Alex Cluster
- Data sets
- Project quota
- $WORK directory

## Problem
- User requires additional storage for a new dataset (350 GB) on top of the existing dataset (350 GB), exceeding the current quota.
- User requests an increase in storage quota to 1000 GB to accommodate both datasets.

## Solution
- HPC Admin informs the user that the project `b160dc` already has a 10 TB quota in the $WORK directory.
- No further action is required as the existing quota is sufficient for the user's needs.

## General Learnings
- Always check the current quota for the project before requesting an increase.
- The $WORK directory on the Alex Cluster has a significant storage allocation for projects.
- Communicate clearly with users about their current resource allocations to avoid unnecessary requests.
```
---

### 2024011842000636_%5BWoody%5D%20Quota%20Erweiterung%20-%20iwtm013h.md
# Ticket 2024011842000636

 # HPC Support Ticket Analysis

## Subject
[Woody] Quota Erweiterung - iwtm013h

## Keywords
- Quota Erweiterung
- Woody
- LAMMPS
- Simulation
- Soft Quota-Limit
- Temporäre Erhöhung

## Problem
- User's simulation with LAMMPS is data-intensive and exceeds the current soft quota limit.
- User requests a temporary increase in the soft quota limit to 3 Terabytes to avoid aborting the simulation.

## Solution
- HPC Admin increased the user's $WORK quota to 3TB.

## General Learnings
- Users may require temporary quota increases for data-intensive simulations.
- HPC Admins can adjust quotas to accommodate user needs.
- Clear communication of the user's requirements and the admin's actions is essential for efficient support.

## Actions Taken
- User requested a quota increase via email.
- HPC Admin responded and increased the quota as requested.

## Notes
- Ensure users provide their user ID (Benutzerkennung) for quick identification.
- Document the reason for quota increase requests for future reference.
---

### 2022031742001101_Zwischenfazit%20duplicity.md
# Ticket 2022031742001101

 # HPC Support Ticket Conversation Summary

## Subject: Zwischenfazit duplicity

### Keywords:
- duplicity
- rsync
- full backup
- incremental backup
- encryption
- compression
- inode usage
- quota
- NFS mount
- data migration

### General Learnings:
- **Backup Performance**: Full backups using duplicity are slower compared to rsync, especially for large volumes. Incremental backups are faster.
- **Encryption and Compression**: Disabling encryption and compression can improve backup speed, but the impact varies.
- **Inode Usage**: Duplicity can reduce inode usage by generating larger files.
- **Quota Management**: Temporary quota increases may be necessary during full backups to avoid warnings.
- **NFS Mount**: NFS can be used for direct mounting of backup directories, but proper configuration and permissions are crucial.
- **Data Migration**: Migrating data between filesystems can be managed server-side to speed up the process.

### Root Cause of Problems:
- **Slow Full Backups**: Large volumes and the need for encryption and compression contribute to slow full backups.
- **Quota Warnings**: Temporary increase in storage usage during full backups leads to quota warnings.
- **NFS Write Permissions**: Incorrect NFS export settings can prevent write access.

### Solutions:
- **Mixed Backup Strategy**: Use duplicity for smaller volumes and rsync for larger volumes to balance speed and efficiency.
- **Adjust Backup Settings**: Disable encryption and compression to improve backup speed.
- **Quota Management**: Plan for temporary quota increases during full backups.
- **NFS Configuration**: Ensure NFS export settings allow write access and use appropriate NFS versions.
- **Server-Side Data Migration**: Utilize server-side tools to migrate data efficiently.

### Specific Actions Taken:
- **Backup Strategy**: Switched from rsync to duplicity for better reliability and inode usage.
- **Quota Adjustment**: Temporarily increased quota to accommodate full backups.
- **NFS Mount**: Configured NFS mount for direct access to backup directories.
- **Data Migration**: Migrated backup directories server-side to a new filesystem.

### Conclusion:
The conversation highlights the importance of balancing backup strategies, managing quota effectively, and ensuring proper configuration of NFS mounts for efficient data management.
---

### 2024041742001999_Access%20to%20tape%20archive%20-%20b159cb.md
# Ticket 2024041742001999

 # HPC Support Ticket Conversation Summary

## Keywords
- Long-term tape storage
- Data archiving
- Quota extension
- Data testament
- Metadata
- Publication data
- NHR projects
- HPCVAULT
- $WORK

## General Learnings
- The HPC site provides long-term tape storage for archiving data.
- Users need to prepare data and metadata for archiving.
- Quota extensions can be requested for $WORK and HPCVAULT.
- A "data testament" is required for archiving, specifying access, deletion date, and notification upon deletion.
- Data should be compressed into ~100GB archives for efficient storage.
- The archiving process may require user interaction for data migration.

## Root Cause of the Problem
- User needs to archive large datasets (up to 36TB) for long-term storage due to upcoming publications.
- User exceeded quota on HPCVAULT and needs an extension to update data before archiving.

## Solution
- HPC Admins increased the user's quota on HPCVAULT by 10TB.
- User will prepare data and metadata for archiving as per the guidelines provided by HPC Admins.
- User will provide a "data testament" specifying access, deletion date, and notification upon deletion.
- User will compress data into ~100GB archives for efficient storage.
- User will inform HPC Admins once the data is ready for archiving.

## Additional Notes
- The tape library was installed in 2020, and data may need to be migrated to a different system or technology before 10 years.
- The archiving process may require user interaction, and financing for a follow-up system is not guaranteed.
- The HPC site is discussing different options for handling long-term data storage for NHR projects.
- The user's project runs until mid-next year, and the HPC Admins have no issue with the data remaining on HPCVAULT until then.
- The user will inform HPC Admins once the paper is published and the data is ready for archiving.
---

### 2023111342002448_Disk%20quota%20-%20iwgt005h.md
# Ticket 2023111342002448

 # HPC Support Ticket: Disk Quota Issue

## Keywords
- Disk quota
- Meggie
- OpenFOAM
- HPC accounts
- $HPCVAULT
- $WORK
- Storage filesystems

## Problem
- User facing difficulties with 100 GB quota on Meggie.
- Requested information on obtaining a second HPC account due to large OpenFOAM cases.

## Root Cause
- Misunderstanding about the disk quota limits and available storage options on the HPC system.

## Solution
- Clarified that there is no 100 GB quota on Meggie.
- Informed user about additional storage options:
  - 500 GB at `$HPCVAULT`
  - 500 GB at `$WORK`
- Provided link to documentation explaining different filesystems and backup policies: [HPC Storage Documentation](https://hpc.fau.de/systems-services/documentation-instructions/hpc-storage/)
- Offered possibility to increase quota at `$HPCVAULT` and `$WORK` if needed.

## General Learning
- Users may not be aware of all available storage options.
- Important to educate users about different filesystems and their respective quotas.
- Documentation and clear communication can resolve many quota-related issues.

## Next Steps
- Review and update storage documentation to ensure clarity.
- Consider proactive communication about storage options during user onboarding.
---

### 2023111642002371__scratch%20auf%20tinyx%20mal%20wieder%20komplett%20voll.md
# Ticket 2023111642002371

 ```markdown
# HPC Support Ticket: /scratch auf tinyx mal wieder komplett voll

## Keywords
- /scratch
- tinyx
- voll
- /tmp
- aufgeräumt

## Problem Description
- User reported that the /scratch directory on tinyx is completely full.

## Root Cause
- The /scratch directory was full due to excessive usage.

## Solution
- HPC Admin cleaned up the /tmp directory to free up space.

## Lessons Learned
- Regular monitoring and maintenance of temporary directories (/tmp) can help prevent storage issues in /scratch.
- Users should be encouraged to manage their storage usage effectively.
```
---

### 2024081242002811_File%20Quota%20Erh%C3%83%C2%B6hung%20%20unrz254%20auf%20Vault.md
# Ticket 2024081242002811

 # HPC Support Ticket: File Quota Increase Request

## Keywords
- File Quota
- Vault
- Backup
- Quota Increase
- mmlsquota
- shownicerquota.pl

## Summary
A user requested an increase in their file quota on the Vault storage system due to exhaustion of their current quota. The user was performing incremental backups of the job archives.

## Problem
- **Root Cause**: User's quota on Vault was perceived to be exhausted.
- **Symptoms**: User reported that their quota was full and requested an increase from 2TB to 4TB.

## Conversation Details
- **User Request**: The user requested a quota increase from 2TB to 4TB for their Vault storage.
- **HPC Admin Response**: The admin checked the quota using `mmlsquota` and found that the user's quota was not actually exhausted. The admin also mentioned that `shownicerquota.pl` had issues with large quota values, which would be fixed during the upcoming maintenance.

## Solution
- **Admin Action**: The admin confirmed that the user's quota was not exhausted and advised the user to ignore any quota warnings until the issue with `shownicerquota.pl` was resolved during the scheduled maintenance.
- **User Response**: The user acknowledged the admin's response and agreed to ignore the quota warnings for the time being.

## Lessons Learned
- **Quota Checking Tools**: `mmlsquota` is a reliable tool for checking quota usage.
- **Tool Limitations**: `shownicerquota.pl` may have issues with large quota values, and users should be aware of this limitation.
- **Communication**: Clear communication between users and admins is essential for resolving quota-related issues.

## Recommendations
- **Regular Maintenance**: Regular maintenance and updates are necessary to fix known issues with quota checking tools.
- **User Education**: Educate users about the limitations of certain tools and how to interpret quota usage reports.

## References
- [GitLab Issue for shownicerquota.pl](https://gitlab.rrze.fau.de/hpc/hpc-system-besprechung/-/issues/53)

## Conclusion
The issue was resolved by confirming the actual quota usage and advising the user to ignore warnings until the maintenance was completed. This ticket highlights the importance of accurate quota checking tools and clear communication between users and admins.
---

### 2022030242000701_Disk%20quota%20exceeded.md
# Ticket 2022030242000701

 # Disk Quota Exceeded Issue

## Keywords
- Disk quota exceeded
- HPCVAULT
- Group quota
- Checkpoints
- Tensorboard events
- $WORK

## Problem Description
- **User Issue:** The user encountered a "disk quota exceeded" error while trying to write checkpoints and tensorboard events on HPCVAULT from TMPDIR.
- **Root Cause:** The group quota for `iwbi` on `vault` was exceeded.

## Solution
- **Admin Response:** The group `iwbi` has reached its group quota of 5TB on `vault`.
- **Recommendation:** Use `$WORK` for writing checkpoints and tensorboard events instead of `HPCVAULT`.
- **Additional Information:** The HPC storage documentation can be found [here](https://hpc.fau.de/systems-services/systems-documentation-instructions/hpc-storage/).

## Follow-up
- **User Query:** How to check the group quota by themselves.
- **Admin Response:** Currently, users are unable to check group quota themselves. The space usage breakdown was provided:
  - 512 `iwbi001h`
  - 868G `iwbi002h`
  - 102G `iwbi003h`
  - 512 `iwbi004h`
  - 4.4T `shared`

## General Learning
- **Quota Management:** Understanding and managing group quotas is crucial to avoid disruptions in workflow.
- **Storage Usage:** Different file systems (`$WORK`, `HPCVAULT`) have specific use cases and should be utilized accordingly.
- **User Empowerment:** Providing users with tools or methods to check their own quotas can help in proactive management of storage resources.
---

### 2023092742001338_Data%20access%20to%20collaborators.md
# Ticket 2023092742001338

 # Data Access to Collaborators

## Keywords
- Data sharing
- File access lists
- Group permissions
- `chmod` command

## Problem
- User wanted to share access to files with a collaborator.
- User had difficulty understanding how to create file access lists.

## Solution
- HPC Admin suggested changing group permissions to share data with all users in the project.
- Command used: `chmod -R g+rX <directory>`

## What Can Be Learned
- Sharing data with collaborators can be achieved by modifying group permissions.
- The `chmod` command with the `g+rX` option allows read and execute permissions for the group.
- Documentation and guides are available for cross-using data between HPC accounts.

## Documentation Link
- [FAQ: Cross-use data between HPC accounts](https://hpc.fau.de/faqs/#i-would-like-to-cross-use-data-between-hpc-accounts)

## Root Cause
- User's difficulty in understanding how to create file access lists.

## Resolution
- Changing group permissions resolved the issue of sharing data with collaborators.
---

### 2024022742001769_Question%20about%3A%20%5BErrno%20122%5D%20Disk%20quota%20exceeded.md
# Ticket 2024022742001769

 ```markdown
# HPC Support Ticket: [Errno 122] Disk quota exceeded

## Keywords
- Disk quota exceeded
- OS error
- pip installation
- $HPCVAULT
- shownicerquota.pl
- maintenance issue

## Problem Description
- **User Issue:** The user encountered an OS error "[Errno 122] Disk quota exceeded" while attempting to install packages using pip in the $HPCVAULT directory.
- **User Action:** The user checked the quota using the `shownicerquota.pl` command and found that the actual storage space had not been exceeded.

## Root Cause
- **HPC Admin Response:** There was a temporary issue with quota computations due to recent maintenance.

## Solution
- **Resolution:** The issue was resolved by the HPC Admin team as of 10:50 on the same day. The user was advised to check the maintenance notice for more details.

## General Learning
- **Maintenance Impact:** Maintenance activities can cause temporary issues with quota computations.
- **User Actions:** Users should check for recent maintenance notices if they encounter unexpected quota issues.
- **Admin Actions:** Admins should communicate maintenance impacts and resolution timelines to users.

## References
- [Scheduled Downtime Notice](https://hpc.fau.de/2024/02/26/scheduled-downtime-of-nhrfau-systems-on-monday-february-26/)
```
---

### 2018042742001473_backup2tape.md
# Ticket 2018042742001473

 ```markdown
# HPC-Support Ticket: backup2tape

## Keywords
- HPC
- Directory
- Tape Storage
- Weather Forecast Model
- Backup

## Summary
A user inquires about the status of their directory (`/home/vault/gwgk/gwgk01/backup2tape`) which was set up for storing large input data for a weather forecast model on tape. The user suspects that their directory has not been backed up to tape yet.

## Root Cause
- The user suspects that their directory has not been backed up to tape.

## Solution
- The HPC Admin needs to verify the backup status of the directory and ensure that the data is being stored on tape as intended.

## General Learnings
- Users may need periodic confirmation that their data is being backed up as expected.
- Regular checks and communication regarding backup processes can prevent data loss concerns.
```
---

### 2021061742000714_L%C3%83%C2%B6schung%20von%20Dateien%20in%20_home_vault.md
# Ticket 2021061742000714

 # HPC Support Ticket: Deletion of Files in /home/vault

## Keywords
- HPC Cluster
- SSH
- File Deletion
- /home/vault
- File Quota
- Zipped Files
- Concurrent Scripts

## Problem Description
The user is experiencing the disappearance of small files transferred via SSH to their `/home/vault` directory on the HPC cluster. The files and eventually the entire directory are being deleted. This issue does not occur when transferring zipped files. The user suspects it is not related to file quota as they automatically zip the directories after transfer.

## Root Cause
The HPC Admin suggests that the issue might be caused by a concurrent script running on the user's account that is deleting the files.

## Solution
- Check for any running scripts or processes that might be deleting the files.
- Ensure no concurrent scripts are interfering with the file transfer and storage process.

## General Learnings
- Always verify if there are any concurrent scripts or processes that might be affecting file operations.
- Zipping files before transfer can help avoid issues related to file quota and potential deletion by concurrent scripts.

## Next Steps
- The user should investigate and stop any scripts that might be causing the deletion.
- If the issue persists, further investigation by the HPC Admin may be required.

## References
- HPC Services
- Regionales RechenZentrum Erlangen (RRZE)
- Friedrich-Alexander-Universitaet Erlangen-Nuernberg
---

### 2017052942000407_FW%3A%20iwst009h%3A%20Soft%20Quota-Limits%20auf%20_home_woody%20erreicht%21.md
# Ticket 2017052942000407

 # HPC Support Ticket Analysis: Quota Limits on /home/woody

## Keywords
- Quota limits
- Soft quota
- Hard quota
- Grace period
- Data management
- CFD simulations
- Ansys
- StarCCM+
- $FASTTMP
- $WOODYHOME
- VAULT

## Root Cause of the Problem
- User received daily emails about reaching soft quota limits on `/home/woody`.
- User needed more storage space for large simulation files generated by CFD simulations using Ansys and StarCCM+.
- Confusion about the implications of exceeding soft quota limits and the grace period.

## What Can Be Learned
- **Quota Limits**: Understanding the difference between soft and hard quota limits.
  - **Soft Quota**: Can be exceeded for a grace period (usually one week), after which no new files can be written until the usage is below the limit.
  - **Hard Quota**: Absolute maximum that cannot be exceeded.
- **Grace Period**: Files are not deleted after the grace period, but the user cannot write new files or update existing ones until the usage is below the soft quota.
- **Data Management**: Importance of managing large simulation files and understanding the storage options available on the HPC system.
- **Requesting Quota Increase**: Users should clearly state where and why they need a quota increase, along with their username.
- **Storage Locations**: Different filesystems have different purposes and properties. Users should choose the most appropriate one for their use case.

## Solution
- HPC Admin increased the user's quota on `/home/woody` to 75 GB soft and 150 GB hard.
- User agreed to monitor their usage and request further increases if necessary.
- User was advised to pick one filesystem that fits their use case, considering the explanatory 'purpose' column in the HPC environment documentation.

## Follow-up
- User will monitor their data usage and request further quota increases if needed.
- No prior information is provided about deleting files from `$FASTTMP` folders, so users should not rely on this for long-term storage.
---

### 2022022342002126_Data-Mount%20von%20FAU%20Externen%20Servern.md
# Ticket 2022022342002126

 # HPC-Support Ticket: Data-Mount von FAU Externen Servern

## Keywords
- Data Mount
- SSHFS
- Autofs
- Quota Anpassung
- Rsync
- HPC Storage
- Checkpoints

## Problem
- User lost GPU resources at Imperial College London due to a paper submission deadline.
- User requested to mount data from Imperial College HPC to FAU HPC using SSHFS or Autofs.
- Data transfer via download would take approximately 6 hours, which the user wanted to avoid.

## Root Cause
- User needed access to data from an external HPC system to meet a deadline.
- User's storage quota on FAU HPC was insufficient for their needs.

## Solution
- HPC Admins informed the user that mounting external servers is not possible due to technical reasons.
- HPC Admins suggested using `rsync` to copy data and offered to adjust the user's quota if necessary.
- User requested a quota increase to 200 GB on `/home/hpc`.
- HPC Admins denied the request for `/home/hpc` quota increase but informed the user about additional storage options:
  - 500 GB under `/home/vault` (`$HPCVAULT`)
  - 10 TB under `$SATURNHOME` for their working group
- HPC Admins advised the user not to store checkpoints on `$HOME` and to use other filesystems for that purpose.

## General Learning
- Mounting external servers on FAU HPC is not technically feasible.
- Users should be aware of and utilize the various storage options available on FAU HPC.
- Checkpoints should not be stored on `$HOME`; other filesystems should be used for this purpose.
- Quota adjustments can be requested, but the availability of other storage options should be considered.

For more information on FAU HPC storage systems, refer to the [HPC Storage Documentation](https://hpc.fau.de/systems-services/systems-documentation-instructions/hpc-storage/).
---

### 2021072942000226_HPC%20speicher.md
# Ticket 2021072942000226

 # HPC Support Ticket: Additional Storage Request

## Keywords
- DFG Antrag
- Speicherplatz
- NFS-Fileserver
- HPC-Hintergrundspeicher
- Serverrahmenvertrag
- Datensicherung
- Bandmedien
- RAID

## Summary
A user requested additional storage space (10-20 TB) for a DFG grant application to handle data from the "Retreat" project.

## Root Cause
- The user needed additional storage space for flexibility in handling project data.

## HPC Admin Response
- The current HPC systems (saturn and titan) have already used 2/5 of their lifespan, making them less suitable for new grant applications.
- Extending the HPC background storage would require significant infrastructure investment, making it cost-effective only for larger expansions (2-4 PB).
- A cost estimate based on the server framework contract was provided:
  - Approximately 80-90 EUR per TB for an NFS-Fileserver.
  - Additional 27.50 EUR per TB for data backup (tape media).
- Total estimated cost for 20 TB: 2,000 - 2,500 EUR.
- The HPC Admin advised that a service offer from the data center might not be suitable for DFG funding, and a server offer from the framework contract for 10-20 TB might not make sense due to the small number of hard drives involved.

## User Decision
- The user decided to opt for an NFS-Fileserver or an extension/update of their existing "Retreat" server, as it would be easier to justify in the grant application.

## General Learnings
- Consider the lifespan and scalability of current HPC systems when planning for additional storage.
- Cost estimates for storage should include both the storage itself and additional costs for data backup.
- Understand the funding guidelines for grant applications to ensure that the requested resources are eligible for funding.
- Provide clear justifications for the requested resources in grant applications.
---

### 2018090942000196_Quota.md
# Ticket 2018090942000196

 # HPC Support Ticket: Quota Increase Request

## Keywords
- Quota
- Temporary Increase
- Data Storage
- Project Completion
- NFS-Storage

## Summary
A user requested a temporary increase in their quota due to generating large amounts of data for a project and experiencing issues with their group's IT infrastructure.

## Root Cause
- User generating large data volumes for project completion.
- Issues with the user's group IT infrastructure preventing data offloading.

## Solution
- HPC Admin temporarily increased the user's quota from 300 GB to 700 GB for 4 weeks.
- After 4 weeks, the quota was reset to the original 300 GB.

## Additional Information
- HPC Admin reminded the user about an email regarding additional NFS-Storage options for groups.
- The email mentioned options for groups to purchase additional storage at specified costs.

## Lessons Learned
- Users may require temporary quota increases for project-specific data generation.
- HPC Admins can accommodate such requests within specified timeframes.
- Communication about additional storage options is important for users facing long-term data storage needs.

## Follow-Up Actions
- Monitor user quotas and be prepared to adjust them temporarily as needed.
- Ensure users are aware of additional storage options and costs.

## Relevant Email Excerpt
```
2) NFS-Work/Projekt-Storage

Sofern sich genügend Arbeitsgruppen beteiligen, wird das RRZE einen
preisoptimierten großen NFS-Storage beschaffen, auf den von allen
HPC-Systemen aus zugegriffen werden kann. Hinsichtlich
Zugriffsgeschwindigkeit und sonstiger Eigenschaften wäre dieser
NFS-Storage mit $WOODYHOME (=/home/woody/...) vergleichbar.
Entsprechend der Beteiligung werden Gruppen-Quotas gesetzt und der
neue NFS-Storage steht auch nur diesen Gruppen zur Verfügung. Die
Daten werden auf einem Hardware-RAID6 gespeichert, das den Ausfall
von bis zu zwei Festplatten gleichzeitig tolerieren kann. Ein
Backup der Daten (auf Tape) oder Snapshots sind *nicht* geplant.

Die Beschaffung würde durch das RRZE zentral erfolgen und
Arbeitsgruppen, die sich am Storage beteiligen, bekommen *einmalig*
eine Rechnung vom RRZE über "Bereitstellung von NFS-Speicherplatz".
Laufende Kosten fallen nicht an. Es wird von einer Standzeit von 5
Jahren ausgegangen.

Einmalige Kosten pro 25 TB: 5000 EUR
(geplanter Betriebsdauer: 5 Jahre)

Verbindliche Rückmeldungen bis spätestens Mitte September!
Gerne auch für mehr als 1x 25 TB.
Arbeitsgruppen, denen 25 TB zu viel (oder 5k EUR zu teuer) sind, können wir auch 10 TB für einmalig 2.500 EUR anbieten.
```
---

### 2020070342001418_Speicherung%20gr%C3%83%C2%B6%C3%83%C2%9Ferer%20Datenvolumen%20-%20Beratung.md
# Ticket 2020070342001418

 # HPC-Support Ticket: Storage and Transfer of Large Data Volumes

## Keywords
- Data storage
- Data transfer
- Video data
- Server costs
- Basis-Storage
- Archive
- FAU-Data-Cloud
- TSM-Archiv

## Problem
- User needs to store and manage approximately 100 TB of video data over 3-4 years.
- Data is generated at a rate of 8 TB every 3 months.
- Data needs to be accessible for analysis by students and possibly automated systems.

## Solutions Discussed
1. **Own Server**:
   - Cost: ~12,000 € for a server with 100 TB storage.
   - Monthly server maintenance: 84 €.
   - Optional backup: 0.01 € per GB.
   - Total cost for 3 years: ~15,024 € plus tax without backup.

2. **Basis-Storage**:
   - Cost: 10 € per 500 GB/month including backup.
   - Can be adjusted in 500 GB increments.
   - Cost for 1 TB per year: 240 €.

3. **Archive**:
   - Cost: 12 € base fee per year (includes 1 TB).
   - Additional cost: 1 € per TB per month.
   - GB-accurate billing.

4. **FAU-Data-Cloud**:
   - Potential solution through the FAU's planned data cloud.
   - Contact: agfd@lists.fau.de.

5. **Temporary Archive**:
   - Temporary write-only archive on available server space.
   - Cost: Similar to archive plus 1 TB Basis-Storage.

6. **TSM-Archiv**:
   - Attractive option for batch data.
   - Cost: ~300 € per 20 TB.
   - User becomes a test user for the new TSM-Archiv.

## Data Transfer
- Data should be transferred from the camera to a PC and then to the central storage.
- Cameras with network capabilities can directly store data on the share.

## Outcome
- User decided to use the TSM-Archiv as a test user.
- A TSM node (rrzearchiv-bcz2-eisbaeren) was created for the project.

## General Learnings
- Large data storage requirements need careful consideration of cost and accessibility.
- Different storage solutions (own server, Basis-Storage, archive) have varying cost structures and access speeds.
- Temporary solutions can be offered while waiting for long-term infrastructure.
- Clear communication about data usage and access requirements is crucial for finding the best solution.

## Next Steps
- Continue monitoring the TSM-Archiv usage.
- Evaluate long-term storage solutions as they become available.
- Ensure user is satisfied with the current storage and transfer methods.
---

### 2023122942000311_Extension%20of%20vault%20quota.md
# Ticket 2023122942000311

 # HPC Support Ticket: Extension of Vault Quota

## Keywords
- Vault quota
- Inode limit
- Data structuring
- 6D pose estimation
- 3D reconstruction
- High-resolution point clouds

## Summary
A PhD candidate requested an increase in vault storage quota for a large dataset used in 6D pose estimation and 3D reconstruction. The dataset size was over 650 GB, and the user needed the storage for approximately 9 months.

## Root Cause
- The user required additional storage space for a large dataset.
- The user was approaching the inode limit (number of files/directories) on the vault storage.

## Solution
- The HPC Admin increased the vault quota to 1 TB.
- The user was advised to restructure their data to avoid hitting the inode limit.
- The inode limit on vault was specified as 200,000 inodes.
- The user was provided with a link to tips on managing filesystems: [FAU Tips](https://www.fau.tv/clip/id/40199).

## Lessons Learned
- Users should be aware of both storage quota and inode limits.
- Proper data structuring is essential to manage large datasets efficiently.
- Quick response and clear communication from HPC support can help users manage their resources effectively.

## Next Steps
- Monitor the user's inode usage to ensure they stay within limits.
- Provide additional resources or training on data management if needed.

## References
- [FAU Tips on Filesystem Management](https://www.fau.tv/clip/id/40199)

## Roles Involved
- HPC Admins
- 2nd Level Support Team
- Head of the Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support
- Software and Tools Developer
---

### 2024010442000626_Request%20to%20Increase%20Block%20Quota%20on%20HPC%20-%20iwso102h.md
# Ticket 2024010442000626

 # HPC Support Ticket: Request to Increase Block Quota

## Keywords
- Block Quota
- Home Directory
- $WORK Directory
- Storage Management
- Quota Exceeded

## Problem
- User exceeded the block quota of 52.4 GB in the home directory (`/home/hpc/iwso102h`).
- The overage is due to large model files and datasets stored in the home directory.

## Root Cause
- Large files and directories consuming excessive space:
  - `/home/hpc/iwso/iwso102h/Master_thesis/dataset`: 5.7 GB
  - `/home/hpc/iwso/iwso102h/Master_thesis/output`: 43 GB
  - `/home/hpc/iwso/iwso102h/.cache`: 6.7 GB
  - `/home/hpc/iwso/iwso102h/.local`: 13 GB

## Solution
- The home directory quota is fixed and cannot be extended.
- Users should move large files to the `$WORK` directory, which has a higher quota.
- Refer to the [HPC Storage Documentation](https://hpc.fau.de/systems-services/documentation-instructions/hpc-storage/) for more information on managing storage.

## General Learning
- Home directories have a fixed quota that cannot be increased.
- Use the `$WORK` directory for storing large datasets and output files.
- Regularly monitor and manage storage usage to avoid quota issues.
- Refer users to relevant documentation and resources for storage management best practices.
---

### 42051758_LRZ%20accounts%20from%20Erlangen.md
# Ticket 42051758

 # HPC Support Ticket: LRZ Accounts from Erlangen

## Keywords
- LRZ accounts
- Home directory quota
- Shared home directory
- Disk space management
- Quota increase

## Problem
- User's home directory is full (50 GB out of 50 GB used).
- Home directory is shared among users from Erlangen University, making it difficult to identify who is using the most space.
- User cannot effectively use their account due to lack of space.

## Root Cause
- Shared home directory quota is exceeded due to collective usage by multiple users.
- Lack of individual quotas or visibility into usage by the master user.

## Solution
1. **Immediate Action**: HPC Admin deleted some data from their own account to free up 1.7 GB of space.
2. **User Action**: Some users deleted old files to free up additional space.
3. **Quota Increase**: The group quota was increased to 100 GB, with over 60 GB available after cleanup.
4. **Future Management**: Users were advised to keep their home directories within a fixed quota and to use the `sdf $HOME` command to check their quota.

## General Learnings
- Shared directories require regular management and communication among users to avoid exceeding quotas.
- Increasing quotas can provide temporary relief, but proper disk space management is essential for long-term sustainability.
- Administrators may need to request usage data from higher-level authorities (e.g., LRZ) to make informed decisions.

## Follow-up
- Regularly monitor and communicate disk space usage to prevent future issues.
- Consider implementing individual quotas if feasible.
---

### 2020040842002511_Inquiry%20about%20RRZE%20server.md
# Ticket 2020040842002511

 ```markdown
# HPC-Support Ticket Conversation Summary

## Subject: Inquiry about RRZE server

### Keywords:
- DFG proposal
- COMSOL Multiphysics
- Storage capacity
- Costs
- Licensing
- HPC servers
- Data management plan

### General Learnings:
- Basic usage of HPC systems at RRZE is free for scientific projects.
- Special hardware or additional storage capacity may incur costs.
- Licenses for application software must be purchased separately.
- Standard disk quota on the file system $WORK is 333 GB.
- HPC filesystems are not meant for long-term storage.
- Zenodo and NOMAD are good options for long-term data storage and sharing.

### Root Cause of the Problem:
- User needs information on using RRZE servers for COMSOL simulations and storage for a DFG proposal.

### Solution:
- **Storage Capacity:** Standard quota on $WORK is 333 GB. Additional storage options are available but depend on current hardware availability.
- **Costs:** Basic usage is free. Additional storage costs can be discussed based on current offerings.
- **Licensing:** COMSOL licenses must be purchased through software@rrze. Costs and surcharges apply for long-term rentals.
- **Recommended Servers:** Woody or TinyEth are recommended for COMSOL users.
- **Data Management Plan:** Zenodo and NOMAD are suggested for long-term storage and data sharing.

### Additional Notes:
- The user should describe planned computations and compute time demands for the DFG project.
- HPC-Services may offer long-term data archiving in the future, but details are not yet available.
```
---

### 2024111342001911_Quota%20Problem.md
# Ticket 2024111342001911

 # HPC Support Ticket: Quota Problem

## Summary
User transferred data between accounts but still receives quota warning emails.

## Keywords
- Quota
- Data Transfer
- Ownership
- `chown`
- `scp`
- `rsync`

## Root Cause
- Quota is determined by the owner of the files, not the file path.
- Transferring data without changing ownership does not affect quota.

## Solution
- Change the owner of the transferred files using `chown`.
- Use `scp` or `rsync` for data transfer to ensure proper ownership.

## Best Practice
- Use `scp` or `rsync` for data transfer to ensure proper ownership and quota calculation.
- Verify ownership and quota using provided scripts like `shownicerquota.pl`.

## Ticket Conversation

### User
- Transferred data between accounts but still receives quota warnings.
- Suspects metadata issue causing quota to remain full.

### HPC Admin
- Explained that quota is based on ownership, not file path.
- Suggested changing ownership using `chown`, which must be done by admins.
- Confirmed ownership change and provided current quota status.
- Recommended using `scp` or `rsync` for future transfers.

### User
- Requested ownership change for specific directories.
- Confirmed successful ownership change and resolution of quota warnings.

## Follow-up
- User encountered similar issue again, resolved by changing ownership of additional directories.
- HPC Admin provided best practice for data transfer and quota management.

## Documentation
- [Why is my data taking up twice as much space on the file systems?](https://doc.nhr.fau.de/faq/?h=faq#why-is-my-data-taking-up-twice-as-much-space-on-the-file-systems)
- `shownicerquota.pl` script for accurate quota display.
---

### 2015110342002697_Fragen%20zum%20Rechnen%20auf%20dem%20Cluster.md
# Ticket 2015110342002697

 ```markdown
# HPC Support Ticket: Questions about Computing on the Cluster

## Keywords
- STAR-CCM+
- Cluster storage
- Macros
- Report generation
- Quota
- Batch-Modus

## Summary
- **User Inquiry:**
  - Size of the directory (corz05) for storing simulations.
  - Possibility of using custom macros for automatic report generation.
- **HPC Admin Response:**
  - Quota for `$WOODYHOME = /home/woody/corz/corz05` increased to 250 GB / 500 GB.
  - STAR-CCM+ can execute macros and Java functions via command-line options.
  - No restrictions on using macros, but everything must run in batch mode without GUI.

## Root Cause
- User needed information on storage quota and capabilities for using macros in STAR-CCM+.

## Solution
- Quota increased to 250 GB / 500 GB.
- Confirmed that macros can be used in batch mode without GUI.

## General Learning
- **Storage Quota:** Users can request and receive increased storage quotas for their directories.
- **Macros in STAR-CCM+:** Custom macros and Java functions can be executed via command-line options in batch mode.
- **Batch Mode:** All operations must run in batch mode without a graphical user interface (GUI).
```
---

### 2023121242002948_Speicherkapazit%C3%83%C2%A4t%20nicht%20ausreichend%20-%20iwi9106h.md
# Ticket 2023121242002948

 # HPC Support Ticket: Insufficient Storage Capacity

## Keywords
- Storage capacity
- Quota increase
- Master's thesis
- Meggie Cluster
- /home/woody
- /home/vault

## Problem
- User received a dataset of approximately 720 GB for their Master's thesis.
- User needs to work on the Meggie Cluster and anticipates adding more data.
- Current storage capacity is limited to 500 GB (/home/vault/ & /home/woody/).

## Solution
- HPC Admin increased the quota on /home/woody to 1500 GB.

## General Learnings
- Users may require additional storage for large datasets and projects.
- Storage quotas can be increased upon request, especially for academic projects like Master's theses.
- Communication with HPC Admin can resolve storage capacity issues.

## Actions Taken
- HPC Admin increased the storage quota for the user's account.

## Follow-up
- No further action required from the user.
- User can now proceed with their Master's thesis work on the Meggie Cluster.
---

### 2023110842001021_Quotaerh%C3%83%C2%B6hung%20b175dc10%20_%20EMPKINS.md
# Ticket 2023110842001021

 ```markdown
# HPC Support Ticket: Quota Increase Request

## Keywords
- Quota limit
- Group quota
- Accounting
- NHR account
- Data ownership
- chown
- chgrp

## Problem Description
A user from the EmpkinS team has reached their quota limit. The user's data is stored under `/home/vault/empkins`, and it was expected that the group quota should apply. The user suspected that their account was not part of the "empk" group, which might be causing the issue.

## Root Cause
- The user's account (b175dc10) is an NHR account, and the data ownership and group membership are critical for quota accounting.
- The path under `/home/vault` is irrelevant for quota accounting; only the owner and group of the data matter.

## Solution
- The HPC Admin team decided to increase the quota for the user's account (b175dc10) after consulting with colleagues.
- The user was informed that upon the expiration of the NHR project, the data must be transferred to another account or copied off the HPC systems to avoid data loss.

## General Learnings
- Quota accounting is based on the owner and group of the data, not the directory path.
- NHR accounts have specific restrictions and cannot be moved to Tier3/FAU groups.
- Increasing the quota for the user's account was the chosen solution to avoid immediate data loss.
- Users must plan for data migration when NHR projects expire to prevent data from being orphaned and potentially deleted.
```
---

### 2018051742000722_Speicherplazterh%C3%83%C2%B6hung.md
# Ticket 2018051742000722

 ```markdown
# HPC-Support Ticket: Speicherplatzerhöhung

## Keywords
- Storage quota
- Data storage
- Simulation data
- Quota increase
- Masterarbeit

## Summary
- **User Issue**: User exceeded the 100GB storage limit in `/home/vault` due to simulation data for a Master's thesis.
- **Request**: Increase storage quota to 400GB.

## Root Cause
- Insufficient storage quota for simulation data required for the user's Master's thesis.

## Solution
- **HPC Admin**: Evaluate the request and increase the storage quota to 400GB if feasible.

## General Learning
- Users may require increased storage quota for large-scale projects such as simulations for academic work.
- Communication with users about storage limits and potential solutions is crucial.
```
---

### 2022051642000832_Quota%20extension.md
# Ticket 2022051642000832

 ### HPC-Support Ticket: Quota Extension for ImageNet Dataset

**Subject:** Quota extension for ImageNet dataset

**User:**
- A student needs ImageNet (1.2TB) for a Master's thesis.
- Requests quota increase to store the dataset in `/home/vault`.

**HPC Admin:**
- Suggests central storage for ImageNet due to potential future use.
- Discusses cheaper server options and no need for backups or snapshots.
- Proposes two options:
  1. Group names a responsible person to manage the dataset and control access via ACL.
  2. User provides data, and HPC Admin places it on the cluster with chair's agreement on terms of use.

**User:**
- Agrees to option 1.
- Asks about HPC account application for employees.
- Confirms cheaper server is sufficient.

**HPC Admin:**
- Provides link to HPC account application form.
- Explains billing options and usage for university research.
- Suggests copying data to `$TMPDIR` to avoid overloading central fileservers.

**User:**
- Confirms HPC account application process for employees.
- Requests additional dataset (Objects365) for multiple students.

**HPC Admin:**
- Schedules Zoom call to discuss further steps.
- Provides path to data-share: `/home/janus/iwi5-datasets`.

**Solution:**
- User applies for HPC account.
- Responsible person is appointed to manage the dataset.
- Data is stored in `/home/janus/iwi5-datasets` and accessible via automount on all HPC systems.

**Keywords:** ImageNet, quota extension, HPC account, data management, ACL, automount, Zoom call, dataset storage.
---

### 2023032442003307_HPC%20Quota%20Extension%20iwso036h%20-%20VisioMel%20Challenge.md
# Ticket 2023032442003307

 # HPC Quota Extension Ticket Analysis

## Keywords
- Quota Extension
- VisioMel Challenge
- Dataset Storage
- Inode Limits
- NFS Directory

## Summary
A user requested a quota extension for participating in the VisioMel Challenge, which required storing a large dataset. The user initially requested an extension of $HPCVAULT or $WORK to 2.0TB but was provided with a new directory `/home/janus/iwso-datasets` with a 5TB quota and 100k inodes.

## Root Cause of the Problem
The user encountered a "Disk Quota Exceeded" error despite having a 5TB quota. The issue was due to exceeding the inode limit of 100k, which restricts the number of files and directories that can be created.

## Solution
The HPC Admin explained that the issue was not with the storage capacity but with the inode limit. The user was advised that storing numerous small files in an NFS directory is not efficient.

## Lessons Learned
- **Quota vs. Inode Limits**: Understanding the difference between storage quota and inode limits is crucial. Exceeding inode limits can cause "Disk Quota Exceeded" errors even if the storage quota is not reached.
- **Efficient Storage Practices**: Storing a large number of small files in an NFS directory is inefficient. Users should consider alternative storage solutions for such datasets.
- **Communication**: Clear communication between users and HPC Admins is essential for resolving quota-related issues efficiently.

## Recommendations
- **Monitor Inode Usage**: Users should monitor their inode usage along with their storage quota to avoid unexpected errors.
- **Optimize File Storage**: Users should optimize their file storage practices, especially when dealing with large datasets consisting of numerous small files.
- **Documentation**: Provide users with documentation on efficient storage practices and the importance of monitoring inode usage.

## References
- [NHR Data Documentation](https://doc.nhr.fau.de/data/datasets/)

## Roles Involved
- **HPC Admins**: Provided the new directory and explained the inode limit issue.
- **User**: Requested the quota extension and reported the "Disk Quota Exceeded" error.

This analysis can serve as a reference for future quota-related issues and help users understand the importance of monitoring inode usage.
---

### 2023031742001733_Frage%20bez%C3%83%C2%BCglich%20Long%20Term%20Storage%20-%20bcpc%20_%20b132dc.md
# Ticket 2023031742001733

 ```markdown
# HPC-Support Ticket: Long Term Storage Inquiry

## Keywords
- Long Term Storage
- HPC Systems
- Quota
- ZOOM Meeting
- Vault
- NHR Project

## Summary
A user inquired about the possibility of long-term data storage on HPC systems following a symposium. The HPC Admins discussed the requirements and arranged a ZOOM meeting to finalize details. A quota of 100TB was allocated for the group on `/home/vault`.

## Timeline
- **17.03.2023**: User inquired about long-term storage options.
- **17.03.2023**: HPC Admin responded, indicating they would discuss details in April.
- **22.05.2023**: HPC Admin suggested a ZOOM meeting to discuss requirements.
- **25.05.2023**: HPC Admin allocated a 100TB quota on `/home/vault` for the group.

## Root Cause
User needed long-term storage options on HPC systems.

## Solution
- HPC Admin allocated a 100TB quota on `/home/vault` for the group.
- A shared directory `vault/bcpc/shared` was created.

## Lessons Learned
- Long-term storage solutions are available on HPC systems.
- ZOOM meetings can be effective for discussing detailed requirements.
- Quotas can be allocated based on group needs and contributions to the HPC infrastructure.

## Conclusion
The user's requirements were met, and they expressed satisfaction with the solution. The ticket was closed successfully.
```
---

### 2016010742001144_Cluster%20Speicherplatz.md
# Ticket 2016010742001144

 # HPC Support Ticket: Cluster Speicherplatz

## Keywords
- Quota Limit
- Storage Space
- MD Simulations
- Publication
- Account Extension

## Problem
- **Root Cause:** Insufficient quota limit for the user's cluster account.
- **Impact:** User unable to perform necessary MD simulations for a publication.

## Solution
- **Request:** Increase storage space to 500 GB as per the initial application.
- **Action:** HPC Admins to review and potentially increase the quota limit for the user's account.

## General Learning
- Users may require additional storage space for critical research tasks.
- Prompt communication and adjustment of quota limits can facilitate important research activities.

## Next Steps
- HPC Admins to confirm the quota increase.
- User to be notified of the status and any further actions required.
---

### 2018092542002092_Request%20to%20increase%20the%20Data%20storage%20quota.md
# Ticket 2018092542002092

 # HPC Support Ticket: Request to Increase Data Storage Quota

## Keywords
- Storage quota
- Soft quota
- Grace period
- Temporary increase
- Quota reduction

## Summary
A user requested a temporary increase in their storage quota due to issues with their local computer, preventing them from transferring data from the HPC login node. The user had exceeded their soft quota and had a grace period of 3 days remaining.

## Root Cause
- User's local computer issues prevented data transfer.
- User exceeded their soft quota and needed additional storage temporarily.

## Solution
- The HPC Admin temporarily increased the user's storage quota.
- Once the user's local system was operational, they requested the quota to be reverted to the original limit (250GB).

## Lessons Learned
- Temporary quota increases can be requested and granted in special circumstances.
- Users should notify the HPC Admin when the increased quota is no longer needed.
- Effective communication between users and HPC Admins is crucial for managing storage quotas.

## Follow-up Actions
- HPC Admins should monitor and adjust quotas as per user requests and system policies.
- Users should be reminded to manage their data storage efficiently to avoid exceeding quotas.
---

### 2024052242001745_Quota%20increase%20request%20to%20the%20user%20v100dd13%20-%20LMU%20DBS.md
# Ticket 2024052242001745

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject: Quota increase request to the user v100dd13 - LMU DBS

### Keywords:
- Quota increase
- Temporary storage
- CEPH
- Data structure
- Filesystem

### Summary:
- **User Request:** Temporary increase of storage quota for user v100dd13 to 5 TB until August 31st for training work involving images and videos.
- **HPC Admin Response:** Suggested using CEPH for the required storage needs and provided links to documentation for workspaces and filesystems.

### Root Cause:
- User requires additional storage for handling large datasets of images and videos.

### Solution:
- **HPC Admin:** Recommended using CEPH for the storage needs and offered further assistance based on the data structure.

### General Learnings:
- **Quota Increase Requests:** Users may need temporary increases in storage quota for specific projects.
- **CEPH Usage:** CEPH is a suitable solution for handling large datasets, especially for images and videos.
- **Documentation:** Providing links to relevant documentation helps users understand available resources and make informed decisions.

### Recommendations for Future Requests:
- **Assess Storage Needs:** Understand the specific storage requirements and data structure of the user.
- **Recommend Appropriate Solutions:** Suggest suitable storage solutions like CEPH and provide documentation links for further guidance.
```
---

### 42157700_Fwd%3A%20Fwd%3A%20PBS%20JOB%20458646.ladm1.md
# Ticket 42157700

 # HPC Support Ticket Analysis: PBS Job Abortion

## Keywords
- PBS Job
- Job Abortion
- Disk Quota
- Scratch Space
- File Count Quota

## Summary
A user's PBS job was aborted by the PBS server due to a disk quota issue. The job could not be executed because the user had exceeded the file count quota in the scratch space.

## Root Cause
- **Disk Quota Exceeded**: The user had too many files in the scratch space (`/lxfs`), which has a file count quota.
- **Error Logs**:
  - `Disk quota exceeded (122) in TMakeTmpDir, Unable to make job transient directory: /scratch/458646.ladm1`
  - `cannot create temp dir '/scratch/458646.ladm1'`

## Solution
- The user was informed about the issue and took action to reduce the number of files in the scratch space.
- The user is now able to work regularly as the problem has been resolved.

## General Learnings
- **Disk Quota Management**: Users should be aware of the disk quota policies, including file count quotas, and manage their storage accordingly.
- **Error Log Interpretation**: Understanding error logs is crucial for diagnosing job failures. In this case, the logs clearly indicated a disk quota issue.
- **Communication**: Effective communication with users about system policies and issues can help resolve problems quickly.

## Roles Involved
- **HPC Admins**: Provided support and resolved the user's issue.
- **User**: Reported the problem and took corrective action.

## Documentation Note
This issue can serve as a reminder for support employees to check disk quotas and error logs when diagnosing job failures. It also highlights the importance of communicating disk quota policies to users.
---

### 2024080542000291_Quota%20auf%20Atuin%3F%20-%20b105dc.md
# Ticket 2024080542000291

 ```markdown
# HPC Support Ticket: Quota auf Atuin?

## Keywords
- Quota
- Atuin
- File quota
- shownicerquota.pl
- df -h
- Technical limitations
- Script side-effects

## Summary
A user reported exceeding the quota on the Atuin system. The issue was related to the file quota rather than the space quota.

## Root Cause
- The file quota on Atuin was accidentally reset to the default value of 10M due to unexpected side-effects of a script.
- The user had almost 16M files stored, instantly exceeding the new file quota.

## Solution
- The file quota was increased to 25M to resolve the issue.
- The user was informed about the technical limitations of viewing file quota on the server.

## What Can Be Learned
- **Quota Checking Commands**: Use `shownicerquota.pl` or `df -h /home/atuin/b105dc` to check space quota.
- **File Quota Limitations**: File quota can only be seen on the server due to technical limitations.
- **Script Side-Effects**: Be cautious of scripts that may unintentionally reset quotas.
- **Communication**: Clearly communicate the difference between space quota and file quota to users.

## Additional Notes
- The group 'sles' does not have a directory on Atuin, which is why `shownicerquota.pl` did not show any information for Atuin or Titan.
- Always verify the impact of scripts on system quotas to avoid unintended resets.
```
---

### 2022030342002135_Request%20to%20increase%20storage%20in%20work%20directory.md
# Ticket 2022030342002135

 ```markdown
# HPC Support Ticket: Request to Increase Storage in Work Directory

## Keywords
- Storage quota
- HPC usage reports
- Work directory
- Quota increase

## Summary
A user requested an increase in storage quota for their work directory to 4 TB. The HPC Admin initially increased the quota to 2 TB and requested usage reports for further increase.

## Problem
- User requested 4 TB storage, which exceeds the usual free HPC storage quota.

## Solution
- HPC Admin increased the quota to 2 TB initially.
- Additional 2 TB was granted upon submission of a structured HPC usage report.

## Communication
- HPC Admin provided a template for the usage report and reminded the user multiple times to submit it.
- User eventually submitted the report, leading to the final quota increase.

## Lessons Learned
- Users should be aware of the standard storage quotas and the requirements for exceeding them.
- Structured usage reports are essential for justifying additional resource allocation.
- Regular follow-ups are necessary to ensure compliance with administrative requests.

## References
- [HPC Usage Reports Template](https://hpc.fau.de/systems-services/hpc-usage-reports/)
```
---

### 2023052342002717_Over%20quota%20in%20file%20system.md
# Ticket 2023052342002717

 ```markdown
# HPC Support Ticket: Over Quota in File System

## Keywords
- Quota
- Home Directory
- File System
- Storage
- Project Storage
- Data Management

## Problem
- User received a warning about being over quota in the file system.
- User has exceeded the 50 GB quota in their home directory.

## Root Cause
- Large data files related to matrix diagonalization and eigenvector storage were saved in the user's home directory, exceeding the allocated quota.

## Solution
- Move data to the project storage directory (`atuin`), which has 10 TB of available storage.
- Reference the documentation for file systems and their intended use: [HPC Storage Documentation](https://hpc.fau.de/systems-services/documentation-instructions/hpc-storage/)

## Additional Information
- The 50 GB quota applies specifically to the home directory.
- No files will be deleted automatically due to exceeding the quota, but it is important to manage storage to avoid further issues.

## Actions Taken
- HPC Admin provided guidance on moving data to the appropriate project storage.
- User acknowledged the information and will take necessary actions.

## Lessons Learned
- Users should be aware of storage quotas and the intended use of different file systems.
- Large data files should be stored in project-specific storage areas rather than the home directory.
- Regularly review and manage storage usage to avoid quota issues.
```
---

### 2024091942001655_Erh%C3%83%C2%B6hung%20Speicherkontingent%20Projekt%20v104dd.md
# Ticket 2024091942001655

 # HPC-Support Ticket: Increase Storage Quota for Project v104dd

## Keywords
- Storage Quota
- Backup
- $WORK
- $HPCVAULT
- Datasets
- WebDataSet Format
- Tarballs

## Summary
The user requested an increase in storage quota for their project (v104dd) to approximately 100 TB. The HPC Admin needed additional information to determine the appropriate storage system.

## Problem
- The user required an increase in storage quota for their project.
- The HPC Admin needed to know if the data required backup and the expected number of individual files.

## Solution
- The user clarified that the data did not require backup as it was also stored on their own servers.
- The data consisted of large datasets in WebDataSet format (tarballs), with individual files mostly around 1 GB, totaling approximately 100k files.
- The quota was increased to 150 TB on the $WORK storage system.

## Lessons Learned
- Different storage systems ($WORK, $HPCVAULT) are available depending on backup requirements.
- It is important to gather information about the number of individual files and backup needs before increasing storage quota.
- Communication between the user and HPC Admin is crucial for determining the appropriate storage solution.

## Actions Taken
- The HPC Admin increased the quota on the $WORK storage system for the project v104dd from 50 TB to 150 TB.

## Follow-up
- No further action is required from the user or the HPC Admin regarding this storage quota increase.
---

### 2024111542001292_Unable%20to%20upload%20files%20to%20Alex%20working%20directories.md
# Ticket 2024111542001292

 ```markdown
# HPC Support Ticket: Unable to Upload Files to Working Directories

## Keywords
- Disk quota
- $HOME directory
- $WORK directory
- Guest account
- Computational time proposal
- Benchmarking
- File upload failure

## Problem Description
- User unable to upload files to previously used directories on Alex GPU.
- Suspected cause: Exhausted soft/hard quota from guest account usage.

## Root Cause
- User exceeded the disk quota in the $HOME directory.
  - Path: `/home/hpc`
  - Used: 105.7G
  - Soft Quota: 104.9G
  - Hard Quota: 209.7G
  - Large data found in `../n102af/n102af11/Alchemical_Debarshee`

## Solution
- Check the FAU documentation on filesystems: [FAU Data Filesystems](https://doc.nhr.fau.de/data/filesystems/)
- Move simulation data to the $WORK directory to free up space in the $HOME directory.

## General Learnings
- Ensure users are aware of disk quotas and proper usage of $HOME and $WORK directories.
- Provide documentation links for users to understand filesystem usage policies.
- Regularly monitor and manage disk usage to prevent quota exhaustion.
```
---

### 2024112942004549_error%20logging%20in.md
# Ticket 2024112942004549

 ```markdown
# HPC Support Ticket: Error Logging In

## Keywords
- Login error
- Quota exceeded
- Home directory
- File systems

## Problem Description
- User is unable to log in to the HPC system.
- User inquires whether the issue is on their side or the HPC side.

## Root Cause
- The user's home directory quota has been exceeded.

## Solution
- **Check Quota:**
  ```sh
  $ shownicerquota.pl
  ```
  or
  ```sh
  $ quota -s
  ```
- **Documentation:** [Quotas Documentation](https://doc.nhr.fau.de/data/filesystems/#quotas)
- **Note:** Quota extension for the home directory is not possible. Users should utilize other file systems for their data.

## General Learnings
- Login issues can often be related to quota limits.
- Users should regularly check their quota usage to avoid such issues.
- Documentation and tools are available to help users manage their quota.
```
---

### 2024060542001767_Storage%20limitation%20-%20v101be12.md
# Ticket 2024060542001767

 # HPC Support Ticket: Storage Limitation

## Keywords
- Storage limitation
- $HOME directory
- $WORK directory
- Anaconda environments
- Disk quota
- Python environments

## Problem
- User encountered a 104GB soft cap on HPC storage.
- Anaconda environments in $HOME directory consumed significant space (77GB), leaving only 23GB free.
- User moved datasets and model checkpoints to the vault and used workspaces for project output files but still faced space issues.

## Root Cause
- Too many files in the "anaconda3" directory under $HOME.
- User did not completely remove old environments and recreate them in $WORK.

## Solution
- Recommended to store Python environments and packages under $WORK.
- User should remove old environments completely and recreate them using the setup described in the documentation, ensuring all files end up in $WORK.
- Documentation link provided: [Creating Conda Environments](https://doc.nhr.fau.de/environment/python-env/#creating-conda-environments)

## Lessons Learned
- Proper management of storage directories ($HOME and $WORK) is crucial.
- Moving large files and environments to $WORK can help manage disk quota.
- Recreating environments in $WORK can prevent disk quota issues related to the number of files.

## Status
- Ticket closed after user managed to delete some files and move environments to $WORK.

## References
- [Python Environments Documentation](https://doc.nhr.fau.de/environment/python-env/)
---

### 2022101242003498_ACL%20und%20group%20directories.md
# Ticket 2022101242003498

 ```markdown
# HPC-Support Ticket: ACL und group directories

## Keywords
- ACL (Access Control List)
- Group permissions
- Read access
- Write access
- Shared directory

## Problem
- User requested read access for the group `b105dc` to the directories `/home/titan/sles002h` and `/home/titan/sles006h` using ACL.
- User also requested a shared directory `/mnt/atuin/b105dc/data` where the group `b105dc` can write.

## Solution
- HPC Admin granted read access to the specified directories for the group `b105dc` using ACL.
- HPC Admin created and configured the shared directory `/mnt/atuin/b105dc/data` with write permissions for the group `b105dc`.

## General Learnings
- ACLs can be used to manage fine-grained permissions for groups and users.
- Shared directories can be configured to allow collaborative work within a group.
- Proper communication and request handling are essential for efficient HPC support.
```
---

### 2021030442002895_Over%20quota%20on%20_home_vault.md
# Ticket 2021030442002895

 # HPC Support Ticket: Over Quota on /home/vault

## Keywords
- Quota
- File Quota
- Block Quota
- Grace Period
- Hard Quota
- Soft Quota
- Filesystem
- Parallel Filesystem

## Problem Description
The user group 'iww1' has exceeded their file quota on the `/home/vault` filesystem. The group has reached the hard limit for the number of files, preventing them from creating new files.

## Quota Report
- **Blocks used:** 4,888,468,688 (4888.5G)
- **Blocks quota soft:** 161,061,273,600 (161.1T)
- **Blocks quota hard:** 177,167,400,960 (177.2T)
- **Files used:** 136,864
- **Files quota soft:** 0
- **Files quota hard:** 0
- **Files grace remaining:** none

## Root Cause
The root cause of the problem is that the group has exceeded their file quota of 0 files, which is set as the hard limit.

## Explanation
- **Blocks:** Measured in 1024 bytes (1 KB).
- **In doubt:** Small values resulting from the parallel filesystem's uncertainty, usually not significant.
- **Soft quota:** Can be exceeded for up to one week (grace period).
- **Hard quota:** Absolute maximum that cannot be exceeded.

## Solution
To resolve the issue, the group needs to delete or archive some of their files to reduce the number of files below the hard quota limit.

## Action Taken
The HPC Admin closed the ticket without further action, indicating that the user group needs to manage their file quota independently.

## General Learning
- Understanding quota limits and their implications.
- Importance of managing file and block usage within allocated quotas.
- Awareness of grace periods for soft quotas.
- Recognizing the constraints of hard quotas.

## Next Steps for Support
- Monitor the group's file usage.
- Provide guidance on file management and archiving strategies.
- Ensure users are aware of quota policies and how to check their usage.
---

### 2020072442001718_Fwd%3A%20Status%20of%20our%20work%20on%20two-phase%20flow%20through%20fixed%20beds.md
# Ticket 2020072442001718

 ```markdown
# HPC Support Ticket: Storage Quota Increase Request

## Keywords
- Storage Quota
- Home Directory
- Simulation Limitations
- Quota Increase Procedure

## Problem
- **Root Cause**: Limited storage quota (330 GB) on the Home/Woody directory preventing the user from running more than 3 simulations simultaneously.

## Solution
- **Action Taken**: The storage quota on /home/woody was increased to 500 GB by the HPC Admin.

## General Learnings
- Users may require additional storage space for their simulations.
- HPC Admins can directly increase the storage quota upon request.
- Proper communication between the user, their supervisor, and HPC support is essential for resolving such issues.

## Steps for Future Reference
1. **User Request**: The user should clearly state the need for additional storage space and the current limitations.
2. **Supervisor Forwarding**: The supervisor forwards the request to HPC support with relevant details.
3. **HPC Admin Action**: The HPC Admin increases the storage quota as requested.
4. **Confirmation**: The user confirms the resolution and thanks the HPC support team.

## Closure
- The ticket was closed after the quota was increased and the user confirmed the resolution.
```
---

### 2019022742001921_Tempor%C3%83%C2%A4re%20Quota-Erweiterung%20in%20woody%20f%C3%83%C2%BCr%20iwtm013h.md
# Ticket 2019022742001921

 ```markdown
# Temporary Quota Extension Request

## Keywords
- Quota Limit
- Temporary Extension
- Simulation Data
- Output Data
- Hard Quota
- Soft Quota
- Bachelor Thesis

## Summary
A user requested a temporary increase in their quota limit for a specific HPC system (woody) due to large output data generated by simulations for their Bachelor thesis.

## Root Cause
- The user's current quota limit is insufficient to handle the large output data generated by their simulations.
- The user needs to complete their simulations without exceeding the hard quota limit.

## Request Details
- User requested an increase in both soft and hard quota limits to at least 1 Terabyte (preferably 1.5 Terabytes) for a duration of approximately 4 weeks.
- The increased quota is necessary to allow parallel computations and ensure the completion of the simulations.

## Solution
- The HPC Admin needs to evaluate the request and, if feasible, temporarily increase the user's quota limits as requested.
- The user should be informed about the decision and any conditions or limitations associated with the temporary quota increase.

## General Learning
- Users may require temporary quota increases for large-scale computations, especially for projects like Bachelor theses.
- It is important to assess the feasibility of such requests and communicate the decision clearly to the user.
```
---

### 2022063042001419_Kurzfristige%20%28ca.%201%20Woche%29%20Ablage%20von%2050%20TB%20Daten.md
# Ticket 2022063042001419

 # HPC Support Ticket: Temporary Storage of 50 TB Data

## Keywords
- Temporary storage
- 50 TB data
- HPC system
- Internal server issue
- Data migration
- Short-term storage

## Problem Description
- Internal server at the department had an issue, requiring temporary storage of 50 TB of data.
- User requested short-term storage on an HPC system for approximately one week.

## Solution
- HPC Admin provided a temporary storage location: `/home/saturn/iwia-data/`.
- User was instructed to move the data to the specified location.

## Outcome
- User confirmed that the data was moved to the temporary storage location.
- After the internal server was back in operation, the user deleted the temporarily stored data.
- No further storage was required.

## Lessons Learned
- HPC systems can be used for short-term data storage in case of internal server issues.
- Communication with HPC Admins is essential for arranging temporary storage solutions.
- Users should promptly delete temporary data once the issue is resolved to free up storage space.

## Follow-up Actions
- Ensure that users are aware of the procedure for requesting temporary storage.
- Monitor temporary storage usage to prevent overloading the HPC system.
- Document the process for future reference and to assist other users with similar needs.
---

### 2023012642001327_nfs%20Backup%20space.md
# Ticket 2023012642001327

 ```markdown
# HPC-Support Ticket Conversation: nfs Backup Space

## Keywords
- NFS Backup Space
- Duplicity Backups
- Tape Backups
- Storage Quota
- CIFS Mount
- NFS Clients for Windows

## Summary
The user requires additional storage space for duplicity backups and has questions regarding tape backups and CIFS mounting.

## Root Cause of the Problem
- Insufficient storage space for duplicity backups.
- Lack of CIFS mount capability for the backup volume.
- Questions about integrating tape backups with duplicity.

## Conversation Details
- **User Request**: Additional storage space for duplicity backups.
- **HPC Admin Response**: Capacity available to increase storage to 100TB.
- **User Request**: Information on integrating tape backups with duplicity.
- **HPC Admin Response**: TSM used for backups, not offered as a service. Snapshots are created for the user's share.
- **User Request**: CIFS mount capability for the backup volume.
- **HPC Admin Response**: CIFS not offered, NFS clients for Windows suggested.

## Solution
- **Storage Quota**: Increase storage quota to 100TB upon user confirmation.
- **Tape Backups**: Snapshots are created for the user's share. Tape backups not offered as a service.
- **CIFS Mount**: Use NFS clients for Windows to mount the backup volume.

## Action Items
- User to confirm the increase in storage quota.
- User to explore NFS clients for Windows for direct backup from the Windows server.

## Additional Notes
- The user and HPC Admin scheduled a Zoom meeting to discuss further details.
- The ticket was closed after addressing the user's concerns.
```
---

### 2018071742001432_Re%3A%20Over%20quota%20on%20_home_hpc.md
# Ticket 2018071742001432

 # HPC Support Ticket: Over Quota on /home/hpc

## Keywords
- Quota exceeded
- Block quota
- Grace period
- Filesystem usage
- HPC Admin
- User support

## Summary
A user received an automated notification about exceeding their block quota on the `/home/hpc` filesystem. The user was unable to identify the large files causing the issue and requested assistance from the HPC Admin.

## Root Cause
- The user's block usage exceeded the soft quota of 10.5G and was approaching the hard limit of 21.0G.
- The user had 19GB of data in `/home/hpc/capm/mppi017h/.local/`.

## Solution
- The HPC Admin identified the directory containing a significant amount of data (`/home/hpc/capm/mppi017h/.local/` with 19GB).
- The user was informed about the specific directory to check for large files.

## Lessons Learned
- Users may not always be aware of the specific files or directories consuming their quota.
- HPC Admins can assist by identifying large directories or files using system tools.
- Regularly checking and managing filesystem usage can prevent quota issues.

## Next Steps
- Users should review and manage their filesystem usage to stay within their allocated quota.
- HPC Admins can provide tools or scripts to help users identify large files and directories.

## References
- HPC Quota Checker email notification
- HPC Admin response identifying the large directory

## Additional Notes
- The grace period allows users to temporarily exceed their soft quota but enforces the hard quota strictly.
- Regular communication and support can help users manage their filesystem usage effectively.
---

### 2022120442000163_help%20with%20imagenet%20dataset.md
# Ticket 2022120442000163

 # HPC Support Ticket: ImageNet Dataset Assistance

## Keywords
- ImageNet dataset
- Dataset path
- Dataset download
- Dataset usage terms
- Stratified sampling
- Data transfer

## Summary
A user requested assistance with accessing the ImageNet dataset for their experiments. The user wanted to know if the dataset was already available on the server and, if not, where to download and place it.

## Root Cause
- User needed access to the ImageNet dataset.
- User was unsure if the dataset was already available on the server.
- User required guidance on where to download and place the dataset if not available.

## Solution
1. **Dataset Availability**:
   - A co-worker found a 1% version of the ImageNet dataset at `/home/janus/iwi5-datasets/imagenet/imagenet-one.tar`.
   - This version contains 1% of the images with stratified sampling for categories.

2. **Usage Terms**:
   - The user must adhere to the terms of access listed at [ImageNet Download](https://image-net.org/download.php).

3. **Dataset Preparation**:
   - The user should untar the dataset to the working machine before using it.

4. **Full Dataset Request**:
   - If the full ImageNet dataset is needed, the user should contact the co-worker to discuss the resolution and transfer details.

## General Learnings
- Always check with co-workers or the HPC support team for dataset availability.
- Ensure compliance with dataset usage terms.
- Prepare datasets properly before use (e.g., untar files).
- Communicate with the support team for any additional requirements or larger data transfers.

## Roles Involved
- **HPC Admins**: Provided initial guidance and referred the user to a co-worker.
- **Co-worker**: Assisted with locating the dataset and provided detailed instructions.

## Conclusion
The user was successfully guided to the available dataset and provided with instructions for its use. Further assistance was offered for obtaining the full dataset if needed.
---

### 2018100942002511_Quota%20Erh%C3%83%C2%B6hung.md
# Ticket 2018100942002511

 # HPC Support Ticket: Quota Increase Request

## Keywords
- Quota Increase
- Temporary Quota
- Vault Storage
- Data Analysis
- Doctoral Research

## Summary
A user requested a temporary increase of their quota on the Vault storage system due to the need to process large datasets for their doctoral research.

## Root Cause
- User requires additional storage space for data analysis.

## Solution
- The user requested an increase of 100GB in their quota.
- The HPC Admin needs to evaluate and approve the request.

## General Learnings
- Users may require temporary quota increases for large data processing tasks.
- It is important to have a process in place for handling and approving quota increase requests.

## Next Steps
- HPC Admin to review the request and decide on the quota increase.
- Communicate the decision back to the user.

## Related Roles
- HPC Admins: Thomas, Michael Meier, Anna Kahler, Katrin Nusser, Johannes Veh
- 2nd Level Support Team: Lacey, Dane (fo36fizy), Kuckuk, Sebastian (sisekuck), Lange, Florian (ow86apyf), Ernst, Dominik (te42kyfo), Mayr, Martin
- Head of the Datacenter: Gerhard Wellein
- Training and Support Group Leader: Georg Hager
- NHR Rechenzeit Support: Harald Lanig
- Software and Tools Developer: Jan Eitzinger, Gruber
---

### 2024121842002462_Application%20for%20a%20group-shared%20directory.md
# Ticket 2024121842002462

 # HPC Support Ticket: Application for a Group-Shared Directory

## Keywords
- Group-shared directory
- File quota
- Permissions
- HPC portal
- Cleanup space

## Problem
- **Root Cause**: Group members need a shared directory to exchange large amounts of data.
- **Issue**: The group's file quota is full, preventing them from writing new files.

## Solution
- **Action Taken**: A shared directory `/home/atuin/b241dd/shared` was created.
- **Recommendation**: The primary user (b241dd10) was advised to clean up space and use a better file format to free up quota.

## General Learnings
- **Directory Creation**: HPC admins can create group-shared directories upon request.
- **Quota Management**: Users must manage their file quotas to ensure they can write new files.
- **Permissions**: PIs or PMs can create secondary accounts via the HPC portal and adjust permissions using `chmod`.

## Follow-up
- Ensure users are aware of their file quotas and how to manage them.
- Provide guidance on efficient file formats and data management practices.
---

### 2024031142001368_Shared%20folders%20on%20clusters%20-%20iwsp.md
# Ticket 2024031142001368

 # Shared Folders on Clusters - iwsp

## Keywords
- Shared folders
- Conda environments
- Group home directory
- Quota allocation
- Permissions

## Problem
- User wanted to share pre-configured conda environments and utilities with group members.
- Initial attempts to share an executable by changing permissions did not work due to home directory access restrictions.
- User preferred a shared directory in the group home with quota allocated by ownership or group quota.

## Solution
- HPC Admin created shared folders for the group at `/home/woody/iwsp/shared` and `/home/atuin/b168dc/shared`.
- Quota is accounted per user.
- Files should have read permissions for the group, and directories should have read and execute permissions.

## General Learnings
- Sharing files within a group requires appropriate directory and file permissions.
- Shared folders can be created in the group home directory to facilitate collaboration.
- Quota allocation can be managed per user or per group depending on the setup.
- HPC Admin can assist in creating shared folders and managing permissions.
---

### 2023121342001616_group%20disk%20quota%20on%20vault%20for%20gwgi.md
# Ticket 2023121342001616

 # HPC Support Ticket: Group Disk Quota on Vault for gwgi

## Keywords
- Group disk quota
- Vault
- Geography department
- gwgi
- Disk space usage
- Quota information

## Problem
The user from the Geography department (gwgi group) wants to know how to check the total disk quota and usage for their group on `/home/vault/gwgi`. They are familiar with the process for another system (saturn) but need similar information for vault.

## Solution
- **Current Usage**: The group gwgi has currently used 213.8TB on vault.
- **Total Quota**: The group quota is 250TB.
- **Additional Quota**: A functional account (gwgifu1h) with 500TB quota was created for a specific user, which does not fall under the group quota.
- **Access**: Users cannot currently check the quota themselves.

## Notes
- The HPC Admin provided the necessary information directly.
- There is no self-service option for users to check their quota on vault.

## Action Taken
- The HPC Admin informed the user about the current disk usage and total quota.
- The user was notified about the additional quota for a specific functional account.

## Future Reference
- If users need to check their disk quota on vault, they should contact HPC support for the information.
- There is no self-service tool available for users to check their quota on vault.
---

### 2022111442001583_Shared%20Verzeichnis%20%28Lustre%29.md
# Ticket 2022111442001583

 ```markdown
# HPC-Support Ticket: Shared Verzeichnis (Lustre)

## Keywords
- Lustre
- Shared Directory
- Permissions
- Cluster
- ChestX-ray Dataset

## Problem
- User requested a shared directory for multiple users to access a large ChestX-ray dataset.
- Directory path: `/lustre/iwi5/shared`

## Root Cause
- User did not specify which cluster the request pertained to.

## Solution
1. **Cluster Identification**: User clarified that the request was for the Alex Cluster.
2. **Directory Creation**: HPC Admin created the shared directory `/lustre/iwi5/shared`.
3. **Permissions**: HPC Admin suggested using `chmod g+rX /lustre/iwi5/$USER/xraydaten` to grant group read permissions.

## General Learnings
- Always specify the cluster when requesting shared directories.
- Use `chmod` to set appropriate permissions for group access.
- HPC Admin can create shared directories upon request with necessary details.
```
---

### 2017020742001873_Quota%20auf%20Woody.md
# Ticket 2017020742001873

 # HPC Support Ticket: Quota Increase Request on Woody

## Keywords
- Quota
- Woody
- Simulation
- Storage
- Increase

## Problem
- **Root Cause**: User running many simulations on Woody is quickly reaching quota limits.
- **Request**: Increase quota on `/home/woody` to 3 TB.

## Conversation Summary
- User requests quota increase due to high simulation load.
- HPC Admin acknowledges the request and notes the current quota usage.
- HPC Admin increases quota to 1 TB soft / 2 TB hard instead of the requested 3 TB.

## Solution
- **Action Taken**: Quota increased from 25 GB (18 GB used) to 1 TB soft / 2 TB hard.
- **Reasoning**: The requested increase to 3 TB was deemed disproportionate.

## General Learning
- **Quota Management**: Be cautious with large quota increase requests.
- **User Communication**: Clearly communicate the reasons for partial fulfillment of requests.
- **Monitoring**: Regularly monitor user storage usage to anticipate and manage quota needs.

## Next Steps
- Monitor user's storage usage to ensure the increased quota is sufficient.
- Consider further adjustments if the user continues to approach quota limits.
---

### 2024112842003702_Request%20for%20Assistance%20with%20Disk%20Quota%20Issue%20on%20FAU%20Alex%20GPU%20Cluster%20-%20b24.md
# Ticket 2024112842003702

 # HPC Support Ticket: Disk Quota Issue on FAU Alex GPU Cluster

## Subject
Request for Assistance with Disk Quota Issue on FAU Alex GPU Cluster

## Keywords
Disk quota, FAU Alex GPU cluster, file system, quota exceeded, storage space, file count

## Summary
User encountered a disk quota issue while attempting to extract data into the directory `/home/atuin/b241dd`. Despite not exceeding the SoftQ limit, the user was unable to create or write new files to the directory.

## Root Cause
- User had a large number of small files, which can cause issues with file system limitations.
- Project-wise quota applied to the user's account, not user-based quota.

## Details
- Username: b241dd10
- Directory: `/home/atuin/b241dd`
- Current Usage: 71.2G out of 104.9G SoftQ
- User deleted a significant amount of data but still encountered quota exceeded errors.

## Steps Taken
1. **Initial Response**:
   - HPC Admin provided information about the file system and corresponding quota.
   - Requested the complete output of the script `shownicerquota.pl`.

2. **Further Investigation**:
   - HPC Admin checked the user's data in `atuin` and found a large amount of data, not initially mentioned by the user.
   - User was advised to run the command `du -hsc *` in both `$WORK` and `$HOME` to find out more detailed info.
   - Recommended using the fast file system `anvme` on Alex for workspaces.

3. **Quota Clarification**:
   - HPC Admin clarified that the quota is applied project-wise rather than user-based quota.
   - The limit of 1000GB is for Tier3 users and does not apply to the user's account.

4. **File Count Issue**:
   - HPC Admin suggested that the user may have too many small files, which can cause issues with file system limitations.
   - Provided a command to find out the number of files per directory:
     ```sh
     ls -1d * | xargs -I % sh -c 'echo -n % "  "; find % -type f | wc -l'
     ```

## Solution
- User should check the number of files per directory and consider consolidating small files to avoid file system limitations.
- Use the fast file system `anvme` on Alex for workspaces and regularly copy data to a local machine or group storage to avoid exceeding time limits.

## Additional Resources
- [FAU Data File Systems](https://doc.nhr.fau.de/data/filesystems/#available-filesystems)
- [FAU Workspaces](https://doc.nhr.fau.de/data/workspaces/)

## Conclusion
The issue was likely caused by a large number of small files and project-wise quota limitations. Users should be aware of file system limitations and regularly manage their data to avoid quota exceeded errors.
---

### 2017071942001887_Erh%C3%83%C2%B6hung%20des%20Speicherplatzes%20%28WOODY%29.md
# Ticket 2017071942001887

 ```markdown
# HPC Support Ticket: Increase Storage Space (WOODY)

## Keywords
- Storage Quota
- Home Directory
- Simulation Data
- HPC_Lima
- WOODY

## Summary
A user requested an increase in storage space for their home directory on the HPC system due to large simulation data.

## Root Cause
- User requires additional storage space for large simulation data (80GB-200GB).
- Current usage in `/home/woody` is 0 bytes.

## Solution
- HPC Admin increased the storage quota for `/home/woody` to 500GB soft / 1000GB hard.

## Lessons Learned
- Verify current storage usage before requesting an increase.
- Ensure the correct directory is specified for storage increase requests.
- Communicate clearly with the HPC support team regarding future storage needs.
```
---

### 2023020142001051_memory%20allocation%20for%20cls%20configurations.md
# Ticket 2023020142001051

 # HPC Support Ticket: Memory Allocation for Lattice-QCD Configurations

## Keywords
- Memory allocation
- Quota exceeded
- HPCVAULT
- Lattice-QCD calculations
- Storage solutions
- $WORK filesystem

## Problem
- User received an email indicating that their quota on HPCVAULT was exceeded.
- User needs to perform large Lattice-QCD calculations requiring access to approximately 1000 configurations, each around 10GB in size.
- Starting with 100 configurations already exceeds the HPCVAULT quota.

## Solution
- HPC Admin suggested using the `atuin` ($WORK) filesystem, which has 10TB of storage allocated to the user's project.
- User was provided with a link to the list of all filesystems: [HPC Storage Documentation](https://hpc.fau.de/systems-services/documentation-instructions/hpc-storage/)
- User was asked to confirm if storing input files on `atuin` ($WORK) would suffice or if a backup on HPCVAULT is necessary.

## General Learnings
- Understand the different storage options available on the HPC system.
- Be aware of the quota limits for various storage systems.
- Consider alternative storage solutions when quota limits are exceeded.
- Communicate with users to determine the best storage solution for their specific needs.

## Next Steps
- Await user confirmation on whether storing input files on `atuin` ($WORK) is sufficient.
- If necessary, explore options for increasing storage quota on HPCVAULT.

## References
- [HPC Storage Documentation](https://hpc.fau.de/systems-services/documentation-instructions/hpc-storage/)
---

### 2025012242002446_Group-shared%20directory%20-%20_home_janus_iwnt-datasets_.md
# Ticket 2025012242002446

 # HPC Support Ticket: Group-Shared Directory - /home/janus/iwnt-datasets/

## Keywords
- Shared directory
- Storage quota
- Video datasets
- Accessibility
- Directory management

## Summary
A user requested a shared directory for storing large video datasets to avoid repeated downloads and manage storage quotas efficiently. The HPC Admin created the directory with specific quotas and provided instructions on accessing and managing the directory.

## Problem
- **Root Cause**: The user needed a shared directory to store large video datasets for training video compression models. The existing storage quotas were insufficient for large datasets.
- **Additional Issues**: The directory was initially not accessible on all HPC systems, and additional users required write access to the directory.

## Solution
- **Directory Creation**: The HPC Admin created a shared directory `/home/janus/iwnt-datasets/` with a capacity quota of 15 TB and a limit of 100k files/directories.
- **Access Instructions**: The directory is available on all HPC systems but is mounted only when explicitly accessed. Users should use the full path to access the directory.
- **Management Transfer**: The ownership of the directory was transferred to another user to manage new subdirectories and access permissions.

## Additional Notes
- **Bundling Data**: Users may need to bundle individual samples into suitable aggregates (e.g., webdataset tar files, Apache Parquet) due to the file limit.
- **Accessibility**: The directory is accessible on all HPC systems but may not always appear in the parent directory listing.

## Conclusion
The HPC Admin successfully created and managed a shared directory for storing large video datasets, addressing the user's storage and accessibility concerns. The directory is now available for collaborative use, with clear instructions for access and management.
---

### 2017032842002063_redirect%20Punktdatein.md
# Ticket 2017032842002063

 # HPC-Support Ticket: Redirect Punktdatein

## Keywords
- Home directory
- Quota
- Comsol
- Data management
- Woody
- Vault
- .local directory

## Problem
- User's home directory is filling up with "Punktdatein" generated by Comsol.
- Home directory has a limited quota of 10GB.
- User wants to redirect these files to a larger storage location like Woody or Vault.

## Root Cause
- Comsol generates a large number of files in the home directory, causing it to fill up quickly.

## Solution
- HPC Admin suggested redirecting the `.local` directory to `$WOODYHOME`.
- User agreed to delete all current data in the home directory.
- HPC Admin created a symbolic link from `~/.local` to `$WOODYHOME/local`.
- User can now manually delete files in the new location if needed.

## General Learnings
- Large simulations can generate a significant amount of data, which can quickly fill up a user's home directory.
- Redirecting data to a larger storage location can help manage this issue.
- Symbolic links can be used to redirect data to different storage locations.
- It's important to regularly clean up unnecessary data to prevent storage issues.
---

### 2016030742000696_Speicher%20Vault.md
# Ticket 2016030742000696

 ```markdown
# HPC Support Ticket: Speicher Vault

## Keywords
- Storage Quota
- GPFS Vault
- Service Addresses
- HPC Admin
- User ID

## Summary
A user requested additional storage space on the GPFS vault. The HPC admin responded by increasing the quota and provided guidance on using the correct service addresses for future requests.

## Root Cause
- User needed additional storage space.
- User was unsure if they were contacting the correct person.

## Solution
- HPC Admin increased the user's quota on `/home/vault`.
- User was advised to use the documented service addresses (`hpc@fau.de` or `support-hpc@fau.de`) for future requests.

## What Can Be Learned
- Users should use the official service addresses for support requests.
- HPC Admins can handle storage quota increases efficiently.
- Proper communication channels ensure timely and appropriate support.
```
---

### 2023082142003054_Berechtigungen%20auf%20%24WORK%20teilen.md
# Ticket 2023082142003054

 # HPC-Support Ticket: Sharing Permissions on $WORK Directory

## Keywords
- HPC
- Permissions
- $WORK Directory
- chmod
- Unix Group
- NHR Project

## Problem
- User wants to share read/write permissions for their $WORK directory with another user to avoid uploading large models multiple times.
- User lacks permissions to authorize the sharing themselves.

## Root Cause
- Insufficient permissions to modify directory access rights.

## Solution
- HPC Admin suggests using `chmod` to grant execute and write permissions to the group on the directory tree.
- The group includes only those invited to the NHR project.

## General Learning
- Users can share directory permissions with others in their Unix group by using the `chmod` command.
- The Unix group is restricted to members invited to the NHR project.
- This approach helps in efficiently sharing large data without redundant uploads.

## Next Steps
- User should apply the suggested `chmod` command to grant the necessary permissions.
- If further assistance is needed, the user can contact the HPC support team.
---

### 2017062742002023_Speicherplatz%20auf%20dem%20HPC.md
# Ticket 2017062742002023

 # HPC Support Ticket: Storage Space on HPC

## Keywords
- Storage space
- Quota
- Home directory
- Vault directory
- i-Nodes
- Online data
- Tape migration

## Summary
A user inquired about the available storage space in their `/home/hpc/caph/mpp...` and `/home/vault/caph/mpp...` directories. The user also mentioned a 10GB quota for the home directory.

## Root Cause
The user needed clarification on the storage space available in specific directories and the quota limits.

## Solution
- **Home Directory Quota**: Confirmed that the quota for the home directory is 10GB.
- **Vault Directory Quota**:
  - The default quota for `/home/vault` is 100GB and 100k i-Nodes.
  - The quota applies to online data, not data migrated to tape.
  - The group "caph" had used approximately 15TB of the 60TB online pool in `/home/vault` as of mid-June.
  - The quota can be increased upon request.

## Additional Information
- The user was informed that the vault directory had temporarily run out of space.
- A new, unrelated request about computing time usage was split into a separate ticket.

## General Learning
- Understanding the distinction between online and tape-migrated data in quota calculations.
- The importance of monitoring and managing storage space to avoid running out of capacity.
- Proper handling of multiple inquiries by splitting them into separate tickets for better tracking and resolution.

## Follow-Up Actions
- Monitor storage usage in the vault directory to prevent future space issues.
- Educate users on how to check their storage quota and usage.
- Ensure that users are aware of the process for requesting quota increases.
---

### 2022012042000091_Re%3A%20Over%20quota%20on%20_home_hpc.md
# Ticket 2022012042000091

 # HPC Support Ticket Analysis: Over Quota on /home/hpc

## Keywords
- Quota
- Inode Quota
- File Quota
- Grace Period
- Archive Files
- Data Format
- HPC Vault

## Summary
A user exceeded the file quota on the `/home/hpc` filesystem due to a large number of small files generated from video simulations. The user requested an increase in memory space and file count limit.

## Root Cause
- **Excessive Small Files**: The user's simulations generate a large number of small files, exceeding the file quota.
- **Misunderstanding of Quota**: The user initially thought the issue was related to memory space rather than the number of files.

## Quota Report
- **Blocks Used**: 37,692,144 (37.7 GB)
- **Files Used**: 614,161
- **Files Quota Soft**: 500,000
- **Files Quota Hard**: 1,000,000
- **Files Grace Remaining**: 7 days

## Solution
- **HPC Admin Response**: The admin clarified that the issue is with the inode quota (too many small files) and suggested using a different file format or archives.
- **Additional Resources**: The admin provided links to resources on file systems and data management.
- **Alternative Storage**: The admin mentioned additional storage available at `/home/vault` ($HPCVAULT) but emphasized the need to change the data format to avoid similar issues.

## Action Items
- **User**: Change the data format or use archives to reduce the number of small files.
- **HPC Admin**: Monitor the user's quota usage and provide further assistance if needed.

## Resources
- [HPC File Systems Presentation](https://hpc.fau.de/files/2022/01/2022-01-11-hpc-cafe-file-systems.pdf)
- [FAU TV Clip on File Systems](https://www.fau.tv/clip/id/40199)

## Conclusion
The user needs to address the issue of excessive small files by changing the data format or using archives. The HPC admin provided resources and alternative storage options to help the user manage their data more effectively.
---

### 2020081342002325_over%20quota%20warning.md
# Ticket 2020081342002325

 # Over Quota Warning Issue

## Keywords
- Over quota warning
- Data storage location
- HPC login warning
- Trash folder

## Problem Description
A new HPC user encountered an over quota warning upon logging into the HPC system. The user had previously stored and transferred 16GB of data but was unsure of the exact storage location to delete the files and resolve the warning.

## Root Cause
The user had 15GB of data stored in the trash folder located at `/home/hpc/caph/mppi093h/.local/share/Trash/`.

## Solution
The HPC Admin identified the location of the large files in the trash folder and informed the user. The user can delete the files from the specified location to resolve the over quota warning.

## Command to Find Large Files
To locate large files, users can use the following command:
```bash
du -ah /home/hpc | sort -rh | head -n 20
```
This command will display the 20 largest files or directories under the `/home/hpc` path.

## General Learnings
- Over quota warnings are often caused by large files in unexpected locations, such as trash folders.
- Users should be aware of their storage usage and regularly check for large files.
- HPC Admins can assist in locating large files and directories.
- The `du` command is useful for finding large files and directories.
---

### 2020050442001161_Daten%20auf%20Band%20schreiben.md
# Ticket 2020050442001161

 # HPC Support Ticket: Data Transfer to Tape

## Keywords
- Data transfer
- FASTTMP
- emmy
- vault
- tape storage

## Summary
A user wants to transfer data from the FASTTMP directory on the emmy system to a location with sufficient space. The user's colleague suggested creating a directory in the vault filesystem, which would then be written directly to tape storage.

## Root Cause
- User needs to transfer data from FASTTMP to a storage location with more space.
- User is seeking assistance in setting up a directory in the vault filesystem for tape storage.

## Solution
- The user requested the HPC team to set up a directory in the vault filesystem for data transfer to tape storage.
- No specific solution provided in the initial conversation; further interaction with the HPC admin is needed.

## General Learnings
- Users may need guidance on transferring data between different storage systems.
- The vault filesystem can be used for direct data transfer to tape storage.
- HPC admins should be prepared to assist with setting up directories and managing data transfers.

## Next Steps
- Await further interaction with the HPC admin to provide a specific solution.
- Document the process for setting up directories in the vault filesystem for future reference.
---

### 2022120842003582_Attempting%20To%20Solve%20Puzzle.md
# Ticket 2022120842003582

 # HPC Support Ticket: Attempting To Solve Puzzle

## Keywords
- HPC Puzzle
- Shared Storage
- NFS
- Crossword Puzzle

## Summary
A user encountered difficulties solving an HPC puzzle, specifically struggling with the term for "shared storage of the masses." The user initially tried various terms such as MAN, LAN, and NAS without success.

## Root Cause
- The user was unable to determine the correct term for "shared storage of the masses" in the HPC puzzle.

## Solution
- The user eventually figured out the correct term, which is **NFS** (Network File System).

## Lessons Learned
- Understanding common HPC terminology is crucial for solving puzzles related to high-performance computing.
- NFS is a widely used term for shared storage in HPC environments.

## Follow-up
- The HPC Admin acknowledged the user's solution and thanked them for participating in the puzzle.

## Additional Notes
- The user showed interest in knowing if others had solved the puzzle correctly and what the correct answer was.
- The HPC Admin's response included a holiday greeting, indicating a friendly and supportive environment.

---

This documentation can be used to assist other users who may encounter similar issues with HPC puzzles or terminology.
---

### 2018081042001176_Quota-Erh%C3%83%C2%B6hung.md
# Ticket 2018081042001176

 # HPC Support Ticket: Quota Increase

## Keywords
- Quota Increase
- Vault Quota
- Soft Quota
- HPC Kennung
- Messdaten

## Summary
A user requested an increase in their Vault quota due to an excess of measurement data generated during their internship. The user provided their HPC Kennung for identification.

## Root Cause
- User's current Vault quota is insufficient for the amount of measurement data being generated.

## Solution
- User requested an increase in their Soft Vault Quota to 300 GB.
- Important to include HPC Kennung in the request for identification.

## Lessons Learned
- Always include your HPC Kennung when requesting a quota increase.
- Provide a clear and concise reason for the quota increase request.
- Ensure that the request is directed to the appropriate HPC support team.

## Follow-up
- HPC Admins should review the request and adjust the quota as necessary.
- If the request is approved, the user should be notified of the quota increase.
---

### 2023072142003458_File%20number%20quota.md
# Ticket 2023072142003458

 # HPC Support Ticket: File Number Quota

## Keywords
- File quota
- Block quota
- Grace period
- Inode quota
- Backup and snapshot system

## Problem
- User exceeded both block quota and file quota on the `/home/vault` filesystem.
- User's calculations produce a large number of small files, making it difficult to stay within the file quota.

## Root Cause
- The user's calculations (ReaxFF trainset calculations with VASP and ReaxFF global force field parameter optimizations) generate a vast number of small files, leading to the file quota being exceeded.

## Solution
- **HPC Admins** increased the user's inode quota on the vault to match the increased size quota.
- User was advised to keep the file count low due to potential issues with the backup and snapshot system.

## General Learnings
- Large numbers of small files can lead to file quota issues.
- Increasing inode quota can help users who need to store many small files.
- High file counts can cause problems for backup and snapshot systems.
- Users should be mindful of both block and file quotas and manage their storage accordingly.
---

### 2024111242001172_Question%20about%20increasing%20the%20volume%20folders..md
# Ticket 2024111242001172

 # HPC Support Ticket: Increasing Volume Folders

## Keywords
- Storage Quota
- Data Upload
- Long-term Storage
- Genomic Data
- $WORK Directory

## Summary
A user requested an increase in storage quota due to the need to store and process large amounts of genomic data. The user also inquired about faster data upload methods and long-term storage options.

## Root Cause
- Insufficient storage space in the $WORK directory for processing large genomic datasets.
- Slow data upload speeds due to limited office internet connection.

## Solution
- **Storage Quota Increase**: The user's quota on the $WORK directory was doubled to 6 TB.
- **Data Upload**: The HPC admins clarified that they do not offer a service to upload data from external hard drives.
- **Long-term Storage**: The HPC admins provided information about an archive service for long-term storage.

## General Learnings
- Always include HPC account details and the specific cluster(s) being used in support requests.
- The HPC center provides an archive service for long-term storage.
- Users should be aware of the need to transfer results back after processing.

## Related Links
- [FAU Archive Service](https://www.anleitungen.rrze.fau.de/serverdienste/fau-archiv/)
---

### 2022032942001598_Temporary%20%28pre%20publication%29%20storage.md
# Ticket 2022032942001598

 ```markdown
# HPC-Support Ticket Conversation: Temporary Storage for Pre-Publication Data

## Keywords
- Temporary storage
- Pre-publication data
- Compression
- Vault quota
- Usage report

## Problem
- User has a large number of output files (simple text files) generated using the HPC.
- Each project is associated with about 500 GB+ of output.
- Files need to be stored temporarily until publication.
- User does not need to keep these files forever but needs to store them temporarily.

## Solution
- **Short-term Solution:** Increased vault quota to 2TB for the user.
- **Compression Advice:**
  - Use `zip` if partial extraction is needed.
  - Use `tar.gz`, `tar.bz`, or `tar.xz` for full extraction.
- **Long-term Solution:** Discuss moving data to tape archive if needed for several years with no changes.

## Additional Information
- **Timescale:** Data needs to be kept for 6-12 months.
- **Usage Report:** User provided a usage report for the HPC service, which was published on the HPC webpage.
- **Quota Increase for PhD Student:** User requested and received an increase in storage space for a PhD student working on an output-heavy project.

## Conclusion
- The user was able to compress and store the data in the vault.
- The usage report was provided and published, which is essential for showing funding agencies the kind of resource enabled by the HPC service.
```
---

### 2024091942001048_quota%20expansion.md
# Ticket 2024091942001048

 # HPC Support Ticket: Quota Expansion

## Keywords
- Quota expansion
- Storage quota
- Meggie cluster
- HPC folder
- $WORK directory
- LES simulation
- OpenFOAM
- Transient flow CFD simulation

## Problem
- User requires additional storage quota for transient flow CFD simulations using the LES method with OpenFOAM on the Meggie cluster.
- Current storage in the HPC folder is insufficient for storing many timestep results.

## Solution
- **HPC Admins** advised that the HPC folder is not intended for large data storage and quota extensions are not possible.
- Recommended using the `$WORK` directory for storing large datasets.
- Provided a link to the file systems documentation: [FAU Data Filesystems](https://doc.nhr.fau.de/data/filesystems/)

## General Learning
- The HPC folder is intended for important data and does not support quota extensions.
- For large datasets, users should utilize the `$WORK` directory.
- Documentation on file systems is available for further reference.

## Next Steps
- Users should move their large datasets to the `$WORK` directory.
- Refer to the provided documentation for more information on file systems and storage options.
---

### 2023113042000641_Quota%20error.md
# Ticket 2023113042000641

 # HPC Support Ticket: Quota Error

## Keywords
- Quota error
- HPC home directory
- Block quota
- Grace period
- Filesystem usage
- $HPCVAULT
- $WORK

## Problem Description
- User received a quota error for the HPC home directory.
- Exceeded block quota of 52.4G on the filesystem /home/hpc.
- Grace period expired, preventing further file saves.

## Root Cause
- User's home directory contains large folders consuming significant space:
  - `calving_front_mohajerani`: 33G
  - `project`: 6.5G
  - `.cache`: 6.9G

## Solution
- **HPC Admin** suggested moving some of the large folders to alternative storage locations such as `$HPCVAULT` or `$WORK`.
- Provided a link to the documentation for an overview of HPC storage systems: [HPC Storage Documentation](https://hpc.fau.de/systems-services/documentation-instructions/hpc-storage/)

## General Learnings
- Users should regularly check their quota usage to avoid exceeding limits.
- Large files and directories should be stored in appropriate storage locations like `$HPCVAULT` or `$WORK` to manage space efficiently.
- Understanding the grace period and quota limits is crucial for effective file management on HPC systems.

## Documentation Reference
- [HPC Storage Documentation](https://hpc.fau.de/systems-services/documentation-instructions/hpc-storage/)
---

### 2022053042002367_iwi5064h%20-%20data%20storage%20query.md
# Ticket 2022053042002367

 # HPC Support Ticket: Data Storage Query for Large Dataset

## Keywords
- Data storage
- HPC cluster
- Access permissions
- Node local storage
- AI/ML workload
- Shared directory

## Problem
- User has a large dataset (1.9 million images, 485 GB) for training models.
- Needs guidance on where to store the dataset on the HPC cluster for easy and quick access.
- Wants to know if the dataset can be made accessible to other students and the procedure for doing so.

## Solution
- **Storage Location**: Copy the dataset to a shared directory (e.g., `/home/woody/iwi5/shared`) with proper permissions for group access.
- **Node Local Storage**: For AI/ML workloads, copy the data to node local storage (`$TMPDIR`) at the beginning of the job. If the dataset is small enough, it can be copied into RAM.
- **Access Permissions**: Set appropriate permissions to allow other students in the group to read the files.

## General Learnings
- Large datasets for AI/ML training should be stored in a shared directory with proper permissions for group access.
- For efficient processing, data should be copied to node local storage (`$TMPDIR`) or RAM at the beginning of the job.
- Sharing data with other users can be managed through directory permissions.

## Related Resources
- [HPC File Systems Presentation](https://hpc.fau.de/files/2022/01/2022-01-11-hpc-cafe-file-systems.pdf)
- [OmniArt Dataset](http://www.vistory-omniart.com/)
---

### 42052331_Home%20umziehen%20%5BAccount%20f%C3%83%C2%BCr%20Nutzung%20von%20HPCSystemen%20am%20RRZE%5D.md
# Ticket 42052331

 # HPC Support Ticket Analysis

## Subject: Home Directory Migration

### Keywords
- Home directory
- Migration
- CPLEX
- Temporary storage
- Job submission
- Resource allocation

### Root Cause
- User's home directory is located in an old path, causing space limitations.
- User requires more space for CPLEX optimizations and temporary storage for large datasets.

### Solution
- **Home Directory Migration**: The user's home directory was successfully migrated from the old path (`/home/rrze/iwn2/iwn204`) to the new path (`/home/hpc/iwn2/iwn204`).
- **Temporary Storage**: The user was advised to use `$FASTTEMP` (global Lustre filesystem) or `$TMPDIR` (local RAID) for temporary storage on the Woodcrest-Cluster.
- **Job Submission**: For accessing the 24-Core/128 GB Opteron machine, the user was instructed to submit jobs from `testfront.rrze.uni-erlangen.de` and request `-lnodes=istanbul4:ppn=24`.

### General Learnings
- Ensure users are aware of the available temporary storage options on different clusters.
- Provide clear instructions for submitting jobs to specific nodes with required resources.
- Regularly update software versions as requested by users to improve performance.

### Actions Taken by HPC Admins
- Migrated the user's home directory to the new path.
- Updated CPLEX to version 12.2 as requested by the user.
- Provided guidance on using temporary storage and submitting jobs to specific nodes.

### Follow-up
- Monitor the user's jobs to ensure they are running smoothly with the new home directory and updated software.
- Keep an eye on the usage of the Opteron machine to manage potential long wait times.
---

### 2024122042002476_Wiederholte%20Missnutzung%20der%20Dateisysteme%20-%20b241dd.md
# Ticket 2024122042002476

 # HPC Support Ticket: Repeated Misuse of File Systems

## Keywords
- File systems
- Inodes
- Project b241dd
- Server atuin
- Misuse
- HPC Admin
- Documentation links
- Weihnachtsschließung

## Summary
The HPC Admin has reduced the number of available inodes for project b241dd on server atuin from 10M to 5M due to repeated misuse of the file systems despite multiple warnings. The issue has been discussed in several tickets with the project team, but no changes in their approach have been observed.

## Root Cause
- Repeated misuse of file systems by project b241dd.
- Lack of adherence to guidelines and warnings from HPC Admins.

## Solution
- Reduction of available inodes from 10M to 5M.
- Encouragement to discuss the issue with project team members.
- Provision of documentation links for proper usage of file systems.

## Documentation Links
- [Datasets](https://doc.nhr.fau.de/data/datasets/)
- [Staging](https://doc.nhr.fau.de/data/staging/)
- [Workspaces](https://doc.nhr.fau.de/data/workspaces/)
- [HPC Café](https://hpc.fau.de/teaching/hpc-cafe/)

## Additional Notes
- During the Weihnachtsschließung, responses may be delayed.
- No response was expected from the user, as noted by the HPC Admin.

## Action Items
- Project team should review and adhere to the guidelines provided in the documentation links.
- Further misuse may result in additional restrictions or penalties.

---

This documentation is intended to help support employees address similar issues in the future.
---

### 2022032142000415_issue%20with%20quota%20on%20woody.md
# Ticket 2022032142000415

 # HPC Support Ticket: Issue with Quota on Woody

## Keywords
- Quota
- Disk usage
- `du -hs`
- Inconsistent data
- Downtime
- Quotacheck

## Problem Description
The user reported an issue with the `quota` command on `/home/woody`, which showed different numbers from `du -hs` and indicated an overuse of disk quota. The user was concerned about potential data loss.

## Root Cause
The discrepancy between `quota` and `du -hs` was likely due to an inconsistency in the quota system, which needed a `Quotacheck` to resolve.

## Solution
- **Quotacheck**: The HPC Admins performed a `Quotacheck` during a scheduled downtime.
- **Consistency**: After the `Quotacheck`, the `quota` and `du` commands showed consistent results, and the user's quota usage decreased by approximately 100 GB.

## Lessons Learned
- Regular `Quotacheck` operations are necessary to maintain consistency between `quota` and actual disk usage.
- Users should be informed about scheduled downtimes and the importance of regular backups to prevent data loss.

## Actions Taken
- The HPC Admins conducted a `Quotacheck` during the downtime.
- The quota system was synchronized, resolving the discrepancy.

## Follow-up
- Ensure regular `Quotacheck` operations are scheduled.
- Communicate with users about the importance of regular backups and the potential for quota inconsistencies.
---

### 42084065_AW%3A%20%5BFallnummer%3A42071724%5D%20HPC-Kennung.md
# Ticket 42084065

 ```markdown
# HPC Support Ticket Analysis

## Subject
AW: [Fallnummer:42071724] HPC-Kennung

## Keywords
- HPC Account
- Speicherplatz (Storage Space)
- Quota
- Home Verzeichnis (Home Directory)
- Fileserver

## Root Cause
User requested additional storage space for complex simulations but did not specify the location (fileserver/directory).

## Solution
1. **User Request:**
   - User requested 500 GB of additional storage space for their HPC account.

2. **Initial Response:**
   - HPC Admin created an HPC account for the user.
   - User was instructed to set a password for the account.

3. **Quota Management:**
   - HPC Admin clarified that the `mssgi1` quota field is obsolete.
   - Quota values are now managed directly on the HPC systems, including home directories starting with `/home/hpc/`.

4. **Clarification Needed:**
   - HPC Admin requested the user to specify the location (fileserver/directory) for the additional storage.

5. **User Clarification:**
   - User specified that the additional storage is needed in the home directory of "Woody".

6. **Quota Increase:**
   - HPC Admin increased the quota for the user's home directory on "Woody" to 500 GB soft / 1000 GB hard.

## General Learnings
- Always specify the location (fileserver/directory) when requesting additional storage space.
- Quota management for HPC accounts is handled directly on the HPC systems.
- There is no cluster-specific activation for storage; quotas are managed per user and directory.

## Conclusion
The user's request for additional storage space was successfully resolved by specifying the location and increasing the quota accordingly.
```
---

### 2015090242000687_Speicherplatzerh%C3%83%C2%B6hung.md
# Ticket 2015090242000687

 # HPC Support Ticket: Speicherplatzerhöhung

## Keywords
- Speicherplatz
- Quota
- HPC-Account
- CFD-Simulationen
- Filesystem
- /home/woody

## Problem
- User requested 500 GB storage space for CFD simulations but was only allocated 25 GB.
- Initial request lacked specific details about the filesystem.

## Root Cause
- Miscommunication regarding the specific filesystem needing increased quota.
- Initial request form did not influence actual quota allocation.

## Solution
- User clarified the request, specifying the filesystem (/home/woody).
- HPC Admin increased the quota for the specified filesystem to 500 GB.

## Lessons Learned
- Ensure specific details about the filesystem are included in storage increase requests.
- Understand that initial request forms may not directly affect quota allocation.
- Maintain professional communication even when clarifying details.

## Actions Taken
- HPC Admin increased the quota on /home/woody to 500 GB for the specified user.

## Documentation Reference
- [HPC Environment Documentation](http://www.hpc.rrze.fau.de/systeme/hpc-environment.shtml#fs)
---

### 2023041342003004_Re%3A%20iwi5124h%3A%20Soft%20Quota-Limits%20auf%20_home_woody%20erreicht%21.md
# Ticket 2023041342003004

 # HPC Support Ticket: Quota Limit Reached on /home/woody

## Keywords
- Quota limits
- Soft quota
- Hard quota
- Datasets
- Thesis
- /home/woody
- /home/janus/iwi5-datasets

## Problem
- User reached soft quota limit on `/home/woody`.
  - Used disk space: 680 GB
  - Soft quota: 600 GB
  - Hard quota: 750 GB
  - Time left: 5 days
- User requested an increase in quota for thesis work.

## Solution
- HPC Admin extended user's quota to 1.5 TB.
  - Command used: `setquota -u <username> 1500G 2T 1m 2m`
- Suggested user to upload data to `/home/janus/iwi5-datasets` if it is used by other group members.

## General Learnings
- Users should use their official email ID (e.g., @fau.de) for communication with HPC support.
- When requesting additional resources, users should specify the amount needed.
- If data is shared among group members, consider uploading it to a shared directory to optimize storage usage.

## Follow-up
- User confirmed that the extended quota was sufficient for their current tasks and models.
- Ticket was closed after user confirmation.
---

### 2016062142000645_Quota-Erweiterung%20f%C3%83%C2%BCr%20_home_woody.md
# Ticket 2016062142000645

 ```markdown
# HPC Support Ticket: Quota Increase Request

## Keywords
- Quota Increase
- HPC Account
- /home/woody
- 2TB
- Soft Quota
- Hard Quota

## Summary
A user requested an increase in their quota for the `/home/woody` directory to 2TB. The HPC Admin granted the request, setting the soft quota to 2000 GB and the hard quota to 4000 GB.

## Root Cause
- User required additional storage space for their HPC account.

## Solution
- The HPC Admin increased the user's quota to 2000 GB (soft) and 4000 GB (hard) on the `/home/woody` directory.

## General Learning
- Quota increase requests can be granted even if they exceed typical increment sizes.
- Soft and hard quotas are set to manage storage usage effectively.
```
---

### 42310383__home_vault_%20speicher%20und%20module%20rrze.md
# Ticket 42310383

 ```markdown
# HPC-Support Ticket Analysis

## Subject: /home/vault/ speicher und module rrze

### Keywords
- Storage quota
- /home/vault
- /home/woody
- mpirun_rrze
- intelmpi module
- OpenFOAM examples

### General Learnings
- **Storage Quota**: Users can request storage quota increases for `/home/vault` and `/home/woody`. `/home/vault` is for long-term archiving and may incur costs, while `/home/woody` is for short-term data and can be increased for free.
- **MPI Commands**: If an intelmpi module is loaded on the Emmy cluster, `mpirun_rrze` is available in the search path.
- **OpenFOAM Examples**: Users may need guidance on finding example scripts in the OpenFOAM module.

### Root Causes and Solutions
- **Storage Quota**:
  - **Root Cause**: User requires more storage for job results.
  - **Solution**: HPC Admins can increase the quota on `/home/woody` for free. For `/home/vault`, there may be costs involved.
- **MPI Commands**:
  - **Root Cause**: User unsure about the new command structure for `mpirun_rrze`.
  - **Solution**: Ensure the intelmpi module is loaded, which makes `mpirun_rrze` available.
- **OpenFOAM Examples**:
  - **Root Cause**: User unable to find example scripts in the OpenFOAM module.
  - **Solution**: Provide guidance on where to find example files or scripts within the OpenFOAM module.

### Additional Notes
- Users should be informed about the differences between `/home/vault` and `/home/woody` for storage purposes.
- Ensure users are aware of the automatic archiving feature of `/home/vault`.
- Provide clear documentation or links to resources for finding example scripts in modules like OpenFOAM.
```
---

### 2018052542001411_Speicheranfrage.md
# Ticket 2018052542001411

 ```markdown
# HPC-Support Ticket Conversation: Speicheranfrage

## Keywords
- Speicheranfrage (Storage Request)
- Masterarbeit (Master's Thesis)
- Große Dateien (Large Files)
- VAULT-Ordner (VAULT Folder)
- Speicherplatz (Storage Space)
- 2 TB, 3 TB, 4 TB

## Summary
A user requests additional storage space for their Master's thesis work, specifically asking to increase the storage in the VAULT folder from 2 TB to 3 or 4 TB.

## Root Cause
- The user requires more storage space for handling large files related to their Master's thesis.

## Solution
- The user has requested an increase in storage space. The HPC Admin needs to evaluate the request and potentially allocate additional storage if feasible.

## General Learning
- Users may require additional storage space for large projects, such as Master's theses.
- The VAULT folder is a common location for storing large datasets.
- Storage requests should be evaluated based on project needs and available resources.
```
---

### 2018052942001075_iwtm007h%20%3A%20storage%20on%20home%20woody.md
# Ticket 2018052942001075

 # HPC-Support Ticket Conversation Analysis

## Keywords
- HPC system
- Quota increase
- Storage
- Simulations
- ASCII files
- /home/woody
- /elxfs
- 200GB

## Summary
A new user requests a quota increase for their home directory to accommodate simulation results that generate numerous small ASCII files. The user references similar practices by other users who store data on `/home/woody` instead of the high-performance short-term storage `/elxfs`.

## Root Cause
- The user requires additional storage space for simulation results.
- Current quota is insufficient for the expected data output.

## Solution
- The user requests an increase in their home directory quota to 200GB.
- No response from HPC Admin is provided in the conversation.

## General Learnings
- Users may need increased storage quotas for specific projects.
- Storage practices can vary based on project requirements and file types.
- Communication with HPC Admins is essential for resource allocation.

## Next Steps
- HPC Admins should review the request and adjust the quota if appropriate.
- Consider providing guidelines on best practices for storage usage in the HPC environment.
---

### 2018050942000498_iwtm006h%3A%20available%20storage%20on%20home%20woody.md
# Ticket 2018050942000498

 # HPC Support Ticket: Available Storage on Home Woody

## Keywords
- HPC storage
- Home directory
- Storage quota
- Simulation data
- ASCII files

## Summary
A new HPC user inquires about the available storage on the `/home/woody` directory and requests an increase in storage quota if necessary.

## Root Cause
- User needs to store a large number of small ASCII files generated by simulations.
- Current storage quota on `/home/woody` may not be sufficient.

## Details
- User is running simulations similar to a colleague who stores results on `/home/woody` instead of high-performance short-term storage `/elxfs`.
- User requests information on the available storage for each user on `/home/woody`.
- User asks if the storage quota can be increased to 200 GB if necessary.

## Solution
- HPC Admins need to provide information on the current storage quota for `/home/woody`.
- If the quota is insufficient, HPC Admins should evaluate and potentially increase the storage quota to 200 GB for the user's account.

## General Learning
- Understanding storage options and quotas on HPC systems is crucial for users running data-intensive simulations.
- Communication with HPC Admins is necessary for adjusting storage quotas to meet specific research needs.

## Next Steps
- HPC Admins to respond with current storage quota information.
- Evaluate the feasibility of increasing the storage quota to 200 GB.
- Provide guidance on best practices for storing simulation data on HPC systems.
---

### 2023082842002739_Increasing%20space%20in%20my%20home%20folder%20%2B%20Blender%20issues%20-%20b112dc10.md
# Ticket 2023082842002739

 # HPC Support Ticket Analysis: Increasing Space in Home Folder + Blender Issues

## Keywords
- Disk space
- $HOME folder
- $WORK folder
- Blender
- GPU utilization
- Monitoring

## Summary
- **User Request**: Increased disk space for $HOME folder to store datasets.
- **HPC Admin Response**: Denied request for increased $HOME space, suggested using $WORK folder.
- **Additional Issue**: Blender jobs not utilizing GPU.

## Root Cause
- **Disk Space**: User needs more space for datasets.
- **Blender Issue**: Jobs not configured to use GPU.

## Solution
- **Disk Space**: Use $WORK folder for storing datasets.
  - Reference: [HPC Storage Documentation](https://hpc.fau.de/systems-services/documentation-instructions/hpc-storage/#work)
- **Blender Issue**: Fix Blender installation/execution to utilize GPU.
  - Reference: [Monitoring Page](https://monitoring.nhr.fau.de/monitoring/user/b112dc10) (access via [ClusterCockpit](https://portal.hpc.fau.de/))

## General Learnings
- **Storage Management**: Use appropriate storage locations for different types of data.
- **Job Configuration**: Ensure jobs are correctly configured to utilize available resources like GPUs.
- **Monitoring**: Use monitoring tools to diagnose and optimize job performance.

## Follow-Up
- **Ticket Closure**: Ticket closed as user switched to different jobs with typical GPU utilization.

---

This report provides a concise overview of the support ticket, including the root causes of the issues and the solutions provided. It serves as a reference for future support cases involving similar problems.
---

### 2022033142000594_Speicherplatz%20f%C3%83%C2%BCr%20Mirror%20von%20Russia%20Today.md
# Ticket 2022033142000594

 # HPC Support Ticket Analysis: Storage for Russia Today Mirror

## Keywords
- Storage
- Backup
- Tape
- Security
- Urheberrechtsgründen (copyright reasons)
- DFG-funded project
- Gestenanalyse (gesture analysis)
- Russia Today
- YouTube mirror
- BigDataStore
- CIO/FauDataCloud-Kontingent

## Problem
- A researcher needs secure storage and backup for a large dataset (up to 100 TB) of Russia Today videos and subtitles for a DFG-funded gesture analysis project.
- Data is currently stored on unsecured servers in the USA and FAU.
- Data cannot be made publicly accessible due to copyright reasons.

## Root Cause
- Lack of secure and backed-up storage for large datasets with specific access restrictions.

## Solution
- HPC Admin suggested using tape for data backup.
- HPC Admin offered to set up an archive account for the researcher or to handle the data backup themselves.
- The researcher was granted the necessary tape storage space for backing up the data.

## General Learnings
- Always consider data security, backup, and access restrictions when handling large datasets.
- Tape storage can be used for secure and independent data backups.
- For sensitive data, ensure it is not publicly accessible and handle it according to legal and political guidelines.
- Coordinate with HPC Admins for allocating storage and managing backups for large datasets.
---

### 2017011242000464_Re%3A%20%5BPhysik-hpc-admins%5D%20Anfrage%20Speicherplatz%20HPC%20Woody.md
# Ticket 2017011242000464

 ```markdown
# HPC Support Ticket: Storage Space Issue

## Keywords
- Storage space
- Quota
- Overquota
- Vault directory
- HPC account
- Research data

## Summary
A user encountered an overquota message due to insufficient storage space for their HPC account. The user requested an increase in their quota for the vault directory to accommodate large research data files.

## Root Cause
- The user's HPC account had insufficient storage space to handle the large data files generated from their research project.

## Solution
- The user's request was forwarded to the RRZE-Helpdesk for further assistance, as the HPC admin team could not resolve the issue directly.

## Lessons Learned
- Users should monitor their storage usage and request quota increases well in advance to avoid overquota situations.
- HPC admins should be aware of the limitations of their support capabilities and forward complex issues to the appropriate support teams.

## Next Steps
- Ensure that users are informed about their storage limits and the process for requesting quota increases.
- Document the procedure for handling storage space requests and overquota issues for future reference.
```
---

### 2024080142002626_new%20shared%20folder.md
# Ticket 2024080142002626

 # HPC Support Ticket: New Shared Folder

## Summary
- **Subject:** New shared folder
- **User Request:** Setup a new shared folder for `.zip` datasets accessible to all `iwal` users.
- **Specifications:**
  - Path: `/home/janus/iwal-datasets/acai`
  - Size: 500 GB
  - Accessible from `tinyx` and `alex`
  - Responsible user: `iwal060h`

## Conversation Highlights
- **Initial Request:** User requested a new shared folder with specific path and size.
- **Admin Response:** Directory created and user set as owner.
- **Issue:** User encountered "Disk Quota exceeded" errors despite available space.
- **Root Cause:** Excessive number of files (inodes) exceeded the limit of 100k.
- **Solution:** User was advised to delete unnecessary extracted files to free up inodes.

## Keywords
- Shared folder
- Disk quota
- Inodes
- Extracted files
- HPC Admin
- User request
- Directory creation
- Error resolution

## Lessons Learned
- **Disk Quota Errors:** Can be caused by exceeding the inode limit, not just storage space.
- **Inode Management:** Regularly check and manage the number of files to avoid inode limit issues.
- **User Communication:** Clear communication between users and HPC Admins is crucial for resolving issues efficiently.

## Action Taken
- **Directory Creation:** HPC Admin created the requested directory and assigned ownership.
- **Error Diagnosis:** HPC Admin identified the root cause of the disk quota error.
- **User Guidance:** User was advised on how to resolve the inode limit issue.

## Follow-Up
- **User Response:** User acknowledged the issue and took action to resolve it.
- **Admin Confirmation:** No further action required from HPC Admin.

This documentation can be used to diagnose and resolve similar issues in the future.
---

### 2018041042000228_%22Over%20quota%20on%20_home_hpc%22.md
# Ticket 2018041042000228

 # HPC Support Ticket: Over Quota on /home/hpc

## Keywords
- Quota
- Molecular dynamics simulations
- Woody
- Amber
- TinyGPU
- IO-Frequenz
- Data transmission

## Problem
- User received a warning for exceeding 10.5GB of data on /home/hpc.
- User is performing molecular dynamics simulations on Woody.
- User requests temporary storage beyond the hard limit of 21.0GB.

## Root Cause
- User's simulations generate large amounts of data, exceeding the allocated quota.

## Discussion
- HPC Admins discussed the user's job and data generation rate.
- The user writes data frequently, approximately every picosecond.
- Concerns raised about the user's plan to automate data transmission from /home to vault.

## Solution
- No direct solution provided in the conversation.
- Further monitoring and assistance required to manage the user's data generation and storage needs.

## General Learnings
- Molecular dynamics simulations can generate large amounts of data quickly.
- Frequent data writing can lead to quota issues.
- Automating data transmission requires careful implementation to avoid further issues.
- HPC Admins should monitor and assist users with high data generation rates.
---

### 2024121642002279_High%20File%20Count%20for%20Project%20b196ac.md
# Ticket 2024121642002279

 ```markdown
# High File Count for Project b196ac

## Keywords
- High file count
- Metadata operations
- HPC file systems
- Data formats
- File storage optimization

## Problem
- **Root Cause**: The project b196ac was storing 12 million files on the $WORK directory, causing high load and excessive metadata operations on the file system.

## Solution
- **Action Taken**: The user was notified about the issue and advised to use more suitable data formats for HPC file systems.
- **User Response**: The user deleted or archived as many files as possible and committed to using appropriate data formats in the future.

## Outcome
- **Result**: The file count was significantly reduced, improving the performance of the file system.
- **Status**: The support ticket was closed as the user complied with the recommendations.

## General Learning
- **Best Practices**: Avoid storing large quantities of small files on HPC file systems. Use data formats that minimize metadata operations.
- **Resources**: Attend monthly introductions for AI users to learn about optimizing file storage.

## References
- [HPC Café Introduction for AI Users](https://hpc.fau.de/teaching/hpc-cafe/#nutshell)
```
---

### 2024030842000802_wecapstor3%20Belegung.md
# Ticket 2024030842000802

 # HPC Support Ticket: wecapstor3 Belegung

## Keywords
- wecapstor3
- File count
- Disk usage
- Quota
- Inode limits

## Problem Description
- The `wecapstor3` storage system is experiencing performance issues due to a high number of files and significant disk usage.

## Root Cause
- Several user directories contain an excessive number of files, with one directory (`mppi098h`) having over 10 million files.
- Large disk space usage by multiple directories, with the highest being 117TB (`mppi19`).

## Details
- **File Count:**
  ```
  capn100h/: 9355
  mpo1217/: 24183
  mpp114/: 3182493
  mppi044h/: 512131
  mppi083h/: 98080
  mppi098h/: 11693699
  mppi104h/: 170727
  mppi110h/: 651028
  mppi112h/: 4518
  mppi116h/: 1157
  mppi132h/: 1431190
  mppi133h/: 2641258
  mppi136h/: 5331
  mppi142h/: 29
  mppi19/: 2667276
  ```
- **Disk Usage:**
  ```
  1.3T    capn100h
  6.4T    mpo1217
  30T     mpp114
  3.4T    mppi044h
  624G    mppi083h
  4.2T    mppi098h
  42T     mppi104h
  2.6T    mppi110h
  226G    mppi112h
  231G    mppi116h
  2.2T    mppi132h
  1.5T    mppi133h
  3.4T    mppi136h
  342G    mppi142h
  117T    mppi19
  ```

## Solution
- **Immediate Action:**
  - Users are advised to clean up their directories to reduce the number of files and disk usage.
- **Long-term Solution:**
  - Consider implementing inode and quota limits to prevent excessive file and disk usage in the future.
  - HPC Admins can technically set up these limits but have not done so previously as the hardware belongs to the users.

## Conclusion
- Regular monitoring and enforcement of storage policies can help maintain the performance of the `wecapstor3` storage system.
- Communication with users about storage best practices and the potential implementation of quotas is essential.
---

### 2025030442002271_Data%20Sharing%20in%20Workspace.md
# Ticket 2025030442002271

 # Data Sharing in Workspace

## Keywords
- Data sharing
- Workspace
- ACL (Access Control List)
- setfacl
- getfacl
- POSIX ACL

## Problem
- User wants to share a specific dataset folder within their workspace with another user without duplicating the dataset.
- User does not want to use the general method of granting read access to all HPC users.

## Root Cause
- Need for restricted data sharing between specific users.

## Solution
- Use POSIX ACL to set specific permissions for the dataset folder.
- Utilize `setfacl` and `getfacl` commands to manage access control lists.

## Steps
1. Open the workspace directory with `setfacl`.
2. Set the desired ACL for the dataset folder to grant access to the specific user.

## Resources
- [setfacl man page](https://linux.die.net/man/1/setfacl)
- [POSIX ACL documentation](https://doc.nhr.fau.de/data/share-perm-posix/)

## General Learning
- POSIX ACLs provide a flexible way to manage file and directory permissions for specific users.
- `setfacl` and `getfacl` are essential tools for setting and viewing ACLs.
- Sharing data without duplication can be efficiently managed using ACLs.
---

### 2024082242003112_Anfrage%20Speicherplatz%20Erweiterung%20%24WORK.md
# Ticket 2024082242003112

 # HPC Support Ticket: Storage Expansion Request for $WORK Directory

## Keywords
- Storage expansion
- $WORK directory
- Data transfer
- rsync
- SSH-Tunnel
- Firewall issues

## Problem Description
- User's research group started a large MRI preprocessing project.
- Project requires significant storage space (32TB) for output data.
- Current $WORK directory storage is insufficient.
- Data transfer rate and firewall issues complicate data transfer to the user's server.

## Root Cause
- Insufficient storage space in the $WORK directory.
- Inefficient data transfer methods and firewall restrictions.

## Solution
- **Storage Expansion**: HPC Admins increased the $WORK directory quota to 50TB.
- **Data Transfer**: Recommended using `rsync` via SSH-Tunnel with `csnhr.nhr.fau.de` as the source/destination for efficient data transfer.

## General Learnings
- Always consider storage requirements for large projects and request quota increases if necessary.
- Use efficient data transfer tools like `rsync` via SSH-Tunnel to handle large data transfers.
- Collaborate with system administrators to address firewall issues and optimize data transfer processes.

## Next Steps
- Monitor storage usage and request further quota increases if needed.
- Implement and test the recommended data transfer method to ensure efficient data handling.

## References
- [FAU HPC Support](https://hpc.fau.de/)
- Contact: support-hpc@fau.de
---

### 2018042642002125_elxfs%20Disk%20quota%20exceeded.md
# Ticket 2018042642002125

 # HPC Support Ticket: elxfs Disk Quota Exceeded

## Keywords
- HPC Emmy
- elxfs
- Disk quota exceeded
- mkdir error

## Problem Description
A user encountered an error while trying to create a directory using `mkdir` on the HPC Emmy system. The error message indicated that the disk quota had been exceeded.

## Root Cause
The user's disk quota on the elxfs filesystem was exceeded, preventing the creation of new directories or files.

## Solution
- **Investigation**: HPC Admins should check the user's disk quota usage on the elxfs filesystem.
- **Action**: If the quota is indeed exceeded, the user should be advised to free up space by deleting unnecessary files or requesting a quota increase if justified.

## General Learnings
- **Disk Quota Management**: Regularly monitor and manage disk quotas to prevent such issues.
- **User Communication**: Clearly communicate disk quota limits and provide guidelines on managing storage space.

## Next Steps
- **Follow-up**: Ensure the user has taken appropriate action to resolve the disk quota issue.
- **Documentation**: Update user documentation to include steps for checking and managing disk quotas.

## Related Teams
- **HPC Admins**: Thomas, Michael Meier, Anna Kahler, Katrin Nusser, Johannes Veh
- **2nd Level Support**: Lacey, Dane (fo36fizy), Kuckuk, Sebastian (sisekuck), Lange, Florian (ow86apyf), Ernst, Dominik (te42kyfo), Mayr, Martin
- **Datacenter Head**: Gerhard Wellein
- **Training and Support Group Leader**: Georg Hager
- **NHR Rechenzeit Support**: Harald Lanig
- **Software and Tools Developer**: Jan Eitzinger, Gruber
---

### 2024022742001091_Meggie_Filesystem%20%27cp%27%20gibt%20seit%20heute%20morgen%20%27Disk%20quota%20exceeded%27%20zur%C3.md
# Ticket 2024022742001091

 # HPC Support Ticket: Disk Quota Exceeded Issue

## Keywords
- Disk quota exceeded
- `cp` command
- `shownicerquota.pl`
- Filesystem maintenance
- Account migration
- Snapshots

## Problem Description
- User unable to write to `/home/vault/mpt1/mpt1014h/` despite having sufficient quota according to `shownicerquota.pl`.
- `cp` command returns "Disk quota exceeded" error.
- Recent account migration and filesystem maintenance occurred.

## Root Cause
- Incorrect quota calculation post-maintenance.

## Troubleshooting Steps
1. User checked quota using `shownicerquota.pl` and `quota` command.
2. User verified available space and compared with quota limits.
3. User suspected snapshots might be included in quota calculation but not displayed.

## Solution
- HPC Admins identified and resolved quota calculation issues post-maintenance.
- User regained write access to the filesystem.

## Lessons Learned
- Post-maintenance checks should include quota calculation verification.
- Users should be informed about potential temporary issues after maintenance.
- Snapshots and their impact on quota should be clearly communicated to users.
---

### 2024081442003781_Quota%20exceeded.md
# Ticket 2024081442003781

 # HPC Support Ticket: Quota Exceeded

## Keywords
- Quota exceeded
- Home directory
- Hidden files
- `.cache` directory
- `du` command
- `ls -a` command

## Problem Description
- User received an email indicating that their quota on `/home/hp` was exceeded.
- User checked directories but the total size did not add up to the reported quota.
- User inquired if `$WORK` or a workspace named `retriever` could be linked to `/home/hp`.

## Root Cause
- Large files in the hidden `.cache` directory, specifically `~/.cache/huggingface`, were consuming significant space.

## Solution
- HPC Admin identified the large directory using the `du -hs` command.
- Advised the user to use `ls -a` or `ls -al` to view hidden files and directories.
- Provided a link to documentation for managing Python environments to avoid similar issues in the future.

## General Learnings
- Always check hidden files and directories when investigating quota issues.
- Use `du -hs` to determine the size of directories.
- Use `ls -a` or `ls -al` to list all files, including hidden ones.
- Be aware of large caches created by applications like Huggingface.

## References
- [Python Environment Initialization](https://doc.nhr.fau.de/environment/python-env/#first-time-only-initialization)
---

### 2024121642002242_High%20File%20Count%20for%20Project%20b180dc.md
# Ticket 2024121642002242

 # HPC Support Ticket: High File Count for Project b180dc

## Keywords
- High file count
- Small files
- Metadata operations
- HPC file systems
- Storage optimization

## Summary
- **Root Cause**: Excessive number of small files stored in the project's $WORK directory, leading to high load and metadata operations on the file system.
- **Details**: The project b180dc is storing 30 million files, causing performance issues on the HPC file systems.

## Solution
- **Recommendation**: Use data formats more suited for HPC file systems.
- **Assistance**: Attend the monthly introduction for AI users for an overview of possible approaches.
- **Contact**: Reach out to the support team for assistance in optimizing file storage.

## Actions Taken
- **Notification**: HPC Admin notified the project owner about the high file count issue.
- **Queue Issue**: The ticket was initially created in the wrong queue and was moved to the correct one.

## Additional Resources
- [HPC Café Introduction for AI Users](https://hpc.fau.de/teaching/hpc-cafe/#nutshell)

## Next Steps
- Await response from the project owner regarding the optimization of file storage.
- Provide further assistance as needed.

---

This documentation aims to help support employees address similar issues related to high file counts and storage optimization on HPC systems.
---

### 2022122242000478_Quota%20Limits.md
# Ticket 2022122242000478

 # HPC Support Ticket: Quota Limits

## Keywords
- Quota Limits
- File Quota
- VAULT
- Medical Image Dataset
- Archive (tar)
- Scratch Space
- TFRecord Files
- Nvidia DALI Dataloader

## Problem Description
The user encountered file quota limits on the VAULT filesystem while storing a medical image dataset. The user received an email notification about exceeding the file quota of 200,000 files with a remaining grace time of 6 days.

## Root Cause
The VAULT filesystem has strict file quota limits due to performance issues with a large number of small files.

## Solution
- **Non-negotiable File Quota**: The file quota on VAULT is not negotiable due to system performance constraints.
- **Alternative Storage**: Use `/home/atuin/b143dc/b143dc10` for the dataset.
- **Archive and Unpack**: Create an archive (e.g., tar) of the dataset and unpack it to `/scratch` at the beginning of the job to train with local data.
- **Optimize Data Loading**: Consider repacking the dataset into TFRecord files to speed up data loading during training, similar to the approach used for ImageNet. Use Nvidia DALI dataloader for efficient data handling.

## Additional Resources
- [HPC-Cafe January 18, 2022: File Systems](https://hpc.fau.de/files/2022/01/2022-01-11-hpc-cafe-file-systems.pdf)
- [FAU.tv Clip on File Systems](https://www.fau.tv/clip/id/40199)

## Follow-up
The user is evaluating the suggested solutions and will time the process similar to the HPC-Cafe evaluation.

## Conclusion
The user needs to optimize data storage and loading methods to comply with the file quota limits on the VAULT filesystem. The suggested solutions aim to improve performance and efficiency while adhering to the system's constraints.
---

### 2023110642000651_Request%20of%20increasing%20disk%20quota%20of%20_home_vault.md
# Ticket 2023110642000651

 # HPC Support Ticket: Request of Increasing Disk Quota of /home/vault

## Summary
- **User**: Tinygpu cluster user working with high-resolution whole slide images (WSIs).
- **Issue**: Insufficient disk quota for storing large datasets (CAMELYON16 and CATCH).
- **Request**: Increase disk quota to 1300GB, later to 2TB.
- **Additional Requests**: Account extension, data sharing, and deletion of old account data.

## Key Points
- **Initial Request**: Increase disk quota to 1300GB for storing CAMELYON16 and CATCH datasets.
- **HPC Admin Response**: Increased quota to 2TB.
- **User Acknowledgement**: Continued acknowledgement in publications and linking to CRIS system.
- **Account Expiration**: User requested extension due to travel; HPC Admin extended account by 1 week.
- **Data Sharing**: User requested shared access to CAMELYON dataset; HPC Admin suggested modifying permissions.
- **Old Account Data**: User requested deletion of old account data; HPC Admin informed about automatic removal after 90 days.

## Root Cause
- **Insufficient Disk Quota**: User's work with high-resolution WSIs required more storage space.
- **Account Expiration**: User's travel led to missed account expiration, requiring extension for data transfer.

## Solutions
- **Disk Quota Increase**: HPC Admin increased the disk quota to 2TB to accommodate large datasets.
- **Account Extension**: HPC Admin extended the account by 1 week to allow for data transfer.
- **Data Sharing**: HPC Admin suggested modifying permissions for sharing datasets.
- **Old Account Data**: HPC Admin informed about automatic removal of old account data after 90 days.

## Additional Notes
- **Publication Acknowledgement**: User continued to acknowledge HPC services in publications and linked entries in the CRIS system.
- **Data Pool**: HPC Admin clarified that data pools are not yet offered but may be available in the future.

## References
- **Documentation**: [Granting HPC Users Access to Your Data](https://doc.nhr.fau.de/data/share/?h=permission#granting-hpc-users-access-to-your-data)
- **HPC Usage Reports**: [HPC Usage Reports](https://hpc.fau.de/about-us/hpc-usage-reports/)
- **CRIS System**: [CRIS System](https://cris.fau.de/)

## Conclusion
The user's requests for increased disk quota, account extension, and data sharing were addressed by the HPC Admin. The user was also informed about the automatic removal of old account data. The user continued to acknowledge HPC services in publications, contributing to the visibility and funding of the services.
---

### 2024112142003171_Request%20for%20shared%20group%20directory.md
# Ticket 2024112142003171

 # HPC Support Ticket: Request for Shared Group Directory

## Keywords
- Shared folder
- Group directory
- Large dataset
- Permissions
- Collaborators
- Software installation

## Summary
A user requested a shared folder for large dataset usage across their group. The HPC Admin identified an issue with the specified group name and corrected it. Additionally, the conversation included guidance on sharing software and libraries among group members.

## Root Cause
- Incorrect group name specified by the user (`g102e` instead of `g102ea`).

## Solution
- The HPC Admin corrected the group name and created the shared directory at `/home/atuin/g102ea`.
- The HPC Admin provided documentation on granting permissions to group members for software sharing.

## General Learnings
- Ensure correct group names when requesting shared directories.
- Shared directories are typically created for complex collaborations or large datasets.
- For simpler collaborations, granting permissions to group members is sufficient and easier.
- Documentation on sharing permissions is available at [https://doc.nhr.fau.de/data/share-perm-posix/#granting-read-access-to-members-of-your-group](https://doc.nhr.fau.de/data/share-perm-posix/#granting-read-access-to-members-of-your-group).

## Next Steps
- Verify the correct group name before submitting requests.
- Refer to the provided documentation for granting permissions to group members.
- For complex collaborations, request a dedicated group-shared directory.
---

### 2024022742002901_getting%20quota%20extension%20on%20tinyx%20for%20user%20iwal139h.md
# Ticket 2024022742002901

 # HPC Support Ticket: Quota Extension Issue on tinyx

## Keywords
- Quota extension
- Home directory quota
- Pip install error
- No space left on device
- Conda environment
- Pytorch installation

## Summary
A user encountered an error while trying to install a package in their conda environment due to insufficient space in their home directory. The user requested a quota extension but was advised to use the `$WORK` directory for Python environments.

## Root Cause
- The user's home directory quota was not exceeded, but there was a delay in the internal quota accounting catching up after the user deleted multiple GB of data.
- The user attempted to install a large package (Pytorch) in their home directory, which triggered the "No space left on device" error.

## Solution
- The HPC Admins recommended using the `$WORK` directory for Python environments as quota increases for the home directory are not offered.
- The user was informed that they should be able to write to their home directory again after the quota accounting caught up.

## General Learnings
- Large packages should be installed in the `$WORK` directory to avoid home directory quota issues.
- There may be a delay in quota accounting after deleting large amounts of data.
- Quota increases for the home directory are not offered, and users should manage their storage accordingly.

## Related Commands
- `du -sh ~ --exclude=directory`: Check home directory usage excluding specific directories.
- `df -h ~`: Check filesystem disk space usage.
- `pip install package==version -f url`: Install a specific package version from a given URL.

## Ticket Conversation
- The user reported an error while installing a Pytorch version in their conda environment due to insufficient space.
- The HPC Admins discussed the user's quota and usage history, noting that the user had deleted multiple GB of data.
- The HPC Admins advised the user to use the `$WORK` directory for Python environments and informed them that they should be able to write to their home directory again.
---

### 2018072042000687_Question%20regarding%20number%20of%20files%20on%20emmy%20cluster%20fasttmp%20directory.md
# Ticket 2018072042000687

 # HPC Support Ticket: File Deletion in Fasttmp Directory

## Keywords
- Emmy cluster
- Fasttmp directory
- File deletion
- File limits
- High-water-mark deletion

## Summary
A user reported that simulation output files were automatically deleted from the `fasttmp` directory on the Emmy cluster. The user was unsure if the issue was due to their simulations, reaching the file number limit, or total file size limit.

## Root Cause
- No high-water-mark deletion or system incident occurred on the cluster.
- The cluster has no individual capacity limit but limits the number of files per account to 50,000.
- The system does not delete files once the limit is reached; it prevents the creation of new files or directories.

## Solution
- The reason for the disappearing files is likely on the user's side.
- The user should check their simulations and scripts for any potential issues causing file deletion.

## General Learnings
- The Emmy cluster does not have an individual capacity limit for users.
- The number of files per account on the parallel file system is limited to 50,000.
- Reaching the file limit prevents the creation of new files or directories but does not result in automatic file deletion.
- Users should use the correct email address for support requests and expect a response within a reasonable timeframe.

## Follow-up Actions
- Users should review their simulations and scripts to identify any issues that may cause file deletion.
- If the problem persists, users should provide additional details to the HPC support team for further investigation.
---

### 2021052042002691_Quota-Erh%C3%83%C2%B6hung.md
# Ticket 2021052042002691

 # HPC Support Ticket: Quota Increase

## Keywords
- Quota Increase
- $HPCVAULT
- A100-Knoten
- TinyGPU
- Sprachmodelle
- Trainingsdaten

## Problem
- User requires more storage space for training data (1 TB) which exceeds their current quota.
- User needs to train language models on A100 nodes of TinyGPU.

## Root Cause
- Insufficient storage quota for the user's training data.

## Solution
- HPC Admin increased the user's quota on $HPCVAULT to 2 TB.

## General Learning
- Users can request quota increases if their current storage is insufficient for their workload.
- HPC Admins can adjust quotas as needed to accommodate user requirements.
- $HPCVAULT is a suitable location for storing large training datasets.

## Roles Involved
- **HPC Admins**: Responsible for managing and adjusting user quotas.
- **2nd Level Support Team**: Provides additional support and troubleshooting if needed.
- **Head of the Datacenter**: Oversees overall datacenter operations.
- **Training and Support Group Leader**: Manages training and support activities.
- **NHR Rechenzeit Support**: Handles applications for grants and support.
- **Software and Tools Developer**: Develops and maintains software tools for HPC.

## Conclusion
- Users should specify their storage needs and request quota increases if necessary.
- HPC Admins can assist by adjusting quotas to ensure users have sufficient storage for their projects.
---

### 2023042642003258_HPC%20Speicher%20Erweiterung%20-%20iwso084h.md
# Ticket 2023042642003258

 # HPC Support Ticket: Storage Quota Increase for Medical Image Data Project

## Keywords
- Storage Quota Increase
- Medical Image Data
- File System Optimization
- Data Privacy

## Summary
A student required additional storage space for a research project involving medical image data. The standard quota of 500GB was insufficient, and a request was made to increase the quota on either $WOODY or $HPCVAULT.

## Problem
- **Root Cause**: The student's project required more storage space than the standard quota allowed.
- **Additional Issue**: The user's directory contained a large number of small files and almost empty directories, which could affect the stability of the data server.

## Solution
- **Quota Increase**: The HPC Admin increased the quota on $WOODY to 3TB.
- **File System Optimization**: The HPC Admin advised the user to use different file formats or archive the data to reduce the number of small files. Relevant resources were provided for further guidance.
- **Data Privacy**: The HPC Admin reminded the user that processing personal data is not permitted on HPC systems.

## Follow-up
- The user clarified that the large number of files were deprecated and could be deleted or archived.
- The HPC Admin confirmed that the majority of the files were located in a specific dataset directory and provided further advice on archiving or converting the data.

## Resources
- [HPC Café: File Systems](https://hpc.fau.de/files/2022/01/2022-01-11-hpc-cafe-file-systems.pdf)
- [FAU.tv: File Systems](https://www.fau.tv/clip/id/40199)

## General Lessons
- **Storage Quota**: Users may require additional storage space for specific projects. The HPC Admin can increase the quota on a case-by-case basis.
- **File System Optimization**: A large number of small files can impact the stability of the data server. Users should be advised to use appropriate file formats or archive data when necessary.
- **Data Privacy**: Users should be reminded about data privacy policies, especially when handling sensitive data such as medical images.
---

### 2023012742001996_Speicherplatzbedarf%20HPC-Cluster.md
# Ticket 2023012742001996

 # HPC Support Ticket: Speicherplatzbedarf HPC-Cluster

## Keywords
- Speicherplatzbedarf
- Quota
- User Quota
- HPC-Cluster
- Messkampagnen
- EMPKINS
- CDI
- Vault
- Fundus

## Problem
- User requires additional storage space (70-100 TB) for upcoming measurement campaigns.
- Current storage is under `\home\vault\empkins`.
- User queries if the data volume can be stored under the same directory with adjusted user quotas.

## Root Cause
- The user needs to store a large amount of data (70-100 TB) for upcoming measurement campaigns.
- The current quota system limits storage per user or group, not per directory.

## Solution
- EMPKINS has been allocated a total of 100 TB by CDI.
- HPC Admins can adjust user quotas to accommodate the required storage.
- User requested to increase the quota for `empk004h` to 70 TB initially.
- HPC Admin adjusted the quota for `empk004h` to 70 TB soft and 80 TB hard.

## General Learnings
- Quotas on the HPC cluster can be managed per user or group, not per directory.
- Adjustments to user quotas can be made to accommodate large data storage requirements.
- Communication with the HPC support team is essential to ensure proper allocation and management of storage resources.

## Actions Taken
- HPC Admin confirmed the total storage allocation for EMPKINS.
- User requested specific quota adjustments.
- HPC Admin adjusted the quota for the specified user account.

## Conclusion
- The user's storage requirements were met by adjusting the user quota.
- The HPC support team provided clear communication and timely resolution to the user's request.
---

### 42320495_quota.md
# Ticket 42320495

 # HPC Support Ticket Conversation Analysis

## Keywords
- Quota
- Hard quota
- Atomistic simulations
- GROMACS 5
- Cluster
- Installation

## General Learnings
- Users may exceed their storage quota due to running large simulations.
- Users should request additional quota if they anticipate needing more storage.
- HPC admins can adjust quotas to accommodate user needs.
- Users may need to switch to newer versions of software for their projects.
- HPC admins can provide information on software availability and installation.

## Root Cause of Problems
1. **Quota Issue:**
   - User exceeded their storage quota due to running large atomistic simulations.
   - User needed additional storage to complete their simulations.

2. **Software Version Query:**
   - User needed to know if a newer version of GROMACS (version 5) was installed on the cluster for an upcoming project.

## Solutions
1. **Quota Issue:**
   - HPC admin increased the user's quota to accommodate the additional storage needed for the simulations.

2. **Software Version Query:**
   - HPC admin addressed the query by checking the availability of GROMACS 5 on the cluster.

## Documentation for Support Employees
- **Quota Management:**
  - If a user exceeds their quota, verify the necessity of additional storage.
  - Adjust the quota as needed to ensure the user can complete their work.
  - Remind users to clean up their storage after completing their tasks.

- **Software Availability:**
  - When users inquire about specific software versions, check the cluster for the requested version.
  - Provide clear instructions on how to access or install the software if available.
  - If the software is not available, guide the user on how to request its installation.

## Additional Notes
- Always ensure users are aware of their storage limits and the process for requesting additional quota.
- Maintain clear communication with users regarding software availability and updates.
---

### 42324814_Userquota%20auf%20woody.md
# Ticket 42324814

 # HPC Support Ticket: User Quota Increase Request

## Keywords
- User quota
- Soft quota limit
- Quota increase
- Home directory
- Vault storage
- Doctoral research
- Data analysis

## Summary
A user encountered issues with their soft quota limit while conducting research for their doctoral thesis. The user requested an increase in their quota to accommodate additional data analysis.

## Root Cause
- The user's current quota limit was insufficient for their research needs.
- The user had already deleted unnecessary files and utilized vault storage but still required more space.

## Solution
- The HPC Admin increased the user's quota on the specified home directory (`/home/woody`).

## Lessons Learned
- Users conducting extensive research may require higher quota limits.
- It is important to monitor and adjust quotas based on user needs to ensure smooth operation.
- Providing clear instructions for requesting quota increases can help users manage their storage more effectively.

## Actions Taken
- The HPC Admin increased the user's quota by approximately 500 GB.

## Follow-up
- Ensure that the user's quota increase meets their research needs.
- Monitor the user's storage usage to prevent future quota issues.

## References
- HPC Services
- Friedrich-Alexander-Universitaet Erlangen-Nuernberg
- Regionales RechenZentrum Erlangen (RRZE)
- [HPC Services Website](http://www.hpc.rrze.fau.de/)
---

### 42321949_Userquota%20auf%20woody.md
# Ticket 42321949

 # HPC Support Ticket: User Quota Increase on Woody

## Keywords
- User quota
- Soft quota limitation
- Quota increase
- Doktorarbeit (PhD thesis)
- wnfs1:/srv/home
- /home/woody
- IDM account
- Benutzername (username)
- Gruppe (group)

## Problem Description
- User encountered soft quota limitation while working on their PhD thesis.
- Despite deleting unnecessary files and using vault for results, the user still required more storage space.
- The user requested an increase in their quota on `wnfs1:/srv/home` (mounted as `/home/woody`).

## Root Cause
- Insufficient storage quota for the user's computational needs.

## Solution
- HPC Admin increased the user's quota on `/home/woody`.

## General Learnings
- Users may require quota increases for large computational projects.
- When requesting a quota increase, users should provide:
  - Reason for the request (e.g., PhD thesis work)
  - Specific storage location (e.g., `/home/woody`)
  - Estimated additional storage needed (e.g., 500 GB or 300 GB)
  - Relevant account information (e.g., IDM account, username, group)
- HPC Admins can resolve such issues by increasing the user's quota as appropriate.
---

### 2022030242002217_Speicherplatz-Miete.md
# Ticket 2022030242002217

 # HPC-Support Ticket: Speicherplatz-Miete

## Keywords
- DFG-Geld
- Storage
- FAIR
- Rechnung
- Hardwarekauf
- Miete
- Datenaufbewahrung
- HPCVAULT

## Problem
- User has 1200 EUR of DFG funds that need to be spent by the end of March.
- User is considering renting storage space to keep project data FAIR.
- User is open to other solutions.

## Discussion
- HPC Admin suggests that renting storage for 1200 EUR is a viable option.
- User specifies that the data needs to be stored for 10 years, which amounts to approximately 10TB at current rental prices.
- HPC Admin expresses concerns about guaranteeing storage for 10 years due to hardware changes and data migration.
- User and HPC Admin discuss the possibility of hardware participation, but it is deemed not cost-effective for small units.
- User eventually finds another solution to spend the funds.

## Solution
- No specific solution was implemented through this ticket, but the discussion highlights the challenges and considerations for long-term data storage and funding.

## General Learnings
- Long-term data storage requires planning for hardware changes and data migration.
- FAIR principles should be considered when storing research data.
- DFG funds can be used for renting storage or hardware purchases, but the expenditure should not appear as basic equipment.
- Collaboration with other departments (e.g., AGFD/CDI) may be necessary for comprehensive data management solutions.

## Root Cause
- The need to spend DFG funds within a short timeframe while ensuring long-term, FAIR-compliant data storage.

## Resolution
- User found an alternative solution to spend the funds.
- The discussion underscored the importance of planning for long-term data storage and the challenges associated with it.
---

### 2024110642000881_Inquiry%20on%20Workspace%20Suitability%20for%20Large%20Dataset%20Training%20on%20Alex%20Cluster.md
# Ticket 2024110642000881

 # HPC Support Ticket: Workspace Suitability for Large Dataset Training on Alex Cluster

## Keywords
- Large dataset
- Workspace mechanism
- NVMe Lustre (anvme) storage
- Disk quota
- Node-local GPU storage
- Data handling
- HPC-Café
- Inodes quota

## Problem
- User has a large dataset (~2.5 TB, ~60,000 files) and lacks disk quota to upload it to `/home/hpc`, `/home/vault`, or `/home/woody`.
- Copying data to node-local GPU storage for each training session is time-intensive.
- User is exploring the workspace mechanism as a solution.

## Questions
1. Would the workspace allow efficient access during training, or would data still need to be copied to node-local GPU storage?
2. Are there any quota limits for using the workspace mechanism?

## Solution
- **Workspace Suitability**: The workspace mechanism (NVMe Lustre (anvme) storage) is suitable for this use case. It should allow efficient access during training, but the user can test if copying data to node-local storage is still necessary.
- **Quota Limits**: There is a quota for inodes but not for the data volume. More information can be found [here](https://doc.nhr.fau.de/data/filesystems/).
- **Additional Resources**: The user is advised to watch the HPC-Café recording on data handling, available [here](https://hpc.fau.de/teaching/hpc-cafe/#HPC-Caf%C3%A9-2024).

## Additional Information
- The user has already consulted several resources on the workspace mechanism but is open to more suggestions.
- The HPC Admins and the 2nd Level Support team provided guidance on the suitability of the workspace mechanism and the quota limits.

## Conclusion
The workspace mechanism is a viable solution for handling large datasets on the Alex cluster. Users should test the efficiency of accessing data directly from the workspace versus copying it to node-local storage. There are no data volume quotas, but inode quotas apply. Additional resources like the HPC-Café recording can provide further insights into data handling.
---

### 2018032242002661_storrage.md
# Ticket 2018032242002661

 ```markdown
# HPC Support Ticket: Shared Directory for Large Data Storage

## Keywords
- Shared Directory
- Large Data
- Backup
- Temporary Storage

## Problem Description
The user is looking for a shared directory on the Woody system where they can store large data. The data does not need to be backed up but should persist for a few days.

## HPC Admin Response
The HPC Admin suggested using the directory `$WOODYHOME = /home/woody/mp24/mp24002h` and inquired about the size of the "large data."

## Solution
- **Directory Suggestion**: `$WOODYHOME = /home/woody/mp24/mp24002h`
- **Clarification Needed**: Definition of "large data"

## General Learnings
- Users may need temporary storage for large data that does not require backup.
- Specific directories can be suggested for such needs, but the size of the data should be clarified.
```
---

### 2021051042000863_Fwd%3A%20Fwd%3A%20Over%20quota%20on%20_home_vault.md
# Ticket 2021051042000863

 # HPC Support Ticket: Over Quota on /home/vault

## Keywords
- File quota
- Block quota
- Inode quota
- Compression
- Grace period
- Soft quota
- Hard quota

## Summary
A user group encountered a file quota exceeded message while transferring data to `/home/vault/gwgi/gwgifu0h`. The group requested an increase in their file quota to accommodate their expanding data storage needs.

## Root Cause
- The user group had exceeded their file quota of 1,000,000 files.
- The group was transferring a large number of small files, which led to the quota being exceeded.

## Solution
- **HPC Admin** doubled the inode quota to 2M.
- **HPC Admin** recommended compressing the files to reduce the number of inodes used.
- The user group agreed to consider compressing files where feasible.

## General Learnings
- Large numbers of small files can quickly exceed file quotas.
- Compression can be an effective way to manage file quotas.
- Regular monitoring and adjustment of quotas may be necessary for groups with expanding data storage needs.
- Communication between users and HPC support is crucial for finding sustainable solutions to storage issues.

## Ticket Status
- The ticket was closed after the inode quota was increased and the user group acknowledged the recommendation for compression.
---

### 2021090842000904_Soft_Hard%20Quota.md
# Ticket 2021090842000904

 # HPC-Support Ticket Conversation: Soft/Hard Quota

## Keywords
- Soft Quota
- Hard Quota
- Simulation Data
- Storage
- NHR-Rechenzeitantrag
- GPU-Stunden
- FAU-Grundversorgung

## Summary
The user requested an increase in their soft and hard quotas for simulation data. The HPC Admins provided guidance on appropriate storage locations and the process for requesting additional resources.

## Root Cause
- The user needed more storage space for simulation data.
- The user was initially using the home directory for simulation data, which is not intended for such purposes.

## Solution
- The HPC Admins advised the user to use `/home/woody` (`$WORK`) or `/home/vault` (`$HPCVAULT`) for simulation data.
- The user's quota on `/home/vault` was increased to 1 TB soft / 2 TB hard.
- Further quota increases were denied due to the user's high GPU usage and the need to submit an NHR-Rechenzeitantrag for additional resources.

## General Learnings
- The home directory is not intended for large simulation data.
- Users should utilize designated storage locations for specific types of data.
- Quota increases may be granted on a case-by-case basis, but repeated increases are not guaranteed.
- High resource usage may require submitting an NHR-Rechenzeitantrag for additional resources.
- Information on available file systems and their intended uses can be found in the HPC storage documentation.

## References
- [HPC Storage Documentation](https://hpc.fau.de/systems-services/systems-documentation-instructions/hpc-storage/)
- [NHR Application Rules](https://hpc.fau.de/systems-services/documentation-instructions/nhr-application-rules/)
---

### 2018091342001491_mpt4012h%20-%20Speicherplatz%20auf%20_home_vault.md
# Ticket 2018091342001491

 # HPC Support Ticket Conversation Analysis

## Keywords
- Speicherplatz (storage space)
- /home/vault
- MD Simulationen (molecular dynamics simulations)
- Quota
- NFS-Work/Projekt-Storage
- HPC-Erweiterungen (HPC expansions)
- Beteiligung (participation)
- Rechnung (invoice)
- Backup
- RAID6

## General Learnings
- Users may request additional storage space for specific projects.
- HPC admins can adjust quotas for users upon request.
- There are options for additional NFS storage with specific costs and conditions.
- Communication about storage options and costs is important for users.

## Root Cause of the Problem
- User required additional storage space for longer MD simulations.

## Solution
- HPC admin increased the quota for the user on /home/vault to 600 GB soft/900 GB hard.

## Additional Information
- HPC admin reminded the user about an email regarding options for additional NFS storage.
- The email detailed costs and conditions for participating in the acquisition of additional NFS storage.

```markdown
# HPC Support Ticket Conversation Analysis

## Keywords
- Speicherplatz (storage space)
- /home/vault
- MD Simulationen (molecular dynamics simulations)
- Quota
- NFS-Work/Projekt-Storage
- HPC-Erweiterungen (HPC expansions)
- Beteiligung (participation)
- Rechnung (invoice)
- Backup
- RAID6

## General Learnings
- Users may request additional storage space for specific projects.
- HPC admins can adjust quotas for users upon request.
- There are options for additional NFS storage with specific costs and conditions.
- Communication about storage options and costs is important for users.

## Root Cause of the Problem
- User required additional storage space for longer MD simulations.

## Solution
- HPC admin increased the quota for the user on /home/vault to 600 GB soft/900 GB hard.

## Additional Information
- HPC admin reminded the user about an email regarding options for additional NFS storage.
- The email detailed costs and conditions for participating in the acquisition of additional NFS storage.
```
---

### 2025031242003139_Need%20assistanc%20to%20clean%20the%20disk%20space.md
# Ticket 2025031242003139

 # HPC Support Ticket: Disk Space Management

## Problem
- User encountered an error while installing Python packages due to exceeded disk quota.
- `OSError: [Errno 122] Disk quota exceeded`
- Large files and directories in `$HOME`:
  - `/home/hpc/iwi5/iwi5276h/.cache/pip` (70G)
  - `/home/hpc/iwi5/iwi5276h/.local/lib/python3.11/site-packages` (28G)
  - Other large directories related to Python packages and caches.

## Root Cause
- User stored large amounts of data and Python packages in `$HOME`, exceeding the soft quota.
- Python packages and caches were installed in the default location (`$HOME`).

## Solution
- Move large files and directories to appropriate storage systems like `$WORK`.
- Configure Python environment to install packages in a directory other than `$HOME`.
- Follow the documentation on Python environments to set up the installation path correctly.

## Keywords
- Disk quota exceeded
- Python packages
- pip cache
- $HOME
- $WORK
- Python environment configuration

## General Learnings
- Always check disk quota and usage before installing large packages.
- Store large files and directories in appropriate storage systems like `$WORK`.
- Configure Python environments to use directories other than `$HOME` for package installations.
- Follow the provided documentation for setting up Python environments correctly.

## Documentation Links
- [Data Filesystems](https://doc.nhr.fau.de/data/filesystems/)
- [Python Environment Setup](https://doc.nhr.fau.de/environment/python-env)

## Resolution
- User resolved the issue by configuring the PATH correctly for Python package installations.
- Moved large directories to `$WORK` to free up space in `$HOME`.

## Closure
- Ticket closed with the resolution that data should be moved to other filesystems like `$WORK`.
- "Stuff" from the internet (downloaded Python environments, Huggingface data) should not be stored in `$HOME`.
---

### 2022100442005117_Quota%20iwtm016h.md
# Ticket 2022100442005117

 # HPC Support Ticket: Quota Issue on Meggie

## Keywords
- Quota
- Hard Quota
- Soft Quota
- Grace Period
- ZFS
- Job Notifications
- sbatch

## Problem Description
- User encountered issues with storage quota on Meggie, specifically on the `/home/woody` directory.
- Hard quota limit was reached at around 450 GB, preventing further file storage.
- User expected a grace period similar to Emmy, where the storage limit could be exceeded for about a week.
- User did not receive quota or job notifications despite using `sbatch` with the `--mail-user` and `--mail-type=ALL` options.

## Root Cause
- The `/home/woody` directory uses the ZFS file system, which only supports hard quotas and does not have a grace period.
- Email notifications from the batch system were not functioning properly.

## Solution
- HPC Admins increased the user's quota on `/home/woody` to 1 TB as a temporary measure.
- Email notifications from the batch system were fixed and should now be functioning correctly.

## General Learnings
- ZFS file system does not support soft quotas or grace periods.
- Ensure email notifications are properly configured and functional for job and quota alerts.
- Users should be informed about the specific quota policies and file system behaviors on different HPC systems.
---

### 2018080942002007_Watermark-deletion%20Algorithmus%20f%C3%83%C2%BCr%20Einsatz%20auf%20einem%20unserer%20Rechner..md
# Ticket 2018080942002007

 # HPC Support Ticket: High Watermark Deletion Algorithm

## Keywords
- High watermark deletion
- Perl script
- Recursive listing
- File deletion
- HPC workspace

## Summary
A user inquired about the high watermark deletion algorithm used by the HPC support team, with the intention of implementing something similar on their own system.

## Root Cause
The user was interested in understanding the high watermark deletion algorithm to implement a similar solution on their own system.

## Solution
The HPC Admin provided details about the Perl script used for high watermark deletion:
- The script performs a recursive listing of all directories and files.
- It maintains a list of entries in memory, with a configurable limit to avoid excessive memory usage.
- When the limit is reached, the script sorts the list and removes the newest 10% of entries.
- The final sorted list is then used to delete files, starting with the oldest, until the desired amount of storage is freed.

The HPC Admin also mentioned that the script has some limitations, such as race conditions and lack of support for hard links, and recommended an alternative approach using [hpc-workspace](https://github.com/holgerBerger/hpc-workspace), which is used by HLRS.

## Conclusion
The user found the alternative approach helpful and thanked the HPC Admin for the recommendation.

## Additional Notes
- The script has been in use for 10 years despite its limitations.
- The HPC Admin advised against using the script due to its limitations and recommended exploring more robust solutions.
---

### 2023021742001155_Neuer%20shared%20order%20am%20Vault.md
# Ticket 2023021742001155

 # HPC Support Ticket: New Shared Folder Request

## Keywords
- Shared folder
- Permissions
- Vault
- Data storage
- Group access

## Summary
A user requested the creation of a new shared folder with write permissions for their group during an important beamtime at a large research facility.

## Root Cause
- User lacked permissions to create a new folder in the existing shared directory.

## Solution
- HPC Admin created a new shared folder `/home/vault/capm/shared/data` with write permissions for the group `cahmadmin`.

## General Learnings
- Users may require additional permissions or admin intervention to create shared folders.
- Quick response from HPC support is crucial during time-sensitive research activities.
- Clear communication of the folder path and permissions granted is essential.

## Follow-up
- Ensure users are aware of the new folder path and permissions.
- Document the process for creating shared folders with group permissions for future reference.
---

### 201808239001171_Re%3A%20%5BRRZE-HPC%5D%20aktuelle%20M%C3%83%C2%B6glichkeiten%20zur%20Beteiligung%20an%20kleineren%20.md
# Ticket 201808239001171

 # HPC-Support Ticket Conversation Analysis

## Keywords
- Storage
- Beteiligung
- HPC-Erweiterungen
- NFS-Storage
- Geld
- Anträge
- Deadline
- Rechnungstellung
- Konfiguration
- IO-Durchsatz
- Quota

## General Learnings
- **Funding for Storage**: The conversation revolves around securing funding for a large, cost-optimized NFS-Storage system.
- **Deadlines and Commitments**: The importance of meeting deadlines and providing verifiable commitments for funding.
- **Communication**: Effective communication and follow-up are crucial for ensuring that all parties are on the same page regarding funding and project progress.
- **Flexibility**: There is a need for flexibility in funding amounts, as the user's ability to contribute may vary based on available resources.

## Root Cause of the Problem
- **Funding Availability**: The user is uncertain about the exact amount of funding they can contribute due to pending applications and financial constraints.

## Solution
- **Verifiable Commitment**: The user commits to a minimum contribution of 5k€, with the possibility of increasing to 10k€ if necessary.
- **Rechnungstellung**: The HPC Admin initiates the billing process for the user's contribution.
- **Storage Configuration**: The HPC Admin configures and optimizes the storage system, ensuring it is available for use by the user's group with a specified quota.

## Documentation for Support Employees
- **Funding Requests**: When handling funding requests, ensure clear communication about deadlines and required contributions.
- **Flexibility in Contributions**: Be prepared to accommodate varying levels of financial contributions from users.
- **Follow-up**: Regularly follow up with users to confirm their commitments and address any concerns or changes in their ability to contribute.
- **Billing and Configuration**: Once funding is secured, promptly initiate the billing process and configure the storage system according to the user's requirements.

This documentation can serve as a reference for handling similar funding requests and storage configurations in the future.
---

### 2020102242000323_Quota.md
# Ticket 2020102242000323

 # HPC Support Ticket: Quota Issue

## Keywords
- Quota
- Hard-Limit
- Fileserver
- Additional Storage
- Simulation Data

## Summary
- **User Issue**: The user's working group does not have a fileserver, leading to the need to store large simulation data on `/home/hpc`. The user's quota is approaching the hard limit.
- **Request**: The user requests additional storage space until their fileserver is available.

## Root Cause
- Lack of dedicated fileserver for the user's working group.
- Large simulation data exceeding the current quota.

## Solution
- **Pending**: The HPC Admin has not yet responded with a solution.

## General Learnings
- Users may require temporary additional storage when their working group does not have a dedicated fileserver.
- Large simulation data can quickly exhaust user quotas.
- It is important to have a process in place for handling temporary storage requests.

## Next Steps
- HPC Admin should evaluate the request and provide additional storage if feasible.
- Consider implementing a policy for handling temporary storage needs.
---

### 42026336_HPC%20Zugange.md
# Ticket 42026336

 ```markdown
# HPC Support Ticket: Access Issues and Quota Clarification

## Keywords
- Account setup
- Archive access
- Directory access
- Quota
- Home directory
- HPC fileservers
- Backup policy

## Summary
A user encountered issues with accessing the archive and a specific directory (`cluster32`), and had questions about their quota.

## Root Cause
1. **Archive Access**: Technical problems prevented the archive access from being set up initially.
2. **Directory Access**: The user's directory existed but they were unable to access it.
3. **Quota Misunderstanding**: The user misinterpreted the quota size displayed by the `quota -v` command.

## Solution
1. **Archive Access**: The archive access was scheduled to be automatically set up over the weekend.
2. **Directory Access**: The HPC Admin confirmed the existence of the user's directory and requested more information on the access issue.
3. **Quota Clarification**: The HPC Admin explained that the quota size is in kilobytes, not bytes, resulting in a 100 MB quota for the home directory and 10 GB for HPC fileservers.

## General Learnings
- **Automatic Setup**: Some access permissions are set up automatically over the weekend.
- **Quota Units**: Ensure users understand the units of quota sizes (kilobytes vs. bytes).
- **Backup Policy**: HPC fileservers have larger quotas but no backup, as documented on the HPC website.

## Documentation Links
- [HPC Fileserver Documentation](http://www.rrze.uni-erlangen.de/dienste/arbeiten-rechnen/hpc/systeme/woodcrest-cluster.shtml#fs)
```
---

### 2024080442000757_Disk%20quota%20exceeded%20in%20alex%20-%20atuin%20_%20b143dc.md
# Ticket 2024080442000757

 # HPC Support Ticket: Disk Quota Exceeded in alex - atuin / b143dc

## Keywords
- Disk quota exceeded
- Python script error
- `shownicerquota.pl`
- Group quota
- ZFS file quota
- Eduroam WiFi
- VSCode

## Problem Description
- User encountered a "disk quota exceeded" error in a Python script.
- The error occurred despite the system quota check via `shownicerquota.pl` not indicating an exceeded quota.

## Root Cause
- The group `b143dc` had a file quota of 10M but was using 21M files.
- The quota enforcement might have been delayed or recently set.

## Solution
- HPC Admins increased the group file quota to 25M to allow the group to continue working.
- User deleted some files in the `$WORK` directory to stay under the 1TB limit.

## Additional Issue
- User reported slow connection and inference when using Eduroam WiFi and VSCode to access the HPC system.

## Response to Additional Issue
- HPC Admins were not aware of any stability or speed issues on their end.
- Suggested potential changes on the Eduroam side or in VSCode as possible causes.

## Notes
- The ticket highlights the importance of checking and managing both file and storage quotas.
- It also underscores the need to investigate external factors when troubleshooting connectivity issues.

## Actions Taken
- Increased group file quota.
- Advised user on managing storage usage.
- Provided information on potential causes of connectivity issues.

## Follow-up
- Monitor group file usage to ensure compliance with the new quota.
- Keep an eye on any reported connectivity issues to identify patterns or widespread problems.
---

### 2018080742000361_HPC%20account%20problem.md
# Ticket 2018080742000361

 # HPC Account Problem: Disk Quota Issue

## Keywords
- Disk quota
- FOAM FATAL ERROR
- Directory creation error
- Parallel file system
- Lustre filesystem
- Hidden files
- Quota limits

## Problem Description
A user reported issues with running simulations on their HPC account. Previously, the user could run simulations on 8 nodes (320 processors) without issues. However, recently, the user encountered errors when trying to run simulations on even 2 nodes. The errors included:
- "FOAM FATAL ERROR: Couldn't create directory"
- "Running out of disk quota"

## Root Cause
The root cause of the problem was the user exceeding the disk quota for the number of files and directories on the `$FASTTMP` parallel file system. The user had reached the limit of 500,000 files and directories and was in the grace period, which had expired.

## Troubleshooting Steps
1. **User Report**: The user reported the issue with detailed error messages.
2. **Admin Response**: The HPC admin identified the disk quota issue and provided information about the limits on the parallel file system.
3. **Quota Check**: The admin checked the user's quota using the command `lfs quota -u <username> /elxfs/`.
4. **File Count**: The admin used the command `find /elxfs/iwst/iwst041h/ | wc -l` to count the number of files and directories in the user's account.
5. **Temporary Quota Increase**: The admin temporarily increased the quota to allow the user to continue working while investigating the issue further.

## Solution
The admin increased the quota limits to 700,000 and 800,000 files and directories as a temporary workaround. The admin also suspected that the issue might be related to deleted but still open files or a problem with the Lustre quotas. The admin planned to check and reset the quota in a month and monitor the situation after the next Lustre failover.

## General Learnings
- **Disk Quota Limits**: Be aware of the disk quota limits for files and directories on parallel file systems.
- **Grace Period**: Understand the grace period for exceeding disk quotas and the consequences of reaching the limit.
- **Temporary Workarounds**: Temporary quota increases can be used as a workaround while investigating the root cause of the issue.
- **Lustre Filesystem**: Issues with the Lustre filesystem, such as deleted but still open files, can affect disk quotas.

## Future Actions
- Monitor the user's disk quota usage.
- Check and reset the quota if necessary.
- Investigate the Lustre filesystem for any underlying issues that may affect disk quotas.
---

### 2021050342002839_Problem%20mit%20Quota%20Checker.md
# Ticket 2021050342002839

 # HPC Support Ticket: Problem mit Quota Checker

## Keywords
- Quota
- Storage
- Filesystem
- Blocks
- Grace Period
- Soft Quota
- Hard Quota
- HPC Admin
- 2nd Level Support

## Summary
A user received a quota warning despite deleting large amounts of data. The user's visible data did not match the reported quota usage.

## Root Cause
- The user had deleted large files but still received quota warnings.
- The user's visible data (~200 KB) did not match the reported quota usage (~37 GB).

## Solution
- HPC Admin confirmed the current quota usage was below the limit.
- The user was advised to check the documentation for appropriate storage locations for large data.
- The issue of invisible data usage was not resolved in the conversation.

## General Learnings
- Quota warnings may persist even after deleting data due to grace periods.
- Users should be aware of appropriate storage locations for different types of data.
- Invisible data usage can be a source of confusion and may require further investigation.

## Next Steps
- Investigate the cause of invisible data usage.
- Ensure users are aware of storage best practices and documentation.

## References
- [HPC Storage Documentation](https://hpc.fau.de/systems-services/systems-documentation-instructions/hpc-storage/#overview)
---

### 2016042942000974_Request%20for%20more%20storage%20space%20quota%28HPC%29.md
# Ticket 2016042942000974

 # HPC Support Ticket: Request for More Storage Space Quota

## Keywords
- Storage quota
- Filesystem
- Simulations
- StarCCM+
- HPC-Kennung

## Summary
A user requested an increase in their storage quota due to the large space requirements of their simulation software, StarCCM+.

## Root Cause
- The user's current storage quota of 10.5G is insufficient for running simulations with fine mesh, which can exceed 10G of space.

## Request Details
- Increase storage quota to at least 30G.
- User's HPC-Kennung: iwst006h

## Actions Taken
- The ticket was acknowledged by an HPC Admin and presumably forwarded to the relevant team for processing.

## Resolution
- The resolution is not explicitly stated in the provided conversation. The standard procedure for quota increase requests should be followed, including review and approval by the appropriate authorities.

## General Learnings
- Users running specific simulation software may require larger storage quotas.
- It is important to review and adjust storage quotas based on user needs and system capacity.
- Always acknowledge and forward tickets to the relevant team for prompt resolution.
---

### 2022100442001201_Over%20quota-Meldung.md
# Ticket 2022100442001201

 # HPC Support Ticket: Over Quota Message

## Keywords
- Over quota
- HPC access
- Expired access
- Storage cleanup
- Temporary reactivation

## Problem
- User received daily "Over quota on /home/hpc" emails after their HPC access expired.
- User could not delete files due to expired access.

## Root Cause
- User's HPC access expired, preventing them from managing their storage.
- Storage quota was exceeded due to large files from previous computations.

## Solution
- HPC Admin temporarily reactivated the user's access to allow them to clean up their storage.
- User confirmed successful cleanup.

## General Learnings
- Temporary reactivation of expired accounts can help users resolve outstanding issues.
- Regularly remind users to clean up their storage before access expiration to prevent over quota issues.
---

### 2025030442004091_Disk%20Usage%20Discrepancy%20on%20%20Home%20Directory%20for%20Account%20b237dc10.md
# Ticket 2025030442004091

 ```markdown
# Disk Usage Discrepancy on Home Directory

## Problem Description
- User reports a discrepancy between the total size of files in their home directory (82 GB) and the size reported by `shownicerquota.pl` (106.5 GB).
- User is unable to recompile codes due to exceeding the soft quota limit.

## Root Cause
- The quota is calculated based on file ownership, not directory location.
- User has multiple accounts, and files owned by the user in other home directories contribute to the quota.

## Keywords
- Disk usage discrepancy
- Quota limit
- File ownership
- Multiple accounts

## Solution
1. **Check File Ownership**: Use `find . -type f -user <username>` to identify files owned by the user in other directories.
2. **Move Files**: Move files to `$WORK` directory and create soft links in `$HOME` if necessary.
3. **Verify Quota**: Use `shownicerquota.pl` to verify the quota usage after moving files.

## Lessons Learned
- Quota is calculated based on file ownership, not directory location.
- Users with multiple accounts should check file ownership across all accounts.
- Regularly move non-critical files to `$WORK` to avoid exceeding quota limits.
```
---

### 2024122342000472_Disable%20.Trash-1000%20directory.md
# Ticket 2024122342000472

 # HPC Support Ticket: Disable .Trash-1000 Directory

## Keywords
- .Trash-1000
- Storage quota
- Deleted files
- Trashbin application
- Dummy file

## Problem Description
The user is running experiments and temporarily storing logs in the `$HPCVAULT` directory. After syncing, the logs are deleted locally to avoid exceeding the storage quota. However, the `.Trash-1000` directory retains deleted files, causing the user to exceed the storage quota.

## Root Cause
The `.Trash-1000` directory is created by the trashbin application of the operating system, which moves deleted files into this directory instead of permanently deleting them.

## Solution
To prevent deleted files from being moved to the `.Trash-1000` directory, create a dummy file with the same name:

```bash
rm -rf .Trash-1000
touch .Trash-1000
```

This will ensure that files are immediately deleted permanently.

## General Learning
- The `.Trash-1000` directory is a feature of the operating system's trashbin application and cannot be disabled by HPC Admins.
- Creating a dummy file with the name `.Trash-1000` prevents deleted files from being moved to this directory.
- This solution helps users manage their storage quota more effectively by ensuring that deleted files are permanently removed.
---

### 2022091342003239_tinyGPU%20qouta%20issue.md
# Ticket 2022091342003239

 # HPC Support Ticket: tinyGPU Quota Issue

## Keywords
- Quota system
- Disk quota exceeded
- Connection refused
- Login-node
- Soft quota

## Problem Description
- User reported an issue with the quota system on tinyGPU.
- Running the `quota` command returned a connection refused error for a specific filesystem.
- User's disk usage was within the soft quota limit, but encountered a "Disk quota exceeded" error while running `tar`.

## Root Cause
- The issue occurred on the login-node (woody3).
- Possible temporary exceeding of the soft quota (500GB) during a failed extraction process.

## Solution
- HPC Admin increased the user's quota on $WORK.
- User was advised to report back if additional space was needed.

## General Learnings
- Quota issues can occur even if the current usage is within limits, possibly due to temporary spikes during operations.
- Increasing the quota can resolve such issues.
- It's important to check if the issue is specific to a particular node.
---

### 42173384_SoftQuota.md
# Ticket 42173384

 ```markdown
# HPC-Support Ticket: SoftQuota

## Keywords
- Soft Quota
- Hard Quota
- Simulation
- Storage
- Vault
- HPC Cluster

## Summary
A user requested an increase in their soft quota for simulations on the HPC cluster. The initial request was for 1 TB, but the admin increased it to 500 GB soft / 1000 GB hard. The user later reached their hard quota and requested an increase back to the original 1 TB soft quota.

## Root Cause
- User required more storage for simulation results.
- Initial quota increase was insufficient for the user's needs.

## Solution
- The HPC Admin increased the soft quota to 1 TB as originally requested.

## Lessons Learned
- Always specify the username and the specific file system when requesting quota changes.
- Provide a detailed justification for the requested quota increase.
- Monitor storage usage and request adjustments as needed to avoid reaching hard quotas.

## Actions Taken
- HPC Admin increased the soft quota to 500 GB and hard quota to 1000 GB initially.
- After the user reached the hard quota, the soft quota was increased to 1 TB.
```
---

### 2020031142000974_reached%20the%20limit%20of%20my%20soft-quota%20in%20_home_woody_.md
# Ticket 2020031142000974

 # HPC Support Ticket: Soft-Quota Limit Reached

## Keywords
- Soft-quota limit
- Home directory
- Quota increase

## Problem
- User received an email indicating that they have reached the soft-quota limit in their home directory (`/home/woody/`).

## Root Cause
- The user's storage usage in the home directory exceeded the allocated soft-quota limit.

## Solution
- **HPC Admin** increased the user's quota on `/home/woody` to 500/750 GB.

## General Learnings
- Users should monitor their storage usage to avoid reaching quota limits.
- If a user reaches their quota limit, they can request an increase from the HPC Admin team.
- The HPC Admin team can adjust quotas as needed to accommodate user requirements.

## Next Steps for Similar Issues
- Verify the user's current storage usage.
- If necessary, increase the user's quota to an appropriate level.
- Inform the user about the new quota limits and best practices for storage management.
---

### 42089863_Quota.md
# Ticket 42089863

 # HPC Support Ticket: Quota Issue

## Keywords
- Quota
- Grace Period
- Data Transfer
- Slow Data Transfer
- Account Over Quota

## Problem
- User's account (iwst10) exceeded quota.
- Slow data transfer rates hindering cleanup efforts.
- User unable to perform computations due to quota limitations.

## Root Cause
- Account exceeded allocated quota.
- Slow data transfer rates.

## Solution
- HPC Admin reset the grace period, providing an additional 7 days for the user to clean up data.

## General Learnings
- Users may request temporary quota increases or grace period resets when they exceed their allocated storage.
- Slow data transfer rates can complicate cleanup efforts, necessitating additional time for users to manage their data.

## Actions Taken
- HPC Admin reset the grace period for the user's account.

## Follow-Up
- User acknowledged the reset and thanked the HPC Admin.

## Notes
- Ensure users are aware of their quota limits and the importance of regular data management to avoid such issues.
- Consider providing guidance on optimizing data transfer rates to facilitate cleanup processes.
---

### 2024091942003822_help.md
# Ticket 2024091942003822

 # HPC Support Ticket: Disk Quota Exceeded

## Keywords
- Disk quota exceeded
- Home directory
- Log files
- $WORK directory
- $HPCVAULT

## Problem
- **User Issue:** User `gwgi023h` encountered a "Disk quota exceeded" error despite deleting a significant amount of data.
- **Root Cause:** Large log files in `/home/hpc/gwgi/gwgi023h/projects/Bello/scripts/rgi60-11/meta_batchscript/` occupying approximately 100 GB.

## Solution
- **HPC Admin Response:**
  - Inform the user that the home directory still contains too much data.
  - Suggest moving data to the `$WORK` directory or `$HPCVAULT` to avoid future quota issues.
  - Provide a link to documentation on filesystems: [FAU Data Filesystems](https://doc.nhr.fau.de/data/filesystems/).

## General Learnings
- Regularly check and manage disk usage in the home directory.
- Utilize alternative storage locations like `$WORK` and `$HPCVAULT` for large datasets.
- Be mindful of log files that can accumulate and consume significant disk space.

## Documentation Link
- [FAU Data Filesystems](https://doc.nhr.fau.de/data/filesystems/)
---

### 2023071042001542_Storage%20quota.md
# Ticket 2023071042001542

 # Storage Quota Increase Request

## Keywords
- Storage quota
- Woody
- 1TB
- setquota
- HPC Admin
- User credentials

## Problem
- **User Request:** Increase storage quota on "woody" to at least 1TB.
- **User Credentials:**
  - IDM: be01mosi
  - HPC: iwb3009h

## Solution
- **Admin Action:** HPC Admin increased the quota using the command:
  ```bash
  setquota -u iwb3009h 1T 1500G 5000k 7500k .
  ```
- **Result:** User's quota on `/home/woody` was successfully increased to 1TB.

## General Learnings
- Users can request storage quota increases by providing their credentials.
- HPC Admins can adjust quotas using the `setquota` command.
- Proper communication and quick response from HPC Admins ensure user satisfaction.

## Notes
- Ensure that the certificate is valid to avoid any expiration issues during the process.
- Always confirm the quota change with the user to ensure the request has been fulfilled correctly.
---

### 42118785_Datenl%C3%83%C2%B6schung.md
# Ticket 42118785

 # HPC Support Ticket: Data Deletion

## Keywords
- Data deletion
- High watermark deletion
- Temporary storage
- Backup
- Quota

## Summary
A user reported that their data was deleted from the Woody-rechner HPC system. The deletion occurred due to a high watermark deletion process, which removes older files to free up space when the filesystem is full.

## Root Cause
- The user's data was stored in a temporary storage area (`/wsfs`) intended for short-term use.
- The high watermark deletion process removed files older than a certain date to manage storage space.
- The user was unaware of the deletion process and did not have time to back up their data.

## Solution
- The HPC Admin was able to restore some of the user's critical files from a backup.
- The user was advised to store important data in a more permanent location (`/home/woody`) with a quota, rather than in temporary storage.

## Lessons Learned
- Users should be aware of the temporary nature of certain storage areas and the potential for automatic deletion of old files.
- Important data should be stored in locations with appropriate backup and retention policies.
- Regular communication about storage policies and best practices can help prevent data loss.

## Actions Taken
- The HPC Admin restored the user's critical files from a backup.
- The user was advised on proper data storage practices to prevent future data loss.

## Follow-Up
- Ensure users are informed about storage policies and the risks associated with temporary storage.
- Provide guidelines on how to manage and back up important data.

## References
- HPC storage policies
- Data backup and retention practices

---

This report can be used as a reference for support employees to understand and resolve similar issues related to data deletion and storage management.
---

### 2023091442000069_Clearing%20Cache%20in%20Workspace.md
# Ticket 2023091442000069

 # HPC Support Ticket: Clearing Cache in Workspace

## Keywords
- Jupyter server
- Disk usage
- `.cache` directory
- Account quota
- Snapshots
- HPC storage

## Problem
- **User Issue**: Frequent restarts of Jupyter server.
- **User Action**: Checked disk usage in home folder using `du -h | sort -h`.
- **User Query**: Can the `.cache` directory be manually cleaned up?

## HPC Admin Response
- **Disk Space**: Restart issues are unlikely due to disk space as the user is not close to the account quota.
- **Cache Cleanup**: No issues expected from cleaning up the `.cache` directory. Snapshots can be used to restore if needed.
- **Storage Locations**: Additional storage available at `$HPCVAULT` and `$WORK`.
- **Documentation**: Refer to [HPC Storage Documentation](https://hpc.fau.de/systems-services/documentation-instructions/hpc-storage/) for more information.

## Solution
- **Cache Cleanup**: User can manually clean up the `.cache` directory.
- **Storage Management**: Utilize additional storage locations (`$HPCVAULT` and `$WORK`) for better space management.

## Additional Notes
- **Quota**: User inquired about the account quota, which was not explicitly confirmed in the conversation.
- **Restart Issue**: The root cause of the Jupyter server restarts was not identified in this conversation. Further investigation may be needed.

## Documentation Link
- [HPC Storage Documentation](https://hpc.fau.de/systems-services/documentation-instructions/hpc-storage/)
---

### 2024070842002231_Fwd%3A%20%5BBHR-FRAU%5D%20Lehrstuhlaccount%20K%C3%83%C2%BChl.md
# Ticket 2024070842002231

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Keywords
- HPC Cluster
- Lehrstuhlaccount
- Data Storage
- $WORK Quota
- ML-Model Training
- Project Setup
- User Accounts

## General Learnings
- **Project Setup**: The process of setting up a project for a department involves identifying a Principal Investigator (PI) and a Point of Contact (PoC).
- **Data Storage**: Large data requirements for research projects can be accommodated by extending the $WORK quota on the HPC cluster.
- **User Management**: Invitations for HPC access can be sent via the HPC Portal, with each invited user receiving an account within the project.
- **Communication**: Effective communication between the HPC support team and users is crucial for resolving issues and ensuring smooth operation.

## Root Cause of the Problem
- The user required additional storage space (4 TB) for a research project involving ML-model training.
- There was a need to clarify whether the storage should be allocated to a personal account or a departmental project.

## Solution
- The HPC Admin allocated a 10 TB quota on the $WORK directory for the departmental project (v105cb).
- The user was informed that all members of the department would have access to this storage.

## Documentation for Support Employees
### Setting Up a Departmental Project
1. **Identify PI and PoC**: Determine the Principal Investigator (PI) and Point of Contact (PoC) for the project.
2. **Gather Information**: Collect necessary information such as postal addresses and email addresses.
3. **Create Project**: Set up the project in the HPC system, ensuring that the PI and PoC can invite other users.
4. **Allocate Storage**: Assign the required storage quota to the project, typically on the $WORK directory.

### Extending Storage Quota
1. **Assess Requirements**: Understand the storage needs of the user or project.
2. **Allocate Quota**: Extend the $WORK quota as needed, ensuring that all project members have access.
3. **Communicate**: Inform the user about the allocated storage and how to access it.

### User Management
1. **Invitations**: Use the HPC Portal to send invitations to users who need access to the project.
2. **Account Creation**: Automatically create accounts for invited users within the project.
3. **Responsibility**: Ensure that the PI and PoC are aware of their responsibilities in managing the project and user access.
```
---

### 2025021242002267_Request%20for%20Increased%20Storage%20Quota%20on%20HPC%20Cluster.md
# Ticket 2025021242002267

 # HPC Support Ticket: Request for Increased Storage Quota

## Keywords
- Storage Quota
- Home Directory
- $WORK Directory
- Deep Learning
- Dataset Storage
- Model Checkpoints
- Experimental Results

## Problem
- **Root Cause:** User exceeded allocated storage quota on `/hpcdatacloud/hpchome/shared`.
- **Details:**
  - Username: `iwnt129h`
  - Current Usage: 133GB
  - Quota Limit: 100GB
  - Hard Limit: 200GB
  - User is working on deep learning-based plastic material classification using multispectral imaging.

## Solution
- **Action Taken:** HPC Admin advised the user to move data to the `$WORK` directory, which has more space.
- **Additional Information:**
  - The storage quota for the home directory cannot be increased.
  - Referenced documentation: [FAU Data Filesystems](https://doc.nhr.fau.de/data/filesystems/)

## General Learning
- **Storage Management:** Users should be aware of different filesystems and their intended use.
- **Alternative Storage Solutions:** Utilize the `$WORK` directory for large datasets and temporary files.
- **Documentation:** Always refer users to relevant documentation for self-service solutions.

## Follow-Up
- Ensure the user understands how to move data to the `$WORK` directory.
- Monitor the user's storage usage to prevent future quota issues.
---

### 2024112042001308_Shared%20directory%20on%20Fritz.md
# Ticket 2024112042001308

 # HPC Support Ticket: Shared Directory on Fritz

## Keywords
- Shared directory
- Software installation
- Group access
- Permissions
- Collaborators
- Students
- Unix group

## Problem
- User wants to install software for MRI image processing with special libraries.
- Needs to share the software and linked libraries with collaborators and students.
- Asks if a dedicated group-shared directory is a suitable solution.

## Root Cause
- User requires a shared space for software installation and access by multiple users.

## Solution
- **Group-Shared Directory**: HPC Admins can create dedicated group-shared directories, but it is usually not necessary unless there are complex collaboration needs, multiple users requiring write access, or large shared datasets.
- **Unix Group Permissions**: If all collaborators and students are in the same Unix group (e.g., accounts starting with "mfqb") and only one person is building the software, it is easier to grant access to the group members for the built software.
- **Documentation**: Instructions for granting permissions to the group are available at [FAU Documentation](https://doc.nhr.fau.de/data/share-perm-posix/#granting-read-access-to-members-of-your-group).

## General Learnings
- Evaluate the need for a dedicated group-shared directory based on the complexity of collaboration and data sharing requirements.
- Utilize Unix group permissions for simpler sharing scenarios.
- Refer to documentation for detailed instructions on granting group access.

## Roles Involved
- **HPC Admins**: Provide guidance and create shared directories if necessary.
- **User**: Requests assistance and implements the solution based on the provided guidance.
---

### 2015101342000663_speicherplatz%20woodyhome.md
# Ticket 2015101342000663

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject: speicherplatz woodyhome

### Keywords:
- Speicherplatz (storage space)
- Woodyhome
- Homeverzeichnis (home directory)
- Quote (quota)
- Erweiterung (extension)

### Summary:
- **User Request**: Increase storage space for `woodyhome` and `home` directories.
- **Current Quota**:
  - Woodyhome: 25.0G
  - Homeverzeichnis: 10.5G
- **Requested Quota**:
  - Woodyhome: 300.0G
  - Homeverzeichnis: 21.0G

### Root Cause:
- Insufficient storage space for user's data sets.

### Solution:
- **HPC Admins** need to evaluate and potentially increase the storage quota for the user's `woodyhome` and `home` directories.
- **2nd Level Support Team** may assist in assessing the feasibility and impact of the quota increase.

### General Learnings:
- Users may require additional storage space for their projects.
- Proper evaluation and communication with HPC Admins and 2nd Level Support Team are crucial for resolving storage quota issues.
```
---

### 2024020942002284_RE%3A%20Over%20quota%20on%20at%20least%20one%20filesystem.md
# Ticket 2024020942002284

 ```markdown
# HPC Support Ticket: Over Quota on Filesystem

## Keywords
- Quota
- Filesystem
- /home/hpc
- /home/vault
- Replication
- Usage

## Problem
- User received a warning about being over quota on at least one filesystem.
- The error message indicated that the user was over quota on `/home/hpc`.
- User calculated total space usage as 53 GB, but the system reported 111.5 GB.

## Root Cause
- Data on `/home/hpc` and `/home/vault` is replicated to two different disc arrays.
- This replication counts towards the quota usage twice.

## Solution
- The usable quota is effectively halved due to replication.
- User can move some data to `/home/vault` or `/home/hpc`.
- Repositories that can be easily downloaded again can be located at `$WORK` without backup.

## Additional Information
- For more details on different filesystems, refer to the [HPC Storage Documentation](https://hpc.fau.de/systems-services/documentation-instructions/hpc-storage/).
```
---

### 2022110442000941_Speicherplatz%20auf%20Vault.md
# Ticket 2022110442000941

 ```markdown
# HPC-Support Ticket Conversation: Storage Quota Increase

## Keywords
- Storage quota
- Vault
- Speicherplatzlimit
- Quota increase
- HPC Benutzername
- Universitäre Emailadresse

## Summary
- **User Issue**: User exceeded storage quota on Vault and requested an increase of approximately 500GB due to anticipated additional video data.
- **Root Cause**: Insufficient storage quota for user's project needs.
- **Solution**: HPC Admin increased the user's quota on Vault to 1 TB.

## Lessons Learned
- Users should use their university email address for communication with HPC support.
- Storage quotas can be increased upon request if justified by project needs.
- HPC Admins can quickly address quota increase requests to ensure smooth project operations.

## Actions Taken
- HPC Admin doubled the user's storage quota on Vault to 1 TB.
- User was reminded to use their university email address for future communications.
```
---

### 2024090442003814_Datenpublikation%20einer%20Ver%C3%83%C2%B6ffentlichung.md
# Ticket 2024090442003814

 # HPC Support Ticket: Data Publication for Research

## Keywords
- Data publication
- HPC storage
- Zenodo
- DOI
- Public access
- Data archiving

## Problem
- User wants to publish a dataset as part of a research publication.
- Data is currently stored on HPC storage, which is not publicly accessible.
- User seeks options to make the data publicly available via a URL on the project website.

## Solution
- **Zenodo** is recommended for data publication.
  - Allows data sets up to 50 GB.
  - Provides a DOI for citation.
  - Ensures long-term data availability.
  - No cost involved.
- Reference link: [Zenodo](https://zenodo.org/)
- Additional information: [FAU Library - Data Archiving and Publication](https://ub.fau.de/forschen/daten-software-forschung/archivierung-und-publikation-der-daten/#collapse_2)

## General Learnings
- Zenodo is a suitable platform for publishing research data.
- Ensure data sets are within the size limit (50 GB) for Zenodo.
- Providing a DOI is crucial for citation and long-term accessibility.
- Always check with the data protection officer for legal compliance before publication.

## Root Cause
- Data stored on HPC storage is not publicly accessible.
- Need for a platform to host and share research data publicly.

## Resolution
- Use Zenodo to publish the dataset.
- Ensure the dataset is divided into chunks of 50 GB or less if necessary.
- Obtain a DOI for the dataset to ensure proper citation and long-term availability.
---

### 2021050442002042_Image%20Net.md
# Ticket 2021050442002042

 ```markdown
# HPC-Support Ticket: Image Net

## Summary
- **Subject:** Image Net
- **Issue:** Sharing a large dataset (Image-Net) with multiple users on the HPC system.
- **Root Cause:** Incorrect file permissions preventing access to the dataset.
- **Solution:** Adjust file permissions using `chmod` to allow read access for others.

## Keywords
- Image-Net
- File permissions
- chmod
- HPC
- Dataset sharing

## Ticket Conversation

### User Request
- **Request:** Sharing the Image-Net dataset (~155 GB) with all users of a specific department or the entire HPC system.
- **Reason:** To save time and resources by avoiding individual dataset downloads.

### HPC Admin Response
- **Solution:** Use `chmod -R o+rX` to set read permissions for others.
- **Caution:** Ensure only the dataset and necessary directories are shared, not the entire home directory.

### User Follow-up
- **Issue:** Colleagues unable to access the dataset despite setting permissions.
- **Details:** Permissions set correctly for the dataset directory but not for the parent directory.

### HPC Admin Follow-up
- **Diagnosis:** Colleagues lack access to the parent directory `/home/woody/iwso/iwso009h`.
- **Solution:** Apply `chmod o+rX /home/woody/iwso/iwso009h` to grant access to the parent directory.

### User Confirmation
- **Result:** Successful access to the dataset after applying the suggested permissions.

## Lessons Learned
- **File Permissions:** Ensure all parent directories have the necessary permissions for access.
- **chmod Command:** Use `chmod -R o+rX` to set read permissions for others recursively.
- **Security:** Be cautious when setting permissions to avoid exposing sensitive data.

## Conclusion
- **Resolution:** The dataset was successfully shared by adjusting file permissions for the dataset and its parent directories.
- **Future Reference:** This solution can be applied to similar issues involving dataset sharing on the HPC system.
```
---

### 42314821_Mehr%20quota%20auf%20woody.md
# Ticket 42314821

 # HPC Support Ticket: Request for Increased Quota on Woody Home

## Keywords
- Quota Increase
- Woody Home
- Storage Limit
- Resource Management

## Summary
A user requested an increase in their quota on the Woody home directory due to reaching their current limit.

## Root Cause
- User reached their storage quota limit on the Woody home directory.

## Solution
- HPC Admin increased the user's quota to 600 GB soft / 1200 GB hard.

## Lessons Learned
- Storage space on HPC clusters is a limited and valuable resource.
- Users should be aware of their storage usage and request quota increases when necessary.
- HPC Admins can adjust quotas to accommodate user needs within reasonable limits.

## Actions Taken
- HPC Admin reviewed the request and increased the user's quota accordingly.

## Follow-up
- No further action required unless the user needs additional quota in the future.
---

### 2023090642002261_Uebertrag%20Dataset%20cluster.md
# Ticket 2023090642002261

 ```markdown
# HPC-Support Ticket: Sharing Data Between Users

## Keywords
- Data sharing
- Permissions
- HPCVAULT
- Group directory
- cp/scp/rsync

## Problem
- User wants to share data stored in `$HPCVAULT` with another user without downloading it from the system.

## Root Cause
- User needs a method to share data within the HPC environment without downloading and re-uploading.

## Solution
- **Permissions**: Adjust file permissions to allow other users to access the data.
  - Reference: [FAQ on cross-using data between HPC accounts](https://hpc.fau.de/faqs/#i-would-like-to-cross-use-data-between-hpc-accounts)
- **Group Directory**: Use the group-specific directory for data sharing.
  - Directory: `/home/janus/iwi5-dataset`
  - Methods: `cp`, `scp`, `rsync`

## Steps Taken
1. User inquired about sharing data without downloading.
2. HPC Admin suggested adjusting permissions and using the group directory for data sharing.
3. User acknowledged the solution.

## Conclusion
- The ticket was closed after the user was provided with the necessary information to share data within the HPC environment.
```
---

### 2017111742000936_quota%20auf%20WOODYCAP.md
# Ticket 2017111742000936

 ```markdown
# HPC Support Ticket: Quota Issue on WOODYCAP

## Keywords
- quota
- shownicerquota.pl
- woodycap3
- woodycap4
- home/woody
- home/vault
- home/hpc

## Problem Description
- User reported that the `quota` command on `woodycap3` only displays `home/woody`.
- `home/vault` and `home/hpc` are not shown.
- The issue affects both `quota` and `shownicerquota.pl`.
- On `woodycap4`, `home/vault` and `home/woody` are visible.

## Root Cause
- The root cause of the problem was not explicitly stated in the conversation.

## Solution
- The HPC Admin mentioned that the problem should be resolved.
- It was noted that the issue had been present for about a week.

## General Learnings
- Issues with the `quota` command can affect visibility of certain directories.
- Similar problems might occur on different nodes (e.g., `woodycap3` vs `woodycap4`).
- Quick resolution and communication with users are essential for maintaining system functionality.
```
---

### 2020042042000713_mppi090h.md
# Ticket 2020042042000713

 # HPC Support Ticket: mppi090h

## Keywords
- Home directory
- Grace period
- Storage quota
- Trash directory
- Account access

## Summary
- **User Issue**: User unable to log in due to expired grace period and excessive storage usage in the home directory.
- **Root Cause**: Large files in the `.local/share/Trash` directory.
- **Solution**: HPC Admin reset the grace period and identified large files in the trash directory.

## Details
- **User**: Unable to log in due to expired grace period and excessive storage usage.
- **HPC Admin**:
  - Reset the grace period.
  - Identified large files in `/home/hpc/capm/mppi090h/.local/share/Trash/`.
  - Provided a list of large files contributing to the storage issue.

## Lessons Learned
- Regularly check and clean the `.local/share/Trash` directory to avoid storage quota issues.
- Resetting the grace period can temporarily restore account access for troubleshooting.
- Large files in the trash directory can significantly impact storage usage.

## Action Items
- **User**: Delete or move large files from the trash directory to free up storage.
- **HPC Admin**: Monitor user storage usage and provide guidance on managing storage quotas.

## Follow-Up
- Ensure the user has successfully logged in and resolved the storage issue.
- Provide additional guidance on managing storage quotas and avoiding similar issues in the future.
---

### 42098934_Bitte%20Account%20dkpfeiff%20l%C3%83%C2%B6schen.md
# Ticket 42098934

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject: Bitte Account dkpfeiff löschen

### Keywords:
- Account Deletion
- Quota Exceeded
- CIP Pool
- Informatik
- Gasthörer

### Summary:
A user requested the deletion of their account due to exceeding their disk quota and no longer needing the account as they were no longer a student. The conversation involved identifying the correct system and department responsible for the account.

### Root Cause of the Problem:
- User exceeded disk quota.
- User no longer needed the account.

### Steps Taken:
1. **Initial Request**: User requested account deletion due to exceeding disk quota and no longer being a student.
2. **Clarification**: HPC Admin requested clarification on the system from which the account originated.
3. **User Response**: User provided additional information, indicating they were a guest student in the Informatik department.
4. **Identification**: HPC Admin identified the account as belonging to the CIP Pool of the Informatik department.
5. **Forwarding**: The request was forwarded to the Informatik department for account deletion.

### Solution:
- The account deletion request was forwarded to the Informatik department, which has its own user management system.
- The user confirmed they did not need any data from the account, allowing for its deletion.

### General Learnings:
- Importance of identifying the correct system and department for account management.
- Collaboration between different departments for user support.
- Handling of account deletion requests and disk quota issues.

### Conclusion:
The issue was resolved by forwarding the request to the appropriate department. The user's account was identified as part of the Informatik CIP Pool, and the deletion process was initiated by the Informatik department.
```
---

### 2024121342001507_Asking%20about%20the%20share%20folder%20for%20training%20data.md
# Ticket 2024121342001507

 ```markdown
# HPC Support Ticket: Sharing Training Data with Students

## Keywords
- Data Sharing
- Training Data
- Share Folder
- $WORK Directory
- License Compliance

## Problem
- User needs to share a 16 GB training dataset with students for DL model training exercises.
- User inquires about creating a share folder in `/home/hpc/mrvl/`.

## Solution
- **HPC Admin** suggests creating a directory on `$WORK` and sharing it with the students.
- Reference documentation: [Data Sharing Guide](https://doc.nhr.fau.de/data/share/)
- User must ensure the dataset can be shared legally (license compliance).

## Lessons Learned
- Use `$WORK` directory for sharing large datasets with multiple users.
- Ensure compliance with data sharing licenses.
- Refer to the official documentation for detailed instructions on data sharing.
```
---

### 2024010842003947_Regarding%20sharing%20data%20between%20different%20phD%20students.md
# Ticket 2024010842003947

 # HPC Support Ticket: Sharing Data Between PhD Students

## Keywords
- Data Sharing
- NHR Project
- Shared Quota
- Read/Write Permissions
- Group Access

## Problem
- User needs to share approximately 8-10 TB of data among different PhD students for training AI models using Alex or tinyGPU clusters.
- Requires a shared space to avoid multiple data transfers and storage.

## Solution
- **Shared Directory Creation**: HPC Admin created a shared directory `/home/atuin/$PROJECT/shared/` with read and write permissions for the group.
- **Permissions**: Users can add read permissions for their group to access data in their user directory.
- **Complexity**: If users belong to different groups, additional steps may be required.

## Steps Taken
1. HPC Admin confirmed the user's account within an NHR project.
2. HPC Admin created the shared directory with the necessary permissions.
3. User verified the path of the shared directory.

## Outcome
- Shared directory `/home/atuin/b144dc/shared/` was successfully created and confirmed.
- Users can now access the shared data without duplicating storage.

## Notes
- Each NHR project has a shared quota of >= 10TB at `/home/atuin/$PROJECT`.
- Further assistance can be provided if users belong to different groups.

## Closure
- The ticket was closed after the shared directory was created and confirmed.
---

### 42054797_woody%20account%20quota.md
# Ticket 42054797

 ```markdown
# HPC Support Ticket: Woody Account Quota Issue and Alias Configuration

## Keywords
- Disk quota
- Aliases
- .bashrc
- .cshrc
- Shell configuration

## Summary
A user reported a disk quota exceeded error while running a simulation, despite using only 1 GB out of 10 GB. Additionally, the user was unable to create aliases in their account.

## Root Cause
- **Disk Quota Issue**: The user was actually using 1 out of 100 GB, indicating a misunderstanding of the quota limits. The error was likely due to writing to the wrong directory.
- **Alias Configuration Issue**: The default shell on the HPC systems is csh, not bash. Aliases defined in `.bashrc` do not work in csh.

## Solution
- **Disk Quota Issue**: The user was advised to check the directory they were writing to and ensure it was within the correct quota limits.
- **Alias Configuration Issue**: The user was instructed to define aliases in the `.cshrc` file instead of `.bashrc`. The syntax for aliases in csh is different from bash.

## Steps to Resolve
1. **Disk Quota Issue**:
   - Verify the correct quota limits.
   - Ensure the simulation is writing to the correct directory.

2. **Alias Configuration Issue**:
   - Create a `.cshrc` file in the home directory if it does not exist.
   - Define aliases in the `.cshrc` file using the correct csh syntax.
   - Example: `alias ll 'ls -l'`
   - To test the aliases, use the command `source .cshrc`.

## Additional Notes
- The `.cshrc` file will be automatically executed upon the next login.
- The user can also request to change the default shell to bash if preferred.
```
---

### 42170975_Over%20quota%20on%20_home_vault.md
# Ticket 42170975

 # HPC Support Ticket: Over Quota on /home/vault

## Keywords
- Quota
- /home/vault
- Email Notifications
- Account Name
- Username-Email Mapping

## Summary
A user reported exceeding the soft quota for the number of files on `/home/vault`. The user had not accessed their files recently and inquired about the validity of the notification.

## Root Cause
- The user's account was over quota, but the user had not received email notifications until recently.
- The email notification system had issues with mapping usernames to email addresses.

## Solution
- The user confirmed their account name and cleaned up their files, resolving the quota issue.
- The HPC Admin explained that the email notification system was recently updated, which might have resolved the previous mapping issues.

## Lessons Learned
- Regularly check and clean up files to avoid exceeding quotas.
- Ensure that the email notification system correctly maps usernames to email addresses.
- Be aware that system updates can affect email notifications.

## Actions Taken
- The user cleaned up their files to comply with the quota.
- The HPC Admin provided information about the email notification system and its recent updates.

## Follow-Up
- Monitor the email notification system to ensure proper delivery of quota alerts.
- Regularly review and update the username-email mapping to prevent future issues.
---

### 2016042042000203_Lima%20error%3A%20Aborted%20by%20PBS%20Server.md
# Ticket 2016042042000203

 # HPC Support Ticket: Lima Error - Aborted by PBS Server

## Keywords
- PBS Server
- Job submission error
- Disk quota exceeded
- Temporary directory
- File quota

## Problem Description
The user attempted to submit a job on Lima but received an error message via email indicating that the job was aborted by the PBS Server and could not be executed. The job did not appear in the queue and did not generate any error or output files.

## Root Cause
The error was caused by exceeding the disk quota for the number of files in the temporary directory (`/lxfs` or `$FASTTMP`). The system has a quota for the number of files to prevent performance degradation due to too many small files.

## Solution
The user had exceeded the file quota, which prevented the creation of a temporary directory for the job. The HPC Admin confirmed that the user had cleaned up their files, bringing them back under the quota, which resolved the issue.

## General Lessons Learned
- Exceeding file quotas in temporary directories can cause job submission failures.
- Regularly monitor and manage file usage to stay within allocated quotas.
- Clean up unnecessary files to prevent issues with job submission and system performance.

## Troubleshooting Steps
1. Check the error message for indications of quota-related issues.
2. Verify the user's file usage in temporary directories.
3. Advise the user to clean up files to stay within the allocated quota.
4. Confirm that the user is back under the quota and can submit jobs successfully.

## References
- HPC Services, Friedrich-Alexander-Universitaet Erlangen-Nuernberg
- Regionales RechenZentrum Erlangen (RRZE)
- [HPC Services Website](http://www.hpc.rrze.fau.de/)
---

### 2024121642002206_High%20File%20Count%20for%20Project%20b143dc.md
# Ticket 2024121642002206

 # HPC Support Ticket: High File Count for Project b143dc

## Keywords
- High file count
- Metadata operations
- Small files
- HPC file systems
- Storage optimization

## Problem
- **Root Cause:** Excessive number of small files stored in the project directory on `$WORK`.
- **Impact:** High load and excessive metadata operations on the file systems.

## Details
- **Project:** b143dc
- **File Count:** 21.5 million files
- **Storage Location:** `$WORK`

## Communication
- HPC Admin reached out to the project owner regarding the high file count.
- Suggested using data formats more suited for HPC file systems.
- Offered assistance and recommended attending the monthly introduction for AI users.

## Solution
- **Recommended Actions:**
  - Use data formats optimized for HPC file systems.
  - Attend the monthly introduction for AI users for an overview of possible approaches.
  - Contact HPC support for assistance in optimizing file storage.

## Resources
- [HPC Café Introduction for AI Users](https://hpc.fau.de/teaching/hpc-cafe/#nutshell)

## Follow-up
- Encourage the project owner to reach out for further assistance if needed.
- Monitor the project's storage usage for improvements.

---

**Note:** This documentation is intended for HPC support employees to reference when addressing similar issues related to high file counts and storage optimization.
---

### 2023083142001261_quota%20exceed%20-%20p101ae10.md
# Ticket 2023083142001261

 # HPC Support Ticket: Quota Exceeded Error

## Keywords
- Disk quota exceeded
- Input/output error
- `mv` command
- `$HPCVAULT`
- `shownicerquota.pl`
- `quota -s`

## Problem Description
The user encountered an error while trying to move a file from their working directory to the vault directory. The error messages indicated an input/output error and that the disk quota was exceeded.

## Root Cause
The user's quota on `$HPCVAULT` was exceeded, preventing them from moving additional files to that directory.

## Solution
1. **Check Quota**: The user was advised to check their quota using the commands `shownicerquota.pl` or `quota -s`.
2. **Cleanup Data**: The user was instructed to clean up data they no longer needed on `$HPCVAULT`.
3. **Quota Increase**: An HPC Admin increased the user's quota on `/home/vault/` by 5x to provide additional space.

## Additional Notes
- The user's project was noted to be running out of compute resources, and they were advised to consider submitting a follow-up project.
- The user was informed about the next cut-off deadline for large-scale projects.

## Example Commands
```bash
shownicerquota.pl
quota -s
```

## Related Topics
- Quota management
- Data backup and storage
- Project resource allocation
---

### 2023041342000981_Re%3A%20Over%20quota%20on%20_home_saturn%20for%20group%20gwgi..md
# Ticket 2023041342000981

 # HPC Support Ticket: Over Quota on /home/saturn for Group gwgi

## Keywords
- Quota exceeded
- Large files
- Process management
- Group storage
- Grace period

## Summary
A user's processes generated large files, causing the group `gwgi` to exceed its storage quota on `/home/saturn`. This issue affected other users' processes and required immediate attention.

## Root Cause
- Faulty processes created large files.
- Group `gwgi` reached its hard quota of 166.7 TB.

## Impact
- Other users' processes were terminated.
- Group storage quota was exceeded, affecting overall performance.

## Solution
- The user deleted the large files to bring the quota back within limits.

## Lessons Learned
- Regularly monitor processes to prevent excessive file generation.
- Promptly address quota warnings to avoid reaching the hard quota.
- Communicate with other users to minimize the impact of storage issues.

## Actions Taken
- The user deleted the large files.
- HPC Admins sent a warning email about the quota exceedance.

## Follow-up
- Ensure users are aware of their storage quotas and the importance of managing their files.
- Implement monitoring tools to detect and alert users about large file generation.

## References
- Quota management documentation
- Process monitoring best practices
---

### 2022031742000745_Re%3A%20Over%20quota%20on%20_home_saturn%20for%20group%20capn..md
# Ticket 2022031742000745

 # HPC Support Ticket: Over Quota on /home/saturn for Group 'capn'

## Keywords
- Quota Exceeded
- Grace Period
- Cleanup
- Archiving
- Directory Deletion

## Problem Description
The group 'capn' exceeded their allocated quota on `/home/saturn`. They were using 15.3 TB out of 15.0 TB allocated, with a grace period of 48.4 hours before reaching the hard quota of 20.0 TB.

## Quota Usage Breakdown
- **capn**: 15.3 TB (101.7%)
- **mppi033h**: 8.7 TB (57.8%)
- Other users had minimal usage.

## Actions Taken
1. **User Notification**: The master user was notified about the quota exceedance and the need to clean up.
2. **Archiving Data**: The user archived data of a former user who had not been active for 1.5 years.
3. **Request for Directory Deletion**: The user requested the HPC Admins to delete the directory `/home/saturn/capn/mppi033h` after archiving.

## Solution
- The user archived the relevant data and requested the HPC Admins to delete the directory.
- The HPC Admins confirmed the deletion process and mentioned that the backup tar file could be deleted in approximately 4 weeks.

## Lessons Learned
- Regularly monitor quota usage to avoid exceeding limits.
- Archive and delete data from inactive users to free up space.
- Communicate with HPC Admins for assistance in deleting large directories.

## Follow-Up
- Ensure that the backup tar file is deleted after the specified period to free up additional space.
- Continue monitoring quota usage to prevent future overages.
---

### 2022081942001482_question.md
# Ticket 2022081942001482

 # HPC Support Ticket Analysis

## Subject: Storage Quota Inquiry and Purchase Request

### Keywords:
- Storage Quota
- Vault Storage
- Purchase Request
- Discount Offer

### Summary:
A user from the WW1 simulation group inquired about their current storage usage and requested a quote for additional storage.

### User Request:
- Current storage usage from 150TB quota.
- Quote for additional storage.

### HPC Admin Response:
- Current usage: 43.41TB out of 150TB.
- Link to storage offer: [Vault Quota Information](https://hpc.fau.de/antrag-auf-bigdata-share/)
- Discount available for advance payment or large quota.

### Outcome:
- User acknowledged the response.
- Ticket closed.

### Lessons Learned:
- Users can request their current storage usage.
- HPC offers discounts for advance payments or large storage quotas.
- Relevant information for storage offers is available on the HPC website.

### Root Cause:
- User needed to know their current storage usage and wanted to purchase additional storage.

### Solution:
- HPC Admin provided the current usage and directed the user to the relevant webpage for storage offers and discount information.

### Documentation for Future Reference:
- Always provide users with their current storage usage when requested.
- Direct users to the appropriate webpage for storage offers and discount information.
- Ensure users are aware of discount options for advance payments or large quotas.
---

### 2023081842001071_Quota%20Problem%20%21.md
# Ticket 2023081842001071

 # HPC Support Ticket: Quota Problem

## Keywords
- Quota limits
- Disk space
- Master thesis
- Automatic email notification
- Quota management

## Problem Description
- User received an automatic email notification about reaching quota limits on the `/home/woody` filesystem.
- User's disk space usage exceeded the soft quota, preventing the creation of new files.
- User requested a quota increase to continue working on their master thesis, which is due in one month.

## Root Cause
- Excessive disk space usage in the `/home/woody` directory, specifically in the `/home/woody/restore/iwi5124h/` subdirectory.

## Solution
- HPC Admins deleted the `/home/woody/restore/iwi5124h/` directory as communicated, bringing the user's disk space usage below the quota limit.

## Lessons Learned
- Regularly monitor and manage disk space usage to avoid reaching quota limits.
- Communicate with HPC Admins to address quota issues promptly.
- Consider requesting temporary quota increases when approaching deadlines, but be prepared to justify the need and provide a plan for reducing disk space usage afterward.
- Automatic email notifications can help users stay informed about their quota usage and take corrective action when necessary.
---

### 2022030242002397_StarCCM%2B%20Disk%20Quota%20Exceeded%20Emmy.md
# Ticket 2022030242002397

 # HPC Support Ticket: Disk Quota Exceeded on Emmy

## Keywords
- Disk Quota
- FASTTMP
- File Limit
- StarCCM+
- Emmy

## Problem Description
- User encountered job failures due to exceeding disk quota on Emmy.
- User deleted unnecessary files but still faced quota issues.

## Root Cause
- The user exceeded the limit of 500k files/directories in the `$FASTTMP` directory.
- Current number of files/directories in `$FASTTMP` was 711k.

## Solution
- HPC Admin informed the user about the file/directory limit.
- User needs to reduce the number of files/directories in `$FASTTMP` to below 500k.

## Lessons Learned
- Disk quota on HPC systems may include limits on the number of files and directories, not just the total storage space.
- Regularly monitor and manage the number of files and directories to avoid exceeding such limits.
- Communicate with HPC Admins for clarification on quota policies and limits.

## Action Items
- Users should check their file/directory usage in `$FASTTMP`.
- Delete or archive unnecessary files to stay within the quota limits.
- HPC Admins should provide clear documentation on quota policies, including file/directory limits.
---

### 2024102942003211_Quota%20gwgifu0h.md
# Ticket 2024102942003211

 # HPC Support Ticket: Quota gwgifu0h

## Keywords
- Quota
- Storage
- Vault
- Group Quota
- User Quota

## Summary
- **User Inquiry:** Requested information about the storage quota for their group on Vault, specifically associated with the user `gwgifu0h`.
- **HPC Admin Response:** Provided the current storage usage and quota limits for the group and the specific user.

## Root Cause
- User needed to know the current storage usage and quota limits for their group and a specific user on Vault.

## Solution
- **HPC Admin:**
  - Informed the user about the group quota on Vault: 346T out of 500T.
  - Specified the storage usage for the user `gwgifu0h`: 293T.
  - Advised the user to use the official support email address for future inquiries.

## General Learnings
- Users should use the official support email address for inquiries.
- Group and user quotas on Vault can be checked and reported by HPC Admins.
- Storage usage and quota limits are important metrics for users to monitor their resource allocation.

## Additional Notes
- Ensure users are aware of the correct channels for support requests.
- Regularly update users on their storage usage to prevent overages.
---

### 2021091142000292_Exceeding%20your%20File%20Quota%20of%20500%2C000%20warning.md
# Ticket 2021091142000292

 # HPC Support Ticket: Exceeding File Quota

## Keywords
- File quota
- Permission denied
- GPFS
- Login issue
- File management

## Problem Description
- User exceeded the file quota of 500,000 in `/home/hpc` during a model training session.
- Unable to log in to the system due to the file quota limit.
- Received "permission denied" message when attempting to delete unnecessary files.

## Root Cause
- Excessive number of files generated in a flat directory structure without subdirectories.
- Two directories each containing 251,000 files of 208 bytes.

## Solution
- User was able to log in again on `cshpc` and `woody3`, indicating the initial login issue was resolved.
- No specific solution provided for the file management issue, but it is noted that the user's file system misuse remains unresolved.

## Lessons Learned
- Exceeding file quotas can lead to login issues and permission errors.
- Flat directory structures with a large number of files can cause performance issues, even on GPFS servers.
- Proper file management and use of subdirectories are essential to avoid such problems.

## Next Steps
- Educate users on proper file management practices.
- Monitor and enforce file quota policies to prevent similar issues in the future.
- Consider providing tools or scripts to help users manage large numbers of files efficiently.
---

### 42307267_Fwd%3A%20Vault%20weg%3F.md
# Ticket 42307267

 ```markdown
# HPC Support Ticket: Vault Quota Issue

## Keywords
- Vault Quota
- `$VAULT` Variable
- `shownicerquota.pl`
- Automounter
- `$HPCVAULT`

## Problem Description
The user reported that they could not find their Vault quota after not logging in for a while. The `$VAULT` variable was not defined, and the user was unsure how to link back to their Vault directory.

## Root Cause
- The `$VAULT` variable was never defined.
- The user was unaware of the new `$HPCVAULT` variable that points to the Vault directory.
- The Vault directory might not appear in the quota output if it hasn't been accessed yet due to the Automounter.

## Solution
- Inform the user about the new `$HPCVAULT` variable that points to `/home/vault/iwpa/iwpa47`.
- Advise the user to use the `shownicerquota.pl` command on the cluster frontends to check their quota without needing to know the specific filesystem details.
- Explain that the Vault directory might not appear in the quota output until it has been accessed, and accessing it with a command like `ls $HPCVAULT` will make it appear.

## General Learnings
- Always check if the relevant environment variables are defined.
- Use cluster-specific commands like `shownicerquota.pl` for easier quota management.
- Understand the behavior of the Automounter and how it affects directory visibility.
```
---

### 2024022742003811_Disk%20Quota%20Vault%20Exceeded%20-%20b209cb10.md
# Ticket 2024022742003811

 # HPC Support Ticket: Disk Quota Vault Exceeded

## Keywords
- Disk Quota
- Vault Directory
- Duplication on Storage Array
- Shared Directory
- Permissions
- Quota Accounting

## Summary
A user encountered a disk quota exceeded error on their HPC directory. The discrepancy between the reported quota usage and the actual directory size was due to duplication on the storage array. The user also had files stored in another user's directory with world-writeable permissions, leading to quota issues.

## Root Cause
- **Duplication on Storage Array**: The storage system reports quota usage as twice the actual size due to duplication.
- **Misplaced Files**: The user stored files in another user's directory with world-writeable permissions, causing quota issues.

## Solution
- **Explanation of Quota Accounting**: The HPC Admin explained the quota accounting system and the duplication factor.
- **Creation of Shared Directory**: A shared directory was created for the project, allowing all relevant users to read and write, with data counting towards the project's quota.
- **Removal of Misplaced Directory**: The HPC Admin removed a misplaced directory owned by another user upon request.

## General Learnings
- **Quota Accounting**: Understand the quota accounting system and the duplication factor on the storage array.
- **Permissions**: Avoid setting world-writeable permissions on directories to prevent unauthorized access and quota issues.
- **Shared Directories**: Use shared directories for collaborative projects to efficiently manage quota and permissions.
- **Project Quota**: For NHR projects, the quota is accounted per project, not per user, allowing better management of storage space.

## Actions Taken
- **Explanation**: Provided detailed explanation of the quota accounting system and the duplication factor.
- **Shared Directory**: Created a shared directory for the project with appropriate permissions.
- **Directory Removal**: Removed a misplaced directory upon request to resolve quota issues.

## Follow-up
- **Permissions Change**: The user will change the permission settings of their directory to prevent future quota issues.
- **File Transfer**: The user will transfer files to the newly created shared directory and ensure proper permissions are set.
---

### 2024030642002877_user%20iwal139h%2C%20Disk%20quota%20on%20_home_janus%20exceeded%3F.md
# Ticket 2024030642002877

 # HPC Support Ticket: Disk Quota Exceeded on /home/janus

## Keywords
- Disk quota exceeded
- NFS file limit
- Extracted archives
- Node-local SSD

## Summary
A user reported an issue with copying files in `/home/janus/iwal-datasets/DNN_SpCo` due to a "Disk quota exceeded" error. The problem was traced to the number of files/directories exceeding the limit for the NFS filesystem.

## Root Cause
- The directory `/home/janus/iwal-datasets/` has a limit of 100k files/directories.
- The user had extracted archives in the `DNN_SpCo/LibriTTS_24k_other` tree, causing the file count to exceed the limit.

## Solution
- Remove the problematic files to reduce the file count below the limit.
- Store only the archive on NFS and extract it to the node-local SSD at the beginning of jobs.

## Lessons Learned
- Always check the file count limit for NFS filesystems.
- Avoid storing extracted archives on NFS; use node-local SSD for temporary extraction.
- Regularly monitor and manage file counts to prevent quota issues.

## Documentation Reference
- [FAU Data Filesystems Documentation](https://doc.nhr.fau.de/data/filesystems/?h=quota#quotas)

## Support Team Involved
- HPC Admins
- 2nd Level Support Team
---

### 2023061242000891_Quota%20increase%20on%20Home%20Vault.md
# Ticket 2023061242000891

 ```markdown
# HPC-Support Ticket: Quota Increase on Home Vault

## Keywords
- Home Vault
- File Quota
- Hard Quota
- Backup
- rsync
- Tar Files
- Job Archive
- Data Compression
- Account Management

## Summary
- **User Request**: Increase file quota on Home Vault.
- **Current Quota**: 200,000 files.
- **Requested Quota**: 10 million files.
- **Reason**: User is running into hard quota limits due to large tar files and rsync backups.

## Root Cause
- User's file quota on Home Vault is insufficient for their backup needs, leading to hard quota limits being reached.

## Solution
- **Admin Response**: The request was discussed in an admin meeting.
- **Action Plan**: HPC Admins will review backup software and consider making daily tarballs.

## General Learnings
- Users may require higher file quotas for backup purposes, especially when dealing with large archives and compressed files.
- Regular review and adjustment of quotas may be necessary to accommodate user needs.
- Consider implementing automated backup solutions to manage large data sets efficiently.
```
---

### 2024070342002348_Concerning%20Exceeded%20Soft%20Quota.md
# Ticket 2024070342002348

 # HPC Support Ticket: Exceeded Soft Quota

## Keywords
- Soft quota limit
- Home directory
- Temporary files
- Quota threshold
- Cache directory

## Problem Description
- User received an email indicating they exceeded the soft quota limit on `/home/hpc/`.
- User's own checks showed that the quota was not exceeded.

## Root Cause
- Possible temporary files being written to `~/.cache` by one of the user's jobs.

## Solution
- If the quota is now below the threshold, the user can ignore the email.
- Check for temporary files in `~/.cache` and clean them up if necessary.

## General Learnings
- Temporary files can cause unexpected quota usage.
- Regularly check and clean up temporary files to avoid exceeding quota limits.
- If the quota is below the threshold after cleaning up, no further action is needed.
---

### 42123650_Anfrage.md
# Ticket 42123650

 ```markdown
# HPC Support Ticket: Data Storage and Archiving

## Keywords
- Data storage
- Archiving
- Backup
- HPC storage
- Long-term storage

## Problem
- User needs to secure a large amount of data (3 TB and more).
- User is unable to create a new folder in the archive.
- User seeks advice on where to store data as they cannot keep buying new hard drives.

## Root Cause
- User lacks permissions or knowledge to create a new folder in the archive.
- User needs guidance on available storage solutions.

## Solution
- **Archive Service**: User should contact `backup@rrze.uni-erlangen.de` to set up a directory for the archive service.
  - Reference: [Preisliste](http://www.rrze.uni-erlangen.de/dienste/konditionen/preise/index.shtml#dienste)
- **Long-term Storage**: For long-term storage in the HPC environment, `/home/vault` is recommended.
  - Documentation: [HPC Storage](http://www.rrze.uni-erlangen.de/dienste/arbeiten-rechnen/hpc/systeme/hpc-storage.shtml)

## General Learnings
- Users should be directed to the appropriate services for data archiving and long-term storage.
- HPC Admins should provide clear instructions and documentation links for users to follow.
- Collaboration with department heads (e.g., LSTM) may be necessary for storage capacity procurement.
```
---

### 2024091442000227_Daten%20l%C3%83%C2%B6schen.md
# Ticket 2024091442000227

 ```markdown
# HPC-Support Ticket: Daten löschen

## Keywords
- Account expiration
- Quota exceeded
- Data deletion
- HPC account management

## Problem
- User's HPC account (`iwb0003h`) has expired.
- User continues to receive "Quota überschritten" (quota exceeded) emails.
- User has no important data left on the account and requests data deletion.

## Root Cause
- Expired account still has data that exceeds the quota limit.

## Solution
- HPC Admin deleted the data from the expired account to resolve the quota issue.

## General Learnings
- Users may continue to receive quota exceeded notifications even after their account has expired.
- HPC Admins can delete data from expired accounts to resolve quota issues.
- Users should ensure all important data is backed up before requesting data deletion.
```
---

### 2024062842000797_Anfrage%3A%20500GB%20group-shared%20directory.md
# Ticket 2024062842000797

 ```markdown
# HPC Support Ticket: Request for 500GB Group-Shared Directory

## Keywords
- Group-shared directory
- Data sharing
- Access permissions
- NFS
- POSIX
- HPCVAULT
- $WORK

## Problem
- User requires a 500GB group-shared directory for their master's thesis.
- Multiple users need access to the directory.

## Solution
- Existing directories for the user's department:
  - `/home/janus/iwso-datasets`
  - `/home/vault/empkins`
- Alternative options:
  - Share individual directories from `$HPCVAULT` or `$WORK`.
- Documentation for setting permissions:
  - [NFS Permissions](https://doc.nhr.fau.de/data/share-perm-nfs/)
  - [POSIX Permissions](https://doc.nhr.fau.de/data/share-perm-posix/)

## General Learnings
- Check for existing shared directories before creating new ones.
- Utilize `$HPCVAULT` or `$WORK` for sharing data if necessary.
- Refer to documentation for setting appropriate permissions.
```
---

### 2022051342001328_create%20sshfs%20folder%20in%20woody%20home%20directory.md
# Ticket 2022051342001328

 # HPC Support Ticket: SSHFS and Storage Quota

## Keywords
- SSHFS
- Storage Quota
- Home Directory
- $HPCVAULT
- $WORK
- Disk Quota Exceeded

## Problem
- User's home directory exceeded 50 GB.
- User attempted to move files to a remote storage server using SSHFS, but the command was not available.
- User tried to copy files to $HPCVAULT but encountered a "Disk quota exceeded" error.

## Root Cause
- User misunderstood the storage quota limits.
- $HPCVAULT quota for the user's group was full (5000 GB shared quota).

## Solution
- HPC Admin suggested reading the storage documentation to understand quota limits.
- User was advised to use $WORK for additional storage, which has a default quota.
- User should coordinate with colleagues to clean up $HPCVAULT storage.

## General Learnings
- Understanding storage quotas and available storage options is crucial.
- SSHFS may not be available on all systems, and alternative file transfer methods should be considered.
- Coordination with colleagues is essential when using shared storage quotas.
- HPC Admins can provide guidance on storage options and quotas.
---

### 2023053042002838_Keine%20Verbindung%20mit%20tinyx%20nicht%20m%C3%83%C2%B6glich.md
# Ticket 2023053042002838

 # HPC Support Ticket: Connection Issue with tinyx

## Keywords
- HPC Server Connection
- Quota Exceeded
- VSCode Code Server
- $HOME Directory
- $WORK Directory

## Problem Description
The user is unable to connect to the HPC server. The issue might be related to exceeded storage quota.

## Root Cause
- The user's $HOME directory has exceeded its quota, preventing VSCode from installing the Code Server.

## Solution
1. **Check Quota Usage**:
   - Use the command `du -h -d 1 $HOME | sort -h` to identify which directories are consuming the most space.
   - Increase the depth by changing `-d 1` to `-d 2`, etc., for more detailed information.

2. **Free Up Space**:
   - Delete or move unnecessary files to free up space in the $HOME directory.

3. **Change Code Server Installation Path**:
   - Modify the VSCode settings to install the Code Server in the $WORK directory.
   - Example configuration:
     ```json
     "remote.SSH.serverInstallPath": {
       "tinyx.nhr.fau.de": "/home/woody/iwfa/iwfa017h"
     }
     ```
   - Refer to [this GitHub issue](https://github.com/microsoft/vscode-remote-release/issues/472#issuecomment-975745519) for more details.

## General Learning
- Exceeding the quota in the $HOME directory can cause various issues, including preventing the installation of necessary tools like the VSCode Code Server.
- Regularly monitor and manage storage usage to avoid quota-related problems.
- VSCode settings can be configured to use alternative directories for installations, such as the $WORK directory.

## Additional Resources
- [VSCode Remote Development Documentation](https://github.com/microsoft/vscode-remote-release)
- [FAU HPC Support](https://hpc.fau.de/)
---

### 2020050442000457_Request%20for%20increase%20of%20quota%20on%20home_woody.md
# Ticket 2020050442000457

 # HPC Support Ticket: Request for Increase of Quota on Home Filesystem

## Keywords
- Quota Increase
- Home Filesystem
- User Group Data Storage
- Regular Quota
- Group Quota
- $WORK Filesystem

## Summary
A user requested an increase in their quota on the home filesystem due to storing a large amount of data used by a specific user group.

## Root Cause
- User's current quota (1500 GB) is already significantly higher than the regular quota.
- User is storing data for a user group on the home filesystem instead of the designated $WORK filesystem.

## Solution
- HPC Admin advised the user to utilize the $WORK filesystem, where the user group has a substantial quota (22.5 TB).
- No quota increase was granted on the home filesystem.

## General Learnings
- Users should be directed to use appropriate filesystems for different types of data storage.
- Regular quotas should be respected, and exceptions should be carefully considered.
- Group data should be stored in designated group storage areas to optimize resource allocation.

## Actions Taken
- HPC Admin responded to the user's request, explaining the current quota policy and suggesting the use of the $WORK filesystem.
- No changes were made to the user's quota on the home filesystem.
---

### 2024020642000488_Over%20Quota%20on%20hpc.md
# Ticket 2024020642000488

 # HPC Support Ticket: Over Quota on HPC

## Keywords
- Quota Exceeded
- Block Quota
- Filesystem Management
- Data Deletion
- User Consent

## Problem
- User received an email reminder about exceeding block quota for the filesystem.
- Requested deletion of files in a folder belonging to a graduated student to free up storage.

## Root Cause
- User's quota was exceeded due to large data storage.
- Misunderstanding about quota calculation and data management policies.

## Solution
- **Quota Calculation**: Quota is counted on a per-user basis.
- **Data Management**:
  - **$HOME**: Store very important data that cannot be easily reproduced.
  - **$HPCVAULT**: Store data that needs to be kept.
  - **$WORK**: Store data and software that can be reproduced with low effort.
- **Data Deletion Policy**: Data from inactive accounts will be deleted after a 3-month period. Deletion before this period requires user consent.

## Recommendations
- Move data to appropriate filesystems based on importance and reproducibility.
- Review and manage data regularly to avoid exceeding quota limits.
- Refer to the [HPC Storage Documentation](https://hpc.fau.de/systems-services/documentation-instructions/hpc-storage/) for more details.

## Follow-Up
- User should review and manage their data storage to stay within quota limits.
- HPC Admins should monitor and provide guidance on data management practices.

## Additional Resources
- [HPC Storage Documentation](https://hpc.fau.de/systems-services/documentation-instructions/hpc-storage/)
---

### 42151977_Datensicherung%20vom%20HPC%20Filesystem.md
# Ticket 42151977

 ```markdown
# HPC Support Ticket: Datensicherung vom HPC Filesystem

## Keywords
- Datensicherung
- WinSCP
- Externe Festplatte
- Woody
- Vault
- Home
- Wochenende
- Testfront
- Cshpc

## Root Cause
- User wants to back up approximately 950 GB of data from woody, vault, and home directories to an external hard drive over the weekend using WinSCP.

## Solution
- The user is advised to proceed with the backup using WinSCP.
- It is recommended to use `testfront` or `cshpc` instead of woody/lima-frontend to avoid the server-side process being terminated due to long runtime.

## General Learnings
- Using WinSCP for large data backups is acceptable.
- Prefer using `testfront` or `cshpc` for long-running processes to avoid interruptions.
```
---

### 2023081742000065_Support%20with%20quote%20exceeded%20issue%20on%20HPC.md
# Ticket 2023081742000065

 # HPC Support Ticket: Quota Exceeded Issue

## Keywords
- File quota exceeded
- Inode count
- Conda environment
- Grace period expired
- VSCode connection issue

## Problem Description
- User exceeded the file quota limit of 500,000 files.
- Grace period expired, preventing the creation of new files.
- Unable to connect via VSCode due to the inability to create new files.
- User has deleted some folders but is still above the limit.

## Root Cause
- Large number of files in the `miniconda3` directory.

## Solution
1. **Check File Count**:
   - Use the command `du -s --inodes <directory_name>` to check the inode count in a specific directory.

2. **Move Conda Environment**:
   - Move the `miniconda3` installation to the `$WORK` filesystem.
   - Change the installation path and/or rebuild the environment there.

3. **Documentation Reference**:
   - Refer to the HPC storage documentation for an overview of available filesystems and their usage: [HPC Storage Documentation](https://hpc.fau.de/systems-services/documentation-instructions/hpc-storage/)

## Additional Notes
- The user's current quota report shows 618,171 files used, exceeding the soft quota of 500,000 files.
- The user has only one Conda environment, which was working fine previously.

## Follow-up Actions
- Ensure the user moves the Conda environment to the appropriate filesystem.
- Verify that the file count is below the quota limit after the changes.

## Related Documentation
- [HPC Storage Documentation](https://hpc.fau.de/systems-services/documentation-instructions/hpc-storage/)
---

### 2018061442000913_Erweiterung%20Speicher%20HPC-Cluster%20Nutzername%20iwst030h.md
# Ticket 2018061442000913

 ```markdown
# HPC-Support Ticket: Erweiterung Speicher HPC-Cluster

## Subject
Erweiterung Speicher HPC-Cluster Nutzername iwst030h

## Keywords
- Speichererweiterung
- Quota
- Filesystem
- /home/woody
- /home/hpc

## Problem
- User erhielt eine E-Mail, dass der maximale Speicher von 10 GB auf dem HPC-Cluster überschritten ist.
- User fragt nach einer Erweiterung des Speichers auf 500 GB.

## Root Cause
- Überschreitung der Quota auf dem Filesystem /home/woody.

## Solution
- HPC Admin informiert, dass eine Quota-Erhöhung auf /home/hpc nicht möglich ist.
- User wird auf die Dokumentation der verfügbaren Filesysteme verwiesen.
- HPC Admin bestätigt, dass die Quota auf /home/woody bereits erhöht wurde.

## What to Learn
- Unterschiedliche Filesysteme haben unterschiedliche Quotas und Nutzungsrichtlinien.
- Bei Speicherproblemen sollte die Dokumentation der verfügbaren Filesysteme konsultiert werden.
- HPC Admins können Quotas auf bestimmten Filesystemen erhöhen, aber nicht auf allen.

## Actions Taken
- HPC Admin hat die Quota auf /home/woody erhöht.
- User wurde auf die Dokumentation der verfügbaren Filesysteme verwiesen.

## Documentation Link
- [Verfügbare Filesysteme](https://www.anleitungen.rrze.fau.de/hpc/environment/#fs)
```
---

### 2024080942001372_%5Baction%20requiered%5D%20very%20high%20file%20count%20on%20atuin%20%5Ba102cb10%5D.md
# Ticket 2024080942001372

 # HPC Support Ticket: High File Count on User Account

## Keywords
- High file count
- System slowdown
- User account cleanup

## Problem Description
- **Root Cause:** User account has an excessive number of files (14 million) in the home directory.
- **Impact:** High file count contributes to slowing down the system.

## Solution
- **Action Required:** User was requested to reduce the number of files in their account.
- **Resolution:** The ticket was closed as the user was in the process of cleaning up their files.

## General Learnings
- High file counts in user accounts can lead to system performance issues.
- Regularly monitor and manage file counts to maintain system efficiency.
- Communicate with users to ensure they are aware of the impact of high file counts and the need for cleanup.

## Roles Involved
- **HPC Admins:** Notified the user about the issue and monitored the cleanup process.
- **User:** Responsible for reducing the file count in their account.

## Additional Notes
- Ensure users are educated on best practices for file management to prevent similar issues in the future.
- Regularly review user accounts for high file counts to proactively address potential performance issues.
---

### 2024111242003331_Platzverbrauch%20_home_vault_empkins.md
# Ticket 2024111242003331

 ```markdown
# HPC-Support Ticket: Platzverbrauch /home/vault/empkins

## Keywords
- Platzverbrauch
- HPC-Cluster
- du -sh
- Unterverzeichnisse
- SFB-Antragsphase

## Problem
- User requires the current disk usage of the directory `/home/vault/empkins` for an upcoming SFB-Antragsphase.
- User lacks access to all subdirectories to perform the `du -sh` command themselves.

## Solution
- HPC Admin provided the current disk usage: 135TB in the directory `/home/vault/empkins`.

## Lessons Learned
- Users may need assistance with accessing disk usage information for directories they do not have full permissions to.
- The `du -sh` command is a common method for checking disk usage.
- HPC Admins can provide necessary information when users lack the required permissions.
```
---

### 42212851_auf%20bash%20am%20woody%20umstellen.md
# Ticket 42212851

 ```markdown
# HPC Support Ticket Conversation Analysis

## Keywords
- Shell change
- Bash
- Woody
- Quota increase
- Home directory

## General Learnings
- **Shell Change Request**: Users may request to change their default shell to `bash`.
- **Global Shell Change**: Changing the shell on individual systems is not possible; it must be done globally across all systems.
- **Delay in Shell Change**: The change may take up to a day to become effective across all systems.
- **Quota Increase Request**: Users may request an increase in their home directory quota.
- **Ticket Management**: Ensure that new requests are handled in separate tickets to avoid reopening old tickets.

## Root Cause of the Problem
- User requested a shell change to `bash` on the Woody system.
- User later requested an increase in their home directory quota.

## Solution
- **Shell Change**: The shell was changed globally to `bash` for the user.
- **Quota Increase**: A new ticket was created to handle the quota increase request.

## Notes for Support Employees
- Ensure shell changes are applied globally.
- Inform users about potential delays in the shell change taking effect.
- Handle new requests in separate tickets to maintain clarity and organization.
```
---

### 2024121642002555_Request%20for%20HPC%20Access%20for%20Shadi%20Khamseh.md
# Ticket 2024121642002555

 ```markdown
# HPC Support Ticket Conversation Analysis

## Keywords
- HPC Access Request
- Master's Project
- Simulations
- Parallel Implementations
- Disk Quota Increase
- CIP Pool
- Project Manager Invitation

## Summary
A student requires HPC access to expedite simulations for a Master's project. The student's supervisor requests access by the end of January 2025. The student also needs an increase in disk quota for the CIP Pool to run training jobs effectively.

## Root Cause of the Problem
- **Insufficient Disk Quota**: The student's current disk quota of 8 GB is insufficient for training requirements.
- **Time-Consuming Simulations**: Running each implementation on a personal PC is extremely time-consuming.

## Solution
- **HPC Access Request**: The supervisor needs to contact the project manager of "Tier3 Grundversorgung LS Inf3 (Rechnerarchitektur)" to invite the student to the project via the HPC Portal.
- **Disk Quota Increase**: The supervisor should provide a rough estimate of the disk space needed and an approximate end date of the project to the CIP Pool support.

## General Learnings
- **HPC Access Procedure**: Students need to be invited to projects by the project manager via the HPC Portal.
- **Disk Quota Requests**: Requests for increased disk quota should include a rough estimate of the required space and the project's end date.
- **Communication**: Effective communication between the student, supervisor, and HPC support is crucial for resolving resource allocation issues.
```
---

### 2018022842000225_Need%20information%20regarding%20extra%20nodes%20and%20quota.md
# Ticket 2018022842000225

 # HPC Support Ticket: Need Information Regarding Extra Nodes and Quota

## Keywords
- Master thesis
- Geophysical simulation
- Emmy cluster
- Data quota
- Storage
- Nodes
- Parallel file system
- Work queue

## Problem
- User requires additional nodes and storage quota for a geophysical simulation.
- Expected storage of output files is around 10 TB.
- User needs to run the simulation for a period of 3 days.

## Solution
- **Storage**: Use the parallel file system ($FASTTMP or /elxfs) on Emmy. No quota for disk space, but oldest files will be deleted if the system becomes too full.
- **Nodes**: User can utilize the "work" queue with up to 64 nodes, which should be sufficient for their purposes.

## General Learnings
- The parallel file system is suitable for temporary storage needs.
- Users can request additional nodes beyond the typical job size stated in their proposal.
- The "work" queue allows for the use of up to 64 nodes.

## Actions Taken
- HPC Admin suggested using the parallel file system for storage.
- Clarification provided on the availability of additional nodes through the "work" queue.

## Root Cause
- User needed additional storage and computational resources for a large-scale simulation.

## Resolution
- User was informed about the parallel file system for storage and the availability of additional nodes through the "work" queue.

## Notes
- Ensure users are aware of the temporary nature of the parallel file system.
- Provide clear guidelines on how to request and utilize additional computational resources.
---

### 2024032342000604_Data%20Staging%20on%20Vault.md
# Ticket 2024032342000604

 ```markdown
# HPC-Support Ticket Conversation: Data Staging on Vault

## Keywords
- Data Staging
- Quota Expansion
- $VAULT
- $WORK
- Sparse Files
- NFS 4.1 Filesystem
- Mirrored Data

## Summary
A user encountered issues with data staging on the HPC cluster due to quota limitations and filesystem constraints. The user initially stored data on $VAULT but faced issues with sparse files, leading to increased data size. The user requested additional quota on $VAULT or $WORK partitions.

## Problem Clarification
- **Dataset Size**: 600 GB
- **Initial Storage**: SSD connected to a computer at the Graphics lab
- **Transfer Speed**: ~120 MBps using parallelized rsync to node-local SSDs
- **$VAULT Issue**: Data size doubled due to lack of sparse file support in NFS 4.1 filesystem

## Questions
1. Workaround for utilizing sparse files on $VAULT?
2. Possibility of expanding quota on $VAULT?

## Solutions and Clarifications
- **$WORK Quota**: Initially thought to be 500 GB, but actually 1 TB. Data on $WORK is mirrored, appearing as double size.
- **Quota Expansion**: User requested additional 700-1000 GB on $WORK for staging data and managing checkpoints, logs, and visualizations.
- **Final Resolution**: Quota on $WORK increased to 2500 GB. User advised to write a "Tier3 User Project Report" as payment for the increased quota.

## Key Takeaways
- **$WORK Quota**: 1 TB, mirrored data appears as double size.
- **$VAULT Issue**: No support for sparse files, leading to increased data size.
- **Quota Expansion**: Possible upon request, with additional documentation required.

## References
- [NHR Data Filesystems Documentation](https://doc.nhr.fau.de/data/filesystems/)
- [HPC Usage Reports](https://hpc.fau.de/about-us/hpc-usage-reports/)
```
---

### 42088939_disk%20quota%21.md
# Ticket 42088939

 # HPC Support Ticket: Disk Quota Increase

## Keywords
- Disk quota
- Quota increase
- Numerical simulations
- Master thesis
- HPC account

## Problem
- User's disk quota is insufficient for large numerical simulations.
- The amount of files is approaching or exceeding the originally given quota.

## Root Cause
- Increased data generation from numerical simulations for the user's master thesis.

## Solution
- HPC Admin increased the user's quota for `/home/woody/iwst/iwst144` by 10x to 100/200 GB.

## General Learnings
- Users may require additional disk quota for large-scale simulations.
- HPC Admins can adjust quotas to accommodate user needs.
- Communication between the user and HPC support is essential for resolving quota issues.

## Actions Taken
1. User requested a quota increase via email.
2. HPC Admin reviewed and approved the request.
3. Quota for the specified directory was increased.

## Follow-up
- Monitor user's disk usage to ensure the increased quota is sufficient.
- Provide guidance on data management if further quota increases are needed.
---

### 42133972_Request%20for%20more%20disk%20space.md
# Ticket 42133972

 # HPC Support Ticket: Request for More Disk Space

## Keywords
- Disk quota exceeded
- Storage allocation
- Filesystem usage
- Simulation data
- Documentation

## Summary
A user encountered repeated job failures due to insufficient disk space. The user requested additional storage but was unaware of the appropriate filesystems for simulation data.

## Root Cause
- The user was storing simulation data in `/home/hpc`, which was not intended for such purposes.
- The user exceeded the disk quota in `/home/hpc`.

## Solution
- The HPC Admin advised the user to store simulation data in the appropriate filesystem (`$WOODYHOME`), which is available on both `lima` and `woody`.
- The user was directed to read the documentation on filesystems to understand the correct usage.

## Lessons Learned
- Users should be aware of the intended use of different filesystems on HPC systems.
- Storing simulation data in the correct filesystem can prevent disk quota issues.
- Reading the documentation is crucial for understanding system policies and best practices.

## Recommendations
- Ensure users are informed about the appropriate filesystems for different types of data.
- Encourage users to refer to the documentation for guidelines on filesystem usage.
- Monitor user disk usage and provide timely support to prevent job failures due to quota issues.
---

### 2024041742000703_%5Biwal024h%5D%20Access%20to%20WOODY.md
# Ticket 2024041742000703

 # HPC Support Ticket: Access Issue to WOODY

## Keywords
- Access issue
- WOODY
- User account
- shownicerquota.pl
- Quota data
- Intermittent issue

## Problem Description
- User unable to access their folder on WOODY (`/home/woody/iwal/iwal024h`).
- `shownicerquota.pl` script times out and returns incomplete quota data.

## Root Cause
- Intermittent issue on WOODY affecting user access and quota data retrieval.

## Solution
- HPC Admins are aware of the intermittent issue and are working on it.
- Users may experience the issue on other days as well.
- Advised to try accessing the folder again later.

## General Learnings
- Intermittent issues can affect user access and quota data retrieval on WOODY.
- HPC Admins are actively working on resolving such issues.
- Users should attempt to access their folders again later if they encounter similar problems.
---

### 2024121642002233_High%20File%20Count%20for%20Project%20b167ef.md
# Ticket 2024121642002233

 # HPC Support Ticket: High File Count for Project b167ef

## Keywords
- High file count
- Metadata operations
- Small files
- HPC file systems
- Archiving files

## Problem
- **Root Cause**: The project b167ef was storing 15 million small files on the `$WORK` directory, causing high load and excessive metadata operations on the HPC file systems.

## Solution
- **User Action**: The user acknowledged the issue and planned to delete old single files that were previously packed into an archive for copying.
- **HPC Admin Assistance**: The HPC admin suggested using data formats more suited for HPC file systems and offered assistance in optimizing file storage. They also recommended attending a monthly introduction for AI users for an overview of possible approaches.

## General Learnings
- Storing a large number of small files can lead to high load and excessive metadata operations on HPC file systems.
- Users should consider using data formats better suited for HPC file systems and regularly clean up old or unnecessary files.
- Attending HPC-related seminars or introductions can provide useful insights into optimizing file storage and other best practices.

## Ticket Status
- The ticket was initially created in the wrong queue but was later moved to the correct one.
- The ticket was closed as the user understood the issue and planned to resolve it.
---

### 2024121242000859_Question%20about%20Storing%20Datasets%20on%20Alex%20Cluster%20-%20UTN.md
# Ticket 2024121242000859

 # HPC Support Ticket Conversation: Storing Datasets on Alex Cluster

## Keywords
- HPC Cluster
- Datasets
- Best Practices
- Central Storage
- ImageNet
- Licensing Restrictions

## Summary
A new PhD student inquired about best practices for storing and managing popular AI datasets on the Alex cluster, specifically asking if there is a central managed space for frequently used datasets.

## Root Cause
- Lack of centralized storage for commonly used datasets.
- Concerns about storage efficiency and redundancy.

## Solution
- **HPC Admin Response**:
  - Consideration for a poll to identify commonly used datasets.
  - Licensing restrictions prevent central access to certain datasets (e.g., ImageNet).
  - Users need to download and manage datasets individually for now.

## General Learnings
- **Central Storage**: Some HPC clusters provide central storage for popular datasets to optimize storage usage.
- **Licensing Issues**: Certain datasets have licensing restrictions that complicate centralized access.
- **User Responsibility**: Users may need to manage their own datasets until a centralized solution is implemented.

## Recommendations
- **Future Actions**: Conduct a poll to identify commonly used datasets and explore solutions for centralized storage while considering licensing restrictions.
- **User Guidance**: Inform users about the current need to manage datasets individually and provide best practices for efficient storage usage.

---

This report can be used as a reference for future inquiries about dataset management on the Alex cluster.
---

### 2023031642003886_long-term%20storage%20-%20addlight%20-%20k103bf.md
# Ticket 2023031642003886

 # HPC-Support Ticket Conversation Summary

## Subject
Long-term storage request for project 'addlight' (k103bf)

## Keywords
- Long-term storage
- $HPCVAULT
- TAPE-System
- Quota increase
- Multi-node jobs
- GPUs

## Problem
- User requested 100TB long-term storage for data backup.
- Need for multi-node GPU jobs for scaling purposes.

## Solution
- **Storage**: Initially allocated 200TB on $HPCVAULT for user k103bf10.
  - Note: Possible integer overflow issue with quota display.
- **GPU Jobs**: Enabled multi-node jobs for all k103bf* accounts with `--qos=a100multi`.

## General Learnings
- $HPCVAULT provides high-quality disk storage with daily snapshots and regular tape backups.
- Quotas on $HPCVAULT are set per account, not per group.
- Multi-node GPU jobs can be enabled for specific accounts upon request.
- Large quota allocations may encounter integer overflow issues in the quota display.

## Follow-up
- User expressed intention to distribute storage resources among additional users upon successful allocation.
- Positive feedback and gratitude expressed by the user for the support provided.
---

### 2017101742002025_Speicherplatz%20auf%20home_hpc.md
# Ticket 2017101742002025

 # HPC Support Ticket Analysis: Storage Requirements for Large Data Analysis

## Keywords
- Storage
- Home directory
- Temporary storage
- Data analysis
- Quota increase
- Backup
- Filesystems
- Cluster
- Data transfer

## Summary
A user requested additional storage space for analyzing large datasets on the HPC cluster. The user initially considered using the `/home/hpc` directory but later realized the limitations and explored other options such as temporary directories (`/tmp`) and other filesystems.

## Root Cause
- The user needed to analyze large datasets (up to 4 TB) for their research.
- The `/home/hpc` directory was not suitable due to its limited size and frequent backups.
- Temporary directories (`/tmp`) were considered but found to be inefficient for the user's needs.

## Solutions Explored
1. **Temporary Directories (`/tmp`)**:
   - Initially considered but found to be inefficient due to simultaneous data transfer from the same source.

2. **Parallels Dateisystems (LiMa/Emmy/Meggie)**:
   - Suggested by HPC Admins as suitable for temporary data storage.
   - These systems have a high-water mark deletion policy, which may not retain data for more than a few weeks.

3. **Quota Increase on `/home/vault` and `/home/woody`**:
   - The user requested a temporary increase in quota for these directories to facilitate data analysis.

## Outcome
- The user ultimately requested a temporary increase in quota for `/home/vault` and `/home/woody` to handle the large datasets.
- The HPC Admins provided guidance on the available filesystems and their characteristics.

## Lessons Learned
- Understanding the characteristics and limitations of different filesystems is crucial for efficient data management on HPC clusters.
- Temporary directories may not always be the best solution for large data transfers and analysis.
- Communication with HPC Admins is essential for finding the most suitable storage solutions for specific research needs.

## Recommendations
- Users should consult the HPC documentation and support team to understand the available storage options and their suitability for different types of data.
- HPC Admins should provide clear guidelines on the use of temporary directories and other filesystems to avoid inefficient data management practices.

## References
- [RRZE HPC Environment Documentation](https://www.anleitungen.rrze.fau.de/hpc/environment/#fs)
---

### 2024121642002181_High%20File%20Count%20for%20Project%20b112dc.md
# Ticket 2024121642002181

 # HPC Support Ticket: High File Count for Project

## Keywords
- High file count
- Metadata operations
- File system optimization
- HPC file systems
- Small files

## Problem
- The project is storing 6.5 million files on `$WORK`, causing high load and excessive metadata operations on the file system.

## Root Cause
- Large quantities of small files stored in the project directory.

## Solution
- **User Action**: Users agreed to clean up files after their vacation.
- **Admin Assistance**: Provided file count per user to help the project leader address the right person.
- **Recommendation**: Suggested using data formats more suited for HPC file systems and offered assistance in optimizing file storage.

## General Learnings
- High file counts, especially with small files, can lead to performance issues in HPC file systems.
- Regularly review and clean up small files to optimize storage usage.
- Consider using more efficient data formats for HPC environments.
- HPC admins can assist in providing detailed usage statistics and optimization strategies.

## Follow-up
- The ticket was closed as the user agreed to address the issue.
- Further assistance was offered if needed.

## References
- [HPC Café Introduction for AI Users](https://hpc.fau.de/teaching/hpc-cafe/#nutshell)
---

### 2024102842001706_Over%20quota%20on%20_home_hpc%20%28c105aa11%29.md
# Ticket 2024102842001706

 # HPC Support Ticket: Over Quota on /home/hpc

## Keywords
- Quota
- Storage
- Backups
- Singularity Images
- Grace Period
- Soft Quota
- Hard Quota
- Temporary Quota Extension

## Problem
- User received a notification about exceeding the quota on `/home/hpc`.
- User's storage usage was initially 80GB, reduced to around 60GB.
- Concern about storage usage doubling due to backups.
- Request for a temporary quota extension for one month to complete ongoing runs.

## Root Cause
- User's storage usage reached the soft quota limit due to large Singularity images.
- Backups might have contributed to the increased storage usage.

## Solution
- HPC Admins clarified that the user is currently below the quota limit.
- No quota extensions are offered for `/home/hpc`.
- Suggested moving Singularity images to `/home/vault` to avoid quota issues.

## What to Learn
- Understand the impact of backups on storage usage.
- Be aware of the soft and hard quota limits and the grace period.
- Consider moving large files to alternative storage locations like `/home/vault` to manage quota effectively.
- HPC Admins do not offer quota extensions for `/home/hpc`.

## Additional Resources
- [FAQ: Why is my data taking up twice as much space on the file systems?](https://doc.nhr.fau.de/faq/#why-is-my-data-taking-up-twice-as-much-space-on-the-file-systems)
---

### 2016061642001707_speicherplatz%20vaulthome.md
# Ticket 2016061642001707

 ```markdown
# HPC Support Ticket: Speicherplatz Vaulthome

## Keywords
- Speicherplatz
- Vaulthome
- Quotaerhöhung
- Back-up
- Dateigröße
- Simulationen

## Summary
- **User Request**: Increase storage space on vaulthome from 105G to 300-400G for upcoming simulations.
- **User Account**: sn059, Group caph
- **Current Storage**: 105G
- **Requested Storage**: 300-400G

## Issue
- User is running out of storage space on vaulthome and needs more space for upcoming simulations.
- User has important files on vaulthome that require backup, which is not provided on woodyhome.

## HPC Admin Response
- Quota increase on vaulthome is possible.
- Vaulthome is not ideal for small files; woodyhome is better suited for smaller files.
- Admin inquired about the size of the files the user is primarily working with.

## User Follow-up
- User has some important files on vaulthome that need backup.
- User has already moved less critical files to woodyhome to optimize storage usage.
- User is trying to adhere to the intended purpose of each filesystem.

## Solution
- No final solution provided in the conversation.
- Further discussion needed to determine the appropriate filesystem for the user's needs based on file sizes and backup requirements.

## General Learning
- **Storage Management**: Understand the purpose and suitability of different filesystems (vaulthome vs. woodyhome) for different types of files.
- **Backup Requirements**: Consider backup needs when deciding where to store important files.
- **Quota Increase**: Quota increases are possible but may require justification based on file sizes and usage patterns.
```
---

### 2024070442000151_shownicerquota.pl%20not%20working.md
# Ticket 2024070442000151

 ```markdown
# HPC Support Ticket: shownicerquota.pl Not Working

## Keywords
- shownicerquota.pl
- $VAULT
- $WORK
- $HOME
- rquotad
- wnfs1
- btrfs
- alex[12]
- tinyx

## Problem Description
The user is unable to see quotas for $VAULT and $WORK directories using the `shownicerquota.pl` command. The command only displays the output for $HOME.

## Root Cause
The auto-(re-)start of `rquotad` on `wnfs1` was broken because a modified `rquotad` for btrfs was still running and not fully cleaned up.

## Solution
The issue with `rquotad` on `wnfs1` needs to be resolved by ensuring the modified `rquotad` for btrfs is properly cleaned up and restarted.

## Additional Information
- The problem should rarely occur on `alex[12]` and `tinyx` because these directories are frequently accessed.

## Lessons Learned
- Ensure that `rquotad` is properly configured and cleaned up, especially when using modified versions for specific filesystems like btrfs.
- Regular access to directories can help prevent quota display issues.
```
---

### 2024090542003116_Additional%20space%20for%20backups%20_%20%2B%205TB%20for%20b159cb15%20on%20_home_vault.md
# Ticket 2024090542003116

 ```markdown
# HPC Support Ticket: Additional Space for Backups

## Keywords
- Storage Quota
- Backup
- Quota Extension
- $HPCVAULT
- Fritz Cluster

## Summary
A user requested additional storage space on $HPCVAULT for backups, initially 5 TB, but later required an additional 5 TB due to quota usage being counted twice.

## Problem
- User exceeded the current storage limit with 1.1 TB of data.
- Additional 1 TB of data needed for backup.
- Quota usage on $HPCVAULT counted twice, leading to insufficient storage allocation.

## Solution
- HPC Admins increased the quota for the user on $HPCVAULT by 5 TB, from 1 TB to 6 TB.
- An additional 5 TB quota extension was granted after the user noticed the double counting issue.

## Lessons Learned
- Users should be aware of how quota usage is calculated on $HPCVAULT.
- HPC Admins should consider the possibility of quota usage being counted twice when granting extensions.
- Clear communication about quota usage and storage limits is essential to avoid misunderstandings.
```
---

### 2023062242001647_Dateien%20zwischen%20Benutzern%20desselben%20Projektes%20teilen.md
# Ticket 2023062242001647

 ```markdown
# Sharing Files Between Users of the Same Project on HPC Server

## Keywords
- HPC Support
- File Sharing
- POSIX Rights
- ACL (Access Control List)
- Shared Folder
- Project Collaboration

## Problem
A user wants to share files located on the HPC server (atuin) with other users within the same project (b109dc). The user is looking for a way to set up a shared folder or share files directly.

## Solution
1. **POSIX Rights**:
   - Use POSIX rights to open the folder for the group.
   - Command: `chmod g+rx /home/atuin/$GROUP/$USER`

2. **ACL (Access Control List)**:
   - If sharing with specific members of the project, use ACL.
   - Refer to the FAQ for detailed instructions: [FAQ Link](https://hpc.fau.de/faqs/#innerID-14970)

## General Learning
- **File Sharing**: Understanding the importance of setting appropriate permissions for file sharing within a project.
- **POSIX Rights**: Using `chmod` to set group permissions for shared access.
- **ACL**: Utilizing ACL for more granular control over file access within a project.

## References
- [HPC FAQ](https://hpc.fau.de/faqs/#innerID-14970)
```
---

### 2020060242000217_Unexpected%20file%20quota%20problem.md
# Ticket 2020060242000217

 # Unexpected File Quota Problem

## Keywords
- Quota Exceeded
- /home/vault/wssp/wssp001h
- quota-Befehl
- File Quota
- SoftQ
- HardQ
- Gracetime
- Filec
- FileQ
- FiHaQ
- FileGrace

## Problem Description
The user received a "Quota Exceeded" error message for the directory `/home/vault/wssp/wssp001h`. Despite the directory appearing empty, the quota was exceeded by 40 times. The `quota` command showed only one file in the directory.

## Root Cause
The root cause of the problem was not explicitly identified in the provided conversation. However, it is implied that there might be hidden or system files consuming the quota.

## Solution
No solution was provided in the conversation. Further investigation is needed to identify and resolve the issue.

## General Learnings
- **Quota Management**: Understanding how to interpret and manage file quotas is crucial for HPC users.
- **Hidden Files**: Be aware that hidden or system files can consume quota without being immediately visible.
- **Troubleshooting**: Use the `quota` command to diagnose quota-related issues.

## Next Steps
- **Investigation**: HPC Admins should investigate the directory for hidden or system files.
- **Communication**: Inform the user about the findings and any actions taken to resolve the issue.
- **Documentation**: Update the knowledge base with the resolution once the issue is fixed.
---

### 2024022242000886_HPC%20Storage%20File%20Quota%20Erhoehung.md
# Ticket 2024022242000886

 # HPC Storage File Quota Increase Request

## Keywords
- HPC Storage
- File Quota
- Symlinks
- Inode Quota
- GPFS
- Backup
- Snapshots

## Summary
A user has reached their file quota limit in their allocated storage pool and is requesting an increase. The user has also inquired about the impact of symlinks on the file count.

## Root Cause
- User has reached the file quota limit of > 150k files.
- User has used symlinks to save space but is unsure if they count towards the file quota.

## Discussion
- **Symlinks and File Quota**: Symlinks are counted towards the inode quota.
- **File Quota Increase**: The user's current quota is less than the default quota (150k < 200k). The quota was previously reduced due to the creation of many small files, which is not optimal for GPFS with backup and snapshots.

## Solution
- **Symlinks**: Confirm that symlinks are counted towards the inode quota.
- **File Quota Increase**: Consider increasing the file quota to 200k as a temporary solution. However, note that the user's project has been allocated replacement quota on a CDI server and should migrate their data.

## Notes
- The inode reduction was implemented in response to a previous ticket (#2023110842001021) due to the user's creation of many small files.
- The user's project has been allocated replacement quota on a CDI server and should migrate their data.

## Follow-up
- Monitor the user's file usage and remind them to migrate their data to the CDI server.
- Review the file quota policy for projects that create many small files.
---

### 2024121642002528_High%20File%20Count%20for%20Project%20b211dd.md
# Ticket 2024121642002528

 # HPC Support Ticket: High File Count for Project b211dd

## Keywords
- High file count
- Small files
- Metadata operations
- File system optimization
- HPC file systems
- Storage usage

## Problem
- **Root Cause**: Excessive number of small files stored on the $WORK file system, leading to high load and excessive metadata operations.
- **Details**: The project b211dd was storing 7.7 million files, causing performance issues on the HPC file system.

## Solution
- **User Action**: The user agreed to check which sub-account was exceeding the limit and to require them to delete unnecessary data and store it properly.
- **HPC Admin Assistance**: Offered assistance in optimizing file storage and recommended attending the monthly introduction for AI users for possible approaches.

## General Learnings
- High file counts, especially small files, can significantly impact the performance of HPC file systems.
- Users should be encouraged to use data formats more suited for HPC environments.
- Regular monitoring and communication with users about their storage usage can help prevent such issues.

## Follow-up
- The ticket was closed as the user acknowledged the issue and agreed to take corrective action.
- Further assistance can be provided if the user requires help in optimizing their file storage.

---

This documentation can be used to address similar issues related to high file counts and file system performance in the future.
---

### 2016041142001934_Speicherplatz%20auf%20woody.md
# Ticket 2016041142001934

 # HPC Support Ticket: Storage Space Increase Request

## Keywords
- Storage limit
- Soft limit
- Speicherplatz
- HPC-Kennung
- Project requirements

## Summary
A user has reached the soft limit of their storage space on the HPC system and requires an increase to accommodate their project needs.

## Root Cause
- User reached the soft limit of their allocated storage space (1.5 TB).
- Additional storage (approximately 300 GB) is needed for the current project.

## Solution
- User requested an increase in their storage limit.
- HPC Admin acknowledged the request.

## General Learning
- Users may require additional storage space for their projects.
- HPC Admins should be notified to adjust storage limits as needed.
- Ensure users provide their HPC-Kennung for identification.

## Next Steps
- HPC Admin to evaluate and increase the storage limit if appropriate.
- Communicate the decision and any further steps to the user.
---

### 42369397_%C3%83%C2%9Cbertragung%20Daten%20woody.md
# Ticket 42369397

 # HPC Support Ticket: Data Transfer Issue

## Keywords
- Data Transfer
- Account Management
- Data Ownership
- Quota Management
- Privacy Concerns

## Root Cause of the Problem
- A user's data was mistakenly transferred to the wrong account due to a typo.
- The intended recipient could not access the data, and the original recipient was no longer reachable.

## Lessons Learned
- **Data Transfer Verification**: Always verify the recipient's account details before transferring data.
- **Communication Channels**: Use official contact addresses for support requests to ensure they are not missed.
- **Data Ownership**: Clarify data ownership and obtain necessary permissions before transferring data.
- **Quota Management**: Be aware of quota limits and manage data accordingly to avoid exceeding limits.
- **Privacy Concerns**: Handle private data with care and delete any private information immediately upon recognition.

## Solution
- The user's supervisor sent a formal written request to the HPC admin to gain access to the data.
- The data was transferred to the correct account after verification and approval.
- The user was given a grace period to review and manage the data to stay within quota limits.

## General Guidelines
- **Data Transfer**: Ensure accurate account details and obtain necessary permissions before transferring data.
- **Communication**: Use official support channels for requests.
- **Quota Management**: Regularly review and manage data to stay within quota limits.
- **Privacy**: Handle private data with care and delete any private information immediately upon recognition.
---

### 2022120942002705_Speicherplatz%20_home_vault_empkins.md
# Ticket 2022120942002705

 ```markdown
# HPC-Support Ticket: Speicherplatz /home/vault/empkins

## Problem
- User reports hitting quota limit (ca. 520 GB) for a specific user (iwso049h).
- Storage requirement is moving towards 3 TB.

## Root Cause
- User quota limit was insufficient for the required storage.

## Solution
- HPC Admin increased the vault quota for the user to 3 TB.

## Additional Issues
- Another user (empk004h) also hit the quota limit.
- Quota checker on the frontend showed incorrect values, causing warning messages.

## Actions Taken
- HPC Admin increased the quota for the second user (empk004h) to 3 TB soft, 5 TB hard.
- HPC Admin confirmed the quota checker issue as a bug and advised the user to ignore the warnings.

## Keywords
- Quota limit
- Storage increase
- Quota checker bug
- HPC Admin
- User quota

## General Learnings
- Users may require increased storage quotas for their projects.
- Quota checker bugs can cause incorrect warnings.
- HPC Admins can adjust user quotas as needed.
```
---

### 2024053142000587_RE%3A%20About%20resources%20on%20Alex%20cluster%20and%20file%20system%20-%20b211dd10_b207dd11.md
# Ticket 2024053142000587

 # HPC Support Ticket Summary

## Keywords
- Quota for $WORK Directory
- Data Transfer Between Project Accounts
- CEPH Storage System
- Data Sharing Mechanics

## Problem Description
- **Quota for $WORK Directory**: The user's project requires significant disk space for training large-scale models and checkpointing, exceeding the current 10TB quota.
- **Data Transfer Between Project Accounts**: The user needs to transfer data between different project accounts within the HPC environment.

## Solution Provided
- **Quota for $WORK Directory**: The HPC Admin recommended using the CEPH storage system for storing temporary data such as checkpoints. [Documentation Link](https://doc.nhr.fau.de/data/workspaces/)
- **Data Transfer Between Project Accounts**: The HPC Admin suggested using the built-in data sharing mechanics documented at [Data Sharing Documentation](https://doc.nhr.fau.de/data/share/#granting-hpc-users-access-to-your-data).

## Outcome
- The user acknowledged the suggestions and will implement them in their projects.

## General Learnings
- The CEPH storage system is a viable solution for storing large amounts of temporary data.
- The HPC environment supports multiple mechanisms for sharing data between different accounts, which can be found in the provided documentation.

## Ticket Status
- The ticket was closed after the user confirmed the suggestions were helpful.
---

### 2024030642003091_TMPDIR%20%22No%20space%20left%20on%20device%22.md
# Ticket 2024030642003091

 # HPC Support Ticket: TMPDIR "No space left on device"

## Keywords
- TMPDIR
- No space left on device
- tar extraction error
- SLURM
- /scratchssd
- Job cleanup

## Problem Description
- **User Issue**: Unable to extract `dataset.tar` file to `$TMPDIR` due to "No space left on device" error.
- **Cluster**: tinygpu
- **Error Log**:
  ```
  tar: dataset/test/path1-lr.npy: Cannot write: No more space on the device
  tar: dataset/test/data.csv: Cannot write: No more space on the device
  ```

## Root Cause
- **Disk Space**: Small SSDs in TinyGPU nodes.
- **Shared Resources**: Multiple users sharing a node.
- **Cleanup Mechanism**: Failure in the cleanup mechanism for `$TMPDIR`.
- **Misuse of /scratchssd**: Some users copy data to `/scratchssd` instead of `$TMPDIR`, leading to persistent data that is not cleaned up properly.

## Solution
- **Immediate Fix**: Implemented additional measures to clean up `/scratchssd` during node reboots.
- **Long-term Fix**: Encourage users to use `$TMPDIR` for job-local data or manually clean up their data.
- **Admin Action**: Enhanced cleanup scripts to ensure `$TMPDIR` is properly managed.

## Lessons Learned
- **User Education**: Inform users about proper usage of `$TMPDIR` and the importance of cleaning up temporary data.
- **Resource Management**: Monitor and manage disk space more effectively, especially on nodes with limited storage.
- **Script Improvements**: Ensure cleanup scripts are robust and handle edge cases where data might not be deleted properly.

## Additional Notes
- **Script Example**:
  ```bash
  dst_dir = os.path.join("/scratchssd", os.environ['SLURM_JOB_ID'])  # copy data to SSD
  ```
  - Users should avoid hardcoding paths and use `$TMPDIR` instead.

- **Cleanup Script**:
  ```bash
  # clean up job-private directory
  rm -rf /scratchssd/.privtmp/$SLURM_JOB_USER/${SLURM_JOB_ID}.${SLURM_CLUSTER_NAME}
  # check if the user still has some other jobs on the node
  job_list=`${SLURM_BIN}squeue --noheader --format=%A --user=$SLURM_JOB_UID --node=localhost`
  for job_id in $job_list; do
    if [ $job_id -ne $SLURM_JOB_ID ] ; then
      exit 0
    fi
  done
  # No other SLURM jobs, purge all remaining processes of this user
  pkill -KILL -U $SLURM_JOB_UID
  # clean up private directories
  [ -d /tmp/.privtmp/$SLURM_JOB_USER ]     && rm -rf /tmp/.privtmp/$SLURM_JOB_USER/
  [ -d /dev/shm/.privtmp/$SLURM_JOB_USER ] && rm -rf /dev/shm/.privtmp/$SLURM_JOB_USER/
  [ -d /scratchssd/.privtmp/$SLURM_JOB_USER ] && rm -rf /scratchssd/.privtmp/$SLURM_JOB_USER/
  ```
  - Ensure cleanup scripts are robust and handle all edge cases.

## Conclusion
Proper usage of `$TMPDIR` and effective cleanup mechanisms are crucial for maintaining disk space on HPC nodes. Educating users and improving scripts can help prevent similar issues in the future.
---

### 2018101242002256_Need%20for%20memory%20storage.md
# Ticket 2018101242002256

 # HPC Support Ticket: Need for Memory Storage

## Keywords
- Memory storage
- Videos
- Deep learning
- GulpIO
- Quota increase
- Meeting

## Summary
A user requested storage for 300 GB of videos on a mount point for an experiment. The dataset consists of videos grouped in GulpIO files, a binary storage format for deep learning. The user needed the storage to avoid GPU starvation during deep network training, which involves only reading the data.

## Root Cause
- The user required additional storage space for their experiment.
- The specific storage needs and data access rates were initially unclear.

## Solution
- The HPC Admin temporarily increased the user's quota on `$WOODYHOME = /home/woody/mfhe/mfhe000h`.
- A meeting was suggested with the user and their supervisor to discuss computational needs and the possibility of extending compute and/or storage hardware.

## General Learnings
- Clarify the specific use case and data access rates when users request additional storage.
- Temporary quota increases can be used to address immediate storage needs.
- Follow-up meetings can help in planning for future hardware extensions based on user requirements.

## Next Steps
- Schedule a meeting with the user and their supervisor to discuss long-term storage and computational needs.
- Monitor the user's storage usage and adjust quotas as necessary.
---

### 2020091242000514_WG%3A%20Over%20quota%20on%20_home_vault.md
# Ticket 2020091242000514

 # HPC Support Ticket: Over Quota on /home/vault

## Keywords
- Quota Exceeded
- /home/vault
- Block Quota
- Tape Migration
- Grace Period
- Symlink
- HPC Storage System

## Summary
A user received an automated email notification indicating that they had exceeded their block quota on the `/home/vault` filesystem. The user had not accessed the vault for about a year but suspected that a `find` command run in their home directory might have accessed the vault through a symlink.

## Root Cause
- The user exceeded their block quota on the `/home/vault` filesystem.
- The user had not accessed the vault recently but suspected that a `find` command might have triggered access.

## Solution
- The HPC Admin advised the user to ignore the email, as the files were temporarily brought back from tape due to the ongoing migration to a new HPC storage system.
- The user did not need to take any action, as the files would be automatically migrated back to tape.

## General Learnings
- Automated quota notifications can be triggered by temporary file access during system migrations.
- Users should be aware of symlinks that might cause unintended access to filesystems.
- HPC Admins can provide context about ongoing system changes to help users understand quota notifications.

## Additional Notes
- The user had only 21 large files on tape, which was not enough to warrant a quota increase.
- The HPC storage system migration process can temporarily affect file access and quota reporting.
---

### 42307388_Quota%20bctc32.md
# Ticket 42307388

 # HPC Support Ticket: Quota Increase Request

## Keywords
- Quota Increase
- Ab-initio Modeling
- Density Functional Theory
- Soft Quota
- Hard Quota
- Filesystem

## Summary
A user requested an increase in the quota for their account due to increased storage requirements for ab-initio modeling simulations based on density functional theory.

## Problem
- **Root Cause**: The user's current storage quota (Soft Quota: 100G, Hard Quota: 200G) is insufficient for their new simulation activities, which require storing significant data at each time step.
- **Filesystem**: The issue pertains to the `home/vault` filesystem.

## Solution
- The user was asked to specify the filesystem for which the quota increase was needed.
- The HPC Admin acknowledged the request and likely proceeded with the quota increase, though the final resolution is not explicitly stated in the conversation.

## General Learnings
- **Quota Management**: Understanding the importance of adequate storage quotas for different types of simulations.
- **Communication**: The need for clear communication regarding the specific filesystem when requesting quota changes.
- **User Support**: The process of handling quota increase requests, including gathering necessary information and acknowledging the request.

## Next Steps
- Ensure the quota increase is implemented and verify with the user that the new quota meets their needs.
- Document the new quota settings for future reference.
---

### 2019061942000813_Grace%20Period%20Extension%20for%20iwal012h.md
# Ticket 2019061942000813

 # HPC Support Ticket: Grace Period Extension for User Account

## Keywords
- Grace period extension
- Quota limit
- Storage folders ($VAULT, $WORK, $WOODYHOME)
- File size management
- Tape storage

## Summary
A user requested an extension of the grace period for their account due to exceeding the soft limit for data storage in the $VAULT directory. The user also inquired about the possibility of increasing their quota.

## Root Cause
- User had a dataset above the soft limit (~140 GB) in the $VAULT directory.
- The average size of the user's files was less than 100 MB, which is not suitable for $VAULT storage.

## Solution
- **Grace Period Extension**: The HPC Admin reset the grace period once.
- **Storage Guidance**: The HPC Admin advised the user that $VAULT is intended for long-term storage of large files (several tens of GB per file) for offline tape storage. Smaller files should be stored in $WORK or $WOODYHOME.
  - **$WOODYHOME**: Provides 200 GB quota for free.
  - **Shareholder-HPC-NFS Server**: Groups can buy or rent allocations.

## General Learning
- **Storage Management**: Understand the purpose and appropriate use of different storage directories ($VAULT, $WORK, $WOODYHOME).
- **File Size Considerations**: Ensure that files stored in $VAULT are large enough to justify tape storage. Smaller files should be moved to more suitable directories.
- **Quota Management**: Be aware of quota limits and the possibility of requesting extensions or higher quotas when necessary.

## Actions Taken
- Grace period reset by HPC Admin.
- User advised on proper storage folder usage.

## Follow-up
- User acknowledged the guidance and agreed to use the recommended storage folders in the future.

---

This documentation can be used as a reference for handling similar requests related to grace period extensions and storage management in the future.
---

### 2023021442001446_Shared%20file%20space%20on%20hpc.md
# Ticket 2023021442001446

 # Shared File Space on HPC

## Keywords
- Shared storage
- Container sharing
- Group access
- HPC storage
- Web UI
- Stable diffusion containers

## Problem
- Users need to upload their own stable diffusion containers to individual HPC storage.
- Inefficient due to lack of shared memory for group access.

## Root Cause
- No shared storage space available for group access to containers.

## Solution
- HPC Admin provided a shared directory `/home/janus/b116ba` with a 5TB quota accessible on all systems.

## What Can Be Learned
- **Shared Storage Request**: Users may require shared storage for efficient group access to software containers.
- **Admin Response**: HPC Admin can provide a shared directory with a specified quota to resolve such issues.
- **Communication**: Clear and concise communication helps in resolving user queries efficiently.

## Future Reference
- For similar requests, direct users to the shared directory or create a new one if necessary.
- Ensure users are aware of the shared storage options available on the HPC system.
---

### 2024021342000518_Kosten%20f%C3%83%C2%BCr%20extra%20Speicherplatz.md
# Ticket 2024021342000518

 # HPC Support Ticket: Additional Storage Costs

## Keywords
- Storage space
- Costs
- /home/titan
- /home/saturn
- /home/vault
- BigData Share

## Summary
- **User Inquiry**: Request for pricing information for additional storage space on /home/titan or /home/saturn.
- **HPC Admin Response**: Storage on Titan and Saturn is fully allocated. No current availability for additional storage on these servers. Alternative option is to extend /home/vault. Pricing information available at [BigData Share Application](https://hpc.fau.de/antrag-auf-bigdata-share/).

## Root Cause
- User needs additional storage space and is inquiring about costs and availability.

## Solution
- Inform the user that storage on Titan and Saturn is fully allocated.
- Provide the link to the BigData Share application for pricing information on extending /home/vault.

## General Learning
- Storage availability and pricing should be regularly updated on the HPC website.
- Users should be directed to alternative storage options if their primary choice is unavailable.
- Clear communication about current storage capacities and future availability is essential.
---

### 2018071242001192_Befehl%20%22quota%22.md
# Ticket 2018071242001192

 # HPC Support Ticket: Issue with "quota" Command

## Keywords
- quota
- storage usage
- $HOME
- VAULT
- certificate expiration
- Quota-RPC

## Problem Description
The `quota` command is not displaying the line with values for the user's own storage usage. This issue has been observed by multiple users over several weeks.

## Root Cause
- The issue is related to the Quota-RPC on the `vault*` servers.
- A certificate has expired, causing the `quota` command to malfunction.

## Solution
- The problem was resolved by an active colleague who fixed the Quota-RPC issue, despite being on vacation.
- The `quota` command is now functioning correctly again.

## Lessons Learned
- Certificate expiration can cause issues with the `quota` command.
- Proactive monitoring and timely renewal of certificates are crucial to prevent such issues.
- Collaboration and quick response from the team, even during vacations, can help resolve issues promptly.

## Actions Taken
- The HPC Admin acknowledged the issue and estimated a resolution timeframe.
- A colleague fixed the Quota-RPC issue, restoring the functionality of the `quota` command.

## Future Prevention
- Regularly check and renew certificates to avoid expiration-related issues.
- Ensure that the Quota-RPC is properly configured and monitored.

## Relevant Contacts
- HPC Admins
- 2nd Level Support Team
- Head of the Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support
- Software and Tools Developer
---

### 2021091542000936_500TB%20Storage.md
# Ticket 2021091542000936

 # HPC Support Ticket Conversation Analysis

## Keywords
- HPC Storage
- 500TB Storage
- VAULT
- Quota
- Funktionsaccount
- GPFS-Storagecluster
- NFS4 ACLs
- Spack Environment
- NCO Installation
- NetCDF Libraries
- Elmer/Ice

## General Learnings
- **Storage Management**: Understanding the allocation and management of large storage quotas, including setting up quotas and managing access permissions.
- **Functional Accounts**: The use of functional accounts for long-term data storage and access management.
- **ACL Management**: Configuring and troubleshooting NFS4 ACLs for fine-grained access control.
- **Spack Environment**: Limitations and issues with using Spack environments in the current HPC setup.
- **Software Installation**: Challenges and solutions related to installing specific software packages like NCO and NetCDF libraries.

## Specific Issues and Solutions

### Storage Allocation and Access
- **Issue**: User inquiring about the status of 500TB storage allocation and access permissions.
- **Solution**: Storage integrated into GPFS-Storagecluster. Funktionsaccount created with specific ACLs for access control.

### ACL Management
- **Issue**: Problems with editing ACLs using `nfs4_editfacl`.
- **Solution**: Use `nfs4_setfacl` for setting ACLs as `nfs4_editfacl` is not functioning correctly on the system.

### Spack Environment
- **Issue**: User unable to create and activate Spack environments due to permission and script errors.
- **Solution**: Spack environments are currently not supported due to alias issues. Users should rely on provided modules or manual installations.

### NCO Installation
- **Issue**: User facing difficulties installing NCO due to missing `libnetcdf.a`.
- **Solution**: Use the provided NCO module on Woody-NG. For custom installations, ensure correct linking of libraries and environmental variables.

### NetCDF Libraries
- **Issue**: User had to disable netcdf4 during NetCDF-C installation.
- **Solution**: Ensure compatibility of library versions and dependencies. Refer to previous successful installations for version numbers.

## Documentation for Support Employees

### Storage Allocation and Access
- **Root Cause**: User needed clarification on storage allocation and access permissions.
- **Solution**: Allocate storage in GPFS-Storagecluster and set up a Funktionsaccount with appropriate ACLs.

### ACL Management
- **Root Cause**: `nfs4_editfacl` not functioning correctly.
- **Solution**: Use `nfs4_setfacl` for setting ACLs.

### Spack Environment
- **Root Cause**: Alias issues preventing the use of Spack environments.
- **Solution**: Inform users that Spack environments are not currently supported. Encourage the use of provided modules or manual installations.

### NCO Installation
- **Root Cause**: Missing `libnetcdf.a` during NCO installation.
- **Solution**: Use the provided NCO module. For custom installations, ensure correct linking of libraries and environmental variables.

### NetCDF Libraries
- **Root Cause**: Incompatibility issues with netcdf4.
- **Solution**: Ensure compatibility of library versions and dependencies. Refer to previous successful installations for version numbers.

This documentation can be used to address similar issues in the future, providing a quick reference for support employees.
---

### 2023080442001409_%7CQuestion%20about%20over%20quota%20on%20_home_hpc.md
# Ticket 2023080442001409

 # HPC Support Ticket: Over Quota on /home/hpc

## Keywords
- Over quota
- /home/hpc storage
- Block quota
- Grace period
- Quota report
- Filesystem

## Summary
A user received emails indicating that their /home/hpc storage is over the limit, despite only using about 17 GB of space. The user requested assistance to understand why the system is showing the storage as full.

## Root Cause
The user's quota report shows that they are exceeding their Block Quota of 52.4G for the filesystem /home/hpc. The user has 58.7G used and 704.4M in doubt, which exceeds the soft quota. The grace period has expired, preventing the user from saving any more files.

## Quota Report Details
- **Blocks used:** 58,697,456 (= 58.7G)
- **Blocks in doubt:** 704,448 (= 704.4M)
- **Blocks quota soft:** 52,428,800 (= 52.4G)
- **Blocks quota hard:** 104,857,600 (= 104.9G)
- **Blocks grace remaining:** expired
- **Files used:** 188,161
- **Files in doubt:** 82
- **Files quota soft:** 500,000
- **Files quota hard:** 1,000,000
- **Files grace remaining:** N/A

## Solution
The user needs to reduce their storage usage below the soft quota limit of 52.4G to regain the ability to save files. This can be done by deleting unnecessary files or moving them to another storage location.

## General Learnings
- Users should regularly check their storage usage to avoid exceeding their quota.
- The 'in doubt' values are a result of the parallel filesystem and should not be a major concern.
- The soft quota can be exceeded for up to one week (grace period), after which the user will no longer be able to write until they are below the limit again.
- The hard quota values are absolute maximums and cannot be exceeded.

## Next Steps
- The user should be advised to clean up their storage to stay within the quota limits.
- If the user continues to have issues, further investigation by the 2nd Level Support team may be required.
---

### 2024022742001018_Fwd%3A%20Storage%20problem%20at%20Alex%20cluster.md
# Ticket 2024022742001018

 ```markdown
# HPC Support Ticket: Storage Problem at Alex Cluster

## Keywords
- Storage issue
- Disk quota exceeded
- $HPCVAULT
- $WORK partition
- Human error
- Bogus quota messages
- rsync

## Problem Description
- User unable to create files on $HPCVAULT due to "disk quota exceeded" error despite having sufficient storage.
- User lacks access to $WORK partition.

## Root Cause
- Human error during project creation resulted in missing user folders.
- Recent system update caused bogus "over quota" messages for some users.

## Solution
- HPC Admin fixed the missing user folders, allowing access to $WORK partition.
- Bogus quota messages were resolved by a system update around 10:50 a.m.

## General Learnings
- Human errors in project setup can lead to missing user folders.
- System updates can cause temporary issues like bogus quota messages.
- Regular communication with users is essential to identify and resolve such issues promptly.
```
---

### 2023022042002719_Question%20about%20quota.md
# Ticket 2023022042002719

 # HPC Support Ticket: Question about Quota

## Keywords
- Quota
- HPCVAULT
- Group Quota
- User Quota
- `quota -s` command
- `mmlsquota` command

## Problem
- User unable to determine available space for new data in HPCVAULT.
- `quota -s` command shows 0k for both quota and limit.

## Root Cause
- User quota deactivated and group quota activated for the user's group (iwbi).
- User was unaware of the change and the need to check group quota.

## Solution
- HPC Admin provided group quota information using `mmlsquota` command.
- Confirmed that the user should be able to write more data to vault based on the current usage and group quota limit.

## What to Learn
- Users should be aware of group quotas and how to check them.
- `quota -s` command may not show relevant information when group quotas are in use.
- HPC Admins can use `mmlsquota` command to check group quotas.
- When user quotas are deactivated, group quotas should be considered for determining available space.
---

### 2023011842003457_Gro%C3%83%C2%9Fes%20Verzeichnis%20verschieben.md
# Ticket 2023011842003457

 # HPC Support Ticket: Moving Large Directory

## Keywords
- Large directory
- `mv` command
- `rsync`
- ACL (Access Control List)
- Quota
- Backup
- Tape-Archiv

## Problem
- User wants to move a large directory containing many files from one location to another.
- Concerns about quota limitations and the best method to perform the move.

## Discussion
- **ACL Option**: HPC Admin suggested using ACL to share the directory, but the user already had ACL set up.
- **Quota Concerns**: The user mentioned potential quota issues and the need to move data to a location where quota increase is easier.
- **Backup Considerations**: Neither the source nor the destination servers have backups. The user was advised to consider archiving important data.

## Solution
- **rsync**: HPC Admin initiated a direct server-to-server `rsync` to move the data.
- **Owner Adjustment**: The admin planned to adjust the owner of the files after the `rsync` completes.
- **Backup Recommendation**: The user was advised to archive important data into tar files and store them in the tape archive.

## General Learnings
- For moving large directories, `rsync` is often the preferred method due to its robustness and ability to handle large data sets.
- Consider using ACL for sharing directories if appropriate.
- Always consider backup options, especially for important data.
- Quota limitations should be taken into account when planning data moves.

## Follow-up
- The user was asked to verify the data after the `rsync` and delete the original directory if everything is in order.

---

This documentation provides a summary of the support ticket conversation, highlighting the key points and solutions for future reference.
---

### 2019121642001968_Increase%20Woody%20storage.md
# Ticket 2019121642001968

 # HPC Support Ticket: Increase Woody Storage

## Keywords
- Storage Quota
- Woody (Meggie)
- Titan
- Climate Model (WRF)
- Simulation
- Backup to Tape
- $WORK
- $HPCVAULT

## Problem
- User hit soft quota on Woody with only six days of simulations.
- Needed to run a longer simulation (1 year) with restarts.
- Misunderstanding about running simulations directly from Titan.

## Solution
- **Storage Location**: Use Titan for running simulations as `/home/titan` is available on all HPC systems.
- **Environment Variable**: Set `$WORK` to point to `/home/titan` instead of `/home/woody`.
- **Backup**: Use `$HPCVAULT` (`/home/vault`) for mid- to long-term storage. Create a subdirectory like "backup2tape" and request a rule to migrate files to tape ASAP.

## General Learnings
- **Storage Management**: Understand the different storage options (Woody, Titan, $HPCVAULT) and their appropriate uses.
- **Environment Variables**: Utilize environment variables like `$WORK` to manage storage locations effectively.
- **Backup Strategy**: Use `$HPCVAULT` for long-term storage and request migration to tape to manage quota efficiently.

## References
- [HPC Storage Documentation](https://www.anleitungen.rrze.fau.de/hpc/hpc-storage/)
---

### 2023021342002929_%5BWoody%5D%20Speicherplatzerweiterung.md
# Ticket 2023021342002929

 ```markdown
# HPC Support Ticket: Storage Quota Increase

## Keywords
- Storage quota
- Soft-quota
- Account
- Simulation
- Woody

## Problem
- User requested an increase in the storage quota for their account on Woody from 500 GB to 1 TB.
- The additional storage was necessary for ongoing and future simulations.

## Solution
- HPC Admin increased the user's storage quota on Woody to 1 TB.

## Lessons Learned
- Users may require additional storage for their simulations.
- HPC Admins can adjust storage quotas upon request.
- Effective communication between users and HPC Admins is crucial for managing resources.
```
---

### 2023122342000401_fritz%20_lustre%20file%20quota%20request%20-%20a103bc11.md
# Ticket 2023122342000401

 ```markdown
# HPC-Support Ticket Conversation: File Quota Request

## Keywords
- File quota
- Lustre file system
- Inode limit
- Simulation runs
- MPI ranks
- Restart files
- Output files
- Storage requirements

## Summary
A user requested an increase in the file quota on the Lustre file system from 80,000 to 400,000 files. The request was justified based on the need for a large number of files for simulation runs, including restart files and output files.

## Root Cause
The user's simulation runs require a significant number of files due to the nature of the simulations, which include multiple sets of restart files and output files. Each MPI rank writes its memory to a separate file, leading to a high file count.

## Solution
The HPC Admin increased the inode limit on the Lustre file system for the user's account as requested.

## What Can Be Learned
- **File Quota Requests**: Users may require increased file quotas for simulations that generate a large number of files.
- **Justification**: Detailed justification, including the number of files needed and the purpose of each file, helps in processing the request.
- **Inode Limits**: Adjusting inode limits is a common solution for handling large file counts on Lustre file systems.
- **Storage Management**: Understanding the storage requirements and file counts for simulations is crucial for efficient resource management.

## Action Taken
- The HPC Admin increased the inode limit on the Lustre file system for the user's account to 400,000 files.

## Follow-Up
- Ensure that the user's simulations run smoothly with the increased file quota.
- Monitor the Lustre file system for any performance issues related to high file counts.
```
---

### 2019080442000025_WG%3A%20Over%20quota%20on%20_home_hpc.md
# Ticket 2019080442000025

 # HPC Support Ticket: Over Quota on /home/hpc

## Keywords
- Quota Exceeded
- Singularity Cache
- Hidden Directory
- Grace Period
- Soft Quota
- Hard Quota

## Summary
A user received multiple notifications about exceeding their quota on the `/home/hpc` filesystem. The user was unaware of any actions that could have caused the significant increase in data usage.

## Root Cause
- **Hidden Directory**: The user's quota was exceeded due to a hidden directory created by Singularity (`/home/hpc/sles/sles000h/.singularity`), which was storing 13G of data.
- **Quota Misunderstanding**: The user was not receiving login warnings and the `quota` command did not provide information about `/home/hpc`, leading to confusion.

## Solution
- **Identify Hidden Directory**: The HPC Support team identified the hidden directory created by Singularity.
- **Documentation Reference**: The team referred to Singularity documentation, which mentions that Singularity creates folders in the user's home directory for Docker layers, Cloud library images, and metadata.
- **Cache Directory Configuration**: The user was advised to set the `SINGULARITY_CACHEDIR` environment variable to a different path to avoid future quota issues.

## General Learnings
- **Hidden Directories**: Applications like Singularity can create hidden directories that consume significant storage space.
- **Quota Commands**: The `quota` command may not always provide information about all filesystems, leading to user confusion.
- **Grace Period**: Users have a grace period to reduce their data usage before reaching the hard quota limit.
- **Documentation**: Referencing application documentation can help identify and resolve unexpected storage usage.

## Next Steps for Similar Issues
- Check for hidden directories created by applications.
- Verify quota usage across all relevant filesystems.
- Advise users to configure application settings to avoid storing large amounts of data in their home directories.
---

### 2019012142000391_Quota%20auf%20WOODYHOME%2C%20mount%20cifs%2C%20sshfs.md
# Ticket 2019012142000391

 # HPC Support Ticket Conversation Analysis

## Keywords
- Quota warning
- Quota limit
- /home/woody
- NFS mount
- cifs
- sshfs
- NAS
- Emmy cluster

## Root Cause of the Problem
- User received a quota warning and needs to understand the quota limit on `/home/woody`.
- User wants to mount their own NAS on the Emmy cluster but encounters issues with `cifs` and `sshfs`.

## What Can Be Learned
- **Quota Management**: Users need clear guidance on how to interpret quota limits and where to find this information on the HPC website.
- **Mounting NAS**: Users may face issues with mounting their own NAS using `cifs` and `sshfs`. They need guidance on the correct commands and permissions required.
- **Efficient Data Transfer**: Users may be using inefficient methods to transfer data between their local machines and the HPC cluster. Providing better solutions for data transfer can improve user experience.

## Solution (if found)
- **Quota Management**: Ensure that quota limits and how to interpret them are clearly documented on the HPC website.
- **Mounting NAS**: Provide detailed instructions on how to mount NAS using `cifs` and `sshfs`, including the necessary permissions and commands.
- **Efficient Data Transfer**: Suggest more efficient methods for data transfer, such as using `rsync` or other tools designed for large data transfers.

## Next Steps
- Update the HPC website to include clear instructions on quota management.
- Create a guide for users on how to mount their own NAS on the Emmy cluster.
- Provide recommendations for efficient data transfer methods.
---

### 2024102442003775_Daten%20l%C3%83%C2%B6schen.md
# Ticket 2024102442003775

 ```markdown
# HPC Support Ticket: Daten löschen

## Problem
- User's HPC account (iwso116h) was deleted or access was lost.
- User received quota exceeded emails despite being unable to log in via SSH.

## Root Cause
- Account deletion or access loss prevented the user from managing their data.
- Quota warnings continued to be sent despite the account status.

## Solution
1. **Account Reactivation**:
   - User was advised to contact the project supervisor to extend the account.
   - After 24 hours, the user should be able to log in and manage their data.

2. **Quota Adjustment**:
   - Quota values were adjusted to prevent further warning emails.
   - Suggestion to modify the quota warning script to check account status before sending emails.

## Keywords
- Account deletion
- Quota exceeded
- SSH access
- Account reactivation
- Quota adjustment

## General Learnings
- Ensure quota warning scripts check account status to avoid sending emails to inactive accounts.
- Reactivating an account may restart the deletion process, so adjusting quota values can be a temporary solution.
```
---

### 42242733_Problem%20on%20CSHPC%20Account.md
# Ticket 42242733

 # HPC Support Ticket: Problem on CSHPC Account

## Keywords
- Account expiration
- Disk quota
- Home directory
- Nomachine NX
- SSH login
- Grace period

## Summary
A user reported being unable to connect to their CSHPC account, initially suspected to be due to account expiration. However, the root cause was identified as exceeding the disk quota in the home directory.

## Root Cause
- **Disk Quota Exceeded**: The user had exceeded the disk quota in their standard home directory for over a week, preventing the creation of new files.

## Solution
- **Reset Grace Period**: The HPC Admin reset the grace period on the user's quota, allowing them to write files again and log in through Nomachine NX.
- **Clean Up Home Directory**: The user was advised to clean up their home directory within 7 days to avoid the grace period expiring again.

## Additional Information
- **Quota Check Command**: The command `shownicerquota.pl` can be used to check the current disk usage.
- **Filesystem Details**: Information on available filesystems at RRZE can be found [here](http://www.rrze.fau.de/dienste/arbeiten-rechnen/hpc/systeme/hpc-environment.shtml#fs).

## Lessons Learned
- **Disk Quota Management**: Regularly check and manage disk quotas to avoid login issues.
- **Warning Messages**: Ensure users are aware of warning messages regarding disk quota limits.
- **Alternative Login Methods**: Inform users about alternative login methods (e.g., SSH) that may still work when Nomachine NX fails.
---

### 2024040442002441_Re%3A%20NHR%20Nutzung%20in%20Erlangen.md
# Ticket 2024040442002441

 # HPC Support Ticket Conversation Analysis

## Keywords
- Quota
- Storage
- Datasets
- GPUs
- NHR@FAU
- HPC Documentation
- NFS-Storage
- CEPH Workspace
- A100
- H100
- BayernKII
- LRZ
- Exportkontrolle
- SSO
- Point of Contact
- Projekt managen
- Onboarding
- Cluster
- Zugang
- Einladungen zur Nutzung
- NVMe-basiert
- KI/ML Anwendungen
- df
- quota -s
- shownicerquota.pl

## General Learnings
- **Quota Management**: Each project gets a default quota of 10 TB on `/home/atuin`. Quotas can be increased upon request.
- **Storage Systems**: The HPC center uses NFS-Storage and NVMe-based CEPH Workspace for KI/ML applications.
- **GPU Resources**: The center has a significant number of NVIDIA A100 and A40 GPUs, with plans to install more H100 GPUs.
- **User Management**: Users can manage their own accounts within their projects.
- **Documentation**: The documentation may contain outdated information, such as the location of quota files.
- **Support Process**: Users should respond to support emails to ensure their requests are tracked in the ticket system.

## Root Cause of Problems
- **Quota Information**: The user was unable to find quota information in the expected location (`/home/atuin/quota/v104dd.txt`).
- **Storage Requirements**: The user needed clarification on the available storage quota and the possibility of increasing it.

## Solutions
- **Quota Information**: The correct way to check quota is using commands like `df`, `quota -s`, and `shownicerquota.pl`.
- **Storage Requirements**: The quota was increased to 50 TB (55 TiB) upon request. Users should explicitly request quota increases if needed.

## Documentation for Support Employees

### Quota Management
- **Default Quota**: 10 TB on `/home/atuin`.
- **Checking Quota**: Use commands `df`, `quota -s`, and `shownicerquota.pl`.
- **Increasing Quota**: Submit a request to HPC Admins for quota increase.

### Storage Systems
- **NFS-Storage**: High capacity storage for general use.
- **CEPH Workspace**: NVMe-based storage optimized for KI/ML applications.

### GPU Resources
- **Current GPUs**: NVIDIA A100 (80 GB / 40 GB) and A40.
- **Future GPUs**: Plans to install H100 GPUs (94 GB HBM) in the second half of the year.

### User Management
- **Account Management**: Users can manage their own accounts within their projects.
- **Point of Contact**: Designated users can manage the project and send invitations to other users.

### Documentation
- **Updates**: Ensure documentation is up-to-date, especially regarding quota information and file locations.

### Support Process
- **Ticket System**: Users should respond to support emails to ensure their requests are tracked in the ticket system.
- **Explicit Requests**: Users should explicitly request quota increases or other resources as needed.

This analysis provides a concise overview of the key points and solutions from the support ticket conversation, which can be used as a reference for future support cases.
---

### 2017032242000101_Mount%3A%20externer%20Server.md
# Ticket 2017032242000101

 ```markdown
# HPC-Support Ticket: Mounting External File Server

## Summary
A user requested to mount an external file server on the HPC servers to avoid copying large data sets and to save temporary storage space.

## Keywords
- Mount
- External File Server
- Data Processing
- Temporary Storage
- Large Data Sets
- Administrative Overhead
- User Permissions

## Problem
- The user wanted to mount an external file server (Columbia) on the HPC servers.
- The 'mount' command is not allowed for regular HPC users.
- The goal was to avoid copying large data sets (100GB-1TB) and to save temporary storage space on the HPC servers.

## Discussion
- The HPC Admins discussed the feasibility of mounting the external server.
- Concerns were raised about the administrative overhead and the reliability of such a setup.
- The server is housed at the RRZE but not administered by them.

## Decision
- After internal discussions, the HPC Admins decided not to mount the external server due to administrative overhead and potential reliability issues.
- The user was advised to use the normal RRZE-HPC file systems for temporary data storage.

## Solution
- The user was informed that the only alternative is to use the existing RRZE-HPC file systems for data storage.
- For large, temporary data, the parallel file systems of the clusters should be used.

## Lessons Learned
- Mounting external servers on HPC systems can introduce significant administrative overhead and reliability concerns.
- Users should be encouraged to use the existing HPC file systems for data storage.
- Clear communication about the limitations and alternatives is crucial for user satisfaction.
```
---

### 42187325_Speicherplatz%20Erweiterung.md
# Ticket 42187325

 ```markdown
# HPC-Support Ticket: Speicherplatz Erweiterung

## Keywords
- Speicherplatz
- Quota
- Erweiterung
- Simulationen
- Woody-Cluster

## Problem
- User requires an increase in storage capacity from 500 GB to 1 TB due to storage-intensive simulations.

## Root Cause
- Insufficient storage capacity for running simulations.

## Solution
- HPC Admin increased the user's quota on `/home/woody` to 1 TB.

## General Learnings
- Users may request storage capacity increases for intensive simulations.
- HPC Admins can adjust quotas to meet user needs.
- Proper communication and quick response are essential for maintaining user satisfaction.
```
---

### 2024022742001072_Disk%20quota%20exceeded%20error%20on%20Alex%20cluster.md
# Ticket 2024022742001072

 ```markdown
# HPC-Support Ticket: Disk Quota Exceeded Error on Alex Cluster

## Keywords
- Disk quota exceeded
- OSError: [Errno 122]
- Downtime
- Quota infos
- Bogus over quota messages

## Problem Description
- **User Issue:** After a recent downtime, all jobs fail with the error "OSError: [Errno 122] Disk quota exceeded."
- **Quota Report:**
  ```
  Path              Used     SoftQ    HardQ    Gracetime  Filec    FileQ    FiHaQ    FileGrace
  /home/hpc           61.3G   104.9G   209.7G        N/A     278K     500K   1,000K        N/A
  /home/vault        704.9G  1048.6G  2097.2G        N/A   2,620      200K     400K        N/A
  ```
- **Additional Info:** Colleagues also encounter the same error.

## Root Cause
- **Cluster Issue:** Bogus "over quota" messages were experienced by some users after a recent update.

## Solution
- **Admin Response:** The issue was fixed around 10:50 a.m.

## General Learning
- **Post-Downtime Issues:** After downtimes or updates, users may experience temporary issues such as bogus quota messages.
- **Quota Management:** Ensure quota settings are correctly applied and monitored post-update.
- **Communication:** Inform users promptly about resolved issues to minimize disruption.
```
---

### 2016031742000695_Rule%20on%20backup2tape.md
# Ticket 2016031742000695

 ```markdown
# HPC-Support Ticket: Rule on backup2tape

## Keywords
- backup2tape
- data migration
- backup rule
- tape archive
- data transfer

## Summary
A user requested a change in the rule for transferring data to tape from 5 days to 1 day for a large amount of data in the `backup2tape` directory.

## Problem
- User needed to archive a large amount of data (1TB on top of ~1TB already moved) in the `backup2tape` directory.
- The current rule was to transfer data to tape after 5 days untouched.
- User requested a change to transfer data after 1 day untouched.

## Solution
- HPC Admin changed the rule from >3 days to >1 day.
- Clarified that the system performs backups before migration to tape.
- Informed the user that files may still be online after one day until the system makes a backup of the data.

## Lessons Learned
- The system performs automatic backups before migrating data to tape.
- Changing the rule for data migration to tape can help manage large data transfers more efficiently.
- Users should be aware that files may remain online until the backup process is complete.

## Conclusion
The user's request was successfully addressed, and the rule was changed to accommodate the large data transfer. The user was informed about the backup process to avoid any confusion.
```
---

### 2015092842002636_HPC%20Quota%20Erweiterung.md
# Ticket 2015092842002636

 # HPC Quota Extension Request

## Keywords
- HPC Quota Extension
- Dateisystem
- /home/woody
- /home/vault
- Quota Increase

## Summary
A user requested a quota extension for their HPC account, specifically an increase of 200GB. The HPC Admin inquired about the specific dateisystem involved. The user specified /home/woody as the preferred dateisystem, with /home/vault as an acceptable alternative.

## Root Cause
- User required additional storage space for their HPC account.

## Solution
- The HPC Admin increased the user's quota on /home/woody by 240GB, resulting in a total quota of 1.99TB.

## What to Learn
- When requesting a quota extension, users should specify the dateisystem they need the increase for.
- HPC Admins can provide quota increases upon request, given the necessary details.
- The process involves specifying the desired dateisystem and the amount of additional storage needed.

## References
- [HPC Environment](http://www.hpc.rrze.fau.de/systeme/hpc-environment.shtml#fs)
- [HPC Services](http://www.hpc.rrze.fau.de/)
---

### 2023112342001466_Re%3A%20Action%20required%3A%20Too%20many%20small%20files%20on%20%24FASTTMP%20of%20Fritz%20-%20k103b.md
# Ticket 2023112342001466

 # HPC Support Ticket Conversation Analysis

## Keywords
- Small files
- Lustre
- Quota
- HDF5
- Tar
- Corrupted files
- Performance issues
- Metadata load
- File consolidation
- Grace time
- Inodes

## General Learnings
- **Small Files Issue**: Lustre-based parallel file systems experience slowdowns due to an abundance of small files, which cause excessive metadata load.
- **Quota Management**: Users need to manage their quota effectively to avoid running out of space.
- **File Consolidation**: Consolidating small files into larger archives improves performance and reduces metadata load.
- **Corrupted Files**: Corrupted tar files are difficult to recover; repacking data is often the only solution.
- **HDF5 Solution**: Using HDF5 for file consolidation can help manage large datasets more efficiently.
- **Grace Time**: Grace time for quota can expire, causing jobs to fail. Resetting grace time and increasing soft quota can resolve this issue.
- **Inodes**: High file counts in a single directory can cause performance issues. Reducing the number of files in such directories is recommended.

## Root Cause of the Problem
- The user had an abundance of small files on the Lustre file system, causing excessive metadata load and performance issues.
- Some files were corrupted due to I/O issues, and the user needed assistance in recovering and managing these files.

## Solution
- The user was advised to consolidate small files into larger archives using HDF5.
- The user was given a reset of grace time and an increase in soft quota to manage their data more effectively.
- The user was advised to reduce the number of files in directories with high file counts to improve performance.

## Documentation for Support Employees
### Small Files and Lustre Performance
Lustre-based parallel file systems experience slowdowns due to an abundance of small files, which cause excessive metadata load. To improve performance:
- Consolidate small files into larger archives using formats like HDF5.
- Delete unnecessary small files to reduce metadata load.

### Quota Management
Users need to manage their quota effectively to avoid running out of space. If a user runs out of quota:
- Reset grace time and increase soft quota if necessary.
- Advise the user to delete or archive old files to free up space.

### Corrupted Files
Corrupted tar files are difficult to recover. If a user encounters corrupted files:
- Advise the user to repack the data in question.
- Provide assistance in managing and recovering corrupted files if possible.

### Grace Time and Inodes
Grace time for quota can expire, causing jobs to fail. If a user encounters this issue:
- Reset grace time and increase soft quota if necessary.
- Advise the user to manage their data more effectively to avoid running out of quota.

High file counts in a single directory can cause performance issues. If a user encounters this issue:
- Advise the user to reduce the number of files in directories with high file counts.
- Provide assistance in managing and organizing files to improve performance.

This documentation can be used to solve similar errors if they appear again.
---

### 2020051442001357_Quota%20auf%20vault.md
# Ticket 2020051442001357

 # HPC Support Ticket: Quota Issue on Vault

## Keywords
- Quota
- File limit
- Vault
- Migration
- HPC Storage

## Problem
- User encountered a quota issue due to the number of files, not storage space.
- User reached the file limit of 200K on Vault.

## Root Cause
- The user's computational work generated a large number of files, exceeding the file quota.

## Solution
- **Request Denied**: Due to upcoming HPC storage renewal, no quota extensions were granted to avoid complicating migration.
- **User's Response**: The user understood the situation and planned to manage the file count independently.

## General Learnings
- Quota limits on Vault include both storage space and the number of files.
- Storage renewal and migration processes can temporarily halt quota extensions.
- Users should be prepared to manage their file counts, especially during migration periods.

## Next Steps for Support
- Inform users about upcoming migrations and their potential impact on quota requests.
- Provide guidelines on managing file counts to stay within quota limits.

## Related Roles
- **HPC Admins**: Handled the quota request and explained the migration constraints.
- **User**: Requested quota increase and understood the limitations due to migration.

## Additional Notes
- The ticket highlights the importance of communication regarding system updates and their impact on user quotas.
- Users should be proactive in managing their file counts to avoid hitting quota limits.
---

### 2023090742000153_FW%3A%20Over%20quota%20on%20_home_hpc%20-%20Questions%20-%20b178bb11.md
# Ticket 2023090742000153

 ```markdown
# HPC Support Ticket: Over Quota on /home/hpc - Questions

## Summary
A user exceeded their quota on the `/home/hpc` filesystem and requested additional storage for a large-scale project. The user also inquired about available storage options and the possibility of increasing the quota.

## Keywords
- Quota
- Storage
- HPC
- Simulations
- Project
- $HOME
- $WORK
- $VAULT

## Root Cause
The user exceeded their block quota of 52.4G on the `/home/hpc` filesystem.

## Solution
- **Quota Increase**: HPC Admins clarified that quota increases for `$HOME` are not offered.
- **Alternative Storage**: The user was advised to use `$WORK` and `$VAULT` for larger storage needs.
  - `$WORK`: Group/project quota of 10T.
  - `$VAULT`: Default quota of 500G per user.
- **Data Project**: The user was informed about the possibility of applying for a "data-project" to extend storage time on the system.

## What to Learn
- **Quota Management**: Understanding the quota limits and grace periods for different filesystems.
- **Storage Options**: Familiarity with available storage options (`$HOME`, `$WORK`, `$VAULT`) and their respective quotas.
- **Data Projects**: Knowledge of applying for "data-projects" to extend storage time.
- **Documentation**: Encouraging users to refer to the HPC storage documentation for detailed information.

## Conclusion
The user moved their data to `$WORK` and will submit jobs from there. The HPC Admins confirmed that the project quota on `$WORK` can be increased if needed.
```
---

### 2022022142000015_Disk%20full.md
# Ticket 2022022142000015

 # HPC Support Ticket: Disk Full

## Keywords
- Disk quota
- $HOME directory
- GPU job
- Cache files
- Temporary files
- Anaconda
- $WORK directory
- $HPCVAULT

## Problem
- User's disk quota in the $HOME directory has been exceeded.
- User suspects cache or temporary files as the cause.
- User is unable to submit GPU jobs due to the quota limitation.

## Root Cause
- Large folders (anaconda3, lfn) consuming significant space in the $HOME directory.
- Software and data inappropriately stored in the $HOME directory.

## Solution
- **Move Software**: Relocate software like Anaconda to the $WORK directory.
  - Reference: [HPC Storage Documentation](https://hpc.fau.de/systems-services/systems-documentation-instructions/hpc-storage/)
- **Move Data**: Transfer data to a more suitable location such as $HPCVAULT.
- **Customize Anaconda**: For help with customizing Anaconda, refer to the [Python and Jupyter Documentation](https://hpc.fau.de/systems-services/systems-documentation-instructions/special-applications-and-tips-tricks/python-and-jupyter/).

## General Learning
- Avoid storing large software and data in the $HOME directory.
- Use appropriate directories like $WORK for software and $HPCVAULT for data.
- Regularly monitor and manage disk usage to prevent quota issues.

## References
- [HPC Storage Documentation](https://hpc.fau.de/systems-services/systems-documentation-instructions/hpc-storage/)
- [Python and Jupyter Documentation](https://hpc.fau.de/systems-services/systems-documentation-instructions/special-applications-and-tips-tricks/python-and-jupyter/)
---

### 42018624_HPC%20Account%20iwst101.md
# Ticket 42018624

 # HPC Support Ticket: HPC Account Quota Increase

## Keywords
- HPC Account
- Quota
- Storage
- Simulation
- Diplomarbeit
- Dateisystem
- /home/woody

## Summary
A user requested an increase in their HPC account quota due to exceeding the current limit while performing simulations for their Diplomarbeit.

## Root Cause
- User exceeded the allocated quota of 10 GB for their HPC account.
- Needed additional storage to avoid frequent data transfers.

## Solution
- HPC Admin increased the user's quota on the /home/woody filesystem to 20 GB.

## General Learnings
- Users may require increased storage for extensive simulations.
- Clarify the specific filesystem when requesting quota changes.
- HPC Admins can adjust quotas to accommodate user needs.

## Next Steps for Similar Issues
- Verify the specific filesystem in question.
- Assess the user's storage requirements and adjust the quota accordingly.
- Communicate the changes clearly to the user.
---

### 2024080542001978_Disk%20quota%20always%20exceeded%20bug%20%20in%20work%20folder%20after%20larger%20quota%20was%20intr.md
# Ticket 2024080542001978

 # HPC-Support Ticket: Disk Quota Exceeded in Work Folder

## Keywords
- Disk quota
- File count quota
- Work folder
- Group quota
- File system performance
- Data staging
- Webdatasets
- HDF5

## Problem Description
- User reported that disk quota was always exceeded in the work folder after the quota was increased by 10 TB.
- The issue occurred only in the work folder and not in other directories like `$HOME` or `$HPCVAULT`.
- The user could not create an empty directory due to the 'Disk quota exceeded' error.

## Root Cause
- The number-of-files-quota was accidentally reset to the new default of '10 million' when the disk quota was increased.
- The group had a large number of files (87.6 million) stored in the work folder, which contributed to the issue.

## Solution
- HPC Admins fixed the issue by setting the file count quota to 100M.
- Users were advised to use proper data formats like webdatasets or HDF5 to manage large numbers of files more efficiently.
- Users were encouraged to clean up duplicates and optimize their data storage practices.

## General Learnings
- Always check both disk space and file count quotas when troubleshooting quota-related issues.
- Proper data management practices, such as using specialized file formats, can significantly improve performance and efficiency.
- Regular communication and collaboration between users and HPC support can help address infrastructure challenges and optimize resource usage.
- Benchmark performance may not always correlate with real-life usage, and continuous monitoring is essential to ensure optimal performance.

## Follow-up Actions
- HPC support will work with users to extend documentation and intro courses on proper data storage in AI contexts.
- Users will be encouraged to clean up duplicates and optimize their data storage practices.
- Continuous monitoring of file system performance and user practices is necessary to ensure optimal resource usage.
---

### 2023062142000239_Tobias%20Kloeffel.md
# Ticket 2023062142000239

 # HPC Support Ticket Conversation Analysis

## Keywords
- Data cleanup
- Quota
- HPC account
- Saturn
- Titan
- Backup
- Wartung
- HPC Portal
- IDM
- Verlängerung
- Hin- und Herkopieren

## Summary
A user requested additional time to clean up data on the HPC system due to personal circumstances. The conversation involved clarifying account validity, data storage, and system maintenance schedules.

## Root Cause of the Problem
- User needed more time to clean up data due to relocation.
- Concerns about data backup and potential system downtime.

## Solution
- HPC Admins agreed to extend the time for data cleanup until the end of August.
- Users were informed about upcoming system maintenance and the lack of backups.
- Quota reminder emails will be sent starting mid-August.

## General Learnings
- **Communication**: Clear communication between users and HPC Admins is crucial for resolving issues.
- **Data Management**: Users should be aware of data storage policies and upcoming maintenance schedules.
- **Backup**: Importance of regular backups and understanding that HPC systems may not provide backup services.
- **Account Management**: Users should regularly check their account validity and quota usage.

## Action Items
- **Users**: Clean up data by the agreed deadline to avoid quota issues.
- **HPC Admins**: Send quota reminder emails to both the user and the data owner to ensure timely action.

## Notes
- Saturn and Titan systems were acquired together and have similar maintenance schedules.
- Users should be prepared for potential system downtime without prior notice after the maintenance period.

---

This report provides a summary of the HPC support ticket conversation, highlighting the key issues, solutions, and general learnings for future reference.
---

### 2024061042002185_Request%3A%20Group%20shared%20directory%20for%20g103ea.md
# Ticket 2024061042002185

 ```markdown
# HPC Support Ticket: Request for Group Shared Directory

## Keywords
- Group shared directory
- Project directory
- SSO-Login verification
- Directory creation

## Summary
A user requested a group shared directory for their project. The HPC Admin created the directory and provided instructions for future requests.

## Root Cause
- User requested a group shared directory for their project.
- The request was initially delayed due to verification issues.

## Solution
- HPC Admin created the directory `/home/atuin/g103ea/shared`.
- User was instructed to use the email address linked to their SSO-Login for future requests to ensure verification.

## Lessons Learned
- Always use the email address linked to your SSO-Login for verification purposes.
- HPC Admins can create group shared directories upon verified requests.
```
---

### 2022111442003278_Quota-Erh%C3%83%C2%B6hung.md
# Ticket 2022111442003278

 # HPC Support Ticket: Quota Increase Request

## Keywords
- Quota Increase
- NHR Project
- /home/atuin
- 10TB to 30TB

## Problem
- User's current quota for their NHR project (`/home/atuin/b124da`) is 10TB, which is insufficient.

## Solution
- HPC Admin increased the quota on `/home/atuin` to 30TB.

## General Learnings
- Users may request quota increases when their allocated storage is insufficient.
- HPC Admins can adjust quotas as needed to accommodate user requests.
- The process involves direct communication between the user and the HPC Admin.

## Related Parties
- HPC Admins
- 2nd Level Support Team
- Head of the Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support
- Software and Tools Developer

## Root Cause
- Insufficient storage quota for the user's project needs.

## Resolution
- Quota was successfully increased to the requested amount.
---

### 2023022342001081_data%20archive%20options%3F.md
# Ticket 2023022342001081

 # HPC-Support Ticket: Data Archive Options

## Keywords
- Long-term data storage
- Project quota
- Data archiving
- Tape library
- Metadata
- Data access

## Problem
- User needs to store multi-terabyte datasets long-term (up to 10 years) for compliance with funding agency requirements.
- Concerned about the lack of long-term storage options beyond 500GB.

## Discussion
- **HPC Admin**: Confirmed that the project has a default quota of 10TB in `$WORK`, extendable upon request. Long-term storage solutions are still under discussion.
- **User**: Clarified the need for data storage for potential misconduct allegations and for future paper revisions/follow-up projects.
- **HPC Admin**: Offered quota extensions on `$WORK` or `$HPCVAULT`. Discussed the possibility of moving data to a tape library for long-term storage.

## Solutions
- **Short-term**: Quota extensions on `$WORK` or `$HPCVAULT` can be requested during the project's lifetime.
- **Long-term**: Data can be moved to the tape library for long-term storage. The procedure is not yet established for NHR accounts but can be arranged.

## Open Questions
- Data access and sharing preferences.
- Data ownership and responsibility, especially when scientists leave the organization.
- Metadata storage and enforcement.

## Next Steps
- User to confirm if the tape library procedure fits their needs.
- Further discussion on data access, ownership, and metadata management.

## Notes
- The tape library was installed in 2020, and data may need to be migrated before the 10-year mark.
- Long-term storage solutions are still under discussion and development.

## Related Links
- [FAU Archiv Procedure](https://www.anleitungen.rrze.fau.de/serverdienste/fau-archiv/fau-archiv-en/)
---

### 2024081642000421_Doppelter%20Speicherverbrauch%20in%20HOME.md
# Ticket 2024081642000421

 ```markdown
# HPC Support Ticket: Double Storage Usage in HOME

## Keywords
- Double storage usage
- Quota discrepancy
- `du` vs `ls`
- HOME vs WORK
- Binary files
- Python

## Problem Description
- User noticed that the quota on HOME increases by double the actual storage required when saving binary files with Python.
- `du` shows double the storage usage, while `ls` shows the correct size.
- Issue observed for both large and small files, including files copied from other systems.
- Problem not observed on WORK.

## Diagnostic Information
- `du -hs` output shows double the size compared to `ls -la`.
- `shownicerquota.pl` output before and after saving a file shows increased usage.
- `quota` command output shows disk quotas for the user.

## Root Cause
- The discrepancy in storage usage is likely due to the file system's handling of sparse files or metadata.

## Solution
- Refer to the FAQ: [Why is my data taking up twice as much space on the file systems?](https://doc.nhr.fau.de/faq/#why-is-my-data-taking-up-twice-as-much-space-on-the-file-systems)

## Lessons Learned
- Understanding file system behavior and quota management is crucial for efficient storage usage.
- Differences in storage reporting tools (`du` vs `ls`) can provide insights into file system operations.
- Consulting FAQs and documentation can resolve common issues quickly.
```
---

### 2018060642000518_Speicherplatz%20auf%20woody.md
# Ticket 2018060642000518

 # HPC Support Ticket: Storage Space Increase on Woody

## Keywords
- Storage space
- Woody
- Quota increase
- RZE Kennung

## Problem
- User's allocated storage space on Woody is insufficient.
- Current storage space: 50GB
- Requested storage space: 500GB

## Root Cause
- Insufficient storage space for user's needs.

## Solution
- HPC Admin increased the storage space to 500GB.

## General Learnings
- Users may request additional storage space if their current allocation is insufficient.
- HPC Admins can adjust storage quotas as needed.
- Users should provide their RZE Kennung for identification purposes.

## Follow-up
- None mentioned.

## Related Tags
- Storage management
- Quota adjustment
- User support
---

### 42015358_computations%20on%20woody.md
# Ticket 42015358

 # HPC Support Ticket Conversation Analysis

## Keywords
- HPC Account Management
- Disk Quota
- CFX Simulation
- Job Submission
- Script Availability

## General Learnings
- **Account Expiration**: Accounts have expiration dates, and data may be deleted after a grace period.
- **Disk Quota**: Users may encounter issues due to exceeding disk quotas on different filesystems.
- **Custom Scripts**: Some simulation tools may require custom scripts that need to be provided by specific users or groups.
- **Filesystem Management**: Different filesystems have different policies for quotas and data retention.

## Specific Issues and Solutions

### Issue: Account Expiration
- **Root Cause**: User's account had expired, leading to login issues.
- **Solution**: User needs to reactivate the account using the usual account forms, signed off by the person-of-contact at their institute.

### Issue: CFX Script Not Found
- **Root Cause**: The `cfxps` command, a custom script, was not available in the user's directory.
- **Solution**: User should check with the specific group (e.g., Philipp Epple and coworkers) who created the script to obtain it.

### Issue: Disk Quota Exceeded
- **Root Cause**: User exceeded disk quota on `/home/woody` and `/home/rrze`.
- **Solution**:
  - HPC Admin increased the quota on `/home/woody`.
  - User needs to remove data from `/home/rrze` as HPC cannot increase the quota there.

## Documentation for Support Employees
- **Account Reactivation**: Ensure users are aware of account expiration dates and the process for reactivation.
- **Custom Scripts**: Document the availability and source of custom scripts required for specific simulation tools.
- **Disk Quota Management**: Monitor and manage disk quotas, providing clear instructions to users on how to manage their data to stay within quotas.

## Conclusion
This conversation highlights the importance of account management, custom script availability, and disk quota management in an HPC environment. Support employees should be prepared to guide users through account reactivation, script acquisition, and data management to ensure smooth operation of computational tasks.
---

### 2024101642003996_Disk%20quota%20for%20project%20b235bb.md
# Ticket 2024101642003996

 # HPC Support Ticket: Disk Quota for Project b235bb

## Keywords
- Disk quota
- Home directory
- Fileserver
- $HOME
- $WORK
- Soft-limit

## Problem
- User requested an increase in disk quota for specific users in a project from ~100 GB to 2 TB.
- The current soft-limit for disk space was too limiting for later stages of the project.

## Root Cause
- The default quota for the home directory ($HOME) cannot be changed.

## Solution
- Inform the user about the available 10 TB on the fileserver (atuin), accessible via $WORK.

## General Learning
- The home directory ($HOME) has a fixed disk quota that cannot be increased.
- Users should utilize the fileserver ($WORK) for larger storage needs, which offers more substantial disk space.

## Actions Taken
- HPC Admin informed the user about the fixed quota for the home directory.
- HPC Admin directed the user to use the fileserver (atuin) for additional storage.

## Follow-up
- Ensure users are aware of the storage options and limitations on the HPC system.
- Provide documentation or training on how to effectively use the fileserver for large data storage.
---

### 42195918_backup%20home_vault.md
# Ticket 42195918

 # HPC Support Ticket: Backup Home/Vault

## Keywords
- Backup
- Tape storage
- Quota
- Migration rule
- /home/vault

## Problem
- User has a large amount of data to backup.
- User is on hard quota in `/home/vault` with less than 30 hours remaining.
- User cannot trigger tape backup directly.

## Root Cause
- User needs to backup data but lacks the ability to initiate tape backup and is constrained by quota limits.

## Solution
- **Temporary Quota Increase**: HPC Admins can temporarily increase the quota for `/home/vault` directories to allow bulk data transfer.
- **Manual Migration**: Users can provide a list of files/directories for HPC Admins to migrate to tape.
- **Automatic Migration Rule**: Set up a rule for automatic migration based on file size, type, and access time.

## General Learnings
- Users cannot directly initiate tape backups.
- Temporary quota increases can be requested for bulk data transfers.
- Automatic migration rules can be set up for frequent data backups.

## Actions Taken
- HPC Admins temporarily increased the quota for the specified directories.
- Users will move data into the directories for tape backup.

## Next Steps
- Users to notify HPC Admins when ready to start moving data.
- HPC Admins to confirm when the data migration can begin.

---

This documentation provides a summary of the issue, the root cause, the solution, and the actions taken to resolve the problem. It can be used as a reference for similar issues in the future.
---

### 2019071942000277_Absturzursache%20bei%20Simulationen%20auf%20EMMY%20_%20FASTTMP%20DIsk%20Quota%20exceeded%20%3F.md
# Ticket 2019071942000277

 # HPC Support Ticket: Absturzursache bei Simulationen auf EMMY / FASTTMP Disk Quota exceeded

## Keywords
- OpenFOAM
- FASTTMP
- Disk Quota
- File Quota
- Parallel Filesystem
- Simulation Abort

## Problem Description
- User's simulations using OpenFOAM on EMMY were aborting with the error "Disk quota exceeded."
- The user was unaware of the file quota limits on FASTTMP and assumed there were no such limits.
- Simulations were generating a large number of small files, leading to the file quota being exceeded.

## Root Cause
- The FASTTMP filesystem has a quota for the number of files that can be created, not just the space used.
- OpenFOAM simulations were generating a large number of small files, exceeding the file quota limit.

## Solution
- **HPC Admin** explained that FASTTMP has a file quota to prevent performance degradation due to a large number of small files.
- The user was advised to use a different filesystem if OpenFOAM cannot be configured to reduce the number of small files.
- The user suggested that future documentation should clearly state the file quota limits to avoid confusion.

## General Learnings
- Parallel filesystems like FASTTMP are optimized for large files and can become slow with many small files.
- File quotas are implemented to prevent misuse and maintain system performance.
- Clear documentation of quota limits can help users understand and avoid issues.
- Users should be aware of the specific requirements and limitations of the filesystems they are using.

## Follow-up
- The user mentioned that a newer version of OpenFOAM (v1906) has improved handling of small files, but it is not yet available on EMMY.
- **HPC Admin** responded that new software versions are not automatically installed but can be requested if needed.

## References
- [HPC Storage Overview](https://www.anleitungen.rrze.fau.de/hpc/hpc-storage/#overview)
---

### 2025022842002273_Project%20proposal%20with%20storage%20requirements%20-%20gz16.md
# Ticket 2025022842002273

 # HPC-Support Ticket Conversation Analysis

## Subject: Project proposal with storage requirements

### Keywords:
- Project proposal
- Storage requirements
- Operational side
- Storage system
- Quality of storage

### Summary:
A user inquires about a project proposal that involves specific storage requirements, potentially including a distinct storage system. The user seeks clarification on the plans, the amount of storage needed, and the quality of storage required for the project.

### Root Cause:
- Lack of information about the storage requirements and plans for a specific project proposal.

### Solution:
- The user needs detailed information from the project lead (Prof. Chiogna) regarding the storage requirements, including the amount and quality of storage needed for the project.

### General Learnings:
- Project proposals may involve specific storage requirements that need to be communicated clearly to the operational side of the HPC center.
- It is important to understand both the quantity and quality of storage needed for new projects to ensure proper resource allocation.

### Next Steps:
- HPC Admins should follow up with the project lead to gather detailed storage requirements.
- Ensure that the operational team is informed about any new storage systems or requirements to facilitate smooth project implementation.

---

This documentation can be used to address similar inquiries about project proposals and their storage requirements in the future.
---

### 2017121542001884_Quota%20auf%20_home_woody.md
# Ticket 2017121542001884

 # HPC Support Ticket: Quota Reduction on /home/woody

## Keywords
- Quota reduction
- /home/woody
- Simulation
- Storage space
- Notification

## Summary
A user reported an unexpected reduction in their quota on `/home/woody`, which impacted their ongoing simulations requiring high storage space.

## Root Cause
- The quota was reduced without prior notification or consultation with the user.
- The user was running simulations that required significant storage space.

## User Request
- Temporary increase in quota to accommodate ongoing simulations.
- Future notifications for such changes to be sent via email rather than automated messages.

## HPC Admin Response
- The total size of `/home/woody` is 88 TB, with half financed by users.
- The HPC center has around 600 users, resulting in an average quota of 80 GB per user.
- The user's quota was temporarily increased to 1 TB, with no guarantee of a permanent increase.

## Solution
- The user's quota was temporarily increased to 1 TB to accommodate their immediate needs.
- No permanent solution was provided, and the user was advised to reduce their storage usage.

## Lessons Learned
- Importance of communicating quota changes to users in advance.
- Temporary quota increases can be granted to accommodate urgent needs.
- Users should be aware of the need to manage their storage usage within the provided quota.

## Next Steps
- Implement a system for notifying users of quota changes via email.
- Monitor and manage storage usage to ensure fair distribution among users.

## References
- HPC Services, Friedrich-Alexander-Universitaet Erlangen-Nuernberg
- Regionales RechenZentrum Erlangen (RRZE)

---

This documentation aims to assist HPC support employees in handling similar quota-related issues in the future.
---

### 2024062742002466_too%20much%20I_O%20on%20Alex%20-%20v103fe15.md
# Ticket 2024062742002466

 # HPC Support Ticket: Excessive I/O on Alex

## Keywords
- Excessive I/O
- Small files
- File system impact
- Data storage optimization

## Problem Description
- **Root Cause:** User's job on Alex generated too many small files, causing excessive I/O operations (~4 million files).
- **Impact:** High I/O operations per second, affecting the file system and impacting all users.

## Affected Directory
- `/home/atuin/v103fe/v103fe15/data/sets/nuscenes/samples`

## Solution
- **Recommendation:** Change the way data is stored to reduce the number of small files.
- **Resource:** Refer to the documentation on data management: [Data Management Guide](https://doc.nhr.fau.de/data/datasets/)

## General Learning
- Excessive I/O due to a large number of small files can degrade file system performance and impact other users.
- Optimizing data storage methods can mitigate such issues.
- Provide users with resources and guidance on best practices for data management.

## Follow-Up
- **Action:** Ticket closed by HPC Admin.
- **Contact:** Users are encouraged to contact support for further assistance.

---

**Note:** This documentation is intended to help support employees identify and resolve similar issues related to excessive I/O and data storage optimization.
---

### 2022102542003848_Linking%20Tier-3%20and%20Tier-2%20accounts.md
# Ticket 2022102542003848

 # HPC Support Ticket: Linking Tier-3 and Tier-2 Accounts

## Keywords
- Tier-3 account
- Tier-2 account
- Home directory
- Data access
- File permissions
- User-spack
- Library installation

## Problem
- User has separate Tier-3 and Tier-2 accounts with different home directories.
- User wants to access data and installed libraries from one account to another to avoid reinstalling dependencies.

## Root Cause
- Tier-3 and Tier-2 accounts use different namespaces, groups, and partially filesystems, preventing direct linking.

## Solution
- **Data Access:**
  - Modify Unix file and directory permissions to allow read access for other accounts.
  - Directories along the path must have at least execute permission (`chmod o+x DIR`).
  - Files need read and optionally execute permission for others.

- **Library Access:**
  - Apply suitable permissions to the USER-SPACK directory to access installed software with both accounts.
  - Note that Tier-3 and NHR accounts have different `$WORK` servers.

## Additional Information
- NHR account lifetime is bound to the granted duration of the NHR project.
- Accounts may be extended for prolonged projects, but new accounts will be generated for new projects.

## Follow-up
- User will attempt the suggested data sharing/access strategy and report back if further assistance is needed.
---

### 2025022842001649_Tar%20installation%20on%20fritz.md
# Ticket 2025022842001649

 # HPC Support Ticket: Tar Installation on Fritz

## Keywords
- Tar installation
- HPC
- Fritz
- Unexpected EOF in archive
- gzip error
- Quota
- Corrupted file

## Summary
A user encountered issues while trying to unzip a tar file on the HPC system Fritz. The error messages indicated an unexpected end of file (EOF) and gzip errors.

## Root Cause
The root cause of the problem was not explicitly identified in the conversation, but potential causes mentioned include:
1. The downloaded/copied tar file is corrupted.
2. The user has exceeded their quota.

## Solution
The HPC Admin suggested the following steps to troubleshoot the issue:
1. Check if the tar file is corrupted.
2. Use the script `shownicerquota.pl` to check if the user is over quota.

## Conversation Highlights
- The user initially contacted the general helpdesk but was redirected to the HPC support team.
- The HPC Admin provided specific instructions for contacting the HPC support team and potential reasons for the tar extraction failure.
- The user confirmed that the provided information was helpful.

## Lessons Learned
- Always verify the integrity of tar files before extraction.
- Check user quota to ensure there is sufficient space for file operations.
- Redirect HPC-specific issues to the appropriate support team for efficient resolution.

## Next Steps
- If the issue persists, the user should contact the HPC support team at `support-hpc@fau.de` for further assistance.
- Ensure that the tar file is not corrupted and that the user is within their quota limits.
---

### 42025845_Re%3A%20iww120%3A%20Soft%20Quota-Limits%20auf%20_home_woody%20erreicht%21.md
# Ticket 42025845

 # HPC Support Ticket: Quota Limits on /home/woody

## Keywords
- Quota limits
- Disk space
- `du -sh` command
- File system
- Backup
- $FASTTMP

## Summary
A user received a quota limit warning for the `/home/woody` directory but found discrepancies when checking the used space with the `du -sh` command.

## Root Cause
- The quota messages are sent once per day based on the disk occupancy at that time.
- The user's running simulations may have created/modified/deleted files, changing the actual occupancy.

## Solution
- The HPC Admin increased the user's quota on `/home/woody` to 50/100 GB.
- Suggested using `$FASTTMP` for large files, noting that there is no backup or quota but high-water-mark deletion.

## General Learnings
- Quota messages reflect the disk occupancy at a specific time and may not match real-time usage.
- The `du -sh` command can be used to check the current disk usage of a directory.
- Different file systems have varying quota and backup policies.
- `$FASTTMP` is suitable for large files but lacks backup and has automatic deletion policies.

## Actions Taken
- Increased user quota on `/home/woody`.
- Provided information on alternative storage options like `$FASTTMP`.

## Follow-up
- Users should monitor their disk usage regularly to avoid reaching quota limits.
- Consider using appropriate file systems based on the nature of the data and backup requirements.
---

### 2023081442000696_Inodes%20auf%20fundus%20bei%20100%20%25%20-%20_faudatacloud_fsbcpc01%20-%20W.%20Utz.md
# Ticket 2023081442000696

 ```markdown
# HPC-Support Ticket Conversation: Inodes auf fundus bei 100 %

## Keywords
- Inodes
- Duplicity
- NFS
- Quota
- RRZE-Backup
- Fundus
- BigDataStorage

## Summary
The user reported that the Inodes on the `faudatacloud/fsbcpc01/shared` directory were fully utilized. The user requested an increase in the Inode limit. The HPC Admin initially misunderstood the issue as a capacity limit problem rather than an Inode limit problem. The user was advised to reduce the number of files and directories to avoid further issues.

## Root Cause
- The user's backup process using Duplicity created a large number of small files, leading to the exhaustion of Inodes.
- The user had previously used rsync, which also contributed to the high Inode usage.

## Solution
- The user was advised to clean up old rsync processes and reduce the number of files created by Duplicity.
- The HPC Admin increased the quota to 150 TB and suggested using the RRZE-Backup service if the issue persists.
- The user was also advised to create larger Duplicity packages to reduce the number of files.

## Lessons Learned
- It is important to distinguish between capacity limits and Inode limits when diagnosing storage issues.
- Regularly cleaning up old backup processes and optimizing the backup strategy can help prevent Inode exhaustion.
- The HPC storage system is not designed for a large number of small files, and alternative solutions like RRZE-Backup should be considered for such use cases.

## Follow-up
- The user was scheduled for a Zoom meeting to discuss the changes in billing.
- The migration of Fundus to a 2PB Windows Filer is under discussion.
- The ticket was closed, and further communication will continue in a related ticket.
```
---

### 2024022742003767_Over%20quota%20-%20mptf007h.md
# Ticket 2024022742003767

 # HPC Support Ticket: Over Quota Issue

## Keywords
- Disk quota exceeded
- Quota management
- GPFS
- File copy error

## Summary
A user encountered a "Disk quota exceeded" error when attempting to copy files in a specific directory on the HPC cluster, despite the quota report indicating that the quota was not exceeded.

## Problem Description
- **Error Message:** "Disk quota exceeded"
- **Affected Directory:** `/home/vault/mptf/mptf007h/boltzmann_CDW/TEST_ANTONIO/restart`
- **Command Used:** `cp` to copy 128 ~1 MB files
- **Quota Report:**
  ```
  Path              Used     SoftQ    HardQ    Gracetime  Filec
  FileQ    FiHaQ    FileGrace
  /home/hpc            5.8G   104.9G   209.7G        N/A  10,605
  500K   1,000K        N/A
  /home/woody        136.2G   500.0G   750.0G        N/A     492K
  5,000K   7,500K        N/A
  /home/vault        531.3G  1048.6G  2097.2G        N/A      92K
  200K     400K        N/A
  ```

## Troubleshooting Steps
1. **User Action:** The user re-ran the copy command, and it worked without any changes, suggesting a temporary issue.
2. **Admin Action:** HPC Admins attempted to reproduce the issue but were unable to do so. They checked the GPFS system, which appeared to be functioning correctly.

## Root Cause
The exact cause of the issue could not be determined due to its non-reproducibility. It was likely a temporary glitch in the system.

## Solution
The issue resolved itself when the user re-ran the copy command. No specific action was taken by the HPC Admins to fix the problem.

## Lessons Learned
- **Temporary Issues:** Sometimes, issues can be temporary and resolve themselves upon retrying the command.
- **Reproducibility:** Without the ability to reproduce an issue, it is challenging to identify the root cause.
- **GPFS Check:** Ensuring the GPFS system is functioning correctly is a crucial step in troubleshooting quota-related issues.

## Next Steps
- **Monitoring:** Continue monitoring for similar issues to identify any patterns or underlying causes.
- **Documentation:** Update documentation to include steps for users to retry commands in case of temporary errors.
---

### 2022122142002432_Need%20of%20Storage.md
# Ticket 2022122142002432

 # HPC Support Ticket: Need of Storage

## Keywords
- Storage request
- File quota
- Conda environments
- Inode usage

## Summary
A user requested additional storage for their project due to a large training dataset. The HPC admin identified that the issue was not disk space but file quota, particularly in the `/home/vault` directory. The user's Conda environments were consuming a significant number of inodes.

## Root Cause
- The user's Conda environments were stored in the `/home/vault` directory, leading to a high inode usage.
- The user was not utilizing the provided miniconda version and the module system.

## Solution
- The HPC admin advised the user to move their Conda environments to the `$WORK` directory.
- The user was instructed to use the miniconda version provided by the HPC center.
- Relevant documentation links were provided to the user for setting up and managing Python environments.

## General Learnings
- Conda environments can consume a large number of inodes, leading to file quota issues.
- Users should be encouraged to use shared resources and provided modules to optimize storage and inode usage.
- Regular monitoring and management of Conda environments are necessary to prevent excessive inode usage.
- Clear communication about the distinction between disk space and file quota is important for user understanding.

## Follow-up Actions
- The Conda discussion was suggested to be moved to a GUI issue or an admin meeting in January.
- The user's request was closed after providing the necessary guidance.

## Relevant Documentation
- [Environment Modules](https://hpc.fau.de/systems-services/documentation-instructions/environment/#modules)
- [Python and Jupyter](https://hpc.fau.de/systems-services/documentation-instructions/special-applications-and-tips-tricks/python-and-jupyter/)
- [TensorFlow and PyTorch](https://hpc.fau.de/systems-services/documentation-instructions/special-applications-and-tips-tricks/tensorflow-pytorch/)
---

### 2025021742000778_Failure%20on%20FRITZ.md
# Ticket 2025021742000778

 ```markdown
# HPC Support Ticket: Failure on FRITZ

## Subject
Failure on FRITZ

## Keywords
- GROMACS jobs
- Quota limit
- File editing issues
- vi editor

## Problem Description
- Three running GROMACS jobs were mysteriously quit by the system without any error message.
- Unable to edit and save job files in `vi`. When trying to save via `:wq`, an error is printed and the content of the file gets deleted.

## Root Cause
- The user's group was at the quota limit on Atuin.

## Solution
- The HPC Admin increased the quota on Atuin by 5TB for the project.

## Lessons Learned
- Quota limits can cause jobs to be terminated without error messages.
- Quota limits can also prevent editing and saving files in `vi`.
- Increasing the quota can resolve these issues.

## Follow-up
- The user agreed to reduce the quota over the upcoming days.

## Ticket Status
- Closed
```
---

### 2017071442001421_Quota%20exceeded.md
# Ticket 2017071442001421

 ```markdown
# HPC-Support Ticket: Quota Exceeded

## Summary
User reports job failures due to exceeded disk quota on the HPC system.

## Keywords
- Quota exceeded
- Lustre filesystem
- Job failures
- Disk quota
- File count
- Grace period

## Problem Description
- User's jobs fail due to exceeded disk quota.
- User has a large number of files and directories, exceeding the quota limit.
- Filesystem miscounts the number of files, causing quota enforcement issues.

## Root Cause
- User had over 15 million files, exceeding the quota limit of 5 million.
- Filesystem miscounts the number of files due to a configuration issue.
- Parameter `osd-zfs.lxfs-MDT0000.quota_iused_estimate` needs to be set to 1 to fix the counting issue.

## Solution
- User needs to delete excess files to stay within the quota limit.
- HPC Admin sets the parameter `osd-zfs.lxfs-MDT0000.quota_iused_estimate` to 1 to correct the file count.
- Monitor the filesystem to ensure the parameter setting is not lost during updates or power failures.

## Lessons Learned
- Regularly monitor and manage file counts to stay within quota limits.
- Ensure proper configuration of the filesystem to avoid miscounting issues.
- Communicate with users about quota limits and the importance of managing file counts.
- Document the parameter settings required to maintain accurate file counts.

## Additional Notes
- The normal quota for file count is 500,000, but it was temporarily increased to 5 million for the user.
- The filesystem has a total capacity of 850 TB, and users should be mindful of their usage to avoid impacting other users.
```
---

### 2018091242000546_Speicherplatzerh%C3%83%C2%B6hung%20Emmy%20Cluster%20f%C3%83%C2%BCr%20bcpc000h.md
# Ticket 2018091242000546

 # HPC Support Ticket: Storage Quota Increase for Emmy Cluster

## Keywords
- Storage Quota
- Emmy Cluster
- MD Simulations
- NFS Storage
- $FASTTMP
- Quota Increase

## Summary
A user requested an increase in storage quota on the Emmy Cluster due to extensive MD simulations. The HPC Admin provided information on suitable storage options and eventually increased the user's quota.

## Root Cause
- User's storage quota was insufficient for MD simulations.
- User required additional storage space similar to a colleague's allocation.

## Solution
- HPC Admin increased the user's quota on `/home/vault` to 1 TB soft / 2 TB hard.
- Recommended using `$FASTTMP` for large binary files generated by MD simulations.
- Provided information on available storage options and their characteristics.

## What Can Be Learned
- Users may require increased storage quota for specific types of simulations.
- Different storage systems (e.g., NFS, $FASTTMP) have varying suitability for different types of data and access patterns.
- HPC Admins can provide guidance on the most appropriate storage solutions based on user needs.
- Documentation on available storage systems should be referenced for optimal usage.

## References
- [HPC Environment Documentation](https://www.anleitungen.rrze.fau.de/hpc/environment/#fs)
- [Job Info](https://www.hpc.rrze.fau.de/HPC-Status/job-info.php?USER=bcpc000h&JOBID=981567&ACCESSKEY=2780c0e1&SYSTEM=EMMY)

## Additional Notes
- HPC Admin reminded the user about an email regarding storage expansion options and costs.
- The user was informed about the possibility of purchasing additional NFS storage for their working group.
---

### 2025011442003451_error%20regarding%20HPC%20account%20-%20iwso157h%20over%20quota.md
# Ticket 2025011442003451

 # HPC Support Ticket: JupyterHub Server Start Error Due to Quota Exceeded

## Keywords
- JupyterHub
- Quota Exceeded
- Server Start Error
- SSH Login
- $WORK Directory

## Problem Description
- User unable to start JupyterHub server.
- Error message indicating memory quota exceeded.
- User received alerts about quota exceedance previously.

## Root Cause
- User's account is over quota, preventing JupyterHub server from starting.

## Solution
- **User Action**: Log in to the cluster using SSH and move files to the `$WORK` directory to free up space.
- **Admin Advice**: Confirmed that SSH login should work even if quota is exceeded. User needs to manage their storage to resolve the issue.

## General Learnings
- Exceeding storage quota can prevent JupyterHub servers from starting.
- Users can still log in via SSH to manage their files even if their quota is exceeded.
- Moving files to the `$WORK` directory can help free up space and resolve quota-related issues.

## Follow-Up
- If the issue persists after moving files, further investigation into the user's account and storage usage may be necessary.
---

### 2020100542000811_Re%3A%20Over%20quota%20on%20_home_vault.md
# Ticket 2020100542000811

 # HPC Support Ticket: Over Quota on /home/vault

## Keywords
- Quota Exceeded
- Ownership Change
- Grace Period
- Soft Quota
- Hard Quota
- LDAP

## Problem Description
- User received a quota warning for exceeding the block quota on the `/home/vault` filesystem.
- The user was not actively using the system but suspected the issue might be related to their group.

## Root Cause
- Data from former group members, whose accounts were deleted from LDAP, were still present in the user's directory.
- These files had no owner and were recently reassigned to the user, causing the quota to be exceeded.

## Solution
- HPC Admins adjusted the user's quota to prevent further warnings.
- Affected directories were identified and listed for the user to help with cleanup.

## Lessons Learned
- Regularly review and clean up data from former group members to avoid quota issues.
- Communicate with HPC Admins to adjust quotas if necessary.
- Understand the difference between soft and hard quotas, and the grace period for exceeding soft quotas.

## Affected Directories
- `/home/vault/iww1/iww163/GROUP/JONATHAN_DISLOC/`
- `/home/vault/iww1/iww163/ERIK/DATA_WOLFRAM/{AU_TENSILE_TEST/,MOD_IMD_30MAR2011/,OLD/,WIRECUT_2_16MAR2011/}`

## Quota Report
- **Blocks used:** 4,845,820,160 (= 4845.8G)
- **Blocks quota soft:** 4,613,734,400 (= 4613.7G)
- **Blocks quota hard:** 5,138,022,400 (= 5.1T)
- **Blocks grace remaining:** 6 days

## Follow-up
- The user acknowledged the issue and planned to clean up the affected directories.
---

### 2021101242002197_Fehlender%20Fasttmp%20ordner%20auf%20emmy.md
# Ticket 2021101242002197

 ```markdown
# HPC-Support Ticket: Missing FASTTMP Folder

## Keywords
- FASTTMP
- Disk Quota
- Emmy
- Account Management

## Problem Description
- User reports missing FASTTMP folder on Emmy.
- User frequently hits HPC home disk quota.

## Root Cause
- FASTTMP folder not created for the user's account.

## Solution
- HPC Admin needs to create the FASTTMP folder for the user's account.

## General Learning
- FASTTMP folders are essential for users who frequently hit disk quota limits.
- Ensure all user accounts have necessary folders created during setup.
```
---

### 2022011142000929_Quota%20Erh%C3%83%C2%B6hung.md
# Ticket 2022011142000929

 ```markdown
# HPC Support Ticket: Quota Increase

## Keywords
- Quota Increase
- Storage Management
- User Request
- HPC Admin
- $WORK Directory

## Summary
A user requested an increase in their quota on the `/home/woody` directory from 1.5 TB to 2 TB to accommodate additional preprocessed data.

## Root Cause
- User needed additional storage space for preprocessed data.

## Solution
- HPC Admin increased the quota on the `$WORK` directory to 2 TB.

## Lessons Learned
- Users may require additional storage space for new data sets or preprocessed data.
- HPC Admins can quickly address quota increase requests to ensure users have sufficient storage.
- Effective communication between users and HPC Admins is crucial for timely resolution of storage-related issues.
```
---

### 2023092942003725_No%20space%20left%20on%20device.md
# Ticket 2023092942003725

 # HPC Support Ticket: No Space Left on Device

## Keywords
- No space left on device
- Inode
- Quota
- Filesystem
- df command
- Home directory

## Summary
A user encountered the error "No space left on device" while working on the cluster, despite having available quota. The issue was observed on a specific node (milan1).

## Root Cause
- The filesystem was full due to high Inode usage, not due to individual user quota issues.
- The Inode limit was reached, causing the error.

## Analysis
- The HPC Admin analyzed the Inode usage and found no single user or group responsible for the excessive usage.
- Top groups by Inode usage were identified: iwal, iwi5, iwso, iwfa, capn.

## Solution
- The Inode limit was increased to 200 million as a preventive measure.
- Current Inode usage was noted as 105 million.

## Lessons Learned
- Regular monitoring of Inode usage is crucial to prevent filesystem issues.
- Increasing the Inode limit can be a temporary solution to avoid disruptions.
- Identifying and managing high Inode usage groups can help in better resource allocation.

## Follow-Up Actions
- Continue monitoring Inode usage.
- Consider implementing policies to manage Inode usage more effectively.
- Communicate with high Inode usage groups to optimize their storage practices.
---

### 2019022142000665_AW%3A%20%5BRRZE-HPC%5D%20current%20opportunities%20to%20participate%20in%20near-term%20HPC-expansion.md
# Ticket 2019022142000665

 # HPC Support Ticket Conversation Analysis

## Keywords
- HPC Storage Expansion
- NFS Storage
- Investment vs. Service
- Quota Increase
- Billing Options

## Summary
- **User Request**: Additional 25 TB of NFS storage for 5,000 EUR.
- **HPC Admin Response**: Confirmed the availability and increased the quota from 22.5 TB to 47.5 TB.
- **Billing Options**:
  - Option a) Investment: 5,000 EUR for 25 TB storage.
  - Option b) Service: To be formulated as a service.
- **User Preference**: Chose Option a) and requested the bill to be sent to a colleague.

## Root Cause
- User needed additional storage due to high utilization of existing storage.

## Solution
- HPC Admin increased the quota by 25 TB and provided billing options.
- User chose the investment option and requested the bill to be sent to a colleague.

## General Learnings
- HPC users can purchase additional storage if needed.
- There are different billing options available for HPC services.
- HPC Admins can quickly adjust quotas and provide necessary support for storage expansion.

## Next Steps
- Ensure the bill is sent to the correct contact.
- Monitor storage usage to anticipate future needs.
---

### 2024030142001243__scratch%20auf%20tinyx%20mal%20wieder%20komplett%20voll.md
# Ticket 2024030142001243

 # HPC Support Ticket Analysis

## Keywords
- /scratch
- tinyx
- full storage
- quota
- ML-Trainingsdaten
- du
- ls
- user limit

## Problem
- The `/scratch` directory on `tinyx` is full.
- A specific user's dataset (`/scratch/dataset/train`) is occupying a significant amount of space (86G).

## Root Cause
- Excessive storage usage by a specific user, likely due to machine learning training data.

## Solution
- HPC Admin set a quota of 20 GB for the user.
- Deleted data from expired users to free up space.

## Lessons Learned
- Regularly monitor storage usage to prevent full storage issues.
- Implement and enforce quotas for users to manage storage space effectively.
- Periodically delete data from inactive or expired users to reclaim storage space.

## Commands Used
- `du -xahd 1 /scratch/* | sort -hr | head -n 1`: Check disk usage of directories in `/scratch`.
- `ls -adl /scratch/dataset/train`: List directory details.

## Follow-up Actions
- Continue monitoring storage usage.
- Communicate storage policies and quotas to users.
- Regularly review and update quotas as needed.
---

### 2023040542000344_Re%3A%20Over%20quota%20on%20_home_hpc.md
# Ticket 2023040542000344

 # HPC Support Ticket: Over Quota on /home/hpc

## Keywords
- Quota exceeded
- Block quota
- Grace period
- Hidden folder
- Objaverse-api
- Custom path

## Summary
A user received an automated email alerting them that they had exceeded their block quota on the `/home/hpc` filesystem. The user attempted to delete files using the `rm -rf all` command but was unsuccessful.

## Root Cause
The majority of the user's data was located in a hidden folder (`.objaverse`) within their home directory. The user was unaware of how to properly manage or delete the data within this folder.

## Solution
An HPC Admin identified the location of the majority of the user's data and advised the user to configure their `objaverse-api` to use a custom path for storing the database. This would help the user manage their data more effectively and avoid exceeding their quota in the future.

## General Learnings
- Users may not be aware of hidden folders and files that consume significant storage space.
- Proper configuration of applications (e.g., `objaverse-api`) to use custom paths can help manage storage space more effectively.
- Users should be educated on how to check their quota usage and manage their data accordingly.
- HPC Admins can assist users in identifying and managing large amounts of data stored in hidden folders.
---

### 2021052142001538_Fw%3A%20Problems%20%26%20Disk%20quota%20exceeded%20titan.md
# Ticket 2021052142001538

 # HPC Support Ticket: Disk Quota Exceeded on Titan

## Keywords
- Disk quota exceeded
- Storage management
- Quota usage
- Data ownership
- `chown` command
- Group quota

## Summary
The user reported issues with editing and uploading files due to exceeded disk quota on the Titan HPC system. The root cause was identified as improper data ownership after moving files to a shared account.

## Root Cause
- The group's total disk quota was exceeded (102.5% usage).
- Data moved to the shared account (`gwgkfu0h`) was still counted under the original user's quota (`gwgi18`).

## Solution
- To change the ownership of the moved data, the original owner (`gwgi18`) needs to run the following command:
  ```bash
  chown --recursive gwgkfu0h /home/titan/gwgk/gwgkfu0h/ERA5
  ```
- Note that changing the ownership will not reduce the group's overall quota usage. The group needs to manage their storage more effectively or request a quota increase.

## Lessons Learned
- Moving data between accounts does not change the ownership automatically.
- The `chown` command must be used to change the ownership of moved data.
- Even after changing ownership, the group quota usage remains the same.
- Regularly monitor and manage storage usage to prevent quota exceedance.
- Communicate with the HPC Admins regarding storage needs and potential quota increases.
---

### 2023101242002317_Fehlermeldung%20%C3%A2%C2%80%C2%9EDisk%20quota%20exceeded%22%20auf%20%24HPCVAULT%2C%20obwohl%20soft%.md
# Ticket 2023101242002317

 # HPC Support Ticket: Disk Quota Exceeded on $HPCVAULT

## Keywords
- Disk quota exceeded
- Soft quota
- $HPCVAULT
- File copy error
- Temporary issue

## Problem Description
- User exceeded soft quota on $HPCVAULT for more than 7 days.
- User deleted data to comply with soft quota but still received "Disk quota exceeded" error when attempting to copy files.

## Root Cause
- The issue appeared to be temporary and specific to certain directories.

## Solution
- The problem resolved itself over time.
- HPC Admin was able to write a file under the user's ID without issues, indicating the problem was not persistent.

## Lessons Learned
- Temporary issues with disk quotas can occur even after compliance with soft quotas.
- Detailed descriptions of actions triggering the error are crucial for troubleshooting.
- Sometimes, waiting can resolve transient issues.

## Actions Taken
- HPC Admin attempted to replicate the issue by writing a file under the user's ID.
- User confirmed the problem resolved itself after some time.

## Follow-up
- If the issue persists, provide detailed steps to reproduce the error, including the specific subdirectory and host.

## Conclusion
- Transient issues with disk quotas can occur and may resolve on their own. Detailed error descriptions are essential for effective troubleshooting.
---

### 2024060542000768_Regarding%20%24HOME%20quota%20-%20dy94rovu%20_%20Ravi%20Ayyala.md
# Ticket 2024060542000768

 # HPC Support Ticket: Regarding $HOME Quota

## Keywords
- $HOME quota
- RRZE-home
- HPC account
- IDM account
- Group membership
- Special agreement

## Summary
A user employed at NHR but working at the chair of system simulation (LSS) requested an increase in their $HOME directory quota from 10 GB to 50 GB, as other employees at LSS typically have a 50 GB quota.

## Root Cause
- The user has two accounts: an HPC account (iwia052h) with a 50 GB quota and an IDM account (dy94rovu) with a 10 GB quota.
- The user's IDM account is not part of the groups (cs10_staff or cs10_guest) that have a special agreement for a 50 GB quota.

## Solution
- The user was advised to contact the IT support of the CS10 chair to request membership in one of the groups (cs10_staff or cs10_guest) that have the special agreement for a 50 GB quota.

## General Learnings
- FAU employees with a work contract receive a standard quota of 10 GB in their Linux home directory.
- Special agreements may exist for certain groups, such as cs10_staff and cs10_guest at CS10, which provide a quota of 50 GB.
- Users may need to request membership in these special groups to receive the increased quota.
- It's important to differentiate between different accounts (e.g., HPC account, IDM account) and their respective quotas.

## Related Commands
- `mmlsquota -u [username] --block-size=auto`: To check the quota of a user.
- `id [username]`: To check the group membership of a user.
---

### 2024102242004081_error%20logging%20in%20%5Biwi5222h%5D.md
# Ticket 2024102242004081

 ```markdown
# HPC Support Ticket: Error Logging In

## Subject
Error logging in [iwi5222h]

## Keywords
- Login issue
- Jupyter Notebook
- Disk quota exceeded
- Write error
- SSH
- Data management

## Problem Description
The user is unable to log in to the HPC cluster and access Jupyter Notebook. The issue started the previous morning.

## Root Cause
The user's disk quota in `/home/hpc` is exceeded, causing a write error when Jupyter tries to start a notebook.

## Diagnostic Information
- **Disk Quota Exceeded**:
  ```
  Path              Used     SoftQ    HardQ    Gracetime  Filec    FileQ    FiHaQ    FileGrace
  !!! /home/hpc          171.7G   104.9G   209.7G  -29694days     245K     500K   1,000K        N/A !!!
  ```
- **Large Directories**:
  ```
  856M    iwi5/iwi5222h/.vscode-server
  1.9G    iwi5/iwi522h/Gem_CAR
  3.7G    iwi5/iwi522h/data
  14G     iwi5/iwi522h/lstm_fixed_learning_rate1
  5.0G    iwi5/iwi522h/lstm_fixed_learning_rate2
  5.7G    iwi5/iwi522h/lstm_fixed_learning_rate3
  6.4G    iwi5/iwi522h/lstm_fixed_learning_rate4
  15G     iwi5/iwi522h/lstm_fixed_learning_rate5
  4.1G    iwi5/iwi522h/lstm_fixed_learning_rate6
  5.9G    iwi5/iwi522h/xlstm_fixed_learning_rate_configchange
  6.5G    iwi5/iwi522h/.cache
  14G     iwi5/iwi522h/.local
  19G     iwi5/iwi522h/.git
  63G     iwi5/iwi522h/from_zero
  ```

## Solution
- **HPC Admin Response**:
  - Inform the user about the disk quota exceeded issue.
  - Advise the user to SSH into the cluster frontend and move or delete some data.
  - Provide a link to the filesystem documentation for guidance on data management.

## General Learning
- **Disk Quota Management**: Regularly check and manage disk quotas to avoid write errors.
- **Data Management**: Move or delete unnecessary data to stay within allocated quotas.
- **SSH Access**: Use SSH to access the cluster frontend for managing files.

## References
- [FAU Filesystems Documentation](https://doc.nhr.fau.de/data/filesystems/)
```
---

### 2017021442001654_command%20quota%20delivers%20too%20few%20information.md
# Ticket 2017021442001654

 # HPC Support Ticket: Quota Command Issue

## Keywords
- `quota` command
- Connection refused
- Quota information
- Systemd
- wnfs1 update

## Problem Description
The user reported that the `quota` command was not providing sufficient information about disk usage and time left. The command returned errors indicating connection issues with specific servers.

## Root Cause
The `quotad` service was not automatically started after a wnfs1 update on 02/02.

## Solution
- The `quotad` service was manually restarted and enabled in systemd.
- The user was informed that the issue should be resolved and they should now see the quota information for `/home/woody`.

## General Learnings
- Ensure that necessary services (like `quotad`) are properly configured to start automatically after updates.
- Check systemd configurations to ensure services are enabled and running as expected.
- Communicate with users to confirm resolution of issues and provide updates on service status.

## Actions Taken
- HPC Admins restarted the `quotad` service and enabled it in systemd.
- The user was notified that the issue should be resolved and they should now see the quota information.

## Follow-up
- Monitor the `quotad` service to ensure it continues to run correctly.
- Verify that users are receiving the expected quota information.
---

### 2024072542004966_Request%20to%20Increase%20Quota%20-%20iwso110h.md
# Ticket 2024072542004966

 # HPC Support Ticket Conversation Analysis

## Keywords
- Quota Increase
- Work Partition
- Shared Directory
- Data Confidentiality
- POSIX Permissions
- Multi-User System
- Data Security

## Summary
A user requested an increase in quota on the Work partition for a large dataset. The HPC Admin suggested using a shared directory to prevent duplication and discussed data confidentiality and security measures.

## Root Cause of the Problem
- User needed additional storage space for a large dataset.
- Concerns about data confidentiality and security.

## Solution
- Use the shared directory `/home/janus/iwso-datasets` for data storage.
- Manage access to the data using POSIX permissions (e.g., set permissions to 700 or 600).
- Understand the general regulations and security measures of the HPC systems.

## General Learnings
- HPC systems are multi-user environments with shared directories to prevent data duplication.
- Data confidentiality can be managed through POSIX permissions.
- HPC systems have specific security measures and regulations that users should be aware of.
- Communication with the HPC Admin is crucial for understanding available resources and best practices.

## Additional Notes
- The shared directory was created upon request and can be managed by the user.
- The HPC systems are not designed for highly sensitive data due to their multi-user nature and security limitations.
- Regular maintenance and updates are performed to keep the systems secure.

## References
- General regulations and security measures of the HPC systems at NHR@FAU.
- POSIX permissions for managing file access.
---

### 2016052042000345_Zu%20wenig%20Speicher%20auf%20HPC.md
# Ticket 2016052042000345

 ```markdown
# HPC-Support Ticket: Insufficient Storage Space

## Keywords
- Storage Quota
- Fluid Dynamics Simulations
- Quota Limits
- Dateisystem /home/woody

## Problem Description
- User received an automatic notification about reaching quota limits on the `/home/woody` filesystem.
- User requires additional storage space for fluid dynamics simulations, each exceeding 2GB.
- Current quota: 25GB soft, 50GB hard.
- User requested an increase to 100GB until 30.07.

## Root Cause
- User's storage quota on `/home/woody` was insufficient for the volume of simulations being conducted.

## Solution
- HPC Admin increased the user's quota to 250GB soft and 500GB hard.

## Lessons Learned
- Users conducting large-scale simulations should regularly monitor their storage usage.
- Proactive communication with HPC Admins can help in timely quota adjustments.
- Automated notifications are crucial for users to manage their storage effectively.

## Actions Taken
- HPC Admin adjusted the user's quota limits to accommodate the increased storage needs.

## Follow-up
- Users should be reminded to clean up unnecessary files to avoid reaching quota limits.
- Regular reviews of storage usage patterns can help in better resource allocation.
```
---

### 42281751_Storage%20on%20LiMa.md
# Ticket 42281751

 # HPC Support Ticket Conversation: Storage on LiMa

## Keywords
- Disk quota exceeded
- LiMa
- Storage limits
- File systems
- Quota extension

## Summary
A user encountered job abortions due to "Disk quota exceeded" errors on LiMa. The user had a total disk usage of about 25 GB and was unsure about the maximum allowable disk usage.

## Root Cause
The user's job was aborted due to exceeding the disk quota on the `$FASTTMP` file system, which is used for temporary files.

## Solution
- **Home Directory Quota**: The standard home directory has a quota of 10 GB, which can be exceeded for up to 1 week and up to 20 GB. Quota extensions are not possible for this file system.
- **File System Usage**:
  - **$FASTTMP**: For strictly temporary files that live for only a few days.
  - **/home/woody/**: For small files.
  - **/home/vault/**: For large files.
- **Quota Extension**: The user was advised to request a quota extension for `$FASTTMP` if needed for simulations producing large amounts of data.

## Lessons Learned
- Always create new tickets for new problems instead of replying to old tickets.
- Understand the different file systems available and their intended uses.
- Be aware of the disk quotas for each file system and how to request extensions if necessary.

## References
- [HPC Environment File Systems](http://www.rrze.uni-erlangen.de/dienste/arbeiten-rechnen/hpc/systeme/hpc-environment.shtml#fs)
- [HPC Services](http://www.hpc.rrze.fau.de/)
---

### 2020091442001788_Re%3A%20%5BRRZE-HPC%5D%20new%20HPC%20storage%20system%20and%20shutdown%20of%20old%20compute%20nodes%.md
# Ticket 2020091442001788

 ```markdown
# HPC Support Ticket Conversation Analysis

## Keywords
- Scheduled downtime
- New HPC storage system
- Shutdown of old compute nodes
- Quota changes
- Samba access
- Hierarchical Storage Management (HSM)

## Summary
- **Scheduled Downtime**: All HPC systems at RRZE will have a scheduled downtime on Monday, September 21, starting at 07:30 and lasting the whole day.
- **New HPC Storage System**: A new storage system will replace the old one, which was bought in 2008. The new system will use IBM Spectrum Scale and will support similar features as the old system.
- **Quota Changes**:
  - $HOME quota increased from 10 GB to 50 GB.
  - $VAULT quota increased from 100 GB to 500 GB.
- **Samba Access**: The old system could be accessed through the SMB/CIFS protocol. This access will still be possible with the new system but will move to a new name: `\\fundus.rrze.uni-erlangen.de`.
- **Shutdown of Old Hardware**: Old compute nodes (tf00x and tf01x in TinyFat, w10xx nodes in Woody) will be shut down on September 21.

## Root Cause of the Problem
- User confusion about the scheduled downtime date (initially thought it was June 21 instead of September 21).

## Solution
- Clarification by the user that the correct date is September 21, as mentioned at the end of the email.

## General Learnings
- Always double-check dates and details in important announcements.
- Communicate clearly about upcoming changes and their impact on users.
- Provide detailed information about new systems and their features to help users transition smoothly.
```
---

### 2020102942000614_Re%3A%20Fwd%3A%20Fwd%3A%20Re%3A%20HPC-Storage-Angebot.md
# Ticket 2020102942000614

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Keywords
- HPC-Storage
- Rechtevergabe
- Hilfskräfte
- SSH-Key
- Quota
- File Quota
- Block Quota
- Backup
- Unix-Permissions
- ACLs
- cronjob
- chown
- chmod
- sticky/suid/sgid-Bit
- Zoom Meeting
- Vault
- Saturn
- Inode-Limit

## General Learnings
- **Rechtevergabe und Hilfskräfte**: Users can request a shared directory with group permissions and a helper user account for short-term employees.
- **Quota Management**: File quotas can be adjusted or removed based on user needs. Understanding the difference between block and file quotas is crucial.
- **Backup Considerations**: Vault has regular backups, which may affect performance with a high number of files.
- **Unix Permissions and ACLs**: Proper setting of Unix permissions and ACLs is essential for managing group access.
- **Cronjobs and File Ownership**: Regular cronjobs can be used to manage file ownership and permissions.
- **Communication**: Effective communication through Zoom meetings and email is important for resolving complex issues.

## Root Causes and Solutions
- **File Quota Exceeded**: User exceeded the file quota due to a large number of small files.
  - **Solution**: Increased the inode limit to accommodate more files.
- **Rechtevergabe**: Need for a shared directory with group permissions and a helper user account.
  - **Solution**: Created a shared directory with group permissions and a helper user account.
- **Backup Performance**: Concerns about backup performance with a high number of files.
  - **Solution**: Increased the inode limit and considered the impact on backups.
- **Unix Permissions**: Need for proper setting of Unix permissions and ACLs.
  - **Solution**: Provided guidance on setting Unix permissions and ACLs.
- **Cronjobs for File Management**: Need for regular cronjobs to manage file ownership and permissions.
  - **Solution**: Offered to set up cronjobs to manage file ownership and permissions.

## Documentation for Support Employees
- **File Quota Management**: Understand the difference between block and file quotas. Adjust or remove quotas based on user needs.
- **Shared Directories**: Create shared directories with group permissions for collaborative work.
- **Helper User Accounts**: Set up helper user accounts for short-term employees using SSH keys.
- **Backup Considerations**: Be aware of the impact of a high number of files on backup performance.
- **Unix Permissions and ACLs**: Provide guidance on setting Unix permissions and ACLs for group access.
- **Cronjobs**: Offer to set up cronjobs for managing file ownership and permissions.

## Additional Notes
- **Communication**: Use Zoom meetings and email for effective communication with users.
- **Documentation**: Keep detailed records of solutions for future reference.
```
---

### 2022110942001897_No%20space%20left%20on%20device%20error%20when%20submitting%20jobs.md
# Ticket 2022110942001897

 # HPC Support Ticket: No Space Left on Device Error When Submitting Jobs

## Keywords
- No space left on device
- sbatch job submission error
- /scratch directory full
- TinyGPU
- HPC job submission

## Problem Description
- User unable to submit jobs via `sbatch` on TinyGPU.
- Error message: `/bin/bash: cannot create temp file for here-document: No space left on device`
- User's quota appears fine, and they can create/copy files in their home directory.
- Multiple users experiencing the same issue.

## Root Cause
- The `/scratch` directory on the TinyGPU frontend was completely filled by another user.

## Solution
- HPC Admins cleaned up the `/scratch` directory.
- The problem was resolved after the cleanup.

## Lessons Learned
- Full `/scratch` directory can cause job submission failures even if user quotas are within limits.
- Regular monitoring and maintenance of shared directories like `/scratch` are essential to prevent such issues.
- Users should be aware of the impact of filling shared directories and adhere to usage policies.

## Actions Taken
- HPC Admins performed cleanup of the `/scratch` directory to resolve the issue.

## Follow-up
- Monitor `/scratch` directory usage to prevent future incidents.
- Educate users on proper usage of shared directories to avoid filling them up.
---

### 2018042042000905_Disk%20Quota%20on%20Emmy%27s%20FASTTMP.md
# Ticket 2018042042000905

 # HPC-Support Ticket: Disk Quota on FASTTMP

## Keywords
- Disk Quota
- FASTTMP
- Emmy Cluster
- Data Management
- User Space Allocation

## Summary
A user reported issues with disk quota on the Emmy cluster's FASTTMP, despite the RRZE's webpage indicating no quota. The user had recently deleted old files but still encountered problems.

## Root Cause
- Possible change in data management policies for FASTTMP.
- Potential discrepancy between actual quota enforcement and documented policies.

## Solution
- Verify current data management policies for FASTTMP.
- Confirm if there is a quota and, if so, the allocated space per user.
- Communicate the findings to the user and update documentation if necessary.

## General Learnings
- Regularly update documentation to reflect current policies.
- Ensure consistent communication regarding resource allocation and management.
- Address user concerns promptly to maintain trust and satisfaction.
---

### 2024022642004222_disk%20quota%20exceed.md
# Ticket 2024022642004222

 ```markdown
# HPC Support Ticket: Disk Quota Exceeded

## Keywords
- Disk Quota
- Downtime
- Maintenance
- Vault
- Gromacs
- Over Quota

## Problem Description
- User unable to generate data on vault.
- `shownicerquta.pl` indicates 8.4TB used out of 19.3TB soft quota.
- Newly generated files were 0 KB.

## Root Cause
- Downtime and maintenance of `$HPCVAULT` and `$HOME`.
- Users experienced bogus "over quota" messages after the downtime.

## Solution
- Issue identified and resolved by HPC Admins around 10:50 a.m.
- No further action required from the user.

## Lessons Learned
- Downtime and maintenance can cause temporary issues with disk quotas.
- Users should report any unusual behavior after maintenance periods.
- HPC Admins should monitor for and address "over quota" messages promptly.
```
---

### 2024031742000689_File%20quota%20reached%20aus%20unbekannten%20Gr%C3%83%C2%BCnden.md
# Ticket 2024031742000689

 # HPC Support Ticket: File Quota Exceeded

## Keywords
- File quota
- Inodes
- Home directory
- Quota report
- File count
- Directory count

## Summary
The user received daily emails indicating that they had exceeded their file quota on the `/home/hpc` filesystem. The user's quota report showed they had used 517,594 files out of a soft quota of 500,000 files. The user checked their home directory and found fewer than 500,000 files, but was informed that files owned by them in other users' home directories also count towards their quota.

## Root Cause
The user's file count command only counted files (`find "$i" -type f`), but the quota system counts both files and directories (inodes).

## Solution
The HPC Admin pointed out that the user should count both files and directories to get an accurate representation of their inode usage. The user's `.cache` directory alone contained over 80% of their inode quota.

## Steps to Resolve
1. **Count both files and directories**: Instead of just counting files with `find "$i" -type f`, the user should count all inodes with `find "$i" | wc -l`.
2. **Check other directories**: The user should also check for files they own in other users' home directories, as these also count towards their quota.

## General Lessons
- Both files and directories count towards the file quota (inode quota).
- Files owned by a user in other users' home directories count towards the user's quota.
- Accurate counting of inodes is essential to manage quota effectively.
---

### 2024090542000226_Schicken%20Gro%C3%83%C2%9Fer%20Datei.md
# Ticket 2024090542000226

 # HPC-Support Ticket: Schicken Großer Datei

## Keywords
- Large file transfer
- Simulation file
- Data link
- FAUBox
- Gigamove
- Lustre
- HPC-Data

## Problem
- User needs to send a 120GB simulation file to a software company due to a bug.
- Existing services (FAUBox, Gigamove) are insufficient for the file size.

## Root Cause
- Lack of a dedicated service for transferring large files.

## Solution
1. **Create a directory for sharing:**
   ```bash
   mkdir /home/saturn/iwpa/iwpa046h/sharing-sim
   ```

2. **Copy the file from Lustre to the new directory:**
   ```bash
   cp /lustre/b142dc/b142dc10/DFG_Free_Inflow_Radial_Fan_Sim/Final_Simulation/Export_test/9 /home/saturn/iwpa/iwpa046h/sharing-sim/
   ```

3. **Set permissions:**
   ```bash
   chmod o+x /home/saturn/iwpa/iwpa046h
   chmod -R o+rX /home/saturn/iwpa/iwpa046h/sharing-sim
   ```

4. **Provide the data link:**
   ```plaintext
   https://hpc-mover.rrze.uni-erlangen.de/HPC-Data/0x7b58aefb/d749a38a7424c704d0b8c4c64f1d0b9a/
   ```

## Additional Information
- The file should be accessible via the provided link.
- Further access restrictions can be configured if needed, as per the instructions at [HPC-Data Howto](https://hpc-mover.rrze.uni-erlangen.de/HPC-Data/howto.html).

## Outcome
- The user successfully transferred the file using the provided instructions.

## Lessons Learned
- For large file transfers, custom solutions may need to be implemented.
- Setting appropriate permissions and using specific directories can facilitate secure file sharing.
---

### 2019030442001748_AW%3A%20%24SATURNHOME%20_%20HPC-Basis-Storage%20mfh3%20-%20mfpp.md
# Ticket 2019030442001748

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Keywords
- Storage Options
- Purchase vs. Rental
- Costs
- Contract Duration
- Form Submission

## General Learnings
- **Storage Options**: The HPC site offers various storage options, including purchase and rental.
- **Costs**: Different costs are associated with different storage capacities and durations.
- **Contract Duration**: Contracts can have varying durations, with options for renewal or fixed terms.
- **Form Submission**: For certain options, users need to fill out and submit specific forms.

## Problem Root Cause
- The user needed clarification on storage options, costs, and contract durations.
- The user opted for the rental option and required guidance on the necessary form submission.

## Solution
- The HPC Admin provided detailed information on available storage options, including costs and contract durations.
- The user was instructed to fill out and submit a form for the rental option.
- The HPC Admin confirmed the receipt of the signed form and set the quota accordingly.

## Additional Notes
- The HPC Admin also mentioned that no backup is provided, only RAID6 for data protection.
- The user was informed about additional costs if the order is placed as a university clinic rather than a professorship.
```
---

### 2025021842003255_Re%3A%20anvme%20close%20to%20capacity%20limit.md
# Ticket 2025021842003255

 ```markdown
# HPC Support Ticket: anvme Close to Capacity Limit

## Keywords
- Workspace capacity
- Inodes
- File sizes
- Storage occupancy
- Data cleanup
- Workspace release
- Data recovery

## Summary
The HPC storage system `/anvme` is at > 90% occupancy, prompting users to clean up their workspaces. The user inquired about how workspace capacity is counted, whether by inodes or file sizes.

## Root Cause
- The storage system `/anvme` is running out of space, with 689TB out of 776TB currently in use.
- Users are notified to clean up their workspaces to free up space.

## Solution
- **Workspace Capacity Counting**: The workspace capacity is counted by inodes, with a quota of 5,000,000 inodes per user.
- **Data Cleanup**: Users are advised to remove duplicated data or data they no longer use.
- **Workspace Release**: Users can release their workspace using the command `ws_release <ID>`. Releasing a workspace makes the ID reusable and the directory inaccessible, but the data is kept for 14 days and can be recovered using the `ws_restore` command.

## Actions Taken
- The user was informed about the inode quota and the current storage occupancy.
- The user was advised to clean up their workspace to free up space.

## General Learnings
- Understanding the difference between inode quota and file size quota.
- Importance of regular data cleanup to prevent storage systems from reaching capacity limits.
- Procedures for releasing and recovering workspaces.
```
---

### 42220920_WG%3A%20Over%20quota%20on%20_home_vault.md
# Ticket 42220920

 ```markdown
# HPC-Support Ticket: Over Quota on /home/vault

## Keywords
- Quota
- /home/vault
- Molecular dynamics output
- Block quota
- Soft quota
- Hard quota
- Grace period
- Filesystem

## Problem
- User exceeded block quota on /home/vault.
- Soft quota: 504.9G
- Hard quota: 1009.7G
- Grace period: 6 days
- User requested quota increase for molecular dynamics output.

## Root Cause
- Insufficient storage space on /home/vault due to large molecular dynamics output files.

## Solution
- User requested quota increase.
- HPC Admin advised to use official contact addresses for initial inquiries.
- Quota increase request was processed.

## General Learnings
- Users should monitor their quota usage to avoid exceeding limits.
- Official contact addresses should be used for initial support requests.
- Quota increase requests can be made through the support team.
- Understanding the difference between soft and hard quotas, and the grace period is important.
```
---

### 2024060942001189_Slow%20storage_archive%20-%20Kainz%20-%20iwai%20_%20b143dc%20_%20b180dc.md
# Ticket 2024060942001189

 # HPC Support Ticket Conversation Analysis

## Keywords
- Slow storage/archive
- Quota management
- ACL (Access Control List)
- NFS4 ACL
- POSIX permissions
- Data ownership
- Group permissions
- Vault storage
- Replication
- Tape-Archiv
- HPC-Cafe
- rzwin home directories
- Cache configs
- Data transfer (rsync)
- Inode quota
- Archive storage

## General Learnings
- **Quota Management**: Quota on vault is account-bound, not path-bound. This can lead to issues where users exceed their quota despite having sufficient overall storage.
- **ACL Configuration**: Proper configuration of ACLs is crucial to ensure that only authorized users have access to specific directories. Misconfiguration can lead to security risks.
- **Data Ownership**: Ensuring that data ownership is clearly defined and managed is important for long-term data management and accessibility.
- **Replication**: Vault storage has replication, which means data is stored twice in the system and counted twice in the quota.
- **Tape-Archiv**: Consideration of tape storage for archiving older data to free up active storage space.
- **HPC-Cafe**: Regular meetings to discuss and decide on the best storage solutions for specific use cases.
- **rzwin Home Directories**: Possibility of increasing home directory sizes for core teams to manage cache configurations more effectively.

## Root Cause of the Problem
- **Quota Exceeded**: The user encountered issues with quota exceeded errors due to the quota being account-bound rather than path-bound.
- **ACL Misconfiguration**: Initial ACL settings allowed all HPC accounts to access and modify data, leading to potential security risks.
- **Data Ownership**: Lack of clear data ownership and management strategy led to inefficiencies in data handling and access.

## Solution
- **Quota Management**: Adjusted quota settings to ensure sufficient storage for the user's needs.
- **ACL Configuration**: Corrected ACL settings to restrict access to authorized groups and users only. Provided guidance on proper ACL configuration.
- **Data Ownership**: Discussed the importance of clear data ownership and management strategies. Suggested using a centralized approach for data management.
- **Replication Awareness**: Informed the user about the replication feature of vault storage and its impact on quota.
- **Tape-Archiv**: Suggested considering tape storage for archiving older data to free up active storage space.
- **HPC-Cafe**: Scheduled a meeting to discuss and decide on the best storage solutions for the user's specific use case.
- **rzwin Home Directories**: Considered the possibility of increasing home directory sizes for the core team to manage cache configurations more effectively.

## Documentation for Support Employees
For similar issues in the future, ensure that:
- Quota settings are properly configured to meet the user's needs.
- ACL settings are correctly configured to restrict access to authorized groups and users only.
- Data ownership and management strategies are clearly defined and communicated to the user.
- The user is aware of the replication feature of vault storage and its impact on quota.
- Tape storage is considered for archiving older data to free up active storage space.
- Regular meetings (HPC-Cafe) are scheduled to discuss and decide on the best storage solutions for specific use cases.
- The possibility of increasing home directory sizes for core teams is considered to manage cache configurations more effectively.
---

### 42002013_Bitte%20um%20mehr%20Scratch%20Space.md
# Ticket 42002013

 ```markdown
# HPC-Support Ticket: Request for More Scratch Space

## Keywords
- Scratch Space
- Benchmarks
- iDataPlex Westmere Nodes
- /tmp
- /scratch
- Performance Testing

## Problem Description
- User requires 300GB of local scratch space for benchmarking applications.
- Insufficient space on `/tmp`.
- No write access to `/scratch`.
- User needs local storage to avoid performance issues with parallel file systems.

## Root Cause
- Insufficient local storage space.
- Lack of write permissions on `/scratch`.

## Solution
- HPC Admin fixed the write access issue on `/scratch`.
- Provided 250GB of local scratch space, which was deemed sufficient by the user.

## Lessons Learned
- Ensure users have appropriate write permissions on designated scratch directories.
- Verify available local storage space on compute nodes to meet user requirements.
- Communicate hardware limitations (e.g., maximum available local storage) to users.

## Follow-up
- Monitor user feedback to ensure the provided solution meets their needs.
- Regularly review and update scratch space allocations based on user requirements and hardware capabilities.
```
---

### 2024082642003749_File%20Sharing_Server.md
# Ticket 2024082642003749

 # HPC Support Ticket: File Sharing/Server

## Keywords
- File Sharing
- Sparse Matrices
- Repository
- Zenodo
- GitHub
- Data Storage
- NHR@FAU

## Problem
- User wants to create a repository for sparse matrices from ML applications.
- Needs a solution to store and share these matrices with others inside and outside the group.
- Matrices are large (1-5 GB each) and the number of matrices is expected to be less than 20 initially.

## Discussion
- HPC Admin suggests various platforms:
  - **hpc-mover**: Not suitable for long-term stable service.
  - **Zenodo**: Recommended for datasets up to 50 GB, provides DOI for permanent access.
  - **GitHub**: Suitable for small datasets, can use GitHub Pages for a frontend.
  - **CDI & CRIS**: Not much progress in the last year.
  - **infovm9-4**: Not recommended.
- User confirms GitHub file size limit is too small, but Zenodo looks promising.

## Solution
- User decides to use **Zenodo** for publishing the datasets due to its 50 GB file size limit and permanent DOI feature.

## General Learnings
- Zenodo is a suitable platform for sharing large datasets with permanent access.
- GitHub is limited by file size but can be used for smaller datasets.
- hpc-mover and infovm9-4 are not recommended for long-term stable data sharing.
- Always consider the size and stability of the data when choosing a sharing platform.
---

### 2024070142003485_Emergency%20help%20needed%20for%20the%20storage.md
# Ticket 2024070142003485

 ```markdown
# Storage Quota Issue Resolution

## Keywords
- Storage quota
- $HOME
- $WORK
- $HPCVAULT
- Filesystems
- Data transfer

## Problem Description
- User received a notification about exceeding storage quota.
- User was only using $HOME for all data, leading to quota issues.
- User had a single job running and claimed no other files were stored.

## Root Cause
- Misuse of $HOME directory for all data storage, leading to quota exceedance.

## Solution
- **HPC Admin** suggested moving data to $WORK and/or $HPCVAULT.
- Provided a link to documentation explaining different storage spaces: [Filesystems Documentation](https://doc.nhr.fau.de/data/filesystems).

## Outcome
- User acknowledged the suggestion and agreed to transfer data to the recommended storage spaces.
- Ticket was closed after user confirmation.

## General Learning
- Users should be aware of different storage spaces available and their appropriate use cases.
- Regularly monitor storage usage to avoid quota issues.
- Refer to documentation for detailed information on storage management.
```
---

### 2024062742001191_Quota%20reached.md
# Ticket 2024062742001191

 # HPC-Support Ticket: Quota Reached

## Keywords
- Quota
- Soft quota
- Hard quota
- Grace period
- File system
- Home directory
- Running jobs
- Space management

## Summary
A user received an email notification about reaching the soft quota on the `/home/woody` file system. Despite freeing up space, the user's running jobs were unable to save files in the directory.

## Root Cause
- The user had reached the soft quota limit of 1000 GB on the `/home/woody` file system.
- The user freed up space but encountered issues with running jobs saving files, which was later identified as an unrelated mistake.

## Solution
- The HPC Admin confirmed that deletions are immediately accounted for by the quota system, with no delay.
- The user was advised to check the quota using `shownicerquota.pl` or `quota -s`.
- The user confirmed that the issue was due to an unrelated mistake and that the quota system was functioning correctly.

## Lessons Learned
- Deletions are immediately reflected in the quota system.
- Users can check their quota using specific commands.
- Running jobs may fill up freed space quickly, so continuous monitoring is necessary.
- Users should verify other potential issues if quota management seems correct.

## References
- [Quota Documentation](https://doc.nhr.fau.de/data/filesystems/#quotas)

## Roles
- **HPC Admins**: Provided guidance on quota management and confirmed system functionality.
- **User**: Reported the issue and confirmed resolution after identifying an unrelated mistake.

## Conclusion
The issue was resolved by confirming the immediate reflection of deletions in the quota system and identifying an unrelated mistake by the user. Continuous monitoring and proper space management are crucial for avoiding quota-related issues.
---

### 2022112242001102__scratch%20auf%20tinyx%20schon%20wieder%20komplett%20voll.md
# Ticket 2022112242001102

 # HPC Support Ticket: /scratch Space Full on tinyx

## Keywords
- /scratch space full
- tinyx
- ML-Trainingsdaten
- ImageNet
- new students
- du -xahd
- sort -hr
- head -n 1

## Problem
The `/scratch` directory on the `tinyx` system was full again after a few days of relief. A user reported that they had to delete some of their files to allow others to continue working. The main culprit was identified as a large dataset (130G) located in `/scratch/data/ILSVRC`, which appeared to be ML training data.

## Root Cause
- Large dataset (130G) stored in `/scratch/data/ILSVRC` by a new student account (active for less than 14 days).
- New students were not informed about the central location for large datasets like ImageNet.

## Solution
- HPC Admin acknowledged the issue and confirmed that space was freed on `tinyx:/scratch`.
- Need to ensure new students are informed about the proper storage locations for large datasets.

## Lessons Learned
- Regular monitoring of `/scratch` space usage is essential.
- New users should be properly onboarded and informed about storage policies and best practices.
- Large datasets should be stored in designated central locations to avoid filling up shared scratch space.

## Commands Used
- `du -xahd 1 /scratch/* | sort -hr | head -n 1`: To identify the largest files/directories in `/scratch`.
- `ls -adl /scratch/data/ILSVRC`: To check the details of the directory containing the large dataset.

## Follow-up Actions
- Ensure new users are informed about storage policies.
- Regularly check and clean up `/scratch` space to prevent it from filling up.
---

### 42031717_iwst16%3A%20Soft%20Quota-Limits%20auf%20_home_cluster32%20erreicht%21.md
# Ticket 42031717

 # HPC Support Ticket: Soft Quota-Limits Reached on /home/cluster32

## Keywords
- Soft Quota
- Hard Quota
- Disk Space
- Simulations
- Quota Increase
- HPC Storage System

## Problem
- **Root Cause**: User reached soft quota limit on `/home/cluster32`.
- **Details**: User's simulations required more disk space than the allocated soft quota of 75GB.

## Conversation Summary
- **User Request**: Asked for an increase in disk space due to expected high usage from simulations.
- **HPC Admin Response**: Initially increased quota from 75GB to 1TB, then corrected to 75GB to 100GB. Also provided access to a new HPC storage system with a 500GB quota.

## Solution
- **Immediate Action**: Increased soft quota from 75GB to 100GB.
- **Additional Support**: Provided access to a new storage directory `/home/vault/iwst/iwst16` with a 500GB quota.

## General Learnings
- **Quota Management**: Importance of correctly setting and managing user quotas.
- **Communication**: Clear communication between users and admins regarding resource needs.
- **Storage Solutions**: Utilizing additional storage systems to meet high demand.

## Next Steps
- **Follow-up**: Discuss further details and long-term storage solutions with the user.
- **Monitoring**: Continue monitoring user's disk usage to prevent future quota issues.

---

This documentation can be used as a reference for handling similar quota-related issues in the future.
---

### 2023121542000024_SoftQ%20auf%20woody%20_%20%24WORK.md
# Ticket 2023121542000024

 ```markdown
# HPC-Support Ticket: Soft Quota Increase on Woody / $WORK

## Keywords
- Soft quota
- Hard quota
- Woody
- $WORK
- FEP-Rechnungen
- Vault
- File quota

## Summary
A user requested an increase in the soft quota and hard quota on the Woody system under the $WORK directory to accommodate a large number of FEP calculations over the weekend.

## Root Cause
- The user anticipated exceeding the current hard quota due to the volume of FEP calculations.
- The user needed to submit calculations on Woody to avoid exceeding the file quota on Vault.

## Solution
- The HPC Admin increased the soft quota to 1 TB and the hard quota to 2 TB on Woody / $WORK.

## Lessons Learned
- Users may require temporary quota increases for large computational tasks.
- Proper communication and timely adjustments by HPC Admins can prevent disruptions in user workflows.
- Users should plan to transfer only necessary results to other storage systems to manage quota usage efficiently.
```
---

### 2021021042001653_Re%3A%20Over%20quota%20on%20_home_vault.md
# Ticket 2021021042001653

 # HPC Support Ticket: Over Quota on /home/vault

## Keywords
- Quota
- /home/vault
- Shared folder
- Tape archive

## Problem
- User exceeded their block quota on the /home/vault filesystem.
- User's personal data is around 30GB, but the shared folder /home/vault/capm/shared contains approximately 1.2TB of data.
- User inherited the shared folder due to their role as an HPC admin.

## Quota Report
- Blocks used: 901.2G
- Blocks quota soft: 524.3G
- Blocks quota hard: 1048.6G
- Blocks grace remaining: 5 days

## Root Cause
- The majority of the data usage comes from the shared folder, which the user inherited as an HPC admin.

## Solution
- HPC Admin increased the user's vault quota to 2TB.
- Suggested moving inactive data from the shared folder to the tape archive to free up space.

## General Learnings
- Users may inherit large shared folders due to their roles, which can lead to quota issues.
- Inactive data can be moved to the tape archive to manage quota limits.
- HPC Admins can adjust quotas to accommodate user needs.

## Related Links
- [FAU Data Archive Application](https://hpc.fau.de/antrag-auf-fau-datenarchiv/)
---

### 2019012342001993_Erh%C3%83%C2%B6hung%20Quota.md
# Ticket 2019012342001993

 # HPC Support Ticket Conversation Analysis

## Keywords
- Quota Increase
- DESY nanoCT Imaging
- Data Transfer
- Collaboration
- FAUBox
- Saturn Storage
- External Access

## Summary
- **User Issue**: User's raw data from DESY nanoCT imaging exceeds their current quota.
- **Request**: Increase in quota to facilitate data handling without frequent transfers.
- **Solution**: HPC Admin increased the user's quota on `/home/vault` to 800 GB soft / 1600 GB hard.

## Detailed Analysis
- **Root Cause**: User's data size (600 GB) exceeds their current soft quota (555 GB).
- **User Request**: Doubling of quota to handle large datasets and avoid frequent data transfers.
- **HPC Admin Response**:
  - Increased quota on `/home/vault` to 800 GB soft / 1600 GB hard.
  - Clarified that group storage on `/home/saturn` is managed within the group.
- **Additional User Questions**:
  - Cost of additional Saturn storage.
  - Methods to share data with external collaborators.
- **HPC Admin Clarifications**:
  - Confirmed cost of 25 TB Saturn storage for 5 years.
  - Suggested creating a separate ticket for external data access.

## Learnings
- **Quota Management**: Users may request quota increases for handling large datasets.
- **Storage Costs**: Understanding the cost structure for additional storage.
- **External Collaboration**: Need for methods to share data with external collaborators.
- **Ticket Management**: Separate tickets for different issues to streamline support processes.

## Action Items
- **User**:
  - Verify if additional storage is needed and discuss with group leaders.
  - Create a separate ticket for external data access if needed.
- **HPC Admin**:
  - Monitor quota usage and adjust as necessary.
  - Provide guidance on external data sharing methods.

## Conclusion
Effective communication and quota management are crucial for handling large datasets. Separate tickets for different issues help in efficient resolution. Understanding storage costs and external collaboration methods is beneficial for users.
---

### 2023122142001753_Speichererweiterung%20Tinyfat%20-%20mpet007h.md
# Ticket 2023122142001753

 # HPC Support Ticket: Storage Quota Increase Request

## Keywords
- Storage Quota
- Tinyfat Cluster
- Scratch SSD
- SLURM Job
- Acknowledgment
- Verlängerungsantrag

## Problem
- User's computation consists of two complementary codes that exchange data through files.
- Large data volumes (up to 500GB/job) quickly exceed the current storage quota (50GB).
- User requests a directory with approximately 20TB of storage on the Tinyfat cluster to run multiple jobs in parallel.

## Solution
- **Storage Quota Increase**: HPC Admin increased the user's quota under `$HPCVAULT` to 4TB.
- **Local SSD Usage**: HPC Admin suggested using local SSDs available on Tinyfat nodes under `/scratchssd` for data exchange within the same SLURM job.
- **Quota Verification**: The `shownicerquota.pl` script may not accurately display quotas above 4TB. The system will not send reminder emails if the quota is within limits.
- **Acknowledgment**: User was reminded to acknowledge HPC usage in their paper.

## General Learnings
- Large storage requests (e.g., 20TB) may not be granted without additional justification.
- Local SSDs on compute nodes can be used for temporary data storage during job execution.
- Quota verification tools may have limitations in displaying large quotas.
- Always acknowledge HPC resources in publications.

## Follow-up
- User submitted a Verlängerungsantrag (extension request) for account renewal.
- HPC Admin confirmed the account extension and provided additional details on local SSD usage.

This documentation can help support employees address similar storage quota increase requests and guide users on utilizing local SSDs for temporary data storage.
---

### 2024022242001572_Space%20to%20store%20experimental%20results%20Fw%3A%20Over%20quota%20on%20_home_hpc.md
# Ticket 2024022242001572

 # HPC Support Ticket: Space to Store Experimental Results

## Keywords
- Quota Exceeded
- /home/hpc
- Block Quota
- Soft Quota
- Hard Quota
- Grace Period
- Experimental Results

## Summary
A user received an automated email indicating that they have exceeded their block quota on the `/home/hpc` filesystem. The user is confused about where to store experimental results.

## Root Cause
- User exceeded the soft quota of 104.9G on the `/home/hpc` filesystem.
- Current usage is 118.9G.
- Grace period of 4 days remaining before reaching the hard limit of 209.7G.

## Solution
- **Immediate Action**: User needs to reduce their data usage below the soft quota of 104.9G to avoid reaching the hard limit or the end of the grace period.
- **Long-term Action**: Consider alternative storage solutions for experimental results, such as project-specific storage or archival systems.

## General Learnings
- Users should be aware of their storage quotas and the consequences of exceeding them.
- Regularly monitor and manage data usage to stay within allocated quotas.
- Understand the difference between soft and hard quotas, as well as the grace period.
- Investigate alternative storage options for large datasets or experimental results.

## Follow-up Actions
- HPC Admins or 2nd Level Support team may need to assist the user in finding suitable storage solutions.
- Provide guidance on best practices for data management and storage.
---

### 2023032742002811_HPC%20Quota.md
# Ticket 2023032742002811

 # HPC Quota Check

## Keywords
- HPC Quota
- Home Directory
- Quota Checker
- `shownicerquota.pl`
- `quota -s`

## Problem
- User received an email from HPC Quota Checker to free up space in the home directory.
- User needs to verify if they are below the specified quota limit after deleting files.

## Solution
- Use the command `shownicerquota.pl` or `quota -s` to check the current quota usage.

## General Learnings
- Users can check their quota usage using specific commands provided by the HPC system.
- It is important to regularly monitor and manage storage usage to avoid quota-related issues.

## Roles Involved
- HPC Admins
- 2nd Level Support Team

## Tools and Commands
- `shownicerquota.pl`
- `quota -s`

## Additional Notes
- Regularly checking quota usage helps in preventing storage-related issues and ensures compliance with HPC policies.
---

### 42084511_HPC-Account.md
# Ticket 42084511

 # HPC-Account Support Ticket Conversation

## Keywords
- HPC Account
- Storage Quota
- Password Setup
- Strömungsmechanik
- Simulation

## Summary
- **User Request**: Increase storage quota from 10GB to 500GB for running flow simulations.
- **HPC Admin Response**: Storage quota increased to 500GB on `/home/woody`.

## Detailed Information
- **Initial Setup**: HPC Admin created an HPC account (`iwst146`) for the user.
- **User Action Required**: User needs to set a password for the new account via the provided link.
- **Storage Request**: User requested an increase in storage quota for flow simulations.
- **Admin Action**: HPC Admin increased the storage quota to 500GB on `/home/woody`.

## Root Cause
- User required additional storage space for flow simulations.

## Solution
- HPC Admin increased the storage quota to 500GB on `/home/woody`.

## Notes
- The increased storage quota is not a standard size but an accommodation by the HPC team.
- User should specify the location where the storage is needed in future requests.

## References
- [IDM Password Setup](http://www.idm.uni-erlangen.de)
- [RRZE Website](http://www.rrze.uni-erlangen.de)
- [HPC Services](http://www.hpc.rrze.uni-erlangen.de/)
---

### 2024121842003229_HPC%20%24WORK%20directory%20not%20accessiable.md
# Ticket 2024121842003229

 # HPC Support Ticket: $WORK Directory Not Accessible

## Keywords
- $WORK directory
- Conda environment
- Disk quota exceeded
- Inodes limit
- Write permissions

## Problem Description
The user is unable to create a new Conda environment in the $WORK directory due to a "NotWritableError." The user has exceeded the disk quota for the project, specifically the inodes limit.

## Root Cause
- The project has a limit of 10 million inodes (files and directories) on the $WORK directory.
- The major offender within the project is occupying almost 9 million inodes, causing the quota to be exceeded.

## Symptoms
- `conda create` command fails with a "NotWritableError."
- `mkdir` command fails with "Disk quota exceeded."
- `df -h $WORK` shows available space but does not account for the inodes limit.

## Solution
- The user needs to address the issue within the project by reducing the number of inodes used.
- Specific documentation is available at [HPC Data Documentation](https://doc.nhr.fau.de/data/datasets/).

## Additional Information
- The HPC Admins have addressed this topic in several HPC Cafes.
- The user should refer to the provided documentation for further guidance on managing data and inodes.

## Relevant Commands
- `echo $WORK`
- `conda create -n playground python`
- `mkdir dir`
- `df -h $WORK`
- `conda info`

## Conclusion
The issue is caused by exceeding the inodes limit for the project. The user needs to manage the project's data to stay within the allocated inodes limit.
---

### 2023062142002166_Quota%20warning%20query%20-%20iwi5087h.md
# Ticket 2023062142002166

 # HPC Support Ticket: Quota Warning Query

## Keywords
- Quota
- Hard Quota
- Soft Quota
- Permission Denied
- File Deletion
- Shared File System
- Data Management Strategy

## Problem Description
- User received a warning about exceeding the soft quota on the HPC system.
- User was unable to access the account due to a "permission denied" message.
- User had reached the hard quota on `$Work` (also known as `/home/woody`).

## Root Cause
- The user had exceeded the hard quota of 750GB on `$Work`.
- The user was storing 12,757,167 files, which is harmful to a shared file system.

## Solution
- HPC Admins informed the user about the quota limits and the impact of storing a large number of files.
- The user was advised to delete unused files or move them to `$vault`.
- HPC Admins deleted the specified directory to free up space and allow the user to write to `$Work` again.

## Lessons Learned
- Users should be aware of their quota limits and the impact of storing a large number of files on a shared file system.
- Regularly deleting unused files or moving them to `$vault` can help prevent quota-related issues.
- HPC Admins can assist users in deleting files if necessary.
- Improving data management strategies can speed up computing and prevent quota-related issues.

## References
- [HPC Café: File Systems](https://hpc.fau.de/files/2022/01/2022-01-11-hpc-cafe-file-systems.pdf)
---

### 2023092842001765_Re%3A%20gwpa005h%3A%20Soft%20Quota-Limits%20auf%20_home_woody%20erreicht%21.md
# Ticket 2023092842001765

 ```markdown
# HPC-Support Ticket: Soft Quota-Limits auf /home/woody erreicht!

## Keywords
- Soft Quota
- Hard Quota
- Speicherplatz
- Dateisystem
- Quota-Limits
- HPC-Support

## Problem
- User hat die Soft-Quota auf /home/woody überschritten.
- Verbleibende Zeit bis zum Erreichen der Hard-Quota: 2 Stunden.
- User kann nicht rechtzeitig Platz schaffen.

## Root Cause
- User hat die Soft-Quota von 1950 GB überschritten und benötigt mehr Zeit, um Dateien zu bereinigen.

## Solution
- HPC Admin hat die Quota auf /home/woody angehoben, um dem User mehr Zeit zu geben, Dateien zu bereinigen.

## What Can Be Learned
- Users should be aware of their quota limits and manage their storage space accordingly.
- If a user exceeds their soft quota, they should immediately take action to free up space.
- HPC Admins can temporarily increase quotas to give users more time to manage their storage.

## Actions Taken
- HPC Admin hat die Quota auf /home/woody angehoben.
- User hat sich für die Hilfe bedankt.

## Status
- Ticket geschlossen.
```
---

### 2023080142004475_Fehlermeldung%20Quota.md
# Ticket 2023080142004475

 ```markdown
# HPC-Support Ticket: Fehlermeldung Quota

## Keywords
- Login issue
- Quota command timeout
- Incomplete quota data
- `shownicerquota.pl` script

## Summary
A user reported receiving an error message upon logging into the HPC system, indicating a timeout running the quota command, resulting in incomplete quota data.

## Root Cause
The error message suggests that the `shownicerquota.pl` script is timing out when attempting to retrieve quota information.

## Solution
No solution was provided in the initial ticket. Further investigation is required to determine the cause of the timeout and resolve the issue.

## Next Steps
- HPC Admins should investigate the `shownicerquota.pl` script to identify why it is timing out.
- Check system logs for any related errors or performance issues.
- Ensure that the quota system is functioning correctly and is not overloaded.
- If necessary, increase the timeout value or optimize the script for better performance.

## Notes
- The issue occurs regardless of the user account (`sles000h` or `b105dc11`).
- The error message is consistent and appears upon login.
```
---

### 2018030542000543_Vault%20Dateianzahlbegrenzgung.md
# Ticket 2018030542000543

 # HPC Support Ticket: Vault Dateianzahlbegrenzung

## Keywords
- Vault
- Dateianzahlbegrenzung
- Dateimengen
- LXFS (LIMA)
- Automatisches Entfernen

## Problem
- **Root Cause:** User requires temporary increase in file limit on Vault to process large datasets.
- **Details:** Current limit is 100,000 files. User needs approximately 1,000,000 files to process a single package containing ~50,000 files.

## Solution
- **Request:** Temporary increase in file limit on Vault.
- **Alternative:** Use LXFS (LIMA) for storage, but concerns about automatic removal of files.

## General Learnings
- **File Limits:** Understand the file limits on different storage systems (Vault, LXFS).
- **Temporary Adjustments:** Consider temporary adjustments to file limits for large processing tasks.
- **Alternative Storage:** Use alternative storage solutions like LXFS, but be aware of automatic file removal policies.

## Next Steps
- **HPC Admins:** Evaluate the feasibility of temporarily increasing the file limit on Vault.
- **User:** Await response from HPC Admins or consider using LXFS with caution regarding automatic file removal.

## Notes
- **User Concerns:** Automatic file removal on LXFS.
- **Storage Systems:** Vault vs. LXFS for large file processing tasks.
---

### 2020111642003778_Bitte%20um%20Freischaltung%20HPC%20Mover.md
# Ticket 2020111642003778

 # HPC Support Ticket Conversation Analysis

## Keywords
- HPC Mover
- .htaccess
- .htpasswd
- 403 Forbidden
- 404 Not Found
- Webserver permissions
- Symlinks
- Quota
- Directory listing
- Internal Server Error

## General Learnings
- **Quota Management**: Home directories have limited quota, and users should use `/home/vault` for larger data.
- **Webserver Permissions**: Directories must be executable for the webserver to access them.
- **.htaccess and .htpasswd**: Proper permissions and paths are crucial for these files to function correctly.
- **Symlinks**: Symlinks must point to directories accessible by the webserver.
- **Error Messages**: Understanding the difference between 403 Forbidden and 404 Not Found is important for troubleshooting.
- **Security**: Default permissions are set to deny for security reasons.

## Root Causes and Solutions

### Issue 1: Directory Permissions
- **Root Cause**: Directory `/home/vault/sles/sles000h/` had permissions set to 700, making it inaccessible to the webserver.
- **Solution**: Change directory permissions to be executable by the webserver.

### Issue 2: .htaccess Not Read
- **Root Cause**: Incorrect permissions or path for .htaccess or .htpasswd files.
- **Solution**: Ensure .htaccess and .htpasswd files have the correct permissions and paths.

### Issue 3: Symlinks Not Working
- **Root Cause**: Symlinks pointing to `/home/hpc/`, which the webserver cannot access.
- **Solution**: Ensure symlinks point to directories within `/home/vault` or `/home/saturn`.

### Issue 4: Internal Server Error with htpasswd
- **Root Cause**: htpasswd command changes file permissions, leading to Internal Server Error.
- **Solution**: Use an updated version of htpasswd that does not change file permissions.

### Issue 5: Quota Usage
- **Root Cause**: Data replication counts towards quota usage twice.
- **Solution**: Temporarily double quotas to accommodate for replication.

### Issue 6: Directory Listing
- **Root Cause**: index.html is disabled to display the header/footer.
- **Solution**: Understand that directory listing is intentionally disabled to display custom headers/footers.

## Documentation for Support Employees
- **Quota Management**: Advise users to use `/home/vault` for larger data due to quota limitations in home directories.
- **Webserver Permissions**: Ensure directories are executable for the webserver to access them.
- **.htaccess and .htpasswd**: Verify permissions and paths for these files to function correctly.
- **Symlinks**: Ensure symlinks point to directories accessible by the webserver.
- **Error Messages**: Differentiate between 403 Forbidden and 404 Not Found for effective troubleshooting.
- **Security**: Understand that default permissions are set to deny for security reasons.

This analysis provides a concise overview of common issues and their solutions, serving as a helpful reference for support employees.
---

### 2024060542001007_request%3A%20tier3%20basic%20supply%20project%20%28RRZE%20customer%20number%20wsv2000%29.md
# Ticket 2024060542001007

 ```markdown
# HPC Support Ticket: Tier3 Basic Supply Project Request

## Keywords
- Tier3 Basic Supply Project
- RRZE Customer Number
- Project Team
- Data Storage
- R
- Stata
- HPC Portal
- Jupyterhub
- Quota

## Summary
A user requests the setup of a Tier3 basic supply project with specific data storage requirements and software needs.

## Problem
- User needs a Tier3 basic supply project setup.
- Project team members need to be assigned manager rights in the HPC portal.
- Data storage requirement is 1500 GB.
- Software needs include R and possibly Stata.

## Solution
- HPC Admin clarifies the need for project team members to log in to the HPC portal before assigning manager rights.
- Recommends "Woody" for R and mentions an experimental RStudio service through Jupyterhub.
- Informs the user about the default quota per account in $WORK being 1 TB.

## Lessons Learned
- Ensure project team members log in to the HPC portal before assigning manager rights.
- Recommend appropriate resources for software needs, such as "Woody" for R and Jupyterhub for RStudio.
- Inform users about default storage quotas.
```
---

### 2023060942002091_Additional%20space%20for%20backups%20-%20b159cb11.md
# Ticket 2023060942002091

 # HPC Support Ticket: Additional Space for Backups

## Keywords
- Quota Extension
- Backup Storage
- $HPCVAULT
- $FASTTMP
- Simulation Data
- Long-term Storage

## Summary
A user requested additional backup space for simulation data that exceeded their current quota on $HPCVAULT. The user needed to back up intermediate snapshots of turbulent fields for further postprocessing and long-term storage.

## Root Cause
- User's quota on $HPCVAULT was insufficient to back up the full simulation data (7.6TB).
- No tape storage was available for the project.

## Solution
- HPC Admins increased the user's quota on $HPCVAULT to 15TB.

## What Can Be Learned
- Users may require quota extensions for large simulation data backups.
- HPC Admins can adjust quotas to accommodate user needs.
- Communication with HPC Admins is essential for managing storage requirements.
- Long-term storage solutions may need to be considered for large datasets.
---

### 2023111542000562_Question%20Regarding%20Over%20Quota%20on%20the%20Filesystem.md
# Ticket 2023111542000562

 # HPC Support Ticket: Over Quota on the Filesystem

## Keywords
- Over quota
- Filesystem
- /home/hpc
- File transfer
- Large data
- Model training
- $WORK filesystem
- Archiving files

## Problem
- User received an email indicating they are over quota on the `/home/hpc` filesystem.
- The issue likely occurred due to a failed file transfer attempt that partially transferred files.

## Root Cause
- Attempted transfer of a large number of images to `/home/hpc`, which is not suitable for storing large datasets or numerous small files.

## Solution
- **File Removal:**
  - Log into the cluster frontend via SSH.
  - Navigate to the path where the files were copied.
  - Remove the files manually using the `rm` command.

- **Alternative Storage:**
  - Use the `$WORK` filesystem, which has a 500 GB quota, for storing training data and large files.
  - More details on available filesystems can be found [here](https://hpc.fau.de/systems-services/documentation-instructions/hpc-storage/).

- **File Archiving:**
  - Use archives (tar or zip) to pack files together for easier transfer and reduced strain on the filesystem.
  - This can also potentially speed up model training.
  - Instructions on using archives in training can be found [here](https://hpc.fau.de/files/2022/01/2022-01-11-hpc-cafe-file-systems.pdf) and in this [recording](https://www.fau.tv/clip/id/40199).

## General Learning
- **Filesystem Usage:**
  - `/home/hpc` should not be used for large datasets or numerous small files.
  - Use appropriate filesystems like `$WORK` for such purposes.

- **File Management:**
  - Archiving files can make transferring and managing large datasets easier and more efficient.
  - Proper file management practices can help avoid quota issues and improve system performance.
---

### 42243071_Anfrage%20nach%20Erweiterung%20des%20Speicherplatzes%20f%C3%83%C2%BCr%20das%20Konto%20bclc03%20auf%2.md
# Ticket 42243071

 # HPC Support Ticket: Request for Storage Extension

## Keywords
- Storage extension
- Grace limit
- Home directory
- Vault directory
- Molecular modeling
- Trajectory files
- Checkpoints
- $FASTTMP

## Problem
- User requires additional storage space for molecular modeling calculations.
- Current storage limits in "home" and "vault" directories are insufficient.
- Large trajectory files are causing jobs to be halted due to exceeding the grace limit.

## User Request
- Increase grace limit in "home" directory to 40-50 GB (regular storage to 20-30 GB).
- Increase storage in "vault" directory to 1 TB (regular storage to 500 GB).

## HPC Admin Response
- Storage extension in "home" directory is not possible due to frequent snapshots.
- Storage in "vault" directory has been increased as requested.
- Suggested using $FASTTMP for temporary files with short lifespans.

## Solution
- Use "vault" directory for extended storage needs.
- Utilize $FASTTMP for temporary files to avoid exceeding storage limits in "home" and "vault" directories.

## Additional Information
- Documentation on available filesystems: [HPC Environment Filesystems](http://www.rrze.uni-erlangen.de/dienste/arbeiten-rechnen/hpc/systeme/hpc-environment.shtml#fs)

## Root Cause
- Insufficient storage space for large trajectory files generated during molecular modeling calculations.

## Lessons Learned
- Understand the purpose and limitations of different storage directories.
- Use appropriate directories for different types of data to optimize storage usage.
- Refer to documentation for detailed information on available filesystems and their usage.
---

### 2025021042005053_Need%20More%20HPC%20Storage.md
# Ticket 2025021042005053

 ```markdown
# HPC Support Ticket: Need More HPC Storage

## Summary
- **User Request:** Increase storage quota to 200 GB until the end of February.
- **HPC Admin Response:** Quota increase for `/home/hpc` is not offered. User has 1TB quota available at `/home/vault` and `/home/woody`, both almost unused.
- **Resolution:** User advised to move data to available storage locations.

## Keywords
- Storage quota
- /home/hpc
- /home/vault
- /home/woody
- Data management

## Root Cause
- User requested additional storage quota for `/home/hpc`.

## Solution
- HPC Admins informed the user that quota increase for `/home/hpc` is not offered.
- User advised to utilize available 1TB quota at `/home/vault` and `/home/woody`.
- User acknowledged the information and agreed to move data.

## Additional Information
- [HPC Storage Systems Documentation](https://doc.nhr.fau.de/data/filesystems)

## Ticket Closure
- **Question:** I need more storage space. Can you please increase my quota at `/home/hpc`?
- **Answer:** We do not offer quota increase for `/home/hpc`, but we can offer you more space at `$WORK` or `$HPCVAULT`.
```
---

### 2022031842001975_Speichernutzung%20auf%20Emmy.md
# Ticket 2022031842001975

 # HPC Support Ticket: Storage Usage on Emmy

## Keywords
- Storage usage
- $FASTTMP
- Quota
- File system overload
- Write permissions

## Summary
A user was consuming an excessive amount of storage on the $FASTTMP file system, leading to potential system overload.

## Root Cause
- The user was utilizing over 140 TB out of 400 TB available on $FASTTMP.
- The storage usage was increasing rapidly, with an additional 300 GB used in the last 15 minutes.

## Impact
- The user's storage consumption was 35% of the total capacity, affecting other users.
- At the current rate, the file system was projected to reach 95% capacity within an hour, risking system overload.

## Solution
- The user was notified to reduce their storage usage immediately.
- The user complied and reduced their storage usage to 32 TB, preventing the file system from overloading.

## Lessons Learned
- Monitoring and timely communication are crucial to prevent storage overload.
- Users should be aware of their storage usage and its impact on other users.
- Administrative actions, such as revoking write permissions, may be necessary to protect the system.

## Follow-up Actions
- Continue monitoring storage usage on $FASTTMP.
- Consider implementing formal quotas to prevent excessive usage by individual users.
- Educate users on responsible storage usage practices.
---

### 2024080442000284_Quota%20hpcvault%20-%20bccb03.md
# Ticket 2024080442000284

 # HPC Support Ticket: Quota Increase Request for HPCVAULT

## Keywords
- Quota Increase
- HPCVAULT
- Block Quota
- Storage Allocation

## Summary
A user requested an increase in their block quota on HPCVAULT from 11.5T to 50T.

## Root Cause
The user required additional storage space for their computational biology research.

## Solution
The HPC Admin increased the block quota for the user's group (bccb03) on HPCVAULT to the requested 50T.

## What Can Be Learned
- Users may request quota increases for additional storage space.
- HPC Admins can adjust block quotas to meet user needs.
- Effective communication and prompt action can resolve storage allocation issues efficiently.

## Actions Taken
1. User submitted a request for a quota increase.
2. HPC Admin reviewed and approved the request.
3. HPC Admin increased the block quota on HPCVAULT to 50T.

## Follow-Up
No further action required as the quota increase was successfully implemented.

## Notes
- Ensure proper documentation of quota changes for future reference.
- Regularly review storage usage to anticipate and address future quota increase requests.
---

### 2024022442000462_username%3A%20iwi5168h%2C%20exceed%20quota%20on%20home_hpc.md
# Ticket 2024022442000462

 # HPC Support Ticket: Exceed Quota on Home Directory

## Keywords
- Exceed quota warning
- Home directory
- Storage limit
- Job crashing
- Cache/application data

## Problem Description
- User receives exceed quota warnings and job crashes due to storage limits.
- User stores project data in `/home/woody` but receives warnings for `/home/hpc`.
- User's home directory is organized as `/home/hpc/<groupname>/<username>`.

## Root Cause
- Possible cache or application data polluting the home directory despite the main work directory being elsewhere.

## Solution
- **Identify Large Files/Folders:**
  ```bash
  du -ahx $HOME | sort -rh | head -5
  ```
- **Find Files Larger than 100MB:**
  ```bash
  find $HOME -xdev -type f -size +100M
  ```
- **List Ten Last Changed Files/Folders:**
  ```bash
  ls -lt $HOME | head -n 10
  ```

## General Learnings
- Home directories on HPC systems may have specific organizational structures.
- Exceeding quota can cause job crashes even if the main work directory is elsewhere.
- Cache or application data can unintentionally fill up the home directory.
- Useful commands to identify and manage large files and directories.

## Roles Involved
- **HPC Admins:** Provided detailed instructions and support.
- **User:** Reported the issue and followed instructions for resolution.

## Additional Notes
- Regularly check and clean up home directories to avoid quota issues.
- Understand the directory structure and storage policies of the HPC system.
---

### 2023060142002846_How%20to%20check%20quota%3F.md
# Ticket 2023060142002846

 ```markdown
# HPC-Support Ticket: How to Check Quota

## Keywords
- Quota
- Used Space
- Free Space
- Woody Directory
- `quotas -s` Command
- Connection Refused
- Disk Quotas

## Problem Description
- User received a notification that their quota in the woody directory is exceeded.
- User attempted to check quota using the `quotas -s` command but encountered an error: `Connection refused`.

## Root Cause
- The `quotas -s` command failed to connect to the quota server (`wadm2.nhr.fau.de`).

## Solution
- The user needs an alternative method to check their quota for the woody directory.
- Suggest using specific commands or tools provided by the HPC environment to check quota, such as `quota -v` or accessing a web-based quota management interface if available.

## General Learning
- Understand the importance of checking quotas regularly to avoid exceeding limits.
- Recognize common errors like `Connection refused` when using quota commands.
- Be aware of alternative methods to check quotas in case the primary method fails.
```
---

### 2024082542000404_Regarding%20System%20Error%20122.md
# Ticket 2024082542000404

 ```markdown
# HPC Support Ticket: System Error 122

## Issue Description
- **Subject:** Regarding System Error 122
- **User Report:** Unable to save Python file in working directory via VSCode SSH Client.
- **Error Message:**
  ```
  Failed to save 'new_data.py': Unable to write file
  'vscode-remote://ssh-remote+7b22686f73744e616d65223a2274696e79782e6e68722e6661752e6465222c2275736572223a22726c766c31303168227d/home/hpc/rlvl/rlvl101h/experiment/new_data.py'
  (Unknown (FileSystemError): Error: Unknown system error -122: Unknown system error -122, close)
  ```

## Root Cause
- **Potential Cause:** Quota exceeded for the user's home directory.
- **Admin Investigation:**
  ```
  Path              Used     SoftQ    HardQ    Gracetime  Filec    FileQ    FiHaQ    FileGrace
  /home/hpc          193.9G   104.9G   209.7G  19967days  17,150      500K   1,000K        N/A
  ```

## Solution
- **Admin Action:** Cleaned up the user's home directory to bring it within quota limits.
- **Verification:**
  ```
  Path              Used     SoftQ    HardQ    Gracetime  Filec    FileQ    FiHaQ    FileGrace
  /home/hpc           43.6G   104.9G   209.7G        N/A  17,099      500K   1,000K        N/A
  ```

## Lessons Learned
- **Quota Management:** Regularly monitor and manage user quotas to prevent such issues.
- **VSCode Support:** Clarify that VSCode support is not provided, but underlying system issues can be addressed.
- **Error Handling:** System error -122 can be indicative of quota issues.

## Keywords
- System Error 122
- VSCode SSH Client
- FileSystemError
- Quota Exceeded
- Home Directory
- Cleanup
```
---

### 42304783_Soft%20Quota%20Limit%20Erh%C3%83%C2%B6hung.md
# Ticket 42304783

 # HPC Support Ticket: Soft Quota Limit Increase

## Keywords
- Soft quota limit
- Storage increase
- Fluid-structure simulations
- Temporary storage

## Problem
- User's soft quota limit on `/home/woody` is 250 GB and has been exceeded.
- User requires more storage for unsteady calculations with fine mesh geometry and upcoming fluid-structure simulations.

## Solution
- HPC Admin increased the user's quota on `/home/woody` to 500 GB soft / 1000 GB hard.
- Recommended using `$FASTTMP` for large files needed temporarily, as it has no quota but implements a sliding deletion policy.

## General Learnings
- Users may need increased storage for complex simulations.
- Temporary storage solutions like `$FASTTMP` should be recommended for large, short-term files.
- Regularly review and adjust quotas based on user needs and system capacity.

## References
- [HPC Environment File Systems](http://www.hpc.rrze.fau.de/systeme/hpc-environment.shtml#fs)
- [HPC Services](http://www.hpc.rrze.fau.de/)
---

### 2025013142002831_quota-related%20issue%20on%20the%20cluster.md
# Ticket 2025013142002831

 # HPC Support Ticket: Quota-Related Issue on the Cluster

## Keywords
- Disk quota exceeded
- Atuin filesystem
- File count limit
- Quota usage

## Issue Description
- **User Report:** The user encountered a "Disk quota exceeded" error when trying to create a directory in their home directory on the Atuin filesystem, despite their quota usage appearing to be within the allocated limit.
- **Error Message:** `mkdir: cannot create directory ‘temp’: Disk quota exceeded`

## Root Cause
- The project has reached the limit of 10 million files, even though there is still free space available.

## Solution
- **HPC Admin Response:** The user and their coworkers need to reduce the number of (small) files on the system.
- **File Count Details:** A list of users within the project, their used space, and file count was provided to help identify and address the issue.

## General Learnings
- Disk quota errors can occur due to file count limits, not just space usage.
- Regularly monitor and manage the number of files to avoid hitting file count limits.
- Communicate with coworkers to ensure collective adherence to file count limits.

## Next Steps
- Users should review and delete unnecessary files.
- Consider archiving or compressing small files to reduce the overall file count.
- Regularly check file counts and usage to prevent future quota-related issues.

## Additional Resources
- Contact HPC Admins for further assistance if needed.
- Refer to the HPC documentation for best practices in file management.

---

This documentation aims to help support employees identify and resolve similar quota-related issues in the future.
---

### 2024031542000058_Erh%C3%83%C2%B6hung%20Quota%20auf%20_home_vault%20unrz254.md
# Ticket 2024031542000058

 ```markdown
# HPC Support Ticket: Increase Quota on /home/vault

## Keywords
- Quota
- Vault
- Filecount
- Block-Quota

## Summary
A user requested an increase in their quota on the Vault storage system. The HPC Admin responded by increasing the block-quota but maintained the filecount-quota.

## Root Cause
- User requested an increase in storage quota.

## Solution
- Block-quota increased to 5 TB.
- Filecount-quota remained unchanged at 200k.

## Lessons Learned
- Storage space (block-quota) is not a limiting factor on Vault.
- Filecount-quota is the primary concern and should be monitored.
- Users should be aware of both block-quota and filecount-quota when requesting storage increases.
```
---

### 42064935_Filesystem%20f%C3%83%C2%BCr%20Rechnungen%20auf%20Tinyblue.md
# Ticket 42064935

 ```markdown
# HPC Support Ticket: Filesystem für Rechnungen auf Tinyblue

## Keywords
- Quota
- Filesystem
- Tinyblue
- c64
- Rechnungen
- /home/woody

## Summary
A user is approaching the quota limit on their home directory (/home/woody) while running computations on Tinyblue. The user requests a quota increase to prevent job failures due to quota exceedance.

## Root Cause
- User is nearing the 10 GB quota limit on /home/woody.

## Solution
- HPC Admins confirm that the quota can be increased upon request.
- HPC Admins suggest using c64 as an alternative, which is available on Tinyblue and has less load on the filesystem.

## Additional Information
- The user plans to use c64 for future projects as discussed with an HPC Admin.
- The current quota for /home/woody is 25.0G with 8.5G used.

## Conclusion
- Users should request a quota increase if they are nearing the limit.
- Using c64 is recommended for better performance and less load on the filesystem.
```
---

### 2022082942002524_Quota.md
# Ticket 2022082942002524

 ```markdown
# HPC Support Ticket: Quota Increase Request

## Keywords
- Quota
- Soft-Limit
- Data Archiving
- Quota Increase

## Problem
- User has reached the soft limit of their quota.
- Projects are not yet completed, preventing data archiving.

## Solution
- HPC Admin increased the user's quota on `/home/vault` to 2 TB.

## Lessons Learned
- Users may require quota increases due to ongoing projects.
- HPC Admins can adjust quotas to accommodate user needs.
- Regular monitoring of quota usage is essential to prevent disruptions.
```
---

### 2022012442003143_Speicher%20Klima-Gruppe.md
# Ticket 2022012442003143

 # HPC Support Ticket: Storage Usage for Climate Group

## Keywords
- Storage usage
- HPC systems
- Climate group
- gwgk*
- gwgi*
- FAU

## Summary
A user requested information about the current storage usage of their team (gwgk* and gwgi*) on the HPC systems. The HPC Admin provided detailed storage usage statistics for various directories and systems.

## Root Cause
The user needed to know the storage usage of their team on the HPC systems to manage their resources effectively.

## Solution
The HPC Admin provided the following storage usage details:

- `/home/woody`: 3.423 TB
- `/home/vault`: 12.410 TB (with ample free space)
- `/home/hpc`: 109 GB
- `Meggie-FASTTMP`: 32.950 TB
- `Emmy-FASTTMP`: 24.780 TB
- `/home/titan`: 215.77 TB out of 225.00 TB (95.90% used)
  - Largest consumers:
    - gwgk001h: 13573G
    - gwgk002h: 16130G
    - gwgi006h: 16939G
    - gwgi008h: 42971G
    - gwgi18: 96248G

## Lessons Learned
- Users can request storage usage information from HPC Admins for better resource management.
- HPC Admins can quickly provide detailed storage usage statistics for specific groups or users.
- Regular monitoring of storage usage can help prevent resource exhaustion.
---

### 42328236_Speicher%20FASTEST%20Emmy.md
# Ticket 42328236

 ```markdown
# HPC-Support Ticket: Speicher FASTEST Emmy

## Keywords
- Storage space
- File writing
- Simulation
- File size
- File count

## Problem Description
- User's simulations are being aborted due to insufficient storage space for writing files.
- User reports using approximately 5 times 3-5 GiB of storage.
- User generates around 300,000 files per simulation, each approximately 100K in size.

## Root Cause
- Insufficient storage space for writing files.
- Possible issue with the large number of files being generated.

## Solution
- Not explicitly provided in the conversation.
- Further investigation needed to determine if the issue is due to storage space or the number of files.

## General Learnings
- Monitor storage usage during simulations.
- Consider the impact of a large number of files on the file system.
- Communicate with users to understand their storage requirements and optimize file management strategies.
```
---

### 2022121542003569_Is%20the%20prompt%20message%20relevant%20with%20me%3F.md
# Ticket 2022121542003569

 # HPC Support Ticket: Message on HPC Front End

## Keywords
- Message-of-the-day (MOTD)
- Storage
- Scratch directory
- Certificate expiration

## Problem
User encounters a message every time they open the HPC front end and is unsure if it is related to their storage usage.

## Root Cause
The message is part of the message-of-the-day (MOTD) and is not directly related to the user's storage usage. It includes information about an expired certificate.

## Solution
- **Ignore the message** if no data is missing from the `tinyx:/scratch` directory.
- The message is a general announcement and does not indicate excessive storage usage by the user.

## General Learning
- MOTD messages can contain various announcements and should not always be interpreted as personal alerts.
- Users should check their storage directories if they suspect data loss or excessive usage.

## Next Steps
- If the user experiences data loss or other issues, they should contact HPC support for further assistance.
- HPC Admins should ensure that MOTD messages are clear and relevant to avoid user confusion.
---

### 2017060142000243_Speicherplatz%20auf%20_home_vault_caph_mppi030h.md
# Ticket 2017060142000243

 ```markdown
# HPC-Support Ticket: Storage Space Issue on /home/vault/caph/mppi030h

## Keywords
- Storage Quota
- Machine Learning
- Snapshots
- Tape Storage
- Quota Increase

## Problem Description
- User requires more storage space than the default 100GB on `/home/vault` for machine learning tasks.
- Snapshots of network topologies and simulation data are consuming significant space.
- Current quota has been exceeded due to the accumulation of large files.

## Root Cause
- Insufficient storage quota for the user's machine learning and simulation data.

## User's Suggested Solutions
- Increase the quota to ~1TB to accommodate long-term parallel training sessions.
- Possibly migrate data to tape storage, though user-triggered commands are not yet available.

## HPC Admin's Response
- [Pending]

## General Learnings
- Machine learning tasks often require substantial storage space.
- Users may need increased quotas for long-term projects.
- Tape storage migration commands are planned but not yet available for users.

## Solution
- [Pending HPC Admin's Response]
```
---

### 2022070442004491_file%20auf%20Git%20pushen%20mit%20%C3%83%C2%BCber%20100%20MB.md
# Ticket 2022070442004491

 # HPC Support Ticket: Pushing Large Files to Git

## Keywords
- Git
- Large files
- GitHub file size limit
- Git Large File Storage (LFS)
- rsync

## Problem
- User unable to push a file larger than 100 MB to GitHub from their `$WORK` directory.
- Error message: `remote: error: File param.pt is 118.40 MB; this exceeds GitHub's file size limit of 100.00 MB`

## Root Cause
- GitHub has a file size limit of 100 MB.
- The user's file exceeds this limit.

## Solution
- **Git Large File Storage (LFS)**: Not currently supported by the HPC admin team.
- **Alternative**: Use `rsync` for transferring large files between devices.

## General Learnings
- Always use the official email address (e.g., @fau.de) for ticket submission to ensure proper tracking.
- Git is not ideal for versioning large files. Consider alternative tools for transferring large data.

## Next Steps
- If Git LFS is required, the user may need to request its installation and configuration.
- For immediate needs, utilize `rsync` for file transfers.

---

This documentation aims to assist HPC support employees in resolving similar issues related to pushing large files to Git repositories.
---

### 42057250_Quota.md
# Ticket 42057250

 # HPC Support Ticket: Quota Issue

## Keywords
- Quota
- Grace period
- Account cleanup
- Data backup
- File deletion

## Problem
- User exceeded their quota (iwst10).
- User requested additional time to clean up their account.

## Conversation Summary
- **User**: Requested a grace period until the following Tuesday to clean up their account.
- **HPC Admin**: Extended the grace period to 7 days and reduced the quota from 1 TB to 750 GB.
- **User**: Requested further extension until Monday to complete data backup and deletion.
- **HPC Admin**: Clarified that no automatic deletion occurs while over quota, but new files cannot be created.

## Solution
- **Grace Period Extension**: HPC Admin extended the grace period to allow the user more time to clean up their account.
- **Quota Reduction**: HPC Admin reduced the quota to encourage the user to free up space.
- **Clarification on Quota Exceedance**: HPC Admin explained the consequences of exceeding the quota (inability to create new files) and assured the user that no automatic deletion would occur.

## General Learnings
- Users may need additional time to clean up their accounts when they exceed their quota.
- Extending the grace period and reducing the quota can help users manage their storage more effectively.
- Clear communication about the consequences of exceeding the quota is important to avoid user confusion.
---

### 2023112842000252_Reg.%20data%20sharing%20between%20user%20accounts.md
# Ticket 2023112842000252

 # HPC Support Ticket: Data Sharing Between User Accounts

## Keywords
- Data sharing
- Multiple HPC accounts
- Project folders
- $WORK environment variable
- NHR projects

## Problem
- User has two HPC accounts (one from Faunhofer IIS and another from a project) and wants to access data from one account in the other without copying the dataset.
- User cannot find the project folder in `/home/woody/`.

## Root Cause
- User is unaware of the data sharing procedure between HPC accounts.
- User is looking for the project folder in the wrong directory.

## Solution
- **Data Sharing**: Refer to the FAQ on data sharing between HPC accounts: [FAQ Link](https://hpc.fau.de/faqs/#i-would-like-to-cross-use-data-between-hpc-accounts).
- **Project Folder**: For NHR projects, the `$WORK` environment variable points to `/home/atuin` instead of `/home/woody`. The project folder `/home/atuin/b197dc` has already been created.

## General Learnings
- Understand the data sharing policies and procedures for multiple HPC accounts.
- Be aware of the correct environment variables and directory structures for different types of projects (e.g., NHR projects).
- Always check the appropriate FAQs and documentation for common issues.
---

### 2022101342001149_How%20to%20check%20how%20much%20memory%20I%20use%3F.md
# Ticket 2022101342001149

 ```markdown
# HPC Support Ticket: Checking Disk Space Usage

## Keywords
- Disk space
- Quota
- Command line
- Shared filesystem

## Problem
- User ran over the disk space quota and needed to check the amount of disk space used to ensure enough space was freed up.

## Solution
- Use the commands `quota` or `shownicerquota.pl` on the command line of any frontend to check disk space usage.

## Additional Information
- The user was specifically concerned about the HPC filesystem with a 50GB limit and no extensions possible.
- The user successfully removed unnecessary files and resolved the issue.

## Lessons Learned
- Users can quickly check their disk space usage using specific commands on the command line.
- It is important to monitor and manage disk space usage to avoid running over the quota.
```
---

### 42213017_Mehr%20quota%20auf%20woody.md
# Ticket 42213017

 ```markdown
# HPC Support Ticket: Request for Increased Quota on Woody Home

## Keywords
- Quota
- Woody Home
- Increase
- Storage
- Request

## Summary
A user requested an increase in their quota on the Woody home directory. The user specified that they would be satisfied with 100GB but preferred 200GB.

## Root Cause
The user needed additional storage space for their work on the Woody home directory.

## Solution
The HPC Admin increased the quota on the Woody home directory for the user.

## Lessons Learned
- Users should send new requests as separate tickets rather than replying to old cases to maintain clarity.
- HPC Admins can adjust quotas based on user requests to ensure sufficient storage for their work.

## Notes
- Ensure proper communication channels are used for new requests to avoid confusion.
- Regularly review and adjust storage quotas to meet user needs.
```
---

### 2020051542000963_Anliegen%20Max%20Schmidt%20bcpc000h.md
# Ticket 2020051542000963

 # HPC Support Ticket Analysis

## Keywords
- SoftQuota
- Used GB
- Grace time
- Data sync
- Data backup
- User ID: bcpc000h

## Problem Description
- User's SoftQuota was exceeded.
- User synced and backed up data, then deleted several hundred GB from `meggie/vault`.
- "Used GB" did not change, and grace time of 4 days is still displayed.

## Root Cause
- Possible issue with quota system not updating after data deletion.

## Solution
- HPC Admin needs to check the quota system to ensure it reflects the recent data deletion.
- Verify if there are any pending processes or delays in updating the quota.

## General Learnings
- Quota systems may not update immediately after data deletion.
- Users should be informed about potential delays in quota updates.
- Regular checks and maintenance of the quota system are essential to ensure accuracy.

## Next Steps
- HPC Admin to investigate and resolve the quota update issue.
- Communicate the resolution to the user.

---

This documentation can be used to address similar issues in the future.
---

### 2023041342000221_Quota%20extension.md
# Ticket 2023041342000221

 ```markdown
# HPC-Support Ticket: Quota Extension

## Keywords
- Quota Extension
- $WORK
- NHR-Rechenzeitantrag
- HPC-Portal
- Test Accounts

## Summary
A user requested an increase in their quota for MD calculations on $WORK. The user initially had a soft quota of 500 GB and requested an increase to 1-1.5 TB.

## Root Cause
The user needed additional storage space for their MD calculations.

## Solution
1. **Initial Request**: The user requested a quota increase for their account.
2. **Admin Response**: The HPC Admin asked for the specific amount of additional space needed.
3. **User Clarification**: The user specified that 1-1.5 TB would be sufficient.
4. **NHR Application Suggestion**: The HPC Admin suggested submitting an NHR-Rechenzeitantrag, which includes additional disk quota.
5. **Temporary Quota Increase**: The user mentioned they had submitted an NHR application and requested a temporary quota increase and test accounts for new systems.
6. **Quota Increase Granted**: The HPC Admin increased the quota for the user's account to 1.5 TB on /home/woody.
7. **NHR Accounts**: The user was informed that NHR project accounts could be managed through the HPC-Portal and used normally during the application review process.

## General Learnings
- Users can request temporary quota increases while waiting for NHR application approval.
- NHR applications provide additional disk quota along with compute time.
- NHR project accounts can be managed and used through the HPC-Portal even during the application review process.
```
---

### 2024121642002297_High%20File%20Count%20for%20Project%20b211dd.md
# Ticket 2024121642002297

 # HPC Support Ticket: High File Count for Project b211dd

## Keywords
- High file count
- Metadata operations
- File system optimization
- Small files
- HPC file systems

## Summary
- **Issue**: High file count (7.7 million files) on $WORK causing high load and excessive metadata operations on the HPC file system.
- **Project**: b211dd
- **User Response**: User did not recognize the project, possibly related to a teaching event.
- **Resolution**: The issue was due to a mistake; the initial email was disregarded.

## Details
- **HPC Admin**: Notified the user about the high file count and its impact on the file system. Suggested using more suitable data formats and offered assistance.
- **User**: Could not identify the project, queried if it was related to a teaching event.
- **HPC Admin**: Acknowledged a mistake and asked the user to disregard the initial email.

## Lessons Learned
- High file counts, especially small files, can significantly impact HPC file system performance.
- Users should be encouraged to use data formats optimized for HPC environments.
- Regular communication and training sessions (e.g., monthly introductions) can help users understand best practices for file storage.
- Mistakes in communication can occur; prompt correction and apology are essential for maintaining user trust.

## Action Items
- Continue to monitor file system usage and notify users of high file counts.
- Provide resources and training on optimizing file storage for HPC environments.
- Ensure accurate communication and promptly address any errors in correspondence.

## References
- [HPC Café Introduction for AI Users](https://hpc.fau.de/teaching/hpc-cafe/#nutshell)
---

### 2023021442003266_Projekt%20b162dc-DeepPano%20Speicherplatz.md
# Ticket 2023021442003266

 # HPC Support Ticket: Projekt b162dc-DeepPano Speicherplatz

## Keywords
- Cluster-Home-Umgebung
- Projektaccount
- $WOODYHOME
- $WORK
- Speicherplatz

## Problem
- User is migrating their cluster home environment from a departmental account to a project account.
- Requests additional storage space on `$WOODYHOME` and automatic home directories for each account.

## Root Cause
- User needs additional storage space and automatic home directory setup for a project account.

## Solution
- HPC Admin advises the user to use `$WORK` instead of `/home/woody`.

## General Learnings
- For storage space requests, users should be directed to use `$WORK` instead of `/home/woody`.
- Ensure users are aware of the appropriate storage locations and their usage policies.

## Next Steps
- Inform users about the correct usage of storage locations.
- Update documentation to reflect the preferred storage locations for project accounts.
---

### 2018121742000371_Speicherplatz%20VAULT%20zuruecksetzen.md
# Ticket 2018121742000371

 # HPC Support Ticket: Resetting VAULT Storage Quota

## Keywords
- VAULT storage
- Soft quota
- Hard quota
- Reset to standard values

## Summary
A user requested to reset their VAULT storage quota to the standard values after no longer needing the increased quota.

## Root Cause
- User had an increased storage quota (2TB Soft, 3TB Hard) that was no longer necessary.

## Solution
- Reset the user's VAULT storage quota to the standard values (105 GB Soft, 210 GB Hard).

## General Learnings
- Users may request changes to their storage quotas based on their needs.
- Standard storage quotas should be known and easily resettable by HPC Admins.
- Proper communication and confirmation of quota changes are essential for user satisfaction.

## Actions Taken
- HPC Admin to reset the user's VAULT storage quota to the standard values.

## Follow-up
- Confirm with the user that the quota has been successfully reset.
- Update any internal records to reflect the change in quota.
---

### 2016102442000962_archive%20server.md
# Ticket 2016102442000962

 # HPC Support Ticket: Archive Server

## Keywords
- Archiving data
- Compression formats
- File permissions
- Quota management
- HSM (Hierarchical Storage Management)

## Summary
A user inquires about archiving project data on the HPC cluster, specifically under `/hpc/vault`. The user has multiple questions regarding the archiving process, compression formats, file permissions, and quota management.

## Root Cause
The user needs guidance on:
1. How to archive data.
2. Best compression formats and methods.
3. Managing file permissions for group access.
4. Understanding quota limits.

## Solution
1. **Archiving Documentation**:
   - No specific "how-to archive" document exists.
   - The `/hpc/vault` directory is suitable for archiving.

2. **Compression Formats**:
   - Use any compression format (`.tar.gz`, `.zip`, `.7z`, `.rar`) that fits the workflow.
   - Default compression settings are generally sufficient.
   - Ensure archive files are between 20 and 200 GB for optimal HSM performance.

3. **File Permissions**:
   - Use Unix directory/file permissions to grant group access.
   - Example: `chmod g+rX /hpc/vault/group/user`
   - Consider long-term ownership issues when users leave the university.

4. **Quota Management**:
   - Online quota: 1 TB soft / 2 TB hard.
   - Offline (tape) quota: No formal limit, but physical constraints apply.
   - Data moved to tape is not counted in the disk quota.

## General Learnings
- **Compression**: Different compression formats have similar rates; default settings are usually sufficient.
- **File Size**: Optimal archive file size for HSM is between 20 and 200 GB.
- **Permissions**: Use Unix permissions for group access; plan for long-term ownership issues.
- **Quota**: Understand the distinction between online and offline quotas.

## Additional Notes
- **Long-term Ownership**: Consider storing archive data under a permanent account (e.g., professor's account) to avoid ownership issues when users leave.
- **HSM Performance**: Balance file size to optimize HSM performance and avoid blocking tape drives.
---

### 2024102842001537_Help%20with%20full%20quota%20issue.md
# Ticket 2024102842001537

 ```markdown
# HPC-Support Ticket: Help with Full Quota Issue

## Keywords
- Quota
- $HOME
- $WORK
- Space Management
- Auxiliary Files
- Environments
- Software Installations

## Problem Description
The user has hit their soft quota and is unable to work due to insufficient space. The user initially thought the issue was with the $WORK directory but was informed that the problem lies in the $HOME directory.

## Root Cause
- The user's $HOME directory is consuming a significant amount of space, specifically:
  - 73GB in `.cache`
  - 30GB in `.local`

## Solution
- The HPC Admin identified that the user's quota issue is in the $HOME directory, not $WORK.
- Recommended clearing space in the `.cache` and `.local` directories to free up space.

## General Learnings
- Always check both $HOME and $WORK directories when diagnosing quota issues.
- Auxiliary files and installed environments/software can consume significant space.
- Regularly monitor and clean up directories like `.cache` and `.local` to avoid hitting quota limits.

## Next Steps
- Users should regularly review and manage their storage usage in both $HOME and $WORK directories.
- Consider setting up automated scripts or reminders to clean up unnecessary files.
```
---

### 2024110842002661_VSC%20login%20error.md
# Ticket 2024110842002661

 ```markdown
# HPC Support Ticket: VSC Login Error

## Keywords
- Visual Studio Code (VSC) login error
- Terminal login
- Home directory quota
- `shownicerquota.pl`
- $HOME
- $WORK
- Documentation page

## Problem Description
- User unable to log in using Visual Studio Code (VSC) but can log in via terminal.
- User provided error output.

## Root Cause
- User's home directory ($HOME) is over quota.

## Diagnostic Steps
- HPC Admin ran `shownicerquota.pl -v <username>` to check user's quota.
- Output showed that the user's home directory was over the hard quota limit.

## Solution
- User advised to clean up their home directory ($HOME) to reduce used space.
- Recommended to use $WORK for larger files and to refer to the documentation page for more information on filesystems.

## Additional Information
- Home directory ($HOME) should be used for important files that need frequent backup.
- Documentation page: [FAU Data Filesystems](https://doc.nhr.fau.de/data/filesystems/)

## Follow-up
- User should clean up their home directory and attempt to log in using VSC again.
```
---

### 2023112842003508_Soft%20und%20Hard%20quota%20f%C3%83%C2%BCr%20Anzahl%20der%20Daten-Files.md
# Ticket 2023112842003508

 ```markdown
# HPC Support Ticket: Soft und Hard Quota für Anzahl der Daten-Files

## Keywords
- Soft quota
- Hard quota
- Inode quota
- Free energy perturbation
- Home/vault
- $WORK
- Backup and snapshot design

## Problem
- User generates a large number of small files for free energy perturbation calculations.
- Requests an increase in soft and hard quota for the number of files.

## Root Cause
- The HPCVAULT filesystem is not designed to handle large quantities of small files due to its backup and snapshot design.

## Solution
- HPC Admin slightly increased the inode quota for the user.
- Recommended using the $WORK directory for such data instead of home/vault.

## General Learning
- The HPCVAULT filesystem is not suitable for storing large numbers of small files.
- For computations that generate many small files, users should use the $WORK directory.
- Inode quotas can be adjusted to accommodate specific user needs.

## Actions Taken
- HPC Admin increased the inode quota.
- User agreed to submit calculations to the $WORK directory.

## Status
- Ticket closed.
```
---

### 2025020642001636_Quota.md
# Ticket 2025020642001636

 # HPC Support Ticket: Quota

## Keywords
- Storage quota
- `rm -rf` command
- File systems
- Backup
- Moving files between directories

## Problem
- User has exceeded the soft storage quota on `/home/hpc`.
- User is unsure if `rm -rf` command will free up space or move files to trash.
- User wants to move important files to `/home/woody` but defaults to `/home/hpc` upon SSH.

## Root Cause
- Lack of understanding about the `rm -rf` command and file system structure.
- Unclear on how to change the default directory upon SSH login.

## Solution
- **Freeing up space**: The `rm -rf` command will completely remove files and free up space. It does not move files to trash.
- **File systems and backup**: Refer to the documentation on file systems and use `$HOME` only for important files that need backup.
- **Moving files**: To move files to `/home/woody`, use the `mv` command. For example:
  ```bash
  mv /home/hpc/important_file /home/woody/
  ```
- **Changing default directory**: To change the default directory upon SSH login, modify the remote shell initialization file (e.g., `.bashrc`, `.bash_profile`) to include:
  ```bash
  cd /home/woody
  ```

## Documentation Reference
- [FAU Data and File Systems](https://doc.nhr.fau.de/data/filesystems/)

## Follow-up
- Ensure the user understands the commands and can successfully move and delete files.
- Verify that the user's default directory changes upon SSH login.
---

### 2025031442000245_Reminder%20TOS%20HPC%20Storage.md
# Ticket 2025031442000245

 ```markdown
# HPC-Support Ticket: Reminder TOS HPC Storage

## Keywords
- HPC Storage
- Data Privacy
- Personal Data
- Shared Directory
- Terms of Service (TOS)

## Summary
- **Issue**: A shared directory (`/home/vault/mpt2/shared`) was being used as a general departmental SharePoint, potentially storing personal data.
- **Root Cause**: Misuse of HPC storage for storing personal data, which is against the Terms of Service (TOS).
- **Solution**: Reminder sent to users about the TOS and the prohibition of storing personal data on HPC systems.

## Lessons Learned
- **Data Privacy**: Ensure users are aware of data privacy regulations and the prohibition of storing personal data on HPC systems.
- **TOS Compliance**: Regularly remind users about the Terms of Service to prevent misuse of HPC resources.
- **Monitoring**: Implement monitoring to detect and address non-compliant usage of shared directories.

## Actions Taken
- **Reminder Sent**: HPC Admin sent a reminder to the users about the TOS and data privacy regulations.
- **Ticket Closed**: The ticket was closed after the reminder was sent.
```
---

### 2017062842001041_Rechnungen%20abgebrochen.md
# Ticket 2017062842001041

 # HPC-Support Ticket: Rechnungen abgebrochen

## Keywords
- Job termination
- Storage quota
- File system full
- Over-quota
- Emmy cluster

## Problem Description
- User reported that all their jobs on the Emmy cluster were unexpectedly terminated at 10:57 AM after running for approximately 22 hours without issues.
- Two of the jobs did not even write the `.o` file.
- Affected job IDs: 765055.eadm, 765062.eadm, 765067.eadm, 765080.eadm, 765095.eadm.

## Root Cause
- The `/home/vault` file system was 100% full at the time of the job terminations.
- The sum of the allowed quotas for all users exceeded the actual hardware capacity, leading to the file system overflow.

## Solution
- No personal quota exceedance was involved; the issue was system-wide.
- Users were not notified about approaching over-quota levels due to the system-wide nature of the problem.
- No user-initiated data migration command was available or planned.

## Lessons Learned
- Regular monitoring of the file system usage is crucial to prevent such issues.
- Communication about system-wide storage limitations should be improved.
- Users should be aware that the sum of individual quotas can exceed the actual storage capacity.

## Follow-up Actions
- Ensure that users are informed about the overall storage situation.
- Implement better monitoring and alerting for system-wide storage usage.
- Review and adjust quota policies if necessary to prevent future overflows.
---

### 2019022842002409_Saturn%20Quota.md
# Ticket 2019022842002409

 # HPC Support Ticket: Saturn Quota

## Keywords
- Quota
- /home/saturn
- User Permissions
- HPC Admin

## Summary
A user requested the addition of specific users to the quota file for `/home/saturn`.

## Root Cause
The user noticed the introduction of a quota file for `/home/saturn` and needed specific users to be granted permissions.

## Solution
The HPC Admin was requested to add the specified users to the quota file for `/home/saturn`.

## General Learning
- Users may need to be added to quota files for specific directories.
- HPC Admins are responsible for managing user permissions and quotas.
- Proper communication and request format are essential for efficient ticket resolution.

## Next Steps
- HPC Admin should confirm the addition of the specified users to the quota file.
- Verify that the users have the appropriate permissions and quotas.
---

### 2021112942003206_Validity%20extension%20of%20HPC%20account.md
# Ticket 2021112942003206

 # HPC Support Ticket: Validity Extension of HPC Account

## Keywords
- Account validity extension
- Storage quota increase
- Affiliation change

## Summary
- **User Request**: Extension of HPC account validity and increase in storage space.
- **HPC Admin Response**: Account affiliation changed from guest scientist to PhD student, storage quota increased to 1TB.

## Root Cause
- User's HPC account was set to expire at the end of December.
- User required additional storage space in the work directory.

## Solution
- **Account Validity**: HPC Admin extended the account validity by changing the user's affiliation.
- **Storage Quota**: HPC Admin increased the storage quota on `$WOODYHOME` to 1TB.

## Procedure for Storage Quota Increase
- User requested additional storage space.
- HPC Admin reviewed and approved the request, then increased the quota.

## General Learnings
- Users can request extensions for their HPC account validity.
- Storage quota increases require approval and can be handled by HPC Admins.
- Changing user affiliation can affect account validity and permissions.

## Follow-up
- No further action required from the user.
- HPC Admin confirmed the changes and closed the ticket.

---

This documentation can be used as a reference for handling similar requests related to account validity extensions and storage quota increases.
---

### 2023030342001269_Over%20quota%20but%20only%2015GB%20used.md
# Ticket 2023030342001269

 ```markdown
# HPC Support Ticket: Over Quota but Only 15GB Used

## Keywords
- Over quota
- Home directory
- WinSCP
- Hidden files
- Conda
- Documentation

## Problem Description
- User received a warning about being over quota in the home directory.
- WinSCP showed only 15GB used, but the user had previously been over quota and deleted files.
- The warning persisted.

## Root Cause
- Hidden files and directories were not visible in WinSCP.
- Large hidden directories, particularly `.conda`, were consuming significant space.

## Solution
- HPC Admin identified large hidden directories using the `du` command.
- The `.conda` directory was found to be 33GB.
- User was advised to refer to the documentation for managing Conda installations to avoid writing everything to the home directory.

## Lessons Learned
- Always check for hidden files and directories when diagnosing quota issues.
- Conda installations can consume significant space in the home directory.
- Documentation should be consulted for best practices in managing Conda environments.

## Documentation Link
- [Python and Jupyter Documentation](https://hpc.fau.de/systems-services/documentation-instructions/special-applications-and-tips-tricks/python-and-jupyter/)
```
---

### 2024120242001779_More%20HPC%20Quota%20Required.md
# Ticket 2024120242001779

 # HPC Support Ticket Conversation Analysis

## Keywords
- HPC Quota
- Dataset Storage
- Python Libraries
- Password Issues
- Error Resolution

## General Learnings
- **Quota Management**: Users should be aware of their storage quotas and the appropriate directories for different types of data.
- **Python Environment**: Proper setup of the Python environment is crucial for avoiding library-related errors.
- **User Training**: New users may benefit from introductory sessions to understand the system better.

## Root Cause of Problems
1. **Exceeding Block Quota**: The user exceeded the storage quota while downloading a large dataset.
2. **Incorrect Storage Directory**: The user stored the dataset in the home directory instead of the appropriate work directory.
3. **Python Library Issues**: The user encountered errors while installing and using Python libraries due to missing dependencies.
4. **Password Issues**: The user had trouble with the password for their HPC account.

## Solutions
1. **Quota Management**:
   - **Solution**: Move the dataset to the `$WORK` directory, which is designed for large datasets.
   - **Reference**: [HPC Filesystems Documentation](https://doc.nhr.fau.de/data/filesystems/)

2. **Python Environment Setup**:
   - **Solution**: Follow the instructions for setting up the Python environment without needing a password.
   - **Reference**: [Python Environment Setup](https://doc.nhr.fau.de/environment/python-env/)

3. **Error Resolution**:
   - **Solution**: Provide detailed steps and error messages to the support team for further assistance.
   - **Example**: `ImportError: /usr/lib/x86_64-linux-gnu/libstdc++.so.6: version 'GLIBCXX_3.4.29' not found`

4. **User Training**:
   - **Solution**: Attend introductory sessions for new users to understand the system better.
   - **Upcoming Sessions**:
     - Wednesday, December 18, 2024: Using the HPC clusters at NHR@FAU – General Introduction, 4:00 p.m.
     - Thursday, December 19, 2024: Using the HPC clusters at NHR@FAU – Introduction for AI Users, 4:00 p.m.
     - **Location**: [Zoom Link](https://go-nhr.de/hpc-in-a-nutshell)

## Conclusion
Users should be proactive in managing their storage quotas and understanding the system's directory structure. Proper setup of the Python environment and attending introductory sessions can help avoid common issues. Detailed error reporting is essential for efficient problem resolution.
---

### 2020111042003225_Storage%20von%20Forschungsdaten.md
# Ticket 2020111042003225

 ```markdown
# HPC-Support Ticket: Storage von Forschungsdaten

## Abstract
- **User Requirement**: Long-term storage of research data, preferably FAIR-compliant.
- **Budget**: Available funds for storage solutions.

## Detailed Description
- **Data Type**: Results from molecular simulations, including MD simulations, analyses, and subsequent computations.
- **Storage Duration**: 10 years.
- **FAIR Compliance**: Desired.
- **Budget**: Remaining funds from appointment resources.
- **Learned**: Band storage is not suitable (or only partially) for this type of data.

## Options Discussed
- **New Research Data Server**: Mentioned but seems to be allocated to various SFBs and other commitments.
- **Physical Expansion**: Difficult but potentially feasible.
- **Disk and Tape Storage**: Mixed solution recommended.
  - **Disk Storage**: $VAULT with 5-year availability.
  - **Tape Storage**: 10-year availability, requires an archive user with long-term FAU affiliation.
- **Pricing**:
  - Disk: 18 Euro/TB/year + backup costs.
  - Tape: 12 Euro/TB/year.
  - Discounts for prepayment and larger quotas.

## User Concerns
- **Quota Increase**: Request for immediate increase for the group and individual users as the 300GB limit is almost reached.
- **Project Quota**: Inquiry about additional storage for projects beyond the standard user quota.

## Solutions Provided
- **Offer**: 300TB HDD + 150TB Tape Storage for 25,000 Euro, available until hardware replacement (earliest 2026).
- **FAIR Compliance**: Not automatic; users are responsible for DOI and data export via HPC-Mover.
- **Quota Increase**: Possible for individual users upon request.
- **Group Quota**: Can be set up for purchased storage.
- **AGFD Allocation**: 100TB to be allocated separately and can be added to the group quota later.

## Next Steps
- **Zoom Meeting**: Scheduled to discuss further details.
- **User Action**: Review budget and submit a separate request to AGFD.

## Keywords
- Long-term storage
- FAIR compliance
- Disk and tape storage
- Quota increase
- Project storage
- Budget allocation
- HPC-Mover
- DOI

## General Learnings
- **Storage Options**: Understanding the different storage solutions available and their suitability for various data types.
- **FAIR Compliance**: Importance of user responsibility in ensuring FAIR principles are met.
- **Quota Management**: Process for increasing quotas for groups and individual users.
- **Budget Allocation**: Considerations for purchasing vs. renting storage solutions.
```
---

### 2023122242001126_Fwd%3A%20Fwd%3A%20Over%20quota%20on%20_home_vault.md
# Ticket 2023122242001126

 ```markdown
# HPC-Support Ticket: Over Quota on /home/vault

## Keywords
- Quota
- Over quota
- /home/vault
- RADAR-Satellitendaten
- Hard quota
- Soft quota
- Grace period
- Blocks used
- Blocks quota
- Files used
- Files quota

## Problem Description
A master's student in the gwgi group received a hard quota notification for exceeding the block quota on the /home/vault filesystem. The student was working with large RADAR-Satellitendaten, which resulted in exceeding the allocated storage space.

## Root Cause
The user exceeded the hard quota limit of 524.3G on the /home/vault filesystem, preventing further file storage.

## Quota Report
- **Blocks used:** 1,048,576,000 (= 1048.6G)
- **Blocks quota soft:** 524,288,000 (= 524.3G)
- **Blocks quota hard:** 1,048,576,000 (= 1048.6G)
- **Blocks grace remaining:** 6 days
- **Files used:** 2,511
- **Files quota soft:** 200,000
- **Files quota hard:** 400,000

## Solution
The HPC Admin increased the hard quota to 12TB to accommodate the large dataset.

## Notes
- The `shownicerquota.pl` script cannot resolve quotas over 4TB, so unusual output may be observed.
- The 'soft' quota values can be exceeded for up to one week (grace period).
- The 'hard' quota values are absolute maximums and cannot be exceeded.

## General Learning
- Users working with large datasets should request increased quota limits in advance.
- HPC Admins can adjust quota limits to meet user needs.
- Understanding the difference between soft and hard quotas is crucial for managing storage effectively.
```
---

### 2022041342003141_Softquota.md
# Ticket 2022041342003141

 ```markdown
# HPC Support Ticket: Softquota

## Keywords
- Softquota
- /home/vault
- Storage
- Simulations
- Quota Increase

## Problem
- User regularly exceeds the softquota of their `/home/vault` directory due to parallel, storage-intensive simulations.

## Solution
- HPC Admin increased the softquota to 1 TB and the hard quota to 1.5 TB.

## Lessons Learned
- Users running storage-intensive simulations may need higher quotas.
- HPC Admins can adjust quotas to accommodate user needs.

## Actions Taken
- HPC Admin adjusted the user's quota settings.

## Root Cause
- Insufficient storage quota for the user's simulation workload.
```
---

### 2021120242000374_quato%20on%20vault.md
# Ticket 2021120242000374

 ```markdown
# HPC Support Ticket: Quota on Vault

## Keywords
- Quota
- Vault
- Access Rights
- Default Quota
- Group Storage

## Summary
A user reported receiving a message indicating they had exceeded their quota on the vault storage system, despite the group having a much larger allocation.

## Root Cause
- The user was assigned a default quota upon account creation, regardless of the group's additional storage allocation.

## Solution
- The HPC Admin identified and corrected the issue, adjusting the user's quota to match the group's allocation.

## Lessons Learned
- Default quotas are assigned to new users regardless of group storage allocations.
- Manual adjustment of quotas may be necessary to align with group allocations.
- Consider updating the account creation script to automatically adjust quotas based on group allocations.

## Actions Taken
- The HPC Admin fixed the quota issue.
- The ticket was closed after the issue was resolved.

## Follow-Up
- Discuss the possibility of updating the account creation script to automatically adjust quotas based on group allocations.
```
---

### 2021031842002341_Scratch-SSD%20auf%20A100%20Systemen.md
# Ticket 2021031842002341

 ```markdown
# HPC Support Ticket: Scratch-SSD auf A100 Systemen

## Keywords
- Scratch-SSD
- A100 Systems
- Mounts
- $TMPDIR
- $FASTTMP
- User-Namespaces

## Problem Description
- User encountered issues with mount points on A100 systems.
- Both `sda3` and `md126` were mounted under `/scratch`.
- `$TMPDIR` and `/scratchssd` pointed to `/dev/md126`.
- `$FASTTMP` contained an error message indicating it no longer exists.

## Root Cause
- A100 nodes have both a system SSD and a data SSD.
- System SSD is mounted under `/scratch` due to autoinstallation.
- User-Namespaces create a private directory under `/scratchssd` for non-root users, overlaying the system scratch.

## Solution
- Pre-copying data to node-local SSD is not possible due to non-persistent User-Namespaces and unpredictable node assignment.
- `$FASTTMP` is only available locally on parallel computers (Emmy and Meggie) and is separate for each.

## General Learnings
- Understand the distinction between system SSD and data SSD on A100 nodes.
- Recognize the role of User-Namespaces in creating private directories.
- Acknowledge the limitations of pre-copying data to node-local SSDs.
- Be aware of the local nature of `$FASTTMP` on parallel computers.
```
---

### 42015893_Re%3A%2042015863.md
# Ticket 42015893

 ```markdown
# HPC Support Ticket Analysis: Subject Re: 42015863

## Keywords
- Data relocation
- Quota increase
- Simulation data
- $WOODYHOME
- /home/rrze

## Summary
- **Root Cause**: User moved data to `$WOODYHOME`, which is the appropriate location for simulation data.
- **Solution**: No immediate quota increase required for `/home/rrze`.

## Lessons Learned
- Users should store simulation data in designated directories like `$WOODYHOME` to avoid quota issues in `/home/rrze`.
- Proper data management can alleviate the need for quota increases.

## Actions Taken
- HPC Admin noted that the ticket was incorrectly created.

## Notes
- Ensure users are aware of appropriate storage locations for different types of data to optimize resource usage.
```
---

### 2020031642002392_Increase%20the%20Soft%20quota%20in%20woody.md
# Ticket 2020031642002392

 # HPC Support Ticket: Increase Soft Quota in Woody

## Keywords
- Soft quota
- /home/woody
- /home/saturn
- Quota increase
- Data size warning

## Problem
- **User ID:** mppi043h
- **Issue:** User receives warnings due to large data size and requests an increase in the soft quota for `/home/woody`.

## Solution
- **Action Taken:** HPC Admin increased the user's quota on `/home/woody` to 400GB.
- **Alternative Solution:** Suggested using `/home/saturn` for additional data storage if more space is needed.

## General Learnings
- Users may request quota increases due to large data sizes.
- HPC Admins can increase quotas on specific directories.
- Alternative storage locations can be suggested for additional data needs.

## Follow-up
- Ensure the user is aware of the new quota limit and the alternative storage option.
- Monitor the user's storage usage to prevent future quota issues.
---

### 2023012642001809_Fwd%3A%20iwi5124h%3A%20Soft%20Quota-Limits%20auf%20_home_woody%20erreicht%21.md
# Ticket 2023012642001809

 # HPC Support Ticket Analysis

## Keywords
- Quota Limits
- Soft Quota
- Hard Quota
- /home/woody
- DINO Model
- TinyGPU
- HPC Cluster
- MSN Model
- Inodes
- Best Practice

## Summary
A user received an email notification about reaching the soft quota limit on the `/home/woody` filesystem. The user requested an increase in quota limits due to ongoing work on their master thesis. Additionally, the user reported issues with running the DINO model on TinyGPU due to memory and power limitations and requested access to the HPC cluster.

## Root Cause of the Problem
- The user reached the soft quota limit of 500 GB on the `/home/woody` filesystem.
- The DINO model could not run effectively on TinyGPU due to insufficient memory and power.

## Solution
- **Quota Increase:** The HPC Admin increased the user's quota to 600 GB.
- **Best Practice:** The HPC Admin advised the user to follow best practices for file system usage, providing links to relevant resources.
- **DINO Model Issues:** The HPC Admin requested more details about the issues with the DINO model to provide further assistance.

## Additional Notes
- The user successfully ran the MSN model on the HPC cluster.
- The user was advised to avoid reaching close to 600k inodes to maintain best practices.

## References
- [HPC Café File Systems Presentation](https://hpc.fau.de/files/2022/01/2022-01-11-hpc-cafe-file-systems.pdf)
- [FAU TV Clip on File Systems](https://www.fau.tv/clip/id/40199)

## Next Steps
- Monitor the user's quota usage to ensure compliance with the increased limits.
- Provide further assistance with the DINO model issues based on the additional details provided by the user.
---

### 2016020842004414_Quota%20extension%20_%20mount%20of%20_home_woody.md
# Ticket 2016020842004414

 # HPC Support Ticket: Quota Extension and Mounting /home/woody

## Keywords
- Quota extension
- Home directory
- Mounting HPC systems
- /home/hpc
- /home/vault
- /home/woody
- aycasamba.rrze.uni-erlangen.de

## Summary
- **User Request**: Increase quota for home directory to 20 GB and enable mounting of /home/woody.
- **HPC Admin Response**: Quota increase for /home/hpc is not possible. Mounting /home/woody is not feasible.
- **Follow-up Request**: Increase quota for /home/woody/caph/mpp227 to 250 GB.

## Root Cause
- User requires additional storage space and access to specific directories.

## Solution
- **Quota Increase**: Not possible for /home/hpc. User requested an increase for /home/woody/caph/mpp227 instead.
- **Mounting /home/woody**: Not feasible as per HPC Admin's response.

## General Learnings
- Quota increases are not generally allowed for /home/hpc.
- Mounting specific directories like /home/woody is not supported.
- Users should request quota increases for other available directories if needed.

## Next Steps
- Await HPC Admin's response regarding the quota increase request for /home/woody/caph/mpp227.
- Inform the user about the limitations and alternative options for storage and access.
---

### 42019635_Telefon%20Ticket.md
# Ticket 42019635

 ```markdown
# HPC Support Ticket: Telefon Ticket

## Keywords
- Cluster storage
- Home directory
- Quota increase

## Problem
- User reported that the cluster storage in the home directory is full.
- Requested a callback.

## Solution
- HPC Admin increased the quota for `/home/cluster32` from 10 GB to 50 GB.

## Lessons Learned
- Users may require increased storage quota for their home directories.
- HPC Admins can adjust quotas to accommodate user needs.
```
---

### 42081924_HPC-Kennung.md
# Ticket 42081924

 # HPC Support Ticket: HPC-Kennung

## Keywords
- HPC-Kennung
- Speicherplatz
- Quota
- Strömungssimulationen
- Passwort
- Dienstleistungen

## Summary
- **User Request**: Increase storage quota for HPC account due to large data requirements for simulations.
- **Initial Quota**: 10 GB on filesystem "wnfs1:/srv/home".
- **Requested Quota**: 500 GB.
- **Provided Quota**: Increased to 400/800 GB.

## Root Cause
- Insufficient storage quota for user's simulation needs.

## Solution
- HPC Admin increased the user's quota to 400/800 GB on the filesystem.

## General Learnings
- Users may require larger storage quotas for specific types of simulations.
- HPC Admins can adjust quotas based on user requests and needs.
- Initial account setup may take up to 2 days for services to be fully configured.
- Users should set their passwords through the provided link after account creation.

## Actions Taken
1. HPC Admin created the HPC account (iwst143).
2. User requested an increase in storage quota.
3. HPC Admin adjusted the quota to meet the user's needs.

## Follow-up
- Ensure users are aware of the process to request quota increases.
- Monitor storage usage to anticipate future quota adjustments.

## References
- [IDM Portal](http://www.idm.uni-erlangen.de)
- [RRZE Website](http://www.rrze.uni-erlangen.de)
- [HPC Services](http://www.hpc.rrze.uni-erlangen.de/)
---

### 2019061742001441_Meggie%20Storage%20Problem.md
# Ticket 2019061742001441

 # HPC Support Ticket: Meggie Storage Problem

## Keywords
- Quota limit
- File system
- Small files
- Simulation data
- Efficiency

## Problem Description
- **Root Cause**: User exceeded the file quota limit in the `/lxfs` folder of Meggie due to producing too many small files.
- **Impact**: Inefficient workflow as the user has to run simulations in sets and manually copy data to local storage.

## Solution
- **Immediate Workaround**: User is copying data to local storage to continue simulations.
- **Recommended Solution**:
  - Modify the simulation code to reduce the number of files produced.
  - Consider using an alternative file system like `$WORK` depending on file size.
- **Note**: The quota on the number of files cannot be extended due to the nature of parallel file systems.

## General Learnings
- Parallel file systems are not designed to handle a large number of small files.
- Enforcing file quotas helps maintain system performance.
- Optimizing code to reduce the number of output files is the most efficient solution for quota issues.
- Alternative file systems may be used depending on the specific use case and file size.

## Ticket Status
- Accidentally closed by HPC Admin.
- Reopened and closed with a resolution provided.
---

### 2020022542001298_%28Datei-%29Setup%20f%C3%83%C2%BCr%20eine%20Simulation%20auf%20Meggie.md
# Ticket 2020022542001298

 ```markdown
# HPC-Support Ticket Conversation: File Setup for Simulation on Meggie

## Keywords
- Meggie-Cluster
- Dateisysteme
- $WORK
- $HOME
- $FASTTMP
- MPI-IO
- Quota
- Simulation
- Ergebnisdaten
- Kompilieren

## Summary
A new user of the Meggie-Cluster seeks advice on the best practices for file setup and data management for simulations. The user describes their intended workflow and asks for guidance on where to store source code, compiled binaries, and simulation results. Additionally, the user inquires about the possibility of increasing their quota in $WORK.

## Root Cause of the Problem
- Uncertainty about the appropriate file system to use for different stages of the simulation workflow.
- Concerns about quota limitations in $WORK.

## Solution (if found)
- **Source Code and Compilation**: The user plans to check out source code from git into a folder in $WORK and compile it there. The HPC Admin's response is not provided, but typically, $WORK is suitable for such tasks due to its larger storage capacity compared to $HOME.
- **Simulation Results**: The user considers using $FASTTMP for writing simulation results due to its support for MPI-IO and then moving the data to $HOME/vault or $WORK. Alternatively, writing directly to $WORK is also considered. The HPC Admin's response would clarify the best practice.
- **Quota Increase**: The user inquires about the possibility of increasing their $WORK quota. The HPC Admin's response would provide information on the feasibility and process for quota adjustments.

## General Learnings
- Understanding the appropriate use of different file systems ($WORK, $HOME, $FASTTMP) for various stages of a simulation workflow.
- Considerations for managing large simulation output files and the importance of MPI-IO support.
- The process for requesting and potentially increasing storage quotas in $WORK.

## Next Steps
- Await the HPC Admin's response for specific guidance on file system usage and quota adjustments.
- Document the best practices for file setup and data management for future reference.
```
---

### 2023012542000017_Quota%20Request%20-%20iwb9001h.md
# Ticket 2023012542000017

 # HPC Support Ticket: Quota Request and Data Management

## Keywords
- Quota Increase
- Data Management
- File Deletion
- TFRecord
- Batch Jobs
- NFS Directory
- GPU Memory Limits

## Summary
A user requested a quota increase to accommodate a large dataset and assistance with deleting unrelated data. The HPC admin provided guidance on optimizing data storage and handling, leading to improved performance and a quota extension.

## Root Cause
- User had a large dataset (800 GB) with a high number of small files, causing slow access and high load on file servers.
- User accidentally copied unrelated data and needed assistance to delete it.

## Solution
- **Data Management**: HPC admin suggested repacking individual files into fewer files (e.g., TFRecord) or combining files into tar archives to reduce the number of files accessed during batch jobs.
- **File Deletion**: HPC admin provided commands for the user to delete the unrelated data themselves, as they usually do not delete files from active accounts.
- **Quota Increase**: After the user implemented changes to optimize data storage, the HPC admin increased the quota on `$WORK` to 1 TB.

## Resources
- [HPC Cafe - January 18, 2022](https://hpc.fau.de/teaching/hpc-cafe/)
- [Google Cloud TPU Documentation](https://cloud.google.com/tpu/docs/classification-data-conversion)
- [Dell Optimization Techniques](https://www.dell.com/support/kbdoc/en-us/000124384/optimization-techniques-for-training-chexnet-on-dell-c4140-with-nvidia-v100-gpus)
- [SC20 Technical Poster](https://sc20.supercomputing.org/proceedings/tech_poster/poster_files/rpost142s2-file2.pdf)

## Lessons Learned
- Optimizing data storage by reducing the number of files can significantly improve performance and reduce load on file servers.
- Users should carefully manage their data and consider the impact of their storage methods on system performance.
- HPC admins may provide guidance and resources for users to optimize their data handling but typically do not delete files from active accounts.
---

### 2022021442004098_Quota%20on%20_home_vault_mpt2_shared_.md
# Ticket 2022021442004098

 # HPC Support Ticket: Quota on /home/vault/mpt2/shared/

## Keywords
- Data quota
- Shared directory
- Soft limit
- User quota
- Group quota
- HPC vault

## Summary
A user inquired about the data quota for a shared directory on the HPC vault, believing there was a group-wide quota of several TB. The user received a warning about exceeding the soft limit and sought clarification.

## Root Cause
- Misunderstanding about the quota system for shared directories.
- No specific agreement or group-wide quota for the shared directory.

## Solution
- HPC Admin clarified that there is no group-wide quota for the shared directory.
- Files are tied to individual users regardless of the directory they are stored in.
- User quota was increased to 1TB to prevent immediate issues.

## General Learnings
- Quotas are typically applied to individual users, not shared directories.
- Special quotas for groups are generally implemented for larger storage needs (>50TB).
- Increasing user quota can be a temporary solution to prevent immediate issues.

## Next Steps
- Users should be aware of their individual quotas and manage their data accordingly.
- For larger storage needs, a new group or functional account may be required.
- Users can request quota extensions if necessary.

## References
- HPC Services
- Regionales RechenZentrum Erlangen (RRZE)
- Friedrich-Alexander-Universitaet Erlangen-Nuernberg

---

This report provides a summary of the issue, the root cause, the solution, and general learnings for future reference.
---

### 2018122842000046_Fwd%3A%20Over%20quota%20on%20_home_vault.md
# Ticket 2018122842000046

 ```markdown
# HPC Support Ticket: Over Quota on /home/vault

## Subject
Over quota on /home/vault

## User Issue
- User received frequent messages about being over quota on `/home/vault` after performing a recursive permissions change, including in the `backup2tape` directory.
- User reported seeing only ~500 GB of files, but the quota report showed much higher usage.

## Quota Report
- Blocks used: 2,583,165,600 (= 2583.2G)
- Blocks in doubt: 511,754,240 (= 511.8G)
- Blocks quota soft: 1,048,576,000 (= 1048.6G)
- Blocks quota hard: 2,097,152,000 (= 2097.2G)
- Blocks grace remaining: expired

## HPC Admin Actions
- Temporarily increased the user's quota on `vault` from 1 TB to 3 TB to stop quota emails.
- Investigated the issue further after the holidays.
- Ran `mmcheckquota` to check and correct quota values.
- Identified discrepancies in quota values for multiple users.
- Concluded that the system might need a restart to clean up "ghosts" but decided to leave the increased quota as a workaround until a restart is feasible.

## Root Cause
- The high "in-doubt" value of 500 GB was unusual and indicated potential issues with the quota system.
- The quota values on `vault` were likely corrupted, as evidenced by discrepancies between reported and actual usage.

## Solution
- Temporarily increased the user's quota to stop quota emails.
- Planned to restart the system to clean up "ghosts" and correct quota values.
- Left the increased quota as a workaround until the system restart.

## Keywords
- Quota
- Over quota
- Vault
- Permissions change
- Backup2tape
- mmcheckquota
- Ghosts
- System restart
```
---

### 42130757_Re%3A%20IdM-Self-Service%20email%20address%20confirmation.md
# Ticket 42130757

 ```markdown
# HPC Support Ticket Analysis

## Subject: Re: IdM-Self-Service email address confirmation

### Keywords:
- Quota Increase
- Email Address Confirmation
- HPC Account Management
- University Email Address

### Root Cause:
- User received a warning about exceeding their quota (25 GB) and requested an increase to 200 GB for running simulations.

### Solution:
- HPC Admin increased the user's quota on `/home/woody` to 200 GB.
- User was advised to specify their user account, file system, and use their university email address for future requests.

### General Learnings:
- Importance of specifying user account and file system in quota increase requests.
- Use of university email addresses for official communication.
- Handling quota increase requests efficiently by HPC Admins.

### Notes:
- Ticket was initially misdirected to IdM support but was correctly reassigned to the HPC queue.
- User confirmed the email address change through the IdM Self Service portal.
```
---

### 2024022742001107_disk%20quota%20exceeded%20-%20obwohl%20kaum%20Dateien.md
# Ticket 2024022742001107

 # HPC Support Ticket: Disk Quota Exceeded Despite Low Usage

## Keywords
- Disk quota
- Quota calculation
- Update issues
- VAULT
- SCP

## Problem Description
- User receives "disk quota exceeded" error when attempting to SCP files to VAULT.
- User reports minimal file usage on their drive.

## Quota Information
```
Path              Used     SoftQ    HardQ    Gracetime  Filec
FileQ    FiHaQ    FileGrace
/home/woody          4.0K   500.0G   750.0G        N/A       1
5,000K   7,500K        N/A
/home/hpc           64.6G   104.9G   209.7G        N/A     133K
500K   1,000K        N/A
/home/vault         38.5G  1048.6G  2097.2G        N/A     681
200K     400K        N/A
```

## Root Cause
- Issue with quota calculation after a recent update.

## Solution
- The problem was resolved by the HPC Admins after identifying and fixing the quota calculation issue.
- Users should be able to write to their drives again after the fix.

## Lessons Learned
- Regular updates can sometimes cause temporary issues with quota calculations.
- Users should report such issues promptly to the HPC support team.
- HPC Admins should monitor for and address any post-update issues to ensure smooth operation.

## Next Steps
- If similar issues arise, check for recent updates and verify quota calculations.
- Inform users of any ongoing maintenance or updates that might affect their usage.
---

### 2024083042001153_Remove%20directory%20created%20by%20expired%20user.md
# Ticket 2024083042001153

 ```markdown
# HPC Support Ticket: Remove Directory Created by Expired User

## Keywords
- Storage issues
- Expired user account
- Directory ownership
- Quota allocation
- $HPCVAULT

## Problem
- User unable to remove a large directory created by an expired user.
- User needs permission for another directory created by the same expired user.

## Root Cause
- Directories were created by an expired user, preventing the current user from modifying or deleting them.

## Solution
- **HPC Admin** changed ownership of all files in the specified directory to the current user's account.
- Clarified that quota on $HOME and $HPCVAULT is counted per user, not per directory.

## What Can Be Learned
- Quota allocation is user-specific, not directory-specific.
- Changing ownership of files can resolve permission issues related to expired user accounts.
- HPC Admins can assist with ownership changes and clarify quota policies.
```
---

### 2021030442002911_Over%20quota%20on%20_home_hpc.md
# Ticket 2021030442002911

 # HPC Support Ticket: Over Quota on /home/hpc

## Keywords
- Quota
- Block Quota
- File Quota
- Hard Quota
- Soft Quota
- Grace Period
- Filesystem

## Problem Description
- The user group 'iww1' has exceeded both their block quota and file quota on the `/home/hpc` filesystem.
- Blocks used: 112,022,336 (112.0G)
- Files used: 617,245
- Both block and file hard quotas are set to 0, indicating no additional storage or files can be created.

## Root Cause
- The group has exceeded their allocated storage and file limits, preventing them from saving or creating new files.

## Explanation
- **Block Quota**: Measures the amount of storage space used.
- **File Quota**: Measures the number of files stored.
- **Hard Quota**: Absolute maximum limit that cannot be exceeded.
- **Soft Quota**: Limit that can be temporarily exceeded during the grace period.
- **Grace Period**: One week during which the soft quota can be exceeded.
- **In Doubt**: Temporary uncertainty in usage due to the parallel nature of the filesystem.

## Solution
- The user group needs to delete or archive files to reduce their storage usage below the hard quota limits.
- No specific solution was provided by the HPC Admins in the ticket conversation.

## Action Taken
- The ticket was closed by the HPC Admins without further details on the resolution.

## Learning Points
- Regularly monitor and manage storage usage to avoid exceeding quotas.
- Understand the difference between hard and soft quotas and the grace period.
- Be aware of the 'in doubt' values and their impact on quota limits.

## Next Steps for Similar Issues
- Advise users to clean up their storage by deleting unnecessary files or archiving old data.
- Provide guidance on how to check and manage their quota usage.
- If necessary, assist in requesting additional quota from the HPC Admins.
---

### 2020081142001197_Freikontingent%20Bachelor-_Masterarbeiten.md
# Ticket 2020081142001197

 # HPC Support Ticket: Freikontingent for Bachelor/Master Theses

## Keywords
- Freikontingent
- Bachelorarbeit
- Masterarbeit
- HPC-Cluster
- Kundennummer
- Rechnerergebnisse

## Summary
A user from the Department of Business Mathematics inquired about the availability of a free quota (Freikontingent) for producing computational results on the HPC cluster for Bachelor and Master theses. The user also asked whether they should use their existing customer number for this purpose.

## Root Cause
The user needed clarification on the availability of a free quota for thesis work and the appropriate customer number to use.

## Solution
The HPC Admin confirmed that there is a free quota available for thesis work and that the existing customer number (mpwm102) should be used.

## What Can Be Learned
- There is a free quota available for Bachelor and Master theses.
- Existing customer numbers can be used for thesis work.
- Quick confirmation from HPC Admins can resolve such queries efficiently.

## Follow-Up
No further action required from the user or the HPC Admin. The user acknowledged the response and thanked the HPC Admin for the quick reply.
---

### 2019073142000119_Question%20on%20the%20email%20of%20HPC%20Quota%20Checker.md
# Ticket 2019073142000119

 # HPC Support Ticket: Quota Exceeded Due to Trash Folder

## Keywords
- HPC Quota Checker
- Trash Folder
- NoMachine
- Command Line Deletion

## Root Cause
- User copied a large folder (Star CCM+) to their home directory, exceeding their quota.
- User moved the folder to the trash but did not delete it, causing the quota to remain exceeded.

## Solution
- **Explanation**: Moving files to the trash does not instantly delete them; they still count towards the quota.
- **Action**: Empty the trash folder to free up space.
  - **Location**: The trash folder can usually be found on the Desktop or in any file explorer window.
  - **Command Line**: Delete the folder `/home/hpc/[username]/.local/share/Trash`.

## General Learnings
- **Quota Management**: Understand that moving files to the trash does not free up quota space.
- **Deletion**: To free up space, files must be permanently deleted, not just moved to the trash.
- **Command Line Usage**: Familiarize with command line operations for file management.

## Ticket Flow
1. **User**: Reported receiving quota exceeded emails after moving a large folder to the trash.
2. **HPC Admin**: Explained that files in the trash still count towards the quota and provided instructions to delete the trash folder.
3. **User**: Attempted to delete the trash folder but encountered issues.
4. **HPC Admin**: Provided the correct path for the trash folder and confirmed the user successfully deleted the files.

## Conclusion
- Ensure users understand the difference between moving files to the trash and permanently deleting them to manage their quota effectively.
- Provide clear instructions for locating and deleting the trash folder via both GUI and command line.
---

### 2018092042000138_Increase%20of%20quota%20on%20%24WOODYHOME%20-%20mpt407.md
# Ticket 2018092042000138

 # HPC Support Ticket: Increase of Quota on $WOODYHOME

## Keywords
- Quota Increase
- Storage Limit
- GPU Cluster
- AMBER Calculations
- NFS Storage

## Problem
- User running parallel calculations on a GPU cluster with limited storage (200 GB).
- Calculations exceed storage capacity within 24 hours.
- Unable to transfer data to local machine due to insufficient quota.
- Restarting calculations is not feasible due to increased output file sizes.

## Root Cause
- Insufficient storage quota for running multiple parallel calculations.

## Solution
- **Temporary Fix**: HPC Admins increased the user's quota to 250/500 GB.
- **Long-term Solution**: Suggested participation in the purchase of a large HPC-NFS storage.
  - Offer: 25 TB for a one-time payment of 5000 EUR or 10 TB for 2500 EUR.
  - Storage accessible from all HPC systems with similar properties to $WOODYHOME.
  - No backup or snapshots planned.
  - Interested groups should provide feedback by mid-September.

## General Learnings
- Communicate storage expansion options to users and research groups.
- Monitor and adjust quotas based on user needs and system capacity.
- Encourage users to plan for long-term storage solutions.

## Related Teams
- HPC Admins
- 2nd Level Support Team
- Datacenter Head
- Training and Support Group Leader
- NHR Rechenzeit Support
- Software and Tools Developers
---

### 2023053042000812_Speicherplatz%20f%C3%83%C2%BCr%20Modelle%20erh%C3%83%C2%B6hen.md
# Ticket 2023053042000812

 # HPC Support Ticket: Increase Storage Space for Models

## Keywords
- Storage space
- $HPCVAULT
- $WORK
- Quota
- Backup

## Problem
- User requires more storage space for models.
- Current storage space is 500GB, needs to be increased to 1TB.
- Models are stored in $HPCVAULT.

## Root Cause
- Insufficient storage space for multiple versions of models in various conversions.

## Solution
- Use $WORK directory (`/home/autin/...`) for additional storage.
- Default quota for $WORK is 10TB.
- No backup is provided for $WORK.

## General Learnings
- Always direct support requests to the official support email (`hpc-support@fau.de`) for timely responses.
- $WORK directory offers more storage space but does not include backup services.
- Administrators can guide users to appropriate storage solutions based on their needs.

## Actions Taken
- User was advised to use $WORK for additional storage.
- Ticket was closed after the user acknowledged the solution.

## Roles Involved
- HPC Admins
- 2nd Level Support Team
- Head of the Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support
- Software and Tools Developer
---

### 2019061842000351_Auskunft%20%C3%83%C2%BCber%20Ressourcen%20am%20RRZE.md
# Ticket 2019061842000351

 # HPC-Support Ticket Conversation Analysis

## Keywords
- HPC Resources
- Storage Systems
- iPAT
- RRZE
- Speicherplatz
- Rechenzeit
- Quota
- Exclusive Use

## General Learnings
- Understanding the allocation and usage of HPC resources.
- Identifying financed and utilized storage systems.
- Determining the exclusivity of storage space.
- Analyzing user-specific storage usage.

## Ticket Summary
- **User Request**: Information about HPC resources at RRZE, specifically:
  - Devices and storage systems financed by iPAT.
  - Storage systems used by iPAT.
  - Utilization and available space in general and iPAT-specific systems.
  - Exclusivity of storage space.
- **HPC Admin Response**:
  - Provided details on iPAT's financial contributions and storage usage.
  - Listed storage systems and their current utilization by iPAT.
  - Clarified the exclusivity of certain storage spaces.
  - Provided a detailed breakdown of storage usage by specific users on Emmy and Meggie clusters.

## Root Cause of the Problem
- User needed detailed information on HPC resources for planning infrastructure expansions.
- Concerns about excessive storage usage by iPAT users.

## Solution
- HPC Admin provided comprehensive information on:
  - Financial contributions and storage systems financed by iPAT.
  - Current storage usage and available space.
  - Exclusivity of storage spaces.
  - Detailed storage usage by top users on Emmy and Meggie clusters.

## Detailed Information
- **Financed Devices and Storage Systems**:
  - 2018/2019: SATURNHOME, 25 TB for 5000€.
  - 2017: Participation in woody nodes, 8000€.
  - 2014/2015: Repurposing funds for hard drives (3000€) from a project into tapes, increasing quota on /home/vault.
- **Storage Systems Used by iPAT**:
  - /home/hpc: Quota per user 10GB, currently 66 GB used by iPAT.
  - /home/vault: Standard quota per user 100GB, currently ~300 GB used by iPAT (excluding tape data).
  - Tape: Currently ~80 TB used by iPAT.
  - /home/woody: Standard quota per user 200GB, currently 1.3TB used by iPAT.
  - /home/saturn (financed): Group quota 25TB, exclusively usable, currently 21.8TB used by iPAT.
  - Parallel filesystem emmy: Total size 430TB, not exclusively usable, currently 169.2TB used by iPAT (40% of total capacity).
  - Parallel filesystem meggie: Total size 850TB, not exclusively usable, currently 185.4TB used by iPAT (22% of total capacity).
- **Top Users Storage Usage**:
  - **Emmy**:
    - 58TB: User 1
    - 46TB: User 2
    - 35TB: Deleted User
    - 8.6TB: User 3
    - 7.0TB: User 4
  - **Meggie**:
    - 76TB: User 5
    - 55TB: User 3
    - 40TB: Deleted User
    - 11TB: User 6

## Conclusion
- The HPC Admin provided detailed and comprehensive information addressing all aspects of the user's request.
- The user was satisfied with the quick and detailed response.
- The ticket was closed as resolved.
---

### 2018061442000468_Vault%20quota.md
# Ticket 2018061442000468

 ```markdown
# HPC-Support Ticket: Vault Quota

## Keywords
- Vault quota
- Soft quota
- Hard quota
- Storage limit
- MD simulations
- AMBER
- Production runs

## Summary
A user has reached their storage quota limit while running molecular dynamics (MD) simulations with AMBER and requests an increase in their vault quota.

## Root Cause
- The user's current storage allocation (104.9G soft quota, 209.7G hard quota) is insufficient for their simulation needs.

## Solution
- The user requests an increase in their vault quota to accommodate longer simulation runs.

## General Learning
- Users running extensive simulations, such as MD with AMBER, may require higher storage quotas.
- Monitoring and adjusting storage quotas based on user needs is essential for smooth operation.

## Next Steps
- HPC Admins should evaluate the user's request and adjust the storage quota if appropriate.
- Consider implementing a process for users to easily request and justify quota increases.
```
---

### 2017082942002105_Quota-Fehlermeldung%20cshpc.md
# Ticket 2017082942002105

 ```markdown
# HPC Support Ticket: Quota Error Message on cshpc

## Keywords
- Quota
- Grace period
- Filesystem
- Error message
- Parsing issue

## Summary
A user reported an error message related to quota limits on the new cshpc system. The error indicated that the user was over quota on at least one filesystem and included a parsing issue with the grace period.

## Root Cause
The error was due to the grace period being displayed in hours instead of days, which caused a parsing issue in the `shownicerquota.pl` script.

## Solution
The HPC Admin fixed the parsing issue in the script, which resolved the error message. However, the user still needed to delete additional data to comply with the quota limits.

## What Can Be Learned
- **Quota Management**: Understanding how quota limits and grace periods are displayed and managed is crucial for troubleshooting similar issues.
- **Script Parsing**: Ensure that scripts handling quota information can correctly parse different formats of grace periods (days vs. hours).
- **User Communication**: Clearly communicate to users the status of their quota and any actions they need to take to resolve over-quota situations.

## Additional Notes
- The user was able to see the complete quota information on the `meggie` system but not on the `cshpc` system during login.
- The HPC Admin acknowledged that similar issues might arise in the future due to the complexity of parsing quota information.
```
---

### 2025020542003252_Trying%20to%20read%20and%20write%20on%20HPC.md
# Ticket 2025020542003252

 ```markdown
# HPC Support Ticket: Trying to Read and Write on HPC

## Subject
Trying to read and write on HPC

## Keywords
- Read-and-write access
- File system
- Quota
- Permissions
- Deleting folders

## Problem Description
The user is experiencing issues with read-and-write access on the HPC system "woody." Specifically, the user is unable to delete folders.

## Troubleshooting Steps
1. **Check Quota**: The HPC Admin suggested using `shownicerquota.pl` to check the user's data and file quota.
2. **Identify File System**: The HPC Admin asked for clarification on which file system and frontend node of Woody the user is referring to.
3. **Check Permissions**: The HPC Admin advised using `ls -l` to list files with their permissions.

## Root Cause
The user is above the quota on `/hpc/home/`.

## Solution
- **Move Conda Environments**: The user should read the documentation on Conda and move the environments to `$work` to free up space in the home directory.

## General Learnings
- **Quota Management**: Users should regularly check their quota to avoid issues with read-and-write access.
- **File Permissions**: Understanding and managing file permissions is crucial for proper file operations.
- **Documentation**: Users should refer to the documentation for best practices and guidelines on managing their environment.
```
---

### 2018101042000298_Quota%20Vault.md
# Ticket 2018101042000298

 # HPC Support Ticket: Quota Vault

## Keywords
- Quota
- Vault
- Storage Volume
- CFD Simulations
- Data Analysis
- Paper
- Thesis

## Summary
A user is experiencing difficulties due to insufficient storage quota for their CFD simulations. The large mesh size of the simulations has nearly filled the user's vault storage, making data analysis cumbersome and time-consuming. The user requests an increase in quota to facilitate the analysis of data for upcoming papers and thesis work.

## Root Cause
- Insufficient storage quota for large CFD simulation data.

## Solution
- The user has requested an increase in storage quota to handle the large volume of data generated by CFD simulations.

## General Learning
- Large-scale simulations, such as CFD, can quickly consume storage quota.
- Users nearing the end of their academic projects may require additional storage for data analysis.
- Proactive management of storage quotas can prevent delays in research and data analysis.

## Next Steps
- HPC Admins should evaluate the user's request and determine if an increase in storage quota is feasible.
- If approved, the quota should be increased to accommodate the user's needs.
- Communicate the decision and any necessary steps to the user.

## Additional Notes
- Ensure that users are aware of storage management best practices to optimize their quota usage.
- Regularly review and adjust storage quotas based on user needs and system capacity.
---

### 2024101042001623_Storage%20Usage%20Discrepancy%20in%20%24HPCVAULT.md
# Ticket 2024101042001623

 # Storage Usage Discrepancy in $HPCVAULT

## Keywords
- Storage usage
- $HPCVAULT
- `du -h`
- `ll -h`
- File system discrepancy

## Problem Description
A user noticed a significant discrepancy in the reported storage usage in their $HPCVAULT directory. The `du -h` command showed a total used space of 5.4T, while manually calculating the sizes of individual files using `ll -h` resulted in approximately 2.8T.

## Root Cause
The discrepancy is caused by an issue described in the FAQ:
"[Why is my data taking up twice as much space on the file systems?](https://doc.nhr.fau.de/faq/#why-is-my-data-taking-up-twice-as-much-space-on-the-file-systems)"

## Solution
Refer to the FAQ for detailed information on why this discrepancy occurs and how to address it.

## General Learning
- Understand the differences between `du -h` and `ll -h` in reporting storage usage.
- Be aware of potential file system issues that can cause discrepancies in reported storage usage.
- Use FAQs and documentation to troubleshoot common issues.

## Roles Involved
- **HPC Admins**: Provide support and guidance.
- **2nd Level Support Team**: Assist in resolving technical issues.
- **User**: Reports the problem and seeks assistance.
---

### 2023091442003771_Frequently%20Exceeding%20my%20Disk%20Quota%20on%20CSHPC.md
# Ticket 2023091442003771

 # HPC Support Ticket: Frequently Exceeding Disk Quota on CSHPC

## Keywords
- Disk Quota
- $HOME
- $HPCVAULT
- $WORK
- Network Filesystems
- Storage Documentation

## Problem
- User frequently exceeds disk quota.
- Requests an increase in available disk space.

## Root Cause
- Misunderstanding of disk quota and available storage options.

## Solution
- **No Quota on CSHPC**: The system uses network filesystems mounted on all servers.
- **$HOME Quota**: No quota increase available for $HOME.
- **Alternative Storage**: Use $HPCVAULT and $WORK for additional space.
- **Documentation**: Refer to [HPC Storage Documentation](https://hpc.fau.de/systems-services/documentation-instructions/hpc-storage/) for more information.

## General Learnings
- Understand the storage structure and available options.
- Utilize alternative storage locations for larger data sets.
- Refer to documentation for detailed information on storage management.
---

### 2023033042003181_Space%20auf%20Vault%20f%C3%83%C2%BCr%20Job-Archiv.md
# Ticket 2023033042003181

 # HPC Support Ticket: Space auf Vault für Job-Archiv

## Keywords
- Vault
- Job Archiv
- Cron Job
- Sicherung
- Quota
- Totalausfall
- Tina Backup
- Tape Migration

## Problem
- User requested additional storage space on Vault to secure job archives via a Cron Job.
- Current backup strategy involves storing backups on the same host, which is not optimal.
- Automatic migration to tape is no longer available.

## Root Cause
- Insufficient storage space on Vault for additional job archive backups.

## Solution
- HPC Admin increased the user's quota on Vault to 1TB.

## General Learnings
- Users may request additional storage for backup purposes, especially after experiencing system failures.
- It is important to provide adequate storage space for critical backups to ensure data redundancy and system recovery.
- Communication about changes in backup strategies (e.g., discontinuation of tape migration) is crucial for users to plan their backup solutions effectively.

## Follow-up Actions
- Monitor the user's storage usage on Vault to ensure it remains within the allocated quota.
- Periodically review and update backup strategies to align with current infrastructure and user needs.
---

### 2023013142003164_Quota-Anpassung%20EmpkinS-User.md
# Ticket 2023013142003164

 # HPC Support Ticket: Quota Increase Request

## Keywords
- Quota Increase
- User Account
- Storage Allocation
- HPC Admin
- FAU

## Summary
A user requested an increase in storage quota for a specific user account. The HPC Admin processed the request and confirmed the new quota allocation.

## Problem
- **Root Cause**: User required additional storage space for their HPC account.

## Solution
- **Action Taken**: HPC Admin increased the quota for the specified user account to 10 TB.
- **Result**: The total allocated quota for the group is now 83 TB out of 100 TB.

## Details
- **Request**: Increase quota for user account `empk013h` to 10 TB.
- **Response**: Quota increased successfully. Current allocations are:
  - `empk013h` - 10 TB
  - `wso049h` - 3 TB
  - `empk004h` - 70 TB

## General Learning
- **Process**: Users can request quota increases via support tickets.
- **Admin Role**: HPC Admins handle quota adjustments and confirm the changes.
- **Communication**: Clear and concise communication between users and HPC Admins ensures efficient resolution of requests.

## Documentation Note
This ticket serves as a reference for handling quota increase requests and the process involved in adjusting storage allocations for user accounts.
---

### 2023091442002754_Platzverbrauch%20im%20SFB%20EmpkinS.md
# Ticket 2023091442002754

 ```markdown
# HPC-Support Ticket: Platzverbrauch im SFB EmpkinS

## Keywords
- Storage usage
- Reporting
- `du -sh` command
- HPC cluster
- SFB Speicherplatz

## Problem
- User needs to report on storage usage for internal purposes.
- User manages subdirectories under `/home/vault/empkins` but lacks access to view detailed data.
- Requests output of `du -sh /home/vault/empkins` to understand storage usage.

## Solution
- HPC Admin provided the output of `du -sh /home/vault/empkins/*`:
  ```
  3.4T    /home/vault/empkins/tpA
  512    /home/vault/empkins/tpB
  367G    /home/vault/empkins/tpC
  28T    /home/vault/empkins/tpD
  512    /home/vault/empkins/tpE
  68K    /home/vault/empkins/tpZ
  ```
- User confirmed that the provided information was sufficient for their needs.

## Lessons Learned
- Users may require storage usage reports for internal reporting.
- The `du -sh` command is useful for summarizing disk usage.
- HPC Admins can assist by providing necessary command outputs when users lack access.

## Root Cause
- User lacked access to detailed storage usage information for reporting purposes.

## Resolution
- HPC Admin provided the required storage usage information using the `du -sh` command.
```
---

### 2022032842001492_over%20quota%20issue.md
# Ticket 2022032842001492

 # Over Quota Issue

## Keywords
- Over quota
- Home folder
- Jupyter notebook
- Trash folder

## Summary
A user reported receiving over quota emails for their home folder despite not having any files in it. Their Jupyter notebook also stopped working.

## Root Cause
The user's `~/.local/share/Trash` folder contained about 90GB of data, causing the home folder to exceed its quota.

## Solution
The HPC Admin identified the large Trash folder as the cause of the issue. The user should empty their Trash folder to free up space and resolve the over quota issue.

## General Learnings
- Check hidden folders and trash folders when investigating over quota issues.
- Large trash folders can cause over quota issues and affect application performance (e.g., Jupyter notebook).
- Regularly empty trash folders to prevent unnecessary storage usage.
---

### 2017032142001102_Speichererweiterung.md
# Ticket 2017032142001102

 # HPC Support Ticket: Speichererweiterung

## Keywords
- Speichererweiterung
- Quota
- Deep Learning
- Input Files
- Woody
- HPC

## Problem
- User requires more storage space for deep learning input files.
- Current storage is insufficient for 350GB input files that need to be stored twice.
- User requests an increase to 800GB, but would accept 400GB.
- Minimum requirement is 150GB available space.

## Solution
- HPC Admin increased the user's quota on `/home/woody` to 800GB with a hard limit of 1600GB.

## General Learnings
- Users may require additional storage for large input files, especially in fields like deep learning.
- HPC Admins can adjust quotas to accommodate user needs.
- Effective communication of current limitations and requirements is crucial for timely support.

## Root Cause
- Insufficient storage space for large input files required for deep learning projects.

## Resolution
- Increased quota on `/home/woody` to 800GB/1600GB to meet the user's storage needs.
---

### 2023052842000246_You%20are%20over%20quota%20on%20at%20least%20one%20filesystem%21.md
# Ticket 2023052842000246

 # HPC Support Ticket: Over Quota on Filesystem

## Keywords
- Quota exceeded
- Filesystem
- Trash folder
- File quota
- Data volume quota

## Problem Description
- User unable to create new files due to quota exceeded error on `/home/hpc`.
- User reports having only ~300 MB of data in their directory.

## Root Cause
- Trash folder (`/home/hpc/iwb3/iwb3006h/.local/share/Trash`) exceeding data volume quota.

## Solution
- Inform user about the trash folder exceeding quota.
- Provide general tips on quota management:
  - Quota restricts both data volume and the number of files.
  - Soft quota for files on `/home/hpc` is 500K, hard quota is 1M.
  - Offer multiple file systems to move data to ([HPC Storage Documentation](https://hpc.fau.de/systems-services/documentation-instructions/hpc-storage/)).
  - Advise against huge piles of small files for better file system performance ([FAQ Entry](https://hpc.fau.de/faqs/#innerID-13955)).

## Follow-up
- User expressed gratitude for the quick response and resolution.
- Ticket closed as the user was highly satisfied.

## General Learnings
- Always check trash folders when diagnosing quota issues.
- Educate users about file quotas and the impact of small files on performance.
- Provide relevant documentation and FAQs for user self-help.
---

### 42200892_Request%20of%20increasing%20quota%20on%20vault.md
# Ticket 42200892

 ```markdown
# HPC Support Ticket: Request of Increasing Quota on Vault

## Keywords
- Storage quota
- OpenFOAM
- Soft quota limit
- /home/vault

## Problem
- User reached the soft quota limit on their storage directory (`/home/vault/iwc1/iwc1138/`).
- Simulation cases with OpenFOAM are large, causing the user to quickly reach the quota limit.

## Root Cause
- Insufficient storage quota allocated to the user's directory.

## Solution
- HPC Admin increased the storage quota to 250 GB.

## Lessons Learned
- Users running large simulations may require higher storage quotas.
- Regularly monitor and adjust storage quotas based on user needs.
- Ensure proper communication and follow-up on ticket status to avoid premature closure.
```
---

### 2025012242001198_erroneous%20user%20placement%20under%20my%20group%20account%20gwgi102.md
# Ticket 2025012242001198

 # HPC Support Ticket: Erroneous User Placement

## Keywords
- User account management
- Group account management
- Disk quota
- Data migration
- HPC portal

## Summary
A user was erroneously assigned to the wrong group account, leading to significant disk space usage and quota issues for the incorrectly assigned group.

## Root Cause
- User "gwgi019h" was mistakenly placed under group account "gwgi102" instead of the intended group account under Thomas Mölg.
- This resulted in excessive disk space usage (1/3 of the quota) for the wrong group, limiting other group members and projects.

## Solution
1. **Temporary Quota Increase**: The quota for the affected group (gwgi102) was increased by 25 TB to mitigate immediate issues.
   - Old quota: 125 TB
   - New quota: 150 TB

2. **Account Reassignment**: The user account was reassigned in the HPC portal to the correct group (gwgk102) to allow proper account management by the intended group leader.

3. **Data Migration Consideration**: Due to the significant amount of data (over 43 TB) and different storage locations (saturn vs. titan), a full data migration was deemed impractical. The account was moved within the HPC portal to avoid complex data transfer operations.

## Lessons Learned
- **Accurate User Assignment**: Ensure accurate user assignment to the correct group during account creation to avoid such issues.
- **Quota Management**: Temporarily increasing the quota can be a quick solution to alleviate immediate storage constraints.
- **Portal Management**: Reassigning accounts within the HPC portal can be a practical solution to avoid complex data migration processes.

## Next Steps
- Monitor the situation to ensure the temporary quota increase is sufficient.
- Consider long-term solutions for data migration if necessary.

## References
- HPC Admin internal discussions
- HPC portal account management
- Disk quota management tools
---

### 2024022742003687_Re%3A%20Over%20quota%20on%20_home_hpc%20-%20iwia047h.md
# Ticket 2024022742003687

 # HPC Support Ticket: Over Quota on /home/hpc

## Keywords
- Quota warning
- Hidden folders
- Grace period
- Block quota
- Filesystem
- Parallel filesystem
- Cache folder

## Summary
A user received quota warning emails despite freeing up memory in their `/home/hpc` directory. The issue affected their interactive work in the cluster, such as auto-saving and opening files and notebooks.

## Root Cause
- The user's screenshot did not show hidden folders, which contained a significant amount of data (42G in `.cache`).
- The filesystem's parallel nature caused 'in doubt' values, leading to uncertainty in the exact usage.

## Solution
- HPC Admins identified the hidden `.cache` folder as the source of excess data.
- The user was advised to delete files from the `.cache` folder to free up space.
- It was noted that it may take a few seconds for the internal database to update after deleting a large chunk of data.

## General Learnings
- Always check hidden folders when investigating quota issues.
- Understand that parallel filesystems may have 'in doubt' values, which can cause discrepancies in reported usage.
- After deleting files, allow some time for the filesystem to update and reflect the changes.
- Users may experience issues with interactive work in the cluster when over quota.
---

### 2022090742000913_shownicerquota%20problem.md
# Ticket 2022090742000913

 # HPC Support Ticket: shownicerquota Problem

## Keywords
- `shownicerquota.pl`
- `quota -s`
- Disk quota
- $HOME
- $WORK
- $VAULT
- Script update
- Quota limits

## Problem Description
- User unable to see disk quota for $VAULT using `shownicerquota.pl` and `quota -s`.
- User exceeding disk quota but cannot determine by how much.

## Root Cause
- Script broken due to recent updates.

## Solution
- HPC Admin provided current quota manually.
- Quota details for $HOME, $WORK, and $VAULT were shared.

## Lessons Learned
- Script updates can break existing functionalities.
- Manual intervention may be required to provide users with necessary information.
- Importance of monitoring and testing scripts post-update.

## Next Steps
- Fix the script to display quota for all filesystems ($HOME, $WORK, $VAULT).
- Test the script thoroughly after updates to ensure all functionalities are intact.

## Relevant Snippet
```
Filesystem Fileset    type    blocks  quota   limit   in_doubt grace |    files quota   limit in_doubt grace Remarks
hpcdatacloud hpchome   USR     33.59G   50G    100G        0   none |    32449 500000 1000000       0   none
hpcdatacloud vault     USR     9.698G  500G   1000G        0   none |    13842 200000  400000       0   none
woody  userused@iwal044h  353G
woody  userquota@iwal044h 477G
```
---

### 2018072442001606_sudo%20installation%20denied.md
# Ticket 2018072442001606

 # HPC Support Ticket: sudo installation denied

## Keywords
- sudo privileges
- cuDNN installation
- tar file
- quota request

## Problem
- User unable to install cuDNN due to lack of superuser privileges.
- User requires additional storage quota for dataset and intermediate results.

## Root Cause
- cuDNN installation requires superuser privileges which the user does not have.
- Insufficient storage quota for the user's deep learning setup.

## Solution
- **cuDNN Installation**: HPC Admin suggested using a tar version of the cuDNN files, which can be extracted without elevated privileges.
- **Storage Quota**: User requested additional quota, but the resolution is not provided in the given conversation.

## General Learnings
- Always look for alternative installation methods that do not require superuser privileges.
- Communicate clearly about storage quota needs for large projects.

---

**Note**: The resolution for the storage quota request is not provided in the given conversation. Further follow-up would be needed to determine the outcome.
---

### 2019103142000452_Archiv.md
# Ticket 2019103142000452

 # HPC Support Ticket: Archiv

## Keywords
- Data transfer
- Quota increase
- Manual migration
- Automatic migration rules
- HSM (Hierarchical Storage Management)
- Tape storage

## Summary
- **User Request:** Manual trigger for data transfer from `/home/vault` to tape storage and quota increase.
- **HPC Admin Response:** Manual trigger only possible server-side. Automatic migration rules can be set up. Quota increase granted with limitations due to system age.

## Root Cause
- User needs to manually trigger data migration and requires higher storage quota.

## Solution
- **Manual Migration:** Not possible by the user; only by HPC Admin.
- **Automatic Migration Rules:** Can be set up by HPC Admin (e.g., migrate files after 2 days).
- **Quota Increase:** Granted with limitations due to system constraints.

## General Learnings
- Manual data migration to tape storage is restricted to server-side operations.
- Automatic migration rules can be configured to manage data transfer based on specific criteria.
- Quota increases may be limited by system age and available storage.
- Future systems may not support HSM, impacting data migration capabilities.

## Notes
- The current system's primary purpose is not archiving, and future systems may lack HSM components.
- Users should be aware of storage limitations and plan accordingly.
---

### 2022082542001881_Fritz%3A%20Speicherquota%20%2B%20Fehlermeldung.md
# Ticket 2022082542001881

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject: Fritz: Speicherquota + Fehlermeldung

### User Issues:
1. **Disk Quota Exceeded**:
   - User is facing issues with both soft and hard disk quotas.
   - Large file sizes generated by VASP, especially for long trajectories, are causing quota overruns.
   - User requests an increase in quota.

2. **Job Failures**:
   - Some VASP jobs are failing with the error message "forrtl: No space left on device".
   - The issue is sporadic and not related to quota limits.

### HPC Admin Responses:
1. **Quota Increase**:
   - HPC Admin increased the user's quota on `/home/vault` from 500 GB to 3 TB.

2. **Job Failure Diagnosis**:
   - HPC Admin requested job IDs for further diagnosis.
   - No specific issues were found on the nodes, but the admin requested more job IDs for ongoing monitoring.

### Additional User Issues:
1. **Missing Directory**:
   - User moved directories between personal vault and project workspace, resulting in a missing directory.
   - HPC Admin suggested checking the snapshot directory for recovery.

2. **Job Completion Issues**:
   - User reported jobs marked as COMPLETED but not actually finished.
   - No error messages were present in the output.
   - HPC Admin closed the ticket as it was handled in a separate ticket.

### Solutions and Recommendations:
1. **Quota Management**:
   - Users should regularly monitor and manage their disk usage.
   - Request quota increases if necessary, providing details on the specific file system.

2. **Job Failure Troubleshooting**:
   - Provide job IDs for failed jobs to assist HPC Admins in diagnosing the issue.
   - Check node-specific logs and error messages for more detailed troubleshooting.

3. **Data Recovery**:
   - Use snapshot directories to recover lost or missing data.
   - Example path: `/home/vault/b146dc/b146dc11/work/Masterarbeit/.snapshots/@GMT-2023.06.09-01.00.00/`

4. **Job Completion Verification**:
   - Verify job completion by checking the output files and logs.
   - Report any discrepancies to HPC Support for further investigation.

### General Learnings:
- Regularly monitor disk usage and manage quotas.
- Provide detailed information, such as job IDs, for effective troubleshooting.
- Utilize snapshot directories for data recovery.
- Verify job completion by checking output files and logs.
```
---

### 2018120842000093_Quota%20on%20vault%20-%20mpt4009h.md
# Ticket 2018120842000093

 # HPC Support Ticket: Quota on vault

## Keywords
- Quota
- Vault
- Archive
- Storage
- Tape migration

## Summary
- **User Request**: Request for additional storage space on vault.
- **HPC Admin Response**: Vault is primarily an archive directory. Large files (>>10GB) that are not accessed for a long time are migrated to tape and do not count towards the quota.

## Root Cause
- User requires additional storage space on vault.

## Solution
- Inform the user that vault is primarily for archiving. Large files that are not accessed frequently will be migrated to tape, freeing up quota space.

## General Learnings
- Understand the purpose of vault as an archive directory.
- Large, inactive files are migrated to tape to optimize storage usage.
- Users should be aware of the quota system and how it is managed.

## Actions Taken
- HPC Admin explained the purpose of vault and the tape migration process.

## Next Steps
- Monitor user's understanding and compliance with the vault's intended use.
- Provide additional guidance if the user continues to require more storage space.
---

