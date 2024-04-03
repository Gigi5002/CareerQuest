from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import Response
from .models import Employer, JobSeeker
from rest_framework import generics, status
from .serializers import (
    EmployerListCreateSerializer, JobSeekerListCreateSerializer,
    ProfileEmployerSerializer, ProfileJobSeekerSerializer)
from rest_framework.views import APIView


class EmployerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Employer.objects.all()
    serializer_class = EmployerListCreateSerializer


class JobSeekerListCreateAPIView(generics.ListCreateAPIView):
    queryset = JobSeeker.objects.all()
    serializer_class = JobSeekerListCreateSerializer


class ProfileEmployerView(APIView):
    def get(self, request):
        user = Employer.objects.get(id=request.user.id)

        serializer = ProfileEmployerSerializer(user)

        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=ProfileEmployerSerializer()
    )
    def patch(self, request):
        user = Employer.objects.get(id=request.user.id)
        serializer = ProfileEmployerSerializer(instance=user, data=request.data, partial=True,
                                               context={'request': request})

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileJobSeekerView(APIView):
    def get(self, request):
        user = JobSeeker.objects.get(id=request.user.id)

        serializer = ProfileJobSeekerSerializer(user)

        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=ProfileJobSeekerSerializer()
    )
    def patch(self, request):
        user = JobSeeker.objects.get(id=request.user.id)
        serializer = ProfileJobSeekerSerializer(instance=user, data=request.data, partial=True,
                                                ontext={'request': request})

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
