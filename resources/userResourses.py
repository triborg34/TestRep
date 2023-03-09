import sqlite3
from flask_restful import Resource,reqparse
from models.user import UserModel



class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',required=True,type=str,help="This blank Must Be fill")
    parser.add_argument('password',required=True,type=str,help="This blank Must Be fill")
    
    def post(self,):
        data=UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"massage":"this user is exists"} ,400



        user=UserModel(**data)
        user.save_to_db()

        return {'massage':"User Create "} ,201

    def get(self):
        
        
        return {"users":[user.userjson() for user in UserModel.query.all()]}




