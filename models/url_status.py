from sqlalchemy import Column, String, TIMESTAMP, Integer, ForeignKey

from models.base import Base


class UrlStatus(Base):
    __tablename__ = 'url_status'

    id = Column(Integer, primary_key=True)
    status = Column(String, default='TO_DO')
    url_id = Column(ForeignKey('urls.id'))
    visited_at = Column(TIMESTAMP)
