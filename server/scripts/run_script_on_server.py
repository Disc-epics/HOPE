#!/usr/bin/env python

from deploy_util import connect
import time
import os
import io
import sys


def run_script(script, timeout=20):

    cgi_install = '''#!/usr/local/bin/python3.4
import os
os.system("bash -c '{}' &> error.txt")
    '''.format(script.replace("'", "\\'").replace('"', '\\"'))

    print(cgi_install)

    conn = connect()

    conn.storeFile('disc', os.path.join(
        'public_html', 'django.cgi'), io.BytesIO(str.encode(cgi_install)))

    try:
        contents = urllib.request.urlopen(
            "https://engineering.purdue.edu/earlybirdsystem").read()
    except:
        pass

    time.sleep(timeout)

    conn.storeFile('disc', 'public_html/django.cgi', open('django.cgi', 'rb'))


if __name__ == '__main__':

    if len(sys.argv) != 2:
        print('Usage: \'bash command\'')

    command = sys.argv[1]

    run_script(command)
