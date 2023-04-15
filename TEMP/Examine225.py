# proghubPython = True
#
# def fun1():
#     global proghubPython
#     proghubPython=None
#
# def fun2():
#     proghubPython = 'py'
#
# fun2()
#
# fun1()
#
# print(proghubPython)
# NONE



# a=[1]+[1]
# print(a)
# [1, 1]

# c=id([1]) == id([1.0])
# print(c)
#True


# e=lambda x: x
# a={1,2,3}
# b=e(a)
# print(a==b)
# True




# dict = {{{ 'Socrat': 'Empty'}:{'Plato': 'A lot of material'}}: 'again'}
# key = {'Socrat': 'Empty'}
# print(dict[key]['Plato'])
# TypeError: unhashable type: 'dict'



# b = [1,2,3] + []
# print(b)
# [1, 2, 3]



# while 1:
#     print(1, break)
# SyntaxError: invalid
# syntax



#!!!!!!!!!!!!!!!!!!!
# d=lambda: False
# print(d)


# destructor of classmethod
# __del__



# b = lambda x, y: print(y)
# b(1,2)
# 2


# d={}
# if d:
#     print("Hello, word!")
# else:
#     print("It is empty")
#
# It is empty

#
# d="some string"
# d[5:12]="int"
# print(d)
#TypeError: 'str'
# object does not support item assignment


# a=[1,2,3,4,5]
# print(a[-1])


# for i in range(-5):
#     print(i)



# import random
# # print(2.1 == random.uniform(2.1, 2.1))
#
# print ( random.uniform(2.1, 2.1))
# True



# try:
#     print(1)
# except Exception:
#     print(0)
#
#     #1


# d=[1]*2
# print(d)
# [1,1]



# b=lambda: print('str')
# type(b())
# str



# a=set('hello')
# print(a)
# print(len(a))
# 4



# for i in range(5):
#     if i % 2 == 0:
#         continue
#     print(i)
#
# 1,3


# b = 'python'
# print(b[:6:2])
# pto



# for i in range(1):
#     print(i)
# 0


# another_dict = {'a':{'a':['a']}}
# print(another_dict.pop('a')==another_dict.clear())
# False


# c=frozenset([1,2,3])=={1,2,3}
# print(c)
# True



# class Test:
#     def print_text(self):
#         print("Parent class Test")
# class Test2(Test):
#     def print_text(self):
#         print("Daugther class Test2")
# test2 =Test2()
# test2.print_text()
#
# Это дочерний класс Test2

#
# a=[1, 2]-1
# print(a)
# TypeError: unsupported operand type(s)



# for i in 'str':
#     print(i.upper(), end ='.')



# b=set('ppp')
# print(b)
# print(str(b)=='p')

#
# for i in 'hello world':
#     if i == 'o':
#         break
#     print(i * 2, end = '')



# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
#
# print(factorial(6))



# n=2.8956
# print(f'{n:.2f}')
# 2.90





# c='str'
# print(c[0:3])
# str


#
# squares=map(lambda x: x*x, [0,1,2,3,4] )
# print(list(squares))
# [0, 1, 4, 9, 16]





# c=lambda x: print(0)
# c(5)
# 0


# a=lambda x: x + x
# print(a(2))




# a = {'a': 10, 'c': 30}
# b = {'c': 20, 'e': 5}
#
# for i in a.keys():
#     print(i)
#     if i not in b:
#         b[i]=a[i]
#
# print(b)
# {'c': 20, 'e': 5, 'a': 10}




# a=(1,2,["h", "j"],6,7)
# print(type(a))
# print(a[2])
# a[2][1]='klklk'
# print(a)
#
# yes


#
# tuple_1 = (1,2,3)
# tuple_2 = (4,5,6)
# tuple_3 = tuple_1 + tuple_2
#
# print(tuple_3)
#
# print(tuple_1 < tuple_2)
# print(tuple_2 < tuple_3)
# print(tuple_1 < tuple_3)
# True
# False
# True



# old_dict = {'a': 10, 'b':10}
# new_dict ={}
# for i, j in old_dict.items():
#     print(i, j)
#     new_dict[j] = i
#
# print(new_dict)
# # {10: 'b'}






# import random
# print(random.random())
# 0.9126124624168264


#
# e=[1] + 1
# print(e)
# error




# e='string'
# print(e[-3:6])
# ing


# x=23
# num=0 if x>10 else 11
# print(num)



# a=1
# for i in range(5):
#     a=a*i
# print(a)


# d={1,2} == set([1,2])
#
# print(d)




#
# c = 'some str'
#
# print(c[-3:9] + " " + c[0:5])
# str some




# d=[1,1,2]
# print(len(set(d)))
# 2



# for i in range(len('str')):
#     if i !=2:
#         print('str'[i], end = '-')
#     else:
#         print('str'[1])
# s-t-t


#
# num=float(2)
# print(num)




# try:
#     b=1/0
# except ZeroDivisionError:
#     b=0
# print(b)



# c = type({1:2, 2:1}) == type ({1,2})
# print(c)
# False


# c=[1, 2] + [0]
# print(c)
# [1, 2, 0]




# try:
#     a=2+'1'
#     print(a)
# except TypeError:
#     print('Error')
# Error



# import random
#
# print(random.uniform(1, 1.1))
# Число от 1 до 1.1


# a=10
# print(b)
# NameError:

# a='str'
# print(len(a))



# #
# f = lambda x+1: x
# c= x + 1 = lambda x
# a= lambda x: x + 1
# b=  def lambda():



#
# def get_sum(a=2, b=3):
#     print(a+b)
# get_sum(4)
# 7


# e = id({1}) == id({1})
# print(e)




# pr =True
#
# def fun1():
#     pr = None
#
#     def fun2():
#         nonlocal pr
#         pr ='py'
#
#     fun2()
#
# fun1()
#
# print(pr)
# True


# for i in 'hello world':
#     print(i*2, end = '')





# proghubPython = True
#
# def fun1():
#     proghubPython=None
#
#     def fun2():
#         global  proghubPython
#         proghubPython = 'py'
#
#     fun2()
# fun1()
# print(proghubPython)




