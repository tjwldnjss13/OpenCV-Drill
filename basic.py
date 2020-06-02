import cv2 as cv

# # Read, Show, Save image
# img = cv.imread('lena.jpg', -1)
# cv.imshow('image', img)
# k = cv.waitKey(0) # Keyboard interrupt
#
# if k == 27:
#     cv.destroyAllWindows()
# elif k == ord('s'):
#     cv.imwrite('lena_copy.png', img)
#     cv.destroyAllWindows()

# Read, Show, Save video
cap = cv.VideoCapture('vtest.avi')
fourcc = cv.VideoWriter_fourcc('M', 'J', 'P', 'G')
out = cv.VideoWriter('output.avi', fourcc, 20.0, (576, 768))
frame_idx = 1
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        print('{} ({}, {})'.format(frame_idx, cap.get(cv.CAP_PROP_FRAME_HEIGHT), cap.get(cv.CAP_PROP_FRAME_WIDTH)))
        out.write(frame)
        gray = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)
        cv.imshow('frame', gray)
        frame_idx += 1
        if cv.waitKey(0) == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv.destroyAllWindows()