# AI/ML — Correlation Engine
Owner: AI/ML role. Port 8001. Receives Document objects, returns Evidence objects
(see ../shared/schemas/evidence.schema.json — the "details.summary" field must be
human-readable, frontend renders it directly).

A WORKING STUB ALREADY EXISTS (main.py) — GET /health and a stub POST /score/stylometric
that returns a fixed placeholder score. Replace the stub scoring logic with the real
function-word-frequency + Burrows' Delta implementation described in your role prompt.
Open-weight local models only — no paid LLM APIs. See ../CONVENTIONS.md.
