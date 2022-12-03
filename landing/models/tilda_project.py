from django.utils import timezone
from django.db import models
from django.db.models import UUIDField
from typing import Union
from uuid import UUID, uuid4


class TildaProjectModel(models.Model):
    id: Union[UUID, UUIDField] = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True)
    external_id: str = models.TextField(null=False, blank=False)
    title: str = models.TextField(null=False, blank=True)
    description: str = models.TextField(null=False, blank=True)
    date_created: timezone.datetime = models.DateTimeField(null=False, blank=False, editable=False,
                                                           default=timezone.now)
    date_updated: timezone.datetime = models.DateTimeField(null=False, blank=False, default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "tilda_project"
