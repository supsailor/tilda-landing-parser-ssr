from django.http.request import QueryDict
from landing.models.tilda_callback import TildaCallbackModel
from django.core.exceptions import ValidationError
from landing.tasks import update_project
from django.utils import timezone


class TildaCallbackController:

    @staticmethod
    def validate_page_id(page_id: str):
        if page_id == '' or page_id is None:
            raise ValidationError('pageId is null')

    @staticmethod
    def validate_project_id(project_id: str):
        if project_id == '' or project_id is None:
            raise ValidationError('projectId is null')

    @staticmethod
    def validate_published(published: str):
        if published == '' or published is None:
            raise ValidationError('published is null')
        try:
            timezone.datetime.strptime(published, '%Y-%m-%dT%H:%M:%S')
        except ValueError:
            raise ValidationError("Incorrect data format, should be %Y-%m-%dT%H:%M:%S")

    @staticmethod
    def validate_public_key(public_key: str):
        if public_key != '123':
            raise ValidationError('incorrect public key')

    def validate_callback(self, query_list: QueryDict):
        self.validate_public_key(public_key=query_list.get('publicKey', None))
        self.validate_page_id(page_id=query_list.get('pageId', None))
        self.validate_project_id(project_id=query_list.get('projectId', None))
        self.validate_published(published=query_list.get('published', None))

    def save_callback(self, query_list: QueryDict):
        self.validate_callback(query_list=query_list)
        callback = TildaCallbackModel(
            page_id=query_list.get('pageId', None),
            project_id=query_list.get('projectId', None),
            published=timezone.datetime.strptime(query_list.get('published', None), "%Y-%m-%dT%H:%M:%S"),
            public_key=query_list.get('publicKey', None)
        )
        callback.save()
        update_project.delay(project_id=callback.project_id, page_id=callback.page_id)
