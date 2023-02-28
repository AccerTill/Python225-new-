from shapes import rectangle, circle

class Cylinder(rectangle.Rectangle, circle.Circle):
    def __init__(self, r, h):
        circle.Circle.__init__(self, r)
        rectangle.Rectangle.__init__(self, self.get_circle_circumference(), h)

    def get_volume(self):
        res = self.get_circle_area() * self.h
        # print(f"Volume: {res}")
        return res

    def print_cylinder(self):
        print(f"Radius of bottom: {self.r}, High: {self.h}")

# if __name__ == '__main__':
