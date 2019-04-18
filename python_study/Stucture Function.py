# -*- conding: utf-8 -*-

class MyClass(object):
    msg = 'hello~'

    def show(self):
        print(self.msg)

    def __init__(self,name= "unset",color="black"): # 构造函数在实例化时自动调用__init__
        print("this is init.",name," ,",color)

inst=MyClass()
inst.show()

inst1=MyClass("Lisa")
inst1.show()