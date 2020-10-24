import cv2
import numpy as np
import matplotlib
import os

matplotlib.use('TkAgg')

def pHash(img):
    # 感知哈希算法
    # 缩放32*32
    img = cv2.resize(img, (32, 32))  # , interpolation=cv2.INTER_CUBIC

    # 转换为灰度图
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 将灰度图转为浮点型，再进行dct变换
    dct = cv2.dct(np.float32(gray))
    # opencv实现的掩码操作
    dct_roi = dct[0:8, 0:8]

    hash = []
    avreage = np.mean(dct_roi)
    for i in range(dct_roi.shape[0]):
        for j in range(dct_roi.shape[1]):
            if dct_roi[i, j] > avreage:
                hash.append(1)
            else:
                hash.append(0)
    return hash

def cmpHash(hash1, hash2):
    # Hash值对比
    # 算法中1和0顺序组合起来的即是图片的指纹hash。顺序不固定，但是比较的时候必须是相同的顺序。
    # 对比两幅图的指纹，计算汉明距离，即两个64位的hash值有多少是不一样的，不同的位数越少，图片越相似
    # 汉明距离：一组二进制数据变成另一组数据所需要的步骤，可以衡量两图的差异，汉明距离越小，则相似度越高。汉明距离为0，即两张图片完全一样
    n = 0
    # hash长度不同则返回-1代表传参出错
    if len(hash1) != len(hash2):
        return -1
    # 遍历判断
    for i in range(len(hash1)):
        # 不相等则n计数+1，n最终为相似度
        if hash1[i] != hash2[i]:
            n = n + 1
    return n
    # n就是不相等的位数，如果n小于5，那么图片非常相似；如果n大于10，就视为不同的图片(大于0.86视为相似图片)

# def runAllImageSimilaryFun(para1, para2):
#
#     img1 = cv2.imread(para1)
#     img2 = cv2.imread(para2)
#
#     hash1 = pHash(img1)
#     hash2 = pHash(img2)
#     n3 = cmpHash(hash1, hash2)
#     # print('感知哈希算法相似度pHash：', n3)
#     print("使用感知哈希算法得出的相似度: " + '%.2f%%' % ((1 - float(n3 / 64)) * 100))


def Phash(path,p2):
    filelist = os.listdir(path)  # 获取文件路径
    max = len(filelist)  # 获取文件长度（个数）
    print(max)
    sameImage = []
    for i in range(1,max + 1):
        # runAllImageSimilaryFun(path + str(i) +'.jpg', p2)
        img1 = cv2.imread(path + str(i) +'.jpg')
        img2 = cv2.imread(p2)
        hash1 = pHash(img1)
        hash2 = pHash(img2)
        n3 = cmpHash(hash1, hash2)
        print(n3)
        Similarity = (1 - float(n3 / 64))
        if Similarity > 0.86:
            sameImage.append(str(i) + '.jpg')
        print('第' + str(i) + "张图与参照图的相似度: " + '%.2f%%' % (Similarity * 100))
    print('与' + p2[39:] + '相似度超过百分之86%的图片有:' + str(sameImage))


Phash("C:/Users/ZCZ/Desktop/frog/tuchong-frog/","C:/Users/ZCZ/Desktop/frog/tuchong-frog/30.jpg")