# coding: utf-8
import itchat
import os
import PIL.Image as Image
from os import listdir
import math
import random
dir='G:/！Github/python/images/yike'
pics = listdir(dir)
numPic = len(pics)
print(u"总人数："+str(numPic))
#eachsize = int(math.sqrt(float(630 * 630) / numPic))
#print(u"容纳照片："+str(eachsize))
#numline = int(630 / eachsize)
numline=9#生成numline*numline的图片
numrow=10
toImage = Image.new('RGBA', (numline*numrow*10, numline*numrow*10))#整个图片大小toImage
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
		img = img.resize((numrow*10, numrow*10), Image.ANTIALIAS)
		#拼接图片
		toImage.paste(img, (x * numrow*10, y * numrow*10))
		x += 1
		if x == numline:
			x = 0
			y += 1
# print len(toImage.split())
if len(toImage.split()) == 4:
    r, g, b, a = toImage.split()
img1 = Image.merge("RGB", (r, g, b))
dir2='G:/！Github/python/images/'
z=random.randrange(0, 101, 2)
img1.save(dir2+ "/"+str(z)+ ".jpg")
print(dir2+ "/"+str(z)+ ".jpg")
