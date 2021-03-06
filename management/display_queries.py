import datetime
import webbrowser
from functions.input_regulation import InputChecker


def CategorySelection(cursor, displayed_categories, cat_choice, categories_seen):
    cursor.execute("SELECT Translated_name FROM Category_table")
    result = cursor.fetchall()

    chunk_index = 0

    sublist_categories = [result[x:x+10] for x in range(0, len(result), 10)]

    for chunk in sublist_categories:

        idientifier = 1
        print("")
        for sublist in sublist_categories[chunk_index]:
            print(sublist[0], idientifier)
            displayed_categories.append(sublist)
            idientifier += 1
        print("")
        cat_choice = InputChecker("ls_ind", 0, int(idientifier) - 1, "Select # (0 -> next page) : ")
        if cat_choice != 0:
            cat_choice = cat_choice + categories_seen
            return result[cat_choice - 1]
        else:
            categories_seen += 10
        chunk_index += 1


def ProductSelection(cursor, cat_choice, displayed_products, products_seen):
    cursor.execute(f"""SELECT Product_name, Product_id, Product_table.Category_id, Nutriscore
    FROM Product_table
    INNER JOIN Category_table
        ON Category_table.Category_id = Product_table.Category_id
    WHERE Category_table.Translated_Name = '{cat_choice}'""")
    result = cursor.fetchall()
    chunk_index = 0

    sublist_producuts = [result[x:x+10] for x in range(0, len(result), 10)]

    for chunk in sublist_producuts:
        idientifier = 1
        print("")
        for sublist in sublist_producuts[chunk_index]:
            print(sublist[0], idientifier)
            displayed_products.append(sublist)
            idientifier += 1
        print("")
        prod_choice = InputChecker("ls_ind", 0, int(idientifier) - 1, "Select Product # (0 -> next page) : ")
        if prod_choice != 0:
            selection_p = displayed_products[prod_choice + products_seen - 1]
            return selection_p
        else:
            products_seen += 10
        chunk_index += 1


def ResultSelection(cursor, origin_nutriscore, selection_c):
    cursor.execute(f"""SELECT Product_id, Product_name, Nutriscore
    FROM Product_table WHERE Nutriscore < '{origin_nutriscore}'
    and Category_id = {selection_c}
    ORDER BY Nutriscore ASC LIMIT 10;""")
    comparison = cursor.fetchall()
    if len(comparison) == 0:
        print('No comparison found, sorry')
        return
    counter = 1

    for product in comparison:
        print(product[1], product[2], counter)
        counter += 1

    print('\n')
    result_text = "To save a comparison, select desired number (0 to skip)"
    result_choice = InputChecker("ls_ind", 0, int(counter) - 1, result_text)
    print(result_choice)
    if result_choice == 0:
        return 0
    else:
        return comparison[result_choice - 1][0]


def SavedInsertion(cursor, origin_id, result_id):
    now = datetime.datetime.utcnow()
    print("Result Saved")
    save = """INSERT INTO Saved_searches
        (Origin_id , Result_id, Date_Saved)
        VALUES(%s, %s, %s)"""
    save_values = (origin_id, result_id, now)
    cursor.execute(save, save_values)


def ViewLink(url):

    webbrowser.open(url, new=2, autoraise=True)
