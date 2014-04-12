SHELL := /bin/sh

LOCALPATH := $(CURDIR)
TESTPATH := $(LOCALPATH)/tests

.PHONY: test clean

test:
	nosetests -v --with-coverage --cover-package=ansible --cover-inclusive --cover-erase tests

# Clean build files
clean:
	find . -name "*.pyc" -print0 | xargs -0 rm -rf
	-rm -rf htmlcov
	-rm -rf .coverage
	-rm -rf build
	-rm -rf dist
	-rm -rf memorandi/*.egg-info
