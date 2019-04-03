from controllers.generic.service_handlers.get_handlers import *
from controllers.generic.service_handlers.post_handlers import *
from controllers.generic.service_handlers.delete_handlers import *
from controllers.generic.service_handlers.put_patch_handlers import PutEntity, PatchEntity

def method_not_allowed(server):
    server.send_response(405)
    server.end_headers()