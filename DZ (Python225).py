# ----------------------------------------
#        HOME WORK of LESSON 22 (DZ 22)

# class Book:
#     name = "name of book"
#     year = "0000"
#     producer = "producer"
#     genre = "genre"
#     writer = "writer"
#     price = "00"
#     def print_info(self):
#         print(" Personal info. ".center(40, "*"))
#         print(f"name: {self.name}\nyear: {self.year}\n"
#             f"producer:{self.producer}\ngenre: {self.genre}\n"
#             f"writer: {self.writer}\nprice: {self.price}")
#         print("-" * 40)
#     def input_info(self, name, year, producer, genre,
#                writer, price):
#         self.name = name
#         self.year = year
#         self.producer = producer
#         self.genre =genre
#         self.writer = writer
#         self.price = price
#     def set_name(self, name):
#         self.name = name
#     def get_name(self):  # get name
#         a = "Name: " + self.name
#         return a
#
# f1=Book()
# f1.input_info("Tom Sayer", "1878", "Mr.Brown","Adventure", "M.Twen", "14$")
# f1.print_info()
# f1.set_name("Lost Word")
# print(f1.get_name())
# f1.print_info()
# f1.set_name("Island of Treasure")
# print(f1.get_name())


# ----------------------------------------------------------------
#            HOME WORK of LESSON 23 (DZ 23)

#
# class Rectangle:
#     def __init__(self, heigth, width):
#         self.heigth = heigth
#         self.width = width
#     def perimeter_search(self):
#          perim=(self.heigth + self.width)*2
#          print(perim, " Perimeter")
#     def hypotenuse_search(self):
#          hypot=(self.heigth **2  + self.width**2) ** 0.5
#          print(round(hypot, 3), " - Hypotenuse")
#     def square_search(self):
#          square=self.heigth * self.width
#          print(square, " - Square")
#     def paint_rectangle(self):
#         print("PICTURE: ")
#         print(" " +self.width * "-")
#         for i in range(self.heigth):
#             print("|" + self.width * " " + "|")
#         print(" " + self.width * "-")
# 
# r1=Rectangle(7,8)
# # print(r1.__dict__)
# # print(r1.heigth, " + ", r1.width)
# r1.perimeter_search()
# r1.square_search()
# r1.paint_rectangle()
# r1.hypotenuse_search()


# ------------------------------------------------------------------
#           HOME WORK of LESSON 24 (DZ 24)

# class Date:
#     def __init__(self, mass=0):
#         self.mass = mass
#         print(self.mass, "- current mass.")
#     @property
#     def conv(self):
#         print("    Get is working.  ")
#         return self.mass
#     @conv.setter
#     def conv(self, mass):
#         print("    Set is working.  ")
#         print(mass, ' - mass in kg')
#         if type(mass)==int:
#             self.mass = str(mass * 2.204) + " - converted in pounds"
#         else:
#             print("Error input.")
#         return self.mass
#
# p1=Date()
# p1.conv=200
# print(p1.conv)


#
# class Point:
#     def set_x(self, x):
#         print("SET")
#         self.x=x
#         # print(self.x, "This is X.")
#     def get_x(self):
#         print("GET")
#         print(self.x, "- this is X.")
#
# p1=Point()
# p1.set_x(123)
# p1.get_x()

#
#
# class Parent:
#     def __init__(self, x=0,y=0):
#         print("Initialization Parent class.")
#         self.x=x
#         self.y=y
#
# class Children1(Parent):
#     print("Initialization Children class.")
#     def __init__(self,x,y,z):
#         super().__init__(x, y)
#         self.verify_z(z)
#         self.z=z
#
#     @property
#     def zzz(self):
#         return self.z
#
#     @zzz.setter
#     def zzz(self, z):
#         self.verify_z()
#         self.z = z
#
#     @classmethod
#     def verify_z(cls, z):
#             print("---Class method is working.---")
#             if type(z) != int:
#                 print("Z - ERROR!!!")
#                 raise TypeError("Z must be digit.")
# a=Children1(23,45, 67)
# print(a.__dict__)
# print(a.zzz)
# a.z=90
# print(a.__dict__)


# --------------------------------------------------------------

#                          DZ lesson 26

# --------------------------------------------------------------
#
#
# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#     def __str__(self):
#         return f'({self.__x}, {self.__y})'
#     def is_digit(self):
#         if not isinstance(self.__x, (int, float)) or not isinstance(self.__y, (int, float)):
#             print("Координаты должны быть числами")
#             return False
#         return True
#     def is_int(self):
#         if not isinstance(self.__x, int) or not isinstance(self.__y, int):
#             print("Координаты должны быть целочисленными")
#             return False
#         return True
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#     def set_coords(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#
# class Line(Prop):
#     def draw_line(self) -> None:
#         print(f'Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}')
#     def set_coords(self, sp, ep):
#         if sp.is_int() and ep.is_int():
#             self._sp = sp
#             self._ep = ep
#
# class Rect(Prop):
#     def draw_rect(self) -> None:
#         print(f'Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}')
#
# # line только вещественные
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
# line.set_coords(Point(10.2, 20), Point(100, 200))
# line.draw_line()
# print("------------------")
# # rect   и целочисленные и вещественные.
# rect = Rect(Point(7, 9), Point(12, 15))
# rect.draw_rect()
# rect.set_coords(Point(30.5, 40.2), Point(50, 60))
# rect.draw_rect()


# --------------------------------------------------------------

#                          DZ lesson 27

# --------------------------------------------------------------
#
# class Liquid:
#     def __init__(self, name, destiny):
#         self.name = name
#         self.destiny = destiny
#
#     def set_destiny(self, destiny):
#         self.destiny = destiny
#
#     def get_value(self, mass):
#         self.value = mass / self.destiny
#         return f"Value of {self.name}: {self.value:.2f} m^3"
#
#     def get_mass(self, value):
#         self.mass = self.destiny * value
#         print("Mass of", value, "m^3", f" {self.name}: {self.mass:.2f} kg", )
#
#     def info(self):
#         print(f'Name: {self.name},  Destiny: {self.destiny} '
#               f'kg/m^3,  Value: {self.value} m^3, ', end=" ")
#
#
# class Alcohol(Liquid):
#     def __init__(self, name, destiny, concentrate, value):
#         super().__init__(name, destiny)
#         self.concentrate = concentrate
#         self.value = value
#
#     def info(self):
#         super().info()
#         print(f"Alc: {self.concentrate}")
#
#     def set_concentrate(self, concentrate):
#         self.concentrate = concentrate
#
#
# a1 = Alcohol("Wine RED", 1064.2, '12%', 7)
# a1.info()
# a1.set_destiny(1134.7)
# a1.set_concentrate("17%")
# a1.info()
# print(a1.get_value(3000))
# a1.get_mass(2)
# print("*" * 40)
# #
# # a1 = Alcohol("Wine White", 1034.9, '16%', 2)
# # a1.info()
# # print(a1.get_mass(3))


# --------------------------------------------------------------

#                          DZ lesson 28

# --------------------------------------------------------------

# ---------------------------     1    -------------------------
#
# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.comp = self.Computer()
#
#     def info(self):
#         print(f'Student: {self.name} => ', end=' ')
#         print(self.comp.show())
#
#     class Computer:
#         def __init__(self):
#             self.model = "HP"
#             self.processor = "i7+"
#             self.memory = 16
#
#         def show(self):
#             return f'Model: {self.model}, Processor: {self.processor}, ' \
#                    f'Memory: {self.memory}'
#
# s1 = Student("Kelly")
# s2 = Student("Alex")
# s1.info()
# s2.info()


# -----------------------------------------------------------------------------------
#                          DZ lesson 29
#                              ЗАДАЧА №1
#       Елена, решил вторую задачу самостоятельно кроме методов __setitem__. Эти методы посмотрю из ваших лекций
# -----------------------------------------------------------------------------------
#
#
# class Clock:
#     __DAY = 86400
#
#     def __init__(self, sec: int):
#         if not isinstance(sec, int):
#             raise ValueError("Секунды должны быть целым числом")
#
#         self.sec = sec % self.__DAY
#
#     def __add__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом данных Clock")
#         return Clock(self.sec + other.sec)
#
#     def __iadd__(self, other):  # +=
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
#             raise ArithmeticError()
#         return Clock(self.sec * other.sec)
#
#     def __floordiv__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError()
#         return Clock(self.sec // other.sec)
#
#     def __mod__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError()
#         return Clock(self.sec % other.sec)
#
#     def __eq__(self, other):  # ----------------------------- Compare-
#         return self.sec == other.sec
#
#     def __ne__(self, other):
#         return not self.__eq__(other)
#
#     def __gt__(self, other):
#         return self.sec > other.sec  # -------------------------------
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
#     def __getitem__(self, item):
#         if not isinstance(item, str):
#             raise ValueError("Ключ должен быть строкой")
#
#         if item == "hour":
#             return (self.sec // 3600) % 24
#         elif item == "min":
#             return (self.sec // 60) % 60
#         elif item == "sec":
#             return self.sec % 60
#         return "Неверный ключ"
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, str):
#             raise ValueError("Key must be string")
#         if not isinstance(value, int):
#             raise ValueError("KValue must be digit.")
#
#         s = self.sec % 60  # секунды
#         m = (self.sec // 60) % 60  # минуты
#         h = (self.sec // 3600) % 24  # часы
#
#         if key == "hour":
#             self.sec = s + 60 * m + value * 3600
#         if key == "min":
#             self.sec = s + 60 * value + h * 3600
#         if key == "sec":
#             self.sec = value + 60 * m + h * 3600
#
#
# c1 = Clock(80000)
# print(c1.get_format_time())
# print(c1["hour"], c1["min"], c1["sec"])
#
# c1['hour'] = 10
# c1['min'] = 20
# c1['sec'] = 30
# print(c1["hour"], c1["min"], c1["sec"])

# ---------------------------------------------------------------
# # c1 = Clock(200)
# # print(c1.get_format_time())
# # c2 = Clock(200)
# # print(c2.get_format_time())
# # # c1 = c1 + c2
# # # print(c1.get_format_time(), "+")    #   the same with lower
# # # c1+=c2
# # # print(c1.get_format_time(), "+=")
# # c4 = Clock(300)
# # print(c4.get_format_time())
# # c3=c4-c1
# # print(c3.get_format_time(), "-")
# # c3=c4*c2
# # print(c3.get_format_time(), "*")
# # c3=c4//c1
# # print(c3.get_format_time(), "//")
# # c3=c4%c2
# # print(c3.get_format_time(), "%")
# #---------------------------------------------------------------
# # c1 = Clock(100)
# # print(c1.get_format_time())
# # c2 = Clock(50)
# # print(c2.get_format_time())
#
# # if c2<c1:
# #     print("Time second is more than first time.")
#
# # if c1==c2:
# #     print("The same time c1 and c2.")
# # if c1!=c2:
# #     print("Not same time c1 and c2.")
#
# # if c1>c2:
# #     print("c1>c2.")
# # else:
# #     print("Not c1 > c2.")


# --------------------------------------------------------------------------

#                                     ЗАДАЧА №2

# --------------------------------------------------------------------------
#
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

# -----------------------------------------------------------------------------------

#                                       DZ 30

# -----------------------------------------------------------------------------------
#
# class Shape:
#     def __init__(self, color):
#         self.color = color
#
#     def draw1(self):
#         if type(self)==Square:
#             print(f"=={self.name}== \nSize: {self.size} \nColor: {self.color}")
#             print(f'Perimeter = {self.size * 4} ')
#             print(f'Square = {self.size ** 2} ')
#             print()
#             for i in range(self.size):
#                 print("*" * self.size)

#         elif type(self)==Rectangle:
#             print(f"=={self.name}== \nLength: {self.size1} \nWidth: {self.size2} \nColor: {self.color}")
#             print(f'Perimeter = {(self.size1 + self.size2) * 2} ')
#             print(f'Square = {self.size1 * self.size2} ')
#             print()
#             for i in range(self.size1):
#                 print("*" * self.size2)

#         elif type(self)==Triangle:
#             print(f"=={self.name}== \nSize1: {self.size1} \nSize2: {self.size2} "
#                   f"\nSize3: {self.size2}  \nColor: {self.color}")
#             print(f'Perimeter = {self.size1 + self.size2 + self.size3} ')
#
#             self.bottom = self.size2 / 2
#             self.high = (self.size1 ** 2 + self.bottom ** 2) ** (0.5)
#             self.tr_square = self.bottom * self.high
#             print(f'Square of Triangle = {self.tr_square :.{2}f}')
#             print()
#
#             for i in range(1, self.size2 + 1):  # painting of triangle
#                 self.a = " " * (self.size2 - i)
#                 self.b = "*" * (i - 1)
#                 self.c = "*"
#                 self.d = "*" * (i - 1)
#                 print(f'{self.a}{self.b}{self.c}{self.d}')
#
# class Square(Shape):
#     def __init__(self, name, color, size):
#         super().__init__(color)
#         self.size = size
#         self.name = name
#
# class Rectangle(Shape):
#     def __init__(self, name, color, size1, size2):
#         super().__init__(color)
#         self.size1 = size1
#         self.size2 = size2
#         self.name = name
#
# class Triangle(Shape):
#     def __init__(self, name, color, size1, size2, size3):
#         super().__init__(color)
#         self.size1 = size1
#         self.size2 = size2
#         self.size3=size3
#         self.name = name
#
# s = Square("Square", 'Green', 3)
# s.draw1()
# print()
# r = Rectangle("Rectangle", 'Yellow', 3, 7)
# r.draw1()
# print()
# t = Triangle("Triangle", 'Violet', 11, 6, 6)
# t.draw1()


# -----------------------------------------------------------------------------------

#                                       DZ 31

# -----------------------------------------------------------------------------------
#
# class Order:
#     def __set_name__(self, owner, name):
#         self.__name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.__name]
#
#     def __set__(self, instance, value):
#         if  isinstance(value, int) and value < 0:
#             raise ValueError(f"{self.__name} - must be more than zero.")
#         instance.__dict__[self.__name] = value
#
# class Goods:
#     name = Order()
#     price = Order()
#     quantity = Order()
#
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#
# g = Goods("Apple", 12, -6)
# print(g.name)
# print(g.price)
# print(g.quantity)
# # g.name ="Cucumber"
# # print(g.name)
# # g.price = -2
#
# # g2 = Goods("Pear", -12, 6)
# # print(g2.name)
# # print(g2.price)
# # print(g2.quantity)


# ------------------------------------------------------------------------------------------------------------

#                                       DZ 32

# Елена, при первом решении проверку положительного значения вывел в дескрипторе Order, а метод проверки
# существования треугольника по длине сторон в классе Triangle. Они работали только по отдельности.
# Один метод приходилось удалять из кода. Чтоб сразу работало все в дескрипторе ввел три переменных
# и счетчик срабатывающий  на каждом третьем значении


# -------------------------------------------------------------------------------------------------------------
# #
# class Order:
#     count = 0
#     a = 0
#     b = 0
#     c = 0
#
#
#     def __set_name__(self, owner, name):
#         self.__name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.__name]
#
#     def __set__(self, instance, value):
#         if isinstance(value, int) and value < 0:
#             raise ValueError(f" - Size \"{value}\" Must be more than zero.")
#         instance.__dict__[self.__name] = value
#         # print(instance.__dict__)
#         # print(self.__name, "-" ,value, "- NAME")
#
#         Order.count +=1
#         if Order.count == 1:
#             Order.a = value
#         elif Order.count ==2:
#             Order.b = value
#         elif Order.count == 3:
#             Order.c = value
#
#         if ((Order.a + Order.b) < Order.c or (Order.a + Order.c) < Order.b
#             or (Order.c + Order.b) < Order.a) and Order.count == 3:
#             print(f'Triangle with sizes ({Order.a}, {Order.b}, {Order.c}) NOT EXISTS.')
#             Order.count = 0
#             print(instance.__dict__)
#
#         elif Order.count == 3:
#             print(f'Triangle with sizes ({Order.a}, {Order.b}, {Order.c}) EXISTS.')
#             Order.count = 0
#             print(instance.__dict__)
#
# class Triangle:
#     size1 = Order()
#     size2 = Order()
#     size3 = Order()
#
#     def __init__(self, size1, size2, size3):
#         self.size1 = size1
#         self.size2 = size2
#         self.size3 = size3
#
#
# t1 = Triangle(2, 5, 6)
# t2 = Triangle(5, 2, 8)
# t3 = Triangle(7, 3, 6)
# # #
# t4 = Triangle(2, -5, 6)
#

# -------------------------------------------------------------------------------------

#                                       DZ 33

# Елена, не совсем понял условие задачи - через дочерние классы вывел расчетку трех
# типов работников. Ниже код как разбивал по файлам и если вы видите мои файлы то
# все в папке "employee".

# --------------------------------------------------------------------------------------


# ---------------- File #1 (Employee.py)---------------------

#
# from employee import Workers as w
#
# class Employee:
#     def __init__(self, code, name):
#         self.code = code
#         self.name = name
#
#     def show_salary(self):
#         print("-" * 20)
#         print(f"TYPE OF WORKER: {type(self).__name__}.")
#         if type(self) == w.Admin:
#             print(f'Code:{self.code} \nName{ self.name} \nWeek salary: {self.week_salary}\n')
#         if type(self) == w.Worker:
#             print(f'Code:{self.code} \nName {self.name} \nWeek salary: {self.hours * self.pay_hours}\n ')
#         if type(self) == w.Trade:
#             print(f'Code:{self.code} \nName{self.name} \nWeek salary: '
#                 f'{self.week_salary + self.percent * self.overal_marge}')
#
#
# # ---------------- File #2 (Workers.py)---------------------
#
# from employee import Employee as e
#
#
# class Admin(e.Employee):
#     def __init__(self, code, name, week_salary):
#         super().__init__(code, name)
#         self.week_salary = week_salary
#
#
# class Worker(e.Employee):
#     def __init__(self, code, name, hours, pay_hours):
#         super().__init__(code, name)
#         self.hours = hours
#         self.pay_hours = pay_hours
#
#
# class Trade(e.Employee):
#     def __init__(self, code, name, week_salary, percent, overal_marge):
#         super().__init__(code, name)
#         self.week_salary = week_salary
#         self.percent = percent
#         self.overal_marge = overal_marge
#
#
# # ---------------- File #3 (Current_salary.py)---------------------
#
# from employee import Workers as w
#
#
# employee1 = w.Admin(12, "Valery Zadorozny", 1500) # код, имя, недельная зарплата.
# employee1.show_salary()
#
# # w.Admin(12, "Valery Zadorozny", 1500).show_salary() # код, имя, недельная зарплата.
# employee2 = w.Worker(14, "Kelly Moon", 34, 25) # код. имя, количество часов, почасовая ставка
# employee2.show_salary()
# employee3 = w.Trade(17, "George Smith", 1200, 0.04, 10203) # - код. имя. недельный заработок. процент. сумма продаж
# employee3.show_salary()


# -------------------------------------------------------------------------------------------

#                                       DZ 34

# Елена, для ключа в словаре ввел аналогичный прописанному уже ранее в задаче генератор ключа.

# --------------------------------------------------------------------------------------------
#
# import json
# from random import choice
#
# def gen_person():
#     name = ''
#     tel = ''
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
#     nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
#
#     while len(name) != 7:
#         name += choice(letters)
#     while len(tel) != 10:
#         tel += choice(nums)
#
#     person = { 'name': name, 'tel': tel  }
#     return person
#
# def write_json(person_dict):
#
#     dict_key = " "
#     letters = "!@#$%^&*()}{?><{}"
#
#     while len(dict_key) != 10:  # --------generator of dict keys
#         dict_key += choice(letters)
#
#     try:
#         data = json.load(open("persons.json"))
#         print("DATA", data)
#     except FileNotFoundError:
#         data = {}
#
#     data[dict_key] = person_dict
#     print("final_data", data)
#
#     with open('persons.json', 'w') as f:
#         json.dump(data, f, indent=2)
#
# for i in range(5):
#     write_json(gen_person())


# -------------------------------------------------------------------------------------------

#                                       DZ 35

# Eлена, если необходимо есть сразу конфигуратор начальной базы (строка 871 либо можно
# начать с пустой и ввести страны и столицы самостоятельно.

# --------------------------------------------------------------------------------------------
# import json
#
# class Countries:
#
#     def __init__(self, json_name):
#         self.data = {}
#         self.overal_data = json_name
#         try:
#             self.data_temp = json.load(open(self.overal_data))
#             print(f"File:   {self.overal_data} - has been opened.")
#         except FileNotFoundError:
#             self.data_temp = self.data
#             print(f"New file:   {self.overal_data} - has been created.")
#         with open(self.overal_data, "w") as f:
#             json.dump(self.data_temp, f, indent=4)
#
#     # def __str__(self):
#     #     return f'{self.overal_data} - new file'
#
#
#     def add_country(self, country, capital):                # 1  (ADDING)
#         self.writing_into_json(country, capital)
#
#
#     def delete_country(self, key):                          # 2 (DELETING)
#         with open(self.overal_data, 'r') as d:
#             self.deleting_data = json.load(d)
#             if key in self.deleting_data:
#                 print(f"Deleting {key} process")
#                 del self.deleting_data[key]
#                 with open(self.overal_data, "w") as w:
#                     json.dump(self.deleting_data, w, indent=4)
#             else:
#                 print("Incorrect country")
#
#
#     def search_country(self, country):                           # 3 (SEARCHING)
#         if country in self.reading_from_json():
#             print(f'{country} presented in base')
#         else:
#             print(f"{country} not presented in base")
#
#
#     def edit_country(self, country, capital):                # 4 (EDITING)
#         with open(self.overal_data, 'r') as d:
#             self.deleting_data = json.load(d)
#             if country in self.deleting_data:
#                 self.deleting_data[country] = capital
#                 with open(self.overal_data, "w") as w:
#                     json.dump(self.deleting_data, w, indent=4)
#             else:
#                 print("Incorrect inputs")
#
#
#     def show_info(self):                                     # 5 (SHOW_INFO)
#         print("Countries and Capitals: ")
#         print("----------------------")
#         for i in self.reading_from_json():
#             print(i, " - ", self.reading_from_json()[i])
#
#
#     def reading_from_json(self):
#         with open(self.overal_data, 'r') as r:
#             self.json_string = json.load(r)
#             return self.json_string
#
#
#     def writing_into_json(self, country, capital):
#         try:
#             self.data_temp = json.load(open(self.overal_data))
#         except FileNotFoundError:
#             self.data_temp = {}
#         self.data_temp[country] = capital
#         with open(self.overal_data, "w") as f:
#             json.dump(self.data_temp, f, indent=4)
#             print("File saved.")
#
#
# country = Countries("Countries_new.json")  # -----Configuration of first database if necessary.
# # country.add_country("Spain", "Madrid")
# # country.add_country("France", "Paris")
# # country.add_country("Australia", "Sydney")
#
# # print(country)
#
#
# print("Press: \n1 for adding \n2 for deleting\n3 for "
#       "searching\n4 for editing\n5 for show\n6 for exit.")
#
# operation = 1
# while operation in range(1,1000):
#     print("-" * 40)
#
#     operation = int(input("Input your operation: "))
#     if operation not in [1, 2, 3, 4, 5, 6]:
#         print("Incorrect input. Must be from 1 till 6.")
#     elif operation == 1:
#         a = input('Input new country: ').strip()
#         b = input('Input new capitol: ').strip()
#         country.add_country(a, b)
#     elif operation == 2:
#         a = input("Input country for deleting: ").strip()
#         country.delete_country(a)
#     elif operation == 3:
#         a = input("Input country for searching: ").strip()
#         country.search_country(a)
#     elif operation == 4:
#         a = input('Input country for edit: ').strip()
#         b = input('Input capitol for edit: ').strip()
#         country.edit_country(a, b)
#     elif operation == 5:
#         print()
#         country.show_info()
#         print()
#     elif operation == 6 :
#         print("Stop operation.")
#         break


# ---------------------------------------------------------------------------------------------------

#                                       DZ 36

# ---------------------------------------------------------------------------------------------------
# import csv
#
#
# with open('data3.csv') as f:
#     a=csv.reader(f, delimiter=";")
#     for i in a:
#         print(i)




# ----------------------------------------------------------------------------------------------------

#                                       DZ 37

# Елена, так как сразу через find_all в переменной saxophones не мог выделить ссылку href из тега "а"
# (не смог понять почему - делал как в примере на лекции, но выдавало None) решил через
# вложенный второй цикл.

# -----------------------------------------------------------------------------------------------------
#
# import requests
# from bs4 import BeautifulSoup
# import lxml
# import csv
#
# url ="https://shop-avallon.ru/catalog/wind-instruments/saksofony/" \
#      "?utm_source=none&utm_medium=cpc&utm_campaign=74234833&utm_content=premium.2&utm_term=" \
#      "---autotargeting&_openstat=ZGlyZWN0LnlhbmRleC5ydTs3NDIzNDgzMzsxMjc3MTY4MDQwMDt5YW5kZXgucnU6c" \
#      "HJlbWl1bQ&yclid=11910330624978452479"
#
# # url ="https://shop-avallon.ru/catalog/wind-instruments/saksofony/"
#
# r = requests.get(url)
# r.encoding = 'utf - 8'
# soup = BeautifulSoup(r.text, "lxml")
#
# def write_csv(data):
#     with open('Saxophones.csv', 'a') as f:
#         writer = csv.writer(f, lineterminator = '\n', delimiter=';')
#         writer.writerow((data['name'], data['url']))
#
# saxophones=soup.find_all('div', class_='tpl-block-list-objects tpl-block-492-list')
#
# for i in saxophones:
#     name= i.find_all('a', class_= "main__hits-card-title")
#     for j in name:
#         text = j.text
#         print(text)
#         url = j['href']
#         print("URL :", url)
#
#         data = {'name': text, 'url': url}
#         write_csv(data)
#

#--------------------------------------------------------------------------------

#                                       DZ 38

# Елена, вы уже решили - код с вашим решением.
#--------------------------------------------------------------------------------

# import json
#
# data = {"Россия": "Москва"}
#
#
# def load_data(func):
#     def wrap(*args, filename):
#         try:
#             data = json.load(open(filename))
#         except FileNotFoundError:
#             data = {}
#         func(*args, filename)
#         print("Файл сохранен")
#     return wrap
#
#
# class CountryCapital:
#     def __init__(self, country, capital):
#         self.country = country
#         self.capital = capital
#         data[self.country] = self.capital
#
#     def __str__(self):
#         return f'{self.country}: {self.capital}'
#
#     @classmethod
#     @load_data
#     def add_country(cls, new_country, new_capital, filename):
#
#         data[new_country] = new_capital
#
#         with open(filename, "w") as f:
#             json.dump(data, f, indent=2, ensure_ascii=False)
#
#     @classmethod
#     @load_data
#     def delete_country(cls, del_country, filename):
#         if del_country in data:
#             del data[del_country]
#
#             with open(filename, "w") as f:
#                 json.dump(data, f, indent=2, ensure_ascii=False)
#         else:
#             print("Такой страны в базе нет")
#
#     @classmethod
#     @load_data
#     def search_data(cls, country, filename):
#         if country in data:
#             print(f"Страна {country} столица {data[country]} есть в словаре!")
#         else:
#             print(f"Страна {country} отсутствует в словаре")
#
#     @classmethod
#     @load_data
#     def change_capital(cls, country, new_value, filename):
#
#         if country in data:
#             data[country] = new_value
#
#             with open(filename, "w") as f:
#                 json.dump(data, f, indent=2, ensure_ascii=False)
#         else:
#             print("Такой страны в базе нет")
#
#     @classmethod
#     def load_from_file(cls, filename):
#         with open(filename, 'r') as f:
#             print(json.load(f))
#
#
# index = ''
# filename1 = 'list_capital.json'
# with open(filename1, "w") as fw:
#     json.dump(data, fw, indent=2, ensure_ascii=False)
#
# while index != 6:
#     try:
#         print("*" * 40)
#         index = int(input('Выбор действия:\n1 - добавление данных\n2 - удаление данных\n'
#                           '3 - поиск данных\n4 - редактирование данных\n5 - просмотр данных\n'
#                           '6 - завершение работы\nВвод: '))
#         if index == 1:
#             country_name = input("Введите название страны (с заглавной буквы): ")
#             capital_name = input("Введите название столицы страны (с заглавной буквы): ")
#             CountryCapital.add_country(country_name, capital_name, filename='list_capital.json')
#         if index == 2:
#             country_name = input("Введите страну для удаления (с заглавной буквы): ")
#             CountryCapital.delete_country(country_name, filename='list_capital.json')
#         if index == 3:
#             country_name = input("Введите название страны (с заглавной буквы): ")
#             CountryCapital.search_data(country_name, filename='list_capital.json')
#         if index == 4:
#             country_name = input("Введите название страны столицу которой хотите изменить (с заглавной буквы): ")
#             new_capital = input("Введите новое название столицы: ")
#             CountryCapital.change_capital(country_name, new_capital, filename='list_capital.json')
#         if index == 5:
#             CountryCapital.load_from_file(filename='list_capital.json')
#     except IndexError:
#         break





