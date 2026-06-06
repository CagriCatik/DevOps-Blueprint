# Functions in YAML Pipelines

Azure Pipelines provides a rich library of built-in **functions** you can use within expressions to create sophisticated conditional logic, string manipulation, and control flow.

## Logical Functions

| Function | Description | Example |
|---|---|---|
| `and(a, b)` | Both conditions must be true | `and(succeeded(), eq(variables['Build.SourceBranch'], 'refs/heads/main'))` |
| `or(a, b)` | Either condition is true | `or(failed(), canceled())` |
| `not(a)` | Negates a condition | `not(canceled())` |
| `eq(a, b)` | Equality check | `eq(variables['env'], 'prod')` |
| `ne(a, b)` | Not-equal check | `ne(variables['env'], 'dev')` |

## Status Check Functions

These are most commonly used in `condition:` blocks:

| Function | Meaning |
|---|---|
| `succeeded()` | Previous task/job/stage succeeded |
| `failed()` | Previous task/job/stage failed |
| `always()` | Always run, regardless of status |
| `canceled()` | Pipeline was canceled |
| `succeededOrFailed()` | Run if not canceled |

## String Functions

```yaml
variables:
  branchName: ${{ replace(variables['Build.SourceBranch'], 'refs/heads/', '') }}
```

| Function | Description |
|---|---|
| `replace(str, old, new)` | Replace substring |
| `contains(str, sub)` | Returns `true` if substring found |
| `startsWith(str, prefix)` | Returns `true` if string starts with prefix |
| `lower(str)` | Convert to lowercase |
| `upper(str)` | Convert to uppercase |

## Practical Example: Only Deploy to Prod on `main`

```yaml
stages:
  - stage: Deploy
    condition: and(succeeded(), eq(variables['Build.SourceBranch'], 'refs/heads/main'))
    jobs:
      - job: DeployProd
        steps:
          - script: echo "Deploying to production..."
```

!!! tip

    **References:**

    - [Expressions and functions (Microsoft)](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/expressions)
