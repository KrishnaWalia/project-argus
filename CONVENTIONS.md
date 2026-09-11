# Project Argus — Engineering Conventions

Read this before writing any code. If Claude suggests something that contradicts this
file, tell it to follow this file instead — this file is the ground truth, not Claude's
default preferences.

## Repo layout (fixed — do not restructure top-level folders)

```
project-argus/
├── docker-compose.yml       # fixed service topology — see CONVENTIONS.md before touching
├── .env.example             # the only env var names in use
├── shared/
│   └── schemas/             # canonical Document / Evidence / ActorNode schemas
│                            #   (JSON Schema — generate Pydantic models / TS types FROM these,
│                            #    don't hand-write duplicate type definitions elsewhere)
├── frontend/                 # Frontend/Dashboard role — nothing outside this folder
├── backend/                  # Backend & Orchestration role
├── ai-ml-service/             # AI/ML role
├── ingestion-service/          # Data Ingestion & External APIs role
├── database/
│   ├── neo4j/                 # Database role: schema/migration scripts
│   └── validation/            # Database role: the known-case validation harness
├── security/                  # Security & Compliance role: middleware, audit logging, docs
└── docs/
    └── pitch/                 # team lead: pitch materials, demo script
```

**Rule: work only inside your own top-level folder.** If you need something from another
role's folder, that's a signal to use the shared contract (schemas/ or the docker-compose
service URL), not to reach into their files directly.

## Naming conventions

- **Python code**: `snake_case` for variables/functions, `PascalCase` for classes,
  files as `snake_case.py`.
- **JS/TS code**: `camelCase` for variables/functions, `PascalCase` for components/classes,
  files as `kebab-case.tsx` or `camelCase.ts` (pick one per-folder and stay consistent —
  frontend role decides, others don't have much JS to worry about).
- **Folders/services**: `kebab-case` (matches docker-compose.yml service names exactly —
  `ai-ml-service`, not `ai_ml_service` or `AIMLService`).
- **Environment variables**: `ARGUS_SCREAMING_SNAKE_CASE`, always prefixed `ARGUS_`. Add
  new ones to `.env.example` in the same PR that introduces them.
- **REST endpoints**: `/api/v1/kebab-case-nouns`, plural for collections
  (e.g. `/api/v1/actor-nodes`, `/api/v1/actor-nodes/{actor_id}`).
- **Ports**: fixed in docker-compose.yml — frontend 3000, backend 8000, ai-ml-service 8001,
  ingestion-service 8002, neo4j 7474/7687, postgres 5432, opensearch 9200. Don't hardcode
  a different port "temporarily" — use the docker-compose values from the start.
- **Health checks**: every service (frontend, backend, ai-ml-service, ingestion-service)
  must expose `GET /health` returning `{"status": "ok"}` once it's actually ready to serve
  requests. This is the fastest way to answer "is the problem that a service is down, or
  that it's up and returning something wrong" during integration debugging — don't skip it
  even though it feels like a low-priority feature. `curl http://localhost:<port>/health`
  should be the first debugging step, every time, for every role.

## Shared fixtures — use these instead of inventing your own mock data

`sample-data/documents.json`, `evidence.json`, and `actor-nodes.json` are a small, fixed
dataset matching the schemas exactly — two aliases that are secretly the same actor
(shared wallet address + similar writing style) and one clearly different actor. Every
role should be able to build and test against this without any other service running:
- Frontend renders the graph from `actor-nodes.json` directly, before backend is ready.
- Backend loads `documents.json`/`evidence.json` as seed data for local dev.
- AI/ML can sanity-check that scoring the two documents in `documents.json` reproduces
  something close to the score in `evidence.json`.
- Database's validation harness and `scripts/reset-demo.sh` both load these same files —
  that's what makes the live demo reproducible instead of depending on whatever state
  happens to be sitting in the database that day.

This is separate from the Ingestion role's synthetic data generator, which produces
larger, more varied test volumes — `sample-data/` is the small, fixed, never-changes-
without-a-team-decision case everyone can rely on being identical.

## The schemas are the contract, not the JSON pasted into a prompt

Everyone should generate their language-specific types FROM `shared/schemas/*.json`
(e.g. `datamodel-code-generator` for Python Pydantic models, `json-schema-to-typescript`
for the frontend) rather than hand-typing a struct that matches "close enough." If the
schema needs to change, edit the file in `shared/schemas/` and tell the team — don't
silently diverge in your own service.

## Git workflow

- `main` is protected — no direct pushes.
- Branch naming: `feature/<role>-<short-description>` (e.g. `feature/ai-ml-stylometry-scoring`).
- Open a PR into `main`; team lead reviews for contract compliance (does it match the
  schemas / docker-compose topology) before merging — not a full code review, just an
  integration-compatibility check.
- Before pushing, run `docker compose up` locally and confirm your service still starts
  cleanly alongside the others — this is the cheapest integration test available and
  catches most cross-role breakage before it reaches `main`.

## Daily workflow (do this every session, not just once — this is what actually prevents drift)

**Start of every session:**
1. `git pull origin main` — before opening Claude, before writing anything. If you're
   using a regular Claude.ai chat (not Claude Code), re-upload/re-paste the current
   contents of `shared/schemas/`, `docker-compose.yml`, and `.env.example` even if you
   uploaded them yesterday — an uploaded file in a chat is a frozen snapshot, it does not
   update when someone else pushes a change. If you have **Claude Code** available
   (terminal/VS Code/desktop), use it instead and point it at your actual cloned repo
   folder — it reads the live filesystem, so `git pull` is enough and there's no
   re-upload step to forget.
2. Tell Claude explicitly, every session: **"Do not modify anything in `shared/schemas/`,
   `docker-compose.yml`, or `.env.example` without telling me first — flag it, don't just
   do it."** These five files are the only thing holding six independent builds together;
   a "helpful" one-line schema tweak made to unblock your own task silently breaks
   everyone else's.

**End of every session:**
1. Run `docker compose up` (or at minimum, restart your own service against the current
   compose file) and confirm it still starts cleanly — this catches most cross-role
   breakage before it leaves your machine.
2. Commit, push to your feature branch, open a PR into `main`.
3. If you touched anything in `shared/` — stop, flag it to the team lead in whatever
   channel you use, and get explicit agreement before merging. A silent shared-file change
   is the single most common way this kind of project breaks.

**Optional but cheap:** add a GitHub Action that runs `docker compose config` (validates
the YAML, not a full build) on every PR — catches typo-level breakage automatically
instead of relying on someone remembering to test locally.

## The one thing to paste into every Claude conversation

When you open Claude for your role, paste your role prompt AND tell Claude:
"Here is the fixed repo structure, docker-compose.yml, and CONVENTIONS.md for the project
— work within this structure, use these exact ports/env-var names/schemas, and don't
propose a different top-level layout." Then paste the relevant files. Claude will fill in
the *implementation* — the structure should already be decided before Claude sees it.
