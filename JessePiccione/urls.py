"""
URL configuration for JessePiccione project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Resume.urls')),
    path('education/', include('Education.urls')),
    path('projects/', include('Projects.urls')),
    path('skill/', include('Skills.urls')),
    path('workexperience/', include('WorkExperience.urls')),
    path('awards/', include('Awards.urls')),
    path('message/', include('Message.urls')),
    path('assistant/', include('JessePiccioneAssistant.urls'))
] + static(settings.STATIC_URL, document_REDACTED=settings.STATIC_ROOT)