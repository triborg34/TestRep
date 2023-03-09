from flask_restful import Resource
from models.storemodel import StoreModel
from models.item import ItemModel

class Store(Resource):
    def get(self,name):
        store=StoreModel.find_item_by_name(name)
        if store:
            return store.json()
        return {'massage':"store not found"} ,404

    def post(self,name):
        if StoreModel.find_item_by_name(name):
            return {'massage':f"{name} is aleredy exist"} ,400
        store=StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {'massage': "error accord"} , 500
        return store.json(),201

    def delete(self,name):
        store=StoreModel.find_item_by_name(name)
        if store:
            store.delete_from_db()
        return {'massage':'store is deleted'}


class StoreList(Resource):
    def get(self):
        return {'stores':[store.json() for store in ItemModel.query.all()]}