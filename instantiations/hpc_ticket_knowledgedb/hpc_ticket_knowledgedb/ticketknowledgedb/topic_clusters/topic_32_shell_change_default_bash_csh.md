# Topic 32: shell_change_default_bash_csh

Number of tickets: 23

## Tickets in this topic:

### 2015111842026116_%C3%83%C2%84nderung%20shell%20csh%20-%3E%20bash%20auf%20den%20hpc%20systemen.md
# Ticket 2015111842026116

 ```markdown
# HPC Support Ticket: Changing Shell from csh to bash

## Keywords
- Shell change
- csh to bash
- HPC systems
- User request

## Summary
A user requested to change their default shell from `csh` to `bash` on the HPC systems.

## Root Cause
The user wanted to switch their default shell to `bash` for better compatibility and ease of use.

## Solution
- **Action Taken**: The HPC Admin changed the user's default shell to `bash`.
- **Timeline**: The change was made, but it might take up to a day for the change to be effective across all systems.

## Notes
- The user provided their login ID (`mpwm13`) for the change.
- The HPC Admin confirmed the change and informed the user about the potential delay.

## General Learning
- Users can request shell changes through the support ticket system.
- Shell changes may take some time to propagate across all HPC systems.
- Always confirm the change with the user and provide an estimated timeline for the change to take effect.
```
---

### 2021061542001888_%C3%83%C2%84nderung%20Login-shell.md
# Ticket 2021061542001888

 ```markdown
# HPC Support Ticket: Changing Login Shell

## Keywords
- Login shell
- Bash
- IDM
- User request

## Problem
- User requested to change their login shell to Bash.

## Solution
- HPC Admin changed the login shell in the Identity Management (IDM) system.
- Noted that it may take some time for the change to propagate to all systems.

## What Can Be Learned
- Users can request changes to their login shell.
- Changes are made in the IDM system and may take time to reflect across all systems.
- HPC Admins handle such requests and provide updates on the status.
```
---

### 2015080542002369_bash%20on%20Emmy%3F.md
# Ticket 2015080542002369

 # HPC Support Ticket: bash on Emmy?

## Keywords
- Default shell
- bash
- csh
- .bashrc
- .bash_profile
- Login shell
- Interactive shell

## Summary
A new user of the cluster EMMY requested a change of the default shell from csh to bash. The user also inquired about the execution of the .bashrc file upon login.

## Root Cause
- Misunderstanding about the default shell on EMMY.
- Confusion about the execution of .bashrc and .bash_profile files.

## Solution
- **Default Shell**: The HPC Admin clarified that the default shell on EMMY is bash for all users, and other login shells are not supported.
- **.bashrc vs .bash_profile**: The HPC Admin explained that bash reads .bashrc when called interactively but not as the initial login shell. For login shells, bash reads .bash_profile. To maintain consistency, users can source .bashrc from .bash_profile.

```bash
# include .bashrc if it exists
if [ -f ~/.bashrc ]; then
    source ~/.bashrc
fi
```

## General Learnings
- Understand the difference between interactive and login shells.
- Know the purpose and execution conditions of .bashrc and .bash_profile files.
- Recognize that the default shell can vary between different clusters and systems.

## Ticket Status
- The user was satisfied with the explanation and had no further questions.
- The ticket was marked as resolved.
---

### 2019031242002562_default%20shell%20change.md
# Ticket 2019031242002562

 # HPC Support Ticket: Default Shell Change

## Keywords
- Default shell
- Bash
- User request
- Shell change

## Summary
A user requested a change of their default shell to Bash.

## Root Cause
The user's current default shell was not Bash, and they required it to be changed.

## Solution
The HPC Admin can change the user's default shell to Bash using the appropriate system commands.

## General Learnings
- Users may request changes to their default shell.
- The HPC Admin should be familiar with the process of changing a user's default shell.
- Ensure proper communication and confirmation with the user regarding the change.

## Actions Taken
- The user requested a change to their default shell.
- The HPC Admin needs to execute the shell change command.

## Next Steps
- Confirm the shell change with the user.
- Document the process for future reference.

## Notes
- Always verify the user's identity before making changes to their account.
- Ensure the user is aware of any potential impacts of changing their default shell.
---

### 2023102042002776_Source%20.bashrc%20on%20login%20node.md
# Ticket 2023102042002776

 ```markdown
# HPC-Support Ticket: Source .bashrc on Login Node

## Keywords
- .bashrc
- .bash_profile
- Automatic Sourcing
- Login Node

## Problem
The user has created a `.bashrc` file in their home directory but needs to manually source it upon login.

## Root Cause
The `.bashrc` file is not being automatically sourced because the login shell does not source it by default.

## Solution
To automatically source the `.bashrc` file upon login, create a `.bash_profile` file with the following content:
```bash
if [ -f ~/.bashrc ]; then
  . ~/.bashrc
fi
```
This ensures that the `.bashrc` file is sourced whenever the user logs in.

## General Learning
- The `.bashrc` file is typically used for interactive shells, while `.bash_profile` is used for login shells.
- To ensure that `.bashrc` is sourced automatically, a `.bash_profile` file can be created to source `.bashrc`.
- Understanding the difference between interactive and login shells is crucial for configuring shell startup files correctly.
```
---

### 2025022542002886_.bashrc%20on%20Fritz.md
# Ticket 2025022542002886

 ```markdown
# HPC Support Ticket: .bashrc on Fritz

## Keywords
- .bashrc
- .bash_profile
- PATH
- Julia
- Session commands

## Problem
User wants to add commands to be loaded each time they connect to Fritz, specifically to add `export PATH="$PATH:~/.juliaup/bin"`. The user is familiar with using a `.bashrc` file but does not see such a file on Fritz.

## Solution
1. Create a `.bashrc` file in the user's home directory with the desired commands.
2. Create a `.bash_profile` file in the user's home directory with the following content to ensure `.bashrc` is loaded in all cases:
   ```bash
   if [ -e ~/.bashrc ]; then
       . ~/.bashrc
   fi
   ```

## General Learning
- `.bashrc` is used to load commands for interactive shells.
- `.bash_profile` can be used to ensure `.bashrc` is loaded in all cases, including non-interactive shells.
- This method ensures that custom commands are executed every time the user connects to the HPC system.
```
---

### 42187527_Bash%20login%20f%C3%83%C2%BCr%20mppi36.md
# Ticket 42187527

 ```markdown
# HPC Support Ticket: Bash Login Shell Request

## Keywords
- HPC Account
- Login Shell
- Bash
- User ID
- Shell Change

## Summary
A user requested to change their default login shell to Bash.

## Problem
- **Root Cause**: User wanted to change the default login shell to Bash.

## Solution
- **Action Taken**: The HPC Admin changed the user's login shell to Bash.
- **Notification**: The user was informed that the change might take up to a day to take effect.

## Lessons Learned
- Users may request changes to their default login shell.
- Shell changes can take up to a day to propagate.
- HPC Admins can handle such requests efficiently.

## Follow-Up
- Ensure the user is aware of the delay in the change taking effect.
- Verify that the shell change has been successfully implemented.
```
---

### 42185245_Change%20of%20login%20shell.md
# Ticket 42185245

 ```markdown
# Change of Login Shell

## Keywords
- Login shell
- `chsh`
- Central directory
- Global change
- Permanent change

## Problem
- User attempted to change login shell to `bash` using `chsh`, but the change was not permanent.

## Root Cause
- Local changes made with `chsh` get overwritten by updates from the central directory.

## Solution
- HPC Admin changed the login shell globally for the user.
- It can take up to 24 hours for the change to propagate to all systems.

## Additional Information
- Changing the login shell on individual machines is not possible; it must be done globally.
- Users should contact HPC support for such changes.

## Follow-Up
- User inquired about submitting jobs with runtimes above 48 hours, which was split into a new ticket.
```
---

### 42157191_Kurze%20Frage%20zur%20.cshrc%20auf%20Lima.md
# Ticket 42157191

 ```markdown
# HPC Support Ticket: Issue with .cshrc on Lima

## Keywords
- .cshrc
- .tcshrc
- tcsh
- csh
- PATH
- Lima

## Problem Description
The user noticed that their `.cshrc` file on Lima was not being automatically read, resulting in the defined PATH not being available.

## Root Cause
The `tcsh` shell on Lima, which is an extended version of `csh`, reads the `.cshrc` file only if the `.tcshrc` file does not exist. The user's `.tcshrc` file was present and had precedence over `.cshrc`.

## Solution
1. **Option 1:** Add `source ~/.cshrc` to the `.tcshrc` file.
2. **Option 2:** Integrate the contents of `.tcshrc` into `.cshrc` and remove the `.tcshrc` file. This will ensure that `.cshrc` is used automatically.

## General Learning
- Understand the relationship between `csh` and `tcsh` shells.
- Recognize the precedence of configuration files in `tcsh`.
- Learn how to manage and integrate shell configuration files to ensure proper functionality.
```
---

### 2023073142002761_.bashrc.md
# Ticket 2023073142002761

 # HPC Support Ticket: .bashrc

## Keywords
- .bashrc
- .bash_profile
- alias commands
- PATH
- login nodes
- swap memory

## Problem
- User created a `.bashrc` file but had to manually source it to use alias commands and PATH settings.
- User noticed that login nodes were slower and suspected full swap memory.

## Solution
- Create a `.bash_profile` file in the user's home directory with the following content:
  ```bash
  if [ -f ~/.bashrc ]; then . ~/.bashrc; fi
  ```
  This ensures that the `.bashrc` file is automatically sourced when a new terminal is opened.
- No specific solution provided for the login nodes issue; HPC Admin was not aware of any known problems.

## General Learnings
- Understanding the difference between `.bashrc` and `.bash_profile`.
- Automating the sourcing of `.bashrc` to streamline user experience.
- Potential causes of slow login nodes, such as full swap memory, should be investigated further.

## References
- [Bash Startup Files](https://www.gnu.org/software/bash/manual/html_node/Bash-Startup-Files.html)
---

### 42144379_cshell%20to%20bash.md
# Ticket 42144379

 ```markdown
# HPC Support Ticket: cshell to bash

## Keywords
- Default shell change
- bash
- cshell
- HPC account configuration

## Problem
User requests to change the default shell from cshell to bash for their HPC account.

## Solution
- HPC Admin changes the default shell to bash.
- The change takes a few hours to propagate and become effective across all systems.

## General Learnings
- Users can request a change in their default shell by contacting HPC support.
- Shell changes may take several hours to fully propagate and become effective.
```
---

### 2016060942001426_Shell%20Umstellung.md
# Ticket 2016060942001426

 # HPC Support Ticket: Shell Umstellung

## Keywords
- Shell change
- Default shell
- bash to csh
- User account

## Summary
- **User Request**: Change default shell from `bash` to `csh`.
- **Account**: mppi011h

## Actions Taken
- **HPC Admin**: The request was deferred.

## Lessons Learned
- Users may request changes to their default shell.
- HPC Admins may defer such requests for various reasons (e.g., policy, technical limitations).

## Root Cause
- User preference for a different shell environment.

## Solution
- Not provided in the conversation. Further details are needed to understand the reason for deferral.

## Notes
- Ensure to communicate clearly with users about the reasons for deferring requests.
- Document any policies or technical limitations regarding shell changes for future reference.
---

### 2015092242003057_Shell-Umstellung.md
# Ticket 2015092242003057

 ```markdown
# Shell Change Request

## Keywords
- Shell change
- Bash to csh
- HPC cluster
- Inconsistent behavior

## Summary
A user requested a permanent change of their shell from Bash to csh. The user provided their email address, matriculation number, and HPC identifier. The request was made due to the user's workgroup using csh as their standard shell.

## HPC Admin Response
- The HPC admin noted that this was an unusual request as most users prefer Bash.
- The admin informed the user that the shell change is only possible on older clusters.
- Newer clusters, such as Emmy, have Bash as the default shell, and it cannot be changed.
- The admin advised against the change due to potential inconsistencies in behavior across different clusters.

## Solution
- The HPC admin agreed to change the shell for the older clusters but advised the user about the potential issues.
- The request was marked as completed.

## Lessons Learned
- Shell changes can lead to inconsistent behavior across different clusters.
- Newer clusters have fixed default shells that cannot be changed.
- It is important to consider the implications of shell changes, especially in a collaborative environment.
```
---

### 42235447_Csh%20auf%20bash%20umstellen.md
# Ticket 42235447

 ```markdown
# HPC-Support Ticket: Csh auf bash umstellen

## Keywords
- Standard Shell
- Bash
- Csh
- Login
- Shell Change

## Summary
- **User Request**: Change the default shell from Csh to Bash.
- **HPC Admin Response**: Confirmed the change and noted that it may take up to a day for the change to take effect.

## Root Cause
- User wanted to switch the default shell from Csh to Bash.

## Solution
- HPC Admin changed the default shell to Bash and informed the user that the change might take up to a day to propagate.

## General Learning
- Users can request a change in their default shell.
- Shell changes may not be immediate and can take some time to propagate across the system.
```
---

### 2017102742001187_Shell-%C3%83%C2%84nderung%20unrz55.md
# Ticket 2017102742001187

 ```markdown
# HPC Support Ticket: Shell Change Issue

## Keywords
- Shell change
- Login shell
- HPC systems
- DFM (Distributed File Management)
- LDAP
- bash
- csh
- Woody-Cluster

## Problem Description
- User changed their login shell to `bash` in the IdM-Portal.
- The change was not reflected on all HPC systems, including clusters and cshpc.
- The user still sees `csh` as the login shell on these systems.

## Root Cause
- The shell for HPC systems is set via DFM, not directly through the IdM-Portal.
- Different clusters have different default shell settings, with some still allowing `csh`.

## Solution
- The HPC Admin manually changed the user's shell in DFM to `bash`.
- The decision was made to leave the current system as is, as the issue is not frequent enough to warrant a system-wide change.

## General Learnings
- Shell settings for HPC systems are managed through DFM.
- Not all HPC clusters support the same shell options; some still use `csh`.
- The default shell for new users is `bash`, but changes are not always straightforward.
- Manual intervention by HPC Admins may be required for shell changes to take effect across all systems.
```
---

### 2019052942001215_Question%20on%20cluster%20login.md
# Ticket 2019052942001215

 # HPC Support Ticket: Cluster Login Issue

## Keywords
- SSH login
- .cshrc
- Illegal variable name
- BASHisms
- ~/.tcshrc

## Problem Description
- User encounters an "Illegal variable name" error when logging into the cluster via SSH.
- The user's `.cshrc` script is not executed properly during login.
- Manually sourcing `.cshrc` resolves the issue temporarily.

## Root Cause
- The user's `~/.tcshrc` file contains BASH-specific syntax (BASHisms), which is not compatible with tcsh.

## Solution
- Remove or correct the BASH-specific syntax in the `~/.tcshrc` file to ensure compatibility with tcsh.

## General Learning
- Ensure that shell-specific configuration files (e.g., `.tcshrc`, `.cshrc`, `.bashrc`) contain syntax compatible with the respective shell.
- BASH-specific syntax in tcsh configuration files can cause errors during login.

## Roles Involved
- HPC Admins
- 2nd Level Support Team
---

### 2022040142001521_csh%20zu%20bash%20shell.md
# Ticket 2022040142001521

 # HPC Support Ticket: Changing Default Shell from csh to bash

## Keywords
- Default Shell
- csh
- bash
- chsh
- IdM-System

## Problem
- User's default shell on SSH login is `csh`.
- User prefers `bash` as the default shell.
- User attempted to change the shell using `chsh -s /bin/bash` but received an error: `You may not change the shell for 'fhn001'`.

## Root Cause
- User does not have permission to change the default shell using `chsh`.

## Solution
- HPC Admin changed the user's default shell to `bash` in the IdM-System.
- The change will take some time to propagate to the HPC systems.

## General Learnings
- Users may not have permission to change their default shell using `chsh`.
- HPC Admins can change the default shell for users in the IdM-System.
- Changes made in the IdM-System may take time to reflect on the HPC systems.
---

### 2018041342000731_Shell%20umstellen.md
# Ticket 2018041342000731

 # HPC Support Ticket: Shell Change Request

## Keywords
- Shell change
- cshell
- bash
- HPC account
- Cluster systems (LiMa, Emmy, Meggie)

## Summary
A user requested a change from bash to cshell for their HPC account. The user initially referred to their account as a "HAP-Account," which caused some confusion. The HPC Admin clarified the correct terminology and processed the request where possible.

## Root Cause
- User confusion over account type terminology.
- User preference for cshell over bash.

## Solution
- HPC Admin changed the user's shell to cshell on systems where it was possible.
- Noted that newer clusters (LiMa, Emmy, Meggie) have bash as the default shell and cannot be changed.
- Informed the user that the change might take some hours to become effective.

## General Learnings
- Importance of clear communication regarding account types and system capabilities.
- Understanding the limitations of shell changes on different cluster systems.
- Proper handling of user requests for shell changes and managing expectations regarding system constraints.
---

### 2016080142001053_stupid%20problem%20with%20shell%20on%20woody.md
# Ticket 2016080142001053

 # HPC Support Ticket: Shell Environment Issue on Woody

## Keywords
- Shell environment
- cshell
- bash
- queue commands (qstat, qsub)
- job submission scripts
- login-shell change

## Problem Description
- User logs into `woody` and is placed in a cshell environment, unlike `emmy` and `lima` which use bash.
- Queue commands (`qstat`, `qsub`) work in cshell but not in bash on `woody`.
- User's job submission scripts are in bash, causing issues with automatic job resubmission.

## Root Cause
- Inconsistent shell environments across different HPC systems.
- Queue commands compatibility issue with bash on `woody`.

## Solution
- HPC Admin offered to change the user's login-shell to bash on all HPC systems.
- User agreed to the change.
- Change was implemented and expected to be effective within a couple of hours.

## General Learnings
- Inconsistent shell environments can cause compatibility issues with scripts and commands.
- Changing the login-shell can resolve such issues.
- Communication with the user is key to understanding and resolving the problem effectively.

## Actions Taken
- HPC Admin changed the user's login-shell to bash on all HPC systems.
- Ticket closed as resolved.

## Follow-up
- User should verify that the shell change has resolved the issue with job submission scripts.
- If issues persist, further investigation into queue system compatibility with bash on `woody` may be required.
---

### 42179907_Default%20Shell%20%C3%83%C2%A4ndern.md
# Ticket 42179907

 # HPC Support Ticket: Default Shell Change

## Keywords
- Default Shell
- chsh
- CSH
- BASH
- IDM
- RRZE-Systems

## Problem
- User attempted to change default shell from CSH to BASH using `chsh`, but it reverted back to CSH after a few minutes.

## Root Cause
- The `chsh` command does not work for changing the default shell on the HPC system.

## Solution
- The default shell change needs to be performed by an HPC Admin.
- The change can take a few hours to propagate across all RRZE-Systems.

## General Learnings
- Users should contact HPC Admins for changing the default shell.
- The `chsh` command is not effective for this purpose.
- The change might take some time to be fully implemented across all systems.

## Actions Taken
- HPC Admin changed the default shell for the user's account to BASH.
- User was informed about the change and the expected delay for it to take effect.

## Future Reference
- For similar issues, users should be directed to contact HPC Admins for default shell changes.
- Admins should inform users about the potential delay in the change taking effect.
---

### 2018070342001771_auf%20csh%20umstellen.md
# Ticket 2018070342001771

 ```markdown
# HPC-Support Ticket: Switching from bash to csh

## Keywords
- Shell change
- bash
- csh
- User configuration

## Summary
A user requested a permanent switch from the bash shell to the csh shell.

## Root Cause
The user prefers using the csh shell over the default bash shell.

## Solution
- The HPC Admin needs to change the default shell for the user.
- This can typically be done by modifying the user's account settings in the system configuration files.

## Steps to Resolve
1. Identify the user's account (e.g., `mppi047h`).
2. Change the default shell to csh using the appropriate system command (e.g., `chsh -s /bin/csh mppi047h`).
3. Verify the change by logging in as the user and checking the active shell.

## Notes
- Ensure the user is aware of the differences between bash and csh.
- Document any specific configurations or scripts that need to be adjusted for compatibility with csh.
```
---

### 2020021042002065_Umstellung%20der%20default%20shell.md
# Ticket 2020021042002065

 # HPC Support Ticket: Changing Default Shell

## Keywords
- Default shell
- C-shell
- Bash
- HPC account
- Shell change request

## Summary
- **User Request**: Change default shell from c-shell to bash.
- **HPC Admin Response**: Default shell is already set to bash.
- **Additional Information**: C-shell is technically outdated and not supported on newer clusters.

## Root Cause
- User misconception about the current default shell.

## Solution
- Inform the user that the default shell is already set to bash.
- Advise against using c-shell due to its technical limitations and lack of support on newer clusters.

## General Learning
- Always verify the current default shell before making changes.
- Educate users about the limitations and support status of different shells.

## Notes
- This ticket highlights the importance of user education and verification of current settings before making changes.
- C-shell is not recommended due to its outdated status and lack of support on newer systems.
---

### 2020060842001849_Change%20Login%20Shell.md
# Ticket 2020060842001849

 # HPC Support Ticket: Change Login Shell

## Keywords
- Login Shell
- Zsh
- Bash
- User Account
- Cluster Computers

## Summary
A user requested to change their login shell to `zsh`. The HPC admin responded that the only supported login shell is `bash`.

## Root Cause
- User requested an unsupported login shell.

## Solution
- Inform the user that only `bash` is supported as the login shell.

## General Learnings
- The HPC cluster supports only `bash` as the login shell.
- Users may request changes to their account settings based on information from lectures or other sources.
- It is important to communicate the supported configurations clearly to users.

## Related Parties
- HPC Admins
- 2nd Level Support Team
- Head of the Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support
- Software and Tools Developer
---

