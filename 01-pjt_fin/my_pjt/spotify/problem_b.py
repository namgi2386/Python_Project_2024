import json
from pprint import pprint


def artist_info(artist, categories):
    id = artist['id']
    name = artist['name']
    genres_ids = artist['genres_ids']
    images = artist['images']
    type = artist['type']
    genres_Name = []

    for categoryID_i in genres_ids:
        for categories_i in range(len(categories)):
            if categoryID_i == categories[categories_i]['id'] :
                genres_Name.append(categories[categories_i]['name']) 

    artist_info = {'id' : id ,
                'name' : name,
                'genres_Name':genres_Name ,
                'images': images,
                'type':type ,
    }
    
    return artist_info

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    artist_json = open('data/artist.json', encoding='utf-8')
    artist_dict = json.load(artist_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(artist_info(artist_dict, genres_list))
