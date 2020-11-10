from django.core.management.base import BaseCommand
import telebot


def start_bot():
    bot = telebot.TeleBot(token='1497860366:AAHTluqd-5_vvsXKeN4_uJflXd-e3cXvmtg')


class Command(BaseCommand):
    help = 'run tg bot'

    def handle(self, *args, **kwargs):
        start_bot()