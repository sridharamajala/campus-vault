from fastapi import FastAPI

# Initialize the core Campus Vault API server engine
app = FastAPI(title="Campus Vault")

@app.get("/")
def health_check():
    """
    Root API health check indicator route.
    Confirms that our Python backend is running smoothly.
    """
    return {"status": "online", "system": "Campus Vault Server"}
