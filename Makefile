# Makefile for running common development tasks

# Define all PHONY targets
.PHONY: all act audit bump clean dist docs docker_build lint setup setup test test_scheduled update_from_template

# Main target i.e. default sessions defined in noxfile.py
all:
	uv run nox

# Nox targets

## Call nox sessions passing parameters
nox-cmd = @if [ "$@" = "test" ]; then \
	if [ -n "$(filter 3.%,$(MAKECMDGOALS))" ]; then \
		uv run nox -s test -p $(filter 3.%,$(MAKECMDGOALS)); \
	elif [ -n "$(filter-out $@,$(MAKECMDGOALS))" ]; then \
		uv run nox -s $@ -- $(filter-out $@,$(MAKECMDGOALS)); \
	else \
		uv run nox -s $@; \
	fi; \
elif [ -n "$(filter-out $@,$(MAKECMDGOALS))" ]; then \
	uv run nox -s $@ -- $(filter-out $@,$(MAKECMDGOALS)); \
else \
	uv run nox -s $@; \
fi

## Individual Nox sessions
act audit bump dist docs lint setup test update_from_template:
	$(nox-cmd)

# Standalone targets

## Run tests marked as scheduled
test_scheduled:
	uv run nox -s test -p 3.11 -- -m scheduled

## Clean build artifacts and caches
clean:
	rm -rf .mypy_cache
	rm -rf .nox
	rm -rf .pytest_cache
	rm -rf .ruff_cache
	rm -rf .venv
	rm -rf dist
	rm -rf .coverage
	make -C docs clean
	rm -rf reports && mkdir -p reports && touch reports/.keep

## Build Docker image
docker_build:
	docker build -t brave-search-python-client .

# Special rule to catch any arguments (like patch, minor, major, pdf, Python versions, or x.y.z)
# This prevents "No rule to make target" errors when passing arguments to make commands
.PHONY: %
%:
	@:

# Help
help:
	@echo "🦁 Available targets for Brave Search Python Client (v$(shell test -f VERSION && cat VERSION || echo 'unknown version'))"
	@echo ""
	@echo "  act                 - Run GitHub actions locally via act"
	@echo "  all                 - Run all default nox sessions, i.e. lint, test, docs, audit"
	@echo "  audit               - Run security and license compliance audit"
	@echo "  bump patch|minor|major|x.y.z - Bump version"
	@echo "  clean               - Clean build artifacts and caches"
	@echo "  dist                - Build wheel and sdist into dist/"

	@echo "  docs [pdf]          - Build documentation (add pdf for PDF format)"
	@echo "  docker_build        - Build Docker image brave-search-python-client"
	@echo "  lint                - Run linting and formatting checks"
	@echo "  setup               - Setup development environment"
	@echo "  test [3.11|3.12|3.13] - Run tests (for specific Python version)"
	@echo "  test_scheduled		 - Run tests marked as scheduled with Python 3.11
	@echo "  update_from_template - Update from template using copier"
	@echo ""
	@echo "Built with love in Berlin 🐻"
