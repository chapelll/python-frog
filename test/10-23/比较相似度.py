from PIL import Image
import shutil
import os


# 比较函数
def bijiao(path, baseImg):
    def hash_img(img):  # 计算图片的特征序列
        a = []  # 存储图片的像素
        hash_img = ''  # 特征序列
        width, height = 100, 100 # 图片缩放大小
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
    max = len(filelist)  # 获取文件长度（个数）
    print(max)  # 打印文件长度

    img1 = Image.open(baseImg)
    sameImage = []

    for i in range(1, max+1):
        img2 = Image.open(path + str(i) + '.jpg')
        equalProbability = (similar(img1, img2))

        if (equalProbability > 0.70):  # 如果有图片和参照图的相似度超过了70%，就将它添加到数组
            sameImage.append(str(i) + '.jpg')

        # print("第" + str(i) + "张图片与参照图的相似度为：" + '%.1f%%' % (equalProbability * 100))
    print('与' + baseImg[-5:] + '相似度超过百分之70%的图片有:' + str(sameImage))


for i in range(1, 5 + 1):
    # 调用多次比较函数，第一个参数是比较的目录，第二个参数是每次的参照图
    bijiao('C://Users//ZCZ//Desktop//青蛙//图虫上的青蛙图片//',
           'C://Users//ZCZ//Desktop//青蛙//图虫上的青蛙图片//' + str(i) + '.jpg')  # 调用比较函数，传入的是你想要比较的图片集的地址
