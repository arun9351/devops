import cv2
x = cv2.VideoCapture(0)
ret , photo = x.read()
cv2.imwrite('photo.png' , photo)
x.release()
