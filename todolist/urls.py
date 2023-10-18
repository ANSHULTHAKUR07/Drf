from django.urls import path,include
from.views import *
from rest_framework.routers import DefaultRouter
from todolist.views import TaskModelViewSet
from rest_framework import renderers
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'taskapi', TaskModelViewSet,basename='taskapi')

app_name = 'todolist'
urlpatterns = [
    path('user',UserAPIView.as_view(),name='userview'),
    path('checkmate/', CheckAPIView.as_view(),name = "checkmate"),
    path('tags', TagAPIView.as_view(),name = "tag"),
    path('tasks', TaskAPIView.as_view(),name = "task"),
    path('logout',LogoutAPIView.as_view(),name="logout"),
    path('checkapi',checkAPIView.as_view(),name="checkapi"),
    path('createuser',CreateUserAPIView.as_view(),name="createuser"),
    path('retrieveupdatedelete/<int:pk>',RetrieveDleteDetailView.as_view(),name='retrieveupdatedelete'),
    path('retrieveupdate/<int:pk>',RetriveUpdateAPIView.as_view(),name='retrieveupdate'),
    path('retrievedelete/<int:pk>',RetriveDestroyAPIView.as_view(),name='retrievedelete'),
    path('taskapiview/', TaskGenericViewSet.as_view({'get':'get_filtered_tasks', 'post':'create', 'get':'list'}),name='taskapiview'),
    
   
] + router.urls

print(urlpatterns)
