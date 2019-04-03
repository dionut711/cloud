import urllib.request
import json
import socket

api_link = "http://ip-api.com/json/{query}"

class GeolocationService:
    def GetIPGeoLocation(self, ip):
        link = api_link.format(query=ip)
        data = json.loads(urllib.request.urlopen(link).read())
        return data

    def GetURLGeoLocation(self, url):
        name = url.split('//')[1].split('/')[0]
        ip = socket.gethostbyname(name)
        if ip:
            return self.GetIPGeoLocation(ip)
