from flask import Flask
from flask_restful import  Api
from flask_jwt import JWT
from sec import authenticate, identity
from resources.userResourses import UserRegister
from resources.store import Store,StoreList
from resources.item import Item,itemList

#yes2
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'jose'
api = Api(app)


@app.before_first_request
def create_table():
    db.create_all()




jwt = JWT(app, authenticate, identity)






# http://127.0.0.1:5000/student/<name>
api.add_resource(Item, '/item/<string:name>')
api.add_resource(itemList, '/items')
api.add_resource(UserRegister,'/register')
api.add_resource(Store,'/store/<string:name>')
api.add_resource(StoreList,'/stores')



if __name__=="__main__":
    from db import db
    db.init_app(app)
    
    app.run(port=5000, debug=True)
