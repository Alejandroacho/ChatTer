## Variables used in target commands
SHELL := /bin/bash

## Style to print targets in a nice format
STYLE = {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}


.PHONY: help
help:	## Show this help which show all the possible make targets and its description.
	@echo ""
	@echo "The following are the make targets you can use in this way 'make <target>':"
	@echo ""
	@awk ' BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / ${STYLE}' $(MAKEFILE_LIST)
	@echo ""
	@echo "You can interact with docker-compose using the following schema:"
	@echo "${DOCKER_FILE}"

.PHONY: install-requirements
install-requirements:	## Install the requirements for the chat-app
	@pip3 install -r requirements.txt

.PHONY: chat
chat:	## Open a shell in the chat-app container
	@python3 app/start.py
