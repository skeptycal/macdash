#!/bin/sh
# Adjusted for macOS

# apt-get update -y
# apt-get install -y build-essential python-dev python-setuptools
# cd /vagrant
pipenv install -e .
python setup.py develop
