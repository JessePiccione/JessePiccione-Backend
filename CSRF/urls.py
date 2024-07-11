from django.urls import path
from .views import CSRFView

urlpatterns = [
    path('',CSRFView.as_view())
]
