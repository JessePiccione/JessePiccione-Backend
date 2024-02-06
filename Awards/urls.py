from django.urls import path
from . import views 
urlpatterns = [
    path('',views.AwardHandler.as_view(), name='awardhandler'),
]