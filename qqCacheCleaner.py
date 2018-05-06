import os

path = "F:/"

def getSuffix(filelist):
    res = set('')
    for item in filelist:
        temp = item.split('.')
        if len(temp)>1:
            res.add(temp[-1])
    return res
    
files = os.listdir(path)
g = getSuffix(files)
