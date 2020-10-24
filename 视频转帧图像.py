import cv2

vc = cv2.VideoCapture('D:/python/FrogVideo/青蛙视频10.mp4')#抓取视频
n = 1 #计数

if vc.isOpened():#确认视频是否打开
    rval, frame = vc.read()
else:
    rval = False

timeF = 25 #视频帧计数间隔频率

i = 0 #给图片命名(从第一张开始)

while rval:
    rval, frame = vc.read()  # 获取视频的帧图像
    if (n % timeF == 0):     # 每隔timeF帧进行存储操作
        i += 1
        print(i)
        cv2.imwrite('D:/python/FrogPhotos/video10toPhotos/{}.jpg'.format(i), frame)  # 存储图像位置
    n = n + 1

vc.release()#释放

# while rval:
#     rval, frame = vc.read()#获取视频的帧图像
#     if (rval!=0):
#         cv2.imwrite('D:/python/demo1/images/' + str(c) + '.jpg', frame)#将帧图像输出为jpg格式文件到路径中
#         c += 1
#         print(c)
#
# vc.release()#释放
