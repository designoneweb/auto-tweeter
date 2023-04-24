#!/bin/bash

python3 -m venv venv
source venv/bin/activate
python3 -m pip install -r requirements.txt
python3 app.py &
sleep 5
open "http://127.0.0.1:5000"
fg
deactivate
