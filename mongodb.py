import pymongo as pm
import datetime
import os
import firestore as fb
import cloudstorage as cs

client = pm.MongoClient() #เชื่อมต่อ MongoDB

def insertEmpoyee(face_id:int,name:str):
    try:
        db = client['project'] #เชื่อมต่อ กับ ฐานข้อมูล
        collection = db['employee']
        collection.insert_one({
            'id': face_id ,
            'name' : name,
            "update" : False
        })
    except Exception as e:
        print(e)
def checkEmpoyee(faceId:int):
    try:
        db = client['project'] #เชื่อมต่อ กับ ฐานข้อมูล
        collection = db['employee']
        data=collection.find_one({'id' : faceId})
        if data is None : 
            return "Unknow"
        else:
            return data['name']
    except Exception as e:
        print(e)
def insertTimestemp(faceId:int,typedata:str):
    try:
        db = client['project']  # เชื่อมต่อ กับ ฐานข้อมูล
        collection = db['timestemp']
        data = collection.insert_one({
            "id" : faceId,
            "timestemp" : datetime.datetime.now(),
            "type" : typedata,
            "update" : False
        })
        return data
    except Exception as e:
        print(e)
def checkTimestemp(faceId:int,typedata:str,dateTime:datetime.datetime):
    try:
        db = client['project'] #เชื่อมต่อ กับ ฐานข้อมูล
        collection = db['timestemp']
        #print(dateTime)
        year = int(dateTime.strftime("%Y"))
        month = int(dateTime.strftime("%m"))
        day = int(dateTime.strftime("%d"))
        #print(datetime.datetime(year, month, day,0,0,0))
        #print(datetime.datetime(year, month, day,23,59,59))
        data = collection.find({
            'id' : faceId,
            "type" : typedata,
            "timestemp": {"$gte": datetime.datetime(year, month, day,0,0,0),"$lte": datetime.datetime(year, month, day,23,59,59)}
        }).count()
        #print(data)
        return data 
    except Exception as e:
        print(e)
def checkUpdate(collectionDB:str):
    try:
        db = client['project'] #เชื่อมต่อ กับ ฐานข้อมูล
        collection = db[collectionDB]
        data=collection.find({'update' : False})
        #print(data)
        for i in data:
            _id = i["_id"]
            i.pop("_id")
            i['update'] = True
            #print(i)
            fb.insertData(collectionDB,str(_id),i)
            cs.uploadImage(str(_id))
            collection.update_one(
                {"_id" : _id},{"$set":{"update" : True}})
    except Exception as e:
        print(e)

#checkUpdate("employee")
#checkUpdate("timestemp")
#print(findTimestemp(462,"in",datetime.datetime.now()))
#findTimestemp(462,"out",2020,7,23)
#timestemp_in(462)
#timestemp_out(462)
#print(datetime.datetime.now().date())