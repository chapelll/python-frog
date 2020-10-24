import os
import string

dirName = "C:\\Users\\ZCZ\\Desktop\\青蛙\\test\\"  # 最后要加双斜杠，不然会报错 C:\Users\ZCZ\Desktop\青蛙\总集2
li = os.listdir(dirName)
for filename in li:
    newname = filename
    newname = newname.split(".")
    if newname[-1] == "png" or newname[-1] == "jpeg" or newname[-1] == "bmp" or newname[-1] == "jfif" or newname[-1] == "JPG":
        # 将后缀名为 png 或者 jpeg 或者 bmp 的图片找出来
        newname[-1] = "jpg"
        newname = str.join(".", newname)  # 这里要用str.join
        filename = dirName + filename
        newname = dirName + newname
        os.rename(filename, newname)
        print(newname, "updated successfully")
