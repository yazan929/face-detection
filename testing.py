import cv2

faces = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('test.jpg')

img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

detections = faces.detectMultiScale(img_gray,scaleFactor=1.1,minNeighbors=6)
# print(detections)

faces =0
for(x,y,w,h) in detections :
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,225,0),2)

    faces+=1

cv2.imshow("output",img)
cv2.imwrite("fix.jpg",img)
print("there are " , faces , " in the picture!!")
cv2.waitKey(0)