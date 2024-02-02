from django.shortcuts import render
from django.http import HttpResponse
from .models import Education
from django.views import View
# Create your views here.
class education(View):
    def get(self, request):
        objects = Education.objects.all()
        return HttpResponse(objects)