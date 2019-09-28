from .models import Survey
from django.db.models import Avg
from channels.db import database_sync_to_async


@database_sync_to_async
def store_sarvey(name, age, smoking, drinking):
    Survey.objects.get_or_create(
        name=name,
        age=int(age),
        first_smoking_age=int(smoking) if smoking is not '' else None,
        first_drinking_age=int(drinking) if drinking is not '' else None
    )


def survey_analysis():
    return {
        'total_survey': len(Survey.objects.all()),
        'age_avg': round(Survey.objects.aggregate(Avg('age'))['age__avg'], 2),
        'smoking_avg': round(Survey.objects.aggregate(Avg('first_smoking_age'))['first_smoking_age__avg'], 2),
        'drinking_avg': round(Survey.objects.aggregate(Avg('first_drinking_age'))['first_drinking_age__avg'], 2)
    }
