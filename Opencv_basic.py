import cv2 as cv
import numpy as np

'Image'
# img = cv.imread('D:\Harsh\Python\DIP\Images\Add2.jpg',17) # 0 for grayscale and increasing value of flag, image size decreases. 17,33,65 are standard value. 
# cv.imshow('Space',img)

# grey= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Space',grey)
# cv.waitKey(3000)

'Video capturing'
# cap = cv.VideoCapture(0)
# while True:
#     ret, frame=cap.read()
#     cv.imshow('video',frame)
#     if cv.waitKey(1) & 0xFF==ord('q'):
#         break
# cap.release()
# cap.destroyAllWindows()

'Shapes'
# img = np.zeros((512,512,3), np.uint8)
# cv.line(img,(0,0),(511,511),(23,20,220),1)   #center, radius, colour, thickness
# cv.circle(img,(244,244),255,(23,20,70),-1) 
# cv.imshow('image',img)
# if cv.waitKey(0) == 27:
#     cv.destroyAllWindows()

'Cropping an image'
# img = cv.imread("D:\Harsh\Python\DIP\Images\add3.jpg")
# img[100,100]= [255,0,0]
# updatePx = img[100,100]
# print(updatePx)
# img[100:200, 300:400] = [255,0,0]
# cv.imshow("updated", img)

'Mixing images'
# img1= cv.imread("D:\Harsh\Python\DIP\Images\Space.jpg")
# img2= cv.imread("D:\Harsh\Python\DIP\Images\Ruins.jpg")

# cv.imshow('image1', img1)
# cv.imshow('image2', img2)

# weightedSum=cv.addWeighted(img1,0.5,img2,0.4,0)
# cv.imshow('Weighted image', weightedSum)
# if cv.waitKey(0)==27:
#     cv.destroyAllWindows()

'Bitwise operations in images'
# img1= cv.imread("D:\Harsh\Python\DIP\Images\BW.jpg")
# img2= cv.imread("D:\Harsh\Python\DIP\Images\WC.jpg")

# cv.imshow('image1', img1)
# cv.imshow('image2', img2)

# dest_and = cv.bitwise_and(img1,img2, mask = None)
# cv.imshow('Weighted image', dest_and)
# if cv.waitKey(0)==27:
#     cv.destroyAllWindows()

# img1= cv.imread("D:\Harsh\Python\DIP\Images\BW.jpg")
# img2= cv.imread("D:\Harsh\Python\DIP\Images\WC.jpg")

# cv.imshow('image1', img1)
# cv.imshow('image2', img2)

# dest_or = cv.bitwise_or(img1,img2, mask = None)
# cv.imshow('Weighted image', dest_or)
# if cv.waitKey(0)==27:
#     cv.destroyAllWindows()

'Masking an image'
# img = cv.imread("D:\Harsh\Python\DIP\Images\Chevrolet.jpg") 
# cv.imshow("Original image", img)

# hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV) #convert bgr to hsv

# lower_yellow = np.array([15,50,180]) #defining range
# upper_yellow = np.array([40,255,255]) 

# mask = cv.inRange(hsv, lower_yellow, upper_yellow) #creating mask

# result = cv.bitwise_and(img, img, mask = mask)

# cv.imshow("Mask", mask)
# cv.imshow("Final", result)
# if cv.waitKey(0)==27:
#     cv.destroyAllWindows()

'Colour Trackbar'
# def onChange(a):
#     pass

# cv.namedWindow("myWindow")
# cv.resizeWindow("myWindow", 600,150)

# cv.createTrackbar("Red", "myWindow", 0, 255, onChange) # trackbar name, window name, initial value, final value, call this function
# cv.createTrackbar("Blue", "myWindow", 0, 255, onChange)
# cv.createTrackbar("Green", "myWindow", 0,255, onChange)
# img = np.zeros((512,512,3), np.uint8)

# while True:
#     r = cv.getTrackbarPos(trackbarname="Red", winname = "myWindow")
#     b = cv.getTrackbarPos(trackbarname="Blue", winname = "myWindow")
#     g = cv.getTrackbarPos(trackbarname="Green", winname = "myWindow")
#     img[:]=[b,g,r]
#     cv.imshow("image", img)
   
#     if cv.waitKey(1)==27:
#         break
# cv.destroyAllWindows()
