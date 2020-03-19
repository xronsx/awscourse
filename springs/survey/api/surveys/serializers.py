from rest_framework import serializers
from surveys.models import Response, Survey

class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ('id', 'name', 'description')

class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Response
        fields = ('survey', 'uuid')
        extra_kwargs = {
            'uuid': {
                'read_only': True
            },
            'survey': {
                'required': True
            }
        }
