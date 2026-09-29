# Microservices CI/CD Pipeline & Containerized API

An enterprise-grade, containerized REST microservice featuring automated GitHub Actions CI/CD workflows, static security analysis, multi-stage Docker builds, and zero-downtime health probing.

## Key Features

- **FastAPI Core**: High-throughput REST API with automated OpenAPI/Swagger documentation.
- **Multi-Stage Dockerfile**: Employs non-root user execution (`appuser`) and dependency isolation, resulting in a minimal attack surface.
- **Full CI/CD Automation**: GitHub Actions pipeline automating lint audits (`flake8`), unit testing (`pytest`), and container security scans.
- **Static Security Auditing**: Integrated `Aqua Security Trivy` scanner checking for CVEs and container image vulnerabilities.
- **Resilient Health Probes**: Native `/healthz` endpoints exposing runtime metrics (memory pressure, system uptime).

## Pipeline Architecture

```text
[ Git Push / PR ] 
       │
       ▼
[ Flake8 Linting & PyTest Unit Tests ] 
       │
       ▼
[ Multi-Stage Docker Image Build ] 
       │
       ▼
[ Trivy Image Vulnerability Scan ] 
       │
       ▼
[ Zero-Downtime Deployment Validation ]