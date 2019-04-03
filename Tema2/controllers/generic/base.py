class EntityServiceHandler:
    def __init__(self, service, view):
        self.service = service
        self.view = view
        
    def send_500(self, server):
        server.send_response(500)
        server.end_headers()

    def send_409(self, server):
        server.send_response(409)
        server.end_headers()

    def send_404(self, server):
        server.send_response(404)
        server.end_headers()

    def send_400(self, server):
        server.send_response(400)
        server.end_headers()

    def send_200(self, server):
        server.send_response(200)
        server.end_headers()