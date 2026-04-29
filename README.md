# fastapi-ddd-boilerplate

A minimal Domain-Driven Design (DDD) starter using FastAPI, Docker, and docker-compose. Intended as a small, opinionated scaffold to start building DDD-style services; Kubernetes manifests will be added in the future.

## Features

- FastAPI application with example endpoints.
- Dockerfile and [compose.yml](compose.yml) for local development (Postgres + Redis + app).
- Simple, expandable layout to introduce DDD layers (domain, application, infrastructure).
- Pinned dependencies in [requirements.txt](requirements.txt).

## Quickstart

Requirements: Docker & Docker Compose, or Python 3.12+ and pip.

Run with Docker Compose (recommended):
```sh
docker compose -f [compose.yml](http://_vscodecontentref_/0) up --build
```
