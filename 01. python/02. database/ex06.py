import sqlite3

# 세션만들기
con = sqlite3.connect('addr.db')
cursor = con.cursor()

cursor.execute("""
UPDATE tblAddr
SET addr = '제주도' WHERE name = '김상형'
""")

con.commit()

cursor.close()
con.close()