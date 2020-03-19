from graphene_django.types import DjangoObjectType

from surveys.models import Survey, Question

class SurveyType(DjangoObjectType):
    class Meta:
        model = Survey

class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
