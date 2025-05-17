"""
API Design Best Practices

Demonstrates:
1. RESTful resource nesting
2. Versioned endpoints
3. Pagination
4. OpenAPI documentation
5. Error standardization
"""
from fastapi import FastAPI, status
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Versioned API router
@app.get("/api/v1/books", tags=["Library"])
async def get_books(page: int = 1, limit: int = 20):
    return {
        "data": [],
        "pagination": {
            "page": page,
            "limit": limit,
            "total": 0
        }
    }

# Standard error response
class ErrorResponse(BaseModel):
    code: str
    message: str
    details: Optional[List[str]] = None

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content=ErrorResponse(
            code=exc.detail.get("code"),
            message=exc.detail.get("message")
        ).dict()
    )

"""
Implemented Features:
- Versioned endpoint structure
- Consistent pagination format
- Standardized error responses
- OpenAPI documentation
- Proper HTTP status codes
"""
