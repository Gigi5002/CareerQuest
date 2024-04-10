from .models import Employer, JobSeeker
from rest_framework import serializers


class EmployerListCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employer
        fields = '__all__'

    def create(self, validated_data):
        user = Employer(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            if field == 'password':
                instance.set_password(value)
            else:
                setattr(instance, field, value)
        instance.save()
        return instance


class JobSeekerListCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = JobSeeker
        fields = '__all__'

    def create(self, validated_data):
        user = JobSeeker(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            if field == 'password':
                instance.set_password(value)
            else:
                setattr(instance, field, value)
        instance.save()
        return instance


class ProfileEmployerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employer
        fields = '__all__'


class ProfileJobSeekerSerializer(serializers.ModelSerializer):

    class Meta:
        model = JobSeeker
        fields = '__all__'
