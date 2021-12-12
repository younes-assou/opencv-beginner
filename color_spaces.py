import cv2 as cv


img = cv.imread('../me1.jpg')
cv.imshow('cars', img)


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)


hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('hsv', hsv)


lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('lab', lab)








cv.waitKey(0)