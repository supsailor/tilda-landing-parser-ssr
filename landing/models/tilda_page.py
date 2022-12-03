from django.utils import timezone
from django.db import models
from django.db.models import UUIDField
from typing import Union
from uuid import UUID, uuid4
from landing.models.tilda_project import TildaProjectModel


class TildaPageModel(models.Model):
    id: Union[UUID, UUIDField] = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True)
    external_id: str = models.TextField(null=False, blank=False)
    project_id: TildaProjectModel = models.ForeignKey(to=TildaProjectModel, null=False, blank=False,
                                                      on_delete=models.CASCADE)
    title: str = models.TextField(null=False, blank=False)
    description: str = models.TextField(null=False, blank=True)
    css = models.JSONField()
    js = models.JSONField()
    images = models.JSONField()
    date_created: timezone.datetime = models.DateTimeField(null=False, blank=False, editable=False,
                                                           default=timezone.now)
    date_updated: timezone.datetime = models.DateTimeField(null=False, blank=False, default=timezone.now)
    html: str = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "tilda_page"
