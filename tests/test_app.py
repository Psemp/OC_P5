import mysql.connector
from display_queries_tst import CategorySelection, ProductSelection, ResultSelection
from db_creation_test import DatabaseCreation
# from request_script import product_list, category_list

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

u_category_choice = 0
u_category_id = 0
u_product_choice = 0
u_selection = 0
u_id_of_substitute = 0
u_products_seen = 0
u_categories_seen = 0


displayed_categories = []
displayed_products = []
display_limit = 10


def Insert_data(mycursor, ObjectList1, ObjectList2):

    for category in ObjectList2:
        category_insertion = """INSERT INTO Category_table
        (Category_id, Category_name, Translated_name)
        VALUES(%s, %s, %s)"""
        category_values = (category.id, category.web_id, category.display_name)
        mycursor.execute(category_insertion, category_values)
    cnx.commit()

    for product in ObjectList1:
        product_insertion = """INSERT INTO Product_table
        (Product_id , Product_name, Brand,Stores,Url,Nutriscore,Category_id)
        VALUES(%s, %s, %s, %s, %s, %s, %s)"""
        product_values = (product.barcode, product.name, product.brand, product.stores, product.url, product.nutriscore, product.category_id[0])
        mycursor.execute(product_insertion, product_values)
    cnx.commit()


# DatabaseCreation(mycursor)
# Insert_data(mycursor, product_list, category_list)
# print(type(CategorySelection(mycursor, displayed_categories, u_category_choice, u_categories_seen)))
# print(CategorySelection(mycursor, displayed_categories, u_category_choice, u_categories_seen))
u_category_choice = CategorySelection(mycursor, displayed_categories, u_category_choice, u_categories_seen)
# print(u_category_choice)
u_category_choice = ''.join(u_category_choice[0])
print(u_category_choice)
# print(ProductSelection(mycursor, u_category_choice, displayed_products, u_products_seen))
u_selection = ProductSelection(mycursor, u_category_choice, displayed_products, u_products_seen)
print(u_selection[2], u_selection[0])
print('\n'*3)
print(ResultSelection(mycursor, u_selection[3], u_selection[2]))
