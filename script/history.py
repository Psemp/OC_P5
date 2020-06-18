def ViewHistory(cursor):
    from display_queries import ViewLink
    from input_regulation import InputChecker

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

    comparison_list = []
    cursor.execute("SELECT * FROM Saved_searches;")
    history = cursor.fetchall()
    for line in history:
        comparison_list.append(Comparison(line[1], line[2], line[3], cursor))

    identifier = 1
    for comp in comparison_list:
        print(f"{comp.r_name} <<Healthier Than>> {comp.o_name} Saved on {comp.date}",
    " !! Identifier =", identifier)
        identifier += 1

    input_text = "To know more about saved result, enter its identfier"
    user_input = InputChecker("ls_ind", 1, identifier - 1, input_text)
    print(f"{comparison_list[user_input - 1].r_name} : Brand is {comparison_list[user_input - 1].r_brand}")
    if len(comparison_list[user_input - 1].r_stores) > 1:
        print(f"You can purchase it in {comparison_list[user_input - 1].r_stores}")

    input_message = "Do you want to open product link ? (y/n) :"
    choice = InputChecker("y_n", 'y', 'n', input_message)

    if choice == 'y':
        cursor.execute(f"""SELECT Url FROM Product_table
        WHERE Product_id = {comparison_list[user_input - 1].r_id}""")
        link = cursor.fetchall()
        link = ''.join(link[0])
        ViewLink(link)
