from django.db import models
from django.conf import settings

NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    place = models.CharField(max_length=250, verbose_name='место')
    time = models.TimeField(verbose_name='время')
    act = models.TextField(verbose_name='действие')
    sign_of_good_habit = models.BooleanField(default=False, verbose_name='пизнак приятной привычки')
    related_habit = models.ForeignKey('self', on_delete=models.CASCADE, **NULLABLE, verbose_name='связанная привычка')
    periodicity = models.PositiveIntegerField(default=1, verbose_name='периодичность')  # по умолчанию ежедневно
    reward = models.TextField(verbose_name='вознаграждение')
    execution_time = models.PositiveIntegerField(verbose_name='время на выполнение')
    sign_of_publicity = models.BooleanField(default=False, verbose_name='признак публичности')

    def __str__(self):
        return f'Я буду {self.act} в ({self.time}) в ({self.place})'

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'
