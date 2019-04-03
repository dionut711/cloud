import http.server
import socketserver
import routing
import logs

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        controller = routing.get_controller(self.path)
        if controller:
            controller(self)
        else:
            return super().do_GET()

if __name__ == "__main__":
    PORT = 8080
    Handler = MyHandler

    logs.create()
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()