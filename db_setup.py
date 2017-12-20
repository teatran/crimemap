import pymysql
import dbconfig

connection = pymysql.connect(host="localhost",
                             user=dbconfig.db_user,
                             passwd=dbconfig.db_password)
try:
    with connection.cursor() as cursor:
        # create database
        sql = "CREATE DATABASE IF NOT EXISTS crimemap"
        cursor.execute(sql)
        # create table
        sql = """CREATE TABLE IF NOT EXISTS crimemap.crimes (
        id int NOT NULL AUTO_INCREMENT,
        latitude FLOAT(10, 6),
        longitude FLOAT(10, 6),
        date DATETIME,
        category VARCHAR(50),
        description VARCHAR(100),
        updated_at TIMESTAMP,
        PRIMARY KEY (id)
        )"""
        cursor.execute(sql)
    connection.commit()
finally:
    connection.close()
