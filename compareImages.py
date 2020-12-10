import numpy as np
import cv2

cap = cv2.VideoCapture(0)

print(cap.isOpened())
img1=cv2.imread('imagesc1.png',1)

#cv2.imshow('diff Image',img1)
#img2=cv2.imread('imagesc2.png',1)



while True:
	ret,img2=cap.read()
	cv2.imshow('video',img2)
	img3=cv2.subtract(img1,img2)
	cv2.imshow('diff',img3)
	countOff=0
	for i in range(20,415):
		for j in range(138,534):
			if img3[i][j].any()!=0:countOff=countOff+1
			
	k=cv2.waitKey(1)
	print(countOff)
	if k == ord('q'):
		cv2.destroyAllWindows()



h=len(img3)
w=len(img3[0])




	
cap.release()