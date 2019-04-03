from controllers.generic.base import EntityServiceHandler
from servertools import last_subpath

class DeleteEntity(EntityServiceHandler):
    def handle(self, server):
        entity_id = last_subpath(server.path)

        try:
            response = self.service.delete(entity_id)
        except:
            server.send_500()
            return

        if response['status_code'] == 200:
            self.send_200(server)
        elif response['status_code'] == 404:
            self.send_404(server)

class DeleteCollection(EntityServiceHandler):
    def handle(self, server):
        try:
            response = self.service.delete_all()
        except:
            self.send_500(server)
            return

        if response['status_code'] == 200:
            self.send_200(server)