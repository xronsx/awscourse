import graphene

from surveys.models import Survey
from .surveys.types import SurveyType
from .surveys.schema import SurveyQueries

class Query(SurveyQueries, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, auto_camelcase=False)
