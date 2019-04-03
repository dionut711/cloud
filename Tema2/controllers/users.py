import servertools
import controllers.generic
from global_refs.services import users as service
from global_refs.views import user as entity_view
from global_refs.views import users as collection_view

get_collection = controllers.generic.GetCollection(service, collection_view).handle
get_entity = controllers.generic.GetEntity(service, entity_view).handle

post_collection = controllers.generic.method_not_allowed
post_entity = controllers.generic.PostEntity(service, entity_view, auto_id=False).handle

delete_collection = controllers.generic.method_not_allowed
delete_entity = controllers.generic.DeleteEntity(service, entity_view).handle

put_collection = controllers.generic.method_not_allowed
put_entity = controllers.generic.PutEntity(service, entity_view).handle

patch_collection = controllers.generic.method_not_allowed
patch_entity = controllers.generic.PatchEntity(service, entity_view).handle

get_router = servertools.CollectionRouter(get_collection, get_entity)
post_router = servertools.CollectionRouter(post_collection, post_entity)
delete_router = servertools.CollectionRouter(delete_collection, delete_entity)
put_router = servertools.CollectionRouter(put_collection, put_entity)
patch_router = servertools.CollectionRouter(patch_collection, patch_entity)
