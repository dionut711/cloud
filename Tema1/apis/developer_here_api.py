import urllib.request
import json
import time

keys_path = "apis/keys.json"
api_link = "https://route.api.here.com/routing/7.2/calculateroute.json?app_id={YOUR_APP_ID}&app_code={YOUR_APP_CODE}&waypoint0=geo!{FROM_COORDS}&waypoint1=geo!{TO_COORDS}&mode=fastest;car;traffic:disabled"

class RouteInfo():
    def __init__(self, duration, distance):
        self.duration = duration
        self.distance = distance
        self.distance_string = "{:,} kms".format(distance // 1000)
        hours = duration // 3600
        mins = (duration % 3600) // 60
        self.duration_string = "{}h {}m".format(hours, mins)

class RoutingService:
    def GetRouteInfo(self, from_coords, to_coords):
        with open(keys_path, "r") as fd:
            keys = json.load(fd)
        app_id = keys["developer-here-id"]
        app_code = keys["developer-here-code"]

        link = api_link.format(YOUR_APP_CODE=app_code, YOUR_APP_ID=app_id, FROM_COORDS=from_coords, TO_COORDS=to_coords)
        try:
            response = urllib.request.urlopen(link)
            data = json.loads(response.read())
            summary = data["response"]["route"][0]["summary"]
            return RouteInfo(summary['baseTime'], summary['distance'])
        except Exception as e:
            return None
       
