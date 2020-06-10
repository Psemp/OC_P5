import mysql.connector
import datetime

usr_pwd = input("Please enter password : ")

cnx = mysql.connector.connect(
    user='root',
    password=usr_pwd,
    host="localhost",
    database="Project5_db",
    auth_plugin='mysql_native_password'
    )

mycursor = cnx.cursor()


class User:

    def __init__(self):
        self.category_choice = 0
        self.category_id = 0
        self.product_choice = 0
        self.id_of_selection = 0
        self.id_of_substitute = 0


displayed_categories = []
displayed_products = []
display_limit = 10
userA = User()
categories_seen = 0
products_seen = 0


def CategorySelection(cursor):
    global categories_seen
    mycursor.execute("SELECT Translated_name, Category_id FROM Category_table")
    result = mycursor.fetchall()

    chunk_index = 0

    sublist_categories = [result[x:x+10] for x in range(0, len(result), 10)]

    for chunk in sublist_categories:

        idientifier = 1
        for sublist in sublist_categories[chunk_index]:
            print(sublist[0], idientifier)
            displayed_categories.append(sublist)
            idientifier += 1
        userA.category_choice = int(input("Select # (0 -> next page) : "))
        if userA.category_choice != 0:
            return
        else:
            categories_seen += 10
        print('end of list')
        chunk_index += 1


def ProductSelection(cursor):
    global products_seen
    mycursor.execute(f"""SELECT Product_name, Product_id FROM Product_table
    WHERE Category_id = {userA.category_choice + products_seen}""")
    result = mycursor.fetchall()

    chunk_index = 0

    sublist_producuts = [result[x:x+10] for x in range(0, len(result), 10)]

    for chunk in sublist_producuts:

        idientifier = 1
        for sublist in sublist_producuts[chunk_index]:
            print(sublist[0], idientifier)
            displayed_products.append(sublist)
            idientifier += 1
        userA.product_choice = int(input("Select category # (0 next) : "))
        if userA.product_choice != 0:
            return
        else:
            products_seen += 10
        print('end of list')
        chunk_index += 1


def ResultSelection(cursor, origin_nutriscore, selection_c):
    selected_category = selection_c[1]
    mycursor.execute(f"""SELECT Product_id, Product_name, Nutriscore
    FROM Product_table WHERE Nutriscore < '{origin_nutriscore}'
    and Category_id = {selected_category}
    ORDER BY Nutriscore ASC LIMIT 10;""")
    comparison = mycursor.fetchall()
    counter = 1

    for product in comparison:
        print(product[1], product[2], counter)
        counter += 1

    print("To save a comparison, select desired number (0 to skip)")
    result_choice = int(input())

    userA.id_of_substitute = comparison[result_choice - 1][0]
    print(comparison[result_choice-1], userA.id_of_substitute,  "THIS IS THE PRINT YOU ARE LOOKING FOR")


def SavedInsertion(cursor, origin_id, result_id, time):
    print("INTO SaveInsert")
    save = """INSERT INTO Saved_searches
        (Origin_id , Result_id, Date_Saved)
        VALUES(%s, %s, %s)"""
    save_values = (origin_id, result_id, time)
    cursor.execute(save, save_values)


def ViewHistory(cursor):
    cursor.execute("SELECT * FROM Saved_searches;")
    history = cursor.fetchall
    for line in history:
        print(line)


CategorySelection(mycursor)
ProductSelection(mycursor)


print(displayed_categories)
selection_c = displayed_categories[userA.category_choice + categories_seen - 1]
selection_p = displayed_products[userA.product_choice + products_seen - 1]
print(selection_c, selection_p)
userA.id_of_selection = selection_p[1]
print(userA.id_of_selection)
mycursor.execute(f"""SELECT Nutriscore FROM Product_table
WHERE Product_id = {userA.id_of_selection}""")
origin_nutriscore = mycursor.fetchall()
origin_nutriscore = ''.join(origin_nutriscore[0])


print(selection_c[1])
print(selection_p[1])
print(userA.id_of_substitute, "ID OF SUB")

if ResultSelection(mycursor, origin_nutriscore, selection_c) != 0:
    now = datetime.datetime.utcnow()
    SavedInsertion(mycursor, userA.id_of_selection, userA.id_of_substitute, now)

cnx.commit()

mycursor.close()
