import cv2
 # Load the cascadea
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# Read the input image
img = cv2.imread('test3.jpg')
# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
#Draw rectangle around the faces
face = 0

for (x, y, w, h) in faces:
     cv2.rectangle(img, (x, y), (x+w, y+h), (10, 200, 255), 2)
     face +=1
 # Display the output
cv2.imshow('img', img)
print(face)
cv2.waitKey()
