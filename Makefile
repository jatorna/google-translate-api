SHELL=/bin/bash -o pipefail

.PHONY: lint
lint:
	@echo ">> Executing linter"
	@pylint --extension-pkg-whitelist='pydantic' backend
