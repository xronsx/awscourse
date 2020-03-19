from django.conf.urls import url, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from ..surveys import views as survey_views

urlpatterns = [
    # auth
    url(r'^auth/login/', TokenObtainPairView.as_view()),
    url(r'^surveys/', survey_views.survey_list),
    url(r'^responses/', survey_views.response_list)
]
