🏦 Loan Default Prediction System — lone-1
Full-Stack | Microservices | FastAPI | ML | Kubernetes | Jenkins CI/CD | React | Selenium

A complete FinTech-grade Loan Default Prediction platform built with FastAPI, a microservice ML architecture, MongoDB, React, Docker, Kubernetes, Jenkins CI/CD, and Selenium automation.

This project is designed to be production-ready, scalable, cloud-deployable, and structured like a real banking/fintech ML system.

🚀 System Overview

This application predicts loan default risk based on user-provided loan attributes.
It follows a microservice architecture:

Microservices

Backend API Gateway (FastAPI)

Auth (JWT)

Prediction routing

Logging

Model metadata

DB operations

ML Predictor Service (FastAPI)

Loads model.pkl

Runs preprocessing + model inference

Returns prediction + probability

ML Trainer Service (FastAPI + CronJob)

Preprocessing

Model training (LR, RF, XGBoost)

Evaluation

Saves best model → Shared PVC

Updates metadata

Frontend

Built in React, using TailwindCSS

Prediction form

Dashboard with charts

Login/Register

Model monitoring

Database

MongoDB stores:

Users

Predictions

Logs

Model metadata

DevOps

Docker Compose for local multi-service setup

Kubernetes (Deployments, Services, Ingress, HPA, PVC)

Jenkins CI/CD pipeline

Selenium Testing integrated into CI

🏗️ Architecture Diagram
React UI → Backend API Gateway → ML Predictor Service → Model.pkl (PVC)

Backend API → MongoDB:
    - Users
    - Predictions
    - Logs
    - Model Metadata

ML Trainer Service → trains → saves model.pkl → PVC → Predictor


All services are containerized and orchestrated via Kubernetes with autoscaling.

📁 Project Structure
lone-1/
├── backend-api-service/
│   └── app/
├── ml-predictor-service/
│   └── app/
├── ml-trainer-service/
│   └── app/
├── frontend/
│   └── src/
├── kubernetes/
├── jenkins/
├── tests/
│   ├── selenium/
│   └── unit/
├── docker-compose.yml
└── README.md

🧠 Features
🔐 Authentication

JWT token-based authentication

Login / Register

Secure password hashing (bcrypt)

🤖 Machine Learning

Preprocessing pipeline

Models: Logistic Regression, Random Forest, XGBoost

Automatic model selection

Probabilistic prediction

Live model serving

Continuous training via ML Trainer

📊 Dashboard

Graphs using Recharts

Prediction history

Model version display

System health

⚙️ DevOps

Docker & Docker Compose

Kubernetes (Ingress + HPA + Secrets + ConfigMaps)

Jenkins CI/CD:

Linting

Unit tests

Selenium tests

Build + push Docker images

Auto-deploy to Kubernetes

🔧 How to Run (Local)
1. Clone Repo
git clone https://github.com/yourusername/lone-1.git
cd lone-1

2. Start Services (Docker Compose)
docker-compose up --build


Services run at:

Backend: http://localhost:8000

Predictor: http://localhost:8001

Trainer: http://localhost:8002

Frontend: http://localhost:3000

MongoDB: localhost:27017

☸️ Kubernetes Deployment
Apply configs:
kubectl apply -f kubernetes/

Check pods:
kubectl get pods

Autoscaling:
kubectl get hpa

🧪 Testing (Selenium)
Run Selenium tests:
pytest tests/selenium/ --headed


Integrated into Jenkins CI pipeline.

🔄 CI/CD Pipeline (Jenkins)

Pipeline performs:

CI

✔ Install dependencies
✔ Lint Python and JS
✔ Run unit tests
✔ Run ML tests
✔ Run Selenium automation
✔ Build Docker images
✔ Push to DockerHub

CD

✔ Deploy to Kubernetes
✔ Rolling updates
✔ Auto rollback on failure
✔ Versioning and tagging

🛡️ Security Features

HTTPS via Ingress

JWT authentication

Password hashing (bcrypt)

Input validation

MongoDB hardening

Secrets handled using Kubernetes Secrets

CORS protection

API Gateway verification

📈 Monitoring & Logging
Logging

Logs stored in MongoDB

Logs API available for UI

Logs per microservice

Monitoring Stack (Optional)

Prometheus metrics scraping

Grafana dashboards

Pod CPU/Memory charts

HPA scaling visualized

📊 Tech Stack
Layer	Technology
Frontend	React + TailwindCSS
Backend Gateway	FastAPI
ML Predictor	FastAPI
ML Trainer	FastAPI
Database	MongoDB
ML Models	Sklearn + XGBoost
DevOps	Docker, Kubernetes
CI/CD	Jenkins
Testing	Selenium, Pytest
Infra	PVC, Ingress, HPA
✨ Future Improvements

Support for multiple ML model versions

Canary deployment for new ML models

Feature store integration

Adding Streaming (Kafka)

more complex lending rules / risk scoring

A/B testing ML pipelines