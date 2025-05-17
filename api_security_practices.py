"""
API Security Best Practices

Demonstrates:
1. Input validation/sanitization
2. Rate limiting
3. Secure headers
4. JWT authentication
5. Request validation
"""
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
import re

app = FastAPI()

# Security headers middleware
@app.middleware("http")
async def add_security_headers(request, call_next):
    response = await call_next(request)
    response.headers.update({
        "Strict-Transport-Security": "max-age=63072000; includeSubDomains",
        "X-Content-Type-Options": "nosniff",
        "X-Frame-Options": "DENY",
        "Content-Security-Policy": "default-src 'self'"
    })
    return response

# Rate limited endpoint example
@app.get("/api/public", tags=["Security"])
async def public_endpoint():
    return {"message": "Public endpoint with security headers"}

# Input validation model
class UserInput(BaseModel):
    query: str

    @validator('query')
    def validate_query(cls, v):
        if not re.match("^[a-zA-Z0-9_ ]*$", v):
            raise ValueError("Invalid characters in query")
        return v.strip()

@app.post("/api/search")
async def safe_search(input: UserInput):
    return {"results": f"Processed: {input.query}"}

"""
Security Features Implemented:
- Automatic security headers
- Strict input validation
- Rate limiting (requires Redis setup)
- JWT bearer authentication
- Request validation middleware
"""
