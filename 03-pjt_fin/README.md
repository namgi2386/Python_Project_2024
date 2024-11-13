>  pjt 03 _ 24. 08. 23.
# 반응형 Portfolio 웹사이트 구현 (금융)

## 🌼포트폴리오 사이트 구현하기🌼

## 목차
1. [Head](#-head-이해하기)
2. [Nav-bar](#nav-bar)
3. [Front](#front-page)
4. [intro-page](#intro-page)
5. [skills](#skills)
6. [contact](#contact-and-footer-생략)


---
---

## 🐳 `<head>` 이해하기
### 🌱bootstrap CDN 
`link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/ ...`  
+ 🍄해당 코드를 통하여, bootstrap의 css를 불러와서 사용한다.  
+ 🍄위치는 나의 style tag 보다 상단에 위치하도록 한다.
+ `CDN` : 지리적으로 분산된 서버들을 연결한 네트워크 (시험출제)

### 🌱Google font
`<link rel="preconnect"...`
+ 🍄구글의 폰트를 사용하기 위한 링크
+ 🍄링크형태이기 때문에 로컬에 다운로드 받지 않는다.
+ 🍄css파일에서도 작성해 줄 코드가 존재

### ✨로컬 css 파일 불러오기✨ 
`<link rel="stylesheet" href="./style.css">`
+ 🍄html의 head에 style tag 를 이용하는 대신
+ 🍄로컬의 css파일을 불러와서 사용할 수 있다.

## 🐙Nav bar 
> 기본적으로 bootstrap의 nav bar tab 의 내용을 기본으로 한다.
###  🌱`navbar-expand-sm`
+ 🦐sm 크기를 기준으로 하여 반응형으로 nav bar 목차들의 형태가 변경된다.
### 🌱`mb-2 mb-lg-0`
+ 🦐mb-2 : 아래 기본 margin-2
+ 🦐mb-lg-0 : lg 크기 이후로 아래 margin-0
### 🌱`href="#intro"`
+ 🦐각각의 목차는 list형태로 만들었으며, 
+ 🦐href="#intro" : id값이 intro인 tag로 스크롤 이동을 할수있도록 한다.

## 🐝Front page
> 아이콘있는 `aside` 그리고 배경 이미지인 `front-figure`로 구분된다.
> 배경이미지를 부모로 하는 `front-text`가 `absolute`하게 위치한다. 

|                   | aside        | front-text | front-fiqure |   |
|-------------------|--------------|------------|--------------|---|
| z-index           | z-3          | z-2        | z-1          |   |
| max-width : 767px | display-none | col-12     | display-none |   |
| size-             | col-1        | col-7      | col-12       |   |


<details>
<summary>CSS 구현 BY @media </summary>

```css
@media (max-width: 767.98px) {
  
  #front-main-figure-img {
    display: none;
    }
    
    #left-side-icon {
      display: none;
    }
    
    #front-main-text-box {
      width: 100%;
        background-color: rgb(206, 197, 197);
    }
}
```

</details>

## 🐔intro page
+ 🐥intro page는 `header` , `intro-img` , `intro-text`로 구성되며, 반응형 페이지로 만들었다. 
 
+ 🐥`intro-text`에 사용된 이모티콘의 크기를 조절하기 위해 3가지의 아이콘의 id를 동일하게 `intro-icon`로 설정했는데, 동일한 id를 사용하는것 보다는 `class`를 이용하는 것이 적절했을듯 싶다.

## 🐨skills
+ 🐻‍❄️4개의 part를 담는 skills 는 `col-12 col-lg-6 col-xxl-4` 로 하여, 사용자에게 가장 적합한 경험을 제공한다.
  
+ 🐻‍❄️skills의 총 4개의 part는 각각 `pront` , `back` , `todays-feeling` , `etc`로 구성된다. 
+ 🐻‍❄️각각의 part에는 3개의 `image`로 구성되며, 화면크기에따라 한줄에 2개 , 혹은 4개의 part가 보이도록 한다.
  + `row row-cols-2 row-cols-md-4 g-4` 

## contact and footer 생략 