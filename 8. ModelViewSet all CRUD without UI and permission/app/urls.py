from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from app import views

router=DefaultRouter()
router.register("employeeapi",views.EmployeeViewSet,basename="employee")

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include(router.urls)) 
]
