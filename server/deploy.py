#!/bin/env python
from smb.SMBConnection import SMBConnection
from getpass import getpass
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

if __name__ == '__main__':

    user = 'disc'
    pw = os.environ['DISC_PASSWORD']
    if not pw:
        pw = getpass('disc password: ')
    conn = SMBConnection(user, pw, 'login', 'templeton.ecn.purdue.edu/disc')

    connected = conn.connect('128.46.104.13')

    # copy them all
    conn.storeFile('disc', 'public_html/django.cgi', open('django.cgi','rb'))
    conn.storeFile('disc', 'public_html/manage.py', open('manage.py', 'rb'))

    for dp, dn, filenames in os.walk('earlybird'):
        try:
            conn.createDirectory('disc', os.path.join('public_html', dp))
        except:
            pass
        for name in filenames:
            if os.path.splitext(name)[1] != '.pyc':
                conn.storeFile('disc', os.path.join(
                    'public_html', dp, name), open(os.path.join(dp, name), 'rb'))
