from django.urls import path, include
from rest_framework import routers
from .views import EmployeModelViewSet

router = routers.DefaultRouter()
router.register(r'employecrud', EmployeModelViewSet)

app_name = 'practisedrf'
urlpatterns = [
    path('', include(router.urls)),
] 