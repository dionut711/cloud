import http.server
import socketserver
import routing

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.do_REQUEST(routing.get_router)

    def do_POST(self):
        self.do_REQUEST(routing.post_router)

    def do_DELETE(self):
        self.do_REQUEST(routing.delete_router)

    def do_PUT(self):
        self.do_REQUEST(routing.put_router)

    def do_PATCH(self):
        self.do_REQUEST(routing.patch_router)

    def do_REQUEST(self, router):
        handler = router.handler(self.path)
        if handler:
            handler(self)
        else:
            self.do_404()

    def do_404(self):
        self.send_response(404)
        self.end_headers()

if __name__ == "__main__":
    PORT = 8080
    Handler = MyHandler

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()