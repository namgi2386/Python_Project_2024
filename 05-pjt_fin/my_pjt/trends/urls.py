from django.urls import path 
from . import views

app_name = 'trends'
urlpatterns = [
    path('', views.index , name='index'),
    path('keyword/', views.keyword , name='keyword'),
    path('keyword/<int:pk>/',views.delete , name='delete'),
    path('crawling/' , views.crawling , name='crawling'),
    path('crawling/advanced/' , views.crawling_advanced , name='crawling_advanced'),
    path('crawling/histograms/', views.crawling_histograms , name='crawling_histograms'),
    path('crawling/clearTrend/', views.clearTrend , name='clearTrend')
]
