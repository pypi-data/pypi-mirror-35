#! /usr/bin/env python
# encoding: utf-8
from __future__ import print_function, division, absolute_import

# Copyright © 2018 Uwe Schmitt <uwe.schmitt@id.ethz.ch>
from contextlib import contextmanager
from datetime import datetime

from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from threading import Thread

from .logger import logger, setup_logger, get_cmdline_logger


class _Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        from datapool import __version__

        message = dict(status="alive", version=__version__, started=str(datetime.now()))
        self.send_response(200)
        self.end_headers()
        self.wfile.write(bytes(json.dumps(message), "utf-8"))


class DataPoolHttpServer:
    def __init__(self, port=8000):
        self.port = port
        self.thread = None
        self.httpd = None

    def start(self):
        server_address = ("", self.port)
        httpd = HTTPServer(server_address, _Handler)
        thread = Thread(target=httpd.serve_forever)
        thread.start()
        self.thread = thread
        self.httpd = httpd
        logger().info("started web server")

    def stop(self):
        if self.thread is None or self.httpd is None:
            raise RuntimeError("you must start server first.")

        if not self.thread.isAlive():
            raise RuntimeError("something went wrong when starting webserver.")

        self.httpd.shutdown()
        self.thread.join()
        logger().info("web server shut down")


@contextmanager
def run_http_server_in_background(config_http_server, print_ok):
    port = config_http_server.port
    server = DataPoolHttpServer(port)
    print_ok("- start background http server on port {}".format(port))
    server.start()
    yield
    print_ok("- stop http server")
    server.stop()
    print_ok("- stopped http server")
