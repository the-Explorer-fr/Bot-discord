import mysql.connector

database = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "root",
)
curseur = database.cursor()

curseur.execute("SHOW DATABASES")

for db in curseur:
    print(db)
print('end')