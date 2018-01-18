# coding: utf-8
import itchat
import os
import PIL.Image as Image
from os import listdir
import math
import wechat_friends

#打印二维码
#itchat.auto_login(enableCmdQR=True)
#出现图片

itchat.auto_login(hotReload=True)
friends = itchat.get_friends(update=True)[0:]
wechat_friends.to_print()
user = friends[0]["UserName"]
#print(user)
os.mkdir(user)
num = 0
for i in friends:
	img = itchat.get_head_img(userName=i["UserName"])
	fileImage = open(user + "/" + str(num) + ".jpg",'wb')
	fileImage.write(img)
	fileImage.close()
	num += 1
pics = listdir(user)
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
		#打开图片
		img = Image.open(user + "/" + i)
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
img1.save(user + ".jpg")

itchat.send_image(user + ".jpg", 'filehelper')