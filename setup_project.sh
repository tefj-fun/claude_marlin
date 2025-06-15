#!/bin/bash

# Setup script for PPE Detection MVP project structure
echo "🚀 Setting up PPE Detection MVP project structure..."

# Create main directories
mkdir -p backend/app/{api,core,models,services}
mkdir -p frontend/{public,src/{components,pages,services,types}}
mkdir -p ml_models/{weights,training,inference}
mkdir -p docs
mkdir -p tests/{backend,frontend}

# Backend structure
echo "📁 Creating backend structure..."
touch backend/app/__init__.py
touch backend/app/main.py
touch backend/app/api/{__init__.py,auth.py,detection.py,users.py}
touch backend/app/core/{__init__.py,config.py,database.py}
touch backend/app/models/{__init__.py,detection.py,user.py}
touch backend/app/services/{__init__.py,ml_detection.py,image_processing.py}
touch backend/{requirements.txt,Dockerfile,.env.example}

# Frontend structure
echo "📁 Creating frontend structure..."
touch frontend/src/App.tsx
touch frontend/src/components/{ImageUpload.tsx,DetectionResults.tsx,Layout.tsx}
touch frontend/src/pages/{Dashboard.tsx,Settings.tsx}
touch frontend/src/services/api.ts
touch frontend/src/types/detection.ts
touch frontend/{package.json,tailwind.config.js,Dockerfile}

# Configuration files
echo "📁 Creating configuration files..."
touch docker-compose.yml
touch docker-compose.prod.yml
touch .gitignore
touch .env.example

# Documentation
echo "📁 Creating documentation..."
touch docs/{api.md,deployment.md,faq.md}

# Test structure
echo "📁 Creating test structure..."
touch tests/backend/{test_detection.py,test_auth.py}
touch tests/frontend/{App.test.tsx,Detection.test.tsx}

echo "✅ Project structure created successfully!"
echo "📋 Next steps:"
echo "1. Run this script: chmod +x setup_project.sh && ./setup_project.sh"
echo "2. Copy the requirements.txt and package.json content (provided separately)"
echo "3. Set up your environment variables"
echo "4. Download ML models"
echo "5. Start development!"