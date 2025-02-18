#!/usr/bin/env python3
"""
Module to develop a simple API using Python with the `http.server` module.
"""


import http.server
import socketserver

PORT = 8000


class SubclassBaseHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    """
    Subclass of http.server.BaseHTTPRequestHandler.

    """

    def do_GET(self):
        """
        method to handle GET requests.
        """
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello, this is a simple API!")

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), SubclassBaseHTTPRequestHandler) as httpd:
        print("Server running on port", PORT)
        httpd.serve_forever()
