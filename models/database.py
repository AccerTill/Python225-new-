# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base  # для определения таблицы и модели
# from sqlalchemy.orm import sessionmaker
#
# DATABASE_NAME = 'students.db'
#
# # Настройки для создания базы данных:
#
# engine = create_engine(f'sqllite:///{DATABASE_NAME}')
#
# Session = sessionmaker  (bind = engine)       #  большой буквы - промежуточная зона для всех объектов
#
# Base = declarative_base() # возвращает новый базовый класс который наследует все связанные классы
#
# def create_db():
#     Base.metadata.create_all(engine) # функция даст возможность добавить классы в виде таблиц БД.
#                                      # Повторно не создаютсяя


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_NAME = 'students.db'

engine = create_engine(f'sqlite:///{DATABASE_NAME}')
Session = sessionmaker(bind=engine)

Base = declarative_base()


def create_db():
    Base.metadata.create_all(engine)










