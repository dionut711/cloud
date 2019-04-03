from controllers.generic.base import EntityServiceHandler
from servertools import last_subpath

class GetCollection(EntityServiceHandler):
    def handle(self, server):
        try:
            content = self.view.forward_str(self.service.get_all())
        except:
            server.send_response(500)
            server.end_headers()
            return

        server.send_response(200)
        server.send_header('Content-type','application/json')
        server.end_headers()
        server.wfile.write(content.encode())

class GetEntity(EntityServiceHandler):
    def handle(self, server):
        entity_id = last_subpath(server.path)

        try:
            data = self.service.get(entity_id)
            content = self.view.forward_str(data)
        except:
            server.send_response(500)
            server.end_headers()
            return

        if content:
            server.send_response(200)
            server.send_header('Content-type','application/json')
            server.end_headers()
            server.wfile.write(content.encode())
        else:
            server.send_response(404)
            server.end_headers()