from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Vacancy, Response, Chosen
from .serializers import (
    VacancyListSerializer,
    ResponseCreateSerializer, VacancyCreateSerializer,
    ChosenSerializer
)

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
    queryset = Vacancy.objects.all()
    serializer_class = VacancyCreateSerializer


class ResponseCreateView(generics.CreateAPIView):
    queryset = Response.objects.all()
    serializer_class = ResponseCreateSerializer
    # queryset = Response.objects.all()
    # serializer_class = ResponseSerializer
    # permission_classes = [IsAuthenticated]
    #
    # def perform_create(self, serializer):
    #     vacancy_id = self.request.data.get('vacancy')
    #     vacancy = Vacancy.objects.get(id=vacancy_id)
    #     serializer.save(user=self.request.user, vacancy=vacancy)


class ChosenListCreateView(generics.ListCreateAPIView):
    queryset = Chosen.objects.all()
    serializer_class = ChosenSerializer
    # permission_classes = [IsAuthenticated]

    # def perform_create(self, serializer):
    #     vacancy_id = self.request.data.get('vacancy')
    #     vacancy = Vacancy.objects.get(id=vacancy_id)
    #     serializer.save(user=self.request.user, vacancy=vacancy)
