from django.urls import path
from .views import HabitListAPIView, PublicHabitListAPIView, HabitCreateAPIView, HabitUpdateAPIView, HabitDeleteAPIView

from goodhabits.apps import GoodhabitsConfig

app_name = GoodhabitsConfig.name

urlpatterns = [
    path('habits/', HabitListAPIView.as_view(), name='habits_list'),
    path('public-habits/', PublicHabitListAPIView.as_view(), name='public_habit_list'),
    path('habits/create/', HabitCreateAPIView.as_view(), name='habits_create'),
    path('habits/update/<int:pk>/', HabitUpdateAPIView.as_view(), name='habits_update'),
    path('habits/delete/<int:pk>/', HabitDeleteAPIView.as_view(), name='habits_delete'),

]
