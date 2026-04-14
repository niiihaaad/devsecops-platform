# DevSecOps Microservice Platform

## 🚀 Overview
This project is a complete DevSecOps pipeline demonstrating CI/CD automation, containerization, security scanning, and Kubernetes deployment of a Python microservice.

---

## 🧱 Architecture

GitHub → GitHub Actions → Docker Build → GHCR → Kubernetes (Minikube)

---

## ⚙️ Tech Stack

- Python (FastAPI)
- Docker
- GitHub Actions (CI/CD)
- GitHub Container Registry (GHCR)
- Kubernetes (Minikube)
- Trivy (Container Security Scan)
- Gitleaks (Secret Scanning)

---

## 🔁 CI/CD Pipeline

1. Code pushed to GitHub
2. GitHub Actions triggered
3. Runs security checks:
   - Gitleaks (secrets)
   - Trivy (image scan)
4. Builds Docker image
5. Pushes image to GHCR
6. Kubernetes pulls image and deploys service

---

## 🛡️ DevSecOps Features

- Secret scanning with Gitleaks
- Container vulnerability scanning with Trivy
- Secure image storage in GHCR
- Kubernetes imagePullSecrets authentication

---

## 📦 Deployment

```bash
kubectl apply -f k8s/
kubectl get pods
