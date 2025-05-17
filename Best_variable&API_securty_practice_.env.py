"""
Secure Configuration Handling Example

Demonstrates:
1. Environment variable loading
2. Configuration validation
3. Type hinting
4. Error handling
5. Documentation best practices
"""
from typing import Optional
import os
from pydantic import BaseModel, ValidationError
import logging

# Configure logging first
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class AppConfig(BaseModel):
    """Application configuration model validating environment variables"""
    db_host: str
    db_port: int
    db_name: str
    db_user: str
    db_password: str
    api_key: Optional[str] = None
    debug: bool = False
    max_file_size_mb: int = 10

    @classmethod
    def from_env(cls):
        """Load configuration from environment variables"""
        try:
            return cls(
                db_host=os.getenv('DB_HOST'),
                db_port=int(os.getenv('DB_PORT', '5432')),
                db_name=os.getenv('DB_NAME'),
                db_user=os.getenv('DB_USER'),
                db_password=os.getenv('DB_PASSWORD'),
                api_key=os.getenv('API_KEY'),
                debug=os.getenv('DEBUG', 'False').lower() == 'true',
                max_file_size_mb=int(os.getenv('MAX_FILE_SIZE_MB', '10'))
            )
        except ValidationError as e:
            logger.error("Invalid configuration: %s", e)
            raise


def main():
    """Main application entry point"""
    try:
        config = AppConfig.from_env()
        logger.info("Successfully loaded configuration")
        # Application logic would continue here...
    except Exception as e:
        logger.error("Failed to start application: %s", e)


if __name__ == "__main__":
    main()
