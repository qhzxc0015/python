# coding: utf-8
import itchat
from itchat.content import *

who_send = None


@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO], True, False, False)
# get img and send to XiaoIce # 将图片等信息转发给小冰
def send_xiaoice(msg):
    global who_send
    who_send = msg['FromUserName']
    msg['Text'](msg['FileName'])
    itchat.send('@%s@%s' % ({'Picture': 'img', 'Video': 'vid'}.get(msg['Type'], 'fil'), msg['FileName']), xiaoice)


@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO], False, False, True)
# get img and send to Sender 将小冰回复的图片等信息转发给发送者
def send_xiaoice(msg):
    global who_send
    msg['Text'](msg['FileName'])
    itchat.send('@%s@%s' % ({'Picture': 'img', 'Video': 'vid'}.get(msg['Type'], 'fil'), msg['FileName']), who_send)


@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
# get text and send to XiaoIce # 将文字等信息转发给小冰
def fw_ice(msg):
    global who_send
    msg_text = msg['Text']
    who_send = msg['FromUserName']
    itchat.send(msg_text, xiaoice)


@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING], isMpChat=True)
# get text and send to Sender # 将小冰回复的文字等信息转发给发送者
def get_ice(msg):
    ice_msg = msg['Text']
    itchat.send(ice_msg, who_send)


# itchat.auto_login(enableCmdQR=2, hotReload=True)
itchat.auto_login(hotReload=True)

xiaoice = itchat.search_mps(name=u'小冰')[0]['UserName']

itchat.run()