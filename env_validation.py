"""
Advanced Environment Validation

Demonstrates:
1. Multi-environment config validation
2. Secret management
3. Type-safe settings
"""
from pydantic import BaseModel, Field, validator
from typing import Literal
import os

class EnvironmentConfig(BaseModel):
    app_env: Literal['development', 'staging', 'production']
    db_host: str
    db_port: int = 5432
    db_use_ssl: bool = False
    feature_cache: bool
    jwt_secret: str = Field(min_length=32)

    @validator('jwt_secret')
    def validate_jwt_secret(cls, v):
        if len(v) < 32:
            raise ValueError('JWT secret must be at least 32 characters')
        return v

class ConfigLoader:
    @staticmethod
    def from_env() -> EnvironmentConfig:
        return EnvironmentConfig(
            app_env=os.getenv('APP_ENV', 'development'),
            db_host=os.getenv('DB_HOST'),
            db_port=int(os.getenv('DB_PORT', '5432')),
            db_use_ssl=os.getenv('DB_USE_SSL', 'false').lower() == 'true',
            feature_cache=os.getenv('FEATURE_CACHE_LAYER', 'false').lower() == 'true',
            jwt_secret=os.getenv('JWT_SECRET', '')
        )

# Usage example
if __name__ == "__main__":
    try:
        config = ConfigLoader.from_env()
        print(f"Valid configuration loaded for {config.app_env}")
    except Exception as e:
        print(f"Configuration error: {str(e)}")
