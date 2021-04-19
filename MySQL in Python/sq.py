import mysql.connector

data = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = ""
)

print(data)