# Python



> ## Contents
>
> 1. [개발환경 구축](#01.-개발환경-구축)
>
> 2. [기본 문법](#02.-기본-문법)
> 	- [기본 구조](#기본-구조)
> 	- [변수](#변수)
> 	- [타입](#타입)
>	- [연산자](#연산자)
>	- [조건문](#조건문)
> 	- [반복문](#반복문)
> 	- [함수](#함수)
>	- [문자열 관리](#문자열-관리)
>	- [리스트와 튜플](#리스트와-튜플)





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



---



### 타입 [(실습파일)](https://github.com/hongjy127/TIL/blob/master/python/lec03.ipynb)

#### 수치형

##### 정수형

- 크기 제한이 없음 (값에 따라 크기 자동 조절)

- 진법

| 진법                | 접두 | 사용 가능한 숫자 |
| ------------------- | ---- | ---------------- |
| 16진법(hexadecimal) | 0x   | 0~9, a~f         |
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
- `round(숫자, 반올림 자리수)` : 실수 반올림
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
def 함수명(인수 목록):
    """"도움말 제공(가장 첫 줄, 삼중따옴표로 지정)""""
    명령 블록
    return 리턴값
    
함수명(인수 목록)  # 함수 호출
```

- 기본값 지정

```python
def 함수명(인수명 = 기본값):
    명령 블록
    return 리턴값    
```

- 가변 인수
  - 인수의 수가 고정되지 않고, 호출 시 원하는 만큼 지정할 수 있음
  - 함수에서는 튜플로 변수를 받음
  - 하나만 사용, 일반 인수 뒤에만 사용

```python
def 함수명(*인수명):
    명령 블록
    return 리턴값    
```

- 키워드 가변 인수
  - **로 지정한 타입은 dictionary
  - 일반 인수, 가변 인수, 키워드 가변 인수 순서로 배치

```python
def 함수명(**인수명):
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

문자열은 순서를 가지는 콜렉션 -> sequence

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

- Python2에서 주로 사용(알아만두기)

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



### 리스트와 튜플 [(실습파일)]()



---










