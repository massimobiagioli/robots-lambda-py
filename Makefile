.PHONY: default test lint deploy logs
default: help ;

help:				## Show this help.
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

test: 				## Test
	python -m pytest

lint: 				## Lint
	python -m pyflakes src test

deploy: 			## Deploy
	sls deploy

logs: 				## Show logs
	sls -f get_all_robots logs
