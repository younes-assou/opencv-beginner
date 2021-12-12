import cv2 as cv
import numpy as np


img = cv.imread('../me1.jpg')
cv.imshow('me', img)

blnk = np.zeros(img.shape[:2], dtype='uint8')
b,g,r = cv.split(img)

blue = cv.merge([b, blnk, blnk])
green = cv.merge([blnk, g, blnk])
red = cv.merge([blnk, blnk, r])

cv.imshow('blue', blue)
cv.imshow('green', green)
cv.imshow('red', red)

merged = cv.merge([b,g,r])
cv.imshow('merged', merged)

cv.waitKey(0)