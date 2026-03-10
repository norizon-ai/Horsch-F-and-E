# Topic 14: certificate_certificates_expiration_expired_the

Number of tickets: 101

## Tickets in this topic:

### 2022091542004234_Fritz%20Freischaltung%20ihpc050h.md
# Ticket 2022091542004234

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject: Fritz Freischaltung ihpc050h

### Keywords:
- Freischaltung (activation)
- Fritz
- ihpc050h
- Projektpartner (project partner)
- EoCoE
- Barcelona
- Certificate expired

### Summary:
A user requested the activation of a specific node (ihpc050h) for a project partner. The HPC Admin responded by noting that the certificate had expired and marked the issue as resolved.

### Root Cause:
- The certificate for the node had expired.

### Solution:
- The HPC Admin acknowledged the expired certificate and marked the issue as resolved.

### General Learnings:
- Always check the status of certificates when dealing with node activation requests.
- Ensure that certificates are up-to-date to avoid activation issues.
```
---

### 2023013042001588_Zertifikatsrollover%20am%20IdP%20der%20TU%20Dresden.md
# Ticket 2023013042001588

 # HPC Support Ticket: Certificate Rollover at TU Dresden IdP

## Keywords
- Certificate Rollover
- TU Dresden IdP
- SAML Communication
- Metadata Update
- Service Provider (SP)
- Identity Provider (IdP)

## Summary
The encryption and signing certificate of the TU Dresden IdP is expiring on 05.02.2023 at 10:25 am. A new certificate has been added to the IdP metadata. Action is required for Service Providers (SPs) that manually communicate the IdP metadata or certificate.

## Root Cause
- Expiration of the current encryption and signing certificate of the TU Dresden IdP.

## Solution
1. **Download New Metadata**:
   - Download the new IdP metadata from the federation [here](https://met.refeds.org/met/entity/https://idp.tu-dresden.de/idp/shibboleth/) or directly from the IdP [here](https://idp.tu-dresden.de/idp/shibboleth) as XML.

2. **Update SP Configuration**:
   - If your SP supports more than one certificate, store the metadata or the certificates at the SP.
   - If your SP supports only one certificate per IdP, store the certificate with the keyname "idp.tu-dresden.de neu" at the SP.

3. **Dynamic Metadata**:
   - If your SP obtains the IdP metadata dynamically, the rollover will be seamless.

## Notes
- **HPC Admin**: It is suspected that no action is required for the HPC Portal or Moodle, as the Dresden certificate is unlikely to be manually integrated.
- **Contact**: For any questions, contact the service desk with the reference "IdP certificate rollover."

## General Learning
- Regularly check for certificate expiration dates and updates.
- Ensure that SPs are configured to handle certificate rollovers seamlessly, either by supporting multiple certificates or by dynamically obtaining metadata.
- Communicate with relevant parties well in advance of certificate expiration to avoid service disruptions.
---

### 2022101442003672_Tier3-Access-Fritz%20%22Sukhminder%20Singh%22%20_%20mp24006h.md
# Ticket 2022101442003672

 # HPC Support Ticket Analysis

## Keywords
- HPC Account Activation
- Software Installation
- Certificate Expiration
- deal.II, opencfs, trilinos
- Finite Element Fracture Simulations
- Structural Optimization
- Single-Node Throughput
- OpenMP Parallel

## Summary
- **User Request:** Access to HPC resources for finite element fracture simulations within a structural optimization framework.
- **Required Software:** deal.II, opencfs, trilinos.
- **Resource Allocation:** Single-node throughput (72 cores, 250 GB), 5000 node hours on Fritz.

## Issue
- **Root Cause:** Certificate expiration.
- **Solution:** HPC Admin enabled the user's account on Fritz.

## Learning Points
- Users must manage the installation of non-centrally installed software (deal.II, opencfs, trilinos) themselves.
- Certificate expiration can lead to account access issues.
- HPC Admins handle account activation and resource allocation.

## Next Steps for Support
- Ensure users are aware of software installation responsibilities.
- Monitor certificate validity to prevent access issues.
- Provide guidance on installing and managing required software if needed.
---

### 2023022742003296_Tier3-Access-Fritz%20%22Tobias%20M%C3%83%C2%BCller%22%20_%20nfcc004h.md
# Ticket 2023022742003296

 ```markdown
# HPC Support Ticket Conversation Analysis

## Subject: Tier3-Access-Fritz "Tobias Müller" / nfcc004h

### Keywords
- HPC Account Activation
- Certificate Expiration
- Multi-node Workload
- Quantum Espresso
- Intel Compiler
- ELPA

### Summary
- **User Request:** Access to HPC system "Fritz" for multi-node workload.
- **Resources Requested:** 5000 node hours, 72 cores, 250 GB per node.
- **Software Requested:** Quantum Espresso PW, Intel Compiler, ELPA.
- **Purpose:** Compilation and testing of Quantum Espresso PW.

### Root Cause of the Problem
- Certificate expiration.

### Solution
- HPC Admin activated the user's account on Fritz.

### General Learnings
- Ensure certificates are up-to-date to avoid access issues.
- Proper communication and documentation are essential for account activation and resource allocation.
- Understand the specific software and hardware requirements for user projects.

### Actions Taken
- HPC Admin activated the user's account on Fritz.
- User was informed about the account activation.

### Follow-up
- No further action required from the user.
- HPC Admin to monitor for any additional requests or issues.
```
---

### 2022111042000288_mppm001h%20Quota.md
# Ticket 2022111042000288

 # HPC Support Ticket: WORK Filesystem Quota Issue

## Keywords
- Quota
- WORK filesystem
- Connection refused
- Certificate expired

## Problem Description
- User unable to view quota for the WORK filesystem.
- Error message: `quota: error while getting quota from wadm2.nhr.fau.de:/srv/apps/U20 for mppm001h (id 412553): Connection refused`

## Root Cause
- Expired certificate on the server.

## Solution
- HPC Admin resolved the issue by renewing the certificate.

## What Can Be Learned
- Certificate expiration can cause connection issues leading to quota viewing problems.
- Regularly check and renew certificates to prevent such issues.
- Users should report any sudden changes in access or functionality to the HPC support team.

## Actions Taken
- HPC Admin identified and renewed the expired certificate.
- Confirmed resolution with the user.

## Follow-up
- Monitor for similar issues to ensure the certificate renewal process is effective.
- Document certificate renewal procedures to prevent future occurrences.

## Related Commands
- `shownicerquota.pl`
- `quota`

## Ticket Status
- Resolved
---

### 2022080242003109_Nodes%20available.md
# Ticket 2022080242003109

 ```markdown
# HPC Support Ticket: Nodes Available

## Keywords
- Job submission issue
- High priority jobs
- Job disappearance
- Certificate expiration

## Summary
A user reported issues with job submission and requested prioritization due to an upcoming deadline. The HPC Admin responded, noting that multiple high-priority jobs were started but disappeared shortly after. The admin also mentioned that a certificate had expired.

## Root Cause
- **Job Disappearance**: High-priority jobs were disappearing after being started.
- **Certificate Expiration**: The admin mentioned a certificate had expired, which could be related to the job submission issues.

## Solution
- **Investigate Job Disappearance**: The admin should investigate why high-priority jobs are disappearing. This could be due to system errors, resource allocation issues, or other technical problems.
- **Renew Certificate**: The expired certificate should be renewed to ensure it is not causing job submission issues.

## General Learnings
- **Job Prioritization**: Users may request job prioritization due to deadlines. It is important to handle these requests promptly and ensure jobs are not disappearing.
- **Certificate Management**: Expired certificates can cause various issues, including job submission problems. Regularly check and renew certificates to avoid such issues.
```
---

### 2024090642000617_%5BDFN%232024090610000712%5D%20Zertifikat%20l%C3%83%C2%A4uft%20ab%20_%20certificate%20about%20to%20e.md
# Ticket 2024090642000617

 # HPC-Support Ticket: Certificate Expiration

## Keywords
- Certificate expiration
- Renewal process
- SSO-Signing
- SSO-Encryption
- Web-SSL
- Apache
- Container redeployment
- Rollover

## Summary
The ticket addresses the expiration of a certificate for the HPC portal and the steps taken to renew and implement the new certificate.

## Root Cause
- The certificate for `portal.hpc.fau.de` was about to expire on 2024-10-03.

## Steps Taken
1. **Auto-Renew Activation**: Auto-renew was activated with a 14-day window.
2. **New Certificate Received**: A new certificate was obtained on 2024-09-20.
3. **Code Integration**: The new certificate was integrated into the code.
4. **Container Redeployment**: The container was redeployed on 2024-09-23 around 19:00 for the rollover.
5. **Certificate Distribution**: The new certificate was sent via encrypted mail for Apache.
6. **Apache Certificate Exchange**: The Apache certificate was exchanged.
7. **Rollover Completion**: The rollover was completed, and the new certificate was entered for SSO-Signing, SSO-Encryption, and Web-SSL.

## Solution
- The new certificate was successfully implemented and is valid until 2025-09-21.

## Documentation
- For detailed instructions on certificate renewal, refer to [DFN Certificates Documentation](https://doku.tid.dfn.de/en:certificates).

## Notes
- Ensure timely renewal of certificates to avoid service disruptions.
- Follow the documented process for certificate renewal and implementation.

---

This documentation can be used as a reference for future certificate renewal processes.
---

### 2022092142002724_Tier3-Access-Fritz%20%22Jonathan%20Steffes%22%20_%20iwpa007h.md
# Ticket 2022092142002724

 # HPC Support Ticket Analysis

## Keywords
- Account activation
- Certificate expiration
- Multi-node workload
- HDR100 Infiniband
- Simcenter Star-CCM+
- Heat exchanger simulation
- Turbulence intensity optimization

## Summary
- **User Request:** Access to HPC system "Fritz" for multi-node workload using Simcenter Star-CCM+ to simulate and optimize a heat exchanger model.
- **Resources Requested:** 2700 node hours on Fritz.
- **Software Required:** Simcenter Star-CCM+.
- **Application:** Simulating a heat exchanger model with variable parameters to minimize turbulence intensity.
- **Expected Results:** Understanding the correlation between different parameters and turbulence intensity to optimize the heat exchanger model.

## Issue
- **Root Cause:** Certificate expiration.
- **Solution:** HPC Admin activated the user's account on Fritz.

## General Learnings
- Ensure certificates are up-to-date to avoid account access issues.
- Properly document resource requests and expected outcomes for future reference.
- Communicate clearly with users about account status and any actions taken.

## Next Steps
- Monitor certificate expiration dates to prevent future access issues.
- Provide users with clear instructions on how to renew certificates if needed.
- Document common issues and solutions for quick reference in future support tickets.
---

### 2019102442001643_Requesting%20access%20to%20Meggie.md
# Ticket 2019102442001643

 # HPC Support Ticket: Requesting Access to Meggie Cluster

## Keywords
- Access Request
- Meggie Cluster
- Atomistic Simulations
- Certificate Expiration

## Summary
A user requested access to the Meggie computer cluster to run atomistic simulations. The HPC admin responded, mentioning a certificate expiration issue.

## Root Cause
- User requires access to the Meggie cluster for atomistic simulations.
- Potential issue with certificate expiration mentioned by the HPC admin.

## Solution
- The HPC admin acknowledged the request but did not provide a clear resolution.
- Further communication is needed to address the certificate expiration and grant access.

## Learning Points
- Ensure users provide necessary details for access requests.
- Address certificate expiration issues promptly to avoid access delays.
- Follow up on access requests to ensure completion and user satisfaction.

## Next Steps
- Verify the status of the certificate.
- Grant the user access to the Meggie cluster if the certificate issue is resolved.
- Confirm with the user that access has been successfully granted.

## Relevant Contacts
- **HPC Admins**: Thomas, Michael Meier, Anna Kahler, Katrin Nusser, Johannes Veh
- **2nd Level Support Team**: Lacey, Dane (fo36fizy), Kuckuk, Sebastian (sisekuck), Lange, Florian (ow86apyf), Ernst, Dominik (te42kyfo), Mayr, Martin
- **Datacenter Head**: Gerhard Wellein
- **Training and Support Group Leader**: Georg Hager
- **NHR Rechenzeit Support**: Harald Lanig
- **Software and Tools Developer**: Jan Eitzinger, Gruber

## Additional Notes
- Ensure proper documentation of access requests and resolutions for future reference.
- Regularly check for and renew expiring certificates to prevent access issues.
---

### 2019051342000595_Access%20to%20Meggie.md
# Ticket 2019051342000595

 ```markdown
# HPC-Support Ticket: Access to Meggie

## Subject
Access to Meggie

## User Request
- **User**: PhD student from the Department of Materials Science, FAU
- **Request**: Access to Meggie for running atomistic simulations

## HPC Admin Response
- **Issue**: Certificate has expired
- **Action Taken**: Certificate renewal or update

## Additional Information
- **Previous Usage**: User has run IMD and LAMMPS jobs on Emmy with moderate node count (typically 10)
- **Performance Issues**: Moderate performance and occasional load imbalances

## Keywords
- Access Request
- Meggie
- Atomistic Simulations
- Certificate Expiration
- Performance Issues
- Load Imbalances

## Lessons Learned
- Ensure certificates are up-to-date for access to HPC resources
- Monitor performance and address load imbalances for better job efficiency

## Solution
- Renew or update the expired certificate to grant access to Meggie
- Address performance issues and load imbalances for improved job execution
```
---

### 2023110842001404_Freischaltung%20von%20Hiwi%20f%C3%83%C2%BCr%20Fritz%20und%20Alex.md
# Ticket 2023110842001404

 ```markdown
# HPC Support Ticket Analysis

## Subject: Freischaltung von Hiwi für Fritz und Alex

### Keywords:
- Account activation
- HPC Portal
- User access
- Expired certificate

### Root Cause:
- User requested activation of an account for specific systems (Fritz and Alex).

### Solution:
- HPC Admin confirmed the activation was completed.
- Note: There was a mention of an expired certificate, but it was not clear if this was related to the activation request.

### Lessons Learned:
- Ensure that account activation requests are clear and include all necessary details.
- Verify that any related certificates are up-to-date to avoid potential issues.
- Confirm with the user once the activation is complete.

### Actions Taken:
- HPC Admin activated the account as requested.
- Confirmation email was sent to the user.

### Follow-up:
- No further action required unless the user encounters issues with the activated account.
```
---

### 2022052042000271_Tier3-Access-Fritz%20%22Dominic%20Soldner%22%20_%20iwtm000h.md
# Ticket 2022052042000271

 ```markdown
# HPC Support Ticket Conversation Analysis

## Subject: Tier3-Access-Fritz "Dominic Soldner" / iwtm000h

### Keywords:
- HPC Account Activation
- Certificate Expiration
- Multi-node Workload
- Software Requirements (dealii, trilinos, boost)
- Thermo-mechanical Simulations
- Additive Manufacturing Processes

### Summary:
- **User Request**: Access to HPC resources for multi-node workload.
- **Resources Needed**: 50,000 hours of compute time, 72 cores, 250 GB per node.
- **Software**: dealii and its dependencies (trilinos, boost) to be installed using spack.
- **Application**: Thermo-mechanical simulations for additive manufacturing processes.
- **Expected Results**: Insights into manufacturing processes, temperature and displacement fields, microstructure evolutions.

### Issue:
- **Root Cause**: Certificate expiration.

### Solution:
- **Action Taken**: HPC Admin activated the user's account on Fritz.

### General Learnings:
- Ensure certificates are up-to-date to avoid account access issues.
- Understand user requirements for compute resources and software dependencies.
- Provide clear communication regarding account activation and resource allocation.

### Notes:
- This ticket highlights the importance of timely certificate renewal and clear communication regarding account activation and resource allocation.
- Ensure that users are aware of the software installation process and dependencies required for their specific applications.
```
---

### 2024070542003316_Tier3-Access-Fritz%20%22Tobias%20Grauvogl%22%20_%20iwst090h.md
# Ticket 2024070542003316

 # HPC Support Ticket: Tier3-Access-Fritz

## Keywords
- HPC Account Activation
- Resource Allocation
- Simulation Requirements
- Deadline Extension

## Summary
A user requested access to the Fritz HPC system for running simulations for their master's thesis. The user specified their resource requirements, software needs, and expected outcomes. The HPC Admin activated the user's account and later extended the access period upon the user's request.

## Problem
- **Root Cause**: The user needed access to the Fritz HPC system to run simulations for their master's thesis. The initial resource allocation was not sufficient to complete the required simulations.

## Solution
- **Account Activation**: The HPC Admin activated the user's account on Fritz.
- **Resource Allocation**: The user was granted 12,000 node hours on Fritz.
- **Software Requirements**: The user required Star-ccm+ and 2402-clang for their simulations.
- **Deadline Extension**: The user requested and was granted an extension of their access period until the end of September to complete their simulations.

## General Learnings
- **Resource Planning**: Users should carefully estimate their resource needs and be prepared to request extensions if necessary.
- **Communication**: Clear and timely communication with HPC support can help ensure that users have the resources they need to complete their projects.
- **Flexibility**: HPC support may be able to accommodate requests for additional resources or extensions if justified by the user's needs.

## Notes
- The user was running turbulent FSI simulations with a nonlinear solid body, which required significant computational resources.
- The user planned to simulate 5-7 rotations at two different working points (7000 rpm and 5000 rpm).
- The user's initial estimate was that running at 20 nodes with 20 cores per node on Meggie would require about 1.5 weeks for one rotation.
---

### 2021082542000419_Prompt%20auf%20cshpc%20kommt%20nicht.md
# Ticket 2021082542000419

 ```markdown
# HPC Support Ticket: Prompt auf cshpc kommt nicht

## Keywords
- Prompt delay
- cshpc
- Hanging connection
- Certificate expiration

## Problem Description
- User reported waiting several minutes without receiving a prompt on cshpc.
- Screenshot indicated a hanging connection.

## Root Cause
- Unclear from the initial investigation.
- Possible certificate expiration mentioned.

## Actions Taken
- HPC Admins investigated but did not identify a specific issue.
- User reported that the problem resolved itself.

## Solution
- No specific solution identified.
- Issue resolved spontaneously.

## Lessons Learned
- Intermittent issues can resolve without clear intervention.
- Certificate expiration can be a potential cause for connection issues.
- Regular monitoring and user feedback are essential for identifying and resolving transient problems.
```
---

### 2022050542003716_Alex%20Freischaltung.md
# Ticket 2022050542003716

 ```markdown
# HPC Support Ticket: Account Activation

## Keywords
- Account activation
- Resource allocation
- A100
- A40
- Expired certificate

## Summary
A user requested the activation of an account for a colleague. The HPC Admin responded by activating the account and allocating resources.

## Root Cause
- User requested account activation for a colleague.

## Solution
- HPC Admin activated the account and allocated 8 A100 and 8 A40 resources.

## Notes
- If additional resources are needed, the user should contact the HPC Admin.
- Ensure certificates are up-to-date to avoid expiration issues.
```
---

### 2022110942001164_FHPC%20Portal%20Private%20Key.md
# Ticket 2022110942001164

 ```markdown
# HPC-Support Ticket: FHPC Portal Private Key

## Subject: FHPC Portal Private Key

## Keywords:
- Certificate expiration
- Private key extraction
- Java Key Store (JKS)
- SSO attributes
- DFN-AAI-Metadatenverwaltung
- SSL Labs

## Summary:
The FHPC Portal's web certificate expired, and the private key was missing. The issue was resolved by extracting the private key from the Java Key Store (JKS) and uploading it to the Apache servers. Additionally, there were issues with SSO attributes not being transferred correctly, which were fixed.

## Detailed Conversation:

### Initial Issue:
- **User**: The web certificate for the FHPC Portal has expired. The certificate was received from another colleague, but the corresponding private key is missing.
- **HPC Admin**: Suggested checking the specified path on the server where the private key was supposed to be located.

### Private Key Extraction:
- **User**: The private key was not found in the specified location.
- **HPC Admin**: Suggested applying for a new certificate if the private key could not be found.
- **User**: Successfully extracted the private key from the JKS with the help of a colleague and uploaded it to the Apache servers.

### SSO Attribute Issue:
- **HPC Admin**: Noticed that some SSO attributes were not being transferred correctly after the certificate update.
- **User**: Fixed the SSO attribute issue.
- **HPC Admin**: Confirmed that the SSO attributes were being transferred correctly before the DFN-AAI-Metadatenverwaltung update.

### Certificate Chain Issue:
- **HPC Admin**: Noticed that the certificate chain was incomplete, causing issues with some browsers and tools like `curl`, `wget`, and `openssl`.
- **User**: Fixed the certificate chain issue, resulting in an A+ rating from SSL Labs.

## Root Cause:
- The private key for the expired certificate was missing.
- The certificate chain was incomplete after the initial update.
- SSO attributes were not being transferred correctly after the certificate update.

## Solution:
- Extracted the private key from the JKS and uploaded it to the Apache servers.
- Fixed the SSO attribute transfer issue.
- Corrected the certificate chain to ensure compatibility with all browsers and tools.

## Conclusion:
The FHPC Portal's web certificate was successfully updated, and all related issues were resolved. The portal is now functioning correctly with an A+ rating from SSL Labs.
```
---

### 2021051242002296_hpc-mover%20request.md
# Ticket 2021051242002296

 ```markdown
# HPC-Support Ticket Conversation: hpc-mover Request

## Keywords
- hpc-mover
- some-hash-value
- certificate expired
- HPC Services
- Regionales RechenZentrum Erlangen (RRZE)

## Summary
A user requested to use the hpc-mover service for a specific directory and inquired about obtaining the some-hash-value. The HPC Admin responded with a link and mentioned that the certificate had expired.

## Root Cause of the Problem
- User needed to use the hpc-mover service.
- User required the some-hash-value for the service.

## Solution
- The HPC Admin provided a link to the HPC-Data service.
- The HPC Admin noted that the certificate had expired.

## General Learnings
- Users may need guidance on obtaining specific values (e.g., some-hash-value) for HPC services.
- Certificate expiration can be a common issue that needs to be addressed.
- Providing direct links to relevant services can help users resolve their issues quickly.
```
---

### 2024100442001788_G%C3%83%C2%89ANT%20TCS%20certificate%20information%3A%20moodle.nhr.fau.de.md
# Ticket 2024100442001788

 ```markdown
# HPC-Support Ticket: GÉANT TCS Certificate Information

## Subject
GÉANT TCS certificate information: moodle.nhr.fau.de

## Keywords
- Certificate Request
- OV Multi-Domain
- Certificate ID
- Download Format
- Certificate Expiry
- Apache/nginx
- Microsoft IIS
- PKCS#7
- PEM encoded

## Summary
A certificate request with profile OV Multi-Domain has been processed and issued for multiple domain names. The certificate will expire on 04/10/2025 23:59 GMT. Instructions for downloading the certificate in various formats are provided.

## Details
- **Certificate ID:** 10605021
- **Expiry Date:** 04/10/2025 23:59 GMT
- **Domains:**
  - moodle.nhr.fau.de
  - www.moodle.nhr.fau.de
  - moodle.nhr.uni-erlangen.de
  - www.moodle.nhr.uni-erlangen.de

## Download Formats
- **Apache/nginx:** "as Certificate (w/ issuer after)"
- **Microsoft IIS:** "as PKCS#7"
- **Available Formats:**
  - as Certificate only, PEM encoded
  - as Certificate (w/ issuer after), PEM encoded
  - as Certificate (w/ chain), PEM encoded
  - as PKCS#7
  - as PKCS#7, PEM encoded
  - as Root/Intermediate(s) only, PEM encoded
  - as Intermediate(s)/Root only, PEM encoded

## Actions Taken
- HPC Admin noted the certificate details and closed the customer request as completed.
- New expiry date noted: Sunday, 5. October 2025 um 01:59:59

## Solution
- Use the provided links to download the certificate in the required format.
- Ensure the certificate is installed correctly on the relevant servers.

## Notes
- The Certificate ID is essential for renewing or revoking the certificate.
- Different download formats are available to suit various server configurations.
```
---

### 2022091942002658_Availability%20of%20Meggie.md
# Ticket 2022091942002658

 # HPC-Support Ticket: Availability of Meggie

## Keywords
- Meggie
- Emmy
- Fritz
- Alex
- NHR Clusters
- Tier3 Access
- $FASTTMP

## Summary
- **User Issue**: Unable to run simulations due to issues with Meggie and Emmy, and lack of access to newer clusters Fritz/Alex.
- **Root Cause**: $FASTTMP on Meggie is not operational.
- **Solution**:
  - No ETA for Meggie's $FASTTMP.
  - Rest of Meggie is usable.
  - Tier3 access to Fritz and Alex is possible via application forms.

## Details
- **User Request**: Inquiry about Meggie's availability and temporary access to NHR clusters.
- **HPC Admin Response**:
  - Informed user about the current status of Meggie.
  - Provided links to apply for Tier3 access to Fritz and Alex.

## Follow-up Actions
- User needs to apply for Tier3 access to Fritz or Alex if immediate computing resources are required.
- Monitor Meggie's $FASTTMP status for future updates.

## Links
- [Tier3 Access to Fritz](https://hpc.fau.de/tier3-access-to-fritz/)
- [Tier3 Access to Alex](https://hpc.fau.de/tier3-access-to-alex/)
---

### 2018112142001916_Request%20for%20the%20FLOW-3D%20installation%20on%20Emmy.md
# Ticket 2018112142001916

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject: Request for the FLOW-3D installation on Emmy

### Keywords:
- FLOW-3D installation
- LiMa shutdown
- Emmy cluster
- Parallel jobs

### Root Cause of the Problem:
- User needs FLOW-3D software installed on Emmy cluster to continue running parallel jobs due to the shutdown of LiMa.

### Solution:
- HPC Admin acknowledged the request and indicated that the certificate has expired.
- The exact status of the installation is unclear from the conversation.

### General Learnings:
- Users may request software installations on different clusters due to the shutdown of existing resources.
- Ensure clear communication regarding the status of software installations and any issues encountered.
- Maintain up-to-date certificates for software installations.

### Next Steps:
- Follow up with the user to confirm the installation status of FLOW-3D on Emmy.
- Ensure that any expired certificates are renewed to avoid installation issues.
- Document the installation process for future reference and troubleshooting.
```
---

### 2018032642002234_FAU-CA%20Zertifikatinformation.md
# Ticket 2018032642002234

 # HPC-Support Ticket: FAU-CA Zertifikatinformation

## Keywords
- Certificate expiration
- Zertifikatinformation
- DFN-PKI-Team
- HPC-Support
- OTRS
- S/MIME-Zertifikat
- Private Key

## Summary
The user reported that a certificate had expired. The DFN-PKI-Team processed the certification request and provided the new certificate along with instructions for importing it into the browser. The HPC Admin noted that the S/MIME certificate for the HPC queue was generated and stored in OTRS, but the HPC does not have the private key.

## Root Cause
- Certificate expiration

## Solution
- The DFN-PKI-Team provided a new certificate with instructions for importing it.
- The HPC Admin noted the status of the S/MIME certificate for the HPC queue.

## General Learnings
- Ensure certificates are renewed before expiration.
- Follow the instructions provided by the DFN-PKI-Team for importing new certificates.
- Keep track of private keys for certificates to avoid issues with access.

## References
- [DFN-PKI-Team Instructions](https://pki.pca.dfn.de/dfn-ca-global-g2/cgi-bin/pub/pki?cmd=getStaticPage;name=index;id=2;RA_ID=4130)
- [Certificate Download Link](https://pki.pca.dfn.de/dfn-ca-global-g2/cgi-bin/pub/pki?cmd=getcert&key=9546288980230672617691361771&type=CERTIFICATE&RA_ID=4130)
- [Informationen für Zertifikatinhaber](https://info.pca.dfn.de/doc/Info_Zertifikatinhaber.pdf)
---

### 2023042442003323_Fritz_Alex%20Freischaltung%20cama204h.md
# Ticket 2023042442003323

 # HPC Support Ticket Analysis

## Subject: HPC Account Activation Request

### Keywords:
- HPC Account Activation
- CAMA Übung
- Certificate Expiration

### Summary:
A user requested the activation of an HPC account for a specific exercise. The HPC Admin noted that the certificate had expired and marked the issue as resolved.

### Root Cause:
- Certificate expiration

### Solution:
- The HPC Admin resolved the issue, likely by renewing the certificate.

### General Learnings:
- Certificate expiration can cause issues with HPC account activation.
- HPC Admins can resolve such issues by renewing the certificate.

### Notes:
- Ensure certificates are up-to-date to avoid disruptions in HPC account activation.
- Regularly check and renew certificates as part of maintenance procedures.
---

### 2020060142000531_support%20request.md
# Ticket 2020060142000531

 ```markdown
# HPC Support Ticket Analysis

## Subject: Support Request

### User Issue:
1. **Connection Issue with cshpc Front End**:
   - User can connect to `cshpc` but its front end is unresponsive.
   - Unable to process further commands (e.g., login to `woody`).

2. **Connection Issue with woody Front End**:
   - User can connect to `dialog` and log in to `woody`.
   - `woody`'s front end is unresponsive, rendering HPC unusable.

### HPC Admin Response:
- **Root Cause**: Certificate has expired.

### Keywords:
- Connection Issue
- Front End Unresponsive
- Certificate Expired
- cshpc
- woody
- dialog

### General Learnings:
- **Certificate Expiration**: Ensure certificates are up-to-date to avoid front-end responsiveness issues.
- **Front-End Unresponsiveness**: Can be caused by expired certificates.
- **Troubleshooting Steps**: Check certificate validity when encountering unresponsive front ends.

### Solution:
- **Renew Certificates**: Ensure all relevant certificates are renewed and updated to resolve front-end responsiveness issues.
```
---

### 2021022342003369_FAU-CA%20Zertifikatinformation.md
# Ticket 2021022342003369

 # HPC-Support Ticket: FAU-CA Zertifikatinformation

## Keywords
- Certificate expiration
- Zertifikatinformation
- DFN-PKI-Team
- OTRS/HPC-Gruppenzertifikat
- PKCS#12-Format
- Serverzertifikat
- CA-Zertifikate

## Problem
- Certificate has expired.

## Details
- The user received an email from the DFN-PKI-Team regarding the completion of their certification request.
- The certificate was issued with a serial number and specific details (CN, OU, O, L, ST, C).
- Instructions were provided for creating a certificate file in PKCS#12 format and accessing CA certificates.

## Solution
- The user needs to follow the instructions provided in the email to renew or create a new certificate.
- For a user certificate, visit the provided link to create a certificate file in PKCS#12 format.
- For a server certificate, download the CA certificates from the specified link and use the attached certificate.

## General Learnings
- Certificates need to be renewed annually.
- Follow the instructions in the email from the DFN-PKI-Team to create or renew certificates.
- Ensure compliance with the regulations outlined in the "Informationen für Zertifikatinhaber" document.

## Roles Involved
- **HPC Admins**: Responsible for managing and renewing certificates.
- **2nd Level Support Team**: Assists with technical issues related to certificates.
- **DFN-PKI-Team**: Provides instructions and support for certificate creation and renewal.

## References
- [DFN-PKI Certificate Creation](https://pki.pca.dfn.de/dfn-pki/dfn-ca-global-g2/4130/certificates/76962592)
- [CA Certificates](https://pki.pca.dfn.de/dfn-ca-global-g2/cgi-bin/pub/pki?cmd=getStaticPage;name=index;id=2;RA_ID=4130)
- [Informationen für Zertifikatinhaber](https://info.pca.dfn.de/doc/Info_Zertifikatinhaber.pdf)
---

### 2022091542003655_Meggie%2C%20High-Octane%20Motorsports%20e.V.md
# Ticket 2022091542003655

 # HPC Support Ticket Conversation Analysis

## Keywords
- HPC Accounts
- Account Verlängerung
- Meggie
- Fritz
- NHR Ressourcen
- Rechenzeit
- CPU core-h
- Professor:in
- Promovierte Mitarbeiter:in
- Antrag

## Summary
- **User Request**: Access to Meggie, extension of HPC accounts, and possibility to simulate on Fritz.
- **Root Cause**: Expiring HPC accounts and need for additional computational resources.
- **Solution**:
  - New HPC accounts for new team members.
  - Access to Meggie granted with new accounts.
  - NHR resource usage requires a special application from a professor or a PhD staff member.
  - Estimate of required CPU core-hours on Fritz needed for the application.

## Detailed Information
- **HPC Accounts**: New accounts should be requested for new team members instead of extending old ones.
- **Meggie Access**: Automatically granted with new HPC accounts.
- **Fritz Access**: Requires a formal application for NHR resources, to be submitted by a professor or a PhD staff member.
- **Rechenzeit**: User needs to estimate the required CPU core-hours for the application.

## Action Items
- **User**: Apply for new HPC accounts for new team members.
- **User**: Estimate the required CPU core-hours for Fritz.
- **User**: Submit a formal application for NHR resources through a professor or a PhD staff member.

## Notes
- Previous simulations were conducted on Emmy.
- The application process for Fritz follows the same procedure as for Starkstrom/Augsburg.

---

This report provides a concise summary of the support ticket conversation, highlighting the key points and actions required for both the user and the HPC support team.
---

### 2020010242000217_Kleinigkeit%20auf%20Webseite.md
# Ticket 2020010242000217

 ```markdown
# HPC-Support Ticket: Kleinigkeit auf Webseite

## Keywords
- Copy-Paste Problem
- Webseite
- SLURM
- Certificate Expiration

## Root Cause
- User identified a typographical error on the website, likely due to a copy-paste mistake.
- The text should read "for SLURM" instead of the current incorrect text.

## Solution
- HPC Admin acknowledged the issue and corrected the typographical error on the website.
- Additionally, the admin noted that a certificate had expired, indicating a secondary issue that was also addressed.

## General Learnings
- Regularly review website content for accuracy and consistency.
- Ensure that certificates are up-to-date to avoid expiration issues.
- Prompt user feedback can help identify and correct minor issues quickly.
```
---

### 2018080342000243_HPC-Antr%C3%83%C2%A4ge%20-%3E%20DFM.md
# Ticket 2018080342000243

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject: HPC-Anträge -> DFM

### Keywords:
- HPC-Anträge
- IDM/DFM
- OTRS-Tickets
- Account-Fragen
- Certificate Expired

### Root Cause of the Problem:
- Certificate has expired.
- HPC applications were not uploaded to IDM/DFM, making them difficult to find in future account-related queries.

### Solution:
- Always upload scanned HPC applications to IDM/DFM as a file.
- This ensures easier access and better organization compared to storing them in OTRS-Tickets.

### General Learnings:
- Utilize IDM/DFM for storing important documents related to HPC applications.
- Proper document management helps in resolving account-related issues more efficiently.
- Ensure certificates are up-to-date to avoid disruptions in service.
```
---

### 2021091442001464_iwtt013h.md
# Ticket 2021091442001464

 ```markdown
# HPC Support Ticket: iwtt013h

## Keywords
- Job execution failure
- Certificate expiration
- HPC cluster issue
- Problem resolution

## Summary
A user reported that their jobs were not being executed on the HPC cluster since the previous day. The HPC Admin identified the issue as a certificate expiration problem.

## Root Cause
- **Certificate Expiration**: The root cause of the job execution failure was identified as an expired certificate.

## Solution
- **Certificate Renewal**: The HPC Admin resolved the issue by renewing the certificate. The problem was fixed by 12:34 on the same day.

## Lessons Learned
- Regularly monitor and renew certificates to prevent job execution failures.
- Communicate with users promptly to confirm the resolution of issues.

## Follow-up
- Ensure that certificate expiration dates are tracked and renewed in a timely manner to avoid similar issues in the future.
```
---

### 2023102442002554_Extension%20MuCoSim%20Project%20in%20HPC%20Portal.md
# Ticket 2023102442002554

 # HPC Support Ticket: Extension MuCoSim Project in HPC Portal

## Keywords
- Project Extension
- HPC Portal
- Expired Certificate

## Summary
- **User Request**: Extend the project `muco100` (Seminar MuCoSim) in the HPC Portal to 30.04.2024.
- **HPC Admin Response**: Indicated that the certificate has expired.

## Root Cause
- The project extension request was not processed due to an expired certificate.

## Solution
- The HPC Admin acknowledged the request but noted the certificate expiration issue.

## General Learnings
- Ensure certificates are up-to-date before requesting project extensions.
- Communicate with HPC Admins to resolve certificate issues promptly.

## Next Steps
- Renew the expired certificate.
- Resubmit the project extension request once the certificate is valid.
---

### 2020030242000731_Job%20auf%20Meggie%20753030%20iwia023h.md
# Ticket 2020030242000731

 ```markdown
# HPC Support Ticket Analysis

## Subject: Job auf Meggie 753030 iwia023h

### Keywords:
- Job inactivity
- Meggie
- Certificate expiration

### Problem:
- User's job on Meggie shows no activity.
- Certificate has expired.

### Root Cause:
- The job is not performing any meaningful tasks.
- Possible issue with expired certificate.

### Solution:
- User is advised to check if the job is executing any useful tasks.
- No specific solution provided for the certificate expiration issue.

### General Learnings:
- Regularly monitor job activity to ensure they are performing as expected.
- Check for certificate expiration as it can affect job execution.

### Next Steps:
- User should verify job functionality.
- HPC Admins may need to address the certificate expiration issue.
```
---

### 2022092042003029_Tier3-Access-Fritz%20%22RUPAM%20GAYEN%22%20_%20mpt4022h.md
# Ticket 2022092042003029

 ```markdown
# HPC Support Ticket Analysis

## Subject
Tier3-Access-Fritz "RUPAM GAYEN" / mpt4022h

## Keywords
- Certificate expiration
- Compute time requirements
- Node hours
- Gromacs
- Molecular dynamics simulations
- Langevin Dynamics
- mdrun
- gmx command

## Problem
- **Root Cause**: The user provided an unrealistic compute time requirement of 40 node hours.
- **Additional Issue**: Certificate expiration mentioned by HPC Admin.

## Solution
- **Compute Time Requirement**: HPC Admin pointed out the need for a more realistic estimate of compute time requirements.
- **Certificate Expiration**: Not explicitly addressed in the conversation, but awareness of certificate expiration is noted.

## What Can Be Learned
- **Realistic Compute Time Estimates**: Users need to provide realistic estimates for compute time requirements.
- **Certificate Management**: Ensure certificates are up-to-date to avoid access issues.
- **Software Requirements**: Users should clearly specify the software they need (e.g., Gromacs, Intel MPI, Open MPI).
- **Application Details**: Providing detailed information about the application and expected outcomes helps in better resource allocation.

## Next Steps
- **User Follow-Up**: The user should be contacted to provide a more accurate estimate of compute time requirements.
- **Certificate Renewal**: Ensure the user's certificate is renewed if expired.
```
---

### 2023011242003182_woody%20down.md
# Ticket 2023011242003182

 # HPC Support Ticket: Woody Down

## Keywords
- Woody down
- Interactive job
- Connection aborted
- Certificate expired

## Summary
- **User Report**: User reported that the HPC system "woody" was down, causing an interruption in an interactive job and preventing further connections.
- **Root Cause**: The HPC Admin identified that the certificate had expired.

## Lessons Learned
- Regularly check and renew certificates for HPC systems to prevent downtime.
- Ensure users are informed about planned maintenance or potential downtimes.

## Solution
- Renew the expired certificate to restore access to the HPC system.

## Actions Taken
- HPC Admin identified the expired certificate as the root cause.
- No specific resolution steps were mentioned in the conversation.

## Next Steps
- Renew the certificate.
- Inform users about the resolution and any preventive measures for the future.
---

### 2021031042000251_Ihr%20Zertifikat%20der%20FAU-CA%20wird%20ablaufen.md
# Ticket 2021031042000251

 ```markdown
# HPC-Support Ticket: Expired Certificate

## Subject
Ihr Zertifikat der FAU-CA wird ablaufen

## Keywords
- Certificate expiration
- DFN-PKI
- Certificate renewal
- FAU-CA
- RRZE

## Problem
- The user's certificate with serial number 9546288980230672617691361771 and name CN=GRP: HPC-Support,OU=Regionales Rechenzentrum Erlangen (RRZE),O=Friedrich-Alexander-Universitaet Erlangen-Nuernberg,L=Erlangen,ST=Bayern,C=DE expired on 25.03.2021 at 15:29.

## Root Cause
- The certificate expiration date was reached without renewal.

## Solution
- The certificate was already renewed by a member of the 2nd Level Support team.

## Steps for Renewal (if needed in the future)
1. Open the DFN-PKI website: [DFN-PKI](https://pki.pca.dfn.de/dfn-ca-global-g2/cgi-bin/pub/pki?cmd=getStaticPage&name=index&RA_ID=4130)
2. Apply for a new certificate through the website.
3. Print the certificate application form.
4. Sign the form and submit it to the participant service either in person or by mail.
5. If the renewal is for a user certificate, ensure the last personal identification by the participant service is not older than 39 months. If it is, submit the form in person for re-identification.
6. The new certificate will be sent via email.

## Important Note
- Keep the old certificate to ensure access to encrypted data such as emails.

## Contact for Further Assistance
- For any questions, contact ca@fau.de.

## Conclusion
- The certificate was already renewed by the 2nd Level Support team, ensuring continued access to services and applications.
```
---

### 2023032242001367_HPC-Portal%20Technical%20Contact%20-%20b143dc%20-%20PatRo-MRI.md
# Ticket 2023032242001367

 # HPC-Support Ticket Conversation Analysis

## Subject
HPC-Portal Technical Contact - b143dc - PatRo-MRI

## Keywords
- HPC-Portal
- Technical Contact
- PatRo-MRI
- HPC-Support
- Certificate Expired

## Summary
A user requested to be added as a technical contact for the PatRo-MRI project in the HPC-Portal. The HPC Admin noted that the certificate had expired and marked the request as completed.

## Root Cause
- User requested to be added as a technical contact for a specific project.

## Solution
- HPC Admin added the user as a technical contact for the project.
- Noted that the certificate had expired.

## General Learnings
- Users may request to be added as technical contacts for specific projects.
- HPC Admins handle such requests and may note additional issues like expired certificates.

## Action Taken
- User was added as a technical contact for the PatRo-MRI project.
- Certificate expiration was noted.

## Follow-up
- Ensure that certificates are renewed to avoid expiration issues.
- Verify that users are correctly added as technical contacts for their respective projects.

## Documentation
This ticket can serve as a reference for handling requests to add users as technical contacts and addressing certificate expiration issues.
---

### 2022102442002449_Failure%20in%20running.md
# Ticket 2022102442002449

 ```markdown
# HPC Support Ticket: Failure in Running

## Keywords
- Job failure
- Error messages
- Certificate expiration
- Remote work

## Summary
A guest researcher reported being unable to run any calculations on the HPC cluster for the past two days. The HPC admin responded that there were no general issues over the weekend and requested more specific information about the problem.

## Root Cause
- The user did not provide specific error messages or details about the affected jobs.
- The HPC admin mentioned a certificate expiration issue, which could be related to the problem.

## Solution
- The user was asked to provide more specific details about the issue, including error messages and affected jobs.
- The professor of the user intervened to investigate the issue further.

## General Learnings
- Always request specific details about job failures, including error messages and affected job IDs.
- Certificate expiration can be a potential cause of job failures.
- Remote workers may face additional challenges in troubleshooting issues.

## Next Steps
- If similar issues arise, ensure that the user provides detailed error messages and job IDs.
- Check for any certificate-related issues that could be causing job failures.
- Consider the unique challenges faced by remote workers when providing support.
```
---

### 2023022042000819_Job%20Verl%C3%83%C2%A4ngerung.md
# Ticket 2023022042000819

 ```markdown
# HPC-Support Ticket: Job Verlängerung

## Keywords
- Job Extension
- Job-ID
- Laufzeit
- Expired Certificate

## Summary
A user requested an extension of a job's runtime to 2 days. The HPC Admin responded with a note about an expired certificate and marked the issue as resolved.

## Root Cause
- User requested an extension for Job-ID: 685461.

## Solution
- The HPC Admin noted that the certificate had expired and marked the issue as resolved.

## General Learning
- Users may request runtime extensions for their jobs.
- Admins should check for any related issues, such as expired certificates, when handling such requests.
- Ensure clear communication about the status of the request and any related issues.
```
---

### 2022021642002247_Early-Fritz%20%22Kajol%20Kulkarni%22%20_%20iwia041h.md
# Ticket 2022021642002247

 # HPC Support Ticket Analysis

## Keywords
- **Certificate Expiration**
- **Single-Node Partition**
- **Fritz Cluster**
- **WaLBerla Software**
- **Fluid Dynamics Dataset**
- **Deep Learning Models**
- **Infiniband HCAs**
- **Documentation**

## Summary
- **User Request:** Access to single-node partition of Fritz cluster for fluid dynamics simulations using WaLBerla software.
- **HPC Admin Response:** Enabled user for the single-node partition and provided documentation link.
- **Root Cause:** Certificate expiration issue mentioned but not detailed.
- **Solution:** User was granted access to the required partition.

## What Can Be Learned
- **Access Granting:** HPC Admins can enable users for specific partitions of the cluster.
- **Documentation:** Important to provide users with relevant documentation links.
- **Certificate Management:** Ensure certificates are up-to-date to avoid expiration issues.
- **Software Requirements:** Users may need specific software (e.g., WaLBerla) for their projects.
- **Collaboration:** Users may request access for additional team members (e.g., master students).

## Action Items
- **Monitor Certificates:** Regularly check and update certificates to prevent expiration.
- **Documentation Update:** Ensure documentation is comprehensive and up-to-date.
- **User Support:** Provide clear instructions and links to relevant resources when enabling access.

## Additional Notes
- **Project Details:** The user aims to create a public fluid dynamics dataset for training deep learning models.
- **Resource Allocation:** The user requested 100,000 hours of compute time.

This analysis can serve as a reference for future support tickets involving similar requests or issues.
---

### 2024020842000153_Ihr%20Zertifikat%20der%20FAU-CA%20wird%20ablaufen.md
# Ticket 2024020842000153

 ```markdown
# HPC-Support Ticket: Expiring DFN-PKI Certificate

## Keywords
- DFN-PKI Global
- Certificate Expiration
- GÉANT TCS
- OTRS-Mailzertifikat
- Certificate Renewal

## Problem
- The user received a notification that their DFN-PKI Global certificate with the serial number 11244016397729298610945101408 will expire on 23.02.2024 at 20:29.
- The notification also mentioned that new certificates are now issued through the GÉANT TCS service.

## Root Cause
- The certificate was set to expire, and the user was informed about the new process for obtaining certificates.

## Solution
- The HPC Admin noted that the OTRS-Mailzertifikat for HPC-Support had already been renewed and switched to GÉANT in January.
- Therefore, the DFN warning was deemed obsolete.

## What to Learn
- Certificates issued by DFN-PKI Global are no longer valid after 30.08.2023.
- New certificates should be obtained through the GÉANT TCS service.
- It is important to check and renew certificates before their expiration to avoid service disruptions.
- Communication with the local participant service is crucial for understanding the new application procedures.

## Actions Taken
- The HPC Admin confirmed that the certificate had already been renewed and the warning was no longer relevant.
- The ticket was closed as the issue had been resolved.
```
---

### 2021022442003152_Test%3A%20Neues%20Gruppenzertifikat.md
# Ticket 2021022442003152

 # HPC Support Ticket: Test - New Group Certificate

## Keywords
- Certificate
- Expired
- Test
- Group Certificate

## Summary
- **Issue**: The certificate has expired.
- **Context**: This ticket was a test and should be ignored.
- **Action**: The test was successfully completed.

## Root Cause
- The certificate had expired, which triggered the test scenario.

## Solution
- The test was concluded successfully, indicating that the process for handling expired certificates is functional.

## General Learning
- Regular tests for handling expired certificates are important to ensure system reliability.
- Successful test completion confirms the effectiveness of the current procedures.

## Roles Involved
- **HPC Admins**: Managed the test scenario.
- **2nd Level Support Team**: Involved in the test process.

## Conclusion
- The test for handling expired certificates was successful, demonstrating the robustness of the system and procedures in place.
---

### 2022051242001777_fritz%20-%20ReqNodeNotAvail.md
# Ticket 2022051242001777

 ```markdown
# HPC-Support Ticket: ReqNodeNotAvail

## Keywords
- ReqNodeNotAvail
- Job Submission
- squeue
- Node Availability
- Certificate Expiration

## Summary
A user reported that their jobs submitted to the HPC cluster "fritz" were showing the status "ReqNodeNotAvail" when checked with `squeue`. The user inquired about the reason for this issue and whether they needed to register their jobs differently.

## Root Cause
- The user's jobs were not being scheduled due to the unavailability of required nodes.
- The HPC admin identified that the certificate had expired.

## Solution
- The HPC admin noted that the certificate had expired, indicating a potential system-wide issue affecting node availability.
- No specific solution was provided in the conversation, but the issue was acknowledged by the HPC admin.

## General Learnings
- The error message "ReqNodeNotAvail" indicates that the required nodes for the job are not available.
- Certificate expiration can lead to node availability issues.
- Users should check for system-wide issues or contact HPC support if they encounter this error.

## Next Steps
- HPC admins should investigate and resolve the certificate expiration issue.
- Users should monitor the status of their jobs and contact HPC support if the issue persists.
```
---

### 2023062142004413_Job%20extension.md
# Ticket 2023062142004413

 ```markdown
# HPC-Support Ticket: Job Extension

## Keywords
- Job extension
- Expired certificate
- HPC-Support

## Summary
- **User Request**: Extension of job with ID 766841 for two days.
- **HPC Admin Response**: Certificate has expired; job extension completed.

## Root Cause
- User required additional time for their job to complete.

## Solution
- HPC Admin extended the job duration as requested.

## General Learnings
- Users may need job extensions due to longer-than-expected processing times.
- Certificate expiration can be a factor in job management.
- Quick and friendly support is appreciated by users.
```
---

### 2022101542000431_Unable%20to%20login.md
# Ticket 2022101542000431

 ```markdown
# HPC Support Ticket: Unable to Login

## Keywords
- Login issue
- Remote access
- Server side problem
- Account problem
- Certificate expiration

## Summary
A user reported being unable to login to the server remotely. The issue occurred suddenly, with no problems the previous day. The user received welcome messages and notices but was not returned to the base node.

## Root Cause
- The user's certificate had expired.

## Solution
- The HPC Admin confirmed that there were no server-side issues and that the user's account was not problematic.
- The user was able to access the server again after the certificate issue was addressed.

## Lessons Learned
- Certificate expiration can cause sudden login issues.
- Regularly check and renew certificates to avoid access problems.
- Verify server-side issues and account status when troubleshooting login problems.
```
---

### 2020060342003767_Application%20of%20using%20Meggie%20cluster.md
# Ticket 2020060342003767

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject: Application of using Meggie cluster

### Keywords:
- Meggie cluster
- Parallel lattice Boltzmann simulations
- LB3D simulation package
- MPI parallelization
- Batch job submission
- Certificate expiration

### Summary:
A user requested access to the Meggie cluster to run parallel lattice Boltzmann simulations using the LB3D package, which is parallelized with MPI. The user had experience with similar simulations on other clusters and supercomputers but was unable to submit batch jobs on Meggie.

### Root Cause of the Problem:
- The user was unable to submit batch jobs despite being able to log in.
- The HPC Admin identified that the certificate had expired.

### Solution:
- The HPC Admin noted that the certificate had expired and marked the request as resolved.

### General Learnings:
- Certificate expiration can prevent users from submitting batch jobs.
- Users should ensure their certificates are up-to-date for uninterrupted access to HPC resources.
- HPC Admins should regularly check and renew certificates to avoid such issues.

### Relevant Roles:
- **HPC Admins**: Thomas, Michael Meier, Anna Kahler, Katrin Nusser, Johannes Veh
- **2nd Level Support Team**: Lacey, Dane (fo36fizy), Kuckuk, Sebastian (sisekuck), Lange, Florian (ow86apyf), Ernst, Dominik (te42kyfo), Mayr, Martin
- **Head of the Datacenter**: Gerhard Wellein
- **Training and Support Group Leader**: Georg Hager
- **NHR Rechenzeit Support and Applications for Grants**: Harald Lanig
- **Software and Tools Developer**: Jan Eitzinger, Gruber
```
---

### 2022042542003163_Early-Fritz%20%22Simon%20Sch%C3%83%C2%A4fer%22%20_%20mfbi000h.md
# Ticket 2022042542003163

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject: Early-Fritz "Simon Schäfer" / mfbi000h

### Keywords:
- Certificate expiration
- User access
- Special software installation
- File-IO strategies
- Sequencing workflows
- Benchmarking
- HPC resources
- ScRNA Cellranger
- CITE-seq-Count

### Summary:
- **Root Cause**: Certificate expiration.
- **Solution**: HPC Admin granted access to the user on Fritz.
- **Additional Information**:
  - User needs to install special software (10X Genomics Cellranger and CITE-seq-Count) themselves.
  - Discussion on File-IO strategies is suggested due to the importance of File-IO in sequencing workflows.
  - User's application involves benchmarking highly parallel workflows with high CPU/RAM demands.
  - Expected outcomes include reducing analysis time for ScRNA datasets from days to hours using HPC resources.

### Lessons Learned:
- Ensure certificates are up-to-date to avoid access issues.
- Users should be aware they may need to install special software themselves.
- File-IO strategies are crucial for optimizing sequencing workflows.
- Benchmarking can help identify bottlenecks and improve workflow efficiency.

### Next Steps:
- Monitor certificate expiration dates to prevent future access issues.
- Provide guidance or documentation on installing special software.
- Schedule discussions on File-IO strategies for users involved in sequencing workflows.
- Continue to support benchmarking efforts to optimize workflows and resource utilization.
```
---

### 2023101142003265_frozen%20jobs%20woodycap6%202384656%20to%2074.md
# Ticket 2023101142003265

 ```markdown
# HPC Support Ticket: Frozen Jobs on woodycap6

## Keywords
- Frozen jobs
- Job termination
- woodycap6
- Job IDs
- Certificate expiration

## Problem Description
- **User Issue**: Jobs on woodycap6 with IDs 2384656 to 2384674 are frozen and cannot be canceled.
- **Root Cause**: Certificate has expired.

## Solution
- **Action Taken**: HPC Admins removed the frozen jobs.
- **Follow-up**: User was informed about the removal of the jobs.

## General Learnings
- **Certificate Management**: Ensure certificates are up-to-date to prevent job freezing issues.
- **Job Termination**: HPC Admins can manually terminate frozen jobs upon user request.

## Recommendations
- **Monitoring**: Regularly check for certificate expiration dates.
- **Communication**: Inform users about the importance of reporting frozen jobs promptly.
```
---

### 2023022842000279_Jobverl%C3%83%C2%A4ngerung.md
# Ticket 2023022842000279

 ```markdown
# HPC-Support Ticket: Jobverlängerung

## Keywords
- Jobverlängerung (Job Extension)
- Expired Certificate

## Problem
- User requested an extension for job ID 690067.

## Root Cause
- The certificate associated with the job had expired.

## Solution
- The HPC Admin resolved the issue by addressing the expired certificate.

## Lessons Learned
- Ensure that certificates are up-to-date to avoid job interruptions.
- Regularly check and renew certificates as part of routine maintenance.
```
---

### 2023051742002818_Fritz%20Freischaltung.md
# Ticket 2023051742002818

 # HPC Support Ticket: Fritz Freischaltung

## Keywords
- Fritz Freischaltung
- CAMA Übung
- Account Freischaltung
- cama100 Accounts

## Summary
A user requested the activation of specific accounts for the CAMA exercise. The HPC Admin responded with a list of activated accounts and noted that a certificate had expired.

## Root Cause
- User required activation of specific accounts for an exercise.

## Solution
- HPC Admin activated the requested accounts and noted the expiration of a certificate.

## What Can Be Learned
- Procedure for activating accounts for specific exercises.
- Importance of checking certificate validity during account activation.

## Example
```plaintext
User: Hallo,
Ich bitte um eine Fritz Freischaltung zwecks der Durchführung der CAMA
Übung für die Accounts cama220h-cama225h, das müssten alle verbleibenden
cama100 Accounts sein die noch keine Freischaltung haben.
Vielen Dank,
Dominik Ernst

HPC Admin: ; certificate has expired
erledigt. Freigeschaltet sind jetzt
fritz|cama|cama204h||1|||node=8||||||||||normal|||
fritz|cama|cama205h||1|||node=4||||||||||normal|||
...
fritz|cama|cama225h||1|||node=4||||||||||normal|||
```

## Notes
- Ensure all requested accounts are activated.
- Check for any expired certificates during the activation process.
---

### 2018040642001422_IGNORE%20-%20Kryptotests.md
# Ticket 2018040642001422

 # HPC-Support Ticket: IGNORE - Kryptotests

## Keywords
- Encrypted emails
- OTRS
- Certificate expiration
- Email forwarding
- Signature

## Problem
- **Root Cause**: Certificate expiration and issues with handling encrypted emails in the OTRS system.
- **Details**: Encrypted emails sent to HPC support were decrypted and displayed in the web interface, but forwarding these emails resulted in missing content, only showing a hint about a non-existent attachment. Additionally, the system could not send encrypted replies to signed emails.

## Solution
- **Status**: No clear solution provided in the conversation.
- **Next Steps**: Investigate the OTRS system's handling of encrypted emails and certificate renewal processes. Ensure that the system can properly forward decrypted content and send encrypted replies to signed emails.

## General Learnings
- Encrypted emails can cause issues with forwarding and replying in the OTRS system.
- Certificate expiration can lead to problems with email encryption and decryption.
- The OTRS system has a field for encryption, but its functionality may be limited.

## Actions for Support Employees
- Check the status of email certificates regularly to prevent expiration.
- Test the handling of encrypted emails in the OTRS system to ensure proper forwarding and replying.
- Document any workarounds or solutions for handling encrypted emails and certificate issues.
---

### 2023020442000215_Error%20in%20log%20in.md
# Ticket 2023020442000215

 ```markdown
# HPC Support Ticket: Error in Login

## Keywords
- Login error
- Certificate expired
- SSH connection
- FAQ reference

## Summary
A user reported login issues over the past two days. The HPC Admin identified the root cause as an expired certificate.

## Conversation Details
1. **User Report**:
   - User reported facing login problems for the past two days.

2. **HPC Admin Response**:
   - Requested more specific details about the command or script used for login.
   - Identified that "connect" is not a command installed on the system.

3. **User Clarification**:
   - User specified that they were trying to connect to "fritz" and encountered an error.

4. **HPC Admin Solution**:
   - Informed the user that the certificate had expired.
   - Directed the user to the FAQs for further assistance: [FAQs](https://hpc.fau.de/faqs/#innerID-13183)

## Root Cause
- Expired certificate causing login issues.

## Solution
- Refer to the FAQs for resolving certificate expiration issues: [FAQs](https://hpc.fau.de/faqs/#innerID-13183)
```
---

### 2018061242000891_Jobs%20auf%20Meggie%20-%20nfcc02.md
# Ticket 2018061242000891

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject: Jobs auf Meggie - nfcc02

### Keywords:
- Job failure
- Job stalling
- Certificate expiration

### Summary:
- **Issue**: Jobs on Meggie stopped working shortly after 9 AM and were stalling.
- **Root Cause**: Certificate expiration.
- **Solution**: Not explicitly stated, but the issue was resolved as the user confirmed that the jobs were running again.

### Lessons Learned:
- **Certificate Management**: Ensure that certificates are up-to-date to prevent job failures.
- **Job Monitoring**: Regularly monitor job status to quickly identify and address issues.
- **User Communication**: Promptly inform users about job status and resolution steps.

### Action Items:
- **HPC Admins**: Implement a system to track and renew certificates before they expire.
- **2nd Level Support**: Assist users in restarting jobs and provide guidance on preventing similar issues.
- **Head of Datacenter/Training and Support Group Leader**: Ensure that certificate management is included in regular maintenance protocols.

### Conclusion:
This ticket highlights the importance of proactive certificate management and effective communication with users to minimize job disruptions.
```
---

### 2023041842000311_Zugang%20Fritz%20Aditya%20Ujeniya.md
# Ticket 2023041842000311

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject: Zugang Fritz Aditya Ujeniya

### Keywords:
- Access Request
- Account Management
- Testing and Benchmarking
- Certificate Expiration

### Summary:
- **User Request:** Access to "fritz" for a specific user account (ihpc118h) for testing and benchmarking PAMPI NuSiF codes.
- **HPC Admin Response:** Access granted, but noted that the certificate has expired.

### Root Cause of the Problem:
- User required access to a specific HPC resource for testing and benchmarking purposes.

### Solution:
- HPC Admins granted the requested access.
- Noted that the certificate had expired, implying potential follow-up actions might be needed for certificate renewal.

### General Learnings:
- Importance of timely access requests for HPC resources.
- Awareness of certificate expiration and the need for regular renewals.
- Collaboration between software developers and HPC admins for resource allocation.
```
---

### 2023022442000517_Job%20Verl%C3%83%C2%A4ngerung.md
# Ticket 2023022442000517

 ```markdown
# HPC Support Ticket: Job Verlängerung

## Keywords
- Job extension
- Laufzeit
- Job id
- Expired certificate

## Summary
A user requested an extension of a job's runtime to 2 days. The HPC Admin responded with a note about an expired certificate and marked the issue as resolved.

## Root Cause
- User requested an extension for a specific job (Job id: 687999).

## Solution
- The HPC Admin noted that the certificate had expired and marked the issue as resolved.

## General Learning
- Users may request extensions for job runtimes.
- Admins should check for any related issues, such as expired certificates, when handling such requests.
- Ensure proper communication and resolution documentation for future reference.
```
---

### 2022102342000185_Tier3-Access-Fritz%20%22Johannes%20Schr%C3%83%C2%B6der%22%20_%20iwpa070h.md
# Ticket 2022102342000185

 ```markdown
# HPC Support Ticket Conversation Analysis

## Subject: Tier3-Access-Fritz "Johannes Schröder" / iwpa070h

### Keywords:
- Account Activation
- Tier3 Access
- Multi-node Workload
- OpenFOAM
- CalculiX
- preCICE
- ParaView
- Fluid-Structure Interactions
- Research

### Summary:
- **User Request:** Access to HPC resources for multi-node workload.
- **Resources Requested:**
  - 1800 node hours on Fritz
  - Software: OpenFOAM, CalculiX, preCICE, ParaView
- **Application:** Turbulent Fluid-Structure Interactions for research and Ph.D. thesis.

### Issue:
- **Root Cause:** Certificate expiration.

### Solution:
- **HPC Admin Action:** Account activation on Fritz.
- **Notification:** User informed about account activation and resource availability.

### General Learnings:
- **Account Management:** Ensure certificates are up-to-date to avoid access issues.
- **Resource Allocation:** Understand the specific resource needs (e.g., node hours, software) for user projects.
- **Communication:** Clearly communicate the status of account activation and resource availability to users.

### Relevant Roles:
- **HPC Admins:** Thomas Zeiser
- **2nd Level Support Team:** Lacey, Dane (fo36fizy), Kuckuk, Sebastian (sisekuck), Lange, Florian (ow86apyf), Ernst, Dominik (te42kyfo), Mayr, Martin
- **Datacenter Head:** Gerhard Wellein
- **Training and Support Group Leader:** Georg Hager
- **NHR Rechenzeit Support:** Harald Lanig
- **Software and Tools Developer:** Jan Eitzinger, Gruber
```
---

### 2019041642002384_Zugang%20Meggie.md
# Ticket 2019041642002384

 ```markdown
# HPC-Support Ticket Conversation: Zugang Meggie

## Keywords
- Access Request
- Meggie Cluster
- waLBerla
- Strömungssimulationen
- Certificate Expired

## Summary
A user requests access to the Meggie Cluster to run flow simulations using waLBerla. The HPC Admin notes that the certificate has expired and marks the issue as resolved.

## Root Cause
- User requires access to the Meggie Cluster for running simulations.
- Certificate expiration issue noted by the HPC Admin.

## Solution
- The HPC Admin acknowledges the request and marks the issue as resolved, indicating that the certificate expiration was addressed.

## General Learnings
- Users may request access to specific clusters for running simulations.
- Certificate expiration can be a common issue that needs to be addressed by HPC Admins.
- Quick resolution and acknowledgment of access requests are important for user satisfaction.
```
---

### 2023091942000194_%5BDFN%232023091910000146%5D%20Zertifikat%20l%C3%83%C2%A4uft%20ab%20_%20certificate%20about%20to%20e.md
# Ticket 2023091942000194

 # HPC Support Ticket Analysis: Certificate Expiration

## Keywords
- Certificate expiration
- Renewal process
- DFN AAI
- HPC portal
- SAML metadata
- Rollover phase

## Summary
A certificate for the HPC portal is about to expire, and the HPC Admins need to renew it following the documented process.

## Root Cause
- The certificate for `portal.hpc.fau.de` is set to expire on 2023-10-17.

## Details
- **Certificate Information:**
  - Subject: `CN=portal.hpc.fau.de,O=Friedrich-Alexander-Universität Erlangen-Nürnberg,ST=Bayern,C=DE`
  - Fingerprint: `3bcf8db5beb8c96fe6ec3ea07e1343cf210e22c45b7a500cff1929c1e8e4ae17`
  - Entity ID: `https://portal.hpc.fau.de/saml/metadata`
  - Expiration Date: `2023-10-17 23:59:59`

- **Renewal Instructions:**
  - Documentation available at [DFN AAI Certificates](https://doku.tid.dfn.de/en:certificates)

- **Additional Notes:**
  - The 2022-2023 certificate is used only for signing in the backend code and DFN-AAI app.
  - The 2023-2024 certificate is used for both signing and encryption in the backend code and DFN-AAI app.
  - Rollover Phase 2 is mentioned.

## Solution
- HPC Admins should renew the certificate before the expiration date following the instructions provided in the [DFN AAI Certificates documentation](https://doku.tid.dfn.de/en:certificates).

## General Learnings
- Regularly monitor certificate expiration dates.
- Follow documented procedures for certificate renewal.
- Ensure proper communication and coordination among HPC Admins and the 2nd Level Support team.
---

### 2023033042003001_Tier3-Access-Fritz%20%22Stefan%20de%20Souza%22%20_%20ihpc115h.md
# Ticket 2023033042003001

 # HPC Support Ticket Analysis

## Keywords
- HPC Account Activation
- Certificate Expiration
- Resource Allocation (Single-node throughput)
- Software Requirements (Own benchmarks, likwid-bench, LINPACK)
- Master Thesis Work
- Power Consumption Modeling

## Summary
- **User Request**: Access to HPC resources for master thesis work on power consumption modeling.
- **Resources Requested**: Single-node throughput (72 cores, 250 GB), 4000 node hours on Fritz.
- **Software Needed**: Own benchmarks, likwid-bench, LINPACK.
- **Issue**: Certificate expiration.
- **Solution**: HPC account enabled by HPC Admin.

## Lessons Learned
- **Certificate Management**: Ensure certificates are up-to-date to avoid access issues.
- **Resource Allocation**: Proper justification is required for special resource requests.
- **Communication**: Clear and detailed communication of needs and expected outcomes is crucial for efficient support.

## Root Cause
- Expired certificate causing account access issues.

## Solution
- HPC Admin enabled the user's account after verifying the request.

## Future Reference
- Regularly check and update certificates to prevent access disruptions.
- Ensure detailed documentation of resource requests and justifications for efficient processing.
---

### 2020062342000606_Nodes%20TG001%2C%20TG002%2C%20TG005%20down.md
# Ticket 2020062342000606

 # HPC Support Ticket: Nodes Down After Job Completion

## Keywords
- Nodes down
- Job completion
- Queue status
- Reboot
- Certificate expiration

## Problem Description
- Nodes TG001, TG002, TG005 are down after job completion.
- Jobs are still marked as running in the queue despite completion.
- Epilogue is written to the logfile, indicating job completion.

## Root Cause
- Unclear from the conversation, but possibly related to a certificate expiration issue.

## Solution
- HPC Admins rebooted the affected nodes.

## Lessons Learned
- Nodes can become unresponsive after job completion due to various reasons, including certificate issues.
- Rebooting the nodes can resolve the issue.
- Monitoring certificate expiration dates is crucial to prevent such issues.

## Actions Taken
- HPC Admins rebooted the nodes to resolve the issue.

## Follow-up
- Ensure certificates are up-to-date to prevent similar issues in the future.
- Monitor node status and job queue for any discrepancies.
---

### 2022052142000635_Tier3-Access-Fritz%20%22RINITA%20SHAI%22%20_%20lo05pymu%40fau.de.md
# Ticket 2022052142000635

 ```markdown
# HPC Support Ticket Analysis

## Subject
Tier3-Access-Fritz "RINITA SHAI" / lo05pymu@fau.de

## Keywords
- Access Request
- Certificate Expiration
- Single-Node Throughput
- Software Requirements
- Resource Allocation

## Summary
A user requested access to the Fritz HPC system for a specific project. The request included details about the required resources, software, and expected outcomes.

## Root Cause
- **Certificate Expiration**: The user's certificate had expired.

## Solution
- **Existing Access**: The HPC Admin informed the user that they already had access to the Fritz system under a different user ID (ptfs155h).

## Lessons Learned
- **Access Verification**: Always verify if the user already has access under a different user ID.
- **Certificate Management**: Ensure that certificates are up-to-date to avoid access issues.
- **Resource Allocation**: Understand the specific resource requirements (e.g., single-node throughput) and software needs (e.g., C/C++, Matlab, Python) for effective support.

## Actions Taken
- The HPC Admin confirmed the user's existing access and provided relevant information.

## Follow-Up
- Ensure the user is aware of their existing access and can proceed with their project.
- Monitor certificate expiration dates to prevent future access issues.
```
---

### 2022113042002739_Alex%20Head%20Node%20not%20reachable.md
# Ticket 2022113042002739

 ```markdown
# HPC-Support Ticket: Alex Head Node Not Reachable

## Keywords
- Head Node
- Connectivity Issue
- Certificate Expiration
- Uni Network
- Alex1
- Alex2

## Summary
A user reported being unable to connect to the head nodes `alex1` and `alex2` from the university network. The root cause was identified as an expired certificate.

## Root Cause
- **Certificate Expiration**: The user mentioned that the certificate had expired, which likely caused the connectivity issue.

## Solution
- **Certificate Renewal**: The HPC Admins need to renew the expired certificate to restore connectivity to the head nodes.

## Actions Taken
- The user reported the issue via email.
- The HPC Admins were informed about the certificate expiration.

## Lessons Learned
- Regularly monitor and renew certificates to prevent connectivity issues.
- Ensure users are aware of the certificate expiration dates and the process for reporting such issues.

## Next Steps
- Renew the expired certificate.
- Inform users once the issue is resolved.
- Schedule regular checks for certificate expiration to prevent future incidents.
```
---

### 2024031542002485_Gridzertifikat%20Vorstellung.md
# Ticket 2024031542002485

 # HPC-Support Ticket: Grid Certificate Application

## Keywords
- Grid-Userzertifikat
- Akkreditierung
- Signierte Email
- Personalausweis
- Server-Zertifikat

## Problem
- User has a completed application for a Grid user certificate and accreditation.
- Unsure where and when to submit the application.

## Solution
- HPC Admin instructs the user to send both documents via signed email.
- User inquires about sending a copy of their ID instead of a personal presentation.
- HPC Admin approves the user's personal certificate.
- User clarifies that the server certificate application was a mistake.

## General Learnings
- Users can submit Grid certificate applications via signed email.
- Personal identification can be verified through a copy of an ID.
- Misunderstandings can occur when application processes are described together.

## Root Cause
- User confusion about the submission process for Grid certificate applications.

## Resolution
- HPC Admin provides clear instructions for submitting the application.
- User follows the instructions and the certificate is approved.

## Notes
- Ensure that application processes are clearly distinguished to avoid user confusion.
- Personal identification can be handled through digital means.
---

### 42015370_Grid-Zertifiikat.md
# Ticket 42015370

 # HPC Support Ticket: Grid-Zertifikat

## Keywords
- Grid-Zertifikat
- SX9 Zugriff
- OpenSSL
- Zertifikatsantrag
- DFN-Policy
- Serverzertifikat
- pkcs12-Keystore

## Problem
- User requires a Grid-Zertifikat for easier access to the SX9 system.
- User needs guidance on obtaining and configuring the certificate.

## Solution
1. **Information Source**:
   - Updated web pages for applying for Grid-Zertifikate: [RRZE Grid Zertifikate](http://www.rrze.uni-erlangen.de/dienste/arbeiten-rechnen/hpc/grid/zertifikate.shtml)

2. **Steps to Obtain Certificate**:
   - Generate a private key and certificate request using OpenSSL.
   - Convert the certificate into a pkcs12-Keystore suitable for Unicore.
   - Use the provided personalized OpenSSL configuration file.
   - Ensure the CN-Feld follows DFN-Policy by prefixing the name with "EXT:".

3. **Submission**:
   - Sign and scan the certificate application.
   - Send the signed application via email or fax to the HPC Admin.
   - Identity verification documents are not required.

4. **Follow-Up**:
   - User prepared and sent the certificate application via fax.
   - Further steps will be handled later.

## General Learnings
- Grid-Zertifikate simplify access to specific HPC systems like SX9.
- The process involves generating keys, submitting applications, and following specific policies.
- HPC Admins provide detailed guidance and necessary configuration files.

## Root Cause
- User needed a Grid-Zertifikat for easier access to the SX9 system and required guidance on the application process.

## Solution Found
- HPC Admin provided detailed instructions and necessary resources for obtaining and configuring the Grid-Zertifikat.
---

### 2023092542003509_HPC%20Verl%C3%83%C2%A4ngerung%20f%C3%83%C2%BCr%20Wintersemester.md
# Ticket 2023092542003509

 ```markdown
# HPC Support Ticket Conversation Analysis

## Subject
HPC Verlängerung für Wintersemester

## Keywords
- HPC Account Verlängerung
- Wintersemester 23/24
- Account Expiration
- Certificate Expired

## Root Cause of the Problem
- User requested an extension for an HPC account for a student.
- The initial request was delayed due to an expired certificate.

## Solution
- The HPC Admin extended the account until 31.03.2024.

## What Can Be Learned
- Ensure that certificates are up-to-date to avoid delays in processing requests.
- Communicate clearly with users about the status of their requests and any issues that arise.

## Actions Taken
- HPC Admin extended the account after resolving the certificate issue.

## General Notes
- Always check for expired certificates when processing account extensions.
- Maintain clear communication with users regarding the status of their requests.
```
---

### 2022061542001715_Schwachstellen%20findings.md
# Ticket 2022061542001715

 ```markdown
# HPC-Support Ticket: Schwachstellen Findings

## Keywords
- Schwachstellen
- Certificate expired
- TLS configuration
- Security scan
- FAU-Netzwerk
- SSL Labs

## Problem
- **Root Cause:** Certificate expiration on the monitoring server (131.188.202.70).
- **Details:** Daily security scans identified vulnerabilities in the FAU network, specifically an expired certificate on the monitoring server.

## Solution
- **Action Taken:** HPC Admins improved the TLS configuration for the service.
- **Outcome:** The service received an A grading on SSL Labs.

## General Learnings
- Regular security scans are essential for identifying vulnerabilities.
- Prompt action is necessary to address expired certificates.
- Improving TLS configurations can enhance security ratings.
- Collaboration between security teams and HPC Admins is crucial for network security.
```
---

### 2020121742001909_Account%20Verl%C3%83%C2%A4ngerung.md
# Ticket 2020121742001909

 ```markdown
# HPC Support Ticket: Account Verlängerung

## Keywords
- Account Verlängerung (Extension)
- HPC Account
- IDM
- Expired Certificate

## Summary
A user requested an extension for their master student's HPC account until August 2021. The HPC Admin responded by noting that the certificate had expired and marked the issue as resolved.

## Root Cause
- User requested an account extension.
- Certificate expiration was noted by the HPC Admin.

## Solution
- The HPC Admin acknowledged the request and noted the certificate expiration.
- No further action was specified, but the issue was marked as resolved.

## Lessons Learned
- Ensure that account extension requests are handled promptly.
- Check for certificate expiration when processing account extensions.
- Communicate clearly with users about the status of their requests and any issues encountered.
```
---

### 2020120242002972_Usage%20report.md
# Ticket 2020120242002972

 # HPC Support Ticket: Usage Report

## Keywords
- Usage report
- Attachment
- Certificate expiration

## Summary
A user submitted a usage report on behalf of their research group but encountered an issue with the certificate expiration.

## Root Cause
- The certificate for the usage report link had expired.

## Solution
- The HPC Admin acknowledged the issue and provided a link to the usage report with an updated certificate.

## Lessons Learned
- Ensure that certificates for links provided to users are up-to-date.
- Users should be informed about the importance of checking certificate validity when accessing links.

## Actions Taken
- HPC Admin provided a new link with an updated certificate.

## Follow-Up
- No further action required from the user.
- HPC Admin should monitor certificate expiration dates to prevent similar issues in the future.
---

### 2023110242002352_G%C3%83%C2%89ANT%20TCS%20certificate%20information%3A%20moodle.nhr.fau.de.md
# Ticket 2023110242002352

 # HPC Support Ticket: GÉANT TCS Certificate Renewal for moodle.nhr.fau.de

## Keywords
- Certificate Renewal
- moodle.nhr.fau.de
- DFN-PKI
- Apache
- DFN-AAI
- Shibboleth
- Rollover

## Summary
A certificate renewal request for `moodle.nhr.fau.de` was processed and approved. The new certificate was integrated into the Apache server, and a rollover process was initiated for DFN-AAI.

## Timeline
1. **Certificate Request**: A certificate renewal request was submitted and awaiting approval.
   - **Common Name**: `moodle.nhr.fau.de`
   - **SANs**: `moodle.nhr.fau.de`, `www.moodle.nhr.fau.de`, `moodle.nhr.uni-erlangen.de`, `www.moodle.nhr.uni-erlangen.de`
   - **Profile**: OV Multi-Domain
   - **Term**: 365 Days

2. **Approval**: The certificate request was approved by the administrator.
   - **Approved**: 02/11/2023 12:38 GMT
   - **Expires**: 01/11/2024 23:59 GMT

3. **Certificate Issuance**: The certificate was issued and download links were provided for various formats.

4. **Integration**:
   - The new certificate was integrated into the Apache server.
   - DFN-AAI rollover process was started with the new certificate added as signing.

5. **Final Configuration**:
   - The new certificate was set for both signing and encryption.
   - The old certificate was retained for signing only.
   - `shibboleth2.xml` was updated, and Moodle was restarted.

## Lessons Learned
- **Certificate Renewal Process**: Understanding the steps involved in renewing a certificate, from request to integration.
- **Apache Configuration**: How to update Apache with a new certificate.
- **DFN-AAI Rollover**: The process of initiating and completing a rollover for DFN-AAI.
- **Shibboleth Configuration**: Updating Shibboleth configuration to use the new certificate.

## Solution
- Follow the certificate renewal process as outlined.
- Ensure proper integration of the new certificate into the Apache server.
- Initiate and complete the DFN-AAI rollover process.
- Update Shibboleth configuration and restart Moodle to apply changes.

This documentation can serve as a reference for future certificate renewal processes and related configurations.
---

### 2022101442000577_%5BDFN%232022101410000431%5D%20Zertifikat%20l%C3%83%C2%A4uft%20ab%20_%20certificate%20about%20to%20e.md
# Ticket 2022101442000577

 # HPC Support Ticket: Certificate Expiration

## Keywords
- Certificate expiration
- Key rollover
- DFN AAI
- SAML metadata
- Zertifikatstausch

## Summary
A certificate for the HPC portal was about to expire, and the DFN AAI team sent a notification to the HPC support team. The certificate needed to be renewed to avoid service disruptions.

## Root Cause
- The certificate for `portal.hpc.fau.de` was set to expire on Tue, 08 Nov 2022 14:27:10 +0100.

## Solution
- The HPC Admins were notified to renew the certificate as per the instructions provided at [DFN Certificates Documentation](https://doku.tid.dfn.de/en:certificates).
- The certificate exchange with key rollover was completed successfully.

## Lessons Learned
- Regularly monitor certificate expiration dates to avoid service interruptions.
- Follow the documented procedures for certificate renewal.
- Ensure timely communication and coordination between the HPC support team and external services like DFN AAI.

## Actions Taken
- Notification sent by DFN AAI team to HPC support.
- HPC Admins acknowledged the notification and initiated the certificate renewal process.
- Key rollover was completed, and the certificate exchange was finalized.

## References
- [DFN Certificates Documentation](https://doku.tid.dfn.de/en:certificates)
- [DFN AAI Hotline](http://www.aai.dfn.de/)

## Notes
- Ensure that all relevant parties are informed about upcoming certificate expirations to prevent service disruptions.
- Document the steps taken during the certificate renewal process for future reference.
---

### 2022012742002862_Early-Fritz%20%22Egor%20Trushin%22%20_%20bctc33.md
# Ticket 2022012742002862

 # HPC Support Ticket Analysis

## Keywords
- Account activation
- Fritz cluster
- Slurm
- MPI
- Intel compiler
- MKL
- VASP package
- Single-node throughput
- Infiniband HCAs
- Partition specification

## Summary
- **User Request**: Activation of account on Fritz cluster for single-node throughput calculations using VASP package. Required software includes Intel Fortran compiler and MKL.
- **HPC Admin Actions**: Account enabled on Fritz cluster. Provided documentation link and instructions on partition specification.
- **Issues**: Certificate expiration mentioned but not detailed.

## Lessons Learned
- **Account Activation**: HPC Admins can enable user accounts on specific clusters.
- **Documentation**: Preliminary documentation and instructions are available for users.
- **Partition Specification**: Users must specify a partition (e.g., `--partition=singlenode`) when submitting jobs.
- **Software Modules**: Intel compiler and MKL are available via modules.
- **Certificate Management**: Ensure certificates are up-to-date to avoid expiration issues.

## Root Cause of Problem
- User needed account activation and access to specific software for their calculations.

## Solution
- HPC Admin enabled the user's account and provided necessary documentation and instructions.

## Additional Notes
- Users should be informed about the need to specify partitions and how to access software modules.
- Regularly check and update certificates to prevent expiration issues.

---

This analysis provides a brief overview of the support ticket conversation, highlighting key actions and lessons learned for future reference.
---

### 2022060842002175_Test%3A%20Queueeinrichtung.md
# Ticket 2022060842002175

 ```markdown
# HPC-Support Ticket: Test Queue Setup

## Keywords
- Test
- Queue Setup
- Certificate Expiration
- Successful Test

## Summary
A test was conducted to verify the queue setup. The user reported that the certificate had expired, but the test was ultimately successful.

## Root Cause
- Certificate expiration was noted by the user.

## Solution
- The test was completed successfully despite the certificate issue.

## Lessons Learned
- Regularly check and update certificates to avoid expiration issues.
- Ensure that tests are conducted thoroughly to verify system functionality.

## Actions Taken
- The HPC Admin closed the ticket after confirming the successful test.
```
---

### 42051957_Fwd%3A%20Frage%20zur%20Beantragung%20eines%20User-Zertifikates.md
# Ticket 42051957

 # HPC Support Ticket: Request for User Certificate

## Keywords
- Grid Certificate
- DFN PKI
- CERN Certificate
- Personal Presentation
- Certificate Policy (CP)
- Certification Practice Statement (CPS)

## Problem
- User requires a personal Grid certificate for a project at CERN.
- User cannot travel back to Erlangen for a personal presentation.
- User inquires about the possibility of sending an ID copy instead.

## Root Cause
- DFN PKI regulations require personal presentation for the issuance of Grid certificates.
- No exceptions found in the DFN-PKI grid-cp and grid-cps documents.

## Solution
- User was advised to check CERN's certificate issuance process.
- User successfully obtained a certificate from CERN.

## General Learnings
- Grid certificates require personal presentation as per DFN PKI regulations.
- Alternative solutions may be available through other institutions like CERN.
- Always refer to the official policies and practices for certificate issuance.

## References
- [DFN-PKI Grid CP](https://www.pki.dfn.de/fileadmin/PKI/DFN-PKI_grid-cp_v15.pdf)
- [DFN-PKI Grid CPS](https://www.pki.dfn.de/fileadmin/PKI/DFN-PKI_grid-cps_v15.pdf)
- [CERN CA Help](https://ca.cern.ch/ca/Help/?kbid=021001)
- [CERN Login](https://login.cern.ch/adfs/ls/?wa=wsignin1.0&wreply=https%3a%2f%2fca.cern.ch%2fca%2f&wct=2010-08-12T08%3a47%3a13Z&wctx=7321142f-e649-4f95-a34d-fda76e3f99a3)
---

### 2022120142001613_G%C3%83%C2%89ANT%20TCS%3A%20Awaiting%20approval%20for%20certificate%20moodle.nhr.fau.de.md
# Ticket 2022120142001613

 # HPC-Support Ticket: Certificate Request for Moodle

## Keywords
- Certificate Request
- Approval Process
- DNS Verification
- Certificate Download
- Certificate Formats
- Apache/nginx
- Microsoft IIS
- PKCS#7
- PEM Encoded

## Summary
A certificate request for `moodle.nhr.fau.de` was submitted and awaited approval. The request included multiple Subject Alternative Names (SANs) and was approved by the administrator after DNS verification. The certificate was issued and instructions for downloading in various formats were provided.

## Root Cause
- Awaiting approval for a certificate request.

## Solution
- The certificate request was approved by the administrator.
- DNS verification was completed successfully.
- The certificate was issued and download links for different formats were provided.

## Steps Taken
1. **Certificate Request Submission**:
   - Requested by: HPC User
   - Common Name: `moodle.nhr.fau.de`
   - SANs: `moodle.nhr.fau.de`, `www.moodle.nhr.fau.de`, `moodle.nhr.uni-erlangen.de`, `www.moodle.nhr.uni-erlangen.de`
   - Certificate Profile: OV Multi-Domain
   - Term: 365 Days

2. **Approval Process**:
   - Approved by: HPC Admin
   - DNS verification completed.

3. **Certificate Issuance**:
   - Certificate issued with the requested names.
   - Expiry date: 01/12/2023 23:59 GMT.
   - Certificate ID provided for renewal or revocation.

4. **Download Instructions**:
   - Provided links for downloading the certificate in various formats suitable for different web servers (Apache/nginx, Microsoft IIS).

## Conclusion
The certificate request was successfully processed, approved, and issued. The user was provided with download links and instructions for different formats. The ticket was closed after the certificate was downloaded.

## Notes
- Ensure DNS verification is completed before approval.
- Provide clear instructions for downloading the certificate in the appropriate format for the user's web server.
- Keep the Certificate ID for future reference in case of renewal or revocation.
---

### 2022050242000242_IdP-Freischaltung%20f%C3%83%C2%BCr%20portal.hpc.fau.de%20von%20NHR%40FAU%20f%C3%83%C2%BCr%20den%20Zu.md
# Ticket 2022050242000242

 # HPC Support Ticket Analysis

## Subject
IdP-Freischaltung für portal.hpc.fau.de von NHR@FAU für den Zugang zu Hochleistungsrechnern im Rahmen des Verbunds für Nationales Hochleistungsrechnen - Uni-Bremen

## Keywords
- HPC
- NHR@FAU
- SSO
- DFN-AAI-Föderation
- IdP
- SdP
- Attribute
- Hochleistungsrechner
- Zugang
- Freischaltung

## Problem
- The certificate for the HPC portal has expired.
- The HPC portal needs to be added to the IdP for users to access high-performance computing resources.

## Root Cause
- The certificate expiration was preventing access to the HPC portal.
- The IdP needed to be configured to release specific attributes for user authentication.

## Solution
- The HPC Admin requested the IdP to release the following attributes:
  - `urn:oid:2.5.4.42` - `urn:mace:dir:attribute-def:givenName`: `givenName`
  - `urn:oid:2.5.4.4` - `urn:mace:dir:attribute-def:sn`: `sn`
  - `urn:oid:0.9.2342.19200300.100.1.3` - `urn:mace:dir:attribute-def:mail`: `mail`
  - `urn:oid:1.3.6.1.4.1.5923.1.1.1.6` - `urn:mace:dir:attribute-def:eduPersonPrincipalName`: `eduPersonPrincipalName`
  - `urn:oid:1.3.6.1.4.1.5923.1.1.1.9` - `urn:mace:dir:attribute-def:eduPersonScopedAffiliation`: `eduPersonScopedAffiliation`
- The user confirmed that these attributes are already enabled for all SPs in the DFN-AAI.

## General Learning
- Ensure that certificates for HPC portals are up-to-date to avoid access issues.
- Proper configuration of IdP attributes is crucial for seamless user authentication and access to HPC resources.
- Communication between HPC Admins and users is essential for resolving access issues and ensuring proper configuration.
---

### 2023032242003285_Tier3-Access-Fritz%20%22Rongguang%20Gan%22%20_%20nfcc013h.md
# Ticket 2023032242003285

 # HPC Support Ticket Analysis

## Keywords
- HPC Account Activation
- Certificate Expiration
- Multi-node Workload
- Quantum Espresso
- Corehole Shifts
- Barium-titanate

## Summary
- **User Request:** Access to HPC resources for multi-node workload using Quantum Espresso to investigate corehole shifts on Barium-titanate surfaces.
- **Issue:** Certificate expiration.
- **Solution:** HPC account enabled after addressing the certificate issue.

## Details
- **Requested Resources:**
  - Multi-node workload with HDR100 Infiniband (1:4 blocking)
  - Per node: 72 cores, 250 GB
  - Total compute time: 4800 node hours on Fritz
- **Software Required:** Quantum Espresso - PW
- **Application:** Investigating corehole shifts on Barium-titanate surfaces with varying oxygen vacancies and electron localizations.
- **Expected Outcomes:** Calculation of corehole shifts and comparison with experimental findings.

## Root Cause
- Certificate expiration led to initial access issues.

## Solution
- HPC Admin enabled the user's account after resolving the certificate issue.

## General Learnings
- Ensure certificates are up-to-date to avoid access issues.
- Proper communication and documentation of resource requirements and expected outcomes are crucial for efficient support.

## Next Steps
- Monitor account activity to ensure smooth operation.
- Provide any additional support or resources as needed for the user's research.
---

### 2023061542001213_using%20Fritz%20instead%20of%20Meggie%20-%20iww1009h.md
# Ticket 2023061542001213

 ```markdown
# HPC Support Ticket Conversation Summary

## Subject: Using Fritz instead of Meggie - iww1009h

### Key Points Learned

- **Access Request**: User unable to SSH into Fritz with current HPC ID.
- **Form Submission**: User needs to fill out a form for access to Fritz.
- **Performance Issues**: User's jobs on Meggie are not performing efficiently.
- **Simulation Details**: User is performing MD simulations using LAMMPS and IMD with EAM potentials.
- **Resource Allocation**: User's resource request is large, requiring an NHR proposal.
- **Monitoring System**: User is advised to use the monitoring system to analyze job performance.
- **Job Optimization**: HPC Admins suggest optimizing job settings and testing different simulation cell sizes.

### Root Cause of the Problem

- **Access Issue**: User's account not enabled for Fritz.
- **Performance Issue**: Poor performance of jobs on Meggie due to potential issues with simulation settings or binary compilation.

### Solution

- **Access Issue**: User needs to submit the Tier3-Fritz form for account activation.
- **Performance Issue**:
  - User should test different simulation cell sizes to identify performance bottlenecks.
  - HPC Admins will analyze job performance using the monitoring system.
  - User is advised to use the recommended LAMMPS module on Fritz.

### Additional Notes

- **Resource Limitation**: User's account on Fritz is enabled with limited resources.
- **Future Actions**: User should keep an eye on job performance and consult with HPC Admins for further optimization.

### References

- **Form Link**: [Tier3-Fritz Access Form](https://hpc.fau.de/tier3-access-to-fritz/)
- **Monitoring System**: [Monitoring NHR FAU](https://monitoring.nhr.fau.de/)
- **NHR Application Rules**: [NHR Application Rules](https://hpc.fau.de/systems-services/documentation-instructions/nhr-application-rules/)
```
---

### 2022020342000853_Re%3A%20%5BDFN%232022020310000734%5D%20new%20application%20in%20dfn-aai.md
# Ticket 2022020342000853

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject: Re: [DFN#2022020310000734] new application in dfn-aai

### Keywords
- DFN-AAI
- Service Provider (SP)
- Entity ID
- Metadata
- Security
- Testföderation

### Root Cause of the Problem
- The certificate for the Service Provider with the Entity ID `https://portal.hpc.fau.de/saml/metadata` has expired.

### Solution
- The Service Provider has been approved and will be added to the DFN-AAI production environment metadata.
- It is recommended to remove the SP from the test federation for security reasons.

### General Learnings
- Always check the validity of certificates for Service Providers.
- Follow the guidelines and recommendations provided in the [DFN-AAI Wiki](https://wiki.aai.dfn.de/de:production).
- Ensure that Service Providers are not left in the test federation for security purposes.

### Roles Involved
- **HPC Admins**: Thomas, Michael Meier, Anna Kahler, Katrin Nusser, Johannes Veh
- **2nd Level Support Team**: Lacey, Dane (fo36fizy), Kuckuk, Sebastian (sisekuck), Lange, Florian (ow86apyf), Ernst, Dominik (te42kyfo), Mayr, Martin
- **Head of the Datacenter**: Gerhard Wellein
- **Training and Support Group Leader**: Georg Hager
- **NHR Rechenzeit Support and Applications for Grants**: Harald Lanig
- **Software and Tools Developer**: Jan Eitzinger, Gruber
```
---

### 2022091942002943_Fwd%3A%20%5BDFN%232022091910000317%5D%20Research%20and%20Scholarship%20EC%20application.md
# Ticket 2022091942002943

 # HPC Support Ticket Analysis

## Subject
Fwd: [DFN#2022091910000317] Research and Scholarship EC application

## Keywords
- Certificate expiration
- Research and Scholarship Entity-Attribut
- Metadata management
- Final publication

## Root Cause
- Certificate has expired.

## Solution
- The Research & Scholarship Entity-Attribut was requested and approved.
- A new checkbox appeared in the metadata management interface, allowing the user to finalize the publication.

## General Learnings
- Ensure certificates are up to date to avoid expiration issues.
- The process for requesting and approving Research & Scholarship Entity-Attribut involves external communication and finalization through the metadata management interface.

## Actions Taken
- The DFN AAI Hotline approved the Research & Scholarship Entity-Attribut.
- The user was instructed to finalize the publication through the metadata management interface.

## Next Steps
- The user should finalize the publication by checking the new checkbox in the metadata management interface.
- Monitor the certificate expiration dates to prevent future issues.

## Relevant Parties
- HPC Admins
- 2nd Level Support Team
- DFN AAI Hotline

## Additional Notes
- Ensure regular communication with external entities like DFN AAI Hotline for timely approvals and updates.
- Regularly review and update certificates to avoid disruptions in service.
---

### 2022012142000802_Re%3A%20%5BRRZE-HPC%5D%20Call%20for%20early-adopter%20of%20parallel%20computer%20Fritz.md
# Ticket 2022012142000802

 # HPC Support Ticket Conversation Analysis

## Keywords
- Early adopter
- Fritz
- Alex
- NHR
- Tier3
- Infiniband
- Ice Lake
- Wordpress
- Certificate expired

## Summary
- **Announcement**: FAU has purchased a new parallel computer "Fritz" with 944 compute nodes, each equipped with two Intel Xeon Platinum 8360Y processors and 256 GB of DDR4 memory.
- **Early Adopter Program**: The HPC team is looking for experienced users to help bring Fritz into stable production. Early adopters will receive plenty of compute cycles but should expect configuration changes and stability issues.
- **Application Process**: Users interested in becoming early adopters should fill out a form available on the HPC website.
- **Issue**: The link to the early adopter application form led to a non-existent webpage.
- **Root Cause**: The Wordpress certificate had expired.
- **Solution**: The HPC Admin fixed the issue by renewing the certificate.

## General Learnings
- Always check links in announcements to ensure they are working.
- Certificate expiration can cause issues with accessing webpages.
- Early adopter programs are beneficial for both users and the HPC team, providing users with more compute cycles and the team with valuable feedback.
- The selection of early adopters is based on expected scientific outcome and diversity of groups, applications, and scientific domains.

## Actions Taken
- The user notified the HPC Admin about the broken link.
- The HPC Admin identified the issue as an expired Wordpress certificate and fixed it.
- The user confirmed that the link was working after the fix.

## Follow-up
- Users should apply for the early adopter program if interested.
- The HPC team should monitor the stability and performance of Fritz during the early adopter phase.
- The HPC team should also consider similar early adopter programs for future hardware purchases.
---

### 2019042342001086_Login%20auf%20aurora1%20schl%C3%83%C2%A4gt%20fehl.md
# Ticket 2019042342001086

 ```markdown
# HPC Support Ticket: Login auf aurora1 schlägt fehl

## Keywords
- Login issue
- Job system
- NEC Aurora
- qsub command
- Certificate expiration
- Service restart

## Problem Description
- User unable to log in to the NEC Aurora job system (aurora1.rrze.uni-erlangen.de) using the qsub command.
- Command used: `qsub -l nodes=aurora1:ppn=24 -l walltime=05:00:00 -I`

## Root Cause
- Certificate expiration after a system reboot.

## Solution
- Restart the affected service to resolve the certificate issue.

## Additional Information
- User inquired about plans to update compilers and other software on the Aurora system.

## Lessons Learned
- Regularly check for certificate expiration and ensure all services are properly restarted after system reboots.
- Keep software and compilers updated to maintain system efficiency and user satisfaction.
```
---

### 2023071442001857_Tier3-Access-Fritz%20%22Shucheta%20Shegufta%22%20_%20iww8022h.md
# Ticket 2023071442001857

 # HPC Support Ticket Analysis

## Keywords
- HPC Account Activation
- Certificate Expiration
- Multi-node Workload
- Software Requirements
- Simulation of Failure and Fracture
- Peridigm
- 3D Simulations
- Computational Requirements

## Summary
- **User Request**: Activation of HPC account for multi-node workload.
- **Software Requirements**: Git, Python3, Trilinos, NetCDF, HDF5, Boost, BLAS, LAPACK, yaml-cpp, openmp-MPI.
- **Application**: Simulation of failure and fracture in porous materials using Peridigm.
- **Expected Results**: Understanding of failure in highly porous materials.
- **Additional Notes**: Transition from 2D to 3D simulations, increased computational requirements.

## Root Cause of the Problem
- Certificate expiration.

## Solution
- HPC Admins enabled the user's HPC account.

## General Learnings
- Ensure certificates are up-to-date for account activation.
- Understand the user's software requirements and expected computational needs.
- Be prepared for increased computational demands as users transition to more complex simulations.

## Next Steps
- Monitor the user's account for any further issues related to certificate expiration.
- Ensure the required software is available and properly configured on the HPC system.
- Prepare for potential increases in computational resource requests.
---

### 2022032342002848_appointment.md
# Ticket 2022032342002848

 # HPC Support Ticket: Appointment for Grid Certificate Identification

## Keywords
- Grid certificate
- Identification process
- Appointment
- Online procedure
- Akkreditierende Einrichtung

## Summary
A user requested an appointment for the identification process of a grid certificate. The user had completed the online procedure and needed an in-person verification.

## Root Cause
- User required in-person identification for grid certificate validation.

## Conversation Flow
1. **User Request**: Initial request for an appointment after 12 PM on any working day.
2. **Follow-up**: User completed the online procedure and requested an appointment for the next day.
3. **HPC Admin Response**: Admin working from home, suggested another admin (GHa) to handle the request.
4. **Appointment Scheduled**: Admin scheduled an appointment for the following Monday at 1 PM, providing office location and instructions.
5. **User Confirmation**: User confirmed the appointment time.

## Solution
- An appointment was scheduled for the user to complete the identification process in person.
- Instructions were provided for the user to find the admin's office.

## General Learnings
- Users need to complete an online procedure before scheduling an in-person appointment for grid certificate identification.
- Admins may need to coordinate with each other to handle appointments, especially when working remotely.
- Clear communication about office location and access instructions is essential for a smooth appointment process.

## Next Steps for Similar Cases
- Guide the user through the online procedure if not already completed.
- Coordinate with available admins to schedule an in-person appointment.
- Provide detailed instructions for the appointment location and any specific access requirements.
---

### 2022111642000768_Tier3-Access-Fritz%20%22Lukas%20Saur%22%20_%20iwpa061h.md
# Ticket 2022111642000768

 # HPC Support Ticket Analysis

## Keywords
- Tier3 Access
- Fritz
- Account Activation
- NHR Projects
- Certificate Expiration
- Resource Allocation
- Software: StarCCM
- Simulation
- Fluid Dynamics

## Summary
- **User Request**: Access to Fritz for simulation of Scroll-Supercharger using StarCCM.
- **Resources Requested**: Single-node throughput (72 cores, 250 GB), multi-node workload (HDR100 Infiniband with 1:4 blocking).
- **Computation Time**: 3000 node hours.

## Issue
- **Root Cause**: Certificate expiration.

## Solution
- **Action Taken**: Account activated on Fritz.
- **Recommendation**: User advised to check with department heads if they should use NHR projects instead of Tier3-Grundversorgung.

## General Learnings
- Ensure certificates are up-to-date to avoid access issues.
- Coordinate with department heads for optimal resource allocation.
- Verify if users can utilize NHR projects for better resource management.

## Next Steps
- Monitor account usage.
- Provide guidance on NHR project utilization if needed.

---

This documentation can be used to resolve similar issues related to account activation and resource allocation on Fritz.
---

### 2023042442003412_Alex_Fritz%20Freischaltung%20SCC%20Accounts.md
# Ticket 2023042442003412

 ```markdown
# HPC Support Ticket Analysis

## Subject: Freischaltung SCC Accounts

### Keywords:
- HPC Accounts
- Freischaltung (Activation)
- Übungsbetrieb (Practice Operation)
- Certificate Expiration

### Summary:
A user requested the activation of HPC accounts (scvl100h - scvl116h) for practice operations. The HPC Admin noted that the certificate had expired and marked the issue as resolved.

### Root Cause:
- Certificate expiration

### Solution:
- The HPC Admin addressed the certificate expiration issue and marked the request as completed.

### General Learnings:
- Ensure certificates are up-to-date for account activations.
- Regularly check and renew certificates to avoid expiration issues.

### Roles Involved:
- **HPC Admins**: Responsible for managing and activating HPC accounts.
- **2nd Level Support Team**: Assists with user requests and troubleshooting.

### Actions Taken:
- The HPC Admin noted the certificate expiration and resolved the issue.

### Future Prevention:
- Implement a system to monitor and alert for certificate expirations.
- Regularly review and update certificates to prevent disruptions in account activations.
```
---

### 2023011842002869_Fritz%20Access%20-%20gwgk002h%20_%20b128dc.md
# Ticket 2023011842002869

 # HPC Support Ticket: Fritz Access Issue

## Keywords
- Fritz cluster access
- SSH login
- Account unavailable
- Data estimation
- Certificate expiration

## Summary
A user was unable to access the Fritz cluster, receiving an "account unavailable" message upon login attempt. The issue was resolved by the HPC Admin, who also inquired about the user's data creation estimate for the next few months.

## Root Cause
- The user's certificate had expired, preventing access to the Fritz cluster.

## Solution
- The HPC Admin renewed or updated the user's certificate, restoring access to the Fritz cluster.

## Follow-up
- The user estimated that their first simulation would generate around 15 TB of data.
- The HPC Admin confirmed that there was no need to place data on a different file system.

## General Learnings
- Certificate expiration can cause account access issues.
- HPC Admins may need to estimate data creation for resource management purposes.
- Users should be able to provide estimates of data generation for their simulations.
---

### 2023081142001002_Tier3-Access-Fritz%20%22Leon%20Pyka%22%20_%20iww1012h.md
# Ticket 2023081142001002

 ```markdown
# HPC Support Ticket Analysis

## Subject
Tier3-Access-Fritz "Leon Pyka" / iww1012h

## Keywords
- HPC Account
- Certificate Expiration
- Multi-node Workload
- HDR100 Infiniband
- IMD, LAMMPS
- Atomistic Simulations
- Master Thesis

## Summary
- **User Request**: Access to HPC resources for multi-node workload.
- **Resources Requested**: 1000 node hours on Fritz.
- **Software Needed**: IMD, LAMMPS.
- **Application**: Atomistic Simulations of Dynamic Cracks.
- **Expected Outcome**: Master Thesis.

## Issue
- **Root Cause**: Certificate has expired.

## Solution
- **Action Taken**: HPC Admin enabled the user's HPC account on Fritz.

## General Learnings
- Regularly check and renew certificates to avoid account access issues.
- Ensure proper communication with users regarding account status and resource allocation.
- Document software requirements and expected outcomes for better resource management.
```
---

### 2020032442001529_Verl%C3%83%C2%A4ngerung%20HPC-Account%20Caroline%20Collischon%20%28mppl001h%29%20bis%2031.12.2020.md
# Ticket 2020032442001529

 ```markdown
# HPC Support Ticket: Account Extension Request

## Keywords
- HPC Account Extension
- Form Submission
- Expired Certificate

## Summary
A user requested an extension for an HPC account until December 31, 2020. The request included a signed form, and the user confirmed that the account holder's signature was not required based on a previous email.

## Root Cause
- The user needed an extension for an HPC account.
- The certificate associated with the account had expired.

## Solution
- The HPC Admin processed the request and noted that the certificate had expired.
- The request was marked as completed.

## Lessons Learned
- Ensure that the certificate associated with the account is valid when processing extension requests.
- Confirm that the necessary forms are correctly submitted and signed as per the guidelines.

## Actions Taken
- The HPC Admin acknowledged the request and noted the expired certificate.
- The request was processed and marked as completed.

## Follow-Up
- Verify the validity of certificates during account extension requests.
- Ensure that users are aware of the requirements for form submission and signature.
```
---

### 2022053142003051_Alex%20Freischaltung.md
# Ticket 2022053142003051

 ```markdown
# HPC Support Ticket: Alex Freischaltung

## Keywords
- Freischaltung (Activation)
- Mucosimstudenten
- Alex
- Expired Certificate

## Summary
A user requested the activation of a Mucosimstudenten account for Alex. The HPC Admin responded that the certificate had expired but proceeded to activate the account.

## Root Cause
- The user requested activation for a specific account.
- The HPC Admin noted that the certificate had expired.

## Solution
- The HPC Admin activated the account despite the expired certificate.

## General Learnings
- Users may request account activations for specific purposes.
- HPC Admins should check for expired certificates and handle them appropriately.
- Communication between users and HPC Admins is essential for resolving account-related issues.
```
---

### 2022062942000486_Tier3-Access-Fritz%20%22Maurice%20Rohracker%22%20_%20iwtm024h.md
# Ticket 2022062942000486

 # HPC Support Ticket Analysis

## Keywords
- Certificate expiration
- Compute time demand
- Multi-node workload
- Node hours calculation
- Meggie cluster
- deal.II software
- Phase-field method
- Fracture mechanics

## Summary
- **User Issue**: Certificate expiration and compute time demand specification.
- **Root Cause**: User specified compute time demand without considering node hours calculation.
- **Solution**: HPC Admin provided guidance on calculating node hours and suggested using Meggie cluster for sufficient compute resources.

## Details
- **Certificate Expiration**: HPC Admin noted that the user's certificate had expired.
- **Compute Time Demand**: User requested 1,000 hours of compute time for a multi-node workload.
- **Node Hours Calculation**: HPC Admin explained the calculation of node hours and suggested that the user's demand could be met within a month using 8 nodes concurrently on the Meggie cluster.
- **Software Requirement**: User required deal.II software for distributed memory parallel FE code to solve fracture mechanic problems using the phase-field method.

## Learning Points
- Importance of accurate compute time demand specification.
- Understanding node hours calculation for multi-node workloads.
- Utilizing available cluster resources efficiently.
- Ensuring certificates are up-to-date for access.

## Next Steps
- Ensure user updates their certificate.
- Provide further guidance on node hours calculation if needed.
- Monitor user's compute time usage and provide support as required.
---

### 2021032542001614_Login%20Probleme.md
# Ticket 2021032542001614

 ```markdown
# HPC Support Ticket: Login Probleme

## Keywords
- Login issues
- Connection problems
- HPC clusters
- File server issues
- Certificate expiration

## Summary
A user reported issues with logging into HPC clusters (meggie, emmy, cshpc). The connection was dropping, and the login process halted after entering the password.

## Root Cause
- **File Server Issues**: There were problems with one of the file servers.
- **Certificate Expiration**: The certificate had expired.

## Solution
- The HPC Admin team identified and resolved the file server issues.
- The certificate was renewed or updated.

## Lessons Learned
- Regularly monitor file server health to prevent login issues.
- Ensure certificates are up-to-date to avoid expiration-related problems.
- Communicate with users promptly to address and resolve issues efficiently.

## Follow-Up
- The user confirmed that the login issues were resolved and everything was functioning normally.
- The ticket was closed after the user confirmed the resolution.
```
---

### 2024032542000799_Extend%20the%20runtime%20for%20the%20process.md
# Ticket 2024032542000799

 ```markdown
# HPC-Support Ticket: Extend the Runtime for the Process

## Keywords
- Runtime extension
- Process ID
- Node assignment
- Certificate error

## Summary
A user requested an extension of the runtime for a specific process on a designated node.

## Problem
- **Root Cause:** User needed additional runtime for a process.
- **Additional Issue:** User mentioned an error related to the local issuer certificate.

## Solution
- **Action Taken:** HPC Admin extended the runtime for the specified process.
- **Pending:** No further action mentioned regarding the certificate error.

## Learning Points
- Users may request runtime extensions for ongoing processes.
- Ensure to address any additional issues mentioned by the user, such as certificate errors.

## Next Steps
- Follow up with the user to resolve the certificate error if it persists.
- Document the process for extending runtime for future reference.
```
---

### 2023060242001069_Tier3-Access-Fritz%20%22Fabian%20B%C3%83%C2%B6hm%22%20_%20vy28quve%40fau.de.md
# Ticket 2023060242001069

 # HPC Support Ticket Analysis

## Keywords
- HPC Account
- Fritz Access
- Certificate Expiration
- Account Activation

## Summary
- **Root Cause**: User's HPC account was not valid, preventing access to Fritz.
- **Solution**: User obtained a valid HPC account through their department, which was then activated on Fritz.

## Detailed Steps
1. **Initial Request**:
   - User requested access to Fritz for performance engineering of MPI applications.
   - Required resources: single-node throughput (72 cores, 250 GB), 150 node hours.
   - Required software: MPI, Likwid.

2. **HPC Admin Response**:
   - Informed user that their HPC account was not valid, preventing access to Fritz.
   - Advised user to obtain a valid HPC account through their department.

3. **User Follow-up**:
   - User obtained a valid HPC account with the identifier `iwia054h`.

4. **Final HPC Admin Response**:
   - Confirmed that the user's HPC account was activated on Fritz.

## General Learnings
- Valid HPC account is required for accessing resources like Fritz.
- Users should obtain HPC accounts through their respective departments.
- HPC admins activate accounts upon verification of their validity.
---

### 2020011642002298_HPC%20Monitoring%20Website.md
# Ticket 2020011642002298

 ```markdown
# HPC Monitoring Website Issue

## Keywords
- HPC Monitoring Website
- IP Address Restriction
- Certificate Expiration
- Account Reactivation

## Problem Description
The HPC monitoring website (`https://hpc-monitoring.rrze.uni-erlangen.de/`) was experiencing issues despite having an IP address restriction in place. The user reported problems with the site and requested assistance from the responsible party.

## Root Cause
- **Certificate Expiration**: The SSL certificate for the website had expired.
- **Account Issues**: The responsible admin's read-only account on the web server had expired due to a role change.

## Solution
- **Certificate Renewal**: The admin fixed the certificate issue.
- **Account Reactivation**: The admin is waiting for the reactivation of their read-only account on the web server.

## Actions Taken
- The responsible admin identified and fixed the certificate issue.
- The admin is awaiting account reactivation to finalize the changes.

## Follow-Up
- The admin will notify the user once the changes are live.
- A meeting was scheduled for further discussion and resolution.

## General Learnings
- Regularly check and renew SSL certificates to avoid expiration issues.
- Ensure that account permissions are up-to-date, especially after role changes.
- Communicate effectively with users to schedule meetings and provide updates on issue resolution.
```
---

### 2020020442001934_QE%20Emmy%20-%3E%20Meggie.md
# Ticket 2020020442001934

 # HPC Support Ticket: QE Emmy -> Meggie

## Keywords
- QE (Quantum Espresso)
- Emmy
- Meggie
- Job migration
- Free nodes
- Certificate expiration

## Summary
- **Root Cause**: Certificate expiration on Emmy.
- **Solution**: Migrate jobs from Emmy to Meggie.
- **Details**: A new QE version was built for Meggie, allowing users to move their jobs due to the availability of many free nodes.

## Lessons Learned
- Regularly check and update certificates to avoid expiration issues.
- Inform users about alternative resources (e.g., Meggie) when one resource (e.g., Emmy) is experiencing issues.
- Ensure that software versions are compatible across different systems to facilitate smooth job migration.

## Actions Taken
- The ticket was closed after verbal clarification.

## Notes
- This ticket highlights the importance of maintaining up-to-date certificates and providing users with alternative computing resources when needed.
---

### 2020120342002096_HPC%20usage%20report.md
# Ticket 2020120342002096

 ```markdown
# HPC Support Ticket: HPC Usage Report

## Keywords
- HPC usage report
- Paper publication
- Delayed submission
- Expired certificate

## Summary
A user submitted an HPC usage report and figure for a published paper. The HPC admin acknowledged receipt but noted that the certificate had expired.

## Root Cause
- Delayed submission of the usage report.
- Expired certificate for the submission link.

## Solution
- The user submitted the report despite the delay.
- The HPC admin acknowledged the submission and noted the expired certificate.

## Lessons Learned
- Users should submit HPC usage reports promptly to avoid delays.
- HPC admins should ensure that certificates for submission links are up-to-date.
```
---

### 2020052142000102_Access%20to%20Meggie.md
# Ticket 2020052142000102

 ```markdown
# HPC Support Ticket: Access to Meggie

## Keywords
- Access Issue
- Meggie
- Password Failure
- Network Maintenance
- Certificate Expiration

## Summary
A user reported being unable to connect to Meggie after multiple failed password attempts. The user could still access the dialog server `cshpc.rrze.fau.de` with the same password.

## Root Cause
- The issue was a side effect of large network maintenance in the RRZE's data center.
- Certificate expiration was also mentioned as a potential issue.

## Solution
- The HPC Admins were aware of the problem and worked on resolving it.
- Access to Meggie was restored after addressing the network maintenance side effects.

## Lessons Learned
- Network maintenance can cause temporary access issues to specific servers.
- Certificate expiration can affect server access and should be monitored.
- Users should be informed about ongoing maintenance to manage expectations.
```
---

### 2021062242001338_Job%20auf%20Meggie%20iwia87%20895745.md
# Ticket 2021062242001338

 ```markdown
# HPC Support Ticket: Job auf Meggie iwia87 895745

## Keywords
- Job monitoring
- No activity
- Meggie
- Job ID: 895745
- Certificate expired

## Summary
An HPC admin noticed that a job on Meggie (Job ID: 895745) showed no activity in the job monitoring system. The admin informed the user to check their job and the application being used.

## Root Cause
- The job was not showing any activity.
- The certificate had expired.

## Solution
- The user was advised to check their job and the application being used.
- No specific solution was provided in the conversation, but the user was prompted to take action.

## General Learnings
- Regularly monitor job activity to ensure jobs are running as expected.
- Check for expired certificates as they can cause issues with job execution.
- Communicate with users to troubleshoot and resolve job-related issues promptly.
```
---

### 2023120642002781_Zertifikatswechsel%20beim%20Shibboleth%20Identity%20Provider%20der%20TU%20Dresden%20%7C%20Certificat.md
# Ticket 2023120642002781

 # HPC Support Ticket: Certificate Change at Shibboleth Identity Provider of TU Dresden

## Keywords
- Shibboleth Identity Provider (IdP)
- Certificate change
- Metadata
- DFN AAI
- Service Provider (SP)

## Summary
The encryption and signing certificate of the TU Dresden IdP is set to expire on 09.01.2024 at 23:59:59. A new certificate is already available in the metadata. Service Providers (SPs) that automatically obtain metadata from the DFN AAI do not need to take any action. The final switch to the new certificate will occur on 04.01.2024.

## Root Cause
- Expiration of the current encryption and signing certificate for the TU Dresden IdP.

## Solution
- Ensure that SPs are configured to automatically obtain metadata from the DFN AAI.
- If not, follow the provided FAQ for manual updates.

## Actions Taken
- HPC Admins confirmed that Portal and Moodle automatically obtain metadata from DFN AAI, so no action is required.

## General Learnings
- Regularly check for updates regarding certificate changes for connected IdPs.
- Ensure that SPs are configured to automatically update metadata to avoid manual intervention.
- Follow provided FAQs or guidelines for manual updates if necessary.

## References
- [TU Dresden IdP](https://idp.tu-dresden.de/idp/shibboleth)
- [FAQ for Certificate Change](https://faq.tickets.tu-dresden.de/otrs/public.pl?Action=PublicFAQZoom;ItemID=975)
---

### 2018121842001091_h%C3%83%C2%A4ngender%20Job%20auf%20Emmy%3F%20_%20iwpa015h.md
# Ticket 2018121842001091

 ```markdown
# HPC Support Ticket: Hängender Job auf Emmy

## Keywords
- Hängender Job (Stalled Job)
- System-Monitoring
- Expired Certificate

## Summary
An HPC Admin noticed a stalled job in the system monitoring and informed the user.

## Root Cause
- The job was stalled due to an expired certificate.

## Solution
- The user was asked to investigate the issue.

## General Learnings
- Regularly check system monitoring for stalled jobs.
- Ensure certificates are up-to-date to prevent job stalls.
- Communicate with users promptly when issues are detected.
```
---

### 2021102642001841_GRID%20certificate%20application.md
# Ticket 2021102642001841

 # HPC-Support Ticket: GRID Certificate Application

## Keywords
- GRID certificate
- GRID data access
- Dirac client
- Globus Online
- User space installation
- Document submission

## Summary
A user from the Erlangen Centre for Astroparticle Physics needed access to GRID data for the CTA experiment and required a GRID certificate. The user wanted to download data directly to the HPC system.

## Root Cause
The user needed a GRID certificate to access GRID data and was unsure about the process and compatibility with the HPC system.

## Solution
1. **Certificate Application**: The user was advised to follow the steps on the provided web page to obtain the GRID certificate. The process was confirmed to be valid.
2. **Data Access**: The HPC system does not provide GRID middleware or WAN filesystem software like CVMFS. The user was informed that data could be accessed using tools like `curl`, `wget`, or Globus Online in user mode on the login nodes.
3. **Dirac Client**: The Dirac client, mentioned by the user, is self-contained and might work on the HPC frontends. The user was advised to install it in their user space.
4. **Document Submission**: The user was initially unsure about the document submission process for the certificate application. The HPC admin clarified that the user could send a scan of the required documents, including their passport, via email.

## General Learnings
- GRID certificates are required to access GRID data.
- The HPC system does not provide GRID middleware, so users must rely on other tools for data access.
- Self-contained clients like the Dirac client can be installed in the user space on the HPC frontends.
- Document submission for certificate applications can be done via email.

## Related Links
- [GRID Computing at RRZE](https://www.rrze.fau.de/serverdienste/hpc/grid-computing/#collapse_4)
---

### 2023020842000986_%C3%83%C2%84nderung%20eines%20HPC-Accounts%20iwb3005h.md
# Ticket 2023020842000986

 ```markdown
# HPC Support Ticket Analysis

## Subject: Änderung eines HPC-Accounts iwb3005h

### Keywords:
- Account Change
- Account Extension
- HPC Application
- Certificate Expiration
- Rechenzeit

### Summary:
- **User Request:** Account change for Yipeng Sun.
- **Initial Issue:** HPC application certificate had expired.
- **Action Taken:** Account was extended as requested.
- **Follow-up:** Telephone conversation to increase overall computing time.

### Root Cause:
- Expired HPC application certificate.

### Solution:
- Extended the account as per the user's request.
- Increased overall computing time after a follow-up telephone conversation.

### General Learnings:
- Ensure HPC application certificates are up-to-date to avoid delays in account changes.
- Communicate effectively with users to understand and address their specific needs, such as extending computing time.
```
---

### 2022012442002126_Early-Fritz%20%22Jan%20H%C3%83%C2%B6nig%22%20_%20iwia028h.md
# Ticket 2022012442002126

 # HPC Support Ticket Analysis

## Keywords
- Clang installation
- Spack
- Certificate expiration
- User access
- Partition submission
- Single-node throughput
- Infiniband cards
- SSH access
- Documentation
- Software requirements (likwid, python 3.8, g++/clang, python3-venv)
- Benchmarking tool validation
- Performance measurement

## General Learnings
- **Clang Installation**: Clang is not currently installed but can be built using Spack.
- **Certificate Expiration**: There is an issue with an expired certificate.
- **User Access**: Users can be granted access to specific partitions based on their needs.
- **Partition Submission**: Users can submit jobs to specific partitions like "singlenode" with limited resources due to hardware constraints.
- **SSH Access**: Users can access the HPC cluster via SSH from the university network/VPN or directly with an IPv6 address.
- **Documentation**: The documentation for the HPC cluster is still in progress and can be found on the official website.
- **Software Requirements**: Users may request specific software for their projects, such as likwid, python 3.8, g++/clang, and python3-venv.
- **Benchmarking Tool Validation**: Users may use the HPC cluster for validating benchmarking tools and measuring performance in a controlled environment.

## Root Cause of the Problem
- The user requested access to specific software and resources for benchmarking tool validation.
- The HPC admin provided access to the "singlenode" partition due to limited Infiniband cards.

## Solution
- The HPC admin granted the user access to the "singlenode" partition.
- The user was informed about the SSH access methods and the ongoing documentation process.
- The user was advised to check the Message of the Day (MOTD) for valuable information upon logging in.

## Additional Notes
- The HPC admin mentioned that the documentation is still being developed and can be accessed at the provided URL.
- The user's request included specific software requirements and the need for single-node throughput until more Infiniband HCAs arrive.
---

### 2022091942004325_Tier3-Access-Fritz%20%22Annina-Benita%20Adams%22%20_%20iwtm037h.md
# Ticket 2022091942004325

 ```markdown
# HPC Support Ticket Conversation Analysis

## Subject: Tier3-Access-Fritz "Annina-Benita Adams" / iwtm037h

### Keywords
- Account Activation
- Certificate Expiration
- Multi-node Workload
- LAMMPS
- Matlab
- MD-FE Simulations
- Polymers
- Bachelor Thesis
- Lehrstuhl für Technische Mechanik

### Summary
- **User Request**: Access to HPC resources for multi-node workload.
- **Resources Needed**: 1920 node hours on Fritz.
- **Software Required**: LAMMPS and Matlab.
- **Application**: Parameter studies for coupled MD-FE simulations of polymers.
- **Expected Outcome**: Optimization of a multiscale simulation tool for fracture simulation of polymers.
- **Supervisors**: Christof Bauer, Felix Weber.

### Issue
- **Root Cause**: Certificate has expired.

### Solution
- **Action Taken**: Account was activated on Fritz.

### Lessons Learned
- Ensure certificates are up-to-date for seamless account activation.
- Verify resource requirements and software availability before granting access.
- Communicate clearly with users about the status of their requests and any issues encountered.

### Follow-up
- Monitor account usage to ensure compliance with requested resources.
- Provide support for any technical issues related to LAMMPS and Matlab usage.
```
---

