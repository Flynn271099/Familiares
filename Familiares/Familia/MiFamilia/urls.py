from django.urls import path
from MiFamilia.views import familiares

urlpatterns = [
    path('index/', familiares),
]