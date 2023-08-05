# ci3

Continuous deployment for kubernetes (k8s) and gitlab.


# Table of Contents
1. [blog](#blog)
2. [use](#use)
3. [develop](#develop)

## blog

More articles on [Medium..](https://medium.com/kubic-ci)

## use

Prerequisites: **ci3** is written and tested in **python3** (linux or mac osx).

As a user you would probably do something like:

	pip install kubic-ci


The following should work w/o errors:

	kubic --help


To start a new project locally you would proceed with:

	kubic init


A typical deploy cycle is:

	kubic build && kubic push && kubic deploy -d hello

where *hello* is the name of your service and project.


### docker image

One can find a simple docker image inside the `docker` folder, which is suitable to be used by gitlab-runner, so that one has already ci3 preinstalled and can deploy to GKE.

The following will pull latest image from dockerhub and run it in your local docker

	docker run -it  kubic3/ci3:latest

Like this kubic-ci can be integrated into CI/CD cycle provided by [gitlab](https://docs.gitlab.com/ee/ci/yaml/).

## develop

### release

Before making a new release:

1. Make sure tests are passing (both locally and remotely on gitlab CI).
2. Increment version according to [semantic versioning](https://semver.org/).

In addition to bumping a new version in `ci3/version.py`, issuing a new release includes few more publishing (post-release) activities: 

1. Publish new python package `python setup.py sdist upload`
2. Build ad upload a new docker image (to avoid confusions, both docker image and python package share the same version). Check how it has been picked up on [dockerhub](https://hub.docker.com/r/kubic3/ci3/) and [microbadger](https://microbadger.com/images/kubic3/ci3).
3. Say something on socials about it ;)
