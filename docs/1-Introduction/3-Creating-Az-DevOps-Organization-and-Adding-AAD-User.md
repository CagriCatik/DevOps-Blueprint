# Creating an Organization and Connecting to Entra ID

## Creating an Azure DevOps Organization

An organization is the top-level container in Azure DevOps, housing your projects, repos, and pipelines.

1. Navigate to the Azure Portal or [dev.azure.com](https://dev.azure.com).
2. Search for **Azure DevOps organizations** and click **Create**.
3. Name your organization and choose a region.

## Connecting to Microsoft Entra ID (Azure AD)

Integrating Azure DevOps with Microsoft Entra ID (formerly Azure Active Directory) provides enterprise-grade centralized user management and single sign-on (SSO).

### Steps to Connect:

1. Go to **Organization Settings** (gear icon).
2. Select **Microsoft Entra ID** from the left navigation.
3. Click **Connect directory**, select your target Entra ID directory, and confirm.

!!! info "Important"

    You must be an Organization Owner or a member of the Project Collection Administrators group, as well as a member of the target Entra ID tenant, to perform this connection.

### Adding Users from Entra ID

Once connected, you can add users directly from your corporate directory:

1. In Azure DevOps, go to **Organization Settings** > **Users**.
2. Click **Add users**. As you type a name, it will automatically query your Entra ID directory.
3. Assign an **Access level** (e.g., Basic or Stakeholder).

!!! note

    Newly added users receive the assigned access level but do not have project-specific permissions by default. You must explicitly grant them permissions (like Administrator or Contributor) at the project level.

!!! tip

    **References:**

    - [Connect your organization to Microsoft Entra ID (Microsoft)](https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/connect-organization-to-azure-ad)