import mysql.connector

cnx = mysql.connector.connect(
    user='root',
    password="06022018",
    host="localhost",
    passwd="06022018",
    database="Project5_db",
    auth_plugin='mysql_native_password'
    )

mycursor = cnx.cursor()


class User:

    def __init__(self):
        self.category_choice = 0


userA = User()


def CategorySelection(cursor):
    mycursor.execute("SELECT Translated_name, Category_id FROM Category_table")
    result = mycursor.fetchall()
    for row in result:
        print(row)
    userA.category_choice = input("Select Category Via its ID : ")


def ProductDisplay(cursor):
    mycursor.execute(f"SELECT * FROM Product_table WHERE Category_id = {userA.category_choice}")
    result = mycursor.fetchall()
    for row in result:
        print(row)


CategorySelection(mycursor)
ProductDisplay(mycursor)
