from rest_framework import generics, permissions
from goodhabits.models import Habit
from goodhabits.paginators import HabitPagination
from goodhabits.serializers import HabitSerializer, HabitCreateSerializer, HabitUpdateSerializer


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Пользователь может редактировать или удалять только свои привычки.
    """

    def has_object_permission(self, request, view, obj):
        # Проверяем, является ли пользователь владельцем данного объекта
        return obj.user == request.user


class HabitListAPIView(generics.ListAPIView):
    """ API для списка привычек."""
    serializer_class = HabitSerializer
    pagination_class = HabitPagination
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Habit.objects.filter(user=user)


class PublicHabitListAPIView(generics.ListAPIView):
    """
    Пользователь может видеть список публичных привычек (без возможности их как-то редактировать или удалять).
    """
    serializer_class = HabitSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Habit.objects.filter(sign_of_publicity=True)


class HabitCreateAPIView(generics.CreateAPIView):
    """ ОСоздание привычки """
    serializer_class = HabitCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class HabitUpdateAPIView(generics.UpdateAPIView):
    """ Обновление привычки """
    serializer_class = HabitUpdateSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        return Habit.objects.filter(user=user)


class HabitDeleteAPIView(generics.DestroyAPIView):
    """ Удаления привычки """
    serializer_class = HabitSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        return Habit.objects.filter(user=user)
