import pickle
import sys

### 관례
# 변수명: 명사
# 함수명: 동사_목적어

# 프로그램 운영에 필요한 factor를 저장해놓음
# dict로 만들어서 운영
def load_config():  # config load
    config = {}
    with open('config.ini', 'rt') as f:
        entries = f.readlines()
        for entry in entries:
            key, values = entry.split('=')
            config[key.strip()] = values.strip()

    return config

def load(fpath, encoding):  # file load
    with open(fpath,'rt', encoding=encoding) as f:
        return f.readlines()

# key가 list
# {이름 : [전화번호, email, 주소], }
# key가 dict
# {이름: {전화번호: ,email: ,주소: }, }     
def make_book(lines):  # list -> dict
    data = {}
    for line in lines[1:]:
        name, phone, email, addr = line.split(',')
        data[name] = [phone.strip(), email.strip(), addr.strip()]
    return data

# 정보관리 기본 기능
# 목록 보여주기(R), 상세정보(R), 추가(C), 수정(U), 삭제(D) -> CRUD 작업(연산)
def select_menu():
    print('1)목록, 2)상세보기, 3)추가, 4)수정, 5)삭제 6)종료')
    menu = int(input('입력: '))
    return menu

def print_book(book):
    # 정렬해서 출력
    names = list(book.keys())
    names.sort()
    print('='*50)
    print('주소록')
    print('='*50)
    # 실제 데이터 출력
    for name in names:
        info = book[name]
        print(f"{name} : {info[0]}, {info[1]}, {info[2]}")
    print('-'*50)

def print_detail(book):
    name = input('이름: ')  # 검색
    if name not in book:
        print(f'{name}은 목록에 없습니다.')
    else:
        info = book[name]  # 예외처리는 하면 안됨 -> get() or in
        print(f"{name} : {info[0]}, {info[1]}, {info[2]}")

def add_entry(book):
    name = input('이름: ')
    if name in book:
        print(f"{name}은 이미 존재합니다.")
        return

    phone = input('전화번호: ')
    email = input('이메일: ')
    addr = input('주소: ')
    book[name] = [phone.strip(), email.strip(), addr.strip()]
    # 원래 파일에 저장



def del_entry(book):
    name = input('삭제할 이름을 입력하세요.: ')
    if name not in book:
        print(f'{name}은 목록에 없습니다.')
        return
    
    del book[name]

def main():
    try:
        config = load_config()
        lines = load(config['FNAME'], config['ENCODING'])
        book = make_book(lines)
        while True:
            menu = select_menu()
            # 해당 메뉴를 실행
            if menu==1:  # 목록
                print_book(book)
            elif menu==2:  # 상세보기
                print_detail(book)
            elif menu==3: #  추가
                add_entry(book)
            elif menu==4: #  수정
                pass
            elif menu==5: #  삭제
                del_entry(book)
            elif menu==6: #  종료
                sys.exit(0)
            else:
                print('잘못 선택했습니다.')

    except Exception as e:
        print(f"예외: {e}")

main()