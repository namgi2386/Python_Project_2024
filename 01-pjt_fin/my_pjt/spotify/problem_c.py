import json
from pprint import pprint


def artist_info(artists, genres):
    artists_info=[]
    for artist in artists:
        id = artist['id']
        name = artist['name']
        genres_ids = artist['genres_ids']
        images = artist['images']
        type = artist['type']
        genres_Name = []

        for categoryID_i in genres_ids:
            for categories_i in range(len(genres)):
                if categoryID_i == genres[categories_i]['id'] :
                    genres_Name.append(genres[categories_i]['name']) 



        artist_info = {'id' : id ,
                    'name' : name,
                    'genres_Name':genres_Name ,
                    'images': images,
                    'type':type ,
        }
        artists_info.append(artist_info)

    return artists_info


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    artists_json = open('data/artists.json', encoding='utf-8')
    artists_list = json.load(artists_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(artist_info(artists_list, genres_list))
