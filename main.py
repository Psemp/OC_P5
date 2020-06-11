import mysql.connector
import time
# from sql_executor import database_creation
from data_insertion import Insert_data
from display_queries import CategorySelection, ProductSelection
from display_queries import ResultSelection, SavedInsertion, ViewHistory


class User:

    def __init__(self):
        self.category_choice = 0
        self.category_id = 0
        self.product_choice = 0
        self.id_of_selection = 0
        self.id_of_substitute = 0
        self.products_seen = 0
        self.categories_seen = 0


displayed_categories = []
displayed_products = []
display_limit = 10
userA = User()

usr_pwd = input("Please enter password : ")

cnx = mysql.connector.connect(
    user='root',
    password=usr_pwd,
    host="localhost",
    passwd=usr_pwd,
    database="Project5_db",
    auth_plugin='mysql_native_password'
    )

mycursor = cnx.cursor()
user_exit = False

print("Recreate database ? (y/n)")
user_answer = input()

if user_answer == 'y':
    from request_script import product_list, category_list
    # database_creation(mycursor)
    Insert_data(mycursor, product_list, category_list)
    mycursor.execute("""DELETE FROM Product_table
    WHERE Product_id < 1000000000000""")

userA = User()
userA.category_choice = CategorySelection(mycursor, displayed_categories, userA.category_choice, userA.categories_seen)
print(userA.category_choice) # Control
userA.id_of_selection = ProductSelection(mycursor, userA.category_choice, displayed_products, userA.products_seen, userA.categories_seen)
print(userA.id_of_selection) # Control
selection_c = displayed_categories[userA.category_choice + userA.categories_seen - 1]
print(selection_c)

mycursor.execute(f"""SELECT Nutriscore FROM Product_table
WHERE Product_id = {userA.id_of_selection}""")
origin_nutriscore = mycursor.fetchall()
origin_nutriscore = ''.join(origin_nutriscore[0])
print(origin_nutriscore)  # Control

userA.id_of_substitute = ResultSelection(mycursor, origin_nutriscore, selection_c)

choice = input("Save your research in database ? (y/n)")

if choice == 'y':
    SavedInsertion(mycursor, userA.id_of_selection, userA.id_of_substitute)

choice = input("Do you want to see history ? (y/n)")

if choice == 'y':
    ViewHistory(mycursor)

cnx.commit()

mycursor.close()
cnx.close()
