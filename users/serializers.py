from .models import Employer, JobSeeker
from rest_framework import serializers


class EmployerListCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employer
        fields = '__all__'


class JobSeekerListCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = JobSeeker
        fields = '__all__'


class ProfileEmployerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employer
        fields = '__all__'


class ProfileJobSeekerSerializer(serializers.ModelSerializer):

    class Meta:
        model = JobSeeker
        fields = '__all__'
