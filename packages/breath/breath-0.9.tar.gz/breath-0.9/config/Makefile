VIRTUAL_ENV = virtualenv

PWD = $(shell pwd)
PACKAGE = breath
CLIENT = client
PY = $(VIRTUAL_ENV)/bin/python3
PIP = $(VIRTUAL_ENV)/bin/pip3

export WORKON_HOME := $(PY)
export PATH := $(WORKON_HOME):$(VIRTUAL_ENV)/bin:$(PATH)


.PHONY: clean clean-test clean-pyc clean-build docs help test
.DEFAULT_GOAL := help

NOW_DATE = $(shell date "+%Y-%m-%d %H:%M:%S")


define BROWSER_PYSCRIPT
import os, webbrowser, sys
try:
	from urllib import pathname2url
except:
	from urllib.request import pathname2url
webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT
BROWSER := python -c "$$BROWSER_PYSCRIPT"


define PRINT_HELP_PYSCRIPT
import re, sys
for line in sys.stdin:
	match = re.match(r'^### (.*) #', line)
	if match:
		target = match.groups()[0]
		print("\n%s" % (target))
	match = re.match(r'^([a-zA-Z0-9_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("  %-15s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT


help:
	@echo System info:
	@echo   - DATE_NOW: $(NOW_DATE)
	@echo   - WORKON_HOME: $(WORKON_HOME)
	@echo   - PACKAGE: $(PACKAGE)
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)
