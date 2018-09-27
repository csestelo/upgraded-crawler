from os import environ

PG_DBNAME = environ.get('PG_DBNAME', 'upgraded-crawler')
PG_USER = environ.get('PG_USER', 'upgraded-crawler')
PG_PASSWD = environ.get('PG_PASSWD', 'root')
PG_HOST = environ.get('PG_HOST', '127.0.0.1')
