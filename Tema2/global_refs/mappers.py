import model.user
import model.topic

user = model.user.UserMapper("users", "username", "first_name", "last_name")
topic = model.topic.TopicMapper("topics", "id", "name", "description")
review = model.review.ReviewMapper("reviews", "id", "user", "subject_id", "score", "content")