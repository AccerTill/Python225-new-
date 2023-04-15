# print(type(7))
# print(type("j"))
# print(id("j"))
# a=['df']
# b=True
# c=None
# print(type(a))
# print(type(b))
# print(type(c))


# a=2
# b=10
# a,b=b,a
# print(b)
# print(a)
#
# g='hello \'hi\''
# print(g)


# a=int(input('input: '))
# b=100
# print(a+b)

#
# a='6.4'
# print(float(a))

# print(1,2,3, sep='$')
#
# print(1,2,3, sep='$', end='---')


# name="World"
#
# print("%s"%(name))
#
#
# print(min(22,44,23,1,0.5))
#
# a=10
# if a/2==5:
#     print("yes")
# else:
#     print('no')


#
# print('Я' > 'А' )
# print( 'Кот' > 'Код' )
# print( 'Сонный' > 'Сон' )

# a=4
# if a>4 or a<4:
#     print('a!=4')
# else:
#     print('a=4')

# a=6
# b=[2,3,4]
# if a not in b:
#     print('not')
# else:
#     print('in')


# a='g'
# if a ==6:
#     print('yes')
# else:
#     print('no')




# dict1 = {11: "eleven", 21: "twenty one", 46: "fourty six", 10: "ten"}

# print("eleven" in dict1)
# print("eleven" not in dict1)
#
# print(21 in dict1)
# print(21 not in dict1)

# print(10 in dict1)
# print(10 not in dict1)


#
# a=0
# while a <10:
#       a += 1
#       if a==5: continue
#
#       print(a)
#
# for x in range(1,10,2):
#       print(x)


# a='Hello'
# for i in a:
#       print(i)

#
# A = [ [1,2,3], [4,5,6] ]
# N=2; M=3
# for i in range(N):
#     for j in range(M):
#        print(A[i][j])
#     print()
#
# print('hello\nworld')

# a='hello word'
# b=a[:3]+"!!!"+a[4:]
# print(b)

# a='hello'
# print(a[2])

# a='abracadabra'
# b=list(a)
# print(b)
# print(a.count('ab'))

#
# a='cat'
# b=a[::-1]
# print(b)


# a='Hello'
# b=a.replace("l", "p", 1)
# print(b)
#
# song = 'cold, cold heart'
# print(song.replace('cold', 'hurt'))
#


#
# a=input(': ')
# if a.isdigit():
#       print('dig')
# else:
#       print('not')


#
# d="abc765675"
# m=d.ljust(50, "-")
# print(m)

#
# a='Khj kjhk$kjh kj$jljl'
# b=a.split("$")
# print(b)
# c=a.replace(" ", '')
# print(c)
#
#
#
# a='abracadabra'
# print(a.find('r'))
# print(a.index('r'))
# print(a.replace('a', 'o'))



#
# a=[1,2,3,4,'k']
# print(a[len(a)-1])
# for i in a:
#     print(i)
#
# a[2]='%%%'
# print(a)
#
# a=[1]* 20
# print(a)

# a= 'Bill'
# b='23'
# d=f'Iam{a}andiam{b}'
# print(d)
# print(d.isalpha())

# a=[1,2,3]
# b=[]
#
# for x in range(3):
#     a[x] = a[x] * 10
# print(a)
# # for i in a:
# #     b.append(i+10)
# # print(b)
#
# print(10 in a)




#
# a=[1,2,3,4]
# print(a.index(3))
#
#
# a=[x**2 for x in range(5)]
# print(a)
#
# cities = ["Москва", "Тверь", "Рязань", "Ярославль", "Владимир"]
# A = [city for city in cities if len(city) < 7]
# # print(A)
#
#
# x = int(input("Введите целое положительное число: "))
# digs = []
# while x:
#     digs.append(x%10)   #берем последнюю цифру числа
#     x = x//10           #отбрасываем последнюю цифру числа
# print(digs)

#
# N=10
# A = list(range(N))
# print(A)

# N = 11
# A = list(range(N))
# print(A)
#
# for i in range(N // 2):
#     A[i], A[N - i - 1] = A[N - i - 1], A[i]
#
# print(A)

#
# a = dict.fromkeys(["+7", "+6", "+5", "+4"])
# print(a)
#
# d = {True: 1, False: "Ложь", "list": [1,2,3], 5: 5}
# for x in d:
#    print(d[x])
# print('')
# for i in d:
#    print(i)



d = {True: 1, False: "Ложь", "list": [1,2,3], 5: 5}
# d2 = d.copy()
# d2["list"] = [5,6,7]
# print(d)
# print(d2)
#
# print(d[True])
# d.setdefault(555, 'lll')
# print(d)
#
# d.pop('kjkjkj', False)
#
#
# print(d.keys())

#
# for x in d.items():
#    print(x)
#
# print('')
# #---------------------------
# for key, value in d.items():
#     print(key, value)

#
# def sayHello():
#     print("hello")
#
# sayHello()
#
#
# print( type(sayHello) )
#
#
# f = sayHello
#
#
# f()


# def myAbs(x):
#     x = -x  if(x<0)  else x
#     return x
#
#
#
# print( myAbs(-5) )



# def f():
#     for x in range(10):
#         yield x
#
# s = f()
# print(s)
# print( next(s))
# print( next(s))
# print( next(s))
# print( next(s))
# print( next(s))
# print( next(s))
# print( next(s))
# print( next(s))
# print( next(s))
# print( next(s))
# print( next(s))
# print( next(s))
# print( next(s))
# print( next(s))


#
# lst = [1,-2,3,-4,-5]
#
#
# def sq(x):
#     return x, x**2
#
# print(list(map(sq, lst)))
#
# def sq(x):
#     return x, x**2


# a=['City', 'Tree', 'Cat', 'Dog']
# b=list(map(lambda x: x.replace('e', "E"),a))
# print(b)


# a = input().split()
# print(a)



# a =list( map(int, input(":").split()))
# print( a )
#
#
# a=[1,2,3,4,5,6,7,8,9,10]
#
# b = list(filter(lambda x: x%2, a))
# print(b)
#
#
#
# print(4%2)

# lst = ("Москва", "Рязань1", "Смоленск", "Тверь2", "Томск")
# b = filter(str.isalpha, lst)
#
# for x in b:
#     print(x, end=" ")


#
# c = "hello worl6d"
# a=[1,2,3,4,5,6,7,8,9,10,'t']
# print(sorted(a))


# def getValues():
#     x = input("x: ")
#     y = input("y: ")
#     try:
#         x = int(x)
#         y = int(y)
#         return x, y
#     except ValueError as v:
#         print(v)
#         return 0, 0
#     finally:
#         print("finally выполняется до return")
#
#
# x, y = getValues()
# print(x, y)


# try:
#     file = open("TEXT.txt",'r', encoding="utf-8" )
#     s=file.readline()
#     print(file.read(2))
#     print(s)
#     print(s)
# except FileNotFoundError:
#     print("Невозможно открыть файл")

#
# try:
#     file = open("TEXT.txt")
#
#     try:
#         s = file.readlines()
#         print(s)
#     finally:
#         file.close()
#
# except FileNotFoundError:
#     print("Невозможно открыть файл")

# import pickle
#
#
# books = [
# ("Евгений Онегин", "Пушкин А.С.", 200),
# ("Муму", "Тургенев И.С.", 250),
# ("Мастер и Маргарита", "Булгаков М.А.", 500),
# ("Мертвые души", "Гоголь Н.В.", 190)
# ]
#
# file = open("TEXT2.bin", "wb")
# pickle.dump(books, file)
# file = open("TEXT2.bin", "rb")
# bs = pickle.load(file)
# print( bs )


# a = [1, 4, 2, -5, 0, 11]
#
# for e, x in enumerate(a):
#     print(e, x)


# import re
#
# text = "Карта map и объект bitmap - это разные вещи"
#
# match = re.findall("map", text)
# print(match)

print(4+7)





