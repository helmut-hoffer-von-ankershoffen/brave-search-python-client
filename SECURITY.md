# Security Policy

## Reporting Security Issues

If you discover a security vulnerability in Brave Search Python Client, please [report it here](https://github.com/helmut-hoffer-von-ankershoffen/brave-search-python-client/security/advisories/new).

We take all security reports seriously. Upon receiving a security report, we will:
1. Confirm receipt of the vulnerability report
2. Investigate the issue
3. Work on a fix
4. Release a security update

## Supported Versions

We currently provide security updates for the latest minor version.

## Automated Security Analysis

Brave Search Python Client employs several automated tools to continuously monitor and improve security:

### 1. Dependency Vulnerability Scanning

- **GitHub Dependabot**: Monitors dependencies for known vulnerabilities and automatically creates pull requests to update them when security issues are found. [Dependendabot alerts](https://github.com/helmut-hoffer-von-ankershoffen/brave-search-python-client/security/dependabot) published.
- **Renovate Bot**: Automatically creates pull requests to update dependencies when new versions are available, with a focus on security patches. [Dependency Dashboard](https://github.com/helmut-hoffer-von-ankershoffen/brave-search-python-client/issues) published.
- **pip-audit**: Regularly scans Python dependencies for known vulnerabilities using data from the Python Advisory Database. `vulnerabilities.json` published [per release](https://github.com/helmut-hoffer-von-ankershoffen/brave-search-python-client/releases).

### 2. Dependency Compliance

- **cyclonedx-py**: Generates a Software Bill of Materials (SBOM) in SPDX format, listing all components and dependencies used in the project. `sbom.json` (SPDX format) published [per release](https://github.com/helmut-hoffer-von-ankershoffen/brave-search-python-client/releases).
- **pip-licenses**: Exports the licenses of all dependencies to ensure compliance with licensing requirements and avoid using components with problematic licenses. `licenses.csv`, `licenses.json` and `licenses_grouped.json` published [per release](https://github.com/helmut-hoffer-von-ankershoffen/brave-search-python-client/releases).

### 3. Static Code Analysis

- **GitHub CodeQL**: Analyzes code for common vulnerabilities and coding errors using GitHub's semantic code analysis engine. [Code scanning results](https://github.com/helmut-hoffer-von-ankershoffen/brave-search-python-client/security/code-scanning) published.
- **SonarQube**: Performs comprehensive static code analysis to detect code quality issues, security vulnerabilities, and bugs. [Security hotspots](https://sonarcloud.io/project/security_hotspots?id=helmut-hoffer-von-ankershoffen_brave-search-python-client) published.

### 4. Secret Detection
- **GitHub Secret scanning**: Automatically scans for secrets in the codebase and alerts if any are found. [Secret scanning alerts](https://github.com/helmut-hoffer-von-ankershoffen/brave-search-python-client/security/secret-scanning) published.
- **Yelp/detect-secrets**: Pre-commit hook and automated scanning to prevent accidental inclusion of secrets or sensitive information in commits. [Pre-Commit hook](https://github.com/helmut-hoffer-von-ankershoffen/brave-search-python-client/blob/main/.pre-commit-config.yaml) published.

## Security Best Practices

We follow these security best practices:
- Regular dependency updates
- Comprehensive test coverage
- Code review process for changes by external contributors
- Automated CI/CD pipelines including security checks
- Adherence to Python security best practices

We promote security awareness among contributors and users

- We indicate security as a priority in our
  [code style guide](CODE_STYLE.md), to be followed by human and agentic
  contributors as mandatory
- We publish our security posture in SECURITY.md (this document), encouraring
  users to report vulnerabilities.

## Security Compliance

For questions about security compliance or for more details about our security practices, please contact helmuthva@googlemail.com.
