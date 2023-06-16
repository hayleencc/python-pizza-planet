from flask import jsonify, request


class BaseService:

    def __init__(self, EntityController):
        self.controller = EntityController

    def create(self):
        entity, error = self.controller.create(request.json)
        return self.get_response(entity, error)

    def update(self):
        entity, error = self.controller.update(request.json)
        return self.get_response(entity, error)

    def get_by_id(self, _id: int):
        entity, error = self.controller.get_by_id(_id)
        return self.get_response(entity, error)

    def get_all(self):
        entity, error = self.controller.get_all()
        return self.get_response(entity, error)

    def get_response(self, entity, error):
        response = entity if not error else {'error': error}
        status_code = 200 if entity else 404 if not error else 400
        return jsonify(response), status_code
