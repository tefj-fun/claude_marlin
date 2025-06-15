from fastapi import FastAPI
from .api import auth, detection, users

app = FastAPI(title="PPE Detection API")

app.include_router(auth.router, prefix="/auth")
app.include_router(detection.router, prefix="/detection")
app.include_router(users.router, prefix="/users")

@app.get("/")
async def root():
    return {"message": "PPE Detection API"}
