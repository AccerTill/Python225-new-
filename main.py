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


# -------------------------------------------------------------
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


# ----------------------------------------------


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


# ---------------------------------------------------------
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

# -------------------------------------------------------------
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

# ---------------------------------------------------------------------------------------

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


# --------------------------------------------------------------

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


# -----------------------------------------
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


# ------------------------------------------

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


# ---------------------------
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


# ---------------------------------------------------------------------
#
# class A:
#     # def __init__(self):
#     #     print("Инициализатор класса А")
#         pass
# class AA:
#     # def __init__(self):
#     #     print("Инициализатор класса АA")
#     def hi(self):
#         print("AA")
# class B(A):
#     def __init__(self):
#         # super().__init__()
#         print("Инициализатор класса B")
#     # def hi(self):
#     #     print("B")
# class C(AA):
#     def __init__(self):
#         super().__init__()
#     #     print("Инициализатор класса C")
#     # def hi(self):
#     #     print("C")
# class D(B, C):
#     def __init__(self):
#         B.__init__(self)
#         C.__init__(self)
#         print("Инициализатор класса D")
#     # def hi(self):
#     #     print("D")
#    # pass
#
# d = D()
# print(D.mro())
# print(D.__mro__)
# d.hi()
#


# -----------------------------
# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#     def __str__(self):
#         return f'({self.x}, {self.y})'
#
# class Styles:
#     def __init__(self, color='red', width=1, *args):
#         print("Инициализатор Styles")
#         self._color = color
#         self._width = width
#         super().__init__(*args)
#
# class Pos:
#     def __init__(self, sp: Point, ep: Point, *args):
#         print("Инициализатор Pos")
#         self._sp = sp
#         self._ep = ep
#         # Styles.__init__(self, *args)
#         super().__init__(*args)
#
# class Line( Pos, Styles):
#     def draw(self):
#         print(f"Рисование линии: {self._sp}, {self._ep},"
#               f" {self._color}, {self._width}")
#
#
# l1=Line(Point(10,10), Point(100,100), 'green', 5)
# l1.draw()
# print(Line.__mro__)
#

# ----------------------------------------------
# Миксины (примеси)
#
# class Displayer:
#     @staticmethod
#     def display(message):
#         print(message)
#
# class LoggerMixin:
#     def log(self, message, filename='logfile.txt'):
#         with open(filename, 'a') as fh:
#             fh.write(message)
#
#     def display(self, message):
#         Displayer.display(message)
#         self.log(message)
#
# class MySubclass(LoggerMixin, Displayer):
#     def log(self, message, filename=''):
#         super().log(message, filename='subclasslog.txt')
#
# subclass = MySubclass()
# subclass.display("Эта строка будет отображаться и записываться в файл")

# ----------------------------------------------------------

#
# class Goods:
#     def __init__(self, name, weight, price):
#         super().__init__()
#         print("Инициализатор Goods")
#         self.name = name
#         self.weight = weight
#         self.price = price
#     def print_info(self):
#         print(f"{self.name}, {self.weight}, {self.price}")
#
# class MixinLog:
#     ID = 0
#     def __init__(self):
#         print("Инициализатор MixinLog")
#         self.ID += 1
#         self.id = self.ID
#     def save_log(self):
#         print(f"{self.id}: товар было продан в 00:00 часов")
#
# class Notebook(Goods, MixinLog):
#     pass
#
#
# n = Notebook("HP", 1.5, 35000)
# n.print_info()
# # print(n.id)
# n.save_log()
# print(Notebook.__mro__)


# -------------------------------------------------------------

# Перегрузка операторов

# 24*60*60 = 86400 (число секунд в одном дне)
#
# class Clock:
#     __DAY = 86400
#
#     def __init__(self, sec: int):
#         if not isinstance(sec, int):
#             raise ValueError("Секунды должны быть целым числом")
#         self.sec = sec % self.__DAY
#
#     def __add__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом данных Clock")
#         return Clock(self.sec + other.sec)
#
#     def __sub__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом данных Clock")
#         return Clock(self.sec - other.sec)
#
#     def __mul__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Must be type of Clock.")
#         return Clock(self.sec * other.sec)
#
#     # def __imul__(self, other):
#     #     if not isinstance(other, Clock):
#     #         raise ArithmeticError("Must be type of Clock.")
#     #     return Clock(self.sec * other.sec)
#
#     def __floordiv__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError()
#         return Clock(self.sec // other.sec)
#     #
#     def __mod__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError()
#         return Clock(self.sec % other.sec)
#
#     def __eq__(self, other):
#         return self.sec == other.sec
#
#     def __ne__(self, other):
#         return not self.__eq__(other)
#
#     def __gt__(self, other):
#         return self.sec > other.sec
#
#     def get_format_time(self):
#         s = self.sec % 60  # секунды
#         m = (self.sec // 60) % 60  # минуты
#         h = (self.sec // 3600) % 24  # часы
#         return f'{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}'
#
#     @staticmethod
#     def __get_form(x):
#         return str(x) if x > 9 else "0" + str(x)
#
#     # def __getitem__(self, item):
#     #     if not isinstance(item, str):
#     #         raise ValueError("Ключ должен быть строкой")
#     #
#     #     if item == "hour":
#     #         return (self.sec // 3600) % 24
#     #     elif item == "min":
#     #         return (self.sec // 60) % 60
#     #     elif item == "sec":
#     #         return self.sec % 60
#     #
#     #     return "Неверный ключ"
#
# c1 = Clock(100)
# # print(c1.sec)
# print(c1.get_format_time())
# c2 = Clock(50)
# print(c2.get_format_time())
# #----------------------------
# # if c1 == c2:
# #     print("Time is the same!")
# # if c1 != c2:
# #     print("Time is NOT the same!")
#
# if c2 < c1:
#     print("Первое время меньше")
# # if c1 != c2:
# #     print("Time is NOT the same!")
#
#


# a=[1,2,3,4,5]
# b=list(a)
# c=list(b)
# print(c)
# print(type(b))
# print(type(a))

# ------------------------------------------------------------------------------
#
# class Point:
#     MAX_COORD = 108
#     MIN_COORD = 0
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def set_coord(self, x, y):
#         if self.MIN_COORDS <= x <= self.MAX_COORDS:
#             self.x = x
#             self.y = y
#
#     # def set_bound(self, left):
#     #     self.MIN_COORD = left
#
#     # @classmethod
#     # def set_bound(cls, left):
#     #     cls.MIN_COORD = left
#
#     def __getattribute__(self, item): #-------------------
#         if item == "x":
#             raise ValueError ("Access is Forbidden")
#         else:
#             print("__getattribute__ is WORKING")
#             return object.__getattribute__(self,item)
#
#     def __setattr__(self, key, value): #------------------
#         if key == "z":
#             raise AttributeError ("Forbidden name.")
#         else:
#             # print("__settattr__")
#             object.__setattr__(self, key, value)
#             # self.x = value # recursion
#             # self.__dict__[key] = value
#
#     def __getattr__(self, item):
#         # print("__getattr__: " + item)
#         return False
#
#     def __delattr__(self, item):
#         print("__delattr__: " + item)
#         object.__delattr__(self, item)
#
# pt1 = Point(1, 3)
# pt2 = Point(4, 9)
# print(Point.MAX_COORD)
# pt1.y=89
# print(pt1.__dict__)
# # print(pt1.yy)
# print(pt1.MAX_COORD)
# del pt1.x
# print(pt1.__dict__)
# # a=pt1.y
# # print(a)
# # print(pt1.x)
# # pt1.set_bound(-100)
# # print(pt1.__dict__)
# # print(Point.__dict__)


#
#
# class Book:
#     def __init__(self, name= " ", autor = " ", pages = 0, year = 0):
#         self.name = name
#         self.autor =autor
#         self.pages = pages
#         self.year = year
#
#     def __setattr__(self, key, value):
#         if key in "name autor" and type(value) != str:
#             raise TypeError("Fault type name autor...")
#         elif key in "pages year" and type(value) != int:
#             raise TypeError("Fault type PAGES YEAR...")
#         else:
#             object.__setattr__(self, key, value)
#
# book = Book("Balakirev", "OOP", 78, 2018)
# print(book.__dict__)
# # book.name = "Pushkin"
# # book.year = 1765
# # print(book.__dict__)


# ----------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------
# import random
#
# class RandomPassword:
#     pass_collection = []
#     def __init__(self, min_length, max_length):
#         self.psw_chars='1234567890)(*&^%$#@!_><?":{}[]'
#         self.min = min_length
#         self.max = max_length
#
#     def __call__(self):
#         self.password = "".join([random.choice(self.psw_chars)for _ in range(random.randint(self.min, self.max))])
#         self.pass_collection.append(self.password)
#         return self.pass_collection
#
# r1=RandomPassword(5,10)
# p=r1()
# print(p)

# ------------------------------------------------------------------------------------
# class FileAcceptor:
#     temp =[]
#     g=0
#     def __init__(self,check):
#         self.names = ["boat.jpg", "moon.bmp", "horse.pg"]
#         self.check = check
#
#     def __call__(self):
#         # for i in self.names:
#         #     if i.split('.')[1] in self.check:
#         #         self.temp.append(i)
#         # return self.temp
#          return filter(lambda x : x.split('.')[1] in self.check, self.names)
#
#
# acc= FileAcceptor("jpg png")
# a=acc()
# print(*a)


# -----------------------------------REPR   STR----
# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return f"{self.__class__}: {self.name}"
#
#     def __str__(self):
#         return f"{self.name}"
#
# # c1=Cat("Murzik")
# # print(c1)
# # print(str(c1))
#
# c2=Cat('Liam')
# print(c2)
# print(str(c2))


# -------------------------------LEN - ABS--------------

# class Point:
#     def __init__(self, *args):
#         self.__coords = args
#     def __len__(self):
#         return len(self.__coords)
#     def __abs__(self):
#         return list(map(abs, self.__coords))
#
# p = Point(1, -2)
# print(len(p))
# print(abs(p))

# ------------------------------------------------------
#
# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
#
#     def __str__(self):
#         return f"{self.title}, {self.author}, {self.pages}"
#
## book = Book("Island", "Smith", 34)
# print(book)
#
# a,b,c = list(map(str, input(":").split()))
# book = Book(a,b,c)
# print(book)
# ------------------------------------------------------
#
# class WordString:
#     def __init__(self, string):
#         self.string = string
#
#     @property
#     def inst(self):
#         return self.string
#     @inst.setter
#     def inst(self, string):
#         self.string = string
#
#     def __len__(self):
#         self.res=self.string.split()
#         print(self.res)
#         print(self.res[1])
#         return len(self.res)
#
#
# wordstring = WordString("Hello, Python!")
# wordstring.string = "Boom, burum!"
# print(wordstring.__dict__)
# print(len(wordstring))
#
#
# a='Hello, Python!'
# b=a.split()
# print(b)


# ---__-------------------------------------PANDAS----------------


# import pandas as pd
#
# df = pd.DataFrame({'name':['Taras', "Ivan", "Stas"], 'surname':
#     ["Shevchenco", "Kozak", "Gerb"], 'heigth': [184,170,176]})
#
# print(df)
# print("*"*20)
#
# # df_tall = df[df['heigth']>175]
# # print(df_tall)
# # print("*"*20)
#
# # df_tall = df[df['name']=="Taras"]
# # print(df_tall)
# # print("*"*20)
#
# # df_tall_named = df[((df['heigth']>175) | (df["name"] == 'Taras'))
# #                    & (df['surname'] == "Shevchenko")]
# # print("*"*20)
# # print(df_tall_named)
#
# max_heigth = 175
# chosen_name ="Taras"
# df_tall_name_sec = df.query('heigth > @max_heigth & name == @chosen_name')
# print(df_tall_name_sec)
# print("*"*20)
#
# #-OR
#
# df_tall_named_trd = df.query('heigth < 175 & `name` != "Taras Shevchenko"')
# print(df_tall_named_trd)


# -------------------------ADD  -------------------------------------


# n=7
# a="j"
# b=a.rjust(3,"*")
# print(b)
# c=str(n).ljust(4,"^")
# print(c)


# --------------------------------------------------------
# class A:
#     def __init__(self, x):
#         self.x = x
#
#     def sum(self):
#         return(f'{self.change(self.x)}')
#
#     @classmethod
#     def change(cls, x):
#         return str(x) * 3
#
#     def __add__(self, other):
#         return A(self.x + other)
#
#     def __add__(self, other):
#         if not isinstance(other, (int, A)):
#             raise ArithmeticError("Must be int!")
#         sc = other
#         if isinstance(other, A):
#             sc=other.x
#         return A(self.x + sc)
#
#     # def __radd__(self, other):
#     #     return self + other
#     #
#     # def __iadd__(self, other):
#     #     print("!")
#     #     if not isinstance(other, (int, A)):
#     #         raise ArithmeticError("Must be int.")
#     #     sc = other
#     #     if isinstance(other, A):
#     #         sc=other.x
#     #     self.x +=sc
#     #     return self
#
# a1=A(6)
# a2=A(10)
# # a=a1+10
# a=a1+a2
# print(a())
# # a=a1+a2
# # a=10+a2
# # a=a1+a2+a1
# # a1+=a2
# # a.x=a.x+2
# # a1=A(10)
# # a2=A(1)
# # a=a+a1+a2
# # # a=101+a
# # a+=100
# # print(a.sum())


# ---------------------------------------------------

# class Point3D:
#
#     def __init__(self, x, y, z):
#         if type(x) == int and type(y) == int and type(z) == int:
#             self.x = x
#             self.y = y
#             self.z = z
#         else:
#             raise TypeError("Incorrect type.")
#
#     def get_info(self):
#         return f'x = {self.x} y = {self.y} z = {self.z}'
#
#     def __add__(self, other):
#         if not isinstance(other, (Point3D)):
#             raise ArithmeticError("Must be int or clock.")
#         if isinstance(other, Point3D):
#             return Point3D(self.x + other.x, self.y + other.y, self.z + other.z)
#
#     def __sub__(self, other):
#         if not isinstance(other, (Point3D)):
#             raise ArithmeticError("Must be int or clock.")
#         if isinstance(other, Point3D):
#             return Point3D(self.x - other.x, self.y - other.y, self.z - other.z)
#
#
# first1 = Point3D(12, 13, 18)
# first2 = Point3D(6, 3, 9)
# first3 = first1 + first2
# print("Сложение координат:  ", first3.get_info())
# first3 = first1 - first2
# print("Вычитание координат: ", first3.get_info())
#
#
# # first1.x=first1.x+10
# # first1= first1+10
# # print(first1.get_info())

# ------------------------------------------------------------------------
# class Animal:
#     def __init__(self,kind):
#         self.kind = kind
#
#     def sound1(self):
#         print(self.kind,':', end = ' ')
#
# class Cat(Animal):
#     def __init__(self, x, age, kind):
#         super().__init__(kind)
#         self.x = x
#         self.age = age
#
#     # def __str__(self):
#     #     return self.x
#
#     def sound(self):
#         super().sound1()
#         print(f'{self.x} - I am cat {self.age} I am meowing.')
#
# class Dog(Animal):
#
#     def __init__(self, x, age, kind):
#         super().__init__(kind)
#         self.x = x
#         self.age=age
#
#     # def __str__(self):
#     #     return self.x
#
#     def sound(self):
#         super().sound1()
#         print(f'{self.x} - I am dog {self.age} I am barking.')
#
#
# cat= Cat("Miau...", "2.3 year", ' Cats')
# dog = Dog ("Gau!", "1,5 year old", ' Dogs')
#
# cat.sound()
# dog.sound()
# # a=[cat,dog]
# # for i in a:
# #     i.sound()
#
# # print("*" * 30)
# # for j in a:
# #     print(j)

# ------------------------------------------------------------------------
# #
# class Human:
#     def __init__(self, lastname, name, age):
#         self.name = name
#         self.lastname = lastname
#         self.age = age
#
#     def info(self):
#         print(end = "" f'{self.lastname} {self.name} {self.age} ')
#
# class Student(Human):
#     def __init__(self, lastname, name, age, direction, group, rating):
#         super().__init__(lastname, name, age)
#         self.direction = direction
#         self.group = group
#         self.rating = rating
#
#     def info(self):
#         super().info()
#         print(f'{self.direction} {self.group} {self.rating}')
#
# class Teacher(Human):
#     def __init__(self, lastname, name, age, spec, exp):
#         super().__init__(lastname, name, age)
#         self.exp = exp
#         self.spec = spec
#
#     def info(self):
#         super().info()
#         print(f'{self.spec} {self.exp}')
#
#
# # class Graduate:
#
#
# s=Student("Vissner", "ALex", 23, "Python", "P534", 5)
# s.info()
# t=Teacher("Hopkins", "Viola", "25", 'Physic', 120)
# t.info()


# ----------------------------  lesson 31 ---------------------------


# class Cat:
#     def __init__(self,name):
#         self.name = name
#
#     def __repr__(self):
#         return f"{self.__class__}: {self.name}"
#
#     def __str__(self): # work premially
#         return f"{self.name}"
#
# cat = Cat("Pushok")
# print(cat)


# ------------------------------


# class Point:
#     def __init__(self, *args):
#         self.__coords = args
#
#     def __len__(self):
#         return len(self.__coords)
#
# p =Point(5, 7, 6)
# print(len(p))


# ------------------------------


# class Point:
#     __slots__ = ("x", "y", "__length")  # interruption of creating new variables.
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.length = math.sqrt(x * x + y * y)
#
#     @property
#     def length(self):
#         return self.__length
#
#     @length.setter
#     def length(self, value):
#         self.__length = value
#
# # pt = Point(1, 2)
# # # pt.z = 5
# # # print(pt.__dict__)
# # # print(pt.x, pt.y, pt.z)
# # pt.length = 10
# # print(pt.x, pt.y, pt.length)
#
# class Point2D:
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# pt = Point(10, 20)
# pt2 = Point2D(10, 20)
# print("pt = ", pt.__sizeof__())
# print("pt2 = ", pt.__sizeof__() + pt2.__dict__.__sizeof__())
# # размеры отличаются
#
#
# ---------------------------------------------

#
# class Point:
#     __slots__ = ("x", "y")
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point3D(Point):
#     # __slots__ = "z"
#
#     def __init__(self, x, y, z):
#         super().__init__(x, y)
#         self.z = z
#
# pt = Point(1, 2)
# pt2 = Point3D(10, 20)
# pt2.z = 30
# print(pt2.z, pt2.y, pt2.z)
# # print(pt2.__dict__)


# --------------------FUNCTORS----------------------


# class Counter:
#     def __init__(self):
#         self.__counter = 0
#
#     def __call__(self, *args, **kwargs):
#         self.__counter += 1
#         print(self.__counter)
#         # return self.__counter
#
#
# c1 = Counter()
# c1()
# c1()
# c1()
# c2 = Counter()
# c2()
# c2()
# c2()

# ------------------------------------------------------
# class StripChars:
#     def __init__(self, chars):
#         self.__chars = chars
#
#     def __call__(self, *args, **kwargs):
#         if not isinstance(args[0], str):
#             raise ValueError('Argument must be str')
#         return args[0].strip(self.__chars)
#
#
# s1 = StripChars("!?:.; ")
# # print(s1(2))
# print(s1(" !Hello Word! "))
#
#
#
# def strip_string(chars):
#     def wrap(string):
#         if not isinstance(string, str):
#             raise ValueError("Agg must be str")
#         return string.strip(chars)
#     return wrap
#
# s2 = strip_string("!?:.; ")
# print(s2(" !Hello Word! "))


# ---------------------------------------------------------


# -------------Class as decorator--------------------------
#
# class MyDecorator:
#     def __init__(self,func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         print("Before calling")
#         self.func()
#         print("After calling")
#
#
# @MyDecorator
# def func1():
#     print("func - (*^")
#
# func1()


# ----------------------------------

# class MyDecorator:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, a, b):
#         print("Before calling")
#         return self.func(a,b)
#         print("After calling")
#         return res
#
#
# @MyDecorator
# def func1(a, b):
#     return a * b
#
#
# print(func1(2, 5))

# --------------------------------------------------------


# class Power:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, a):
#         print("Before calling")
#         # return self.func(a) + ", Python!"
#         print("After calling")
#
#         return self.func(a) + ", Python!"
#
#
# @Power
# def func1(a):
#     return a
#
#
# print(func1("Hello"))

# --------------------------------------------------------
# class MyDecorator:
#     def __init__(self,func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         st1 = "Before \n"
#         st2 = "\nAfter."
#         res = st1 + str(self.func(*args, **kwargs)) + st2
#         return res
#
# @MyDecorator
# def func1(a,b):
#     return a * b
#
# print(func1(2,5))
#
# @MyDecorator
# def func2(a, b, c):
#     return a * b * c
#
# print(func2(2, 5, 9))
#
#
# @MyDecorator
# def func3(a, b, c):
#     return a + b + c
#
# print(func3(2, 5, 9))


# -----------------------------------------------------------

# class MyDecorator:
#     def __init__(self, arg):
#         self.name = arg
#
#     def __call__(self, func):
#         def wrap(a, b):
#             print(" Before ")
#             print(self.name)
#             func(a, b)
#             print(" After. ")
#
#         return wrap
#
# @MyDecorator('test2')
# def add(a, b):
#     print(a, b)
#
# add(2, 5)


#
# class MyDecorator:
#     def __init__(self, arg): # arg from decorator parameter.
#         self.name = arg
#
#     def __call__(self, func):
#         def wrap(a, b):
#             print("Before \n")
#             # print(self.name, " - test2")  # - 'test2
#             print(func(a, b) + " & " + self.name)
#             print("\nAfter.")
#
#         return wrap
#
#
# @MyDecorator('test2')
# def add(a, b):
#     return (str(a + b))
#
#
# add(2, 5)


# class MyDecorator:
#     def __init__(self, arg):  # arg from decorator parameter.
#         self.name = arg
#
#     def __call__(self, func):
#         def wrap(a, b):
#             print(" Before ")
#             print(func(a, b) ** self.name)
#         return wrap
#
# @MyDecorator(3)
# def add(a, b):
#     return a * b
#
# add(2, 2)


# --------------------------------------------------------------


#
# class Power:
#     def __init__(self, arg):  # arg from decorator parameter.
#         self.name = arg
#
#     def __call__(self, func):
#         def wrap(a, b):
#             print(self.name)
#             print("Start...")
#             return func(a, b) ** self.name
#         return wrap
#
# @Power(3)
# def add(a, b):
#     return a * b
#
# print(add(2, 2))


# --------------------------------------------------------------

# -----------------Декорирование методов------------------------

# --------------------------------------------------------------
#
# # def dec(fn):                   # обычно выносят наружу
# #     def wrap(*args, **kwargs):
# #         print(" * " * 10)
# #         fn(*args, **kwargs)
# #         print(" * " * 10)
# #     return wrap
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     @staticmethod  # можно занести внутрь как статический метод.
#     def dec(fn):
#         def wrap(*args, **kwargs):
#             print(" * " * 10)
#             fn(*args, **kwargs)
#             print(" * " * 10)
#         return wrap
#
#     @dec
#     def info(self):
#         print(f'{self.name} {self.surname}')
#
#
# p1 = Person("Karl", "Bublick")
# p1.info()
#
# p2=Person("Nina", "Esparsa")
# p2.info()


# --------------------------------------------------------------

# -----------------Декорирование классов------------------------

# --------------------------------------------------------------


# def decorator(cls):
#     class Wrapper(cls):
#         def doubler(self, value):
#             return str(value - 1 ) + " - Version of Python"
#     return Wrapper
#
# @decorator
# class ActualClass:
#     def __init__(self):
#         print("Initializator ActualClass")
#
#     def quad(self, value):
#         return value * 4
#
#
# obj =ActualClass()
# print(obj.quad(4))
# print(obj.doubler(4))

# --------------------------------------------------------------


# --------------------------------------------------------------------------

# ----Descriptors (Дескрипторы) (__get__, __set__, __delete__, __set_name__)
#
#
# class StringD:
#     def __init__(self, value=None):
#         if value:
#             self.set(value)
#
#     def get(self):
#         return self.__value
#
#     def set(self,value):
#         self.__value = value
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = StringD(name)
#         self.surname = StringD(surname)
#         # self.__name = name
#         # self.__surname = surname
#     # @property
#     # def name(self):
#     #     return self.__name
#     #
#     # @name.setter
#     # def name(self, value):
#     #     self.__name = value
#     #
#     # @property
#     # def surname(self):
#     #     return self.__surname
#     #
#     # @name.setter
#     # def name(self, value):
#     #     self.__surname = value

# p = Person("Alex", "Petrov")
# # print(p.name)
# print(p.name.get())
# p.name.set("Nina")
# print(p.name.get())


# --------------------------------------------------------------------------

# ----Descriptors (Дескрипторы) (__get__, __set__, __delete__, __set_name__)
#
# class ValidString:
#     def __set_name__(self, owner, name):
#         self.__name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.__name]
#
#     def __set__(self, instance, value):
#         if not isinstance(value, str):
#             raise ValueError(f"{self.__name} - must be string")
#         instance.__dict__[self.__name] = value
#
# class Person:
#     name = ValidString()
#     surname = ValidString()
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
# p = Person("Ivan", "Petrov")
# print(p.name)
# print(p.surname)
#
# p.name = 'Vadim'
# print(p.name)
# print(p.surname)
# print(p.__dict__)
#
# # p.name = 34
# # print(p.name)

# ---------------------------------------------------------
# class Integer:
#
#     @classmethod
#     def verify_coords(cls, coord):
#         if not isinstance(coord, int):
#             raise TypeError(f'Coord {coord} must be integer')
#
#     def __set_name__(self, owner, name):
#         # print(")(*&^")
#         # print(owner.__dict__)
#         self.name ="_" + name
#
#     def __get__(self, instance, owner):
#         # return instance.__dict__[self.name]
#         return getattr(instance, self.name)
#
#     def __set__(self,  instance, value):
#         self.verify_coords(value)
#         # instance.__dict__[self.name]=value
#         setattr(instance, self.name, value)
#
# class Point3D:
#     x = Integer()
#     y = Integer()
#     z = Integer()
#
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
# p1 = Point3D(1,2,5)
# print(p1.__dict__)
# print(p1.x)


# --------------------------------------------------------------------

# ---------------------Метаклассы-------------------------

# --------------------------------------------------------------------

# a = 5
# print(type(a))
# print(type(int))

# class MyList(list):
#
#     def get_length(self):
#         return len(self)
#
#     def pr(self):
#         print(self, "---")


# MyList = type(
#     'MyList',
#     (list,),
#     dict(get_length = lambda self: len(self))
# )

#  --------------------THE SAME RESULT!
# MyList = type(
#     'MyList',
#     (list,),
#     dict(get_length = lambda self: len(self))
# )
#
#
# lst = MyList()
# # print(lst.__dict__)
# lst.append(5)
# lst.append(7)
# lst[0] = 3
# print(lst, lst.get_length())

# type(
# имя класса
# кортеж родительских классов
# словарь, содержащий атрибуты и их значения
# )


# super(MyMetaClass, cls).__init__(*args, **kwargs)

# --------------------------------------------------------------
# class MyMetaClass(type):
#     def __new__(cls, *args, **kwargs):
#         print('Создание нового объекта', args[0])
#         return super(MyMetaClass, cls).__new__(cls, *args, **kwargs)
#
#     def __init__(cls, *args, **kwargs):
#         print('Инициализация класса', args[0])
#         super(MyMetaClass, cls).__init__(*args, **kwargs)
#
#
# class Student(metaclass = MyMetaClass):
#     def __init__(self, name):
#         self.name = name
#
#     def get_name(self):
#         return self.name
#
# stud = Student("Rogazza")
# print("Name:", stud.get_name())
# print("Type of object Student: ", type(stud))
# print("Type of class Student: ", type(Student))


# -----------------------------------------------------------

#                          MODULES creating

# ------------------------------------------------------------

# import geometry.trian # both metoda are aviable
# import geometry.rect
# # import geometry.sq
# # import geometry
# # from geometry import *
# from geometry import rect, sq, trian # as tr
#
#
# r1 = rect.Rectangle(1, 2)
# r2 = rect.Rectangle(3, 4)
# s1 = sq.Square(10)
# s2 = geometry.sq.Square(20)
# t1 = trian.Triangle(1, 2, 3)
# t2 = geometry.trian.Triangle(4, 5, 6)
#
# shape = [r1, r2, s1, s2, t1, t2]
# for g in shape:
#     print(g.get_perimetr())
#
# # import sys
# # sys.path


# ----------------------------------------------------
# ----------------------IMPORT MODULES---------------
# ----------------------------------------------------


# from car import electrocar as el
#
# f=[el.ElectroCar("Tesla", "T", 2018, 99000), el.ElectroCar("Tesla", "TTT", 2019, 93400)]
# ff=list(map(lambda x: x.description_battery(), f))
# print(ff)
#
# def main():
#     e_car = el.ElectroCar("Tesla", "T", 2018, 99000)
#     e_car.show_car()
#     e_car.description_battery()
#
#
# if  __name__ == '__main__':
#     main()


# ----------------------------------------------------


#-----------------------------------------------------


from math import pi


# class Rectangle:
#     def __init__(self, l, h):
#         self.l = l
#         self.h = h
#
#     def get_rect_perimeter(self):
#         res = self.l * 2 + self.h * 2
#         print(f'Perimeter of Rectangle: {res}')
#         return res
#
#     def get_rect_area(self):
#         res = self.l * self.h
#         print(f'Square of Rectangle: {res}')
#         return res
#
#     def print_rect(self):
#         print(f"Sides: {self.l}, {self.h}")
#         return {self.l, self.h}
#
# class Circle:
#     def __init__(self, r):
#         self.r = r
#
#     def get_circle_circumference(self):
#         res = 2 * pi * self.r
#         print(f'Perimeter of Circle: {round(res, 2)}', "***")
#         return res
#
#     def get_circle_area(self):
#         res = pi * self.r ** 2
#         print(f'Square of Circle: {res}')
#         return res
#
#     def print_circle(self):
#         print(f"Radius of current Circle: {self.r}")
#         return self.r
#
# class Cylinder(Rectangle, Circle):
#     def __init__(self, r, h):
#         Circle.__init__(self, r)
#         Rectangle.__init__(self, self.get_circle_circumference(), h)
#
#     def get_volume(self):
#         res = self.get_circle_area() * self.h
#         print(f"Volume: {res}")
#         return res
#
#     def print_cylinder(self):
#         print(f"Radius of bottom: {self.r}, High: {self.h}")

#------

from shapes import cylinder, circle, rectangle


if  __name__ == '__main__':

    cylinders = [cylinder.Cylinder(4, 7), cylinder.Cylinder(2, 5),
                 cylinder.Cylinder(9, 3), cylinder.Cylinder(5, 5)]
    circles = [circle.Circle(4), circle.Circle(2), circle.Circle(6),
               circle.Circle(8), circle.Circle(1)]
    rects = [rectangle.Rectangle(3, 7), rectangle.Rectangle(2, 7),
             rectangle.Rectangle(19, 12)]


    circle_max_s = max(circles, key = lambda c: c.get_circle_area())
    print("Max circle square:", f'{round( circle_max_s.get_circle_area(),2)}')

    rect_min_p=min(rects, key = lambda s: s.get_rect_perimeter())
    print(f'Rectangle with less perimters: {rect_min_p.print_rect()}'
          f' = {rect_min_p.get_rect_perimeter()}')

    cylinders_v = list(map(lambda c: c.get_volume(), cylinders))
    cylinders_v_average = sum(cylinders_v)/len(cylinders_v)
    print(f"Average volume of cylinders: {round(cylinders_v_average, 2)}")




#-----------------------------------------------------------------------------

#                                   SERIALISATION
#                                and DESERIALISATION

#-----------------------------------------------------------------------------



# Упаковка данных
# Сериализация
# Десериализация

# В стандартной библиотеке Python
# marshal (.pyc)
# pickle
# json

#------------------------------------------------------
# dump() - сохраняет данные в файл
# load() - считывает из файла
#
# dumps()
# loads()
#------------------------------------------------------
#                             PICKLE
#------------------------------------------------------

import pickle

# filename = "basket.txt"
# shop_list = {
#     "fruits": ['apple', "mango"],
#     "vegetables": ['carrot'],
#     'buget': 100
# }
#
# with open(filename, "wb") as fh:
#     pickle.dump(shop_list, fh)
#
# with open(filename, "rb") as fh:
#     shop_list_2=pickle.load(fh)
#
# print(shop_list_2)

#-----------------------------------------------------

# class Test:
#     num = 35
#     st = 'Hello'
#     lst = [1,2,3]
#     dct = {'first': "a", 'second' : 2, "third": [1,2,3]
#            }
#     tpl =(23,22)
#
#     def __str__(self):
#         return f'Number: {Test.num}\nString: {Test.st}\nList:' \
#                f' {Test.lst}\nDict:{Test.dct}\nCortege: {Test.tpl} '
#
# obj =Test()
# print(obj)
#
# d_save = pickle.dumps(obj)
# print(f'Serialisation in string: \n{d_save}\n')
#
# d_read = pickle.loads(d_save)
# print(f'Serialisation in string: \n{d_read}\n')



#class Employee:
    def __init__(self, code, name):
        self.code = code
        self.name = name

    def show_salary(self):
        print("-" * 20)
        print(f"TYPE OF WORKER: {type(self).__name__}.")
        if type(self) == Admin:
            print(f'Code:{self.code} \nName{self.name} \nWeek salary: {self.week_salary}\n')
        if type(self) == Worker:
            print(f'Code:{self.code} \nName{self.name} \nWeek salary: {self.hours * self.pay_hours}\n ')
        if type(self) == Trade:
            print(
                f'Code:{self.code} \nName{self.name} \nWeek salary: '
                f'{self.week_salary + self.percent * self.overal_marge}')


class Admin(Employee):
    def __init__(self, code, name, week_salary):
        super().__init__(code, name)
        self.week_salary = week_salary


class Worker(Employee):
    def __init__(self, code, name, hours, pay_hours):
        super().__init__(code, name)
        self.hours = hours
        self.pay_hours = pay_hours


class Trade(Employee):
    def __init__(self, code, name, week_salary, percent, overal_marge):
        super().__init__(code, name)
        self.week_salary = week_salary
        self.percent = percent
        self.overal_marge = overal_marge


employee1 = Admin(12, "Valery Zadorozny", 1500)
employee1.show_salary()
# print(type(employee1).__name__)

employee2 = Worker(14, "Kelly Moon", 34, 25)
employee2.show_salary()

employee3 = Trade(17, "George Smith", 1200, 0.04, 10203)
employee3.show_salary()















