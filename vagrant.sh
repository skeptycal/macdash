#!/usr/bin/env bash
# -*- coding: utf-8 -*-
# Adjusted for macOS

(return 0 2>/dev/null) && exit 64 # script should not be 'sourced'

##############################################################################
# check prerequisite versions
unset PYTHONDONTWRITEBYTECODE
declare -i SET_DEBUG=1
declare -i PY_MAJ_VER=$(python --version 2>&1 | cut -d ' ' -f 2 | cut -d '.' -f 1)
declare PY_MIN_VER=$(python --version 2>&1 | cut -d ' ' -f 2 | cut -d '.' -f 2-3)
declare -i BREW_MAJ_VER=$(brew --version | tail -n 3 | head -n 1 | cut -d '.' -f 1 | cut -d ' ' -f 2)
declare BREW_VER=$(brew --version | tail -n 3 | head -n 1 | cut -d ' ' -f 2)
PYENV_LOADED=$PYENV_VIRTUALENV_INIT # value is 1 if venv is active
VENV_LOADED="$VIRTUAL_ENV"          # value is venv directory if venv is loaded

##############################################################################
# verbose information
if [ $SET_DEBUG == 1 ]; then
    echo
    echo "MacDash installation ..."
    echo "----------------------------------------------"
    echo "Python version (2.7 required):    ${PY_MAJ_VER}.${PY_MIN_VER}"
    echo "Homebrew version (2+ required):   $BREW_VER"
    echo
    echo "PYENV: $PYENV_LOADED"
    echo "VENV: $VIRTUAL_ENV"
    echo
    echo "----------------------------------------------"
fi

##############################################################################
# install Homebrew if needed
if [ $BREW_MAJ_VER -lt 2 ]; then
    echo "Homebrew 2+ is required. Using Ruby install ..."
    echo ''
    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
fi

if ! [[ $(which pipenv) ]]; then
    echo "Python 2 (2.7.16) and pipenv are required. Using Brew install ..."
    brew install pipenv pyenv pyenv-virtualenv pyenv-virtualenvwrapper >>/dev/null
    pyenv install 2.7.16
    pyenv rehash
    pyenv local system
    pyenv shell system
    pyenv global system
fi

eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
pyenv rehash
pyenv

exit
if [ $PIPENV_ACTIVE==1 ]; then
    echo 'pipenv shell active ...'
    python install -e .
    python setup.py develop
else
    # TODO only python 2.7 for now due to psdash ancestor
    pipenv install --python 2.7
    pipenv shell
fi

# previous Linux psdash installation
# apt-get update -y
# apt-get install -y build-essential python-dev python-setuptools
# cd /vagrant
