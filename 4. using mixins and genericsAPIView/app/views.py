
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

class EmployeeList(mixins.ListModelMixin,mixins.CreateModelMixin, generics.GenericAPIView):
   queryset=Employee.objects.all()
   serializer_class=EmployeeSerializer
   def get(self,request):
      return self.list(request)

   def post(self,request):
      return self.create(request)

class EmployeeCrud(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
   queryset=Employee.objects.all()
   serializer_class=EmployeeSerializer
   def get(self,request,pk):
      return self.retrieve(request,pk)
   def put(self,request,pk):
      return self.update(request,pk)
   def delete(self,request,pk):
      return self.destroy(request,pk)