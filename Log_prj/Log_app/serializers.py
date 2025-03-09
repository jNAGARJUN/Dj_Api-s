from rest_framework import serializers
from .models import EmpDetails
# from django.contrib.auth.hashers import make_password, check_password

class EmpDetailsSerializer(serializers.ModelSerializer):
        class Meta:
            model = EmpDetails
            fields = ['emp_id', 'username', 'email', 'password']


