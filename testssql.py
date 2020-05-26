import mysql.connector

db = mysql.connector.connect(
    user='root',
    password="somepassword",
    host="localhost",
    passwd="somepassword",
    database="Project5_db",
    auth_plugin='mysql_native_password'
    )

mycursor = db.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS Project5_db DEFAULT CHARACTER SET utf8;")
mycursor.execute("USE Project5_db;")
mycursor.execute("CREATE TABLE Category_table(Category_id INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT, Category_name VARCHAR(50) NOT NULL, Translated_name VARCHAR(45) NULL")
mycursor.execute("CREATE TABLE Product_table(Product_id BIGINT(13) UNSIGNED NOT NULL PRIMARY KEY, Product_name` VARCHAR(45) NOT NULL, Brand VARCHAR(45), Stores VARCHAR(45), Nutriscore ENUM('A', 'B', 'C', 'D', 'E') NOT NULL, Category_id INT UNSIGNED NOT NULL")