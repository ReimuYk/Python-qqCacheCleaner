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

class picCell:
    def __init__(self,root):
        self.f = Frame(root,width=400,height=400,bg='red')
        self.c = Canvas(self.f,width=400,height=400,bg='gray')
        self.c.pack()
    def setPic(self,filename):
        self.fname = filename
        self.pic = Image.open(filename)
        self.resize()
        self.im = ImageTk.PhotoImage(self.pic)
        self.p = self.c.create_image(200,200,image=self.im)
    def grid(self,r,c):
        self.f.grid(row=r,column=c)
    def resize(self):
        size = self.pic.size
        if size[0]<=size[1]:
            newsize=(int(400*size[0]/size[1]),400)
            self.pic = self.pic.resize(newsize)
        else:
            newsize=(400,int(400*size[1]/size[0]))
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
        c1.setPic("F:\_Main\程序设计\Python3\imgEditor\out.png")
        c1.grid(2,0)
        self.tk.mainloop()
        
##files = os.listdir(path)
##g = getSuffix(files)
g = GUI()
