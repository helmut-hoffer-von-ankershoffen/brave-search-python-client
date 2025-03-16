# Code Style

Author: Helmut Hoffer von Ankershoffen (@helmut-hoffer-von-ankershoffen ) - Status: Draft - Created: 2025-03-16 - Updated: 2025-03-16

This document describes the code style used in
[oe-python-template](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template)
and derivatives. It defines strict requirements to be followed by all
contributors - humans and agents - to ensure consistency and readability across
the codebase.

## Code

We favor readability and maintainability over cleverness and brevity.

- We always write code that is easy to read, understand, maintain, test,
  document, deploy, use, integrate, and extend.
- We always write code that is efficient and performant, but only if it does not
  sacrifice readability, maintainability, and testability.
- We always write code that is secure and does not introduce vulnerabilities.
- We always write code that is portable and does not introduce platform-specific
  dependencies.
- We always write code that is compatible with the Python version indicated in
  the .python-version file in the root of this repository.

## Naming

We believe that good names are essential for code readability and
maintainability. A good name is one that is descriptive, unambiguous, and
meaningful. It should convey the purpose and intent of the code it represents.

- We take extra care to find proper names for all identifiers, including
  variables, functions, classes, types, tests, modules, and packages. We prefer
  descriptive names that clearly indicate the purpose and functionality of the
  code.
- We avoid using abbreviations, acronyms, and jargon unless they are widely
  understood and accepted in the context of the code. We prefer full words and
  phrases that are easy to understand.
- We avoid using single-letter names, except for loop variables and iterators.
- We avoid using generic names like `data`, `info`, `temp`, `foo`, `bar`, etc.
  These names do not convey any meaning and make the code harder to read and
  understand.
- We avoid using names that are too long or too short. A good name should be
  concise but descriptive. It should be long enough to convey the purpose and
  intent of the code, but not so long that it becomes cumbersome to read and
  write.
- We avoid using names that are too similar or too different. A good name should
  be unique and distinct. It should not be confused with other names in the
  code. It should not be so different that it becomes hard to remember and
  recognize.

## Formatting

We use [ruff](https://github.com/astral-sh/ruff) to format Python code

- The ruff formatter adheres to the
  [Black](https://black.readthedocs.io/en/stable/the_black_code_style/current_style.html)
  code style which is [PEP 8](https://www.python.org/dev/peps/pep-0008/)
  compliant.
- The ruff formatter is configured to use a max line length of 120.
- The ruff formatter is called by the lint session of nox.

Beyond PEP 8 we adhere to the following naming conventions: We use the following
conventions for Python code:

- Class names: `PascalCase` - descriptive nouns that clearly indicate purpose.
- Function/method names: `snake_case` - verb phrases that describe actions.
- Variables/attributes: `snake_case` - descriptive nouns/noun phrases.
- Constants: `UPPER_SNAKE_CASE`.
- Private members: Prefix with single underscore `_private_attribute`.
- "True" private members: Prefix with double underscore `__truly_private`.
- Type variables: `CamelCase` with short, descriptive names (e.g., `T`, `KT`,
  `VT`).
- Boolean variables/functions: Prefix with `is_`, `has_`, `should_`, etc.
- Interface classes: Suffix with `Interface` or `Protocol`.

## Linting and type checking

We use [ruff](https://github.com/astral-sh/ruff) to lint Python code

- All linting rules are enabled except those explicitly disabled in
  pyproject.toml
- The ruff linter is called by the lint session of nox.

We use [mypy](https://mypy.readthedocs.io/) for static type checking of Python
code.

- mypy is configured to use the `strict` mode in pyproject.toml
- mypy is called by the lint session of nox.

## Documentation

We use docstrings to document the purpose of modules, classes, types, functions,
its parameters and returns

- We use Google style docstrings with typed Args and Returns.
- We comment complex code and algorithms to explain their purpose and
  functionality.
- We leave references with deep links in code to external documentation,
  standards, and specifications.

We provide an auto-generated OpenAPI specification and reference documentation.

We generate the final documentation using Sphinx and publish it to readthedocs.

- Generation of documentation is called by the docs session of nox

## Testing

We use [pytest](https://docs.pytest.org/en/stable/) for testing Python code.

- Tests are defined in the `tests/` directory
- We use pytest fixtures to set up test data and state
- We leverage several pytest plugins:
  - `pytest-asyncio` for testing async code
  - `pytest-cov` for coverage reporting
  - `pytest-docker` for integration tests with containers
  - `pytest-env` for environment variable management
  - `pytest-regressions` for regression testing
  - `pytest-xdist` for parallel test execution
- Test execution is automated through the nox test session which runs across the
  Python versions indicated in the `pyproject.toml`.

Our test coverage is measured using `pytest-cov` and reported in the CI
pipeline.

- We aim for 100% unit coverage on all code paths, including error handling and
  edge cases.
- We fail the CI if unit test coverage drops below 85%.

Apart from unit tests we provide integration tests and end-to-end tests:

- We smoke test as part of the CI/CD pipeline.
- We facilitate exploratory testing to ensure comprehensive coverage.
- We use `pytest-docker` for integration tests with containers.

## Error Handling

We use structured, explicit error handling that enables effective debugging and
monitoring:

- Use specific exception classes instead of generic ones.
- Include contextual information in exception messages.
- Log exceptions with appropriate severity levels and context.
- Gracefully degrade functionality when possible rather than failing completely.
- Use type hints to catch type errors at compile time rather than runtime.
- Design errors to be actionable for both users and developers.

## Logging

We log information to help with debugging and monitoring:

- Use structured logging with consistent fields across all log entries.
- Include correlation IDs for tracking requests across components.
- Log at appropriate levels (DEBUG, INFO, WARNING, ERROR, CRITICAL).
- Be mindful of PII and sensitive data in logs, using obfuscation where needed.
- Consider log volume and performance impact in production environments.

## Performance Considerations

We consider performance from the early design stage, not as an afterthought:

- Consider algorithmic complexity (Big O notation) for all operations.
- Prefer lazy evaluation when dealing with large datasets.
- Use appropriate data structures for specific access patterns.
- Be mindful of memory usage, especially for long-running processes.
- Consider profiling for critical paths and potential bottlenecks.
- Document performance characteristics and assumptions.
- Write benchmarks for performance-critical code.
- Design for horizontal scaling from the beginning.
- Use asynchronous operations appropriately for I/O-bound tasks.
- Consider caching strategies when appropriate.

## API Design

For both internal and external APIs we follow the principle of least surprise.

- We maintain backward compatibility whenever possible. If not possible we add a
  new major version of the API.
- Implement proper versioning for breaking changes.
- Document error conditions, return values, and side effects.
- Design for testability and mockability.
- Provide sensible defaults while allowing for configuration.
- Follow RESTful principles for HTTP APIs.
- Use consistent parameter ordering and naming.
- Implement proper validation with helpful error messages.
- Consider rate limiting and circuit breaking for external services.

## Security

We prioritize security at every stage of development to prevent vulnerabilities
and protect our users.

- Follow the principle of least privilege for all operations and access
  controls.
- Never store secrets (API keys, passwords, tokens) in code repositories.
  - Use environment variables or dedicated secret management services.
  - Code is checked via `detect-secrets` pre-commit hook to prevent accidental
    commits of secrets.

We implement proper input validation and sanitization for all external inputs
via [pydantic](https://pydantic-docs.helpmanual.io/):

- Validate inputs as early as possible in the data flow.

We handle authentication and authorization correctly:

- Use industry-standard authentication protocols (OAuth, JWT).
- Separate authentication from authorization logic.
- Implement proper session management with secure cookies.
- Protect against common vulnerabilities:
  - SQL Injection: Use parameterized queries or ORM frameworks.
  - XSS: Apply proper output encoding.
  - CSRF: Implement anti-CSRF tokens for state-changing operations.
  - SSRF: Validate and restrict URL destinations.
  - Command Injection: Avoid direct system command execution where possible.
- Implement proper error handling that doesn't leak sensitive information.
- Use secure defaults and fail closed (secure) rather than open (insecure).

We apply the principle of defense in depth:

- Don't rely on a single security control.
- Implement multiple layers of protection.
- Document security considerations in code and design documents.
- Write security-focused tests:
  - Test for security property violations.
  - Test error cases and edge conditions.
  - Test for resource exhaustion scenarios.
- Apply proper rate limiting and throttling to prevent abuse.
- For cryptographic operations:
  - Use established libraries, not custom implementations.
  - Follow current best practices for algorithm selection and key management.
  - Be aware of the limitations of cryptographic primitives.
- Regularly run security-focused static analysis tools as part of CI/CD:
  - CodeQL analysis (via GitHub Actions)
  - SonarCloud checks for security vulnerabilities

Our security posture is defined in [SECURITY.md](SECURITY.md).

## Dependency Management

We use modern dependency management practices:

- [uv](https://github.com/astral-sh/uv) for fast, reliable package installation
  and environment management
- Dependency version locking via uv.lock file
- Regular dependency auditing:
  - Security auditing via `pip-audit`
  - License compliance checks via `pip-licenses`
  - SBOM generation via `cyclonedx-py`

Dependency updates are automated via Dependabot and Renovate to ensure we stay
current with security patches.

## Versioning

We use [semantic versioning](https://semver.org/) for versioning our releases:

- MAJOR: Breaking changes
- MINOR: New features, non-breaking changes
- PATCH: Bug fixes, non-breaking changes

Our API versioning follows the same principles, with major versions indicated in
the URL (e.g., /api/v1/resource) and the full version provided as part of the
OpenAPI pecification.

## Conventional Commits

Our commit messages follow conventional commits format.

- We use 'feat','fix','chore','docs','style','refactor','test' prefixes and
  components in parentheses. E.g.
  `feat(api): add new endpoint for user registration`.

## Guidance for AI Pair Programming

When generating code with AI assistance:

- AI-generated code must follow all style guidelines in this document.
- Always review AI-generated code for correctness, security implications, and
  adherence to project patterns.
- Use AI to generate tests alongside implementation code.
- Request explanations for complex algorithms or patterns in the generated code.
- Remember that AI should augment, not replace, human judgment about code
  quality and design decisions.
