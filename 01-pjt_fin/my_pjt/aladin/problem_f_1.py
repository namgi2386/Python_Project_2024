import json
from pprint import pprint

def best_new_books(books):
    name_and_score = {}
    best_score = 0
    best_name = ""
    year_default = '2023'
    list_of_2023 =[]
    #print(books)

    for book in books :

        boook = book['id']
        book2 = open(f'data/books/{boook}.json', encoding='utf-8')
        book_detail = json.load(book2)
        d = book_detail['pubDate']
        name_and_score[book['title']] = d
        if year_default in d:
            list_of_2023.append(book['title'])

    for book in books : # books.json [ {} ,{ } ,{ }]
        if book['title'] in list_of_2023:
            boook = book['id']
            book2 = open(f'data/books/{boook}.json', encoding='utf-8')
            book_detail = json.load(book2)
            b = book_detail['customerReviewRank']
            name_and_score[book['title']] = b
            #print(name_and_score)
            if b > best_score:
                best_score = b
                best_name = book['title']
    
    return best_name

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books_list = json.load(books_json)

    print(best_new_books(books_list))
