class Order:
    count = 0
    a = 0
    b = 0
    c = 0


    def __set_name__(self, owner, name):
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        if isinstance(value, int) and value < 0:
            raise ValueError(f" - Size \"{value}\" Must be more than zero.")
        instance.__dict__[self.__name] = value
        # print(instance.__dict__)
        # print(self.__name, "-" ,value, "- NAME")

        Order.count +=1
        if Order.count == 1:
            Order.a = value
        elif Order.count ==2:
            Order.b = value
        elif Order.count == 3:
            Order.c = value

        if ((Order.a + Order.b) < Order.c or (Order.a + Order.c) < Order.b
            or (Order.c + Order.b) < Order.a) and Order.count == 3:
            print(f'Triangle with sizes ({Order.a}, {Order.b}, {Order.c}) NOT EXISTS.')
            Order.count = 0
            print(instance.__dict__)

        elif Order.count == 3:
            print(f'Triangle with sizes ({Order.a}, {Order.b}, {Order.c}) EXISTS.')
            Order.count = 0
            print(instance.__dict__)

class Triangle:
    size1 = Order()
    size2 = Order()
    size3 = Order()

    def __init__(self, size1, size2, size3):
        self.size1 = size1
        self.size2 = size2
        self.size3 = size3


t1 = Triangle(2, 5, 6)
t2 = Triangle(5, 2, 8)
t3 = Triangle(7, 3, 6)
# #
t4 = Triangle(2, -5, 6)