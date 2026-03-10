# Topic 27: nomachine_xrdp_desktop_session_nx

Number of tickets: 29

## Tickets in this topic:

### 2024072542002388_Problem%20mit%20XRDP.md
# Ticket 2024072542002388

 # HPC Support Ticket: Problem with XRDP

## Keywords
- XRDP
- Connection issue
- SSH login
- Session termination
- pkill command

## Problem Description
The user reported that their XRDP connection to the HPC system stopped working for about two weeks. The XRDP window would open briefly and then close immediately. The user had not made any changes to their setup and could still log in via SSH.

## Root Cause
The issue was caused by a parked XRDP session that got stuck due to a recent update.

## Solution
The HPC Admin suggested terminating the existing XRDP session and logging in again to create a new session. The user was instructed to:

1. Log in to the `csnhr` via SSH.
2. Execute the command `pkill -9 -u <username>` to forcefully terminate all running processes.
3. Wait for approximately 30 seconds.
4. Attempt to log in with XRDP again.

## Outcome
The user confirmed that the solution worked and they were able to log in via XRDP successfully.

## General Learning
- Updates can sometimes cause XRDP sessions to get stuck.
- Terminating the stuck session and creating a new one can resolve the issue.
- The `pkill` command can be used to forcefully terminate user processes.
---

### 2024080242002446_Alex%20Availability.md
# Ticket 2024080242002446

 ```markdown
# HPC Support Ticket: Alex Availability

## Keywords
- Alex
- cshpc
- decommissioned
- hostname resolution
- ssh error
- NoMachine NX
- XRDP

## Problem
- User unable to access Alex via SSH.
- Error message: `ssh: Could not resolve hostname cshpc.rrze.fau.de: Name or service not known`
- Connection closed by remote host.

## Root Cause
- The host `cshpc` was decommissioned.

## Solution
- Refer to the official announcement for more information: [Dialog Server cshpc Decommissioned, NoMachine NX to be Replaced by XRDP](https://hpc.fau.de/2024/08/01/dialog-server-cshpc-decommissioned-nomachine-nx-to-be-replaced-by-xrdp/)

## General Learning
- Always check for recent announcements or decommissioning notices when encountering hostname resolution issues.
- Update access methods and tools as per the latest guidelines provided by the HPC support team.
```
---

### 2025012942001354_Probleme%20bei%20Verbindung%20mit%20Fritz%20via%20Remote-Desktop.md
# Ticket 2025012942001354

 # HPC Support Ticket: Connection Issue with Fritz via Remote Desktop

## Keywords
- XRDP
- Remote Desktop
- SSH
- MobaXTerm
- WinSCP
- VPN
- .bat-Datei
- Passphrase
- Blackscreen
- XFCE
- KDE-Plasma
- .xsession-errors
- .log

## Problem Description
- User unable to connect to Fritz via XRDP.
- Remote Desktop window shows a black screen and closes after a few seconds.
- SSH connections via MobaXTerm and WinSCP work fine.
- Remote Desktop connection to Meggie works without issues.
- Problem persists across different VPN clients and devices (Desktop and Laptop).
- Error logs mention KDE-Plasma, despite the user using XFCE.

## Root Cause
- Possible stuck XRDP session on Fritz.

## Solution
- Follow the steps outlined in the FAQ: [FAQ Link](https://doc.nhr.fau.de/faq/#i-cannot-connect-via-xrdp-anymore--what-should-i-do)

## Additional Information
- User provided .xsession-errors and .log files for further analysis.
- User ID for Fritz: b246dc11

## Next Steps
- If the FAQ solution does not resolve the issue, further investigation of the provided log files may be necessary.

## Support Team
- HPC Admins
- 2nd Level Support Team

## Related Personnel
- Head of the Datacenter: Gerhard Wellein
- Training and Support Group Leader: Georg Hager
- NHR Rechenzeit Support: Harald Lanig
- Software and Tools Developer: Jan Eitzinger, Gruber
---

### 2021031142001408_Using%20Star-CCM%2B%20in%20interactive%20GUI%20mode.md
# Ticket 2021031142001408

 # HPC Support Ticket: Using Star-CCM+ in Interactive GUI Mode

## Keywords
- Star-CCM+
- GUI mode
- Front-end nodes
- Emmy cluster
- Windows system
- X-forwarding
- Putty
- XMing
- NoMachineNX
- cshpc

## Problem
User wants to run Star-CCM+ in GUI mode on the front-end nodes of the Emmy cluster using a Windows system.

## Root Cause
- User is new to HPC and unaware of the restrictions and proper procedures for running GUI applications.

## Solution
- **Documentation**: Refer to the official documentation for running Star-CCM+ on HPC systems.
- **Batch Mode**: Star-CCM+ should normally run in batch mode on compute nodes for production runs.
- **Pre-/Postprocessing**: Use local machine for pre-/postprocessing. If not possible, use the frontend for small simulations or an interactive job.
- **X-forwarding**: Use X-forwarding via Putty and XMing for GUI applications.
- **NoMachineNX**: Recommended for better performance. Instructions available on the HPC documentation site.

## Outcome
- User successfully used NoMachineNX on cshpc for running Star-CCM+ in GUI mode.

## General Learnings
- GUI applications should not be run on cluster frontends for production runs.
- X-forwarding and NoMachineNX are viable solutions for running GUI applications on HPC systems.
- Always refer to the official documentation for application-specific instructions.

## References
- [Star-CCM+ Documentation](https://hpc.fau.de/systems-services/systems-documentation-instructions/special-applications-and-tips-tricks/star-ccm/)
- [NoMachineNX Instructions](https://hpc.fau.de/systems-services/systems-documentation-instructions/clusters/dialogserver/)
---

### 2024121942001989_Remoteverbindung%20Fritz.md
# Ticket 2024121942001989

 # HPC-Support Ticket: Remoteverbindung Fritz

## Problem
- **User**: Unable to connect to Fritz Desktop after logging out.
- **Symptoms**: Black screen, unable to log in to HPC.
- **Root Cause**: xRDP session stuck, causing no meaningful output.

## Troubleshooting Steps
1. **HPC Admin**: Asked user to test a normal SSH connection.
2. **User**: Confirmed using a public key and a .config file for graphical access.
3. **HPC Admin**: Identified the issue as a stuck xRDP session.

## Solution
1. **HPC Admin**: Instructed user to log in via SSH and terminate the xRDP session.
   ```bash
   ssh b246dc12@csnhr.nhr.fau.de
   pkill -9 -u b246dc12
   ```
2. **User**: Successfully terminated the session and was able to log in again via xRDP.

## Keywords
- xRDP
- SSH
- Stuck session
- Terminate processes
- Graphical access

## Lessons Learned
- Stuck xRDP sessions can cause black screens and login issues.
- Terminating the session via SSH can resolve the issue.
- Users should be familiar with SSH commands to manage their sessions.

## Documentation
- [SSH Command Line](https://doc.nhr.fau.de/access/ssh-command-line/)
- [xRDP Access](https://doc.nhr.fau.de/access/xrdp/)
---

### 42055674_Darstellungsprobleme%20bei%20STAR-CCM%2B%20via%20SSH_XWin32.md
# Ticket 42055674

 # HPC Support Ticket: Darstellungsprobleme bei STAR-CCM+ via SSH/XWin32

## Keywords
- Darstellungsprobleme
- STAR-CCM+
- SSH
- XWin32
- NX
- Windows-Installationspaket
- HPC
- Dialogserver

## Problem Description
The user is experiencing display issues with STAR-CCM+ when accessed via SSH/XWin32.

## Root Cause
The exact root cause of the display issues is not specified, but it is related to the use of XWin32 for remote access.

## Solution
The HPC Admin suggests replacing XWin32 with "NX" to resolve the display issues. A pre-configured Windows installation package for NX is provided, along with download instructions and access credentials.

## Steps to Resolve
1. Download the NX Client from the provided link.
2. Install the NX Client using the provided Windows installation package.
3. Follow the instructions on the [RRZE Dialogserver page](http://www.rrze.uni-erlangen.de/dienste/arbeiten-rechnen/hpc/systeme/dialogserver.shtml) to configure and use NX.

## Additional Information
- **Download Link**: [NX Client Installation Package](http://www.rrze.uni-erlangen.de/dienste/arbeiten-rechnen/hpc/kundenbereich/rzinst-NOMACHINE-NXClient-3.2.0.13-2K_XP_2K3_VI-ML-fau-3.0.exe)
- **Access Credentials**: hpc / passwort

## Conclusion
Switching from XWin32 to NX can potentially resolve display issues with STAR-CCM+ when accessed remotely via SSH.
---

### 2024031142003768_Frage%20zur%20HPC%20Nutzung.md
# Ticket 2024031142003768

 # HPC Support Ticket Conversation Summary

## Subject: Frage zur HPC Nutzung

### Keywords
- NoMachine
- SSH Key
- MobaXterm
- XRDP
- Remote Desktop
- Config File
- Matlab
- Grafische Benutzeroberfläche

### General Learnings
- **NoMachine Access**: NoMachine can still be used after the SSH key update. Users need to configure SSH access for `cshpc.nhr.fau.de`.
- **SSH Configuration**: Proper configuration of the SSH config file is crucial for successful connections. The file should be named `config` without any extension and placed in the `.ssh` directory.
- **XRDP Performance**: XRDP can be slower compared to NoMachine, especially on slower connections. Users can try different desktop environments to improve performance.
- **SSH Key Management**: Ensure the SSH key is correctly referenced in the config file and has the correct permissions.
- **Matlab on Woody**: Users can connect to `woody` from within an XRDP session on `csnhr.nhr.fau.de` using `ssh -Y woody`.

### Root Cause of the Problem
- **SSH Key Not Found**: The SSH client was not finding the private key due to incorrect path or filename.
- **Incorrect Username**: The SSH client was attempting to log in with the wrong username.
- **XRDP Performance**: XRDP was slower compared to NoMachine, likely due to higher data rate requirements.

### Solutions
- **SSH Key Configuration**: Ensure the SSH key is correctly referenced in the config file and has the correct permissions. Use the correct path and filename for the key.
- **Username Configuration**: Ensure the correct username is specified in the SSH config file.
- **XRDP Optimization**: Users can try different desktop environments to improve XRDP performance. The `.xsession` file can be created in the home directory to specify the desktop environment.
- **Matlab Access**: Connect to `woody` from within an XRDP session on `csnhr.nhr.fau.de` using `ssh -Y woody`.

### Additional Notes
- **NoMachine Deprecation**: NoMachine will be deprecated on `csnhr.nhr.fau.de` in the near future. Users are encouraged to switch to XRDP.
- **SSH Config File**: The SSH config file should be named `config` without any extension and placed in the `.ssh` directory.
- **Key Permissions**: Ensure the SSH key has the correct permissions (`chmod 600 ~/.ssh/id_ed25519`).

This summary provides a concise overview of the key points and solutions discussed in the HPC support ticket conversation. It can be used as a reference for support employees to address similar issues in the future.
---

### 2022031442003275_KDE%20auf%20Nomachine%20funktioniert%20nicht.md
# Ticket 2022031442003275

 # HPC Support Ticket: KDE auf NoMachine funktioniert nicht

## Keywords
- KDE Desktop
- NoMachine
- Virtual Desktop
- Fehlermeldung
- System Administrator
- Ubuntu 20.04
- startkde
- startplasma-x11
- Symlink

## Problem
Der KDE-Desktop auf NoMachine funktioniert nicht mehr. Nach der Auswahl der Option "Einen neuen KDE virtuellen Desktop erstellen" bleibt der Bildschirm schwarz und es erscheint die Fehlermeldung "Cannot find the KDE environment. Please contact your system administrator."

## Root Cause
Der Desktop-Teil von KDE wurde 2014 von "KDE" in "Plasma Desktop" umbenannt. Seit Ubuntu 20.04 wurde der ehemalige 'startkde'-Befehl in 'startplasma-x11' umbenannt. NoMachine versucht jedoch weiterhin "startkde" zu verwenden.

## Solution
Ein Symlink von 'startkde' zu 'startplasma-x11' wurde angelegt, um das Problem zu beheben.

## What to Learn
- Überprüfen Sie die Befehle, die von NoMachine verwendet werden, um sicherzustellen, dass sie aktuell sind.
- Symlinks können verwendet werden, um Kompatibilität mit älteren Befehlen zu gewährleisten.
- Aktualisierungen von Softwarekomponenten können zu Kompatibilitätsproblemen führen, die durch einfache Anpassungen gelöst werden können.
---

### 2019121742001359_Ansys%20Fluent.md
# Ticket 2019121742001359

 # HPC Support Ticket: Ansys Fluent Display Issue

## Keywords
- Ansys Fluent
- Display issue
- White screen
- X11 driver
- HPC account
- CIP Pool
- Laptop

## Problem Description
- User experiences a white screen when trying to run Ansys Fluent on HUBER CIP Pool or their personal machine.
- The console is functional, but the display is not rendering correctly.
- CFD Post works fine on both HUBER CIP Pool and the user's laptop.

## Root Cause
- The issue is related to the graphics driver used by Fluent.

## Solution
- Start Fluent with the X11 driver to resolve display issues:
  ```
  fluent -driver x11
  ```

## General Learnings
- Display issues in HPC applications can often be resolved by specifying a different graphics driver.
- The `-driver` command line option can be used to change the graphics driver in Ansys Fluent.
- It's important to test applications in different environments to diagnose and isolate issues effectively.

## Related Ticket
- Subject: Ansys Fluent
- Date: 17.12.2019
- HPC Admin: Katrin Nusser
- User: Sidharath Madaan (iwpa045h)
---

### 2024080742003909_Probleme%20bei%20HPC-Cluster%20Meggie.md
# Ticket 2024080742003909

 # HPC Support Ticket: Probleme bei HPC-Cluster Meggie

## Keywords
- HPC Cluster Meggie
- STAR CCM+
- NoMachine
- XRDP
- KDE Plasma Desktop
- SSH Tunnel
- Lags

## Problem Description
- User is experiencing significant lags when using STAR CCM+ on the Meggie cluster via XRDP with KDE Plasma Desktop.
- The issue started after the deactivation of NoMachine.
- User mentions that another cluster, Fritz, works normally but they lack the necessary permissions to use it.

## Root Cause
- The user is running STAR CCM+ within an XRDP session, which involves an SSH tunnel to the Meggie cluster.
- This workflow is inherently slow due to the need for the GUI to communicate over SSH.

## Solution
- No immediate solution provided by the HPC Admin.
- User is advised to consult colleagues for tips on a more comfortable usage setup.

## What Can Be Learned
- Running GUI applications over SSH tunnels within XRDP sessions can lead to significant performance issues.
- It is important to understand the workflow and the tools being used to diagnose performance problems accurately.
- Consulting with colleagues or other users who have experience with the specific software (STAR CCM+) can provide valuable insights and potential solutions.

## Next Steps
- Users experiencing similar issues should consider alternative methods for running GUI applications on HPC clusters.
- Further investigation into optimizing the workflow for STAR CCM+ on the Meggie cluster may be necessary.
- Documentation and user guides should be updated to reflect the potential performance issues with XRDP and SSH tunnels.
---

### 2024011042001686_NX%20auf%20CSHPC.md
# Ticket 2024011042001686

 ```markdown
# HPC Support Ticket: NX auf CSHPC

## Keywords
- NX
- Desktop
- CSHPC
- XFCE4
- TDE
- nxserver
- nxerror.log
- Firewall
- Session-Log

## Problem Description
- User unable to start a desktop session on CSHPC using NX after returning from vacation.
- The session hangs without any error message, even with a custom session using "Run the console".

## Diagnostic Information
- `pstree` output shows the process tree involving `nxserver.bin`.
- `nxerror.log` contains an error related to a bad display name in the "add" and "delete" commands.

## Root Cause
- Possible issue with quoting in the display name causing a bad display name error.
- Potential local firewall issue preventing the NX client from connecting to the tunneled port.

## Solution
- User reported that switching to TDE and XFCE4 resolved the issue.
- HPC Admin suggested checking the session types and using a custom session with the command `/usr/bin/starttde`.

## General Learnings
- Check `nxerror.log` for display name errors.
- Verify session types and use custom sessions with appropriate commands.
- Consider local firewall issues if sessions fail to connect.
```
---

### 2024050742001229_Frage%20zu%20XRDP%20login.md
# Ticket 2024050742001229

 # HPC Support Ticket: XRDP Login Issue

## Keywords
- XRDP
- Remote Desktop
- Login Issue
- SSH
- Session Management

## Problem Description
- User unable to login via XRDP since the morning.
- Error message displayed on the login screen.
- Previously, the login worked without issues.

## Root Cause
- The user's existing session on the server (csnhr) was stuck, causing the login attempt to fail when trying to resume the session.

## Solution
- The HPC Admin suggested logging in via SSH and terminating the existing session using the command `pkill -9 -u <username>`.
- The user confirmed that this solution worked.

## General Learnings
- XRDP login issues can be caused by stuck sessions.
- Terminating the stuck session via SSH can resolve the issue.
- Regularly checking and managing sessions can prevent such problems.

## Steps for Support Employees
1. Verify if there is a general issue with XRDP.
2. If no general issue is found, suggest the user to terminate the existing session via SSH.
3. Provide the command `pkill -9 -u <username>` for terminating the session.
4. Confirm with the user if the issue is resolved.

## Additional Notes
- Always ensure that the user's account and system details are correctly noted for troubleshooting.
- Communicate clearly with the user to understand the exact nature of the problem and provide step-by-step solutions.
---

### 2024041742001855_Re%3A%20Anfrage%20zur%20Nutzung%20von%20HPC-Instanzen%20per%20Remote%20Desktop%20Verbindung.md
# Ticket 2024041742001855

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject
Re: Anfrage zur Nutzung von HPC-Instanzen per Remote Desktop Verbindung

## Keywords
- Remote Desktop (RDP)
- NoMachineNX
- XRDP
- Dialogserver
- Clusterknoten
- Batch-Betrieb
- Lizensierungsmodell

## Summary
A user inquired about using HPC instances via Remote Desktop for running the software Mplus. The HPC Admin provided information on available remote desktop options and the suitability of HPC instances for the user's needs.

## Root Cause of the Problem
The user wanted to use HPC instances for running software that requires a graphical interface, which is not typically supported on HPC clusters.

## Solution
- **Remote Desktop Options**: The user can connect to Dialogserver via NoMachineNX or XRDP. XRDP will be the only option in the future.
- **Suitability for Tasks**: Dialogserver is not suitable for compute-intensive tasks. These should be run on cluster nodes.
- **Batch Operation**: The software should ideally run in batch mode without a graphical interface.
- **Licensing**: The user needs to ensure that their software license can be used on the HPC clusters.

## General Learnings
- **Communication**: Users should always contact support-hpc@fau.de for HPC-related queries to ensure they reach the right person.
- **Remote Access**: NoMachineNX and XRDP are available for remote desktop connections, with XRDP being the future standard.
- **Task Suitability**: Dialogserver is not suitable for compute-intensive tasks. These should be run on cluster nodes.
- **Software Compatibility**: Software should ideally run in batch mode without a graphical interface to be suitable for HPC clusters.
- **Licensing**: Users need to verify that their software licenses can be used on HPC clusters.
```
---

### 2023032042003743_X11%20und%20interactive%20jobs.md
# Ticket 2023032042003743

 ```markdown
# HPC-Support Ticket: X11 and Interactive Jobs

## Keywords
- X11
- Interactive Jobs
- GUI
- Python Application
- X Forwarding
- NoMachine
- SSH

## Problem
- User wants to run a Python application with a GUI on the cluster while controlling the GUI from their own computer.
- X forwarding works outside of jobs but not within interactive jobs.
- Documentation confirms that X11 forwarding is not available for interactive jobs.

## Root Cause
- Most cluster nodes do not have the necessary X libraries installed.
- X11 forwarding is not supported for interactive jobs.

## Solution
- Allocate an interactive job and use SSH with X forwarding (`ssh -X/-Y`) and proxy jumps to start the application on the node.
- For better performance, connect via NoMachine to `cshpc.rrze.fau.de` and then use SSH with X forwarding to the node.

## Additional Information
- No plans to support X11 forwarding for interactive jobs in the future.
- Using NoMachine and SSH with X forwarding is a recommended alternative.

## Ticket Status
- Closed
```
---

### 2022062042001474_Nomachine%20NX%20mit%20TDE%20defekt.md
# Ticket 2022062042001474

 # HPC Support Ticket: NoMachine NX with TDE Issue

## Keywords
- NoMachine NX
- TDE
- Black screen
- Connection issue
- cshpc.rrze.fau.de
- SSH
- Uni-PC
- Laptop

## Problem Description
- User unable to connect to `cshpc.rrze.fau.de` via NoMachine NX with TDE since Friday.
- Connection results in a black screen followed by disconnection after a few seconds.
- Other connection methods like NoMachine NX with KDE and SSH via terminal still functional.
- Issue persists across different devices (Uni-PC and laptop).

## Root Cause
- Unknown; could be a recent change in the system or a user-specific issue.

## Troubleshooting Steps
- Verify if there were any system changes recently.
- Check user-specific configurations for NoMachine NX with TDE.
- Test NoMachine NX with TDE on other user accounts to isolate the issue.

## Solution
- Not provided in the conversation. Further investigation required.

## Notes
- Involve HPC Admins if system-wide changes are suspected.
- Escalate to 2nd Level Support team if user-specific configurations need detailed inspection.

## Follow-up Actions
- Update the user on the progress of the investigation.
- Document any findings and solutions for future reference.
---

### 2024071842002436_csnhr%3A%20Probleme%20beim%20Login%20%C3%83%C2%BCber%20Windows%20via%20XRDP.md
# Ticket 2024071842002436

 # HPC Support Ticket: Probleme beim Login über Windows via XRDP

## Keywords
- XRDP
- Windows Login
- Session Management
- pkill
- thinclient_drives
- Performance Issues
- Remote Desktop Client

## Problem Description
- User unable to log in via XRDP on Windows.
- Graphical desktop appears briefly and then closes.
- Command prompt window remains open and closes after some time.
- Issue affects multiple users.

## Root Cause
- Stuck sessions causing login issues.
- Potential issues with `thinclient_drives` directory.

## Solution
1. **Kill Stuck Sessions:**
   - Use `pkill -9 -u <username>` to terminate stuck sessions.
   - Wait for systemd to clean up session remnants.

2. **Adjust Remote Desktop Client Settings:**
   - Reduce expected bandwidth.
   - Lower color depth (e.g., from 32-bit to 16-bit).

3. **Handle `thinclient_drives` Issues:**
   - Note that `thinclient_drives` is a FUSE mount used for RDP features.
   - The mount may remain and cause issues, but it should not affect performance.
   - The mount will be cleared on the next system reboot.

## Additional Notes
- The path for `thinclient_drives` has been changed to `/run/user/%u/thinclient_drives` to allow root to clean up broken mounts.
- Users with existing sessions before the change will retain the broken mount until the next reboot.

## Conclusion
- The issue was resolved by terminating stuck sessions and adjusting Remote Desktop Client settings.
- The `thinclient_drives` issue is known and will be addressed in future reboots.

## Follow-up Actions
- Monitor for similar issues and apply the same solutions if they recur.
- Ensure users are aware of the changes to the `thinclient_drives` path and the need for a reboot to clear broken mounts.
---

### 2025022442003136_Anmeldung%20auf%20Fritz%20via%20Remote%20Desktop%20b142dc10.md
# Ticket 2025022442003136

 ```markdown
# HPC Support Ticket: Remote Desktop Issue on csnhr

## Keywords
- Remote Desktop
- Blackscreen
- Processes
- pkill
- xrdp
- csnhr
- Fritz

## Summary
A user encountered a black screen when trying to reconnect to a remote desktop session on csnhr after the session had hung and processes were terminated.

## Root Cause
- The user terminated processes on the wrong system (Fritz) instead of the correct one (csnhr).
- Leftover processes on csnhr were causing the remote desktop session to hang.

## Solution
- The user was advised to terminate the processes on csnhr using the command `pkill -9 -u <username>`.
- Cleaning up the processes on csnhr resolved the issue, and the remote desktop session started working again.

## Lessons Learned
- Ensure that processes are terminated on the correct system where the remote desktop session is running.
- Check for any lingering processes that might be causing the session to hang.
- Properly identify the system mentioned in the ticket to provide accurate support.
```
---

### 2019032142001181_Firefox%20auf%20cshpc%20startet%20nicht.md
# Ticket 2019032142001181

 # HPC-Support Ticket: Firefox auf cshpc startet nicht

## Keywords
- Firefox
- Connection refused
- AppArmor
- Ubuntu 18.04
- XDG_RUNTIME_DIR
- KDE ActivityManager
- xfce4-Session
- systemd-DBUS

## Problem Description
- User unable to start Firefox on cshpc.
- Error message: "Connection refused."
- AppArmor logs indicate issues with Firefox.
- User's session logs flooded with KDE ActivityManager errors.

## Root Cause
- The issue likely started after the update to Ubuntu 18.04 on 03.12.2018.
- AppArmor configuration was not properly set for the user's home directory under `/home.local/`.

## Solution
- HPC Admin adjusted the AppArmor configuration to accommodate the user's home directory location.
- User was advised to disable KDE ActivityManager through KDE system settings to reduce unnecessary log entries.

## General Learnings
- Updates to the operating system can cause compatibility issues with existing software configurations.
- AppArmor configurations need to be adjusted for non-standard home directory locations.
- KDE services can be started in xfce4-sessions due to systemd-DBUS, causing unnecessary log entries and resource usage.

## Steps for Similar Issues
1. Check if the issue started after a recent update.
2. Verify AppArmor configurations for the user's home directory.
3. Adjust AppArmor settings if necessary.
4. Advise the user to disable unnecessary KDE services through KDE system settings if they are causing issues in an xfce4-session.
---

### 2022111942000048_Probleme%20beim%20Einloggen%20auf%20cshpc%20mit%20NoMachine.md
# Ticket 2022111942000048

 ```markdown
# HPC Support Ticket: Login Issues with NoMachine

## Keywords
- NoMachine
- Login issues
- Virtual desktop
- Custom session
- KDE session
- Patches and reboot
- Trinity

## Problem Description
- User unable to login to HPC via NoMachine.
- New virtual desktop created upon login, losing previous settings.
- Custom session option leads to a black screen and connection reset.

## Root Cause
- Recent patches and system reboot caused issues with NoMachine.
- Trinity session not functioning correctly.

## Solution
- Use KDE session type as a workaround.
- Issue with Trinity session was resolved by HPC Admins.

## Lessons Learned
- System updates and reboots can cause temporary issues with remote login tools like NoMachine.
- Specific session types (e.g., KDE) can be used as a temporary workaround.
- Communication with HPC Admins is crucial for resolving such issues.
```
---

### 42132811_Probleme%20bei%20Gnuplot.md
# Ticket 42132811

 ```markdown
# HPC-Support Ticket: Probleme bei Gnuplot

## Problem Description
- **User Issue**: Gnuplot crashes with the error message "X connection to localhost:17.0 broken (explicit kill or server shutdown)" when plotting large files (>100 MB).
- **Affected Systems**: Woody, LiMa
- **User Environment**: Windows with NX for remote access

## Troubleshooting Steps
1. **Initial Investigation**:
   - User reported that the issue only occurs with large files.
   - Other X-Window-Manager programs work fine.

2. **Admin Response**:
   - Requested user to provide the exact Gnuplot commands and the output of `limit` and `ulimit -a`.

3. **User Feedback**:
   - User identified that the issue occurs with the `with lines` option in Gnuplot.
   - Simple plot commands work without issues.

4. **Admin Reproduction**:
   - Admin reproduced the issue using NX and the `with lines` option.
   - No issue when connecting directly via SSH from a Linux machine.

5. **Workarounds**:
   - Using Gnuplot module 4.2.5 on Woody resolved the issue.
   - Direct SSH connection from a Linux machine also resolved the issue.

## Solution
- **Workaround 1**: Use Gnuplot module 4.2.5 on Woody.
- **Workaround 2**: Connect directly via SSH from a Linux machine instead of using NX.

## Keywords
- Gnuplot
- X connection error
- Large files
- NX
- SSH
- Woody
- LiMa

## General Learning
- **Root Cause**: The issue is related to the combination of NX and the `with lines` option in Gnuplot, particularly with large files.
- **Solution**: Using a different Gnuplot version or connecting directly via SSH can resolve the issue.
```
---

### 2020050542001525_Probleme%20Verbindung%20HPC%20mit%20NoMachine.md
# Ticket 2020050542001525

 # HPC Support Ticket: Connection Issue with NoMachine on Mac

## Keywords
- NoMachine
- Mac
- Black screen
- Connection issue
- Trinity/TDE
- Minor update
- starttde script
- Autodetection

## Problem Description
- User experiences a black screen and connection drop when trying to connect to HPC using NoMachine on a Mac.
- Issue started on Monday.

## Root Cause
- Minor update of Trinity on 30.04. changed the way the 'starttde' script searches for Trinity binaries.
- The script was searching in `/usr/bin/` instead of the correct path `/opt/trinity/bin`.

## Troubleshooting Steps
- Checked server logs for meaningful errors.
- Verified user's quota in their home directory.
- Terminated any leftover processes from previous sessions.
- Investigated potential issues with login scripts (.profile, .bashrc, .cshrc).

## Solution
- Hardcoded the correct path `/opt/trinity/bin` in the `/usr/bin/starttde` script to fix the broken autodetection.
- Confirmed the issue was resolved after the fix.

## Notes
- The issue affected only new sessions started after the update on 30.04. at 08:12.
- The autodetection logic in the `starttde` script currently works only if Trinity is the default window manager.
- The fix might be temporary as future updates could revert the changes.

## Follow-up
- Monitor for similar issues after future updates.
- Consider reporting the autodetection bug to Trinity maintainers for a permanent fix.
---

### 2019061142000953_Probleme%20mit%20noMachine%20am%20cshpc.md
# Ticket 2019061142000953

 ```markdown
# HPC-Support Ticket: Problem with noMachine on cshpc

## Keywords
- noMachine
- cshpc
- White screen
- Maintenance
- Desktop environment (KDE, GNOME)
- Virtual desktop

## Problem Description
After logging into the cshpc dialog server via noMachine and starting the recommended resource-saving custom desktop ("starttde" + "run on a virtual desktop"), a white screen appears in noMachine. This issue occurs regardless of the chosen desktop environment (KDE, GNOME). The problem started after maintenance on the cshpc.

## Root Cause
The issue is likely related to the recent maintenance performed on the cshpc, which may have affected the noMachine configuration or the desktop environments.

## Solution
No specific solution was provided in the conversation. Further investigation by the HPC Admins is required to identify and resolve the issue.

## General Learnings
- Maintenance activities can impact the functionality of remote desktop tools like noMachine.
- It is important to test remote desktop tools after maintenance to ensure they are functioning correctly.
- Users should report any issues promptly to the HPC support team for quick resolution.
```
---

### 2023112342003026_Interactive%20GUI%20Mode.md
# Ticket 2023112342003026

 # HPC Support Ticket: Interactive GUI Mode for StarCCM+

## Keywords
- Interactive GUI Mode
- StarCCM+
- Post-processing
- Login Nodes
- NoMachineNX
- SSH Option "-X"
- X11-forwarding

## Problem
- User wants to use StarCCM+ 2020.2 for post-processing on the cluster to avoid downloading large amounts of data.
- User couldn't find documentation on how to access and use the GUI mode for StarCCM+ on the cluster.

## Root Cause
- Lack of clear documentation for using StarCCM+ in interactive GUI mode on the cluster.
- Current cluster setup does not support GUI post-processing for large simulation cases.

## Solution
- **For small simulation cases:**
  1. Use NoMachineNX to connect to the cluster with a virtual desktop.
  2. Open a shell in the virtual desktop and connect to the login node with `ssh -X meggie`.
  3. Load the Star-CCM+ module and start the application with `starccm+ -power -podkey $PODKEY`.

## General Learnings
- The login nodes are shared among all users, and running resource-intensive applications can impact others.
- GUI post-processing over SSH may be slow due to data transmission.
- The cluster is not currently optimized for GUI post-processing of large simulation cases.
- A visualization node is being planned for the cluster, but the ETA is unknown.

## Documentation Reference
- [StarCCM+ Documentation](https://hpc.fau.de/systems-services/documentation-instructions/special-applications-and-tips-tricks/star-ccm/)
- [NoMachineNX Setup](https://hpc.fau.de/systems-services/documentation-instructions/clusters/dialogserver/)
---

### 2024011742000218_cshnr%20RDP-Verbindung%20rei%C3%83%C2%9Ft%20ab%20bei%20hohen%20Aufl%C3%83%C2%B6sungen.md
# Ticket 2024011742000218

 ```markdown
# HPC-Support Ticket: RDP Connection Drops at High Resolutions

## Keywords
- RDP
- xfreerdp
- High Resolution
- Connection Drop
- Ubuntu 22.04
- csnhr

## Problem Description
- User experiences RDP connection drops when using high resolutions (3000x2000 or more) on csnhr.
- Connection works initially but drops during complex tasks that involve significant pixel changes.
- Error messages indicate transport layer issues and network disconnects.
- Lower resolutions (e.g., Full HD) work without issues.
- xfreerdp works fine with 4K resolution on another server (moloch).

## Root Cause
- The root cause appears to be related to the handling of high-resolution data over the RDP connection, potentially due to network or server limitations.

## Solution
- No solution provided in the conversation.
- Further investigation by HPC Admins is required.

## General Learnings
- High-resolution RDP sessions can be unstable and may drop connections during intensive tasks.
- Different servers may handle high-resolution RDP sessions differently.
- Error messages related to transport layer and network disconnects can indicate issues with high-resolution data handling.
```
---

### 2024031442001559_Frage%20zu%20GUI%20in%20NoMachine.md
# Ticket 2024031442001559

 ```markdown
# HPC Support Ticket: Frage zu GUI in NoMachine

## Keywords
- NoMachine
- Matlab
- GUI
- SSH
- X11 Forwarding

## Problem Description
The user was unable to open the graphical user interface (GUI) of Matlab on the HPC cluster via NoMachine. The user logged into the cluster using NoMachine, opened a terminal, and used `ssh -X` to connect to the HPC node. Despite loading the Matlab module and starting Matlab, only the terminal interface was available.

## Root Cause
The issue was related to the use of `ssh -X` for X11 forwarding, which did not enable the graphical interface for Matlab.

## Solution
The user was advised to use `ssh -Y` instead of `ssh -X` for X11 forwarding. This change allowed the graphical interface of Matlab to open correctly.

## What Can Be Learned
- **X11 Forwarding Options**: The difference between `ssh -X` and `ssh -Y` for X11 forwarding. `ssh -Y` is more permissive and can be used to enable graphical interfaces that `ssh -X` might restrict.
- **Terminal Usage**: Ensure that the terminal used for SSH connections is opened within the NoMachine session to enable graphical output.

## Additional Notes
- The HPC Admin confirmed that the described procedure should work as expected and suggested verifying that the terminal is opened within the NoMachine session.
- The solution was found in another support ticket (Ticket#2024031142003768).
```
---

### 2024070942004335_Star%20CCM%20Display%20variable.md
# Ticket 2024070942004335

 # HPC Support Ticket: Star CCM Display Variable Issue

## Keywords
- Star CCM+
- DISPLAY variable
- X-Forwarding
- SSH
- NoMachine
- xRDP
- Cache issues

## Summary
The user encountered a warning message indicating that the `DISPLAY` environment variable was not set when attempting to run Star CCM+ on the HPC cluster. This issue prevented the GUI from displaying correctly.

## Root Cause
- The `DISPLAY` variable was not set, which is required for GUI applications to function properly.
- Potential cache issues or "leftovers" from previous crashes of Star CCM+ were suspected to cause the problem.

## Troubleshooting Steps
1. **Initial Response**:
   - The HPC Admin confirmed that the `DISPLAY` variable is not set by default and that X-Forwarding needs to be explicitly enabled.
   - The user clarified that the GUI was not displaying and the application was unusable.

2. **Further Investigation**:
   - The user provided details on their login method (NoMachine and KDE Desktop) and the steps they followed to start the GUI.
   - The HPC Admin suggested checking for cache issues in directories like `~/.star`, `~/.local`, and `~/.cache`.

3. **Additional Information**:
   - The user discovered that switching frontend nodes without restarting the SSH session caused the issue to reappear.
   - The user confirmed that the `DISPLAY` variable was set correctly when checked with `echo $DISPLAY`.

## Solution
- The user found that restarting the SSH session resolved the issue temporarily.
- The HPC Admin suggested that the migration from NoMachine to xRDP might help in the future.
- The user was advised to check for and clean up any cache issues that might be causing the problem.

## Conclusion
The issue was likely caused by cache or session-related problems. Restarting the SSH session and checking for cache issues were effective troubleshooting steps. The migration to xRDP was also noted as a potential future solution.

## References
- [Migration to xRDP](https://hpc.fau.de/2024/06/06/dialog-server-cshpc-to-be-decommissioned-nomachine-nx-to-be-replaced-by-xrdp/)
---

### 2023062642002701_Datenupload%20in%20URL.md
# Ticket 2023062642002701

 # HPC Support Ticket: Datenupload in URL

## Keywords
- Datenupload
- Swiftbrowser
- DKRZ
- NoMachine
- KDE
- GNOME
- Firefox
- Konqueror
- Python Swiftclient
- Authentifizierung
- .profile
- Windows OS

## Problem
- User wants to upload a large scientific dataset (~450GB) from the HPC cluster to the DKRZ Swiftbrowser.
- Initial attempts using wget and curl resulted in "Forbidden" messages.
- User tried using NoMachine to access a browser on the HPC cluster, but encountered issues with KDE and GNOME desktop environments not loading properly.
- Only Konqueror browser worked, but it did not display the Swiftbrowser website correctly.

## Root Cause
- The user's .profile file contained errors that prevented KDE from starting properly.
- The user's Windows OS might have contributed to the issues with NoMachine.

## Solution
- HPC Admins suggested renaming the .profile file to resolve the KDE startup issue.
- After renaming the .profile file, KDE started successfully, and the user was able to use Firefox to access the Swiftbrowser website.
- The user successfully uploaded the dataset to the DKRZ Swiftbrowser.

## General Learnings
- Always check for errors in the .profile file when encountering desktop environment startup issues.
- NoMachine can be used to access a browser on the HPC cluster for data uploads.
- The Python Swiftclient can be used for data uploads to the DKRZ Swiftbrowser, but proper authentication is required.
- When encountering issues with NoMachine, try using a different desktop environment or check for OS-specific issues.

## Success Story
- The user successfully uploaded a large scientific dataset to the DKRZ Swiftbrowser using the HPC cluster and NoMachine.
- The dataset will be published and made available for long-term storage.
- The user expressed gratitude for the support provided by the HPC Admins.
---

### 2018090942000311_OS%20non%20responsive.md
# Ticket 2018090942000311

 ```markdown
# HPC Support Ticket: OS Non-Responsive

## Keywords
- Ubuntu
- NoMachine
- Unresponsive
- SysRq
- Reboot
- nxserver

## Problem Description
The user's Ubuntu operating system on NoMachine became unresponsive. The desktop screen was stuck, and the user could not open anything. The user tried to create a new connection but it did not resolve the issue. The user did not have the SysRq (Print Screen) key on their MacBook, making it difficult to reboot the system via keyboard.

## Root Cause
The exact root cause of the unresponsive OS was not explicitly identified, but it was likely related to a NoMachine session issue.

## Solution
The user managed to unfreeze the system without specifying the exact steps taken. The HPC Admin closed the ticket after confirming the system was responsive again. The admin used the following commands to list and kill NoMachine sessions:
```bash
/usr/NX/bin/nxserver --list mfhe000h
/usr/NX/bin/nxserver --kill 8ED46A7388D17EF6AE794EB8E303B29F
```

## General Learnings
- NoMachine sessions can sometimes become unresponsive.
- Users without a SysRq key may face difficulties rebooting the system via keyboard.
- Listing and killing NoMachine sessions using `nxserver` commands can help resolve unresponsive sessions.
- It is useful to document steps taken to unfreeze the system for future reference.
```
---

### 2019061042000955_NoMachine.md
# Ticket 2019061042000955

 ```markdown
# HPC Support Ticket: NoMachine Connection Issue

## Keywords
- NoMachine
- Connection Issue
- White Screen
- Ghost Session
- .nx Directory

## Problem Description
- User unable to connect to HPC via NoMachine; screen remains white after initial steps.

## Root Cause
- Ghost session with orphaned processes.

## Troubleshooting Steps
1. **Kill Ghost Session Processes**: HPC Admin identified and terminated orphaned processes.
2. **Delete .nx Directory**: User was advised to delete the `.nx` directory in their home directory.

## Solution
- After terminating the ghost session processes and deleting the `.nx` directory, the issue was resolved.

## General Learnings
- Ghost sessions can cause connection issues in NoMachine.
- Deleting the `.nx` directory can help resolve NoMachine connection problems.
- Regularly check for and terminate orphaned processes to prevent similar issues.
```
---

