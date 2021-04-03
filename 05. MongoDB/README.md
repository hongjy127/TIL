# MongoDB



## 설치

[The most popular database for modern apps | MongoDB](https://www.mongodb.com/3)

​	Software 메뉴 > Community Server

​	(Install MongoDB Compass 설치 X)

​	PATH 추가(C:\Program Files\MongoDB\Server\4.4\bin)

[Robomongo](https://robomongo.org/download)



## MongoDB

- 데이터베이스 > 컬렉션 > 도큐먼트
- 데이터베이스가 없어도 알아서 생성
- 제약이 적어서 오류날 일이 거의 없음(오타 주의)
  - 원자성(성공 or 실패, 부분성공은 없음)

```
db	// 현재 사용중인 데이터베이스명
show dbs	// 모든 데이터베이스명 출력
show collections	// 현재 데이터베이스의 컬렉션
```



### 생성

- `insert`, `insertOne`, `insertMany`

```
use testDB	// 알아서 데이터베이스 생성
db.testCollection.insertOne(	// 알아서 컬렉션 생성
	{도큐먼트}
)
```

```
db.testCollection.insertMany([	// 알아서 컬렉션 생성
	{도큐먼트},
	{도큐먼트},
	{도큐먼트}
	]
)
```



### 조회

- `find({조건문서},{프로젝션문서}), findOne`

```
db.testCollection.find()	// 전체
db.testCollection.find({doc})	// 해당하는 것만

db.A.find({'name.firstName' : 'Karoid'})
// 점연산자를 사용가능 -> '' 붙여주기
```



### 수정

- `replaceOne`, `replaceMany`

```
db.testCollection.replaceOne(
    <query>,
    <document>,
    {
    upsert: <boolean>,
    writeConcern: <document>,
    collation: <document>
    }
)
```

- `updateOne`, `updateMany`

```
db.testCollection.updateOne(
    <query>,
    <update>,
    {
    upsert: <boolean>,
    writeConcern: <document>,
    collation: <document>,
    arrayFilters: [ <filterdocument1>, …]
    }
)
```

연산자 $



### 삭제

- 도큐먼트 삭제: `deleteOne`, `deleteMany`

```
db.testCollection.deleteMany({})	// 전체 삭제
```

- 컬렉션 삭제: `drop`

```
db.testCollection.drop()
```





## Python - MongoDB

- 패키지 설치

```
pip install pymongo
```



```python
from pymongo import MongoClient

# db 서버 접속
db_client = MongoClient("mongodb://localhost:27017/") 

# db 목록
print(db_client.list_database_names())

# db 선택
test_db = db_client['db_name']
# collection 선택
test_col = test_db['collection_name']
```



### 생성

```
x = test_col.insert_one(test_value)
x = test_col.insert_many(test_value)
```



### 조회

```
x = test_col.find()
x = test_col.find().sort("내용")
```



### 삭제

```
x = test_col.delete_one()
x = test_col.delete_many()
```

