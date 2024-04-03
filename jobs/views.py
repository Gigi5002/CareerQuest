from rest_framework import generics
from .models import Vacancy,Chosen
from users.models import UserType
from .serializers import (
    VacancyListSerializer,
    ResponseSerializer, VacancyCreateSerializer,
    ChosenSerializer
)

from rest_framework.exceptions import PermissionDenied, NotFound
from .paginations import VacancyPagination
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .filters import VacancyFilter


class VacancyListView(generics.ListAPIView):
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    queryset = Vacancy.objects.all()
    serializer_class = VacancyListSerializer
    filterset_class = VacancyFilter
    pagination_class = VacancyPagination
    search_fields = ['jobs__category']
    ordering_fields = ['jobs__salary']


class VacancyCreateView(generics.CreateAPIView):
    serializer_class = VacancyCreateSerializer

    def perform_create(self, serializer):
        user = self.request.user
        if user.user_type == UserType.employers:
            serializer.save(employer=user)
        else:
            raise PermissionDenied("Only employers can create vacancies")


class ResponseCreateView(generics.CreateAPIView):
    serializer_class = ResponseSerializer

    def perform_create(self, serializer):
        user = self.request.user
        if user.user_type == UserType.job_seeker:
            serializer.save(user=user)
        else:
            raise PermissionDenied("На вакансии могут откликаться только соискатели работы")


class ChosenListCreateView(generics.ListCreateAPIView):
    serializer_class = ChosenSerializer

    def get_queryset(self):
        user = self.request.user
        if not user.is_authenticated:
            raise PermissionDenied("You must be logged in to view this content")
        queryset = Chosen.objects.filter(user=user)
        if not queryset.exists():
            raise NotFound("No chosen items found for this user")
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)