# AgAs (Automatically generate advertising scripts)

![Agas](https://github.com/Hyunwooz/DjangoGptProject_BE/assets/107661525/db450707-8bb6-4d45-915e-825e2fac0365)

## 1. 목표 및 기능

### 1.1 목표

-   ChatGPT를 이용하여 업무의 생산성을 높일 수 있는 서비스 개발
-   ChatGPT를 통해 광고 카피 문구를 생성해주는 서비스

### 1.2 기능

-   회원가입 및 로그인 , 소셜 로그인 (GitHub)
    ```
    이메일을 통한 회원가입 뿐만 아니라 깃허브를 이용한 소셜로그인 기능을 제공하고 있습니다.
    회원탈퇴와 비밀번호 변경 기능도 제공하고 있습니다.
    ```
-   JSON Web Token 인증 방식
    ```
    로그인시 발급된 Access Token을 통해서 유저 인증을 진행하는 기능을 제공하고 있습니다.
    ```
-   Profile CRU
    ```
    회원가입 후 자신을 대표하는 프로필을 꾸밀 수 있는 기능을 제공하고 있습니다.
    프로필 이미지와 한줄 소개를 작성하실 수 있습니다.
    ```
-   광고 카피 CRD ( with ChatGPT )
-   광고 카피 조회수 기능
-   맘에드는 광고 카피 좋아요
    ```
    ChatGTP를 통해 만든 광고 카피를 공유할 수 있는 장소와 기능을 제공하고 있습니다.
    특정 광고 카피 디테일 뷰에 들어가게 되면 조회수가 올라갑니다.    
    마음에 드는 광고 카피에 좋아요를 남길 수도 있습니다.
    ```
-   댓글 CRD
    ```
    댓글을 이용하여 광고 카피에 대한 의견을 남길 수 있습니다.
    ```
-   제목, 카테고리 검색
    ```
    원하시는 키워드 검색을 통해서 
    게시물의 제목 또는 내용에 해당 키워드가 포함된 게시물을 찾아 보실 수 있습니다.

    또한 원하시는 종류의 카테리고만을 모아서 보실 수 있습니다.
    ```

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
-   ~~http://43.200.64.24/~~ 현재 배포 되고 있지 않습니다.
-   Back-End Repo : https://github.com/Hyunwooz/DjangoGptProject_BE
#### Front-End
-   http://www.kanghyunwoo.com/
-   Front-End Repo : https://github.com/Hyunwooz/DjangoGptProject_FE

## 3. 프로젝트 구조와 개발 일정

### 3.1 Entity Relationship Diagram
![ERD](https://github.com/Hyunwooz/DjangoGptProject_FE/assets/107661525/9bfbf5e4-5c88-4ba1-bda7-023454420c61)

### 3.2 URL 설계

|이름|URL|비고|
|------|---|---|
|User|||
|로그인|user/join/||
|회원가입|user/login/||
|프로필|user/profile/||
|깃헙 로그인|user/login/github/||
|깃헙 로그인 콜백|user/login/github/callback/|||
|Token|||
|token|user/token/||
|refresh|user/token/refresh/||
|verify|user/token/verify/||
|Chatbot|||
|마이페이지|Chatbot/mylist/||
|라운지|Chatbot/lounge/||
|디테일 뷰|Chatbot/detail/||
|카피 삭제|Chatbot/delete/||
|공개 설정|Chatbot/public/||
|비공개 설정|Chatbot/private/||
|댓글 작성|Chatbot/comment/write/||
|댓글 삭제|Chatbot/comment/delete/||
|검색|Chatbot/search/||
|좋아요|Chatbot/like/||

### 3.3 프로젝트 구조
```
DjangoGptProject
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
### 3.4 개발 일정

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
![main](https://github.com/Hyunwooz/DjangoGptProject_FE/assets/107661525/52255c94-8052-40d3-8790-c8421eebc818)
![auth_user](https://github.com/Hyunwooz/DjangoGptProject_FE/assets/107661525/4a2de49e-bdc7-49fb-96a6-8b1086273364)
![일일 제한](https://github.com/Hyunwooz/DjangoGptProject_FE/assets/107661525/c16e3ef5-4594-42cb-a6c1-eca883a31964)
```
광고 카피를 생성하는 메인 기능입니다. 로그인된 유저만 이용이 가능합니다.

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.ScopedRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'contact': '1000/day',
        'chatbot': '5/day',
    },
}

유저당 일일 5회만 이용 가능합니다.
``` 
![joinlogin](https://github.com/Hyunwooz/DjangoGptProject_FE/assets/107661525/71fcca25-ae05-4927-9e5c-85c5a92136fb)
![github](https://github.com/Hyunwooz/DjangoGptProject_FE/assets/107661525/fd359c43-8298-4618-9292-a922d9bed0d3)
```
회원가입과 로그인 기능입니다.
Gitgub 로그인도 구현하였습니다.
``` 
![profile](https://github.com/Hyunwooz/DjangoGptProject_FE/assets/107661525/2b91b30e-f5bc-4e52-a83f-18a26a86e38d)
![private 설정](https://github.com/Hyunwooz/DjangoGptProject_FE/assets/107661525/f07c7494-7693-4872-a795-b0f5ece5c04e)
```
프로필 이미지 및 닉네임, 자기 소개 문구를 수정할 수 있습니다.
본인의 게시물이라면 삭제가 가능하며
Public과 Private 설정을 통해 공개하고 싶은 광고 카피만 공개할 수 있습니다.
``` 
![search](https://github.com/Hyunwooz/DjangoGptProject_FE/assets/107661525/cf6a13ca-1637-494d-b83c-c2d228a0a9c2)
![like](https://github.com/Hyunwooz/DjangoGptProject_FE/assets/107661525/986d19af-7caf-4954-b5e9-3ddde01693d3)
```
원하는 제목 , 카테고리 등을 통해 광고 카피 검색이 가능합니다.
맘에 드는 광고 카피에 좋아요와 댓글을 달 수 있습니다.
자신이 작성한 댓글이라면 삭제 또한 가능합니다.
``` 
## 6. 개발과정과 느낀점

### Github Login

우선 예전에 다른 프로젝트를 통해서 Github 소셜 로그인은 해본 경험이 있어서 해당 기능 개발 순서를 뒤쪽으로 계획하고 진행하였습니다.

참고 블로그 : https://medium.com/chanjongs-programming-diary/django-rest-framework%EB%A1%9C-%EC%86%8C%EC%85%9C-%EB%A1%9C%EA%B7%B8%EC%9D%B8-api-%EA%B5%AC%ED%98%84%ED%95%B4%EB%B3%B4%EA%B8%B0-google-kakao-github-2-cf1b4059b5d5

위의 블로그를 참고하여 개발을 진행하였습니다.

앞서 말씀드린 것처럼 미리 경험이 있기에 개발 순서를 뒤로 밀었는데 좋은 판단이 아니였습니다.

이번 프로젝트는 FE서버와 BE서버를 분리해서 개발하기에 제가 미리 경험했던 그떄와는 환경이 달라졌기 때문입니다.

```
def github_login(request):
    return redirect(
        f"https://github.com/login/oauth/authorize?client_id={client_id}&redirect_uri={GITHUB_CALLBACK_URI}"
    )
```
해당 부분에서 return redirect를 사용할 수 없기에 오류가 일어났습니다.

이를 해결하기 위해 FE 서버에서 접근하기로 결정했습니다.
```
const github_login = async (event) => {
    ... 생략...
    await fetch(url, {
        method: "POST",
        headers: {},
    })
    .then((res) => res.json())
    .then((data) => {
        if (data) {
            location.href = data.url
        } 
    })
}
```
![스크린샷 2023-08-02 155125](https://github.com/Hyunwooz/DjangoGptProject_BE/assets/107661525/b7c55175-17b0-44f7-93b9-0900aeebce9e)
```
class GithubLogin(APIView):
    def post(self, request):
        
        data = {
            'url': f"https://github.com/login/oauth/authorize?client_id={CLIENT_ID}&redirect_uri={redirect_uri}"
        }
        return JsonResponse(data)
```

Url을 JsonResponse로 다시 FE서버로 보내준 후 FE서버에서 해당 URL을 GET 합니다.

Callback URL은 FE서버의 로그인 페이지로 설정하였습니다.

그 후 발급받은 Code를 다시 BE 서버로 전달해줍니다.

```
const github_login_func = async() => {
    const urlParams = new URL(location.href).searchParams;
    const code = urlParams.get('code');
    const url = 'http://0.0.0.0/user/login/github/callback/'

    if(code) {
        await fetch(url, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({"code": code})
        })
        .then((res) => res.json())
        ... 생략 ...
    }
}
```

code를 받은 BE 서버에서 access token을 발급받고 , 해당 토큰을 이용하여 github 계정 정보를 불러옵니다.

그 후 github 계정 정보를 이용하여 User 객체를 생성하여 FE 서버에 보내줍니다.

```
class GithubLogin_callback(APIView):
    def post(self, request):
        code = request.data['code']
        token_req = requests.post(
        f"https://github.com/login/oauth/access_token?client_id={CLIENT_ID}&client_secret={CLIENT_SECRET}&code={code}&accept=&json&redirect_uri={redirect_uri}&response_type=code", headers={'Accept': 'application/json'})
        
        token_req_json = token_req.json()
        access_token = token_req_json.get('access_token')
        user_req = requests.get(f"https://api.github.com/user",headers={"Authorization": f"Bearer {access_token}"})
        user_json = user_req.json()
        
        ... 생략 ...
```

### FE <-> BE 데이터 통신

Database에서 전달 받은 객체를 넘기기는 부분에서 오류가 자주 발생하였고 , Json 형식과 dict 형식이 비슷하지만 완전히 같지는 않아 호환되지않는 점으로 인해 많은 오류가 발생하였습니다.

위의 2가지가 빈번히 발생하여 이번 프로젝트를 진행하면서 아주 힘들었습니다.

1.  Database에서 전달 받은 객체를 넘기기는 부분
    ```
    if serializer.is_valid():
        user = serializer.save(request)

        token = RefreshToken.for_user(user)
        refresh = str(token)
        access = str(token.access_token)
        data = {
            'user': user,
            'access': access,
            'refresh': refresh 
        }
        return Response(data=data,status=status.HTTP_200_OK)
    ```
    - Error 구문
    ```
    Internal Server Error
    TypeError: Object of type User is not JSON serializable
    ```
    - Error 발생 이유
    ```
    user = serializer.save(request) 
    # 해당 구문의 데이터 타입이 QuerySet 이라서 발생하였습니다.
    # 쿼리셋은 Django ORM에서 제공하는 데이터 타입입니다.
    ```
    - Error를 해결한 Code
    ```
    if serializer.is_valid(raise_exception=False):
        user = serializer.save(request)

        token = RefreshToken.for_user(user)
        refresh = str(token)
        access = str(token.access_token)

        user_dict  = user.__dict__ 
        # QuerySet를 dict으로 형변환 후 넘겨주었습니다.
        user_dict['_state'] = user_dict['_state'].__dict__
        # 위와 같은 이유로 dict으로 형변환 하였습니다.

        data = {
            'user': user_dict,
            'access': access,
            'refresh': refresh 
        }

        return Response(data=data,status=status.HTTP_200_OK)
    ```
2.  json.loads() 에러
    ```
    questions = {
        "role": "user",
        "content": request.data,
    }
        
    prompt.append(questions)
    
    ## conncet gpt api start
    response = requests.post('https://estsoft-openai-api.jejucodingcamp.workers.dev/', json=prompt)
    ai_anwser = response.json()['choices'][0]['message']['content']
    ## end
    
    gpt_anwser = json.loads(ai_anwser)
    ```
    - Error 구문
    ```
    json.decoder.JSONDecodeError: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
    ```
    - Error 발생 이유
    ```
    ai_anwser = response.json()['choices'][0]['message']['content']
    # 해당 데이터는 str 형식이였습니다.
    # EX) ai_anwser = "{'key': 'value'}"
    # Json으로 load할 데이터가 위 처럼 '(홑따옴표)로 되어있어서 해당 오류가 발생하였습니다.
    ```
    - Error를 해결한 Code
    ```
    remake = ai_anwser.replace("'",'"')
    # 간단히 '(홑따옴표)를 "(겹따옴표)로 변경해주어 에러를 해결하였습니다.
    gpt_anwser = json.loads(remake)
    ```
3.  CORS
    ```
    Access to fetch at 'http://127.0.0.1:8000/user/login/' from origin 'http://127.0.0.1:5500' has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource.
    ```
    이 문제는 `django-cors-headers`를 이용하여 쉽게 해결하였습니다.

    ```
    settings.py

    INSTALLED_APPS = [
        'corsheaders',
    ]

    MIDDLEWARE = [
        'corsheaders.middleware.CorsMiddleware',
    ]

    CORS_ALLOWED_ORIGINS = [
        # 허용할 Origin 추가
        "http://127.0.0.1:5500"
    ] # 화이트리스트 추가 입니다.

    # CORS_ORIGIN_ALLOW_ALL = True # 모두 허용
    ```
4.  FE에서 header를 잘못 설정한 경우

    ```
    const api_login = async (event) => {
        event.preventDefault()
        ... 생략 ...

        await fetch(url, {
            method: "POST",
            headers: {
            "Content-Type": "multipart/form-data;
        },
            body: formData,
        })

        ... 생략 ...
    }
    ```
    - Error 구문
    ![스크린샷 2023-07-26 141613](https://github.com/Hyunwooz/DjangoGptProject_BE/assets/107661525/b37fe10d-3bbc-4def-81b9-e61f2c3ffee5)
    ![스크린샷 2023-07-26 141532](https://github.com/Hyunwooz/DjangoGptProject_BE/assets/107661525/3f8470fa-e172-4e8e-aa71-a205a2b7623e)
    ![스크린샷 2023-07-26 141549](https://github.com/Hyunwooz/DjangoGptProject_BE/assets/107661525/71e0c70f-8c7c-423d-acbc-1bb023a548eb)
    ![스크린샷 2023-07-26 141606](https://github.com/Hyunwooz/DjangoGptProject_BE/assets/107661525/545b05cb-6030-4a2c-80fc-fa7c591dfa22)
    ```
    POST http://127.0.0.1:8000/user/login/ 400 (Bad Request)

    network response
    {"detail":"JSON parse error - Expecting value: line 1 column 2 (char 1)"}
    ```
    - Error 발생 이유
    ```
    Client 쪽에서 잘못된 형식으로 Server로 Data를 전달했기에 발생한 문제.
    ```
    - Error를 해결한 Code
    ```
    formData를 보낼때, header 부분은 브라우저가 자동으로 설정해주기 때문에 Content-Type을 따로 지정할 필요가 없었습니다.

    해당 Error는 2가지 해결방법이 존재했습니다.

    1. header에 Content-Type을 따로 지정하지 않고 통신
    2. "Content-Type": "multipart/form-data; boundary=boundary;"
        - 항목과 항목을 구분하는 구분자 사용하기.

    const api_login = async (event) => {
        event.preventDefault()
        ... 생략 ...

        await fetch(url, {
            method: "POST",
            headers: {
        },
            body: formData,
        })

        ... 생략 ...
    }
    ```
5.  CORS 정책 위반 문제인줄 알았지만 전혀 다른 부분이였던 ERROR
    - FE Console 창 Error 구문
    ```
    has been blocked by cors policy: no 'access-control-allow-origin' header is present on the requested resource.
    ```
    - BE /var/log/syslog
    ```
    Aug  2 06:40:26 ip-172-26-6-254 uwsgi[22993]:   File "/home/ubuntu/DjangoGptProject_BE/./user/views.py", line 23
    Aug  2 06:40:26 ip-172-26-6-254 uwsgi[22993]:     return JsonResponse(data)
    Aug  2 06:40:26 ip-172-26-6-254 uwsgi[22993]:                              ^
    Aug  2 06:40:26 ip-172-26-6-254 uwsgi[22993]: IndentationError: unindent does not match any outer indentation level
    ```
    - Error 발생 이유
    ```
    알고보니 Django의 User/veiws.py에서 들여쓰기가 잘못되어있었습니다.
    CORS 정책에만 매몰되어 해결방법을 찾다가 /var/log/syslog를 확인하여 해결하였습니다.
    ```

### 마치며

Django Rest Framework에 대해서 많은 공부를 하게 되었으며,
데이터를 주고받을때 주는 환경과 받는 환경의 차이가 있다는 걸 고려해야 한다는 것을 깨달았습니다.

Front-End와 Back-End가 유기적인 의사소통이 필요하다는 것을 많이 느꼈습니다.

이번 프로젝트는 예외 처리 부분에서 큰 아쉬움을 느끼고 있지만, 다음번 프로젝트를 진행할 때는 예외처리에 대해 좀 더 공부해서 탄탄한 Django 프로젝트들을 진행해보고 싶습니다.

더욱 발전한 개발자로 돌아오도록 하겠습니다.

끝까지 읽어주신 모든 분들 감사합니다 :)
