#!/usr/bin/python
import sys
import logging

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, "/var/www/annotation/")

from application.main import app as application

application.secret_key = 'sa@!@2ccjkiyu2@!#%&#e@!@'

if __name__ == '__main__':
    application.run()
