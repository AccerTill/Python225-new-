#lessons

from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from workers.database import Base # +++

association_table = Table('association', Base.metadata,  # +++
                          Column('profession_id', Integer, ForeignKey('profession .id')),
                          Column('company_id', Integer, ForeignKey('company.id')))


class Profession(Base): # +++
    __tablename__ = 'professions' # +++

    id = Column(Integer, primary_key=True)
    profession_title = Column(String(250), nullable=False)
    companies = relationship("Company", secondary=association_table, backref='company_profession')

    def __repr__(self):
        return f"Профессия (ID: {self.id}, Название: {self.profession_title})"
