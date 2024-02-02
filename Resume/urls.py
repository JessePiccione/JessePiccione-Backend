from django.urls import path
from . import views
NAME_SPACE = 'resume'
urlpatterns = [
    path('',views.index, name='index'),
    path('home/',views.home, name='home' )
]