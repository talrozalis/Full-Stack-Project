from django.urls import path, include
from . import views
from rest_framework import routers
router = routers.DefaultRouter()
router.register('employees-api', views.EmployeeView)

urlpatterns = [
path('employees-api', include(router.urls))
]
