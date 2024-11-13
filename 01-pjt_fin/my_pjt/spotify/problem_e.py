import json

def dec_artists(artists):
    name_and_score = []
    num = 10000000
    go = []
    for book in artists :
        temp_dict = {}
        boook = book['id']
        book2 = open(f'data/artists/{boook}.json', encoding='utf-8')
        book_detail = json.load(book2)
        b = book_detail['followers']['total']
        #print(b)
        if b > num:
            temp_dict['name'] = book['name']
            temp_dict['uri-id'] = book['uri'][15:]
            name_and_score.append(temp_dict)
        
    return name_and_score


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    artists_json = open('data/artists.json', encoding='utf-8')
    artists_list = json.load(artists_json)

    print(dec_artists(artists_list))
