# Runtime Parameters

**Runtime Parameters** allow pipeline users to pass values into the pipeline at queue time through the Azure DevOps UI, rather than hardcoding or changing YAML every time.

## Parameters vs. Variables

| Feature | Parameters | Variables |
|---|---|---|
| Set at | Queue time (UI) | Pipeline authoring time |
| Type-safe | ✅ Yes (string, boolean, number, object) | ❌ Always strings |
| Required | Can be required | Optional by default |
| Default value | Supported | Supported |

## Defining and Using Parameters

```yaml
parameters:
  - name: environment
    displayName: 'Target Environment'
    type: string
    default: dev
    values:
      - dev
      - qa
      - prod

  - name: runTests
    displayName: 'Run unit tests?'
    type: boolean
    default: true

  - name: imageTag
    displayName: 'Docker image tag'
    type: string

trigger: none  # Manual trigger to use parameters

stages:
  - stage: Deploy
    displayName: Deploy to ${{ parameters.environment }}
    jobs:
      - job: DeployJob
        steps:
          - ${{ if eq(parameters.runTests, true) }}:
            - script: pytest
              displayName: Run tests

          - script: |
              helm upgrade --install my-app ./charts \
                --set image.tag=${{ parameters.imageTag }} \
                --namespace ${{ parameters.environment }}
```

## Object Parameters (Advanced)

Parameters can also be **objects** (arrays or dictionaries) for advanced scenarios like looping over a list of environments:

```yaml
parameters:
  - name: deployTargets
    type: object
    default:
      - env: dev
        slot: staging
      - env: prod
        slot: production

stages:
  - ${{ each target in parameters.deployTargets }}:
    - stage: Deploy_${{ target.env }}
      jobs:
        - job: Deploy
          steps:
            - script: echo "Deploying to ${{ target.env }} in slot ${{ target.slot }}"
```

!!! tip

    **References:**

    - [Runtime parameters (Microsoft)](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/runtime-parameters)
