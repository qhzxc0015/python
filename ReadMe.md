- 基于itchat对微信进行信息采集及其自动化控制

  wechat_rooms为微信群成员信息获取

  wechat_friends为个人好友信息获取

- 需要插件itchat
  win在cmd下：`pip install itchat`
  linux下：`sudo pip install itchat`

- 登录异常时候删除一下当前文件夹下的*itchat.pkl*

  保持热登录状态，初次登录后会把登录的一些信息保存在同目录下的itchat.pkl文件中，即使这次程序运行结束，下次在同目录下再次调用这个方法的时候可以不用再扫二维码登录了。根据网页版微信的登录机制，这种保持是有时限的，隔一段时间后就要重新登录。​

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

