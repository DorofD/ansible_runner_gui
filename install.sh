#!/bin/bash
# установка python 3.9
sudo apt update
sudo apt install python3.9
sudo apt install python3.9-venv
sudo apt install python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools
sudo apt install libpython3.9-dev
sudo apt-get install apt-transport-https
sudo apt-get update
# настройка окружения
python3.9 -m venv arg_env
source arg_env/bin/activate
pip install wheel
pip install -r requirements.txt
pip install uwsgi
mv .env.example .env
python init.py
deactivate
# установка node.js и сборка проекта
curl -fsSL https://deb.nodesource.com/setup_19.x | sudo -E bash - &&\
sudo apt-get install -y nodejs
npm init -y
npm install
npm run build
