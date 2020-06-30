
def Insert_data(mycursor, cat_list, prod_list, cnx):

    for category in cat_list:
        category_insertion = """INSERT INTO Category_table
        (Category_id, Category_name, Translated_name)
        VALUES(%s, %s, %s)"""
        category_values = (category.id, category.web_id, category.display_name)
        mycursor.execute(category_insertion, category_values)
    cnx.commit()

    for product in prod_list:
        product_insertion = """INSERT INTO Product_table
        (Product_id , Product_name, Brand,Stores,Url,Nutriscore,Category_id)
        VALUES(%s, %s, %s, %s, %s, %s, %s)"""
        product_values = (product.barcode, product.name, product.brand, product.stores, product.url, product.nutriscore, product.category_id[0])
        mycursor.execute(product_insertion, product_values)
    cnx.commit()

    #  I have no idea why but the insertion fails if the constraint is not
    #  added, so i'll just leave it here
