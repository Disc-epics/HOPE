#!/usr/bin/env python3
from smb.SMBConnection import SMBConnection
import os
from deploy_util import connect, copy_dir

# change directory to ../
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

if __name__ == '__main__':

    conn = connect()

    # copy them all
    conn.storeFile('disc', 'public_html/django.cgi', open('django.cgi', 'rb'))
    conn.storeFile('disc', 'public_html/manage.py', open('manage.py', 'rb'))
    conn.storeFile('disc', 'public_html/process_tasks.sh', open('process_tasks.sh', 'rb'))
    conn.storeFile('disc', 'private/creds.json', open('creds.json', 'rb'))

    copy_dir(conn, 'earlybird', 'public_html')
