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

pictureSize=150
class picCell:
    def __init__(self,canvas,x,y):
        self.c=canvas
        self.x = x
        self.y = y
        self.fname = None
    def setPic(self,filename):
        self.fname = filename
        self.pic = Image.open(filename)
        self.resize()
        self.im = ImageTk.PhotoImage(self.pic)
        self.p = self.c.create_image(self.x,self.y,image=self.im)
    def removePic(self):
        self.fname = None
        self.pic = None
        self.im = None
        self.p = None
    def resize(self):
        size = self.pic.size
        if size[0]<=size[1]:
            newsize=(int(pictureSize*size[0]/size[1]),pictureSize)
            self.pic = self.pic.resize(newsize)
        else:
            newsize=(pictureSize,int(pictureSize*size[1]/size[0]))
            self.pic = self.pic.resize(newsize)

class CtrlBoard:
    def __init__(self,root):
        self.cellWidth = 150
        self.cellHeight = 150
        self.c = Canvas(root,height=self.cellHeight*5,width=self.cellWidth*7,bg='white')
        self.c.grid(row=2,column=1,rowspan=5)
        self.cells = []
        for i in range(5):
            self.cells.append([])
            for j in range(7):
                temp = picCell(self.c,self.cellWidth*(j+0.5),self.cellHeight*(i+0.5))
                self.cells[-1].append(temp)
        for i in range(1,5):
            self.c.create_line((0,self.cellHeight*i,self.cellWidth*7,self.cellHeight*i),width=2)
        for i in range(1,7):
            self.c.create_line((self.cellWidth*i,0,self.cellWidth*i,self.cellHeight*5),width=2)
        self.c.bind("<ButtonPress-1>",self.leftDown)
        self.c.bind("<ButtonRelease-1>",self.leftUp)
        self.downIndex=None
        self.upIndex=None
    def setPic(self,filename,xi,yi):
        self.cells[xi][yi].setPic(filename)
    def removePic(self,xi,yi):
        self.cells[xi][yi].removePic()
    def reset(self,oldIndex,newIndex):
        if oldIndex==newIndex:
            print("same")
            return
        if self.getCell(newIndex).fname!=None:
            print("occupied")
            return
        if self.getCell(oldIndex).fname==None:
            print("nothing")
            return
        ff = self.getCell(oldIndex).fname
        self.setPic(ff,newIndex[1],newIndex[0])
        self.removePic(oldIndex[1],oldIndex[0])
    def getCell(self,index):
        return self.cells[index[1]][index[0]]
    def getCellIndex(self,x,y):
        xi = int(x/self.cellWidth)
        yi = int(y/self.cellHeight)
        return (xi,yi)
    def leftDown(self,e):
        print("down",self.getCellIndex(e.x,e.y))
        self.down = self.getCellIndex(e.x,e.y)
    def leftUp(self,e):
        print("up",self.getCellIndex(e.x,e.y))
        self.up = self.getCellIndex(e.x,e.y)
        self.reset(self.down,self.up)
class GUI:
    def __init__(self):
        self.tk = Tk()
        Label(self.tk,text="Cache Dir:").grid(row=0,column=0)
        self.cacheDir = StringVar()
        Entry(self.tk,textvariable=self.cacheDir).grid(row=0,column=1)
        Label(self.tk,text="Dest Dir:").grid(row=1,column=0)
        self.destDir = StringVar()
        Entry(self.tk,textvariable=self.destDir).grid(row=1,column=1)
##        c1 = picCell(self.tk)
##        c1.setPic("F:/胡雨奇.jpg")
##        c1.grid(2,1)
##        c2 = picCell(self.tk)
##        c2.setPic("F:\_Main\程序设计\Python3\imgEditor\out.png")
##        c2.grid(3,1)
        cb = CtrlBoard(self.tk)
        cb.setPic("F:\_Main\程序设计\Python3\imgEditor\out.png",1,4)
        self.tk.mainloop()
    def getCacheDir(self):
        return self.cacheDir.get()
    def getDestDir(self):
        return self.destDir.get()
        
##files = os.listdir(path)
##g = getSuffix(files)
g = GUI()
