# Import OpenCV2 for image processing
import cv2

# Import numpy for matrices calculations
import numpy as np

# Create Local Binary Patterns Histograms for face recognization
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Load the trained mode
recognizer.read('trainer/trainer.yml')

# Load prebuilt model for Frontal Face
cascadePath = "haarcascade_frontalface_default.xml"

# Create classifier from prebuilt model
faceCascade = cv2.CascadeClassifier('Cascades/haarcascade_frontalface_default.xml')
#eyeCascade = cv2.CascadeClassifier('Cascades/haarcascade_eye.xml')
smileCascade = cv2.CascadeClassifier('Cascades/haarcascade_smile.xml')

# Set the font style
font = cv2.FONT_HERSHEY_SIMPLEX

# Initialize and start the video frame capture
cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video widht
cam.set(4, 480) # set video height

# Loop
while True:
    # Read the video frame
    ret, img =cam.read()
    #img = cv2.flip(im, -1) # Flip vertically
    # Convert the captured frame into grayscale
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    # Get all face from the video frame
    faces = faceCascade.detectMultiScale(gray, 1.2,5)

    # For each face in faces
    for(x,y,w,h) in faces:

        # Create rectangle around the face
        cv2.rectangle(img, (x-20,y-20), (x+w+20,y+h+20), (0,255,0), 4)
        # Recognize the face belongs to which ID
        Id = recognizer.predict(gray[y:y+h,x:x+w])
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w] 
        '''
        eyes = eyeCascade.detectMultiScale(
            roi_gray,
            scaleFactor= 1.5,
            minNeighbors=10,
            minSize=(5, 5),
            )
        for (ex, ey, ew, eh) in eyes:
            print(eyes)
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (255, 0, 0), 2)
        if (not len(eyes)):
            print("no eyes")
        '''
        '''
        smile = smileCascade.detectMultiScale(
            roi_gray,
            scaleFactor= 1.5,
            minNeighbors=15,
            minSize=(25, 25),
            )
        
        for (xx, yy, ww, hh) in smile:
            cv2.rectangle(roi_color, (xx, yy), (xx + ww, yy + hh), (0, 0, 255), 2)
        '''
        print("ID : ",Id[0])
        # Check the ID if exist 
        if(Id[0] == 125):
            Id = "Dream"
        #If not exist, then it is Unknown
        elif(Id[0] == 2):
            Id = "View"
        else:
            #print(Id)
            Id = "Unknow"

        # Put text describe who is in the picture
        cv2.rectangle(img, (x-22,y-90), (x+w+22, y-22), (0,255,0), -1)
        cv2.putText(img, str(Id), (x,y-40), font, 2, (255,255,255), 3)

    # Display the video frame with the bounded rectangle
    cv2.imshow('img',img) 

    # If 'q' is pressed, close program
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# Stop the camera
cam.release()

# Close all windows
cv2.destroyAllWindows()
