import random
import json

# 금융 상품과 옵션에 대한 더미 데이터 생성 함수
def generate_dummy_deposit_products(num_products=5):
    companies = ['은행A', '은행B', '은행C', '은행D', '은행E']
    products = []
    
    for i in range(num_products):
        product = {
            'fin_prdt_cd': f'FP{i+1:03}',  # 고유 코드 생성
            'kor_co_nm': random.choice(companies),
            'fin_prdt_nm': f'상품명 {i+1}',
            'etc_note': f'설명 {i+1}에 대한 설명입니다.',
            'join_deny': random.choice([1, 2, 3]),
            'join_member': '모든 고객',
            'join_way': random.choice(['온라인', '오프라인']),
            'spcl_cnd': '우대 조건 없음'
        }
        products.append(product)

    return products

def generate_dummy_deposit_options(deposit_products, num_options=10):
    options = []
    
    for i in range(num_options):
        product = random.choice(deposit_products)
        option = {
            
            'fin_prdt_cd': product['fin_prdt_cd'],  # 수정된 부분
            'intr_rate_type_nm': '정기적금',
            'intr_rate': round(random.uniform(1.0, 5.0), 2),  # 1%에서 5% 사이의 금리
            'intr_rate2': round(random.uniform(1.0, 7.0), 2),  # 1%에서 7% 사이의 최고 금리
            'save_trm': random.choice([6, 12, 24, 36])  # 6개월, 1년, 2년, 3년
        }
        options.append(option)

    return options

# 더미 데이터 생성 및 JSON으로 변환
products = generate_dummy_deposit_products()
options = generate_dummy_deposit_options(products)

data = {
    'products': products,
    'options': options
}

json_data = json.dumps(data, ensure_ascii=False, indent=4)
print(json_data)
with open('dummy_data.json', 'w', encoding='utf-8') as json_file:
    json_file.write(json_data)