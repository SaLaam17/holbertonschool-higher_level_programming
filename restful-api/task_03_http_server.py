#!/usr/bin/env python3
"""
Module to develop a simple API using Python with the `http.server` module.
"""


import http.server
import socketserver
import json

PORT = 8000


class SubclassBaseHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    """
    Subclass of http.server.BaseHTTPRequestHandler.

    """

    def do_GET(self):
        """
        method to handle GET requests.
        """
        if self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            data = {
                "name": "John", "age": 30, "city": "New York"
            }
            json_data = json.dumps(data)

            self.wfile.write((json_data).encode("utf-8"))

        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            info = {
                "version": "1.0", "description": "A simple API built with http.server"
            }
            json_info = json.dumps(info)

            self.wfile.write((json_info).encode("utf-8"))

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found!")


if __name__ == "__main__":
    with socketserver.TCPServer(
        ("", PORT),
        SubclassBaseHTTPRequestHandler
    ) as httpd:
        print("Server running on port", PORT)
        httpd.serve_forever()
