
def Insert_data(mycursor, ObjectList1, ObjectList2):
    for product in ObjectList1:
        mycursor.execute("INSERT INTO Product_table VALUES(Product_id , Product_name, Brand, Stores, Nutriscore, Category_id);")
        product_values = ()
    for category in ObjectList2:
        mycursor.execute(f"INSERT INTO Category_table VALUES({category.id}, {category.web_id}, {category.name});")
