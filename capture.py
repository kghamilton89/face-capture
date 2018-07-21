#Import numpy and cv2 libraries
import numpy as np
import cv2 as cv


# Create haarcascade for recognition
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')

# Create variables. `img` contains the image to analyze and `gray` converts the image to grayscale
image = cv.imread('test.jpg')
convert = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# OpenCV function for facial recognition.
face = face_cascade.detectMultiScale(convert, 1.9, 5)

# Label faces.
for (x,y,w,h) in face:
    cv.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
    grayscale = convert[y:y+h, x:x+w]
    original = image[y:y+h, x:x+w]
    
    # OpenCV function for eye recognition
    eyes = eye_cascade.detectMultiScale(grayscale)
    for (ex,ey,ew,eh) in eyes:
        cv.rectangle(original,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

# Print and write image with labeling.
cv.imshow('image',image)	
cv.imwrite('res.jpg',image)
cv.waitKey(0)
cv.destroyAllWindows()
