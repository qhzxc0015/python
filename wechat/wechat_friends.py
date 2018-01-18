# coding:utf-8
import itchat
#from echarts import Echart, Legend, Pie

# 热登录，不必每次扫码
itchat.auto_login(hotReload=True)

# 获取好友列表及群名称
friends = itchat.get_friends(update=True)[0:]
groups = itchat.get_chatrooms(update=True)[0:]
# 初始化计数器，有男有女，当然，有些人是不填的
male = female = other = 0

# 遍历这个列表，列表里第一位是自己，所以从"自己"之后开始计算
# 1表示男性，2女性
for i in friends[1:]:
    sex = i["Sex"]
    if sex == 1:
        male += 1
    elif sex == 2:
        female += 1
    else:
        other += 1

# 总数算上，好计算比例啊～
total = len(friends[1:])
total_g=len(groups[0:])

#好了，打印结果
def to_print():
    print(u'好友数：%d' % total )
    print(u'群数目：%d' % total_g )
    print(u"男性好友：%.2f%%" % (float(male) / total * 100))
    print(u"女性好友：%.2f%%" % (float(female) / total * 100))
    print(u"未填性别：%.2f%%" % (float(other) / total * 100))
to_print()
    #输出所有好友昵称
for i in range(total):
    print(str(i+1)+": "+friends[i]["NickName"])
#输出所有群昵称
#for i in range(total_g):
#    print(groups[i]["NickName"])
	
# echarts
#print(u"男性好友：%.2f%%" % (float(male) / total * 100))
#print(u"女性好友：%.2f%%" % (float(female) / total * 100))
#print(u"未填性别：%.2f%%" % (float(other) / total * 100))

#chart = Echart(u'%s的微信好友性别比例' % (friends[0]['NickName']), 'from WeChat')
#chart.use(Pie('WeChat',
#              [{'value': male, 'name': u'男性 %.2f%%' % (float(male) / total * 100)},
#               {'value': female, 'name': u'女性 %.2f%%' % (float(female) / total * 100)},
#               {'value': other, 'name': u'其他 %.2f%%' % (float(other) / total * 100)}],
#              radius=["50%", "70%"]))
#chart.use(Legend(["male", "female", "other"]))
#del chart.json["xAxis"]
#del chart.json["yAxis"]
#chart.plot()
