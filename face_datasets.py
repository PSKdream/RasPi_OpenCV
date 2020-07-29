# Import OpenCV2 for image processing
import cv2 
import numpy as np
import pymongo as pm
import mongodb as mg

def face_dataset():
    # Start capturing video 
    cam = cv2.VideoCapture(0)
    cam.set(3, 640) # set video width
    cam.set(4, 480) # set video height

    # Detect object in video stream using Haarcascade Frontal Face
    faceCascade = cv2.CascadeClassifier('Cascades/haarcascade_frontalface_default.xml')

    # For each person, one face id
    face_id = input('\n enter user id end press <return> ==>  ')
    name = input('\n enter name end press <return> ==>  ')
    print("\n [INFO] Initializing face capture. Look the camera and wait ...")

    # Initialize sample face image
    count = 0

    # Start looping
    while(True):

        # Capture video frame
        ret, image_frame = cam.read()

        # flip video image vertically for RasPi
        #image_frame = cv2.flip(image_frame, -1) 
        
        # Convert frame to grayscale
        gray = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)

        # Detect frames of different sizes, list of faces rectangles
        faces = faceCascade.detectMultiScale(gray, 1.3, 5)

        # Loops for each faces
        for (x,y,w,h) in faces:

            # Crop the image frame into rectangle
            cv2.rectangle(image_frame, (x,y), (x+w,y+h), (255,0,0), 2)
            
            # Increment sample face image
            count += 1
            print(count)

            # Save the captured image into the datasets folder
            cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])

            # Display the video frame, with bounded rectangle on the person's face
            cv2.imshow('frame', image_frame)

        # To stop taking video, press 'q' for at least 100ms
        if cv2.waitKey(10) == ord('q'):
            break

        # If image taken reach 100, stop taking video
        elif count>=100:
            mg.insertEmpoyee(int(face_id),name)
            break

    # Stop video
    cam.release()

    # Close all started windows
    cv2.destroyAllWindows()


    