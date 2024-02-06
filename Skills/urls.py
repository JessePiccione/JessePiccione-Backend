from django.urls import path
from . import views

urlpatterns = [
    path('', views.skillsHandler.as_view(), name='get_skill'),
]