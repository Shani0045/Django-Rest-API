
from django.contrib import admin
from django.urls import path
from app.views import employeeListView,employeeDetailViewuser,userListView
urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/employee",employeeListView),
    path("api/employee/<int:pk>",employeeDetailViewuser),
    path("api/user",userListView)
]
