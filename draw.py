import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')

#blank[200:250,300:350] = 0,0,255
#cv.imshow("Red", blank)

#cv.rectangle(blank, (10,10), (blank.shape[1]//2,blank.shape[0]//2), (0,255,0), thickness=1)
#cv.imshow("Rectangle", blank)

#cv.circle(blank, (blank.shape[1]//2,blank.shape[0]//2), 50, (0,0,255), thickness=1)
#cv.imshow("Circle", blank)

#cv.line(blank,(blank.shape[1]//4,blank.shape[0]//4),(blank.shape[1]//2,blank.shape[0]//2),(255,0,0), thickness=10)
#cv.imshow("Line", blank)

cv.putText(blank,'LOVVE FATMA',(200,200), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,0,255), 2)
cv.imshow('Text',blank)


cv.waitKey(0)
