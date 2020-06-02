import cv2 as cv

cap = cv.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        gray = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)
        cv.imshow('gray', gray)
        if cv.waitKey(1) == ord('q'):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()
