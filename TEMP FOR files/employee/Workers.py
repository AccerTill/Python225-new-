from employee import Employee as e

class Admin(e.Employee):
    def __init__(self, code, name, week_salary):
        super().__init__(code, name)
        self.week_salary = week_salary


class Worker(e.Employee):
    def __init__(self, code, name, hours, pay_hours):
        super().__init__(code, name)
        self.hours = hours
        self.pay_hours = pay_hours


class Trade(e.Employee):
    def __init__(self, code, name, week_salary, percent, overal_marge):
        super().__init__(code, name)
        self.week_salary = week_salary
        self.percent = percent
        self.overal_marge = overal_marge
