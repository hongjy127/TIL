# Git

> Contents
>
> git 명령어
> git 실습




## Git이란?

Version Control System




## Git 명령어

- git 설치 (https://git-scm.com/)

- git book (https://git-scm.com/book/ko/v2)



### Settings

- 컴퓨터마다 한 번씩만 설정하는 것

`git config --global user.name "이름"`

`git config --global user.email "이메일"`

---

- Project 생성 시 설정하는 것

1. `$ mkdir <dir name>`

   `$ cd <dir name>`

2. `$ touch .gitignore`

3. `$ touch README.md`

4. `$ git init`

---

- Github에 백업

1. `$ git init` 이 되어있는 상태 (로컬 저장소)

2. `$ git add .`

3. `$ git commit -m 'COMMIT MESSAGE'`

4. Github에 remote 저장소 만들기 (new repository)

5. `$ git remote add origin <URL>`

6. `$ git push origin master`

---

- 다운로드
	- `$ git pull origin master`
	- `$ git clone <URL>`

---

- Github로 협업하기 (branch)










## Git 실습


```
$ cd learn_git

$ git init
```

: learn_git 폴더를 repository (repo, 저장소) 로 만듦.
: ls -a 을 실행하면 .git/이 생김.

주의)

`$ git init` 를 home 폴더에 적용하면 안됨.

---

`$ git status ` : 현재 상태 보기

`$ git log` : commits 요약

---

### add/commit

`$ git add FILE/DIRECTORY_NAME` : 등록 or tracking

`$ git add .`  : directory 전체 올리기

`$ git commit -m 'COMMIT_MESSAGE'` : commit

![image-20201230001553477](basic.assets/image-20201230001553477.png)

`$ git rm --cached FILE/DIRECTORY_NAME`  : tracking 취소

`$ git restore --staged FILE/DIRECTORY_NAME`  : stage에서 내리기

`$ git restore FILE/DIRECTORY_NAME` : 복원 (잘 안씀)

---

### github에 올리기

new repository로 올리고 주소 복사

`$ git remote add`

`$ git remote add origin 주소` : 주소를 origin이라는 이름으로 등록 (한 번만 등록하면 됨.)

`$ git push origin master` : origin(등록한 이름)을 push (백업됨.)












