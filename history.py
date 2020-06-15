def ViewHistory(cursor):
    cursor.execute("SELECT * FROM Saved_searches;")
    history = cursor.fetchall()
    for line in history:
        print(line[1], line[2], line[3])
