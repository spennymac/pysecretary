from __future__ import absolute_import

import os
import shutil

import nox

BLACK_PATHS = ("docs", "pysecretary", "tests", "noxfile.py", "setup.py")


def default(session):
    session.install(
        "pytest", "pytest-cov",
    )

    # Run py.test against the unit tests.
    session.run(
        "py.test",
        "--quiet",
        "--cov=pysecretary",
        "--cov=tests",
        "--cov-append",
        "--cov-config=.coveragerc",
        "--cov-report=",
        "--cov-fail-under=0",
        *session.posargs,
    )


@nox.session(python=["3.5", "3.6", "3.7", "3.8"])
def unit(session):
    """Run the unit test suite."""
    default(session)


@nox.session(python=["3.8"])
def lint(session):
    session.install("black")
    session.install("-e", ".")
    session.run("black", "--check", *BLACK_PATHS)


@nox.session(python=["3.8"])
def lint_setup_py(session):
    session.run("python", "setup.py", "check", "--strict")


@nox.session(python=["3.8"])
def blacken(session):
    session.install("black")
    session.run("black", *BLACK_PATHS)


@nox.session(python=["3.8"])
def docs(session):
    """Build the docs."""

    session.install("recommonmark", "sphinx", "sphinx_rtd_theme")
    session.install("-e", ".[all]")

    shutil.rmtree(os.path.join("docs", "_build"), ignore_errors=True)
    session.run(
        "sphinx-build",
        "-W",  # warnings as errors
        "-T",  # show full traceback on exception
        "-N",  # no colors
        "-b",
        "html",
        "-d",
        os.path.join("docs", "_build", "doctrees", ""),
        os.path.join("docs", ""),
        os.path.join("docs", "_build", "html", ""),
    )
