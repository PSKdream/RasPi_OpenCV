import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('./Admin_SDK.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

def insertData(collectionDB,key,data):
    try:
        doc_ref = db.collection(collectionDB).document(key)
        doc_ref.set(data)
    except Exception as e:
        print(e)