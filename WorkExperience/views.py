from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import WorkExperience
# Create your views here.

class workexperience(View):
    def get(self, request):
        objects = WorkExperience.objects.all()
        return HttpResponse(objects)