from django.contrib.auth.models import User
from .models import Employee
from string import punctuation
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
class EmployeeSerializer(serializers.ModelSerializer):
    # emp_name = serializers.CharField(source="name")  # renaming the exiting model field name name to emp_name
    class Meta:
        model=Employee
        fields="__all__"   # or  ['name','email']

    # for response data modification
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if representation.get("name") == "shani":
            representation["name"]=self.context.get("name", "").title()
        else:
            representation["name"] = representation.get("name", "").title()

        return representation

    # check for request data and process the specific data
    # def to_internal_value(self, data):
    #     resource_data = data['resource']
    #     return super().to_internal_value(resource_data)


    def validate_phone(self, value):   # check for specific field like phone
        if not value.startswith("+91"):
            raise serializers.ValidationError("phone no should starts with +91")
        return value
    
    # for request check and validate requested data
    def validate(self, data):   # check for all fields
        if not any(i in punctuation for i in data.get("password")):
            raise serializers.ValidationError("password should contains at least one special characters")
        return data
    
    



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields="__all__"
    