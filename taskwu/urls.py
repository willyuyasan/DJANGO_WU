from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from taskwu import views



#Procedure for generationg all the possible views (GET, PUT, POST, DELETE)
router = routers.DefaultRouter()
router.register(r'tasks', views.TaskView)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('docs/', include_docs_urls(title='Tasks API'))
]
