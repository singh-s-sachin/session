from pymongo import MongoClient
import datetime
import uuid
import time
while(True):
    try:
        client = MongoClient("localhost",27017)
        db= client.tokens
        ten_minutes_ago = (datetime.datetime.now() - datetime.timedelta(minutes=1))
        db.token.delete_many({"time":{"$lte":int(ten_minutes_ago.timestamp() * 1000)}})
    except:
        print("error")