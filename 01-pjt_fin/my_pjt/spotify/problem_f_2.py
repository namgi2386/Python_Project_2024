"""
    장르에 acoustic이 포함된 아티스트 이름 목록 출력하기
"""

# import json
# from pprint import pprint


# def acoustic_artists():
#     artists_json = open('data/artists.json', encoding='utf-8')
#     artists = json.load(artists_json)
#     genres_json = open('data/genres.json', encoding='utf-8')
#     genres = json.load(genres_json)
#     name_and_score = []
#     artists_info=[]
#     for artist in artists:
#         id = artist['id']
#         name = artist['name']
#         genres_ids = artist['genres_ids']
#         images = artist['images']
#         type = artist['type']
#         genres_Name = []

#         for categoryID_i in genres_ids:
#             for categories_i in range(len(genres)):
#                 if categoryID_i == genres[categories_i]['id'] :
#                     genres_Name.append(genres[categories_i]['name'])
        
#         artist_info = {'id' : id ,
#                     'name' : name,
#                     'genres_Name':genres_Name ,
#                     'images': images,
#                     'type':type ,
#         }
#         artists_info.append(artist_info)

#     print(artist_info)

#     # for book in artists :
#     #     temp_dict = {}
#     #     boook = book['id']
#     #     book2 = open(f'data/artists/{boook}.json', encoding='utf-8')
#     #     book_detail = json.load(book2)
#     #     b = book_detail['followers']['total']
#     #     #print(b)
#     #     if 5000000 < b < 10000000 :
#     #         temp_dict['followers'] = b
#     #         temp_dict['name'] = book['name']
#     #         name_and_score.append(temp_dict)
        
#     return name_and_score


# # 아래의 코드는 수정하지 않습니다.
# if __name__ == "__main__":
#     pprint(acoustic_artists())
