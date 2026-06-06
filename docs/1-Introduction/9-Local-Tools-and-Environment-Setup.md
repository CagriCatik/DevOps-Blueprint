# Local Tools and Environment Setup

Everything in this guide is hands-on, so before the first pipeline you need a working local environment: an **Azure account**, the **command-line tools** that talk to Azure, **Git** for version control, and an **editor**. This page is the one-stop checklist. It is referenced from the later chapters — especially [Infrastructure as Code with Bicep](../6-Infrastructure-as-Code-with-Bicep/1-What-is-IaC-and-Bicep.md), where the Azure CLI and Bicep are essential.

!!! tip

    On the recommended reading order, do this page early — right after the [overview](1-Introduction.md). You only set this up once.

## What you will install

| Tool | Why you need it | Verify with |
|---|---|---|
| **Azure account** | A subscription to deploy into | `az account show` |
| **Azure CLI** (`az`) | Command-line control of Azure; runs in every pipeline task | `az version` |
| **Bicep CLI** | Authors/transpiles Infrastructure-as-Code | `az bicep version` |
| **Git** | Version control; checks out code in pipelines | `git --version` |
| **Visual Studio Code** | Editor with Azure/Bicep/YAML support | — |
| **VS Code extensions** | Syntax, validation, IntelliSense | — |

## Step 1 — Register a free Azure account

You need an Azure subscription to deploy resources. The **Azure Free account** includes a starting credit and a set of always-free services — plenty for this guide.

1. Go to [azure.microsoft.com/free](https://azure.microsoft.com/free/).
2. Sign in with a Microsoft account (or create one) and complete identity + card verification (the card is for identity only; free-tier usage is not charged).
3. After signup, confirm you have an active subscription at [portal.azure.com](https://portal.azure.com) → **Subscriptions**.

!!! note

    The free credit covers the small resources we provision (Log Analytics, Data Factory, App Service). Always **clean up** resource groups you no longer need — `az group delete --name <rg>` — so you don't burn credit. Billing and licensing details are on the [Azure DevOps Billing](2-Azure-DevOps-Billing.md) page.

## Step 2 — Install the Azure CLI

The Azure CLI (`az`) is how you — and your pipelines — drive Azure from the command line.

=== "Windows"

    ```powershell
    winget install --exact --id Microsoft.AzureCLI
    ```

=== "macOS"

    ```bash
    brew install azure-cli
    ```

=== "Linux"

    ```bash
    curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
    ```

Then sign in and verify:

```powershell
az login                # opens a browser to authenticate
az account show         # confirms the active subscription
az version
```

## Step 3 — Install Bicep

Bicep is our Infrastructure-as-Code language. It ships with the Azure CLI; install/upgrade the Bicep binary with:

```powershell
az bicep install
az bicep version
```

!!! note

    If `az bicep version` already prints a version, you're done — recent Azure CLI builds bundle it. We use Bicep heavily in the [Infrastructure as Code](../6-Infrastructure-as-Code-with-Bicep/1-What-is-IaC-and-Bicep.md) module.

## Step 4 — Install Git

Git is the version-control system behind Azure Repos. On Windows, **Git for Windows** also gives you **Git Bash**, a Unix-style shell many of this guide's `bash` snippets assume.

=== "Windows"

    ```powershell
    winget install --exact --id Git.Git
    ```

=== "macOS"

    ```bash
    brew install git
    ```

=== "Linux"

    ```bash
    sudo apt-get update && sudo apt-get install -y git
    ```

Verify, then set your identity (used on every commit):

```bash
git --version
git config --global user.name  "Your Name"
git config --global user.email "you@example.com"
```

The day-to-day commands (clone, branch, commit, merge) are in the [Git & Azure Repos Cheatsheet](8-Git-and-Azure-Repos-Cheatsheet.md).

## Step 5 — Install Visual Studio Code

VS Code is a free, cross-platform editor with first-class Azure, Bicep, and YAML support.

=== "Windows"

    ```powershell
    winget install --exact --id Microsoft.VisualStudioCode
    ```

=== "macOS"

    ```bash
    brew install --cask visual-studio-code
    ```

=== "Linux"

    Download from [code.visualstudio.com](https://code.visualstudio.com/) or use your package manager.

## Step 6 — Install the VS Code extensions

These extensions give you syntax highlighting, validation, and IntelliSense for everything in this guide. Install from the command line:

```bash
code --install-extension ms-azuretools.vscode-bicep
code --install-extension ms-vscode.azurecli
code --install-extension ms-azure-devops.azure-pipelines
code --install-extension redhat.vscode-yaml
code --install-extension ms-python.python
```

| Extension | Helps with |
|---|---|
| **Bicep** (`ms-azuretools.vscode-bicep`) | Bicep authoring, IntelliSense, the [IaC module](../6-Infrastructure-as-Code-with-Bicep/4-Log-Analytics-Bicep-Template-and-Module.md) |
| **Azure CLI Tools** (`ms-vscode.azurecli`) | `az` command help and `.azcli` scripts |
| **Azure Pipelines** (`ms-azure-devops.azure-pipelines`) | `azure-pipelines.yml` schema + validation |
| **YAML** (`redhat.vscode-yaml`) | General YAML linting |
| **Python** (`ms-python.python`) | The Flask sample app and tests |

## Step 7 — (Windows) Set Git Bash as the default terminal

Many snippets in this guide use Unix-style `bash`. On Windows, make **Git Bash** VS Code's default integrated terminal so those commands run as written:

1. In VS Code press ++ctrl+shift+p++ → **Terminal: Select Default Profile**.
2. Choose **Git Bash**.
3. Open a new terminal (++ctrl+grave++) — it should now be a Git Bash prompt.

!!! tip

    PowerShell is also fully supported — this guide's Windows snippets work in both. Use whichever you prefer; the IaC module's provisioning **scripts** are deliberately written in PowerShell Core (`pscore`) so they run identically on Microsoft-hosted Linux agents.

## You're ready

Run this quick check — all four should print a version:

```bash
az version && az bicep version && git --version && code --version
```

With your local environment ready, continue with the [Azure DevOps overview](1-Introduction.md) and [billing](2-Azure-DevOps-Billing.md), then create your [organization and project](3-Creating-Az-DevOps-Organization-and-Adding-AAD-User.md).

!!! tip

    **References:**

    - [Create an Azure free account (Microsoft)](https://azure.microsoft.com/en-us/free/)
    - [Install the Azure CLI (Microsoft)](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli)
    - [Install Bicep tools (Microsoft)](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/install)
    - [Visual Studio Code (Microsoft)](https://code.visualstudio.com/docs)
