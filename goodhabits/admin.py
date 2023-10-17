from django.contrib import admin

from goodhabits.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ('user', 'place', 'time', 'act', 'periodicity', 'reward', 'sign_of_publicity')
