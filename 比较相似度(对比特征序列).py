from PIL import Image

def hash_img(img):  # 计算图片的特征序列
    a = []  # 存储图片的像素
    hash_img = ''  # 特征序列
    width, height = 10,10  # 图片缩放大小
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

number = 1
img1 = Image.open('C:/Users/ZCZ/Desktop/hashTest/95.jpg')
img2 = Image.open('C:/Users/ZCZ/Desktop/hashTest/96.jpg')
print("两张图片的相似度为：" + '%.1f%%' % (similar(img1, img2) * 100))