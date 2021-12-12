import cv2 as cv

img = cv.imread('../me1.jpg')
cv.imshow('me', img)
ks=3
average = cv.blur(img, (ks,ks))
cv.imshow('average blur', average)

gauss = cv.GaussianBlur(img, (ks,ks), 0)
cv.imshow('gaussian blur', gauss)

median = cv.medianBlur(img, ks)
cv.imshow('median blur', median)

bilateral = cv.bilateralFilter(img, 5, 35, 25)
cv.imshow('bilateral', bilateral)

cv.waitKey(0)