from rest_framework.serializers import Serializer
from .models import Employee,EmployeeSerializer
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from .custompermission import MyPermission
class EmployeeViewSet(ModelViewSet):
   queryset=Employee.objects.all()
   serializer_class=EmployeeSerializer
   filterset_fields=['name']
   #authentication_classes=[BasicAuthentication]
   #permission_classes=[IsAuthenticated]
   #permission_classes=[MyPermission]
   authentication_classes=[SessionAuthentication]
   permission_classes=[IsAuthenticated]
   