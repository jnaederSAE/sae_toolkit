import pymssql
import os
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.environ.get('DB_HOST')
DB_USER = os.environ.get('DB_USER')
DB_PW = os.environ.get('DB_PW')
DB_NAME = os.environ.get('DB_NAME')


class Database:

    def __init__(self,
                 host=DB_HOST,
                 user=DB_USER,
                 pw=DB_PW,
                 db=DB_NAME):
        self.cur = None
        self.host = host
        self.user = user
        self.pw = pw
        self.db = db

        self.conn = pymssql.connect(host=self.host,
                                    user=self.user,
                                    password=self.pw,
                                    database=self.db)

    def connectDatabase(self):
        self.cur = self.conn.cursor(as_dict=True)

    def executeQuery(self, statement):
        self.connectDatabase()
        self.cur.execute(statement)
        return list(self.cur.fetchall())
