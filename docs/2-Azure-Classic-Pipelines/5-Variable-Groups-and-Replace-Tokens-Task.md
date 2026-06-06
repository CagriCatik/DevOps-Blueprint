# Variable Groups & Replace Tokens Task

**Variable Groups** store key-value pairs that can be shared across pipelines and release stages. The **Replace Tokens** task uses those variables to inject environment-specific configuration into application config files at deployment time.

## Concept: "Build Once, Deploy Many"

```mermaid
flowchart TD
    A[Single Build Artifact] --> B[Release Pipeline]
    B --> C[Stage: Dev\nVarGroup: App-Dev]
    B --> D[Stage: QA\nVarGroup: App-QA]
    B --> E[Stage: Prod\nVarGroup: App-Prod]
    C --> F[Replace #{ConnectionString}# → dev-db]
    D --> G[Replace #{ConnectionString}# → qa-db]
    E --> H[Replace #{ConnectionString}# → prod-db]
```

## Creating a Variable Group
1. Go to **Pipelines → Library → + Variable group**.
2. Name the group (e.g., `App-Production`).
3. Add key-value pairs. Mark secrets as **🔒 secret** to mask them in logs.

### Linking to Azure Key Vault
For high-security environments, link the variable group to an **Azure Key Vault**. Azure DevOps will pull the secrets at runtime without storing them in Azure DevOps itself.

## The Replace Tokens Task
Install the **Replace Tokens** extension from the Azure DevOps Marketplace. Then add the task to your release stage:

| Setting | Value |
|---|---|
| Root directory | `$(System.DefaultWorkingDirectory)` |
| Target files | `**/*.json`, `**/.env` |
| Token prefix | `#{` |
| Token suffix | `}#` |
| Action on missing variable | `fail` |

### Example: `config.json` before replacement
Our Flask app reads its settings from a small `config.json` checked into the repo with **placeholders** instead of real values:

```json
{
  "DATABASE_URL": "#{DATABASE_URL}#",
  "SECRET_KEY": "#{SECRET_KEY}#"
}
```

After the Replace Tokens task runs, `#{DATABASE_URL}#` and `#{SECRET_KEY}#` are replaced with the actual values from the linked Variable Group for that stage.

!!! tip

    Many Python apps prefer **environment variables** over a config file. The Replace Tokens approach works the same way on a `.env` file:

    ```text
    DATABASE_URL=#{DATABASE_URL}#
    SECRET_KEY=#{SECRET_KEY}#
    ```

    Your Flask app then reads them with `os.environ["DATABASE_URL"]` (or a library like `python-dotenv`).

!!! warning

    Never commit real secrets to your repository. Always use token placeholders (`#{...}#`) in config files and supply the real values through Variable Groups.

!!! tip

    **References:**

    - [Replace Tokens task (Marketplace)](https://marketplace.visualstudio.com/items?itemName=qetza.replacetokens)
    - [Variable groups for Azure Pipelines (Microsoft)](https://learn.microsoft.com/en-us/azure/devops/pipelines/library/variable-groups)
