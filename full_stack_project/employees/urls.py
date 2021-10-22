from django.urls import path, include
<<<<<<< HEAD

urlpatterns = [

=======
from . import views
from rest_framework import routers
router = routers.DefaultRouter()
router.register('employees-api', views.EmployeeView)

urlpatterns = [
path('employees-api', include(router.urls))
>>>>>>> b481b53 (commit_3)
]