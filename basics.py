import cv2 as cv

img = cv.imread("me1.jpg")
cv.imshow('me', img)


blured = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
cv.imshow('blured', blured)

canny = cv.Canny(img, 60,70)
cv.imshow('canny edges', canny)



cv.waitKey(0)