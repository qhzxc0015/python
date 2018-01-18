# coding: utf-8
import itchat
import os
import PIL.Image as Image
from os import listdir
import math
import random
dir='G:/！Github/python/images/jd_alll'
pics = listdir(dir)
numPic = len(pics)
print(u"总人数："+str(numPic))
eachsize = int(math.sqrt(float(1280 * 1280) / numPic))
print(u"容纳照片："+str(eachsize))
numline = int(1280 / eachsize)
toImage = Image.new('RGBA', (1280, 1280))
print(u"每行数照片数："+str(numline))
x = 0
y = 0
for i in pics:
	try:
		# 打开图片
		img = Image.open(dir + "/" + i)
	except IOError:
		print("Error: 没有找到文件或读取文件失败")
	else:
		#缩小图片
		img = img.resize((eachsize, eachsize), Image.ANTIALIAS)
		#拼接图片
		toImage.paste(img, (x * eachsize, y * eachsize))
		x += 1
		if x == numline:
			x = 0
			y += 1
# print len(toImage.split())
if len(toImage.split()) == 4:
    r, g, b, a = toImage.split()
img1 = Image.merge("RGB", (r, g, b))
dir2='G:/！Github/python/images/image'
img1.save(dir2+ "/"+str(random.randrange(0, 101, 2))+ ".jpg")
print(dir2+ "/"+str(random.randrange(0, 101, 2))+ ".jpg")
