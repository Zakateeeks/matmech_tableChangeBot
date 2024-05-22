import configparser

import psycopg2

config = configparser.ConfigParser()
config.read('../data.ini')
password = config["DB"]["PASS"]

conn = psycopg2.connect(dbname='students', user='user',
                        password=password, host='localhost')
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXIST students (
        urfuID INT,
        name TEXT,
        priority TEXT,
        speciality TEXT,
        institutes TEXT,
        budget TEXT,
        points INT,
        comment TEXT
    )
""")

conn.commit()
