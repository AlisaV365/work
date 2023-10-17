from rest_framework import generics
from goodhabits.models import Habit
from goodhabits.paginators import HabitPagination
from goodhabits.serializers import HabitSerializer, HabitCreateSerializer, HabitUpdateSerializer


class HabitListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    pagination_class = HabitPagination

    def get_queryset(self):
        user = self.request.user
        return Habit.objects.filter(user=user)


class PublicHabitListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer

    def get_queryset(self):
        return Habit.objects.filter(sign_of_publicity=True)


class HabitCreateAPIView(generics.CreateAPIView):
    serializer_class = HabitCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class HabitUpdateAPIView(generics.UpdateAPIView):
    serializer_class = HabitUpdateSerializer

    def get_queryset(self):
        user = self.request.user
        return Habit.objects.filter(user=user)


class HabitDeleteAPIView(generics.DestroyAPIView):
    serializer_class = HabitSerializer

    def get_queryset(self):
        user = self.request.user
        return Habit.objects.filter(user=user)
