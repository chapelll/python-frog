from PIL import Image
import shutil
import os
#比较函数
def bijiao(path):
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
    print(total_num)

    number = 1
    img1 = Image.open(path+'1.jpg')

    while number < len(filelist):       #遍历该文件夹中的所有文件
        number = number + 1
        img2 = Image.open(path + str(number) + '.jpg')
        equalProbability = (similar(img1, img2))

        # if (equalProbability > 0.8):  #如果有图片和参照图的相似度超过了80%，就将这张图片移走
        #     moveImg = 'C:\\Users\\ZCZ\\Desktop\\pyTest\\' + str(number) + '.jpg'
        #     shutil.move(moveImg, "C:\\Users\\ZCZ\\Desktop\\badImage\\")

        # equalProbability = "第"+ str(number) +"张图片与参照图的相似度为：" + '%.1f%%' % (similar(img1, img2) * 100)
        print("第" + str(number) + "张图片与参照图的相似度为：" + '%.1f%%' % (equalProbability * 100))


bijiao('C://Users//ZCZ//Desktop//青蛙//总集2//') #调用比较函数，传入的是你想要比较的图片集的地址