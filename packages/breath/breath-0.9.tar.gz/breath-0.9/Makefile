include config/Makefile

#============================
### START DEVELOPING ########
#============================

setup: clean install ## execute setup script

setup-venv: clean-venv ## setup virtual environment
	python3.6 -m venv $(VIRTUAL_ENV)

install: setup-venv install-dep ## start virtual environment and install dev. requirements

install-dep: clean-py ## install development libs
	sudo apt-get install portaudio19-dev -y
	$(PIP) install --no-cache-dir -e .
	$(PIP) install setuptools --upgrade
	$(PIP) install --no-cache-dir -e ".[develop]"

#============================
### RUNNING #################
#============================

run-train: ## run package script
	$(PY) $(PACKAGE) train

run-start: ## run package script
	$(PY) $(PACKAGE) start

#============================
### BUILD ###################
#============================

build-requirements: ## freeze requirements
	$(PIP) freeze > requirements.txt


build-dist: clean-py ## builds source and wheel package
	$(PY) setup.py sdist
	$(PY) setup.py bdist_wheel
	ls -l dist

build-publish: build-dist ## publish to pip
	bumpversion patch --list
	twine upload dist/*

#============================
### CLEANING ################
#============================

clean: clean-venv clean-py # clean all setup files/folders

clean-venv: clean-py #clean virtual environment folder
	rm -fr $(VIRTUAL_ENV)

clean-logs: #clean logs directory
	rm -fr logs

clean-py: clean-build clean-pyc ## remove all Python files/folders

clean-build: ## remove build artifacts
	rm -fr build
	rm -fr dist
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +
	find . -name '*.tar.gz' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +
