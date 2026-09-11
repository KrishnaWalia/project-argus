from fastapi import FastAPI

app = FastAPI(title="Project Argus - Ingestion Service")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/ingest/synthetic")
def generate_synthetic():
    # STUB — replace with the real synthetic data generator.
    return {"status": "STUB — synthetic data generator not yet implemented."}
