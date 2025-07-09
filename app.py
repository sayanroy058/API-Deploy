from g4f.api import run_api
import os
from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse

API_KEY = "ghioipuygfhvbjyut78976r5tdfghvcxders45r6t7y8"

app = run_api()

@app.middleware("http")
async def verify_api_key(request: Request, call_next):
    auth_header = request.headers.get("Authorization")
    if auth_header != f"Bearer {API_KEY}":
        raise HTTPException(status_code=401, detail="Unauthorized")
    response = await call_next(request)
    return response
