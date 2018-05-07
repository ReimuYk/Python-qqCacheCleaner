import os
from tkinter import *
from PIL import Image,ImageTk

path = "F:/"

def getSuffix(filelist):
    res = set('')
    for item in filelist:
        temp = item.split('.')
        if len(temp)>1:
            res.add(temp[-1])
    return res

def getSuffixFile(filelist,suf):
    res = []
    for item in filelist:
        temp = item.split('.')
        if temp[-1]==suf:
            res.append(item)
    return res

pictureSize=200
class picCell:
    def __init__(self,root):
        self.f = Frame(root,width=pictureSize,height=pictureSize,bg='red')
        self.c = Canvas(self.f,width=pictureSize,height=pictureSize,bg='gray')
        self.c.bind("<ButtonPress-1>",self.leftDown)
        self.c.bind("<ButtonRelease-1>",self.leftUp)
##        self.c.bind("<B1-Motion>",self.motion)
        self.c.pack()
    def leftDown(self,e):
        print("left",e.x,e.y)
        print(self.fname)
    def leftUp(self,e):
        print("up",e.x,e.y)
        print(self.fname)
    def motion(self,e):
        print(e.x,e.y)
    def setPic(self,filename):
        self.fname = filename
        self.pic = Image.open(filename)
        self.resize()
        self.im = ImageTk.PhotoImage(self.pic)
        self.p = self.c.create_image(int(pictureSize/2),int(pictureSize/2),image=self.im)
    def removePic(self):
        self.fname = None
        self.pic = None
        self.im = None
        self.p = None
    def grid(self,r,c):
        self.f.grid(row=r,column=c)
    def resize(self):
        size = self.pic.size
        if size[0]<=size[1]:
            newsize=(int(pictureSize*size[0]/size[1]),pictureSize)
            self.pic = self.pic.resize(newsize)
        else:
            newsize=(pictureSize,int(pictureSize*size[1]/size[0]))
            self.pic = self.pic.resize(newsize)

class GUI:
    def __init__(self):
        self.tk = Tk()
        Label(self.tk,text="Cache Dir:").grid(row=0,column=0)
        self.cacheDir = StringVar()
        Entry(self.tk,textvariable=self.cacheDir).grid(row=0,column=1)
        Label(self.tk,text="Dest Dir:").grid(row=1,column=0)
        self.destDir = StringVar()
        Entry(self.tk,textvariable=self.destDir).grid(row=1,column=1)
        c1 = picCell(self.tk)
        c1.setPic("F:/胡雨奇.jpg")
        c1.grid(2,1)
        c2 = picCell(self.tk)
        c2.setPic("F:\_Main\程序设计\Python3\imgEditor\out.png")
        c2.grid(3,1)
        self.tk.mainloop()
    def getCacheDir(self):
        return self.cacheDir.get()
    def getDestDir(self):
        return self.destDir.get()
        
##files = os.listdir(path)
##g = getSuffix(files)
g = GUI()
