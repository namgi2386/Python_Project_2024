from rest_framework import serializers
from .models import Weather

# django 가 사용하는 데이터 형식 (python)
# 우리 서비스 = 웹 서비스 => 다른 언어, 환경에서 요청이 올 수도 있다.
# -> 모든 요청에 부합할 수 있도록 데이터 형식을 정해야한다.
# -> Json 형식으로 돌려주자!
# -> DRF 는 Json 형식으로 변환을 serializers 를 통해서 쉽게 할 수 있도록 해준다.
# DB에 지정된 필드들만 포장에 관여: ModelSerializer
#   - 여러 테이블의 데이터를 한 번에 포장: Nested Serializer
# DB 필드 외의 데이터들도 포장에 관여: Serializer
class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = '__all__'
