#!/usr/local/bin/python3.4
from os.path import isfile, join
from os import listdir
import os
import sys
WWW_PATH = os.path.dirname(os.path.abspath(__file__))
DJANGO_PROJECT_PATH = os.path.dirname(WWW_PATH)
sys.path.append(DJANGO_PROJECT_PATH + "/")
sys.path.append(DJANGO_PROJECT_PATH + "/earlybirdsystem")


def run_with_cgi(application):
    environ = dict(os.environ.items())
    environ['wsgi.input'] = sys.stdin
    environ['wsgi.errors'] = sys.stderr
    environ['wsgi.version'] = (1, 0)
    environ['wsgi.multithread'] = False
    environ['wsgi.multiprocess'] = True
    environ['wsgi.run_once'] = True
    if environ.get('HTTPS', 'off') in ('on', '1'):
        environ['wsgi.url_scheme'] = 'https'
    else:
        environ['wsgi.url_scheme'] = 'http'
    headers_set = []
    headers_sent = []

    def write(data):
        if not headers_set:
            raise AssertionError("write() before start_response()")
        elif not headers_sent:
            status, response_headers = headers_sent[:] = headers_set
            sys.stdout.write('Status: %s\r\n' % status)
            for header in response_headers:
                sys.stdout.write('%s: %s\r\n' % header)
            sys.stdout.write('\r\n')

        # apparently writing directly to the buffer is buffered, so we need to
        # flush first to make sure that the headers are sent before the data
        sys.stdout.flush()
        if isinstance(data, str):
            data = bytes(str, 'utf-8')
        sys.stdout.buffer.write(data)
        sys.stdout.flush()

    def start_response(status, response_headers, exc_info=None):
        if exc_info:
            try:
                if headers_sent:
                    raise exc_info[0](exc_info[1]).with_traceback(exc_info[2])
            finally:
                exc_info = None
        elif headers_set:
            raise AssertionError("Headers already set!")
        headers_set[:] = [status, response_headers]
        return write
    result = application(environ, start_response)
    try:
        for data in result:
            if data:
                write(data)
        if not headers_sent:
            write('')
    finally:
        if hasattr(result, 'close'):
            result.close()


try:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "earlybird.settings")
    os.environ.setdefault('EARLYBIRD_ON_ECN', '1')
    os.environ.setdefault('EALRYBIRD_CREDENTIALS_FILE',
                          '../private/creds.json')

    sys.path.append(os.path.join(WWW_PATH, 'deps'))
    import django.core.wsgi
    run_with_cgi(django.core.wsgi.get_wsgi_application())
except Exception as inst:
    print("Content-type: text/html\n\n")
    print(inst)
    raise inst
