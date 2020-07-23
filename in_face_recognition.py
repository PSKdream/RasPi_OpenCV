# Import OpenCV2 for image processing
import cv2
# Import numpy for matrices calculations
import numpy as np
import pymongo as pm
import datetime
import mongodb as mg
from multimethod import multimethod 


# Create Local Binary Patterns Histograms for face recognization
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Load the trained mode
recognizer.read('trainer/trainer.yml')

# Create classifier from prebuilt model
faceCascade = cv2.CascadeClassifier('Cascades/haarcascade_frontalface_default.xml')
eyeCascade = cv2.CascadeClassifier('Cascades/haarcascade_eye.xml')
smileCascade = cv2.CascadeClassifier('Cascades/haarcascade_smile.xml')

# Set the font style
font = cv2.FONT_HERSHEY_SIMPLEX
fontSmall = cv2.FONT_HERSHEY_PLAIN

# Initialize and start the video frame capture
cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video widht
cam.set(4, 480) # set video height

# Loop
while True:
    # Read the video frame
    ret, image_frame = cam.read()

    # Flip vertically for RasPI
    #image_frame = cv2.flip(image_frame, -1) 
    
    # Convert the captured frame into grayscale
    gray = cv2.cvtColor(image_frame,cv2.COLOR_BGR2GRAY)

    # Get all face from the video frame
    faces = faceCascade.detectMultiScale(gray, 1.2,5)
    
    # show date time
    cv2.putText(image_frame, str(datetime.datetime.now()) , (10,400), fontSmall, 1, (255,255,255))

    # For each face in faces
    for(x,y,w,h) in faces:
        # Create rectangle around the face
        cv2.rectangle(image_frame, (x-20,y-20), (x+w+20,y+h+20), (0,255,0), 4)
        # Recognize the face belongs to which ID
        face_id = recognizer.predict(gray[y:y+h,x:x+w])
        
        # Check the ID if exist 
        #print("ID : ",face_id[0])
        face_name = mg.checkEmpoyee(face_id[0])

        # Put text describe who is in the picture
        cv2.rectangle(image_frame, (x-22,y-90), (x+w+22, y-22), (0,255,0), -1)
        cv2.putText(image_frame, str(face_name), (x,y-40), font, 1, (255,255,255), 3)
        
        #savedatabase
        check = mg.checkTimestemp(face_id[0],"in",datetime.datetime.now())
        #print(check)
        
        if check is 0 and face_name is not "Unknow":
            _id = mg.insertTimestemp(face_id[0],"in").inserted_id
            cv2.putText(image_frame, "Check time in : OK" , (300,400), font, 1, (0,255,0),2)
            cv2.imwrite("image/"+str(_id)+'.jpg', image_frame)
        elif face_name is not "Unknow":
            cv2.putText(image_frame, "Check time in : OK" , (300,400), font, 1, (0,255,0),2)

    #print(datetime.datetime.now().date())
    # If 'q' is pressed, close program
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
    # Display the video frame with the bounded rectangle
    cv2.imshow('image_frame',image_frame) 

# Stop the camera
cam.release()
# Close all windows
cv2.destroyAllWindows()
