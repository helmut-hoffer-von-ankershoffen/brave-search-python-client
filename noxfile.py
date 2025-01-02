import json
from pathlib import Path

import nox

nox.options.reuse_existing_virtualenvs = True
nox.options.default_venv_backend = "uv"


def _setup_venv(session: nox.Session, all_extras=True) -> None:
    """Install dependencies for the given session using uv."""
    args = ["uv", "sync", "--frozen"]
    if all_extras:
        args.append("--all-extras")
    session.run_install(
        *args,
        env={
            "UV_PROJECT_ENVIRONMENT": session.virtualenv.location,
            "UV_PYTHON": str(session.python),
        },
    )


@nox.session(python=["3.11", "3.12", "3.13"])
def test(session: nox.Session):
    _setup_venv(session)
    session.run(
        "pytest",
        "--disable-warnings",
        "--junitxml=junit.xml",
        "-n",
        "auto",
    )


@nox.session(python=["3.13"])
def lint(session: nox.Session):
    _setup_venv(session)
    session.run("ruff", "check", ".")
    session.run(
        "ruff",
        "format",
        "--check",
        ".",
    )


@nox.session(python=["3.13"])
def audit(session: nox.Session):
    _setup_venv(session)
    session.run("pip-audit", "-f", "json", "-o", "vulnerabilities.json")
    session.run("jq", ".", "vulnerabilities.json", external=True)
    session.run("pip-licenses", "--format=json", "--output-file=licenses.json")
    session.run("jq", ".", "licenses.json", external=True)
    # Read and parse licenses.json
    licenses_data = json.loads(Path("licenses.json").read_text(encoding="utf-8"))

    licenses_inverted: dict[str, list[dict[str, str]]] = {}
    licenses_inverted = {}
    for pkg in licenses_data:
        license_name = pkg["License"]
        package_info = {"Name": pkg["Name"], "Version": pkg["Version"]}

        if license_name not in licenses_inverted:
            licenses_inverted[license_name] = []
        licenses_inverted[license_name].append(package_info)

    # Write inverted data
    Path("licenses-inverted.json").write_text(
        json.dumps(licenses_inverted, indent=2), encoding="utf-8"
    )
    session.run("jq", ".", "licenses-inverted.json", external=True)
    session.run("cyclonedx-py", "environment", "-o", "sbom.json")
    session.run("jq", ".", "sbom.json", external=True)


@nox.session(python=["3.13"])
def docs(session: nox.Session):
    _setup_venv(session)
    session.run("make", "-C", "docs", "html", external=True)
