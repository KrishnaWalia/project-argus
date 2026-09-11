from fastapi import FastAPI
import json, os

app = FastAPI(title="Project Argus - Backend")

SAMPLE_DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "sample-data")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/api/v1/actor-nodes")
def get_actor_nodes():
    # STUB: reads the fixed sample fixture. Replace with real Neo4j-backed logic.
    with open(os.path.join(SAMPLE_DATA_DIR, "actor-nodes.json")) as f:
        return json.load(f)

@app.post("/load-fixture")
def load_fixture():
    # STUB for scripts/reset-demo.sh to call. Replace with real DB reset + reseed.
    return {"status": "fixture reload not yet implemented — backend role TODO"}
