import cv2
import numpy as np


def empty(a):
    pass


class HandDetection:
    def __init__(self):
        pass

    def create_trackbars(self):
        cv2.namedWindow("Trackbars")
        cv2.resizeWindow("Trackbars", 500, 300)
        cv2.createTrackbar("HueMin", "Trackbars", 0, 179, empty)
        cv2.createTrackbar("HueMax", "Trackbars", 179, 179, empty)
        cv2.createTrackbar("SatMin", "Trackbars", 0, 255, empty)
        cv2.createTrackbar("SatMax", "Trackbars", 255, 255, empty)
        cv2.createTrackbar("ValMin", "Trackbars", 0, 255, empty)
        cv2.createTrackbar("ValMax", "Trackbars", 60, 255, empty)

    def create_mask(self, img):
        imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        hue_min = cv2.getTrackbarPos("HueMin", "Trackbars")
        hue_max = cv2.getTrackbarPos("HueMax", "Trackbars")
        sat_min = cv2.getTrackbarPos("SatMin", "Trackbars")
        sat_max = cv2.getTrackbarPos("SatMax", "Trackbars")
        val_min = cv2.getTrackbarPos("ValMin", "Trackbars")
        val_max = cv2.getTrackbarPos("ValMax", "Trackbars")
        lower = np.array([hue_min, sat_min, val_min])
        upper = np.array([hue_max, sat_max, val_max])
        mask = cv2.inRange(imgHSV, lower, upper)
        return mask


################ DRIVER CODE ###################

hd = HandDetection()
hd.create_trackbars()

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    frame = cv2.flip(frame, 1)
    mask = hd.create_mask(frame)

    cv2.imshow("Mask", mask)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
