# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## Requirements

- Python {{ cookiecutter.python_version }}
- [Poetry](https://python-poetry.org)

## Installation, Dependencies, and Packaging

Run the following command from the root directory of this project.

```bash
poetry install
```

The above command will create a python virtual environment in directory `.venv/`.

If you add/remove/modify the dependencies in `pyproject.toml`, then run
this command to update/generate `poetry.lock`:

```bash
poetry lock --no-update
```

Run the following to create a wheel file:

```bash
poetry build
```

This will create a wheel file in directory [dist/](dist/).

## Run type checking, linting, and tests

This project is using:
- [mypy](https://mypy.readthedocs.io) for type checking
- [pylint](https://pylint.readthedocs.io) for linting
- [isort](https://pycqa.github.io/isort/) and [black](https://github.com/psf/black) for code formatting
- [pytest](https://docs.pytest.org) for running the tests
- [taskipy](https://github.com/taskipy/taskipy) for task runner

Invoke the following command to run type checking:

```bash
poetry run task mypy
```

Run this command to run the tests:

```bash
poetry run task test
```

The above command will not generate the test coverage report. To generate the report, you can invoke:

```bash
poetry run task test_report
```

This will generate a test coverage report that can be accessed at [cover_html/index.html](cover_html/index.html).

You can invoke this command to lint the codes:

```bash
poetry run task lint
```

The codes can be formatted to a standard format by running:

```bash
poetry run task format
```

The type checking, linting, and code format checking can be run all together by invoking:

```bash
poetry run task all
```
