class Review:
    def __init__(self, id, user, topic, score, content):
        self.id = id
        self.user = user
        self.topic = topic
        self.score = score
        self.content = content

    def set_id(self, id):
        self.id = id

class ReviewMapper:
    def __init__(self, table, id, user, topic, score, content):
        self.table = table
        self.id = id
        self.user = user
        self.topic = topic
        self.score = score
        self.content = content
    
    @property
    def id_name(self):
        return self.id

    def columns(self, include_id=True):
        result = [self.id] if include_id else []
        result += [self.user, self.topic, self.score, self.content]
        return result

class ReviewsFactory:
    def __init__(self, users_service, topics_service, id=0, user=1, topic=2, score=3, content=4):
        self.id = id
        self.user = user
        self.topic = topic
        self.score = score
        self.content = content
        self.users_service = users_service
        self.topics_service = topics_service
    
    def from_list(self, data):
        user = self.users_service.get(data[self.user])
        topic = self.topics_service.get(data[self.topic])
        return Review(data[self.id], user, topic, data[self.score], data[self.content])

    def to_list(self, review, include_id=True):
        result = [None] * 5
        result[self.id] = review.id     
        result[self.user] = review.user
        result[self.topic] = review.topic   
        result[self.score] = review.score
        result[self.content] = review.content
        if not include_id:
            del result[self.id]
        return result