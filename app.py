import mysql.connector
import sys
from management.sql_executor import DatabaseCreation
from management.data_insertion import Insert_data
from management.display_queries import CategorySelection, ProductSelection, ViewLink
from management.display_queries import ResultSelection, SavedInsertion
from functions.history import ViewHistory
from functions.input_regulation import InputChecker


u_category_choice = 0
u_category_id = 0
u_product_choice = 0
u_id_of_selection = 0
u_id_of_substitute = 0
u_products_seen = 0
u_categories_seen = 0


displayed_categories = []
displayed_products = []
display_limit = 10

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
print("Select History or comparison")
input_message = "Do you want to see history ? (y/n) : "
choice = InputChecker("y_n", 'y', 'n', input_message)

if choice == 'y':
    ViewHistory(mycursor)


input_message = "Recreate database ? (y/n) : "
user_answer = InputChecker("y_n", 'y', 'n', input_message)

if user_answer == 'y':
    from functions.request_script import product_list, category_list
    DatabaseCreation(mycursor)
    Insert_data(mycursor, category_list, product_list, cnx)
    mycursor.execute("""DELETE FROM Product_table
    WHERE Product_id < 1000000000000""")
    print("\n" * 20)


u_category_choice = CategorySelection(mycursor, displayed_categories, u_category_choice, u_categories_seen)
u_category_choice = ''.join(u_category_choice[0])
if u_category_choice is None:
    sys.exit("No category Selected, terminating script")
u_id_of_selection = ProductSelection(mycursor, u_category_choice, displayed_products, u_products_seen, u_categories_seen)
if u_id_of_selection is None:
    sys.exit("No product Selected, terminating script")
selection_c = displayed_categories[u_category_choice + u_categories_seen - 1]

mycursor.execute(f"""SELECT Nutriscore FROM Product_table
WHERE Product_id = {u_id_of_selection}""")
origin_nutriscore = mycursor.fetchall()
origin_nutriscore = ''.join(origin_nutriscore[0])

u_id_of_substitute = ResultSelection(mycursor, origin_nutriscore, selection_c)

if u_id_of_substitute is None:
    sys.exit("No substitude Selected/Detected, terminating script")

input_message = "Do you want to open product link ? (y/n) :"
choice = InputChecker("y_n", 'y', 'n', input_message)

if choice == 'y':
    mycursor.execute(f"""SELECT Url FROM Product_table
WHERE Product_id = {u_id_of_substitute}""")
    link = mycursor.fetchall()
    link = ''.join(link[0])
    ViewLink(link)

input_message = "Save your research in database ? (y/n) :"
choice = InputChecker("y_n", 'y', 'n', input_message)
if choice == 'y':
    SavedInsertion(mycursor, u_id_of_selection, u_id_of_substitute)


def HistoryCheck(cursor):
    cursor.execute('SELECT * FROM Saved_searches')
    history = cursor.fetchall()
    print(history, len(history))
    if len(history) == 0:
        print('nope')


cnx.commit()

mycursor.close()
cnx.close()
