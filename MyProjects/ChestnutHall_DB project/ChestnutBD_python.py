#!/usr/bin/python

import pymysql

# Open database connection
db = pymysql.connect("localhost","root","123456789","Chestnut_DB" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
data = cursor.execute("select * from Student")

# Fetch a single row using fetchone() method.
# data = cursor.fetchone()
print ("Database version : %s " % data)

# disconnect from server
db.close()
