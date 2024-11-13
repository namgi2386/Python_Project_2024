# 임남기

---

## 🅰️branch

### 🔵 브랜치 목록

> master  : 최종 브랜치  
> develop  : 개발 전용 브랜치  
> namgi  : 각자 push 할 브랜치  
> suyeon  : 각자 push 할 브랜치  

### 🔵 브랜치 전략

> 1. 원격 브랜치로부터 pull 받은 뒤 로컬 namgi 브랜치에서 수정 후 
> 2. 원격 namgi 브랜치로 push
> 3. 원격 namgi > develop : merge request
> 4. 모든 개발 완료 후  develop > main : merge request
> 5. 완료

## 🅱️학습 내용

### 🔵 학습 목표
> + 기존에 DRF와 Rest-framework 내용을 기반으로 시작한다.  
> + 이번 프로젝트에서는 직접 rest-api를 만들어 본다.


### 🔵 학습한 내용 및 소감

#### 1. API ⭐
> + 금융감독원 open API로부터 DATA를 가져오기 위해서는 2가지가 필요하다. 
>    1. 발급받은 `API KEY`
>    2. DATA를 요청할 `URL` 그리고 적절한 요청변수

> + API 가이드 공식문서를 확인하며 적절한 URL과 요청변수를 가져오는것이 매우 중요하다.
> + 예시 URL를 확인하며 직접 적용해보고 시도해보는 과정이 많음 도움 되었다.

> + `api_test` 함수를 이용하여 호출된 data를 조회해보며 진행한다.
> + 지정된 url에 json 형태로 data 요청을 보낸다.
> + 요청 받은 data 중 내가 원하는 데이터만을 `JsonResponse`로 감싸 클라이언트에 `JSON` 형식으로 반환한다.

### 2. env
> + 환경변수 파일 및 설정
> + `.env` 파일을 생성하고 gitignore에 등록하여 나의 소중한 정보를 저장한다.
> + `settings` 의 `os , environ` 를 이용하여 적절하게 `.env`의 정보를 가져온다.
> + 이후 `settings`에 설정해 둔 변수를 사용할 수 있도록 한다.

### 3. 기본 세팅
> + model 작성
> + model을 기반으로 Serializer 작성
> + url 작성

### 4. DATA 저장 ⭐
> + `api_test` 와 동일하게 url , 요청변수를 이용하여 json 형태로 `response`를 받아온다.
> + response 의 방대한 데이터 중 내가 원하는 필드를 가져오기 위해 response를 확인 해야 한다. 
> + get 함수를 이용하여 data 추출한다.
> + model로부터 filter를 이용하여 중복된 data는 저장하지 않는다.
> + 추출된 data를 딕셔너리 형태로 변수에 저장한다.
> + 유효성 검사가 완료된 serialize data 를 save 한다. 

### 5. DATA 조회 및 생성
> + 해당 PART에서의 내용은 기존의 DRF 실습에서와 동일하게 진행 가능하다.