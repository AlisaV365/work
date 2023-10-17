from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import telebot

bot = telebot.TeleBot('6686791128:AAHxQRTi36OKijSyzMACSAHu4hI_jGjFQY8')


@csrf_exempt
def webhook(request):
    json_string = request.body.decode('UTF-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return HttpResponse("")


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # Обработка входящих сообщений от пользователей
    pass
