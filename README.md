# Project Argus — Team Shadow Knights (SIH26151)

Multi-signal de-anonymization framework for dark web threat actors — fuses stylometric
writing analysis, PGP/wallet-reuse detection, and username correlation into a
confidence-scored actor graph, for investigator lead generation (not automated
accusation). Passive-OSINT, open-source only. See `CONVENTIONS.md` for how this repo
is organized and the rules that keep six people's work compatible.

## Quickstart

```bash
git clone <this repo>
cd project-argus
cp .env.example .env        # fill in local dev passwords
docker compose up
```

Every service exposes `GET /health` — check `curl http://localhost:<port>/health` if
something isn't behaving, before digging further.

## Repo map

- `docker-compose.yml` — fixed service topology (ports, hostnames, env vars). Read before touching.
- `shared/schemas/` — the Document / Evidence / ActorNode contract. Source of truth.
- `sample-data/` — a small, fixed demo dataset matching the schema. Use this instead of
  inventing your own mock data — it's what the frontend demo scenario and the reset
  script both load, and it means you can build and test your piece without any other
  service running.
- `scripts/reset-demo.sh` — wipes state and reloads `sample-data/` for a clean pitch run.
- `frontend/`, `backend/`, `ai-ml-service/`, `ingestion-service/`, `database/`, `security/`
  — one folder per role. Work only inside your own.
- `docs/pitch/` — demo script, timeline, judge Q&A prep.

## Before you write any code

Read `CONVENTIONS.md`. It has the naming rules, git workflow, and the daily
pull/sync discipline that keeps six independent builds from drifting apart.
