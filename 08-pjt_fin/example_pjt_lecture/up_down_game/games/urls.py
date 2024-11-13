from django.urls import path
from . import views

app_name="games"
urlpatterns = [
    path('start/', views.start_game, name="start_game"), # 1. 게임 화면 출력
    path('make-guess/<int:game_session_id>/', views.make_guess, name="make_guess"),# 2. 정답을 체크할 수 있는 URL
]
