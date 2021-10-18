from django.contrib import admin
from django.urls import path
from app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("employees/",views.EmployeeList.as_view()),
    path("employee/<int:pk>",views.EmployeeCrud.as_view()),
]
