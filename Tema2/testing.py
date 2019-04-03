# import urllib
# import urllib.parse

# path = "/archive/entries?sort=asc&category=cars"

# res = urllib.parse.urlparse(path)
# params = urllib.parse.parse_qs(res.query)
# print(res)

# print([None] * 3)

# import model.user
# import views.json.user
# import json

# mapper = model.user.UserMapper("Username", "First Name", "Last Name")
# user = model.user.User("jimboy", "Jimmy", "Boy")
# view = views.json.user.User(mapper)

# res = view.forward_str(user).encode()
# print(res)
# d = {"Username":"BradHolmes", "First Name":"Brad", "Last Name":"Holmes"}

# res = view.backward_str(json.dumps(d))
# print(res)

import global_refs.factories

factory = global_refs.factories.users

res = factory.from_list(['jimboy', 'jimmy', 'boy'])
print(res)

print(factory.to_list(res))