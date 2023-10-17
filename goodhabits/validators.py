from django.core.exceptions import ValidationError


def validate_habit(instance):
    if instance.sign_of_good_habit and instance.reward:
        raise ValidationError("У приятной привычки не может быть указано вознаграждение.")

    if instance.sign_of_good_habit and instance.related_habit:
        raise ValidationError("Связанной привычкой может быть только привычка с признаком приятной привычки.")

    if instance.periodicity > 7:
        raise ValidationError('Привычка не может быть выполняется реже, чем 1 раз в 7 дней.')

    if instance.execution_time > 120:
        raise ValidationError("Время выполнения не может превышать 120 секунд.")
