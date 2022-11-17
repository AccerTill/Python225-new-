class Rectangle:
    def __init__(self, l, h):
        self.l = l
        self.h = h

    def get_rect_perimeter(self):
        res = self.l * 2 + self.h * 2
 #       print(f'Perimeter of Rectangle: {res}')
        return res

    def get_rect_area(self):
        res = self.l * self.h
  #      print(f'Square of Rectangle: {res}')
        return res

    def print_rect(self):
#        print(f"Sides: {self.l}, {self.h}")
        return {self.l, self.h}


# print(__name__)
