# Frontend / Dashboard
Owner: Frontend role. Port 3000. Talks only to `backend` (http://localhost:8000).
Do not talk to neo4j/postgres/ai-ml-service/ingestion-service directly — always through backend's API.

A MINIMAL STUB ALREADY EXISTS (server.js + public/index.html, plain Express) — GET /health
and a static placeholder page. This is intentionally bare-bones; replace it with a real
React/Vite app (or whatever the role prompt agrees is fastest) that renders
sample-data/actor-nodes.json as a graph. Update package.json/Dockerfile accordingly if you
change the framework — just keep it listening on port 3000 with /health intact.
See ../CONVENTIONS.md and ../shared/schemas/ before writing code.
