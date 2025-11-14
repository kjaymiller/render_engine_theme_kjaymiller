import nox
import os

# Test against these Python versions
PYTHON_VERSIONS = ["3.11", "3.12", "3.13", "3.14"]

# Use pyenv for locating Python interpreters
os.environ["PYENV_VERSION"] = "3.11:3.12:3.13:3.14"
nox.options.pythons = PYTHON_VERSIONS
nox.options.reuse_existing_virtualenvs = True


@nox.session(python=PYTHON_VERSIONS)
def test(session: nox.Session) -> None:
    """Run tests with pytest."""
    session.run("uv", "pip", "install", "-e", ".[dev]", external=True)
    session.run("pytest", "tests/", "-v")


@nox.session(python=PYTHON_VERSIONS)
def lint(session: nox.Session) -> None:
    """Run linting with ruff."""
    session.run("uv", "pip", "install", "-e", ".[dev]", external=True)
    session.run("ruff", "check", "src", "tests")


@nox.session(python=PYTHON_VERSIONS)
def check(session: nox.Session) -> None:
    """Run both linting and tests."""
    session.run("uv", "pip", "install", "-e", ".[dev]", external=True)
    session.run("ruff", "check", "src", "tests")
    session.run("pytest", "tests/", "-v")
