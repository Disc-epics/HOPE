# HOPE

## Getting a local development server to run

It is *highly* recommended to use Linux or macOS as a development environment for this project.
On windows, you can use [windows subsystem for linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10).

### Acquiring the credentials

The database, twilio account, and other various things are password protected, and the passwords do not
live in this repository for safety reasons. So, all the credentials are stored in a JSON file, named
`creds.json`. This is in the DISC sharepoint foler and should be downloaded and put in the `server`
directory. No extra configuration should be necessary.

### Prerequisites


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

Some systems (usually linux and mac) may require you to use `python3` instead of `python`.

## Accessing the server files

To access the server files, on windows type `\\templeton.ecn.purdue.edu\disc\` into windows
explorer, and use the `disc` as the username and the disc ECN password found in `creds.json`.

On macOS/Linux, connect to `smb://templeton.ecn.purdue.edu/disc/` or 
`sftp://templeton.ecn.purdue.edu/web/groups/earlybirdsystem` with the same credentials.

However, it is suggested for ease and reproducability to update the server using the `./scripts/deploy.py`
script instead of manually copying files.

## Basic server setup
The site is on ECN, which has a pretty restricted environment to run in.
It uses apache to host all the content, with a hook into python using mod_python to run the django app.

This glue code is from the [tutorial on ecn](https://engineering.purdue.edu/ECN/Support/KB/Docs/ConfiguringDjango)
and can be found at `server/django.cgi`. This code is only every run on the server, which means it can be difficult to test.

The server configuration has python 3.4.
This is because python 3.4 is the latest version of python installed on the ECN servers,
and django 2.0 is the lastest version that supports python 3.4. If this is installed on another server
with more up to date python versions, that can be updated.

Note that there have been modifications to the `django.cgi` file from the tutorial: namely porting to python 3 because it was python 2, and setting some environment variables that are needed just on the server.

Apache knows to use `django.cgi` because of the `.htacces` file in the `public_html` directory of the server, which forwards all requests to `django.cgi`,
which in turn passes all requests to the django app.

The `django.cgi` file can really only be debugged on the server (unless you have your own apache instance installed); it is never run in the local setup.

### Deploying

To deploy, all that needs to happen is copy the python and various files over to the server.
In order to make this less painful than drag and drop, there is a script that does it 
for you in `scripts/deploy.py`. After this is run, the server should be updated. If things
don't work properly, you can always restart the server.

### Managing the server (restarting, access log, error log)

In order to manage the server, ssh (you can use PuTTY on windows) into the templeton
ecn server:

```bash
ssh disc@templeton.ecn.purdue.edu
```

Then there are several commands available, including `errorlog`, `restart`, etc.
Use `help` to show all possibilities

### Running a script on the server

As there is no ssh access to the server, it is extremely difficult to run scripts on the server
and get information about the server that is often very valuable (running processes, installed programs,
etc). However, from the server program you can run programs (using `os.system`) or similar.

There has been a script setup to automate this process, and it located in `./scripts/run_script_on_server.py`. It works by updating the `django.cgi` file with a simple script that just runs
a bash process with the script provided on the commandline. Example:

```bash
./scripts/run_script_on_sever.py 'ps aux > running_processes.txt'
```

Which will write `running_processes.txt` in the `public_html` folder.

### Adding dependencies

Because we don't have ssh access to the server, running commands is a pain, and the main reason we need to do that is
for adding dependencies. However, it can be done by editing the `django.cgi` script to run a bash script on the server.

There is a convenience script for this specificly:

```bash
./scritps/add_dependency.py twilio
```

Which edits the `django.cgi` script, does an http request so it gets ran, then copies back the regular `django.cgi`.
Yes, it's hacky, but it also works.

### Adding credentials

If a new service is installed that requiress a password, it is generally not considered good practice to
just put the password in the code. In order to make the process easier, a central store for credentials,
in `creds.json`, has been setup. It is avaialbe in the DISC team sharepoint, under project documentation.

In code, all the fields are availabe through `settings.CREDENTIALS`:

```python
from .settings import CREDENTIALS

...

pw = CREDENTIALS['MY_PW']
```

When you add a field to `creds.json`, make sure to re-upload it to the sharepoint, run 
`scripts/deploy.py` to copy it to the server, and tell your teammates to re-download `creds.json`

## Common errors

There are a few common errors that took a long time to solve and are avoidable.

### Links point to the ECN webpage instead of one of ours
Because the server isn't mounted in the root directory of a domain (`https://engineering.purdue.edu/earlybirdsystem), having a `<a href='/'> ... </a?>` will link to `https://engineering.purdue.edu/`.

To avoid this, you can either use relative urls (`../account`, as used in the login). If this isn't
an option, there is a variable, `settings.PREFIX` that is available from Django that you can use
in templates. The prefix is the path of the root directory, *including* the trailing slash.


### Syntax errors on the server that don't happen locally

These are a pain to debug, bug usually are some sort of dependency issue. See where the code is failing
from the backtrace, and lookup on [`pypi`](https://pypi.org/) what the minimum required python version
is for the version of the dependency you are using is. The server uses Python 3.4, so you may have to 
downgrade to an older version that supports Python 3.4.

Use the `./scripts/add_dependency.py` script to downgrade the library.
