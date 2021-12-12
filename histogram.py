import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('../me1.jpg')
cv.imshow('me', img)

#gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('gray me', gray)

blnk = np.zeros(img.shape[:2], dtype='uint8')
mask = cv.circle(blnk, (img.shape[1]//2,img.shape[0]//2), 100, 255, -1)
masked = cv.bitwise_and(img,img, mask=mask)


#gray_hist = cv.calcHist([img], [0], None, [256], [0,256])

""" plt.figure()
plt.title('grayscale histogram')
plt.xlabel('bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show() """

plt.figure()
plt.title('color histogram')
plt.xlabel('bins')
plt.ylabel('# of pixels')
colors = ('b','g','r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img], [i], mask, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])
plt.show()

cv.waitKey(0)