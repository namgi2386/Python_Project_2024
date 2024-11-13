import json
from pprint import pprint


def artist_info(artist):
    id = artist['id']
    name = artist['name']
    genres_ids = artist['genres_ids']
    images = artist['images']
    type = artist['type']


    artist_info = {'id' : id ,
                'name' : name,
                'genres_ids':genres_ids ,
                'images': images,
                'type':type ,
    }

    return artist_info


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    artist_json = open('data/artist.json', encoding='utf-8')
    artist_dict = json.load(artist_json)

    pprint(artist_info(artist_dict))
