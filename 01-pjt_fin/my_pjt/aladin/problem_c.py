import json
from pprint import pprint

def books_info(books, categories):
    books_info = []
    for book in books:
        id = book['id']
        title = book['title']
        author = book['author']
        priceSales = book['priceSales']
        description = book['description']
        cover = book['cover']
        categoryID_list = book['categoryId']
        categoryName = []
        for categoryID_i in categoryID_list:
            for categories_i in range(len(categories)):
                if categoryID_i == categories[categories_i]['id'] :
                    categoryName.append(categories[categories_i]['name'])

        book_info = {'id' : id,
                    'title' : title,
                    'author':author,
                    'priceSales': priceSales,
                    'description':description,
                    'cover':cover,
                    'categoryName' :categoryName, 
        }
        books_info.append(book_info)

    return books_info

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books = json.load(books_json)

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    pprint(books_info(books, categories_list))
