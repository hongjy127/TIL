# 	HTML

Hyper Text Markup Language



- 설정

확장팩 > live server (바로 웹으로 보여주는거) (단축키: `Alt+L+O`)



- HTML

  - 컴퓨터에게 보여줄 내용을 구조화 > 계층화
- 내용(HTML)과 스타일(CSS) 분리 > 태그명, 속성 언제 사용하는지 외우기



## 기본 문법

- 들여쓰기는 필수사항은 아니지만 부모-자식 레벨에서 들여쓰기 맞춰줌(동일 레벨에서는 동일 들여쓰기)
- 태그 이름은 대소문자를 구분하지 않지만 보통 소문자 사용(섞어 쓰지는 말기)
- 화이트 문자(엔터, 탭, 공백)가 몇개가 나와도 1개로 처리함.
- <태그></태그>
- <태그/> : 태그의 내용이 없는 경우 단일 태그로 사용



- index.html : 별도의 경로를 주지 않아도 나옴 > 홈페이지



html : 5 선택하면 자동으로 골격이 만들어짐

```html
<!DOCTYPE html>		<!--html 5임을 나타내는 문장-->
<html lang="ko">	<!--en여도 상관 없음-->
<html>
    <!--Browser에게 주는 영역-->
    <head>
        <meta charset="UTF-8">		<!--가장 중요 (파일 저장도 UTF-8로)-->
    	<meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>제목 영역</title>
    </head>
    
    <!--사용자가 볼 수 있는 content-->
    <body>
		본문 영역
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

- 특수문자

  - `&캐릭터명칭;` 으로 표기
  -  `<pre>` : 공백, 특수문자, 줄바꿈을 그대로 표시

  | 특수문자 | 특수문자 처리 |
  | -------- | ------------- |
  | <        | \&lt;         |
  | \>       | \&gt;         |
  | &        | \&amp;        |
  | spacebar | \&nbsp;       |

- 모양관련태그 : CSS등장 이후 쓰지 않음(기능만 남아있음)

- 링크

  ```html
  <!-- URL: 절대, 상대경로 모두 가능 -->
  <a href="URL" target=""></a>
  ```
  
    ```html
  <!-- 이미지링크 -->
    <a href="URL">
        <img src="Image.png"/> 이미지를 클릭하면 링크로
    </a>
    ```
  
- 책갈피 : 문서 내 특정 위치로 이동

  ```html
  <a href="#북마크 이름"></a>
  ...
<a id="북마크 이름"></a>
  

  <!-- 다른 링크로도 가능 -->
<a href="파일경로#북마크 이름"></a>
  
  ```

<!--#은 자기 자신이 됨 -->
  <!-- 아직 링크가 없을 때 (pass같은 개념으로 사용) -->
  <a href="#"></a>
  ```
  
- 목록

  ```html
  <!-- 무순서 목록 -->
  <ul>
      <li>목록1</li>
      <li>목록2
          <ul>
              <li>세부목록1</li>
              <li>세부목록2</li>
          </ul>
      </li>
      <li>목록3</li>
  </ul>
  ```

  ```html
  <!-- 순서 목록 -->
  <ol>
      <li>1</li>
      <li>2</li>
      <li>3</li>
      <li>4</li>
  </ol>
  ```

  ```html
  <!-- 정의형 목록 -->
  <dl>
      <dt>정의한 항목1</dt>
      <dd>설명1</dd>
      <dt>정의한 항목2</dt>
      <dd>설명2</dd>
  </dl>
  ```

- 표

  - `<thead></thead>` `<tbody></tbody>` `<tfoot></tfoot>`
  - `<caption>` : 표 제목 삽입
  - `rowspan` `colspan` : 셀 병합

  ```html
  <table border="" style="">
      <tr>	<!-- row 생성 -->
          <th>표 머리1</th>
          <th>표 머리2</th>
      </tr>
      <tr>
          <td>열 생성1</td>
          <td>열 생성2</td>
      </tr>
  </table>
  ```



### 속성

- 태그에 대해 부가적인 속성을 사용할 때

- 속성이 여러개인 경우 띄어쓰기

    ```html
    <태그명 속성="값">내용</태그명>
    <태그명 속성="값" 속성="값">내용</태그명>
    ```

- 이미지 속성

    ```html
    <img src="path" border="" width="" height="" alt="" title="">
    ```



### 레이아웃

```html
<!-- navigation -->
<nav>메뉴</nav>

<!-- section -- article, header 등을 포함 -->
<section>
    <article>
        <header>
            <h2>부제목</h2>
        </header>
        <p>부세션</p>
    </article>
</section>

<!-- 부가 정보 부분 -->
<aside>
    <h2>부가적 제목</h2>
    <p>부가적 정보</p>
</aside>

<!-- 사이트 정보 부분 -->
<footer>
    <small>사이트 정보 표시</small>
</footer>
```



### 입력 양식 태그

- 폼 태그

  - 알아만 두고 필요할 때 찾아서 쓰기
  - property(단독), attribute( = )

  ```html
  <form name="" action="" method="">
      <input type="" name="" value="">
      <select>
          <option></option>
      </select>`
  </form>
  ```

  - method : get, post
  - type : text, submit, reset, radio, checkbox, button, date(html5부터 제공), number, range, search
  - textarea, legend



### 공간 분할 태그

- `<div>`
  - block 형식으로 분할

- `<span>`
  - inline 형식으로 분할


















