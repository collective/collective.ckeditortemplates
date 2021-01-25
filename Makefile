#!/usr/bin/make
#

all: run

.PHONY: setup
setup:
	virtualenv-2.7 .
	./bin/pip install --upgrade pip
	./bin/pip install -r requirements.txt

.PHONY: buildout
buildout:
	if ! test -f bin/buildout;then make setup;fi
	bin/buildout

.PHONY: run
run:
	if ! test -f bin/instance;then make buildout;fi
	bin/instance fg

.PHONY: cleanall
cleanall:
	rm -fr lib bin/buildout develop-eggs downloads eggs parts .installed.cfg
