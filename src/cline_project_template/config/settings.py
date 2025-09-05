"""
Application settings loader.
"""

from pydantic import AnyUrl, Field
from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    """
    Application settings loaded from environment variables or .env files.

    Attributes:
        env: Environment name (dev, test, prod).
        api_base: Base URL for the API.
        retry_limit: Max number of retries for operations.
        feature_x_enabled: Feature flag for experimental feature X.
    """

    env: str = Field(default="dev")
    api_base: AnyUrl
    retry_limit: int = Field(default=3, ge=0, le=10)
    feature_x_enabled: bool = False

    class Config:
        env_prefix = "APP_"
        case_sensitive = False
