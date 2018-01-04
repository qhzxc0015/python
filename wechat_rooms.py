# coding:utf-8
import itchat
import xlwt

# 热登录，不必每次扫码
itchat.auto_login(hotReload=True)
print ("已登录")
groups = itchat.get_chatrooms(update=True)[0:]
total_g=len(groups)
for i in range(total_g):
    print(groups[i]["NickName"])
# 固定群名称
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
if __name__=="__main__":
    ChatRoom = itchat.update_chatroom(getroom_message(), detailedMember=True)
    total = len(ChatRoom['MemberList'])
    wb = xlwt.Workbook()
    ws = wb.add_sheet('JD_2')
    ws.write(0, 0, u"昵称")
    ws.write(0, 1, u"性别")
    ws.write(0, 2, u"备注")
    ws.write(0, 3, u"个人标签")
    ws.write(0, 4, u"省份")
    ws.write(0, 5, u"城市")
    ws.write(0, 6, u"总人数:%d" % total)
    male = female = other = 0
    for i in range(total):
        if ChatRoom['MemberList'][i]["Sex"] == 1:
            male += 1
        elif ChatRoom['MemberList'][i]["Sex"] == 2:
            female += 1
        else:
            other += 1
    ws.write(1, 6, u"男性比例：%.2f%%" % (float(male) / total * 100))
    ws.write(2, 6, u"女性比例：%.2f%%" % (float(female) / total * 100))
    ws.write(3, 6, u"其他比例：%.2f%%" % (float(other) / total * 100))
    for i in range(total):
        ws.write(i+1, 0, ChatRoom['MemberList'][i]['NickName'])
        if ChatRoom['MemberList'][i]["Sex"] == 1:
            ws.write(i+1, 1, u'男')
        elif ChatRoom['MemberList'][i]["Sex"] == 2:
            ws.write(i+1, 1, u'女')
        else:
            ws.write(i+1, 1, u'其他')
        ws.write(i+1, 2, ChatRoom['MemberList'][i]['DisplayName'])
        ws.write(i+1, 3, ChatRoom['MemberList'][i]['Signature'])
        ws.write(i+1, 4, ChatRoom['MemberList'][i]['Province'])
        ws.write(i+1, 5, ChatRoom['MemberList'][i]['City'])
#        ws.write(i+1, 6, ChatRoom['MemberList'][i]['OwnerUin'])#RemarkName是对群内好友的个人备注，可以看到群内好友
#        ws.write(i, 4, ChatRoom['MemberList'][i]['UserName'])
    wb.save('G:\github\python\excels\JD_members.xls')
    print ("ok")