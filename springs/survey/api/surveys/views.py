from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated

from .serializers import SurveySerializer, ResponseSerializer
from surveys.models import Survey, Response

class SurveyViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    model = Survey
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer

class ResponseViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    model = Response
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer
    permission_classes = [IsAuthenticated]

    # list()
    # create()

survey_list = SurveyViewSet.as_view({
    'get': 'list'
})

response_list = ResponseViewSet.as_view({
    'post': 'create',
    'get': 'list'
})
