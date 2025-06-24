SECRET_KEY = 'JCEMLVUQHFBUlBWR5okLDZj4FxAE4Ayfh9b5GT4tTd4'

scheme = 'postgresql+psycopg2'
username = 'postgres'
password = 'skmSKM01'
host_name = 'localhost'
port = '5432'
database_name = 'de-codees'

URL_DB = f"{scheme}://{username}:{password}@{host_name}:{port}/{database_name}"

SQLALCHEMY_DATABASE_URI = URL_DB