import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cap=cv2.VideoCapture(0)
while(cap.isOpened()):
    _,frame=cap.read()
    img_copy=frame.copy()
    img_copyq=cv2.cvtColor(img_copy,cv2.COLOR_BGR2GRAY)

    faces=face_cascade.detectMultiScale(img_copy,1.1,4)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.imshow('video',frame)
        if(cv2.waitKey(1) & 0xFF == ord('q')):
            break
cap.release()
cv2.destroyAllWindows()