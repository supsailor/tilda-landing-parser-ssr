from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .api.tilda_callback import TildaCallbackApi
from .api.tilda_page import TildaPageSingleApi, TildaPageListApi
from .api.tilda_project import TildaProjectSingleApi, TildaProjectListApi
from .views.landing import landing

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.


urlpatterns = [
    path('callback/', TildaCallbackApi.as_view()),
    path('page/<str:pk>', TildaPageSingleApi.as_view()),
    path('page/', TildaPageListApi.as_view()),
    path('project/<str:pk>', TildaProjectSingleApi.as_view()),
    path('project/', TildaProjectListApi.as_view()),
    path('<str:page_id>/', landing)
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])
