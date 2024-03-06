from django.urls import path
from . import views 

urlpatterns = [
    path('message', views.AssistantMessageView.as_view())
]