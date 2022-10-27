# class Point:      #-----------------------------------------------------------------Point
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f'({self.__x}, {self.__y})'
#
#     def is_digit(self):
#         if not isinstance(self.__x, (int, float)) or not isinstance(self.__y, (int, float)):
#             print("Координаты должны быть числами")
#             return False
#         return True
#
#     def is_int(self):
#         if not isinstance(self.__x, int) or not isinstance(self.__y, int):
#             print("Координаты должны быть целочисленными")
#             return False
#         return True
#
# class Prop:       #-------------------------------------------------------------------Prop
#     def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1):
#         print("Инициализатор базового класса Prop")
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self.__width = width
#
#     def get_width(self):
#         return self.__width
#
# class Line(Prop):     #--------------------------------------------------------------LINE
#     def __init__(self, *args):
#         print('Переопределенный инициализатор Line')
#         super().__init__(*args)     #-----------------------------------------------SUPER
#         self.__width = 5
#
#     def draw_line(self) -> None:
#         print(f'Рисование линии: {self._sp}, {self._ep}, {self._color}, {self.__width}')
#
# class Rect(Prop):#--------------------------------------------------------------RECT
#     def __init__(self, sp, ep, color='red', width=1, bg='yellow'):
#         super().__init__(sp, ep, color, width)
#         self.background = bg
#
#     def draw_rect(self) -> None:
#         print(f'Рисование прямоугольника: {self._sp}, {self._ep}, '
#               f'{self._color}, {self.get_width()}, {self.background}')
#
# line = Line(Point(1, 2), Point(10, 20), 'green', 3)
# line.draw_line()
# print(line.__dict__)
# # print(line._width)
# # print(type(line))
# rect = Rect(Point(30, 40), Point(70, 80))
# rect.draw_rect()
#
# # print(issubclass(Point, object))
# # print(line.__dict__)



# -----------------------------------------


#------------------------POINT---------------
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
        print('работает проверка для LINE на целочисленность.')
        if not isinstance(self.__x, int) or not isinstance(self.__y, int):
            print("Координаты должны быть целочисленными")
            return False
        return True
#--------------------------PROP--------------
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
#-----------------------LINE-----------------
class Line(Prop):
    def draw_line(self) -> None:
        print(f'Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}')

    def set_coords(self, sp, ep):
        if sp.is_int() and ep.is_int():
            self._sp = sp
            self._ep = ep
#------------------------RECT----------------
class Rect(Prop):
    def draw_rect(self) -> None:
        print(f'Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}')

#--------SOLUTION------
           # только целочисленные значения
line = Line(Point(1.67, 789), Point(10, 20))
# line.draw_line()
line.set_coords(Point(10, 20), Point(100, 200))
line.draw_line()

          # как целочисленные так и вещественные
# rect = Rect(Point(7, 9), Point(12, 15))
# rect.draw_rect()
# rect.set_coords(Point(30.5, 40.2), Point(50, 60))
# rect.draw_rect()




















