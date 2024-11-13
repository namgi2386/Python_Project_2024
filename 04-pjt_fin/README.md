# 🎥PJT04🎥 : DB를 활용한 웹페이지 구현

## 🔖목차

> [1.개요](#1-프로젝트의-목적)  
> [2.목표](#2-프로젝트의-목표)  
> [3.이론](#3-프로젝트의-이론)  
> [4.✨내용✨](#4-응용)  
    > ___[Index](#index-화면구성)   
    > ___[Create](#create)  
> [5.소감](#5-소감)  

---

## 1. 📗프로젝트의 목적
+ 영화 커뮤니티 웹사이트 구현
## 2. 📕프로젝트의 목표
+ `Django`를 이용한 `CRUD`의 이해

+ `Form`과 `Model`을 이용한 `SQLite` 
+ `static file`를 활용해 서버를 구성
+ `bootstrap`과 `Grid system`을 통한 반응형 웹사이트 구현
+ `style.css`를 이용한 `css`적용
## 3. 📙프로젝트의 이론
#### 1. 🦉Django에서의 MTV 패턴에 대한 이해
![MVC](MVC-1.png)
+ `Client` : url을 통해 `request`, `response`한다.
+ `URL` : `Client` 로부터 요청받은 url에 대하여 view의 함수를 호출한다.
+ `View` : `request`와 `Model , Form`을 이용하여 함수를 실행하며, 결과를 반영한다. 
+ `Model` : `DB`에 저장할 형태를 지정되며 `DB`와 상호작용한다.
+ `Template` : `*.html`파일을 통해 `Client`와 소통한다.

#### 2. 🐦 STATIC에 대한 이해 
> static files : 서버 측에서 변경되지 않고 고정적으로 제공되는 파일  
> 정적 파일을 제공하기 위한 경로가 있어야 함

## 4. 📘응용
### 🎉Index 화면구성
![index_img](image.png)

---

1. bootstrap의 navbar를 응용한 navbar
2. static/assets에 위치한 net_logo.png 이미지를 load 내장함수를 이용하여 사용한다
3. 각 navbar button은 해당 페이지로 이동 가능하다
4. index에서는 DB에 생성된 모든 영화를 반영하게 되며, 이미지를 보여주게 된다
5. 이미지를 통하여 각각의 영화의 detail한 내용을 확인할 수 있다.
6. 이미지를 업로드 하지 않은 상태로 영화를 등록 할 수 있으며, 이미지가 없다면 static/asset에 위치한 loading.png 파일이 노출된다. 
7. 이미지는 정해진 container의 크기에 맞춰서 조정되며, 범위를 벗어나지 않는다.
8. 이미지는 grid system을 이용하여 화면의 크기에 맞춰서 반응형으로 구성되었다.

### Create
![create_img](image-1.png)

---

1. 생성페이지는 페이지`html`을 `client`에게 보여주는 part와 작성된 내용을 model에 따라 db에 반영하는 part가 결합된 형태이다.  
2. 이미지를 업로드 하기 위해 `mediafiles` 개념에 대해 이해한다.  
3. 각 영화의 점수를 기록하는 point를 model에 추가하여 point값에 따라 index에 보여지는 영화의 순서를 정렬하게 된다.  
