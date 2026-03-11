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
- **Infrastructure:** Isolated backend on **Norizon's Azure** (same codebase as Service Q&A, different config/data/users)
- **Test users:** Matthias (Construction/Setting Tech) and Robert (CAD Admin) — ~1h every 2 weeks

### Must-Have Requirements (from stakeholder interviews)
- Natural language queries — typo-tolerant, word order doesn't matter
- Clickable source links back to Confluence pages / Jira tickets
- Compact answers first, drill deeper on follow-up
- Search PDFs and file attachments, not just Confluence page text
- Confluence AND Jira searchable in one interface

---

## Current State

A **live deployed version already exists** on Norizon's Azure. HORSCH's team has seen and demoed it. Based on that demo, they came back with two change requests.

---

## Progress Log

### Frontend Modernisation + Svelte 5 Migration — DONE (March 2026)
- **Svelte 5 migration complete** — all components use runes API (`$props()`, `$state()`, `$derived()`, `$effect()`, `untrack()`, `{@render}`, `onclick`)
- **UI redesigned** to ChatGPT/Claude aesthetic — centered conversation rail, clean white backgrounds, inline sources
- **Chat UI**: message bubbles, 17px base font, Nora avatar (favicon.png, transparent bg), greeting with user name
- **Sidebar**: collapsible, session history with type icons (magnifying glass = search, document = meeting), context menus (rename/pin/delete), delete confirmation dialog
- **Meeting documentation workflow**: full pipeline working (upload → processing → speaker verification → template review → export), all buttons functional with `$state()` reactivity fixes
- **Confirmation dialogs**: consistent flat card design across all components (matching Sidebar style)
- **Delete flow**: deleting current open chat navigates back to homepage
- **Global zoom**: `body { zoom: 1.08 }` in app.css for comfortable sizing
- **Docker Compose**: full local stack running (frontend, deepsearch, searxng, workflow-service, deepgram-service, postgres, redis, minio, confluence-mcp, confluence-publisher)
- **Svelte 4 stores** (`writable`/`derived` in `svelte/store`) still used in store files — not yet migrated to `.svelte.ts` runes. Works fine, just not fully Svelte 5 idiomatic.

### Auth0 → Azure Authentication — IN PROGRESS
- Current auth: Auth0 SPA SDK (`@auth0/auth0-spa-js`) in frontend, Auth0 JWT verification in workflow-service backend
- Next: Replace with MSAL.js (frontend) + Azure AD JWT verification (backend)

---

## Immediate Work (Do These First)

These are prerequisites — get the platform into shape locally before redeploying.

> ⚠️ **Work locally first using Docker.** Validate everything works end-to-end in the local Docker environment before redeploying to Azure. Do not touch the Azure deployment until local is confirmed working.

### 1. Frontend Modernisation + Svelte 4 → 5 Migration — COMPLETE
- ~~Redesign the UI to feel like a modern chat agent (think ChatGPT/Claude style)~~
- ~~Migrate the frontend from **Svelte 4 to Svelte 5**~~
- ~~Test locally via Docker Compose before any deployment~~

### 2. Auth0 → Azure Authentication — NEXT
- The current deployment uses **Auth0** (built by Omar originally)
- Replace with **Azure-native auth** (Azure Entra ID / Azure AD)
- Rationale: everything already runs on Azure; removes third-party auth dependency; cleaner for enterprise client
- Implement and verify locally first, then redeploy

---

## Next Steps After Auth + Frontend

From the Implementation Proposal (page 27983873 — read it in full):

### Step 1 — Build JiraAgent
Mirror the existing `ConfluenceMCPAgent` pattern. The `mcp-atlassian` package (already in Dockerfile) supports Jira via `jira_search` (JQL) and `jira_get_issue`.

Key files to create:
- `services/custom-deepresearch/deepsearch/agents/mcp_utils.py` — shared MCP helper (extract from confluence/tools.py)
- `services/custom-deepresearch/deepsearch/agents/jira/tools.py` — JiraSearchTool + JiraGetIssueTool
- `services/custom-deepresearch/deepsearch/agents/jira/agent.py` — JiraMCPAgent
- `services/custom-deepresearch/deepsearch/agents/jira/__init__.py` — factory registration
- `services/custom-deepresearch/prompts/jira_agent.yaml` — JQL strategies, bilingual DE/EN
- Edit `main.py:35` — add jira import

### Step 2 — Enable Jira in MCP Container
Add Jira env vars to docker-compose. HORSCH uses **Server/Data Center** → use `JIRA_PERSONAL_TOKEN`, not email+API key.

### Step 3 — Attachment Search (Quick Win)
Add CQL strategies to Confluence agent prompt:
```
type = attachment AND text ~ "keyword"
type = attachment AND space = "FUE" AND text ~ "keyword"
(type = page OR type = attachment) AND text ~ "keyword"
```
Handle `type == "attachment"` in `ConfluenceSearchTool._page_to_search_result()` to include parent page metadata.

### Step 4 — HORSCH F&E Instantiation
Create `instantiations/horsch_fue/` with:
- `agents.yaml` — horsch_confluence + horsch_jira, web_search disabled
- `.env.example` — CONFLUENCE_URL, CONFLUENCE_PERSONAL_TOKEN, JIRA_URL, JIRA_PERSONAL_TOKEN
- `docker-compose.yml` — 3 services: atlassian-mcp, deepsearch, frontend

### Step 5 — Azure Deployment
Only after local Docker validation. Adapt `instantiations/internal_setup/azure/` — reduce to 3 Container Apps, add Jira secrets to Key Vault.

---

## Key People

| Person | Org | Role |
|--------|-----|------|
| **Hans Neidl** | HORSCH | Project sponsor |
| **Alex Kress** | HORSCH D-Lab | Technical lead, primary counterpart |
| **Matthias** | HORSCH F&E | Constructor/Setting Tech — test user |
| **Robert** | HORSCH F&E | Constructor/CAD Admin — test user |
| **Christoph Wiesent** | HORSCH | Jira/Confluence admin — involve as needed |
| **Lisa** | Norizon | Stakeholder interviews, consultant |

---

## Open Questions

- Which Confluence spaces are in scope for F&E indexing?
- How do we surface contradictory data in search results to the user?
- When to involve Christoph Wiesent for Jira/Confluence technical integration?
- Which CAD system does HORSCH use? (Never named in interviews)