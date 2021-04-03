# 데이터베이스

[[MariaDB]](https://github.com/hongjy127/TIL/blob/master/MariaDB/MariaDB.md)



## SQLite

- 설정

  vscode에서 SQL사용 (`import sqlite3`)

  확장팩 > sqlite 설치



- 기본 구조

```python
import sqlite3

# 세션만들기
con = sqlite3.connect('DB파일명')
cursor = con.cursor()

# SQL 명령 실행
cursor.execute("""
SQL문을 모두 여기에 작성
SQL문은 모두 문자열
""")

# 실제로 테이블에 반영하는 코드 (실수방지)
# insert, update, delete는 commit이 꼭 필요
con.commit()

cursor.close()
con.close()
```

- fetch

```python
cursor.fetchall()	# 전부 다 가져오기
cursor.fetchone()	# 한개씩 가져오기
# 목록이 있는 경우 tuple의 tuple로 리턴 ((,,), (,,), ...)
# 목록이 없는 경우 None 리턴
```



## MySQL

- 설정

  vscode에서 MySQL 사용 (`import MySQLdb`)

  `> pip install mysqlclient`

  확장팩 > MySQL 설치

```python
# sqlite3와 동일
import MySQLdb

# 세션만들기
# db, host, user, passwd는 생성한 사용자와 동일하게
db = MySQLdb.connect(db="DB명", host="DB서버주소", user="iot", passwd="1234")
c = db.cursor()

# SQL 명령 실행

c.close()
db.close()
```

