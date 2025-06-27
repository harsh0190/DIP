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
        cv2.createTrackbar("HueMax", "Trackbars", 39, 179, empty)
        cv2.createTrackbar("SatMin", "Trackbars", 39, 255, empty)
        cv2.createTrackbar("SatMax", "Trackbars", 255, 255, empty)
        cv2.createTrackbar("ValMin", "Trackbars", 0, 255, empty)
        cv2.createTrackbar("ValMax", "Trackbars", 255, 255, empty)

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

    def centroid(self, contour):
        if len(contour) == 0:
            return (-1, -1)
        M = cv2.moments(contour)
        try:
            x = int(M["m10"] / M["m00"])
            y = int(M["m01"] / M["m00"])
        except ZeroDivisionError:
            return (-1, -1)
        return (x, y)

    def find_contours(self, mask):
         contours = []
         contours,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
         max_cnt = sorted(contours, key=lambda x:cv2.contourArea(x), reverse=True)

         approx_contours = []
         for contour in max_cnt:
            epsilon = 0.005*cv2.arcLength(contour,True)
            approx = cv2.approxPolyDP(contour,epsilon,True)
            approx_contours.append(approx)
         return approx_contours
    
    def draw_contours(self,contours,frame):
        for contour in contours:
            cv2.drawContours(frame, [contour], -1,(255,255,0),2)
            x,y = self.centroid(contour)
            cv2.circle(frame, (x,y), 4, (255,0,0),-1)
        return frame


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
    contour = hd.find_contours(mask)

    frame = hd.draw_contours(contour,frame)
    cv2.imshow("Image", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
