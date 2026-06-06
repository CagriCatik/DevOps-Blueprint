# Terraform Environment Setup

You already installed the **Azure CLI, Git, and VS Code** in [Local Tools and Environment Setup](../1-Introduction/9-Local-Tools-and-Environment-Setup.md). This page adds only the **Terraform-specific** pieces on top — the Terraform CLI, a package manager to keep it updated, the HashiCorp VS Code extension, and a working folder. We won't repeat the Azure CLI / Git / VS Code steps.

!!! note

    Already have the Azure CLI, Git, and VS Code? Skip straight to [Step 2](#step-2-install-terraform). If not, do the [base setup](../1-Introduction/9-Local-Tools-and-Environment-Setup.md) first — Terraform needs the Azure CLI to authenticate to Azure.

## What this page adds

| Tool | Why | Verify with |
|---|---|---|
| **Chocolatey** (Windows) | Package manager to install/update Terraform cleanly | `choco --version` |
| **Terraform CLI** | The `terraform` command itself | `terraform version` |
| **HashiCorp Terraform** VS Code extension | HCL syntax, formatting, IntelliSense | — |

## Step 1 — Install Chocolatey (Windows)

[Chocolatey](https://chocolatey.org/) is a package manager for Windows that makes installing and *upgrading* Terraform a one-liner. In an **elevated PowerShell** (Run as Administrator):

```powershell
Set-ExecutionPolicy Bypass -Scope Process -Force
[System.Net.ServicePointManager]::SecurityProtocol = `
  [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```

Verify:

```powershell
choco --version
```

!!! note

    On **macOS/Linux** use Homebrew or the official HashiCorp repo instead of Chocolatey — see Step 2's tabs. Chocolatey is Windows-only.

## Step 2 — Install Terraform

=== "Windows (Chocolatey)"

    ```powershell
    choco install terraform -y
    ```

=== "macOS (Homebrew)"

    ```bash
    brew tap hashicorp/tap
    brew install hashicorp/tap/terraform
    ```

=== "Linux (apt)"

    ```bash
    wget -O- https://apt.releases.hashicorp.com/gpg | \
      sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg
    echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] \
      https://apt.releases.hashicorp.com $(lsb_release -cs) main" | \
      sudo tee /etc/apt/sources.list.d/hashicorp.list
    sudo apt update && sudo apt install terraform
    ```

Confirm the install:

```powershell
terraform version
terraform -help
```

!!! tip

    Pin or check your version — Terraform configs can require a minimum (`required_version` in the `terraform {}` block, covered in [Core Workflow](4-Terraform-Core-Workflow-and-First-Resource.md)). To upgrade later with Chocolatey: `choco upgrade terraform`.

## Step 3 — Set up the HashiCorp Terraform VS Code extension

This extension gives syntax highlighting, `terraform fmt` on save, IntelliSense for providers, and inline docs.

```powershell
code --install-extension hashicorp.terraform
```

Then enable format-on-save for `.tf` files. In VS Code **settings.json** (++ctrl+shift+p++ → *Preferences: Open User Settings (JSON)*):

```json
{
  "[terraform]": {
    "editor.defaultFormatter": "hashicorp.terraform",
    "editor.formatOnSave": true
  },
  "[terraform-vars]": {
    "editor.defaultFormatter": "hashicorp.terraform",
    "editor.formatOnSave": true
  }
}
```

!!! tip

    Format-on-save runs `terraform fmt` automatically, keeping every `.tf` file canonically formatted — the Terraform equivalent of `black` for Python. Consistent formatting makes pull-request diffs about *content*, not whitespace.

## Step 4 — Create the source-code folder

Keep Terraform code in its own repo (the same separation rationale as the Bicep [infra repo](../6-Infrastructure-as-Code-with-Bicep/2-Setup-Service-Connection-and-Structure.md)). Create and initialise it:

```bash
mkdir shopping-terraform
cd shopping-terraform
git init
```

Add a Terraform-aware `.gitignore` **before your first commit** — state files and downloaded providers must never be committed:

```gitignore
# Local .terraform directories and provider plugins
**/.terraform/*

# State files — may contain secrets; managed by the remote backend
*.tfstate
*.tfstate.*

# Crash logs and plan output
crash.log
*.tfplan

# Variable files that may hold secrets
*.auto.tfvars
*.tfvars
!example.tfvars
```

!!! warning

    **Never commit `*.tfstate`.** State can contain secrets in plain text (passwords, keys) and is the source of truth for what exists. We move it to a secure remote backend on [Azure Provider and Remote State](8-Azure-Provider-and-Remote-State.md); until then it stays local and git-ignored.

## You're ready

```powershell
terraform version && az version && git --version
```

All three should print versions. Next we authenticate to Azure and create the very first Terraform resource.

!!! tip

    **References:**

    - [Install Terraform (HashiCorp)](https://developer.hashicorp.com/terraform/install)
    - [HashiCorp Terraform VS Code extension](https://marketplace.visualstudio.com/items?itemName=HashiCorp.terraform)
    - [Chocolatey Terraform package](https://community.chocolatey.org/packages/terraform)
