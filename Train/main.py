from flask import Flask,request,jsonify, make_response
import json
import uuid
from pymongo import MongoClient
from session import create_token,get_data
import hashlib

app=Flask(__name__)


@app.route('/register',methods=["POST"])
def register():
    data=request.get_json()
    name=data["Name"]
    num=data["Mobile Number"]
    mail=data["email"]
    password=data["password"]
    password=password + "qyweugfuweiyufongjxl#7676809pf"
    password=hashlib.sha256(password.encode()).hexdigest()
    uid=str(uuid.uuid1())
    try:
        client=MongoClient("localhost",27017)
        db=client.train
    except:
        return jsonify({"message":"Database denied connection"})
    k=db.user.insert_one({"Name":name,"Mobile Number":num,"email":mail,"password":password,"_id":uid})
    return jsonify({"message":"success","id":uid})

@app.route('/register',methods=["GET"])
def show():
    try:
        client=MongoClient("localhost",27017)
        db=client.train
    except:
        return jsonify({"message":"Database denied connection"})
    k=db.user.find()
    l=[]
    for i in k:
        l.append({"name":i["Name"],"num":i["Mobile Number"],"id":i["_id"]})
    return jsonify({"users":l})

@app.route('/login',methods=["GET"])
def login():
    data=request.get_json()
    mail=data["email"]
    password=data["password"]
    password=password + "qyweugfuweiyufongjxl#7676809pf"
    password=hashlib.sha256(password.encode()).hexdigest()
    try:
        client=MongoClient("localhost",27017)
        db=client.train
        user_data=db.user.find_one({"email":mail})
    except:
        return jsonify({"message":"Database denied connection"})
    if(user_data is None):
            return jsonify({"message":"User dosent exists"})
    if(user_data["password"]!=password):
        return jsonify({"message":"Incorrect password"})
    auth_token=str(create_token({"uid":user_data["_id"],"name":user_data["Name"],"mob":user_data["Mobile Number"]}))
    return jsonify({"login":"successful","token":auth_token})

@app.route('/ticket',methods=["POST"])
def ticket():
    data=request.get_json()
    token=data["token"]
    user_data=dict(get_data(token))
    print(user_data)
    try:
        client=MongoClient("localhost",27017)
        db=client.train
    except:
        return jsonify({"message":"Database denied connection"})
    k=db.ticket.insert_one({"_id":str(uuid.uuid4),"name":user_data["name"],"mobile":user_data["mob"]})
    return jsonify({"Status":"Booked","PNR":str(k)})
app.run(debug=True)