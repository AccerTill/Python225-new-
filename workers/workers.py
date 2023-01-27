# students

from sqlalchemy import Column, ForeignKey, Integer, String

from workers.database import Base # +++

class Workers(Base):     #   +++
    __tablename__='workers'

    id = Column(Integer, primary_key = True)
    surname = Column(String(250), nullable = False) # обязательно для заполнения - (nullable = False)
    name = Column(String(250), nullable=False)
    patronymic = Column(String(250), nullable=False)
    age = Column(Integer)
    company = Column(Integer, ForeignKey('company.id'))    #  +++ !!!!!!!!!!!

    def __init__(self, full_name, age, id_company): # +++
        self.surname = full_name[0]
        self.name = full_name[1]
        self.patronymic=full_name[2]
        self.age = age
        self.company = id_company

    def __repr__(self):
        return f"Работник (ФИО: {self.surname} {self.name} {self.patronymic}, Возраст: {self.age}, ID компании:" \
               f"{self.company})"
