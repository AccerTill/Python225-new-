from employee import Workers as w

class Employee:
    def __init__(self, code, name):
        self.code = code
        self.name = name

    def show_salary(self):
        print("-" * 20)
        print(f"TYPE OF WORKER: {type(self).__name__}.")
        if type(self) == w.Admin:
            print(f'Code:{self.code} \nName{self.name} \nWeek salary: {self.week_salary}\n')
        if type(self) == w.Worker:
            print(f'Code:{self.code} \nName{self.name} \nWeek salary: {self.hours * self.pay_hours}\n ')
        if type(self) == w.Trade:
            print(
                f'Code:{self.code} \nName{self.name} \nWeek salary: '
                f'{self.week_salary + self.percent * self.overal_marge}')