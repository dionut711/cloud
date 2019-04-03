import urllib.request
import json

class APIEntry:
    def __init__(self, name, link, description=None, category=None):
        self.name = name
        self.link = link
        self.description = description
        self.category = category

class APIsService:
    def GetAllEntries(self):
        contents = urllib.request.urlopen("https://api.publicapis.org/entries").read()
        data = json.loads(contents)
        entries = data['entries']
        return [APIEntry(entry['API'], entry['Link'], entry['Description'], entry['Category']) for entry in entries]
