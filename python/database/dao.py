# DAO : Data Access Object
import MySQLdb
import math
from models import AddressBookEntry

# 튜플로 만드는 경우 가독성이 떨어져서 객체를 리턴
# 페이지 만들 때 주로 이렇게 사용함
class Pagination:
    def __init__(self, total_count, total_page, datas):
        self.total_count = total_count
        self.total_page = total_page
        self.datas = datas

class AddressBookDao:
    def __init__(self, cursor):
        self.cursor = cursor

    def get_total_count(self):
        query = "SELECT COUNT(*) FROM addressbook"
        self.cursor.execute(query)
        return self.cursor.fetchone()[0]

    def get_list(self, start, perpage):
        query = f"SELECT * FROM addressbook ORDER BY name LIMIT {start}, {perpage}"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()   # ((,,),...), ()
        # Comprehension
        return (AddressBookEntry(*row) for row in rows)
        # Map


    def get_page(self, page, perpage):
        start = (page-1)*perpage
        total_count = self.get_total_count()
        total_page = math.ceil(total_count/perpage)
        rows = self.get_list(start, perpage)
        return Pagination(total_count, total_page, rows)

    def get(self, num):
        query = f"SELECT * FROM addressbook WHERE num = {num}"
        self.cursor.execute(query)
        row = self.cursor.fetchone()    # tuple or None
        if row:
            # query에서 나온 결과와 AddressBookEntry에 넣는 인수의 순서가 동일하다는 가정 하에
            return AddressBookEntry(*row)
        else:
            return None
    
    def search(self, keyword):
        keyword = keyword.lower()
        query = f"SELECT * FROM addressbook WHERE LOWER(name) LIKE '%{keyword}%'"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        return (AddressBookEntry(*row) for row in rows)

    # 수행평가
    def add(self, name, phone, email, addr):
        query = f"INSERT INTO addressbook (name, phone, email, addr) VALUES ('{name}', '{phone}', '{email}', '{addr}')"
        self.cursor.execute(query)

    def update(self, num, name, phone, email, addr):
        query = f"UPDATE addressbook SET name='{name}', phone='{phone}', email='{email}', addr='{addr}' WHERE num='{num}'"
        self.cursor.execute(query)

    def delete(self, num):
        query = f"DELETE FROM addressbook WHERE num='{num}'"
        self.cursor.execute(query)