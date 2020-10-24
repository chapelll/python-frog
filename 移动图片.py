import os
import shutil
import numpy as np
import pandas as pd

img111 = 'C:\\Users\\ZCZ\\Desktop\\goodImage\\4.jpg'
#获取图片
# path_img = 'C:\\Users\\ZCZ\\Desktop\\goodImage\\'
# ls = os.listdir(path_img)
# lenl = len(ls)
# print(len(ls))

# for i in range(lenl):
#     # if i.find('testnan')!=-1:
shutil.move(img111, "C:\\Users\\ZCZ\\Desktop\\badImage\\")
    # print(i, name[i])