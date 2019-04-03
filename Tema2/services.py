class EntityService:
    def __init__(self, database, mapper, factory):
        self.database = database
        self.mapper = mapper
        self.factory = factory

    def get_all(self):
        results = self.database.select(self.mapper.table)
        if results:
            return [self.factory.from_list(result) for result in results]
        else:
            return []

    def get(self, entity_id):
        query = 'WHERE {}=?'.format(self.mapper.id_name)
        results = self.database.select(self.mapper.table, query, (entity_id,))
        if results:
            return self.factory.from_list(results[0])

    def insert(self, obj, instance_id=None):
        include_id = True if instance_id else False
        if instance_id:
            obj.set_id(instance_id)
        data = self.factory.to_list(obj, include_id)
        columns = self.mapper.columns(include_id)
        response = self.database.insert(self.mapper.table, data, columns)
        if response['status_code'] == 201:
            obj.set_id(response['id'])
            response['content'] = self.get(response['id'])
        return response

    def update(self, obj, instance_id):
        data = self.factory.to_list(obj, include_id=False)
        columns = self.mapper.columns(include_id=False)
        response = self.database.update(self.mapper.table, self.mapper.id_name, instance_id, data, columns)
        return response
        

    def delete(self, entity_id):
        return self.database.delete_by_id(self.mapper.table, self.mapper.id_name, entity_id)

    def delete_all(self):
        return self.database.delete_all(self.mapper.table)
        