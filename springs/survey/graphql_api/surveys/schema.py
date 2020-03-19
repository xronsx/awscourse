import graphene

from surveys.models import Survey, Question
from .types import SurveyType, QuestionType

class SurveyQueries(object):
    surveys = graphene.List(SurveyType)
    questions = graphene.List(QuestionType)
    survey = graphene.Field(
        SurveyType,
        id=graphene.Argument(graphene.ID, required=False),
        description='Lookup a category by ID or pk.'
    )

    def resolve_surveys(self, info, **kwargs):
        return Survey.objects.all()

    def resolve_questions(self, info, **kwargs):
        return Question.objects.all()
