# Topic 5: ssh_portal_key_keys_sso

Number of tickets: 403

## Tickets in this topic:

### 2023032042000013_Issues%20with%20HPC%20Login.md
# Ticket 2023032042000013

 # HPC Support Ticket: Issues with HPC Login

## Summary
- **User Issue**: Unable to log into HPC account despite entering the correct password.
- **Error Message**: Wrong password response.
- **Additional Context**: User is connected to FAU VPN.

## Root Cause
- **Initial Assumption**: Incorrect password.
- **Actual Issue**: Incorrect SSH command syntax in VSCode configuration.

## Troubleshooting Steps
1. **Admin Check**: Successful login recorded in auth.log.
2. **User Feedback**: Provided full error message from VSCode.
3. **Admin Diagnosis**: Identified space in SSH command causing connection failure.

## Solution
- **Correct SSH Command**: Remove space in the command.
  ```sh
  ssh -J iwfa005h@cshpc.rrze.fau.de iwfa005h@tinyx.nhr.fau.de
  ```
- **Alternative Command**: Direct connection when using FAU VPN.
  ```sh
  ssh iwfa005h@tinyx.nhr.fau.de
  ```

## Additional Information
- **Password Reset**: User can change password using IDM.
- **Account Extension**: User needs to fill out the application form for extension.

## Keywords
- HPC Login Issue
- Wrong Password
- VSCode SSH Configuration
- FAU VPN
- SSH Command Syntax

## Lessons Learned
- **Common Issue**: Incorrect SSH command syntax can cause connection failures.
- **Troubleshooting**: Check for spaces or typos in SSH commands.
- **User Guidance**: Provide clear instructions for configuring SSH in VSCode.

## Closure
- **Resolution**: User successfully connected after correcting the SSH command.
- **Ticket Status**: Closed.
---

### 2024030142003198_HPC%20account%20inactive.md
# Ticket 2024030142003198

 # HPC Account Inactive Issue

## Keywords
- HPC account
- SSH key setup
- Account state: inactive
- Principal Investigator
- Account deactivation

## Problem Description
- User's HPC account showed as archived and inactive after attempting SSH key setup.
- User uploaded SSH key on the 28th, but the account state changed to inactive.

## Root Cause
- The Principal Investigator deactivated the account due to the user not being actively involved in their seminar or lab.

## Solution
- The user was advised to contact the Principal Investigator regarding the deactivation.
- HPC Admins confirmed that they did not have further information and the account management lies with the Principal Investigator.

## General Learnings
- Account deactivation can occur due to administrative decisions by the Principal Investigator.
- SSH key setup issues may not be the cause of account deactivation.
- Users should contact their Principal Investigator for account-related queries.

## Ticket Closure
- The ticket was closed as the HPC Admins could not take further action. The account management is handled by the Principal Investigator.
---

### 2024031142000672_Migration%20of%20mfml%20HPC%20accounts%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20mandato.md
# Ticket 2024031142000672

 # HPC Support Ticket: Migration of mfml HPC Accounts to New HPC Portal / SSH Keys Become Mandatory

## Keywords
- HPC account migration
- SSH keys
- HPC portal
- Single Sign-On (SSO)
- IdM portal
- SSH key types (RSA, ECDSA, ED25519)
- Usage statistics
- ClusterCockpit
- Jupyterhub

## Summary
The HPC support team is migrating existing HPC accounts from the IdM portal to a new online HPC portal. This migration involves several changes, including the mandatory use of SSH keys for accessing HPC systems.

## Key Points
- **New HPC Portal**: Accessible at [https://portal.hpc.fau.de](https://portal.hpc.fau.de).
- **SSO Login**: Use IdM credentials for Single Sign-On.
- **SSH Keys**: Mandatory for HPC system access from the end of March.
  - Accepted types: RSA (4096 bits), ECDSA (512 bits), ED25519.
  - Upload SSH PublicKey to the HPC portal.
  - Propagation delay: Up to two hours.
- **Documentation**: Available at [SSH Secure Shell Access](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/) and [FAQs](https://hpc.fau.de/faqs/#ID-230).
- **Windows Users**: Recommended to use OpenSSH built into Windows (Power)Shell or MobaXterm instead of Putty.
- **IdM Portal Expiration**: Ignore automatic messages about HPC service expiration in the IdM portal.
- **Account Validity**: Managed through the HPC portal starting from the end of February.
- **Usage Statistics**: Visible to users, PIs, and project managers.
- **ClusterCockpit and Jupyterhub**: Access via Single Sign-On links from within the HPC portal.

## Root Cause of the Problem
- Migration process requires users to adapt to new authentication methods and portal functionalities.

## Solution
- Users need to generate and upload SSH keys to the new HPC portal.
- Access HPC systems and services through the new HPC portal using SSO.
- Contact PIs or project managers for account validity updates.

## Additional Notes
- The HPC portal and IdM portal are decoupled.
- New HPC accounts should be requested through PIs or project managers.
- Updated Jupyterhub instance with new software and hardware.

This documentation aims to assist support employees in understanding and resolving similar issues related to HPC account migration and SSH key requirements.
---

### 2024060442000297_New%20invitation%20for%20%22A07SFB1277%20-%20Quantum%20transport%20and%20time-dependent%20dynamics%2.md
# Ticket 2024060442000297

 # HPC Support Ticket Analysis

## Subject
New invitation for "A07SFB1277 - Quantum transport and time-dependent dynamics of Dirac fermions" waiting at portal.hpc.fau.de

## Keywords
- SSO Login
- eduPersonPrincipalName
- SSH Public Key
- Technical Account
- HPC Portal
- IdM Credentials

## Problem Description
The user received an invitation to join a project on the HPC portal but encountered issues with SSO login due to the `eduPersonPrincipalName` attribute not being correctly transferred. The user was using a technical account shared by multiple guests/bachelor students.

## Root Cause
The technical account did not have a proper `eduPersonPrincipalName` attribute, which is required for SSO login.

## Solution
The user decided to request a new account for the guest, which should resolve the SSO login issue.

## General Learnings
- Ensure that all accounts, including technical accounts, have the necessary SSO attributes for successful login.
- If a technical account is shared among multiple users, consider creating individual accounts to avoid attribute-related issues.
- Always provide clear instructions for accepting invitations and uploading SSH keys, as outlined in the initial email.

## Support Team Involvement
- **HPC Admins**: Provided initial support and identified the SSO attribute issue.
- **2nd Level Support Team**: Not explicitly involved in this ticket but available for escalation if needed.
- **Head of Datacenter** and **Training and Support Group Leader**: Not involved in this specific ticket.
- **NHR Rechenzeit Support**: Not involved in this specific ticket.
- **Software and Tools Developer**: Not involved in this specific ticket.

## Documentation Reference
For further information, refer to the [HPC Portal Documentation](https://doc.nhr.fau.de/hpc-portal/).

## Contact
In case of problems, users should send an email with a clear description of the issue to 'hpc-support@fau.de'.
---

### 2023011742000747_Error%20in%20uploading%20public%20key.md
# Ticket 2023011742000747

 # HPC Support Ticket: Error in Uploading Public Key

## Keywords
- SSH Key
- Public Key
- Private Key
- Putty
- OpenSSH
- MobaXterm
- IPv6
- Proxy Jump Host

## Problem
- User unable to upload public key.
- User sent compromised private key (PPK file).

## Root Cause
- Incorrect key format (SSH2 instead of OpenSSH).
- User error in exporting key from Putty.

## Solution
1. **Generate New SSH Key**:
   - Use `ssh-keygen` on command line or PowerShell.
   - Documentation: [SSH Secure Shell Access to HPC Systems](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/#ssh_public_key)

2. **Convert Key Format**:
   - Use `ssh-keygen -i -f ssh2.pub` to convert SSH2 key to OpenSSH format.

3. **Upload Public Key**:
   - Copy the generated public key into the HPC portal.

4. **Use MobaXterm**:
   - Specify the path to the newly generated private key in MobaXterm.

5. **Connect via IPv6 or Proxy Jump Host**:
   - Direct connection if IPv6 is available.
   - Configure proxy jump host over `cshpc.rrze.fau.de` if IPv6 is not available.

## Additional Notes
- Connecting with Putty to NHR systems is non-trivial.
- MobaXterm is recommended for easier configuration.

## Follow-up
- User acknowledged the response and will follow the instructions.
- HPC Admin confirmed the solution (LGTM).
---

### 2024051542001704_Account%20and%20change%20of%20affiliation.md
# Ticket 2024051542001704

 ```markdown
# HPC Support Ticket: Account and Change of Affiliation

## Keywords
- HPC Account
- Account Reactivation
- Affiliation Change
- SSH Key
- HPC Portal
- Export Control Regulations
- Tier3 Project

## Summary
A user requests access to an inactive HPC account to download and archive data. Additionally, the user inquires about the impact of changing affiliations within the university clinic.

## Root Cause
- The user's HPC account was not imported into the HPC portal due to a lack of response from the previous supervisor.
- The user is changing affiliations within the university clinic, necessitating a new HPC account.

## Solution
1. **Account Reactivation:**
   - The HPC Admin imported the user's account into the HPC portal.
   - The user needs to upload an SSH key to the HPC portal for login purposes.
   - The previous supervisor must log into the HPC portal and accept the export control regulations for extended account usage.

2. **Affiliation Change:**
   - The user needs to apply for a new HPC account due to the change in affiliation.
   - The new department's supervisor must log into the HPC portal and accept the export control regulations.
   - The new department may need to establish a Tier3 project if it does not already exist.

## Additional Information
- The user was provided with links to the HPC portal and documentation on SSH key usage.
- The HPC Admin requested the new department's supervisor's name and FAU organization number (and RRZE customer number if available).

## Conclusion
The user's account was reactivated, and instructions were provided for accessing the account and applying for a new account due to the change in affiliation. The new department's supervisor must also take specific actions to facilitate the user's new account.
```
---

### 2023071742003813_Account%20expiring.md
# Ticket 2023071742003813

 # HPC Support Ticket: Account Expiring

## Keywords
- Account extension
- HPC portal
- SSH keys
- IdM portal
- Account validity

## Problem
- User's HPC account (gwgi026h) is nearing expiration.
- User's contract at FAU has been extended and they need to extend their HPC account as well.

## Root Cause
- User was unaware of the changes in the account management system from IdM portal to HPC portal.
- User's account was actually valid until early 2026, but they were using passwords instead of SSH keys.

## Solution
- Inform the user about the migration from IdM portal to HPC portal.
- Advise the user to switch from passwords to SSH keys for account access.
- Direct the user to the HPC portal (https://portal.hpc.fau.de/) for account management.
- Notify the user that their supervisor (Prof. Braun) can adjust the account validity if needed.

## General Learnings
- With the move to the new HPC portal, account extensions may not require paperwork.
- SSH keys have become mandatory for HPC account access.
- Users should be directed to the HPC portal for account management tasks.
- Supervisors can manage the validity of their team members' accounts.
---

### 2024020642002637_SSH%20keys.md
# Ticket 2024020642002637

 ```markdown
# HPC Support Ticket: SSH Keys

## Keywords
- SSH keys
- RSA keys
- Key length
- Public key upload
- HPC portal

## Problem
- User attempted to upload a public SSH key to the HPC portal but received an error indicating the key was too short.
- The minimum accepted key length for RSA keys is 3072 bits.
- User generated a new key using `ssh-keygen -t rsa -b 4096` but encountered issues during the upload process.

## Root Cause
- The user inadvertently uploaded an old, shorter key instead of the newly generated 4096-bit key.
- The new key was saved in a different location, and the user did not overwrite the existing default key.

## Solution
- Ensure the newly generated key is saved in the correct location.
- Verify the key length and timestamp to confirm it is the newly generated key.
- Upload the correct public key to the HPC portal.

## Steps to Verify
1. Generate a new SSH key with the desired length:
   ```sh
   ssh-keygen -t rsa -b 4096
   ```
2. Specify a full path and filename for the new key to avoid overwriting issues:
   ```sh
   Enter file in which to save the key (/home/$USER/.ssh/id_rsa): /home/$USER/debug/demo
   ```
3. Check the timestamp of the key files to ensure the correct key is being used:
   ```sh
   ls -la /home/$USER/.ssh/*
   ```
4. Upload the correct public key to the HPC portal.

## Conclusion
- The issue was resolved by ensuring the correct key was generated and uploaded.
- Users should be mindful of key locations and timestamps to avoid uploading outdated keys.
```
---

### 2024030142001529_Migration%20of%20mpkr04%20HPC%20account%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20mandat.md
# Ticket 2024030142001529

 # HPC Support Ticket Summary

## Subject
Migration of HPC account to new HPC portal / SSH keys become mandatory

## Keywords
- HPC account migration
- SSH keys
- HPC portal
- Single Sign-On (SSO)
- IdM portal
- Account validity
- Usage statistics
- ClusterCockpit
- Jupyterhub

## General Learnings
- The HPC services are migrating to a new online HPC portal.
- Access to HPC systems will require SSH keys from March 11th.
- Accepted SSH key types are RSA (4096 bit), ECDSA (512 bit), and ED25519.
- The HPC portal is decoupled from the IdM portal.
- Account validity updates should be requested from the PI or project manager.
- Usage statistics are visible to PIs and project managers.
- Access to ClusterCockpit and Jupyterhub should be done via SSO links from the HPC portal.

## Root Cause of the Problem
- The user needs to migrate their HPC account to the new portal and set up SSH keys for access.

## Solution
- Log in to the new HPC portal using SSO with IdM credentials.
- Generate and upload SSH keys with the specified requirements.
- Contact the PI or project manager for account validity updates.
- Use SSO links for ClusterCockpit and Jupyterhub access.

## Additional Notes
- Windows users are recommended to use OpenSSH or MobaXterm.
- Ignore automatic messages about HPC service expiration from the IdM portal.
- The new HPC portal will be the sole source for account validity starting from the end of February.
---

### 2025022042003911_Ssh%20bash.md
# Ticket 2025022042003911

 # HPC Support Ticket: SSH Bash Login Issue

## Keywords
- SSH
- Bash
- Login Issue
- Fileserver
- Hang

## Problem Description
- User unable to log in via SSH to the bash console.

## Root Cause
- Issues with a fileserver causing logins to hang.

## Solution
- The fileserver issue was resolved, and logins should be back to normal since 07:30 AM.

## General Learnings
- Fileserver issues can cause SSH login hangs.
- Regular monitoring and quick resolution of fileserver issues are crucial for maintaining SSH access.

## Actions Taken
- HPC Admin informed the user about the fileserver issue and its resolution.

## Next Steps
- Monitor fileserver health to prevent similar issues in the future.
- Communicate any ongoing issues promptly to users.
---

### 2022120842001066_Account%20f%C3%83%C2%BCr%20BTDFT2Fritz.md
# Ticket 2022120842001066

 # HPC Support Ticket: Account Issue for Project BTDFT2Fritz

## Keywords
- Account creation
- SSO (Single Sign-On)
- Email mismatch
- Portal invitation
- Account activation

## Problem Description
The user had invited a colleague to the project BTDFT2Fritz, who successfully received an account and could log in. However, the user themselves did not have an account and could not see the invitation in the "Benutzer"-Tab of the HPC portal.

## Root Cause
The user's SSO attribute had a dedicated email address (ingo.schelter@uni-bayreuth.de), but the invitation was sent to a different email address (bt**@uni-bayreuth.de), causing a mismatch and preventing the user from seeing the invitation.

## Solution
The HPC Admin corrected the target email address of the invitation to match the SSO email address. After this correction, the user was able to see and accept the invitation, leading to successful account creation.

## General Learnings
- Ensure that the email address used for SSO matches the email address used for invitations.
- If a user cannot see an invitation in the portal, check for email mismatches.
- Correcting the email address in the invitation can resolve the issue and allow the user to proceed with account creation.

## Steps Taken
1. HPC Admin verified the open invitation and email address mismatch.
2. HPC Admin corrected the email address in the invitation.
3. User accepted the invitation and the account was generated.

## Conclusion
The issue was resolved by ensuring the email addresses matched, allowing the user to accept the invitation and create an account. This solution can be applied to similar cases where users cannot see invitations in the portal.
---

### 2024071742002732_VS%20Code%20Debugger%20inside%20Interactive%20Shell%20using%20GPU.md
# Ticket 2024071742002732

 # HPC Support Ticket: VS Code Debugger inside Interactive Shell using GPU

## Keywords
- VS Code Debugger
- Interactive Shell
- GPU
- SSH Configuration
- Remote Debugging
- Visual Studio Code Remote - SSH Extension
- Launch Configurations
- Tasks

## Problem Description
The user is trying to run the VS Code Debugger inside an interactive shell with GPU access while debugging remotely using VS Code. The user has already tried configuring Launch Configurations and tasks but encountered issues with the SSH connection to the compute node.

## Root Cause
The user encountered an SSH connection error due to an incorrect hostname in the SSH configuration file. The hostname `tg068.nhr.fau.de` was incorrect, and the correct hostname should be `tg068.rrze.uni-erlangen.de`.

## Solution
1. **Submit an Interactive Job**:
   ```bash
   salloc.tinygpu --gres=gpu:1 --time=00:30:00
   ```

2. **Add the Hostname to Local SSH Config**:
   ```plaintext
   # compute node
   Host tg068.rrze.uni-erlangen.de
   User iwi5216h
   ProxyJump csnhr.nhr.fau.de
   IdentityFile ~/.ssh/id_ed25519_fau
   IdentitiesOnly yes
   PasswordAuthentication no
   PreferredAuthentications publickey
   ForwardX11 no
   ForwardX11Trusted no
   ```

3. **Connect to the Compute Node through VS Code**:
   - If only the single compute node is added, its name should be shown.
   - If a matching rule like `tg???` is used, the hostname might need to be entered again.

4. **Configure Launch Configuration**:
   - The Launch configuration should be related to `${workspaceRoot}`, making it independent of whether it is executed locally or remotely.

5. **Install Extensions**:
   - Ensure that extensions are installed both locally and remotely. After the connection is established, there should be a button "Install on <SSH target>" at the extensions.

## General Learnings
- Ensure correct hostnames are used in SSH configurations.
- Use the `ProxyJump` directive for SSH connections through a jump host.
- Configure VS Code Launch Configurations to be independent of the execution environment.
- Install necessary extensions both locally and remotely for seamless debugging.

## References
- [VS Code Remote - SSH Extension](https://code.visualstudio.com/docs/remote/ssh)
- [Launch Configurations](https://code.visualstudio.com/docs/editor/debugging#_launch-configurations)
- [Tasks](https://code.visualstudio.com/docs/editor/tasks)
- [Template for Connecting to Cluster Nodes](https://doc.nhr.fau.de/access/ssh-command-line/#template-for-connecting-to-cluster-nodes)
---

### 2024022342000946_Migration%20of%20iwb8%20HPC%20accounts%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20mandato.md
# Ticket 2024022342000946

 # HPC Support Ticket Conversation Summary

## Keywords
- Migration of HPC accounts
- New HPC portal
- SSH keys
- Single Sign-On (SSO)
- IdM portal
- Account validity
- Usage statistics
- ClusterCockpit
- Jupyterhub

## General Learnings
- The migration process of existing HPC accounts from the IdM portal to a new online HPC portal has started.
- Access to HPC systems will be by SSH keys only starting from the end of February.
- Users need to generate SSH key pairs with passphrases and upload the public keys to the HPC portal.
- The IdM portal and the new HPC portal are completely decoupled.
- Users should contact their PI or project manager to update the validity of their HPC accounts.
- Usage statistics of different HPC systems will be visible to PIs and project managers.
- Single Sign-On links from within the HPC portal should be used for ClusterCockpit and Jupyterhub services.

## Root Cause of the Problem
- The user's email address was undeliverable, leading to a bounced email.

## Solution
- No solution provided in the conversation. The HPC Admin resends the initial message without addressing the email delivery issue.

## Additional Notes
- The HPC portal can be accessed at [https://portal.hpc.fau.de](https://portal.hpc.fau.de).
- Accepted SSH key types are RSA with a length of at least 4096 bits, ECDSA with a length of 512, and ED25519.
- Documentation and FAQs for SSH keys are available at [HPC Documentation](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/) and [FAQs](https://doc.nhr.fau.de/faq/#ssh).
- Windows users are recommended to use OpenSSH built into the Windows (Power)Shell or MobaXterm instead of Putty.
---

### 2024091742000374_AW%3A%20Your%20account%20%22b136dc17%22%20for%20project%20%22FRASCAL-MD%20-%20Particle-based%20compu.md
# Ticket 2024091742000374

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject
AW: Your account "b136dc17" for project "FRASCAL-MD - Particle-based computing at LTM for FRASCAL (b136dc)" will soon expire at portal.hpc.fau.de

## Keywords
- Account expiration
- Account extension
- SSH Public Key
- HPC-Portal
- Project runtime
- PI (Principal Investigator)
- Project managers

## Root Cause of the Problem
- The user's HPC account was about to expire.
- The account extension was overlooked during the last renewal process.

## Solution
- The account was extended to 30.09.2025.
- The user was informed that an SSH Public Key needs to be added to the HPC-Portal for account usage.
- Additional information on connecting via SSH was provided through a documentation link.

## What Can Be Learned
- Regularly check account expiration dates to avoid service disruptions.
- Ensure that SSH Public Keys are properly configured for HPC account access.
- Provide clear instructions and documentation links for users to follow.
- Communicate with the PI or project managers for account extensions if the project runtime allows.

## Actions Taken
- The account was extended.
- The user was informed about the necessity of adding an SSH Public Key.
- Documentation on SSH connection was shared.

## Closure
- The ticket was closed after the account extension and necessary information were provided.
```
---

### 2022121542002202_Probleme%20beim%20SSO%20im%20HPC%20Portal.md
# Ticket 2022121542002202

 # HPC Support Ticket Analysis: SSO Issues in HPC Portal

## Keywords
- SSO Login
- eduGAIN
- 403 Error
- Unsupported Request
- Team Accounts
- Export Controls
- IPv6-only
- eduGAIN Federation
- DFN-AAI
- InCommon Federation
- SWAMID Federation
- UK Access Management Federation

## Summary
Users from various universities reported issues with SSO login via eduGAIN on the HPC portal. The errors included 403 errors and unsupported request messages. The HPC Admins discussed potential causes and solutions, including the need for universities to register the application and the possibility of withdrawing from the competition due to numerous issues.

## Root Cause
- **University of California, Santa Cruz**: 403 Error
- **Sun Yat-sen University**: Unsupported Request
- **Tsinghua University**: Unsupported Request
- **National Tsing Hua University**: Not found in eduGAIN list

## Solutions and Actions
- **Successful Logins**: Some universities successfully logged in, indicating that the issue might be with specific universities not registering the application.
- **Incomplete Data**: Some users had incomplete data transferred, such as missing first name, last name, and affiliations.
- **Certificate Expiration**: One issue was related to an expired certificate.
- **eduGAIN Federation**: The HPC Admins decided to stick with eduGAIN as it provides access to over 8,000 institutions.
- **Team Accounts**: The HPC Admins expressed concerns about sharing team accounts and emphasized the importance of following IT regulations.
- **IPv6-only**: There was a mention of issues related to IPv6-only, which might require significant support.

## Documentation and Next Steps
- **SSO Status Documentation**: A document was created to track the SSO status and brainstorm further steps.
- **Final Decision**: The final decision on whether to use the system will be made in the second half of January.

## Conclusion
The ticket highlights the challenges of SSO integration with eduGAIN and the importance of universities registering the application. It also emphasizes the need for strict adherence to IT regulations and the potential for significant support requirements related to IPv6-only issues.
---

### 2024022342002221_Migration%20of%20mpt1%20HPC%20accounts%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20mandato.md
# Ticket 2024022342002221

 # HPC Support Ticket Summary

## Subject
Migration of mpt1 HPC accounts to new HPC portal / SSH keys become mandatory

## Keywords
- HPC account migration
- SSH keys
- HPC portal
- Single Sign-On (SSO)
- IdM portal
- SSH key types (RSA, ECDSA, ED25519)
- Usage statistics
- ClusterCockpit
- Jupyterhub

## Summary
- **Migration Process**: Existing HPC accounts are being migrated from the IdM portal to a new online HPC portal.
- **Access**: The new HPC portal can be accessed via SSO using IdM credentials.
- **SSH Keys**: Access to HPC systems will require SSH keys only. Accepted types are RSA (4096 bits), ECDSA (512 bits), and ED25519.
- **Documentation**: Users unfamiliar with SSH keys should refer to the provided documentation and FAQs.
- **Expiration Notice**: Users will receive an email about the expiration of their HPC service in the IdM portal, which can be ignored.
- **Account Validity**: The new HPC portal will be the sole source for account validity.
- **Usage Statistics**: Users and their PIs/project managers can view usage statistics in the HPC portal.
- **ClusterCockpit and Jupyterhub**: Access to these services will be via SSO links within the HPC portal.

## Root Cause of the Problem
- Users need to transition to the new HPC portal and set up SSH keys for continued access to HPC systems.

## Solution
- Users should log in to the new HPC portal using SSO.
- Generate and upload SSH keys as per the specified types and lengths.
- Use the SSO links within the HPC portal for accessing ClusterCockpit and Jupyterhub.
- Contact the PI or project manager for account validity updates.

## Additional Notes
- The HPC portal and IdM portal are decoupled.
- Recommended tools for Windows users include OpenSSH built into the Windows (Power)Shell or MobaXterm.

## References
- [HPC Portal](https://portal.hpc.fau.de)
- [SSH Documentation](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/)
- [FAQs](https://hpc.fau.de/faqs/#ID-230)
---

### 2024031742000251_HPC%20Zugang%20abgelaufen%20-%20mpet007h.md
# Ticket 2024031742000251

 # HPC Support Ticket: Account Expiration Issue

## Keywords
- HPC Account Expiration
- SSH Key Authentication
- Account Migration
- HPC Portal
- IDM Portal

## Summary
A user reported being unable to log in to their HPC account due to an expired account. The user had requested an extension but did not receive any notification about the account expiration.

## Root Cause
- The user's account had expired due to a migration process from the IDM portal to the new HPC portal.
- The user had not followed the necessary steps outlined in an email sent on March 1, which detailed the migration process and the requirement for SSH keys.

## Solution
- The user was informed about the migration process and the need to log in to the new HPC portal and accept the Terms of Service (TOS).
- After following these steps, the user's account was reactivated, and they were able to log in successfully.

## Lessons Learned
- Users should carefully read and follow instructions provided in emails regarding account migrations and updates.
- HPC Admins should ensure that users are aware of any upcoming changes and the steps they need to take to maintain their account access.
- Regularly check the status of your HPC account and ensure that all necessary actions are taken to keep it active.

## References
- [Migration of FAU HPC Accounts from IDM Portal to HPC Portal](https://hpc.fau.de/2024/03/04/migration-of-fau-hpc-accounts-from-idm-portal-to-hpc-portal/)

## Ticket Status
- The ticket was closed after the user successfully logged in to the HPC portal and accepted the TOS, reactivating their account.
---

### 2021033142000452_PuTTY%20Sicherheitswarnung.md
# Ticket 2021033142000452

 # PuTTY Security Warning Issue

## Keywords
- PuTTY
- Sicherheitswarnung
- Key mismatch
- HPC-System
- meggie1
- meggie2
- ED25519

## Problem Description
A user encountered a security warning while trying to connect to the HPC system via PuTTY. The connection worked fine the previous day.

## Root Cause
The user was connected to `meggie1` the previous day, and PuTTY stored the key for `meggie1`. The current connection attempt was to `meggie2`, which has a different key, causing a key mismatch warning.

## Solution
- **Immediate Action**: The user can ignore the warning and proceed with the connection, as the key exchange is necessary to establish an encrypted connection.
- **Long-term Fix**: The HPC Admins should ensure that both `meggie1` and `meggie2`, which are accessible under the same DNS entry, use the same key to prevent such warnings in the future.

## General Learning
- Security warnings in PuTTY should not be ignored without understanding the cause, as they can indicate a security issue.
- Key mismatches can occur when connecting to different servers with different keys under the same DNS entry.
- Ensuring consistent keys across servers under the same DNS entry can prevent such warnings.

## Roles Involved
- **HPC Admins**: Provided the explanation and solution for the key mismatch issue.
- **User**: Reported the issue and followed the instructions provided by the HPC Admins.

## Next Steps
- HPC Admins should synchronize the keys for `meggie1` and `meggie2` to prevent future key mismatch warnings.
- Users should be informed about the potential for key mismatch warnings and how to handle them safely.
---

### 2024022042001611_Migration%20of%20iwsp%20HPC%20accounts%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20mandato.md
# Ticket 2024022042001611

 # HPC Support Ticket Summary

## Subject
Migration of iwsp HPC accounts to new HPC portal / SSH keys become mandatory

## Keywords
- HPC account migration
- SSH keys
- HPC portal
- Single Sign-On (SSO)
- IdM portal
- ClusterCockpit
- Jupyterhub

## Key Points
- **Migration to New HPC Portal**: Existing HPC accounts are being migrated to a new online HPC portal.
- **SSH Keys Mandatory**: Access to HPC systems will require SSH keys starting end of February. Accepted types are RSA (4096 bits), ECDSA (512 bits), and ED25519.
- **SSO Login**: Users should login to the new portal using SSO with IdM credentials.
- **Usage Statistics**: Users and their PIs/project managers can view usage statistics in the HPC portal.
- **ClusterCockpit and Jupyterhub**: Access these services via SSO links from within the HPC portal.

## Root Cause of the Problem
- Users need to migrate their accounts and set up SSH keys for continued access to HPC systems.

## Solution
- **Account Migration**: Users should login to the new HPC portal using SSO with their IdM credentials.
- **SSH Key Setup**: Generate and upload SSH key pairs with a passphrase to the HPC portal.
- **Service Access**: Use SSO links within the HPC portal to access ClusterCockpit and Jupyterhub.

## Additional Information
- **Documentation and FAQs**: Users unfamiliar with SSH keys should refer to the provided documentation and FAQs.
- **Windows Users**: Recommended to use OpenSSH built into Windows (Power)Shell or MobaXterm instead of Putty.
- **Account Validity**: The HPC portal will be the sole source for account validity starting from 1.3.2024. Users should contact their PI or project manager to update account validity.

## Relevant Links
- [HPC Portal](https://portal.hpc.fau.de)
- [Documentation](https://doc.nhr.fau.de/access/overview/)
- [FAQs](https://doc.nhr.fau.de/faq/)

---

This summary provides a quick reference for support employees to assist users with similar issues related to HPC account migration and SSH key setup.
---

### 2023053042003622_Migration%20of%20bccb%2A%20HPC%20accounts%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20mand.md
# Ticket 2023053042003622

 # HPC Support Ticket: Migration to New HPC Portal and SSH Key Mandate

## Keywords
- HPC portal migration
- SSH keys
- Single Sign-On (SSO)
- IdM portal
- Account validity
- Usage statistics
- ClusterCockpit
- Jupyterhub

## Summary
The HPC services at FAU are migrating to a new online HPC portal, accessible via SSO using IdM credentials. SSH keys will become mandatory for accessing HPC systems by mid-June. Users need to generate and upload SSH key pairs to the new portal.

## Key Points to Learn
- **Portal Migration**: The new HPC portal is accessible at [https://portal.hpc.fau.de](https://portal.hpc.fau.de) and requires SSO login with IdM credentials.
- **SSH Keys**: Access to HPC systems will require SSH keys (RSA 4096-bit, ECDSA 512-bit, ED25519). Users must generate and upload their public keys to the portal.
- **Account Validity**: The new HPC portal will be the sole source for account validity. Users should ignore expiration messages from the IdM portal.
- **Usage Statistics**: The portal displays usage statistics, which are also visible to PIs and project managers.
- **ClusterCockpit and Jupyterhub**: Users must use SSO links from the HPC portal to access these services.

## Root Cause of the Problem
- Users need to adapt to the new portal and SSH key requirements for continued access to HPC services.

## Solution
- Users should log in to the new HPC portal using SSO, generate and upload SSH keys, and use the portal for all account-related activities and service access.

## Additional Resources
- [SSH Documentation](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/)
- [FAQs](https://hpc.fau.de/faqs/#ID-230)

## Notes for Support Employees
- Ensure users are aware of the migration timeline and the necessity of SSH keys.
- Provide guidance on generating and uploading SSH keys if users are unfamiliar with the process.
- Direct users to the new HPC portal for all account management and service access.
---

### 2022081242002592_SSH-Probleme%20b118bb13.md
# Ticket 2022081242002592

 # SSH Login Issue on NHR@FAU Rechner

## Keywords
- SSH Key
- Passphrase
- Password Prompt
- Login Issue
- FAQ
- cshpc.rrze.fau.de

## Problem Description
- User created an RSA SSH key with a passphrase and uploaded it to the FAU account page.
- User is unable to log in to the `cshpc.rrze.fau.de` frontend despite the key being accepted.
- The system prompts for a password instead of the SSH key passphrase.

## Root Cause
- The SSH key setup might have been incorrect or not properly propagated.
- Possible issue with the SSH key configuration or the system not recognizing the uploaded key.

## Solution
- HPC Admin provided a new FAQ entry: [FAQ Link](https://hpc.fau.de/faq/i-managed-to-log-in-to-cshpc-with-an-ssh-key-but-get-asked-for-a-password-when-continuing-to-a-cluster-frontend/)
- User suggested deleting the existing SSH key and uploading a new one.

## General Learnings
- Ensure SSH keys are correctly generated and uploaded.
- Check FAQs and documentation for common issues related to SSH login.
- If issues persist, consider regenerating and re-uploading the SSH key.

## Next Steps
- Verify the SSH key setup and ensure it is correctly configured on the server.
- Follow the FAQ instructions for troubleshooting SSH login issues.
- If the problem persists, contact HPC support for further assistance.
---

### 2023051242000409_AW%3A%20New%20invitation%20for%20%22Tier3%20Grundversorgung%20UTN%20%28S.%20Graf%29%22%20waiting%20a.md
# Ticket 2023051242000409

 # HPC Support Ticket: SSH Key Setup for New Account

## Keywords
- SSH Key
- Passwordless Login
- HPC Portal
- SSO (Single Sign-On)
- IdM Credentials
- Public Key Upload

## Problem Description
- User unable to log in via cmd or WinSCP due to password prompt.
- User followed instructions but did not set up SSH key.

## Root Cause
- User did not upload an SSH public key to the HPC portal.

## Solution
1. **Accept Invitation**:
   - Log in to the HPC portal via SSO using IdM credentials.
   - Navigate to 'User' -> 'Your Invitations' and accept the invitation.

2. **Upload SSH Public Key**:
   - Generate an SSH key pair if not already done.
   - Upload the public key (`ssh-rsa`) to the corresponding account in the HPC portal ('User' -> 'Your Accounts').

3. **Wait for Key Distribution**:
   - The SSH key will be distributed to all systems within a few hours (maximum 24 hours).
   - After distribution, passwordless login will be possible.

## Additional Resources
- [HPC FAQs: SSH Key Setup](https://hpc.fau.de/faqs/#ID-230)

## Notes
- Ensure the user follows the steps for SSH key setup to enable passwordless login.
- If issues persist, the user should contact HPC support with a clear description of the problem.

---

This documentation aims to assist HPC support employees in resolving similar issues related to SSH key setup for new accounts.
---

### 2024070942004442_publickey%20issue.md
# Ticket 2024070942004442

 # HPC Support Ticket: Publickey Issue

## Subject
Publickey issue

## User Report
- **Project**: b211dd
- **Username**: b211dd19
- **Issue**: After uploading SSH public key, user receives "Permission denied (publickey)" when attempting to SSH into `cshpc.rrze.fau.de` or `csnhr.nhr.fau.de`.
- **Extra Info**: User can start an Alex cluster via JupyterHub but cannot ping `github.com`.

## HPC Admin Actions
1. **Log Analysis**:
   - Checked logs for user `b211dd19` on `csnhr.nhr.fau.de` and `cshpc.rrze.fau.de`.
   - Found multiple instances of "Connection closed by authenticating user" messages.

2. **Request for Debugging**:
   - Requested user to run SSH with debugging messages enabled (`ssh -vv <your SSH options and arguments>`) and send the output.
   - Provided a link to the troubleshooting section: [SSH Command Line Troubleshooting](https://doc.nhr.fau.de/access/ssh-command-line/#troubleshooting).

## Keywords
- SSH
- Publickey
- Permission denied
- Debugging
- Log analysis

## What Can Be Learned
- **Common SSH Issues**: Understanding common SSH problems and how to troubleshoot them.
- **Log Analysis**: Importance of checking server logs for authentication issues.
- **Debugging SSH**: Using `ssh -vv` to gather detailed information for troubleshooting.

## Root Cause
- The root cause of the problem is not explicitly identified in the conversation, but it is likely related to the SSH public key configuration or permissions.

## Solution
- The solution involves running SSH with debugging messages enabled to gather more information and referring to the troubleshooting guide for common SSH problems.

## Next Steps
- Await user's response with the debugging output to further diagnose the issue.

## Closure
- The ticket was closed without a clear resolution, indicating that further action or information is needed from the user.

---

This report provides a concise summary of the issue, actions taken, and steps for resolution, which can be used as a reference for future similar issues.
---

### 2023112142005251_Frage%20nach%20dem%20Konto%20bei%20HPC%20-%20iwep001h.md
# Ticket 2023112142005251

 # HPC Support Ticket Conversation Summary

## Keywords
- Account Setup
- HPC Portal
- IDM
- Ansys License
- HPC Cafe
- HPC Introduction Seminar
- Zoom Meeting
- Project Invitation
- MobaXTerm
- SSH
- Module System

## General Learnings
- There are two systems for account creation: the old paper-based IDM system and the new digital HPC portal.
- The HPC Cafe is not an introductory event; there is a separate seminar for beginners.
- Users may need assistance with setting up SSH and understanding the module system.
- MobaXTerm can be used to simplify SSH setup on Windows.

## Root Cause of the Problem
- The user was confused about the account setup process and the difference between the IDM and HPC portal systems.
- The user needed guidance on how to use the HPC systems and tools, including SSH and the module system.

## Solution
- The HPC Admin explained the account setup process and the difference between the IDM and HPC portal systems.
- The HPC Admin provided information about the HPC introduction seminar and scheduled a Zoom meeting to provide further assistance.
- The HPC Admin helped the user set up MobaXTerm and explained how to use SSH and the module system.

## Additional Notes
- The user will likely have further questions about using Ansys on the HPC systems.
- The ticket was closed after the initial setup and explanation, but the user may need additional assistance in the future.
- The user comes from a Windows background and has limited HPC experience, so they may need more detailed guidance and support.
---

### 2023101842000997_Beantragung%20HPC%20Zugang%20-%20mfsi001h%20-%20Grieshaber-Bouyer%20-%20R_RStudio.md
# Ticket 2023101842000997

 ```markdown
# HPC Support Ticket Conversation Summary

## Key Points Learned

1. **SSH Configuration**:
   - The user had issues with SSH configuration for proxy jump.
   - The correct configuration should have `Host cshpc` and `HostName cshpc.rrze.fau.de`.
   - The user's configuration was incorrect, leading to authentication issues.

2. **SSH Key Management**:
   - The user uploaded an SSH key to the HPC Portal.
   - The user was prompted for a password when trying to connect to `woody` from `cshpc`.
   - The user did not need to place a private key in their user directory on `cshpc`.

3. **Account Migration**:
   - The user's account was migrated to the HPC Portal as the leading system.
   - The user was not informed about this migration, leading to confusion and authentication issues.

4. **Documentation and Support**:
   - The HPC support team provided documentation and examples for correct SSH configuration.
   - The support team offered to assist the user via Zoom to resolve the issue.

## Solutions Provided

1. **Correct SSH Configuration**:
   - The user was advised to correct their SSH configuration to properly set up proxy jump.
   - The correct configuration was provided in the documentation.

2. **SSH Key Usage**:
   - The user was informed that they do not need to place a private key in their user directory on `cshpc`.
   - The user was advised to use the SSH key uploaded to the HPC Portal for authentication.

3. **Account Migration Communication**:
   - The user was informed about the migration of their account to the HPC Portal.
   - The user was advised to wait for the SSH key to be available on the clusters, which can take up to 2 hours.

4. **Zoom Support**:
   - The support team offered to assist the user via Zoom to resolve the issue.
   - The Zoom link was provided for a meeting on the same day.

## Conclusion

The user's issues were primarily related to incorrect SSH configuration and lack of communication about account migration. The HPC support team provided documentation, examples, and offered direct assistance via Zoom to resolve the problems. The user was advised to correct their SSH configuration and use the SSH key uploaded to the HPC Portal for authentication. The support team also informed the user about the account migration and the need to wait for the SSH key to be available on the clusters.
```
---

### 2024021542003011_Migration%20of%20iwmm%20HPC%20accounts%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20mandato.md
# Ticket 2024021542003011

 # HPC Support Ticket Conversation Summary

## Keywords
- Migration
- HPC Portal
- SSH Keys
- Single Sign-On (SSO)
- IdM Portal
- Account Validity
- Usage Statistics
- ClusterCockpit
- Jupyterhub

## General Learnings
- **Migration Process**: The migration of HPC accounts from the IdM portal to a new online HPC portal has started.
- **SSH Keys**: Access to HPC systems will require SSH keys from 1.3.2024. Accepted types are RSA (4096 bits), ECDSA (512 bits), and ED25519.
- **Account Validity**: The HPC portal will be the sole source for account validity from 1.3.2024. Users should contact their PI or project manager to update account validity.
- **Usage Statistics**: PIs and project managers can view usage statistics in the HPC portal.
- **ClusterCockpit and Jupyterhub**: Users should use Single Sign-On links from the HPC portal to access these services.

## Root Cause of the Problem
- **Email Delivery Failure**: The initial email from the HPC Admin could not be delivered to one recipient due to an incorrect email address.

## Solution
- **Corrected Email**: The HPC Admin resent the email with the correct address and updated information about the migration deadline.

## Additional Notes
- **Documentation**: Users unfamiliar with SSH keys should refer to the provided documentation and FAQs.
- **Windows Users**: Recommended to use OpenSSH in Windows (Power)Shell or MobaXterm instead of Putty.

For further assistance, users should contact the HPC support team at [support-hpc@fau.de](mailto:support-hpc@fau.de).
---

### 2024022942002915_Migration%20of%20iwit14%20HPC%20accounts%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20manda.md
# Ticket 2024022942002915

 # HPC Support Ticket Conversation Summary

## Subject
Migration of iwit14 HPC accounts to new HPC portal / SSH keys become mandatory

## Keywords
- HPC account migration
- SSH keys
- HPC portal
- IdM portal
- Single Sign-On (SSO)
- SSH key types (RSA, ECDSA, ED25519)
- Account validity
- Usage statistics
- ClusterCockpit
- Jupyterhub

## What Can Be Learned
- **Migration Process**: The migration of HPC accounts from the IdM portal to a new online HPC portal is underway.
- **SSH Keys**: Starting March 11th, access to HPC systems will require SSH keys. Accepted types are RSA (4096 bits), ECDSA (512 bits), and ED25519.
- **HPC Portal**: The new HPC portal can be accessed at [https://portal.hpc.fau.de](https://portal.hpc.fau.de) using SSO with IdM credentials.
- **Account Validity**: The HPC portal will be the sole source for account validity starting from the end of February.
- **Usage Statistics**: Users, PIs, and project managers can view usage statistics in the HPC portal.
- **ClusterCockpit and Jupyterhub**: Access these services via SSO links within the HPC portal.

## Root Cause of the Problem
- Users need to migrate their accounts to the new HPC portal and set up SSH keys for continued access.

## Solution
- **Login**: Use SSO with IdM credentials to access the new HPC portal.
- **SSH Keys**: Generate and upload SSH key pairs with passphrases. Refer to documentation for guidance.
- **Account Validity**: Contact the PI or project manager to update account validity.
- **Usage Monitoring**: Use the HPC portal for usage statistics and access ClusterCockpit and Jupyterhub via SSO links.

## Additional Notes
- Windows users are recommended to use OpenSSH built into the Windows (Power)Shell or MobaXterm instead of Putty.
- Ignore automatic messages from the IdM portal regarding account expiration.

---

This summary provides a quick reference for support employees to understand the migration process and the necessary steps for users to maintain access to HPC systems.
---

### 2025022542002001_Connection%20SSH%20%20to%20Nodes.md
# Ticket 2025022542002001

 ```markdown
# HPC Support Ticket: Connection SSH to Nodes

## Keywords
- SSH Connection
- Graphic Nodes
- Bash Console
- Dateisysteme
- Shell

## Problem Description
- User reported difficulties connecting to graphic nodes via SSH.
- Connection to the Bash console could not be established.

## Root Cause
- The dateisysteme were heavily loaded the previous night and morning.
- This caused the connection to work but prevented the shell from being provided.

## Solution
- The user was advised to try again later.
- The issue resolved itself over time.

## Lessons Learned
- Specific error descriptions are crucial for accurate troubleshooting.
- High load on dateisysteme can affect SSH connections and shell availability.
- Users should retry connections after some time if the issue is related to system load.
```
---

### 2015121642000458_LIMA%20_apps_.md
# Ticket 2015121642000458

 # HPC Support Ticket: /apps/ Folder Unavailable on LIMA

## Keywords
- LIMA
- /apps/ folder
- Login node
- Module loading
- Unavailability

## Problem Description
The user reported that the `/apps/` folder was unavailable on the LIMA system, preventing the loading of any modules.

## Root Cause
The issue was identified as a problem with the login node "lima1".

## Solution
The HPC Admin team addressed the problem with the login node "lima1", and the issue was resolved.

## Lessons Learned
- **Monitoring Login Nodes**: Regular monitoring of login nodes is crucial to ensure the availability of essential directories like `/apps/`.
- **Communication**: Prompt communication with users about the status of issues helps in managing expectations and reducing downtime.

## Actions Taken
- The HPC Admin team fixed the problem with the login node "lima1".

## Future Prevention
- Implement automated checks for critical directories on login nodes.
- Ensure quick resolution of login node issues to minimize disruptions.

## References
- [HPC Services](http://www.hpc.rrze.fau.de/)
- [Institute of Geography](http://www.geographie.nat.uni-erlangen.de/personen/johannes-fuerst/)
---

### 2024030142000673_Migration%20of%20mfsd%20HPC%20accounts%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20mandato.md
# Ticket 2024030142000673

 # HPC Support Ticket: Migration of HPC Accounts to New Portal / SSH Keys Mandatory

## Keywords
- HPC account migration
- SSH keys
- HPC portal
- IdM portal
- Single Sign-On (SSO)
- SSH key types (RSA, ECDSA, ED25519)
- ClusterCockpit
- Jupyterhub

## Summary
- **Migration Process**: Existing HPC accounts are being migrated to a new online HPC portal.
- **Access Change**: From March 15th, access to HPC systems will require SSH keys only.
- **SSH Key Requirements**: Accepted SSH key types are RSA (4096 bits), ECDSA (512 bits), and ED25519.
- **Portal Access**: The new HPC portal can be accessed via SSO using IdM credentials.
- **Usage Statistics**: Users, PIs, and project managers can view usage statistics in the HPC portal.
- **ClusterCockpit and Jupyterhub**: Access these services via SSO links within the HPC portal.

## User Issue
- **Root Cause**: User was informed about the migration and new requirements but did not immediately respond due to being in training.

## Solution
- **Action Required**: User needs to generate and upload SSH keys to the new HPC portal.
- **Documentation**: Refer to the provided documentation and FAQs for guidance on SSH key generation and usage.

## Additional Notes
- **Expiration Notices**: Users may receive automatic expiration notices from the IdM portal, which can be ignored.
- **Account Validity**: The HPC portal will be the sole source for account validity starting from the end of February.
- **Account Management**: Users should contact their PI or project manager for account validity updates or new account requests.

## Recommendations for Support Employees
- **SSH Key Assistance**: Be prepared to assist users with generating and uploading SSH keys.
- **Portal Navigation**: Guide users through the new HPC portal and its features.
- **Documentation Reference**: Direct users to the relevant documentation and FAQs for detailed instructions.

---

This report provides a concise overview of the migration process, key requirements, and steps users need to take to ensure smooth access to HPC systems.
---

### 2024072542004582_Project%20invitation%20wrong%20address.md
# Ticket 2024072542004582

 # HPC Support Ticket: Project Invitation Wrong Address

## Keywords
- Project Invitation
- Email Address
- Alias Email
- Correct Address
- Unreachable User
- HPC Admins

## Summary
A user requested an HPC Admin to add a colleague to a project, but the invitation was sent to an incorrect alias email address due to an error on their side. The user is now unreachable, and the correct email address needs to be added to the project.

## Root Cause
- Incorrect email address used for project invitation.

## Solution
- HPC Admins need to add the correct email address to the project.

## General Learnings
- Ensure correct email addresses are used when inviting users to projects.
- Verify email addresses before sending invitations to avoid issues when users become unreachable.
- HPC Admins can manually add users to projects if provided with the correct email address.

## Actions Taken
- User requested HPC Admins to add the correct email address to the project.
- Correct email address provided: `alexandros.ziogas@iis.ee.ethz.ch`.

## Next Steps
- HPC Admins to add the correct email address to the project `j101df`.

## Related Parties
- HPC Admins
- 2nd Level Support Team
- Head of the Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support
- Software and Tools Developer
---

### 2023053042002829_Migration%20of%20bco1%23%23%23h%20HPC%20accounts%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become.md
# Ticket 2023053042002829

 # HPC Support Ticket Conversation Summary

## Subject
Migration of HPC accounts to new HPC portal / SSH keys become mandatory

## Keywords
- HPC account migration
- SSH keys
- HPC portal
- Single Sign-On (SSO)
- IdM portal
- SSH key types (RSA, ECDSA, ED25519)
- Account validity
- Usage statistics
- ClusterCockpit
- Jupyterhub

## General Learnings
- **Migration Process**: HPC accounts are being migrated from the IdM portal to a new online HPC portal.
- **SSH Keys**: Access to HPC systems will require SSH keys by mid-June. Accepted types are RSA (4096 bits), ECDSA (512 bits), and ED25519.
- **Portal Access**: The new HPC portal can be accessed via SSO using IdM credentials.
- **Account Validity**: The HPC portal will be the sole source for account validity. Users should contact their PI or project manager for updates.
- **Usage Statistics**: PIs and project managers can view usage statistics in the HPC portal.
- **ClusterCockpit and Jupyterhub**: Users should use SSO links from the HPC portal to access these services.

## Root Cause of the Problem
- Users need to migrate their accounts and set up SSH keys for continued access to HPC systems.

## Solution
- Users should log in to the new HPC portal using SSO and upload their SSH public keys.
- For SSH key generation and usage, users can refer to the provided documentation and FAQs.
- Windows users are recommended to use OpenSSH or MobaXterm.

## Additional Notes
- The IdM portal and the new HPC portal are decoupled.
- Users should ignore automatic messages about HPC service expiration from the IdM portal.
- New HPC accounts should be requested through the PI or project manager, not directly from RRZE.

---

This summary provides a concise overview of the migration process, key requirements, and steps users need to take to ensure continued access to HPC services.
---

### 2024030442001738_Unable%20to%20log%20in%20via%20SSH.%20Getting%20%22Permission%20denied%20%28publickey%29%22%20-%20%2.md
# Ticket 2024030442001738

 ```markdown
# SSH Key Authentication Issue

## Problem Description
The user encountered a "Permission denied (publickey)" error when attempting to log in via SSH. The issue persisted despite the correct configuration and key setup.

## Troubleshooting Steps
1. **Initial Configuration**:
   - The user configured the SSH key with a custom name (`fau-alex`) and specified it in the `.ssh/config` file.
   - The `.ssh/config` file was moved temporarily to isolate the issue.

2. **SSH Command**:
   - The user ran the command `ssh -v -i /export/home/lemercier/.ssh/fau-alex f101ac13@cshpc.rrze.fau.de` to test the connection.

3. **Error Message**:
   - The error message indicated that the SSH client was unable to find the private key associated with the public key `fau-alex.pub`.
   - The SSH client attempted to use default key names (`id_rsa`, `id_dsa`, etc.) but did not find the custom-named key.

## Root Cause
The root cause of the problem was the incorrect encryption protocol used when generating the SSH keys. The user initially used RSA, which was not compatible with the server's requirements.

## Solution
The user regenerated the SSH keys using the correct encryption protocol as specified in the [HPC documentation](https://doc.nhr.fau.de/access/ssh-command-line/#generating-an-ssh-key-pair). After generating the new keys, the user was able to log in successfully.

## Key Takeaways
- Ensure that the correct encryption protocol is used when generating SSH keys.
- Verify that the `.ssh/config` file is correctly configured to point to the custom-named private key.
- If issues persist, temporarily move the `.ssh/config` file to isolate the problem and test the connection with the SSH command.

## Conclusion
The issue was resolved by regenerating the SSH keys with the correct encryption protocol. This documentation can be used as a reference for similar issues in the future.
```
---

### 2024022942002184_Migration%20of%20mfch%20HPC%20accounts%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20mandato.md
# Ticket 2024022942002184

 # HPC Support Ticket Summary

## Subject
Migration of mfch HPC accounts to new HPC portal / SSH keys become mandatory

## Keywords
- HPC account migration
- SSH keys
- HPC portal
- Single Sign-On (SSO)
- IdM portal
- SSH key types
- Account validity
- Usage statistics
- ClusterCockpit
- Jupyterhub

## Key Points
- **Migration to New HPC Portal**: Existing HPC accounts are being migrated to a new online HPC portal.
- **SSH Keys Mandatory**: Starting March 11th, access to HPC systems will require SSH keys.
- **SSH Key Types**: Accepted types are RSA (4096 bits), ECDSA (512 bits), and ED25519.
- **SSH Key Upload**: Users need to generate and upload their SSH public keys to the HPC portal.
- **Account Validity**: The HPC portal will be the sole source for account validity starting from the end of February.
- **Usage Statistics**: Users, PIs, and project managers can view usage statistics in the HPC portal.
- **Single Sign-On**: Access to ClusterCockpit and Jupyterhub will be through SSO links within the HPC portal.

## Root Cause of the Problem
- Users need to transition to the new HPC portal and set up SSH keys for continued access to HPC systems.

## Solution
- **Login to HPC Portal**: Use SSO with IdM credentials to access the new HPC portal.
- **Generate SSH Keys**: Create SSH key pairs with a passphrase and upload the public key to the HPC portal.
- **Ignore IdM Expiration Email**: Disregard automatic messages about HPC service expiration in the IdM portal.
- **Contact PI/Project Manager**: For account validity updates, contact the PI or project manager instead of filling out paper forms.
- **Use SSO Links**: Access ClusterCockpit and Jupyterhub through SSO links in the HPC portal.

## Additional Resources
- [SSH Secure Shell Access Documentation](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/)
- [FAQs](https://hpc.fau.de/faqs/#ID-230)

## Notes
- Windows users are recommended to use OpenSSH built into the Windows (Power)Shell or MobaXterm instead of Putty.
- The HPC portal and IdM portal are completely decoupled.
---

### 2024040242001963_Missing%20Required%20Attributes%20in%20SSO-Response.md
# Ticket 2024040242001963

 # Missing Required Attributes in SSO-Response

## Keywords
- SSO-Response
- Missing attributes
- Email activation
- HPC-Portal
- IDM Kennung
- FAUmail
- dovecot

## Problem Description
- User encounters error message 'Missing required attributes in SSO-Response' upon first login to the HPC-Portal.
- Required attributes from the SAML metadata are not activated.

## Root Cause
- The user recently activated their email address for delivery to FAUmail/dovecot.
- The HPC-Portal did not receive the user's email via SSO at the time of the error.

## Solution
- The issue is expected to resolve itself shortly after the email activation.
- No immediate action is required from the user or the HPC Admin.

## General Learning
- Email activation and proper configuration are crucial for SSO to function correctly.
- Recent changes in email settings may cause temporary issues with SSO attribute transmission.
- Allow some time for the system to update and propagate changes.

## Roles Involved
- HPC Admins
- 2nd Level Support Team
- Users
---

### 2024022742003294_Migration%20of%20mfex%20HPC%20accounts%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20mandato.md
# Ticket 2024022742003294

 # HPC Support Ticket: Migration of HPC Accounts to New Portal / SSH Keys Mandatory

## Keywords
- HPC account migration
- SSH keys
- HPC portal
- IdM portal
- Single Sign-On (SSO)
- SSH key types (RSA, ECDSA, ED25519)
- Account validity
- Usage statistics
- ClusterCockpit
- Jupyterhub

## Summary
The HPC services at FAU are migrating existing HPC accounts to a new online HPC portal. Users will need to generate and upload SSH keys for access. The new portal will be the sole source for account validity and usage statistics.

## Key Points
- **Migration Process**: Existing HPC accounts are being migrated to a new HPC portal accessible via SSO using IdM credentials.
- **SSH Keys**: Access to HPC systems will require SSH keys (RSA, ECDSA, ED25519) with a passphrase.
- **Account Validity**: The new HPC portal will manage account validity, decoupled from the IdM portal. Users should contact their PI or project manager for extensions.
- **Usage Statistics**: Both users and PIs can view usage statistics in the HPC portal.
- **ClusterCockpit and Jupyterhub**: Access these services via SSO links within the HPC portal.

## Actions for Users
- **Login**: Access the new HPC portal using SSO with IdM credentials.
- **SSH Keys**: Generate and upload SSH keys to the HPC portal.
- **Account Management**: Contact PI or project manager for account validity updates.
- **Service Access**: Use SSO links for ClusterCockpit and Jupyterhub.

## Documentation and Support
- **SSH Key Documentation**: [HPC Documentation](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/)
- **FAQs**: [HPC FAQs](https://doc.nhr.fau.de/faq/#ssh)
- **Recommended Tools**: OpenSSH built into Windows (Power)Shell or MobaXterm for Windows users.

## Additional Notes
- Ignore automatic messages from the IdM portal regarding account expiration.
- The HPC portal will be the sole source for account validity starting from the end of February.

---

This report provides a concise overview of the migration process and the necessary actions for users to ensure a smooth transition to the new HPC portal.
---

### 2025031142002203_Access%20Issue%20with%20HPC%20Cluster.md
# Ticket 2025031142002203

 ```markdown
# HPC Support Ticket: Access Issue with HPC Cluster

## Keywords
- Permission Denied
- SSH Key
- HPC Portal
- Configuration
- Access Issue
- Key Distribution

## Problem Description
- User encountered a "Permission Denied" error while trying to access the HPC cluster.
- User followed the provided instructions, including generating an SSH key, adding the public key to the HPC Portal, and modifying the configuration.
- User ran `sh csnhr.nhr.fau.de` and selected "Yes" but received "Permission Denied".
- User ran `ssh -vvv csnhr.nhr.fau.de` and encountered an error (output attached).

## Root Cause
- The SSH key might not have been distributed to all HPC systems yet.
- There was an issue on the HPC side that needed to be resolved.

## Solution
- Wait up to two hours for the SSH key to be distributed to all HPC systems.
- HPC Admins resolved an issue on their side and advised the user to try again.

## Additional Information
- User modified the config file for both `csnhr` and `fritz` as explained in a session.
- User was able to access the HPC cluster but was kicked out after entering the password.
- HPC Admins advised the user to try again after resolving an issue on their side.

## Documentation Link
- [HPC Portal User Tab Documentation](https://doc.nhr.fau.de/hpc-portal/#the-user-tab)
```
---

### 2023030242001716_Vorbereitungen%20zur%20Umstellung%20iwal%20von%20Papier-HPC-Antr%C3%83%C2%A4gen%20auf%20HPC-Portal.md
# Ticket 2023030242001716

 # HPC-Support Ticket Conversation Summary

## Subject
Vorbereitungen zur Umstellung iwal von Papier-HPC-Anträgen auf HPC-Portal

## Keywords
- HPC-Portal
- SSO
- DFN-AAI
- SSH-Keys
- Account Migration
- FAU-IdM
- FHG-IdM
- eduPersonPrincipalName
- Kundennummern
- Ablaufdatum
- Exportkontrolle
- Passwörter
- Jupyterhub

## Summary
The conversation revolves around the migration of HPC accounts from paper-based applications to the electronic HPC portal. Key points include:

- **SSO Testing**: FHG members need to test if they can log in via DFN-AAI.
- **Account Migration**: Importing existing accounts into the HPC portal, ensuring proper matching of FHG-IdM usernames.
- **SSH Keys**: Transitioning from password-based SSH access to SSH keys.
- **Kundennummern**: Assigning customer numbers to differentiate account types.
- **Ablaufdatum**: Managing account expiration dates.
- **Exportkontrolle**: Full responsibility for account expiration and export control transferred to the user.

## Detailed Steps and Solutions

### SSO Testing
- FHG members should test logging in via DFN-AAI to ensure SSO attributes are correctly transferred.

### Account Migration
- **Import List**: A detailed import list was provided, including FHG-IdM usernames and email addresses.
- **Matching**: Imported accounts were matched based on eduPersonPrincipalName.
- **Non-Imported Accounts**: Some accounts (iwal000h, iwal006h, iwal013h, iwal069h) were not imported due to missing UIDs.

### SSH Keys
- Users need to log in via the HPC portal and register their SSH keys.
- Passwords for SSH access will be deprecated, and only SSH keys will be accepted.

### Kundennummern
- Standard customer numbers were assigned:
  - iwal100: Tier3 Grundversorgung AudioLabs
  - iwal101: Studentische Abschlußarbeiten Tier3 Grundversorgung AudioLabs
  - iwal102: Projektpartner Tier3 Grundversorgung AudioLabs
  - iwal103: Lehre Tier3 Grundversorgung AudioLabs

### Ablaufdatum
- Account expiration dates were updated in the import list.
- Future account extensions will be managed via the HPC portal.

### Exportkontrolle
- Full responsibility for account expiration and export control was transferred to the user.
- Nationality checks were removed to avoid responsibility issues.

## Conclusion
The migration process involved several steps, including SSO testing, account matching, transitioning to SSH keys, and assigning customer numbers. The HPC portal will be the primary system for managing accounts, with passwords being deprecated in favor of SSH keys. Future account extensions and expiration dates will be managed via the portal.

## Next Steps
- Ensure all users log in via the HPC portal and register their SSH keys.
- Manage account extensions and expiration dates through the HPC portal.
- Monitor and resolve any issues with non-imported accounts.

## Important Notes
- Some accounts were not imported due to missing UIDs.
- The HPC portal will be the datenführendes System, with passwords for SSH access being deprecated by the end of March.

This summary provides a comprehensive overview of the migration process and the steps taken to ensure a smooth transition to the HPC portal.
---

### 2024022742001394_Additional%20remote%20acces%20new%20project.md
# Ticket 2024022742001394

 # HPC Support Ticket: Additional Remote Access for New Project

## Keywords
- SSH Configuration
- Multiple Projects
- Remote Access
- Ubuntu 16.04
- ProxyCommand
- IdentityFile

## Problem
- User needs to connect to a new project (b210bb104) from their workstation, which is already linked to another project (b178bb11).
- User's SSH config file is set up for a single project.

## Root Cause
- The SSH config file specifies a single user (b178bb11) for all hosts, preventing connection to the new project.

## Solution
- Remove the `User` entry from the SSH config file.
- Connect to the different projects using `ssh b178bb11@cshpc` or `ssh b210bb104@cshpc`.

## Example Configuration
```plaintext
ServerAliveInterval 60

# FAU - Erlangen
Host cshpc.rrze.fau.de
    HostName cshpc.rrze.fau.de
    IdentityFile ~/.ssh/key_FAU_orMD.txt.pub
    IdentitiesOnly yes
    PasswordAuthentication no
    PreferredAuthentications publickey

Host fritz
    HostName fritz.nhr.fau.de
    ProxyCommand ssh -W %h:%p cshpc.rrze.fau.de
    IdentityFile ~/.ssh/key_FAU_orMD.txt.pub
    IdentitiesOnly yes
    PasswordAuthentication no
    PreferredAuthentications publickey

Host alex
    HostName alex.nhr.fau.de
    ProxyCommand ssh -W %h:%p cshpc.rrze.fau.de
    IdentityFile ~/.ssh/key_FAU_orMD.txt.pub
    IdentitiesOnly yes
    PasswordAuthentication no
    PreferredAuthentications publickey
```

## General Learning
- Users can connect to multiple projects by specifying the project ID in the SSH command.
- The `User` entry in the SSH config file should be removed to allow flexibility in connecting to different projects.
- Proper configuration of `ProxyCommand` and `IdentityFile` is crucial for seamless remote access.

## Ticket Status
- Closed by HPC Admin.
---

### 2023011942002563_Fwd%3A%20New%20invitation%20for%20%22GastroDigitalShirt%20-%20Development%20and%20test%20of%20deep%2.md
# Ticket 2023011942002563

 # HPC Support Ticket Analysis

## Keywords
- Project Invitation
- SSO (Single Sign-On)
- Email Mismatch
- HPC Portal
- SSH Public Key

## Problem
- **Root Cause:** Email mismatch between the user's SSO credentials and the email address used for the invitation.
- **Symptom:** User unable to see the project invitation in their account.

## Solution
- **Action Taken:** HPC Admin adjusted the invitation email in the system to match the user's SSO email.
- **Result:** User was able to see and accept the invitation.

## General Learnings
- Ensure that the email address used for project invitations matches the user's SSO email.
- If a user cannot see a project invitation, check for email mismatches.
- HPC Admins can adjust invitation emails in the system to resolve such issues.

## Next Steps for Similar Issues
- Verify the user's SSO email address.
- Check the email address used for the project invitation.
- If there is a mismatch, adjust the invitation email in the system.
---

### 2024080542004359_RE%3A%20%5BNHR%40FAU%5D%20Dialog%20server%20%22cshpc%22%20to%20be%20replaced%2C%20XRDP%20taking%20ov.md
# Ticket 2024080542004359

 ```markdown
# HPC Support Ticket: Dialog Server Replacement and SSH Configuration Issue

## Keywords
- SSH Configuration
- ProxyJump
- ProxyCommand
- Ubuntu 16.04
- OpenSSH 7.3
- XRDP
- NoMachine NX
- Dialog Server Replacement

## Summary
A user encountered issues with SSH configuration due to an outdated version of OpenSSH on Ubuntu 16.04. The user was attempting to set up a new remote connection via SSH with the Alex system.

## Root Cause
- The user's SSH configuration file contained the `ProxyJump` option, which is not supported by the version of OpenSSH shipped with Ubuntu 16.04.
- The old dialog server `cshpc.rrze.fau.de` was being decommissioned and replaced by `csnhr.nhr.fau.de`.

## Solution
- The HPC Admin suggested using `ProxyCommand` instead of `ProxyJump` to resolve the SSH configuration issue.
- The user was advised to update their systems to a more recent version of Ubuntu to avoid vulnerabilities and ensure compatibility with newer features.

## General Learnings
- Ensure that the SSH client version is compatible with the configuration options being used.
- Regularly update systems to avoid security vulnerabilities and compatibility issues.
- Follow the provided documentation for updating SSH configuration files when dialog servers are replaced.
- Use `ProxyCommand` as an alternative to `ProxyJump` for older SSH versions.

## References
- [SSH Configuration Template](https://doc.nhr.fau.de/access/ssh-command-line/#template-for-connecting-to-hpc-systems)
- [XRDP Documentation](https://doc.nhr.fau.de/access/xrdp/)
```
---

### 2024030542002708_User%20account%20gesperrt.md
# Ticket 2024030542002708

 ```markdown
# HPC Support Ticket: User Account Lockout

## Keywords
- Account Lockout
- SSH Keys
- HPC Portal
- IDM Portal
- Account Expiry
- Account Reactivation

## Problem Description
A user was unable to log in after their account expired and was reactivated.

## Root Cause
- The account expiry date was changed during cleanup activities, causing the account to be locked.
- There was no entry in the `precedenceconfig` for the user's account, leading to the expiry date from IDM taking precedence.
- The migration to the HPC Portal was not completed properly.

## Solution
- The HPC Admin identified the missing entry in the `precedenceconfig` and corrected it.
- The account was reactivated, and the user was advised to upload new SSH keys to the HPC Portal after any account changes.

## Lessons Learned
- Ensure proper completion of migrations to the HPC Portal.
- Regularly check and update the `precedenceconfig` to avoid conflicts with IDM expiry dates.
- Advise users to upload new SSH keys after any account changes to maintain access.
```
---

### 2025031042002787_HPC%20portal%20shows%20account%20state%20as%20inactive%20-%20Roobesh%20Balaji.md
# Ticket 2025031042002787

 # HPC Support Ticket: Account Inactive Issue

## Keywords
- HPC portal
- Account state
- Inactive account
- SSH connection
- Project manager
- Account extension

## Problem Description
- User's HPC portal shows account as inactive and archived.
- User unable to connect via SSH (`ssh tinyx.nhr.fau.de`).

## Root Cause
- Account expired and automatically set to inactive.
- Project manager extended the account date but did not change the status to active.

## Solution
- User should request the project manager to change the account status from inactive to active.

## General Learnings
- Accounts may be automatically set to inactive upon expiration.
- Extending the account date does not automatically activate the account.
- Project managers are responsible for managing account status.
- Inactive accounts may cause issues with SSH connections.

## Ticket Conversation Summary
- **User**: Reported account shown as inactive and unable to connect via SSH.
- **HPC Admin**: Advised user to ask the project manager to extend access.
- **HPC Admin**: Noted that the project manager updated the date but not the status.
- **User**: Confirmed that the account was extended but still inactive.
- **HPC Admin**: Instructed user to ask the project manager to activate the account.

## Related Parties
- HPC Admins
- 2nd Level Support Team
- Project Manager

## Relevant Links
- [FAU HPC Support](mailto:support-hpc@fau.de)
- [FAU HPC Website](https://hpc.fau.de/)
---

### 2024062142001594_no%20access%20to%20clusters.md
# Ticket 2024062142001594

 # HPC Support Ticket: No Access to Clusters

## Subject
No access to clusters

## User Issue
- Unable to connect to HPC clusters despite having permission.
- Console output indicates missing SSH key and permission denied errors.

## Console Output
```
C:\Users\Besitzer>ssh alex.nhr.fau.de
no such identity: C:\\Users\\Besitzer\\.ssh\\id-ed25519_nhr_fau: No such file or directory
ep56inew@csnhr.nhr.fau.de: Permission denied (publickey,password).
kex_exchange_identification: Connection closed by remote host
Connection closed by UNKNOWN port 65535
```

## Detailed Debug Output
```
C:\Users\Besitzer>ssh -vv alex.nhr.fau.de
...
debug1: identity file C:\\Users\\Besitzer\\.ssh\\id-ed25519_nhr_fau type -1
debug1: identity file C:\\Users\\Besitzer\\.ssh\\id-ed25519_nhr_fau-cert type -1
...
debug1: Authenticating to csnhr.nhr.fau.de:22 as 'ep56inew'
...
debug1: Trying private key: C:\\Users\\Besitzer\\.ssh\\id-ed25519_nhr_fau
no such identity: C:\\Users\\Besitzer\\.ssh\\id-ed25519_nhr_fau: No such file or directory
debug2: we did not send a packet, disable method
debug1: No more authentication methods to try.
ep56inew@csnhr.nhr.fau.de: Permission denied (publickey,password).
kex_exchange_identification: Connection closed by remote host
Connection closed by UNKNOWN port 65535
```

## Root Cause
- Missing SSH key file: `C:\\Users\\Besitzer\\.ssh\\id-ed25519_nhr_fau`
- Incorrect HPC username: `ep56inew` instead of `iwai110h`

## Solution
1. Ensure the SSH key file `C:\\Users\\Besitzer\\.ssh\\id-ed25519_nhr_fau` exists.
2. Use the correct HPC username `iwai110h` instead of `ep56inew`.

## Keywords
- SSH key missing
- Permission denied
- Incorrect HPC username
- Connection closed by remote host

## General Learning
- Always check for the existence of the required SSH key files.
- Ensure the correct HPC username is used for authentication.
- Verify SSH configuration and debug output for detailed error information.
---

### 2024022842000901_Migration%20of%20iwtm%20HPC%20accounts%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20mandato.md
# Ticket 2024022842000901

 # HPC Support Ticket Conversation Summary

## Subject
Migration of iwtm HPC accounts to new HPC portal / SSH keys become mandatory

## Keywords
- HPC account migration
- SSH keys
- HPC portal
- Single Sign-On (SSO)
- IdM portal
- SSH key types (RSA, ECDSA, ED25519)
- Usage statistics
- ClusterCockpit
- Jupyterhub

## General Learnings
- **Migration Process**: HPC accounts are being migrated from the IdM portal to a new HPC portal.
- **SSH Keys**: Access to HPC systems will require SSH keys from March 11th. Accepted types are RSA (4096 bits), ECDSA (512 bits), and ED25519.
- **Portal Access**: The new HPC portal can be accessed via SSO using IdM credentials.
- **Account Validity**: The HPC portal will be the sole source for account validity starting from the end of February.
- **Usage Statistics**: Users, PIs, and project managers can view usage statistics in the HPC portal.
- **ClusterCockpit and Jupyterhub**: Access these services via SSO links within the HPC portal.

## Root Cause of the Problem
- Users need to transition to the new HPC portal and set up SSH keys for continued access.

## Solution
- **Login**: Access the new HPC portal using SSO with IdM credentials.
- **SSH Keys**: Generate and upload SSH keys to the HPC portal. Follow the provided documentation and FAQs for guidance.
- **Account Management**: Contact the PI or project manager to update account validity or request new accounts.
- **Service Access**: Use SSO links within the HPC portal for ClusterCockpit and Jupyterhub.

## Additional Notes
- Windows users are recommended to use OpenSSH built into the Windows (Power)Shell or MobaXterm instead of Putty.
- Ignore automatic messages from the IdM portal regarding service expiration.

---

This summary provides a concise overview of the migration process, key requirements, and steps users need to take to ensure continued access to HPC services.
---

### 2024091042001457_Not%20able%20to%20connect%20to%20tinyx.md
# Ticket 2024091042001457

 # HPC Support Ticket: Unable to Connect to tinyx

## Keywords
- SSH Connection
- Network Unreachable
- ProxyJump Host
- Network Problem

## Issue
- User unable to connect to `tinyx` or HPC using `ssh tinyx`.
- Error message: `ssh: connect to host csnhr.nhr.fau.de port 22: Network is unreachable`.

## Root Cause
- The user's computer is unable to reach the proxyjump-host `csnhr.nhr.fau.de`.
- Multiple users from Fraunhofer IIS reported the same issue, suggesting a network problem at IIS.

## Solution
- The issue is likely a network problem at Fraunhofer IIS, which is outside the scope of HPC support.
- Users experiencing this issue should contact their local IT support for assistance.

## General Learnings
- Network issues can cause SSH connection failures.
- ProxyJump hosts are critical for SSH connections to HPC systems.
- Localized network problems can affect multiple users within the same organization.
- HPC support may not be able to resolve external network issues.
---

### 2023100242003157_Error%20-%20Internal%20Server%20Error%3A%20Mail%20could%20not%20be%20sent%21%20%28Status%3A%20500%29.md
# Ticket 2023100242003157

 ```markdown
# HPC Support Ticket: Error - Internal Server Error: Mail could not be sent! (Status: 500) for ID '10965'

## Keywords
- Internal Server Error
- Mail could not be sent
- Status: 500
- Project Invitation
- HPC Portal

## Problem Description
User encountered an error when trying to invite another member to their project. The error message was: "Error - Internal Server Error: Mail could not be sent! (Status: 500) for ID '10965'".

## Root Cause
The mail server failed to send the invitation email, resulting in a 500 Internal Server Error.

## Solution
- **Immediate Workaround**: The invitation was correctly created in the HPC Portal. The invited user can see the invitation by logging into the HPC Portal.
- **Long-term Fix**: The error was identified and fixed by the HPC Portal developer. The fix was deployed to prevent future occurrences.

## Lessons Learned
- **Communication**: Even if the email fails to send, the invitation is still created in the HPC Portal and can be accessed by the invited user.
- **Troubleshooting**: Check the HPC Portal for the invitation status if email delivery fails.
- **Priority**: Issues related to email delivery may be considered low priority if the invitation is visible in the portal.

## Actions Taken
- HPC Admin confirmed the invitation was created in the HPC Portal.
- HPC Admin noted that the issue was due to a mail server failure.
- The issue was marked as low priority due to the visibility of the invitation in the portal.
- The HPC Portal developer fixed the error and deployed the fix.
```
---

### 2023030142003485_Umstellung%20der%20HPC-Accounts%20der%20HS-Coburg%20am%20RRZE%20_%20NHR%40FAU%20-%20corz037h.md
# Ticket 2023030142003485

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject
Umstellung der HPC-Accounts der HS-Coburg am RRZE / NHR@FAU - corz037h

## Keywords
- HPC-Accounts
- HS-Coburg
- RRZE / NHR@FAU
- HPC-Portal
- DFN-AAI/eduGAIN
- SSH-PublicKeys
- SSH-Key
- Passwort
- Windows PowerShell
- Windows Subsystem für Linux
- mobaXtern
- Putty
- JumpHost-Feature
- Deaktivierung
- Datenlöschung

## Summary
The HPC accounts of HS-Coburg at RRZE / NHR@FAU are being transitioned from a paper-based system to a new, fully electronic HPC portal. Users must log in via DFN-AAI/eduGAIN to continue using their accounts. SSH-PublicKeys will be required for access starting at the end of March.

## Root Cause of the Problem
- The user's email address is no longer active, leading to communication issues.

## Solution
- Users should log in to the HPC portal using DFN-AAI/eduGAIN.
- Upload SSH-PublicKeys to the portal for continued access.
- Use Windows PowerShell, Windows Subsystem for Linux, or mobaXtern for SSH access.
- Contact the central email address or visit the HS-Coburg website for updated contact information.

## Additional Information
- HPC accounts not linked to a person by the end of March will be deactivated and data will be deleted after 3 months.
- Windows users are advised to use tools that support OpenSSH.
- Frequent issues related to SSH access can be found in the FAQ.

## Recommendations
- Ensure users are aware of the transition and the importance of logging into the HPC portal.
- Provide clear instructions on how to generate and upload SSH-PublicKeys.
- Offer support for users who encounter issues during the transition process.
```
---

### 2024022042000639_Migration%20of%20mpai%20HPC%20accounts%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20mandato.md
# Ticket 2024022042000639

 # HPC Support Ticket Summary

## Subject
Migration of mpai HPC accounts to new HPC portal / SSH keys become mandatory

## Keywords
- HPC account migration
- SSH keys
- HPC portal
- Single Sign-On (SSO)
- IdM portal
- ClusterCockpit
- Jupyterhub

## Summary
The HPC Admin informed users about the migration of their HPC accounts to a new online HPC portal. Key points include:
- Access to the new HPC portal via SSO using IdM credentials.
- Mandatory use of SSH keys for HPC system access starting end of February.
- Accepted SSH key types: RSA (4096 bits), ECDSA (512 bits), ED25519.
- Documentation and FAQs provided for SSH key generation.
- Expiration of HPC service in IdM portal can be ignored; the new HPC portal is the source for account validity.
- PI or project managers to be contacted for account validity updates.
- Usage statistics visible to PIs and project managers.
- Access to ClusterCockpit and Jupyterhub via SSO links within the HPC portal.

## Root Cause
N/A (Informational ticket)

## Solution
N/A (Informational ticket)

## Additional Notes
- Windows users recommended to use OpenSSH built into Windows (Power)Shell or MobaXterm.
- The HPC portal and IdM portal are completely decoupled.
- Users should contact their PI or project manager for account-related updates.

## References
- [HPC Portal](https://portal.hpc.fau.de)
- [SSH Documentation](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/)
- [FAQs](https://hpc.fau.de/faqs/#ID-230)
---

### 2025012842001338_HPC-Portal%20-%20Probleme%20mit%20SSO-Login.md
# Ticket 2025012842001338

 # HPC-Support Ticket: SSO-Login Issue

## Keywords
- HPC-Portal
- SSO-Login
- Projektpartner Tier3-Grundversorgung
- External Doctoral Student
- Local Account

## Problem Description
An external doctoral student, invited as a "Projektpartner Tier3-Grundversorgung," is experiencing issues with the HPC-Portal. The problem arises from missing information during the SSO-Login process, preventing the creation of an HPC account.

## Root Cause
- Missing information during SSO-Login.

## Steps Taken
- The user has already contacted their organization's IT department.
- The user inquired about potential solutions from the HPC support team, including the possibility of creating a local account if the SSO issue is too complex to resolve.

## Solution
- The HPC support team needs to investigate the SSO-Login issue and determine if the missing information can be retrieved or corrected.
- If the SSO issue is too complex, the support team should consider creating a local account for the user as an alternative solution.

## General Learning
- SSO-Login issues can prevent the creation of HPC accounts.
- Collaboration with the user's IT department is essential for resolving SSO-related problems.
- Creating a local account can be a viable alternative if SSO issues cannot be easily resolved.

## Next Steps
- HPC Admins should review the SSO-Login process and identify the missing information.
- If necessary, coordinate with the user's IT department to resolve the SSO issue.
- If the SSO issue persists, consider creating a local account for the user.
---

### 2024112742003919_Unzustellbar%3A%20New%20invitation%20for%20%22Tier3-Grundversorgung%20HSC%20%28HS-Coburg%29%22%20wai.md
# Ticket 2024112742003919

 # HPC Support Ticket Analysis

## Subject
Unzustellbar: New invitation for "Tier3-Grundversorgung HSC (HS-Coburg)" waiting at portal.hpc.fau.de

## Keywords
- Email delivery issue
- Invitation correction
- Missing character in email address

## Root Cause
The email address provided for the invitation was missing the initial character "l".

## Solution
The HPC Admin corrected the missing "l" in the email address stored in the invitation.

## Lessons Learned
- Always verify email addresses for accuracy before sending invitations.
- Double-check for any missing characters in email addresses to avoid delivery issues.

## Actions Taken
- The HPC Admin corrected the email address in the invitation.
- The ticket was closed after the correction was made.

## General Advice
- Ensure email addresses are correctly entered and verified to prevent delivery failures.
- Regularly review and update contact information to maintain accurate records.
---

### 2024021642000987_Migration%20of%20mptf%20HPC%20accounts%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20mandato.md
# Ticket 2024021642000987

 # HPC Support Ticket Summary

## Subject
Migration of mptf HPC accounts to new HPC portal / SSH keys become mandatory

## Keywords
- HPC account migration
- SSH keys
- HPC portal
- Single Sign-On (SSO)
- IdM portal
- ClusterCockpit
- Jupyterhub

## Summary
- **Migration to New HPC Portal**: Existing HPC accounts are being migrated to a new online HPC portal accessible via SSO using IdM credentials.
- **SSH Keys Mandatory**: Access to HPC systems will require SSH keys starting from the end of February. Accepted key types are RSA (4096 bits), ECDSA (512 bits), and ED25519.
- **Usage Monitoring**: Users can view their usage statistics, which are also accessible by PIs and project managers.
- **ClusterCockpit and Jupyterhub**: Access to these services will now be through SSO links within the HPC portal.

## Root Cause of the Problem
- Users need to adapt to the new HPC portal and SSH key requirements for accessing HPC systems.

## Solution
- **Generate SSH Keys**: Users should generate SSH key pairs with passphrases and upload the public keys to the HPC portal.
- **Use SSO Links**: For ClusterCockpit and Jupyterhub, users should use the SSO links provided within the HPC portal.
- **Contact PI/Project Manager**: For account validity updates or new account requests, users should contact their PI or project manager instead of RRZE.

## Additional Information
- **Documentation and FAQs**: Users unfamiliar with SSH keys should refer to the provided documentation and FAQs.
- **Windows Users**: Recommended to use OpenSSH built into Windows (Power)Shell or MobaXterm instead of Putty.
- **Expiration Notices**: Users can ignore automatic expiration messages from the IdM portal; the HPC portal will be the sole source for account validity.

## Conclusion
The migration to the new HPC portal requires users to adopt SSH keys for access and use SSO links for monitoring tools. Users should contact their PI or project manager for account-related updates.
---

### 2023060742002102_HPC-Konto%3A%20Verl%C3%83%C2%A4ngerung.md
# Ticket 2023060742002102

 # HPC Support Ticket Conversation Analysis

## Keywords
- HPC-Konto
- Verlängerung
- Migration
- SSH keys
- HPC portal
- IdM portal
- Expiration
- PI (Principal Investigator)
- Project manager

## Summary
A user requested an extension for their HPC account, which was set to expire. The HPC admin responded with information about the migration process to a new HPC portal and the necessity of using SSH keys for access.

## Root Cause of the Problem
- The user's HPC account was set to expire.
- The user was unaware of the migration process and the new requirements for account extension.

## Solution
- The user was informed about the migration process and the new HPC portal.
- The user was advised to contact their PI or project manager for account extension.
- The user was instructed to generate and upload SSH keys for future access.

## General Learnings
- HPC accounts are being migrated to a new online portal.
- Access to HPC systems will require SSH keys.
- Account extensions should be requested through the PI or project manager.
- The new HPC portal will be the sole source for account validity.
- Usage statistics will be visible to PIs and project managers.
- Single Sign-On (SSO) will be used for accessing ClusterCockpit and Jupyterhub services.

## Documentation Links
- [HPC Portal](https://portal.hpc.fau.de)
- [SSH Documentation](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/)
- [FAQs](https://hpc.fau.de/faqs/#ID-230)

## Roles Involved
- HPC Admins
- 2nd Level Support Team
- Head of the Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support
- Software and Tools Developer
---

### 2022112542003355_SSH%20Login%20to%20cshpc.rrze.fau.de%20not%20possible%20after%20upload%20of%20public%20key.md
# Ticket 2022112542003355

 # HPC Support Ticket: SSH Login to cshpc.rrze.fau.de not possible after upload of public key

## Keywords
- SSH Login
- Public Key
- Connection Timeout
- IPv4/IPv6 Problem
- LRZ Policy
- MobaXTerm
- OpenSSH Format
- Username Issue

## Summary
The user encountered issues with SSH login to `cshpc.rrze.fau.de` after uploading a public key. The initial attempt from an LRZ Linux cluster login node resulted in a connection timeout, suggesting an LRZ policy issue. The user then attempted to connect from a local Windows machine using MobaXTerm but faced key format and username issues.

## Root Cause
1. **LRZ Policy**: The LRZ Linux cluster login nodes are not allowed to make outbound connections.
2. **Key Format**: The SSH key in `.ppk` format was not compatible with OpenSSH used on the HPC systems.
3. **Username Issue**: The user was using an incorrect username (`di52cac`) instead of the correct one (`b157be16`).

## Solution
1. **Use Local Machine**: Connect from a local machine instead of the LRZ Linux cluster login nodes.
2. **Convert Key Format**: Convert the SSH key from `.ppk` format to OpenSSH format.
3. **Correct Username**: Use the correct username (`b157be16`) for the SSH login.

## Steps Taken
1. **HPC Admin**: Informed the user about the LRZ policy preventing outbound connections.
2. **HPC Admin**: Advised the user to convert the SSH key to OpenSSH format.
3. **HPC Admin**: Provided the correct username (`b157be16`) for the SSH login.

## Conclusion
The user successfully connected to the FAU HPC gateway after converting the SSH key to OpenSSH format and using the correct username. The issue was resolved by addressing the key format and username problems.

## Notes
- Ensure that the correct username is communicated clearly to external users.
- Provide clear instructions for key format conversion and SSH login procedures.
---

### 2023051042000663_fail%20to%20ssh%20to%20fritz.nhr.fau.de.md
# Ticket 2023051042000663

 # HPC-Support Ticket: SSH Access Issue

## Subject
- User unable to SSH into HPC cluster using provided username and SSH key.

## Keywords
- SSH
- Public Key Authentication
- SSH Key
- Username
- Permission Denied
- Debug Output

## Problem Description
- User attempted to SSH into the HPC cluster using an email-based username and encountered a "Permission denied (Publickey)" error.
- User uploaded a public SSH key to the HPC portal but was prompted for a password instead of the SSH key passphrase.

## Root Cause
- Incorrect username format: User attempted to use an email-based username instead of the assigned username.
- SSH key not located in the default file: User's SSH key was stored in a non-standard file location.

## Solution
- HPC Admin provided the correct username format: `b172da10@cshpc.rrze.uni-erlangen.de`.
- HPC Admin suggested three solutions to resolve the SSH key issue:
  1. Use the `-i` option to specify the SSH key file: `ssh -i /Users/xiaojun/.ssh/SU2ETH b172da10@cshpc.rrze.uni-erlangen.de`.
  2. Write an SSH config file to specify the key file location.
  3. Copy the SSH key to the default file location.
- User confirmed that writing an SSH config file resolved the issue.

## Documentation
- HPC Admin provided a link to the documentation for SSH secure shell access to HPC systems: [SSH Documentation](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/).

## Closure
- The ticket was closed after the user confirmed that the issue was resolved.
---

### 2024040842004128_Regarding%20access%20to%20my%20hpc%20account.md
# Ticket 2024040842004128

 # HPC Support Ticket: Access Issue with HPC Account

## Keywords
- SSH access
- Permission denied
- Public SSH key
- Password reset
- Debug information

## Problem Description
- **User Issue**: Unable to access HPC account via SSH, receiving "Permission denied (publickey,password)" error.
- **Commands Used**:
  ```sh
  ssh bcml002h@csnhr.nhr.fau.de
  ssh bcml002h@woody.nhr.fau.de
  ```
- **Error Message**:
  ```sh
  Permission denied (publickey,password)
  ```

## Root Cause
- Possible incorrect password or issues with SSH key configuration.

## Solution
- **HPC Admin Response**:
  - Refer to the FAQ on SSH for troubleshooting steps.
  - Provide debug information if the FAQ does not resolve the issue.
  - FAQ Link: [FAQ on SSH](https://doc.nhr.fau.de/faq/#ssh)

## General Learnings
- Always check the FAQ for common issues related to SSH access.
- Provide detailed debug information when seeking further assistance.
- Ensure proper configuration of SSH keys and correct password usage.

## Next Steps for Support
- Review the FAQ on SSH.
- Gather and analyze debug information if the issue persists.
- Assist with password reset if necessary.

---

This documentation can be used to troubleshoot similar SSH access issues in the future.
---

### 2024103142002431_FUB%20SSO%20Login.md
# Ticket 2024103142002431

 ```markdown
# HPC-Support Ticket: FUB SSO Login

## Keywords
- SSO Login
- FU-Berlin
- Missing Attributes
- SAML Metadata
- DFN
- eduGAIN

## Problem Description
User attempted to log in with an FU-Berlin SSO account and received an error message indicating that required attributes for account creation were missing.

## Root Cause
The SSO login was successful, but the following attributes were missing:
- `urn:oid:2.5.4.42` - `urn:mace:dir:attribute-def:givenName`
- `urn:oid:2.5.4.4` - `urn:mace:dir:attribute-def:sn`
- `urn:oid:0.9.2342.19200300.100.1.3` - `urn:mace:dir:attribute-def:mail`
- `urn:oid:1.3.6.1.4.1.5923.1.1.1.6` - `urn:mace:dir:attribute-def:eduPersonPrincipalName`
- `urn:oid:1.3.6.1.4.1.5923.1.1.1.9` - `urn:mace:dir:attribute-def:eduPersonScopedAffiliation`

## Solution
The user was advised to contact the FU-Berlin support to activate the missing attributes for the service provider (SP) `https://portal.hpc.fau.de/saml/metadata`. Support addresses for organizations can be found at:
- [DFN](https://tools.aai.dfn.de/entities/)
- [eduGAIN](https://technical.edugain.org/isFederatedCheck/Organisations/)

## General Learning
- Ensure that all required attributes are activated for SSO login.
- Users should contact their organization's support to resolve missing attribute issues.
- HPC Admins can guide users to the appropriate support channels.
```
---

### 2019091742002346_Unable%20to%20login%20RRZE%20via%20SSH.md
# Ticket 2019091742002346

 # HPC Support Ticket: Unable to Login via SSH

## Keywords
- SSH login
- Connection reset by peer
- RRZE HPC
- ssh_exchange_identification

## Problem Description
User attempted to log in to the RRZE HPC via SSH but received the error message: `ssh_exchange_identification: read: Connection reset by peer`.

## Root Cause
The error message indicates that the SSH connection was abruptly closed by the server. This could be due to various reasons such as network issues, server overload, or incorrect SSH configuration.

## Solution
- **Check Network Connectivity**: Ensure that the user has a stable internet connection.
- **Verify SSH Configuration**: Confirm that the SSH client is correctly configured.
- **Server Status**: Check if the server is experiencing high load or maintenance.
- **Contact HPC Admins**: If the issue persists, the user should contact the HPC Admins for further assistance.

## General Learnings
- SSH connection issues can be caused by network problems, server issues, or misconfigurations.
- The error message `ssh_exchange_identification: read: Connection reset by peer` indicates a problem on the server side.
- Basic troubleshooting steps include checking network connectivity and SSH configuration.
- For persistent issues, escalation to HPC Admins is recommended.
---

### 2024100342000512_ssh%20login%20issue.md
# Ticket 2024100342000512

 ```markdown
# SSH Login Issue

## Keywords
- SSH login
- Command prompt
- Filesystem issue

## Problem Description
- User unable to get the command prompt after SSH login to `csnhr`.
- Welcome message and last login info are displayed, but no command prompt.

## Root Cause
- Filesystem issue on the HPC system.

## Solution
- HPC Admin identified and resolved the filesystem issue.

## Lessons Learned
- Filesystem issues can prevent the command prompt from appearing after SSH login.
- Quick identification and resolution of filesystem problems can restore normal functionality.

## Actions Taken
- HPC Admin acknowledged the issue and worked on resolving the filesystem problem.
- User confirmed the issue was fixed.
```
---

### 2023103042001043_HPC%20account%20for%20the%20ArchSup%20exercise%20students.md
# Ticket 2023103042001043

 ```markdown
# HPC Support Ticket Conversation Summary

## Keywords
- HPC Account Creation
- SSH Key Submission
- Job Submission Error
- Performance Counters
- Export Control Regulations

## General Learnings
- Ensure correct email address for managing student HPC accounts.
- Use appropriate account names to avoid conflicts.
- Inform students about account creation and activation.
- Apply solutions to all affected accounts.
- Use `--constraint=hwperf` instead of `--gres=likwid:1` for performance counters.

## Root Causes and Solutions

### HPC Account Creation
- **Issue**: Conflict with existing account names.
- **Solution**: Use unique account names that align with the course name (e.g., `arch205h` instead of `cama205h`).

### SSH Key Submission
- **Issue**: Unclear submission process for new SSH keys.
- **Solution**: Inform students to submit SSH keys via the appropriate portal (`https://portal.hpc.fau.de/` or `http://www.idm.fau.de/`).

### Job Submission Error
- **Issue**: Invalid account or account/partition combination specified.
- **Solution**: Ensure all accounts are correctly added to the SLURM database and apply the solution to all accounts.

### Performance Counters
- **Issue**: Access to performance monitoring registers locked.
- **Solution**: Use `--constraint=hwperf` instead of `--gres=likwid:1` for allocating nodes with performance counters.

### Export Control Regulations
- **Issue**: Ensure compliance with export control regulations for international students.
- **Solution**: Inform students about export control regulations and provide relevant links for more information.

## Conclusion
This report summarizes the key issues and solutions discussed in the HPC support ticket conversation. It serves as a documentation for support employees to look up help for similar errors in the future.
```
---

### 2024051342000218_New%20HPC%20access.md
# Ticket 2024051342000218

 ```markdown
# HPC Support Ticket Conversation Summary

## Issue
User Shubham Gupta is unable to connect to the new HPC account using VS Code and SSH. The user has generated separate SSH keys for the new account but is facing authentication and connection issues.

## Key Points
- **SSH Configuration**: The user's SSH configuration file needs to be updated to include the new account details.
- **VS Code Configuration**: The user needs to update the VS Code configuration to include the new account details.
- **Authentication Issues**: The user is prompted for a password and authentication fails.
- **Connection Issues**: The user is unable to establish a connection to the HPC account from VS Code.

## Troubleshooting Steps
1. **SSH Configuration**:
   - Ensure the SSH configuration file includes the correct details for the new account.
   - Example configuration:
     ```plaintext
     Host tinyx-iwfa
       HostName tinyx.nhr.fau.de
       ProxyJump cshpc-iwfa
       User iwfa044h
       IdentityFile ~/.ssh/HPC_SSH

     Host cshpc-iwfa
       HostName csnhr.nhr.fau.de
       User iwfa044h
       IdentityFile ~/.ssh/HPC_SSH

     Host tinyx-iwi5
       HostName tinyx.nhr.fau.de
       ProxyJump cshpc-iwi5
       User iwi5204h
       IdentityFile ~/.ssh/id_ed25519_nhr_fau

     Host cshpc-iwi5
       HostName csnhr.nhr.fau.de
       User iwi5204h
       IdentityFile ~/.ssh/id_ed25519_nhr_fau
     ```

2. **VS Code Configuration**:
   - Update the VS Code configuration to include the new account details.
   - Ensure the remotePlatform is correctly configured.

3. **Authentication Issues**:
   - Ensure the correct SSH key is being used for the new account.
   - Verify that the SSH key is uploaded to the HPC account.

4. **Connection Issues**:
   - Check the SSH output for any errors or warnings.
   - Ensure the correct hostname and username are being used in the SSH command.

## Resolution
- **SSH Configuration**: The user updated the SSH configuration file to include the correct details for the new account.
- **VS Code Configuration**: The user updated the VS Code configuration to include the new account details.
- **Authentication Issues**: The user verified that the correct SSH key is being used for the new account and that the SSH key is uploaded to the HPC account.
- **Connection Issues**: The user checked the SSH output for any errors or warnings and ensured the correct hostname and username are being used in the SSH command.

## Next Steps
- The user will continue to troubleshoot the issue with the help of the HPC support team.
- The user will update the SSH and VS Code configurations as needed.
- The user will verify the SSH key and authentication details.

## Additional Resources
- [VS Code SSH Configuration Documentation](https://doc.nhr.fau.de/access/ssh-vscode/)
```
---

### 2023030142003421_Umstellung%20der%20HPC-Accounts%20der%20HS-Coburg%20am%20RRZE%20_%20NHR%40FAU%20-%20corz09.md
# Ticket 2023030142003421

 # HPC Support Ticket Conversation Summary

## Subject
Umstellung der HPC-Accounts der HS-Coburg am RRZE / NHR@FAU - corz09

## Keywords
- HPC Accounts
- DFN-AAI/eduGAIN
- HPC-Portal
- SSH-PublicKeys
- SSH-Key
- Password Access
- Windows PowerShell
- Windows Subsystem for Linux
- mobaXterm
- OpenSSH
- Putty
- JumpHost-Feature
- Account Deactivation
- Data Deletion

## General Learnings
- The HPC accounts at HS-Coburg are transitioning from a paper-based system to an electronic HPC-Portal.
- Users need to log in via DFN-AAI/eduGAIN to link their accounts to their identities.
- SSH-PublicKeys will be required for access starting at the end of March.
- Windows users are advised to use Windows PowerShell, Windows Subsystem for Linux, or mobaXterm.
- Accounts not linked by the end of March will be deactivated and data deleted after 3 months.

## Root Cause of the Problem
- Certificate has expired.

## Solution
- Users must log in to the HPC-Portal using DFN-AAI/eduGAIN to link their accounts.
- Upload SSH-PublicKeys to the HPC-Portal for continued access.
- Use recommended SSH clients for Windows users.

## Additional Resources
- [HPC-Portal Usage](https://hpc.fau.de/systems-services/documentation-instructions/getting-started/nhrfau-hpc-portal-usage/)
- [SSH Access Documentation](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/)
- [FAQ on SSH Access](https://hpc.fau.de/faqs/#innerID-13183)
- [mobaXterm](https://mobaxterm.mobatek.net/)

## Contacts for Further Assistance
- Rechenzentrum der HS-Coburg
- Fakultät Wirtschaftswissenschaften der HS-Coburg
- HPC Admins
- 2nd Level Support Team
- Head of the Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support and Applications for Grants
- Software and Tools Developer
---

### 2024011842002732_Migration%20of%20iwpa%20HPC%20accounts%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20mandato.md
# Ticket 2024011842002732

 ```markdown
# HPC Support Ticket: Migration of iwpa HPC Accounts to New HPC Portal / SSH Keys Become Mandatory

## Keywords
- HPC account migration
- SSH keys
- HPC portal
- Single Sign-On (SSO)
- IdM portal
- ClusterCockpit
- Jupyterhub

## Summary
The HPC services at FAU are migrating existing iwpa HPC accounts from the IdM portal to a new, purely online HPC portal. Access to HPC systems will require SSH keys starting from the end of January. Users need to generate and upload SSH public keys to the new portal.

## Key Points
- **Migration Process**: Accounts are being migrated to a new HPC portal accessible via SSO using IdM credentials.
- **SSH Keys**: Access to HPC systems will require SSH keys (RSA 4096 bits, ECDSA 512 bits, ED25519). Users must generate and upload their public keys.
- **Documentation**: Detailed instructions and FAQs are available for users unfamiliar with SSH keys.
- **Windows Users**: Recommended to use OpenSSH built into Windows (Power)Shell or MobaXterm instead of Putty.
- **IdM Portal Expiration**: Users will receive an email about HPC service expiration in the IdM portal, which can be ignored. The new HPC portal will be the sole source for account validity.
- **Account Validity**: Users need to contact their PI or project manager to update account validity.
- **Usage Statistics**: PIs and project managers can view usage statistics in the HPC portal.
- **ClusterCockpit and Jupyterhub**: Users must use Single Sign-On links from within the HPC portal for these services.

## Root Cause of the Problem
- Users have not logged into the new HPC portal or uploaded their SSH public keys.

## Solution
- Users should log into the HPC portal using SSO with their IdM credentials.
- Generate and upload SSH public keys to the HPC portal.
- Follow the provided documentation and FAQs for assistance.

## Additional Notes
- The IdM portal and the new HPC portal are completely decoupled.
- Users should contact their PI or project manager for account validity updates.
- The HPC portal provides usage statistics for different HPC systems.
```
---

### 2024051042002883_Ask%20Password%20While%20remote%20SSH%20Connection.md
# Ticket 2024051042002883

 ```markdown
# HPC Support Ticket: Ask Password While Remote SSH Connection

## Keywords
- SSH password
- Remote connection
- Password authentication issues
- HPC system access
- Troubleshooting

## Problem Description
The user is experiencing difficulties accessing the HPC system remotely due to password authentication issues. Despite following standard procedures, the user is unable to establish a successful connection.

## Root Cause
- Password authentication issues during SSH connection.

## Troubleshooting Steps
- User provided screenshots and photos detailing the output and relevant files associated with the issue.

## Solution
- HPC Admin advised the user to ensure proper on-boarding procedures are followed.

## Notes
- Access to the HPC system is crucial for the user's ongoing work and projects.
- Additional information may be required from the user for further troubleshooting.

## Follow-Up
- Ensure the user is properly on-boarded and has the correct credentials for SSH access.
- Verify that the user is following the correct procedures for remote SSH connection.
```
---

### 2024031142000609_Migration%20of%20gwpa%20HPC%20accounts%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20mandato.md
# Ticket 2024031142000609

 # HPC Support Ticket: Migration to New HPC Portal and SSH Key Requirement

## Keywords
- HPC portal migration
- SSH keys
- Single Sign-On (SSO)
- IdM portal
- Account validity
- Usage statistics
- ClusterCockpit
- Jupyterhub

## Summary
The HPC services at FAU are migrating from the IdM portal to a new online HPC portal. Users need to generate and upload SSH keys for access. The HPC portal will be the sole source for account validity, and usage statistics will be visible to PIs and project managers.

## Key Points
- **Migration to New HPC Portal**: The migration process has started, and users should log in to the new portal using SSO with their IdM credentials.
- **SSH Keys Mandatory**: From the end of March, access to HPC systems will require SSH keys. Accepted types are RSA (4096 bits), ECDSA (512 bits), and ED25519.
- **Account Validity**: The HPC portal will manage account validity independently of the IdM portal. Users should contact their PI or project manager for extensions.
- **Usage Statistics**: PIs and project managers can view usage statistics in the HPC portal.
- **ClusterCockpit and Jupyterhub**: Users should use the SSO link from the HPC portal to access these services.

## User Response
- The user is away from the office until 27.03 and will respond after that date.

## Root Cause of the Problem
- N/A (Informational ticket)

## Solution
- N/A (Informational ticket)

## Additional Resources
- [SSH Secure Shell Access Documentation](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/)
- [FAQs](https://hpc.fau.de/faqs/#ID-230)

## Notes
- Windows users are recommended to use OpenSSH built into the Windows (Power)Shell or MobaXterm instead of Putty.
- The IdM portal and the new HPC portal are completely decoupled.
---

### 42088811_HPC-Login.md
# Ticket 42088811

 ```markdown
# HPC-Login Issue: Connection Reset by Peer

## Keywords
- HPC Login
- Connection Reset by Peer
- Uni-Netz
- Wohnheim
- VPN Client
- Firewall

## Problem Description
- User unable to connect to HPC (memoryhog) using Putty or WinSCP.
- Error message: "Network error: connection reset by peer!"
- VPN connection also not working, despite previously functioning.

## Root Cause
- Possible firewall changes in the Wohnheim network.
- No login attempts recorded on memoryhog, indicating connection not reaching the server.

## Solution
- User advised to check with local Wohnheim admins regarding recent firewall changes.
- Verify if the issue is with the VPN connection or the connection to memoryhog via VPN.

## General Learnings
- Network issues can be caused by local network configurations, such as firewall settings.
- Checking login attempts on the server can help diagnose connection issues.
- Communication with local network admins is crucial for troubleshooting network-related problems.
```
---

### 2022092042004126_Problem%20beim%20einloggen%20auf%20fritz.md
# Ticket 2022092042004126

 ```markdown
# HPC-Support Ticket Conversation: Problem beim einloggen auf fritz

## Keywords
- SSH login
- Passphrase
- Key authentication
- fritzcluster

## Problem Description
User is unable to log in to the `fritz` cluster via SSH. The user is prompted to enter the passphrase for the key `/home/red35846/hpcfau` multiple times.

## Root Cause
The root cause of the problem is likely related to the SSH key authentication process. The user's key might be incorrectly configured or the passphrase might be incorrect.

## Solution
- Verify the correctness of the SSH key and its passphrase.
- Ensure the SSH key is properly configured and added to the SSH agent.
- Check the permissions of the SSH key file.

## General Learnings
- SSH key authentication issues are common and can often be resolved by verifying the key and passphrase.
- Proper configuration and permissions of the SSH key file are crucial for successful authentication.
- Users should be guided to check their SSH key setup and passphrase when encountering such issues.
```
---

### 2025011042001022_Missing%20invitation.md
# Ticket 2025011042001022

 # Missing Invitation Issue

## Keywords
- Invitation
- Email Alias
- SSO Login
- HPC Portal
- Missing Invitation

## Problem Description
- User received an invitation to a project via an email alias.
- User logged in via SSO but could not see the invitation in their account.

## Root Cause
- The invitation was sent to an email alias instead of the primary email address registered with the HPC Portal.

## Solution
- The invitation must be sent to the primary email address registered with the HPC Portal.
- User should request the sender to resend the invitation to the correct email address.

## General Learnings
- Always ensure that invitations are sent to the primary email address registered with the HPC Portal.
- Aliases may not be recognized by the system, leading to issues with invitation visibility.

## Next Steps for Support
- Verify the email address registered with the HPC Portal.
- Advise the user to request a new invitation to the correct email address if necessary.
---

### 2023080142002682_Login%20nach%20SSH%20key%20%C3%83%C2%BCber%20HPC%20Portal.md
# Ticket 2023080142002682

 # HPC Support Ticket: SSH Key Authentication Issues

## Keywords
- SSH Key Authentication
- HPC Portal
- LDAP
- SVN Repository
- SSH Config
- Password Prompt

## Problem Description
- **Root Cause**: The HPC group with ID `gwgi` experienced SSH connection issues after a recent configuration change. Despite successful SSH key authentication, users were unable to establish SSH tunnels.
- **Additional Issue**: After resolving the initial problem, users encountered a password prompt when committing to an SVN repository, which was not recognized due to the SSH key change.

## Solution
- **Initial Issue**: The `gwgi.*` entry in the precedence configuration was still commented out, causing the system to use LDAP instead of the HPC Portal. The HPC Admin activated the entry to resolve the issue.
- **SVN Issue**: The SVN repository was configured to use password authentication, which was no longer valid after the SSH key change. The solution involved using `svn+ssh://` with proper SSH config settings or accessing the repository directly via `file:///` if it resides on the HPC file system.

## General Learnings
- Ensure that configuration changes are fully implemented and verified.
- SSH key authentication issues can be diagnosed using `ssh -v`.
- SVN repositories can be configured to use SSH keys for authentication, and proper SSH config settings are crucial.
- Direct access to repositories on the HPC file system can bypass authentication issues.

## Next Steps
- Verify that all configuration changes are correctly applied.
- Update documentation to reflect changes in authentication methods.
- Provide users with guidance on configuring SVN to use SSH keys.
---

### 2024041842004654_Assistance%20Required%3A%20Invitation%20Not%20Displaying%20on%20HPC%20Portal.md
# Ticket 2024041842004654

 # HPC Support Ticket: Invitation Not Displaying on HPC Portal

## Keywords
- Invitation Email
- HPC Portal
- SSO (Single Sign-On)
- IdM Credentials
- Email Mismatch
- University of Bayreuth

## Problem Description
The user received an invitation email to access services on the HPC portal but the invitation does not appear under 'User' -> 'Your Invitations'.

## Root Cause
The invitation email was sent to the user's primary email address (`tong.wu@uni-bayreuth.de`), but the University of Bayreuth transmits a different email address (`bt308838@uni-bayreuth.de`) via SSO. This mismatch caused the invitation to not be visible on the portal.

## Solution
The HPC Admin identified the email mismatch as the root cause. The user should ensure that the email address used for the invitation matches the one transmitted via SSO.

## General Learnings
- Ensure that the email address used for invitations matches the one used for SSO.
- Check the FAQ for common issues related to invitations and account data visibility.
- Always provide clear descriptions of issues when seeking support.

## References
- [FAQ: I received an invite mail from the HPC portal but there is no account data visible](https://doc.nhr.fau.de/faq/#i-received-an-invite-mail-from-the-hpc-portal-but-there-is-no-account-data-visible)
- [HPC Portal Documentation](https://doc.nhr.fau.de/hpc-portal/)
---

### 2020051442002276_notice%20on%20security%20incidents%20at%20HPC%20centers%20worldwide.md
# Ticket 2020051442002276

 # HPC Support Ticket: Security Incidents at HPC Centers Worldwide

## Keywords
- Security incident
- Compromised systems
- Stolen user credentials
- SSH keys
- Passphrase
- Command history
- Unusual observations

## Summary
Several HPC centers worldwide have experienced security incidents, leading to system downtimes. The root cause is suspected to be attackers using stolen user credentials to access systems, potentially spreading from one compromised site to another.

## Root Cause
- **Stolen user credentials**: Attackers are using stolen credentials to gain access to HPC systems.

## Recommendations
- **Use different passwords**: Always use different passwords for different sites or services.
- **Secure SSH keys**: Ensure SSH keys use a secure passphrase.
- **Different SSH keys**: Use different SSH keys for different sites whenever possible.
- **Report usage of compromised sites**: Inform HPC Admins if you have used any external HPC sites known to be compromised.
- **Report unusual observations**: Notify HPC Admins of any strange entries in command history, unexpected files or directories, or unusual "last login" entries.

## Actions Taken
- HPC Admins are investigating and assessing the situation with colleagues across Germany.
- Users are advised to be extra vigilant and follow the recommended security practices.

## Status
- Investigation ongoing.
- No indications of compromise at RRZE, but vigilance is advised.

## Next Steps
- Continue monitoring and investigating the situation.
- Keep users informed about progress and disclose further information as available.

## Notes
- The security incident highlights the importance of strong and unique passwords, secure SSH keys, and vigilant monitoring of system activities.

---

This documentation is intended to help support employees understand and respond to similar security incidents in the future.
---

### 2024022742003169_Migration%20of%20iwi2%20HPC%20accounts%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20mandato.md
# Ticket 2024022742003169

 # HPC Support Ticket Summary

## Subject
Migration of iwi2 HPC accounts to new HPC portal / SSH keys become mandatory

## Keywords
- HPC account migration
- SSH keys
- HPC portal
- Single Sign-On (SSO)
- IdM portal
- Account validity
- Usage statistics
- ClusterCockpit
- Jupyterhub

## General Learnings
- **Migration Process**: The migration of HPC accounts from the IdM portal to a new HPC portal is underway.
- **SSH Keys**: Access to HPC systems will require SSH keys from March 11, 2024. Accepted SSH key types are RSA (4096 bits), ECDSA (512 bits), and ED25519.
- **Portal Access**: The new HPC portal can be accessed at [https://portal.hpc.fau.de](https://portal.hpc.fau.de) using SSO with IdM credentials.
- **Account Validity**: The HPC portal will be the sole source for account validity starting from the end of February.
- **Usage Statistics**: Users, PIs, and project managers can view usage statistics in the HPC portal.
- **ClusterCockpit and Jupyterhub**: Access these services via SSO links from within the HPC portal.

## Root Cause of the Problem
- Users need to transition to the new HPC portal and set up SSH keys for continued access to HPC systems.

## Solution
- **Login to HPC Portal**: Use SSO with IdM credentials to access the new HPC portal.
- **Generate and Upload SSH Keys**: Create SSH key pairs with a passphrase and upload the public key to the HPC portal.
- **Ignore IdM Expiration Emails**: The HPC portal will manage account validity, so ignore automatic expiration messages from the IdM portal.
- **Contact PI/Project Manager**: For account validity updates or new account requests, contact the PI or project manager instead of RRZE.

## Additional Resources
- [SSH Documentation](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/)
- [FAQs](https://doc.nhr.fau.de/faq/#ssh)

## Support Teams
- **HPC Admins**: Manage the HPC systems and user accounts.
- **2nd Level Support Team**: Provide technical support for HPC users.
- **Head of the Datacenter**: Oversees the datacenter operations.
- **Training and Support Group Leader**: Manages training and support activities.
- **NHR Rechenzeit Support**: Handles applications for grants and support.
- **Software and Tools Developer**: Develops software and tools for HPC systems.
---

### 2024091742004414_Request%20for%20HPC%20Invitation%20Renewal.md
# Ticket 2024091742004414

 # HPC Invitation Renewal Issue

## Keywords
- HPC Invitation
- Expired Invitation
- Renewal
- Unix Group
- Access Issue

## Problem Description
- **Root Cause**: User's HPC invitation expired due to oversight.
- **Symptom**: User unable to be re-invited to gain access to the HPC.

## Solution
- **Action Taken**: HPC Admin deleted the old invitation.
- **Result**: A new invitation can now be created for the user.

## General Learnings
- Expired invitations need to be deleted to allow for new invitations.
- Users should be reminded to renew invitations before expiration to avoid access issues.

## Roles Involved
- **HPC Admins**: Provided support and resolved the issue.
- **User**: Reported the problem and followed up with gratitude.

## Related Teams
- 2nd Level Support Team
- Datacenter Management
- Training and Support Group
- NHR Rechenzeit Support
- Software and Tools Development

## Relevant Links
- [HPC FAU](https://hpc.fau.de/)
- [Support Email](mailto:support-hpc@fau.de)
---

### 2023112342003839_Re%3A%20New%20invitation%20for%20%22Tier3%20Grundversorgung%20Uni-Bayreuth%20%28via%20IT-Servicezent.md
# Ticket 2023112342003839

 # HPC Support Ticket Analysis

## Keywords
- HPC Account Setup
- SSO Login
- Invitation Issue
- SSH Key Upload
- SSH Connection
- Email Mismatch

## Summary
The user encountered issues with accepting an invitation and establishing an SSH connection to the HPC cluster. The root cause was an email mismatch between the invitation and the DFN-AAI email address.

## Detailed Analysis

### Problem 1: Invitation Not Visible
- **Root Cause**: Email mismatch between the invitation and the DFN-AAI email address.
- **Solution**: HPC Admins resolved the email mismatch, allowing the user to see and accept the invitation.

### Problem 2: SSH Connection Issue
- **Root Cause**: User attempted to use UBT password instead of SSH key for authentication.
- **Solution**: HPC Admins advised the user to wait one day after accepting the invitation and to use the uploaded SSH key for the connection.

## Steps Taken
1. **Invitation Issue**:
   - User reported not seeing the invitation.
   - HPC Admins identified and resolved the email mismatch.
   - User was able to see and accept the invitation.

2. **SSH Connection Issue**:
   - User reported unable to establish an SSH connection using UBT password.
   - HPC Admins advised waiting one day and using the uploaded SSH key for authentication.

## Conclusion
The primary issues were resolved by addressing the email mismatch and providing clear instructions for SSH key usage. This ticket highlights the importance of accurate email configuration and proper SSH key management for HPC access.

## Future Reference
- Ensure email addresses are correctly configured for invitations.
- Advise users to wait for account activation and use SSH keys for authentication.
- Provide clear instructions for uploading and using SSH keys.
---

### 2024030442003567_Problem%20about%20my%20account.md
# Ticket 2024030442003567

 # HPC Support Ticket: Problem with Account Expiration

## Keywords
- Account expiration
- Service package HPC
- IDM Portal
- SSH keys
- Portal migration

## Problem
- User reported that their HPC account service package showed as expired in the IDM Portal.

## Root Cause
- Misunderstanding due to a change in the management portal.
- User did not read the migration email sent earlier.

## Solution
- Inform the user about the portal migration and the mandatory use of SSH keys.
- Direct the user to read the migration email for detailed instructions.
- Guide the user to generate and upload SSH keys as per the new portal requirements.

## General Learnings
- Always check for recent emails regarding system updates or migrations.
- SSH keys are mandatory for login after the portal migration.
- Account extensions are managed by supervisors through the portal.

## Actions Taken
- HPC Admin clarified that the account did not expire but the management portal changed.
- User was directed to read the migration email for further instructions.

## References
- [Generating an SSH Key Pair](https://doc.nhr.fau.de/access/ssh-command-line/#generating-an-ssh-key-pair)
- HPC Support Email: support-hpc@fau.de
- HPC Website: [FAU HPC](https://hpc.fau.de/)
---

### 2024121242000831_FAU%20HPC%20-%20iwfa108h%20_%20VScode.md
# Ticket 2024121242000831

 # HPC-Support Ticket Conversation Summary

## Subject: FAU HPC - iwfa108h / VS Code

### Keywords:
- VS Code
- SSH
- Permission Denied
- Corrupted Server Files
- Factory Reset
- GPU Out-of-Memory
- Login Options Disabled
- Cache Stuck
- Python Packages

### Problem:
- User unable to access VS Code on HPC server.
- Error messages indicate failure to upload and unpack VS Code server files.
- Additional issues include GPU out-of-memory messages, login options being disabled, cache getting stuck, and Python package errors.

### Root Cause:
- Possibly corrupted VS Code server files on the remote machine.
- Permission issues preventing the deletion of corrupted files.

### Solution:
1. **Delete Corrupted Server Files:**
   - User was advised to delete the possibly corrupted server files on the remote machine using the command:
     ```sh
     rm -rf ~/.vscode-server
     ```
   - This should be done from a standard SSH login terminal.

2. **Reinstall VS Code Server:**
   - Follow the documentation to set up VS Code again: [Documentation Link](https://doc.nhr.fau.de/access/ssh-vscode/)

3. **Address Permission Issues:**
   - Ensure the user has the necessary permissions to delete files in their home directory.
   - If permission denied errors persist, contact HPC Admins for further assistance.

### Additional Notes:
- User reported multiple issues beyond VS Code, such as GPU out-of-memory messages, login options being disabled, cache getting stuck, and Python package errors.
- User's project advisor suggested a factory reset, but HPC Admins advised troubleshooting specific issues first.
- If issues persist, a factory reset may be considered as a last resort.

### Follow-Up:
- User should attempt the suggested solutions and report back if issues persist.
- HPC Admins should be prepared to assist with permission issues or further troubleshooting if needed.

### Conclusion:
- The primary issue with VS Code access was likely due to corrupted server files.
- Addressing permission issues and reinstalling the VS Code server should resolve the problem.
- Additional issues reported by the user may require further investigation and troubleshooting.
---

### 2024022842002337_Zugang%20HPC.md
# Ticket 2024022842002337

 # HPC Support Ticket: Access Issue

## Keywords
- HPC Access
- Login Issue
- Smartcard Error
- Account Reactivation
- IIS Intranet
- Fraunhofer Gesellschaft

## Problem Description
- User unable to log in to HPC.
- Previous account details provided (Nutzerkennung: ip82afug, HPC Username: iwal004h).
- Error message received: "Die Anmeldung ist fehlgeschlagen. Wahrscheinlich ist Ihre Smartcard nicht korrekt eingebunden."

## Root Cause
- Smartcard not correctly integrated.
- Changes in HPC access modalities since the user's last usage.

## Solution
- HPC Admin redirected the user to Dr. Turowski for further assistance.
- Dr. Turowski informed the user about the new registration process via the IIS Intranet.
- User will receive a new invitation linked to their IIS account.

## General Learnings
- HPC access modalities may change over time.
- Users should refer to the IIS Intranet for updated registration procedures.
- Smartcard integration issues can cause login failures.
- HPC Admins can redirect users to specific support personnel for specialized assistance.

## References
- [IIS Intranet HPC Registration](https://intern.iis.fhg.de/display/hpc/Register+for+HPC+access)
- [HPC Portal](https://portal.hpc.fau.de/)
- [FAU HPC Support](mailto:support-hpc@fau.de)
- [FAU HPC Website](https://hpc.fau.de/)
---

### 2024022142000833_Migration%20of%20iww2%20HPC%20accounts%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20mandato.md
# Ticket 2024022142000833

 # HPC Support Ticket Summary

## Subject
Migration of iww2 HPC accounts to new HPC portal / SSH keys become mandatory

## Keywords
- HPC account migration
- SSH keys
- HPC portal
- Single Sign-On (SSO)
- IdM portal
- SSH key types (RSA, ECDSA, ED25519)
- Usage statistics
- ClusterCockpit
- Jupyterhub

## What Can Be Learned
- **Migration Process**: The migration of HPC accounts from the IdM portal to a new HPC portal is underway.
- **SSH Keys**: Access to HPC systems will require SSH keys only. Accepted types are RSA (4096 bits), ECDSA (512 bits), and ED25519.
- **HPC Portal**: The new HPC portal can be accessed via SSO using IdM credentials. It will be the sole source for account validity.
- **Usage Statistics**: Users and their PIs/project managers can view usage statistics in the HPC portal.
- **ClusterCockpit and Jupyterhub**: Access to these services will be through SSO links within the HPC portal.
- **Account Management**: Extensions or terminations of HPC accounts should be communicated to the PI or project manager, not directly to the HPC support team.

## Root Cause of the Problem
- Users need to transition to the new HPC portal and set up SSH keys for continued access to HPC systems.

## Solution
- Users should log in to the new HPC portal using SSO, generate and upload SSH keys, and use the portal for all account-related activities.
- For Windows users, it is recommended to use OpenSSH built into the Windows (Power)Shell or MobaXterm instead of Putty.
- Users should contact their PI or project manager for account validity updates.

## Additional Resources
- [HPC Portal](https://portal.hpc.fau.de)
- [Documentation](https://doc.nhr.fau.de/access/overview/)
- [FAQs](https://doc.nhr.fau.de/faq/)
---

### 2024022942002308_Problem%20with%20%20Upload%20SSH%20public%20key%20to%20the%20HPC%20Portal.md
# Ticket 2024022942002308

 # HPC Support Ticket: Problem with Uploading SSH Public Key to the HPC Portal

## Keywords
- SSH key generation
- Public key upload
- HPC Portal
- SSO login
- Key content
- Alias
- ssh-keygen
- Default location
- `cat ~/.ssh/id_*pub`
- `-f` flag
- `-i` flag
- SSH config file

## Problem Description
The user successfully generated an SSH public/private key pair on their local machine but is unable to locate the public key file to upload it to the HPC Portal. The user is prompted to enter an "Alias" and "Key Content" but cannot find the key content.

## Root Cause
The user is unaware of the default location where the SSH public key is saved and how to retrieve its content.

## Solution
1. **Default Location**: The default location for the SSH public key is `~/.ssh/id_*pub`.
2. **Retrieve Key Content**: Use the command `cat ~/.ssh/id_*pub` to display the content of the public key file.
3. **Custom Location**: If a non-default location is used, specify the file location with the `-f` flag during key generation (e.g., `ssh-keygen -f /path/to/key`).
4. **SSH Config**: If using a non-default location, configure SSH to use the custom key file by editing the SSH config file or using the `-i` flag.

## Additional Resources
- [SSH Command Line Documentation](https://doc.nhr.fau.de/access/ssh-command-line/)

## Next Steps
If the user continues to experience issues, they should consult their local admin for further assistance.

## Roles Involved
- **HPC Admins**: Provided guidance on locating and retrieving the SSH public key.
- **User**: Experienced difficulty in locating the SSH public key for upload to the HPC Portal.

## Conclusion
The user needs to understand the default location of the SSH public key and how to retrieve its content for upload to the HPC Portal. The provided commands and documentation should resolve the issue.
---

### 2024102142003306_Updating%20the%20ssh%20key%3F.md
# Ticket 2024102142003306

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject: Updating the SSH Key

### Keywords:
- SSH Key
- HPC Portal
- Email Address
- Account Activation
- SSO-Identity

### Summary:
A user switched to a new laptop and couldn't remember the passkey for their SSH key. They attempted to upload a new key via the HPC Portal but encountered issues due to multiple email addresses being used for login.

### Root Cause:
- User had multiple email addresses associated with the HPC Portal.
- The user's primary account was linked to an INAF email address, but they attempted to log in with a UNI-Heidelberg email address.

### Solution:
- The user was advised to log in with their INAF email address, which was already set up properly.
- The user successfully logged in with the INAF email address and uploaded a new SSH key.

### General Learnings:
- Users can upload multiple SSH keys.
- It is important to use the correct email address associated with the HPC Portal account.
- Accounts may take time to be activated after confirmation.
- Logging in with the wrong SSO-account can create confusion and empty accounts.

### Actions Taken:
- HPC Admins guided the user to log in with the correct email address.
- The user successfully logged in and uploaded a new SSH key.
- The user was informed about the potential recreation of empty accounts if logging in with the wrong SSO-account.
```
---

### 2024031142000771_Migration%20of%20slcl%20HPC%20accounts%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20mandato.md
# Ticket 2024031142000771

 # HPC Support Ticket: Migration of HPC Accounts to New Portal / SSH Keys Mandatory

## Keywords
- HPC account migration
- SSH keys
- HPC portal
- IdM portal
- Single Sign-On (SSO)
- SSH key types (RSA, ECDSA, ED25519)
- Usage statistics
- ClusterCockpit
- Jupyterhub

## Summary
The HPC services at FAU are migrating existing HPC accounts to a new online HPC portal. This migration involves several changes, including the mandatory use of SSH keys for accessing HPC systems and the introduction of a new portal for managing HPC accounts.

## Key Points to Learn
- **New HPC Portal**: Accessible at [https://portal.hpc.fau.de](https://portal.hpc.fau.de). Login using Single Sign-On (SSO) with IdM credentials.
- **SSH Keys Mandatory**: From the end of March, access to HPC systems will require SSH keys. Accepted types are RSA (4096 bits), ECDSA (512 bits), and ED25519.
- **SSH Key Upload**: Generate SSH key pairs with a passphrase and upload the public key to the HPC portal. It may take up to two hours for all HPC systems to recognize the updated keys.
- **Documentation and FAQs**: Available at [SSH Documentation](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/) and [FAQs](https://hpc.fau.de/faqs/#ID-230).
- **Windows Users**: Recommended to use OpenSSH built into Windows (Power)Shell or MobaXterm instead of Putty.
- **Account Validity**: The HPC portal will be the sole source for account validity starting from the end of February. Ignore expiration messages from the IdM portal.
- **Usage Statistics**: Viewable in the HPC portal. PIs and project managers will also have access to these statistics.
- **ClusterCockpit and Jupyterhub**: Access via Single Sign-On links from within the HPC portal.

## Root Cause of the Problem
- The migration process requires users to adapt to new authentication methods and portal management.

## Solution
- Users need to generate and upload SSH keys to the new HPC portal.
- Access the HPC portal using SSO with IdM credentials.
- Use the HPC portal for account management and to view usage statistics.
- For ClusterCockpit and Jupyterhub, use the Single Sign-On links provided within the HPC portal.

## Additional Notes
- The HPC portal and IdM portal are completely decoupled.
- For account validity updates, contact the PI or project manager instead of RRZE.
- New HPC accounts for colleagues or students should also be requested through the PI or project manager.
---

### 2022091242001046_Anpassungen%20auf%20Meggie.md
# Ticket 2022091242001046

 # HPC-Support Ticket Conversation: Anpassungen auf Meggie

## Summary
- **Issue**: Users unable to connect to Meggie via SSH due to host key verification failure.
- **Root Cause**: ECDSA host key for meggie.rrze.fau.de has changed.
- **Solution**: Remove the offending key from `/etc/ssh/ssh_known_hosts` and add the correct host key.

## Detailed Conversation

### User Report
- **Problem**: Users unable to connect to Meggie via SSH.
- **Error Message**:
  ```
  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
  @       WARNING: POSSIBLE DNS SPOOFING DETECTED!          @
  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
  The ECDSA host key for meggie.rrze.fau.de has changed,
  and the key for the corresponding IP address 2001:638:a000:3924::11
  is unchanged. This could either mean that
  DNS SPOOFING is happening or the IP address for the host
  and its host key have changed at the same time.
  Offending key for IP in /etc/ssh/ssh_known_hosts:7132
  remove with:
  ssh-keygen -f "/etc/ssh/ssh_known_hosts" -R "2001:638:a000:3924::11"
  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
  @    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @
  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
  IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
  Someone could be eavesdropping on you right now (man-in-the-middle attack)!
  It is also possible that a host key has just been changed.
  The fingerprint for the ECDSA key sent by the remote host is
  SHA256:OidKJlJ3KNbXlJpRUiZNoKp8vephfTbhQepA7Zmn8p4.
  Please contact your system administrator.
  Add correct host key in /home/hpc/fhn0/fhn001/.ssh/known_hosts to get rid of this message.
  Offending RSA key in /etc/ssh/ssh_known_hosts:7131
  remove with:
  ssh-keygen -f "/etc/ssh/ssh_known_hosts" -R "meggie.rrze.fau.de"
  ECDSA host key for meggie.rrze.fau.de has changed and you have requested strict checking.
  Host key verification failed.
  ```

### HPC Admin Response
- **Action**: HPC Admins updated the module file and provided a solution for the SSH issue.
- **Solution**:
  ```
  ssh-keygen -f "/etc/ssh/ssh_known_hosts" -R "2001:638:a000:3924::11"
  ssh-keygen -f "/etc/ssh/ssh_known_hosts" -R "meggie.rrze.fau.de"
  ```

### Additional Issues
- **OpenFOAM Module**: Error loading OpenFOAM module due to missing OpenMPI module.
- **SLURM Configuration**: Issues with CPU allocation leading to double allocation of CPUs.

### Solutions Provided
- **OpenFOAM Module**: Updated the module file to include the correct OpenMPI version.
- **SLURM Configuration**:
  - Suggested checking `cgroup.conf` for `ConstrainCores=yes` and `ConstrainRAMSpace=yes`.
  - Provided steps to verify SLURM job allocation using `/proc/self/cgroup` and `/sys/fs/cgroup/cpuset/.../cpuset.cpus`.
  - Recommended reviewing SLURM configuration and ensuring proper restart of SLURM services after changes.

## Conclusion
The main issue of host key verification failure was resolved by removing the offending keys and adding the correct host key. Additional issues with OpenFOAM and SLURM configuration were addressed with specific solutions provided by the HPC Admins.
---

### 2019090942002003_connection%20to%20cluster%20emmy%20refused.md
# Ticket 2019090942002003

 # HPC Support Ticket: Connection to Cluster Refused

## Keywords
- SSH Connection
- Connection Refused
- Virtual Machine
- Cluster Access
- Account Validity

## Summary
A user reported issues connecting to the HPC cluster "emmy" from different locations using an SSH command. The error message received was "ssh: connect to host emmy.rrze.fau.de port 53741: Connection refused."

## Root Cause
- The user attempted to connect to the cluster from a Linux virtual machine on a laptop in the main library and later from the computer room of LTM.
- The error message indicates a connection refused issue, which could be due to network restrictions, firewall settings, or incorrect SSH configuration.

## Troubleshooting Steps
1. **Verify Account Validity**: Ensure the user's HPC account is active and valid.
2. **Check Network Connectivity**: Confirm that the network from which the user is attempting to connect allows SSH traffic to the cluster.
3. **Firewall Settings**: Ensure that the firewall settings on the user's virtual machine and the network do not block the required port.
4. **SSH Configuration**: Verify that the SSH command and configuration are correct.

## Solution
- The HPC Admin's response suggests a user error ("klingt stark nach Problem zwischen Tastatur und Stuhl"), indicating that the issue might be related to user input or configuration rather than a technical problem with the cluster.
- Further investigation is needed to determine the exact cause and provide a specific solution.

## General Learning
- Always verify account validity when troubleshooting connection issues.
- Network restrictions and firewall settings can impact SSH connections.
- Ensure correct SSH configuration and command usage.
- Consider user-related issues when diagnosing connection problems.

## Next Steps
- If the issue persists, gather more details about the user's network environment and SSH configuration.
- Provide specific instructions for configuring the SSH client and troubleshooting network connectivity.
---

### 2024081642002027_Problem%20accessing%20Fritz.md
# Ticket 2024081642002027

 # HPC Support Ticket: Problem Accessing Fritz

## Keywords
- SSH
- ProxyJump
- Public Key Authentication
- Known Hosts
- Hanging Connection

## Summary
A user reported issues with SSH access to the `fritz.nhr.fau.de` server. The connection would hang without prompting for a password. The user provided detailed SSH debug output for analysis.

## Root Cause
The SSH connection to `fritz.nhr.fau.de` via `csnhr.nhr.fau.de` was hanging during the authentication process. The debug output indicated successful authentication to `csnhr.nhr.fau.de` but no further progress in establishing the connection to `fritz.nhr.fau.de`.

## Debug Output Analysis
- Successful authentication to `csnhr.nhr.fau.de` using public key.
- Connection to `fritz.nhr.fau.de` initiated but no response received.
- No errors reported in the SSH debug output beyond the initial connection setup.

## Possible Solutions
1. **Check Server Status**: Verify that `fritz.nhr.fau.de` is operational and not experiencing downtime or maintenance.
2. **Network Issues**: Investigate potential network issues between `csnhr.nhr.fau.de` and `fritz.nhr.fau.de`.
3. **SSH Configuration**: Ensure that the SSH configuration on `fritz.nhr.fau.de` is correctly set up to accept connections from `csnhr.nhr.fau.de`.
4. **Firewall Rules**: Check for any firewall rules that might be blocking the connection.
5. **Logs**: Review server logs on `fritz.nhr.fau.de` for any errors or warnings related to SSH connections.

## Next Steps
- **HPC Admins**: Investigate the status of `fritz.nhr.fau.de` and check for any network or configuration issues.
- **2nd Level Support**: Assist in reviewing server logs and network diagnostics.

## Conclusion
The issue appears to be related to the connection between `csnhr.nhr.fau.de` and `fritz.nhr.fau.de`. Further investigation is required to identify the exact cause and resolve the problem.

---

This documentation can be used as a reference for similar issues in the future.
---

### 2024030142003312_Unable%20to%20access%20hpc%20after%20new%20ssh%20setup.md
# Ticket 2024030142003312

 # HPC-Support Ticket: Unable to Access HPC After New SSH Setup

## Subject
Unable to access HPC after new SSH setup.

## User Issue
- User created SSH private and public keys and uploaded the public key to the HPC portal.
- Unable to access HPC the next day.
- Provided SSH config file and connection logs.

## SSH Config File
```plaintext
Host tinyx.nhr.fau.de
    HostName tinyx.nhr.fau.de
    User iwi5174h
    ProxyJump iwi5174h@csnhr.nhr.fau.de
    IdentityFile C:\Users\MSI-PC\.ssh\keys_for_hpc
    IdentitiesOnly yes
    PasswordAuthentication no
    PreferredAuthentications publickey
    ForwardX11 no
    ForwardX11Trusted no
```

## Connection Logs
- Logs indicate multiple attempts to find the SSH executable.
- Error messages include `Permission denied (publickey)` and `Connection closed by remote host`.

## HPC Admin Response
- Confirmed that the SSH private key file `keys_for_hpc` was not found.
- Suggested using default filenames for SSH keys and configuring without a config file initially.

## Root Cause
- SSH private key file `keys_for_hpc` not found.
- Path formatting issues in the SSH config file.

## Solution
- Move existing key files and config file to another location.
- Generate new SSH keys using default filenames.
- Upload the new public key to the HPC portal.
- Wait for the key to be activated.
- Attempt login using the following commands:
  ```sh
  ssh -v -J iwi5174h@csnhr.nhr.fau.de iwi5174h@tinyx.nhr.fau.de
  ssh -v -J iwi5174h@cshpc.rrze.fau.de iwi5174h@tinyx.nhr.fau.de
  ```
- If successful, reconfigure the SSH config file.

## Keywords
- SSH key
- Public key
- Private key
- SSH config file
- Permission denied
- Connection closed
- ProxyJump
- IdentityFile
- PasswordAuthentication
- PreferredAuthentications
- ForwardX11

## General Learnings
- Ensure SSH keys are generated with default filenames.
- Verify the path and filename of the SSH private key in the config file.
- Use verbose SSH commands to diagnose connection issues.
- Move existing configuration files and keys to avoid conflicts during troubleshooting.
---

### 2021050742000441_connection.md
# Ticket 2021050742000441

 ```markdown
# HPC Support Ticket: Connection Issue

## Keywords
- Connection issue
- SSH permissions
- Time Machine backup
- Disk Utility
- macOS

## Problem Description
The user encountered an issue connecting to the HPC system after reinstalling their laptop. The error message indicated a problem with the permissions of the `.ssh/config` file.

## Root Cause
The root cause of the problem was incorrect permissions on the `.ssh/config` file, likely due to restoring the user from a Time Machine backup on macOS.

## Solution
The HPC Admin suggested using the "repair permissions" option in Disk Utility to fix the permissions issue. The user confirmed that this solution resolved the problem.

## General Learnings
- Permissions issues can occur when restoring from a Time Machine backup on macOS.
- The "repair permissions" option in Disk Utility can be used to fix such issues.
- Incorrect permissions on SSH configuration files can prevent successful connections to HPC systems.
```
---

### 2023051242001641_Fritz%3A%20ssh%20connectivity%20issue.md
# Ticket 2023051242001641

 # HPC Support Ticket: SSH Connectivity Issue

## Keywords
- SSH connectivity
- Permission denied
- Public key authentication
- Username error
- Key distribution delay

## Problem Description
- User unable to connect to HPC cluster via SSH.
- Error message: `Permission denied (publickey,gssapi-keyex,gssapi-with-mic)`.
- Incorrect username used in SSH command.
- Recent public key upload, waiting for distribution.

## Root Cause
- Incorrect username in SSH command.
- Delay in public key distribution across clusters.

## Troubleshooting Steps
1. **Verify Username**: Ensure the correct username is used in the SSH command.
   - Incorrect: `b146dc12h`
   - Correct: `b146dc12`
2. **Wait for Key Distribution**: After uploading a new public key, allow a few hours for distribution across all clusters.

## Solution
- Use the correct username in the SSH command.
- Wait for the public key to be distributed across all clusters, which may take a few hours.

## Follow-up
- If the issue persists after using the correct username and waiting for key distribution, further investigation is needed to ensure the public key is properly uploaded and configured.

## Notes
- Users may attempt to ping the cluster using the incorrect format (e.g., `ping b146dc12@fritz.nhr.fau.de`), which will result in a `Name or service not known` error.
- Ensure users are aware of the delay in key distribution after uploading a new public key.
---

### 2023030142003583_Umstellung%20der%20HPC-Accounts%20der%20HS-Coburg%20am%20RRZE%20_%20NHR%40FAU%20-%20corz042h.md
# Ticket 2023030142003583

 # HPC-Support Ticket Conversation Analysis

## Keywords
- HPC Accounts
- HS-Coburg
- RRZE / NHR@FAU
- HPC-Portal
- DNF-AAI/eduGAIN
- SSH-PublicKeys
- SSH-Key
- Password
- Hochschul-Emailadresse
- Windows PowerShell
- Windows Subsystem für Linux
- mobaXtern
- OpenSSH
- Putty
- JumpHost-Feature
- FAQ

## Summary
The HPC-Support Ticket conversation revolves around the transition of HPC accounts from a paper-based system to a new electronic HPC-Portal. Users are required to log in via DNF-AAI/eduGAIN to link their existing accounts to their identities. SSH-PublicKeys will be used for access, and password-based access will be discontinued.

## Root Cause of the Problem
- The user's email address (sebstian.franz@cat-racing.de) is no longer valid, causing email delivery failures.

## Solution
- The HPC Admin attempted to reach the user via an alternative method to inform them about the transition process and the need to log in to the HPC-Portal.

## General Learnings
- **Transition to Electronic Portal**: The management of HPC accounts is moving from a paper-based system to an electronic HPC-Portal.
- **SSH-Key Access**: Access to HPC systems will be via SSH-Key only, with password access being discontinued by the end of March.
- **Email Communication**: Future HPC-related emails will be sent to the user's Hochschul-Emailadresse instead of their previous email address.
- **SSH Tools**: Recommendations for Windows users include using Windows PowerShell, Windows Subsystem for Linux, or mobaXtern, which contain OpenSSH as an SSH-Client.
- **Account Deactivation**: Accounts not linked to a person by the end of March will be deactivated, and associated data will be deleted after three months.

## References
- [HPC-Portal Usage](https://hpc.fau.de/systems-services/documentation-instructions/getting-started/nhrfau-hpc-portal-usage/)
- [SSH Access](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/)
- [FAQ](https://hpc.fau.de/faqs/#innerID-13183)
- [mobaXtern](https://mobaxterm.mobatek.net/)
---

### 2024051142000231_Fehlende%20ben%C3%83%C2%B6tigte%20Attribute%20in%20SSO-Antwort.md
# Ticket 2024051142000231

 # HPC-Support Ticket: Missing Required Attributes in SSO Response

## Keywords
- SSO (Single Sign-On)
- HPC Portal
- Attribute Missing
- FU Berlin
- DFN
- eduGAIN

## Problem Description
Users encountered issues logging into the HPC Portal due to missing required attributes in the SSO response.

## Root Cause
The SSO response from the user's institution (FU Berlin) did not include the necessary attributes required by the HPC Portal.

## Solution
Users were advised to contact the responsible department at FU Berlin to ensure the required attributes are transmitted. The email address for the inquiry should be found through the directories provided by DFN or eduGAIN.

## General Learnings
- Ensure that SSO responses include all required attributes for successful login to the HPC Portal.
- Users should contact their institution's IT department to resolve attribute-related issues.
- Use DFN or eduGAIN directories to find the appropriate contact information for attribute-related inquiries.

## Next Steps for Support
- Verify that the user has contacted their institution's IT department.
- Follow up with the user to ensure the issue has been resolved.
- Document the specific attributes required for future reference.

## Roles Involved
- **HPC Admins**: Thomas Gruber
- **2nd Level Support Team**: Not directly involved in this ticket.
- **Head of the Datacenter**: Gerhard Wellein
- **Training and Support Group Leader**: Georg Hager
- **NHR Rechenzeit Support**: Harald Lanig
- **Software and Tools Developer**: Jan Eitzinger, Gruber

## Relevant Links
- [HPC Portal](https://portal.hpc.fau.de/)
- [FAU HPC](https://hpc.fau.de/)

## Contact
- **HPC Support Email**: support-hpc@fau.de
---

### 2024111342003267_Re%3A%20New%20invitation%20for%20%22Vorlesung%20Rechnerarchitektur%22%20waiting%20at%20portal.hpc.fa.md
# Ticket 2024111342003267

 # HPC Support Ticket Analysis

## Subject
Re: New invitation for "Vorlesung Rechnerarchitektur" waiting at portal.hpc.fau.de

## Keywords
- HPC Portal
- Invitation
- SSH Public Key
- SSO Login
- IdM Credentials
- Project Access

## Problem
- User did not receive an invitation to the project "Vorlesung Rechnerarchitektur."

## Root Cause
- Invitations occasionally go missing in the HPC Portal.

## Solution
- User was advised to contact the course administrators for a new invitation.
- HPC Admin noted that invitations sometimes do not reach all intended recipients.

## General Learnings
- **Invitation Issues**: Occasionally, invitations to HPC projects do not reach all users.
- **Contact Course Administrators**: Users should contact the course administrators for missing invitations.
- **SSH Key Upload**: After accepting the invitation, users need to upload an SSH public key to their account.
- **Documentation**: Further information can be found at the HPC Portal documentation.

## Actions Taken
- HPC Admin advised the user to contact the course administrators.
- HPC Admin noted the recurring issue with missing invitations.

## Future Reference
- For similar issues, advise users to contact the relevant course administrators.
- Be aware of the potential for missing invitations in the HPC Portal.

---

This documentation can be used to address similar issues in the future, ensuring that users are directed to the appropriate course administrators for missing invitations.
---

### 2022101042005231_Question%20about%20Login%20NHR%20Learning%20Platform.md
# Ticket 2022101042005231

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject: Question about Login NHR Learning Platform

### Keywords:
- Login issue
- NHR Learning Platform
- Email error
- Invisible character
- Moodle system

### Root Cause:
- Invisible character after the "@" in the email address causing login failure.

### Solution:
- HPC Admin corrected the user record in the Moodle system.

### General Learnings:
- Invisible characters in email addresses can cause login issues.
- Correcting the user record in the Moodle system can resolve such issues.
- Always check for hidden characters when troubleshooting email-related login problems.
```
---

### 2022061742000954_Problem%20logging%20in%20https%3A__portal.hpc.fau.de_%20-%20b118bb11%20-%20tumu.md
# Ticket 2022061742000954

 # HPC Support Ticket: Problem Logging In via SSO

## Keywords
- SSO Login
- Account Expiration
- DFN-AAI + eduGAIN
- Data Transfer
- SSH Keys

## Summary
A user from Technical University of Munich (TUM) encountered issues logging into the HPC portal using their FAU account. The root cause was the expiration of their previous account.

## Root Cause
- The user's previous account (`ro98myry`) had expired at the end of May.
- The user attempted to log in using their FAU IDM account, which is no longer required for the HPC portal.

## Solution
- The user was instructed to log in via "Another institution (DFN-AAI + eduGAIN)" and select TUM.
- A new account (`b118bb11`) was created, and the user was informed about the need to transfer old data to the new directory.
- The user was advised to use SSH keys for login to the HPC systems and provided with instructions on how to upload their SSH public key through the portal.

## Additional Information
- The new account will not work on TinyGPU but only on Alex.
- The HPC Admins offered assistance with transferring existing data from the old account and adapting job scripts if needed.
- The user was informed about the benefits of using Alex nodes for Gromacs due to the availability of 16 cores per requested GPU.

## Follow-Up
- The HPC Admins will notify the user once the new file server for `$WORK` is available for data transfer.
- The user can refer to the provided documentation for details on SSH key creation and portal usage.

## General Learning
- Users should be aware of account expiration dates and the need to use their home institution's account for logging into the HPC portal.
- SSH keys are required for login to the HPC systems, and users should follow the provided instructions for uploading their public keys.
- The HPC Admins can assist with data transfer and job script adaptation as needed.
---

### 2024012242002993_problem%20with%20login%20to%20cshpc%20-%20nfcc013h.md
# Ticket 2024012242002993

 # HPC Support Ticket Analysis: Login Issue for User `nfcc013h`

## Keywords
- Login issue
- SSH problems
- IDM-Account
- eduGAIN
- HPC-Portal
- SSO-Kennung
- FAU-IdM-Kennungen
- DFN-AAI/eduGAIN-Verbund
- Gastwissenschaftler

## Summary
A user (`nfcc013h`) is experiencing issues logging into the HPC system. The user has not attempted to log in since November, and there are potential issues with the user's IDM-Account and home institution not being part of eduGAIN.

## Root Cause
- The user's IDM-Account (`nfcc013h`) has expired.
- The user's home institution (Nagoya Institute of Technology) is not part of the eduGAIN federation.

## Steps Taken
1. **Initial Investigation**: HPC Admins found no login attempts since November.
2. **SSH Debugging**: Recommended the user to follow the SSH debugging guide.
3. **IDM-Account Check**: Confirmed that the user's IDM-Account has expired.
4. **eduGAIN Check**: Verified that the user's home institution is not part of eduGAIN.

## Solution
- **IDM-Account Renewal**: The user needs to renew their IDM-Account following the guidelines provided in the link.
- **eduGAIN Inclusion**: The user's home institution needs to be included in the eduGAIN federation. The user can contact the technical contact at their institution or the GakuNin Federation (JP) operator for further steps.

## Additional Notes
- The user requested a phone call to resolve the issue more efficiently.
- HPC Admins provided information on the new process for guest researchers at FAU.
- The user was informed about the availability of student helpers at the RRZE-Servicetheke for telephonic support.

## Conclusion
The user needs to renew their IDM-Account and ensure their home institution is part of the eduGAIN federation to resolve the login issue. If the institution cannot be included in eduGAIN quickly, the user may need to obtain a FAU-IdM-Account.
---

### 2024041242002452_New%20HPC%20user.md
# Ticket 2024041242002452

 # HPC Support Ticket: New HPC User Access

## Keywords
- HPC Portal
- Management Tab
- PI (Principal Investigator)
- Technical Contact
- Access Request
- Invitation Process

## Problem
- User unclear about the application process for new HPC access.
- Confusion regarding the requirement for an invitation to be sent by the PI or technical contact.

## Root Cause
- Lack of understanding about the new system's invitation process.

## Solution
- **HPC Admin** instructed the user to log in to the HPC portal and navigate to the management tab.
- Provided a link to the documentation: [HPC Portal Management Tab](https://doc.nhr.fau.de/hpc-portal/#the-management-tab-visible-only-for-pis-and-technical-contacts)

## Outcome
- User successfully set up the new HPC access.

## General Learning
- The invitation process for new HPC users requires the PI or technical contact to log in to the HPC portal and use the management tab.
- Documentation and support links are crucial for guiding users through new processes.

## Future Reference
- For similar issues, direct users to the HPC portal and provide relevant documentation links.
- Ensure users understand the role of the PI or technical contact in the invitation process.
---

### 2024022942003165_Idm%20HPC%20service%20system%20access%3F.md
# Ticket 2024022942003165

 ```markdown
# HPC-Support Ticket: Idm HPC Service System Access

## Keywords
- Idm HPC Access
- SSH Keys
- HPC Portal
- Account Expiration
- Migration

## Summary
Users received a notification that their HPC access was expiring, causing concern about losing access before an important deadline. The issue was related to the migration to a new HPC portal and the mandatory use of SSH keys.

## Root Cause
- The Idm portal sent automatic messages about HPC service expiration, which were incorrect due to the migration to the new HPC portal.
- Some users had not yet set up their SSH keys, which were required for continued access.

## Solution
- Users were informed to ignore the Idm portal expiration messages.
- Users were instructed to generate and upload SSH keys to the HPC portal.
- Documentation and FAQs were provided for setting up SSH keys.
- The HPC portal became the sole source for account validity, decoupled from the Idm portal.

## General Learnings
- During migrations, ensure clear communication about changes in access methods and account validity.
- Provide detailed instructions and support for setting up new authentication methods (e.g., SSH keys).
- Decoupling portals can lead to confusion; ensure users are aware of which portal to refer to for account information.
```
---

### 2023102742002192_Account%20Unavailable%20for%20HPC%3A%20MuCoSIM.md
# Ticket 2023102742002192

 # HPC Support Ticket Analysis: Account Unavailable for HPC: MuCoSIM

## Keywords
- Account Activation
- SSH Keys
- MuCoSIM Project
- Server Description

## Root Cause of the Problem
- User received an invite for the MuCoSIM project and uploaded SSH keys, but the account is not yet active.

## What Can Be Learned
- Ensure that the account activation process is completed after SSH keys are uploaded.
- Verify that the server description provides sufficient information for troubleshooting.

## Solution
- HPC Admins should check the account activation status and ensure all necessary steps have been completed.
- Verify that the SSH keys are correctly uploaded and associated with the user's account.

## Actions Taken
- User provided the server description for further investigation.
- HPC Admins need to review the account activation process and SSH key upload.

## Next Steps
- HPC Admins should activate the user's account if all requirements are met.
- If the issue persists, involve the 2nd Level Support team for further troubleshooting.

## Notes
- Ensure clear communication with the user regarding the account activation process and any additional steps required.
- Document any common issues related to account activation for future reference.
---

### 2023031442002051_Keine%20Anmeldung%20%C3%83%C2%BCber%20SSH%20mehr%20m%C3%83%C2%B6glich.md
# Ticket 2023031442002051

 ```markdown
# HPC Support Ticket: SSH Login Issue

## Keywords
- SSH login issue
- Locale settings warning
- /home/woody filesystem
- Verbose output

## Problem Description
- User unable to log in via SSH (both VS Code and terminal).
- Terminal shows locale settings warning and falls back to a fallback locale.
- User can access home directory but not the /home/woody filesystem.

## Root Cause
- Possible issue with the /home/woody filesystem.

## Solution
- HPC Admin identified a problem with the /home/woody filesystem.
- User was advised to wait for the filesystem issue to be resolved.
- HPC Admin requested verbose output of the SSH command for further diagnosis if the issue persists.

## What to Learn
- Locale settings warnings can indicate issues with SSH login.
- Filesystem problems can affect SSH access to specific directories.
- Verbose output (`-v` flag) is useful for diagnosing SSH issues.
```
---

### 2022060742000222_Re%3A%20Andreas%20Waechter%2C%20Alex%20Account%3F.md
# Ticket 2022060742000222

 ```markdown
# HPC Support Ticket Conversation Analysis

## Key Points Learned

1. **SSO/SAML Configuration**: The main issue revolved around configuring the SSO/SAML attributes for the Northwestern University's IdP to work with the FAU HPC portal.
2. **NameID Attribute**: The `NameID` attribute was crucial for the SSO login to function correctly. Initially, it was not included in the list of required attributes.
3. **Persistent Format**: The persistent format for the `NameID` attribute was necessary for the configuration to work.
4. **Collaboration**: The issue was resolved through collaboration between the user's IT department and the FAU HPC support team, with assistance from external SAML specialists.
5. **Alternative Solutions**: In case of delays or issues with the SSO configuration, alternative methods such as classical IdM accounts were discussed but deemed less efficient.

## Root Cause of the Problem

The root cause of the problem was the missing `NameID` attribute in the SSO/SAML configuration, which was required for the login process to complete successfully. Additionally, the format of the `NameID` attribute needed to be set to persistent.

## Solution

The solution involved:
1. **Identifying the Missing Attribute**: The FAU HPC support team identified the missing `NameID` attribute and its required format.
2. **Collaboration with IT**: The user's IT department was informed about the necessary changes and worked on implementing them.
3. **External Assistance**: Specialists from Unicon were consulted to provide additional guidance on configuring the SAML attributes correctly.
4. **Testing and Verification**: The changes were tested and verified to ensure the login process worked as expected.

## Documentation for Future Reference

For future reference, ensure that the `NameID` attribute is included in the SSO/SAML configuration and set to the persistent format. If issues persist, consult with SAML specialists and verify that all required attributes are correctly configured in the IdP.

```

This concise report can be used as a reference for solving similar issues in the future.
---

### 2025010742000851_Regarding%20account%20access.md
# Ticket 2025010742000851

 # HPC Support Ticket: Account Access Issue

## Keywords
- Account access
- Email ID expiration
- SSH key pair
- HPC portal
- SSO-Identität umhängen

## Problem
- User unable to access HPC portal due to expired email ID.
- Cannot create new SSH keys for existing user account.
- New account created but file access sharing not working.

## Root Cause
- User's email ID associated with HPC account has expired.
- New email ID not linked to the existing HPC user account.

## Solution
- HPC Admin recommended changing the SSO identity of the existing account to the new email ID.
- Verification of both email IDs was required from the user's supervisor.
- Once verified, the old account was updated with the new email ID.
- The new account was set to expire as it was no longer required.

## General Learnings
- Linking a new email ID to an existing HPC account requires verification.
- Updating the SSO identity is preferred over creating a new account.
- Expired email IDs can cause access issues to HPC portals and SSH key creation.
---

### 2023053042004032_Migration%20of%20nfcc%20HPC%20accounts%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20mandato.md
# Ticket 2023053042004032

 # HPC Support Ticket: Migration of HPC Accounts to New Portal / SSH Keys Mandatory

## Keywords
- HPC account migration
- SSH keys
- HPC portal
- IdM portal
- Single Sign-On (SSO)
- SSH key types (RSA, ECDSA, ED25519)
- Usage statistics
- ClusterCockpit
- Jupyterhub

## Summary
The HPC services at FAU are migrating user accounts from the IdM portal to a new online HPC portal. This migration includes changes in authentication methods and account management processes.

## Key Points to Learn
- **New HPC Portal**: Accessible at [https://portal.hpc.fau.de](https://portal.hpc.fau.de). Login using IdM credentials via Single Sign-On (SSO).
- **SSH Keys Mandatory**: By mid-June, access to HPC systems will require SSH keys. Accepted types are RSA (4096 bits), ECDSA (512 bits), and ED25519.
- **SSH Key Upload**: Generate SSH key pairs with a passphrase and upload the public key to the HPC portal. It may take up to two hours for updates to propagate.
- **Documentation**: Refer to [SSH documentation](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/) and [FAQs](https://hpc.fau.de/faqs/#ID-230) for assistance.
- **Windows Users**: Recommended to use OpenSSH built into Windows (Power)Shell or MobaXterm instead of Putty.
- **Account Validity**: The HPC portal will be the sole source for account validity. Ignore expiration notices from the IdM portal.
- **Account Management**: Contact the PI or project manager to update account validity or request new accounts.
- **Usage Statistics**: Viewable in the HPC portal by users, PIs, and project managers.
- **ClusterCockpit and Jupyterhub**: Access via Single Sign-On links within the HPC portal.

## Root Cause of the Problem
- Migration process requires users to adapt to new authentication methods and account management procedures.

## Solution
- Follow the instructions provided in the email to generate and upload SSH keys.
- Use the new HPC portal for account management and accessing services.
- Refer to the provided documentation and FAQs for detailed guidance.

## Additional Notes
- The IdM portal and the new HPC portal are completely decoupled.
- Ensure that all users are aware of the changes and the new procedures for account management and accessing services.
---

### 2023030142003501_Umstellung%20der%20HPC-Accounts%20der%20HS-Coburg%20am%20RRZE%20_%20NHR%40FAU%20-%20corz002h.md
# Ticket 2023030142003501

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject
Umstellung der HPC-Accounts der HS-Coburg am RRZE / NHR@FAU - corz002h

## Keywords
- HPC-Accounts
- HS-Coburg
- RRZE / NHR@FAU
- DFN-AAI/eduGAIN
- HPC-Portal
- SSH-PublicKeys
- SSH-Key
- Passwort
- Windows PowerShell
- Windows Subsystem für Linux
- mobaXtern
- OpenSSH
- Putty
- JumpHost-Feature
- Deaktivierung
- Datenlöschung

## Summary
The HPC accounts of HS-Coburg at RRZE / NHR@FAU are transitioning from a paper-based system to a new, fully electronic HPC-Portal. Users must log in via DFN-AAI/eduGAIN to continue using their accounts. SSH-PublicKeys will be required for access starting at the end of March.

## Root Cause of the Problem
- Certificate has expired.
- Users need to transition to the new HPC-Portal and upload SSH-PublicKeys.

## Solution
1. **Login to HPC-Portal**: Users must log in to the HPC-Portal using DFN-AAI/eduGAIN.
2. **Upload SSH-PublicKeys**: Users should upload their SSH-PublicKeys via the "User / Benutzer" tab in the HPC-Portal.
3. **Transition to SSH-Key Access**: Starting at the end of March, access will only be possible via SSH-Key, not password.

## Additional Information
- **HPC-Portal Documentation**: [HPC-Portal Usage](https://hpc.fau.de/systems-services/documentation-instructions/getting-started/nhrfau-hpc-portal-usage/)
- **SSH Documentation**: [SSH Secure Shell Access](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/)
- **FAQ**: [SSH Access FAQ](https://hpc.fau.de/faqs/#innerID-13183)
- **Recommended Tools for Windows Users**: Windows PowerShell, Windows Subsystem für Linux, mobaXtern

## Consequences of Non-Compliance
- Accounts not linked to a person by the end of March will be deactivated.
- Data associated with deactivated accounts will be deleted after 3 months.

## Contact Information
For further questions, users should contact the support team at HS-Coburg or the FAU.
```
---

### 2024022942002166_Re%3A%20Regarding%20HPC%20extension%20-%20iwb9005h.md
# Ticket 2024022942002166

 ```markdown
# HPC Support Ticket Conversation Analysis

## Key Points Learned

- **HPC Account Management**:
  - Accounts can be transferred to a new HPC portal.
  - SSH keys are mandatory for access.
  - Accounts can be extended by supervisors or managers.
  - Invitations for new accounts can be sent via the HPC portal.

- **Communication**:
  - Importance of clear and timely communication between students, supervisors, and HPC support.
  - Follow-up emails and reminders are crucial for resolving issues.

- **Troubleshooting**:
  - Common issues include account expiration and SSH key setup.
  - Solutions involve extending accounts and guiding users through the portal.

## Root Cause of Problems

- **Account Expiration**:
  - Students' HPC accounts were about to expire, causing potential disruption to their work.
  - Supervisors were not immediately available to extend the accounts due to exams or other commitments.

- **SSH Key Setup**:
  - Users needed to generate and upload SSH keys to access the HPC portal.
  - Instructions for SSH key setup were sent but not always followed correctly.

## Solutions

- **Account Extension**:
  - HPC admins extended accounts temporarily to allow data transfer and continued work.
  - Supervisors were guided through the process of sending invitations and extending accounts via the HPC portal.

- **SSH Key Setup**:
  - Users were reminded to follow the instructions for generating and uploading SSH keys.
  - HPC admins provided step-by-step guidance when necessary.

## Documentation for Future Reference

### Extending HPC Accounts

1. **Login to HPC Portal**:
   - Go to [HPC Portal](https://portal.hpc.fau.de/ui/management).

2. **Select Project**:
   - In the management tab, find the relevant project (e.g., iwb9101 for students).

3. **Send Invitation**:
   - Scroll to “Add new invitation”.
   - Send the invitation to the user's SSO email (e.g., @fau.de).

### Generating and Uploading SSH Keys

1. **Generate SSH Key**:
   - Follow the instructions provided in the email or system to generate an SSH key.

2. **Upload SSH Key**:
   - Login to the new HPC portal.
   - Upload the generated SSH key as per the instructions.

### Communication Tips

- **Clear and Timely Communication**:
  - Ensure all parties (students, supervisors, HPC support) are kept informed about account status and any issues.
  - Use follow-up emails to confirm actions and next steps.

- **Documentation**:
  - Keep records of all communications and actions taken for future reference.

By following these guidelines, HPC support can efficiently manage account extensions and SSH key setups, ensuring minimal disruption to users' work.
```
---

### 2022101342002086_HPC-Portal%20f%C3%83%C2%BCr%20alte%20Account.md
# Ticket 2022101342002086

 # HPC-Support Ticket Conversation Analysis

## Keywords
- HPC-Portal
- IDM
- SSH-Key
- Account Integration
- Password Authentication

## Summary
A user requested to integrate an old HPC account into the HPC-Portal associated with their IDM. The user's primary goal was to use SSH-key authentication instead of password authentication.

## Root Cause of the Problem
- The user wanted to switch from password authentication to SSH-key authentication.
- The user believed this was only possible through the HPC-Portal.

## Solution
- HPC Admins clarified that SSH-keys can be used with IDM-based HPC accounts by manually adding the public key to the `~/.ssh/authorized_keys` file.
- The HPC-Portal will eventually manage all FAU HPC accounts, but currently, it is only used for NHR projects due to missing service integrations.

## General Learnings
- SSH-key authentication is possible with IDM-based HPC accounts.
- The HPC-Portal will eventually replace password authentication for all FAU HPC accounts.
- Manual integration of old accounts into the HPC-Portal is technically possible but not currently advantageous.

## Action Items
- Users should manually add their SSH public keys to the `~/.ssh/authorized_keys` file for SSH-key authentication.
- HPC Admins will continue integrating services into the HPC-Portal for a smoother transition.
---

### 2024030142000413_Migration%20of%20wssa%20HPC%20accounts%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20mandato.md
# Ticket 2024030142000413

 # HPC Support Ticket Conversation Summary

## Subject
Migration of wssa HPC accounts to new HPC portal / SSH keys become mandatory

## Keywords
- HPC account migration
- SSH keys
- HPC portal
- Single Sign-On (SSO)
- IdM portal
- Password expiration
- Account validity
- ClusterCockpit
- Jupyterhub

## Key Points
- **Migration Process**: Existing HPC accounts are being migrated to a new online HPC portal.
- **Access Method**: From March 15th, access to HPC systems will be via SSH keys only.
- **SSH Key Types**: Accepted types are RSA (4096 bit), ECDSA (512 bit), and ED25519.
- **SSH Key Upload**: Users need to generate and upload SSH keys to the HPC portal.
- **Portal Access**: The new HPC portal can be accessed at [https://portal.hpc.fau.de](https://portal.hpc.fau.de) using IdM credentials.
- **Account Validity**: The HPC portal will be the sole source for account validity starting from the end of February.
- **Usage Statistics**: Users, PIs, and project managers can view usage statistics in the HPC portal.
- **ClusterCockpit and Jupyterhub**: Access these services via Single Sign-On links within the HPC portal.

## Root Cause of the Problem
- Users need to transition to the new HPC portal and set up SSH keys for continued access.

## Solution
- **Generate SSH Keys**: Users should generate SSH keys with the specified types and lengths.
- **Upload SSH Keys**: Upload the public SSH keys to the HPC portal.
- **Access Portal**: Log in to the new HPC portal using IdM credentials.
- **Ignore Expiration Emails**: Disregard automatic messages about HPC service expiration from the IdM portal.

## Additional Resources
- [SSH Secure Shell Access Documentation](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/)
- [FAQs](https://hpc.fau.de/faqs/#ID-230)

## Notes
- For Windows users, it is recommended to use OpenSSH built into the Windows (Power)Shell or MobaXterm instead of Putty.
- Contact the PI or project manager to update the validity of HPC accounts or to request new accounts.
---

### 2025012842000375_Password%20reset.md
# Ticket 2025012842000375

 ```markdown
# HPC Support Ticket: Password Reset

## Keywords
- Password reset
- SSH key
- Login issue
- HPC account
- Project details

## Problem
- **Root Cause**: User forgot their password and is unable to log in to the HPC system.

## Solution
- **Action Required**: User needs to create a new SSH key.
- **Instructions**: Detailed instructions for creating a new SSH key can be found at [SSH Command Line Instructions](https://doc.nhr.fau.de/access/ssh-command-line/).

## General Learnings
- Users should be directed to create a new SSH key when they forget their password.
- Provide users with a link to detailed instructions for creating SSH keys.
- Ensure users include their HPC account and project details in their support requests.
```
---

### 2022112842002431_Zugriff%20auf%20ANSYS%20_%20Star-CCM%2B%20Software%20an%20Fritz%20%26%20Alex%20m%C3%83%C2%B6glich%3F.md
# Ticket 2022112842002431

 # HPC-Support Ticket Conversation Summary

## Keywords
- SSH Login
- Public Key Authentication
- ANSYS
- Star-CCM+
- License Server
- Port Forwarding
- FAU HPC
- LRZ
- NHR

## General Learnings
- **SSH Key Format**: Ensure SSH keys are in the correct format (OpenSSH) before uploading to the FAU User Portal.
- **User Authentication**: Verify the correct username is used for SSH login.
- **License Server Access**: Understand the requirements for accessing external license servers, including port forwarding and network policies.
- **Documentation**: Refer to existing documentation for software-specific instructions and configurations.

## Root Causes and Solutions

### SSH Login Issues
- **Problem**: User unable to connect to FAU HPC gateway using SSH.
  - **Root Cause**: Incorrect SSH key format and incorrect username.
  - **Solution**: Convert SSH key to OpenSSH format and use the correct username (`b157be16`).

### ANSYS and Star-CCM+ Software Access
- **Problem**: User unable to access ANSYS and Star-CCM+ software directories.
  - **Root Cause**: Software directories are restricted.
  - **Solution**: Request access from HPC Admins and ensure proper licensing is in place.

### License Server Access
- **Problem**: User needs to access LRZ license server for ANSYS and Star-CCM+.
  - **Root Cause**: Ports need to be forwarded and license server needs to be configured.
  - **Solution**: Use port forwarding to access the LRZ license server. Refer to documentation for detailed instructions.

### Documentation Links
- **ANSYS**:
  - [ANSYS CFX](https://hpc.fau.de/systems-services/documentation-instructions/special-applications-and-tips-tricks/ansys-cfx/)
  - [ANSYS Fluent](https://hpc.fau.de/systems-services/documentation-instructions/special-applications-and-tips-tricks/ansys-fluent/)
  - [ANSYS Mechanical](https://hpc.fau.de/systems-services/documentation-instructions/special-applications-and-tips-tricks/ansys-mechanical/)
- **Star-CCM+**:
  - [Star-CCM+](https://hpc.fau.de/systems-services/documentation-instructions/special-applications-and-tips-tricks/star-ccm/)

## Additional Notes
- **Port Forwarding**: User-defined port forwarding can be set up similarly to accessing SVN, GIT, and Mercurial repositories on SuperMUC-NG.
- **ANSYS Fluent GPU Solver**: No specific experience with ANSYS Fluent GPU solver on FAU HPC systems.

This summary provides a concise overview of the issues and solutions discussed in the HPC-Support ticket conversation, serving as a reference for future support cases.
---

### 2024030342000179_Migration%20of%20mpwm%20HPC%20accounts%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20mandato.md
# Ticket 2024030342000179

 # HPC Support Ticket: Migration of HPC Accounts to New Portal / SSH Keys Mandatory

## Keywords
- HPC account migration
- SSH keys
- HPC portal
- IdM portal
- Single Sign-On (SSO)
- SSH key types (RSA, ECDSA, ED25519)
- Account validity
- Usage statistics
- ClusterCockpit
- Jupyterhub

## Summary
The HPC services at FAU are migrating existing HPC accounts to a new online HPC portal. This migration involves several changes, including the mandatory use of SSH keys for accessing HPC systems and the decoupling of the IdM portal from the new HPC portal.

## Key Points to Learn
- **HPC Portal Access**: The new HPC portal can be accessed at [https://portal.hpc.fau.de](https://portal.hpc.fau.de) using Single Sign-On (SSO) with IdM credentials.
- **SSH Keys Mandatory**: From March 15th, access to HPC systems will require SSH keys. Accepted types are RSA (4096 bits), ECDSA (512 bits), and ED25519.
- **SSH Key Upload**: Users must generate SSH key pairs with passphrases and upload the public keys to the HPC portal. It may take up to two hours for all HPC systems to recognize the updated keys.
- **Account Validity**: The new HPC portal is the sole source for account validity. Users should ignore expiration notices from the IdM portal.
- **Usage Statistics**: The HPC portal displays usage statistics for different HPC systems, which are also visible to PIs and project managers.
- **ClusterCockpit and Jupyterhub**: Access to ClusterCockpit and Jupyterhub should be done through Single Sign-On links within the HPC portal.

## Documentation and FAQs
- **SSH Documentation**: [https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/)
- **FAQs**: [https://hpc.fau.de/faqs/#ID-230](https://hpc.fau.de/faqs/#ID-230)

## Recommendations for Windows Users
- Use the OpenSSH built into the Windows (Power)Shell or MobaXterm instead of Putty.

## Contact Information
- **Support Email**: [support-hpc@fau.de](mailto:support-hpc@fau.de)
- **HPC Website**: [https://hpc.fau.de/](https://hpc.fau.de/)

## Root Cause and Solution
- **Root Cause**: Migration of HPC accounts to a new portal and the introduction of mandatory SSH keys.
- **Solution**: Users must generate and upload SSH keys to the new HPC portal and use Single Sign-On for accessing related services.
---

### 2023092842003852_Can%27t%20login%20via%20Fraunhofer%20SSO.md
# Ticket 2023092842003852

 # HPC Support Ticket: Can't Login via Fraunhofer SSO

## Keywords
- SSO Login
- Fraunhofer-Gesellschaft
- DFN-AAI
- Smartcard
- Authentication Error

## Problem Description
A student assistant at Fraunhofer IIS encountered an error while attempting to log in via SSO to the HPC Service. The error message indicated a potential issue with the Smartcard integration.

## Root Cause
The error occurred during the SSO login process at the HPC-Portal but was related to the Fraunhofer authentication infrastructure. The specific error message suggested a problem with the Smartcard integration.

## Solution
The HPC Admins advised the user to contact the technical/IT support team of Fraunhofer IIS, as the error was related to the Fraunhofer authentication infrastructure, which is outside the scope of the HPC support team.

## General Learning
- **Scope of Support**: HPC Admins can assist with issues related to the HPC Service but not with external authentication infrastructures.
- **Error Handling**: For authentication errors related to external institutions, users should contact their local IT support.
- **Communication**: Clear communication about the scope of support helps manage user expectations and ensures they seek assistance from the appropriate support teams.

## Next Steps
- If similar issues arise, direct users to their local IT support for authentication-related problems.
- Ensure users understand the distinction between HPC Service issues and external authentication issues.
---

### 2022091142000451_Meggie%3A%20Falscher%20Hostkey.md
# Ticket 2022091142000451

 # HPC Support Ticket: Host Key Mismatch

## Keywords
- Host key
- SSH
- Authentication failure
- Remote host identification changed
- `known_hosts`
- `ssh-keygen`

## Problem Description
The user encountered an SSH authentication failure due to a host key mismatch. The error message indicated that the remote host identification had changed, suggesting a possible man-in-the-middle attack or a legitimate host key change.

## Root Cause
The HPC system (Meggie) had been reinstalled, and the host key was not updated globally, leading to a mismatch with the user's known hosts.

## Solution
1. **User-side workaround**: The user could manually update the host key in their local `known_hosts` file.
   ```
   ssh-keygen -f "/home/hpc/iwi3/iwi3047h/.ssh/known_hosts" -R "meggie"
   ```
2. **Admin-side fix**: HPC Admins acknowledged the issue and planned to update the host keys globally on other systems the following week.

## General Learnings
- Host key changes can cause SSH authentication failures.
- Users can manually update their `known_hosts` file to resolve the issue temporarily.
- Global updates to host keys should be performed by HPC Admins to prevent widespread issues.
- Regular communication about system updates can help users anticipate and understand these issues.
---

### 2024111542002371_Requirements%20to%20access%20HPC.md
# Ticket 2024111542002371

 # HPC Support Ticket: Requirements to Access HPC

## Keywords
- HPC access requirements
- Tier3 HPC project
- Account creation
- SSH key
- HPC portal
- Invitation process

## Summary
A user inquired about the requirements to access HPC for their master thesis, specifically needing GPUs for time series analysis and evaluating ML and DL models. The user was unsure if there were any charges associated with using the system.

## Root Cause
- User needed access to HPC resources for their master thesis.
- User was unclear about the process and potential costs.

## Solution
- The user's professor already had a Tier3 HPC project.
- The professor could send an invitation to the user via the HPC portal.
- The user would then log into the HPC portal, accept the invitation, and upload an SSH key.
- The account would be created automatically and would be available within one day.

## Instructions
1. **Professor Invitation**: The professor logs into the HPC portal and sends an invitation to the user.
   - Documentation: [HPC Portal Management Tab](https://doc.nhr.fau.de/hpc-portal/#the-management-tab-visible-only-for-pis-and-technical-contacts)
2. **User Acceptance**: The user logs into the HPC portal, accepts the invitation, and uploads an SSH key.
   - Documentation: [Connecting to HPC Systems](https://doc.nhr.fau.de/getting_started/#connecting-to-hpc-systems)
3. **Account Creation**: The account is automatically created and will be available within one day.

## Notes
- No signed paper form is required from the user.
- The process involves the HPC portal for both the professor and the user.
- The user should be aware that it will take one day for the account to be available on the systems.

This documentation can be used to assist other users with similar inquiries about accessing HPC resources.
---

### 2024120442003264_WG%3A%20New%20invitation%20for%20%22Projektpartner%20Tier3-Grundversorgung%20Professur%20f%C3%83%C2%.md
# Ticket 2024120442003264

 # HPC-Support Ticket Conversation Analysis

## Subject
New invitation for "Projektpartner Tier3-Grundversorgung Professur für Hochleistungsrechnen (Prof. Wellein)" waiting at portal.hpc.fau.de

## Keywords
- HPC Portal
- SSO Login
- Email Invitation
- Export Control
- Nationality
- Gmail Account
- University Email
- IDM Credentials

## Problem Description
The user received an email invitation to a project but could not see the invitation in their university portal because the invitation was sent to a different email address (Gmail) than the one associated with their university account.

## Root Cause
- The user's IDM SSO login was associated with a Gmail address, not their university email.
- The HPC portal did not reflect the changes made to link the university email with the IDM SSO account.

## Solution
- The user was instructed to log in to the HPC portal using their IDM SSO credentials.
- The user's nationality was confirmed for export control purposes.
- The user eventually resolved the issue by updating their email settings and logging into the correct portal.

## General Learnings
- Ensure users log in to the correct HPC portal, not their university portal.
- Verify the email address associated with the user's IDM SSO account.
- Confirm the user's nationality for export control compliance.
- Provide clear instructions for accepting invitations and uploading SSH keys.

## Steps for Similar Issues
1. Instruct the user to log in to the HPC portal using their IDM SSO credentials.
2. Verify the email address associated with the user's IDM SSO account.
3. Confirm the user's nationality for export control purposes.
4. Provide clear instructions for accepting invitations and uploading SSH keys.

## Conclusion
The issue was resolved by ensuring the user logged into the correct portal and verifying their email settings. The user's nationality was also confirmed for export control compliance.
---

### 2016113042001573_SSH%20Agent%20forwarding.md
# Ticket 2016113042001573

 ```markdown
# SSH Agent Forwarding Issue

## Keywords
- SSH Agent Forwarding
- SSH Client Configuration
- Password Prompt
- HPC Frontends

## Problem Description
User encountered issues with SSH agent forwarding between HPC frontends (cshpc and woody). Direct SSH connections to each frontend worked with the agent, but subsequent connections between the frontends prompted for a password.

## Root Cause
The root cause was identified as a misconfiguration in the user's SSH client settings after a recent reinstallation.

## Solution
The user resolved the issue by correcting the SSH client configuration settings.

## Lessons Learned
- Ensure SSH client configurations are correctly set, especially after reinstallations.
- Verify SSH agent forwarding settings to avoid password prompts during multi-hop SSH connections.

## Actions Taken
- The ticket was closed as the user resolved the issue independently.
```
---

### 2020121642001581_Unable%20to%20Access%20Account.md
# Ticket 2020121642001581

 # HPC-Support Ticket: Unable to Access Account

## Subject
Unable to Access Account

## User Issue
- User unable to access account `iwsp027@emmy.rrze.fau.de` via SSH while connected to the university's VPN.
- Authentication methods attempted: publickey, gssapi-keyex, gssapi-with-mic, password.
- Permission denied after entering the password.

## Debug Output
- SSH connection established successfully.
- Authentication methods tried: publickey, gssapi-keyex, gssapi-with-mic, password.
- No valid Key exchange context for gssapi-keyex.
- No Kerberos credentials available for gssapi-with-mic.
- Public key authentication failed.
- Password authentication failed with "Permission denied, please try again."

## HPC Admin Responses
- Initial response indicated a VPN issue, but later clarified it was not a VPN problem.
- Suggested that the issue might be with the authentication credentials.
- Correct username provided: `iwsp027h` instead of `iwsp027`.

## Solution
- The root cause of the problem was an incorrect username.
- The correct username `iwsp027h` was provided by the HPC Admin.
- User confirmed that using the correct username resolved the issue.

## Keywords
- SSH
- VPN
- Authentication
- Publickey
- Password
- Permission denied
- Username

## What to Learn
- Always verify the username and password when encountering authentication issues.
- Ensure that the correct username is used for SSH connections.
- If public key authentication fails, check the availability and correctness of the public key.
- If password authentication fails, ensure that the correct password is being used.
- Communicate clearly with the user to understand the exact problem and provide precise solutions.
---

### 2024031942003815_Unable%20to%20connect%20to%20hpc%20via%20ssh%20-%20iwb8100h.md
# Ticket 2024031942003815

 ```markdown
# HPC Support Ticket: Unable to Connect via SSH

## Keywords
- SSH
- Connection Issues
- SSH Key
- ProxyJump
- Username Mismatch

## Problem Description
The user is unable to connect to `tinyx.nhr.fau.de` via SSH despite following the provided tutorial and configuring the SSH key correctly.

## Root Cause
The SSH configuration file (`~/.ssh/config`) is missing the necessary section for the proxy jump host (`csnhr.nhr.fau.de`), leading to a username mismatch during the authentication process.

## Solution
Ensure that the entire SSH configuration template is copied, including the section for the proxy jump host. The `csnhr.nhr.fau.de` section is required for the `tinyx.nhr.fau.de` section to function correctly.

## Steps to Resolve
1. Copy the entire SSH configuration template from the tutorial.
2. Ensure that the `csnhr.nhr.fau.de` section is included in the `~/.ssh/config` file.
3. Verify that the correct username is used for both the proxy jump host and the target host.

## Example Configuration
```ini
Host tinyx.nhr.fau.de
    HostName tinyx.nhr.fau.de
    User iwb8100h
    ProxyJump csnhr.nhr.fau.de
    UseKeychain yes
    AddKeysToAgent yes
    IdentityFile ~/.ssh/id_ed2559_nhr_fau
    IdentitiesOnly yes
    PasswordAuthentication no
    PreferredAuthentications publickey
    ForwardX11 no
    ForwardX11Trusted no

Host csnhr.nhr.fau.de
    HostName csnhr.nhr.fau.de
    User iwb8100h
    UseKeychain yes
    AddKeysToAgent yes
    IdentityFile ~/.ssh/id_ed2559_nhr_fau
    IdentitiesOnly yes
    PasswordAuthentication no
    PreferredAuthentications publickey
    ForwardX11 no
    ForwardX11Trusted no
```

## Conclusion
Ensure that all necessary sections of the SSH configuration template are included to avoid username mismatches and authentication failures.
```
---

### 2023053042004014_Migration%20of%20bcpc%20HPC%20accounts%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20mandato.md
# Ticket 2023053042004014

 # HPC Support Ticket Conversation Summary

## Subject
Migration of bcpc HPC accounts to new HPC portal / SSH keys become mandatory

## Keywords
- HPC account migration
- SSH keys
- HPC portal
- Single Sign-On (SSO)
- IdM portal
- Account validity
- Usage statistics
- ClusterCockpit
- Jupyterhub

## General Learnings
- **Migration to New HPC Portal**: The HPC services are migrating from the IdM portal to a new online HPC portal.
- **SSH Keys Mandatory**: Access to HPC systems will require SSH keys by mid-June. Accepted SSH key types are RSA (4096 bits), ECDSA (512 bits), and ED25519.
- **SSH Key Generation**: Users need to generate SSH key pairs with passphrases and upload the public keys to the HPC portal.
- **Account Validity**: The HPC portal will be the sole source for account validity. Users should contact their PI or project manager for account extensions.
- **Usage Statistics**: The HPC portal will display usage statistics, visible to PIs and project managers.
- **ClusterCockpit and Jupyterhub**: Access to these services will be through Single Sign-On links within the HPC portal.

## Root Cause of the Problem
- Users need to migrate their accounts to the new HPC portal and set up SSH keys for continued access.

## Solution
- **Login to New Portal**: Users should log in to the new HPC portal using their IdM credentials.
- **Generate SSH Keys**: Users should generate SSH key pairs and upload the public keys to the HPC portal.
- **Ignore IdM Expiration Emails**: Users can ignore emails about HPC service expiration from the IdM portal.
- **Contact PI/Project Manager**: For account validity updates, users should contact their PI or project manager.

## Additional Notes
- **Documentation and FAQs**: Users unfamiliar with SSH keys should refer to the provided documentation and FAQs.
- **Windows Users**: Recommended to use OpenSSH built into Windows (Power)Shell or MobaXterm instead of Putty.

---

This summary provides a concise overview of the migration process and the necessary steps for users to maintain access to HPC services.
---

### 2023101842003261_Invitation%20for%20%22Projektpartner%20Tier3%20Grundversorgung%20LS%20Werkstoffsimulation%20%28WW8%2.md
# Ticket 2023101842003261

 # HPC Support Ticket Analysis

## Keywords
- HPC Portal
- SSO Login
- Invitation
- Email Accounts
- SSH Public Key
- Username
- Password
- Dialogserver

## Problem
- User unable to find invitation in HPC portal.
- Invitation sent to different email account.
- Uncertainty about username and password for dialogserver.

## Root Cause
- Invitation was sent to an email account (`sbailo@physik.hu-berlin.de`) different from the one used for SSO login (`luigi.sbailo@hu-berlin.de`).
- User was unaware of the correct username and password for accessing the dialogserver.

## Solution
- HPC Admin changed the invitation email to match the SSO login email.
- User was able to accept the invitation and upload the SSH public key.
- HPC Admin needs to provide the correct username and password for dialogserver access.

## General Learnings
- Ensure invitations are sent to the correct email address associated with the user's SSO login.
- Provide clear instructions on how to log in to the dialogserver, including username and password details.
- Users may have multiple email accounts, so it's important to verify the correct one for HPC portal access.
---

### 2023112342004883_Ssh%20zum%20Alex%20Cluster.md
# Ticket 2023112342004883

 # HPC Support Ticket: SSH Access to Alex Cluster

## Keywords
- SSH
- Public Key
- Authentication
- ssh_config
- HPC Portal
- Login Node

## Problem Description
The user is unable to SSH into the Alex Cluster from a login node of the HPC FAU. The error message indicates that the authentication methods have been exhausted without success.

## Root Cause
- The user has multiple public keys registered in the HPC Portal.
- The local SSH settings are not configured to use the correct key for authentication.

## Solution
1. **Configure Local SSH Settings**:
   - The user needs to adjust their local SSH configuration to ensure the correct key is used for authentication.
   - A template for the `ssh_config` file can be found at [HPC FAU SSH Documentation](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems).

2. **Ensure Correct Key Usage**:
   - Verify that the correct public key is being offered during the SSH connection attempt.
   - Ensure that the private key corresponding to the public key registered in the HPC Portal is available and correctly referenced in the SSH configuration.

## General Learning
- **Multiple Public Keys**: Users may have multiple public keys registered, and the SSH client needs to be configured to use the correct one.
- **SSH Configuration**: Proper configuration of the `ssh_config` file is crucial for seamless SSH access, especially in environments with multiple keys.
- **Documentation Reference**: Always refer to the official documentation for configuration templates and guidelines.

## Additional Resources
- [HPC FAU SSH Documentation](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems)
- [Alex Cluster Documentation](https://hpc.fau.de/systems-services/documentation-instructions/clusters/alex-cluster/#sshhostkeys)

This report can be used as a reference for similar issues related to SSH authentication and configuration in the HPC environment.
---

### 2023092542004151_Bitte%20die%20Einladung%20%2210958%22%20canceln.md
# Ticket 2023092542004151

 ```markdown
# HPC Support Ticket: Cancel Invitation

## Keywords
- Invitation
- Cancel
- Wrong Project
- Permissions
- Database

## Summary
A user requested to cancel an invitation that was mistakenly sent to the wrong project. The HPC Admin noted that their permissions were insufficient to delete invitations through the portal and had to perform the action directly in the database.

## Root Cause
- User was added to the wrong project due to an incorrect invitation.

## Solution
- HPC Admin withdrew the invitation directly from the database due to insufficient permissions in the portal.

## Lessons Learned
- Ensure invitations are sent to the correct projects to avoid such issues.
- HPC Admins may need higher permissions or a more streamlined process to handle invitation cancellations.
- Direct database manipulation may be required for certain administrative tasks.
```
---

### 2025012242002302_SSH-Key%20funktioniert%20nicht%20-%20dsam003h.md
# Ticket 2025012242002302

 # HPC Support Ticket: SSH-Key funktioniert nicht

## Keywords
- SSH-Key
- Windows
- Linux
- config file
- Permission denied
- Passphrase
- DNS
- Debugging

## Problem Description
- User can access HPC via SSH-Key on Linux partition but encounters "Permission denied" error on Windows.
- User has configured SSH key and config file on Windows but still faces issues.

## Root Cause
- Incorrect DNS used for connection.
- Possible issues with SSH config file and permissions.

## Troubleshooting Steps
1. **Verify Passphrase vs. Password**:
   - HPC Admin clarified that there is no password for FAU Clusters, only a passphrase.

2. **Check SSH Config File**:
   - Ensure the config file has no file extension.
   - Refer to the template for connecting to HPC systems: [Template for Connecting to HPC Systems](https://doc.nhr.fau.de/access/ssh-command-line/#template-for-connecting-to-hpc-systems)

3. **Debugging SSH Connection**:
   - User was asked to provide the output of SSH with debugging enabled: `ssh -vv ...`

4. **Correct DNS**:
   - HPC Admin identified that the user was using the wrong DNS (`woody.rrze.fau.de`).
   - Correct DNS provided: `woody.nhr.fau.de`

## Solution
- Use the correct DNS (`woody.nhr.fau.de`) for the SSH connection.
- Ensure the SSH config file is correctly set up without a file extension.
- If issues persist, provide the debugging output for further analysis.

## Additional Notes
- The user encountered issues with OpenSSH looking for the config file in a restricted directory and received an async IO error when trying to reference the config file directly.
- Further debugging output is required to diagnose additional issues.

## References
- [Template for Connecting to HPC Systems](https://doc.nhr.fau.de/access/ssh-command-line/#template-for-connecting-to-hpc-systems)

## Support Team
- **HPC Admins**: Provided initial troubleshooting steps and identified the incorrect DNS.
- **2nd Level Support Team**: Not directly involved in this ticket but available for further escalation if needed.

## Next Steps
- If the user continues to face issues, gather the debugging output and escalate to the 2nd Level Support Team for further analysis.
---

### 2024120942003586_AW%3A%20%28extern%29%20New%20invitation%20for%20%22HPC4AAI%20-%20Studentische%20Abschlu%C3%83%C2%9Fa.md
# Ticket 2024120942003586

 # HPC Support Ticket Conversation Analysis

## Keywords
- Invitation
- Expiration
- SSO Login
- SSH Public Key
- Cookies
- Error Message

## Summary
A user received an invitation to an HPC project but encountered an error message when trying to accept it. The user suspected the invitation might have expired.

## Root Cause
- The user received an error message (`myerror.png`) while trying to accept the invitation.
- The error message suggested a potential issue with cookies.

## Solution
- The HPC Admin confirmed that the invitation had not expired.
- The user was advised to check if the issue was related to cookies, as suggested by the error message.
- The invitation was eventually accepted successfully.

## What Can Be Learned
- **Invitation Expiration**: Invitations have an expiration period, but it's important to verify if the invitation is still valid.
- **Error Messages**: Pay attention to error messages for clues on troubleshooting steps.
- **Cookies**: Issues with cookies can sometimes prevent successful login or acceptance of invitations.
- **SSO Login**: Ensure proper SSO login using IdM credentials.
- **SSH Public Key**: After accepting the invitation, upload an SSH public key to the corresponding account.

## Documentation Links
- [HPC Portal Documentation](https://doc.nhr.fau.de/hpc-portal/)

## Support Contacts
- **HPC Admins**: For general support and administration.
- **2nd Level Support Team**: For technical issues and troubleshooting.
- **Gehard Wellein**: Head of the Datacenter.
- **Georg Hager**: Training and Support Group Leader.
- **Harald Lanig**: NHR Rechenzeit Support and Applications for Grants.
- **Jan Eitzinger and Gruber**: Software and Tools developers.

## Conclusion
This conversation highlights the importance of checking error messages and verifying the status of invitations. It also emphasizes the need for proper SSO login and SSH key management.
---

### 2024020842003427_Invitation%20missing.md
# Ticket 2024020842003427

 # HPC Support Ticket: Invitation Missing

## Keywords
- Invitation not visible
- Email mismatch
- SSO/IdP issue
- Home directory error
- Account not available

## Problem Description
- User received an invitation email but could not see the invitation in the portal.
- SSO/IdP transmitted a different email address than the one the invitation was sent to.

## Root Cause
- Email mismatch between the invitation email and the email transmitted by SSO/IdP.

## Solution
- HPC Admin updated the invitation email to match the one transmitted by SSO/IdP.

## Additional Issue
- User encountered an error when connecting to Alex: "Could not chdir to home directory... This account is currently not available."

## Additional Solution
- HPC Admin informed the user that it takes until the next day morning for all services to be set up after accepting the invitation.

## General Learnings
- Email mismatches can cause invitation issues.
- SSO/IdP may transmit unexpected email addresses.
- After accepting an invitation, services may take time to be fully set up.
- Home directory errors may indicate that the account is not yet fully activated.

## Related Parties
- HPC Admins
- 2nd Level Support Team
- Head of the Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support
- Software and Tools Developer
---

### 2024030142001298_Migration%20of%20mppm001h%20HPC%20accounts%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20man.md
# Ticket 2024030142001298

 # HPC Support Ticket Conversation Summary

## Subject
Migration of HPC accounts to new HPC portal / SSH keys become mandatory

## Keywords
- HPC account migration
- SSH keys
- HPC portal
- Single Sign-On (SSO)
- IdM portal
- SSH key types (RSA, ECDSA, ED25519)
- Usage statistics
- ClusterCockpit
- Jupyterhub

## General Learnings
- **Migration Process**: HPC accounts are being migrated from the IdM portal to a new online HPC portal.
- **SSH Keys**: Access to HPC systems will require SSH keys from March 15th. Accepted types are RSA (4096 bits), ECDSA (512 bits), and ED25519.
- **Portal Access**: The new HPC portal can be accessed via SSO using IdM credentials.
- **Account Validity**: The HPC portal will be the sole source for account validity starting from the end of February.
- **Usage Statistics**: Users, PIs, and project managers can view usage statistics in the HPC portal.
- **ClusterCockpit and Jupyterhub**: Access these services via SSO links from the HPC portal.

## Root Cause of the Problem
- Users need to migrate their accounts and set up SSH keys for continued access to HPC systems.

## Solution
- **Account Migration**: Log in to the new HPC portal using SSO with IdM credentials.
- **SSH Key Setup**: Generate and upload SSH key pairs with passphrases to the HPC portal. Follow the documentation and FAQs for guidance.
- **Ignore IdM Expiration Emails**: Emails about HPC service expiration in the IdM portal can be ignored.
- **Account Validity Update**: Contact the PI or project manager to update account validity.

## Additional Notes
- **Windows Users**: Recommended to use OpenSSH built into Windows (Power)Shell or MobaXterm instead of Putty.
- **Documentation**: Refer to the provided documentation and FAQs for detailed instructions on SSH key setup.

---

This summary provides a concise overview of the migration process, key requirements, and steps for users to follow. It serves as a quick reference for support employees to assist users during the migration period.
---

### 2024022942002264_Migration%20of%20ws35%20HPC%20accounts%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20mandato.md
# Ticket 2024022942002264

 # HPC Support Ticket: Migration of ws35 HPC Accounts to New HPC Portal / SSH Keys Become Mandatory

## Keywords
- HPC account migration
- SSH keys
- HPC portal
- IdM portal
- Single Sign-On (SSO)
- SSH key types (RSA, ECDSA, ED25519)
- Usage statistics
- ClusterCockpit
- Jupyterhub

## Summary
The HPC services at FAU are migrating existing HPC accounts from the IdM portal to a new online HPC portal. This migration involves several changes, including the mandatory use of SSH keys for accessing HPC systems.

## Key Points
- **New HPC Portal**: Accessible at [https://portal.hpc.fau.de](https://portal.hpc.fau.de). Login with SSO using IdM credentials.
- **SSH Keys**: Mandatory for accessing HPC systems. Accepted types are RSA (4096 bits), ECDSA (512 bits), and ED25519.
- **SSH Key Documentation**: Available at [HPC Documentation](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/) and [FAQs](https://hpc.fau.de/faqs/#ID-230).
- **Windows Users**: Recommended to use OpenSSH built into Windows (Power)Shell or MobaXterm instead of Putty.
- **Account Validity**: The HPC portal will be the sole source for account validity. Contact PI or project manager for updates.
- **Usage Statistics**: Visible to users, PIs, and project managers.
- **ClusterCockpit and Jupyterhub**: Access via Single Sign-On links from within the HPC portal.

## Root Cause of the Problem
- Users need to migrate their accounts to the new HPC portal and set up SSH keys for continued access to HPC systems.

## Solution
- Users should log in to the new HPC portal using their IdM credentials.
- Generate and upload SSH key pairs with passphrases.
- Use the new HPC portal for all account-related activities and access to HPC systems.

## Additional Notes
- The IdM portal and the new HPC portal are completely decoupled.
- Users should ignore automatic messages about HPC service expiration from the IdM portal.
- For new HPC accounts, users should contact their PI or project manager instead of RRZE.

---

This documentation is intended to assist support employees in understanding and resolving similar issues related to HPC account migration and SSH key setup.
---

### 2024062442000491_Unable%20to%20access%20the%20hpc%20account.md
# Ticket 2024062442000491

 # HPC Support Ticket Analysis: Unable to Access HPC Account

## Keywords
- HPC account access
- SSH keys
- Permission error
- ProxyJump configuration
- Documentation reference

## Root Cause of the Problem
- Invalid OpenSSH private key in the file "hpc_key".
- Incorrect SSH key permissions (0644).
- Manual connection attempt to `cshpc` instead of using ProxyJump.

## Solution
- Ensure the SSH private key is valid and correctly formatted.
- Correct the permissions of the SSH key file to 0600.
- Configure the SSH client for ProxyJump to automatically connect to `meggie.rrze`.
- Refer to the documentation for configuring connection settings:
  - [MobaXTerm Configuration](https://doc.nhr.fau.de/access/ssh-mobaxterm/#configuring-connection-settings)
  - [OpenSSH Configuration](https://doc.nhr.fau.de/access/ssh-command-line/#template-for-connecting-to-hpc-systems)

## General Learnings
- Always verify the validity and permissions of SSH keys.
- Use ProxyJump for secure and automated connections.
- Follow the provided documentation for configuration steps.
- Be aware of upcoming system changes, such as the decommissioning of `cshpc`.

## Additional Notes
- The user was reminded about the upcoming decommissioning of `cshpc` and the need to switch to `csnhr`.
- The support team provided detailed documentation links for configuring SSH clients.
---

### 2024102442002651_User%20mpm1001h.md
# Ticket 2024102442002651

 # HPC Support Ticket Analysis

## Keywords
- User account activation
- Login issue
- IdM-Account
- SSH key
- HPC portal
- Account management

## Summary
A user was unable to log in to the HPC cluster despite being listed as active in the administration account. The issue was due to the service termination date in the IdM-Account.

## Root Cause
- The user's service in the IdM-Account had terminated on 30/03/2024.
- The user was on leave ("beurlaubt") but needed to continue their project.

## Solution
- The HPC Admin advised that the HPC entry in IDM is outdated.
- Users should log into the HPC portal (`https://portal.hpc.fau.de/`) and upload an SSH key as described in the documentation (`https://doc.nhr.fau.de/access/ssh-command-line/`).
- After uploading the SSH key, the login should work again within a few hours.

## General Learnings
- Always check the HPC portal for the latest account management procedures.
- Ensure that the service termination date in the IdM-Account is up-to-date.
- Uploading an SSH key through the HPC portal can resolve login issues.

## Actions for Support Employees
- Direct users to the HPC portal for account management.
- Provide instructions for uploading SSH keys.
- Verify the service termination date in the IdM-Account and update if necessary.
---

### 2024030142000486_Migration%20of%20mpm3%20HPC%20accounts%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20mandato.md
# Ticket 2024030142000486

 # HPC Support Ticket: Migration of mpm3 HPC Accounts to New HPC Portal / SSH Keys Become Mandatory

## Keywords
- HPC account migration
- SSH keys
- HPC portal
- Single Sign-On (SSO)
- IdM portal
- SSH key types (RSA, ECDSA, ED25519)
- Usage statistics
- ClusterCockpit
- Jupyterhub

## Summary
The HPC support team is migrating existing HPC accounts from the IdM portal to a new, purely online HPC portal. This migration includes changes to the login process and the introduction of mandatory SSH keys for accessing HPC systems.

## Key Points to Learn
- **HPC Portal Access**: The new HPC portal can be accessed at [https://portal.hpc.fau.de](https://portal.hpc.fau.de) using Single Sign-On (SSO) with IdM credentials.
- **SSH Keys**: From March 11th, access to HPC systems will require SSH keys. Accepted SSH key types are RSA (at least 4096 bits), ECDSA (512 bits), and ED25519.
- **SSH Key Generation**: Users need to generate SSH key pairs with a passphrase and upload the public key to the HPC portal. It may take up to two hours for all HPC systems to recognize the updated SSH public keys.
- **Documentation and FAQs**: For users unfamiliar with SSH keys, documentation and FAQs are available at [HPC Documentation](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/) and [HPC FAQs](https://hpc.fau.de/faqs/#ID-230).
- **Windows Users**: Recommended tools for Windows users are OpenSSH built into the Windows (Power)Shell or MobaXterm instead of Putty.
- **Account Validity**: The HPC portal will be the sole source for account validity starting from the end of February. Users should contact their PI or project manager to update account validity.
- **Usage Statistics**: The HPC portal will display usage statistics for different HPC systems, which will also be visible to PIs and project managers.
- **ClusterCockpit and Jupyterhub**: Users should use the Single Sign-On link from within the HPC portal to access ClusterCockpit and Jupyterhub services.

## Root Cause and Solution
- **Root Cause**: The migration process requires users to adopt SSH keys for secure access to HPC systems.
- **Solution**: Users need to generate and upload SSH keys to the HPC portal and use the new portal for all HPC-related activities.

## Additional Notes
- Users may receive an email from the IdM portal about the expiration of their HPC service, which can be ignored.
- The HPC portal and IdM portal are completely decoupled, and the HPC portal will not be aware of contract extensions or departures from the university.

This documentation aims to assist HPC support employees in understanding and resolving similar issues related to account migration and SSH key implementation.
---

### 2024110642002763_Invitation%20not%20received.md
# Ticket 2024110642002763

 # HPC Support Ticket: Invitation Not Received

## Keywords
- Invitation not visible
- Multiple email addresses
- Project invitation
- HPC portal
- IdP email mismatch

## Problem Description
The user received an invitation to an HPC project but could not see the invitation in the HPC portal. The root cause of the problem was that the user's account is associated with two email addresses, and the invitation was sent to the email address that did not match the one registered with the Identity Provider (IdP).

## Solution
The HPC Admin advised the user to ask the project manager to resend the invitation to the correct email address (the one registered with the IdP) and delete the invalid invitation. The invitation email address must match the one transmitted by the IdP, as found under the user's profile after login.

## General Learnings
- Invitations are tied to the email address registered with the IdP.
- In case of multiple email addresses, ensure the invitation is sent to the correct one.
- Project managers can resend invitations and delete invalid ones.
- Users can check their registered email address under their profile in the HPC portal.

## Related Links
- [HPC Portal Documentation](https://doc.nhr.fau.de/hpc-portal/#the-management-tab-visible-only-for-pis-and-technical-contacts)
- [HPC FAU Website](https://hpc.fau.de/)
---

### 2024021442001604_Problem%20with%20login%20HPC%20account.md
# Ticket 2024021442001604

 ```markdown
# HPC Support Ticket: Problem with Login HPC Account

## Keywords
- Login issue
- SSH
- MobaXterm
- File server issues

## Problem Description
- User unable to see the path in the terminal after logging in via SSH using MobaXterm.
- Command used: `ssh -l iwb9003h cshpc.rrze.fau.de`

## Root Cause
- Issues with one of the file servers.

## Solution
- The file server issues were resolved by the HPC Admins.
- User confirmed that the problem was solved after the resolution.

## Lessons Learned
- File server issues can cause login problems, such as missing terminal paths.
- Regularly check the status of file servers when troubleshooting login issues.
- Communicate with users to confirm the resolution of issues.
```
---

### 2023052642001972_HPC%20account%20fuer%20Gastwissenschaftler%20Raphael%20Desrues%2C%20gu84gopi%20-%20CCC.md
# Ticket 2023052642001972

 # HPC Support Ticket: HPC Account for Guest Researcher

## Keywords
- HPC Account
- Guest Researcher
- Paper Application
- HPC Portal
- SSH Keys
- SSO Attributes
- FAU-IDM-Kennung

## Summary
A guest researcher required an HPC account for MD-simulations on tinygpu. The initial process faced issues, but a paper application was submitted and eventually resolved through the HPC portal.

## Root Cause
- Delay in migrating HPC accounts to the new portal.
- Initial issues with the account creation process.

## Solution
- Paper application was used as a temporary solution.
- HPC Admin expedited the migration process, allowing the user to trigger the account creation themselves.
- The guest researcher received an HPC invitation and was assisted with setting up SSH keys.
- SSO login and account generation were successful.

## General Learnings
- Paper applications can be used as a fallback when the portal is not fully operational.
- HPC Admins can expedite the migration process if necessary.
- SSH keys are essential for account setup and should be assisted if needed.
- If SSO attributes are not transmitted, the guest researcher can reserve an email address for their FAU-IDM-Kennung and log in via FAU-SSO.

## Roles Involved
- **HPC Admins**: Assisted with the account creation and migration process.
- **2nd Level Support Team**: Provided support and assistance with the account setup.
- **Head of the Datacenter**: Oversaw the datacenter operations.
- **Training and Support Group Leader**: Managed training and support activities.
- **NHR Rechenzeit Support**: Handled applications for grants.
- **Software and Tools Developer**: Developed necessary software and tools.

## Conclusion
The issue was resolved through a combination of paper applications and expedited migration. The guest researcher was able to set up their account and begin their research.
---

### 2023110342000905_HPC%20Account%20-%20bcpc01.md
# Ticket 2023110342000905

 ```markdown
# HPC Account Issue: bcpc01

## Keywords
- HPC Account
- IDM-Portal
- HPC-Portal
- SSH Key
- Login Issue
- Ticket Management

## Problem Description
- User reported that their HPC account (bcpc01) was marked as expired in the IDM-Portal but still active in the HPC-Portal.
- User was unable to log in to the HPC system.

## Root Cause
- Discrepancy between the account status in the IDM-Portal and HPC-Portal.
- Potential issue with SSH key configuration.

## Ticket Management
- Initial request was delayed due to misrouting within the ticketing system (OTRS).
- User followed up after several days without a response.

## Solution
- HPC Admin confirmed that the SSH key was correctly configured.
- User was advised to follow the debugging steps for SSH problems provided in the FAQ.
- User resolved the issue independently after following the provided steps.

## Lessons Learned
- Ensure proper routing of tickets to avoid delays.
- Provide clear and timely communication with users regarding the status of their requests.
- Refer users to relevant documentation for troubleshooting common issues.

## References
- [Debugging SSH Problems](https://hpc.fau.de/faqs/#debugging-ssh-problems)
```
---

### 2024111042000426_connect%20ssh%20problem%20-%20iwi5241h.md
# Ticket 2024111042000426

 ```markdown
# SSH Connection Issue: Server Refused Key

## Keywords
- SSH
- Mobaxterm
- Key Refusal
- SSH Config
- Key Propagation Delay

## Problem Description
User encountered an issue when attempting to connect via SSH using Mobaxterm:
- **Error Message:** "Server refused our key."

## Root Cause
1. **Key Propagation Delay:** The new SSH key was uploaded to the portal recently, and there is a delay of at least 2 hours before the key is copied over to the systems.
2. **Incorrect Key Configuration:** The transmitted key might be incorrect due to an existing path in the SSH config pointing to a different key file.

## Solution
1. **Wait for Key Propagation:** Ensure that at least 2 hours have passed since the new SSH key was uploaded to the portal.
2. **Verify Key Configuration:** Make sure that the key file used for the SSH connection is the one generated together with the public key uploaded to the portal.

## Additional Notes
- Ensure that the login attempt is made with the correct HPC credentials.

## Conclusion
The issue can be resolved by waiting for the key propagation delay and ensuring the correct key configuration in the SSH settings.
```
---

### 2023051042001153_Host%20key%20memoryhog.md
# Ticket 2023051042001153

 ```markdown
# HPC-Support Ticket: Host Key Mismatch for 'memoryhog'

## Keywords
- SSH
- Host Key
- ECDSA
- ssh_known_hosts
- IP Address
- Hostname

## Problem Description
The user encountered a warning when attempting to SSH into 'memoryhog'. The warning indicated a mismatch between the ECDSA host key for 'memoryhog' and the key for its IP address.

## Root Cause
The `ssh_known_hosts` file contained an outdated entry for the old glados-Testcluster installation, including its IP address. This caused a mismatch between the hostname and IP address keys.

## Solution
The issue was resolved by identifying and removing the outdated entry in the `ssh_known_hosts` file. This ensured that the correct key was used for both the hostname and IP address.

## General Learning
- Ensure that `ssh_known_hosts` entries are up-to-date, especially after system migrations or updates.
- Mismatched host keys can cause SSH connection warnings or failures.
- Verify and update SSH known hosts entries to avoid key mismatch issues.
```
---

### 2024021942001453_Migration%20of%20mfpb%20HPC%20accounts%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20mandato.md
# Ticket 2024021942001453

 # HPC Support Ticket Summary

## Subject
Migration of mfpb HPC accounts to new HPC portal / SSH keys become mandatory

## Keywords
- HPC account migration
- SSH keys
- HPC portal
- Single Sign-On (SSO)
- IdM portal
- ClusterCockpit
- Jupyterhub

## Key Points
- **Migration Process**: Existing HPC accounts are being migrated to a new online HPC portal.
- **SSH Keys**: Access to HPC systems will require SSH keys only. Accepted types are RSA (4096 bits), ECDSA (512 bits), and ED25519.
- **Portal Access**: The new HPC portal can be accessed at [https://portal.hpc.fau.de](https://portal.hpc.fau.de) using SSO with IdM credentials.
- **Usage Statistics**: Users can view their usage statistics, which are also visible to PIs and project managers.
- **ClusterCockpit and Jupyterhub**: Access these services via SSO links from the HPC portal.

## Instructions for Users
- **SSH Key Generation**: Generate SSH key pairs with passphrases and upload the public key to the HPC portal.
- **Documentation**: Refer to the documentation and FAQs for SSH key setup.
- **Windows Users**: Recommended to use OpenSSH built into Windows (Power)Shell or MobaXterm instead of Putty.
- **Account Validity**: Contact the PI or project manager to update account validity.

## Notes for Support Employees
- **Expiration Messages**: Users may receive automatic expiration messages from the IdM portal, which can be ignored.
- **Decoupled Portals**: The IdM portal and the new HPC portal are completely decoupled.
- **Usage Monitoring**: PIs and project managers can monitor usage statistics of their team members.

## Root Cause of the Problem
- **Migration Requirement**: The need to migrate accounts to a new portal and enforce SSH key usage for security and management purposes.

## Solution
- **Follow Migration Instructions**: Users should follow the provided instructions to access the new portal, generate SSH keys, and update their account information as needed.

---

This summary provides a concise overview of the migration process, key instructions, and important notes for both users and support employees.
---

### 2024011942000769_Probable%20security%20breach%20-%20a104bc11.md
# Ticket 2024011942000769

 # HPC Support Ticket: Probable Security Breach

## Keywords
- Security breach
- SSH key
- HPC portal
- Password
- DFN-AAI/SSO
- Authorized_keys
- Login activity

## Problem
- User experienced a probable hacking attack on their private machine used to connect to the HPC cluster.
- Concerns about the security of their password and SSH key.

## Actions Taken by HPC Admins
- Checked login activity; no increased activity observed.
- Removed old SSH key from the HPC portal.
- Verified the absence of an `authorized_keys` file in the user's `~/.ssh` directory.

## Solution
- User was instructed to upload a new SSH public key to the HPC portal once their system was restored.
- It was noted that it would take approximately 2 hours for all HPC systems to recognize the new SSH key.
- No further action was required regarding passwords as the system relies on DFN-AAI/SSO.

## Outcome
- User confirmed that their new system was up and secure.
- New SSH key was successfully uploaded and access was regained.

## General Learnings
- Immediate notification of potential security breaches is crucial.
- Regularly check login activity and remove compromised SSH keys.
- Ensure users understand the process for uploading new SSH keys and the time required for system recognition.
- DFN-AAI/SSO simplifies password management in such scenarios.

## Root Cause
- Probable hacking attack on the user's private machine.

## Solution Found
- Removal of old SSH key and upload of a new SSH public key to the HPC portal.
---

### 2024031242003801_Connection%20timeout.md
# Ticket 2024031242003801

 ```markdown
# HPC Support Ticket: Connection Timeout

## Keywords
- SSH connectivity issue
- VSCode
- Connection timeout
- SSH Resolver
- Remote-SSH extension
- OpenSSH
- SSH config file

## Problem Description
- User experiencing intermittent SSH connectivity issues with HPC.
- Connection establishes after restarting VSCode a few times but gets auto-disconnected.
- Logs indicate multiple attempts to locate SSH executable, eventually using `C:\Windows\System32\OpenSSH\ssh.exe`.
- Connection times out with error: `Error: Connecting with SSH timed out`.

## Root Cause
- Possible issues with SSH configuration or network stability.
- Multiple failed attempts to locate SSH executable before successful connection.

## Solution
- HPC Admin suggested running `ssh -vv tinyx.nhr.fau.de` from the command line to gather more detailed logs.
- Recommended adding reconnect options to the SSH config file to avoid disconnects.

## General Learnings
- Ensure SSH executable path is correctly set in VSCode settings.
- Use verbose SSH logging (`ssh -vv`) to diagnose connection issues.
- Configure SSH to automatically reconnect to avoid frequent disconnections.
```
---

### 2023053142000151_Migration%20of%20HPC%20accounts%20of%20AG%20M%C3%83%C2%B6lg%20to%20new%20HPC%20portal%20_%20SSH%20ke.md
# Ticket 2023053142000151

 # HPC Support Ticket Conversation Summary

## Keywords
- HPC account migration
- SSH keys
- HPC portal
- IdM portal
- Single Sign-On (SSO)
- Account validity
- Usage statistics
- ClusterCockpit
- Jupyterhub
- Project management

## General Learnings
- **Migration to New HPC Portal**: The migration process involves moving HPC accounts from the IdM portal to a new online HPC portal.
- **SSH Keys Mandatory**: Access to HPC systems will require SSH keys by mid-June. Accepted key types are RSA (4096 bits), ECDSA (512 bits), and ED25519.
- **SSH Key Upload**: Users need to generate SSH key pairs with passphrases and upload the public keys to the HPC portal.
- **Account Validity**: The HPC portal will be the sole source for account validity. Users should contact their PI or project manager to update account validity.
- **Usage Statistics**: The HPC portal displays usage statistics, which are also visible to PIs and project managers.
- **ClusterCockpit and Jupyterhub**: Users should use Single Sign-On links from the HPC portal to access ClusterCockpit and Jupyterhub.
- **Project Management**: PIs and project managers can manage account validity and view usage statistics for their team members.

## Specific Actions
- **Adding Users to Other Projects**: HPC Admins can add users to additional projects via the "Other Projects" feature in the HPC portal. This grants additional Unix group memberships and makes the users visible to the managers of those projects.

## Root Cause and Solution
- **Root Cause**: The need to migrate HPC accounts to a new portal and enforce SSH key-based access.
- **Solution**: Users must log in to the new HPC portal using SSO, generate and upload SSH keys, and use the portal for account management and accessing services like ClusterCockpit and Jupyterhub.

## Documentation Links
- [SSH Secure Shell Access to HPC Systems](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/)
- [FAQs](https://hpc.fau.de/faqs/#ID-230)

## Additional Notes
- Windows users are recommended to use OpenSSH built into the Windows (Power)Shell or MobaXterm instead of Putty.
- The IdM portal and the new HPC portal are completely decoupled, so the HPC portal will not automatically update account validity based on contract extensions or departures from the university.
---

### 2024030142000521_Migration%20of%20iww6003h%20HPC%20accounts%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20man.md
# Ticket 2024030142000521

 # HPC Support Ticket: Migration of HPC Accounts to New Portal / SSH Keys Mandatory

## Keywords
- HPC account migration
- SSH keys
- HPC portal
- IdM portal
- Single Sign-On (SSO)
- SSH key types (RSA, ECDSA, ED25519)
- Usage statistics
- ClusterCockpit
- Jupyterhub

## Summary
- **Migration Process**: HPC accounts are being migrated from the IdM portal to a new online HPC portal.
- **Access Method**: Starting March 15th, access to HPC systems will be via SSH keys only.
- **SSH Key Requirements**: Accepted SSH key types are RSA (4096 bits), ECDSA (512 bits), and ED25519.
- **Portal Access**: The new HPC portal can be accessed at [https://portal.hpc.fau.de](https://portal.hpc.fau.de) using SSO with IdM credentials.
- **Account Validity**: The HPC portal will be the sole source for account validity starting from the end of February.
- **Usage Monitoring**: Users, PIs, and project managers can view usage statistics in the HPC portal.
- **ClusterCockpit and Jupyterhub**: Access these services via SSO links from within the HPC portal.

## Root Cause of the Problem
- Users need to transition to the new HPC portal and set up SSH keys for continued access to HPC systems.

## Solution
- **Generate SSH Keys**: Users should generate SSH key pairs with a passphrase and upload the public key to the HPC portal.
- **Documentation**: Refer to the provided documentation and FAQs for guidance on SSH keys.
- **Windows Users**: Recommended to use OpenSSH built into Windows (Power)Shell or MobaXterm instead of Putty.
- **Account Validity**: Contact the PI or project manager to update the validity of the HPC account.

## Additional Notes
- Ignore automatic messages from the IdM portal regarding HPC service expiration.
- The HPC portal and IdM portal are completely decoupled.
- New HPC accounts should be requested through the PI or project manager, not RRZE.

## References
- [HPC Portal](https://portal.hpc.fau.de)
- [SSH Documentation](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/)
- [FAQs](https://hpc.fau.de/faqs/#ID-230)
---

### 2023112342004267_SSH%20key%20not%20getting%20added%20to%20HPC%20server.md
# Ticket 2023112342004267

 ```markdown
# HPC-Support Ticket: SSH Key Not Getting Added to HPC Server

## Subject
SSH key not getting added to HPC server

## User Issue
- User reinstalled OS on Linux PC and forgot to backup SSH private keys.
- New public SSH key not getting added to the HPC server.
- Error message: `Permission denied (publickey)`.

## User Actions Taken
1. Added a new key without removing the existing key from the same machine.
2. Deleted the reference to the machine from `known_hosts` on the HPC server using `ssh-keygen -R`.
3. Removed all keys from the Linux machine via the HPC portal and added a new key.

## HPC Admin Response
- Requested user to connect again with the option `ssh -vv` and send the output.
- Confirmed that the key referenced is known on the HPC server, suggesting a problem with the user's SSH configuration.

## Keywords
- SSH key
- Permission denied (publickey)
- known_hosts
- ssh-keygen -R
- HPC server
- ssh -vv

## Lessons Learned
- Always backup SSH keys before reinstalling the OS.
- Use `ssh -vv` to get detailed output for troubleshooting SSH connection issues.
- Ensure proper configuration of SSH keys and `known_hosts` file.

## Root Cause
- Potential misconfiguration in the user's SSH setup or issues with the new key not being properly recognized by the HPC server.

## Solution
- Use `ssh -vv` to diagnose the issue and provide detailed output to the HPC support team for further assistance.
```
---

### 2025022142000082_SSH%20login%20issue.md
# Ticket 2025022142000082

 # SSH Login Issue

## Keywords
- SSH login
- Command prompt
- Welcome message
- Last login info
- Fileserver issues
- Login hang

## Problem Description
User experiences an SSH login issue where they receive the welcome message and last login information but do not get the command prompt.

## Root Cause
Issues with a fileserver caused logins to hang.

## Solution
The fileserver issues were resolved by 07:30 AM, restoring normal login functionality.

## General Learning
- Fileserver issues can cause SSH logins to hang without reaching the command prompt.
- Monitoring and resolving fileserver issues can restore normal login functionality.

## Actions Taken
- HPC Admin informed the user about the fileserver issues and their resolution.

## Future Reference
If similar issues occur, check the status of the fileserver and ensure it is functioning correctly.
---

### 2024020142000899_HPC%20connection%20issue%20-%20iwfa030h.md
# Ticket 2024020142000899

 ```markdown
# HPC Connection Issue - User iwfa030h

## Keywords
- SSH keys
- Connection timeout
- HPC portal
- Account status

## Issue Description
- User iwfa030h reported being unable to login to the HPC system due to connection timeout.
- The user mentioned having added SSH keys last week and was able to login without issues previously.

## Root Cause
- No SSH key uploaded to the HPC portal.

## Support Interaction
- HPC Admin informed the user that there was no SSH key uploaded to the HPC portal.
- The user was directed to contact Andreas Mayr for further assistance regarding the account status.

## Solution
- The user needs to upload the SSH key to the HPC portal.
- Contact Andreas Mayr for account status verification.

## General Learnings
- Ensure SSH keys are properly uploaded to the HPC portal.
- Verify account status with the appropriate support team member if login issues persist.
```
---

### 42041387_Login%20auf%20testfront%20_%20woody.md
# Ticket 42041387

 # HPC Support Ticket Conversation Analysis

## Keywords
- Login issues
- SSH key authentication
- Password prompt
- Frontend access
- Key generation
- Agent forwarding

## Problem
- User unable to log in to frontends "woody" and "testfront" from "cshpc" due to password prompt.

## Root Cause
- User does not know the password for the account and needs to use SSH key authentication.

## Solution
- Configure SSH key authentication:
  - Option 1: Use agent forwarding to pass the user's existing SSH key.
  - Option 2: Generate a new SSH key on the HPC system and add it to the authorized keys:
    ```sh
    ssh-keygen -t rsa -b 4096 -f ~/.ssh/id_rsa -N ""
    cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
    ```

## General Learning
- SSH key authentication is required for accessing frontends when the password is unknown.
- Users can configure agent forwarding or generate a new SSH key for seamless login.

## Roles
- **HPC Admins**: Provide support and solutions for login issues.
- **2nd Level Support Team**: Assist with technical issues and troubleshooting.
- **Head of Datacenter**: Oversees datacenter operations.
- **Training and Support Group Leader**: Manages training and support activities.
- **NHR Rechenzeit Support**: Handles computing time support and grant applications.
- **Software and Tools Developer**: Develops and maintains software tools.
---

### 2024092442003956_Missing%20invitation%20in%20HPC-Portal.md
# Ticket 2024092442003956

 ```markdown
# Missing Invitation in HPC-Portal

## Keywords
- HPC-Portal
- Invitation
- User Tab
- SSO (Single Sign-On)
- Email Address

## Problem Description
The user was invited to a project but the invitation did not appear in the HPC-Portal. The supervisor reinvited the user, but the invitation and corresponding notification email still did not appear.

## Root Cause
The SSO system of the user's university transmitted an incorrect email address (`bt308848@uni-bayreuth.de`) instead of the user's actual email address (`Tim.Niemeyer@uni-bayreuth.de`).

## Solution
The HPC Admin corrected the email address associated with the invitation. The user was advised to report this issue to the SSO team of their university.

## Steps Taken
1. HPC Admin verified the user's status on the HPC portal.
2. User confirmed that there were no active accounts or pending invitations under the User tab.
3. HPC Admin identified the incorrect email address transmitted by the SSO system.
4. HPC Admin corrected the email address and resolved the issue.

## General Learning
- Ensure that the email address used for SSO matches the email address used for invitations.
- Verify the User tab in the HPC-Portal for active accounts and pending invitations.
- Report any discrepancies in email addresses to the relevant SSO team.
```
---

### 2024082142000895_Error%20during%20SAML%20authentication%20-%20KU-Eichst%C3%83%C2%A4tt.md
# Ticket 2024082142000895

 # Error during SAML Authentication - KU-Eichstätt

## Keywords
- SAML Authentication
- Shibboleth
- Timestamp Mismatch
- Server Time Settings
- Zeitzonen-Einstellungen
- SSO-Timestamp
- Login-Zeit
- FAU Portal
- IdP/SSO-Admin Team

## Problem Description
The user reported being unable to log in to the FAU HPC portal via Shibboleth. The issue was specific to the FAU portal, as Shibboleth login on another portal worked fine.

## Root Cause
The root cause of the problem was a mismatch between the server times of the Identity Provider (IdP) at KU Eichstätt-Ingolstadt and the Service Provider (SP) at FAU. The timestamps in the SAML response did not match the actual login times, leading to a `SAMLException` indicating that the response issue time was either too old or in the future.

## Diagnostic Steps
1. **Initial Report**: The user reported the issue via email, mentioning that the problem was specific to the FAU portal.
2. **Log Analysis**: HPC Admins analyzed the logs and found three failed login attempts with mismatched timestamps.
3. **Research**: The HPC Admin researched the error and found that it was likely due to a timezone mismatch between the IdP and SP servers.

## Solution
1. **Identify Timezone Mismatch**: The HPC Admin identified that the IdP at KU Eichstätt-Ingolstadt was likely set to UTC, while the SP at FAU was set to UTC+2 (Berlin/Europe).
2. **Contact IdP/SSO-Admin Team**: The HPC Admin suggested that the user contact their IdP/SSO-Admin team to check for any recent changes in timezone settings.
3. **Internal Check**: The HPC Admin also planned to check with their SSO-Admin team for any recent changes on their side.

## Outcome
The user acknowledged the issue and agreed to contact their IdP/SSO-Admin team to resolve the timezone mismatch.

## General Learnings
- **Timezone Settings**: Ensure that the timezone settings of the IdP and SP servers are synchronized to avoid timestamp mismatches.
- **Log Analysis**: Analyzing logs can provide valuable insights into the root cause of authentication issues.
- **Collaboration**: Effective communication and collaboration between different admin teams are crucial for resolving complex issues.

## References
- [Broadcom Knowledge Article](https://knowledge.broadcom.com/external/article/293730/response-issue-time-is-either-too-old-or.html)
- [MicroStrategy Community Article](https://community.microstrategy.com/s/article/Response-issue-time-is-either-too-old-or-with-date-in-the-future-skew-60-prevents-users-from-logging-in-using-SAML-authentication-in-MicroStrategy-10-6-and-above?language=en_US)
---

### 2022082342003516_SWFFT%20Jobs.md
# Ticket 2022082342003516

 # HPC Support Ticket Conversation: SWFFT Jobs

## Keywords
- SWFFT Jobs
- Process Pinning
- srun
- likwid-mpirun
- SSH Configuration
- ProxyJump
- Password Authentication
- SSH Key
- Hostname
- Job Script

## General Learnings
- Proper pinning of processes is crucial for efficient job execution.
- Using both `srun` and `likwid-mpirun` in the job script is not recommended.
- SSH configuration for accessing compute nodes can be complex and may require specific settings.
- The `IdentitiesOnly yes` option in SSH configuration can help in resolving authentication issues.
- ProxyJump can be used to access compute nodes, with the choice of jump host depending on the specific setup.

## Root Cause of the Problem
- The user's SWFFT jobs were not properly pinned, with most processes running on Hardware Thread 0 and others on Hardware Thread 36.
- The job script used both `srun` and `likwid-mpirun`, which is not recommended.
- The user had issues with SSH configuration, specifically with ProxyJump and authentication.

## Solution
- The user was advised to modify the job script to use `likwid-mpirun` correctly:
  ```bash
  likwid-mpirun -mpi slurm --mpiopts "--cpu-freq=2400000-2400000" ...
  ```
- The user was advised to check the pinning using `ps -ef | grep ^ptfs172h` on the compute nodes.
- The user was provided with guidance on SSH configuration, including the use of `IdentitiesOnly yes` and the correct ProxyJump settings.
- The user was directed to specific documentation and FAQs for further assistance with SSH configuration.

## Additional Notes
- The user was informed about potential imbalances between nodes, which might be due to the algorithm.
- The user was advised to use `cshpc` as the jump host for ProxyJump.
- The user was provided with a link to additional SSH documentation and templates.
---

### 2024031942001621_ssh%20connection%20stopped%20working.md
# Ticket 2024031942001621

 ```markdown
# HPC-Support Ticket: SSH Connection Stopped Working

## Keywords
- SSH
- Connection closed
- Remote host
- VIM
- Reconnect
- kex_exchange_identification

## Summary
User experienced intermittent SSH connection issues, with the terminal freezing, particularly while using VIM. Eventually, the user was unable to reconnect and received error messages indicating the connection was closed by the remote host.

## Root Cause
- Intermittent SSH connection issues leading to terminal freezing.
- Error message: `kex_exchange_identification: Connection closed by remote host`.

## Solution
- **Temporary Fix**: Close the terminal and attempt to reconnect.
- **Permanent Fix**: Not explicitly mentioned in the conversation. Further investigation by HPC Admins or 2nd Level Support team may be required to identify and resolve the underlying issue.

## Lessons Learned
- Intermittent SSH connection issues can lead to terminal freezing and eventual disconnection.
- Error messages such as `kex_exchange_identification: Connection closed by remote host` indicate a problem with the SSH connection.
- Users should be advised to close and reopen the terminal as a temporary fix while the issue is being investigated.

## Next Steps
- HPC Admins or 2nd Level Support team should investigate the root cause of the SSH connection issues.
- Ensure that the user's access and permissions are correctly configured.
- Monitor the SSH server logs for any anomalies or errors that could provide more insight into the issue.
```
---

### 2023080842003043_Re%3A%20Account%20und%20Paper.md
# Ticket 2023080842003043

 # HPC Support Ticket Conversation Analysis

## Keywords
- HPC Portal
- Account Renewal
- Email Address Mismatch
- Cluster Cockpit
- JupyterHub
- Paper Status

## General Learnings
- **Account Renewal Process**: Users need to log in to the HPC portal using their institutional identity. If there are attribute errors, they should be resolved by the local IT department.
- **Email Address Management**: Ensure the email address in the HPC portal matches the one used for communication. Admins can change the email address in the portal if needed.
- **Cluster Cockpit Access**: The link to the Cluster Cockpit can be found by navigating to the user's account in the HPC portal and expanding the desired account details.

## Root Cause of the Problem
- **Email Address Mismatch**: The user's email address in the HPC portal did not match the one used for communication, causing the invitation email to bounce.

## Solution
- **Email Address Update**: The HPC Admin updated the user's email address in the portal to match the one used for communication.
- **Cluster Cockpit Access**: The user was instructed to navigate to their account in the HPC portal and expand the account details to find the link to the Cluster Cockpit.

## Unresolved Issues
- The status of the paper mentioned in the conversation was not fully resolved within the provided conversation.

## Follow-up Actions
- The user should continue to monitor their account and email settings to prevent future mismatches.
- The HPC Admin should ensure that all users are aware of the account renewal process and the importance of keeping their email addresses up to date.

## Documentation for Support Employees
- **Account Renewal**: Guide users to log in to the HPC portal using their institutional identity. If they encounter attribute errors, advise them to contact their local IT department.
- **Email Address Management**: Verify that the user's email address in the HPC portal matches the one used for communication. If not, update it in the portal.
- **Cluster Cockpit Access**: Instruct users to navigate to their account in the HPC portal and expand the account details to find the link to the Cluster Cockpit.

This analysis provides a concise overview of the key points and solutions from the HPC support ticket conversation, which can be used to assist with similar issues in the future.
---

### 2024022942002817_Migration%20of%20mpt3001h%20HPC%20account%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20mand.md
# Ticket 2024022942002817

 # HPC Support Ticket Conversation Summary

## Subject
Migration of HPC account to new HPC portal / SSH keys become mandatory

## Keywords
- HPC account migration
- SSH keys
- HPC portal
- Single Sign-On (SSO)
- IdM portal
- SSH key types (RSA, ECDSA, ED25519)
- Usage statistics
- ClusterCockpit
- Jupyterhub

## General Learnings
- **Migration Process**: The HPC account is being migrated from the IdM portal to a new online HPC portal.
- **SSH Keys**: Access to HPC systems will require SSH keys starting March 11th. Accepted SSH key types are RSA (4096 bits), ECDSA (512 bits), and ED25519.
- **Portal Access**: The new HPC portal can be accessed at [https://portal.hpc.fau.de](https://portal.hpc.fau.de) using SSO with IdM credentials.
- **Account Validity**: The HPC portal will be the sole source for account validity starting from the end of February.
- **Usage Statistics**: The HPC portal will display usage statistics, which will also be visible to PIs and project managers.
- **ClusterCockpit and Jupyterhub**: Users should use the SSO link from within the HPC portal to access ClusterCockpit and Jupyterhub.

## Root Cause of the Problem
- The migration process requires users to switch to SSH keys for accessing HPC systems.

## Solution
- Generate one or more SSH key pairs with a passphrase and upload the SSH PublicKey to the HPC portal.
- Use the new HPC portal for account management and accessing services like ClusterCockpit and Jupyterhub.

## Additional Information
- Documentation and FAQs are available for users unfamiliar with SSH keys.
- Windows users are recommended to use OpenSSH built into the Windows (Power)Shell or MobaXterm instead of Putty.
- For account validity updates, users should contact their PI or project manager instead of filling out paper forms.
---

### 2022081042002818_Anfrage%20vom%20An%20Vuong%20Nguyen.md
# Ticket 2022081042002818

 # HPC Support Ticket Conversation Analysis

## Keywords
- HPC Account
- Password
- SSH Keys
- HPC Portal
- DFN AAI/SSO
- MobaXTerm
- HS-Coburg

## Problem
- User is unable to log in to HPC account via MobaXTerm due to lack of password.

## Root Cause
- Misunderstanding about the authentication method for HPC systems.

## Solution
- **HPC Portal Access:** Use HS-Coburg username and password through DFN AAI/SSO.
- **HPC System Access:** Use SSH keys, which need to be uploaded through the HPC portal. It typically takes 2 hours for SSH keys to be propagated to all HPC systems.

## References
- [NHR@FAU HPC Portal Usage](https://hpc.fau.de/systems-services/documentation-instructions/getting-started/nhrfau-hpc-portal-usage/)
- [SSH Secure Shell Access to HPC Systems](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/)

## General Learning
- HPC accounts do not use traditional passwords for access.
- Access to HPC systems is managed through SSH keys.
- The HPC portal is the central hub for managing SSH keys and other account settings.

## Roles Involved
- **HPC Admins:** Provided detailed instructions on accessing the HPC systems.
- **User:** Requested assistance with logging into the HPC account.

## Follow-Up
- Ensure the user follows the provided instructions and successfully logs into the HPC system.
- Monitor for any further issues related to SSH key propagation or portal access.
---

### 42018336_Probleme%20mit%20UNIX-Server.md
# Ticket 42018336

 # HPC Support Ticket: Probleme mit UNIX-Server

## Keywords
- SSH connection issue
- Permission denied
- Home directory access
- Wartungsarbeiten (maintenance work)
- Fileserver
- Nebenwirkungen (side effects)
- Dialogserver (dialog server)

## Problem Description
- User unable to access home directory via SSH.
- Error messages:
  - `Could not chdir to home directory /home/rrze/iwc2/iwc228: Permission denied`
  - `/usr/bin/X11/xauth: timeout in locking authority file /home/rrze/iwc2/iwc228/.Xauthority`
  - `Cannot open '/home/rrze/iwc2/iwc228/.mailrc': Permission denied`

## Root Cause
- Maintenance work on the central fileserver caused unforeseen side effects on some HPC systems, including `cshpc`.

## Temporary Solution
- Use the general dialog server `cssun`, which was not affected by the side effects.

## Final Resolution
- Maintenance work completed by the Solaris department resolved the issues on the affected HPC systems.

## Lessons Learned
- Maintenance work on central servers can have unexpected side effects on connected systems.
- Providing alternative servers can help users continue their work during such issues.
- Clear communication about maintenance work and its potential impacts is crucial.

## Action Taken
- HPC Admins acknowledged the issue and provided a temporary solution.
- The Solaris department completed the necessary maintenance work to resolve the issue.

## Follow-up
- No further action required as the issue was resolved.
---

### 2016040542002491_Problems%20login%20to%20Lima.md
# Ticket 2016040542002491

 # HPC Support Ticket: Problems Logging into Lima

## Keywords
- Login issue
- Lima
- SSH
- Connection reset by peer

## Problem Description
User encountered an issue while attempting to log in to Lima. The error message received was:
```
ssh_exchange_identification: read: Connection reset by peer
```

## Root Cause
The error indicates a problem with the SSH connection, possibly due to network issues, server overload, or misconfiguration.

## Solution
- **Check Network Connectivity**: Ensure that the user's network connection is stable.
- **Server Status**: Verify the status of the Lima server to ensure it is not overloaded or down.
- **SSH Configuration**: Review the SSH configuration on both the client and server sides for any misconfigurations.

## General Learnings
- SSH errors like "Connection reset by peer" can be caused by various factors including network issues, server load, or configuration problems.
- Always check network connectivity and server status as initial troubleshooting steps.
- Reviewing SSH configurations can help identify and resolve login issues.

## Next Steps
- If the issue persists, escalate to the HPC Admins for further investigation.
- Document any additional findings or solutions for future reference.
---

### 2022090742002699_Meggie%20Cluster%20Verbindung%20Problem.md
# Ticket 2022090742002699

 ```markdown
# HPC Support Ticket: Meggie Cluster Verbindung Problem

## Keywords
- SSH Connection Issue
- Remote Host Identification Changed
- Host Key Verification Failed
- Maintenance Downtime
- Key Update

## Problem Description
The user is unable to connect to the Meggie Cluster via SSH. The error message indicates that the remote host identification has changed, suggesting a possible man-in-the-middle attack or a change in the host key.

## Root Cause
- The Meggie Cluster was down for maintenance, and new keys were introduced as part of the maintenance process.

## Solution
1. **Check Maintenance Announcements**: Verify if the cluster is undergoing maintenance by checking the official announcements or emails.
2. **Remove Old Key**: Delete the old key for the Meggie Cluster from the `known_hosts` file located at `C:\\Users\\akatan/.ssh/known_hosts:10`.
3. **Retry Connection**: Attempt to reconnect to the Meggie Cluster after removing the old key.

## Additional Information
- **Maintenance Details**: For detailed information about the maintenance, refer to the official announcement at [RRZE Maintenance Announcement](https://www.rrze.fau.de/2022/08/wartungsankuendigung-hpc-systeme-fuer-den-5-9-2022/).
- **Contact Support**: If the issue persists, contact the HPC Support team for further assistance.

## Conclusion
The issue was resolved by removing the old key from the `known_hosts` file and retrying the connection after the maintenance period.
```
---

### 2022092742003472_scp%20und%20ssh%20auf%20Fritz.md
# Ticket 2022092742003472

 # HPC Support Ticket: scp und ssh auf Fritz

## Keywords
- `scp`
- `ssh`
- `Permission denied`
- `/dev/shm`
- `Headnode`
- `Rechenknoten`
- `passwortloses ssh`
- `Keyfile`

## Problem Description
- User is experiencing `Permission denied` errors when using `scp` and `ssh` between the headnode and compute nodes on the Fritz cluster.
- The issue does not occur on the Meggie cluster.
- The user does not have SSH keys set up.

## Root Cause
- Passwordless SSH between compute nodes was not yet activated on the Fritz cluster.
- Misunderstanding about the necessity of SSH keys or passwords for accessing compute nodes.

## Solution
- HPC Admins activated passwordless SSH between compute nodes on the Fritz cluster.
- Clarified that SSH login to compute nodes is possible while a job is running, but requires a password or keyfile.

## General Learnings
- Ensure passwordless SSH is enabled between compute nodes for seamless data transfer.
- Clarify SSH access requirements for users, especially regarding the use of passwords or keyfiles.
- Verify that all necessary file systems are available on both headnodes and compute nodes.

## Additional Notes
- The user was using `/dev/shm` as local scratch to reduce data transfer to disk.
- The user's script runs on the first of the requested nodes, not on the headnode.
- For Quantum Espresso, passwordless SSH between nodes is sufficient. For CPMD, additional considerations are needed for accessing output data in `/dev/shm`.
---

### 2024021442002158_Migration%20of%20capm%20HPC%20accounts%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20mandato.md
# Ticket 2024021442002158

 # HPC Support Ticket Summary

## Subject
Migration of HPC accounts to new HPC portal / SSH keys become mandatory

## Keywords
- HPC account migration
- SSH keys
- HPC portal
- Single Sign-On (SSO)
- IdM portal
- ClusterCockpit
- Jupyterhub

## Summary
- **Migration Process**: HPC accounts are being migrated from the IdM portal to a new online HPC portal.
- **SSH Keys**: Access to HPC systems will require SSH keys only. Accepted types are RSA (4096 bits), ECDSA (512 bits), and ED25519.
- **Portal Access**: The new HPC portal can be accessed at [https://portal.hpc.fau.de](https://portal.hpc.fau.de) using SSO with IdM credentials.
- **Usage Statistics**: Users can view their usage statistics, which are also visible to PIs and project managers.
- **ClusterCockpit and Jupyterhub**: Access these services via SSO links from within the HPC portal.

## Root Cause
- Users need to generate and upload SSH keys to the new HPC portal for continued access.

## Solution
- Generate SSH key pairs with a passphrase.
- Upload the public key to the HPC portal.
- Use the new HPC portal for account management and accessing services.

## Additional Information
- **Documentation**: [SSH Secure Shell Access](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/)
- **FAQs**: [HPC FAQs](https://hpc.fau.de/faqs/#ID-230)
- **Recommended Tools for Windows**: OpenSSH built into Windows (Power)Shell or MobaXterm.

## Closure
- The ticket was closed by the HPC Admin.
---

### 2024040442002137_Probleme%3A%20HPC%20Portal%20Login%20SSO%20mit%20anderer%20Institution.md
# Ticket 2024040442002137

 ```markdown
# HPC Support Ticket: SSO Login Issue with External Institution

## Keywords
- SSO Login
- HPC Portal
- External Institution
- Attribute Transfer
- IDM Verantwortlicher

## Problem Description
A guest student from ENS Paris Saclay is unable to log in to the HPC portal via SSO. The user receives an error during the SSO login process.

## Root Cause
The root cause of the problem is that no one from ENS Paris Saclay has previously logged in via SSO. The necessary attributes for SSO login are not being transferred correctly.

## Solution
- The IDM Verantwortlicher (Identity Management Responsible) at ENS Paris Saclay needs to be contacted to ensure that the required attributes are transferred to the HPC portal.
- Once the attributes are correctly transferred, the SSO login should function properly.

## Steps Taken
1. The user reported the SSO login issue via email.
2. HPC Admin responded, explaining that the issue is due to missing attribute transfer from ENS Paris Saclay.
3. The user was advised to contact the IDM Verantwortlicher at ENS Paris Saclay to resolve the attribute transfer issue.

## General Learning
- SSO login issues with external institutions often stem from missing or incorrect attribute transfers.
- The IDM Verantwortlicher at the external institution needs to be involved to ensure proper attribute transfer.
- This is typically a straightforward process once the correct attributes are configured.
```
---

### 2022041542000283_Problem%20Emmy%20Cluster%20Zugang.md
# Ticket 2022041542000283

 ```markdown
# HPC Support Ticket: Problem Emmy Cluster Zugang

## Keywords
- SSH Login Issue
- Emmy Cluster
- Connection Closed by Remote Host
- SSH-Hostkeys Permissions
- Perceus

## Summary
A user reported an issue with SSH login to the Emmy Cluster, receiving the error message "kex_exchange_identification: Connection closed by remote host."

## Root Cause
The issue was system-related. During maintenance work on `e015[2-6]`, Perceus encountered an error that corrupted its internal database and altered the permissions on the SSH-Hostkeys, causing the SSH daemon to refuse connections.

## Solution
The HPC Admin team identified and resolved the issue with the SSH-Hostkeys permissions, restoring normal SSH login functionality.

## Lessons Learned
- System maintenance can inadvertently affect SSH login functionality.
- Regular monitoring and quick response to user reports are crucial for maintaining system accessibility.
- Proper handling of SSH-Hostkeys permissions is essential for ensuring secure and reliable SSH access.
```
---

### 2024061542000598_Cannot%20login%20on%20Alex%20using%20terminal%20and%20cannot%20log%20in%20VSCode.md
# Ticket 2024061542000598

 ```markdown
# HPC Support Ticket: Cannot Login on Alex Using Terminal and Cannot Log in VSCode

## Keywords
- Login issues
- SSH configuration
- VSCode connection
- Account access

## Problem Summary
- User unable to log in to `alex.nhr.fau.de` via terminal but can log in to `tinyx.nhr.fau.de`.
- VSCode fails to connect when entering the passphrase for both `tinyx` and `alex`.

## Root Cause
1. **Account Access**: User's account is not enabled on `alex`.
2. **SSH Configuration**: Misconfiguration in `ssh_config` file, attempting to log in with the username `hpcaccount` instead of the user's actual account.
3. **VSCode Configuration**: Potential misconfiguration or cached settings in VSCode causing connection issues.

## Solution
1. **Account Access**:
   - User needs to contact their advisor or colleague to get access to `alex`.

2. **SSH Configuration**:
   - Update the `ssh_config` file to use the correct username (`iwi5215h`).

3. **VSCode Configuration**:
   - Remove the VSCode remote targets and add them again to refresh the connection settings.
   - Seek additional help from the user's group if the issue persists.

## Additional Resources
- Onboarding repository for further assistance: [i5_cluster_onboarding](https://gitos.rrze.fau.de/ym60imaq/i5_cluster_onboarding)

## Notes
- For student projects, `tinyGPU` is usually sufficient.
- If the connection with SSH on the command line works, the issue in VSCode is likely a configuration problem.
```
---

### 2024101742003387_ssh%20Verbindung%20zu%20tinyx.md
# Ticket 2024101742003387

 # HPC Support Ticket: SSH Connection Issue to tinyx

## Keywords
- SSH
- Mac Terminal
- tinyx
- csnhr
- ProxyJump
- Publickey Authentication

## Problem Description
The user was experiencing difficulties connecting to `tinyx.nhr.fau.de` via SSH using the Mac Terminal. The connection to `csnhr.nhr.fau.de` was successful, but the user was receiving a "Permission denied (publickey,hostbased)" error when attempting to connect to `tinyx`.

## Root Cause
The user was attempting to initiate the SSH connection to `tinyx` from the `csnhr` server instead of their local machine. This manual approach bypassed the necessary ProxyJump configuration, leading to authentication failures.

## Solution
The HPC Admin advised the user to run the SSH command from their local machine, utilizing the ProxyJump configuration in their SSH config file. This approach allows the SSH client to handle the connection through the proxy server automatically.

## Steps to Resolve
1. Ensure the SSH config file (`~/.ssh/config`) is correctly set up with the ProxyJump directive.
2. Run the SSH command from the local machine:
   ```sh
   ssh tinyx.nhr.fau.de
   ```

## Lessons Learned
- Always initiate SSH connections from the local machine when using ProxyJump.
- The Mac Terminal is suitable for SSH connections; the issue was not related to the terminal application.
- Proper configuration of the SSH client is crucial for successful connections through proxy servers.

## Additional Notes
- The user's SSH config file was correctly set up, but the method of initiating the connection was incorrect.
- The HPC Admin provided a clear explanation and solution, which resolved the user's issue promptly.
---

### 2024010542000197_Invitation%20issues%20-%20v101be.md
# Ticket 2024010542000197

 # HPC Support Ticket: Invitation Issues - v101be

## Keywords
- HPC access
- Invitation issues
- SSO email mismatch
- Alex cluster access
- FAQ reference

## Summary
A user reported not seeing invitations on their account despite receiving emails about them. The root cause was an email mismatch during the SSO login process.

## Root Cause
- The invitation email (`kadraa@cs.uni-freiburg.de`) did not match the email transmitted by the IdP during SSO (`arlindkadra@gmail.com`).

## Solution
- The HPC Admin updated the invitation email to match the one transmitted by the IdP.
- The user was instructed to check the transmitted email in the "Personal data" box on the HPC portal.

## Additional Notes
- Access to the Alex cluster is automatically enabled for the project v101be but takes until the morning after accepting the invitation to be fully set up.
- Reference to FAQ for login issues: [FAQ Link](https://hpc.fau.de/faqs/#i-managed-to-log-in-to-cshpc-with-an-ssh-key-but-get-asked-for-a-password-when-continuing-to-a-cluster-frontend)
- The user inquired about access to the Alex cluster for experiments involving transformers, which was confirmed to be automatically enabled.

## Follow-up
- A follow-up email discussed resolving the SSO authentication issue and confirmed that the users could start submitting jobs to the Alex cluster.
- The Head of the Datacenter inquired about any issues in using the infrastructure and offered assistance.

This documentation can be used to resolve similar invitation and email mismatch issues in the future.
---

### 2024082742001043_Login%20Probleme%20Fritz.md
# Ticket 2024082742001043

 # HPC Support Ticket: Login Probleme Fritz

## Keywords
- Login problems
- SSH configuration
- Hostname resolution
- Jumphost decommissioning

## Problem Description
Users in project `b165da` encountered login issues on the HPC system `Fritz`. The error messages included:
- `ssh: Could not resolve hostname cshpc.rrze.fau.de: Name or service not known`
- `ssh_exchange_identification: Connection closed by remote host`

## Root Cause
The users were attempting to connect via a jumphost (`cshpc.rrze.fau.de`) that had been decommissioned at the end of July, as announced multiple times.

## Solution
- Update the SSH configuration to replace all instances of the decommissioned hostname (`cshpc.rrze.fau.de`) with the new hostname (`csnhr.nhr.fau.de`).
- Refer to the official announcement for more details: [Dialog Server cshpc Decommissioned](https://hpc.fau.de/2024/08/01/dialog-server-cshpc-decommissioned-nomachine-nx-to-be-replaced-by-xrdp/)

## General Learnings
- Ensure users are aware of and follow announcements regarding system changes.
- Regularly update SSH configurations to reflect current hostnames and settings.
- Communicate effectively with users to resolve login issues promptly.
---

### 2024111042000015_Re%3A%20New%20invitation%20for%20%22Tier3-Grundversorgung%20Universit%C3%83%C2%A4t%20Bamberg%22%20wa.md
# Ticket 2024111042000015

 # HPC Support Ticket Analysis

## Keywords
- SSO Configuration
- Email Invitation
- SSO Identity
- IdM Credentials
- SSH Public Key
- HPC Portal

## Problem
- **Root Cause**: The SSO configuration was repaired, but the invitation was sent to an incorrect email address (`marcni@zedat.fu-berlin.de`) instead of the correct one (`marc.nickert@berlin.de`).
- **User Issue**: The user has not received the invitation to accept due to the incorrect email address.

## Solution
- **Admin Response**: The user was advised to request a new invitation from the project initiator (Alexander Raab) to the correct email address.

## General Learnings
- Ensure that email addresses are correctly entered when sending invitations.
- Users should verify their email addresses and notify support if there are discrepancies.
- SSO configurations should be thoroughly checked to avoid such issues.

## Steps for Support Employees
1. Verify the email address used for the invitation.
2. Advise the user to request a new invitation to the correct email address.
3. Ensure the user follows the steps to accept the invitation and upload the SSH public key.

## References
- [HPC Portal Documentation](https://doc.nhr.fau.de/hpc-portal/)
- [HPC Support Email](mailto:hpc-support@fau.de)

## Roles Involved
- **HPC Admins**: Provide support and guidance.
- **2nd Level Support Team**: Assist with technical issues.
- **Head of the Datacenter**: Oversee datacenter operations.
- **Training and Support Group Leader**: Manage training and support activities.
- **NHR Rechenzeit Support**: Handle computing time support and grant applications.
- **Software and Tools Developer**: Develop and maintain software tools.
---

### 2023011942003231_Re%3A%20New%20invitation%20for%20%22Projektpartner%20Tier3-Grundversorgung%20Professur%20f%C3%83%C2%.md
# Ticket 2023011942003231

 ```markdown
# HPC Support Ticket Analysis

## Subject
Re: New invitation for "Projektpartner Tier3-Grundversorgung Professur für Hochleistungsrechnen" waiting at portal.hpc.fau.de

## User Issue
- **SSH Access**: User can SSH into `ihpc107h@cshpc.rrze.fau.de` but encounters issues when attempting to hop onto `Alex` or `Fritz` using the same account and identity file (SSH key).

## Keywords
- SSH
- Identity File
- SSH Key
- Access Issues
- Hopping

## Root Cause
- The user is experiencing SSH access issues when trying to connect to `Alex` or `Fritz` from `ihpc107h@cshpc.rrze.fau.de`.

## Solution
- **Not Found**: The solution is not explicitly mentioned in the provided conversation. Further investigation by HPC Admins or 2nd Level Support team is required.

## General Learnings
- Ensure SSH keys and configurations are correctly set up for hopping between different HPC nodes.
- Verify access permissions and configurations on target nodes (`Alex`, `Fritz`).

## Next Steps
- HPC Admins or 2nd Level Support team should investigate the SSH configuration and access permissions on `Alex` and `Fritz`.
- Verify the user's SSH key and ensure it is correctly propagated across the required nodes.
```
---

### 2024081542001904_Can%27t%20connect%20to%20fritz.md
# Ticket 2024081542001904

 ```markdown
# HPC Support Ticket: Can't Connect to Fritz

## Keywords
- SSH connection issue
- Frontend nodes
- .ssh/config file
- Hanging connection
- Error after passphrase entry

## Problem Description
The user is unable to connect to `mfbi005h@fritz.nhr.fau.de`. After entering the key passphrase, the connection hangs and eventually gives an error. Connections to other machines (e.g., alex/woody) work fine.

## Root Cause
One of the frontend nodes (`fritz3`) is experiencing problems. The generic `ssh fritz` command attempts to connect to a problematic node.

## Solution
- Explicitly log in to other functional frontend nodes (e.g., `ssh fritz1`).
- Update the `.ssh/config` file to specify the working frontend node.

## Steps Taken
1. User reported the issue with detailed SSH log.
2. HPC Admin identified the problematic frontend node (`fritz3`).
3. User successfully connected to `fritz1` and updated their `.ssh/config` file.

## General Learnings
- Always check the status of individual frontend nodes when experiencing connection issues.
- Update the `.ssh/config` file to specify working nodes to avoid generic connection attempts.
```
---

### 2022082542001229_Re%3A%20%5BWWU%2320220825177%5D.md
# Ticket 2022082542001229

 # HPC Support Ticket Conversation Analysis

## Keywords
- REFEDS Research and Scholarship (R&S)
- DFN AAI metadata management
- SSO-Attributes
- FAU HPC-Portal
- Entity ID
- eduPersonPrincipalName, mail, givenName, sn, eduPersonScopedAffiliation
- mdui:DisplayName, mdui:InformationURL

## General Learnings
- The REFEDS Research and Scholarship (R&S) entity category simplifies attribute release for Service Providers.
- The FAU HPC-Portal requires specific attributes to be released by Identity Providers.
- The DFN AAI metadata management system is used to request and manage entity categories.
- The process involves verifying the Service Provider and entity ID, and ensuring the required attributes are correctly configured.

## Root Cause of the Problem
- The user, Sara Maskri, requested computational time on the FAU HPC but encountered issues with attribute transfer from the Uni-Münster IdP to the FAU HPC portal.

## Solution
- The FAU administrators were advised to request the REFEDS Research and Scholarship (R&S) entity category for their Service Provider.
- Once the entity category is granted by the DFN AAI team, most Identity Providers will automatically release the required attributes.
- The attributes mdui:DisplayName and mdui:InformationURL were added to the DFN-AAI metadata to comply with the REFEDS R&S requirements.

## Actions Taken
- The HPC Admins confirmed the Service Provider and entity ID with the user's IT department.
- The HPC Admins requested the REFEDS R&S entity category for the FAU HPC-Portal.
- The attributes mdui:DisplayName and mdui:InformationURL were configured and added to the DFN-AAI metadata.

## Conclusion
- The REFEDS R&S entity category simplifies the process of attribute release and reduces the need for manual configuration by Identity Providers.
- Ensuring the correct attributes are configured and the entity category is requested can resolve attribute transfer issues for HPC users.
---

### 2023103042001936_Broken%20URL%20_%20Re%3A%20New%20invitation%20for%20%22NHR_BayernKI-Basisprojekt%20KU-Eichst%C3%83%C.md
# Ticket 2023103042001936

 # HPC-Support Ticket Conversation Summary

## Subject: Broken URL / Re: New invitation for "NHR/BayernKI-Basisprojekt KU-Eichstätt" waiting at portal.hpc.fau.de

### Keywords:
- Broken URL
- Email Invitation
- Plain-Text Email
- Mail Client Issues
- Outlook for Mac
- Safari Issues
- Portal Update
- Einladungen Löschen

### General Learnings:
- **Email Client Dependency**: Issues with email links can be client-specific.
- **Plain-Text Email**: Plain-text emails can be misinterpreted by some email clients.
- **Browser Issues**: Specific browser versions can cause display issues on the portal.
- **Invitation Management**: Users cannot currently delete invitations themselves.

### Root Cause of the Problem:
- **Broken URL**: The invitation email contained a broken URL due to misplaced quotation marks.
- **Mail Client Issue**: Outlook for Mac (Version 16.78.2) caused the URL to be misinterpreted.
- **Safari Issues**: Safari 17.1 caused display issues on the portal due to recent updates.

### Solutions:
- **Remove Quotation Marks**: The HPC Admins decided to remove quotation marks around URLs in the next portal update to avoid URL issues.
- **Use Different Browser**: The user switched to Chrome to avoid Safari-specific display issues.
- **Manual Invitation Deletion**: The HPC Admins manually deleted specific invitations upon user request.

### Detailed Conversation:

#### User:
- Reported broken URL in invitation email.
- Identified issue with Outlook for Mac.
- Noted display issues in Safari due to recent updates.
- Requested information on deleting invitations.

#### HPC Admins:
- Confirmed that emails are sent as plain-text.
- Suggested removing quotation marks around URLs.
- Provided a list of pending invitations and offered to delete specific ones.
- Confirmed deletion of a specific invitation.

#### 2nd Level Support Team:
- Not directly involved in this conversation.

#### Other Roles:
- Not directly involved in this conversation.

### Conclusion:
- The issue with the broken URL was resolved by planning to remove quotation marks in the next portal update.
- The user was advised to use Chrome to avoid Safari-specific display issues.
- The HPC Admins manually deleted specific invitations as requested by the user.
---

### 2024021942002925_Migration%20of%20mp24%20HPC%20accounts%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20mandato.md
# Ticket 2024021942002925

 # HPC Support Ticket: Migration of HPC Accounts to New Portal / SSH Keys Mandatory

## Keywords
- HPC account migration
- SSH keys
- HPC portal
- IdM portal
- Single Sign-On (SSO)
- SSH key types (RSA, ECDSA, ED25519)
- Usage statistics
- ClusterCockpit
- Jupyterhub

## Summary
The HPC services at FAU are migrating existing HPC accounts to a new online HPC portal. This migration involves several changes, including the mandatory use of SSH keys for access and the introduction of a new portal for account management.

## Key Points
- **Migration to New HPC Portal**: The new HPC portal can be accessed at [https://portal.hpc.fau.de](https://portal.hpc.fau.de) using Single Sign-On (SSO) with IdM credentials.
- **SSH Keys Mandatory**: Starting from the end of February, access to HPC systems will require SSH keys. Accepted SSH key types are RSA (at least 4096 bits), ECDSA (512 bits), and ED25519.
- **SSH Key Generation and Upload**: Users need to generate SSH key pairs with a passphrase and upload the public key to the HPC portal. It may take up to two hours for all HPC systems to recognize the updated keys.
- **Documentation and FAQs**: Users unfamiliar with SSH keys can refer to the documentation and FAQs provided.
- **Windows Users**: Recommended to use OpenSSH built into Windows (Power)Shell or MobaXterm instead of Putty.
- **IdM Portal Expiration**: Users will receive an email about the expiration of their HPC service in the IdM portal, which can be ignored. The HPC portal will be the sole source for account validity.
- **Account Validity Update**: Users no longer need to fill in paper forms to update account validity. They should contact their PI or project manager.
- **Usage Statistics**: The HPC portal will display usage statistics, which will also be visible to PIs and project managers.
- **ClusterCockpit and Jupyterhub**: Users should use the Single Sign-On link from within the HPC portal to access ClusterCockpit and Jupyterhub.

## Root Cause of the Problem
- The migration process requires users to adapt to a new system for account management and access, which involves learning about and using SSH keys.

## Solution
- Users should follow the instructions provided to generate and upload SSH keys, and use the new HPC portal for account management and accessing services like ClusterCockpit and Jupyterhub.

## Additional Resources
- [SSH Secure Shell Access Documentation](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/)
- [FAQs](https://hpc.fau.de/faqs/#ID-230)

This documentation will help support employees understand the migration process and assist users with any related issues.
---

### 2024030642000833_Fwd%3A%20New%20invitation%20for%20%22LS%20Datenbanksysteme%20und%20Data%20Mining%20-%20LMU%22%20wait.md
# Ticket 2024030642000833

 # HPC Support Ticket Analysis

## Keywords
- Invitation not received
- Project invitation
- SSO (Single Sign-On)
- IdM credentials
- Email mismatch
- SSH public key

## Summary
A user reported not receiving an invitation to a project despite following the provided instructions. The root cause was identified as a mismatch between the email address used for the invitation and the email address transmitted by the user's SSO provider.

## Root Cause
- **Email Mismatch**: The invitation was sent to an email address different from the one transmitted by the user's SSO provider, leading to the invitation not being matched correctly.

## Solution
- Ensure that invitations are sent to the email address transmitted by the user's SSO provider. This requires coordination between the project inviter and the user to confirm the correct email address.

## General Learnings
- **Email Consistency**: It is crucial to ensure that the email address used for invitations matches the one used by the SSO provider to avoid mismatches.
- **SSO Integration**: Understanding how the SSO provider transmits user data is essential for troubleshooting such issues.
- **User Communication**: Clear communication with the user about the email address used for SSO can help prevent such issues.

## Steps for Future Reference
1. **Verify Email Address**: Confirm the email address used by the SSO provider.
2. **Send Invitation**: Ensure the invitation is sent to the correct email address.
3. **User Instructions**: Provide clear instructions to the user on how to accept the invitation and upload the SSH public key.

By following these steps, similar issues can be avoided in the future.
---

### 2024120642002351_Unable%20to%20connect%20via%20ssh.md
# Ticket 2024120642002351

 # HPC Support Ticket: Unable to Connect via SSH

## Keywords
- SSH
- Connection Issue
- Public Key Authentication
- Known Hosts
- OpenSSH
- Windows
- Verbose Output

## Problem Description
The user is unable to connect to the HPC cluster via SSH. The verbose output of the SSH command shows that the connection is established but authentication fails.

## Root Cause
The root cause of the problem is the failure of public key authentication. The SSH client offers a public key, but the server does not accept it.

```
debug1: Authentications that can continue: publickey
debug1: Offering public key: C:\\Users\\Admin/.ssh/id_ed25519_nhr_fau
debug2: we sent a publickey packet, wait for reply
debug1: Authentications that can continue: publickey
debug2: we did not send a packet, disable method
debug1: No more authentication methods to try.
Permission denied (publickey).
```

## Possible Solutions
1. **Verify Public Key**: Ensure that the public key (`id_ed25519_nhr_fau.pub`) is correctly added to the authorized keys on the server.
2. **Check Key Permissions**: Ensure that the private key file (`id_ed25519_nhr_fau`) has the correct permissions (`600`).
3. **SSH Agent**: Ensure that the SSH agent is running and the key is added to the agent.
4. **Known Hosts**: Ensure that the server's host key is correctly added to the `known_hosts` file.

## Additional Notes
- The user is using OpenSSH for Windows.
- The server's host key algorithm is `ssh-ed25519`.
- The client and server agree on the key exchange algorithm `curve25519-sha256`.

## Follow-up Actions
- If the problem persists, escalate to the HPC Admins for further investigation.
- Update the user documentation to include troubleshooting steps for SSH public key authentication issues.
---

### 2024030142000744_Unerwartete%20K%C3%83%C2%BCndigung%20meines%20HPC-Accounts.md
# Ticket 2024030142000744

 # HPC Support Ticket: Unerwartete Kündigung des HPC-Accounts

## Problem
- **User:** Account `iwi5142h` wurde unerwartet gekündigt.
- **Erwartetes Kündigungsdatum:** 31. März
- **Tatsächliches Kündigungsdatum:** 29. Februar
- **Antragseingang:** 10. Dezember

## Ursache
- **Migration:** Account wurde auf ein neues Verwaltungsportal umgestellt.
- **SSH-Keys:** Verwendung von SSH-Keys ist jetzt zwingend notwendig.

## Lösung
1. **Email-Benachrichtigung:**
   - User sollte eine Email am 22. Februar um 14:18 mit dem Betreff "Migration of iwi5 HPC accounts to new HPC portal / SSH keys become mandatory" erhalten haben.

2. **SSH-Key Generierung:**
   - SSH-Key-Paar generieren: `ssh-keygen -t ed25519 -f ~/.ssh/id_ed2559_nhr_fau`
   - Sicheres Passwort setzen.
   - Öffentlichen Schlüssel (`.pub`) ins HPC-Portal hochladen.

3. **SSH-Konfiguration:**
   - SSH-Konfigurationsdatei (`~/.ssh/config`) anpassen:
     ```plaintext
     Host alex.nhr.fau.de
         HostName alex.nhr.fau.de
         User <HPC account>
         ProxyJump csnhr.nhr.fau.de
         IdentityFile ~/.ssh/id_ed2559_nhr_fau
         IdentitiesOnly yes
         PasswordAuthentication no
         PreferredAuthentications publickey
         ForwardX11 no
         ForwardX11Trusted no
     ```
   - Ähnliche Änderungen für `tinyx.nhr.fau.de` vornehmen.

4. **Verbindung testen:**
   - Verbindung mit `ssh alex.nhr.fau.de` testen.
   - Bei Fehlern wie "Connection refused" oder "Permission denied" überprüfen, ob der SSH-Key korrekt hochgeladen und konfiguriert wurde.

## Unterstützung
- **HPC Admins:** Unterstützung bei der Konfiguration und Fehlerbehebung.
- **2nd Level Support Team:** Weitere Unterstützung bei komplexeren Problemen.

## Dokumentation
- **SSH-Konfiguration:** [Dokumentation](https://doc.nhr.fau.de/access/ssh-command-line/)
- **HPC-Portal:** [Dokumentation](https://doc.nhr.fau.de/hpc-portal/#the-user-tab)
- **MobaXterm und VSCode:** [Dokumentation](https://doc.nhr.fau.de/access/ssh-mobaxterm/) bzw. [Dokumentation](https://doc.nhr.fau.de/access/ssh-vscode/)

## Fazit
- **Root Cause:** Migration und neue SSH-Key-Anforderungen.
- **Lösung:** SSH-Key generieren, hochladen und SSH-Konfiguration anpassen.
- **Unterstützung:** HPC Admins und 2nd Level Support Team.
---

### 2024082042002546_Issue%20with%20SSH%20Login.md
# Ticket 2024082042002546

 ```markdown
# Issue with SSH Login

## Keywords
- SSH Login
- Public Key
- Config File
- ProxyJump
- IPv4/IPv6
- VPN

## Summary
The user was unable to log in via SSH from their work computer in Berlin, despite being able to log in from their laptop without issues. The problem was eventually resolved by adding the correct configuration for the jump host in the `.ssh/config` file.

## Root Cause
- The `.ssh/config` file on the user's work computer was not correctly set up to include the jump host (`csnhr.nhr.fau.de`).
- The user's IP address and VPN connection were causing issues with the SSH login.

## Steps Taken
1. **Initial Diagnosis**: The user followed the instructions provided on the HPC portal to add their university computer to SSH but encountered a password prompt.
2. **Key Upload**: The user uploaded their public key to the HPC portal, but there were file system issues that might have affected key distribution.
3. **Debugging**: The user was asked to provide the output of the SSH login with the debugging option (`ssh -vv`).
4. **Config File Review**: The HPC Admin reviewed the user's `.ssh/config` file and identified that the jump host configuration was missing.
5. **Solution**: The user added the missing configuration for the jump host (`csnhr.nhr.fau.de`) to their `.ssh/config` file, which resolved the issue.

## Solution
Add the following configuration to the `.ssh/config` file:

```plaintext
Host csnhr.nhr.fau.de csnhr
    HostName csnhr.nhr.fau.de
    User p101ae10
    IdentityFile ~/.ssh/id_ed25519_nhr_fau
    IdentitiesOnly yes
    PasswordAuthentication no
    PreferredAuthentications publickey
    ForwardX11 no
    ForwardX11Trusted no
```

## Conclusion
The issue was resolved by ensuring the `.ssh/config` file included the correct configuration for the jump host. This is particularly important when connecting via VPN or different IP addresses.
```
---

### 2023053042003659_Migration%20of%20bccc%2A%20HPC%20accounts%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20mand.md
# Ticket 2023053042003659

 # HPC Support Ticket: Migration of HPC Accounts to New Portal / SSH Keys Mandatory

## Keywords
- HPC account migration
- SSH keys
- HPC portal
- Single Sign-On (SSO)
- IdM portal
- Passphrase
- RSA, ECDSA, ED25519
- OpenSSH
- MobaXterm
- Putty
- ClusterCockpit
- Jupyterhub

## Summary
- **Migration Process**: Existing HPC accounts are being migrated to a new online HPC portal.
- **Access Change**: By mid-June, access to HPC systems will require SSH keys only.
- **SSH Key Requirements**: RSA (4096 bits), ECDSA (512 bits), ED25519.
- **Portal Access**: Login via SSO using IdM credentials.
- **Usage Monitoring**: Users, PIs, and project managers can view usage statistics.
- **Tool Access**: ClusterCockpit and Jupyterhub access via SSO links within the HPC portal.

## Root Cause
- Expiration of certificates and migration to a new HPC portal necessitating SSH key authentication.

## Solution
- **Generate SSH Keys**: Users must generate SSH key pairs with a passphrase and upload the public key to the HPC portal.
- **Documentation**: Refer to the provided documentation and FAQs for guidance on SSH key generation and usage.
- **Ignore IdM Expiration**: Users can ignore automatic messages about HPC service expiration in the IdM portal.
- **Account Validity**: Contact the PI or project manager to update HPC account validity.

## Additional Notes
- **Windows Users**: Recommended to use OpenSSH built into Windows (Power)Shell or MobaXterm instead of Putty.
- **ClusterCockpit and Jupyterhub**: Access via SSO links within the HPC portal for updated instances.

## References
- [HPC Portal](https://portal.hpc.fau.de)
- [SSH Documentation](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/)
- [FAQs](https://hpc.fau.de/faqs/#ID-230)
---

### 2024042242001578_SSH%20connection.md
# Ticket 2024042242001578

 # HPC Support Ticket: SSH Connection Issue

## Keywords
- SSH connection
- Laptop
- Institute-provided device
- Office computer
- SSH command line
- id_ed2559_nhr_fau
- iww8019h@tinyx.nhr.fau.de

## Problem Description
The user is unable to connect to the HPC from an institute-provided laptop (WW8) using SSH, despite following the instructions provided in the documentation. The same SSH command works perfectly from the user's office computer at the institute.

## Root Cause
The root cause of the problem is not explicitly identified in the conversation. However, potential issues could include:
- Network restrictions on the laptop
- Incorrect SSH key configuration on the laptop
- Differences in the network environment between the laptop and the office computer

## Solution
No solution is provided in the conversation. Further investigation is needed to identify the root cause and provide a solution.

## General Learnings
- SSH connection issues can be specific to the device or network environment.
- It is important to verify that the SSH key and configuration are correctly set up on the device experiencing the issue.
- Network restrictions or differences in network environments can affect SSH connectivity.

## Next Steps
- Verify the SSH key and configuration on the laptop.
- Check for any network restrictions or differences between the laptop and the office computer.
- Consult with the 2nd Level Support team or HPC Admins for further assistance if needed.
---

### 2024022742000681_AW%3A%20New%20invitation%20for%20%22Studentische%20Abschlu%C3%83%C2%9Farbeiten%20Tier3%20Grundversor.md
# Ticket 2024022742000681

 # HPC Support Ticket Analysis

## Keywords
- HPC Portal
- Invitation
- Email Address
- SSO Login
- SSH Public Key
- IDM Credentials

## Problem Description
- User received an invitation to a project via an email address not associated with the FAU domain (outlook.de).
- User was unable to find the invitation on the HPC portal after logging in with their IDM credentials.

## Root Cause
- The invitation was sent to an email address outside the FAU domain, which is not recognized by the HPC portal.

## Solution
- The user was advised to use their FAU email address for the invitation.
- The HPC Admin confirmed that the invitation would be resent to the user's FAU email address.
- No need to resubmit the application form.

## General Learnings
- Ensure that all communications and invitations are sent to email addresses within the FAU domain.
- Users should log in to the HPC portal using their IDM credentials and check the 'User' -> 'Your Invitations' section for pending invitations.
- After accepting the invitation, users should upload an SSH public key to their corresponding account.

## Roles Involved
- **HPC Admins**: Provided guidance and resolved the issue by resending the invitation to the correct email address.
- **User**: Reported the problem and followed the instructions provided by the HPC Admins.

## Additional Resources
- Further information can be found at: [HPC Portal Documentation](https://doc.nhr.fau.de/hpc-portal/)
- For any issues, users should send an email with a clear description of the problem to 'hpc-support@fau.de'.
---

### 2024022342001123_Migration%20of%20iwso%20HPC%20accounts%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20mandato.md
# Ticket 2024022342001123

 # HPC Support Ticket: Migration of HPC Accounts to New Portal / SSH Keys Mandatory

## Keywords
- HPC account migration
- SSH keys
- HPC portal
- Single Sign-On (SSO)
- IdM portal
- Passphrase
- RSA, ECDSA, ED25519
- ClusterCockpit
- Jupyterhub

## Summary
The HPC Admin team announced the migration of existing HPC accounts to a new online HPC portal. Users are required to generate and upload SSH keys for future access. The IdM portal will no longer manage HPC account validity.

## Key Points
- **Migration to New HPC Portal**: Access the new portal using SSO with IdM credentials.
- **SSH Keys Mandatory**: Generate and upload SSH keys (RSA 4096 bits, ECDSA 512 bits, ED25519) with a passphrase.
- **Account Validity**: The new HPC portal will manage account validity; ignore IdM portal expiration messages.
- **Usage Statistics**: PIs and project managers can view usage statistics.
- **ClusterCockpit and Jupyterhub**: Use SSO links from the HPC portal for access.

## User Responses
- **Out of Office**: Users responded with out-of-office messages, indicating limited access to emails during the migration period.
- **Part-Time PhD**: One user mentioned completing their PhD part-time, expecting delays in email responses.

## Solutions
- **SSH Key Generation**: Users should generate SSH keys and upload the public key to the HPC portal.
- **SSO Access**: Use SSO links for ClusterCockpit and Jupyterhub access.
- **Account Management**: Contact PIs or project managers for account validity updates.

## Documentation Links
- [SSH Secure Shell Access to HPC Systems](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/)
- [FAQs](https://doc.nhr.fau.de/faq/#ssh)

## Notes for Support Employees
- Ensure users are aware of the migration process and the importance of generating SSH keys.
- Provide guidance on using SSO links for accessing ClusterCockpit and Jupyterhub.
- Direct users to contact their PIs or project managers for account validity updates.
---

### 2024021842000394_Migration%20of%20fhn0_fhng%20HPC%20accounts%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20ma.md
# Ticket 2024021842000394

 # HPC Support Ticket: Migration of HPC Accounts to New Portal / SSH Keys Mandatory

## Keywords
- HPC account migration
- SSH keys
- HPC portal
- Single Sign-On (SSO)
- IdM portal
- ClusterCockpit
- Jupyterhub
- Account validity
- Usage statistics

## Summary
The HPC services at FAU are migrating existing HPC accounts to a new online HPC portal. This migration involves several changes, including the mandatory use of SSH keys for access and the decoupling of the IdM portal from the new HPC portal.

## Key Points
- **New HPC Portal**: Accessible at [https://portal.hpc.fau.de](https://portal.hpc.fau.de). Login with SSO using IdM credentials.
- **SSH Keys**: Mandatory for access starting end of February. Accepted types are RSA (4096 bits), ECDSA (512 bits), and ED25519.
- **Account Validity**: Managed through the new HPC portal. Users should contact their PI or project manager for updates.
- **Usage Statistics**: Visible to users, PIs, and project managers.
- **ClusterCockpit and Jupyterhub**: Accessible via SSO links from within the HPC portal.

## User Responses
- **User 1**: Acknowledged the message and mentioned their availability starting March 4, 2024.
- **User 2**: Informed about their unavailability until February 26, 2024, and provided contact information for urgent matters.

## Root Cause of the Problem
- **Migration Process**: Users need to adapt to the new portal and SSH key requirements.
- **Communication**: Ensuring users are aware of the changes and how to update their account validity.

## Solution
- **SSH Key Generation**: Users should generate SSH key pairs with passphrases and upload the public key to the HPC portal.
- **Account Management**: Users should contact their PI or project manager for account validity updates.
- **Documentation**: Users unfamiliar with SSH keys should refer to the provided documentation and FAQs.

## Additional Notes
- **Windows Users**: Recommended to use OpenSSH built into Windows (Power)Shell or MobaXterm instead of Putty.
- **IdM Portal**: Users can ignore automatic messages about HPC service expiration in the IdM portal.

## Conclusion
The migration to the new HPC portal requires users to adapt to new access methods and account management procedures. Proper communication and documentation are essential to ensure a smooth transition.
---

### 2023041142002858_WG%3A%20%28extern%29%20Fwd%3A%20Information%20%C3%83%C2%BCber%20abgelaufene%20Dienstleistungen%20_%2.md
# Ticket 2023041142002858

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject
WG: (extern) Fwd: Information über abgelaufene Dienstleistungen / Information about expired services (corz09)

## Keywords
- Expired services
- SSH-Key
- Cluster login
- ANSYS
- STAR-CCM+
- Meggie-Cluster

## Summary
Users received an email stating their accounts (corz09 and corz024h) had expired, despite having transitioned to SSH-Key authentication. This caused confusion and login issues.

## Root Cause
- The expiration notice was from the old user management system and was not relevant to the new SSH-Key-based system.
- Login issues were due to incorrect SSH-Key usage.

## Solution
- Confirmed that the expiration notice was irrelevant.
- Provided guidance on using the correct SSH-Key for login.
- Installed the latest versions of ANSYS and STAR-CCM+ on the Meggie-Cluster as requested.

## Lessons Learned
- Expiration notices from old systems can cause confusion and should be clearly communicated as irrelevant if they do not affect the current system.
- Ensure users are aware of the correct SSH-Key usage for login.
- Quick resolution of software installation requests can enhance user satisfaction.

## Actions Taken
- HPC Admins explained the irrelevance of the expiration notice.
- HPC Admins guided the user on correct SSH-Key usage.
- HPC Admins installed the requested software versions on the Meggie-Cluster.

## Follow-up
- Users confirmed successful login and availability of the requested software.
```
---

### 2024022942002488_Migration%20of%20iwc1a010%20HPC%20account%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20mand.md
# Ticket 2024022942002488

 # HPC Support Ticket Conversation Summary

## Subject
Migration of HPC account to new HPC portal / SSH keys become mandatory

## Keywords
- HPC account migration
- SSH keys
- HPC portal
- Single Sign-On (SSO)
- IdM portal
- SSH key types (RSA, ECDSA, ED25519)
- Usage statistics
- ClusterCockpit
- Jupyterhub

## General Learnings
- The HPC services are migrating from the IdM portal to a new online HPC portal.
- Access to HPC systems will require SSH keys from March 11 onwards.
- Accepted SSH key types are RSA (4096 bits), ECDSA (512 bits), and ED25519.
- Users should generate SSH key pairs with passphrases and upload the public key to the HPC portal.
- The HPC portal is decoupled from the IdM portal and will be the sole source for account validity.
- Users can ignore expiration messages from the IdM portal.
- Usage statistics are visible to PIs and project managers.
- ClusterCockpit and Jupyterhub access should be done via Single Sign-On links from the HPC portal.

## Root Cause of the Problem
- The migration process requires users to adopt SSH keys for accessing HPC systems.
- Users need to update their account information and SSH keys in the new HPC portal.

## Solution
- Users should generate SSH key pairs and upload the public key to the HPC portal.
- Access the HPC portal using Single Sign-On (SSO) with IdM credentials.
- Use the new HPC portal for account management and access to services like ClusterCockpit and Jupyterhub.

## Additional Resources
- [SSH Secure Shell Access Documentation](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/)
- [FAQs](https://hpc.fau.de/faqs/#ID-230)

## Contact Information
- HPC Support: [support-hpc@fau.de](mailto:support-hpc@fau.de)
- HPC Portal: [https://portal.hpc.fau.de](https://portal.hpc.fau.de)
---

### 2024080742000466_Pending%20invitation%20at%20portal.hpc.fau.de.md
# Ticket 2024080742000466

 ```markdown
# HPC Support Ticket: Pending Invitation at HPC Portal

## Keywords
- Pending invitation
- HPC portal
- Project invitation
- User acceptance
- User tab

## Problem Description
A user reported that an invitation sent to a colleague for joining an HPC project was still pending despite being accepted.

## Root Cause
The colleague had logged into the HPC portal but had not actively accepted the invitation on the user tab.

## Solution
The HPC Admin advised that the colleague needed to actively accept the invitation on the user tab within the HPC portal.

## General Learning
- Ensure that users not only log into the HPC portal but also actively accept invitations on the user tab.
- Check the status of invitations on the user tab to confirm acceptance.

## Actions Taken
- The HPC Admin reviewed the status of the invitation and identified that the colleague had not completed the acceptance process.
- The user was informed about the necessary steps to complete the invitation acceptance.
```
---

### 2024021942003086_Migration%20of%20mpt4%20HPC%20accounts%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20mandato.md
# Ticket 2024021942003086

 # HPC Support Ticket: Migration of HPC Accounts to New Portal / SSH Keys Mandatory

## Keywords
- HPC account migration
- SSH keys
- HPC portal
- IdM portal
- Single Sign-On (SSO)
- SSH key types (RSA, ECDSA, ED25519)
- Account validity
- Usage statistics
- ClusterCockpit
- Jupyterhub

## Summary
- **Migration Process**: Existing HPC accounts are being migrated from the IdM portal to a new online HPC portal.
- **Access Method**: Future access to HPC systems will be via SSH keys only.
- **SSH Key Requirements**: Accepted SSH key types are RSA (4096 bits), ECDSA (512 bits), and ED25519.
- **Portal Access**: The new HPC portal can be accessed at [https://portal.hpc.fau.de](https://portal.hpc.fau.de) using SSO with IdM credentials.
- **Account Validity**: The new HPC portal will be the sole source for account validity.
- **Usage Statistics**: Users, PIs, and project managers can view usage statistics in the HPC portal.
- **ClusterCockpit and Jupyterhub**: Access these services via SSO links within the HPC portal.

## Root Cause of the Problem
- Users need to transition to the new HPC portal and set up SSH keys for continued access.

## Solution
- **Login**: Use SSO with IdM credentials to access the new HPC portal.
- **SSH Keys**: Generate and upload SSH key pairs with passphrases to the HPC portal.
- **Documentation**: Refer to the provided documentation and FAQs for guidance on SSH keys.
- **Windows Users**: Recommended to use OpenSSH built into Windows (Power)Shell or MobaXterm.
- **Account Validity**: Contact the PI or project manager to update account validity.

## Additional Notes
- Ignore automatic messages from the IdM portal regarding HPC service expiration.
- The new HPC portal is decoupled from the IdM portal and will not automatically update contract extensions or departures.
- New HPC accounts should be requested through the PI or project manager, not directly through RRZE.

## References
- [HPC Portal](https://portal.hpc.fau.de)
- [SSH Documentation](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/)
- [FAQs](https://hpc.fau.de/faqs/#ID-230)
---

### 2022020942001396_Log%20in.md
# Ticket 2022020942001396

 ```markdown
# HPC-Support Ticket: Log in Issue

## Keywords
- SSH
- Login issue
- Resource temporarily unavailable
- Linux subsystem on Windows
- Entrance node

## Problem Description
User unable to connect to the HPC entrance node via SSH from a Linux subsystem shell on Windows. The error message received is:
```
ssh: connect to host emmy.rrze.fau.de port 22: Resource temporarily unavailable
```

## Root Cause
Potential issues could include:
- Network connectivity problems
- Server-side issues with the entrance node
- Configuration issues with the Linux subsystem on Windows

## Solution
- Verify network connectivity and ensure that the entrance node is reachable.
- Check the status of the entrance node to ensure it is operational.
- Review the configuration of the Linux subsystem on Windows to ensure it is set up correctly for SSH connections.

## Actions Taken
- HPC Admins and 2nd Level Support team should investigate the network and server status.
- Provide guidance on configuring the Linux subsystem on Windows for SSH connections if necessary.

## Notes
- This issue may recur if there are intermittent network or server problems.
- Ensure users are aware of any scheduled maintenance or known issues affecting the entrance node.
```
---

### 2024073042004116_access%20to%20alex%20HPC.md
# Ticket 2024073042004116

 ```markdown
# HPC Support Ticket: Access to alex HPC

## Keywords
- SSH Key
- HPC Portal
- Permission Denied (publickey)
- Account Extension
- Identity Provider

## Root Cause
- User deleted the SSH key in their local `~/.ssh/` folder, resulting in a "Permission denied (publickey)" error when attempting to log in.
- User is unable to log in to the HPC portal as they are no longer employed by FAU.

## Summary
- User is a former postdoc with an extended HPC account to finish publications.
- User encountered login issues due to a deleted SSH key.
- HPC Admin confirmed that the user's account is linked to a new SSO identity in the USA.

## Steps Taken
1. User contacted HPC Admin regarding the SSH key issue.
2. HPC Admin forwarded the ticket to the HPC team for resolution.
3. HPC team confirmed that the user's account is linked to a new SSO identity.
4. User was informed that they should be able to reset their SSH key without issues.

## Solution
- The user's account was successfully linked to their new identity provider in the USA.
- User should be able to reset their SSH key and regain access to their HPC account.

## General Learnings
- Ensure users are aware of the importance of maintaining their SSH keys.
- HPC Admins should be able to assist users in linking their accounts to new identity providers.
- Communication between the user, HPC Admin, and the HPC team is crucial for resolving access issues.
```
---

### 2024050842001307_Re%3A%20New%20invitation%20for%20%22Studentische%20Abschlu%C3%83%C2%9Farbeiten%20Tier3%20Grundversor.md
# Ticket 2024050842001307

 # HPC-Support Ticket Conversation Summary

## Subject
Re: New invitation for "Studentische Abschlußarbeiten Tier3 Grundversorgung LS Informatik 5 Mustererkennung (Prof. A. Maier)" waiting at portal.hpc.fau.de

## Keywords
- SSH Configuration
- Public Key Authentication
- SSH Debugging
- SSH Config File
- Connection Timeout
- Permission Denied

## Problem Description
- User accepted the invitation and uploaded the SSH public key but encountered issues when trying to connect via SSH.
- Error messages included "Permission denied, please try again" and "Connection timed out."

## Root Cause
- Incorrect SSH config file name or extension.
- Possible misconfiguration in the SSH key generation command.

## Troubleshooting Steps
1. **SSH Config File Check**:
   - Ensure the SSH config file is named `config` without any extension.
   - Verify the location of the config file in the `.ssh` folder.

2. **SSH Key Generation Command**:
   - User used `ssh-keygen -t ed25519 -f ~/.ssh/id_ed25519_nhr_fau` to generate the key.

3. **Debugging SSH Connection**:
   - User ran `ssh -vv iwi5202h@tinyx.nhr.fau.de` to gather more information about the connection issue.

## Solution
- The issue was resolved by removing the `.txt` extension from the SSH config file.

## Additional Resources
- [SSH Command Line Access](https://doc.nhr.fau.de/access/ssh-command-line/)
- [SSH with MobaXterm](https://doc.nhr.fau.de/access/ssh-mobaxterm/)

## Conclusion
- The user successfully resolved the SSH connection issue by correcting the SSH config file name.
- The HPC Admins provided guidance and resources to assist the user in troubleshooting the problem.

## Follow-up
- The user was advised to familiarize themselves with foundational HPC skills and provided with tutorials for further learning.

---

This summary can be used as a reference for similar issues in the future.
---

### 2021120142001741_Connecting%20to%20Interactive%20Job%20directly.md
# Ticket 2021120142001741

 # HPC Support Ticket: Connecting to Interactive Job Directly

## Keywords
- SSH
- Interactive Job
- VSCode
- ProxyJump
- SLURM
- qsub
- salloc
- sbatch
- GPU Node
- VPN
- Environment Variable
- SLURM_EXPORT_ENV

## Problem
- User unable to connect directly via SSH to an interactive job started on a GPU node.
- Connection only possible via woody-frontend.
- VSCode integration not working due to SSH limitations.
- Port-forwarding not functioning.

## Root Cause
- User not fully within the university network.
- Automatic logout due to inactivity in the interactive session.

## Solutions
- **Network Configuration**: Use VPN (split-tunnel) or ProxyJump with woody or cshpc as the jump host.
  - Documentation: [SSH Secure Shell Access to HPC Systems](https://hpc.fau.de/systems-services/systems-documentation-instructions/ssh-secure-shell-access-to-hpc-systems/#advanced_usage)
- **Interactive Job Management**:
  - Use `qsub.tinygpu -I` for interactive jobs.
  - Use `salloc.tinygpu` for starting interactive jobs on SLURM nodes.
  - Use `sbatch.tinygpu` for non-interactive batch jobs.
- **Environment Variable**:
  - Unset `SLURM_EXPORT_ENV` to prevent environment export issues.
  - Use `--export=none` in SLURM options to avoid environment conflicts.

## Additional Notes
- **VSCode Integration**:
  - First connect to woody, then install VSCode dependencies and extensions.
  - Connect to other nodes afterward.
- **Interactive Session Management**:
  - No way to exit the interactive shell without terminating the job.
  - Interactive sessions are not intended for long-term development; use them for testing and compilation.

## Documentation
- [GPU Cluster Documentation](https://hpc.fau.de/systems-services/systems-documentation-instructions/clusters/tinygpu-cluster/)
- [SSH Secure Shell Access to HPC Systems](https://hpc.fau.de/systems-services/systems-documentation-instructions/ssh-secure-shell-access-to-hpc-systems/#advanced_usage)

## Conclusion
- Use VPN or ProxyJump for direct SSH connections.
- Manage interactive sessions carefully to avoid automatic logout.
- Unset `SLURM_EXPORT_ENV` and use `--export=none` for environment management.
---

### 2024011742002038_Re%3A%20New%20invitation%20for%20%22FRASCAL-MD%20-%20Particle-based%20computing%20at%20LTM%20for%20F.md
# Ticket 2024011742002038

 ```markdown
# HPC Support Ticket Analysis

## Subject
Re: New invitation for "FRASCAL-MD - Particle-based computing at LTM for FRASCAL" waiting at portal.hpc.fau.de

## Keywords
- HPC Portal
- Account Activation
- SSH Keys
- Documentation
- Support Contact

## Root Cause of the Problem
User had difficulty finding the necessary guide for account activation and SSH key generation.

## Solution
- **User Suggestion**: Add a link to the relevant guide in the invitation email before mentioning the support address.
- **HPC Admin Action**: Added the link to the email text before the problem contact information.

## What Can Be Learned
- **Documentation Importance**: Providing clear and accessible documentation can save users time and reduce support requests.
- **Email Enhancement**: Including relevant links in invitation emails can improve user experience and reduce confusion.
- **Feedback Implementation**: User feedback can be valuable for improving support processes.

## Actions Taken
- HPC Admins added the documentation link to the email text.
- The link will be updated when new documentation is available.

## Future Considerations
- Regularly update documentation links in automated emails.
- Continuously gather and implement user feedback to improve support processes.
```
---

### 2024022142003303_AW%3A%20New%20invitation%20for%20%22LS%20Datenbanksysteme%20und%20Data%20Mining%20-%20LMU%22%20waiti.md
# Ticket 2024022142003303

 ```markdown
# HPC Support Ticket: Missing Invitation

## Keywords
- Invitation
- SSO
- Email Address
- HPC Portal
- SSH Public Key

## Problem Description
The user reported that there was no invitation under the 'Users' section of their account. The invitation was sent to an email address different from the one registered with the SSO.

## Root Cause
The invitation was sent to an incorrect email address (`liao@dbs.ifi.lmu.de`) instead of the email address registered with the SSO (`ruotong.liao@lmu.de`).

## Solution
- Ensure that the invitation is sent to the email address registered with the SSO.
- The user should check their profile information in the HPC portal to verify the correct email address.

## Steps to Resolve
1. Verify the email address registered with the SSO in the user's profile.
2. Resend the invitation to the correct email address.
3. Instruct the user to log in via SSO using their IdM credentials to accept the invitation ('User' -> 'Your Invitations').
4. After accepting the invitation, the user should upload an SSH public key ('ssh-rsa') to the corresponding account ('User' -> 'Your Accounts').

## Additional Information
- Further information can be found at: [HPC Portal Documentation](https://doc.nhr.fau.de/hpc-portal/)
- In case of problems, users should send an email with a clear description of the issue to `hpc-support@fau.de`.
```
---

### 2024062742001351_HPC%20Portal%20SSO%20Access.md
# Ticket 2024062742001351

 # HPC Portal SSO Access Issue

## Keywords
- SSO
- HPC Portal
- Attribute Keys
- Surname
- GivenName
- Shibboleth
- SSO-Response

## Problem Description
A user reported an issue with accessing the HPC Portal through SSO. Despite releasing all required attributes, the portal indicated "Missing required attributes in SSO-Response."

## Root Cause
The keys of the "sn" (surname) and "givenName" attributes sent from the user's institution did not match the expected values. The keys sent were:
- `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/surname`
- `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/givenname`

The expected keys were:
- `urn:oid:2.5.4.4` / `urn:mace:dir:attribute-def:sn`
- `urn:oid:2.5.4.42` / `urn:mace:dir:attribute-def:givenName`

## Solution
The HPC Admin suggested changing the keys of the "sn" and "givenName" attributes to match the expected values on the user's side. This should resolve the issue.

## Additional Notes
- The user mentioned they are not an IT expert but will attempt to make the required changes.
- There was a previous partial user-account with an earlier timestamp that transmitted only one required attribute, `eduPersonScopedAffiliation`.
- The user expressed interest in meeting the HPC Admin but was unable to do so during their current visit.

## Follow-up
The user will attempt to make the necessary changes and report back on their progress.
---

### 2024021942002836_Migration%20of%20bcbl%20HPC%20accounts%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20mandato.md
# Ticket 2024021942002836

 # HPC Support Ticket Summary

## Subject
Migration of bcbl HPC accounts to new HPC portal / SSH keys become mandatory

## Keywords
- HPC account migration
- SSH keys
- HPC portal
- Single Sign-On (SSO)
- IdM portal
- SSH key types (RSA, ECDSA, ED25519)
- Account validity
- Usage statistics
- ClusterCockpit
- Jupyterhub

## What Can Be Learned
- **Migration Process**: HPC accounts are being migrated from the IdM portal to a new online HPC portal.
- **SSH Keys**: Access to HPC systems will require SSH keys only. Accepted types are RSA (4096 bits), ECDSA (512 bits), and ED25519.
- **Portal Access**: The new HPC portal can be accessed via SSO using IdM credentials.
- **Account Validity**: The HPC portal will be the sole source for account validity. Users should contact their PI or project manager for updates.
- **Usage Statistics**: Usage of different HPC systems can be viewed in the HPC portal. PIs and project managers will also have access to these statistics.
- **ClusterCockpit and Jupyterhub**: Users should use the SSO link from the HPC portal to access these services.

## Root Cause of the Problem
- Users need to generate and upload SSH keys to the new HPC portal for continued access to HPC systems.

## Solution
- Generate an SSH key pair with a passphrase.
- Upload the SSH PublicKey to the HPC portal.
- Use the SSO link from the HPC portal to access ClusterCockpit and Jupyterhub.

## Additional Information
- Documentation and FAQs are available for users unfamiliar with SSH keys.
- Windows users are recommended to use OpenSSH built into the Windows (Power)Shell or MobaXterm.
- The IdM portal and the new HPC portal are completely decoupled.

## Relevant Links
- [HPC Portal](https://portal.hpc.fau.de)
- [SSH Documentation](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/)
- [FAQs](https://hpc.fau.de/faqs/#ID-230)
---

### 2021042042002513_Nachfrage%20connection%20SSH.md
# Ticket 2021042042002513

 ```markdown
# HPC-Support Ticket: SSH Connection Issue

## Keywords
- SSH
- Connection timeout
- VPN
- Server access

## Problem Description
- User was able to connect to the server via SSH in the morning.
- Later attempts to connect resulted in a timeout error: `ssh: connect to host woody.rrze.fau.de port 22: Operation timed out`.
- VPN was active during the attempts.

## Root Cause
- The exact root cause is not specified in the provided conversation.

## Solution
- No solution provided in the conversation.

## General Learnings
- SSH connection issues can occur even when VPN is active.
- Timeout errors may indicate network issues or server-side problems.
- Further investigation is needed to diagnose and resolve the issue.
```
---

### 2023062342001511_Wallet%20time%20model%20training.md
# Ticket 2023062342001511

 # HPC Support Ticket: Wallet Time Model Training

## Keywords
- Wallet time
- JobID
- Fine-tuning model
- Time limit increase
- Email attribute transfer
- SSO (Single Sign-On)
- CSIC
- rediris.es

## Summary
Users requested an increase in wallet time for their jobs to fine-tune a model. Additionally, there was an issue with email attribute transfer via SSO for a user invitation.

## Conversation Details

### User Request
- **Initial Request**: Increase wallet time for job ID 769355.
- **Follow-up Request**: Increase time limit to 3 days for job ID 954438.

### HPC Admin Response
- **Action Taken**: Wallet time increased for both job IDs.
- **Additional Issue**: Email attribute transfer problem for a user invitation via SSO from CSIC.

### User Follow-up
- **Acknowledgment**: Users acknowledged the increase in wallet time.
- **Action on Additional Issue**: Users agreed to contact CSIC/rediris.es to resolve the email attribute transfer issue.

## Root Cause of the Problem
- **Wallet Time Increase**: Users needed more time to fine-tune their model.
- **Email Attribute Transfer**: CSIC transmits "no tiene correo" instead of the email address via SSO, preventing email notifications and updates from reaching the user.

## Solution
- **Wallet Time Increase**: HPC Admin increased the wallet time for the specified job IDs.
- **Email Attribute Transfer**: Users were advised to contact CSIC/rediris.es to enable the transfer of the email attribute for the HPC portal.

## General Learnings
- Users can request an increase in wallet time for their jobs by providing the job ID.
- Email attribute transfer issues via SSO can prevent important notifications from reaching users.
- Users should contact their respective SSO providers to resolve email attribute transfer issues.

## Documentation for Support Employees
- **Wallet Time Increase**: When users request an increase in wallet time, verify the job ID and increase the time limit as needed.
- **Email Attribute Transfer**: If there are issues with email attribute transfer via SSO, advise users to contact their SSO provider to enable the transfer of the email attribute.
---

### 2024022842001696_Problem%20Logging%20into%20the%20Cluster.md
# Ticket 2024022842001696

 # HPC Support Ticket: Problem Logging into the Cluster

## Keywords
- SSH login issue
- Passphrase not recognized
- Troubleshooting guide
- SSH command with `-vvv`

## Summary
- **User Issue**: Unable to log in to the HPC cluster via SSH due to passphrase not being recognized.
- **HPC Admin Response**: No known general login problem. User directed to follow the troubleshooting guide and provide detailed SSH command output with `-vvv` for further diagnosis.

## Root Cause
- Passphrase not recognized during SSH login.

## Solution
- Follow the troubleshooting guide: [SSH Command Line Troubleshooting](https://doc.nhr.fau.de/access/ssh-command-line/#troubleshooting)
- Provide the exact SSH command used with `-vvv` and the generated output for further assistance.

## General Learning
- Always check the troubleshooting guide for common issues.
- Use `-vvv` with SSH commands to generate detailed output for debugging.
- No general login problem reported; individual troubleshooting is necessary.

## Next Steps
- If the issue persists, provide the detailed SSH command output to the HPC support team for further investigation.
---

### 2022050242000233_IdP-Freischaltung%20f%C3%83%C2%BCr%20portal.hpc.fau.de%20von%20NHR%40FAU%20f%C3%83%C2%BCr%20den%20Zu.md
# Ticket 2022050242000233

 # HPC Support Ticket Analysis: IdP-Freischaltung für portal.hpc.fau.de

## Keywords
- HPC
- NHR@FAU
- SSO
- DFN-AAI-Föderation
- IdP
- Metadata
- Attributes
- Certificate expiration

## Summary
The ticket involves the activation of a new web portal for managing HPC computing time projects at NHR@FAU, requiring SSO login via the DFN-AAI-Föderation. The HPC Admin requested the activation of specific attributes in the IdP for user registration.

## Problem
- **Root Cause**: The certificate for the portal had expired.
- **Issue**: No feedback from KIT regarding the activation of the service in their IdP.

## Solution
- **Action Taken**: The HPC Admin confirmed that the SSO login was functioning with guest credentials.
- **Next Steps**: Await further feedback from KIT to ensure full activation.

## Learning Points
- **SSO Integration**: Understanding the process of integrating a new service into the DFN-AAI-Föderation.
- **Attribute Requirements**: The specific attributes required for user registration in the SdP.
- **Certificate Management**: The importance of monitoring and renewing certificates to avoid service disruptions.

## References
- [NHR@FAU Portal](https://portal.hpc.fau.de/)
- [NHR@FAU Metadata](https://portal.hpc.fau.de/saml/metadata)
- [NHR Application Rules](https://hpc.fau.de/systems-services/systems-documentation-instructions/nhr-application-rules/)

## Conclusion
This ticket highlights the importance of proper communication and follow-up with external entities for SSO integration and the critical role of certificate management in maintaining service availability.
---

### 2022111342000184_Typo%20in%20ssh%20instruction.md
# Ticket 2022111342000184

 # HPC Support Ticket: Typo in SSH Instruction

## Keywords
- SSH Configuration
- Typo
- IdentityFile
- Documentation Error

## Problem
- **Root Cause:** Typographical error in the SSH configuration documentation.
- **User Report:** The configuration option "IdentitiyFile" is incorrectly spelled. It should be "IdentityFile".

## Solution
- **Action Taken:** HPC Admin acknowledged the issue and will correct the spelling error in the documentation for future users.

## Lessons Learned
- **Documentation Accuracy:** Ensuring documentation is free of typos and errors is crucial for user experience.
- **User Feedback:** Encourage users to report any discrepancies they find in the documentation to improve its quality.

## Next Steps
- **Update Documentation:** Correct the spelling of "IdentityFile" in the SSH configuration instructions.
- **Review Process:** Implement a review process for documentation updates to catch similar errors in the future.

---

This report can be used as a reference for future documentation errors and to emphasize the importance of accurate and up-to-date user guides.
---

### 2024120542003879_AW%3A%20%28extern%29%20New%20invitation%20for%20%22HPC4AAI%20-%20Studentische%20Abschlu%C3%83%C2%9Fa.md
# Ticket 2024120542003879

 # HPC Support Ticket Conversation Analysis

## Keywords
- HPC Portal
- Invitation
- SSO Login
- IdM Credentials
- SSH Public Key
- Cookies
- Error Message

## Summary
A user received an invitation to a project on the HPC portal but encountered an error message. The HPC Admin suggested checking the cookies settings as a potential solution.

## Root Cause of the Problem
- The user encountered an error message while trying to accept the invitation on the HPC portal.

## Solution
- The HPC Admin suggested that the user should follow the instructions regarding cookies.

## General Learnings
- Users may encounter issues with accepting invitations on the HPC portal.
- Checking and following instructions related to cookies can potentially resolve login or invitation acceptance issues.
- Users should be guided to upload an SSH public key after accepting the invitation.

## Steps for Support Employees
1. **Verify Error Message**: Ask the user for the specific error message they are encountering.
2. **Check Cookies Settings**: Instruct the user to ensure their browser's cookies settings are correctly configured.
3. **Guide Through SSO Login**: Ensure the user is logging in via SSO using their IdM credentials.
4. **Upload SSH Key**: Remind the user to upload an SSH public key to the corresponding account after accepting the invitation.

## Additional Resources
- [HPC Portal Documentation](https://doc.nhr.fau.de/hpc-portal/)
- HPC Support Email: `hpc-support@fau.de`

This documentation can be used to troubleshoot similar issues in the future.
---

### 2022120742003388_fritz%20access%20using%20ssh%20key.md
# Ticket 2022120742003388

 # HPC Support Ticket: SSH Key Authentication Issue

## Keywords
- SSH Key Authentication
- Public/Private Key
- SSH Diagnostics (`ssh -v`)
- Account Provisioning
- Portal Users

## Problem Description
- User unable to login using SSH key; prompted for password instead of passphrase.
- SSH diagnostic output shows public key authentication attempt but falls back to password.
- User confirms presence of correct public and private keys.

## Diagnostic Output
```
ssh -v -i ~/Desktop/.ssh/id_rsa muco102h@fritz.nhr.fau.de
...
debug1: Authentications that can continue: publickey,gssapi-keyex,gssapi-with-mic,password
debug1: Next authentication method: publickey
debug1: Offering RSA public key: /home/mobaxterm/Desktop/.ssh/id_rsa
debug1: Authentications that can continue: publickey,gssapi-keyex,gssapi-with-mic,password
debug1: Next authentication method: password
muco102h@fritz.nhr.fau.de's password:
```

## Root Cause
- Issue with account provisioning affecting all portal users.
- Directory `/apps/rrze/usersshkeys/` was empty on all clusters.

## Solution
- The provisioning issue was resolved by HPC Admins.
- Users should be able to authenticate using SSH keys after the fix.

## Lessons Learned
- SSH key authentication issues can be caused by backend provisioning problems.
- Diagnostic output from `ssh -v` is crucial for troubleshooting SSH issues.
- Ensure the SSH key directory is correctly populated and accessible.

## Next Steps
- Verify that the SSH key directory is populated and accessible.
- Monitor for similar issues and ensure prompt resolution of provisioning problems.
- Educate users on using `ssh -v` for diagnostic purposes.
---

### 2023030142003547_Umstellung%20der%20HPC-Accounts%20der%20HS-Coburg%20am%20RRZE%20_%20NHR%40FAU%20-%20corz001h.md
# Ticket 2023030142003547

 # HPC Support Ticket Conversation Summary

## Subject
Umstellung der HPC-Accounts der HS-Coburg am RRZE / NHR@FAU - corz001h

## Keywords
- HPC Accounts
- HS-Coburg
- RRZE / NHR@FAU
- DFN-AAI/eduGAIN
- HPC-Portal
- SSH-PublicKeys
- SSH-Key
- Password Access
- Windows PowerShell
- Windows Subsystem for Linux
- mobaXterm
- OpenSSH
- Putty
- JumpHost-Feature
- Account Deactivation
- Data Deletion

## Problem
- Certificate has expired.
- Transition from paper-based system to electronic HPC-Portal.

## Solution
- Users need to log in to the HPC-Portal using DFN-AAI/eduGAIN.
- Existing HPC accounts will be linked to the user's identity in the portal.
- Users must upload SSH-PublicKeys via the "User / Benutzer" tab.
- SSH-PublicKeys will be synchronized to HPC systems within two hours.
- Access to HPC systems will be restricted to SSH-Key only by the end of March.
- Windows users are advised to use Windows PowerShell, Windows Subsystem for Linux, or mobaXterm.
- Accounts not linked by the end of March will be deactivated, and associated data will be deleted after three months.

## Additional Information
- Documentation and instructions for the HPC-Portal and SSH access are provided via links.
- Common SSH access issues are addressed in the FAQ.
- For further inquiries, users should contact the support team at HS-Coburg or the FAU faculty.

## Root Cause
- Expired certificate and need for transition to a new electronic system.

## Solution Implemented
- Users must log in to the HPC-Portal and upload SSH-PublicKeys to continue using their accounts.
- Transition to SSH-Key only access by the end of March.

## Documentation Links
- [HPC-Portal Usage](https://hpc.fau.de/systems-services/documentation-instructions/getting-started/nhrfau-hpc-portal-usage/)
- [SSH Access](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/)
- [FAQ](https://hpc.fau.de/faqs/#innerID-13183)
- [mobaXterm](https://mobaxterm.mobatek.net/)
---

### 2023071442000367_Migration%20of%20gwgi%20HPC%20accounts%20of%20AG%20Braun%20to%20new%20HPC%20portal%20_%20SSH%20keys%.md
# Ticket 2023071442000367

 # HPC Support Ticket Conversation Summary

## Keywords
- SSH keys
- SSO (Single Sign-On)
- FAU email address
- IdM portal
- HPC portal
- SSH configuration
- VPN
- SSH debugging

## General Learnings
- The HPC portal requires SSH keys for access.
- Users need to generate and upload SSH key pairs to the HPC portal.
- The FAU IdM system must have a registered email address for the user.
- The HPC portal and IdM portal are decoupled, and the HPC portal will not know about contract extensions or departures.
- Users need to contact their PI or project manager to update the validity of their HPC account.
- Some HPC systems require VPN access from external networks.
- SSH configuration files can be used to simplify access to HPC systems.

## Root Causes and Solutions

### User: Kristine
- **Root Cause**: Missing required attributes in SSO-Response due to an unregistered FAU email address.
- **Solution**: Register an FAU email address in the IdM portal and ensure it is connected to the Exchange mailbox.

### User: Marius
- **Root Cause**: Inability to access the HPC system using SSH keys.
- **Solution**: Use a jump host configuration for SSH access and ensure the correct hostname is used. VPN may be required for external access.

## Additional Notes
- The HPC portal provides usage statistics that are visible to PIs and project managers.
- ClusterCockpit and Jupyterhub services require Single Sign-On links from within the HPC portal.
- The HPC portal will be the only source for account validity by the end of July.
- Windows users are recommended to use OpenSSH built into the Windows (Power)Shell or MobaXterm instead of Putty.

## Documentation Links
- [SSH Secure Shell Access to HPC Systems](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/)
- [FAQs](https://hpc.fau.de/faqs/#ID-230)
- [SSH Configuration for HPC Portal](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/#ssh_config_hpc_portal)
- [FAQs on SSH Configuration](https://hpc.fau.de/faqs/#innerID-13183)

This summary provides a concise overview of the key points and solutions discussed in the HPC support ticket conversation. It can be used as a reference for support employees to address similar issues in the future.
---

### 2024021742000538_Migration%20of%20AIBE%20HPC%20accounts%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20mandato.md
# Ticket 2024021742000538

 # HPC Support Ticket: Migration of AIBE HPC Accounts to New HPC Portal / SSH Keys Become Mandatory

## Keywords
- HPC account migration
- SSH keys
- HPC portal
- IdM portal
- Single Sign-On (SSO)
- SSH key types (RSA, ECDSA, ED25519)
- Account validity
- Usage statistics
- ClusterCockpit
- Jupyterhub

## Summary
The HPC Admins are migrating existing HPC accounts to a new online HPC portal. Users will need to generate and upload SSH keys for access. The new portal will be the sole source for account validity and usage statistics.

## Key Points to Learn
- **Migration Process**: Existing HPC accounts are being migrated to a new HPC portal.
- **SSH Keys**: Access to HPC systems will require SSH keys (RSA, ECDSA, ED25519) with a passphrase.
- **HPC Portal**: The new portal can be accessed via SSO using IdM credentials. It will show existing HPC accounts and usage statistics.
- **Account Validity**: The new HPC portal will manage account validity. Users should contact their PI or project manager for updates.
- **ClusterCockpit and Jupyterhub**: Access these services via SSO links from the HPC portal.

## Root Cause of the Problem
- Users need to adapt to the new HPC portal and SSH key requirements for continued access to HPC services.

## Solution
- Generate and upload SSH keys to the new HPC portal.
- Use the HPC portal for account management and accessing services like ClusterCockpit and Jupyterhub.
- Contact the PI or project manager for account validity updates.

## Additional Resources
- [SSH Secure Shell Access Documentation](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/)
- [FAQs](https://hpc.fau.de/faqs/#ID-230)
- [HPC Portal](https://portal.hpc.fau.de)
---

### 2024061842006069_Zugang%20zu%20Woody%20f%C3%83%C2%BCr%20Kurs.md
# Ticket 2024061842006069

 # HPC Support Ticket: Zugang zu Woody für Kurs

## Keywords
- HPC Accounts
- HPC-Portal
- SSH-Keys
- IDM-Portal
- Lehrveranstaltungen
- Scripting-Kurs

## Summary
The user requested HPC accounts for a scripting course in geography. The HPC Admin provided instructions on how to create accounts via the HPC-Portal and clarified the use of SSH-Keys.

## Problem
- User requested HPC accounts for course participants.
- User needed a temporary account for group management.
- User inquired about setting passwords for HPC accounts via the IDM-Portal.

## Solution
- HPC Admin created a project in the HPC-Portal for the scripting course.
- User was instructed to invite multiple email addresses via the HPC-Portal.
- HPC Admin clarified that SSH-Keys are mandatory for HPC accounts and that accounts will not appear in the IDM-Portal.
- User was informed that SSH-Keys take 2 hours to propagate across all HPC systems.

## Key Takeaways
- HPC accounts for educational purposes are managed via the HPC-Portal.
- SSH-Keys are required for HPC accounts, and passwords are no longer used.
- The HPC-Portal and IDM-Portal are separate systems.
- Managers need to invite themselves to receive a gwku-Kennung.

## Additional Notes
- The user successfully invited the students and set up SSH-Keys for the course.
- The HPC Admin provided timely support and clarified all queries related to account management and access.
---

### 2023053042003981_Migration%20of%20mfbi%20HPC%20accounts%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20mandato.md
# Ticket 2023053042003981

 # HPC Support Ticket: Migration of HPC Accounts to New Portal / SSH Keys Mandatory

## Keywords
- HPC account migration
- SSH keys
- HPC portal
- Single Sign-On (SSO)
- IdM portal
- Passphrase
- RSA, ECDSA, ED25519
- OpenSSH
- MobaXterm
- ClusterCockpit
- Jupyterhub

## Summary
The HPC services at FAU are migrating existing HPC accounts to a new online HPC portal. Users need to generate and upload SSH keys for access.

## Key Points
- **Migration to New HPC Portal**: Access the new portal at [https://portal.hpc.fau.de](https://portal.hpc.fau.de) using SSO with IdM credentials.
- **SSH Keys Mandatory**: By mid-June, access to HPC systems will require SSH keys. Accepted types are RSA (4096 bits), ECDSA (512 bits), and ED25519.
- **SSH Key Generation**: Generate SSH key pairs with a passphrase and upload the public key to the HPC portal. It may take up to two hours for updates to propagate.
- **Documentation and FAQs**: Refer to [SSH documentation](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/) and [FAQs](https://hpc.fau.de/faqs/#ID-230) for assistance.
- **Windows Users**: Recommended to use OpenSSH built into Windows (Power)Shell or MobaXterm instead of Putty.
- **Account Validity**: The HPC portal will be the sole source for account validity. Ignore expiration messages from the IdM portal.
- **Usage Statistics**: Usage statistics for different HPC systems will be visible in the HPC portal, accessible by PIs and project managers.
- **ClusterCockpit and Jupyterhub**: Use Single Sign-On links from within the HPC portal for accessing ClusterCockpit and Jupyterhub.

## Root Cause of the Problem
- Users need to migrate their accounts to the new HPC portal and set up SSH keys for continued access.

## Solution
- Log in to the new HPC portal using SSO.
- Generate and upload SSH keys as per the provided guidelines.
- Use Single Sign-On links for accessing ClusterCockpit and Jupyterhub.
- Refer to the documentation and FAQs for detailed instructions.

## Additional Notes
- The HPC portal and IdM portal are decoupled. Account validity updates should be communicated to the PI or project manager.
- New HPC accounts should be requested through the PI or project manager, not directly through RRZE.
---

### 2024021842000429_Migration%20of%20iwi9030h%20HPC%20accounts%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20man.md
# Ticket 2024021842000429

 # HPC Support Ticket Conversation Summary

## Subject
Migration of HPC accounts to new HPC portal / SSH keys become mandatory

## Keywords
- HPC account migration
- SSH keys
- HPC portal
- Single Sign-On (SSO)
- IdM portal
- Password expiration
- Account validity
- ClusterCockpit
- Jupyterhub

## Key Points
- **Migration to New HPC Portal**: Existing HPC accounts are being migrated to a new online HPC portal.
- **SSH Keys Mandatory**: Access to HPC systems will require SSH keys only by the end of February.
- **SSH Key Types**: Accepted types are RSA (4096 bits), ECDSA (512 bits), and ED25519.
- **SSH Key Generation**: Users need to generate SSH key pairs with passphrases and upload the public key to the HPC portal.
- **Account Validity**: The HPC portal will be the sole source for account validity, decoupled from the IdM portal.
- **Usage Statistics**: Users, PIs, and project managers can view usage statistics in the HPC portal.
- **Single Sign-On**: For ClusterCockpit and Jupyterhub, users must use the SSO link from the HPC portal.

## Root Cause of the Problem
- Users need to adapt to the new HPC portal and the mandatory use of SSH keys for access.

## Solution
- Users should generate SSH key pairs, upload the public key to the HPC portal, and use the SSO link for accessing ClusterCockpit and Jupyterhub.
- For further assistance, users can refer to the provided documentation and FAQs.

## Additional Notes
- Windows users are recommended to use OpenSSH built into the Windows (Power)Shell or MobaXterm instead of Putty.
- Users should contact their PI or project manager for account validity updates instead of filling out paper forms.

## References
- [HPC Portal](https://portal.hpc.fau.de)
- [SSH Documentation](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/)
- [FAQs](https://hpc.fau.de/faqs/#ID-230)
---

### 42108488_Login%20auf%20woody%20h%C3%83%C2%A4ngt.md
# Ticket 42108488

 # HPC Support Ticket: Login auf woody hängt

## Keywords
- Login issue
- Woody
- Prompt
- Login-Skript
- Fileserver
- RRZE
- SSH
- Connection refused
- Qstat

## Problem Description
- User experiences a hang after authentication when logging into `woody`.
- No prompt is displayed.
- Unable to determine if the issue is with `woody1` or `woody2` due to "Connection refused" error when attempting to SSH into a specific machine.
- Other machines (`sfront04`, `testfront1`, `lima`, `memoryhog`, `cshpc`) are functioning normally.

## User Observations
- Pressing `CTRL+C` after the hang results in a prompt being displayed.
- `Qstat` seems to be functioning correctly.

## Root Cause
- The issue is caused by a problem with another RRZE fileserver (`gez:/proj/giga`).

## Solution
- No specific solution provided in the conversation.
- Further investigation into the fileserver issue is required.

## General Learnings
- Login issues can sometimes be resolved by interrupting the process with `CTRL+C`.
- Problems with fileservers can cause login hangs on HPC systems.
- It's important to check the status of related fileservers when troubleshooting login issues.

## Next Steps
- Investigate the fileserver issue (`gez:/proj/giga`).
- Monitor the login process on `woody` for any further hangs.
- Update the user and the support team on the resolution of the fileserver problem.
---

### 2024040442003092_%C3%A7%C2%AD%C2%94%C3%A5%C2%A4%C2%8D%3A%20New%20invitation%20for%20%22Studentische%20Abschlu%C3%83%C.md
# Ticket 2024040442003092

 # HPC Support Ticket Conversation Analysis

## Keywords
- SSH Connection
- Permission Denied
- SSH Public Key
- HPC Portal
- SSO Login
- IdM Credentials
- Debugging Log

## Summary
A user encountered a "Permission denied" error while attempting to connect to the HPC system via SSH. The user had received an invitation to a project and was instructed to upload an SSH public key to their account.

## Root Cause
- The user did not properly configure their SSH keys or did not follow the correct procedure for uploading the public key to the HPC portal.

## Steps Taken
1. **Invitation and Instructions**: The user received an invitation to a project and was instructed to log in via SSO using IdM credentials and upload an SSH public key.
2. **SSH Connection Attempt**: The user attempted to connect via SSH but encountered a "Permission denied" error.
3. **HPC Admin Response**: The HPC Admin confirmed that the user had uploaded SSH keys and provided a link to documentation for local setup. The Admin also requested a debugging log for further investigation.

## Solution
- The user was advised to follow the documentation for local SSH setup: [SSH Command Line Documentation](https://doc.nhr.fau.de/access/ssh-command-line/).
- The user was asked to provide a debugging log with the command `ssh -v <your usual SSH options and arguments>` for further troubleshooting.

## General Learnings
- **SSH Key Configuration**: Proper configuration and uploading of SSH public keys are crucial for successful SSH connections to the HPC system.
- **Documentation**: Users should refer to the provided documentation for setting up SSH on their local machines.
- **Debugging**: Enabling debugging (`ssh -v`) can provide valuable information for troubleshooting SSH connection issues.

## Next Steps
- If the issue persists, the user should provide the requested debugging log to the HPC support team for further analysis.
- The support team should ensure that the user has correctly followed the SSH setup documentation and uploaded the public key to the appropriate account.
---

### 2024021842000385_Migration%20of%20sles%20HPC%20accounts%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20mandato.md
# Ticket 2024021842000385

 # HPC Support Ticket Conversation Summary

## Subject
Migration of sles HPC accounts to new HPC portal / SSH keys become mandatory

## Keywords
- HPC account migration
- SSH keys
- HPC portal
- Single Sign-On (SSO)
- IdM portal
- SSH key types
- Account validity
- Usage statistics
- ClusterCockpit
- Jupyterhub

## What Can Be Learned
- **Migration Process**: The migration of HPC accounts from the IdM portal to a new online HPC portal is underway.
- **SSH Keys**: Access to HPC systems will require SSH keys only. Accepted types are RSA (4096 bits), ECDSA (512 bits), and ED25519.
- **SSH Key Upload**: Users need to generate SSH key pairs with passphrases and upload the public key to the HPC portal.
- **Portal Access**: The new HPC portal can be accessed via SSO using IdM credentials.
- **Account Validity**: The HPC portal will be the sole source for account validity, decoupled from the IdM portal.
- **Usage Statistics**: Users and their PIs/project managers can view usage statistics in the HPC portal.
- **ClusterCockpit and Jupyterhub**: Access to these services will be via SSO links from within the HPC portal.

## Root Cause of the Problem
- Users need to transition to the new HPC portal and set up SSH keys for continued access to HPC systems.

## Solution
- Users should log in to the new HPC portal using SSO.
- Generate and upload SSH keys as per the specified types and lengths.
- Use the SSO links within the HPC portal for accessing ClusterCockpit and Jupyterhub.

## Additional Resources
- [SSH Secure Shell Access Documentation](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/)
- [FAQs](https://hpc.fau.de/faqs/#ID-230)

## Contact Information
- **Support Email**: support-hpc@fau.de
- **HPC Portal**: [https://portal.hpc.fau.de](https://portal.hpc.fau.de)
- **HPC Website**: [https://hpc.fau.de/](https://hpc.fau.de/)
---

### 2024031542002467_Tier3-Access-Alex%20%22Behzad%20Safaei%22%20_%20iwia103h.md
# Ticket 2024031542002467

 # HPC Support Ticket Analysis

## Subject
Tier3-Access-Alex

## Keywords
- Account activation
- SSH access
- Permission denied
- FAQ reference

## Summary
A user encountered issues accessing the Alex cluster after their account was activated. The user could log into `csnhr` but received a "permission denied" error when attempting to connect to `alex.nhr.fau.de`.

## Root Cause
The user's account was newly created and required additional time for setup. Additionally, the user was not aware of the correct SSH key configuration for accessing the cluster.

## Solution
The HPC Admin provided a link to the FAQ that addresses SSH key configuration issues. The user followed the instructions in the FAQ and resolved the issue.

## Lessons Learned
- Newly created accounts may require additional time for full setup.
- Users should refer to the FAQ for common issues such as SSH key configuration.
- Proper SSH key configuration is crucial for accessing HPC clusters.

## References
- [FAQ: SSH Key Configuration](https://doc.nhr.fau.de/faq/#i-managed-to-log-in-to-t46--with-an-ssh-key--but-get-asked-for-a-password---permission-denied-when-continuing-to-a-cluster-frontend)

## Conclusion
The issue was resolved by referring the user to the appropriate FAQ. This highlights the importance of user education and documentation in troubleshooting common HPC access issues.
---

### 2024022642003143_kex_exchange_identification%20-%20Connection%20closed%20by%20remote%20host.md
# Ticket 2024022642003143

 ```markdown
# HPC Support Ticket: kex_exchange_identification - Connection closed by remote host

## Keywords
- SSH connection issue
- kex_exchange_identification
- Connection closed by remote host
- Scheduled downtime

## Problem Description
User unable to connect to NHR server via SSH, receiving error message:
```
kex_exchange_identification: Connection closed by remote host
```

## Root Cause
- Scheduled maintenance and downtime of NHR@FAU systems.

## Solution
- Wait until the scheduled maintenance is completed and try connecting again.

## Lessons Learned
- Always check for scheduled maintenance announcements before reporting connection issues.
- Communicate maintenance schedules clearly to users to avoid confusion.

## References
- [Scheduled Downtime Announcement](https://hpc.fau.de/2024/02/26/scheduled-downtime-of-nhrfau-systems-on-monday-february-26/)
```
---

### 2023101942002537_ssh%20access%20-%20%20iwwm101h.md
# Ticket 2023101942002537

 # HPC Support Ticket: SSH Access Issue

## Subject
- ssh access - iwwm101h

## User Issue
- Unable to login via SSH.
- Username: `2XLQA7JY6U4LHP7JFKOMBQCPGTW4EJML@hu-berlin.de`
- SSH key uploaded but still prompted for password.

## Key Points Learned
- User attempted to login with incorrect username.
- User's SSH key was too short (3072 bits instead of required 4096 bits).
- HPC Admin identified issues with import scripts and SSH key length.
- User was advised to update SSH key and adjust SSH config.
- User was able to login to `cshpc.rrze.fau.de` but faced issues logging into `alex.nhr.fau.de`.
- HPC Admin suggested direct connection to `alex` using proxy jump over `cshpc`.

## Root Cause
- Incorrect username used for SSH login.
- SSH key length was insufficient.
- Issues with import scripts on HPC side.

## Solution
- User updated SSH key to 4096 bits.
- HPC Admin fixed import script issues.
- User configured SSH config for direct connection to `alex` using proxy jump over `cshpc`.

## Final Status
- User was able to login to `cshpc.rrze.fau.de`.
- User was advised to connect directly to `alex` using proxy jump over `cshpc`.

## Additional Notes
- HPC Admin provided detailed instructions and kept the user updated on the progress.
- User was reminded to follow the SSH configuration template provided in the documentation.

## References
- [SSH Secure Shell Access to HPC Systems](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/)
- [Configure host settings in ~/.ssh/config](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/)
- [Template for HPC portal and NHR users](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/)
---

### 2024030142001323_Migration%20of%20mpp3%20HPC%20accounts%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20mandato.md
# Ticket 2024030142001323

 # HPC Support Ticket Summary

## Subject
Migration of mpp3 HPC accounts to new HPC portal / SSH keys become mandatory

## Keywords
- HPC account migration
- SSH keys
- HPC portal
- Single Sign-On (SSO)
- IdM portal
- Account validity
- Usage statistics
- ClusterCockpit
- Jupyterhub

## General Learnings
- **Migration Process**: The migration of HPC accounts from the IdM portal to a new online HPC portal is underway.
- **SSH Keys**: Access to HPC systems will require SSH keys from March 15th. Accepted key types are RSA (4096 bits), ECDSA (512 bits), and ED25519.
- **Portal Access**: The new HPC portal can be accessed at [https://portal.hpc.fau.de](https://portal.hpc.fau.de) using SSO with IdM credentials.
- **Account Validity**: The HPC portal will be the sole source for account validity starting from the end of February.
- **Usage Statistics**: Users, PIs, and project managers can view usage statistics in the HPC portal.
- **ClusterCockpit and Jupyterhub**: Access these services via SSO links within the HPC portal.

## Root Cause of the Problem
- Users need to transition to the new HPC portal and set up SSH keys for continued access to HPC systems.

## Solution
- **Generate SSH Keys**: Users should generate SSH key pairs with a passphrase and upload the public key to the HPC portal.
- **Documentation**: Refer to the provided documentation and FAQs for guidance on SSH keys.
- **Windows Users**: Recommended to use OpenSSH built into Windows (Power)Shell or MobaXterm instead of Putty.
- **Account Management**: Contact the PI or project manager for account validity updates or new account requests.

## Additional Notes
- Ignore automatic messages from the IdM portal regarding service expiration.
- The HPC portal and IdM portal are decoupled, so the HPC portal will not automatically update contract extensions or departures.

---

This summary provides a quick reference for support employees to understand the migration process and assist users with related issues.
---

### 2025030742001301_SSH%20connection%20issue.md
# Ticket 2025030742001301

 # SSH Connection Issue

## Keywords
- SSH connection problem
- Passphrase
- SSH key pairs
- File permissions
- `ssh-add -D`
- Zoom meeting

## Problem Description
A user encountered an SSH connection issue where the SSH command asked for a passphrase but stopped asking after several incorrect attempts. The user created new SSH key pairs, but the issue persisted.

## Troubleshooting Steps
1. **Passphrase Verification**:
   - Ensure the correct passphrase is entered when running the SSH command.

2. **File Permissions**:
   - Check if the SSH keys have the correct file permissions as described in the documentation.

3. **Remove SSH Agent Keys**:
   - Run `ssh-add -D` to remove all identities from the SSH agent and attempt to connect again.

4. **Zoom Meeting**:
   - Schedule a Zoom meeting with the user to discuss the issue in detail.

## Solution
The issue was resolved by creating a new SSH key pair with a different name.

## Conclusion
The root cause of the problem was likely related to the SSH key pair or the SSH agent. Removing the identities from the SSH agent and creating a new key pair resolved the issue.

---

This documentation can be used to solve similar SSH connection issues in the future.
---

### 2024061042002989_HPC%20CONNECTION%20PROBLEM%20-%20JOVAN%20CORRING%20%28FRAUNHOFER%20IIS%29.md
# Ticket 2024061042002989

 # HPC Connection Problem: External Institution Login Issue

## Keywords
- HPC Connection
- Portal Login
- External Institution
- Fraunhofer Gesellschaft
- Smartkey
- SCInterface Manager

## Problem Description
- User unable to connect to HPC through the portal.
- User selects "Other institution" and then "Fraunhofer Gesellschaft."
- Smartkey is properly connected but login fails.

## Root Cause
- Issue with the login process for external institutions, specifically Fraunhofer Gesellschaft.

## Solution
- The issue needs to be resolved internally at Fraunhofer Gesellschaft (FHG).
- User should refer to the internal Wiki for hints or contact the inviting person for assistance.

## Steps Taken
1. User attempted to log in via the HPC portal.
2. User selected "Other institution" and then "Fraunhofer Gesellschaft."
3. User encountered a login failure despite having a properly connected smartkey.
4. HPC Admin advised the user to resolve the issue internally at FHG and to refer to the internal Wiki or the inviting person for assistance.

## Notes
- The problem is specific to the login process for external institutions.
- Users should ensure they follow internal guidelines and contact their institution's IT service if needed.

## Follow-up
- If the issue persists, the user should provide additional details or screenshots to the HPC Admin for further investigation.
- The HPC Admin may need to coordinate with the external institution's IT service for a resolution.
---

### 2024011742002234_HPC%20account%20renewal.md
# Ticket 2024011742002234

 # HPC Account Renewal Ticket Analysis

## Keywords
- HPC account renewal
- Account expiration
- IDM portal
- HPC portal migration
- SSH keys
- capn group
- woody cluster

## Summary
A user requested an HPC account renewal for a colleague, including access to a specific cluster and group. The HPC admin responded by creating a new account and providing instructions for setup and support resources. Later, the user inquired about an account expiration discrepancy, which the admin clarified was due to a migration to a new HPC portal.

## Root Cause of the Problem
- User confusion about account expiration dates due to portal migration.
- Initial request for account renewal instead of a new account setup.

## Solution
- HPC admin created a new account and provided detailed setup instructions.
- Admin explained the portal migration process and clarified the account expiration date.

## General Learnings
- Account renewals may be handled by creating new accounts.
- Portal migrations can cause temporary discrepancies in account information.
- Clear communication about system changes (e.g., portal migrations) is crucial.
- Users should be directed to relevant support resources, such as documentation and training events.

## Follow-up Actions
- Ensure users are informed about upcoming system changes.
- Provide clear instructions for account setup and support resources.
- Monitor account migrations to address any potential issues.
---

### 2025022842002666_access%20to%20woody.md
# Ticket 2025022842002666

 # HPC Support Ticket: Access to Woody Cluster

## Keywords
- SSH access
- Hostname resolution
- ProxyJump
- SSH keys
- Debugging options
- Configuration update

## Summary
A user encountered issues accessing the Woody cluster via SSH due to a decommissioned proxy server.

## Problem Description
- User was unable to connect to the Woody cluster.
- Error message: `ssh: Could not resolve hostname cshpc.rrze.fau.de: Name or service not known`.
- User had not modified SSH keys or logged in for about half a year.

## Root Cause
- The proxy server `cshpc.rrze.fau.de` had been decommissioned.
- The user's `.ssh/config` file was outdated and still referencing the decommissioned server.

## Troubleshooting Steps
1. HPC Admin requested the output of `ssh -vv` for debugging.
2. The debug output revealed the attempt to connect through the decommissioned proxy server.

## Solution
- Update the `.ssh/config` file to use the new proxy server `csnhr`.
- Follow the template provided in the [documentation](https://doc.nhr.fau.de/access/ssh-command-line/#template-for-connecting-to-hpc-systems).

## Conclusion
The user successfully connected to the Woody cluster after updating the SSH configuration file.

## References
- [Decommissioning Notice](https://hpc.fau.de/2024/08/01/dialog-server-cshpc-decommissioned-nomachine-nx-to-be-replaced-by-xrdp/)
- [SSH Command Line Documentation](https://doc.nhr.fau.de/access/ssh-command-line/)
---

### 2024040342003638_Invitation%20to%20HPC.md
# Ticket 2024040342003638

 # HPC Support Ticket: Invitation to HPC

## Keywords
- HPC
- IDM Account
- SSO
- Email Address
- Postfachzustellung
- Gastwissenschaftler
- NHR@FAU
- DFN-AAI/eduGAIN

## Problem Description
A guest scientist was added to an NHR@FAU project but encountered an error during the IDM account generation process. The error message indicated that "attributes required for correct account generation are missing."

## Root Cause
- The SSO process does not transfer the email address because the Postfachzustellung is not activated in the IDM.
- The likelihood of matching invitations sent to a @gmail.com address is very low.

## Solutions Proposed
1. **Activate Postfachzustellung in IDM**: The guest scientist can activate mail delivery in the IDM, possibly with the help of the RRZE-Servicetheke.
2. **Use Official Email**: Clarify with the RRZE-Servicetheke if an external email can be registered as the official email for guest scientists and if it will be transmitted via SSO from the IdP.
3. **Use DFN-AAI/eduGAIN**: The guest scientist can attempt to log in via DFN-AAI/eduGAIN with their home institution's credentials. If successful, the invitation should be sent to the email address transmitted via SSO.

## Conclusion
The issue arises from the lack of email address transfer during the SSO process due to the Postfachzustellung not being activated. The solutions involve either activating the Postfachzustellung, using an official email, or logging in via DFN-AAI/eduGAIN.

## Additional Notes
- The guest scientist was able to log in to the IDM but encountered issues with account generation.
- The HPC Admin suggested three potential solutions to resolve the issue.
- The ticket involves communication between the user and the HPC Admin to troubleshoot and resolve the problem.
---

### 2024100342001039_Login%20problem%20-%20user%20ihpc100h.md
# Ticket 2024100342001039

 ```markdown
# HPC Support Ticket: Login Problem

## Subject
Login problem - user ihpc100h

## User Issue
- **Symptom**: User unable to get shell prompt after successful SSH login.
- **Command Used**: `ssh ihpc100h@csnhr.nhr.fau.de`
- **Affected Users**: Multiple users experiencing the same issue.

## HPC Admin Response
- **Root Cause**: Overloading of fileservers causing shell to block during login.
- **Account Issue**: Account `ihpc100h` registered to another user, indicating potential account sharing.
- **Solution**:
  - **Immediate Action**: Check if the prompt appears after some time (<30s).
  - **Long-term Action**: Refer to the service disruption notice due to high file server load.

## Keywords
- SSH login
- Shell prompt
- Fileserver overload
- Account sharing
- Service disruption

## Lessons Learned
- **Fileserver Overload**: High load on fileservers can cause login delays and shell blocking.
- **Account Sharing**: Ensure users are not sharing accounts, as it is against policy.
- **Communication**: Inform users about ongoing service disruptions and provide relevant links for updates.

## References
- [Service Disruptions on Clusters Due to High File Server Load](https://hpc.fau.de/2024/10/03/service-disruptions-on-clusters-due-to-high-file-server-load-2/)
```
---

### 2024021542000916_Migration%20of%20empk%20HPC%20accounts%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20mandato.md
# Ticket 2024021542000916

 # HPC Support Ticket Conversation Summary

## Subject
Migration of empk HPC accounts to new HPC portal / SSH keys become mandatory

## Keywords
- HPC account migration
- SSH keys
- HPC portal
- Single Sign-On (SSO)
- IdM portal
- SSH key types (RSA, ECDSA, ED25519)
- Usage statistics
- ClusterCockpit
- Jupyterhub

## General Learnings
- **Migration Process**: The migration of HPC accounts from the IdM portal to a new online HPC portal is underway.
- **SSH Keys**: Access to HPC systems will require SSH keys by the end of February 2024. Accepted SSH key types are RSA (4096 bits), ECDSA (512 bits), and ED25519.
- **Portal Access**: The new HPC portal can be accessed via SSO using IdM credentials.
- **Account Validity**: The HPC portal will be the sole source for account validity, decoupled from the IdM portal.
- **Usage Statistics**: Users and their PIs/project managers can view usage statistics in the HPC portal.
- **ClusterCockpit and Jupyterhub**: Access to these services will be via SSO links from within the HPC portal.

## Root Cause of the Problem
- The user is on vacation until February 21st and will address the email upon return.

## Solution
- No immediate solution required as the user will address the email after returning from vacation.

## Additional Notes
- Users should generate and upload SSH keys to the HPC portal.
- Windows users are recommended to use OpenSSH built into the Windows (Power)Shell or MobaXterm instead of Putty.
- For account validity updates, users should contact their PI or project manager instead of filling out paper forms.

---

This summary provides a concise overview of the migration process, SSH key requirements, and changes in accessing HPC services. It serves as a reference for support employees to address similar issues in the future.
---

### 2021041842000421_Unable%20to%20access%20from%20faui00c.cs.fau.de.md
# Ticket 2021041842000421

 # HPC Support Ticket: Unable to Access from faui00c.cs.fau.de

## Keywords
- SSH
- Authentication Failure
- SSH Key
- HPC Access
- Username Issue

## Problem Description
- User unable to SSH into HPC from `faui00c.cs.fau.de`.
- Error message: `Received disconnect from 10.28.8.12 port 22:2: Too many authentication failures`.
- Possible cause: User initially tried logging in with IDM-ID instead of the correct username.

## Root Cause
- Incorrect username used for SSH login.

## Solution
- Use the correct username for SSH login.
- SSH keys can be placed on the HPC system by creating a `.ssh` directory and adding `authorized_keys`.

## Additional Information
- Connection via other nodes (e.g., `ircbox`) works fine.
- SSH keys work as expected once the correct username is used.

## Ticket Resolution
- Issue resolved automatically after using the correct username.
- Ticket closed by HPC Admin with the note: `Die Kundenanfrage wird geschlossen, weil ... von selbst erledigt.`

## General Learning
- Ensure the correct username is used for SSH login.
- SSH keys can be configured on the HPC system for secure access.
- Incorrect login attempts can lead to authentication failures and disconnection.
---

### 2024021842000411_opencast%20HPC-Account%20_%20Umstellung%20HPC-Portal%20%26%20SSH-Keys.md
# Ticket 2024021842000411

 ```markdown
# HPC-Support Ticket: opencast HPC-Account / Umstellung HPC-Portal & SSH-Keys

## Keywords
- HPC Account
- HPC Portal
- SSH Keys
- Account Migration
- Access Methods
- Account Validity
- Usage Statistics
- ClusterCockpit
- Jupyterhub

## Summary
- **Issue**: Determining the usage and necessity of the "opencast" HPC account.
- **Action**: Informing users about the migration to a new HPC portal and the mandatory use of SSH keys for access.
- **Outcome**: The "opencast" account was deemed unnecessary and marked as inactive.

## Details
- **HPC Admin**: Inquired about the usage of the "opencast" account, noting the last activity in Summer 2022.
- **User Response**: Confirmed that the account is no longer needed.
- **HPC Admin**: Updated the expiration date in the HPC portal, marking the "opencast" account as inactive.

## General Learnings
- **Migration Process**: Existing HPC accounts are being migrated to a new online HPC portal.
- **Access Methods**: Future access to HPC systems will be via SSH keys only, with no passwords.
- **SSH Key Types**: Accepted SSH key types are RSA (4096 bits), ECDSA (512 bits), and ED25519.
- **Portal Features**: The HPC portal allows users to see their usage statistics, which are also visible to PIs and project managers.
- **Single Sign-On**: Access to ClusterCockpit and Jupyterhub will be through Single Sign-On links within the HPC portal.

## Solution
- **Account Management**: If an account is no longer needed, it should be marked as inactive in the HPC portal.
- **SSH Key Setup**: Users should generate and upload SSH key pairs to the HPC portal for future access.
- **Portal Usage**: Users should familiarize themselves with the new HPC portal for managing their accounts and accessing usage statistics.
```
---

### 2023052442002368_Unable%20to%20access%20systems%20with%20SSH%20key.md
# Ticket 2023052442002368

 # HPC-Support Ticket: Unable to Access Systems with SSH Key

## Keywords
- SSH Key
- Access Denied
- Ubuntu 20.04
- Windows System Linux 2 (WSL2)
- Public Key
- Portal
- Dialogserver

## Summary
A user recently joined a project and is unable to connect to the dialogserver using their SSH key. The user uploaded their public key to the portal but still faces access issues. The user is operating from an Ubuntu 20.04 environment within Windows System Linux 2 (WSL2).

## Root Cause
- Possible issues with SSH key configuration or propagation delay in the portal.
- Potential compatibility issues with WSL2.

## Solution
- Verify the SSH key is correctly uploaded and propagated in the portal.
- Ensure the SSH key is correctly configured in the user's WSL2 environment.
- Check for any known issues or compatibility problems with WSL2 and the HPC system.

## Actions Taken
- The user uploaded their public key to the portal.
- The user attempted to add a new key but faced no success.

## Next Steps
- HPC Admins should verify the SSH key propagation and configuration.
- 2nd Level Support team should assist in troubleshooting WSL2 compatibility issues.
- Provide detailed instructions for SSH key configuration in WSL2 if necessary.

## Notes
- Ensure the user is aware of any delay in SSH key propagation.
- Document any specific steps or configurations required for WSL2 users.

---

This documentation aims to assist support employees in resolving similar SSH key access issues, particularly for users operating from WSL2 environments.
---

### 2024030442002791_Migration%20of%20dsam%20HPC%20accounts%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20mandato.md
# Ticket 2024030442002791

 # HPC Support Ticket Conversation Summary

## Subject
Migration of dsam HPC accounts to new HPC portal / SSH keys become mandatory

## Keywords
- HPC account migration
- SSH keys
- HPC portal
- Single Sign-On (SSO)
- IdM portal
- SSH key types
- Account validity
- Usage statistics
- ClusterCockpit
- Jupyterhub

## What Can Be Learned
- **Migration Process**: HPC accounts are being migrated from the IdM portal to a new online HPC portal.
- **Access Method**: Access to HPC systems will be via SSH keys only from March 11th.
- **SSH Key Requirements**: Accepted SSH key types are RSA (4096 bits), ECDSA (512 bits), and ED25519.
- **SSH Key Upload**: Users need to generate SSH key pairs with passphrases and upload the public key to the HPC portal.
- **Account Validity**: The HPC portal is the sole source for account validity, not the IdM portal.
- **Usage Statistics**: Users, PIs, and project managers can view usage statistics in the HPC portal.
- **ClusterCockpit and Jupyterhub**: Access these services via Single Sign-On links from within the HPC portal.

## Root Cause of the Problem
- Users need to adapt to the new SSH key-based access method and the migration to the new HPC portal.

## Solution
- Generate and upload SSH keys as per the specified requirements.
- Use the new HPC portal for account management and accessing services.
- Ignore expiration messages from the IdM portal.
- Contact PIs or project managers for account validity updates.

## Additional Resources
- [SSH Secure Shell Access Documentation](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/)
- [FAQs](https://hpc.fau.de/faqs/#ID-230)
- [HPC Portal](https://portal.hpc.fau.de)
---

### 2025011442002569_Urgent%20Assistance%20Required%3A%20Unable%20to%20Connect%20to%20TinyX%20Cluster.md
# Ticket 2025011442002569

 # HPC Support Ticket: Unable to Connect to TinyX Cluster

## Keywords
- Connection Issue
- TinyX Cluster
- VScode
- Quota Exceeded
- SSH Client

## Problem Description
- User unable to connect to TinyX cluster.
- VScode repeatedly asks for passkey and fails to connect.

## Root Cause
- User's home directory quota exceeded, preventing VScode from writing necessary files.

## Solution
- **Immediate Fix**: Use a standard SSH client to access the cluster instead of VScode.
- **Long-term Fix**:
  1. Log in using a normal SSH client.
  2. Clean up the home directory to free up space.
  3. Retry connecting with VScode after ensuring the quota is no longer exceeded.

## Lessons Learned
- VScode may not provide useful error messages when the home directory quota is exceeded.
- Always ensure sufficient space in the home directory to avoid connectivity issues.
- Use alternative SSH/SCP clients if VScode fails to connect due to quota issues.

## Additional Notes
- Proper software should ideally provide clear error messages in such situations.
- Regularly monitor and manage home directory usage to prevent quota-related issues.
---

### 2020071942000461_SSH%20Verfahren.md
# Ticket 2020071942000461

 ```markdown
# HPC Support Ticket: SSH Verfahren

## Keywords
- SSH
- ssh-keygen
- ssh-copy-id
- Permission denied
- HPC Cluster
- Password authentication

## Problem Description
- User wants to use SSH keys instead of password authentication.
- User followed steps to generate SSH keys and copy the public key to the HPC server.
- User still needs to enter the password when connecting.
- User gets "Permission denied" when trying to check the SSH directory on the HPC account.

## Root Cause
- Insufficient information to diagnose the exact issue.
- Possible issues include incorrect key permissions, incorrect key usage, or server-side configuration problems.

## Solution
- HPC Admin requested the full output of `ssh -v` for further diagnosis.
- User was referred to an HPC-Cafe event for additional help.

## General Learnings
- Ensure proper permissions for SSH keys and directories.
- Use `ssh -v` to gather detailed information for troubleshooting.
- SSH key authentication can be applied to multiple clusters (Emmy, Woody, etc.) once the issue is resolved.

## Next Steps
- User should provide the output of `ssh -v` for further analysis.
- HPC Admin will use the detailed output to diagnose and resolve the issue.
```
---

### 2024032042001869_Cluster%20offline%3F.md
# Ticket 2024032042001869

 ```markdown
# HPC Support Ticket: Cluster Offline?

## Keywords
- Cluster unreachable
- SSH access issue
- Scheduled downtime
- Maintenance

## Problem Description
- User unable to access clusters Woody/Alex via SSH.
- SSH connection attempt results in indefinite waiting.

## Root Cause
- Scheduled maintenance and downtime of HPC systems.

## Solution
- Check the HPC maintenance schedule for any ongoing or upcoming downtimes.
- Inform users about scheduled maintenance periods in advance.

## Lessons Learned
- Regularly update users about maintenance schedules.
- Ensure users are aware of the maintenance calendar to avoid confusion and downtime issues.

## References
- [Scheduled Downtime of HPC Systems on March 11 and 20](https://hpc.fau.de/2024/03/19/scheduled-downtime-of-hpc-systems-on-march-11-and-20/)
```
---

### 2024022942002353_Migration%20of%20ensc001h%20HPC%20account%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20mand.md
# Ticket 2024022942002353

 # HPC Support Ticket Conversation Summary

## Subject
Migration of HPC account to new HPC portal / SSH keys become mandatory

## Keywords
- HPC account migration
- SSH keys
- HPC portal
- Single Sign-On (SSO)
- IdM portal
- SSH key types (RSA, ECDSA, ED25519)
- Usage statistics
- ClusterCockpit
- Jupyterhub

## General Learnings
- **Migration Process**: The HPC account is being migrated from the IdM portal to a new online HPC portal.
- **SSH Keys**: Access to HPC systems will require SSH keys only. Accepted types are RSA (4096 bits), ECDSA (512 bits), and ED25519.
- **Portal Access**: The new HPC portal can be accessed via SSO using IdM credentials.
- **Expiration Notices**: Ignore automatic expiration messages from the IdM portal; the HPC portal will be the sole source for account validity.
- **Account Management**: Contact the PI or project manager for account validity updates or new account requests.
- **Usage Statistics**: Usage of different HPC systems can be viewed in the HPC portal by the user, PI, and project managers.
- **ClusterCockpit and Jupyterhub**: Use SSO links from within the HPC portal for access.

## Root Cause of the Problem
- The migration process requires users to adopt SSH keys for access and familiarize themselves with the new HPC portal.

## Solution
- Generate SSH key pairs with a passphrase and upload the public key to the HPC portal.
- Use the new HPC portal for account management and access to services like ClusterCockpit and Jupyterhub.
- Contact the PI or project manager for any account-related updates.

## Documentation Links
- [SSH Secure Shell Access Documentation](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/)
- [FAQs](https://hpc.fau.de/faqs/#ID-230)

## Additional Notes
- Windows users are recommended to use OpenSSH built into the Windows (Power)Shell or MobaXterm instead of Putty.
- The HPC portal and IdM portal are completely decoupled.
---

### 2023090542002806_AW%3A%20New%20invitation%20for%20%22Studentische%20Abschlu%C3%83%C2%9Farbeiten%20Tier3%20Grundversor.md
# Ticket 2023090542002806

 # HPC Support Ticket: Invitation Not Visible

## Keywords
- HPC Portal
- Invitation
- SSO (Single Sign-On)
- IdM Credentials
- Email Mismatch
- SSH Public Key

## Problem Description
- User received an invitation to access HPC resources but could not see the invitation in their portal after logging in.
- The invitation was sent to `lukas.eller@uni-bayreuth.de`, but the user's SSO login used `bt715254@uni-bayreuth.de`.

## Root Cause
- Mismatch between the email address used for the invitation and the email address associated with the user's SSO login.

## Solution
- HPC Admin modified the invitation to match the email address used by the SSO login (`bt715254@uni-bayreuth.de`).
- User was able to see and accept the invitation after the modification.

## General Learnings
- Ensure that the email address used for invitations matches the email address associated with the user's SSO login.
- If there is a mismatch, HPC Admins can modify the invitation to resolve the issue.
- After accepting the invitation, users should upload their SSH public key to the corresponding account.
---

### 2023042842001354_Format%20Error%20in%20Public%20Key.md
# Ticket 2023042842001354

 # HPC Support Ticket: Format Error in Public Key

## Keywords
- SSH Key
- Public Key
- Format Error
- OpenSSH
- Authorized Keys
- Key Pair Generation

## Problem Description
- User encountered a "Format Error in Public Key" while trying to publish their SSH key.
- The error message indicated that the key was not in the correct format for OpenSSH authorized_keys files.
- User did not receive a public key via mail and requested examples and further steps.

## Root Cause
- The user did not generate or format the SSH key correctly.
- Lack of understanding about the required format for SSH public keys.

## Solution
- **HPC Admin** instructed the user to generate the key pair themselves.
- Provided a link to the documentation: [SSH Secure Shell Access to HPC Systems](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/#ssh_public_key).
- Additional troubleshooting steps for common SSH connection problems were also provided: [FAQs](https://hpc.fau.de/faqs/#ID-230).

## General Learnings
- Users often struggle with the format of SSH keys.
- Documentation should be improved to better explain the key generation and formatting process.
- Providing example keys should be done carefully to avoid misuse.
- Ensure users understand they need to generate their own key pairs.

## Next Steps for Support
- Review and enhance documentation on SSH key generation and formatting.
- Provide clear instructions and examples without compromising security.
- Direct users to relevant documentation and FAQs for common issues.
---

### 2023080942000286_Port%20Forwarding%20-%20GOLD%20docking%20-%20k101ee.md
# Ticket 2023080942000286

 # HPC Support Ticket: Port Forwarding - GOLD Docking

## Subject
Port Forwarding - GOLD docking - k101ee

## User
Joana Massa, PhD student
Institute of Pharmaceutical and Medicinal Chemistry
Corrensstr. 48 / Röntgenstr. 19 48149 Münster
+492518332914
www.agkoch.de

## Problem
The user needs to connect to a license server running on a PC in their university network for a software application. The user has successfully tunneled a port from this PC to the login node using SSH, but the compute nodes cannot access this port.

## Root Cause
- The port forwarding was not globally accessible.
- The compute nodes were trying to access the port on 'fritz.nhr.fau.de', which points to four different servers, leading to inconsistent access.

## Solution
- Use the `-g` parameter in SSH to make the port forwarding globally accessible.
- Specify the exact login node (e.g., 'fritz1' to 'fritz4') where the tunnel is running, instead of using 'fritz.nhr.fau.de'.
- Open the tunnel within the job if the license server should not be widely accessible. Ensure the SSH connection is passwordless and uses IPv6.

## Additional Notes
- The user successfully implemented GNU Parallel for parallelization.
- The HPC Admin suggested optimizing the job script to utilize all cores on a node.
- The HPC Admin proposed a virtual docking afternoon/morning via Zoom to foster experience exchange among projects using docking software.

## Keywords
- Port forwarding
- SSH tunneling
- License server
- GNU Parallel
- Job optimization
- Virtual docking event

## What Can Be Learned
- Proper configuration of SSH tunneling for license server access.
- Optimizing job scripts for better resource utilization.
- Using GNU Parallel for parallelization.
- Importance of specifying exact login nodes for consistent access.
- Collaboration and experience sharing through virtual events.

## Follow-up
- The user expressed interest in participating in the virtual docking event.
- The HPC Admin will coordinate with other centers via the life-science mailing list for potential collaboration on docking solutions.
---

### 2024031142000556_Migration%20of%20bcml%20HPC%20accounts%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20mandato.md
# Ticket 2024031142000556

 # HPC Support Ticket Conversation Summary

## Subject
Migration of bcml HPC accounts to new HPC portal / SSH keys become mandatory

## Keywords
- HPC account migration
- SSH keys
- HPC portal
- Single Sign-On (SSO)
- IdM portal
- Passphrase
- RSA, ECDSA, ED25519
- OpenSSH
- MobaXterm
- ClusterCockpit
- Jupyterhub

## General Learnings
- **Migration Process**: HPC accounts are being migrated from the IdM portal to a new online HPC portal.
- **SSH Keys**: Access to HPC systems will require SSH keys from the end of March. Accepted key types are RSA (4096 bits), ECDSA (512 bits), and ED25519.
- **Portal Access**: The new HPC portal can be accessed via SSO using IdM credentials.
- **Usage Statistics**: Users and their PIs/project managers can view usage statistics in the HPC portal.
- **Service Access**: ClusterCockpit and Jupyterhub services should be accessed via SSO links from the HPC portal.
- **Account Validity**: The HPC portal is the sole source for account validity starting from the end of February.

## Root Cause of the Problem
- Users need to migrate their accounts and set up SSH keys for continued access to HPC systems.

## Solution
- Users should log in to the new HPC portal using SSO and upload their SSH public keys.
- For SSH key generation and usage, users can refer to the provided documentation and FAQs.
- Windows users are recommended to use OpenSSH or MobaXterm.

## Additional Notes
- Users will receive an email about the expiration of their HPC service in the IdM portal, which can be ignored.
- Account validity updates should be communicated to the PI or project manager, not the HPC support team.
- New HPC accounts should also be requested through the PI or project manager.

---

This summary provides a concise overview of the migration process, the requirements for SSH keys, and the changes in account management and service access. It serves as a quick reference for support employees to assist users during the transition.
---

### 2023041242002865_HPC%20Zugang.md
# Ticket 2023041242002865

 ```markdown
# HPC Support Ticket: HPC Zugang

## Keywords
- SSH Key
- HPC Portal
- Permission Denied
- SSH Access
- Documentation

## Problem Description
The user is unable to connect from the dialog server (cshpc) to the front-ends (e.g., ssh iwal075h@woody.nhr.fau.de) despite entering the correct IDM password. The user receives a "Permission denied" error.

## Root Cause
The user is unsure how to use the SSH key created in the HPC portal.

## Solution
1. **Generate SSH Key**: Follow the instructions to generate an SSH key.
2. **Upload SSH Key**: Upload the generated SSH key to the HPC portal.
3. **Wait for Propagation**: Note that it may take up to 2 hours for the SSH key to be distributed across all systems.

## Relevant Documentation
- [SSH Secure Shell Access to HPC Systems](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/#ssh_public_key)
- [NHR@FAU HPC Portal Usage](https://hpc.fau.de/systems-services/documentation-instructions/getting-started/nhrfau-hpc-portal-usage/)
- [SSH, Access, Keys](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/)

## Additional Notes
If the user continues to experience login issues, they should contact HPC support for further assistance.
```
---

### 2024052342002742_Login%20auf%20alex_fritz%20f%C3%83%C2%BCr%20User%20mfbi005h%20von%20cshpc%20nicht%20m%C3%83%C2%B6gli.md
# Ticket 2024052342002742

 # HPC Support Ticket Conversation Analysis

## Subject
Login auf alex/fritz für User mfbi005h von cshpc nicht möglich

## Keywords
- Login issue
- Permission denied
- SSH key
- HPC-Portal
- Configuration

## Summary
A user reported that a colleague (mfbi005h) could not log in to HPC systems alex and fritz, despite being able to access cshpc. The error message indicated a permission issue related to SSH keys.

## Root Cause
- The user's SSH key configuration was likely incorrect or not properly set up for the HPC systems.

## Solution
- The HPC Admin suggested reconfiguring the SSH client according to the provided documentation.
- If the issue persists, the user should run `ssh -vv` to diagnose which keys are being attempted and provide the output to the HPC Admin for further assistance.

## General Learnings
- Ensure that SSH keys are correctly configured for accessing HPC systems.
- Use `ssh -vv` to diagnose SSH connection issues.
- Refer to the HPC documentation for proper SSH configuration templates.
- Note that cshpc will be decommissioned, and users should transition to csnhr if possible.

## References
- [HPC-Portal des RRZE](https://portal.hpc.fau.de/)
- [SSH Configuration Documentation](https://doc.nhr.fau.de/access/ssh-command-line/#template-for-connecting-to-hpc-systems)
---

### 2023112142005501_Projekteinladung%20-%20mfsi.md
# Ticket 2023112142005501

 # HPC Support Ticket Conversation Analysis

## Subject: Projekteinladung - mfsi

### Keywords:
- HPC access
- SSO (Single Sign-On)
- FAU-IdM-Kennung
- DFN-AAI
- eduGAIN
- Gastzugang

### Problem:
- User requested HPC access for a new team member (Kiril).
- The invitation was sent to a non-SSO capable email address (anoshkinki@gmail.com).
- The status of the invitation remained pending.

### Root Cause:
- The email address used for the invitation was not SSO capable.
- The UK-Erlangen does not participate in the DFN-AAI, requiring a FAU-IdM-Kennung for access.

### Solution:
- The user needs to provide an SSO capable email address for the invitation.
- If the user's institution does not participate in DFN-AAI, they need to obtain a FAU-IdM-Kennung for "Beschäftigte vorab" through a paper form and ID verification at RRZE.
- Alternatively, the user can advocate for their institution to join the DFN-AAI to simplify the process.

### General Learnings:
- HPC access requires an SSO capable email address.
- FAU-IdM-Kennung can be obtained for users whose institutions do not participate in DFN-AAI.
- Participation in DFN-AAI or eduGAIN simplifies the access process for academic institutions.
- Gastzugang can be provided to new team members to familiarize themselves with the cluster before their official start.

### Follow-up Actions:
- Update the user on the requirement for an SSO capable email address.
- Provide information on obtaining a FAU-IdM-Kennung if necessary.
- Encourage institutions to join DFN-AAI for easier access.

### References:
- [DFN-AAI Participating Institutions](https://tools.aai.dfn.de/entities/)
- [eduGAIN Federated Organizations](https://technical.edugain.org/isFederatedCheck/Organisations/)
- [FAU-IdM-Kennung Application](https://hpc.fau.de/)
---

### 2024011642003101_ssh%20connection%20to%20fritz.md
# Ticket 2024011642003101

 ```markdown
# HPC Support Ticket: SSH Connection Issue

## Keywords
- SSH Connection
- Connection Reset
- Remote Host
- UNKNOWN Port 65535
- Server Availability

## Problem Description
User encountered an SSH connection error when attempting to connect to the HPC cluster "fritz". The error message received was:
```
client_loop: send disconnect: Connection reset
kex_exchange_identification: Connection closed by remote host
Connection closed by UNKNOWN port 65535
```

## Root Cause
- Temporary server unavailability around 16:50.
- Multiple users reported SSH issues around the same time.

## Solution
- The issue resolved itself after approximately 5 minutes.
- The user was able to reconnect successfully shortly after the incident.

## Lessons Learned
- Temporary server outages can cause SSH connection issues.
- Monitoring server availability and user reports can help identify and resolve such issues quickly.
- Users should be informed about temporary outages and expected resolution times.
```
---

### 2025020342002301_Urgent.md
# Ticket 2025020342002301

 # HPC Support Ticket: Urgent

## Keywords
- VS Code
- Remote OS Selection
- Linux
- Windows
- SSH Connection
- Documentation

## Issue
- User mistakenly selected Linux as the remote OS while setting up HPC access on VS Code from a Windows system.
- Unable to change the OS selection in VS Code settings.

## Root Cause
- Misunderstanding of the remote OS selection in VS Code. The remote OS should be set to Linux as the HPC clusters are Linux systems.

## Solution
- The remote OS selection in VS Code refers to the OS of the remote system, not the local system.
- Ensure the remote OS is set to Linux when connecting to HPC clusters.
- Follow the documentation for setting up SSH connections in VS Code: [VS Code SSH Documentation](https://code.visualstudio.com/docs/remote/ssh#_connect-to-a-remote-host)
- Verify if there are any error messages and check if the user can connect to the HPC systems via the command line: [SSH Command Line Documentation](https://doc.nhr.fau.de/access/ssh-command-line/)

## Additional Resources
- Python environment modules: [Environment Modules](https://doc.nhr.fau.de/environment/modules/)
- Python documentation: [Python SDT](https://doc.nhr.fau.de/sdt/python/), [Python Environment](https://doc.nhr.fau.de/environment/python-env/)
- Introduction for new HPC users: [HPC Café](https://hpc.fau.de/teaching/hpc-cafe/#nutshell)

## Notes
- The user does not have sudo privileges on the HPC systems.
- Ensure the user is familiar with the Linux environment and shells (Bash/Zsh) as the HPC clusters are Linux-based.
---

### 2024031142000716_Migration%20of%20mfpt%20HPC%20accounts%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20mandato.md
# Ticket 2024031142000716

 # HPC Support Ticket Summary

## Subject
Migration of mfpt HPC accounts to new HPC portal / SSH keys become mandatory

## Keywords
- HPC account migration
- SSH keys
- HPC portal
- IdM portal
- Single Sign-On (SSO)
- SSH key types (RSA, ECDSA, ED25519)
- Usage statistics
- ClusterCockpit
- Jupyterhub

## General Learnings
- **Migration Process**: The HPC accounts are being migrated from the IdM portal to a new online HPC portal.
- **SSH Keys**: Access to HPC systems will require SSH keys from the end of March. Accepted types are RSA (4096 bits), ECDSA (512 bits), and ED25519.
- **Portal Access**: The new HPC portal can be accessed via SSO using IdM credentials.
- **Account Validity**: The HPC portal will be the sole source for account validity starting from the end of February.
- **Usage Statistics**: Users, PIs, and project managers can view usage statistics in the HPC portal.
- **ClusterCockpit and Jupyterhub**: Access these services via SSO links within the HPC portal.

## Root Cause of the Problem
- Users need to generate and upload SSH keys to access HPC systems.
- Users need to adapt to the new HPC portal for account management and service access.

## Solution
- Generate SSH key pairs with a passphrase and upload the public key to the HPC portal.
- Use the new HPC portal for account management and accessing services like ClusterCockpit and Jupyterhub via SSO links.
- Contact the PI or project manager for account validity updates.

## Additional Resources
- [SSH Secure Shell Access Documentation](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/)
- [FAQs](https://hpc.fau.de/faqs/#ID-230)

## Notes
- Windows users are recommended to use OpenSSH built into Windows (Power)Shell or MobaXterm instead of Putty.
- Ignore automatic messages from the IdM portal regarding HPC service expiration.
---

### 2023021042001981_HPC%2C%20login%20to%20compute%20node%20on%20fritz.md
# Ticket 2023021042001981

 # HPC Support Ticket: Login to Compute Node on Fritz

## Keywords
- HPC
- Login
- Compute Node
- Fritz
- SSH Forwarding
- Slurm Attach
- SSH Agent Forwarding
- SSH Private Key

## Problem
- User unable to login to compute nodes on Fritz where their jobs are running.

## Root Cause
- User did not know the correct method to login to compute nodes.
- FAQ did not provide clear information on how to login to compute nodes.

## Solutions
1. **SSH Forwarding**: User successfully used SSH forwarding to login to compute nodes.
2. **Slurm Attach**: HPC Admin suggested using "Slurm attach" for shared nodes.
3. **SSH Agent Forwarding**: HPC Admin suggested using SSH agent forwarding.
4. **Additional SSH Private Key**: HPC Admin suggested using an additional SSH private key available on the HPC systems.

## General Learnings
- Users logging in via SSO may need to use SSH forwarding as they might not have created a password.
- On shared nodes with multiple jobs, users cannot influence which job they will be attached to when logging in by SSH.
- Legacy accounts can still use their password with SSH.

## Follow-up Actions
- Update FAQ to include clear information on how to login to compute nodes.
- Ensure users are aware of the different methods to login to compute nodes.
---

### 2022092242000895_access%20woody-ng.md
# Ticket 2022092242000895

 # HPC Support Ticket: Access to Woody-NG

## Issue
- User unable to access `woody-ng.nhr.fau.de` or any other cluster.

## Root Cause
- The user's account was coupled to their PhD affiliation, which had expired.

## Solution
1. **Rename and Update Hostname:**
   - The frontend for Woody-NG was renamed to Woody and is accessible via `woody.nhr.fau.de`.
   - Remove the old frontend from the `<yourhome>/.ssh/known_hosts` file using:
     ```sh
     ssh-keygen -f <yourhome>/.ssh/known_hosts -R woody-ng.nhr.fau.de
     ```

2. **Update Account Affiliation:**
   - The user's HPC account was updated to be coupled with their FAU employee affiliation.
   - It might take a day for this information to propagate to all clusters.

## Additional Issues
- **Conda Installation Error:**
  - The user encountered issues installing `pybind11` using conda.
  - Error: `NoWritablePkgsDirError: No writeable pkgs directories configured.`

## Solution for Conda Issue
1. **Add Package Directory:**
   ```sh
   conda config --add pkgs_dirs $WORK/.conda/pkgs
   ```

2. **Use Conda Environment:**
   - Always use a conda environment or Python virtual environment before installing packages.
   - If using the base environment, run:
     ```sh
     conda config --add envs_dirs $WORK/.conda/envs
     ```

## Additional Information
- **Cluster Status:**
  - No overview website for the new cluster.
  - Use `sinfo` in the shell on the frontend to check the status.

- **Documentation:**
  - Woody throughput cluster documentation available at: [Woody Cluster Documentation](https://hpc.fau.de/systems-services/documentation-instructions/clusters/woody-cluster/)

## Conclusion
- The user's account was successfully updated, and they were able to access the cluster.
- The conda installation issue was resolved by adding a package directory and using a conda environment.
---

### 2024120642002001_New%20Account%3A%20Connecting%20issues%20Fritz.md
# Ticket 2024120642002001

 # HPC Support Ticket: New Account Connecting Issues

## Keywords
- New Account
- SSH Connection Issue
- Cluster: `fritz.nhr.fau.de`
- Cluster: `csnhr.nhr.fau.de`
- First-time Connection

## Summary
A user is experiencing issues connecting to the `fritz.nhr.fau.de` cluster via SSH, despite being able to connect to `csnhr.nhr.fau.de`. This is the user's first attempt to connect to the cluster.

## Root Cause
- The user is unable to establish an SSH connection to `fritz.nhr.fau.de`.
- The user has confirmed access to `csnhr.nhr.fau.de`.

## Solution
- Verify the user's account permissions for `fritz.nhr.fau.de`.
- Check SSH configuration and network settings for `fritz.nhr.fau.de`.
- Provide step-by-step instructions for first-time SSH connection to the cluster.

## General Learning
- New users may encounter SSH connection issues due to configuration or permission problems.
- Always verify account permissions and SSH settings when troubleshooting connection issues.
- Provide clear instructions for first-time users to ensure a smooth onboarding process.

## Next Steps
- HPC Admins should review the user's account and SSH configuration.
- 2nd Level Support team should assist with troubleshooting and provide necessary documentation.
- If the issue persists, escalate to Georg Hager for training and support guidance.
---

### 2024031342001873_login%20with%20private%20key%20is%20not%20working%20-%20mptf07%20_%20Bockstedte.md
# Ticket 2024031342001873

 # HPC Support Ticket Analysis: SSH Key Authentication Issue

## Keywords
- SSH key authentication
- HPC portal
- `from` limitation
- Hostname resolution
- ProxyJump
- `authorized_keys`

## Problem Summary
- User unable to access HPC system via SSH despite successful initial setup.
- SSH key authentication fails due to 'from' limitation not resolving hostnames correctly.

## Root Cause
- The `from` limitation in the SSH key configuration was set to a hostname that the SSH daemon on the server could not resolve.
- The user attempted to use the same SSH key for multiple hosts, leading to potential conflicts.

## Solution
1. **Remove 'from' Limitation**: The user was advised to remove the optional 'from' limitation to allow access from any host.
2. **Update SSH Key**: The user updated the SSH key in the HPC portal and ensured no conflicting keys were present in the `.ssh` directory.
3. **Wait for Key Distribution**: The user waited for the updated SSH key to be distributed across the HPC system.

## General Learnings
- **Hostname Resolution**: Ensure that the SSH daemon can resolve hostnames if using the 'from' limitation.
- **SSH Key Management**: Avoid using the same SSH key for multiple hosts to prevent conflicts.
- **Key Distribution Time**: Allow sufficient time for SSH key updates to propagate across the HPC system.
- **ProxyJump Considerations**: Be aware of IP address changes when using ProxyJump for SSH connections.

## Additional Notes
- The `authorized_keys` file and specific key files in the `.ssh` directory should be managed carefully to avoid authentication issues.
- Regular communication with HPC admins can help resolve complex authentication problems efficiently.
---

### 2023053042003721_ssh%20access%20denied.md
# Ticket 2023053042003721

 # HPC Support Ticket: SSH Access Denied

## Keywords
- SSH Access
- Public Key Authentication
- Config File
- ProxyJump
- Permission Denied

## Problem Description
- User unable to access HPC cluster from a new computer despite adding SSH key and configuring SSH config file.
- User receives "Permission denied" error when attempting to log in using SSH.

## Root Cause
- Incorrect username specified in the SSH config file for the jump host (`cshpc.rrze.fau.de`).
- SSH config file lacks a proper section for the jump host, causing it to fall back to the default username.

## Diagnostic Steps
- User provided the contents of their SSH config file.
- User provided the output of `ssh -vv fritz` for detailed debugging information.

## Solution
- Ensure the SSH config file includes a proper section for the jump host (`cshpc`) with the correct username.
- Example config file:
  ```plaintext
  Host cshpc
  HostName cshpc.rrze.fau.de
  User correct_username
  IdentityFile /home/sec57280/.ssh/fritzkey
  IdentitiesOnly yes
  PasswordAuthentication no
  PreferredAuthentications publickey

  Host fritz
  HostName fritz.nhr.fau.de
  User correct_username
  ProxyJump cshpc.rrze.fau.de
  IdentityFile /home/sec57280/.ssh/fritzkey
  IdentitiesOnly yes
  PasswordAuthentication no
  PreferredAuthentications publickey
  ```

## General Learning
- Always ensure that the SSH config file specifies the correct username for each host.
- The `ProxyJump` directive requires a corresponding section in the config file for the jump host.
- If SSH prompts for a password instead of a passphrase, it indicates a configuration issue that needs to be addressed.

## Next Steps
- Verify the SSH config file and ensure all sections are correctly configured.
- Test the SSH connection again to confirm access.

## Additional Resources
- HPC documentation on SSH configuration.
- Contact HPC Admins or 2nd Level Support team for further assistance.
---

### 2024050342002217_HCP%20cluster%20extension.md
# Ticket 2024050342002217

 ```markdown
# HPC Support Ticket: HCP Cluster Extension

## Keywords
- HPC Cluster
- Account Extension
- SSH Key
- Project Change
- Account Status

## Summary
A user encountered issues while trying to accept an invitation to an HPC cluster after creating and submitting an SSH key. The root cause was identified as an existing account that needed to be extended rather than a new invitation. Additionally, the user's account status had changed from a student thesis project to a project partner, requiring administrative intervention.

## Root Cause
- **Existing Account**: The user's account already existed, causing errors when trying to accept a new invitation.
- **Project Change**: The user's status changed from "student thesis" to "project partners," necessitating an account move.

## Solution
- **Account Extension**: The HPC Admin extended the user's account validity.
- **Project Change**: The HPC Admin confirmed the need to move the account to the new project and corrected the account status.

## Steps Taken
1. **User Actions**:
   - Created and submitted an SSH key.
   - Attempted to accept the invitation but encountered errors.

2. **HPC Admin Actions**:
   - Identified the issue with the existing account.
   - Extended the account validity.
   - Corrected the account status and confirmed the need for a project change.

3. **Supervisor Actions**:
   - Extended the user's account.
   - Resent the invitation to the HCP cluster.

## Conclusion
The user's account was successfully extended and the status corrected. The HPC Admin confirmed the need to move the account to the new project if required. The user should be able to log in and use the account within 2 hours.
```
---

### 2024110742002681_Fwd%3A%20New%20invitation%20for%20%22Studentische%20Abschlu%C3%83%C2%9Farbeiten%20Tier3%20Grundverso.md
# Ticket 2024110742002681

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject
Fwd: New invitation for "Studentische Abschlußarbeiten Tier3 Grundversorgung LS Maschinelles Lernen und Datenanalytik (Prof. B. Eskofier)" waiting at portal.hpc.fau.de

## Keywords
- HPC Portal
- Project Invitation
- SSO Login
- SSH Public Key
- IdM Credentials
- Email Redirection

## Problem
- User received an invitation email for an HPC project but could not see the invitation in the HPC Portal.
- Email was redirected from FAU email to personal email.

## Root Cause
- The invitation was deleted by the sender, which is why it was not visible in the HPC Portal.

## Solution
- User was advised to contact the sender of the invitation to clarify the status of the project invitation.

## General Learnings
- Ensure that invitations are not deleted by the sender before the recipient accepts them.
- Verify the email address to which the invitation was sent and ensure it matches the user's login credentials.
- Users should follow the instructions in the invitation email to log in via SSO using their IdM credentials.
- After accepting the invitation, users should upload an SSH public key ('ssh-rsa') to the corresponding account.

## Actions Taken
- HPC Admin confirmed that the invitation was deleted by the sender.
- User was advised to contact the sender for further clarification.

## Closure
- The ticket was closed after the user was informed about the deleted invitation and advised to contact the sender.
```
---

### 2025012942004048_WG%3A%20Action%20required%20-%20publications%20linked%20with%20NHR%40FAU%20resources.md
# Ticket 2025012942004048

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Keywords
- HPC Account
- SSH Key
- Project Invitation
- Tier3 Grundversorgung
- HPC-Portal
- Export Control Guidelines
- Account Activation

## General Learnings
- **Account Management**: Understanding the process of inviting users to projects and managing their accounts.
- **SSH Key**: Importance of uploading SSH keys for account activation.
- **Project Setup**: Steps required to create a new Tier3 basic supply project.
- **Export Control Guidelines**: Necessity for the PI to log in and confirm these guidelines.

## Root Cause of the Problem
- The user's account had expired due to inactivity and no SSH key was uploaded.
- The user needed to be associated with the correct project under the appropriate PI.

## Solution
- **Account Reactivation**: The simplest solution was to reactivate the user's account if needed.
- **New Invitation**: The PI (Professor) needed to send a new invitation to the user through the HPC-Portal.
- **SSH Key Upload**: The user needed to upload an SSH public key to the corresponding account.
- **Project Association**: Ensure the user is associated with the correct project under the PI's management.

## Steps for PI to Invite User
1. Log in to the HPC-Portal.
2. Navigate to "Management" -> "Tier3 Grundversorgung Lehrstuhl...".
3. Click on "Add new invitation".
4. Enter the user's email address.
5. Submit the invitation.

## Additional Notes
- The PI must confirm the export control guidelines.
- If delegating day-to-day business, additional managers must also log in to the HPC-Portal.
- The PI should request a Tier3 basic supply project by contacting `hpc-support@fau.de` with the names of additional managers and the RRZE customer number.
- Setup and assignment of rights are carried out by NHR@FAU, and the creation of the project can take a few days.
```
---

### 2022051142000467_HPC%20Zugang%20_%20Technischen%20Hochschule%20N%C3%83%C2%BCrnberg%20_%20Fakult%C3%83%C2%A4t%20AMP.md
# Ticket 2022051142000467

 # HPC Support Ticket Conversation Summary

## Keywords
- HPC Access
- SSO Login
- IdP-Freischaltung
- HPC-Portal
- Projektanlegung
- Quota
- Slurm
- Zoom/Teams Meeting

## General Learnings
- **Communication Preference**: Users may prefer a quick call or video meeting over lengthy email exchanges to clarify access and setup details.
- **SSO Login**: Users should be able to log in via SSO on the HPC portal. If not, they should contact their local IT support for IdP-Freischaltung.
- **Project Management**: Users can manage projects and invite new users through the HPC portal without needing paper forms.
- **Account Creation**: New account creation and SSH key provisioning may take some time.

## Root Cause of the Problem
- **SSO Login Issue**: The user was unable to log in via SSO initially due to IdP-Freischaltung not being completed by the local IT department.
- **Project Management Questions**: The user had questions about managing quotas and adding new users to projects.

## Solution
- **SSO Login**: The user was advised to contact their local IT department to complete the IdP-Freischaltung. Once done, the user was able to log in successfully.
- **Project Management**: The HPC admin provided guidance on managing projects, quotas, and adding new users through the HPC portal. A follow-up meeting was scheduled to address any remaining questions.

## Ticket Closure
- The ticket was closed after the user's questions were addressed, and they were able to log in and manage projects on the HPC portal.
---

### 2023100542003535_Migration%20of%20iww8%20HPC%20accounts%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20mandato.md
# Ticket 2023100542003535

 # HPC Support Ticket: Migration of HPC Accounts to New Portal / SSH Keys Mandatory

## Keywords
- HPC account migration
- SSH keys
- HPC portal
- IdM portal
- Single Sign-On (SSO)
- SSH key types (RSA, ECDSA, ED25519)
- Usage statistics
- ClusterCockpit
- Jupyterhub

## Summary
The HPC services at FAU are migrating existing HPC accounts to a new online HPC portal. Users will need to generate and upload SSH keys for access. The new portal will be the sole source for account validity and usage statistics.

## Key Points
- **Migration Process**: Existing HPC accounts are being migrated to a new online HPC portal.
- **SSH Keys**: Access to HPC systems will require SSH keys (RSA, ECDSA, ED25519) by the end of October.
- **Portal Access**: The new HPC portal can be accessed via Single Sign-On (SSO) using IdM credentials.
- **Account Validity**: The new HPC portal will be the only source for account validity and usage statistics.
- **Usage Monitoring**: PIs and project managers can view usage statistics.
- **ClusterCockpit and Jupyterhub**: Access these services via Single Sign-On links from within the HPC portal.

## Action Items
- **Generate SSH Keys**: Users must generate SSH key pairs with passphrases and upload the public keys to the HPC portal.
- **Update Account Validity**: Users should contact their PI or project manager to update account validity.
- **Monitor Usage**: PIs and project managers can monitor usage statistics through the HPC portal.

## Documentation and FAQs
- [SSH Secure Shell Access Documentation](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/)
- [FAQs](https://hpc.fau.de/faqs/#ID-230)

## Tools Recommendation
- **Windows Users**: Use OpenSSH built into Windows (Power)Shell or MobaXterm instead of Putty.

## Additional Notes
- Ignore automatic messages from the IdM portal regarding service expiration.
- The IdM portal and the new HPC portal are completely decoupled.

## Contact
For further assistance, contact the HPC support team at [support-hpc@fau.de](mailto:support-hpc@fau.de).
---

### 2025011342000358_Can%27t%20connect%20to%20HPC%20Systems.md
# Ticket 2025011342000358

 # HPC Support Ticket: Can't connect to HPC Systems

## Keywords
- SSH Key Authentication
- Public Key
- SSH Configuration
- ProxyJump
- Permission Denied
- HPC Account

## Problem Summary
User unable to log into HPC systems despite following the key generation and configuration process.

## Root Cause
- Incorrect assumption that the same account is used for the portal and HPC system.
- Misconfiguration in SSH keys or account name.

## Ticket Conversation
### User
- Created SSH key using `ssh-keygen -t ed25519 -f ~/.ssh/id_ed25519_nhr_fau`.
- Copied public key to the portal.
- Configured `.ssh/config` with appropriate settings for `csnhr.nhr.fau.de` and `fritz.nhr.fau.de`.
- Received "Permission denied (publickey,password)" error.

### HPC Admin
- Informed user that `lu43jih` is a valid HPC account name.
- Suggested using `b157be24` as the correct account.

### User
- Confirmed that using the correct account name resolved the issue.

## Solution
- Ensure the correct HPC account name is used.
- Verify SSH key and configuration settings.

## Lessons Learned
- Always confirm the correct account name for HPC systems.
- Double-check SSH key and configuration settings for accuracy.
- Use verbose SSH output (`ssh -vvv`) to diagnose connection issues.

## Additional Notes
- The user's assumption about account names led to the issue.
- Proper communication and verification of account details are crucial for successful HPC access.
---

### 2018080642000318_Login%20auf%20Lima%20nicht%20m%C3%83%C2%B6glich.md
# Ticket 2018080642000318

 # HPC Support Ticket Analysis

## Subject: Login auf Lima nicht möglich

### Keywords:
- SSH
- Login
- Lima
- Abschaltung

### Problem Description:
- User unable to login to Lima via SSH.
- User inquires if the system is shut down.

### HPC Admin Response:
- No specific response provided.

### Root Cause:
- Unknown, as the HPC Admin did not provide a detailed response.

### Solution:
- Not provided in the conversation.

### General Learnings:
- Importance of clear communication from HPC Admins.
- Potential need for a standardized response for common issues.

### Next Steps:
- Investigate the status of Lima.
- Provide a detailed response to the user regarding the system status.
- Update the knowledge base with troubleshooting steps for SSH login issues.
---

### 2024040342003772_Host%20Key%20Warnmeldung%20cshpc.md
# Ticket 2024040342003772

 ```markdown
# HPC-Support Ticket Conversation: Host Key Warning

## Keywords
- SSH
- Host Key Warning
- DNS
- SSHFP
- ED25519 Key
- LDAP
- Kerberos
- OpenSSH
- Ubuntu
- VerifyHostKeyDNS

## Summary
A user encountered a warning message when attempting to connect from `bdlweb` to `cshpc`. The warning indicated that the remote host identification had changed, suggesting a potential security risk.

## Root Cause
- The ED25519 key was not listed in the DNS entries for `cshpc`, leading to the warning message.
- The DNS entries were incomplete, containing only RSA and ECDSA keys with correct SHA256 hashes, but lacking the ED25519 key.

## Solution
- The user was advised to switch to `csnhr.nhr.fau.de` to avoid the warning.
- Alternatively, the user could disable the DNS host key verification using the `-o VerifyHostKeyDNS=no` option in the SSH command.

## Additional Information
- The `bdlweb` machine runs Ubuntu 22.04.4 LTS with OpenSSH 8.9p1.
- The `/etc/ssh/ssh_known_hosts` file was not present on `bdlweb`.
- The issue might be related to LDAP and Kerberos integration.
- The `cshpc` system is scheduled to be decommissioned soon, so the DNS entries will not be updated.

## Conclusion
The user was able to resolve the issue by switching to a different host (`csnhr.nhr.fau.de`) or by disabling the DNS host key verification. This solution is temporary as the `cshpc` system will be decommissioned in the near future.
```
---

### 2024030142003331_Migration%20iwi5.md
# Ticket 2024030142003331

 # HPC Support Ticket: Migration iwi5

## Keywords
- SSH Key
- HPC Portal
- VS Code
- Access Refused
- Public SSH Key
- Migration

## Problem
- **User Issue**: Access to HPC system refused after migration of iwi5 accounts.
- **Root Cause**: Incorrect setup of SSH key for accessing the HPC system.

## Conversation Summary
- **User**: Received an email about iwi5 account migration and the need to use SSH keys for access. Added public SSH key to HPC Portal but access was refused.
- **HPC Admin**: Provided a link to instructions for generating an SSH key pair and advised to copy/paste the public key content into the HPC Portal.

## Solution
- **Steps**:
  1. Generate an SSH key pair following the instructions at [FAU SSH Key Generation](https://doc.nhr.fau.de/access/ssh-command-line/#generating-an-ssh-key-pair).
  2. Copy the content of the public SSH key.
  3. Paste the public SSH key content into the appropriate area in the HPC Portal.

## Additional Information
- **VS Code Integration**: The user inquired about setting up SSH keys from VS Code, but no specific instructions were provided in the conversation.

## Conclusion
- The user needs to follow the provided instructions to generate and configure the SSH key correctly to regain access to the HPC system.

---

This documentation can be used to assist other users facing similar issues with SSH key configuration after account migration.
---

### 2024071742003491_Not%20able%20to%20run%20slurm%20batch%20job%20using%20alex%20cluster.md
# Ticket 2024071742003491

 # HPC-Support Ticket: Not Able to Run Slurm Batch Job Using Alex Cluster

## Subject
User unable to run slurm batch job using alex cluster due to SSH configuration issues.

## Problem Description
- User attempted to set up SSH configuration to access alex cluster via csnhr.
- Initial SSH command to csnhr prompted for a password, but using the correct key file with the passphrase worked.
- User unable to SSH into alex cluster from csnhr, receiving "Permission denied (publickey,gssapi-keyex,gssapi-with-mic)" error.
- Attempting to use `ssh -J csnhr.nhr.fau.de iwi5221h@alex.nhr.fau.de` resulted in "This account is currently not available."

## Root Cause
- Incorrect SSH configuration leading to authentication issues.
- User attempted to log into csnhr first, which left the key behind, preventing further SSH to alex cluster.

## Solution
- Update SSH configuration to include both csnhr and alex blocks.
- Use `ssh alex.nhr.fau.de` directly from the local machine to utilize the ProxyJump feature.

## Steps Taken
1. **Initial SSH Configuration:**
   ```plaintext
   Host alex.nhr.fau.de alex
       HostName alex.nhr.fau.de
       User iwi5221h
       ProxyJump csnhr.nhr.fau.de
       IdentityFile ~/.ssh/id_ed25519_nhr_fau
       IdentitiesOnly yes
       PasswordAuthentication no
       PreferredAuthentications publickey
       ForwardX11 no
       ForwardX11Trusted no
   ```

2. **Updated SSH Configuration:**
   ```plaintext
   Host csnhr.nhr.fau.de csnhr
       HostName csnhr.nhr.fau.de
       User iwi5221h
       IdentityFile ~/.ssh/id_ed25519_nhr_fau
       IdentitiesOnly yes
       PasswordAuthentication no
       PreferredAuthentications publickey
       ForwardX11 no
       ForwardX11Trusted no

   Host alex.nhr.fau.de alex
       HostName alex.nhr.fau.de
       User iwi5221h
       ProxyJump csnhr.nhr.fau.de
       IdentityFile ~/.ssh/id_ed25519_nhr_fau
       IdentitiesOnly yes
       PasswordAuthentication no
       PreferredAuthentications publickey
       ForwardX11 no
       ForwardX11Trusted no
   ```

3. **Correct SSH Command:**
   ```plaintext
   ssh alex.nhr.fau.de
   ```

## Outcome
- User successfully logged into csnhr but encountered issues when attempting to connect to alex cluster.
- HPC Admins advised to use `ssh alex.nhr.fau.de` directly from the local machine to utilize the ProxyJump feature.

## Additional Notes
- Ensure the SSH key is correctly configured and the passphrase is entered when prompted.
- Verify that the account is active and not temporarily disabled.

## Conclusion
The issue was resolved by updating the SSH configuration and using the correct SSH command to utilize the ProxyJump feature. This ensures the key is forwarded correctly, allowing access to the alex cluster.
---

### 2022041842000591_hpc%20port.md
# Ticket 2022041842000591

 # HPC Support Ticket: SSH Port Number for Third-Party Clients

## Keywords
- HPC login
- SSH port
- PuTTY
- MobaXterm
- Default port

## Problem
A new HPC user is unable to find the port number required to log in to the HPC cluster using third-party clients such as PuTTY or MobaXterm.

## Root Cause
The user is unaware of the default SSH port number used for HPC login.

## Solution
- The default SSH port number is 22.
- Third-party clients like PuTTY and MobaXterm use this port by default, so no changes are typically required.

## Additional Resources
- A YouTube video tutorial is available to guide users through the login process: [YouTube Video](https://youtu.be/J8PqWUfkCrI)

## Conclusion
Users should use the default SSH port number (22) when logging in to the HPC cluster using third-party clients. No additional configuration is usually needed.
---

### 2024022942003389_Migration%20of%20iwtd%20HPC%20account%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20mandator.md
# Ticket 2024022942003389

 # HPC Support Ticket: Migration of HPC Account to New HPC Portal / SSH Keys Become Mandatory

## Keywords
- HPC Account Migration
- HPC Portal
- SSH Keys
- Single Sign-On (SSO)
- IdM Portal
- Export Control Regulations
- Manager Rights
- Account Categories
- ClusterCockpit
- Jupyterhub

## Summary
The HPC support team is migrating HPC accounts from paper-based applications and the IdM portal to a new, purely online HPC portal. This migration involves several steps, including confirming export control regulations, assigning manager rights, categorizing accounts, and transitioning to SSH key-based authentication.

## Key Points
- **Migration to HPC Portal**: The HPC portal is accessible via SSO with IdM credentials.
- **Export Control Regulations**: The Principal Investigator (PI) must log in and confirm export control regulations.
- **Manager Rights**: PI can assign manager rights to one or more employees for day-to-day management.
- **Account Categories**: Accounts are categorized into different types (e.g., iwtd100, iwtd101, iwtd102) for statistical purposes and future re-validation.
- **SSH Keys**: Access to HPC systems will be exclusively via SSH keys after migration. Passwords will no longer be stored.
- **ClusterCockpit and Jupyterhub**: Accessible via SSO through the HPC portal.

## Root Cause of the Problem
- The PI did not respond to the initial request, leading to a delay in the migration process.

## Solution
- The HPC Admin proceeded with the migration, setting the account to expire in October and importing it into the HPC portal. The user was notified via email.

## General Learnings
- **SSH Key Security**: Enhances security by requiring both a passphrase and the SSH key itself, preventing simple password phishing.
- **Account Management**: PIs and managers can handle account lifecycle changes directly in the HPC portal, reducing the need for paper-based applications.
- **Usage Statistics**: PIs and managers can view the compute time usage of their group and individual accounts in the HPC portal.
- **Future Features**: Additional services and features will be integrated into the HPC portal, streamlining access and management.

## Documentation Links
- [SSH Secure Shell Access to HPC Systems](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/)
- [FAQs on SSH](https://hpc.fau.de/faqs/#ID-230)
- [NHR@FAU HPC Portal Usage](https://hpc.fau.de/systems-services/documentation-instructions/getting-started/nhrfau-hpc-portal-usage/)

## Next Steps
- Ensure the PI logs in and confirms the export control regulations.
- Assign manager rights to designated employees.
- Categorize and update account details as needed.
- Inform users about the transition to SSH key-based authentication and provide necessary documentation.

This documentation serves as a guide for support employees to handle similar migration issues in the future.
---

### 2022092042002404_Connecting%20to%20HPC%20systems.md
# Ticket 2022092042002404

 # HPC Support Ticket: Connecting to HPC Systems

## Keywords
- SSH connection
- Host key verification
- Known hosts file
- Password authentication
- Username mismatch

## Problem Description
- User unable to connect to HPC system via SSH.
- Error message indicates remote host identification has changed.
- User receives "Permission denied" error despite entering the correct password.

## Root Cause
- HPC system keys were changed, causing a host key mismatch.
- User attempted to connect with an incorrect username.

## Solution
1. **Host Key Update**: Remove the offending key from the `known_hosts` file.
   ```bash
   ssh-keygen -R woody.rrze.fau.de
   ```
2. **Username Correction**: Ensure the correct username is used for SSH connection.
   ```bash
   ssh correct_username@woody.rrze.fau.de
   ```

## General Learnings
- Regular updates to system keys can cause host key verification issues.
- Users should be informed about key changes and how to update their `known_hosts` file.
- Verify the correct username before attempting to connect to the HPC system.
- Password authentication issues may be due to incorrect usernames or account-related problems.

## Roles Involved
- **HPC Admins**: Provided guidance on updating the `known_hosts` file and corrected the username.
- **User**: Followed instructions to update the `known_hosts` file and attempted to connect with the correct username.

## Additional Notes
- Ensure users are aware of any recent changes to system keys or authentication methods.
- Provide clear instructions for updating the `known_hosts` file and verifying usernames.
---

### 2022110442002216_Woody%20login%20-%3E%20Warning%3A%20Remote%20Host%20Identification%20has%20changed.md
# Ticket 2022110442002216

 # HPC Support Ticket: Remote Host Identification Changed

## Keywords
- SSH
- Remote Host Identification
- Host Key
- Known Hosts
- ECDSA Key
- Man-in-the-Middle Attack
- System Upgrade

## Problem Description
- User receives a warning about remote host identification change when attempting to SSH into `woody`.
- The warning indicates a possible man-in-the-middle attack or a change in the host key.
- User is unable to log in due to strict host key checking.

## Root Cause
- The host key for `woody` has changed due to a recent system upgrade involving new hardware, OS, and location.

## Solution
- Verify the new host key fingerprint with the official documentation.
- Remove the old host key from the `known_hosts` file using the command provided in the warning message:
  ```
  ssh-keygen -f "/home/user/.ssh/known_hosts" -R "woody.rrze.fau.de"
  ```
- Attempt to SSH into `woody` again to accept the new host key.

## Additional Notes
- The official hostname for `woody` has been updated to `woody.nhr.fau.de`, but the old alias will remain functional.
- Other clusters like `meggie` and `alex` were not affected by this issue.

## Documentation Reference
- [Woody Cluster Documentation](https://hpc.fau.de/systems-services/documentation-instructions/clusters/woody-cluster/#collapse_0)
---

### 2023061942002769_Re%3A%20Erinnerung%3A%20HPC-Zugang%20wiederhergestellt.md
# Ticket 2023061942002769

 # HPC Support Ticket Conversation Analysis

## Keywords
- HPC-Portal
- SSH-Key
- Password
- Account Reactivation
- Login Issues

## Summary
- **User Issue**: User unable to log in to HPC-Portal despite account reactivation.
- **Root Cause**: Missing SSH-Key in the HPC-Portal for the user's account.
- **Solution**: User needs to generate and upload an SSH-Key to the HPC-Portal.

## Detailed Analysis
- **Account Reactivation**: User's HPC account was reactivated with an extended duration.
- **Login Method Change**: Password login is no longer supported; SSH-Key is required.
- **User Action**: User attempted to log in but was prompted for a password after entering the SSH-Key.
- **HPC Admin Response**: HPC-Portal does not recognize the SSH-Key for the user's account.
- **Next Steps**: User should generate and upload an SSH-Key to the HPC-Portal. It may take up to 2 hours for the key to be recognized by all HPC systems.

## Instructions for Users
1. **Generate SSH-Key**:
   - On Linux or macOS: `ssh-keygen -t rsa -b 4096` (ensure to set a passphrase).
   - On Windows: Use mobaXterm (ensure key length is at least 4096 bits).
2. **Upload SSH-Key**: Upload the generated SSH-Key to the HPC-Portal.
3. **Wait for Propagation**: It may take up to 2 hours for the key to be recognized by all HPC systems.

## Instructions for Support Employees
- **Verify SSH-Key**: Ensure the user has uploaded the correct SSH-Key to the HPC-Portal.
- **Check Account Status**: Confirm the account is active and the SSH-Key is recognized.
- **Troubleshoot Login Issues**: If the user still encounters issues, assist with generating and uploading the SSH-Key.

## Conclusion
The user's inability to log in was due to the lack of an SSH-Key in the HPC-Portal. Generating and uploading the SSH-Key should resolve the issue. If problems persist, further troubleshooting with the HPC Support team is recommended.
---

### 2023042142000742_vscode%20auf%20compute%20nodes.md
# Ticket 2023042142000742

 ```markdown
# HPC-Support Ticket: vscode auf compute nodes

## User Request
- User wants to use a VSCode remote server (code-server) to debug code in an interactive SLURM job.
- The server would be accessible via SSH or HTTP.
- User is specifically interested in debugging a Julia script on a GPU node.

## HPC Admin Response
- General approach for VSCode and code-server is documented:
  - [VSCode SSH Tunnel](https://code.visualstudio.com/docs/remote/ssh#_forwarding-a-port-creating-ssh-tunnel)
  - [Code-Server Port Forwarding](https://coder.com/docs/code-server/latest/guide#port-forwarding-via-ssh)
- User should ensure proper authentication to prevent unauthorized access to the VSCode instance.
- Port forwarding example:
  ```sh
  ssh -L 8080:127.0.0.1:8080 -J <Benutzer>@cshpc.rrze.fau.de <Benutzer>@tgxxx.rrze.uni-erlangen.de
  ```

## User Workflow
1. Request an interactive job on `tinygpu` using `salloc`.
2. Job granted on `tg062`.
3. SSH configuration:
   ```sh
   Host faudialog
       Hostname cshpc.rrze.fau.de
       user capn100h
       ForwardAgent yes
       PubKeyAuthentication yes
   Host woody
       Hostname woody.nhr.fau.de
       user capn100h
       ProxyJump faudialog
       ForwardAgent yes
       PubKeyAuthentication yes
   Host tinygpu
       Hostname tinyx.nhr.fau.de
       user capn100h
       ProxyJump faudialog
       ForwardAgent yes
       PubKeyAuthentication yes
   Host tg062
       Hostname tg062
       user capn100h
       ProxyJump tinygpu
       ForwardAgent yes
       PubKeyAuthentication yes
   ```
4. Attempt to connect to `tg062` using VSCode remote.

## Issues Encountered
- SSH key/agent not accepted.
- Simple SSH command `ssh -J capn100h@tinyx.nhr.fau.de capn100h@tg062` did not work.

## Troubleshooting Steps
- Replace `-J capn100h@tinyx.nhr.fau.de` with `-J capn100h@cshpc.rrze.fau.de`.
- Provide output of `ssh -vv -J capn100h@cshpc.rrze.fau.de capn100h@tg062`.

## Resolution
- Temporary workaround: Add public keys from the HPC portal to `~/.ssh/authorized_keys`.
- Permanent fix: System administrators resolved the issue, allowing login to TinyGPU nodes with SSH keys from the HPC portal.

## Conclusion
- User confirmed the issue was resolved and thanked the support team.
- Ticket closed.
```
---

### 2024060442003516_New%20account%20-%20iwwm101h.md
# Ticket 2024060442003516

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Keywords
- Account Transfer
- SSH Key Issues
- VPN Access
- Agent Refused Operation
- Permission Issues
- Locked Key
- Agent Configuration
- Security Policies

## Summary
A user with a new FAU account wants to transfer their HPC resources invitation from their previous HU account. The user encounters issues with SSH key authentication and VPN access.

## Root Cause of the Problem
- **Account Transfer**: The user wants to transfer their HPC resources invitation to a new FAU account.
- **SSH Key Issues**: The user encounters issues with SSH key authentication, specifically "signing failed for ED25519" and "agent refused operation."
- **VPN Access**: The user can only access the HPC account with a VPN from FAU.

## Solutions
- **Account Transfer**: The HPC Admins clarified that a new invitation is needed for the new FAU account. However, since the user already has an existing HPC account, the affiliation was changed from HU to FAU.
- **SSH Key Issues**: The HPC Admins suggested that the SSH key might not have been distributed to all clusters yet. They also provided troubleshooting steps, such as adding "-v" to the SSH command line to get more detailed output.
- **Agent Refused Operation**: The HPC Admins suggested that the issue might be due to permission issues, a locked key, agent configuration, or security policies. They recommended trying without the agent by using the command `env SSH_AUTH_SOCK='"" ssh -v iwwm101h@alex.nhr.fau.de`.
- **VPN Access**: The HPC Admins suggested that the user might be experiencing local restrictions at their chair. They also recommended using ProxyJump through csnhr.

## General Learnings
- **Account Transfer**: Changing the affiliation of an existing HPC account is possible if the user belongs to the same group.
- **SSH Key Issues**: SSH key distribution might take up to 2 hours. Detailed output can be obtained by adding "-v" to the SSH command line.
- **Agent Refused Operation**: The issue might be due to permission issues, a locked key, agent configuration, or security policies. Trying without the agent can help identify the issue.
- **VPN Access**: Local restrictions at the user's chair might be responsible for VPN access issues. Using ProxyJump through csnhr can help resolve the issue.
```
---

### 2023030142003556_Umstellung%20der%20HPC-Accounts%20der%20HS-Coburg%20am%20RRZE%20_%20NHR%40FAU%20-%20corz040h.md
# Ticket 2023030142003556

 # HPC Support Ticket Conversation Analysis

## Subject
Umstellung der HPC-Accounts der HS-Coburg am RRZE / NHR@FAU - corz040h

## Keywords
- HPC Accounts
- HS-Coburg
- RRZE / NHR@FAU
- DFN-AAI/eduGAIN
- HPC-Portal
- SSH-PublicKeys
- SSH-Key
- Passwort
- Windows PowerShell
- Windows Subsystem für Linux
- mobaXtern
- OpenSSH
- Putty
- JumpHost-Feature
- Deaktivierung
- Datenlöschung

## Root Cause of the Problem
- The current paper-based system for managing HPC accounts is being transitioned to a new, fully electronic HPC-Portal.
- Users need to log in to the new portal to continue using their HPC accounts.

## Solution
- Users must log in to the HPC-Portal using DFN-AAI/eduGAIN.
- Existing HPC accounts will be linked to the user's identity in the portal.
- Users need to upload SSH-PublicKeys via the "User / Benutzer" tab in the portal.
- SSH-PublicKeys will be synchronized to the HPC systems within two hours.
- After March, access to HPC systems will only be possible via SSH-Key, not password.

## Additional Information
- Detailed instructions for using the HPC-Portal and SSH are provided in the documentation links.
- Windows users are advised to use Windows PowerShell, Windows Subsystem for Linux, or mobaXtern, which include OpenSSH.
- Accounts not linked by the end of March will be deactivated, and associated data will be deleted after three months.
- For further questions, users should contact the support team at HS-Coburg or the specified faculty member at HS-Coburg.

## References
- [HPC-Portal Usage](https://hpc.fau.de/systems-services/documentation-instructions/getting-started/nhrfau-hpc-portal-usage/)
- [SSH Secure Shell Access](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/)
- [FAQ on SSH Access](https://hpc.fau.de/faqs/#innerID-13183)
- [mobaXtern](https://mobaxterm.mobatek.net/)
---

### 2024030142000619_Migration%20of%20iwih%20HPC%20accounts%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20mandato.md
# Ticket 2024030142000619

 # HPC Support Ticket Conversation Summary

## Keywords
- HPC account migration
- SSH keys
- HPC portal
- IdM portal
- Single Sign-On (SSO)
- ClusterCockpit
- Jupyterhub

## General Learnings
- The HPC services at FAU are migrating from the IdM portal to a new online HPC portal.
- Access to HPC systems will require SSH keys starting from March 15th.
- Users should generate SSH key pairs and upload the public key to the HPC portal.
- The HPC portal and IdM portal are decoupled; account validity updates should be communicated to the PI or project manager.
- Usage statistics are visible to PIs and project managers.
- ClusterCockpit and Jupyterhub access should be done via Single Sign-On links from the HPC portal.

## Problem
- User created an SSH key but could not see an active account under the user tab on the HPC portal to add the public key.

## Root Cause
- Fault on the HPC Admin side; the user's account was not properly migrated or visible.

## Solution
- HPC Admin corrected the fault, making the user's HPC account visible on the portal.

## Follow-up
- User should now be able to see their account and upload the SSH public key.

## Documentation Links
- [SSH Secure Shell Access to HPC Systems](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/)
- [FAQs](https://hpc.fau.de/faqs/#ID-230)
- [HPC Portal Documentation](https://doc.nhr.fau.de/hpc-portal/#upload-ssh-public-key-to-hpc-portal)
---

### 2024020642001138_Benutzer%20ki23jiba%20im%20Kurs%20von%20Petra%20Imhof.md
# Ticket 2024020642001138

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject: User in Course Unable to Login Due to SSH Key Issue

### Keywords:
- SSH Key
- Login Issue
- Key Registration
- Key Distribution
- Course User
- Manual Acceleration

### Root Cause:
- User forgot the passphrase for their SSH key and uploaded a new one.
- The new SSH key is not yet registered/distributed, preventing the user from logging in.

### Problem:
- The user cannot work until the new SSH key is registered and distributed.

### Request:
- To manually accelerate the SSH key registration/distribution process to minimize downtime for the user.

### Solution:
- If possible, HPC Admins can manually expedite the SSH key registration/distribution process.
- If not possible, the user will have to wait for the standard processing time.

### General Learning:
- SSH key issues can cause significant downtime for users.
- Manual intervention by HPC Admins can sometimes expedite the resolution of such issues.
- Communication with the support team is crucial for timely resolution.
```
---

### 2024072342000901_problem%20connecting%20to%20the%20clusters%20-%20iwi5223h%20_%20cama252h.md
# Ticket 2024072342000901

 # HPC Support Ticket: Problem Connecting to Clusters

## Keywords
- SSH Key
- Permission Denied
- Publickey
- Password
- Hostbased
- Connection Templates
- SSH Command Line Guide

## Problem Description
User encountered "Permission denied" errors when attempting to access HPC clusters using SSH keys for accounts `iwi5223h` and `cama252h`.

## Root Cause
- Possible incorrect SSH key configuration or usage.
- SSH key distribution delay.

## Troubleshooting Steps
1. **Verify Correct SSH Key Usage**: Ensure the user is using the correct SSH key type (RSA, ECDSA, ED25519) as per the HPC documentation.
2. **Follow SSH Command Line Guide**: Use the connection templates and follow the guide at [SSH Command Line Guide](https://doc.nhr.fau.de/access/ssh-command-line/).
3. **Wait for SSH Key Distribution**: SSH keys may take up to a day to be distributed across all systems.

## Solution
- The user confirmed that the problem was resolved after following the guide and waiting for the SSH key distribution.

## General Learnings
- Always ensure the correct SSH key is used for cluster access.
- Follow the official SSH command line guide for proper configuration.
- Be patient as SSH key distribution may take some time.
- If the problem persists, consider a short Zoom meeting for further troubleshooting.

## Status
- Ticket closed as resolved.
---

### 2024031142000305_Migration%20of%20iwi3%20HPC%20accounts%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20mandato.md
# Ticket 2024031142000305

 # HPC Support Ticket Conversation Summary

## Subject
Migration of iwi3 HPC accounts to new HPC portal / SSH keys become mandatory

## Keywords
- HPC account migration
- SSH keys
- HPC portal
- Single Sign-On (SSO)
- IdM portal
- Passphrase
- RSA, ECDSA, ED25519
- OpenSSH
- MobaXterm
- ClusterCockpit
- Jupyterhub

## General Learnings
- **Migration to New HPC Portal**: The migration process from the IdM portal to a new online HPC portal has started.
- **SSH Keys Mandatory**: From the end of March, access to HPC systems will require SSH keys.
- **SSH Key Types**: Accepted SSH key types are RSA (4096 bits), ECDSA (512 bits), and ED25519.
- **SSH Key Generation**: Users need to generate SSH key pairs with passphrases and upload the public key to the HPC portal.
- **SSO Login**: The new HPC portal uses Single Sign-On (SSO) with IdM credentials.
- **Account Validity**: The HPC portal will be the sole source for account validity starting from the end of February.
- **Usage Statistics**: PIs and project managers can view usage statistics in the HPC portal.
- **ClusterCockpit and Jupyterhub**: Access these services via SSO links from within the HPC portal.

## Root Cause of the Problem
- Users need to migrate their accounts to the new HPC portal and set up SSH keys for continued access.

## Solution
- **Generate SSH Keys**: Follow the documentation to generate SSH key pairs and upload the public key to the HPC portal.
- **Login to HPC Portal**: Use SSO with IdM credentials to access the HPC portal.
- **Ignore IdM Expiration Email**: The HPC service expiration email from the IdM portal can be ignored as the HPC portal will manage account validity.
- **Contact PI/Project Manager**: For account validity updates or new account requests, contact the PI or project manager instead of RRZE.

## Additional Notes
- **Windows Users**: Recommended to use OpenSSH built into Windows (Power)Shell or MobaXterm instead of Putty.
- **Documentation**: Refer to the provided documentation and FAQs for detailed instructions on SSH key setup.

---

This summary provides a concise overview of the migration process and the necessary steps for users to continue accessing HPC services.
---

### 2023101742003531_HPC%20Connection%20Error%20-%20iwfa021h.md
# Ticket 2023101742003531

 # HPC Connection Error - iwfa021h

## Keywords
- HPC Connection Error
- SSH Connection
- Connection Timed Out
- Intermittent Connectivity

## Summary
The user experienced intermittent connectivity issues when trying to connect to their HPC account via SSH. The problem resolved itself temporarily but recurred.

## Root Cause
- Intermittent network issues or server-side problems causing connection timeouts.

## User Reported Issue
- **Error Message:** Connection to 131.188.3.39 port 22: Connection timed out
- **Command Used:** `ssh iwfa021h@cshpc.rrze.fau.de`

## HPC Admin Response
- The HPC Admin suggested using SSH for connection and provided a FAQ link for reference.
- The Admin did not provide a specific solution but acknowledged the intermittent nature of the issue.

## Solution
- The issue resolved itself temporarily, indicating potential network instability or server-side issues.
- Users should try connecting via SSH and report any persistent errors with the command and error message.

## General Learnings
- Intermittent connectivity issues can be due to network problems or server-side issues.
- Users should try connecting via SSH and provide detailed error messages for better troubleshooting.
- The HPC Admin may need to investigate server-side logs or network stability for persistent issues.

## Next Steps
- Monitor the network and server stability.
- Provide users with a standard troubleshooting guide for SSH connection issues.
- Document any recurring issues for future reference and pattern identification.
---

### 2023110242002745_HPC%20Portal%20account%20ihpc120h%20stopped%20working%20for%20Fritz.md
# Ticket 2023110242002745

 # HPC Support Ticket: Account Access Issue

## Keywords
- HPC Portal
- SSH Configuration
- Account Lockout
- Proxy Connection
- VPN
- Visual Studio Code (VSCode)

## Problem Description
- User unable to access HPC cluster (Fritz) since the beginning of the week.
- Account is valid and active in HPC Portal.
- Connection to `cshpc.rrze.fau.de` successful, but connection to `fritz.nhr.fau.de` terminated with message: "This account is currently not available."
- Multiple failed login attempts due to VSCode issue.

## Root Cause
- Disruption of SSH file configuration by Visual Studio Code.
- Possible account lockout due to multiple failed login attempts.

## Troubleshooting Steps
1. **User Actions:**
   - Attempted to change SSH public key multiple times.
   - Resolved part of the problem by connecting via a proxy instead of using a VPN.

2. **HPC Admins:**
   - Requested user to try again after potential account reset or unlock.

## Solution
- User confirmed the account is working again after HPC Admins' intervention.
- Suggested to avoid VSCode for SSH configurations and use proxy connection instead of VPN.

## General Learnings
- Visual Studio Code can disrupt SSH configurations.
- Multiple failed login attempts can lead to account lockout.
- Proxy connection can be a solution when VPN causes issues.
- Regularly check and validate SSH configurations when experiencing connection issues.
---

### 2025022642003883_Unable%20to%20Access%20hpc.fau.de%20from%20csnhr.nhr.fau.de.md
# Ticket 2025022642003883

 # HPC Support Ticket: Unable to Access hpc.fau.de from csnhr.nhr.fau.de

## Keywords
- SSH access
- Public key authentication
- Permission denied
- hpc.fau.de
- csnhr.nhr.fau.de
- authorized_keys

## Problem Description
- User is able to connect to `csnhr.nhr.fau.de` using SSH key.
- Unable to SSH into `hpc.fau.de` from `csnhr.nhr.fau.de`.
- `ssh -v` command hangs or gets `Permission denied (publickey)`.
- `nc -zv hpc.fau.de 22` fails.
- User has manually added public key to `~/.ssh/authorized_keys` on `csnhr.nhr.fau.de`.

## Root Cause
- User is attempting to SSH into `hpc.fau.de`, which is the webserver and not intended for user login.

## Solution
- Inform the user that `hpc.fau.de` is the webserver and not intended for SSH access.
- Direct the user to the getting started guide: [Getting Started Guide](https://doc.nhr.fau.de/getting_started/).
- Suggest attending the next beginners introduction session.

## General Learnings
- Ensure users understand the purpose of different servers.
- Provide clear documentation and training sessions to avoid confusion.
- Verify user access and permissions when troubleshooting SSH issues.

## Next Steps
- Review and update documentation to clarify server roles.
- Ensure users are aware of upcoming training sessions.

---

This report aims to help support employees quickly identify and resolve similar issues in the future.
---

### 2024051642001168_Cannot%20connect%20to%20HPC.md
# Ticket 2024051642001168

 ```markdown
# HPC Support Ticket: Cannot Connect to HPC

## Problem Description
- **User Issue**: Unable to connect to HPC using SSH, receiving "Permission denied (publickey,hostbased)" error.
- **Environment**: Mac machine, using FAU VPN.
- **Actions Taken**: Generated and uploaded public key multiple times.

## Troubleshooting Steps
1. **Configuration Check**:
   - User was asked if they configured `.ssh/config` according to the documentation.
   - User confirmed they followed the steps.

2. **Detailed Error Output**:
   - User was asked to provide the output of `ssh -vv ...` for detailed error information.

3. **Waiting Period**:
   - User was advised to wait for two hours after updating the public key.

## Solution
- **Waiting Period**: After waiting for two hours, the user was able to connect successfully.

## Additional Query
- **Multiple Accounts**: User has access to two different HPC accounts with different usernames.
- **Configuration Management**: User asked how to manage `.ssh/config` for both accounts.

## Recommendation
- **SSH Key Management**: Use different SSH keys for different accounts.
- **Configuration**: Both keys can be configured in one `.ssh/config` file, and SSH will automatically identify the corresponding key for each account.

## Keywords
- SSH Connection
- Public Key Error
- `.ssh/config`
- Multiple HPC Accounts
- FAU VPN
- Mac Machine

## Lessons Learned
- **Public Key Propagation**: Updating public keys may take time to propagate.
- **SSH Configuration**: Proper configuration of `.ssh/config` is crucial for managing multiple SSH keys and accounts.
- **Detailed Error Output**: Using `ssh -vv ...` provides detailed error information for troubleshooting.
```
---

### 2016040542002089_killing%20of%20jobs.md
# Ticket 2016040542002089

 ```markdown
# HPC Support Ticket: Job Killing Issue

## Keywords
- Job killing
- Account availability
- SSH connection error
- Job output file
- Error file
- Prologue
- Epilogue
- Resource request
- Node list
- Power management

## Summary
- **User Issue**: Jobs are getting killed immediately after submission.
- **Error Message**: "This account is currently not available."
- **Additional Issue**: User unable to log in via SSH, receiving error "ssh_exchange_identification: Connection closed by remote host."

## Ticket Conversation
- **Initial Report**: User reports jobs being killed immediately after submission with no information in the error file.
- **Admin Response**: Admin suggests the issue might be temporary due to system hiccups and advises retrying the job.
- **Follow-up**: User reports the issue persists and is unable to log in via SSH.

## Root Cause
- The root cause of the job killing issue is the account being unavailable.
- The SSH connection error indicates a broader system issue affecting user access.

## Solution
- **Admin Action**: Admin acknowledges the issue and suggests retrying the job due to temporary system hiccups.
- **User Action**: User retries the job but the issue persists.
- **Final Resolution**: Admin marks the issue as resolved without specifying the exact fix.

## Lessons Learned
- **Account Availability**: Ensure the user's account is active and available for job submission.
- **System Hiccups**: Temporary system issues can cause job failures and SSH connection problems.
- **Retry Strategy**: Advise users to retry job submissions after temporary system issues.
- **Error Logs**: Check job output files for error messages when error files are empty.

## Documentation for Future Reference
- **Job Output File**: Contains detailed information about job execution, including prologue and epilogue.
- **Resource Request**: Verify requested resources (ncpus, neednodes, nodes, walltime) match available resources.
- **Node List**: Check the list of nodes allocated to the job for any potential issues.
- **Power Management**: Ensure power management settings are correctly configured.

```
---

### 2023030142003494_Umstellung%20der%20HPC-Accounts%20der%20HS-Coburg%20am%20RRZE%20_%20NHR%40FAU%20-%20corz038h.md
# Ticket 2023030142003494

 # HPC-Support Ticket Conversation Summary

## Subject
Umstellung der HPC-Accounts der HS-Coburg am RRZE / NHR@FAU - corz038h

## Keywords
- HPC-Account Umstellung
- HPC-Portal
- SSH-Key
- DFN-AAI/eduGAIN
- Windows PowerShell
- Windows Subsystem für Linux
- mobaXtern
- Putty

## General Learnings
- The HPC accounts at HS-Coburg are transitioning from a paper-based system to a new electronic HPC-Portal.
- Users must log in to the HPC-Portal using DFN-AAI/eduGAIN to link their existing accounts.
- SSH-Keys will be required for accessing HPC systems starting at the end of March.
- Windows users are advised to use Windows PowerShell, Windows Subsystem for Linux, or mobaXtern for SSH access.
- Accounts not linked by the end of March will be deactivated and data deleted after 3 months.

## Root Cause of the Problem
- Incorrect user address in the initial email.

## Solution
- HPC Admin corrected the address and confirmed the rest of the content was accurate.
- User successfully logged into the HPC-Portal and the account was linked.

## Additional Notes
- Detailed instructions and FAQs for the HPC-Portal and SSH access are available on the FAU HPC website.
- For further questions, users should contact the designated support personnel at HS-Coburg.

## References
- [HPC-Portal Usage](https://hpc.fau.de/systems-services/documentation-instructions/getting-started/nhrfau-hpc-portal-usage/)
- [SSH Access](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/)
- [SSH FAQ](https://hpc.fau.de/faqs/#innerID-13183)
- [mobaXtern](https://mobaxterm.mobatek.net/)
---

### 2022091242000931_Remote%20access%20to%20Meggie.md
# Ticket 2022091242000931

 # Remote Access Issue to Meggie

## Keywords
- Remote access
- Meggie
- DNS spoofing
- Remote host identification
- Off-campus access
- Upgrades

## Summary
A user reported difficulties accessing Meggie remotely while off-campus. The user encountered warnings about possible DNS spoofing and changes in remote host identification.

## Root Cause
- Possible changes in Meggie's configuration due to upgrades.
- Potential network or DNS issues affecting remote access.

## Solution
- Verify if there were recent upgrades to Meggie that might have changed its remote access configuration.
- Check DNS settings and ensure there are no spoofing issues.
- Instruct the user to clear their known_hosts file or update it with the new host key.

## Actions Taken
- HPC Admins and 2nd Level Support team investigated the issue.
- Verified recent upgrades and their impact on remote access.
- Provided guidance to the user on updating their known_hosts file.

## Notes
- This issue highlights the importance of communicating changes in system configurations to users.
- Regular updates to known_hosts files may be necessary after system upgrades.
---

### 2023031642003386_Access%20to%20%C3%A2%C2%80%C2%9CGastroDigitalShirt%C3%A2%C2%80%C2%9D%2C%20project%20number%20b131dc.md
# Ticket 2023031642003386

 # HPC Support Ticket: Access to "GastroDigitalShirt", Project Number b131dc

## Keywords
- Affiliation change
- Account migration
- SSH key transfer
- Directory permissions
- Project access

## Summary
A user changed affiliation from FAU to University of Freiburg and needed to migrate data from their old HPC account to the new one. They also encountered issues with SSH key transfer and directory permissions.

## Issues and Solutions

### Account Migration
- **Issue**: User needed to migrate data from old account (`mfhe001h`) to new account (`b131dc11`).
- **Solution**: HPC Admins reactivated the old account temporarily for data copying. Data was copied to subdirectories in the new account's `$HOME` and `$WORK`.

### SSH Key Transfer
- **Issue**: User could not access all clusters with the new SSH key.
- **Solution**: HPC Admins informed the user that SSH keys are transferred to different systems within 2 hours. The user was advised to check the FAQ for more information.

### Directory Permissions
- **Issue**: User could not access copied data in `$WORK` due to permission issues.
- **Solution**: HPC Admins updated the folder permissions to give the user the necessary access.

### Multiple Accounts
- **Issue**: User had two accounts for the same project by mistake.
- **Solution**: One of the accounts (`b131dc12`) was deactivated upon user's request.

## General Learnings
- When changing affiliations, users may need temporary access to their old accounts for data migration.
- SSH keys take time to propagate to all systems.
- Directory permissions may need to be updated after data migration.
- Users should be reminded to check FAQs and documentation for common issues.

## Follow-up
- Ensure that the user has successfully copied all necessary data.
- Verify that the user can access all required clusters with their SSH key.
- Confirm that the user has the correct permissions for all migrated directories.
---

### 2023053142000187_Migration%20of%20iwi9%20HPC%20accounts%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20mandato.md
# Ticket 2023053142000187

 # HPC Support Ticket: Migration of HPC Accounts to New HPC Portal / SSH Keys Become Mandatory

## Keywords
- HPC Portal Migration
- SSH Keys
- Single Sign-On (SSO)
- Manager Role
- Account Validity
- ClusterCockpit
- Jupyterhub

## Summary
The migration of HPC accounts from the IdM portal to a new online HPC portal is underway. Access to HPC systems will require SSH keys only by mid-June. Users need to generate and upload SSH keys to the HPC portal. The HPC portal will be the sole source for account validity.

## Problem
- User without an HPC account cannot upload SSH keys.
- Confusion about the login process for the HPC portal and the need for SSH keys.

## Solution
- The HPC portal login will always be via SSO using IdM credentials.
- SSH keys are required for accessing HPC systems, not for logging into the HPC portal.
- Manager role granted to the user for managing iwi9-Tier3-Grundversorgungsprojekte.

## Details
- **HPC Portal Access**: Login with SSO using IdM credentials.
- **SSH Keys**: Required for accessing HPC systems. Accepted types are RSA (4096 bits), ECDSA (512 bits), and ED25519.
- **Account Validity**: The HPC portal will be the only source for account validity.
- **Manager Role**: Granted to the user for managing specific projects.
- **Usage Statistics**: Visible to PIs and project managers in the HPC portal.
- **ClusterCockpit and Jupyterhub**: Access via Single Sign-On links within the HPC portal.

## Additional Notes
- New HPC accounts and SSH keys may take up to two hours to be recognized across all HPC systems.
- Manager role allows for managing accounts and granting extensions without needing an HPC account.

## Conclusion
The migration to the new HPC portal requires users to generate and upload SSH keys for accessing HPC systems. The portal login remains via SSO using IdM credentials. Manager roles can be granted for administrative purposes without needing an HPC account.
---

### 2024072542005349_Uploading%20ssh-key%20to%20HPC%20Portal%20-%20b143dc15%20and%20iwbi005h.md
# Ticket 2024072542005349

 ```markdown
# HPC-Support Ticket Conversation: Uploading SSH-Key to HPC Portal

## Summary
A user who recently switched to a new faculty position at another university encountered issues with SSH key management for HPC access. The user accidentally deleted their SSH keys and needed assistance to update their keys in the HPC portal.

## Key Points Learned

### User Issue
- **Root Cause**: User accidentally deleted their SSH keys while configuring a new SSH connection.
- **Impact**: Unable to log into the HPC system.

### HPC Admin Responses
- **Initial Response**: Informed the user that they need to upload their SSH key to the HPC portal themselves.
- **Policy Clarification**: Emphasized the need for policies to be followed, such as obtaining permission from the project owner for continued access.
- **Account Management**: Provided steps to log into the HPC portal using the new affiliation email and linking the old accounts to the new email.

### Solution Steps
1. **User Action**: The user was instructed to log into the HPC portal with their new affiliation email.
2. **Admin Action**: The HPC admin linked the user's old accounts to their new email after obtaining permission from the project owner.
3. **SSH Key Management**: The user was able to manage their SSH keys again through the HPC portal.

### Additional Notes
- **Encrypted Emails**: The user initially sent encrypted emails, which were found to be unnecessary for the information exchanged. The user was advised to send unencrypted emails for better communication.
- **Out of Office**: One of the project owners was out of the office, which delayed the permission process.

## Conclusion
The issue was resolved by linking the user's old accounts to their new email and allowing them to manage their SSH keys through the HPC portal. The importance of following policies and obtaining necessary permissions was highlighted.
```
---

### 2024021642002163_Migration%20of%20caph%20HPC%20accounts%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20mandato.md
# Ticket 2024021642002163

 # HPC Support Ticket Summary

## Subject
Migration of HPC accounts to new HPC portal / SSH keys become mandatory

## Keywords
- HPC account migration
- SSH keys
- HPC portal
- Single Sign-On (SSO)
- IdM portal
- ClusterCockpit
- Jupyterhub

## Summary
- **Migration to New HPC Portal**: Users are being migrated from the IdM portal to a new online HPC portal.
- **SSH Keys Mandatory**: Starting end of February, access to HPC systems will require SSH keys. Accepted types are RSA (4096 bits), ECDSA (512 bits), and ED25519.
- **SSH Key Upload**: Users need to generate SSH key pairs with passphrases and upload the public keys to the HPC portal.
- **Documentation and FAQs**: Users unfamiliar with SSH keys should refer to the provided documentation and FAQs.
- **Windows Users**: Recommended to use OpenSSH built into Windows (Power)Shell or MobaXterm instead of Putty.
- **Account Validity**: The HPC portal will be the sole source for account validity. Users should contact their PI or project manager for account updates.
- **Usage Statistics**: Users and their PIs/project managers can view usage statistics in the HPC portal.
- **ClusterCockpit and Jupyterhub**: Users should use Single Sign-On links from within the HPC portal for these services.

## Root Cause
- Migration process requires users to adapt to new authentication methods and portal usage.

## Solution
- Users need to generate and upload SSH keys to the new HPC portal.
- Users should use Single Sign-On links for accessing ClusterCockpit and Jupyterhub.
- For account updates, users should contact their PI or project manager.

## Additional Notes
- The IdM portal and the new HPC portal are completely decoupled.
- Users will receive an email about the expiration of their HPC service in the IdM portal, which can be ignored.
- The HPC portal will not automatically update account validity based on contract extensions or departures from the university.
---

### 2024072242001992_Unable%20to%20login%20to%20the%20cluster%20-%20b165da21.md
# Ticket 2024072242001992

 ```markdown
# HPC Support Ticket: Unable to Login to the Cluster

## Keywords
- Login issue
- Cluster access
- SSH configuration
- User support

## Summary
A user reported being unable to login to the cluster despite the portal indicating that the issue had been resolved. The HPC Admin advised the user to check their SSH configuration.

## Root Cause
- Possible misconfiguration in the user's SSH settings.

## Solution
- The user was directed to verify their SSH configuration using the provided documentation link: [SSH Command Line Configuration](https://doc.nhr.fau.de/access/ssh-command-line/).

## Outcome
- The user confirmed that the issue was resolved after checking their configuration.

## General Learnings
- Always verify SSH configuration when users report login issues.
- Provide users with clear documentation links for troubleshooting common issues.
```
---

### 2025031342000532_Login%20issues%20at%20HPC-Portal.md
# Ticket 2025031342000532

 ```markdown
# HPC-Support Ticket: Login Issues at HPC-Portal

## Keywords
- Login issues
- External PhD student
- FAU email address
- DFN-AAI
- eduGAIN
- University Hospital Würzburg

## Problem Description
- User is an external PhD student and cannot log in to the HPC portal.
- Invitation sent to University Hospital Würzburg email address.
- User does not have a FAU email address.

## Root Cause
- University Hospital Würzburg is not listed in DFN-AAI metadata, although it is part of eduGAIN.
- The HPC portal relies on DFN-AAI for metadata information.

## Solution
- User needs to obtain a FAU email address and a new invitation for that address.
- HPC Admins confirmed that the issue cannot be resolved from their end due to missing metadata in DFN-AAI.

## General Learnings
- Ensure external users have the appropriate institutional email address for access.
- Verify the institution's presence in DFN-AAI metadata for seamless login.
- Communicate with users about the necessity of obtaining an institutional email address if their current one is not supported.
```
---

### 2025012142002715_Accounts%20gel%C3%83%C2%B6scht_%20nicht%20angezeigt%20-%20k107ce21%20-%20TU-Do%20SSO-%C3%83%C2%84nde.md
# Ticket 2025012142002715

 # HPC Support Ticket Analysis

## Subject
Accounts gelöscht/ nicht angezeigt - k107ce21 - TU-Do SSO-Änderung

## Keywords
- HPC Portal
- SSO (Single Sign-On)
- TU Dortmund
- Account Access
- SSH Keys
- User Attributes

## Problem
- User's access to HPC resources (Fritz, Alex, Helma) not displayed in the HPC Portal.
- User can log in with existing SSH keys but cannot change them.
- New SSO attribute from TU Dortmund causing duplicate SSO users.

## Root Cause
- Change in SSO attributes from TU Dortmund leading to the creation of a new SSO user.

## Solution
- Verify with TU Dortmund if the SSO attribute change is intentional.
- If confirmed, update the HPC account to the new SSO user.
- Ensure the correct SSO name is being transmitted from TU Dortmund.

## Actions Taken
- HPC Admin identified the issue with SSO attributes.
- User was advised to clarify the SSO change with TU Dortmund.
- HPC Admin confirmed the correct SSO name was being transmitted and closed the ticket.

## General Learnings
- SSO attribute changes can lead to duplicate users and access issues.
- Coordination with the user's institution is necessary to resolve SSO-related problems.
- Regular checks on SSO attribute transmission can prevent such issues.
---

### 2024090442001781_Passwort%20f%C3%83%C2%BCr%20Cluster-Nutzung%20Meggie.md
# Ticket 2024090442001781

 ```markdown
# HPC Support Ticket: Passwort für Cluster-Nutzung Meggie

## Keywords
- SSH Key
- Passwort
- Meggie
- .ssh/config
- csnh.nhr.fau.de

## Problem
- User cannot log in to Meggie using SSH key.
- User is prompted for a password, but neither IDM password nor SSH key password is accepted.

## Root Cause
- The `.ssh/config` file is not properly configured for direct SSH access to Meggie.

## Solution
- Configure the `.ssh/config` file according to the template provided in the [NHR@FAU documentation](https://doc.nhr.fau.de/access/ssh-command-line/#template-for-connecting-to-hpc-systems).
- Ensure both csnhr and meggie sections are correctly configured.
- Once configured, the user can directly SSH into Meggie without needing to log into csnhr first.

## General Learning
- Proper configuration of the `.ssh/config` file is crucial for seamless SSH access to HPC systems.
- Direct SSH access to Meggie can be achieved by correctly setting up the `.ssh/config` file, eliminating the need for intermediate logins.
```
---

### 2024062842002581_Unable%20to%20Log%20into%20HPC%20-%20Assistance%20Required%20-%20iwi5212h.md
# Ticket 2024062842002581

 ```markdown
# HPC Support Ticket: Unable to Log into HPC

## Subject
Unable to Log into HPC - Assistance Required

## User Issue
The user is unable to log into the HPC system despite multiple attempts and assistance from a colleague. The user provided the output of the `ssh -vv` command for diagnosis.

## Keywords
- SSH login issue
- ProxyJump
- ssh_config
- Connection refused

## Root Cause
The user's `ssh_config` file was missing the necessary configuration block for the `csnhr` host, which is required for the ProxyJump to work correctly.

## Diagnostic Output
```
ssh -vv iwi5212h@tinyx.nhr.fau.de
OpenSSH_9.4p1, LibreSSL 3.3.6
debug1: Reading configuration data /Users/kingfisher/.ssh/config
debug1: /Users/kingfisher/.ssh/config line 1: Applying options for tinyx.nhr.fau.de
debug1: /Users/kingfisher/.ssh/config line 7: Applying options for tinyx.nhr.fau.de
debug1: Reading configuration data /etc/ssh/ssh_config
debug1: /etc/ssh/ssh_config line 21: include /etc/ssh/ssh_config.d/* matched no files
debug1: /etc/ssh/ssh_config line 54: Applying options for *
debug1: Setting implicit ProxyCommand from ProxyJump: ssh -vv -W '[%h]:%p' csnhr.nhr.fau.de
debug1: Authenticator provider $SSH_SK_PROVIDER did not resolve; disabling
debug1: Executing proxy command: exec ssh -vv -W '[tinyx.nhr.fau.de]:22' csnhr.nhr.fau.de
debug1: identity file /Users/kingfisher/.ssh/id_ed25519_nhr_fau type 3
debug1: identity file /Users/kingfisher/.ssh/id_ed25519_nhr_fau-cert type -1
debug1: Local version string SSH-2.0-OpenSSH_9.4
OpenSSH_9.4p1, LibreSSL 3.3.6
debug1: Reading configuration data /Users/kingfisher/.ssh/config
debug1: Reading configuration data /etc/ssh/ssh_config
debug1: /etc/ssh/ssh_config line 21: include /etc/ssh/ssh_config.d/* matched no files
debug1: /etc/ssh/ssh_config line 54: Applying options for *
debug1: Authenticator provider $SSH_SK_PROVIDER did not resolve; disabling
debug1: Connecting to csnhr.nhr.fau.de port 22.
ssh: connect to host csnhr.nhr.fau.de port 22: Connection refused
kex_exchange_identification: Connection closed by remote host
Connection closed by UNKNOWN port 65535
```

## Solution
The HPC Admin suggested that the user's `ssh_config` file was missing the necessary configuration block for the `csnhr` host. The user was advised to include both the `tinyx` and `csnhr` blocks from the provided template.

## Resolution
The user confirmed that adding the missing configuration block resolved the issue, allowing them to successfully log into the HPC system.

## Lessons Learned
- Ensure that the `ssh_config` file includes all necessary configuration blocks for ProxyJump to work correctly.
- Verify that the `ssh_config` file is complete and follows the provided template.
```
---

### 2024011842000314_Migration%20of%20iwia%20HPC%20accounts%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20mandato.md
# Ticket 2024011842000314

 # HPC Support Ticket: Migration of iwia HPC Accounts to New HPC Portal / SSH Keys Become Mandatory

## Keywords
- Migration
- HPC Portal
- SSH Keys
- Single Sign-On (SSO)
- IdM Portal
- Account Validity
- ClusterCockpit
- Jupyterhub

## Summary
The migration process of existing HPC accounts from the IdM portal to a new, purely online HPC portal has begun. Users are required to log in to the new portal and upload SSH keys for continued access.

## Key Points
- **Migration to New HPC Portal**: Users need to log in to the new HPC portal using SSO with IdM credentials.
- **SSH Keys Mandatory**: Access to HPC systems will require SSH keys by the end of January. Accepted key types are RSA (4096 bits), ECDSA (512 bits), and ED25519.
- **Account Validity**: The HPC portal will be the sole source for account validity. Users should contact their PI or project manager to update account validity.
- **Usage Statistics**: The HPC portal will display usage statistics, which will also be visible to PIs and project managers.
- **ClusterCockpit and Jupyterhub**: Users should use the SSO link from within the HPC portal to access these services.

## Documentation and FAQs
- [SSH Secure Shell Access Documentation](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/)
- [FAQs](https://hpc.fau.de/faqs/#ID-230)

## Solution
1. **Log in to the HPC Portal**: Access the portal at [https://portal.hpc.fau.de](https://portal.hpc.fau.de) using SSO with IdM credentials.
2. **Generate and Upload SSH Keys**: Create SSH key pairs with a passphrase and upload the public key to the HPC portal.
3. **Update Account Validity**: Contact the PI or project manager to update account validity as needed.
4. **Access Services**: Use the SSO link from within the HPC portal to access ClusterCockpit and Jupyterhub.

## Additional Notes
- **Windows Users**: Recommended to use OpenSSH built into Windows (Power)Shell or MobaXterm instead of Putty.
- **Account Deletion**: Accounts not logged into within the next 3 months will be considered orphaned and deleted.
- **IdM Portal Expiration**: Ignore automatic messages about HPC service expiration in the IdM portal. The HPC portal will be the relevant source for account validity.
---

### 2023032242001027_SSO%20login%20NHR.md
# Ticket 2023032242001027

 ```markdown
# HPC Support Ticket: SSO Login NHR

## Summary
- **Subject:** SSO login NHR
- **Users:** Two new guest researchers
- **Issue:** SSO login problems

## Keywords
- SSO login
- Email address
- IdM portal
- Postfach-Zustellung
- External Weiterleitung
- RRZE support

## Problem
- Two new guest researchers encountered SSO login issues similar to previous experiences.
- User IDs: `yh77epel`, `zi44bevo`
- `zi44bevo` not activated.
- `yh77epel` missing email address in IdM.

## Root Cause
- Email addresses not properly linked or activated in the IdM portal.
- Missing "Postfach-Zustellung" or external "Weiterleitung" settings.

## Solution
- **For `yh77epel`:**
  - Ensure email address is activated and visible in the overview.
  - Set "Postfach-Zustellung" in the IdM portal.
- **For `zi44bevo`:**
  - Ensure the account is activated.
  - Set "Postfach-Zustellung" in the IdM portal.

## Steps Taken
1. **HPC Admin:**
   - Identified that `zi44bevo` was not activated.
   - Noted that `yh77epel` had no email address in IdM.
   - Suggested contacting RRZE support for further assistance.

2. **RRZE Support:**
   - Confirmed that "Postfach-Zustellung" was not set for `yh77epel`.
   - Provided instructions to set "Postfach-Zustellung" in the IdM portal.

## General Learning
- Ensure email addresses are properly linked and activated in the IdM portal.
- Check for "Postfach-Zustellung" or external "Weiterleitung" settings for guest researchers.
- Escalate to RRZE support if necessary.
```
---

### 2024042342003234_Re%3A%20Reactivated%20account%20ptfs244h%20for%20%22PTFS-Vorlesung%20%28Prof.%20Wellein%29%22%20at%2.md
# Ticket 2024042342003234

 # HPC Support Ticket: SSH Key Replacement Process

## Keywords
- SSH key
- HPC portal
- Account reactivation
- SSH keypair
- Public key upload

## Summary
A user deleted their SSH key from the HPC portal and needed guidance on creating and uploading a new one.

## Root Cause
- User deleted their SSH key and required instructions for creating and uploading a new one.

## Solution
1. **Create a new SSH keypair**: Follow the instructions provided in the [HPC portal documentation](https://doc.nhr.fau.de/access/ssh-command-line/).
2. **Upload the public key**: After generating the new SSH keypair, upload the public key to the HPC portal.
3. **Wait for activation**: The new key will be activated within 24 hours or by the next day.

## Additional Information
- **Account Reactivation**: The user's account was reactivated by an HPC Admin.
- **Storage Consolidation**: The user's home directory and other account folders might have been subjected to storage consolidation operations by the admin team.
- **Existing SSH Keys**: SSH public keys already associated with the account in the HPC portal can be used again without restrictions.

## References
- [HPC Portal Documentation](https://doc.nhr.fau.de/hpc-portal/)
- [SSH Command Line Access](https://doc.nhr.fau.de/access/ssh-command-line/)

## Next Steps for Support
- Ensure the user follows the provided instructions for creating and uploading the new SSH key.
- Monitor the account for any issues related to the new SSH key activation.

---

This documentation can be used to assist users who need to replace their SSH keys in the HPC portal.
---

### 2022101742003407_Unable%20to%20view%20hoc%20account.md
# Ticket 2022101742003407

 # HPC Support Ticket: Unable to View HPC Account

## Keywords
- HPC account visibility
- idM portal
- SSH keys
- HPC portal
- User tab

## Problem
- User unable to see HPC account on idM portal.
- User unable to set a password and use SSH to login.

## Root Cause
- User was looking in the wrong portal (idM) for their HPC account.
- User was unaware of the mandatory use of SSH keys for login.

## Solution
- Inform the user that their HPC account is visible in the HPC portal under the "User" tab.
- Explain that passwords cannot be set for HPC accounts and SSH keys are mandatory for login.
- Provide instructions for uploading SSH public keys through the HPC portal and the approximate time for clusters to recognize uploaded keys.
- Share relevant documentation links for HPC portal usage and SSH key troubleshooting.

## General Learnings
- Users may confuse idM portal with HPC portal.
- SSH keys are essential for HPC system login, and users should be guided on their usage and upload process.
- Clear documentation and FAQs should be provided to assist users in navigating common issues.

## Relevant Links
- [NHR@FAU HPC Portal Usage](https://hpc.fau.de/systems-services/documentation-instructions/getting-started/nhrfau-hpc-portal-usage/)
- [FAQs on SSH Keys](https://hpc.fau.de/faqs/#ID-230)
---

### 2023050242000633_Problem%20by%20runnign%20my%20code%20from%20local%20machine.md
# Ticket 2023050242000633

 ```markdown
# HPC Support Ticket: Problem Running Code from Local Machine

## Keywords
- PyCharm Professional
- Remote Python Interpreter
- SSH Configuration
- GPU Allocation
- Multi-hop SSH
- Virtual Environment

## Summary
The user encountered issues running their code on the HPC system from their local machine using PyCharm Professional. The code could not find the allocated GPU when run directly from PyCharm, but it worked when run from the shell.

## Root Cause
- PyCharm was not correctly configured to connect to the specific node where the job was running.
- The user needed to specify the node name in the SSH Interpreter settings in PyCharm.
- Multi-hop SSH configuration was required to connect to the node through a publicly accessible host.

## Solution
1. **Configure SSH Interpreter in PyCharm**:
   - Specify the node name where the interactive job is running.
   - Adjust the configuration every time the job runs on a different node.

2. **Multi-hop SSH Configuration**:
   - Add the following snippet to the `~/.ssh/config` file:
     ```plaintext
     Host tg0*
       User <account_id>
       ProxyJump tinyx.nhr.fau.de
       # Optionally: when you use SSH keys, uncomment and specify path to private key
       # IdentityFile ~/.ssh/id_....
       # IdentitiesOnly yes
       # PasswordAuthentication no
       # PreferredAuthentications publickey

     Host tinyx.nhr.fau.de
       HostName tinyx.nhr.fau.de
       User <account_id>
       # Optionally: when you use SSH keys, uncomment and specify path to private key
       # IdentityFile ~/.ssh/id_....
       # IdentitiesOnly yes
       # PasswordAuthentication no
       # PreferredAuthentications publickey
     ```

3. **Set the Node Name in PyCharm**:
   - Instead of setting the bastion name (tinyx) as the Host in PyCharm SSH configuration, set the node name (e.g., tg063).

## Conclusion
The user successfully configured PyCharm to connect to the allocated node using multi-hop SSH and was able to run the code with access to the GPU.

## General Learnings
- Ensure that the SSH Interpreter in PyCharm is correctly configured to connect to the specific node where the job is running.
- Use multi-hop SSH configuration to connect to nodes through a publicly accessible host.
- Adjust the SSH Interpreter settings in PyCharm for each job that runs on a different node.
```
---

### 2023060942001271_HPC-Portal%20Migration.md
# Ticket 2023060942001271

 # HPC-Portal Migration Ticket Summary

## Keywords
- HPC-Portal Migration
- FAU SSO
- Dialog Server
- cshpc.rrze.fau.de
- Nomachine
- SSH Key

## Summary
- **User Inquiry:** The user has migrated their HPC account to the new HPC-Portal and is asking about the authentication method for the portal and the access method for the dialog server and Nomachine.
- **Questions:**
  - Will the portal access remain FAU SSO?
  - Will the dialog server (cshpc.rrze.fau.de) and Nomachine require SSH key only?

## Root Cause
- The user is seeking clarification on the authentication and access methods post-migration to the new HPC-Portal.

## Solution
- **Pending:** The solution is not provided in the given conversation. The HPC Admins or 2nd Level Support team need to respond with the relevant information regarding the authentication and access methods.

## General Learnings
- Users may have concerns about changes in authentication and access methods after migrating to a new portal.
- It is important to provide clear communication about any changes in access methods to ensure a smooth transition for users.

## Next Steps
- HPC Admins or 2nd Level Support team should provide the user with the necessary information about the authentication and access methods post-migration.
- Update the knowledge base with the provided solution for future reference.
---

### 2023061442003348_Re%3A%20New%20invitation%20Saad%20Ahmad%20for%20%22GastroDigitalShirt%22%20at%20portal.hpc.fau.de.md
# Ticket 2023061442003348

 # HPC Support Ticket: Email Address Mismatch for SSO Login

## Keywords
- Email address mismatch
- SSO login
- Invitation update
- HPC portal
- University of Freiburg

## Problem Description
- An invitation was sent to a user's email address (`saad.ahmad@mars.uni-freiburg.de`), but the system showed a different email address (`sa312@uni-freiburg.de`) and a personal email (`saadahmed81994@gmail.com`) for the same user.
- The HPC Admin was unsure if these addresses belonged to the same person and how the University of Freiburg transmits email addresses as SSO attributes.

## Root Cause
- The University of Freiburg's IT department (RZ Freiburg) forwards private email addresses, leading to a mismatch in the system.

## Solution
- The HPC Admin confirmed with the user that the personal email address (`saadahmed81994@gmail.com`) was correct.
- The invitation email address was updated to match the personal email address transmitted through SSO/DFN-AAI by the University of Freiburg.
- The user was notified to log in again to the HPC portal to see the updated invitation.

## General Learnings
- Universities may forward private email addresses, causing mismatches in the system.
- Always confirm the correct email address with the user before updating the invitation.
- Update the invitation email address to match the one transmitted through SSO/DFN-AAI to resolve login issues.
---

### 2023030142003467_Umstellung%20der%20HPC-Accounts%20der%20HS-Coburg%20am%20RRZE%20_%20NHR%40FAU%20-%20corz034h.md
# Ticket 2023030142003467

 # HPC-Support Ticket Conversation Summary

## Subject
Umstellung der HPC-Accounts der HS-Coburg am RRZE / NHR@FAU - corz034h

## Keywords
- HPC-Accounts
- HS-Coburg
- RRZE / NHR@FAU
- HPC-Portal
- DFN-AAI/eduGAIN
- SSH-PublicKeys
- SSH-Key
- Passwort
- Windows PowerShell
- Windows Subsystem für Linux
- mobaXtern
- OpenSSH
- Putty
- JumpHost-Feature
- Deaktivierung
- Datenlöschung

## Problem
- Certificate has expired.
- Transition from paper-based system to electronic HPC-Portal.

## Solution
- Users need to log in to the HPC-Portal using DFN-AAI/eduGAIN.
- Existing HPC-Accounts will be linked to the user's identity in the portal.
- Users must upload SSH-PublicKeys for access.
- Access will be restricted to SSH-Key only by the end of March.
- Accounts not linked by the end of March will be deactivated and data deleted after 3 months.

## Additional Information
- Detailed instructions and FAQs are provided in the links mentioned.
- Windows users are advised to use Windows PowerShell, Windows Subsystem for Linux, or mobaXtern.
- Putty is not recommended due to different SSH-Key formats and lack of JumpHost-Feature support.

## Contacts for Further Assistance
- Rechenzentrum der HS-Coburg
- Fakultät Wirtschaftswissenschaften der HS-Coburg

## Important Dates
- End of March: Deadline for linking accounts.
- 3 months after deactivation: Data deletion.

## References
- [HPC-Portal Usage](https://hpc.fau.de/systems-services/documentation-instructions/getting-started/nhrfau-hpc-portal-usage/)
- [SSH Access](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/)
- [FAQ](https://hpc.fau.de/faqs/#innerID-13183)
- [mobaXtern](https://mobaxterm.mobatek.net/)

---

This summary provides a quick reference for support employees to understand the transition process and assist users with similar issues.
---

### 2024021842000438_Migration%20of%20ihpc037h%20HPC%20account%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20mand.md
# Ticket 2024021842000438

 # HPC Support Ticket Conversation Summary

## Subject
Migration of HPC account to new HPC portal / SSH keys become mandatory

## Keywords
- HPC account migration
- SSH keys
- HPC portal
- Single Sign-On (SSO)
- IdM portal
- Passphrase
- RSA, ECDSA, ED25519
- OpenSSH
- MobaXterm
- ClusterCockpit
- Jupyterhub

## General Learnings
- The HPC services are migrating to a new online HPC portal.
- Access to HPC systems will require SSH keys only.
- Accepted SSH key types are RSA (4096 bits), ECDSA (512 bits), and ED25519.
- Users should generate SSH key pairs with passphrases and upload the public keys to the HPC portal.
- The HPC portal and IdM portal are decoupled; the HPC portal will be the sole source for account validity.
- Users should contact their PI or project manager for account validity updates.
- Usage statistics are visible to PIs and project managers.
- ClusterCockpit and Jupyterhub access should be done via Single Sign-On links from the HPC portal.

## Root Cause of the Problem
- Migration process requires users to adapt to new authentication methods and portal usage.

## Solution
- Users should generate and upload SSH keys to the new HPC portal.
- Access HPC systems using SSH keys and the new HPC portal for account management.
- Use Single Sign-On links for ClusterCockpit and Jupyterhub.

## Additional Notes
- Documentation and FAQs are available for users unfamiliar with SSH keys.
- Windows users are recommended to use OpenSSH or MobaXterm.
- Ignore automatic messages from the IdM portal regarding service expiration.
---

### 2024022142001029_Migration%20of%20mpm1%20HPC%20accounts%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20mandato.md
# Ticket 2024022142001029

 # HPC Support Ticket Summary

## Subject
Migration of mpm1 HPC accounts to new HPC portal / SSH keys become mandatory

## Keywords
- HPC account migration
- SSH keys
- HPC portal
- Single Sign-On (SSO)
- IdM portal
- Account validity
- Usage statistics
- ClusterCockpit
- Jupyterhub

## What Can Be Learned
- **Migration Process**: The migration of HPC accounts from the IdM portal to a new online HPC portal is underway.
- **SSH Keys**: Access to HPC systems will require SSH keys (RSA, ECDSA, ED25519) with a passphrase.
- **Portal Access**: The new HPC portal can be accessed via SSO using IdM credentials.
- **Account Validity**: The HPC portal will be the sole source for account validity, decoupled from the IdM portal.
- **Usage Statistics**: Users and PIs can view usage statistics in the HPC portal.
- **ClusterCockpit and Jupyterhub**: Access these services via SSO links within the HPC portal.

## Root Cause of the Problem
- Users need to transition to the new HPC portal and set up SSH keys for continued access.

## Solution
- **Generate SSH Keys**: Users should generate SSH key pairs and upload the public key to the HPC portal.
- **Login via SSO**: Use SSO for accessing the HPC portal, ClusterCockpit, and Jupyterhub.
- **Contact PI/Manager**: For account validity updates, users should contact their PI or project manager.

## Additional Notes
- **Documentation**: Users unfamiliar with SSH keys should refer to the provided documentation and FAQs.
- **Windows Users**: Recommended to use OpenSSH built into Windows (Power)Shell or MobaXterm.

---

This summary provides a concise overview of the migration process, required actions, and key changes for HPC users.
---

### 2023033142001028_Cannot%20ssh%20into%20Alex%20-%20b131dc11.md
# Ticket 2023033142001028

 ```markdown
# HPC Support Ticket: Cannot ssh into Alex

## Keywords
- SSH
- ProxyJump
- Public Key Authentication
- Permission Denied
- Key Distribution Delay
- SSH Config File
- Verbose SSH Output

## Summary
A user encountered issues with SSH access to the Alex cluster, despite having set up SSH keys and followed online instructions.

## Problem Description
- **ProxyJump Configuration Issue**: The user received an error when setting up the `.ssh/config` file for ProxyJump:
  ```
  "b131dc11@cshpc.rrze.fau.de: Permission denied (publickey).
  kex_exchange_identification: Connection closed by remote host
  Connection closed by UNKNOWN port 65535"
  ```
- **SSH Key Distribution Delay**: The user uploaded an SSH key but encountered a delay in key distribution:
  ```
  "b131dc11@alex: Permission denied (publickey,gssapi-keyex,gssapi-with-mic)"
  ```

## Root Cause
- **ProxyJump Configuration**: The `.ssh/config` file was not correctly configured, leading to authentication issues.
- **Key Distribution Delay**: There was a delay in the distribution of the SSH key, which can take up to 2 hours.

## Solution
- **Specify SSH Key File**: The user resolved the issue by specifying the SSH key file explicitly:
  ```
  ssh -i ~/.ssh/cshpc_ssh b131dc11@alex.nhr.fau.de
  ```
- **Verbose SSH Output**: The HPC Admins suggested using `ssh -vvv` to diagnose the issue further if needed.

## Lessons Learned
- Ensure the `.ssh/config` file is correctly configured for ProxyJump.
- Be aware of the delay in SSH key distribution, which can take up to 2 hours.
- Specify the SSH key file explicitly if the default key is not used.
- Use `ssh -vvv` for detailed diagnostic information when troubleshooting SSH issues.
```
---

### 2024021542002245_Migration%20of%20exzi%20HPC%20accounts%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20mandato.md
# Ticket 2024021542002245

 # HPC Support Ticket: Migration of HPC Accounts to New HPC Portal / SSH Keys Become Mandatory

## Keywords
- HPC account migration
- SSH keys
- HPC portal
- IdM portal
- Single Sign-On (SSO)
- ClusterCockpit
- Jupyterhub

## Summary
The HPC services at FAU are migrating existing HPC accounts from the IdM portal to a new, purely online HPC portal. This migration involves several changes, including the mandatory use of SSH keys for accessing HPC systems.

## Key Points to Learn
- **HPC Portal Access**: The new HPC portal can be accessed at [https://portal.hpc.fau.de](https://portal.hpc.fau.de) using Single Sign-On (SSO) with IdM credentials.
- **SSH Keys**: Access to HPC systems will require SSH keys. Accepted key types are RSA (4096 bits), ECDSA (512 bits), and ED25519. Users should generate SSH key pairs with passphrases and upload the public keys to the HPC portal.
- **SSH Key Propagation**: It may take up to two hours for all HPC systems to recognize updated SSH public keys.
- **Documentation**: Users unfamiliar with SSH keys should refer to the documentation and FAQs provided by the HPC support team.
- **Windows Users**: Recommended tools for Windows users are OpenSSH built into Windows (Power)Shell or MobaXterm instead of Putty.
- **IdM Portal Expiration**: Users will receive an email about the expiration of their HPC service in the IdM portal, which can be ignored. The HPC portal will be the sole source for account validity.
- **Account Validity**: The HPC portal and IdM portal are decoupled. Users should contact their PI or project manager to update the validity of their HPC account.
- **Usage Statistics**: The HPC portal displays usage statistics for different HPC systems, which are also visible to PIs and project managers.
- **ClusterCockpit and Jupyterhub**: Users should use the Single Sign-On link from within the HPC portal to access ClusterCockpit and Jupyterhub.

## Root Cause of the Problem
- The migration process requires users to adapt to new authentication methods and portal functionalities.

## Solution
- Users should follow the instructions provided in the migration email to access the new HPC portal, generate and upload SSH keys, and use the Single Sign-On links for accessing related services.

## Additional Notes
- The HPC portal will not automatically update account validity based on contract extensions or departures from the university. Users must manually update their account validity through their PI or project manager.
- The new Jupyterhub instance accessible through the HPC portal has updated software and hardware.
---

### 2024070942004148_Adding%20institutions%20to%20portal.md
# Ticket 2024070942004148

 # HPC Support Ticket: Adding Institutions to Portal

## Keywords
- Institution Addition
- Portal Login
- DFN/AAI
- eduGAIN
- Attribute Release

## Problem
- User requested to add an institution (Centre for Genomic Regulation) to the HPC portal login.
- User inquired about actions they could take from their side.

## Root Cause
- The institution was already listed in eduGAIN but required local admin to release necessary attributes for the HPC portal.

## Solution
- HPC Admins informed the user that institutions are added automatically if they participate in DFN/AAI or eduGAIN.
- The user was advised to have their local admins release the required attributes for the HPC portal.

## General Learnings
- Institutions are not manually added to the HPC portal.
- Participation in DFN/AAI or eduGAIN is required for automatic addition.
- Local admins need to release necessary attributes for the HPC portal.

## Actions Taken
- HPC Admins verified the institution's listing on eduGAIN.
- User was instructed to have local admins release required attributes.

## Follow-up
- No further action required from HPC Admins.
- User acknowledged the information and expressed gratitude.
---

### 2023010342000513_Error%20in%20uploading%20public%20key.md
# Ticket 2023010342000513

 # HPC Support Ticket: Error in Uploading Public Key

## Keywords
- SSH Key Upload
- Public Key Error
- Alias
- Key Content
- Mailing List Subscriptions

## Problem Description
User encountered an error while trying to upload a public SSH key after accepting an invitation. The error message was not clearly visible due to layout issues.

## Root Cause
1. Layout issue affecting the readability of the error message.
2. Possible misunderstanding of the "Alias" and "Key Content" fields during SSH key upload.

## Solution
1. **Layout Issue**: Update the Mailing List Subscriptions on the right-hand side to improve the layout and make the error message readable.
2. **SSH Key Upload**:
   - **Alias**: This can be any short description to help identify the key. It is not the contents of the public key.
   - **Key Content**: This should include the entire contents of the public key, including the "ssh-rsa" at the beginning of the line.

## General Learnings
- Ensure that the layout is updated to make error messages readable.
- Clarify the purpose of the "Alias" and "Key Content" fields for users uploading SSH keys.
- Provide clear instructions on how to correctly input the public key content.

## Next Steps
- If the issue persists, further investigation into the specific error message may be required.
- Ensure that the user has followed the instructions correctly for updating the layout and inputting the SSH key.
---

### 2023030142003431_Umstellung%20der%20HPC-Accounts%20der%20HS-Coburg%20am%20RRZE%20_%20NHR%40FAU%20-%20corz024h.md
# Ticket 2023030142003431

 # HPC Support Ticket Conversation Analysis

## Subject
Umstellung der HPC-Accounts der HS-Coburg am RRZE / NHR@FAU - corz024h

## Keywords
- HPC Accounts
- HS-Coburg
- RRZE / NHR@FAU
- HPC-Portal
- DFN-AAI/eduGAIN
- SSH-PublicKeys
- SSH-Key
- Password
- Windows PowerShell
- Windows Subsystem für Linux
- mobaXterm
- OpenSSH
- Putty
- JumpHost-Feature
- Deactivation
- Data Deletion

## Summary
The HPC accounts of HS-Coburg at RRZE / NHR@FAU are transitioning from a paper-based system to a new, fully electronic HPC-Portal. Users need to log in via DFN-AAI/eduGAIN to ensure their accounts remain active. The transition involves linking existing HPC accounts to user identities in the portal and uploading SSH-PublicKeys for access.

## Root Cause of the Problem
- Certificate expiration
- Need for transition to a new electronic system

## Solution
1. **Login to HPC-Portal**: Users must log in to the HPC-Portal using DFN-AAI/eduGAIN.
2. **Link Account**: Existing HPC accounts will be linked to user identities in the portal.
3. **Upload SSH-PublicKeys**: Users can upload SSH-PublicKeys, which will be synchronized within two hours.
4. **Transition to SSH-Key Access**: By the end of March, access will only be possible via SSH-Key, not password.

## Additional Information
- **Documentation**:
  - HPC-Portal: [HPC-Portal Usage](https://hpc.fau.de/systems-services/documentation-instructions/getting-started/nhrfau-hpc-portal-usage/)
  - SSH and SSH-Keys: [SSH Access](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/)
  - FAQ: [SSH Access FAQ](https://hpc.fau.de/faqs/#innerID-13183)
- **Recommendations for Windows Users**: Use Windows PowerShell, Windows Subsystem für Linux, or mobaXterm, which include OpenSSH as an SSH-Client.
- **Deactivation and Data Deletion**: Accounts not linked by the end of March will be deactivated, and associated data will be deleted after three months.

## Contacts for Further Assistance
- HS-Coburg Rechenzentrum
- Fakultät Wirtschaftswissenschaften der HS-Coburg
- HPC Admins: support-hpc@fau.de

## Conclusion
Users need to follow the outlined steps to ensure their HPC accounts remain active and accessible. Failure to do so will result in account deactivation and data deletion.
---

### 2024032042001011_Tier3%20Grundversorgung%20LS%20Elektronische%20Bauelemente%20%28Prof.%20J.%20Schulze%29.md
# Ticket 2024032042001011

 ```markdown
# HPC Support Ticket: Access Issue to NHR Cluster

## Keywords
- NHR cluster access
- SSH keys
- Permission denied
- Scheduled downtime
- SSH troubleshooting

## Summary
A user reported being unable to access the NHR cluster despite following the setup instructions for SSH keys and configuration. The error message received was "Permission denied (publickey,password)."

## Root Cause
- **Scheduled Downtime**: The HPC systems were undergoing maintenance, which included work on the file servers, resulting in disabled logins to `csnhr` and `cshpc`.

## Steps Taken by User
1. Confirmed project invitation and received HPC account name and home directory.
2. Created and uploaded public/private SSH keys (RSA with 4096 bit).
3. Updated the `/.ssh/config` file with the provided template.

## Solution
- **Wait for Maintenance to Complete**: The user was advised to try logging in again after the scheduled maintenance was completed.
- **SSH Troubleshooting**: If the issue persists, the user was instructed to provide the output of the SSH command with the `-v` option for further troubleshooting.

## Additional Resources
- [Scheduled Downtime Announcement](https://hpc.fau.de/2024/03/19/scheduled-downtime-of-hpc-systems-on-march-11-and-20/)
- [SSH Troubleshooting Documentation](https://doc.nhr.fau.de/access/ssh-command-line/#troubleshooting)

## Conclusion
The issue was likely due to the scheduled maintenance. The user should retry accessing the cluster after the maintenance period and follow the troubleshooting steps if the problem persists.
```
---

### 2018040342000616_HPC-Umgebung%20Humangenetik.md
# Ticket 2018040342000616

 # HPC Support Ticket Conversation Analysis

## Keywords
- Resource Manager
- TORQUE
- CentOS 6
- Public Key
- DSA-Key
- OpenSSH
- RSA-Format

## Issues and Solutions

### Issue 1: Resource Manager Installation
- **Root Cause**: User requested the installation of a Resource Manager (TORQUE) on a system running CentOS 6.
- **Solution**: HPC Admin confirmed that TORQUE would be installed within the week.

### Issue 2: Public Key Authentication
- **Root Cause**: User unable to access other HPC systems using a DSA public key.
- **Solution**: OpenSSH no longer accepts DSA keys by default since version 7.0. User advised to generate and use an alternative public key, such as RSA with sufficient length.

## General Learnings
- **Resource Manager Installation**: Ensure that resource managers like TORQUE are installed and configured correctly on systems running CentOS 6.
- **Public Key Authentication**: Be aware of changes in OpenSSH versions that affect key acceptance. Advise users to use RSA keys instead of DSA keys for better compatibility and security.

## Actions Taken
- HPC Admin confirmed the installation of TORQUE on the specified system.
- User was advised to generate and use an RSA key for public key authentication.

## Follow-Up
- Ensure that the user is able to access other HPC systems using the new RSA key.
- Verify that the TORQUE installation is functioning correctly and address any issues reported by the user.

## References
- [OpenSSH Release Notes](http://www.openssh.com/txt/release-7.0)

## Roles
- **HPC Admins**: Thomas Zeiser
- **2nd Level Support Team**: Lacey, Dane (fo36fizy), Kuckuk, Sebastian (sisekuck), Lange, Florian (ow86apyf), Ernst, Dominik (te42kyfo), Mayr, Martin
- **Head of the Datacenter**: Gerhard Wellein
- **Training and Support Group Leader**: Georg Hager
- **NHR Rechenzeit Support and Applications for Grants**: Harald Lanig
- **Software and Tools Developer**: Jan Eitzinger, Gruber

This documentation aims to assist support employees in resolving similar issues in the future.
---

### 2024022642002939_Cannot%20connect%20via%20SSH.md
# Ticket 2024022642002939

 # HPC Support Ticket: Cannot Connect via SSH

## Keywords
- SSH Connection
- Connection Reset
- Maintenance Downtime

## Issue
User is unable to connect to the HPC TinyGPU front end via SSH. The error messages include:
- `kex_exchange_identification: read: Connection reset by peer`
- `Connection reset by 131.188.3.39 port 22`
- `kex_exchange_identification: Connection closed by remote host`
- `Connection closed by UNKNOWN port 65535`

## Root Cause
The issue is due to scheduled maintenance downtime of the NHR@FAU systems.

## Solution
The user should try again after the maintenance period is over.

## General Learning
- Always check for scheduled maintenance notices before reporting connectivity issues.
- SSH connection errors like `Connection reset by peer` can be indicative of server-side issues or downtime.

## References
- [Scheduled Downtime Notice](https://hpc.fau.de/2024/02/20/scheduled-downtime-of-nhrfau-systems-on-monday-february-26/)
---

### 2024052142002808_Request%20for%20an%20urgent%20appointment%20tomorrow%20for%20resolving%20HPC%20account%20issues.md
# Ticket 2024052142002808

 ```markdown
# HPC Support Ticket: Request for Urgent Appointment for HPC Account Issues

## Summary
- **User Issue**: Unable to access HPC account since Friday night.
- **Root Cause**: SSH key passphrase issue.
- **Solution**: Enter the passphrase selected during SSH keypair creation.

## Keywords
- HPC Account Access
- SSH Key
- Passphrase
- VS Code Integration
- JupyterHub

## Ticket Conversation

### User Initial Request
- **Issue**: Unable to access HPC account; prompted for password despite documentation stating no password required.
- **Details**:
  - Account: mfdp100h
  - Home directory: /home/hpc/mfdp/mfdp100h
  - Principal Investigator: Jana Hutter

### HPC Admin Response
- **Request**: Provide output when connecting with `ssh -v <hostname>`.

### User Follow-up
- **Issue**: SSH key passphrase prompt; IDM password and new SSH key attempts failed.
- **Purpose**: Access JupyterHub from local terminal.

### HPC Admin Solution
- **Solution**: Enter the passphrase selected when creating the SSH keypair.

### User Update
- **Status**: Able to access the system but unable to access through VS Code.

### HPC Admin Advice
- **Advice**: Restart VS Code, delete VS Code caches; SSH is the basis, and as long as it works, the problem is likely in VS Code.

## Lessons Learned
- **SSH Key Management**: Ensure users understand the importance of the passphrase for SSH keys.
- **VS Code Integration**: Troubleshooting steps for VS Code include restarting and clearing caches.
- **Documentation**: Clarify documentation regarding password prompts and SSH key usage.

## Conclusion
- **Resolution**: User regained access by entering the correct SSH key passphrase.
- **Next Steps**: Assist user with VS Code integration issues by providing troubleshooting steps.
```
---

### 2025012342001114_Undeliverable%3A%20%5BExtern%5D%20New%20invitation%20for%20%22M4SKI%20-%20Multi-modal%20human-machin.md
# Ticket 2025012342001114

 # HPC Support Ticket Conversation Analysis

## Subject
- **Title:** Undeliverable: [Extern] New invitation for "M4SKI - Multi-modal human-machine interface with AI (b263ef)" waiting at portal.hpc.fau.de

## Issue
- **Root Cause:** Email bounce-back due to incorrect email address.
- **Details:** The invitation email sent to `vincent.tischler.2@hof-university.de` was undeliverable. The email address was found to be incorrect.

## Actions Taken
- **HPC Admin:**
  - Identified the bounce-back email.
  - Searched for the correct email address on the institute's homepage.
  - Found a slightly different email address: `vincent.tischler.3@hof-university.de`.
  - Suggested sending a new invitation to the corrected email address.

## Solution
- **HPC Admin:**
  - Sent a new invitation to `vincent.tischler.3@hof-university.de`.
  - Successfully created an HPC account for the user.
  - Archived the old invitation.

## Keywords
- Email bounce-back
- Incorrect email address
- Invitation
- HPC account
- Archive

## General Learnings
- Always verify email addresses before sending important communications.
- Use official sources like institute homepages to find correct contact information.
- Archive old invitations once the new ones are successfully sent and the account is created.

## Roles
- **HPC Admins:** Thomas, Michael Meier, Anna Kahler, Katrin Nusser, Johannes Veh
- **2nd Level Support Team:** Lacey, Dane (fo36fizy), Kuckuk, Sebastian (sisekuck), Lange, Florian (ow86apyf), Ernst, Dominik (te42kyfo), Mayr, Martin
- **Head of the Datacenter:** Gerhard Wellein
- **Training and Support Group Leader:** Georg Hager
- **NHR Rechenzeit Support and Applications for Grants:** Harald Lanig
- **Software and Tools Developer:** Jan Eitzinger, Gruber
---

### 2025031442001735_Need%20help%20with%20access%20to%20clusters.md
# Ticket 2025031442001735

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject: Need help with access to clusters

### Keywords:
- SSH
- Permission denied
- Publickey
- GSSAPI
- SSH config
- Troubleshooting
- Cluster access
- HPC account

### Summary:
A user encountered issues accessing HPC clusters via SSH, receiving "Permission denied" errors. The user followed the guidance for SSH access but was unable to connect to the clusters.

### Root Cause:
- The user did not have the correct SSH keys configured for accessing the clusters.
- The user's SSH config was not correctly set up, leading to authentication failures.

### Steps Taken:
1. **User Actions:**
   - Attempted to access clusters (fritz, alex, tinyx, woody) via SSH.
   - Received "Permission denied" errors for all clusters.
   - Provided SSH debug information (`ssh -vv`).

2. **HPC Admin Actions:**
   - Directed the user to set up SSH config as described in the documentation.
   - Provided troubleshooting steps.
   - Analyzed the SSH debug information provided by the user.
   - Confirmed that the user's account is part of an NHR project and can use Alex and Fritz clusters.
   - Informed the user that Alex is suitable for GPU-intensive tasks.

### Solution:
- The user successfully configured the SSH keys and was able to access the Fritz and Alex clusters.
- The user confirmed that the clusters are now accessible and suitable for running the transformer model.

### Conclusion:
- Proper SSH key configuration is crucial for accessing HPC clusters.
- Following the documented steps for SSH setup and troubleshooting can resolve most access issues.
- Users should ensure they have the correct permissions and are aware of the clusters they can access based on their project.

### Additional Notes:
- The user was part of an NHR project and had access to specific clusters (Alex and Fritz).
- The user needed GPU resources, which were available on the Alex cluster.
```
---

### 2023112042004469_Die%20Verwendung%20der%20HPC%20-%20iwnt113h.md
# Ticket 2023112042004469

 # HPC Support Ticket: Die Verwendung der HPC - iwnt113h

## Keywords
- SSH Key
- HPC Account
- Permission Denied
- FAQ
- IDM

## Summary
A user encountered issues with setting up and using an SSH key for their HPC account. The user was unsure about the process and faced permission denied errors.

## Problem
- User did not understand the concept of SSH keys and how to set them up.
- User faced permission denied errors when trying to access the HPC system.

## Solution
1. **Explanation of SSH Keys**:
   - HPC Admin provided information on SSH keys and directed the user to the FAQ for more details.
   - User was advised to consult their supervisor for further assistance.

2. **SSH Key Setup**:
   - User was instructed to upload an SSH key to the HPC portal.
   - It was noted that it takes approximately 2 hours for the SSH key to become active.

3. **Independence from IDM**:
   - HPC Admin clarified that the new HPC account is independent of IDM.
   - User should be able to access the system without a password using the command `ssh iwnt113h@cshpc.rrze.uni-erlangen.de`.

4. **Permission Denied Error**:
   - HPC Admin suggested that the private part of the SSH key might not have been correctly placed on the user's computer.
   - User was directed to the FAQ for SSH debugging information.
   - HPC Admin requested assistance from experienced users in the user's department.

## Additional Notes
- The ticket was eventually closed without a clear resolution to the permission denied error.
- The user was advised to seek help from their supervisor or experienced colleagues.

## Conclusion
The user was provided with information on setting up and using SSH keys for their HPC account. However, the permission denied error was not fully resolved, and the user was advised to seek further assistance.
---

### 2024050342001978_CAMA%20public%20key%20error.md
# Ticket 2024050342001978

 ```markdown
# HPC Support Ticket: CAMA Public Key Error

## Keywords
- SSH Public Key
- Error 400
- Bad Public Key
- Key Content
- HPC Portal
- CAMA Lecture

## Summary
A student encountered an error while trying to submit an SSH public key for a project invitation on the HPC portal. The error message was "Error - Bad Public Key (Status: 400) for ID 'ahad-test-key'".

## Root Cause
The user was attempting to submit an SSH public key but encountered an error due to incorrect key content or format.

## Solution
1. **Verify Key Format**: Ensure the SSH public key matches the required format.
2. **Copy-Paste Entire Key**: Copy and paste the entire content of the public key file (`id-rsa.pub`) into the "key content" box.
3. **Follow Documentation**: Refer to the documentation for detailed instructions on uploading a key: [HPC Portal User Tab](https://doc.nhr.fau.de/hpc-portal/#the-user-tab).

## Additional Steps
- If the issue persists, provide a screenshot of the error and the content entered for further assistance.

## Conclusion
Properly formatted SSH public keys are essential for successful submission. Following the documentation and ensuring the entire key content is copied correctly should resolve the issue.
```
---

### 2024022742002651_Migration%20of%20iwtt%20HPC%20accounts%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20mandato.md
# Ticket 2024022742002651

 # HPC Support Ticket: Migration to New HPC Portal and SSH Key Requirement

## Keywords
- HPC portal migration
- SSH keys
- Single Sign-On (SSO)
- Account validity
- Usage statistics
- ClusterCockpit
- Jupyterhub

## Summary
The HPC services at FAU are migrating to a new online HPC portal. Users need to generate and upload SSH keys for access. The new portal will be the sole source for account validity and usage statistics.

## Key Points
- **Migration to New HPC Portal**: The migration process has started, and users should log in to the new portal using SSO with their IdM credentials.
- **SSH Keys Mandatory**: Starting March 11th, access to HPC systems will require SSH keys. Accepted types are RSA (4096 bits), ECDSA (512 bits), and ED25519.
- **Account Validity**: The new HPC portal is decoupled from the IdM portal. Users should contact their PI or project manager to update account validity.
- **Usage Statistics**: Users and their PIs/project managers can view usage statistics in the new portal.
- **ClusterCockpit and Jupyterhub**: Users should use the SSO link from the HPC portal to access these services.

## Action Items
- Generate and upload SSH keys to the new HPC portal.
- Use the SSO link for ClusterCockpit and Jupyterhub.
- Contact PI or project manager for account validity updates.

## Documentation and FAQs
- [SSH Secure Shell Access Documentation](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/)
- [FAQs](https://hpc.fau.de/faqs/#ID-230)

## Tools Recommended
- OpenSSH built into Windows (Power)Shell
- MobaXterm

## Contact
For further assistance, contact the HPC support team at [support-hpc@fau.de](mailto:support-hpc@fau.de).
---

### 2024050842001531_Guest%20account%20for%20non-academic%20collaborator.md
# Ticket 2024050842001531

 # HPC Support Ticket: Guest Account for Non-Academic Collaborator

## Keywords
- Guest account
- Non-academic collaborator
- FAU IdM account
- HPC portal
- SSO (FAU/DFN-AAI/eduGAIN)
- Export control

## Problem
- User wants to open a guest account for a collaborator who is not in academia.
- Collaborator has a Gmail or company email account.
- User is familiar with sending invitations but unsure about email account requirements.

## Solution
1. **FAU IdM Account Request**:
   - User can request an FAU IdM account for the guest.
   - Guest can use the IdM account to log into the HPC portal.
   - Previously, the [Application-IdMIdentification](https://www.rrze.fau.de/files/2017/07/Application-IdMIdentification.pdf) form was sufficient.
   - Currently, the [d.3 workflow for guest scientists](https://www.intern.fau.de/forschung-organisieren/gastwissenschaftlerinnen-und-gastwissenschaftler/) might be required.

2. **SSO Login**:
   - The ability to log in to the HPC portal through SSO (FAU/DFN-AAI/eduGAIN) is mandatory.

3. **Point of Contact**:
   - The user can be the point of contact in the application document.

## Notes
- There might be export control considerations.
- The exact workflow for guest scientists might have changed, so it's important to check the latest requirements.

## Follow-up
- User will ask the collaborator to fill in the IdM request, endorsed by the user.
- User confirmed that they can be the point of contact in the application document.
---

### 2024042942002921_some%20question%20about%20ssh%20connection.md
# Ticket 2024042942002921

 ```markdown
# SSH Connection Issue: Permission Denied (publickey,password)

## Keywords
- SSH Connection
- Permission Denied
- Public Key
- Password
- SSH Client Configuration
- Private Key Permissions
- Debugging Guide

## Problem Description
The user encountered a "Permission denied (publickey,password)" error while attempting to establish an SSH connection to the server. Despite verifying public keys, checking SSH client configurations, and ensuring correct private key permissions, the issue persisted.

## Troubleshooting Steps
1. **Verify Public Keys**: Ensure that the public keys are correctly configured.
2. **Check SSH Client Configurations**: Review the SSH client settings for any misconfigurations.
3. **Private Key Permissions**: Confirm that the private key permissions are set correctly.

## Solution
1. **Remove Special Characters from Username**: The HPC Admin suggested removing the "< >" characters from the username in the SSH configuration file.
2. **Follow Debugging Guide**: If the issue persists, follow the debugging guide provided by the HPC Admin and include the output with the `-vv` flag for detailed logging.

## Additional Resources
- [SSH Command Line Debugging Guide](https://doc.nhr.fau.de/access/ssh-command-line/)

## Conclusion
The root cause of the problem was likely related to special characters in the username within the SSH configuration file. Following the debugging guide and providing detailed logs can help in further diagnosing the issue if it persists.
```
---

### 2024042942003778_CAMA%20exercise%20HPC%20account.md
# Ticket 2024042942003778

 # HPC Support Ticket: Invalid SSH Key Format

## Keywords
- SSH Key
- Key Format
- Error Message
- Documentation
- Command Line
- MobaXTerm

## Problem
- **Root Cause**: User attempted to upload an SSH key file directly, which resulted in an error stating that 'ssh-rsa' is not a valid key.

## Solution
- **Action Taken**: HPC Admin advised the user to copy-paste the content of the SSH key file instead of uploading the file directly.
- **Additional Guidance**: Provided documentation links for generating SSH key pairs:
  - [Command Line Instructions](https://doc.nhr.fau.de/access/ssh-command-line/)
  - [Windows (MobaXTerm) Instructions](https://doc.nhr.fau.de/access/ssh-mobaxterm/)

## General Learning
- **Key Takeaway**: SSH keys should be copied and pasted as text, not uploaded as files. Ensure users are aware of the correct format and method for submitting SSH keys.

## Documentation Links
- [SSH Command Line Instructions](https://doc.nhr.fau.de/access/ssh-command-line/)
- [SSH MobaXTerm Instructions](https://doc.nhr.fau.de/access/ssh-mobaxterm/)
---

### 2022091942001015_VS%20Code%20Connect%20to%20Woody.md
# Ticket 2022091942001015

 # HPC Support Ticket: VS Code Connection Issue and Woody-ng Partitions

## Keywords
- VS Code
- SSH Connection
- Woody
- Woody-ng
- Partitions
- GPU

## Problem Description
- User unable to establish SSH connection to HPC servers (woody, cshpc) via VS Code, despite successful terminal login.
- User inquires about partitions and GPU availability on woody-ng.

## Root Cause
- Outdated VS Code version causing SSH connection issues.
- Misunderstanding of woody-ng partitions and GPU availability.

## Solution
- **VS Code Connection Issue**: Upgrade VS Code to the latest version (1.71.2) to resolve SSH connection problems.
- **Woody-ng Partitions**:
  - Woody-ng is exclusively for the woodycluster.
  - Use `woody3.rrze.uni-erlangen.de` (to be renamed to `tinyx.nhr.fau.de`) as the frontend.
  - Partitions starting with "work*" are likely compute partitions for general workloads.
  - GPU availability on woody-ng is not explicitly mentioned; users should check with HPC Admins or refer to announcement emails and HPC-Cafe slides for more information.

## General Learnings
- Keeping software (e.g., VS Code) up to date can resolve unexpected connectivity issues.
- Understanding the purpose and configuration of different HPC clusters and partitions is crucial for effective resource utilization.
- Regularly check announcements and updates from the HPC support team for changes in infrastructure and available resources.
---

### 2024082242002079_HPC%20Zugang%20f%C3%83%C2%BCr%20Gastwissenschaftler.md
# Ticket 2024082242002079

 ```markdown
# HPC Support Ticket: HPC Access for Guest Researcher

## Keywords
- HPC Access
- Guest Researcher
- Email Address
- Portal
- TinyGPU
- DFN-AAI
- EduGAIN
- Project

## Problem
- A guest researcher needs HPC access (TinyGPU).
- The guest's email address is not active, preventing access through the portal.

## Solution
- The guest researcher can create an @fau email address to receive an invitation.
- Alternatively, the guest can be invited through their home university if it is part of DFN-AAI or EduGAIN.
- There is a specific project in the portal for guest researchers: `iwi9102 Projektpartner Tier3-Grundversorgung Lehrstuhl für Informatik 9 (Graphische Datenverarbeitung)`.

## Outcome
- The guest researcher successfully created an @fau email address and gained access.

## General Learning
- Guest researchers can gain HPC access by creating an institutional email address or being invited through their home university if it is part of DFN-AAI or EduGAIN.
- Specific projects in the portal are available for guest researchers.
```
---

### 2024022742003016_Migration%20of%20iwst%20HPC%20accounts%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20mandato.md
# Ticket 2024022742003016

 # HPC Support Ticket: Migration of HPC Accounts to New Portal / SSH Keys Mandatory

## Keywords
- HPC account migration
- SSH keys
- HPC portal
- Single Sign-On (SSO)
- IdM portal
- ClusterCockpit
- Jupyterhub

## Summary
The HPC services at FAU are migrating existing HPC accounts from the IdM portal to a new online HPC portal. Access to HPC systems will require SSH keys starting March 11th. Users need to generate and upload SSH keys to the new portal.

## Key Points
- **Migration to New HPC Portal**: The new HPC portal can be accessed at [https://portal.hpc.fau.de](https://portal.hpc.fau.de) using SSO with IdM credentials.
- **SSH Keys Mandatory**: Starting March 11th, access to HPC systems will be via SSH keys only. Accepted types are RSA (4096 bits), ECDSA (512 bits), and ED25519.
- **SSH Key Upload**: Users must generate SSH key pairs with a passphrase and upload the public key to the HPC portal. It may take up to two hours for the update to propagate.
- **Documentation**: Users unfamiliar with SSH keys should refer to the documentation and FAQs at [https://doc.nhr.fau.de/access/overview/](https://doc.nhr.fau.de/access/overview/) and [https://doc.nhr.fau.de/faq/](https://doc.nhr.fau.de/faq/).
- **Windows Users**: Recommended to use OpenSSH built into Windows (Power)Shell or MobaXterm instead of Putty.
- **IdM Portal Expiration**: Users will receive an email about HPC service expiration in the IdM portal, which can be ignored. The HPC portal will be the sole source for account validity.
- **Account Validity**: To update the validity of HPC accounts, users should contact their PI or project manager, not RRZE.
- **Usage Statistics**: The HPC portal displays usage statistics for different HPC systems, visible to PIs and project managers.
- **ClusterCockpit and Jupyterhub**: Users should use the SSO link from the HPC portal to access ClusterCockpit and Jupyterhub.

## Solution
Users need to generate SSH key pairs, upload the public key to the HPC portal, and use the SSO link for accessing ClusterCockpit and Jupyterhub. For account validity updates, users should contact their PI or project manager.

## Additional Notes
- The IdM portal and the new HPC portal are completely decoupled.
- The HPC portal will not automatically update based on contract extensions or departures from the university.
- New HPC accounts should be requested through the PI or project manager, not RRZE.
---

### 2024021942003693_Missing%20invitation%20and%20failed%20login.md
# Ticket 2024021942003693

 # HPC Support Ticket Analysis: Missing Invitation and Failed Login

## Keywords
- Missing invitation
- Failed login
- Single Sign-On (SSO)
- HPC portal
- Email mismatch
- Institution login

## Root Cause of the Problem
- **Email Mismatch**: The invitation was sent to `arne.spang@uni-bayreuth.de`, but the Bayreuth IDP reported the email as `bt308350@uni-bayreuth.de` upon login.
- **Login Issues**: The user attempted to log in with different email addresses, leading to confusion and failed login attempts.

## Solution
- **Update Invitation Email**: The HPC Admin updated the invitation email to match the one reported by the Bayreuth IDP (`bt308350@uni-bayreuth.de`).
- **SSO Login Clarification**: The user was instructed to use Single Sign-On (SSO) with their Bayreuth credentials, not the local login field.

## General Learnings
- **Email Reporting Inconsistencies**: The Bayreuth IDP may report different email addresses for the same user, causing mismatches.
- **SSO Login**: Users should use SSO with their institution's credentials, not the local login field on the HPC portal.
- **Invitation Email Update**: In case of email mismatch, the invitation email can be updated to resolve the issue.

## Troubleshooting Steps for Similar Issues
1. **Check Email Address**: Verify the email address used for the invitation and the one reported by the IDP.
2. **Update Invitation**: If there is a mismatch, update the invitation email to match the IDP-reported address.
3. **SSO Login**: Ensure the user is logging in via SSO with their institution's credentials.

## Relevant Contacts
- **HPC Admins**: For invitation updates and login clarifications.
- **Institution IT Support**: For issues with logging into the institution's SSO.
---

### 2025012842001329_Re%3A%20Visit%20Gerhard%20Wellein_Discussion%20about%20GPU%20infrastructure.md
# Ticket 2025012842001329

 ```markdown
# HPC Support Ticket Conversation Analysis

## Keywords
- Account activation
- Home directory
- SSH key distribution
- Portal access
- GPU infrastructure
- Test accounts
- Visit scheduling

## General Learnings
- **Account Activation**: Re-activating old accounts may not generate new invitations.
- **Home Directory**: Home directories may take several hours to be created after account activation.
- **SSH Key Distribution**: SSH keys may take time to propagate through the system.
- **Portal Access**: Users can log in via EduGAIN using their institutional NetID.
- **GPU Infrastructure**: Discussions about GPU infrastructure and test accounts for AI researchers.
- **Visit Scheduling**: Coordination of visits and meetings for infrastructure discussions.

## Root Cause of Problems
- **Missing Home Directory**: Home directories are not immediately created upon account activation.
- **SSH Key Propagation**: SSH keys take time to be distributed and recognized by the system.

## Solutions
- **Home Directory**: Inform users that home directories will be created within a few hours.
- **SSH Key Propagation**: Advise users to wait for the SSH key to propagate through the system.

## Documentation for Support Employees
### Account Activation and Home Directory
- **Issue**: User's home directory is missing after account activation.
- **Cause**: Home directories are created several hours after account activation.
- **Solution**: Inform the user to wait until the next day for the home directory to be created.

### SSH Key Propagation
- **Issue**: User cannot access the system immediately after adding a new SSH key.
- **Cause**: SSH keys take time to propagate through the system.
- **Solution**: Advise the user to wait for the SSH key to be recognized by the system.

### Portal Access
- **Issue**: User cannot see an invitation in the portal.
- **Cause**: Re-activated accounts may not generate new invitations.
- **Solution**: Inform the user to check the portal and ensure they can log in via EduGAIN using their institutional NetID.

### Visit Scheduling
- **Issue**: Coordination of visits and meetings for infrastructure discussions.
- **Cause**: Multiple stakeholders need to agree on a suitable date.
- **Solution**: Use email communication to coordinate and confirm dates with all relevant parties.
```
---

### 2024022142001216_Migration%20of%20mpt2%20HPC%20accounts%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20mandato.md
# Ticket 2024022142001216

 # HPC Support Ticket Conversation Summary

## Keywords
- HPC account migration
- SSH keys
- HPC portal
- IdM portal
- Single Sign-On (SSO)
- ClusterCockpit
- Jupyterhub
- Usage statistics

## General Learnings
- The HPC account migration process involves moving from the IdM portal to a new online HPC portal.
- Access to HPC systems will require SSH keys only, with specific types and lengths accepted.
- The HPC portal and IdM portal are decoupled, and account validity updates should be communicated to the PI or project manager.
- Usage statistics are visible to PIs and project managers.
- ClusterCockpit and Jupyterhub access should be done through Single Sign-On links from the HPC portal.

## Root Cause of the Problem
- The user's email address was undeliverable, leading to a failed message delivery.

## Solution
- No specific solution provided in the conversation, but the HPC Admin re-sent the migration information.

## Additional Notes
- Windows users are recommended to use OpenSSH built into the Windows (Power)Shell or MobaXterm instead of Putty.
- Documentation and FAQs are available for users unfamiliar with SSH keys.

---

This summary provides key points and general learnings from the HPC support ticket conversation, along with the root cause of the problem and any available solutions.
---

### 2023053042003613_Migration%20of%20bca%20HPC%20accounts%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20mandator.md
# Ticket 2023053042003613

 # HPC Support Ticket: Migration of HPC Accounts to New Portal / SSH Keys Mandatory

## Keywords
- HPC account migration
- SSH keys
- HPC portal
- IdM portal
- Single Sign-On (SSO)
- SSH key types (RSA, ECDSA, ED25519)
- Usage statistics
- ClusterCockpit
- Jupyterhub

## Summary
- **Migration Notice**: HPC accounts are being migrated to a new online HPC portal.
- **Access Change**: Access to HPC systems will require SSH keys by mid-June.
- **SSH Key Requirements**: RSA (4096 bits), ECDSA (512 bits), ED25519.
- **Portal Access**: Login via SSO using IdM credentials.
- **Usage Monitoring**: PIs and project managers can view usage statistics.
- **ClusterCockpit & Jupyterhub**: Access via SSO links within the HPC portal.

## Root Cause of the Problem
- Expiration of HPC service in the IdM portal.
- Need for SSH key-based access.

## Solution
- **SSH Key Generation**: Users need to generate SSH key pairs with a passphrase and upload the public key to the HPC portal.
- **Portal Access**: Users should log in to the new HPC portal using SSO with their IdM credentials.
- **Ignore IdM Expiration Notice**: Users can ignore the automatic expiration message from the IdM portal.
- **Account Validity**: Contact the PI or project manager to update the validity of the HPC account.

## Additional Notes
- **Documentation**: Users unfamiliar with SSH keys should refer to the provided documentation and FAQs.
- **Windows Users**: Recommended to use OpenSSH built into Windows (Power)Shell or MobaXterm instead of Putty.
- **Usage Statistics**: PIs and project managers can monitor usage statistics in the HPC portal.

## Follow-Up
- **User Response**: The user is on vacation until 06.06.2023 and may reply with a delay.

---

This documentation provides a concise overview of the migration process, SSH key requirements, and access changes for HPC users. It also includes solutions for common issues and additional notes for support employees.
---

### 2024091142001259_Private%20key%20and%20public%20key%20-%20b205cb10.md
# Ticket 2024091142001259

 ```markdown
# HPC Support Ticket Analysis: Private Key and Public Key

## Summary
This support ticket involves a user who lost access to their HPC account due to a stolen computer. The user needed to regenerate SSH keys and configure their new machine to access the HPC system.

## Key Issues and Solutions

### 1. Lost SSH Keys
- **Problem**: The user's computer was stolen, and they lost their SSH keys.
- **Solution**: Generate a new SSH key pair and upload the public key to the HPC portal.

### 2. Configuring SSH
- **Problem**: The user had difficulty configuring the SSH settings to connect to the HPC systems.
- **Solution**: Provide a template for the `.ssh/config` file and ensure the user replaces placeholders with their specific details.

### 3. Alias and Key Content in HPC Portal
- **Problem**: The user was unsure about what to put in the "ALIAS" and "Key Content" fields in the HPC portal.
- **Solution**: Explain that the alias is a label for the key, and the key content is the content of the public key file (`.pub`).

### 4. SSH Agent and Permissions
- **Problem**: The user encountered errors related to SSH agent permissions.
- **Solution**: Use the `ssh-add -D` command to remove all identities and re-enter the passphrase. Ensure the SSH key file has the correct permissions.

### 5. Forgotten Password
- **Problem**: The user forgot their password to the HPC portal.
- **Solution**: The admin can reset the password or provide instructions for password recovery.

## Steps Taken

1. **Generate New SSH Keys**:
   - The user was instructed to generate a new SSH key pair using the command:
     ```bash
     ssh-keygen -t ed25519 -C "user@example.com"
     ```
   - The user was advised to use a different passphrase from the one used previously.

2. **Upload Public Key**:
   - The user uploaded the content of the public key file (`.pub`) to the HPC portal.

3. **Configure SSH**:
   - The user created a `.ssh/config` file with the following template:
     ```plaintext
     Host csnhr.nhr.fau.de csnhr
         HostName csnhr.nhr.fau.de
         User <HPC account>
         IdentityFile ~/.ssh/id_ed25519_nhr_fau
         IdentitiesOnly yes
         PasswordAuthentication no
         PreferredAuthentications publickey
         ForwardX11 no
         ForwardX11Trusted no

     Host fritz.nhr.fau.de fritz
         HostName fritz.nhr.fau.de
         User <HPC account>
         ProxyJump csnhr.nhr.fau.de
         IdentityFile ~/.ssh/id_ed25519_nhr_fau
         IdentitiesOnly yes
         PasswordAuthentication no
         PreferredAuthentications publickey
         ForwardX11 no
         ForwardX11Trusted no

     Host alex.nhr.fau.de alex
         HostName alex.nhr.fau.de
         User <HPC account>
         ProxyJump csnhr.nhr.fau.de
         IdentityFile ~/.ssh/id_ed25519_nhr_fau
         IdentitiesOnly yes
         PasswordAuthentication no
         PreferredAuthentications publickey
         ForwardX11 no
         ForwardX11Trusted no
     ```
   - The user replaced `<HPC account>` with their actual HPC account username.

4. **SSH Agent and Permissions**:
   - The user was instructed to use the `ssh-add -D` command to remove all identities and re-enter the passphrase.
   - The user ensured that the SSH key file had the correct permissions using the `ls -l` command.

5. **Password Recovery**:
   - The admin reset the user's password or provided instructions for password recovery.

## Conclusion
The user successfully regenerated their SSH keys, configured their SSH settings, and regained access to the HPC system. The admin provided assistance with password recovery and ensured the user's new keys were properly configured.

## Future Reference
This report can be used as a reference for similar issues in the future. It outlines the steps for regenerating SSH keys, configuring SSH settings, and resolving common errors related to SSH agent permissions and password recovery.
```
---

### 2024021542001148_Migration%20of%20mpap%20HPC%20accounts%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20mandato.md
# Ticket 2024021542001148

 # HPC Support Ticket: Migration of mpap HPC Accounts to New HPC Portal / SSH Keys Become Mandatory

## Keywords
- HPC Portal Migration
- SSH Keys
- Manager Role Assignment
- Single Sign-On (SSO)
- Account Validity
- Usage Statistics
- ClusterCockpit
- Jupyterhub

## Summary
The HPC services at FAU are migrating existing HPC accounts from the IdM portal to a new, purely online HPC portal. This migration involves several changes, including the mandatory use of SSH keys for access and the decoupling of the IdM and HPC portals.

## Key Points to Learn

### Migration Process
- **New HPC Portal**: Accessible at [HPC Portal](https://portal.hpc.fau.de).
- **Login**: Use Single Sign-On (SSO) with IdM credentials.
- **SSH Keys**: Mandatory for access starting at the end of February. Accepted types are RSA (4096 bits), ECDSA (512 bits), and ED25519.
- **Documentation**: Available for SSH key generation and usage at [HPC Documentation](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/) and [FAQs](https://hpc.fau.de/faqs/#ID-230).

### Account Management
- **Account Validity**: The HPC portal will be the sole source for account validity. Ignore expiration messages from the IdM portal.
- **Role Assignment**: Manager roles and account validity updates are handled by HPC Admins. Users should contact their PI or project manager for changes.
- **Usage Statistics**: Visible to users, PIs, and project managers in the HPC portal.

### Tools and Services
- **ClusterCockpit**: Access via Single Sign-On link within the HPC portal.
- **Jupyterhub**: Access via Single Sign-On link within the HPC portal for an updated instance.

## Root Cause of the Problem
- **Manager Role Assignment**: The user's PI was unable to assign the manager role due to unfamiliarity with the new HPC portal.

## Solution
- **HPC Admin Intervention**: HPC Admins will handle the role assignment within the day.

## Additional Notes
- **Windows Users**: Recommended to use OpenSSH built into Windows (Power)Shell or MobaXterm instead of Putty.
- **Account Expiration**: The HPC portal will not automatically update account validity based on contract extensions or departures. Users must contact their PI or project manager for updates.

This documentation aims to assist HPC support employees in resolving similar issues related to the migration process and role assignments in the new HPC portal.
---

### 2024053142001844_keine%20verbindung.md
# Ticket 2024053142001844

 # HPC Support Ticket: Connection Issue

## Subject: keine verbindung

## Keywords:
- SSH connection
- Public key authentication
- Key mismatch
- HPC cluster access

## Problem Description:
The user is unable to connect to the HPC cluster via SSH. The user has followed the instructions multiple times without success.

## Root Cause:
- The public key offered for authentication does not match the key uploaded to the HPC portal.
- The fingerprint of the key used for authentication (`SHA256:83I/48mDjnMtAhZJuVicIpN0TPcXRzvXNuykFC/zXx0`) does not match the fingerprint of the key uploaded to the HPC portal (`SHA256:J386DxIr6mYt1I7YNdjS4S6WAELuETDAZ3M9pklHnYs`).

## Solution:
1. Ensure the correct public key is uploaded to the HPC portal.
2. Verify that the public key in `C:\\Users\\mkitz/.ssh/id_ed25519_nhr_fau.pub` matches the key uploaded to the HPC portal.
3. Wait for 2 hours after any changes to the keys.
4. If the issue persists, schedule a Zoom meeting with the HPC support team for further assistance.

## Additional Notes:
- The user's SSH configuration file (`C:\\Users\\mkitz/.ssh/config`) is correctly set up and found.
- The correct username is used for login.
- The private key file is read and authentication is attempted with it.

## Conclusion:
The issue was resolved by ensuring the correct public key was uploaded to the HPC portal and verifying the key match. The user was able to connect to the HPC cluster after following the provided solution.

---

This documentation can be used to troubleshoot similar SSH connection issues in the future.
---

### 2024030142001047_Migration%20of%20mpet%20HPC%20accounts%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20mandato.md
# Ticket 2024030142001047

 # HPC Support Ticket Summary

## Subject
Migration of mpet HPC accounts to new HPC portal / SSH keys become mandatory

## Keywords
- HPC account migration
- SSH keys
- HPC portal
- Single Sign-On (SSO)
- IdM portal
- Passphrase
- RSA, ECDSA, ED25519
- OpenSSH
- MobaXterm
- ClusterCockpit
- Jupyterhub

## Key Points
- **Migration to New HPC Portal**: Existing HPC accounts are being migrated to a new online HPC portal.
- **SSH Keys Mandatory**: From March 11th, access to HPC systems will require SSH keys.
- **SSH Key Types**: Accepted types are RSA (4096 bits), ECDSA (512 bits), and ED25519.
- **SSH Key Generation**: Users need to generate SSH key pairs with passphrases and upload the public key to the HPC portal.
- **Documentation**: Users unfamiliar with SSH keys should refer to the provided documentation and FAQs.
- **Windows Users**: Recommended to use OpenSSH built into Windows (Power)Shell or MobaXterm instead of Putty.
- **Account Validity**: The HPC portal will be the sole source for account validity, decoupled from the IdM portal.
- **Usage Statistics**: Users and their PIs/project managers can view usage statistics in the HPC portal.
- **Single Sign-On**: For ClusterCockpit and Jupyterhub, users should use the SSO link from within the HPC portal.

## Root Cause of the Problem
- Users need to migrate their accounts and set up SSH keys for continued access to HPC systems.

## Solution
- Users should log in to the new HPC portal using SSO with their IdM credentials.
- Generate and upload SSH keys as per the specified requirements.
- Use the SSO links for ClusterCockpit and Jupyterhub.
- Contact PIs or project managers for account validity updates.

## Additional Notes
- The IdM portal will send an automatic message about the HPC service expiring, which can be ignored.
- The HPC portal will not automatically update account validity based on contract extensions or departures from the university.
---

### 2024112042003164_Issue%20with%20remote%20access%20to%20cluster%20with%20ssh.md
# Ticket 2024112042003164

 ```markdown
# Issue with Remote Access to Cluster with SSH

## Keywords
- SSH
- Config file
- Remote access
- HPC cluster
- SSH keys

## Problem Description
- User unable to access HPC cluster from new laptop despite following the same procedure used on old laptop.
- User has two public SSH keys: one for old laptop (access works) and one for new laptop (access fails).
- User uploaded new SSH key but still unable to access the cluster.

## Root Cause
- The SSH config file was named `config.txt` instead of `config`.

## Solution
- Rename the config file from `config.txt` to `config`.

## Lessons Learned
- Ensure the SSH config file is named correctly (`config` without any extension).
- Verify the presence and correct naming of necessary files in the `.ssh` directory.
- Use the `-v` option with SSH for troubleshooting connection issues.

## Steps Taken
1. User reported issue with SSH access to the cluster.
2. HPC Admin identified the incorrect naming of the config file.
3. User renamed the config file and successfully accessed the cluster.

## Conclusion
- Proper naming of the SSH config file is crucial for successful remote access to the HPC cluster.
```
---

### 2024013042003048_Regarding%20the%20ssh%20setup%20-%20Roobesh%20Balaji.md
# Ticket 2024013042003048

 # HPC Support Ticket: SSH Setup Issues on Windows 11

## Keywords
- SSH setup
- Windows 11
- Public key authentication
- ssh-copy-id
- authorized_keys
- Connection timeout
- Debug output

## Problem Description
- User unable to set up SSH-based login for HPC account on Windows 11.
- `ssh-copy-id` command not recognized.
- Manual upload of public key to `authorized_keys` file did not resolve the issue.
- Connection attempts to HPC clusters result in "no such host is known" or "Connection timed out" errors.

## Root Cause
- Incorrect method used for uploading public key.
- Incorrect cluster names used for SSH login attempts.

## Solution
1. **Generate Key-Pair**: Ensure a valid SSH key-pair is generated.
2. **Upload Public Key**: Use the HPC portal (`https://portal.hpc.fau.de/`) to upload the public key. The commands quoted are for the IDM version and may not work on Windows 11.
3. **Wait for Key Distribution**: Allow up to 2 hours for the key to be distributed across the HPC systems.
4. **Login Attempt**: Try logging in to `cshpc.rrze.uni-erlangen.de`.
5. **Debug Output**: If login fails, use `ssh -vvv` for detailed debug output and provide this to the support team for further analysis.

## Additional Notes
- Ensure correct cluster names are used for SSH login attempts.
- Verify network connectivity and firewall settings if connection timeouts occur.

## References
- [SSH Secure Shell Access to HPC Systems](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/#publickey-legacy)
- HPC Portal: [https://portal.hpc.fau.de/](https://portal.hpc.fau.de/)
---

### 2024021942003997_Migration%20of%20iwep%20HPC%20accounts%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20mandato.md
# Ticket 2024021942003997

 # HPC Support Ticket Conversation Summary

## Subject
Migration of iwep HPC accounts to new HPC portal / SSH keys become mandatory

## Keywords
- HPC account migration
- SSH keys
- HPC portal
- Single Sign-On (SSO)
- IdM portal
- SSH key types (RSA, ECDSA, ED25519)
- Usage statistics
- ClusterCockpit
- Jupyterhub

## General Learnings
- **Migration Process**: The migration of HPC accounts from the IdM portal to a new HPC portal is underway.
- **SSH Keys**: Access to HPC systems will be via SSH keys only. Users need to generate and upload SSH key pairs.
- **SSH Key Types**: Accepted types are RSA (4096 bits), ECDSA (512 bits), and ED25519.
- **Portal Access**: The new HPC portal can be accessed via SSO using IdM credentials.
- **Account Validity**: The HPC portal will be the sole source for account validity, decoupled from the IdM portal.
- **Usage Statistics**: Users and their PIs/project managers can view usage statistics in the HPC portal.
- **ClusterCockpit & Jupyterhub**: Access these services via SSO links within the HPC portal.

## Root Cause of the Problem
- Users need to transition to the new HPC portal and set up SSH keys for continued access.

## Solution
- **Generate SSH Keys**: Users should generate SSH key pairs with a passphrase.
- **Upload SSH Keys**: Upload the public key to the HPC portal.
- **Access Portal**: Login to the HPC portal using SSO with IdM credentials.
- **Ignore IdM Expiration**: Ignore automatic messages about HPC service expiration in the IdM portal.

## Additional Resources
- [SSH Documentation](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/)
- [FAQs](https://hpc.fau.de/faqs/#ID-230)

## Notes
- **Windows Users**: Recommended to use OpenSSH built into Windows (Power)Shell or MobaXterm instead of Putty.
- **Account Management**: Contact PI or project manager for account validity updates and new account requests.

This summary provides a quick reference for support employees to understand the migration process and assist users with the transition.
---

### 2024032142001385_HPC%20Access%20without%20VPN.md
# Ticket 2024032142001385

 # HPC Access without VPN

## Keywords
- HPC Access
- VPN
- SSH Configuration
- ProxyJump
- Frontend Nodes
- JupyterHub
- IPv6
- ISP Restrictions

## Problem
- User needs to access HPC for project work while traveling.
- VPN does not work for the user.
- User can access HPC without VPN from their home in Erlangen.
- Concern about accessing HPC from outside Germany.

## Root Cause
- VPN not functioning for the user.
- Potential ISP or router restrictions in the new location.

## Solution
- **SSH Configuration**: Ensure the SSH config file is correctly set up with ProxyJump.
  ```plaintext
  Host tinyx.nhr.fau.de
    HostName tinyx.nhr.fau.de
    ProxyJump user@cshpc.rrze.fau.de
    User user
    IdentityFile ~/.ssh/HPC_SSH

  Host cshpc.rrze.fau.de
    User user
    IdentityFile ~/.ssh/HPC_SSH
  ```
- **Accessing Frontend Nodes**: Confirm that the frontend node (tinyx) is accessible via the configured ProxyJump.
- **JupyterHub**: Note that JupyterHub will not be accessible without VPN. Interactive Jupyter notebooks on a node should still work.
- **IPv6**: Ensure the internet connection supports IPv6 if accessing frontend nodes directly.
- **ISP Restrictions**: Check for any restrictions from the local ISP or router that might block SSH connections.

## General Learnings
- **ProxyJump Configuration**: Proper SSH configuration with ProxyJump allows access to HPC resources from anywhere.
- **VPN Dependency**: Some services like JupyterHub require VPN access.
- **IPv6 Requirement**: Direct access to frontend nodes may require IPv6 support.
- **ISP/Router Restrictions**: Local network settings can impact HPC access.

## References
- [SSH Command Line Instructions](https://doc.nhr.fau.de/access/ssh-command-line/)
- [JupyterHub Access](https://doc.nhr.fau.de/access/jupyterhub/)
---

### 2022091942003541_Woody%20login.md
# Ticket 2022091942003541

 # HPC Support Ticket: Woody Login Issue

## Keywords
- SSH Login Issue
- DNS Spoofing Warning
- Host Key Change
- ssh_known_hosts
- Woody Cluster

## Problem Description
User unable to login to Woody cluster via SSH due to a host key change warning. The error message indicates a possible DNS spoofing or a change in the host key for the Woody cluster.

## Error Message
```
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@       WARNING: POSSIBLE DNS SPOOFING DETECTED!          @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
The ECDSA host key for woody has changed,
and the key for the corresponding IP address 2001:638:a000:4801::15
is unchanged. This could either mean that
DNS SPOOFING is happening or the IP address for the host
and its host key have changed at the same time.
Offending key for IP in /etc/ssh/ssh_known_hosts:8512
remove with:
ssh-keygen -f "/etc/ssh/ssh_known_hosts" -R "2001:638:a000:4801::15"
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
Someone could be eavesdropping on you right now (man-in-the-middle attack)!
It is also possible that a host key has just been changed.
The fingerprint for the ECDSA key sent by the remote host is
SHA256:sf45uAzebm6at31zW3/e/T6nyd+sdCSBR9wgeu8ZOuc.
Please contact your system administrator.
Add correct host key in /home/hpc/iwal/iwal044h/.ssh/known_hosts to get rid of this message.
Offending RSA key in /etc/ssh/ssh_known_hosts:8520
remove with:
ssh-keygen -f "/etc/ssh/ssh_known_hosts" -R "woody"
ECDSA host key for woody has changed and you have requested strict checking.
Host key verification failed.
```

## Root Cause
The host key for the Woody cluster has changed, causing SSH to warn about a possible security issue.

## Solution
1. **Update `ssh_known_hosts`**: Remove the offending keys from the `ssh_known_hosts` file using the provided commands.
   ```sh
   ssh-keygen -f "/etc/ssh/ssh_known_hosts" -R "2001:638:a000:4801::15"
   ssh-keygen -f "/etc/ssh/ssh_known_hosts" -R "woody"
   ```
2. **Add Correct Host Key**: Add the correct host key to the user's `known_hosts` file.

## Additional Notes
- Ensure that the `ssh_known_hosts` file on the cshpc cluster is up to date.
- Contact HPC Admins if the issue persists after updating the `ssh_known_hosts` file.

## Relevant Roles
- **HPC Admins**: Thomas, Michael Meier, Anna Kahler, Katrin Nusser, Johannes Veh
- **2nd Level Support Team**: Lacey, Dane (fo36fizy), Kuckuk, Sebastian (sisekuck), Lange, Florian (ow86apyf), Ernst, Dominik (te42kyfo), Mayr, Martin
- **Head of the Datacenter**: Gerhard Wellein
- **Training and Support Group Leader**: Georg Hager
- **NHR Rechenzeit Support and Applications for Grants**: Harald Lanig
- **Software and Tools Developer**: Jan Eitzinger, Gruber
---

### 2022120742002807_Fwd%3A%20Testaccount%20auf%20Fritz%20-%20k105be%20-%20PharmacoMech-FSI%20-%20Klawonn%20_%20Uni-K%C3%.md
# Ticket 2022120742002807

 ```markdown
# HPC Support Ticket Conversation Analysis

## Keywords
- Testaccount
- Rechenzeit
- DFG Projekt
- Hackangriff
- SSO-Attribute
- HPC-Portal
- SSH-Keys
- Jobmonitoring
- ClusterCockpit
- Normalprojekt
- Freischaltungsprozess
- Rechenzeitantrag
- Projektverlängerung

## General Learnings
- **Test Account Approval**: Test projects exceeding the standard limit can be approved if a normal project is expected to follow.
- **SSO Attribute Issues**: Users may encounter issues with SSO attributes, which need to be resolved by their local IT department.
- **Project Reactivation**: Expired test accounts can be reactivated upon request.
- **Communication**: Clear communication between users and HPC support is crucial for resolving issues efficiently.

## Root Cause of Problems
- **Exceeding Test Limit**: The user requested more compute time than the standard test limit.
- **SSO Attribute Error**: The user encountered an error due to missing SSO attributes during the initial login.
- **Expired Test Account**: The test account expired, requiring reactivation for continued use.

## Solutions
- **Test Account Approval**: Approve the test project with a reminder to submit a normal project as the limit is approached.
- **SSO Attribute Error**: Direct the user to contact their local IT department to resolve the SSO attribute issue.
- **Project Reactivation**: Reactivate the expired test account to allow continued use while the normal project application is in progress.

## Documentation for Support Employees
- **Test Account Approval Process**:
  - Review the compute time request.
  - Approve if within reasonable limits and a normal project is expected to follow.
  - Send a reminder to submit a normal project as the test limit is approached.

- **SSO Attribute Error Resolution**:
  - Inform the user to contact their local IT department to resolve missing SSO attributes.
  - Provide guidance on the HPC portal and SSH key usage.

- **Project Reactivation**:
  - Reactivate expired test accounts upon user request.
  - Ensure the user is aware of the need to submit a normal project application.
```
---

### 2023031042000649_Can%27t%20connec%27t%20to%20HPC.md
# Ticket 2023031042000649

 # HPC Support Ticket: Can't Connect to HPC via VS Code

## Keywords
- VS Code
- SSH
- Connection Issue
- Lock File
- Remote I/O Error
- VPN

## Problem Description
- User unable to connect to HPC account via VS Code.
- Connection via terminal (SSH) works.
- Error message indicates permission denied and remote I/O error related to lock files.

## Root Cause
- VS Code's SSH remote extension having issues with lock files.
- Possible expired certificate.

## Troubleshooting Steps
1. **Check SSH Connection**: Verify that the user can connect via SSH terminal.
2. **Identify Error Messages**: Look for error messages related to lock files and remote I/O errors.

## Solution
1. **Disable `remote.SSH.useFlock`**:
   - Set `"remote.SSH.useFlock": false` in VS Code settings.
2. **Kill Running Code Servers**:
   - Terminate any running VS Code servers on the HPC cluster.
3. **Delete Lock File**:
   - Remove the lock file located at `/home/hpc/iwi5/iwi5118h/.vscode-server/bin/441438abd1ac652551dbe4d408dfcec8a499b8bf/vscode-remote-lock.iwi5118h.441438abd1ac652551dbe4d408dfcec8a499b8bf`.
4. **Retry Connection**:
   - Attempt to connect through VS Code again.

## Additional Resources
- [StackOverflow Solution](https://stackoverflow.com/a/67083117)
- [GitHub Issue](https://github.com/microsoft/vscode-remote-release/issues/2518)

## Notes
- The user is connected via VPN.
- The issue persists only when trying to connect via IDE (VS Code).

## Conclusion
The issue is related to VS Code's SSH remote extension and lock files. Following the steps above should resolve the connection problem. If the issue persists, further investigation into the expired certificate may be necessary.
---

### 2023030142003511_Umstellung%20der%20HPC-Accounts%20der%20HS-Coburg%20am%20RRZE%20_%20NHR%40FAU%20-%20corz043h.md
# Ticket 2023030142003511

 # HPC Support Ticket Conversation Summary

## Keywords
- HPC Accounts
- HS-Coburg
- RRZE / NHR@FAU
- HPC-Portal
- DFN-AAI/eduGAIN
- SSH-PublicKeys
- SSH-Key
- Password
- Windows PowerShell
- Windows Subsystem for Linux
- mobaXtern
- OpenSSH
- Putty
- JumpHost-Feature
- Deactivation
- Data Deletion

## General Learnings
- The HPC account management system for HS-Coburg at RRZE / NHR@FAU is transitioning from a paper-based system to an electronic HPC-Portal.
- Users need to log in to the HPC-Portal using DFN-AAI/eduGAIN to continue using their HPC accounts.
- After logging in, existing HPC accounts will be linked to the user's identity in the portal.
- Users can upload SSH-PublicKeys in the "User / Benutzer" tab, which will be synchronized to the HPC systems within two hours.
- Starting at the end of March, access to HPC systems will only be possible via SSH-Key, not password.
- Windows users are advised to use Windows PowerShell, Windows Subsystem for Linux, or mobaXtern, which contain OpenSSH as an SSH-Client.
- HPC accounts not linked to a person by the end of March will be deactivated, and associated data will be deleted after three months.
- For questions about the transition, users should contact the specified support personnel at HS-Coburg.

## Root Cause of the Problem
- The user's HPC account needed to be migrated to the new electronic HPC-Portal system.

## Solution
- The user logged into the HPC-Portal using DFN-AAI/eduGAIN.
- The HPC Admin verified the user's account and linked it to their identity in the portal.

## Follow-up Actions
- Users should upload their SSH-PublicKeys in the "User / Benutzer" tab.
- Users should transition to using SSH-Key for HPC system access by the end of March.

## References
- [HPC-Portal Usage](https://hpc.fau.de/systems-services/documentation-instructions/getting-started/nhrfau-hpc-portal-usage/)
- [SSH and SSH-Keys](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/)
- [FAQ on SSH Access](https://hpc.fau.de/faqs/#innerID-13183)
- [mobaXtern](https://mobaxterm.mobatek.net/)
---

### 2024080242002204_Cannot%20connect%20to%20HPC%20systems.md
# Ticket 2024080242002204

 # HPC Support Ticket: Cannot Connect to HPC Systems

## Keywords
- SSH connection issue
- SSH key pairs
- Config file
- ProxyJump configuration
- Debugging SSH connection

## Problem Description
The user recently gained permission to access HPC cluster nodes but encountered issues when attempting to connect via SSH. The user followed instructions to create and upload SSH key pairs and created the necessary config file. However, running the SSH command resulted in no response.

## Root Cause
The root cause of the problem was a configuration error in the SSH config file. Specifically, the `ProxyJump` line was incorrectly set for the `csnhr` entry.

## Diagnostic Steps
1. The user provided the output of `ssh -vv csnhr.nhr.fau.de` to the HPC Admin for analysis.
2. The HPC Admin reviewed the output and identified the configuration error.

## Solution
The HPC Admin advised the user to correct the SSH config file by removing the `ProxyJump` line for the `csnhr` entry. The corrected config file should look like this:

```plaintext
Host csnhr.nhr.fau.de csnhr
HostName csnhr.nhr.fau.de
User iwso150h
IdentityFile ~/.ssh/id_HPCfau_rhinoForce
IdentitiesOnly yes
PasswordAuthentication no
PreferredAuthentications publickey
ForwardX11 no
ForwardX11Trusted no
```

## General Learnings
- Always check the SSH config file for correctness when encountering connection issues.
- Use `ssh -vv` to gather detailed debugging information.
- Ensure that the `ProxyJump` configuration is correctly set up, if required.
- Use the official FAU email for support communications to avoid delays and ensure proper tracking.

## Additional Notes
- The user was reminded to use their FAU email for future support communications.
- The HPC Admin provided detailed instructions on how to correct the config file.

This documentation can be used to troubleshoot similar SSH connection issues in the future.
---

### 2023112842000725_Re%3A%20New%20invitation%20for%20%22Tier3%20Grundversorgung%20Uni-Bayreuth%20%28via%20IT-Servicezent.md
# Ticket 2023112842000725

 # HPC Support Ticket Analysis

## Keywords
- HPC-Support
- Invitation
- SSO
- IdM credentials
- ssh public key
- Tier3 Grundversorgung
- University of Bayreuth
- IT-Servicezentrum
- FAU

## Problem
- User unable to find invitation under 'User' -> 'Your Invitations'.

## Root Cause
- Mismatch between the email address used by the IdP (Identity Provider) for SSO and the email address to which the invitation was sent.

## Solution
- HPC Admin adjusted the invitation to match the email address provided by the IdP (bt308691@uni-bayreuth.de).

## General Learnings
- Ensure that the email address used for SSO matches the email address to which the invitation is sent.
- Users should check their SSO email address if they encounter issues with invitations.
- HPC Admins can resolve such issues by adjusting the invitation email address.

## Next Steps for Similar Issues
1. Verify the email address used for SSO.
2. Check if the invitation was sent to the correct email address.
3. Adjust the invitation email address if necessary.
4. Inform the user to check their invitations again.

## Roles Involved
- HPC Admins
- 2nd Level Support Team
- Head of the Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support
- Software and Tools Developer
---

### 2024021542001666_unable%20to%20access%20the%20servers.md
# Ticket 2024021542001666

 # HPC Support Ticket: Unable to Access the Servers

## Keywords
- SSH keys
- ProxyJump
- HPC clusters
- Gromacs
- GPU vs CPU benchmarks

## Problem
- User unable to connect to HPC clusters (Fritz and Alex) from the dialog server.
- Permission denied error when attempting to SSH into the clusters.

## Root Cause
- SSH keys were not properly configured for ProxyJump.
- User was unaware of the need to set up ProxyJump for accessing the clusters.

## Solution
- HPC Admins suggested setting up ProxyJump.
- Provided links to FAQs and templates for configuring ProxyJump:
  - [FAQ on ProxyJump](https://hpc.fau.de/faqs/#i-managed-to-log-in-to-cshpc-with-an-ssh-key-but-get-asked-for-a-password-when-continuing-to-a-cluster-frontend)
  - [SSH Config Templates](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/#ssh_config_hpc_portal)

## Outcome
- User successfully configured ProxyJump and gained access to Fritz and Alex clusters.
- User was advised to run benchmarks on both GPU (Alex) and CPU (Fritz) systems using Gromacs.

## General Learnings
- Ensure SSH keys are properly distributed and configured for ProxyJump when accessing HPC clusters.
- Provide clear instructions and templates for setting up ProxyJump to users.
- Advise users on running benchmarks on both GPU and CPU systems for performance comparison.
---

### 2024030642001752_Fehlkonfiguration%20Ihrer%20Website%20-%20SSHFP%20_%20DNSSEC%20nicht%20korrekt%20konfiguriert.md
# Ticket 2024030642001752

 # HPC-Support Ticket: Fehlkonfiguration Ihrer Website - SSHFP / DNSSEC nicht korrekt konfiguriert

## Problem
- **Fehlkonfiguration von SSHFP DNS-Einträgen** für die Domain `grid.rrze.uni-erlangen.de` und `grid.rrze.fau.de`.
- **Mögliche Szenarien**:
  1. HostKey-Fingerabdrücke in den SSHFP DNS-Einträgen stimmen nicht mit den tatsächlichen HostKeys des SSH-Servers überein.
  2. SSHFP DNS-Einträge werden nicht ausreichend gesichert übertragen, weil DNSSEC nicht konfiguriert ist.

## Auswirkungen
- **Szenario 1**: Manuelle Verifizierung der HostKeys durch den Nutzer erforderlich, was zu Fehlern führen kann.
- **Szenario 2**: Mögliche Manipulation der SSHFP-Einträge durch Angreifer, was die Sicherheit der SSH-Verbindung gefährdet.

## Lösung
- **Korrektur der SSHFP DNS-Einträge**: Die fehlerhaften Einträge wurden korrigiert.
- **Ursache**: Ein kaputter Automatismus erzeugte die Einträge, aktualisierte sie jedoch nie.

## Weitere Schritte
- **Überprüfung und Aktualisierung**: Andere DNS-Einträge sollten ebenfalls überprüft und aktualisiert werden.
- **Live-Check-Tool**: Verwendung des Tools zur Überprüfung der Konfiguration und weiteren Informationen.

## Schlüsselwörter
- SSHFP
- DNSSEC
- HostKey-Verifizierung
- SSH-Sicherheit
- DNS-Infrastruktur
- Automatisierung

## Allgemeines
- **Kommunikation**: Effektive Kommunikation zwischen Forschungsgruppe und HPC-Admins zur Identifikation und Behebung von Sicherheitsproblemen.
- **Automatisierung**: Überprüfung und Wartung von Automatisierungsprozessen zur Vermeidung von Fehlkonfigurationen.

## Dokumentation
- **DNSSEC-Konfiguration**: Sicherstellung, dass DNSSEC korrekt konfiguriert ist, um die Authentizität der übertragenen Daten zu gewährleisten.
- **SSHFP-Einträge**: Regelmäßige Überprüfung und Aktualisierung der SSHFP-Einträge, um sicherzustellen, dass sie mit den tatsächlichen HostKeys übereinstimmen.
---

### 2024101642003781_Cannot%20ssh%20auth%20to%20gate_fritz%20after%20account%20had%20temporarily%20been%20deactivated.md
# Ticket 2024101642003781

 ```markdown
# HPC-Support Ticket: Cannot SSH Auth to Gate/Fritz After Account Reactivation

## Summary
User unable to authenticate via SSH to the gate server after account reactivation.

## Keywords
- SSH Authentication
- Account Reactivation
- SSH Key
- Gate Server
- Login Node

## Problem
- User reactivated their account after it had been temporarily deactivated.
- Despite waiting more than 2 hours, the user could not authenticate to the gate server using their existing SSH key.
- The SSH key was rejected by the gate server.

## Root Cause
- The account reactivation process had not fully propagated.
- Misunderstanding of the 2-hour wait time for account reactivation vs. SSH key update.

## Troubleshooting Steps
1. User provided SSH config and verbose SSH connection log.
2. HPC Admin confirmed the need for both `csnhr` and `fritz` sections in the SSH config.
3. User clarified that the proxy jump configuration was in place but the initial connection to the gate server was failing.
4. HPC Admin noted that the account was reactivated less than 2 hours before the attempted login.

## Solution
- Wait for the full 2-hour period after account reactivation for changes to propagate.
- Clarify in the portal that the 2-hour wait time applies to account reactivation as well as SSH key updates.

## Additional Notes
- If the account has been inactive for a longer period, it may take until the next morning for the account to be fully reactivated.
- Consider adding a message in the portal to indicate the expected wait time for account reactivation.

## Follow-up
- Issue #111 created to address the need for a reactivation message in the portal.
```
---

### 2022081842000421_Fragen%20%C3%83%C2%BCber%20Einloggen.md
# Ticket 2022081842000421

 ```markdown
# HPC-Support Ticket Conversation: Fragen über Einloggen

## Keywords
- SSH login
- Public key authentication
- Permission denied
- Password prompt
- Windows vs. Linux SSH behavior

## Summary
A user with an account for a specific project encounters issues with SSH login on both Windows and Linux systems. The user has uploaded public keys for both systems but faces different issues on each platform.

## Root Cause of the Problem
1. **Windows Laptop Issue**: The user can access the portal server without a password but is denied permission when attempting to log in to `alex.nhr.fau.de` with the message 'Permission denied (publickey, password)'.
2. **Linux Workstation Issue**: The user is prompted for a password immediately when attempting to SSH into `cshpc.rrze.fau.de`, despite having uploaded a public key.

## Solution
1. **Windows Laptop**:
   - Ensure the correct public key is being used for `alex.nhr.fau.de`.
   - Verify the public key is correctly configured in the SSH agent and the server's authorized_keys file.

2. **Linux Workstation**:
   - Check the SSH configuration to ensure the correct key is being used.
   - Verify the public key is correctly added to the SSH agent and the server's authorized_keys file.

## General Learnings
- **Public Key Authentication**: Ensure that the correct public key is used and properly configured for each system.
- **SSH Configuration**: Differences in SSH behavior between Windows and Linux can be due to configuration settings or how keys are managed.
- **Password Prompt**: If a password is prompted, it may indicate that the public key is not being used correctly.

## Next Steps
- **HPC Admins**: Assist the user in verifying the public key configuration on both systems.
- **2nd Level Support Team**: Provide guidance on configuring SSH keys and troubleshooting common issues.
```
---

### 2024050342002815_Unable%20to%20connect%20to%20the%20servers.md
# Ticket 2024050342002815

 ```markdown
# HPC Support Ticket: Unable to Connect to Servers

## Summary
User unable to connect to HPC servers "Alex" and "Fritz" due to SSH key issues.

## Keywords
- SSH key
- Permission denied (publickey)
- sign_and_send_pubkey: signing failed
- agent refused operation
- ssh-config
- debug output

## Problem
- User submitted the wrong SSH key passphrase.
- Error message: `sign_and_send_pubkey: signing failed for RSA ... from agent: agent refused operation`.
- Permission denied (publickey).

## Steps Taken
1. User set up `ssh-config` as described in the documentation.
2. User provided debug output and commands used.
3. HPC Admin suggested generating a new key pair and uploading it to the portal.
4. User uploaded a new key pair but faced the same issue.
5. User generated a new key pair using ED25519 and successfully accessed the cluster.

## Solution
- Generate a new SSH key pair using ED25519.
- Upload the new key to the HPC portal.
- Ensure the new key is used for authentication.

## Additional Notes
- User data remains unaffected during key distribution.
- HPC Admin offered a Zoom call for further assistance.

## Conclusion
The issue was resolved by generating a new SSH key pair using ED25519 and uploading it to the portal.
```
---

### 2024110542004236_Verbindung%20Cluster%20Fritz.md
# Ticket 2024110542004236

 # HPC Support Ticket: Verbindung Cluster Fritz

## Keywords
- SSH
- Permissions
- Private Key
- .ssh Directory
- Configuration File

## Problem Description
The user encountered an error while attempting to connect to the HPC cluster using SSH. The error message indicated that the private key file permissions were too open, making the key insecure.

## Root Cause
The user manually created the `.ssh` directory and copied the private key files with incorrect permissions (0644), which allowed other users to read the private key.

## Solution
1. **Correct Permissions**:
   - Set the correct permissions for the `.ssh` directory and the private key file.
     ```bash
     chmod 700 /home/hpc/b246dc/b246dc12/.ssh
     chmod 600 /home/hpc/b246dc/b246dc12/.ssh/id_ed25519
     ```

2. **Configuration File**:
   - Ensure that the configuration file (`.config`) is correctly set up on the local machine, not on the HPC system.

3. **SSH Command**:
   - Run the SSH command from the local machine, not from the HPC system.
     ```bash
     ssh -X fritz.nhr.fau.de
     ```

## General Learnings
- Private keys should be kept secure and only accessible by the owner.
- The `.ssh` directory and private key files should have restricted permissions (700 for the directory and 600 for the key file).
- Configuration files and private keys should be stored on the local machine, not on the HPC system.
- Follow the official HPC documentation for setting up SSH connections to avoid common pitfalls.

## Additional Notes
- The user was following an outdated or incorrect guide provided by their department.
- The HPC Admin emphasized the importance of keeping private keys secure and not storing them on shared systems.
- The ticket was escalated internally for further assistance.
---

### 2024073042001575_Fwd%3A%20New%20invitation%20for%20%22Tier3%20Grundversorgung%20LS%20Analytics%20%26%20Mixed-Integer%.md
# Ticket 2024073042001575

 # HPC Support Ticket Conversation Summary

## Keywords
- SSH Key
- Permission Denied
- HPC Portal
- SSH Command Line
- Proxy Jump
- Debug Output
- Security
- SSH Key Pair

## General Learnings
- Ensure correct server addresses and domain names.
- Use proxy jump for direct login to cluster frontends.
- Separate SSH key pairs for internal logins for security reasons.
- Follow FAQ and documentation for troubleshooting common issues.

## Problem
- User could log in to `cshpc.rrze.fau.de` but received "Permission denied" when attempting to log in to `woody.rrze.fau.de`.

## Root Cause
- Incorrect server address and missing SSH key on the target server.

## Solution
- Correct the server address to `woody.nhr.fau.de`.
- Manually copy the private SSH key to the target server's `.ssh` directory.
- Use proxy jump for direct login to the cluster frontend.
- Ensure separate SSH key pairs for internal logins for security reasons.

## References
- [HPC Portal Documentation](https://doc.nhr.fau.de/hpc-portal/)
- [SSH Command Line Documentation](https://doc.nhr.fau.de/access/ssh-command-line/)
- [HPC Cafe 2024](https://hpc.fau.de/teaching/hpc-cafe/#HPC-Caf%C3%A9-2024)
- [Dialog Server Decommissioning](https://hpc.fau.de/2024/06/06/dialog-server-cshpc-to-be-decommissioned-nomachine-nx-to-be-replaced-by-xrdp/)

## Notes
- Always refer to the latest documentation and FAQ for troubleshooting common issues.
- Ensure compliance with security best practices when handling SSH keys.
---

### 2024110542000892_SSH-Key%20und%20Zugriff%20auf%20Meggie.md
# Ticket 2024110542000892

 # HPC Support Ticket: SSH-Key and Access to Meggie

## Keywords
- SSH Key
- Meggie Access
- Fingerprint
- Password Prompt
- HPC Portal

## Summary
A user encountered issues accessing the Meggie cluster despite setting up an SSH key. The user uploaded the SSH key to the HPC portal but was still prompted for a password.

## Root Cause
- The SSH key was correctly uploaded to the HPC portal.
- The user was still prompted for a password, indicating a potential issue with the SSH key configuration or propagation delay.

## Solution
- Verify the SSH key configuration on both the user's machine and the HPC portal.
- Ensure that the SSH key has been properly propagated to the Meggie cluster.
- Check for any additional configuration steps required by the HPC portal for SSH key usage.

## Lessons Learned
- SSH key propagation may take time, and users should be informed about potential delays.
- Double-checking SSH key configurations and ensuring proper propagation can resolve access issues.
- Provide clear instructions on the HPC portal for setting up and using SSH keys to minimize user confusion.

## Next Steps
- HPC Admins should review the SSH key propagation process to ensure timely updates.
- The 2nd Level Support team should assist the user in verifying the SSH key configuration and troubleshooting any remaining issues.
- Update the HPC portal documentation to include detailed steps for setting up and using SSH keys.
---

### 2024090942002968_SSH-key%20undefined%20nach%20Account-Verl%C3%83%C2%A4ngerung.md
# Ticket 2024090942002968

 # SSH-Key Issue After Account Extension

## Keywords
- SSH-Key
- Account Extension
- Lokalisierungsproblem
- Boolean
- Account Update
- Datenbank-Eintrag
- HPC-Portal
- Bug-Report

## Problem Description
After extending the account duration, an SSH-key issue was displayed for the user accounts. The SSH-key status showed as "undefined" after the extension.

## Root Cause
The issue was not solely a localization error but rather a problem with the account update process. When an account is updated with new information, the corresponding Boolean value that should fill the SSH-key field is not provided, resulting in the "undefined" status.

## Solution
The SSH-key itself remains unchanged in the database. To resolve the display issue, the account list of the project needs to be reloaded (by pressing F5 or using the "Accounts neu laden" button). This action correctly fills the SSH-key field.

## Lessons Learned
- SSH-keys do not have an expiration date in the current system.
- The issue is related to how the account update process handles Boolean values.
- Reloading the account list resolves the display issue without requiring users to re-enter their SSH-keys.

## Actions Taken
- The issue was identified and documented.
- The HPC Admin team confirmed that the SSH-keys were still present in the database.
- The 2nd Level Support team provided a solution to reload the account list.

## Future Considerations
- Ensure that the account update process correctly handles Boolean values to avoid similar issues in the future.
- Continue monitoring for localization errors in the HPC-Portal.

## Conclusion
The SSH-key issue after account extension was a display problem caused by the account update process not providing the necessary Boolean value. Reloading the account list resolved the issue without affecting the actual SSH-keys.
---

### 2023071042003237_Login%20to%20specific%20Fritz_Alex%20nodes.md
# Ticket 2023071042003237

 # HPC Support Ticket: Login to Specific Fritz/Alex Nodes

## Keywords
- SSH key authentication
- Login to compute nodes
- srun command
- ssh config
- Password authentication

## Problem Description
The user was unable to log in to specific compute nodes (Fritz/Alex) after switching to SSH key authentication. The user was prompted for a password, and the old password did not work.

## Root Cause
- The user did not have an SSH key configured on the frontend nodes.
- The user was attempting to log in to the compute nodes without using an SSH key, causing the system to fall back to password authentication.

## Solution
1. **Use the Same SSH Key**: The user can use the same SSH key for logging into the compute nodes as they do for the frontend nodes. The login must be initiated from a device that has the private key.
2. **Interactive Login via `srun`**: The user can log in interactively to a node with a running job using the following command:
   ```sh
   srun --pty --overlap --jobid YOUR-JOBID /bin/bash -l
   ```
   For more details, refer to the [FAQ section](https://hpc.fau.de/faqs/#innerID-13272).

## General Learnings
- Ensure SSH keys are properly configured and used for logging into both frontend and compute nodes.
- Use the `srun` command for interactive login to nodes with running jobs.
- Verify the SSH configuration and login attempts using `ssh -vv` for detailed output.

## References
- [FAQ: Interactive Login to Nodes](https://hpc.fau.de/faqs/#innerID-13272)

## Roles Involved
- **HPC Admins**: Provided detailed instructions and solutions.
- **User**: Reported the issue and followed the instructions provided by the HPC Admins.
---

### 2022042942000355_IdP-Freischaltung%20f%C3%83%C2%BCr%20portal.hpc.fau.de%20von%20NHR%40FAU%20f%C3%83%C2%BCr%20den%20Zu.md
# Ticket 2022042942000355

 # HPC Support Ticket: IdP-Freischaltung für portal.hpc.fau.de

## Keywords
- SSO-Freischaltung
- DFN-AAI-Föderation
- NHR@FAU
- Hochleistungsrechner
- Shibboleth
- IdP
- SdP
- Attribute

## Problem
- **Root Cause**: The SSO attributes for the new HPC portal at NHR@FAU were not enabled, preventing users from accessing the high-performance computing resources.
- **Details**: The HPC Admin received a request to enable SSO attributes for the new HPC portal at NHR@FAU. The Admin was unsure who was responsible for this task at the user's institution.

## Solution
- **Steps Taken**:
  1. The HPC Admin forwarded the request to the appropriate contact at the user's institution.
  2. The user forwarded the request to their internal IT support team.
  3. The IT support team enabled the required SSO attributes in their Shibboleth IdP.
- **Attributes Enabled**:
  - `urn:oid:2.5.4.42` - `urn:mace:dir:attribute-def:givenName`: `givenName`
  - `urn:oid:2.5.4.4` - `urn:mace:dir:attribute-def:sn`: `sn`
  - `urn:oid:0.9.2342.19200300.100.1.3` - `urn:mace:dir:attribute-def:mail`: `mail`
  - `urn:oid:1.3.6.1.4.1.5923.1.1.1.6` - `urn:mace:dir:attribute-def:eduPersonPrincipalName`: `eduPersonPrincipalName`
  - `urn:oid:1.3.6.1.4.1.5923.1.1.1.9` - `urn:mace:dir:attribute-def:eduPersonScopedAffiliation`: `eduPersonScopedAffiliation`

## General Learnings
- **SSO Configuration**: Enabling the correct SSO attributes is crucial for users to access HPC resources.
- **Communication**: Effective communication and forwarding requests to the appropriate contacts can resolve issues efficiently.
- **DFN-AAI-Föderation**: Understanding the roles and responsibilities within the DFN-AAI-Föderation is important for HPC support.

## References
- [NHR@FAU Portal](https://portal.hpc.fau.de/)
- [DFN-AAI-Föderation](https://www.aai.dfn.de/)
- [NHR Application Rules](https://hpc.fau.de/systems-services/systems-documentation-instructions/nhr-application-rules/)
---

### 2016040342000147_kein%20Login%20mehr%20m%C3%83%C2%B6glich.md
# Ticket 2016040342000147

 ```markdown
# HPC-Support Ticket: Login Issue

## Subject: kein Login mehr möglich

### Keywords:
- Login issue
- Permission denied
- HPC/IDM-Migration
- Mitarbeiterstatus
- Ablaufdatum

### Problem Description:
- User unable to log in to Emmy / Lima.
- Error message: "Permission denied, please try again."
- User's credentials were active according to IDM.
- User speculated that the issue might be related to a change in their employment status.

### Root Cause:
- Incorrect date was transferred during the HPC/IDM-Migration in January.
- Automatic adjustment of the expiration date by IDM/FM (linked to affiliation).

### Solution:
- HPC Admin identified the issue and corrected the expiration date.
- Access should be restored within a few hours.

### General Learnings:
- Migration processes can lead to incorrect data transfer.
- Automatic adjustments by IDM/FM can cause unexpected issues.
- Regularly check and update user affiliations and expiration dates to prevent access issues.
```
---

### 2024021342003015_Alex%20GPU%20Cluster%3A%20Einloggen%20auf%20Node%20via%20ssh.md
# Ticket 2024021342003015

 # HPC Support Ticket: SSH Login to GPU Node

## Keywords
- SSH login
- GPU node
- Resource monitoring
- Permission denied
- Password prompt

## Problem Description
The user is attempting to SSH into a GPU node on the Alex Cluster to monitor resource usage of a running job. The user receives a password prompt followed by a "Permission denied, please try again" message.

## Root Cause
The user is not able to SSH into the node due to incorrect authentication or lack of necessary permissions.

## Solution
- **Authentication Method**: Ensure the user is using the correct authentication method (e.g., SSH keys instead of password).
- **Permissions**: Verify that the user has the necessary permissions to access the node.
- **Alternative Monitoring**: Suggest alternative methods for monitoring resource usage, such as using job monitoring tools provided by the cluster's job scheduler.

## General Learnings
- **SSH Authentication**: Understand the importance of proper SSH key setup for passwordless login.
- **Permissions**: Ensure users have the correct permissions for accessing compute nodes.
- **Resource Monitoring**: Familiarize users with available tools for monitoring job resource usage without direct node access.

## Next Steps
- **HPC Admins**: Review user permissions and SSH key setup.
- **2nd Level Support**: Provide guidance on using job monitoring tools.
- **User**: Follow up with HPC Admins for further assistance if needed.

## Related Contacts
- **HPC Admins**: Thomas, Michael Meier, Anna Kahler, Katrin Nusser, Johannes Veh
- **2nd Level Support**: Lacey, Dane (fo36fizy), Kuckuk, Sebastian (sisekuck), Lange, Florian (ow86apyf), Ernst, Dominik (te42kyfo), Mayr, Martin
- **Head of Datacenter**: Gerhard Wellein
- **Training and Support Group Leader**: Georg Hager
- **NHR Rechenzeit Support**: Harald Lanig
- **Software and Tools Developer**: Jan Eitzinger, Gruber
---

### 2024072242001938_Re%3A%20Manager%20access%20granted%20for%20project%20%22SelBlockInv%20-%20Selected%20Block%20Inversi.md
# Ticket 2024072242001938

 # HPC Support Ticket Conversation Analysis

## Keywords
- Manager access
- Project management
- SSO login
- IdM credentials
- User invitation
- Account review
- HPC portal
- Documentation
- Support email
- Automatic email

## What Can Be Learned
- **Manager Access Granted**: The user was granted manager access to a specific project on the HPC portal.
- **SSO Login**: Users need to log in via SSO using their IdM credentials to access the project.
- **Project Management**: Managers can invite new users and review existing accounts through the portal.
- **Documentation**: Additional information and guidance are available on the HPC portal documentation page.
- **Support Contact**: Users should email `hpc-support@fau.de` for any issues, providing a clear description of the problem.
- **Automatic Email**: The email was generated automatically, indicating a standard process for granting access.
- **Vacation Notice**: The user is on vacation and will respond upon return, highlighting the importance of checking availability before escalating issues.

## Root Cause of the Problem
- No immediate problem identified; the email was informational and the user acknowledged receipt.

## Solution
- No solution needed as the email was informational and the user acknowledged receipt.

## Notes for Support Employees
- Ensure users are aware of the SSO login process and where to find documentation.
- Remind users to contact support with clear problem descriptions if they encounter issues.
- Be mindful of user availability, especially during vacation periods.
---

### 2024112842000983_Aktivierung%20eines%20HPC-.Accounts.md
# Ticket 2024112842000983

 ```markdown
# HPC Support Ticket: Activation of an HPC Account

## Keywords
- HPC Account Activation
- HPC Portal
- Invitation
- Genehmigung (Approval)

## Summary
A user, who is a new scientific employee at the university, needs an HPC account but has not received an invitation for activation.

## Root Cause
The user has not received an invitation to activate their HPC account and is unaware of the steps required to obtain one.

## Solution
1. **User Inquiry**: The user inquired about the steps needed to activate their HPC account, as they have not received an invitation.
2. **Initial Admin Response**: The admin initially responded that it takes until the next day after approval in the HPC portal for an account to be activated.
3. **Clarification Needed**: Another admin pointed out that the initial response did not address the user's question about where to get the invitation from.
4. **Portal Check**: The admin noted that the portal indicated the user had confirmed an invitation, suggesting a possible misunderstanding or portal issue.

## General Learnings
- **Invitation Process**: Users need to be informed about where and how to receive an invitation for HPC account activation.
- **Portal Verification**: Admins should verify the portal status to ensure the user has indeed confirmed an invitation.
- **Clear Communication**: Ensure that responses directly address the user's specific questions to avoid confusion.

## Next Steps
- **User Guidance**: Provide clear instructions on how to obtain an invitation for HPC account activation.
- **Portal Review**: Review the portal to ensure it accurately reflects the user's status and any pending invitations.
```
---

### 2023030142003476_Umstellung%20der%20HPC-Accounts%20der%20HS-Coburg%20am%20RRZE%20_%20NHR%40FAU%20-%20corz036h.md
# Ticket 2023030142003476

 # HPC-Support Ticket Conversation Analysis

## Keywords
- HPC-Accounts
- HS-Coburg
- RRZE / NHR@FAU
- HPC-Portal
- DNF-AAI/eduGAIN
- SSH-PublicKeys
- SSH-Key
- Passwort
- Windows PowerShell
- Windows Subsystem für Linux
- mobaXtern
- Putty
- OpenSSH
- JumpHost-Feature
- Deaktivierung
- Datenlöschung

## Summary
The HPC-Support ticket conversation revolves around the transition of HPC accounts from a paper-based system to a new electronic HPC-Portal. Users are required to log in to the portal using DNF-AAI/eduGAIN to continue using their accounts. The conversation also highlights the importance of uploading SSH-PublicKeys and the upcoming deactivation of password-based access.

## Root Cause of the Problem
- The certificate has expired.
- Users need to transition to the new HPC-Portal and upload SSH-PublicKeys.

## Solution
- Users must log in to the HPC-Portal using DNF-AAI/eduGAIN.
- HPC Admins will link existing accounts to the user's identity.
- Users should upload SSH-PublicKeys, which will be synchronized within two hours.
- Access to HPC systems will be restricted to SSH-Key only by the end of March.

## Additional Information
- Detailed instructions and FAQs are available on the provided links.
- Windows users are advised to use Windows PowerShell, Windows Subsystem for Linux, or mobaXtern.
- Accounts not linked by the end of March will be deactivated, and associated data will be deleted after three months.

## References
- [HPC-Portal Usage](https://hpc.fau.de/systems-services/documentation-instructions/getting-started/nhrfau-hpc-portal-usage/)
- [SSH Access](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/)
- [FAQ](https://hpc.fau.de/faqs/#innerID-13183)
- [mobaXtern](https://mobaxterm.mobatek.net/)

## Contacts for Further Assistance
- Rechenzentrum der HS-Coburg
- Fakultät Wirtschaftswissenschaften der HS-Coburg
- HPC Admins (support-hpc@fau.de)
---

### 2024040542000861_Re%3A%20New%20invitation%20for%20%22SMoReM%20-%20Small%20Models%20as%20Role%20Models%22%20waiting%20.md
# Ticket 2024040542000861

 # HPC Support Ticket Analysis

## Keywords
- SSO Login
- Fraunhofer Gesellschaft
- Fehler eingetreten
- HPC Portal
- IdM Credentials
- SSH Public Key

## Summary
A user received an invitation to join an HPC project but encountered an error ("Fehler eingetreten") when attempting to log in via SSO using their Fraunhofer Gesellschaft credentials.

## Root Cause
The user was unable to log in to the HPC portal using their Fraunhofer Gesellschaft credentials, resulting in an error message.

## Solution
No solution was provided in the conversation. The user was advised to contact HPC support for further assistance.

## General Learnings
- Users may encounter login issues when using SSO with external institution credentials.
- It is important to provide clear instructions for uploading SSH public keys after accepting an invitation.
- Users should be directed to the documentation for further information and troubleshooting steps.

## Next Steps
- HPC Admins should investigate the SSO login issue with Fraunhofer Gesellschaft credentials.
- The 2nd Level Support team should be prepared to assist users with similar login issues.
- Consider updating the documentation to include troubleshooting steps for SSO login errors.
---

### 2023030142000942_Problem%20beim%20upload%20des%20ssh%20keys.md
# Ticket 2023030142000942

 # HPC Support Ticket: SSH Key Upload Issue

## Keywords
- SSH key upload
- Error message
- HPC portal
- Account activation
- Login issue

## Problem Description
- User encountered an error while uploading SSH keys (both RSA and ed25519) on the HPC portal.
- Error message: `Error - Unclosed counted closure near index 19 ^[a-zA-Z0-9+/=]{68, }$ ^ (Status: 500) for ID 'ED'`

## Root Cause
- The error was due to a bug in the HPC portal that was recently introduced.

## Solution
- The bug was identified and fixed by the HPC Admins.
- User was able to upload the SSH key successfully after the bug was resolved.

## Additional Issue
- After successfully uploading the SSH key, the user was able to log in to `cshpc.rrze.fau.de` but encountered an issue when trying to log in to `fritz.nhr.fau.de`.
- Error message: `This account is currently not available. Connection to fritz.nhr.fau.de closed`

## Next Steps
- The user needs to check if there are any additional activation steps required for the account on `fritz.nhr.fau.de`.
- Further investigation is needed to determine why the account is not available.

## General Learnings
- Bugs in the HPC portal can cause unexpected errors during SSH key upload.
- After resolving the initial issue, ensure that the user's account is fully activated and accessible on all required systems.
- Clear communication with the user is essential to guide them through the setup process.
---

### 2023100942001664_Shh%20Keys%20for%20lecture%20-%20Lehrveranstaltung%20Department%20Geographie%20-%20gwku.md
# Ticket 2023100942001664

 # HPC Support Ticket: SSH Keys for Lecture

## Keywords
- HPC Accounts
- Bulk Accounts
- IDM Credentials
- SSH Keys
- Password Authentication
- Student Access

## Summary
A Ph.D. student from the Department of Geography and Geosciences requested HPC accounts for approximately 20 students participating in a seminar. The user inquired about the necessity of SSH keys for each physical PC/Laptop used to access the HPC systems.

## Root Cause
The user needed clarification on whether SSH keys were required for each device or if there was a simplified access method using HPC credentials and passwords.

## Solution
- **Bulk Accounts Creation**: HPC Admins decided to create bulk accounts using IDM, which would use password authentication.
- **Account List**: The user provided a list of IDM credentials for the students.
- **Account Creation**: HPC Admins created accounts (srse001h to srse019h) with an expiration date of 10.4.23.
- **Student Instructions**: Students were instructed to find their respective HPC IDs from the IDM portal.

## General Learnings
- For seminars and lectures, bulk accounts can be created using IDM credentials.
- These accounts use password authentication, simplifying access for students.
- Students need to retrieve their HPC IDs from the IDM portal.
- No need for individual SSH keys for each device; password authentication is sufficient.

## Follow-up
- Ensure students are informed about the account creation and how to access their HPC IDs.
- Monitor the expiration dates of the accounts and extend if necessary.
---

### 2024022942003549_Migration%20of%20wsw5002h%20HPC%20accounts%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20man.md
# Ticket 2024022942003549

 # HPC Support Ticket: Migration of HPC Accounts to New Portal / SSH Keys Mandatory

## Keywords
- HPC account migration
- SSH keys
- HPC portal
- Single Sign-On (SSO)
- IdM portal
- SSH key types (RSA, ECDSA, ED25519)
- Usage statistics
- ClusterCockpit
- Jupyterhub

## Summary
- **Migration Process**: Existing HPC accounts are being migrated from the IdM portal to a new online HPC portal.
- **Access Method**: From March 11th, access to HPC systems will require SSH keys only.
- **SSH Key Types**: Accepted types are RSA (4096 bits), ECDSA (512 bits), and ED25519.
- **SSH Key Upload**: Users need to generate SSH key pairs with passphrases and upload the public key to the HPC portal.
- **Portal Access**: The HPC portal can be accessed via SSO using IdM credentials.
- **Expiration Notices**: Users may receive expiration notices from the IdM portal, which can be ignored as the HPC portal will be the sole source for account validity.
- **Account Management**: Users should contact their PI or project manager for account validity updates.
- **Usage Statistics**: Usage statistics will be visible to PIs and project managers.
- **ClusterCockpit and Jupyterhub**: Access to these services will be via SSO links from within the HPC portal.

## Root Cause of the Problem
- The migration process requires users to adapt to new access methods and update their SSH keys.

## Solution
- Users should generate and upload SSH keys to the new HPC portal.
- Access the HPC portal using SSO with IdM credentials.
- Ignore expiration notices from the IdM portal.
- Contact PIs or project managers for account validity updates.
- Use SSO links for ClusterCockpit and Jupyterhub access.

## Additional Resources
- [SSH Secure Shell Access Documentation](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/)
- [FAQs](https://hpc.fau.de/faqs/#ID-230)

## Notes for Support Employees
- Ensure users are aware of the migration process and the requirement for SSH keys.
- Provide guidance on generating and uploading SSH keys.
- Direct users to the appropriate documentation and FAQs for further assistance.
- Inform users about the changes in account management and access methods for ClusterCockpit and Jupyterhub.
---

### 2024121842002042_Unable%20to%20access%20Alex%20cluster.md
# Ticket 2024121842002042

 # HPC Support Ticket: Unable to Access Alex Cluster

## Keywords
- SSH access
- Alex cluster
- Permission denied
- Public key
- HPC introduction

## Problem Description
- User unable to access Alex cluster using SSH from both local PC and HPC account.
- Error messages:
  - From local PC: "This account is currently not available. Connection to alex.nhr.fau.de closed."
  - From HPC account: "Permission denied (publickey,gssapi-keyex,gssapi-with-mic)."

## Root Cause
- Account access issue and potential public key authentication problem.

## Solution
- **HPC Admin** resolved the account access issue, allowing the first SSH command to work.
- User was advised to attend the HPC introduction for new users to learn more about SSH access.

## General Learnings
- Ensure account access is properly configured for cluster access.
- Attend HPC introduction sessions for comprehensive guidance on SSH access and other HPC functionalities.
- Public key authentication issues may require additional configuration or troubleshooting.

## Next Steps
- Verify account access and permissions.
- Ensure proper public key setup for SSH access.
- Attend relevant training sessions for further assistance.
---

### 2024022842002168_Migration%20of%20mfh3_mfpp%20HPC%20accounts%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20ma.md
# Ticket 2024022842002168

 # HPC Support Ticket Summary

## Subject
Migration of mfh3/mfpp HPC accounts to new HPC portal / SSH keys become mandatory

## Keywords
- HPC account migration
- SSH keys
- HPC portal
- Single Sign-On (SSO)
- IdM portal
- ClusterCockpit
- Jupyterhub

## Summary
The HPC services at FAU are migrating existing HPC accounts to a new online HPC portal. Users will need to generate and upload SSH keys for access. The IdM portal will no longer manage HPC account validity.

## Key Points
- **Migration to New HPC Portal**: Access the new portal at [https://portal.hpc.fau.de](https://portal.hpc.fau.de) using SSO with IdM credentials.
- **SSH Keys Mandatory**: From March 11, access to HPC systems will require SSH keys. Accepted types are RSA (4096 bits), ECDSA (512 bits), and ED25519.
- **SSH Key Documentation**: Refer to [SSH documentation](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/) and [FAQs](https://hpc.fau.de/faqs/#ID-230).
- **Windows Users**: Recommended to use OpenSSH built into Windows (Power)Shell or MobaXterm instead of Putty.
- **Account Validity**: The HPC portal will manage account validity. Contact the PI or project manager for extensions or new accounts.
- **Usage Statistics**: Viewable by users, PIs, and project managers.
- **ClusterCockpit and Jupyterhub**: Access via Single Sign-On links within the HPC portal.

## Root Cause of the Problem
- Users need to adapt to the new HPC portal and SSH key requirements for continued access to HPC services.

## Solution
- Generate and upload SSH keys as per the provided documentation.
- Use the new HPC portal for account management and access to services like ClusterCockpit and Jupyterhub.
- Contact the PI or project manager for account validity updates.

## Additional Notes
- Ignore automatic messages from the IdM portal regarding HPC service expiration.
- The HPC portal and IdM portal are completely decoupled.
---

### 2023053042002963_Migration%20of%20bco%2A%20HPC%20accounts%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20manda.md
# Ticket 2023053042002963

 # HPC Support Ticket: Migration of HPC Accounts to New Portal / SSH Keys Mandatory

## Keywords
- HPC account migration
- SSH keys
- HPC portal
- Single Sign-On (SSO)
- IdM portal
- Passphrase
- RSA, ECDSA, ED25519
- ClusterCockpit
- Jupyterhub
- Bash shell

## Summary
The HPC services at FAU are migrating user accounts from the IdM portal to a new online HPC portal. This migration includes changes to authentication methods and account management processes.

## Key Points
- **New HPC Portal**: Accessible at [https://portal.hpc.fau.de](https://portal.hpc.fau.de).
- **Authentication**: Login using Single Sign-On (SSO) with IdM credentials.
- **SSH Keys**: Mandatory for accessing HPC systems by mid-June. Accepted types are RSA (4096 bits), ECDSA (512 bits), and ED25519.
- **SSH Key Upload**: Upload public keys to the HPC portal. It takes up to two hours for all systems to recognize the update.
- **Documentation**: Available at [HPC Documentation](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/) and [FAQs](https://hpc.fau.de/faqs/#ID-230).
- **Windows Users**: Recommended to use OpenSSH built into Windows (Power)Shell or MobaXterm instead of Putty.
- **Account Validity**: Managed through the HPC portal. Contact PI or project manager for extensions or new accounts.
- **Usage Statistics**: Visible to users, PIs, and project managers.
- **ClusterCockpit and Jupyterhub**: Access via Single Sign-On links within the HPC portal.
- **Shell Change**: All systems will use Bash shell.

## Root Cause of the Problem
- Expiration of the certificate and the need to migrate to a new HPC portal with updated authentication methods.

## Solution
- Users need to generate and upload SSH keys to the new HPC portal.
- Access the HPC portal using SSO with IdM credentials.
- Use the new HPC portal for account management and monitoring usage statistics.
- Contact PI or project manager for account extensions or new accounts.

## Additional Notes
- Ignore automatic messages from the IdM portal regarding HPC service expiration.
- The new HPC portal is the sole source for account validity.
- The migration ensures a more streamlined and secure access process for HPC services.
---

### 2024102942002445_Cannot%20find%20invitation%20to%20project.md
# Ticket 2024102942002445

 ```markdown
# HPC Support Ticket: Cannot Find Invitation to Project

## Keywords
- HPC Portal
- Invitation
- Project ID
- Email Address
- Login

## Problem
- User cannot see the invitation to a new project on the HPC portal landing page.
- The user logs into the HPC portal with one email address but the invitation was sent to a different email address.

## Root Cause
- The invitation was sent to an email address different from the one used to log into the HPC portal.

## Solution
- Ensure that the email address used for logging into the HPC portal matches the email address to which the invitation was sent.

## Lessons Learned
- Verify the email address used for logging into the HPC portal.
- Ensure that invitations are sent to the correct email address associated with the user's HPC portal account.
```
---

### 2023112342003704_Re%3A%20New%20invitation%20for%20%22Tier3%20Grundversorgung%20Uni-Bayreuth%20%28via%20IT-Servicezent.md
# Ticket 2023112342003704

 # HPC Support Ticket Analysis

## Keywords
- Invitation
- HPC Portal
- SSO Login
- IdM Credentials
- SSH Public Key
- Email Address Mismatch

## Problem
- **Root Cause**: The email address used for the invitation did not match the email address provided by DFN-AAI, leading to the invitation not being correctly associated with the user's login.

## Solution
- **Action Taken**: The HPC Admin corrected the email address mismatch, allowing the user to find the invitation in their user area.

## General Learnings
- Ensure that the email address used for invitations matches the one provided by DFN-AAI.
- Users should log in via SSO using their IdM credentials to accept invitations.
- After accepting the invitation, users need to upload an SSH public key ('ssh-rsa') to the corresponding account.

## Steps for Users
1. Log in to the HPC portal via SSO using IdM credentials.
2. Navigate to 'User' -> 'Your Invitations' to accept the invitation.
3. Upload an SSH public key to the corresponding account under 'User' -> 'Your Accounts'.

## Steps for HPC Admins
- Verify that the email address used for invitations matches the one provided by DFN-AAI.
- If there is a mismatch, correct the email address and resend the invitation.

## Contact for Further Assistance
- In case of problems, users should send an email with a clear description of the issue to `hpc-support@fau.de`.
---

### 2024022942002862_Migration%20of%20mpfp000h%20HPC%20accounts%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20man.md
# Ticket 2024022942002862

 # HPC Support Ticket: Migration of HPC Accounts to New Portal / SSH Keys Mandatory

## Keywords
- HPC account migration
- SSH keys
- HPC portal
- IdM portal
- Single Sign-On (SSO)
- SSH key types (RSA, ECDSA, ED25519)
- ClusterCockpit
- Jupyterhub

## Summary
- **Migration Process**: Existing HPC accounts are being migrated from the IdM portal to a new online HPC portal.
- **Access Method**: Starting March 11th, access to HPC systems will be via SSH keys only.
- **SSH Key Requirements**: Accepted SSH key types are RSA (minimum 4096 bits), ECDSA (512 bits), and ED25519.
- **Portal Access**: The new HPC portal can be accessed at [https://portal.hpc.fau.de](https://portal.hpc.fau.de) using SSO with IdM credentials.
- **Account Validity**: The HPC portal will be the sole source for account validity starting from the end of February.
- **Usage Statistics**: Users, PIs, and project managers can view usage statistics in the HPC portal.
- **ClusterCockpit and Jupyterhub**: Access these services via Single Sign-On links within the HPC portal.

## Root Cause of the Problem
- Users need to transition to the new HPC portal and set up SSH keys for continued access to HPC systems.

## Solution
- **Login**: Access the new HPC portal using SSO with IdM credentials.
- **SSH Keys**: Generate and upload SSH key pairs with a passphrase to the HPC portal.
- **Documentation**: Refer to the provided documentation and FAQs for guidance on SSH keys.
- **Windows Users**: Recommended to use OpenSSH built into Windows (Power)Shell or MobaXterm instead of Putty.
- **Account Validity**: Contact the PI or project manager to update the validity of the HPC account.

## Additional Notes
- Ignore automatic messages from the IdM portal regarding service expiration.
- The HPC portal and IdM portal are completely decoupled.
- New HPC accounts for colleagues or students should be requested through the PI or project manager.

## References
- [HPC Portal](https://portal.hpc.fau.de)
- [SSH Documentation](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/)
- [FAQs](https://hpc.fau.de/faqs/#ID-230)
---

### 2024042542002848_Config%20file%20hpc.md
# Ticket 2024042542002848

 # HPC Support Ticket Conversation: Config File Issue

## Keywords
- SSH Configuration
- VS Code
- ProxyJump
- IdentityFile
- Username
- PasswordAuthentication

## Problem
- User unable to connect to HPC account via SSH in VS Code.
- Config file issues with ProxyJump and IdentityFile.
- User prompted for password for an unknown account.

## Root Cause
- Incorrect configuration in the SSH config file.
- Missing username in the ProxyJump entry.

## Solution
- Ensure the SSH config file includes the correct username for the ProxyJump entry.
- Follow the provided template for the SSH config file.

## Steps Taken
1. User provided initial SSH config file.
2. HPC Admin suggested referring to the documentation for VS Code configuration and provided a template for the SSH config file.
3. User updated the config file but still faced issues.
4. HPC Admin advised adding an additional entry for `csnhr.nhr.fau.de` with the correct username.

## Documentation Links
- [VS Code Configuration](https://doc.nhr.fau.de/access/ssh-vscode/)
- [SSH Config Template](https://doc.nhr.fau.de/access/ssh-command-line/#template-for-connecting-to-hpc-systems)

## Final Config Example
```plaintext
Host tinyx.nhr.fau.de
    HostName tinyx.nhr.fau.de
    User iwso130h
    ProxyJump iwso130h@csnhr.nhr.fau.de
    IdentityFile ~/.ssh/id_ed25519_nhr_fau
    IdentitiesOnly yes
    PasswordAuthentication no
    PreferredAuthentications publickey
    ForwardX11 no
    ForwardX11Trusted no
```

## Conclusion
- Ensure all necessary entries in the SSH config file are correctly configured with the appropriate usernames and paths.
- Refer to the provided documentation for detailed configuration steps.
---

### 2024121042002995_DRINGEND%20-%20Verdacht%20auf%20illegales%20Account-Sharing%20oder%20Account-Missbrauch%20-%20Projek.md
# Ticket 2024121042002995

 # HPC Support Ticket: Account Sharing or Misuse Suspicion

## Keywords
- Account Sharing
- Account Misuse
- SSH Keys
- Nutzungsbedingungen
- Projektverantwortung
- Account Sperrung
- Abuse-Team
- CISO

## Summary
A suspicion of illegal account sharing or account misuse was raised when a student contacted HPC support regarding a filesystem issue. The account in question was being used by someone other than the account owner.

## Root Cause
- A student (Master's degree candidate) was using the account of a project member to run experiments.
- The student used an SSH key registered to the project member's account.

## Solution
1. **Account Sperrung**: The account was immediately suspended.
2. **Investigation**: The project leader (PI) was contacted to clarify the situation.
3. **SSH Key Deletion**: The SSH key used by the student was deleted.
4. **Account Reactivation**: After the PI confirmed the situation and assured compliance with the rules, the account was reactivated.
5. **New SSH Key**: The account owner was instructed to upload a new SSH key.
6. **Student Account Creation**: The PI was advised to invite the student to the project to create a personalized account.

## Lessons Learned
- **Account Sharing Prohibition**: Account sharing is strictly prohibited as per the usage conditions.
- **PI Responsibility**: The PI is responsible for ensuring compliance with the usage conditions within the project.
- **SSH Key Management**: SSH keys should not be shared and must be managed securely.
- **Prompt Action**: Immediate action is necessary to prevent further misuse and potential damage.

## Follow-Up Actions
- Ensure all project members are aware of the usage conditions.
- Monitor account usage to prevent future misuse.
- Regularly review and update SSH keys for security.

## References
- Nutzungsbedingungen for HPC systems at NHR@FAU
- HPC support contact: support-hpc@fau.de
- HPC website: [https://hpc.fau.de/](https://hpc.fau.de/)
---

### 2024111342003731_Alex%20cluster%20instantly%20disconnects%20after%20ssh..md
# Ticket 2024111342003731

 # HPC Support Ticket: Instant Disconnect After SSH

## Keywords
- SSH
- Instant Disconnect
- `.bash_profile`
- ProxyJump
- VPN
- Windows PC
- Linux Ubuntu
- `ssh -vvv`

## Problem Description
User experiences instant disconnect after SSH into the cluster using ProxyJump or VPN. The issue occurs on both Windows PC and Linux Ubuntu systems. The problem started after modifying the `.bash_profile` file.

## Root Cause
The root cause of the problem is likely due to changes made in the `.bash_profile` file. The user mentioned that the issue started after modifying this file to configure VSCode terminal.

## Diagnostic Steps
- The user provided the output of the `ssh -vvv` command, which shows successful authentication but immediate disconnection.
- The output indicates that the SSH session is established but terminates abruptly without any clear error message.

## Solution
The user suggested that the issue might be resolved by removing the contents of the `.bash_profile` file. This suggests that the modifications in the `.bash_profile` file are causing the SSH session to terminate immediately.

## Action Taken
- HPC Admins should access the user's account and remove or comment out the contents of the `.bash_profile` file to verify if this resolves the issue.
- If the problem persists, further investigation into the `.bash_profile` modifications and their impact on the SSH session is required.

## Follow-up
- After removing the contents of the `.bash_profile` file, the user should attempt to SSH into the cluster again and report back if the issue is resolved.
- If the issue is not resolved, additional diagnostic steps may be necessary to identify the exact cause of the disconnect.

## Notes
- The issue affects both Windows and Linux systems, indicating that it is not platform-specific.
- The user's suggestion to remove the `.bash_profile` contents is a good starting point for troubleshooting.

## Related Teams
- HPC Admins
- 2nd Level Support Team
- Software and Tools Developer

## Documentation
This report can be used as a reference for similar issues in the future. If other users experience instant disconnects after modifying their `.bash_profile` file, the steps outlined here can be followed to diagnose and resolve the problem.
---

### 2022091442004165_hpc-Account%20f%C3%83%C2%BCr%20Uni-Bamberg-Personen.md
# Ticket 2022091442004165

 ```markdown
# HPC Support Ticket: HPC Account for University of Bamberg Personnel

## Keywords
- HPC Account
- SSO (Single Sign-On)
- HPC Portal
- Tier3 Project Numbers
- SSO Attributes
- IdP (Identity Provider)
- SdP (Service Provider)

## Summary
A user from the University of Bamberg requested an HPC account. The process involved setting up the account through the HPC portal and ensuring the necessary SSO attributes were configured.

## Root Cause of the Problem
- The user needed an HPC account.
- The University of Bamberg needed to configure SSO attributes for the HPC portal.

## Solution
1. **HPC Portal Registration**: The user was instructed to log in to the HPC portal using SSO.
2. **SSO Attribute Configuration**: The University of Bamberg needed to configure the following SSO attributes for the HPC portal:
   - `urn:oid:2.5.4.42` - `urn:mace:dir:attribute-def:givenName`: `givenName`
   - `urn:oid:2.5.4.4` - `urn:mace:dir:attribute-def:sn`: `sn`
   - `urn:oid:0.9.2342.19200300.100.1.3` - `urn:mace:dir:attribute-def:mail`: `mail`
   - `urn:oid:1.3.6.1.4.1.5923.1.1.1.6` - `urn:mace:dir:attribute-def:eduPersonPrincipalName`: `eduPersonPrincipalName`
   - `urn:oid:1.3.6.1.4.1.5923.1.1.1.9` - `urn:mace:dir:attribute-def:eduPersonScopedAffiliation`: `eduPersonScopedAffiliation`
3. **Tier3 Project Numbers**: The HPC admin mentioned the need for Tier3 project numbers for the user's account.

## General Learnings
- HPC account creation involves logging in through the HPC portal using SSO.
- Proper configuration of SSO attributes is crucial for successful account creation.
- Tier3 project numbers may be required for account setup.
```
---

### 2024030142001574_Status%20of%20HPC%20account.md
# Ticket 2024030142001574

 # HPC Support Ticket: Status of HPC Account

## Keywords
- HPC account expiry
- Account migration
- SSH keys
- HPC portal
- IdM portal
- Account extension

## Summary
A user received an email stating the expiry of their recently assigned HPC account and inquired about the reason and how to extend it.

## Root Cause
- The user was not informed about the migration process from the IdM portal to the new HPC portal.
- The expiry email from the IdM portal caused confusion.

## Solution
- The HPC Admin explained the migration process and clarified that the expiry notice from the IdM portal can be ignored.
- The user was directed to the new HPC portal for account management and SSH key setup.
- For account extension, the user was advised to contact their project manager or PI.

## General Learnings
- **Migration Notice**: Ensure all users are informed about system migrations and changes in account management processes.
- **SSH Key Setup**: Users need to generate and upload SSH keys to the new HPC portal for continued access.
- **Account Extension**: Users should contact their project manager or PI for account extensions, not the HPC support team.
- **Portal Decoupling**: The new HPC portal is decoupled from the IdM portal, and users should refer to the HPC portal for account validity.

## Relevant Links
- [HPC Portal](https://portal.hpc.fau.de)
- [SSH Documentation](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/)
- [FAQs](https://hpc.fau.de/faqs/#ID-230)
---

### 2024051642000258_AW%3A%20ssh%20into%20alex%20with%20command%20restrictions.md
# Ticket 2024051642000258

 # HPC Support Ticket: SSH into HPC with Command Restrictions

## Keywords
- SSH command restrictions
- `authorized_keys`
- `command` option
- Permission denied
- OpenSSH config files
- `LocalCommand`
- Absolute path
- HPC portal

## Summary
A user encountered issues with SSH command restrictions using the `command` option in the `authorized_keys` file. The problem resulted in a "Permission denied" error when attempting to execute restricted commands.

## Root Cause
- The `command` option in the HPC portal was not fully implemented, causing keys with command restrictions to be dropped.
- The user attempted to use relative paths instead of absolute paths for the command.

## Solution
- The HPC Admins implemented the `command` option in the HPC portal.
- The user was instructed to use absolute paths starting with `/home/` for the command.

## Lessons Learned
- Ensure that the `command` option is properly implemented and supported in the HPC portal.
- Always use absolute paths for commands in the `authorized_keys` file.
- The `LocalCommand` option in OpenSSH config files runs after authentication but before the shell starts, which can affect the availability of environment setups.

## Follow-up
- The user confirmed that the issue was resolved after making the necessary changes.
- Additional code was added to the API script to allow SCP commands.

## References
- OpenSSH documentation on `authorized_keys` and `command` option.
- HPC portal documentation on SSH key management.
---

### 2024041442000718_key%20content%20in%20.ssh%20file.md
# Ticket 2024041442000718

 ```markdown
# HPC Support Ticket: Key Content in .ssh File

## Keywords
- SSH key
- Remote access
- PyCharm
- HPC Portal
- Error message: "indicate package is too large"

## Problem Description
- User unable to access remote server due to error message "indicate package is too large."
- User needs to upload new public key to HPC Portal but cannot access .ssh file on remote host.
- User is using PyCharm for remote connection.

## Root Cause
- User's SSH key setup is causing issues with remote access.
- User needs to upload a new public key to the HPC Portal but lacks the necessary content from the .ssh file.

## Solution
- **Option 1:** Create a new SSH key pair on the second machine and upload the new public key to the HPC Portal.
  - Instructions: [SSH Command Line Guide](https://doc.nhr.fau.de/access/ssh-command-line/)
- **Option 2:** Transfer the existing SSH key pair from the first machine to the second machine.
  - Recommendation: Use separate key pairs for better security.

## Additional Notes
- HPC Admins have no experience with remote usage of PyCharm, which seems to be a feature of the Professional version.
- User may need to seek assistance from their supervisor or someone else at their chair for PyCharm-specific issues.

## References
- [SSH Command Line Guide](https://doc.nhr.fau.de/access/ssh-command-line/)
- [HPC Portal](https://portal.hpc.fau.de/)
```
---

### 2024031242002374_Account%20ilev005h%20deaktiviert.md
# Ticket 2024031242002374

 # HPC Support Ticket: Account Deactivation and SSH Key Issue

## Keywords
- Account deactivation
- SSH key
- HPC portal
- IdM portal
- Account migration
- SSH log
- SHA256 fingerprint

## Problem Description
- User received a notification that their account (ilev005h) had expired and could not log in to the cluster.
- User attempted to create a new account but was unable to activate it due to the existing account still being active in the HPC portal.
- User had previously set up an SSH key that had been functioning correctly.

## Root Cause
- The account migration from the IdM portal to the HPC portal caused issues with account status and SSH key functionality.
- The SSH key was not being recognized correctly on the landing node.

## Solution
- HPC Admin identified and fixed the issue on their end after reviewing the SSH log provided by the user.
- The fix was applied to the main systems, with some systems requiring additional time to update.

## Steps Taken
1. User reported the issue with account deactivation and SSH key not working.
2. HPC Admin provided a link to the migration notice: [Migration of FAU HPC Accounts from IdM Portal to HPC Portal](https://hpc.fau.de/2024/03/04/migration-of-fau-hpc-accounts-from-idm-portal-to-hpc-portal/).
3. User verified the SHA256 fingerprint of the SSH key and provided the SSH log.
4. HPC Admin identified the issue using the SSH log and applied a fix.
5. User confirmed that the issue was resolved and they could access the cluster again.

## Lessons Learned
- Account migrations can cause temporary issues with account status and SSH key functionality.
- Providing detailed logs (such as SSH logs) can help HPC Admins identify and resolve issues more quickly.
- Communication about migrations and changes in account management systems is crucial to help users understand and troubleshoot issues.
---

### 2023070642001452_Alex%20login%20-%20bccb002h.md
# Ticket 2023070642001452

 # HPC Support Ticket: Alex Login Issue

## Keywords
- HPC Account Expiration
- SSH Key Pair
- HPC Portal Migration
- Account Reactivation

## Problem Description
- User unable to log in to the Alex cluster.
- Error message: "This account is currently not available."
- User had generated a key pair three weeks prior and it was working fine.

## Root Cause
- HPC account expired on 30.06.23.
- Account was migrated to the new HPC portal, causing it to be marked as expired in the IDM.

## Solution
- User needs to update their SSH PublicKey in the new HPC portal.
- Accepted SSH key types:
  - RSA with a length of at least 4096 bits
  - ECDSA with a length of 512
  - ED25519
- It may take up to two hours for all HPC systems to recognize the updated SSH PublicKeys.
- User should contact their PI or project manager to update the validity of their HPC account.

## Additional Information
- The new HPC portal does not recognize passwords; SSH keys are mandatory.
- The IdM portal and the new HPC portal are completely decoupled.
- For Windows users, it is recommended to use OpenSSH built into the Windows (Power)Shell or MobaXterm instead of Putty.

## Relevant Links
- [HPC Account Application](https://www.rrze.fau.de/infocenter/kontakt-hilfe/formulare/#hpc)
- [SSH Documentation](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/)
- [FAQs](https://hpc.fau.de/faqs/#ID-230)

## Follow-up Actions
- Ensure the user's group is set correctly in the HPC portal.
- Verify that the user has followed the migration instructions sent via email.
---

### 2024101742002959_Account%20f%C3%83%C2%BCr%20HPCs.md
# Ticket 2024101742002959

 # HPC Support Ticket: Account Management and SSH Configuration

## Keywords
- HPC Account Management
- SSH Key Configuration
- Account Verlängerung
- HPC-Portal
- IdM-Portal
- SSH Config File

## Problem
- Users from the Institute for Water Engineering and Water Management had three active HPC accounts that were not visible in the HPC-Portal.
- The users were unsure if their account extensions were processed.
- There was confusion regarding the new SSH key pair access method.
- Users needed to configure SSH for multiple HPC accounts on a shared server.

## Root Cause
- The IdM-Portal no longer manages HPC accounts; all management is now done through the HPC-Portal.
- Users had not yet registered in the HPC-Portal, which is required to link existing accounts.
- Incorrect user names and email addresses were provided, leading to confusion in account linking.

## Solution
- **Account Management:**
  - Users were instructed to register in the HPC-Portal.
  - HPC Admins linked the users' accounts after their initial registration.
  - Account extensions and new account requests should be directed to the responsible IT personnel (e.g., Frau Marginean).

- **SSH Configuration:**
  - Users were advised to configure their SSH settings correctly, avoiding the use of "@" in the host definition.
  - Each user should have their own identity file to comply with security policies.
  - The `User` field in the SSH config should be defined separately, not within the `Host` field.

## Example SSH Config
```plaintext
# needed only for Tier3-Grundversorgung
Host fhn001
    HostName meggie.rrze.uni-erlangen.de
    User fhn001
    ProxyJump csnhr.nhr.fau.de
    IdentityFile ~/.ssh/id_ed25519_nhr_fau
    IdentitiesOnly yes
    PasswordAuthentication no
    PreferredAuthentications publickey
    ForwardX11 no
    ForwardX11Trusted no

# needed only for Tier3-Grundversorgung
Host fhn0001h
    HostName meggie.rrze.uni-erlangen.de
    User fhn0001h
    ProxyJump csnhr.nhr.fau.de
    IdentityFile ~/.ssh/id_ed25519_nhr_fau
    IdentitiesOnly yes
    PasswordAuthentication no
    PreferredAuthentications publickey
    ForwardX11 no
    ForwardX11Trusted no
```

## Additional Notes
- Ensure that all users are registered in the HPC-Portal to facilitate account management.
- Regularly update account information and extensions through the designated IT personnel.
- Follow the provided SSH configuration guidelines to avoid security violations and ensure proper access to HPC resources.
---

### 2022113042003621_Re%3A%20New%20invitation%20for%20%22GastroDigitalShirt%20-%20Development%20and%20test%20of%20deep%20.md
# Ticket 2022113042003621

 ```markdown
# HPC-Support Ticket: SSO Login Issue for External User

## Summary
- **User**: External user from Albert-Ludwigs-Universität Freiburg
- **Issue**: Unable to log in via SSO, stuck on a cryptic page
- **Project**: GastroDigitalShirt

## Root Cause
- **Initial Problem**: NameID element missing in SAML response
- **Secondary Problem**: Required attributes not transmitted after successful SSO login

## Steps Taken
1. **Initial Diagnosis**:
   - User reported issue with SSO login.
   - HPC Admins identified missing NameID element in SAML response.

2. **Adjustments Made**:
   - HPC Admins requested external IdP team to adjust IdP configuration.
   - Added `eduPersonTargetedID` attribute to IdP configuration.
   - Changed NameID format to `Transient` in consultation with SSO team.

3. **Further Issues**:
   - User reported successful SSO login but account creation failed due to missing attributes.
   - HPC Admins identified required attributes not being transmitted.

4. **Resolution**:
   - External IdP team released necessary attributes.
   - Successful logins observed from the compute center of Uni Freiburg.

## Solution
- Ensure external IdP configuration includes the necessary attributes and NameID format.
- Verify that the full set of attributes required by the HPC portal is transmitted after SSO login.

## Keywords
- SSO Login
- SAML
- NameID
- IdP Configuration
- eduPersonTargetedID
- Transient Format
- Attribute Transmission

## Lessons Learned
- Proper configuration of IdP is crucial for successful SSO login.
- Missing attributes can prevent account creation even if SSO login is successful.
- Collaboration with external IdP teams is essential for resolving such issues.
```
---

### 2024013042002451_Migration%20of%20iwpa40%20HPC%20account%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20mandat.md
# Ticket 2024013042002451

 # HPC Account Migration to New Portal

## Keywords
- HPC account migration
- SSH keys
- Single Sign-On (SSO)
- HPC portal
- IdM portal
- ClusterCockpit
- Jupyterhub

## Summary
The HPC account migration process involves moving from the IdM portal to a new online HPC portal. Users must generate and upload SSH keys for access, and the portal provides usage statistics and updated services.

## Key Points
- **Migration Process**: The HPC account is being migrated from the IdM portal to a new online HPC portal.
- **Access Method**: Access to HPC systems will be via SSH keys only. Accepted key types are RSA (4096 bits), ECDSA (512 bits), and ED25519.
- **SSH Key Upload**: Users must generate SSH key pairs with passphrases and upload the public keys to the HPC portal.
- **Single Sign-On (SSO)**: Login to the HPC portal is via SSO using IdM credentials.
- **Account Validity**: The HPC portal is the sole source for account validity. Users should ignore expiration notices from the IdM portal.
- **Usage Statistics**: The HPC portal displays usage statistics, which are also visible to PIs and project managers.
- **ClusterCockpit and Jupyterhub**: Access to these services is now via SSO links within the HPC portal.

## Action Required
- Generate and upload SSH keys to the HPC portal.
- Use SSO links for ClusterCockpit and Jupyterhub.
- Contact the PI or project manager for account validity updates.

## Additional Information
- **Documentation**: [SSH Secure Shell Access](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/)
- **FAQs**: [HPC FAQs](https://hpc.fau.de/faqs/#ID-230)

## Solution
- Follow the instructions to generate and upload SSH keys.
- Use the SSO links for accessing ClusterCockpit and Jupyterhub.
- Contact the PI or project manager for any account-related updates.

## Root Cause
- The migration process requires users to update their access methods and familiarize themselves with the new HPC portal.

## Notes
- The HPC portal and IdM portal are completely decoupled.
- Failure to respond or log in within two months may result in account deletion.
---

### 2024022742002875_Migration%20of%20iwgt%20HPC%20accounts%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20mandato.md
# Ticket 2024022742002875

 # HPC Support Ticket: Migration of HPC Accounts to New Portal / SSH Keys Mandatory

## Keywords
- HPC account migration
- SSH keys
- HPC portal
- IdM portal
- Single Sign-On (SSO)
- ClusterCockpit
- Jupyterhub
- Account validity
- Usage statistics

## Summary
- **Migration Notice**: HPC accounts are being migrated to a new online HPC portal.
- **SSH Keys**: Access to HPC systems will require SSH keys starting March 11th.
- **Portal Access**: Users should log in to the new HPC portal using SSO with IdM credentials.
- **Account Validity**: The new HPC portal will manage account validity, decoupled from the IdM portal.
- **Usage Statistics**: Users and their PIs/project managers can view usage statistics in the HPC portal.
- **ClusterCockpit and Jupyterhub**: Access these services via SSO links within the HPC portal.

## Root Cause of the Problem
- User was notified about the migration but did not respond due to no longer being affiliated with the relevant department.

## Solution
- The ticket was closed as the user is no longer at the relevant department and cannot respond to the migration notice.

## General Learnings
- **Migration Process**: Understand the steps involved in migrating HPC accounts to the new portal.
- **SSH Key Requirements**: Familiarize with generating and uploading SSH keys.
- **Portal Decoupling**: Recognize that the new HPC portal is independent of the IdM portal for account management.
- **Usage Monitoring**: Be aware that usage statistics are visible to both users and their PIs/project managers.
- **Service Access**: Use SSO links within the HPC portal for accessing ClusterCockpit and Jupyterhub.

## Recommendations
- **User Education**: Ensure users are educated on generating SSH keys and using the new portal.
- **Communication**: Clearly communicate the migration process and the importance of updating account information.
- **Support Resources**: Provide documentation and FAQs to assist users with the migration and SSH key setup.

---

This report serves as a documentation for support employees to reference when similar issues arise.
---

### 2024012242000646_Migration%20of%20iwfa%20HPC%20accounts%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20mandato.md
# Ticket 2024012242000646

 # HPC Support Ticket: Migration of HPC Accounts to New Portal / SSH Keys Mandatory

## Keywords
- HPC account migration
- SSH keys
- HPC portal
- IdM portal
- Single Sign-On (SSO)
- ClusterCockpit
- Jupyterhub

## Summary
The HPC services at FAU are migrating existing HPC accounts to a new online HPC portal. Access to HPC systems will require SSH keys starting from the end of January. Users need to generate and upload their SSH public keys to the new portal.

## Key Points
- **Migration Process**: Existing HPC accounts are being migrated from the IdM portal to a new online HPC portal.
- **SSH Keys**: Access to HPC systems will require SSH keys. Accepted key types are RSA (4096 bits), ECDSA (512 bits), and ED25519.
- **Portal Access**: Users should log in to the new HPC portal using Single Sign-On (SSO) with their IdM credentials.
- **Account Validity**: The new HPC portal will be the sole source for account validity. Users should ignore expiration notices from the IdM portal.
- **Usage Statistics**: The HPC portal will display usage statistics, which will also be visible to PIs and project managers.
- **ClusterCockpit and Jupyterhub**: Users should use the Single Sign-On links from within the HPC portal to access these services.

## Documentation and FAQs
- [SSH Secure Shell Access Documentation](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/)
- [FAQs](https://hpc.fau.de/faqs/#ID-230)

## Solution
1. **Generate SSH Key Pair**: Users should generate an SSH key pair with a passphrase.
2. **Upload Public Key**: Upload the SSH public key to the new HPC portal.
3. **Login to HPC Portal**: Use SSO with IdM credentials to log in to the HPC portal.
4. **Access HPC Systems**: Use the uploaded SSH keys to access HPC systems.

## Additional Notes
- The IdM portal and the new HPC portal are completely decoupled.
- Users should contact their PI or project manager to update the validity of their HPC account.
- For new HPC accounts, users should also contact their PI or project manager.

## Root Cause of Problem
- Users were not aware of the migration process and the requirement for SSH keys.

## Solution Found
- Inform users about the migration process and provide detailed instructions on generating and uploading SSH keys.

---

This report provides a concise summary of the migration process and the necessary steps for users to continue accessing HPC services. It includes relevant links to documentation and FAQs for further assistance.
---

### 2024021542003324_Migration%20of%20mfki%20HPC%20accounts%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20mandato.md
# Ticket 2024021542003324

 # HPC Support Ticket: Migration of HPC Accounts to New Portal / SSH Keys Mandatory

## Keywords
- HPC account migration
- SSH keys
- HPC portal
- Single Sign-On (SSO)
- IdM portal
- Password expiration
- Account validity
- Usage statistics
- ClusterCockpit
- Jupyterhub

## Summary
The HPC services at FAU are migrating existing HPC accounts to a new online HPC portal. This migration involves several changes, including the mandatory use of SSH keys for access and the introduction of a new portal for account management.

## Key Points
- **New HPC Portal**: Accessible at [https://portal.hpc.fau.de](https://portal.hpc.fau.de). Login with SSO using IdM credentials.
- **SSH Keys**: Access to HPC systems will require SSH keys (RSA 4096-bit, ECDSA 512-bit, ED25519). Generate and upload SSH public keys to the HPC portal.
- **Password Expiration**: Ignore automatic messages about HPC service expiration in the IdM portal. The HPC portal will be the sole source for account validity.
- **Account Management**: Contact the PI or project manager to update account validity or request new accounts.
- **Usage Statistics**: Viewable in the HPC portal by users, PIs, and project managers.
- **ClusterCockpit and Jupyterhub**: Use Single Sign-On links from within the HPC portal for access.

## Documentation and FAQs
- **SSH Access Documentation**: [https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/)
- **FAQs**: [https://hpc.fau.de/faqs/#ID-230](https://hpc.fau.de/faqs/#ID-230)

## Recommendations for Windows Users
- Use OpenSSH built into Windows (Power)Shell or MobaXterm instead of Putty.

## Root Cause and Solution
- **Root Cause**: Migration to a new HPC portal and mandatory use of SSH keys.
- **Solution**: Generate and upload SSH keys, use the new HPC portal for account management, and follow the provided documentation for SSH access.

## Additional Notes
- The IdM portal and the new HPC portal are completely decoupled.
- The HPC portal will not automatically update account validity based on contract extensions or departures from the university.

This documentation is intended to assist HPC support employees in understanding and resolving similar issues related to the migration of HPC accounts and the mandatory use of SSH keys.
---

### 2024031942003726_Ihpc100h%20-%20request%20for%20multimode%20GPU%20access.md
# Ticket 2024031942003726

 # HPC Support Ticket: Multimode GPU Access Request

## Keywords
- SSO (Single Sign-On)
- IdM (Identity Management)
- Email Address Association
- Invitation Management
- HPC Portal

## Problem
- User received an invitation to join an HPC project but could not accept it due to an unlinked email address in their IdM account.
- The username provided with the SSO identity was not recognized as an email address.
- The invitation was sent to a personal email address instead of the institutional one.

## Root Cause
- The user's IdM account was not linked to a valid email address, causing issues with invitation management in the HPC portal.

## Solution
- HPC Admin updated the invitation to the user's institutional email address.
- The user's institution (CNR) associated a valid email address with the user's IdM account.
- The invitation was successfully moved to the user's institutional email address.

## General Learnings
- Ensure that IdM accounts are linked to valid email addresses for proper invitation management.
- Communicate with the user's institution to resolve email association issues.
- Update invitations in the HPC portal as needed to reflect the correct email addresses.

## Actions Taken
- HPC Admin updated the invitation email address.
- The user's institution updated the email association in the IdM account.
- The invitation was successfully transferred to the user's institutional email address.

## Follow-up
- No further action required from the HPC Admin or the user.
---

### 2022052342003067_IdP-Freischaltung%20f%C3%83%C2%BCr%20portal.hpc.fau.de%20%28Teilticket%202022-05-0462%5C01%29.md
# Ticket 2022052342003067

 # HPC-Support Ticket Conversation Analysis

## Subject
IdP-Freischaltung für portal.hpc.fau.de (Teilticket 2022-05-0462\01)

## Keywords
- Shibboleth
- SSO
- eduPersonPrincipalName (eppn)
- Account Management
- HPC Portal
- NHR@FAU
- DFN-AAI-Föderation
- Meta-Daten
- Attributes
- Persistent-ID
- samlPairwiseID

## Summary
The conversation revolves around the integration of the HPC portal at NHR@FAU with the Identity Provider (IdP) of TH Nürnberg for Single Sign-On (SSO) access. Key issues discussed include handling changes in eduPersonPrincipalName (eppn), account management, and user validation.

## Issues and Solutions

### 1. Handling Changes in eduPersonPrincipalName (eppn)
- **Issue**: The eppn can change due to events like name changes (e.g., marriage).
- **Solution**:
  - The eppn is used as the identifying argument for user accounts.
  - In case of a change, users need to send an email to `hpc-support@fau.de` to update their account before the next login.
  - A manual merging of accounts may be required, using the original email address as a "missing link."

### 2. Account Deletion
- **Issue**: Users need a way to delete their accounts.
- **Solution**:
  - Account deletion can be requested via email to `hpc-support@fau.de`.
  - Accounts that have used computing resources must be retained for billing and tracking purposes.

### 3. Account Validation
- **Issue**: Inactive accounts need to be managed.
- **Solution**:
  - Users must log in every 6 months to validate their accounts.
  - Inactive accounts will be deleted, but those with computing resource usage will be retained.

### 4. User Roles
- **Issue**: Clarification on whether specific user roles are required.
- **Solution**:
  - No specific user roles are required. Both students and employees can use the resources.
  - Authorization is managed within the HPC portal based on project membership and roles assigned by project leaders.

## Additional Information
- **Test Login URL**: `https://portal.hpc.fau.de/`
- **Attributes Required**:
  - `urn:oid:2.5.4.42` - `urn:mace:dir:attribute-def:givenName`: `givenName`
  - `urn:oid:2.5.4.4` - `urn:mace:dir:attribute-def:sn`: `sn`
  - `urn:oid:0.9.2342.19200300.100.1.3` - `urn:mace:dir:attribute-def:mail`: `mail`
  - `urn:oid:1.3.6.1.4.1.5923.1.1.1.6` - `urn:mace:dir:attribute-def:eduPersonPrincipalName`: `eduPersonPrincipalName`
  - `urn:oid:1.3.6.1.4.1.5923.1.1.1.9` - `urn:mace:dir:attribute-def:eduPersonScopedAffiliation`: `eduPersonScopedAffiliation`

## Conclusion
The integration of the HPC portal with the IdP of TH Nürnberg involves managing changes in user identifiers, account validation, and role-based access. The solutions provided ensure that users can maintain access to their accounts and that the system remains secure and compliant with billing and tracking requirements.
---

### 2024022342001712_Migration%20of%20iwhf%20HPC%20accounts%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20mandato.md
# Ticket 2024022342001712

 # HPC Support Ticket: Migration of HPC Accounts to New Portal / SSH Keys Mandatory

## Keywords
- HPC account migration
- SSH keys
- HPC portal
- IdM portal
- Single Sign-On (SSO)
- SSH key types (RSA, ECDSA, ED25519)
- Account validity
- Usage statistics
- ClusterCockpit
- Jupyterhub

## Summary
- **Migration Process**: Existing HPC accounts are being migrated from the IdM portal to a new online HPC portal.
- **Access Method**: Future access to HPC systems will be via SSH keys only.
- **SSH Key Requirements**: Accepted SSH key types are RSA (minimum 4096 bits), ECDSA (512 bits), and ED25519.
- **SSH Key Upload**: Users need to generate SSH key pairs with passphrases and upload the public keys to the HPC portal.
- **Account Validity**: The HPC portal will be the sole source for account validity, decoupled from the IdM portal.
- **Usage Statistics**: Users, PIs, and project managers can view usage statistics in the HPC portal.
- **ClusterCockpit and Jupyterhub**: Access via Single Sign-On links from within the HPC portal.

## Root Cause of the Problem
- Users need to adapt to the new SSH key-based access method and the migration to the new HPC portal.

## Solution
- **SSH Key Generation**: Users should generate SSH key pairs and upload the public keys to the HPC portal.
- **Portal Access**: Users should log in to the new HPC portal using Single Sign-On (SSO) with their IdM credentials.
- **Account Management**: Users should contact their PI or project manager for account validity updates.

## Additional Resources
- [SSH Secure Shell Access Documentation](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/)
- [FAQs](https://hpc.fau.de/faqs/#ID-230)

## Notes
- The migration process is ongoing, and users will receive emails about the expiration of their HPC service in the IdM portal, which can be ignored.
- The new HPC portal provides updated software and hardware for Jupyterhub.

---

This documentation is intended for HPC support employees to assist users during the migration process and to address any issues related to SSH key-based access and the new HPC portal.
---

### 2024050342000559_Login%20Fritz%20nicht%20moeglich.md
# Ticket 2024050342000559

 ```markdown
# HPC-Support Ticket Conversation: Login Fritz nicht möglich

## Subject
Login Fritz nicht möglich

## User Issue
- User cannot log in to Fritz.
- User can access the public NHR@FAU gate but not Fritz.
- User provided `.ssh` config and `ssh -v` output.

## User Configuration
```plaintext
# ssh jump gate for access from outside
Host fritz_gate
    User a103bc11
    HostName cshpc.rrze.fau.de
    ControlMaster auto
    ControlPath ~/.ssh/sockets/%r@%h-%p
    ControlPersist 600

Host fritz
    User a103bc11
    ProxyJump fritz_gate
    #HostName fritz.rrze.fau.de
    HostName fritz.nhr.fau.de
    ControlMaster auto
    ControlPath ~/.ssh/sockets/%r@%h-%p
    ControlPersist 600
```

## HPC Admin Response
- Requested user to test login with the following command:
  ```plaintext
  ssh -J a103bc11@cshpc.rrze.fau.de a103bc11@fritz.nhr.fau.de -i <pfad/zum/key>
  ```
- If successful, the issue is likely in the user's `ssh-config`.
- Recommended configuration can be found [here](https://doc.nhr.fau.de/access/ssh-command-line/).

## Root Cause
- The issue was with the Fritz cluster itself.
- All login nodes were rebooted at the mentioned time.

## Solution
- The reboot was unintentional and affected the login nodes.
- The user was able to log in again after the reboot.

## Additional Information
- The user was not on any mailing list for NHR@FAU updates and requested to be added.
- The user reported issues with the Lustre filesystem, which were not resolved by the reboot.
- The user opened a separate ticket for the Lustre problems.

## Status Updates
- The HPC Admin provided a screenshot from the monitoring system showing unusual job activity on many compute nodes.
- A reboot was triggered for all compute nodes to address potential issues.
- The user was informed about the status updates and the platform for such updates.

## Conclusion
- The login issue was resolved after the reboot.
- The user was advised to check the recommended `ssh-config` for future reference.
- The user was informed about the platform for status updates.
```
---

### 2019013142001987_cshpc%20login.md
# Ticket 2019013142001987

 # HPC Support Ticket: cshpc Login Issue

## Keywords
- Login issue
- cshpc
- SSH
- Password prompt
- Terminal freeze
- woodycap

## Summary
A user reported an issue with logging into the `cshpc` system via SSH. After entering the password, the terminal freezes. The user confirmed that logging into `woodycap` works normally.

## Root Cause
The exact root cause is not specified in the provided conversation. However, it indicates a potential issue with the SSH service or network configuration specific to `cshpc`.

## Solution
No solution is provided in the conversation. Further investigation by the HPC Admins is required to diagnose and resolve the issue.

## General Learnings
- **SSH Login Issues**: Freezing after password entry can indicate problems with the SSH service, network configuration, or system load.
- **System Comparison**: Comparing login behavior across different systems (e.g., `cshpc` vs. `woodycap`) can help isolate the issue.
- **User Communication**: Clear and detailed communication from users, including steps taken and observed behavior, is crucial for diagnosing issues.

## Next Steps
- HPC Admins should check the SSH service logs on `cshpc`.
- Verify network connectivity and configuration.
- Monitor system load and performance during login attempts.
- If necessary, escalate to the 2nd Level Support team for further investigation.
---

### 2024042442003134_ssh%20zugang%20meggie%20-%20muco123h.md
# Ticket 2024042442003134

 # HPC Support Ticket: SSH Access Issue

## Subject
ssh access meggie - muco123h

## Keywords
- SSH
- ProxyJump
- Public Key Authentication
- Key Propagation Delay

## Problem Description
User encountered issues connecting to `meggie.rrze.fau.de` via SSH using ProxyJump through `cshpc.rrze.fau.de`. The user had uploaded a new public SSH key through the HPC portal but was still experiencing authentication failures.

## Debug Output
```
debug1: Authenticating to meggie.rrze.uni-erlangen.de:22 as 'muco123h'
debug1: SSH2_MSG_KEXINIT sent
debug1: SSH2_MSG_KEXINIT received
debug1: kex: algorithm: curve25519-sha256
debug1: kex: host key algorithm: ecdsa-sha2-nistp256
debug1: kex: server->client cipher: chacha20-poly1305@openssh.com MAC: <implicit> compression: none
debug1: kex: client->server cipher: chacha20-poly1305@openssh.com MAC: <implicit> compression: none
debug1: expecting SSH2_MSG_KEX_ECDH_REPLY
debug1: Server host key: ecdsa-sha2-nistp256 SHA256:OidKJlJ3KNbXlJpRUiZNoKp8vephfTbhQepA7Zmn8p4
debug1: Host 'meggie.rrze.uni-erlangen.de' is known and matches the ECDSA host key.
debug1: Found key in /home/maxi/.ssh/known_hosts:12
debug1: resetting send seqnr 3
debug1: rekey out after 134217728 blocks
debug1: SSH2_MSG_NEWKEYS sent
debug1: expecting SSH2_MSG_NEWKEYS
debug1: resetting read seqnr 3
debug1: SSH2_MSG_NEWKEYS received
debug1: rekey in after 134217728 blocks
debug1: Will attempt key: /home/maxi/.ssh/id_ed25519_nhr_fau ED25519 SHA256:KeaxNVkRAlS8a/IIn49p4jVSJGLFTyV2RV7HWnPtvr4 explicit agent
debug1: SSH2_MSG_EXT_INFO received
debug1: kex_input_ext_info:
server-sig-algs=<ssh-ed25519,ssh-rsa,rsa-sha2-256,rsa-sha2-512,ssh-dss,ecdsa-sha2-nistp256,ecdsa-sha2-nistp384,ecdsa-sha2-nistp521>
debug1: SSH2_MSG_SERVICE_ACCEPT received
debug1: Authentications that can continue: publickey,gssapi-keyex,gssapi-with-mic,password
debug1: Next authentication method: publickey
debug1: Offering public key: /home/maxi/.ssh/id_ed25519_nhr_fau ED25519 SHA256:KeaxNVkRAlS8a/IIn49p4jVSJGLFTyV2RV7HWnPtvr4 explicit agent
debug1: Authentications that can continue: publickey,gssapi-keyex,gssapi-with-mic,password
debug1: No more authentication methods to try.
muco123h@meggie.rrze.uni-erlangen.de: Permission denied (publickey,gssapi-keyex,gssapi-with-mic,password).
```

## Root Cause
The issue was due to a delay in the propagation of the new SSH key across all systems. The user had recently uploaded a new key, and it took approximately 2 hours for the key to be available on all systems.

## Solution
Wait for the key propagation to complete. The issue resolved itself after the key was fully propagated.

## Lessons Learned
- Key propagation delays can cause temporary authentication issues.
- Ensure users are aware of potential delays when uploading new SSH keys.
- Verify key availability on all relevant systems before troubleshooting further.

## Support Team Involved
- HPC Admins
- 2nd Level Support Team
---

### 2024031242003819_Unable%20to%20access%20remote.md
# Ticket 2024031242003819

 # HPC Support Ticket: Unable to Access Remote

## Keywords
- SSH
- VS Code
- Connection Timed Out
- Command Line

## Problem Description
- User unable to connect to remote SSH in VS Code.
- Receives "connection timed out" error.

## Troubleshooting Steps
- HPC Admin suggests trying to access from the command line using `ssh -vv tinyx.nhr.fau.de`.

## Root Cause
- Unknown; could be related to network issues, firewall settings, or incorrect configuration in VS Code.

## Solution
- Not yet determined. Further investigation required based on the outcome of the command line test.

## General Learnings
- Always verify if the issue persists when using the command line to rule out configuration problems in VS Code.
- Use `ssh -vv` for verbose output to gather more information about the connection issue.

## Next Steps
- Await user feedback on the command line test.
- If the issue persists, escalate to 2nd Level Support for deeper investigation.
---

### 2024071742000805_Problem%20beim%20Anmelden%20bei%20HPC-portal%20wegen%20meinem%20Praktikum%20%28sp%C3%83%C2%A4ter%20m.md
# Ticket 2024071742000805

 # HPC Support Ticket Conversation Summary

## Subject
Problem beim Anmelden bei HPC-portal wegen meinem Praktikum (später meine Bachelorarbeit) mit Prof. Dr.-Ing Harald Köstler

## Keywords
- SSH Key Generation
- Public Key Upload
- SSH Configuration
- Zoom Meeting Request
- Authentication Issues

## Problem
- User unable to log in to HPC portal due to lack of NVIDIA graphics card on personal PC.
- User needs to configure SSH keys for remote access.
- User facing issues with uploading public key content.
- User unable to authenticate via SSH despite configuration.

## Steps Taken
1. **Initial Request**: User requests help with setting up SSH keys and remote access.
2. **Admin Response**: Admin provides guidance on SSH key generation and upload.
3. **User Issue**: User unable to find and upload public key content.
4. **Admin Guidance**: Admin explains the location of SSH keys and how to copy the public key content.
5. **User Follow-up**: User successfully uploads public key but faces authentication issues.
6. **Admin Troubleshooting**: Admin suggests checking SSH configuration and provides troubleshooting steps.

## Solution
- **SSH Key Generation**: Use `ssh-keygen` to generate SSH keys.
- **Public Key Upload**: Copy the content of the public key file (usually located in `~/.ssh/id_rsa.pub`) and paste it into the portal.
- **SSH Configuration**: Follow the configuration steps provided in the [documentation](https://doc.nhr.fau.de/access/ssh-command-line).
- **Troubleshooting**: If authentication issues persist, check the output of the troubleshooting commands provided in the documentation.

## Notes
- User requested a Zoom meeting for additional assistance.
- Admin suggested contacting the course supervisors for further support.
- The ticket was closed after the user successfully uploaded the public key but faced ongoing authentication issues.

## Next Steps
- If the user continues to face authentication issues, a Zoom meeting or further troubleshooting with the 2nd Level Support team may be necessary.
- Ensure the user has correctly configured their SSH settings and followed all steps in the provided documentation.

## Documentation Links
- [SSH Command Line Access](https://doc.nhr.fau.de/access/ssh-command-line)

## Conclusion
The user was able to generate and upload the public key but faced ongoing authentication issues. Further troubleshooting and potential Zoom meeting support may be required to resolve the issue.
---

### 2023051342000461_Connecting%20to%20the%20fritz%20cluster.md
# Ticket 2023051342000461

 # HPC Support Ticket: Connecting to the Fritz Cluster

## Subject
Connecting to the Fritz Cluster

## User Issue
- User created an SSH key and configured SSH but encountered issues connecting to the Fritz cluster.
- Password prompt when connecting to `cshpc.rrze.fau.de`.
- Connection timeout when connecting to `fritz.nhr.fau.de`.

## Root Cause
- Incorrect `IdentityFile` path in SSH config.
- Incorrect file permissions for SSH config.
- Incorrect file name for SSH config (`config.txt` instead of `config`).
- Possible issues with SSH config syntax and hostname resolution.

## Solution
1. **Correct `IdentityFile` Path**: Ensure the `IdentityFile` in the SSH config points to the private SSH key file, not the directory.
   ```plaintext
   IdentityFile C:\Users\ebner\.ssh\id_ed25519
   ```

2. **Correct File Permissions**: Set the correct permissions for the SSH config file.
   ```plaintext
   chmod 600 ~/.ssh/config
   ```

3. **Rename SSH Config File**: Ensure the SSH config file is named `config`, not `config.txt`.
   ```plaintext
   mv config.txt config
   ```

4. **Simplify SSH Config**: Simplify the hostnames in the SSH config to avoid issues with FQDNs.
   ```plaintext
   Host cshpc
   HostName cshpc.rrze.fau.de
   User b172da12
   ProxyJump cshpc

   Host fritz
   HostName fritz.nhr.fau.de
   User b172da12
   ProxyJump cshpc
   ```

5. **Debug SSH Connection**: Use `ssh -vvv` to debug the SSH connection and identify any issues.
   ```plaintext
   ssh -vvv fritz
   ```

## Additional Information
- **Python and Packages**: User needed to install Python and required packages.
- **Segmentation Fault**: User encountered a segmentation fault in their Python program.
  - **Cause**: Likely due to a code error or dependency issue, possibly in C/C++ code.
  - **Solution**: Use a debugger like `pdb` to identify and fix the issue.

## References
- [Python and Jupyter Documentation](https://hpc.fau.de/systems-services/documentation-instructions/special-applications-and-tips-tricks/python-and-jupyter/)
- [Module System Documentation](https://hpc.fau.de/systems-services/documentation-instructions/environment/)
- [Segmentation Fault Wikipedia](https://de.wikipedia.org/wiki/Schutzverletzung)
- [Python Debugger (pdb)](https://docs.python.org/3/library/pdb.html)

## Conclusion
The user successfully resolved the SSH connection issues by correcting the SSH config file and permissions. They also installed the necessary Python packages and were advised on how to handle segmentation faults in their Python program.
---

### 2024022942001667_Migration%20of%20iww3%20HPC%20accounts%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20mandato.md
# Ticket 2024022942001667

 # HPC Support Ticket: Migration of HPC Accounts to New Portal / SSH Keys Mandatory

## Keywords
- HPC account migration
- HPC portal
- SSH keys
- Single Sign-On (SSO)
- IdM portal
- Account validity
- Usage statistics
- ClusterCockpit
- Jupyterhub

## Summary
The HPC services at FAU are migrating existing HPC accounts to a new online HPC portal. This migration involves several changes, including the mandatory use of SSH keys for accessing HPC systems and the decoupling of the IdM portal from the new HPC portal.

## Key Points to Learn
- **HPC Portal Access**: The new HPC portal can be accessed at [https://portal.hpc.fau.de](https://portal.hpc.fau.de) using Single Sign-On (SSO) with IdM credentials.
- **SSH Keys Mandatory**: From March 11, access to HPC systems will require SSH keys. Accepted key types are RSA (4096 bits), ECDSA (512 bits), and ED25519.
- **SSH Key Upload**: Users must generate SSH key pairs with passphrases and upload the public keys to the HPC portal. It may take up to two hours for all HPC systems to recognize the updated keys.
- **Account Validity**: The new HPC portal will be the sole source for account validity. Users should ignore automatic expiration messages from the IdM portal.
- **Usage Statistics**: The HPC portal will display usage statistics for different HPC systems, which will also be visible to PIs and project managers.
- **ClusterCockpit and Jupyterhub**: Users must use the Single Sign-On links from within the HPC portal to access ClusterCockpit and Jupyterhub.

## Documentation and FAQs
- **SSH Documentation**: [SSH Secure Shell Access to HPC Systems](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/)
- **FAQs**: [HPC FAQs](https://hpc.fau.de/faqs/#ID-230)

## Recommendations for Windows Users
- Use the OpenSSH built into the Windows (Power)Shell or MobaXterm instead of Putty.

## Contact Information
- **HPC Support**: [support-hpc@fau.de](mailto:support-hpc@fau.de)
- **HPC Website**: [https://hpc.fau.de/](https://hpc.fau.de/)

## Root Cause and Solution
- **Root Cause**: Migration of HPC accounts to a new portal and the introduction of mandatory SSH keys for access.
- **Solution**: Users must generate and upload SSH keys to the new HPC portal and use Single Sign-On for accessing various services.
---

### 2024072442001881_AW%3A%20FW%3A%20FW%3A%20introductions%2C%20WF%20project%20data.md
# Ticket 2024072442001881

 # HPC-Support Ticket Conversation Analysis

## Keywords
- SSO-Login
- SSO-Response
- Missing required attributes
- Federated account
- DFN-AAI + EduGAIN
- SSH key
- HPC portal
- Identity provider configuration
- Attribute activation

## General Learnings
- **Federated Login Issues**: Users may encounter issues with federated logins due to missing required attributes in the SSO-Response.
- **Attribute Configuration**: Identity providers need to be configured to submit specific attributes for successful account creation on the HPC portal.
- **Collaboration**: Effective communication and collaboration between different institutions and support teams are crucial for resolving complex issues.
- **Data Transfer**: Planning and coordinating data transfer between institutions require careful consideration of storage quotas and access permissions.

## Root Cause of the Problem
- The user's identity provider (University of Oxford) did not submit the required attributes for successful account creation on the HPC portal.

## Solution
- The user was advised to contact their organization's support address to activate the following attributes for the service provider:
  - `urn:oid:2.5.4.42` - `urn:mace:dir:attribute-def:givenName`
  - `urn:oid:2.5.4.4` - `urn:mace:dir:attribute-def:sn`
  - `urn:oid:0.9.2342.19200300.100.1.3` - `urn:mace:dir:attribute-def:mail`
  - `urn:oid:1.3.6.1.4.1.5923.1.1.1.6` - `urn:mace:dir:attribute-def:eduPersonPrincipalName`
  - `urn:oid:1.3.6.1.4.1.5923.1.1.1.9` - `urn:mace:dir:attribute-def:eduPersonScopedAffiliation`

## Actions Taken
- The user was CC'd to the relevant contact address at their institution and the HPC support team to facilitate the configuration of the identity provider.
- The user was advised to upload their SSH key to the HPC portal once the attribute issue is resolved.

## Next Steps
- The user should follow up with their institution's support team to ensure the required attributes are activated.
- Once the attributes are activated, the user should attempt to log in again and upload their SSH key to the HPC portal.
- If the issue persists, the user should contact HPC support for further assistance.

## Documentation for Support Employees
- **Federated Login Troubleshooting**: When users encounter issues with federated logins, check if the required attributes are being submitted by the identity provider.
- **Attribute Configuration**: Provide users with the list of required attributes and guide them to contact their institution's support team for configuration.
- **SSH Key Upload**: Remind users to upload their SSH key to the HPC portal after resolving the attribute issue.
- **Collaboration**: Facilitate communication between the user's institution and the HPC support team to ensure a smooth resolution of the issue.
---

### 2024022942003441_Migration%20of%20ilev%20HPC%20accounts%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20mandato.md
# Ticket 2024022942003441

 # HPC Support Ticket Conversation Summary

## Keywords
- Migration
- HPC portal
- SSH keys
- Single Sign-On (SSO)
- IdM portal
- Account validity
- Usage statistics
- ClusterCockpit
- Jupyterhub

## General Learnings
- **Migration to New HPC Portal**: The existing HPC accounts are being migrated to a new online HPC portal.
- **SSH Keys Mandatory**: Starting March 11th, access to HPC systems will require SSH keys. Accepted types are RSA (4096 bits), ECDSA (512 bits), and ED25519.
- **SSH Key Generation**: Users need to generate SSH key pairs with passphrases and upload the public key to the HPC portal.
- **Account Validity**: The HPC portal will be the sole source for account validity. Users should contact their PI or project manager for extensions or updates.
- **Usage Statistics**: The HPC portal will display usage statistics, which are also visible to PIs and project managers.
- **Single Sign-On (SSO)**: Users should use SSO links from the HPC portal for ClusterCockpit and Jupyterhub.
- **Windows Users**: Recommended to use OpenSSH built into Windows (Power)Shell or MobaXterm instead of Putty.

## Root Cause of the Problem
- **Migration Process**: Users need to adapt to the new HPC portal and SSH key requirements.
- **Account Validity**: Users need to understand the new process for extending or updating account validity.

## Solution
- **SSH Key Generation**: Follow the documentation and FAQs provided to generate and upload SSH keys.
- **Account Validity**: Contact the PI or project manager for any updates or extensions to the HPC account.

## Additional Notes
- **IdM Portal Expiration**: Users can ignore automatic messages about HPC service expiration in the IdM portal.
- **ClusterCockpit and Jupyterhub**: Use SSO links from the HPC portal for accessing these services.

For further assistance, refer to the provided documentation and FAQs or contact the HPC support team.
---

### 2023030142003574_Umstellung%20der%20HPC-Accounts%20der%20HS-Coburg%20am%20RRZE%20_%20NHR%40FAU%20-%20corz041h.md
# Ticket 2023030142003574

 ```markdown
# HPC-Support Ticket Conversation: Account Transition to Electronic Portal

## Keywords
- HPC Accounts
- Electronic Portal
- DFN-AAI/eduGAIN
- SSH-PublicKeys
- SSH-Key Access
- Hochschul-Emailadresse
- HPC-Portal
- Windows PowerShell
- Windows Subsystem for Linux
- mobaXterm
- OpenSSH
- Putty
- JumpHost-Feature
- Account Deactivation
- Data Deletion

## Summary
The HPC accounts for HS-Coburg at RRZE / NHR@FAU are transitioning from a paper-based system to a new electronic HPC portal. Users must log in via DFN-AAI/eduGAIN to continue using their accounts. SSH-PublicKeys will be required for access starting at the end of March.

## Root Cause
- Certificate expiration.
- Transition to a new electronic portal for account management.

## Solution
1. **Login to HPC Portal**: Users must log in to the HPC portal using DFN-AAI/eduGAIN.
2. **Link Account**: Existing HPC accounts will be linked to the user's identity in the portal.
3. **Upload SSH-PublicKeys**: Users can upload SSH-PublicKeys in the "User / Benutzer" tab.
4. **SSH-Key Synchronization**: SSH-PublicKeys will be synchronized to HPC systems within two hours.
5. **Email Update**: Future HPC emails will be sent to the user's Hochschul-Emailadresse.

## Additional Information
- **SSH Access**: Starting at the end of March, access will only be possible via SSH-Key, not password.
- **Windows Users**: Recommended to use Windows PowerShell, Windows Subsystem for Linux, or mobaXterm, which include OpenSSH.
- **Putty**: Not recommended due to different SSH-Key format and lack of JumpHost-Feature support.
- **Account Deactivation**: Accounts not linked by the end of March will be deactivated, and data will be deleted after three months.

## References
- [HPC Portal Usage](https://hpc.fau.de/systems-services/documentation-instructions/getting-started/nhrfau-hpc-portal-usage/)
- [SSH Access Documentation](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/)
- [FAQ on SSH Access](https://hpc.fau.de/faqs/#innerID-13183)
- [mobaXterm](https://mobaxterm.mobatek.net/)

## Contacts for Further Assistance
- HS-Coburg Rechenzentrum
- Fakultät Wirtschaftswissenschaften der HS-Coburg
- HPC Admins: support-hpc@fau.de
```
---

### 2024030842002131_HPC%20account%20extension.md
# Ticket 2024030842002131

 # HPC Account Extension Request

## Keywords
- HPC account extension
- HPC portal
- SSH keys
- Account migration
- Project manager
- Single Sign-On (SSO)
- IdM portal

## Problem
- User believed their HPC account was expired and requested an extension.

## Root Cause
- User was unaware of the account migration to the new HPC portal and the updated expiration date.

## Solution
- Informed the user that their account is still valid and has been migrated to the new HPC portal.
- Provided instructions on how to access and manage the account through the HPC portal.
- Advised the user that the project manager can extend the account via the HPC portal.

## General Learnings
- Account migrations may cause confusion regarding account status and expiration dates.
- Communicating migration details and new procedures to users is crucial.
- Project managers are responsible for extending accounts in the new HPC portal.
- SSH keys are mandatory for accessing HPC systems post-migration.

## Actions Taken
- Re-sent the migration email with detailed instructions.
- Directed the user to contact their project manager for account extension.

## Follow-up
- Ensure users are aware of and understand the migration process.
- Provide clear documentation and support for SSH key generation and usage.
---

### 2024020542002853_Account%20archived.md
# Ticket 2024020542002853

 # HPC Support Ticket: Account Archived

## Keywords
- Account reactivation
- SSH key update
- Thesis supervisor
- Account extension
- New HPC account application

## Problem
- User's HPC account was archived.
- User missed adding SSH key initially but updated it later.
- User is no longer working with the previous supervisor and is working on a different thesis.

## Root Cause
- Account archived due to missing SSH key.
- Change in thesis supervisor leading to uncertainty in account management.

## Solution
- **Account Reactivation**: User was advised to contact the previous supervisor for reactivation.
- **Account Extension**: If the user has changed chairs for the new thesis, a new HPC account application is required. The process depends on the new chair's procedures (via HPC portal or paper form).
- **Form**: User was provided with the link to the HPC application form ["HPC-Antrag.pdf"](https://www.rrze.fau.de/files/2017/06/HPC-Antrag.pdf).

## General Learnings
- Updating SSH keys is crucial for keeping accounts active.
- Change in thesis supervisor or chair may require a new HPC account application.
- Account extension processes vary by chair, and users should consult their supervisor or the RRZE contact person.

## Related Roles
- **HPC Admins**: Provide initial support and guidance.
- **2nd Level Support Team**: May be involved in account management and reactivation processes.
- **Thesis Supervisor/RRZE Contact Person**: Responsible for account extension and management based on the user's affiliation.
---

### 2024010542000624_Not%20able%20to%20login%20to%20HPC%20-%20iwfa047h.md
# Ticket 2024010542000624

 ```markdown
# HPC Support Ticket: Not Able to Login to HPC

## Subject
Not able to login to HPC

## User Issue
- User unable to login to HPC via VSCode; login works via command prompt.
- Issue started in the afternoon.
- Username: iwfa047h

## User Logs
- Authenticated to HPC server.
- Debug logs indicate successful authentication and session setup.
- No apparent errors in the SSH logs.

## HPC Admin Response
- Limited support due to holiday season.
- No recent changes to system services.
- Issue likely on user's side (different/new key, waiting for password, etc.).
- HPC Admin tested connection via VSCode (VSCodium) with no issues.
- Provided link to VSCode troubleshooting page for remote connections.

## Troubleshooting Steps
- User should check VSCode troubleshooting page for remote connections.
- User should provide a status update if the issue persists.

## Root Cause
- Likely issue with VSCode configuration or user-side settings.

## Solution
- User should follow the VSCode troubleshooting guide to resolve the issue.
- If the problem persists, further investigation will be needed when full support is available.

## Keywords
- VSCode, SSH, login issue, troubleshooting, remote connection
```
---

### 2024111942002864_SSH%20key.md
# Ticket 2024111942002864

 ```markdown
# HPC Support Ticket: SSH Key Issue

## Keywords
- SSH key
- Permission denied
- SSH config file
- Debugging SSH
- HPC account access

## Problem Description
- User experiencing "Permission denied" error when trying to access HPC account.
- User created an SSH key using `ssh-keygen -t rsa -b 4096 -f ~/.ssh/id_zl`.
- Public key submitted to the portal, but access still denied.

## Root Cause
- SSH config file not properly configured.

## Solution
- Configure the SSH config file according to the instructions provided in the link: [Template for Connecting to HPC Systems](https://doc.nhr.fau.de/access/ssh-command-line/#template-for-connecting-to-hpc-systems).

## Steps Taken
1. HPC Admin suggested configuring the SSH config file.
2. User followed the instructions and successfully accessed the HPC system.

## Additional Information
- HPC Admin requested details about the cluster and operating system.
- HPC Admin suggested using the SSH debugging option (`ssh -vv ...`) for further troubleshooting if needed.

## Conclusion
- Proper configuration of the SSH config file resolved the "Permission denied" error.
```
---

### 2023041142002269_HPC-Portal%3A%20error%20message%20bei%20Hinzuf%C3%83%C2%BCgen%20von%20Einladungen.md
# Ticket 2023041142002269

 ```markdown
# HPC-Portal: Error Message When Adding Invitations

## Keywords
- HPC-Portal
- Invitations
- Error Message
- Backend Issue
- Browser Compatibility
- Fix Deployed

## Problem Description
- **User Issue:** Error messages when adding invitations to a project in the HPC-Portal.
  - Error 1: `Error - No such property: email for class: java.lang.String Possible solutions: empty (Status: 500) for ID ''`
  - Error 2: `Error - n.payloads is undefined (Status: ) for ID ''`
- **Browsers Tested:** Firefox 111, Chromium

## Root Cause
- The issue was identified as a backend code problem, not related to the user's browser or its version.

## Solution
- **HPC Admin:** Identified and fixed the backend code issue.
- **Status:** The fix was deployed, and both single and bulk invitations are now functioning as expected.

## Lessons Learned
- Backend issues can manifest as browser-specific errors, but the root cause may lie in the server-side code.
- Regular updates and monitoring of backend code are essential to maintain the functionality of the HPC-Portal.
- Effective communication between users and HPC Admins helps in quickly identifying and resolving issues.
```
---

### 2023060542000304_Migration%20of%20bctc%20HPC%20accounts%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20mandato.md
# Ticket 2023060542000304

 # HPC Support Ticket: Migration of HPC Accounts to New Portal / SSH Keys Mandatory

## Keywords
- HPC account migration
- SSH keys
- HPC portal
- Single Sign-On (SSO)
- IdM portal
- Passphrase
- RSA, ECDSA, ED25519
- Windows users
- OpenSSH, MobaXterm
- Account validity
- Usage statistics
- ClusterCockpit
- Jupyterhub

## Summary
The HPC services at FAU are migrating existing HPC accounts to a new online HPC portal. Users need to generate and upload SSH keys for future access.

## Key Points
- **Migration Process**: Existing HPC accounts are being migrated to a new HPC portal accessible via SSO using IdM credentials.
- **SSH Keys**: Access to HPC systems will require SSH keys by mid-June. Accepted key types are RSA (4096 bits), ECDSA (512 bits), and ED25519.
- **SSH Key Upload**: Users must generate SSH key pairs with passphrases and upload the public keys to the HPC portal.
- **Windows Users**: Recommended tools are OpenSSH built into Windows (Power)Shell or MobaXterm.
- **Account Validity**: The HPC portal will be the sole source for account validity. Users should contact their PI or project manager for updates.
- **Usage Statistics**: PIs and project managers can view usage statistics in the HPC portal.
- **ClusterCockpit and Jupyterhub**: Users must use SSO links from the HPC portal to access these services.

## Documentation and FAQs
- [SSH Secure Shell Access Documentation](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/)
- [FAQs](https://hpc.fau.de/faqs/#ID-230)

## Solution
1. **Login to HPC Portal**: Use SSO with IdM credentials at [HPC Portal](https://portal.hpc.fau.de).
2. **Generate SSH Keys**: Create SSH key pairs with passphrases using accepted key types.
3. **Upload Public Keys**: Upload the public keys to the HPC portal.
4. **Access Services**: Use SSO links from the HPC portal for ClusterCockpit and Jupyterhub.

## Notes
- The migration process may cause automatic expiration messages from the IdM portal, which can be ignored.
- The HPC portal and IdM portal are decoupled, so account validity updates must be done through the PI or project manager.
---

### 2024022842002122_Migration%20of%20iwi1%20HPC%20accounts%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20mandato.md
# Ticket 2024022842002122

 # HPC Support Ticket: Migration of HPC Accounts to New Portal / SSH Keys Mandatory

## Keywords
- HPC account migration
- SSH keys
- HPC portal
- Single Sign-On (SSO)
- IdM portal
- ClusterCockpit
- Jupyterhub

## Summary
The HPC services at FAU are migrating existing HPC accounts to a new online HPC portal. This migration involves several changes, including the mandatory use of SSH keys for accessing HPC systems.

## Key Points to Learn
- **New HPC Portal**: The new portal can be accessed at [https://portal.hpc.fau.de](https://portal.hpc.fau.de) using SSO with IdM credentials.
- **SSH Keys Mandatory**: Starting from 15.03.2024, access to HPC systems will require SSH keys. Accepted key types are RSA (4096 bits), ECDSA (512 bits), and ED25519.
- **SSH Key Upload**: Users must generate SSH key pairs with passphrases and upload the public keys to the HPC portal. It may take up to two hours for all HPC systems to recognize the updated keys.
- **IdM Portal Expiration**: Users will receive emails about their HPC service expiring in the IdM portal, but these can be ignored as the HPC portal will be the sole source for account validity.
- **Account Management**: Account validity updates and new account requests should be directed to the project's PI or manager, not RRZE.
- **Usage Statistics**: The HPC portal displays usage statistics for different HPC systems, which are also visible to PIs and project managers.
- **ClusterCockpit and Jupyterhub**: Access to these services should be done through the SSO link in the HPC portal, not directly with username and password.

## Recommendations
- **SSH Key Generation**: Users unfamiliar with SSH keys should refer to the documentation and FAQs provided.
- **Windows Users**: Recommended to use OpenSSH built into Windows (Power)Shell or MobaXterm instead of Putty.

## Root Cause of the Problem
- The migration process requires users to adapt to new authentication methods and portal usage.

## Solution
- Follow the instructions provided in the email to migrate accounts, generate and upload SSH keys, and use the new HPC portal for all account-related activities.

---

This report provides a concise overview of the migration process and the necessary actions for users to adapt to the new HPC portal and authentication methods.
---

### 2024102342001117_Please%20Help%20%5Bmrvl121v%5D.md
# Ticket 2024102342001117

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Keywords
- SSH public keys
- Format ERROR
- HPC-Portal
- .pub file
- Documentation

## Summary
A user encountered a "Format ERROR" while trying to add SSH public keys to the HPC-Portal. The user followed the provided documentation but was unable to resolve the issue.

## Root Cause
The user was having trouble with the format of the SSH public key, leading to a "Format ERROR" when attempting to upload it to the HPC-Portal.

## Solution
The HPC Admin suggested that the user should ensure they are uploading the content of their .pub file. The admin also advised the user to contact support using their @fau.de email address.

## General Learnings
- Ensure that the content of the .pub file is correctly formatted and uploaded.
- Use the email address registered with the HPC-Portal for support communications.
- Refer to the official documentation for guidance on adding SSH public keys.

## Next Steps
- Verify the format of the SSH public key.
- Contact HPC support using the registered email address for further assistance.
```
---

### 2024030142000995_Migration%20of%20iw30001h%20HPC%20account%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20mand.md
# Ticket 2024030142000995

 # HPC Support Ticket: Migration to New HPC Portal and SSH Key Requirement

## Keywords
- HPC account migration
- SSH keys
- HPC portal
- Single Sign-On (SSO)
- IdM portal
- SSH key types (RSA, ECDSA, ED25519)
- Usage statistics
- ClusterCockpit
- Jupyterhub

## Summary
The HPC Admins informed users about the migration of their HPC accounts to a new HPC portal, which requires SSH keys for access. The IdM portal will no longer manage HPC accounts, and users must update their account validity through their PI or project manager.

## Key Points to Learn
- **Migration to New HPC Portal**: The HPC services are transitioning to a new online portal accessible via SSO using IdM credentials.
- **SSH Keys Mandatory**: From March 15th, access to HPC systems will require SSH keys. Accepted types are RSA (4096 bits), ECDSA (512 bits), and ED25519.
- **SSH Key Upload**: Users must generate SSH key pairs with passphrases and upload the public key to the HPC portal. It may take up to two hours for updates to propagate.
- **Account Validity**: The new HPC portal is the sole authority for account validity. Users should contact their PI or project manager to update account validity.
- **Usage Statistics**: The HPC portal displays usage statistics, which are also visible to PIs and project managers.
- **ClusterCockpit and Jupyterhub**: Users must use SSO links from the HPC portal to access these services.

## Common Issues and Solutions
- **SSH Key Generation**: Users unfamiliar with SSH keys should refer to the provided documentation and FAQs.
- **Account Expiration Notices**: Users can ignore automatic messages about account expiration from the IdM portal.

## References
- [HPC Portal](https://portal.hpc.fau.de)
- [SSH Documentation](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/)
- [FAQs](https://hpc.fau.de/faqs/#ID-230)

## Next Steps for Users
1. Log in to the new HPC portal using SSO.
2. Generate and upload SSH keys.
3. Contact PI or project manager for account validity updates.
4. Use SSO links for ClusterCockpit and Jupyterhub.
---

### 2023030142000808_Error%20when%20uploading%20SSH%20key%20to%20HPC%20portal.md
# Ticket 2023030142000808

 # HPC Support Ticket: Error when uploading SSH key to HPC portal

## Keywords
- SSH key upload
- HPC portal
- Error message
- Unclosed counted closure
- Status 500
- RSA key
- Certificate expiration

## Problem Description
User encounters an error when attempting to upload an SSH key to the HPC portal. The error message indicates an "Unclosed counted closure" near a specific index, with a Status 500.

## Root Cause
The error is likely due to an expired certificate affecting the SSH key upload process.

## Solution
- **HPC Admin** confirmed that the issue was fixed, at least for RSA keys, after successful testing.
- The fix was implemented by another **HPC Admin**.

## General Learnings
- Certificate expiration can cause issues with SSH key uploads.
- Regular testing and updates are necessary to ensure smooth operation of the HPC portal.
- Collaboration among **HPC Admins** is crucial for resolving technical issues.

## Next Steps for Similar Issues
- Check for any recent certificate updates or expirations.
- Test the SSH key upload process with different key types (e.g., RSA, ECDSA).
- Consult with other **HPC Admins** or the **2nd Level Support team** for further assistance.
---

### 2024021442000605_Migration%20of%20capn%20HPC%20accounts%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20mandato.md
# Ticket 2024021442000605

 # HPC Support Ticket Summary

## Subject
Migration of HPC accounts to new HPC portal / SSH keys become mandatory

## Keywords
- HPC account migration
- SSH keys
- HPC portal
- Single Sign-On (SSO)
- IdM portal
- ClusterCockpit
- Jupyterhub

## Summary
- **Migration Process**: HPC accounts are being migrated from the IdM portal to a new online HPC portal.
- **Access**: The new HPC portal can be accessed via SSO using IdM credentials.
- **SSH Keys**: From 29.02.2024, access to HPC systems will require SSH keys. Accepted types are RSA (4096 bits), ECDSA (512 bits), and ED25519.
- **Documentation**: Users unfamiliar with SSH keys should refer to the provided documentation and FAQs.
- **Expiration Notices**: Users may receive emails about HPC service expiration from the IdM portal, which can be ignored.
- **Account Validity**: The HPC portal will be the sole source for account validity. Users should contact their PI or project manager for updates.
- **Usage Statistics**: Usage statistics will be visible to PIs and project managers.
- **ClusterCockpit and Jupyterhub**: Users should use SSO links from the HPC portal for these services.

## Root Cause
- Migration of HPC accounts to a new portal and the introduction of mandatory SSH keys for access.

## Solution
- Users should generate and upload SSH keys to the new HPC portal.
- Users should use SSO links for accessing ClusterCockpit and Jupyterhub.
- For account validity updates, users should contact their PI or project manager.

## Additional Notes
- The HPC portal and IdM portal are decoupled.
- Recommended tools for Windows users include OpenSSH built into Windows (Power)Shell or MobaXterm.

---

This summary provides a concise overview of the migration process, key changes, and necessary actions for users and support employees.
---

### 2024111942003176_Re%3A%20New%20invitation%20for%20%22SelPredMultiMod%20-%20Analysis%20of%20Selective%20Prediction%20o.md
# Ticket 2024111942003176

 ```markdown
# HPC Support Ticket Analysis

## Subject
Re: New invitation for "SelPredMultiMod - Analysis of Selective Prediction on Multimodal Models" waiting at portal.hpc.fau.de

## Keywords
- Invitation
- Email
- Project
- Portal
- User Error

## Summary
The user mistakenly sent an invitation email to the wrong address. Shortly after, the user realized the error and resent the invitation to the correct project-responsible email address.

## Root Cause
User error in sending the invitation to the wrong email address.

## Solution
The user corrected the error by resending the invitation to the correct email address.

## Lessons Learned
- Always double-check email addresses before sending important communications.
- Quickly correct any errors by resending the information to the correct recipient.
```
---

### 2024102142004574_Issue%20by%20connecting%20to%20cluster%20from%20PyCharm.md
# Ticket 2024102142004574

 ```markdown
# Issue: Connecting to Cluster from PyCharm

## Keywords
- PyCharm
- SSH Configuration
- ProxyJump
- Public Key Authentication
- HPC Cluster

## Problem Description
The user is attempting to connect to the HPC cluster from PyCharm using an SSH configuration file. The configuration includes settings for a front node and a compute node with ProxyJump. Despite setting up the configuration and mapping paths in PyCharm, the connection does not work.

## SSH Configuration
```plaintext
Host frontnode
  HostName tinyx.nhr.fau.de
  Port 22
  User iwi5227h
  IdentityFile ~/.ssh/id_rsa
  IdentitiesOnly yes
  PasswordAuthentication no
  PreferredAuthentications publickey

Host node01
  HostName tg096
  User iwi5227h
  IdentityFile ~/.ssh/id_rsa
  ProxyJump frontnode
```

## Root Cause
The exact root cause of the problem is not clear from the conversation. However, it could be related to the SSH configuration or PyCharm settings.

## Solution
The HPC Admin stated that they do not provide support for PyCharm and advised the user to seek help from their research chair.

## General Learnings
- HPC Admins do not provide support for third-party software like PyCharm.
- Users should seek assistance from their research chair or colleagues for issues related to specific software.
- Proper SSH configuration is crucial for connecting to HPC clusters.
- Ensure that all paths and settings in PyCharm are correctly mapped and configured.
```
---

### 2024050742003165_ssh%20key%20f%C3%83%C2%BCr%20zweiten%20Account.md
# Ticket 2024050742003165

 # HPC Support Ticket: SSH Key for Second Account

## Keywords
- SSH Key
- Multiple Accounts
- Security
- Data Management

## Summary
A user inquired about using the same SSH key for two different accounts: a personal account and a group data management account.

## Root Cause
The user wanted to know if it is possible to use the same SSH key for multiple accounts.

## Solution
- **Technical Feasibility**: It is technically possible to use the same SSH key for multiple accounts.
- **Security Recommendation**: For security reasons, especially if the second account is shared among multiple users, it is advisable to use a separate SSH key.

## General Learning
- **SSH Key Management**: Understanding the technical feasibility and security implications of using the same SSH key for multiple accounts.
- **Best Practices**: It is generally recommended to use separate SSH keys for different accounts, especially when accounts are shared among multiple users, to enhance security.

## Action Taken
The HPC Admin advised the user to use a separate SSH key for the group data management account due to security concerns.

## Conclusion
This ticket highlights the importance of considering both technical feasibility and security best practices when managing SSH keys for multiple accounts.
---

### 2023030142003403_Umstellung%20der%20HPC-Accounts%20der%20HS-Coburg%20am%20RRZE%20_%20NHR%40FAU%20-%20corz04.md
# Ticket 2023030142003403

 # HPC-Support Ticket Conversation Summary

## Subject
Umstellung der HPC-Accounts der HS-Coburg am RRZE / NHR@FAU - corz04

## Keywords
- HPC-Accounts
- HS-Coburg
- RRZE / NHR@FAU
- DFN-AAI/eduGAIN
- HPC-Portal
- SSH-PublicKeys
- SSH-Key
- Passwort
- Windows PowerShell
- Windows Subsystem für Linux
- mobaXtern
- OpenSSH
- Putty
- JumpHost-Feature
- Deaktivierung
- Datenlöschung

## Problem
- Certificate has expired.
- Transition from paper-based system to electronic HPC-Portal.

## Solution
- Users need to log in to the HPC-Portal using DFN-AAI/eduGAIN.
- Existing HPC-Accounts will be linked to the user's identity in the HPC-Portal.
- Users must upload SSH-PublicKeys via the "User / Benutzer" tab in the HPC-Portal.
- SSH-PublicKeys will be synchronized to the HPC-Systems within two hours.
- Access to HPC-Systems will be restricted to SSH-Key only by the end of March.
- Accounts not linked by the end of March will be deactivated and data deleted after three months.

## Additional Information
- HPC-Portal usage instructions: [HPC-Portal Usage](https://hpc.fau.de/systems-services/documentation-instructions/getting-started/nhrfau-hpc-portal-usage/)
- SSH and SSH-Keys information: [SSH Access](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/)
- FAQ for SSH access issues: [SSH FAQ](https://hpc.fau.de/faqs/#innerID-13183)
- Recommended tools for Windows users: Windows PowerShell, Windows Subsystem für Linux, mobaXtern.

## Contacts for Further Assistance
- Rechenzentrum der HS-Coburg
- Fakultät Wirtschaftswissenschaften der HS-Coburg

## Important Dates
- End of March: Deadline for account linking and transition to SSH-Key access.
- Three months after deactivation: Data deletion for unlinked accounts.

## Notes
- Putty uses a different format for SSH-Keys and does not support the JumpHost-Feature.
- OpenSSH is recommended for SSH access.
---

### 2023072642002682_URGENT%20%7C%20Not%20able%20to%20add%20public%20ssh-key%20%7C%20portal.hpc.fau.de.md
# Ticket 2023072642002682

 # HPC Support Ticket: URGENT | Not able to add public ssh-key | portal.hpc.fau.de

## Keywords
- SSH Key
- Account Reactivation
- Database Error
- HPC Portal
- Bug Report

## Issue Description
- User unable to add public SSH keys to their account after reactivation.
- Error message displayed on the HPC portal.

## Root Cause
- Problem with the account entry in the database.

## Solution
- HPC Admin manually fixed the account entry in the database.
- User should now be able to upload an SSH key without issues.

## Additional Notes
- The error indicates a potential bug in the HPC portal code causing the database error.
- User was asked to report back if the SSH key upload worked as intended.

## Follow-up Actions
- Monitor for similar issues to identify and fix the underlying bug in the HPC portal code.
- Ensure proper communication with the user to confirm the resolution of the issue.
---

### 2025021242002632_Trouble%20connecting%20via%20ssh.md
# Ticket 2025021242002632

 # HPC Support Ticket: Trouble Connecting via SSH

## Keywords
- SSH
- Permission denied
- Publickey
- Password
- SSH Config
- Key Distribution

## Problem Description
The user is unable to connect to the HPC network via SSH despite following the setup instructions. The user receives a "Permission denied (publickey,password)" error message.

## Root Cause
- The user's SSH key was recently uploaded and not yet distributed to all systems.
- The SSH key distribution process can take up to 2 hours.

## Debug Output Analysis
- The SSH debug output shows that the user's public key is being offered but not accepted.
- The authentication methods tried were publickey and password, both of which failed.

## Solution
- Wait for up to 2 hours for the SSH key to be distributed to all systems.
- If the issue persists after 2 hours, contact HPC support with the updated debug output.

## Additional Notes
- The user was reminded to use their FAU email address for contacting HPC support.
- The HPC Admin provided a link to the HPC portal for more information on key distribution times.

## Follow-up
- If the user continues to experience issues, further investigation into the SSH key and configuration may be necessary.

## Related Documentation
- [SSH Command Line Instructions](https://doc.nhr.fau.de/access/ssh-command-line/)
- [HPC Portal - User Tab](https://doc.nhr.fau.de/hpc-portal/#the-user-tab)
---

### 2024090242001418_Access%20to%20HPC%20cluster%20denied%20-%20b231cb10%20-%20SSH%20agent%20refused%20operation.md
# Ticket 2024090242001418

 # HPC Support Ticket: Access to HPC Cluster Denied

## Subject
Access to HPC cluster denied - b231cb10 - SSH agent refused operation

## User Issue
- User is having trouble accessing the HPC cluster via SSH after updating their public SSH key.
- The user forgot the passphrase for the SSH key.
- Error message: `sign_and_send_pubkey: signing failed for ED25519 "/home/mscherer/.ssh/id_ed25519_nhr_fau" from agent: agent refused operation`
- Permission denied (publickey).
- Connection closed by remote host.

## Root Cause
- The SSH agent is refusing to provide the key, possibly due to an incomplete passphrase entry process or the passphrase dialog not being shown.

## Troubleshooting Steps
1. **Verify SSH Key and Config File**
   - Ensure the SSH key is correctly configured and uploaded to the HPC portal.
   - Check the `.ssh/config` file for correct sections for both `csnhr` and `alex`.

2. **Check SSH Agent**
   - Run `ssh-add -l` to check if the SSH agent has any identities loaded.
   - If there is no output, the SSH agent is not running or has no identities loaded.

3. **Debug SSH Connection**
   - Run `ssh -vv ...` to get detailed debugging information about the SSH connection.
   - Example output provided by the user shows the SSH agent refusing the operation.

4. **Enforce Passphrase Entry**
   - Run `ssh-add -t <time> <ssh-private-key>` to set a maximum lifetime for the SSH private key and enforce passphrase entry.
   - If the above command does not work, try `killall ssh-agent` to kill all SSH agent processes.
   - Run `ssh-add -D` to delete all identities recorded by the agent.

5. **Reboot the Computer**
   - If the above steps do not resolve the issue, rebooting the computer may help.

## Solution
- The user ran `ssh-add -t <time> <ssh-private-key>` and was prompted for the passphrase, which resolved the issue.
- Subsequent connection to the server was granted.

## Additional Notes
- The user was using a Linux machine and had copied/pasted the template for the `.ssh/config` file.
- The HPC Admin verified that the key was correctly distributed to the `csnhr` and `alex` systems.
- The user was available for a Zoom call if further assistance was needed.

## Conclusion
The issue was resolved by enforcing the passphrase entry using the `ssh-add` command. This documentation can be used to solve similar errors in the future.
---

### 2024052042000286_Cluster%20name%20for%20hpc%20account.md
# Ticket 2024052042000286

 # HPC Support Ticket: Cluster Name for HPC Account

## Keywords
- HPC account
- SSH connection
- VS Code
- Cluster name
- NHR FAU

## Problem
- User received an HPC account for their master thesis.
- User needs the cluster name to connect to VS Code via SSH.
- User tried `iwi1102h@tinyx.nhr.fau.de` but it didn't work.

## Solution
- HPC Admin provided guidelines for SSH access and VS Code configuration.
- User was directed to the following documentation links:
  - [SSH Access Guidelines](https://doc.nhr.fau.de/access/ssh-command-line/)
  - [VS Code Configuration](https://doc.nhr.fau.de/access/ssh-vscode/)
  - [Cluster Overview](https://doc.nhr.fau.de/clusters/overview/)

## General Learnings
- Users need to follow specific guidelines for SSH access and VS Code configuration.
- Documentation links are essential for users to set up their environment correctly.
- Cluster names and configurations are crucial for successful SSH connections.

## Root Cause
- User did not have the correct cluster name for their HPC account.

## Resolution
- User was provided with documentation links to configure SSH and VS Code correctly.
- User should follow the guidelines to determine the correct cluster name and set up the SSH config file.
---

### 2024022242002713_Migration%20of%20iwi5%20HPC%20accounts%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20mandato.md
# Ticket 2024022242002713

 # HPC Support Ticket Conversation Summary

## Subject
Migration of iwi5 HPC accounts to new HPC portal / SSH keys become mandatory

## Keywords
- HPC account migration
- SSH keys
- HPC portal
- Single Sign-On (SSO)
- IdM portal
- SSH key types (RSA, ECDSA, ED25519)
- Usage statistics
- ClusterCockpit
- Jupyterhub

## What Can Be Learned
- **Migration Process**: The migration of HPC accounts from the IdM portal to a new HPC portal is underway.
- **SSH Keys**: Access to HPC systems will require SSH keys only. Accepted types are RSA (4096 bits), ECDSA (512 bits), and ED25519.
- **SSH Key Upload**: Users need to generate SSH key pairs with passphrases and upload the public keys to the HPC portal.
- **Portal Access**: The new HPC portal can be accessed via SSO using IdM credentials.
- **Account Validity**: The HPC portal will be the sole source for account validity, decoupled from the IdM portal.
- **Usage Statistics**: Users and their PIs/project managers can view usage statistics in the HPC portal.
- **ClusterCockpit and Jupyterhub**: Access to these services will be through SSO links within the HPC portal.

## Root Cause of the Problem
- The migration process requires users to adapt to new authentication methods and update their SSH keys.

## Solution
- Users should generate and upload SSH keys to the new HPC portal.
- Access the HPC portal via SSO using IdM credentials.
- Use SSO links for ClusterCockpit and Jupyterhub.

## Additional Resources
- [SSH Documentation](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/)
- [FAQs](https://doc.nhr.fau.de/faq/#ssh)
---

### 2023050842003307_Connecting%20via%20SSH%20in%20Vscode.md
# Ticket 2023050842003307

 ```markdown
# HPC Support Ticket: Connecting via SSH in VSCode

## Subject
Connecting via SSH in VSCode

## User Issue
- User's account was created via NHR Portal and can only be accessed via SSH key.
- User previously used PuTTY/WinSCP for SSH connections.
- User wants to connect via VSCode Remote SSH plugin for more flexibility.

## HPC Admin Response
- HPC Admin provided a link to the VSCode documentation for setting up SSH connections.
- User successfully set up the connection and provided an instruction file for future reference.

## Keywords
- SSH
- VSCode
- Remote SSH Plugin
- NHR Portal
- PuTTY
- WinSCP

## Solution
- Follow the VSCode documentation for setting up SSH connections: [VSCode SSH Tutorial](https://code.visualstudio.com/docs/remote/ssh-tutorial#_add-ssh-key-to-your-vm)
- User created an instruction file for future reference, which was added to the HPC documentation.

## General Learnings
- Users can connect to HPC systems via VSCode using the Remote SSH plugin.
- Documentation and user-generated instructions can be valuable resources for future users.
- HPC Admins can refer users to official documentation for setting up new tools.
```
---

### 2023050442001638_Aw%3A%C3%82%C2%A0New%20invitation%20for%20%22Vorlesung%20Computer%20Architecture%20for%20Medical%20A.md
# Ticket 2023050442001638

 # HPC Support Ticket Conversation Analysis

## Keywords
- Invitation
- HPC Portal
- SSO
- IdM credentials
- SSH public key
- FAU address
- Expired certificate

## Summary
A user reported not receiving a pending invitation for a course on the HPC portal. The conversation reveals several key points about the invitation process and common issues.

## Root Cause of the Problem
- The user did not receive the invitation due to an expired certificate.
- The invitation was sent to an incorrect or non-FAU email address.

## Solution
- The HPC Admin resends the invitation to the correct FAU email address.
- The user is instructed to follow the link, log in via SSO using IdM credentials, and upload an SSH public key.

## General Learnings
- Invitations for HPC portal access are sent to FAU email addresses.
- Users need to log in via SSO using IdM credentials to accept invitations.
- After accepting the invitation, users must upload an SSH public key to the corresponding account.
- Expired certificates can cause issues with receiving invitations.
- Users should provide their FAU email address for invitation resends.

## Steps for Support Employees
1. Verify the user's FAU email address.
2. Resend the invitation if it has expired or was sent to the wrong address.
3. Instruct the user to log in via SSO using IdM credentials.
4. Guide the user to upload an SSH public key after accepting the invitation.

This documentation can be used to resolve similar issues related to HPC portal invitations and SSH key uploads.
---

### 2024030142000566_Migration%20of%20mpo1001h%20HPC%20accounts%20to%20new%20HPC%20portal%20_%20SSH%20keys%20become%20man.md
# Ticket 2024030142000566

 # HPC Support Ticket Conversation Summary

## Subject
Migration of mpo1001h HPC accounts to new HPC portal / SSH keys become mandatory

## Keywords
- HPC account migration
- SSH keys
- HPC portal
- Single Sign-On (SSO)
- IdM portal
- SSH key types (RSA, ECDSA, ED25519)
- Usage statistics
- ClusterCockpit
- Jupyterhub

## General Learnings
- **Migration Process**: The migration of HPC accounts from the IdM portal to a new online HPC portal is underway.
- **SSH Keys**: Access to HPC systems will be via SSH keys only from March 15th. Users need to generate and upload SSH key pairs with passphrases.
- **SSH Key Types**: Accepted SSH key types are RSA (4096 bits), ECDSA (512 bits), and ED25519.
- **Portal Access**: The new HPC portal can be accessed at [https://portal.hpc.fau.de](https://portal.hpc.fau.de) using SSO with IdM credentials.
- **Account Validity**: The HPC portal will be the sole source for account validity starting from the end of February.
- **Usage Statistics**: Users and their PIs/project managers can view usage statistics in the HPC portal.
- **ClusterCockpit and Jupyterhub**: Access to these services will be through SSO links within the HPC portal.

## Root Cause of the Problem
- Users need to migrate their accounts to the new HPC portal and set up SSH keys for continued access.

## Solution
- Users should log in to the new HPC portal using SSO with their IdM credentials.
- Generate and upload SSH key pairs with passphrases to the HPC portal.
- Use the SSO links within the HPC portal to access ClusterCockpit and Jupyterhub.

## Additional Resources
- [SSH Documentation](https://hpc.fau.de/systems-services/documentation-instructions/ssh-secure-shell-access-to-hpc-systems/)
- [FAQs](https://hpc.fau.de/faqs/#ID-230)
---

### 2024020542004066_TriFORCE%20-%20Learning%20adaptive%20reusable%20skills%20for%20intelligent%20autonomous%20agents%20%.md
# Ticket 2024020542004066

 ```markdown
# HPC Support Ticket: TriFORCE Project Account Creation Issue

## Keywords
- HPC Portal
- TU Darmstadt
- SSO Issues
- Attribute Release
- DFN-AAI
- HRZ

## Summary
A user from TU Darmstadt encountered issues while trying to create an account in the HPC portal associated with the project "TriFORCE - Learning adaptive reusable skills for intelligent autonomous agents."

## Root Cause
The user received an error message upon logging in with their IDM account from TU Darmstadt. The issue was related to Single Sign-On (SSO) problems specific to TU Darmstadt.

## Solution
- **HPC Admin Response**: The HPC Admin informed the user that the issue was on the TU Darmstadt side. The HRZ of TU Darmstadt needed to release the required attributes to the HPC service provider.
- **Action Required**: The user was advised to contact the HRZ at TU Darmstadt (idmadmin@hrz.tu-darmstadt.de and service@hrz.tu-darmstadt.de) for further assistance.
- **Follow-up**: The HPC Admin noted that TU Darmstadt had become active in resolving the issue, indicating progress.

## General Learning
- **SSO Issues**: SSO problems can often be resolved by the home institution (in this case, TU Darmstadt) releasing the necessary attributes to the service provider.
- **Contact Points**: For SSO-related issues, users should contact their home institution's IT support (HRZ for TU Darmstadt).
- **DFN-AAI**: Understanding the role of DFN-AAI in attribute release is crucial for resolving such issues.

## Conclusion
The ticket highlights the importance of coordination between the user's home institution and the HPC service provider to resolve SSO-related issues. Users should be directed to their institution's IT support for attribute release problems.
```
---

### 2022013142003031_localhost%3A8920%20connection%20problem%20and%20password%20required.md
# Ticket 2022013142003031

 # HPC Support Ticket: Localhost Connection Problem and Password Required

## Keywords
- SSH Connection
- Password Issue
- Port 8920
- Permission Denied
- Public Key
- Hostbased Authentication

## Problem Description
- User is attempting to connect to HPC clusters via SSH.
- Connection to `localhost:8920` requires a password, which the user does not know.
- Error message: `iis\akatan@tg081's password: iis\\akatan@tg081: Permission denied (publickey,password,hostbased).`

## Root Cause
- User is unaware of the correct password for SSH connection.
- Possible expired certificate issue mentioned by HPC Admin.

## Solution
- **Password Clarification**: The password is the same across all HPC systems and is set in the identity management system (idm).
- **SSH Command**: User should provide the exact SSH command used for further diagnosis.
- **Compute Node Access**: User can only use SSH with one of the compute nodes while their job is running.

## Additional Notes
- The ticket was initially moved due to potential certificate expiration.
- Further details and the exact SSH command are required for a more precise solution.

## Next Steps
- User should verify their password and ensure it matches the one set in idm.
- Provide the exact SSH command used for connecting to the HPC cluster for further assistance.

---

This documentation aims to help support employees diagnose and resolve similar SSH connection and password issues in the future.
---

### 2024032742002542_SSH%20login%20auf%20cshpc.md
# Ticket 2024032742002542

 # HPC Support Ticket Analysis: SSH Login Issue

## Keywords
- SSH login
- Public key authentication
- Permission denied
- Host restriction
- Key pair generation
- HPC portal

## Summary
The user encountered a "Permission denied (publickey,password)" error when attempting to log in via SSH using their key pair. The root cause was identified as a host restriction set in the HPC portal for the key.

## Root Cause
- The user's SSH key pair was correct, but the login attempt was denied due to a host restriction set in the HPC portal.
- The user's key pair was not generated on the target machine, which is a requirement for proper configuration.

## Solution
- The HPC Admin identified the issue from the log file, which indicated a correct key but an incorrect host.
- The user was advised to generate the SSH key pair on the target machine and configure the connection settings correctly.
- Guidance was provided through documentation links for generating SSH key pairs via command line or MobaXTerm.

## General Learnings
- Ensure that SSH key pairs are generated on the target machine.
- Verify host restrictions set in the HPC portal for the key.
- Use provided documentation for generating SSH key pairs and configuring connection settings.

## Documentation Links
- [SSH Command Line Guide](https://doc.nhr.fau.de/access/ssh-command-line/)
- [SSH MobaXTerm Guide](https://doc.nhr.fau.de/access/ssh-mobaxterm/)

## Additional Notes
- The user's account had expired, and they were informed about the migration of FAU HPC accounts from the IDM portal to the HPC portal.
- The user was advised to check the HPC portal for an up-to-date overview of their services.
---

### 2022102542000949_Probleme%20beim%20Anmelden%20f%C3%83%C2%BCr%20das%20HPC-Cluster.md
# Ticket 2022102542000949

 ```markdown
# HPC-Support Ticket: Login Issues with SSH

## Keywords
- SSH login
- Cluster access
- Connection issues
- Maintenance schedule

## Problem Description
- User unable to login to the HPC cluster via SSH.
- Issue started recently.
- Maintenance work scheduled for the next day.

## Root Cause
- Unknown; could be a temporary issue or related to upcoming maintenance.

## Solution
- Not explicitly provided in the conversation.
- Suggested to check if the issue is known or related to upcoming maintenance.

## General Learnings
- Always check for known issues or upcoming maintenance when experiencing login problems.
- Verify if the issue is widespread or specific to the user.

## Next Steps
- Confirm with HPC Admins if there are any ongoing issues.
- Inform the user about the status of the cluster and any potential fixes.
```
---

