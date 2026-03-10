# Topic 42: visualization_paraview_vnc_node_viewer

Number of tickets: 8

## Tickets in this topic:

### 2018102542001938_Paraview%20in%20cluster.md
# Ticket 2018102542001938

 # HPC Support Ticket: Paraview in Cluster

## Keywords
- Paraview
- Openfoam Simulation
- Star CCM+
- X-forwarding
- Interactive job
- Graphics libraries
- VirtualGL
- CUDA
- GPU

## Problem
- User has large mesh files for Openfoam simulation and Star CCM+ that cannot be viewed on their local PC due to insufficient RAM.
- User wants to use Paraview on the HPC cluster to view these files but encounters issues with missing graphics libraries.

## Root Cause
- The compute nodes on the cluster are missing some graphics-related libraries required by Paraview.
- The user is not specifying the correct node type in their qsub command.

## Solution
- Use the following qsub command to request an interactive job with X-forwarding on a node with the required graphics libraries:
  ```
  qsub -I -X -lnodes=1:ppn=40:phi2x,walltime=01:00:00
  ```
- Load the Paraview module and start Paraview:
  ```
  module load paraview
  paraview
  ```

## Additional Notes
- VirtualGL is not recommended due to compatibility issues with CUDA.
- For Windows users, an X server is required locally, or NoMachine NX can be used as an alternative for the initial connection.
- Compute- or memory-intensive applications are not allowed on the login nodes.

## Related Links
- [NoMachine NX Guide](https://www.anleitungen.rrze.fau.de/hpc/dialogserver/)
- [VirtualGL and CUDA Compatibility Issue](https://servicedesk.gauss-allianz.de/otrs/index.pl?Action=AgentTicketZoom;TicketID=2073)
---

### 2023111342003214_VTK%20visualization%20-%20b159cb11.md
# Ticket 2023111342003214

 ```markdown
# HPC Support Ticket: VTK Visualization

## Keywords
- VTK Visualization
- Visualization Node
- Fritz Cluster
- Sbatch
- VNC
- Port Forwarding
- Job Submission
- Pending Jobs

## Summary
A user requested access to the visualization node to create 3D visualizations using VTK for turbulence simulations. The user encountered issues with job submission and accessing the visualization node.

## Issues and Solutions

### Issue 1: Access to Visualization Node
- **Problem**: User requested access to the visualization node for VTK visualizations.
- **Solution**: HPC Admins provided access to the visualization node and instructions for using it.

### Issue 2: Job Submission Error
- **Problem**: User encountered an error when submitting a job using `sbatch /apps/virtualgl/startvnc.slurm`.
- **Error Message**: `sbatch: error: Batch job submission failed: Invalid account or account/partition combination specified`.
- **Solution**: The visualization queue had access control enabled, which was later removed. The user was advised to try again.

### Issue 3: Job Remains Pending
- **Problem**: User's job remained in "PENDING" state and was not visible in `squeue`.
- **Solution**: The issue was noted, and the user was advised to check the documentation and try again.

## General Learnings
- The visualization node is experimental and may have issues not yet encountered by other users.
- Documentation for the visualization node is available but may be incomplete.
- Users should check the slurm-output file for VNC display and password information.
- Port forwarding is required to access the visualization node from a local machine.
- The visualization node may have access control enabled, which can cause job submission errors.

## Documentation
- [Fritz Cluster Documentation](https://hpc.fau.de/systems-services/documentation-instructions/clusters/fritz-cluster/#remotevis)

## Next Steps
- Users should report any issues encountered while using the visualization node.
- HPC Admins should continue to update and improve the documentation for the visualization node.
```
---

### 2022102042001617_Query%20related%20to%20Remote%20Visualization.md
# Ticket 2022102042001617

 # HPC Support Ticket: Remote Visualization

## User Query
- **User ID:** iwtm040h
- **Issue:** Remote visualization task using Paraview with large files.
- **Dataset Size:** 6.9 GB
- **Problem:** Slow loading and updating of features in Paraview.

## HPC Admin Responses

### Initial Setup
- **Visualization Node:** Alex cluster.
- **Steps:**
  1. Login to Alex (`ssh alex.nhr.fau.de`).
  2. Submit VNC job (`sbatch /apps/virtualgl/startvnc.slurm`).
  3. Check output for VNC display and password.
  4. Setup SSH tunnel and start VNC viewer.
  5. Load Paraview module in VNC session.

### Troubleshooting
- **Issue:** VNC session terminal not opening on Ubuntu 20.
  - **Solution:** Try another VNC application like Remina.
- **Issue:** Slow data loading in Paraview.
  - **Solution:** Copy dataset to local NVMe SSD (`/scratch`).

### Performance Improvement
- **Issue:** Sequential data processing in Paraview.
  - **Solution:** Use Paraview server for parallel processing (not recommended on HPC due to security concerns).
- **Issue:** Large number of small files.
  - **Solution:** Reduce file count by writing one large file per timestep. Consider using HDF5 format.

### Additional Notes
- **VirtualGL:** Not necessary if using TurboVNC only as a client.
- **Dataset Location:** Path provided for further analysis.

## Conclusion
- **Root Cause:** Sequential data processing and large number of small files.
- **Solution:** Use local NVMe SSD, consider Paraview server for parallel processing, and reduce file count.

---

This documentation provides a summary of the support ticket, including the user's query, the steps taken by HPC admins, troubleshooting, performance improvement suggestions, and the final conclusion.
---

### 2022122142002076_Programm%20zum%20Bilder%20ansehen%20auf%20Fritz%20login-Knoten.md
# Ticket 2022122142002076

 # HPC Support Ticket: Image Viewer Request on Login Node

## Keywords
- Image viewer
- Login node
- gwenview
- GraphicsMagick
- ImageMagick
- RHEL8
- KDE dependency

## Summary
A user requested an image viewer to be installed on the login node to quickly view images (png, jpeg, etc.). The user mentioned that `gwenview` was previously available on another system.

## Root Cause
The user needed a simple image viewer on the login node to quickly view images.

## Discussion
- **HPC Admin**: Noted that `gwenview` has extensive KDE dependencies, which is not ideal.
- **HPC Admin**: Suggested `GraphicsMagick` or `ImageMagick` as alternatives.
- **HPC Admin**: Preferred `ImageMagick` due to its additional tools for image conversion.

## Solution
- **HPC Admin**: Installed `GraphicsMagick` on the login node.
- **Usage**: Users can view images using the command `gm display *png`.

## Conclusion
The user's request was addressed by installing `GraphicsMagick`, which provides a simple image viewer and additional tools for image manipulation.

## Additional Notes
- The solution was implemented considering the minimal dependencies and additional functionalities provided by `GraphicsMagick`.
- This ticket can serve as a reference for future requests for image viewers on login nodes.
---

### 2023071442002203_Paraview%20Server%20-%20iwia007h.md
# Ticket 2023071442002203

 # HPC Support Ticket: Paraview Server Request

## Keywords
- Paraview Server
- Visualization
- VTK Data
- Large Files
- System Crash
- Visualization Server
- Fritz Cluster
- Module Load

## Problem
- User experiencing crashes when visualizing large VTK files (~20GB) locally using Paraview.
- Requesting access to a Paraview server on RRZE/NHR@FAU systems for better performance.

## Solution
- HPC Admins informed the user that there are no immediate plans for a dedicated Paraview server.
- Offered access to the visualization server in the Fritz cluster, which is in test operation.
- Provided instructions to load the Paraview module: `module load paraview/5.11.2`.
- Documentation available at: [Fritz Cluster Documentation](https://hpc.fau.de/systems-services/documentation-instructions/clusters/fritz-cluster/#remotevis).

## General Learnings
- Large data visualization issues can be addressed using HPC resources.
- Visualization servers integrated into HPC clusters can handle large datasets more effectively.
- Users should be directed to relevant documentation and module loading instructions for visualization tools.
- Continuous communication and updates on server availability are crucial for user satisfaction.
---

### 2022021442002009_Regarding%20the%20visualization%20node%20at%20Fritz%20cluster.md
# Ticket 2022021442002009

 # HPC-Support Ticket: Visualization Node at Fritz Cluster

## Keywords
- Visualization Node
- Remote Visualization
- VNC
- TurboVNC
- xvfb
- GUI-based File Browser
- Image Viewer
- Access Request

## Summary
A user inquired about using the visualization node at the Fritz cluster for remote visualization of simulation results. The HPC Admin provided detailed steps for setting up and using the visualization node via VNC. The user also requested additional tools and access for a colleague.

## Root Cause of the Problem
- Physical network link issues with the visualization node.
- User needed GUI-based file browser and image viewer.
- User required xvfb for preprocessing tasks.
- Access request for a colleague.

## Solution
1. **Network Link Issue:**
   - The HPC Admin informed the user about the network link issue and later notified when the visualization node was back online.

2. **Setting Up VNC:**
   - Detailed steps were provided for setting up and using the visualization node via VNC.
   - Steps included logging into Alex, submitting a job script, configuring SSH tunneling, and using TurboVNC.

3. **GUI-based File Browser and Image Viewer:**
   - The HPC Admin offered to install usable tools from RHEL8/AlmaLinux8 on the visualization node if available.

4. **xvfb Installation:**
   - The HPC Admin mentioned they would check if xvfb and its dependencies could be included in future node images.

5. **Access Request:**
   - The HPC Admin enabled access for the user's colleague on Alex.

## Steps for Setting Up VNC
1. Login to Alex.
2. Submit the job script: `sbatch /apps/virtualgl/startvnc.slurm`.
3. Check the generated `startvnc.slurm.o*` for the VNC display number.
4. Configure SSH tunneling:
   - Within the university network: `ssh -L 5901:localhost:59xx HPCACCOUNT@atest01.nhr.fau.de`.
   - Outside the university network: `ssh -L 5901:localhost:59xx -J YOURHPCACCOUNT@cshpc.rrze.fau.de YOURHPCACCOUNT@atest01.nhr.fau.de`.
5. Start TurboVNC on the local machine and use `localhost:1` as the display.
6. Enter the one-time password provided in the `startvnc.slurm.o*` file.
7. Terminate the VNC session using the Start menu to free resources on the batch node.

## Additional Notes
- The user reported no issues using the visualization node on a machine with Ubuntu 20.04.
- Colleagues reported failures using old MacOS versions or Linux with GNOME on Wayland.

## Conclusion
The HPC Admin provided comprehensive support for setting up and using the visualization node, addressing the user's requests for additional tools and access. The user was able to use the visualization node without issues.
---

### 2024101442004641_Data%20visualisation%20Alex%20Cluster.md
# Ticket 2024101442004641

 ```markdown
# HPC Support Ticket: Data Visualisation on Alex Cluster

## Keywords
- Data Visualisation
- Paraview
- Alex Cluster
- Fritz Cluster
- Tier3 Grundsicherung
- CFD Simulations

## Problem
- User has an account for the Alex Cluster and wants to visualise CFD simulation data using Paraview.
- Recommended method is to use Fritz with the fviz1 node, but the user has no access to Fritz.

## Solution
- HPC Admin granted access to Fritz for the user's Alex Cluster account (b238dc12).

## General Learnings
- Users running simulations on Alex Cluster may need access to Fritz for data visualisation.
- Access to Fritz can be granted by HPC Admins upon request.
- Tier3 Grundsicherung application is an alternative method to gain access to Fritz, but direct request to HPC Admins can be simpler and faster.

## Actions Taken
- HPC Admin provided access to Fritz for the user's Alex Cluster account.

## Root Cause
- User lacked access to the Fritz cluster, which is required for data visualisation using Paraview.
```
---

### 2024082342001694_Paraview%20client-server.md
# Ticket 2024082342001694

 # HPC-Support Ticket: Paraview Client-Server Issue

## Subject
Paraview client-server

## User Issue
- User unable to visualize a large Paraview file (20GB) stored on the Lustre file system.
- Server crashes with the warning "WARN| This operation not yet supported for more than 2147483647 objects."
- Remote rendering disabled warning upon connection.

## Troubleshooting Steps
1. **Version Check**:
   - User loaded Paraview version 5.11.2 on both server and local machine.
   - HPC Admin suggested trying different versions (5.12.1, 5.13.0-RC2).

2. **MPI Execution**:
   - User ran `pvserver` with MPI (`mpiexec`).
   - HPC Admin tested with and without MPI, encountering similar issues.

3. **File Testing**:
   - User generated large and small files for testing.
   - HPC Admin tested these files and encountered freezing issues with both.

4. **Bug Report**:
   - HPC Admin identified a potential bug in Paraview's XdmfReader.
   - Bug reported to Paraview repository on GitLab.

## Root Cause
- Potential bug in Paraview's XdmfReader when used with MPI in server+client mode.

## Solution
- Temporary workaround: Use other file formats until the bug is fixed.
- Follow the progress of the issue on GitLab.

## Keywords
- Paraview
- XdmfReader
- MPI
- Remote rendering
- Bug report
- File format

## Conclusion
- The issue is currently unresolved and awaiting a fix from Paraview developers.
- Ticket will be reopened upon progress from Paraview developers.
---

