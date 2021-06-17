Image Augumentation Project.

The project is a way to test github action for continous integration **for deployment** environment

A flask application which uses **gunicorn** for deployment is used.

PS: There was some sort of consideration in using either `waitress` and `gunicorn` since the later only support unix environment. However since we are using docker for our deployment, we can easily just use gunicorn _we have our own vm_