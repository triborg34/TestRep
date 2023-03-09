

from flask_restful import Api, reqparse, Resource
from flask_jwt import jwt_required
import sqlite3
from models.item import ItemModel


class Item(Resource):


    parser = reqparse.RequestParser()
    parser.add_argument('price', required=True, type=float,
                        help="This fill must be filled")
    parser.add_argument('store_id', required=True, type=int,
                        help="This fill must be filled")

    @jwt_required()
    def get(self, name):

        item=ItemModel.find_item_by_name(name)
        if item:
            return item.json()
        return {"massage": "Item Does Not Exist"}, 404

    def post(self, name):
        data = Item.parser.parse_args()
        item = ItemModel(name,data['price'],data['store_id'])
        if ItemModel.find_item_by_name(name):
            return {"massage": f"{name} is exist"}, 400
        
        try:
            item.save_to_db()
        except:
            return {"massage":"Something Went Wrong"},500
        return item.json(), 201

    

        


        # if next(filter(lambda x: x['name'] == name, items), None):
        #     return {'massage': f"An item with name {name} is already exists"}, 400

        # data = Item.parser.parse_args()
        # item = {"name": name, "price": data['price']}
        # items.append(item)
        # return item, 201

    def delete(self, name):
        # global items
        # items = list(filter(lambda x: x['name'] != name, items))
        # return {'massage': 'Item Deleted'}

        item=ItemModel.find_item_by_name(name)
        if item:
            item.delete_from_db()
        return {"massage":"Item has been Deleted"}


    def put(self, name):
        

        data = Item.parser.parse_args()

        item = ItemModel.find_item_by_name(name)
        
        if item is None:
            item=ItemModel(name, **data)

            

        else:
            item.price=data['price']
            item.store_id=data['store_id']
        
        item.save_to_db()
        return item.json()
    




class itemList(Resource):
    def get(self):
        return {'items':list(map(lambda x:x.json() ,ItemModel.query.all()))}
