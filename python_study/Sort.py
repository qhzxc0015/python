# -*- coding: utf-8 -*-
myList=[0,-11,10,2,5,8,3,7]
print("before sort:")
print(myList)

lenList=len(myList)
for i in range(0,lenList):
    for j in range(i+1,lenList):
        if myList[i]>myList[j]:
            myList[i],myList[j]=myList[j],myList[i]
print("after sort:")
print(myList)