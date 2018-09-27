from sqlalchemy import create_engine

from conf import PG_USER, PG_PASSWD, PG_HOST, PG_DBNAME
from models.base import metadata

engine = create_engine(
    f'postgresql://{PG_USER}:{PG_PASSWD}@{PG_HOST}/{PG_DBNAME}'
)

metadata.create_all(engine)
print('ok')
