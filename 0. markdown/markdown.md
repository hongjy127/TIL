# Markdown

[TOC]

## settings

 파일 > 환경설정 > 이미지> 경로이미지복사 선택 & 가능하다면 상대적 위치 사용



### 단축키

Ctrl + /



## Markdown 문법

### Headers

```
# H1
## H2
### H3
#### H4
##### H5
###### H6
```



### BlockQuote

```
> BlockQuote
> > BlockQuote
> > > BlockQuote
```

> BlockQuouote
> > BlockQuote
> >
> > > BlockQuote



### 목록

- 순서

```
1. 1번
2. 2번
3. 3번 내림차순 정렬
```

1. 1번
2. 2번
3. 3번 내림차순 정렬



- 순서 없음 (`-`, `+`, `*` 모두 가능)

```
- 목록
  - 목록
    - 목록
    
* 목록
  * 목록
    * 목록

+ 목록
  + 목록
    + 목록
```

- 목록
  - 목록
    - 목록
    
* 목록
  * 목록
    * 목록

+ 목록
  + 목록
    + 목록



### Code Block

```
​```
This is a code block
​```
```

```
This is a code block
```



```
​```python
def function():
	pass
	return
​```
```

```python
def function():
	pass
	return
```



### 수평선

페이지 나눌 때 주로 사용

```
---
---
```

---

---



### Link

`[Inner link](#inner-link)`

[Inner link](#link)

- 뒤는 소문자로 쓰기
- 띄어쓰기는 -로 구분
- #뒤에 띄어쓰기 하지 말기

`[URL](<URL>)`

[markdown](https://github.com/hongjy127/TIL/blob/master/markdown/markdown.md)



