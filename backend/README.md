# Backend & Orchestration
Owner: Backend role. Port 8000. Talks to neo4j, postgres, ai-ml-service, ingestion-service.
Serves ActorNode/Evidence data to frontend in the shape defined by ../shared/schemas/.

A WORKING STUB ALREADY EXISTS (main.py) — GET /health and GET /api/v1/actor-nodes
(serving sample-data/actor-nodes.json). `docker compose up` should bring this up
successfully on day one. Build your real logic on top of this, don't start from scratch —
replace the stubbed parts (fixture-reading, /load-fixture) with real Neo4j-backed logic.
See ../CONVENTIONS.md before writing code.
