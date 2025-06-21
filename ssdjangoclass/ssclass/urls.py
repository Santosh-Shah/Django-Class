from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_ssclass, name='all_ssclass'),
]