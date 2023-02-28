from employee import Workers as w

employee1 = w.Admin(12, "Valery Zadorozny", 1500)
employee1.show_salary()

employee2 = w.Worker(14, "Kelly Moon", 34, 25)
employee2.show_salary()

employee3 = w.Trade(17, "George Smith", 1200, 0.04, 10203)
employee3.show_salary()