from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/health/live")
def liveness():
    """Kubernetes liveness probe - il container è vivo?"""
    return {"status": "ok"}

@app.get("/health/ready")
def readiness():
    """Kubernetes readiness probe - pronto a ricevere traffico?"""
    # qui puoi controllare DB, dipendenze esterne, ecc.
    return {"status": "ok"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}