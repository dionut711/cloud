import views.json

user = views.json.User("Username", "First Name", "Last Name")
users = views.json.CollectionViewer(user)

topic = views.json.Topic("ID", "Name", "Description")
topics = views.json.CollectionViewer(topic)

review = views.json.Review("ID", "User", "Topic", "Score", "Content", user, topic)
reviews = views.json.CollectionViewer(review)