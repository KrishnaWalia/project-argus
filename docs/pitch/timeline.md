# Build Timeline (adjust hours to your actual hackathon window)

Generic 3-phase structure — fit your real hackathon duration into these phases rather
than skipping straight to Phase 3. The point isn't the exact hours, it's having a shared
checkpoint everyone is accountable to.

## Phase 1 — Scaffolding (do this before writing real logic)
- Repo skeleton exists, everyone has cloned it, `docker compose up` starts all stub
  services successfully (even if they don't do anything real yet).
- Every service responds on `GET /health`.
- Frontend renders the graph view against `sample-data/` (not live backend data yet).
- **Checkpoint: can the whole stack start together, even doing nothing useful?** If no,
  do not move to Phase 2 — fix this first, it only gets more expensive to fix later.

## Phase 2 — Core logic, in parallel
- AI/ML: stylometric scoring working and validated against the Federalist Papers case.
- Ingestion: synthetic data generator producing realistic Document objects.
- Backend: real aggregation of Evidence into ActorNodes, served via the real API.
- Database: Neo4j/Postgres schema live, validation harness runnable.
- Security: access control + audit logging wired into backend; defensibility paragraphs drafted.
- Frontend: graph view + explainability panel working against real (not mock) backend data.
- **Checkpoint: run `scripts/reset-demo.sh`, then walk through the full pipeline once,
  end to end, with real (not mock) data.** Fix whatever breaks before adding new features.

## Phase 3 — Demo hardening (do not skip this for "one more feature")
- Run the full demo script (see `demo-script.md`) at least twice, start to finish, exactly
  as you'll present it.
- Confirm `scripts/reset-demo.sh` actually produces a clean, repeatable state both times.
- Freeze new feature work. Remaining time goes to: fixing anything that broke during
  rehearsal, tightening the pitch narrative, preparing answers to the hard judge
  questions (see `demo-script.md`).
- **Checkpoint: could a teammate who wasn't in the room run the demo from the reset
  script alone and get the same result you do?** If no, that's your last bug to fix.
