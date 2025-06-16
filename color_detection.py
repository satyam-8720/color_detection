import cv2 as cv
import numpy as np

def getlimit(color):
    bgr=np.uint8([[color]])
    hsvc=cv.cvtColor(bgr,cv.COLOR_BGR2HSV)

    lower_limit=np.array([max(hsvc[0][0][0]-10,0),100,100],dtype='uint8')  
    upper_limit=np.array([min(hsvc[0][0][0]+10,179),255,255],dtype='uint8')
    # max and min used for boundary cases

    return lower_limit,upper_limit

bgr_color=[0,255,255] #yellow
lower_limit,upper_limit=getlimit(bgr_color)

vid=cv.VideoCapture(0)

while(True):
    isTrue,frame=vid.read()
    hsv_frame=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    mask=cv.inRange(hsv_frame,lower_limit,upper_limit)
    #cv.imshow("mask",mask)
    contours,_ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        area = cv.contourArea(contour)
        if area > 500:  # Filter small noise
            x, y, w, h = cv.boundingRect(contour)
            cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Green box
            cv.imshow("detected",frame)

    if cv.waitKey(20) & 0xff==ord('d'):
        break 

vid.release()
cv.destroyAllWindows()