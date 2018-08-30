#!/usr/bin/python
# -*- coding:utf-8 -*-

from wsgiref.simple_server import make_server

port = 8000
host = ""

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'application/json')])
    return '{"msg":"running"}'

httpd = make_server(host, port, application)
print "Serving HTTP on port 8000..."

httpd.serve_forever()

