from django.contrib.auth.models import User
from .models import Employee
from rest_framework import serializers
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields="__all__"   # or  ['name','email']
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields="__all__"
    