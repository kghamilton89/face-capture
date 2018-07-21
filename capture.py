#Import numpy and cv2 libraries
import numpy as np
import cv2 as cv


# Create haarcascade for recognition
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')

# Create variables. `img` contains the image to analyze and `gray` converts the image to grayscale
img = cv.imread('test.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# OpenCV function for facial recognition.
faces = face_cascade.detectMultiScale(gray, 1.9, 5)

# Label faces.
for (x,y,w,h) in faces:
    cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    gray_main = gray[y:y+h, x:x+w]
    color_main = img[y:y+h, x:x+w]
    
    # OpenCV function for eye recognition
    eyes = eye_cascade.detectMultiScale(gray_main)
    for (ex,ey,ew,eh) in eyes:
        cv.rectangle(color_main,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        
#cv.imshow('gray', gray)

# Print image with labeling.
cv.imshow('img',img)	
cv.waitKey(0)
cv.destroyAllWindows()
