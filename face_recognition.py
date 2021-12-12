import numpy as np
import cv2 as cv
import os

haar_cascade = cv.CascadeClassifier('haar_face.xml')

people =[]
DIR = './Faces/train'
for i in os.listdir(DIR):
    people.append(i)


face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

img = cv.imread('./Faces/val/ben_afflek/3.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('person', gray)

# detect face

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h,x:x+w]
    
    label, confidence = face_recognizer.predict(faces_roi)
    print(f'label = {people[label]} with confidence of {confidence}')

    cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0),2)

cv.imshow('detected face', img)

cv.waitKey(0)