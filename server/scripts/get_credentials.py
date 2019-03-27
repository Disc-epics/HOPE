import os
import json

server_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


def get_cred(name):
    with open(os.path.join(server_dir, 'creds.json')) as f:
        creds = json.load(f)

        return creds[name]
