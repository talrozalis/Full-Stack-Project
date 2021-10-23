from rest_framework import serializers
from .models import Employee, Title, Specialist, Manager, Employee_ID

class Employee_IDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee_ID
        fields = ['id', 'url', 'employee_id']

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'url', 'first_name', 'last_name', 'employee_id', 'email_address', 'phone_number', 'hire_date', 'salary', 'title']

class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Title
        fields = ['id', 'url', 'title', 'specialist']

class SpecialistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialist
        fields = ['id', 'url', 'specialist']

class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = ['id', 'url', 'manager_details', 'direct_reporter_id']

