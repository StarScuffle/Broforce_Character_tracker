from ctypes import windll
dc = windll.user32.GetDC(0)

def getpixel(x,y):
    return windll.gdi32.GetPixel(dc,x,y)

import time

arr = []
time.sleep(5)
for x in range(0,100):
    arr_y=[]
    for y in range(900,1037):
        arr_y.append(getpixel(x,y))
    print(str(x)+'% completed')
    arr.append(arr_y)

from PIL import Image
from utilites import *

img = Image.new('RGB',(100,137))

for x in range(len(arr)):
    for y in range(len(arr[0])):
        img.putpixel((x,y),decimal_to_RGB(arr[x][y]))
