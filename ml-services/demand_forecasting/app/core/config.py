from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    # Service Configuration
    SERVICE_NAME: str = "Demand Forecasting Service"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    
    # Database
    DATABASE_URL: str = "postgresql://procurement_user:procurement_pass@localhost:5432/procurement_db"
    
    # MLOps
    MLFLOW_TRACKING_URI: str = "http://localhost:5000"
    MODEL_REGISTRY_PATH: str = "./models"
    
    # Model Configuration
    DEFAULT_FORECAST_HORIZON: int = 90  # days
    MAX_FORECAST_HORIZON: int = 365  # days
    MODEL_RETRAIN_INTERVAL: int = 7  # days
    
    # Logging
    LOG_LEVEL: str = "INFO"
    LOG_FORMAT: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    
    # Performance
    MAX_WORKERS: int = 4
    REQUEST_TIMEOUT: int = 30  # seconds
    
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
