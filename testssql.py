import mysql.connector
from sql_db_creation import Create_Dbs
from data_insertion import Insert_data
from demeter import product_list, category_list

cnx = mysql.connector.connect(
    user='root',
    password="06022018",
    host="localhost",
    passwd="06022018",
    database="Project5_db",
    auth_plugin='mysql_native_password'
    )

mycursor = cnx.cursor()

Create_Dbs(mycursor)

Insert_data(mycursor, product_list, category_list)

cnx.commit()

mycursor.close()
cnx.close()
