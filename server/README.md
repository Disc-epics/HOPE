# Earlybird alert system server

## Development setup

Requirements: Python 3.3+

The server is a flask app. It is suggested to use virtualenv to isolate the development
environment from the rest of the system:

Linux:
```bash
cd server
python -m venv venv
. ./venv/bin/activate
pip install flask
FLASK_APP=main.py flask run
```

Windows (assuming `python` and `pip` are in `PATH`):
```batch
cd server
python -m venv venv
venv\Scripts\activate
pip install flask
```
