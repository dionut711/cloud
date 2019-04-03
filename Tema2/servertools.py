import urllib

class Router:
    def __init__(self):
        self._handlers = dict()

    def handler(self, path):
        subpaths = path.split('/')
        for key, handler in self._handlers.items():
            if key == subpaths[1]:
                if isinstance(handler, Router):
                    return handler.handler(reconstruct_path(subpaths[2:]))
                else:
                    return handler
        return None
    
    def add(self, path, handler):
        self._handlers[path] = handler

class CollectionRouter(Router):
    def __init__(self, handler_collection, handler_entity):
        super().__init__()
        self.handler_collection = handler_collection
        self.handler_entity = handler_entity
    
    def handler(self, path):
        subpaths = path.split('/')
        if len(subpaths) == 1:
            return self.handler_collection
        if len(subpaths) == 2:
            return self.handler_entity

def reconstruct_path(subpaths):
    path = ""
    for subpath in subpaths:
        path += "/" + subpath
    return path

def last_subpath(path):
    res = urllib.parse.urlparse(path)
    return res.path.split('/')[-1]