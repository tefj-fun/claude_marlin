# PPE Detection MVP - Claude Marlin

A computer vision application for detecting Personal Protective Equipment (PPE) in workplace environments to enhance safety compliance.

## 🎯 Project Overview

This MVP focuses on detecting 5 core PPE items:
- Safety Helmets
- Safety Goggles
- Safety Vests
- Safety Gloves  
- Safety Boots

## 🏗️ Architecture

```
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── __init__.py
│   │   │   ├── auth.py
│   │   │   ├── detection.py
│   │   │   └── users.py
│   │   ├── core/
│   │   │   ├── __init__.py
│   │   │   ├── config.py
│   │   │   └── database.py
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   ├── detection.py
│   │   │   └── user.py
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   ├── ml_detection.py
│   │   │   └── image_processing.py
│   │   └── main.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .env.example
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   │   ├── ImageUpload.tsx
│   │   │   ├── DetectionResults.tsx
│   │   │   └── Layout.tsx
│   │   ├── pages/
│   │   │   ├── Dashboard.tsx
│   │   │   └── Settings.tsx
│   │   ├── services/
│   │   │   └── api.ts
│   │   ├── types/
│   │   │   └── detection.ts
│   │   └── App.tsx
│   ├── package.json
│   ├── tailwind.config.js
│   └── Dockerfile
├── ml_models/
│   ├── weights/
│   ├── training/
│   └── inference/
├── docker-compose.yml
├── .gitignore
└── README.md
```

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- Node.js 18+
- Docker & Docker Compose
- GPU support (recommended for ML processing)

### 1. Clone Repository
```bash
git clone <your-repo-url>
cd claude_marlin
```

### 2. Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# Copy environment file
cp .env.example .env
# Edit .env with your configuration
```

### 3. Frontend Setup
```bash
cd frontend
npm install
```

### 4. Database Setup
```bash
# Using Docker
docker-compose up -d postgres redis

# Run migrations
cd backend
python -m alembic upgrade head
```

### 5. Download ML Model
```bash
# Download pre-trained YOLO model
mkdir -p ml_models/weights
# Add your model download script here
```

### 6. Run Application
```bash
# Start backend
cd backend
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Start frontend (new terminal)
cd frontend
npm start
```

Visit `http://localhost:3000` to access the application.

## 🛠️ Technology Stack

### Backend
- **FastAPI**: Modern Python web framework
- **PostgreSQL**: Primary database
- **Redis**: Caching and real-time data
- **OpenCV**: Image processing
- **YOLOv8/Ultralytics**: PPE detection model
- **Pydantic**: Data validation
- **SQLAlchemy**: ORM

### Frontend
- **React 18**: UI framework
- **TypeScript**: Type safety
- **Tailwind CSS**: Styling
- **Axios**: HTTP client
- **React Query**: Data fetching

### ML/AI
- **YOLOv8**: Object detection
- **OpenCV**: Image preprocessing
- **NumPy**: Numerical operations
- **Pillow**: Image handling

## 📋 Phase 1 Features

### ✅ Completed
- [ ] Basic project structure
- [ ] Image upload API endpoint
- [ ] PPE detection service
- [ ] Simple web interface
- [ ] Database schema
- [ ] User authentication

### 🔄 In Progress
- [ ] ML model integration
- [ ] Frontend components
- [ ] API documentation

### ⏳ Planned
- [ ] Error handling
- [ ] Unit tests
- [ ] Docker deployment

## 🔧 API Endpoints

### Authentication
- `POST /auth/login` - User login
- `POST /auth/register` - User registration
- `POST /auth/logout` - User logout

### Detection
- `POST /api/detect/image` - Upload and detect PPE in image
- `GET /api/detect/history` - Get detection history
- `GET /api/detect/stats` - Get detection statistics

### Configuration
- `GET /api/equipment/types` - Get PPE equipment types
- `PUT /api/equipment/config` - Update PPE configuration

## 🧪 Testing

```bash
# Backend tests
cd backend
pytest

# Frontend tests
cd frontend
npm test
```

## 📊 Database Schema

### Users Table
```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    role VARCHAR(20) DEFAULT 'operator',
    created_at TIMESTAMP DEFAULT NOW()
);
```

### Equipment Types Table
```sql
CREATE TABLE equipment_types (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    is_active BOOLEAN DEFAULT true,
    detection_threshold FLOAT DEFAULT 0.5
);
```

### Detection Events Table
```sql
CREATE TABLE detection_events (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    image_path VARCHAR(255),
    detections JSONB,
    confidence_scores JSONB,
    violation_count INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT NOW()
);
```

## 🔒 Environment Variables

```bash
# Database
DATABASE_URL=postgresql://user:password@localhost:5432/ppe_detection
REDIS_URL=redis://localhost:6379

# Security
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# ML Model
MODEL_PATH=./ml_models/weights/yolov8n.pt
CONFIDENCE_THRESHOLD=0.5
```

## 🚀 Deployment

### Docker Deployment
```bash
# Build and run all services
docker-compose up --build

# Production deployment
docker-compose -f docker-compose.prod.yml up -d
```

### Manual Deployment
1. Set up PostgreSQL and Redis
2. Configure environment variables
3. Run database migrations
4. Start backend server
5. Build and serve frontend

## 📈 Performance Targets

- **Detection Accuracy**: >80% for each PPE item
- **Processing Time**: <3 seconds per image
- **API Response**: <500ms for non-ML endpoints
- **Concurrent Users**: Support 10+ simultaneous users

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

For support and questions:
- Create an issue in the repository
- Check the [documentation](docs/)
- Review the [FAQ](docs/faq.md)

## 🗺️ Roadmap

### Phase 2: Live Camera Integration
- Real-time video stream processing
- WebSocket connections
- Camera management interface

### Phase 3: Advanced Features
- Alert system
- Reporting dashboard
- Multi-camera support

### Phase 4: Production Ready
- Performance optimization
- Security hardening
- Comprehensive testing

---

**Status**: 🚧 Under Development - Phase 1
**Last Updated**: June 2025
