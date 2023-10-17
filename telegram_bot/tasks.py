from telebot import TeleBot
from celery import shared_task
from goodhabits.models import Habit

bot = TeleBot('6686791128:AAHxQRTi36OKijSyzMACSAHu4hI_jGjFQY8')

@shared_task
def habits_notification(object_pk):
    # Получите привычку на основе object_pk
    habit = Habit.objects.get(pk=object_pk)

    habit_act = habit.act
    habit_time = habit.time
    habit_place = habit.place

    message = f'Трекер привычек напоминает: требуется совершить {habit_act} в {habit_time} в {habit_place}'
    bot.send_message(habit.creator.chat_id, message)