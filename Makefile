.PHONY: default test
default: help ;

help:				## Show this help.
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

test: 				## Test
	python -m pytest

lint: 				## Lint
	python -m pyflakes src test