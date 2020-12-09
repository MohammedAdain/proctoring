import cv2

cap = cv2.VideoCapture(0) # video capture source camera (Here webcam of laptop) 
#ret,frame = cap.read() # return a single frame in variable `frame`

while(cap.isOpened()):
    ret,frame=cap.read()
    img = cv2.rectangle(frame, (138,20), (534,415), (178, 231, 9),1)
    img = cv2.putText(frame, "Place your face in the square", (138,427), cv2.FONT_HERSHEY_SIMPLEX,0.5, (178, 231, 9), 1)
    cv2.imshow('video',frame)
    if cv2.waitKey(1) & 0xFF == ord('y'): #save on pressing 'y' 
        cv2.imwrite('imagesc2.png',frame)
        img=cv2.imread('imagesc1.png',1)
	#cv2.imshow('capturedImage',img)
    k=cv2.waitKey(1)
    if k==27:
        break

cap.release()