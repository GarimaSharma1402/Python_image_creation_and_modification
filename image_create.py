#creating a landscape using simple shapes
import cv2, numpy as np
img=np.zeros([512,512,3],np.uint8)
cv2.imshow("Image",img)
cv2.waitKey()
cv2.rectangle(img,(0,400),(600,600),(218,137,35),-1)
cv2.imshow("Image",img)
cv2.waitKey()
cv2.rectangle(img,(200,375),(400,400),(200,25,144),-1)
cv2.imshow("Image",img)
cv2.waitKey()
cv2.line(img,(150,375),(150,100),(100,100,144),2)
cv2.imshow("Image",img)
cv2.waitKey()
cv2.rectangle(img,(150,150),(300,200),(43,199,199),-1)
cv2.imshow("Image",img)
cv2.waitKey()
cv2.circle(img,(40,40),20,(216,216,227),-1)
cv2.imshow("Image",img)
cv2.waitKey()
