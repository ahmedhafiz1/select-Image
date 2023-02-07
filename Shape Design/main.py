import cv2 as cv 
import tkinter as tk 
from tkinter import filedialog
import os 
temp=cv.imread("template.png")
mh,mw,mc=temp.shape
folderPath="image"
imgPathList=os.listdir(folderPath)
imgList=[]
for path in imgPathList:
    img=cv.imread(f"{folderPath}/{path}")
    imgList.append(img)
print(len(imgList))
def event(event,x,y,flag,peram):
    if event==cv.EVENT_LBUTTONDBLCLK:
        cond_1=x>=425 and x<=680
        cond_2=y>=640 and y<=675
        if cond_1 and cond_2:
            root=tk.Tk()
            root.withdraw()
            filePath=filedialog.askopenfilename()
            img=cv.imread(filePath) 
            img=cv.resize(img, (0,0),None,0.5,0.5)
            sh,sw,sc=img.shape
            cy,cx=int((mh/2-sh/2)),int((mw/2-sw/2))
            temp[cy:cy+sh,cx:cx+sw]=img
while True:
    cv.namedWindow("Select Image")
    cv.setMouseCallback("Select Image", event)
    cv.imshow("Select Image", temp)
    if cv.waitKey(1)==ord("q"):
        cv.destroyAllWindows()
        break