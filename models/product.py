from sqlalchemy import Column, String, Integer, ForeignKey

from models.base import Base


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    url_id = Column(ForeignKey('urls.id'))
    name = Column(String)
    title = Column(String)
