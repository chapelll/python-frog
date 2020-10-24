import cv2
import numpy as np
from PIL import Image
import requests
from io import BytesIO
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def calculate(image1, image2):
    # 灰度直方图算法
    # 计算单通道的直方图的相似值
    hist1 = cv2.calcHist([image1], [0], None, [256], [0.0, 255.0])
    hist2 = cv2.calcHist([image2], [0], None, [256], [0.0, 255.0])
    # 计算直方图的重合度
    degree = 0
    for i in range(len(hist1)):
        if hist1[i] != hist2[i]:
            degree = degree + \
                     (1 - abs(hist1[i] - hist2[i]) / max(hist1[i], hist2[i]))
        else:
            degree = degree + 1
    degree = degree / len(hist1)
    return degree


def classify_hist_with_split(image1, image2, size=(256, 256)):
    # RGB每个通道的直方图相似度
    # 将图像resize后，分离为RGB三个通道，再计算每个通道的相似值
    image1 = cv2.resize(image1, size)
    image2 = cv2.resize(image2, size)
    sub_image1 = cv2.split(image1)
    sub_image2 = cv2.split(image2)
    sub_data = 0
    for im1, im2 in zip(sub_image1, sub_image2):
        sub_data += calculate(im1, im2)
    sub_data = sub_data / 3
    return sub_data

def getImageByUrl(url):
    # 根据图片url 获取图片对象
    html = requests.get(url, verify=False)
    image = Image.open(BytesIO(html.content))
    return image


def PILImageToCV():
    # PIL Image转换成OpenCV格式
    path = "/Users/waldenz/Documents/Work/doc/TestImages/t3.png"
    img = Image.open(path)
    plt.subplot(121)
    plt.imshow(img)
    print(isinstance(img, np.ndarray))
    img = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)
    print(isinstance(img, np.ndarray))
    plt.subplot(122)
    plt.imshow(img)
    plt.show()


def CVImageToPIL():
    # OpenCV图片转换为PIL image
    path = "/Users/waldenz/Documents/Work/doc/TestImages/t3.png"
    img = cv2.imread(path)
    # cv2.imshow("OpenCV",img)
    plt.subplot(121)
    plt.imshow(img)

    img2 = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.subplot(122)
    plt.imshow(img2)
    plt.show()


def bytes_to_cvimage(filebytes):
    # 图片字节流转换为cv image
    image = Image.open(filebytes)
    img = cv2.cvtColor(np.asarray(image), cv2.COLOR_RGB2BGR)
    return img


def runAllImageSimilaryFun(para1, para2):
    # 均值、差值、感知哈希算法三种算法值越小，则越相似,相同图片值为0
    # 三直方图算法和单通道的直方图 0-1之间，值越大，越相似。 相同图片为1

    # t1,t2   14;19;10;  0.70;0.75
    # t1,t3   39 33 18   0.58 0.49
    # s1,s2  7 23 11     0.83 0.86  挺相似的图片
    # c1,c2  11 29 17    0.30 0.31

    if para1.startswith("http"):
        # 根据链接下载图片，并转换为opencv格式
        img1 = getImageByUrl(para1)
        img1 = cv2.cvtColor(np.asarray(img1), cv2.COLOR_RGB2BGR)

        img2 = getImageByUrl(para2)
        img2 = cv2.cvtColor(np.asarray(img2), cv2.COLOR_RGB2BGR)
    else:
        # 通过imread方法直接读取物理路径
        img1 = cv2.imread(para1)
        img2 = cv2.imread(para2)

    n5 = calculate(img1, img2)
    print("使用单通道直方图算法得出的相似度: " + '%.2f%%' % (round(n5[0], 2) * 100))

    n4 = classify_hist_with_split(img1, img2)
    print("使用三直方图算法得出的相似度: " + '%.2f%%' % (round(n4[0], 2) * 100))



if __name__ == "__main__":
    p1 = "D:/python/demo2/images/7.jpg"
    p2 = "D:/python/demo2/images/8.jpg"
    runAllImageSimilaryFun(p1, p2)
