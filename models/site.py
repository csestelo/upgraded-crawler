from sqlalchemy import Column, String, Integer

from models.base import Base


class Site(Base):
    __tablename__ = 'sites'

    id = Column(Integer, primary_key=True)
    domain = Column(String)
