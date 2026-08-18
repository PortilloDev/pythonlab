# pythonLab

A FastAPI service scaffolded with a clean architecture layout.

## Architecture

The codebase is organized into layers, with dependencies pointing inward:

```
app/
├── domain/          # Entities and core business rules (no framework dependencies)
├── application/      # Use cases orchestrating domain logic
├── infrastructure/   # Implementations of external concerns (DB, third-party APIs, ...)
├── api/               # HTTP layer: FastAPI routers, request/response schemas
└── core/              # Cross-cutting concerns (settings, ...)
```

## Requirements

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) for dependency management

## Setup

```bash
uv sync
```

This creates a `.venv` and installs all runtime and development dependencies.

## Run locally

```bash
uv run uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`. Interactive docs are served at
`http://localhost:8000/docs`.

## Health check

```bash
curl http://localhost:8000/api/v1/health
```

## Tests

```bash
uv run pytest
```

## Linting

```bash
uv run ruff check .
```

## Docker

Build the image:

```bash
docker build -t pythonlab .
```

Run the container:

```bash
docker run -p 8000:8000 pythonlab
```

## Continuous Integration

GitHub Actions runs linting and tests on every push and pull request against `main`
(see `.github/workflows/ci.yml`).
