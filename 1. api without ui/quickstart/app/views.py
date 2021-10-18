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
# Create your views here.
@csrf_exempt
def employeeListView(request):
    if request.method=='GET':
        employees=Employee.objects.all()
        serilizer=EmployeeSerializer(employees,many=True)
        return JsonResponse(serilizer.data,safe=False)
    elif request.method=='POST':
        jsondata=JSONParser().parse(request)
        serializer_d=EmployeeSerializer(data=jsondata)
        if serializer_d.is_valid():
            serializer_d.save()
            return JsonResponse(serializer_d.data,safe=False)
        else:
            return JsonResponse(serializer_d.errors,safe=False)

@csrf_exempt
def employeeDetailViewuser(request,pk):
    try:
        employee=Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return HttpResponse(status=404)


    if request.method=='DELETE':
        employee.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
    elif request.method=='GET':
        serializer=EmployeeSerializer(employee)
        return JsonResponse(serializer.data,safe=False)
    elif request.method=='PUT':
        jsondata=JSONParser().parse(request)
        serializer_d=EmployeeSerializer(employee,data=jsondata)
        if serializer_d.is_valid():
            serializer_d.save()
            return JsonResponse(serializer_d.data,safe=False)
        else:
            return JsonResponse(serializer_d.errors,safe=False)


def userListView(request):
    users=User.objects.all()
    userserializer=UserSerializer(users,many=True)
    return JsonResponse(userserializer.data,safe=False)


