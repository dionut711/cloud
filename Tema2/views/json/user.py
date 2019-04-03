import json
import model.user

class User:
    def __init__(self, username, first_name, last_name):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name

    def forward(self, user):
        result = dict()
        result[self.username] = user.username
        result[self.first_name] = user.first_name
        result[self.last_name] = user.last_name
        return result

    def forward_str(self, user):
        return json.dumps(self.forward(user))

    def backward(self, user, require_all=True):
        username = user.get(self.username, None)
        if require_all:
            first_name = user[self.first_name]
            last_name = user[self.last_name]
        else:
            first_name = user.get(self.first_name, None)
            last_name = user.get(self.last_name, None)
        return model.user.User(username, first_name, last_name)

    def backward_str(self, user, require_all=True):
        return self.backward(json.loads(user), require_all=require_all)