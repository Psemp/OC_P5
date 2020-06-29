class Comparison:

    def __init__(self, r_id, o_id, date, cursor):
        self.r_id = r_id
        self.o_id = o_id
        self.date = date
        query = f"""SELECT Product_name, Brand, Stores
    FROM Product_table
    WHERE Product_table.Product_id = {r_id};"""
        cursor.execute(query)
        result = cursor.fetchall()
        self.r_name = result[0][0]
        self.r_brand = result[0][1]
        self.r_stores = result[0][2]
        query = f"""SELECT Product_name
    FROM Product_table
    WHERE Product_id = {o_id};"""
        cursor.execute(query)
        result = cursor.fetchall()
        self.o_name = result[0][0]
