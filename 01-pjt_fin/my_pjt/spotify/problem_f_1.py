"""
    팔로워가 5,000,000이상, 10,000,000미만인 아티스트들을 
    아티스트 이름과 팔로워를 목록으로 출력하기
"""

import json
from pprint import pprint


def get_popular():
    artists_json = open('data/artists.json', encoding='utf-8')
    artists = json.load(artists_json)
    name_and_score = []
    go = []
    for book in artists :
        temp_dict = {}
        boook = book['id']
        book2 = open(f'data/artists/{boook}.json', encoding='utf-8')
        book_detail = json.load(book2)
        b = book_detail['followers']['total']
        #print(b)
        if 5000000 < b < 10000000 :
            temp_dict['followers'] = b
            temp_dict['name'] = book['name']
            name_and_score.append(temp_dict)
        
    return name_and_score

# 아래의 코드는 수정하지 않습니다.
if __name__ == "__main__":
    pprint(get_popular())
