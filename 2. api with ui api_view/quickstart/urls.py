
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('docs/', include_docs_urls(title='My Custom API Docs', permission_classes=[])),
    path('admin/', admin.site.urls),
    path("",include("app.urls")),
    path("api",include("app.urls")),
]
