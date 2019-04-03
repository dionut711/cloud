import servertools
import routes.testing
import routes.main
import controllers.users
import controllers.topics
import controllers.reviews

get_router = servertools.Router()
get_router.add('testroute', routes.testing.get)
get_router.add('', routes.main.home_page)
get_router.add('styles', routes.main.styles)
get_router.add('users', controllers.users.get_router)
get_router.add('topics', controllers.topics.get_router)
get_router.add('reviews', controllers.reviews.get_router)

post_router = servertools.Router()
post_router.add('testroute', routes.testing.post)
post_router.add('users', controllers.users.post_router)
post_router.add('topics', controllers.topics.post_router)
post_router.add('reviews', controllers.reviews.post_router)

delete_router = servertools.Router()
delete_router.add('testroute', routes.testing.delete)
delete_router.add('users', controllers.users.delete_router)
delete_router.add('topics', controllers.topics.delete_router)
delete_router.add('reviews', controllers.reviews.delete_router)

put_router = servertools.Router()
put_router.add('testroute', routes.testing.put)
put_router.add('users', controllers.users.put_router)
put_router.add('topics', controllers.topics.put_router)

patch_router = servertools.Router()
patch_router.add('users', controllers.users.patch_router)
patch_router.add('topics', controllers.topics.patch_router)