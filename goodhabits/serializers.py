from rest_framework import serializers
from goodhabits.models import Habit


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'


class HabitCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        exclude = ('user',)


class HabitUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        exclude = ('user',)
