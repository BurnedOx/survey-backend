from django.db import models

# Create your models here.

class Survey(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    first_smoking_age = models.IntegerField(null=True)
    first_drinking_age = models.IntegerField(null=True)

    def __str__(self):
        return self.name
