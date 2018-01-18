- [Itchat帮助文档](http://itchat.readthedocs.io/zh/latest/api/)

- 介绍

  --wechat

  - wechat_rooms_details为微信群成员信息获取
    wechat_friends为个人好友信息获取
    wechat_msg为回复信息查看
    Robot_Ice 消息转发至小冰，小冰回复再转发回来
    Robot_TL 图灵机器人
    Robot_room_to_room 自动将群消息统一转发至其他
    wechat_images 拼接好友头像，以255好友为一张图

- 需要插件itchat
  win在cmd下：`pip install itchat`
  linux下：`sudo pip install itchat`

- 登录异常时候删除一下当前文件夹下的*itchat.pkl*

  保持热登录状态，初次登录后会把登录的一些信息保存在同目录下的itchat.pkl文件中，即使这次程序运行结束，下次在同目录下再次调用这个方法的时候可以不用再扫二维码登录了。根据网页版微信的登录机制，这种保持是有时限的，隔一段时间后就要重新登录。

- 注意事项（通过输出到excel解决）：
> 这里的输出都是单行输出，比如:
```
print("ID：")
print(ChatRoom['MemberList'][i]["UserName"])
```
> 因为如果连续输出会乱码，如下输出：
```
print(ChatRoom['MemberList'][i]['DisplayName'], ChatRoom['MemberList'][i]["NickName"], ChatRoom['MemberList'][i]['Signature'])
```
> 会有如下错误：
```
(u'\u673a\u5668\u4eba\u5c0f\u52a9\u624b', u'\u541b\u5b50\u5766\u8361\u83614151', u'')
```

- 各字段含义

```
{
    "Uin": 0,
**  "UserName": 用户名称，一个"@"为好友，两个"@"为群组
**  "NickName": 昵称
    "HeadImgUrl":头像图片链接地址
    "ContactFlag": 1-好友，2-群组，3-公众号
    "MemberCount": 成员数量，只有在群组信息中才有效,
    "MemberList": 成员列表,
**  "RemarkName": 备注名称
    "HideInputBarFlag": 0,
**  "Sex": 性别，0-未设置（公众号、保密），1-男，2-女
    "Signature": 公众号的功能介绍 or 好友的个性签名
    "VerifyFlag": 0,
    "OwnerUin": 0,
    "PYInitial": 用户名拼音缩写
    "PYQuanPin": 用户名拼音全拼
    "RemarkPYInitial":备注拼音缩写
    "RemarkPYQuanPin": 备注拼音全拼
    "StarFriend": 是否为星标朋友  0-否  1-是
    "AppAccountFlag": 0,
    "Statues": 0,
    "AttrStatus": 119911,
    "Province": 省
    "City": 市
    "Alias": 
    "SnsFlag": 17
    "UniFriend": 0,
**  "DisplayName": "",群备注
    "ChatRoomId": 0,
    "KeyWord": 
    "EncryChatRoomId": ""
}
{
    "UserName": "xxx", # ID，这里的是昵称
    "Province": "xxx",  
    "City": "xxx",   
    "Scene": 17,
    "QQNum": 0,
    "Content": "",
    "Alias": "xxx", # 微信号
    "OpCode": 0,
    "Signature": "",
    "Ticket": "",
    "Sex": 0, # 1:男, 2:女
    "NickName": "xxx", # 昵称
    "AttrStatus": 4293221,
    "VerifyFlag": 0
}
```

- 图灵机器人

`pip install wxpy `

`pip install itchat pillow`

`pip install pillow`

`pip install numpy`

- 待用研究

1. 向所有的好友发送不同的祝福消息
```
#coding=utf8
import itchat, time

itchat.auto_login(True)

SINCERE_WISH = u'祝%s新年快乐！'

friendList = itchat.get_friends(update=True)[1:]
for friend in friendList:
    # 如果是发送目的，把下面的方法改为itchat.send即可
    print(SINCERE_WISH % (friend['DisplayName']or friend['NickName']), friend['UserName'])
    time.sleep(.5)
```
2. 向指定群聊的所有人发送消息
```
#coding=utf8
  import itchat,time

itchat.auto_login(True)

REAL_SINCERE_WISH=u'%s新年快乐!!'

chatroomName=u'亲朋友群'
itchat.get_chatrooms(update=True)
chatrooms=itchat.search_chatrooms(name=chatroomName)
if chatrooms is None:
    print(u'没有找到群聊:'+chatroomName)
else:
    chatroom=itchat.update_chatroom(chatrooms[0]['UserName'])
    for friend in chatroom['MemberList']:
        friend=itchat.search_friends(userName=friend['UserName'])
    
        #如果是真正发送，把下面的方法改为　itchat.send(REAL_SINCERE_WISH%(friend['DisplayName']or friend['NickName']),friend['UserName'])
    
        print(REAL_SINCERE_WISH%(friend['NickName'] or friend['DisplayName']))
        time.sleep(.5)
```

3. [基于itchat实现微信群消息同步机器人](https://www.jianshu.com/p/7aeadca0c9bd)