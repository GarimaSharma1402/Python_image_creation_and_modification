#swap faces of lion on bear
#In later part, merge both images
import cv2, numpy as np
lion=cv2.imread("lion.jpg")
cv2.imshow('lion.jpg',lion)
cv2.waitKey()
cv2.destroyAllWindows()
lion=cv2.imread('lion.jpg')
crop_lion=lion[70:200,70:200]
cv2.imshow('cropped lion',crop_lion)
cv2.waitKey()
cv2.destroyAllWindows()
bear=cv2.imread("bear.jpg")
cv2.imshow('bear.jpg',bear)
cv2.waitKey()
cv2.destroyAllWindows()
bearl=cv2.imread('bear.jpg')
crop_bear=bear[30:160,40:170]
cv2.imshow('cropped bear',crop_bear)
cv2.waitKey()
cv2.destroyAllWindows()
bear=cv2.imread('bear.jpg')
bear[30:160,40:170]=crop_lion
cv2.imshow('bear.jpg',bear)
cv2.waitKey()
cv2.destroyAllWindows()

#merge images
lion=cv2.imread('lion.jpg')
bear=cv2.imread('bear.jpg')
bear1=bear[0:275,0:500]
lion1=lion[0:275,0:500]
combine=cv2.hconcat([lion1,bear1])
cv2.imshow("joined_image",combine)
cv2.waitKey()
cv2.destroyAllWindows()