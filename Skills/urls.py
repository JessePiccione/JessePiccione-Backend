from django.urls import path
from . import views

urlpatterns = [
    path('', views.skill.as_view(), name='skill'),
    path('category/', views.skill.as_view(), name='skillcategory'),
]