
def Insert_data(mycursor, ObjectList1, ObjectList2, cnx):
    for category in ObjectList1:
        category_insertion = """INSERT INTO Category_table
        (Category_id, Category_name, Translated_name)
        VALUES(%s, %s, %s)"""
        category_values = (category.id, category.web_id, category.display_name)
        mycursor.execute(category_insertion, category_values)
    cnx.commit()

    for product in ObjectList2:
        product_insertion = """INSERT INTO Product_table
        (Product_id , Product_name, Brand,Stores,Url,Nutriscore,Category_id)
        VALUES(%s, %s, %s, %s, %s, %s, %s)"""
        product_values = (product.barcode, product.name, product.brand, product.stores, product.url, product.nutriscore, product.category_id[0])
        mycursor.execute(product_insertion, product_values)
    cnx.commit()
