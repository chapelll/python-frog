#1.批量重命名所有图像
#2.拿到第一张图像 1.jpg 将它与所有其他图像进行对比，与他相似度超过80%的放到 test-bad 文件夹
#3.将第一张图片 1.jpg 重新命名(添加时间标记) 放到 test-good 文件夹 (它已经通过筛选)
import os
from PIL import Image
import shutil

def Rename(path):

    #重命名脚本
    #path表示待处理的文件夹路径

    filelist = os.listdir(path)  # 获取文件路径
    total_num = len(filelist)  # 获取文件长度（个数）
    i = 1  # 表示文件的命名是从1开始的
    for item in filelist:
        if item.endswith('.jpg'):  # 初始的图片的格式为jpg格式的（或者源文件是png格式及其他格式，后面的转换格式就可以调整为自己需要的格式即可）
            src = os.path.join(os.path.abspath(path), item)
            dst = os.path.join(os.path.abspath(path),
                               format(str(i), '0>1s') + '.jpg')  # 处理后的格式也为jpg格式的，当然这里可以改成png格式
            # dst = os.path.join(os.path.abspath(self.path),  format(str(i)) + '.jpg')#处理后的格式也为jpg格式的，当然这里可以改成png格式

            # 这种情况下的命名格式为xn000.jpg形式，可以自主定义想要的格式
            try:
                os.rename(src, dst)
                print('converting %s to %s ...' % (src, dst))
                i = i + 1
            except:
                continue
    print('total %d to rename & converted %d jpgs' % (total_num, i))


def bijiao(path,pathGood,pathBad):

    # SSIM比较相似度脚本
    # path表示待处理的文件夹路径

    def hash_img(img):  # 计算图片的特征序列
        a = []  # 存储图片的像素
        hash_img = ''  # 特征序列
        width, height = 200, 200  # 图片缩放大小
        img = img.resize((width, height))  # 图片缩放为width×height
        for y in range(img.height):
            b = []
            for x in range(img.width):
                pos = x, y
                color_array = img.getpixel(pos)  # 获得像素
                color = sum(color_array) / 3  # 灰度化
                b.append(int(color))
            a.append(b)
        for y in range(img.height):
            avg = sum(a[y]) / len(a[y])  # 计算每一行的像素平均值
            for x in range(img.width):
                if a[y][x] >= avg:  # 生成特征序列,如果此点像素大于平均值则为1,反之为0
                    hash_img += '1'
                else:
                    hash_img += '0'

        return hash_img

    def similar(img1, img2):  # 求相似度
        hash1 = hash_img(img1)  # 计算img1的特征序列
        hash2 = hash_img(img2)  # 计算img2的特征序列
        differnce = 0
        for i in range(len(hash1)):
            differnce += abs(int(hash1[i]) - int(hash2[i]))
        similar = 1 - (differnce / len(hash1))
        return similar

    filelist = os.listdir(path)  # 获取文件路径
    total_num = len(filelist)  # 获取文件长度（个数）

    #path: 'C:\\Users\\ZCZ\\Desktop\\pyTest\\'

    number = 1
    img1 = Image.open(path+'1.jpg')

    while number < len(filelist):       #遍历该文件夹中的所有文件
        number = number + 1
        img2 = Image.open(path + str(number) + '.jpg')
        equalProbability = (similar(img1, img2))

        if (equalProbability > 0.8):  #如果有图片和参照图的相似度超过了80%，就将这张图片移走
            moveImg = path + str(number) + '.jpg'
            shutil.move(moveImg, pathBad)

        # equalProbability = "第"+ str(number) +"张图片与参照图的相似度为：" + '%.1f%%' % (similar(img1, img2) * 100)
        print("第" + str(number) + "张图片与参照图的相似度为：" + '%.1f%%' % (equalProbability * 100))





#Rename('C:\\Users\\ZCZ\\Desktop\\青蛙\\test\\')
bijiao('C:\\Users\\ZCZ\\Desktop\\青蛙\\test\\','C:\\Users\\ZCZ\\Desktop\\青蛙\\testGood\\','C:\\Users\\ZCZ\\Desktop\\青蛙\\testBad\\')
