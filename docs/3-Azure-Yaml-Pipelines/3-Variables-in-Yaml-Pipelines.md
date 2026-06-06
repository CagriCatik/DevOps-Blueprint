# Variables in YAML Pipelines

Variables in Azure Pipelines store values that can be reused and referenced throughout your pipeline. They can be defined at multiple scopes and originate from multiple sources.

## Variable Scopes

```mermaid
graph TD
    A[Variable Sources] --> B[Pipeline-level\nyaml: variables:]
    A --> C[Stage-level\nscoped to a stage]
    A --> D[Job-level\nscoped to a job]
    A --> E[Library\nVariable Groups]
    A --> F[Pipeline UI\nSecret Variables]
    B --> G[$(myVar)]
    C --> G
    D --> G
    E --> G
    F --> G
```

## Defining Variables

```yaml
variables:
  # Simple key-value
  buildConfiguration: Release
  imageName: shopping-frontend

  # Reference a variable group from Library
  - group: my-prod-secrets

stages:
  - stage: Build
    variables:
      stageVar: 'only-in-build-stage'
    jobs:
      - job: Build
        variables:
          jobVar: 'only-in-this-job'
        steps:
          - script: echo $(buildConfiguration) $(stageVar) $(jobVar)
```

## Setting Variables at Runtime

You can dynamically set a variable for use in subsequent steps within the same job:

```yaml
steps:
  - script: echo "##vso[task.setvariable variable=myDynamicVar]hello-world"
    displayName: Set dynamic variable

  - script: echo $(myDynamicVar)
    displayName: Use dynamic variable
```

## Passing Variables Between Jobs (Output Variables)

```yaml
jobs:
  - job: Producer
    steps:
      - script: echo "##vso[task.setvariable variable=myOutput;isOutput=true]produced-value"
        name: SetVar

  - job: Consumer
    dependsOn: Producer
    variables:
      # Reference the output variable from the Producer job
      consumedValue: $[ dependencies.Producer.outputs['SetVar.myOutput'] ]
    steps:
      - script: echo $(consumedValue)
```

!!! tip

    **References:**

    - [Define variables (Microsoft)](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/variables)
