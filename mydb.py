import mysql.connector

dataBase=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Sidd1234'
)

#prepare cursor object
cursorObject=dataBase.cursor()

cursorObject.execute("CREATE DATABASE crm")

print("All done !")