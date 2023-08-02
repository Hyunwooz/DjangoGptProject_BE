# Django ChatGPT Project Back-End

-   Django ChatGPT Project Back-End Repo 입니다.

## 1. 목표 및 기능

### 1.1 목표

-   ChatGPT를 이용하여 업무의 생산성을 높일 수 있는 서비스 개발
-   ChatGPT를 통해 광고 카피 문구를 생성해주는 서비스

### 1.2 기능

-   회원가입 및 로그인 
-   Github 로그인
-   JSON Web Token 인증 방식
-   Profile CRU
-   광고 카피 CRD ( with ChatGPT )
-   광고 카피 조회수 표시
-   맘에드는 광고 카피 좋아요
-   댓글 CRD
-   제목 검색
-   카테고리 검색

## 2. 개발 환경 및 배포 URL

### 2.1 개발 환경

-   Python == 3.10.4
-   Django == 4.2.3
-   Pillow == 10.0.0

### 2.2 배포 환경

#### Back-End
-   Aws Lightsail
-   Nginx
-   uwsgi

#### Front-End
-   Github Page

### 2.2 배포 URL

#### Back-End
-   http://43.200.64.24/
-   Back-End Repo : https://github.com/Hyunwooz/DjangoGptProject_BE
#### Front-End
-   http://www.kanghyunwoo.com/
-   Front-End Repo : https://github.com/Hyunwooz/DjangoGptProject_FE

## 3. 프로젝트 구조와 개발 일정

### 3.1 Entity Relationship Diagram
![ERD](https://github.com/Hyunwooz/DjangoGptProject_FE/assets/107661525/9bfbf5e4-5c88-4ba1-bda7-023454420c61)

### 3.2 프로젝트 구조
```
Django-blog
│
|   .gitignore
|   README.md
|   requirements.txt
+---Api
|   |   db.sqlite3
|   |   manage.py
|   +---Api 
|   +---chatbot
|   +---media
|   |   \---user
|   |       \---media
|   \---user
\---venv
```
### 3.3 개발 일정

#### 개발 일정

2023.07.26 ~ 2023.08.02

#### 기술 스택

-   Python
-   Django
-   SQLite
-   HTML
-   바닐라 JS
-   CSS

## 4. 전체 페이지

-   전체 페이지 UI
![main](https://github.com/Hyunwooz/DjangoGptProject_FE/assets/107661525/369fafca-0af8-4adb-b1fd-d7d699ffb1d4)
```
로그인된 메인 페이지
``` 
![no_login](https://github.com/Hyunwooz/DjangoGptProject_FE/assets/107661525/29d5bf36-75ff-4521-b766-34fc71c96067)
```
로그인 하지 않은 페이지의 Header
``` 
![로그인조인](https://github.com/Hyunwooz/DjangoGptProject_FE/assets/107661525/75c35bcc-392b-46f7-a96d-6208873f5c09)
```
로그인과 조인 페이지
``` 
![마이페이지](https://github.com/Hyunwooz/DjangoGptProject_FE/assets/107661525/730f71ee-bd33-4656-8593-152d14199c8a)
```
마이 페이지와 프로필 수정 페이지
``` 
![라운지서치](https://github.com/Hyunwooz/DjangoGptProject_FE/assets/107661525/cf8cf202-ed23-4d07-87f7-1d9392fad8a1)
```
라운지 페이지와 카테고리 서치 페이지
``` 
![디테일제목서치](https://github.com/Hyunwooz/DjangoGptProject_FE/assets/107661525/8cae191a-81eb-4cc8-88ee-ae9b2576db75)
```
타이틀 서치 페이지와 광고 카피 디테일 페이지
``` 
## 5. 기능
![login-join](https://github.com/Hyunwooz/Django-blog/assets/107661525/9782cb48-7ffa-4fd9-8607-ac73abe04b0d)
```
회원가입 및 로그인
``` 

## 6. 개발과정과 느낀점

### Title
#### Subtitle

### 마치며

