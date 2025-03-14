# Security Policy

## Reporting Security Issues

If you discover a security vulnerability in Brave Search Python Client, please report it by sending an email to helmuthva@googlemail.com.

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

- **Renovate Bot**: Automatically creates pull requests to update dependencies when new versions are available, with a focus on security patches.
- **GitHub Dependabot**: Monitors dependencies for known vulnerabilities and automatically creates pull requests to update them when security issues are found.
- **pip-audit**: Regularly scans Python dependencies for known vulnerabilities using data from the Python Advisory Database.

### 2. Dependency Compliance

- **pip-licenses**: Exports the licenses of all dependencies to ensure compliance with licensing requirements and avoid using components with problematic licenses.
- **cyclonedx-py**: Generates a Software Bill of Materials (SBOM) in SPDX format, listing all components and dependencies used in the project.

### 3. Static Code Analysis

- **SonarQube**: Performs comprehensive static code analysis to detect code quality issues, security vulnerabilities, and bugs.
- **GitHub CodeQL**: Analyzes code for common vulnerabilities and coding errors using GitHub's semantic code analysis engine.

### 4. Secret Detection

- **Yelp/detect-secrets**: Pre-commit hook and automated scanning to prevent accidental inclusion of secrets or sensitive information in the codebase.

## Security Best Practices

We follow these security best practices:
- Regular dependency updates
- Comprehensive test coverage
- Code review process for changes by external contributors
- Automated CI/CD pipelines including security checks
- Adherence to Python security best practices

## Security Compliance

For questions about security compliance or for more details about our security practices, please contact helmuthva@googlemail.com.
