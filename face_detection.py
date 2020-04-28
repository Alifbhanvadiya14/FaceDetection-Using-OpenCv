import cv2
import numpy as np
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#img=cv2.imread("C:\\Users\\HP\\Desktop\\IMG_0423.JPG")

cap=cv2.VideoCapture(0)

while True:
    ret,img=cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Search the co-ordintes of the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.05,minNeighbors=5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)



    cv2.imshow("Gray", img)
    key=cv2.waitKey(30)  & 0xFF
    if key==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()



