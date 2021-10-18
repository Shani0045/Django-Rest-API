
from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from rest_framework.schemas import get_schema_view
from rest_framework.serializers import Serializer
from .models import Employee,EmployeeSerializer
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework import mixins,generics
from rest_framework.response import Response

class EmployeeList(generics.ListCreateAPIView):
   queryset=Employee.objects.all()
   serializer_class=EmployeeSerializer

class EmployeeCrud(generics.RetrieveUpdateDestroyAPIView):
   queryset=Employee.objects.all()
   serializer_class=EmployeeSerializer
