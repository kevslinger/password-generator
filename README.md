# Random Password Generator Service

This service allows you to randomly generate passwords meeting your specifications, including the password length, between 1 and 200 characters, as well as whether or not to consider numbers, lowercase letters, uppercase letter, and special symbols in the generated password.
The service is built very efficiently, and you can generate as many passwords as you'd like.
Why not try it out! See [Getting Start](#getting-started) and follow the simple installation to run the service.

Workflow Diagram Here

## Getting Started

- [Random Password Generator Service](#random-password-generator-service)
  - [Getting Started](#getting-started)
  - [Install](#install)
    - [Install from Docker](#install-from-docker)
    - [Build from Source](#build-from-source)
  - [Deploy](#deploy)
  - [Usage](#usage)
    - [Running with Docker](#running-with-docker)
    - [Running from Source](#running-from-source)

## Install

There are two ways to install the password generator: from [Docker](https://www.docker.com) or by building the source code.

### Install from Docker 

This service has been packaged into a docker container! 
You can find it on the DockerHub at [kevslinger/password-generator](https://hub.docker.com/repository/docker/kevslinger/password-generator).
To download the container, please ensure you have docker installed on your machine.
Then, use the command

```bash
docker pull kevslinger/password-generator
```

### Build from Source

This service can also be built and ran locally without Docker using the provided source code.
First, download the code using

```bash
git clone git@github.com:kevslinger/password-generator.git
```

Then install the dependencies.
For instance, create a virtual environment and use pip3 by running the commands
```bash
cd password-generator
virtualenv venv -p 3.8
source venv/bin/activate
pip3 install -r requirements.txt
```

Now all required python dependencies have been included in the codebase.

## Deploy

If you edit the source code and would like to rebuild the Docker container to include your latest changes, run the command

```bash
docker build --tag kevslinger/password-generator .
```



## Usage

You can run the password generation service from the Docker container or from your local build of the source code.

### Running with Docker

To run the Docker container, you can use the following command
```bash
docker run --publish 8080:8080 kevslinger/password-generator
```

This will map the Docker container's port 8080 to your port 8080 and allow you to connect to the service at http://127.0.0.1:8080.

### Running from Source
After building the source code and installing the dependencies, run the following command

```bash
python3 app.py
```

This will launch the service at http://127.0.0.1:8080.
