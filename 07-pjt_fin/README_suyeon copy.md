# 07-pjt
## 버전1_금융

## 목표
금융 상품 데이터를 활용한 REST API Server 구축

## 목차
[정기예금 상품 목록 DB 저장](#1-정기예금-상품-목록-db-저장)  
[전체 정기예금 상품 목록 출력](#2-전체-정기예금-상품-목록-출력)  
[정기 예금 상품 추가하기](#3-정기-예금-상품-추가하기)    
[특정 상품의 옵션 리스트 출력](#4-특정-상품의-옵션-리스트-출력)   
[금리가 가장 높은 상품의 정보 출력](#5-금리가-가장-높은-상품의-정보-출력)
[생성형 AI를 활용한 더미 데이터 생성](#6-생성형-ai를-활용한-더미-데이터-생성)  
[어려웠던점 & 소감](#어려웠던점--소감)


## 1. 정기예금 상품 목록 DB 저장
- 정기예금 상품 목록 및 옵션 목록 저장 : 정기예금 API로 부터 데이터를 저장하기 위해 
```
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
```

코드를 작성해서 Postman으로 데이터가 잘 오는지 확인하고 model을 참고해서 가져오고 싶은 목록들을 필터해서 상품목록과 옵션목록을 받아왔다.
- 이때 비어있거나 없는 데이터, 예를 들어 금리가 비어있을 때는 -1을 출력하도록 해주었다.

## 2. 전체 정기예금 상품 목록 출력
- `DepositProducts_list = DepositProducts.objects.all()`로 전체 정기예금 상품 목록을 가져와서 serializer해준 후 출력해주었다.
  
## 3. 정기 예금 상품 추가하기
- `serializer = DepositProductsSerializer(data=request.data)`코드를 작성해서 입력한 데이터를 serializer한 후 상품이 제대로 추가되어 출력되는지 확인하였다. 이때 잘못된 입력이 들어오면 `'message': f'이미 있는 데이터이거나, 데이터가 잘못 입력되었습니다.`가 출력되도록 하였다.

## 4. 특정 상품의 옵션 리스트 출력
- `options = DepositOptions.ovjects.filter(fin_prdt_cd=fin_prdt_cd)`코드를 작성해서 fin_prdt_cd가 같은 option들을 가져와 serializer해준 후 출력해주었다.

## 5. 금리가 가장 높은 상품의 정보 출력
- `option_list = DepositOptions.objects.all()` 코드를 작성해서 전체 옵션을 모두 가져와서 `if maximum_option_rate < option.intr_rate2 :`코드를 작성해서 가장 높은 금리를 찾고 `product = DepositProducts.objects.get(fin_prdt_cd=maximum_option.fin_prdt_cd)` 가장 높은 금리를 가지고있는 옵션의 fin_prdt_cd를 이용해서 product를 찾아 serializer한 후 상품과 옵션을 함께 출려하도록 해주었다.

## 6. 생성형 AI를 활용한 더미 데이터 생성
- AI에게 만들고 싶은 더미데이터의 요구조건과 model에 대한 정보를 줘서 더미데이터를 생성하는 코드를 작성해주라고 하였다. 코드는 2가지 주요 함수를 통해 금융 상품과 관련된 더미 데이터를 생성한다. `generate_dummy_deposit_products(num_products)`라는 코드는 지정된 수의 금융 상품 데이터를 생성한다. `random.choice()`코드로 회사명과 가입 방법을 랜덤으로 선택하고 `generate_dummy_deposit_options(deposit_products, num_options)`라는 코드로 특정 금융 상품 목록에서 무작위로 선택된 상품에 대한 옵션 데이터를 생성한다. 최종적으로 조합된 데이터를 JSON 데이터로 변환하고 dummy_data.json 파일에 저장하였다.

## 어려웠던점 & 소감
- 처음에 API에서 원하는 데이터만 가져와야 하는 부분이 어려웠다. 그래서 라이브 강사님께서 작성해주신 코드와 금융감독원 홈페이지에 API사용 가이드를 참고하면서 코드를 작성해보고 Postman으로 확인해보면서 진행하였다. 공식문서의 중요성을 느낄 수 있었다.
- 또한 전체데이터 중에서 내가 원하는 데이터만 추출하려면 데이터의 구조가 어떻게 생겼는지 분석하는 것이 중요하다는 것을 느꼈다.
- 처음으로 혼자가 아닌 둘이서 프로젝트를 진행해야 되서 git을 써봤는데 혼자서 할 때보다 신경써야할 부분도 많았고 처음으로 git을 쓰면서 진행하는거라 어렵고 버벅대는 부분도 많았다. 아직도 git을 사용하는 것이 익숙해지지 않았지만 다음 프로젝트를 하면서 익숙해지도록 해봐야겠다...
- 2,3,4번 코드를 작성할 때는 Django REST API 수업시간에 배웠던 내용을 활용하는것이 대부분이었어서 크게 어려운부분은 없었다.
