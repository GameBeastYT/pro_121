
import cv2
import time
import numpy as np

cap = cv2.VideoCapture(0)
bg = cv2.imread("bangkok2.jpeg")

while True:
    ret, img = cap.read()
    img = cv2.resize(img, (640, 480))
    bg = cv2.resize(bg, (640, 480))
    lower_black = np.array([30, 30, 0])
    upper_black = np.array([104, 153, 170])
    mask1 = cv2.inRange(img, lower_black, upper_black)
    result1 = cv2.bitwise_and(img, img, mask = mask1)
    f = img - result1
    f = np.where(f == 0, bg, f)
    if cv2.waitKey(1) & 0xFF == ord("Q"):
        break
cap.release()
cv2.destroyAllWindows()

#Saturation = intensity of the color