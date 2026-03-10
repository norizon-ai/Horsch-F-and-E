# Topic 47: server_storage_investment_budget_backup

Number of tickets: 5

## Tickets in this topic:

### 2022061042000109_Daten%20und%20GPU-Server%20Hosting.md
# Ticket 2022061042000109

 ```markdown
# HPC-Support Ticket Conversation: Daten und GPU-Server Hosting

## Keywords
- Data storage
- Backup
- Archiving
- GPU servers
- Budget planning
- HPC clusters
- Investment
- Hosting
- NHR

## Summary
A user from the Philosophical Faculty, Institute for Psychology, is planning a computing infrastructure and requires advice and pricing for data storage, GPU servers, and backup solutions. The conversation covers various aspects of data management, including storage quality, access patterns, and backup requirements. The user also inquires about GPU server options and the possibility of hosting a custom GPU server at the RRZE.

## Key Points Learned

### Data Storage and Backup
- **Archiving**: The user needs a solution for archiving 3-5TB of data annually for 10 years. The data should be logically divided into independent 50GB chunks.
- **Analysis Data**: The user requires 30TB of SSD storage for data analysis, accessible both locally and via HPC systems. No backup is needed for this data.
- **Additional Data**: The user needs 200TB of disk storage, accessible from GPU servers. Backup may be required for this data.

### GPU Servers
- **GPU Hours**: The user inquires about the number of GPU hours included in the basic provision and the possibility of additional hours through NHR applications.
- **Custom GPU Server**: The user considers hosting a custom GPU server at the RRZE and provides a detailed configuration for discussion.

### Budget and Investment
- **Budget Planning**: The user is currently in the budget planning phase and prefers one-time investments over recurring payments.
- **Investment Options**: The user is open to investing in existing GPU systems and discusses the pros and cons of different investment strategies.

### Solutions and Recommendations
- **Backup/Archive**: The existing backup/archive prices are a good starting point. Long-term cost predictions are not feasible due to technological advancements.
- **Storage Quality**: SSD storage is recommended for analysis data, while disk storage is sufficient for additional data.
- **GPU Server Hosting**: The RRZE offers server hosting/housing services. The user is advised to consult the relevant documentation and forms.
- **Custom GPU Server**: A detailed configuration is discussed, including CPU, GPU, storage, and networking components. The estimated cost for such a server is around 50-60k€.

## Root Cause of the Problem
The user requires a comprehensive computing infrastructure for data storage, analysis, and backup, along with high-performance GPU servers for deep learning tasks. The user seeks advice on the best solutions, pricing, and investment strategies.

## Solution
The HPC Admins provide detailed advice on data storage, backup, and GPU server options. They discuss the user's requirements, offer recommendations, and provide information on available services and investment options. The user is advised to write a formal request, which will be reviewed by the HPC team for further action.
```
---

### 2022082342003105_Erweiterung%20der%20Rechenleistung%20durch%20Rechenknoten%2C%20welche%20durch%20das%20Fraunhofer%20I.md
# Ticket 2022082342003105

 ```markdown
# HPC Support Ticket: Expansion of Computing Capacity with Fraunhofer IIS Funded Compute Nodes

## Keywords
- Compute Server
- GPU System
- Machine Learning
- Deep Learning
- ETH Hybrid-Kabel
- HDR Anschlusskabel
- Bestellvorgang
- Leistungsbeschreibung

## Summary
The user is in the process of ordering an additional compute server to expand the HPC's computing capacity, financed by Fraunhofer IIS. The ticket involves clarifying technical details about cabling for the new server.

## Root Cause
The user needs specific information about the cabling requirements for the new compute server:
1. Whether the ETH Hybrid-Kabel (100 GbE to 4 x 25/10 GbE) is a copper cable.
2. The required length of the HDR Anschlusskabel (optical).

## Solution
The user requests clarification on the cabling specifications to complete the order process. They are bound by an offer deadline and need a quick resolution.

## Next Steps
- **HPC Admins**: Provide the user with the necessary information about the cabling specifications.
- **2nd Level Support Team**: Assist in resolving any technical queries related to the cabling if needed.

## Notes
- The user has attached a performance description for reference.
- The user is under a time constraint due to an offer deadline.
```
---

### 2024050242002282_WG%3A%20W%202-Professur%20f%C3%83%C2%BCr%20Intelligente%20Sprachschnittstellen%3B%20Konzeptpapier.md
# Ticket 2024050242002282

 # HPC Support Ticket Analysis

## Subject
WG: W 2-Professur für Intelligente Sprachschnittstellen; Konzeptpapier

## Keywords
- Rechenzeit
- Serverkosten
- All-Flash
- Nvidia H100
- Tier3-Grundversorgung
- NHR@FAU
- Abwärmeleistung
- Kanzler

## Summary
A user submitted a concept paper requesting a commitment for computing time and an evaluation of the costs and feasibility of desired servers.

## Root Cause
- User requested evaluation of server costs and computing time.
- Specific hardware requirements: 30 TB All-Flash storage and 8x Nvidia H100 GPUs.

## Analysis
- **Cost Evaluation**: 60k€ for 30 TB All-Flash storage is overpriced. A server with 8x Nvidia H100 GPUs for 160k€ is unlikely.
- **Feasibility**: The Informatik-Serverraum has capacity for a server with 10 kW heat dissipation.
- **Computing Time**: 200,000 GPU-hours in Tier3-Grundversorgung discussed with Gerhard. Decision lies with the Kanzler.

## Solution
- **Cost**: Re-evaluate the cost of storage and GPUs.
- **Feasibility**: Ensure the server room can handle the heat dissipation.
- **Computing Time**: Await decision from the Kanzler regarding Tier3 resources.

## Conclusion
The decision on allocating significant Tier3 resources to a W2-Professor lies with the Kanzler. The feasibility of the server setup should be re-evaluated for cost and energy efficiency.

---

**Note**: This report is intended for internal use by HPC support employees to assist in resolving similar issues in the future.
---

### 2023090142003465_AW%3A%20Anfrage%20Housing%20von%20ML-Rechnerkapazit%C3%83%C2%A4ten%20-%20UTN%20%2810%20Nodes%20mit%2.md
# Ticket 2023090142003465

 # HPC Support Ticket Conversation Analysis

## Subject
AW: Anfrage Housing von ML-Rechnerkapazitäten - UTN (10 Nodes mit je 8x RTX6000)

## Keywords
- Housing von Hardware
- Rechenleistung im Batchbetrieb
- NHR@FAU
- GPU-Server
- RTX A6000
- Storage
- Maintenance

## Summary
The user inquires about the feasibility of housing specific ML computing capacities at the HPC site. The HPC Admins provide detailed options for both housing the hardware and utilizing existing HPC cluster resources.

## Root Cause of the Problem
The user needs to determine whether to house their own hardware or utilize existing HPC resources for ML computations.

## Options Provided
1. **Housing of Hardware**:
   - RRZE-Systemgruppe offers housing/hosting as a standard service.
   - Requires at least one complete rack for 10 GPU servers with 8 GPUs each.
   - Estimated ~30 kW power and cooling requirements, likely distributed across 3 racks.
   - Pricing details available on RRZE website.

2. **Rechenleistung im Batchbetrieb**:
   - NHR@FAU can provide initial computing power on the Tier3/NHR-GPGPU-Cluster "Alex".
   - Future expansion with L40-GPGPU-Knoten (successor to A40) is planned.
   - Investment in homogeneous system expansion possible with access to NHR@FAU conditions.
   - Estimated costs for 10 L40-Knoten: 800,000-1,000,000 € including 5 years of hardware maintenance.
   - Additional storage investment required, estimated ~50,000 € for 200 TB NVMe-Storage.

## Solution
The user should evaluate the provided options and decide whether to house their own hardware or utilize the existing HPC cluster resources. Further discussions and a Zoom meeting can be arranged for detailed planning.

## Next Steps
- The user will discuss the options with the applicant and may contact the HPC Admins for further questions.
- A Zoom meeting can be scheduled for personal discussion.

## Additional Notes
- The user expresses gratitude for the quick and comprehensive response.
- The HPC Admins provide detailed cost estimates and technical considerations for both options.

---

This report summarizes the key points from the HPC support ticket conversation, providing a reference for future similar inquiries.
---

### 2022062242003763_Fwd%3A%20W3%20Professur%20Cognitive%20Computational%20Neuroscience%20-%20Wunschpapier%20Fatma%20Deni.md
# Ticket 2022062242003763

 ```markdown
# HPC Support Ticket Conversation Analysis

## Keywords
- Datenanalyse-Server
- A100 GPU
- Storage
- RAM
- Budget
- Patientendaten
- TinyGPU
- Backup
- Archiv
- RRZE-Basisstorage

## Summary
- **User Request**: A dedicated data analysis server for handling sensitive patient data.
- **Specifications**: A100 80 GB GPU, 240TB Storage, 8 TB SSD, 128 GB RAM.
- **Budget**: 50,000.00 €
- **Additional Requests**: Costs for data storage and usage of "TinyGPU" hours for data analysis.

## HPC Admin Response
- **Necessity**: The dedicated server is essential due to the sensitive nature of patient data.
- **Budget Assessment**: The allocated budget of 50,000 € is insufficient. A more realistic estimate is 75,000 €.
  - **GPU**: 2x A100 GPUs (~25k€ each)
  - **Storage**: 240 TB (~15k€)
  - **RAM**: 128 GB is insufficient; should be more than 160 GB (~7.5k€)
  - **Additional Components**: Host processors, chassis, SSD cache.
- **TinyGPU Usage**: Agreed for non-sensitive data, with long-term plans for HPC expansion through third-party funding.
- **Backup and Archive Costs**: Appropriate.
- **RRZE-Basisstorage Costs**: Considered too high (36,000 € for 30 TB over 5 years). Suggested alternative: Purchase a dedicated server for ~10k€ and use RRZE for hosting and backup, reducing costs significantly.

## Root Cause of the Problem
- Insufficient budget allocation for the required hardware.
- High costs for RRZE-Basisstorage.

## Solution
- Increase the budget to 75,000 € to meet hardware requirements.
- Consider purchasing a dedicated server for storage and using RRZE for hosting and backup to reduce costs.
```
---

