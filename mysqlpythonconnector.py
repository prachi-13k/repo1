import mysql.connector as mysql


db = mysql.connect(
    host="localhost",
    user="root",
    passwd="12345678",
#    database = "datacamptutorial1"
)

print("db: ", db)

cursor = db.cursor()
print("cursor: ", cursor)
cursor.execute("DROP DATABASE datacamptutorial1")

print("cursor: ", cursor)