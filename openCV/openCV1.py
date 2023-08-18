import cv2
img = cv2.imread(r"C:\Users\User\OneDrive\Documents\CV and Personal Documents\photograph.jpg")
print(img)

cv2.imshow('Chiradeep',img)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


haar_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
faces_rect = haar_cascade.detectMultiScale(gray_img,1.1,9)

for (x,y,w,h) in faces_rect:
    cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
    
cv2.imshow("xyz", img)
cv2.waitKey(0)

print(faces_rect)

