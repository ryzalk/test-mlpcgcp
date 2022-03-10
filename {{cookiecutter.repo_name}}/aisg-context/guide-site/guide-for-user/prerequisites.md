# Prerequisites

Aside from an internet connection, you would need the following to
follow through with the guide:

- NUS Staff/Student account
- Google account with `@aisingapore.org`/`@aiap.sg` domains provisioned
  by AI Singapore
- PC with the following installed:
  - If your machine is with a Windows OS, you should use
    [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/about)
    to execute the GNU/Linux commands that is needed for some steps
  - Pulse Secure
    - Refer to [NUS IT eGuides](https://nusit.nus.edu.sg/eguides/)
      for installation guides.
  - Web browser
  - Terminal
  - Docker Engine
    - [System requirements for Windows](https://docs.docker.com/desktop/windows/install/)
  - [miniconda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html)
    (recommended) or [Anaconda](https://docs.anaconda.com/anaconda/install/index.html)
  - [Google Cloud SDK](https://cloud.google.com/sdk/docs/install)
  - [kubectl](https://kubernetes.io/docs/tasks/tools/),
    CLI for Kubernetes
  - [Helm](https://helm.sh/docs/intro/install/),
    CLI for Kubernetes' package manager
- Access to a project on
  [Google Cloud Platform](https://console.cloud.google.com)

## NUS VPN

Your credentials for your NUS Staff/Student account is needed to
login to NUS' VPN for access to the following:

- AI Singapore's GitLab instance
- NUS resources

In order to interact with remote Git repositories situated on
AI Singapore's GitLab instance (clone, push, fetch, etc.)
outside of NUS' network or GCP (for regions `asia-southeast1` and
`us-central1`), you would need to login to NUS' VPN.
