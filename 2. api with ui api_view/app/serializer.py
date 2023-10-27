from django.contrib.auth.models import User
from .models import Employee
from rest_framework import serializers
class EmployeeSerializer(serializers.ModelSerializer):
    # emp_name = serializers.CharField(source="name")  # renaming the exiting model field name name to emp_name
    class Meta:
        model=Employee
        fields="__all__"   # or  ['name','email']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if representation.get("name") == "shani":
            representation["name"]=self.context.get("name", "").title()
        else:
            representation["name"] = representation.get("name", "").title()

        return representation


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields="__all__"
    