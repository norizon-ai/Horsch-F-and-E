# Topic 35: surfconext_maintenance_rolling_providers_announcement

Number of tickets: 13

## Tickets in this topic:

### 2023112842002509_AANKONDIGING%3A%205%20december%202023%20Onderhoud%20SURFconext%20_%20ANNOUNCEMENT%3A%205%09December%.md
# Ticket 2023112842002509

 # HPC-Support Ticket Conversation Summary

## Subject
ANNOUNCEMENT: 5 December 2023 Maintenance SURFconext

## Keywords
- Maintenance
- SURFconext
- Rolling update
- Engineblock upgrade
- Software maintenance
- No downtime expected

## Summary
- **Date**: Tuesday, 5 December 2023
- **Time**: During office hours
- **Activity**: Rolling update for Engineblock upgrade
- **Impact**: No expected downtime; services should remain available
- **Affected Parties**: Identity Providers (IdPs) and Service Providers (SPs) connected to SURFconext

## Details
- **Planned Work**: Upgrade of Engineblock for software maintenance and fixes.
- **Service Availability**: All services are expected to remain operational with no downtime.
- **Impact**: No impact on the availability of SURFconext and connected IdPs and SPs.

## Notifications
- Recipients: Contact persons of institutions or services in SURFconext, subscribers to the SURFconext-alert mailing list.
- Contact for Questions: support@surfconext.nl

## Root Cause
- Regular software maintenance and fixes for Engineblock.

## Solution
- Perform the rolling update during business hours to minimize disruption.

## Notes
- This maintenance is routine and aimed at keeping the system up-to-date without causing service interruptions.
- Users should not experience any downtime, but they are encouraged to contact support if any issues arise.

---

This summary can be used as a reference for future maintenance activities and to address any similar issues that may arise.
---

### 2023080842003838_AANKONDIGING%3A%2015%20augustus%202023%20Onderhoud%20SURFconext%20_%20ANNOUNCEMENT%3A%0915%20August%.md
# Ticket 2023080842003838

 # HPC Support Ticket Conversation Summary

## Subject
**ANNOUNCEMENT: 15 August 2023 Maintenance SURFconext**

## Keywords
- Maintenance
- SURFconext
- SURFsecureID
- OpenID Connect gateway
- Infrastructure patching
- Database platform
- Rolling update
- Service availability

## Summary
- **Maintenance Window:** 05:00 - 07:00 on 15 August 2023
- **Rolling Update:** During working hours
- **Activities:**
  - Stricter validation of redirect URLs in OpenID Connect gateway
  - Patching SURFconext infrastructure
  - Minor changes to SURFconext database platform
- **Expected Impact:** No impact on connected Identity Providers (IdPs) and Service Providers (SPs)
- **Service Availability:** All services expected to remain available during maintenance

## Lessons Learned
- Regular maintenance is crucial for system stability and security.
- Rolling updates during working hours ensure minimal disruption.
- Stricter validation of redirect URLs enhances security.
- Infrastructure patching and database changes are routine maintenance tasks.
- Communication about maintenance activities helps manage user expectations.

## Root Cause (if applicable)
- N/A (This is an announcement, not a problem report)

## Solution (if applicable)
- N/A (This is an announcement, not a problem report)

## Notes
- Users receive this notification because they are listed as contacts for an Identity Provider or Service Provider, or because they are subscribed to the SURFconext-alert mailing list.
- For questions or comments, users should email support@surfconext.nl.

---

This summary provides a concise overview of the maintenance activities and their expected impact, serving as a reference for future maintenance communications and support documentation.
---

### 2024091842001666_SURFconext%20notification%3A%20disruption%20SURFconext.md
# Ticket 2024091842001666

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject: SURFconext notification: disruption SURFconext

### Keywords:
- SURFconext
- DDoS attack
- Federated login
- Service Providers
- Outage
- Helpdesk notification

### Summary:
- **Issue**: SURFconext experienced reduced availability starting from 18 September, 10:20 CET, affecting federated logins to some Service Providers.
- **Root Cause**: Suspected DDoS attack on one or more systems.
- **Action Taken**: Users were informed to notify their end-user helpdesk about the outage.
- **Status Tracking**: Users can check the status of the outage at [https://grotestoring.surf.nl](https://grotestoring.surf.nl).
- **Communication**: Further updates will be provided via email.

### Lessons Learned:
- **Notification**: Importance of timely communication with end-users and helpdesk during service disruptions.
- **Status Tracking**: Providing a link for real-time status updates helps in managing user expectations.
- **Security**: DDoS attacks can cause significant disruptions, highlighting the need for robust security measures.

### Solution:
- **Immediate**: Inform end-users and helpdesk about the outage.
- **Long-term**: Strengthen security protocols to mitigate future DDoS attacks.

### Additional Notes:
- HPC Admins attempted to unsubscribe from the mailing list to reduce spam.
```
---

### 2025021342003381_Toelichting%20incident%20SURFconext%20Dashboard%20%28opgelost%29%20_%20Explanation%20of%09SURFconext.md
# Ticket 2025021342003381

 # HPC Support Ticket: SURFconext Dashboard Incident

## Keywords
- Responsible Disclosure
- Data Leak
- Public Access
- Contact Details
- JSON File
- Developer Console
- SURFconext Dashboard

## Summary
A responsible disclosure was reported to the SURFconext team regarding a data leak in the SURFconext IdP Dashboard. Contact details of service providers were publicly accessible via a JSON file through the browser's developer console.

## Root Cause
- Contact details for administrative, technical, and support questions were stored in a single JSON file.
- This file was publicly accessible, leading to potential exposure of personal data.

## Impact
- A total of 3,200 unique email addresses were exposed.
- It is unclear if the data was misused, as log files cannot distinguish between legitimate and non-legitimate access.

## Solution
- The contact details were removed from the publicly available information.
- SURFconext advised service providers to use only functional addresses for contact roles.

## Lessons Learned
- Ensure that sensitive data is not publicly accessible.
- Regularly review and update security measures to prevent data leaks.
- Promptly address responsible disclosure reports to mitigate potential risks.

## Follow-up Actions
- Monitor for similar incidents and apply necessary security patches.
- Encourage service providers to use functional addresses for contact roles to minimize personal data exposure.

## Contact
For further questions or information, contact SURFconext support at support@surfconext.nl.

---

**Note:** This report is intended for internal use by HPC support employees to assist in resolving similar issues in the future.
---

### 2023102442002741_AANKONDIGING%3A%2031%20oktober%202023%20Onderhoud%20SURFconext%20_%20ANNOUNCEMENT%3A%2031%09October%.md
# Ticket 2023102442002741

 # HPC Support Ticket Analysis

## Subject
**AANKONDIGING: 31 oktober 2023 Onderhoud SURFconext / ANNOUNCEMENT: 31 October 2023 Maintenance SURFconext**

## Keywords
- Maintenance
- SURFconext
- Rolling Update
- Autorisation Rules
- Attribute Aggregation
- OpenID Connect
- IP Ranges
- Negation
- Bugfix
- SURFconext Invite
- ID Token
- Claims
- Downtime
- Impact

## Summary
- **Date**: Tuesday, 31 October 2023
- **Time**: During office hours
- **Type**: Rolling update
- **Services Affected**: SURFconext
- **Expected Downtime**: None
- **Impact**: No impact on connected Identity Providers (IdPs) and Service Providers (SPs)

## Details
- **Autorisation Rules**:
  - Support for negation across multiple IP ranges
  - Bugfix for negation in combination with multiple attribute values
- **Attribute Aggregation**:
  - Support for SURFconext Invite
- **OpenID Connect**:
  - Ability to receive claims directly in ID token

## Root Cause
- N/A (This is an announcement for scheduled maintenance)

## Solution
- N/A (This is an announcement for scheduled maintenance)

## Notes
- Users are informed because they are listed as contacts for an Identity Provider or Service Provider, or subscribed to the SURFconext-alert mailing list.
- Questions and comments should be directed to `support@surfconext.nl`.

## Conclusion
This maintenance announcement informs users about a rolling update to SURFconext services, including improvements to autorisation rules, attribute aggregation, and OpenID Connect. No downtime is expected, and the impact on connected services is minimal.
---

### 2024051442002634_SURFconext%20notification%3A%20Verstoring%20SURFconext%20_%20SURFconext%20notification%3A%20Disrupti.md
# Ticket 2024051442002634

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject: SURFconext notification: Verstoring SURFconext / SURFconext notification: Disruption SURFconext

### Keywords:
- SURFconext
- Network Disruption
- Federated Login
- Service Providers
- Status Update
- Support Contact

### Summary:
- **Issue**: SURFconext experienced a nationwide disruption starting on May 14 around 15:50 CEST, affecting federated login for connected service providers.
- **Impact**: Users were temporarily unable to log in to services connected via SURFconext.
- **Status**: Most services have been restored, but some components are still experiencing issues.
- **Communication**: Users were informed about the status and progress via email and a dedicated status page.

### Root Cause:
- Nationwide disruption within the SURF network.

### Solution:
- The SURFconext team is actively working to resolve the remaining issues.
- Users can check the status page and will receive updates via email.

### Lessons Learned:
- Importance of prompt communication during service disruptions.
- Value of a dedicated status page for real-time updates.
- Necessity of having a backup plan for critical services to minimize downtime.

### Actions Taken:
- The HPC Admin closed the customer request.

### Recommendations:
- Ensure that critical services have redundancy and failover mechanisms.
- Maintain open communication channels with users during service disruptions.
- Regularly update the status page to keep users informed.
```
---

### 2023111542003747_AANKONDIGING%3A%2021%20november%202023%20Onderhoud%20SURFconext%20_%20ANNOUNCEMENT%3A%0921%20Novembe.md
# Ticket 2023111542003747

 # HPC Support Ticket: SURFconext Maintenance Announcement

## Keywords
- Maintenance
- SURFconext
- Load Balancer
- Configuration Adjustment
- No Downtime Expected

## Summary
- **Date:** 21 November 2023
- **Time:** 05:00 - 07:00 CET
- **Activity:** Load balancer configuration adjustment
- **Expected Impact:** No downtime expected; services should remain available

## Details
- **Notification:** Sent to contact persons of Identity Providers and Service Providers, and subscribers of the SURFconext-alert mailing list.
- **Support Contact:** support@surfconext.nl

## Lessons Learned
- Regular maintenance activities are crucial for system stability.
- Load balancer adjustments can be performed without service interruption.
- Effective communication with users and stakeholders is essential before maintenance activities.

## Root Cause (if applicable)
- N/A (This is an announcement, not a problem report)

## Solution (if applicable)
- N/A (This is an announcement, not a problem report)

## Notes
- Ensure that all relevant parties are informed about maintenance windows.
- Monitor the system during maintenance to confirm no downtime occurs.
- Document any changes made during maintenance for future reference.
---

### 2023100342000434_AANKONDIGING%3A%2010%20oktober%202023%20Onderhoud%20SURFconext%20_%20ANNOUNCEMENT%3A%2010%09October%.md
# Ticket 2023100342000434

 # HPC-Support Ticket Conversation Summary

## Subject
ANNOUNCEMENT: 10 October 2023 Maintenance SURFconext

## Keywords
- Maintenance
- SURFconext
- Privacy questions
- Service Provider Dashboard
- IdP Dashboard
- Rolling update
- No downtime

## Summary
- **Date**: Tuesday, 10 October 2023
- **Time**: During office hours
- **Description**: Revision of privacy questions in the Service Provider Dashboard and IdP Dashboard.
- **Availability**: Services expected to remain available with no downtime.
- **Impact**: No impact on the availability of SURFconext and connected SAML IdPs and SPs.

## Root Cause
- Scheduled maintenance for updating privacy questions in the dashboards.

## Solution
- Rolling update during business hours to ensure minimal disruption.

## Notes
- Users are notified because they are listed as contacts for an Identity Provider or Service Provider, or subscribed to the SURFconext-alert mailing list.
- Questions and comments should be directed to `support@surfconext.nl`.

## Relevant Links
- [Service Provider Dashboard](https://wiki.surfnet.nl/pages/viewpage.action?pageId=10125365)
- [IdP Dashboard](https://dashboard.surfconext.nl/apps/all)

## Conclusion
This maintenance is routine and should not affect the availability of services. Users are informed to be aware of the changes and to contact support if any issues arise.
---

### 2024051442002769_Re%3A%20SURFconext%20notification%3A%20Verstoring%20SURFconext%20_%20SURFconext%20notification%3A%20.md
# Ticket 2024051442002769

 ```markdown
# HPC-Support Ticket Conversation Analysis

## Subject
Re: SURFconext notification: Verstoring SURFconext / SURFconext notification: Disruption SURFconext

## Keywords
- SURFconext
- Disruption
- Login issues
- Network outage
- Status updates
- Support contact

## Summary
- **Issue**: SURFconext was partially unreachable due to a nationwide disruption in the SURF network.
- **Impact**: Federated login was temporarily unavailable for all connected service providers.
- **Resolution**: The disruption was resolved, and logging in via SURFconext is possible again for all users and services.
- **Follow-up**: The SURFconext team will evaluate the outage and take measures to prevent future recurrences.

## Root Cause
- Nationwide disruption within the SURF network.

## Solution
- The SURFconext team worked to resolve the network issues, restoring login functionality for most services.

## Lessons Learned
- **Communication**: Regular updates were provided via email and a status page.
- **Support**: Users were directed to a support email for further assistance.
- **Prevention**: Comprehensive evaluation and preventive measures will be taken to avoid similar issues in the future.

## Actions Taken
- **HPC Admins**: Closed the customer request after the issue was resolved.
- **2nd Level Support Team**: Monitored the situation and provided updates as necessary.

## Recommendations
- Ensure that network redundancy and failover mechanisms are in place to minimize the impact of such disruptions.
- Maintain clear communication channels with users during outages.
- Regularly review and update incident response plans to improve future handling of similar issues.
```
---

### 2023091342001668_AANKONDIGING%3A%2019%20september%202023%20Onderhoud%20SURFconext%20_%20ANNOUNCEMENT%3A%0919%20Septem.md
# Ticket 2023091342001668

 # HPC Support Ticket Analysis

## Subject
ANNOUNCEMENT: 19 September 2023 Maintenance SURFconext

## Keywords
- Maintenance
- SURFconext
- IP Configuration
- SURFsecureID Token
- Rolling Update
- No Downtime

## Summary
A maintenance announcement for SURFconext was sent out, detailing a rolling update during business hours on September 19, 2023. The update involves changes to IP address configurations to enable or disable the requirement for a SURFsecureID token based on IP range. No downtime is expected, and the availability of SURFconext and connected SAML IdPs and SPs will not be affected.

## User Concern
The user received a notification about the maintenance and shared it with the HPC Admins.

## HPC Admin Response
The HPC Admins indicated that the maintenance was not a concern for them.

## Lessons Learned
- Regular maintenance notifications are important for keeping stakeholders informed.
- Changes to IP configurations can be implemented without downtime.
- The impact of such changes on connected services should be minimal.

## Root Cause
No specific problem was reported; the ticket was an informational announcement.

## Solution
No action required from the HPC Admins as the maintenance is expected to have no impact on their operations.

## Documentation for Future Reference
- **Maintenance Notifications:** Ensure that all relevant parties are informed about upcoming maintenance.
- **IP Configuration Changes:** Understand that such changes can be implemented without service disruption.
- **Impact Assessment:** Evaluate the impact of maintenance activities on connected services to ensure minimal disruption.
---

### 2023061342002565_AANKONDIGING%3A%2020%20juni%202023%20Onderhoud%20SURFconext%20_%20ANNOUNCEMENT%3A%2020%09June%202023.md
# Ticket 2023061342002565

 # HPC Support Ticket Conversation Summary

## Subject
- **ANNOUNCEMENT: 20 June 2023 Maintenance SURFconext**

## Keywords
- Maintenance
- SURFconext
- Loadbalancer
- Rolling update
- oidcng
- Redirect URL validation
- loa1_5 to loa1.5
- Downtime
- Impact
- Identity Providers (IdPs)
- Service Providers (SPs)

## Summary
- **Maintenance Window**: 05:00 - 07:00 on 20 June 2023
- **Rolling Update**: During office hours on 20 June 2023
- **Planned Activities**:
  - Update loadbalancer configuration
  - Bugfix for redirect URL validation when a query parameter is used
  - Change loa1_5 to loa1.5
- **Availability of Services**: Expected to remain available with no downtime
- **Impact**: No impact on connected SAML IdPs and SPs

## Root Cause
- Scheduled maintenance and updates to improve system performance and fix bugs.

## Solution
- Perform the updates as planned during the specified maintenance window and rolling update period.

## Notes
- Users are notified because they are listed as contacts for an Identity Provider or Service Provider, or subscribed to the SURFconext-alert mailing list.
- For questions and comments, users should contact `support@surfconext.nl`.

## General Learning
- Regular maintenance and updates are essential to ensure system stability and performance.
- Communication with users about maintenance schedules and expected impacts is crucial for transparency and minimizing disruptions.

---

This summary provides a concise overview of the maintenance activities, their impact, and the steps taken to ensure smooth operations. It can be used as a reference for future maintenance planning and user communication.
---

### 2023070642001443_AANKONDIGING%3A%2013%20juli%202023%20Onderhoud%20SURFconext%20_%20ANNOUNCEMENT%3A%2013%09July%202023.md
# Ticket 2023070642001443

 # HPC Support Ticket Analysis

## Subject
ANNOUNCEMENT: 13 July 2023 Maintenance SURFconext

## Keywords
- Maintenance
- SURFconext
- Rolling update
- Patching infrastructure
- No downtime expected

## Summary
- **Date:** Thursday, 13 July 2023
- **Time:** During office hours
- **Activity:** Rolling update and patching of SURFconext infrastructure
- **Expected Impact:** No downtime expected; services should remain available

## User Concern
- User received a notification about scheduled maintenance for SURFconext infrastructure.
- Maintenance involves patching the infrastructure.
- No downtime is expected, and services should remain available.

## HPC Admin Response
- HPC Admin indicated that the maintenance is not a concern for them.

## Lessons Learned
- Regular maintenance and updates are essential for infrastructure stability.
- Communication about maintenance schedules is important to ensure stakeholders are informed.
- HPC Admins may not always be directly impacted by external service maintenance.

## Solution
- No action required from HPC Admins as the maintenance is expected to have no impact on services.

## Additional Notes
- Users are notified via email as they are listed as contacts for Identity Providers or Service Providers, or subscribed to the SURFconext-alert mailing list.
- Questions and comments should be directed to `support@surfconext.nl`.
---

### 2024090542001985_AANKONDIGING%3A%2012%20september%202024%20Onderhoud%20SURFconext%20_%20ANNOUNCEMENT%3A%0912%20Septem.md
# Ticket 2024090542001985

 # HPC-Support Ticket Conversation Analysis

## Subject
**AANKONDIGING: 12 september 2024 Onderhoud SURFconext / ANNOUNCEMENT: 12 September 2024 Maintenance SURFconext**

## Keywords
- Maintenance
- SURFconext
- Rolling update
- Patch infrastructure
- No downtime
- Office hours
- 12 September 2024

## Summary
- **Date**: 12 September 2024
- **Time**: During office hours
- **Activity**: Rolling update and patching of SURFconext infrastructure
- **Expected Impact**: No downtime expected; services should remain available
- **Affected Services**: SURFconext, connected Identity Providers (IdPs), and Service Providers (SPs)

## Details
- The SURFconext team will perform a rolling update during business hours on 12 September 2024.
- The update involves patching the SURFconext infrastructure.
- No downtime is expected, and all services are expected to remain available.
- The maintenance will not affect the availability of SURFconext or connected IdPs and SPs.

## Notifications
- Recipients are listed as contacts of an Identity Provider or Service Provider, or subscribed to the SURFconext-alert mailing list.
- Questions and comments should be directed to `support@surfconext.nl`.

## Root Cause and Solution
- **Root Cause**: N/A (This is an announcement, not a problem report)
- **Solution**: N/A

## General Learning
- Regular maintenance and updates are crucial for the smooth operation of HPC services.
- Rolling updates can minimize downtime and ensure continuous service availability.
- Effective communication with users and stakeholders is essential before scheduled maintenance.

## Notes for Support Employees
- Ensure that all relevant contacts are informed about upcoming maintenance.
- Monitor the system during updates to address any unexpected issues promptly.
- Document any changes or updates for future reference and troubleshooting.
---

