# halon-api
A Python wrapper for the API for Mail Transport Agent Halon.
The functions in the wrapper are described in [doc/functions.md](./doc/functions.md).

Please read [the original documentation](https://docs.halon.io/api) for
complete in depth documentation on function arguments and the data returned by the API.

The wrapper is available as a PyPI package [_halon-api_](https://pypi.org/project/halon-api/).

# Install
Install the PyPI package using _pip_: `pip install halon-api`

# How to use

```
from halon_api import HalonAPI

h = HalonAPI(
    "halon.example.com",
    "halon-user",
    "secret-password",
)

print("Halon software version:", h.get_software_version())
```

# Development
How to set up development environment.

## Setup virtual environment
* Make virtual python environment: `python -m venv .venv`
* Activate environment: `source .venv/bin/activate`
* Deactivate virtual environment (When done): `deactivate`

## Install software
* Install required packages: `pip install requirements.txt`
* Install required packages for development: `pip install requirements-dev.txt`
* Use _pre-commit_ to install git hook scripts: `pre-commit install`

## Build the PyPI package
How to build and install the PyPI package locally.
* Build the package: `python -m build`
* Install the package: `pip install dist/halon-api-x.y.z.tar.gz`

## Generate documentation
Automated documentation of API functions can be generated by _pydoc-markdown_.
It will update the file `doc/functions.md`.
* Generate markdown (from repo root): `pydoc-markdown doc/pydoc-markdown.yaml`
