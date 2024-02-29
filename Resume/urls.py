from django.urls import path
from . import views
NAME_SPACE = 'resume'
urlpatterns = [
    path('',views.index.as_view(), name='index'),
    path('home/',views.home.as_view(), name='home'),
]