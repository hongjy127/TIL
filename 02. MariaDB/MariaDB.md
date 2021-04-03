# MariaDB

- 데이터베이스(DBMS)
- RDBMS
  - Oracle, MSSQL, MySQL(Oracle), MariaDB
  - NoSQL
  - MongoDB, ...



## MariaDB 설치

- [[MariaDB 설치]](https://mariadb.org/)

  - root 비밀번호 (다른 머신 허용x - 보안)
  - UTF-8 선택, 나머지는 디폴트

  - 서비스 > 알아서 실행됨.

- 테스트 데이터 구축

  - [[테스트 데이터 설치]](http://download.hanbit.co.kr/mariadb/10.3/) -> C:/temp로 압축해제 (간단한 경로로)

    - employees, sqlDB, shopDB 설치

  - MariaDB cmd창
  
    - 항상 ; 찍어주기
    - HeidiSQL로도 가능하지만 경로설정이 필요하므로 MariaDB cmd창에서 실행
    
    ```
    > cd \employees
    > mysql -u root -p
    
    # 외부 sql 파일 실행
    MariaDB[(none)]> source employees.sql
    MariaDB[employees]> show databases;
    # 기본 저장 단위 - 표(table)
    
    exit
    ```



## 사용자 관리

```mariadb
-- 사용자 생성
-- CREATE USER 'userid'@'허용되는 머신 IP' IDENTIFIED BY 'passwd';
CREATE USER 'iot'@'%' IDENTIFIED BY '1234';

-- 권한 부여
-- GRANT ALL PRIVILEGES ON DB명.객체 TO 'userid'@'허용되는 머신 IP';
-- *는 모든 객체를 말함, ``자동완성 조심
GRANT ALL PRIVILEGES ON sqlDB.* TO 'iot'@'%';
GRANT ALL PRIVILEGES ON employees.* TO 'iot'@'%';
```



- 데이터베이스 복사

 ```
-- 복사
mysqldump -u root -p db_name > db_name.sql
> 비밀번호 치는 란이 나옴

-- 다운
db_name.sql 폴더에서
mysql -u root -p db_name < db_name.sql
 ```





## MariaDB 기본 문법

- CRUD: 데이터베이스 생성 -> 테이블 생성 -> 데이터 입력 -> 데이터 조회/활용

- GUI로 할 수 있지만 코드를 이용해서 하기
- 대소문자를 구분하지 않음 / 관례) **키워드는 대문자, 사용자가 지정한건 소문자**
- 가독성을 위해 절단위로 enter, 문장 마지막에;
- 명칭에 공백이 있는 경우 `` 사용, 일반적으로 snake 명명법 사용



### 데이터베이스 모델링

- 정규화 원칙
  1. 모든 행은 식별할 수 있는 값(PK)가 존재해야함
  2. 데이터 중복 x
  3. ...
- 테이블 설계



### SQL 종류

- DDL
- DML - **SELECT**, INSERT, UPDATE, DELETE
- DCL



### 데이터 형식

- 숫자: INT, BIGINT, FLOAT, DECIMAL, ...
- 문자: CHAR, VARCHAR, LONGTEXT, LONGBLOB, ...
  - LONGTEXT: 소설, 게시판 글 등
  - LONGBLOB: 이미지, 동영상 데이터 등

- 날짜, 시간: DATE, DATETIME, ...



- 데이터 형 변환

```mariadb
CAST(표현식 AS 데이터형식[(길이)])
CONVERT(표현식, 데이터형식[(길이)])

-- 자주사용
SELECT CAST('2022/12/12' AS DATE);
SELECT CAST('2022@12@12' AS DATE);
```



### SQL

```mariadb
-- 한 줄 주석
/*
여러 줄 주석
도구 > 환경설정 > 단축키 > SQL > 주석설정/해제 > 원하는 키로 설정
*/
```



- 명칭

```mariadb
USE employees;	-- 왼쪽 목록에서 선택해도 동일
DESC titles;	-- discribe: 테이블 구조 출력

DESC employees.titles;
```



- 데이터베이스

```mariadb
DROP DATABASE IF EXISTS sqlDB;	-- 삭제
CREATE DATABASE sqlDB;			-- 생성
SELECT 필드 목록 [AS] 이름		-- 내용 출력
FROM 테이블명
[ WHERE 조건 ]
[ GROUP BY 컬럼명 ]
[ HAVING 조건 ]
[ ORDER BY 컬럼명];
```



#### SELECT

가장 자주 사용

- WHERE

  - 관계연산자(**AND, OR, NOT**) 사용
  - **BETWEEN ~ AND**: 더 자주 사용

  ```mariadb
  SELECT userid, name, addr
  FROM usertbl
  WHERE height BETWEEN 180 AND 183;
  ```

  - **IN()**
  - =: 완전 일치
  - **LIKE**: 포함 (%, _ 사용)

  ```mariadb
  SELECT userid, name, addr
  FROM usertbl
  WHERE name LIKE '%%';
  ```

  

- 서브쿼리

  - FROM/WHERE 절에 SELECT문 제시
  - SELECT문은 단일행 쿼리, 멀티행인 경우 ANY/ALL/SOME 사용
  - () 안에 작성

  ```mariadb
  SELECT name, height FROM usertbl
  	WHERE height > (SELECT height FROM usertbl WHERE name = '김경호');
  ```

- 정렬

  - ASC: 오름차순, default
  - DESC: 내림차순

  ```mariadb
  SELECT name, height FROM usertbl ORDER BY height DESC, name ASC;
  ```

- DISTINCT: 중복 제거

- LIMIT: 출력 개수 제한

  - ORDER BY와 같이 자주 사용

  ```mariadb
  SELECT emp_no, hire_date FROM employees
  	ORDER BY hire_date ASC
  	LIMIT 0,5; -- LIMIT 시작위치, 개수
  -- web(pagination)
  -- LIMIT (n-1)c, c
  ```

- 테이블 복사

  - KEY 제약조건은 복사되지 않음

  ```mariadb
  CREATE TABLE 새로운 테이블명 (SELECT 복사할 열 FROM 기본테이블명);
  ```

- GROUP BY

  - 특정 열에 대해 동일한 값을 가지는 행들을 하나의 행으로 처리

  | 집계함수        |                           |
  | --------------- | ------------------------- |
  | AVG()           | 평균                      |
  | MIN()           | 최솟값                    |
  | MAX()           | 최댓값                    |
  | COUNT()         | 행의 개수                 |
  | COUNT(DISTINCT) | 행의 개수 (중복은 한개만) |
  | STDEV()         | 표준편차                  |
  | VAR_SAMP()      | 분산                      |

  ```mariadb
  SELECT userID, SUM(amount) AS '총 구매 개수'	-- column 이름
  FROM buyTBL
  GROUP BY userID;
  
  -- page 셀 때 자주 사용
  SELECT COUNT(*) FROM userTBL;
  ```

- HAVING

  - GROUP BY에서 필터링

  ```mariadb
  SELECT userID, SUM(amount) AS '총 구매 개수'	-- column 이름
  FROM buyTBL
  -- WHERE SUM(amount) > 1000	-- GROUP BY 이전
  GROUP BY userID
  HAVING SUM(amount) > 1000;
  ```

- AUTO_INCREMENT

  - 값을 제시하지 않은 경우 자동 증가 값으로 추가 (주로 PK로 사용)

  ```mariadb
  CREATE TABLE testbl(
      id int AUTO_INCREMENT PRIMARY KEY,
      userID char(3)
  	)
  	
  -- 잘 안씀
  ALTER TABLE testbl AUTO_INCREMENT=100;
  ```



#### INSERT

```mariadb
INSERT INTO 테이블명[(
    column1,
    column2,
	...)]
VALUES ('value1', 'value2', ...)

-- 대량의 데이터를 넣을 때
INSERT INTO 테이블명[(
    column1,
    column2,
	...)]
SELECT문;
```



#### UPDATE

```mariadb
UPDATE 테이블명
SET column1='value1', column2='value2', ...
[WHERE 조건];	-- 없으면 전체 행 수정
```



#### DELETE

```mariadb
DELETE FROM 테이블명
[WHERE 조건];	-- 없으면 전체 행 삭제
```



#### 내장함수

- 제어흐름함수

```mariadb
-- IF(조건, 참, 거짓)
SELECT IF (100>200, '참', '거짓')

-- IFNULL(수식1, 수식2) -- 보통 col명이 들어옴
-- 수식1이 NULL이 아니면 수식1 리턴, NULL이면 수식2 리턴
SELECT IFNULL (100, 'NULL')

-- NULLIF(수식1, 수식2)

-- CASE ~ WHEN ~ ELSE ~ END
SELECT
 CASE column명
  WHEN ~ THEN ~
  ELSE ~
 END;
```

- 문자열

    ```mariadb
    SELECT
    BIT_LENGTH(문자열),
    CHAR_LENGTH(문자열),
    LENGTH(문자열);	-- bite
    ```
    - 문자열 결합
    ```mariadb
    -- CONCAT 안에 문자, 숫자가 같이 들어오면 알아서 형변환이 일어나지만 이러한 연산은 하지 않는 것이 좋음.
    CONCAT(문자열1, 문자열2, ...)	-- 문자열 결합
    CONCAT_WS(구분자, 문자열1, 문자열2, ...) -- 구분자로 문자열 결합	
    ```
    - INSTR
    ```mariadb
    INSTR(기준 문자열, 부분 문자열)	-- index 얻음
    ```

    - INSERT

    ```mariadb
    -- 위치에 길이만큼빼고 삽입할 문자열을 넣음
    INSERT(기준문자열, 위치, 길이, 삽입할 문자열)
    ```

    - LOWER, UPPER
    - SUBSTRING

    ```mariadb
    SUBSTRING(문자열, 시작위치, 길이)
    SUBSTRING(문자열 FROM 시작위치 FOR 길이)
    ```

- 날짜 및 시간

    - NOW(), SYSDATE()
    - YEAR(), MONTH(), DAY()
    - DATE(), TIME()

    ```mariadb
    SELECT DATE(NOW()), TIME(NOW());	-- 지금 날짜, 시간
    ```



#### JOIN

- 1:1, 1:N, N:M 관계



##### INNER JOIN (내부 조인)

- 공통컬럼을 기반으로 결합(PK-부모, FK-자식테이블)
- 값이 있는 행을 대상으로(외부조인과 다름)
- 열목록을 작성할 때 테이블명 다 써주기(테이블명.열목록, table도 alias 가능)

```mariadb
SELECT 열목록
FROM 첫번째 테이블
	INNER JOIN 두번째 테이블
	ON 조인될 조건
[WHERE 검색 조건]
```

##### OUTER JOIN (외부 조인)

- 값이 없어도 모든 행에 대해 조인

```mariadb
SELECT 열목록
FROM 첫번째 테이블(LEFT 테이블)
	<LEFT/RIGHT/FULL> OUTER JOIN 두번째 테이블(RIGHT 테이블)
	ON 조인될 조건
[WHERE 검색 조건]
```

##### CROSS JOIN (상호 조인)

- 가능한 모든 조합

##### SELF JOIN (자체 조인)

- Alias를 두 개 배정하여 논리적으로 2개의 테이블을 만듦.

---

#### 테이블

- 생성/삭제

```mariadb
-- 부모테이블인 경우 자식테이블을 삭제해야 삭제가 됨.
-- 일반적으로 개발시 외래키를 걸지않음(테스트 하기 번거로움)

DROP TABLE if EXISTS buytbl, usertbl;
CREATE TABLE usertbl
(	컬럼명		데이터타입 	[제약조건],
 ...
);
```

- 수정

```mariadb
ALTER TABLE 테이블명
수정사항;
```

- 제약조건

```mariadb
-- CONSTRAINT로 제약조건에 명칭 부여 가능
-- 제약조건명칭 관례: 제약조건타입_테이블명_컬럼명
CONSTRAINT 제약조건 제약조건명칭(컬럼명)

-- 제약조건
PRIMARY KEY
FOREIGN KEY(필드명) REFERENCES 참조테이블명(참조테이블_필드명)
UNIQUE
CHECK
DEFAULT
NULL / NOT NULL
AUTO_INCREMENT
```

#### 뷰

- SELECT문의 결과를 하나의 테이블로 봄
- SELECT문이 복잡한데 자주 써야할 때 사용 (보통 join) 
- 생성

```mariadb
CREATE VIEW 뷰이름
AS
SELECT 쿼리
```

- 삭제

```mariadb
DROP VIEW 뷰이름
```

#### 인덱스

- 정보를 빠르게 찾기 위함, 검색속도 향상
- 생성

```mariadb
-- 이 컬럼에 대한 인덱스를 만들겠다
CREATE INDEX 인덱스명
ON 테이블명(컬럼명, ...);
```

- 삭제

```mariadb
DROP INDEX 인덱스명 ON 테이블명;
```



## Python

[[Python-mariaDB]](https://github.com/hongjy127/TIL/tree/master/python/database)