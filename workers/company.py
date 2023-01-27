# group

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from workers.database import Base     # +++


class Company(Base):        # +++
    __tablename__ = 'companies'  # +++

    id = Column(Integer, primary_key=True)
    company_name = Column(String(250), nullable=False) # +++
    worker = relationship('Workers')

    def __repr__(self):
        return f"Компания (ID: {self.id}, Название: {self.company_name})" # +++