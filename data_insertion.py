
def Insert_data(mycursor, ObjectList1, ObjectList2):
    for product in ObjectList1:
        mycursor.execute(f"INSERT INTO Product_table VALUES({product.barcode}, {product.name}, {product.brand}, {product.stores}, {Nutriscore}, {Category_id})")

    for category in ObjectList2:
        mycursor.execute(f"INSERT INTO Category_table VALUES({category.id}, {category.web_id}, {category.name})")
