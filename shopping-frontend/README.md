# shopping-frontend

The sample Flask app used throughout the [Azure DevOps Blueprint](../README.md) guide. It is deliberately tiny — two routes and two tests — so the focus stays on Azure DevOps, not the application.

## Routes

| Method | Path | Response |
|---|---|---|
| `GET` | `/` | `Welcome to the Shopping Frontend!` |
| `GET` | `/health` | `{"status": "ok"}` (handy for deployment/health checks) |

## Project layout

```text
shopping-frontend/
├── app/
│   ├── __init__.py
│   └── main.py            # The Flask application
├── tests/
│   └── test_main.py       # pytest unit tests
├── requirements.txt       # Runtime deps (Flask, gunicorn)
├── requirements-dev.txt   # Test/lint tools (pytest, pytest-cov, flake8)
├── Dockerfile             # For the container / Kubernetes chapters
├── azure-pipelines.yml    # The CI pipeline (module 3)
├── pytest.ini             # Test config (puts project root on sys.path)
└── .flake8                # Lint config
```

## Run it locally

```bash
# 1. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate          # macOS / Linux
# .venv\Scripts\Activate.ps1        # Windows (PowerShell)

# 2. Install dependencies
pip install -r requirements-dev.txt

# 3. Lint and test
flake8 .
pytest

# 4. Start the app (development server)
python -m app.main
# Visit http://localhost:8000
```

For production the app is served by **gunicorn** (as in the `Dockerfile`):

```bash
gunicorn --bind 0.0.0.0:8000 --workers 2 app.main:app
```

## Run in Docker

```bash
docker build -t shopping-frontend .
docker run --rm -p 8000:8000 shopping-frontend
# Visit http://localhost:8000/health
```

## CI

`azure-pipelines.yml` installs dependencies, runs `flake8`, then `pytest` with JUnit + coverage on every push to `main`. The later guide modules extend this to build/push a Docker image and deploy to App Service, a VM, and AKS.
