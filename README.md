# Azure DevOps Blueprint

A **beginner-friendly, Python-focused** guide to **Azure DevOps** CI/CD — from creating your first organization and repo to building automated pipelines that test and deploy a real Python web app to App Service, Linux VMs, Docker, and Kubernetes.

> Every example builds, tests, and deploys the **same** small Flask app (`shopping-frontend`), so you can focus on learning Azure DevOps instead of a new app in each chapter.

## What's inside

| Module | Topic |
|---|---|
| **1. Introduction** | What Azure DevOps is, billing, org/project/repo setup, the sample Python app, and a [Git & Azure Repos cheatsheet](docs/1-Introduction/8-Git-and-Azure-Repos-Cheatsheet.md) |
| **2. Classic Pipelines** | CI/CD with the visual editor: build, test + coverage, App Service, Linux VM (Nginx + Gunicorn), Docker/ACR, AKS |
| **3. YAML Pipelines** | Pipeline-as-code: syntax, stages/jobs, variables, templates, environments, caching, a Python CI template, and an end-to-end AKS lab |
| **4. Self-Hosted Agents** | Running your own agents on a VM, Docker, Kubernetes, KEDA autoscaling, and a full Windows-agent reference |
| **5. Security** | Least-privilege permissions for projects, pipelines, environments, service connections, and repos |

## Build & preview locally

You need **Python 3.x**.

```bash
# 1. Create and activate a virtual environment
python -m venv .venv
.venv\Scripts\activate          # Windows

# 2. Install the build tool
pip install -r requirements.txt

# 3. Live preview with auto-reload at http://localhost:8000
zensical serve

# 4. Build the static site into ./site
zensical build --clean
```
