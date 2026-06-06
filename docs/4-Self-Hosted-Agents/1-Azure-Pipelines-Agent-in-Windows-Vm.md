# Azure Pipelines Agent on a Windows VM

Running a self-hosted Azure Pipelines agent on a Windows Virtual Machine gives you complete control over the build environment, including installed software, hardware capabilities, and networking.

## 1. Create an Agent Pool

In Azure DevOps, agents are grouped into **Agent Pools**.

1. Go to **Project Settings** > **Agent pools**.
2. Click **Add pool**, select **Self-hosted**, name it (e.g., `Windows-Agent`), and grant permission to all pipelines.

## 2. Install the Agent on the VM

1. Remote Desktop (RDP) into your Azure Windows VM.
2. In the Azure DevOps Agent Pool UI, click **New agent** and download the Windows agent `.zip` file.
3. Extract the contents to a dedicated folder (e.g., `C:\agent`).

## 3. Configure the Agent

1. Open PowerShell as an Administrator and navigate to the agent folder.
2. Run the configuration script:

   ```powershell
   .\config.cmd
   ```

3. Follow the prompts:
   - **Server URL:** `https://dev.azure.com/{your-organization}`
   - **Authentication type:** Press Enter for PAT (Personal Access Token).
   - **PAT:** Paste a PAT that has **Agent Pools (Read & Manage)** scope.
   - **Agent Pool:** `Windows-Agent`
   - **Run as a service:** `Y` (Ensures the agent restarts automatically if the VM reboots).

## 4. Install Dependencies

A bare agent cannot run pipelines if the required tools are missing. For our Python + Docker workflow, install:

*   **Install Python:** Download and install the specific Python version your app needs (e.g., 3.12) from [python.org](https://www.python.org/downloads/). During install, tick **"Add Python to PATH"**.
*   **Install Git:** Required for the agent to check out your source code.
*   **Install Docker Desktop (optional):** Only needed if your pipeline builds container images. Configure it to use the WSL2 engine.
*   **Restart the Agent Service:** After installing new software, restart the Azure Pipelines Agent service in `services.msc` so it refreshes its PATH and detects the new tools (its "capabilities").

!!! tip

    For Python work, a **Linux** self-hosted agent is usually the smoother choice — Python tooling and most production targets run on Linux. The same `config` steps apply; you would run `./config.sh` instead of `.\config.cmd`. See the next chapters for [Docker](2-Azure-Pipelines-Agent-in-Docker-Container.md) and [Kubernetes](3-Azure-Pipelines-Agent-in-Kubernetes-Cluster.md) Linux agents.

!!! tip

    **References:**

    - [Deploy an Azure Pipelines agent on Windows (Microsoft)](https://learn.microsoft.com/en-us/azure/devops/pipelines/agents/windows-agent)