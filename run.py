#!flask/bin/python

import logging
from logging.handlers import RotatingFileHandler

import functools, datetime
from flask import session, request

from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado import autoreload

from web import app

# set the secret key.  keep this really secret:
app.secret_key = '5xyDNnpGTxzHqD_ZjmBcFVpUr@7A6_xs'

if __name__ == '__main__':
	
	handler = RotatingFileHandler('info.log', maxBytes=10000, backupCount=1)
	handler.setLevel(logging.INFO)
	app.logger.addHandler(handler)
	
	http_server = HTTPServer(WSGIContainer(app))
	http_server.listen(5002)
	IOLoop.instance().start()