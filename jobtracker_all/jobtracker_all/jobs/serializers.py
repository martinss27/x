from rest_framework import serializers
from .models import JobApplication, User

class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = ['id', 'title', 'company', 'position', 'status', 'applied_date', 'notes']
        read_only_fields = ['id']

class UserSerializer(serializers.ModelSerializer):
    job_applications = JobApplicationSerializer(many=True, read_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'job_applications']
        read_only_fields = ['id']