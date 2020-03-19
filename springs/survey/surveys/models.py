from django.db import models
from core.models import TimeStampedModel

import uuid

# Create your models here.
class Survey(TimeStampedModel):
    name = models.CharField(max_length=400)
    description = models.TextField()

class Question(TimeStampedModel):
    text = models.TextField()
    survey = models.ForeignKey(Survey, related_name='questions')

class Response(TimeStampedModel):
    survey = models.ForeignKey(Survey)
    # uuid = models.CharField(max_length=400), callable
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    # Override save() when uuid are exhausted
    # def save():
        # Search field if exists
        # Regenerate while not exists()

class Answer(TimeStampedModel):
    question = models.ForeignKey(Question)
    response = models.ForeignKey(Response)
    # created_at = models.DateTimeField(auto_now_add=True)
