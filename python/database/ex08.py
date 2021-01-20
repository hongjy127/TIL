import MySQLdb

db = MySQLdb.connect(db="employees", host="localhost", user="iot", passwd="1234")
c = db.cursor()

# sqlite와 동일

c.close()
db.close()