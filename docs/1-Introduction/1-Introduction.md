# Azure DevOps Overview

## Introduction

Welcome to the Azure DevOps guide. Azure DevOps is a comprehensive suite of services from Microsoft designed to support the entire software development lifecycle (SDLC)—from planning and coding to building, testing, and deployment.

This guide is written for **Python developers** and assumes **no prior CI/CD experience**. Every example uses the same small Python web app, so you can focus on learning the tools rather than a new application each chapter.

!!! tip "Beginner tip"

    If you are brand new, skim [Azure DevOps Overview](1-Introduction.md) (this page) and then meet [The Sample Python Application](7-Sample-Python-Application.md) before diving into pipelines.

## Core Objectives & Features

This knowledge base focuses on utilizing Azure DevOps for Continuous Integration and Continuous Delivery (CI/CD). Key components covered include:

* **Azure Repos:** Cloud-hosted Git repositories for version control. We use a sample **Python (Flask)** project throughout the CI/CD pipeline demonstrations.
* **Azure Pipelines (Classic & YAML):** Automates the building, testing, and deployment of code. We will transition from the visual, legacy **Classic Pipelines** to the modern, code-centric **Multi-stage YAML Pipelines**.
* **Releases & Environments:** Deploying applications to various environments, including Azure App Service, Windows Server VMs, Docker containers, and Azure Kubernetes Service (AKS).
* **Self-Hosted Agents:** Creating pipeline agents on Windows Servers, Docker, and within a Kubernetes cluster using the KEDA operator for autoscaling.
* **Security & Permissions:** Configuring least-privilege access for projects, pipelines, and environments.

## Prerequisites

To follow along with hands-on deployments, an **Azure Cloud account** is required. You can start with an Azure Free account, which typically provides $200 in initial credits.

!!! tip

    **References:**

    - [Azure DevOps Documentation (Microsoft)](https://learn.microsoft.com/en-us/azure/devops/)
    - What is Azure DevOps? [dev.to](https://dev.to)