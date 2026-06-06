# The Sample Python Application

Every chapter in this guide builds, tests, and deploys the **same** small application. Meeting it now means the pipeline examples later will feel familiar instead of abstract.

Our app is **`shopping-frontend`** — a tiny **Flask** web app (the kind of thing that would serve the home page of an online shop). It is deliberately simple: a couple of routes and a couple of tests. That keeps the spotlight on Azure DevOps, not on the app.

## Project structure

```text
shopping-frontend/
├── app/
│   ├── __init__.py
│   └── main.py            # The Flask application
├── tests/
│   └── test_main.py       # pytest unit tests
├── requirements.txt       # Runtime dependencies (Flask, gunicorn)
├── requirements-dev.txt   # Test/lint tools (pytest, pytest-cov, flake8)
├── Dockerfile             # For the container/Kubernetes chapters
└── azure-pipelines.yml    # The CI/CD pipeline (added in the YAML module)
```

## The application code

**`app/main.py`**

```python
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to the Shopping Frontend!"


@app.route("/health")
def health():
    # A health endpoint is handy for deployment checks and load balancers.
    return jsonify(status="ok")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
```

**`tests/test_main.py`**

```python
from app.main import app


def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Shopping Frontend" in response.data


def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"
```

## Dependency files

**`requirements.txt`** — what the app needs to *run*:

```text
flask==3.0.*
gunicorn==23.0.*
```

**`requirements-dev.txt`** — extra tools the *pipeline* needs to test and lint:

```text
-r requirements.txt
pytest==8.*
pytest-cov==5.*
flake8==7.*
```

!!! note

    Splitting runtime and dev dependencies is a Python best practice: your production server only installs `requirements.txt`, while the build agent installs `requirements-dev.txt` to run the tests.

## How a Python pipeline differs from a compiled language

If you have seen .NET or Java pipelines, the Python flow is a little different — and usually simpler, because Python is **interpreted** (there is no separate "compile" step). Here is the mental map we use throughout this guide:

| Pipeline stage | What it means for Python | Typical command |
|---|---|---|
| **Restore** | Install dependencies | `pip install -r requirements-dev.txt` |
| **Build** | There is no compile step — instead we **lint** to catch errors | `flake8 .` |
| **Test** | Run unit tests and measure coverage | `pytest --cov=app` |
| **Publish** | Package the source code into a deployable artifact (a zip) | `archive` + `PublishPipelineArtifact` |
| **Deploy** | Run the app with a production server | `gunicorn app.main:app` |

!!! tip

    **`gunicorn`** is the production web server we use to run Flask in the cloud. The built-in `app.run()` server is only for local development — never use it in production.

## Run it locally first (optional but recommended)

Before automating anything, it helps to run the app on your own machine so you know what "working" looks like:

```bash
# 1. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate        # On Windows: .venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements-dev.txt

# 3. Run the tests
pytest

# 4. Start the app
python -m app.main
# Visit http://localhost:8000 in your browser
```

Once this works locally, the rest of the guide is about making Azure DevOps do these exact steps for you, automatically, on every push.

!!! tip

    **References:**

    - [Flask documentation](https://flask.palletsprojects.com/)
    - [pytest documentation](https://docs.pytest.org/)
    - [Build Python apps in Azure Pipelines (Microsoft)](https://learn.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python)
