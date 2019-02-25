#!/usr/bin/env python

import tempfile
from getpass import getpass
import sys
import subprocess
import os
from smb.SMBConnection import SMBConnection
from deploy_util import connect, copy_dir

if __name__ != '__main__':
    exit(0)

if len(sys.argv) != 2:
    print("Unexpected number of arguments. Usage: {} PACKAGE_NAME[==VERSION]".format(
        sys.argv[0]))
    exit(1)


with tempfile.TemporaryDirectory() as dir:

    print("Using {} as the temp dir".format(dir))

    # run pip to get all the files
    completed = subprocess.run(['pip', 'install', '--target=.', '--ignore-installed',
                                '--only-binary=:all:', '--python-version=34', '--no-deps', '--upgrade', sys.argv[1]], cwd=dir)

    if completed.returncode != 0:
        print("Bad retcode from pip")
        exit(1)

    # copy all the files to the server
    conn = connect()

    foldername = sys.argv[1].partition('=')[0]

    copy_dir(conn, os.path.join(dir, foldername),
             os.path.join('public_html', 'deps', foldername))
