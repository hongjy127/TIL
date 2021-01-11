# 주소록 앱 ---> 객체 지향적으로 ....

# 1. 문제 파악
# 2. 문제 해결을 위해 필요한 객체가 뭐냐? ****
# 2.1 어떤 정보를 다루느냐?
#   1) 이름,이메일, 전화번호, 주소--> 주소록 정보
#   2) 설정 정보(파일명, encoding 방식..)
# 2.2 단위 데이터의 형태가 어떻게 되는가?
#   1) 하나의 주소록 정보 : 이름, 이메일, 전화번호, 주소 --> 단위 데이터   
#   2) 설정 정보
# 2.3 데이터의 개수, 어떻게 관리할 것인가?
#   1) 주소록 정보 N개 --> 콜렉션
#   2) 설정 정보 1개 -> 단일 변수 


# 모델(Model) 객체
class Configuration:
    def __init__(self):
        # csv 파일 경로명, encoding, ... -> 설정 파일에 분석해서 초기화
        config = self.load()
        self.fname = config['FNAME']
        self.encoding = config['ENCODING']

    def load(self):
        config = {}
        with open('config.ini','rt') as f:
            entries = f.readlines()
            for entry in entries:
                key, value = entry.split('=')
                config[key.strip()] = value.strip()
        return config

    def __str__(self):
        return f'<Configuration fname {self.fname}, encoding {self.encoding}>'

# 단위 테스트(unit test)
# config = Configuration()
# print(config)

class AddressBookEntry:
    def __init__(self, name, phone, email, addr):
        self.name = name
        self.phone = phone
        self.email = email
        self.addr = addr

    def __str__(self):
        return f'<AddressBookEntry {self.name}, {self.phone}, {self.email}, {self.addr}>'
    
    def __repr__(self):
        return f'<AddressBookEntry {self.name}>'

# entry = AddressBookEntry('홍길동','010-1111-1111', 'hong@naver.com','서울')
# print(entry)

class AddressBook:  # 프로토타입 객체
    def __init__(self):
        self.book = []

    def load(self, config):
        with open(config.fname, 'rt', encoding=config.encoding) as f:
            lines = f.readlines()[1:]
            for line in lines:
                name, phone, email, addr = line.strip().split(',')
                # AddresssBookEntry를 생성하여 self.book에 추가
                entry = AddressBookEntry(name, phone, email, addr)
                self.book.append(entry)
        # 정렬
        self.book.sort(key=lambda a: a.name)

    def add(self, name, phone, email, addr):
        pass

    def delete(self, name):
        pass

    def update(self, name, phone, email, addr):
        pass

    def __str__(self):
        return f'<AddressBook {self.book}>'

# config = Configuration()
# book = AddressBook()
# book.load(config)
# print(book)

import sys
# Configuration 설정 정보 담당
# AddressBookEntry 한 사람 주소 정보 담당
# AddressBook 목록 관리

class Application:
    def __init__(self):
        self.config = Configuration()
        self.addressbook = AddressBook()
        self.addressbook.load(self.config)        

    def select_menu(self):
        print('1)목록, 2)상세보기, 3)추가, 4)수정, 5)삭제 6)종료')
        menu = int(input('입력: '))
        return menu

    def run(self,menu):
        # 해당 메뉴를 실행
            if menu==1:  # 목록
                self.print_book()
            elif menu==2:  # 상세보기
                self.print_detail()
            elif menu==3: #  추가
                self.add()
            elif menu==4: #  수정
                self.update()
            elif menu==5: #  삭제
                self.delete()
            elif menu==6: #  종료
                self.exit()
            else:
                print('잘못 선택했습니다.')

    def print_book(self):
        print('='*50)
        print('주소록')
        print('='*50)
        for index, entry in enumerate(self.addressbook.book,1):
            print(f'{index:02d}] {entry.name}: {entry.phone}, {entry.email}, {entry.addr}')

        print('-'*50)

    def print_detail(self):
        pass

    def add(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

    def exit(self):
        sys.exit(0)

def main():
    app = Application()
    while True:
        menu = app.select_menu()
        app.run(menu)

main()


# 기존 방법 : 절차 중심 --> Top down
# OOP: 객체 지향방법 --> bottom up
# Application
#     Configuration
#     AddressBook
#         AddressBookEntry