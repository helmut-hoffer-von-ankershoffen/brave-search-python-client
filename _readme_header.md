# 🦁 Brave Search Python Client

[![License](https://img.shields.io/github/license/helmut-hoffer-von-ankershoffen/brave-search-python-client?logo=opensourceinitiative&logoColor=3DA639&labelColor=414042&color=A41831)
](https://github.com/helmut-hoffer-von-ankershoffen/brave-search-python-client/blob/main/LICENSE)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/brave-search-python-client.svg?logo=python&color=204361&labelColor=1E2933)](https://github.com/helmut-hoffer-von-ankershoffen/brave-search-python-client/blob/main/noxfile.py)
[![CI](https://github.com/helmut-hoffer-von-ankershoffen/brave-search-python-client/actions/workflows/test-and-report.yml/badge.svg)](https://github.com/helmut-hoffer-von-ankershoffen/brave-search-python-client/actions/workflows/test-and-report.yml)
[![Read the Docs](https://img.shields.io/readthedocs/brave-search-python-client)](https://brave-search-python-client.readthedocs.io/en/latest/)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=helmut-hoffer-von-ankershoffen_brave-search-python-client&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=helmut-hoffer-von-ankershoffen_brave-search-python-client)
[![Security](https://sonarcloud.io/api/project_badges/measure?project=helmut-hoffer-von-ankershoffen_brave-search-python-client&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=helmut-hoffer-von-ankershoffen_brave-search-python-client)
[![Maintainability](https://sonarcloud.io/api/project_badges/measure?project=helmut-hoffer-von-ankershoffen_brave-search-python-client&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=helmut-hoffer-von-ankershoffen_brave-search-python-client)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=helmut-hoffer-von-ankershoffen_brave-search-python-client&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=helmut-hoffer-von-ankershoffen_brave-search-python-client)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=helmut-hoffer-von-ankershoffen_brave-search-python-client&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=helmut-hoffer-von-ankershoffen_brave-search-python-client)
[![CodeQL](https://github.com/helmut-hoffer-von-ankershoffen/brave-search-python-client/actions/workflows/codeql.yml/badge.svg)](https://github.com/helmut-hoffer-von-ankershoffen/brave-search-python-client/security/code-scanning)
[![Dependabot](https://img.shields.io/badge/dependabot-active-brightgreen?style=flat-square&logo=dependabot)](https://github.com/helmut-hoffer-von-ankershoffen/brave-search-python-client/security/dependabot)
[![Renovate enabled](https://img.shields.io/badge/renovate-enabled-brightgreen.svg)](https://renovatebot.com/)
[![Coverage](https://codecov.io/gh/helmut-hoffer-von-ankershoffen/brave-search-python-client/graph/badge.svg?token=SX34YRP30E)](https://codecov.io/gh/helmut-hoffer-von-ankershoffen/brave-search-python-client)
[![Ruff](https://img.shields.io/badge/style-Ruff-blue?color=D6FF65)](https://github.com/helmut-hoffer-von-ankershoffen/brave-search-python-client/blob/main/noxfile.py)
[![MyPy](https://img.shields.io/badge/mypy-checked-blue)](https://github.com/helmut-hoffer-von-ankershoffen/brave-search-python-client/blob/main/noxfile.py)
[![GitHub - Version](https://img.shields.io/github/v/release/helmut-hoffer-von-ankershoffen/brave-search-python-client?label=GitHub&style=flat&labelColor=1C2C2E&color=blue&logo=GitHub&logoColor=white)](https://github.com/helmut-hoffer-von-ankershoffen/brave-search-python-client/releases)
[![GitHub - Commits](https://img.shields.io/github/commit-activity/m/helmut-hoffer-von-ankershoffen/brave-search-python-client/main?label=commits&style=flat&labelColor=1C2C2E&color=blue&logo=GitHub&logoColor=white)](https://github.com/helmut-hoffer-von-ankershoffen/brave-search-python-client/commits/main/)
[![PyPI - Version](https://img.shields.io/pypi/v/brave-search-python-client.svg?label=PyPI&logo=pypi&logoColor=%23FFD243&labelColor=%230073B7&color=FDFDFD)](https://pypi.python.org/pypi/brave-search-python-client)
[![PyPI - Status](https://img.shields.io/pypi/status/brave-search-python-client?logo=pypi&logoColor=%23FFD243&labelColor=%230073B7&color=FDFDFD)](https://pypi.python.org/pypi/brave-search-python-client)
[![Docker - Version](https://img.shields.io/docker/v/helmuthva/brave-search-python-client?sort=semver&label=Docker&logo=docker&logoColor=white&labelColor=1354D4&color=10151B)](https://hub.docker.com/r/helmuthva/brave-search-python-client/tags)
[![Docker - Size](https://img.shields.io/docker/image-size/helmuthva/brave-search-python-client?sort=semver&arch=arm64&label=image&logo=docker&logoColor=white&labelColor=1354D4&color=10151B)](https://hub.docker.com/r/helmuthva/brave-search-python-client/)
[![Copier](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-orange.json)](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template)
[![Open in Dev Containers](https://img.shields.io/static/v1?label=Dev%20Containers&message=Open&color=blue&logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iI2ZmZiIgZD0iTTE3IDE2VjdsLTYgNU0yIDlWOGwxLTFoMWw0IDMgOC04aDFsNCAyIDEgMXYxNGwtMSAxLTQgMmgtMWwtOC04LTQgM0gzbC0xLTF2LTFsMy0zIi8+PC9zdmc+)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/helmut-hoffer-von-ankershoffen/brave-search-python-client)
[![Open in GitHub Codespaces](https://img.shields.io/static/v1?label=GitHub%20Codespaces&message=Open&color=blue&logo=github)](https://github.com/codespaces/new/helmut-hoffer-von-ankershoffen/brave-search-python-client)

<!---
[![ghcr.io - Version](https://ghcr-badge.egpl.dev/helmut-hoffer-von-ankershoffen/brave-search-python-client/tags?color=%2344cc11&ignore=0.0%2C0%2Clatest&n=3&label=ghcr.io&trim=)](https://github.com/helmut-hoffer-von-ankershoffen/brave-search-python-client/pkgs/container/brave-search-python-client)
[![ghcr.io - Sze](https://ghcr-badge.egpl.dev/helmut-hoffer-von-ankershoffen/brave-search-python-client/size?color=%2344cc11&tag=latest&label=size&trim=)](https://github.com/helmut-hoffer-von-ankershoffen/brave-search-python-client/pkgs/container/brave-search-python-client)
-->

> [!TIP]
> 📚 [Online documentation](https://brave-search-python-client.readthedocs.io/en/latest/) - 📖 [PDF Manual](https://brave-search-python-client.readthedocs.io/_/downloads/en/latest/pdf/)

> [!NOTE]
> 🧠 This project was scaffolded using the template [oe-python-template](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template) with [copier](https://copier.readthedocs.io/).

---
