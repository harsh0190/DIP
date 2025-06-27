import numpy as np
import cv2 as cv

def greyScale(image):
    imgray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    return imgray


def getTh(image):
    _, thresh = cv.threshold(image, 127, 255, 0)
    return thresh


def main():
    image = cv.imread('Python\DIP\contours\elon.jpeg')
    cv.imshow("elon musk",image)

    # Step 1:
    gr_image = greyScale(image)
    cv.imshow("elon musk grey",gr_image)

    # Step 2:
    th_image = getTh(gr_image)
    cv.imshow("elon musk thres",th_image)

    # Step 3:
    contours,_ = cv.findContours(th_image, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
    print(contours)
    print("Type : ",type(contours))
    print("Number of contours: ",len(contours))
    print("Data type of single contour: ",type(contours[0]))
    print("Shape of contour array: ",np.shape(contours[0]))
    print("Dimension of contour array: ",np.ndim(contours[0]))

    # Step 4:
    cv.drawContours(image,contours,-1,(255,0,0),2)
    cv.imshow("elon musk contours",image)

    cv.waitKey(0)
    

main()




