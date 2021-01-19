# MariaDB

- 데이터베이스(DBMS) -- RDBMS -- Oracle, MSSQL, MySQL(Oracle), MariaDB

  ​									 -- NoSQL -- MongoDB, ...



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



## MariaDB 기본 문법

- CRUD: 데이터베이스 생성 -> 테이블 생성 -> 데이터 입력 -> 데이터 조회/활용

- GUI로 할 수 있지만 코드를 이용해서 하기
- 대소문자를 구분하지 않음 / 관례) **키워드는 대문자, 사용자가 지정한건 소문자**
- 가독성을 위해 절단위로 enter, 문장 마지막에;
- 명칭에 공백이 있는 경우 `` 사용, 일반적으로 snake 명명법 사용



### SQL 종류

- DDL
- DML - SELECT
- DCL



### 데이터베이스 모델링

- 정규화 원칙
  1. 모든 행은 식별할 수 있는 값(PK)가 존재해야함
  2. 데이터 중복 x
  3.  ...

- 테이블 설계



### SQL 기본 문법

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

- WHERE

  - 관계연산자(**AND, OR, NOT**) 사용
  - **BETWEEN ~ AND**: 더 자주 사용

  ```mariadb
  SELECT userid, name, addr
  FROM usertbl
  WHERE height BETWEEN 180 AND 183;
  ```

  - **IN()**
  - =: 완전 일치, **LIKE**: 포함 (%, _ 사용)

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

  













## Python

[[Python-mariaDB]](https://github.com/hongjy127/TIL/tree/master/python/database)