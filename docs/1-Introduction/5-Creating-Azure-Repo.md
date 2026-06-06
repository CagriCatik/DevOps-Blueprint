# Creating and Cloning an Azure Repo

Azure Repos provides secure, cloud-hosted Git repositories.

## Creating a Repository

1. Navigate to your Azure DevOps project.
2. Select **Repos** from the sidebar.
3. Click the repository dropdown at the top and select **New repository**.
4. Provide a name and select **Git** as the repository type.

## Cloning the Repository

To push code from your local machine to Azure Repos, you must clone the remote repository and authenticate.

### 1. Get the Clone URL

Click the **Clone** button in the top right corner of your repo to copy the HTTPS or SSH URL.

### 2. Authentication

While Azure DevOps historically allowed generating direct Git credentials (passwords), modern authentication relies on secure methods:

* **Git Credential Manager (GCM):** The recommended method. When you run `git clone <URL>`, a browser popup prompts you to sign in with your Azure DevOps Microsoft account. GCM securely caches the token.
* **Personal Access Tokens (PAT):** You can generate a PAT in your User Settings and embed it in the URL: `git clone https://<PAT>@dev.azure.com/org/project/_git/repo`.
* **SSH Keys:** Highly recommended for Linux/macOS. Generate an SSH key and upload the public key to your Azure DevOps User Settings.

## Pushing Code

Once cloned, copy your application code into the folder and push it. In this guide that code is our [sample Python (Flask) app](7-Sample-Python-Application.md) — the `app/`, `tests/`, and `requirements*.txt` files:

```bash
git add .
git commit -m "Add initial Python (Flask) project"
git push origin main
```

!!! tip

    Add a Python **`.gitignore`** before your first push so you never commit junk like `.venv/`, `__pycache__/`, or `.pytest_cache/`. GitHub's official [Python.gitignore](https://github.com/github/gitignore/blob/main/Python.gitignore) is a great starting point.

!!! note

    Need the full command reference for branching, committing, pull requests, and more? See the [Git & Azure Repos Cheatsheet](8-Git-and-Azure-Repos-Cheatsheet.md).

!!! tip

    **References:**

    - [Clone an existing Git repo (Microsoft)](https://learn.microsoft.com/en-us/azure/devops/repos/git/clone)
    - [Use Git Credential Manager to authenticate (Microsoft)](https://learn.microsoft.com/en-us/azure/devops/repos/git/set-up-credential-managers)
