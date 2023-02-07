import cv2 as cv 
import tkinter as tk 
from tkinter import filedialog
background=cv.imread("template.png")
mh,mw,_=background.shape
def event(event,x,y,flag,peram):
    if event==cv.EVENT_LBUTTONDBLCLK:
        cond1=x>=400 and x<=675
        cond2=y>=640 and y<=680
        if cond1 and cond2:
            root=tk.Tk()
            root.withdraw()
            filePath=filedialog.askopenfilename()
            img=cv.imread(filePath)
            img=cv.resize(img, (300,300))
            sh,sw,_=img.shape
            cx,cy=int(mw/2-sw/2),int(mh/2-sh/2)
            background[cy:cy+sh,cx:cx+sw]=img
            cv.rectangle(background, (cx,cy), (cx+sw,cy+sh), (0,0,0))
while True:
    cv.namedWindow("select image")
    cv.setMouseCallback("select image", event)
    cv.imshow("select image", background)
    if cv.waitKey(1)==ord("q"):
        break
cv.destroyAllWindows()