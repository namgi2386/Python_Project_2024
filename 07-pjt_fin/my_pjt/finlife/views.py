from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
from django.conf import settings
from .models import DepositProducts, DepositOptions
from .serializers import DepositProductsSerializer, DepositOptionsSerializer
from rest_framework import status


API_KEY = settings.API_KEY
BASE_URL = 'http://finlife.fss.or.kr/'

@api_view(['GET'])
def api_test(request):
    URL = BASE_URL + 'finlifeapi/depositProductsSearch.json'
    params = {
        'auth' : settings.API_KEY,
        'topFinGrpNo' : '020000',
        'pageNo' : '1'
    }
    response = requests.get(URL, params=params).json()
    return JsonResponse({'response': response['result']})


@api_view(['GET'])
def save_deposit_products(request):
    # 1. api로부터 데이터 가져오기
    URL = BASE_URL + 'finlifeapi/depositProductsSearch.json'
    params = {
        'auth' : settings.API_KEY,
        'topFinGrpNo' : '020000',
        'pageNo' : '1'
    }
    response = requests.get(URL, params=params).json()

    # # 2. 원하는 필드 가져오기
    for dic in response['result']['baseList'] :
        fin_prdt_nm = dic.get('fin_prdt_nm')
        kor_co_nm = dic.get('kor_co_nm')
        fin_prdt_cd = dic.get('fin_prdt_cd')
        etc_note = dic.get('etc_note')
        join_deny = dic.get('join_deny')
        join_member = dic.get('join_member')
        join_way = dic.get('join_way')
        spcl_cnd = dic.get('spcl_cnd')

        if DepositProducts.objects.filter(fin_prdt_nm=fin_prdt_nm , kor_co_nm=kor_co_nm ,  fin_prdt_cd= fin_prdt_cd , etc_note=etc_note , join_deny=join_deny , join_member=join_member ,join_way=join_way , spcl_cnd=spcl_cnd).exists():
            continue

        save_data = {
            'fin_prdt_nm': fin_prdt_nm,
            'kor_co_nm' :kor_co_nm,
            'fin_prdt_cd' : fin_prdt_cd,
            'etc_note' : etc_note,
            'join_deny' : join_deny,
            'join_member' : join_member,
            'join_way' : join_way,
            'spcl_cnd' : spcl_cnd,
        }
        serializer = DepositProductsSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    
    for dic in response['result']['optionList'] : 
        fin_prdt_cd = dic.get('fin_prdt_cd')
        intr_rate_type_nm = dic.get('intr_rate_type_nm')
        intr_rate = dic.get('intr_rate')
        intr_rate2 = dic.get('intr_rate2')
        save_trm = dic.get('save_trm')

        if DepositOptions.objects.filter( fin_prdt_cd = fin_prdt_cd, intr_rate_type_nm = intr_rate_type_nm, intr_rate = intr_rate, intr_rate2 = intr_rate2, save_trm = save_trm ).exists():
            continue
        if not intr_rate:
            intr_rate = -1
        save_data = {
        'fin_prdt_cd' : fin_prdt_cd,
        'intr_rate_type_nm' : intr_rate_type_nm,
        'intr_rate' : intr_rate,
        'intr_rate2' : intr_rate2,
        'save_trm' : save_trm
        }
        serializer = DepositOptionsSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            product = DepositProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
            serializer.save(product = product)
    return JsonResponse({'message' :'성공!' })


@api_view(['GET', 'POST'])
def deposit_products(request):
    # 3. 전체 정기예금 상품 목록 출력
    if request.method == "GET":
        DepositProducts_list = DepositProducts.objects.all()
        serializer = DepositProductsSerializer(DepositProducts_list, many=True)
        return Response(serializer.data)

    # 4. 정기 예금 상품 추가하기
    elif request.method == "POST":
        serializer = DepositProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'message': f'이미 있는 데이터이거나, 데이터가 잘못 입력되었습니다.'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
# 5. 특정 상품 옵션 리스트 출력
def deposit_product_options(request, fin_prdt_cd):
    options = DepositOptions.ovjects.filter(fin_prdt_cd=fin_prdt_cd)
    serializer = DepositOptionsSerializer(options, many=True)
    return Response(serializer.data)
    


@api_view(['GET'])
# 6. 금리가 가장 높은 상품의 정보 출력
def top_rate(request):
    option_list = DepositOptions.objects.all()
    maximum_option_rate = 0
    for option in option_list:
        if maximum_option_rate < option.intr_rate2 :
            maximum_option_rate = option.intr_rate2
            maximum_option = option
    product = DepositProducts.objects.get(fin_prdt_cd=maximum_option.fin_prdt_cd)
    serializer2 = DepositProductsSerializer(product)
    serializer = DepositOptionsSerializer(maximum_option)

    return Response({'products': serializer2.data , 'options':[serializer.data]})

    
