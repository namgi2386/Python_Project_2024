import json

def max_polularity(artists):
    name_and_score = {}
    best_score = 0
    best_name = ""
    for book in artists : # artists.json [ {} ,{ } ,{ }]
        boook = book['id']
        book2 = open(f'data/artists/{boook}.json', encoding='utf-8') #>> artists
        book_detail = json.load(book2)

        b = book_detail['popularity'] #>>> popularity
        
        name_and_score[book['name']] = b
        if b > best_score:
            best_score = b
            best_name = book['name']
        
    return best_name


# 아래의 코드는 수정하지 않습니다.
if __name__ == "__main__":
    artists_json = open("data/artists.json", encoding="utf-8")
    artists_list = json.load(artists_json)

    print(max_polularity(artists_list))
