# Data Storage & Versioning

So we now have our development environment. However, the data for us to
conduct EDA and predictive modeling on is nowhere in sight.

Since the context of this guide is within the Google Cloud Platform,
we will be making use of its
[Google Cloud Storage](https://cloud.google.com/storage)
service for remote and object storage.

In most cases, raw data for 100E projects provided by the project
sponsors are uploaded to GCS through AI Singapore's
in-house tool for uploading data: UDP. When data is uploaded to GCS
through UDP, a GCS bucket is populated with timestamped directories
containing whatever raw that was uploaded.

For example, assuming your project ID is `ai-proj-aut0`,
a GCS bucket with the same name `ai-proj-aut0` exists. The tree in the
bucket can look something like this:

```bash
.
└── ai-proj-aut0
    ├── 20211214_1109568/
    ├── 20211214_1110821/
    ├── 20211214_1448200/
    └── 20211214_1449172/
```

The subdirectories are timestamps indicative of the time that the raw
data was added to GCS. A question that follows is how do we get
the data into the persistent storage that's accessible by Polyaxon's
jobs and services? Well, let's go back to the VSCode environment to use
the integrated terminal.

From [this section](./dev-env#cloud-sdk-for-development-environment),
we've learned how to set up authorisation for `gcloud`
to use the service account
credentials we have attached to the service containers.
This means that we can use
[`gsutil`](https://cloud.google.com/storage/docs/gsutil)
to pull in data from a GCS bucket.

```bash
$ mkdir -p /polyaxon-v1-data/workspaces/<YOUR_NAME>/data/ai-proj-aut0 && cd "$_"
$ gsutil -m rsync -r gs://ai-proj-aut0 .
```

The `-m` flag is to utilise parallel synchronisation which would speed
things up and the `-r` concerns recursion through a bucket/directory.

Now, when a new set of raw data has been uploaded, a new subdirectory
will appear in the bucket. Say the tree now looks like the following:

```bash
.
└── ai-proj-aut0
    ├── 20211215_0952332/
    ├── 20211214_1109568/
    ├── 20211214_1110821/
    ├── 20211214_1448200/
    └── 20211214_1449172/
```

To retrieve that new set of raw data i.e. the folder `20211215_0952332`,
just run the same command in the relevant folder again:

```bash
$ cd /polyaxon-v1-data/workspaces/<YOUR_NAME>/data/ai-proj-aut0
$ gsutil -m rsync -r gs://ai-proj-aut0 .
```

The `gsutil` utility will synchronise the directory in the persistent
storage with the remote object storage/bucket.
With that said, __do not place your processed data directory within
this same directory containing all the raw data__ lest you'd lose
the processed data upon sychronisation. Let the directory for raw data
contain just raw data.

### Sample Data

While you may have your own project data to work with, for the purpose
of following through with this template guide, let's download
the sample data for the [problem statement](./preface#guides-problem-statement)
at hand.

__Note:__ The sample data for this guide's problem statement is made
accessible to the public. Hence any team or individual can download
it. It is highly likely that your data is not publicly accessible and
neither should it be, especially if it is a 100E project.

```bash
$ mkdir -p /polyaxon-v1-data/workspaces/<YOUR_NAME>/data/acl-movie-review-data-aisg && cd "$_"
$ gsutil -m rsync -r gs://acl-movie-review-data-aisg .
```

In the following section, we will work towards processing the raw data
and eventually training a sentiment classifier model.

Reference(s):

- [`gsutil` Reference - rsync](https://cloud.google.com/storage/docs/gsutil/commands/rsync)
