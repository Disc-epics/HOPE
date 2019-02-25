#!/usr/bin/env python
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

    copy_dir(conn, 'earlybird', 'public_html')
    # for dp, dn, filenames in os.walk('earlybird'):
    #     try:
    #         conn.createDirectory('disc', os.path.join('public_html', dp))
    #     except:
    #         pass
    #     for name in filenames:
    #         if os.path.splitext(name)[1] != '.pyc':
    #             conn.storeFile('disc', os.path.join(
    #                 'public_html', dp, name), open(os.path.join(dp, name), 'rb'))
