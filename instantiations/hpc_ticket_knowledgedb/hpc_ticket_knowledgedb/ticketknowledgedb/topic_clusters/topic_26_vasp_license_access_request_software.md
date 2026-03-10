# Topic 26: vasp_license_access_request_software

Number of tickets: 29

## Tickets in this topic:

### 2022032442000277_WG%3A%20VASP%20license%20on%20HPC.md
# Ticket 2022032442000277

 # HPC Support Ticket: VASP License on HPC

## Keywords
- VASP license
- HPC clusters
- Eligibility
- Cost
- Central VASP installation

## Summary
A user inquired about the VASP license requirements and cost for using VASP on HPC clusters.

## Root Cause
- User needed information on VASP license requirements and cost for a master student to use VASP on HPC.

## Information Provided
- VASP installation is available on specific HPC clusters (e.g., Fritz and Alex) for eligible users.
- Eligibility requires the chair to have a VASP license and the user's email to be listed with the VASP developers.
- Users must fill out a form to request access to the central VASP installation.
- The cost of a VASP license is approximately 5k EUR for a chair with 6 users, and it is a one-time fee for each VASP release.

## Solution
- Users should fill out the form at [HPC VASP Request Form](https://hpc.fau.de/systems-services/systems-documentation-instructions/special-applications-and-tips-tricks/vasp/request-access-to-central-vasp-installation/) to verify eligibility.
- Users should ensure their chair has a VASP license and their email is listed with the VASP developers.

## General Learning
- VASP access on HPC clusters requires specific eligibility criteria and a one-time license fee.
- Users must follow the provided form to request access and verify their eligibility.
- The cost and licensing details are important considerations for users planning to use VASP on HPC clusters.
---

### 2024061942001642_namd.md
# Ticket 2024061942001642

 ```markdown
# HPC Support Ticket: NAMD Access Request

## Keywords
- NAMD
- VMD
- Access Request
- License Agreement
- Account Activation

## Summary
A user requested access to NAMD and VMD software on the HPC system. The user confirmed that they have accepted the license agreements on the NAMD/VMD download website.

## Root Cause
The user needed access to NAMD and VMD software but was not yet authorized.

## Solution
The HPC Admin activated the user's account (bco123) for NAMD and VMD on the HPC system.

## What Can Be Learned
- Users need to request access to specific software like NAMD and VMD.
- Users must confirm that they have accepted the license agreements for the software.
- HPC Admins can activate user accounts for specific software upon request.
```
---

### 2024100442002625_Compiling%20vasp%20with%20DFT-D4%20external%20package.md
# Ticket 2024100442002625

 # HPC Support Ticket: Compiling VASP with DFT-D4 External Package

## Keywords
- VASP
- DFT-D4
- Compilation
- Module Installation
- Error Handling

## Summary
A user requested assistance with compiling VASP 6.4.3 with the DFT-D4 external package to enable the DFT-D4 method for their calculations. The HPC admins provided information on existing modules and worked towards resolving the issue.

## Problem
- **User Request:** The user needed VASP 6.4.3 compiled with the DFT-D4 library to use the DFT-D4 method in their calculations.
- **Existing Solution:** An existing VASP module (vasp6/6.3.0-hybrid-intel-impi-AVX2-with-addons) was available with D3 enabled, but the user preferred version 6.4.3 for consistency.

## Steps Taken
1. **Initial Response:** The HPC admin informed the user about the existing VASP module with D3 enabled and inquired if version 6.3.0 was acceptable.
2. **User Clarification:** The user insisted on using VASP 6.4.3 with DFT-D4.
3. **Forwarding the Ticket:** The ticket was forwarded to the colleague responsible for VASP modules, who was on leave.
4. **Module Installation:** A new VASP module (vasp6/6.4.3-hybrid-intel-impi-AVX512-with-addons) was compiled with DFT-D4 and other necessary libraries.
5. **Error Encountered:** The user encountered errors when running the new module.
6. **Error Analysis:** The HPC admin acknowledged the error and mentioned it might be a bug in the compilers or software, requiring further investigation.

## Solution
- **Module Provided:** A new VASP module (vasp6/6.4.3-hybrid-intel-impi-AVX512-with-addons) was compiled with DFT-D4 and other libraries.
- **Error Handling:** The HPC admin acknowledged the error and planned to investigate further, indicating it might be a bug in the compilers or software.

## Lessons Learned
- **Communication:** Clear communication between the user and HPC admins is crucial for understanding the user's requirements and providing appropriate solutions.
- **Module Management:** Keeping track of available modules and their features helps in quickly addressing user requests.
- **Error Handling:** Some errors may require deeper investigation and might be related to bugs in the software or compilers.

## Next Steps
- **Error Resolution:** Further investigation is needed to resolve the illegal memory access error encountered by the user.
- **Module Update:** Ensure that the new VASP module is stable and functional for the user's calculations.

## Conclusion
The HPC support team worked collaboratively to address the user's request for a VASP module with DFT-D4 enabled. While a new module was provided, further investigation is needed to resolve the encountered errors.
---

### 2020101542003209_VASP%20request%20of%20bco132%20-%205-319.md
# Ticket 2020101542003209

 ```markdown
# HPC Support Ticket: VASP Access Request

## Keywords
- VASP access
- License verification
- Software installation
- User authorization

## Summary
A user requested access to VASP (Vienna Ab initio Simulation Package) for their HPC account. The HPC Admin verified the license and sought authorization from the primary license contact.

## Problem
- User requested access to VASP version 5.
- HPC Admin needed to verify the license and obtain authorization.

## Solution
- HPC Admin contacted the primary license contact to confirm the user's access.
- Authorization was granted, allowing the user access to VASP.

## Lessons Learned
- Always verify software licenses before granting access.
- Communicate with the primary license contact for authorization.
- Ensure that license agreements and access permissions are up-to-date.

## Actions Taken
1. User submitted a request for VASP access.
2. HPC Admin verified the license and contacted the primary license contact.
3. Authorization was granted, and the user was given access to VASP.

## Notes
- The primary license contact confirmed that members of a VASP5-only group could temporarily access VASP6 for promotional purposes.
- Ensure that all HPC centers are informed about any changes in license agreements or access permissions.
```
---

### 2020090742000284_VASP%20request%20of%20unrz008h%20-%20WA20-0012.md
# Ticket 2020090742000284

 ```markdown
# HPC-Support Ticket: VASP Access Request

## Keywords
- VASP access
- License management
- User request
- HPC account
- Institutional license

## Summary
A user requested access to VASP (Vienna Ab initio Simulation Package) for their HPC account. The request included details such as the user's name, email, institution, and license number. The HPC Admin noted that no further inquiry in Vienna was necessary as the license account is managed by the HPC team.

## What Can Be Learned
- **User Request Process**: Understanding the process for users to request access to specific software packages like VASP.
- **License Management**: How licenses are managed and verified by the HPC team.
- **Institutional Collaboration**: The importance of institutional collaboration in managing software licenses.

## Root Cause
The user needed access to VASP for their research, and the request was handled internally by the HPC team.

## Solution
The HPC Admin confirmed that the license account is managed by the HPC team, and no further action was required from Vienna. The request was processed internally.
```
---

### 2025022042002671_Bitte%20VASP%20f%C3%83%C2%BCr%20mpsa101h%20freischalten.md
# Ticket 2025022042002671

 # HPC Support Ticket: VASP Access Request

## Keywords
- VASP
- License
- Access Request
- Home Directory
- Slurm
- Tier3 Grundversorgung

## Summary
A user requested VASP access for a new employee. The HPC Admin guided the user through the necessary steps to enable VASP access.

## Root Cause
- The new employee was not listed under any VASP license.
- The user was unaware of the specific procedure to request VASP access.

## Steps Taken
1. **Initial Request**: The user requested VASP access for a new employee who was recently added to their Tier3 Grundversorgung.
2. **Admin Response**: The HPC Admin informed the user that the new employee was not listed under any VASP license and provided a link to the VASP access request form.
3. **User Action**: The user filled out the VASP access request form with the necessary details, including the license number and requested versions.
4. **Admin Action**: The HPC Admin processed the request and enabled VASP access for the new employee.
5. **Follow-up**: The HPC Admin informed the user that the home directory and Slurm access would be available the day after accepting the invitation.

## Solution
- Ensure that new employees are listed under the appropriate VASP license.
- Fill out the VASP access request form with the required details.
- Wait for the HPC Admin to process the request and enable access.
- Note that the home directory and Slurm access will be available the day after accepting the invitation.

## Documentation Links
- [VASP Access Request Form](https://hpc.fau.de/request-access-to-central-vasp-installation/)
- [HPC Portal User Tab Documentation](https://doc.nhr.fau.de/hpc-portal/#the-user-tab)

## Notes
- The user was already aware that the home directory and Slurm access would take some time to be set up.
- The HPC Admin provided clear instructions and documentation links to guide the user through the process.
---

### 2025013142001537_VASP%20access.md
# Ticket 2025013142001537

 # HPC Support Ticket: VASP Access

## Keywords
- VASP
- License number
- Primary VASP license contact
- NHR@FAU
- Installation license
- Execution license

## Problem
- User needs access to VASP for experiments.
- User does not have a license number or primary VASP license contact email.
- User's email is not registered with VASP.
- User is a member of NHR@FAU.

## Root Cause
- NHR@FAU only holds an installation license for VASP, not an execution license.

## Solution
- User cannot access VASP through NHR@FAU due to lack of execution license.
- User needs to obtain a VASP execution license or find an alternative solution.

## General Learning
- Understand the difference between installation and execution licenses.
- NHR@FAU's VASP installation license does not grant execution rights.
- Users must have the appropriate license and contact information to access VASP.
---

### 2024022942003674_VASP%20on%20NHR%40FAU.md
# Ticket 2024022942003674

 # HPC-Support Ticket Conversation Summary

## Subject: VASP on NHR@FAU

### User Request
- **User**: Requested access to VASP on NHR@FAU for noncollinear Spin-Orbit DFT calculations.
- **Licenses**: Provided VASP license details (21-0363 and WA20-0017 5-328).
- **Requirements**: VASP without flags `-DNGXhalf` and `-DNGZhalf`.

### HPC Admin Response
- **Access Granted**: User was granted access to VASP modules.
- **Executable Availability**: Confirmed availability of VASP executables without the specified flags.
- **Directory Information**: Provided directory path for `makefile.include`.

### User Follow-Up
- **Issue**: VASP job not using all cores due to SLURM changes.
- **Solution**: Add `export SRUN_CPUS_PER_TASK=$SLURM_CPUS_PER_TASK` to job script.

### HPC Admin Analysis
- **Performance Issue**: Identified suboptimal INCAR parameters.
- **Recommendations**:
  - Use larger `NCORE` to reduce memory usage.
  - Adjust `KPAR` and `NPAR` settings.
  - Consider smaller `ENCUT` if possible.
  - Reduce history for DIIS.
  - Evaluate `LREAL` setting.

### User Additional Issues
- **Memory Usage**: High memory usage for 16x16 k-points calculation.
- **Job Restart**: Issues with VASP job restarts.
- **Band Structure Calculation**: Problems with band structure calculation.

### HPC Admin Further Assistance
- **Longer Job Time**: Suggested submitting a request for longer job time via email.
- **Memory Management**: Provided tips for optimizing memory usage.
- **Performance Monitoring**: Used ClusterCockpit to monitor VASP performance.
- **Zoom Meeting**: Scheduled a Zoom meeting for further discussion.

### Final Recommendations
- **Settings**:
  - `KPAR=1`
  - `NCORE=36` or `72`
  - `ALGO=Fast`
- **Estimate Run Time**: Use `grep LOOP OUTCAR` to estimate total run time.
- **Request Longer Job Time**: Submit an email to support-hpc for job time extension if needed.

### Conclusion
- **Root Cause**: Suboptimal INCAR parameters and memory management.
- **Solution**: Adjust VASP settings and request longer job time if necessary.

---

This summary provides a concise overview of the HPC-Support ticket conversation, highlighting key issues, solutions, and recommendations for future reference.
---

### 2022120642003862_VASP%20request%20of%20b158cb14%20-%2020-0414%205-1616.md
# Ticket 2022120642003862

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject
VASP request of b158cb14 - 20-0414 5-1616

## Keywords
- VASP access request
- HPC account
- License number
- VASP 6
- First-time usage
- Certificate expiration

## Summary
A user requested access to VASP 6 for their HPC account. The request included details such as the user's name, email, license number, and institution. The HPC Admin responded by granting access and offering further support.

## Root Cause of the Problem
- Certificate expiration was noted by the HPC Admin.

## Solution
- The HPC Admin granted access to the VASP 6 module and offered additional support if needed.

## General Learnings
- Users need to provide detailed information for VASP access requests, including license numbers and institutional details.
- HPC Admins should check for certificate expiration and ensure that users are granted access to the requested modules.
- Offering additional support through Liaison-Scientists can help first-time users get started with VASP on the HPC system.
```
---

### 2022020842000326_VASP%20request%20of%20bctc38%20-%2020-0186%205-204.md
# Ticket 2022020842000326

 # HPC Support Ticket Analysis: VASP Access Request

## Keywords
- VASP access request
- License number
- Expired certificate
- VASP versions (5, 6)
- HPC account
- Institution details

## Summary
A user requested access to VASP versions 5 and 6 for their HPC account. The request included details such as the user's name, email, institution, and license number. The HPC Admin responded, noting that the certificate had expired and that the user had already been granted access to VASP 6 on a specific system.

## Root Cause
- Expired certificate for VASP access.

## Solution
- The HPC Admin informed the user that they had already been granted access to VASP 6 on one system and mentioned that there is no central VASP installation on other systems.

## General Learnings
- Ensure that certificates for software access are up to date.
- Check if the user has already been granted access to the requested software versions.
- Communicate the availability of software installations across different systems.

## Action Items for Support Employees
- Verify the status of certificates for software access requests.
- Confirm if the user has already been granted access to the requested software.
- Provide information on the availability of software installations on different systems.
---

### 2024020142004019_VASP%206.4%20on%20Alex.md
# Ticket 2024020142004019

 # HPC Support Ticket: VASP 6.4 on Alex

## Keywords
- VASP 6.4
- Alex cluster
- GPU installations
- Machine Learning Force Field (ML-FF) simulations
- NCCL variant
- Module installation

## Problem
- User requires VASP 6.4 for ML-FF simulations on the Alex cluster.
- Current preinstalled VASP version on Alex is 6.3.0.
- User lacks experience with GPU installations.

## Solution
- HPC Admins installed VASP 6.4.2 on Alex.
- Two new modules are available: `vasp6/6.4.2-nccl` and `vasp6/6.4.2-nonccl`.
- NCCL variant should be used with one MPI process per GPU.
- User was informed to contact support if any issues arise.

## General Learnings
- VASP 6.4 significantly improves ML-FF simulation performance.
- Different VASP modules (NCCL, non-NCCL) have varying performance characteristics.
- Proper module selection and usage instructions are crucial for optimal performance.
- HPC Admins can assist with software installations and provide usage guidelines.

## Root Cause
- Lack of the required VASP version (6.4) on the Alex cluster for ML-FF simulations.

## Resolution
- Installation of VASP 6.4.2 modules on the Alex cluster.
- Provision of usage instructions for the new modules.
---

### 2018120342002831_VASP%20%28DFT%29%20auf%20HPC%20Rechnern%20Grundlegende%20FAQs%20zu%20HPC.md
# Ticket 2018120342002831

 # HPC Support Ticket Conversation: VASP (DFT) auf HPC Rechnern

## Keywords
- VASP
- HPC
- Compilation
- Rechenzeit
- Basisdienst
- Schulung

## Summary
A user inquires about using VASP on HPC systems for larger scientific jobs, seeking information on the effort required to transition to HPC, software compilation, resource limitations, and training requirements.

## Root Cause
The user's current workstations are insufficient for their computational needs, leading to longer-than-desired calculation times.

## Solution
1. **Software Compilation**:
   - The user needs to compile VASP themselves or collaborate with another group (e.g., Prof. Görling's group) for a precompiled binary or Makefile.
   - The Emmy-Cluster is recommended as the target system, with necessary compilers, MPI, and MKL available.

2. **Data Retention**:
   - All data in `/home/*` will be retained as long as the HPC account is valid, regardless of active usage.

3. **Resource Limitations**:
   - The HPC-Basisdienst has no immediate resource limitations regarding compute time.
   - There are no unexpected costs; the user will be notified if their activities exceed the free contingent.

4. **Training Requirements**:
   - No mandatory training is required for new HPC users.

## General Learnings
- Users can transition to HPC systems for larger computational tasks without significant initial resource estimation.
- Compilation of software like VASP is typically required, but collaboration with other groups can simplify this process.
- Data retention policies ensure that user data is preserved even during periods of inactivity.
- The HPC-Basisdienst provides flexible resource usage without immediate cost concerns.
- No mandatory training is required for new HPC users, making the transition process more accessible.

## Actions Taken
- A new HPC account (mpfp000h) was created for the user.
- The user was instructed to set a password for the new account via the self-service portal.
- The user was informed that it may take up to 2 days for the services to be fully set up on the HPC servers.

## Notes
- The user was advised to collaborate with Prof. Görling's group for VASP compilation.
- The user's account setup was completed, and they were provided with instructions for initial login and password setup.
---

### 2022060142002179_Tier3-Access-Fritz%20%22Laura%20Ulm%22%20_%20bctc035h.md
# Ticket 2022060142002179

 # HPC Support Ticket Analysis

## Keywords
- HPC Account Activation
- VASP Access
- Certificate Expiration
- Multi-node Workload
- VASP Local Installation
- Reaction Intermediates Optimization
- Liquid Metal Surface Catalysis

## Summary
- **User Request**: Activation of HPC account for multi-node workload with local VASP installation.
- **Issue**: User's certificate has expired, and they are not authorized to use VASP according to the VASP portal.
- **Solution**: HPC Admin activated the user's account but noted the lack of VASP authorization.

## Details
- **User Needs**:
  - Multi-node workload with HDR100 Infiniband and specific node requirements.
  - Local installation of VASP.
  - Application in liquid metal surface catalysis research.
- **Admin Response**:
  - Account activated on Fritz.
  - Notification of lack of VASP authorization.
- **Root Cause**: Expired certificate and lack of VASP authorization.

## Lessons Learned
- Always check certificate validity and software authorization before granting access.
- Ensure users are aware of their software usage permissions.

## Next Steps
- User should renew their certificate.
- User should obtain VASP authorization if needed.
- HPC Admins should provide guidance on certificate renewal and software authorization processes.
---

### 2022020842000317_VASP%20request%20of%20bctc39%20-%2020-0186%205-204.md
# Ticket 2022020842000317

 ```markdown
# HPC Support Ticket Analysis

## Keywords
- VASP access request
- License number
- Expired certificate
- VASP versions (VASP 5, VASP 6)
- Institution details
- Primary license contact

## Summary
A user requested access to VASP versions 5 and 6 for their HPC account. The request included details such as the user's name, email, institution, and license number. The HPC admin responded that the certificate had expired and mentioned that the user had already been granted access to VASP 6 on another system.

## Root Cause
- Expired certificate for VASP access.

## Solution
- The HPC admin informed the user about the expired certificate and mentioned that access had already been granted on another system.

## General Learnings
- Always check the validity of certificates when processing VASP access requests.
- Ensure that users are aware of their existing access on other systems.
- Keep track of license numbers and primary license contacts for future reference.
```
---

### 2025010842003571_VASP%20request%20of%20b243cb11%20-%2023-0183.md
# Ticket 2025010842003571

 # HPC Support Ticket: VASP Access Request

## Keywords
- VASP access request
- Module availability
- GPU benchmarking
- Software installation

## Summary
- **User Request:** Access to VASP 6 for HPC account.
- **Institution:** Theoretical Physics, University of Bayreuth.
- **License Number:** 23-0183.
- **Requested Version:** VASP 6.

## HPC Admin Response
- **Action Taken:** VASP 6 modules made available on Fritz.
- **Pending Action:** VASP 6.5 installation is on the ToDo list.
- **Additional Offer:** Benchmarking VASP input for potential GPU benefits.

## Learnings
- **Module Availability:** Ensure requested software modules are available and accessible to users.
- **Software Installation:** Keep track of pending software installations and update users accordingly.
- **GPU Benchmarking:** Offer benchmarking services to optimize user workflows.

## Root Cause
- User needed access to specific software (VASP 6) for their HPC account.

## Solution
- HPC Admins granted access to the requested software modules and offered additional support for optimization.

## Next Steps
- Install VASP 6.5 as per the ToDo list.
- Follow up with the user for potential GPU benchmarking.

---

This documentation can be used as a reference for handling similar VASP access requests and offering additional support services.
---

### 2021070742003005_VASP%20request%20of%20iwsp011h%20-%2019-0006.md
# Ticket 2021070742003005

 # HPC Support Ticket: VASP Access Request

## Keywords
- VASP access request
- License verification
- Manual compilation
- Special libraries
- Simulation types

## Summary
A user requested access to VASP (versions 5 and 6) through the HPC form. The HPC admin approved the request but needed to manually verify the license, leading to a delay. The user inquired about further instructions and the need for manual compilation.

## Root Cause of the Problem
- Delay in manual license verification.
- Lack of pre-compiled VASP module for the requested version.

## Solution
- **License Verification**: The HPC admin manually verified the license.
- **Manual Compilation**: The admin provided instructions for compiling VASP manually:
  ```bash
  module load intel64
  tar -xf vasp.6.2.1.tgz
  cd vasp.6.2.1/
  cp arch/makefile.include.linux_intel makefile.include
  make
  ```
- **Special Libraries**: The admin inquired about the need for additional libraries (libbeef, DFTB4, etc.) and the type of simulations the user intended to perform (GGA, hybrid, GW, etc.).

## General Learnings
- VASP license requests require manual verification.
- Pre-compiled modules may not be available for all versions, necessitating manual compilation.
- Users should be prepared to provide additional information about their simulation needs and required libraries.

## Follow-up
- The admin will run the test suite with the provided settings and inform the user of any errors.
- The user may need to specify additional libraries and simulation types for further assistance.
---

### 2024011842001859_VASP%20request%20of%20b205cb10%20-%20License%2022-0268.md
# Ticket 2024011842001859

 # HPC Support Ticket Analysis: VASP Access Request

## Keywords
- VASP access request
- License verification
- Email mismatch
- License agreement conditions
- VASP module access

## Summary
A user requested access to VASP for their HPC account but encountered issues due to an email mismatch in the VASP database.

## Root Cause
- The user's email (`bt307920@uni-bayreuth.de`) was not found in the VASP database.
- The user might be registered with a different email address.

## Solution
- The HPC Admin verified the user's registration with an alternative email (`Hafssa.Arraghraghi@uni-bayreuth.de`).
- Access to the central VASP modules on the HPC system was granted after verification.

## General Learnings
- Ensure that the email provided in the access request matches the one registered in the VASP database.
- HPC Admins should check for alternative email addresses if the initial one is not found.
- Access to VASP is subject to license agreement conditions, which must be adhered to strictly.

## Actions Taken
- HPC Admin checked the VASP database for the user's email.
- HPC Admin verified the user's registration with an alternative email.
- Access to VASP modules was granted after successful verification.

## Follow-up
- Additional details regarding VASP access will be provided in a separate ticket by another HPC Admin.

## Relevant Parties
- HPC Admins
- 2nd Level Support Team
- Software and Tools Developers
- Head of the Datacenter
- Training and Support Group Leader
- NHR Rechenzeit Support and Applications for Grants

## Conclusion
Proper email verification is crucial for granting access to licensed software like VASP. HPC Admins should be prepared to check alternative email addresses if the initial one does not match the database records.
---

### 2023103042001347_Lizenzpflichtige%20Software%20%28VASP%2C%20BAND%2C%20ADF%29%20-%20b163cb.md
# Ticket 2023103042001347

 # HPC-Support Ticket: Lizenzpflichtige Software (VASP, BAND, ADF)

## Keywords
- Lizenzpflichtige Software
- VASP
- BAND
- ADF
- Software for Chemistry & Materials
- NHR FAU
- Rechenzeitantrag
- HPC-Account
- Fritz-Cluster
- Slurm
- Installation

## Problem
- User möchte lizenzpflichtige Software (VASP, BAND, ADF) auf dem HPC-Cluster nutzen.
- Unklarheit über den genauen Ablauf zur Nutzung der Software.

## Lösung
### VASP
1. **Email-Adressen der Nutzer an HPC-Support senden**: Die Nutzer müssen bei VASP gemeldet sein.
2. **Überprüfung der Email-Adressen in der VASP-Datenbank**: HPC-Support überprüft die Zugriffsberechtigung.
3. **Freischaltung der HPC-Accounts**: Zugriff auf vasp5/vasp6-Module auf Fritz (und ggf. Alex) wird freigeschaltet.
4. **Regelmäßige Überprüfung**: VASP meldet regelmäßig Änderungen in der Lizenz, HPC-Support passt Zugriffsrechte an.

### BAND und ADF
- **Selbstinstallation**: User wird gebeten, die Software selbst in einem eigenen Verzeichnis zu installieren.
- **Unterstützung bei Problemen**: HPC-Support bietet Unterstützung bei Installationsproblemen, hat aber keine Erfahrung mit den Codes.

## Hinweise
- **Knoteninformationen**: Schwierigkeiten bei der Bereitstellung spezifischer Knoteninformationen, da Slurm die Auswahl der Knoten vornimmt.
- **Kommunikation**: Nutzer wird gebeten, zukünftig die Support-Email-Adresse zu verwenden, um automatisch ein Ticket zu erstellen.

## Ergebnis
- **VASP**: Zugriff für mehrere Nutzer erfolgreich freigeschaltet.
- **BAND und ADF**: User wird die Installation selbst vornehmen und bei Bedarf Unterstützung anfordern.

## Zusammenfassung
Dieser Ticket-Verlauf zeigt den Prozess zur Freischaltung lizenzpflichtiger Software auf einem HPC-Cluster. Es wird deutlich, dass spezifische Abläufe für verschiedene Softwarepakete existieren und dass die Kommunikation über die Support-Email-Adresse wichtig ist, um Tickets effizient zu bearbeiten.
---

### 2023102642002381_VASP%20with%20-DDFTD4%20on%20Fritz.md
# Ticket 2023102642002381

 # HPC Support Ticket: VASP with -DDFTD4 on Fritz

## Keywords
- VASP6
- DFTD4
- Fritz
- Compilation flags
- Module load

## Problem
- User inquired about the availability of VASP6 compiled with the DFTD4 van der Waals method and the `-DDFTD4` flag on the Fritz HPC system.

## Root Cause
- The user needed to know which VASP6 installation includes the DFTD4 library for their computational work.

## Solution
- The HPC Admin confirmed that the only VASP module on Fritz that includes DFT-D4 is:
  ```bash
  module load vasp6/6.3.0-hybrid-intel-impi-AVX2-with-addons
  ```

## General Learnings
- Always check the specific module versions and their compilation flags when using specialized libraries like DFTD4.
- Use the `module load` command to load the appropriate module for your computational needs.
- Communicate with HPC support for clarifications on software installations and their configurations.

## Additional Notes
- The DFTD4 library needs to be installed prior to compiling VASP with the `-DDFTD4` flag.
- The HPC Admin provided detailed information on the specific module that includes the required library.

---

This documentation can be used to resolve similar inquiries about VASP installations and specific compilation flags on the Fritz HPC system.
---

### 2020092542001472_LAMMPS_Meggie%20access.md
# Ticket 2020092542001472

 # HPC-Support Ticket Conversation Summary

## Subject: LAMMPS/Meggie Access

### Keywords:
- LAMMPS installation
- VASP installation
- HPC cluster access
- Meggie cluster
- Emmy cluster
- Spack
- Personal VASP license

### General Learnings:
- **Cluster Access**: Users need to provide a project description for access to specific clusters.
- **Software Installation**: Users can install software like LAMMPS in their home directory using Spack.
- **VASP Installation**: Users with personal VASP licenses can install VASP in their home directory following specific instructions.
- **Central Installation**: Central installation of software like LAMMPS and VASP is planned but requires user input for specific modules and packages.

### Root Cause of Problems:
- **LAMMPS Installation**: Difficulty in centrally installing LAMMPS due to diverse user requirements.
- **VASP Installation**: Lack of central VASP installation and need for user-specific installation instructions.

### Solutions:
- **LAMMPS Installation**: Users can install LAMMPS in their home directory using Spack. Instructions provided for both Meggie and Emmy clusters.
- **VASP Installation**: Users can compile VASP in their home directory using provided makefile and Intel modules.

### Detailed Steps:

#### LAMMPS Installation:
1. **Access Meggie/Emmy cluster**.
2. **Install LAMMPS using Spack**:
   ```bash
   mkdir soft
   cd soft
   git clone https://github.com/spack/spack.git
   cd spack/bin
   ./spack install lammps
   ```
3. **LAMMPS Location**:
   - Meggie: `~/soft/spack/opt/spack/linux-centos7-haswell/gcc-4.8.5/lammps-20200721-*/bin`
   - Emmy: `~/soft/spack/opt/spack/linux-centos7-ivybridge/gcc-4.8.5/lammps-20200721-*/bin`

#### VASP Installation:
1. **Copy makefile**:
   ```bash
   cp arch/makefile.include.linux_intel ./makefile.include
   ```
2. **Load Intel modules**:
   ```bash
   module load intel64
   ```
3. **Compile VASP**:
   ```bash
   make all
   ```
4. **Optional Optimization**:
   ```makefile
   OFLAG = -O2 -axCORE-AVX2 -mavx
   ```

### Additional Notes:
- Users are encouraged to share their LAMMPS modules and packages for future central installation.
- Users interested in central VASP installation should fill out the online form.

### References:
- **Request access to central VASP installation**: [Form Link](https://hpc.fau.de/services/request-access-to-central-vasp-installation/)

This summary provides a quick reference for HPC support employees to assist users with similar issues related to LAMMPS and VASP installations on HPC clusters.
---

### 2022120742002825_VASP%20request%20of%20b158cb12%20-%2020-0414%205-1616.md
# Ticket 2022120742002825

 # HPC Support Ticket Analysis

## Keywords
- VASP access request
- License number
- Module access
- Support for usage

## Summary
- **User Request:** Access to VASP 6 for HPC account.
- **Institution:** Julius-Maximilians University, Institut für Theoretische Physik und Astrophysik.
- **License Number:** 20-0414 5-1616.
- **Primary License Contact:** Provided.

## Issue
- **Root Cause:** Certificate has expired.

## Solution
- **Action Taken:** HPC Admin granted access to the "vasp6" module.
- **Follow-up:** Offered support from Liaison-Scientists for VASP usage on Fritz.

## General Learnings
- Ensure certificates are up-to-date for software access.
- Provide clear instructions and support for new software access.
- Offer additional support through Liaison-Scientists for complex software usage.

## Next Steps
- Verify user access to the "vasp6" module.
- Ensure user is aware of available support resources.

---

This documentation can be used to resolve similar issues related to VASP access requests and expired certificates.
---

### 42061312_Vasp5.2%20compilation.md
# Ticket 42061312

 ```markdown
# Vasp5.2 Compilation Issue

## Keywords
- Vasp5.2
- Compilation
- Makefile
- Stack Memory
- rhfatm.o

## Problem Description
The user encountered an error while trying to compile Vasp5.2 on their local machine. The error message indicated that there was no rule to make the target `rhfatm.o`, which is needed by `vasp`.

## Root Cause
The root cause of the problem was a mismatch between the Makefile version (vasp5.2.8) and the code version (vasp5.2.2).

## Solution
The issue was resolved by ensuring that the Makefile and the code versions matched. The user was able to compile both versions of VASP successfully after this correction.

## Lessons Learned
- Ensure that the Makefile and the code versions are compatible.
- Mismatched versions can lead to compilation errors.
- Collaboration with colleagues and experts can help resolve complex issues.

## Support Team Involvement
- HPC Admins provided initial support and forwarded the issue to the relevant experts.
- The Head of the Datacenter and the Training and Support Group Leader were involved in coordinating the resolution.
- The 2nd Level Support team and Software and Tools developers were consulted for technical expertise.

## Conclusion
Proper version management and collaboration are crucial for successful software compilation. Ensuring that all components are compatible can prevent many common compilation errors.
```
---

### 2024032142003089_VASP%20request%20of%20bctc038h%20-%2020-0186%205-204.md
# Ticket 2024032142003089

 ```markdown
# HPC Support Ticket Conversation: VASP Access Request

## Keywords
- VASP access request
- HPC account
- License number
- VASP versions
- Institution details
- Primary license contact

## Summary
A user requested access to VASP versions 5 and 6 for their HPC account. The request included necessary details such as the user's name, email, license number, institution, and primary license contact.

## Root Cause
The user needed access to specific versions of VASP for their research.

## Solution
The HPC Admin granted access to the requested VASP modules on the HPC system.

## What Can Be Learned
- **Request Process**: Users need to provide specific details when requesting access to software like VASP.
- **Admin Response**: HPC Admins can quickly grant access to requested software modules once the necessary information is provided.
- **Communication**: Clear and concise communication between the user and the HPC Admin ensures a smooth process for granting software access.
```
---

### 2023112742002458_VASP%20request%20of%20b146dc10%20-%2020-186.md
# Ticket 2023112742002458

 ```markdown
# HPC-Support Ticket Conversation: VASP Access Request

## Keywords
- VASP access request
- HPC account
- License number
- Institution
- Primary license contact
- VASP 6

## Summary
A user requested access to VASP 6 for their HPC account. The request included details such as the user's name, email, license number, institution, and primary license contact.

## User Request
- **Subject:** VASP access request
- **HPC Account:** b146dc10
- **First Name:** Julien
- **Last Name:** Steffen
- **Email:** julien.steffen@fau.de
- **License Number:** 20-186
- **Requested Version:** VASP 6
- **Institution:** Lehrstuhl für Theoretische Chemie, Prof. Dr. Andreas Görling
- **Primary License Contact:** christian.neiss@fau.de

## HPC Admin Response
- **Action:** The HPC account was granted access to the central VASP6 installations.
- **Admin:** Thomas Zeiser
- **Date:** 27.11.2023

## What Can Be Learned
- **Process:** Users requesting access to specific software (e.g., VASP) need to provide their HPC account details, license number, and institutional information.
- **Outcome:** Once the request is processed, the HPC Admin grants access to the requested software version.
- **Documentation:** This ticket serves as a reference for handling future VASP access requests, ensuring that all necessary information is collected and processed correctly.
```
---

### 2024120242004507_VASP%20request%20of%20b248cb11%20-%2023-0183.md
# Ticket 2024120242004507

 # HPC Support Ticket Conversation Summary

## Subject: VASP Request for HPC Account

### User Request
- **Request Type**: VASP access
- **Account**: b248cb11
- **User Details**:
  - First Name: Yuxuan
  - Last Name: Yao
  - Email: ge28quz@mytum.de
- **License Number**: 23-0183
- **Requested Version**: VASP 6
- **Institution**: University of Bayreuth; Chair for Theoretical Physics; Prof. Dr. Harald Oberhofer Group
- **Primary License Contact**: ge28quz@mytum.de

### HPC Admin Response
- **Action**: Granted access to VASP modules on Fritz.

### User Issue
- **Problem**: VASP memory issue causing job cancellation.
- **Job Details**:
  - Path: /home/hpc/b248cb/b248cb11/elastic_vasp_test/AVA/C11_C22_C12_I/strain_0.00
  - Script: Example script from the page [VASP Documentation](https://doc.nhr.fau.de/apps/vasp/).
  - Memory Used: 506751 kBytes
- **Question**: Query about stack size limit and hidden memory limits.

### 2nd Level Support Response
- **Suggestion**: Increase `OMP_STACKSIZE` to 500m or larger.
- **Additional Info**:
  - Check INCAR file for hybrid XC calculation.
  - Set `NCORE=1` in INCAR for hybrid calculations.

### User Follow-Up
- **Action**: Added `export OMP_STACKSIZE=500m` and set `NCORE=1`.
- **Result**: Job with 148 atoms and box size (8,9,24) ran successfully.

### Additional User Issue
- **Problem**: Larger system (~250 atoms) job killed due to memory issue when increasing nodes.
- **Job Details**:
  - Path: /home/hpc/b248cb/b248cb11/test/AVA-MBA-ELASTIC/AVA-3D-no-vaccum-elastic
  - Script Settings:
    ```bash
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=4
    #SBATCH --cpus-per-task=18
    #SBATCH --partition=multinode
    export OMP_STACKSIZE=500m
    ```

### 2nd Level Support Response
- **Recommendation**: Avoid hybrid (MPI+OMP) and use MPI-only runs.
- **Benchmark**: MPI-only runs for large systems (>>250 atoms) without memory issues.
- **Script Adjustment**:
  - Set `NCORE=36` or `NCORE=18` in INCAR for MPI-only calculations.

### User Feedback
- **Result**: MPI-only runs smoother than hybrid style.
- **Status**: Job running successfully.

### Key Learnings
- **Memory Management**: Increasing `OMP_STACKSIZE` can resolve memory issues for hybrid calculations.
- **Parallelization**: MPI-only runs are recommended for large systems to avoid memory issues and stack size concerns.
- **INCAR Settings**: Set `NCORE=36` or `NCORE=18` for MPI-only calculations.

### Solution
- **Memory Issue**: Increase `OMP_STACKSIZE` to 500m or larger.
- **Large Systems**: Use MPI-only runs and set appropriate `NCORE` values in INCAR.

### References
- [VASP Documentation](https://doc.nhr.fau.de/apps/vasp/)
- [VASP Benchmark](https://hpc.fau.de/files/2023/11/vasp-benchmark-2023.pdf)
---

### 2022102742003899_VASP%20request%20of%20a102cb12%20-%2019-0075.md
# Ticket 2022102742003899

 ```markdown
# HPC Support Ticket Conversation Analysis

## Subject: VASP Request for Account a102cb12 - License 19-0075

### Keywords:
- VASP access request
- License validation
- Module availability
- User feedback

### Summary:
- **User Request:** Access to VASP for account a102cb12 with license number 19-0075.
- **Institution:** Institute of Materials Science, University of Stuttgart.
- **Requested Version:** VASP 5.

### HPC Admin Response:
- **License Validity:** The user's chair's license is valid until 2023, allowing access to both VASP 5 and VASP 6.
- **Module Availability:** Modules for both VASP 5 and VASP 6 are available on Fritz.
  - `vasp5/5.4.4.pl2-intel-impi-AVX512`
  - `vasp6/6.3.0-hybrid-intel-impi-AVX2-with-addons`
  - `vasp6/6.3.2-hybrid-intel-impi-AVX512`
  - `vasp6/6.3.0-hybrid-intel-impi-AVX2`
  - `vasp6/6.3.0-hybrid-intel-impi-AVX512`
- **Feedback Request:** Users are encouraged to report any issues or provide positive feedback.

### Additional Information:
- The account was previously enabled for VASP on Fritz.
- Licenses valid until June 30, 2019, indicate access to VASP 5 only.
- Licenses valid after June 30, 2019, indicate access to VASP 6.

### Root Cause of the Problem:
- The user was unaware of the availability of VASP modules and needed confirmation of access.

### Solution:
- Confirmation of license validity and module availability.
- Encouragement to use the modules and provide feedback.

### General Learnings:
- Always check license validity and corresponding module availability.
- Communicate clearly with users about the modules they can access.
- Encourage users to report issues and provide feedback for continuous improvement.
```
---

### 2024032142002741_VASP%20modules%20on%20fritz%20with%20HDF5%20support.md
# Ticket 2024032142002741

 ```markdown
# HPC Support Ticket: VASP Modules on Fritz with HDF5 Support

## Keywords
- VASP
- HDF5 support
- Module access
- License conditions
- Fritz cluster

## Problem
- User lacks HDF5 support and other features in the current VASP version.
- User's HPC account does not have access to the new VASP 6.4.2 module.
- User encounters errors when trying to access the new VASP module.

## Root Cause
- VASP has strict license conditions that require user eligibility verification.

## Solution
- User needs to complete the access request form for the central VASP installation.
- HPC Admins will verify the user's eligibility with VASP.at and grant access to the VASP modules if approved.

## General Learnings
- VASP modules on Fritz cluster require user eligibility verification due to strict license conditions.
- Access to VASP modules can be requested through a specific form on the HPC website.
- HPC Admins handle the verification process and grant access to eligible users.
```
---

### 2022112942000752_VASP%20request%20of%20mpfp000h%20-%2022-0368%205-2988.md
# Ticket 2022112942000752

 ```markdown
# HPC Support Ticket: VASP Access Request

## Keywords
- VASP access
- HPC account
- License number
- Rechenzeit
- NHR application
- FAU
- Meggie
- Fritz cluster

## Summary
- **User Request:** Access to VASP versions 5 and 6 for HPC account.
- **Issue:** Initial lack of VASP modules on Meggie.
- **Solution:** VASP modules added; account activated on Fritz cluster.
- **Additional Information:** User advised on NHR application for increased computational needs.

## Detailed Information
- **User Details:**
  - First name: Alexander
  - Last name: Schneider
  - Email: alexander.schneider@physik.uni-erlangen.de
  - License number: 22-0368 5-2988
  - Institution: Friedrich-Alexander Universität Erlangen-Nürnberg
  - Research Group: Prof. Dr. M. Alexander Schneider
  - Org. unit: Institut der kondensierten Materie, Department für Physik

- **HPC Admin Response:**
  - VASP modules (vasp5 and vasp6) added to Meggie.
  - User's HPC account activated on Fritz cluster.
  - User advised to submit an NHR application if annual computational needs exceed 500,000 core-hours.

## Root Cause
- Lack of VASP modules on Meggie initially.

## Solution
- VASP modules added to Meggie.
- User account activated on Fritz cluster.
- User informed about NHR application process for increased computational resources.

## Additional Notes
- User has minimal computational usage for the year.
- NHR application process explained to save FAU's electricity costs.
```
---

### 2022022242002548_Early-Fritz%20%22Julien%20Steffen%22%20_%20bctc034h.md
# Ticket 2022022242002548

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Keywords
- VASP License
- Early-User Access
- Freischaltung (Activation)
- Certificate Expiration
- Single-Node Throughput
- Ab Initio MD Simulations
- Machine Learning Force Field
- Ionic Liquids
- Metal Surfaces
- CLINT Collaborative Research Center

## General Learnings
- **VASP License Verification**: Before granting access to VASP modules, the user's email must be verified against the VASP developer database.
- **Early-User Access**: Users can request early access to HPC resources for specific projects.
- **Certificate Expiration**: Ensure that certificates are up-to-date to avoid access issues.
- **Documentation**: Provide users with links to relevant documentation for new systems.

## Root Cause of the Problem
- The user's email was not associated with a VASP license, preventing access to the VASP modules.

## Solution
- The user's email was added to the VASP license of the Theoretical Chemistry department.
- The user was granted early-user access to the Fritz cluster and the VASP module.
- The user was provided with a link to the continuously updated documentation for the Fritz cluster.
```
---

