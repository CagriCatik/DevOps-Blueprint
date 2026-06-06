# Azure DevOps Blueprint — for Python Developers

This is a **hands-on, beginner-friendly** guide to **Azure DevOps**, written specifically for people building and shipping **Python applications**.

If you have never used Azure DevOps before, you are in the right place. We start from "what is it and why should I care?" and finish with a complete, automated pipeline that builds, tests, and deploys a real Python web app — with no prior CI/CD experience assumed.

## What you will learn

By the end of this guide you will be able to:

- Create an Azure DevOps **organization, project, and Git repository**.
- Build a **CI/CD pipeline** that automatically tests and deploys your Python code every time you push.
- Deploy a Python app to **Azure App Service, a Linux VM, Docker, and Kubernetes (AKS)**.
- Run your own **self-hosted build agents** and scale them automatically.
- **Secure** your pipelines, secrets, and repositories using least-privilege best practices.
- Provision the **Azure infrastructure itself as code** with **Bicep** and **Terraform**, deployed from a pipeline.

## The app we will use throughout

Every example in this guide builds, tests, and deploys the **same small Python web app** — a Flask application called `shopping-frontend`. Defining it once means you can focus on learning Azure DevOps instead of a new app in every chapter.

**Start here:** [The Sample Python Application](1-Introduction/7-Sample-Python-Application.md)

## Key terms in one sentence each

New to DevOps vocabulary? Keep this cheat sheet handy:

| Term | Plain-English meaning |
|---|---|
| **CI (Continuous Integration)** | Automatically build and test your code every time someone pushes a change. |
| **CD (Continuous Delivery/Deployment)** | Automatically ship the tested code to a server or cloud environment. |
| **Pipeline** | The recipe that tells Azure DevOps how to build, test, and deploy your app. |
| **Agent** | The machine (cloud or your own) that actually runs the pipeline steps. |
| **Artifact** | The packaged output of a build (e.g., a zip of your app) that gets deployed. |
| **Repo** | A Git repository — where your source code lives. |

**Quick reference:** [Git & Azure Repos Cheatsheet](1-Introduction/8-Git-and-Azure-Repos-Cheatsheet.md) — every command for branching, committing, pull requests, and more.

## Learning path (recommended order)

1. **[Introduction](1-Introduction/1-Introduction.md)** — What Azure DevOps is, pricing, and getting your account, project, and repo ready.
2. **[Azure Classic Pipelines](2-Azure-Classic-Pipelines/1-Python-Classic-Build-Pipeline.md)** — Learn CI/CD concepts using the visual, click-based editor (great for absolute beginners).
3. **[Azure YAML Pipelines](3-Azure-Yaml-Pipelines/1-Basic-Yaml-Pipeline-Syntax.md)** — The modern, code-based way to define pipelines (what you should use for real projects).
4. **[Self-Hosted Agents](4-Self-Hosted-Agents/1-Azure-Pipelines-Agent-in-Windows-Vm.md)** — Run pipelines on your own machines and auto-scale them.
5. **[Security in Azure DevOps](5-Security-in-Azure-DevOps/1-Security-Groups-in-Azure-DevOps.md)** — Lock everything down with least-privilege permissions.
6. **[Infrastructure as Code with Bicep](6-Infrastructure-as-Code-with-Bicep/1-What-is-IaC-and-Bicep.md)** — Provision the Azure resources behind the app with Bicep, deployed from a YAML pipeline.
7. **[Infrastructure as Code with Terraform](7-Infrastructure-as-Code-with-Terraform/1-What-is-Terraform.md)** — Provision the same Azure footprint with Terraform — providers, state, modules, and the `azuread`/`azapi` providers.

!!! tip

    **Brand new to all of this?** Read the modules in order. Each one builds on the previous. If you only have time for one path to production, do **Introduction → YAML Pipelines** and deploy to **Azure App Service**.

!!! note

    **References:**

    - [Azure DevOps Documentation (Microsoft)](https://learn.microsoft.com/en-us/azure/devops/)
    - [Build, test, and deploy Python apps (Microsoft)](https://learn.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python)
