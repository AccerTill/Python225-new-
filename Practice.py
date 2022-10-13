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
text2 = "1 hello 12"

text = "HELLO! Ilona, 65 Alex, Andrew, Paul and " \
       "George are here."
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

def remove_empty_dirs(root_tree):
    for root, dirs, files in os.walk(root_tree):
        # if  os.listdir(root): # пути к непустым папкам
        #     print(root)
        if not os.listdir(root):  # пути к пустым папкам (not)
            os.rmdir(root)
            print(f'Directory {root} is removed')

remove_empty_dirs('TEST')


print(os.path.split(r"D:\Python225\test\nested2\nested3\1.txt"))  # разбивает путь
# на кортеж (head, tail)
print(os.path.dirname(r"D:\Python225\test\nested2\nested3\1.txt"))
print(os.path.basename(r"D:\Python225\test\nested2\nested3\1.txt"))

