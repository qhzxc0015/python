# -*- coding: utf-8 -*-
# time.sleep使用
import time

def fbis(num):
    result=[0,1] # list常用的列表类型，用[]定义，
    for i in range(num-2): # range用于生成从0到num-3的数字
        result.append(result[-2]+result[-1]) # 负数表示列表中的倒数元素，result[-1]指倒数第一个元素
    return result

def main():
    result= fbis(10)
    for i,num in enumerate(result): # enumerate生成带有索引的迭代序列
        print (u"第%d个数是： %d" %(i,num)) #u表示字符串使用utf-8格式编码
        time.sleep(1)

if __name__ == '__main__': # 只读内置变量
    main()