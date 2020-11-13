# Run Mega-Linter locally to test your branch of code

If you want to test locally against the **Mega-Linter** to test your branch of code, you will need to complete the following:

- Clone your testing source code to your local environment
- Install Docker to your local environment
- Pull the container down
- Run the container
- Debug/Troubleshoot

## Install Docker to your local machine

You can follow the link below on how to install and configure **Docker** on your local machine

- [Docker Install Documentation](https://docs.docker.com/install/)

## Download the latest Mega-Linter Docker container

- Pull the latest **Docker** container down from **DockerHub**
  - `docker pull nvuillam/mega-linter:v4`
    Once the container has been downloaded to your local environment, you can then begin the process, or running the container against your codebase.

## Run the container Locally

- You can run the container locally with the following **Base** flags to run your code:
  - `docker run -v /path/to/local/codebase:/tmp/lint nvuillam/mega-linter`
    - To run against a single file you can use: `docker run -v /path/to/local/codebase/file:/tmp/lint/file nvuillam/mega-linter`
  - **NOTE:** If you want to override the `/tmp/lint` folder, you can set the `DEFAULT_WORKSPACE` environment variable to point to the folder you'd prefer to scan.

### Flags for running Locally

You can add as many **Additional** flags as needed, documented in [Configuration](index.md#Configuration)

### Example

```shell
git clone https://github.com/nvuillam/npm-groovy-lint.git
docker pull github/mega-linter:latest
docker run -e FILTER_REGEX_INCLUDE='(.*lib/.*)' -e FILTER_REGEX_EXCLUDE='(.*lib/example/.*)' -v ~/npm-groovy-lint:/tmp/lint nvuillam/mega-linter
```

## Troubleshooting

### Run container and gain access to the command line

If you need to run the container locally and gain access to its command line, you can run the following command:

- `docker run -it --entrypoint /bin/bash nvuillam/mega-linter`
- This will drop you in the command line of the docker container for any testing or troubleshooting that may be needed.

### Found issues

If you find a _bug_ or _issue_, please open a **GitHub** issue at: [nvuillam/mega-linter/issues](https://github.com/nvuillam/mega-linter/issues)
