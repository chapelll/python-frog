import cv2

vc = cv2.VideoCapture('D:/python/demo1/video/1570542967.mp4')#抓取视频
n = 1  # 计数

if vc.isOpened():  # 判断是否正常打开
    rval, frame = vc.read()
else:
    rval = False

timeF = 10  # 视频帧计数间隔频率

i = 0 #开始命名
while rval:  # 循环读取视频帧
    rval, frame = vc.read()
    if (n % timeF == 0):  # 每隔timeF帧进行存储操作
        i += 1
        print(i)
        cv2.imwrite('D:/python/demo1/images/{}.jpg'.format(i), frame)  # 存储为图像
    n = n + 1

vc.release()
