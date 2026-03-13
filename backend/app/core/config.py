from pydantic_settings import BaseSettings
from typing import List, Optional
import secrets


class Settings(BaseSettings):
    # Project
    PROJECT_NAME: str = "Smart Procurement Platform"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    
    # Security
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # 8 days
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 30  # 30 days
    ALGORITHM: str = "HS256"
    
    # CORS
    ALLOWED_HOSTS: List[str] = ["*"]
    
    # Database
    DATABASE_URL: str = "postgresql://procurement_user:procurement_pass@localhost:5432/procurement_db"
    
    # Redis
    REDIS_URL: str = "redis://localhost:6379"
    
    # Kafka
    KAFKA_BOOTSTRAP_SERVERS: str = "localhost:9092"
    
    # MLOps
    MLFLOW_TRACKING_URI: str = "http://localhost:5000"
    MODEL_REGISTRY_PATH: str = "./models"
    
    # External Services
    DEMAND_FORECASTING_SERVICE_URL: str = "http://localhost:8001"
    PRICE_PREDICTION_SERVICE_URL: str = "http://localhost:8002"
    SUPPLIER_RISK_SERVICE_URL: str = "http://localhost:8003"
    ANOMALY_DETECTION_SERVICE_URL: str = "http://localhost:8004"
    RECOMMENDATIONS_SERVICE_URL: str = "http://localhost:8005"
    OPTIMIZATION_SERVICE_URL: str = "http://localhost:8006"
    
    # Pagination
    DEFAULT_PAGE_SIZE: int = 20
    MAX_PAGE_SIZE: int = 100
    
    # File Upload
    MAX_UPLOAD_SIZE: int = 10 * 1024 * 1024  # 10MB
    ALLOWED_UPLOAD_EXTENSIONS: List[str] = [".csv", ".xlsx", ".json"]
    
    # Logging
    LOG_LEVEL: str = "INFO"
    LOG_FORMAT: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    
    # Background Tasks
    CELERY_BROKER_URL: str = "redis://localhost:6379/0"
    CELERY_RESULT_BACKEND: str = "redis://localhost:6379/0"
    
    # Monitoring
    PROMETHEUS_ENABLED: bool = True
    METRICS_PORT: int = 9090
    
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
