#!/bin/bash

# shellcheck disable=SC2164
cd Client

pip3 install virtualenv
virtualenv venv -p python3.9
source venv/bin/activate

pip3 install -r requirements.txt

python3 client.py