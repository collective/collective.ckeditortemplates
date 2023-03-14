#!/usr/bin/make
# pyenv is a requirement, with 2.7, 3.7 and 3.10 python versions, and virtualenv installed in each version
# plone parameter must be passed to create environment or after a make cleanall

SHELL=/bin/bash
plones=4.3 5.2 6.0
b_o=

ifeq (, $(shell which pyenv))
  $(error "pyenv command not found! Aborting")
endif

ifndef plone
  plone=$(shell [ -e .plone-version ] && cat .plone-version)
  b_o=-N
endif

ifndef python
ifeq ($(plone),4.3)
  python=2.7
endif
ifeq ($(plone),5.2)
  python=3.7
endif
ifeq ($(plone),6.0)
  python=3.10
endif
endif

all: buildout

.PHONY: help
help:
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n\nTargets:\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-10s\033[0m %s\n", $$1, $$2 }' $(MAKEFILE_LIST)

.python-version:  ## Setups pyenv version
	@pyenv local `pyenv versions |grep "  $(python)" |xargs`
	@echo "Local pyenv version is `cat .python-version`"
	@ if [[ `pyenv which virtualenv` != `pyenv prefix`* ]] ; then echo "You need to install virtualenv in `cat .python-version` pyenv python (pip install virtualenv)"; exit 1; fi

bin/buildout: .python-version  ## Setups environment
	virtualenv .
	./bin/pip install --upgrade pip
	./bin/pip install -r requirements-$(plone).txt
	@echo "$(plone)" > .plone-version

.PHONY: setup
setup: oneof-plone cleanall bin/buildout ## Setups environment

.PHONY: buildout
buildout: oneof-plone bin/buildout  ## Runs setup and buildout
	rm -f .installed.cfg .mr.developer.cfg
	bin/buildout -t 5 -c test-$(plone).cfg ${b_o}

.PHONY: cleanall
cleanall:  ## Cleans all installed buildout files
	rm -fr bin include lib local share develop-eggs downloads eggs parts .installed.cfg .mr.developer.cfg .python-version .plone-version pyvenv.cfg

.PHONY: which-python
which-python: oneof-plone  ## Displays versions information
	@echo "plone var = $(plone)"
	@echo "python var = $(python)"
	@echo "python env = `cat .python-version`"

.PHONY: vcr
vcr:  ## Shows requirements in checkversion-r.html
	@bin/versioncheck -rbo checkversion-r-$(plone).html test-$(plone).cfg

.PHONY: vcn
vcn:  ## Shows newer packages in checkversion-n.html
	@bin/versioncheck -npbo checkversion-n-$(plone).html test-$(plone).cfg

.PHONY: guard-%
guard-%:
	@ if [ "${${*}}" = "" ]; then echo "You must give a value for variable '$*' : like $*=xxx"; exit 1; fi

.PHONY: oneof-%
oneof-%:
	@ if ! echo "${${*}s}" | tr " " '\n' |grep -Fqx "${${*}}"; then echo "Invalid '$*' parameter ('${${*}}') : must be one of '${${*}s}'"; exit 1; fi
