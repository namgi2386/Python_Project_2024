from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import GameSession

import random


# 사용자에게 게임 화면을 출력
# -> 정답을 함께 생성
# 정답: 1~100 사이의 정수
def start_game(request):
    target_number = random.randint(1, 100)
    game_session = GameSession.objects.create(target_number=target_number)
    context = {
        'target_number': target_number,
        'game_session_id': game_session.id,
    }

    return render(request, 'games/game.html', context)


# 사용자의 추측 번호를 전달 받을 것
# DB에 정답이 저장되어 있는데
# 어...?? 어떻게 현재 게임의 정답을 가져올까 ?
# -> 파라미터로 session_id 도 전달
def make_guess(request, game_session_id):
    game_session = get_object_or_404(GameSession, id=game_session_id)
    if request.method == 'POST':
        print("request.POST = ", request.POST)
        user_guess = int(request.POST.get('user_guess'))

        message = ''
        if user_guess < 1 or user_guess > 100:
            message = "1~100 사이 숫자만 입력하세요."
        elif user_guess > game_session.target_number:
            message = 'DOWN!'
            game_session.user_guess = user_guess
            game_session.attempts += 1
            game_session.save()
        elif user_guess < game_session.target_number:
            message = 'UP!'
            game_session.user_guess = user_guess
            game_session.attempts += 1
            game_session.save()
        else:
            message = '정답입니다!'
            game_session.attempts += 1
            game_session.save()
        
        response_data = {
            'message': message,
            'attempts': game_session.attempts
        }
        return JsonResponse(response_data)
    else:
        return JsonResponse({ 'error': 'Invalid Http Method!' })
