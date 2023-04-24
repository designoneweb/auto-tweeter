@echo off

python -m venv venv
call venv\Scripts\activate.bat
python -m pip install -r requirements.txt
start "Flask App" /B python app.py
TIMEOUT /T 5
start "http://127.0.0.1:5000"
pause
call deactivate.bat
