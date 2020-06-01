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
        self.product_choice = 0  # Id of product
        self.choice_mage = False


class System:

    def __init__(self):
        self.current_page = 0
        self.total_pages = 0
        self.keep_printing = True


display_limit = 10
userA = User()
category_sys = System()
product_sys = System()


def CategorySelection(cursor):
    mycursor.execute("SELECT Translated_name, Category_id FROM Category_table")
    result = mycursor.fetchall()

    chunk_index = 0

    sublist_categories = [result[x:x+10] for x in range(0, len(result), 10)]

    for chunk in sublist_categories:

        for sublist in sublist_categories[chunk_index]:

            print(sublist)

        userA.category_choice = input("Select Category Via its ID : ")
        print('end of list')
        chunk_index += 1


def ProductDisplay(cursor):
    mycursor.execute(f"SELECT * FROM Product_table WHERE Category_id = {userA.category_choice}")
    result = mycursor.fetchall()
    number_identifier = 1
    for row in result:
        print(row[1], number_identifier)
        number_identifier += 1


CategorySelection(mycursor)
ProductDisplay(mycursor)
