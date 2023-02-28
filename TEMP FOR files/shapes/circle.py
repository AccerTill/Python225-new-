from math import pi

class Circle:
    def __init__(self, r):
        self.r = r

    def get_circle_circumference(self):
        res = 2 * pi * self.r
        # print(f'Perimeter of Circle: {round(res, 2)}', "***")
        return res

    def get_circle_area(self):
        res = pi * self.r ** 2
        # print(f'Square of Circle: {res}')
        return res

# print(__name__)
