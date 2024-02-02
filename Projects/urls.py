from django.urls import path
from . import views

urlpatterns = [
    path('',views.project.as_view(), name='projects'),
]