import cv2 as cv
import numpy as np

blnk = np.zeros((400,400), dtype='uint8')

rectangle = cv.rectangle(blnk.copy(), (30,30), (370,370), 255, thickness=-1)
circle = cv.circle(blnk.copy(), (200,200), 200, 255, thickness=-1)

cv.imshow('rectangle', rectangle)
cv.imshow('circle', circle)

bitwise_and = cv.bitwise_and(rectangle,circle)
cv.imshow('bitwise and', bitwise_and)

bitwise_or = cv.bitwise_or(rectangle,circle)
cv.imshow('bitwise or', bitwise_or)

bitwise_xor = cv.bitwise_xor(rectangle,circle)
cv.imshow('bitwise xor', bitwise_xor)

bitwise_not = cv.bitwise_not(rectangle)
cv.imshow('bitwise not', bitwise_not)

cv.waitKey(0)