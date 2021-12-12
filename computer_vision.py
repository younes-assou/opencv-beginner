import cv2 as cv

capture = cv.VideoCapture(0)
capture.set(3,1600)
capture.set(4,800)
while True :
    isTrue, frame = capture.read()

    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

