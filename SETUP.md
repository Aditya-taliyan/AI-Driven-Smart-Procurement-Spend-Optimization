# Smart Procurement Platform - Setup Guide

## 🚀 Quick Start

### Prerequisites
- Docker and Docker Compose
- Node.js 16+ (for frontend development)
- Python 3.9+ (for backend development)
- Git

### 1. Clone and Setup
```bash
git clone <repository-url>
cd smart-procurement-platform
cp.env.example .env
```

### 2. Environment Configuration
```bash
# Copy environment templates
cp .env.example .env
# Edit .env with your configuration
```

### 3. Start Development Environment
```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

### 4. Access Services
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs
- **MLflow**: http://localhost:5000
- **Jupyter Notebook**: http://localhost:8888

## 🏗️ Architecture Overview

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

## 📊 ML Services

### Demand Forecasting (Port 8001)
- LSTM for complex patterns
- Prophet for time series
- XGBoost for structured data

### Price Prediction (Port 8002)
- Random Forest
- LightGBM

### Supplier Risk (Port 8003)
- Logistic Regression
- XGBoost

### Anomaly Detection (Port 8004)
- Isolation Forest
- Autoencoder

### Recommendations (Port 8005)
- Matrix Factorization
- Content-Based Filtering

### Optimization (Port 8006)
- Linear Programming
- Genetic Algorithm

## 🔧 Development

### Backend Development
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend Development
```bash
cd frontend
npm install
npm start
```

### ML Service Development
```bash
cd ml-services/demand_forecasting
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8001
```

## 🧪 Testing

### Backend Tests
```bash
cd backend
pytest
```

### Frontend Tests
```bash
cd frontend
npm test
```

### ML Model Tests
```bash
cd ml-services
python -m pytest
```

## 📈 Monitoring

### Application Logs
```bash
# View all logs
docker-compose logs

# View specific service logs
docker-compose logs backend
docker-compose logs frontend
```

### MLflow Tracking
- Access at http://localhost:5000
- Track experiments, models, and performance

### Database Access
```bash
# Connect to PostgreSQL
docker-compose exec postgres psql -U procurement_user -d procurement_db
```

## 🔒 Security

### Environment Variables
- Never commit `.env` files
- Use strong secrets for production
- Enable HTTPS in production

### Database Security
- Change default passwords
- Use SSL connections
- Implement row-level security

## 🚀 Deployment

### Production Build
```bash
# Build production images
docker-compose -f docker-compose.prod.yml build

# Deploy to production
docker-compose -f docker-compose.prod.yml up -d
```

### Environment Configuration
- Development: `.env.dev`
- Staging: `.env.staging`
- Production: `.env.prod`

## 🐛 Troubleshooting

### Common Issues

1. **Port Conflicts**
   - Check if ports 3000, 8000-8006, 5000 are available
   - Modify ports in docker-compose.yml if needed

2. **Database Connection**
   - Ensure PostgreSQL is running
   - Check DATABASE_URL in .env

3. **ML Services Not Responding**
   - Check service logs: `docker-compose logs ml-demand-forecasting`
   - Verify MLflow is accessible

4. **Frontend Build Issues**
   - Clear node_modules: `rm -rf node_modules`
   - Reinstall: `npm install`

### Health Checks
```bash
# Check all services
curl http://localhost:8000/health
curl http://localhost:8001/health
curl http://localhost:3000
```

## 📚 Documentation

- [API Documentation](http://localhost:8000/docs)
- [ML Model Documentation](docs/models.md)
- [Architecture Guide](docs/architecture.md)
- [User Manual](docs/user-guide.md)

## 🤝 Contributing

1. Fork the repository
2. Create feature branch
3. Make changes with tests
4. Submit pull request

## 📄 License

MIT License - see LICENSE file for details
