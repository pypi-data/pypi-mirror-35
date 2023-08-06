# SenseMAPI - Pythonic access to the OpenSenseMap API

[![pipeline status](https://gitlab.com/tue-umphy/python3-sensemapi/badges/master/pipeline.svg)](https://gitlab.com/tue-umphy/python3-sensemapi/commits/master) [![coverage report](https://gitlab.com/tue-umphy/co2mofetten/python3-sensemapi/badges/master/coverage.svg)](https://tue-umphy.gitlab.io/python3-sensemapi/coverage-report/)
[![documentation](https://img.shields.io/badge/docs-sphinx-brightgreen.svg)](https://tue-umphy.gitlab.io/python3-sensemapi/) [![PyPI](https://badge.fury.io/py/sensemapi.svg)](https://badge.fury.io/py/sensemapi)

`sensemapi` is a Python package to access the [OpenSenseMap
API](https://api.opensensemap.org).

## Installation

Install `sensemapi` via `pip3` from the repository root:

```bash
pip3 install --user .
```

## Development

The following might only be interesting for developers

### Tests

Since this is an API library, you need to specify an account to run the tests:

```bash
export SENSEMAP_EMAIL="user@email.com"
export SENSEMAP_PASSWORD="5uP3rP45sW0Rd"
```

You may also specifiy this sensitive data in a file which can then be
`source`d.

To run the test suite, run from the repository root

```bash
./setup.py test
```

To get a test coverage, run

```bash
make coverage
```
