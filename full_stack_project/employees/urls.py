from django.urls import path, include
from . import views
from rest_framework import routers
router = routers.DefaultRouter()
router.register('employees', views.EmployeeView),
router.register('title', views.TitleView),
router.register('specialist', views.SpecialistView),
router.register('manager', views.ManagerView),
router.register('employee_id', views.Employee_IDView)

urlpatterns = [
    path('employees-api', include(router.urls)),
    path('', views.homepage, name='home'),
    path('<slug:slug>/', views.details, name='details')
]

