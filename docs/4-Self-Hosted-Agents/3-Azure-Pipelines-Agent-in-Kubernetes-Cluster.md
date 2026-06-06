# Azure Pipelines Agent in a Kubernetes Cluster

Deploying your Azure Pipelines agent as a Pod inside an Azure Kubernetes Service (AKS) cluster provides high availability and integrates your CI/CD directly into your cloud-native infrastructure.

## 1. Cluster Authentication

First, authenticate your local machine to your AKS cluster using the Azure CLI:

```bash
az aks get-credentials --resource-group <ResourceGroup> --name <ClusterName>
```

## 2. Secure the Personal Access Token (PAT)

Never hardcode your Azure DevOps Personal Access Token inside your Kubernetes deployment manifests. Instead, use a Kubernetes Secret.

1. Base64 encode your PAT.
2. Create a `Secret` manifest:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: azp-secret
  namespace: azp-agent
type: Opaque
data:
  token: <BASE64_ENCODED_PAT>
```

## 3. Deploy the Agent

Create a Kubernetes `Deployment` that utilizes the agent container image stored in your Azure Container Registry (ACR).

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: azp-agent
  namespace: azp-agent
spec:
  replicas: 1
  selector:
    matchLabels:
      app: azp-agent
  template:
    metadata:
      labels:
        app: azp-agent
    spec:
      containers:
      - name: azp-agent
        image: <your-acr>.azurecr.io/azp-agent:linux
        env:
        - name: AZP_URL
          value: "https://dev.azure.com/{your-org}"
        - name: AZP_POOL
          value: "Kubernetes-Pool"
        - name: AZP_TOKEN
          valueFrom:
            secretKeyRef:
              name: azp-secret
              key: token
        securityContext:
          privileged: true # Required for Podman image building
```

Apply the manifests:

```bash
kubectl apply -f secret.yaml
kubectl apply -f deployment.yaml
```

## 4. Manual Scaling and High Availability

Because the agent runs as a Kubernetes Deployment, you can easily scale it manually to handle multiple concurrent jobs:

```bash
kubectl scale deployment azp-agent --replicas=3 -n azp-agent
```

If a worker node goes down, Kubernetes will automatically reschedule the agent pod to a healthy node, ensuring high availability.

!!! tip

    **References:**

    - [Kubernetes Secrets (Kubernetes Docs)](https://kubernetes.io/docs/concepts/configuration/secret/)