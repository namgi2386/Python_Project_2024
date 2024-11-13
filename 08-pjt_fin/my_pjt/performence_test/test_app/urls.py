from django.urls import path
from . import views

app_name='test_app'
urlpatterns = [
    # 내장 메서드 sort()
    path('normal_sort/', views.normal_sort),
    # 우선순위큐
    path('priority_queue/', views.priority_queue),
    # 버블정렬
    path('bubble_sort/', views.bubble_sort),
    path('test_index/' , views.load_csv_view_for_template , name="test_view"),
    path('test_json/data/test_data/', views.load_csv_view_data_testdata ),
    path('test_json/data/null_data/', views.load_csv_view_data_nulldata ),
    path('test_json/data/null_data/ave/', views.load_csv_view_data_nulldata_ave ),
    path('jywon_avg/', views.jywon_avg),
    path('sooyeun_avg/' , views.sooyeun_avg),
]

