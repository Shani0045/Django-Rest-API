
from django.contrib import admin
from django.urls import path
from app.views import employeeListView,employeeDetailViewuser,userListView
urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/employees/",employeeListView.as_view()),
    path("api/employee/<int:pk>",employeeDetailViewuser.as_view()),
    path("api/user",userListView.as_view())
    
]
