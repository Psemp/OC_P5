import mysql.connector
import sys
from management.sql_executor import DatabaseCreation
from management.data_insertion import Insert_data
from management.display_queries import CategorySelection, ProductSelection, ViewLink
from management.display_queries import ResultSelection, SavedInsertion
from functions.history import ViewHistory
from functions.input_regulation import InputChecker


u_category_choice = 0
u_selection = 0
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

if u_category_choice is None:
    sys.exit("No category Selected, terminating script")

u_category_choice = ''.join(u_category_choice[0])
u_selection = ProductSelection(mycursor, u_category_choice, displayed_products, u_products_seen)

if u_selection is None:
    sys.exit("No product Selected, terminating script")

u_id_of_substitute = ResultSelection(mycursor, u_selection[3], u_selection[2])

if u_id_of_substitute is None or u_id_of_substitute == 0:
    sys.exit("No substitude Selected/Detected, terminating script")

input_message = "Do you want to open product link ? (y/n) : "
choice = InputChecker("y_n", 'y', 'n', input_message)

if choice == 'y':
    mycursor.execute(f"""SELECT Url FROM Product_table
WHERE Product_id = {u_id_of_substitute}""")
    link = mycursor.fetchall()
    link = ''.join(link[0])
    ViewLink(link)

input_message = "Save your research in database ? (y/n) : "
choice = InputChecker("y_n", 'y', 'n', input_message)
if choice == 'y':
    SavedInsertion(mycursor, u_selection[1], u_id_of_substitute)


cnx.commit()

mycursor.close()
cnx.close()
