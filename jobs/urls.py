from django.urls import path

from .views import VacancyListView, ResponseCreateView, VacancyCreateView, ChosenListCreateView

urlpatterns = [
    path('vacancy_list/', VacancyListView.as_view()),
    path('vacancy_create/', VacancyCreateView.as_view()),
    path('responses_create/', ResponseCreateView.as_view()),
    path('chosen/', ChosenListCreateView.as_view())
]
