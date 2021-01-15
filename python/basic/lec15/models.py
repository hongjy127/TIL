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
        
    def save(self, config):
        with open(config.fname, 'wt', encoding=config.encoding) as f:
            f.write('이름,전화번호,email,주소\n')
            for entry in self.book:
                # line = ','.join(entry)  # iterable 객체로 만들기
                line = f'{entry.name},{entry.phone},{entry.email},{entry.addr}'
                f.write(line+'\n')

    def add(self, name, phone, email, addr):
        entry = AddressBookEntry(name, phone, email, addr)
        self.book.append(entry)
        self.book.sort(key=lambda a: a.name)

    def delete(self, index):
        del self.book[index]

    def update(self, index, name, phone, email, addr):
        self.book[index].name = name
        self.book[index].phone = phone
        self.book[index].email = email
        self.book[index].addr = addr
        self.book.sort(key=lambda a: a.name)

    def search(self,keyword):
        # result = []
        # for entry in self.book:
        #     if entry.name.find(keyword) != -1:
        #         result.append(entry)
        # return result
        return list(filter(lambda entry: entry.name.find(keyword) != -1, self.book))

    def __str__(self):
        return f'<AddressBook {self.book}>'