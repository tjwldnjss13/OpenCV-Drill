import cv2 as cv
import numpy as np

events = [i for i in dir(cv) if 'EVENT' in i]


# def click_event(event, x, y, flags, param):
#     if event == cv.EVENT_LBUTTONDOWN:
#         strXY = '{}, {}'.format(x, y)
#         font = cv.FONT_HERSHEY_SIMPLEX
#         cv.putText(img, strXY, (x, y), font, .5, (255, 255, 0), 1)
#         cv.imshow('image', img)
#     elif event == cv.EVENT_RBUTTONDOWN:
#         blue = img[y, x, 0]
#         green = img[y, x, 1]
#         red = img[y, x, 2]
#         strBGR = '{}, {}, {}'.format(blue, green, red)
#         font = cv.FONT_HERSHEY_SIMPLEX
#         cv.putText(img, strBGR, (x, y), font, .5, (255, 255, 255), 1)
#         cv.imshow('image', img)


def click_event(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(img, (x, y), 3, (0, 0, 255), -1)
        points.append((x, y))
        if len(points) >= 2:
            cv.line(img, points[-1], points[-2], (0, 255, 0), 5)
        cv.imshow('image', img)
    elif event == cv.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        cv.circle(img, (x, y), 2, (0, 0, 255), -1)
        myColorImage = np.zeros((512, 512, 3), np.uint8)

        myColorImage[:] = [blue, green, red]
        cv.imshow('color', myColorImage)


img = cv.imread('lena.jpg', -1)
cv.imshow('image', img)

points = []

cv.setMouseCallback('image', click_event)

cv.waitKey(0)
cv.destroyAllWindows()