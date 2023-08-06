from wsgiref.simple_server import make_server
from .. import config
from .common import guid
import sys
import os


class context:
    def __init__(self, environ, write):
        self.environ = environ
        self.write = write
        self.messages = None


class application:
    def __init__(self):
        self.app = None
        self.middlewares = []
        self.guid = guid

    def start(self):
        self._print_info()
        sys.path.insert(0, config["middleware"]["path"])
        for middleware in config["middleware"]["list"]:
            self.middleware(getattr(__import__(middleware), middleware)) # NOQA
        make_server('', config["port"], self._run).serve_forever()

    def middleware(self, middleware):
        self.middlewares.append(middleware)

    def _print_info(self):
        print("---------------------------------------------------")
        print(" port | {port} ".format(port=config["port"]))
        print(" url  | http://localhost:{port} ".format(port=config["port"]))
        print(" path | {path} ".format(path=os.getcwd()))
        print("---------------------------------------------------")

    def _run(self, environ, start_response):
        request = context(environ, None)
        response = context(environ, start_response)
        for middleware in self.middlewares:
            if not middleware(self, request, response, config):
                break
        return response.messages
