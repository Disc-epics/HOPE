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
from run_script_on_server import run_script
import io

if __name__ != '__main__':
    exit(0)

if len(sys.argv) != 2:
    print("Unexpected number of arguments. Usage: {} PACKAGE_NAME[==VERSION]".format(
        sys.argv[0]))
    exit(1)


script = 'pip3 install --target=deps --ignore-installed --no-deps --upgrade {} > error.txt'.format(
    sys.argv[1])

run_script(script)
