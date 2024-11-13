from django.urls import path
from . import views

app_name="weathers"
urlpatterns = [
    # 원래 서비스라면 index 를 없애도 무관하다.
    # 강의를 위해 save-data url 을 따로 구성
    # API 요청 후 데이터 확인
    path('', views.index, name="index"),
    # API 요청 후 원하는 데이터만 DB에 저장
    path('save-data/', views.save_data, name="save_data"),
    # 전체 데이터 조회
    path('list-data/', views.list_data, name="list_data"),
    # 특정 조건의 데이터만 확인하기: 섭씨 30도가 넘는 시간대만 조회
    path('hot-weathers/', views.hot_weathers, name="hot_weathers"),
]
