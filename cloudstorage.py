import pyrebase
config = {
    "apiKey": "AIzaSyBkSQnsBLjiPrJbZTbMYsufsZFkyee4UwY",
    "authDomain": "opencv-project-4eb12.firebaseapp.com",
    "databaseURL": "https://opencv-project-4eb12.firebaseio.com",
    "projectId": "opencv-project-4eb12",
    "storageBucket": "opencv-project-4eb12.appspot.com",
    "messagingSenderId": "437717112231",
    "appId": "1:437717112231:web:28bf4fc29a57a7b28c9282"
}
firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

def uploadImage(_id:str):
    try:
        path_on_cloud = "image/"+_id+".jpg"
        path_local = "image/"+_id+".jpg"
        storage.child(path_on_cloud).put(path_local)
    except Exception as e:
        print(e)
    