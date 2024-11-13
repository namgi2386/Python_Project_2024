import json
from pprint import pprint


def book_info(book):
    id = book['id']
    title = book['title']
    author = book['author']
    priceSales = book['priceSales']
    description = book['description']
    cover = book['cover']
    categoryID_list = book['categoryId']

    book_info = {'id' : id ,
                'title' : title,
                'author':author ,
                'priceSales': priceSales,
                'description':description ,
                'cover':cover ,
                'categoryId' :categoryID_list , 
    }

    return book_info
    # 여기에 코드를 작성합니다.


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    book_json = open('data/book.json', encoding='utf-8')
    book = json.load(book_json)

    pprint(book_info(book))
