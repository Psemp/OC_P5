import mysql.connector
import datetime

# usr_pwd = input("Please enter password : ")

# cnx = mysql.connector.connect(
#     user='root',
#     password=usr_pwd,
#     host="localhost",
#     database="Project5_db",
#     auth_plugin='mysql_native_password'
#     )

# mycursor = cnx.cursor()


# class User:

#     def __init__(self):
#         self.category_choice = 0
#         self.category_id = 0
#         self.product_choice = 0
#         self.id_of_selection = 0
#         self.id_of_substitute = 0


# displayed_categories = []
# displayed_products = []
# display_limit = 10
# userA = User()
# categories_seen = 0
# products_seen = 0


def CategorySelection(cursor, displayed_categories, cat_choice, categories_seen):
    cursor.execute("SELECT Translated_name, Category_id FROM Category_table")
    result = cursor.fetchall()

    chunk_index = 0

    sublist_categories = [result[x:x+10] for x in range(0, len(result), 10)]

    for chunk in sublist_categories:

        idientifier = 1
        for sublist in sublist_categories[chunk_index]:
            print(sublist[0], idientifier)
            displayed_categories.append(sublist)
            idientifier += 1
        cat_choice = int(input("Select # (0 -> next page) : "))
        if cat_choice != 0:
            cat_choice = cat_choice + categories_seen
            print(cat_choice)
            return cat_choice
        else:
            categories_seen += 10
        print('end of list')
        chunk_index += 1


def ProductSelection(cursor, cat_choice, displayed_products, products_seen, categories_seen):
    print("HELLO")
    cursor.execute(f"""SELECT Product_name, Product_id FROM Product_table
    WHERE Category_id = {cat_choice + categories_seen}""")
    print(cat_choice, categories_seen)
    result = cursor.fetchall()
    print(result)
    chunk_index = 0

    sublist_producuts = [result[x:x+10] for x in range(0, len(result), 10)]

    for chunk in sublist_producuts:
        idientifier = 1
        for sublist in sublist_producuts[chunk_index]:
            print(sublist[0], idientifier)
            displayed_products.append(sublist)
            idientifier += 1
        prod_choice = int(input("Select category # (0 next) : "))
        if prod_choice != 0:
            selection_p = displayed_products[prod_choice + products_seen - 1]
            print(selection_p)
            return selection_p[1]
        else:
            products_seen += 10
        print('end of list')
        chunk_index += 1


def ResultSelection(cursor, origin_nutriscore, selection_c):
    selected_category = selection_c[1]
    cursor.execute(f"""SELECT Product_id, Product_name, Nutriscore
    FROM Product_table WHERE Nutriscore < '{origin_nutriscore}'
    and Category_id = {selected_category}
    ORDER BY Nutriscore ASC LIMIT 10;""")
    comparison = cursor.fetchall()
    counter = 1

    for product in comparison:
        print(product[1], product[2], counter)
        counter += 1

    print("To save a comparison, select desired number (0 to skip)")
    result_choice = int(input())

    return comparison[result_choice - 1][0]


def SavedInsertion(cursor, origin_id, result_id):
    now = datetime.datetime.utcnow()
    print("INTO SaveInsert")
    save = """INSERT INTO Saved_searches
        (Origin_id , Result_id, Date_Saved)
        VALUES(%s, %s, %s)"""
    save_values = (origin_id, result_id, now)
    print(origin_id, result_id, now)
    cursor.execute(save, save_values)


def ViewHistory(cursor):
    cursor.execute("SELECT * FROM Saved_searches;")
    history = cursor.fetchall()
    for line in history:
        print(line[1], line[2], line[3])



# print(displayed_categories)
# selection_c = displayed_categories[userA.category_choice + categories_seen - 1]
# selection_p = displayed_products[userA.product_choice + products_seen - 1]
# print(selection_c, selection_p)
# userA.id_of_selection = selection_p[1]
# print(userA.id_of_selection)
# mycursor.execute(f"""SELECT Nutriscore FROM Product_table
# WHERE Product_id = {userA.id_of_selection}""")
# origin_nutriscore = mycursor.fetchall()
# origin_nutriscore = ''.join(origin_nutriscore[0])


# print(selection_c[1])
# print(selection_p[1])
# print(userA.id_of_substitute, "ID OF SUB")

# if ResultSelection(mycursor, origin_nutriscore, selection_c) != 0:
#     now = datetime.datetime.utcnow()
#     SavedInsertion(mycursor, userA.id_of_selection, userA.id_of_substitute, now)

# cnx.commit()

# mycursor.close()
