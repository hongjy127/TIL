import sqlite3

con = sqlite3.connect('addr.db')
cursor = con.cursor()

name = input("이름: ")
phone = input("전화번호: ")
addr = input("주소: ")

query = f"""
INSERT INTO tblAddr(name, phone, addr)
VALUES('{name}','{phone}','{addr}')
"""
cursor.execute(query)

# insert, update, delete는 commit이 꼭 필요
# 실수방지 / 잘못해서 데이터를 지웠을때
con.commit()

cursor.close()
con.close()