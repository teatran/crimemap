import pymysql
import dbconfig


class DBHelper:

    def connect(self, database='crimemap'):
        return pymysql.connect(host="localhost",
                               user=dbconfig.db_user,
                               passwd=dbconfig.db_password,
                               db=database)

    def select_all(self):
        connection = self.connect()
        try:
            query = "SELECT description FROM crimes"
            with connection.cursor() as cursor:
                cursor.execute(query)
            return cursor.fetchall()
        finally:
            connection.close()

    def insert(self, des):
        connection = self.connect()
        try:
            query = ("INSERT INTO crimes (description) VALUES" +
                     "('{}');".format(des))
            with connection.cursor() as cursor:
                cursor.execute(query)
                connection.commit()
        finally:
            connection.close()
            
    def delete_all(self):
        connection = self.connect()
        try:
            query = "DELETE FROM crimes;"
            with connection.cursor() as cursor:
                cursor.execute(query)
                connection.commit()
        finally:
            connection.close()
                
