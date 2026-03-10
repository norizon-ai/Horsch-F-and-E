# Topic 24: vpn_password_access_tinygpu_ssh

Number of tickets: 35

## Tickets in this topic:

### 2022090742003714_FAU%20Netz.md
# Ticket 2022090742003714

 ```markdown
# HPC-Support Ticket: FAU Netz

## Summary
- **Subject:** FAU Netz
- **User Issue:** IP addresses of the user's research group were removed from the FAU network, causing difficulties in accessing login nodes without a VPN.
- **IP Ranges:**
  - Erlangen: 134.94.72.0/23 (134.94.72.1 - 134.94.73.254)
  - Nürnberg: 134.94.109.128/25 (134.94.109.129 - 134.94.109.254)

## Key Points
- **Root Cause:** IP addresses were removed from the FAU network, preventing direct access to login nodes.
- **User's Goal:** Avoid using a VPN to access login nodes (e.g., Meggie) at the RRZE.
- **Network Usage:** The IP ranges cover the working devices of the research group located in Erlangen and Nürnberg.

## Solution
- **Clarification:** The HPC Admin clarified that the IPv4 addresses were never able to access the login nodes directly due to the use of RFC1918 IPv4 addresses.
- **IPv6 Access:** The login nodes of newer clusters (Meggie, Fritz, Alex) have global routed IPv6 addresses, allowing direct access from IPv6-capable networks.
- **Action Required:** The user should contact their network department if IPv6 access is not functioning.

## Keywords
- FAU Netz
- IP Addresses
- VPN
- Login Nodes
- IPv6
- RFC1918
- Network Support
- Research Group

## Lessons Learned
- **IPv4 Limitations:** RFC1918 IPv4 addresses cannot be accessed directly from global IPv4 addresses.
- **IPv6 Capability:** Ensure that the network is IPv6-capable for direct access to login nodes.
- **Communication:** Clear communication with the network department is crucial for resolving IP-related issues.
```
---

### 2022020242002077_Antr%C3%83%C2%A4ge%20HPC-Account%20M.%20Sun%20und%20A.%20Sindel.md
# Ticket 2022020242002077

 # HPC Support Ticket Conversation Analysis

## Subject
Anträge HPC-Account M. Sun und A. Sindel

## Keywords
- HPC Account Applications
- IdM-Kennung
- HPC-Kennung
- Password Setup
- HPC-Cafe
- Cluster Alex
- TinyGPU
- Early Adopter Program

## Root Cause of the Problem
- Expired certificate
- New HPC account applications for two users
- Cluster Alex not in regular operation

## Solution
- **Account Setup**: HPC Admins created HPC-Kennung for both users and provided instructions for setting up passwords via IdM-Kennung.
- **Cluster Access**: For early access to Cluster Alex, users were directed to fill out the early adopter form. Alternatively, they were advised to use TinyGPU.
- **Support**: Users were encouraged to participate in the HPC-Cafe for additional support.

## General Learnings
- **Account Creation**: HPC Admins handle account creation and provide necessary credentials and instructions.
- **Cluster Access**: Specific clusters may require additional steps for access, such as filling out early adopter forms.
- **User Support**: Regular support sessions like HPC-Cafe are available for users to get help and guidance.
- **Communication**: Clear and timely communication is essential for resolving user requests and providing necessary information.

## Notes
- **Delay in Service**: There may be delays in setting up services on HPC servers, which can take up to 2 days.
- **Password Propagation**: Password changes may take several hours to propagate across HPC systems.
- **Alternative Resources**: In case of cluster unavailability, alternative resources like TinyGPU can be utilized.

## Conclusion
The ticket highlights the process of handling new HPC account applications, including account creation, password setup, and providing access to specific clusters. It also emphasizes the importance of user support and communication in resolving such requests.
---

### 2019040342002631_A%20question%20about%20access%20to%20the%20HPC%20resources.md
# Ticket 2019040342002631

 # HPC Support Ticket: Access to HPC Resources from Abroad

## Keywords
- HPC access
- Abroad access
- VPN
- Proxy
- FAU network
- Private IP addresses
- Dialog servers

## Problem
- User inquires about accessing HPC resources from abroad.
- Concern about needing a proxy or VPN to obtain an FAU IP address.

## Root Cause
- HPC systems at RRZE use private IP addresses that are only accessible within the FAU network.

## Solution
- Use dialog servers as the entry point for accessing HPC clusters from outside the FAU network.
- Alternatively, use a VPN to connect to the FAU network.

## Reference
- [Dialog Server Anleitung](https://www.anleitungen.rrze.fau.de/hpc/dialogserver/)

## General Learning
- HPC systems with private IP addresses require specific methods for external access.
- Dialog servers and VPNs are common solutions for secure remote access to HPC resources.

## Notes
- Ensure users are aware of the necessary steps to access HPC resources remotely.
- Provide clear documentation and support for setting up VPN and using dialog servers.
---

### 2025020842001052_Regarding%20TinyGPU%20Access.md
# Ticket 2025020842001052

 # HPC Support Ticket Conversation Analysis

## Keywords
- SSH access
- TinyGPU
- Password issues
- Vault directory
- Lecture accounts
- HPC access for model training

## Root Cause of Problems
1. **TinyGPU Access**: User unable to access TinyGPU using the same password as for `csnhr.nhr.fau.de`.
2. **Vault Directory**: User unable to access `/home/vault` directory, receiving "No such file or directory" error.

## Solutions Provided
1. **Vault Directory**:
   - **Issue**: Lecture accounts do not have access to `/home/vault` due to their short-term nature.
   - **Solution**: Use `$WORK` directory instead for storage.

2. **TinyGPU Access**:
   - **Issue**: User attempted to access TinyGPU with incorrect credentials.
   - **Solution**: HPC accounts are bound to specific purposes (e.g., lectures, thesis work). Access to TinyGPU for general model training and self-learning is not permitted.

## General Learnings
- **Storage Directories**: Understand the purpose and access rights of different storage directories (`$WORK`, `$HOME`, `/home/vault`).
- **Account Purpose**: HPC accounts are tied to specific purposes and have limited access based on those purposes.
- **Password Management**: Ensure users are aware of the correct credentials for different systems and resources.

## Documentation for Support Employees
- **Vault Directory Access**: Inform users that lecture accounts do not have access to `/home/vault`. Direct them to use `$WORK` for storage.
- **TinyGPU Access**: Clarify that access to resources like TinyGPU is restricted to specific purposes and not available for general use.

---

This analysis provides a concise overview of the issues faced by the user and the solutions provided by the HPC Admins, which can be used as a reference for future support cases.
---

### 2021060842000286_Anmeldung%20auf%20Woody%20Cluster%20abgeblockt.md
# Ticket 2021060842000286

 # HPC Support Ticket: Anmeldung auf Woody Cluster abgeblockt

## Keywords
- SSH
- Password
- IDM Portal
- VPN
- Arch Linux
- Cisco AnyConnect
- HPC Account
- SSH Config

## Problem Description
- User unable to log in to Woody Cluster via SSH despite knowing the correct password.
- User changed the password in the IDM Portal but still faced login issues.
- Error message: `Permission denied, please try again.`

## Root Cause
- Password changes in the IDM Portal take several hours to propagate to the HPC systems.
- Possible misconfiguration in the SSH config file.

## Solution
- Confirm the correct username (`mpwm023h` with "h" at the end).
- Wait for several hours for the password change to take effect.
- Verify and adjust the SSH config file if necessary.

## Lessons Learned
- Password changes in the IDM Portal require time to sync with HPC systems.
- Ensure the correct username is used for login attempts.
- Regularly check the SSH config file for any potential issues.

## Additional Notes
- The user was able to log in with the old password after adjusting the SSH config file.
- The new password should be effective after several hours.

## Relevant Roles
- **HPC Admins**: Provided guidance on the username and password sync delay.
- **2nd Level Support Team**: Can assist with similar issues in the future.

## Tools and Systems Involved
- Woody Cluster
- IDM Portal
- SSH
- VPN (Cisco AnyConnect)
- Arch Linux

## Conclusion
- Ensure users are aware of the delay in password synchronization.
- Verify usernames and SSH configurations to troubleshoot login issues.
---

### 2022092142004955_error%20in%20connecting%20to%20tinygpu%20cluster.md
# Ticket 2022092142004955

 # HPC Support Ticket: Error in Connecting to TinyGPU Cluster

## Keywords
- SSH connection error
- TinyGPU cluster
- Remote access
- Authentication issue

## Summary
A user reported an issue with connecting to the TinyGPU cluster via SSH. The error occurred when attempting to use the command `ssh iwi5095h@woody.rrze.fau.de`.

## Root Cause
The root cause of the problem was not explicitly stated in the initial message, but it is likely related to an SSH authentication or network configuration issue.

## Solution
The solution was not provided in the initial message. Further investigation by the 2nd Level Support team or HPC Admins is required to diagnose and resolve the issue.

## Steps for Diagnosis
1. **Check SSH Key Configuration**: Ensure that the SSH keys are correctly configured and the public key is added to the authorized_keys file on the server.
2. **Verify Network Connectivity**: Check if the user can ping the server or access other services on the same network.
3. **Review Error Logs**: Examine the SSH error logs on both the client and server sides for more detailed error messages.
4. **Authentication Methods**: Confirm that the user is using the correct authentication method (e.g., password, key-based authentication).

## Next Steps
- The 2nd Level Support team should contact the user for more details and request the error screenshot if not already provided.
- HPC Admins may need to review the server logs and network configuration to identify any potential issues.

## Notes
- This issue highlights the importance of proper SSH configuration and network connectivity for accessing HPC resources.
- Regular training sessions on remote access and SSH configuration, led by Georg Hager, can help users avoid such issues in the future.
---

### 2024022942001863_FW%3A%20SAMPLE3D%20Workshop.md
# Ticket 2024022942001863

 # HPC-Support Ticket Conversation Analysis

## Keywords
- SAMPLE3D Workshop
- IdM Account
- VPN Setup
- Cisco-Client
- HPC Account
- FAU Services
- Workshop Materials
- Activation Letter
- RRZE Helpdesk
- HPC Portal
- SSH Keys

## General Learnings
- Users may face issues with account expiration and VPN setup.
- The RRZE Helpdesk is the primary point of contact for account-related issues.
- Detailed instructions for VPN setup are crucial for non-native speakers.
- Workshop materials and activation letters are essential for participation.
- HPC account management and access require specific instructions and support.

## Root Cause of Problems
1. **Account Expiration**: The user's IdM account expired earlier than expected, causing access issues.
2. **VPN Setup**: The user encountered difficulties setting up the VPN due to lack of English instructions and technical issues.
3. **HPC Account Management**: The user was unaware of the migration process and required guidance on accessing the HPC portal.

## Solutions
1. **Account Expiration**:
   - The user was advised to contact the RRZE Helpdesk to extend the account.
   - The HPC Admin confirmed that the account was still active and provided further assistance.

2. **VPN Setup**:
   - Detailed instructions were provided by the IT expert, including steps for downloading and installing the Cisco-Client.
   - The user was advised to log in to the IDM-Portal with their IDM-ID and password to initiate the download.

3. **HPC Account Management**:
   - The user was informed about the migration of HPC accounts and the requirement for SSH keys.
   - Guidance was provided on logging into the HPC portal using the IdM account.

## Documentation for Support Employees

### Account Expiration
**Issue**: User's IdM account expired earlier than expected.
**Solution**:
- Advise the user to contact the RRZE Helpdesk for account extension.
- Confirm the account status with the HPC Admin.

### VPN Setup
**Issue**: User faced difficulties setting up the VPN due to lack of English instructions and technical issues.
**Solution**:
- Provide detailed instructions for downloading and installing the Cisco-Client.
- Instruct the user to log in to the IDM-Portal with their IDM-ID and password to initiate the download.

### HPC Account Management
**Issue**: User was unaware of the migration process and required guidance on accessing the HPC portal.
**Solution**:
- Inform the user about the migration of HPC accounts and the requirement for SSH keys.
- Provide guidance on logging into the HPC portal using the IdM account.

This documentation will help support employees address similar issues in the future.
---

### 2024072542002619_Zugang%20zu%20TinyGPU%20f%C3%83%C2%BCr%20Bachelorarbeit.md
# Ticket 2024072542002619

 # HPC Support Ticket: Access to TinyGPU for Bachelor Thesis

## Keywords
- HPC Account
- TinyGPU
- Bachelor Thesis
- Transformer Network
- Lehrstuhl
- HPC Portal
- Account Management

## Summary
A user requested access to TinyGPU for their bachelor thesis to train a transformer network. The user provided their details and their supervisor's information.

## Root Cause
The user's supervisor does not have an account in the HPC Portal, which is necessary for creating and managing HPC accounts.

## Solution
- **Account Creation**: HPC accounts are managed through Lehrstühle (chairs). The user should discuss with their supervisor which chair they are associated with.
- **Contact Information**: The user should contact the HPC support team using their university email address.
- **Additional Information**: Further details on account management can be found on the [HPC Portal Management Tab](https://doc.nhr.fau.de/hpc-portal/#the-management-tab-visible-only-for-pis-and-technical-contacts).

## General Learnings
- HPC accounts are managed through Lehrstühle.
- Users should use their university email for official communications.
- Detailed information on account management is available on the HPC Portal.

## Next Steps
- The user should discuss with their supervisor to identify the appropriate Lehrstuhl.
- The user should contact the HPC support team using their university email address for further assistance.
---

### 2023070442003169_HPC%20Accounts%20for%20HESP%20lecture%20are%20not%20working%20on%20alex%20cluster.md
# Ticket 2023070442003169

 # HPC Support Ticket: GPU Cluster Access Issue

## Keywords
- HPC Account
- GPU Clusters
- Access Issue
- VPN
- Entry Node
- Account Activation
- Password Distribution

## Problem Description
- Users participating in a course were unable to connect to GPU clusters (alex, fritz) despite having HPC accounts.
- Users could connect to the entry node and other clusters (meggie, woody) but were immediately disconnected from GPU clusters with the message: "This account is currently not available."
- Users could not log in to tinyx clusters as their passwords were not accepted.

## Root Cause
- The accounts were not yet activated for the alex cluster.
- There was a mention of an expired certificate, which might have contributed to the issue.

## Solution
- HPC Admin activated the accounts for the alex cluster using the following commands:
  ```bash
  sacctmgr add account rzku parent=fau
  for i in $(seq 25 34); do /root/bin/add-early-user.sh iwgr0${i}h 1 1 1; done
  ```
- Users were informed that it might take up to 24 hours for the password to be distributed and for them to be able to log in.

## General Learnings
- New accounts may not have immediate access to all clusters and may require manual activation by HPC Admins.
- Password distribution after modification in IDM can take up to 24 hours.
- Expired certificates can cause connection issues.
- Users should test access to multiple nodes to isolate the issue.
---

### 42085273_Ihre%20HPC-Kennung.md
# Ticket 42085273

 # HPC Support Ticket Conversation Analysis

## Keywords
- HPC-Kennung (HPC ID)
- VPN-Client
- Uninetz (University Network)
- Access denied
- Dialogserver
- HPC-Server (memoryhog)
- IDM (Identity Management)

## General Learnings
- **HPC ID Setup**: New HPC IDs are created and require users to set a password via the IDM portal.
- **Access Delay**: It can take up to 2 days for HPC services to be fully set up and accessible.
- **VPN Access**: HPC servers are generally accessible within the university network but may require manual routing adjustments for VPN access.
- **Dialogserver**: The recommended method for external access to HPC systems is through the Dialogserver.

## Root Cause of the Problem
- **Access Issue**: The user received an "Access denied" message when attempting to log in with the new HPC ID.
- **VPN Configuration**: The VPN client may not include all necessary routes for HPC systems.

## Solution
- **Account Propagation**: Ensure the HPC account is propagated to all relevant systems, which may take up to 2 days.
- **Dialogserver Usage**: Use the Dialogserver for external access to HPC systems.
- **Manual Routing**: If using VPN, manual routing adjustments may be necessary to include all HPC system networks.

## Additional Notes
- **IDM and Mail Issues**: There were potential issues with mail-postfach-änderungen and IDM-Zuordnung that needed to be resolved.
- **Documentation**: The Dialogserver usage is documented and recommended for external access.

This analysis provides a structured overview of the conversation, highlighting key points and solutions for future reference in similar support cases.
---

### 2023101042003749_Re%3A%20New%20invitation%20for%20%22Studentische%20Abschlu%C3%83%C2%9Farbeiten%20Tier3%20Grundversor.md
# Ticket 2023101042003749

 # HPC Support Ticket Conversation Analysis

## Keywords
- HPC Portal
- SSH Key
- Tinygpu Access
- Password Authentication
- SSO (Single Sign-On)
- IdM Credentials

## Summary
The user encountered issues accessing the Tinygpu cluster using a password. The HPC Admin clarified that the account does not have a password and access is only possible with an SSH key uploaded to the HPC portal.

## Root Cause of the Problem
- The user attempted to access the Tinygpu cluster using a password instead of an SSH key.

## Solution
- The user needs to upload an SSH public key to the HPC portal and configure SSH to use the key when connecting.
- Detailed instructions are available at [HPC SSH Access Documentation](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/).

## General Learnings
- HPC accounts do not use passwords for access; SSH keys are required.
- Users should follow the instructions provided in the invitation email to upload their SSH public key.
- Configuring SSH to use the key is essential to avoid password prompts.

## Relevant Links
- [HPC SSH Access Documentation](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/)
- [HPC Portal](https://portal.hpc.fau.de/)

## Roles Involved
- **HPC Admins**: Provided detailed instructions and clarifications.
- **User**: Requested assistance with accessing the Tinygpu cluster.

## Next Steps for Support
- Ensure the user has uploaded the SSH key correctly.
- Provide additional guidance on configuring SSH if needed.
- Verify that the user can access the Tinygpu cluster using the SSH key.
---

### 2022120942002732_probelm%20with%20tinyx.md
# Ticket 2022120942002732

 # HPC Support Ticket: Problem with Accessing tinyx

## Keywords
- SSH access
- Permission denied
- Password propagation
- HPC systems
- tinyx
- woody

## Problem Description
- User unable to access `tinyx` via SSH, receiving "permission denied" error.
- User can access `woody` with the same credentials.
- User attempted access using: `ssh tinyx.nhr.fau.de -l bctc017h`

## Logs and Diagnostics
- Multiple failed password attempts logged for the user on `tinyx`.
- Example log entries:
  ```
  Dec  9 13:09:44 tinyx sshd[1302797]: Failed password for bctc017h from 131.188.128.65 port 54074 ssh2
  Dec  9 14:14:33 tinyx sshd[1607613]: Failed password for bctc017h from 10.28.244.15 port 53058 ssh2
  ```

## Root Cause
- Password changes take several hours to propagate to all HPC systems.

## Solution
- Inform the user that password changes may take several hours to propagate to all systems.
- Advise the user to wait and attempt access again later.

## General Learning
- Password synchronization across HPC systems is not instantaneous and may take several hours.
- Users should be informed about potential delays in password propagation when troubleshooting access issues.

## Next Steps for Support
- Monitor the situation and ensure the user is informed about the propagation delay.
- Verify if the issue persists after the expected propagation time and provide further assistance if needed.
---

### 2023021642001684_Access%20to%20TinyGPU.md
# Ticket 2023021642001684

 # HPC Support Ticket: Access to TinyGPU

## Keywords
- Access Denied
- Password Issues
- SSH
- TinyGPU
- Password Propagation Delay

## Problem Description
- User can access the HPC cluster but faces access denial when trying to access TinyGPU due to password issues.
- Commands used:
  ```sh
  ssh user@cshpc.rrze.fau.de -t ssh user@tinyx
  ssh user@cshpc.rrze.fau.de
  ssh user@tinyx
  ```
- Password accepted for `cshpc` but fails for `tinyx`.

## Root Cause
- Password propagation delay: New password takes a few hours to propagate to all HPC systems.

## Solution
- Wait for a few hours for the password to propagate.
- Alternative command that worked:
  ```sh
  ssh <user>@tinyx.nhr.fau.de
  ```

## Lessons Learned
- Password changes may not be immediate across all systems.
- Users should wait for password propagation or try alternative commands.

## Ticket Status
- Closed as the issue was resolved.
---

### 2025020942000481_Alex%20Cluster%20Access%20Problem.md
# Ticket 2025020942000481

 ```markdown
# HPC Support Ticket: Alex Cluster Access Problem

## Keywords
- Alex Cluster
- Account Access
- Account Reactivation
- TinyGPU
- Documentation

## Summary
A user reported being unable to access the Alex cluster, despite having access to other clusters like TinyGPU. The user's account had been deactivated and then reactivated recently.

## Root Cause
- The user never had access to the Alex cluster.

## Solution
- The HPC Admin confirmed that the user's account (iwi5229h) never had access to the Alex cluster.
- The user was directed to the documentation for gaining access to the Alex cluster: [Accessing Alex](https://doc.nhr.fau.de/clusters/alex/#accessing-alex).

## Lessons Learned
- Always verify if a user has the necessary permissions for a specific cluster.
- Provide clear documentation on how to request access to specific clusters.
- Misunderstandings about account permissions can occur, especially after account reactivation.

## Actions Taken
- The HPC Admin confirmed the user's lack of access to the Alex cluster.
- The user was informed about the correct procedure to gain access.
- The ticket was closed after the user acknowledged the clarification.
```
---

### 2024052442001411_Regarding%20accessing%20tinygpu%20from%20HOME-PC.md
# Ticket 2024052442001411

 # HPC Support Ticket: Accessing TinyGPU from Home PC

## Keywords
- SSH
- VPN
- Public Key
- SSH Config
- Proxy Jumping
- Cisco Full-Tunnel

## Problem
- User unable to connect to TinyGPU and Meggie from home PC via SSH.
- Error message: `Permission denied (publickey,hostbased)`.

## Root Cause
- SSH key pair not properly configured on the home PC.
- SSH config not set up as per the documentation.

## Solution
1. **Generate SSH Key Pair on Home PC:**
   - Create a new SSH key pair on the home PC.
   - Upload the public key to the HPC portal.

2. **Set Up SSH Config:**
   - Configure the SSH config file as described in the [documentation](https://doc.nhr.fau.de/access/ssh-command-line/).
   - This enables proxy jumping and eliminates the need for VPN.

3. **Use Cisco Full-Tunnel Option (if SSH config is not set up):**
   - If the SSH config is not set up, use the Cisco “full-tunnel” option to connect via VPN.

## General Learnings
- Proper SSH key pair generation and configuration are crucial for secure and seamless access to HPC resources.
- Setting up the SSH config simplifies the connection process and can eliminate the need for VPN.
- Multiple SSH keys can be uploaded to the HPC portal for different devices.

## Documentation Reference
- [SSH Command Line Access Documentation](https://doc.nhr.fau.de/access/ssh-command-line/)
---

### 2017080242001282_HPC%20TinyGPU%20request.md
# Ticket 2017080242001282

 # HPC Support Ticket: TinyGPU Request

## Keywords
- TinyGPU
- HPC Account
- Password Reset
- Account Reactivation
- Project Access

## Summary
A user requested access to TinyGPUs for a research project. The user already had an HPC account, which was reactivated for the new project.

## Root Cause
- User expected the account to have expired at the end of the last semester.
- User needed TinyGPU access added to the existing account.

## Solution
- HPC Admin informed the user that the account was still active and provided instructions for password reset if needed.
- HPC Admin confirmed that the account was valid for TinyGPU access.

## General Learnings
- Users may not be aware of the status of their HPC accounts.
- Reactivating an account for a new project can resolve access issues.
- Clear communication about account status and access permissions is essential.

## Actions Taken
- HPC Admin acknowledged the receipt of the application.
- HPC Admin informed the user about the existing account and provided password reset instructions.
- HPC Admin confirmed the account's validity for TinyGPU access.

## Follow-up
- No further action was required as the user's account was confirmed to be valid for TinyGPU access.
---

### 2022102142003373_Error%20while%20running%20the%20script.md
# Ticket 2022102142003373

 ```markdown
# HPC Support Ticket: Error while running the script

## Keywords
- GPU request error
- Login node
- Documentation
- Expired certificate

## Summary
A user encountered an error while requesting a specific GPU and sought guidance from the HPC support team.

## Root Cause
- The user was attempting to run the script on the wrong login node.
- The certificate had expired.

## Solution
- The HPC Admin advised the user to refer to the documentation for the correct login node.
- Documentation link provided: [TinyGPU Cluster Documentation](https://hpc.fau.de/systems-services/documentation-instructions/clusters/tinygpu-cluster/)

## General Learnings
- Ensure users are on the correct login node when running scripts.
- Check for expired certificates and renew them if necessary.
- Always refer users to the relevant documentation for detailed instructions.
```
---

### 2021081842002771_Login%20Woody.md
# Ticket 2021081842002771

 # HPC Support Ticket: Login Issue on Woody

## Keywords
- SSH login
- Password synchronization
- HPC systems
- Password hash
- VPN

## Problem Description
- User unable to login to Woody via SSH, both from external VPN and from another HPC system (Emmy).
- Error message: `Permission denied, please try again.`

## Root Cause
- User recently changed their HPC password.
- Password changes take several hours to propagate across all HPC systems.
- Woody had not yet updated the password hash, causing the login failure.

## Solution
- Wait for the password synchronization process to complete.
- Retry logging in after some time.

## General Learnings
- Password changes may not immediately take effect on all HPC systems.
- Some systems may update faster than others.
- If experiencing login issues after a password change, wait and retry later.
- This delay is a normal part of the password synchronization process.
---

### 2024090642003231_Regarding%20HPC%20Access.%20Password%20required%20while%20accessing%20Alex%20cluster.md
# Ticket 2024090642003231

 ```markdown
# HPC Support Ticket: Accessing Alex Cluster

## Keywords
- HPC Access
- Alex Cluster
- Password Issue
- SSH Keys
- Jupyterhub
- TinyGPU
- Representation Learning

## Problem Description
- **User Issue**: User attempting to access Alex HPC cluster for a project on Representation Learning encounters a password prompt.
- **Root Cause**: Access to Alex cluster was not requested or enabled for the "Representation Learning" lecture.

## Solution
- **HPC Admin Response**:
  - Access to Alex cluster is not enabled for the user's lecture.
  - User should use TinyGPU instead.
  - User accounts do not have passwords; SSH keys must be used for access (or go through the HPC portal to access Jupyterhub).
  - Tutors of the lecture should assist with general problems like setting up SSH.

## General Learnings
- **Access Restrictions**: Ensure that access to specific HPC clusters is requested and enabled for the relevant lecture or project.
- **Authentication Methods**: HPC accounts typically use SSH keys for authentication, not passwords.
- **Alternative Resources**: When access to a specific cluster is not available, alternative resources like TinyGPU may be used.
- **Support Channels**: Tutors and lecture organizers can provide additional support for setting up and accessing HPC resources.

## Next Steps
- **User**: Contact the lecture tutor (Mischa Dombrowski) for further assistance with setting up SSH and accessing TinyGPU.
- **HPC Admin**: No further action required unless additional support is needed.
```
---

### 2023013142002058_TinyGPU%20access.md
# Ticket 2023013142002058

 # HPC Support Ticket: TinyGPU Access

## Keywords
- HPC account activation
- Directory creation
- Account expiration
- Service and directory availability

## Problem
- User unable to access specific directory (`/woody/iwi5063h`) after account activation.
- Root cause: Account had expired and was recently reactivated.

## Solution
- Wait until the next day for all services and directories to become available after account reactivation.

## General Learnings
- Account reactivation may take time to propagate through all services and directories.
- Users should be informed about potential delays in service availability after account reactivation.

## Roles Involved
- HPC Admins
- User (researcher/student)
---

### 2023040342000848_Cannot%20login%20to%20Alex%20or%20TinyGPU.md
# Ticket 2023040342000848

 # HPC Support Ticket: Cannot Login to Alex or TinyGPU

## Keywords
- SSH Key
- Login Issue
- Public Key
- Private Key
- Key Pair Generation

## Problem Description
- User unable to login to TinyGPU despite updating the public key in their HPC account.
- User can login to HPC using SSH key but faces issues with TinyGPU.

## Root Cause
- The issue likely stems from the private key not being accessible on cshpc.

## Solution
- Generate a new key pair on cshpc.
- Update the public part of the key to the user's HPC account as per the FAQs.

## Lessons Learned
- Ensure that the private key is accessible on the machine from which you are attempting to login.
- Follow the FAQs for generating and updating SSH keys.
- Be specific in support requests to facilitate quicker resolution.

## References
- [FAQs on SSH Key Management](https://hpc.fau.de/faqs/#innerID-13183)
---

### 2017120742000337_VPN%20service.md
# Ticket 2017120742000337

 ```markdown
# HPC-Support Ticket: VPN Service

## Keywords
- VPN
- CISCO AnyConnect Secure Mobility Client
- HPC Service
- Lima
- Emmy
- Gaussian
- Amber16
- GPU
- CPU
- Protein Modeling

## Summary
The user has successfully installed and connected to the VPN using the CISCO AnyConnect Secure Mobility Client but needs assistance in connecting to the HPC service (Lima or Emmy) to use Gaussian and Amber16 for protein modeling on GPUs and CPUs.

## Root Cause
- User is a novice and requires guidance on connecting to the HPC service after successfully setting up the VPN.

## Solution
- Provide detailed instructions on how to connect to the HPC service (Lima or Emmy) after VPN setup.
- Include steps for accessing Gaussian and Amber16 for protein modeling.

## General Learnings
- Users may need additional guidance beyond initial VPN setup to connect to specific HPC services.
- Clear documentation on connecting to HPC services and accessing specific software tools is essential for novice users.
```
---

### 2024030242000233_SSH%20to%20tiny%20cluster%20gives%20public%20key%20error.md
# Ticket 2024030242000233

 ```markdown
# SSH to Tiny Cluster Gives Public Key Error

## Keywords
- SSH
- Public Key Error
- Permission Denied
- Configuration Error
- Cfengine
- PasswordAuthentication
- Match

## Problem Description
- User unable to SSH into the tiny cluster.
- Error message: `Permission denied (publickey,hostbased)`.
- Issue started overnight after previously successful logins.

## Root Cause
- Configuration error introduced by Cfengine.
- `PasswordAuthentication no` line was added before the `Match` line, causing authentication issues.

## Solution
- Corrected the configuration using `BeginGroupIfNoLineContaining` to ensure proper order of lines.
- Ensured that only portal accounts are not prompted for passwords.

## Lessons Learned
- Configuration management tools like Cfengine can introduce errors if not properly configured.
- Order of lines in configuration files is crucial for proper functionality.
- Regular monitoring and quick response to configuration changes can prevent prolonged downtime.
```
---

### 2022102442004241_Unable%20to%20access%20home%20directory.md
# Ticket 2022102442004241

 ```markdown
# HPC Support Ticket: Unable to Access Home Directory

## Keywords
- Home directory access
- Permission denied
- Account termination
- IDM misconfiguration
- Certificate expiration

## Summary
A user reported being unable to access their home directory on the TinyGPU cluster, receiving a "Permission denied" error.

## Root Cause
- The user's account was marked for termination by a supervisor.
- Misconfiguration in the Identity Management (IDM) system.
- Expired certificate.

## Conversation Highlights
- **User Report**: Unable to access home directory, receiving "Permission denied" error.
- **HPC Admin Response**: Account termination requested by supervisor. Misconfiguration in IDM system noted.

## Solution
- The user was informed that their account was terminated as per the request of their supervisor.
- The HPC Admin noted a misconfiguration in the IDM system and an expired certificate.

## Lessons Learned
- Ensure proper communication with users regarding account termination.
- Regularly check IDM configurations to avoid misconfigurations.
- Monitor certificate expiration dates to prevent access issues.
```
---

### 2023060142003854_Cannot%20access%20HPC%20account.md
# Ticket 2023060142003854

 # HPC Support Ticket: Cannot Access HPC Account

## Keywords
- HPC Account Access
- Password Update Delay
- VPN Connection
- Permission Denied

## Problem Description
- User recently obtained an HPC account and changed the password.
- User receives "permission denied" error when attempting to log in.

## Root Cause
- Password update delay: It takes a few hours for the system to update the password on all clusters.
- Network issue: User was not connected to the university network or VPN.

## Troubleshooting Steps
1. **Wait for Password Update**: Instruct the user to wait for a few hours after changing the password to allow the system to update.
2. **Check Login Attempts**: Verify if there are any login attempts in the logs.
3. **Verify Network Connection**: Ensure the user is connected to the university network or VPN.

## Solution
- **Wait for Password Sync**: Advise the user to wait for the password to sync across all clusters.
- **Connect to VPN**: Ensure the user is connected to the VPN if they are not on the university network.

## Notes
- Users should be informed about the delay in password updates.
- Ensure users are aware of the network requirements for accessing HPC resources.

## Follow-up
- If the issue persists, further investigation into the user's account and network configuration may be necessary.
---

### 2024030142003474_Zugang%20tinygpu%20gest%C3%83%C2%B6rt%20-%20mppm001h.md
# Ticket 2024030142003474

 # HPC Support Ticket: Access Issue to tinygpu

## Keywords
- SSH keys
- Permission denied
- Connection refused
- HPC portal
- Cluster frontends
- Erratic behavior

## Problem Description
The user reports intermittent issues when trying to connect from `cshpc` to `tinyx` or other cluster frontends. The errors include:
- "Permission denied (publickey,password,hostbased)"
- "Connection refused"
- "Permission denied (publickey,hostbased)"

The user has already set up SSH keys for their own machines on the HPC portal but is unsure if additional keys are needed for internal HPC infrastructure.

## Root Cause
The root cause of the problem is likely related to SSH key configuration or permissions within the HPC infrastructure.

## Solution
The HPC Admin provided a link to the FAQ for further troubleshooting:
- [FAQ: I managed to log in to t40 with an SSH key, but get asked for a password - permission denied when continuing to a cluster frontend](https://doc.nhr.fau.de/faq/#i-managed-to-log-in-to-t40--with-an-ssh-key--but-get-asked-for-a-password---permission-denied-when-continuing-to-a-cluster-frontend)

## General Learning
- Ensure SSH keys are properly configured for all necessary connections within the HPC infrastructure.
- Refer to the FAQ for common issues related to SSH key authentication and permissions.
- Erratic behavior in SSH connections can often be resolved by verifying key configurations and permissions.
---

### 2021110342002194_HPC%20Use%20-%20Tinygpu.md
# Ticket 2021110342002194

 # HPC Support Ticket: HPC Use - TinyGPU

## Keywords
- HPC Account
- Woody-Cluster
- TinyGPU Cluster
- Mini-Project
- Account Access

## Summary
A user inquired about accessing the TinyGPU cluster in addition to the Woody-Cluster for their mini-project.

## Root Cause
The user was unsure if they needed to fill out an additional form to access the TinyGPU cluster or if they could simply be added to it.

## Solution
The HPC Admin confirmed that the user's existing HPC account allows them to use the TinyGPU cluster without needing to fill out an additional form.

## General Learnings
- Users with an HPC account can access multiple clusters without needing to submit separate applications for each cluster.
- It is important to communicate clearly with users about the scope of their HPC account access.

## Actions Taken
- The HPC Admin provided the user with the necessary information about their account access.
- The ticket was resolved by confirming that no additional form was required for accessing the TinyGPU cluster.

## Notes
- Ensure that users are aware of the clusters they have access to with their HPC account to avoid confusion.
- Maintain clear communication channels for users to inquire about their account capabilities.
---

### 2024012542003478_Not%20able%20to%20login%20to%20TinyGPU.md
# Ticket 2024012542003478

 # HPC Support Ticket: Unable to Login to TinyGPU

## Keywords
- SSH login issue
- Permission denied
- VPN network
- Password prompt
- Discontinued account
- TinyGPU, Woody, Meggie nodes
- MacOS Terminal

## Problem Description
User is unable to connect to `tinyX` instances via SSH, despite being able to connect to other nodes (`woody` and `meggie`). The user receives a "Permission denied" error after entering the password. The user suspects the issue might be related to a previously discontinued HPC account.

## Setup
- User is connected via FAU VPN network.
- User can connect to other nodes (`woody` and `meggie`).
- Using MacOS default Terminal.
- Password has not been changed.

## Steps Tried by User
- Copied password from plaintext note into command line.
- Attempted to use the old account's password.

## Root Cause
Potential issues could be:
- Incorrect password for the current account.
- Account not properly reactivated after previous discontinuation.
- Incorrect username or node address.

## Solution
- **HPC Admins** should verify the user's account status and ensure it is properly authorized for `tinyX` instances.
- **2nd Level Support** can assist in resetting the user's password if necessary.
- Ensure the user is using the correct username and node address for `tinyX`.

## General Learnings
- Always verify account status and permissions when users report login issues.
- Check for potential conflicts with previously discontinued accounts.
- Ensure users are using the correct credentials and node addresses.

## Next Steps
- **HPC Admins** to check account status and permissions.
- **2nd Level Support** to assist with password reset if needed.
- Confirm correct username and node address with the user.
---

### 2023050942003501_Unable%20to%20login%20on%20HPC%20cluster.md
# Ticket 2023050942003501

 # HPC Support Ticket: Unable to Login on HPC Cluster

## Keywords
- Login issue
- Account unavailable
- HPC cluster
- IDM
- Fritz
- Alex
- TinyGPU
- Restricted access mode

## Problem Description
- User unable to login to HPC cluster using IDM credentials.
- Initial welcome message followed by "the account is currently unavailable" error.

## Root Cause
- User's certificate has expired.
- User requires access to TinyGPU but attempted to log in to Fritz or Alex, which are in restricted access mode.

## Solution
- User directed to follow instructions for TinyGPU cluster access.
- If access to Fritz or Alex is needed, user instructed to follow specific cluster access instructions.

## Links to Documentation
- [TinyGPU Cluster Documentation](https://hpc.fau.de/systems-services/documentation-instructions/clusters/tinygpu-cluster/)
- [Alex Cluster Documentation](https://hpc.fau.de/systems-services/documentation-instructions/clusters/alex-cluster/)
- [Fritz Cluster Documentation](https://hpc.fau.de/systems-services/documentation-instructions/clusters/fritz-cluster/)

## Notes
- Always verify the cluster you are attempting to access.
- Ensure certificates and access permissions are up to date.
- Follow cluster-specific documentation for access instructions.
---

### 2021120942000594_HPC%20Erweiterung%20Zielsysteme.md
# Ticket 2021120942000594

 # HPC Support Ticket: HPC Erweiterung Zielsysteme

## Keywords
- HPC Antrag
- Zielsystem
- TinyGPU
- Department Kapazitäten
- AIBE
- A100
- A40
- Early Adopter

## Problem
- User requested an extension of HPC access for a specific user from TinyGPU to department capacities (TG090 - TG097).
- User mentioned that the certificate has expired.

## Root Cause
- The initial HPC application was only for the TinyGPU system.
- The user requested an extension to include additional department capacities.

## Solution
- The HPC Admin confirmed that the user's account is already enabled for the entire TinyGPU cluster, including AIBE A100.
- The admin noted that access to A40 is not yet available in normal operation and can only be assigned through the early adopter program.
- The A100 in Alex is not yet available.

## General Learnings
- Ensure that HPC applications specify all required systems and capacities.
- Understand the availability and access procedures for different HPC resources, such as early adopter programs.
- Communicate clearly with users about the status of their requests and the availability of resources.

## Actions Taken
- The request was initially deferred due to the need for an HPC application and capacity extension.
- The HPC Admin provided detailed information about the current access status and the availability of requested resources.

## Next Steps
- Inform the user about the early adopter program for A40 access.
- Monitor the availability of A100 in Alex and update the user accordingly.

## References
- [Early Adopter Program](https://hpc.fau.de/early-adopter-alex/)
- [HPC Services](http://hpc.fau.de/)

## Contact
- HPC Services: [support-hpc@fau.de](mailto:support-hpc@fau.de)
---

### 2022110242001417_Host%20name%20error.md
# Ticket 2022110242001417

 # HPC Support Ticket: Host Name Error

## Keywords
- Host name error
- Login issue
- VPN connection
- tinyFat
- woody.nhr.fau.de

## Problem Description
User reported being unable to log in and access `tinyFat`. The user mentioned that `woody.nhr.fau.de` was still accessible.

## Root Cause
The user discovered that the FAU VPN connection was lost, which prevented access to `tinyFat`.

## Solution
Reconnecting to the FAU VPN resolved the issue, allowing the user to log in and access `tinyFat` successfully.

## Lessons Learned
- Always check VPN connectivity when encountering login or access issues.
- Ensure that VPN connections are stable and active for accessing specific HPC resources.

## Ticket Conversation Summary
- User reported login issue with `tinyFat`.
- User later identified and resolved the issue by reconnecting to the FAU VPN.
- HPC Admin acknowledged the resolution.

## Recommendations
- Include VPN connectivity checks in troubleshooting steps for login issues.
- Educate users on the importance of maintaining active VPN connections for accessing certain HPC resources.
---

### 2024020742001967_Zugang%20zu%20tinyx.nhr.fau.de.md
# Ticket 2024020742001967

 # HPC Support Ticket: Access to TinyGPU Cluster

## Keywords
- TinyGPU Cluster
- Tier3 Accounts
- Access Issues
- Automatic Account Activation

## Summary
A user requested access to the TinyGPU cluster but encountered issues despite having a Tier3 account. The HPC admin confirmed that all Tier3 accounts are automatically enabled on TinyGPU. The user later resolved the issue independently.

## Problem
- User unable to access TinyGPU cluster despite having a Tier3 account.

## Root Cause
- The user did not specify the exact issue but later found it to be a trivial problem.

## Solution
- The user resolved the issue independently.

## Lessons Learned
- Tier3 accounts are automatically enabled on TinyGPU.
- Users should check for simple, trivial issues before requesting support.

## Actions Taken
- HPC admin confirmed automatic account activation for Tier3 users on TinyGPU.
- User resolved the issue independently.

## Follow-up
- No further action required from HPC support.
---

### 42164823_Account.md
# Ticket 42164823

 ```markdown
# HPC Support Ticket: Account Access Issue

## Keywords
- Account access
- VPN
- Password reset
- Remote access
- IDM portal

## Summary
A user reported being unable to log in to their HPC account while away from the university. The issue was initially suspected to be related to VPN configuration or distance but was later identified as a password problem.

## Root Cause
- Incorrect password attempts were logged.
- The user was unaware of the remote access procedure and password reset options.

## Solution
- The HPC Admin advised the user to use the `cshpc.rrze.uni-erlangen.de` server for remote access.
- The user was informed that their HPC account is linked to their IDM student account and can reset the password through the IDM portal.
- Additional support options were provided, such as contacting the helpdesk for further assistance.

## General Learnings
- Ensure users are aware of remote access procedures, including the use of specific servers for external connections.
- Educate users on password reset options through linked accounts and IDM portals.
- Provide clear instructions for troubleshooting common issues like VPN configuration and password resets.
```
---

### 2022060942002566_mobaxterm%20permission%20denied.md
# Ticket 2022060942002566

 # HPC Support Ticket: MobaXterm Permission Denied

## Keywords
- HPC Account
- VPN
- MobaXterm
- Permission Denied
- Account Request
- Group ID
- Contact Person

## Problem Description
- User is unable to connect to HPC via MobaXterm after successfully connecting to VPN.
- Error message indicates permission denied issue.

## Root Cause
- User does not have an HPC account and is attempting to log in with IdM credentials.

## Solution
- User needs to apply for an HPC account as it is a separate service.
- The hosting chair (supervisor) must request the HPC account for the user.
- The user should follow the instructions in the [Getting Started](https://hpc.fau.de/systems-services/systems-documentation-instructions/getting-started/) guide.

## Additional Information
- The group ID for the relevant research group is "iww6" and the subgroup ID is "iww6101".
- The contact person for the group is the one initially suspected by the supervisor.

## Follow-up Actions
- Supervisor will ensure the user submits an application for an HPC account.
- HPC Admins will process the account request upon receipt.

## Notes
- HPC Admins and 2nd Level Support team are available to assist with further queries.
- Specific roles include Head of Datacenter, Training and Support Group Leader, NHR Rechenzeit Support, and Software and Tools developers.
---

### 2020051542002523_Zugang_HPC.md
# Ticket 2020051542002523

 # HPC Support Ticket: Access Issues

## Keywords
- HPC Access
- SSH
- Password Issues
- VPN
- IdM-Portal
- Permission Denied

## Problem Description
- User unable to access HPC via SSH despite having an account and setting a password.
- Error message: "Permission denied" when attempting to connect via SSH.

## Root Cause
- Log files indicate "Failed password for [username]".

## Solution
- **Password Reset**: User should reset the password via the IdM-Portal.
- **Propagation Time**: Note that it may take several hours for the password change to propagate across all HPC systems.

## Additional Notes
- **Communication**: Users should use their university email address for communication with HPC support.
- **VPN**: Ensure VPN is correctly configured and active during the SSH attempt.

## Steps for Support Employees
1. **Check Logs**: Verify the log files for password failure messages.
2. **Advise Password Reset**: Instruct the user to reset their password via the IdM-Portal.
3. **Inform Propagation Time**: Notify the user about the potential delay in password propagation.
4. **Email Communication**: Ensure the user is using their university email for support requests.

## Conclusion
Proper password management and communication practices are crucial for resolving HPC access issues. Ensure users are aware of the steps and potential delays involved in password resets.
---

