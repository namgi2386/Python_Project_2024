# 01-pjt

## problem review

## # Problem_a (book.json으로부터 데이터 가져오기)
-   해당 코드를 통해 함수가 실행된다.
-   원하는 파일 속 데이터를 불러온 뒤 json파일로 인코딩 하는 과정

```py
if __name__ == '__main__':
    book_json = open('data/book.json', encoding='utf-8')
    book = json.load(book_json)

    pprint(book_info(book))
```

-   함수에서는 책의 정보(딕셔너리형태)를 받아온다.
-   책의 정보로부터 원하는 키,밸류를 추출해낸다.
-   추출해 낸 정보들을 딕셔너리형태(book_info)로 반환

```py
def book_info(book):
...
  id = book['id']
...
  book_info = {'id' : id ,... }
...
return book_info
```

## # Problem_b (두개의 파일로부터 데이터 가져와서 변경하기)

> Problem_a 의 내용을 따라감

-   book.json, categories.json 으로부터 정보를 가져온다.
-   book으로부터 가져오는 책의 categoryID 정보와
-   category 로부터 가져오는 ID 값을 for문을 이용하여 비교한다.
-   categoryName 이라는 키를 생성하여, value값으로는 categoris의 'name'을 사용한다.

```py
categoryID_list = book['categoryId']
categoryName = []
...
  categories[categories_i]['id']
...
  categoryName.append(categories[categories_i]['name'])
```

## # Problem_c (파일 속 각각의 책들의 데이터 개별적으로 가져오기)

> Problem_b 의 내용을 따라감

- books 로부터 각각의 책 데이터는 for문을 사용하여 가져온다.
- books 전체의 데이터는 books_info에 저장되며,
- 각각의 book 데이터는 book_info에 저장된 뒤 books_info에 append 된다. 
```py
    books_info = []
    for book in books:
      ...
      book_info = {'id' : id, ... }
      ...
      books_info.append(book_info)
      ...
    return books_info 
```

## # Problem_d ( 폴더에 접근하여 데이터 가져오기 )

> Problem_c 의 내용을 따라감
- for문을 사용하여, 폴더 속 파일들의 데이터를 개별적으로 가져온다.
  ```py
  book2 = open(f'data/books/{boook}.json', encoding='utf-8')
        book_detail = json.load(book2)
  ```
- 개별적인 파일로부터 customerReviewRank 의 value값을 가져온다.
  ```py
  b = book_detail['customerReviewRank']
  ```
- 각각의 책들에 대한 점수를 비교하여 최고점과 최고의책을 갱신한다.
  ```py
  best_score = 0
  best_name = ""
    ...
    if b > best_score:
        best_score = b
        best_name = book['title']
  ```

## # Problem_e (응용)

> Problem_d 의 내용을 따라감
- 응용
  ```py
  year_default = '2023'
  list_of_2023 =[]
  ...
  if year_default in b:
      list_of_2023.append(book['title'])
  ```
## # Problem_f

> Problem_d 와 Problem_e 의 내용을 따라감
- Problem_e에서와 같이 list_of_2023 를 만들어 낸다.
- 이후 list_of_2023의 각 요소들에 대하여 최고평점을 구해낸다.
  ```py
    for book in books : 
      if book['title'] in list_of_2023:
  ```

## what I learn today

Learned how to access and retrieve information from other files and folders within the same directory. During this process, I had the opportunity to gain a detailed understanding of the functionalities of dictionaries. I particularly learned a lot about inserting and modifying data in dictionaries and lists.

## Hard for study

There was difficulty in starting without knowing the functions of basic provided code like **main**. Also, the process of accessing and retrieving data from other files felt quite complex.

## I feel good~ :music:

It feels like I can categorize all the data in the world.
