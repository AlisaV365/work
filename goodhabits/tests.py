from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

import users
from users.models import User
from goodhabits.models import Habit
from goodhabits.serializers import HabitSerializer


class HabitCreateAPIViewTest(APITestCase):
    def setUp(self) -> None:

        self.user = User.objects.create(
            email='avt758018@yandex.ru'
        )

        self.client = APIClient()
        self.client.force_authenticate(user=self.user)  # Аутентифицировать пользователя

        self.habit = Habit.objects.create(
            user=self.user,
            place='test place',
            act='test act',
            periodicity=1,
            time='12:00:00',
            execution_time='10'
        )

    def test_create_habit(self):
        """ Тестирование создания привычки """
        data = {
            'user': self.user.pk,
            'place': 'test place',
            'act': 'test act',
            'time': '12:00:00',
            'periodicity': 1,
            'reward': 'test reward',
            'execution_time': 60,
        }

        # Отправка POST-запроса для создания привычки
        response = self.client.post(
            reverse('goodhabits:habits_create'),
            data=data,
        )

        print(response.json())

        # Проверка статуса ответа
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED)

        # Проверка, что привычка действительно создана
        self.assertEqual(
            Habit.objects.count(), 2)

        # Проверка, что привычка принадлежит текущему пользователю
        self.assertEqual(
            Habit.objects.first().user,
            self.user)

        # Проверка данных созданной привычки
        self.assertEqual(
            response.json(),
            {
                'id': 2,
                'place': 'test place',
                'act': 'test act',
                'time': '12:00:00',
                'sign_of_good_habit': False,
                'periodicity': 1,
                'reward': 'test reward',
                'execution_time': 60,
                'related_habit': None,
                'sign_of_publicity': False
            }
        )

    def test_list_habits(self):
        """ Тестирование вывода списка привычек """

        Habit.objects.create(
            user=self.user,
            place='Work',
            time='09:00',
            act='Read',
            execution_time=60,
            reward='test'
        )

        response = self.client.get(
            reverse('goodhabits:habits_list')

        )

        print(response.json())

        self.client.force_authenticate(
            user=self.user
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        # Сериализуем привычки и сравниваем с результатом запроса
        habits = Habit.objects.filter(user=self.user)
        serializer = HabitSerializer(habits, many=True)
        self.assertEqual(
            response.json()['results'],
            serializer.data
        )

    def test_update_habit(self):
        """Тестирование редактирования привычки"""

        data = {
            'place': 'Test update place',
            'act': 'Test update act',
            'user': self.user.pk,
            'time': '13:15:00',
            'periodicity': 2,
            'reward': 'test new reward',
            'execution_time': 22,
        }

        response = self.client.put(
            reverse('goodhabits:habits_update', kwargs={"pk": self.habit.pk}),
            data=data
        )

        print(response.data)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json()['place'],
            'Test update place'
        )

        self.assertEqual(
            response.json()['act'],
            'Test update act'
        )

        self.assertEqual(
            response.json()['periodicity'],
            2
        )

    def test_delete_habit(self):
        """Тестирование удаления привычки"""
        url = reverse(
            'goodhabits:habits_delete', args=[self.habit.pk]
        )

        response = self.client.delete(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertFalse(
            Habit.objects.filter(pk=self.habit.pk).exists()
        )

