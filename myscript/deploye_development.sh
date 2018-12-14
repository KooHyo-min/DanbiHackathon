#!/usr/bin/env bash

# Initialize
sudo apt -y update
sudo apt -y upgrade

# git
sudo apt install git
git config --global user.name $1
git config --global user.email $2
git config --global color.ui auto
git config --global core.quotepath off
git config --global credential.helper store

# required packages
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils libffi-dev

# pyenv
sudo apt install curl
curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
# .bashrc 에 하기 내용 추가
#export PATH="$HOME/.pyenv/bin:$PATH"
#eval "$(pyenv init -)"
#eval "$(pyenv virtualenv-init -)"
pyenv update

# virtualenv
PYTHON_VERSION=3.5.6
pyenv install $PYTHON_VERSION
pyenv virtualenv $PYTHON_VERSION DanbiHackathon
pyenv local DanbiHackathon

# pip
pip install --upgrade pip
pip install --upgrade setuptools

pip install flake8
pip install pygame
# https://files.pythonhosted.org/packages/ec/8c/acba4494370dd1f68af341a76084c4c1f10f1ca258a741ace4f526716935/pygame-1.9.4-cp35-cp35m-manylinux1_x86_64.whl

pip install SpeechRecognition
sudo apt install libasound-dev portaudio19-dev libportaudiocpp0
pip install --upgrade pyaudio
sudo apt-get install python-pyaudio python3-pyaudio

