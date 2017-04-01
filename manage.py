#!/usr/bin/env python
# coding: utf-8

"""
    manage
    ~~~~~~

    Set of some useful management commands.

    :copyright: (c) 2015 by Roman Zaiev.
    :license: BSD, see LICENSE for more details.
"""

import subprocess
from flask.ext.script import Shell, Manager
from app import app
from base import models
from ext import db
from settings import BaseConfig
from datetime import datetime

manager = Manager(app)

@manager.command
def clean_pyc():
    """Removes all *.pyc files from the project folder"""
    clean_command = "find . -name *.pyc -delete".split()
    subprocess.call(clean_command)


@manager.command
def init_data():
    """Fish data for project"""
    db.drop_all()
    db.create_all()

    for e in BaseConfig.EVENT_BASE_BUNDLE :
        event = models.Event(e[0], e[1], e[2], e[3], e[4])
        event.save()
		
    for s in BaseConfig.SCHEDULE_BASE_BUNDLE :
        schedule = models.Schedule(int(s[0]), s[1], datetime.strptime(s[2] , '%Y-%m-%d'), datetime.strptime(s[3] , '%Y-%m-%d'))
        schedule.save()
    
    user = models.User(username='John Doe', email='john@doe.com', password='test')
    user.save()



manager.add_command('shell', Shell(make_context=lambda:{'app': app, 'db': db}))


if __name__ == '__main__':
    manager.run()
