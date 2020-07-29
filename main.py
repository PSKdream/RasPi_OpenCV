import face_datasets 
import training
import face_recognition 
import mongodb as mg

print("1 : dataset")
print("2 : training")
print("3 : check in")
print("4 : check out")
print("5 : update data to could")
print("0 : Exit program")

while(1):
    print("\n------------------------------------")
    choice = int(input("Please input function : "))

    if(choice is 1):
        face_datasets.face_dataset()
    elif (choice is 2):
        training.training()
    elif (choice is 3):
        print("Back to main program please button q")
        face_recognition.timestemp("in")
    elif (choice is 4):
        print("Back to main program program please button q")
        face_recognition.timestemp("out")
    elif (choice is 5):
        mg.checkUpdate("employee")
        mg.checkUpdate("timestemp")
    elif (choice is 0):
        break
    else:
        print("error")
