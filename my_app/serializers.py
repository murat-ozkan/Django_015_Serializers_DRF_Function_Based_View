from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        # fields = ['number', 'first_name', 'last_name']
        fields = '__all__'
        # exclude = ['id']