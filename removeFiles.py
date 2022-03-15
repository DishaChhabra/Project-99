import os
import shutil
import time

#/Desktop/new folder/.docx
path = input('enter the path : ')
seconds = time.time() - (30*24*60*60)
if os.path.exists(path):
    files = os.listdir(path)
    print(seconds)
    for i in files:
        ctime = os.stat(path+'/'+i).st_ctime
        print(ctime)
        if seconds<ctime:
            os.remove(path+'/'+i)
            print(i, 'has been deleted')
else:
    print('path does not exist.')