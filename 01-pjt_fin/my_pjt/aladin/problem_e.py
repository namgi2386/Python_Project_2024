import json

def new_books(books):
    name_and_score = {}
    year_default = '2023'
    list_of_2023 =[]
    for book in books :
        if book['id'] is not None:
            boook = book['id']
            book2 = open(f'data/books/{boook}.json', encoding='utf-8')
            book_detail = json.load(book2)
            b = book_detail['pubDate']
            name_and_score[book['title']] = b
            if year_default in b:
                list_of_2023.append(book['title'])
    return list_of_2023



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books_list = json.load(books_json)

    print(new_books(books_list))
