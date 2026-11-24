"""The FastAPI application: every HTTP endpoint is registered on `app`.

Run locally from the backend/ folder:
    uvicorn app.main:app --reload
"""

from fastapi import FastAPI

app = FastAPI(title="Accessible Sidewalk Map", version="0.1.0")


@app.get("/health")
def health() -> dict[str, str]:
    """Answers "is the server alive?" for deploy scripts and uptime checks."""
    return {"status": "UP"}
