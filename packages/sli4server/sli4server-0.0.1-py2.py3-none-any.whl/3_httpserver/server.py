import socket
import threading
import socketserver
import io

from http.server import SimpleHTTPRequestHandler, HTTPServer,HTTPStatus

class ThreadedHTTPRequestHandler(SimpleHTTPRequestHandler):

    def do_GET(self):

        cur_thread = threading.current_thread()
        print(self.__dict__)
        f = io.BytesIO()
        enc = "UTF-8"
        encoded = ''.join(self.path).encode(enc)
        f.write(encoded)
        f.seek(0)

        path = self.translate_path(self.path)
        self.send_response(HTTPStatus.OK, self.path)
        ctype = self.guess_type(path)
        self.send_header("Content-type", "text/html; charset=%s" % enc)
        self.send_header("Content-Length", str(len(self.path)))
        self.end_headers()
        self.copyfile(f, self.wfile)

def run(server_class=HTTPServer, handler_class=ThreadedHTTPRequestHandler):
    server_address = ('', 9988)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

if __name__ == "__main__":
    run()

