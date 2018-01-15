# coding:utf-8
import itchat
from itchat.content import *
# TEXT	文本	文本内容(文字消息)
# MAP	地图	位置文本(位置分享)
# CARD	名片	推荐人字典(推荐人的名片)
# SHARING	分享	分享名称(分享的音乐或者文章等)
# PICTURE 下载方法		图片/表情
# RECORDING	语音	下载方法
# ATTACHMENT	附件	下载方法
# VIDEO	小视频	下载方法
# FRIENDS	好友邀请	添加好友所需参数
# SYSTEM	系统消息	更新内容的用户或群聊的UserName组成的列表
# NOTE	通知	通知文本(消息撤回等)
@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])#这里的TEXT文本消息,MAP地图,CARD名片,SHARING分享,表示如果有人发送这些消息，那么就会调用下面的方法
#给发送人回复相同文字：
def text_reply(msg):
    NN=itchat.search_friends(userName=msg['FromUserName'])['NickName']
    print NN
    #msg.user.send('%s: %s' % (msg.type, msg.text))
    itchat.send_msg('get message：%s'%msg['Text'],toUserName=msg['FromuserName'])
    return "T :%s" % msg["Text"]

# @itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])#图片，语音，附件，小视频
#下载该文件，并发送回发送人：
# def download_files(msg):
#     msg.download(msg.fileName)
#     typeSymbol = {
#         PICTURE: 'img',
#         VIDEO: 'vid', }.get(msg.type, 'fil')
#     return '@%s@%s' % (typeSymbol, msg.fileName)
#

# @itchat.msg_register(FRIENDS)#好友邀请	添加好友所需参数
#加好友自动回复：
# def add_friend(msg):
#     msg.user.verify()
#     msg.user.send('Nice to meet you!')
#

# @itchat.msg_register(TEXT, isGroupChat=True)#群消息
#群聊消息回复：
# isAt 判断是否 @本号
# ActualNickName : 实际 NickName(昵称)
# Content : 实际 Content
# def text_reply(msg):
#     if msg.isAt:#判断是否有人@自己
#如果有人@自己，就发一个消息告诉对方我已经收到了信息
#         msg.user.send(u'@%s\u2005I received: %s' % (
#             msg.actualNickName, msg.text))


itchat.auto_login(hotReload=True)
itchat.run(True)

print ("已登录")
friends = itchat.get_friends(update=True)[0:]
total = len(friends)
for i in range(total):
    print(friends[i]["NickName"]+",id: "+friends[i]["UserName"])
# 给文件助手说话
itchat.send('Hello, filehelper', toUserName='filehelper')