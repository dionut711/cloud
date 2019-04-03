from controllers.generic.base import EntityServiceHandler
from servertools import last_subpath

class PostEntity(EntityServiceHandler):
    def __init__(self, service, view, auto_id=False):
        super().__init__(service, view)
        self.auto_id = auto_id

    def send_201(self, server, data, resource_id):
        server.send_response(201)
        server.send_header('Location', server.path + '/' + str(resource_id))
        server.send_header('Content-type','application/json')
        server.end_headers()

        content = self.view.forward_str(data)
        server.wfile.write(content.encode())

    def handle(self, server):
        try:
            content_length = int(server.headers.get('Content-Length'))
            content = server.rfile.read(content_length)
            data = self.view.backward_str(content)
            instance_id = last_subpath(server.path) if not self.auto_id else None
        except:
            self.send_400(server)
            return

        try:
            response = self.service.insert(data, instance_id=instance_id)
        except:
            self.send_500(server)
            return

        if response['status_code'] == 409:
            self.send_409(server)
        elif response['status_code'] == 201:
            if self.auto_id:
                self.send_201(server, response['content'], str(response['id']))
            else:
                self.send_404(server)
