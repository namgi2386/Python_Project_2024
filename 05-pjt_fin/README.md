# 05-pjt

## 목차

[1. 키워드 추가하기](#1-키워드-추가하기)

+ [Keyword model 정의]  
+ [키워드 추가 form 구현]  
+ [추가 된 키워드 화면에서 보여주기]  
+ [삭제하기 ]  

[2. 크롤링 기능 구현](#2-크롤링-기능-구현)

+ [Keyword DB로부터 name 값 가져오기]  
+ [name값을 이용한 크롤링]  
+ [개발자도구를 통한 검색횟수의 Tag 확인]  
+ [Trend model 정의 및 저장]  
+ [화면에서 보여주기 ]  

[3. 히스토그램 기능 구현](#3-히스토그램-기능-구현)

+ [Trend DB로부터 값 가져오기]  
+ [matplotlib을 이용한 그래프 생성]  
+ [그래프 화면에서 보여주기]  

[4. 조건부 크롤링 기능 구현](#4-조건부-크롤링-기능-구현)

+ [개발자도구를 통한 지난1년 키워드의 Tag 확인]  
+ [DB 저장 및 그래프 생성]  
+ [그래프 화면에서 보여주기]  

[5. 더러워진 DB 청소하기](#5-더러워진-db-청소하기)

+ [CLEAR Trend]  


## 1. ✨✨✨✨✨키워드 추가하기✨✨✨✨✨

### Keyword model 정의
---
![01](static/readme/01keyword.png)
---
### 키워드 추가하는 입력 form 구현
```py
class KeywordForm(forms.ModelForm):
    class Meta:
        model = Keyword
        fields = ('name',)
```
> KeywordForm을 이용하여 view에서 키워드의 입력을 받는다.  
> CRUD의 CREATE의 과정과 동일하다.  
### 추가 된 키워드 화면에서 보여주기
---
![02](static/readme/03KEY.png)
---
### 삭제하기 
<details>
<summary>
코드보기
</summary>

```py
def delete(request , pk):
    keywords = Keyword.objects.get(pk=pk)
    if request.method == 'POST':
        keywords.delete()
        return redirect('trends:keyword')
    return redirect('trends:index')
```
</details>

> CRUD의 DELETE의 과정과 동일하다.

## 2. ✨✨✨✨✨크롤링 기능 구현✨✨✨✨✨

### Keyword DB로부터 name 값 가져오기
<!-- <details>
<summary>
코드보기
</summary>

</details> -->

<details>
<summary>
코드보기
</summary>

```py
def crawling(request):
    keywoods = Keyword.objects.all()

    for key_name in keywoods:
        stat = get_google_data(key_name.name,"")
        Trend.objects.get_or_create(name=key_name.name , result=stat , search_period="all")

    keywords = Trend.objects.all()
    context ={
        'keywords' : keywords,
    }
    return render(request, 'trends/crawling.html', context )
```
</details>

1. keyword로부터 data 가져오기
2. 각 data에대한 name값을 이용하여 크롤링 실행
3. 함께 인자로 사용되는 문자열은 조건부크롤링을 위함
4. 중복제거후 저장을 위해 `get_or_create` 매서드를 사용
5. 크롤링이 끝났다면 templates로 이동하여 화면을 보여주게 된다.

### Trend DB
![02](static/readme/02trend.png)
---
### 크롤링 화면
![02](static/readme/04crow.png)
---


## 3. ✨✨✨✨✨히스토그램 기능 구현✨✨✨✨✨

### Trend DB로부터 값 가져오기
<details>
<summary>
코드보기
</summary>

```py
    trends = Trend.objects.all()

    names = [trend.name for trend in trends]
    results = [trend.result for trend in trends]
```
</details>

> Trend의 각 data에 대하여 name과 result를 변수로 가져온다.  
> 두 값을 이용하여 그래프를 생성한다.


### matplotlib을 이용한 그래프 생성

<details>
<summary>
코드보기
</summary>

```py
    fig, ax = plt.subplots()
    ax.bar(names, results, color='skyblue')
    ax.set_xlabel('Name')
    ax.set_ylabel('Result')
    ax.set_title('Trend Results')

    # Save the plot to a BytesIO object
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    
    # Encode image to base64 string
    image_png = buffer.getvalue()
    buffer.close()
    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')
```
</details>

### 그래프 화면
![02](static/readme/05gra.png)
---


## 4. ✨✨✨✨✨조건부 크롤링 기능 구현✨✨✨✨✨✨

### 개발자도구를 통한 지난1년 키워드의 Tag 확인

### DB 저장 및 그래프 생성
### 그래프 화면에서 보여주기



## 5. ✨✨✨✨✨더러워진 DB 청소하기✨✨✨✨✨
### CLEAR Trend

> DB에 저장되어가는 data를 전부 정리하기 위해 버튼만들어 두었다. 
```py
def clearTrend(request):
    Trend.objects.all().delete()
    return redirect('trends:keyword')
```

