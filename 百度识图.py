# encoding:utf-8

import requests
import base64

'''
动物识别
'''

request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/animal"
# 二进制方式打开图片文件
f = open('C:\\Users\\ZCZ\\Desktop\\源图像\\3.jpg', 'rb')
img = base64.b64encode(f.read())

params = {"image":img}
access_token = "24.7a875e62b90321e08004ed6ddbd9cab1.2592000.1605099709.282335-22809941"
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print (response.json())