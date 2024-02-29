from django.shortcuts import render
from django.views import View
from .models import WorkExperience
# Create your views here.

class workexperience(View):
    def post(self, request):
        objects = WorkExperience.objects.all()
        context = {
            'objects':objects
        }
        return render(request, 'workexperience.html', context, status=200)