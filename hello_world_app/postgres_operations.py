import os

import sqlalchemy


DB_HOST = os.environ["DB_HOST"]
DB_PORT = os.environ["DB_PORT"]
DB_NAME = os.environ["DB_NAME"]
DB_USER = os.environ["DB_USER"]
DB_PASS = os.environ["DB_PASS"]


class PostgresClient:
    def __init__(self):
        self.db_host = DB_HOST
        self.db_port = DB_PORT
        self.db_name = DB_NAME
        self.db_user = DB_USER
        self.db_pass = DB_PASS
        self.engine = self.create_engine()

    def create_engine(self):
        engine = sqlalchemy.create_engine(
            sqlalchemy.engine.url.URL(
                drivername="postgresql+psycopg2",
                username=self.db_user,
                password=self.db_pass,
                host=self.db_host,
                port=self.db_port,
                database=self.db_name,
            ),
        )
        return engine

    def list_data(self):
        rows_count = 0
        with self.engine.connect() as conn:
            result = conn.execute("SELECT * FROM hello")
            for row in result:
                rows_count += 1
                print(dict(row))
        return rows_count

    def write_data(self, sentence):
        with self.engine.connect() as conn:
            result = conn.execute(f"INSERT INTO hello (sentence) VALUES ('{sentence}')")
