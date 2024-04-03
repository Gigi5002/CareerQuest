from rest_framework import serializers
from .models import (Vacancy, Chosen,
                     Response, Category, Industry,
                     Speciality, Experience, Employer)


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title',)


class IndustryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = ('title',)


class SpecialityListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speciality
        fields = ('title',)


class ExperienceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ('title',)


class EmployerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = ('company_name',)


class VacancyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = '__all__'


class StatusListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ('status',)


class VacancyListSerializer(serializers.ModelSerializer):
    category = CategoryListSerializer(many=True)
    industry = IndustryListSerializer(many=True)
    specializing = SpecialityListSerializer(many=True)
    experience = ExperienceListSerializer(many=True)
    company = EmployerListSerializer(many=True)
    status = StatusListSerializer()

    class Meta:
        model = Vacancy
        fields = ('id',
                  'industry',
                  'category',
                  'specializing',
                  'experience',
                  'salary',
                  'status',
                  'location',
                  'company',
                  'published_date',
                  )


class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Response
        fields = '__all__'


class ResponseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Response
        fields = '__all__'


class ChosenSerializer(serializers.ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Chosen
        fields = '__all__'
