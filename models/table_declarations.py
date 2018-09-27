from sqlalchemy import Table, Column, Integer, String, ForeignKey, TIMESTAMP

from models.base import metadata

site = Table(
    'sites', metadata,
    Column('id', Integer, primary_key=True),
    Column('domain', String, nullable=False)
)

url = Table(
    'urls', metadata,
    Column('id', Integer, primary_key=True),
    Column('link', String),
    Column('site_id', ForeignKey('sites.id'))
)

product = Table(
    'products', metadata,
    Column('id', Integer, primary_key=True),
    Column('url_id', ForeignKey('urls.id')),
    Column('name', String),
    Column('title', String)
)

url_status = Table(
    'url_status', metadata,
    Column('id', Integer, primary_key=True),
    Column('status', String, default='TO_DO'),
    Column('url_id', ForeignKey('urls.id')),
    Column('visited_at', TIMESTAMP),
)

__all__ = ['site', 'url', 'product', 'url_status']
