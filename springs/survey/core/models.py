# Django libraries
# 3rd party libraries
# Standard/core python libraries
# Our custom libraries
from django.db import models
from django.utils import timezone
from django.db.models.query import QuerySet

class SoftDeletionQuerySet(QuerySet):
    def delete(self):
        return super(SoftDeletionQuerySet, self).update(deleted_at=timezone.now)

    def hard_delete(self):
        return super(SoftDeletionQuerySet, self).delete()

class SoftDeletionManager(models.Manager):
    def __init__(self,  *args, **kwargs):
        self.alive_only = kwargs.pop('alive_only', True)
        return super(SoftDeletionManager, self).__init__(*args, **kwargs)

    def get_queryset(self):
        if self.alive_only: # Base case
            return SoftDeletionQuerySet(self.model).filter(deleted_at=None)
        return SoftDeletionQuerySet(self.model)

# Create your models here.
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    objects = SoftDeletionManager()
    all_objects = SoftDeletionManager(alive_only=False)

    class Meta:
        abstract = True

    # create, delete -> standard methods of Model
    def delete(self):
        self.deleted_at = timezone.now()
        self.save()
