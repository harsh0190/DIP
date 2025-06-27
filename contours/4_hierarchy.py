import cv2 as cv
import numpy as np


def greyScale(image):
    imgray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    return imgray


def getTh(image):
    _, thresh = cv.threshold(image, 127, 255, 0)
    return thresh


def showContours(image, contours):
    for contour in contours:
        cv.drawContours(image, [contour], -1, (0, 255, 0), 1)
        cv.imshow("image", image)
        cv.waitKey(0)


def main():
    image = cv.imread("Python\DIP\contours\hierarchy.png")

    # Step 1:
    gr_image = greyScale(image)

    # Step 2:
    th_image = getTh(gr_image)

    # Step 3:

    # RETR_LIST
    contours,hierarchy = cv.findContours(th_image, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
    print("RETR_LIST \n",hierarchy)
    showContours(image, contours)

    # RETR_EXTERNAL
    contours,hierarchy = cv.findContours(th_image, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    print("\n RETR_EXTERNAL \n",hierarchy)

    # RETR_TREE
    contours,hierarchy = cv.findContours(th_image, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
    print("\n RETR_TREE \n",hierarchy)


main()
