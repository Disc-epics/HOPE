# HOPE

## Prerequisites

The server configuration has python 3.4 and django 2.0.
This is because python 3.4 is the latest version of python installed on the ECN servers,
and django 2.0 is the lastest version that supports python 3.4. If this is installed on another server
with more up to date python versions, that can be updated.

### Getting a local development server to run

First install python 3.4+. On windows, go to the [python download page](https://www.python.org/downloads/)
and install it. Make sure to check the option to add it to the system path (unless you know what you're doing).

On linux or mac, use your system package manager or [brew](brew.sh) respectively.

Then, install the dependencies for the server. If you have other python projects on that machine, use
a [virtualenv](https://docs.python.org/3/library/venv.html). Otherwise, don't worry about it.

Then, from the `server` directory, run

```bash
pip install -r requirements.txt
```

To install django and other requirements.

Next, run the development server:

```bash
python ./server/manage.py runserver
```

## Basic setup
The site is on ECN, which has a pretty restricted environment to run in.
It uses apache to host all the content, with a hook into python using mod_python to run the django app.

This glue code is from the [tutorial on ecn](https://engineering.purdue.edu/ECN/Support/KB/Docs/ConfiguringDjango)
and can be found at `server/django.cgi`. This code is only every run on the server, which means it can be difficult to test.

