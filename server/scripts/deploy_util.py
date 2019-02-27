from smb.SMBConnection import SMBConnection
from getpass import getpass
import os


def connect():
    user = 'disc'
    pw = os.environ.get('DISC_PASSWORD')
    if not pw:
        pw = getpass('disc password: ')
    conn = SMBConnection(user, pw, 'login', 'templeton.ecn.purdue.edu/disc')

    connected = conn.connect('128.46.104.13')
    return conn


def copy_dir(conn, dir, dest):

    print('Making directory {}'.format(dest))
    try:
        conn.createDirectory('disc', dest)
    except:
        pass
    for dp, dirs, filenames in os.walk(dir):
        for to_make in dirs:
            print('Making directory {}'.format(
                os.path.join(dest, to_make)))
            try:
                conn.createDirectory('disc', os.path.join(dest, dp, to_make))
            except:
                pass
        for name in filenames:
            if os.path.splitext(name)[1] != '.pyc':
                print("Copying {} to {}".format(os.path.join(
                    dp, name), os.path.join(dest, dp, name)))
                conn.storeFile('disc', os.path.join(
                    dest, dp, name), open(os.path.join(dp, name), 'rb'))
