import mysql.connector

# import re

# for line in open('db_creation_script.sql'):
#     statement = ""

#     if re.match(r'--', line):
#         continue
#     if len(line) == 0:
#         continue
#     if not re.search(r';$', line):
#         statement = statement + line
#     else:
#         statement = statement + line
#         # print(statement)

#         statement = ""

usr_pwd = input("Please enter password : ")

cnx = mysql.connector.connect(
    user='root',
    password=usr_pwd,
    host="localhost",
    passwd=usr_pwd,
    database="Project5_db",
    auth_plugin='mysql_native_password'
    )

mycursor = cnx.cursor()

mycursor.execute("SELECT * FROM Saved_searches;")
history = mycursor.fetchall()

result_list = []
origin_list = []

for line in history:
    id_r = line[1]
    id_o = line[2]
    mycursor.execute(f"""SELECT Product_name
FROM Product_table
INNER JOIN Saved_searches
    ON Product_id = Result_id
WHERE Product_table.Product_id = {id_r};""")
    result_list.append(mycursor.fetchall())

    mycursor.execute(f"""SELECT Product_name
FROM Product_table
INNER JOIN Saved_searches
    ON Product_id = Origin_id
WHERE Product_table.Product_id = {id_o};""")
    origin_list.append(mycursor.fetchall())

# for line in history:
#     print(line[0], line[1], line[2], line[3])

# print(result_list)
# print(origin_list)

index = 0
for sublist in result_list:
    print(result_list[index], origin_list[index])
    index += 1

print(''.join((result_list[1][0])))
# query = f"""SELECT Product_name
# FROM Product_table
# INNER JOIN Saved_searches
#     ON Product_id = Result_id
# WHERE Product_table.Product_id = {id}"""
