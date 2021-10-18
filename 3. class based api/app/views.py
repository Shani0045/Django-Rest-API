import json
from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from rest_framework import serializers
from rest_framework import response
from rest_framework.schemas import get_schema_view
from .models import Employee,EmployeeSerializer,userSerializer
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404

class employeeListView(APIView):
    def get(self,request):
        employees=Employee.objects.all()
        serilizer=EmployeeSerializer(employees,many=True)
        return Response(serilizer.data)
        
    def post(self,request):
        serializer_d=EmployeeSerializer(data=request.data)
        if serializer_d.is_valid():
            serializer_d.save()
            return Response(serializer_d.data)
        else:
            return Response(serializer_d.errors)


class employeeDetailViewuser(APIView):
    def get_employee(self,pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
           raise Http404

    def get(self,request,pk):
        employee=self.get_employee(pk)
        serializer=EmployeeSerializer(employee)
        return Response(serializer.data)

    def delete(self,request,pk):
        self.get_employee(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self,request,pk):
        employee=self.get_employee(pk)
        serializer_d=EmployeeSerializer(employee,data=request.data)
        if serializer_d.is_valid():
            serializer_d.save()
            return Response(serializer_d.data)
        else:
            return Response(serializer_d.errors)

class userListView(APIView):
    def get(self,request):
        users=User.objects.all()
        userserializer=userSerializer(users,many=True)
        return Response(userserializer.data)


