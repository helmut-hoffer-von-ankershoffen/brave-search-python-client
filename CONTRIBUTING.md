# Contributing to brave-search-python-client

Thank you for considering contributing to brave-search-python-client!

## Setup

Clone this GitHub repository via ```git clone git@github.com:helmut-hoffer-von-ankershoffen/brave-search-python-client.git``` and change into the directory of your local starbridge repository: ```cd brave-search-python-client```

Install the dependencies:

### macOS

```shell
if ! command -v brew &> /dev/null; then # if Homebrew package manager not present ...
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" # ... install it
else
  which brew # ... otherwise inform where brew command was found
fi
# Install required tools if not present
which jq &> /dev/null || brew install jq
which xmllint &> /dev/null || brew install xmllint
which act &> /dev/null || brew install act
uv run pre-commit install             # install pre-commit hooks, see https://pre-commit.com/
```

### Linux

Notes:

- Not yet validated
- .github/workflows/test-and-report.yml might provide further information

```shell
sudo sudo apt install -y curl jq libxml2-utils gnupg2  # tooling
curl --proto '=https' --tlsv1.2 -sSf https://raw.githubusercontent.com/nektos/act/master/install.sh | sudo bash # act
uv run pre-commit install # see https://pre-commit.com/
```

## Code

```
src/brave_search_python_client/
├── __init__.py          # Package initialization
├── client.py            # Main client implementation
├── cli.py               # Command Line Interface
├── constants.py         # Constants
├── requests.py          # Pydantic models for requests
└── responses/           # Pydantic models for responses
tests/
├── client_test.py       # Client tests including response validation
├── requests_tests.py    # Tests for request validation
├── cli_test.py          # CLI tests
└── fixtures/            # Example responses
```

## Build

All build steps are defined in `noxfile.py`.

```shell
uv run nox
```

You can run individual build steps - called sessions in nox as follows:

```shell
uv run nox -s test      # run tests
uv run nox -s lint      # run formatting and linting
uv run nox -s audit     # run security and license audit, inc. sbom generation
```

## Running GitHub CI workflow locally

Notes:

- Workflow defined in .github/workflows/ci.yml
- Calls all build steps defined in noxfile.py

```shell
./github-action-run.sh
```

## Docker

```shell
docker build -t brave-search-python-client .
```

```shell
docker run --env BRAVE_SEARCH_API_KEY=YOUR_BRAVE_SEARCH_API_KEY brave-search-python-client --help
```

## Pull Request Guidelines

- **Pre-Commit Hooks:** We use pre-commit hooks to ensure code quality. Please install the pre-commit hooks by running `uv run pre-commit install`. This ensure all tests, linting etc. pass locally before you can commit.
- **Squash Commits:** Before submitting a pull request, please squash your commits into a single commit.
- **Branch Naming:** Use descriptive branch names like `feature/your-feature` or `fix/issue-number`.
- **Testing:** Ensure new features have appropriate test coverage.
- **Documentation:** Update documentation to reflect any changes or new features.
