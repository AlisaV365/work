from django.urls import path
from . import views
import telebot

urlpatterns = [
    path('6686791128:AAHxQRTi36OKijSyzMACSAHu4hI_jGjFQY8/', views.webhook),
]
