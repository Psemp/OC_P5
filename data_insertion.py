
def Insert_data(mycursor, ObjectList1, ObjectList2):
    for product in ObjectList1:
        product_insertion = "INSERT INTO Product_table (Product_id , Product_name, Brand, Stores, Nutriscore, Category_id) VALUES(s%, s%, s%, s%, s%, s%)"
        product_values = (product.barcode, product.name, product.brand, product.stores, product.nutriscore, product.category_id)
        mycursor.execute()
        
    for category in ObjectList2:
        mycursor.execute(f"INSERT INTO Category_table VALUES({category.id}, {category.web_id}, {category.name});")
