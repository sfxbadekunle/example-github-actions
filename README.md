Sample project github integration

The project is a way to test github action for continous integration **for deployment** environment

A flask application which uses **gunicorn** for deployment is used.

PS: There was some sort of consideration in using either `waitress` and `gunicorn` since the later only support unix environment. However since we are using docker for our deployment, we can easily just use gunicorn _we have our own vm_

Running locally
`docker run -p 3000:3000 tonytunde2012/sampleflask`

Another approach to running this will be to deploy first time with `docker watchtower` so that for any update on the server we get an updated image right away.

I have added the docker-compose for this.


Observations and thinking:
Rather than manually tagging, using GitOps to do the labelling by tagging the commit.

Running multiple jobs in parallel to leverage github actions parallelism
Consider we have tasks for test and on multiple systems

Using Matrix workflow:
To support multiple configuration and test examples in parallel

Initially, let's just push to master and have our base deployment.

Second, let's use a `deploy` job name with the if conditinals so that we restrict our deployment ensuring that code test pass, send a pr to main and then push for deployment.

TASK, make github action such that deployment only happens on pr, test is done for all push

Handling failure of deployment and tests
-- We may need to send a notification in case a deployment failed or a build failed, we can do this with an email or slack notification of some other github addons. This makes our automation deployment even more robust (since we implement a quick feedback mechanism)

Why we need to seperate the jobs is to allow some more flexibility when building your automation and possible seperation of concerns when build environment starts getting complicated