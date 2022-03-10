# End-to-end Project Template

__Customised for `{{cookiecutter.project_name}}`__.

__Project Description:__ {{cookiecutter.description}}

This template that also serves as a guide was generated using the
following
[`cookiecutter`](https://cookiecutter.readthedocs.io/en/stable/)
template:
https://github.com/aimakerspace/ml-project-cookiecutter-gcp

This `mkdocs` site is for serving the contents of the end-to-end
guide in a more readable manner, as opposed to plain
Markdown views. The contents of this guide have been customised
according to the inputs provided upon generation of this repository
through the usage of [`cruft`](https://cruft.github.io/cruft/),
following instructions detailed
[here](https://github.com/aimakerspace/ml-project-cookiecutter-gcp/blob/master/README.md)
.

Inputs provided to `cookiecutter`/`cruft` for the generation of this
template:

- __`cookiecutter.project_name`:__ {{cookiecutter.project_name}}
- __`cookiecutter.description`:__ {{cookiecutter.description}}
- __`cookiecutter.repo_name`:__ {{cookiecutter.repo_name}}
- __`cookiecutter.src_package_name`:__ {{cookiecutter.src_package_name}}
- __`cookiecutter.src_package_name_short`:__ {{cookiecutter.src_package_name_short}}
- __`cookiecutter.gcp_project_id`:__ {{cookiecutter.gcp_project_id}}
- __`cookiecutter.author_name`:__ {{cookiecutter.author_name}}
- __`cookiecutter.open_source_license`:__ {{cookiecutter.open_source_license}}

There are __two separate guides__:

- __[Guide (User)](./guide-for-user/prerequisites):__ This guide is for the users of
  the MLOps platforms and toolings.
- __[Guide (Administrator)](./guide-for-admin/prerequisites):__ This guide is for
  the administrators and provisioners of the infrastructure required
  for setting up the components of the MLOps platforms and toolings.

## Overview For Guide (User)

- [Prerequisites](./guide-for-user/prerequisites)
- [Preface](./guide-for-user/preface)
- [MLOps Components & Platform](./guide-for-user/mlops-components-platform)
    - [Kubernetes](./guide-for-user/mlops-components-platform#kubernetes)
        - [`kubectl` Configuration for GKE](./guide-for-user/mlops-components-platform#kubectl-configuration-for-gke)
        - [Persistent Volumes](./guide-for-user/mlops-components-platform#persistent-volumes)
    - [Polyaxon](./guide-for-user/mlops-components-platform#polyaxon)
        - [Polyaxon Dashboard](./guide-for-user/mlops-components-platform#polyaxon-dashboard)
        - [Relevant Concepts](./guide-for-user/mlops-components-platform#relevant-concepts)
        - [Secrets & Credentials on Kubernetes](./guide-for-user/mlops-components-platform#secrets-credentials-on-kubernetes)
    - [Google Container Registry](./guide-for-user/mlops-components-platform#google-container-registry)
- [Development Environment](./guide-for-user/dev-env)
    - [VSCode](./guide-for-user/dev-env#vscode)
        - [Git from VSCode](./guide-for-user/dev-env#git-from-vscode)
    - [Jupyter Lab](./guide-for-user/dev-env#jupyter-lab)
    - [Using Docker within Polyaxon Services](./guide-for-user/dev-env#using-docker-within-polyaxon-services)
    - [Git Repository](./guide-for-user/dev-env#git-repository)
    - [Cloud SDK for Development Environment](./guide-for-user/dev-env#cloud-sdk-for-development-environment)
- [Virtual Environment](./guide-for-user/virtual-env)
- [Data Storage & Versioning](./guide-for-user/data-storage-versioning)
    - [Sample Data](./guide-for-user/data-storage-versioning#sample-data)
- [Job Orchestration](./guide-for-user/job-orchestration)
    - [Pipeline Configuration](./guide-for-user/job-orchestration#pipeline-configuration)
    - [Data Preparation & Preprocessing](./guide-for-user/job-orchestration#data-preparation-preprocessing)
    - [Model Training](./guide-for-user/job-orchestration#model-training)
        - [Experiment Tracking](./guide-for-user/job-orchestration#experiment-tracking)
        - [Container for Experiment Job](./guide-for-user/job-orchestration#container-for-experiment-job)
        - [Hyperparameter Tuning](./guide-for-user/job-orchestration#hyperparameter-tuning)
- [Deployment](./guide-for-user/deployment)
    - [Model Artifacts](./guide-for-user/deployment#model-artifacts)
    - [Model Serving (FastAPI)](./guide-for-user/deployment#model-serving-fastapi)
        - [Local Server](./guide-for-user/deployment#local-server)
        - [Docker Container](./guide-for-user/deployment#docker-container)
        - [Deploy to GKE](./guide-for-user/deployment#deploy-to-gke)
    - [Model Serving (Kapitan Scout)](./guide-for-user/deployment#model-serving-kapitan-scout)
- [Batch Inferencing](./guide-for-user/batch-inferencing)
- [Continuous Integration & Deployment](./guide-for-user/cicd)
- [Documentation](./guide-for-user/documentation)
    - [GitLab Pages](./guide-for-user/documentation#gitlab-pages)

## Overview for Guide (Administrator)

> Coming soon...

## Directory Tree

```
{{cookiecutter.repo_name}}
    ├── {{cookiecutter.repo_name}}-conda-env.yml
    │                   ^-  The `conda` environment file for reproducing
    │                       the project's development environment.
    ├── LICENSE         <-  The license this repository is to be
    │                       respected under. Can be absent due to
    │                       omission upon generation of repository.
    ├── README.md       <-  The top-level README containing the basic
    │                       guide for using the repository.
    ├── .gitlab-ci.yml  <-  YAML file for configuring instructions for
    │                       GitLab CI/CD.
    ├── .dockerignore   <-  File for specifying files or directories
    │                       to be ignored by Docker contexts.
    ├── .pylintrc       <-  Configurations for `pylint`.
    ├── .gitignore      <-  File for specifying files or directories
    │                       to be ignored by Git.
    ├── aisg-context    <-  Folders containing files and assets relevant
    │   │                   for works within the context of AISG's
    │   │                   development environments.
    │   ├── code-server <-  Directory containing the entry point script
    │   │                   for the VSCode server's Docker image.
    │   ├── jupyter     <-  Directory containing the entry point scripts
    │   │                   and config for the Jupyter server's Docker
    │   │                   image.
    │   ├── k8s         <-  Manifest files for spinning up Kubernetes
    │   │                   resources.
    │   └── polyaxon    <-  Specification files for services and jobs
    │                       to be executed by the Polyaxon server.
    ├── assets          <-  Screenshots and images.
    ├── conf            <-  Configuration files associated with the
    │                       various pipelines as well as for logging.
    ├── data            <-  Folder to contain any data for the various
    │                       pipelines. Ignored by Git except its
    │                       `.gitkeep` file.
    ├── docker          <-  Dockerfiles associated with the various
    │                       stages of the pipeline.
    ├── docs            <-  A default Sphinx project; see sphinx-doc.org
    │                       for details.
    ├── models          <-  Directory for trained and serialised models.
    ├── notebooks       <-  Jupyter notebooks. Naming convention is a
    │                       number (for ordering), the creator's
    │                       initials, and a short `-` delimited
    │                       description, e.g.
    │                       `1.0-jqp-initial-data-exploration`.
    ├── scripts         <-  Bash scripts for any parts of the pipelines.
    └── src             <-  Directory containing the source code and
        |                   packages for the project repository.
        |── {{cookiecutter.src_package_name}}
        |               ^-  Package containing modules for all pipelines
        |                   except deployment.
        |── {{cookiecutter.src_package_name}}_fastapi
        |               ^-  Package for deploying the predictive models
        |                   within a FastAPI server.
        └── tests       <-  Directory containing tests for the
                            repository's packages.
```

Reference(s):

- [Dockerfile reference - `.dockerignore`](https://docs.docker.com/engine/reference/builder/#dockerignore-file)
- [Atlassian's Tutorial on `.gitignore`](https://www.atlassian.com/git/tutorials/saving-changes/gitignore)
- [GitLab CI/CD Quickstart](https://docs.gitlab.com/ee/ci/quick_start/)
- [`pylint` Docs - Command-line Arguments and Configuration Files](https://pylint.pycqa.org/en/latest/user_guide/ide-integration.html?highlight=pylintrc#command-line-arguments-and-configuration-files)
