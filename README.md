# combine

Simple CLI to combine and sort arrays written in python

## Usage

Run the CLI without arguments to see usage and help information

The CLI can be run directly as a python script or by invoking a containerized version of this CLI that is published on Docker Hub

__EX:__

```bash
./combine.py [1,3,5] [6,4,2]
```

__EX:__

```bash
docker run mgauthiere/combine:latest [1,3,5] [6,4,2]
```

## Building

This project uses a completely automated CI/CD pipeline which runs on GitHub Actions

The Actions runner invokes the `pipeline` shell script which features the following stages:

1. Lint and Test
    - Checks the code using standard python static inspection tools and by running unit and end to end tests for the CLI in a containerized environment which makes dependency management very simple
2. Release
    - Implements the [semantic-release](https://github.com/semantic-release/semantic-release) tooling to analyze the repo's commit history to automatically determine what the project's next semantic version should be based on commit messages that follow the Angular Commit Message Conventions.
3. Deploy
    - Containerizes and publishes the combine CLI to Docker Hub, when the semantic-release tooling has determined that a new version should be published
