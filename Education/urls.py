from django.urls import path
from . import views

urlpatterns = [
    path('', views.education.as_view(), name='get_education'),
]