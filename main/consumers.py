from channels.generic.websocket import AsyncWebsocketConsumer
import json
from .models import Survey
from .utils import *


class SurveyConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        data = survey_analysis()

        await self.channel_layer.group_add(
            'global',
            self.channel_name
        )

        await self.accept()

        await self.send(text_data=json.dumps({
            'totalSurvey': data['total_survey'],
            'population': data['age_avg'],
            'smoking': data['smoking_avg'],
            'drinking': data['drinking_avg']
        }))

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            'global',
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        name = text_data_json['name']
        age = text_data_json['age']
        smoking = text_data_json['smoking']
        drinking = text_data_json['drinking']

        await store_sarvey(name, age, smoking, drinking)
        data = survey_analysis()

        await self.channel_layer.group_send(
            'global',
            {
                'type': 'survey_data',
                'totalSurvey': data['total_survey'],
                'population': data['age_avg'],
                'smoking': data['smoking_avg'],
                'drinking': data['drinking_avg']
            }
        )

    async def survey_data(self, event):
        await self.send(text_data=json.dumps({
            'totalSurvey': event['totalSurvey'],
            'population': event['population'],
            'smoking': event['smoking'],
            'drinking': event['drinking']
        }))
