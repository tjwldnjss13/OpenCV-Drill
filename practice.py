import cv2 as cv

cap = cv.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        cv.imshow('frame', frame)
        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            break
    else:
        break

cap.release()