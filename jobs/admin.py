from django.contrib import admin
from .models import (
    Vacancy, Category, Industry, Chosen,
    Response, Speciality, Experience
)

admin.site.register(Vacancy)
admin.site.register(Category)
admin.site.register(Industry)
admin.site.register(Chosen)
admin.site.register(Response)
admin.site.register(Speciality)
admin.site.register(Experience)
