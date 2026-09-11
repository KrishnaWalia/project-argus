from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Project Argus - AI/ML Correlation Engine")

class ScoreRequest(BaseModel):
    text_a: str
    text_b: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/score/stylometric")
def score_stylometric(req: ScoreRequest):
    # STUB — replace with real function-word frequency + Burrows' Delta implementation.
    # See the team prompt doc's AI/ML role for the actual method to implement.
    return {
        "type": "stylometric",
        "score": 0.5,
        "details": {"summary": "STUB response — real stylometric scoring not yet implemented."}
    }
