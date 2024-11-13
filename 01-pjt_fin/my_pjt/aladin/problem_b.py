import json
from pprint import pprint

def book_info(book, categories):
    
    
    id = book['id']
    title = book['title']
    author = book['author']
    priceSales = book['priceSales']
    description = book['description']
    cover = book['cover']
    categoryID_list = book['categoryId']
    categoryName = []
    for categoryID_i in categoryID_list:
                                    # 02 print(f" 여기 {categoryID_i}") >>> 151128 , 50919 >> 2번 할거임
        for categories_i in range(len(categories)):
                                    # 03 print(f" 여기  {categories[categories_i]}") >> 20개의 카테고리
                                    # 04 print(f" 여기  {categories[categories_i]['id']}")
                                    # 05 print(int(categoryID_i))
            if categoryID_i == categories[categories_i]['id'] :
                                    # 01 print(f" 여기 {categories[categories_i]['name']}")
                categoryName.append(categories[categories_i]['name'])
                


    book_info = {'id' : id ,
                'title' : title,
                'author':author ,
                'priceSales': priceSales,
                'description':description ,
                'cover':cover ,
                'categoryName' :categoryName , 
    }

    return book_info


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    book_json = open('data/book.json', encoding='utf-8')
    book = json.load(book_json)

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    pprint(book_info(book, categories_list))
