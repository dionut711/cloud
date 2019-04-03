import services
import components
import urllib
import logs
import time

def do_GET(handler):
        handler.send_response(200)
        handler.send_header('Content-type','text/html')
        handler.end_headers()

        start = time.perf_counter()
        data_dict = get_location_json(handler)
        route_json = get_route_json(handler, data_dict['lat'], data_dict['lon'])
        latency = time.perf_counter() - start

        if route_json:
            data_dict.update(route_json)

        html = str(data_dict)
        handler.wfile.write(html.encode())

        to = time.localtime(time.time())
        data_dict['request_time'] = "{}:{}:{}".format(to.tm_hour, to.tm_min, to.tm_sec)
        data_dict['latency'] = str(latency)
        logs.add(data_dict)

def get_location_json(self):
    res = urllib.parse.urlparse(self.path)
    res = urllib.parse.parse_qs(res.query)
    url = res['url'][0]
    location_json = services.ipgeolocation_service.GetURLGeoLocation(url)
    location_json['api_ip'] = url
    return location_json

def get_route_json(self, lat, lon):
    my_ip = services.public_ip_service.GetPublicIP()
    my_location = services.ipgeolocation_service.GetIPGeoLocation(my_ip)
    from_coords = "{:.2f},{:.2f}".format(my_location['lat'], my_location['lon'])
    to_coords = "{:.2f},{:.2f}".format(lat, lon)

    route = services.routing_service.GetRouteInfo(from_coords, to_coords)
    if route:
        return {'distance':route.distance_string, 'duration':route.duration_string}
    else:
        return {'distance':'unreachable', 'duration':'unreachable'}