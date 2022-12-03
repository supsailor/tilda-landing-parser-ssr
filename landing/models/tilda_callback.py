from django.utils import timezone
from django.db import models
from django.db.models import UUIDField
from typing import Union
from uuid import UUID, uuid4


class TildaCallbackModel(models.Model):
    id: Union[UUID, UUIDField] = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True)
    page_id: str = models.TextField(null=False, blank=False)
    project_id: str = models.TextField(null=False, blank=False)
    published: timezone.datetime = models.DateTimeField(null=False, blank=False)
    public_key: str = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.id

    class Meta:
        db_table = "tilda_callback"
