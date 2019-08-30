# -*- coding:utf-8 -*-
#number=["金蛋","鸭蛋","鹅蛋","铁蛋"]
number=["金蛋","鸭蛋","鹅蛋","铁蛋"]
list1=(1,2,11,4,2,6,7,8)
# number.insert(1,'鸟蛋')
# number.extend(["臭蛋","鸡蛋"])
# for i in number:
#     print(i)
# list2=list1[::-1]
# print(list2)

# print(list1[1:2:1])
str="上海/自来水/来自/海上"

print(str.index("上"))
print(str.split("/"))
print(','.join(number))
print("{0}:{1:.2f}".format("圆周率是",3.14123))
print("%s:%d"%("只取整数",12.34))
print(list(list1))
print(sum(list1))
g=lambda x:2*x+1
print(g(2))
