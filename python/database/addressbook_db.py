import MySQLdb
from app_base import Application
from dao import AddressBookDao

class AddrBookApp(Application):
    def __init__(self):
        super().__init__()
        print(self.config)
        self.db = MySQLdb.connect(db=self.config['db'],
                                 host=self.config['host'],
                                 user=self.config['user'],
                                 passwd=self.config['passwd'],
                                 charset="utf8", use_unicode=True) # defualt가 utf-8아님
        self.cursor = self.db.cursor()
        self.PERPAGE = 20   # 한 페이지당 출력 건수
        self.addressbook_dao = AddressBookDao(self.cursor)

    def create_menu(self, menu):
        menu.add('목록', self.print_list)
        menu.add('상세보기', self.print_detail)
        menu.add('검색', self.search)
        menu.add('추가', self.add)
        menu.add('수정', self.update)
        menu.add('삭제', self.delete)
        menu.add('종료', self.exit)

    def print_list(self):
        page = int(input('페이지:'))
        pagination = self.addressbook_dao.get_page(page, self.PERPAGE)
        print('='*75)
        print('주소록')
        print('='*75)
        for e in pagination.datas:
            print(f'{e.num:8d} {e.name:20s} {e.phone:16s} {e.email:20s} {e.addr}')
        print('-'*75)
        # 현재페이지/전체페이지 (총 데이터건수)
        print(f"{page}/{pagination.total_page} (총 {pagination.total_count} 건)")
        print('-'*75)

    def print_detail(self):
        num = int(input('번호:'))
        row = self.addressbook_dao.get(num)
        # row 출력
        if not row:
            print(f'{num}은 없습니다.')
            return
        
        # row[0] 로쓰면 가독성이 없어서 AddrBookEntry의 인스턴스로 만들어줌
        print(f'num: {row.num}')    
        print(f'이름: {row.name}')
        print(f'전화번호: {row.phone}')
        print(f'email: {row.email}')
        print(f'주소: {row.addr}')

    def search(self):
        keyword = input('검색어:')
        rows = self.addressbook_dao.search(keyword)
        # rows 출력
        print('='*75)
        print(f'검색결과({keyword})')
        print('='*75)
        for e in rows:
            print(f'{e.num:8d} {e.name:20s} {e.phone:16s} {e.email:20s} {e.addr}')
        print('-'*75)

    def add(self):
        # create
        pass

    def update(self):
        # update
        pass

    def delete(self):
        # delete
        pass

    def destroyed(self):
        self.cursor.close()
        self.db.close()

if __name__ == "__main__":
    app = AddrBookApp()
    app.run()