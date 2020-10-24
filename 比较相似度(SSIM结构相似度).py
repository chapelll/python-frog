from skimage.measure import compare_ssim
import imageio
import numpy as np

img1 = imageio.imread('C://Users//ZCZ//Desktop//青蛙//图虫上的青蛙图片//5.jpg')
img2 = imageio.imread('C://Users//ZCZ//Desktop//青蛙//图虫上的青蛙图片//452.jpg')

img2 = np.resize(img2, (img1.shape[0], img1.shape[1], img1.shape[2]))

print(img2.shape)
print(img1.shape)
ssim = compare_ssim(img1, img2, multichannel=True)

print(ssim)
print("两张图片的相似度为：" + '%.2f%%' % (ssim * 100))  #ssim就是图片相似度的百分数

