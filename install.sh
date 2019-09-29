#!/usr/bin/env bash
# -*- coding: utf-8 -*-
# Adjusted for macOS

(return 0 2>/dev/null) && exit 64 # script should not be 'sourced'

declare -i SET_DEBUG=1 # TODO debug verbose
##############################################################################
# check prerequisite versions
unset PYTHONDONTWRITEBYTECODE
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

##############################################################################
# install pipenv and python 2 if needed
if ! [[ $(which pipenv) ]]; then
    echo "Python 2 (2.7.16) and pipenv are required. Using Brew install ..."
    brew install pipenv pyenv pyenv-virtualenv pyenv-virtualenvwrapper >>/dev/null
    pyenv install 2.7.16
    pyenv rehash
    exec pipenv install --python 2.7
    [[ $VIRTUAL_ENV!='' ]] && exec pipenv shell
fi

##############################################################################
# pyenv can be picky ... init, rehash, set local, cd home x2, cd back here ...
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
pyenv rehash
pyenv local 2.7.16
OLD_PWD=$PWD
cd ~
cd ~
cd $OLD_PWD

##############################################################################
# setup repo
[[ $VIRTUAL_ENV != '' ]] && exec pipenv shell
[[ $SET_DEBUG -eq 1 ]] && echo "pipenv shell active: $VIRTUAL_ENV"
pipenv install -e .
[[ $VIRTUAL_ENV != '' ]] && exec pipenv shell

python setup.py develop

##############################################################################
# previous Linux psdash installation
# apt-get update -y
# apt-get install -y build-essential python-dev python-setuptools
# cd /vagrant
