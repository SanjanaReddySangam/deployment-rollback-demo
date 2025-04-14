# 🚀 Deployment Rollback Demo using GitHub Actions

This project demonstrates a simple yet powerful CI/CD pipeline with **automatic rollback** using **Docker** and **GitHub Actions**.

When a new version of the application is pushed:
- Version 2 is deployed using Docker.
- A health check is performed.
- If the deployment fails (e.g., returns HTTP 500), the pipeline automatically rolls back to the last known good version (Version 1).

---

## 📂 Project Structure

```
deployment-rollback-demo/
├── app/
│   ├── v1/             # Working version of the app
│   │   └── app.py
│   └── v2/             # Broken version (used to simulate failure)
│       └── app.py
├── Dockerfile          # Builds app from selected version
├── docker-compose.yml  # Runs container with selected version
└── .github/
    └── workflows/
        └── deploy.yml  # CI/CD workflow with rollback logic
```

---

## 🛠 Tech Stack

- **GitHub Actions** for CI/CD
- **Docker & Docker Compose** for containerization
- **Flask (Python)** simple web app
- **Health Check + Auto-Rollback Logic**

---

## 🔁 How It Works

1. Code is pushed to the `main` branch.
2. GitHub Actions builds and deploys Version 2.
3. A health check hits the root endpoint (`/`).
4. If it fails (non-200 response), it triggers a rollback to Version 1 using Docker.

---

## ✅ Example Output

- **Version 1** returns:  
  `Hello from Version 1!`

- **Version 2** raises an error, causing the pipeline to roll back automatically.

---

## 📦 Build and Run Locally

```bash
# Build and run Version 1
docker compose build --build-arg APP_VERSION=v1
docker compose up

# Test Version 2 (should fail)
docker compose build --build-arg APP_VERSION=v2
docker compose up
```

---

## ✅ Live GitHub Actions Status

![CI](https://github.com/SanjanaReddySangam/deployment-rollback-demo/actions/workflows/deploy.yml/badge.svg)

---

## 🧠 What You Learn

- GitHub Actions workflow creation
- Conditional logic in CI pipelines
- Docker ARG and dynamic builds
- Health checking and rollback strategy
