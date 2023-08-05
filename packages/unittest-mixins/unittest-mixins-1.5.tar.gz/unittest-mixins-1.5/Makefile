# Licensed under the Apache License: http://www.apache.org/licenses/LICENSE-2.0
# For details: https://github.com/nedbat/unittest-mixins/blob/master/NOTICE.txt

# Makefile for unittest_mixing

default:
	@echo "* No default action *"

test:
	tox

clean:
	-rm -rf *.egg-info
	-rm -rf build dist
	-rm -f *.pyc */*.pyc */*/*.pyc */*/*/*.pyc */*/*/*/*.pyc */*/*/*/*/*.pyc
	-rm -f *.pyo */*.pyo */*/*.pyo */*/*/*.pyo */*/*/*/*.pyo */*/*/*/*/*.pyo
	-rm -f *.bak */*.bak */*/*.bak */*/*/*.bak */*/*/*/*.bak */*/*/*/*/*.bak
	-rm -rf __pycache__ */__pycache__ */*/__pycache__ */*/*/__pycache__ */*/*/*/__pycache__ */*/*/*/*/__pycache__
	-rm -f MANIFEST
	-rm -f .coverage .coverage.* coverage.xml
	-rm -rf htmlcov
	-rm -f setuptools-*.egg distribute-*.egg distribute-*.tar.gz

sterile: clean
	-rm -rf .tox*
	-rm -rf .pytest_cache

smoke:
	tox -e py27

SDIST_CMD = python setup.py sdist --formats=gztar

kit:
	$(SDIST_CMD)

kit_upload:
	twine upload dist/*
