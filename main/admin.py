from django.contrib import admin
from .models import Survey, SurveyType

# Register your models here.

admin.site.register(Survey)
admin.site.register(SurveyType)
