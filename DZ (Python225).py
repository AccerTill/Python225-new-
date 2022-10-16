# ------------------------------DZ 22

# class Book:
#     name = "name of book"
#     year = "0000"
#     producer = "producer"
#     genre = "genre"
#     writer = "writer"
#     price = "00"
#
#     def print_info(self):
#         print(" Personal info. ".center(40, "*"))
#         print(f"name: {self.name}\nyear: {self.year}\n"
#             f"producer:{self.producer}\ngenre: {self.genre}\n"
#             f"writer: {self.writer}\nprice: {self.price}")
#         print("-" * 40)
#
#     def input_info(self, name, year, producer, genre,
#                writer, price):
#         self.name = name
#         self.year = year
#         self.producer = producer
#         self.genre =genre
#         self.writer = writer
#         self.price = price
#
#     def set_name(self, name):
#         self.name = name
#
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
# print(f1)

# class Person:
#     name = "Name"

#
# ----------------------------------------------------------------

class Rectangle:
    def __init__(self, heigth, width):
        self.heigth = heigth
        self.width = width

    def perimeter_search(self):
         perim=(self.heigth + self.width)*2
         print(perim, " Perimeter")
    def hypotenuse_search(self):
         perim=(self.heigth **2  + self.width**2) ** 0.5
         print(perim, " - Hypotenuse")

    def square_search(self):
         square=self.heigth * self.width
         print(square, " - Square")
    def paint_rectangle(self):
        print("PICTURE: ")
        print(" " +self.width * "-")
        for i in range(self.heigth):
            print("|" + self.width * " " + "|")
        print(" " + self.width * "-")


r1=Rectangle(3,5)
print(r1.__dict__)
print(r1.heigth, r1.width)
r1.perimeter_search()
r1.square_search()
r1.paint_rectangle()
r1.hypotenuse_search()
















