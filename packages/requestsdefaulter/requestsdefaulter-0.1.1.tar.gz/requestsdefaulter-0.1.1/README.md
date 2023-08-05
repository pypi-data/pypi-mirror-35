# Requests Defaulter

Small library to set default headers in requests

Currently there's no easy way to set default headers in requests. This
patches the requests library to enable default headers to be set across
the board.

## Using this library

You can install this library from pypi. 

To do this using [pipenv](https://docs.pipenv.org/) run:

```
pipenv install requestsdefaulter
```

You can then set default headers in requests by running

```python
import requestsdefaulter

def default_header_provider():
    return { "X-Your-Header": "Contents Of Header"}

requestsdefaulter.default_headers(default_header_provider)
```

And make your request as normal

```python
import requests

requests.get("https://example.com")
```

And your request will contain the header

## Developing

These instructions will get you a copy of the project up and running.

### Prerequisites

This project uses [pipenv](https://docs.pipenv.org/).

It expects Python 3.6

### Installing

To install the dependencies of this library run

```shell
$ pipenv install --dev                                                                                                                                                                                                              master ✱ ➜ ◼
Installing dependencies from Pipfile.lock (f97fb9)…
  🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 11/11 — 00:00:01
To activate this project's virtualenv, run the following:
 $ pipenv shell
```

## Running the tests

To run all the tests simply run

```shell
make test
```

### Behavioural Tests

We use behave to test the library to run the tests run

```shell
pipenv run behave
```

### Security Check

This will check against PEP 508 and for security vulnerabilities in dependencies

```shell
pipenv check
```

### Coding Style Checks

Compare the code to pep8

```
pipenv run flake8
```

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
