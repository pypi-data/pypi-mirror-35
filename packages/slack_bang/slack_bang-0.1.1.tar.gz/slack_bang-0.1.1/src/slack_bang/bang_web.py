# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import multiprocessing
import gunicorn.app.base

from gunicorn.six import iteritems

from slack_bang import web_config
from slack_bang.web.web_runner import app


def number_of_workers():
    try:
        return (multiprocessing.cpu_count() * 2) + 1 / 2
    except:
        return 1


class StandaloneApplication(gunicorn.app.base.BaseApplication):

    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super(StandaloneApplication, self).__init__()

    def load_config(self):
        config = dict([(key, value) for key, value in iteritems(self.options)
                       if key in self.cfg.settings and value is not None])
        for key, value in iteritems(config):
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application


def run_web():
    host = web_config.get('host', '127.0.0.1')
    port = web_config.get('port', '8300')

    options = {
        'bind': '%s:%s' % (host, port),
        'workers': number_of_workers()
    }
    StandaloneApplication(app, options).run()

if __name__ == '__main__':
    run_web()
