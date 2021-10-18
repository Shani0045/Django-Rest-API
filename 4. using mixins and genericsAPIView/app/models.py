from django.db import models
from rest_framework import serializers
from django.contrib.auth.models import User
# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    password=models.CharField(max_length=30)
    phone=models.CharField(max_length=10)

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields="__all__"

