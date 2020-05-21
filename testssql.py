import mysql.connector

db = mysql.connector.connect(
    user='root',
    password="",
    host="localhost",
    passwd="",
    database="Test",
    auth_plugin='mysql_native_password'
    )

mycursor = db.cursor()

mycursor.execute("CREATE DATABASE testdatabase")
