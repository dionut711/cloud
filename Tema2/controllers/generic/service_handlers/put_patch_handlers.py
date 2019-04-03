from controllers.generic.base import EntityServiceHandler
from servertools import last_subpath

class UpdateEntity(EntityServiceHandler):
    def __init__(self, service, view, require_all):
        super().__init__(service, view)
        self.require_all = require_all

    def handle(self, server):
        try:
            content_length = int(server.headers.get('Content-Length'))
            content = server.rfile.read(content_length)
            data = self.view.backward_str(content, require_all=self.require_all)
            instance_id = last_subpath(server.path)
        except:
            self.send_400(server)
            return

        try:
            response = self.service.update(data, instance_id=instance_id)
        except:
            self.send_500(server)
            return

        if response['status_code'] == 400:
            self.send_400(server)
        elif response['status_code'] == 200:
            self.send_200(server)

class PatchEntity(UpdateEntity):
    def __init__(self, service, view):
        super().__init__(service, view, require_all=False)

class PutEntity(UpdateEntity):
    def __init__(self, service, view):
        super().__init__(service, view, require_all=True)
