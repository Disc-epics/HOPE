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

## Basic server setup
The site is on ECN, which has a pretty restricted environment to run in.
It uses apache to host all the content, with a hook into python using mod_python to run the django app.

This glue code is from the [tutorial on ecn](https://engineering.purdue.edu/ECN/Support/KB/Docs/ConfiguringDjango)
and can be found at `server/django.cgi`. This code is only every run on the server, which means it can be difficult to test.

Note that there have been modifications to the `django.cgi` file from the tutorial: namely porting to python 3 because it was python 2.

Apache knows to use `django.cgi` because of the `.htacces` file in the `public_html` directory of the server, which forwards all requests to `django.cgi`,
which in turn passes all requests to the django app.

The `django.cgi` file can really only be debugged on the server (unless you have your own apache instance installed); it is never run in the local setup.

### Deploying

To deploy, all that needs to happen is copy the python and various files over to the server.
In order to make this less painful than drag and drop, there is a script that does it 
for you in `scripts/deploy.py`. After this is run, the server should be updated. If things
don't work properly, you can always restart the server.

### Managing the server (restarting, access log, error log)

In order to manage the server ssh (you can use PuTTY on windows) into the templeton
ecn server:

```bash
ssh disc@templeton.ecn.purdue.edu
```

Then there are several commands available, including `errorlog`, `restart`, etc.
Use `help` to show all possibilities

### Adding dependencies

Because we don't have any sort of ssh access to ECN, any dependencies we want need to be copied over. This seems like a pain,
but actually is quite painless if you use the `scripts/add_dependency.py` script. Just run `python scripts/add_dependency.py pack==ver`,
and it will copy it all over for you. Note that it does not copy dependencies of the dependencies, so you may have to add them manually
via more calls to `add_dependency.py`. 

