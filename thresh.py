import cv2 as cv

img = cv.imread('../me1.jpg')
cv.imshow('me', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

threshold, thresholded = cv.threshold(gray, 120, 200, cv.THRESH_BINARY)
cv.imshow('thresholded 120', thresholded)

threshold, thresholded_inv = cv.threshold(gray, 120, 200, cv.THRESH_BINARY_INV)
cv.imshow('thresholded inv', thresholded_inv)

adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 15, 5)
cv.imshow('adaptive threshold', adaptive_thresh)

cv.waitKey(0)