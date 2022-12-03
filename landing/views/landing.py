from django.shortcuts import render
from landing.models.tilda_project import TildaProjectModel
from landing.models.tilda_page import TildaPageModel

def landing(request, page_id):
    #this_project = TildaProjectModel.objects.get(external_id=project_id)
    this_page = TildaPageModel.objects.get(external_id=page_id)

    context = {"page": this_page}

    return render(request, 'landing/landing.html', context=context)