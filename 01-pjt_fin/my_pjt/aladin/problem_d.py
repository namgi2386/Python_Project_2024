import json
from pprint import pprint

def best_book(books):
    name_and_score = {}
    best_score = 0
    best_name = ""
    for book in books : # books.json [ {} ,{ } ,{ }]
        boook = book['id']
        book2 = open(f'data/books/{boook}.json', encoding='utf-8')
        book_detail = json.load(book2)

        b = book_detail['customerReviewRank']
        
        name_and_score[book['title']] = b
        if b > best_score:
            best_score = b
            best_name = book['title']
        
    return best_name


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books_list = json.load(books_json)

    print(best_book(books_list))

