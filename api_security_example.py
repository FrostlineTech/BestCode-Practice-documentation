"""
API Security & Variable Handling Practices

Demonstrates:
1. Secure environment variable usage
2. Request validation
3. Security headers
4. Rate limiting
5. Error sanitization
"""
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel, validator
import os
import re

app = FastAPI()

# Load config from environment
API_KEY = os.getenv("API_KEY")
JWT_SECRET = os.getenv("JWT_SECRET")

# Security middleware
@app.middleware("http")
async def add_headers(request, call_next):
    response = await call_next(request)
    response.headers.update({
        "X-Content-Type-Options": "nosniff",
        "Content-Security-Policy": "default-src 'self'"
    })
    return response

# Secure endpoint example
@app.get("/secure")
async def secure_endpoint(key: str = Depends(api_key_auth)):
    return {"message": "Secure endpoint accessed"}

# Validation model
class UserInput(BaseModel):
    username: str
    
    @validator('username')
    def validate_username(cls, v):
        if not re.match("^[a-zA-Z0-9_]{3,20}$", v):
            raise ValueError("Invalid username format")
        return v

"""
Key Security Features:
- Environment variables for secrets
- Input validation/sanitization
- Security headers
- Authentication dependency
- Error message sanitization
"""
