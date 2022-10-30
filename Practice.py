# d = {(3,4,5): (1,2,3), "b": "two", 5: [34,56,67], 4: "one"}
# d[4]="!"
# print(d[5][2])
# print(d[(3,4,5)])
#
# key = "five"
#
# if key in d:
#     del d[key]
# print(d)

#
# d = {"a": "one", "b": "two", "c": "three", "aa": "one"}
# key = "!"
# for key in d:
#     print(key, "->", d[key])

#
# try:
#     del d[key]
# except:
#     print("No elements")


# d = {"a": "one", "b": "two", "c": "three", "aa": "one"}
# value = d.get("aa")
# print(value)
# # get - interrupts mistakes
# print(d.items())
# print(d.keys())
# print(d.values())
# d.update([("P",3333),["oi",9898]])
# print(d)

# new_d = dict()
# new_d["a"]=d.pop('a')
# print(new_d)

#
# a = ["one", 1, 2, 3, "two", 10, 20, 'three', 15, 36, 60, "four", -20]
# d=dict()
# s=''
# for i in a:
#     if type (i) == str:
#    # print(i)
#         d[i]=[]
#     #     s=i
#     # else:
#     #     d[s].append(i)
# print(d)


# a=[1,2,3]
# y=[234,456,658]
# b=["one","two","three"]
# c={k:v for k,v in zip(a,b)}
# print(c)
# l=zip(a)
# print(list(l))
# h=zip(a,y)
# print(dict(h))

# one = {"name": "Igor", "last_name": "Smith", "job": "Consultant"}
# two = {"name": "Olga", "last_name": "Doe", "job": "Manager"}
# # print(list(zip(one,two)))
#
# for (k1,v1), (k2, v2) in zip(one.items(), two.items()):
#     print(k1, v1)
#     print(k2, v2)

# pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
# # for i in pairs:
# #     print(*i)
#
# print(*pairs)
#
# a,b=zip(*pairs)
# print(a)
# print(b)

# a=[1,2,3,4,5]
# c,*d=a
# print(c)
# print(d)


# one = {'apple': 20, 'orange': 35, 'pepper': 60}
# two = {'pepper': 40, 'onion': 55}
# print([two, one])
# print({**two, **one})


# a=[2,23,456,23,1,7, "grey"]
# b={i: i for i in a}
# print(b)

# import builtins
#
# # print(dir(builtins))
# names =dir(builtins)
# for t in names:
#     print(t)


# def func1(a):
#     def func2():
#         return a + 1
#     return func2()
#
# print((func1(10)))

# s=func1(10)
# print(s(2))


# def increment(x):
#     print(x , "1 x")
#     def inner(y):
#         print(x , "x")
#         print(y , "y")
#         return x+y
#     return inner
#
# a=increment(12)
# print(a(18), "final")
#
# print(increment(100)(256))

# def one(a):
#     def two(b):
#         return a+b
#     return two
#
# g=one(10)
# print(g(2))
#
# def one1(f):
#     return lambda x: f*x
#
#
# g1=one1(10)
# print(g1(2))


# print((lambda a: a*b)(2)(8))
# print((lambda x: lambda y: lambda c: x/y+c)(3)(2)(100))

# one = {'apple': 20, 'orange': 5, 'pepper': 60, "carrot": 12}
# # print(sorted(one.values()))
# list_d= list(one.items())
# list_d.sort(key = lambda i: i[0])
# print(list_d)
# # print(dict(list_d))

# a = {"name": "Paul", "lastname": 'Brown', "rating": 10},
# b = {"name": "Bob", "lastname": 'Smith', "rating": 12},
# c = {"name": "Les", "lastname": 'Paul', "rating": 9},
#
# players1 = [*a, *b, *c]
# #
# players=[
# {"name": "Paul", "lastname": 'Brown', "rating": 10},
# {"name": "Bob", "lastname": 'Smith', "rating": 12},
# {"name": "Les", "lastname": 'Paul', "rating": 9},
#   ]

# print(players)
# print(players1)
# # d=list(a.items(),b.items(),c.items())
# # l=list(a.items()),list(b.items()),list(c.items())
# # print(l)
# # print(l[1][2][1])
# # l.sort(key = lambda i:i[2][1])
# # print(l)
#
# # res = sorted(players, key = lambda item: item['rating'])
# res1=sorted(players1, key = lambda item: item['rating'])
# # print(res)
# print(*res1)


# a = [(lambda x, y: x + y), lambda x,y: x-y, lambda x,y: x*y, lambda x,y: x/y]
# print(a[1](2,3))

#
# a={"one": lambda x: x-1, 'two': lambda x: abs(x) - 1, "three": lambda x: x }
# b=[-3,10,0,1]
# for i in b:
#     print(a["one"](i))


# d = {
#     1: lambda: print('Понедельник'),
#     2: lambda: print('Вторник'),
#     3: lambda: print('Среда'),
#     4: lambda: print('Четверг'),
#     5: lambda: print('Пятница'),
#     6: lambda: print('Суббота'),
#     7: lambda: print('Воскресенье')
# }
# d[1]()

# print((lambda a,b: a if a>b else b) (15,4))
# b=[12,23,34]
# a=map(lambda x: x*2, b)
# print(list(a))


# b=[12,23,34]
# c=['a','b','c']
# a=map(lambda x ,y : {x:y}, b,c)
# print(list(a))
# import random
#
# a=[random.randint(1,20) for i in range (10)]
# print(a)
# b=filter(lambda x: x<10, a)
# print(list(b))

# def dec(func):
#     def wrapper():
#         print("1")
#         func()
#         print("2")
#     return wrapper
#
# @ dec
# def func():
#     print("Hello!")
#
# func()


# a = 10
# b = 5
# print("summa:", a, 'and', b, "=", end = " ")
# print(a+b)

#
# d=[234,345,234,46,67,]
# a=2
# b=3
# c=4
# for i in d:
#     print(i, end=" ")

#
# def func1(ar1,ar2):
#     def func2(fn):
#         def wrapper(*args):
#             print("args:", *args)
#             print(ar1, "+", ar2, end=" ")
#             fn(*args)
#         return wrapper
#     return func2
#
# @func1("!", "---")
# def func(a,b):
#     print(a+b)
#
# func(12,23)


# print(int("34"))
# print(int("125"))
# print(float("23.5"))
# print(int(45))

# a=True
# b=False
# if b:
#     print("!")
# else:
#     print("...")


# print('Как Ваша фамилия?')
#
# name = input()
# print(name)
# f="dfg"
#
# print('Здравствуйте, '+ name + '!' )
# print("Hello " + f + "!")


# s = 0
#
# for k in range(-5,11):
#
#       s = s + 2 * k
#
# print(s)

# print("100", 10)
# print(int("100", 10))
# print(int("100", 2))
# print(int("100", 8))
# print(int("100", 16))
# print()
# print(int("1010", 2))
# print(int("12", 8))
# print(int("A", 16))

# print(bin(18))#2
# print(oct(18))#8
# print(hex(18))#16
# print("---")
# print(0b10010)
# print(0o22)


#
#
# import math
# print(f'Number -{round(math.pi,3)}')
# print(f"Number - {math.pi: .3f}")


# a="we_doc"
# b="gh.txt"
# print(fr"home\{a}\{b}")


# def func(x):
#     """
#     Function for x.
#     :param x: main parameter
#     """
#     return x*2
#
# print(func(5))
# # print(func.__name__)
# print(func.__doc__)


#
# a=[x for x in [ord(x) for x in input("-")]]
# print(a)

import random

# # print(ord("a"))
# # print(chr(1))
#
# b=list(chr(random.randint(40, 80)) for i in range(5))
# c=list(chr(random.randint(100, 126)) for u in range(5))
# random.shuffle(b+c)
# print(b+c)

# a=dir(str)
# for i in a:
#     print(i)
#
# b="Hello Python!"
# print(b.isdigit())

#
# a,b=list(map(str,input("-").split()))
# print("".join(list(b))+ " " + "".join(list(a)))

#
# string = "Hello Python"
# a=string[:string.find(" ")]
# b=string[string.find(" "):]
# print(b, a)
#
# a=input("-")
# print(list((i for i in a if i.isdigit())))

# print(a.find("!"))
# print(a.index("n"))
#
# a=list(map(int, input(" - ".split())))

# print("dkjbnstjgnrtkg".isalnum())
# print("dkjbnst@#jgnrtkg".isalnum())
# print("dkjbnstjgn4rtkg".isalpha())
# print("".isalnum())
# print("ASDI".isupper())
# print("ASDi".isupper())
# print("hello".center(11, "!"))
# print("python".lstrip("p").rstrip("n"))


# print("www.ftkjgnt.gjtgi.kjgtrig".split(".",2))

# a="Hello Python you are very good"
# # # b=a.split()
# # # print(b)
# # # f="*".join(b)
# # # print(f)
# d=a.replace(" ", '*')
# print(d)

# a="Every day even yesterday I make " \
#   "exercises for examine of Python."
#
# h=print(len(list(filter(lambda x: x[0]=="E" or x[0]=="e", a.split()))), "words")
#
# d=a.count("E")
# n=a.count(" e")
# print(d+n)


# REGULAR METHODS


import re

# s="Я ищу совпадения в 2021 года. И я из найду в 2 счёта"
# reg = 'Я ищу'
#
# print(s.find(reg))
# print(re.findall(reg, s))# returns list
# print(re.search(reg, s))# returns first seaching object
# print(re.search(reg,s).span())
# print(re.search(reg,s).start())
# print(re.search(reg,s).end())
# print(re.search(reg,s).group())
# print(re.match(reg, s))
# reg1 = 'совпадения'
# print(s.find(reg1))
# print(re.findall(reg1, s))# returns list
# print(re.search(reg1, s))# returns first seaching object


# s="05-03-1987 # Дата рождения"
#
# print("Дата рождения:", re.sub("#.*","",s))
# print("Дата рождения:", re.sub("-","!",re.sub("#.*","",s) ))

# s = "12 hello python3, 1991."
# reg = r"\d{2,4}"
# print(re.findall(reg, s))


# s="+7499456-45-78 +74994564578,  7(499) 456 45 78, 74994564578"
# reg =r"\+?\d{11}"
# print(re.findall(reg,s))


# s="I am looking roe my hidden glasses"
# reg = r"I"
# print(re.findall("i",s, re.IGNORECASE))


# text="""
# one
# two
# """
# print(re.findall((r'one\w+', text)))


# a="Python 3 is very 34 fast. 1990."
#
# print(re.findall(r"\d+",a))
# print(re.findall(r"\d{4}",a))
# print(re.findall(r"\b\w{4}\b",a))
# print(re.findall(r"\b\w{6}\b",a))
# print(re.findall(r"\b\w+\b",a))


# b="Impressions78_hot@mail.ru"
# c="Hot (@ dog)"
#
# print(re.findall(r"\w+[@\.]\w+", b))
# print(re.findall(r"[a-zA-Z]",c))
# print(re.findall(r"\w{3}", c))
#


# b="Impressions78_hot@mail.ru 12345@mail.ru " \
#   " login.3-67@i.ru for x in y"
# print(re.findall(r"[a-zA-Z\w\.\-]+@[a-zA-Z]+\.[a-z]+",b))

# a="Hello python! I am here. Where are you?"
# print(re.findall(r"\w+\s\w+\!", a))
#
# b="Hello_python! I Am here."
# print(re.findall(r"\w+\!", b))
#
# c="Hello-python! I Am here."
# print(re.findall(r"[\w-]+", c))


#
# Символы
# \d: цифровой символ от 0 до 9
# \D: любой нецифровой символ;
# \s: пробельный символ;
# \S: любой непробельный символ;
# \w: любой символ;
# \W: любой не цифро-буквенный символ;
# \b: определяет границы слова;
# . : обозначает любой символ; (пример)
# \. : соответствует точке.
#
# Модификаторы
#
# {}:  группировка числовых значений. Например, \d{3} дает совпадения, включающие 3 цифры,
# а \d{3,5} — совпадения, содержащие от 3 до 5 цифр. По сути, это {min, max}.
#
# []:  группировка символов. Соответствует одному из символов в скобках. Например,
# [a-z] выдаст совпадения с каждым символом алфавита в нижнем регистре.
#
# +:  соответствует предыдущему элементу один или более раз. Например, [a-z]+a сгруппирует результат совпадений,
# как показано в примере.
#
# ?:  соответствует предыдущему элементу 0 или один раз. Здесь можно посмотреть принцип действия [a-z]?a.
#
# *:  соответствует предыдущему элементу 0 или множество раз. Обратимся к примеру [a-z]*a.
#
# $:  означает конец строки.
#
# ^:  указывает на начало строки.
#
# |:  оператор или. Например, col(o|u)r соответствует и американскому,
#     и британскому вариантам написания слова color.


# d="<body> Example for python lesson</body>"
# print(re.findall(r"<[a-z/]+>", d))
# print(re.findall(r"<[/a-z]{1,10}>", d))
# print(re.findall(r"<.*>", d)) #max symbols are covered.
# print(re.findall(r"<.*?>", d)) #lazy - minimal symbols are covered.

#
# d="<body> Image <img src = 'bg.jpg'> - page backside </body>"
# reg = r"<img[^>]*"
# print(re.findall(reg, d))
#
# f="<body> Image <img alt='picture' 'bg.jpg'> - page backside </body>"
# reg = r"<img[^>]*"
# print(re.findall(reg, f))

#
# f="Hello Python@"
# print(re.findall(r"[a-zA-Z\s]+[^>]", f))
# print(re.findall("H[^@]*", f))


# l="Hello, Python!"
# print(re.findall(r"\w*", l))

# text = "Методы этой группы[16  - fg] выполняют[17] " \
#        "преобразование регистра[18][19] строки"
# print(re.findall(r"\[[1-9a-z\s-]+\]", text))
#
# # print(re.findall(r'\[.*?]', text))
# text2 = "1 hello 12"
#
# text = "HELLO! Ilona, 65 Alex, Andrew, Paul and " \
#        "George are here."
# print(re.findall(r"^HELLO!", text))
# print(re.findall(r"here.$", text))
# print(re.findall(r"^1[a-zA-Z\s]+12$", text2))
# print(re.findall(r"\bA[a-z]+", text))
# print(re.findall(r"[A-Za-z]+[w]\b", text))
# print(re.findall(r"Ilona|Bob", text))
# print(re.findall(r"[4567]", text))
#
# text = "Hello! Ilona, @ 65 Alex, Andrew," \
#        " Paul are here."
# print(re.findall(r"[0-9]", text))
# print(re.findall(r"[a-zA-Z]+", text))
# print(re.findall(r"[^0-9\s]+", text))
# print(re.findall(r"[^0-9a-zA-Z\s\,.!]+", text))
# print(re.findall(r"\b[^IAHP\s\,.]+", text))
# print(re.findall(r"[ ]", text))
# print(re.findall(r"[^ ]+", text))

# text = "Hello! Ilona, @tr №65 Alex, Andrew," \
#        " Paul are here."
# print(re.findall(r".", text))
# print(re.findall(r"[^.]", text))
# print(re.findall(r"[A]+\d+", text))
# print(re.findall(r"\d[A]+", text))
# print(re.findall(r"№\d+", text))
# print(re.findall(r"@[a-z]+\d", text))
#
# text = "Hello! g8876  g9  77 Ilona, @tr №65 Alex, Andrew," \
#        " Paul are here."
# print(re.findall(r"g[0-9]{1,10}", text))
# print(re.findall(r"g[0-9]*", text))
# print(re.findall(r"g[0-9]?", text))
# print(re.findall(r"[0-9]+", text))
# print(re.findall(r"[a-zA-Z]+[^\s]+[^0-9]+", text))
# text = "Hello! g8876  Ilona, @tr №65 Alex, Andrew," \
#        " Paul are +77 here."
# print(re.findall(r"\+\d+", text))
# print(re.findall(r"\+\d+", text))

# text = "Https://python.ru is address of Python 3"
# text = "Https://python.ru is address of Python 3"
# print(re.findall(r"(Https)(://)([a-zA_Z]+)\.(ru)", text))

# def func(n):
#     if n == 0:
#         print("End...")
#         return
#     print(n)
#     func(n-1)
#     print(n)
# func(5)


# a="0123456789"
# b= a[356 % 10]
# print(b)
#
# k=356 % 10
# l=357 % 10
# j=8 % 3
# kk=10 // 3
# print(j)
# print(kk)
# print(l)
# print(j)

# f="1234567890"
# ff=f[20 % 7]
# print(ff)
# print(f[int(ff)])


# names = ['Adam', ['Bob', ['Chet', 'Cat'], 'Barb', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann']
# res =[]
# def func(names):
#     for i in names:
#         if type(i)==list:
#             func(i)
#         else:
#             res.append(i)
#     return res
#
# d=func(names)
# print(d)


# O              OPENING FILES


# f = open("text.txt", "r")
# print(f)
# print(*f)
# f.close()
#
# f=open(r"C:\PycharmProjects\Python225\text.txt", "r")
# print(*f)
# print(f.closed)
# print(f.mode, " - mode")
# print(f.name)
# print(f.encoding)

# f=open(r"C:\PycharmProjects\Python225\text.txt", "r")
# print(f.read(3))
# print(f.read())
# f.close()
#
# f=open(r"C:\PycharmProjects\Python225\text.txt", "r")
# try:
#        print(f.read())
# except FileNotFoundError:
#        print("Error!")
# finally:
#        f.close()

#
# f=open(r"C:\PycharmProjects\Python225\text.txt", "r")
# try:
#        # for i in range (4):
#        print(f.readline(3))
#        print(f.readline(3))
# finally:
#        f.close()


# f=open(r"C:\PycharmProjects\Python225\text.txt", "r")
# try:
#        print(f.readlines(26)) # opening in list
# finally:
#        f.close()


# count = 0
# f=open(r"C:\PycharmProjects\Python225\text.txt", "r")
# for line in f:
#        if line:
#               count += 1
#               print(line)
# print(count, " =  count")
# f.close()


# count = 0
# f=open(r"C:\PycharmProjects\Python225\text.txt", "r")
# # print(len(f.readlines()))
# cnt = 0
# for line in f:
#        cnt += 1
# print(cnt)
#
# f=open(r"C:\PycharmProjects\Python225\text.txt", "r")
# count = 0
# s = f.readlines()
# while s!="":
#        s=f.readline()
#        count +=1
# print(count)
# f.close()
#
# f=open(r"C:\PycharmProjects\Python225\text_new.txt", "a")
# # f.write("Hello! \nWorld")
# # f.write("\nNew text again!")
# # for i in range(6):
# #        f.write("\nNew text again!")
# # print(f.write("\nNew text - dftkjgtgtgtgtgdtgegegege5ge5gt"))
# lines = [" \nThis is line 1", "This is line 2" ]
# f.writelines(lines)
# f.close()

# f = open(r"C:\PycharmProjects\Python225\text_new.txt", "w")
# lst = [str(i) + str(i - 1) for i in range(1, 20)]
# # print(lst)
# for index in lst:
#        f.write(index + " \t")
# f.close()


# f = open(r"C:\PycharmProjects\Python225\text_new_1.txt", "w")
# f.write("Change string in tex editor;\nChanges of string in list;\nWrite list in file;")
# f.close()
#
# f=open(r"C:\PycharmProjects\Python225\text_new_1.txt", "r")
# read_file = f.readlines()
# print(read_file)
# for i in range(len(read_file)):
#        if read_file[i]=="Changes of string in list;\n":
#            read_file[i] ="Hello, world!\n"
# print(read_file)
# f.close()
#
# f=open(r"C:\PycharmProjects\Python225\text_new_1.txt", "w")
# f.writelines(read_file)
# f.close()


#
# count = 0
# def func(a):
#     for i in range(len(a)):
#             global count
#             if a[i]>0:
#                 func(a[i+1:])
#                 break
#             else:
#                 count+=1
#     return count
# d = func([12, 4, -2, 456, -8, 56, -38, -9, -67, -1])
# print(d, " - digits are less than 0")

#
# f=open(r"C:\PycharmProjects\Python225\text.txt", "r")
# print(f.read(3))
# print(f.tell())
# print(f.seek(1))
# print(f.read())
# print(f.tell())
# f.close()


# f=open(r"C:\PycharmProjects\Python225\text.txt", "r+")
# print(f.write("I am learning Python."))
# print(f.seek(3))
# print(f.write("-new string-"))
# print(f.tell())
# print(f.seek(15))
# print(f.write("-PYTHON-"))
# print(f.tell())
# print(f.seek(0))
# print(f.write("!!!"))
# print(f.tell())
# f.close()

# with open(r"C:\PycharmProjects\Python225\text.txt", "w+") as f:
#        print(f.write('0123456789'))
# with open(r"C:\PycharmProjects\Python225\text.txt", "r") as f:
#        for line in f:
#               print(line[:6])


# file_name = "C:\PycharmProjects\Python225\text.txt"
# lst =[4.5, 2.9, 3.9, 1.0, 0.3, 4.33, 7.777]
# def get_line(lt):
#        lt = list(map(str, lt))
#        return ' '.join(lt)
# print(get_line(lst))
# with open(r"file_name", "w") as f:
#        f.write(get_line(lst))
# # print("Done!")  #  only tupe - str may be writted into docs
# max=0
# with open(r"file_name", "r") as f:
#        g=list(map(float, f.read().split()))
#        print(g)
#        for i in g:
#               if len(str(i))>max:
#                      max = len(str(i))
# print(max)
# print("Done!")  #  only tupe - str may be writted into docs


# t=[i for i in range(11)]
#
# tt=list(map(str,t))
# ttt=" ".join(tt)
# print(ttt)
# with open(r"C:\PycharmProjects\Python225\text.txt", "w+") as f:
#        print(f.write(ttt))
# with open(r"C:\PycharmProjects\Python225\text.txt", "r") as f:
#        for line in f:
#               print(line)
#
# text = "String #1\nString #2\nString #3\nString #4\nString" \
#        " #5\nString #6\nString #7\nString #8\nString #9\nString #10"
# with open(r"C:\PycharmProjects\Python225\New.txt", "w") as f:
#        f.write(text)
#
# # read_file = "New.txt"
# # write_file = "two.txt"
#
# with open(r"C:\PycharmProjects\Python225\New.txt", "r") as fr, open(r"C:\PycharmProjects\Python225\Two.txt", 'w') as fw:
#      for line in fr:
#             line = line.replace("String", "line-")
#             fw.write(line)

# ------------------------------OS----------------------------------

import os
import time


# print("Current directory: ", os.getcwd())
# print(os.listdir())   # list of folders in current directory

# # for i in os.listdir():
# #        print(i)

# print(os.listdir(".."))   # up one lever from current directory

# os.mkdir("folder") # creating of folder in current directory (only one time)

# os.makedirs("nested1/nested2/nested3") # creating internal folders

# os.makedirs("nested1/nested2/nested4") # creating internal added folder in end of path

# os.remove("text_new_1.txt") # removing files from current directory

# os.remove("text_new.txt") # removing files from current directory

# os.remove("Nef File.py") # removing files from current directory

# os.rename("nested1", "TEST") # renaming folder (files)

# os.rename("text.txt", "TEST/test1.txt") # renaming and replacing

# os.renames("Two.txt", "TEST1/text_test.txt") # renames and replacing

# os.rmdir("folder") # removing EMPTY folder

# os.rmdir("TEST")  #  removing FULL folder

# for root, dirs, files in os.walk("TEST", topdown=False): # if False search is inverted
#     print("Root", root)
#     print("\tSubdirs:", dirs)
#     print(("\t\tFiles:", files))
#     print()

# def remove_empty_dirs(root_tree):
#     for root, dirs, files in os.walk(root_tree):
#         # if  os.listdir(root): # пути к непустым папкам
#         #     print(root)
#         if not os.listdir(root):  # пути к пустым папкам (not)
#             os.rmdir(root)
#             print(f'Directory {root} is removed')
#
# remove_empty_dirs('TEST')
#
#
# print(os.path.split(r"D:\Python225\test\nested2\nested3\1.txt"))  # разбивает путь
# # на кортеж (head, tail)
# print(os.path.dirname(r"D:\Python225\test\nested2\nested3\1.txt"))
# print(os.path.basename(r"D:\Python225\test\nested2\nested3\1.txt"))
#
#
# print(os.path.join("C:\PycharmProjects", "Python225", "text.txt"))

# dirs = ["Work/F1", "Work/F2/F21"]  # creating directories
# for dir in dirs:
#        os.makedirs(dir)

# files = {
#      "Work": ['w.txt'],
#      "Work\\F1": ['f11.txt', 'f12.txt', 'f13.txt'],
#      "Work\\F2\\f21": ['f211.txt', 'f212.txt']
# }
# for d, f in files.items():
#        for file in f:
#               file_path = os.path.join(d, file)
#               print(file_path)
#               open(file_path, "w").close()

# file_with_text = [r"Work\w.txt", r"Work\F1\f12.txt",
#                   r"Work\F2\f21\f211.txt", r"Work\F2\f21\f212.txt"]
#
# for file in file_with_text:
#     with open(file, "w") as f:
#         f.write(f"Any text in file {file}.")
#
# def print_tree(root, topdown):
#     print(f"Walk around {root} {'to_bottom' if topdown else 'to_up'}")
#     for root, dirs, files in os.walk(root, topdown = topdown):
#         print(root)
#         print(dirs)
#         print(files)
#     print("-"*50)
#
# print_tree("-Work-", topdown=False)
# print_tree("-Work-", topdown=True)

# -----------------------------------------------
# def print_tree(root, topdown):
#     print(f"Обход {root} {'сверху вниз' if topdown else 'снизу вверх'}")
#     for root, dirs, files in os.walk(root, topdown=topdown):
#         print(root)
#         print(dirs)
#         print(files)
#     print("-" * 50)
#
# #
# print_tree('Work', topdown=False)
# print_tree('Work', topdown=True)


# -----------------------------------------------

# print(os.path.split(r"D:\Python225\test\nested2\nested3\1.txt"))

# print(os.path.exists(r"C:\PycharmProjects\Python225\Work\w.txt")) # checking existing of path and file
#
# path=r"C:\PycharmProjects\Python225\New.txt"
# print(os.path.getatime(path)) # time of last opening of time
# print(os.path.getmtime(path)) # time of last changing of time
# print(os.path.getctime(path)) # time of last changing of time

# path = r"C:\Program Files\PyCharm Community Edition 2022.2.2\plugins\python-ce" \
#        r"\helpers\typeshed\stdlib"

# size = os.path.getsize(path)
# print(size)
# ksize = size // 1024
# print("Size", ksize, "Kbytes")
# c_time = os.path.getctime(path)
# print(c_time)
# print(time.strftime("%d.%m.%y, %H:%M:%S", time.localtime(c_time)))


# print(os.path.isfile(r"C:\Program Files\PyCharm Community Edition 2022.2.2"
#                      r"\plugins\python-ce\helpers\typeshed\stdlib\ssl.pyi"))
# print(os.path.isfile(r"C:\Program Files\PyCharm Community Edition 2022.2.2"
#                      r"\plugins\python-ce\helpers\typeshed\stdlib"))
# print(os.path.isdir(r"C:\Program Files\PyCharm Community Edition 2022.2.2"
#                      r"\plugins\python-ce\helpers\typeshed\stdlib"))


# -----------------------------------------
# -------------------------------------ООП (объектно ориентированное программирование)
# -----------------------------------------


# class Point:
#        """Class for coordinates of points on plate."""
#        x=1
#        y=1
#
# p1=Point()
# print(type(p1))
# Point.x=100
# p1.x=200
# print(p1.x, p1.y)
# print(Point.x)
# print(id(p1.x))
# print(id(Point.x))
# print(id(p1))
# print(id(Point))
# print(Point.__doc__)
# print(Point.__name__)
# print(dir(Point))
# p2 = Point()
# print(p2.x, p1.y)

# class Point:
#     """Class for coordinates of points on plate."""
#     x = 1
#     y = 1
#     def set_coords(self):
#         print(self.__dict__)
# p1 = Point()
# p1.x=200
# p1.y=5
# p1.set_coords()
# Point.set_coords(p1)
# p2 =Point()
# p2.set_coords()


# print(p1.x, p1.y)
# print(type(p1))
# Point.x = 100
# print(Point.x, "Point.x ")
# print(Point.x, Point.y)
# print(id(p1), "-id")
# print(id(Point), '-id')
# print(p1.__dict__, ' p1.__dict__')
# print(Point.__doc__)
# print(Point.__name__)
# print(dir(Point))
# p2 = Point()
# print(p2.x, p2.y)
# print(p2.__dict__)
# print()
# print(Point.__dict__)




# class Point:
#     x = 1
#     y = 1
#     def set_coords(self, x, y):
#         self.x = x
#         self.y = y
#
# p1=Point()
# p1.set_coords(5, 10)
# print(p1.__dict__)
#
# p2=Point()
# p2.set_coords(3, 8)
# print(p2.__dict__)
#
# Point.set_coords(p2, 2, 7)
# print(p2.__dict__)
#
# -----------------------------------------------------
#
# class Human:
#     name = "name"
#     birthday = "00.00.0000"
#     phone = "00-00-00"
#     country = "country"
#     city = "city"
#     address = "street, house"
#     def print_info(self):
#         print(" Personal info. ".center(40, "*"))
#         print(f"name: {self.name}\nbirthday: {self.birthday}\n"
#               f"phone:{self.phone}\ncountry: {self.country}\n"
#               f"city: {self.city}\naddress: {self.address}")
#         print("=" * 40)
#     def input_info(self, first_name, birthday, phone, country,
#                    city, address):
#         self.name = first_name
#         self.birthday = birthday
#         self.phone = phone
#         self.country = country
#         self.city = city
#         self.address = address
#     def set_name(self, name):  # Install name
#         self.name = name
#     def get_name(self):  # get name
#         a = "Name: " + self.name
#         return a
#     def set_birthday(self, birthday):
#         self.birthday = birthday
#     def get_birthday(self):
#         return self.birthday
#
# h1 = Human()
# h1.input_info("Cat", "23.05.1986", "45-46-98", "Spain", 'Madrid', "Libre via")
# h1.print_info()
# h1.set_name("Valery")
# print(h1.get_name())
# h1.set_birthday(("12.04.2021"))
# print(h1.get_birthday())


#
# class Point:
#     x = 1
#     y = 1
#
# p1 = Point()
# p1.x = 5
# p1.y = 10
# print(p1.__dict__)
# print(p1.x)
# print(getattr(p1,"x"))
# # print(hasattr(p1, "z"))
# # print(hasattr(p1, "y"))
# p1.z=7
# p1.name= "Viola"
# # setattr(p1,"u", 5)
# # setattr(Point,"w", 53)
# print(p1.__dict__)
# # print(p1.w)
# # print(p1.u)
# delattr(p1, "z")
# print(p1.__dict__)


#
# class Person:
#     skill = 10
#     def __init__(self,name,surname):
#         self.name = name
#         self.surname = surname
#     def print_info(self):
#         print("Info of staff: ", self.name, self.surname)
#     def add_skill(self, k):
#         self.skill += k
#         print("Qualification: ", self.skill, "\n")
#
# p1 = Person("Alex", "Vissner")
# p1.print_info()
# p1.add_skill(3)
#
# p2 = Person("Susan", "Nisson")
# p2.print_info()
# p1.add_skill(2)


#
# class Point:
#    def __init__(self, x=0, y=0):
#         self.x=x
#         self.y=y
#         print("This is initializator!")
#    def __del__(self):
#        print("Deleting of example: " + self.__class__.__name__)
#
# p1=Point(5, 10)
# print(p1.__dict__, " DICT")
# del p1
# print(p1.x)


# class Point:
#     count = 0  # статические свойства
#     def __init__(self, x=0, y=0):  # динамические свойства
#         self.x = x
#         self.y = y
#         # self.count +=1
#         Point.count +=1
#         # print(Point.count)
#
# p1 = Point(5, 10)
# p2 = Point(15, 20)
# p3 = Point(152, 210)
# # print(Point.count)
# # print(p1.count, "p1.count")
# print(p1.count, "p2.count")
# print(Point.count)

#
# class Robot:
#     k = 0
#     def __init__(self, name):
#         self.name = name
#         print("--Initialization of robot:", self.name)
#         Robot.k +=1
#     def __del__(self):
#         print(self.name, "   Off robots.")
#         Robot.k -=1
#         if Robot.k == 0:
#             print(self.name, "---Last robot.---")
#         else:
#             print("   Working robots Qty is:", Robot.k)
#         # print("   Now quantity of working robots is: ", Robot.k)
#     def say_hi(self):
#         print("--Hello! My name is:", self.name)
#
# droid1=Robot("#1")
# droid1.say_hi()
# print("---------Quantity of robots: ", Robot.k)
# droid2=Robot("#2")
# droid2.say_hi()
# print("---------Quantity of robots: ", Robot.k)
# droid3=Robot("#3")
# droid3.say_hi()
# print("Quantity of robots: ", Robot.k)
# print("----------------------------------------")
# print("\n ***   Now robots are working   *** \n")
# print("Work of robots is finished, let's off robots")
# del droid1
# del droid2
# print("Quantity of robots: ", Robot.k)
#
# class Point:
#     __slots__ = ["x", "y", "z"] # коллекция slots не имеет dict
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
# p1 = Point(5, 10)
# p1.z = 2
# print(p1.z)
# # p1.x = 100
# # p1.y = "abc"
# # print(p1.__x, p1.__y)
# print(p1.__dict__)

#
# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#     def __set_x(self, x):
#         print("Call __set_x")
#         self.__x = x
#     def __get_x(self):
#         print("Call __get_x")
#         return self.__x
#     def __del_x(self):
#         print("Deleting property")
#         del self.__x
#     coord_x = property(__get_x, __set_x,__del_x)
#
# p1 = Point(5, 10)
# p1.coord_x = 100
# print(p1.coord_x)
# del p1.coord_x  # deleting x.
# p1.coord_x=7
# print(p1.__dict__)

#
# class Car:
#     name = "C200"
#     make = "mersedes"
#     model = 2008
#     def start(self):
#         print("Start!")
#     def stop(self):
#         print("Stop...")
# car_a = Car()
# car_b = Car()
# print(type(car_b))
# car_b.start()
# print(car_b.model)
# print(dir(car_b))

# class Car:
#     car_count =0
#     def start(self,name,make,model):
#         print("Start engine..")
#         self.name = name
#         self.make = make
#         self.make = model
#         Car.car_count +=1
#
# car_a = Car()
# car_a.start("Corrola", "Toyota", 2015)
# print(car_a.name)
# print(car_a.car_count)
#
# car_b = Car()
# car_b.start("City", "Honda", 2013)
# print(car_b.name)
# print(car_b.car_count)



# class Car:
#     @staticmethod
#     def get_class_details():
#         print("This is class Car")
# Car.get_class_details()
# g=Car()
# g.get_class_details()

# class Square:
#     @staticmethod
#     def get_squares(a,b):
#         return a*a, b*b
# print(Square.get_squares(3,5))
# g=Square()
# print(g.get_squares(34, 8))


# class Car:
#     def start(self):
#          print("Engine has been start")
#
# car_a=Car()
# print(car_a)


# class Car:
#     def __str__(self, name):
#         name = "name"
#         print(name)
#         return "Car class object"
#     def start(self):
#         print("Starting..")
#
# car_a=Car()
# print(car_a)
# car_a.start()


# class Car:
#     car_count = 0
#     def __init__(self):
#         Car.car_count +=1
#         print(Car.car_count)
# car1=Car()
# car2=Car()

# class Car:
#     def start(self):
#         message = "Engine start..."
#         print(message)
#         return message
# car1=Car()
# print(car1.message)
# print(car1.start())

# class Car:
#     message1="Engine start"
#     def start(self):
#         message2 = "Car is start"
#         return  message2
# car1=Car()
# print(car1.message1)


# class Vehicle:
#     def vehicle_method(self):
#         print("This is parent method.")
# class Car(Vehicle):
#     def car_method(self):
#         print("This is second method. ")
# car1=Car()
# car1.vehicle_method()


# class Vehicle:
#     def vehicle_method(self):
#         print("111")
# class Car(Vehicle):
#     def car_method(self):
#         print("222")
# class Cycle(Vehicle):
#     def cycle_method(self):
#         print("333")
#
# a1=Car()
# a1.vehicle_method()
# a1=Cycle()
# a1.cycle_method()





# class A:
#     def a_method(self):
#         print("AAA")
# class B:
#     def b_method(self):
#         print("BBB")
# class C(A,B):
#     def c_method(self):
#         print("CCC")
#
# s1=C()
# s1.a_method()
# s1.b_method()






# class Car:
#     count = 0
#     def start(self, a,b=None):
#         if b==None:
#             print(a)
#             Car.count +=1
#             print(Car.count, " Count")
#         else:
#             print(a+b)
#             Car.count+=1
#             print(Car.count, " Count")
# a1=Car()
# a1.start(23,5)
# a1.start(27)

#




# class Vehicle:
#     def print_details(self):
#         print("Это родительский метод из класса Vehicle")
# class Car(Vehicle):
#     def print_details(self):
#         print("Это дочерний метод из класса Car")
# class Cycle(Vehicle):
#     def print_details(self):
#         print("Это дочерний метод из класса Cycle")
#
# car_a = Vehicle()
# car_a.print_details()
#
# car_b = Car()
# car_b.print_details()
#
# car_c = Cycle()
# car_c.print_details()
#
# a1=Cycle()
# a1.print_details()
#
# class Car:
#     def __init__(self,model):
#         self.model =model
#     @property
#     def model(self):
#         return self.__model
#     @model.setter
#     def model(self, model):
#         if model < 2000:
#             self.__model = 2000
#         elif model > 2018:
#             self.__model = 2000
#         else:
#             self.__model = 2000
#     def getCarModel(self):
#         return "Year" + str(self.model)
#
# a1=Car(2088)
# print(a1.model)
# print(a1.model())





# class Change:
#     @staticmethod
#     def inc(x):
#         return x+1
#     @staticmethod
#     def dec(x):
#         return x-1
#
# print(Change.inc(5), Change.dec(8))




#
# class Mat:
#     @staticmethod
#     def min(a):
#         return min(a)
#     @staticmethod
#     def middle(a):
#         return sum(a)/len(a)
#
# a=[23,5,3,7]
# # a1=Mat()
# # print(Mat.min(a))
# # print(Mat.middle(a))
# a1=Mat()
# print(a1.min(a))
# print(a1.middle(a))






# class Person:
#     def __init__(self, name , age ):
#         self.__name = name
#         self.__age = age
#     @property
#     def coord_name(self):  # __get_x
#         # print("Вызов __get_name")
#         return self.__name
#     @coord_name.setter
#     def coord_name(self, n):  # __set_x
#         # print("Вызов __set_name")
#         self.__name = n
#     @coord_name.deleter
#     def coord_name(self):  # __del_x
#         # print("Удаление свойства")
#         del self.__name

    # coord_x = property(__get_x, __set_x, __del_x)

#
# p1 = Person("Ilona", 24)
# print(p1.__dict__, "---DICT")
# p1.coord_name = "Kelly"
# print(p1.coord_name)
# print(p1.__dict__,"---DICT")
# del p1.coord_name
# print(p1.__dict__,"---DICT")
# p1.coord_name = "Hansa"

#
#
# #-------------------------------
#
#
# class Person:
#     def __init__(self, name, old):
#         self.__name = name
#         self.__old = old
#     @property
#     def name(self):
#         return self.__name
#     @name.setter
#     def name(self, n):
#         self.__name = n
#     @name.deleter
#     def name(self):
#         del self.__name
#
# #     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, new_old):
#         self.__old = new_old
#
#     @old.deleter
#     def old(self):
#         del self.__old
#
#
# p1 = Person('Kelly', 15)
# print(p1.name)
# print(p1.__dict__, "---DICT")
# p1.name = 'Igor'
# del p1.name
# p1.old = 31
# print(p1.old)
# del p1.old
# print(p1.__dict__)


# print(1 / 0.45359237)


#-------------------------------------------------------------
#
# class Date:
#     def __init__(self, day=0, month=0, year=0):
#         self.day = day
#         self.month = month
#         self.year = year
#     def string_to_db(self):
#         return f'{self.year}-{self.month}-{self.day}'
#     @classmethod
#     def from_string(cls, data_as_string):
#         d, m, y = map(int, data_as_string.split('.'))
#         return cls(d, m, y)
#     @staticmethod
#     def is_date_valid(data_as_string):
#         if data_as_string.count('.') == 2:
#             d, m, y = map(int, data_as_string.split('.'))
#             return d <= 31 and m <= 12 and y <= 3999
# # a=Date(23, 12, 45)
# # print(a)
# # print(a.string_to_db())
# dates = [
#     '30.12.2020',
#     '30.12.2020',
#     '31.01.2021',
#     '12.31.2020'
# ]
# for string_date in dates:
#     if Date.is_date_valid(string_date):
#         date = Date.from_string(string_date)  # '30.12.2020'
#         string_to_db = date.string_to_db()
#         print(string_to_db)
#     else:
#         print("Некорректная дата")
#



# ---------------------------------




# class Point:
#     x=1
#     y=2
# p1=Point()
# Point.x=100
# print(Point.__dict__)
# print(p1.x,p1.y)
# p1.x=200
# p1.y=300
# print(p1.x,p1.y)


# -----------------------------------------------
# -----------------------------------------------
#                     OOP
# -----------------------------------------------
# -----------------------------------------------

# class Point:
#     x=1
#     y=1
#     def set_coords(self, x,y):
#         self.x=x
#         self.y=y
#         return x,y
# a=Point()
# a.x=100
# a.y=200
# print(a.__dict__)
# print(a.set_coords(45,67))
# print(Point.set_coords(a, 8989,344))
# print(a.__dict__)

#
#
# class a:
#     name = "name"
#     surname = 'surname'
#     def info(self):
#         print("INFO: ", self.name, self.surname)
#
#     def input(self, name, surname):
#         self.name=name
#         self.surname = surname
#     def setname(self, name):
#         self.name = name
#     def getname(self):
#         return self.name
#
#     def setbr(self, br):
#         self.br = br
#     def getbr(self):
#         return self.br
#
#
# s=a()
# ss=a()
# # s.name = "Violetta"
# # s.surname="Brown"
# # s.input("Gregory", "Smith")
# # s.info()
# ss.input("Robert", "Patrick")
# ss.setname("Liam")
# # print(ss.getname(), "---getting name---")
# ss.setbr("23.12.89")
# # ss.info()
# # print(ss.getbr())
# # print(ss.__dict__)
# print(getattr(ss, "name"))
# print(getattr(ss, "surname"))
# print(getattr(ss, "br"))
# print(hasattr(ss, "Number"))
# print(hasattr(ss, "name"))
# setattr(ss, "age", 34)
# print(ss.__dict__)
# delattr(ss, "br")
# print(ss.__dict__)
# # print(getattr(ss, "surname"))
# # print(getattr(ss, "br"))
#

#
# class Person:
#     skill = 10
#     def __new__(cls, *args, **kwargs):
#         print("Constructor.")
#         return super().__new__(cls) # for both calls
#     def __init__(self):
#          print("Initializator.")
#
# #     def __init__(self, name, surname):
# #             self.name =name
# #             self.surname = surname
# #             print("Initializator.")
# Person()
# # p1=Person("Alex", "Vissner")
# # print(p1.__dict__)
# # for i in p1.__dict__:
# #    print (i, '->',p1.__dict__[i])
# # print(p1.name, p1.surname)


#
# class Point:
#     def __init__(self, x=0, y=0):
#         self.x=x
#         self.y=y
#     def __del__(self):
#         print("Deleting " + self.__class__.__name__)
#
# p1 = Point(34,6)
# print(p1.__dict__)
# # print(p1.__class__)
# del p1
# # print(p1.x)
# # print(p1.__dict__)

# class Point:
#     # count=0
#     def __init__(self, x):
#         self.x=x
#         # Point.count+=1
#     def __del__(self):
#         print(self.x, " deleting")
#
# a=Point("hjhj")
# a.x=1000
# print(a.__dict__)
# print(a.x)
# b=Point("jhhlfwef")
# d=Point("wurytewuy")
# b=Point(23)
# print(Point.count)
# print(b.count)
# del d
# print(b.x)
# del b
# del d

# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x=x
#         self.__y=y
#
# p1=Point(23,45)
# # print(p1.__x, p1.__y)
# # print(Point.__dict__)
# # print(p1.__dict__)
# p1.__x=9000
# p1.__y="hjk"
# print(p1.__dict__)
# p1.__x=9000435
# p1.__y="hjk34234"
# print(p1.__x, p1.__y)
# print(p1.__dict__)

#
# class Point:
#     # __slots__=["x", "y", "z"] # or (,,,)
#     def __init__(self, x=0, y=0):
#         self.__x=x
#         self.__y=y
#     def __get_x(self):
#         print("Get.")
#         return self.__x
#     def __set_x(self, x):
#         print("Set.")
#         self.__x = x
#     def __del_x(self):
#         del self.__x
#
#     # coords_x=property(__get_x, __set_x, __del_x)
#
# p1 =Point(34, 67)
# p1.coords_x = 1000
# print(p1.__dict__)
# print(p1.coords_x)
# del p1.coords_x
# print(p1.__dict__)
#
# # p1.z=900
# # print(p1.__dict__)




#
#
# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x=x
#         self.__y=y
#
#     @property
#     def coord_x(self):
#         print("Get.")
#         return self.__x
#     @coord_x.setter
#     def coord_x(self, x):
#         print("Set.")
#         self.__x = x
#     @coord_x.deleter
#     def coord_x(self):
#         del self.__x
#     # coords_x=property(__get_x, __set_x, __del_x)
#
# p1 =Point(5, 10)
# p1.coord_x = 100
# print(p1.coord_x)
# print(p1.__dict__)
# del p1.coord_x
# print(p1.__dict__)
# p1.coord_x=7
# print(p1.__dict__)
#
# # p1.z=900
# # print(p1.__dict__)


# ------------------------


#
# class Person:
#     def __init__(self, name="name", age=0):
#         self.__name=name
#         self._age=age
#
#     @property
#     def d_name(self):
#         print("Get.")
#         return self.__name
#     @d_name.setter
#     def d_name(self, name):
#         print("Set.")
#         self.__name = name
#     @d_name.deleter
#     def d_name(self):
#         print("Del")
#         del self.__name
#     # coords_x=property(__get_x, __set_x, __del_x)
#
# p1 =Person("Viola", 10)
# print(p1.__dict__)
# p1.d_name = "Lesly"
# print(p1.d_name)
# print(p1.__dict__)
# del p1.d_name
# print(p1.__dict__)
# p1.d_name="Antony"
# print(p1.__dict__)



# class Point:
#     __count =0
#     def __init__(self, x=0, y=0):
#         self.__x =x
#         self.__y =y
#         Point.__count+=1
#     @staticmethod
#     def get_count():
#         return Point.__count
#
# p1=Point()
# p2=Point()
# print(p1.get_count())
# p2=Point()
# print(p1.get_count())


# class Point:
#     @staticmethod
#     def inc(x):
#         return x+1
#
# p1=Point()
# print(p1.inc(2))


#----------------------------------------------


# class Date:
#     def __init__(self, mass):
#         self.mass = mass
#     def string_to_db(self):
#         if type(self.mass) == int or type(self.mass) == float:
#             res = round(self.mass * 2.204, 3)
#         else:
#             res = "Incorrect input.."
#         return str(res) + " pounds."
#
# a=Date(89)
# print(a.string_to_db())
# b=Date("hj")
# print(b.string_to_db())



# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def a(self):
#         print(self.x + 1000, " -Self")
#     def b(self):
#         print('---------')
#         self.a()
#         print(f"{self.y * 0.333}")
# s=Point(12,100)
# s.b()









# def func(x):
#     if type(x)==str:
#         return True
#     else:
#         return False
#
# s=func("e")
# if s==False:
#     print("1")
# else:
#     print("2")



#---------------------------------------------------------
#
# class Person:
#     # def __init__(self, name , age ):
#     #     self.__name = name
#     #     self.__age = age
#     @property
#     def coord_name(self):  # __get_x
#         print("Вызов __get_name")
#         return self.__name
#     @coord_name.setter
#     def coord_name(self, n):  # __set_x
#         print("Вызов __set_name")
#         self.__name = n
#     @coord_name.deleter
#     def coord_name(self):  # __del_x
#         print("Удаление свойства")
#         del self.__name
#
#     # coord_x = property(__get_x, __set_x, __del_x)
#
#
# p1 = Person()
# p1.coord_name="Kelly"
# print(p1.__dict__)
# print(p1.coord_name)
# del p1.coord_name
# print(p1.__dict__)
# # p1 = Person("Ilona", 24)
# # print(p1.__dict__, "---DICT")
# # p1.coord_name = "Kelly"
# # print(p1.coord_name)
# # print(p1.__dict__,"---DICT")
# # del p1.coord_name
# # print(p1.__dict__,"---DICT")
# # p1.coord_name = "Hansa"

#-------------------------------------------------------------
#
# class Rect:
#     def __init__(self, h, w):
#         self.h=h
#         self.w=w
#
#     def show_rect(self):
#         print(f"Rectrangle: {self.h} - {self.w}")
#
# class RectFon(Rect):
#     def __init__(self, w,h, bg):
#         super().__init__(h,w)
#         self.fon=bg
#
#     def show_rect(self):
#         super().show_rect()
#         print(f"Rectrangle: {self.fon} ")
#
# class RectBorder(Rect):
#     def __init__(self, w,h, bord):
#         super().__init__(h,w)
#         self.bord=bord
#
#     def show_rect(self):
#         super().show_rect()
#         print(f"Rectrangle: {self.bord} ")
#
#
# shape1=RectFon(45, 65, "red")
# shape1.show_rect()
#
# shape2=RectFon(600, 300, "1px solid red")
# shape2.show_rect()

#---------------------------------------------------------------------------------------

#
# class Vector(list):
#     def __str__(self):
#         return " ".join(map(str, self))
#
#
# v = Vector ([1,2,3])
# print(v)
#




# class Vector(a):
#     def __str__(self):
#         return str(a)
#
#
# v = Vector(78)
# print(v)


#--------------------------------------------------------------

from abc import ABC, abstractmethod
#
# class Check(ABC):
#     def draw(self):
#         print("Нарисовал фигуру.")
#
#     @abstractmethod
#     def move(self):
#         # pass
#         print("Method move() in base class")
#
# class Queen(Check):
#     def move(self):
#         super().move()
#         print("Method move() in ch class...Movement of figure e2e4")
#
# # q=Check()
# q=Queen()
# q.draw()
# q.move()


#-----------------------------------------
# class Currency(ABC): #---------------------------------
#     def __init__(self, value):
#         self.value = value
#
#     @abstractmethod
#     def convert_to_rub(self):
#         pass
#
#     def print_value(self):
#         print(self.value, end=" ")
#
# class Dollar(Currency):   #------------------------------
#     rate_to_rub = 74.16
#     suffix = "USD"
#
#     def convert_to_rub(self):
#         rub = self.value * Dollar.rate_to_rub
#         return rub
#
#     def print_value(self):
#         super().print_value()
#         print(Dollar.suffix, end = " ")
#
#
# class Euro(Currency):     #------------------------------
#     rate_to_rub = 90.14
#     suffix = "EUR"
#
#     def convert_to_rub(self):
#         rub = self.value * Euro.rate_to_rub
#         return rub
#
#     def print_value(self):
#         super().print_value()
#         print(Euro.suffix, end = " ")
#
#
#
# d=[Dollar(5), Dollar(10), Dollar(50), Dollar(100)]
# k=[Euro(5), Euro(10), Euro(50), Euro(100)]
# print("*" * 20)
# for elem in d:
#     elem.print_value()
#     print(f"= {elem.convert_to_rub():.2f} RUB")
# for elem in k:
#     elem.print_value()
#     print(f"= {elem.convert_to_rub():.2f} RUB")



# a=Dollar(10)
# print(a.convert_to_rub())
# print(Dollar.suffix)
# print(Dollar.rate_to_rub)


#------------------------------------------

# class A:
#     data = 9003
#
#     def __init__(self, name):
#         self.name = name
#     def info(self):
#         print(self.name)
#
#     class B:
#         def __init__(self, name, obj):
#             self.inner_name = name
#             self.obj = obj
#
#         def inner_info(self):
#             print("!", self.inner_name)
#
# a=A("Kelly")
# print(a.name)
# a.info()
# inner_a = a.B("Lilu", 89)
# inner_a.inner_info()
# h=A.B("Stephan", 876)
# print(h.inner_name)


#---------------------------
#
# class A:
#     def __init__(self):
#         self.name = "Yellow"
#         self.kkk = self.B()
#     def check(self):
#         print("check")
#
#     class B:
#         def __init__(self):
#             self.name = "Pale red"
#
# a=A()
# print(a.name)
# a.check()
# f=A.B()
# print(f.name)
# g=a.kkk
# print(g.name)


#---------------------------------------------------------------------

class A:
    # def __init__(self):
    #     print("Инициализатор класса А")
        pass
class AA:
    # def __init__(self):
    #     print("Инициализатор класса АA")
    def hi(self):
        print("AA")
class B(A):
    def __init__(self):
        # super().__init__()
        print("Инициализатор класса B")
    # def hi(self):
    #     print("B")
class C(AA):
    def __init__(self):
        super().__init__()
    #     print("Инициализатор класса C")
    # def hi(self):
    #     print("C")
class D(B, C):
    def __init__(self):
        B.__init__(self)
        C.__init__(self)
        print("Инициализатор класса D")
    # def hi(self):
    #     print("D")
   # pass

d = D()
print(D.mro())
print(D.__mro__)
d.hi()









