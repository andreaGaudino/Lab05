import mysql.connector
from mysql.connector import errorcode


def get_connection() -> mysql.connector.connection:
    try:
        #cnx = mysql.connector.connect(option_files='./database/connector.cnf')
        cnx = mysql.connector.connect(user='root', password='password', host='127.0.0.1', database='iscritticorsi')
        return cnx
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
            return None
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
            return None
        else:
            print(err)
            return None


class DBConnect:
    pass
