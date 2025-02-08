from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import unittest

app = Flask(__name__)
api = Api(app)

fake_data = [
    {"id": 1, "name": "Item 1", "price": 10.99},
    {"id": 2, "name": "Item 2", "price": 12.99},
    {"id": 3, "name": "Item 3", "price": 8.99}
]

class Item(Resource):
    def get(self, item_id):
        for item in fake_data:
            if item['id'] == item_id:
                return item, 200
        return "Item not found", 404

    def post(self):
        new_item = request.get_json()
        fake_data.append(new_item)
        return new_item, 201

    def put(self, item_id):
        updated_item = request.get_json()
        for index, item in enumerate(fake_data):
            if item['id'] == item_id:
                fake_data[index] = updated_item
                return updated_item, 200
        return "Item not found", 404

    def delete(self, item_id):
        global fake_data
        fake_data = [item for item in fake_data if item['id'] != item_id]
        return "Item deleted", 200

api.add_resource(Item, '/item', '/item/<int:item_id>')

if __name__ == '__main__':
    app.run(debug=True)