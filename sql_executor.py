import mysql.connector

usr_pwd = input("Please enter password : ")

cnx = mysql.connector.connect(
    user='root',
    password=usr_pwd,
    host="localhost",
    database="Project5_db",
    auth_plugin='mysql_native_password'
    )

mycursor = cnx.cursor()


def database_creation(cursor):

    with open('db_creation_script.sql') as sql:
        db_creation = sql.read()

    cursor.execute(db_creation, multi=True)
