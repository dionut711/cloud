class User:
    def __init__(self, username, first_name, last_name):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name

    def set_id(self, id):
        self.username = id

    def __str__(self):
        return str(self.__dict__)

class UserMapper:
    def __init__(self, table, username, first_name, last_name):
        self.table = table
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
    
    @property
    def id_name(self):
        return self.username

    def columns(self, include_id=True):
        result = [self.username] if include_id else []
        result += [self.first_name, self.last_name]
        return result

class UsersFactory:
    def __init__(self, username=0, first_name=1, last_name=2):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
    
    def from_list(self, data):
        return User(data[self.username], data[self.first_name], data[self.last_name])

    def to_list(self, user, include_id=True):
        result = [None] * 3
        result[self.first_name] = user.first_name
        result[self.last_name] = user.last_name    
        result[self.username] = user.username    
        if not include_id:
            del result[self.username]
        return result
