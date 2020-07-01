def ViewHistory(cursor):
    from management.display_queries import ViewLink
    from functions.input_regulation import InputChecker
    from models.comparison import Comparison

    comparison_list = []
    cursor.execute("SELECT * FROM Saved_searches;")
    history = cursor.fetchall()
    if len(history) == 0:
        print("No comparison saved in database - Skipping")
        return

    for line in history:
        comparison_list.append(Comparison(line[1], line[2], line[3], cursor))

    identifier = 1
    for comp in comparison_list:
        print(f"{comp.r_name} <<Healthier Than>> {comp.o_name} SAVED ON {comp.date}", " !! Identifier =", identifier)
        identifier += 1

    print('\n')
    input_text = "To know more about saved result, enter its identfier"
    user_input = InputChecker("ls_ind", 1, identifier - 1, input_text)
    print(f"{comparison_list[user_input - 1].r_name} : Brand is {comparison_list[user_input - 1].r_brand}")
    if len(comparison_list[user_input - 1].r_stores) > 1:
        print(f"You can purchase it in {comparison_list[user_input - 1].r_stores}")

    input_message = "Do you want to open product link ? (y/n) : "
    choice = InputChecker("y_n", 'y', 'n', input_message)

    if choice == 'y':
        cursor.execute(f"""SELECT Url FROM Product_table
        WHERE Product_id = {comparison_list[user_input - 1].r_id}""")
        link = cursor.fetchall()
        link = ''.join(link[0])
        ViewLink(link)
