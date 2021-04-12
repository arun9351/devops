import cv2

x = cv2.VideoCapture(0)
while True:
    ret , photo = x.read()
    cv2.imshow ('hi',photo)
    if cv2.waitKey(1) == 13:
        cv2.destroyAllWindows()
        break    
x.release()
