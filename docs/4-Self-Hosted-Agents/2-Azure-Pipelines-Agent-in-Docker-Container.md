# Azure Pipelines Agent in a Docker Container

Containerizing your self-hosted agent ensures an isolated, reproducible, and easily deployable build environment.

## 1. Prepare the Dockerfile

To create a containerized agent, you need a `Dockerfile` and a startup script (`start.sh`). The `start.sh` script downloads the agent package, configures it using environment variables, and starts the listener.

!!! warning

    Make sure your `start.sh` file uses **Unix (LF)** line endings. If created on Windows, it might default to CRLF, which will cause the container to crash.

```dockerfile
FROM ubuntu:22.04

# Install base dependencies
RUN apt-get update && apt-get install -y curl git jq iputils-ping

# Install the build tools your pipelines need (here: Python 3 + pip)
RUN apt-get install -y python3 python3-pip python3-venv

# Install Podman (instead of Docker)
RUN apt-get install -y podman

WORKDIR /azp
COPY start.sh .
RUN chmod +x start.sh

ENTRYPOINT ["./start.sh"]
```

## 2. Why Podman Instead of Docker?

From Kubernetes version 1.24 onwards, the Docker runtime (Dockershim) was removed. Using Docker-in-Docker (DinD) inside Kubernetes has become problematic. **Podman** is a daemonless, drop-in replacement for the Docker CLI that works seamlessly inside containers and Kubernetes clusters.

## 3. Run the Container

Build the image and run it. Pass the required Azure DevOps configuration via environment variables:

```bash
docker run -d --name azp-agent \
  --privileged \
  -e AZP_URL="https://dev.azure.com/{your-organization}" \
  -e AZP_TOKEN="{your-pat-token}" \
  -e AZP_POOL="Docker-Pool" \
  your-agent-image:latest
```

!!! info "Important"

    The `--privileged` flag is required if the container needs to build other container images using Podman. This gives Podman the necessary access to the host kernel.

## 4. Push to a Container Registry

Once tested, tag and push your agent image to a secure registry (like Azure Container Registry - ACR) so it can be pulled by a Kubernetes cluster later.

!!! tip

    **References:**

    - [Run a self-hosted agent in Docker (Microsoft)](https://learn.microsoft.com/en-us/azure/devops/pipelines/agents/docker)
