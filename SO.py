# # class Tutorial:
#     title = "H"          # атрибут класса.
#
#     def __init__(self, name):
#         self.name = name          # локальный атрибут


# class Point:
#     """Class number one"""
#     color = "red"
#     circle = 123
#
# a=Point()
# a.x=1
# a.y=2
# print(a.__doc__, a.x, a.y)
# print(Point.__doc__)
# print(hasattr(a, "circle"))
# print(a.__dict__)
# print(a.circle)
# setattr(a, 'color', "Violet")
# setattr(a, 'Weigh', 555)
# print(a.__dict__)
# # delattr(a, "color")
# del a.Weigh
# # del a.color
# print(a.__dict__)
# print(Point.color)
# print(hasattr(a, "color"))
# print(a.color)


# setattr(a, "color", "yellow")
# print(a.color)
# print(getattr(Point, "Fool", False))
# print(getattr(Point, "color", False))
# setattr(Point, "color", "green")
# print(getattr(Point, "color", False))
# print(a.__dict__)
# print(Point.__dict__)

# Point.type= "disc"
# Point.disc = "Wide"
# # print(Point.__dict__)
# setattr(Point, "sharp", 67.8)
# # print(Point.__dict__)
# print(Point.sharp)
# setattr(Point, "sharp", 888888 )
# setattr(Point, "color", "yellow")
# print(Point.sharp)
# print(Point.color)
# getattr(Point, "color")
# # getattr(Point, "Fool")
# print(getattr(Point, "Fool", False))
# print(getattr(Point, "color", False))
# print(getattr(Point, "color"))
# # del Point.sharp
# print(Point.sharp)
# delattr(Point, "color")
# # print(Point.__dict__)
# print(getattr(Point, "color", False))


# ----------------
# class DataBase:
#     pk = 1
#     title = "Классы и объекты"
#     author = "Сергей Балакирев"
#     views = 14356
#     comments = 12
#
# print(DataBase.__dict__)
# DataBase.views=100000
# setattr(DataBase, "inflation", 9)
# print(DataBase.__dict__)
# print(hasattr(DataBase, "inflation"))

# ----------------------------------------

# class Data:
#     pass
#
#
#
# setattr(Data, "color", "red")
# print(Data.__dict__)
# print(Data.color)
# -----------------------------------------
#
# class D:
#     pk = 1
#     title = "Классы и объекты"
#     author = "Сергей Балакирев"
#     views = 14356
#     comments = 12
#
# print(getattr(D, "title", False))
# print(getattr(D, "jk", False))

# -----------------------------------------

# class D:
#     total = 0
#     line=9098
#
# t=D()
# t.name="France"
# t.days=6
# D.total+=1
# t2=D()
# t2.name="Italy"
# t2.days=98
# D.total+=1
# print(D.total)
# print(D.__dict__)
# print(t.__dict__)
# print(D.__dict__)
# print(*t.__dict__.keys())
# print(*t.__dict__.items())
# print(hasattr(t, "line"))
# print(hasattr(t, "name"))
# print(t.line)

# ----------------------------------------------------------

# class D:
#     def set(self, x):
#         self.x=x
#
#     def get(self):
#         return self.x + 1000
# a=D()
# a.set(102)
# print(a.get())
# f=hasattr(a, "get")
# ff=hasattr(D, "get")
# ff=hasattr(D, "getsrf")
# print(f)
# print(ff)

# ----------------------------------------------------------
# class Media:
#
#     def open(self, file):
#         self.filename = file
#
#     def play(self):
#         print(f"Playing.{self.filename}")
#
# a=Media()
# b=Media()
# a.open("F1")
# b.open("F2")
# a.play()
# b.play()

# #----------------------------------------------------------
# class Graph:
#     Y = [0,10]
#     def pr(self):
#         print(Graph.Y)
#
#     def set_data(self, data):
#         self.data = data
#         print(self.data)
#     #
#     def draw(self):
#         # for i in self.data:
#         #     if i >= Graph.Y[0] and i<=Graph.Y[1]:
#         #         print(i, end = " ")
#         print(*[i for i in self.data if min(Graph.Y)<i<max(Graph.Y)])
# #
# #
# a=Graph()
# # a.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
# # a.draw()
#
# a.pr()
# Graph.pr(a)


# --------------------------------------------------------
# import sys
#
#
# class StreamData:
#     def create(self, fields, lst_values):
#         self.fields = fields
#         self.lst_values = lst_values
#
# class StreamReader:
#     FIELDS = ('id', 'title', 'pages')
#
#     def readlines(self):
#         lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк
#                                                                 # из входного потока
#         print(lst_in)
#
#
#         sd = StreamData()
#         res = sd.create(self.FIELDS, lst_in)
#         return sd, res
#
# sr = StreamReader()
#
# data, result = sr.readlines()


# ----------------------------------


# import sys
# print(sys.stdin)
# for line in sys.stdin:
# #     # rstrip('\n') "отрезает" от строки line идущий справа символ
# #     # перевода строки, ведь print сам переводит строку
#     print(line.rstrip('\n'))


# class A:
#     def create(self, fields, lst_values):
#         if len(fields) != len(lst_values):
#             return False
#         for i, key in enumerate(fields):
#             setattr((self, key, lst_values[i]))
#         return True
#
#
#
# s=A()
# print(s.create(["45","56","67"], ['er','rt','ty']))


# -----------------------------------------------------

# class DataBase:
#     lst_data = []
#     FIELDS = ('id', 'name', 'old', 'salary')
#
#     def insert(self,data):
#         for i in data:
#             self.lst_data.append(dict(zip(self.FIELDS, i.split())))
#         return self.lst_data
#
#
# f= ["1 Сергей 35 120000", "2 Федор 23 12000", "3 Иван 13 1200"]
# a=DataBase()
# print(a.insert(f))

# ----------------------------------------------------
# class Translator:
#     a=[]
#
#     def add(self, eng, rus):
#         if [eng,rus] not in self.a:
#             self.a.append([eng,rus])
#             print(self.a)
#         else:
#             print("Already exists.")
#
#     def remove(self, eng):
#         for i in self.a:
#             if i[0]==eng:
#                 self.a.remove(i)
#         print(self.a)
#
#     def trans(self, eng):
#         for i in self.a:
#             if i[0]==eng:
#                 print(i[1])
#
# s=Translator()
# s.add("tree", "дерево")
# s.add("river", "река")
# s.add("go", "идти")
# s.remove("tree")
# s.trans("go")

# ----------------------------

# class A:
#     def __init__(self, x=0, y=0):
#         self.x=x
#         self.y=y
#     def __del__(self):
#         print('deleting' + str(self))
#
#
# a=A(y=90)
# print(a.__dict__)

# ------------------------------------

# class Money:
#     def __init__(self, summ):
#         self.summ = summ
#
# my_money = Money(100)
# print(my_money.__dict__)
# print(my_money.summ)
# your_money = Money(1000)

# --------------------------------------


# class Point:
#     def __init__(self, x, y, color = 'red'):
#         self.x =x
#         self.y=y
#         self.color = color

# p1 = Point(10, 20)
# print(p1.__dict__)
# p2 = Point(12, 5, 'red')
# print(p2.__dict__)
# print(p1.color)

# points = [Point(i, i) for i in range(1, 10, 2)]
# points[1].color = 'yellow'
# print(points)

# s=[]
# for i in range(10):
#     i = Point(i, i+2)
#     print(i.__dict__)
#     s.append(i)
# print(s)

# ------------------------------------
import random


#
# a=random.randint(1,100)
# print(a)

# class Line:
#
#     def __init__(self, a,b,c,d):
#         self.sp = (a, b)
#         self.ep = (c, d)


# s = Line(23, 4, 56, 7)
# print(s.__dict__)
# elements=[]
# for i in range(20):
#     a = random.randint(0,9)
#     b = random.randint(0, 9)
#     c = random.randint(0, 9)
#     d = random.randint(0, 9)
# elements.append(random.choice([Line(0, 0, 0, 0), Rect(a, b, c, d), Ellipse(a, b, c, d)] ))
# elements.append(Line(0, 0, 0, 0))
#
#     i=Line(a,b,c,d)
#     print(i.__dict__)
# # print(elements)


# class Line:
#
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def check1(self):
#         if self.a+self.b<self.c or self.c+self.b<self.a \
#                 or self.c+self.a<self.b or self.a < 0  or self.b <0  or self.c < 0:
#             print("Not Triangle...")
#         else:
#             print("Triangle")
#
# a=Line(78,49,900)
# a.check1()

# ----------------------------------------------------------
# class Graph:
#     dd=" "
#     def __init__(self, data, is_show=True):
#         self.data = data
#         self.is_show=is_show
#         print(self.data)
#
#     def show_table(self):
#
#         if not self.is_show:
#             print("Closed...")
#         else:
#             # for i in d:
#             #     self.dd += str(i) + " "
#             print(" ".join(map(str, self.data)))
#
# d=[23,45,3,5,564,3,234]
# a=Graph(d, True)
# a.show_table()

# dd=""
# for i in d:
#     dd += str(i) + " "
# print(dd)
# print(a.data)

# -----------------------------------------------------------------

# class CPU:
#     def __init__(self, name, frequency):
#         self.name = name
#         self.frequency = frequency
#
# class Memory:
#     def __init__(self, name, memorysize):
#         self.name = name
#         self.memorysize = memorysize
#
# class MotherBoard:
#     def __init__(self, name, CPU, Memory):
#         self.name = name
#         self.CPU = CPU
#         self.Memory = Memory
#         # print(f'{self.cpu.name}')
#         # self.total_mem_slots = 4
#         # self.mem_slots = mems[:self.total_mem_slots]
#
#     def get_config(self):
#         print(f"**** {self.CPU.name} ******")
#         print(f"**** {self.Memory.name} ******")
#         return f"MotherBoard: {self.name}, " \
#                f"Центральный процессор: {self.CPU.name}"
#
# mb = MotherBoard("AMD", CPU("INTEL 79798",2000), Memory("King", 1000))
# print(mb.get_config())


# ------------------------------------------------------------------
# class Cart:
#
#     def __init__(self):
#         self.goods = []
#     def add(self, a):
#         self.goods.append(a)
#         print(self.goods)
#         return self.goods
#     def rem(self, indx):
#         self.goods.pop(indx)
#         return self.goods
#
#     def get_list(self,x):
#         print(x.name)
#         # return [f'{x.name}{x.price}']
#
# class Table:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
# class TV:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
# class Notebook:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
# class Cup:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#
# s=Cart()
# print(s.add(TV("Rubin", 898)))
# s.get_list(TV)


# -------------------------------------------------------
# import sys
#
# class ListObject:
#     def __init__(self, data):
#         self.data = data
#         self.next_obj = None
#
#     def link(self, obj):
#         self.next_obj = obj
#         # print(self.next_obj, "---")
#
#
# # lst_in =list(map(str.strip, sys.stdin.readlines()))
#
#
# lst_in = ["1. First steps in OOP", "1.1 Methods of classes. Self"]
# head_obj = ListObject(lst_in[0])
# obj = head_obj
#
# for i in range(1,len(lst_in)):
#     obj_new = ListObject(lst_in[i])
#     obj.link(obj_new)
#     obj = obj_new
#
# print(obj)


# ---------------------------------------------------------------------------


#
# import sys

# class ListObject:
#     def __init__(self, data):
#         self.data = data
#         self.next_obj = None
#
#     def link(self, obj):
#         self.next_obj = obj
#         print("---", self.next_obj )
#
#
# lst_in = [23,34,45,56,67,78,89]
# head_obj = ListObject(lst_in[0])
# obj = head_obj
#
# for i in range(1,len(lst_in)):
#     obj_new = ListObject(lst_in[i])
#     print(obj_new)
#     obj.link(obj_new)
#     obj = obj_new


# lst_in =list(map(str.strip, sys.stdin.readlines()))

#
# lst_in = ["1. First steps in OOP", "1.1 Methods of classes. Self"]

# print(head_obj , "head obj")
# print(head_obj.__dir__)

# print(head_obj)
# print(obj)


# ----------------------------------------------------------------------

# class Cell:
#     def __init__(self, around_mines, mine):
#         self.around_mines=around_mines
#         self.mine = True
#         self.fl_open=False
#
# class GamePhone:


# c1 = Cell(around_mines, mine)
# pole_game = GamePole(N,M)
#

# ----------------------------------------------

# class Point:
#     def __new__(cls, *args, **kwargs):
#         print("calling __new__ for " + str(cls))
#         return super().__new__(cls)
#
#     def __init__(self, x=0, y=0):
#         print("Calling __init__")
#         self.x = x
#         self.y = y
#
#
# pt =Point(1, 2)
# print(pt)


# ---------------------------------------------

# class Abst:
#     def __new__(cls, *args, **kwargs):
#         return "impossible to create sub class"
#         return super().__new__(cls)
#
#     def __init__(self, x=0, y=0):
#         print("Calling __init__")
#         self.x = x
#         self.y = y
#
# pt =Abst(1, 2)
# print(pt)

# ------------------------------------------------
# class Point:
#     __instance=None
#     __count =0
#     def __new__(cls,count = 0, *args, **kwargs):
#         if cls.__count <4:
#             cls.__instance = super().__new__(cls)
#             cls.__count+=1
#             print("***")
#         return cls.__instance
#
#
#     def __init__(self, x=0, y=0):
#         print("**** Calling __init__" + str(self))
#         self.x = x
#         self.y = y
#
# #
# pt1 = Point(1, 2)
# pt2 = Point(1222, 334)
# pt3 = Point(152, 434)
# pt4 = Point(13222, 3144)
# pt5 = Point(122, 344)
# pt6 = Point(1222, 3144)
# pt7 = Point(132, 3544)
# pt8 = Point(1232, 31465)
#
# print(pt1)
# print(pt2)
# print(pt3)
# print(pt4)
# print(pt5)
# print(pt6)
# print(pt7)
# print(pt8)


# --------------------------------------
# class Point:
#     count = 0
#     def __new__(cls, *args, **kwargs):
#         if cls.count < 4:
#             print("* * * Calling __new__" + str(cls))
#             cls.count += 1
#             return super().__new__(cls)
#         else:
#             return None
#     def __init__(self, x=0, y=0):
#         print("**** Calling __init__" + str(self))
#         self.x = x
#         self.y = y
#
# pt1 = Point(1, 2)
# pt2 = Point(1222, 334)
# pt3 = Point(152, 434)
# pt4 = Point(13222, 3144)
# pt5 = Point(122, 344)
# pt6 = Point(1222, 3144)
# pt7 = Point(132, 3544)
# pt8 = Point(1232, 31465)
#
# print(pt1)
# print(pt2)
# print(pt3)
# print(pt4)
# print(pt5)
# print(pt6)
# print(pt7)
# print(pt8)

# --------------------------------------------------------------

# TYPE_OS = 1   #1 -Windows; 2-Linux
#
# class DialogWindows:
#     name_class ="DialogWindows"
#
# class DialogLinux:
#     name_class = "DialogLinux"
#
# class Dialog:
#     def __new__(cls, s, type, *args):
#         if type ==1:
#             cls.s=DialogWindows()
#             print( "cls.s=DialogWindows()")
#         else:
#             cls.s = DialogLinux()
#             print("cls.s=DialogLinux()")
#
#
# dlg =Dialog("s", 1 )
# dlg2 =Dialog("s", 2 )
# setattr("s", 1)

# -------------------------------------------------------
#
# TYPE_OS = 1   #1 -Windows; 2-Linux
#
# class DialogWindows:
#     def __init__(self):
#         print("!!!!!!!!!")
#     name_class ="DialogWindows"
#
# class DialogLinux:
#     name_class = "DialogLinux"
#
# class Dialog:
#     def __new__(cls, *args, **kwargs):
#         obj = None
#         if TYPE_OS ==1:
#             obj =super().__new__(DialogWindows)
#         else:
#             obj = super().__new__(DialogLinux)
#         obj.name = args[0]
#         print(obj.name)
#         return obj
#
# dlg = Dialog("Fantom")
# print(dlg.name_class, "-----")
# # print(dlg.name)
# -------------------------------------------------

#
# a= "add lock dod sad first"
# aa=a.split()
# print(aa)
# for i in aa:
#     if i[0]==i[-1]:
#         print(i)
#     else:
#         print("-")

#
# n=int(input())
# for i in range(1,n):
#     if i ** 2 > n:
#         print(i)
#         break


# ------------------
# class Point:
#     "Instruction"
#     color = "red"
#     circle = 2
#
# a=Point()
# b=Point()
#
# a.x=1
# print(a.__dict__)
# a.y=2
# print(a.__dict__)
#
# b.x=10
# print(a.__dict__)
# b.y=20
# print(a.__dict__)
#
# print(Point.__doc__)

# p=Point()
# p.color = "blue"
# print(p.__dict__)
# Point.color = "Yellow"
# Point.quantity = 12
# print(Point.__dict__)
# setattr(p, "heigth", 8989)
# print(p.__dict__)
# print(hasattr(p, "heigth"))
# delattr(p, "heigth")
# print(p.__dict__)
# print(getattr(p, "color"))
# del p.color
# print(p.color)


# ---------------------------

# class Point:
#     a=2
#     b=3
#
# Point.a=23
# Point.c=230
# print(Point.__dict__)
# print(hasattr(Point, "b"))
# print(getattr(Point, "a"))
# print(getattr(Point, "v", False))
# print(getattr(Point, "a", True))

# ------------------------------


#
# class Point:
#     type="ellipse"
#     color = 'red'
#
# fig=Point()
# fig.start=(10,5)
# fig.spt=(103,54)
# fig.color = "blue"
# print(fig.__dict__)
# delattr(fig, "color")
# print(fig.color)
# print(fig.__dict__)
#
# print(hasattr(fig, "stp"))
# print(hasattr(fig, "color"))

# ----------------------------
# class Point:
#     color = 'blue'
#
#     def f(self, x, y):
#         self.x=x
#         self.y=y
# print(self, "*****")
# print(pt)
# print(Point)
# print(pt.__dict__)
# print(Point.color)
# print(pt.color, "&")
# print(hasattr(pt, "color"))
# setattr(pt, "size", 98989898)
# setattr(Point, "size1", 333333)
#         # print(hasattr(pt, "x"), "^^^^^^^^^")
#     def g(self):
#         return (self.x , self.y)
#
# pt=Point()
# pt.f(34,56)
# print(pt.g())
# d=getattr(pt, "g")
# print(d())
# ---------------------------------------------------
#
# class MediaPlayer:
#
#     def open(self, file):
#         self.filename = file
#
#     def play(self):
#        print('Playing')
#
# m1=MediaPlayer()
# m1.open("FILEMEDIA1")
# m1.play()
# m2=MediaPlayer()
# m2.play()

# --------------------------------------------------
#
# class Graph:
#     LIMIT_Y=[0,10]
#
#     def setdata(self, data):
#         self.data=data
#
#     def draw(self):
#         print(list(filter(lambda x: 10>x>0, self.data)))
#
# a=Graph()
# a.setdata([23,-5,87,34,8,-234,5,547,67,32,-54,23,6,6])
# a.draw()


# ------------------------------------------------------
# class StreamData:
#
#     def create(self, fields, lst_values): #FIELDS, lst
#         self.fields = fields
#         self.lst_values = lst_values
#         for i, key in enumerate(self.fields):
#             setattr(self, key, self.lst_values[i])
#         print(hasattr(self, "id"))
#         print(hasattr(self, "title"))
#         print(self.__dict__)
#
#
# class Stream:
#     FIELDS = ("id", "title", "pages")
#
#     def readlines(self):
#         lst = ["10", "Python", "512"]
#         sd=StreamData()
#         res = sd.create(self.FIELDS, lst)
#         return sd, res
#
# sr=Stream()
# sr.readlines()
# data,result = sr.readlines()


# a=[23,45,34,56,6,678,798]
# b=['we', 'f', 't', 'y', 'f', 't', 'y']
# for i, key in enumerate(a):
#     print(i, key, b[i])

# -----------------------------------------

# class Point:
#     def __init__(self,a):
#         self.a=a
#         print(self.a)
#     def __del__(self):
#         print("deleting")
#
#     def check(self):
#         print("Check")
#         print(Point.__dict__)
#
#
#
# s=Point(34)

# ----------------------------------------
# class Money:
#     def __init__(self, a, b, color="blue"):
#         self.a = a
#         self.b = b
#         self.color = color
#         # print(self.a, self.b, self.color)
#
# points=[Money(i, i) for i in range(0, 25)]
# points[2].color= "VIOLET"
# print(points[2])

# -----------------------------
# import random
# class Line:
#
#     def __init__(self, a,b,c,d):
#         print("working init ----")
#         self.sp =(a,b)
#         self.ep = (c,d)
#
#
# class Rect:
#     def __init__(self, a,b,c,d):
#         self.sp =(a,b)
#         self.ep = (c,d)
#
# class Ellipse:
#     def __init__(self, a,b,c,d):
#         self.sp =(a,b)
#         self.ep = (c,d)
#
# g1 = Line(2,3,4,5)
# g2 = Rect(34,45,5,6)
# g3 = Ellipse(12,3,5,7)
#
# names=[Line, Rect, Ellipse]
#
# elements = [random.choice(names)(random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10)) for i in range (100)]
# print(elements)
#
# for i in elements:
#     if type(i)=="Line":
#         print("!")


# from random import randint
#
# # s = [("GH","jk","fd")[randint(0,2)] for i in range(10)]
# # print(s)
#
# a=("GH","jk","fd")[randint(0,2)]
# print(a)

# --------------------------------------------------------------------------

# class TriangleChecker:
#     def __init__(self,a,b,c):
#         self.a=a
#         self.b=b
#         self.c=c
#     #
#     def checker(self):
#         print("@@@@")
#         if type(self.a)==int:
#             print("INT")
#
#     def check(self):
#         print("check ---")
#         self.checker()
#
#
# a,b,c=map(int, input(": ").split())
#
# tr = TriangleChecker(a,b,c)
# tr.check()


# ------------------------------------------------------------------
#
# class Graph:
#     def __init__(self, data):
#         self.data = data
#         self.show = True
#         print(self.data, "* INIT")
#
#     def setdata(self, h):
#         self.data = h
#         print(self.data)
#
#     def showgraph(self):
#         if self.show ==True:
#            print('Print graph')
#         else:
#             print("none")
#
#     def showdiag(self):
#         print('Diagramm')
#
#     def setshow(self, a):
#         self.show=a
#
#
# data = [2, 3, 5, 23, 43, 57, 563, 2]
# gr = Graph(data)
# gr.setdata([34,4,56])
# gr.setshow(True)
# gr.showgraph()
# # ------------------------------------------------------------

# class CPU:
#     def __init__(self, name, fr):
#         self.name = name
#         self.fr=fr
# class Memory:
#     def __init__(self, name, size):
#         self.name = name
#         self.size = size
# class MotherBoard:
#     def __init__(self, name,cpu,*mems):
#         self.name = name
#         self.cpu = cpu
#         self.totalmemslots = 4
#         self.memslots= mems[:self.totalmemslots]
#     def getconfig(self):
#         return [f"{self.name}", f"{self.cpu.name},{self.cpu.fr}",
#                 f"{self.totalmemslots}", "Memory:" + " ;".join(map(lambda x: f"{x.name} - {x.size}", self.memslots))]
#
# mb= MotherBoard("GigByte", CPU("Intel", 2000), Memory("Kingseton",10600),
#                 Memory("Kings456ton1",2003450), Memory("Kingswereton",1500),Memory("Kinton1",203450))
# d=mb.getconfig()
# print(d)
# -------------------------------------------------
#
# class A:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
# class B:
#     def __init__(self, bname, a):
#         self.bname = bname
#         self.a = a
#
#     def conf(self):
#         return[f" {self.bname}", f"A-class: {self.a.name} *** {self.a.surname}" ]
#
# f=B('NAME FIRST', A("Alex", "Vissner"))
#
# print(f.conf())
# print(f.a.surname)
# print(f.bname)
# print(f.a.name)

# ---------------------------------------------------

# class Point:
#     s = None
#
#     def __new__(cls, *args, **kwargs):
#         print("Calling __new__")
#         if cls.s == None:
#             cls.s = super().__new__(cls)
#         return cls.s
#
#     def __init__(self, x=0, y=0):
#         print("Calling __init__.")
#         self.x = x
#         self.y = y
#
#
# pt = Point(12, 34)
# pt2 = Point(122, 314)
# print(pt)
# print(pt2)


# ------------------------------------
#
# class Point:
#     count = 0
#
#     def __new__(cls, *args, **kwargs):
#         print("Calling __new__")
#         if cls.count <4:
#             cls.count +=1
#             return super().__new__(cls)
#
#     def __init__(self, x=0, y=0):
#         print("Calling __init__.")
#         self.x = x
#         self.y = y
#
# pt1 = Point(1, 2)
# pt2 = Point(1222, 334)
# pt3 = Point(152, 434)
# pt4 = Point(13222, 3144)
# pt5 = Point(122, 344)
# pt6 = Point(1222, 3144)
# pt7 = Point(132, 3544)
# pt8 = Point(1232, 31465)
#
# print(pt1)
# print(pt2)
# print(pt3)
# print(pt4)
# print(pt5)
# print(pt6)
# print(pt7)
# print(pt8)

# ----------------------------------
#
# class Point:
#     __instance=None
#     __count =0
#     def __new__(cls,count = 0, *args, **kwargs):
#         if cls.__count <4:
#             cls.__instance = super().__new__(cls)
#             cls.__count+=1
#             print("***")
#         return cls.__instance
#
#
#     def __init__(self, x=0, y=0):
#         print("**** Calling __init__" + str(self))
#         self.x = x
#         self.y = y
#
# pt1 = Point(1, 2)
# pt2 = Point(1222, 334)
# pt3 = Point(152, 434)
# pt4 = Point(13222, 3144)
# pt5 = Point(122, 344)
# pt6 = Point(1222, 3144)
# pt7 = Point(132, 3544)
# pt8 = Point(1232, 31465)
#
# print(pt1)
# print(pt2)
# print(pt3)
# print(pt4)
# print(pt5)
# print(pt6)
# print(pt7)
# print(pt8)


# ------------------

#
# class Point:
#     __instance=None
#     __count =0
#     def __new__(cls,count = 0, *args, **kwargs):
#         if cls.__count <4:
#             cls.__instance = super().__new__(cls)
#             cls.__count+=1
#             print("***")
#         return cls.__instance
#
#
#     def __init__(self, x=0, y=0):
#         print("**** Calling __init__" + str(self))
#         self.x = x
#         self.y = y
#
# #
# pt1 = Point(1, 2)
# pt2 = Point(1222, 334)
# pt3 = Point(152, 434)
# pt4 = Point(13222, 3144)
# pt5 = Point(122, 344)
# pt6 = Point(1222, 3144)
# pt7 = Point(132, 3544)
# pt8 = Point(1232, 31465)
#
# print(pt1)
# print(pt2)
# print(pt3)
# print(pt4)
# print(pt5)
# print(pt6)
# print(pt7)
# print(pt8)

# --------------
# class Point:
#     __instance = None
#     count = 0
#     def __new__(cls, *args):
#         if cls.count < 4:
#             cls.__instance= super().__new__(cls)
#             cls.count+=1
#             print(cls.__instance, "***")
#             print(cls.__instance)
#         return cls.__instance
#
#
# pt1 = Point(1, 2)
# pt2 = Point(1222, 334)
# pt3 = Point(152, 434)
# pt4 = Point(13222, 3144)
# pt5 = Point(122, 344)
# pt6 = Point(1222, 3144)
# pt7 = Point(132, 3544)
# pt8 = Point(1232, 31465)
#
# print("------------")
# print(pt1)
# print(pt2)
# print(pt3)
# print(pt4)
# print(pt5)
# print(pt6)
# print(pt7)
# print(pt8)

# -------------------------------------------------------------
#
#
# class DialogWindows:
#     name_class = "DialogWindows"
# def __init__(self, name):
#     self.name = name
#     print("111", f"{self.name} ---")
#     self.r=23

#
# class DialogLinux:
#     name_class = "DialogLinux"
# def __init__(self, name):
#     self.name = name
#     print("222", f"{self.name} 000")
#     self.rr=28


# class Dialog:
#     def __new__(cls, *args, **kwargs):
#         obj = None
#         if args[1]==1:
#             obj=super().__new__(DialogWindows)
#         else:
#             obj=super().__new__(DialogLinux)
#         obj.name = args[0]
#         return obj
#
#
#
# dlg=Dialog("Kelly",1)
# print(dlg)
# print(dlg.name)
# print(Dialog.__dict__)


# def __init__(self, name):
#     self.name=name
# def create(self):
#     if TYPE_OS==1:
#        self.a=DialogWindows(self.name)
#        return self.a
#     else:
#         self.b=DialogLinux(self.name)
#         return self.b


# -------------------------------------------------------------

# class Point:
#     def __init__(self, x,y):
#         print("init in working.")
#         self.x=x
#         self.y=y
#
#     def clone(self):
#         print("clone is working.")
#         f=Point(self.x, self.y)
#         print(self.x, self.y, "working second it")
#         return f
#
# pt=Point(2,5)
# print(pt)
# g=pt.clone()
# print(g)


# ---------------------------------------------------------------


# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def get_coord(self):
#         return self.x, self.y
#
# v=Vector(1,2)
# f=Vector.get_coord(v)
# print(f)

# ---------------------------------------------------------------
# class Loader:
#     @classmethod
#     def json_parse(cls):
#         print("working...")
#         return " "
#
# ld= Loader()
#
# Loader.json_parse()
# ld.json_parse()
# # ld.json_parse(Loader)
# res = ld.json_parse()
# # Loader.json_parse(ld)
# res = Loader.json_parse()

# ---------------------------------------------
# class Factory:
#     @staticmethod
#     def build_sequence():
#         return []
#     @staticmethod
#     def build_number(sub):
#         return int(sub)
#
# class Loader:
#     @staticmethod
#     def parse_format(string, factory):
#         seq = factory.build_sequence()
#         print(seq, 'seq')
#         print(string.split(" "))
#         for sub in string.split(" "):
#             print(sub, type(sub), 'sub')
#             item = factory.build_number(sub)
#             seq.append(item)
#         return seq
#
# res = Loader.parse_format("4 5 -6", Factory)
# print(res)


#
# a="23, 45,  56"
# aa = a.split()
# print(aa)


# -----------------------------------------------
#
# class FormLogin:
#     def __init__(self, lgn, psw):
#         self.login =lgn
#         self.password =psw
#     def render_template(self):
#         return "\n".json(['<form action = "#">', self.login.get_html(), self.password.get_html(), '</form>'])
#
# login = FormLogin(TextInput("LOGIN"), PasswordInput("PASSWORD"))
# html = login.render_template()
#
# class TextInput:
#     def __init__(self, name, size):
#         self.name = name
#         self.size = size
#
#     def get_html(self):
#
# class PasswordInput:
#     def __init__(self, name, size):
#         self.name = name
#         self.size = size
#
# login = TextInput("NAME_1", 'QWERTY')
# psw =PasswordInput("NAME_2","ASDFGH")


# ------------------------------------------------------------
#
# from accessify import private, protected
#
# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = self.y =0
#         if self.__check_value(x) and self.__check_value(y):
#             self.__x=x
#             self.__y=y
#
#     @private
#     @classmethod
#     def __check_value(cls, x):
#         return type(x) in (int, float)
#
#     def set_coord(self, x, y):
#         if self.__check_value(x) and self.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             raise ValueError ("Coords must be integer.")
#
#     def get_coord(self):
#         return self.__x, self.__y
#
# pt=Point(1, 2)
# pt.set_coord(56, 20)
# print(pt.get_coord())
# # print(pt.__x)
# print(Point.__dir__)
# print(dir(pt))
# print(pt._Point__x)
# print(pt._Point__y)
# pt._Point__y = 987
# print(pt._Point__y)


# ------------------------------------------------------------
# from accessify import private, protected
#
# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = self.y =0
#         if self.__check_value(x) and self.__check_value(y):
#             self.__x=x
#             self.__y=y
#
#     # @private
#     @classmethod
# def __check_value(cls, x): # убрали двы подчеркивания для публичности
#     return type(x) in (int, float)
#
#     def set_coord(self, x, y):
#         if self.__check_value(x) and self.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             raise ValueError ("Coords must be integer.")
#
#     def get_coord(self):
#         return self.__x, self.__y
#
# pt=Point(1, 2)
# pt.set_coord(10, 20)
# # pt.check_value(5)
# pt._Point__check_value(5)
#
# # print(pt.get_coord())
# # # print(pt.__x)
#
# # print(Point.__dir__)
# # print(dir(pt))
# # print(pt._Point__x)
# # print(pt._Point__y)
# # pt._Point__y = 987
# # print(pt._Point__y)
#


# ---------------------------------------
#
# class Clock:
#     def __init__(self, time):
#         self.__time = 0
#         if self.__checktime(time):
#             self.__time = time
#
#     @classmethod
#     def __checktime(self, tm):
#         return 100000>tm>=0 and type(tm)==int
#
#     def settime(self, tm):
#         if self.__checktime(tm):
#             self.__time = tm
#         else:
#             print("Incorrect input time.")
#
#     def gettime(self):
#         return self.__time
#
#
# clock = Clock(4530)
# print(clock._Clock__checktime(-10000000000))
# # print(clock.gettime())
# # clock.settime(-90)
# # clock.settime(90)
# # print(clock.gettime())


# ----------------------------------------------------------
#
# class Money:
#     def __init__(self, mn):
#             self.__money = 0
#             if self.__check_money(mn):
#                 self.__money= mn
#     @classmethod
#     def __check_money(cls, money):
#         return money>=0
#
#     def set_money(self, money):
#         if self.__check_money(money):
#             self.__money=money
#
#     def get_money(self):
#         return self.__money
#
#     def add_money(self, mn):
#         print(mn.get_money(), "__________")
#         self.__money += mn.get_money()
#         print(self.__money)
#         # return self.__money
#
# mn=Money(11111)
# mn1=Money(10)
# mn1.add_money(mn)
# # mn2=Money(20)
# # mn1.set_money(100)
# # mn1.add_money(140)
# # print(mn1.get_money())
#
#


# --------------------------------------------------------------
# class Point:
#     MAX_COORD = 100
#     MIN_COORD = 0
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def set_coord(self, x, y):
#         # if Point.MIN_COORDS <= x <= Point.MAX_COORDS:
#         if self.MIN_COORD <= x <= self.MAX_COORD:
#             self.x = x
#             self.y = y
#
#     def __getattribute__(self, item):
#         print("__getatribute__ working")
#         if item == 'x':
#             raise ValueError("access is forbidden")
#         else:
#             return object.__getattribute__(self,item)
#
#     def __setattr__(self, key, value):
#         print("__setattr__ working")
#         # print(self, key, '___', value)
#         if key == "z":
#             raise AttributeError("Forbidden name of attribute.")
#         else:
#             # object.__setattr__(self, key, value)
#             # self.x = value
#             self.__dict__[key]=value
#
#     def __getattr__(self, item):
#         # print("__getattr__: " + item)
#         return False
#
#     def __delattr__(self, item):
#         print("__delattr__ working: " + item)
#         object.__delattr__(self, item)
#
#
#
#     # @classmethod
#     # def set_bound(cls, left):
#     #     cls. MIN_COORD=left
#
# pt1 = Point(1,2)
# pt2 = Point(10,20)
# # pt1.z =5
# # print(pt1.yy)
# del pt1.x
# print(pt1.__dict__)
# # print(pt1.MAX_COORD)
#
# # a=pt1.y
# # print(a)
#
# # pt1.set_bound(-100)
# # print(pt1.__dict__)
# # print(Point.__dict__)


# ---------------------------PROPERTY--------------------------------------
#
# class Person:
#     def __init__(self, name, old):
#         self.__name=name
#         self.__old=old
#
#     def get_old(self):
#         return self.__old
#
#     def set_old(self, old):
#         self.__old = old
#
#     old = property(get_old, set_old) # without () !!!
#
# p = Person("Sergey", 20)
# p.__dict__['old'] = 'old in object p'
# p.old= 38
# # p.set_old(35)
# print(p.old, p.__dict__)
# # print(p.get_old())
# # a=p.old


# ------------------------------------------

# class Point:
#     def __init__(self, name):
#         self.__name=name
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, name):
#         if type(name)== str and 100>len(name)>2:
#             self.__name = name
#         else:
#             print("Incorrect data")
#
#     @name.deleter
#     def name(self):
#         del self.__name
#
# p=Point("Kelly")
# print(p._Point__name)
# p.name = "L"
# p.__dict__['name'] = "Vanessas"
# print(p._Point__name)
# print(p.name)
# # print(p.name)
# # del p.name
# # print(p.__dir__)

# -----------------------------------------------------------

# class WindowDlg:
#     def __init__(self, name, width, heigh):
#         self.__name = name
#         self.__width = width
#         self.__heigh = heigh
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, name):
#         self.__name = name
#         self.show()
#
#     @name.deleter
#     def name(self):
#         del self.__name
#
#     def show(self):
#          print(f" {self.__name}, {self.__width} {self.__heigh}")
#
#
# w=WindowDlg("Wind", 12, 34)
# w.name="New wind"
# w.name="New r"


# class StackObj:
#     def __init__(self, data, next):
#
# class Stack:
#     def __init__(self, data,next):


# ------------------------------------------------------------

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#     def append(self, val):
#         end = Node(val)
#         n = self
#         while (n.next):
#             n = n.next
#             print(n, " n in cycle")
#         n.next = end
#
#
# ll = Node(1)
# ll.append(2)
# ll.append(3)

#   "n and self and ll are the same"


#---------------------------------------------------

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        print("---")
        return f" [{self.data}] -> {self.next}"

# node1=Node(1)
# node2=Node(2)
# print(node2)
# node1.next = node2
# node3=Node(3)
# node2.next = node3
# node4=Node(4)
# node3.next = node4
# print(node1)
# print(node2)




class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        print("---")
        return str(self.head)

    if __name__=="__main__":
        linked_list = LinkedList()
        temp = Node(1)
        linked_list.head = temp
        for i in range(2,5):
            temp.next = Node(i)
            temp = temp.next

        print(linked_list)











