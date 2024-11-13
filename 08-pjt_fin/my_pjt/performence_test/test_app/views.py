from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.shortcuts import render
import random
import pandas as pd

array_length = 1000
random_range = 5000

@api_view(['GET'])
def bubble_sort(request):
    li = []
    for i in range(array_length):
        li.append(random.choice(range(1, random_range)))
    for i in range(len(li) - 1, 0, -1):
        for j in range(i):
            if li[j] < li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
    context = {
      'top': li[0]
    }
    return JsonResponse(context)

@api_view(['GET'])
def normal_sort(request):
    li = []
    for i in range(array_length):
        li.append(random.choice(range(1, random_range)))
    li.sort(reverse=True)
    context = {
        'top': li[0]
    }
    return JsonResponse(context)

from queue import PriorityQueue

@api_view(['GET'])
def priority_queue(request):
    pq = PriorityQueue()
    for i in range(array_length):
        pq.put(-random.choice(range(1, random_range)))
    context = {
        'top': -pq.get()
    }
    return JsonResponse(context)

##########################################################################
#################           여기서부터 코드 작성          #################
##########################################################################


# T. 테스트용 html 사용
def load_csv_view_for_template(request):
    csv_path = '../data/test_data.CSV'

    data = pd.read_csv(csv_path, encoding='euc-kr')

    data_dict = data.to_dict('records')
    return render(request, 'test_app/testindex.html', {'data': data_dict})

# A. DATA 읽어오기
def load_csv_view_data_testdata(request):

    csv_path = '../data/test_data.CSV' 
    data = pd.read_csv(csv_path , encoding='euc-kr')
    
    data_dict = data.to_dict('records')
    
    return JsonResponse({'dot': data_dict})

# B. 결측치 처리하기
def load_csv_view_data_nulldata(request):

    csv_path = '../data/test_data_has_null.CSV' 
    data = pd.read_csv(csv_path , encoding='euc-kr')
    data['나이'].fillna('Null', inplace=True)
    data['성별'].fillna('Null', inplace=True)
    data['직업'].fillna('Null', inplace=True)
    data['사는곳'].fillna('Null', inplace=True)
    data_dict = data.to_dict('records')
    
    return JsonResponse({'dot': data_dict})

def load_csv_view_data_nulldata_ave(request):

    csv_path = '../data/test_data_has_null.CSV' 
    data = pd.read_csv(csv_path , encoding='euc-kr')
    data['성별'].fillna('없음', inplace=True)
    data['직업'].fillna('백수', inplace=True)
    data['사는곳'].fillna('어딘가', inplace=True)
    ave_age = data['나이'].mean(skipna=True)
    data['나이'].fillna(0, inplace=True)
    data['dif_age'] = abs(data['나이']- ave_age)
    data['dif_age1'] = abs(data['나이']- ave_age)
    data['dif_age2'] = abs(data['나이']- ave_age)
    data['dif_age3'] = abs(data['나이']- ave_age)
    data['dif_age4'] = abs(data['나이']- ave_age)
    data['dif_age5'] = abs(data['나이']- ave_age)
    data['dif_age6'] = abs(data['나이']- ave_age)
    data['dif_age7'] = abs(data['나이']- ave_age)
    data['dif_age8'] = abs(data['나이']- ave_age)
    data['dif_age9'] = abs(data['나이']- ave_age)

    sorted_data = data.sort_values(by='dif_age').head(10)
    
    print(ave_age)
    data_dict = sorted_data.to_dict('records')
    return JsonResponse({'dot': data_dict})

##################################################################
################## 여기서부터 친구 코드 ############################

@api_view(['GET'])
def jywon_avg(request):
    csv_path = '../data/test_data.CSV'
    df = pd.read_csv(csv_path , encoding='euc-kr')
    df2 = df.copy()
    avg = df2['나이'].dropna().mean()
    df2['평균 나이와의 차이'] = abs(df2['나이'] - avg)
    df2 = df2.sort_values(by=['평균 나이와의 차이']).drop('평균 나이와의 차이', axis=1).head(10)
    data = df2.to_dict('records')
    return JsonResponse({
        'avg': avg,
        'data': data,
        })



import os
from django.conf import settings
# 전역 변수로 DataFrame선언
df_global = None

# DataFrame 초기화 함수
def initialize_dataframe():
    global df_global
    file_path = os.path.join(settings.BASE_DIR, 'data', 'test_data_has_null.CSV') # 절대 경로 사용
    df_global = pd.read_csv(file_path, encoding='cp949')
    df_global = df_global.fillna("NULL") # 결측치(NaN)를 "NULL"로 치환

@api_view(['GET'])
def sooyeun_avg(request):
    global df_global
    # Dataframe이 초기화 되지 않았으면 초기화
    if df_global is None:
        initialize_dataframe()

    df_age = df_global[df_global['나이'] != "NULL"]  # "NULL"이 아닌 값만 필터링
    df_age['나이'] = pd.to_numeric(df_age['나이'], errors='coerce')  # "나이" 필드를 숫자로 변환
    average_age = df_age['나이'].mean()  # 평균 계산

    # 평균 나이와 가장 비슷한 10개의 행 선택
    df_age['차이'] = abs(df_age['나이'] - average_age)  # 나이와 평균 나이의 차이 계산
    similar_ages_df = df_age.sort_values(by='차이').head(10)  # 차이가 작은 순으로 정렬 후 상위 10개 선택
    similar_ages_df = similar_ages_df.drop(columns=['차이'])  # 차이 컬럼 제거

    data = similar_ages_df.to_dict('records')
    return JsonResponse({'average_age': round(average_age,2), 'similar_ages': data})