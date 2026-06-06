# Auto-Scaling Kubernetes Pipeline Agents with KEDA

Manually scaling pipeline agents is inefficient. **KEDA (Kubernetes Event-driven Autoscaling)** allows your AKS cluster to automatically scale your agent pods based on the number of pending jobs in your Azure DevOps queue.

## 1. Install KEDA
KEDA can be installed easily using Helm:
```bash
helm repo add kedacore https://kedacore.github.io/charts
helm repo update
helm install keda kedacore/keda --namespace keda --create-namespace
```

## 2. Jobs vs. Deployments
When auto-scaling with KEDA, it is highly recommended to scale **Kubernetes Jobs** rather than Deployments.
*   **Why?** If KEDA scales down a Deployment, it might randomly terminate a Pod that is currently executing a pipeline, causing the build to fail unpredictably.
*   **The Solution:** Use the `--once` flag in your agent's startup script. KEDA will spawn a Kubernetes `Job` for each pending pipeline run. The agent will process exactly one pipeline job and then intentionally exit, cleanly completing the Kubernetes Job.

## 3. Configure the KEDA ScaledJob
To configure KEDA, you define a `ScaledJob` custom resource. This resource connects the Azure DevOps trigger to your agent pod template.

```yaml
apiVersion: keda.sh/v1alpha1
kind: ScaledJob
metadata:
  name: azp-scaledjob
  namespace: azp-agent
spec:
  jobTargetRef:
    template:
      spec:
        containers:
        - name: azp-agent
          image: <your-acr>.azurecr.io/azp-agent:linux
          args: ["--once"] # Crucial: Makes the agent terminate after one job
          env:
          # (AZP_URL, AZP_POOL, and AZP_TOKEN references)
  maxReplicaCount: 10 # Limits concurrent agents
  triggers:
  - type: azure-pipelines
    metadata:
      poolName: "Kubernetes-Pool"
      organizationURLFromEnv: "AZP_URL"
    authenticationRef:
      name: pipeline-trigger-auth
```

## 4. The Placeholder Agent
KEDA monitors the Azure DevOps agent pool to determine the queue length.
!!! info "Important"

    Azure Pipelines requires at least one registered agent in a pool before it allows a pipeline to even enter the queue. Therefore, you must leave a "dummy" or offline agent registered in your pool so pipelines can be queued; KEDA will then detect the queue and scale up the actual pods.

Once the pipeline finishes, the agent container exits successfully, and KEDA handles scaling back down to zero.

!!! tip

    **References:**

    - [KEDA Scalers: Azure Pipelines](https://keda.sh/docs/latest/scalers/azure-pipelines/)