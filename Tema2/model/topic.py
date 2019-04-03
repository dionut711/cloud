class Topic:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

    def set_id(self, id):
        self.id = id

class TopicMapper:
    def __init__(self, table, id, name, description):
        self.table = table
        self.id = id
        self.name = name
        self.description = description
    
    @property
    def id_name(self):
        return self.id

    def columns(self, include_id=True):
        result = [self.id] if include_id else []
        result += [self.name, self.description]
        return result

class TopicsFactory:
    def __init__(self, id=0, name=1, description=2):
        self.id = id
        self.name = name
        self.description = description
    
    def from_list(self, data):
        return Topic(data[self.id], data[self.name], data[self.description])

    def to_list(self, user, include_id=True):
        result = [None] * 3
        result[self.name] = user.name     
        result[self.description] = user.description   
        result[self.id] = user.id
        if not include_id:
            del result[self.id]
        return result