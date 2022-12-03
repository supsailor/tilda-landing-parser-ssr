from landingService.config import *
from landing.models.tilda_page import TildaPageModel
from landing.models.tilda_project import TildaProjectModel
import requests
from django.utils import timezone


class TildaPageController:

    def __init__(self, page_external_id: str):
        self.page_external_id = page_external_id

    def get_page_from_tilda(self) -> dict:
        url = '%s/%s/getpagefullexport/' % (TILDA_BASE_URL, TILDA_API_VERSION)

        params = {
            'publickey': TILDA_PUBLIC_KEY,
            'secretkey': TILDA_SECRET_KEY,
            'pageid': self.page_external_id
        }

        response = requests.get(url=url, params=params)
        return dict(response.json())

    @staticmethod
    def map_response_to_page(response: dict) -> TildaPageModel():
        page = TildaPageModel()
        page.external_id = response.get('result').get('id')
        page.project_id = TildaProjectModel.objects.get(external_id=response.get('result').get('projectid'))
        page.title = response.get('result').get('title')
        page.description = response.get('result').get('description', '')
        page.css = response.get('result').get('css')
        page.js = response.get('result').get('js')
        page.images = response.get('result').get('images')
        page.html = response.get('result').get('html')
        return page

    def save(self):
        response = self.get_page_from_tilda()
        page = self.map_response_to_page(response=response)
        TildaPageModel.objects.update_or_create(
            external_id=page.external_id,
            defaults={
                'project_id': page.project_id,
                'title': page.title,
                'description': page.description,
                'html': page.html,
                'date_updated': timezone.datetime.now(),
                'css': page.css,
                'js': page.js,
                'images': page.images
            }
        )
