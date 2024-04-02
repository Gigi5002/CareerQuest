from .models import Employer, JobSeeker, User, UserType
from rest_framework import serializers


class EmployerListCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employer
        fields = '__all__'


class JobSeekerListCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = JobSeeker
        fields = '__all__'


