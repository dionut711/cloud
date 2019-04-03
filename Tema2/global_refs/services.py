from global_refs.model import database
import global_refs.factories as factories
import global_refs.mappers as mappers
import services

users = services.EntityService(database, mappers.user, factories.users)
topics = services.EntityService(database, mappers.topic, factories.topics)
