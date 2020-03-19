from django.db import models
from django.contrib.auth.models import User

# Create your models here.

status_choices = (
    ('Active', 'active'),
    ('Archived', 'archived'),
    ('Deleted', 'deleted'),
)


class Survey(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    first_smoking_age = models.IntegerField(null=True)
    first_drinking_age = models.IntegerField(null=True)

    def __str__(self):
        return self.name


class SurveyType(models.Model):
    type = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='created_by')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='updated_by')
    status = models.CharField(max_length=200, choices=status_choices, default='Active')
    description = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.type


class Vote(models.Model):
    type_id = models.ForeignKey(SurveyType, on_delete=models.CASCADE)
