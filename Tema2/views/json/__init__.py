import json
from views.json.user import User
from views.json.topic import Topic
from views.json.review import Review

class CollectionViewer:
    def __init__(self, instance_view):
        self.instance_view = instance_view

    def forward(self, data):
        result = list()
        for item in data:
            result.append(self.instance_view.forward(item))
        return result

    def forward_str(self, data):
        return json.dumps(self.forward(data))

    def backward(self, user):
        raise NotImplementedError

    def backward_str(self, user):
        raise NotImplementedError