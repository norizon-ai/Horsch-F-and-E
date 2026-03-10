# Topic 36: workspace_cephfs_data_nvme_cephfsworkspace

Number of tickets: 11

## Tickets in this topic:

### 2024070542001783_%5Baction%20requiered%5D%20Replacement%20of%20cephfs%20with%20anvme%20%5Bb143dc20%5D.md
# Ticket 2024070542001783

 # HPC Support Ticket: Replacement of CephFS with NVMe

## Keywords
- NVMe storage
- CephFS
- Lustre
- Workspace allocation
- Data migration
- Storage unavailability

## Summary
The HPC Admins are upgrading the NVMe storage in Alex by replacing CephFS with Lustre to improve performance. Users currently utilizing workspaces on `/cephfs/workspace` need to take action to migrate their data.

## Actions Required
1. **Allocate New Workspace:**
   - Use the command `ws_allocate -F anvme` to allocate a new workspace.

2. **Move Data:**
   - Transfer data from `/cephfs/workspace` to the new workspace.

3. **Notify HPC Admins:**
   - Inform the HPC Admins once the data migration is complete and the old data is no longer needed.

## Important Dates
- **Storage Unavailability:**
  - The storage located at `/cephfs` will become unavailable starting 01.08.2024.

## Contact Information
- **Support Email:**
  - `support-hpc@fau.de`
- **Website:**
  - [HPC FAU](https://hpc.fau.de/)

## Root Cause
- Performance improvement initiative by replacing CephFS with Lustre.

## Solution
- Allocate a new workspace using `ws_allocate -F anvme`.
- Migrate data from `/cephfs/workspace` to the new workspace.
- Notify HPC Admins once the migration is complete.

## Notes
- Ensure all necessary data is moved before the deadline to avoid data loss.
- Regularly check for similar upgrade notifications to stay informed about future changes.
---

### 2023101742003183_Job%20on%20Alex%20and%20new%20Ceph-storage.md
# Ticket 2023101742003183

 ```markdown
# HPC-Support Ticket: Job on Alex and new Ceph-storage

## Keywords
- Ceph-storage
- Experimental operation
- Data transfer
- Job improvement
- Test user
- Zoom meeting

## Summary
- **HPC Admin** contacted the user regarding the new Ceph-storage in experimental operation.
- The user was identified as transferring large amounts of data from Atuin to Alex nodes.
- The HPC Admin suggested that the user could benefit from switching to the new Ceph-storage.
- The user agreed to test the new storage and provide feedback.
- A Zoom meeting was scheduled to discuss the details.

## Problem
- The user was transferring large datasets, which could potentially be optimized by using the new Ceph-storage.

## Solution
- The user agreed to test the new Ceph-storage and provide feedback.
- A Zoom meeting was scheduled for further discussion and setup.

## Follow-up
- The meeting details and Zoom link were sent via Outlook.
- The ticket was closed with the expectation that the user would test the Ceph-storage and provide feedback.
```
---

### 2024070542001765_%5Baction%20requiert%5D%20Replacement%20of%20cephfs%20with%20anvme%20%5Bb119ee10%5D.md
# Ticket 2024070542001765

 # HPC Support Ticket: Replacement of CephFS with NVMe

## Keywords
- NVMe storage
- CephFS
- Lustre
- Workspace allocation
- Data migration
- Storage decommissioning

## Summary
The HPC site is upgrading its NVMe storage performance by replacing CephFS with Lustre. Users with data on `/cephfs/workspace` need to migrate their data to a new workspace allocated on NVMe.

## Problem
- User has data stored on `/cephfs/workspace`.
- CephFS storage will become unavailable starting 01.08.2024.

## Solution
1. Allocate a new workspace on NVMe:
   ```
   ws_allocate -F anvme
   ```
2. Move data from `/cephfs/workspace` to the new NVMe workspace.
3. Notify HPC Admins once data migration is complete and `/cephfs` data is no longer needed.

## Notes
- The ticket was closed as there were no active workspaces left on CephFS.
- Ensure users are aware of the storage decommissioning date to avoid data loss.

## Related Parties
- HPC Admins
- 2nd Level Support Team
- Users with data on `/cephfs/workspace`
---

### 2024070542001774_%5Baction%20requiered%5D%20Replacement%20of%20cephfs%20with%20anvme%20%5Bb143dc12%5D.md
# Ticket 2024070542001774

 # HPC Support Ticket: Replacement of CephFS with ANVME

## Keywords
- CephFS
- Lustre
- NVME storage
- Workspace allocation
- Data migration
- Extension limits
- Server integration

## Summary
The HPC site is transitioning from CephFS to Lustre for NVME storage to improve performance. Users are required to allocate new workspaces and migrate their data. The old CephFS storage will become unavailable starting 01.08.2024.

## User Concerns
- The new workspace has only 10 extensions.
- Query about the future of Ceph servers.
- Possibility of extending workspace beyond 900 days.

## Admin Responses
- The 10 extensions amount to nearly 3 years, which should suffice for typical project durations of 1-2 years.
- Ceph servers will be integrated into the new Lustre cluster.
- Admins can extend the workspace beyond 900 days if needed, or users can create a new workspace and move their data.

## Action Items
- Users should allocate a new workspace using `ws_allocate -F anvme` and migrate their data.
- Notify admins once data migration is complete and old data can be deleted.

## Notes
- The transition is aimed at increasing storage performance.
- Proper communication and data management are crucial during this transition period.

## Root Cause
- The need for improved storage performance led to the decision to replace CephFS with Lustre.

## Solution
- Allocate a new workspace and migrate data as instructed. Admins will handle the integration of old servers and can assist with extensions if needed.
---

### 2024070542001809_%5Baction%20requiered%5D%20Replacement%20of%20cephfs%20with%20anvme%20%5Bb180dc18%5D.md
# Ticket 2024070542001809

 # HPC Support Ticket: Replacement of CephFS with NVMe

## Keywords
- NVMe storage
- CephFS
- Lustre
- Workspace allocation
- Data migration
- Storage unavailability

## Summary
The HPC Admin team is upgrading the NVMe storage performance by replacing Ceph with Lustre. Users currently utilizing workspaces on `/cephfs/workspace` need to take action to migrate their data.

## Actions Required
1. **Allocate New Workspace**:
   - Use the command `ws_allocate -F anvme` to allocate a new workspace.

2. **Move Data**:
   - Transfer data from `/cephfs/workspace` to the newly allocated workspace.

3. **Notify HPC Admin**:
   - Inform the HPC Admin team once the data migration is complete and the old data is no longer needed.

## Important Dates
- **Storage Unavailability**: The storage located at `/cephfs` will become unavailable starting **01.08.2024**.

## Contact Information
- **HPC Admin Team**: support-hpc@fau.de
- **Website**: [HPC FAU](https://hpc.fau.de/)

## Root Cause
- Performance upgrade of NVMe storage requires the replacement of Ceph with Lustre.

## Solution
- Users need to allocate a new workspace, migrate their data, and notify the HPC Admin team to avoid data loss due to the upcoming storage unavailability.

## Notes
- Ensure timely action to prevent data loss.
- Follow the provided instructions for workspace allocation and data migration.
---

### 2024070542001854_%5Baction%20requiered%5D%20Replacement%20of%20cephfs%20with%20anvme%20%5Bb180dc22%5D.md
# Ticket 2024070542001854

 ```markdown
# HPC Support Ticket: Replacement of cephfs with anvme

## Keywords
- NVME storage
- CEPH
- Lustre
- Workspace allocation
- Data migration
- Storage unavailability

## Summary
The HPC site is upgrading its NVME storage by replacing CEPH with Lustre to improve performance. Users are required to migrate their data from `/cephfs/workspace` to a new workspace allocated with `ws_allocate -F anvme`.

## User Actions
1. Allocate a new workspace using `ws_allocate -F anvme`.
2. Transfer data from `/cephfs/workspace` to the new workspace.
3. Notify HPC Admins once data migration is complete for deletion of old data.

## Important Dates
- Storage at `/cephfs` will become unavailable starting 01.08.2024.

## Solution
- Users should follow the steps outlined in the ticket to migrate their data and notify HPC Admins upon completion.

## Notes
- The user acknowledged the heads-up and started the data transfer process.
- The user confirmed the completion of data transfer and requested the deletion of the old workspace.
- The ticket was closed after the user confirmed the completion of the data migration.
```
---

### 2024073142001519_Anfrage%20auf%20Verl%C3%83%C2%A4ngerung%20des%20Jobs%201914495.md
# Ticket 2024073142001519

 ```markdown
# HPC Support Ticket Conversation Analysis

## Subject: Request for Job Extension (Job ID: 1914495)

### Keywords:
- Job Extension
- Filesystem Usage
- CEPH to Lustre Migration
- NVME Storage
- Workspace Allocation

### Summary:
A user requested an extension for a job (ID: 1914495) to 4 days. The HPC Admin denied the request due to the use of an outdated filesystem (/cephfs) which is scheduled to be decommissioned.

### Root Cause:
- The job was using the /cephfs filesystem, which is being phased out in favor of /anvme.

### Solution:
- Users need to allocate a new workspace using `ws_allocate -F anvme` and move their data to the new workspace.
- The old data on /cephfs should be deleted once it is no longer needed.

### General Learnings:
- Always check the filesystem being used by jobs before requesting extensions.
- Be aware of upcoming changes in storage systems and migrate data accordingly.
- Communicate with the HPC support team for any urgent matters, especially during holidays.

### Additional Notes:
- The user was informed about the filesystem change on 5.07 and the deadline for migration is 01.08.2024.
- For urgent matters during holidays, users should contact the service center.
```
---

### 2024070542001792_%5Baction%20requiered%5D%20Replacement%20of%20cephfs%20with%20anvme%20%5Bb160dc10%5D.md
# Ticket 2024070542001792

 ```markdown
# HPC Support Ticket: Replacement of cephfs with anvme

## Keywords
- cephfs
- anvme
- workspace
- data migration
- storage discontinuation

## Summary
The HPC site is replacing CEPH with Lustre to increase NVME storage performance. Users are required to migrate their data from `/cephfs/workspace` to `/anvme/workspace`.

## Root Cause
- The current storage system (CEPH) is being replaced with a new system (Lustre) for improved performance.

## Solution
1. **Allocate New Workspace**:
   - Use the command `ws_allocate -F anvme` to allocate a new workspace.

2. **Move Data**:
   - Transfer data from `/cephfs/workspace` to the newly allocated `/anvme/workspace`.

3. **Notify HPC Admins**:
   - Inform HPC Admins once the data has been successfully moved and the old workspace is no longer needed.

## Timeline
- **Initial Notification**: Users were informed about the upcoming discontinuation of `/cephfs` storage.
- **Reminder**: A reminder was sent to ensure users take necessary actions.
- **User Action**: The user confirmed that data has been moved and the old workspace can be deleted.
- **Admin Action**: The workspace was released, and cleanup was scheduled.

## Important Dates
- **Discontinuation Date**: `/cephfs` storage will become unavailable starting 01.08.2024.

## Notes
- Ensure all users are aware of the storage migration and take necessary actions to avoid data loss.
- Regular reminders should be sent to users to ensure compliance with the migration process.
```
---

### 2023121842002133_Long%20installation%20times%20with%20pip.md
# Ticket 2023121842002133

 # HPC Support Ticket: Long Installation Times with pip

## Keywords
- pip installation
- venv
- file server load
- Ceph storage
- workspaces
- high load
- temporary problem

## Problem Description
- User experiencing long installation times with pip in a virtual environment (venv) on the Alex cluster.
- Colleagues do not face the same issue.

## Root Cause
- High load on file servers, particularly when installing venv into `$HOME` or `$WORK`.

## Solution
- No immediate solution available.
- Suggested to try Ceph storage accessible through Alex, but it is under evaluation and requires regular backups.
- Ceph storage is used through workspaces with a certain lifetime that needs manual extension.

## Additional Notes
- The issue is often temporary and may not affect all users.
- User is working on a comparison study requiring frequent venv creations and installations.
- HPC Admin suggested streamlining the process but no specific solution was provided.

## Follow-up
- User will wait until Ceph storage is out of evaluation or until installation times become unbearable.
- HPC Admin acknowledged the pain points and hopes to provide an alternative in the future.

## Documentation
- Preliminary documentation on workspaces is attached to the ticket.

## Conclusion
- The issue is related to file server load and may be mitigated by using Ceph storage in the future. However, Ceph storage is still under evaluation and has no guarantees regarding availability and integrity. Regular backups are recommended.
---

### 2024031542002752_Umzug%20Ceph-Workspace%20auf%20neuen%20User.md
# Ticket 2024031542002752

 ```markdown
# HPC-Support Ticket: Transferring Ceph-Workspace to New User Account

## Keywords
- Ceph-Workspace
- User Account Transfer
- Data Migration
- Project Account Expiration

## Problem
- User had been using a Ceph-Workspace created by an old user account (b185cb17) for storing training data.
- The old project account is expiring, and a new project account has been created.
- User wants to transfer the Ceph-Workspace to the new user account (b214cb11) to avoid manual data transfer.

## Solution
- **HPC Admins** informed the user that it is not possible to transfer workspaces between accounts.
- User needs to request a new workspace with the new account (b214cb11) and manually migrate the data.

## General Learning
- Ceph-Workspaces cannot be transferred between user accounts.
- When a project account expires, users must create a new workspace with the new account and manually transfer the data.
```
---

### 2024070542001756_%5Baction%20requiert%5D%20Replacement%20of%20cephfs%20with%20anvme%20%5Bb105dc11%5D.md
# Ticket 2024070542001756

 # HPC Support Ticket: Replacement of cephfs with anvme

## Keywords
- NVME storage
- CEPH
- Lustre
- Workspace allocation
- Data migration
- Storage unavailability

## Summary
The HPC support team is upgrading the NVME storage system by replacing CEPH with Lustre to improve performance. Users are required to migrate their data from the current `/cephfs/workspace` to a new workspace allocated with `ws_allocate -F anvme`. The old storage will become unavailable starting 01.08.2024.

## User Issue
- User received an email delivery failure notice due to an incorrect email address.
- User confirmed that the data on `/cephfs/workspace` can be deleted.

## Solution
- HPC Admin moved the user's data on `/cephfs/workspace` to `.removed`.
- The support ticket was closed after confirming the data migration and deletion.

## Lessons Learned
- Always ensure email addresses are correct to avoid delivery failures.
- Communicate storage changes well in advance to allow users time to migrate their data.
- Provide clear instructions for data migration, including commands and deadlines.
- Confirm with users once their data has been successfully migrated or deleted.

## Actions Taken
- HPC Admin sent a notification email to the user regarding the storage upgrade and data migration process.
- User confirmed that the data on `/cephfs/workspace` can be deleted.
- HPC Admin moved the user's data to `.removed` and closed the support ticket.
---

