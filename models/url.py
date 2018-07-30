from sqlalchemy import Column, Integer, String, ForeignKey

from models.base import Base


class Url(Base):
    __tablename__ = 'urls'

    id = Column(Integer, primary_key=True)
    link = Column(String)
    site_id = Column(ForeignKey('sites.id'))
