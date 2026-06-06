# Azure DevOps Billing and Access Levels

Understanding how Azure DevOps billing works ensures you manage costs effectively while utilizing the right CI/CD resources.

## Access Levels (User Licensing)

Azure DevOps uses a per-user, per-month billing model.

* **Basic Access (First 5 free):** Gives users full access to Azure Boards, Repos, and Pipelines. Beyond the first 5 users, it costs approximately $6/user/month.
* **Stakeholder Access (Free, unlimited):** Ideal for users who only need to view dashboards, track work items, or approve releases. Stakeholders cannot access source code or configure pipelines.
* **Basic + Test Plans:** Required for users executing manual and exploratory testing.

## Pipeline Capacity (Parallel Jobs)

Azure DevOps bills based on how many CI/CD pipelines can run simultaneously, known as **parallel jobs**.

### Free Tier Limits

* **Private Projects:** Include **1 free Microsoft-hosted job** (capped at 1,800 minutes/month) and **1 free self-hosted job** (unlimited minutes).
* **Public Projects:** Include up to **10 free Microsoft-hosted jobs** (unlimited minutes) and unlimited self-hosted jobs. *Note: Free grants for public projects may require submitting a request form.*

### Paid Capacity

If your team needs to run more jobs concurrently, you must purchase additional capacity:

* **Microsoft-Hosted:** ~$40 per extra job/month (removes the 1,800-minute limit).
* **Self-Hosted:** ~$15 per extra job/month. You manage the infrastructure (e.g., VMs, containers), but gain unlimited minutes.

## Azure Artifacts

Azure DevOps includes **2 GB of free storage** for Azure Artifacts (used for hosting your own package feeds — for Python that means **pip/PyPI-style packages**, plus npm, Maven, NuGet, and more). Additional storage is billed per gigabyte.

!!! note

    You only need Azure Artifacts if you want to publish **private Python packages** for your team to `pip install`. For a single app like our sample, you can skip it for now.

!!! tip

    **References:**

    - [Azure DevOps Pricing (Microsoft)](https://azure.microsoft.com/en-us/pricing/details/devops/azure-devops-services/)
    - Azure DevOps Access Levels [Microsoft Learn](https://learn.microsoft.com/en-us/azure/devops/organizations/security/access-levels)