import json
import model.review

class Review:
    def __init__(self, id, user, topic, score, content, user_view, topic_view):
        self.id = id
        self.user = user
        self.topic = topic
        self.score = score
        self.content = content
        self.user_view = user_view
        self.topic_view = topic_view

    def forward(self, review):
        result = dict()
        result[self.id] = review.id     
        result[self.user] = self.user_view.forward(review.user)
        result[self.topic] = self.topic_view.forward(review.topic)
        result[self.score] = review.score
        result[self.content] = review.content
        return result

    def forward_str(self, review):
        return json.dumps(self.forward(review))

    def backward(self, data, require_all=True):
        id = data.get(self.id, None)
        if require_all:
            user = data[self.user]
            topic = data[self.topic]
            score = data[self.score]
            content = data[self.content]
        else:
            user = data.get(self.user, None)
            topic = data.get(self.topic, None)
            score = data.get(self.score, None)
            content = data.get(self.content, None)
        return model.review.Review(id, user, topic, score, content)

    def backward_str(self, user, require_all=True):
        return self.backward(json.loads(user), require_all=require_all)