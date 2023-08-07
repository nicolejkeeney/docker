# Docker for python projects
This repository contains files and instructions for setting up a docker container for python projects. It includes files for building a docker image with a few common geospatial packages, along with jupyter lab + notebook. The environment is built inside the docker image using either a `conda-lock` file, or a conda `environment.yml` and pip `requirements.txt` files. The repository also includes a handy-dandy Makefile for launching a JupyterLab instance from your local machine in the docker container. <br><br>
The repository author is grateful to the [Pangeo community](https://pangeo.io/) for its [open source repository](https://github.com/pangeo-data/pangeo-docker-images/tree/master) for building the pangeo docker images and extensive documentation on their construction. This repository is built off the pangeo docker workflow and recycles code from the Dockerfile for their [base image](https://github.com/pangeo-data/pangeo-docker-images/tree/master/base-image).<br><br>

## What is docker? 
[Docker](https://www.docker.com/) enables developers to create isolated development environments that can be shared across platforms, avoiding the frustrating issue of passing around conda or pip environments that work on some machines but not others. Docker is a particularly useful tool for developers in the geospatial data space, since many geospatial python packages have complex dependencies that can be challenging to install. <br><br>

## Using this repository 
This should all be relatively simply to set up, given that all the required files are included. You'll want to first make sure that you have the docker app on your local machine, which can be downloaded from [docker.com](https://www.docker.com/). Then, you'll need to clone this repository to your local machine. Finally, you just need to run the line `make local` from within the directory for this repo. <br><br>Running `make local` will trigger the Makefile to do the following: 
1) Build the docker image from the Dockerfile and environment file/s in the repo. The image will be named `geospatial-img`. **This step will only occur if you haven't built the image in a previous instance.**
2) Run JupyterLab from a containerized instance of the image `geospatial-img`.

### An important note on JupyterLab 
When you launch a JupyterLab instance from the docker container, the terminal output will print a link for you to open the JupyterLab in your browser. **You'll need to copy-paste this link into your web-browser; it will not automatically open for you.** Use the **bottom** link. See the screenshot below. 
![jupyterlab_link](https://github.com/nicolejkeeney/geo-py-docker/assets/66140951/fb4d75da-973f-4168-af30-ce6c39ec693f)

## Find an issue? 
The repository author is a self-taught programmer; some of the language in the README may be imperfect. While I've done my best, I don't have an in-depth understanding of docker. Sorry! Please open an [issue](https://github.com/nicolejkeeney/docker/issues) in GitHub, shoot me an email, or [open a PR](https://github.com/nicolejkeeney/geo-py-docker/pulls) to fix the language if you are inclined to do so (which would be much appreciated!). 
