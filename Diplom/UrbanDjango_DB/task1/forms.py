from django import forms

class UserRegister(forms.Form):
    username = forms.CharField(max_length=30, label='Введите логин')
    password = forms.CharField(min_length=8, label='Введите пароль', strip=False)
    repeat_password = forms.CharField(min_length=8, label='Повторите пароль', strip=False)
    age = forms.CharField(max_length=3, label='Введите возраст')
    subscribe = forms.BooleanField(required=False, label='Зарегистрироваться')