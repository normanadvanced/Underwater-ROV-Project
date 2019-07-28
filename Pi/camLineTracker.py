import cv2
import numpy as np


cam = cv2.VideoCapture(0)#THIS NEEDS TO BE CHANGED TO A PICAM
maxAreaContour = 1000 #This will need to be adjusted
minAreaContour = 10
redy = 152
greeny = 445 #needs adjusted
while True:
    ret, img = cam.read()#just make sure that you're using a picam here
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(img,30,200)
    ret, thresh = cv2.threshold(img, 180, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    iter = 0
    for i in contours:
        areaContour = cv2.contourArea(i)
        #print(areaContour)        
        areatol = areaContour >= minAreaContour and areaContour <= maxAreaContour
        
        sum = 0
        for j in i:
            sum += j[0][1] #1 is y, 0 is x for the second array indicy
        mean = sum / len(i)
        redtol = mean > redy - 3 and mean < redy + 3
        greentol = mean > greeny - 3 and mean < greeny + 3
        
        #if areatol:
        #    cv2.drawContours(img, contours, iter, (0,255,0), 3)
        #    iter += 1
        #else:
        #    iter += 1
        #    continue
            
        if redtol and areatol:
            print("red")
            min = 9999999
            for j in i:
                if j[0][0] < min:
                    min = j[0][0]
            print(min)
        elif greentol and areatol:
            print("green")
            max = -1
            for j in i:
                if j[0][0] > max:
                    max = j[0][0]
            print(max)
        
    cv2.imshow("contours", img)
    cv2.waitKey(1000)
