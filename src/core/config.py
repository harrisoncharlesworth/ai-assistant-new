from typing import List

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """Application settings."""
    
    # Project info
    PROJECT_NAME: str = "AI Assistant"
    VERSION: str = "1.0.0"
    DESCRIPTION: str = "Modern AI assistant with multi-model support and real-time capabilities"
    
    # API Configuration
    API_V1_STR: str = "/api/v1"
    CORS_ORIGINS: List[str] = ["*"]
    
    # Security
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    ALGORITHM: str = "HS256"
    
    # Database
    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    DATABASE_URL: str | None = None
    
    # Redis
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    
    # AI Models
    OPENAI_API_KEY: str
    ANTHROPIC_API_KEY: str | None = None
    DEFAULT_MODEL: str = "gpt-4"
    
    # Monitoring
    SENTRY_DSN: str | None = None
    ENVIRONMENT: str = "development"
    
    model_config = SettingsConfigDict(env_file=".env", case_sensitive=True)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if not self.DATABASE_URL:
            self.DATABASE_URL = (
                f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
                f"@{self.POSTGRES_SERVER}/{self.POSTGRES_DB}"
            )

settings = Settings() 