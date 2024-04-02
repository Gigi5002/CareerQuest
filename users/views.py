from .models import Employer, JobSeeker, User, UserType
from rest_framework import generics
from .serializers import EmployerListCreateSerializer, JobSeekerListCreateSerializer
from rest_framework.views import APIView


class EmployerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Employer.objects.all()
    serializer_class = EmployerListCreateSerializer


class JobSeekerListCreateAPIView(generics.ListCreateAPIView):
    queryset = JobSeeker.objects.all()
    serializer_class = JobSeekerListCreateSerializer
