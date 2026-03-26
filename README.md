# AI-Driven-Smart-Procurement-Spend-Optimization
Mini project for academic submission: AI-Driven Smart Procurement &amp; Spend Optimization Intelligence Platform
# 
# 01/03/2026   in Synopsis i add information about my project and team members

# AI-Driven Smart Procurement & Spend Optimization Intelligence Platform

A production-grade AI-driven procurement platform built with open-source technologies for final-year engineering capstone project.

## 🎯 Problem Statement

Organizations lose millions due to:
- Poor supplier selection
- Price volatility  
- Maverick spending
- Lack of forecasting
- Reactive sourcing

## 🧠 Core Features

- **Smart Spend Analyzer**: Category trends, leakage detection, duplicate invoices
- **Vendor Intelligence**: Scorecards, risk profiles, historical performance
- **Savings Opportunity Engine**: Price variance analysis, contract consolidation
- **Negotiation Simulator**: Scenario comparison, counter-offer impact
- **Scenario Planning**: Supplier drop, demand spike, price shock
- **Explainable AI**: SHAP plots, feature importance

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Frontend      │    │   Backend       │    │   ML Services   │
│   React +       │◄──►│   FastAPI +     │◄──►│   PyTorch +     │
│   TailwindCSS   │    │   SQLAlchemy    │    │   Scikit-learn  │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         └───────────────────────┼───────────────────────┘
                                 │
                    ┌─────────────────┐
                    │   PostgreSQL    │
                    │   + DuckDB      │
                    └─────────────────┘
```

## 🛠️ Tech Stack

### Backend
- **FastAPI**: High-performance API framework
- **SQLAlchemy**: ORM for database operations
- **Pydantic**: Data validation and serialization
- **PostgreSQL**: Primary database
- **DuckDB**: Analytics and data warehousing

### ML Stack
- **Python**: Core ML language
- **PyTorch**: Deep learning framework
- **Scikit-learn**: Traditional ML algorithms
- **XGBoost/LightGBM**: Gradient boosting
- **Prophet**: Time series forecasting
- **SHAP/LIME**: Model explainability

### Frontend
- **React**: Modern UI framework
- **TailwindCSS**: Utility-first CSS
- **Recharts/ECharts**: Data visualization

### MLOps
- **MLflow**: Model lifecycle management
- **DVC**: Data version control
- **Docker**: Containerization

### Optimization
- **Google OR-Tools**: Mathematical optimization
- **PuLP**: Linear programming

## 📁 Project Structure

```
smart-procurement-platform/
├── backend/                 # FastAPI application
│   ├── app/
│   │   ├── api/            # API endpoints
│   │   ├── core/           # Configuration
│   │   ├── models/         # Database models
│   │   ├── schemas/        # Pydantic schemas
│   │   └── services/       # Business logic
│   ├── requirements.txt
│   └── Dockerfile
├── ml-services/            # ML pipeline services
│   ├── demand_forecasting/
│   ├── price_prediction/
│   ├── supplier_risk/
│   ├── anomaly_detection/
│   ├── recommendations/
│   └── optimization/
├── frontend/               # React application
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── hooks/
│   │   └── utils/
│   ├── package.json
│   └── Dockerfile
├── data/                   # Sample datasets
├── pipelines/              # Data processing pipelines
├── docker/                 # Docker configurations
├── notebooks/              # Jupyter notebooks
├── docs/                   # Documentation
└── docker-compose.yml      # Development environment
```

## 🚀 Quick Start

### Prerequisites
- Docker and Docker Compose
- Python 3.9+
- Node.js 16+

### Development Setup

1. **Clone and setup**:
```bash
git clone <repository>
cd smart-procurement-platform
```

2. **Start development environment**:
```bash
docker-compose up -d
```

3. **Access services**:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs
- MLflow: http://localhost:5000

## 🧪 ML Modules

### Demand Forecasting
- **LSTM**: Deep learning for complex patterns
- **Prophet**: Facebook's time series forecasting
- **XGBoost**: Gradient boosting for structured data

### Price Prediction
- **Random Forest**: Ensemble method for price trends
- **LightGBM**: Fast gradient boosting

### Supplier Risk Assessment
- **Logistic Regression**: Risk classification
- **XGBoost**: Complex risk patterns

### Anomaly Detection
- **Isolation Forest**: Outlier detection
- **Autoencoder**: Unsupervised anomaly detection

### Recommendation Engine
- **Matrix Factorization**: Collaborative filtering
- **Content-Based Filtering**: Feature-based recommendations

### Optimization Engine
- **Linear Programming**: Cost optimization
- **Genetic Algorithm**: Complex multi-objective optimization

## 📊 Data Models

### Core Entities
- **Suppliers**: Vendor information and performance
- **Products**: Catalog items and specifications
- **Purchase Orders**: Transaction records
- **Invoices**: Billing and payment data
- **Contracts**: Agreements and terms
- **Users**: System users and roles

## 🔧 Configuration

### Environment Variables
```bash
# Database
DATABASE_URL=postgresql://user:password@localhost:5432/procurement

# ML Services
MLFLOW_TRACKING_URI=http://localhost:5000
MODEL_REGISTRY_PATH=./models

# Security
SECRET_KEY=your-secret-key
JWT_ALGORITHM=HS256
```

## 🧪 Testing

```bash
# Backend tests
cd backend && pytest

# Frontend tests
cd frontend && npm test

# ML model validation
cd ml-services && python -m pytest
```

## 📈 Monitoring & MLOps

- **MLflow**: Model tracking and registry
- **DVC**: Data versioning and pipeline tracking
- **Prometheus**: Metrics collection
- **Grafana**: Visualization dashboards

## 📚 Documentation

- [Architecture Guide](docs/architecture.md)
- [API Documentation](docs/api.md)
- [ML Models](docs/models.md)
- [Deployment Guide](docs/deployment.md)
- [User Manual](docs/user-guide.md)

## 🤝 Contributing

1. Fork the repository
2. Create feature branch
3. Make changes with tests
4. Submit pull request

## 📄 License

MIT License - see LICENSE file for details

## 🎓 Academic Use

This project is designed as a engineering capstone demonstrating:
- Real business impact
- End-to-end architecture
- Advanced ML pipelines
- Optimization algorithms
- Explainability
- MLOps practices
- Scalable design
- Security considerations
