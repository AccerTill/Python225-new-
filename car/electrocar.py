from car import carclass


class ElectroCar(carclass.CarClass):
    def __init__(self, brand, model, year, probeg):
        super().__init__(brand, model, year, probeg)
        self.battery = 100

    def description_battery(self):
        print(f"This car has power {self.battery} %")
        return "^&*"

if __name__=="__main__":
    e_car = ElectroCar("Tesla", "TT", 2022, 93340)
    e_car.show_car()
    e_car.description_battery()




