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

class Shape:
    def __init__(self, color):
        self.color = color

    def draw1(self):
        if type(self)==Square:
            print(f"=={self.name}== \nSize: {self.size} \nColor: {self.color}")
            print(f'Perimeter = {self.size * 4} ')
            print(f'Square = {self.size ** 2} ')
            print()
            for i in range(self.size):
                print("*" * self.size)
        elif type(self)==Rectangle:
            print(f"=={self.name}== \nLength: {self.size1} \nWidth: {self.size2} \nColor: {self.color}")
            print(f'Perimeter = {(self.size1 + self.size2) * 2} ')
            print(f'Square = {self.size1 * self.size2} ')
            print()
            for i in range(self.size1):
                print("*" * self.size2)
        elif type(self)==Triangle:
            print(f"=={self.name}== \nSize1: {self.size1} \nSize2: {self.size2} "
                  f"\nSize3: {self.size2}  \nColor: {self.color}")
            print(f'Perimeter = {self.size1 + self.size2 + self.size3} ')

            self.bottom = self.size2 / 2
            self.high = (self.size1 ** 2 + self.bottom ** 2) ** (0.5)
            self.tr_square = self.bottom * self.high
            print(f'Square of Triangle = {self.tr_square :.{2}f}')
            print()

            for i in range(1, self.size2 + 1):  # painting of triangle
                self.a = " " * (self.size2 - i)
                self.b = "*" * (i - 1)
                self.c = "*"
                self.d = "*" * (i - 1)
                print(f'{self.a}{self.b}{self.c}{self.d}')


class Square(Shape):
    def __init__(self, name, color, size):
        super().__init__(color)
        self.size = size
        self.name = name

class Rectangle(Shape):
    def __init__(self, name, color, size1, size2):
        super().__init__(color)
        self.size1 = size1
        self.size2 = size2
        self.name = name

class Triangle(Shape):
    def __init__(self, name, color, size1, size2, size3):
        super().__init__(color)
        self.size1 = size1
        self.size2 = size2
        self.size3=size3
        self.name = name


s = Square("Square", 'Green', 3)
s.draw1()
print()
r = Rectangle("Rectangle", 'Yellow', 3, 7)
r.draw1()
print()
t = Triangle("Triangle", 'Violet', 11, 6, 6)
t.draw1()


