# coding:utf-8
import itchat

# 热登录，不必每次扫码
itchat.auto_login(hotReload=True)
#固定群名称
name = u'京东2018届宝宝（北京②群）'

#获取群信息
def getroom_message():
    itchat.dump_login_status()
    RoomList = itchat.search_chatrooms(name=name)
    if RoomList is None:
            print("%s group is not found!" % (name))
    else:
        return RoomList[0]['UserName']

#输出所需信息
ChatRoom = itchat.update_chatroom(getroom_message(), detailedMember=True)
total = len(ChatRoom['MemberList'])
for i in range(total):
    print(ChatRoom['MemberList'][i]['DisplayName'], ChatRoom['MemberList'][i]["NickName"],
          ChatRoom['MemberList'][i]['Signature'])
    print("ID：")
    print(ChatRoom['MemberList'][i]["UserName"])
    print("备注：")
    print(ChatRoom['MemberList'][i]['DisplayName'])
    print("姓名：")
    print(ChatRoom['MemberList'][i]["NickName"])
    print("个人标签：")
    print(ChatRoom['MemberList'][i]['Signature'])
    print("---------------------")

# 初始化计数器，有男有女，当然，有些人是不填的
#male = female = other = 0

# 遍历这个列表，列表里第一位是自己，所以从"自己"之后开始计算
# 1表示男性，2女性
#for i in friends[1:]:
#    sex = i["Sex"]
#    if sex == 1:
#        male += 1
#    elif sex == 2:
#        female += 1
#    else:
#        other += 1

# 总数算上，好计算比例啊～
#total = len(friends[1:])
#total_g=len(groups[0:])

# 好了，打印结果
#print(u'群聊数目：%d' % total_g )
#print(u"男性好友：%.2f%%" % (float(male) / total * 100))
#print(u"女性好友：%.2f%%" % (float(female) / total * 100))
#print(u"未填性别：%.2f%%" % (float(other) / total * 100))
#for i in range(0,6):
#    print(groups[i]["NickName"])

