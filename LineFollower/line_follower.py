import numpy as np
from djitellopy import tello
import cv2

me = tello.Tello()
me.connect()
print(me.get_battery())
me.streamon()

hsvVals = [0, 0, 188, 179, 33, 245]
sensors = 3
threshold = 0.2
width, height = 480, 360
sensitivity = 3  # Higher number = less sensitive
weights = [-25, -15, 0, 15, 25]
fSpeed = 15
curve = 0

def thresholding(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array(hsvVals[:3])
    upper = np.array(hsvVals[3:])
    mask = cv2.inRange(hsv, lower, upper)
    return mask

def getContours(imgThres, img):
    cx = 0
    contours, _ = cv2.findContours(imgThres, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    if len(contours) != 0:
        biggest = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(biggest)
        cx = x + w // 2
        cv2.drawContours(img, biggest, -1, (255, 0, 255), 7)
        cv2.circle(img, (cx, y + h // 2), 10, (0, 255, 0), cv2.FILLED)
    return cx

def getSensorOutput(imgThres, sensors):
    imgs = np.hsplit(imgThres, sensors)
    totalPixels = (img.shape[1] // sensors) * img.shape[0]
    senOut = [1 if cv2.countNonZero(im) > threshold * totalPixels else 0 for im in imgs]
    return senOut

def sendCommands(senOut, cx):
    global curve
    lr = (cx - width // 2) // sensitivity
    lr = int(np.clip(lr, -10, 10))
    if 2 > lr > -2:
        lr = 0
    if senOut == [1, 0, 0]: curve = weights[0]
    elif senOut == [1, 1, 0]: curve = weights[1]
    elif senOut == [0, 1, 0]: curve = weights[2]
    elif senOut == [0, 1, 1]: curve = weights[3]
    elif senOut == [0, 0, 1]: curve = weights[4]
    elif senOut == [0, 0, 0]: curve = weights[2]
    elif senOut == [1, 1, 1] or senOut == [1, 0, 1]: curve = weights[2]
    me.send_rc_control(lr, fSpeed, 0, curve)

while True:
    img = me.get_frame_read().frame
    img = cv2.resize(img, (width, height))
    img = cv2.flip(img, 0)

    imgThres = thresholding(img)
    cx = getContours(imgThres, img)  # For translation
    senOut = getSensorOutput(imgThres, sensors)  # For rotation
    sendCommands(senOut, cx)

    cv2.imshow("Output", img)
    cv2.imshow("Path", imgThres)
    cv2.waitKey(1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        me.land()
        break