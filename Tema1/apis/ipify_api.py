import urllib.request

api_link = "https://api.ipify.org"

class PublicIPService:
    def GetPublicIP(self):
        response = urllib.request.urlopen(api_link)
        return response.read().decode('utf-8')