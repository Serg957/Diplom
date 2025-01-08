
from django.shortcuts import render
from django.http import HttpResponse
from task1.forms import UserRegister
from .models import *


def home_page(request):
    title = 'Steam Play'
    headline = 'Главная страница'
    context = {
        'title': title,
        'headline': headline,
    }
    return render(request, 'platform.html', context)


def game_page(request):
    title = 'Games'
    text = 'Игры'
    pay = 'Купить'
    games = Game.objects.all().values()
    context = {
        'title': title,
        'text': text,
        'pay': pay,
        'games': games,
    }
    return render(request, 'games.html', context)


def cart_page(request):
    title = 'Cart'
    text = 'Корзина'
    context = {
        'title': title,
        'text': text,
    }
    return render(request, 'cart.html', context)


def sign_up_by_django(request):
    info = {'error': []}
    i = 0

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if username not in get_all_users() and password == repeat_password and int(age) >= 18:
                new_user = Buyer.objects.create(name=username, balance=1000, age=int(age))
                response = HttpResponse(f'Приветствуем {new_user.name}')
                response.status_code = 201
                return response
            else:
                if username in get_all_users():
                    i += 1
                    info[f'error {i}'] = HttpResponse(f'Пользователь {username} уже существует', status=400,
                                                      reason='repeated login')
                    return HttpResponse('Пользователь уже существует', status=400, reason='repeated login')
                if password != repeat_password:
                    i += 1
                    info[f'error {i}'] = HttpResponse('Пароли не совпадают', status=400,
                                                      reason='The passwords do not match')
                    return HttpResponse('Пароли не совпадают', status=400, reason='The passwords do not match')
                if int(age) < 18:
                    i += 1
                    info[f'error {i}'] = HttpResponse(
                        'Вы должны быть старше 18 лет', status=400, reason='insufficient age')
                    return HttpResponse('Вы должны быть старше 18', status=400, reason='insufficient age')

    else:
        form = UserRegister()
        context = {'info': info, 'form': form}
        return render(request, 'registration_page.html', context)


def get_all_users():
    return Buyer.objects.all().values_list('name', flat=True)