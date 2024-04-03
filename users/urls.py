from django.urls import path
from .views import (JobSeekerListCreateAPIView, EmployerListCreateAPIView,
                    ProfileJobSeekerView, ProfileEmployerView)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('employer/', EmployerListCreateAPIView.as_view()),  # для работодателя(компаниии)
    path('job_seeker/', JobSeekerListCreateAPIView.as_view()),  # для соискателей(в поисках работы)
    path('profile_employer/', ProfileEmployerView.as_view()),
    path('profile_job_seeker/', ProfileJobSeekerView.as_view())
    # path('token/refresh/', TokenRefreshView.as_view()),
    # path('token/verify/', TokenVerifyView.as_view()),
]
