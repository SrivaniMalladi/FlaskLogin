# to create a table named employee

import sqlite3
from flask import Flask

app = Flask(__name__)


database = 'empform.db'
def init_db():

    db = sqlite3.connect(database)

    db.execute('''CREATE TABLE IF NOT EXISTS empform(
                        empid integer PRIMARY KEY AUTOINCREMENT,
                        empname text NOT NULL,
                        desig text,
                        depart text,
                        sal integer);''')

    print('database table created successfully')

    db.commit()
    db.close()


if __name__ == '__main__':
    init_db()