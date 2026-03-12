# CLAUDE.md — HORSCH F&E: Project Context & Implementation Brief

> This document is the canonical briefing for Claude Code working on the HORSCH F&E workstream. Keep it up to date as the project evolves.

---

## Instructions for Claude Code

Before doing anything else in this project, read the following Confluence pages in full. They contain all the context you need — the user problem, the stakeholder needs, the technical architecture, and the implementation plan. Use the Atlassian MCP tool to fetch them by page ID:

| Page | ID | What it contains |
|------|----|-----------------|
| F&E Bedarfsanalyse (Stakeholder Interview) | **27459585** | Detailed needs analysis — pain points, workflow, requirements from Matthias & Robert |
| F&E Austausch – Wissensmanagement & KI | **27426817** | Second stakeholder interview write-up — same meeting, narrative format |
| (Internal) HORSCH F&E Workstream Overview | **27623425** | Full onboarding doc — big picture, key people, open questions for Omar |
| Implementation Proposal for F&E | **27983873** | Step-by-step technical spec — JiraAgent, attachment search, instantiation, Azure deployment |

---

## Who I Am & What I'm Working On

I'm **Omar**, a developer at **Norizon**. I'm working on the **HORSCH F&E workstream** — building an AI-powered search tool for the engineering team at HORSCH Maschinen GmbH (a leading agricultural machinery manufacturer in Schwandorf, Germany).

Norizon and HORSCH have a **9-month cooperation (Q3 2025 – Q2 2026)** covering AI-powered knowledge management. I joined in March 2026 and own the F&E workstream end-to-end.

---

## The Problem We're Solving

HORSCH's R&D engineers (constructors) cannot find information in their Confluence/Jira systems. The built-in Confluence search is broken for their use case. This causes:

- Engineers asking colleagues instead of searching ("Frag mal den, der weiß das schon")
- Design guideline violations going undetected until PDM release — the very last step, costly and frustrating
- A vicious cycle: nobody finds anything → nobody documents → data quality worsens
- Contradictory information between Confluence pages and Jira comments with no version control

**The core ROI:** Catching design errors at step 2 (research) instead of step 6 (release).

---

## What We're Building

An AI-powered search tool running on the **Norizon Nora platform (DeepSearch)**. Engineers query Confluence and Jira in natural language and get answers with clickable source links.

- **Platform:** Norizon Nora / DeepSearch
- **Infrastructure:** Isolated per-client deployment on **Norizon's Azure** — one resource group per customer (see Multi-Tenancy below)
- **Test users:** Matthias (Construction/Setting Tech) and Robert (CAD Admin) — ~1h every 2 weeks

### Must-Have Requirements (from stakeholder interviews)
- Natural language queries — typo-tolerant, word order doesn't matter
- Clickable source links back to Confluence pages / Jira tickets
- Compact answers first, drill deeper on follow-up
- Search PDFs and file attachments, not just Confluence page text
- Confluence AND Jira searchable in one interface

---

## Architecture Decisions (from Lisa & Omar call, March 2026)

### Multi-Tenancy — One Resource Group Per Client
Each client (e.g. HORSCH) gets its own dedicated Azure Resource Group containing all its own resources: Container Apps (frontend, deepsearch, confluence-mcp, jira-mcp), PostgreSQL database, Key Vault (for Confluence/Jira personal tokens), and networking. No shared infrastructure between clients or with the internal Norizon deployment.

### MCP Container Split — Confluence and Jira Separated
`confluence-mcp` and `jira-mcp` run as **separate containers**, not combined. This makes each easier to manage, debug, and scale independently. Both use the same `mcp-atlassian` base image but with different env vars and responsibilities.

### Attachment Search Strategy
The current `ConfluenceMCPAgent` uses CQL live queries — known to have limitations in indexing accuracy, especially for attachments on Server/DC. Agreed approach:
1. **Now:** Try CQL attachment strategies first (`type = attachment AND text ~ "keyword"`) — simple, no extra infra
2. **If CQL is insufficient on HORSCH's Server/DC instance:** Hybrid approach — keep the live Confluence connection (no local data loading), layer Elasticsearch indexing on top to improve retrieval, then use `ConfluenceGetPageTool` to extract full page content for the results. This avoids storing data locally while gaining ES search quality.
3. **Decision point:** Evaluate after first connection to HORSCH's Confluence. Involve Christoph Wiesent to check if Office Connector plugin is installed.

### Repo Strategy — Work in Norizon Repo, HORSCH in instantiations/
All shared platform code (frontend, deepsearch, MCP services) lives in the main **Norizon repo**. HORSCH F&E is an instantiation inside `instantiations/horsch_fue/`. Changes made for HORSCH that improve the platform flow back into the shared codebase naturally. **Not** using git submodules.

### shadcn/ui
The redesigned Svelte 5 frontend uses **shadcn/ui** — the component library behind the modern aesthetic seen in Claude, ChatGPT, Linear etc. Confirm with Claude Code whether it was included in the Svelte 5 migration.

---

## Security Requirements

- **No open endpoints on the internet** — internal services (MCP containers, databases) must not be publicly accessible. Everything sits behind Azure networking / private endpoints.
- **EU data residency** — all infrastructure deployed on Azure EU regions (DSGVO/GDPR compliant). Data never leaves EU.
- **Atlassian Data Center compatible** — all Confluence/Jira integrations must support Server/DC auth (personal access tokens, not cloud API keys).

---

## Quality Requirements

- **Search accuracy** — the ConfluenceMCPAgent CQL approach has known accuracy limitations. Must be evaluated on HORSCH's actual Confluence and improved if insufficient (see Attachment Search Strategy).
- **Conflicting information handling** — the system must handle contradictory information between Confluence and Jira. How conflicts are surfaced to the user is an open design question — needs explicit solution before handoff to test users.

---

## To-Do: Playbook / Documentation (Planned)

Write a **setup playbook** in Confluence covering the full end-to-end deployment story:

- **Part 1 — Multi-Tenancy Model & Resource Group Setup:** How we structure Azure per client (one resource group per client), what gets provisioned (Container Apps, PostgreSQL, Key Vault, networking), and how to replicate it for a new client onboarding
- **Part 2 — Azure Entra External ID (CIAM) Setup:** How CIAM was configured end-to-end, app registration per client, the MSAL.js integration, backend JWT verification, and gotchas (e.g. v4 cache regression, Safari ITP on localhost)
- **Part 3 — Full Deployment Reference:** Container Apps config, Key Vault secret seeding, env vars per service, networking rules (no public endpoints on MCP/DB)

> ⏳ Planned — to be written during or after the HORSCH F&E Azure deployment (Step 5), when the full process is fresh.

---

## Progress Log

### Frontend Modernisation + Svelte 5 Migration — DONE (March 2026)
- **Svelte 5 migration complete** — all components use runes API (`$props()`, `$state()`, `$derived()`, `$effect()`, `untrack()`, `{@render}`, `onclick`)
- **UI redesigned** to ChatGPT/Claude aesthetic — centered conversation rail, clean white backgrounds, inline sources
- **Meeting documentation workflow**: full pipeline working (upload → processing → speaker verification → template review → export)
- **Delete flow**: deleting current open chat navigates back to homepage
- **Docker Compose**: full local stack running (frontend, deepsearch, searxng, workflow-service, deepgram-service, postgres, redis, minio, confluence-mcp, confluence-publisher)
- **Svelte 4 stores** (`writable`/`derived` in `svelte/store`) still used in store files — not yet migrated to `.svelte.ts` runes. Works fine, not fully Svelte 5 idiomatic yet.

### Auth0 → Azure Entra External ID (CIAM) — DONE (March 2026)
- **Fully replaced Auth0** with Microsoft Entra External ID (CIAM) — any email can sign up via OTP, all auth traffic stays within Azure Europe (DSGVO compliant)
- **CIAM Tenant:** `norizonauth.onmicrosoft.com` | **Authority:** `https://norizonauth.ciamlogin.com/`
- **Client ID:** `2a4c4497-8b2e-4059-a215-0ef905fa7ead` | **Tenant ID:** `4e355899-bcbf-44b5-b879-a67c2e8b3716`
- **Frontend:** `@auth0/auth0-spa-js` → `@azure/msal-browser@3.30.0` (v3 chosen over v4 due to known v4 cache regression — GitHub issues #7551, #7533)
- **authStore.ts** fully rewritten with MSAL.js — same store interface preserved
- **ID token** sent to backend (CIAM returns opaque access tokens with OIDC scopes)
- **Backend JWT verification** via OIDC discovery from `norizonauth.ciamlogin.com` — auto-discovers JWKS URI and issuer
- **Database migration**: `auth0_subject` → `external_subject` column rename (Alembic migration `002`)
- **Docker Compose env vars** updated for both frontend and workflow-service
- **Session persistence**: Works on Chrome; Safari localhost limited by ITP (will work on production with real domain)
- **Known:** Debug logging in `workflow-service/app/auth/jwt.py` — remove after production confirmation

### Teams Recording Import Fixes — DONE (March 2026)

---

## Immediate Next Steps

> ⚠️ **Work locally first using Docker.** Validate everything end-to-end locally before touching Azure.

### Step 1 — Create HORSCH Azure Resource Group (Decouple from Norizon)
- Create a dedicated Azure Resource Group for HORSCH F&E — fully isolated from the internal Norizon deployment
- Provision: Container Apps environment, PostgreSQL instance, Key Vault (store CONFLUENCE_PERSONAL_TOKEN, JIRA_PERSONAL_TOKEN)
- Networking: ensure MCP containers and DB are not publicly exposed
- Region: Azure EU

### Step 2 — Build JiraAgent + Separate jira-mcp Container
Mirror the existing `ConfluenceMCPAgent` pattern. Separate container from confluence-mcp.

Key files to create:
- `services/jira-mcp/` — new container, mirrors confluence-mcp with Jira env vars
- `services/custom-deepresearch/deepsearch/agents/mcp_utils.py` — extract shared `_call_mcp_tool()` + `_extract_text()` from confluence/tools.py
- `services/custom-deepresearch/deepsearch/agents/jira/tools.py` — JiraSearchTool + JiraGetIssueTool
- `services/custom-deepresearch/deepsearch/agents/jira/agent.py` — JiraMCPAgent
- `services/custom-deepresearch/deepsearch/agents/jira/__init__.py` — factory registration
- `services/custom-deepresearch/prompts/jira_agent.yaml` — JQL strategies, bilingual DE/EN
- Edit `main.py:35` — add jira import
- Add `jira-mcp` service to docker-compose with `JIRA_URL` + `JIRA_PERSONAL_TOKEN`

### Step 3 — HORSCH F&E Instantiation (Local Docker first)
Create `instantiations/horsch_fue/` with:
- `agents.yaml` — horsch_confluence + horsch_jira agents, web_search disabled
- `.env.example` — CONFLUENCE_URL, CONFLUENCE_PERSONAL_TOKEN, JIRA_URL, JIRA_PERSONAL_TOKEN
- `docker-compose.yml` — 4 services: confluence-mcp, jira-mcp, deepsearch, frontend
- Test locally against real HORSCH credentials (coordinate with Alex/Christoph)

### Step 4 — Evaluate Attachment Search on HORSCH's Server/DC
- Connect to HORSCH Confluence, run CQL attachment queries
- Check with Christoph Wiesent whether Office Connector plugin is installed
- If CQL works: done. If not: plan hybrid ES approach.

### Step 5 — Azure Deployment (HORSCH Resource Group)
- Adapt `instantiations/internal_setup/azure/` Bicep + scripts for HORSCH
- Deploy 4 Container Apps: confluence-mcp, jira-mcp, deepsearch, frontend
- Seed Key Vault with HORSCH credentials
- Confirm no public endpoints on MCP containers or DB

### Step 6 — Write Setup Playbook in Confluence
- Document Azure Entra External ID (CIAM) setup end-to-end
- Document full Azure deployment architecture (resource group, Container Apps, Key Vault, networking)
- Add to Confluence under HORSCH F&E space

---

## Key People

| Person | Org | Role |
|--------|-----|------|
| **Hans Neidl** | HORSCH | Project sponsor |
| **Alex Kress** | HORSCH D-Lab | Technical lead, primary counterpart |
| **Matthias** | HORSCH F&E | Constructor/Setting Tech — test user |
| **Robert** | HORSCH F&E | Constructor/CAD Admin — test user |
| **Christoph Wiesent** | HORSCH | Jira/Confluence admin — involve for attachment search + integration |
| **Lisa** | Norizon | Co-founder, architecture & strategy |

---

## Open Questions

- Which Confluence spaces are in scope for F&E indexing?
- How do we surface contradictory information between Confluence and Jira to the user?
- Does HORSCH's Confluence Server/DC have the Office Connector plugin installed? (Determines attachment search path)
- When to formally involve Christoph Wiesent?
- Which CAD system does HORSCH use? (Never named in interviews)