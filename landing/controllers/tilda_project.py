from landingService.config import *
from landing.models.tilda_project import TildaProjectModel
import requests
from django.utils import timezone


class TildaProjectController:

    def __init__(self, project_external_id: str):
        self.project_external_id = project_external_id

    def get_project_from_tilda(self) -> dict:
        url = '%s/%s/getprojectexport/' % (TILDA_BASE_URL, TILDA_API_VERSION)

        params = {
            'publickey': TILDA_PUBLIC_KEY,
            'secretkey': TILDA_SECRET_KEY,
            'projectid': self.project_external_id
        }

        response = requests.get(url=url, params=params)
        return dict(response.json())

    @staticmethod
    def map_response_to_project(response: dict) -> TildaProjectModel():
        project = TildaProjectModel()
        project.external_id = response.get('result').get('id')
        project.title = response.get('result').get('title')
        project.description = response.get('result').get('description', '')
        return project

    def save(self):
        new_project = self.map_response_to_project(response=self.get_project_from_tilda())
        TildaProjectModel.objects.update_or_create(
            external_id=new_project.external_id,
            defaults={
                "title": new_project.title,
                "description": new_project.description,
                'date_updated': timezone.datetime.now()
            }
        )
