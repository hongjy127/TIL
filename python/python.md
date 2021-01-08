

# Python



> ## Contents
>
> 1. [개발환경 구축]
>
> 2. [기본 문법]
> 	- 기본 구조
> 	- 변수
> 	- 타입
> 	- 연산자
> 	- 조건문
> 	- 반복문
> 	- 함수
> 	- 문자열 관리
> 	- 리스트와 튜플
> 	- 사전과 집합
> 	- 컬렉션 관리
> 	- 표준 모듈





## 01. 개발환경 구축

- [[파이썬 설치]](https://www.python.org/)

- [[아나콘다 설치]](https://www.anaconda.com/) - 설치할 때 PATH 추가

  (아나콘다로 버전, 라이브러리를 편하게 관리)

### vscode - python 설정

- 확장> Korean Language Pack, Python, Code Runner 설치
- 관리>설정>Code-runner:Run In Terminal에 체크





## 02. 기본 문법



### 기본 구조 [(실습파일)](https://github.com/hongjy127/TIL/blob/master/python/lec01.ipynb)

- 들여쓰기 필수
- 대, 소문자 구분
- #이후는 주석


```python
help(함수명)  # 도움말
```
- 출력
```python
print(출력 내용)
print(출력 내용, sep=구분자, end=끝문자)  # 출력
```

- 입력
  - input 함수는 문자열 타입으로 리턴

```python
variable = input('질문내용')
```



---



### 변수 [(실습파일)](https://github.com/hongjy127/TIL/blob/master/python/lec02.ipynb)

- 값을 저장하고 있는 메모리
- 알파벳, 밑줄, 숫자로 구성 / 첫 글자는 숫자 사용 불가 / 대소문자 구분
- 키워드 사용 불가
- 대입하는 값의 타입이 고정되어있지 않음



###### 참고) 변수 표기법

snake 표기법 : subject_total

CamelCase : subjectTotalSum (Java, JavaScript)

케밥 표기법 : subject-total (HTML)

필요하지만 쓰이지는 않는 변수는 _로 나타냄



---



### 타입 [(실습파일)](https://github.com/hongjy127/TIL/blob/master/python/lec03.ipynb)

#### 수치형

##### 정수형

- 크기 제한이 없음 (값에 따라 크기 자동 조절)

- 진법

| 진법                | 접두 | 사용 가능한 숫자 |
| ------------------- | ---- | ---------------- |
| 16진법(hexadecimal) | 0x   | 0-9, a-f         |
| 8진법(octal)        | 0o   | 0~7              |
| 2진법(binary)       | 0b   | 0, 1             |

##### 실수형

##### 복소수형

- 실수부 + 허수부j



#### 문자열

- 한 줄로 표현 - 큰 따옴표(" "), 작은 따옴표(' ')로 묶음.
- 여러 줄로 표현 - 삼중따옴표(""" """)
- 문자열 확장(문자 이스케이프)

| 확장열 | 설명        |
| ------ | ----------- |
| \n     | 개행        |
| \t     | 탭          |
| \\"    | 큰 따옴표   |
| \\'    | 작은 따옴표 |
| \\\    | \문자       |

- 문자 코드

```python
ord(문자열)  # 문자열 -> 숫자
chr(숫자)  # 숫자 -> 문자열

# 순서(문자열을 정렬할 때 사용)
# ABC ... Z
# 특수문자
# abc ... z
```



#### 컬렉션

##### List

- [ , , ]
- 변수이름으로 list 쓰면 안됨

```list()``` : 리스트로 만들어줌

##### Tuple

- ( , , )

- List와 다른 점은 읽기 전용.

- List는 내용이 변할 수 있지만 tuple은 값이 고정됨.

##### dict

- key와 value가 쌍으로 관리



#### 그 외

##### boolean

- True / False

##### None

- 어떠한 값도 없음

|                             거짓                             |   참   |
| :----------------------------------------------------------: | :----: |
| False, None, 0, 비어있는 문자열(""), 비어있는 컬렉션([], ()) | 나머지 |




---



### 연산자 [(실습파일)](https://github.com/hongjy127/TIL/blob/master/python/lec04.ipynb)

#### 대입 연산자

- 값을 지정해 변수에 저장하는 것

#### 산술연산자

- +, -, *, /
- ** : 거듭제곱
- // : 정수 나누기
- % : 나머지

#### 복합 대입 연산자

- +=, -+, *=

#### 비교 연산자

| 연산자 | 설명                        |
| ------ | --------------------------- |
| ==     | 같다                        |
| !=     | 다르다                      |
| <      | 좌변이 우변보다 작다        |
| >      | 좌변이 우변보다 크다        |
| <=     | 좌변이 우변보다 작거나 같다 |
| >=     | 좌변이 우변보다 크거나 같다 |

#### 논리 연산자

| 연산자 | 설명                       |
| ------ | -------------------------- |
| and    | 두 조건이 모두 참이다      |
| or     | 두 조건 중 하나라도 참이다 |
| not    | 조건을 반대로 뒤집는다     |

#### 문자열 연산

- `'str' + 'str'` : concatenate
- `'str' * 정수` : str을 정수만큼 반복
- `str()` : 문자열로 변환
- `int()` : 정수로 변환
- `int(문자열, 진법)` : 문자열를 10진법으로 변환 (진법의 default 값이 10이라 10진법으로 바꿔줌.)

#### 타입 변환

- `float()` : 실수로 변환
- `round(숫자[, 반올림 자리수])` : 실수 반올림
- `bool()` : boolean으로 변환
- `list()` : list로 변환
- `tuple()` : tuple로 변환
- `dict()` : dictionary로 변환



---



### 조건문 [(실습파일)](https://github.com/hongjy127/TIL/blob/master/python/lec05.ipynb)

#### if 문

- 조건은 비교, 논리 연산자를 사용

```python
if 조건: 명령  # 단일 라인인 경우만 가능
```

```python
if 조건:
    명령문 1  # 모두
    명령문 2  # 들여쓰기
```

```python
if 조건:
    명령 블록
else:  # if문의 조건이 False인 경우 실행 
    명령 블록
```

```python
if 조건1:
    명령 블록
elif 조건2:
    명령 블록
else:
    명령 블록
```



---



### 반복문 [(실습파일)](https://github.com/hongjy127/TIL/blob/master/python/lec06.ipynb)

#### while문

- 조건이 참인 동안 명령 블록을 실행
- 무한루프가 되지 않게 조건에 변수를 사용

```python
while 조건:
    명령 블록
```

#### for문

- 컬렉션의 요소를 하나씩 꺼내 명령 블록을 실행
- `range(시작, 끝, 증가값)` 을 많이 사용함

```python
for 제어변수 in 컬렉션:
    명령 블록
```

- 이중루프

```python
for 제어변수1 in 컬렉션1:
    명령 블록1
    for 제어변수2 in 컬렉션2:
        명령 블록2
```



##### break

- 반복문을 벗어나게 함

##### continue

- 이후 명령을 실행하지 않고 다음 반복을 시작



---



### 함수 [(실습파일)](https://github.com/hongjy127/TIL/blob/master/python/lec07.ipynb)

- 함수정의

```python
def funcname(parameter_list):
    """
    docstring
    """
    pass
    return 리턴값
    
함수명(인수 목록)  # 함수 호출
```

- 람다함수
  - 함수 이름이 없음, 재사용하지 않음(functional programming)

```python
# lambda 함수
lambda parameter_list: expression
```

- 기본값 지정

```python
def funcname(인수명 = 기본값):
    명령 블록
    return 리턴값    
```

- 가변 인수
  - 인수의 수가 고정되지 않고, 호출 시 원하는 만큼 지정할 수 있음
  - 함수에서는 튜플로 변수를 받음
  - 하나만 사용, 일반 인수 뒤에만 사용

```python
def funcname(*인수명):
    명령 블록
    return 리턴값    
```

- 키워드 가변 인수
  - **로 지정한 타입은 dictionary
  - 일반 인수, 가변 인수, 키워드 가변 인수 순서로 배치
    - `funcname(인수1, 인수2, *가변인수, **키워드가변인수1, **키워드가변인수2)`
  - 키워드 가변 인수는 여러개 사용 가능

```python
def funcname(**인수명):
    명령 블록
    return 리턴값    
```

#### 변수

- 지역 변수 : 함수 내에서만 사용

- 전역 변수 : 어디서든 접근 가능한 변수

  `global 변수`

- stack, call by value

#### pass

- 아무것도 안하고 넘어감
- 함수는 코드 블럭이 있어야 하기 때문에 실제 구현을 나중으로 미룰 때 pass 지정



---



### 문자열 관리 [(실습파일)](https://github.com/hongjy127/TIL/blob/master/python/lec08.ipynb)

문자열은 순서를 가지는 컬렉션 -> sequence

#### index

- 문자열[정수] : 0부터 인덱싱
- 문자열[-정수] : 끝에서부터 인덱싱

#### slicing

- 문자열[begin : end : step]

#### 검색

- `word.find(str)` : str을 word 에서 찾아 index를 반환, 없으면 -1 반환
- `word.rfind(str)` : str을 word 뒤에서부터 찾아 index를 반환, 없으면 -1 반환
- `word.index(str)` : find()와 동일, 없으면 예외 발생
- `word.count(str)` : str이 word에서 몇 번 등장하는지 리턴

#### 조사

모두 boolean으로 return

- `word in str`
- `word not in str`
- `word.startswith(str)`
- `word.endtswith(str)`

#### 기타 메서드

모두 boolean으로 return

- isalpha
- islower
- isupper
- isspace
- isalnum
- isdecimal
- isdigit
- isnumeric
- isidentifier
- isprintable

#### 변경

문자열은 불변객체로 다른 값으로 바꾸지 못함 -> 원본을 읽어 새로운 문자열을 만들어줌

- .lower()
- .upper()
- .swapcase() : 대문자 <-> 소문자
- .capitalize() : 첫글자 대문자, 나머지 소문자로
- .title() : 모든 단어의 첫글자 대문자, 나머지 소문자로
- .strip() : 좌, 우 공백 제거
- .lstrip() : 왼쪽 공백 제거
- .rstrip() : 오른쪽 공백 제거

#### 분할

- .split(구분자) : 구분자 기준으로 분리하여 리스트로 리턴, 구분자 기본값은 공백
- .splitlines()
- 결합문자열.join(문자열)

#### 대체

- .replace(기존문자열, 대체문자열)

#### 포맷팅

- Python2에서 주로 사용(알아만 두기)

| 포맷 |          |
| ---- | -------- |
| %d   | 정수     |
| %f   | 실수     |
| %s   | 문자열   |
| %c   | 문자하나 |
| %h   | 16진수   |
| %o   | 8진수    |
| %%   | 문자     |

- Python3에서 주로 사용

`"{:포맷문자열}".format(값)`

- Python3.7부터 지원하는 새로운 방법(f-string)

`f"{값}"`

`f"{값:포맷문자열}"`

###### ex)

`f"이름: {name:3s}, 나이:{age:3d}, 키: {height:.1f}"`



---



### 리스트와 튜플 [(실습파일)](https://github.com/hongjy127/TIL/blob/master/python/lec09.ipynb)

#### 리스트

- [ , , ]
- list() : 리스트로 만들기
- sequence
- 안에 들어가는 데이터 타입은 섞여도 상관 없음
- 문자열과 동일한 문법(index, slicing, +, *)
- comprehension

`[수식 for 변수 in 리스트 if 조건]` : 리스트 범위를 순회하며 변수를 추출하여 수식을 생성

##### 삽입

- .append(값) : 리스트의 끝에 값을 추가 (자주사용)
- .insert(위치, 값) : 지정한 위치에 값을 삽입

##### 확장

- .extend() : 원본에 확장
- +는 새로운 값에 대입 가능

##### 삭제

- .remove(값) : 값을 찾아 첫번째 요소 제거
- del(리스트(index)) : 지정한 인덱스 제거
- 리스트[시작:끝] = [] : 지정한 범위 제거
- .pop() : 리스트 끝 요소를 삭제하고, 삭제한 요소를 리턴
- .pop(인덱스)

##### 검색

- .index(값) : list에서 값을 찾아 index를 반환, 없으면 예외 발생
- .count(값) : 값이 리스트에 몇 번 나오는지 계산
- 값 in 시퀀스
- 값 not in 시퀀스

##### 정렬

- sort(\[reverse=True][key=키에 적용할 함수]) : 리스트를 정렬(디폴트 오름차순), 메서드
- .reverse() : 리스트의 순서를 역으로, 메서드
- sorted(시퀀스) : 정렬함수

.

#### 튜플

- ( , , ) (괄호 생략 가능)
- tuple() : 튜플로 만들어줌

- 리스트보다 속도가 빠름
- indexing, slicing 가능
- indexing으로 수정, 삭제 불가능 (읽기전용)

- unpacking, swap, return 튜플 (함수는 값을 하나만 리턴 가능, 튜플 하나를 리턴하는건 가능)



---



### 사전과 집합 [(실습파일)](https://github.com/hongjy127/TIL/blob/master/python/lec10.ipynb)

#### dictionary

```python
dic = {
    key1:value1,
    key2:value2
    key3:value3
}

# key:value(요소)를 entry라고 부름
# entry의 순서는 의미가 없음

dic[key1]  # value1, key가 없으면 예외발생
dic.get(key1 [, 기본값])  # value1 (예외 발생 x)
dic.keys()  # key 목록
dic.values()  # value 목록
dic.items()  # (key, value) 튜플 목록

dic.update(dic2)  # 사전 합치기(주로 web에서 쓰임), 키가 중복되면 dic2가 살아남음
```

- key는 중복을 허용하지 않음(집합개념)
- value는 중복 가능

- 이중list(tuple)는 dict로 바꿀 수 있음

```python
# 이런 꼴만 dict로 변경
li = [
    [key1, value1],
    [key2, value2],
    [key3, value3]
]

dic = dict(li)  # list -> dict
```



- list vs. dict

  - 검색의 성능이 필요하면 dict

    list에서 요소를 찾으려면 (for ... if ...) 루프를 돌아야함 -> O(n) (find, index 메소드도 이만큼)

    숫자가 정렬이 되어있다면 -> O(logn)

    검색이 필요 없음(한번에 알아냄) -> O(1) : dict



#### 집합

- {value1, value2, ...}
- `set(sequence)`
- 중복을 허락하지 않음



- .add(value)
- .remove(value)



##### 집합 연산

| 연산          | 기호 | 메소드               |
| ------------- | ---- | -------------------- |
| 합집합        | \|   | union                |
| 교집합        | &    | intersection         |
| 차집합        | -    | difference           |
| 배타적 차집합 | ^    | symmetric_difference |



---



### 컬렉션 관리 [(실습파일)](https://github.com/hongjy127/TIL/blob/master/python/lec11.ipynb)

#### 컬렉션 관리 함수

- eunmerate(seq [, start])

```python
# index를 같이 출력할 때 자주 사용
for num, i in enumerate(seq):
    print(num, i)
```

- zip

```python
# 위치기반으로 묶어 튜플로 반환
# 개수가 다르면 짧은 시퀀스에 맞춤
# zip 객체로 return, for문에 사용할 수 있음

for num, i in zip(seq1, seq2):
    print(num, i)
```

```python
# list(zip(seq1, seq2))로 바꿔 사용가능하나 한번만 loof 사용 가능
# 계속 사용하려면 보통 list로 바로 바꿔서 사용함

zip_list = list(zip(seq1, seq2))  # list로 변환
zip_dict = dict(zip(seq1, seq2))  # dictionary로 변환
```

- functional programming : 함수를 매개변수로 전달하는 방식
  - filter(판정함수, seq) : seq로 리턴
  - map(함수, seq) : seq가 여러개라면 길이가 동일
    - any(seq), all(seq)과 자주 쓰임
  - sort

#### 컬렉션의 사본

- reference(참조형)
  - list, 문자열(숫자, boolean 빼고 다)
  - heap에 저장됨
  - 참조값은 수정할 수 없음(C에서만 가능)
- 기본형
  - 숫자, boolean
- 참조형의 복사본
  - seq.copy()
  - 참조도 복사하게 됨.
  - 깊은 복사는 import copy
  - is : 같은 참조인지 조사 (== : 같은 데이터인지 조사)



---



### 표준 모듈 [(실습파일)](https://github.com/hongjy127/TIL/blob/master/python/lec12.ipynb)

- 파이썬에서 제공
- 내가 직접 만드는거
- 다른사람(외부 라이브러리)

```python
import 모듈 [as alias]  # 모듈이 너무 길면 alias를 붙여 줄이기
from 모듈 import funcname1, funcname2 ...  # 모듈에서 일부 함수만 가져옴
```

- 자주사용

```python
import math

math.ceil(x) # 올림
# ex) 페이지 수
```

```python
import time  # IoT에서 자주 사용

# I/O 작업이 오래 걸리니 최대한 줄이고/작업을 한번에
# buffer : 시간에 대한 완충
time.time()

time.localtime()
time.sleep(sec)  # Thread
time.strftime  # 시간정보(time)를 문자열(str)로 포멧팅(f)
```

```python
import random

random.random()  # [0,1)사이의 난수
random.randint(begin,end)  # end 포함
random.randrange(begin,end)  # end 미포함
```

```python
import sys

sys.exit(0)  # 숫자는 보통 개발자가 정하지만 관례로 0: 정상적인 종료 상태
```



---



### 예외 [(실습파일)](https://github.com/hongjy127/TIL/blob/master/python/lec13.ipynb)



- try/except : 쓰는 습관 들이기
  - 예외 종류: NameError, ValueError, zeroDevisionError, IndexError, TypeError

```python
try:
	명령 블록(내가 원래 하고자 하는것)
except 예외 as 변수:
    오류 처리문
else:
    명령 블록(예외가 발생할 때)
```

- raise : 개발자에 의해 임의로 예외를 발생

```python
raise 예외
```

- finally : 예외와 관련 없이 항상 호출(cleanup 수행)
- assert 조건, 메세지 : 조건이 True이면 통과, False이면 예외발생



---



### 파일 [(실습파일)](https://github.com/hongjy127/TIL/blob/master/python/lec14.ipynb)

- open(path, mode) : 파일 열기 / close() : 파일 닫기
  - 항상 `with open() as f`: 형식으로 작성하기

| 모드 |                                            |
| ---- | ------------------------------------------ |
| r    | 읽기, 파일이 없는 경우 예외 발생           |
| w    | 쓰기, 파일이 없으면 새로 생김              |
| a    | 추가                                       |
| x    | 쓰기용으로 여나 기존 파일이 있는 경우 실패 |
| t    | text 모드로 열기                           |
| b    | binary 모드로 열기(숫자)                   |

- .write() : 줄바꿈 없음
- 파일읽기
  - .read([n개의 내용])
  - .readline() : 한 줄 읽기 (각 라인 끝에 \n이 들어있음)
  - .readlines() : 전체 라인 읽기 (각 라인 끝에 \n이 들어있음)
  - EOF (end of file)

- seek(위치, 기준) : 입출력 위치
  - 0: 파일의 처음 위치
  - 1: 현재 위치
  - 2: 파일의 끝 위치

#### pickle 모듈

- 파이썬의 자료형(python에서만 사용 가능)
- 저장하기
  - `pickle.dump(data, file)`
  - file : "bw"로 오픈한 파일 객체
- 로드하기
  - `pickle.load(file)`
  - file: "br"로 오픈한 파일 객체



---



### 주의할 점들

- 되도록 함수로 만들어서 사용
- 함수는 단일책임의 원칙
- 변수 만들 때 관례
  - 변수명: 명사
  - 함수명: 동사_목적어

- hard coding  피하기 (전역변수는 최대한 피하기)
  - input
  - sys.argv
  - config.ini

- \ufeff - ms의 utf-8에 이게 항상 붙음







