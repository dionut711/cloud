import entries
import location
import metrics

routes = dict()
routes['/entries'] = entries.do_GET
routes['/location'] = location.do_GET
routes['/logs'] = metrics.do_GET

def get_controller(path):
    for key in routes:
        if path.startswith(key):
            return routes[key]
    return None