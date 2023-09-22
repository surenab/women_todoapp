import cv2 as cv
import cv2
import numpy as np

cap = cv.VideoCapture(0)

while (True):
    # Take each frame
    _, frame = cap.read()
    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    height, width, _ = frame.shape
    center_x, center_y = width // 2, height // 2
    radius = min(center_x, center_y)  # Using the smaller dimension for radius

    mask = np.zeros((height, width), np.uint8)
    cv2.circle(mask, (center_x, center_y), radius, (255, 255, 255), -1)

    # # Step 4: Use the mask to keep only the circular part of the image
    circular_gray_img = cv2.bitwise_and(frame, frame, mask=mask)

    # # define range of blue color in HSV
    lower_blue = np.array([50, 50, 50])
    upper_blue = np.array([230, 255, 255])
    # # Threshold the HSV image to get only blue colors
    mask = cv.inRange(hsv, lower_blue, upper_blue)
    # # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame, frame, mask=mask)
    cv.imshow('frame', circular_gray_img)
    # cv.imshow('mask',mask)
    cv.imshow('res', res)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()
