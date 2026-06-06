# Classic vs. YAML Pipelines

Azure Pipelines offers two methods for creating CI/CD workflows: the legacy **Classic Pipelines** (GUI-based) and the modern **YAML Pipelines** (Code-based).

## Classic Pipelines
Classic pipelines use a visual, drag-and-drop editor.

* **Pros:** Very intuitive, easy to set up without knowing syntax, and provides a clear graphical representation.
* **Cons:** 
  * No true version control (configurations are stored in Azure DevOps, not in your Git repo).
  * Difficult to track changes or apply code review processes (Pull Requests).
  * Build (CI) and Release (CD) are managed in completely separate interfaces.
  * Does not support modern features like Container Jobs.

## YAML Pipelines (Pipeline-as-Code)
YAML pipelines define the CI/CD process in an `azure-pipelines.yml` text file stored alongside your application code.

* **Pros:**
  * **Infrastructure as Code (IaC):** The pipeline is versioned, branched, and tagged exactly like your application code.
  * **Collaboration & Auditing:** Any pipeline change must go through a Pull Request, enabling code review and security audits.
  * **Unified CI/CD:** You can define both multi-stage builds and deployments in a single file and a single UI view.
  * **Advanced Features:** Supports container jobs, templating for reusability, and matrix strategies.
* **Cons:** Requires learning YAML syntax and the specific Azure Pipelines schema.

!!! warning

    **Industry Standard:** Microsoft strongly recommends YAML Pipelines for all new projects. While Classic pipelines are still supported, they are considered legacy and new features are primarily developed for YAML.

!!! tip

    **References:**

    - [Classic vs. YAML Pipelines (Microsoft)](https://learn.microsoft.com/en-us/azure/devops/pipelines/get-started/pipelines-get-started)