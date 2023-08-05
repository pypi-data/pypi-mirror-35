import os
import importlib

import izaber
from izaber import config, app_config, autoloader
from izaber.startup import request_initialize, initializer
from izaber.log import log
from izaber.paths import paths

import flask


autoloader.add_prefix('izaber.flask')

CONFIG_BASE = """
default:
    debug: true
    flask:
        host: 127.0.0.1
        port: 5000
        secret_key: 'correctbatteryhorsestaple'

"""

class IZaberFlask(flask.Flask):

    allowed_protocol = None

    def __init__(self,*args,**kwargs):
        # By default the static_folder and static_url_path point
        # to this module's location.
        # By setting it to None, it will not automatically create the
        # /static/ to the local static folder allowing us to to
        # override it later on
        # We want to create something like an empty container
        # app to start worth so we can load all components as
        # blueprint entries
        kwargs.setdefault('static_folder',None)
        kwargs.setdefault('static_url_path',None)
        super(IZaberFlask,self).__init__(*args,**kwargs)
        self.allowed_protocol = None

    def app_protocol(self,path_info):
        return self.allowed_protocol

    def run(self, host=None, port=None, debug=None, **options):
        if host is None:
            host = config.flask.host
        if port is None:
            port = config.flask.port
        if debug is None:
            debug = config.debug
        super(IZaberFlask,self).run(
                                    host,
                                    port,
                                    debug,
                                    **options
                                )

app = IZaberFlask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@initializer('flask')
def load_config(**kwargs):
    request_initialize('config',**kwargs)
    request_initialize('logging',**kwargs)
    config.config_amend_(CONFIG_BASE)

    app.secret_key = config.flask.secret_key


