from rest_framework.serializers import Serializer
from .models import Employee,EmployeeSerializer
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

class EmployeeViewSet(ModelViewSet):
   queryset=Employee.objects.all()
   serializer_class=EmployeeSerializer