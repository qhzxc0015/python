# coding: utf-8
import itchat
import os
import PIL.Image as Image
from os import listdir
import math

#打印二维码
#itchat.auto_login(enableCmdQR=True)
#出现图片
name=u"京东2018届宝宝（总部①群）"
#通过群名得到群username
def getroom_message():
    itchat.dump_login_status()
    RoomList = itchat.search_chatrooms(name=name)
    if RoomList is None:
        print("%s group is not found!" % (name))
    else:
        return RoomList[0]['UserName']
itchat.auto_login(hotReload=True)
groups = itchat.get_chatrooms(update=True)[0:]
for i in range(len(groups)):
	print (groups[i]["NickName"])
ChatRoom = itchat.update_chatroom(getroom_message(), detailedMember=True)
total = len(ChatRoom['MemberList'])

user = groups[0]["UserName"]
print(user)

os.mkdir(user)
num = 0
for i in range(total):
	img = itchat.get_head_img(userName=ChatRoom['MemberList'][i]["UserName"],chatroomUserName=getroom_message())
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
		# 打开图片
		img = Image.open(user + "/" + i)
	except IOError:
		print("Error: 没有找到文件或读取文件失败")
	else:
		# 缩小图片
		img = img.resize((eachsize, eachsize), Image.ANTIALIAS)
		# 拼接图片
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