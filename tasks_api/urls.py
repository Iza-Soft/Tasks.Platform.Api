from django.urls import path, include
# from rest_framework.routers import DefaultRouter

from tasks_api import views

# router = DefaultRouter()
# router.register('workspace', views.WorkSpaceApiView.as_view())

urlpatterns = [
    path('workspace/', views.WorkSpaceApiView.as_view()),
    path('workspace/<int:workspace_id>/',  views.WorkSpaceDetailsApiView.as_view()),
    path('task/', views.TaskApiView.as_view()),
    #path('', include(router.urls))
]