from landingService.celery import app

from landing.controllers.tilda_page import TildaPageController
from landing.controllers.tilda_project import TildaProjectController


@app.task(name='update landing')
def update_project(project_id, page_id):
    #TildaProjectController(project_external_id=project_id).save()
    TildaPageController(page_external_id=page_id).save()
