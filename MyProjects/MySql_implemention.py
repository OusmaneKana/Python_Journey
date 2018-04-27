import MySQLdb

db = MySQLdb.connect(host = "localhost", user = "root", passwd = "123456789", db = "Chestnut_DB")
 # Filled credentials and critical information with *** for security purposes
cur = db.cursor()

cur.execute("SELECT * FROM Student")

for row in cur.fetchall():
    print row[0], "", row[1]
