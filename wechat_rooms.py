# coding:utf-8
import itchat
import xlwt

# 热登录，不必每次扫码
itchat.auto_login(hotReload=True)
print ("已登录")
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
def to_excel(x, y, args):
    wb = xlwt.Workbook()
    ws.write(x, y, args)
#输出所需信息
if __name__=="__main__":
    ChatRoom = itchat.update_chatroom(getroom_message(), detailedMember=True)
    total = len(ChatRoom['MemberList'])
    wb = xlwt.Workbook()
    ws = wb.add_sheet('JD_2')
    for i in range(total):
        ws.write(i, 0, ChatRoom['MemberList'][i]['NickName'])
        if ChatRoom['MemberList'][i]["Sex"] == 1:
            ws.write(i, 1, 'boy')
        elif ChatRoom['MemberList'][i]["Sex"] == 2:
            ws.write(i, 1, 'girl')
        else:
            ws.write(i, 1, 'other')
        ws.write(i, 2, ChatRoom['MemberList'][i]['DisplayName'])
        ws.write(i, 3, ChatRoom['MemberList'][i]['Signature'])
#        ws.write(i, 4, ChatRoom['MemberList'][i]['UserName'])
    wb.save('members.xls')
    print ("ok")