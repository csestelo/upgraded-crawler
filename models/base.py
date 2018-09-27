import asyncio

from aiopg import create_pool
from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base

from conf import PG_DBNAME, PG_USER, PG_PASSWD, PG_HOST

metadata = MetaData()
Base = declarative_base(metadata=metadata)

dsn = f'dbname={PG_DBNAME} user={PG_USER} password={PG_PASSWD} host={PG_HOST}'


async def init_pg():
    return await create_pool(dsn)

pool = asyncio.get_event_loop().run_until_complete(init_pg())


__all__ = ['pool', 'metadata', 'Base']
