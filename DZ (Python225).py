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



#------------------------------------------------------------------
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


class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    def __str__(self):
        return f'({self.__x}, {self.__y})'
    def is_digit(self):
        if not isinstance(self.__x, (int, float)) or not isinstance(self.__y, (int, float)):
            print("Координаты должны быть числами")
            return False
        return True
    def is_int(self):
        if not isinstance(self.__x, int) or not isinstance(self.__y, int):
            print("Координаты должны быть целочисленными")
            return False
        return True

class Prop:
    def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1):
        self._sp = sp
        self._ep = ep
        self._color = color
        self._width = width
    def set_coords(self, sp, ep):
        if sp.is_digit() and ep.is_digit():
            self._sp = sp
            self._ep = ep

class Line(Prop):
    def draw_line(self) -> None:
        print(f'Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}')
    def set_coords(self, sp, ep):
        if sp.is_int() and ep.is_int():
            self._sp = sp
            self._ep = ep

class Rect(Prop):
    def draw_rect(self) -> None:
        print(f'Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}')

# line только вещественные

line = Line(Point(1, 2), Point(10, 20))
line.draw_line()
line.set_coords(Point(10.2, 20), Point(100, 200))
line.draw_line()
print("------------------")
# rect   и целочисленные и вещественные.
rect = Rect(Point(7, 9), Point(12, 15))
rect.draw_rect()
rect.set_coords(Point(30.5, 40.2), Point(50, 60))
rect.draw_rect()





















