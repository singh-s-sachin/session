from pymongo import MongoClient
import uuid
import json
import time
def create_token(json_data):
    try:
        client = MongoClient("localhost",27017)
        db= client.tokens
        token=str(uuid.uuid4())
        db.token.insert({"token":token,"time": int(round(time.time() * 1000)),"data":json_data})
    except:
        return "false"
    return token
def get_data(token):
    try:
        client = MongoClient("localhost",27017)
        db= client.tokens
        data=db.token.find_one({"token":token})
        return dict(data["data"])
    except:
        return "Database denied connection"