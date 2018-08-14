# coding:utf-8
import itchat
import xlwt
import time

# 热登录，不必每次扫码
itchat.auto_login(hotReload=True)
print ("微信已登录")

def begin(wb,name):
    # 注意，如果保存通文件会覆盖sheet
    ws = wb.add_sheet(name, cell_overwrite_ok=False)
    # 第一行信息
    ws.write(0, 0, u"昵称")
    ws.write(0, 1, u"性别")
    ws.write(0, 2, u"备注名")
    ws.write(0, 3, u"省份")
    ws.write(0, 4, u"城市")
    ws.write(0, 5, u"个人标签")
    ws.write(0, 6, u"所属群组")
    ws.write(0, 7, u"总人数:%d" % total)
    # 求男女比例
    male = female = other = 0
    for i in range(total):
        if ChatRoom['MemberList'][i]["Sex"] == 1:
            male += 1
        elif ChatRoom['MemberList'][i]["Sex"] == 2:
            female += 1
        else:
            other += 1
    ws.write(1, 7, u"男性比例：%.2f%%" % (float(male) / total * 100))
    ws.write(2, 7, u"女性比例：%.2f%%" % (float(female) / total * 100))
    ws.write(3, 7, u"其他比例：%.2f%%" % (float(other) / total * 100))
    # 各种信息存入excel
    for i in range(total):
        # 1昵称
        ws.write(i + 1, 0, ChatRoom['MemberList'][i]['NickName'])
        # 2性别
        if ChatRoom['MemberList'][i]["Sex"] == 1:
            ws.write(i + 1, 1, u'男')
        elif ChatRoom['MemberList'][i]["Sex"] == 2:
            ws.write(i + 1, 1, u'女')
        else:
            ws.write(i + 1, 1, u'其他')
        # 3备注名
        ws.write(i + 1, 2, ChatRoom['MemberList'][i]['DisplayName'])
        # 4省
        ws.write(i + 1, 3, ChatRoom['MemberList'][i]['Province'])
        # 5市
        ws.write(i + 1, 4, ChatRoom['MemberList'][i]['City'])
        # 6个性标签
        ws.write(i + 1, 5, ChatRoom['MemberList'][i]['Signature'])
        # 所属群组
        ws.write(i + 1, 6, name)
        #        ws.write(i+1, 6, ChatRoom['MemberList'][i]['OwnerUin'])#RemarkName是对群内好友的个人备注，可以看到群内好友
        #        ws.write(i, 4, ChatRoom['MemberList'][i]['UserName'])

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
    groups = itchat.get_chatrooms(update=True)[0:]
    total_g=len(groups)
    print ("-----------")
    print ("群列表如下（请将要读取的群保存到通讯录）：")
    for i in range(total_g):
        print(u"群编号"+str(i+1)+": "+groups[i]["NickName"])
    print ("-----------")
    num = int(input("请输入要读取的群编号: "))
    name = groups[num-1]["NickName"]
    ChatRoom = itchat.update_chatroom(getroom_message(), detailedMember=True)
    total = len(ChatRoom['MemberList'])
    wb = xlwt.Workbook()
    begin(wb,name)
    flag = input("是否继续读取（1继续，0停止）: ")
    while int(flag) > 0:
        num = int(input("请输入要读取的群编号(不要重复输入): "))

        name = groups[num - 1]["NickName"]
        ChatRoom = itchat.update_chatroom(getroom_message(), detailedMember=True)
        total = len(ChatRoom['MemberList'])
        begin(wb, name)
        flag = input("是否继续读取（1继续，0停止）: ")
    # 保存excel时间路径与名称
    time = time.strftime('%Y%m%d', time.localtime(time.time()))
    #str2 = 'G:\github\python\excels' + '\\' + time + name + ".xls"
    str2='D:\py_project' + '\\' + time +"JD.xls"
    wb.save(str2)
    print ("-----------")
    print (u"群成员信息读取成功,保存路径：" + str2)
