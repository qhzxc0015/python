# coding: utf-8
from wxpy import *
# 扫码登陆
bot = Bot()
# 初始化图灵机器人 (API key 申请: http://tuling123.com)
tuling1 = Tuling(api_key='207074369b084d969d1fd3f189c2eb4a')#吃吃
tuling2 = Tuling(api_key='b85cee2d9f0646dd9e976304c5230b1c')#丛丛
# 自动回复所有文字消息
@bot.register(msg_types=TEXT)
def auto_reply_all(msg):
    tuling2.do_reply(msg)
# 开始运行
bot.join()

# #coding=utf8
# import requests
# import itchat
# import time
# from itchat.content import *
#
# KEY = '207074369b084d969d1fd3f189c2eb4a'  # 这里填写你的图灵api代码
# def get_response(msg):                        #向图灵机器人发送消息，并获得回复
#     apiUrl = 'http://www.tuling123.com/openapi/api'
#     data = {
#         'key'    : KEY,
#         'info'   : msg,
#         'userid' : 'wechat-robot',
#     }
#     try:
#         r = requests.post(apiUrl, data=data).json()
#         if 'url' in r:
#             return r.get('url')
#         elif 'list' in r:
#             w = "我也想吃，我也想知道"
#             return w
#         else:
#             return r.get('text')
#     except:
#         return
# @itchat.msg_register(itchat.content.TEXT)     #用图灵回复的消息回复文本消息
# def tuling_reply(msg):
#     defaultReply = 'I received: ' + msg['Text']
#     reply = get_response(msg['Text'])
#     time.sleep(5)
#     return reply or defaultReply
# @itchat.msg_register([CARD, MAP, NOTE, SHARING])  # 处理位置、名片、通知、分享
# def text_reply(msg):
#     time.sleep(5)
#     itchat.send('稍等，我看一下', toUserName=msg['FromUserName'])
#
# @itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO]) #处理图片、录音、文件、视频
# def download_files(msg):
#     msg['Text'](msg['FileName'])
#     return '@%s@%s' % ({'Picture': 'img', 'Video': 'vid'}.get(msg['Type'], 'fil'), msg['FileName'])
#
# @itchat.msg_register(FRIENDS)# 收到好友邀请自动添加好友
# def add_friend(msg):
#     time.sleep(5)
#     itchat.add_friend(**msg['Text']) # 该操作会自动将新好友的消息录入，不需要重载通讯录
#     itchat.send_msg('Hai!', msg['RecommendInfo']['UserName'])
#
# @itchat.msg_register(TEXT, isGroupChat=True) #群机器人回复
# def group_reply(msg):
#     defaultReply = 'I received: ' + msg['Text']
#     reply = get_response(msg['Text'])
#     return reply or defaultReply
#
#
# #itchat.auto_login(enableCmdQR=2)  # 如部分的linux系统，块字符的宽度为一个字符（正常应为两字符），故赋值为2
# #itchat.auto_login(enableCmdQR=True)  #通过以下命令可以在登陆的时候使用命令行显示二维码
# itchat.auto_login(True) #为了让实验过程更加方便（修改程序不用多次扫码），我们使用热启动
# itchat.run()  #登录运行