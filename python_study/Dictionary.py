# -*- conding: utf-8 -*-

def check_book(**dictParam ):
    # if dictParam.has_key('price'):  注，Python3以后删除了has_key()方法改为以下放发：
    if 'price' in dictParam:
        price = int(dictParam['price'])
        if price > 100:
            print("***I want buy the book!!**")
    print("this book information are as follow:")
    for key in dictParam.keys():
        print(key,":",dictParam[key])
    print()

if __name__ == '__main__':
    check_book(author='James',title='Economics')
    check_book(author="Linda",title="Deepin in Python",date="2015-5-1",price="302")
    check_book(author='Jinker',title='How to keep healthy',price='10')