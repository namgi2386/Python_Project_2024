import json

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


def sorted_cs_books_by_price(books, categories):
    category_dict = {}
    for book in books:
        categoryName = []

        categoryID_list = book['categoryId']
        for categoryID_i in categoryID_list:
            for categories_i in range(len(categories)):
                if categoryID_i == categories[categories_i]['id'] :
                    categoryName.append(categories[categories_i]['name'])
        if '컴퓨터 공학' in categoryName :
            category_dict[book['title']] = categoryName
    
    category_list = list(category_dict.keys())
    return category_list

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books = json.load(books_json)

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    print(sorted_cs_books_by_price(books, categories_list))
