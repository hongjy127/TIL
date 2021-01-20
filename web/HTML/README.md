# HTML

- 설정

확장팩 > live server (바로 웹으로 보여주는거) (단축키: `Alt+L+O`)



- HTML

  - 컴퓨터에게 보여줄 내용을 구조화 > 계층화

  - 내용(HTML)과 스타일(CSS) 분리 > 태그명, 속성 언제 사용하는지 외우기



## 기본 문법

- 들여쓰기는 필수사항은 아니지만 부모-자식 레벨에서 들여쓰기 맞춰줌(동일 레벨에서는 동일 들여쓰기)

- `Ctrl+K+F` : 들여쓰기 단축키 (vscode)

- 태그 이름은 대소문자를 구분하지 않지만 보통 소문자 사용(섞어 쓰지는 말기)

- 화이트 문자(엔터, 탭, 공백)가 몇개가 나와도 1개로 처리함.



html : 5 선택하면 자동으로 골격이 만들어짐

```html
<!DOCTYPE html>  <!--html 5임을 나타내는 문장-->
<html lang="ko">
<html>
    <!--Browser에게 주는 영역-->
    <head>
        <meta charset="UTF-8">	<!--가장 중요 (파일 저장도 UTF-8로)-->
    	<meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title></title>
    </head>
    
    <!--사용자가 볼 수 있는 content-->
    <body>

    </body>
</html>
```



### 태그

```html
<!-- 주석 -->
<h1>제목1</h1>
<h2>제목2</h2>
<h3>제목3</h3>
<h4>제목4</h4>
<h5>제목5</h5>
<h6>제목6</h6>
<hr>문서의 구분선</hr>
<p>단락 구분</p>
<strong>중요한 문장</strong>
<br>줄바꿈
```



### 속성

태그에 대해 부가적인 속성을 사용할 때

속성이 여러개인 경우 띄어쓰기

```html
<태그명 속성="값">내용</태그명>
```



레이아웃





특수문자

&캐릭터명칭;

기본규칙 깨고 그대로 나타내라는 태그

 ```<pre>```



모양관련태그 -> CSS등장 이후 쓰지 않음.



링크

`<a href="URL"></a>`

이미지링크

```html
<a href="ex03.html">
                <img src="profileImage.png" width="500" height="500"/> 홍이의 곱슐랭
            </a> <br>
```



책갈피

자기자신

다른파일

#의 의미





index.html

별도의 경로를 주지 않아도 나옴.

-> 홈페이지



material icon theme







