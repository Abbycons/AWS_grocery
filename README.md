# GroceryMate E-Commerce Application

A full-stack e-commerce platform for grocery shopping, built with Python Flask backend and React frontend.

## 🏗️ Architecture Overview

The system is built on a modern, scalable architecture:

**Frontend Tier:**
- React.js application with responsive design
- Docker containerization for consistent deployment

**Backend Tier:**
- Python Flask API with RESTful endpoints  
- Docker containerization for easy deployment

**Data Tier:**
- PostgreSQL database for reliable data storage
- Secure database management

## 📁 Project Structure

AWS_grocery/
├── backend/           # Python Flask API
│   ├── app/          # Application logic and routes
│   ├── models/       # Database models
│   └── requirements.txt
├── frontend/         # React application
│   ├── src/          # React components and hooks
│   ├── public/       # Static assets
│   └── package.json
├── docs/             # Documentation
└── README.md

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Node.js 16+
- PostgreSQL
- Docker (optional)

### Backend Setup
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app/run.py

### Frontend Setup
cd frontend
npm install
npm start

### Docker Deployment
# Backend
cd backend
docker build -t grocerymate-backend .
docker run -p 5000:5000 grocerymate-backend

# Frontend  
cd frontend
docker build -t grocerymate-frontend .
docker run -p 3000:3000 grocerymate-frontend

## 🛒 Features

- **User Authentication:** Secure registration, login, and session management
- **Role-Based Access Control:** Protected routes for different user types
- **Product Catalog:** Search, filter, and browse products
- **Favorites Management:** Save and manage favorite items
- **Shopping Cart:** Add, modify, and remove items
- **Checkout System:** Multiple payment options
- **Responsive Design:** Mobile-friendly interface

## 🔧 Configuration

1. Set up your database connection:
   DATABASE_URL=postgresql://username:password@localhost:5432/grocerymate
   JWT_SECRET_KEY=your-secret-key-here

## 📊 Database Setup

CREATE DATABASE grocerymate;
-- The application will automatically create tables on first run

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License.
