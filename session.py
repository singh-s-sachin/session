from pymongo import MongoClient
import uuid
import time
def create_token(json_data):
    try:
        client = MongoClient("localhost",27017)
        db= client.tokens
        token=uuid.uuid4()
        db.token.insert({"token":token,"time": int(round(time.time() * 1000)),"data":json_data})
    except:
        return "false"
    return token
    