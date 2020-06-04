import cv2 as cv
import datetime

cap = cv.VideoCapture(0)

# Set a new resolution
# cap.set(3, 1280)
# cap.set(4, 720)

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        # frame = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)
        font = cv.FONT_HERSHEY_SIMPLEX
        text = 'Width: ' + str(cap.get(3)) + ' Height: ' + str(cap.get(4))
        datet = str(datetime.datetime.now())
        cv.putText(frame, datet, (0, 50), font, 1, (255, 255, 255), 2, cv.LINE_AA)
        cv.imshow('frame', frame)
        if cv.waitKey(1) == ord('q'):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()
