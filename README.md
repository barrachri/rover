# A Rover project

## Intro

This is a Rover, ready to be deployed to Mars.

Whether you like it or not, it can only move **forward**.

## Installation

**You need Python +3.6 available on your system**.


To create a new local environment
```bash
python3 -m venv .venv
```

to activate the env

```bash
# might be different depending on your shell
source .venv/bin/activate
```

to install the requirements (needed only for dev)

```
pip install -r requirements-dev.txt
```

We use [pre-commit](https://pre-commit.com/), to hook linters on `git commit` command

```bash
pre-commit install
```

## Running it locally

```python
>>> from rover import Rover
>>> position = (4, 2, "EAST")
>>> rover = Rover(name="C3PO", position=position)
>>> new_position = rover.send_command("FFF")
(7,2) EAST
```

## Run tests

You can use the Makefile

```bash
make test
```

or run

```bash
pytest --cov -v .
```
