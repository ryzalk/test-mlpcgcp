# Preface

## Repository Setup

This repository provides an end-to-end template for AI
Singapore's AI engineers to onboard their AI projects. This repository
was created using AI Singapore's
[`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/)
template located
[here](https://github.com/aimakerspace/ml-project-cookiecutter-gcp).
Instructions for generating this template is detailed in that
repository's `README.md`.

While this repository provides users with a set of boilerplates,
with this `README.md` document, you are presented with a linear guide on
how to use the boilerplates that are rendered when you generated this
repository using [`cruft`](https://cruft.github.io/cruft/).
You can follow along the guide but it will be tackling a simple problem
statement.
Once you've grasp what this template offers, you can deviate from it
and customise it to your needs.

Since we will be making use of this repository and the files
contained within it, __ensure that this repository is pushed to a
remote repository__.
Most probably you will be resorting to
[AI Singapore's GitLab instance](https://gitlab.aisingapore.net/) as
the remote.
Refer to
[here](https://docs.gitlab.com/ee/user/project/working_with_projects.html#create-a-project)
on creating a blank remote repository (or project in GitLab's term).
After creating the remote repository, retrieve the remote URL and push
the local repository to remote:

```bash
$ git init
$ git remote add origin <REMOTE_URL>
$ git add .
$ git commit -m "Initial commit."
$ git push -u origin master
```

## Guide's Problem Statement

For this guide, we will work towards building a predictive model that is
able to conduct sentiment classification for movie reviews.
The model is then to be deployed through a REST API and used for batch
inferencing as well.
The raw dataset to be used is made available for you to download;
instructions are detailed under
["Data Storage & Versioning"](./data-storage-versioning),
to be referred to later on.

## Google Cloud Platform (GCP) Projects

Each project in AI Singapore that requires the usage of GCP resources
would be provided with a
[GCP project](https://cloud.google.com/docs/overview#projects). Such
projects would be accessible through the
[GCP console](https://console.cloud.google.com/home) once you've logged
into your AI Singapore Google account. Projects are managed and
provisioned by AI Singapore's MLOps team. If you'd like to request for a
project to be created (or for any other enquiries as well), please
contact `mlops@aisingapore.org`.

### Authorisation

You can use GCP's [Cloud SDK](https://cloud.google.com/sdk) to interact
with the varying GCP services.
When you're using the SDK for the first time,
you are to provide authorisation using a user or service account. In AI
Singapore's context, unless your use case concerns some automation or
CI/CD pipelines, you will probably be using your user account
(i.e. Google accounts with AI Singapore domains such as
`@aisingapore.org` or `@aiap.sg`).
See [here](https://cloud.google.com/sdk/docs/authorizing) for more
information on authorising your SDK.

A simple command to authorise access:

```bash
$ gcloud auth login
```

To register `gcloud` for Docker so you can push to
Google Container Registry:

```bash
$ gcloud auth configure-docker
```

With your user account, you should have access to the following GCP
products/services:

- [Kubernetes Engine (GKE)](https://cloud.google.com/kubernetes-engine)
- [Cloud Storage (GCS)](https://cloud.google.com/storage)
- [Container Registry (GCR)](https://cloud.google.com/container-registry)
