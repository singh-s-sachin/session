import requests
from pymongo import MongoClient
import uuid
import json
print("Fetching data")
response = requests.get("https://api.covid19india.org/state_test_data.json")
client = MongoClient("localhost",27017)
db= client.corona
print("Processing data")
data=response.json()
raw_data=data.get("states_tested_data")
length=len(raw_data)
m=1
print("Saving data")
for i in raw_data:
    if(m%100==0):
        print(m,"/",length)
    db.statewise.insert_one(i)
    m+=1
