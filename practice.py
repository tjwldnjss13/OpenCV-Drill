import cv2 as cv

cap = cv.VideoCapture('vtest.avi')
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        gray = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)
        print('{}, {}'.format(cap.get(cv.CAP_PROP_FRAME_HEIGHT), cap.get(cv.CAP_PROP_FRAME_WIDTH)))
        cv.imshow('frame', gray)
        if cv.waitKey(0) == ord('q'):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()