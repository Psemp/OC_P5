
def Insert_data(mycursor, ObjectList1, ObjectList2):
    for product in ObjectList1:
        product_insertion = """INSERT INTO Product_table
        (Product_id , Product_name, Brand, Stores, Nutriscore, Category_id)
        VALUES(%s, %s, %s, %s, %s, %s)"""
        product_values = (product.barcode, product.name, product.brand, product.stores, product.nutriscore, product.category_id[0])
        mycursor.execute(product_insertion, product_values)

    for category in ObjectList2:
        category_insertion = """INSERT INTO Category_table
        (Category_id, Category_name, Translated_name)
        VALUES(%s, %s, %s)"""
        category_values = (category.id, category.web_id, category.display_name)
        mycursor.execute(category_insertion, category_values)

    mycursor.execute("""ALTER TABLE Product_table
    ADD CONSTRAINT fk_category_id FOREIGN KEY (category_id)
    REFERENCES Category_table(Category_id);""")
