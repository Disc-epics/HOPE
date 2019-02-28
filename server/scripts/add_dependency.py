#!/usr/bin/env python

import time
import urllib.request
import tempfile
from getpass import getpass
import sys
import subprocess
import os
from smb.SMBConnection import SMBConnection
from deploy_util import connect, copy_dir
import io

if __name__ != '__main__':
    exit(0)

if len(sys.argv) != 2:
    print("Unexpected number of arguments. Usage: {} PACKAGE_NAME[==VERSION]".format(
        sys.argv[0]))
    exit(1)

cgi_install = '''#!/usr/local/bin/python3.4
import os
os.system("bash -c 'pip3 install --target=deps --ignore-installed --no-deps --upgrade {} > error.txt'")
'''.format(sys.argv[1])

conn = connect()

conn.storeFile('disc', os.path.join(
    'public_html', 'django.cgi'), io.BytesIO(str.encode(cgi_install)))

try:
    contents = urllib.request.urlopen(
        "https://engineering.purdue.edu/earlybirdsystem").read()
except:
    pass

time.sleep(20)

conn.storeFile('disc', 'public_html/django.cgi', open('django.cgi', 'rb'))
