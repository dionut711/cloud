import json
import model.topic

class Topic:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

    def forward(self, topic):
        result = dict()
        result[self.id] = topic.id
        result[self.name] = topic.name
        result[self.description] = topic.description
        return result

    def forward_str(self, topic):
        return json.dumps(self.forward(topic))

    def backward(self, topic, require_all=True):
        id = topic.get(self.id, None)
        if require_all:
            name = topic[self.name]
            description = topic[self.description]
        else:
            name = topic.get(self.name, None)
            description = topic.get(self.description, None)
        return model.topic.Topic(id, name, description)

    def backward_str(self, user, require_all=True):
        return self.backward(json.loads(user), require_all=require_all)