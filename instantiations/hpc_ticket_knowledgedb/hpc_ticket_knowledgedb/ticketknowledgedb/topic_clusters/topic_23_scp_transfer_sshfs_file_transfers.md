# Topic 23: scp_transfer_sshfs_file_transfers

Number of tickets: 37

## Tickets in this topic:

### 2023021442001099_Re%3A%20%5BEXT%5D%20Re%3A%20%5BNHR%40FAU%5D%20Downtime%20of%20all%20NHR%40FAU%20HPC%20systems%20on%2.md
# Ticket 2023021442001099

 # HPC Support Ticket Conversation Summary

## Keywords
- Downtime
- SCP file transfer
- Hostname resolution
- FAU Network
- HPC clusters
- Power grid maintenance

## General Learnings
- **Downtime Notification**: HPC Admins notify users about scheduled downtimes via email, including the reason and duration.
- **File Transfer**: Users may encounter issues with file transfers using SCP due to incorrect hostnames.
- **Hostname Resolution**: The hostname to be used for file transfer depends on the network the client is located in.

## Root Cause of the Problem
- User attempted to transfer files using SCP with an incorrect hostname (`b165da15@fritz4`), leading to hostname resolution failure.

## Solution
- **Correct Hostnames**:
  - Use `fritz4.nhr.fau.de` when within the FAU Network.
  - Use `cshpc.rrze.fau.de` when accessing from anywhere else in the world.
- **Documentation**: Refer to the official documentation for detailed instructions on clusters and HPC storage:
  - [Fritz Cluster Documentation](https://hpc.fau.de/systems-services/documentation-instructions/clusters/fritz-cluster/)
  - [HPC Storage Documentation](https://hpc.fau.de/systems-services/documentation-instructions/hpc-storage/)

## Additional Notes
- **Downtime Details**: The downtime was scheduled for power grid maintenance at the RRZE building. Jobs colliding with the downtime would be postponed.
- **Service Interruptions**: Frontends and fileservers would be available most of the time, but some service interruptions were expected.

This summary can be used as a reference for support employees to address similar issues in the future.
---

### 2024060742002664_sshfs%20mounting%20does%20not%20work.md
# Ticket 2024060742002664

 # HPC-Support Ticket: sshfs Mounting Does Not Work

## Keywords
- sshfs
- ssh
- debug
- connection closed
- mounting
- remote host disconnected

## Problem Description
The user is unable to mount a remote directory using `sshfs` despite successful SSH connections. The `sshfs` command closes the connection immediately after authentication.

## Debug Output Analysis
- **SSHFS Version**: 3.7.1
- **SSH Connection**: Successful authentication using public key.
- **Error**: Remote host disconnects after authentication.
- **Log Details**:
  - Connection established and authenticated using public key.
  - Sending subsystem: sftp.
  - Remote host disconnects with exit status -1.

## Root Cause
The root cause of the problem is not immediately clear from the provided debug output. The connection is successfully established and authenticated, but the remote host disconnects during the SFTP subsystem initialization.

## Troubleshooting Steps
1. **Compare SSH Logs**: Request the user to provide a similar debug log for a normal SSH login to compare the behavior.
2. **Check SSH Agent**: Verify if the user has an SSH agent running locally.
3. **Simplify Command**: Try the `sshfs` command without additional options to isolate the issue.
   ```bash
   sshfs csnhr.nhr.fau.de:/home/hpc/hmai/hmai111h ./<myfolder>
   ```

## Solution (if found)
No solution was provided in the initial conversation. Further investigation is required to identify the root cause and resolve the issue.

## Next Steps
- Analyze the SSH debug log for normal login.
- Check for any differences in the SSH and `sshfs` configurations.
- Consult with the 2nd Level Support team for additional troubleshooting if needed.

## References
- [Mounting Documentation](https://doc.nhr.fau.de/data/mounting/)

## Support Team
- **HPC Admins**: Thomas, Michael Meier, Anna Kahler, Katrin Nusser, Johannes Veh
- **2nd Level Support**: Lacey, Dane (fo36fizy), Kuckuk, Sebastian (sisekuck), Lange, Florian (ow86apyf), Ernst, Dominik (te42kyfo), Mayr, Martin
- **Datacenter Head**: Gerhard Wellein
- **Training and Support Group Leader**: Georg Hager
- **NHR Rechenzeit Support**: Harald Lanig
- **Software and Tools Developers**: Jan Eitzinger, Gruber
---

### 2024051042001446_problem%20for%20login%20to%20server%20cshpc.rrze.fau.de.md
# Ticket 2024051042001446

 # HPC Support Ticket: Access Denied Error with WinSCP

## Keywords
- WinSCP
- Access Denied
- SSH Key
- IDM Password
- Data Transfer

## Problem Description
- User encountered an "access denied" error while attempting to transfer data using WinSCP.
- Both SSH key password and IDM password were tried but did not work.

## Root Cause
- The exact root cause is not explicitly stated in the conversation.

## Solution
- The HPC Admin suggested that the user's on-boarding process might not be complete.
- No specific technical solution was provided in the conversation.

## General Learnings
- Ensure that new users are properly on-boarded before attempting to access HPC resources.
- Verify that the user has the correct credentials and permissions for data transfer.
- Check the on-boarding status of the user if they encounter access issues.

## Next Steps
- Verify the user's on-boarding status.
- Ensure the user has the correct credentials and permissions.
- Provide detailed instructions for using WinSCP if the user is properly on-boarded.

## References
- [Data Copying with WinSCP](https://doc.nhr.fau.de/data/copying/#winscp)
---

### 2022111742001087_File%20tranfer%20to_from%20Alex.md
# Ticket 2022111742001087

 # HPC Support Ticket: File Transfer to/from Alex

## Keywords
- SCP
- SSH Key
- Authentication
- File Transfer
- Verbose Output

## Problem
- User unable to download files from Alex Cluster using SCP.
- SCP prompts for password despite using SSH key for authentication.
- SSH key works for SSH login but not for SCP.

## Root Cause
- SCP command unable to recognize or use the provided SSH key.
- Incorrect key format or path issue.

## Troubleshooting Steps
1. **Specify SSH Key Path**: Use the `-i` flag to specify the path to the private key.
   ```sh
   scp -i /path/to/private_key -r user@host:/path/to/remote/file .
   ```
2. **Verbose Output**: Add `-v` flags to the SCP command to get detailed output.
   ```sh
   scp -v -i /path/to/private_key -r user@host:/path/to/remote/file .
   ```

## Solution
- Ensure the SSH key is in the correct format (e.g., OpenSSH format).
- Verify the path to the private key is correct and accessible.
- Use verbose output to diagnose authentication issues.

## General Learning
- SCP uses the same authentication mechanism as SSH.
- Specifying the SSH key path with the `-i` flag is crucial if the key is not in the default location.
- Verbose output (`-v`) is helpful for diagnosing SCP issues.

## Next Steps
- If the issue persists, consult with HPC Admins or the 2nd Level Support team for further assistance.
- Ensure the SSH key is properly configured and accessible.
---

### 42049021_Probleme%20auf%20woody%20beim%20%20%20Erstellen_%C3%83%C2%84ndern%20von%20Dateien.md
# Ticket 42049021

 # HPC Support Ticket: Issues with File Modifications on Woody

## Keywords
- File system issues
- Woody cluster
- Fish protocol
- SFTP
- Konqueror
- Filezilla
- SCP
- `.cshrc` file

## Problem Description
- User unable to save changes to files or create new files with content on Woody cluster.
- Issue does not occur on cluster32.
- User logs in via Fish protocol using Konqueror.

## Troubleshooting Steps
1. **HPC Admin** attempted to reproduce the issue but was successful in creating, modifying, and deleting files under the user's account.
2. User clarified that the issue occurs with all files and that files copied from the local network to Woody are created with 0 bytes.
3. **HPC Admin** identified the problem as specific to the Fish protocol and the `/home/woody` filesystem.

## Workarounds Suggested
1. Use SFTP instead of Fish in Konqueror.
2. Use SCP on the command line instead of graphical clients.

## Further Issues
- User encountered problems with SFTP in Konqueror and Filezilla (out of memory error).
- **HPC Admin** successfully tested SFTP with a different username and suggested direct communication with the user's local admin.

## Root Cause and Solution
- The issue was traced to an `echo` command in the user's `~/.cshrc` file in their RRZE home directory.
- SFTP and SCP do not tolerate output generated by shell configuration files.
- Removing or commenting out the `echo` command resolved the issue for SFTP and SCP.
- Fish protocol still does not work on `/home/woody`, but SFTP provides a standardized alternative.

## Conclusion
- The problem was specific to the user's shell configuration file and affected SFTP and SCP functionality.
- Modifying the `.cshrc` file resolved the issue, allowing the user to use SFTP for file transfers.
---

### 2024032642002464_problem%20with%20sshfs.md
# Ticket 2024032642002464

 # HPC Support Ticket: Problem with SSHFS

## Keywords
- SSHFS
- Mounting HPC home files
- Terminal not responding
- Full path vs dot
- Frontend node vs csnhr
- IdentityFile
- .ssh/config

## Problem Description
The user is trying to mount their HPC home files on their workstation using the `sshfs` command. The terminal becomes unresponsive after entering the command.

## Root Cause
- The user is using a dot (`.`) to represent the current directory in the `sshfs` command, which may cause issues.
- The user is trying to mount their home directory via a frontend node (Fritz) instead of using `csnhr`.

## Solution
- Use the full path of the local directory instead of a dot (`.`).
- Mount the home directory via `csnhr` instead of the frontend node.
- Ensure that the `IdentityFile` is correctly specified, or use `.ssh/config` to avoid providing the key file.

## Relevant Documentation
- [Mounting file systems via SSHFS](https://doc.nhr.fau.de/data/mounting/)
- [SSH command line](https://doc.nhr.fau.de/access/ssh-command-line/)

## Ticket Status
The user was able to successfully use `sshfs` via `csnhr`.
---

### 2024031442003771_Login%20zu%20Cluster%20-%20iwst090h.md
# Ticket 2024031442003771

 To summarize the key points from the conversation:

1. **SSH Configuration and Key Management**:
   - The user had issues with SSH key-based authentication, being prompted for a password despite having configured SSH keys and a config file.
   - The user's config file was not being read correctly, and the keys were not being used for authentication.
   - The HPC admin suggested using an SSH agent or WinSCP for managing keys and ensuring the config file is read correctly.
   - The user was advised to move the config file and keys to the HPC home directory to ensure they are used correctly.

2. **File Transfer Issues**:
   - The user was unable to transfer files to Meggie without being prompted for a password.
   - The HPC admin suggested using WinSCP for file transfers, which is more user-friendly and supports SSH keys.
   - The user was advised to configure WinSCP with their SSH key for seamless file transfers.

3. **General Troubleshooting**:
   - The user was unable to log in to Meggie directly and was being redirected to cshpc.
   - The HPC admin confirmed that all network file systems ($HOME, $HPCVAULT, $WORK) are mounted on all clusters, so files transferred to cshpc are also available on Meggie.
   - The user was advised to use the first option in the FAQ for logging in directly to Meggie from their local machine.

4. **Conclusion**:
   - The user's issues were primarily related to SSH configuration and key management.
   - The HPC admin provided detailed steps to resolve the issues, including using an SSH agent, WinSCP, and ensuring the config file is read correctly.
   - The user was able to log in to Meggie directly after following the advice and configuring WinSCP for file transfers.

By following these steps, the user should be able to resolve their SSH authentication and file transfer issues. If further assistance is needed, the user can refer to the FAQ or contact the HPC support team.
---

### 2022022842002019_Inbound%20Datentransfer%20via%20cshpc.md
# Ticket 2022022842002019

 # HPC Support Ticket: Inbound Datentransfer via cshpc

## Keywords
- SSH connections
- Network unreachable
- Data transfer nodes
- Parallel transfers
- IPv6
- cshpc
- rsync
- scp

## Problem Description
- User encountered "Network unreachable" errors with `scp` and `rsync` while transferring data to `cshpc`.
- User attempted to transfer multiple files simultaneously using `parallel` with 8 jobs.

## Root Cause
- There is a limit on the number of new SSH connections that can be established per minute from the same IP address.
- The limit is 5 new connections per minute per source IP.

## Solution
- Reduce the number of parallel connections to avoid hitting the connection limit.
- Consider using IPv6 for external access to certain frontends if available.

## General Learnings
- `cshpc` has a 20 GBit network connection and is suitable for data transfer.
- There are no dedicated data transfer nodes at FAU, but `cshpc` serves this purpose.
- Some frontends are accessible via IPv6 from external networks.
- Be mindful of the shared nature of resources and avoid excessive parallel transfers.

## Additional Notes
- Future plans include a new node (`csNHR`) with enhanced network capabilities.
- Users should be aware of the limits on new SSH connections to avoid temporary rejections.
---

### 2022110442001851_Sharing%20%24HOME%20between%20HPC%20and%20%22personal%22%20workstation.md
# Ticket 2022110442001851

 # HPC Support Ticket: Sharing $HOME between HPC and Personal Workstation

## Keywords
- HPC-home
- Workstation
- IDM
- HPC-ID
- Network storage
- Quotas
- sshfs

## Problem
- User recently started working on a personal/chair-related workstation.
- Workstation login uses IDM, not HPC-ID.
- Network access handled by RRZE.
- Default home directory is network storage with quotas.
- User wants to share $HOME directory between HPC clusters and the workstation.

## Root Cause
- Different authentication systems (IDM vs. HPC-ID) and network configurations prevent direct sharing of $HOME directory.

## Solution
- It is not possible to use the HPC-home as the home directory on a workstation.
- Recommended workaround: Use `sshfs` to mount the HPC-home on the workstation.

## General Learnings
- HPC-home directories cannot be directly shared with personal workstations due to different authentication and network setups.
- `sshfs` can be used to mount HPC-home on a workstation for easier access to files.

## Roles Involved
- HPC Admins
- User (Simon Bachhuber)
---

### 42108377_FTP-Server%20tempor%C3%83%C2%A4r.md
# Ticket 42108377

 ```markdown
# HPC-Support Ticket: Temporary FTP Server

## Keywords
- FTP Server
- Data Transfer
- External Service Provider
- Software Evaluation
- Web Server
- SSH/Rsync/SFTP
- Temporary Access

## Problem Description
- **User Issue**: The user is attempting to send a large amount of data (~50GB, with files ranging from 5-7GB each) to an external service provider (SoftGenetics) for software evaluation. The provided FTP access is slow and unreliable.
- **Request**: The user is asking if it is possible to set up a temporary FTP access so that the external service provider can retrieve the data from the HPC system.

## Discussion and Solutions
- **HPC Admins**:
  - Confirmed that the HPC group does not operate an FTP server or other download portals.
  - Suggested setting up a web server on the user's system ("gattaca.rrze") and tunneling the port outward or using rsync/ssh inward.
  - Emphasized that using FTP for transferring user data is not secure due to lack of encryption.
  - Proposed using SSH/Rsync/SFTP for secure data transfer.

- **2nd Level Support Team**:
  - Discussed the possibility of using a web server or SSH/Rsync/SFTP for data transfer.
  - Suggested moving the ticket to the HPC queue for direct resolution with the user.

## Conclusion
- **Root Cause**: The external FTP access provided by the service provider is slow and unreliable.
- **Solution**: Set up a temporary web server on the user's system or use SSH/Rsync/SFTP for secure data transfer. Avoid using FTP due to security concerns.

## Notes
- The HPC group does not operate an FTP server.
- Using FTP for transferring user data is not recommended due to lack of encryption.
- Temporary access solutions like setting up a web server or using SSH/Rsync/SFTP are preferred for secure data transfer.
```
---

### 2024030742003098_Storage%20in%20Work%20directory.md
# Ticket 2024030742003098

 # HPC-Support Ticket Conversation: Storage in Work Directory

## Keywords
- New account
- Working directory
- Storage
- Home directory
- Data transfer
- SCP command

## Root Cause of the Problem
- User unable to locate working directory in the new account.
- Insufficient storage in the home directory for the user's project.
- Need to transfer data from the old account to the new account.

## What Can Be Learned
- Users may require assistance in locating their working directory, especially when transitioning to a new account.
- Storage limitations in the home directory can be a common issue for users with large projects.
- Users may need guidance on transferring data between accounts, including the use of SCP commands.

## Solution (if found)
- Provide instructions on how to locate the working directory.
- Offer solutions for increasing storage capacity, such as using external storage or requesting additional quota.
- Guide users on using SCP commands to transfer data between accounts.

## Notes for Support Employees
- Ensure users are aware of the location and usage of their working directory.
- Be prepared to assist with storage management and data transfer processes.
- Consider providing documentation or tutorials on common tasks like data transfer using SCP.
---

### 2018082842001419_Mount%20HPC%20Folders%20on%20Windows%20PC.md
# Ticket 2018082842001419

 # HPC Support Ticket: Mount HPC Folders on Windows PC

## Keywords
- HPC Folders
- Windows PC
- Mounting
- sshfs
- Samba
- File Transfer

## Problem Description
The user can mount HPC folders on Ubuntu and Mac using `sshfs` for easy file transfer and editing. They are looking for a similar solution to mount HPC folders on a Windows PC. The user found a guide using Samba, but the required package is not installed on the HPC.

## Root Cause
The user needs a method to mount HPC folders on a Windows PC similar to `sshfs` on Ubuntu and Mac. The Samba package is not available on the HPC.

## Solution
No direct solution was provided in the ticket conversation. The HPC Admin marked the request as completed but did not specify the method used.

## General Learning
- Users may need to mount HPC folders on Windows PCs for file transfer and editing.
- `sshfs` is a common method for mounting HPC folders on Ubuntu and Mac.
- Samba is an alternative method, but it requires the appropriate package to be installed on the HPC.
- The HPC Admin completed the request, but the specific solution was not documented in the ticket.

## Next Steps
- Document the method used by the HPC Admin to mount HPC folders on Windows PCs.
- Provide a guide or FAQ for users on how to mount HPC folders on Windows PCs.
- Consider installing the Samba package on the HPC if it is a viable solution.
---

### 2022082242003198_File%20transfer%20issues%3B%20Connection%20closed%20by%20remote%20host.md
# Ticket 2022082242003198

 # HPC Support Ticket: File Transfer Issues

## Keywords
- File transfer
- SSH rate limit
- Connection closed by remote host
- Network unreachable
- rsync
- scp
- Bash loop
- ProxyJump
- ControlMaster
- Multiplexed connections

## Problem Description
- User experiences issues when transferring files from FAU to a local machine via SSH.
- The transfer works initially but fails after a few iterations in a bash loop.
- Error message: `ssh: connect to host cshpc.rrze.fau.de port 22: Network is unreachable kex_exchange_identification: Connection closed by remote host`

## Root Cause
- Rate limit on the number of new SSH connections per host in a certain timeframe.
- Inefficient file transfer method: opening a new SSH connection for each file.

## User Setup
- Connects to FAU through a dialog server using an SSH config file with ProxyJump.
- Uses a bash loop with rsync or scp to transfer files.

## Solution
- Avoid opening a new SSH connection for each file transfer.
- Consider using rsync with include/exclude patterns or a file list to transfer files in a single connection.
- Explore the use of multiplexed connections or ControlMaster to reuse existing SSH connections.

## Lessons Learned
- Be aware of SSH rate limits when transferring files.
- Optimize file transfer methods to minimize the number of new SSH connections.
- Utilize advanced features of file transfer tools like rsync to improve efficiency.
- Consider reusing SSH connections for repeated transfers.
---

### 2017070542001984_Daten%C3%83%C2%BCbertragung%20von%20hpc%20an%20lokalen%20Windowsrechner.md
# Ticket 2017070542001984

 # HPC Support Ticket: Data Transfer from HPC to Local Windows PC

## Keywords
- Data transfer
- HPC account
- Local Windows PC
- Zip folder
- PuTTY
- WinSCP
- WebDAV
- FAUbox

## Problem Description
The user is having trouble transferring a zip folder from their HPC account to a local Windows PC. They inquired about using PuTTY, Windows Command Prompt, or WebDAV via PuTTY to transfer the folder to FAUbox.

## Solution
The HPC Admin recommended installing WinSCP, a graphical interface tool that allows easy file transfer between the local PC (including FAUbox) and the HPC home directory.

## General Learnings
- **WinSCP Recommendation**: For users struggling with file transfers between HPC and local Windows machines, WinSCP is a user-friendly solution.
- **Graphical Interface**: Tools with graphical interfaces like WinSCP can simplify complex tasks for users who are not comfortable with command-line interfaces.
- **Efficient Support**: Providing clear and actionable recommendations, such as installing specific software, can quickly resolve user issues.

## Root Cause
The user was unaware of an efficient method to transfer files between the HPC account and a local Windows PC.

## Resolution
Install WinSCP to facilitate easy file transfers between the HPC account and the local Windows PC.

---

This documentation can be used to assist other users facing similar issues with file transfers between HPC accounts and local Windows machines.
---

### 2021042842000153_hpc%20mount.md
# Ticket 2021042842000153

 # HPC Support Ticket: hpc mount

## Keywords
- sshfs
- FUSE
- osxfuse
- Samba mount
- macOS
- Homebrew

## Problem Description
The user attempted to mount their HPC access using `sshfs` on a macOS system but encountered issues related to FUSE. Despite having FUSE installed, the user was unable to proceed with the `sshfs` installation.

## Root Cause
- The `sshfs` package from Homebrew requires FUSE, which was installed but not recognized correctly.
- The Homebrew version of `sshfs` has known issues.

## Solution
1. **Alternative Mounting Method**: Use Samba mount instead of `sshfs`.
   - **Steps**:
     - Open Finder -> Preferences -> Show these items on the desktop: check "Connected servers".
     - Finder -> Go -> Connect to server:
       - Server address:
         - `smb://fundus.rrze.uni-erlangen.de/hpc_home`
         - `smb://fundus.rrze.uni-erlangen.de/hpc_vault`
       - Click "Connect" and provide HPC username and password.

2. **Install Required Packages**:
   - `osxfuse`: `brew install osxfuse` (admin rights required)
   - `sshfs`: Download and install from [GitHub](https://github.com/osxfuse/sshfs/releases/download/osxfuse-sshfs-2.5.0/sshfs-2.5.0.pkg) (admin rights required)

3. **Execute the `sshfs` Command**:
   - `sshfs user@remotehost:/path /path/to/mount`

## Additional Notes
- The user encountered a `kext load failed: -603947007` error, which is a known issue with `osxfuse`.
- For further troubleshooting, refer to the [osxfuse GitHub issues page](https://github.com/osxfuse/osxfuse/issues).

## Conclusion
The user was advised to use Samba mount as an alternative to `sshfs` due to known issues with the Homebrew version of `sshfs`. Additional troubleshooting steps were provided for resolving `osxfuse` errors.
---

### 2024012442001098_Issue%20with%20HPC%20Cluster%20-%20iwi5176h.md
# Ticket 2024012442001098

 # HPC Support Ticket Conversation Summary

## Keywords
- HPC Cluster
- Data Storage
- Access Issues
- CUDA Installation
- Connection Timeout

## General Learnings
- **Filesystems**: Understanding the different filesystems available on the HPC cluster and their appropriate use cases.
- **Access and Permissions**: Troubleshooting access and permission issues when uploading data.
- **Software Installation**: Guidelines for installing software packages like CUDA without requiring sudo privileges.
- **Connection Issues**: Diagnosing and resolving connection timeout errors in WinSCP/FileZilla.

## Detailed Issues and Solutions

### Issue 1: Data Storage Location
- **Problem**: User unsure where to store data.
- **Solution**:
  - **Filesystems**:
    - `$HOME` (`/home/hpc/iwi5/iwi5176h`): Personal home directory.
    - `$HPCVAULT` (`/home/vault/iwi5/iwi5176h`): High-quality storage with frequent backups and snapshots.
    - `$WORK` (`/home/woody/iwi5/iwi5176h`): Working directory with a quota of 500GB.
  - **Recommendation**: Use `$WORK` or `$HPCVAULT` for data storage.

### Issue 2: Access and Space Issues
- **Problem**: Access error in `/home/vault` and space issues in `/home/hpc/iwi5/iwi5176h`.
- **Solution**:
  - **Access Error**: Ensure correct permissions and use appropriate directories.
  - **Space Issue**: Use `$WORK` or `$HPCVAULT` for larger data storage.

### Issue 3: CUDA Installation
- **Problem**: User attempting to install CUDA in `/home/vault/iwi5/iwi5176h` without sudo privileges.
- **Solution**:
  - **Environment Modules**: Use pre-installed CUDA modules instead of manual installation.
  - **Installation Directory**: Install personal packages in `$WORK` (`/home/woody/iwi5/iwi5176h`).

### Issue 4: Connection Timeout
- **Problem**: Connection timeout error when connecting to `cshpc.rrze.fau.de` using WinSCP/FileZilla.
- **Solution**:
  - **Timeout Value**: Increase the timeout value in FileZilla preferences to more than 20 seconds.
  - **Retry Connection**: Sometimes the server response is slow; retrying the connection may resolve the issue.

## Documentation and Resources
- **HPC Storage Documentation**: [HPC Storage Documentation](https://hpc.fau.de/systems-services/documentation-instructions/hpc-storage/)
- **HPC Cafe**: Regular sessions for new users to get familiar with the HPC environment.
- **Online Introduction**: Detailed online resources for new users.

## Conclusion
This conversation highlights common issues faced by new HPC users, including data storage, software installation, and connection problems. The solutions provided can serve as a reference for future support cases.
---

### 2018072342001546_aycassamba%20link.md
# Ticket 2018072342001546

 # HPC-Support Ticket: aycassamba Link Issue

## Keywords
- aycassamba
- MacMini
- Mounting Share
- Doppelpunkt (Colon)
- Host
- Pfad (Path)

## Problem Description
The user encountered an issue while trying to mount the aycassamba share on a MacMini. The user had to insert a colon (:) after the host and before the path to successfully mount the share.

## Root Cause
The user's operating system (MacMini) requires a colon (:) to separate the host and the path when mounting a share.

## Solution
Insert a colon (:) after the host and before the path when mounting the aycassamba share on a MacMini.

## General Learning
- Different operating systems may require specific syntax for mounting shares.
- Always check the documentation for the correct syntax based on the operating system being used.
- If the documentation is missing crucial information, it might need to be updated to include OS-specific instructions.
---

### 2020102942001695_Download%20Speed.md
# Ticket 2020102942001695

 # HPC Support Ticket: Download Speed

## Keywords
- Download Speed
- Transfer Rate
- WLAN Speed Test
- SFTP
- WinSCP
- Windows 10
- 1&1 Provider
- Fritzbox 7590
- Fritz Repeater 2400
- Mesh Network

## Problem Description
- User experiencing slow file transfer speeds (4000 KB/s) from HPC to laptop.
- Speed test shows 40 Mb/s over WLAN.

## Root Cause
- Insufficient information initially provided by the user.
- Potential network or configuration issues.

## Information Requested
- Transfer details: Source and destination.
- Transfer protocol used.
- Program and operating system used for transfer.
- Network connection details.
- VPN status.

## User Response
- Transfer from `home/hpc/corz006h` to laptop.
- Protocol: SFTP.
- Program: WinSCP on Windows 10 Home.
- Provider: 1&1 with Fritzbox 7590 and Fritz Repeater 2400 in Mesh.
- No VPN active.

## Solution
- Not explicitly provided in the conversation.
- Further investigation required based on the detailed information provided by the user.

## General Learnings
- Importance of gathering detailed information for troubleshooting.
- Common issues with network configurations and transfer protocols.
- Potential impact of network hardware (e.g., routers, repeaters) on transfer speeds.
---

### 2023041442002558_User%20name%20not%20showing%20in%20HPC_user%20portal.md
# Ticket 2023041442002558

 # HPC Support Ticket: Username Not Showing in HPC User Portal

## Keywords
- SCP
- SSH
- HPC Portal
- SSH Key
- Legacy Application
- IdM
- Hostname Resolution

## Problem Description
- User encountered issues while trying to use `scp` to transfer files to the HPC cluster.
- Initial command resulted in an error: `ssh: Could not resolve hostname d: Name or service not known`.
- User attempted to use SSH keys but did not have an account on the HPC portal.

## Root Cause
- Incorrect file path format in the `scp` command.
- User account was created using the legacy application (IdM) and not through the HPC portal, preventing SSH key upload via the portal.

## Solution
- Correct the file path format in the `scp` command:
  ```sh
  scp D:\Thesis\numpy-transformer-master USERNAME@CLUSTERNAME.nhr.fau.de:/home/hpc/iwia/iwia050h
  ```
- For SSH keys, follow the documentation for IdM-based accounts:
  - Refer to the section "IdM-based (i.e. when you had to fill and sign a paper form)" in the provided documentation.

## Additional Notes
- Always use the official `@fau.de` email address when contacting support.
- Supervisors or HPC Admins can provide further assistance if needed.

## References
- [SSH Secure Shell Access to HPC Systems](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/#publickey-portal)
- [HPC Portal User Interface](https://portal.hpc.fau.de/ui/user)
---

### 2022020942001145_ssh%20to%20HPC%2C%20what%20to%20do%20if....md
# Ticket 2022020942001145

 # HPC Support Ticket: SSH Best Practices for Multiuser Environments

## Keywords
- SSH
- Public Key Authentication
- Multiuser Environment
- File Transfer
- Security Best Practices

## Problem Description
The user is concerned about the best practices for SSH public-key authentication in a multiuser environment. Specifically, the user needs to transfer large files between the HPC cluster and a multiuser server they administer. The user is aware that storing private keys on untrusted hosts is not recommended but needs a solution for secure and efficient file transfers.

## Root Cause
- The user requires a secure method to transfer large files between two remote hosts without storing private keys on untrusted systems.
- The current method of using a proxy jump over a single-user laptop is not efficient due to network limitations.

## Solution
- The HPC Admin suggested using `scp` to transfer files directly between the two remote hosts, with the local machine only being used for authentication.
- The user attempted this method but encountered authentication issues.
- The user found that using the `-3` option with `scp` works but routes data through the local machine, which is not efficient for large transfers over WLAN.

## Recommendations
- Use `scp` with proper authentication setup to avoid storing private keys on untrusted hosts.
- Ensure that both remote hosts can communicate directly without firewall restrictions.
- Consider using strong passwords for private keys to enhance security.

## Additional Information
- The user provided feedback that the suggested `scp` method did not work as expected due to authentication issues.
- The user found a workaround using the `-3` option but noted its inefficiency for large transfers over WLAN.

## Conclusion
The user needs a more efficient and secure method for file transfers between remote hosts in a multiuser environment. The HPC Admin's suggestion to use `scp` for direct transfers is a step in the right direction, but further configuration is needed to address authentication issues and ensure efficient data transfer.
---

### 2024051042002892_Assistance%20Needed%20with%20SCP%20Issue%20on%20Linux.md
# Ticket 2024051042002892

 ```markdown
# HPC-Support Ticket: Assistance Needed with SCP Issue on Linux

## Keywords
- SCP
- Linux
- File Transfer
- Troubleshooting
- Support

## Issue Description
The user is encountering difficulties while using SCP to transfer files between systems on Linux.

## Root Cause
The exact root cause is not specified in the initial email, but it involves issues with SCP file transfers.

## Solution
No solution is provided in the initial conversation. Further details and troubleshooting steps are required to identify and resolve the issue.

## Actions Taken
- The user reached out to HPC support for assistance with SCP issues.
- The HPC Admin responded, redirecting the user to on-board their student.

## Next Steps
- Schedule a call or exchange emails to gather more details about the SCP issue.
- Provide troubleshooting steps or solutions based on the gathered information.

## Notes
- Ensure proper on-boarding of students as per HPC Admin's instructions.
- Follow up with the user to gather more specific error messages or logs related to the SCP issue.
```
---

### 42173071_technical%20support.md
# Ticket 42173071

 ```markdown
# HPC Support Ticket: Exporting Data from STAR-CCM+

## Keywords
- Data export
- STAR-CCM+
- External hard disk
- SCP
- Woody

## Problem Description
- User needs to export data from STAR-CCM+ on Woody.
- Data size is approximately 125 GB.
- User has an external hard disk but is unsure how to define it in the media at the root directory.

## Root Cause
- Lack of knowledge on how to transfer data between the remote system (Woody) and a local external hard disk.

## Solution
- Use SCP (Secure Copy Protocol) to transfer data between the remote system (Woody) and the local system.

## General Learning
- SCP is a common method for securely transferring files between remote and local systems.
- Ensure users are familiar with basic file transfer protocols and tools like SCP for handling large data transfers.

## Additional Notes
- Provide users with documentation or tutorials on using SCP for data transfer.
- Ensure that users understand the importance of secure data transfer methods.
```
---

### 2023042842001514_sshfs%20m%C3%83%C2%B6glich%3F.md
# Ticket 2023042842001514

 # HPC Support Ticket: sshfs Access Issue

## Keywords
- sshfs
- Connection reset by peer
- Private key
- SFTP
- Mounting remote filesystem

## Problem Description
- User attempted to mount a remote filesystem on `fritz` using `sshfs`.
- Received error: `read: Connection reset by peer`.
- Command used: `sshfs -o IdentityFile=/path/to/pubkey -o allow_other user@fritz.nhr.fau.de:/home/hpc/project/user /localmountpoint`.

## Root Cause
- Incorrect path to the private key file.

## Solution
- Ensure the correct path to the private key is specified in the `IdentityFile` option.
- Correct command: `sshfs -o IdentityFile=/correct/path/to/privatekey -o allow_other user@fritz.nhr.fau.de:/home/hpc/project/user /localmountpoint`.

## General Learnings
- Verify the correctness of the private key path when using `sshfs`.
- `sshfs` is not blocked on the server side and functions as a generic SFTP client.
- Common issues with `sshfs` can often be resolved by checking configuration details such as key paths and permissions.

## Additional Notes
- `sshfs` is a useful tool for mounting remote filesystems and can be used similarly to other SFTP clients.
- Ensure proper error handling and debugging steps when encountering connection issues.
---

### 2018061842000531_Fehlerhafte%20Kopien%20bei%20ftp.md
# Ticket 2018061842000531

 # HPC-Support Ticket: Fehlerhafte Kopien bei ftp

## Keywords
- FTP
- Data corruption
- Windows 10
- Ubuntu 16.04
- SCP
- HPC

## Problem Description
- User reports data corruption when copying files from a Windows 10 FTP server to the HPC using the `ftp` command.
- Corruption results in a few kilobytes of data loss in large files (~1TB), rendering them unreadable.
- No issues when copying files from the FTP server to an intermediate Ubuntu 16.04 PC and then using `scp` to transfer to the HPC.

## Root Cause
- Potential issues with the FTP protocol or the specific FTP server implementation on Windows 10 leading to data corruption during transfer.

## Solution
- Use an intermediate Ubuntu PC to first download the files from the FTP server and then transfer them to the HPC using `scp`.

## General Learnings
- FTP transfers can be unreliable for large files, leading to data corruption.
- Using `scp` for file transfers can be more reliable than FTP.
- Intermediate steps, such as using a different operating system for file transfers, can help mitigate data corruption issues.

## Next Steps
- Investigate the FTP server configuration on the Windows 10 PC.
- Consider using more robust file transfer protocols like SFTP or SCP directly from the Windows 10 PC if possible.
- Document the issue for future reference and to assist other users experiencing similar problems.
---

### 2024101342000191_copying%20file%20from%20hpc%20remote%20to%20my%20local%20machine.md
# Ticket 2024101342000191

 ```markdown
# HPC Support Ticket: Copying File from HPC Remote to Local Machine

## Subject
Copying file from HPC remote to my local machine

## User Issue
The user attempted to copy files from the HPC server to their local machine using `scp` but encountered a "Permission denied (publickey)" error.

## Debug Information
- **Command Used:**
  ```sh
  scp -vv -r iwi5237h@csnhr.nhr.fau.de:~/mmdetection /mnt/backup/
  ```
- **Error Message:**
  ```sh
  iwi5237h@csnhr.nhr.fau.de: Permission denied (publickey).
  ```
- **Debug Output:**
  - The user attempted to run the `scp` command from the HPC server (csnhr).
  - The command failed due to authentication issues (no valid private key found).

## Root Cause
The user was running the `scp` command from the HPC server instead of their local machine. Additionally, the user did not have a valid private key configured for authentication.

## Solution
The HPC Admin advised the user to run the `scp` command from their local machine instead of the HPC server.

## Keywords
- `scp`
- `Permission denied (publickey)`
- `HPC server`
- `local machine`
- `authentication`
- `private key`

## Lessons Learned
- Ensure that `scp` commands for copying files from the HPC server to a local machine are run from the local machine.
- Verify that the user has the correct private key configured for SSH authentication.
```
---

### 2022011942002949_Dateien-Upload%20vom%20Meggie%20Cluster%20auf%20die%20FAUbox.md
# Ticket 2022011942002949

 # HPC-Support Ticket: Dateien-Upload vom Meggie Cluster auf die FAUbox

## Keywords
- Meggie Cluster
- FAUbox
- Daten Transfer
- WinSCP
- sshfs
- hpc-mover

## Problem
- User möchte Dateien vom Meggie Cluster direkt in die FAUbox hochladen.
- User hat große Datensätze auf einem HPC-Account, die externen Personen zum Download bereitgestellt werden sollen.

## Root Cause
- Direkter Daten Transfer von Meggie in die FAUbox ist nicht möglich.
- User benötigt eine Methode, um große Datensätze externen Personen zugänglich zu machen.

## Lösung
- **Daten Transfer:**
  - Unter Linux/mac: Verzeichnis mounten (z.B. per sshfs), für /home/.. geht das vom Frontend aus.
  - Unter Windows: WinSCP verwenden.
  - Alternativ: [hpc-mover](https://hpc-mover.rrze.uni-erlangen.de/HPC-Data/howto.html) verwenden.

- **Bereitstellung großer Datensätze:**
  - hpc-mover kann verwendet werden, um große Datensätze externen Personen zum Download bereitzustellen.

## Beteiligte Personen
- **HPC Admins:** Johannes Veh
- **User:** Sibille Wehrmann

## Zusammenfassung
- Direkter Daten Transfer von Meggie in die FAUbox ist nicht möglich.
- WinSCP und sshfs sind geeignete Methoden für den Daten Transfer.
- hpc-mover kann verwendet werden, um große Datensätze externen Personen zum Download bereitzustellen.

## Weitere Schritte
- User sollte hpc-mover für die Bereitstellung großer Datensätze verwenden.
- Bei weiteren Fragen sollte der User den HPC-Support kontaktieren.
---

### 2024041042003204_Re%3A%20%5BNHR%40FAU%5D%20Today%3A%20HPC%20intro%20for%20beginners.md
# Ticket 2024041042003204

 # HPC Support Ticket Conversation Analysis

## Keywords
- SCP command
- SSH key authentication
- Password prompt
- SSH configuration
- File transfer
- HPC system
- Public key
- Config file

## Summary
A user encountered issues with file transfers using the SCP command, despite using SSH key authentication. The user was prompted for a password, which they did not have. The HPC admin provided guidance on setting up the SSH configuration and requested additional information to troubleshoot the issue.

## Root Cause of the Problem
- Incorrect or incomplete SSH configuration.
- Possible mismatch between the SSH key and the server's authorized keys.

## Solution
- Ensure the SSH configuration matches the template provided in the documentation.
- Verify the public key is correctly added to the server's authorized keys.
- Use the `ssh -v` command to provide detailed output for further troubleshooting.

## General Learnings
- Proper SSH configuration is crucial for seamless file transfers using SCP.
- The `ssh -v` command is useful for diagnosing SSH connection issues.
- Users should follow the documentation for setting up SSH configurations.
- HPC admins can guide users through troubleshooting steps and request detailed output for better assistance.

## Next Steps
- The user should verify their SSH configuration and provide the output of the `ssh -v` command for further analysis.
- The HPC admin will continue to assist the user based on the provided information.
---

### 2024050942000244_data%20transfer.md
# Ticket 2024050942000244

 # HPC Support Ticket: Data Transfer Between Accounts

## Keywords
- Data Transfer
- SCP
- Rsync
- SSH Key
- File Permissions
- CP Command

## Problem
- User is the PI of one project and project manager of another.
- Needs to transfer data from one account to another.
- Cannot use `cp -r` due to lack of access between accounts.

## Root Cause
- Lack of access permissions between the two accounts.

## Discussion
- **HPC Admin** suggested using `scp` or `rsync` for data transfer.
- **HPC Admin** mentioned the importance of having the private SSH key for authentication.
- **HPC Admin** highlighted security concerns regarding storing private keys on the system.
- **HPC Admin** proposed changing file permissions to allow access between accounts.

## Solution
- Use `scp` or `rsync` for data transfer if SSH keys are properly configured.
- Change file permissions to allow access between accounts for using `cp -r`.

## References
- [Data Copying Instructions](https://doc.nhr.fau.de/data/copying/)
- [Data Sharing Instructions](https://doc.nhr.fau.de/data/share/)

## General Learnings
- Understanding the use of `scp` and `rsync` for data transfer.
- Importance of SSH key management and security implications.
- Changing file permissions to facilitate data transfer between accounts.
- Avoiding unnecessary network overhead by using `cp` when possible.
---

### 2024050242004039_Assistance%20Needed%20with%20File%20Transfer%20Issue.md
# Ticket 2024050242004039

 # HPC Support Ticket: Assistance Needed with File Transfer Issue

## Subject
Assistance Needed with File Transfer Issue

## User Issue
- User encounters a password prompt when attempting to transfer files via `scp` despite having generated a public key and configured the SSH config file.
- User can connect to the HPC system via SSH without issues but faces problems with file transfers.

## Key Points from Conversation
- User initially logs into the HPC system and then attempts to use `scp` for file transfer.
- User provides the output of the `scp -v` command, indicating that the command is being executed from the HPC system rather than the local machine.
- HPC Admin suggests using the `scp` command directly from the local machine without logging into the HPC system first.

## Root Cause
- The `scp` command was being executed from the HPC system instead of the local machine, leading to authentication issues.

## Solution
- Use the `scp` command directly from the local machine without logging into the HPC system first.
- Example command:
  ```sh
  scp -v /Users/username/Downloads/untitled_folder ilev101h@woody.nhr.fau.de:/home/hpc/ilev/ilev101h/RLfiles
  ```

## Additional Notes
- For Windows users, WinSCP is recommended for file transfers. Documentation can be found [here](https://doc.nhr.fau.de/data/copying/#winscp).
- Ensure the SSH config file is correctly set up to use the appropriate identity file and authentication method.

## Conclusion
- The issue was resolved by instructing the user to execute the `scp` command from their local machine instead of the HPC system.
- This documentation can be used to assist other users facing similar file transfer issues.
---

### 2021101842001749_Re%3A%20Alternative%20zum%20CIFS-Mount%3F.md
# Ticket 2021101842001749

 # HPC Support Ticket: Alternative to CIFS-Mount

## Keywords
- CIFS-Mount
- Samba
- Windows
- Linux
- Dateinamen
- Sonderzeichen
- Backup

## Problem
- **Root Cause**: Windows (and Samba) do not support special characters like `:` or `?` in filenames. This causes issues during file transfers, where filenames containing these characters are altered.
- **User Issue**: The user is using CIFS-Mount to access files on the HPC cluster, but special characters in filenames are causing problems during transfers.

## Solution
- **Advice**: Avoid using special characters in filenames as they are not supported by Windows and can cause issues even under Linux, especially during backups.
- **No Support**: The HPC Admins cannot provide support for issues related to the use of special characters in filenames.

## General Learnings
- **Naming Conventions**: Follow the naming conventions for filenames to avoid issues across different operating systems.
- **Backup Issues**: Special characters in filenames can cause problems during backups, even on Linux.
- **Alternatives**: Explore alternatives to CIFS-Mount if special characters are necessary, though no specific alternatives were mentioned in this conversation.

## References
- [Microsoft Naming Conventions](https://docs.microsoft.com/en-us/windows/win32/fileio/naming-a-file)

## Next Steps
- **User Action**: Review and update filenames to comply with naming conventions.
- **Support Action**: Refer users to the naming conventions documentation for further guidance.
---

### 2020062242002161_Brief%20access%20to%20ftp%20on%20meggie.md
# Ticket 2020062242002161

 ```markdown
# HPC Support Ticket: Brief Access to FTP on Meggie

## Keywords
- FTP access
- Command line
- Meggie frontends
- lftp
- File transfer

## Problem
- User needed to send a 70GB file to the University of Innsbruck.
- Requested brief access to FTP at the command line on Meggie.

## Solution
- HPC Admin informed the user that the command-line FTP client `lftp` is available on the Meggie frontends.
- User confirmed completion of the task.

## General Learnings
- The `lftp` command-line FTP client is available on Meggie frontends for file transfers.
- Users can request specific tools or access for temporary tasks.

## Root Cause
- User needed a specific tool (`lftp`) to transfer a large file.

## Resolution
- Provided access to `lftp` on Meggie frontends.
```
---

### 2018060842002451_Emmy%20acces.md
# Ticket 2018060842002451

 # HPC Support Ticket: File Transfer from Emmy Cluster to Personal Computer

## Keywords
- Emmy cluster
- FAU network
- SSH
- SCP
- File transfer
- Dialog server

## Problem Description
- User is accessing the Emmy cluster from outside the FAU network via a dialog server.
- User needs to copy files from Emmy to their personal computer.
- Attempted using `scp` directly from Emmy to personal computer and via dialog server without success.

## Root Cause
- Incorrect usage of `scp` for file transfer through intermediate server.

## Solution
- Use `scp` with proper syntax to transfer files from Emmy to the dialog server first, and then from the dialog server to the personal computer.
- Example commands:
  ```sh
  scp user@emmy.rrze.fau.de:/path/to/file user@cshpc.rrze.fau.de:/path/to/destination
  scp user@cshpc.rrze.fau.de:/path/to/destination /local/path/to/destination
  ```

## General Learning
- Understanding the correct usage of `scp` for file transfers through intermediate servers.
- Importance of proper syntax and command structure for secure file transfers in HPC environments.

## Additional Notes
- Ensure users are aware of the security implications of transferring files through intermediate servers.
- Provide clear documentation on file transfer procedures for users accessing HPC clusters from outside the network.
---

### 2015100542000366_HPC%20mount%20on%20MAC.md
# Ticket 2015100542000366

 # HPC Mount Issue on macOS

## Keywords
- macOS
- Home directory mount
- LAN connection
- Reboot
- Error message

## Problem Description
- User unable to mount home directory since Thursday.
- Error message appears during the mounting process.
- Attempts to resolve the issue by disconnecting LAN and rebooting the computer were unsuccessful.

## Root Cause
- Unknown; further investigation required.

## Solution
- None provided in the conversation.

## Actions Taken
- The request was moved to another queue or team for further investigation.

## General Learnings
- Common troubleshooting steps like disconnecting LAN and rebooting may not always resolve mounting issues.
- Further investigation is often required to identify the root cause of such issues.

## Next Steps
- Continue troubleshooting by checking network configurations, server status, and user permissions.
- Consult with the 2nd Level Support team or HPC Admins for additional assistance.
---

### 2020090342001236_Password%20denied%20but%20correct.md
# Ticket 2020090342001236

 # HPC-Support Ticket: Password Denied but Correct

## Keywords
- SCP
- Password authentication
- Permission denied
- Public key
- GSSAPI
- Remote file transfer

## Issue Summary
- User unable to securely copy files from HPC to office computer using SCP.
- Password authentication works from home laptop but not from office computer.
- Error message: `permission denied (publickey,gssapi-keyex,gssapi-with-mic,password)`.

## Root Cause
- Possible configuration differences between home laptop and office computer.
- Potential network restrictions or security policies at the office.

## Troubleshooting Steps
1. **Verify SSH Configuration**:
   - Check if the SSH configuration on the office computer matches the home laptop.
   - Ensure that the correct SSH keys are being used.

2. **Network Restrictions**:
   - Investigate if there are any network restrictions or firewalls at the office that might be blocking the SCP connection.

3. **Authentication Methods**:
   - Confirm that the office computer is configured to use the same authentication methods as the home laptop.
   - Ensure that the correct public key is being used if public key authentication is required.

4. **Log Files**:
   - Check SSH log files on both the client and server for more detailed error messages.

## Solution (if found)
- Ensure that the SSH configuration on the office computer is correctly set up to use the appropriate authentication methods.
- Verify that there are no network restrictions blocking the SCP connection.

## Notes
- The user's password works for SSH login but not for SCP, indicating a possible configuration issue specific to SCP.
- The error message suggests multiple authentication methods are being attempted, including public key and GSSAPI.

## Next Steps
- If the issue persists, escalate to the 2nd Level Support team for further investigation.
- Consider involving HPC Admins if network or server-side configurations need to be adjusted.

---

This documentation aims to assist support employees in troubleshooting similar issues related to SCP and password authentication.
---

### 2023083042001048_Regarding%20data%20transfer%20problem.md
# Ticket 2023083042001048

 # HPC Support Ticket: Data Transfer Problem

## Keywords
- Data Transfer
- SCP
- Permission Denied
- Username Issue
- Windows
- VPN

## Problem Description
User encountered a "Permission denied" error when attempting to transfer data to the HPC using the `scp` command. The user was unable to transfer data to or from the remote system.

## Root Cause
- Incorrect username used in the `scp` command.

## Troubleshooting Steps
1. **Username Verification**: The HPC Admin identified that the user was using an incorrect username (`iwi5147`) instead of the correct one (`iwi5147h`).
2. **Command Correction**: The user was advised to use the correct username in the `scp` command.

## Solution
- Use the correct username in the `scp` command:
  ```sh
  scp C:\Users\User\b.TXT iwi5147h@tinyx.nhr.fau.de:/home/hpc/iwi5/iwi5147h
  ```

## General Learnings
- Always verify the username and other credentials when encountering permission issues.
- Ensure the file path is correctly specified in the `scp` command to avoid "No such file or directory" errors.

## Additional Notes
- The user was using a Windows PC and connected via VPN.
- The issue was resolved by correcting the username in the `scp` command.
---

### 42086986_question%20about%20ssh%20file%20transfer.md
# Ticket 42086986

 # HPC Support Ticket: SSH File Transfer Issue

## Keywords
- SSH File Transfer
- SFTP Server
- Exit Value 0
- SSH Secure Shell
- WinSCP
- Putty

## Problem Description
- User unable to open File Transfer Window via SSH.
- Error message: "File transfer server could not be started or exited unexpectedly. Exit value 0 was returned."
- User's software: SSH Secure Shell Ver. 3.2.9 (Build 283)
- Operating system: Windows XP
- Target server: woody.rrze.uni-erlangen.de

## Root Cause
- Outdated SSH client software (SSH Secure Shell Ver. 3.2.9 from 2003) not compatible with current security standards.

## Solution
- Update SSH client software to a current version.
- Recommended software: WinSCP or Putty.

## General Learnings
- Always check the software version and compatibility when troubleshooting SSH issues.
- Ensure that the SFTP server is in the user's path on the server side.
- Recommend up-to-date software for better security and compatibility.
---

### 2023072042003451_Question%20on%20mounting%20Fritz%20server%20folder%20in%20a%20user%20Windows%20OS.md
# Ticket 2023072042003451

 ```markdown
# HPC-Support Ticket Conversation Summary

## Subject: Question on mounting Fritz server folder in a user Windows OS

### Keywords:
- Windows OS
- Fritz cluster
- Mounting server folder
- SFTP
- MobaXterm
- WinSCP
- SFTP Drive 2022
- cshpc.rrze.fau.de

### Problem:
- User repeatedly downloads molecular structure files to a Windows laptop for visualization using Ovito.
- User wants to mount the server folder on their Windows laptop for easier access.
- User's home folder: `/home/hpc/a102cb/a102cb12`
- Cluster: Fritz cluster `fritz.nhr.fau.de`
- Login node: `fritz3.nhr.fau.de`
- User tried SFTP in MobaXterm but folder browser was not shown.
- User tried SFTP Drive 2022 and win sshfs but could not make a connection.

### Solution:
- HPC Admin recommended using MobaXterm and WinSCP for file transfer.
- HPC Admin suggested connecting to `cshpc.rrze.fau.de` instead of a Fritz frontend node for file transfers.
- User successfully connected to `cshpc.rrze.fau.de` using SFTP Drive 2022.

### General Learnings:
- For file transfers, connect to `cshpc.rrze.fau.de` instead of a Fritz frontend node.
- MobaXterm and WinSCP are recommended for file transfer due to their ease of use and navigation.
- SFTP Drive 2022 can be used to mount server folders on Windows OS.

### Root Cause:
- User was attempting to connect to the wrong server node for file transfers.

### Resolution:
- User successfully connected to `cshpc.rrze.fau.de` using SFTP Drive 2022, resolving the issue.
```
---

