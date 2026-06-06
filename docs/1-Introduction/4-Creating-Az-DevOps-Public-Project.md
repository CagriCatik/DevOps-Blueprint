# Creating a Public Project and Enabling Parallel Jobs

## Private vs. Public Projects

By default, Azure DevOps organizations are restricted to creating **private projects**. However, creating a **public project** is highly beneficial for open-source development, as it grants generous free pipeline limits (e.g., 10 parallel Microsoft-hosted jobs and unlimited self-hosted jobs).

### Allowing Public Projects

1. Go to **Organization Settings** > **Policies**.
2. Toggle **Allow public projects** to On.
3. You can now create a new project and set its visibility to **Public**.

## Enabling Classic Pipelines

To encourage the modern "Pipeline-as-Code" methodology, Microsoft disables Classic (GUI-based) build and release pipelines for new organizations. If you need to use them (e.g., for legacy support or learning purposes):

1. Go to **Organization Settings** > **Pipelines** > **Settings**.
2. Toggle off the settings: **Disable creation of classic release pipelines** and **Disable creation of classic build pipelines**.

## Requesting Free Parallel Jobs

To prevent crypto-mining abuse, Microsoft temporarily disabled the automatic grant of free parallel jobs for new public and private projects. You must explicitly request them.

### Steps to Request Parallelism:

1. Fill out the **Azure DevOps Parallelism Request Form**.
2. Provide your Name, Email, Organization Name, and specify if you are requesting jobs for a Public or Private project.
3. Provide a link to your repository and a justification (e.g., "Creating demo pipelines for a CI/CD training course").
4. Submit the request. Approval typically takes 2–3 business days.

!!! tip

    **References:**

    - [Configure parallel jobs (Microsoft)](https://learn.microsoft.com/en-us/azure/devops/pipelines/licensing/concurrent-jobs)
    - [Make a private project public (Microsoft)](https://learn.microsoft.com/en-us/azure/devops/organizations/public/make-project-public)