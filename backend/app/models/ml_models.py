from sqlalchemy import Column, Integer, String, Float, DateTime, Text, Boolean, ForeignKey, Enum, JSON
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
import enum

from app.core.database import Base


class ModelType(enum.Enum):
    DEMAND_FORECASTING = "demand_forecasting"
    PRICE_PREDICTION = "price_prediction"
    SUPPLIER_RISK = "supplier_risk"
    ANOMALY_DETECTION = "anomaly_detection"
    RECOMMENDATION = "recommendation"
    OPTIMIZATION = "optimization"


class ModelStatus(enum.Enum):
    TRAINING = "training"
    READY = "ready"
    DEPLOYED = "deployed"
    DEPRECATED = "deprecated"
    FAILED = "failed"


class MLModel(Base):
    __tablename__ = "ml_models"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, index=True)
    version = Column(String(50), nullable=False)
    model_type = Column(Enum(ModelType), nullable=False)
    
    # Model Information
    description = Column(Text)
    algorithm = Column(String(100))  # LSTM, XGBoost, Random Forest, etc.
    
    # Performance Metrics
    accuracy = Column(Float)
    precision = Column(Float)
    recall = Column(Float)
    f1_score = Column(Float)
    mse = Column(Float)
    mae = Column(Float)
    r2_score = Column(Float)
    
    # Training Information
    training_data_path = Column(String(500))
    training_date = Column(DateTime(timezone=True))
    training_duration = Column(Float)  # in seconds
    training_parameters = Column(JSON)
    
    # Model Metadata
    features = Column(JSON)  # List of feature names
    target_variable = Column(String(100))
    feature_importance = Column(JSON)
    
    # Deployment Information
    status = Column(Enum(ModelStatus), default=ModelStatus.TRAINING)
    deployment_date = Column(DateTime(timezone=True))
    endpoint_url = Column(String(500))
    
    # MLflow Information
    mlflow_run_id = Column(String(100))
    mlflow_experiment_id = Column(String(100))
    
    # Model File Information
    model_path = Column(String(500))
    model_size = Column(Integer)  # in bytes
    
    # Validation Information
    validation_score = Column(Float)
    cross_validation_scores = Column(JSON)
    
    # Usage Statistics
    prediction_count = Column(Integer, default=0)
    last_used = Column(DateTime(timezone=True))
    
    # Configuration
    prediction_threshold = Column(Float)
    confidence_threshold = Column(Float)
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    
    # Relationships
    predictions = relationship("ModelPrediction", back_populates="model")
    feature_importance_records = relationship("ModelFeatureImportance", back_populates="model")
    
    def __repr__(self):
        return f"<MLModel(id={self.id}, name={self.name}, type={self.model_type}, status={self.status})>"


class ModelPrediction(Base):
    __tablename__ = "model_predictions"
    
    id = Column(Integer, primary_key=True, index=True)
    model_id = Column(Integer, ForeignKey("ml_models.id"), nullable=False)
    
    # Prediction Details
    input_data = Column(JSON)  # Input features
    prediction = Column(JSON)  # Prediction output
    confidence_score = Column(Float)
    
    # Context Information
    entity_type = Column(String(100))  # supplier, product, etc.
    entity_id = Column(Integer)  # ID of the entity
    prediction_type = Column(String(100))  # risk_score, demand_forecast, etc.
    
    # Explainability
    shap_values = Column(JSON)
    feature_contributions = Column(JSON)
    explanation_text = Column(Text)
    
    # Performance
    prediction_time = Column(Float)  # Time taken for prediction in ms
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    
    # Relationships
    model = relationship("MLModel", back_populates="predictions")
    
    def __repr__(self):
        return f"<ModelPrediction(id={self.id}, model_id={self.model_id}, confidence={self.confidence_score})>"


class ModelFeatureImportance(Base):
    __tablename__ = "model_feature_importance"
    
    id = Column(Integer, primary_key=True, index=True)
    model_id = Column(Integer, ForeignKey("ml_models.id"), nullable=False)
    
    # Feature Information
    feature_name = Column(String(255), nullable=False)
    importance_score = Column(Float, nullable=False)
    importance_type = Column(String(50))  # shap, permutation, gain, etc.
    
    # Additional Metrics
    feature_value = Column(Float)
    feature_contribution = Column(Float)
    
    # Context
    prediction_id = Column(Integer, ForeignKey("model_predictions.id"))
    entity_type = Column(String(100))
    entity_id = Column(Integer)
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    
    # Relationships
    model = relationship("MLModel", back_populates="feature_importance_records")
    
    def __repr__(self):
        return f"<ModelFeatureImportance(id={self.id}, feature={self.feature_name}, importance={self.importance_score})>"
