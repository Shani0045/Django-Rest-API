import json
from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from rest_framework import serializers
from .models import Employee
from .serializer import EmployeeSerializer,UserSerializer
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
@api_view(['GET','POST'])
def employeeListView(request):
    if request.method=='GET':
        employees=Employee.objects.all()
        serilizer=EmployeeSerializer(employees,many=True)
        return Response(serilizer.data)
    elif request.method=='POST':
        serializer_d=EmployeeSerializer(data=request.data)
        if serializer_d.is_valid():
            serializer_d.save()
            return Response(serializer_d.data)
        else:
            return Response(serializer_d.errors)

@api_view(['GET','PUT','DELETE'])
def employeeDetailViewuser(request,pk):
    try:
        employee=Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return Response(status=404)
    if request.method=='DELETE':
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method=='GET':
        serializer=EmployeeSerializer(employee)
        return Response(serializer.data)
    elif request.method=='PUT':
        serializer_d=EmployeeSerializer(employee,data=request.data)
        if serializer_d.is_valid():
            serializer_d.save()
            return Response(serializer_d.data)
        else:
            return Response(serializer_d.errors)

@api_view(['GET'])
def userListView(request):
    if request.method=='GET':
        users=User.objects.all()
        userserializer=UserSerializer(users,many=True)
        return Response(userserializer.data)


