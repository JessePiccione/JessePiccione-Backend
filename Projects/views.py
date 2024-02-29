from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_protect
from .models import Project

# Create your views here.
class project(View):  
    def post(self, request):
        objects = Project.objects.all()
        context={'objects': objects }
        return render(request, 'project.html', context, status=200)
