from django.urls import path
from . import views

urlpatterns = [
    path('',views.workexperience.as_view(),name='workexperience')
]